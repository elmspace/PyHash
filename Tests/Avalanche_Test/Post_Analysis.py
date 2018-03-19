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


# Master[["CoefficientOfVariation_1","CoefficientOfVariation_2","CoefficientOfVariation_3","CoefficientOfVariation_4"]].plot(style=['bs-','rs-','gs-','ms-']);
# plt.show()


##########################################################################################################
##########################################################################################################
##########################################################################################################
Master["Study_1"] = abs(Master["mean_1"] - Master["exp_val_1"])/Master["exp_val_1"];
Master["Study_2"] = abs(Master["mean_2"] - Master["exp_val_2"])/Master["exp_val_2"];
Master["Study_3"] = abs(Master["mean_3"] - Master["exp_val_3"])/Master["exp_val_3"];
Master["Study_4"] = abs(Master["mean_4"] - Master["exp_val_4"])/Master["exp_val_4"];

FactorPlot = Master[["Study_1","Study_2"]].plot(x=Master["numb_input_1"],style=['bo-','ro-']);
FactorPlot.set_xlabel("Sample Size");
FactorPlot.set_ylabel("abs(Mean - Exp)/Exp");
plt.show();

FactorPlot = Master[["Study_3","Study_4"]].plot(x=Master["numb_input_1"],style=['go-','mo-']);
FactorPlot.set_xlabel("Sample Size");
FactorPlot.set_ylabel("abs(Mean - Exp)/Exp");
plt.show();

##########################################################################################################
##########################################################################################################
##########################################################################################################

# Master[["chisq_1","chisq_2","chisq_3","chisq_4"]].plot(style=['bs-','rs-','gs-','ms-']);
# plt.show()