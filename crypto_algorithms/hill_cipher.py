# from numpy import *
# from consts import *
# import numpy as np
#
#
# def hill_cipher_encrypt(message, K):
#     encrypted = ""
#     message_in_numbers = []
#
#     for letter in message:
#         message_in_numbers.append(letter_to_index(letter))
#
#     split_P = [
#         message_in_numbers[i: i + int(K.shape[0])]
#         for i in range(0, len(message_in_numbers), int(K.shape[0]))
#     ]
#     for P in split_P:
#         P = np.transpose(np.asarray(P))[:, np.newaxis]
#
#         while P.shape[0] != K.shape[0]:
#             P = np.append(P, letter_to_index(" "))[:, np.newaxis]
#
#         numbers = np.dot(K, P) % len(alphabet)
#         n = numbers.shape[0]
#         for idx in range(n):
#             number = int(numbers[idx, 0])
#             encrypted += index_to_letter(number)
#
#     return encrypted
#
#
# def hill_cipher_decrypt(text, K):
#     # Convert the text to a numpy array
#     text_array = np.array([ord(c) for c in text])
#
#     # Reshape the array into a matrix with n rows (where n is the length of the key)
#     n = len(K)
#     text_matrix = text_array.reshape((n, -1))
#
#     # Convert the key to a numpy array
#     key_array = np.array([ord(c) for c in key])
#
#     # Reshape the key array into a key matrix
#     key_matrix = key_array.reshape((n, n))
#
#     # Invert the key matrix
#     key_matrix = np.linalg.inv(key_matrix)
#
#     # Multiply the key matrix by the text matrix
#     result_matrix = np.dot(text_matrix, key_matrix)
#
#     # Mod 26 the result
#     result_matrix = result_matrix % 26
#
#     # Convert the result matrix back to a flat array
#     result_array = result_matrix.flatten()
#
#     # Convert the result array back to a list of characters
#     result_text = [chr(c) for c in result_array]
#
#     # Return the result as a string
#     return ''.join(result_text)
#
#
# message = input("enter a plaintext to encrypt: ")
# K = np.matrix([[3, 3], [2, 5]])
# decrypted_message = hill_cipher_decrypt(message, K)
# print("Original message: " + message)
# print("Decrypted message: " + decrypted_message)
#
# message = input("enter a plain text to encrypt: ")
# Kinv = matrix_mod_inv(K, len(alphabet))
# encrypted_message = hill_cipher_encrypt(message, K)
# print("Original message: ", message)
# print("Encrypted message: ", encrypted_message)



import numpy as np
from egcd import egcd  # pip install egcd

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def matrix_mod_inv(matrix, modulus):
    """We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
    """

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv


def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted


# def decrypt(cipher, Kinv):
#     decrypted = ""
#     cipher_in_numbers = []
#
#     for letter in cipher:
#         cipher_in_numbers.append(letter_to_index[letter])
#
#     split_C = [
#         cipher_in_numbers[i : i + int(Kinv.shape[0])]
#         for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
#     ]
#
#     for C in split_C:
#         C = np.transpose(np.asarray(C))[:, np.newaxis]
#         numbers = np.dot(Kinv, C) % len(alphabet)
#         n = numbers.shape[0]
#
#         for idx in range(n):
#             number = int(numbers[idx, 0])
#             decrypted += index_to_letter[number]
#
#     return decrypted


def main():
    message = input("Message: ")
    K = np.matrix([[3,10,20],[20,19,17], [23,78,17]]) # for length of alphabet = 27
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    # decrypted_message = decrypt(encrypted_message, Kinv)

    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    # print("Decrypted message: " + decrypted_message)


main()