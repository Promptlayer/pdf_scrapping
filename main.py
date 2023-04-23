import os
import sys
import csv
from datetime import datetime
try:
    from sub_tools.tool_datascience.interface_ui import Ui_LLMandSCRAP
except ImportError:
    from interface_ui import Ui_LLMandSCRAP

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Slot, QThread, Signal
from PySide6.QtGui import QKeySequence, QStandardItemModel, QStandardItem, QShortcut


import PyPDF2
import pdfplumber
import re
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import spacy

# import ressources_rc

class Worker(QThread):
    progress = Signal(int)
    def __init__(self, parent=None):
        super().__init__(parent)

    def create_data(self, method_number, progress_callback):
        if method_number == 1:
            self.create_data_method_1(progress_callback)
        elif method_number == 2:
            self.create_data_method_2(progress_callback)
        elif method_number == 3:
            self.create_data_method_3(self.parent().edit_2.text(), progress_callback)
        else:
            self.create_data_method_4(self.parent().edit_2.text(), progress_callback)


    def run(self):
        for i in range(101):
            QThread.sleep(1)
            self.progress.emit(i)
            
    
    def create_data_method_1(self, progress_callback):
        pdf_file = self.parent().edit_1.text()

        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            result_list = []

            for page_number in range(num_pages):
                with pdfplumber.open(pdf_file) as pdf:
                    progress_callback(int((page_number / num_pages) * 100))
                    page = pdf.pages[page_number]
                    text = page.extract_text()

                    formula_pattern = re.compile(r'\b(?P<formula_name>[A-Za-z0-9_]+)\s*=\s*(?P<formula>[^,]+)')
                    explanation_pattern = re.compile(r'(?P<explanation>[A-Za-z0-9_\-\s]+)')

                    for match in formula_pattern.finditer(text):
                        formula_name = match.group('formula_name')
                        formula = match.group('formula')

                        explanation_match = explanation_pattern.search(text, match.end())
                        if explanation_match:
                            explanation = explanation_match.group('explanation')
                        else:
                            explanation = 'Nicht gefunden'

                        result_list.append([formula_name, formula, explanation])

        for index, item in enumerate(result_list):
            self.parent().tableWidget_1.insertRow(index)
            for col, data in enumerate(item):
                self.parent().tableWidget_1.setItem(index, col, QTableWidgetItem(str(data)))
            self.parent().tableWidget_1.resizeColumnsToContents()


    def create_data_method_2(self, progress_callback):
        nlp = spacy.load("en_core_web_sm")
        pdf_file = self.parent().edit_1.text()

        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            result_list = []

            for page_number in range(num_pages):
                with pdfplumber.open(pdf_file) as pdf:
                    progress_callback(int((page_number / num_pages) * 100))
                    page = pdf.pages[page_number]
                    text = page.extract_text()

                    doc = nlp(text)

                    for sent in doc.sents:
                        if "Formel" or "Kalkulation" in sent.text:
                            formula_name = sent.text.strip()
                            explanation_text = sent.next_sentence.text.strip()

                            result_list.append([formula_name, explanation_text])

        for index, item in enumerate(result_list):
            self.parent().tableWidget_1.insertRow(index)
            for col, data in enumerate(item):
                self.parent().tableWidget_1.setItem(index, col, QTableWidgetItem(str(data)))
            self.parent().tableWidget_1.resizeColumnsToContents()



    def create_data_method_3(self, url, progress_callback):
        
        nlp = spacy.load("en_core_web_sm")

        url = self.parent().edit_2.text()
        response = requests.get(url)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for script in soup(["script", "style"]):
            script.decompose()

        page_text = soup.get_text()
        doc = nlp(page_text)

        result_list = []

        for sent in doc.sents:
            if "Formel" or "Kalkulation" in sent.text:
                progress_callback(int((sent / doc.sents) * 100))
                formula_name = sent.text.strip()
                explanation_text = sent.next_sentence.text.strip()

                result_list.append([formula_name, explanation_text])

        for index, item in enumerate(result_list):
            self.parent().tableWidget_2.insertRow(index)
            for col, data in enumerate(item):
                self.parent().tableWidget_2.setItem(index, col, QTableWidgetItem(str(data)))
            self.parent().tableWidget_2.resizeColumnsToContents()



    def create_data_method_4(self, url, progress_callback):
        url = self.parent().edit_2.text()

        response = requests.get(url)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        formula_pattern = re.compile(r'\b(?P<formula_name>[A-Za-z0-9_]+)\s*=\s*(?P<formula>[^,;\n]+)')
        explanation_pattern = re.compile(r'(?P<explanation>[A-Za-z0-9_\-\s\+\-\*/\^%\(\)]+)')

        formulas = soup.select(formula_pattern)
        explanations = soup.select(explanation_pattern)

        result_list = []

        for formula, explanation in zip(formulas, explanations):
            progress_callback(int((formula / formulas) * 100))
            formula_name = formula.text.strip()
            explanation_text = explanation.text.strip()

            result_list.append([formula_name, explanation_text])

        for index, item in enumerate(result_list):
            self.parent().tableWidget_2.insertRow(index)  # Änderung hier
            for col, data in enumerate(item):
                self.parent().tableWidget_2.setItem(index, col, QTableWidgetItem(str(data)))  # Änderung hier
            self.parent().tableWidget_2.resizeColumnsToContents()  # Änderung hier



    def compare_tables(self):
        table_1 = self.parent().tableWidget_1
        table_2 = self.parent().tableWidget_2
        table_3 = self.parent().tableWidget_3

        # Löschen Sie alle Zeilen in der Vergleichstabelle, bevor Sie Daten hinzufügen
        while table_3.rowCount() > 0:
            table_3.removeRow(0)

        for row in range(table_1.rowCount()):
            item_1 = table_1.item(row, 0)
            item_2 = table_2.item(row, 0)

            if item_1 and item_2 and item_1.text() == item_2.text():
                table_3.insertRow(table_3.rowCount())
                for col in range(table_1.columnCount()):
                    item = QTableWidgetItem(item_1.text())
                    table_3.setItem(table_3.rowCount() - 1, col, item)
                table_3.resizeColumnsToContents()


class DataScienceTool(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.errors = []
        self.datascience_ui = Ui_LLMandSCRAP()
        self.datascience_ui.setupUi(self)

        # self.ressources_rc = ressources_rc

        self.combo_1 = self.datascience_ui.combo_1 # Die vier Methoden
        self.combo_1.addItems(["PDF - Plumber", "PDF - Spacy", "URL - Spacy", "URL - BeautifulSoup"])
        self.combo_1.setEditable(False)
        self.combo_1.currentIndexChanged.connect(self.combo_1_changed)

        self.combo_2 = self.datascience_ui.combo_2 # [1,2] Tabelle 1 oder 2
        
        self.combo_3 = self.datascience_ui.combo_3
        
        self.casual_button_1 = self.datascience_ui.casual_button_1 # PDF-Datei oder Textfile auswählen
        self.casual_button_2 = self.datascience_ui.casual_button_2 # Resultate in CSV-Datei speichern
        self.casual_button_3 = self.datascience_ui.casual_button_3 # Vergleichen starten

        self.green_button = self.datascience_ui.green_button # Methoden abrufen starten
        self.green_button.setEnabled(False)

        self.red_button = self.datascience_ui.red_button # In combo_2 ausgewählte Tabelle löschen

        self.edit_1 = self.datascience_ui.edit_1 # Pfad zur PDF-Datei
        self.edit_2 = self.datascience_ui.edit_2 # URL der Webseite, von der Sie die Formeln und Erklärungen extrahieren möchten
        self.edit_2.setPlaceholderText("https://your_website_url.com")
        
        self.edit_3 = self.datascience_ui.edit_3

        self.progress_bar = self.datascience_ui.progress_bar # Fortschrittsbalken

        self.tableWidget_1 = self.datascience_ui.tableWidget_1 # Tabelle 1
        self.tableWidget_1.horizontalHeaderItem(0).setText('Formel')
        self.tableWidget_1.horizontalHeaderItem(1).setText('Beschreibung')
        self.tableWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget_2 = self.datascience_ui.tableWidget_2 # Tabelle 2
        self.tableWidget_2.horizontalHeaderItem(0).setText('Formel')
        self.tableWidget_2.horizontalHeaderItem(1).setText('Beschreibung')
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget_3 = self.datascience_ui.tableWidget_3 # Tabelle 3 - Vergleichsresultate
        self.tableWidget_3.horizontalHeaderItem(0).setText('Formel')
        self.tableWidget_3.horizontalHeaderItem(1).setText('Beschreibung')
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.stackedWidget = self.datascience_ui.stackedWidget

        self.page_1 = self.datascience_ui.page_1
        self.page_2 = self.datascience_ui.page_2

        self.nav_button_1 = self.datascience_ui.nav_button_1 
        self.nav_button_2 = self.datascience_ui.nav_button_2
        self.nav_button_3 = self.datascience_ui.nav_button_3

        self.list_created = self.datascience_ui.list_created
        self.list_created.setStyleSheet("color: #d9deee;")
        self.data_selected = self.datascience_ui.data_selected
        self.data_selected.setStyleSheet("color: #d9deee;")

        self.nav_button_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.nav_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        self.casual_button_1.clicked.connect(self.open_file)
        self.casual_button_2.clicked.connect(self.save_data_to_csv)
        self.casual_button_3.clicked.connect(self.compare_tables)   

        self.green_button.clicked.connect(self.run_selected_method)

        copy_shortcut = QShortcut(QKeySequence("Ctrl+C"), self)
        copy_shortcut.activated.connect(self.copy_selection)

        self.tableWidget_1 = self.datascience_ui.tableWidget_1
        self.tableWidget_2 = self.datascience_ui.tableWidget_2
        self.tableWidget_3 = self.datascience_ui.tableWidget_3


    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Öffnen Sie die PDF-Datei", "", "PDF-Dateien (*.pdf)", options=options)
        if file_name:
            self.edit_1.setText(file_name)
            if self.combo_1.currentIndex() == 0:
                self.green_button.setEnabled(True)
                self.data_selected.setStyleSheet("color: #000000;")

    def combo_1_changed(self):
        if self.combo_1.currentIndex() == 0 or self.combo_1.currentIndex() == 1:
            if self.edit_1.text() == "":
                self.green_button.setEnabled(False)
                self.data_selected.setStyleSheet("color: #d9deee;")
            else:
                self.green_button.setEnabled(True)
                self.data_selected.setStyleSheet("color: #000000;")

        elif self.combo_1.currentIndex() == 2 or self.combo_1.currentIndex() == 3:
            if self.edit_2.text() == "":
                self.green_button.setEnabled(False)
                self.data_selected.setStyleSheet("color: #d9deee;")
            else:
                self.green_button.setEnabled(True)
                self.data_selected.setStyleSheet("color: #000000;")


    def run_selected_method(self):
        method_number = self.combo_1.currentIndex() + 1
        self.worker = Worker(self)
        self.worker.progress.connect(self.update_progress_bar)
        self.worker.create_data(method_number, self.update_progress_bar)
        self.worker.start()

        if method_number in [1, 2]:
            self.tableWidget = self.tableWidget_1
        elif method_number in [3, 4]:
            self.tableWidget = self.tableWidget_2
        else:
            self.tableWidget = self.tableWidget_3




    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)
        if value == 100:
            self.list_created.setStyleSheet("color: #000000;")

    @Slot()
    def show_data_selected_label(self):
        self.data_selected.setVisible(True)
        self.data_selected.setStyleSheet("color: #000000;")

    @Slot()
    def show_list_created_label(self):
        self.list_created.setVisible(True)
        self.list_created.setStyleSheet("color: #000000;")

    def save_data_to_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Daten als CSV speichern", "", "CSV-Dateien (*.csv)", options=options)
        if file_name:
            if not file_name.endswith('.csv'):
                file_name += '.csv'
            
            with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                
                # Write header row
                header = []
                for col in range(self.tableWidget.columnCount()):
                    header.append(self.tableWidget.horizontalHeaderItem(col).text())
                writer.writerow(header)

                # Write data rows
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for col in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, col)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
   
    def compare_tables(self):
        self.tableWidget_3.clear()
        self.tableWidget_3.setRowCount(self.tableWidget_1.rowCount())
        self.tableWidget_3.setColumnCount(self.tableWidget_1.columnCount())

        for row in range(self.tableWidget_1.rowCount()):
            for col in range(self.tableWidget_1.columnCount()):
                item_1 = self.tableWidget_1.item(row, col)
                item_2 = self.tableWidget_2.item(row, col)
                if item_1 is not None and item_2 is not None:
                    if item_1.text() == item_2.text():
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem(item_1.text()))
                    else:
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem("X"))
                else:
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem("X"))

    def copy_selection(self):
        selected_ranges = self.tableWidget.selectedRanges()
        if not selected_ranges:
            return

        selected_range = selected_ranges[0]
        text = ""
        for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
            row_text = []
            for col in range(selected_range.leftColumn(), selected_range.rightColumn() + 1):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    row_text.append(item.text())
                else:
                    row_text.append('')
            text += '\t'.join(row_text) + '\n'

        clipboard = QApplication.clipboard()
        clipboard.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = DataScienceTool()
    main_window.show()
    sys.exit(app.exec())