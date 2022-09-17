from my_codes import titulo, end_program


def grade(*grades, sit=False):
    """
    Returns a student's grade dictionary containing the total of entries, the greatest, the lowest and the mediam.
    param grades: Many grades as user may want
    param sit: False by default. True for showing if the student is approved (mediam > 4) or held back
    return: Dictionary containing all the information.
    """
    student = {'total': len(grades), 'top': max(grades), 'bottom': min(grades), 'median': (sum(grades) / len(grades))}
    if sit:
        if student['total'] > 4:
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
