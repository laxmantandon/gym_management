// Copyright (c) 2022, Laxman and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Training Subscription', {
	// refresh: function(frm) {

	// }

	membership_plan: function(frm) {
		frm.trigger("set_dates");
	},

	set_dates: function(frm) {
		frappe.db.get_doc('Membership Plan', frm.doc.membership_plan)
			.then(r => {
				var end_date = frappe.datetime.add_months(frm.doc.start_date, r.duration);
				frm.set_value("end_date", end_date);
		});
	}
});
