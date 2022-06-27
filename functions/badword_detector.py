with open('functions/files/dictionary.txt', encoding='utf8') as file:
    badword_dict = file.readlines()
    file.close()

for i in range(len(badword_dict)):
    badword_dict[i] = badword_dict[i].replace('\n', '')

print(badword_dict)

def badword_detector_function(string):
    string = string.lower()
    for badword in badword_dict:
        if badword in string:
            result = 1
            break
        else:
            result = 0
    
    if result == 1:
        return True
    else:
        return False
