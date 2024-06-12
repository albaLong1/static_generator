from textnode import TextNode

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image
)

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_image = "image"

def main():
    dummy_value1 = TextNode("This is a [text] node,",text_type_text)
    new_nodes = split_nodes_delimiter([dummy_value1],"'", text_type_italic)
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    new_list = extract_markdown_images(text)
    for item in new_list:
        print(item)
    text1 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text1))
    node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        text_type_text,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)

    


if __name__ == "__main__":
    main()