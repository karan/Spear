#!/usr/bin/env python

from operator import itemgetter

import click
import requests


TODAY_URL = 'http://hook-api.herokuapp.com/today'

def get_today():
  return sorted(requests.get(TODAY_URL).json()['hunts'], 
                key=lambda post: post['rank'])

@click.command()
@click.option('--num', '-n', default=1000, 
              help='Number of today\'s top products.')
def main(num):
  sorted_posts = get_today()

  click.echo()
  for post in sorted_posts[:num if num <= len(sorted_posts) else len(sorted_posts)]:
    click.secho('%d. ' % post['rank'], nl=False)
    click.secho('%s\t' % post['title'], bold=True, fg="red", nl=False)
    click.secho('%s' % post['tagline'], fg="yellow")
    click.echo()


if __name__ == '__main__':
  main()
