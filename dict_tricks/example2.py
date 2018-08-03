import datetime

type_based_operation = dict()
type_based_operation[str] = lambda data: 'The string is: {}'.format(data)
type_based_operation[int] = lambda data: 100 + data
type_based_operation[datetime.datetime] = lambda data: datetime.datetime.now()


dt = datetime.datetime(2018, 1, 1)
print(type_based_operation[type('Hello')]('Hello'))
print(type_based_operation[type(200)](200))
print(type_based_operation[type(dt)](dt))