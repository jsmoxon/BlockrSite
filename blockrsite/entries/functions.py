import datetime

def word_count(text):
    words = text.split(" ")
    return len(words)

def clean_time(entry_time, goal_time):
    """
    ensures that the time for the flag is not >23; takes a goal_time and ensures that they are not >23
    if it is return it
    else return a roll it over into the next day and fix the date
    """
    sum = entry_time + goal_time
    if sum <23:
        return sum
    else:
        return abs(24-sum)

def clean_blacklist(user, string_of_urls):
    """
    takes a user and string of urls, parses the string into a list that can be uploaded to the database via a for loop
    """
    return string_of_urls.split(',')
