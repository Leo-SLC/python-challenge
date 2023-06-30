
#Import Data

import csv
from os import path
my_report = open('analysis/Report.txt', 'w')
data = csv.DictReader(open(path.join('Resources','budget_data.csv')))

#Define Variables
months = 0
total = 0
pre_rev = 0
total_ch = 0
inc = ['',0]
dec = ['',0]

#Determine Revenue and Months
for row in data:
    months += 1
    rev = int(row["Profit/Losses"])
    total += rev
    #Prevent the starting value in Jan from affecting the average
    change = rev - pre_rev 
    if pre_rev == 0:
        change = 0

    total_ch += change

    # Greatest increase
    if change > inc[1]:
        inc[0] = row['Date']
        inc[1] = change

    #Greatest Decrease
    if change < dec[1]:
        dec[0] = row['Date']
        dec[1] = change
    
    pre_rev = rev

#Prepare Ouptu
output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${total:,}
    Average Change: ${total_ch/(months - 1):,.2f}
    Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
    Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''
#Print Output and write results file
print(output)
my_report.write(output)





# Tutor Geronimo Perez helped with the f''' function. 
# Assistance in determining formatting percentages was found at: https://medium.com/bitgrit-data-science-publication/python-f-strings-tricks-you-should-know-7ce094a25d43#:~:text=Number%20formatting&text=Or%2C%20if%20you%20want%20f,the%20end%20of%20the%20string.
#Additional help https://www.geeksforgeeks.org/python-maximum-minimum-set/