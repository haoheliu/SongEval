# 🎵 SongEval: Aesthetic Evaluation Toolkit for Complete Songs

This repository provides a **trained aesthetic evaluation toolkit** based on [SongEval](https://huggingface.co/datasets/ASLP-lab/SongEval), the first large-scale, open-source dataset for human-perceived song aesthetics. The toolkit enables **automatic scoring of generated music** across five perceptual dimensions aligned with professional musician judgments.

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
- 🎧 Accepts **complete songs** (vocals + accompaniment) as input
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