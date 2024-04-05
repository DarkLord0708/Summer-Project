a1 = 0xaaaaaaaaaaaaaaaa
a2 = 0x5555555555555555

b1 = 0xcccccccccccccccc
b2 = 0x3333333333333333

c1 = 0xf0f0f0f0f0f0f0f0
c2 = 0x0f0f0f0f0f0f0f0f

d1 = 0xff00ff00ff00ff00
d2 = 0x00ff00ff00ff00ff

# first
ob = "0b110110101110000010101000101100111101101011100000"
b6 = ob[:-16]
x = int(b6,2)
y1 = bin(int(bin(x & d2)+"0"*8,2))
y2 = bin(int(bin(x & d1)[:-8],2))
s1 = y1[2:]
s2 = y2[2:]

while len(s1)%8 !=0:
    s1 = "0"+s1

while len(s2)%8 !=0:
    s2 = "0"+s2

l1 = [s1[i:i+8] for i in range(0,len(s1),8)]
l2 = [s2[i:i+8] for i in range(0,len(s2),8)]
b5 = l1[0]+l2[0]+l1[2]+l2[2]
b5 = "0b"+b5

# second
x = int(b5,2)
y1 = bin(int(bin(x & c2)+"0"*4,2))
y2 = bin(int(bin(x & c1)[:-4],2))
s1 = y1[2:]
s2 = y2[2:]

while len(s1)%4 !=0:
    s1 = "0"+s1

while len(s2)%4 !=0:
    s2 = "0"+s2


l1 = [s1[i:i+4] for i in range(0,len(s1),4)]
l2 = [s2[i:i+4] for i in range(0,len(s2),4)]
b4 = l2[0]+l1[0]+l2[2]+l1[2]+l2[4]+l1[4]+l2[6]
b4 = "0b"+b4

# third
x = int(b4,2)
y1 = bin(int(bin(x & b2)+"0"*2,2))
y2 = bin(int(bin(x & b1)[:-2],2))
s1 = y1[2:]
s2 = y2[2:]

while len(s1)%2 !=0:
    s1 = "0"+s1

while len(s2)%2 !=0:
    s2 = "0"+s2


l1 = [s1[i:i+2] for i in range(0,len(s1),2)]
l2 = [s2[i:i+2] for i in range(0,len(s2),2)]
b3 = l1[0]+l2[0]+l1[2]+l2[2]+l1[4]+l2[4]+l1[6]+l2[6]+l1[8]+l2[8]+l1[10]+l2[10]+l1[12]+l2[12]
b3 = "0b"+b3

# fourth
x = int(b3,2)
y1 = bin(int(bin(x & a2)+"0"*1,2))
y2 = bin(int(bin(x & a1)[:-1],2))
s1 = y1[2:]
s2 = y2[2:]

while len(s1)%1 !=0:
    s1 = "0"+s1

while len(s2)%1 !=0:
    s2 = "0"+s2


l1 = [s1[i:i+1] for i in range(0,len(s1),1)]
l2 = [s2[i:i+1] for i in range(0,len(s2),1)]

b2 = ""
for i in range(0,26,2):
    b2 = b2 +l2[i]+l1[i]
b2 = b2 + '1'

ans = int(b2,2)
flag = "flag{"+str(ans)+"}"
print(flag)
