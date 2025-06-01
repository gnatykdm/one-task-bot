from utils.logs import setup_logger
from logging import Logger

logger: Logger = setup_logger()

class Validator:
    @staticmethod
    def validate_time(time: str) -> bool:
        if not time:
            logger.error("Invalid time: empty input")
            return False

        try:
            time_parts = time.split(":")
            if len(time_parts) != 2:
                logger.error(f"Invalid time format: {time}")
                return False

            hour = int(time_parts[0])
            minute = int(time_parts[1])

            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                logger.error(f"Time out of range: {time}")
                return False

            return True
        except ValueError:
            logger.error(f"Non-integer values in time: {time}")
            return False
