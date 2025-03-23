from textnode import TextNode, TextType

def main():
    text_test = TextNode("Testy testing", TextType.LINK, "https://www.boot.dev")
    print(text_test)

main()