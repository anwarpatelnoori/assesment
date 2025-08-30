# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ManufacturerItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		manufacturer: DF.Link
	# end: auto-generated types
	def validate(self):
		# validate duplicate item
		item_codes = []
		for idx, item in enumerate(self.mfr_items):
			if item.item_code in item_codes:
				frappe.throw(f"Duplicate Item Code Found: {item.item_code} at row {idx + 1}")
				break
			item_codes.append(item.item_code)
		blocked = frappe.db.get_value("Custom Manufacturer", self.manufacturer, "is_blocked")
		if blocked:
			frappe.throw(f"{self.manufacturer} is blocked")
	def before_save(self):
		pass
