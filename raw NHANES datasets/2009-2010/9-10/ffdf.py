import pandas as pd

# Load datasets (2009-2010 NHANES: "_F.xpt" suffix)
demo = pd.read_sas("DEMO_F.xpt", format="xport")[['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1']]  # Use RIDRETH1 instead of RIDRETH3
glu = pd.read_sas("GLU_F.xpt", format="xport")[['SEQN', 'LBXGLU']]
ghb = pd.read_sas("GHB_F.xpt", format="xport")[['SEQN', 'LBXGH']]
diq = pd.read_sas("DIQ_F.xpt", format="xport")[['SEQN', 'DIQ010']]  # Verify DIQ010 exists in DIO_F.xpt
trigly = pd.read_sas("TRIGLY_F.xpt", format="xport")[['SEQN', 'LBXTR']]
hdl = pd.read_sas("HDL_F.xpt", format="xport")[['SEQN', 'LBDHDD']]
bmx = pd.read_sas("BMX_F.xpt", format="xport")[['SEQN', 'BMXBMI', 'BMXWAIST']]
bpx = pd.read_sas("BPX_F.xpt", format="xport")[['SEQN', 'BPXSY1', 'BPXDI1']]  # Confirm BPXSY1/BPXDI1 exist
mcq = pd.read_sas("MCQ_F.xpt", format="xport")[['SEQN', 'MCQ300C']]  # Verify MCQ300C exists in MOQ_F.xpt
paq = pd.read_sas("PAQ_F.xpt", format="xport")[['SEQN', 'PAQ650', 'PAQ665']]
diet = pd.read_sas("DR1TOT_F.xpt", format="xport")[['SEQN', 'DR1TKCAL', 'DR1TSUGR']]  # Check DR1TKCAL/DR1TSUGR
alb_cr = pd.read_sas("ALB_CR_F.xpt", format="xport")[['SEQN', 'URDACT']]

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
                 .merge(alb_cr, on='SEQN', how='left')

# Save dataset
merged_data.to_csv("diabetes_dataset_2009_2010.csv", index=False)