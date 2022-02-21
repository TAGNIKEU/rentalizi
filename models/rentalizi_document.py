from odoo import models, fields, api


class Document(models.Model):
    _name = "rentalizi.document"
    _description = "Tout autre document lié à la location"

    type_document = fields.Selection([('appels_fonds', 'Appels de fonds'), ('assemlee_generale', 'Assemblée générale'),
                                      ('attestation_assurance', "Attestation d'assurance"),
                                      ('attestation_scolarite', 'Attestation de scolarité'),
                                      ('attestation_employeur', 'Attestation employeur'),
                                      ('bilan_annuel', 'Bilan annuel'), ('bulletin_salaire', 'Bulletin de salaire'),
                                      ('caution_solidaire', 'Caution solidaire'), ('certificat', 'Certificat'),
                                      ('contrat', 'Contrat'), ('contrat_abonnement', "Contrat d'abonnement"),
                                      ('contrat_assurance', "Contrat d'assurance"),
                                      ('contrat_entretien', "Contrat d'entretien"),
                                      ('contrat_location', 'Contrat de location'),
                                      ('contrat_travail', 'Contrat de travail'),
                                      ('contrat_technique', 'Contrat technique'),
                                      ('dernier_avis_imposition', "Dernier avis d'imposition"),
                                      ('dernier_bulletin_pension', "Dernier bulletin de pension"), ('devis', "Devis"),
                                      ('diagnostic', "Diagnostic"), ('etat_des_lieux', "Etat des lieux"),
                                      ('facture', "Facture"), ('inventaire', "Inventaire"), ('kbis', "Kbis"),
                                      ('piece_identite', "Pièce d'identité"), ('quittance_loyer', "Quittance de loyer"),
                                      ('reglement_copropriete', "Règlement copropriété"),
                                      ('reglement_interieur', "Règlement intérieur"),
                                      ('releve_compte', "Relevé de compte"),
                                      ('releve_identite_bancaire', "Relevé d'identité bancaire"),
                                      ('revision_loyer', "Révision du loyer"),
                                      ('taxes_impots_locaux', "Taxes et impôts locaux"),
                                      ('titre_propriete', "Titre de propriété"), ('autres', "Autres")],
                                     string='Type document', required=True)
    fichier = fields.Binary(string="Fichier")
    description = fields.Text(string="Description")
    location_id = fields.Many2one("rentalizi.locations", string="Location")
    immeuble_id = fields.Many2one("rentalizi.immeuble", string="Immeuble")
