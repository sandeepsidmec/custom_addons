import { Navbar } from "@point_of_sale/app/navbar/navbar";
import { patch } from "@web/core/utils/patch";


//patch(Navbar.prototype, {
//    CustomAction() {
//        this.dialog.add(SelectCreateDialog, {
//            resModel: "sale.order",
//            noCreate: true,
//            multiSelect: false,
//            domain: [
//                ["state", "!=", "cancel"],
//                ["invoice_status", "!=", "invoiced"],
//                ["currency_id", "=", this.pos.currency.id],
//            ],
//            onSelected: async (resIds) => {
//                await this.pos.onClickSaleOrder(resIds[0]);
//            },
//        });
//    },
//});


patch(Navbar.prototype, {
    CustomAction() {
        alert("hiii");
    },
});
