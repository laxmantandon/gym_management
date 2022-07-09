// Copyright (c) 2022, Laxman and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Group Class Booking', {
	refresh: function(frm) {
		frm.set_query("membership_plan", () => {
			return {
				filters: {
					is_group_class: ["=", true]
				}
			}
		})
	},

	membership_plan: function (frm) {
		frm.trigger("get_end_date");
	},

	start_date: function (frm) {
		frm.trigger("get_end_date");
	},

	get_end_date: function(frm) {
		frappe.db.get_doc('Membership Plan', frm.doc.membership_plan)
			.then(r => {
				var end_date = frappe.datetime.add_months(frm.doc.start_date, r.duration);
				frm.set_value("end_date", end_date);
				frm.set_value("amount", r.amount);
		});
	}
});
