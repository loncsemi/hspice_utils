from utils.data_loader import HspiceDataLoader

loader = HspiceDataLoader()

#  --- printtr Examples ---
printtr_df = loader.load_printtr('data/transient/err_0_vdd_500mV/out/err_0_vdd_500mV.printtr0', prnt=False)

printtr_dict = loader.load_multiple_printtr('data/tran', prnt=False)

# --- mt0 Examples ---
mt0_df = loader.load_mt('data/monte/err_0_vdd_500mV/out/err_0_vdd_500mV.mt0.csv', prnt=False)

mt0_dict = loader.load_multiple_mt('data/monte', prnt=False)