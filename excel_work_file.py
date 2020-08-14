import pandas as pd
import os
import xlrd
import openpyxl
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
import xlsxwriter
import datetime
global visits_sheet, patients_sheet

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class Tables():
    def __init__(self):
        self.patients_sheet = pd.read_excel('project_tables.xlsx',header=0,sheet_name='patients', names=['id', 'gender',
             'age', 'date_of_birth', 'origin', 'IgE', 'anti-TPO', 'TSH', 'CRP', 'ANA'])
        self.visits_sheet = pd.read_excel('project_tables.xlsx',index_col=None,header=0,sheet_name='visits', names=['id'
            , 'visit_num', 'visit_date', 'UAS7', 'AH_regular', 'AH_increase','steroids','Cyclosporin','Singular','OMA_300','OMA_450',
             'angioedma','Urticaria','tiredness','Breath_problems','Swallowing_diff','Abdominal_pain','attack_num','IS_currently_active', 'Autopic_back',
             'autoimmune_back','disease_begin_date'])

        self.writer = pd.ExcelWriter("project_tables.xlsx", engine='xlsxwriter')

    def search_patient(self,id_number):
        try:
            id_number = int(id_number)
        except ValueError:
            id_number = 000
        result_dict = {}
        max_visit = None
        try:
            if any(self.patients_sheet.id == id_number):
                result_dict = self.patients_sheet.loc[self.patients_sheet.id == id_number]
                result_dict = result_dict.to_dict(orient='records')[0]
                max_visit = self.visits_sheet.loc[self.visits_sheet.id == id_number]['visit_num'].max() + 1
        except:
            pass
        return result_dict,max_visit

    def add_new_patient(self,patient_dict):
        answer,nothing = self.search_patient(patient_dict['id'])
        if answer:
            # print(patient_dict.keys())
            for key in list(patient_dict.keys())[1:]:
                self.patients_sheet.loc[self.patients_sheet['id'] == patient_dict['id'], key] = patient_dict[key]
                self.patients_sheet.to_excel(self.writer, sheet_name="patients", startrow=0, startcol=0, index=False)
        else:
            print("got here")
            print(patient_dict)
            new_patient_sheet = self.patients_sheet.append(patient_dict,ignore_index=True)
            new_patient_sheet.to_excel(self.writer, sheet_name="patients", startrow=0, startcol=0, index=False)



    def add_new_visit(self, visit_dict):
        print(visit_dict)
        new_visit_sheet = self.visits_sheet.append(visit_dict, ignore_index=True)
        new_visit_sheet.to_excel(self.writer, sheet_name="visits", startrow=0, startcol=0, index=False)

    def save(self):
        self.writer.save()

def get_age(string_date):
    print(string_date)
    try:
        birthDate = datetime.strptime(string_date, '%d/%m/%Y')
        today = datetime.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    except:
        age = "--"
        birthDate = "--"
    return str(age), str(birthDate)
