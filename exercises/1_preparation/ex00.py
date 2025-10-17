def get_combined_text(s1, s2):
	combined = ""
	for a, b in zip(s1, s2):
		combined += a
		combined += b
	return combined

def main():
	txt1 = "パトカー"
	txt2 = "タクシー"
	temp = get_combined_text(txt1, txt2)
	print(temp)

if __name__ == "__main__":
	main()