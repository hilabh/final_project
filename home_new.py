from tkinter import *
import tkinter.ttk as ttk
from datetime import datetime, date
import excel_work_file as PT
import matplotlib.pyplot as pl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import tkinter.messagebox as tkm
from PIL import ImageTk, Image
import seaborn as sns
import pandas as pd
X=0
sys.path.append(".")
from pandastable import Table, TableModel
#import login_register

DF = PT.Tables()
visit_df = DF.visits_sheet.copy(deep=True)
patients_df = DF.patients_sheet.copy(deep=True)


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Setup Menu
        MainMenu(self)
        # Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        for i in range(5):
            self.columnconfigure(i, weight=200, minsize=1)
            self.rowconfigure(i, weight=200, minsize=1)
        self.configure(background='#c2dfff')
        """buttons:"""
        page_one = Button(self, text="הוספת מטופל", command=lambda: controller.show_frame(PageOne),
                          font=('Arial', 16)).grid(row=4, column=1,sticky = N)
        page_two = Button(self, text="טבלאות מטופלים", command=lambda: controller.show_frame(PageTwo),
                          font=('Arial', 16)).grid(row=4, column=2,sticky = N)
        page_three = Button(self, text="פילוח מטופלים", command=lambda: controller.show_frame(PageThree),
                            font=('Arial', 16)).grid(row=4, column=3,sticky = N)
        """text1 = Text(self, height = 2, width = 30, font = ('Arial', 18, 'bold'))
        text1.grid(row = 4, column = 2, columnspan = 3)
        text1.insert(END, "ברוכים הבאים")"""
        lable1 = Label(self, text="!ברוכים הבאים", bg='#c2dfff', font=('Arial', 20, 'bold')).grid(row=1, column=2,sticky = N)
        melel = Label(self, text="מערכת לחקר מחלת האורטיקריה", bg='#c2dfff', font=('Arial', 18)).grid(row=2, column=2,sticky = N)
        lable2 = Label(self, text=":אנא בחר את האופציה הרצויה", bg='#c2dfff', font=('Arial', 18)).grid(row=3, column=2,sticky = N)
        # self.img = ImageTk.PhotoImage(Image.open("picture.jpg"))
        self.img = ImageTk.PhotoImage(Image.open('picture.jpg'))
        panel = Label(self, image=self.img)
        panel.grid(row=0, column=1, columnspan=3,pady = 3)

# הוספת מטופל חדש
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        controller.resizable(width=TRUE, height=TRUE)
        for i in range(13):
            self.columnconfigure(i, weight=10, minsize=1)
        for i in range(23):
            self.rowconfigure(i, weight=100, minsize=1)

        controller.geometry('{}x{}'.format(900, 700))
        top_frame = Frame(controller, bg='red', width=450, height=50, pady=3)
        center = Frame(controller, bg='gray2', width=50, height=40, padx=3, pady=3)

        top_frame = Frame(controller, bg='cyan', width=450, height=50, pady=3)
        center = Frame(controller, bg='gray2', width=50, height=40, padx=3, pady=3)

        self.configure(background='#c2dfff')
        label = Label(self, text="הוספת מטופל", font=('Arial', 22, 'bold'), bg='#c2dfff')
        label.grid(row=0, column=5, columnspan=6)
        frame = Frame(self, relief=RAISED, borderwidth=1, bg='#F5F5DC')
        frame.grid(row=5, column=5, columnspan=6, )

        start_page = Button(self, text="          בית", command=lambda: controller.show_frame(StartPage),
                            font=('Arial', 14),
                            bg='#c2dfff', relief="flat", activebackground="#F5F5DC", highlightbackground="Black",
                            cursor="hand2").grid(row=1, column=0, columnspan=6, sticky=W)
        page_three = Button(self, text="   פילוח מטופלים", command=lambda: controller.show_frame(PageThree),
                            font=('Arial', 14), bg='#c2dfff', relief="flat", activebackground="#F5F5DC",
                            highlightbackground="Black", cursor="hand2").grid(row=2, column=0, columnspan=6, sticky=W)
        page_two = Button(self, text=" טבלאות מטופלים", command=lambda: controller.show_frame(PageTwo),
                          font=('Arial', 14), bg='#c2dfff', relief="flat", activebackground="#F5F5DC",
                          highlightbackground="Black", cursor="hand2").grid(row=3, column=0, columnspan=6, sticky=W)

        yScroll = Scrollbar(self, orient=VERTICAL)
        yScroll.grid(row=0, column=23, rowspan=23, sticky=N + S)

        self.id_1 = StringVar()
        self.date_birth = StringVar()
        self.visit_date = StringVar(self, value=str(date.today().strftime('%d/%m/%Y')))
        self.gender = IntVar()
        self.visit_num = IntVar(self, value=0)
        self.origin = StringVar()
        self.UAS7 = IntVar()
        self.ige = IntVar()
        self.anti_tpo = IntVar()
        self.ANA = IntVar()
        self.TSH = IntVar()
        self.CRP = IntVar()
        self.angio = IntVar()
        self.urticaria = IntVar()
        self.Disease_beg_date = StringVar(self, value=str(date.today().strftime('%d/%m/%Y')))
        self.seisure_num = IntVar()
        self.is_attaced_now = IntVar()
        self.autoimmune_back = StringVar(self, " ")
        self.autopic_back = StringVar()
        self.check_ai = IntVar(self, value=0)

        Label(self, text=":ת.ז", font=('Arial', 13), bg='#c2dfff').grid(row=1, column=9, columnspan=1, sticky=E)
        id_entry = Entry(self, textvariable=self.id_1, width="30").grid(row=1, column=8, columnspan=1, sticky=E)
        Button(self, text='בדוק האם מטופל קיים', command=self.check_if_exists, bg="#D3D3D3", font=('Arial', 13)). \
            grid(row=1, column=6, columnspan=2)
        Label(self, text=":תאריך לידה", font=('Arial', 13), bg='#c2dfff').grid(row=2, column=9, columnspan=1, sticky=E)
        date_birth_entry = Entry(self, textvariable=self.date_birth, width="30").grid(row=2, column=8, columnspan=1,
                                                                                      sticky=E)
        visit_date_text = Label(self, font=('Arial', 13), text=":תאריך ביקור", bg='#c2dfff').grid(row=3, column=9,
                                                                                                  columnspan=1,
                                                                                                  sticky=E)
        visit_date_entry = Entry(self, textvariable=self.visit_date, width="30").grid(row=3, column=8, columnspan=1,
                                                                                      sticky=E)
        gender_text = Label(self, text=":מין", font=('Arial', 13), bg='#c2dfff').grid(row=4, column=9, columnspan=1,
                                                                                      sticky=E)
        Radiobutton(self, text=":זכר", font=('Arial', 13), bg='#c2dfff', padx=5, variable=self.gender, value=1).grid(
            row=4, column=6, columnspan=4, )
        Radiobutton(self, text=":נקבה", padx=20, font=('Arial', 13), bg='#c2dfff', variable=self.gender, value=0).grid(
            row=4, column=5
            , columnspan=4, sticky=E)
        visit_num_text = Label(self, text=":מספר ביקור", font=('Arial', 13), bg='#c2dfff').grid(row=3, column=6,
                                                                                                columnspan=2, sticky=E)
        visit_num_entry = Entry(self, textvariable=self.visit_num, width="30").grid(row=3, column=5, columnspan=2,sticky=E)
        origin_text = Label(self, text=":ארץ מוצא", font=('Arial', 13), bg='#c2dfff').grid(row=6, column=9,
                                                                                           columnspan=1, sticky=E)
        origin_entry = Entry(self, textvariable=self.origin, width="30").grid(row=6, column=8, columnspan=1, sticky=E)
        UAS7_text = Label(self, text="UAS7", font=('Arial', 13), bg='#c2dfff').grid(row=7, column=9, columnspan=1,
                                                                                    sticky=E)
        UAS7_entry = Entry(self, textvariable=self.UAS7, width="30").grid(row=7, column=8, columnspan=1, sticky=E)
        labo_test_text = Label(self, text=":בדיקות מעבדה", font=('Arial', 13, 'bold', "underline"), bg='#c2dfff').grid(
            row=8, column=9, columnspan=2)
        ige_text = Label(self, text=":IgE", font=('Arial', 13), bg='#c2dfff').grid(row=9, column=9, columnspan=1)
        ige_entry = Entry(self, textvariable=self.ige, width="10").grid(row=9, column=8, columnspan=1, sticky=E)
        anti_tpo_text = Label(self, text=":anti-TPO", font=('Arial', 13), bg='#c2dfff').grid(row=9, column=7,
                                                                                             columnspan=1)
        anti_tpo_entry = Entry(self, textvariable=self.anti_tpo, width="10").grid(row=9, column=6, columnspan=1,
                                                                                  sticky=E)

        ANA_text = Label(self, text=":ANA", font=('Arial', 13), bg='#c2dfff').grid(row=10, column=7, columnspan=1)
        ANA_entry = Entry(self, textvariable=self.ANA, width="10").grid(row=10, column=6, columnspan=1, sticky=E)

        TSH_text = Label(self, text=":TSH", font=('Arial', 13), bg='#c2dfff').grid(row=9, column=5, columnspan=1)
        TSH_entry = Entry(self, textvariable=self.TSH, width="10").grid(row=9, column=4, columnspan=1, sticky=E)
        CRP_text = Label(self, text=":CRP", font=('Arial', 13), bg='#c2dfff').grid(row=10, column=9, columnspan=1)
        CRP_entry = Entry(self, textvariable=self.CRP, width="10").grid(row=10, column=8, columnspan=1, sticky=E)
        med_treat_text = Label(self, text=":Medical Treatments", font=('Arial', 13, 'bold', 'underline'),
                               bg='#c2dfff').grid(row=12, column=5, columnspan=3)
        self.med_treat_lb = Listbox(self, selectmode=MULTIPLE, width="30", height="7", exportselection=0)
        for item in ['AH-regular dose', 'AH-Increased dose', 'Steroids', 'Cyclosporin', 'Singular', 'oma 300 mg',
                     'oma 450 mg']:
            self.med_treat_lb.insert(END, item)
        self.med_treat_lb.grid(row=13, column=5, columnspan=3, rowspan=4)
        clinique_text = Label(self, text=":Clinique", font=('Arial', 13, 'bold', 'underline'), bg='#c2dfff').grid(
            row=12, column=9, columnspan=1, sticky=E)
        angio_Button = Checkbutton(self, text=":Angioedma", font=('Arial', 13), bg='#c2dfff', variable=self.angio,
                                   onvalue=1, offvalue=0, width="10").grid(row=16, column=9, columnspan=1)
        urticaria_Button = Checkbutton(self, text=":Urticaria", variable=self.urticaria, onvalue=1, offvalue=0,
                                       font=('Arial', 13), bg='#c2dfff', width="10").grid(row=16, column=7,
                                                                                          columnspan=4)
        # is_attacked_now_Button = Checkbutton(self, text="is currently seisured?",font=('Arial',13),bg='#c2dfff', variable=self.is_attaced_now, onvalue=1, offvalue=0,width="15").grid(row=14, column=9, columnspan=1)
        self.symptoms_lb = Listbox(self, selectmode=MULTIPLE, width="30", height="5", exportselection=0)
        for symp in ['עייפות', 'קשיי נשימה', 'קשיי בליעה', 'כאב בטן']:
            self.symptoms_lb.insert(END, symp)
        self.symptoms_lb.grid(row=13, column=8, columnspan=2, sticky=S)
        Disease_beg_date_text = Label(self, text=":תאריך תחילת מחלה", font=('Arial', 13), bg='#c2dfff').grid(row=17,
                                                                                                             column=9,
                                                                                                             sticky=W,
                                                                                                             columnspan=2)
        Disease_beg_date_entry = Entry(self, textvariable=self.Disease_beg_date, width="20").grid(row=17, column=8,
                                                                                                  sticky=W,
                                                                                                  columnspan=1)
        Seisure_num_text = Label(self, text=":מספר התקף", font=('Arial', 13), bg='#c2dfff').grid(row=17, column=5,
                                                                                                 columnspan=2, sticky=W)
        Seisure_num_entry = Entry(self, textvariable=self.seisure_num, width="10").grid(row=17, column=4, sticky=E,
                                                                                        columnspan=1)
        autoimmune_background_entry = Entry(self, textvariable=self.autoimmune_back, width="20")
        autoimmune_background_entry.grid(row=18, column=8, columnspan=2, sticky=W)
        autoimmune_background_text = Label(self, text=":רקע אוטואימוני", font=('Arial', 13), bg='#c2dfff').grid(row=18,
                                                                                                                column=9,
                                                                                                                columnspan=3,
                                                                                                                sticky=W)
        autopic_background_text = Label(self, text=":רקע אוטופי", font=('Arial', 13), bg='#c2dfff').grid(row=19,
                                                                                                         column=9,
                                                                                                         columnspan=3,
                                                                                                         sticky=W)
        autopic_background_entry = Entry(self, textvariable=self.autopic_back, width="20").grid(row=19, column=8,
                                                                                                columnspan=2, sticky=W)

        register = Button(self, text="הכנס למערכת", font=('Arial', 13), width="10", height="2",    command=lambda:[self.save_info()],
                          bg="grey").grid(row=19, column=6, columnspan=1)

        reset = Button(self, text="אפס", font=('Arial', 13), width="10", height="2", bg="grey",
                       command=self.reset_values).grid(row=19, column=5, columnspan=1)

    def check_if_exists(self):
        id_check = self.id_1.get()
        answer, visit = DF.search_patient(id_check)
        if answer and visit:
            tkm.showinfo("ID Found", "תעודת זהות " + id_check + " מטופל קיים במערכת")
            self.id_1.set(answer["id"])
            self.date_birth.set(str(answer['date_of_birth'].strftime('%d/%m/%Y'))) if answer["date_of_birth"] else 0
            self.gender.set(answer["gender"]) if answer["gender"] in [0, 1] else 0
            self.visit_num.set(visit)
            self.origin.set(answer["origin"]) if answer["origin"] else 0
            self.ige.set(answer["IgE"]) if answer["IgE"] else 0
            self.anti_tpo.set(answer["anti-TPO"]) if answer["anti-TPO"] else 0
            self.TSH.set(answer["TSH"]) if answer["TSH"] else 0
            self.CRP.set(answer["CRP"]) if answer["CRP"] else 0
            self.ANA.set(answer["ANA"]) if answer["ANA"] else 0

        else:
            tkm.showinfo("ID Not Found", "מטופל לא קיים במערכת")

    def reset_values(self):
        self.id_1.set("")
        self.date_birth.set("")
        self.visit_date.set(str(date.today().strftime('%d/%m/%Y')))
        self.gender.set(0)
        self.visit_num.set(0)
        self.origin.set("")
        self.UAS7.set(0)
        self.ige.set(0)
        self.anti_tpo.set(0)
        self.ANA.set(0)
        self.TSH.set(0)
        self.CRP.set(0)
        self.angio.set(0)
        self.urticaria.set(0)
        self.Disease_beg_date.set(str(date.today().strftime('%d/%m/%Y')))
        self.seisure_num.set(0)
        self.is_attaced_now.set(0)
        self.autoimmune_back.set("")
        self.autopic_back.set("")
        self.med_treat_lb.selection_clear(0, 'end')
        self.symptoms_lb.selection_clear(0, 'end')

    def save_info(self):
        age, date_birth_info_new = self.get_age(self.date_birth.get())
        med_treat_info = self.med_treat_lb.curselection()
        symptoms_info = self.symptoms_lb.curselection()
        visit_date_new = str(datetime.strptime(self.visit_date.get(), '%d/%m/%Y'))
        begin_date_new = str(datetime.strptime(self.Disease_beg_date.get(), '%d/%m/%Y'))
        pateint_dict = {"id":self.id_1.get(),"gender":self.gender.get(),"date_of_birth":date_birth_info_new,"age":age, "origin":self.origin.get(),
                        "IgE":self.ige.get(), "anti-TPO":self.anti_tpo.get(), "TSH":self.TSH.get(), "CRP":self.CRP.get(), "ANA":self.ANA.get()}
        visit_dict = {"id":self.id_1.get(),"visit_num":self.visit_num.get(),'visit_date':visit_date_new, "UAS7":self.UAS7.get(),'AH_regular': int(0 in med_treat_info), 'AH_increase': int(1 in med_treat_info),
                      'steroids':int(2 in med_treat_info), 'Cyclosporin':int(3 in med_treat_info), 'Singular':int(4 in med_treat_info), 'OMA_300':int(5 in med_treat_info),	'OMA_450':int(6 in med_treat_info),	'angioedma':self.angio.get(),	'Urticaria':self.urticaria.get(),
                      'tiredness':int(0 in symptoms_info),	'Breath_problems':int(1 in symptoms_info),	'Swallowing_diff':int(2 in symptoms_info),
                      'Abdominal_pain':int(3 in symptoms_info), 'attack_num':self.seisure_num.get(), 'IS_currently_active':self.is_attaced_now.get(),
                    'Autopic_back':self.autopic_back.get(), 'autoimmune_back':self.autoimmune_back.get(), 'disease_begin_date':begin_date_new}

        if pateint_dict['id'] == '' or pateint_dict['date_of_birth'] == '--':
            tkm.showinfo("שגיאה", "נא לוודא תעודת זהות ותאריך לידה תקינים")
        else:
            global DF
            DF.add_new_patient(pateint_dict)
            DF.add_new_visit(visit_dict)
            DF.save()
            self.reset_values()
            tkm.showinfo("הרשמה", "מטופל נרשם בהצלחה")
            DF = PT.Tables()
            global visit_df, patients_df
            visit_df = DF.visits_sheet.copy(deep=True)
            patients_df = DF.patients_sheet

    def get_age(self, string_date):
        try:
            birthDate = datetime.strptime(string_date, '%d/%m/%Y')
            today = datetime.today()
            age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        except:
            age = "--"
            birthDate = "--"
        return str(age), str(birthDate)

    def get_gender(self, gender_bin):
        if gender_bin == 1:
            return "Male"
        else:
            return "Female"

# טבאות מטופלים
class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(background='#c2dfff')
        for i in range(9):
            self.columnconfigure(i, weight=200, minsize=1)
            self.rowconfigure(i, weight=200, minsize=1)
        start_page = Button(self, text="          בית", command=lambda: controller.show_frame(StartPage),
                            font=('Arial', 14), bg='#c2dfff', relief="flat", activebackground="#F5F5DC",
                            highlightbackground="Black", cursor="hand2").grid(row=1, column=0, columnspan=1, sticky=W)
        page_one = Button(self, text="  הוספת מטופל", command=lambda: controller.show_frame(PageOne),
                          font=('Arial', 14), bg='#c2dfff', relief="flat", activebackground="#F5F5DC",
                          highlightbackground="Black", cursor="hand2").grid(row=2, column=0, columnspan=1, sticky=W)
        page_three = Button(self, text="  פילוח מטופלים", command=lambda: controller.show_frame(PageThree),
                            font=('Arial', 14), bg='#c2dfff', relief="flat", activebackground="#F5F5DC",
                            highlightbackground="Black", cursor="hand2").grid(row=3, column=0, columnspan=1, sticky=W)

        self.controller = controller
        label = Label(self, text=":ביקורי המטופלים ", font=('Arial', 22, 'bold'), bg='#c2dfff')
        label.grid(row=0, column=4, columnspan=2)
        self.frame = Frame(self, relief=RAISED, borderwidth=1, bg='#F5F5DC')
        self.frame.grid(row=5, column=5, columnspan=6, )

        # here we present the tables

        self.id_entry = StringVar()

        Label(self, text=":הכנס תעודת זהות", font=('Arial', 13), bg='#c2dfff').grid(row=2, column=5, columnspan=1,
                                                                                    sticky=W)
        Entry(self, textvariable=self.id_entry, width="30").grid(row=2, column=4, sticky=E)
        Button(self, text='חפש מטופל', command=self.show_option).grid(row=2, column=3, sticky=E)
        Button(self, text="אפס", font=('Arial', 13), width="10", height="2", bg="grey",
               command=self.reset).grid(row=10, column=2, columnspan=1, sticky=E)


        self.new_dataframe_visits = visit_df.copy(deep=True)
        self.new_dataframe_visits.rename(columns={'id': 'ת.ז', 'visit_num': 'מספר ביקור', 'visit_date': 'תאריך ביקור',
                                                  'AH_regular': 'AH regular dose', 'AH_increase': 'AH increase',
                                                  'OMA_300': 'OMA 300',
                                                  'OMA_450': 'OMA 450', 'tiredness': 'עייפות',
                                                  'Breath_problems': 'קשיי נשימה',
                                                  'Swallowing_diff': 'קשיי בליעה', 'Abdominal_pain': 'כאבי בטן',
                                                  'attack_num': 'מספר התקף'
            , 'IS_currently_active': 'האם בהתקף', 'Autopic_back': 'רקע אטופי', 'autoimmune_back': 'רקע אוטואימוני',
                                                  'disease_begin_date': 'תאריך תחילת מחלה'}, inplace=True)


        amudot = ['AH regular dose', 'AH increase', 'steroids', 'Cyclosporin', 'Singular', 'OMA 300', 'OMA 450',
                  'angioedma', 'Urticaria', 'עייפות', 'קשיי נשימה', 'קשיי בליעה', 'כאבי בטן', 'האם בהתקף', 'רקע אטופי',
                  'רקע אוטואימוני']
        for j in amudot:
            for index, row in self.new_dataframe_visits.iterrows():
                if self.new_dataframe_visits[j][index] == 1:
                    self.new_dataframe_visits[j][index] = 'Yes'
                elif self.new_dataframe_visits[j][index] == 0:
                    self.new_dataframe_visits[j][index] = 'No'


        self.table_frame=Frame(self, relief=SUNKEN, borderwidth=2, bg='#F5F5DC')
        self.table_frame.grid(row=4,column=2,columnspan=12)
        self.pt = Table(self.table_frame, dataframe=self.new_dataframe_visits,height = 350, width = 1000)


        self.pt.autoResizeColumns()
        self.pt.show()



    def show_option(self):
        global visit_df



        self.new_dataframe_visits = visit_df.copy(deep=True)
        self.new_dataframe_visits.rename(columns={'id': 'ת.ז', 'visit_num': 'מספר ביקור', 'visit_date': 'תאריך ביקור',
                                                  'AH_regular': 'AH regular dose', 'AH_increase': 'AH increase',
                                                  'OMA_300': 'OMA 300',
                                                  'OMA_450': 'OMA 450', 'tiredness': 'עייפות',
                                                  'Breath_problems': 'קשיי נשימה',
                                                  'Swallowing_diff': 'קשיי בליעה', 'Abdominal_pain': 'כאבי בטן',
                                                  'attack_num': 'מספר התקף'
            , 'IS_currently_active': 'האם בהתקף', 'Autopic_back': 'רקע אטופי', 'autoimmune_back': 'רקע אוטואימוני',
                                                  'disease_begin_date': 'תאריך תחילת מחלה'}, inplace=True)

        amudot = ['AH regular dose', 'AH increase', 'steroids', 'Cyclosporin', 'Singular', 'OMA 300', 'OMA 450',
                  'angioedma', 'Urticaria', 'עייפות', 'קשיי נשימה', 'קשיי בליעה', 'כאבי בטן', 'האם בהתקף', 'רקע אטופי',
                  'רקע אוטואימוני']
        for j in amudot:
            for index, row in self.new_dataframe_visits.iterrows():
                if self.new_dataframe_visits[j][index] == 1:
                    self.new_dataframe_visits[j][index] = 'Yes'
                elif self.new_dataframe_visits[j][index] == 0:
                    self.new_dataframe_visits[j][index] = 'No'

        identifier = self.id_entry.get()  # get option
        try:
            identifier = int(identifier)
            if (len(visit_df.loc[visit_df['id'] == identifier]) > 0):
                self.pt.close()
                self.pt = Table(self.table_frame, dataframe=self.new_dataframe_visits.loc[visit_df.id == int(identifier)])
                self.pt.show()
            else:
                tkm.showinfo("ID Not Found", "מטופל לא קיים במערכת")
                self.id_entry.set("")
        except:
            tkm.showinfo("ID Not Found", "מטופל לא קיים במערכת")
            self.id_entry.set("")

    def reset(self):
        self.id_entry.set("")
        self.pt.close()
        self.pt = Table(self.table_frame, dataframe=self.new_dataframe_visits)
        self.pt.show()


# פילוח מטופלים
class PageThree(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(background='#c2dfff')
        label = Label(self, text="                     פילוחים סטטסטיים", font=('Arial', 22, 'bold'), bg='#c2dfff')
        label.pack(padx=10, pady=10)
        self.frame = Frame(self, relief=RAISED, borderwidth=1, bg='#F5F5DC')
        self.frame.pack(fill=BOTH, expand=True, side=RIGHT)

        start_page = Button(self, text="בית", command=lambda: controller.show_frame(StartPage), font=('Arial', 14),
                            bg='#c2dfff', relief="flat", activebackground="#F5F5DC", highlightbackground="Black",
                            cursor="hand2",bd = 1).pack(fill="x", pady=10)
        page_one = Button(self, text="הוספת מטופל", command=lambda: controller.show_frame(PageOne), font=('Arial', 14),
                          bg='#c2dfff', relief="flat", activebackground="#F5F5DC", highlightbackground="Black",
                          cursor="hand2",bd = 1).pack(fill="x", pady=10)
        page_two = Button(self, text="טבלאות מטופלים", command=lambda: controller.show_frame(PageTwo),
                          font=('Arial', 14), bg='#c2dfff', relief="flat", activebackground="#F5F5DC",
                          highlightbackground="Black", cursor="hand2",bd = 1).pack(fill="x", pady=10)

        global visit_df, patient_df
        visit_df = DF.visits_sheet
        patient_df = DF.patients_sheet
        Label(self.frame, text='     : בחר את הגרף הרצוי', font=('Arial', 16, 'bold'),bg="#F5F5DC").pack(fill="x", pady=10)

        Button(self.frame, text=' כתלות בזמן UAS-7', font=('Arial', 13), command=self.first_segment).pack(side=TOP, anchor = N)

        Button(self.frame, text='אופן טיפול כתלות במין', font=('Arial', 13), command=self.second_segment).pack(
            side=TOP, anchor = N)  # show option

        reset = Button(self.frame, text= "אפס", font=('Ariel',13),width='10', height='2', bg='grey',command=self.reset_values).pack(side=BOTTOM)

    def first_segment(self):
        global visit_df, patients_df, X
        visit_df = DF.visits_sheet
        patients_df = DF.patients_sheet
        if X==0:
            Label(self.frame, text='        בחר את תעודת הזהות של המטופל/ים', font=('Arial', 13)).pack(fill="x", pady=10,expand=True,side=TOP)
            self.id_entry = StringVar()
            id_entry = Entry(self.frame, textvariable=self.id_entry, width="30").pack()
            Button(self.frame, text='חפש מטופל', command=self.search_patient, bg="#D3D3D3", font=('Arial', 13)).pack()

            self.IDs_lb = Listbox(self.frame, selectmode=MULTIPLE, width="30", height="7", exportselection=0)
            for item in list(patient_df['id']):
                self.IDs_lb.insert(END, item)
            self.IDs_lb.pack(pady=10, expand=True, side=TOP)

            def select_all():
                self.IDs_lb.select_set(0, END)

            Button(self.frame, text='בחר הכל', command=select_all).pack()

            def selection_clear():
                self.IDs_lb.selection_clear(0, END)

            Button(self.frame, text='נקה', command=selection_clear).pack()
            Button(self.frame, text='צור גרף', font=('Arial', 13), command=self.create_first_segment).pack(pady=10, expand=True,side=TOP)
            X+=1
        else:
            self.IDs_lb.selection_clear(0,END)


    def search_patient(self):
        global visit_df, patients_df
        visit_df = DF.visits_sheet
        patients_df = DF.patients_sheet
        id_ = self.id_entry.get()
        index=0
        for gg in list(patient_df['id']):
            if id_==str(gg):
                self.IDs_lb.select_set(index)
                return
            index+=1
        tkm.showinfo("ID Not Found", "מטופל לא קיים במערכת")

    def create_first_segment(self):
        global visit_df, patients_df
        visit_df = DF.visits_sheet
        patients_df = DF.patients_sheet
        self.window = Toplevel(self)
        id_info = self.IDs_lb.curselection()
        new_list = []
        for x in id_info:
            new_list.append(patients_df['id'][x])
        lf = ttk.Labelframe(self.window, text=' לאורך זמן UAS-7 ')
        lf.pack()
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        for id_ in new_list:
            new_df = visit_df.loc[visit_df['id'] == id_][['id', 'UAS7', 'visit_num']]
            if not (new_df.empty):
                new_df.plot(x='visit_num', y='UAS7', ax=ax, marker='o', linestyle='-', label="ID:" + str(id_))

        canvas = FigureCanvasTkAgg(fig, master=lf)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def reset_values(self):
        self.window.destroy()
        self.frame.close()
        self.IDs_lb.selection_clear(0,END)

    def second_segment(self):
        self.window = Toplevel(self)
        lf = ttk.Labelframe(self.window, text=' אופן הטיפול כתלות במין')
        lf.pack()
        listi = []
        for index, rows in visit_df.iterrows():
            for col in ['AH_regular',"AH_increase","steroids" ,"Cyclosporin" ,"Singular","OMA_300","OMA_450"]:
                if rows[col] == 1:
                    gender = int(patients_df[patients_df.id == rows['id']]['gender'])
                    str_gender = 'Female' if gender == 0 else 'Male'
                    dicti = {'gender':str_gender, 'treat':col}
                    listi.append(dicti)
        new_df = pd.DataFrame(listi,columns=['gender', 'treat'])
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        sns.countplot(x='gender',hue='treat',data=new_df, ax=ax)
        canvas = FigureCanvasTkAgg(fig, master=lf)
        canvas.draw()
        canvas.get_tk_widget().pack()


class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        filemenu.add_command(label="logout", command=master.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


def main():
    #login_register.main_screen()
    app = App()
    app.mainloop()

main()

