try:
    filename = input("Enter filename: ")
    infile = open(filename, "r")
    line = infile.readline()
    value = int(line)
except IOError :
   print("Error: file not found.")
  
except ValueError as exception :
   print("Error:", str(exception))

filename = input("Enter filename: ")
outfile = open(filename, "w")
content_ = "This is a test\n"
try:
    outfile.write(content_)
except Exception as e:
   print("Error: {exception}")
finally:
    outfile.close()

# https://movies.stackexchange.com/questions/128615/sci-fi-movie-with-fleshy-game-consoles-that-plug-into-the-spinepython