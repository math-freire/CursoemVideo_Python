from my_codes import titulo, end_program


def grade(*grades, sit=False):
    grades_total = len(grades)
    grades_max = max(grades)
    grades_min = min(grades)
    grades_median = (sum(grades) / grades_total)
    student = {'total': grades_total,
               'top': grades_max,
               'bottom': grades_min,
               'median': grades_median}
    if sit:
        if grades_median > 4:
            student['situation'] = 'Approved'
        else:
            student['situation'] = 'Held Back'
    return student


titulo('GRADES - OPT PARAM', (len('GRADES - OPT PARAM') + 6))
x = grade(1, 2, 3, 5, 6, sit=True)
print(x)
x = grade(5, 8, 9, 10, 7.6, sit=True)
print(x)
x = grade(4, 5, 6, 3)
print(x)
end_program()
