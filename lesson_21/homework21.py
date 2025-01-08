"""
HW21.1 Testing time 'heartbeat'.

The client’s monitoring system sends a signal
indicating it is operational every 30-31 seconds
for example, Timestamp 05:45:40, and in the next message — Timestamp 05:45:09
(here the heartbeat difference is 31 seconds).

There are several duplicate streams sending data simultaneously,
so we can only analyze one stream — Key TSTFEED0300|7E3E|0400.

Using automation tools, analyze the provided log: hblog.txt.
1. Filter only the lines with the specified key: Key TSTFEED0300|7E3E|0400.
2. Create a function that returns a log file analyzing
the correctness of the requirements:
- For each case where the heartbeat exceeds 31 seconds
but is less than 33 seconds, log a WARNING in the file hb_test.log.
- For each case where the heartbeat is exactly 33 seconds or more,
log an ERROR in the file hb_test.log.
3. Note: It would be helpful for error analysis
to include the time at which the error occurred.

Make sure to include the result — the hb_test.log file — in your PR.
"""

import logging
import re
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='hb_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
_log = logging.getLogger(__name__)


def parse_timestamps(filename: str):
    """Parse timestamps from the file and return a list of tuples."""
    timestamps = []
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if 'Key TSTFEED0300|7E3E|0400' in line:
                    match = re.search(r'Timestamp (\d{2}:\d{2}:\d{2})', line)
                    if match:
                        try:
                            timestamp = datetime.strptime(
                                match.group(1), '%H:%M:%S')
                            timestamps.append((line_number, timestamp))
                        except ValueError as time_err:
                            _log.error(f'''
                                Invalid time format: {line_number}: {time_err}
                            ''')
    except Exception as err:
        _log.error(f'Error while parsing timestamps: {err}')

    return timestamps


def analyze_timestamps(timestamps: list):
    """Analyze timestamps and log heartbeat delays."""
    if len(timestamps) < 2:
        _log.warning('Not enough timestamps for analysis.')
        return

    try:
        for i in range(len(timestamps) - 1):
            line_number_current, timestamp_current = timestamps[i]
            line_number_next, timestamp_next = timestamps[i + 1]
            delta = (timestamp_current - timestamp_next).total_seconds()

            if 31 < delta < 33:
                _log.warning(
                    f'Heartbeat delay detected: {delta} seconds '
                    f'at line {line_number_current} ({timestamp_current})'
                )
            elif delta >= 33:
                _log.error(
                    f'Critical heartbeat delay: {delta} seconds '
                    f'at line {line_number_current} ({timestamp_current})'
                )
    except Exception as err:
        _log.error(f'Error during analysis: {err}')


def analyze_heartbeat(filename: str):
    """Analyze the heartbeat log file."""
    try:
        timestamps = parse_timestamps(filename)
        if timestamps:
            analyze_timestamps(timestamps)
        else:
            _log.warning('No valid timestamps found for analysis.')
    except Exception as err:
        _log.critical(f'Unexpected error in analyze_heartbeat: {err}')


if __name__ == '__main__':
    analyze_heartbeat('hblog.txt')
