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
  
  if rank > len(posts):
    click.secho(('\n\tCannot get that rank. Currently %d products have been hunted '
                  'with Spear.\n' % len(posts)), fg="red")
    return

  url = BASE_URL + posts[int(rank)-1]['permalink']
  webbrowser.open(url, new=2)

def print_posts(posts):
  """Neatly prints all passed posts to the console."""

  click.echo()
  for post in posts:
    click.secho('%d. ' % post['rank'], nl=False)
    click.secho('%s\t' % post['title'], bold=True, fg="red", nl=False)
    click.secho('%s' % post['tagline'], fg="yellow")
    click.echo()


@click.command()
@click.option('--num', '-n', default=1000, 
              help='Number of today\'s top products.')
@click.argument('rank', nargs=1, required=False)
def main(num, rank):
  """A CLI to Product Hunt that shows (top num) products from today
  and/or open the product at rank rank in web browser."""

  file_existed = os.path.isfile(FILE_NAME)

  if rank:
    rank = int(rank)
  
  # if a rank is passed, we assume the user wants to open the product at the
  # rank. But if the local file doesn't exist, we query the API, and retry.
  if rank and file_existed:
    browse_rank(load_posts(), rank)
  else:
    posts = get_todays_posts()
    end_index = num if num <= len(posts) else len(posts)
    posts = posts[:end_index]

    if not rank:
      print_posts(posts)

    save_posts(posts)
    
    if rank:
      # rank was passed, and url could not be opened in first try
      browse_rank(load_posts(), rank)

if __name__ == '__main__':
  main()
