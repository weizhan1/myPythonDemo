
Tests:

input ->  output

"0101" -> [2,2]
"01" -> [1,1]
"a" -> [0,0]

"0000" -> [4, 0]
"11111" -> [0,5]
"" -> [0, 0]
"1010" -> [2, 2]
"1001" - > [2, 2]
"0110" -> [2, 2]
"-0!1$0&1"-> [2, 3]
"1035 890150" -> [3, 2]
" " -> [0, 0]
"11...." very large number of input -> 

def bin_counter(ones_and_zeroes):
 zerocnt = 0
 onecnt = 0
 for c in ones_and_zeros:
   if c == '0':
     zerocnt += 1
   elif c == '1':
     onecnt += 1
 alist = [zerocnt, onecnt]
 return alist
