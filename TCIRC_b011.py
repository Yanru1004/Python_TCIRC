#b011 姐妹校交流

import struct
#讀取匯率、貨幣數

c,n = input().strip().split(' ')

c = struct.unpack('f',struct.pack('f',float(c)))[0]
n = int(n)

result = struct.pack('f',n/c)

result = struct.unpack('f',result)[0]

print(f'{result:0.5f}')
