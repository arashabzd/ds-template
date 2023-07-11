import argparse
import logging
import sys

import package

logging.basicConfig(
    level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)


def main(args):
    logger.info(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Description of your script")

    parser.add_argument("-f", "--file", help="File argument")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    try:
        main(args)
        sys.exit(0)
    except Exception:
        sys.exit(1)
