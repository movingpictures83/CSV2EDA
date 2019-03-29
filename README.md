# CSV2EDA
# Language: Python
# Input: CSV (file to convert)
# Output: EDA (converted file)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to convert a network represented in Comma-Separated Value (CSV) format
to an EDge Attribute (EDA) file that is importable into Cytoscape.

Since the EDA file is a Cytoscape format, the plugin is built around network data
and assumes the CSV file is constructed such that nodes are represented by both rows
and columns and entry (i, j) is the weight of the edge from node i to node j.

The output EDA file contains nodes and edges in the following format:

name    newweight
Acinetobacter.01 (pp) C.Gammaproteobacteria.02  0.888058066368
Acinetobacter.01 (pp) C.Gammaproteobacteria.04  0.871748447418
....

Only non-zero edges are included in the file.  Zero-weight edges are assumed
to not exist.  The value "newweight" is chosen for the column since importing
this file into Cytoscape would require the above nodes to already exist in a network.
