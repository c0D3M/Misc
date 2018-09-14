**ASCII**
8 bits , control characters but not printable often,  
If a C program want to send these ASCII, it can be done in following way  
```
./a.out "$(printf "AAAAA\x08\x32\x20\xfa\x10\x16")"
```
**base64**
6 bits, contains only printable characters  
so a 3 bytes ASCII can be represented as 4 base 64 characters,  
Often used in cryptography, like PEM format useds it.  
![](https://www.imperva.com/blog/wp-content/uploads/2018/04/B64-5.png)  

Converter: https://cryptii.com/base64-to-hex  

**UTF-8**
Variable length encoding scheme, range from 1 byte to 4 byte.  
First 128(0-127) characters corresponds  one-to-one to ASCII.  
2 byte represents Hebrew etc  
3 bytes Japanese, Korean etc  
4 byte emoji etc  
Check table on wiki, which tells if an icon need how many bytes to represent.  

**UTF-16**
minimum 2 bytes to represent. 2 or 4 byte.

**UTF-32**
Fixed 4 byte. Not compatible with ASCII.

**base65536** 
uses 16 bits as compare to 6 bits of base 64.  
inefficient as compared base64, for example if you have to send 'A' ,  
base65536 will send 16 bits as opposed to 6 bits of base 64/UTF-8(8 bits).  
base65536 choses safe codepoints from Unicode code point.  
https://qntm.org/safe
