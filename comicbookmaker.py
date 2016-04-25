#! /usr/bin/python3
# vim: set expandtab tabstop=4 shiftwidth=4 :
"""Module to retrieve webcomics and create ebooks"""

import book
import argparse
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


def main():
    """Main function"""
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
    args = parser.parse_args()
    if not args.comic:
        args.comic = comic_names
    if not args.action:
        args.action = ['update']
    comic_classes = [COMIC_NAMES[c] for c in sorted(set(args.comic) - set(args.excluded))]
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
            content = get_file_content_until_tag(path, '# Generated folders')
            with open(path, 'w') as f:
                f.write(''.join(content))
                for com in comic_classes:
                    com.gitignore(f)
        elif action == 'readme':
            path = 'README.md'
            content = get_file_content_until_tag(path, '----------------')
            with open(path, 'w') as f:
                f.write(''.join(content))
                for com in comic_classes:
                    com.readme(f)
        elif action == 'check':
            for com in comic_classes:
                com.check_everything_is_ok()
        elif action == 'fix':
            for com in comic_classes:
                com.try_to_get_missing_resources()
        elif action == 'reset_new':
            for com in comic_classes:
                com.reset_new()
        else:
            print("Unknown action : %s" % action)

if __name__ == "__main__":
    main()
