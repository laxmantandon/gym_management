// Copyright (c) 2022, Laxman and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker Booking', {
	refresh: function(frm) {
		frm.set_query("locker_id", () => {
			return {
				filters: {
					status: ["in", ["Vacant", ""]]
				}
			}
		})
	},

	locker_id: function(frm) {
		frm.trigger("get_locker_amount");
	},

	get_locker_amount: function(frm) {
		frappe.db.get_doc('Gym Locker', frm.doc.locker_id)
			.then(r => {
				frm.set_value("amount", r.amount);
		});
	}
});
