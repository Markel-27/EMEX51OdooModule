# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Sector (models.Model):
    #Esta es la referencia odoo. Como project.task. Task es una clase del modulo project.
    #Nuestro modulo en odoo es emex51.
    _name = 'emex51_module.sector'
    # Declaracion de los atributos de tipo basico de en Odoo.
    #El atributo string es como se ve en el form de la view de odoo.
#id lo crea odoo. Es un field reserved.
    name = fields.Char(required = True, string = "Nombre")
    tipo = fields.Selection(selection=[('creature','Creature'),('army','Army')])
    #Declaracion de los atributos relacionales con otras clases.
    #Un empleado gestiona varios sectores, un sector en gestionado por varios empleados.
# NM con atributos clase intermedia dos 1N
    employees = fields.One2many('emex51_module.sectoremployees','employee',string="Empleados")
    #Un visitante visita varios sectores, un sector es visitado por varios  visitantes
    visitors = fields.Many2many('emex51_module.visitor',string="Visitantes")
    #En un sector hay varias existencias y una existencia esta en un sector.
# Estas pueden ser armas o criaturas
    content = fields.One2many('emex51_module.sectorcontent','sector',string="Contenido")
