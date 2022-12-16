安装R语言开发环境
- brew install r
- brew install gettext
- install.packages("BiocManager")
- install.packages('shiny', dependencies = TRUE)
- install.packages("d3heatmap_0.6.1.2.tar.gz",repos=NULL,type="source")
- BiocManager::install("caret")

terminal cd 到项目所在目录运行
- install.packages('languageserver', repos='https://cran.r-project.org/')


if (!require("devtools")) install.packages("devtools")
   devtools::install_github("rstudio/d3heatmap")