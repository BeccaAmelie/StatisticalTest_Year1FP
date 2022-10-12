# ScriptName: my_functions.py
# Author: Rebecca Bronczyk
# Student Number: 121722211

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

def ttestdfchanger(df1:int, df2:int) -> tuple[int,int]:
    '''
    purpose:
    Function to adjust the degrees of freedom to rows and colums in the F-table

    procedure:
    checks both degrees of freedom seperately and adjusts their value so it matches the rows and columns of the F-table
    
    return: 
    returns a tuple or error message if it failed

    Assumptions:
    both degrees of freedom are integers 
    '''
    # try to run the code
    try:
        # for the first group

        # if the degrees of freedom of group 1 = 11
        if df1 == 11:
            # adjusted degrees of freedom for group 1 are 10
            df1 = 10
        # if the degrees of freedom of group 1 between 12 and 14 
        elif df1 >=12 and df1 <15:
            # adjusted degrees of freedom for group 1 are 12
            df1 = 12
        # degrees of freedom for group 1 are 12
        elif df1 >=15 and df1 <20:
            # adjusted degrees of freedom for group 1 are 15
            df1=15
        elif df1 >=20 and df1 <24:
            # adjusted degrees of freedom for group 1 are 20
            df1=20
        elif df1 >=24 and df1 <30:
            # adjusted degrees of freedom for group 1 are 24
            df1=24
        elif df1 >=30 and df1 <60:
            # adjusted degrees of freedom for group 1 are 30
            df1=30
        elif df1 >=60 and df1 <120:
            # adjusted degrees of freedom for group 1 are 60
            df1=60
        elif df1 >=120 and df1 <300:
            # adjusted degrees of freedom for group 1 are 120
            df1= 120
        elif df1 >=300:
            # adjusted degrees of freedom for group 1 are 300
            df1= 300
        # not necessary but for completeness: if df for group 1 less than 12
        else:
            # df for group 1 stay the same
            df1 = df1
        

        # for the second group

        # if the degrees of freedom of group 2 = 11
        if df2 == 11:
            # adjusted degrees of freedom for group 2 are 10
            df2 = 10
        # if the degrees of freedom of group 2 are between 12 and 14
        elif df2 >=12 and df2 <15:
            # adjusted degrees of freedom for group 2 are 12
            df2 = 12
        # if the degrees of freedom of group 2 are between 15 and 19
        elif df2 >=15 and df2<20:
            # adjusted degrees of freedom for group 2 are 15
            df2=15
        # if the degrees of freedom of group 2 are between 20 and 23
        elif df2 >=20 and df2 <24:
            # adjusted degrees of freedom for group 2 are 20
            df2=20
        # if the degrees of freedom of group 2 are between 24 and 29
        elif df2 >=24 and df2 <30:
            # adjusted degrees of freedom for group 2 are 24
            df2=24
        # if the degrees of freedom of group 2 are between 30 and 59
        elif df2 >=30 and df2 <60:
            # adjusted degrees of freedom for group 2 are 30
            df2=30
        # if the degrees of freedom of group 2 are between 60 and 119
        elif df2 >=60 and df2 <120:
            # adjusted degrees of freedom for group 2 are 60
            df2=60
        # if the degrees of freedom of group 2 are between 120 and 299
        elif df2 >=120 and df2 <300:
            # adjusted degrees of freedom for group 2 are 120
            df2= 120
        # if the degrees of freedom of group 2 are equal/greater than 300
        elif df2 >=300:
            # adjusted degrees of freedom for group 2 are 300
            df2= 300
        # not necessary but for completeness: if df for group 2 less than 12
        else:
            # df for group 2 stay the same
            df2 = df2
        # return the adjusted degrees of freedom for both groups
        return df1, df2
    # if something goes wrong
    except: 
        # return the message that the degrees of freedom for the Levene's test are not computable
       return "Failed to compute degrees of freedom for Mann-Whitney test. Check your input."

# biggie, smallie = ttestdfchanger(299,10) # 120, 10
# biggie, smallie = ttestdfchanger(2100,0) # 120 0
# print(biggie, smallie)

def ttest(IV:str, DV1:str, DV2:str, n1:int, n2:int, variance1:float, variance2:float, mean1:float, mean2:float)->str:
    '''
    purpose:
    function to conduct an independent samples t-test
    
    calculations:
    calculates standard deviations, pooled variance, and t
    compares t to t-critical value from ttable -> checks for statistical significance (checks at p = .05 level)
    calculates effect size

    return: 
    returns APA style reporting sentence (or error message)
    '''
    # import math for instant magic
    import math
    # ttable
    ttable = { 0: "error",
        1:12.71, 2:4.303, 3: 3.182, 4:2.776, 5:2.571, 6:2.447, 7:2.365, 8:2.306, 9:2.262, 
        10:2.228, 11:2.201, 12:2.179, 13:2.160, 14:2.145, 15: 2.131, 16:2.120, 17:2.110, 18:2.101 ,19:2.093, 
        20:2.086, 21:2.080, 22:2.074, 23:2.069, 24:2.064, 25: 2.060, 26: 2.056, 27:2.052, 28:2.048, 29:2.045, 
        30:2.042, 40:2.021 , 60: 2.000, 80: 1.990, 100: 1.984, 1000: 1.962
    }
    try:
        # create string out of mean of first group and format it (2 characters after decimal)
        meanstr1 = "{:.2f}".format(mean1)
        # create string out of mean of second group and format it (2 characters after decimal)
        meanstr2=  "{:.2f}".format(mean2)
        # calculate population size (N)
        N = n1+n2
        # calculate degrees of freedom
        df = n1 + n2 -2
        '''calculate t'''
        # calculate raw mean difference & pooled variance
        # calculate standard deviation from variance of first group 
        sd1 = math.sqrt(variance1)
        # create string out of sd1 (format: 2 characters after decimal)
        sd1str = "{:.2f}".format(sd1)
        # calculate standard deviation from variance of second group 
        sd2 = math.sqrt(variance2)
        # create string out of sd2 (format: 2 characters after decimal)
        sd2str = "{:.2f}".format(sd2)
        # calculate pooled variance 
        pv = math.sqrt(((sd1/n1)**2)+((sd2/n2)**2))
        # calculate t
        t = ((mean1 - mean2) / (pv))
        # create t as string formatted to 2 characters after decimal
        tstr = "{:.2f}".format(t)
        
        '''calculate effect size (Cohens d)'''
        # calculate SDp
        SDp = math.sqrt((((n1 -1)*sd1**2) + ((n2 -1)*sd2**2)) / (n1 + n2 -2))
        
        # with SDp: calculate Codhens D
        cohen = "{:.2f}".format(((mean1 - mean2) / (SDp)))

        '''look up t critical'''
        # get to t critical
        # if sample size smaller/equal to 30
        if N <= 30:
            # the row in the ttable matches the degrees of freedom 
            tcritical = ttable[df]
        # if sample size between 31 and 39
        elif N < 40 and N >30:
            # look at df 30
            tcritical = ttable[30]
        # if sample size between 40 and 59
        elif N < 60 and N >39:
            # look at df 40
            tcritical = ttable[40]
        # if sample size between 60 and 79
        elif N < 80 and N >59:
            # look at df 60
            tcritical = ttable[60]
        # if sample size between 80 and 99
        elif N < 100 and N > 79:
            # look at df 80
            tcritical = ttable[80]
        # if sample size between 100 and 999
        elif N < 1000 and N >99:
            # look at df 100
            tcritical = ttable[100]
        # if 1000+ people in sample
        else:
            # look at df 1000
            tcritical = ttable[1000] 

        '''create returnstring'''
        # if significant 
        if t> tcritical:
            # returnstring is APA formatted report sentence for ttest: reporting statistical significance
            returnstring= str("An independent samples t-test indicated statistically significant differences in" + str(IV) + " between participants in group " +str(DV1) + " (M = " + meanstr1 + ", SD = " + str(sd1str) + ") and those in group " + str(DV2) + " (M =" + meanstr2 + ", SD =" + sd2str + "), t(" + N + ")=" + tstr + ", p < .05 , Cohen’s d =" + cohen+ ".")
        # if insignificant
        else:
            # returnstring is APA formatted report sentence for ttest: reporting NO statistical significance
            returnstring = str("An independent samples t-test indicated no statistically significant differences in " + str(IV) + " between participants in group " + str(DV1) + " (M = " + meanstr1 + ", SD = " + str(sd1str) + ") and those in group " + str(DV2) + " (M =" + meanstr2 + ", SD =" + sd2str + "), t(" + str(N) + ")=" + tstr + ", p > .05 , Cohen’s d =" + cohen+ ".")
        # return the returnstring to two_independent_groups_checker
        return returnstring
    except: 
        return "Failed to compute t-test. Check your input."

def mannwhitney(DV:str, IV1:str, IV2:str, data1:list, data2: list, n1: int, n2: int)->str:
    '''
    purpose:
    Function to run a Mann-Whitney test

    calculations:
    ranks data and calculates mean of ranks for both groups
    calculates U and z score & checks for statistical significance using the tables (mann whitney or standard normal table) (checks at p = .05 level) 
    calculates effect size

    return: 
    returns APA style reporting sentence (or error message)
    '''
    # import math for instant magic
    import math
    # mann withney table
    mannwhitneytable = {
        3: [ "error",0, 0, 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8], 
        4: ["error",0, 1,2,3,4,4,5,6,7,8,9,10,11,11,12,13,14], 
        5: [0,1,2,3,5,6,7,8,9,11,12,13,14,15,17,18,19,20], 
        6:[1,2,3,5,6,8,10,11,13,14,16,17,19,21,22,24,25, 27], 
        7: [1,3,5,6,8,10,12,14,16,18,20,22, 24,26,28,30,32,34],
        8: [2,4,6,8,10,13,15,17,19,22,24,26,29,31,34,36,38,41],
        9:[2,4,7,10,12,15,17,20,23,26,28,31, 34, 37, 39, 42, 45, 48],
        10:[3,5,8,11,14,17,20,23,26,29,33,36,39,42,45,48,52,55],
        11:[3,6,9,13,16,19,23,26,30,33,37,40,44,47,51,55,58,62],
        12:[4,7,11,14,18,22,26,29,33,37,41,45,49,53,57,61,65,69],
        13:[4,8,12,16,20,24,28,33,37,41,45,50,54,59,63,67,72,76],
        14:[5,9,13,17,22,26,31,36,40,45,50,55,59,64,67,74,78,83],
        15:[5, 10, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 70, 75, 80, 85,90],
        16:[6,11, 15, 21, 26, 31, 37,42,47,53,59,64,70,75,81,86,92, 98],
        17:[6,11, 17, 22, 28, 34, 39, 45, 51, 57, 63, 67, 75, 81, 87, 93, 99, 105],
        18:[7, 12, 18, 24, 30, 36, 42, 48, 55, 61, 67, 74, 80, 86, 93, 99, 106, 112],
        19:[7,13,19,25,32,38,45,52,58,65,72,78,85,92, 99, 106, 113, 119],
        20:[8,14,20,27,34,41,48,55,62,69,76,83,90,98,105,112,119, 127],
    }
    # standard normal table (positive values only)
    standardtable = {
    0.0: [.50000, .50399, .50798, .51197, .51595, .51994, .52392, .52790, .53188, .53586],
    0.1: [.53983, .54380, .54776, .55172, .55567, .55962, .56356, .56749, .57142, .57535],
    0.2: [.57926, .58317, .58706, .59095, .59483, .59871, .60257, .60642, .61026, .61409], 
    0.3: [.61791, .62172, .62552, .62930, .63307, .63683, .64058, .64431, .64803, .65173], 
    0.4: [.65542, .65910, .66276, .66640, .67003, .67364, .67724, .68082, .68439, .68793], 
    0.5: [.69146, .69497, .69847, .70194, .70540, .70884, .71226, .71566, .71904, .72240], 
    0.6: [.72575, .72907, .73237, .73565, .73891, .74215, .74537, .74857, .75175, .75490], 
    0.7: [.75804, .76115, .76424, .76730, .77035, .77337, .77637, .77935, .78230, .78524],
    0.8: [.78814, .79103, .79389, .79673, .79955, .80234, .80511, .80785, .81057, .81327],
    0.9: [.81594 ,.81859, .82121, .82381, .82639, .82894, .83147, .83398, .83646, .83891],
    1.0: [.84134, .84375, .84614, .84849, .85083, .85314, .85543, .85769, .85993, .86214],
    1.1: [.86433, .86650, .86864, .87076, .87286, .87493, .87698, .87900, .88100, .88298] ,
    1.2: [.88493, .88686, .88877, .89065, .89251, .89435, .89617, .89796, .89973, .90147]  ,
    1.3: [.90320, .90490, .90658, .90824, .90988, .91149, .91309, .91466, .91621, .91774]  ,
    1.4: [.91924, .92073, .92220, .92364, .92507, .92647, .92785, .92922, .93056, .93189]  ,
    1.5: [.93319, .93448, .93574, .93699, .93822, .93943, .94062, .94179, .94295, .94408]  ,
    1.6: [.94520, .94630, .94738, .94845 ,.94950 ,.95053 ,.95154 ,.95254 ,.95352, .95449]  ,
    1.7: [.95543, .95637, .95728, .95818, .95907, .95994, .96080, .96164, .96246, .96327]  ,
    1.8: [.96407, .96485, .96562, .96638 ,.96712 ,.96784 ,.96856 ,.96926 ,.96995 ,.97062]  ,
    1.9: [.97128, .97193, .97257, .97320 ,.97381 ,.97441 ,.97500 ,.97558 ,.97615 ,.97670]  ,
    2.0: [.97725, .97778, .97831, .97882 ,.97932 ,.97982 ,.98030 ,.98077 ,.98124 ,.98169]  ,
    2.1: [.98214, .98257, .98300, .98341 ,.98382 ,.98422 ,.98461 ,.98500 ,.98537 ,.98574] ,
    2.2: [.98610, .98645, .98679, .98713 ,.98745 ,.98778 ,.98809 ,.98840 ,.98870 ,.98899]  ,
    2.3: [.98928, .98956, .98983, .99010, .99036, .99061, .99086 ,.99111 ,.99134 ,.99158] ,
    2.4: [.99180, .99202, .99224 ,.99245 ,.99266 ,.99286 ,.99305 ,.99324 ,.99343 ,.99361]  ,
    2.5: [.99379, .99396, .99413 ,.99430, .99446 ,.99461 ,.99477 ,.99492 ,.99506 ,.99520] ,
    2.6: [.99534, .99547, .99560, .99573, .99585, .99598, .99609, .99621, .99632, .99643] ,
    2.7: [.99653, .99664, .99674, .99683, .99693, .99702, .99711, .99720, .99728, .99736] ,
    2.8: [.99744, .99752, .99760, .99767, .99774 ,.99781 ,.99788 ,.99795 ,.99801 ,.99807]  ,
    2.9: [.99813, .99819 ,.99825 ,.99831 ,.99836 ,.99841 ,.99846 ,.99851 ,.99856 ,.99861]  ,
    3.0: [.99865, .99869 ,.99874 ,.99878 ,.99882 ,.99886 ,.99889 ,.99893 ,.99896 ,.99900]  ,
    3.1: [.99903, .99906, .99910, .99913, .99916, .99918, .99921, .99924 ,.99926 ,.99929]  ,
    3.2: [.99931, .99934, .99936, .99938, .99940, .99942, .99944, .99946 ,.99948 ,.99950 ] ,
    3.3: [.99952, .99953, .99955, .99957, .99958, .99960, .99961, .99962 ,.99964 ,.99965 ] ,
    3.4: [.99966, .99968, .99969, .99970, .99971, .99972, .99973, .99974 ,.99975 ,.99976 ] ,
    3.5: [.99977, .99978, .99978, .99979, .99980, .99981, .99981, .99982 ,.99983 ,.99983 ] ,
    3.6: [.99984, .99985, .99985, .99986, .99986, .99987, .99987, .99988 ,.99988 ,.99989]  ,
    3.7: [.99989, .99990, .99990, .99990, .99991, .99991, .99992, .99992 ,.99992 ,.99992],
    3.8: [.99993, .99993, .99993, .99994, .99994, .99994, .99994, .99995 ,.99995 ,.99995]  ,
    3.9: [.99995, .99995, .99996, .99996, .99996, .99996, .99996, .99996 ,.99997 ,.99997] }
    # import stats for instant magic
    import statistics
    #n2 = row
    if n2<3 or (n2 == 3 and n1 == 1) or (n2 == 4 and n1 == 1):
        return "Sample size too small for Mann-Whitney test."
    else:
        try:
            # calculate median for first group
            median1 = statistics.median(data1)
            # create a formatted string from median 1 (reduce to two characters after the point)
            medianstr1 =  "{:.2f}".format(median1)
            # calculate median for second group
            median2 = statistics.median(data2)
            # create a formatted string from median 2 (reduce to two characters after the point)
            medianstr2 =  "{:.2f}".format(median2)
            # for group 1: calculate first quartile
            one_q1 = (n1+1) / 4
            # for group 1: calculate third quartile
            one_q3 = (n1+1) * 3/4
            # calculate interquartile range for group 1 and format (two characters after the point)
            IQR1 = "{:.2f}".format(one_q3 - one_q1)
            # for group 2: calculate first quartile
            two_q1 = (n2+1) / 4
            # for group 2: calculate third quartile
            two_q3 = (n2+1) * 3/4
            # calculate interquartile range for group 2 and format (two characters after the point)
            IQR2 = "{:.2f}".format((two_q3 - two_q1)) 
            # full dataset is data of group1 and group2 added
            data = data1 + data2
            # sort the data
            data.sort()
            # assign i to 1
            i = 1
            # create list ranked_data
            ranked_data = []
            for value in data:
                ranked_data.append([value, i])
                i+=1
            # print(ranked_data)
            # check how 
            for i in range(len(ranked_data)):
                counter = 0
                ranks = 0
                for j in range(len(data)):
                    if ranked_data[i][0] == data[j]:
                        counter +=1
                        ranks += int(ranked_data[j][1])
                #print("rank",i[1], ranks)
                    #print(ranks)
                adjustedrank = ranks / counter
                # print(adjustedrank)
                ranked_data[i] = [ranked_data[i][0], adjustedrank] 
            # print(ranked_data)

            # get adjusted ranks of each group
            #create empty list IV1_ranks to store list of ranks values of group 1 have gotten
            IV1_ranks=[]
            # loop over data of group 1
            for val in data1: 
                #print(val)
                # looop over ranked_data
                for value in ranked_data:
                    #print(value[0])
                    # if val in data of group 1 is the same as the first index of the value in ranked_data
                    if val == value[0]:
                        # append the adjusted rank at index 1 to IV1_ranks
                        IV1_ranks.append(value[1])
                        # break the loop over the ranked_data (because not more than one value can be fitting for one value in data1)
                        break
            # sum of ranks for group 1 is the sum of IV1_ranks
            r1 = sum(IV1_ranks)

            # create empty list IV2_ranks to store list of ranks values of group 2 have gotten
            IV2_ranks=[]
            # loop over data of group 2
            for val in data2: 
                # looop over ranked_data
                for value in ranked_data:
                    # if val in data of group 2 is the same as the first index of the value in ranked_data
                    if val == value[0]:
                        # append the adjusted rank at index 2 to IV2_ranks
                        IV2_ranks.append(value[1])
                        # break the loop over the ranked_data (because not more than one value can be fitting for one value in data2)
                        break
            # sum of ranks for group 2 is the sum of IV2_ranks
            r2 = sum(IV2_ranks)
            
            # Calcuulate U 
            # determine which group has the higher sum of ranks
            # if its group 1
            if r1 > r2:
                # group 1s sum of ranks is r
                r= r1
                # group 1s sample size is n
                n= n1
            # if its group 2
            else: 
                # group 2s sum of ranks is r
                r= r2
                # group 2s sample size is n
                n = n2
            # calculate U
            U = (n1*n2) + ((n*(n+1))/2) - (r)
            # create U as a string with the format of two numbers after the decimal
            Ustr = "{:.2f}".format(U)
            #print(U)

            # test for statistical significance
            # if sample is not more than 20 people
            if n1+n2 <=20:
                # look up row in Mann-Whitney table  (n2 = row)
                Uval = mannwhitneytable[n2]
                # look for column in Mann-Whitney table (n1 = column)
                Ucritical = Uval[n1-1]
                # calculate z score
                z = (U -((n1*n2)/2)) / math.sqrt(((n1*n2)*(n1+n2+1))/12)
                # make a string formatted to 2 numbers after decimal
                z = "{:.2f}".format(z)
                # zstr = z
                zstr = z
                # last value of zstr as integer is last number of z
                lastz = int(zstr[-1])
            else:
                # no U critical for N > 20 -> make it = U so it is never smaller than U critical for check below
                Ucritical = U 
                # calculate z score
                z = (U -((n1*n2)/2)) / math.sqrt(((n1*n2)*(n1+n2+1))/12)
                # make a string formatted to 2 numbers after decimal
                z = "{:.2f}".format(z)
                # zstr = z
                zstr = z
                # last value of zstr as integer is last number of z
                lastz = int(zstr[-1])
            # print(zstr)
            # if z is negative
            if zstr[0] == "-":
                # cut off the first value of it and the last
                zstr = zstr[1:-1:]
                # print(zstr)
                # convert it to a float
                z_float = float(zstr)
                # look up row in standard table
                zval = standardtable[z_float]
                # column in standard table = last number of z
                zval = zval[lastz]
                # z is 1 + z
                zval = 1 + float(z)
            # if z is positive
            else:
                # only cut off last value
                zstr= zstr[:-1:]
                # convert it to a float
                z_float = float(zstr)
                # look up row in standard table
                zrow = standardtable[z_float]
                # column in standard table = last number of z
                zval = zrow[lastz] 

            # calculate rosenthals R --> effect size
            r = "{:.2f}".format(zval/ math.sqrt(n1+n2))

            # if median of group 1 is higher than that of group 2 
            if median1 > median2:
                # highlow is higher
                highlow = "higher"
            # if median of group 1 is equal to that of group 2 
            elif median1 == median2:
                # highlow is equal
                highlow = "equal"
            # if median of group 1 is lower than that of group 2 
            else:
                # highlow is lower
                highlow = "lower"
            # if U smaller than U critical (N<=20) or z significant at .05 level
            if (U < Ucritical) or (zval <= 0.05): 
                #significant
                # returnstr = APA style reporting sentence for significant Mann-Whitney test
                if highlow != "equal":
                    returnstr = str("In this sample of " + str(n1+n2) + " participants, those in group " + str(IV1) + " had " + highlow + " scores in " + str(DV) + " (Median =" + medianstr1 +", IQR = " + str(IQR1) +") than those in group " + str(IV2) + " (Median = " +medianstr2 + ", IQR = " + str(IQR2)+ "), the difference was statistically significant, U =" + Ustr + ", z = " + z + ", p < .05, r =" + r + ".") 
                else: 
                    returnstr = str("In this sample of " + str(n1+n2) + " participants, those in group " + str(IV1) + " had " + highlow + " scores in " + str(DV) + " (Median =" + medianstr1 +", IQR = " + str(IQR1) +") to those in group " + str(IV2) + " (Median = " +medianstr2 + ", IQR = " + str(IQR2)+ "), the difference was statistically significant, U =" + Ustr + ", z = " + z + ", p < .05, r =" + r + ".") 
            # if U bigger than U critical (N<=20) or z INsignificant at .05 level
            else:
                # insignificant
                # returnstr = APA style reporting sentence for INsignificant Mann-Whitney test
                # if highlow is equal
                if highlow != "equal":
                    # change string to "to"
                    returnstr = str("In this sample of " + str(n1+n2) + " participants, those in group " + str(IV1) + " had " + highlow + " scores in " + str(DV) + " (Median =" + medianstr1 +", IQR =" + str(IQR1) +") than those in group " + str(IV2) + " (Median = " + medianstr2 + ", IQR = " + str(IQR2)+ "), however, the difference was not statistically significant, U =" + Ustr + ", z = " + z + ", p > .05, r =" + r + ".") 
                # if not
                else: 
                    # change string to "than"
                    returnstr = str("In this sample of " + str(n1+n2) + " participants, those in group " + str(IV1) + " had " + highlow + " scores in " + str(DV) + " (Median =" + medianstr1 +", IQR = " + str(IQR1) +") to those in group " + str(IV2) + " (Median = " +medianstr2 + ", IQR = " + str(IQR2)+ "), the difference was statistically significant, U =" + Ustr + ", z = " + z + ", p < .05, r =" + r + ".")
            # return the APA style sentence
            return returnstr
        except:
            return "Failed to compute Mann-Whitney Test. Check your input."

def two_independent_groups_checker(DV:str = "missing", IV1:str="missing", IV2:str="missing", data1:list="missing", data2: list="missing")->str:
    # print(DV, IV1, IV2, data1, data2)
    '''
    purpose:
    takes dependent variable, two independent groups and their data

    procedure: 
    checks if the equal variances can be assumed (Levene's Test)  --> checks  at p = .05 alpha level 
    checks if normally distributed (usually also other things have to be checked but for the purpose of this code: if skewness and kurtosis are fine normal distribution is assumed to be True )
    if so: conducts ttest (calls ttest function)
    if not: conducts mann-whitney (calls mann-whitney function)

    return:
    returns returnstring from statistical test or error message 

    assumption:
    all data in the lists are integers
    '''
    # import statistics for instant magic
    import statistics
    # ftable with columns: 1 2 3 4 5 6 7 8 9 10 12 15 20 24 30 60 120 unlimited  --> >300
    f_table = {0: "error", 
                1:[161, 200, 216, 225, 230, 234, 237, 239, 241, 242, 244, 246, 248, 249, 250, 252, 253, 254], 
               2: [18.5, 19, 19.2, 19.2, 19.3, 19.3, 19.4, 19.4, 19.4, 19.4, 19.4, 19.4, 19.4, 19.5,19.5, 19.5, 19.5, 19.5],
               3: [10.1, 9.55, 9.28, 9.12, 9.01, 8.94, 8.89, 8.85, 8.81, 8.79, 8.74, 8.70, 8.66, 8.64, 8.62, 8.57, 8.55, 8.53],
               4: [7.71, 6.94, 6.59, 6.39, 6.26, 6.16, 6.09, 6.04, 6.00, 5.96, 5.91, 5.86, 5.80, 5.77, 5.75, 5.69, 5.66, 5.63],
               5: [6.61, 5.79, 5.41, 5.19, 5.05, 4.95, 4.88, 4.82, 4.77, 4.74, 4.68, 4.62, 4.56,4.53, 4.50, 4.43, 4.40, 4.37],
               6: [5.99, 5.14, 4.76, 4.53, 4.39, 4.28, 4.21, 4.15, 4.10, 4.06, 4.00, 3.94, 3.87, 3.84, 3.81, 3.74, 3.70, 3.67],
               7: [5.59, 4.74, 4.35, 4.12, 3.97, 3.87, 3.79, 3.73, 3.68, 3.64, 3.57, 3.51, 3.44, 3.41, 3.38, 3.30, 3.27, 3.23],
               8: [5.32, 4.46, 4.07, 3.84, 3.69, 3.58, 3.50, 3.44, 3.39, 3.35, 3.28, 3.22, 3.15, 3.12, 3.08, 3.01, 2.97, 2.93],
               9: [5.12, 4.26, 3.86, 3.63, 3.48, 3.37, 3.29, 3.23, 3.18, 3.14, 3.07, 3.01, 2.94, 2.90, 2.86, 2.79, 2.75, 2.71],
               10: [4.96, 4.10, 3.71, 3.48, 3.33, 3.22, 3.14, 3.07, 3.02, 2.98, 2.91, 2.84, 2.77, 2.74, 2.70, 2.62, 2.58, 2.54],
               12: [4.75, 3.89, 3.49, 3.26, 3.11, 3.00, 2.91, 2.85, 2.80, 2.75, 2.69, 2.62, 2.54, 2.51, 2.47, 2.38, 2.34, 2.30],
               15: [4.54, 3.68, 3.29, 3.06, 2.90, 2.79, 2.71, 2.64, 2.59, 2.54, 2.48, 2.40, 2.33, 2.29, 2.25, 2.16, 2.11, 2.07],
               20: [4.35, 3.49, 3.10, 2.87, 2.71, 2.60, 2.51, 2.45, 2.39, 2.35, 2.28, 2.20, 2.12, 2.08, 2.04, 1.95, 1.90, 1.84],
               24: [4.26, 3.40, 3.01, 2.78, 2.62, 2.51, 2.42, 2.36, 2.30, 2.25, 2.18, 2.11, 2.03, 1.98, 1.94, 1.84, 1.79, 1.73],
               30: [4.17, 3.32, 2.92, 2.69, 2.53, 2.42, 2.33, 2.27, 2.21, 2.16, 2.09, 2.01, 1.93, 1.89, 1.84, 1.74, 1.68, 1.62],
               60: [4.00, 3.15, 2.76, 2.53, 2.37, 2.25, 2.17, 2.10, 2.04, 1.99, 1.92, 1.84, 1.75, 1.70, 1.65, 1.53, 1.47, 1.39],
               120:[3.92, 3.07, 2.68, 2.45, 2.29, 2.18, 2.09, 2.02, 1.96, 1.91, 1.83, 1.75, 1.66, 1.61, 1.55, 1.43, 1.35, 1.25],
               300: [3.84, 3.00, 2.60, 2.37, 2.21, 2.10, 2.01, 1.94, 1.88, 1.83, 1.75, 1.67, 1.57, 1.52, 1.46, 1.32, 1.22, 1.00] 
               }
    try:
        # if any variable is missing
        if DV == "missing" or IV1=="missing" or IV2=="missing" or data1 =="missing" or data2=="missing":
            # return that something is missing
            return "A variable is missing. Check your input."
        # control for ints, floats or boold in the IVs and DVs
        if (type(IV1) == int or type(IV1) == float or type(IV1) == bool) or (type(IV2) == int or type(IV2) == float or type(IV2) == bool) or (type(DV) == int or type(DV) == float or type(DV) == bool):
            # if any of them is a float, bool or int return error message
            return "Invalid variable type."
        if type(data1) != list or type(data2) != list:
            return "Invalid input type for the data."
        # loop over data 1 
        for i in data1:
            # if data is not an int
            if type(i) != int:
                # return error message
                return "Invalid data type."
        # loop over data 2 
        for j in data2:
            # if data is not an int
            if type(j) != int:
                # return error message
                return "Invalid data type"
        # get group1 sample size 
        n1 = len(data1)
        # get group2 sample size 
        n2 = len(data2)
        # print(n1,n2)
        
        #Assumption: Homogenity of variance
        #Means
        # calculate mean of first group
        # set sumdata1 to 0
        sumdata1 = 0
        # loop over data of first group
        for i in data1:
            # add each value to sumdata1
            sumdata1+=i
        # calculate mean for group1
        mean1 = sumdata1/n1
        
        # calculate mean of second group
        # set sumdata2 to 0
        sumdata2 = 0
        # loop over data of second group
        for i in data2:
            # add each value to sumdata2
            sumdata2+=i 
        # calculate mean for group2
        mean2 = sumdata1/n2 
        # print(mean1,mean2)
        
        #DF
        # calculate degrees of freedom 
        # if there is not only one person in group1
        if n1 != 1:
            # subtract one from sample size
            df1 = n1-1
        # for completeness: if only one person
        else:
            # leave df1
            df1 = 1

        # if there is not only one person in group 2
        if n2 != 1:
            # subtract one from sample size
            df2 = n2-1 
        # for completeness: if only one person
        else:
            # leave df2
            df2=1
        
        # Variances
        # calculate sum of squares 
        # set s1 to 0
        s1 = 0
        # set s2 to 0
        s2 = 0
        # loop over data1
        for val1 in data1:
            # add difference of value and mean by power of 2 to s1
            s1 += (val1- mean1)**2
        # calculate variance of group1
        variance1 = s1/df1

        # loop over data2
        for val2 in data2: 
            # add difference of value and mean by power of 2 to s2
            s2 += (val2- mean2)**2
        # calculate variance of group2
        variance2= s2/df2
        # print(variance1,variance2)
        
        # Find F
        #larger s/ smaller s 
        # prevent division by 0 error
        if variance2 == 0.0:
            # if variance2 is 0 F is varaince1
            F = variance1
        # if variance2 is not 2
        else: 
            # check which variance is bigger
            # if its variance 1: divide by variance2
            if variance1 > variance2: 
                # prevent division by 0 error
                if variance2 == 0.0:
                    # if variance2 is 0 F is varaince1
                    F = variance1
                # if variance2 not = 0
                else: 
                    # calculate F
                    F = variance1/variance2
            # if its variance 2
            else: 
                # prevent division by 0 error
                if variance1 == 0.0:
                    # if variance2 is 0 F is varaince1
                    F = variance2
                # if variance2 not = 0
                else: 
                    # divide by variance1
                    F =  variance2/variance1
        # print(F)
        # column = larger sample  & row = smaller sample 
        
        # find out which group has bigger df
        # if group 1
        if df1 > df2:
            # group2 is small_dv
            small_dv = df2
            # group1 is big_dv
            big_dv = df1
        # if group 2
        else: 
            # group1 is small_dv
            small_dv = df1
            # group2 is big_dv
            big_dv = df2
        # print(small_dv, big_dv)
        # check if dfs have to be changed for Ftable: call testdfchanger with dfs: smallie & biggie = adjusted dfs
        smallie, biggie = ttestdfchanger(small_dv,big_dv)
        # print(smallie,biggie)
        # loop over Ftable
        for keys, values in f_table.items():
            # if the key is the smaller df and the bigger df is smaller/equal 10
            if keys == smallie and biggie <= 10:
                # look up fcritical at column biggie-1
                Fcritical = values[biggie-1]
            # if bigger df is bigger than 10
            elif keys == smallie and biggie > 10:
                # if its 12
                if biggie == 12: 
                    # column is 10
                    Fcritical = values[10]
                # if its 15
                elif biggie == 15:
                    # column is 11
                    Fcritical = values[11]
                # if its 20
                elif biggie == 20:
                    # column is 12
                    Fcritical = values[12]
                # if its 24
                elif biggie == 24: 
                    # column is 13
                    Fcritical = values[13]
                # if its 30
                elif biggie ==30:
                    # column is 14
                    Fcritical = values[14]
                # if its 60
                elif biggie == 60:
                    # column is 15
                    Fcritical = values[15]
                # if its 120
                elif biggie == 120:
                    # column is 16
                    Fcritical = values[16]
                # if its 300
                elif biggie==300:
                    # column is 17
                    Fcritical = values[17]
        # print(Fcritical)
        # check wether equal variances can be assumed
        # if F smaller than Fcritical
        if F < Fcritical:
            # means variances are equal
            equalvariances= True
        else:
            # means variance not equal
            equalvariances= False
        #print(equalvariances)

        #Assumption: Normal distribution of DV
        # data is data of both groups
        data = data1 + data2
        # total sample size = n
        n = n1+n2
        # calculate mean for all data
        datamean = statistics.mean(data)

        #calculate sum of squares
        # define sum of squares
        s2 = 0
        # define sum of squares
        s3 = 0 
        # define sum of squares
        s4 = 0
        # loop over data
        for i in data:
            # calculate deviation of value from mean
            deviation = i - datamean
            # add to sum of squares
            s2 = deviation**2 + s2
            # add to sum of **3
            s3 = deviation**3 + s3
            # add to sum of **4
            s4 = deviation**4 + s4
        # calculate variance
        variance = s2/(n-1)
        # calculate standard deviation
        sd = variance**0.5
        # second moment
        m2 = s2/n
        # fourth moment
        m4 = s4/n
        # calculate skewness
        data_skewness = (s3 / ((n-1)*sd**3)) 
        # calculate kurtosis
        data_kurtosis = ((m4/m2**2)-3) 
        # print(data_skewness, data_kurtosis)
        # if skewness between -1 and 1 (does not reach 1) and kurtosis between -1 and 1 (does not reach 1)
        if (data_skewness < 1.0 and data_skewness > -1.0) and (data_kurtosis < 1.0 and data_kurtosis > -1.0):
            # data is normally distributed
            normaldistribution = True
        # if skewness and/or kurtosis are bigger than 1 or smaller than -1 (1 or beyond)
        else:
            # data is not normally distributed
            normaldistribution = False 
        # if assumptions for ttest met
        # if variances equal and data normally distributed
        if equalvariances and normaldistribution:
            # run ttest
            # print("Run ttest")
            # call ttest with the variables  DV, IV1, IV2,  n1, n2, variance1, variance2, mean1, mean2 -> returnstring is what is returned by ttest 
            returnstring = ttest(DV, IV1, IV2, n1, n2, variance1, variance2, mean1, mean2)
        # if assumptions not met
        else:
            # run mann whitney test
            #print("Run mannwhitney")
            # call mannwhitney with the variables  DV, IV1, IV2, data1, data2, n1, n2 -> returnstring is what is returned by  mannwhitney
            returnstring = mannwhitney(DV, IV1, IV2, data1, data2, n1, n2)
        # return the returnstring
        return returnstring
    # exception handling
    except:
        # return fail to check assumptions
        return "Failed to check the assumptions of the t-test. Check your input."

# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", [1,2,3,4,5],[1,2,3,4,5])) # In this sample of 10 participants, those in group smoker had equal scores in loneliness (Median =3.00, IQR = 3.00) to those in group non-smoker (Median = 3.00, IQR = 3.00), the difference was statistically significant, U =12.50, z = 0.00, p < .05, r =0.16.
# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", ((1,2,3,4,5)),[1,2,3,4,5])) #Failed to check the assumptions of the t-test. Check your input.
# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", [1,1,1,1,2],[5,5,5,5,4])) # In this sample of 10 participants, those in group smoker had lower scores in loneliness (Median =1.00, IQR = 3.00) than those in group non-smoker (Median = 5.00, IQR = 3.00), the difference was statistically significant, U =0.00, z = -2.61, p < .05, r =-0.51.
# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", [],[])) # Could not check for ttest assumptions
# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", [],[1])) # Could not check for ttest assumptions
# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", [1,1,2,2,2,2,2,2,2,3,3],[3,3,4,4,4,4,4,4,4,5,5]))
# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", [1,1,2,2,2,2,2,2,2,3,3],[3,3,4,4,4,4,4,4,4,5,5])) # In this sample of 22 participants, those in group smoker had lower scores in loneliness (Median =2.00, IQR = 6.00) than those in group non-smoker (Median = 4.00, IQR = 6.00), the difference was statistically significant, U =2.00, z = -3.84, p < .05, r =-0.61.
# print(two_independent_groups_checker("loneliness", "smoker", "non-smoker", [1,1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5])) # An independent samples t-test indicated no statistically significant differences in loneliness between participants in group smoker (M = 2.80, SD = 1.14) and those in group non-smoker (M =2.80, SD =1.36), t(20)=0.0, p > .05 , Cohen’s d =0.00
# print(two_independent_groups_checker(("loneliness"), ("smoker"), ("smoker"), [1,1,2,2,2,2,2,2,2,3,3],[3,3,4,4,4,4,4,4,4,5,5])) # In this sample of 22 participants, those in group smoker had lower scores in loneliness (Median =2.00, IQR = 6.00) than those in group non-smoker (Median = 4.00, IQR = 6.00), the difference was statistically significant, U =2.00, z = -3.84, p < .05, r =-0.61.
# print(two_independent_groups_checker(["loneliness"], ("smoker"), ("smoker"), [1,1,2,2,2,2,2,2,2,3,3],[3,3,4,4,4,4,4,4,4,5,5])) # In this sample of 22 participants, those in group smoker had lower scores in ['loneliness'] (Median =2.00, IQR = 6.00) than those in group smoker (Median = 4.00, IQR = 6.00), the difference was statistically significant, U =2.00, z = -3.84, p < .05, r =-0.61.
# print(two_independent_groups_checker(["loneliness"], ["smoker"], ["non-smoker"], [1,1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5])) # An independent samples t-test indicated no statistically significant differences in ['loneliness'] between participants in group ['smoker'] (M = 2.80, SD = 1.14) and those in group ['non-smoker'] (M =2.80, SD =1.36), t(20)=0.00, p > .05 , Cohen’s d =0.00
# print(two_independent_groups_checker(True, ["smoker"], ["non-smoker"], [1,1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5])) # Invalid variable type
# print(two_independent_groups_checker("loneliness", ["smoker"], ["non-smoker"], ["Hi"],[2,2,2,3,3,3,3,5,5,5])) # Invalid data type
# print(two_independent_groups_checker("loneliness", ["smoker"], ["non-smoker"], [1,1.1,2,3,3,3,3,4,4,4],[2,2,2,3,3,3,3,5,5,5])) #"Invalid data type."
# print(two_independent_groups_checker("loneliness", ["smoker"], ["non-smoker"], [1,1,2,3,3,3,3,4,4,4],[2,2.4,2.3,3,3,3,3.5,5,5,5]))
# print(two_independent_groups_checker("loneliness", ["smoker"], ["non-smoker"], [True],[2,2,2,3,3,3,3,5,5,5])) #Failed to check the assumptions of the t-test. Check your input.
# print(two_independent_groups_checker("loneliness", ["smoker"], ["non-smoker"], [1.2,2],[2,3])) # Invalid data type
# print(two_independent_groups_checker("loneliness", ["smoker"], ["non-smoker"], [1,2],[2,3])) # Sample size too small for Mann-Whitney test
# print(two_independent_groups_checker("loneliness", [55], ["non-smoker"], [1,2,3,4],[2,3,4,5])) # In this sample of 8 participants, those in group [55] had lower scores in loneliness (Median =2.50, IQR = 2.50) than those in group ['non-smoker'] (Median = 3.50, IQR = 2.50), the difference was statistically significant, U =4.50, z = -1.01, p < .05, r =-0.00.
# print(two_independent_groups_checker("loneliness", 55, ["non-smoker"], [1,2,3,4],[2,3,4,5])) # Invalid variable type
# two_independent_groups_checker("loneliness", "smoker", ["non-smoker"], ["hi",2,3,4],[2,3,4,5]) # Invalid data type
# print(two_independent_groups_checker("loneliness", "smoker", ["non-smoker"], (3,2,3,4),[2,3,4,5]))
# print(two_independent_groups_checker("loneliness", "smoker", ["non-smoker"], "hello",[2,3,4,5]))
#print(two_independent_groups_checker("loneliness", "smoker", ["non-smoker"], True,[2,3,4,5]))
# print(two_independent_groups_checker({"loneliness": 1}, "smoker", ["non-smoker"], [2,3,4,5],[2,3,4,5]))
# print(two_independent_groups_checker("loneliness", "smoker", ["non-smoker"], {2:1,3:3,4:4,5:9},[2,3,4,5]))
# print(two_independent_groups_checker("smoker", ["non-smoker"], [2,3,4,5],[2,3,4,5]))
# template for calling functions in another file

# def print_function(input_string:str) -> str:
#     '''
#     input_string - string input\n
#     return input_string with a nice happy face
#     '''
#     try:
#         return input_string+" :)"
#     except:
#         return "Oops"


# def print_function2(input_string:str, added_string:str = ":(") -> str:
#     '''
#     input_string - string input\n
#     return input_string with added_string added to it
#     '''
#     try:
#         return input_string+" "+added_string
#     except:
#         return "Oops"
