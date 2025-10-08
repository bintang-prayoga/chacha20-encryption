import json

from base64 import b64encode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

def save_to_file(data, filename='encrypted.json'):
    with open('results/' + filename,
                'w') as f:
            f.write(data)

def main():
    key = get_random_bytes(32)
    cipher = ChaCha20.new(key=key)

    ciphertext = cipher.encrypt(json.dumps(open('example.json').read()).encode('utf-8'))

    print ("The key is " + key.hex())

    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ciphertext).decode('utf-8')
    public_key = b64encode(key).decode('utf-8')

    result = json.dumps({'nonce':nonce, 'ciphertext':ct, 'public_key':public_key})
    print(result)

    save_to_file(result)

if __name__ == "__main__":
    main()