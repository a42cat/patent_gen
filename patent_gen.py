import argparse
import os

parser = argparse.ArgumentParser(
    prog='Patent files generator',
    allow_abbrev=True,
    description='Script for converting code '
                'into document format for subsequent licensing.'
)
parser.add_argument('-p', '--prescan', type=str, help='Pre-scan the project.')
parser.add_argument('-i', '--input', type=str, help='Input project directory.', default='')
parser.add_argument('-o', '--output', type=str, help='Output project directory.', default='')
parser.add_argument('-l', '--log', type=str, help='Log file path.', default=False)
parser.add_argument('-v', '--verbose', action='count', help='Verbose input.', default=1)
parser.add_argument('--exclude', type=str, help='Exclude file formats.')
parser.add_argument('--include', type=str, help='Include file formats.')

args = parser.parse_args()


def scan_project() -> None:

    folders = []
    for i in os.walk(args.input):
        folders.append(i)
    print(folders)


def prepare():
    if args.input == '':
        print('Enter the path to the project...')
        args.input = input()
        print('Path to the project: %s' % args.input)
    if args.output == '':
        print('Enter path to output files...')
        args.output = input()
        print('Path to output files: %s' % args.output)
    print(args)


def run():
    print('Running the project file converter...')
    prepare()
    #scan_project()
    print('End.')
    exit(0)


if __name__ == '__main__':
    run()
    # generator.run()
