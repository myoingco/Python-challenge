# Create a script that contains the following:
print("Election Results")
print("-------------------------")

import csv

electiondata = "/Users/meichelyoingco/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

with open(electiondata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    fields = next(csvfile)

    ballot_id = []
    county = []
    candidate = []
    #candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

    for rows in csvreader:
        ballot_id.append(rows[0])
        county.append(rows[1])
        candidate.append(rows[2])

# The total number of votes cast
    total_votes = len(ballot_id)
    print(f"Total Votes: {total_votes}")

print("-------------------------")

# A complete list of candidates who received votes & the total number of votes each candidate won

candidate_1 = (candidate.count("Charles Casper Stockham"))
candidatename_1 = "Charles Casper Stockham"

candidate_2 = (candidate.count("Diana DeGette"))
candidatename_2 = "Diana DeGette"

candidate_3 = (candidate.count("Raymon Anthony Doane"))
candidatename_3 = "Raymon Anthony Doane"

# The percentage of votes each candidate won

p1 = ((candidate_1/total_votes) * 100)
round_p1 = round(p1, 3)

p2 = ((candidate_2/total_votes) * 100)
round_p2 = round(p2, 3)

p3 = ((candidate_3/total_votes) * 100)
round_p3 = round(p3, 3)


print(f"{candidatename_1}: {round_p1}% ({candidate_1})")
print(f"{candidatename_2}: {round_p2}% ({candidate_2})")
print(f"{candidatename_3}: {round_p3}% ({candidate_3})")


print("-------------------------")

# The winner of the election based on popular vote

c = 85213
d = 272892
r = 11606

winner = max(c,d,r)

if winner == d:
    print("Winner: Diana DeGette")
elif winner == c:
    print("Winner: Charles Casper Stockham")
elif winner == r:
    print("Winner: Raymon Anthony Doane")

print("-------------------------")

#export txt file

file = open("/Users/meichelyoingco/Desktop/python-challenge/PyPoll/analysis/PyPoll_Results.txt", "w")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write("----------------------------\n")
file.write(f"{candidatename_1}: {round_p1}% ({candidate_1})\n")
file.write(f"{candidatename_2}: {round_p2}% ({candidate_2})\n")
file.write(f"{candidatename_3}: {round_p3}% ({candidate_3})\n")
file.write("----------------------------\n")
file.write("Winner: Diana DeGette\n")
file.write("----------------------------\n")