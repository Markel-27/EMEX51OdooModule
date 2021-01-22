# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
from odoo.exceptions import ValidationError
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Army (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.army'
    _inherit = 'emex51_module.sectorcontent'    
    # Declaracion de los atributos de tipo basico de en Odoo.
    #El atributo string es como se ve en el form de la view de odoo. id lo crea odoo. Es un field reserved.
    ammunition = fields.Integer(required = True, string = "Municion Total")
    sector = fields.Many2one ('emex51_module.sector', ondelete = 'cascade', string = "Sector", domain=[('tipo','=','army')])
    
    @api.constrains('ammunition')
    def _check_ammunition(self):
        for army in self: 
            if army.ammunition <0:
                raise ValidationError("Enter positive value.")
            elif army.ammunition>99999:
                raise ValidationError("Enter lower value")