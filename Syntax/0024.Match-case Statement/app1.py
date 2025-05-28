# Match-case Statement (Python 3.10 or greater):

user_day = input("Enter a day: ")

match user_day:
    case 'Monday': print('1')
    case 'Tuesday': print('2')
    case 'Wednesday': print('3')
    case 'Thursday': print('4')
    case 'Friday': print('5')
    case 'Saturday': print('6')
    case 'Sunday': print('7')
    case _: print('Unknown!') # default -> '_'
# -------------------------------------------
