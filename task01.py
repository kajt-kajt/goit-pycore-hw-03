from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculate number of days from today till the given date.

    If given date is in future, negative number is returned.
    If input string does not match format, None is returned.

    Parameters: 
        date (str): some date in format "YYYY-MM-DD" (f.e., "2020-10-09")
    
    Returns: 
        int: number of days; 
    """
    
    try:
        given_date=datetime.strptime(date,"%Y-%m-%d").date()
    except ValueError:
        print(f"ERROR: Given input value \"{date}\" does not match format \"YYYY-MM-DD\"!")
        return None
    else:
        curr_date=datetime.today().date()
        return (curr_date-given_date).days

