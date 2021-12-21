from tkinter import *
from tkmacosx import *

from main import Subject

math = Subject("math")
root = Tk()

subject = {
    "wa1": [0,0,0,1],
    "wa2": [0,0,0,2],
    "wa3": [0,0,0,3],
    "eoy": [0,0,0,4]
}


for exam, var_list in subject.items():
    subject[exam][0]= StringVar()
    subject[exam][1]= StringVar()
    subject[exam][2]= StringVar()

my_list = [0]
my_list[0] = StringVar()


root.title("ri-score-utility")
root.geometry("500x500")




def stat_entry():

    Label(root, text="Weightage").grid(row=0, column=2)
    Label(root, text="Score_attained").grid(row=0, column=3)
    Label(root, text="Score_max").grid(row=0, column=4)

    identifier = "wa1"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: math.wa1.update_info(float(subject["wa1"][0].get()), float(subject["wa1"][1].get()), float(subject["wa1"][2].get()))).grid(row=subject[identifier][-1], column=5)

    identifier = "wa2"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: math.wa2.update_info(float(subject["wa2"][0].get()), float(subject["wa2"][1].get()), float(subject["wa2"][2].get()))).grid(row=subject[identifier][-1], column=5)

    identifier = "wa3"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: math.wa3.update_info(float(subject["wa3"][0].get()), float(subject["wa3"][1].get()), float(subject["wa3"][2].get()))).grid(row=subject[identifier][-1], column=5)

    identifier = "eoy"
    Label(root, text=identifier).grid(row=subject[identifier][-1], column=1)
    Entry(root, textvariable=subject[identifier][0], width=8).grid(row=subject[identifier][-1], column=2)
    Entry(root, textvariable=subject[identifier][1], width=8).grid(row=subject[identifier][-1], column=3)
    Entry(root, textvariable=subject[identifier][2], width=8).grid(row=subject[identifier][-1], column=4)
    Button(root, text="save", command=lambda: math.eoy.update_info(float(subject["eoy"][0].get()), float(subject["eoy"][1].get()), float(subject["eoy"][2].get()))).grid(row=subject[identifier][-1], column=5)

    Label(root, text="").grid(row=5, column=1)

    def target():
        reverse = {v: k for k, v in math.get_eoy_score_target().items()}
        
        value = reverse[float(value_inside.get())]
        my_label.config(text=str(value))
    

    options_list = []
    for cutoff, gpa in math.gpa_dict.items():
        options_list.append(str(gpa))

    value_inside = StringVar()
    value_inside.set("Select an option")

    thingy = OptionMenu(root, value_inside, *options_list)
    thingy.grid(row=6, column=1)
    my_label = Label(root, text="")
    my_label.grid(row=6, column=3)
    Button(root, text="get_eoy_score_target", command=lambda: target()).grid(row=6, column=2)

    


stat_entry()

root.mainloop()

# a small change - for testing purposes