def reverse(string):
    separator = ''
    return separator.join(reversed(string))

print(reverse('sam'))

def reverseSentence(sentence):
    separator = ' '
    lst = sentence.split()
    lst.reverse()
    return separator.join(lst)

print(reverseSentence('switch my order'))

def minEl(lst):
    return min(lst)

print(minEl([2,1,3]))

def maxEl(lst):
    return max(lst)

print(maxEl([2,1,3]))

def remainder(num, den):
    return num % den

print(remainder(5,3))

def unique(lst):
    return list(set(lst))

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