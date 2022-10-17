import TestCallTime as tct
import Plot_Report as pr
import concat_df_to_csv as cdf
import os

from sites_to_call import sites







for site in sites:
   df_out = tct.main(**site)
   pr.main(df_out)

cdf.main()
