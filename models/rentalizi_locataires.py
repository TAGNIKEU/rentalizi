from odoo import models, fields, api


class Locataires(models.Model):
    _name = "rentalizi.locataires"
    _description = "Locataires des biens"

    type_locataire = fields.Selection([('particulier', 'Particulier'), ('societe', 'Société/Autre')],
                                      string="Type de locataire", default="particulier")

    # Informations personnelles dans le cas d'un particulier - informations sur un particulier
    civilite_locataire = fields.Selection([('m', 'M.'), ('mme', 'Mme'), ('mlle', 'Mlle'), ('m_mme', 'M. et Mme')],
                                          string="Civilité")
    prenom_locataire = fields.Char(string="Prénom")
    prenom_locataire_2 = fields.Char(string="Prénom 2")
    nom_locataire = fields.Char(string="Nom")
    date_naissance_locataire = fields.Date(string="Date de naissance")
    lieu_naissance_locataire = fields.Char(string="Lieu de naissance")

    # Informations personnelles dans le cas d'une société ou autre - informations sur la société
    nom_societe = fields.Char(string="Nom de la société")
    numero_tva = fields.Char(string="Numéro TVA")
    rcs_siren = fields.Char(string="RCS/SIREN")
    capital_societe = fields.Integer(string="Capital")
    profession_societe = fields.Char(string="Profession exercée")

    # Image du responsable
    photo_locataire = fields.Binary(string="Photo")

    # Pièce d'identité
    type_identite = fields.Selection([('carte_identite', '''Carte d'identité'''), ('passport', 'Passport')],
                                     string="Type de pièce")
    numero_piece_identite = fields.Char(string="Numéro de la pièce")
    expiration_piece_identite = fields.Date(string="Date d'expitation")
    fichier_piece_identite = fields.Binary(string="Fichier")

    # Informations de contact
    email_locataire = fields.Char(string="Adresse Email")
    invitation = fields.Boolean(string="Invitation", help="Invitez et donnez accès au site à votre locataire via son "
                                                          "adresse email")
    email_locataire_2 = fields.Char(string="Email secondaire")
    telephone_locataire = fields.Char(string="Téléphone")
    telephone_locataire_2 = fields.Char(string="Téléphone 2")

    # Adresse
    adresse_locataire_id = fields.Many2one("rentalizi.adresse", string="Adresse")

    # Situation professionnelle
    profession_locataire = fields.Char(string="Profession locataire")
    revenus_locataire = fields.Integer(string="Revenus")
    situation_pro = fields.Char(string="Situation professionnelle")

    # Adresse professionnelle
    employeur = fields.Char(string="Employeur")
    adresse_pro_id = fields.Many2one("rentalizi.adresse", string="Adresse professionnelle")
    telephone_pro = fields.Char(string="Téléphone professionnel")

    # Informations complémentaires
    commentaires = fields.Text(string="Commentaires")
    nouvelle_adresse = fields.Char(string="Nouvelle adresse", help="Nouvelle adresse après son départ")

    # Coordonnées bancaires
    nom_banque = fields.Char(string="Banque")
    adresse_banque_id = fields.Many2one("rentalizi.adresse", string="Adresse banque")
    code_banque = fields.Char(string="Code banque")
    code_guichet = fields.Char(string="Code guichet")
    numero_compte = fields.Char(string="Numéro du compte")
    cle_rib = fields.Char(string="Clé RIB")
    iban = fields.Char(string="IBAN")
    swift_bic = fields.Char(string="SWIFT/BIC")




