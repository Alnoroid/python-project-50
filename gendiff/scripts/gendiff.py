import argparse

from gendiff import generate_diff

parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.',
    argument_default=argparse.SUPPRESS
)

parser._optionals.title = 'optional arguments'

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
        '-f', '--format', default='stylish',
        help='set format of output'
    )

args = parser.parse_args()


def main():
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
