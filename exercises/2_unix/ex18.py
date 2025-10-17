from collections import defaultdict

def get_first_word_cnts(path):
	with open(path, "r") as f:
		lines = f.readlines()
		first_word_to_cnt = defaultdict(int)
		for line in lines:
			first_word_to_cnt[line.split("\t")[0]] += 1
	return (first_word_to_cnt)

def main():
	print(get_first_word_cnts("./popular-names.txt"))

if __name__ == "__main__":
	main()

# cut -f 1 popular-names.txt | sort | uniq -c | sort -nr