from odoo import models

class StudentXlsx(models.AbstractModel):
    _name = 'report.student_management.report_student_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, students):
            sheet = workbook.add_worksheet("Student card")
            format1 = workbook.add_format({'font_size': 8, 'align': "vcenter", 'bold': True})
            format2 = workbook.add_format({'font_size': 6, 'align': "vcenter"})

            row = 0
            for student in students:
                sheet.write(row + 0, 0, 'Student ID', format1)
                sheet.write(row + 0, 1, student.student_id.id or '', format2)

                sheet.write(row + 1, 0, 'Age', format1)
                sheet.write(row + 1, 1, student.age or '', format2)

                sheet.write(row + 2, 0, 'Allotment Date', format1)
                sheet.write(row + 2, 1, str(student.allotment_date) or '', format2)

                sheet.write(row + 3, 0, 'Joining Date', format1)
                sheet.write(row + 3, 1, str(student.joining_date) or '', format2)
