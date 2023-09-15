
import sys
from systemrdl import RDLCompiler, RDLCompileError
from peakrdl_ipxact import IPXACTExporter
from peakrdl_ipxact import IPXACTImporter

from exporter import SystemRDLExporter

input_files = sys.argv[1:]

rdlc = RDLCompiler()
ipxact = IPXACTImporter(rdlc)

try:
  for input_file in input_files:
    if input_file.endswith(".rdl"):
      rdlc.compile_file(input_file)
    if input_file.endswith(".xml"):
      ipxact.import_file(input_file)

  root = rdlc.elaborate()

  x = SystemRDLExporter()
  x.export(root, "./test.rdl")

except RDLCompileError:
  sys.exit(1)