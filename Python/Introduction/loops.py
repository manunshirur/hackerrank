if __name__ == '__main__':
    n = int(input())
    print(*[i ** 2 for i in range(0, n)], sep="\n")