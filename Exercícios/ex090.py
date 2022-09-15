results = {'name': input('Name: '),
           'average': float(input('Average: '))}
if results['average'] <= 4:
    results['condition'] = 'Held Back'
else:
    results['condition'] = condition = 'Approved'

print(f"Name: {results['name']}")
print(f"Average: {results['average']}")
print(f"Condition: {results['condition']}")

# or

print('-'*10)
for k, v in results.items():
    print(f'- {k} is {v}')
