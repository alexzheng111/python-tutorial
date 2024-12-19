from fastapi_tutorial.qb_rating.models import QuarterBackStatistics


def calculate_quarterback_rating(stats: QuarterBackStatistics) -> float:
    completion_percentage = stats.completions / stats.attempts
    yards_per_attempt = stats.yards / stats.attempts
    touchdowns_per_attempt = stats.touchdowns / stats.attempts
    interceptions_per_attempts = stats.interceptions / stats.attempts

    a = clip((completion_percentage - 0.3) * 5, 0, 2.375)
    b = clip((yards_per_attempt - 3) * 0.25, 0, 2.375)
    c = clip(touchdowns_per_attempt * 20, 0, 2.375)
    d = clip(2.375 - (interceptions_per_attempts * 25), 0, 2.375)

    passer_rating = (a + b + c + d) * 100 / 6
    return passer_rating


def clip(number: float, min_value: float, max_value: float) -> float:
    return max(min(number, max_value), min_value)
