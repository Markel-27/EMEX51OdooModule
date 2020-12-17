# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
class Visitor (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo,
#anadiremos atributos extra que necesitamos para nuestro modulo
    _name = "emex51_module.visitor"
    _inherit = 'res.users'
    # Declaracion de los atributos de tipo basico de en Odoo.
    #La clase res.users ya contiene name, email, password, login, login_date (lastConnection)
    dni = fields.Char(string = "DNI")
    requesteVisitDate = fields.Date(string = "Fecha peticion visita")
    visitReply = fields.Boolean(string = "Respuesta a peticion")
    visited = fields.Boolean(string = "Visitado")
    visitDate = fields.Date(string = "Fecha visita")
    #Declaracion de los atributos relacionales con otras clase
    #Los visitantes son gestionados por un empleado
    employee = fields.Many2one('emex51_module.employee',ondelete ='set null',string="Empleado")
    #Un visitante visita varios sectores, un sector es visitado por varios  visitantes
    visitedSectors = fields.Many2many('emex51_module.sector',string="Sectores visitados")
