# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Boss (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo, a�adiremos atributos extra que necesitamos para nuestro m�dulo
    _name = "emex51.boss"
    _inherit = 'res.users'
    
    # Declaraci�n de los atributos de tipo b�sico de en Odoo.
    wage = fields.Float(string = "Salario")
    
    #Declaraci�n de los atributos relacionales con otras clases.
    
    #Un jefe gestiona varios empleados.
    empleados = fields.One2many ('emex51.employee','jefe', string = "Empleados")