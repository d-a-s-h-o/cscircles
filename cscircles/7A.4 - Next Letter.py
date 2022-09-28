letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
i = str(input())
for letter in letters:
    if letter == i:
        if letter != 'Z':
            print(letters[letters.index(letter) + 1])
        else:
            print('A')
