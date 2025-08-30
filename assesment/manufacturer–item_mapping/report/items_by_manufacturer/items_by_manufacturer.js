// Copyright (c) 2025, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.query_reports["Items by Manufacturer"] = {
	filters: [
		{
			"fieldname": "manufacturer",
			"label": __("Manufacturer"),
			"fieldtype": "Link",
			"options": "Custom Manufacturer"
		},
	],
};
