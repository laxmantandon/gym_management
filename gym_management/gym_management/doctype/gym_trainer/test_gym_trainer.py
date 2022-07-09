# Copyright (c) 2022, Laxman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymTrainer(FrappeTestCase):
	def test_create_gym_trainer(self):
		doc = self.make_gym_trainer()
		self.assertEqual(doc.first_name, "_Test")

	def make_gym_trainer(self):
		try:
			gym_trainer = frappe.get_doc({
				"doctype": "Gym Trainer",
				"first_name": "_Test",
				"last_name": "_Test Last Name",
				"contact": "+91-9926100041",
				"address_1": "Main Road",
				"city": "Raipur",
				"state": "Chhattisgarh",
				"status": "Lead"
			})
			gym_trainer.insert()
			return gym_trainer

		except Exception as e:
			frappe.throw(e)




