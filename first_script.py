my_iterable = range(1,3)

my_interator = my_iterable.__iter__()

my_interator.__next__()

list(range(1,3))

my_string = "ABC"
for letters in my_string:
    print(letters)
my_list = ["A", "B", "C"]
for letters in my_list:
    print(letters)

[x for x in range(1,10)]
{x for x in [1,1,2,2,3,3,4,4,5,6]}
[x for x in range(1,50) if x % 5 == 0]

d = {'name': "James", 'age': 23, 'country': 'Australia'}
for k in d:
    print(k)
d.keys()
d.values()
for v in d.values():
    print(v)
d.items()
for k,v in d.items():
    print(f'The key is: {k} and the value is: {v}')
[(k,v) for k,v in d.items()]


class EvenNums:
    val = 0

    def __iter__(self):
        return(self)    

    def __next__(self):
        self.val += 2

        if self.val > 8:
            raise StopIteration
        
        return self.val

even_numbers = EvenNums()

for x in even_numbers:
    print(x)
