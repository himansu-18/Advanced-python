import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("IPL 2026 Team Information")
root.geometry("650x500")

# IPL Teams Data
teams = {

"CSK":{
"color":"#f7d417",
"Batsmen":["Ruturaj Gaikwad","Devon Conway","Ajinkya Rahane"],
"Bowlers":["Deepak Chahar","Maheesh Theekshana","Tushar Deshpande"],
"Allrounders":["Ravindra Jadeja","Moeen Ali","Shivam Dube"],
"Wicketkeepers":["MS Dhoni"]
},

"MI":{
"color":"#005da0",
"Batsmen":["Rohit Sharma","Suryakumar Yadav","Tilak Varma"],
"Bowlers":["Jasprit Bumrah","Piyush Chawla"],
"Allrounders":["Hardik Pandya","Romario Shepherd"],
"Wicketkeepers":["Ishan Kishan"]
},

"RCB":{
"color":"#d71920",
"Batsmen":["Virat Kohli","Faf du Plessis","Rajat Patidar"],
"Bowlers":["Mohammed Siraj","Reece Topley"],
"Allrounders":["Glenn Maxwell","Cameron Green"],
"Wicketkeepers":["Dinesh Karthik"]
},

"KKR":{
"color":"#3a225d",
"Batsmen":["Shreyas Iyer","Rinku Singh","Nitish Rana"],
"Bowlers":["Mitchell Starc","Varun Chakravarthy"],
"Allrounders":["Andre Russell","Sunil Narine"],
"Wicketkeepers":["Rahmanullah Gurbaz"]
},

"DC":{
"color":"#17479e",
"Batsmen":["David Warner","Prithvi Shaw"],
"Bowlers":["Anrich Nortje","Kuldeep Yadav"],
"Allrounders":["Axar Patel","Mitchell Marsh"],
"Wicketkeepers":["Rishabh Pant"]
},

"RR":{
"color":"#ff69b4",
"Batsmen":["Jos Buttler","Yashasvi Jaiswal"],
"Bowlers":["Trent Boult","Yuzvendra Chahal"],
"Allrounders":["Riyan Parag","Ravichandran Ashwin"],
"Wicketkeepers":["Sanju Samson"]
},

"SRH":{
"color":"#ff822a",
"Batsmen":["Rahul Tripathi","Aiden Markram"],
"Bowlers":["Bhuvneshwar Kumar","T Natarajan"],
"Allrounders":["Washington Sundar","Marco Jansen"],
"Wicketkeepers":["Heinrich Klaasen"]
},

"PBKS":{
"color":"#ed1b24",
"Batsmen":["Shikhar Dhawan","Jonny Bairstow"],
"Bowlers":["Arshdeep Singh","Kagiso Rabada"],
"Allrounders":["Sam Curran","Liam Livingstone"],
"Wicketkeepers":["Jitesh Sharma"]
},

"LSG":{
"color":"#00aaff",
"Batsmen":["KL Rahul","Quinton de Kock"],
"Bowlers":["Ravi Bishnoi","Mark Wood"],
"Allrounders":["Marcus Stoinis","Krunal Pandya"],
"Wicketkeepers":["Nicholas Pooran"]
},

"GT":{
"color":"#1c1c1c",
"Batsmen":["Shubman Gill","Sai Sudharsan"],
"Bowlers":["Mohammed Shami","Rashid Khan"],
"Allrounders":["Rahul Tewatia","Vijay Shankar"],
"Wicketkeepers":["Wriddhiman Saha"]
}

}

team_var = tk.StringVar()

# Dropdown
dropdown = ttk.Combobox(root,textvariable=team_var)
dropdown['values'] = list(teams.keys())
dropdown.pack(pady=10)

# Text area
text = tk.Text(root,height=22,width=70)
text.pack(pady=10)

def show_team():

    team = team_var.get()

    if team not in teams:
        return

    data = teams[team]

    # Change theme color
    root.configure(bg=data["color"])

    text.delete(1.0,tk.END)

    text.insert(tk.END,f"\nTEAM : {team}\n\n")

    for category in ["Batsmen","Bowlers","Allrounders","Wicketkeepers"]:
        text.insert(tk.END,category + ":\n")

        for player in data[category]:
            text.insert(tk.END,"  - " + player + "\n")

        text.insert(tk.END,"\n")

button = tk.Button(root,text="Show Team Info",command=show_team)
button.pack()

root.mainloop()