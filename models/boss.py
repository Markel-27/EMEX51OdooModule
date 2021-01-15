# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
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
    
    @api.constrains('salario')
    def _check_salario(self):
        for boss in self: 
            if boss.salario <0:
                raise ValidationError("Enter positive value.")
            elif boss.salario>99999:
                raise ValidationError("Enter lower value")            
            
    @api.constrains('login')
    def login(self):
        for boss in self: 
            if boss.login <0:
                raise ValidationError("Enter positive value.")
            elif boss.login>99999:
                raise ValidationError("Enter lower value")
                       
            
    @api.constrains('email')
    def email(self):
        for boss in self:         
            if not boss.email ('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$'):
                raise "Correo incorrecto"
        
