from dataclasses import dataclass

@dataclass(frozen=True)
class DemoSeedPlan:
    organizations: int = 10
    users: int = 100
    organizers: int = 80
    auctions: int = 300
    lots: int = 5000
    vehicles: int = 5000
    payments: int = 500
    notifications: int = 2000

DEMO_SEED_PLAN = DemoSeedPlan()

def build_demo_seed_summary(plan: DemoSeedPlan = DEMO_SEED_PLAN) -> dict:
    return plan.__dict__ | {"mode": "deterministic-factories-pending-db-runtime"}
