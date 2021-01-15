# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
class Visitor (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo,
#anadiremos atributos extra que necesitamos para nuestro modulo
    _name = "emex51_module.visitor"
    _inherit = 'res.users'
    # Declaracion de los atributos de tipo basico de en Odoo.
    #La clase res.users ya contiene name, email, password, login, login_date (lastConnection)
    dni = fields.Char(string = "DNI")
    requestedVisitDate = fields.Date(string = "Fecha peticion visita")
    visitReply = fields.Boolean(string = "Respuesta a peticion")
    visited = fields.Boolean(string = "Visitado")
    visitDate = fields.Date(string = "Fecha visita")
    #Declaracion de los atributos relacionales con otras clase
    #Los visitantes son gestionados por un empleado
    employee = fields.Many2one('emex51_module.employee',ondelete ='set null',string="Empleado")
    #Un visitante visita varios sectores, un sector es visitado por varios  visitantes
    visitedSectors = fields.Many2many('emex51_module.sector',string="Sectores visitados")

    @api.constrains('dni')
    def dni(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = dni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni)%23] == dig_control
        return False