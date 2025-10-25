# wap to ask user to enter names of their 3 fav movies and store them as a list
name = input("Enter you name: ")
print("Hello",name,"!")
movies = []

mov1 = input("Enter the first movie name: ")
movies.append(mov1)

mov2 = input("Enter the second movie name: ")
movies.append(mov2)

mov3 = input("Enter the third movie name:")
movies.append(mov3)

print(movies)

# direct way --

film = []
film.append(input("Enter first movie: "))
film.append(input("Enter second movie: "))
film.append(input("Enter third movie: "))

print(film)