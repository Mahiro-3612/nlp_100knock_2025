import random

def typoglycemia(txt):
	word_list = txt.split(' ')
	typo_list = []
	for word in word_list:
		if len(word) > 5:
			# random.shuffleは値を返さない
			inner_chrs = list(word[1:-1])
			random.shuffle(inner_chrs)
			typo_word = word[0] + "".join(inner_chrs) + word[-1]
			typo_list.append(typo_word)
		else:
			typo_list.append(word)
	return " ".join(typo_list)

def main():
	print(typoglycemia("I cluon’dt believe that I cuold aucllaty udsrntnaed what I was rndaieg : the poeannemhl pwoer of the hmaun mind ."))

if __name__ == "__main__":
	main()