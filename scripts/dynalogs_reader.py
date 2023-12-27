from pylinac import Dynalog

def read_dynalog(dynalog_file):
    dynalog_data = Dynalog(dynalog_file)
    fluences = {}
    fluences['actual'] = dynalog_data.fluence.actual.calc_map().tolist()
    fluences['expected'] = dynalog_data.fluence.expected.calc_map(resolution=1).tolist()
    #not sure how to calculate error
    return fluences