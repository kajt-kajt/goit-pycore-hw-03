from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users: list[dict[str,str]]) -> list[dict[str,str]]:
    """
    Generate the list of birthday greetings for upcoming week

    If this year's birthday of a person is Saturday or Sunday, greeting day is moved to next Monday.

    Parameters:
        users (list[dict[str,str]]): list of dictionaries with names and birth dates.
                                     Each dictionary should have key "name" with name of a person and
                                     a key "birthday" with str value of birth date in format "YYYY.mm.dd"

    Returns:
        list[dict[str,str]]: list of dictionaries with names and greeting dates.
                             Each dictionary contains key "name" with the name of a person to greet, and
                             a key "congratulation_date" with str value of date within a week for birthday greeting
    """
    
    result=[]
    today_date=datetime.today().date()
    for user in users:
        user_birthdate=datetime.strptime(user["birthday"],"%Y.%m.%d").date()
        # Substitute year to current one to get first estimate of congratulation date
        user_congratulation_day=date(year=today_date.year,
                               month=user_birthdate.month,
                               day=user_birthdate.day)
        # If user already had birthday this year, let's move his congratulation date to next year
        if user_congratulation_day<today_date:
            user_congratulation_day=date(year=today_date.year+1,
                               month=user_birthdate.month,
                               day=user_birthdate.day)
        # If user's congratulation date is Saturday, let's move it on Monday
        if user_congratulation_day.weekday() == 5: 
            user_congratulation_day=user_congratulation_day+timedelta(days=2)
        # If user's congratulation date is Sunday, let's move it on Monday
        if user_congratulation_day.weekday() == 6: 
            user_congratulation_day=user_congratulation_day+timedelta(days=1)
        # If user's congratulation date is within a week, let's add him to output
        if (user_congratulation_day-today_date)<timedelta(days=7):
            result.append({
                "name":user["name"],
                "congratulation_date":datetime.strftime(user_congratulation_day,"%Y.%m.%d")
                })
    return result

