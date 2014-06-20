#!/usr/bin/env python

from operator import itemgetter
import os
import pickle
import webbrowser

import click
import requests

BASE_URL = 'http://www.producthunt.com'
TODAY_URL = 'http://hook-api.herokuapp.com/today'
FILE_NAME = 'posts.pkl'

def save_posts(posts):
  """Saves the passed posts object in a file."""

  with open(FILE_NAME, 'wb') as f:
    pickle.dump(posts, f, pickle.HIGHEST_PROTOCOL)

def load_posts():
  """Reads and returns the saved posts from file."""
  
  with open(FILE_NAME, 'r') as f:
    return pickle.load(f)

def get_todays_posts():
  """Queries the Product Hunt API, sorts and returns the list of posts."""
  
  return sorted(requests.get(TODAY_URL).json()['hunts'], 
                key=lambda post: post['rank'])


def browse_rank(posts, rank):
  """Opens the permalink for post at rank rank in default browser."""
  url = BASE_URL + posts[int(rank)-1]['permalink']
  webbrowser.open(url, new=2)


@click.command()
@click.option('--num', '-n', default=1000, 
              help='Number of today\'s top products.')
@click.argument('rank', nargs=1, required=False)
def main(num, rank):
  """A CLI to Product Hunt that shows (top num) products from today
  and/or open the product at rank rank in web browser.

  Once posts are grabbed from the API, they are saved in a file for consistency
  within a session."""

  file_existed = os.path.isfile(FILE_NAME)
  
  # if a rank is passed, we assume the user wants to open the product at the
  # rank. But if the local file doesn't exist, we query the API, and retry.
  if rank and file_existed:
    browse_rank(load_posts(), rank)
  else:
    posts = get_todays_posts()

    if not rank:
      click.echo()
      for post in posts[:num if num <= len(posts) else len(posts)]:
        click.secho('%d. ' % post['rank'], nl=False)
        click.secho('%s\t' % post['title'], bold=True, fg="red", nl=False)
        click.secho('%s' % post['tagline'], fg="yellow")
        click.echo()

    save_posts(posts)

    if rank:
      # this will be executed only if rank is passed, but no file was
      # initially found
      browse_rank(load_posts(), rank)

if __name__ == '__main__':
  main()
