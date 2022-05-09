"""Basic Python script showing importing of external libraries
and running a job on an interval. This also can be done with
asyncio.
"""
import time
import json

import requests


def main():
    print("Running basic python function")
    while True:
        r = requests.get('https://www.google.com')
        print(r)
        print(r.content)
        time.sleep(10)


if __name__ == '__main__':
    main()
