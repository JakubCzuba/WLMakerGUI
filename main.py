import customtkinter
from pathlib import Path
from PIL import Image
import winreg

app = customtkinter.CTk()
app.title("WL-Maker GUI")
app.geometry("1100x800")
customtkinter.set_appearance_mode("dark")

framestart = customtkinter.CTkFrame(
    app, 
    fg_color="#0a0b0e"
)
framemenu = customtkinter.CTkFrame(
    app, 
    fg_color="#0a0b0e"
)

framecreatewl = customtkinter.CTkFrame(
    framemenu,
    fg_color="#0a0b0e",
    border_color="#ff004b",
    border_width=2,
    height=80,
    width=355,
    corner_radius=55,
)

framecreatewl.place(
    relx=0.5, 
    rely=0.15, 
    anchor="center",
    
)

framestart.pack(
    fill="both", 
    expand=True
)

def button_callback():
    framestart.pack_forget()
    framemenu.pack(
        fill="both", 
        expand=True
        )

buttonstart = customtkinter.CTkButton(
    framestart,
    text="Utwórz zestawienie WL",
    width=100,
    height=80,
    corner_radius=50,
    border_color="#ff004b",
    border_width=2,
    fg_color="#101116",
    command=button_callback,
    font=("Arial", 20),
    text_color="#fffc58"
)
buttonstart.place(
    relx=0.5, 
    rely=0.4, 
    anchor="center", 
)

buttonexit=customtkinter.CTkButton(
    framestart,
    text="Jebać to, ide do domu.",
    width=100,
    height=80,
    corner_radius=50,
    border_color="#ff004b",
    border_width=2,
    fg_color="#101116",
    command=app.destroy,
    font=("Arial", 20),
    text_color="#fffc58"    
)
buttonexit.place(
    relx=0.5,
    rely=0.6,
    anchor="center"
)

def backarrow_callback():
    framemenu.pack_forget()
    framestart.pack(
        fill="both",
        expand=True
    )

backarrowpath=Path(__file__).resolve().parent/"reply.png"

backarrowpng=customtkinter.CTkImage(
    light_image=Image.open(backarrowpath),
    size=(50,50)
)

backarrow = customtkinter.CTkButton(
    framemenu,
    width=60,
    height=60,
    corner_radius=100,
    border_color="#ff004b",
    fg_color="#101116",
    border_width=2,
    image=backarrowpng,
    command=backarrow_callback,
    text=""
)

backarrow.place(
    relx=0.1,
    rely=0.15,
    anchor="center"
)

labelmenu = customtkinter.CTkLabel(
    framecreatewl, 
    text="Wybierz pliczek i baw sie dobrze przyjacielu", 
    justify="center", 
    font=("Arial", 20), 
    corner_radius=0,
    text_color="#fffc58",
    fg_color="transparent",
    bg_color="transparent",
    height=80,
    width=350,
)
labelmenu.pack(
    padx=35,
    pady=10,
)

filelist = customtkinter.CTkScrollableFrame(
    framemenu,
    width=800,
    height=400,
    scrollbar_button_color="#025b37",
    fg_color="#101116",
    border_color="#6766b3",
    border_width=2
)
filelist.place(
    anchor="center",
    relx=0.5,
    rely=0.5
)

with winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
) as klucz:
    desktoppath, _ = winreg.QueryValueEx(klucz, "Desktop")

desktop = Path(winreg.ExpandEnvironmentStrings(desktoppath))

pathfiles = desktop / "WLMaker"

def filesrefresh():
    for widget in filelist.winfo_children():
        widget.destroy()

    if not pathfiles.is_dir():
        showcomment(
            "Sorry bratku ale pojebałeś ścieżki,\n nie ma folderu WLMaker na pulpicie.\n Weź go sobie utwórz bo inaczej nie będzie działać, sorcia."
        )
        return

    excelfiles = []

    for itemfile in pathfiles.iterdir():
        if (
            itemfile.is_file()
            and itemfile.suffix.lower() in (".xlsx", ".xls", ".xlsm")
            and not itemfile.name.startswith("~$")
        ):
            excelfiles.append(itemfile)

    if not excelfiles:
        showcomment(
            "Mordzia ale z czego ja mam tu generowac zestawienia?\n Nie dodałeś żadnego pliku excwela do folderu WLMaker,\n zrób to szybciutko bo inaczej nie popracujemy."
        )
        return

    for itemfile in excelfiles:
        filename = customtkinter.CTkButton(
            filelist,
            text=itemfile.name,
            font=("Arial", 20),
            corner_radius=50,
            text_color="#02ffa4",
            fg_color="#060608",
            border_color="#00b0ff",
            border_width=2
        )
        filename.pack(anchor="w", padx=10, pady=10)


def showcomment(tekst):
    errorcomment = customtkinter.CTkFrame(
        filelist,
        fg_color="#060608",
        corner_radius=25
    )
    errorcomment.pack(padx=10, pady=150)

    showerroe = customtkinter.CTkLabel(
        errorcomment,
        text=tekst,
        font=("Arial", 20),
        text_color="#02ffa4",
        fg_color="transparent",
        corner_radius=0,
        justify="center",
        wraplength=600
    )
    showerroe.pack(padx=35, pady=20)


buttonrefresh = customtkinter.CTkButton(
    framemenu,
    text="Odśwież",
    font=("Arial", 20),
    fg_color="#101116",
    text_color="#fffc58",
    border_color="#ff004b",
    border_width=2,
    corner_radius=20,
    command=filesrefresh
)
buttonrefresh.place(
    relx=0.5,
    rely=0.85,
    anchor="center"
)

filesrefresh()

app.mainloop()