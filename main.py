from mlproject import logger
#from src.mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataInjectioTrainingPipeline

STAGE_NAME = "Data Injection stage"

try:
    logger.info(f">>>>>>>>>{STAGE_NAME} started<<<<<<<<")
    data_injection = DataInjectioTrainingPipeline()
    data_injection.main()
    logger.info(f">>>>>>>>>{STAGE_NAME} completed<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

