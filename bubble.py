def bubble(n, a):
    flag = 1
    for i in range(0, n-1):     # N-1 итераций работы алгоритма
        for j in range(0, n-1-i):   # проход по оставшимся не отсортированным парам массива
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = 1
        if flag == 1:
            for x in a:
                print(x, end=' ')
            print('')
            flag = 0


if __name__ == '__main__':
    n = int(input())
    a = [int(_) for _ in input().split(' ')]
    bubble(n, a)
