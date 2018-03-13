import os;
import sys;

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../', '')));

from HashFunction import HashFunction;
from Utility import *;
import pickle;
import time;

####################################################
input_String = "Test";
#===========

input_ConfigData = {};
input_ConfigData["hash_multiple"] = 512;
input_ConfigData["chunck_size"] = input_ConfigData["hash_multiple"]/16;
input_ConfigData["hash_char_size"] = input_ConfigData["chunck_size"]/4;
input_ConfigData["RoundConst"] = 16;

#===========
# These are right rotate and shift values when creating the W list
input_ConfigData["aaa"] = 0;#7;
input_ConfigData["bbb"] = 0;#18;
input_ConfigData["ccc"] = 32;#3; # Shift
input_ConfigData["ddd"] = 0;#17;
input_ConfigData["eee"] = 0;#19;
input_ConfigData["fff"] = 32;#10; # Shift
#============
# These are the right rotate values for the compression portion
input_ConfigData["aa"] = 0;#6;
input_ConfigData["bb"] = 0;#11;
input_ConfigData["cc"] = 0;#25;
input_ConfigData["dd"] = 0;#2;
input_ConfigData["ee"] = 0;#13;
input_ConfigData["ff"] = 0;#22;


################################################################################################ Algo Starts Here:

# These parameters will be the same for the whole test:
isAlreadyBinary = True;
outputFormat = "hash";
MatrixDataSavePath = ".\\Results_512\\";
##############################

# 1- Create a random string
# 2- Check to see if it is in a list of random string from before
# 3- Add it to a list of random string
# 4- Calculate the hash of the string
# 5- Check if it already exists in the list of hash values
# 	5-a if yes, note the number of random string tried and exit
#	5-b if not, continue this process 



LengthOfRandomStringInLetters = 10**4;
NumberOfRandomStringSample = 10**5;

ListOfRandomStrings = [];
ListOfHashValues = [];

# 62 is the set of letters and numbers we are choosing from
MaxNumbOfPossibleRandomStirngs = 62**LengthOfRandomStringInLetters;
if (MaxNumbOfPossibleRandomStirngs>NumberOfRandomStringSample):
	print "Your smaple size will not cover all the possible combination of string."

for trys in range(NumberOfRandomStringSample):

	# Create a random string of length x
	RandomString = AlphaNumRandom(LengthOfRandomStringInLetters);

	# Check if the string already exist in the list:
	if((RandomString in ListOfRandomStrings) == False):
		# Add the stirng to the list
		ListOfRandomStrings.append(RandomString);

		# Then we convert the string into binary, this will be used to run the test. Flipping the binos.
		RandomStringBino = ''.join(format(ord(i),'b').zfill(8) for i in RandomString);

		# Set this to true, since we have already converted our string into binary
		HashOutput = HashFunction(RandomStringBino, input_ConfigData, isAlreadyBinary, outputFormat);

		# See if we have already produced this hash
		if(HashOutput in ListOfHashValues):
			print "Found collision.";
			print "Sample: "+str(trys);
			break;
		else:
			ListOfHashValues.append(HashOutput);

print len(ListOfRandomStrings);