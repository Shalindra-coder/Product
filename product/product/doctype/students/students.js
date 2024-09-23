// Copyright (c) 2024, shalidnra and contributors
// For license information, please see license.txt

frappe.ui.form.on("Students", {
    onload(frm) {
        console.log("Running load...");
    },
    
    refresh(frm) {
        console.log("Refresh event triggered.");

        // You can add custom buttons or additional logic here
        if (frm.doc.status === "Active") {
            frm.add_custom_button("Send Reminder", () => {
                // Logic to send a reminder
                frappe.msgprint("Reminder sent to student!");
            });
        }
    },

    status(frm) {
        console.log("Status change detected.");
        if (frm.doc.status === "Accepted") {
            frappe.msgprint("Congratulations you Selected!");
        }
    }
});
