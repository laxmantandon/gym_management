# Copyright (c) 2022, Laxman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymGroupClassBooking(Document):
	def validate(self):
		self.is_valid_member()
		self.validate_start_and_end_date()

	def on_submit(self):
		self.set_member_status('Active')
		self.post_gym_gl_entry()

	def on_cancel(self):
		self.set_member_status('Lead')
		self.cancel_gl_entry()

	def is_valid_member(self):
		member = frappe.get_doc('Gym Member', self.member)

		if member.status == 'Active':
			frappe.throw(f"{member.name} Already Has Active Membership")

	def validate_start_and_end_date(self):
		if self.end_date <= self.start_date:
			frappe.throw("End date can not be less than start date")

	def set_member_status(self, status):
		member = frappe.get_doc('Gym Member', self.member)
		member.status = status
		member.save()

	def post_gym_gl_entry(self):
		
		gl_entry = frappe.new_doc('Gym GL Entries')
		gl_entry.name = self.name
		gl_entry.ledger_name = self.member
		gl_entry.ledger_full_name = self.full_name
		gl_entry.document_no = self.name
		gl_entry.document_date = self.posting_date
		gl_entry.document_type = "Group Class Booking"
		gl_entry.debit_amount = self.amount
		gl_entry.credit_amount = 0
		gl_entry.description = f"Plan {self.membership_plan}, From {self.start_date}, To {self.end_date}"
		gl_entry.save()
		gl_entry.submit()

	def cancel_gl_entry(self):
		gl_entry = frappe.get_doc('Gym GL Entries', self.name)
		if gl_entry:
			gl_entry.cancel()
