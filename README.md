# Python Teamwork Time Entry

This project facilitates the entry of time into your teamwork domain through teamwork's api.
Contains a helper that takes a path to a csv file containing daily time entries and sends it to teamwork through it's api.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 2.7 and pip

### Installing

```
pip install -r requirements.txt
```

### Example

data
```
description,date,time,hours,minutes,task_id
"Test ing",2018222,10:10,2,0,55555777
"Test ing-2",2018222,12:10,7,0,44444777
```

Usage:
```
python time_entry/runner.py --file data/time_entry.csv --user_id [your_id] --token [your_token] --domain [your_domain] --dry_run
```
dry_run option will enable you to test your file and what will be run before sending it to your teamwork domain.

Enjoy! :O

## Authors

* **Ariel Luguern** - *Most work* - [aluguern](https://github.com/aluguern)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
