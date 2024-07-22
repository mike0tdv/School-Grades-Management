with open('Student Names.txt', 'r') as file:
    keys = file.read().splitlines()
with open('Student Grades.txt', 'r') as file:
    values = file.read().splitlines()

keyLen = len(keys)
valueLen = len(values)
grades = []
missing_values = []

if keyLen != valueLen:
    if keyLen > valueLen:
        values.extend([""] * (len(keys) - len(values)))
        diff = keyLen - valueLen
        print(f"There are {diff} student/s without grades!")
        for i in range(diff):
            print(keys[-diff])
            diff -= 1
        decision = input("Do you want to continue or do you want to enter the grades through here (1/2): ")
        if decision == "1":
            students = {keys[i]: values[i] for i in range(len(keys)-diff)}
            print(students)
        elif decision == "2":
            while diff > 0:
                for i in range(diff):
                    length = int(input(f"How many grades should {keys[-diff]} have: "))
                    for k in range(length):
                        grades.append(input(f"Enter the {k+1} grade: "))
                    values[-diff] = ' '.join(grades)
                    grades = []
                    diff -= 1
                if diff == 0:
                    break
            students = {keys[i]: values[i] for i in range(len(keys))}
            print(students)
    else:
        keys.extend([""] * (len(values) - len(keys)))
        diff = valueLen - keyLen
        print(f"There are {diff} grades without named students!")
        for i in range(diff):
            print(values[-diff])
            diff -= 1
        decision = input("Do you want to continue or do you want to enter the names through here (1/2): ")
        if decision == "1":
            students = {keys[i]: values[i] for i in range(len(values)-diff)}
            print(students)
        elif decision == "2":
            while diff > 0:
                for i in range(diff):
                    name = int(input(f"What is the name of the kid that has these grades {values[-diff]}: "))
                    keys[-diff] = name
                    diff -= 1
                if diff == 0:
                    break
            students = {keys[i]: values[i] for i in range(len(keys))}
            print(students)

for i in range(valueLen):
    if values[i] == "":
        missing_values.append(i)

if len(missing_values) == 0:
    students = {keys[i]: values[i] for i in range(len(keys))}
    print(students)
else:
    print(f"There are {len(missing_values)} students without grades!")
    for i in range(len(missing_values)):
        print(keys[missing_values[i]])
    decision = input("Do you want to continue or do you want to enter the grades through here (1/2): ")
    if decision == "1":
        students = {keys[i]: values[i] for i in range(len(keys))}
        print(students)
    elif decision == "2":
        for i in range(len(missing_values)):
            length = int(input(f"How many grades should {keys[missing_values[i]]} have: "))
            for k in range(length):
                grades.append(input(f"Enter the {k + 1} grade: "))
            values[missing_values[i]] = ' '.join(grades)
            grades = []
        students = {keys[i]: values[i] for i in range(len(keys))}
        print(students)







