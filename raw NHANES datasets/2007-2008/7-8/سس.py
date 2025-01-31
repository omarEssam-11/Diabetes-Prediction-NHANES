import pandas as pd

# Load datasets (2007-2008 NHANES: "_E.xpt" suffix)
demo = pd.read_sas("DEMO_E.xpt", format="xport")[['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1']]
glu = pd.read_sas("GLU_E.xpt", format="xport")[['SEQN', 'LBXGLU']]
ghb = pd.read_sas("GHB_E.xpt", format="xport")[['SEQN', 'LBXGH']]
diq = pd.read_sas("DIQ_E.xpt", format="xport")[['SEQN', 'DIQ010']]
trigly = pd.read_sas("TRIGLY_E.xpt", format="xport")[['SEQN', 'LBXTR']]
hdl = pd.read_sas("HDL_E.xpt", format="xport")[['SEQN', 'LBDHDD']]
bmx = pd.read_sas("BMX_E.xpt", format="xport")[['SEQN', 'BMXBMI', 'BMXWAIST']]
bpx = pd.read_sas("BPX_E.xpt", format="xport")[['SEQN', 'BPXSY1', 'BPXDI1']]
mcq = pd.read_sas("MCQ_E.xpt", format="xport")[['SEQN', 'MCQ300C']]
paq = pd.read_sas("PAQ_E.xpt", format="xport")[['SEQN', 'PAQ650', 'PAQ665']]
diet = pd.read_sas("DR1TOT_E.xpt", format="xport")[['SEQN', 'DR1TKCAL', 'DR1TSUGR']]

# Load albumin and creatinine data and calculate the ratio
alb_cr = pd.read_sas("ALB_CR_E.xpt", format="xport")[['SEQN', 'URXUMA', 'URXUCR']]  # Use URXUMA and URXUCR
alb_cr['URDACT'] = alb_cr['URXUMA'] / alb_cr['URXUCR']  # Calculate ratio

# Merge datasets
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
                 .merge(alb_cr[['SEQN', 'URDACT']], on='SEQN', how='left')  # Include the calculated ratio

# Save dataset
merged_data.to_csv("diabetes_dataset_2007_2008.csv", index=False)