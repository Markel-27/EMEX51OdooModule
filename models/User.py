# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class User (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo, a�adiremos atributos extra que necesitamos para nuestro m�dulo
    _name = "res.users"
    _inherit = 'res.users'
    
    # Declaraci�n de los atributos de tipo b�sico de en Odoo.
     
    #La clase res.users ya contiene name, email, password, login, login_date (lastConnection)
    last_pawword_change = fields.Date()
    
    #Los dos siguientes campos son valores preestablecidos en un enum.
    privilege = fields.Selection(selection=[('user','admin'),])
    status = fields.Selection(selection=[('enabled','disabled'),])
    
    
    
    
    
