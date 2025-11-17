import threading
import time
import webbrowser
import logging
from flask import Flask, send_from_directory

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

current_gif = ""
current_audio = ""

audio_files = {
    "PeggleJazz": "PeggleJazz.mp3",
    "PeggleMarch": "PeggleMarch.mp3",
    "PeggleSynth": "PeggleSynth.mp3",
    "Lapis": "LapisPhilosophorum.mp3",
    "Save": "CharmlessMan.mp3"
}

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>ENTERPOTATO DISPLAY</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background-color: black;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            img {
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
            }
            #audioPlayer {
                display: none;
            }
        </style>
        <script>
            let currentGif = '';
            let currentAudio = '';
            
            function updateGif() {
                if (currentGif) {
                    document.getElementById('gif').src = '/bg/' + currentGif;
                }
            }
            
            function updateAudio() {
                const audioPlayer = document.getElementById('audioPlayer');
                if (currentAudio) {
                    audioPlayer.src = '/audio/' + currentAudio;
                    audioPlayer.loop = true;
                    audioPlayer.play().catch(e => console.log('Audio play failed:', e));
                } else {
                    audioPlayer.pause();
                    audioPlayer.src = '';
                }
            }
            
            function checkForUpdates() {
                fetch('/current_gif')
                    .then(response => response.text())
                    .then(gifName => {
                        if (gifName !== currentGif) {
                            currentGif = gifName;
                            updateGif();
                        }
                    })
                    .catch(e => console.log('GIF fetch error:', e));
                    
                fetch('/current_audio')
                    .then(response => response.text())
                    .then(audioName => {
                        if (audioName !== currentAudio) {
                            currentAudio = audioName;
                            updateAudio();
                        }
                    })
                    .catch(e => console.log('Audio fetch error:', e));
            }
            checkForUpdates();
            let intervalCount = 0;
            const fastInterval = setInterval(() => {
                checkForUpdates();
                intervalCount++;
                if (intervalCount > 5) {
                    clearInterval(fastInterval);
                    setInterval(checkForUpdates, 2000);
                }
            }, 300);
        </script>
    </head>
    <body>
        <img id="gif" src="" style="display: none;" onload="this.style.display='block';">
        <audio id="audioPlayer"></audio>
    </body>
    </html>
    '''

@app.route('/current_gif')
def get_current_gif():
    return current_gif

@app.route('/current_audio')
def get_current_audio():
    return current_audio

@app.route('/bg/<path:filename>')
def serve_gif(filename):
    return send_from_directory('BG', filename)

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('Mus', filename)

def start_server():
    app.run(host='0.0.0.0', port=5000, use_reloader=False, debug=False)

def background(gif_name):
    global current_gif
    current_gif = gif_name

def playAudio(track_name):
    global current_audio
    current_audio = audio_files[track_name]

def stopAudio():
    global current_audio
    current_audio = ""

server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

time.sleep(2)
webbrowser.open('http://localhost:5000')
background('yakuza-goro.gif')
playAudio('Lapis')

def main():
    x = int(input("?"))
    if x == 2:
        time.sleep(3)
        background('v1-ballin.gif')
        playAudio('PeggleJazz')

main()