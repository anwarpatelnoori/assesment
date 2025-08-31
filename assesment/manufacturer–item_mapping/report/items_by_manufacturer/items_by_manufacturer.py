# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	items_by_manufacturer = get_data(filters)
	data = format_data(items_by_manufacturer)

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Manufacturer"),
			"fieldname": "manufacturer",
			"fieldtype": "Link",
			"options": "Custom Manufacturer",
			"width": 250,
		},
		{
			"label": _("Item"),
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"width": 150,
		},
	]


def get_data(filters) -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	mfr = frappe.qb.DocType("Manufacturer Item")
	item = frappe.qb.DocType("Mfr Items")
	mfr_details = frappe.qb.DocType("Custom Manufacturer")
	query = (
		frappe.qb.from_(item)
		.join(mfr)
		.on(item.parent == mfr.name)
		.join(mfr_details)
		.on(mfr.manufacturer == mfr_details.name)  
		.select(
				mfr.manufacturer,
				item.item_code
		)
	)
	if filters.get("manufacturer"):
		query = query.where(mfr.manufacturer == filters.get("manufacturer"))
	data = query.run(as_dict = True)	
	return query.run(as_dict = True)

def format_data(data):
	grouped_data = []
	last_parent = None
	for data in data:
		row = data.copy()
		if data.get('manufacturer') != last_parent:
			last_parent = data["manufacturer"]
		else:
			row["manufacturer"] = ""
		grouped_data.append(row)
	print(f'\n\n\n\n\n\n{grouped_data}\n\n\n\n\n\n\n')
	return grouped_data