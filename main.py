#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Travis_Chua>
#Group Name: <...>
#Class: <PN2004K>
#Date: <22/02/2021>
#Version: <1>
#region: S. E. A region between 1998 to 2008 
#########################################################################

#########################################################################
#import pandas for data analysis
#########################################################################
import pandas as pd
#import matplotlib.pyplot as plt for displaying data
import matplotlib.pyplot as plt
class DataAnalysis():
  def __init__(self):
    Display_Visitors()
#########################################################################
    
    
def Display_Visitors():
  df = pd.read_csv('MonthyVisitors.csv')
  region_list = ["1"]
  region_name = ""
  time_name = ''
  visitor = []
  countries = []
  total_visitor = []
  visitor_dict = {}
  #Check for the right input
  while True:
    x =  input("Enter start date YYYYMMM eg.(1998Jan) Min:1998Jan : ")
    #if error continue prompt for input
    if not x in date_list:
      print('Error!')
    #if no error break out of loop
    elif x in date_list:
      break
  #Check for the right input
  while True:
    y= input("Enter end date YYYYMMM eg.(2008May) Max:2008Nov : ")
    #if error continue prompt for input
    if not y in date_list:
      print("Error!")
    #if no error break out of loop
    elif y in date_list:
      break
  #assign variable value according to input
  a = date_dict[x]
  a = int(a)
  b = date_dict[y]
  b = int(b)
  b =  b+1
  #Print guide for user
  print("Select a region:", "\n", "(1)South East Asia(SEA)", )
  while True:
        #prompt for user input
        region = input("Enter a region. Enter 1 for SEA : ")
        region = str(region)
        # if user input not in region_list , print error
        if not region in region_list:
            print("Error!")
        #else if region in region_list , break out of loop
        elif region in region_list:
            break
  if region == "1":
        c = 2
        c = int(c)
        d = 9
        d = int(d)
        region_name = "South-East Asia"
  #Show user region and time period chosen by them
  print(region_name, "was selected for region and", time_name,
          "was selected for time period.")
  #specifying the dataframe
  df
  df = df.iloc[a:b, c:d]
  #index d - index c to find how many countries in region
  country_idx = d - c
  #specifying which columns to iterate through
  df.columns[0:int(country_idx)]
  #for loop to append every country in the columns
  for country in df.columns[0:int(country_idx)]:
      countries.append(country)
      #append every visitor by columns
      for visitors in df[country]:
          visitor.append(visitors)
  #converting the na to 0 and string integer to integer for addition purposes
  for i in range(0, len(visitor)):
      if visitor[i] == " na ":
          visitor[i] = 0
      else:
          visitor[i] = int(visitor[i])
  #find out how many nummber in the list
  number_of_visitors = len(visitor)
  #counter = how many number a country have
  counter = number_of_visitors / len(countries)
  #Initialize Variables
  Index1 = 0
  Index2 = int(counter)
  #summing the total for one country and appending it to total_visitor list
  for i in range(0, (len(countries))):
      total_visitor.append(sum(visitor[Index1:Index2]))
      Index1 = Index1 + (int(counter))
      Index2 = Index2 + (int(counter))
  #create dict according countries(key):total_visitor(value)
  visitor_dict = {countries[i]: total_visitor[i]for i in range(len(countries))}
  #sort dictionary in descending order
  sort_visitor_dict = sorted(visitor_dict.items(),key=lambda x: x[1],reverse=True)
  #convert list to dictionary
  visitor_dict = dict(sort_visitor_dict)
  #convert dictionary to datatframe
  df = pd.DataFrame(list(visitor_dict.items()),columns=['Country', 'Visitors'])
  #print the data table in descending order
  print(df)
  #Initialize lists
  labels = []
  sizes = []
  #appending the list with key and values from the dictionary
  for x, y in visitor_dict.items():
    labels.append(x)
    sizes.append(y)
  #initialize list and variable
  distance = 0.2
  seperate = []
  #for loop to append distance according to amount of region in countries
  for i in range(0, len(countries)):
    seperate.append(distance)
  # Plot pie chart
  plt.pie(sizes,labels=labels, explode=seperate, startangle=180, autopct='%1.2f%%',shadow=True)
  plt.axis('equal')
  #create legend
  plt.legend(loc="best")
  #Show pie chart
  plt.show()
if __name__ == '__main__':
    #Project Title
    print('######################################')
    print('  Data Analysis App - PYTHON Project  ')
    print('######################################')
    #initialize list and variables
    df = pd.read_csv('MonthyVisitors.csv')
    year_list = []
    month_list = []
    date_dict = {}
    #appending every year in The "Year" column
    for year in df["Year"]:
      year_list.append(year)
    #removing NaN from the list
    year_list = [x for x in year_list if str(x) != 'nan']
    #removing the decimal point from the int
    year_list = list(map(int,year_list))
    #change the int to str
    year_list = list(map(str,year_list))
    #appending every month in The "Month" column
    for month in df["Month"]:
      month_list.append(month)
    #removing NaN from the list
    month_list = [x for x in month_list if str(x) != 'nan']
    # using list comprehension + zip() 
    # interlist element concatenation 
    date_list = [i + j for i, j in zip(year_list, month_list)] 
    #initialize list and variables
    index_list = []
    index_number = 0
    #appending index numbers to the length of date list
    for i in range(0,len(date_list)):
      index_list.append(index_number)
      index_number=index_number+1
    #Dictionary that index every month and year in data
    date_dict  = { date_list[i]: index_list[i]for i in range(len(date_list))}
    #perform data analysis on specific excel (CSV) file
    DataAnalysis() 