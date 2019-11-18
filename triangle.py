#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: november 2019
# This show two functions


def calculate_area(base, height):
    # process
    area = (base*height)/2
    print("The area is {0}".format(area))


def main():
    while True:
        base_user_string = input("Enter the base of the traingle: (integer) ")
        height_user_string = input("Enter the height of the traingle: \
                                   (integer) ")
        try:
            base_user_int = int(base_user_string)
            height_user_int = int(height_user_string)

            calculate_area(base_user_int, height_user_int)
            break
        except Exception:
            print("that is an invalid integer")


if __name__ == "__main__":
    main()
