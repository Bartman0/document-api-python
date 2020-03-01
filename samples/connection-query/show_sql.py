from tableaudocumentapi import Datasource

sourceTDS = Datasource.from_file('Sales.tds')
print(sourceTDS.has_extract())

print(sourceTDS.get_query())

sourceTDS = Datasource.from_file('Cash Register.tds')

print(sourceTDS.get_query())
