import argparse
import os
import datetime
import time

parser = argparse.ArgumentParser(
    prog='Patent files generator',
    allow_abbrev=True,
    description='Script for converting code '
                'into document format for subsequent licensing.'
)
parser.add_argument('-p', '--prescan', type=str, help='Pre-scan the project.', default=1)
parser.add_argument('-i', '--input', type=str, help='Input project directory.', default='D:\Projects\ironcatbot')
parser.add_argument('-o', '--output', type=str, help='Output project directory.', default='D:\Python\out')
parser.add_argument('-l', '--log', type=str, help='Log file path.', default=1)
parser.add_argument('-v', '--verbose', action='count', help='Verbose input.', default=1)
parser.add_argument('--exclude', type=str, help='Exclude file formats.')
parser.add_argument('--include', type=str, help='Include file formats.')

args = parser.parse_args()


def scan_project() -> None:
    folders = []
    files = {}
    for folder in os.walk(args.input):
        folders.append(folder)

    if args.prescan == 1:
        for folder in folders:
            for file in folder[2]:
                f_name, f_ext = os.path.splitext(file)

                if f_ext == '':
                    f_ext = 'empty extension'

                if files.get(f_ext) is None:
                    files[f_ext] = 1
                else:
                    files[f_ext] = files[f_ext] + 1

        for ext in files:
            # print(ext, files[ext], sep='\t\t\t', end='\n')
            print("{:<20}{:10d}".format(ext, files[ext]))

    # print(folders)


def logging(string) -> None:
    now = datetime.datetime.now()
    log_date_format = '%d-%m-%Y %H:%M:%S'

    if args.log == 1:
        log = open(args.output + '\\' + 'patent_gen.log', 'a+')
        log.write(str(now.strftime(log_date_format)) + ' ' + string + '\n')
        log.close()


def prepare():
    if args.input == '':
        print('Enter the path to the project...')
        args.input = input()
        print('Path to the project: %s' % args.input)
    if args.output == '':
        print('Enter path to output files...')
        args.output = input()
        print('Path to output files: %s' % args.output)
    # print(args)


def run():
    # TODO delete start_time
    start_time = time.time()

    print('Running the project file converter...')
    prepare()
    scan_project()
    # TODO delete print end_time
    print("--- %s seconds ---" % (time.time() - start_time))

    print('End.')
    exit(0)


if __name__ == '__main__':
    run()
    # generator.run()
