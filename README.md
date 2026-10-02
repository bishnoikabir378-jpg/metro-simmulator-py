
data sources:
---collected metro station data from DMRC website
---my metro_data.txt file contins data in form (line,present station,next station,minutes between,change yes/no)

Assumptions made:
--- time between 2 stations assumed to be same i.e. 2 minutes
--- 3 minutes interchange delay
--- interchanges are autodetected based on the shortest path.
---first metro will start at 6:00 in morning from dwarka sector 21,Noida electronic city,yamuna bank,vaishali,janakpuri west,botanical garden
---user must input time between 6:00 to 23:00 
---the station entered must have correct speelling and be in blue and magenta line and can contain lowercase or uppercase anything
---if you enter janakpuri west and botanical garden you must enter magenta or blue with it
--- user will have to run the program again and can perform task again.

instructions to run the program:

--- bonus fare added on the basis of station in between start and end
---i have merged both the parts of Question in a single part i.e. metro timings simulator and ride journey planner user just need to enter the start and end station and time and my code will print both the timings of next direction and journey planner in that direction.
--- user just need to enter the first and last station and the current time and my program will print all the things
    to avoid unnecessary options my code will print the changeover station according to the shortest path and 
    will print the next metro time and fare and total time and time you will reach 
