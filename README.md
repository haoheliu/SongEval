# 🎵 SongEval: A Benchmark Dataset for Song Aesthetics Evaluation

[![Hugging Face Dataset](https://img.shields.io/badge/HuggingFace-Dataset-blue)](https://huggingface.co/datasets/ASLP-lab/SongEval)
[![Arxiv Paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/pdf/2505.10793)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)  


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
- 📦 **Installable Python package** for easy integration

---

## 📦 Installation

### Option 1: Install as Python Package (Recommended)

Install the package in development mode:

```bash
git clone https://github.com/ASLP-lab/SongEval.git
cd SongEval
pip install -e .
```

### Option 2: Manual Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ASLP-lab/SongEval.git
cd SongEval
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Using the Python Package

```python
import songeval

# Evaluate a single song (model loaded automatically on first use)
scores = songeval.evaluate_song("path/to/your/song.wav")
print(scores)
# Output: {'Coherence': 3.2456, 'Musicality': 3.1234, 'Memorability': 2.9876, 'Clarity': 3.4567, 'Naturalness': 3.1111}

# Evaluate multiple songs efficiently (model loaded once and reused)
evaluator = songeval.get_evaluator()
results = evaluator.evaluate_songs(["song1.wav", "song2.mp3", "song3.wav"])
print(results)

# Force CPU mode if needed
scores = songeval.evaluate_song("path/to/song.wav", use_cpu=True)
```

### Using Command Line Interface

- Evaluate a single audio file:

```bash
songeval -i /path/to/audio.mp3 -o /path/to/output
```

- Evaluate a list of audio files:

```bash
songeval -i /path/to/audio_list.txt -o /path/to/output
```

- Evaluate all audio files in a directory:

```bash
songeval -i /path/to/audio_directory -o /path/to/output
```

- Force evaluation on CPU (⚠️ CPU evaluation may be significantly slower):

```bash
songeval -i /path/to/audio.wav -o /path/to/output --use_cpu
```

### Using the Original Script

```bash
python eval.py -i /path/to/audio.mp3 -o /path/to/output
```

---

## 📚 API Reference

### `songeval.evaluate_song(audio_path, use_cpu=False)`

Evaluate a single song file efficiently.

**Parameters:**
- `audio_path` (str): Path to the audio file (.wav or .mp3)
- `use_cpu` (bool): Force CPU mode even if GPU is available

**Returns:**
- `dict`: Dictionary with scores for each dimension:
  - 'Coherence': Overall Coherence score
  - 'Musicality': Overall Musicality score  
  - 'Memorability': Memorability score
  - 'Clarity': Clarity of Song Structure score
  - 'Naturalness': Naturalness of Vocal Breathing and Phrasing score

### `songeval.get_evaluator(use_cpu=False)`

Get a global evaluator instance. The model is loaded only once and reused.

**Parameters:**
- `use_cpu` (bool): Force CPU mode even if GPU is available

**Returns:**
- `SongEvaluator`: The evaluator instance

### `SongEvaluator.evaluate_songs(audio_paths)`

Evaluate multiple song files efficiently.

**Parameters:**
- `audio_paths` (list): List of paths to audio files

**Returns:**
- `dict`: Dictionary mapping file IDs to their scores

---

## 🙏 Acknowledgement
This project is mainly organized by the audio, speech and language processing lab [(ASLP@NPU)](http://www.npu-aslp.org/).

We sincerely thank the **Shanghai Conservatory of Music** for their expert guidance on music theory, aesthetics, and annotation design.
Meanwhile, we thank AISHELL to help with the orgnization of the song annotations.

<p align="center"> <img src="assets/logo.png" alt="Shanghai Conservatory of Music Logo"/> </p>

## 📑 License
This project is released under the CC BY-NC-SA 4.0 license. 

You are free to use, modify, and build upon it for non-commercial purposes, with attribution.

## 📚 Citation
If you use this toolkit or the SongEval dataset, please cite the following:
```
@article{yao2025songeval,
  title   = {SongEval: A Benchmark Dataset for Song Aesthetics Evaluation},
  author  = {Yao, Jixun and Ma, Guobin and Xue, Huixin and Chen, Huakang and Hao, Chunbo and Jiang, Yuepeng and Liu, Haohe and Yuan, Ruibin and Xu, Jin and Xue, Wei and others},
  journal = {arXiv preprint arXiv:2505.10793},
  year={2025}
}

```
