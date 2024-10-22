$exclude = @("venv", "botMV.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botMV.zip" -Force