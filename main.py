import math as m

import database


class Exam():
    def __init__(self, subj_name, exam_name):
        self.subj_name = database.initialize_table(subj_name)
        self.exam_name = exam_name
        self.weightage = database.get_stored_values(subj_name)[list([database.get_stored_values(subj_name)[0][0],
                                database.get_stored_values(subj_name)[1][0],
                                database.get_stored_values(subj_name)[2][0],
                                database.get_stored_values(subj_name)[3][0]]).index(exam_name)][1]
        self.score_attained = database.get_stored_values(subj_name)[list([database.get_stored_values(subj_name)[0][0],
                                database.get_stored_values(subj_name)[1][0],
                                database.get_stored_values(subj_name)[2][0],
                                database.get_stored_values(subj_name)[3][0]]).index(exam_name)][2]
        self.score_max = database.get_stored_values(subj_name)[list([database.get_stored_values(subj_name)[0][0],
                                database.get_stored_values(subj_name)[1][0],
                                database.get_stored_values(subj_name)[2][0],
                                database.get_stored_values(subj_name)[3][0]]).index(exam_name)][3]
        self.gpa_dict = {
            80: 4.0,
            70: 3.6,
            65: 3.2,
            60: 2.8,
            55: 2.4,
            50: 2.0}


    def get_info(self):
        return f"Weightage: {self.weightage}%, Attained: {self.score_attained}, Max: {self.score_max}"

    def update_info(self, weightage, score_attained, score_max):
        if weightage > 0 and weightage < 100:
            self.weightage = float(weightage)
        else:
            return "Weightage must be between 0 and 100"

        if score_attained >= 0 and score_max > 0 and score_attained <= score_max:
            self.score_attained = score_attained
            self.score_max = score_max

        database.update_values(self.subj_name, self.exam_name, weightage, score_attained, score_max)
        return f"Weightage: {weightage}%, Attained: {score_attained}, Max: {score_max}"

    def get_exam_percentage(self):
        return (self.score_attained/self.score_max) * 100

    def get_exam_gpa(self):
        percentage = (self.score_attained/self.score_max) * 100
        for cutoff, gpa in self.gpa_dict.items():
            if percentage >= cutoff:
                return gpa

    def get_score_target(self):
        target_dict = {}
        for cutoff in self.gpa_dict:
            target_dict[m.ceil((self.score_max*cutoff)/100)] = self.gpa_dict[cutoff]
        return target_dict

    def get_obj_type(self):
        return type(self).__name__


class Final(Exam):
    pass

    def update_info(self, weightage, score_attained, score_max):
        if weightage > 0 and weightage < 100:
            self.weightage = float(weightage)
        else:
            return "Weightage must be between 0 and 100"


        if score_max > 0 and score_attained <= score_max:
            self.score_max = float(score_max)
            self.score_attained = float(score_attained)

        database.update_values(self.subj_name, self.exam_name, weightage, score_attained, score_max)
        return f"Weightage: {weightage}%, Attained: {score_attained}, Max: {score_max}"

class Subject():
    def __init__(self, name):
        self.name = database.initialize_table(name)
        self.wa1 = Exam(database.initialize_table(name), 'wa1')
        self.wa2 = Exam(database.initialize_table(name), 'wa2')
        self.wa3 = Exam(database.initialize_table(name), 'wa3')
        self.eoy = Final(database.initialize_table(name), 'eoy')
        self.gpa_dict = {
            80: 4.0,
            70: 3.6,
            65: 3.2,
            60: 2.8,
            55: 2.4,
            50: 2.0}


    def get_eoy_score_target(self):
        secured_percentage_points = self.wa1.weightage*(self.wa1.score_attained/self.wa1.score_max) + \
            self.wa2.weightage*(self.wa2.score_attained/self.wa2.score_max) + \
            self.wa3.weightage*(self.wa3.score_attained/self.wa3.score_max)

        target_dict = {}
        for cutoff in self.gpa_dict:
            try:
                target = ((float(cutoff)-secured_percentage_points)/self.eoy.weightage)*self.eoy.score_max
                target_dict[m.ceil(target)] = self.gpa_dict[cutoff]
            except:
                return "Check value type"

        return target_dict

    def get_overall_gpa(self):
        percentage = self.wa1.weightage*(self.wa1.score_attained/self.wa1.score_max) + \
            self.wa2.weightage*(self.wa2.score_attained/self.wa2.score_max) + \
            self.wa3.weightage*(self.wa3.score_attained/self.wa3.score_max) + \
            self.eoy.weightage*(self.eoy.score_attained/self.eoy.score_max)

        print(percentage)
        for cutoff, gpa in self.gpa_dict.items():
            if percentage >= cutoff:
                return gpa

    def get_info(self):
        return database.get_stored_values(self.name)

subj_list = ["english", "math", "mt", "history", "literature", "geography", "physics", "biology", "chemistry"]
subs = {}
for s in subj_list:
    subs[s] = {"wa1":Exam(s, "wa1"), 
                "wa2": Exam(s, "wa2"), 
                "wa3": Exam(s, "wa3"), 
                "eoy": Final(s, "eoy")}


def get_subj_summary(subs_subject):
    print(subs_subject["wa1"].get_info())

def get_targ_score(subs_subject):
    secured_percentage_points = subs_subject["wa1"].weightage*(subs_subject["wa1"].score_attained/subs_subject["wa1"].score_max) + \
            subs_subject["wa2"].weightage*(subs_subject["wa2"].score_attained/subs_subject["wa2"].score_max) + \
            subs_subject["wa3"].weightage*(subs_subject["wa3"].score_attained/subs_subject["wa3"].score_max)

    target_dict = {}
    for cutoff in subs_subject["wa1"].gpa_dict:
            try:
                target = ((float(cutoff)-secured_percentage_points)/subs_subject["eoy"].weightage)*subs_subject["eoy"].score_max
                target_dict[m.ceil(target)] = subs_subject["wa1"].gpa_dict[cutoff]
            except:
                return "Check value type"

    return target_dict

tmp = "math"
print(get_targ_score(subs[tmp]))