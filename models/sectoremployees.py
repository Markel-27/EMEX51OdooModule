# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
#Esta clase es la tabla que se crea por la relacion muchos a muchos entre empleado y sector con e
#l atributo fecha.
class SectorEmployees (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.sectoremployees'
    # Declaracion de los atributos de tipo basico de en Odoo.
    #El atributo string es como se ve en el form de la view de odoo. id lo crea odoo. Es un
# field reserved.
    workDate = fields.Date(string ="Fecha de trabajo")
    #Declaracion de los atributos relacionales con otras clases.
    employees = fields.Many2one('emex51_module.employee',ondelete ='set null',string="Empleados")
    sectors = fields.Many2one('emex51_module.sector',ondelete ='set null',string="Sectores")
