encryption_dict = {}
decryption_dict = {}
key = 0


def decrypt_values(encryp_dict):
	"""This function return a decrypted dictionary based on the passed argument

	Parameter:
		- encryp_dict: a key-value pair containing encrypted values

	This function uses chr() built-in function that takes a valid 
	ASCII based integer and returns an equivalent ASCII character 
	as a part of decrypted value, and then store it in a dict called
	"decryption_dict".
	"""
	dec = '' # this will be use to convert derypted values into a string
	for k, v in enumerate(encryp_dict.values()):
		for i in range(len(v)):
			# combined separated derypted values to form the original word
			dec += chr(v[i])
		# assign the "dec" content as a value in the decryption_dict
		decryption_dict[k] = dec
		dec = '' # reset to an empty string

	return decryption_dict


word = input('\n Enter a word: ')

while word.lower() != 'q':
	# uses ord() built-in function to encrypt the letters of a word
	# then store it in a list called "encrypted_values" through list comprehension
	encrypted_values = [ord(i) for i in word]


	# store the "encrypted_values" as a value in a dict called "encryption_dict"
	encryption_dict[key] = encrypted_values

	# increase the dictionary key by 1 when a successful loop occurs
	key += 1

	# prompt the user if they wanted more inputs otherwise terminate the loop
	user_opt = input('\n Another one [y/n]? ').lower()

	if user_opt == 'y':
		word = input('\n Enter a word: ')

	else:
		break

print('\nEncryption Dict\n\n', encryption_dict)

answer = input('\n Do you want to decrypt your inputs [y/n]? ').lower()

if answer == 'y':
	# pass the encrypted word(s) to decrypt_values function
	print('\nDecryption Dict\n\n', decrypt_values(encryption_dict))
else:
	pass
