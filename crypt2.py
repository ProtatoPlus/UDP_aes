import binascii
from Crypto.Cipher import AES
from Crypto import Random

def encrypt(passwrd, message):
    msglist = []
    key = bytes(passwrd, "utf-8")
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(bytes(message, "utf-8"))
    msg = binascii.hexlify(msg)
    for letter in str(msg):
        msglist.append(letter)
    msglist.remove("b")
    msglist.remove("'")
    msglist.remove("'")
    fcipher = ''.join(msglist)
    return fcipher

def padded_hex(i, l):
    given_int = i
    given_len = l

    hex_result = hex(given_int)[2:] # remove '0x' from beginning of str
    num_hex_chars = len(hex_result)
    extra_zeros = '0' * (given_len - num_hex_chars) # may not get used..

    return ('0x' + hex_result if num_hex_chars == given_len else
            '?' * given_len if num_hex_chars > given_len else
            '0x' + extra_zeros + hex_result if num_hex_chars < given_len else
            None)

def decrypt(passwrd, message):
    msglist = []
    key = bytes(passwrd, "utf-8")
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    try:        
        msg = cipher.decrypt(binascii.unhexlify(bytes(message, "utf-8")))[len(iv):]
    except:
        print("An error occured that has yet to be patched.")
    for letter in str(msg):
        msglist.append(letter)
    msglist.remove("b")
    msglist.remove("'")
    msglist.remove("'")
    fcleartext = ''.join(msglist)
    return fcleartext