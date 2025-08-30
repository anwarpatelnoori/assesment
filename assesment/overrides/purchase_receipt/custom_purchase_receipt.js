frappe.ui.form.on('Purchase Receipt', {
    supplier(frm) {
        frm.trigger("set_item_query");
    },
    onload_post_render: function () {
    },
    set_item_query(frm) {
        if (!cur_frm.doc.supplier){
            return
        }
        frm.set_query("item_code", "items", function (frm, cdt, cdn) {
            return {
                query: "assesment.agency_management.doctype.agency.agency.get_items_from_agency", 
                filters: {
                    agency_name: cur_frm.doc.supplier
                }
            };
        });
    }
});
