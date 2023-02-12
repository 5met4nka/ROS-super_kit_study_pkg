#!/usr/bin/env python3
import time
import datetime

def main():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        time.sleep(5)

if __name__ == "__main__":
    main()
