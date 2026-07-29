from datetime import date
import sys
import inflect

p = inflect.engine()



def main():
    dob_input = input("Date of Birth: ")
    dob = parse_date(dob_input)

    minutes = calculate_minutes(dob, date.today())

    print(format_words(minutes))

def parse_date(date_str):
    """Parses a date string in YYYY-MM-DD format into a date object."""
    try:
         return date.fromisoformat(date_str)
    except ValueError:
         sys.exit("Invalid date")

def calculate_minutes(birth_date, today_date):
     """Calculates the total minutes between two date objects."""
     delta = today_date - birth_date

     return delta.days * 24 * 60

def format_words(minutes):
     """Converts a number of minutes into English words without 'and'."""
     words = p.number_to_words(minutes, andword="")

     return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()

