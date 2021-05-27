def hash_pin(input: bytes):
    hash = 0

    for i in input:
        tmp1 = hash + hash
        tmp2 = tmp1 + tmp1 + hash
        hash = tmp2 + tmp2 + i - 0x30

    return hash & 0xFFFF

def hash_username(input: bytes):
    hash = 0

    for i in input:
        tmp1 = hash + i
        tmp2 = tmp1 + tmp1
        tmp3 = tmp2 + tmp2
        tmp4 = tmp3 + tmp3
        tmp5 = tmp4 + tmp4
        hash = tmp5 + tmp5 - tmp1

    return hash & 0xFFFF

print(hex(hash_pin(b'ffff')))

print(hex(hash_username(b'AA')))
print(hex(hash_username(b'BB')))
print(hex(hash_username(b'CC')))
print(hex(hash_username(b'\xca\x3d\xfc\x50\xb9\xf4b')))