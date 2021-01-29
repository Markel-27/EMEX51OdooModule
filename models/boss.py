# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#Markel Lopez de Uralde

from odoo import models,fields,api
from odoo.exceptions import ValidationError
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Boss (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo,
#anadiremos atributos extra que necesitamos para nuestro modulo
    _name = 'emex51_module.boss'
    _inherit = 'res.users'
    # Declaracion de los atributos de tipo basico de en Odoo.
    wage = fields.Float(string = "Salario")
    #Declaracion de los atributos relacionales con otras clases.
    #Un jefe gestiona varios empleados.
    employees = fields.One2many ('emex51_module.employee','boss', string = "Empleados")
    
    @api.constrains('wage')
    def _check_wage(self):
        for boss in self:
            if boss.wage <0:
                raise ValidationError("Enter positive value.")
            elif boss.wage>99999:
                raise ValidationError("Enter lower value") 
    
    @api.constrains('email')
    def _check_email(self):
        for boss in self:
            if len(boss.email) <5:
                raise ValidationError("Enter longer value.")   
                
    #@api.onchange('email')
    #def _onchange_email(self):
    #    if len(self.email) < 5:
    #        return{
    #            'warning':{
    #                'title': "Incorrect email value",
    #                'message': "Introduce a valid email",
    #            },
    #    }
