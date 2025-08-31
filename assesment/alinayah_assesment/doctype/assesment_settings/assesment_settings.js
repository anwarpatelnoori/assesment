// Copyright (c) 2025, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Assesment Settings", {
	generate_demo_data: function (frm) {
		frm.call("create_demo_data")	},
	delete_demo_data: function (frm) {
		frm.call("delete_demo_data");
	}
});