import argparse


def parsing_definition():
    parser = argparse.ArgumentParser(
        description='Create and Search Text Notes')
    parser.add_argument('-ff', '--filefolder', dest='create_file_folder',
                        help='defines that will be created a file and folder',
                        action='store_true')
    parser.add_argument('-fi', '--file', dest='create_file',
                        help='defines that will be created a file.',
                        action='store_true')
    parser.add_argument('-fo', '--folder', dest='create_folder',
                        help='defines that will be created a folder.',
                        action='store_true')
    parser.add_argument('name', type=str,
                        help='set the name of the ' +
                        'folder or initial Note file.',
                        action='store')
    args = parser.parse_args()

    return args


def arg_routing():
    args = parsing_definition()
    if args.create_file_folder:
        print(f"Creating folder and File by the name of: {args.name}")
    if args.create_file:
        print(f"Creating File by the name of: {args.name}")
    if args.create_folder:
        print(f"Creating Folder by the name of: {args.name}")
