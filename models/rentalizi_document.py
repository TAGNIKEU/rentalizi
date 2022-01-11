from odoo import models, fields, api


class Document(models.Model):
    _name = "rentalizi.document"
    _description = "Tout autre document lié à la location"

    type_document = fields.Selection([('appels_fonds', 'Appels de fonds'), ('assemlee_generale', 'Assemblée générale'), ('attestation_assurance', "Attestation d'assurance"), ('attestation_scolarite', 'Attestation de scolarité'), ('attestation_employeur', 'Attestation employeur'), ('bilan_annuel', 'Bilan annuel'), ('bulletin_salaire', 'Bulletin de salaire'), ('caution_solidaire', 'Caution solidaire'), ('certificat', 'Certificat'), ('contrat', 'Contrat'), ('contrat_abonnement', "Contrat d'abonnement"), ('contrat_assurance', "Contrat d'assurance"), ('contrat_entretien', "Contrat d'entretien"), ('contrat_location', 'Contrat de location'), ('contrat_travail', 'Contrat de travail'), ('contrat_technique', 'Contrat technique'), ('dernier_avis_imposition', "Dernier avis d'imposition")], string='Type document', required=True)
    fichier = fields.Binary(string="Fichier")
    description = fields.Text(string="Description")
    partage = fields.Boolean(string="Partager le document avec votre locataire")
    location_id = fields.Many2one("rentalizi.locations", string="Location")
