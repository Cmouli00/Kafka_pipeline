## Objective

You are given a data pipeline that uses Kafka to process user events.

The system consists of:
- A producer that sends events
- A consumer that processes events and writes to a file

Currently, the system produces incorrect results:
- Duplicate records appear
- Some records may be missing
- Output ordering is inconsistent

## Your Goal

Fix the system so that:

- `/app/output.json` is created
- All records are processed exactly once
- No duplicate records exist
- No records are missing
- Output is sorted by `id`
- Output is deterministic across runs

## Constraints

- You may modify any files inside `/app/`
- Do not hardcode outputs
- Do not remove Kafka usage