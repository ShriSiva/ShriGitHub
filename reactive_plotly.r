library(shiny)
library(DT)
library(plotly)
library(crosstalk)
setwd("C:/Users/sarah/Documents")
deck <- read.csv("ECGenie_client.csv")

m <- deck %>% 
    tibble::rownames_to_column()

ui <- fluidPage(
    h1("ECGenie Metrics", align = "center"),
    plotlyOutput("x2"),
    DT::dataTableOutput("x1"),
    fluidRow(
        p(class = 'text-center', downloadButton('x3', 'Download Filtered Data'))
    )
)

server <- function(input, output) {
    
    d <- SharedData$new(m, ~rowname)
    
    # highlight selected rows in the scatterplot
    output$x2 <- renderPlotly({
        
        s <- input$x1_rows_selected
        
        if (!length(s)) {
            p <- d %>%
                plot_ly(x = ~HRV, y = ~HR, mode = "markers", color = ~Strain) %>%
                layout(showlegend = T) %>%
                highlight("plotly_selected", color= I('red'))
                
        } else if (length(s)) {
            pp <- m %>%
                plot_ly() %>% 
                add_trace(x = ~HRV, y = ~HR, mode = "markers", color = ~Strain) %>%
                layout(showlegend = T)
            
            # selected data
            pp <- add_trace(pp, data = m[s, , drop = F], x = ~HRV, y = ~HR, mode = "markers",
                           color = I('red'))
        }
        
    })
    
    # highlight selected rows in the table
    output$x1 <- DT::renderDataTable({
        m2 <- m[d$selection(),]
        dt <- DT::datatable(m)
        if (NROW(m2) == 0) {
            dt
        } else {
            DT::formatStyle(dt, "rowname", target = "row",
                            color = DT::styleEqual(m2$rowname, rep("white", length(m2$rowname))),
                            backgroundColor = DT::styleEqual(m2$rowname, rep("black", length(m2$rowname))))
        }
    })
    
    # download the filtered data
    output$x3 = downloadHandler('ecgeniedata.csv', content = function(file) {
        s <- input$x1_rows_selected
        if (length(s)) {
            write.csv(m[s, , drop = FALSE], file)
        } else if (!length(s)) {
            write.csv(m[d$selection(),], file)
        }
    })
    
}

shinyApp(ui, server)