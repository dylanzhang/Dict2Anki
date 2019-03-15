try:
    from aqt import mw
    from .addon.addonWindow import Windows
    from PyQt5.QtWidgets import QAction


    def showWindow():
        w = Windows()
        w.exec()


    action = QAction("Dick2Anki...", mw)
    action.triggered.connect(showWindow)
    mw.form.menuTools.addAction(action)

except ImportError:
    import os
    from PyQt5.QtWidgets import QApplication
    from addon.addonWindow import Windows
    import sys
    if os.environ.get('dict2anki-dev'):
        app = QApplication(sys.argv)
        window = Windows()
        window.show()
        sys.exit(app.exec())
