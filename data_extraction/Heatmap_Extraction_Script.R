###############################################################################
# Heatmap Extraction Script
# Written by: Ikrame Bahlou
# Based on the reverse‑engineering method described on R‑Bloggers (2020) 
# https://www.r-bloggers.com/2020/01/how-to-reverse-engineer-a-heat-map-into-its-underlying-values/
# With assistance from Microsoft Copilot
#
# This script extracts numerical values from a heatmap image by:
# 1. Cropping the image to include only the heatmap grid
# 2. Dividing the grid into equal cells (rows × columns)
# 3. Computing the average color of each cell
# 4. Converting color intensity into a numeric scale (−3 to +3)
# 5. Exporting the result as an Excel file
#
# All sections that must be modified for another dataset or heatmap
# are clearly marked with:  >>> MODIFY HERE <<<
###############################################################################

library(magick)     # For image loading and cropping
library(openxlsx)   # For exporting Excel files


###############################################################################
# 1. LOAD THE CROPPED IMAGE  >>> MODIFY HERE <<<
#
# IMPORTANT:
# - The image must contain ONLY the heatmap grid (no margins, no titles).
# - Crop manually using Preview (Mac) or any image editor.
# - Save the cropped file as PNG or JPG.
###############################################################################

img <- image_read("HC_only.png")  
# Example:
# "HC_only.png"  → cropped image containing only the 15 HC columns
# "MCS_only.png" → cropped image containing only the 12 MCS columns
# "UWS_only.png" → cropped image containing only the 11 UWS columns


###############################################################################
# 2. DEFINE GRID SIZE  >>> MODIFY HERE <<<
#
# n_cols must match the number of patients in the cropped image:
# - HC  → 15 columns
# - MCS → 12 columns
# - UWS → 11 columns

n_rows <- 13     # <<< MODIFY HERE depends on regions 
n_cols <- 15     # <<< MODIFY HERE (15 for HC, 12 for MCS, 11 for UWS)


###############################################################################
# 3. DEFINE PATIENT NAMES  >>> MODIFY HERE <<<
#
# Must match the number of columns above.
###############################################################################

patients <- paste0("HC", 1:15)  
# For MCS: patients <- paste0("MCS", 1:12)
# For UWS: patients <- paste0("UWS", 1:11)


###############################################################################
# 4. DEFINE REGION NAMES (13 rows)
# These are fixed for your dataset.
###############################################################################

regions <- c(
  "L_FPC","R_FPC","L_MFC","R_MFC","L_IFC","R_IFC",
  "L_SMC","R_SMC","L_PPC","R_PPC","L_TPC","R_TPC","V1"
)


###############################################################################
# 5. GET IMAGE DIMENSIONS
###############################################################################

info <- image_info(img)
W <- info$width
H <- info$height

# Compute the size of each cell in the grid
cell_w <- W / n_cols
cell_h <- H / n_rows


###############################################################################
# 6. EXTRACT RAW COLOR VALUES FROM EACH CELL
#
# For each cell:
# - Crop the corresponding rectangle
# - Compute mean R, G, B values
# - Use (R - B) as a simple intensity measure
###############################################################################

values_raw <- matrix(NA, nrow = n_rows, ncol = n_cols)

for (r in 1:n_rows) {
  for (c in 1:n_cols) {
    
    # Compute pixel coordinates of the cell
    x1 <- floor((c - 1) * cell_w)
    y1 <- floor((r - 1) * cell_h)
    x2 <- floor(c * cell_w)
    y2 <- floor(r * cell_h)
    
    # Crop the cell from the image
    crop <- image_crop(img, sprintf("%dx%d+%d+%d", x2 - x1, y2 - y1, x1, y1))
    
    # Extract RGB channels
    arr <- image_data(crop, channels = "rgb")
    
    R <- mean(as.integer(arr[1,,]))
    G <- mean(as.integer(arr[2,,]))
    B <- mean(as.integer(arr[3,,]))
    
    # Simple intensity measure: red minus blue
    values_raw[r, c] <- R - B
  }
}


###############################################################################
# 7. RESCALE VALUES TO THE RANGE −3 TO +3
###############################################################################

vmin <- min(values_raw)
vmax <- max(values_raw)

values <- -3 + (values_raw - vmin) * (6 / (vmax - vmin))

colnames(values) <- patients
rownames(values) <- regions


###############################################################################
# 8. EXPORT TO EXCEL  >>> MODIFY HERE <<<
#
# Change the filename depending on the group:
# - "HC_values.xlsx"
# - "MCS_values.xlsx"
# - "UWS_values.xlsx"
###############################################################################

write.xlsx(values, "HC_values.xlsx", rowNames = TRUE)
# <<< MODIFY HERE 


###############################################################################
# END OF SCRIPT
###############################################################################
