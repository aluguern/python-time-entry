#!/usr/bin/env python
"""
This script takes a path to a csv file containing
daily time entries and sends it to teamwork through it's api.
"""
from __future__ import print_function
import argparse
from teamwork import time_entry_manager


__author__ = "Ariel Luguern"
__copyright__ = "Copyright 2019, Sqrt3"
__credits__ = ["Ariel Luguern"]
__maintainer__ = "Ariel Luguern"
__email__ = "aluguern@hotmail.com"
__status__ = "Development"


def main(domain, file, user_id, token, dry_run):
    manager = time_entry_manager.TimeEntryManager(domain, file, user_id, token)
    manager.send(dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This script takes a path to a csv file"
        "containing daily time entries and sends it to teamwork.")
    parser.add_argument(
        "-d", "--domain",
        help="Teamwork domain.",
        type=str,
        required=True)
    parser.add_argument(
        "-f", "--file",
        help="Path to csv file (default is ./time_entry.csv)",
        default="time_entry.csv",
        type=str,
        required=False)
    parser.add_argument(
        "-u", "--user_id",
        help="User id whose time is logged.",
        type=str,
        required=True)
    parser.add_argument(
        "-t", "--token",
        help="Api token for teamwork calls yo.",
        type=str,
        required=True)
    parser.add_argument(
        "--dry_run",
        help="Outputs the result of what the execution would be.",
        action="store_true")
    args = parser.parse_args()

    main(args.domain, args.file, args.user_id, args.token, args.dry_run)
