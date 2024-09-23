# Copyright (c) 2024, shalidnra and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document



class StockItems(Document):
    def before_save(self):
        amount = 0
        
        for item in self.items:
            amount += item.price * item.quantity  

        if amount < 1000:
            self.total_amount = amount 
            adiscount = amount*0.1
            self.payble_amount = amount-adiscount
            self.discount = adiscount
        else:
            self.total_amount = amount
            adiscount = amount*0.2  
            self.payble_amount = amount-adiscount
            self.discount = adiscount
        
        
