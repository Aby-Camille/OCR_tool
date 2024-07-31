import easyocr
reader = easyocr.Reader(['fr', 'en', 'es'])
result = reader.readtext('CNI-test.jpg')

for (text, prob) in result:
    print(f'Text: {text}, Probability: {prob}')