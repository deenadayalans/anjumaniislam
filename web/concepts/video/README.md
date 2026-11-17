# Video slots

Every full-screen section loads the **real drone file first**. If that file doesn't exist yet, it falls back to the sample clip. When the drone footage arrives, drop the files in this folder with these names and they replace the samples automatically. No code changes are needed.

| Slot (drop the real file here) | Used in | Shot we need | Sample used until then |
|---|---|---|---|
| `drone-campus.mp4` | 01 "Breaking through", 02 hero, 03 "Written into the clouds" | Dawn. The drone rises from the misty valley, clears the cloud line and reveals the campus on the plateau. Slow, steady, no cuts. 20–40 s. | `sample-above-clouds.mp4` |
| `drone-ridge.mp4` | 01 "The clouds roll in" band | Late afternoon. A slow lateral glide along the Table Land edge, with the Krishna valley and Dhom dam below. | `sample-ghats-ridge.mp4` |

**Encoding spec:** H.264 MP4, 1920×1080 (deliver 4K masters separately), 24–30 fps, no audio, CRF around 23, `-movflags +faststart`, under 8 MB per loop. Also export a poster frame (`drone-campus-poster.jpg`) and update the `poster=` attributes.

## Sample clip credits (Wikimedia Commons, CC BY 4.0, trimmed and re-encoded)
- `sample-above-clouds.mp4`: "Mawlangren Above the Clouds" by Wann Majaw. Filmed in Meghalaya, not Panchgani. https://commons.wikimedia.org/wiki/File:Mawlangren_Above_the_Clouds.webm
- `sample-ghats-ridge.mp4`: "From the mountain high, the forest stretches like a green ocean…" by Mathanprasath K. Filmed in the Western Ghats. https://commons.wikimedia.org/wiki/File:From_the_mountain_high,_the_forest_stretches_like_a_green_ocean,_kissed_by_mist_and_rain_%E2%80%94_a_silent_breath_of_nature,_and_continue_with_move_on.webm

Neither sample shows Panchgani or the school. They are mood placeholders only and must be replaced before launch.
