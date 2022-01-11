from odoo import models, fields, api


class Assurance(models.Model):
    _name = "rentalizi.assurance"
    _description = "Asurance lié à la location"

    type_assurance = fields.Selection([('assurance_locataire', 'Assurance locataire'), ('assurance_loyer_impaye', 'Assurance loyer impayé')], string='Type', required=True)
    document = fields.Binary(string="Document")
    description = fields.Text(string="Description")
    date_etablissement = fields.Date(string="Date d'établissement")
    date_echeance = fields.Date(string="Date d'échéance")
    location_id = fields.Many2one("rentalizi.locations", string="Locations")
