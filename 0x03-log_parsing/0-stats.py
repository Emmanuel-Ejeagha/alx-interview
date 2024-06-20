#!/usr/bin/python3

"""Module that reads stdin line by line and computes metrics


"""
import sys


def print_statistics(size, status):
    """Prints the statistics based on the current state"""

    print("File size: {:d}".format(size))
    for k, v in sorted(status.items()):
        if v > 0:
            print("{}: {:d}".format(k, v))


def my_main():
    """The function that will solve the problem"""

    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
    size = 0
    count = 0
    string = ""
    try:
        for line in sys.stdin:
            line = line.strip()
            line_split = line.split()
            try:
                file_size = int(line_split[-1])
                status_code = line_split[-2]
                if status_code in status:
                    status[status_code] += 1
                else:
                    raise Exception
            except ValueError:
                continue
            except Exception:
                size += file_size
                continue
            size += file_size
            count += 1
            if count % 10 == 0:
                print_statistics(size, status)
    finally:
        print_statistics(size, status)


if __name__ == '__main__':
    my_main()
