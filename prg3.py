# Write a code that checks if two given strings are anagrams
s = input('enter your string : ')
ref = ""
for i in s:
    ref = i + ref
if ref == s:
    print('Yes')
else:
    print('No')