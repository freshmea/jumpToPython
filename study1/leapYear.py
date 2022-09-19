# leapYear.py

if __name__ == "__main__":

    year = int(input())
    if year % 4 == 0 and year % 100 != 100 or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is a ordinary year")