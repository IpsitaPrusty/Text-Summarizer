from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from TextSummarizer.logging import logger

logger.info("welcome to the TextSummarizer project!")


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e