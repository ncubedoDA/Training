
from odoo import fields, models, api

class AdvancedCourseWizard(models.TransientModel):
    _name = 'advanced.course.wizard'
    _description = 'Advanced Course Wizard'


    teacher_id = fields.Many2one('res.partner',string='Teacher')

    def create_course(self):
        print("hola")