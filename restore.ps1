[CmdletBinding(SupportsShouldProcess = $true)]
param()

$ErrorActionPreference = 'Stop'
$userHome = [System.Environment]::GetFolderPath('UserProfile')
$geminiDir = Join-Path $userHome '.gemini'
$configDir = Join-Path $geminiDir 'config'
$skillsDir = Join-Path $configDir 'skills'
$agentsSkillsDir = Join-Path $userHome '.agents\skills'
$scriptRoot = $PSScriptRoot

function Ensure-Directory {
    [CmdletBinding(SupportsShouldProcess = $true)]
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        if ($PSCmdlet.ShouldProcess($Path, 'Create directory')) {
            New-Item -ItemType Directory -Path $Path -Force | Out-Null
        }
    }
}

Write-Host 'Antigravity skills restore' -ForegroundColor Cyan
Write-Host "Repository: $scriptRoot"
Write-Host "User profile: $userHome"

$coreSkills = @('ui-ux-pro-max', 'brand', 'banner-design', 'design', 'design-system', 'slides', 'ui-styling', 'web-builder')
$copyMappings = @()
foreach ($skill in $coreSkills) {
    $copyMappings += [pscustomobject]@{
        Source = Join-Path (Join-Path $scriptRoot 'skills') $skill
        Destination = $agentsSkillsDir
        ContentsOnly = $false
    }
}
$copyMappings += @(
    [pscustomobject]@{ Source = "$scriptRoot\skills\designer-skills"; Destination = "$geminiDir\designer-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\taste-skill"; Destination = "$geminiDir\taste-skill\skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\codeigniter4\ci4-app-api-skills"; Destination = "$geminiDir\ci4-app-api-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\codeigniter4\codeigniter-skills"; Destination = "$geminiDir\codeigniter-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\vue-ecosystem\vuejs-ai-skills"; Destination = "$geminiDir\vuejs-ai-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\vue-ecosystem\nuxt-skills"; Destination = "$geminiDir\nuxt-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\security\claude-code-owasp"; Destination = "$geminiDir\claude-code-owasp"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\security\security-audit-skill"; Destination = "$geminiDir\security-audit-skill"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\awesome-agent-skills"; Destination = "$geminiDir\awesome-agent-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\threejs\threejs-core-skills"; Destination = "$geminiDir\threejs-core-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\threejs\threejs-webgpu-skills"; Destination = "$geminiDir\threejs-webgpu-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\threejs\threejs-interactive-skills"; Destination = "$geminiDir\threejs-interactive-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\gsap\gsap-official-skills"; Destination = "$geminiDir\gsap-official-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\gsap\gsap-creative-skills"; Destination = "$geminiDir\gsap-creative-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\motion"; Destination = "$geminiDir\motion-design-skills"; ContentsOnly = $true },
    [pscustomobject]@{ Source = "$scriptRoot\skills\image-to-3d"; Destination = "$geminiDir\image-to-3d-skills"; ContentsOnly = $true }
)

$missingSources = @($copyMappings | Where-Object { -not (Test-Path -LiteralPath $_.Source) })
if ($missingSources.Count -gt 0) {
    throw "Restore package is incomplete; required bundle missing: $($missingSources.Source -join ', ')"
}
$templatePath = Join-Path $scriptRoot '.gemini-config\skills.json'
try {
    $template = Get-Content -LiteralPath $templatePath -Raw | ConvertFrom-Json
    if (-not ($template.PSObject.Properties.Name -contains 'entries') -or @($template.entries).Count -eq 0) {
        throw 'entries array is missing or empty'
    }
} catch {
    throw "Restore package has an invalid skills config template: $($_.Exception.Message)"
}
$installedConfigPath = Join-Path $configDir 'skills.json'
if (Test-Path -LiteralPath $installedConfigPath) {
    try {
        $preflightConfig = Get-Content -LiteralPath $installedConfigPath -Raw | ConvertFrom-Json
        if (-not ($preflightConfig.PSObject.Properties.Name -contains 'entries')) { throw 'entries array is missing' }
    } catch {
        throw "Existing skills config is invalid; no files were installed: $installedConfigPath. $($_.Exception.Message)"
    }
}

Ensure-Directory $agentsSkillsDir
Ensure-Directory $geminiDir
Ensure-Directory $configDir
Ensure-Directory $skillsDir
foreach ($mapping in $copyMappings) {
    if (-not (Test-Path -LiteralPath $mapping.Source)) {
        throw "Required bundle disappeared during restore: $($mapping.Source)"
    }
    Ensure-Directory $mapping.Destination
    if ($mapping.ContentsOnly) {
        $sourcePath = Join-Path $mapping.Source '*'
    } else {
        $sourcePath = $mapping.Source
    }
    if ($PSCmdlet.ShouldProcess($mapping.Destination, "Copy bundle from $($mapping.Source)")) {
        Copy-Item -Path $sourcePath -Destination $mapping.Destination -Recurse -Force
    }
}

# Merge generated skill search paths with existing user paths, preserving unrelated entries.
$templatePath = Join-Path $scriptRoot '.gemini-config\skills.json'
if (Test-Path -LiteralPath $templatePath) {
    $template = Get-Content -LiteralPath $templatePath -Raw | ConvertFrom-Json
    $templatePaths = @($template.entries | ForEach-Object {
        if (-not $_.path) { throw 'Invalid skills.json template: each entry needs a path.' }
        $_.path.Replace('${USER_HOME}', ($userHome -replace '\\', '/'))
    })
    $installedConfigPath = Join-Path $configDir 'skills.json'
    $existingPaths = @()
    if (Test-Path -LiteralPath $installedConfigPath) {
        try {
            $existingConfig = Get-Content -LiteralPath $installedConfigPath -Raw | ConvertFrom-Json
            if (-not ($existingConfig.PSObject.Properties.Name -contains 'entries')) { throw 'entries array is missing' }
            $existingPaths = @($existingConfig.entries | Where-Object { $_.path } | ForEach-Object { [string]$_.path })
        } catch {
            throw "Existing skills config is invalid; preserved without changes: $installedConfigPath. $($_.Exception.Message)"
        }
    }
    $mergedPaths = @($existingPaths + $templatePaths | Select-Object -Unique)
    $configProperties = [ordered]@{}
    if ($existingConfig) {
        foreach ($property in $existingConfig.PSObject.Properties) {
            if ($property.Name -ne 'entries') { $configProperties[$property.Name] = $property.Value }
        }
    }
    $configProperties['entries'] = @($mergedPaths | ForEach-Object { [pscustomobject]@{ path = $_ } })
    $newConfig = [pscustomobject]$configProperties
    if ($PSCmdlet.ShouldProcess($installedConfigPath, 'Back up existing config and merge skill paths')) {
        if (Test-Path -LiteralPath $installedConfigPath) {
            $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
            Copy-Item -LiteralPath $installedConfigPath -Destination "$installedConfigPath.$stamp.bak"
        }
        $temporaryConfig = "$installedConfigPath.tmp"
        $newConfig | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $temporaryConfig -Encoding utf8
        Move-Item -LiteralPath $temporaryConfig -Destination $installedConfigPath -Force
    }
}

# Create deterministic links. Duplicate skill folder names get a namespace prefix instead of silently hiding one.
$skillDirs = @(
    foreach ($mapping in $copyMappings) {
        if (-not (Test-Path -LiteralPath $mapping.Source)) { continue }
        $sourceRoot = (Resolve-Path -LiteralPath $mapping.Source).Path
        $destinationRoot = $mapping.Destination
        if (-not $mapping.ContentsOnly) {
            $destinationRoot = Join-Path $destinationRoot (Split-Path $mapping.Source -Leaf)
        }
        Get-ChildItem -LiteralPath $sourceRoot -Filter 'SKILL.md' -File -Recurse -Force -ErrorAction Stop | ForEach-Object {
            $dirPath = $_.Directory.FullName
            $relative = if ($dirPath.Length -gt $sourceRoot.Length) {
                $dirPath.Substring($sourceRoot.Length).TrimStart('\', '/')
            } else {
                ''
            }
            $targetDirectory = if ([string]::IsNullOrWhiteSpace($relative)) { $destinationRoot } else { Join-Path $destinationRoot $relative }
            [pscustomobject]@{ Name = $_.Directory.Name; FullName = $targetDirectory }
        }
    }
) | Sort-Object FullName -Unique
$groups = $skillDirs | Group-Object Name
$created = 0
$alreadyCorrect = 0
$conflicts = [System.Collections.Generic.List[string]]::new()
foreach ($group in $groups) {
    foreach ($directory in ($group.Group | Sort-Object FullName)) {
        $linkName = $directory.Name
        if ($group.Count -gt 1) {
            $parentPath = Split-Path $directory.FullName -Parent
            $parentName = Split-Path $parentPath -Leaf
            if ($parentName -eq 'skills') {
                $grandParent = Split-Path $parentPath -Parent
                if ($grandParent) {
                    $parentName = Split-Path $grandParent -Leaf
                }
            }
            $linkName = "$parentName--$($directory.Name)"
        }
        $linkPath = Join-Path $skillsDir $linkName
        if (Test-Path -LiteralPath $linkPath) {
            $existing = Get-Item -LiteralPath $linkPath -Force
            $target = if ($existing.Target) { [string]$existing.Target } else { '' }
            if ($target -and [System.IO.Path]::GetFullPath($target) -eq [System.IO.Path]::GetFullPath($directory.FullName)) {
                $alreadyCorrect++
            } else {
                $conflicts.Add("$linkName -> $linkPath (existing entry points elsewhere or is not a junction)")
            }
            continue
        }
        if ($PSCmdlet.ShouldProcess($linkPath, "Create skill junction to $($directory.FullName)")) {
            try {
                New-Item -ItemType Junction -Path $linkPath -Target $directory.FullName -ErrorAction Stop | Out-Null
                $created++
            } catch {
                $conflicts.Add("$linkName -> $linkPath ($($_.Exception.Message))")
            }
        }
    }
}

if ($conflicts.Count -gt 0) {
    Write-Warning "Restore finished with $($conflicts.Count) unresolved link conflict(s):"
    $conflicts | ForEach-Object { Write-Warning "  $_" }
    throw 'Restore is incomplete. Resolve the reported conflicts and run restore.ps1 again.'
}
Write-Host "Restore complete: $created junction(s) created; $alreadyCorrect already correct; $($skillDirs.Count) skills discovered." -ForegroundColor Green
Write-Host 'Existing MCP configuration was left untouched.'
