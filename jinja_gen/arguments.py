import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(description='Jinja Generator',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f', '--file', type=str,
                        metavar='', help='Path to the YAML file containing all configurations',
                        required=True)
    parser.add_argument('-o', '--output-dir', type=str,
                        metavar='',
                        help='Output directory for generated configurations')
    parser.add_argument('--dry', action='store_true', default=False,
                        help='A dry run showing files to be generated')
    parser.add_argument('-k', '--output-name-key', type=str, default='name',
                        metavar='', help='An extra key identifier populated for template with name')
    parser.add_argument('-d', '--output-dir-key', type=str, default='dir',
                        metavar='',
                        help='An extra key identifier populated for template with output directory')
    args = parser.parse_args()

    # Make file path absolute
    args.file = os.path.abspath(args.file)

    # If output dir not given, store in the same folder as the YAML file
    if not args.output_dir:
        args.output_dir = os.path.join(
            os.path.dirname(args.file),
            os.path.splitext(os.path.basename(args.file))[0]
        )

    # If path is relative, then output relative to the config file with the same folder name
    if not os.path.isabs(args.output_dir):
        args.output_dir = os.path.join(os.path.dirname(args.file), args.output_dir)

    return args
