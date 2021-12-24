from tkinter import *
from tkmacosx import *

from main import Exam, Final
from main import get_targ_score

subj_list = ["english", "math", "mt", "history", "literature", "geography", "physics", "biology", "chemistry"]
subs = {}
for s in subj_list:
    subs[s] = {"wa1":Exam(s, "wa1"), 
                "wa2": Exam(s, "wa2"), 
                "wa3": Exam(s, "wa3"), 
                "eoy": Final(s, "eoy")}

root = Tk()

subject = {
    "wa1": [0,0,0,3],
    "wa2": [0,0,0,4],
    "wa3": [0,0,0,5],
    "eoy": [0,0,0,6]
}


for exam, var_list in subject.items():
    subject[exam][0]= StringVar()
    subject[exam][1]= StringVar()
    subject[exam][2]= StringVar()

my_list = [0]
my_list[0] = StringVar()


root.title("ri-score-utility")
root.geometry("500x500")




def stat_entry(subj_name):

    root.title(f"ri-score-utility {subj_name}")

    print(get_targ_score(subs[subj_name]))

    Label(root, text="Weightage").grid(row=2, column=2)
    Label(root, text="Score_attained").grid(row=2, column=3)
    Label(root, text="Score_max").grid(row=2, column=4)

    identifier = "wa1"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: subs[subj_name]["wa1"].update_info(float(subject["wa1"][0].get()), float(subject["wa1"][1].get()), float(subject["wa1"][2].get()))).grid(row=subject[identifier][-1], column=5)

    identifier = "wa2"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: subs[subj_name]["wa2"].update_info(float(subject["wa2"][0].get()), float(subject["wa2"][1].get()), float(subject["wa2"][2].get()))).grid(row=subject[identifier][-1], column=5)

    identifier = "wa3"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: subs[subj_name]["wa3"].update_info(float(subject["wa3"][0].get()), float(subject["wa3"][1].get()), float(subject["wa3"][2].get()))).grid(row=subject[identifier][-1], column=5)

    identifier = "eoy"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: subs[subj_name]["eoy"].update_info(float(subject["eoy"][0].get()), float(subject["eoy"][1].get()), float(subject["eoy"][2].get()))).grid(row=subject[identifier][-1], column=5)

    Label(root, text="").grid(row=7, column=1)

    def target(subj_name):
        reverse = {v: k for k, v in get_targ_score(subs[subj_name]).items()}
        
        value = reverse[float(value_inside.get())]
        my_label.config(text=str(value))
    

    options_list = []
    for cutoff, gpa in subs[subj_name]["wa1"].gpa_dict.items():
        options_list.append(str(gpa))

    value_inside = StringVar()
    value_inside.set("Select an option")

    thingy = OptionMenu(root, value_inside, *options_list)
    thingy.grid(row=8, column=1)
    my_label = Label(root, text="")
    my_label.grid(row=8, column=3)
    Button(root, text="get_eoy_score_target", command=lambda: target(subj_name)).grid(row=8, column=2)

    

def switcheroo(subject):

    # Reset main window
    for l in root.grid_slaves():
        l.grid_forget()
    
    # Creae option menu
    subj_option = StringVar()
    subj_option.set("Select an option")
    subjthingy = OptionMenu(root, subj_option, *subj_list)
    subjthingy.grid(row=0, column=0)
    
    # Create button to confirm chosen subject
    Button(root, text="switch", command=lambda: stat_entry(subj_option.get())).grid(row=0, column=1)
    


subj_option = StringVar()
subj_option.set("Select an option")

subjthingy = OptionMenu(root, subj_option, *subj_list)
subjthingy.grid(row=0, column=0)
Button(root, text="switch", command=lambda: stat_entry(subj_option.get())).grid(row=0, column=1)



root.mainloop()

# a small change - for testing purposes