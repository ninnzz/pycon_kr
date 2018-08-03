import datetime

def type_based_operation(data):
    if type(data) == str:
        return 'The string is: {}'.format(data)
    elif type(data) == int:
        return 100 + data
    elif type(data) == datetime.datetime:
        return datetime.datetime.now()
    return

print(type_based_operation('Hello'))
print(type_based_operation(200))
print(type_based_operation(datetime.datetime(2018, 1, 1)))