# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#Endika Ubierna
from odoo import models,fields,api
from odoo.exceptions import ValidationError
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class SectorContent (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.sectorcontent'
    #El atributo string es como se ve en el form de la view de odoo.
#id lo crea odoo. Es un field reserved.
    name = fields.Char(required = True, string = "Nombre", size=25)
    arrivalDate = fields.Date(string ="Fecha de llegada")
    #Declaracion de los atributos relacionales con otras clases.
    #En un sector hay varias existencias y una existencia esta en un sector. Estas pueden ser
# armas o criaturas
    sector = fields.Many2one ('emex51_module.sector',ondelete = 'cascade', string = "Sector")
    
    @api.constrains('name')
    def _check_name_length(self):
        for sectorcontent in self:
            if len(sectorcontent.name)<3:
                raise ValidationError('El nombre es muy corto, debe tener al menos 3 caracteres')
            elif len(sectorcontent.name)>20:
                raise ValidationError('El nombre es muy largo, debe tener menos de 20 caracteres')