#!/usr/bin/env python3
"""
Example usage of the SongEval package.

This script demonstrates how to use the SongEval package to evaluate song quality.
"""

import songeval

def main():
    # Replace with your actual audio file paths
    audio_files = [
        "/home/lxb/Disk_SSD/projects/song_generation/song_transcription/data/9708.clip.wav",
    ]
    
    try:
        # Get evaluator instance (model loaded once and reused)
        evaluator = songeval.get_evaluator()
        
        # Evaluate multiple songs
        results = evaluator.evaluate_songs(audio_files)
        
        print("Evaluation results:")
        for file_id, scores in results.items():
            print(f"\n{file_id}:")
            for dimension, score in scores.items():
                print(f"  {dimension}: {score}")
                
    except Exception as e:
        print(f"Error evaluating songs: {e}")

if __name__ == "__main__":
    main() 