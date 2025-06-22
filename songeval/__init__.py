"""
SongEval: A trained aesthetic evaluation toolkit for song quality assessment.

This package provides a simple interface to evaluate song quality across five dimensions:
- Overall Coherence
- Memorability  
- Naturalness of Vocal Breathing and Phrasing
- Clarity of Song Structure
- Overall Musicality
"""

from .evaluator import SongEvaluator

__version__ = "0.1.0"
__all__ = ["SongEvaluator"]

# Global evaluator instance for efficient reuse
_evaluator_instance = None

def get_evaluator(use_cpu=False):
    """
    Get a global evaluator instance. The model is loaded only once and reused.
    
    Args:
        use_cpu (bool): Force CPU mode even if GPU is available
        
    Returns:
        SongEvaluator: The evaluator instance
    """
    global _evaluator_instance
    if _evaluator_instance is None:
        _evaluator_instance = SongEvaluator(use_cpu=use_cpu)
    return _evaluator_instance

def evaluate_song(audio_path, use_cpu=False):
    """
    Evaluate a single song file efficiently.
    
    Args:
        audio_path (str): Path to the audio file (.wav or .mp3)
        use_cpu (bool): Force CPU mode even if GPU is available
        
    Returns:
        dict: Dictionary with scores for each dimension:
            - 'Coherence': Overall Coherence score
            - 'Musicality': Overall Musicality score  
            - 'Memorability': Memorability score
            - 'Clarity': Clarity of Song Structure score
            - 'Naturalness': Naturalness of Vocal Breathing and Phrasing score
    """
    evaluator = get_evaluator(use_cpu=use_cpu)
    return evaluator.evaluate_song(audio_path) 