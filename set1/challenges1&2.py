def hex_to_bin(s):
    hex_to_bin_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }

    res = ""
    for c in s:
        res += hex_to_bin_dict[c]

    return res

def bin_to_hex(s):
    bin_to_hex_dict = {
        10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"
    }

    res = ""
    count = 3
    val = 0

    for i in range(len(s)):
        if s[i] == "1":
            val += 2**count
        count -= 1

        if count < 0:
            if val >= 10:
                res += bin_to_hex_dict[val]
            else:
                res += str(val)
            count = 3
            val = 0

        
    return res

def bin_to_base64(s):
    base64_dict = {
        0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H",
        8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P",
        16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X",
        24: "Y", 25: "Z", 26: "a", 27: "b", 28: "c", 29: "d", 30: "e", 31: "f",
        32: "g", 33: "h", 34: "i", 35: "j", 36: "k", 37: "l", 38: "m", 39: "n",
        40: "o", 41: "p", 42: "q", 43: "r", 44: "s", 45: "t", 46: "u", 47: "v",
        48: "w", 49: "x", 50: "y", 51: "z", 52: "0", 53: "1", 54: "2", 55: "3",
        56: "4", 57: "5", 58: "6", 59: "7", 60: "8", 61: "9", 62: "+", 63: "/"
    }

    res = ""
    count = 5
    val = 0

    for i in range(len(s)):
        if s[i] == "1":
            val += 2**count
        count -= 1

        if count < 0:
            res += base64_dict[val]
            count = 5
            val = 0
        
    return res

def xor_two_buffers(a, b):
    res = ""
    decoded1 = hex_to_bin(a)
    decoded2 = hex_to_bin(b)

    for i in range(len(decoded1)):
        res += str(int(decoded1[i]) ^ int(decoded2[i]))

    result = bin_to_hex(res)

    return result
