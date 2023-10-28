# Name: Randy Fu
# Date:
# Do not forget to change the file name -> Save as
import math
import string
import PIL
from PIL import Image
import itertools
from itertools import permutations
''' Tasks '''
# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# 2. Output the list of those integers (from #1) that are divisible by three.
'''msg = input("nums: ")
print (msg)
print (msg.split())
print ([int(x) for x in msg.split()]) #list comprehension'''
numslist = [int(x) for x in input("list of numbers: ").strip().split()]
print ('1. sum =  '+str(sum(numslist))) # #1
print ('2. list of multiples of 3:  '+str([x for x in numslist if x % 3 == 0])) # #2



# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8        (x)
terms = int(input("Type n for Fibonacci sequence: ").strip())
n1 = 1
n2 = 1
count = 0
fib_str = '3. fibonacci: '
while(count < terms):
   fib_str = fib_str + str(n1)+ ' '
   nth = n1+n2
   n1 = n2
   n2 = nth
   count+=1
print(fib_str.strip())
# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
msgstr = input("Type a string: ").strip()
print('4. every other string: '+msgstr[::2])   

# 5. Given a positive integer input, check whether the number is prime or not.
checknum = int(input('Type a number to check prime: ').strip())
prime = 'True'
for i in range(2,int(checknum/2)+1):
   if checknum % i == 0:
      prime = 'False'
print('5. Is prime? '+ prime)
# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
#sqrt(p(p-a)(p-b)(p-c)) where p is a+b+c/2
lengths = input('Type three sides of triangle: ').strip()
nums = [int(x) for x in lengths.split()]
p = sum(nums)/2
parts = [p-n for n in nums]
parea = 1
for nums in parts:
   parea *= nums
print('6. The area of ' +lengths+ ' is ' + str(math.sqrt(p * parea)))               
# 7. Given a input of a string, remove all punctuation from the string. 
sentence = input('Type a sentence: ').strip()
changed_sent = sentence.translate(str.maketrans('', '', string.punctuation)).replace(" ","")
print('7. Punct removed: ' + changed_sent)
# eg. "Don't quote me," she said. -> Dontquotemeshesaid
# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
is_palindrome = 'False'
if changed_sent.lower() == changed_sent[::-1].lower():
   is_palindrome = 'True'
print('8. Is palindrome? ' + is_palindrome)
# 9. Count the number of each vowel in the input string (from #7).
vowels = 'aeiou'
print('9. Count each vowel: ' + str({letter: sentence.lower().count(letter) for letter in vowels}))
 
# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.  
# eg. 2 5 -> 0, 2, 6, 12
bounds = [int(x) for x in input("Type two integers (lower bound and upper bound): ").strip().split()]
nums = [x**2 - 3*x + 2 for x in range(min(bounds),max(bounds)+1)]
results = ''.join(str(x)+' ' for x in nums).strip()
print("10. Evaluate f(k)=k^2 - 3k + 2 from "+str(bounds[0]) + " to " + str(bounds[1])+ " : " + results)
 
# 11. Given an input of a string, determines a character with the most number of occurrences.
sentence = input("Type a string: ").strip()
occur = {}
for i in sentence:
   if i in occur:
      occur[i] += 1
   else:
      occur[i] = 1
most = []
   #count = max(occur, key = occur.get)
count = max(occur.values())
for i in occur:
   if occur.get(i) == count:
       most.append(i)
   #most = max(occur, key = occur.get) if occur else None
print("11. Most occurred char: " + ''.join(str(x)+ ' ' for x in most).strip())
# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
splitsent = sentence.split()
vowellist = [s for s in splitsent if s[0].lower() in vowels and s[-1] in vowels]
print('12. List of words starting and ending with vowels: '+str(vowellist))
# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
capslist = [s[0].upper() + s[1:] for s in splitsent]
print('13. Capitalize starting letter of every word: ' + ''.join(str(x)+' ' for x in capslist).strip())
# 14. With the input string from #11, prints out the string with each word in the string reversed.
print('14. Reverse every word: ' + ''.join(s[::-1] + ' ' for s in splitsent))
# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy
search = splitsent.pop(0)
replacement = splitsent.pop(0)
for i in range(len(splitsent)):
   if splitsent[i] == search:
      splitsent[i] = replacement
new_sentence = ''.join(x + ' ' for x in splitsent).strip()
new_sentence.replace(search,replacement)
print('15. Find the first and replace with the second: '+new_sentence)
# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
duplstring = input('Type a string to remove all duplicate chars: ')
charlist = []
for x in duplstring:
   if x not in charlist:
      charlist.append(x)
print('16. Remove all duplicat chars: '+ ''.join(s for s in charlist))
# 17. Given an input of a string, determines whether the string contains only digits.
digitstring = input('Type a string to check if it has only digits or not: ')
digits_only = digitstring.isnumeric()
print('17. Is a number? '+str(digits_only))
# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
# converts it to a number, and prints out the decimal value.
is_binary = True
if digits_only == True:
   for x in digitstring:
      if x != '1' and x != '0':
         is_binary = False
if is_binary == True:
   print('18. It is a binary number: '+str(int(digitstring,2)))
else:
   print('18. Not binary number')
# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
first_string = input('Type the first string to check anagram: ')
sec_string = input('Type the second string to check anagram: ')
is_anagram = True
if sorted(first_string) != sorted(sec_string):
   is_anagram = False
print('19. Are '+first_string+' and '+sec_string+' anagram?: '+str(is_anagram))

# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
img_name = input('Type the image file name: ')
try:
   img = Image.open(img_name)
   print('20. Image dimensions: '+ str(img.size[0])+' by '+str(img.size[1]))
except IOError:
   print("20. Image doesn't exist")

# 21. Given an input of a string, find the longest palindrome within the string.
sentence = input('Type a string to ind the longest palindrome: ').replace(" ",'')
results = []
for i in range(len(sentence)):
   for j in range(0,i):
      part = sentence[j:i+1]
      if part == part[::-1]:
         results.append(part)
max_len = results[0]
for x in results:
   if len(x) > len(max_len):
      max_len = x
print('21. Longest palindrome within the string: ' + str(max_len))
 
# 22. Given an input of a string, find all the permutations of a string.
per_sentence = input('Type a string to do permutation: ')
s = [''.join(x) for x in permutations(per_sentence)]
print('22. all permutations: '+str(s))
# 23. Given the input string from #22, find all the unique permutations of a string.
print('23. all unique permutations: '+str(set(s)))
# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
long_sent = list(input('Type a string to find the longest non-decreasing sub: '))
len_max = 0
cur_string = long_sent.pop(0)
fin_string = cur_string
for x in long_sent:
   if x >= cur_string[-1]:
      cur_string = cur_string+x
   else:
      cur_string = x
   if len(cur_string) > len(fin_string):
      fin_string = cur_string
print('24. longest non-decreasing sub: '+fin_string)

