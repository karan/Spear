#!/usr/bin/env python

import click
import requests


TODAY_URL = 'http://hook-api.herokuapp.com/today'

def get_today():
  return requests.get(TODAY_URL).json()['hunts']

@click.command()
@click.option('--num', '-n', default=10, help='Number of top products.')
def main(num):
  posts = get_today()
  sorted_posts = sorted(posts, key=lambda post: post['rank'])

  for post in posts:
    click.echo('%d - %s - %s - %s comments' % (post['rank'], post['title'], post['tagline'], post['comment_count']))


if __name__ == '__main__':
  main()
