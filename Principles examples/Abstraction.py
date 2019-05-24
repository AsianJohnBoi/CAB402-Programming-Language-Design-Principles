def viralAdvertising(n):
    shared =5
    cumulative=0
    for i in range(1, n+1):
        liked = shared//2
        cumulative+=liked
        shared = liked*3
    return cumulative

if __name__ == '__main__':
    n = 1238
    result = viralAdvertising(n)
    print(result)

    x = []
    for i in range(1, 10):
        x.append(i)
    print(x)