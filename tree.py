from decision import DecisionQuery, DecisionResult
class HeartAttackTree:
    def __init__(self):
        self.pass_exam = DecisionQuery(
            "PassExam",
            DecisionResult("Exam"),
            DecisionResult("Automatic 3"),
            self.get_pass_exam
        )

        self.activities = DecisionQuery(
            "Activities",
            DecisionResult("Automatic 5"),
            self.pass_exam,
            self.get_activities
        )

        self.theories = DecisionQuery(
            "Theories",
            self.activities,
            DecisionResult("Exam"),
            self.get_theories
        )

        self.practice = DecisionQuery(
            "Practice",
            self.theories,
            DecisionResult("Repeat"),
            self.get_practice
        )