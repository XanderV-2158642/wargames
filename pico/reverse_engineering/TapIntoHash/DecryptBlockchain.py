import hashlib
import ast

with open("enc_flag", "r") as flag_file:
    data = flag_file.read()


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

#take everything that is after "Encrypted Blockchain:"

encrypted_blockchain = data.split("Encrypted Blockchain: ")[-1].strip()
encrypted_blockchain = ast.literal_eval(encrypted_blockchain)

key = data.split("Encrypted Blockchain: ")[0].split('Key: ')[1].strip()
key = ast.literal_eval(key)

key_hash = hashlib.sha256(key).digest()

blocksize = 16

decrypted_plaintext = ""
for i in range(0, len(encrypted_blockchain), blocksize):
    block = encrypted_blockchain[i:i+blocksize]
    decrypted_block = xor_bytes(block, key_hash).decode()
    print(decrypted_block)
    decrypted_plaintext += decrypted_block

print(decrypted_plaintext)
