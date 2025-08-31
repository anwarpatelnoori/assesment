# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AssesmentSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF


	# end: auto-generated types
	pass
# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt
from assesment.demo_data_populate import create_demo_items, create_demo_agents, create_demo_manufacturers, create_new_manufacturer_item  
import frappe
from frappe.model.document import Document


class AssesmentSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF


	# end: auto-generated types
	@frappe.whitelist()
	def create_demo_data(self):
		try:
			create_demo_items()
			create_demo_agents()
			create_demo_manufacturers()
			create_new_manufacturer_item()
			frappe.msgprint("Demo Data Created 💥💥")
			return True    
		except Exception as e:
			# Log the traceback + error message in Frappe’s Error Log doctype
			frappe.log_error(
				message=frappe.get_traceback(),
				title="Demo Data Creation Failed"
			)
			# Show a friendly error message to the user
			frappe.throw("⚠ Demo Data already exists or cannot be created.")
			return False

	@frappe.whitelist()
	def delete_demo_data(self):
		# delete all agencies
		frappe.db.sql("delete from `tabAgency`;")

		# delete all custom manufacturers
		frappe.db.sql("delete from `tabCustom Manufacturer`;")

		# delete all manufacturer items
		frappe.db.sql("delete from `tabManufacturer Item`;")

		# delete items in group "Medical Items"
		frappe.db.sql("delete from `tabItem` WHERE item_group = 'Medical Items';")

		# delete the Item Group itself (only if it exists)
		frappe.db.sql("delete from `tabItem Group` WHERE name = 'Medical Items';")
		frappe.msgprint("Demo Data Deleted Successfully! 🗑️🗑️")