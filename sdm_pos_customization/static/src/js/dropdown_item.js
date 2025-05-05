import { Navbar } from "@point_of_sale/app/navbar/navbar";
import { patch } from "@web/core/utils/patch";
import { SelectCreateDialog } from "@web/views/view_dialogs/select_create_dialog";


//patch(Navbar.prototype, {
//    CustomAction() {
//        alert("hiii");
//    },
//});
patch(Navbar.prototype, {
    CustomAction() {
        this.dialog.add(SelectCreateDialog, {
            resModel: "res.partner",
            noCreate: true,
            multiSelect: false,
            onSelected: async (resIds) => {
                await this.pos.CustomAction(resIds[0]);
            },
        });
    },
});