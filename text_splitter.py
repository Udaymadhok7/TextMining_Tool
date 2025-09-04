from sentiment_analysis import score_paragraph


if __name__ == "__main__":
    f = open("randomparas.txt")
    huge_text = f.read()

    chunks = huge_text.split("\n") # splitting the huge text to paragraphs
    for i,chunk in enumerate(chunks):
        print(f"Para{i} , Score is {score_paragraph(chunk)}")

    f.close() # clearing memory leaks