import math
from typing import final
"""   
    +--------- PYTHON BIT OPERATORS, FUNCTIONS, AND TRICKS ----------------+
    |  operator          meaning                  examples                 |
    |   &          and                     1010 & 1100 = 1000              |
    |   |          non-exclusive or        1010 | 1100 = 1110              |
    |   ^          exclusive or            1010 ^ 1100 = 0100              |
    |   ~          not (flip all bits)    ~1010        = ????              |
    |              flip all bits           0x1F-(0b11010) = 101            |
    |   <<         shift left  n bits      101    << 3 = 101000            |
    |   >>         shift right n bits      101000 >> 3 = 101               |
    +----------------------------------------------------------------------+
    |   0b or 0B   interpret as binary      0b10101    = 21                |
    |   bin()      express as binary        bin(21)    = 10101             |
    +----------------------------------------------------------------------+
    |  turn ON  nth bit from right: num |=  (1 << n)                       |
    |  turn OFF nth bit from right: num &= ~(1 << n)                       |
    |  flip     nth bit from right: num ^=  (1 << n)                       |
    |  test     nth bit from right: if (num & (1 << n))  > 0: ...          |
    |                               if (num & (1 << n)) == 0: ...          |
    |  clear the right-most bit:    num = num & (num-1)                    |
    |  smear right-most 1 to right: num | (num-1)                          |
    |  extract right-most 1:        num = num & -num (e.g., 101100 ->10)   |
    |  extract nth bit from left:   bit = (num >> n) & 1                   |
    |  mod 2**n:                    x mod 2**n = x &(2**n - 1)             |
    +----------------------------------------------------------------------+
    |  Below, the 0 is a zero, not a letter in 0b (= 0B).                  |
    |  print (0b10101)           # = 21                                    |
    |  print ( int("10101", 2) ) # = 21 (string to binary integer)         |
    |  print(bin(21))            # = 0b10101                               |
    |  print(bin(21)[2:])        # =   10101                               |
    |  n = 0b1001                                                          |
    |  print(n.bit_length())     # = 4                                     |
    +----------------------------------------------------------------------+
"""
'''
binary string
print(bin(5)) 0b101 or 0B101
print(bin(5)[2:]) 101
n = 0b001
print(n) 9
print(bin(n)[2:]) 1001
print(n.bit_length()) 4

convert base
print(int('101',2)) 5



a = 0b1001 #1001 --> 1001 ~1001 0110 --> 1s 1001 --> 2s 1010 -->-10
b = 0b1100 #1100
print('and',bin(a & b)[2:]) #1000
print('or',bin(a | b)[2:]) #1101
print('xor',bin(a^b)[2:]) #101
print('not',~a) #signed bit number -10
print('shift left',bin(a<<1)[2:],a<<1) #10010 18
print('shift right',bin(a >> 1)[2:], a>>1) #100 4

num - 0b1000
n = 3
num |= (1 << (n-1)) #turn ON 3rd bit from right
print(bin(nim)[2:]) # 1100

num &= ~(1 << (n-1)) #turn OFF 3rd bit from right
'''
# Question 1: What is the 4-bit binary representation of number?
#return bin((0b1111 = int(bin(number)[3:],2)) + 1)[2:]

def fourBitBinaryRep(number):
   """ Write your code here """
   # num = list(bin(number).replace('0b',''))
   # for x in range(len(num)):
   #    if num[x] == 1:
   #       num[x] = 0
   #    elif num[x] == 0:
   #       num[x] = 1 
   #num = bin(number).replace('0b','')
   #flippednum = ''
   #for x in num:
   #   if x == '1' or x == '0':
   #      flippednum = flippednum+x
   #i = len(flippednum)-1
   #while flippednum[i] != '1':
   #   i -= 1
   #if i == -1:
   #   return '1'+flippednum
   #n = i-1
   #finalnum = flippednum[i]
   #while n >= 0:
   #   if flippednum[n] == '1':
   #      finalnum = '0'+finalnum
   #   elif flippednum[n] == '0':
   #      finalnum = '1'+finalnum
   #   n -= 1
   #return finalnum
   y = bin((0b1111 ^ int(bin(number)[3:],2)) + 1)[2:]
   num = 4-len(y)
   return '0'*num + y
   
   
   

# Question 2: # Create a binary number of max bits. Initially set every bit to 1. By the sieve method
# of Eratosthenes, set to zero any bit whose position number is not a prime number.

def isPrime(num):
   if num > 1:
      for i in range(2, num//2+1):
         if num % i == 0:
            return False
      return True
   return False


def sieveOfEratosthenesUsingBits(max):     # max = the number of bits
   """ Write your code here """
   #make all numbers 1111111
   #if not prime number make num=0
   #print num at pos where thing is 1
   numslist = []
   testlist = []
   for x in range(1,max+1):
      numslist.append([x,1])
   for y in numslist:
      if isPrime(y[0]) == False:
         y[1] = 0
   for z in numslist:
      if z[1] == 1:
         testlist.append(z[0])
   for x in testlist:
       print(x, end = ' ')
  
def main():
   number = -13    
   #print(isPrime(4))
   print(fourBitBinaryRep(number))  # -13 (= -0b1101) is 0011
   sieveOfEratosthenesUsingBits(100)   # total 25 prime numbers should be printed
   
if __name__ == '__main__':  main()
   