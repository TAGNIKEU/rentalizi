from odoo import models, fields, api


class Immeuble(models.Model):
    _name = 'rentalizi.immeuble'
    _description = "Ajout des immeubles pour gestion dans notre application"

    nom = fields.Char(string='Identifiant', required=True)
    adresse = fields.Char(string='Adresse', required=True)
    pays_id = fields.Many2one('res.country', string='Pays', required=True)
    ville_id = fields.Many2one('rentalizi.ville', string='Ville')
    code_postal = fields.Char(string='Code postal')
    superficie = fields.Integer(string='Superficie(m²)')
    description = fields.Text(string='Description')
    notes = fields.Text(string='Notes')
