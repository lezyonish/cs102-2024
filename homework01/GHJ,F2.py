def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for S in ciphertext:
        if "A" <= S <= "Z":
            new_S = chr((ord(S) - ord("A") - shift) % 26 + ord("A"))
            plaintext += new_S
        elif "a" <= S <= "z":
            new_S = chr((ord(S) - ord("a") - shift) % 26 + ord("a"))
            plaintext += new_S
        else:
            plaintext += S
    return plaintext
if __name__ == "__main__":
    print(decrypt_caesar(input()))