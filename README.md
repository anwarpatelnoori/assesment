### alinayah_assesment

alinayah_assesment
### Prerequisite
- Frappe V15
- ERPNext V15

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

bash
cd $PATH_TO_YOUR_BENCH
bench get-app git@github.com:anwarpatelnoori/assesment.git --branch main
bench install-app assesment
bench migrate

## While Running migratation test data will be created and output will look something like this
<img width="1360" height="790" alt="image" src="https://github.com/user-attachments/assets/1d3fe68f-c35e-4d53-aa1a-1a390652dcc1" />

## If somehow it fails(due to patches line bug). Please go to Assesment Settings, to mangae demo data
<img width="1518" height="437" alt="image" src="https://github.com/user-attachments/assets/8d449223-a06d-4781-8023-e9e9b82e61f2" />

- Click on `Generate Demo Data`. This will create demo data
<img width="1220" height="329" alt="image" src="https://github.com/user-attachments/assets/f6544195-4be1-45b3-b462-5839d321b828" />

- Click on `Delete Demo Data`. This will delete demo data 
<img width="1226" height="321" alt="image" src="https://github.com/user-attachments/assets/5ac0d4ad-4838-4f43-9972-99b7501fcb81" />





### App Module
- After Installing app these 2 workspace will come
<img width="1787" height="411" alt="image" src="https://github.com/user-attachments/assets/df3c9cd1-6fb0-4b81-97b2-4ac19aaba0e0" />

## Testing Instruction: Module 1: Agency Management 
### Agency DocType Functionalites :
- Agency name is manatory
<img width="1134" height="544" alt="image" src="https://github.com/user-attachments/assets/66a3d9d8-6cd0-4d08-9766-2f2b2b0ee252" />

- Once all deatils are enter and saved, Create Supplier button is visble
- On Clicking on this, Contact is created and then Supplier is created
<img width="1288" height="492" alt="image" src="https://github.com/user-attachments/assets/bd68269e-6827-4860-8cc2-3a4405930530" />

- After Creation Go To Supplier button will be added and it is linked to Respective Supplier
<img width="1212" height="671" alt="image" src="https://github.com/user-attachments/assets/0e07de21-836a-4a21-9d2f-6213b245a0a3" />

#### Agency DocType Validations:
- Prevents duplicate items in agency items table.
<img width="1370" height="702" alt="image" src="https://github.com/user-attachments/assets/a92d9676-5e38-4b62-9585-0f60de568edb" />

- Prevent deactivating an Agency if it purchase has been done with this supplier or Items has been added in the child table.
- It will show with hyeper link of Purchase Invoice/receipt of that supplier if it founds
<img width="1352" height="503" alt="image" src="https://github.com/user-attachments/assets/2bcde301-df19-43c9-8498-eed4efbe102a" />

- Inactive Agencies show in red on list view.
<img width="1420" height="488" alt="image" src="https://github.com/user-attachments/assets/aa36e3f5-5c3a-4a0d-9189-3f78d6792abf" />

#### Report
- Report: Agency Lead Times (Agency, Item, Min Order Qty, Lead Time)
- Filters:  Agency, Item
- Agency name & Id will not repat if it has more than one item    
<img width="1035" height="460" alt="image" src="https://github.com/user-attachments/assets/a14e66aa-44c7-4953-b6ed-abf74957a75f" />

### Agency Item filterd in Purchase Invoice and Receipt
<img width="1869" height="812" alt="image" src="https://github.com/user-attachments/assets/a3191b88-4c96-45ad-bdf2-5a3a1333f494" />


## Testing Instruction: Module 2: Manufacturer–Item Mapping
### Manufacturer DocType Functionalites :
- Manufacturer Name and Global Location Number is manatory
<img width="1211" height="402" alt="image" src="https://github.com/user-attachments/assets/9950f870-0cf3-4f73-99ad-960dbf5c0bdf" />

### Manufacturer Item DocType Functionalites :  
- Manufacturer is manatory and it will list those are active only
- Validation is writen to not allow blocked manfuacters 
- Part Number will be fetched from Item Master even if it is left blanked it will fetch 
<img width="1769" height="742" alt="image" src="https://github.com/user-attachments/assets/82f820a4-c92a-48fc-89ee-8e2f97fb5460" />

### Manufacturer Item validations:
- It will not allow block supplier even from data import, server script is written for that case
- Prevents duplicate items in manufactures items table
<img width="1263" height="442" alt="image" src="https://github.com/user-attachments/assets/f50a763d-dddb-4c64-8d49-305b8d3dc9ac" />

 *Uniquess of Manufacturer and Item Code is mainted by this approach*
-  Enabled Unique Property of Manufacturer
-  Prevent  duplicate items in manufactures items table    

### Check Manufacture with Item
- It has Item Field
- Get Manufacturer Button
- Upon clicking this it will list all the manufacturers of that item  in html field
<img width="1303" height="424" alt="image" src="https://github.com/user-attachments/assets/a08ca35e-9889-4449-891e-4c6b7e2abbcb" />
<img width="873" height="458" alt="image" src="https://github.com/user-attachments/assets/a2ff5d5f-020e-4328-a9eb-72b93e814ca4" />

### Report: Items by Manufacturer.
<img width="530" height="318" alt="image" src="https://github.com/user-attachments/assets/da2ee007-3d5c-4cc7-8a2b-70c5f5c2a0ab" />


### Rest API requiremtn: http://localhost:8001/api/method/assesment.manufacturer–item_mapping.doctype.check_manufacture_with_item.check_manufacture_with_item.get_all_manufactures?name=100
<img width="1363" height="948" alt="image" src="https://github.com/user-attachments/assets/8c1c263a-c0ce-4431-87d0-f93a8a9597c3" />
