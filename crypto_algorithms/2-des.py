import pyDes

# كود الencryption في ال2des
def two_des_encrypt(des_key1, des_key2, message):
    des_key1 = "ABCDEFGH"
    des_key2 = "12345678"
    k = pyDes.des(des_key1, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_msg = k.encrypt(message)
    k = pyDes.des(des_key2, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_msg = k.encrypt(encrypted_msg)
    return encrypted_msg

#
# # كود الdecryption في ال2des
# def two_des_decrypt(key1, key2, encrypted_msg):
#     k = pyDes.des(key2, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
#     decrypted_msg = k.decrypt(encrypted_msg)
#     k = pyDes.des(key1, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
#     decrypted_msg = k.decrypt(decrypted_msg)
#     return decrypted_msg
#

des_key1 = "ABCDEFGH"
des_key2 = "12345678"
msg = input("Message: ")
encrypted_msg = two_des_encrypt(des_key1, des_key2, message=msg)
print("Encrypted Message: ", encrypted_msg)
