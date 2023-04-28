import logging

LOG_DIR = "housing_log"

CURRENT_TIME_STEP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%s')}"

LOG_FILE_NAME = f"log_{CURRENT_TIME_STEP}.log"

os.mkdirs(LOG_DIR)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO
                    )