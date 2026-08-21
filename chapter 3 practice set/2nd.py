#Write a program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Ali").replace("<|Date|>","12/12/2023"))
print(letter.replace("You are selected!","You are not selected!"))