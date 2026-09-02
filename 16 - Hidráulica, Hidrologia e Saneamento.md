---
tags:
  - hidraulica
  - hidrologia
  - saneamento
  - especifico-eng
---

# 💧 Hidráulica, Hidrologia e Saneamento

> [!NOTE]
> Área de grande relevância, exigindo domínio tanto teórico (ciclo hidrológico) quanto prático (cálculo de perdas de carga e dimensionamento).

## 1. Hidráulica Geral
- **Estática dos Fluidos:** Lei de Stevin, Princípio de Pascal, empuxo (Arquimedes).
- **Cinemática:** Tipos de escoamento (laminar, turbulento, permanente, uniforme).
- **Equação da Continuidade:** $Q = V_1 \cdot A_1 = V_2 \cdot A_2$.
- **Teorema de Bernoulli:** Conservação de energia (carga de posição, carga de pressão, carga cinética).
- **Perdas de Carga:** 
  - Fórmulas empíricas: **Hazen-Williams** (condutos forçados de água), **Darcy-Weisbach** (universal).
- **Orifícios e Vertedores:** Fórmulas para cálculo de vazão. Tipos de vertedores (retangular, triangular, Cipolletti).
- **Condutos Forçados:** Linha piezométrica e linha de energia.
- **Canais:** Escoamento livre, fórmula de **Manning** ($V = \frac{1}{n} \cdot R_h^{2/3} \cdot I^{1/2}$).

## 2. Hidrologia Aplicada
- **Ciclo Hidrológico:** Precipitação, evapotranspiração, infiltração, escoamento superficial e subterrâneo.
- **Precipitação:** Chuvas de projeto, curvas IDF (Intensidade-Duração-Frequência), tempo de recorrência (TR).
- **Infiltração:** Capacidade de infiltração do solo.
- **Escoamento Superficial:** Fatores intervenientes.
- **Hidrograma Unitário:** Resposta da bacia a uma chuva efetiva unitária.
- **Tempo de Concentração ($t_c$):** Tempo para a água da chuva ir do ponto mais remoto até o exutório.
- **Método Racional:** $Q = \frac{C \cdot i \cdot A}{360}$ (para bacias pequenas, onde o $t_c$ é pequeno).

## 3. Sistemas de Abastecimento de Água
- **Componentes:** Captação (superficial/subterrânea) $\rightarrow$ Adução $\rightarrow$ ETA $\rightarrow$ Reservação $\rightarrow$ Distribuição.
- **Tratamento (ETA):**
  1. Coagulação (adição de sulfato de alumínio, mistura rápida)
  2. Floculação (mistura lenta)
  3. Decantação
  4. Filtração
  5. Desinfecção/Fluoretação

## 4. Sistemas de Esgotamento Sanitário
- **Coleta:** Sistema separador absoluto (esgoto separado da água pluvial).
- **Transporte e Estações Elevatórias:** Bombeamento de esgoto para vencer desníveis.
- **Tratamento (ETE):**
  - **Preliminar:** Gradeamento, desarenador (remoção de sólidos grosseiros e areia).
  - **Primário:** Decantadores primários (remoção de sólidos suspensos sedimentáveis).
  - **Secundário:** Processos biológicos (lodos ativados, lagoas de estabilização, reatores UASB) para remoção de matéria orgânica (DBO).
  - **Terciário:** Remoção de nutrientes (N e P), patógenos.
- **Reuso:** Uso de efluentes tratados para fins não potáveis.

## 5. Drenagem Pluvial
- **Micro e Macrodrenagem:** 
  - Micro: sistema inicial de captação (guias, sarjetas, bocas de lobo).
  - Macro: galerias tronco, canais, bacias de detenção/retenção.
- **Dimensionamento de Galerias:** Velocidade mínima e máxima, declividade.
- **Componentes:** Poços de visita (PV), caixas de captação, dissipadores de energia.

## 6. Aterros Sanitários
- **Projeto:** Seleção de área, vida útil.
- **Impermeabilização:** Manta PEAD, camada de argila (para evitar contaminação do lençol freático).
- **Drenagem:** Sistema de coleta de chorume e de gases (biogás/metano).
- **Monitoramento:** Poços de monitoramento a montante e jusante.

## 7. Resíduos Sólidos
- **Classificação (NBR 10004):** Classe I (Perigosos), Classe IIA (Não Inertes) e Classe IIB (Inertes).
- **Gestão:** Coleta, transporte, tratamento e destinação final ambientalmente adequada.

## 8. Marco Regulatório do Saneamento
- **Lei 14.026/2020:** 
  - Metas de universalização (99% água potável e 90% coleta e tratamento de esgotos até 2033).
  - Fim dos contratos de programa (obrigatoriedade de licitação).
  - Regionalização dos serviços.
  - Papel regulatório da ANA (Agência Nacional de Águas e Saneamento Básico).

## 9. Estudos de Viabilidade em Saneamento
- **EVTE (Estudo de Viabilidade Técnica e Econômica):** Avaliação de alternativas de projeto, análise de custos (CAPEX e OPEX), rentabilidade.

> [!WARNING]
> Confundir ETA com ETE é um erro comum. Memorize que ETA usa coagulação/floculação e ETE usa tratamento biológico (UASB, lodos ativados).

---

### Fórmulas Importantes
- **Continuidade:** $Q = V \cdot A$
- **Hazen-Williams:** $V = 0,355 \cdot C \cdot D^{0,63} \cdot J^{0,54}$
- **Manning:** $Q = \frac{1}{n} \cdot A \cdot R_h^{2/3} \cdot I^{1/2}$
- **Método Racional:** $Q = C \cdot I \cdot A$

### Checklist de Estudo
- [ ] Revisar tipos de escoamento e perdas de carga
- [ ] Memorizar a fórmula do Método Racional
- [ ] Entender todas as etapas de uma ETA e uma ETE
- [ ] Revisar os conceitos de macro e microdrenagem
- [ ] Ler os principais pontos da Lei 14.026/2020 (Marco do Saneamento)
