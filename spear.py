#!/usr/bin/env python

from operator import itemgetter
import pickle
import webbrowser

import click
import requests

BASE_URL = 'http://www.producthunt.com'
TODAY_URL = 'http://hook-api.herokuapp.com/today'


def save_posts(obj):
  with open('posts.pkl', 'wb') as f:
    pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_posts():
  with open('posts.pkl', 'r') as f:
    return pickle.load(f)

def get_today():
  return sorted(requests.get(TODAY_URL).json()['hunts'], 
                key=lambda post: post['rank'])


@click.command()
@click.option('--num', '-n', default=1000, 
              help='Number of today\'s top products.')
@click.argument('rank', nargs=1, required=False)
def main(num, rank):
  """A CLI to Product Hunt."""
  posts = get_today()

  click.echo()
  for post in posts[:num if num <= len(posts) else len(posts)]:
    click.secho('%d. ' % post['rank'], nl=False)
    click.secho('%s\t' % post['title'], bold=True, fg="red", nl=False)
    click.secho('%s' % post['tagline'], fg="yellow")
    click.echo()

  save_posts(posts)
  if rank:
    posts = load_posts()
    url = BASE_URL + posts[int(rank)-1]['permalink']
    webbrowser.open(url, new=2)

if __name__ == '__main__':
  main()
