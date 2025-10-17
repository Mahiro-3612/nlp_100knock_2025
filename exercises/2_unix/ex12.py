def show_tail(path, n):
	with open(path, "r") as f:
		lines = f.readlines()
		tail_lines = lines[-n:]
		for line in tail_lines:
			print(line, end="")

def main():
	show_tail("./popular-names.txt", 10)

if __name__ == "__main__":
	main()

# tail ./popular-names.txt