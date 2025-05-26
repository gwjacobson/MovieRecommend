from HashMap import HashMap

def choice_1_fun():
    choice =  input("what would you like to do?  ")

    if choice == "a":
        movieRec_fun()
    elif choice == "b":
        movieAdd_fun()
    else:
        print("Please ENTER either 'a' or 'b': ")
        choice_1_fun()

def movieRec_fun():
    pass

def movieAdd_fun():
    pass



print("Hello, Welcome to Graeme's Movie Recommendation Program!")

print("To get a movie recommendation, ENTER 'a'")
print("To add a new movie title to the software, ENTER 'b'")

choice_1_fun() #initial user selection to get recommendation or add title


'''
if choice_1 == 'a':

#this is where you can additional genres
#adding additional genres needs to be updated in MovieTitles, as well
    print("Available movie genres: ") #List out available movie genres and corresponding input value
    print("For Horror: 0")
    print("For Action: 1")
    print("For Drama: 2")
    print("For Comedy: 3")
    print("For Anime: 4")
    print("For Romance: 5")
    print("For Documentary: 6")
    print("For Family: 7")
    print("For Other: 8")

    genre_choice = input("Make selection of corresponding number for desired movie genre: ") #movie genre choice
    genre_choice_int = int(genre_choice)

    if genre_choice_int in range(0, 9):
        pass
    else:
        genre_choice = input("Please make a valid numerical selection: ")

elif choice_1 == 'b':
    pass
'''