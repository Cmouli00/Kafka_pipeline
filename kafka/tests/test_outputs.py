import json
import os

def test_output_exists():
    assert os.path.exists("/app/output.json")

def test_no_duplicates():
    with open("/app/output.json") as f:
        data = json.load(f)

    ids = [x["id"] for x in data]
    assert len(ids) == len(set(ids))

def test_all_records_present():
    with open("/app/output.json") as f:
        data = json.load(f)

    ids = set(x["id"] for x in data)
    assert ids == {1, 2, 3, 4, 5}

def test_sorted():
    with open("/app/output.json") as f:
        data = json.load(f)

    ids = [x["id"] for x in data]
    assert ids == sorted(ids)