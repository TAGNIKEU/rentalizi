from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Ville(models.Model):
    _name = 'rentalizi.ville'
    _description = "Ville d'appartenance d'un immeuble. Permet de créer les villes auxquelles apprtient les immeubles"
    _rec_name = 'nom'

    nom = fields.Char(string='Nom')

# Contrainte permettant de définir les noms de villes uniques pour éviter les doublons. La casse est prise en compte
    @api.constrains('nom')
    def _check_name_unique(self):
        for rec in self:
            noms = self.search([('nom', '=ilike', rec.nom), ('id', '!=', rec.id)])
            if noms:
                raise ValidationError('Le nom de ville doit être unique!!')



