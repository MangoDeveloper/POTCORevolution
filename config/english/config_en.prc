# Window:
window-title Pirates Online Revolution [Pre-Alpha]
win-size 800 600

# Audio:
audio-library-name p3openal_audio

# Resource settings
model-path resources/
model-path resources/phase_2
model-path resources/phase_3
model-path resources/phase_4
model-path resources/phase_5
default-model-extension .bam

# DClass:
dc-file astron/dclass/pirates.dc
dc-file astron/dclass/otp.dc

# Performance:
smooth-lag 0.4
heartbeat-interval 5
threaded-net #t
support-threads #t
lock-to-one-cpu #f
lock-to-one-core #f
deferred-generate-interval 0.0
texture-anisotropic-degree 16
compressed-textures 0

# PlayToken:
fake-playtoken Skipps

# Developer options:
want-dev #f
want-pstats 0

# Game Options:
loading-screen 0

notify-level-gobj warning
notify-level-loader warning
notify-level-Entity debug
notify-level-DistributedEntity debug
notify-level-Level debug
notify-level-DistributedLevel debug

server-port 6667
server-version sv-1.0.0

want-hotkeys #f
