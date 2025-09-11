
numbers = [1,2,3,4]

times_two = map(lambda x: x*2, numbers)

print(list(times_two))

[x*2 for x in range(10)]

[x + 4 for x in range(10) if x % 2 == 0]

def some_func(val):
    return val + 10

[some_func(x) for x in range(10)]

m = [[j for j in range(3)] for i in range(4)]

[value for sublist in m for value in sublist]

[value
    for sublist in m
    for value in sublist]

{x for x in {1,2,3}}

{x for x in set([1,2,3,4,3,4,5]) if x % 2 == 0}

{s for s in range(1,5) if s % 2}
{s for s in range(1,5) if s % 2 == 0}
{s for s in range(1,5)}

{x: x**3 for x in range(10)}
