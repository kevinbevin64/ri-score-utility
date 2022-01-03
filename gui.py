from tkinter import *
from tkmacosx import *

import math as m

from main import Exam


# Create Root window
root = Tk()
root.title("ri-score-utility")

# Create dictionary of subjects
subject_list = ["english", "math", "mt", "history", "literature", "geography", "physics", "biology", "chemistry"]
subject_dict = {}
for subject in subject_list:
    subject_dict[subject] = {"wa1":{"weightage":StringVar(), "score_attained":StringVar(), "score_max":StringVar()}, 
                "wa2": {"weightage":StringVar(), "score_attained":StringVar(), "score_max":StringVar()}, 
                "wa3": {"weightage":StringVar(), "score_attained":StringVar(), "score_max":StringVar()}, 
                "eoy": {"weightage":StringVar(), "score_attained":StringVar(), "score_max":StringVar()}}

    for exam in list(["wa1", "wa2", "wa3", "eoy"]):
        subject_dict[subject][exam]["weightage"].set(str(Exam(subject, exam).weightage))
        subject_dict[subject][exam]["score_attained"].set(str(Exam(subject, exam).score_attained))
        subject_dict[subject][exam]["score_max"].set(str(Exam(subject, exam).score_max))


def enter_scores(subject_name):
    r, c = 0, 0

    selected_subject = StringVar()
    selected_subject.set(subject_name)

    def switch_subject(subject_name):
        for widget in root.grid_slaves():
            widget.destroy()
        enter_scores(subject_name)

    OptionMenu(root, selected_subject, *subject_list).grid(row=r+1, column=c+1)
    Button(root, text="Switch", command=lambda: switch_subject(selected_subject.get())).grid(row=r+1, column=c+2)

    Label(root, text="Weightage / %").grid(row=r+2, column=c+2)
    Label(root, text="Score_attained").grid(row=r+2, column=c+3)
    Label(root, text="Score_max").grid(row=r+2, column=c+4)
    Label(root, text="Test_percentage").grid(row=r+2, column=c+5)
    Label(root, text="Test_gpa").grid(row=r+2, column=c+6)


    exams = ["wa1", "wa2", "wa3", "eoy"]
    for exam in exams:
        Label(root, text=exam).grid(row=r+3, column=c+1)
        Entry(root, width=8, textvariable=subject_dict[subject_name][exam]["weightage"]).grid(row=r+3, column=c+2)
        Entry(root, width=8, textvariable=subject_dict[subject_name][exam]["score_attained"]).grid(row=r+3, column=c+3)
        Entry(root, width=8, textvariable=subject_dict[subject_name][exam]["score_max"]).grid(row=r+3, column=c+4)
        r += 1
    
    r = 0

    # subject_info = {}
    # for exam in list(["wa1", "wa2", "wa3", "eoy"]):
    #     subject_info[exam] = 



    def save_values(subject_name):
        for exam in exams:
            Exam(subject_name, exam).update_info(float(subject_dict[subject_name][exam]["weightage"].get()),float(subject_dict[subject_name][exam]["score_attained"].get()),float(subject_dict[subject_name][exam]["score_max"].get()))
        
    Button(root, text="Save", command=lambda: save_values(subject_name)).grid(row=r+6, column=c+6)
    
    Label(root, text="").grid(row=r+7, column=c+1)

    def print_score_target(subject_name):
        try:
            points_claimed = Exam(subject_name, "wa1").weightage*(Exam(subject_name, "wa1").score_attained/Exam(subject_name, "wa1").score_max) + \
                    Exam(subject_name, "wa2").weightage*(Exam(subject_name, "wa2").score_attained/Exam(subject_name, "wa2").score_max) + \
                    Exam(subject_name, "wa3").weightage*(Exam(subject_name, "wa3").score_attained/Exam(subject_name, "wa3").score_max)
        except:
            print("Failed")

        target_dict = {}
        for cutoff in Exam(subject_name, "wa1").gpa_dict:
            try:
                target = ((float(cutoff)-points_claimed)/Exam(subject_name, "eoy").weightage)*Exam(subject_name, "eoy").score_max
                target_dict[m.ceil(target)] = Exam(subject_name, "wa1").gpa_dict[cutoff]
            except:
                print("filaed")

        reversed_target_dict = {v: k for k, v in target_dict.items()}
        
        value = reversed_target_dict[float(selected_gpa.get())]
        eoy_targ_result.config(text=str(value))
    
    gpa_list = []
    for cutoff, gpa in Exam(subject_name, "wa1").gpa_dict.items():
        gpa_list.append(str(gpa))
    selected_gpa = StringVar()
    selected_gpa.set(gpa_list[0])
    OptionMenu(root, selected_gpa, *gpa_list).grid(row=r+8, column=c+1)
    Button(root, text="get_eoy_score_target", command=lambda: print_score_target(subject_name)).grid(row=r+8, column=c+2)
    eoy_targ_result = Label(root, text="")
    eoy_targ_result.grid(row=r+8, column=c+3)

enter_scores(subject_list[0])

root.mainloop()
