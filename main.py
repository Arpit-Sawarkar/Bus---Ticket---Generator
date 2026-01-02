import tkinter as tk
from tkinter import ttk
from datetime import datetime

city_list = [
    "Navsari", "Kathora square", "Shegaon Naka", "Gadge nagar",
    "Panchavati", "Ervin square", "Bus-depot", "Amravati Rly. Stn",
    "Jaystambh squ", "Rajkamal ", "Rajapeth", "Navathe squ", "Sai-nagar",
    "Badnera", "Badnare Rly. Stn"
]
FARE_PER_STOP = 5
ticket_counter = 36266604  # no  of ticket (auto increment)


def calculate_fare(from_city, to_city, full_count, half_count):
    try:
        from_index = city_list.index(from_city)
        to_index = city_list.index(to_city)
        distance = abs(from_index - to_index)
        rate = distance * FARE_PER_STOP
        half_rate = rate / 2
        total = (full_count * rate) + (half_count * half_rate)
        return rate, half_rate, total
    except ValueError:
        return 0, 0, 0


def show_ticket(from_city, to_city, full_count, half_count, rate, half_rate, total):
    global ticket_counter
    now = datetime.now()
    date_str = now.strftime("%d/%m/%y")
    time_str = now.strftime("%I:%M:%S %p")
    ticket_lines = ""
    if full_count > 0 and half_count == 0:
        ticket_lines += f"| Full: {full_count} * ₹{rate:.2f} = ₹{full_count * rate:.2f}       |"
    elif half_count > 0 and full_count == 0:
        ticket_lines += f"| Half: {half_count} * ₹{half_rate:.2f} = ₹{half_count * half_rate:.2f}       |"
    elif full_count > 0 and half_count > 0:
        ticket_lines += f"| Full: {full_count} * ₹{rate:.2f} = ₹{full_count * rate:.2f}       |\n"
        ticket_lines += f"| Half: {half_count} * ₹{half_rate:.2f} = ₹{half_count * half_rate:.2f}       |"

    ticket_text = f"""\
+---------------------------------+
|● Happy Journey  ● शुभ यात्रा       |
|        ⦿ Amravati AMC          |
|---------------------------------|
| Ticket No: {ticket_counter}            |
| Date: {date_str}                  |
| Time: {time_str}               |
| From: {from_city}  To: {to_city}  |
{ticket_lines}
| Total: ₹{total:.2f}                   |
|---------------------------------|
| ○ Thank You    ○ धन्यवाद          |
|   आपला प्रवास सुखात जावो.          |
+---------------------------------+
"""

    # ticket popup window
    win = tk.Toplevel()
    win.title("Passenger Ticket")

    text_frame = tk.Frame(win, width=50, height=10)
    text_frame.pack_propagate(False)
    text = tk.Text(win, height=15, width=47, font=("Courier New", 14), bg="#F8F8F0", fg="black")
    text.pack(fill="both", expand=True)
    text_frame.pack()

    text.insert(tk.END, ticket_text)
    text.config(state='disabled')
    close_btn = tk.Button(win, text="Close", command=win.destroy)
    close_btn.pack(pady=5)
    ticket_counter += 1


def submit_form():
    from_city = from_var.get()
    to_city = to_var.get()
    try:
        full = int(full_entry.get())
    except:
        full = 0
    try:
        half = int(half_entry.get())
    except:
        half = 0
    rate, half_rate, total = calculate_fare(from_city, to_city, full, half)
    # conductor console
    now = datetime.now()
    time_str = now.strftime("%I:%M:%S %p")
    print("\n =====Amravati Parivahan===== ")
    print(f"Ticket No  :   {ticket_counter}")
    print(f"Date          :   {now.strftime('%d/%m/%y')}")
    print(f"Time          :   {now.strftime('%I:%M:%S %p')}")
    print(f"From          :  {from_city}")
    print(f"To              :  {to_city}")
    if full > 0 and half == 0:
        print(f"Full       :   {full} × ₹{rate:.2f} = ₹{full * rate:.2f}")
    elif half > 0 and full == 0:
        print(f"Half       :   {half} × ₹{half_rate:.2f} = ₹{half * half_rate:.2f}")
    elif full > 0 and half > 0:
        print(f"Full       :    {full} × ₹{rate:.2f} = ₹{full * rate:.2f}")
        print(f"Half       :   {half} × ₹{half_rate:.2f} = ₹{half * half_rate:.2f}")
    print(f"Total      :   ₹{total:.2f}")
    # passenger ticket popup
    show_ticket(from_city, to_city, full, half, rate, half_rate, total)


# main input window conductor
root = tk.Tk()
root.title("Bus Conductor Popup")
root.geometry("300x200")
tk.Label(root, text="From :").grid(row=0, column=0, padx=10, pady=5, sticky='e')
from_var = tk.StringVar()
from_combo = ttk.Combobox(root, textvariable=from_var, values=city_list, state='readonly')
from_combo.grid(row=0, column=1, padx=10, pady=5)
from_combo.current(0)

tk.Label(root, text="To :").grid(row=1, column=0, padx=10, pady=5, sticky='e')
to_var = tk.StringVar()
to_combo = ttk.Combobox(root, textvariable=to_var, values=city_list, state='readonly')
to_combo.grid(row=1, column=1, padx=10, pady=5)
to_combo.current(3)

tk.Label(root, text="Full ticket :").grid(row=2, column=0, padx=10, pady=5, sticky='e')
full_entry = tk.Entry(root)
full_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Half ticket:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
half_entry = tk.Entry(root)
half_entry.grid(row=3, column=1, padx=10, pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit_form, bg="#ADD8E6", fg="black")
submit_btn.grid(row=4, columnspan=2, pady=10)
root.bind('<Return>', lambda e: submit_btn.invoke())  # enter button to submit

root.mainloop()







