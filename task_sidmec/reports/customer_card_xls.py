from odoo import models

class CustomerXlsx(models.AbstractModel):
    _name = 'report.task_sidmec.report_customer_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, customers):
            sheet = workbook.add_worksheet("Customer card")
            format1 = workbook.add_format({'font_size': 8, 'align': "vcenter", 'bold': True})
            format2 = workbook.add_format({'font_size': 6, 'align': "vcenter"})

            row = 0
            for customer in customers:
                sheet.write(row + 0, 0, 'Customer ID', format1)
                sheet.write(row + 0, 1, customer.customer_id.id or '', format2)

                sheet.write(row + 1, 0, 'Age', format1)
                sheet.write(row + 1, 1, customer.age or '', format2)

                sheet.write(row + 2, 0, 'Email', format1)
                sheet.write(row + 2, 1, str(customer.email) or '', format2)
