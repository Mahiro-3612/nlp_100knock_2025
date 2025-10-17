import re
from collections import defaultdict

def create_letter_count_list(txt):
	formatted_txt = re.sub(r'[.,]', '', txt)
	formatted_txt_list = formatted_txt.split(" ")
	symbol_to_idx = defaultdict(int)
	for i, formatted_txt in enumerate(formatted_txt_list):
		if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
			symbol = formatted_txt[:1]
		else:
			symbol = formatted_txt[:2]
		symbol_to_idx[symbol] = i
	return(symbol_to_idx)

def main():
	txt = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	symbol_to_idx = create_letter_count_list(txt)
	print(symbol_to_idx)

if __name__ == "__main__":
	main()