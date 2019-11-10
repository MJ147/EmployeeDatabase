# Baza pracowników
# 1. Operacje CRUD
# 1.2 addEmployee: if duplikat -> komunikat, else: dodanie do bazy
# 1.3 getEmployee: if brak w bazie -> komunikat, else: pobranie z bazy
# 1.2 removeEmployee: if brak w bazie -> komunikat, else: usunięcie z bazy
# 1.2 updateEmployee: if brak w bazie -> komunikat, else: pobranie indeksu
#                     i przypisanie do indeksu nowego pracownika


def addEmployee(database, employee):
    if employee in database:
        print(employee['name'] + employee['surname'] + 'już istnieje w bazie')
    else:
        database.append(employee)


def getEmployee(database, employee):
    if employee not in database:
        print(employee['name'] + employee['surname'] + 'nie istnieje w bazie')
    else:
        return employee

def removeEmployee(database, employee):
    if employee not in database:
        print(employee['name'] + employee['surname'] + 'nie istnieje w bazie')
    else:
        database.remove(employee)


def updateEmployee(database, employee, update):
    if employee not in database:
        print(employee['name'] + employee['surname'] + 'nie istnieje w bazie')
    else:
        index = database.index(employee)
        database[index] = update

def averagePayment(database):
    if not database:
        print('baza jest pusta')
        return -1
    else:
        sum = 0
        for employee in database:
            sum += employee['payment']
    return sum / len(database)

def minPayment(database):
    if not database:
        print('baza jest pusta')
        return -1
    else:
        min = database[0]['payment']
        minEmployee = ''
        for employee in database:
            if min > employee['payment']:
                min = employee['payment']
                minEmployee = employee
    return minEmployee

def maxPayment(database):
    if not database:
        print('baza jest pusta')
        return -1
    else:
        max = database[0]['payment']
        maxEmployee = ''
        for employee in database:
            if max < employee['payment']:
                max = employee['payment']
                maxEmployee = employee
    return maxEmployee

def findPosition(employeesDatabase, positionsDatabase, position):
    if len(employeesDatabase) == 0:
        print('baza jest pusta')
    elif position not in positionsDatabase:
        print('nie ma takiego stanowiska')
    else:
        employeesWithPosition = []
        for employee in employeesDatabase:
            if employee['position'] == position:
                employeesWithPosition.append(employee)
    return employeesWithPosition


#TESTS:

position1 = {
    'name': 'Projektant'
}

position2 = {
    'name': 'Księgowy'
}

positionsDatabase = [position1, position2]

employee1 = {
    'name': 'Jurek',
    'surname': 'Kowalski',
    'position': position1,
    'payment': 5000
}

employee2 = {
    'name': 'Miro',
    'surname': 'Koko',
    'position': position2,
    'payment': 4000
}

employee3 = {
    'name': 'Roman',
    'surname': 'Nowak',
    'position': position1,
    'payment': 6000
}

employeesDatabase = [employee1, employee2, employee3]

#test addEmployee:

employeeTest = {
    'name': 'Marek',
    'surname': 'Polan',
    'position': 'Projektant',
    'payment': 4000
}

employeesDatabaseTest = []
employeesDatabaseTest2 = [employeeTest]
addEmployee(employeesDatabaseTest, employeeTest)
if (employeesDatabaseTest == employeesDatabaseTest2):
    print('addEmployee TEST : TRUE')
else:
    print('addEmployee TEST : FALSE')

#test averagePayment:

if averagePayment(employeesDatabase) == 5000:
    print('averagePayment TEST : TRUE')
else:
    print('averagePayment TEST : FALSE')

#test findPosition:

print(findPosition(employeesDatabase, positionsDatabase, position1))

#test minPayment:

if minPayment(employeesDatabase) == employee2:
    print('minPayment TEST : TRUE')
else:
    print('minPayment TEST : FALSE')

#test maxPayment:

if maxPayment(employeesDatabase) == employee3:
    print('minPayment TEST : TRUE')
else:
    print('minPayment TEST : FALSE')