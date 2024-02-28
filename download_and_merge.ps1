# Download files
Write-Host "Downloading files..."
Invoke-WebRequest -Uri "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/training1.zip" -OutFile "training1.zip"
Invoke-WebRequest -Uri "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/training2.zip" -OutFile "training2.zip"
Invoke-WebRequest -Uri "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/holdout.zip" -OutFile "holdout.zip"
Invoke-WebRequest -Uri "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/mini_holdout.zip" -OutFile "mini_holdout.zip"
Invoke-WebRequest -Uri "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/mini_holdout_answers.csv" -OutFile "mini_holdout_answers.csv"

# Unzip files
Write-Host "Unzipping files..."
Expand-Archive -Path "training1.zip" -DestinationPath "training1" -Force
Expand-Archive -Path "training2.zip" -DestinationPath "training2" -Force
Expand-Archive -Path "holdout.zip" -DestinationPath "holdout" -Force
Expand-Archive -Path "mini_holdout.zip" -DestinationPath "mini_holdout" -Force

# Merge training data
Write-Host "Merging training data..."
New-Item -ItemType Directory -Name "training"
Move-Item -Path "training1\*" -Destination "training"
Move-Item -Path "training2\*" -Destination "training"

# Clean up
Write-Host "Cleaning up..."
Remove-Item -Path "training1" -Recurse -Force
Remove-Item -Path "training2" -Recurse -Force
Remove-Item -Path "training1.zip" -Force
Remove-Item -Path "training2.zip" -Force
Remove-Item -Path "holdout.zip" -Force
Remove-Item -Path "mini_holdout.zip" -Force

Write-Host "Data ready."
