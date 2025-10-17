import random

def shuffle_file(path):
	with open(path, "r") as f:
		lines = f.readlines()
		random.shuffle(lines)
		for line in lines:
			print(line, end="")

def main():
	shuffle_file("./popular-names.txt")

if __name__ == "__main__":
	main()

# sort -R ./popular-names.txt