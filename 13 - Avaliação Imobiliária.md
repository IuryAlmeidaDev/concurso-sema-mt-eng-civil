---
tags:
  - avaliacao
  - imoveis
  - nbr14653
  - especifico-eng
---
# 🏠 Avaliação Imobiliária

> [!WARNING]
> Tópicos modernos como AVM (Automated Valuation Models) e Machine Learning são novidades em editais recentes e requerem atenção especial para questões conceituais!

## 1. NBR 14.653 (Avaliação de Bens)
Norma fundamental para avaliações:
- **Parte 1 (Procedimentos Gerais)**: Define o valor de mercado, valor em risco, custo de reprodução e reposição.
- **Parte 2 (Imóveis Urbanos)**: Especifica os métodos de avaliação para áreas urbanas e os graus de fundamentação/precisão.
- **Parte 3 (Imóveis Rurais)**: Adapta os conceitos à produtividade e uso da terra.
- **Parte 4 (Empreendimentos)**: Avaliação de base de fluxo de caixa e potencial comercial.

## 2. Métodos de Avaliação
- **Comparativo Direto de Dados de Mercado**: O mais utilizado e recomendado. Consiste em comparar o imóvel a propriedades semelhantes negociadas no mercado. Utiliza regressão linear e homogeneização.
- **Método Involutivo**: Baseado no estudo de viabilidade técnico-econômica de um projeto hipotético para o terreno, subtraindo os custos e lucro do valor de venda. Utilizado para glebas e terrenos grandes.
- **Método Evolutivo**: Soma o valor do terreno (comparativo) ao valor das benfeitorias (custo de reedição, descontando depreciação). Comum para imóveis atípicos (escolas, hospitais, fábricas).
- **Capitalização da Renda**: Calcula o valor presente de um fluxo futuro de receitas líquidas esperado para a propriedade.

## 3. O Produto Imobiliário
- Estudo focado em entender as demandas do mercado, localização, público-alvo, tipologias e padrão construtivo ideal.

## 4. Plano de Negócios e Comercialização
- Projeta o ritmo de vendas (velocidade de vendas - VGV), custos de marketing, comissionamentos e estratégias de lançamento.

## 5. EVTEA (Estudo de Viabilidade Técnico-Econômica e Ambiental)
- Avalia se um projeto deve ou não ser realizado baseando-se em métricas financeiras (VPL, TIR, Payback), restrições ambientais, viabilidade física e legal.

## 6. Incorporação Imobiliária (Lei 4.591/64)
- **Conceito**: Atividade de promover a construção de edificações compostas de unidades autônomas, alienando-as antes de concluídas.
- Envolve o Patrimônio de Afetação e o papel do incorporador.

## 7. Parcelamento do Solo Urbano (Lei 6.766/79)
- **Loteamento**: Subdivisão de gleba com a **abertura** ou ampliação/prolongamento de vias públicas de circulação.
- **Desmembramento**: Subdivisão de gleba com aproveitamento do sistema viário **existente** (não abre novas ruas).
- Requisitos básicos de áreas públicas institucionais e áreas verdes.

## 8. Aprovações e Licenças
- Etapas legais: Alvará de construção, licenciamento ambiental (LP, LI, LO), anuência prévia, Habite-se.

## 9. Coleta de Dados
- Formas de conseguir dados para amostragem: plataformas imobiliárias, corretores, registros de cartórios, pesquisas in loco. O cuidado na eliminação de _outliers_ e dados tendenciosos é essencial.

## 10. AVM e Machine Learning na Avaliação
- **AVM (Automated Valuation Model)**: Sistemas de software que fornecem estimativas de valor usando modelagem matemática e bases de dados, sem intervenção direta do avaliador para cada laudo.
- **Modelos Avançados**:
  - **Random Forest**: Algoritmo de florestas aleatórias (conjunto de árvores de decisão). Robusto para precificação pois lida bem com relações não lineares de características do imóvel.
  - **Gradient Boosting**: Técnica iterativa de aprendizado de máquina que reduz erros de árvores anteriores, criando um modelo final preditivo muito preciso para o valor de mercado.

---
## Checklist de Estudos
- [ ] Conhecer os graus de fundamentação e precisão da NBR 14.653
- [ ] Diferenciar os 4 principais métodos (Comparativo, Involutivo, Evolutivo e Renda)
- [ ] Entender a diferença entre Loteamento e Desmembramento (Lei 6.766)
- [ ] Ler conceitos básicos sobre AVM, VPL e TIR
