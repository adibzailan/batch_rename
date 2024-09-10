import sys
import logging
import datetime
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer, QThread, pyqtSignal
from ui.main_window import BatchRenameUI
from ui.splash_screen import SplashScreen

# Set up logging
log_filename = f"batch_rename_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(log_filename),
                        logging.StreamHandler(sys.stdout)
                    ])

class InitThread(QThread):
    update_progress = pyqtSignal(int)
    error_occurred = pyqtSignal(str)
    
    def run(self):
        try:
            logging.info("Starting initialization tasks")
            # Simulate initialization tasks
            for i in range(1, 101):
                # Perform actual initialization tasks here
                self.msleep(30)  # Simulate work being done
                self.update_progress.emit(i)
            logging.info("Initialization tasks completed")
        except Exception as e:
            logging.error(f"Error during initialization: {str(e)}")
            self.error_occurred.emit(str(e))

def main():
    logging.info("Starting application")
    app = QApplication(sys.argv)
    
    try:
        # Show splash screen
        logging.info("Creating splash screen")
        splash = SplashScreen()
        splash.show()

        # Initialize main window
        logging.info("Creating main window")
        window = BatchRenameUI()

        # Function to update splash screen progress
        def update_splash_progress(value):
            splash.progress.setValue(value)
            logging.debug(f"Splash screen progress: {value}%")

        # Function to show main window and close splash screen
        def show_main_window():
            def close_splash_and_show_main():
                logging.info("Closing splash screen and showing main window")
                splash.close()
                window.show()
            
            # Add a small delay before closing splash and showing main window
            QTimer.singleShot(500, close_splash_and_show_main)

        # Function to handle initialization errors
        def handle_init_error(error_msg):
            logging.error(f"Initialization error: {error_msg}")
            splash.close()
            QMessageBox.critical(None, "Initialization Error", f"An error occurred during initialization: {error_msg}")
            app.quit()

        # Create and start initialization thread
        logging.info("Starting initialization thread")
        init_thread = InitThread()
        init_thread.update_progress.connect(update_splash_progress)
        init_thread.finished.connect(show_main_window)
        init_thread.error_occurred.connect(handle_init_error)
        init_thread.start()

        logging.info("Entering main event loop")
        exit_code = app.exec()
        logging.info(f"Application exiting with code: {exit_code}")
        return exit_code

    except Exception as e:
        logging.critical(f"Unhandled exception in main: {str(e)}")
        QMessageBox.critical(None, "Critical Error", f"An unhandled error occurred: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())