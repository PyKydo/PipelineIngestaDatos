import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: (message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    
    logger.info("La aplicación ha iniciado correctamente")