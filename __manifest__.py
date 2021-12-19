# -*- coding: utf-8 -*-
{
    'name': "rentalizi",

    'summary': """
        Application de gestion locative des biens immobiliers
    """,

    'description': """
        Créez vos biens, créez vos locataires et attribuez les biens aux locataire.
        suivez l'évolution de vos locations et soyez notifiés lorque ce dernier arrive à expiration
        Générez vos contrats de bail et faites les parvenir aux locataires soir physiquement soit par mail 
    """,

    'author': "RBK Services",
    'website': "https://www.rbk-services.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Immobilier',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/rentalizi_vues_paiement.xml',
        'views/rentalizi_vues_locations.xml',
        'views/rentalizi_vues_adresses.xml',
        'views/rentalizi_vues_locataires.xml',
        'views/rentalizi_vues_complements.xml',
        'views/rentalizi_vues_villes.xml',
        'views/rentalizi_vues_lots.xml',
        'security/ir.model.access.csv',
        'views/rentalizi_vues_immeubles.xml',
        'views/rentalizi_menus.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}