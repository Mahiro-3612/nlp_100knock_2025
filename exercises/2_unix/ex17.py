def count_unique_first_words(path):
	with open(path, "r") as f:
		lines = f.readlines()
		first_words = set()
		for line in lines:
			first_words.add(line.split("\t")[0])
	return (len(first_words))

def main():
	print(count_unique_first_words("./popular-names.txt"))

if __name__ == "__main__":
	main()

# cut -f 1 popular-names.txt | sort | uniq | wc -l
