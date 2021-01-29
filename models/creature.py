# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
from odoo.exceptions import ValidationError
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Creature (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.creature'
    _inherit = 'emex51_module.sectorcontent'
    # Declaracion de los atributos de tipo basico de en Odoo. id lo crea odoo. 
    #Es un field reserved.
    species = fields.Char(required = True, string = "Especie")
    
    sector= fields.Many2one ('emex51_module.sector',ondelete = 'cascade', string = "Sector", domain =[('tipo','=','creature')])
            
    @api.constrains('species')
    def _check_species_length(self):
        for creature in self:
            if len(creature.species)<3:
                raise ValidationError('El nombre es muy corto, debe tener al menos 3 caracteres')
            elif len(creature.species)>20:
                raise ValidationError('El nombre es muy largo, debe tener menos de 20 caracteres')