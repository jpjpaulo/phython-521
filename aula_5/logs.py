# Modulo de logs do python
import os
import logging

import dotenv


dotenv.load_dotenv()

FORMAT_STRING = '''

%(asctime)s | %(levelname)s | 
%(filename)s | %(message)s

'''.replace('\n', '').strip()

DATE_FORMAT_STRING = '''

%d/%m/%Y %H:%M:%S

'''.replace('\n', '').strip()

opts = {
	'filename': 'app.log',
	'level': int(os.getenv('DEBUG_LEVEL') or 0),
	'format': FORMAT_STRING,
	'datefmt': DATE_FORMAT_STRING
}
logging.basicConfig(**opts)

logging.debug('mensagem de DEBUG')
logging.info('Vai Corinthians')
logging.warning('mensagem de WARNING')
logging.error("mensagem de ERROR")
logging.critical('mensagem de CRITICAL')