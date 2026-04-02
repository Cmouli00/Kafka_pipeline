#!/bin/bash
set -e

# start infra + producer
python pipeline.py

# replace consumer logic
cp /app/../solution/fix_pipeline.py /app/consumer.py

# rerun consumer
python consumer.py