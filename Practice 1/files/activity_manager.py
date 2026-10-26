import datetime
from activity import *

FILENAME = 'activities.txt'


# ---------- input helpers ----------
def read_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Please enter a number.')
            continue
        if low <= value <= high:
            return value
        print(f'Value must be between {low} and {high}.')


def read_date():
    while True:
        day = read_int('Day: ', 1, 31)
        month = read_int('Month: ', 1, 12)
        year = read_int('Year: ', 1900, 2100)
        try:
            datetime.date(year, month, day)      # checks e.g. 31/04 or 29/02
            return day, month, year
        except ValueError:
            print('That date does not exist. Try again.')


def read_time_and_duration():
    while True:
        hours = read_int('Start hours (0-23): ', 0, 23)
        minutes = read_int('Start minutes (0-59): ', 0, 59)
        duration = read_int('Duration in minutes: ', 1, 24 * 60)
        if hours * 60 + minutes + duration <= 24 * 60:
            return hours, minutes, duration
        print('Activity must finish before midnight. Try again.')


def read_description():
    while True:
        text = input('Description: ').strip()
        if text != '':
            return text
        print('Description cannot be empty.')


def pick_activity(activities):
    # shows a numbered list and returns the chosen index (or None)
    if len(activities) == 0:
        print('No activities available.')
        return None
    print()
    for i in range(len(activities)):
        print(f'{i + 1:>3}. {activities[i].get_activity()}')
    choice = read_int('Enter activity number (0 to cancel): ', 0, len(activities))
    if choice == 0:
        return None
    return choice - 1


def sort_key(a):
    return (a.get_year(), a.get_month(), a.get_day(), a.get_start())


def print_table(activities):
    if len(activities) == 0:
        print('No activities found.')
        return
    print(f'\n{"Date":<12}{"Start":<8}{"End":<8}{"Minutes":>8}   Description')
    print('-' * 60)
    for a in sorted(activities, key=sort_key):
        print(a.get_activity())


# ---------- menu actions ----------
def add_activity(activities):
    day, month, year = read_date()
    hours, minutes, duration = read_time_and_duration()
    description = read_description()
    activities.append(Activity(day, month, year, hours, minutes, duration, description))
    print('Activity added successfully.')


def modify_activity(activities):
    index = pick_activity(activities)
    if index is None:
        return
    a = activities[index]

    print('\n1. Modify Date')
    print('2. Modify Time and Duration')
    print('3. Modify Description')
    option = input('Enter modification option: ')

    if option == '1':
        day, month, year = read_date()
        a.set_day(day)
        a.set_month(month)
        a.set_year(year)
    elif option == '2':
        hours, minutes, duration = read_time_and_duration()
        a.set_hours(hours)
        a.set_minutes(minutes)
        a.set_duration(duration)
    elif option == '3':
        a.set_description(read_description())
    else:
        print('Invalid modification option.')
        return
    print('Activity modified successfully.')


def remove_activity(activities):
    index = pick_activity(activities)
    if index is None:
        return
    del activities[index]
    print('Activity removed successfully.')


def search_activity(activities):
    keyword = input('Search keyword: ').strip().lower()
    matches = [a for a in activities if keyword in a.get_description().lower()]
    print_table(matches)


def show_all(activities):
    print_table(activities)


def show_month(activities):
    month = read_int('Month (1-12): ', 1, 12)
    year = read_int('Year: ', 1900, 2100)
    matches = [a for a in activities if a.get_month() == month and a.get_year() == year]
    print_table(matches)


def show_day(activities):
    day, month, year = read_date()
    matches = [a for a in activities
               if a.get_day() == day and a.get_month() == month and a.get_year() == year]
    print_table(matches)


def show_overlaps(activities):
    found = False
    for i in range(len(activities)):
        for j in range(i + 1, len(activities)):
            a = activities[i]
            b = activities[j]
            overlap = a.get_overlap(b)
            if overlap > 0:
                found = True
                start = max(a.get_start(), b.get_start())
                end = min(a.get_end(), b.get_end())
                print('\nOverlap found on ' + a.get_date() + ':')
                print('  ' + a.get_activity())
                print('  ' + b.get_activity())
                print(f'  Shared time: {format_time(start)} - {format_time(end)} ({overlap} minutes)')
    if not found:
        print('No overlapping activities.')


def save_activities(activities):
    with open(FILENAME, 'w') as f:
        for a in activities:
            f.write(f'{a.get_day()},{a.get_month()},{a.get_year()},'
                    f'{a.get_hours()},{a.get_minutes()},{a.get_duration()},'
                    f'{a.get_description()}\n')
    print('Activities saved successfully.')


def load_activities(activities):
    loaded = []
    try:
        with open(FILENAME, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                # maxsplit=6 so the description may safely contain commas
                d, m, y, h, mi, dur, desc = line.split(',', 6)
                loaded.append(Activity(int(d), int(m), int(y), int(h), int(mi), int(dur), desc))
    except FileNotFoundError:
        print('No saved file found.')
        return
    except ValueError:
        print('File is corrupted. Nothing was loaded.')
        return

    activities.clear()
    activities.extend(loaded)
    print('Activities loaded successfully.')


def menu():
    print('\n1. Add an activity')
    print('2. Modify an activity')
    print('3. Remove an activity')
    print('4. Search an activity')
    print('5. Show all activities')
    print('6. Show all activities in a month')
    print('7. Show all activities on a day')
    print('8. Show overlapping activities')
    print('9. Save activities')
    print('10. Load activities')
    print('11. Quit')
    return input('Enter your choice: ').strip()


def main():
    activities = []

    while True:
        choice = menu()

        if choice == '1':
            add_activity(activities)
        elif choice == '2':
            modify_activity(activities)
        elif choice == '3':
            remove_activity(activities)
        elif choice == '4':
            search_activity(activities)
        elif choice == '5':
            show_all(activities)
        elif choice == '6':
            show_month(activities)
        elif choice == '7':
            show_day(activities)
        elif choice == '8':
            show_overlaps(activities)
        elif choice == '9':
            save_activities(activities)
        elif choice == '10':
            load_activities(activities)
        elif choice == '11':
            print('Program terminated.')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
