from odoo import models, fields, api


# Modèle permettant la création d'immeubles
class Immeuble(models.Model):
    _name = "rentalizi.immeuble"
    _description = "Ajout des immeubles pour gestion dans notre application"
    _rec_name = "nom"

    nom = fields.Char(string="Identifiant", required=True)
    adresse_id = fields.Many2one("rentalizi.adresse", string="Adresse")
    superficie = fields.Integer(string="Superficie(m²)")
    annee_construction = fields.Date(string="Année de construction")
    complements = fields.Many2many("rentalizi.complements", string="Parties et équipements")
    devise_id = fields.Many2one("res.currency", default=lambda self: self.env.ref('base.main_company').currency_id)
    taxe_fonciere = fields.Monetary(string="Taxe foncière", currency_field="devise_id")
    prix_acquisition = fields.Monetary(string="Prix d'acquisition", currency_field="devise_id")
    frais_acquisition = fields.Monetary(string="Frais d'acquisition", currency_field="devise_id")
    date_acquisition = fields.Date(string="Date d'acquisition")
    description = fields.Text(string="Description")
    notes = fields.Text(string="Notes")
    lot_ids = fields.One2many("rentalizi.lot", "nom", string="Lots")
    ville_id = fields.Many2one("rentalizi.ville", related="adresse_id.ville_id")
    code_postal = fields.Char(related="adresse_id.code_postal")
