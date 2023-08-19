# Challenge 1: Converting 12-hour time to 24-hour time.

def convert_time_system(hour, minute, period):
    try:
        # Check if the given period is "am" or "pm".
        if period.lower() == "am":
            # Check if hour and minute are within valid ranges.
            if hour < 1 or hour > 12 or minute < 0 or minute > 59:
                print("Invalid Hour or Minute")
            # Convert and format hour to 24-hour format.
            elif hour < 10:
                print(f"0{hour}{minute:00} hours")
            elif hour == 12:
                print(f"00{minute:00} hours")
        elif period.lower() == "pm":
            # Check if hour and minute are within valid ranges.
            if hour < 1 or hour > 12 or minute < 0 or minute > 59:
                print("Invalid Hour or Minute")
            # Convert and format hour to 24-hour format.
            elif hour < 12:
                print(f"{hour + 12}{minute:00} hours")
            else:
                print(f"{hour}{minute:00} hours")
        else:
            # Invalid period input.
            print("Invalid period")
    except TypeError:
        # Handle the case where hour or minute are not numbers.
        print("Hour or Minute should be numbers")
    except AttributeError:
        # Handle error when period is not a string
        print("Period should be a string of either am or pm")
