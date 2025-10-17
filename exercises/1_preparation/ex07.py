def insert_letters(x, y, z):
	return str(x) + "時の" + str(y) + "は" + str(z)

def main():
	inserted = insert_letters(12, "気温", 22.4)
	print(inserted)

if __name__ == "__main__":
	main()