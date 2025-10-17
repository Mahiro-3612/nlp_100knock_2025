import re

def get_letter_grams(txt, letter_len):
	formatted_txt = re.sub(r'[,.]', '', txt)
	combined_txt = formatted_txt.replace(' ', '')
	combined_txt_len = len(combined_txt)
	letter_gram = []
	i = 0
	while (i + letter_len - 1 < combined_txt_len):
		letter_gram.append(combined_txt[i:i + letter_len])
		i += 1
	return letter_gram

def get_word_grams(txt, words_len):
	formatted_txt = re.sub(r'[,.]', '', txt)
	word_list = formatted_txt.split(' ')
	word_cnt = len(word_list)
	word_gram = []
	i = 0
	while (i + words_len - 1 < word_cnt):
		word_gram.append(tuple(word_list[i:i + words_len]))
		i += 1
	return word_gram

def main():
	txt = "I am an NLPer"
	letter_gram = get_letter_grams(txt, 3)
	word_gram = get_word_grams(txt, 2)
	print(f"letter_gram: {letter_gram}")
	print(f"word_gram: ", word_gram)

if __name__ == "__main__":
	main()

