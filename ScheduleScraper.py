from selenium import webdriver
import time
import SQLCommands

driver = webdriver.Chrome("Drivers/chromedriver.exe")
department = ["CSE"]  # Enter Department's Code
semester = "summer"  # spring, summer, fall, or winter

# Table starts at the 5th row
for dep in department:
    website = f"http://www.buffalo.edu/class-schedule?switch=showcourses&semester={semester}&division=UGRD&dept={dep}"
    driver.get(website)
    time.sleep(5)
    connect = SQLCommands.create_connection("pythonsqlite.db")
    numOfCourses = int(driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td').text.strip().split(" ")[0]) + 5
    for i in range(5, numOfCourses):
        prof = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[" + str(i) + "]/td[10]").text.strip()
        cour = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[" + str(i) + "]/td[3]").text.strip()
        abr = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr[" + str(i) + "]/td[2]").text.strip()
        course = (abr + " - " + cour)
        if SQLCommands.courseindb(course):
            if SQLCommands.profandcourse(prof, course) and prof != "Staff":
                SQLCommands.dbappend(course, prof)
            elif not SQLCommands.profNOTindb(prof):
                SQLCommands.update_semester(("✔", prof, course))
        else:
            if cour == "Title" or prof == "Staff" or abr == "CSE 495TUT" or abr == "CSE 499TUT" or abr == "CSE 498TUT":
                pass
            else:
                SQLCommands.dbappend(course, prof)
