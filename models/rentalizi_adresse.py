from odoo import models, fields, api


class Adresse(models.Model):
    _name = "rentalizi.adresse"
    _description = "Adresse des immeubles, lots et locataires"
    _rec_name = "adresse"

    adresse = fields.Char(string="Adresse")
    adresse_2 = fields.Char(string="Adresse 2")
    ville_id = fields.Many2one("rentalizi.ville", string="Ville")
    code_postal = fields.Char(string="Code postal")
    region = fields.Char(string="Région")
    pays = fields.Many2one("res.country", string="Pays")

