# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# quick program demonstrating how to write into a txt file;


# name the file;
file_name = "moj_pierwszy_plik.txt"

f = open( file_name, 'wb' ) 		# open the file;
										# note : if the file does not exist it will be created automatically;

	
	# TODO:	add file to this repo path: file_name.txt


# to write into the txt file, use the .write function

f.write("Zapis informacji do pliku \n\n\n")		# "\n" indicates a new line



f.write("po kazdej wyprowadzonym stringu trzeba przejsc do nowej linii \n")		# editing the file
f.write("wypisujac znak specjalny \\n albo dodajac \\na koncu naszego stringu \n")

f.write("\n\n")

f.write("Czy rozumiesz juz jak dziala pisanie do pliku? \n")

"""
notes :
	
	writing into a txt file is much faster (~100 - 1000 times) than printing messages
	on the screen.
	
	doing this is called "logging" (pl: logowanie). this way, the information on the output
	is much clearer.
"""


f.close()			# close the file; this should always be the last line of code after writing into a file
						# if you write any code related to the file after this, it will not be recognised

print("\n\n")
print("Pisanie do pliku zakonczone")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
