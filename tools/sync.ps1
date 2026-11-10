# 一键同步：把当前所有改动提交并推送到 GitHub
# 用法：
#   VSCode 里按 Ctrl+Shift+B（会提示输入说明）
#   或在 PowerShell 里运行： .\tools\sync.ps1 -Message "练习：读取 Excel"
param(
    [string]$Message = ""
)

$ErrorActionPreference = 'Continue'
$repo = Split-Path -Parent $PSScriptRoot

# 定位 git：优先 PATH，找不到就回退到安装目录
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
$git = if ($gitCmd) { $gitCmd.Source } else { 'D:\Program Files\Git\cmd\git.exe' }
if (-not (Test-Path -LiteralPath $git)) {
    Write-Host '[错误] 找不到 git，请确认 Git for Windows 已安装。' -ForegroundColor Red
    exit 1
}

Push-Location -LiteralPath $repo
try {
    $branch = (& $git branch --show-current).Trim()
    if (-not $branch) { $branch = 'main' }

    Write-Host '== 1/4 收集改动 ==' -ForegroundColor Cyan
    & $git add -A

    & $git diff --cached --quiet
    $hasChanges = ($LASTEXITCODE -eq 1)

    if ($hasChanges) {
        if ([string]::IsNullOrWhiteSpace($Message)) {
            $Message = 'practice: ' + (Get-Date -Format 'yyyy-MM-dd HH:mm')
        }
        Write-Host ("== 2/4 提交：$Message ==") -ForegroundColor Cyan
        & $git commit -m $Message
        if ($LASTEXITCODE -ne 0) {
            Write-Host '[错误] 提交失败，已停止，不会推送。' -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host '== 2/4 没有新改动，跳过提交 ==' -ForegroundColor Cyan
    }

    Write-Host ("== 3/4 推送到 GitHub ($branch) ==") -ForegroundColor Cyan
    & $git push origin $branch
    if ($LASTEXITCODE -ne 0) {
        Write-Host '[错误] 推送失败，检查网络或 GitHub 登录状态。' -ForegroundColor Red
        exit 1
    }

    Write-Host '== 4/4 完成 ==' -ForegroundColor Green
    Write-Host '线上查看： https://github.com/zenquanw/hustle' -ForegroundColor Green
}
finally {
    Pop-Location
}
