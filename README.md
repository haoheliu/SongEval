# 🎵 SongEval: A Benchmark Dataset for Song Aesthetics Evaluation

This repository provides a **trained aesthetic evaluation toolkit** based on [SongEval](https://huggingface.co/datasets/ASLP-lab/SongEval), the first large-scale, open-source dataset for human-perceived song aesthetics. The toolkit enables **automatic scoring of generated song** across five perceptual aesthetic dimensions aligned with professional musician judgments.

---

## 🌟 Key Features

- 🧠 **Pretrained neural models** for perceptual aesthetic evaluation
- 🎼 Predicts **five aesthetic dimensions**:
  - Overall Coherence
  - Memorability
  - Naturalness of Vocal Breathing and Phrasing
  - Clarity of Song Structure
  - Overall Musicality
<!-- - 🧪 Supports **batch evaluation** for model benchmarking -->
- 🎧 Accepts **full-length songs** (vocals + accompaniment) as input
- ⚙️ Simple inference interface

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ASLP-lab/SongEval.git
cd SongEval
pip install -r requirements.txt
```

## 🚀 Quick Start

- Evaluate a single audio file:

```bash
python eval.py -i /path/to/audio.mp3 -o /path/to/output
```

- Evaluate a list of audio files:

```bash
python eval.py -i /path/to/audio_list.txt -o /path/to/output
```

- Evaluate all audio files in a directory:

```bash
python eval.py -i /path/to/audio_directory -o /path/to/output
```

- Force evaluation on CPU  (⚠️ CPU evaluation may be significantly slower) :


```bash
python eval.py -i /path/to/audio.wav -o /path/to/output --use_cpu
```


## 🙏 Acknowledgement

We sincerely thank the **Shanghai Conservatory of Music** for their expert guidance on music theory, aesthetics, and annotation design.
<p align="center"> <img src="assets/sy_logo.jpg" alt="Shanghai Conservatory of Music Logo" width="200"/> </p>

## 📑 License
This project is released under the CC BY-NC-SA 4.0 license. 

You are free to use, modify, and build upon it for non-commercial purposes, with attribution.

## 📚 Citation
If you use this toolkit or the SongEval dataset, please cite the following:
```
@inproceedings{SongEval,
  title     = {SongEval: A Large-Scale Benchmark Dataset for Aesthetic Evaluation of Complete Songs},
  author    = {...},
  booktitle = {...},
  year      = {2025}
}

```