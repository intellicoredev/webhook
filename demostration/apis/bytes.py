import binascii
import struct
from binascii import hexlify, unhexlify


def example():
    data = "419b3365c2c653cf00000002"
    data = '000000003f844444ffffff02'

    print('1. data_original: {}'.format(data))

    # Starting with a hex string you can unhexlify it to bytes
    data_bytes = binascii.unhexlify(data)
    print('2. ata_bytes: {}'.format(data_bytes))

    # Given raw bytes, get an ASCII string representing the hex values
    hex_data = binascii.hexlify(data_bytes)  # 12 bytes values 0 and 255
    print('3. len {} data_hex: {}'.format(len(hex_data), hex_data))

    # The resulting value will be an ASCII string but it will be a bytes type
    # It may be necessary to decode it to a regular string
    text_string = hex_data.decode('utf-8')  # Result is string "00ff"
    print('4. data_text_string: {}'.format(text_string))

    mutable_bytes = bytearray(data_bytes)

    print('5. mutable_bytes: {} {}'.format(len(mutable_bytes), mutable_bytes))
    j = 0
    for i in mutable_bytes:
        # print('{},{}'.format(i, j))
        print('6. {},{}'.format(j, mutable_bytes[j]))
        j = j + 1

    lat = mutable_bytes[0:4]
    lng = mutable_bytes[4:8]
    b1 = mutable_bytes[8:8]
    b2 = mutable_bytes[9:9]
    b3 = mutable_bytes[10:10]
    cmd = mutable_bytes[11:12]

    lat_str = ''.join(chr(i) for i in lat)
    print('7. bytes lat {}'.format(lat_str))

    lng_str = ''.join(chr(i) for i in lng)
    print('8. bytes lng {}'.format(lng_str))

    str_b1 = ''.join(chr(i) for i in b1)
    print('9. bytes b1 {}'.format(str_b1))

    str_b2 = ''.join(chr(i) for i in b2)
    print('10. bytes b2 {}'.format(str_b2))

    str_b3 = ''.join(chr(i) for i in b3)
    print('11. bytes b3 {}'.format(str_b3))

    str_cmd = ''.join(chr(i) for i in b2)
    print('12. bytes cmd {}'.format(str_b2))

    hex_data = binascii.hexlify(lat_str)  # 4  bytes values 0 and 255
    print('13. size {} data_hex: {}'.format(len(lat_str), hex_data))

    print('14. size mutable_bytes {} '.format(len(mutable_bytes)))
    print('15. {} {} {} {} {} {}'.format(lat, lng, b1, b2, b3, cmd))

    hex_data = binascii.hexlify(lat)  # 4  bytes values 0 and 255
    print('16. size {} data_hex: {}'.format(len(lat), hex_data))

    hex_data = binascii.hexlify(lng)  # 4  bytes values 0 and 255
    print('17. size {} data_hex: {}'.format(len(lng), hex_data))

    data = lat
    b = ''.join(chr(i) for i in data)
    struct.unpack('>f', b)
    print('18. lat len {} data_str: {}'.format(len(data), b))

    hex_data = binascii.hexlify(data)  # 4  bytes values 0 and 255
    print('19. size {} lat_hex: {}'.format(len(lat), hex_data))

    data = lng
    b = ''.join(chr(i) for i in data)
    struct.unpack('>f', b)
    val = b

    print('20. lat {} val_struct: {}'.format(lat, val))
    print('21. lng {} data_str: {}'.format(len(data), b))

    hex_data = binascii.hexlify(data)
    print('size {} lng_hex: {}'.format(len(lng), hex_data))

    data_str = '419b3365c2c653cf00000002'

    # data_str = '000000000000000001100002'
    data_str = '419b3365c2c653cf00000002'

    result = bytearray.fromhex(data_str)
    print('size {} data_str: {}'.format(len(result), result))

    lat = result[0:4]
    val = struct.unpack('>f', lat)
    print('lat {} val_struct: {}'.format(lat, val))

    lng = result[4:8]
    val = struct.unpack('>f', lng)
    print('lng {} val_struct: {}'.format(lng, val))

    b1 = result[8]
    b2 = result[9]
    b3 = result[10]
    cmd = result[11]

    print('b1 {} b2 {} b3 {} cmd {}'.format(b1, b2, b3, cmd))

    print('result: {} {}'.format(len(result), result))
    j = 0
    for i in result:
        # print('{},{}'.format(i, j))
        print('{},{}'.format(j, result[j]))
        j = j + 1


def decode_data(data_str):
    data_sigfox = '000000003f844444ffffff02'
    data_sigfox = data_str
    print('data_sigfox {}'.format(data_sigfox))

    # Starting with a hex string you can unhexlify it to bytes
    data_bytes = binascii.unhexlify(data_sigfox)
    print('data_bytes {}'.format(data_bytes))

    # Given raw bytes, get an ASCII string representing the hex values
    hex_data = binascii.hexlify(data_bytes)  # Two bytes values 0 and 255
    print('hex_data {}'.format(hex_data))

    # The resulting value will be an ASCII string but it will be a bytes type
    # It may be necessary to decode it to a regular string
    text_string = hex_data.decode('utf-8')  # Result is string "00ff"
    print('text_string {}'.format(text_string))

    data_str = text_string
    result = bytearray.fromhex(data_str)
    print('size {} data_str: {}'.format(len(result), result))

    lat = result[0:4]
    val = struct.unpack('>f', lat)
    print('Latitud: lat {} val_struct: {}'.format(lat, val))

    lng = result[4:8]
    val = struct.unpack('>f', lng)
    print('Longitud: lng {} val_struct: {}'.format(lng, val))

    b1 = result[8]
    b2 = result[9]
    b3 = result[10]
    cmd = result[11]

    print('b1 {} b2 {} b3 {} cmd {}'.format(b1, b2, b3, cmd))

    print('result: {} {}'.format(len(result), result))
    j = 0
    for i in result:
        # print('{},{}'.format(i, j))
        print('{},{}'.format(j, result[j]))
        j = j + 1

    lat = bytes(tuple(result[0:4]))
    lng = bytes(tuple(result[4:8]))
    byte_b1 = bytes(b1)
    byte_b2 = bytes(b2)
    byte_b3 = bytes(b3)
    byte_cmd = bytes(cmd)

    all_data_in_bytes = bytes(tuple(result))

    print('lat {},lng {}'.format(lat, lng))
    print('b1 {},b2 {} b3 {} cmd {}'.format(byte_b1, byte_b2, byte_b3, byte_cmd))

    print('All data in bytes: {} {}'.format(all_data_in_bytes, type(all_data_in_bytes)))

    a_byte = bytes_to_int(byte_b1)
    i = a_byte  # Get the integer value of the byte

    bin = "Bin: {0:b}".format(i)  # binary: 11111111
    hex = "Hex: {0:x}".format(i)  # hexadecimal: ff
    oct = "Oct: {0:o}".format(i)  # octal: 377
    dec = "Dec: {0:d}".format(i)  # decimal:

    print(bin)
    print(hex)
    print(oct)
    print(dec)
    print(a_byte)

    byte1 = int(byte_b1, 10)  # 240
    bit_mask = int('00000001', 2)  # Bit 1
    print(bit_mask & byte1)  # Is bit set in byte1?

    bin = "Bin: {0:b}".format(byte1)  # binary: 11111111
    print(bin)

    return ""


def decode_sigfox(data_str):
    data_sigfox = data_str
    data_bytes = binascii.unhexlify(data_sigfox)
    hex_data = binascii.hexlify(data_bytes)  # Two bytes values 0 and 255
    text_string = hex_data.decode('utf-8')  # Result is string "00ff"

    data_str = text_string
    result = bytearray.fromhex(data_str)

    lat = result[0:4]
    val_lat = struct.unpack('>f', lat)

    lng = result[4:8]
    val_lng = struct.unpack('>f', lng)

    b1 = result[8]
    b2 = result[9]
    b3 = result[10]
    cmd = result[11]

    lat = bytes(tuple(result[0:4]))
    lng = bytes(tuple(result[4:8]))
    byte_b1 = b1
    byte_b2 = b2
    byte_b3 = b3
    byte_cmd = cmd

    all_data_in_bytes = bytes(tuple(result))

    print('byte_b1: {} type {}'.format(byte_b1, type(byte_b1)))
    i = byte_b1
    bin = "{0:b}".format(i)  # binary: 11111111
    hex = "{0:x}".format(i)  # hexadecimal: ff
    oct = "{0:o}".format(i)  # octal: 377

    print(bin)
    print(hex)
    print(oct)

    print('byte_b2: {} type {}'.format(byte_b2, type(byte_b2)))
    print('byte_b3: {} type {}'.format(byte_b3, type(byte_b3)))
    print('byte_cmd: {} type {}'.format(byte_cmd, type(byte_cmd)))

    # print ('lat {},lng {}'.format(lat, lng))
    # print ('b1 {},b2 {} b3 {} cmd {}'.format(byte_b1, byte_b2, byte_b3, byte_cmd))

    # print ('All data in bytes: {} {}'.format(all_data_in_bytes, type(all_data_in_bytes)))

    # str_lat = ''.join(chr(i) for i in lat)
    # str_lng = ''.join(chr(i) for i in lng)

    return val_lat, val_lng, lat, lng, byte_b1, byte_b2, byte_b3, byte_cmd, all_data_in_bytes


def define_bytes(data_str):
    bit_8 = 0b10000000
    bit_7 = 0b01000000
    bit_6 = 0b00100000
    bit_5 = 0b00010000
    bit_4 = 0b00001000
    bit_3 = 0b00000100
    bit_2 = 0b00000010
    bit_1 = 0b00000001

    bit_hex_8 = 0x80
    bit_hex_7 = 0x40
    bit_hex_6 = 0x20
    bit_hex_5 = 0x10
    bit_hex_4 = 0x8
    bit_hex_3 = 0x4
    bit_hex_2 = 0x2
    bit_hex_1 = 0x1

    mask_8 = bit_hex_8
    mask_7 = bit_hex_7
    mask_6 = bit_hex_6
    mask_5 = bit_hex_5
    mask_4 = bit_hex_4
    mask_3 = bit_hex_3
    mask_2 = bit_hex_2
    mask_1 = bit_hex_1

    data = '000000003f844444ffffff02'


def parse_byte(byte=255):
    bit_8 = 0b10000000
    bit_7 = 0b01000000
    bit_6 = 0b00100000
    bit_5 = 0b00010000
    bit_4 = 0b00001000
    bit_3 = 0b00000100
    bit_2 = 0b00000010
    bit_1 = 0b00000001

    bit_hex_8 = 0x80
    bit_hex_7 = 0x40
    bit_hex_6 = 0x20
    bit_hex_5 = 0x10
    bit_hex_4 = 0x8
    bit_hex_3 = 0x4
    bit_hex_2 = 0x2
    bit_hex_1 = 0x1

    mask_8 = 0x80
    mask_7 = 0x40
    mask_6 = 0x20
    mask_5 = 0x10
    mask_4 = 0x8
    mask_3 = 0x4
    mask_2 = 0x2
    mask_1 = 0x1

    # byte_int = int.from_bytes(bytes, byteorder == 'little')

    b8 = byte & mask_8
    b7 = byte & mask_7
    b6 = byte & mask_6
    b5 = byte & mask_5
    b4 = byte & mask_4
    b3 = byte & mask_3
    b2 = byte & mask_2
    b1 = byte & mask_1

    return b8, b7, b6, b5, b4, b3, b2, b1


def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result


def int_to_bytes(value, length):
    result = []

    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)

    result.reverse()

    return result


def print_byte(label, byte=0):
    print('{} {} type {}'.format(label, byte, type(byte)))
    i = byte
    bin = "{0:b}".format(i)  # binary: 11111111
    hex = "{0:x}".format(i)  # hexadecimal: ff
    oct = "{0:o}".format(i)  # octal: 377
    dec = "{0:d}".format(i)  # octal: 377

    print(label, bin, oct, dec, hex)


def set_bit(v, index, x):
    """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
    mask = 1 << index  # Compute mask, an integer with just bit 'index' set.
    v &= ~mask  # Clear the bit indicated by the mask (if x is False)
    if x:
        v |= mask  # If x was True, set the bit indicated by the mask.
    return v


def square(x):
    return (x ** 2)


def cube(x):
    return (x ** 3)


if __name__ == "__main__":
    print("Decode")

    data_sigfox = '000000003f844444ffffff02'
    # data_sigfox = "419b3365c2c653cf00000002"
    data_sigfox = '000000003f844444ffffff02'
    data_sigfox = '419b3365c2c653cabcdefa02'

    data_body = decode_sigfox(data_sigfox)
    print('1. Decode data.body {}'.format(data_body))
    lat_float, lng_float, lat, lng, b1, b2, b3, cmd, all_data_in_bytes = data_body
    print('2. lat_float {},lng_float {} lat {},lng {}'.format(lat_float, lng_float, lng, lat))
    print('3. b1 {},b2 {} b3 {} cmd {}'.format(b1, b2, b3, cmd))
    print('4. All data in bytes: {} {}'.format(all_data_in_bytes, type(all_data_in_bytes)))
    r8, r7, r6, r5, r4, r3, r2, r1 = parse_byte(b1)
    print('5. Reles {} {} {} {} {} {} {} {}| {}'.format(r1, r2, r3, r4, r5, r6, r7, r8, b1))
    r8, r7, r6, r5, r4, r3, r2, r1 = parse_byte(b2)
    print('6. b2 {} {} {} {} {} {} {} {}| {}'.format(r1, r2, r3, r4, r5, r6, r7, r8, b2))
    r8, r7, r6, r5, r4, r3, r2, r1 = parse_byte(b3)
    print('7. b3 {} {} {} {} {} {} {} {} |{}'.format(r1, r2, r3, r4, r5, r6, r7, r8, b3))
    r8, r7, r6, r5, r4, r3, r2, r1 = parse_byte(cmd)
    print('8. cmd {} {} {} {} {} {} {} {} |{}'.format(r1, r2, r3, r4, r5, r6, r7, r8, cmd))

    print_byte("b1", b1)
    print_byte("b2", b2)
    print_byte("b3", b3)
    print_byte("cmd", cmd)

    mask_1 = int('10000000', 2)  # Bit 1
    mask_2 = int('01000000', 2)  # Bit 1
    mask_3 = int('00100000', 2)  # Bit 1
    mask_4 = int('00010000', 2)  # Bit 1
    mask_5 = int('00001000', 2)  # Bit 1
    mask_6 = int('00000100', 2)  # Bit 1
    mask_7 = int('00000010', 2)  # Bit 1
    mask_8 = int('00000001', 2)  # Bit 1
    print('10. Masked bytes')

    print('b1 ', mask_1 & b1, mask_2 & b1, mask_3 & b1, mask_4 & b1, mask_5 & b1, mask_6 & b1, mask_7 & b1,
          mask_8 & b1)  # Is bit set in byte1?
    print('b2 ', mask_1 & b2, mask_2 & b2, mask_3 & b2, mask_4 & b2, mask_5 & b2, mask_6 & b2, mask_7 & b2,
          mask_8 & b2)  # Is bit set in byte1?
    print('b3 ', mask_1 & b1, mask_2 & b3, mask_3 & b3, mask_4 & b3, mask_5 & b3, mask_6 & b3, mask_7 & b3,
          mask_8 & b3)  # Is bit set in byte1?
    print('cmd ', cmd, mask_1 & cmd, mask_2 & cmd, mask_3 & cmd, mask_4 & cmd, mask_5 & cmd, mask_6 & cmd, mask_7 & cmd,
          mask_8 & cmd)  # Is bit set in byte1?

    # data_sigfox = '419b3365c2c653cf00000002'
    # print ("Decode {}", decode_data(data_sigfox))

    b1_str_bits = "{0:08b}".format(b1)
    b1_list_bits = list(b1_str_bits)
    bits_list_nums_b1 = list(map(lambda x: 1 if x == '1' else 0, b1_list_bits))
    print(bits_list_nums_b1)
    for i in bits_list_nums_b1:
        print(i)


{% for key in data %}
              <tr>
                  <td>{{ key.device }}</td>
                  <td>{{ key.time }}</td>
                  <td>{{ key.station }}</td>
                  <td>{{ key.data }}</td>
                  <td>{{ key.lat }}</td>
                  <td>{{ key.lng }}</td>
                  <td>{{ key.reles }}</td>

                  <td>{{ key.energia }}</td>
                  <td>{{ key.blue }}</td>
                  <td>{{ key.duplicate }}</td>
                  <td>{{ key.snr }}</td>
                  <td>{{ key.avgSnr }}</td>
                  <td>{{ key.rssi }}</td>
                  <td>{{ key.seqNumber }}</td>
              </tr>
          {% endfor %}
