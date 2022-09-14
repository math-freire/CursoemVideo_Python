results = {'name': input('Name: '),
           'average': float(input('Average: '))}
if results['average'] <= 4:
    results['condition'] = 'Held Back'
else:
    results['condition'] = condition = 'Approved'

print(f"Average: {results['average']}")
print(f"Name: {results['name']}")
print(f"Condition: {results['condition']}")
