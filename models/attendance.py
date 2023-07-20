from odoo import api, fields, models
from datetime import datetime

class HoresoAttendance(models.Model):
    _name = 'horeso.attendance'
    _description = 'Horeso Attendance'
    _rec_name = 'employee_id'
    
    employee_id = fields.Many2one(comodel_name='horeso.employees', string='Employee')
    check_in_time = fields.Datetime(string='Check In Time', default=fields.Datetime.now)
    check_out_time = fields.Datetime(string='Check Out Time', default=fields.Datetime.now)
    ho_field = fields.Html(string='Houkoku/Report')
    ren_field = fields.Html(string='Renraku/Communication')
    so_field = fields.Html(string='Soudan/Discussion')
    
    @api.depends('check_in_time')
    def _compute_age(self):
        for rec in self:
            rec.check_in_time = datetime.now()

    @api.depends('check_out_time')
    def _compute_age(self):
        for rec in self:
            rec.check_out_time = datetime.now()
            