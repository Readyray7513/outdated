from datetime import datetime

# Function to convert a month name to its corresponding number (1-12)
def month_to_number(month):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    try:
        # Find the index of the month in the list and add 1 (since list indices start at 0)
        return months.index(month.capitalize()) + 1
    except ValueError:
        # If the month name is not found, return None (invalid month)
        return None

# Function to clean the day by removing any non-digit characters (e.g., "st", "nd", "rd", "th")
def clean_day(day):
    return ''.join([char for char in day if char.isdigit()])

# Main function to rearrange and validate the date
def rearrange_date(date_input):
    # Step 1: Normalize the input by stripping leading/trailing whitespace
    date_input = date_input.strip()
    
    # Step 2: Check if the input contains slashes (e.g., "9/8/1636")
    if '/' in date_input:
        # Split the input by slashes
        parts = date_input.split('/')
        # Ensure there are exactly 3 parts (month, day, year)
        if len(parts) != 3:
            return "Invalid format"
        # Check if any part is a month name (e.g., "September/8/1636" is invalid)
        for part in parts:
            if month_to_number(part) is not None:
                return "Invalid format"
        # Try to parse the date in MM/DD/YYYY format
        try:
            parsed_date = datetime.strptime(date_input, "%m/%d/%Y")
            return parsed_date.strftime("%Y-%m-%d")  # Return in ISO 8601 format
        except ValueError:
            # If parsing fails, the date is invalid
            return "Invalid date"
    else:
        # Step 3: Handle inputs without slashes (e.g., "September 8, 1636")
        # Check if the input contains a comma (required for "Month Day, Year" format)
        if ',' not in date_input:
            # If no comma, check if the input contains a month name
            parts = date_input.split()
            for part in parts:
                if month_to_number(part) is not None:
                    # If a month name is found but no comma, the format is invalid
                    return "Invalid format"
            # If no month name is found, the format is invalid
            return "Invalid format"
        
        # Step 4: Split the input by the comma to separate "Month Day" and "Year"
        parts = date_input.split(',')
        if len(parts) != 2:
            return "Invalid format"
        before_comma, year_part = parts
        # Strip any extra whitespace from the parts
        before_comma = before_comma.strip()
        year_part = year_part.strip()
        
        # Step 5: Split the part before the comma into "Month" and "Day"
        date_parts = before_comma.split()
        if len(date_parts) != 2:
            return "Invalid format"
        month_part, day_part = date_parts
        
        # Step 6: Convert the month name to a number
        month = month_to_number(month_part)
        if month is None:
            return "Invalid format"
        
        # Step 7: Clean the day by removing any suffixes (e.g., "1st" -> "1")
        day_str = clean_day(day_part)
        if not day_str.isdigit():
            return "Invalid format"
        day = int(day_str)
        
        # Step 8: Validate the year
        if not year_part.isdigit():
            return "Invalid format"
        year = int(year_part)
        
        # Step 9: Validate the date using the datetime module
        try:
            parsed_date = datetime(year, month, day)
            return parsed_date.strftime("%Y-%m-%d")  # Return in ISO 8601 format
        except ValueError:
            # If the date is invalid (e.g., February 30), return "Invalid date"
            return "Invalid date"

# Main loop to repeatedly prompt the user for a date until a valid one is entered
while True:
    date_input = input("Enter a date: ")
    result = rearrange_date(date_input)
    if result not in ("Invalid format", "Invalid date"):
        print(result)
        break
    else:
        print("Invalid format. Please try again.")