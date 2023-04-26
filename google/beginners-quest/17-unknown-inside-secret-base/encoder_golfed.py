from struct import *
R=range
B=bytes
def encode(s):
  a=B(R(65,91))
  return B(p^q for p,q in zip(b"BEGN\0\0\0\x1a"+a.lower()+b"DATA"+pack(">I",len(s))+s+b"END.\0\0\0\x1a"+a,[g&255 for g in R(2,9999)if all(g%k for k in R(2,g))]))
#END
