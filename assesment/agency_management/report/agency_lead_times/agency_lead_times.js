// Copyright (c) 2025, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.query_reports["Agency Lead Times"] = {
	filters: [
		{
			"fieldname": "name",
			"label": __("Agency"),
			"fieldtype": "Link",
			"options": "Agency"
		},
		{
			"fieldname": "item",
			"label": __("Item"),
			"fieldtype": "Link",
			"options": "Item"
		},
	],
};
