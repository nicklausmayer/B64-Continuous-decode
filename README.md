## Used during NahamCon CTF 2024
- This python program will decode a given file encoded in base 64 until a given string has been found.
- Useful for CTF competitions
---
```
#!/bin/env python
import base64
flag = open("file", 'r').read()
flag = base64.b64decode(flag).decode('utf-8')

while "flag{" not in flag:	 
	flag = base64.b64decode(flag).decode('utf-8')

print(flag)
```

1. We import the base64 package, included with python since 2.4
2. We open and read the file containing the flag, encoded in base64 repeatedly
3. We use the base64 module, 'b64decode' function to decode the flag. Then we use the python decode function to decode the bytes returned from the b64decode function.
	- You could also decode using ascii as well
4. Then we begin a while loop to decode the flag until it returns a string that starts with "flag{"
5. The flag only prints after the loop has completed

---
### POC: 
During NahamCon CTF 2024, for the challenge Base3200 we were given a file containing 79918301 characters.
[Linux 'wc' command snippet.png](https://i.imgur.com/b3DPn4f.png)
The name of the challenge gave away the fact that we would use a variation of a base encoding, so I attempted to decode using base64. First using the `base64 -d` bash command to ensure that it was encoded using base64. 
[Linux 'base64 -d' & cut command snippet.png](https://i.imgur.com/YC9gO5f.png)
Since the output of the decode was very long I used the `cut` command to decrease the output.
Knowing that the flag is encoded in base64, most likely multiple times I tried to manually decode by copying and pasting `base64 -d`.
[Continued decoding.png](https://i.imgur.com/2uqohqT.png)
I could very well continue to pipe `base64 -d`, but instead I decided to write a python program to do the work for me.
[Retrieved flag.png](https://i.imgur.com/oEAOdHG.png)
Boom! Now we have retrieved the decoded flag.

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
