import pandas as pd
import unicodedata

class Teste:
	problemAmount = 0
	studentAmount = 0
	studentsGrades = {}
	dataFrame = 0
	excelFile = 0

	def parseQuantities(self):
		Teste.studentAmount, Teste.problemAmount = Teste.dataFrame.shape

		Teste.problemAmount -= 3

	def showResults(self):
		print '------------------------'

		for student, grade in Teste.studentsGrades.items():
			print '--- Student:', student + ' - Grade:', grade

		print '-----------------------\n'

		print '(Total students:', str(Teste.studentAmount) + ')\n', '(Total problems:', str(Teste.problemAmount) + ')'

	def __init__(self, currentExcel, chosenTest):
		Teste.excelFile = currentExcel

		Teste.dataFrame = Teste.excelFile.parse(chosenTest)

		Teste.parseQuantities(self)
		
		for row in range(0, Teste.studentAmount):
			currentStudent = Teste.dataFrame.iloc[row][0]

			grade = Teste.dataFrame.iloc[row][Teste.problemAmount + 1]

			# currentStudent = unicode(currentStudent, "utf-8")

			gradePercentage = float((grade * 100.0) / Teste.problemAmount)

			Teste.studentsGrades[currentStudent] = gradePercentage

		Teste.showResults(self)

def getTest():
	print 'Which test do you want to filter?\n', '(input format: Teste x)'

	chosenTest = raw_input()

	return chosenTest

def main():
	file = 'huxley-group-export.xls'

	exc = pd.ExcelFile(file)

	test = getTest()

	testResults = {}

	for x in exc.sheet_names:
		if(x == test):
			testResults = Teste(exc, x).studentsGrades
			break

	return

if __name__ == "__main__":
	main()