// Copyright (c) 2025, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Agency", {
    refresh(frm) {
        if (!frm.is_new()) {
            frappe.db.exists("Supplier", { "supplier_name": frm.doc.agency_name }).then(r => {
                if (r == true) {
                    // add go to supplier button if exists 
                    frm.add_custom_button('Go to Supplier', () => {
                        frappe.set_route("Form", "Supplier", frm.doc.agency_name)
                    });
                }
                else {
                    //  create supplier button if not exists
                    frm.add_custom_button('Create Supplier', () => {
                        frm.call("create_supplier", {
                            agency_name: frm.doc.agency_name,
                            email_id: frm.doc.email_id,
                            country: frm.doc.country,
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


