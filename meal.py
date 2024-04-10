# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
# implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
# If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.


def main():
    time = input("what time is it? ")
    formatted_time = convert(time)

    if formatted_time >= 7 and formatted_time <= 8:
        print("breakfast time")
    elif formatted_time >= 12 and formatted_time <= 13:
        print("lunch time")
    elif formatted_time >= 18 and formatted_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours_int, mins_int = int(hours), int(minutes)

    time_float = hours_int + mins_int / 60
    return time_float


if __name__ == "__main__":
    main()
