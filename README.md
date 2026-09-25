# Methylation-Data
Python toolkit for processing DNA methylation array data (IDATs or beta values) to compute epigenetic age estimates, age acceleration, cell-type proportions, and covariate-adjusted residuals from methylation sample sheets.

## Layout
- `QC/` – QC reports, filtered CpG/sample lists, imputation summary, phenotype data (pData).
- `Normalized/` – ssnoob-normalized beta values (`ssnoob_betas_EPICv2custom_DML`, 915,748 CpGs × 21 samples), rounded to 4 decimals and split into gzipped parts to fit GitHub's file size limits. Rebuild the full matrix with:
  ```python
  from Normalized.load_betas import load_betas
  betas = load_betas()
  ```
