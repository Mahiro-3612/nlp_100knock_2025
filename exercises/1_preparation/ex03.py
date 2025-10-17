import re

def create_letter_count_list(txt):
	formatted_txt = re.sub(r'[.,]', '', txt)
	formatted_txt_list = formatted_txt.split(" ")
	count_list = []
	for txt in formatted_txt_list:
		count_list.append(len(txt))
	return count_list

def main():
	txt = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	count_list = create_letter_count_list(txt)
	print(count_list)

if __name__ == "__main__":
	main()