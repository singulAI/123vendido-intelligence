from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

@dataclass(frozen=True)
class ScheduledJob:
    job_type: str
    payload: dict
    run_at: datetime | None = None
    queue: str = "default"

class Scheduler(Protocol):
    async def enqueue(self, job: ScheduledJob) -> str: ...

class InMemoryScheduler:
    def __init__(self):
        self.jobs: list[ScheduledJob] = []
    async def enqueue(self, job: ScheduledJob) -> str:
        self.jobs.append(job)
        return f"memory-job-{len(self.jobs)}"
