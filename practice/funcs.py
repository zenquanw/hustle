def add_all(nums):
    total = 0
    for n in nums:
        total = total + n
    return total


print(add_all([1, 2, 3, 4]))


def avg_all(nums):
    total = 0
    for n in nums:
        total = total + n
    return total / len(nums)


print(avg_all([10, 20, 30]))


def unique_all(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


print(unique_all([1, 1, 12, 2, 3, 3, 4]))

def word_count(text):
    result = {}
    for word in text.split():
        if word in result:
            result[word]+= 1
        else:

            result[word] = 1
    return result
print(word_count('q b c a b a b a b'))


def max_of(nums):
    max_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num

print(max_of([1, 5, 3, 9, 2]))


def is_even(num):
    return num % 2 == 0
print(is_even(4))

def reverse_text(text):
    return text[::-1]

print(reverse_text('acb'))

def to_dict(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

print(to_dict([('a', 1), ('b', 2), ('c', 3)]))

def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())


print(count_lines(__file__))

def clean_space(s):
    return "".join( s.split())
print(clean_space('  1   hello     world     '))