
# Hello Git

Our project is a Keylogger designed to capture and log keystrokes typed by the user on the target system. The keylogger operates in the background and records all key inputs, which are then automatically sent to a designated email address for monitoring or analysis.

## Authors

- [@Navaneethakrishnan2004](https://github.com/Navaneethakrishnan2004)
- [@Sreeaswinrajha](https://github.com/sreeaswinrajha)
- [@sophiyasophi](https://github.com/sophiyasophi)
- [@Ranjana1812](https://github.com/Ranjana1812)


## Deployment

To deploy this project run

```bash
  git clone https://github.com/Navaneethakrishnan2004/Advance-Key-Logger.git
```
Run on terminal or vs code or any Python environment
```bash
  python logger.py
```
```bash
  python Keylogger.py
```
## Steps
1. install Dependencies: Make sure you have the necessary libraries installed.
2. Modify the Code for Background Execution: By default, PyInstaller can hide the console window when running an executable by using the --noconsole option. This prevents the terminal from appearing when the file is executed.
3. Create an verbose file so that we can avoid opening the terminal and can run the exe file as an normal file (we want to give the location of where we store the logger.exe file)
4. The created file will be stored in boot folder
5. Then it will send alert if the keyword stored in it is entered

## Features

- Word detection: The keylogger scans the recorded keystrokes in real-time to detect a specific target word (e.g., "password"). 
- Email alert system: If the target word is detected in the log, an email alert is automatically sent to a predefined email address, notifying the recipient that the word has been entered.
- Silent operation: The keylogger runs silently in the background, without displaying a terminal or console window, ensuring that the user is not aware of its presence.
- Local logging: In addition to email alerts, the keylogger can store logs locally in a text file for later retrieval and analysis
- Easily customizable: The keylogger can be easily modified to include additional features, such as logging mouse movements, screenshots, or more advanced data exfiltration techniques.
- Multi-threaded: Uses multithreading for periodic reporting, ensuring smooth execution without affecting system performance.


## Feedback

If you have any feedback, please reach out to us at navaneethakrishnanps2021ai@gmail.com or sreeaswinrajhar@gmail.com




