

class Validator:
    @staticmethod
    def validate_time(time: str) -> bool:
        if not time:
            return False
        try:
            time_parts = time.split(":")
            if len(time_parts) != 2:
                return False

            hour = int(time_parts[0])
            minute = int(time_parts[1])

            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                return False

            return True
        except ValueError:
            return False

    @staticmethod
    def validate_note(note: str) -> bool:
        if not note or len(note) <= 3:
            return False
        return True

