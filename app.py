# coding:utf-8
import shuffler
import customtkinter as ctk
from os.path import exists


app_config = {
    "title": "Repart Group",
    "width": 475,
    "height": 475
}


class App(ctk.CTk):
   
    def __init__(self):
        super().__init__()
        self.title(app_config['title'])
        self.geometry(f"{app_config['width']}x{app_config['height']}")
        self.resizable(width=False, height=False)

        self.all_students = list()


    def add_student(self, key):
        if key.keysym.lower() == "return":
            student = self.new_student_input.get()
            if student.strip(" ") != "":
                self.all_students.append(student)
            
                if exists("datas/students.txt"):
                    with open("datas/students.txt", "a+", encoding="utf8") as register:
                        content = register.read()
                        content += student + "\n"
                        register.write(content)
                        register.close()
                else:
                    register = open('datas/students.txt', "w+", encoding="utf8")
                    register.write(student + "\n")
                    register.close()
                
                self.new_student_input.delete(0, 'end')
                self.update_old_students_box()


    def update_old_students_box(self):
        if exists("datas/students.txt"):
            for widget in self.old_students_box.winfo_children():
                widget.destroy()
            with open("datas/students.txt", "r", encoding="utf8") as register:
                students = register.readlines()
                row = 0
                for student in students.__reversed__():
                    student = student.replace("\n", "")
                    if student.strip(" ") != "":
                        ctk.CTkLabel(self.old_students_box, text=student, font=("Inter", 16)).grid(row=row, column=0, padx=15, pady=(5, 0), sticky='nw')
                    row += 1
                register.close()

    def start_shuffle(self):
        if exists("datas/students.txt"):
            with open("datas/students.txt") as register:
                students_, students = register.readlines(), list()
                for line in students_:
                    line = line.replace("\n", "")
                    if line.strip(" ") != "":
                        students.append(line)
                register.close()
        
            step = self.step_input.get()
            if step.strip(" ") != "":
                step = int(step)
                groups = shuffler.run(students, step)

                groups_toplevel = ctk.CTkToplevel(self)
                groups_toplevel.title(f"({len(groups)}) Groupes")
                groups_toplevel.geometry(f"{app_config['width']}x{app_config['height']}")
                groups_toplevel.resizable(width=False, height=False)
                groups_toplevel.columnconfigure(0, weight=1)
                groups_toplevel.rowconfigure(0, weight=1)

                frame = ctk.CTkScrollableFrame(groups_toplevel)
                frame.grid(row=0,column=0,sticky='nwse', ipadx=30, ipady=30, padx=30, pady=30)
                frame.columnconfigure(0, weight=1)

                i1 = 0
                for group in groups:
                    i2 = 1
                    frame_ = ctk.CTkFrame(frame)
                    frame_.grid(row=i1,column=0,sticky='nwse', ipadx=30, ipady=5, pady=(0, 15))

                    ctk.CTkLabel(frame_, text=f"[Groupe {i1+1}]", font=("inter Bold", 16)).grid(row=0, column=0, sticky="nw", pady=(0, 5))
                    i1 += 1
                    
                    for student in group:
                        ctk.CTkLabel(frame_, text=student, font=("Inter", 16)).grid(row=i2, column=0, sticky="nw")
                        i2 += 1

                groups_toplevel.mainloop()

    def build(self):

        self.columnconfigure(0, weight=1)

        self.new_student_input = ctk.CTkEntry(self, placeholder_text="Le nom d'un étudiant", font=("Inter", 16))
        self.new_student_input.grid(row=0, column=0, sticky='nwse', padx=30, pady=(30, 0), ipady=5, columnspan=2)

        self.step_input = ctk.CTkEntry(self, placeholder_text="Pas", font=("Inter", 16))
        self.step_input.grid(row=1, column=1, sticky='nwse', padx=(15,30), pady=(15, 0), ipady=5)

        started_button = ctk.CTkButton(self, text="Générer des groupes", font=("Inter", 16), command=self.start_shuffle)
        started_button.grid(row=1, column=0, sticky='nwse', padx=(30,15), pady=(15, 0), ipady=5)

        self.old_students_box = ctk.CTkScrollableFrame(self)
        self.old_students_box.grid(row=2, column=0, sticky='nwse', padx=30, pady=(30, 0), ipady=5, columnspan=2)

        def empty_old_students_box():
            open('datas/students.txt', "w+", encoding="utf8").close()
            self.update_old_students_box()
            
        empty_old_students_box = ctk.CTkButton(self, text="Vider", font=("Inter", 16), fg_color="#b00020", hover_color="#c00020", command=empty_old_students_box)
        empty_old_students_box.grid(row=3, column=0, sticky='nwse', padx=30, pady=(30, 0), ipady=5, columnspan=2)

        
        self.update_old_students_box()
        self.bind("<Key>", self.add_student)
        self.mainloop()


if __name__ == '__main__':
    App().build()