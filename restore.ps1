<#
.SYNOPSIS
    Antigravity AI Skills & Configuration Restore Script
.DESCRIPTION
    Script ini memulihkan seluruh skills dan konfigurasi global Antigravity
    ke direktori ~/.gemini/config/ dan ~/.agents/skills/
#>

$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Antigravity Skills & Config Restore" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

$userHome = [System.Environment]::GetFolderPath("UserProfile")
$geminiDir = Join-Path $userHome ".gemini"
$configDir = Join-Path $geminiDir "config"
$skillsDir = Join-Path $configDir "skills"
$agentsSkillsDir = Join-Path $userHome ".agents\skills"
$scriptRoot = $PSScriptRoot

# 1. Pastikan folder tujuan ada
Write-Host "`n[1/4] Membuat direktori tujuan..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
New-Item -ItemType Directory -Force -Path $agentsSkillsDir | Out-Null

# 2. Pulihkan Konfigurasi
Write-Host "[2/4] Memulihkan file konfigurasi Antigravity..." -ForegroundColor Yellow
if (Test-Path "$scriptRoot\.gemini-config\skills.json") {
    Copy-Item "$scriptRoot\.gemini-config\skills.json" "$configDir\skills.json" -Force
}
if (Test-Path "$scriptRoot\.gemini-config\mcp_config.json") {
    Copy-Item "$scriptRoot\.gemini-config\mcp_config.json" "$configDir\mcp_config.json" -Force
}

# 3. Pulihkan Skills ke ~/.agents/skills/ dan ~/.gemini/
Write-Host "[3/4] Menyalin aset skills..." -ForegroundColor Yellow
# UI UX Pro Max & bundle skills
$coreSkills = @("ui-ux-pro-max", "brand", "banner-design", "design", "design-system", "slides", "ui-styling")
foreach ($skill in $coreSkills) {
    $src = Join-Path "$scriptRoot\skills" $skill
    if (Test-Path $src) {
        Copy-Item -Recurse -Force $src $agentsSkillsDir
    }
}

# Designer Skills suite
$designerDest = Join-Path $geminiDir "designer-skills"
if (Test-Path "$scriptRoot\skills\designer-skills") {
    New-Item -ItemType Directory -Force -Path $designerDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\designer-skills\*" $designerDest
}

# Taste Skill suite
$tasteDest = Join-Path $geminiDir "taste-skill\skills"
if (Test-Path "$scriptRoot\skills\taste-skill") {
    New-Item -ItemType Directory -Force -Path $tasteDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\taste-skill\*" $tasteDest
}

# CodeIgniter 4 Skills suite
if (Test-Path "$scriptRoot\skills\codeigniter4\ci4-app-api-skills") {
    $ci4AppDest = Join-Path $geminiDir "ci4-app-api-skills"
    New-Item -ItemType Directory -Force -Path $ci4AppDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\codeigniter4\ci4-app-api-skills\*" $ci4AppDest
}
if (Test-Path "$scriptRoot\skills\codeigniter4\codeigniter-skills") {
    $ci4CoreDest = Join-Path $geminiDir "codeigniter-skills"
    New-Item -ItemType Directory -Force -Path $ci4CoreDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\codeigniter4\codeigniter-skills\*" $ci4CoreDest
}

# Vue 3 & Nuxt Ecosystem Skills suite
if (Test-Path "$scriptRoot\skills\vue-ecosystem\vuejs-ai-skills") {
    $vueDest = Join-Path $geminiDir "vuejs-ai-skills"
    New-Item -ItemType Directory -Force -Path $vueDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\vue-ecosystem\vuejs-ai-skills\*" $vueDest
}
if (Test-Path "$scriptRoot\skills\vue-ecosystem\nuxt-skills") {
    $nuxtDest = Join-Path $geminiDir "nuxt-skills"
    New-Item -ItemType Directory -Force -Path $nuxtDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\vue-ecosystem\nuxt-skills\*" $nuxtDest
}

# Security Audit & Bug Hunter Suite
if (Test-Path "$scriptRoot\skills\security\claude-code-owasp") {
    $owaspDest = Join-Path $geminiDir "claude-code-owasp"
    New-Item -ItemType Directory -Force -Path $owaspDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\security\claude-code-owasp\*" $owaspDest
}
if (Test-Path "$scriptRoot\skills\security\security-audit-skill") {
    $auditDest = Join-Path $geminiDir "security-audit-skill"
    New-Item -ItemType Directory -Force -Path $auditDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\security\security-audit-skill\*" $auditDest
}

# Awesome Agent Skills Catalog
if (Test-Path "$scriptRoot\skills\awesome-agent-skills") {
    $awesomeDest = Join-Path $geminiDir "awesome-agent-skills"
    New-Item -ItemType Directory -Force -Path $awesomeDest | Out-Null
    Copy-Item -Recurse -Force "$scriptRoot\skills\awesome-agent-skills\*" $awesomeDest
}

# 4. Buat Directory Junctions di ~/.gemini/config/skills/
Write-Host "[4/4] Mendaftarkan Junctions di global skills directory..." -ForegroundColor Yellow
$allSkillMds = Get-ChildItem -Recurse $geminiDir -Filter "SKILL.md" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Directory
$allAgentMds = Get-ChildItem -Recurse $agentsSkillsDir -Filter "SKILL.md" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Directory

$totalLinked = 0
foreach ($dir in (@($allSkillMds) + @($allAgentMds))) {
    $link = Join-Path $skillsDir $dir.Name
    if (-not (Test-Path $link)) {
        try {
            New-Item -ItemType Junction -Path $link -Target $dir.FullName | Out-Null
            $totalLinked++
        } catch {}
    }
}

Write-Host "`n✅ Pemulihan selesai! $totalLinked skills terhubung secara global ke Antigravity." -ForegroundColor Green
Write-Host "Silakan restart Antigravity IDE atau jalankan sesi baru untuk memuat seluruh skill." -ForegroundColor Green
