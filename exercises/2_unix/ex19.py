def sort_by_third_word(path):
	with open(path, "r") as f:
		lines = f.readlines()
		sorted_lines = sorted(
                lines,
                key=lambda line: int(line.split("\t")[2]),
                reverse=True
            )
	return (sorted_lines)

def main():
	sorted_lines = sort_by_third_word("./popular-names.txt")
	for line in sorted_lines:
		print(line, end='')

if __name__ == "__main__":
	main()

# cut -f 1 popular-names.txt | sort | uniq | wc -l