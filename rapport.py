def read_file():
    with open("insertion.txt", "r") as file:
        content = file.read()
        content = content.split("\n")
        return content

# fonction permettant de compter le nombre d'occurence d'un mot dans une liste
def count_occurence(word, list):
    count = 0
    for element in list:
        if element == word:
            count += 1
    return count

def main():
    # read file
    content = read_file()
    # count occurence
    for word in content:
        print(f"{word}, {count_occurence(word, content)} fois")
        
main()