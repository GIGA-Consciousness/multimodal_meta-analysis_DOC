
#setup

install.packages("remotes")
remotes::install_github("guido-s/meta", ref = "R-book-first-edition")
install.packages("dplyr")

#load libraries

library(readxl)
library(dplyr)
library(meta)

#define folder to save files and visualization options
folder <- "C:/Users/asala/Dropbox/Meta-analysis/implementation/011_final_analysis/EEG/results" #edit path
options(max.print=1000000)
setwd(folder)

#load file with EEG measures (in our case final_EEG_MA_all)
final_EEG_MA_all <- read_excel("final_EEG_MA_all.xlsx") #file containing statistics from all studies


#first run filtering out specific lines (reserved for sensitivity analysis 1 and 6)

final_EEG_MA_all<-final_EEG_MA_all[(final_EEG_MA_all$Sensitivity_Analysis_Measures!=1 & final_EEG_MA_all$Sensitivity_Analysis_Measures!=6 ),]
final_EEG_MA_all<-final_EEG_MA_all[(final_EEG_MA_all$Sensitivity_Analysis_Groupings==0 | final_EEG_MA_all$Sensitivity_Analysis_Groupings==4 ),]

"MCS_control"

#dataset for MCS_control comparison

DB_MCS_Controls<-filter(final_EEG_MA_all, MCS_HC == 1)
DB_MCS_Controls <- DB_MCS_Controls[order(DB_MCS_Controls$Subgroup),]

SMDMCS_Controls = metacont(N_MCS, Mean_MCS, SD_MCS, N_Control, Mean_Control, SD_Control, 
                           data = DB_MCS_Controls, studlab = Authors, comb.fixed = FALSE,
                           comb.random = TRUE, sm = "SMD")
#summary(MCS_Control)
# forest(MCS_Control, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")
RES_MCS_Controls<- update.meta(SMDMCS_Controls,byvar=Subgroup,comb.fixed = FALSE,
                               comb.random = TRUE)
RES_MCS_Controls
# forest(subgroup.EEG3, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

pdf(file = paste(folder,"forestplot_MCS_HC.pdf", sep = "/"), width = 12, height = 400)
forest(RES_MCS_Controls, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

#initialize dataframe
output_MCS_Controls=data.frame()

#add first coloumn with correct number of rows
data.frame(RES_MCS_Controls$bylevs)->output_MCS_Controls[RES_MCS_Controls$bylevs,1]
#add all other coloumns
data.frame(RES_MCS_Controls$TE.random.w)->output_MCS_Controls[,2]
data.frame(RES_MCS_Controls$lower.random.w)->output_MCS_Controls[,3]
data.frame(RES_MCS_Controls$upper.random.w)->output_MCS_Controls[,4]
data.frame(RES_MCS_Controls$I2.w)->output_MCS_Controls[,5]
data.frame(RES_MCS_Controls$tau2.w)->output_MCS_Controls[,6]
data.frame(RES_MCS_Controls$pval.Q.w)->output_MCS_Controls[,7]
data.frame(RES_MCS_Controls$k.w)->output_MCS_Controls[,8]
#write output
write.csv(output_MCS_Controls, "summary_MCS_HC.csv", row.names=FALSE)

dev.off()







"UWS_control"

#dataset for UWS_control comparison

DB_UWS_Controls<-filter(final_EEG_MA_all, UWS_HC == 1)
DB_UWS_Controls <- DB_UWS_Controls[order(DB_UWS_Controls$Subgroup),]

SMDUWS_Controls = metacont(N_UWS, Mean_UWS, SD_UWS, N_Control, Mean_Control, SD_Control, 
                           data = DB_UWS_Controls, studlab = Authors, comb.fixed = FALSE,
                           comb.random = TRUE, sm = "SMD")
#summary(UWS_Control)
# forest(UWS_Control, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")
RES_UWS_Controls<- update.meta(SMDUWS_Controls,byvar=Subgroup,comb.fixed = FALSE,
                               comb.random = TRUE)
RES_UWS_Controls
# forest(subgroup.EEG3, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

pdf(file = paste(folder,"forestplot_UWS_HC.pdf", sep = "/"), width = 12, height = 400)
forest(RES_UWS_Controls, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

#initialize dataframe
output_UWS_Controls=data.frame()

#add first coloumn with correct number of rows
data.frame(RES_UWS_Controls$bylevs)->output_UWS_Controls[RES_UWS_Controls$bylevs,1]
#add all other coloumns
data.frame(RES_UWS_Controls$TE.random.w)->output_UWS_Controls[,2]
data.frame(RES_UWS_Controls$lower.random.w)->output_UWS_Controls[,3]
data.frame(RES_UWS_Controls$upper.random.w)->output_UWS_Controls[,4]
data.frame(RES_UWS_Controls$I2.w)->output_UWS_Controls[,5]
data.frame(RES_UWS_Controls$tau2.w)->output_UWS_Controls[,6]
data.frame(RES_UWS_Controls$pval.Q.w)->output_UWS_Controls[,7]
data.frame(RES_UWS_Controls$k.w)->output_UWS_Controls[,8]
#write output
write.csv(output_UWS_Controls, "summary_UWS_HC.csv", row.names=FALSE)

dev.off()






"DOC_control"

#dataset for DOC_control comparison

DB_DOC_Controls<-filter(final_EEG_MA_all, DOC_HC == 1)
DB_DOC_Controls <- DB_DOC_Controls[order(DB_DOC_Controls$Subgroup),]

SMDDOC_Controls = metacont(N_DOC, Mean_DOC, SD_DOC, N_Control, Mean_Control, SD_Control, 
                           data = DB_DOC_Controls, studlab = Authors, comb.fixed = FALSE,
                           comb.random = TRUE, sm = "SMD")
#summary(DOC_Control)
# forest(DOC_Control, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")
RES_DOC_Controls<- update.meta(SMDDOC_Controls,byvar=Subgroup,comb.fixed = FALSE,
                               comb.random = TRUE)
RES_DOC_Controls
# forest(subgroup.EEG3, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

pdf(file = paste(folder,"forestplot_DOC_HC.pdf", sep = "/"), width = 12, height = 400)
forest(RES_DOC_Controls, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

#initialize dataframe
output_DOC_Controls=data.frame()

#add first coloumn with correct number of rows
data.frame(RES_DOC_Controls$bylevs)->output_DOC_Controls[RES_DOC_Controls$bylevs,1]
#add all other coloumns
data.frame(RES_DOC_Controls$TE.random.w)->output_DOC_Controls[,2]
data.frame(RES_DOC_Controls$lower.random.w)->output_DOC_Controls[,3]
data.frame(RES_DOC_Controls$upper.random.w)->output_DOC_Controls[,4]
data.frame(RES_DOC_Controls$I2.w)->output_DOC_Controls[,5]
data.frame(RES_DOC_Controls$tau2.w)->output_DOC_Controls[,6]
data.frame(RES_DOC_Controls$pval.Q.w)->output_DOC_Controls[,7]
data.frame(RES_DOC_Controls$k.w)->output_DOC_Controls[,8]
#write output
write.csv(output_DOC_Controls, "summary_DOC_HC.csv", row.names=FALSE)

dev.off()





"MCS_UWS"

#dataset for MCS_UWS comparison

DB_MCS_UWS<-filter(final_EEG_MA_all, MCS_UWS == 1)
DB_MCS_UWS <- DB_MCS_UWS[order(DB_MCS_UWS$Subgroup),]

SMDMCS_UWS = metacont(N_MCS, Mean_MCS, SD_MCS, N_UWS, Mean_UWS, SD_UWS, 
                      data = DB_MCS_UWS, studlab = Authors, comb.fixed = FALSE,
                      comb.random = TRUE, sm = "SMD")
#summary(MCS_UWS)
# forest(MCS_UWS, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")
RES_MCS_UWS<- update.meta(SMDMCS_UWS,byvar=Subgroup,comb.fixed = FALSE,
                          comb.random = TRUE)
RES_MCS_UWS
# forest(subgroup.EEG3, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

pdf(file = paste(folder,"forestplot_MCS_UWS.pdf", sep = "/"), width = 12, height = 400)
forest(RES_MCS_UWS, sortvar = Authors, test.overall.random = TRUE, col.diamond = "red")

#initialize dataframe
output_MCS_UWS=data.frame()

#add first coloumn with correct number of rows
data.frame(RES_MCS_UWS$bylevs)->output_MCS_UWS[RES_MCS_UWS$bylevs,1]
#add all other coloumns
data.frame(RES_MCS_UWS$TE.random.w)->output_MCS_UWS[,2]
data.frame(RES_MCS_UWS$lower.random.w)->output_MCS_UWS[,3]
data.frame(RES_MCS_UWS$upper.random.w)->output_MCS_UWS[,4]
data.frame(RES_MCS_UWS$I2.w)->output_MCS_UWS[,5]
data.frame(RES_MCS_UWS$tau2.w)->output_MCS_UWS[,6]
data.frame(RES_MCS_UWS$pval.Q.w)->output_MCS_UWS[,7]
data.frame(RES_MCS_UWS$k.w)->output_MCS_UWS[,8]
#write output
write.csv(output_MCS_UWS, "summary_MCS_UWS.csv", row.names=FALSE)

dev.off()

save.image(file = "variablesR.RData")
rm(list=ls())