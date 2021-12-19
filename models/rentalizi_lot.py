from odoo import models, fields, api


class Lot(models.Model):
    _name = 'rentalizi.lot'
    _description = 'Lots de différents types contenus dans un immeuble'
    _rec_name = 'nom'

    # Informations générales
    nom = fields.Char(string='Nom du lot')
    type = fields.Selection([('appartement', 'Appartement'), ('atelier', 'Atelier'), ('boutique', 'Boutique'),
                             ('box_stockage', 'Box de stockage'), ('bureau_partage', 'Bureau partagé'),
                             ('bureaux', 'Bureaux'), ('caravane', 'Caravane'), ('cave', 'Cave'), ('chalet', 'Chalet'),
                             ('chambre', 'Chambre'), ('chateau', 'Château'), ('commerce', 'Commerce'),
                             ('entrepot', 'Entrepôt'), ('garage', 'Garage'), ('grenier', 'Grenier'),
                             ('hotel_particulier', 'Hôtel particulier'), ('local_professionnel', 'Local professionnel'),
                             ('loft', 'Loft'), ('maison', 'Maison'), ('parking', 'Parking'),
                             ('mobile_home', 'Mobile home'), ('studio', 'Studio'), ('terrain', 'Terrain'),
                             ('autre', 'Autre')], string="Type")
    # Adresse
    adresse_id = fields.Many2one("rentalizi.adresse", string="Adresse")
    batiment = fields.Char(string="Bâtiment")
    escalier = fields.Char(string="Escalier")
    etage = fields.Char(string="Etage")
    numero = fields.Integer(string="Numéro")
    # Description
    superficie = fields.Integer(string='Superficie(m²)')
    nbre_pieces = fields.Integer(string='Nombre de pièces')
    nbre_chambres = fields.Integer(string='Nombre de chambres')
    salles_bain = fields.Integer(string='Salles de bain')
    annee_construction = fields.Date(string="Année de construction")
    description = fields.Text(string='Description')
    notes = fields.Text(string="Notes")
    immeuble_id = fields.Many2one("rentalizi.immeuble", string="Immeuble")
    # Informations complémentaires
    type_habitat = fields.Selection([('collectif', 'Immeuble collectif'), ('individuel', 'Immeuble individuel')])
    regime_juridique = fields.Selection([('copropriete', 'Copropriété'), ('mono_propriete', 'Mono propriété')])
    bien_meuble = fields.Boolean(string="Bien meublé")
    fumeurs_acceptes = fields.Boolean(string="Fumeurs acceptés?")
    animaux_acceptes = fields.Boolean(string="Animaux acceptés?")
    complements = fields.Many2many("rentalizi.complements", string="Parties et équipements")
    parking = fields.Char(string="Parking")
    autres_dependances = fields.Char(string="Autres dépendances")
    cave = fields.Char(string="Cave")
    lot = fields.Char(string="Lot")
    milliemes = fields.Float(string="Millièmes")
    # Références cadastrales
    feuille_cadastrale = fields.Char(string="Feuille cadastrale")
    parcelle_cadastrale = fields.Char(string="Parcelle cadastrale")
    categorie_cadastrale = fields.Char(string="Catégorie cadastrale")
    valeur_locative = fields.Float(string="Valeur locative cadastrale")
    # les informations locatives
    devise_id = fields.Many2one("res.currency", default=lambda self: self.env.ref('base.main_company').currency_id)
    type_location = fields.Selection([('meuble', 'Meublé'), ('vide', 'Vide'), ('saisonniere', 'Saisonnière')])
    loyer_hc = fields.Monetary(string="Loyer HC", currency_field="devise_id")
    charges = fields.Monetary(string="Charges", currency_field="devise_id")
    # informations financières
    taxe_habitation = fields.Monetary(string="Taxe d'habitation", currency_field="devise_id")
    taxe_foncière = fields.Monetary(string="Taxe foncière", currency_field="devise_id")
    prix_acquisition = fields.Monetary(string="Prix d'acquisition", currency_field="devise_id")
    frais_acquisition = fields.Monetary(string="Frais d'acquisition", currency_field="devise_id")
    date_acquisition = fields.Date(string="Date d'acquisition")
    # Centre d'impôts
    nom_centre_impots = fields.Char(string="Nom du centre")
    adresse_centre_impots = fields.Many2one("rentalizi.adresse", string="Adresse du centre")
    notes_centre_impots = fields.Text(string="Quelques notes")

