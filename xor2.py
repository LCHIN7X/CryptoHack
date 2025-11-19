from pwn import xor

# Given values (hex)
KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
K2_xor_K1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
K2_xor_K3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
E = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Recover KEY2 and KEY3 using XOR properties
KEY2 = xor(KEY1, K2_xor_K1)   # KEY2 = KEY1 ^ (KEY2 ^ KEY1)
KEY3 = xor(KEY2, K2_xor_K3)   # KEY3 = KEY2 ^ (KEY2 ^ KEY3)

# Recover the FLAG
FLAG = xor(E, xor(KEY1, xor(KEY2, KEY3)))   # FLAG = E ^ KEY1 ^ KEY2 ^ KEY3

# Print the flag
print(FLAG.decode())
