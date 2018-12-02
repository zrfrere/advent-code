
def main():
    print(foo('day1.txt'))

def foo(filename):
    total = 0
    file_object = open( filename ) 
    for line in file_object.readlines():
        if line[0] == '+':
            total += int(line[1:])
        else:
            total -= int(line[1:])
    return total

main()