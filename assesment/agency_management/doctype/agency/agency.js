// Copyright (c) 2025, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Agency", {
    refresh(frm) {
        if (!frm.is_new()) {
            frappe.db.exists("Supplier", { "supplier_name": frm.doc.agency_name }).then(r => {
                if (r == false) {
                    frm.add_custom_button('Create Supplier', () => {
                        frm.call("create_supplier", {
                            agency_name: frm.doc.agency_name,
                            email_id: frm.doc.email_id,
                            territory: frm.doc.territory,
                            phone_number: frm.doc.phone_number
                        }).then(() => {
                            frm.refresh();
                        })
                    });
                }
            })
        }
    },
});


