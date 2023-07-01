values = {
    '1': 128,
    '2': 64,
    '3': 32,
    '4': 16,
    '5': 8,
    '6': 4,
    '7': 2,
    '8': 1,
    'null': 0,
}

y = 0
Binary = [False] * 8  # Initialize the entry log as a list of False values

while y <= 1020:
    print(f'\nOctet = {y}')
    print(f'Entry Log: {" ".join("1" if b else "0" for b in Binary)}')
    counter = input('\n1 = 128 \n2 = 64 \n3 = 32 \n4 = 16 \n5 = 8 \n6 = 4 \n7 = 2 \n8 = 1 \n\nnull = 0 \n\n–> ')
    if counter in values:
        y += values[counter]
        print(f'\n+ {values[counter]}')
        if counter != 'null':
            entry_position = int(counter) - 1  # Calculate the position in the entry log
            Binary[entry_position] = True  # Update the entry log at the calculated position
    elif counter == 'stop':
        print(f'\nOctet = {y}')
        break

print('Sum of IP address values:', y)
print(f'Final Entry Log: {" ".join("1" if b else "0" for b in Binary)}')



#.replace() is a string method in Python that replaces occurrences of a specified substring with a new substring.

#In this case, '0' is the substring to be replaced.

#'1' is the new substring that will replace '0'.

#The 1 as the third argument specifies that only the first occurrence of '0' in the Binary string should be replaced.