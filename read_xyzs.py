import os, sys 
import ase
from ase.io import read, write

import pandas as pd 

def read_struc(inpath):
	tmp_struc = read(inpath, format="aims")
	return tmp_struc

for root_folder in ["train", "test"]:
	#read in csv
	df = pd.read_csv(root_folder+".csv")
	for tmp_id in df['id'].tolist():
		inpath = os.path.join("train", str(tmp_id), "geometry.xyz")
		out_struc = read_struc(inpath)
		print("structure id %s (as an ase atoms object) from %s: " %(tmp_id, root_folder))
		print(out_struc)
sys.exit()
