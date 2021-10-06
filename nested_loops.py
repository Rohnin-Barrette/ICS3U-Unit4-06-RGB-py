#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# this program uses nested loops


def main():
    # this program uses nested loops
    # this is to keep track of how many times you go through the loop
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("({0},{1},{2})".format(counter3, counter2, counter1))

    print("Done.")


if __name__ == "__main__":
    main()
