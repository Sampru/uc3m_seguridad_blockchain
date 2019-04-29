import logging  # For logs

from functional.cipher import *
from functional.hasher import *
from functional.signer import *
from utils.arg_manager import *

"""Supported operations switch"""
chooser = {'cs': encrypt, 'ds': decrypt,
           'h': get_hash, 'vh': check_hash,
           'ca': sign, 'da': check_sign}


def main():
    """Main function
    Parses the arguments and calls the requested function.
    """
    args = parse_args()
    try:
        # check_args will check if the program should continue. It will raise an error if not
        check_args(args)
        # Order exectuion
        chooser.get(args.mode)(args)
    except (UnsupportedOperationError, ArgumentError) as e:
        logging.warning(e)


if __name__ == "__main__":
    main()
