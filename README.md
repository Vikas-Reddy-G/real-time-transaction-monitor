# Real-time Transaction Monitoring Simulator

This project simulates a stream of financial transactions in real-time and flags suspicious activity based on simple rules.

## Features

- Generates fake transactions with random amount, timestamp, and device country.
- Flags transactions that:
  - Have very high amount (>$3000)
  - Occur during odd hours (before 6 AM or after 10 PM)
  - Originate from foreign devices (outside US, IN, UK)
- Outputs alerts to console in real-time.

## Requirements

- Python 3.x

## How to Run

1. Clone the repo or download the code.
2. Run the simulator script:

```bash
python src/simulator.py
