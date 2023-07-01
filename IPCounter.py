values = {
    '1': 128,
    '2': 64,
    '3': 32,
    '4': 16,
    '5': 8,
    '6': 4,
    '7': 2,
    '8': 1
}

y = 0
Binary = '0 0 0 0 0 0 0 0'  # Initialize the entry log

while y <= 1020:
    print(f'Octet = {y}')
    print(f'Entry Log: {Binary}')
    counter = input('\n1 = 128 \n2 = 64 \n3 = 32 \n4 = 16 \n5 = 8 \n6 = 4 \n7 = 2 \n8 = 1 \n\n–> ')
    if counter in values:
        y += values[counter]
        print(f'\n+ {values[counter]}')
        Binary = Binary.replace('0', '1', 1)  # Update the entry log
    elif counter == 'stop':
        print(f'\nOctet = {y}')
        break

print('Sum of IP address values:', y)


#.replace() is a string method in Python that replaces occurrences of a specified substring with a new substring.

#In this case, '0' is the substring to be replaced.

#'1' is the new substring that will replace '0'.

#The 1 as the third argument specifies that only the first occurrence of '0' in the Binary string should be replaced.