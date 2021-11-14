from odoo import models, fields, api


class Lot(models.Model):
    _name = 'rentalizi.lot'
    _description = 'Lots de différents types contenus dans un immeuble'

    nom = fields.Char(string='Nom du lot')
    type = fields.Selection([('appartement', 'Appartement'), ('chambre', 'Chambre'), ('studio', 'Studio'),
                             ('bureau', 'Bureau'), ('boutique', 'Boutique')])
    superficie = fields.Integer(string='Superficie(m²)')
    nbre_pièces = fields.Integer(string='Nombre de pièces')
    nbre_chambres = fields.Integer(string='Nombre de chambres')
    salles_bain = fields.Integer(string='Salles de bain')
    description = fields.Text(string='Description')
