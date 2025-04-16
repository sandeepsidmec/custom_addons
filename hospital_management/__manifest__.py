{
    "name": "hospital management system",
    "author": "sandeep",
    "version": "18.0",
    "license": "LGPL-3",
    "depends": ["sale", "sale_management", "mail", ],
    "data":
        [
            "security/ir.model.access.csv",
            "views/view_patient.xml",
            "views/view_patient_lines.xml",
            "views/view_doctor.xml",
            "views/view_sale_order.xml",
            "data/patient_confirm_mail.xml",
            "wizard/patient_wizard_invoices.xml",
            "report/report_patient_template.xml",
            "report/report.xml",
            "views/menu.xml", ],
}
