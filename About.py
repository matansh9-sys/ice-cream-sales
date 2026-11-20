from pathlib import Path

from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About me")
        self.setGeometry(150, 150, 380, 540)
        self.setStyleSheet(
            "QWidget { background-color: #111827; color: #f9fafb; }"
        )

        self.title_label = QLabel("ABOUT ME", self)
        self.title_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #93c5fd;"
        )
        self.title_label.adjustSize()
        self.title_label.move((self.width() - self.title_label.width()) // 2, 12)

        self.photo_label = QLabel(self)
        self.photo_label.setGeometry(50, 55, 280, 280)
        self.photo_label.setStyleSheet(
            "background-color: #1f2937; border: 3px solid #374151; "
            "border-radius: 12px; padding: 5px;"
        )
        image_path = Path(__file__).with_name("about_photo.jpeg")
        photo = QPixmap(str(image_path))
        if photo.isNull():
            raise FileNotFoundError(f"Could not load profile image: {image_path}")
        self.photo_label.setPixmap(
            photo.scaled(
                260,
                260,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

        self.details_card = QWidget(self)
        self.details_card.setObjectName("detailsCard")
        self.details_card.setGeometry(35, 350, 310, 120)
        self.details_card.setStyleSheet(
            "QWidget#detailsCard { background-color: #1f2937; "
            "border: 1px solid #374151; border-radius: 12px; }"
        )

        self.name_label = QLabel("Matan Shoel", self.details_card)
        self.name_label.setGeometry(14, 8, 280, 28)
        self.name_label.setStyleSheet(
            "background: transparent; border: none; padding: 0; "
            "font-size: 17px; font-weight: bold; color: #bfdbfe;"
        )

        self.email_label = QLabel("Email:", self.details_card)
        self.email_label.setGeometry(14, 44, 80, 24)
        self.email_label.setStyleSheet(
            "background: transparent; border: none; padding: 0; color: #f9fafb;"
        )
        self.email_button = QPushButton("matansh9@gmail.com", self.details_card)
        self.email_button.setGeometry(98, 42, 205, 28)
        self.email_button.setStyleSheet(
            "background: transparent; color: #60a5fa; text-align: left; "
            "border: none; padding: 0; font-size: 11px;"
        )
        self.email_button.clicked.connect(self._open_email)

        self.instagram_label = QLabel("Instagram:", self.details_card)
        self.instagram_label.setGeometry(14, 78, 128, 24)
        self.instagram_label.setStyleSheet(
            "background: transparent; border: none; padding: 0; color: #f9fafb;"
        )
        self.instagram_button = QPushButton("Open profile", self.details_card)
        self.instagram_button.setGeometry(146, 76, 142, 28)
        self.instagram_button.setStyleSheet(
            "background: transparent; color: #60a5fa; text-align: left; "
            "border: none; padding: 0; font-size: 11px;"
        )
        self.instagram_button.clicked.connect(self._open_instagram)

        self.github_button = QPushButton("GitHub Repository", self)
        self.github_button.setGeometry(35, 485, 310, 32)
        self.github_button.clicked.connect(self._open_github)

    
    
    def _open_github(self):

        QDesktopServices.openUrl(
            QUrl("https://github.com/matansh9-sys/ice-cream-sales")
        )



    def _open_email(self):
        QDesktopServices.openUrl(QUrl("mailto:matansh9@gmail.com"))

    def _open_instagram(self):
        QDesktopServices.openUrl(
            QUrl("https://www.instagram.com/matanshoel/")
        )


def main():
    app = QApplication([])
    window = AboutWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
