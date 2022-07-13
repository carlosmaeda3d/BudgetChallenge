from tkinter import *
from tkinter import ttk
import tkinter as tk

class MonthData:
    def __init__(self, wk_month, wk_num, wk_range, wk_income, wk_expenses, wk_total):
        self.wk_month = wk_month
        self.wk_num = wk_num
        self.wk_range = wk_range
        self.wk_income = wk_income
        self.wk_expenses = wk_expenses
        self.wk_total = wk_total

class BudgetApp:

    def __init__(self, root):
        #Main variables
        bg_green = "#86DB6B"
        dark_green = "#4D5C49"

        #Setting of window and frame
        root.title("Budget")
        root.eval("tk::PlaceWindow . center")
        frame1 = Frame(root, width=800, height=300, bg=bg_green)
        frame1.grid(row=0, column=0)

        def prev_month():
            print("Previous Month")

        def next_month():
            print("Next Month")

        def edit_month():
            print("Edit Month")

        def new_week():
            print("New Week")

        def week_info():
            print("Week Info")

        def month_frame():
            frame1.pack_propagate(False)
            frame1.grid_propagate(False)

            # Labels
            month_text = StringVar()
            month_label = tk.Label(frame1, textvariable=month_text, font=("TkHeadingFont", 28, "bold"), fg=dark_green,
                                  bg=bg_green)
            month_label.pack(pady=10)
            month_text.set("July")

            # Buttons
            prev_month_button = tk.Button(frame1, text="Previous Month", font=("TkHeadingFont", 11), bg=dark_green,
                                          fg="white", width=13, cursor="hand2", command=prev_month)
            new_month_button = tk.Button(frame1, text="Next Month", font=("TkHeadingFont", 11), bg=dark_green,
                                         fg="white", width=13, cursor="hand2", command=next_month)
            edit_month_button = tk.Button(frame1, text="Edit Month", font=("TkHeadingFont", 11), bg=dark_green,
                                          fg="white", cursor="hand2", width=10, height=4, command=edit_month)
            new_week_button = tk.Button(frame1, text="New Week", font=("TkHeadingFont", 11), bg=dark_green,
                                          fg="white", cursor="hand2", width=10, height=2, command=new_week)
            week_info_button = tk.Button(frame1, text="Week Info", font=("TkHeadingFont", 11), bg=dark_green,
                                          fg="white", cursor="hand2", width=10, height=2, command=week_info)

            prev_month_button.place(x=10, y=20)
            new_month_button.place(x=665, y=20)
            edit_month_button.place(x=650, y=120)
            new_week_button.place(x=300, y=240)
            week_info_button.place(x=400, y=240)

            # Lists & Listboxes
            month_list = [
                MonthData("July_22", "Week 1", "Test Range", 2000, 1000, 1000),
                MonthData("July_22", "Week 2", "Test Range", 2000, 1000, 1000),
                MonthData("July_22", "Week 3", "Test Range", 2000, 1000, 1000),
                MonthData("July_22", "Week 4", "Test Range", 2000, 1000, 1000)
            ]

            # Define Columns
            tree_columns = ("wk_num", "wk_range", "wk_income", "wk_expenses", "wk_total")

            tree = ttk.Treeview(frame1, columns=tree_columns, show="headings", height=5)

            # Define Headings
            tree.heading("wk_num", text="Week #")
            tree.heading("wk_range", text="Range")
            tree.heading("wk_income", text="Income")
            tree.heading("wk_expenses", text="Expenses")
            tree.heading("wk_total", text="Totals")

            # Creates widths for each column
            for tree_column in tree_columns:
                tree.column(column=tree_column, width=80)

            # Inserts Data
            for i in month_list:
                tree.insert("", "end", values=(i.wk_num, i.wk_range, i.wk_income, i.wk_expenses, i.wk_total))

            # Creates grid
            tree.grid(row=0, column=0, sticky="n e s w", pady=100, padx=200)

        month_frame()

#initualize app
root = Tk()
BudgetApp(root)
root.mainloop()
