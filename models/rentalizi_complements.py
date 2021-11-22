from odoo import models, fields, api


class Complements(models.Model):
    _name = 'rentalizi.complements'
    _description = 'Informations complémentaires sur les immeubles tels que gardien, garage, etc...'

    designation = fields.Char(string='Désignation des parties et équipements')
