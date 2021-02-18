if __name__ == '__main__':
    n = int(input().strip())
    if n % 2==1 :
        print('Weird')
    elif n==18:
        print('Weird')
    elif n==20:
        print('Weird')
    elif n % 2== 0 or 2 <= n <=5:
        print('Not Weird')
    elif n % 2== 0 or 6 <= n <=20:
        print('Weird')