from HashFunction import HashFunction;


####################################################
input_String = "Test";
#===========

input_ConfigData = {};
input_ConfigData["hash_multiple"] = 500;
input_ConfigData["chunck_size"] = input_ConfigData["hash_multiple"]/16;
input_ConfigData["hash_char_size"] = input_ConfigData["chunck_size"]/4;

#===========
# These are right rotate and shift values when creating the W list
input_ConfigData["aaa"] = 7;
input_ConfigData["bbb"] = 18;
input_ConfigData["ccc"] = 3;
input_ConfigData["ddd"] = 17;
input_ConfigData["eee"] = 19;
input_ConfigData["fff"] = 10;
#============
# These are the right rotate values for the compression portion
input_ConfigData["aa"] = 6;
input_ConfigData["bb"] = 11;
input_ConfigData["cc"] = 25;
input_ConfigData["dd"] = 2;
input_ConfigData["ee"] = 13;
input_ConfigData["ff"] = 22;


HashFunction(input_String, input_ConfigData);