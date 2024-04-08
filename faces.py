def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

input_text = input("")
output_text = convert(input_text)
print(output_text)