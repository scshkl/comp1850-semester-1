days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
# weekday = [x for x in days if x != 'saturday' or x != 'sunday'] # does not work

# weekday = [x for x in days if x != 'saturday' and x != 'sunday'] # work
weekday = [x for x in days if x not in ['saturday', 'sunday']]    # also work

print(weekday)