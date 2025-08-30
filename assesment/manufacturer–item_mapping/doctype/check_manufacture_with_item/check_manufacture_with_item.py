# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class CheckManufacturewithItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		item: DF.Link | None
	# end: auto-generated types

	@frappe.whitelist()
	def get_all_manufactures(self,name):
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
				mfr_details.manufacturer_name,
				mfr_details.gln,
				mfr_details.country
			)
			.where(
				item.item_code == self.item or name
			)
		)
		return query.run(as_dict = True)
@frappe.whitelist()
def get_all_manufactures(name):
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
			mfr_details.manufacturer_name,
			mfr_details.gln,
			mfr_details.country
		)
		.where(
			item.item_code ==  name
		)
	)
	return query.run(as_dict = True)

