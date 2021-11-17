#You will be given two CSV files, one consisting of rules for PV Ventures' budget and another
#consisting of chronological investment opportunities. Any investment that does not violate the
#budget should be assumed to be made, so that the relevant budget is then reduced by that
#amount.
#The output of your program should be a list of investment opportunities which violate the
#budget (each ID on a separate line).
#input
# path/to/budget.csv
# /path/to/investments.csv
#output--->3 5 10
import pandas as pd

df = pd.read_csv ('File name.csv')
