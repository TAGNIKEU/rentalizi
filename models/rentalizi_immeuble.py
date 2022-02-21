from odoo import models, fields, api


# Modèle permettant la création d'immeubles
class Immeuble(models.Model):
    _name = "rentalizi.immeuble"
    _description = "Ajout des immeubles pour gestion dans notre application"
    _rec_name = "nom"

    nom = fields.Char(string="Identifiant", required=True)
    adresse_id = fields.Many2one("rentalizi.adresse", string="Adresse")
    superficie = fields.Float(string="Superficie(m²)")
    annee_construction = fields.Date(string="Année de construction")
    complements = fields.Many2many("rentalizi.complements", string="Parties et équipements")
    taxe_fonciere = fields.Float(string="Taxe foncière")
    prix_acquisition = fields.Float(string="Prix d'acquisition")
    frais_acquisition = fields.Float(string="Frais d'acquisition")
    date_acquisition = fields.Date(string="Date d'acquisition")
    description = fields.Text(string="Description")
    notes = fields.Text(string="Notes")
    lot_ids = fields.One2many("rentalizi.lot", "immeuble_id", string="Lots")
    ville_id = fields.Many2one("rentalizi.ville", related="adresse_id.ville_id")
    code_postal = fields.Char(related="adresse_id.code_postal")
    document_ids = fields.One2many("rentalizi.document", "immeuble_id", string="Documents")
