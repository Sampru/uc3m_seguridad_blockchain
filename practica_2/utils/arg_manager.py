import argparse

from utils.constants import *
from utils.file_manager import check_file


class ArgumentError(BaseException):
    """Error raised when any argument is missing"""
    pass


class UnsupportedOperationError(BaseException):
    """Error raised when the operation is not implemented yet"""
    pass


def parse_args():
    """Creates a help message, and parses the arguments"""
    parser = argparse.ArgumentParser(description=text_description)
    parser.add_argument('-m', '--mode', choices=['cs', 'ds', 'h', 'vh', 'ca', 'da', 'cert', 'ts', 'tsv'], type=str,
                        required=True, help=text_help_mode, metavar='modo')
    parser.add_argument('-p', '--password', type=str, required=False, help=text_help_password, metavar=text_metavar_password)
    parser.add_argument('-i', '--input', type=str, required=True, help=text_help_input, metavar=text_metavar_path)
    parser.add_argument('-ad', '--additional-input', type=str, required=False, help=text_help_add, metavar=text_metavar_path)
    parser.add_argument('-o', '--output', type=str, required=False, help=text_help_output, metavar=text_metavar_path)
    return parser.parse_args()


def check_args(args):
    """Check if the hole set of arguments is provided, and its validity depending on the mode argument"""
    # argparse ensures that mode will be a well formed argument
    mode = args.mode

    # Input file must be checked
    if not check_file(args.input):
        raise FileNotFoundError

    # For every mode, a check of parameters is done
    # If any is missing, or the operation is unsupported, an error will be risen
    if mode in ['cs', 'ds']:
        if args.password is None or args.output is None:
            raise ArgumentError(text_error_incorrect_arguments)
    elif mode == 'h':
        if args.output is None:
            raise ArgumentError(text_error_incorrect_arguments)
    elif mode == 'ca':
        if args.output is None:
            raise ArgumentError(text_error_incorrect_arguments)
    elif mode in ['vh', 'da']:
        if args.additional_input is None:
            raise ArgumentError(text_error_incorrect_arguments)
        if check_file(args.additional_input):
            raise FileNotFoundError
    # TODO: extra points
    elif mode == 'cert':
        raise UnsupportedOperationError(text_error_unsupported_operation)
    elif mode == 'ts':
        raise UnsupportedOperationError(text_error_unsupported_operation)
    elif mode == 'tsv':
        raise UnsupportedOperationError(text_error_unsupported_operation)

