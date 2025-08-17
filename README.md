# School Management Software

**Author:** : Kunal (Github id :Kunal-R-Kumar)
**Email:** kkumar021104@gmail.com
**Language:** Python
**Lines of Code:** 1950
**Functions:** 47

---

## **Project Overview**

The **School Management Software** is a comprehensive, **user-friendly, menu-driven application** designed to handle the day-to-day administrative needs of schools. It efficiently manages **student and teacher records**, tracks **marks**, and ensures **data security** through password protection and encoding. The system is built with simplicity in mind, enabling school staff to **add, search, update, and delete records** with minimal effort.

The software is ideal for small to medium schools or educational institutions that want a **digital solution** for administrative record keeping without relying on complex database systems.

---

## **Core Functionalities**

### **1. Security & Menu Management**

The software emphasizes **data protection and secure access**. It includes:

* **Password creation and verification** (`password()`, `psscheck()`) for safe access.
* **Data encoding and decoding** (`encode()`, `encoder()`, `decode()`, `decoder()`) to protect sensitive information.
* **Menu navigation and query handling** (`query()`, `entry()`) for a user-friendly interface.
* **Password deletion** (`pssdeleter()`) to manage authentication as required.

These features ensure that only authorized personnel can access or modify school data.

---

### **2. Student Management**

The student module contains **27 dedicated functions** designed to cover all aspects of student data handling:

#### **Admission & Validation**

* **Ensure unique admission numbers** (`admchecker(z)`), preventing duplicate entries.
* **Generate unique admission numbers automatically** (`adm_maker()`).
* **Validate class ranges** (`classlimit(z)`), ensuring students belong to classes 1–12.
* **Check for non-empty name fields** (`namechecker(z)`), maintaining data integrity.
* **Validate streams for classes 11–12** (`streamchecker(z)`), ensuring proper categorization.

#### **Record Operations**

* **Add new student records** (`wrtsr()`) with all essential details.
* **Read all student data** (`reasr()`) for complete reporting.
* **Search for students** (`sers()`) using multiple techniques for flexibility.
* **Update student records individually** (`updatesr()`), ensuring easy modifications.
* **Delete individual student records** (`rec_deleters()`), maintaining database accuracy.

#### **Marks Management**

* **Enter marks for classes 1–5** (`wrtmrks15()`, `wrtmrk15(a,b)`) and update them (`updatemrk15()`).
* **Enter marks for classes 6–10** (`wrtmrks610()`, `wrtmrk610(a,b)`) and update them (`updatemrk610()`).
* **Enter marks for classes 11–12** (`wrtmrks1112()`, `wrtmrk1112(a,b)`) and update them (`updatemrk1112()`).
* **Display class-wise results**:

  * Classes 1–5: `rslt15()`
  * Classes 6–10: `rslt610()`
  * Class 11: `rslt11()`
  * Class 12: `rslt12()`
* **Display individual student results** (`rsltprtclr()`), allowing teachers to track performance.
* **Validate class levels** for mark entry (`classchecker15(z)`, `classchecker610(z)`, `classchecker1112(z)`).

---

### **3. Teacher Management**

The teacher module contains **7 dedicated functions** for maintaining staff records:

* **Ensure unique teacher IDs** (`tchridchecker(z)`) and auto-generate IDs (`tchrid_maker()`).
* **Add new teacher records** (`enttr()`).
* **Read all teacher data** (`reatr()`) for easy oversight.
* **Search teacher records** (`sert()`) with multiple search techniques.
* **Update teacher records individually** (`updatetr()`).
* **Delete individual teacher records** (`rec_deletert()`).

This module ensures that both **student and teacher data** can be efficiently managed and maintained.

---

### **4. Backup & Restore**

Data integrity and safety are essential in school management. The software provides:

* **Student data checkpoint creation** (`backupst()`) to store snapshots.
* **Teacher data checkpoint creation** (`backuptc()`) for staff records.
* **Restore student data** (`restorest()`) from the latest checkpoint.
* **Restore teacher data** (`restoretc()`) to recover previously stored information.

These functions ensure **data can be recovered** in case of accidental deletion or corruption.

---

## **Technical Details**

* **Total Lines of Code:** 1950
* **Documentation:** 58 lines
* **Code:** 1892 lines
* **Functions:** 47

  * Security & Menu: 9
  * Student Management: 27
  * Teacher Management: 7
  * Backup & Restore: 4

The code is **modular**, making it easy to understand and extend. Functions are logically grouped and self-contained for maintainability.

---

## **Installation & Usage**

1. Ensure **Python 3.x** is installed on your system.
2. Download the project files.
3. Open a terminal/command prompt and navigate to the project directory.
4. Run the main script to launch the **menu-driven interface**:

   ```bash
   python main.py
   ```
5. Use the menu options to:

   * Manage **students**
   * Manage **teachers**
   * Enter or update **marks**
   * Backup or restore data

---

## **Advantages**

* Fully **menu-driven**, easy to use for non-technical users.
* **Secure** with password protection and encoding.
* Handles **both student and teacher records** efficiently.
* Enables **bulk or individual mark entry** and updates.
* **Backup and restore** ensures safe data management.
* Modular and **extensible**, allowing future features to be added easily.

---

## **Future Enhancements**

* Add **class-wise and stream-wise performance analytics**.
* Enable **multi-user access with role-based permissions**.
* Integrate **GUI for better user experience**.
* Add **report generation** in PDF or Excel format.

---

## **Contact**

* **Author:** Kunal (Github id : [Kunal-R-Kumar]([url](https://github.com/Kunal-R-kumar)))
* **Email:** [kkumar021104@gmail.com](mailto:kkumar021104@gmail.com)
