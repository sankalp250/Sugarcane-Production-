from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(plain_text, key):
    
    if len(key) != 8:
        raise ValueError("DES key must be 8 bytes long")
    
    
    cipher = DES.new(key, DES.MODE_ECB)
    
    padded_text = pad(plain_text.encode(), 8)
    
    
    encrypted_text = cipher.encrypt(padded_text)
    
    return encrypted_text

def decrypt(encrypted_text, key):
    
    if len(key) != 8:
        raise ValueError("DES key must be 8 bytes long")
    
    
    cipher = DES.new(key, DES.MODE_ECB)
    
    decrypted_padded_text = cipher.decrypt(encrypted_text)
    
    
    decrypted_text = unpad(decrypted_padded_text, 8)
    
    return decrypted_text.decode()

if __name__ == "__main__":
    key = get_random_bytes(8)  
    plain_text = "Hello, DES!"
    
    print(f"Original Text: {plain_text}")
    
    encrypted_text = encrypt(plain_text, key)
    print(f"Encrypted Text: {encrypted_text.hex()}")
    
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")
    