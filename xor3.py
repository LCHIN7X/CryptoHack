from pwn import xor

hexs = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data = bytes.fromhex(hexs)

# try keys 0..255
for k in range(256):
    out = xor(data, bytes([k]))
    try:
        s = out.decode('utf-8')
    except UnicodeDecodeError:
        continue
    if all(32 <= ord(c) < 127 for c in s):
        print(k, hex(k), s)


