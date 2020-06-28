import cx_Freeze
executables = [cx_Freeze.Executable("email sender box.py")]

cx_Freeze.setup(
    name="EMAIL SENDER",
    options={"build_exe": {"packages":["tkinter","smtplib"
                                       ,"email","os"
                                       ,"time","math","functools"],
                            "include_files": ["emailsender.ico"]}},
    executables = executables
    )
