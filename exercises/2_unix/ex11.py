def show_head(path, n):
	with open(path, "r") as f:
		lines = f.readlines()
		head_n_lines = lines[:n]
		for line in head_n_lines:
			print(line, end="")

def main():
	show_head("./popular-names.txt", 10)

if __name__ == "__main__":
	main()

# head ./popular-names.txt