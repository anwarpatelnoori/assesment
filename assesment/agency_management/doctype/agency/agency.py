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
		country: DF.Link | None
		email_id: DF.Data | None
		is_active: DF.Check
		phone_number: DF.Phone | None
	# end: auto-generated types

	def validate(self):
		item_codes = []
		for idx, item in enumerate(self.agency_item):
			if item.item in item_codes:
				frappe.throw(f"Duplicate Item Code Found: {item.item} at row {idx + 1}")
				break
			item_codes.append(item.item)

		if self.is_active == 0: 
			if len(self.agency_item)>0:
				frappe.throw("Can't Blaock Agent, as Items are already linked")
			purchase_invoice_exists = frappe.db.exists("Purchase Invoice", {"supplier": self.agency_name, "docstatus": 1})
			purchase_receipt_exists = frappe.db.exists("Purchase Receipt", {"supplier": self.agency_name, "docstatus": 1})
			if purchase_invoice_exists:
				frappe.throw(
					msg = ("Purchase Invoice already exists: <a href='{0}' target='_blank'>{1}</a>").format(
								frappe.utils.get_url_to_form("Purchase Invoice", purchase_invoice_exists),
								purchase_invoice_exists
							),
					title = ("Can't Block Agent, as Purchase is already done")
				)

			if purchase_receipt_exists:
				frappe.throw(
					msg = ("Purchase Receipt already exists: <a href='{0}' target='_blank'>{1}</a>").format(
								frappe.utils.get_url_to_form("Purchase Receipt", purchase_receipt_exists),
								purchase_receipt_exists
							),
					title = ("Can't Block Agent, as Purchase is already done")
				)



	@frappe.whitelist()
	def create_supplier(self, agency_name, email_id= None, country= None, phone_number= None):
		#create supplier only if not exists
		supplier_exists = frappe.db.exists("Supplier",{"supplier_name":agency_name})
		if not supplier_exists:
			supplier = frappe.new_doc("Supplier")
			supplier.supplier_name = agency_name
			supplier.custom_agency = self.name
			if country:
				supplier.country = self.country
			supplier.insert()
			
			# create contact and link with supplier
			contact = frappe.new_doc("Contact")
			contact.first_name = agency_name
			if email_id:
				contact.append("email_ids",{
					"email_id" : email_id,
					"is_primary" : 1
				})
			if phone_number:	
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

	@frappe.whitelist()
	def check_supplier(self):
		supplier_exists = frappe.db.exists("Supplier", { "supplier_name": self.agency_name })
		return frappe.db.exists("Supplier", { "supplier_name": self.agency_name })

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_items_from_agency(doctype, txt, searchfield, start, page_len, filters):
	filters = frappe.parse_json(filters)
	agency_name = filters.get("agency_name") 
	# filter only agency items
	return frappe.db.sql("""
		SELECT 
			agency_item.item as item_code
		FROM `tabAgency` agency
		JOIN `tabAgency Item` agency_item ON agency_item.parent = agency.name
		WHERE
			agency.agency_name = %(agency_name)s
			AND (agency_item.item LIKE %(txt)s)
		LIMIT %(page_len)s OFFSET %(start)s
	""", {
		"agency_name": agency_name,  
		"txt": f"%{txt}%",
		"page_len": page_len,
		"start": start
	})





		
