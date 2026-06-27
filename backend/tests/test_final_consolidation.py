from app.domain.context_builder.contracts import AIContextBuilder, AIContextBuilderInput
from app.domain.decision.contracts import DecisionEngine, DecisionInput
from app.domain.plugins.contracts import PluginKind
from app.domain.radar.contracts import AlertKind
from app.domain.score.contracts import Score360
from app.domain.timeline.contracts import TimelineEventType
from app.infrastructure.seeds.demo import build_demo_seed_summary


def test_score_360_and_decision_engine_consolidate_result():
    score = Score360.weighted(opportunity_score=90, risk_score=20, repair_score=80, market_score=70, liquidity_score=65, roi_score=95, confidence_score=80)
    decision = DecisionEngine().decide(DecisionInput(lot_id="lot-1", score_360=score))
    assert decision.final_decision_score == score.final_auction_score
    assert decision.recommendation in {"buy", "watch", "avoid"}


def test_timeline_radar_and_plugins_are_prepared():
    assert TimelineEventType.FIPE_CHANGED.value == "fipe_changed"
    assert AlertKind.VEHICLE.value == "vehicle_alert"
    assert PluginKind.GOVERNMENT_API.value == "government_api"


def test_ai_context_builder_never_uses_images_only():
    context = AIContextBuilder().build(AIContextBuilderInput(images=[{"url": "mock"}], lot={"number": "1"}, vehicle={"make": "VW"}))
    assert context.images
    assert context.lot["number"] == "1"
    assert context.vehicle["make"] == "VW"
    assert context.sources[0].origin == "ai_context_builder"


def test_demo_seed_plan_targets_scale():
    summary = build_demo_seed_summary()
    assert summary["auctions"] >= 300
    assert summary["lots"] >= 5000
    assert summary["vehicles"] >= 5000
