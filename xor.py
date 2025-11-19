from pwn import xor


label = b"label" #tell python this is a 


new_bytes = xor(label, b"\x0d") #0x0d = 13

new_string = new_bytes.decode('latin-1') #turn number back into lettter
print("crypto{" + new_string + "}")
