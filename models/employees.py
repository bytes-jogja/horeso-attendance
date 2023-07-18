from odoo import api, fields, models 

class HoresoEmployees(models.Model):
    _name = 'horeso.employees'
    _description = 'Horeso Employees'
    _rec_name = 'name'
    
    name = fields.Char(string='Full Name')
    ref = fields.Char(string='Reference')
    team = fields.Selection([
        ('jogja', 'Tim Jogja'),
        ('pusat', 'Tim Pusat'),
    ], string='Tim')
    active = fields.Boolean(string='Active', default=True)