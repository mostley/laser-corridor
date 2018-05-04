# Laser-Corridor

A laser security grid based kids game using [OpenCV](http://opencv.org/).

## Getting Started
1.  Clone repository
    ``` bash
    git clone https://github.com/mostley/laser-corridor.git
    ```
2. Install dependencies for python
    ``` bash
    pip install opencv-python
    pip install numpy
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
| Attribute | Default Value | Description |
| :--- | :--- | :--- |
| *game.duration* | `30` | An int value that sets the game/soundtrack duration in seconds. |
| *framesource.capture* | `cv2.VideoCapture(0)` | An object that captures a video with the device index or video file name as parameter.|
