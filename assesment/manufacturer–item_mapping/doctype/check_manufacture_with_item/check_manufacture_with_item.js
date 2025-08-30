frappe.ui.form.on("Check Manufacture with Item", {
	get_manufacture(frm) {
        if (frm.doc.item) {
            frm.call("get_all_manufactures").then(r => {
                if (r.message.length>0) {                    
                    // Start building the table
                    let table = `
                        <table class="min-w-full table-auto border-collapse">
                            <thead>
                                <tr>
                                    <th class="border px-4 py-2 text-left">Manufacturer Name</th>
                                    <th class="border px-4 py-2 text-left">GLN No</th>
                                    <th class="border px-4 py-2 text-left">Country</th>
                                </tr>
                            </thead>
                            <tbody>
                    `;
                    // Loop through the data from r.message and create rows
                    r.message.forEach(item => {
                        table += `
                            <tr>
                                <td class="border px-4 py-2">${item.manufacturer_name || 'N/A'}</td>
                                <td class="border px-4 py-2">${item.gln_no || 'N/A'}</td>
                                <td class="border px-4 py-2">${item.country || 'N/A'}</td>
                            </tr>
                        `;
                    });

                    // Close the table tag
                    table += `
                            </tbody>
                        </table>
                    `;
                    frm.set_df_property("all_manufactures", "options", table);
                } else {
                    frm.set_df_property("all_manufactures", "options", "<b>No Manfuactures Found for the item</b>")
                }
            });
        } else {
            frappe.msgprint("Select Item First");
        }
	},
});
