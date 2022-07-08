# Copyright (c) 2022, Laxman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymTrainingSubscription(Document):
	def validate(self):
		self.is_valid_member()
		# self.is_valid_time_slot()
		self.validate_start_and_end_date()

	def on_submit(self):
		self.set_trainer_status('Engaged')
		self.post_gym_gl_entry()

	def on_cancel(self):
		self.set_trainer_status('Free')
		self.cancel_gl_entry()

	def is_valid_member(self):
		member = frappe.get_doc('Gym Member', self.member)

		if member.status != 'Active':
			frappe.throw(f"{member.name} Does not have active membership")

	def validate_start_and_end_date(self):
		if not self.end_date:
			frappe.throw("Please enter End Date")

		if self.end_date <= self.start_date:
			frappe.throw("End date can not be less than start date")

	def set_trainer_status(self, status):
		trainer = frappe.get_doc('Gym Trainer', self.trainer)
		trainer.status = status
		trainer.save()

	def post_gym_gl_entry(self):
		
		gl_entry = frappe.new_doc('Gym GL Entries')
		gl_entry.name = self.name
		gl_entry.ledger_name = self.member
		gl_entry.ledger_full_name = self.full_name
		gl_entry.document_no = self.name
		gl_entry.document_date = self.posting_date
		gl_entry.document_type = "Personal Trainer"
		gl_entry.debit_amount = self.amount
		gl_entry.credit_amount = 0
		gl_entry.description = f"Personal Trainer Allocation, Trainer Name {self.trainer}"
		gl_entry.save()
		gl_entry.submit()

	def cancel_gl_entry(self):
		gl_entry = frappe.get_doc('Gym GL Entries', self.name)
		if gl_entry:
			gl_entry.cancel()

	# def is_valid_time_slot(self):
	# 	trainer = frappe.get_doc('Gym Trainer', self.trainer)
	# 	if trainer:
	# 		if trainer.status == 'Occupied':
	# 			trainer.throw(f"Trainer {self.locker_id} is already engaged")
