$rootDir = $PSScriptRoot

$envPath = Join-Path $rootDir 'backend\.venv'

if(Test-Path $envPath){
    & "$envPath\Scripts\activate.ps1"
    Write-Host "Virtual Environment Activated"
} else {
    Write-Host "Virtual Environment not found at $envPath"
}