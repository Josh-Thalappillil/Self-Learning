# a = ["banana", "apple", "microsoft"]

# for element in a:
    # print(element)

def loop_avg():

    b = [20, 10, 5]
    total = 0

    for e in b:
        # this loop helps me find the total
        total = total + e

    # we can also find the average
    avg = total/len(b)
    print(avg)

def lists():
    c = list(range(1, 5))
    print(c)

def rgloop():
    total = 0
    for i in range(1, 5):
        total += i
        print(total)


def multiples():
    list(range(1, 100))
    # compute all multiples of 3 and 5 that are less than 100 
    total = 0
    for i in range(1, 100):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)



a = (20, 10, 5)
list(a)
total = 0

for i in a:
    total = total + i
    avg = total/len(list(a))

print(total)
print(avg)