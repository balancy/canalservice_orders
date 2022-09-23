import pandas

sheet_id = '1AkbjncKtr9_xW3mFcpxX9E1FDoFyn0sAbomPFIUxmDo'
SAMPLE_RANGE_NAME = 'A2:D'


url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&range={SAMPLE_RANGE_NAME}'

data = pandas.read_csv(url)
for elm in data.rows:
    print(elm)
