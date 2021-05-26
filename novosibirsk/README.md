# Novosibirsk

This solution is based around a format string vulnerability.

This challenge is not that much different than `Addis Ababa`. There is a format string vulnerability that is present that can be leveraged to write data to the unprotected memory space. The limitations of this format string vulnerablity are no NULL bytes and less than 0x1F4 bytes long. To bypass HSM-2 I just targeted the interrupt call and changed the 0x7E to 0x7F which is `unlock_door`. Same approach as `Addis Ababa` write the pointer target, we don't need a `%x` because the stack starts directly at our input, then add filler to print the number of characters we want (0x7F-2 for the address) then a `%n` to write the value.

The solution used for this challenge was `c8444242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242424242256e`