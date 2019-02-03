"""
TimeEntryManager:
    Helper to manage sending time entries through teamwork's api.
"""
from __future__ import print_function
import requests
import csv
import sys
import json


__author__ = "Ariel Luguern"
__copyright__ = "Copyright 2019, Sqrt3"
__credits__ = ["Ariel Luguern"]
__maintainer__ = "Ariel Luguern"
__email__ = "aluguern@hotmail.com"
__status__ = "Development"


TEAMWORK_BASE_URL = 'https://{}.teamwork.com/tasks/{}/time_entries.json'


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n\n{}'.format(
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))


class TimeEntryManager(object):
    """TimeEntryManager:
        Helper to manage sending time entries through teamwork's api.

    Attributes:
        __domain  : Teamwork domain.
        __file    : Path to csv file.
        __user_id : User id whose time is logged.
        __token   : teamwork api token.
    """

    def __init__(self, domain, file, user_id, token):
        self.__domain = domain
        self.__file = file
        self.__user_id = user_id
        self.__token = token

    def send(self, dry_run=False):
        with open(self.__file) as csvfile:
            reader = csv.DictReader(csvfile)
            for counter, row in enumerate(reader):
                time_entry = self.csv_to_json(row)
                res = self.post_time_entry(time_entry,
                                           row['task_id'], dry_run)
                if not res.ok:
                    eprint("Something went wrong [{}] for reasons [{}]".format(
                        res, res.text))
                elif dry_run is False:
                    print("Success sending time-entry [{}]".format(counter))

    def csv_to_json(self, row):
        return {
            "description": row['description'],
            "person-id": self.__user_id,
            "date": str(row['date']),
            "time": str(row['time']),
            "hours": str(row['hours']),
            "minutes": str(row['minutes'])
        }

    def post_time_entry(self, payload, task_id, dry_run=False):
        headers = {
            'Content-Type': 'application/json',
        }
        url = TEAMWORK_BASE_URL.format(self.__domain, task_id)
        data = json.dumps({"time-entry": payload})

        req = requests.Request('POST', url,
                               data=data,
                               headers=headers,
                               auth=(self.__token, "xxx"))
        prepared = req.prepare()

        if dry_run is True:
            pretty_print_POST(prepared)
            return requests.Response()
        s = requests.Session()
        res = s.send(prepared)
        return res
