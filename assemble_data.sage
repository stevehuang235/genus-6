import re
from collections import defaultdict

load("Shared/weil_poly_utils.sage")

curves = []
file_keys = ["hyperelliptic", "plane_quintic", "bielliptic", "trigonal_maroni_0", "trigonal_maroni_2", "generic"]
rx = re.compile(r"\[\[(.*)\],'\<(.*), (.*)\>',(.*)\]\n$")
for stratum in file_keys:
    with open("Census/{}/data_{}.txt".format(stratum, stratum)) as f:
        for str in f:
            m = rx.match(str)
            counts, isom_order, isom_type, eqn = m.group(1,2,3,4)
            counts = tuple(eval(counts))
            isom_order = int(isom_order)
            isom_type = int(isom_type)
            curves.append((counts, isom_order, isom_type, stratum, eqn))
