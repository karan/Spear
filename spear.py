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
    click.secho('%d - ' % post['rank'], nl=False)
    click.secho('%s - ' % post['title'], bold=True, fg="red", nl=False)
    click.secho('%s' % post['tagline'], fg="yellow")


if __name__ == '__main__':
  main()
