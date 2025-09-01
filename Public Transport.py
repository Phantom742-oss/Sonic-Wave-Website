'''import matplotlib.pyplot as plt
labels = ['Always', 'Often', 'Sometimes', 'Rarely']
percentages = [35, 25, 30, 10]  # Data from page 5
colors = ['red', 'blue', 'green', 'orange']

bars = plt.bar(labels, percentages, color=colors)
plt.title('Frequency of Overcrowding in Public Transport')
plt.xlabel('Frequency')
plt.ylabel('Percentage (%)')
plt.ylim(0, 40)
plt.legend(bars, labels, title="Frequency Levels", bbox_to_anchor=(1.05, 1))
plt.tight_layout()  # Prevents legend overlap
plt.show()'''


'''import matplotlib.pyplot as plt
categories = ['<5%', '5-10%', '10-20%', '>20%']
data = [25, 40, 25, 10]  # Data from page 4
colors = ['red', 'blue', 'green', 'orange']

bars = plt.bar(categories, data, color=colors)
plt.title('Monthly Income Spent on Public Transport')
plt.xlabel('Income Percentage')
plt.ylabel('Percentage (%)')
plt.ylim(0, 45)
plt.legend(bars, categories, title="Income Spent", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()'''



'''import matplotlib.pyplot as plt
options = ['Very convenient', 'Somewhat convenient', 'Inconvenient', 'Very difficult']
values = [20, 35, 30, 15]  # Data from page 4
colors = ['red', 'blue', 'green', 'orange']

bars = plt.bar(options, values, color=colors)
plt.title('Last-Mile Connectivity Convenience')
plt.xlabel('Convenience Level')
plt.ylabel('Percentage (%)')
plt.ylim(0, 40)
plt.xticks(rotation=15)
plt.legend(bars, options, title="Convenience Levels", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()'''



'''import matplotlib.pyplot as plt
measures = ['More security', 'Better lighting', 'More CCTV', 'Women compartments']
votes = [30, 25, 25, 20]  # Data from page 6
colors = ['red', 'blue', 'green', 'orange']

bars = plt.bar(measures, votes, color=colors)
plt.title('Safety Measures Requiring Improvement')
plt.xlabel('Measure')
plt.ylabel('Percentage (%)')
plt.ylim(0, 35)
plt.xticks(rotation=10)
plt.legend(bars, measures, title="Safety Measures", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()'''



#Q1
'''import matplotlib.pyplot as plt

# Data
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
percentages = [69.2, 15.4, 10.3, 5.1, 0]  # Approximated to sum to 100%
color=['Blue','Red','Yellow','Green','Black']
# Plot
plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=age_groups, colors=color, autopct='%1.1f%%' )
plt.title('Age Group Distribution of Respondents')
plt.legend(title="Age Groups")    #bbox_to_anchor=(1, 0.5)
plt.show()'''



#Q2

import matplotlib.pyplot as plt

# Data
occupations = ['Student', 'Working Professional', 'Business Owner', 'Homemaker', 'Retired']
percentages = [64.1, 28.2, 5.1, 2.6, 0]  # Approximated to sum to 100%
color=['Blue','Red','Yellow','Green','Black']
# Plot
plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=occupations, colors=color, autopct='%1.1f%%')
plt.title('Primary Occupation of Respondents')
plt.legend(title="Occupations")
plt.show()




'''
#Q3
import matplotlib.pyplot as plt

# Data
accesible = ['Yes, Always','Sometimes','No, not very easy to acess']
percentages = [57.9 , 28.9, 13.2]  # Approximated to sum to 100%
color=['Blue','Red','Yellow','Green','Black']
# Plot
plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=accesible, colors=color, autopct='%1.1f%%')
plt.title('public transport Location accessibility')
plt.legend(title="How much accesible")
plt.show()
'''





#Q4
'''import matplotlib.pyplot as plt

# Data
accesible = ['Less than 5%','5-10%','10-20%','More than 20%']
percentages = [53.8 , 25.6, 12.8, 7.7]  # Approximated to sum to 100%
color=['Blue','Red','Yellow','Green','Black']
# Plot
plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=accesible, colors=color, autopct='%1.1f%%')
plt.title('public transport Affordability')
plt.legend(title="Occupations")
plt.show()'''





#Q5
'''import matplotlib.pyplot as plt
measures = ['Less than 30 minutes', '30 minutes-1 hours', '1-2 hours', 'More Than 2 hours']
votes = [28.2, 43.6, 20.5, 7.7]  # Data from page 6
colors = ['red', 'blue', 'green', 'orange']

bars = plt.bar(measures, votes, color=colors)
plt.title('time spend in commuting daily')
plt.xlabel('Measure')
plt.ylabel('Percentage (%)')
plt.ylim(0, 50)
plt.xticks(rotation=10)
plt.legend(bars, measures, title="Commuting Time", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()'''








'''import matplotlib.pyplot as plt
measures = ['Yes, always', 'Often', 'Sometimes', 'Rarely']
votes = [38.5, 30.8, 23.1, 7.7]  # Data from page 6
colors = ['red', 'blue', 'green', 'orange']

bars = plt.bar(measures, votes, color=colors)
plt.title('Overcrowding in Public Transports')
plt.xlabel('Measure')
plt.ylabel('Percentage (%)')
plt.ylim(0, 50)
plt.xticks(rotation=10)
plt.legend(bars, measures, title="how much overcrowding", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()'''
























































































































































































































































































































































''''
import matplotlib.pyplot as plt

# Data
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
percentages = [69.2, 15.4, 10.3, 5.1, 0]  # Approximated to sum to 100%

# Plot
plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=age_groups, autopct='%1.1f%%', startangle=90)
plt.title('Age Group Distribution of Respondents')
plt.legend(title="Age Groups", bbox_to_anchor=(1, 0.5))
plt.show()
'''