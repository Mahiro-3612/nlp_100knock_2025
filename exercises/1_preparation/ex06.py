from ex05 import get_letter_grams

def get_union(txt1, txt2):
	union = []
	bigrams_1 = get_letter_grams(txt1, 2)
	bigrams_2 = get_letter_grams(txt2, 2)
	for bigram_1, bigram_2 in zip(bigrams_1, bigrams_2):
		if bigram_1 not in union:
			union.append(bigram_1)
		if bigram_2 not in union:
			union.append(bigram_2)
	return union

def get_intersection(txt1, txt2):
	intersection = []
	bigrams_1 = get_letter_grams(txt1, 2)
	bigrams_2 = get_letter_grams(txt2, 2)
	for bigram_1 in bigrams_1:
		if bigram_1 in bigrams_2:
			intersection.append(bigram_1)
	return intersection

def get_difference(txt1, txt2):
	difference = []
	bigrams_1 = get_letter_grams(txt1, 2)
	bigrams_2 = get_letter_grams(txt2, 2)
	for bigram_1 in bigrams_1:
		if bigram_1  not in bigrams_2:
			difference.append(bigram_1)
	return difference

def main():
	txt1 = "paraparaparadise"
	txt2 = "paragraph"
	union = get_union(txt1, txt2)
	intersection = get_intersection(txt1, txt2)
	difference = get_difference(txt1, txt2)
	print("union is: ", union)
	print("intersection is: ", intersection)
	print("difference is: ", difference)
	if "se" in union:
		if "se" in difference:
			print("\"se\" is in txt1")
		else:
			print("\"se\" is in txt2")
	else:
		print("\"se\" not in both texts")

if __name__ == "__main__":
	main()


# set(list)みたいにしたら、和、積、差が | 、 - 、 & で表せる