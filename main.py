import math as m

gpa_dict = {
    80: 4.0,
    70: 3.6,
    65: 3.2,
    60: 2.8,
    55: 2.4,
    50: 2.0
}


class Exam():
    def __init__(self):
        self.weightage = None
        self.score_attained = None
        self.score_max = None

    def update_info(self, weightage, score_attained, score_max):
        if weightage > 0 and weightage < 100:
            self.weightage = weightage
        else:
            return "Weightage must be between 0 and 100"
        if score_attained >= 0 and score_max > 0 and score_attained <= score_max:
            self.score_attained = score_attained
            self.score_max = score_max
        return f"Weightage: {weightage}%, Attained: {score_attained}, Max: {score_max}"

    def get_exam_percentage(self):
        return (self.score_attained/self.score_max) * 100

    def get_exam_gpa(self):
        percentage = (self.score_attained/self.score_max) * 100
        for cutoff, gpa in gpa_dict.items():
            if percentage >= cutoff:
                return gpa

    def get_score_target(self):
        target_dict = {}
        for cutoff in gpa_dict:
            target_dict[m.ceil((self.score_max*cutoff)/100)] = gpa_dict[cutoff]
        return target_dict


class Subject():
    def __init__(self):
        self.wa1 = Exam()
        self.wa2 = Exam()
        self.wa3 = Exam()
        self.eoy = Exam()

    def get_eoy_score_target(self):
        secured_percentage_points = self.wa1.weightage*(self.wa1.score_attained/self.wa1.score_max) + \
            self.wa2.weightage*(self.wa2.score_attained/self.wa2.score_max) + \
            self.wa3.weightage*(self.wa3.score_attained/self.wa3.score_max)

        target_dict = {}
        for cutoff in gpa_dict:
            try:
                target = ((float(cutoff)-secured_percentage_points)/self.eoy.weightage)*self.eoy.score_max
                target_dict[m.ceil(target)] = gpa_dict[cutoff]
            except:
                return "Check value type"

        return target_dict

    def get_overall_gpa(self):
        percentage = self.wa1.weightage*(self.wa1.score_attained/self.wa1.score_max) + \
            self.wa2.weightage*(self.wa2.score_attained/self.wa2.score_max) + \
            self.wa3.weightage*(self.wa3.score_attained/self.wa3.score_max) + \
            self.eoy.weightage*(self.eoy.score_attained/self.eoy.score_max)

        print(percentage)
        for cutoff, gpa in gpa_dict.items():
            if percentage >= cutoff:
                return gpa


math = Subject()
print(math.wa1.update_info(10,29,30))
