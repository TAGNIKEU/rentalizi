from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Ville(models.Model):
    _name = 'rentalizi.ville'
    _description = "ville d'appartenance d'un immeuble"
    _rec_name = 'nom'

    nom = fields.Char(string='Nom')

    @api.constrains('nom')
    def _check_name_unique(self):
        noms = self.search([])
        for rec in noms:
            if self.nom.lower() == rec.nom.lower():
                raise ValidationError('Le nom de ville doit être unique!!')



