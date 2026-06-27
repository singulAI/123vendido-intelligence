from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, JSON, Numeric, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.domain.common.entities import TimestampMixin, UUIDMixin
from app.infrastructure.database.base import Base

class Organization(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "organizations"
    name: Mapped[str] = mapped_column(String(160), index=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    settings: Mapped[dict] = mapped_column(JSON, default=dict)

class User(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str | None] = mapped_column(String(160))
    hashed_password: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    organization_id = mapped_column(ForeignKey("organizations.id"), nullable=True)

class PermissionGroup(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "permission_groups"
    name: Mapped[str] = mapped_column(String(120), unique=True)
    description: Mapped[str | None] = mapped_column(Text)

class Permission(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "permissions"
    code: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    description: Mapped[str | None] = mapped_column(Text)
    group_id = mapped_column(ForeignKey("permission_groups.id"))

class Role(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "roles"
    name: Mapped[str] = mapped_column(String(120), unique=True)
    permissions = relationship("Permission", secondary="role_permissions")

class RolePermission(Base):
    __tablename__ = "role_permissions"
    role_id = mapped_column(ForeignKey("roles.id"), primary_key=True)
    permission_id = mapped_column(ForeignKey("permissions.id"), primary_key=True)

class UserRole(Base):
    __tablename__ = "user_roles"
    user_id = mapped_column(ForeignKey("users.id"), primary_key=True)
    role_id = mapped_column(ForeignKey("roles.id"), primary_key=True)
    organization_id = mapped_column(ForeignKey("organizations.id"), primary_key=True)

class Product(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(120)); description: Mapped[str | None] = mapped_column(Text)
class Plan(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "plans"
    product_id = mapped_column(ForeignKey("products.id")); name: Mapped[str] = mapped_column(String(120)); price_cents: Mapped[int] = mapped_column(Integer, default=0); features: Mapped[dict] = mapped_column(JSON, default=dict)
class Trial(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "trials"
    plan_id = mapped_column(ForeignKey("plans.id")); days: Mapped[int] = mapped_column(Integer, default=7)
class Coupon(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "coupons"
    code: Mapped[str] = mapped_column(String(80), unique=True); discount_percent: Mapped[int] = mapped_column(Integer, default=0)
class Subscription(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "subscriptions"
    organization_id = mapped_column(ForeignKey("organizations.id")); plan_id = mapped_column(ForeignKey("plans.id")); status: Mapped[str] = mapped_column(String(40), default="trialing")
class Payment(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "payments"
    subscription_id = mapped_column(ForeignKey("subscriptions.id")); amount_cents: Mapped[int] = mapped_column(Integer); provider: Mapped[str] = mapped_column(String(80), default="pix"); status: Mapped[str] = mapped_column(String(40))
class Invoice(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "invoices"
    payment_id = mapped_column(ForeignKey("payments.id"), nullable=True); number: Mapped[str] = mapped_column(String(80), unique=True); payload: Mapped[dict] = mapped_column(JSON, default=dict)
class PixConfiguration(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "pix_configurations"
    organization_id = mapped_column(ForeignKey("organizations.id")); provider: Mapped[str] = mapped_column(String(80)); credentials_ref: Mapped[str] = mapped_column(String(255))

class ConnectorConfiguration(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "connector_configurations"
    provider: Mapped[str] = mapped_column(String(80), index=True); version: Mapped[str] = mapped_column(String(40), default="mock"); credentials_ref: Mapped[str | None] = mapped_column(String(255)); timeout_seconds: Mapped[int] = mapped_column(Integer, default=30); retry_policy: Mapped[dict] = mapped_column(JSON, default=dict); is_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
class ConnectorLog(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "connector_logs"
    provider: Mapped[str] = mapped_column(String(80)); status: Mapped[str] = mapped_column(String(40)); details: Mapped[dict] = mapped_column(JSON, default=dict)

class Job(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "jobs"
    type: Mapped[str] = mapped_column(String(60), index=True); status: Mapped[str] = mapped_column(String(40), default="queued"); payload: Mapped[dict] = mapped_column(JSON, default=dict); attempts: Mapped[int] = mapped_column(Integer, default=0); scheduled_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True))
class DeadLetterJob(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "dead_letter_jobs"
    job_id = mapped_column(ForeignKey("jobs.id")); reason: Mapped[str] = mapped_column(Text); payload: Mapped[dict] = mapped_column(JSON, default=dict)

class Organizer(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "organizers"
    name: Mapped[str] = mapped_column(String(160)); website: Mapped[str | None] = mapped_column(String(255))
class Auction(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "auctions"
    organizer_id = mapped_column(ForeignKey("organizers.id")); title: Mapped[str] = mapped_column(String(220)); official_url: Mapped[str | None] = mapped_column(String(500))
class AuctionNotice(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "auction_notices"
    auction_id = mapped_column(ForeignKey("auctions.id")); document_url: Mapped[str | None] = mapped_column(String(500)); extracted_text: Mapped[str | None] = mapped_column(Text)
class Lot(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "lots"
    auction_id = mapped_column(ForeignKey("auctions.id")); number: Mapped[str] = mapped_column(String(80)); official_url: Mapped[str | None] = mapped_column(String(500)); user_observations: Mapped[dict] = mapped_column(JSON, default=dict)
    __table_args__ = (UniqueConstraint("auction_id", "number"),)
class Vehicle(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "vehicles"
    lot_id = mapped_column(ForeignKey("lots.id")); make: Mapped[str | None] = mapped_column(String(80)); model: Mapped[str | None] = mapped_column(String(120)); year: Mapped[int | None] = mapped_column(Integer); plate: Mapped[str | None] = mapped_column(String(20)); metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)
class Analysis(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "analyses"
    lot_id = mapped_column(ForeignKey("lots.id")); version: Mapped[int] = mapped_column(Integer); engine: Mapped[str] = mapped_column(String(80)); result: Mapped[dict] = mapped_column(JSON, default=dict); confidence: Mapped[float | None] = mapped_column(Numeric(5, 4)); limitations: Mapped[list] = mapped_column(JSON, default=list)
class Favorite(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "favorites"
    user_id = mapped_column(ForeignKey("users.id")); lot_id = mapped_column(ForeignKey("lots.id"))
class Report(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "reports"
    user_id = mapped_column(ForeignKey("users.id")); lot_id = mapped_column(ForeignKey("lots.id"), nullable=True); payload: Mapped[dict] = mapped_column(JSON, default=dict)
class AuditLog(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "audit_logs"
    actor_id = mapped_column(ForeignKey("users.id"), nullable=True); action: Mapped[str] = mapped_column(String(160)); resource: Mapped[str] = mapped_column(String(160)); payload: Mapped[dict] = mapped_column(JSON, default=dict)

class Asset(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "assets"
    kind: Mapped[str] = mapped_column(String(40), index=True)
    filename: Mapped[str] = mapped_column(String(255))
    content_type: Mapped[str | None] = mapped_column(String(120))
    size_bytes: Mapped[int | None] = mapped_column(Integer)
    checksum_sha256: Mapped[str | None] = mapped_column(String(64), index=True)
    duplicate_of_id = mapped_column(ForeignKey("assets.id"), nullable=True)
    storage_provider: Mapped[str] = mapped_column(String(80), default="local")
    bucket: Mapped[str] = mapped_column(String(120))
    object_key: Mapped[str] = mapped_column(String(500))
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)
    ocr_status: Mapped[str] = mapped_column(String(40), default="pending")
    ai_status: Mapped[str] = mapped_column(String(40), default="pending")

class DataLakeEntry(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "data_lake_entries"
    source_type: Mapped[str] = mapped_column(String(80), index=True)
    source_id: Mapped[str] = mapped_column(String(80), index=True)
    stage: Mapped[str] = mapped_column(String(60), index=True)
    version: Mapped[int] = mapped_column(Integer, default=1)
    payload: Mapped[dict] = mapped_column(JSON, default=dict)
    parent_entry_id = mapped_column(ForeignKey("data_lake_entries.id"), nullable=True)
    immutable: Mapped[bool] = mapped_column(Boolean, default=False)

class VersionSnapshotModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "version_snapshots"
    resource_type: Mapped[str] = mapped_column(String(80), index=True)
    resource_id: Mapped[str] = mapped_column(String(80), index=True)
    version: Mapped[int] = mapped_column(Integer)
    payload: Mapped[dict] = mapped_column(JSON, default=dict)
    changed_by: Mapped[str | None] = mapped_column(String(80))
    change_reason: Mapped[str | None] = mapped_column(Text)
    __table_args__ = (UniqueConstraint("resource_type", "resource_id", "version"),)

class FeatureFlagModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "feature_flags"
    key: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    rollout_percentage: Mapped[int] = mapped_column(Integer, default=0)
    rules: Mapped[dict] = mapped_column(JSON, default=dict)

class PromptTemplateModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "prompt_templates"
    key: Mapped[str] = mapped_column(String(160), index=True)
    version: Mapped[int] = mapped_column(Integer, default=1)
    provider: Mapped[str | None] = mapped_column(String(80))
    template: Mapped[str] = mapped_column(Text)
    variables: Mapped[list] = mapped_column(JSON, default=list)
    temperature: Mapped[float] = mapped_column(Numeric(3, 2), default=0.2)
    max_tokens: Mapped[int | None] = mapped_column(Integer)
    fallback_template_key: Mapped[str | None] = mapped_column(String(160))
    __table_args__ = (UniqueConstraint("key", "version"),)

class AIUsageLog(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "ai_usage_logs"
    provider: Mapped[str] = mapped_column(String(80), index=True)
    model: Mapped[str] = mapped_column(String(120))
    prompt_template_key: Mapped[str | None] = mapped_column(String(160))
    prompt_version: Mapped[int | None] = mapped_column(Integer)
    cost_cents: Mapped[int] = mapped_column(Integer, default=0)
    latency_ms: Mapped[int | None] = mapped_column(Integer)
    payload: Mapped[dict] = mapped_column(JSON, default=dict)

class FinancialCalculation(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "financial_calculations"
    lot_id = mapped_column(ForeignKey("lots.id"), nullable=True)
    inputs: Mapped[dict] = mapped_column(JSON, default=dict)
    result: Mapped[dict] = mapped_column(JSON, default=dict)
    version: Mapped[int] = mapped_column(Integer, default=1)

class HistoryEntryModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "history_entries"
    kind: Mapped[str] = mapped_column(String(60), index=True)
    actor_id: Mapped[str | None] = mapped_column(String(80))
    resource_type: Mapped[str] = mapped_column(String(80), index=True)
    resource_id: Mapped[str] = mapped_column(String(80), index=True)
    payload: Mapped[dict] = mapped_column(JSON, default=dict)
    correlation_id: Mapped[str | None] = mapped_column(String(120), index=True)

class KnowledgeGraphEdgeModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "knowledge_graph_edges"
    source_type: Mapped[str] = mapped_column(String(80), index=True)
    source_id: Mapped[str] = mapped_column(String(80), index=True)
    relation: Mapped[str] = mapped_column(String(120), index=True)
    target_type: Mapped[str] = mapped_column(String(80), index=True)
    target_id: Mapped[str] = mapped_column(String(80), index=True)
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)

class DecisionRecord(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "decision_records"
    lot_id = mapped_column(ForeignKey("lots.id"), nullable=True)
    final_decision_score: Mapped[float] = mapped_column(Numeric(5, 2))
    recommendation: Mapped[str] = mapped_column(String(40))
    rationale: Mapped[list] = mapped_column(JSON, default=list)
    confidence: Mapped[float] = mapped_column(Numeric(5, 4), default=0)

class Score360Model(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "score_360"
    lot_id = mapped_column(ForeignKey("lots.id"), nullable=True)
    opportunity_score: Mapped[float] = mapped_column(Numeric(5, 2))
    risk_score: Mapped[float] = mapped_column(Numeric(5, 2))
    repair_score: Mapped[float] = mapped_column(Numeric(5, 2))
    market_score: Mapped[float] = mapped_column(Numeric(5, 2))
    liquidity_score: Mapped[float] = mapped_column(Numeric(5, 2))
    roi_score: Mapped[float] = mapped_column(Numeric(5, 2))
    confidence_score: Mapped[float] = mapped_column(Numeric(5, 2))
    final_auction_score: Mapped[float] = mapped_column(Numeric(5, 2))
    version: Mapped[int] = mapped_column(Integer, default=1)

class TimelineEventModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "timeline_events"
    lot_id = mapped_column(ForeignKey("lots.id"), nullable=True)
    event_type: Mapped[str] = mapped_column(String(80), index=True)
    payload: Mapped[dict] = mapped_column(JSON, default=dict)
    correlation_id: Mapped[str | None] = mapped_column(String(120), index=True)

class SavedSearchModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "saved_searches"
    user_id = mapped_column(ForeignKey("users.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(160))
    filters: Mapped[dict] = mapped_column(JSON, default=dict)

class WatchlistModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "watchlists"
    user_id = mapped_column(ForeignKey("users.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(160))
    alert_kinds: Mapped[list] = mapped_column(JSON, default=list)

class WarehouseDatasetModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "warehouse_datasets"
    name: Mapped[str] = mapped_column(String(160), unique=True)
    layer: Mapped[str] = mapped_column(String(80), index=True)
    source: Mapped[str] = mapped_column(String(160))
    refresh_policy: Mapped[str] = mapped_column(String(80), default="daily")
    schema_version: Mapped[int] = mapped_column(Integer, default=1)

class EmbeddingRecordModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "embedding_records"
    resource_type: Mapped[str] = mapped_column(String(80), index=True)
    resource_id: Mapped[str] = mapped_column(String(80), index=True)
    vector_provider: Mapped[str] = mapped_column(String(80), default="mock")
    embedding_model: Mapped[str] = mapped_column(String(120), default="mock-embedding")
    dimensions: Mapped[int] = mapped_column(Integer, default=0)
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)

class AIMemoryEntryModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "ai_memory_entries"
    prompt: Mapped[str] = mapped_column(Text)
    response: Mapped[str] = mapped_column(Text)
    user_feedback: Mapped[str | None] = mapped_column(Text)
    correction: Mapped[str | None] = mapped_column(Text)
    learning: Mapped[dict] = mapped_column(JSON, default=dict)
    history_entry_id = mapped_column(ForeignKey("history_entries.id"), nullable=True)

class PluginManifestModel(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "plugin_manifests"
    key: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    kind: Mapped[str] = mapped_column(String(80), index=True)
    version: Mapped[str] = mapped_column(String(40))
    enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    configuration_schema: Mapped[dict] = mapped_column(JSON, default=dict)
    healthcheck_path: Mapped[str | None] = mapped_column(String(255))
