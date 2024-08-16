from mlproject import logger
from mlproject.pipeline.data_ingestion_stage import DataIngestionTrainingPipeline
from mlproject.pipeline.data_validation_stage import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"==== stage {STAGE_NAME} started =====")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"==== stage {STAGE_NAME} completed ====\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"

try:
    logger.info(f"==== stage {STAGE_NAME} started ====")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"==== stage {STAGE_NAME} completed ====\n\n")
except Exception as e:
    logger.exception(e)
    raise e