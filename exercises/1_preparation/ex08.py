def cipher(txt):
	encrypted= ""
	for letter in txt:
		if letter >= 'a' and letter <= 'z':
			# ordで文字コード取得、chrで文字コード解読
			enc_letter = chr(219 - ord(letter))
		else:
			enc_letter = letter
		encrypted += enc_letter
	return (encrypted)

def main():
	encode = cipher("the quick brown fox jumps over the lazy dog")
	print("暗号化:",encode)
	decode = cipher(encode)
	print("復号化:",decode)

if __name__ == "__main__":
	main()