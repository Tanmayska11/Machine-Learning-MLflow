from  mlproject.config.configuration import ConfigurationManager
from  mlproject.components.data_ingestion import DataIngestion
from mlproject import logger



STAGE_NAME = "Data Injection stage"

class DataInjectioTrainingPipeline:
    def __init__(self): 
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>{STAGE_NAME} started <<<<<<<<<")
        obj =DataInjectionPipeline()
        obj.main()
        logger.info(f">>>>>>>>{STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e