import logging
from batch_rename_ui import BatchRenameUI

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    app = BatchRenameUI()
    app.run()