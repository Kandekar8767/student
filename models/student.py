from odoo import models, fields

class Student(models.Model):
    _name = "student.record"
    _description = "Student Record"

    name = fields.Char(string="Student Name", required=True)
    roll_no = fields.Integer(string="Roll Number")
    division = fields.Selection(
        [('A', 'A'), ('B', 'B'), ('C', 'C')],
        string="Division"
    )
    standard = fields.Char(string="Standard")
    age = fields.Integer(string="Age")
    remarks = fields.Text(string="Remarks")
