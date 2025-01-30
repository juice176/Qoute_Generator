#Andrea Muñoz
import requests
import sys
import tkinter as tk
#class to redirect console print statements into Gui system
class ConsoleRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)
    def flush(self):
        pass
#initialize tkinter gui window
root = tk.Tk()
root.title("Qoutes of the Day")
root.geometry('550x300')
#function for button action 
#extracts qoute and author from api request
def clicked():
    response = requests.get("https://thequoteshub.com/api/")
    if response.status_code == 200:
        data = response.json()

        qoute = data['text']
        author = data['author']
        
        output_label.config(text=f'"{qoute}"\n- {author}')
        
    else: 
        print(f"Failed to retrive data: {response.status_code}")

output_text = tk.Text(root, height=10, width=40, wrap=tk.WORD)

sys.stdout = ConsoleRedirector(output_text)

output_label = tk.Label(root, text="Click the button to get a quote!", wraplength=300)
output_label.grid(column=1, row=5, columnspan=2, pady=10)
#button
btn = tk.Button(root, text = "Click for Qoute", fg="green", command= clicked)
btn.grid(column=1 , row = 1)
#main
root.mainloop()

