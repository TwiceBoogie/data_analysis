# produces a diagnostic report that shows data entry errors (row wise)
def detect_errors_row():
    infile_name = input("What's the file name: ")
    infile = open(infile_name, "r", encoding="utf-8")
    print("{0:^50}".format("Row-Level Data Entry Errors"))
    print("{0:<10}{1:>10}{2:>10}{3:>10}{4:>10}".format(
        "Age Group", "Males", "Females", "Total", "Error"))

    for line in infile:
        age, males, females, total = line.split()
        males = int(males)
        females = int(females)
        total = int(total)
        row_total = males + females
        row_error = row_total - total
        print("{0:<10}{1:>10}{2:>10}{3:>10}{4:>10}".format(
            age, males, females, total, row_error))
    infile.close()


# Produce a diagnostic report that shows data entry errors (column wise)
def detect_errors_column():
    infile_name = input("What is the file name: ")
    infile = open(infile_name, "r", encoding="utf-8")
    print("{0:^50}".format("Column-Level Data Entry Errors"))
    print("{0:<10}{1:>10}{2:>10}{3:>10}".format(
        "Age Group", "Males", "Females", "Total"))

    males_accum, females_accum, total_accum = 0, 0, 0

    for line in infile:
        age, males, females, total = line.split()
        males = int(males)
        females = int(females)
        total = int(total)
        print("{0:<10}{1:>10}{2:>10}{3:>10}".format(
            age, males, females, total))

        if age != "Total":
            males_accum += males
            females_accum += females
            total_accum += total
        else:
            males -= males_accum
            females -= females_accum
            total -= total_accum
            print("{0:<10}{1:>10}{2:>10}{3:>10}".format(
                "Error", males, females, total))


# detect_errors_row()
detect_errors_column()
