import pandas as pd;
import pickle;
import matplotlib.pyplot as plt
from matplotlib import style;
style.use('ggplot')


File1 = ".\\Study1\\Analysis.p";
File2 = ".\\Study2\\Analysis.p";
File3 = ".\\Study3\\Analysis.p";
File4 = ".\\Study4\\Analysis.p";

Data1 = pickle.load(open(File1,"rb"));
Data2 = pickle.load(open(File2,"rb"));
Data3 = pickle.load(open(File3,"rb"));
Data4 = pickle.load(open(File4,"rb"));

ColumnNames = Data1.columns.values;
Study1ColNames = [i+"_1" for i in ColumnNames];
Study2ColNames = [i+"_2" for i in ColumnNames];
Study3ColNames = [i+"_3" for i in ColumnNames];
Study4ColNames = [i+"_4" for i in ColumnNames];

Data1.columns = Study1ColNames;
Data2.columns = Study2ColNames;
Data3.columns = Study3ColNames;
Data4.columns = Study4ColNames;

Master = Data1.merge(Data2, left_on="numb_input_1", right_on="numb_input_2", how="outer");
Master = Master.merge(Data3, left_on="numb_input_1", right_on="numb_input_3", how="outer");
Master = Master.merge(Data4, left_on="numb_input_1", right_on="numb_input_4", how="outer");

Master.to_csv("Avalanche.csv");




##########################################################################################################
##########################################################################################################
##########################################################################################################
# This section will plot the normalized delta mean as a function of the sample size.
##########################################################################################################
# Master["Study_1"] = abs(Master["mean_1"] - Master["exp_val_1"])/Master["exp_val_1"];
# Master["Study_2"] = abs(Master["mean_2"] - Master["exp_val_2"])/Master["exp_val_2"];
# Master["Study_3"] = abs(Master["mean_3"] - Master["exp_val_3"])/Master["exp_val_3"];
# Master["Study_4"] = abs(Master["mean_4"] - Master["exp_val_4"])/Master["exp_val_4"];
# # Plot Study 1 and 2
# FactorPlot = Master[["Study_1","Study_2"]].plot(x=Master["numb_input_1"],style=['bo-','ro-']);
# FactorPlot.set_xlabel("Sample Size");
# FactorPlot.set_ylabel("abs(Mean - Exp)/Exp");
# plt.show();
# # Plot Study 3 and 4
# FactorPlot = Master[["Study_3","Study_4"]].plot(x=Master["numb_input_1"],style=['go-','mo-']);
# FactorPlot.set_xlabel("Sample Size");
# FactorPlot.set_ylabel("abs(Mean - Exp)/Exp");
# plt.show();
##########################################################################################################
##########################################################################################################
##########################################################################################################
# This part plots the Coefficient of Variation for all 4 studies.
##########################################################################################################
# CoVPlot = Master.plot(x=Master["numb_input_1"], y=["CoefficientOfVariation_1","CoefficientOfVariation_2","CoefficientOfVariation_3","CoefficientOfVariation_4"], style=['bs-','rs-','gs-','ms-']);
# CoVPlot.set_xlabel("Sample Size");
# CoVPlot.set_ylabel("Coefficient of Variation");
# CoVPlot.legend(["Study_1", "Study_2", "Study_3", "Study_4"]);
# plt.show();
##########################################################################################################
##########################################################################################################
##########################################################################################################
# This section plots the Chi Squared as a function of sample size.
##########################################################################################################
# ChiSqPlot = Master.plot(x=Master["numb_input_1"], y=["chisq_1","chisq_2"],style=['bs-','rs-']);
# ChiSqPlot.set_xlabel("Sample Size");
# ChiSqPlot.set_ylabel("Chi-Squared");
# ChiSqPlot.legend(["Study_1", "Study_2"]);
# plt.show();
# ###
# ChiSqPlot = Master.plot(x=Master["numb_input_1"], y=["chisq_3","chisq_4"],style=['gs-','ms-']);
# ChiSqPlot.set_xlabel("Sample Size");
# ChiSqPlot.set_ylabel("Chi-Squared");
# ChiSqPlot.legend(["Study_3", "Study_4"]);
# plt.show();
##########################################################################################################
##########################################################################################################
##########################################################################################################