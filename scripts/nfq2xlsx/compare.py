from pynfq import pyNFQ as nfq

nfq_obj = nfq(path_to_ticker_symbol_csv="TickerOnly.csv")

nfq_obj.comp_rslt_Tkcr(dir="csv")
