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

