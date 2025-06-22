import argparse
import json
import os
import glob
from .evaluator import SongEvaluator


def main():
    """Command-line interface for SongEval."""
    parser = argparse.ArgumentParser(
        description="SongEval: A trained aesthetic evaluation toolkit for song quality assessment"
    )
    parser.add_argument(
        "-i", "--input_path",
        type=str,
        required=True,
        help="Input audio: path to a single file, a text file listing audio paths, or a directory of audio files."
    )
    parser.add_argument(
        "-o", "--output_dir",
        type=str,
        required=True,
        help="Output directory for generated results (will be created if it doesn't exist)."
    )
    parser.add_argument(
        "--use_cpu",
        action="store_true",
        help="Force CPU mode even if a GPU is available."
    )
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Initialize evaluator
    evaluator = SongEvaluator(use_cpu=args.use_cpu)
    
    # Determine input files
    if os.path.isfile(args.input_path):
        if args.input_path.endswith(('.wav', '.mp3')):
            input_files = [args.input_path]
        else:
            # Assume it's a text file with paths
            with open(args.input_path, "r") as f:
                input_files = [line.strip() for line in f if line.strip()]
    elif os.path.isdir(args.input_path):
        input_files = [
            file for file in glob.glob(os.path.join(args.input_path, '*')) 
            if file.lower().endswith(('.wav', '.mp3'))
        ]
    else:
        raise ValueError(f"input_path {args.input_path} is not a file or directory")
    
    print(f"Found {len(input_files)} audio files to evaluate")
    
    # Evaluate all files
    results = evaluator.evaluate_songs(input_files)
    
    # Save results
    output_file = os.path.join(args.output_dir, "result.json")
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    
    print(f"Results saved to {output_file}")
    
    # Print summary
    if results:
        print("\nEvaluation Summary:")
        for file_id, scores in results.items():
            print(f"\n{file_id}:")
            for dimension, score in scores.items():
                print(f"  {dimension}: {score}")


if __name__ == "__main__":
    main() 