#연습문제7
import time
fseconds = time.time()
fmins = fseconds//60
min = fmins%60
fhours = fmins//60
hour = fhours%24

print("현재 시간(영국 그리니치 시각):",int(hour),"시",int(min),"분")
