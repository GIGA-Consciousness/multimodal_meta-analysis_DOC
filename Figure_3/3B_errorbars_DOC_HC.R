# #setting font to Gill Sans MT, if not available
# install.packages("showtext")
library(showtext)
# 
font_add(family = "GillSansMT", regular = "C:/Users/asala/Downloads/gill-sans-mt-2/GIL_____.TTF")
showtext_auto() # Enable showtext


##################

#basics
setwd("C:/Users/asala/Dropbox/Meta-analysis/paper/figures/Figure_3") #edit path

#import library
library(ggplot2)
theme_set(
  theme_classic() +
    theme(legend.position = "top")
)

#load df, removing extra rows full of NAN
library(readxl)
df <- read_excel("Figure_3_input.xlsx", 
                 sheet = "DOC_HC_results", n_max = 39)
                 

# Initialize ggplot with data
ggplot(df, aes(y = Position, x = Effect, xmin = Effect-Error, xmax = Effect+Error)) +
  geom_pointrange(aes(),color = df$Subgroup_color, size = 1.5, fatten=3, linewidth=1.5)+
  geom_point(aes(),y=df$Position, x=df$Significant, color = 'red', size = 2.5) +
  theme(plot.margin = margin(t = 0, r = 5, b = 0, l = 5),
        text = element_text(family = "GillSansMT",size=20,color = "#4D4D4D"), 
        axis.title.y=element_blank(),
        panel.grid.major.x = element_line(color = 1,
                                          size = 0.25,
                                          linetype = 2)) + 
  scale_y_continuous(breaks=df$Position,labels=df$Measure2, position="left",expand = expansion(mult = c(0.02, 0.05)))+
  scale_x_continuous(limits = c(-3.1, 3.1))+
  labs(x='Pooled SMD')



#save the plot
ggsave('DOC_HC_results.tiff', width = 7, height = 12, device='tiff', dpi=700)

library(showtext)

showtext_auto(TRUE)

# save the text as svg and match showtext's rendering resolution to TIFF
showtext_opts(dpi = 700)

ggsave(
  "DOC_HC_results.svg",
  width = 7,
  height = 12,
  units = "in",
  device = "svg"
)
