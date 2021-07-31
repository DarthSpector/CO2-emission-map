Sectors=[ 'E-11','E-9', 'E-8', 'E-7',
'F-5','F-6','F-7','F-8','F-10','F-11',
'G-5','G-6','G-7', 'G-8', 'G-9', 'G-10', 'G-11','G-13', 'G-14',
'H-8','H-9','H-10','H-11', 'H-12',
'I-8','I-9','I-10','I-11' ]
                 #E-11,E-9, E-8,E-7,F-5,F-6,F-7,F-8,F-10,F-11,  G-5,G-6,G-7,G-8,G-9 G-10,G-11,G-13,G-14, H-8,H-9,H-10,H-11,H-12, I-8,I-9,I-10,I-11          
start_x_pixels = [290, 515, 590,680,872,767,670,575, 378, 288  ,875,767,670,575,472,378, 288,88,   4  , 575,472, 378, 284, 187, 575,472, 378, 285] 
end_x_pixels =   [370, 570, 665,715,880,855,758,663, 465, 370  ,878,855,758,663,565,465, 370,175,  83 , 663,565, 465, 371, 275, 663,565, 465, 371]
start_y_pixels = [95,  123, 150,170,230,190,190,190, 190, 190  ,320,285,285,285,285,285, 285,285,  285, 375,375, 375, 375, 375, 480,480, 480, 480]
end_y_pixels =   [180, 160, 182,180,250,275,275,275, 275, 275  ,330,365,365,365,365,365, 365,365,  365, 471,468, 468, 468, 468, 565,565, 565, 565]

sorted_x_start_array = [' ' for i in range(len(start_x_pixels))]
sorted_x_end_array = [' ' for i in range(len(end_x_pixels))]
sorted_y_start_array = [' ' for i in range(len(start_y_pixels))]
sorted_y_end_array = [' ' for i in range(len(end_y_pixels))]

sorted_sector_array = [' ' for i in range(len(Sectors))]

colours = ["#7CA928", "#95B121", "#AEB91A", "#C6C013", "#E3B61C", "#EFB420", "#FAB123", "#FAAA15", "#FAA322",   
                "#FAA307", "#F79807", "#F48C06", "#F18106","#EE7505","#EB6905", "#E85D04", "#E55204", "#E24603","#DA3B03",
                "#D22F03", "#C52A05", "#B82506","#9E1A09","#960E08","#8D0207","#7C030B","#73040D", "#6A040F"]
    
global name

global data

def screenshot(sector, d):

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    options.add_argument("--window-size=1920x1080")
    from time import sleep
    import os

    WebDriverWait(d,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(sector + ", Islamabad")
    Submit = d.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Submit.click()
            
    # if sector != "G-5" and sector != "E-7" and sector != "E-8" and sector != "E-9" and sector != "F-6": 
    #     sleep(2)
    #     Zoom= d.find_element_by_class_name("ujtHqf-zoom-icon")
    #     Zoom.click()
        
    d.fullscreen_window()
    

    global name
    name = sector + '.png'
    print(name)
    
    # myScreenshot = pyautogui.screenshot()
    FILE_PATH = "D:\enviro-data-main\screenshots"
    FILE_NAME = sector+".png"
    FILE_INFO = os.path.join(FILE_PATH, FILE_NAME) 
    sleep(5)
    d.get_screenshot_as_file(FILE_INFO)
    WebDriverWait(d,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(Keys.CONTROL + "A")
    WebDriverWait(d,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(Keys.BACK_SPACE)
    # myScreenshot.save(FILE_INFO)
    
    # print("end...")
   

def image_annalyser(sctr): 
    green,orange,red,black=0,0,0,0
    from PIL import Image
    import os
    FILE_PATH = "D:\enviro-data-main\screenshots"
    FILE_NAME = sctr +".png"
    FILE_INFO = os.path.join(FILE_PATH, FILE_NAME)

    im = Image.open(FILE_INFO, 'r')
    print(im)

    pixel_values = list(im.getdata())
    for i in  pixel_values:  #color has multiple values with small variance, add black color
        if i==(99,214,104,255) or i==(93, 201, 97) or i== (204, 230, 205) or i== (160, 218, 163):
            green+=1
        elif i == (255,151,77,255) or i==(255, 151, 77)or i==(238, 178, 136):
            orange+=1
        elif i==(242, 77, 68) or i == (242,60,50,255) or i== (227, 77, 69) or i==(229, 97, 90):
            red+=1  
        elif i ==(129,31,31,255) or i==(129, 31, 32) or i==(183, 127, 127):
            black+=1 

    return green,red,orange,black

def emmisions_calculations(g,o,r,b):
    formula= (555/700)
    emmisions=((g*formula*0.5)+(o*formula*0.7)+(r*formula*0.8)+(b*formula*0.96))*0.525
    emmisions=int(emmisions)
    return str(emmisions)



def clean_up(sctr):
    import os
    FILE_PATH = "D:\enviro-data-main\screenshots"
    FILE_NAME = sctr+".png"
    FILE_INFO = os.path.join(FILE_PATH, FILE_NAME)
    os.remove(FILE_INFO)
    print("File Removed!")


    
def send_to_website(data):
    
    starting_html='''
     
     <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
            <meta name = "viewport" content="width=device-width, initial-scale=1">
            <title>Enviro Data</title>
            <link rel="stylesheet" href="Website.css">
    </head>
    <body>
        <header id="main-header">
            <div class="main-container">
                <h1>
                    CO<sub>2</sub> Emissions in Islamabad
                    <img src="images/HeadingImage.jpeg" alt="">
                </h1>
            </div>
        </header>

        <nav id="navbar">
            <div class="container">
                <ul>
                    <li><a href="data.html" > Home</a></li>
                    <li><a href="About.html" > About</a></li>
                    <li><a href="Team.html" > The Team</a></li>
                
                </ul>
            </div>
        </nav>
        <div class="container">
            <section id="image-showcase">
                
                <div class="chart-container">
                    
                    <img src="images/ all.png" id='chart-showcase'>
                    <img src="images/ E.png" id='chart-showcase'>
                    <img src="images/ F.png"id='chart-showcase'>
                    <img src="images/ G.png" id='chart-showcase'>
                    <img src="images/ H.png" id='chart-showcase'>
                    <img src="images/ I.png"id='chart-showcase'>
           
                </div>
                <!-- <div class="container">
                </div> -->
            </section>
            <!-- <section id = "chart-showcase"> -->
            
            <aside id="text-showcase">
                <div class="container"></div>
                <table>    
                        <th>
                            Sector Emissions per Hour
                        </th>
    '''
    ending_html= '''   
                    </table>  
                </div>
                <!-- <section class="chart-container">     -->
                
       <!-- </section> -->
            </aside>
            
        </div>
        
       <footer id="main-footer">
           <p>Copyright &copy;2021 FORI Interns</p>
       </footer>
    </body>
    </html>
    '''
    
    f = open('D:\enviro-data-main\Website\data.html', "w")
    f.write(starting_html + data + ending_html)
    f.close() 
    #send txt file to website

subsectors=[4,6,9,5,4]
sector_emmisions=[]
main_sectors = ['E','F','G','H','I']
startc=[0,4,10,19,24]
endc=[4,10,19,24,28]

def pie_chart(emmisions):
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib as mpl
    end=False
    i=0
    while end==False: 
        total=0
        for j in range(subsectors[i]):
            total+=emmisions[i]
        sector_emmisions.append(total)    
        i+=1
        if i==5:
            end=True

    mpl.rcParams['font.size'] = 16
    plt.figure(5)
    plt.title('Emmisons per Sectors')
    plt.pie(np.array(sector_emmisions), labels = main_sectors)
    plt.legend(title = "Sectors:",bbox_to_anchor=(1,1))
    plt.savefig('D:\enviro-data-main\Website\images\ ' +'all.png')
    for i in range(0,5):
        plt.figure(i)
        mpl.rcParams['font.size'] = 18
        plt.title(main_sectors[i] + ' - Sectors')
        y = np.array(emmisions[startc[i]:endc[i]])
        plt.pie(y, labels =Sectors[startc[i]:endc[i]])
        plt.savefig('D:\enviro-data-main\Website\images\ ' +main_sectors[i] +'.png')

def duplicate_check(emissions):
    for i in range(len(emissions)):
        emissions[i] = int(emissions[i])
    # print("emissions before check: "+str(emissions))
    
    for i in range(len(emissions)):
        comparable = emissions[i]
        for j in range(len(emissions)):
            if i != j:
                if emissions[j] == comparable:
                    emissions[j] += 1
    # print("emissions after check: " + str(emissions))
    return emissions
    
def sorting(unsorted_emissions, sorted_emissions):
    for emission_num in range(28):
        for sorted_num in range(28):
            if sorted_emissions[sorted_num] == unsorted_emissions[emission_num]:        
                sorted_sector_array[sorted_num] = Sectors[emission_num]
                sorted_x_start_array[sorted_num] = start_x_pixels[emission_num]
                sorted_x_end_array[sorted_num] = end_x_pixels[emission_num]
                sorted_y_start_array[sorted_num] = start_y_pixels[emission_num]
                sorted_y_end_array[sorted_num] = end_y_pixels[emission_num]
               
    print("Sorted emissions are: " + str(sorted_emissions))
    print("Sorted sectors are: " + str(sorted_sector_array))

    print("Sorted start x pixels are: " + str(sorted_x_start_array))
    print("Sorted end x pixels are: " + str(sorted_x_end_array))
    print("Sorted start y pixels are: " + str(sorted_y_start_array))
    print("Sorted end y pixels are: " + str(sorted_y_end_array))
    
    return sorted_sector_array, sorted_x_start_array, sorted_x_end_array, sorted_y_start_array, sorted_y_end_array

def process():
    data=''
    Emissions = []

    from selenium import webdriver
    from time import sleep
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.options import Options

    import numpy as np
    from PIL import Image  
    import os
    
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw 

    op = Options()
    op.headless = True
    driver = webdriver.Firefox(firefox_options=op, executable_path=GeckoDriverManager().install())
    driver.get("https://www.google.com/maps/@33.6972788,72.9780491,14.31z/data=!5m1!1e1")

    sleep(1)
    for sector in Sectors:
        screenshot(sector, driver)
        green,orange,red,black= image_annalyser(sector)
        emission_for_sector = emmisions_calculations(green,orange,red,black)
        Emissions.append(emission_for_sector)
        #clean_up(sector)
    
    unsorted_emissions = duplicate_check(Emissions)
    sorted_emissions = np.sort(Emissions) 

    sorted_sector_array, sorted_x_start_array, sorted_x_end_array, sorted_y_start_array, sorted_y_end_array = sorting(unsorted_emissions, sorted_emissions) 

    for i in range(len(Emissions)):
        j = 27 - i
        data = data + '<tr><th>' + str(sorted_sector_array[j]) + ': '+ str(sorted_emissions[j]) + ' kg/hour </th></tr>\n'
        send_to_website(data)

    FILE_PATH = "D:\enviro-data-main\Website\images"
    path = os.path.join(FILE_PATH, "Map.png")     
    # Open image
    im = Image.open(path)
    draw = ImageDraw.Draw(im)
    from colormap import hex2rgb
    font_path = "D:\enviro-data-main\Fonts"
    font_path =  os.path.join(font_path, "anonoma-mono-less-characters.ttf")
    font = ImageFont.truetype(font_path, 18)

    for i in range(len(colours)):
        rgb_color = hex2rgb(colours[i])
        if sorted_sector_array[i] == 'E-9':
            x = 515
            x_limit_triangle = x + 5
            for y in range(100, 123):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), (rgb_color))
                    x+=1

                x_limit_triangle += 3
                x = 515


            for y in range(123, 160):
                for x in range(515, 570):
                    im.putpixel((x, y), rgb_color)

            SECTOR_WIDTH = 66
            x_initial = 520
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(123, 182):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), rgb_color)
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.3


        elif sorted_sector_array[i] == 'E-8':
            E_8_start_x = 593
            turn = 0
            x = E_8_start_x
            x_limit_triangle = x + 5
            for y in range(127, 150):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), rgb_color)
                    x+=1
                turn += 0.3
                x_limit_triangle += 3
                x = E_8_start_x - int(turn) 
            
            E_8_start_x = 593
            turn = 0
            x = E_8_start_x
            x_limit_triangle = x
            for y in range(127, 182):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), rgb_color)
                    x+=1
                turn += 0.3
                x = E_8_start_x - int(turn)     
                SECTOR_WIDTH = 75
                x_initial = 590
                x_limit_parlogram = x_initial + SECTOR_WIDTH

            for y in range(150, 182):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), rgb_color)
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0
    
        elif sorted_sector_array[i] == 'E-7':        
            x = 672
            x_limit_triangle = x + 5
            for y in range(153, 182):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), rgb_color)
                    x+=1

                x_limit_triangle += 3
                x = 672
        
        elif sorted_sector_array[i] == 'G-5':
            for x in range(860, 893):
                for y in range(297, 367):
                    im.putpixel((x, y), (rgb_color))
            for x in range(860, 885):
                for y in range(284, 297):
                    im.putpixel((x, y), (rgb_color))
            x = 885
            x_limit_triangle = x + 3
            for y in range(284, 299):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), (rgb_color))
                    x+=1

                x_limit_triangle += 0.3
                x = 885
        elif sorted_sector_array[i] == 'F-6':
            SECTOR_WIDTH = 28
            x_initial = 847
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(190, 240):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), (rgb_color))
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.5

        elif sorted_sector_array[i] == 'F-5':
            x = 883
            x_limit_triangle = x + 5
            for y in range(190, 198):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), ((rgb_color)))
                    x+=1

                x_limit_triangle += 4
                x = 883
        
            SECTOR_WIDTH = 32
            x_initial = 884
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(198, 239):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), ((rgb_color)))
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.6

            SECTOR_WIDTH = 20
            x_initial = 882
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(193, 211):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), ((rgb_color)))
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.7

            SECTOR_WIDTH = 20
            x_initial = 861
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(230, 275):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), ((rgb_color)))
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0

            SECTOR_WIDTH = 25
            x_initial = 870
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(210, 225):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), ((rgb_color)))
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.5

            SECTOR_WIDTH = 20
            x_initial = 871
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(210, 232):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), ((rgb_color)))
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.5

            for x in range(870, 892):
                for y in range(210, 264):
                    im.putpixel((x, y), ((rgb_color)))

            SECTOR_WIDTH = 10
            x_initial = 882
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(262, 275):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), ((rgb_color)))
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.5
            


        for x in range(sorted_x_start_array[i], sorted_x_end_array[i]):
            for y in range(sorted_y_start_array[i], sorted_y_end_array[i]):
                im.putpixel((x,y), (rgb_color))

        
        middle_x = sorted_x_start_array[i] + (sorted_x_end_array[i] - sorted_x_start_array[i])//2 - 16
        middle_y = sorted_y_start_array[i] + (sorted_y_end_array[i] - sorted_y_start_array[i])//2 - 16
        draw.text((middle_x, middle_y), sorted_sector_array[i], (255,255,255), font = font)

    driver.quit()
    im.show()
    result = os.path.join(FILE_PATH, "result.png")
    im.save(result)
    pie_chart(unsorted_emissions)


# import time
# epoch_time = int(time.time())
# print(epoch_time)
process()