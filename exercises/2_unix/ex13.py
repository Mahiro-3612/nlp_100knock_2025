def show_head_no_tab(path, n):
	with open(path, "r") as f:
		lines = f.readlines()
		head_n_lines = lines[:n]
		for line in head_n_lines:
			print(line.replace("\t", ' '), end="")


def main():
	show_head_no_tab("./popular-names.txt", 10)

if __name__ == "__main__":
	main()

# head ./popular-names.txt | sed 's/\t/ /g'