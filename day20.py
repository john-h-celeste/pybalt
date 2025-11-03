import tkinter as tk

'''

# p_survey_var.py
# Create the root window
root = tk.Tk()

# set the title
root.title('CS Problem Solving and Solution Survey')

# set the root window size
root.geometry('640x480+300+300')
root.resizable(False, False)

title = tk.Label(
  root,
  text='Please take survey',
  font=('Arial 16 bold'),
  bg='black',
  fg='white'
)

# Use string vars for strings
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var)

# Use boolean var for True/False
like_var = tk.BooleanVar()
language_inp = tk.Checkbutton(
  root, variable=like_var, text='Check this box if you like Python'
)

# Use int var for whole numbers
# Value can set a default
num_var = tk.IntVar(value=3)
num_label = tk.Label(text='How many hours do you work on Python homework a week?')
# note that even with an intvar, the key is still 'textvariable'
num_inp = tk.Spinbox(
  root,
  textvariable=num_var,
  from_=0,
  to=1000,
  increment=1
)

# Use OptionMenu with variables instead of Listbox
language_var = tk.StringVar(value='Any')
language_label = tk.Label(
  root,
  text='What is the best programming language?' )
language_choices = (
  'Any', 'C', 'C++', 'Java', 'Javascript', 'Python')
language__inp = tk.OptionMenu(
  root, language_var, *language_choices)
python_label = tk.Label(root, text='Do you expect an A in COP2080?')
# Use a Frame to keep widgets together
alpha_frame = tk.Frame(root)

python_var = tk.BooleanVar()
# The radio buttons are connected by using the same variable

alpha_yes_inp = tk.Radiobutton(
  alpha_frame,
  text='Yes',
  value=True,
  variable=python_var
)

def on_submit():
  """To be run when the user submits the form"""

  # Vars all use 'get()' to retreive their variables
  name = name_var.get()
  # Because of IntVar, .get() will try to convert
  # the contents of num_var to int.
  try:
    number = num_var.get()
  except tk.TclError:
    number = 10000

  # OptionMenu makes things simple
  language_ = language_var.get()

  # Checkbutton and Radiobutton values
  python_liker = like_var.get()
  python_user = python_var.get()

  # Text widgets require a range
  haiku = python_haiku_inp.get('1.0', tk.END)

root.mainloop()
'''

root = tk.Tk()

(main_frame := tk.Frame(root, padx = 5, pady = 5, borderwidth = 5, relief = 'solid')).grid(column = 0, row = 0)

(  url_frame := tk.Frame(main_frame, padx = 5, pady = 5, borderwidth = 5, relief = 'solid')).grid(column = 0, row = 0)

(    url_entry := tk.Entry(url_frame)).grid(column = 0, row = 0, sticky = 'NS')

(    fetch_button := tk.Button(url_frame, text = 'fetch')).grid(column = 1, row = 0)

(  image_frame := tk.Frame(main_frame, padx = 5, pady = 5, borderwidth = 5, relief = 'solid')).grid(column = 0, row = 1, sticky = 'EW')

(    image_list := tk.Frame(image_frame, padx = 5, pady = 5, borderwidth = 5, relief = 'solid')).grid(column = 0, row = 0, sticky = 'EW')

(    radio_frame := tk.Frame(image_frame, padx = 5, pady = 5, borderwidth = 5, relief = 'solid')).grid(column = 1, row = 0, sticky = 'EW')

(  scrape_button := tk.Button(main_frame, text = 'scrape')).grid(column = 0, row = 2, sticky = 'E')

(status_frame := tk.Frame(root, padx = 5, pady = 5, borderwidth = 5, relief = 'solid')).grid(column = 0, row = 1)

root.mainloop()