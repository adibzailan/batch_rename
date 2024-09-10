import sys
import logging
import datetime
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer, QThread, pyqtSignal, QEventLoop
from ui.main_window import BatchRenameUI
from ui.splash_screen import SplashScreen

# Set up logging
log_filename = f"batch_rename_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(level=logging.DEBUG,  # Changed to DEBUG for more detailed logging
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(log_filename),
                        logging.StreamHandler(sys.stdout)
                    ])

print("Logging initialized")

class InitThread(QThread):
    update_progress = pyqtSignal(int)
    initialization_complete = pyqtSignal()
    error_occurred = pyqtSignal(str)
    
    def run(self):
        try:
            logging.info("Starting initialization tasks")
            print("Initialization tasks started")
            # Simulate initialization tasks
            for i in range(1, 101):
                self.msleep(30)  # Simulate work being done
                self.update_progress.emit(i)
                if i % 10 == 0:
                    print(f"Initialization progress: {i}%")
            
            logging.info("Initialization tasks completed")
            print("Initialization tasks completed")
            self.initialization_complete.emit()
        except Exception as e:
            logging.error(f"Error during initialization: {str(e)}")
            print(f"Error during initialization: {str(e)}")
            self.error_occurred.emit(str(e))

def main():
    logging.info("Starting application")
    print("Starting application")
    app = QApplication(sys.argv)
    
    try:
        # Show splash screen
        logging.info("Creating splash screen")
        print("Creating splash screen")
        splash = SplashScreen()
        splash.show()

        # Create main window (but don't show it yet)
        logging.info("Creating main window")
        print("Creating main window")
        window = BatchRenameUI()
        
        # Create an event loop to keep the application running
        event_loop = QEventLoop()

        # Function to update splash screen progress
        def update_splash_progress(value):
            splash.progress.setValue(value)
            logging.debug(f"Splash screen progress: {value}%")

        # Function to show main window and close splash screen
        def show_main_window():
            logging.info("Preparing to show main window")
            print("Preparing to show main window")
            
            def close_splash_and_show_main():
                logging.info("Closing splash screen and showing main window")
                print("Closing splash screen and showing main window")
                splash.close()
                window.show()
                logging.info("Main window displayed")
                print("Main window displayed")
            
            # Add a small delay before closing splash and showing main window
            QTimer.singleShot(500, close_splash_and_show_main)

        # Function to handle initialization errors
        def handle_init_error(error_msg):
            logging.error(f"Initialization error: {error_msg}")
            print(f"Initialization error: {error_msg}")
            splash.close()
            QMessageBox.critical(None, "Initialization Error", f"An error occurred during initialization: {error_msg}")
            event_loop.quit()

        # Create and start initialization thread
        logging.info("Starting initialization thread")
        print("Starting initialization thread")
        init_thread = InitThread()
        init_thread.update_progress.connect(update_splash_progress)
        init_thread.initialization_complete.connect(show_main_window)
        init_thread.error_occurred.connect(handle_init_error)
        init_thread.start()

        # Connect the main window's close event to quit the event loop
        window.closeEvent = lambda event: event_loop.quit()

        logging.info("Entering main event loop")
        print("Entering main event loop")
        event_loop.exec()
        
        logging.info("Event loop finished")
        print("Event loop finished")

        return 0

    except Exception as e:
        logging.critical(f"Unhandled exception in main: {str(e)}")
        print(f"Unhandled exception in main: {str(e)}")
        QMessageBox.critical(None, "Critical Error", f"An unhandled error occurred: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())