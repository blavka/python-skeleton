#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import click_log
import logging
import sys

__version__ = '0.0.0'


@click.command()
@click.version_option(version=__version__)
@click_log.simple_verbosity_option(default='INFO')
def cli():
    '''Skeleton.'''
    logging.info('Process started')
    logging.info('Process stopped')


def main():
    try:
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
        cli()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        click.echo(str(e), err=True)
        if "DEBUG" in sys.argv:
            raise e
        sys.exit(1)


if __name__ == '__main__':
    main()
