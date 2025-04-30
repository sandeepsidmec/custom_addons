{
    "name": "POS Customization",
    'category': 'POS',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'sdm_pos_customization/static/src/js/product_card.js',
            'sdm_pos_customization/static/src/js/orderline.js',
            'sdm_pos_customization/static/src/xml/product_card.xml',
            'sdm_pos_customization/static/src/xml/product_screen.xml',
            'sdm_pos_customization/static/src/xml/orderline.xml',
        ],
    },
}
