### This file generates a json file with the following format (same as `test.json`):
# {
#   "session_id": "1234567890",
#   "market_id": "412a-1234-1234-1234-1234567890",
#   "market_name": "Market Name",
#   "order_id": "412a-1234-1234-1234-1234567890",
#   "loan_amount": 1200000,
#   "loan_term": 30,
#   "loan_fee_rate": 0.05,
#   "loan_fee_amount": 60000,
#   "loan_date": "2018-01-01",
#   "loan_due_date": "2018-02-01"
# }

import json
import random
import string
import datetime

def random_string(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def random_date(start, end):
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def random_int(start, end):
    return random.randint(start, end)

def random_float(start, end):
    return random.uniform(start, end)

def random_bool():
    return random.choice([True, False])

def random_list(start, end, length):
    return [random_int(start, end) for i in range(length)]

def random_dict(start, end, length):
    return {random_string(): random_int(start, end) for i in range(length)}

def random_json():
    return {
        "session_id": random_string(),
        "market_id": random_string(),
        "market_name": random_string(),
        "order_id": random_string(),
        "loan_amount": random_int(100000, 1000000),
        "loan_term": random_int(1, 30),
        "loan_fee_rate": random_float(0.01, 0.1),
        "loan_fee_amount": random_int(10000, 100000),
        "loan_date": str(random_date(datetime.datetime(2018, 1, 1), datetime.datetime(2018, 12, 31))),
        "loan_due_date": str(random_date(datetime.datetime(2018, 1, 1), datetime.datetime(2018, 12, 31))),
    }

# Now we generate a hundred of random json files under /sample directory
for i in range(1000):
    with open(f"./sample/test{i}.json", "w") as f:
        json.dump(random_json(), f)
