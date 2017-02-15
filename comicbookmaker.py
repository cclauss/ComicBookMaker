#! /usr/bin/python3
# vim: set expandtab tabstop=4 shiftwidth=4 :
"""Module to retrieve webcomics and create ebooks"""

import book
import argparse
import logging
from comics import COMIC_NAMES


def get_file_content_until_tag(path, tag):
    """Get content from a filepath up to a given tag.
    If tag is not is the file, an exception is thrown."""
    content = []
    with open(path) as f:
        for l in f:
            content.append(l)
            if tag == l.strip():
                return content
    raise ValueError('Could not find "%s" in file "%s"' % (tag, path))


def add_new_lines_after_tag(path, new_lines, tag):
    """Add lines to file from a given tag.
    All content until tag is kept, all content after is lost."""
    content = get_file_content_until_tag(path, tag)
    with open(path, 'w') as f:
        f.write(''.join(content + new_lines))


def main():
    """Main function"""
    logger = logging.getLogger()
    comic_names = sorted(COMIC_NAMES.keys())
    parser = argparse.ArgumentParser(
        description='Downloads webcomics and generates ebooks for offline reading')
    parser.add_argument(
        '--comic', '-c',
        action='append',
        help=('comics to be considered (default: ALL)'),
        choices=comic_names,
        default=[])
    parser.add_argument(
        '--excluded', '-e',
        action='append',
        help=('comics to be excluded'),
        choices=comic_names,
        default=[])
    parser.add_argument(
        '--action', '-a',
        action='append',
        help=('actions required'),
        default=[])
    parser.add_argument(
        '--loglevel', '-l',
        type=int,
        action='store',
        help=('log level (as per the Python logging module)'),
        default=logging.CRITICAL)
    args = parser.parse_args()
    logger.setLevel(args.loglevel)
    if not args.comic:
        args.comic = comic_names
    if not args.action:
        args.action = ['update']
    comic_classes = [COMIC_NAMES[c] for c in sorted(set(args.comic) - set(args.excluded))]
    logging.debug('Starting')
    for action in args.action:
        if action == 'book':
            book.make_book(comic_classes)
        elif action == 'update':
            for com in comic_classes:
                com.update()
        elif action == 'info':
            for com in comic_classes:
                com.info()
        elif action == 'gitignore':
            path = '.gitignore'
            new_content = [com.gitignore() for com in comic_classes]
            add_new_lines_after_tag(path, new_content, '# Generated folders')
        elif action == 'readme':
            path = 'README.md'
            new_content = [com.readme() for com in comic_classes]
            add_new_lines_after_tag(path, new_content, '----------------')
        elif action == 'check':
            for com in comic_classes:
                com.check_everything_is_ok()
        elif action == 'fix':
            for com in comic_classes:
                com.try_to_get_missing_resources()
        elif action == 'reset_new':
            for com in comic_classes:
                com.reset_new()
        elif action == 'delete_last':
            for com in comic_classes:
                com.delete_last()
        else:
            print("Unknown action : %s" % action)

if __name__ == "__main__":
    main()
