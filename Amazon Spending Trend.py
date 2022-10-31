
import pandas as pd  #pd tells python to use pandas to operations
df = pd.read_csv('/Users/nyadual/Desktop/amazon_orders_history.csv')
df.head()
df.shape   # To get the know the sizw of the dataset; this dataset has 195 rows and 13 columns

#Cleaning the dataset
#To proceed with the analysis, i have to clean the data. for instance i need to remove the $ 
#To do this i will  replace Null value with a 0

df = df.fillna(0)
df.head()

#this function remove $ from total row
df["total"] = df["total"].str.replace('$','', regex =True).astype(float)
df.head()

#Calaculating the total spent on amazon from january 2019 to october 2022
df["total"].sum() # 9306.369999999999

#Calculate the mean of my purchases/ the mean is can be use to find the average spending hence
#the avaerage spent is $48
df["total"].mean() # 47.724974358974315 
df["total"].median() # 35.78
df["total"].max()  #352.67
df["total"].min() #0.0 what on earth i got for free on amazon lol


# Calaculate how much i paid slaes tax. 
#Clean the VAT colum i.e the value added tax
df["VAT"] = df["VAT"].str.replace('$','', regex =True).astype(float)
df.head()

#Analysing the value added Tax column
df["VAT"].sum() #8608.77 am shooked !! That's alot
#some items did not charge aany taxes. To figure out the overall tax charge
#To do that divide total/VAT
df["total"].sum()/df["VAT"].sum()  #overall effective tax rate is  1.08



#Analaysing how my spending habbits have changed over time
# We need to convert dates to datetime so that the computer can recongnized it
#df['date'] = pd.to_datetime(df['date'])
#df.head()
# I will use virtuals to get a good view of my analysis overtime
#To enable matplotib and pandas

df.plot.bar(x = 'date', y = 'total', rot = 90, figsize = (30,20), color = "green")

# To resize the graph, i will use figsize
daily_orders = df.groupby('date').sum()['total']
daily_orders.head()

daily_orders.plot.bar(figsize = (30,20), color = "green")


#Calculate the amount spend on shipping
#Cleaning the shipping row; start by removing the $ 

df["shipping"] = df["shipping"].str.replace('$','', regex =True).astype(float)
df.head()

#calculate the total amount i paid for shipping
df['shipping'].sum() # 448.95000000000005 weird since i use prime
#Avaerage spending for shipping
df['shipping'].mean() # 2.3023076923076937

#Shipping refunded; clean the row for this data
df["shipping_refund"] = df["shipping_refund"].str.replace('$','', regex =True).astype(float)
df.head()
#calculate the total shipping  refund
df['shipping_refund'].sum() #-209.7

#Overall total spent on shipping / since the shipping refund is negative, i used + to - the sums
df['shipping'].sum() + df['shipping_refund'].sum() #239.25000000000006





