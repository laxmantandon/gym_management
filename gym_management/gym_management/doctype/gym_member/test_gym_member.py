# Copyright (c) 2022, Laxman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymMember(FrappeTestCase):
	def test_create_gym_member(self):
		doc = self.make_gym_member()
		# member = frappe.get_doc("Gym Member", "_Test")
		self.assertEqual(doc.first_name, "_Test")

	def make_gym_member(self):
		try:
			gym_member = frappe.get_doc({
				"doctype": "Gym Member",
				"first_name": "_Test",
				"last_name": "_Test Last Name",
				"contact": "+91-9926100041",
				"address_1": "Main Road",
				"city": "Raipur",
				"state": "Chhattisgarh",
				"status": "Lead"
			})
			gym_member.insert()
			return gym_member

		except Exception as e:
			frappe.throw(e)