str1 = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
word1 = 'better'
word2 = 'never'
word3 = 'is'
separated = str1.split()
count1 = separated.count('better')
count2 = separated.count('never')
count3 = separated.count('is')
print('better =', count1)
print('never =', count2)
print('is =', count3)  # task 1

print(str1.upper())  # task 2
print(str1.replace('i', '&'))  # task 3

four = int(input())
digit_one = four // 1000
digit_two = (four // 100) % 10
digit_three = (four % 100) // 10
digit_four = four % 10

sum = digit_one * digit_two * digit_three * digit_four
print(sum)  # task 4

reverse = str(four)
print(reverse[::-1])  # task 5

ascended = [digit_one, digit_two, digit_three, digit_four]
print(sorted(ascended))  # task 6

first_variable = 5
second_variable = 10

first_variable, second_variable = second_variable, first_variable
print(first_variable)  # task 7