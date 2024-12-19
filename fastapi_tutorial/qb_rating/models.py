from pydantic import BaseModel


class QuarterBackStatistics(BaseModel):
    name: str
    completions: int
    attempts: int
    yards: int
    touchdowns: int
    interceptions: int
