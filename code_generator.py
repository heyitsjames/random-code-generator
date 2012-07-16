#!/usr/bin/python
import math, sys, random, csv
from optparse import OptionParser

""" Simple script that prints a number of alphanumeric codes, with options for uniqueness, number of codes, and strength"""
""" Feel free to add, subtract, enhance, detract, or shamelessly rip off this script """
""" James Rasmussen, 2012 """

def main():
	rand_string = ""
	available_chars_ext = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|')
	available_chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
	chars = None
	output_file = open('codes.csv', 'w+')
	
	usage = "usage: %prog [options] codeLength numberOfCodes"
	parser = OptionParser(usage)
	parser.add_option("-s", "--strong", dest="strong",
	                  action="store_true", help="adds special characters and capitalized letters to the mix", default=False)
	parser.add_option("-u", "--unique", dest="unique", action="store_true", default=False, help="forces each code to be unique (will take longer with a large volume)")
	parser.add_option("-f", "--filename", dest="file",
	                  metavar="FILE", help="write output to FILE (default is codes.csv in same directory as script)")
	parser.add_option("-d", "--delimiter", dest="delimiter",
	                  metavar="DELIMITER", help="specify what you would like the delimiter to be (default is a return carriage)")
	
	(options, args) = parser.parse_args()
	
	if len(args) != 2:
		if len(args) == 0:
			parser.print_usage()
			sys.exit()
		else:
			parser.error("incorrect number of arguments")
	if options.strong:
		chars = available_chars_ext
	else:
		chars = available_chars
	if options.file:
		output_file = open(options.file, 'w+')
	
		
	rand_string_list = []
	code_length = int(args[0])
	num_codes_generated = int(args[1])
	
	def generate(code_length, num_codes_generated):
		if options.unique and int(args[1]) > 10000:
			print "You have chosen to generate a high volume of unique codes. Please be patient as they generate..."
		code_iterator = 0
		while (code_iterator < num_codes_generated):
			rand_string = ""
			for c in range(0,code_length):
				rand_char = chars[random.randint(0,len(chars)-1)]
				rand_string += rand_char
			if options.unique:
				if rand_string not in rand_string_list:
					code_iterator += 1
					rand_string_list.append(rand_string)
			else:
				code_iterator += 1
				rand_string_list.append(rand_string)
			
	generate(code_length, num_codes_generated)
	with output_file as f:
		if options.delimiter:
			d = options.delimiter
		else:
			d = '\n'
		writer = csv.writer(f,delimiter=d)
		writer.writerow(rand_string_list)

if __name__ == "__main__":
    main()