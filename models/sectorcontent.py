# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class SectorContent (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.sectorcontent'
    #El atributo string es como se ve en el form de la view de odoo.
#id lo crea odoo. Es un field reserved.
    name = fields.Char(required = True, string = "Nombre")
    arrivalDate = fields.Date(string ="Fecha de llegada")
    #Declaracion de los atributos relacionales con otras clases.
    #En un sector hay varias existencias y una existencia esta en un sector. Estas pueden ser
# armas o criaturas
    sector = fields.Many2one ('emex51_module.sector',ondelete = 'cascade', string = "Sector")
