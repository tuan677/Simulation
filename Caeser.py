def encrypt(text,s):
  result = ""
 # transverse the plain text
  for i in range(len(text)):
    char = text[i]
    # Encrypt uppercase characters in plain text
    if (char.isupper()):
      result += chr((ord(char) + s - 65) % 26 + 65)
    # Encrypt lowercase characters in plain text
    elif (char.islower()):
      result += chr((ord(char) + s - 97) % 26 + 97)
    # Don't encrypt characters in plain text
    else:
      result += chr(ord(char))
  return result

#check the above function
text = "                    "
s = 3
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher Text : " + encrypt(text,s))

def decrypt(text,s):
  result = ""
 # transverse the cipher text
  for i in range(len(text)):
    char = text[i]
    # Decrypt uppercase characters in cipher text
    if (char.isupper()):
      result += chr((ord(char) - s - 65) % 26 + 65)
    # Decrypt lowercase characters in cipher text
    elif (char.islower()):
      result += chr((ord(char) - s - 97) % 26 + 97)
    # Don't encrypt characters in plain text
    else:
      result += chr(ord(char))
  return result

#check the above function
text = "                    "
s = 3
print("Cipher Text : " + text)
print("Shift pattern : " + str(s))
print("Plain Text :" + decrypt(text,s))
