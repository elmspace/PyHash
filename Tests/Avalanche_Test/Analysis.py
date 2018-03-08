"""
	In this module, we will do the analysis of the data we have collected from the avalanche test.
"""

# Import libraries
import pickle;
import os;
import sys;
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../', '')));
from Utility import *;



# Lets read the data from a pickle file
Matrix = pickle.load(open("Matrix_8192.p","rb"));

for i in Matrix:
	print max(i), min(i);

raw_input("...")


print CalculateSTD(Matrix, "matrix");
print CalculateMean(Matrix, "matrix");
raw_input("...")

# Now that we have the data, we can calculate the chi^2
# The data is in a Matrix format, list of list.


ExpectedValue = 8192/2;
print CalculateChiSq(Matrix, ExpectedValue);
