"""
	In this module, we will do the analysis of the data we have collected from the avalanche test.
"""

# Import libraries
import pickle;
import os;
import sys;
from os import listdir;
from os.path import isfile, join;
import pandas as pd;
import matplotlib.pyplot as plt
from matplotlib import style;
style.use('ggplot')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../', '')));
from Utility import *;


SavePickleIn = ".\\Study4\\";
BaseResultsPath = ".\\Study4\\Results\\";

ResultsFiles = [f for f in listdir(BaseResultsPath) if isfile(join(BaseResultsPath, f))];


NumberOfRandomStringsList = [];
ExpectValueList = [];
ChiSqlList = [];
MeanList = [];
STDList = [];
DegOfFreedomList = [];
CoefficientOfVariation = [];

for results in ResultsFiles:
	# Lets read the data from a pickle file
	Matrix = pickle.load(open(BaseResultsPath+results,"rb"));

	NumberOfRandomStrings = int(str(results).split("_")[1]);
	ExpectedValue = float(NumberOfRandomStrings)/2.0;

	NumberOfRandomStringsList.append(NumberOfRandomStrings);
	ExpectValueList.append(ExpectedValue);
	ChiSqlList.append(CalculateChiSq(Matrix, ExpectedValue));
	MeanList.append(CalculateMean(Matrix, "matrix"));
	STDList.append(CalculateSTD(Matrix, "matrix"));
	DegOfFreedomList.append((len(Matrix) * len(Matrix[0])) - 1);
	CoefficientOfVariation.append(float(CalculateSTD(Matrix, "matrix"))/float(CalculateMean(Matrix, "matrix")));





ListOfColumns = ["chisq","mean","std","exp_val","numb_input", "DegOfFreedom", "CoefficientOfVariation"];
TotalData = pd.DataFrame(columns=ListOfColumns);


TotalData["chisq"] = ChiSqlList;
TotalData["mean"] = MeanList;
TotalData["std"] = STDList;
TotalData["exp_val"] = ExpectValueList;
TotalData["numb_input"] = NumberOfRandomStringsList;
TotalData["DegOfFreedom"] = DegOfFreedomList;
TotalData["factor"] = (TotalData["std"]);
TotalData["CoefficientOfVariation"] = CoefficientOfVariation;

TotalData.sort_values(by=["numb_input"], inplace=True);
TotalData.index = TotalData["numb_input"];


pickle.dump(TotalData,open(SavePickleIn+"Analysis.p","wb"));



