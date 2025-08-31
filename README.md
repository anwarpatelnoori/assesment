### alinayah_assesment

alinayah_assesment
### Prerequisite
- Frappe V15
- ERPNext V15

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app git@github.com:anwarpatelnoori/assesment.git --branch main
bench install-app assesment
```
### App Module
- After Installing app these 2 workspace will come
<img width="1787" height="411" alt="image" src="https://github.com/user-attachments/assets/df3c9cd1-6fb0-4b81-97b2-4ac19aaba0e0" />

## Testing Instruction: Module 1: Agency Management
### Agency DocType Functionalites :
- Agency name is manatory
<img width="1134" height="544" alt="image" src="https://github.com/user-attachments/assets/66a3d9d8-6cd0-4d08-9766-2f2b2b0ee252" />

- Once all deatils are enter and saved, `Create Supplier` button is visble
- On Clicking on this, Contact is created and then Supplier is created
<img width="1288" height="492" alt="image" src="https://github.com/user-attachments/assets/bd68269e-6827-4860-8cc2-3a4405930530" />

- After Creation `Go To Supplier` button will be added and it is linked to Respective Supplier
<img width="1212" height="671" alt="image" src="https://github.com/user-attachments/assets/0e07de21-836a-4a21-9d2f-6213b245a0a3" />

#### Agency DocType Validations:
- Prevents duplicate items in agency items table.
<img width="1370" height="702" alt="image" src="https://github.com/user-attachments/assets/a92d9676-5e38-4b62-9585-0f60de568edb" />
- Prevent deactivating an Agency if it purchase has been done with this supplier or Items has been added in the child table.
- - It will show with hyeper link of Purchase Invoice/receipt of that supplier if it founds
<img width="1352" height="503" alt="image" src="https://github.com/user-attachments/assets/2bcde301-df19-43c9-8498-eed4efbe102a" />
- Inactive Agencies show in red on list view.
<img width="1420" height="488" alt="image" src="https://github.com/user-attachments/assets/aa36e3f5-5c3a-4a0d-9189-3f78d6792abf" />
#### Report
- Report: Agency Lead Times (Agency, Item, Min Order Qty, Lead Time)
- Filters:  Agency, Item    
<img width="1035" height="460" alt="image" src="https://github.com/user-attachments/assets/a14e66aa-44c7-4953-b6ed-abf74957a75f" />

