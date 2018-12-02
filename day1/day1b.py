
def main():
    print(foo('day1b.txt'))

def foo(filename):
    thisdict = {
        0 : True
    }
    total = 0
    while True:
        file_object = open( filename ) 
        for line in file_object.readlines():
            if line[0] == '+':
                total += int(line[1:])
            else:
                total -= int(line[1:])

            if total in thisdict:
                return total
            else:
                thisdict[total] = True

main()