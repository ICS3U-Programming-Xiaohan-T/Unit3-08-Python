#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: Apr 2 2025
# This program is to determine wether the year is a leap year or not.


def main():
    # Get user input for the year as an string
    year_as_string = input("Please enter a year: ")
    try:
        # Casting the string into integer
        year = int(year_as_string)
        # Determine if the year is divisible by 4
        if year % 4 == 0:
            # If so, see if the year is divisible by 100.
            if year % 100 == 0:
                # If so, see if the year is divisible by 400.
                if year % 400 == 0:
                    # Display the output that it is a leap year
                    print("{} is a leap year!".format(year))
                else:
                    # If is not divisible, display the output that it is not a leap year
                    print("{} is not a leap year.".format(year))
            else:
                # If not divisible by 100, display that the year is a leap year
                print("{} is a leap year!".format(year))
        else:
            # If the year is not divisible by 4, display the output that is not a leap year
            print("{} is not a leap year.".format(year))
    except Exception:
        # Exceptions where enter an invalid input
        print("Incorrect input, enter an integer")


if __name__ == "__main__":
    main()
