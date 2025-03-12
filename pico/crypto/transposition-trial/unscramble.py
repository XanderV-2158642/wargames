import random
content = ""
with open("message.txt", "r") as txt:
    content = txt.read()

correctstring = ""

print("message contains: ", content)

seen_options = []

while len(content) > 0:
    # take first 3 of content
    # swap space for '_'
    printcontent = content[:3].replace(' ', '_')
    print(len(correctstring), ": ", correctstring.replace(' ', '_'), "+", printcontent)
    choice = input("scramble or correct? (s - c)")
    if choice == 'c':
        print("adding content")
        seen_options = []
        correctstring += content[:3]
        content = content[3:]
    elif choice == 's':
        # scramble the contents first three characters
        first3 = content[:3]
        seen_options.append(first3)
        shuffled_string = first3[-1] + first3[:2]
        while shuffled_string in seen_options:
            shuffled_string = ''.join(random.sample(first3, len(first3)))
        seen_options.append(shuffled_string)
        content = shuffled_string + content[3:]
    else:
        print("invalid choice")
