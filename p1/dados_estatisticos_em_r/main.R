library(jsonlite)
library(dplyr)

# Verificar se o arquivo JSON existe
file_path <- "/Users/italodom/DESENVOLVIMENTO/ITALO/FIAP/p1/dados_estatisticos_em_r/database.json"
if (!file.exists(file_path)) {
  stop(paste("Arquivo JSON não encontrado no caminho:", file_path))
}

# Tente carregar o arquivo JSON
dados <- tryCatch({
  fromJSON(file_path, simplifyVector = FALSE)  # Carregar como lista
}, error = function(e) {
  stop(paste("Erro ao carregar o arquivo JSON. Verifique o formato:", e$message))
})

# Inicializar um data.frame vazio
df <- data.frame()

# Loop para transformar o JSON em um data.frame
for (item in dados) {

  # Extrair dados de cultura, área e insumos
  tryCatch({
    cultura <- item$cultura
    area <- item$area
    insumos <- item$insumos

    # Construir o data.frame acumulativo
    df <- bind_rows(df,
                    data.frame(
                      Cultura = cultura,
                      Area = area,
                      Insumo = names(insumos),
                      Quantidade = as.numeric(insumos)
                    ))
  }, error = function(e) {
    cat("Erro ao processar item. Detalhes:", e$message, "\n")
  })
}

# Diagnóstico do data.frame montado
cat("\nEstrutura do data.frame gerado:\n")
str(df)

# Verificar se o data.frame não está vazio
if (nrow(df) == 0) {
  stop("Nenhum dado válido foi extraído do arquivo JSON.")
}

# Calcular a Média e o Desvio-Padrão por Cultura
data_stats <- df %>%
  group_by(Cultura) %>%
  summarise(
    Media = round(mean(Area, na.rm = TRUE), 2),
    DesvioPadrao = round(sd(Area, na.rm = TRUE), 2),
    .groups = "drop"
  )

# Exibir as Estatísticas
cat("\nMédia e Desvio-Padrão por Cultura:\n")
print(data_stats)

# Salvar as Estatísticas em um Arquivo CSV
output_file <- "/Users/italodom/DESENVOLVIMENTO/ITALO/FIAP/p1/dados_estatisticos_em_r/estatisticas_insumos_por_cultura.csv"
write.csv(data_stats, output_file, row.names = FALSE)
cat(paste("\nEstatísticas salvas em:", output_file, "\n"))

