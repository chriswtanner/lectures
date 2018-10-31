def main():

    tmp_list = []
    tmp_list.append("jackie")
    tmp_list.append("emily")
    tmp_list.append("jackie")
    print("list:" + str(tmp_list))

    students = set()
    students.add("jackie")
    students.add("emily")
    students.add("jackie")
    print("set:" + str(students))
    for student in students:
        print(student)

    students.remove("jackie")
    print(students)

    print(len(students))

if __name__ == "__main__":
    main()
