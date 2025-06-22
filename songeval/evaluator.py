import os
import librosa
import numpy as np
import torch
from muq import MuQ
from hydra.utils import instantiate
from omegaconf import OmegaConf
from safetensors.torch import load_file
from .model import Generator


class SongEvaluator:
    """
    A trained aesthetic evaluation toolkit for song quality assessment.
    
    This class loads the pretrained model once and can be reused to evaluate
    multiple songs efficiently.
    """
    
    def __init__(self, use_cpu=False):
        """
        Initialize the SongEvaluator.
        
        Args:
            use_cpu (bool): Force CPU mode even if GPU is available
        """
        self.device = torch.device('cuda') if (torch.cuda.is_available() and (not use_cpu)) else torch.device('cpu')
        self._model = None
        self._muq = None
        self._setup_complete = False
        
    def _setup(self):
        """Load the models (called automatically on first use)."""
        if self._setup_complete:
            return
            
        # Get the package directory
        package_dir = os.path.dirname(os.path.abspath(__file__))
        checkpoint_path = os.path.join(package_dir, "ckpt", "model.safetensors")
        config_path = os.path.join(package_dir, "config.yaml")
        
        # Load configuration
        train_config = OmegaConf.load(config_path)
        
        # Initialize and load the generator model
        self._model = instantiate(train_config.generator).to(self.device).eval()
        state_dict = load_file(checkpoint_path, device="cpu")
        self._model.load_state_dict(state_dict, strict=False)
        
        # Load MuQ model for feature extraction
        self._muq = MuQ.from_pretrained("OpenMuQ/MuQ-large-msd-iter")
        self._muq = self._muq.to(self.device).eval()
        
        self._setup_complete = True
        
    @torch.no_grad()
    def evaluate_song(self, audio_path):
        """
        Evaluate a single song file.
        
        Args:
            audio_path (str): Path to the audio file (.wav or .mp3)
            
        Returns:
            dict: Dictionary with scores for each dimension:
                - 'Coherence': Overall Coherence score
                - 'Musicality': Overall Musicality score  
                - 'Memorability': Memorability score
                - 'Clarity': Clarity of Song Structure score
                - 'Naturalness': Naturalness of Vocal Breathing and Phrasing score
                
        Raises:
            FileNotFoundError: If the audio file doesn't exist
            ValueError: If the audio file format is not supported
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
        if not audio_path.lower().endswith(('.wav', '.mp3')):
            raise ValueError(f"Unsupported audio format. Please use .wav or .mp3 files. Got: {audio_path}")
        
        # Setup models if not already done
        self._setup()
        
        # Load and process audio
        wav, sr = librosa.load(audio_path, sr=24000)
        audio = torch.tensor(wav).unsqueeze(0).to(self.device)
        
        # Extract features using MuQ
        output = self._muq(audio, output_hidden_states=True)
        input_features = output["hidden_states"][6]
        
        # Get predictions
        scores = self._model(input_features).squeeze(0)
        
        # Return results
        return {
            'Coherence': round(scores[0].item(), 4),
            'Musicality': round(scores[1].item(), 4),
            'Memorability': round(scores[2].item(), 4),
            'Clarity': round(scores[3].item(), 4),
            'Naturalness': round(scores[4].item(), 4)
        }
    
    @torch.no_grad()
    def evaluate_songs(self, audio_paths):
        """
        Evaluate multiple song files efficiently.
        
        Args:
            audio_paths (list): List of paths to audio files
            
        Returns:
            dict: Dictionary mapping file IDs to their scores
        """
        # Setup models if not already done
        self._setup()
        
        results = {}
        
        for audio_path in audio_paths:
            try:
                file_id = os.path.basename(audio_path).split('.')[0]
                scores = self.evaluate_song(audio_path)
                results[file_id] = scores
            except Exception as e:
                print(f"Error evaluating {audio_path}: {e}")
                continue
                
        return results 