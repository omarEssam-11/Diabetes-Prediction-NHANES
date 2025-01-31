import pandas as pd

# Load datasets (no OGTT)
demo = pd.read_sas("DEMO_I.xpt", format="xport")[['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH3']]
glu = pd.read_sas("GLU_I.xpt", format="xport")[['SEQN', 'LBXGLU']]
ghb = pd.read_sas("GHB_I.xpt", format="xport")[['SEQN', 'LBXGH']]
diq = pd.read_sas("DIQ_I.xpt", format="xport")[['SEQN', 'DIQ010']]
trigly = pd.read_sas("TRIGLY_I.xpt", format="xport")[['SEQN', 'LBXTR']]
hdl = pd.read_sas("HDL_I.xpt", format="xport")[['SEQN', 'LBDHDD']]
bmx = pd.read_sas("BMX_I.xpt", format="xport")[['SEQN', 'BMXBMI', 'BMXWAIST']]
bpx = pd.read_sas("BPX_I.xpt", format="xport")[['SEQN', 'BPXSY1', 'BPXDI1']]  # Corrected BP variables
mcq = pd.read_sas("MCQ_I.xpt", format="xport")[['SEQN', 'MCQ300C']]  # Family history of diabetes (file renamed)
paq = pd.read_sas("PAQ_I.xpt", format="xport")[['SEQN', 'PAQ650', 'PAQ665']]
diet = pd.read_sas("DR1TOT_I.xpt", format="xport")[['SEQN', 'DR1TKCAL', 'DR1TSUGR']]  # Corrected filename
alb_cr = pd.read_sas("ALB_CR_I.xpt", format="xport")[['SEQN', 'URDACT']]

# Merge datasets (excluding OGTT)
merged_data = demo.merge(glu, on='SEQN', how='left') \
                 .merge(ghb, on='SEQN', how='left') \
                 .merge(diq, on='SEQN', how='left') \
                 .merge(trigly, on='SEQN', how='left') \
                 .merge(hdl, on='SEQN', how='left') \
                 .merge(bmx, on='SEQN', how='left') \
                 .merge(bpx, on='SEQN', how='left') \
                 .merge(mcq, on='SEQN', how='left') \
                 .merge(paq, on='SEQN', how='left') \
                 .merge(diet, on='SEQN', how='left') \
                 .merge(alb_cr, on='SEQN', how='left')

# Save dataset
merged_data.to_csv("diabetes_dataset_2015_2016.csv", index=False)