try:
    global filename
    global total
    global sample
    global line
    filename = input('Name of file')
    global f
    f = open(filename, 'r')
    sample = 0
    total = 0
    global currentline
    currentline = 0
    global line
    for line in f:
        line.rstrip('\n')
        currentline += 1
        line = int(line)
        total += line
        sample += 1
    sum = total / sample
    print('The average is: ', sum)

except Exception as ex:
    print('Error!')
    print('Type is: ', type(ex).__name__)
    if type(ex).__name__ == 'FileNotFoundError':
        print('An error occurred finding the file.')
        y = input('Type Y to correct and continue: ').lower()
        if y == 'y':
            sample = 0
            total = 0
            filename = input('Name of file')
            x = open(filename, 'r')
            currentline = 0
            for line in x:
                line.rstrip('\n')
                currentline += 1
                line = int(line)
                total += line
                sample += 1
            sum = total / sample
            print('The average is: ', sum)
        else:
            print('You chose to quit.')
    if type(ex).__name__ == 'ValueError':
        print('Error! Data inside of file is wrong type.')
        print('The error was found in line:', currentline)
        y = input('Type Y to correct and continue: ').lower()
        if y == 'y':
            line = 0
            for line in f:
                line.rstrip('\n')
                currentline += 1
                line = int(line)
                total += line
                sample += 1
            sum = total / sample
            print('The average is: ', sum)

        else:
            print('You decided to quit.')
