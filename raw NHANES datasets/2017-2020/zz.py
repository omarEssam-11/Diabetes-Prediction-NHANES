import pandas as pd

# Load datasets (no OGTT)
demo = pd.read_sas("P_DEMO.xpt", format="xport")[['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH3']]
glu = pd.read_sas("P_GLU.xpt", format="xport")[['SEQN', 'LBXGLU']]
ghb = pd.read_sas("P_GHB.xpt", format="xport")[['SEQN', 'LBXGH']]
diq = pd.read_sas("P_DIQ.xpt", format="xport")[['SEQN', 'DIQ010', 'DIQ050', 'DIQ070']]
trigly = pd.read_sas("P_TRIGLY.xpt", format="xport")[['SEQN', 'LBXTR']]
hdl = pd.read_sas("P_HDL.xpt", format="xport")[['SEQN', 'LBDHDD']]
bmx = pd.read_sas("P_BMX.xpt", format="xport")[['SEQN', 'BMXBMI', 'BMXWAIST']]
# bpxo = pd.read_sas("P_BPXO.xpt", format="xport")[['SEQN', 'BPXSAR', 'BPXDAR']]
# bpxo = pd.read_sas("P_BPXO.xpt", format="xport")[['SEQN', 'BPXSY1', 'BPXDI1']]
bpxo = pd.read_sas("P_BPXO.xpt", format="xport")[['SEQN', 'BPXOSY1', 'BPXODI1']]
# mcq = pd.read_sas("P_MCQ.xpt", format="xport")[['SEQN', 'MCQ250', 'MCQ160B']]
mcq = pd.read_sas("P_MCQ.xpt", format="xport")[['SEQN', 'MCQ300C']]  # Family history of diabetes
alq = pd.read_sas("P_ALQ.xpt", format="xport")[['SEQN', 'ALQ130']]
paq = pd.read_sas("P_PAQ.xpt", format="xport")[['SEQN', 'PAQ650', 'PAQ665']]
smq = pd.read_sas("P_SMQ.xpt", format="xport")[['SEQN', 'SMQ040']]
diet = pd.read_sas("P_DR1TOT.xpt", format="xport")[['SEQN', 'DR1TKCAL', 'DR1TSUGR']]
alb_cr = pd.read_sas("P_ALB_CR.xpt", format="xport")[['SEQN', 'URDACT']]

# Merge datasets (excluding OGTT)
merged_data = demo.merge(glu, on='SEQN', how='left') \
                 .merge(ghb, on='SEQN', how='left') \
                 .merge(diq, on='SEQN', how='left') \
                 .merge(trigly, on='SEQN', how='left') \
                 .merge(hdl, on='SEQN', how='left') \
                 .merge(bmx, on='SEQN', how='left') \
                 .merge(bpxo, on='SEQN', how='left') \
                 .merge(mcq, on='SEQN', how='left') \
                 .merge(alq, on='SEQN', how='left') \
                 .merge(paq, on='SEQN', how='left') \
                 .merge(smq, on='SEQN', how='left') \
                 .merge(diet, on='SEQN', how='left') \
                 .merge(alb_cr, on='SEQN', how='left')

# Save dataset
merged_data.to_csv("diabetes_dataset.csv", index=False)
#

df = pd.read_csv("diabetes_dataset.csv")
df.head()