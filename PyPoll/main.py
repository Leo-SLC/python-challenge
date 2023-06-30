
#Import Data

import csv
from itertools import count
from os import path
my_report = open('analysis/election_Report.txt', 'w')
data = csv.DictReader(open(path.join('Resources','election_data.csv')))

#Define Initial variables
ballots = 0
can1ballots = 0
can2ballots = 0
can3ballots = 0

candidate = ['Candidate',3]
candidate1 = "Charles Casper Stockham"
candidate2 = "Diana DeGette"
candidate3 = "Raymon Anthony Doane"
county = ['', 0]

#Obtain Ballot total and Candidate totals
for row in data:
    ballots += 1
    
    if row["Candidate"] == candidate1:
      can1ballots += 1
       
    if row["Candidate"] == candidate2:
      can2ballots += 1
    
    if row["Candidate"] == candidate3:
      can3ballots += 1

#Determine winner
results = {can1ballots : candidate1, can2ballots : candidate2, can3ballots : candidate3}
winner = max(can1ballots, can2ballots, can3ballots)

elected = results[winner]


#Prepare Output
output = f'''
    Election Results
    -------------------------
    Total Votes: {ballots}
    -------------------------
    Charles Casper Stockham: {(can1ballots / ballots):.3%} ({can1ballots})
    Diana DeGette: {(can2ballots / ballots):.3%} ({can2ballots})
    Raymon Anthony Doane: {(can3ballots / ballots):.3%} ({can3ballots})
    -------------------------
    Winner: {elected}
    -------------------------

'''

#Print and Create Output file
print(output)
my_report.write(output)



# Tutor Geronimo Perez helped with the f''' function. 
# Assistance in determining formatting percentages was found at: https://medium.com/bitgrit-data-science-publication/python-f-strings-tricks-you-should-know-7ce094a25d43#:~:text=Number%20formatting&text=Or%2C%20if%20you%20want%20f,the%20end%20of%20the%20string.
#Additional help https://www.geeksforgeeks.org/python-maximum-minimum-set/

