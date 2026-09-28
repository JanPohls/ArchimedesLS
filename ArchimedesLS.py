from tkinter import OptionMenu, Button, Checkbutton,  Label, Entry, Text, Menu, Frame
from tkinter import Tk, Toplevel
from tkinter import INSERT, END, RIDGE, NORMAL, DISABLED
from tkinter import messagebox, filedialog
from tkinter import StringVar, IntVar, DoubleVar, BooleanVar
from tkinter import font as tkFont
#from tkinter import colorchooser

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import numpy as np



class FullScreenApp(object):
    def __init__(self, screen, **kwargs):
        """
        Change to fullscreen
        Input:
        -------------------
        screen: computer screen
        """

        self.screen = screen
        edge = 3
        self._small = '400x200+0+0'
        screen.geometry("{0}x{1}+0+0".format(
            screen.winfo_screenwidth() - edge, screen.winfo_screenheight() - edge))
        screen.bind('<Escape>', self.toggle_screen)


    def toggle_screen(self, event):
        small = self.screen.winfo_geometry()
        self.screen.geometry(self._small)
        self._small = small


    def screen_dim(self):
        """
        Get dimensions of screen

        Output:
        -----------------
        screenheight, screenwidth: int
            Height and width of screen
        """
        return self.screen.winfo_screenheight(), self.screen.winfo_screenwidth()



class Help:
    """
    Produce help windows
    """
    def __init__(self):
        self.screen_help = Toplevel()
        self.screen_help.configure(bg = MainApplication._from_rgb(self, (241, 165, 193)))
        self.screen_help.geometry('700x300')
        self.screen_help.iconbitmap('icon_spb.ico')

    def welcome(self):
        """
        Welcome window
        """
        text = Text(self.screen_help, height=15)
        text.insert(INSERT, 'Welcome to Archimedes LS! Compute the density of liquids and solids including uncertainty using the Archimedes Principle. \n')
        text.insert(INSERT, '\n')
        text.insert(INSERT, '\n')
        text.insert(END, 'You can calculate the density of the liquid using standards! The density can change with temperature and composition. Please check  out the documentaries for more information!  \n \n Thank you for choosing the Rietica Refinement Plot App!')
        text.grid(row=0, column=0, padx=10, pady=(30, 10))

    def documentary(self, *args):
        """
        Documentary window
        """
        text = Text(self.screen_help, height=15)
        text.insert(INSERT, 'Welcome to Archimedes LS App! \n')
        text.insert(INSERT, '\n')
        text.insert(END, 'Please read the documentations or send an email to: \n Jan.Pohls@unb.ca \n')
        text.grid(row=0, column=0, padx=10, pady=(30, 10))

    def about(self):
        """
        About window
        """
        text = Text(self.screen_help)
        text.insert(INSERT, 'This is a program to calculate the density of liquid and solid samples using the Archmimedes principle. \n')
        text.insert(INSERT, '\n')
        text.insert(INSERT, 'The software was written in Python and Tkinter!  This is version v1.0 and I am  looking for any suggestions and reports of errors. \n')
        text.insert(INSERT, '\n')
        text.insert(INSERT, 'This is a free software and should not be used for commercial reasons. \n')
        text.insert(INSERT, '\n')
        text.insert(INSERT, 'If you have suggestions, concerns, or find errors, please send me an email: \n Jan.Pohls@unb.ca \n ')
        text.insert(INSERT, '\n')
        text.insert(INSERT, 'Thank you for choosing the Archimedes LS App. \n \n  --Jan-- \n \n')
        text.insert(INSERT,  '\xa9 Jan-Hendrik Poehls, PhD, MSc, BSc, 2026')
        text.grid(row=0, column=0, padx=10, pady=(30, 10))



class EntryItem:
    """
    Create an entry widget in Tkinter including a label

    Input:
    --------------------------
    parent: parent
        window
    name: str
        name of the entry
    row: int
        row in the window
    column: int
        column in the window
    padx: int
        pixels to pad widget horizontally
    pady: int
        pixels to pad widget vertically
    width: int
        width of the widget
    columnspan: int
        number of columns widget takes up
    state: str
        Normal or disabled
    ipadx: int
        pixels to pad widget horizontally inside the widget's borders
    options: list
        list of different options
    """
    def __init__(self, parent, name, row=0, column=1, padx=10, pady=6, width=20, columnspan=1, state=NORMAL, ipadx=0, options=['0']):
        self.parent = parent
        self.name = name
        self.row = row
        self.column = column
        self.padx = padx
        self.pady = pady
        self.width = width
        self.columnspan = columnspan
        self.state = state
        self.ipadx = ipadx
        self.options = options
        self.initial_val = StringVar()
        self.var = StringVar()
        self.entry = Entry(self.parent, textvariable=self.var, state=self.state, width=self.width)
        self.label = Label(self.parent, text=name, relief=RIDGE, anchor='w')
        self.menu = OptionMenu(self.parent, self.initial_val, *self.options)


    def create_EntryItem(self, padx_label=10, pady_label=6, ipadx_label=0):
        """
        Create entry widget

        Input:
        --------------------------
        padx_label: int
            pixels to pad widget horizontally of the label
        pady_label: int
            pixels to pad widget vertically of the label
        ipadx_label: int
            pixels to pad widget horizontally inside the widget's borders
        """
        self.entry.grid(row=self.row, column=self.column, columnspan=self.columnspan, padx=self.padx, pady=self.pady, ipadx=self.ipadx)
        self.label.grid(row=self.row, column=self.column-1, columnspan=self.columnspan, padx=padx_label, pady=pady_label, ipadx=ipadx_label)


    def set_name(self, new_name='NaN'):
        """
        Change the variable name

        Input:
        ------------------------
        new_name: str
            Name of the variable
        """
        self.var.set(new_name)


    def get_name(self):
        """
        Get the name of the entry
        """
        return self.var.get()


    def delete(self):
        """
        Delete the entry
        """
        self.entry.delete(0, END)


    def entry_forget(self):
        """
        Remove entry from grid
        """
        self.entry.grid_forget()


    def set_menu(self, name):
        """
        Change the initial value of a menu widget

        Input:
        ------------------------
        name: str
            name of the initial value for the menu widget
        """
        self.initial_val.set(name)


    def set_entry(self):
        """
        Place entry widget on the window
        """
        self.entry.grid(row=self.row, column=self.column, columnspan=self.columnspan, padx=self.padx, pady=self.pady, ipadx=self.ipadx)


    def set_label(self, padx_label=10, pady_label=6, ipadx_label=0):
        """
        Place the label widget on the window

        Input:
        -------------------
        padx_label: int
            pixels to pad widget horizontally of the label
        pady_label: int
            pixels to pad widget vertically of the label
        ipadx_label: int
            pixels to pad widget horizontally inside the widget's borders
        """
        self.label.grid(row=self.row, column=self.column-1, columnspan=self.columnspan, padx=padx_label, pady=pady_label, ipadx=ipadx_label)


    def create_MenuOption(self):
        """
        Create a menu widget with various options
        """
        self.initial_val.set(self.options[0])
        self.menu = OptionMenu(self.parent, self.initial_val, *self.options)
        self.menu.grid(row=self.row, column=self.column, columnspan=self.columnspan, padx=self.padx, pady=self.pady, ipadx=self.ipadx)


    def font(self, new_font):
        """
        Change the font menu widget

        Input:
        ---------------------
        new_font: str
            new font
        """
        self.menu['font'] = new_font



class MainApplication:
    """
    Main application including all functions used on the main window

    Input:
    -----------------------------
    parent: window
        window of the main application
    """
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.parent.configure(bg=self._from_rgb((0, 128, 0)))
        self.title = self.parent.title('Archimedes LS App')
        self.icon = self.parent.iconbitmap('icon_spb.ico')
        self.font_window = tkFont.Font(family='Helvetica', size=10, weight='bold')

        self.app = FullScreenApp(self.parent)
        self.screenheight, self.screenwidth = self.app.screen_dim()
        self.size_x = DoubleVar(); self.size_y = DoubleVar()
        self.size_x.set(self.screenwidth / 1536. * 10)
        self.size_y.set(self.screenheight / 864. * 6)

        # Create Plot Data
        self.font_size_axes = DoubleVar(); self.font_size_axes.set(16)
        self.font_size_ticks = DoubleVar(); self.font_size_ticks.set(16)
        self.font_size_legend = DoubleVar(); self.font_size_legend.set(16)
        self.space_y_axis = DoubleVar(); self.space_y_axis.set(10)
        #self.size_x = DoubleVar(); self.size_x.set(10)
        #self.size_y = DoubleVar(); self.size_y.set(6)
        self.size_x_space = DoubleVar(); self.size_x_space.set(0.18)
        self.size_x_length = DoubleVar(); self.size_x_length.set(0.78)
        self.size_y_space = DoubleVar(); self.size_y_space.set(0.23)
        self.size_y_length = DoubleVar(); self.size_y_length.set(0.68)

        # Create MenuBar
        my_Menu = Menu(self.parent)
        self.parent.config(menu = my_Menu)

        file_menu = Menu(my_Menu)
        my_Menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New', command=self.clear)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.close_program)

        edit_menu = Menu(my_Menu)
        my_Menu.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='Edit Graph', command=self.Edit_graph)
        #edit_menu.add_command(label='Edit Colors', command=self.edit_color)

        calculate_menu = Menu(my_Menu)
        my_Menu.add_cascade(label='Calculate', menu=calculate_menu)
        calculate_menu.add_command(label='Calculate Density of Liquid', command=self.calculate_liquid)
        calculate_menu.add_command(label='Calculate Density of Solid', command=self.calculate_solid)
        calculate_menu.add_command(label='Calculate Minimum Mass', command=self.Calculate_minimum)

        help_menu = Menu(my_Menu)
        my_Menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='Welcome', command=self.welcome)
        help_menu.add_command(label='Documentations', command=self.documentary)
        help_menu.add_separator()
        help_menu.add_command(label='About', command=self.about)

        self.app = FullScreenApp(self.parent)

        # Create Entries for MainApplication
        self.dens_liq = EntryItem(self.parent, name='Density of Liquid / (g/cm3)', row=1, column=5, columnspan=1, ipadx=10, padx=10)
        self.dens_liq.create_EntryItem(ipadx_label=10)
        self.dens_liq.set_name(0.0)
        self.dens_liq_unc_var = StringVar()
        self.dens_liq_unc = Entry(self.parent, textvariable=self.dens_liq_unc_var, state=NORMAL, width=20)
        self.dens_liq_unc.grid(row=1, column=7, columnspan=1, padx=10, pady=6, ipadx=10)
        self.dens_liq_unc_var.set(0.0)
        self.dens_sol = EntryItem(self.parent, name='Density of Solid / (g/cm3)', row=2, column=5, columnspan=1, ipadx=10, padx=10)
        self.dens_sol.create_EntryItem(ipadx_label=14)
        self.dens_sol.set_name(0.0)

        self.data_label = Label(self.parent, text="Data", relief=RIDGE, anchor='w')
        self.data_label.grid(row=0, column=1, columnspan=1, padx=10, pady=6, ipadx=20)
        self.uncertainty_label = Label(self.parent, text="Uncertainty", relief=RIDGE, anchor='w')
        self.uncertainty_label.grid(row=0, column=3, columnspan=1, padx=10, pady=6, ipadx=20)
        self.data_label2 = Label(self.parent, text="Data", relief=RIDGE, anchor='w')
        self.data_label2.grid(row=0, column=5, columnspan=1, padx=10, pady=6, ipadx=20)
        self.uncertainty_label2 = Label(self.parent, text="Uncertainty", relief=RIDGE, anchor='w')
        self.uncertainty_label2.grid(row=0, column=7, columnspan=1, padx=10, pady=6, ipadx=20)
        self.ref1 = EntryItem(self.parent, name='Reference 1 / g', row=1)
        self.ref1.create_EntryItem(ipadx_label=46)
        self.ref1.set_name(0.000)
        self.ref1_unc_var = StringVar()
        self.ref1_unc = Entry(self.parent, textvariable=self.ref1_unc_var, state=NORMAL, width=20)
        self.ref1_unc_var.set(0.0001)
        self.ref1_unc.grid(row=1, column=3, columnspan=1, padx=10, pady=6, ipadx=20)

        self.ref1liq = EntryItem(self.parent, name="Reference 1 in liquid/ g", row=2)
        self.ref1liq.create_EntryItem(ipadx_label=25)
        self.ref1liq.set_name(0.000)

        self.ref1_unc_liq_var = StringVar()
        self.ref1_unc_liq = Entry(self.parent, textvariable=self.ref1_unc_liq_var, state=NORMAL, width=20)
        self.ref1_unc_liq_var.set(0.0001)
        self.ref1_unc_liq.grid(row=2, column=3, columnspan=1, padx=10, pady=6, ipadx=20)
        self.ref1den = EntryItem(self.parent, name="Density of Reference 1 / (g/cm3)", row=3)
        self.ref1den.create_EntryItem(ipadx_label=0)
        self.ref1den.set_name(0.000)
        self.ref2 = EntryItem(self.parent, name='Reference 2 / g', row=5)
        self.ref2.create_EntryItem(ipadx_label=46)
        self.ref2.set_name(0.0)
        self.ref2_unc_var = StringVar()
        self.ref2_unc = Entry(self.parent, textvariable=self.ref2_unc_var, state=NORMAL, width=20)
        self.ref2_unc_var.set(0.0001)
        self.ref2_unc.grid(row=5, column=3, columnspan=1, padx=10, pady=6, ipadx=20)
        self.ref2liq = EntryItem(self.parent, name="Reference 2 in liquid/ g", row=6)
        self.ref2liq.create_EntryItem(ipadx_label=25)
        self.ref2liq.set_name(0.0)
        self.ref2_unc_liq_var = StringVar()
        self.ref2_unc_liq = Entry(self.parent, textvariable=self.ref2_unc_liq_var, state=NORMAL, width=20)
        self.ref2_unc_liq_var.set(0.0001)
        self.ref2_unc_liq.grid(row=6, column=3, columnspan=1, padx=10, pady=6, ipadx=20)
        self.ref2den = EntryItem(self.parent, name="Density of Reference 2 / (g/cm3)", row=7)
        self.ref2den.create_EntryItem(ipadx_label=0)
        self.ref2den.set_name(0.0)
        self.ref3 = EntryItem(self.parent, name='Reference 3 / g', row=9)
        self.ref3.create_EntryItem(ipadx_label=46)
        self.ref3.set_name(0.0)
        self.ref3_unc_var = StringVar()
        self.ref3_unc = Entry(self.parent, textvariable=self.ref3_unc_var, state=NORMAL, width=20)
        self.ref3_unc_var.set(0.0001)
        self.ref3_unc.grid(row=9, column=3, columnspan=1, padx=10, pady=6, ipadx=20)
        self.ref3liq = EntryItem(self.parent, name="Reference 3 in liquid/ g", row=10)
        self.ref3liq.create_EntryItem(ipadx_label=25)
        self.ref3liq.set_name(0.0)
        self.ref3_unc_liq_var = StringVar()
        self.ref3_unc_liq = Entry(self.parent, textvariable=self.ref3_unc_liq_var, state=NORMAL, width=20)
        self.ref3_unc_liq_var.set(0.0001)   #("±"+str(0.0001)) 
        self.ref3_unc_liq.grid(row=10, column=3, columnspan=1, padx=10, pady=6, ipadx=20)
        self.ref3den = EntryItem(self.parent, name="Density of Reference 3 / (g/cm3)", row=11)
        self.ref3den.create_EntryItem(ipadx_label=0)
        self.ref3den.set_name(0.0)
        self.sample = EntryItem(self.parent, name='Sample / g', row=13)
        self.sample.create_EntryItem(ipadx_label=56)
        self.sample.set_name(0.0)
        self.sample_unc_var = StringVar()
        self.sample_unc = Entry(self.parent, textvariable=self.sample_unc_var, state=NORMAL, width=20)
        self.sample_unc_var.set(0.0001)
        self.sample_unc.grid(row=13, column=3, columnspan=1, padx=10, pady=6, ipadx=20)
        self.sampleliq = EntryItem(self.parent, name="Sample in liquid/ g", row=14)
        self.sampleliq.create_EntryItem(ipadx_label=35)
        self.sampleliq.set_name(0.0)
        self.sample_unc_liq_var = StringVar()
        self.sample_unc_liq = Entry(self.parent, textvariable=self.sample_unc_liq_var, state=NORMAL, width=20)
        self.sample_unc_liq_var.set(0.0001)
        self.sample_unc_liq.grid(row=14, column=3, columnspan=1, padx=10, pady=6, ipadx=20)


        # Create Buttons for MainApplication
        self.btn_calculate_liq = Button(self.parent, text='Calculate density of liquid', command=self.calculate_liquid, bg=self._from_rgb((118, 61, 76)), fg='white')
        self.btn_calculate_liq['font'] = self.font_window
        self.btn_calculate_liq.grid(row=16, column=0, columnspan=2, padx=10, ipadx=40)
        self.btn_calculate_sol = Button(self.parent, text='Calculate density of solid', command=self.calculate_solid, bg=self._from_rgb((118, 61, 76)), fg='white')
        self.btn_calculate_sol['font'] = self.font_window
        self.btn_calculate_sol.grid(row=18, column=0, columnspan=2, padx=10, ipadx=43)


        self.font_options = [
            'Times New Roman',
            'Arial',
            'Gabriola',
            'Courier New',
            'Cambria',
            'Calibri',
        ]
        self.initial_font = StringVar(); self.initial_font.set(self.font_options[0])
        self.create_empty_plot()


    def create_empty_plot(self):
        """
        Create an emplty plot at the start and when it is cleared
        """

        plt.rcParams["font.family"] = self.initial_font.get()
        plt.rcParams.update({'font.size': self.font_size_ticks.get()})

        self.fig = Figure(figsize=(self.size_x.get(), self.size_y.get()), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent)
        self.canvas.draw()
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.grid(row=3, column=4, columnspan=10, rowspan=13)

        ax1 = self.fig.add_axes([self.size_x_space.get(), self.size_y_space.get(), self.size_x_length.get(), self.size_y_length.get()])
        ax1.set_xlabel(r'$m_{sample}$ / $\Delta m$', fontsize=float(self.font_size_axes.get()))
        ax1.set_xlim(0, 5)
        ax1.set_ylabel(r'$\rho_{solid}$ / g cm$^{-3}$', fontsize=float(self.font_size_axes.get()))
        ax1.set_ylim(3, 15)

        self.toolbar_frame = Frame(self.parent) 
        self.toolbar_frame.grid(row=18,column=4,columnspan=4) 
        toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        toolbar.update()


    def calculate_liquid(self):
        """
        Calculate the density of the liquid using three reference values
        """ 
        self.get_data_liquid()
        if not (len(self.m1) == len(self.m2) == len(self.y) == len(self.sigma_m1) == len(self.sigma_m2)):
            messagebox.showerror('ERROR',"All arrays must have the same length.")
        
        elif 0 in self.m1 or 0 in self.m2 or 0 in self.y:
            messagebox.showerror('ERROR',"Fill in the masses and densities of the three reference samples.")
        
        else:
            print(self.sigma_m2, self.sigma_m1)
            a = self.y * (self.m1 - self.m2) / self.m1

            # Partial derivatives
            da_dm1 = self.y * self.m2 / self.m1**2
            da_dm2 = -self.y / self.m1

            # Propagated uncertainty
            sigma_a = np.sqrt(
                (da_dm1 * self.sigma_m1)**2 +
                (da_dm2 * self.sigma_m2)**2
            )

            # Weighted average
            weights = 1 / sigma_a**2
            a_mean = np.sum(weights * a) / np.sum(weights)
            sigma_mean = np.sqrt(1 / np.sum(weights))

            self.dens_liq.set_name(f"{a_mean:.4f}")
            self.dens_liq_unc_var.set(f"{sigma_mean:.4f}")

            plt.rcParams["font.family"] = self.initial_font.get()
            plt.rcParams.update({'font.size': self.font_size_ticks.get()})

            self.fig = Figure(figsize=(self.size_x.get(), self.size_y.get()), dpi=100)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent)
            self.canvas.draw()
            self.plot_widget = self.canvas.get_tk_widget()
            self.plot_widget.grid(row=3, column=4, columnspan=10, rowspan=13)

            #plt.style.use('grayscale')
            ax1 = self.fig.add_axes([self.size_x_space.get(), self.size_y_space.get(), self.size_x_length.get(), self.size_y_length.get()])

            ax1.errorbar(self.m1/(self.m1 - self.m2), self.y,  xerr=sigma_a, fmt='o', ms=4, capsize=5, color='r')
            x_fit = np.linspace(np.min(self.m1/(self.m1 - self.m2)) * 0.8, np.max(self.m1/(self.m1 - self.m2)) * 1.2, 100)
            y_fit = x_fit * a_mean
        
            ax1.plot(x_fit, y_fit, color='k', ls='--')

            ax1.set_xlim(np.min(self.m1 / (self.m1 - self.m2)) * 0.8, np.max(self.m1 / (self.m1 - self.m2)) * 1.2)
            ax1.set_ylim(np.min(self.y) * 0.8, np.max(self.y) * 1.2)
            ax1.set_xlabel(r'$m_{sample}$ / $\Delta m$', fontsize=float(self.font_size_axes.get()))
            ax1.set_ylabel(r'$\rho_{solid}$ / g cm$^{-3}$', fontsize=float(self.font_size_axes.get()))
            plt.tight_layout()

            self.toolbar_frame = Frame(self.parent) 
            self.toolbar_frame.grid(row=18,column=4,columnspan=4) 
            toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
            toolbar.update()

    
    def calculate_solid(self):
        """
        Calculate the density of the unknown solid sample
        """
        self.get_data_solid()
        if 0 == self.m_s or 0 == self.m_s_liq or 0 == self.d_liq:
            messagebox.showerror("ERROR", "Fill in the masses of the sample and the density of the liquid.")

        else:
            dens_sol = self.m_s * self.d_liq / (self.m_s - self.m_s_liq)

            # Partial derivatives
            dy_dm_s = -self.d_liq * self.m_s_liq / (self.m_s - self.m_s_liq)**2
            dy_dm_s2 =  self.d_liq * self.m_s / (self.m_s - self.m_s_liq)**2
            dy_d_liq  =  self.m_s / (self.m_s - self.m_s_liq)

            # Error propagation
            sigma_y = np.sqrt(
                (dy_dm_s * self.m_s_unc)**2 +
                (dy_dm_s2 * self.m_s_liq_unc)**2 +
                (dy_d_liq  * self.d_liq_unc )**2
            )
            self.dens_sol.set_name(f"{dens_sol:.4f}±{sigma_y:.4f}") 


    def get_data_liquid(self):
        """
        Get the data to calculate the density of the liquid
        """
        r1 = self.ref1.get_name(); r1_unc = self.ref1_unc_var.get(); r1_liq = self.ref1liq.get_name(); r1_liq_unc = self.ref1_unc_liq_var.get(); d1 = self.ref1den.get_name()
        r2 = self.ref2.get_name(); r2_unc = self.ref2_unc_var.get(); r2_liq = self.ref2liq.get_name(); r2_liq_unc = self.ref2_unc_liq_var.get(); d2 = self.ref2den.get_name()
        r3 = self.ref3.get_name(); r3_unc = self.ref3_unc_var.get(); r3_liq = self.ref3liq.get_name(); r3_liq_unc = self.ref3_unc_liq_var.get(); d3 = self.ref3den.get_name()
        
        self.m1 = np.array([r1, r2, r3], dtype=float)
        self.m2 = np.array([r1_liq, r2_liq, r3_liq], dtype=float)
        self.y = np.array([d1, d2, d3], dtype=float)

        self.sigma_m1 = np.array([r1_unc, r2_unc, r3_unc], dtype=float)
        self.sigma_m2 = np.array([r1_liq_unc, r2_liq_unc, r3_liq_unc], dtype=float)


    def get_data_solid(self):
        """
        Get the data to calculate the density of the solid
        """    
        self.m_s = float(self.sample.get_name())
        self.m_s_unc = float(self.sample_unc_var.get())
        self.m_s_liq = float(self.sampleliq.get_name())
        self.m_s_liq_unc = float(self.sample_unc_liq_var.get())
        self.d_liq = float(self.dens_liq.get_name())
        self.d_liq_unc = float(self.dens_liq_unc_var.get())
        

    def close_update_graph(self):
        """
        Close the Edit window and create an empty plot
        """
        self.plot_widget.grid_forget()
        self.Top.destroy()

    def close_minimum_calc(self):
            """
            Close the Minimum Calcuation window
            """
            self.Top_calc.destroy()


    def Calculate_minimum(self):
        """
        Calculate the minimum mass to achieve a desired density
        """
        self.Top_calc = Toplevel()
        self.Top_calc.configure(bg = self._from_rgb((0, 128, 0)))
        self.Top_calc.geometry("600x400")
        self.Top_calc.iconbitmap('icon_spb.ico')

        self.label_input = Label(self.Top_calc, text='Calculate the minimum mass')
        self.label_input.grid(row=0, column=0,columnspan=3, pady=(10, 5))
        self.label_input['font'] = self.font_window

        self.data_label = Label(self.Top_calc, text="Data", relief=RIDGE, anchor='w')
        self.data_label.grid(row=1, column=1, columnspan=1, padx=10, pady=6, ipadx=20)
        self.uncertainty_label = Label(self.Top_calc, text="Uncertainty", relief=RIDGE, anchor='w')
        self.uncertainty_label.grid(row=1, column=3, columnspan=1, padx=10, pady=6, ipadx=20)

        self.dens_sol_min = EntryItem(self.Top_calc, name='Density of solid / (g/cm3)', row=2)
        self.dens_sol_min.create_EntryItem(ipadx_label=36)
        self.dens_sol_min.set_name(0.000)
        self.dens_sol_min_unc_var = StringVar()
        self.dens_sol_min_unc = Entry(self.Top_calc, textvariable=self.dens_sol_min_unc_var, state=NORMAL, width=20)
        self.dens_sol_min_unc_var.set(0.0001)
        self.dens_sol_min_unc.grid(row=2, column=3, columnspan=1, padx=10, pady=6, ipadx=20)

        self.dens_liq_min = EntryItem(self.Top_calc, name='Density of liquid / (g/cm3)', row=3)
        self.dens_liq_min.create_EntryItem(ipadx_label=34)
        self.dens_liq_min.set_name(0.000)
        self.dens_liq_min_unc_var = StringVar()
        self.dens_liq_min_unc = Entry(self.Top_calc, textvariable=self.dens_liq_min_unc_var, state=NORMAL, width=20)
        self.dens_liq_min_unc_var.set(0.0001)
        self.dens_liq_min_unc.grid(row=3, column=3, columnspan=1, padx=10, pady=6, ipadx=20)

        self.mass_a_min = EntryItem(self.Top_calc, name='Mass in air / g', row=4, state=DISABLED)
        self.mass_a_min.create_EntryItem(ipadx_label=66)
        self.mass_a_min.set_name(0.000)
        self.mass_a_min_unc_var = StringVar()
        self.mass_a_min_unc = Entry(self.Top_calc, textvariable=self.mass_a_min_unc_var, state=NORMAL, width=20)
        self.mass_a_min_unc_var.set(0.0001)
        self.mass_a_min_unc.grid(row=4, column=3, columnspan=1, padx=10, pady=6, ipadx=20)

        self.mass_l_min = EntryItem(self.Top_calc, name='Mass in liquid / g', row=5, state=DISABLED)
        self.mass_l_min.create_EntryItem(ipadx_label=58)
        self.mass_l_min.set_name(0.000)
        self.mass_l_min_unc_var = StringVar()
        self.mass_l_min_unc = Entry(self.Top_calc, textvariable=self.mass_l_min_unc_var, state=NORMAL, width=20)
        self.mass_l_min_unc_var.set(0.0001)
        self.mass_l_min_unc.grid(row=5, column=3, columnspan=1, padx=10, pady=6, ipadx=20)

        btn_calc = Button(self.Top_calc, text='Calculate', command=self.minimum_calculation)
        btn_calc.grid(row=6, column=1, padx=10, pady=10, ipadx=35)

        btn_close = Button(self.Top_calc, text='Close', command=self.close_minimum_calc)
        btn_close.grid(row=6, column=3, padx=10, pady=10, ipadx=35)


    def minimum_calculation(self):
        """
        Calculate the minimum mass
        """
        rho_s = float(self.dens_sol_min.get_name())
        rho_l = float(self.dens_liq_min.get_name())
        sigma_rho_s = float(self.dens_sol_min_unc_var.get())
        sigma_rho_l = float(self.dens_liq_min_unc_var.get())
        sigma_m_a = float(self.mass_a_min_unc_var.get())
        sigma_m_l = float(self.mass_l_min_unc_var.get())
        if rho_l**2 * sigma_rho_s**2 - rho_s**2 * sigma_rho_l**2 >= 0:
            mass_min = rho_s * np.sqrt(((rho_s-rho_l)**2*sigma_m_a**2 + rho_s**2 * sigma_m_l**2) / (rho_l**2 * sigma_rho_s**2 - rho_s**2 * sigma_rho_l**2))
            mass_l_min = mass_min * (rho_s- rho_l)/rho_s
            self.mass_a_min.set_name(mass_min)
            self.mass_l_min.set_name(mass_l_min)
        else:
            messagebox.showerror('ERROR',"Increase the uncertainty of the solid density or density of the liquid or reduce the uncertainty of the liquid density.")



    def Edit_graph(self):
        """
        Edit plot by changing size and font
        """
        self.Top = Toplevel()
        self.Top.configure(bg = self._from_rgb((0, 128, 0)))
        self.Top.geometry("600x400")
        self.Top.iconbitmap('icon_spb.ico')

        self.label_input = Label(self.Top, text='Change Parameters of the Graph')
        self.label_input.grid(row=0, column=0,columnspan=3, pady=(10, 5))
        self.label_input['font'] = self.font_window

        self.font_size_axes_entry = Entry(self.Top, textvariable=self.font_size_axes, width=24)
        self.font_size_axes_entry.grid(row=1, column=1, padx=10, pady=(50, 10))
        self.font_size_axes_label = Label(self.Top, text='Font Size Axes', relief=RIDGE, anchor='w')
        self.font_size_axes_label.grid(row=1, column=0, padx=10, pady=(50, 10), ipadx=8)

        self.font_size_ticks_entry = Entry(self.Top, textvariable=self.font_size_ticks, width=24)
        self.font_size_ticks_entry.grid(row=2, column=1, padx=10)
        self.font_size_ticks_label = Label(self.Top, text='Font Size Ticks', relief=RIDGE, anchor='w')
        self.font_size_ticks_label.grid(row=2, column=0, padx=10, ipadx=8)

        self.font_size_legend_entry = Entry(self.Top, textvariable=self.font_size_legend, width=24)
        self.font_size_legend_entry.grid(row=3, column=1, padx=10)
        self.font_size_legend_label = Label(self.Top, text='Font Size Legend', relief=RIDGE, anchor='w')
        self.font_size_legend_label.grid(row=3, column=0, padx=10, ipadx=8)

        self.space_y_axis_entry = Entry(self.Top, textvariable=self.space_y_axis, width=24)
        self.space_y_axis_entry.grid(row=4, column=1, padx=10)
        self.space_y_axis_label = Label(self.Top, text='Space Y axis', relief=RIDGE, anchor='w')
        self.space_y_axis_label.grid(row=4, column=0, padx=10, ipadx=15)

        self.size_x_entry = Entry(self.Top, textvariable=self.size_x, width=24)
        self.size_x_entry.grid(row=4, column=3, padx=10)
        self.size_x_label = Label(self.Top, text='Figure Width', relief=RIDGE, anchor='w')
        self.size_x_label.grid(row=4, column=2, padx=10, ipadx=17)

        self.size_y_entry = Entry(self.Top, textvariable=self.size_y, width=24)
        self.size_y_entry.grid(row=1, column=3, padx=10, pady=10)
        self.size_y_label = Label(self.Top, text='Figure Height', relief=RIDGE, anchor='w')
        self.size_y_label.grid(row=1, column=2, padx=10, pady=10, ipadx=15)

        self.size_x_space_entry = Entry(self.Top, textvariable=self.size_x_space, width=24)
        self.size_x_space_entry.grid(row=2, column=3, padx=10, pady=10)
        self.size_x_space_label = Label(self.Top, text='Plot Start x', relief=RIDGE, anchor='w')
        self.size_x_space_label.grid(row=2, column=2, padx=10, pady=10, ipadx=16)

        self.size_y_space_entry = Entry(self.Top, textvariable=self.size_y_space, width=24)
        self.size_y_space_entry.grid(row=3, column=3, padx=10, pady=10)
        self.size_y_space_label = Label(self.Top, text='Plot Start y', relief=RIDGE, anchor='w')
        self.size_y_space_label.grid(row=3, column=2, padx=10, pady=10, ipadx=16)

        self.size_x_length_entry = Entry(self.Top, textvariable=self.size_x_length, width=24)
        self.size_x_length_entry.grid(row=4, column=3, padx=10, pady=10)
        self.size_x_length_label = Label(self.Top, text='Plot Width x', relief=RIDGE, anchor='w')
        self.size_x_length_label.grid(row=4, column=2, padx=10, pady=10, ipadx=20)

        self.size_y_length_entry = Entry(self.Top, textvariable=self.size_y_length, width=24)
        self.size_y_length_entry.grid(row=5, column=3, padx=10, pady=10)
        self.size_y_length_label = Label(self.Top, text='Plot Width y', relief=RIDGE, anchor='w')
        self.size_y_length_label.grid(row=5, column=2, padx=10, pady=10, ipadx=20)

        self.font_menu = OptionMenu(self.Top, self.initial_font, *self.font_options)
        self.font_menu.grid(row=5, column=1, padx=10, pady=10)
        self.font_label = Label(self.Top, text='Font', relief=RIDGE, anchor='w')
        self.font_label.grid(row=5, column=0, padx=10, pady=10, ipadx=32)

        btn_close = Button(self.Top, text='Close', command=self.close_update_graph)
        btn_close.grid(row=6, column=3, padx=10, pady=10, ipadx=35)


    def _from_rgb(self, rgb):
        """
        translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb
    

    def clear(self):
        """
        Clear the data/graph but keep edit graph
        """
        self.create_empty_plot()

    
    def close_program(self):
        """
        Close the program
        """
        self.parent.quit()
        self.parent.destroy()


    def welcome(self):
        """
        Create welcome window
        """
        welcome = Help()
        welcome.welcome()


    def documentary(self):
        """
        Create documentary window
        """
        documentary = Help()
        documentary.documentary()


    def about(self):
        """
        Create about window
        """
        about = Help()
        about.screen_help.geometry('700x450')
        about.about()


def _quit():
    """
    Close the program
    """
    root.quit()
    root.destroy()


if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.protocol("WM_DELETE_WINDOW", _quit)
    root.mainloop()
    
