def show_head_first_word(path, n):
	with open(path, "r") as f:
		lines = f.readlines()
		head_n_lines = lines[:n]
		for line in head_n_lines:
			print(line.split("\t")[0])


def main():
	show_head_first_word("./popular-names.txt", 10)

if __name__ == "__main__":
	main()

# head ./popular-names.txt | cut -f 1 -d $'\t'