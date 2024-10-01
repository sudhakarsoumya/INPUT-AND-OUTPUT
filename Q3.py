...
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18
...

teams = []
for i in range(1, 3):
    print(f"Team {i}:")
    a = input("Team Name:\n")
    b = input("Score:\n")
    c = input("Overs played:\n")
    team_details = {
        "name": a,
        "score": b,
        "overs": c
    }
    teams.append(team_details)
print("\nMatch Details:")
for i in range(2):
    print(f"Team {i + 1}:")
    print(f"Name: {teams[i]['name']}")
    print(f"Score: {teams[i]['score']}")
    print(f"Overs played: {teams[i]['overs']}")
