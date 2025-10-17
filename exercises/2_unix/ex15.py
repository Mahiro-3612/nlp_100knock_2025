import math

def split_file(path, n):
	with open(path, "r") as f:
		lines = f.readlines()
		line_cnt = len(lines)
		line_cnt_per_file = math.ceil(line_cnt / n)
		i = 0
		while (i < n):
			with open(f"./output/file_{i}.txt", 'w', encoding='utf-8') as out:
				out.writelines(lines[line_cnt_per_file * i : min(line_cnt_per_file * (i + 1), line_cnt)])
			i += 1

def main():
	split_file("./popular-names.txt", 10)

if __name__ == "__main__":
	main()

# split -n l/10 popular-names.txt popular-names_split_