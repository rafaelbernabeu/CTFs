from struct import *
r=range
h=bytes
def t(a, b):
  return a+pack(">I",len(b))+b
def encode(s):
  a=h(r(65, 91))
  m=t(b"BEGN",a.lower())+t(b"DATA",s)+t(b"END.",a)
  n=[g&255 for g in r(2, 7919)if not[k for k in r(2, g)if g%k<1]]
  return h(p^q for p,q in zip(m,n))
#END