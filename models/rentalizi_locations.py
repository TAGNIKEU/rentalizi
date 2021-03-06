from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Locations(models.Model):
    _name = "rentalizi.locations"
    _description = "Relations entre locataires et lots"
    _rec_name = "identifiant"

    bien = fields.Many2one("rentalizi.lot", string="Bien loué", required=True)
    etat_location = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string="Etat de la location")
    type_bail = fields.Selection([('habitation_vide', '''Bail d'habitation vide'''),
                                  ('habitation_meuble', '''Bail d'habitation meublé'''),
                                  ('meuble_etudiant', 'Bail meublé étudiant'), ('mobilite', 'Bail mobilité'),
                                  ('location_saisonniere', 'Bail de location saisonnière'), ('mixte', 'Bail mixte'),
                                  ('commercial', 'Bail commercial'), ('professionnel', 'Bail professionnel'),
                                  ('civil', 'Bail civil'), ('autre', 'Autre')], string="Type de bail", required=True,
                                 default="habitation_meuble")
    identifiant = fields.Char(string="Identifiant")
    utilisation = fields.Selection([('residence_principale', 'Résidence principale du locataire'),
                                    ('residence_secondaire', 'Résidence secondaire du locataire'),
                                    ('exclusion', '''Le locataire est autorisé à exercer son activité professionnelle, 
                                    à l'exclusion, cependant, de toute activité commerciale, 
                                    artisanale ou industrielle''')], string="Utilisation du bien",
                                   default="residence_principale")
    activite_exercee = fields.Char(string="Activité exercée dans les lieux")
    debut_bail = fields.Date(string="Début du bail", required=True)
    fin_bail = fields.Date(string="Fin du bail")
    duree_bail = fields.Char(string="Durée du bail", compute="_compute_duree_bail")
    # Renouvellement du bail par tacite reconduction
    renouvellement = fields.Boolean(string="Renouvellement?")
    # Fréquence de paiement du loyer
    paiement = fields.Selection([('mensuel', 'Mensuel'), ('bimestriel', 'Bimestriel'), ('trimestriel', 'Trimestriel'),
                                 ('quadrimestriel', 'Quadrimestriel'), ('semestriel', 'Semestriel'),
                                 ('annuel', 'Annuel'), ('forfaitaire', 'Forfaitaire')], string="Piement")
    # Date de paiement du loyer prévue dans le contrat.
    date_paiement = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                                      ('7', '7')], string="Date de paiement")
    # Cette date définit la période de la quittance de loyer. Si vous choisissez le 15 du mois, les quittances seront
    # datées du 15 au 14 du mois suivant.
    date_quittancement = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                                           ('7', '7')], string="Date de quittancement")
    # Si vous choisissez le J-5, le loyer et l'avis d'échéance sera généré 5 jours avant la date de quittancement.
    # Ex. Le loyer du 1 au 30 Avril sera généré le 26 Mars. Pour chaque contrat de location, les loyers sont générés
    # automatiquement chaque mois dans la rubrique Finances.
    generation_loyer = fields.Selection([('meme_date', 'Même que date quittancement'), ('j-1', 'J-1'), ('j-2', 'J-2'),
                                         ('j-3', 'J-3'), ('j-4', 'J-4'), ('j-5', 'J-5'), ('j-6', 'J-6')],
                                        string="Génération du loyer")
    moyen_paiement = fields.Selection([('carte_credit', 'Carte de crédit'), ('cheque', 'Chèque'), ('espece', 'Espèce'),
                                       ('automatique', 'Prélèvement automatique'), ('virement', 'Virement')])
    # Loyer
    loyer_hc = fields.Float(string="Loyer hors charges", required=True)
    taxe_hc = fields.Float(string="Taxe sur le loyer")
    charges_loyer = fields.Float(string="Charges")
    taxe_charges = fields.Float(string="Taxe sur les charges")
    type_charges = fields.Selection([('provision_charges', 'Provision pour charges'),
                                     ('forfait_charges', 'Forfait pour charges')], string="Type de charges",
                                    default="provision_charges")
    description_charges = fields.Text(string="Description de la charge")
    loyer_ttc = fields.Float(string="Loyer charges comprises", required=True)
    # Autres paiements: Autres paiements exceptionnels tels que le ménage, parking etc. Ces paiements figureront sur
    # chaque quittance et s'ajoutent au Loyer.
    autre_paiement_ids = fields.One2many("rentalizi.paiement", "location_id", string="Autre paiement")
    # Dépôt de garantie:
    depot_garantie = fields.Float(string="Dépôt de garantie", required=True)
    # Allocations logement: Renseigner ici les aides telles que la CAF, l'APL, qui vous sont versées automatiquement.
    # Le paiement sera généré automatiquement chaque mois comme déjà perçu.
    paiement_caf_apl = fields.Float(string="Paiement CAF/APL")
    # Frais de retard
    frais_retard = fields.Float(string="Frais de retard")
    type_prelevement = fields.Selection([('pourcentage', '%'), ('fixe', '€')])
    # Loyers prépayés ou solde locataire: Information reprise dans le solde locataire. Vous pouvez reporter le solde
    # des comptes à un loyer ultérieur.
    solde_locataire = fields.Float(string="Loyer prépayé/Solde")
    # Révision du loyer
    revision_loyer_selon = fields.Selection([('indice_reference_loyer', 'Indice de référence des loyers'),
                                             ('pourcentage_convevu_hausse', 'Pourcentage convenu à la hausse')],
                                            default="indice_reference_loyer", string="Révision du loyer selon")
    indice_référence = fields.Selection([('irl', 'IRL'), ('ilc', 'ILC'), ('icc', 'ICC'), ('ilat', 'ILAT'),
                                         ('indice_sante', 'Indice de santé')], string="Indice de référence",
                                        default="irl")
    # Partie à revoir
    trimestre = fields.Selection([('trimestre_4_2022', 'Trimestre 4'), ('trimestre_3_2022', 'Trimestre 3'),
                                  ('trimestre_2_2022', 'Trimestre 2'), ('trimestre_1_2022', 'Trimestre 1')],
                                 string="Trimestre", default="trimestre_3_2022")
    pourcentage = fields.Float(string="Pourcentage")
    # Si vous activez cette option, le site révisera automatiquement, chaque année à la date anniversaire, le montant
    # du loyer. Vous recevrez un email de notification. Cette option est disponible uniquement pour les indices IRL
    # et ILC.
    revision_auto = fields.Boolean(string="Révision automatique")
    # Période de révision du loyer.
    periode_revision = fields.Selection([('1', '1 an'), ('3', '3 ans')], string="Période")
    # Encadrement des loyers
    loyer_majore_fixe_arrete_prefectoral = fields.Selection([('oui', 'Oui'), ('non', 'Non')],
                                                            string="Le loyer du logement objet du présent contrat "
                                                                   "est-il soumis au loyer de référence majoré fixé par"
                                                                   " arrêté préfectoral ?")
    evolution_loyer_plafonnee_irl = fields.Selection([('oui', 'Oui'), ('non', 'Non')],
                                                     string="Le logement est-il dans une zone où l'évolution du loyer "
                                                            "est plafonnée à l'IRL ?")
    loyer_reference = fields.Float(string="Loyer de référence €/m²")  # Montant mensuel du loyer de référence €/m².
    loyer_majore = fields.Float(string="Loyer majoré €/m²")  # Montant mensuel du loyer de référence majoré €/m².
    complement_loyer = fields.Float(string="Complément de loyer")
    # A remplir si votre loyer est supérieur au loyer de référence majoré. Le complement de loyer doit être justifié.
    description_complement = fields.Text(string="Description du complément")
    bail_termine_depuis_18_mois = fields.Selection([('oui', 'Oui'), ('non', 'Non')],
                                                   string="Le bail du précédent locataire est-il terminé depuis "
                                                          "plus de 18 mois ? ", default="oui")
    # Montant du dernier loyer acquitté par le précédent locataire.
    dernier_loyer_applique = fields.Float(string="Dernier loyer appliqué")
    date_versement = fields.Date(string="Date de versement")
    derniere_revision = fields.Date(string="Dernière révision")
    loyer_objet_reevaluation = fields.Selection([('oui', 'Oui'), ('non', 'Non')], string="Le loyer fait-il l'objet "
                                                                                         "d'une réévaluation? ",
                                                default="non")
    montant_hausse_mensuelle = fields.Float(string="Montant de la hausse de loyer mensuelle")
    modalite_application_annuelle = fields.Selection([('par_tiers', 'Par tiers'), ('par_sixieme', 'Par sixième')],
                                                     string="Modalité d'application annuelle de la hausse")
    locataires_ids = fields.One2many("rentalizi.locataires", "location_id", string="Locataires")
    # Informations complémentaires
    montant_travaux_proprietaire = fields.Float(string="Montant")
    description_travaux_proprietaire = fields.Text(string="Description")
    document_travaux_priprietaire = fields.Binary(string="Document propriétaire")
    montant_travaux_locataire = fields.Float(string="Montant")
    description_travaux_locataire = fields.Text(string="Description")
    document_travaux_locataire = fields.Binary(string="Document locataire")
    conditions_particuliere = fields.Text(string="Conditions particulières")
    clauses_particuliere = fields.Text(string="Clauses particulières")
    commentaires = fields.Text(string="commentaires")
    # Assurance
    assurance_ids = fields.One2many("rentalizi.assurance", "location_id", string="Assurance")
    # Documents
    document_ids = fields.One2many("rentalizi.document", "location_id", string="Documents")
    # Quittance
    loyer_prorata = fields.Boolean(string="Cocher la case en cas de premier loyer au prorata")
    date_fin_periode = fields.Date(string="La date de fin de période pour la 1ère quittance")
    adresse_quittancement_autre = fields.Boolean(string="Cocher si l'adresse de quittancement est autre que l'adresse "
                                                        "du bien loué")
    adresse_quittancement = fields.Text(string="Adresse de quittancement")
    titre_document = fields.Selection([('quittance', 'Quittance'), ('facture', 'Facture')],
                                      string="Titre du document", default="quittance")
    numerotation = fields.Boolean(string="Numérotation")  # Activer / désactiver la numérotation automatique du document
    avis_deuxieme_page = fields.Boolean(string="Avis en deuxième page")  # Générer l'avis d'échéance pour le mois
    # suivant en deuxième page de la quittance du mois en cours.
    texte_quittance = fields.Text(string="Texte pour la quittance")  # Texte à afficher automatiquement en bas de la
    # Quittance
    texte_avis_echeance = fields.Text(string="Texte pour l'avis d'échéance")  # Texte à afficher automatiquement en
    # bas de l'Avis d'échéance
    # Autres réglages
    report_solde_locataire = fields.Selection([('manuel', 'Manuel'), ('automatique', 'Automatque')],
                                              string="Report du solde locataire", default="manuel")
    # En cas de report Automatique, à chaque nouveau paiement de loyer généré dans la rubrique Finances le
    # système modifiera l’échéance. Le montant sera augmenté/diminué par rapport à la somme reportée.
    notification_quittance_dispo = fields.Boolean(string="Recevoir une notification dès que la Quittance / Avis est "
                                                         "disponible en téléchargement")
    notification_locataire_quittance = fields.Boolean(string="Notifier le(s) locataire(s) dès que la Quittance / Avis "
                                                             "est disponible en téléchargement")
    email_rappel = fields.Boolean(string="Envoyer un email de rappel 6 et 3 mois avant l’échéance du contrat")
    notification_locataire_echeance = fields.Boolean(string="Notifier le(s) locataire(s) 3 mois avant l’échéance du "
                                                            "contrat")
    partage = fields.Boolean(string="Partager le document avec votre locataire")

    @api.depends('debut_bail', 'fin_bail')
    def _compute_duree_bail(self):
        for rec in self:
            rec.duree_bail = {"Anée(s)": relativedelta(rec.fin_bail, rec.debut_bail).years,
                              "Mois": relativedelta(rec.fin_bail, rec.debut_bail).months,
                              "Jour(s)": relativedelta(rec.fin_bail, rec.debut_bail).days}
