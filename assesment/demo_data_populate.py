from assesment.demo_data import medical_items, agencies, manufacturers
import random
import frappe
import string

def create_demo_items():
    item_group = frappe.new_doc("Item Group")
    item_group.item_group_name = "Medical Items"
    item_group.insert()
    frappe.db.commit()
    for name, details in medical_items.items():
        new_item = frappe.new_doc("Item") 
        new_item.item_code = name
        new_item.item_name = details['item_code']
        new_item.custom_part_number = details['part_number']
        new_item.item_group = "Medical Items"
        new_item.insert()
    frappe.db.commit()

def create_demo_agents():
    all_items =  frappe.get_all("Item", {"item_group":"Medical Items"})
    for name, details in agencies.items():
        agency = frappe.new_doc("Agency")
        agency.agency_name = name
        agency.email_id = details.get("email")
        agency.phone_number = details.get("phone")
        agency.country = details.get("country")
        agency.is_active = random.randint(0,1)
        
        # link random medical_items
        length = random.randint(1, len(all_items))
        random_item_list = random.sample(all_items, length)
        for item in random_item_list:
            agency.append("agency_item",{
                "item": item.get("name"),
                "rate": random.randint(100,200),
                "qty": random.randint(300,500),
                "lead_time": random.randint(1,10)
            })
        agency.insert()
    frappe.db.commit()

def create_demo_manufacturers():
    for name, details in manufacturers.items():
        mfr = frappe.new_doc("Custom Manufacturer")
        mfr.manufacturer_name = name
        mfr.gln = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        mfr.country = details.get("country")
        mfr.website = f'https://{name.replace(" ", "").lower()}'
        mfr.is_blocked = random.randint(0,1)
        mfr.insert()
    frappe.db.commit()

def create_new_manufacturer_item():
    all_manufacturer = all_manufacturer = frappe.get_all("Custom Manufacturer", filters = {"is_blocked": 0})
    all_items =  frappe.get_all("Item", {"item_group":"Medical Items"})
    for mfr in all_manufacturer:
        mfr_item = frappe.new_doc("Manufacturer Item")
        mfr_item.manufacturer = mfr.get("name")

        # link random medical_items
        length = random.randint(1, len(all_items))
        random_item_list = random.sample(all_items, length)
        for item in random_item_list:
            mfr_item.append ("mfr_items", {
                "item_code": item.get("name"),
                "gtin": ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            })
        mfr_item.insert()
    frappe.db.commit()

def execute():
    print(f'\n\nCreating Demo Data. Wait for few seconds')
    print("Creating Demo Items")
    create_demo_items()
    print("Created Demo Items\n")
    print("Creating Demo Agencies")
    create_demo_agents()
    print("Created Demo Agencies\n")
    print("Creating Demo Manufacturer")
    create_demo_manufacturers()
    print("Created Demo Manufacturer\n")
    print("Creating Demo Manufacturer Item ")
    create_new_manufacturer_item()
    print("Created Demo Manufacturer Item ")
    print(f'Demo Data created💥💥💥')
    print(f'\n\n')

@frappe.whitelist()
def create_demo_data():
    try:
        create_demo_items()
        create_demo_agents()
        create_demo_manufacturers()
        create_new_manufacturer_item()
        return True    
    except Exception as e:
        # Log the traceback + error message in Frappe’s Error Log doctype
        frappe.log_error(
            message=frappe.get_traceback(),
            title="Demo Data Creation Failed"
        )
        # Show a friendly error message to the user
        frappe.throw("⚠️ Demo Data already exists or cannot be created.")
        return False


    