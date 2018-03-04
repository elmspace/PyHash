"""
Import libraries.
All operators (AND, XOR and so on) are in Utility module
"""
from Utility import *;


def HashFunction(input_String, input_ConfigData):

	####################################################
	# Origianl string
	original_string = input_String;

	####################################################

	hash_multiple = input_ConfigData["hash_multiple"];
	chunck_size = input_ConfigData["chunck_size"];
	hash_char_size = input_ConfigData["hash_char_size"];

	#===========
	# These are right rotate and shift values when creating the W list
	aaa = input_ConfigData["aaa"];
	bbb = input_ConfigData["bbb"];
	ccc = input_ConfigData["ccc"];
	#----
	ddd = input_ConfigData["ddd"];
	eee = input_ConfigData["eee"];
	fff = input_ConfigData["fff"];
	#============
	# These are the right rotate values for the compression portion
	aa = input_ConfigData["aa"];
	bb = input_ConfigData["bb"];
	cc = input_ConfigData["cc"];
	#----
	dd = input_ConfigData["dd"];
	ee = input_ConfigData["ee"];
	ff = input_ConfigData["ff"];
	#===========

	####################################################
	############################### The Code Starts Here


	# Get the length of the original string
	length_of_original_string = len(original_string);

	# Convert the original string into binary
	binary_format_of_original_string = ''.join(format(ord(i),'b').zfill(8) for i in original_string);


	# Get the length of the binary string
	length_of_binary_format_of_original_string = len(binary_format_of_original_string);


	# Append 1 to the end of the string
	binary_format_of_original_string += "1";

	# Lets find K such that B+1+K+64 is multiple of hash_multiple
	for i in range(0,hash_multiple):
		if(float(length_of_binary_format_of_original_string + 1 + 64 + i)%float(hash_multiple) == 0):
			K = i;
			break;

	# Lets make a K length 0 string
	TempList = ["0" for i in range(0,int(K))];
	K = "".join(TempList);


	# Get the length of the original string and convert it into binary
	binary_format_of_length_of_string = '{0:08b}'.format(length_of_binary_format_of_original_string);


	# Lets make the Big-endian
	# First we fill a 64-bit portion 
	TempList = ["0" for i in range(0,64-len(binary_format_of_length_of_string))]
	# Now we make the Big-endian
	big_endian = "".join(TempList) + binary_format_of_length_of_string;


	# Now we put everythong together
	big_papa = binary_format_of_original_string + K + big_endian;


	# Let divide up BigPapa into chunk sizes, as defined above
	big_papa_in_chuncks = [big_papa[i:i+chunck_size] for i in range(0,len(big_papa),chunck_size)];

	# The Right Shift and Right Rorate are defined in Utility

	# Create the W list, the first 16 will be the same as the big_papa_in_chuncks
	W = big_papa_in_chuncks;


	# Lets create the remaining portion of the W list
	for i in range(16,64):
		# This makes the s0
		s0_1 = RightRotate(W[i-15], aaa);
		s0_2 = RightRotate(W[i-15], bbb);
		s0_3 = RightShift(W[i-15], ccc);
		s0 = XOR_Operator(XOR_Operator(s0_1,s0_2),s0_3);
		# This makes the s1
		s1_1 = RightRotate(W[i-2], ddd);
		s1_2 = RightRotate(W[i-2], eee);
		s1_3 = RightShift(W[i-2], fff);
		s1 = XOR_Operator(XOR_Operator(s1_1,s1_2),s1_3);
		# We append the new members to the W list
		W.append(ADD_Operator(ADD_Operator(ADD_Operator(W[i-16],s0),W[i-7]),s1));


	# We create the h list
	first_8_primes = PrimesGenerator(8);
	first_8_primes = [(float(i))**(1.0/2.0) for i in first_8_primes];
	first_8_primes = [i%1 for i in first_8_primes];
	first_8_primes = [i*2.0**(float(chunck_size)) for i in first_8_primes];
	first_8_primes = [int(i//1) for i in first_8_primes];
	first_8_primes = ["{:032b}".format(i) for i in first_8_primes];
	h = first_8_primes;



	# We create the k list
	first_64_primes = PrimesGenerator(64);
	first_64_primes = [(float(i))**(1.0/3.0) for i in first_64_primes];
	first_64_primes = [i%1 for i in first_64_primes];
	first_64_primes = [i*2.0**(float(chunck_size)) for i in first_64_primes];
	first_64_primes = [int(i//1) for i in first_64_primes];
	first_64_primes = ["{:032b}".format(i) for i in first_64_primes];
	k = first_64_primes;



	#================================= Compression Section

	# I will use h[value] and not use the initialize, its the same thing

	h_origianl = h[:];


	for i in range(0,64):
		s1_1 = RightRotate(h[4], aa);
		s1_2 = RightRotate(h[4], bb);
		s1_3 = RightRotate(h[4], cc);
		s1 = XOR_Operator(XOR_Operator(s1_1,s1_2),s1_3);

		ch_1 = AND_Operator(h[4],h[5]);
		ch_2 = AND_Operator(NOT_Operator(h[4]),h[6]);
		ch = XOR_Operator(ch_1,ch_2);

		temp1 = ADD_Operator(h[7],ADD_Operator(s1,ADD_Operator(ch,ADD_Operator(k[i],W[i]))));

		s0_1 = RightRotate(h[0],dd);
		s0_2 = RightRotate(h[0],ee);
		s0_3 = RightRotate(h[0],ff);
		s0 = XOR_Operator(XOR_Operator(s0_1,s0_2),s0_3);

		maj_1 = AND_Operator(h[0],h[1]);
		maj_2 = AND_Operator(h[0],h[2]);
		maj_3 = AND_Operator(h[1],h[2]);
		maj = XOR_Operator(XOR_Operator(maj_1,maj_2),maj_3);
		
		temp2 = ADD_Operator(s0,maj);

		h[7] = h[6];
		h[6] = h[5];
		h[5] = h[4];
		h[4] = ADD_Operator(h[3],temp1);
		h[3] = h[2];
		h[2] = h[1];
		h[1] = h[0];
		h[0] = ADD_Operator(temp1,temp2);



	# Adde the shuffeled h values to the original values
	h[0] = ADD_Operator(h_origianl[0],h[0]);
	h[1] = ADD_Operator(h_origianl[1],h[1]);
	h[2] = ADD_Operator(h_origianl[2],h[2]);
	h[3] = ADD_Operator(h_origianl[3],h[3]);
	h[4] = ADD_Operator(h_origianl[4],h[4]);
	h[5] = ADD_Operator(h_origianl[5],h[5]);
	h[6] = ADD_Operator(h_origianl[6],h[6]);
	h[7] = ADD_Operator(h_origianl[7],h[7]);


	# Put the hash values together to create the human readable hash
	FinalHex = ""
	for i in h:
		# If the size of the hash is not what we expect,
		# append 0s to the front of it
		HexConv = str(format(int(i,2),'x'));
		if(len(HexConv) < hash_char_size):
			DelSize = hash_char_size - len(HexConv);
			for ii in range(0,DelSize):
				HexConv  = "0"+HexConv;

		FinalHex += HexConv;


	# Here is the has value
	print FinalHex
