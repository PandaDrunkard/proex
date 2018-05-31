n = int(input())

numbers = list(map(lambda s: int(s), input().split()))

print(f'{min(numbers)} {max(numbers)} {sum(numbers)}')