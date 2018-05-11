# -*- encoding: utf-8 -*-

{
    'name' : 'Tunisia - Accounting 9.0',
    'version' : '1.0',
    'author' : 'WHITECAPE TECHNOLOGIES',
    'website': 'http://www.whitecapetech.com',
    'summary': 'Manage Chart of Accounts and Taxes template for companies in Tunisia with odoo 9',
    'category' : 'Localization',
    'description': """
This is the base module to manage Chart of Accounts and Taxes template for companies in Tunisia.
=================================================================================================
Ce Module charge le modèle du plan de comptes standard Tunisien et permet de générer les états
comptables aux normes tunisiennes.""",

    'depends': ['base_iban', 'account', 'base_vat'],
    'data': [
        'data/tn_pcg_taxes.xml',
        'data/plan_comptable_general.xml',
        'data/tn_tax.xml',
        'data/tn_fiscal_templates.xml',
        'data/account_chart_template.yml',
    ],
    'images': [
		'images/wct_tn.png',
        ],
    'active': True,
    'installable': True,
}

