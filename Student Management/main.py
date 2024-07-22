with open('Student Names.txt', 'r') as file:
    keys = file.read().splitlines()
with open('Student Grades.txt', 'r') as file:
    values = file.read().splitlines()

keyLen = len(keys)
valueLen = len(values)
grades = []

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
    # else:
    #     keys.extend([""] * (len(values) - len(keys)))
    #     diff = valueLen - keyLen
    #     print(f"There are {diff} grades without named students!")
    #     for i in range(diff):
    #         print(keys[-diff])
    #         diff -= 1
    #     decision = input("Do you want to continue or do you want to enter the names through here (1/2): ")
    #     if decision == "1":
    #         students = {keys[i]: values[i] for i in range(len(values)-diff)}
    #         print(students)
    #     elif decision == "2":
    #         while diff > 0:
    #             for i in range(diff):
    #                 name = int(input(f"What is the name of the kid that has these grades {values[-diff]}: "))
    #                 keys[-diff] = name
    #                 diff -= 1
    #             if diff == 0:
    #                 break
    #         students = {keys[i]: values[i] for i in range(len(keys))}
    #         print(students)



for i in range(valueLen):
    if values[i] == "":
        missing = + 1

        print("The following student does not have any entered grades: " + keys[i])
        decision = input("Do you want to continue or do you want to enter the grades through here (1/2): ")
        if decision == "1":
            students = {keys[i]: values[i] for i in range(len(keys))}
            print(students)
        elif decision == "2":
            length = int(input(f"How many grades should {keys[i]} have: "))
            grades = []
            for k in range(length):
                grades.append(input(f"Enter the {k+1} grade: "))
            values[i] = ' '.join(grades)
            students = {keys[i]: values[i] for i in range(len(keys))}
            print(students)
    else:
        students = {keys[i]: values[i] for i in range(len(keys))}
        print(students)
        break

