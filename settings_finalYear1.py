# ScriptName: settings.py
# Author: Rebecca Bronczyk
# Student Number: 121722211
# settings for your tests
'''
Coding problem: Independent samples 

Create a function that will take a dependendent variable and two independent variable groups and the data of both groups regarding the DV
The function will check wether the normal distribution (Skewness and curtosis) and equal variances are assumed (Levenes test)
If the assumptions are met a helper function is called, that will run an independent samples t-test on the data
If not, a Mann-Whitney test is run (using a helper function)
The function returns the APA style report sentence

Assumptions:
IVs and DV are no integers/floats/booleans -> int in list/tuple is okay and will give output with int in list; else it returns "Invalid variable type.")
The data have to be integers in lists (Else it returns "Invalid input type for the data.")
If a variable is missing it returns: "A variable is missing. Check your input."
'''
# ===================================================
# functions to call (names of params)
test_func = [#"print_function", # print_function example 
             #"print_function2", # print_function 2 example
             # "", # your function name
            "two_independent_groups_checker" # print result of independent-samples t-test or mann-whitney test
            ]

# ===================================================
# input parameter(s) and values to pass to the functions
param_name = [
              # print_function example
              #["input_string"], 
              # print_function 2 example
              # ["input_string", "added_string"], 
              # your function parameter name(s) - list of String list(s) - with one name per parameter
              ["DV", "IV1", "IV2", "data1", "data2"]
             ]
#list of lists, values taht are passed to params
input_vals = [
              # print_function example with one param
              #[["I'm in another file"], ["Really, in another file"], [7], [True], ["Oops"], ["this won't work"], # [], [], [], [] 
              #],
              # print_function 2 example, with 2 params
              #[ ["I'm in another file", ":)"], ["Really, in another file"], [7, ":)"], [True, ":)"], ["Oops", ":)"], ["this won't work", ":o)"], # [], [], [], [] 
              #],
              # your function parameter inout values - list of String list(s) - with one value per parameter
              [# E1
              ["loneliness", "smoker", "non-smoker", [1,2,3,4,5],[1,2,3,4,5]], 
               # E2
              ["loneliness", "smoker", "non-smoker", ((1,2,3,4,5)),[1,2,3,4,5]], 
              #E3
              ["loneliness", "smoker", "non-smoker", [1,1,1,1,2],[5,5,5,5,4]], 
              #E4
              ["loneliness", "smoker", "non-smoker", [],[]], 
              #E5
              ["loneliness", "smoker", "non-smoker", [],[1]], 
              #E6
              ["loneliness", "smoker", "non-smoker", [1,1,2,2,2,2,2,2,2,3,3],[3,3,4,4,4,4,4,4,4,5,5]], 
              # E7
              ["loneliness", "smoker", "non-smoker", [1,1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5]], 
              # E8
              [("loneliness"), ("smoker"), ("smoker"), [1,1,2,2,2,2,2,2,2,3,3],[3,3,4,4,4,4,4,4,4,5,5]], 
               # E9
              [["loneliness"], ("smoker"), ("smoker"), [1,1,2,2,2,2,2,2,2,3,3],[3,3,4,4,4,4,4,4,4,5,5]], 
               #E10
              [["loneliness"], ["smoker"], ["non-smoker"], [1,1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5]],
                #E11 
              [True, ["smoker"], ["non-smoker"], [1,1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5]], 
                #E12
              ["loneliness", ["smoker"], ["non-smoker"], ["Hi"],[2,2,2,3,3,3,3,5,5,5]],
                #E13 
              ["loneliness", ["smoker"], ["non-smoker"], [1,1.1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5]], 
                #E14
              ["loneliness", ["smoker"], ["non-smoker"], [True],[2,2,2,3,3,3,3,5,5,5]], 
                #E15
              ["loneliness", ["smoker"], ["non-smoker"], [1,2],[2,3]], 
                #E16
              ["loneliness", [55], ["non-smoker"], [1,2,3,4],[2,3,4,5]], 
              #   #E17
              ["loneliness", 55, ["non-smoker"], [1,2,3,4],[2,3,4,5]], 
                # E18
              ["loneliness", "smoker", ["non-smoker"], ["hi",2,3,4],[2,3,4,5]],
              # E19 
              ["loneliness", "smoker", ["non-smoker"], (3,2,3,4),[2,3,4,5]],
              # E20
              ["loneliness", "smoker", ["non-smoker"], "hello",[2,3,4,5]],
              # E21
              ["loneliness", "smoker", ["non-smoker"], True,[2,3,4,5]],
              # E22
              [{"loneliness": 1}, "smoker", ["non-smoker"], [2,3,4,5],[2,3,4,5]],
              # E23
              ["loneliness", "smoker", ["non-smoker"], {2:1,3:3,4:4,5:9},[2,3,4,5]],
              # E24
              ["smoker", ["non-smoker"], [2,3,4,5],[2,3,4,5]]
            ]]

# ===================================================
# output values I must test against for this function
outputlist = [
              # print_function example
              #[ "I'm in another file :)", "Really, in another file :)", "Oops", "Oops", "Oops :)", "this won't work", #
              #],
              # print_function 2 example
              #[ "I'm in another file :)", "Really, in another file", "Oops", "Oops", "Oops :)", "this won't work ;)", #
              #],
              # your function return values to be tested against
              [#E1
               "In this sample of 10 participants, those in group smoker had equal scores in loneliness (Median =3.00, IQR = 3.00) to those in group non-smoker (Median = 3.00, IQR = 3.00), the difference was statistically significant, U =12.50, z = 0.00, p < .05, r =0.16.", 
               #E2
               "Failed to check the assumptions of the t-test. Check your input.", 
               #E3
               "In this sample of 10 participants, those in group smoker had lower scores in loneliness (Median =1.00, IQR = 3.00) than those in group non-smoker (Median = 5.00, IQR = 3.00), the difference was statistically significant, U =0.00, z = -2.61, p < .05, r =-0.51.",
               #E4
               "Failed to check the assumptions of the t-test. Check your input.", 
               #E5
               "Failed to check the assumptions of the t-test. Check your input.", 
               #E6
               "In this sample of 22 participants, those in group smoker had lower scores in loneliness (Median =2.00, IQR = 6.00) than those in group non-smoker (Median = 4.00, IQR = 6.00), the difference was statistically significant, U =2.00, z = -3.84, p < .05, r =-0.61.", 
               #E7
               "An independent samples t-test indicated no statistically significant differences in loneliness between participants in group smoker (M = 2.80, SD = 1.14) and those in group non-smoker (M =2.80, SD =1.36), t(20)=0.00, p > .05 , Cohen’s d =0.00.", 
               #E8
               "In this sample of 22 participants, those in group smoker had lower scores in loneliness (Median =2.00, IQR = 6.00) than those in group smoker (Median = 4.00, IQR = 6.00), the difference was statistically significant, U =2.00, z = -3.84, p < .05, r =-0.61.", 
               # E9
               "In this sample of 22 participants, those in group smoker had lower scores in ['loneliness'] (Median =2.00, IQR = 6.00) than those in group smoker (Median = 4.00, IQR = 6.00), the difference was statistically significant, U =2.00, z = -3.84, p < .05, r =-0.61.", 
               #E10
               "An independent samples t-test indicated no statistically significant differences in ['loneliness'] between participants in group ['smoker'] (M = 2.80, SD = 1.14) and those in group ['non-smoker'] (M =2.80, SD =1.36), t(20)=0.00, p > .05 , Cohen’s d =0.00.", 
               #E11
               "Invalid variable type.",
               #E12
               "Invalid data type.", 
               #E13
               "Invalid data type.", 
               #E14
               "Invalid data type.", 
               #E15
               "Sample size too small for Mann-Whitney test.", 
               #E16
               "In this sample of 8 participants, those in group [55] had lower scores in loneliness (Median =2.50, IQR = 2.50) than those in group ['non-smoker'] (Median = 3.50, IQR = 2.50), the difference was statistically significant, U =4.50, z = -1.01, p < .05, r =-0.00.", 
              #  #E17
              "Invalid variable type.", 
              #  #E18
              "Invalid data type.",
              #  # E19
              "Invalid input type for the data.",
              #  #E20
              "Invalid input type for the data.",
              #  # E21
              "Invalid input type for the data.",
              #  # E22
              "In this sample of 8 participants, those in group smoker had equal scores in {'loneliness': 1} (Median =3.50, IQR = 2.50) to those in group ['non-smoker'] (Median = 3.50, IQR = 2.50), the difference was statistically significant, U =8.00, z = 0.00, p < .05, r =0.18.",
              #  #E23
              "Invalid input type for the data.",
              #E24
              "A variable is missing. Check your input."]
            ]