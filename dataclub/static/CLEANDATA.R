library(dplyr)

setwd("C:\\Users\\tadeu\\Desktop\\FGV\\GV DATA\\data_project\\dataclub\\static") 


df <- read.csv("testdata.csv", stringsAsFactors = F)
df[] <- lapply(df, gsub, pattern = "%", replacement = "") %>% lapply(as.numeric)
df[,1:7] <- df[,1:7]/100

write.csv(df, "testdata.csv", sep = ",", row.names = F)
