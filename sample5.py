# f=open('myfile.txt','w')
# print f
# 
# f.write("aaaaaaaaaaaaadffffffffff")
# f.write("bbbbbbbbbbbsadfasdf")
# 
# f.close()

f=open('myfile.txt','r+')

# s=f.readline()
# print s
f.write('ddgeterteryhyuru')

f.seek(5)

s1=f.read(5)
print s1

print f.tell()

f.seek(-3,2)
s2=f.read(1)
print s2

print f.tell()

# f.seek(5)
# print f.read(1)
# 
# f.seek(-3, 2)
# print f.read(1)
# 
# f.close()

import glob

s=glob.glob('*.*')
print s

