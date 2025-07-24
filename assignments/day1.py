import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('Orange_Telecom_Churn_Data.csv')

#Aggregate data by groupby 
group_sizes = (data
.groupby('area_code')
.size())
print(group_sizes)

#day_calls vs day_minutes
plt.plot(data.total_day_minutes, 
data.total_day_calls,
ls ='', marker='o')

#calls vs minutes of day and night
plt.plot(data.total_day_minutes, 
data.total_day_calls,
ls ='', marker='o',label = 'day' )
plt.plot(data.total_eve_minutes, 
data.total_eve_calls,
ls ='', marker='x', label = 'evening')

#Joint distribution and scatter plot of day minutes and day calls
sns.jointplot(x='total_day_minutes', 
y='total_day_calls', 
data=data, size=2)
