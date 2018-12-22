import collections, sys from heapq
import heappush, heappop, heapify from collections
import defaultdict


source = open("C:\\Users\\Swaroop\\Desktop\\huffman.txt")

def char_frequency(str1):
   dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,' ':0,'.':0,',':0,"'":0,'!':0,'?':0}
   for ch in strl1:
       for n in ch:
           keys = dict.keys()
           if n in keys:
               dict[n] += 1

   return dict




abc=""

for a in source:
   for ch in a:
       if ch in {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','?','!',"'",'.',','}:
           abc = abc +ch

huffman_dict=char_frequency(abc)


def encode(symb2freq):
   """Huffman encode the given dict mapping symbols to weights"""
   heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
   heapify(heap)
   while len(heap) > 1:
       lo = heappop(heap)
       hi = heappop(heap)
       for pair in lo[1:]:
           pair[1] = '0' + pair[1]
       for pair in hi[1:]:
           pair[1] = '1' + pair[1]
       heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
   return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

huff = encode(huffman_dict)


print ("Symbol\tWeight\tHuffman Code")
for p in huff:
   print ("%s\t%s\t%s" % (p[0], huffman_dict[p[0]], p[1]))