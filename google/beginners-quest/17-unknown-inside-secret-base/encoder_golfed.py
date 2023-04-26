import struct as s
def t(a, b):
  return b''.join([bytes(a, "utf-8")[:4],s.pack(">I", len(b)),b])
def y(d):
  n=[x for x in range(2,7919)if not[t for t in range(2,x)if not x%t]]
  return bytes([(d[i] ^ (n[i] & 0xff))for i in range(len(d))])
def encode(s):
  a=bytes([x for x in range(65, 91)])
  return y(b''.join([t("BEGN", a.lower()),t("DATA", s),t("END.",a)]))
#END