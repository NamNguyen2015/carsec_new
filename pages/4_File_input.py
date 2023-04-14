#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:15:55 2022
@author: namnguyen
"""
import numpy as np
import streamlit as st
import json
import pandas as pd
import os
from collections import defaultdict
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import CARSEC as CS
from zipfile import ZipFile
import tempfile

#%%%%%%%%%%%%%%%%%%
st.subheader('Download Excel Template input')
st.markdown("Please download this file as a template excel and free to modify your own parameters.")
with open("Input_files/CARSEC_excel_multi_index.xlsx", "rb") as fp:
	btn = st.download_button(label="Download Excel Template",data=fp,file_name="CARSEC_Excel_Input.xlsx",mime="application/xlsx")
#%%%%%%%%%%%%%%%%%%%	
st.subheader('Upload your own Excel file')
st.markdown("Once the excel file is prepared, please drop your file here and click the download button to get multiple file.txt")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	st.write('Data preview')
	_tables=pd.read_excel(uploaded_file,sheet_name=None)
	for k in _tables: 
		st.write(k)
		st.write(_tables[k])
#%%%%%%%%%%%%%%%%%%%
st.subheader('Download Muti CARSEC files')

#=============================================================================
#path='/app/carsecn_applications/Output_files/Multi_CARSEC'

path1=os.getcwd()

path2=os.path.join(path1,'Output_files')

path3=os.path.join(path2,'Multi_CARSEC')


path=path3
if os.path.exists(path):
	dirs = os.listdir(path)
	for file in dirs:
		path_file=os.path.join(path,file)
		os.remove(path_file)
		

if uploaded_file is not None:
	#CS.excel_to_CARSEC(load_path=uploaded_file,export_path='/app/carsecn_applications/Output_files/Multi_CARSEC/CS_Multi_')

	CS.excel_to_CARSEC(load_path=uploaded_file,export_path=os.path.join(path,'CS_Multi_'))

	CS.excel_to_CARSEC(load_path=uploaded_file,export_path=os.path.join(path,''))
	#CS.excel_to_CARSEC(load_path=uploaded_file,export_path=path)
	#CS.excel_to_CARSEC(load_path=uploaded_file,export_path=os.path.join(path,''))



dirs = os.listdir(path)
with ZipFile('CARSEC_multi.zip', 'w') as zipObj:
	# Add multiple files to the zip
	for file in dirs:
		path_file=os.path.join(path,file)
		zipObj.write(os.path.join(path_file))
	
with open('CARSEC_multi.zip', "rb") as fp:
	btn = st.download_button(label='Download CARSEC files',data=fp,file_name="CARSEC_multi.zip",mime="application/ZIP")
# =============================================================================
	
	
	
