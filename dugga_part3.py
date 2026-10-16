## Question 3

''''Generating a plot based on the data in cnv_data filen'''
import pandas as pd   # imported this package for 
import matplotlib.pyplot as plt
''''Question 3:a'''
df = pd.read_csv("/home/bahja/cnv_data.csv")  # reading the data file as well as given the path of the  data file
print(df.columns) # this gives the names of the all the columns
print(df.shape)  # this prints antal coumner och antal rader
print(df.head(5)) # this prints the first five lines of the data

plt.scatter(df["position_mb"], df["log2_ratio"], color= "tab:green", marker="o") # creating a one scatter plot figur where from csv file data and give the colums as x och y-axis
plt.xlabel("position_mb")   # naming the x-axis
plt.ylabel("log2_ratio")  # also here y-axis
plt.title("position_mb vs log2_ratio") # give the plot the title here, just used the x-axis name and y-axis name

''''Question 3b'''
plt.savefig("cnv_data_plot.png", dpi= 300)  # saving the plot as a png file with dpi
plt.show()
