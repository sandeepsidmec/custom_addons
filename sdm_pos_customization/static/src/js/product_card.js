import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card"
import { patch } from "@web/core/utils/patch";

patch(ProductCard, {
    props: {
        ...ProductCard.props,
        barcode: { type: undefined, optional: true },
        lst_price: {type: Number},
    },
});