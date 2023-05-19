# A program to produce four data analysis reports

from population_group import PopulationGroup


def main():
    data = build_population_group_list()
    sums = calculate_column_total(data)

    data.sort(key=by_age_group)
    print_report(data, "COUNTS BY AGE GROUP\n", sums)

    data.sort(key=by_total_count, reverse=True)
    print_report(data, "COUNTS BY DESCENDING TOTAL COUNT\n", sums)

    data.sort(key=by_male_count, reverse=True)
    print_report(data, "COUNTS BY DESCENDING MALE COUNT\n", sums)

    data.sort(key=by_female_count, reverse=True)
    print_report(data, "COUNTS BY DESCENDING FEMALE COUNT\n", sums)


def build_population_group_list():
    infile_name = input("What's the name of the file: ")
    infile = open(infile_name, "r", encoding="utf8")
    population_group_list = []

    for line in infile:
        age, male, female, total = line.split()
        male = int(male)
        female = int(female)
        total = int(total)
        lst = PopulationGroup(age, male, female, total)
        if age != "Total":
            population_group_list.append(lst)
    infile.close()

    return population_group_list


def calculate_column_total(pop_group_list):
    male_total, female_total, overall_total, percent_total = 0, 0, 0, 0

    for group in pop_group_list:
        male_total += group.male_count
        female_total += group.female_count
        overall_total += group.total_count
        percent_total += group.calculate_category_percentage()
    return male_total, female_total, overall_total, percent_total


def print_report(pop_group_list, title, total):
    print()
    print("{:^50}".format(title))
    print("{0:<10}{1:>10}{2:>10}{3:>10}{4:>10}".format(
        "Age Group", "Males", "Females", "Total", "Percent"))

    for group in pop_group_list:
        print("{0:<10}{1:>10,}{2:>10,}{3:>10,}{4:>10.2f}".format(group.category, group.male_count,
              group.female_count, group.total_count, group.calculate_category_percentage()))
    print("{0:<10}{1:>10,}{2:>10,}{3:>10,}{4:>10.2f}".format(
        "Total", total[0], total[1], total[2], round(total[3])))


def by_age_group(data_instance):
    return data_instance.category


def by_total_count(data_instance):
    return data_instance.total_count


def by_male_count(data_instance):
    return data_instance.male_count


def by_female_count(data_instance):
    return data_instance.female_count


main()
