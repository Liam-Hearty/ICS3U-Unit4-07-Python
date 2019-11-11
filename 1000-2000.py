#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program uses a loop inside another loop.


def main():
    # this function uses a nested loop

    counter = 0

    # process & output
    for numbers in range(1000, 2001):
        counter += 1
        if counter % 5 == 0:
            print("{} ".format(numbers))
        else:
            print("{} ".format(numbers), end="")


if __name__ == "__main__":
    main()
