# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
class Employee (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo, a�adiremos atributos extra que necesitamos para nuestro m�dulo
    _name = "emex51.employee"
    _inherit = 'res.users'
    
    # Declaraci�n de los atributos de tipo b�sico de en Odoo.
    wage = fields.Float(string = "Salario")
    jobPosition = field.Char(string = "Puesto de trabajo")
    
    #Declaraci�n de los atributos relacionales con otras clases.

    #Un empleado gestiona a varios visitantes
    visitantes = fields.One2many('emex51.visitor','employee',string="Visitantes")
    #Un empleado tiene un jefe un jefe gestiona varios empleados
    jefe = fields.Many2one('emex51.boss',ondelete ='set null',string="Jefe")
    #Un empleado gestiona varios sectores, un sector en gestionado por varios empleados
    sectores = fields.One2many('emex51.sectoremployees','empleados',string="Sectores")
    