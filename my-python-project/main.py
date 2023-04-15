from helper import validate_and_execute, print

user_input = ''
while user_input != 'exit':
    user_input = input('Hey user, enter a number of days and conversion units!\n')
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)

