from xlrd import open_workbook
import xlwt
import xlrd

def main():
	LD = open_workbook('LD.xls')
	Test = open_workbook('Test.xls')

	Result = xlwt.Workbook(encoding="utf-8")
	Result_sheet1 = Result.add_sheet("Sheet1")

	LD_sheet = LD.sheet_by_index(0)
	Test_Sheet = Test.sheet_by_index(0)
	count = 0

	for LD_row in range(140):
		for Test_row in range(120):
			if LD_sheet.cell_value(LD_row,1) > Test_Sheet.cell_value(Test_row,1):
				if LD_sheet.cell_value(LD_row,1) < Test_Sheet.cell_value(Test_row,2):
					Result_sheet1.write(count,0,LD_sheet.cell_value(LD_row,0))
					Result_sheet1.write(count,1,Test_Sheet.cell_value(Test_row,0))
					Result_sheet1.write(count,2,Test_Sheet.cell_value(Test_row,3))
					Result_sheet1.write(count,3,Test_Sheet.cell_value(Test_row,4))
					count += 1

	Result.save("Result.xls")


