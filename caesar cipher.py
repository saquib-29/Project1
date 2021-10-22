from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

is_decision=True

while is_decision==True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  if direction=='encode':
    text=input("Type your message:\n")
    shift=int(input("Type the shift number:\n"))
    def encrypt(plain_text, shift_amount):
      cipher_text = ""
      for letter in plain_text:
        if letter in alphabet:
          position = alphabet.index(letter)
          new_position = position + shift_amount
          cipher_text += alphabet[new_position]
        else:
          cipher_text+=letter
      print("The {} text is: {}\n".format(direction,cipher_text))
    encrypt(text,shift)

  elif direction=='decode':
    text=input("Type your message:\n")
    shift=int(input("Type the shift number:\n"))
    def decrypt(plain_text, shift_amount):
      cipher_text = ""
      for letter in plain_text:
        if letter in alphabet:
          position = alphabet.index(letter)
          new_position = position - shift_amount
          cipher_text += alphabet[new_position]
        else:
          cipher_text+=letter
      print("The {} text is: {}\n".format(direction,cipher_text))
    decrypt(text,shift)

  else:
    print("Wrong input")

  print("Do you want to go again?Yes or No")
  decision=input().lower()
  if decision=="no":
    is_decision=False


