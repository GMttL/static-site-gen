from textnode import *


def main():
	node = TextNode("This is some anchor text", TextType.LINK, "https://google.com")
	print(node)


if __name__ == "__main__":
	main()
