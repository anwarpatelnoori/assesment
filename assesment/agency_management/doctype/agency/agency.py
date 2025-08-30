# Copyright (c) 2025, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Agency(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from assesment.agency_management.doctype.agency_item.agency_item import AgencyItem
		from frappe.types import DF

		agency_item: DF.Table[AgencyItem]
		agency_name: DF.Data
		email_id: DF.Data | None
		is_active: DF.Check
		phone_number: DF.Phone | None
		territory: DF.Link | None
	# end: auto-generated types

	def validate(self):
		if self.is_active == 0 and len(self.agency_item)>0:
			frappe.throw(f"You Can't disable the {self.agency_name} as it items are linked to it")


	@frappe.whitelist()
	def create_supplier(self, agency_name, email_id= None, territory= None, phone_number= None):
		#create supplier only if not exists
		supplier_exists = frappe.db.exists("Supplier",{"supplier_name":agency_name})
		if not supplier_exists:
			supplier = frappe.new_doc("Supplier")
			supplier.supplier_name = agency_name
			supplier.insert()
			contact = frappe.new_doc("Contact")
			contact.first_name = agency_name
			contact.append("email_ids",{
				"email_id" : email_id,
				"is_primary" : 1
			})
			contact.append("phone_nos",{
				"phone": phone_number,
				"is_primary_mobile_no":1
			})
			contact.append("links",{
				"link_doctype": "Supplier",
				"link_name": supplier.name
			})
			contact.insert()
			return frappe.msgprint(f'Supplier Created with name {supplier.name}')
		else:
			return frappe.throw(
						title='Dupplicate Entry',
						msg=f'Supplier {agency_name} already exists'
					)





		
