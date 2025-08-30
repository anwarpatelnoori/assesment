# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CustomManufacturer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		country: DF.Link | None
		gln: DF.Data
		is_blocked: DF.Check
		manufacturer_name: DF.Data
		website: DF.Data | None
	# end: auto-generated types

	pass
