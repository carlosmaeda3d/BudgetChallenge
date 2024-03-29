from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
import tkinter as tk

class MonthData:
    def __init__(self, wk_month, wk_num, wk_start_date, wk_income, wk_expenses, wk_total):
        self.wk_month = wk_month
        self.wk_num = wk_num
        self.wk_start_date = wk_start_date
        self.wk_income = wk_income
        self.wk_expenses = wk_expenses
        self.wk_total = wk_total

    def __repr__(self):
        return self.wk_month + "," + self.wk_num + "," + self.wk_start_date + "," + self.wk_income + "," \
               + self.wk_expenses + "," + self.wk_total

class WeekData:
    def __init__(self, wk_month, wk_num, wk_item_type, wk_item_name, wk_item_amount):
        self.wk_month = wk_month
        self.wk_num = wk_num
        self.wk_item_type = wk_item_type
        self.wk_item_name = wk_item_name
        self.wk_item_amount = wk_item_amount

    def __repr__(self):
        return self.wk_month + ", " + str(self.wk_num) + ", " + self.wk_item_type + ", " + self.wk_item_name + ", " + \
               str(self.wk_item_amount) + "\n"

class MonthWeeksData:
    def __init__(self, mw_month, mw_start_date, mw_total_weeks):
        self.mw_month = mw_month
        self.mw_start_date = mw_start_date
        self.mw_total_weeks = mw_total_weeks

    def __repr__(self):
        return self.mw_month + ", " + str(self.mw_start_date) + ", " + str(self.mw_total_weeks) + "\n"

class BudgetApp:

    def __init__(self, root):
        #Setting of window
        root.title("Budget")
        root.eval("tk::PlaceWindow . center")

        #Main variables
        intro_text = "HOW TO USE: \n- Start by clicking edit month and input start date and add how many weeks are in " \
                     "the month. \n- Click the week you want to work on, then click edit week to start adding income " \
                     "and expense amounts.\n- To delete weeks, click edit month and change to the amount of weeks " \
                     "you want.\n- To delete income and expense amounts, click the week you want to edit, then " \
                     "click edit week. From there delete the individual amounts."
        bg_green = "#86DB6B"
        dark_green = "#4D5C49"
        months = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
                  "October", "November", "December")
        month_text = StringVar()
        current_month = IntVar()
        tut_play = IntVar()
        month_list = []
        month_weeks_list = []
        week_list = []
        main_selected_week = StringVar()
        # Setting start month
        current_month.set(6)
        month_text.set("July")
        tut_play.set(0)

        def tut_screen():
            if tut_play.get() == 0:
                messagebox.showinfo("How To Use App", intro_text)
                tut_play.set(1)
            else:
                return

        def frame_delete(frame):
            # Destroys all widgets, then destroys frame
            for widget in frame.winfo_children():
                widget.destroy()
            frame.destroy()

        def month_list_creator():
            # Adds week amounts and start date
            weeks = 0
            start_date = datetime

            for m in month_weeks_list:
                if m.mw_month == month_text.get():
                    weeks = m.mw_total_weeks
                    start_date = m.mw_start_date

            # Figures out income and expenses from week list and makes month list from it
            for i in range(weeks):
                total_income = 0
                total_expense = 0

                # Gets start date for each week in range
                if i == 0:
                    new_date = start_date.strftime("%m/%d/%y")
                else:
                    added = i * 7
                    old_date = start_date
                    new = old_date + timedelta(days=added)
                    new_date = new.strftime("%m/%d/%y")

                # Gets income and expense data from week list
                for m in week_list:
                    if m.wk_month == month_text.get():
                        if m.wk_num == i + 1:
                            if m.wk_item_type == "Income":
                                total_income += m.wk_item_amount
                            elif m.wk_item_type == "Expense":
                                total_expense += m.wk_item_amount

                grant_total = total_income - total_expense

                # Creates items for month list and adds them
                new_item = MonthData(month_text.get(), "Week " + str(i + 1), new_date, str(total_income),
                                     str(total_expense), str(grant_total))
                month_list.append(new_item)
            # print(month_list)

        def month_frame():
            frame1 = Frame(root, width=800, height=300, bg=bg_green)
            frame1.grid(row=0, column=0)
            frame1.pack_propagate(False)
            frame1.grid_propagate(False)

            # Clears month list then creates new one so it doesn't keep
            month_list.clear()
            month_list_creator()

            def month_tree_delete():
                # Deletes items in tree
                for item in self.month_tree.get_children():
                    self.month_tree.delete(item)

            def prev_month():
                month = current_month.get()
                month -= 1

                # If it gets to end of month, it starts from 0
                if month == 12:
                    month = 0
                    current_month.set(month)
                else:
                    current_month.set(month)

                # Changes month text to new month
                month_text.set(months[current_month.get()])

                # Clears month list then creates new one so it doesn't keep
                month_list.clear()
                month_list_creator()

                # Deletes items in tree and adds new month
                month_tree_delete()
                for i in month_list:
                    if i.wk_month == month_text.get():
                        self.month_tree.insert("", "end",
                                               values=(i.wk_num, i.wk_start_date, i.wk_income, i.wk_expenses, i.wk_total))

            def next_month():
                month = current_month.get()
                month += 1

                # If it gets to end of month, it starts from 0
                if month == 12:
                    month = 0
                    current_month.set(month)
                else:
                    current_month.set(month)

                # Changes month text to new month
                month_text.set(months[current_month.get()])

                # Clears month list then creates new one so it doesn't keep
                month_list.clear()
                month_list_creator()

                # Deletes items in tree and adds new month
                month_tree_delete()
                for i in month_list:
                    if i.wk_month == month_text.get():
                        self.month_tree.insert("", "end", values=(i.wk_num, i.wk_start_date, i.wk_income, i.wk_expenses,
                                                                  i.wk_total))

            def edit_month():
                frame_delete(frame1)
                edit_month_frame()

            def week_info():
                week_selected = self.month_tree.focus()
                week_value = self.month_tree.item(week_selected, 'values')
                if week_value == "":
                    messagebox.showinfo("Error", "No Week Selected!")
                    return
                else:
                    main_selected_week.set(week_value[0])
                    frame_delete(frame1)
                    week_frame()

            # Labels
            month_label = tk.Label(frame1, textvariable=month_text, font=("TkHeadingFont", 28, "bold", "underline"),
                                   fg=dark_green, bg=bg_green)
            month_label.pack(pady=10)
            month_text.set(months[current_month.get()])

            # Buttons
            prev_month_button = tk.Button(frame1, text="Previous Month", font=("TkHeadingFont", 11), bg=dark_green,
                                          fg="white", width=13, cursor="hand2", command=prev_month)
            new_month_button = tk.Button(frame1, text="Next Month", font=("TkHeadingFont", 11), bg=dark_green,
                                         fg="white", width=13, cursor="hand2", command=next_month)
            edit_month_button = tk.Button(frame1, text="Edit Month", font=("TkHeadingFont", 11), bg=dark_green,
                                          fg="white", cursor="hand2", width=10, height=4, command=edit_month)
            week_info_button = tk.Button(frame1, text="Week Info", font=("TkHeadingFont", 11), bg=dark_green,
                                         fg="white", cursor="hand2", width=20, height=2, command=week_info)

            prev_month_button.place(x=10, y=20)
            new_month_button.place(x=665, y=20)
            edit_month_button.place(x=650, y=120)
            week_info_button.place(x=300, y=240)

            # TREEVIEW::::: Define Columns
            tree_columns = ("wk_num", "wk_start_date", "wk_income", "wk_expenses", "wk_total")

            self.month_tree = ttk.Treeview(frame1, columns=tree_columns, show="headings", height=5)

            # Define Headings
            self.month_tree.heading("wk_num", text="Week #")
            self.month_tree.heading("wk_start_date", text="Start Date")
            self.month_tree.heading("wk_income", text="Income")
            self.month_tree.heading("wk_expenses", text="Expenses")
            self.month_tree.heading("wk_total", text="Totals")

            # Creates widths for each column
            for tree_column in tree_columns:
                self.month_tree.column(column=tree_column, width=80)

            # Inserts Data
            for i in month_list:
                if i.wk_month == month_text.get():
                    self.month_tree.insert("", "end", values=(i.wk_num, i.wk_start_date, i.wk_income, i.wk_expenses,
                                                              i.wk_total))

            # Creates grid
            self.month_tree.grid(row=0, column=0, sticky="n e s w", pady=100, padx=200)

            #Tutorial part
            tut_screen()

        def week_frame():
            frame2 = Frame(root, width=800, height=300, bg=bg_green)
            frame2.grid(row=0, column=0)
            frame2.pack_propagate(False)
            frame2.grid_propagate(False)

            def week_trees_delete():
                # Deletes items in tree
                for item in self.income_tree.get_children():
                    self.income_tree.delete(item)

                for item in self.expense_tree.get_children():
                    self.expense_tree.delete(item)

            def income_clicker(event):
                # Clears entries
                name_input.set("")
                amount_input.set("")
                type_select.set("")
                self.expense_tree.selection_toggle(self.expense_tree.selection())


                # Grab the record number
                selected = self.income_tree.focus()
                # Grab record values
                values = self.income_tree.item(selected, "values")
                # Output to entry boxes. It first checks if is selected, else deselect to prevent index range error
                if len(self.income_tree.selection()) > 0:
                    name_input.set(values[0])
                    amount_input.set(values[1])
                    type_select.set("Income")
                else:
                    clear_item()

            def expense_clicker(event):
                # Clears entries and selections
                name_input.set("")
                amount_input.set("")
                type_select.set("")
                self.income_tree.selection_toggle(self.income_tree.selection())

                # Grab the record number
                selected = self.expense_tree.focus()

                # Grab record values
                values = self.expense_tree.item(selected, "values")

                # Output to entry boxes. It first checks if is selected, else deselect to prevent index range error
                if len(self.expense_tree.selection()) > 0:
                    name_input.set(values[0])
                    amount_input.set(values[1])
                    type_select.set("Expense")
                else:
                    clear_item()

            def delete_item():
                # Figures out what is selected and deletes. Gives error message is nothing is selected
                if len(self.income_tree.selection()) > 0 or len(self.expense_tree.selection()) > 0:
                    if len(self.income_tree.selection()) > 0:
                        selected = self.income_tree.selection()[0]
                        values = self.income_tree.item(selected, "values")
                        for i in week_list:
                            if i.wk_month == month_text.get() and i.wk_num == int(main_selected_week.get()[5]) \
                                    and i.wk_item_type == "Income":
                                if i.wk_item_name == values[0] and i.wk_item_amount == int(values[1]):
                                    week_list.remove(i)
                        self.income_tree.delete(selected)

                    elif len(self.expense_tree.selection()) > 0:
                        selected = self.expense_tree.selection()[0]
                        values = self.expense_tree.item(selected, "values")
                        for i in week_list:
                            if i.wk_month == month_text.get() and i.wk_num == int(main_selected_week.get()[5]) \
                                    and i.wk_item_type == "Expense":
                                if i.wk_item_name == values[0] and i.wk_item_amount == int(values[1]):
                                    week_list.remove(i)
                        self.expense_tree.delete(selected)
                else:
                    messagebox.showinfo("Error", "No item selected")
                    return

                # Clear inputs
                clear_item()

            def clear_item():
                name_input.set("")
                amount_input.set("")
                type_select.set("")
                self.income_tree.selection_toggle(self.income_tree.selection())
                self.expense_tree.selection_toggle(self.expense_tree.selection())

            def save_item():
                # Gives error if anything other than int is used in item amount
                try:
                    val = int(amount_input.get())
                except:
                    messagebox.showinfo("Error", "AMOUNT: Need to input a number")
                    return

                #\\\\\\\\\\\THINK OF A BETTER WAY FOR MAKING SURE NOT BLANK!! CAN BYPASS WITH SPACE!!!///////////////
                # Gives error if name is blank
                if name_input.get() in ("", " ", "  "):
                    messagebox.showinfo("Error", "NAME: Can't leave this item blank")
                    return

                if type_select.get() == "":
                    messagebox.showinfo("Error", "Type: Can't leave this item blank")
                    return

                # Gives error if name matches another name in week. If not it will cause issue with deleting
                for i in week_list:
                    if i.wk_month == month_text.get() and i.wk_num == int(main_selected_week.get()[5]) \
                            and i.wk_item_type == type_select.get() and i.wk_item_name == name_input.get():
                        messagebox.showinfo("Error", "NAME: Please rename. Can't match name from week.")
                        return

                # Adding item to week list
                new_item = WeekData(month_text.get(), int(main_selected_week.get()[5]), type_select.get(),
                                    name_input.get(), int(amount_input.get()))
                week_list.append(new_item)

                # Deletes trees and resets them
                week_trees_delete()
                for i in week_list:
                    if i.wk_month == wk_frame_month.get():
                        if i.wk_num == wk_frame_week.get():
                            if i.wk_item_type == "Income":
                                self.income_tree.insert("", "end", values=(i.wk_item_name, i.wk_item_amount))
                            elif i.wk_item_type == "Expense":
                                self.expense_tree.insert("", "end", values=(i.wk_item_name, i.wk_item_amount))

                # Clear inputs
                clear_item()
                # print(week_list)

            def back_month():
                frame_delete(frame2)

                # Clears month list then creates new one so it doesn't keep
                month_list.clear()
                month_list_creator()

                month_frame()

            #Labels
            week_label_text = StringVar()
            week_label = tk.Label(frame2, textvariable=week_label_text, font=("TkHeadingFont", 20, "bold", "underline"),
                                  fg=dark_green, bg=bg_green)

            income_label = tk.Label(frame2, text="Income", font=("TkHeadingFont", 20, "bold"),
                                  fg=dark_green, bg=bg_green)

            expenses_label = tk.Label(frame2, text="Expenses", font=("TkHeadingFont", 20, "bold"),
                                    fg=dark_green, bg=bg_green)

            edit_label = tk.Label(frame2, text="New/Edit Item", font=("TkHeadingFont", 15, "bold", "underline"),
                                      fg=dark_green, bg=bg_green)

            week_label.pack(pady=10)
            income_label.place(x=100, y=50)
            expenses_label.place(x=300, y=50)
            edit_label.place(x=600, y=50)

            # Week number string
            week_label_text.set(main_selected_week.get())

            # Labels-Edit Item Area
            edit_labels_xstart = 640
            edit_labels_ystart = 95
            type_label = tk.Label(frame2, text="Type:", font=("TkHeadingFont", 11, "bold", "underline"),
                                      fg=dark_green, bg=bg_green)
            name_label = tk.Label(frame2, text="Name:", font=("TkHeadingFont", 11, "bold", "underline"),
                                  fg=dark_green, bg=bg_green)
            amount_label = tk.Label(frame2, text="Amount:", font=("TkHeadingFont", 11, "bold", "underline"),
                                  fg=dark_green, bg=bg_green)

            type_label.place(x=edit_labels_xstart, y=edit_labels_ystart, anchor=E)
            name_label.place(x=edit_labels_xstart, y=edit_labels_ystart + 35, anchor=E)
            amount_label.place(x=edit_labels_xstart, y=edit_labels_ystart + 70, anchor=E)


            # Buttons
            back_button = tk.Button(frame2, text="Month Sheet", font=("TkHeadingFont", 11), bg=dark_green,
                                          fg="white", width=13, cursor="hand2", command=back_month)
            save_button = tk.Button(frame2, text="Save", font=("TkHeadingFont", 11), bg=dark_green,
                                    fg="white", width=6, cursor="hand2", command=save_item)
            clear_button = tk.Button(frame2, text="Clear", font=("TkHeadingFont", 11), bg=dark_green,
                                    fg="white", width=6, cursor="hand2", command=clear_item)
            delete_button = tk.Button(frame2, text="Delete", font=("TkHeadingFont", 11), bg=dark_green,
                                    fg="white", width=6, cursor="hand2", command=delete_item)
            back_button.place(x=50, y=250)
            save_button.place(x=600, y=200)
            clear_button.place(x=680, y=200)
            delete_button.place(x=600, y=250)

            # Combobox & Entries
            type_select = StringVar()
            name_input = StringVar()
            amount_input = StringVar()

            name_entry = tk.Entry(frame2, width=20, textvariable=name_input)
            amount_entry = tk.Entry(frame2, width=20, textvariable=amount_input)

            type_chooser = ttk.Combobox(frame2, width=10, state="readonly", textvariable=type_select)
            type_chooser["values"] = ["Income", "Expense"]

            type_chooser.place(x=edit_labels_xstart + 10, y=edit_labels_ystart, anchor=W)
            name_entry.place(x=edit_labels_xstart + 10, y=edit_labels_ystart + 35, anchor=W)
            amount_entry.place(x=edit_labels_xstart + 10, y=edit_labels_ystart + 70, anchor=W)

            # Treeviews
            # TREEVIEW::::: Define Columns
            wk_frame_month = StringVar()
            wk_frame_month.set(month_text.get())
            wk_frame_week = IntVar()
            wk_frame_week.set(int(main_selected_week.get()[5]))

            income_tree_columns = ("income_item_name", "income_item_amount")
            expense_tree_columns = ("expense_item_name", "expense_item_amount")

            self.income_tree = ttk.Treeview(frame2, columns=income_tree_columns, show="headings", height=5,
                                            selectmode="browse")
            self.expense_tree = ttk.Treeview(frame2, columns=expense_tree_columns, show="headings", height=5,
                                             selectmode="browse")

            # Define Headings
            self.income_tree.heading("income_item_name", text="Item Name")
            self.income_tree.heading("income_item_amount", text="Amount")
            self.expense_tree.heading("expense_item_name", text="Item Name")
            self.expense_tree.heading("expense_item_amount", text="Amount")


            # Creates widths for each column
            for tree_column in income_tree_columns:
                self.income_tree.column(column=tree_column, width=80)

            for tree_column in expense_tree_columns:
                self.expense_tree.column(column=tree_column, width=80)

            # Inserts Data
            for i in week_list:
                if i.wk_month == wk_frame_month.get():
                    if i.wk_num == wk_frame_week.get():
                        if i.wk_item_type == "Income":
                            self.income_tree.insert("", "end", values=(i.wk_item_name, i.wk_item_amount))
                        elif i.wk_item_type == "Expense":
                            self.expense_tree.insert("", "end", values=(i.wk_item_name, i.wk_item_amount))

            # Binding trees to text boxes with single click using button release. NO SINGLE CLICK ACTION
            # Double click bind is "<Double-1>"
            self.income_tree.bind("<ButtonRelease-1>", income_clicker)
            self.expense_tree.bind("<ButtonRelease-1>", expense_clicker)

            # Creates grid
            self.income_tree.place(x=75, y=100)
            self.expense_tree.place(x=290, y=100)



        def edit_month_frame():
            frame3 = Frame(root, width=400, height=200, bg=bg_green)
            frame3.grid(row=0, column=0)
            frame3.pack_propagate(False)
            frame3.grid_propagate(False)

            def save_month():
                # Check to see if date is in correct format
                try:
                    datetime.strptime(date_input.get(), "%m/%d/%y")
                except:
                    messagebox.showinfo("Error", "Needs to be in correct date format. MM/DD/YY")
                    return

                if week_sel_combo.get() == "":
                    messagebox.showinfo("Error", "Need to select how many weeks")
                    return

                # First checks if month data is already there, if so it updated the data, else it adds inputs
                #   to month_weeks list
                on_list = 0
                new_item = MonthWeeksData(month_text.get(), datetime.strptime(date_input.get(), "%m/%d/%y"),
                                          int(week_sel_combo.get()))

                for idx, i in enumerate(month_weeks_list):
                    if i.mw_month == month_text.get():
                        on_list += 1
                        # Update month-week list
                        month_weeks_list[idx] = new_item

                if on_list == 0:
                    # Add new item to month-week list
                    month_weeks_list.append(new_item)

                # Removes any data from week_list if changes made to week amounts
                for w in list(week_list):
                    if w.wk_month == month_text.get() and w.wk_num > int(week_sel_combo.get()):
                        week_list.remove(w)

                # Goes back to month sheet
                frame_delete(frame3)
                month_list.clear()
                month_list_creator()
                month_frame()

            def back_month():
                frame_delete(frame3)

                # Clears month list then creates new one so it doesn't keep
                month_list.clear()
                month_list_creator()

                month_frame()

            # Header
            frame_label = tk.Label(frame3, text="Edit Month", font=("TkHeadingFont", 20, "bold", "underline"),
                                      fg=dark_green, bg=bg_green)
            frame_label.pack()

            # Start Month Date
            date_input = StringVar()

            start_label = tk.Label(frame3, text="Start Date", font=("TkHeadingFont", 13, "bold", "underline"),
                                      fg=dark_green, bg=bg_green)
            start_input = tk.Entry(frame3, width=15, justify="center", textvariable=date_input)
            start_label.place(x=40, y=50)
            start_input.place(x=35, y=80)

            # How many weeks drop down
            many_weeks_label = tk.Label(frame3, text="How many weeks?", font=("TkHeadingFont", 13, "bold", "underline"),
                                fg=dark_green, bg=bg_green)
            week_sel_combo = ttk.Combobox(frame3, width=5, state="readonly")
            week_sel_combo["values"] = [1, 2, 3, 4, 5]
            many_weeks_label.place(x=210, y=50)
            week_sel_combo.place(x=260, y=80)

            # Buttons
            back_button = tk.Button(frame3, text="Month Sheet", font=("TkHeadingFont", 11), bg=dark_green,
                                    fg="white", width=13, cursor="hand2", command=back_month)

            save_button = tk.Button(frame3, text="Save", font=("TkHeadingFont", 11), bg=dark_green,
                                    fg="white", width=13, cursor="hand2", command=save_month)
            save_button.place(x=130, y=115)
            back_button.place(x=130, y=160)

            # Making sure if month is already made, it puts current weeks and date in there
            for c in month_weeks_list:
                if c.mw_month == month_text.get():
                    date = datetime.strftime(c.mw_start_date, "%m/%d/%y")
                    week_sel_combo.set(c.mw_total_weeks)
                    date_input.set(date)

        month_frame()
        # week_frame()
        # edit_month_frame()

# Initualize app
root = Tk()
BudgetApp(root)
root.mainloop()
