$exclude = @("venv", "dados_ibge.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "dados_ibge.zip" -Force