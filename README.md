# Laser-Corridor

A laser security grid based kids game using [OpenCV](http://opencv.org/).

## Getting Started
1.  Clone repository
    ``` bash
    git clone https://github.com/mostley/laser-corridor.git
    ```
2. Install dependencies for python (Differs from OS and package manager)
    ``` bash
    pip install numpy
    pip install opencv-python
    ```
3. Import and configure sounds
4. Start game
    ``` bash
    python game.py
    ```

## Sounds
Laser-Corridor requires four .wav files which are located in directory `sounds`. The `soundtrackFile` is played on game start and indicates the playing time, meanwhile `finishSounds` is triggered on game-end-events. 
``` python
self.finishSounds = {
            Finishsounds.success: 'success.wav',
            Finishsounds.failure: 'failure.wav',
            Finishsounds.timeIsUp: 'timeIsUp.wav'
        }
        self.soundtrackFile = 'soundtrack.wav'
```

## Configuration
| Attribute | Description |
| :--- | :--- |
| *game.duration* | An int value that sets the game/soundtrack duration in seconds. |
| *framesource.inputVideo* | The device index or video file name |
| *framesource.minTreshBinary* | An int value between 1 and 254 that sets the threshold for creating binary black/white images |
| *detector.minTreshDetection* | An int value between 1 and 254 that sets the threshold for detecting white blobs |

