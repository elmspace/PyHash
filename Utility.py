import random;
import math;

"""
	Expects a string, will do the following:
	Ex: 01011100 --> 10001011 for rotate value of 3
	input_String = Input String (ex: 1010101)
	input_R = Right rotate by this amount
"""
def RightRotate(input_String, input_R):
	right_rotated = input_String;

	for i in range(0,input_R):
		LastElement = right_rotated[len(right_rotated)-1];
		right_rotated = LastElement+right_rotated;
		right_rotated = right_rotated[:-1];

	return right_rotated;




"""
	Expects a string, will do the following:
	Ex: 01011100 --> 00001011 for shift value of 3
	input_String = Input String (ex: 1010101)
	input_S = Shift to right by this amount
"""
def RightShift(input_String, input_S):
	right_shifted = input_String;

	for i in range(0,input_S):
		append_this = "0";
		right_shifted = append_this+right_shifted;
		right_shifted = right_shifted[:-1];

	return right_shifted;



"""
	XOR Operator will perform XOR operation on two string.
	It will convert them into base 2 int and then perform XOR.
	It will return a string.
"""
def XOR_Operator(input_String1, input_String2):
	return '{0:0{1}b}'.format(int(input_String1,2) ^ int(input_String2,2),len(input_String1));




"""
	 ADD Operator will perform the Bitwise addition
	 It will take in two string and return a string
"""
def ADD_Operator(input_String1, input_String2):

	Result = bin(int(input_String1,2) + int(input_String2,2));
	Result = str(Result)[2:len(Result)];

	if(len(Result) > len(input_String1)):
		DiffLen = len(Result) - len(input_String1);
		for ii in range(0,DiffLen):
			Result = Result[1:len(Result)];

	if(len(Result) < len(input_String1)):
		DiffLen = len(input_String1) - len(Result);
		for ii in range(0,DiffLen):
			Result = "0"+Result;

	return Result





"""
 Performs and AND operations
"""
def AND_Operator(input_String1, input_String2):
	if(len(input_String1) < len(input_String2)):
		jj = len(input_String2) - len(input_String1)
		for ii in range(0,jj):
			input_String1 = "0"+input_String1;

	if(len(input_String2) < len(input_String1)):
		jj = len(input_String1) - len(input_String2)
		for ii in range(0,jj):
			input_String2 = "0"+input_String2;

	Result = [];
	for i in range(0,len(input_String1)):
		if(input_String1[i] == "0" or input_String2[i] == "0"):
			Result.append("0");
		else:
			Result.append("1");

	return "".join(Result);




"""
 Performs a NOT operation
"""
def NOT_Operator(input_String1):
	Result = [];
	for i in range(0,len(input_String1)):
		if(input_String1[i] == "1"):
			Result.append("0");
		else:
			Result.append("1");

	return "".join(Result);



"""
	This function will return a list of primes, with list of
	length = input_SizeOfList
"""
def PrimesGenerator(input_SizeOfList):

	ListOfPrimes = [];
	n = 0;
	while(len(ListOfPrimes)<input_SizeOfList):
		if n==2:
			ListOfPrimes = [2]

		s=range(3,n+1,2)
		mroot = n ** 0.5
		half=(n+1)/2-1
		i=0
		m=3
		while m <= mroot:
			if s[i]:
				j=(m*m-3)/2
				s[j]=0
				while j<half:
					s[j]=0
					j+=m
			i=i+1
			m=2*i+3

		ListOfPrimes = [2]+[x for x in s if x];
		n += 1;

	return ListOfPrimes






"""
	This function will take in as input a int, and will return a random alpha-numeric string of
	the inputted length;
"""
def AlphaNumRandom(input_LengthOfRandString):
	return ''.join(random.choice('0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz') for i in range(input_LengthOfRandString))





"""
	This function will calculate the chi^2 for a mtrix of size m by n.
	It takes as input, the Matrix and the expected value.
	It outputs the chi^2 value for that Matrix.
"""
def CalculateChiSq(input_Matrix, input_ExpValue):

	# First we get the dimessions of the matrix
	Rows = len(input_Matrix);
	Cols = len(input_Matrix[0]);
	chisq = 0.0;
	# Now we want to loop thorugh the matrix and calculate chi
	for row in range(0,Rows):
		for col in range(0,Cols):

			chisq += ((float(input_Matrix[row][col]) - float(input_ExpValue))**2/float(input_ExpValue));

	return chisq;




"""
	This function will caluclate the mean for a data set.
	The data set can be a matrix of dimention m by n (a list of lists)
	Or a list of dimension n
	input_Data -> the data itself
	input_DataType -> The type of the data, <matrix> <list>
"""
def CalculateMean(input_Data, input_DataType):
	MeanValue = None;
	if(input_DataType == "matrix"):
		Rows = len(input_Data);
		Cols = len(input_Data[0]);
		MeanValue = 0.0;
		TotalNumberOfElements = float(Rows) * float(Cols);
		for row in range(Rows):
			for col in range(Cols):
				MeanValue += input_Data[row][col];
		# Calculate the mean		
		MeanValue = float(MeanValue) / TotalNumberOfElements;
		return MeanValue;
	elif(input_DataType == "list"):
		MeanValue = 0.0;
		MeanValue = float(sum(input_Data))/float(len(input_Data));
	else:
		return MeanValue;



"""
	This function will calculate the standard deviation for a input data
	The input data can be a list, or a matrix, a list of lists.
	input_Data is the actual data.
	input_DataType is the type of the input_Data, either a list or matrix.
"""
def CalculateSTD(input_Data, input_DataType):
	STDValue = None;
	if(input_DataType == "matrix"):
		Rows = len(input_Data);
		Cols = len(input_Data[0]);
		STDValue = 0.0;
		TotalNumberOfElements = float(Rows) * float(Cols);
		MeanValue = CalculateMean(input_Data,"matrix");
		for row in range(Rows):
			for col in range(Cols):
				STDValue += float((input_Data[row][col] - MeanValue)**2);
		STDValue /= TotalNumberOfElements;
		STDValue = math.sqrt(STDValue);
		return STDValue;
	elif(input_DataType == "list"):
		MeanValue = CalculateMean(input_Data,"list");
		STDValue = 0.0;
		for i in range(len(input_Data)):
			STDValue += float((input_Data[i] - MeanValue)**2);
		STDValue /= float(len(input_Data));
		STDValue = math.sqrt(STDValue);
		return STDValue;
	else:
		return None;







# End
