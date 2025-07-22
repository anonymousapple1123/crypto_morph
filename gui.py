# gui.py
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QTextEdit, QLabel, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from crypto.rsa_handler import RSAHandler
from crypto.file_handler import read_file, write_file
import os
import datetime


class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSA Encryption GUI")
        self.setMinimumWidth(600)

        self.rsa = RSAHandler()

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Input Text:")
        self.input_text = QTextEdit()

        self.output_label = QLabel("Output Text:")
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.load_button = QPushButton("Load from File")
        self.encrypt_button = QPushButton("Encrypt")
        self.decrypt_button = QPushButton("Decrypt")
        self.save_button = QPushButton("Save Output to File")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.load_button)
        btn_layout.addWidget(self.encrypt_button)
        btn_layout.addWidget(self.decrypt_button)
        btn_layout.addWidget(self.save_button)

        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_text)
        self.layout.addLayout(btn_layout)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_text)

        self.setLayout(self.layout)

        self.load_button.clicked.connect(self.load_file)
        self.encrypt_button.clicked.connect(self.encrypt_text)
        self.decrypt_button.clicked.connect(self.decrypt_text)
        self.save_button.clicked.connect(self.save_output)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)")
        if path:
            content = read_file(path)
            self.input_text.setPlainText(content)

    def encrypt_text(self):
        plain_text = self.input_text.toPlainText()
        if not plain_text:
            QMessageBox.warning(self, "Error", "No input text to encrypt.")
            return
        try:
            encrypted = self.rsa.encrypt(plain_text)
            self.output_text.setPlainText(encrypted)
        except Exception as e:
            QMessageBox.critical(self, "Encryption Error", str(e))

    def decrypt_text(self):
        cipher_text = self.input_text.toPlainText()
        if not cipher_text:
            QMessageBox.warning(self, "Error", "No input text to decrypt.")
            return
        try:
            decrypted = self.rsa.decrypt(cipher_text)
            self.output_text.setPlainText(decrypted)
        except Exception as e:
            QMessageBox.critical(self, "Decryption Error", str(e))

    def save_output(self):
        text = self.output_text.toPlainText()
        if not text:
            QMessageBox.warning(self, "Error", "No output text to save.")
            return
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/encrypted_{timestamp}.txt"
        os.makedirs("output", exist_ok=True)
        write_file(filename, text)
        QMessageBox.information(self, "Saved", f"Output saved to {filename}")
