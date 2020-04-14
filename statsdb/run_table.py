import qc_analysis

def dictionary(mydict):
    for key in mydict.keys():
        print(key, mydict[key])


header_scopes={}
values={}

def add_header_scope(self, classtype, scope):
    self.header_scopes[classtype] = scope

def parse_file(filename):
    ret = []
    """
    expected_fields:
    TYPE_OF_EXPERIMENT
    PATH_TO_FASTQC
    INSTRUMENT
    CHMESTRY_VERSION
    SOFTWARE_ON_INSTRUMENT_VERSION
    CASAVA_VERION
    RUN_FOLDER
    SAMPLE_NAME
    LANE
    """
    print("Parsed file : ", filename)
    try:
        fh = open( filename, "r" )
    except IOError as err:
        print("Cannot open file ", filename)
    to_parse = fh.readline()
    # print("to parse :", to_parse)
    to_parse = to_parse.strip().lower()
    # print("to parse :", to_parse)
    header = to_parse.split("\t")
    # print("header: ", header)
    values= {}

    for to_parse in fh:
        to_parse = to_parse.strip()
        if to_parse == "":
            continue
        line=to_parse.replace(" ", "").split("\t")
        # print("After spliting:", line)
        # creating object for each record
        analysis = qc_analysis.QcAnalysis()

        for i in range(len(header)):
            key = header[i]
            value = line[i]
            # print(key, value)
            values[key] = value
            analysis.add_property(key, value)

        for key, value in values.items():
            analysis.add_valid_type(key, value)
        ret.append(analysis)

    return ret

def get_property_from_QCanalysis(self, value):
    return self.analysis.get_property(value)
