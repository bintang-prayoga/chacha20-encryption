import json

from base64 import b64decode
from Crypto.Cipher import ChaCha20

def save_to_file(data, filename='decrypted.json'):
    with open('results/' + filename, 'w', encoding='utf-8') as f:
        if isinstance(data, (dict, list)):
            json.dump(data, f, ensure_ascii=False, indent=2)
        else:
            f.write(data)

def main():
    try:
        with open('results/encrypted.json') as f:
            b64 = json.load(f)
        nonce = b64decode(b64['nonce'])
        ciphertext = b64decode(b64['ciphertext'])
        key = b64decode(b64['public_key'])

        cipher = ChaCha20.new(key=key, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)
        text = plaintext.decode('utf-8')

        parsed = None
        try:
            parsed = json.loads(text)
            unwrap_count = 0
            while isinstance(parsed, str) and unwrap_count < 5:
                try:
                    parsed = json.loads(parsed)
                    unwrap_count += 1
                except Exception:
                    break
        except json.JSONDecodeError:
            parsed = text

        if isinstance(parsed, (dict, list)):
            print(json.dumps(parsed, ensure_ascii=False))
            save_to_file(parsed)
        else:
            try:
                out = {"data": parsed}
                print(json.dumps(out, ensure_ascii=False))
                save_to_file(out)
            except Exception:
                
                print(text)
                save_to_file(text)
    except (ValueError, KeyError) as e:
        print("Incorrect decryption")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()