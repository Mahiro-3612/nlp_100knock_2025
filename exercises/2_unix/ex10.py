def count_lines(path):
	count = 0
	with open(path, "r") as f:
		lines = f.readlines()
		count = len(lines)
	return(count)

def main():
	print(count_lines("popular-names.txt"))

if __name__ == "__main__":
	main()

# wc -l ./popular-names.txt