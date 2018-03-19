import os;
import sys;

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../../', '')));

from HashFunction import HashFunction;
from Utility import *;
import pickle;
import time;

####################################################
input_String = "Test";
#===========

input_ConfigData = {};
input_ConfigData["hash_multiple"] = 128;
input_ConfigData["chunck_size"] = input_ConfigData["hash_multiple"]/16;
input_ConfigData["hash_char_size"] = input_ConfigData["chunck_size"]/4;
input_ConfigData["RoundConst"] = 64;

#===========
# These are right rotate and shift values when creating the W list
input_ConfigData["aaa"] = 0;
input_ConfigData["bbb"] = 0;
input_ConfigData["ccc"] = 0; # Shift
input_ConfigData["ddd"] = 0;
input_ConfigData["eee"] = 0;
input_ConfigData["fff"] = 0; # Shift
#============
# These are the right rotate values for the compression portion
input_ConfigData["aa"] = 0;
input_ConfigData["bb"] = 0;
input_ConfigData["cc"] = 0;
input_ConfigData["dd"] = 0;
input_ConfigData["ee"] = 0;
input_ConfigData["ff"] = 0;


################################################################################################ Algo Starts Here:

# These parameters will be the same for the whole test:
isAlreadyBinary = True;
outputFormat = "binary";
MatrixDataSavePath = ".\\Results_128\\";
##############################


for SampleSize in range(1, 1000, 5):
	DeltaTime = 0.0;
	# Define the sie of the matrix
	n = 160;
	m = 64;
	Matrix = [[0 for j in range(0,m)] for i in range(0,n)];
	for randStringNumber in range(0,SampleSize):
		StartTime = time.time();
		################################# Get the original hash/bino
		# First we take a random string:
		RandomString = AlphaNumRandom(20);
		
		# Then we convert the string into binary, this will be used to run the test. Flipping the binos.
		RandomStringBino = ''.join(format(ord(i),'b').zfill(8) for i in RandomString);

		# Set this to true, since we have already converted our string into binary
		HashOutput = HashFunction(RandomStringBino, input_ConfigData, isAlreadyBinary, outputFormat);

		# Save the original random binary and its hash value, we will use this for the XOR calculation
		Original_BinaryInput = RandomStringBino;
		Origianl_HashOfInput = HashOutput;

		# Create a list to hold the modified items
		List_Modified_Binary_Holder = [];
		List_Modified_Hash_Holder = [];

		# Now we will look thorugh each ith element of the original input
		for i in range(0,len(Original_BinaryInput)):
			# Create  a modified version of the input
			ModifiedInput = list(Original_BinaryInput);
			# Flip the ith element of the binary
			if(ModifiedInput[i] == "0"):
				ModifiedInput[i] = "1";
			else:
				ModifiedInput[i] = "0";
			# Convert it back to string
			ModifiedInput = "".join(i for i in ModifiedInput);
			# Get the has of the modified input, in binary format
			HashOfModifiedBinary = HashFunction(ModifiedInput, input_ConfigData, isAlreadyBinary, outputFormat);
			# Append the results to the list
			List_Modified_Binary_Holder.append(ModifiedInput);
			List_Modified_Hash_Holder.append(HashOfModifiedBinary);


		# Now we can calculate the XOR of the modified hash values and the original hash:
		# Lets loop through the modified hash values:
		XOR_List = [];
		for ModifiedHashValue in List_Modified_Hash_Holder:
			XOR_List.append(XOR_Operator(ModifiedHashValue,Origianl_HashOfInput));

		for i in range(0,len(XOR_List)):
			for j in range(0,len(XOR_List[i])):
				if(XOR_List[i][j] == "1"):
					Matrix[i][j] += 1;

	EndTime = time.time();
	DeltaTime += float(abs(StartTime - EndTime))/60.0;
	print "Run time: ["+str(DeltaTime)+"] Number of random string: ["+str(randStringNumber)+"]";

	pickle.dump(Matrix, open(MatrixDataSavePath+"Matrix_"+str(SampleSize)+"_"+str(int(DeltaTime))+".p","wb"));






# End
