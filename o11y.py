from opentelemetry.sdk.trace import Tracer

class O11yExporter(SpanExporter):
    def __init__(self, name: str = ""):
        super()