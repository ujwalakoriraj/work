from pyhelm.chartbuilder import ChartBuilder
from pyhelm.tiller import Tiller
chart = ChartBuilder({"name": "webapp", "source": {"type": "directory", "location": "D:/python/microservices_in_python"}})

from pyhelm.chartbuilder import ChartBuilder
from pyhelm.tiller import Tiller

tiller = Tiller('chart-example.local')
chart = ChartBuilder({"name": "webapp", "source": {"type": "directory", "location": "D:/python/microservices_in_python/webapp"}})
tiller.install_release(chart.get_helm_chart(), dry_run=False, namespace='default')

