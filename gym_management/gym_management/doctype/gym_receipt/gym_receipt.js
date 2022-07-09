// Copyright (c) 2022, Laxman and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Receipt', {
	refresh: function(frm) {
		frappe.db.get_single_value("Gym Settings", "default_payment_mode")
			.then(r => {
				console.log(r)
				if (r) {
					frm.set_value("payment_mode", r);
					frm.refresh_field("payment_mode");
				} else {
					frappe.msgprint("Default Payment Mode not specified in Gym Settings")
				}
				
			})
	}
});
