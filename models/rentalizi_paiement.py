from odoo import models, fields, api


class Paiement(models.Model):
    _name = "rentalizi.paiement"
    _description = "Paiements additionnel ou autres paiements liés à une location donnée"

    montant = fields.Float(string="Montant")
    taxe = fields.Float(string="Taxe")
    type = fields.Selection([('charge', 'Charge'), ('loyer', 'Loyer')])
    description = fields.Text(string="Description")
    location_id = fields.Many2one("rentalizi.locations", string="Location")
