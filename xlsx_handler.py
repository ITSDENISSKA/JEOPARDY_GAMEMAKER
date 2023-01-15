import openpyxl


class Handler:
    def __init__(self, path):
        self.path = path

    def processing(self):
        try:
            questions_pack = []

            workbook = openpyxl.load_workbook(self.path)
            workbook.active = 0
            sheet = workbook.active

            for index in list(sheet.values)[1:]:
                questions_pack.append(list(index[1:]))

            workbook.active = 1
            sheet2 = workbook.active
            themes = list()
            answers = list(sheet2.values)[1:]

            for index in list(sheet2.values)[1:]:
                themes.append(index[0])

            for index in range(len(answers)):
                questions_pack[index] = list(zip(questions_pack[index], answers[index][1:]))

            return themes, questions_pack

        except Exception:
            return "Error"
