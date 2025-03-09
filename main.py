from mlproject import logger
#from src.mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataInjectioTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Injection stage"

try:
    logger.info(f">>>>>>>>>{STAGE_NAME} started<<<<<<<<")
    data_injection = DataInjectioTrainingPipeline()
    data_injection.main()
    logger.info(f">>>>>>>>>{STAGE_NAME} completed<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
