# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MfrItems(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		gtin: DF.Data | None
		item_code: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		part_number: DF.Data | None
	# end: auto-generated types

	pass
