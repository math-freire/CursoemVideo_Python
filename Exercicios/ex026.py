x = input('Type anything: ').strip().upper()

print('A appears {} times.'.format(x.count('A')))
print('A appears for the first time at position #{}.'.format(x.find('A')+1))  # +1 so pos won't be #0
print('A appears for the last time at position #{}.'.format(x.rfind('A'+1)))
