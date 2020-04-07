# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# The folllowing notebook has Snomed/[NHS Dictionary of Medicines and Devices](https://ebmdatalab.net/what-is-the-dmd-the-nhs-dictionary-of-medicines-and-devices/) codes for proton pump inhibitors.

from ebmdatalab import bq
import os
import pandas as pd

# +
sql = '''WITH bnf_codes AS (
 SELECT bnf_code FROM hscic.presentation WHERE 
    bnf_code LIKE '0103050%' #BNF ppi section
  )

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

ppi_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','ppi_codelist.csv'))
pd.set_option('display.max_rows', None)
ppi_codelist
# -

# q - do we exclude IVs? 
# Remove generic heliclear when tidying (hasn't been Rx but just for completeness)
