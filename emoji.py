import emoji


def emo():
    text = input("Input:")
    output = emoji.emojize(text, language="alias")
    print("Output:", output)


emo()
