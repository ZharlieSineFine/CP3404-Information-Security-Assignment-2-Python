def decrypt_vigenere(ciphertext, keyword):
    # Define the alphabet for reference
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword_length = len(keyword)
    decrypted_text = []

    # Convert each character in the ciphertext to the corresponding decrypted character
    for i, char in enumerate(ciphertext):
        if char.isalpha():  # Check if the character is a letter
            # Find the positions in the alphabet
            cipher_pos = alphabet.index(char.lower())
            key_pos = alphabet.index(keyword[i % keyword_length].lower())
            # Calculate the decrypted character position
            decrypted_pos = (cipher_pos - key_pos) % 26
            decrypted_char = alphabet[decrypted_pos]
            decrypted_text.append(decrypted_char)
        else:
            # Directly append non-alphabet characters
            decrypted_text.append(char)

    # Join all characters to form the decrypted text
    return ''.join(decrypted_text)


# Define the ciphertext and the keyword
ciphertext = """
pchhlptizjhfatcrifnkhctoqvgxbusvwggszbjchmwvghnvetdsqnrkxtslmdbsuczhtt
iysunjtcldlhcwjkqkitktmsumgtjthlipmwvghfnxgxfdxwtacmoiyxgjvlmjxgftiytn
ckwoudnnvfdwexekgdoemxfbvihmwzgwsrxpiszcfxapivyfbcdouegmhnwwbrxgzgkude
ttcpgqwxkwhmunryovmgtufcgxwmryoxwvbdegkuxxiysquvngrzslqitihbihvdeqhunb
cxhkynhhzbjvkwhrzouwvizcqmfbhtivmgwhftdljtkvphyplxeuoykgiysvypltkvdnva
tislmqgapcqyuxacsucptrfbwcpndlggiwuavoxwvbdeqguvatisdlgfpemeoaxgjoqxux
acsumyadtcqnkgjfivfamgrrhuubcxzhwqfbfrlnauxugdlgfpkqkyftcuqoycktucyytm
xdsdwehguwqavhiysdoemxfbuonxhtrdmcktkmscetacmrjggqzrwbgutjhnhqpcvldgre
tftdwftxjovyengzhlyufpiyhnunryovnjxcvkbitdhkcfegqryoqaggnjswbgkteczyzb
hkbxggkdlgrhnbcvpuimxgjwwyuljtvdmehbdghwvapkcizgkhvfycexhwcunttszbjcpl
ttiucvbtjadlmxijcqfkgtsfregkhvlkcdbikvhmcftwzdquthdcuyehcmsqnkhcrzrhnb
cvoxwvbdegdhfhuwsuhqydiarzrkdksfnkhckcecfwtigfixxgruhihlttiucvrxjgxyuy
diqguubhcwpcvxsnoqacgscsxhiigfdrmgwpjqkyoxufffipwjthlhilttiuycgsrbrhaf
dlgfxclwfkhpgkiywvmeatdslmkghvqxlgtcurryugdkogxtxhjhkyuxrlflnkxhdouegm
pjdhwvhutrdmyxlzzoxklrlgvnjbhzbvyemxfb
""".replace('\n', '').replace(' ', '')  # Remove newlines and spaces for clean processing
keyword = 'product'

# Decrypt the ciphertext
decrypted_text = decrypt_vigenere(ciphertext, keyword)
print(decrypted_text)
