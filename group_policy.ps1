# Set Password complexity policy to Enabled
Set-ItemProperty -Path "HKLM:\SECURITY\Policies\Microsoft\Windows NT\SecEdit\GptTmpl.inf\Account" -Name "PasswordComplexity" -Value 1

# Ensure 'MSS: (DisableIPSourceRouting) IP source routing protection level (protects against packet spoofing)' is set to 'Enabled
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Services\Tcpip\Parameters" -Name "DisableIPSourceRouting" -Value 2

# Force restart the computer
Restart-Computer -Force

 
