# Copyright (c) 2024, shalidnra and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Students(Document):  
    def validate(self):
        total_marks = 0
        subject_count = 0
        
        for subject in self.subjects:
            total_marks += subject.score  
            subject_count += 1
        
        if subject_count > 0:
            self.percent = (total_marks / (subject_count * 100)) * 100 
