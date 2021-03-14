installNeedPacks <- function() {
  packages <- c("PMCMR", "scmamp")
  if (!require("BiocManager")) {
    install.packages("BiocManager")
  }
  for (pack in packages) {
    if (!require(pack, character.only = TRUE)) {
      BiocManager::install(pack)
    }
    library(pack, character.only = TRUE, verbose = F)
  }
}

installNeedPacks()

library(scmamp)

dados <- as.matrix(read.csv("packets-error.csv"))

colnames(dados) <- c("4x4", "8x8", "16x16")

png("./packets-error.png", width=642, height=482)
plotCD(dados, cex=1.25, decreasing = F)
title(main='Nemenyi Test - Packets')
dev.off()