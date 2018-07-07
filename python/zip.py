names = ['Cecilia', 'Lise', 'Marie']
letters = [len(name) for name in names]

longest_name = None
max_letters = 0

for name, letter in zip(names, letters):
    if letter > max_letters:
        longest_name = name
        max_letters = letter

print('longest name is %s, and the length is %d.'%(longest_name, max_letters))
