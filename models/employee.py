# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
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

