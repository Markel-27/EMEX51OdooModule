# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Creature (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.creature'
    _inherit = 'emex51_module.sectorcontent'
    # Declaracion de los atributos de tipo basico de en Odoo. id lo crea odoo. 
    #Es un field reserved.
    species = fields.Char(required = True, string = "Especie")
