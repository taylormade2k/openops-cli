from ..utils.logger import get_logger

logger = get_logger(__name__)

def run(input_path, output_path=None):
    logger.info("Starting process...")
    logger.info(f"Processing file: {input_path}")
    print(f"✅ Completed processing {input_path}")
