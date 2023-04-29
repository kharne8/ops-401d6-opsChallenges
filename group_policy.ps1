# Set Password complexity policy to Enabled
Set-ItemProperty -Path "HKLM:\SECURITY\Policies\Microsoft\Windows NT\SecEdit\GptTmpl.inf\Account" -Name "PasswordComplexity" -Value 1

# Set RelaxMinimumPasswordLengthLimits to 1
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\SAM" -Name "RelaxMinimumPasswordLengthLimits" -Value 1

# Force restart the computer
Restart-Computer -Force

