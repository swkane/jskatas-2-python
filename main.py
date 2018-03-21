def reverse(string):
    separator = ''
    return separator.join(list(reversed(string)))

print(reverse('sam'))

def reverseSentence(sentence):
    separator = ' '
    lst = sentence.split()
    lst.reverse()
    return separator.join(lst)

print(reverseSentence('switch my order'))

def min(lst):
    lst.sort()
    return lst[0]

print(min([2,1,3]))

def max(lst):
    lst.sort(reverse=True)
    return lst[0]

print(max([2,1,3]))

def remainder(num, den):
    return num % den

print(remainder(5,3))

def unique(lst):
    for x in lst:
        if lst.count(x) > 1:
            lst.remove(x)
    return lst

print(unique([1,2,3]))
print(unique([1,2,1,3]))
print(unique([1,1,1,2,3]))

def uniqueCount(lst):
    result = {}
    for x in lst:
        result[x] = 0
    for x in lst:  
        result[x] = result[x] + 1
    return result

print(uniqueCount([1,2,3]))
print(uniqueCount([1,2,1,3]))
print(uniqueCount([1,1,1,2,3]))

def evaluateExpression(expression, dict):
    lst = dict.keys()
    for x in lst:
        expression = expression.replace(x, str(dict[x]))
    return eval(expression)

print(evaluateExpression("a + b + c - d", {'a': 1, 'b': 7, 'c': 3, 'd': 14}))