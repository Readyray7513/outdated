## Date Formatter & Validator 📅  

This Python program takes a date input in different formats, validates it, and converts it into **ISO 8601 format (YYYY-MM-DD)**.  

### **Supported Formats**  
✅ `MM/DD/YYYY` → (e.g., `9/8/1636`)  
✅ `Month Day, Year` → (e.g., `September 8, 1636`)  

### **Invalid Inputs**  
❌ Numbers in place of month names (`9 September 1636`)  
❌ Missing commas in `Month Day, Year` format (`September 8 1636`)  
❌ Invalid dates (`February 30, 2000`)  
❌ Special characters or text that aren't valid dates  

### **How to Use**  
1. Run the program:  
   ```bash
   python date_formatter.py
   ```  
2. Enter a date in a supported format when prompted.  
3. If the date is valid, it will be displayed in **YYYY-MM-DD** format.  
4. If the input is incorrect, you'll be asked to try again.  

### **Example Inputs & Outputs**  
| Input  | Output  |
|--------|--------|
| `9/8/1636`  | `1636-09-08`  |
| `September 8, 1636`  | `1636-09-08`  |
| `February 30, 2020`  | Invalid date  |
| `December 25 2023`  | Invalid format  |

A handy tool for ensuring date consistency across different formats! 🎯
