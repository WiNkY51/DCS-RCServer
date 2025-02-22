dofile(lfs.writedir()..[[Scripts\Export.lua]])

function ProcessCommand(commaand)
    if commaand == "GEAR_UP" then 
    LoSetCommand(430)
    elseif string.find(commaand, "THROTTLE:") then
        local value = tonumber(string.match(commaand, "THROTTLE:($d+)"))
        if value then
            LoSetCommand(2004, value / 100)
        end
    end
end