# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#Xabier Carnero

from odoo import models,fields,api
from odoo.exceptions import ValidationError
class Employee (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo,
#anadiremos atributos extra que necesitamos para nuestro modulo
    _name = "emex51_module.employee"
    _inherit = 'res.users'
    # Declaracion de los atributos de tipo basico de en Odoo.
    wage = fields.Float(string = "Salario")
    jobPosition = fields.Char(string = "Puesto de trabajo")
    #Declaracion de los atributos relacionales con otras clases.
    #Un empleado gestiona a varios visitantes
    visitors = fields.One2many('emex51_module.visitor','employee',string="Visitantes")
    #Un empleado tiene un jefe un jefe gestiona varios empleados
    boss = fields.Many2one('emex51_module.boss',ondelete ='set null',string="Jefe")
    #Un empleado gestiona varios sectores, un sector en gestionado por varios empleados,
# NM con atributos clase intermedia dos 1N
    sectors = fields.One2many('emex51_module.sectoremployees','employees',string="Sectores")

    @api.constrains('wage')
    def _check_wage(self):
        for employee in self:
            if employee.wage < 0:
                raise ValidationError("Enter positive value.")
            elif employee.wage > 999999999999:
                raise ValidationError("Enter lower value.")

    @api.constrains('name')
    def _check_name(self):
        for employee in self:
            if employee.name.isalpha() is False:
                raise ValidationError("Nombre must be a name.")

    @api.constrains('login')
    def _check_login(self):
        for employee in self:
            if len(employee.login) > 20:
                raise ValidationError("Login must have less caracters.")
            elif len(employee.login) < 4:
                raise ValidationError("Login must have more caracters.")