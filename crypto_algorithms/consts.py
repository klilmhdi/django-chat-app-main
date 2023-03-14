import numpy as np
from egcd import egcd
import pyDes

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
des_key1 = "ABCDEFGH"
des_key2 = "12345678"
K = np.matrix([[3, 10, 20], [20, 19, 17], [23, 78, 17]])

# التحويل الى مصفوفة


def convert_to_matrix(data, rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(data[i * cols + j])
        matrix.append(row)
    return matrix

# التحويل من مصفوفة


def convert_from_matrix(matrix):
    # Initialize an empty result list
    result = []

    # Iterate through each row in the matrix
    for row in matrix:
        # Add each element in the row to the result list
        result.extend(row)

    # Return the result list
    return result

# التحويل من حرف لخانة


def letter_to_index(letter):
    # Create a dictionary that maps each letter to its index
    letter_to_index_dict = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25
    }

    # Convert the letter to uppercase, if necessary
    letter = letter.upper()

    # Return the index for the given letter
    return letter_to_index_dict.get(letter, 26)

# التحويل العكسي من الخانة لحرف


def index_to_letter(index):
    # Create a list of the letters of the alphabet
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Return the letter at the given index
    return alphabet[index]


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, s, t = egcd(b % a, a)
        return gcd, t - (b // a) * s, s

# عكس باقي قسمة المصفوفة


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
    )
    return matrix_modulus_inv


def hill_cipher_encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index(letter))

    split_P = [
        message_in_numbers[i: i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index(" "))[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter(number)

    return encrypted


def encrypt_1(request):
    return hill_cipher_encrypt(request, K)


def two_des_encrypt(message, des_key1="ABCDEFGH", des_key2="12345678"):
    k = pyDes.des(des_key1, pyDes.CBC, "\0\0\0\0\0\0\0\0",
                  pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_msg = k.encrypt(message)
    k = pyDes.des(des_key2, pyDes.CBC, "\0\0\0\0\0\0\0\0",
                  pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_msg = k.encrypt(encrypted_msg)
    return encrypted_msg


def encrypt_2(request):
    return two_des_encrypt(message=request)
