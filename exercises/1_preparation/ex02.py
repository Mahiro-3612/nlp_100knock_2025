def get_reversed(txt):
	# reversed_txt = txt[::-1]と書いてもいい
	reversed_txt = ""
	for letter in reversed(txt):
		reversed_txt += letter
	return (reversed_txt)

def main():
	txt = "stressed"
	reversed_txt = get_reversed(txt)
	print(reversed_txt)

if __name__ == "__main__":
	main()
