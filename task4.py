#------------------------------
#Log Analysis System 
#-----------------------------
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from collections import Counter

def analyze_log(file_path):
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) < 9:
                    continue
                ip = parts[0]
                url = parts[6]
                status = parts[8]
                ip_counter[ip] += 1
                url_counter[url] += 1
                status_counter[status] += 1

        return ip_counter.most_common(5), url_counter.most_common(5), status_counter
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return [], [], {}

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.log *.txt"), ("All files", "*.*")])
    if file_path:
        ip_data, url_data, status_data = analyze_log(file_path)
        output_text.delete('1.0', tk.END)

        output_text.insert(tk.END, "📌 Top 5 IP Addresses:\n")
        for ip, count in ip_data:
            output_text.insert(tk.END, f"{ip}: {count} times\n")

        output_text.insert(tk.END, "\n🌐 Top 5 URLs:\n")
        for url, count in url_data:
            output_text.insert(tk.END, f"{url}: {count} times\n")

        output_text.insert(tk.END, "\n📊 Status Code Count:\n")
        for status, count in status_data.items():
            output_text.insert(tk.END, f"{status}: {count} times\n")

# GUI Design
window = tk.Tk()
window.title("Log Analysis System")
window.geometry("600x500")
window.config(bg="#f5f5f5")

tk.Label(window, text="📁 Log Analysis Tool", font=("Helvetica", 16, "bold"), bg="#f5f5f5").pack(pady=10)

tk.Button(window, text="Browse Log File", command=browse_file, bg="#007acc", fg="white",
          font=("Helvetica", 12), padx=10, pady=5).pack(pady=10)

output_text = scrolledtext.ScrolledText(window, width=70, height=20, font=("Courier", 10))
output_text.pack(padx=10, pady=10)

tk.Label(window, text="Created by: Abhay", bg="#f5f5f5", font=("Helvetica", 9, "italic")).pack(pady=5)

window.mainloop()
