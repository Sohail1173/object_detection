import logging
from datetime import datetime
import os

logging_file=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
# logging_file = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
print(logging_file)


logging_dir=os.path.join(os.getcwd(),"log",logging_file)

os.makedirs(logging_dir,exist_ok=True)

log_file=os.path.join(logging_dir,logging_file)

logging.basicConfig(filename=log_file,format="[%(asctime)s] %(name)s-%(levelname)s-%(message)s",level=logging.INFO)
