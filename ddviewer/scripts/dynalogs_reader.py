from pylinac import Dynalog
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def read_dynalog(dynalog_file):
    dynalog_data = Dynalog(dynalog_file)
    fluences = {}
    fluences['actual'] = dynalog_data.fluence.actual.calc_map().tolist()
    fluences['expected'] = dynalog_data.fluence.expected.calc_map(resolution=1).tolist()
    #not sure how to calculate error
    test = 33
    plt.plot(fluences['actual'][test])
    plt.plot(fluences['expected'][test])

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    chart_image = base64.b64encode(buffer.read()).decode('utf-8')

    fluences['chart_image'] = chart_image

    plt.close()

    return fluences