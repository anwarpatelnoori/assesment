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
	agency_data = get_data(filters)
	data = format_data(agency_data)

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Agency"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Agency",
			"width": 120,
		},
		{
			"label": _("Agency Name"),
			"fieldname": "agency_name",
			"fieldtype": "Link",
			"options": "Supplier",
			"width": 120,
		},
		{
			"label": _("Item"),
			"fieldname": "item",
			"fieldtype": "Link",
			"options": "Item",
			"width": 120,
		},
		{
			"label": _("Min Order Qty"),
			"fieldname": "qty",
			"fieldtype": "Float",
			"width": 150,
		},
		{
			"label": _("Lead Time"),
			"fieldname": "lead_time",
			"fieldtype": "Float",
			"width": 120,
		},

	]


def get_data(filters) -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	agency = frappe.qb.DocType("Agency")
	agency_item = frappe.qb.DocType("Agency Item")
	agency_query = (
		frappe.qb.from_(agency_item)
		.join(agency)
		.on(agency_item.parent == agency.name)
		.select(
			agency.name,
			agency.agency_name,
			agency_item.parent,
			agency_item.item,
			agency_item.rate,
			agency_item.qty,
			agency_item.lead_time
		)
		.where(
			agency.is_active == 1
		)
		.orderby(agency.creation)
	)
	if filters.get("name"):
		agency_query = agency_query.where(agency.name == filters.get("name"))
	if filters.get("item"):
		agency_query = agency_query.where(agency_item.item == filters.get("item"))
	agency_data = agency_query.run(as_dict=True)
	return agency_data

def format_data(agency_data):
	grouped_data = []
	last_parent = None
	for data in agency_data:
		row = data.copy()
		if data.get('parent') != last_parent:
			last_parent = data["parent"]
		else:
			row["name"] = ""
			row["agency_name"] = ""
		grouped_data.append(row)
	return grouped_data