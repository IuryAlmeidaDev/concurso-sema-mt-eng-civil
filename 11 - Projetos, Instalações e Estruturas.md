---
tags:
  - projetos
  - instalacoes
  - estruturas
  - especifico-eng
---
# 📐 Projetos, Instalações e Estruturas

## PARTE 1: PROJETOS E INSTALAÇÕES

### 1. Projetos de Obras Civis
- Compatibilização de projetos (BIM é essencial).
- Envolve projetos de arquitetura, fundações, estrutura, instalações (MEP - Mecânica, Elétrica, Hidráulica).

### 2. Instalações Hidrossanitárias (NBR 5626, NBR 8160, NBR 10844)
- **Água fria e quente:** Pressão estática máxima (40 m.c.a) e dinâmica mínima. Uso do método dos pesos (Hunter) para vazão de projeto.
- **Esgoto:** Uso de fecho hídrico (sifão, ralo sifonado) para evitar retorno de gases. Ventilação sanitária é obrigatória.
- **Águas Pluviais:** Dimensionamento de calhas e condutores usando a chuva de projeto (Tempo de Retorno e Intensidade).

### 3. Instalações Elétricas (NBR 5410)
- **Critérios de dimensionamento:** Capacidade de condução de corrente, queda de tensão admissível.
- **Componentes:** Disjuntores termomagnéticos (proteção contra curto e sobrecarga), DR (Diferencial Residual - choque elétrico), DPS (Surtos).
- **Aterramento:** Sistemas TN, TT, IT. O TN-S (neutro e proteção separados) é um dos mais usados.

### 4. Instalações de Gás (NBR 15526, NBR 13523)
- **GLP (Gás Liquefeito de Petróleo):** Mais pesado que o ar. Recipientes em área externa e ventilada.
- **GN (Gás Natural):** Mais leve que o ar. 

### 5. Prevenção e Combate a Incêndio (PPCI)
- **Componentes:** Extintores, hidrantes, mangotinhos, chuveiros automáticos (*sprinklers*).
- **SPDA (Para-raios):** NBR 5419. Gaiola de Faraday, método de Franklin, esfera rolante.
- **Rotas de Fuga:** NBR 9077. Portas corta-fogo, sinalização, escadas enclausuradas.

### 6. Obras de Arte Especiais
- **Pontes e Viadutos:** Superestrutura (tabuleiro), mesoestrutura (pilares) e infraestrutura (fundações). 
- Sujeitos a cargas móveis (Linhas de Influência - Trem tipo).

---

## PARTE 2: ESTRUTURAS

### 1. Concreto Armado (NBR 6118)
- **Domínios de deformação:** Domínio 2 (aço escoa, concreto não rompe), Domínio 3 (ruptura simultânea ou aço escoa e concreto rompe - o ideal), Domínio 4 (concreto rompe sem escoamento do aço - frágil, evitar!).
- **Cobrimento:** Protege a armadura (varia com a Classe de Agressividade Ambiental).
- **Esforços:** 
  - Flexão: Armadura longitudinal.
  - Cisalhamento: Estribos (armadura transversal).

### 2. Estruturas Metálicas (NBR 8800) e Mistas
- Aço estrutural (ASTM A36, A572).
- Ligações por solda (filete, penetração) ou parafusos (alta resistência, AR).
- **Mistas:** Viga de aço + Laje de concreto conectadas por *stud bolts* (conectores de cisalhamento). 

### 3. Mecânica das Estruturas e Análise
- **Equilíbrio da estática:** $\sum F_x = 0$, $\sum F_y = 0$, $\sum M = 0$.
- **Vínculos:** Apoios de 1º grau (móvel), 2º grau (fixo), 3º grau (engaste).
- **Diagramas:**
  - N (Normal): Tração e compressão.
  - V ou Q (Cortante): Variação linear em carga distribuída, constante em cargas pontuais.
  - M (Momento Fletor): Máximo onde a cortante é zero.
- **Estruturas Isostáticas:** Resolvidas por equações de equilíbrio.
- **Estruturas Hiperestáticas:** Requerem métodos como Processo de Cross, Método das Forças, Método dos Deslocamentos.

## NBRs Relevantes
- **NBR 6118:** Projeto de estruturas de concreto.
- **NBR 8800:** Estruturas de aço e estruturas mistas de aço e concreto.
- **NBR 6120:** Cargas para cálculo de estruturas.
- **NBR 8681:** Ações e segurança nas estruturas.

## Checklist de Revisão
- [ ] Compreender os limites de pressão na rede de água fria.
- [ ] Diferenciar os disjuntores, DR e DPS nas instalações elétricas.
- [ ] Revisar cálculo de reações de apoio de vigas biapoiadas e engastadas.
- [ ] Entender perfeitamente os Domínios de deformação (especialmente 2 e 3) do concreto armado.
