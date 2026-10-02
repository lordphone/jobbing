# Projects & Leadership

Usually 1–2 lines at the bottom. ECE fellow is leadership; the other two are projects.

## ld-ece-fellow

tags: leadership
facts:
- ECE Leadership & Engagement Fellow
- CMU
- Aug 2026 -- present
- owns budgeting, marketing, and outreach for ECE student programs
- company-sponsored hackathons, alumni events, tech event outings
approved:
- default: **ECE Leadership & Engagement Fellow** (CMU, Aug 2026 -- present): Own budgeting, marketing, and outreach for ECE student programs — company-sponsored hackathons, alumni events, and tech event outings.

## pj-my-av

tags: ml, systems
facts:
- https://github.com/lordphone/my-av
- PyTorch CNN-GRU
- real-time prediction of steering angle and speed
- from 20-frame (1s) video
- 33 hours of Comma2k19
- data pipeline: shuffling, temporal windowing, 240×320 frame processing
- trained on local CUDA and GCP Vertex AI
- streaming inference
approved:
- default: **my-av:** Built a CNN-GRU model that predicts steering angle and speed from 20-frame (1s) video; processed 33 hours of Comma2k19 footage and ran streaming inference on local CUDA and GCP Vertex AI.
- short: **my-av:** Built a CNN-GRU that predicts steering and speed from 1s video; trained on 33 hours of Comma2k19 on local CUDA and GCP Vertex AI.
- pipeline: **my-av:** Developed a PyTorch CNN-GRU for real-time steering-angle and speed prediction from 20-frame (1s) video; built a data pipeline over 33 hours of Comma2k19 with shuffling, temporal windowing, and 240×320 frame processing.
- training: **my-av:** Trained locally and on GCP Vertex AI and implemented streaming inference for autonomous driving.

`pipeline` and `training` are two bullets. Use both only when this project gets two lines.

## pj-wisconsin-autonomous

tags: systems, embedded
facts:
- Wisconsin Autonomous, Vehicle Integration
- integrated wheel-speed encoders on the competition rover
- voltage-to-frequency converters
- streamed / transmitted real-time data to the onboard NVIDIA Jetson
note: source paste was cut off after "transmitting real-time data to"; Jetson is from the current resumes.
approved:
- default: **Wisconsin Autonomous:** Integrated wheel-speed encoders on the competition rover and streamed real-time data to the onboard NVIDIA Jetson.
- encoders: **Wisconsin Autonomous:** Integrated wheel-speed encoders with voltage-to-frequency converters and streamed real-time data to the onboard NVIDIA Jetson.

## pj-codingplans

tags: llm, fullstack
facts:
- codingplans: website informing the public which LLM coding/token plans are trustworthy and worth the money
- bought plans out of pocket from companies including Z.AI, MiniMax, and Kimi
- task-specific tests: KV cache, long context, needle-in-a-haystack
- results show which providers nerfed caching or heavily quantized their models (cost-saving measures against users' interests)
- motivation: understand token cost without subsidization; keep providers in check as plans get more expensive
note: dates, stack, and URL not given yet.
approved:
- default: **codingplans:** Building a website that rates LLM coding/token plans; bought plans from Z.AI, MiniMax, and Kimi and tested KV caching, long context, and needle-in-a-haystack to show which providers nerfed caching or heavily quantized their models.

## pj-badminton-courts

tags: llm, personal
facts:
- personal tool built with AI coding tools
- he hosts a group of CMU badminton players every weekend
- manages everybody's usernames and passwords so the group can guarantee it has courts to play on
note: for written answers; not printed on resumes yet. Stack and dates not given.
