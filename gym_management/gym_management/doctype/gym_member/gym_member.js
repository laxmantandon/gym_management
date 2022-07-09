// Copyright (c) 2022, Laxman and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
	refresh: function(frm) {

		if (frm.doc.status != "Active") {
			frm.add_custom_button('New Membership', () => {
				frappe.new_doc('Gym Membership', {
					member: frm.doc.name
				})
			}, __("Create"));				
		}

		if (frm.doc.status == "Active") {
			frm.add_custom_button('Locker Booking', () => {
				frappe.new_doc('Gym Locker Booking', {
					member: frm.doc.name
				})
			}, __("Create"));
	
			frm.add_custom_button('Trainer Allocation', () => {
				frappe.new_doc('Gym Training Subscription', {
					member: frm.doc.name
				})
			}, __("Create"));	

			frm.add_custom_button('Group Class Booking', () => {
				frappe.new_doc('Gym Group Class Booking', {
					member: frm.doc.name
				})
			}, __("Create"));	

			frm.add_custom_button('Statement of Account', () => {
				frappe.set_route('gym-gl-entries/view/report', { ledger_name : frm.doc.name, status: "Submitted"})
			}, __("View"));				

		}


	}
});
