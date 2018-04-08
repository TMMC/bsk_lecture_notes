from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os

__AUTHOR__ = "Paweł Bogdan"

def position(alphabet, letter):
    for i in range(len(alphabet)):
        if alphabet[i] == letter:
            return i
    return -1

def cesar_encrypt(alphabet, plaintext, k):
    result = ''
    for letter in plaintext.lower():
        index = position(alphabet, letter)
        if index == -1:
            result += letter
        else:
            index = (index + k) % len(alphabet)
            result += alphabet[index]
    return result.upper()
        
    
def break_cesar(alphabet, ciphertext, dictionary):
    for k in range(len(alphabet)):
        plain = cesar_encrypt(alphabet, ciphertext, k)
        words = plain.split(' ')
        found = True
        for word in words:
            if word.strip(',.').lower() not in dictionary:
                found = False
                break
        if found:
            return plain
    return None
        

def break_hash(h, dictionary):
    for word1 in dictionary:
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(bytes(word1, 'utf-8'))
        dig = digest.finalize().hex()
        if dig == h:
            return word1
        for word2 in dictionary:
            digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
            digest.update(bytes(word1+word2, 'utf-8'))
            dig = digest.finalize().hex()
            if dig == h:
                return word1+word2
   
def aes_encrypt(key, iv, src_file, dest_file):
    backend = default_backend()
    algorithm = algorithms.AES(bytes.fromhex(key))
    mode = modes.CBC(bytes.fromhex(iv))
    cipher = Cipher(algorithm, mode, backend)
    encryptor = cipher.encryptor()
    dictionary = open(src_file, 'rb').read()
    out = open(dest_file, 'wb')
    out.write(encryptor.update(dictionary) + encryptor.finalize())
    out.flush()
    out.close()
    
def aes_encryption_command(key, iv, src_file, dest_file):
    return 'openssl aes-256-cbc -e -K {0} -iv {1} -in {2} -out {3} -nopad'.format(key, iv, src_file, dest_file)

def aes_decrypt(key, src_file, dest_file):
    command = "openssl aes-256-ecb -d -K {0} -in {1} -out {2}".format(key, src_file, dest_file)
    os.system(command)

def read_rsa_key(path):
    key_file = open(path, 'rb')
    private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    result = {'d': private_key.private_numbers().d,
          'p': private_key.private_numbers().p,
          'q': private_key.private_numbers().q,
          'n': private_key.public_key().public_numbers().n,
          'e': private_key.public_key().public_numbers().e
         }
    return result

def sign_file(path_to_file, path_to_key, path_to_signature):
    key_file = open(path_to_key, 'rb')
    private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    file = open(path_to_file, 'rb')
    content = file.read()
    signature = private_key.sign(content, padding.PKCS1v15(), hashes.SHA256())
    result_file = open(path_to_signature, 'wb')
    result_file.write(signature)
    result_file.flush()
    result_file.close()

def sign_file_command(path_to_file, path_to_key, path_to_signature):
    command = 'openssl dgst -sign {0} -keyform PEM -sha256 {1} > {2}'.format(path_to_key, path_to_file, path_to_signature)
    return command