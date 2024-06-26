from robusta.core.sinks.sink_base_params import SinkBaseParams
from robusta.core.sinks.sink_config import SinkConfigBase


class VictoropsSinkParams(SinkBaseParams):
    url: str

    @classmethod
    def _get_sink_type(cls):
        return "victorops"


class VictoropsConfigWrapper(SinkConfigBase):
    victorops_sink: VictoropsSinkParams

    def get_params(self) -> SinkBaseParams:
        return self.victorops_sink
