# Python If-Else
if __name__ == '__main__':
    n = int(input().strip())

if n in range(1,101):
    if n%2 == 0:
        if n in range(2,6):
            print('Not Weird')
        elif n in range(6,21):
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Weird')

