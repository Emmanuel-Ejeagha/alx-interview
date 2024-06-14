#!/usr/bin/python3

"""Module that finds the minium operation"""


def minOperations(n):
    """Find the minimum number of operation"""
    # current_text_count = 1
    CTC = 1
    COPY_ALL = 0
    count_op = 0

    while CTC < n:
        # if n is divisible by the CTC count, then we should copy and paste it
        # There cannot be two copy_all
        # but there can be more than one paste at a time
        if n % CTC == 0:
            COPY_ALL = CTC
            count_op += 1

        CTC += COPY_ALL
        count_op += 1
    if CTC > n:
        return 0
    return count_op
