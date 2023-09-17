import pickle
import sys
'''
Program reads content from the game.dat file and creates a new file copying only 
those records from the game.dat where the game is "Basket Ball".
'''

# function collects information from user.
def set_data():
    with open(r"C:\Users\Pascal\Desktop\ALX\Practices\7-file_handling\game.dat", "ab") as outputFile:
        game_name = (input("Enter Game Name: "))
        participant = input("Enter name of Participant: ")

        #create a list
        game_information = [game_name, participant]

        #serialize the object and writing to file
        pickle.dump(game_information, outputFile)


# function that writes new record into the new file basket.dat
def writeNewRecord(game_name):

    #opens file in Binary mode
    with open(r"C:\Users\Pascal\Desktop\ALX\Practices\7-file_handling\game.dat", "rb") as inputFile:
        with open(r"C:\Users\Pascal\Desktop\ALX\Practices\7-file_handling\game.dat", "wb") as newFile:

            # reads to the end of file
            try:
                while True:
                    #reading the object from file
                    data = pickle.load(inputFile)

                    if data[0] == game_name:
                        pickle.dump(data, newFile)

            except EOFError:
                pass

            finally:

                display(newFile)

def display(newFile):
    with open(r"C:\Users\Pascal\Desktop\ALX\Practices\7-file_handling\game.dat", "rb") as newFile:
        new_data = pickle.load(newFile)
        print("Game Name:", new_data[0])
        print("Participant:", new_data[1])


def main():
    while True:
        set_data()
        newRecord = input("Do you want to enter a new record? y/n: ")
        if newRecord in 'Nn':
            break

    game_name = input("Enter Game Name: ")

    game_info = writeNewRecord(game_name)


if __name__ == '__main__':
    main()