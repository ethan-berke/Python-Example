def main():
    input('Press enter to start Task 1: ')
    filename = input('Name of file')
    try:
        f = open(filename, 'r')
    except FileNotFoundError as e:
        print('An error occurred finding the file.')
        y = input('Type Y to correct and continue: ').lower()
        if y == 'y':
            try:
                sum = readnumbers('numbers.txt')
                print("The average is: ", sum)
            except:
                print('File not found in your directory.')
        else:
            print('You decided to quit.')
    else:
        sum = readnumbers(filename)
        print('The average is: ', sum)


def readnumbers(file):
    f = open(file, 'r')
    global sample
    global total
    sample = 0
    total = 0
    currentline = 0
    for line in f:
        line.rstrip('\n')
        currentline += 1
        try:
            line = int(line)
        except ValueError:
            print('Error! Data inside of file is wrong type.')
            print('The error was found in line:', currentline)
            y = input('Type Y to correct and continue: ').lower()
            if y == 'y':
                line = 0
            else:
                print('You decided to quit.')
        total += line
        sample += 1
    average = total / sample
    return average
main()