import os
import json
import glob
import re

vault_dir = r"C:\Users\03573608183\Documents\Obsidian\SEMA-MT-Eng-Civil"
web_dir = r"C:\Users\03573608183\Documents\Obsidian\SEMA-MT-Eng-Civil"
os.makedirs(web_dir, exist_ok=True)

# List of files in order
files_meta = [
    {"id": "00-dashboard", "title": "🎯 Dashboard e Visão Geral", "file": "00 - Dashboard.md", "category": "Planejamento"},
    {"id": "01-fluxo", "title": "📋 Fluxo de Estudo Completo", "file": "01 - Fluxo de Estudo.md", "category": "Planejamento"},
    {"id": "02-cronograma", "title": "📅 Cronograma Oficial", "file": "02 - Cronograma Oficial.md", "category": "Planejamento"},
    {"id": "03-portugues", "title": "📝 Língua Portuguesa", "file": "03 - Língua Portuguesa.md", "category": "Conhecimentos Básicos"},
    {"id": "04-geografia-historia-mt", "title": "🗺️ Geografia e História de MT", "file": "04 - Geografia e História de MT.md", "category": "Conhecimentos Gerais"},
    {"id": "05-etica-filosofia", "title": "⚖️ Ética, Filosofia e Legislação", "file": "05 - Ética, Filosofia, Atualidades e Legislação.md", "category": "Conhecimentos Gerais"},
    {"id": "06-legislacao-ambiental", "title": "🌿 Legislação e Política Ambiental", "file": "06 - Legislação Ambiental (Transversal).md", "category": "Conhecimentos Transversais"},
    {"id": "07-licenciamento", "title": "🔍 Licenciamento e Fiscalização", "file": "07 - Licenciamento e Fiscalização Ambiental.md", "category": "Conhecimentos Transversais"},
    {"id": "08-recursos-clima", "title": "🌍 Recursos Naturais, Poluição e Clima", "file": "08 - Recursos Naturais, Poluição e Clima.md", "category": "Conhecimentos Transversais"},
    {"id": "09-geotecnia", "title": "🏗️ Geotecnia e Obras de Terra", "file": "09 - Geotecnia e Obras de Terra.md", "category": "Engenharia Civil"},
    {"id": "10-materiais", "title": "🧱 Materiais e Tecnologia da Construção", "file": "10 - Materiais e Tecnologia da Construção.md", "category": "Engenharia Civil"},
    {"id": "11-projetos-estruturas", "title": "📐 Projetos, Instalações e Estruturas", "file": "11 - Projetos, Instalações e Estruturas.md", "category": "Engenharia Civil"},
    {"id": "12-orcamento", "title": "💰 Orçamento, Planejamento e Fiscalização", "file": "12 - Orçamento, Planejamento e Fiscalização de Obras.md", "category": "Engenharia Civil"},
    {"id": "13-avaliacao", "title": "🏠 Avaliação Imobiliária (NBR 14653/AVM)", "file": "13 - Avaliação Imobiliária.md", "category": "Engenharia Civil"},
    {"id": "14-pavimentacao", "title": "🛣️ Pavimentação, Vias e Mobilidade", "file": "14 - Pavimentação, Vias e Mobilidade.md", "category": "Engenharia Civil"},
    {"id": "15-sustentabilidade", "title": "♻️ Sustentabilidade e Acessibilidade", "file": "15 - Sustentabilidade e Acessibilidade.md", "category": "Engenharia Civil"},
    {"id": "16-hidraulica", "title": "💧 Hidráulica, Hidrologia e Saneamento", "file": "16 - Hidráulica, Hidrologia e Saneamento.md", "category": "Engenharia Civil"},
    {"id": "17-legislacao-eng", "title": "📜 Legislação de Engenharia e Urbanismo", "file": "17 - Legislação de Engenharia e Urbanismo.md", "category": "Engenharia Civil"},
    {"id": "18-discursiva", "title": "✍️ Prova Discursiva — Estratégia", "file": "18 - Prova Discursiva - Estratégia.md", "category": "Discursiva & Banca"},
    {"id": "19-cesgranrio", "title": "🎓 Estratégia Banca Cesgranrio", "file": "19 - Estratégia para a Banca Cesgranrio.md", "category": "Discursiva & Banca"}
]

docs_data = []

for item in files_meta:
    fpath = os.path.join(vault_dir, item["file"])
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    docs_data.append({
        "id": item["id"],
        "title": item["title"],
        "category": item["category"],
        "fileName": item["file"],
        "content": content
    })

print("Loaded all docs. Count:", len(docs_data))

# Generate HTML
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Guia de Estudo — SEMA/MT 2026 (Engenheiro Civil)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <style>
    :root {
      --primary: #059669;
      --primary-hover: #047857;
      --primary-light: #ecfdf5;
      --bg: #ffffff;
      --bg-alt: #f8fafc;
      --border: #e2e8f0;
      --text: #0f172a;
      --text-muted: #64748b;
      --sidebar-w: 320px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      color: var(--text);
      background: var(--bg);
      line-height: 1.65;
    }

    /* Layout */
    .app { display: flex; min-height: 100vh; }
    
    /* Sidebar */
    .sidebar {
      width: var(--sidebar-w);
      background: var(--bg-alt);
      border-right: 1px solid var(--border);
      position: fixed;
      top: 0; bottom: 0; left: 0;
      display: flex;
      flex-direction: column;
      z-index: 50;
      transition: transform 0.3s ease;
    }

    .sidebar-header {
      padding: 20px 20px 14px;
      border-bottom: 1px solid var(--border);
      background: #ffffff;
    }
    .brand-title {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .brand-sub {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 500;
      margin-top: 2px;
    }
    .search-box {
      margin-top: 12px;
      position: relative;
    }
    .search-box input {
      width: 100%;
      padding: 9px 12px 9px 34px;
      font-size: 0.85rem;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: #ffffff;
      outline: none;
      transition: border-color 0.2s;
    }
    .search-box input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.15);
    }
    .search-icon {
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    .sidebar-menu {
      flex: 1;
      overflow-y: auto;
      padding: 16px 12px 24px;
    }
    .category-group { margin-bottom: 20px; }
    .category-title {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      padding: 0 10px 6px;
    }
    .nav-item {
      display: block;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 500;
      color: #334155;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s ease;
      margin-bottom: 2px;
    }
    .nav-item:hover {
      background: #e2e8f0;
      color: #0f172a;
    }
    .nav-item.active {
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      border-left: 3px solid var(--primary);
    }

    /* Main Content */
    .main {
      margin-left: var(--sidebar-w);
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }

    .top-bar {
      height: 58px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
      background: #ffffff;
      position: sticky;
      top: 0;
      z-index: 40;
    }
    .top-bar-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .mobile-menu-btn {
      display: none;
      background: none;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 6px 10px;
      font-size: 1.1rem;
      cursor: pointer;
    }
    .badge-info {
      background: #f1f5f9;
      color: #475569;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .badge-primary {
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 700;
    }
    .github-link {
      font-size: 0.85rem;
      font-weight: 600;
      color: #334155;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .github-link:hover { color: var(--primary); }

    .content-container {
      max-width: 960px;
      width: 100%;
      margin: 0 auto;
      padding: 40px 32px 80px;
    }

    /* Markdown Styling */
    .markdown-body h1 {
      font-size: 2.1rem;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
      margin-bottom: 16px;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 12px;
    }
    .markdown-body h2 {
      font-size: 1.45rem;
      font-weight: 700;
      color: #1e293b;
      margin-top: 36px;
      margin-bottom: 14px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }
    .markdown-body h3 {
      font-size: 1.18rem;
      font-weight: 700;
      color: #334155;
      margin-top: 24px;
      margin-bottom: 10px;
    }
    .markdown-body p {
      margin-bottom: 16px;
      color: #334155;
      font-size: 1rem;
    }
    .markdown-body ul, .markdown-body ol {
      margin-bottom: 20px;
      padding-left: 24px;
      color: #334155;
    }
    .markdown-body li { margin-bottom: 6px; }

    /* Tables */
    .markdown-body table {
      width: 100%;
      border-collapse: collapse;
      margin: 24px 0;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      font-size: 0.92rem;
    }
    .markdown-body th, .markdown-body td {
      border: 1px solid var(--border);
      padding: 11px 16px;
    }
    .markdown-body th {
      background: #f1f5f9;
      color: #1e293b;
      font-weight: 700;
      text-align: left;
    }
    .markdown-body tr:nth-child(even) { background: #f8fafc; }

    /* Callouts */
    .callout {
      border-radius: 8px;
      padding: 14px 18px;
      margin: 20px 0;
      font-size: 0.95rem;
      line-height: 1.6;
      border-left: 5px solid;
    }
    .callout-note {
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1e40af;
    }
    .callout-tip {
      background: #ecfdf5;
      border-color: #10b981;
      color: #065f46;
    }
    .callout-warning {
      background: #fffbeb;
      border-color: #f59e0b;
      color: #92400e;
    }
    .callout-important {
      background: #f5f3ff;
      border-color: #8b5cf6;
      color: #5b21b6;
    }

    /* Mermaid */
    .mermaid {
      background: #f8fafc;
      padding: 24px;
      border-radius: 12px;
      border: 1px solid var(--border);
      margin: 24px 0;
      display: flex;
      justify-content: center;
      overflow-x: auto;
    }

    /* Tasks Checkboxes */
    .task-list-item {
      list-style-type: none;
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }
    .task-list-item input[type="checkbox"] {
      width: 18px;
      height: 18px;
      accent-color: var(--primary);
      cursor: pointer;
    }

    /* Navigation Footer */
    .doc-nav {
      display: flex;
      justify-content: space-between;
      gap: 16px;
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid var(--border);
    }
    .doc-btn {
      display: flex;
      flex-direction: column;
      padding: 12px 18px;
      border: 1px solid var(--border);
      border-radius: 10px;
      text-decoration: none;
      color: #334155;
      transition: all 0.2s;
      max-width: 48%;
      cursor: pointer;
    }
    .doc-btn:hover {
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary);
    }
    .doc-btn-label {
      font-size: 0.72rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
    }
    .doc-btn-title {
      font-size: 0.92rem;
      font-weight: 600;
      margin-top: 2px;
    }

    /* Responsive */
    @media (max-width: 900px) {
      .sidebar {
        transform: translateX(-100%);
      }
      .sidebar.open {
        transform: translateX(0);
      }
      .main {
        margin-left: 0;
      }
      .mobile-menu-btn {
        display: block;
      }
      .content-container {
        padding: 24px 18px 60px;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <div class="brand-title">🏗️ SEMA/MT 2026</div>
        <div class="brand-sub">Analista de Meio Ambiente • Eng. Civil</div>
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" id="searchInput" placeholder="Pesquisar leis ou temas...">
        </div>
      </div>
      <nav class="sidebar-menu" id="sidebarMenu"></nav>
    </aside>

    <!-- Main Content -->
    <div class="main">
      <header class="top-bar">
        <div class="top-bar-left">
          <button class="mobile-menu-btn" id="menuToggle" aria-label="Menu">☰</button>
          <span class="badge-primary">Salário R$ 10.491,97</span>
          <span class="badge-info">Prova: 13/12/2026</span>
        </div>
        <a href="https://github.com/IuryAlmeidaDev/concurso-sema-mt-eng-civil" target="_blank" class="github-link">
          🐙 Ver no GitHub
        </a>
      </header>

      <main class="content-container">
        <article class="markdown-body" id="contentArea">
          Carregando conteúdo...
        </article>

        <div class="doc-nav" id="docNav"></div>
      </main>
    </div>
  </div>

  <script>
    const DOCS = """ + json.dumps(docs_data, ensure_ascii=False) + """;

    // Setup Marked options
    marked.setOptions({
      gfm: true,
      breaks: true
    });

    mermaid.initialize({ startOnLoad: false, theme: 'default' });

    let currentDocIndex = 0;

    // Process markdown to convert Obsidian callouts and wikilinks
    function processMarkdown(md) {
      // Clean YAML frontmatter
      md = md.replace(/^---[\\s\\S]*?---\\s*/m, '');

      // Replace Obsidian Wikilinks: [[Target|Label]] -> [Label](#/id)
      md = md.replace(/\\[\\[(.*?)\\|(.*?)\\]\\]/g, function(match, p1, p2) {
        const found = DOCS.find(d => d.title.includes(p1.trim()) || d.fileName.includes(p1.trim()));
        const linkId = found ? found.id : '00-dashboard';
        return `[${p2.trim()}](#/${linkId})`;
      });

      md = md.replace(/\\[\\[(.*?)\\]\\]/g, function(match, p1) {
        const found = DOCS.find(d => d.title.includes(p1.trim()) || d.fileName.includes(p1.trim()));
        const linkId = found ? found.id : '00-dashboard';
        return `[${p1.trim()}](#/${linkId})`;
      });

      // Render Markdown to HTML first
      let html = marked.parse(md);

      // Process Callouts in HTML blockquotes
      html = html.replace(/<blockquote>\\s*<p>\\s*\\[!NOTE\\]\\s*([\\s\\S]*?)<\\/p>\\s*<\\/blockquote>/gi, '<div class="callout callout-note"><strong>ℹ️ NOTA:</strong> $1</div>');
      html = html.replace(/<blockquote>\\s*<p>\\s*\\[!TIP\\]\\s*([\\s\\S]*?)<\\/p>\\s*<\\/blockquote>/gi, '<div class="callout callout-tip"><strong>💡 DICA:</strong> $1</div>');
      html = html.replace(/<blockquote>\\s*<p>\\s*\\[!WARNING\\]\\s*([\\s\\S]*?)<\\/p>\\s*<\\/blockquote>/gi, '<div class="callout callout-warning"><strong>⚠️ ATENÇÃO:</strong> $1</div>');
      html = html.replace(/<blockquote>\\s*<p>\\s*\\[!IMPORTANT\\]\\s*([\\s\\S]*?)<\\/p>\\s*<\\/blockquote>/gi, '<div class="callout callout-important"><strong>❗ IMPORTANTE:</strong> $1</div>');
      html = html.replace(/<blockquote>\\s*<p>\\s*\\[!CAUTION\\]\\s*([\\s\\S]*?)<\\/p>\\s*<\\/blockquote>/gi, '<div class="callout callout-warning"><strong>🛑 CUIDADO:</strong> $1</div>');

      // Process Mermaid code blocks
      html = html.replace(/<pre><code class="language-mermaid">([\\s\\S]*?)<\\/code><\\/pre>/gi, '<div class="mermaid">$1</div>');

      return html;
    }

    // Render Sidebar
    function renderSidebar(filteredDocs = null) {
      const menu = document.getElementById('sidebarMenu');
      const docsToRender = filteredDocs || DOCS;
      
      const categories = {};
      docsToRender.forEach(doc => {
        if (!categories[doc.category]) categories[doc.category] = [];
        categories[doc.category].push(doc);
      });

      let html = '';
      for (const [category, items] of Object.entries(categories)) {
        html += `<div class="category-group">
          <div class="category-title">${category}</div>`;
        items.forEach(doc => {
          const isActive = DOCS[currentDocIndex] && DOCS[currentDocIndex].id === doc.id ? 'active' : '';
          html += `<a class="nav-item ${isActive}" onclick="loadDoc('${doc.id}')">${doc.title}</a>`;
        });
        html += `</div>`;
      }
      menu.innerHTML = html;
    }

    // Load Document
    async function loadDoc(id) {
      const index = DOCS.findIndex(d => d.id === id);
      if (index === -1) return;

      currentDocIndex = index;
      window.location.hash = '#/' + id;

      const doc = DOCS[index];
      const contentArea = document.getElementById('contentArea');
      contentArea.innerHTML = processMarkdown(doc.content);

      // Render Mermaid diagrams if present
      const mermaidDivs = contentArea.querySelectorAll('.mermaid');
      if (mermaidDivs.length > 0) {
        try {
          await mermaid.run({ nodes: mermaidDivs });
        } catch(e) {
          console.warn('Mermaid render warning:', e);
        }
      }

      // Update Navigation Buttons (Next / Prev)
      renderNavButtons();
      renderSidebar();

      // Scroll to top
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Close mobile sidebar if open
      document.getElementById('sidebar').classList.remove('open');
    }

    function renderNavButtons() {
      const navContainer = document.getElementById('docNav');
      let html = '';

      if (currentDocIndex > 0) {
        const prev = DOCS[currentDocIndex - 1];
        html += `<div class="doc-btn" onclick="loadDoc('${prev.id}')">
          <span class="doc-btn-label">← Anterior</span>
          <span class="doc-btn-title">${prev.title}</span>
        </div>`;
      } else {
        html += `<div></div>`;
      }

      if (currentDocIndex < DOCS.length - 1) {
        const next = DOCS[currentDocIndex + 1];
        html += `<div class="doc-btn" style="text-align: right; margin-left: auto;" onclick="loadDoc('${next.id}')">
          <span class="doc-btn-label">Próximo →</span>
          <span class="doc-btn-title">${next.title}</span>
        </div>`;
      }

      navContainer.innerHTML = html;
    }

    // Search filter
    document.getElementById('searchInput').addEventListener('input', function(e) {
      const term = e.target.value.toLowerCase().trim();
      if (!term) {
        renderSidebar();
        return;
      }
      const filtered = DOCS.filter(d => 
        d.title.toLowerCase().includes(term) || 
        d.content.toLowerCase().includes(term)
      );
      renderSidebar(filtered);
    });

    // Mobile menu toggle
    document.getElementById('menuToggle').addEventListener('click', function() {
      document.getElementById('sidebar').classList.toggle('open');
    });

    // Hash change handler for direct links
    window.addEventListener('hashchange', function() {
      const hash = window.location.hash.replace('#/', '');
      if (hash) {
        loadDoc(hash);
      }
    });

    // Initial load
    const initialHash = window.location.hash.replace('#/', '');
    if (initialHash && DOCS.some(d => d.id === initialHash)) {
      loadDoc(initialHash);
    } else {
      loadDoc('00-dashboard');
    }
  </script>
</body>
</html>
"""

output_path = os.path.join(web_dir, "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print("index.html compiled successfully. Size:", len(html_template), "bytes")
