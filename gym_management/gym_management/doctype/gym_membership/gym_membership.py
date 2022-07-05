# Copyright (c) 2022, Laxman and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import add_days, cint, date_diff, flt, get_datetime, getdate, nowdate, now_datetime
from frappe.model.document import Document

class GymMembership(Document):
	def validate(self):
		self.is_valid_member()
		self.validate_start_and_end_date()
		self.set_member_as_active()
		# self.post_gl_entry()

	def is_valid_member(self):
		member = frappe.get_doc('Gym Member', self.member)

		if member.status == 'Active':
			frappe.throw(f"{member.name} Already Has Active Membership")

	def validate_start_and_end_date(self):
		if self.end_date <= self.start_date:
			frappe.throw("End date can not be less than start date")

	def set_member_as_active(self):
		member = frappe.get_doc('Gym Member', self.member)
		member.status = "Active"
		member.save()