# Function to check if the "MX MCHNCL" keyboard is connected
function Test-MXKeyboard {
    $keyboard = Get-CimInstance Win32_PnPEntity | Where-Object { $_.Name -match "^HID Keyboard" }
  
    return $keyboard
}

# Store initial state of the keyboard
$keyboardConnected = Test-MXKeyboard


# Loop to keep checking the device status
Write-Host "Monitoring MX MCHNCL device status... Press Ctrl+C to stop."# Debug print to show initial state

while ($true) {
    while ($true) {
        # Check if the keyboard is still connected
        $currentState = Test-MXKeyboard

        # If the keyboard was previously connected and is no longer found
        if ($keyboardConnected -and !$currentState) {
            Write-Host "HID keyboard removed"
            $keyboardConnected = $null  # Update state to reflect the device is removed
            break;
        }
        # If the keyboard was previously removed and is now found
        elseif (-not $keyboardConnected -and $currentState) {
            Write-Host "HID keyboard added"
            $keyboardConnected = $currentState  # Update state to reflect the device is added
        }
        
        # Sleep before checking again
        Start-Sleep -Milliseconds 500
    }
    Write-Host "Waiting for mouse action to request keyboard..."
    Start-Process "C:\Program Files\InputSwitcher\request_keyb_on_mouse_action.exe" -Wait -Verb RunAs -WindowStyle Hidden
}






