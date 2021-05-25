from argparse import ArgumentParser
import sys

def decode_binary(input_file, output_file):
    next_addr = 0

    for line in input_file:
        addr,data = line.split(':')[:2]

        addr = int(addr, 16)

        data = ''.join(data.split(' ')[3:11]).strip()

        if data == '*':
            data = '00'*16

        print('{:04x}: {}'.format(addr, data))

        data = bytes.fromhex(data)

        if next_addr == addr:
            output_file.write(data)
        else:
            difference = addr - next_addr
            blank_data = bytes.fromhex('00'*difference)
            output_file.write(blank_data)
            output_file.write(data)

        next_addr = addr + 16



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        with open(args.output_file, 'wb') as o:
            decoded_binary = decode_binary(f, o)