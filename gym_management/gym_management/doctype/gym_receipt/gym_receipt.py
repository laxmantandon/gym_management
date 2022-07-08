# Copyright (c) 2022, Laxman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymReceipt(Document):
	def validate(self):
		pass

	def on_submit(self):
		self.post_gl_entries()

	def on_cancel(self):
		self.cancel_gl_entry()

	def post_gl_entries(self):

		gl_entry = frappe.new_doc('Gym GL Entries')
		gl_entry.name = self.name
		gl_entry.ledger_name = self.member
		gl_entry.ledger_full_name = self.full_name
		gl_entry.document_no = self.name
		gl_entry.document_date = self.posting_date
		gl_entry.document_type = "Receipt"
		gl_entry.debit_amount = 0
		gl_entry.credit_amount = self.amount
		gl_entry.description = f"Amount Received by {self.payment_mode}, Remarks: {self.remarks} Ref Number {self.transaction_reference}"
		gl_entry.save()
		gl_entry.submit()

	def cancel_gl_entry(self):
		gl_entry = frappe.get_doc('Gym GL Entries', self.name)
		if gl_entry:
			gl_entry.cancel()		
