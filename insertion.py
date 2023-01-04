

def user_input():
    print("Entrez un ou plusieurs mots séparés par des espaces: ")
    user_list = input()
    user_list = user_list.split(" ")
    return user_list

def add_to_file(user_list):
    with open("insertion.txt", "a") as file:
        for word in user_list:
            file.write(word + "\n")


def main():
    # Get user input
    user_list = user_input()
    # Add user input to file
    add_to_file(user_list)


main()