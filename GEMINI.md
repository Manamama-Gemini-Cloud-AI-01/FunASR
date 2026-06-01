# FunASR Project Updates & Strategic Assessment (May 2026)

This document tracks the evolution of FunASR and provides a "warts and all" assessment of its current stability for integration into other projects.

## 🚨 Repository Alert Status (Updated May 27, 2026)
**Current Status:** **IMPROVED STABILITY** on `main` branch (Version 1.3.9).

### 1. Developer Fixes (v1.3.1 → v1.3.9)
- **SenseVoice + SPK Fixed:** Resolved the critical crash when using SenseVoice ASR with speaker verification models.
- **Torchaudio Compat:** Added fallback guards for `torchaudio >= 2.11` to prevent initialization errors.
- **Lazy Imports:** Implemented import guards for optional dependencies (`fastapi`, `transformers`), allowing the library to run even with a "messy" environment.
- **Whisper Fine-tuning:** Implemented `forward()` for Whisper models, enabling native fine-tuning within the FunASR pipeline.
- **vLLM Acceleration:** Heavy investment in `AutoModelVLLM` for GPU-based production throughput (>= v0.21).

### 2. The Transformers v5 "Deadlock" (Still Present)
- **The Problem:** Modern stacks (Transformers 5.x) are still incompatible with `qwen-asr` (v0.0.6) and other sub-models. It triggers an `AttributeError: 'Qwen3ASRConfig' object has no attribute 'thinker_config'`.
- **The Workaround:** Users **must** pin their environment: `pip install "transformers==4.57.6" "huggingface-hub<1.0"`.

---

## 🧪 Experimental Results (Polish ASR)

### 1. Model Quality Tier List (Polish)

| Tier | Model | Parameters | Verdict |
| :--- | :--- | :--- | :--- |
| **Godzilla** | **`Qwen/Qwen2-Audio-7B-Instruct`** | **7 Billion** | **Peak Intelligence.** Multimodal LLM that understands context. Best chance to beat WhisperX quality. Extremely heavy on CPU (RTF 20+). |
| **Industrial** | **`FunAudioLLM/Fun-ASR-MLT-Nano-2512`** | **800 Million** | **The Workhorse.** Trained on tens of millions of hours. Significantly better than the 0.6B/1.7B research models. Optimized for 31 languages. |
| **Research** | `Qwen/Qwen3-ASR-1.7B` | 1.7 Billion | **Unstable.** Prone to linguistic drift (hallucinating Portuguese/Russian) on CPU. High "LLM Tax" for mediocre results. |
| **Mobile** | `iic/SenseVoiceSmall` | 234 Million | **Fast Default.** Great for low-latency and basic multilingual tasks. CPU viable (17x realtime). |

---

## ⚖️ Strategic Comparison: FunASR vs. WhisperX

| Metric | WhisperX (The Scribe) | FunASR (The Engine) |
| :--- | :--- | :--- |
| **CPU Performance** | 🥇 **Champion.** Optimized C++ (CTranslate2). RTF ~1.2. | 🥉 **Laggard.** Unoptimized PyTorch. RTF ~5.0. |
| **Polish Accuracy** | 🥇 **Stable.** Very few hallucinations. | 🥈 **Variable.** Needs "Godzilla" models to compete. |
| **Orchestration** | 🥈 **Rigid.** Good for transcription only. | 🥇 **Powerful.** VAD + SPK + Emotion in one pipeline. |
| **Future Path** | Stable but plateaued. | Moving fast toward **GPU/LLM integration**. |

**Verdict on Migration:** 
If your existing script relies on **CPU speed and high-resolution timestamps**, stick with **WhisperX**. FunASR is not yet ready to replace the Whisper "Scribe" for simple, fast Polish transcription. Use FunASR primarily for its **extra features** (Emotion Detection, Speaker Diarization) or if you move to **high-end GPUs**.

---

## 🛠️ Recommended Components & Best Practices
These components remain the gold standard for FunASR pipelines:
1. **`funasr/fsmn-vad`**: For efficient segmentation.
2. **`funasr/campplus`**: For speaker identity.
3. **Configuration Rule**: **Always** use `hub="hf"`, `trust_remote_code=True`, and manually force `model_hub="hf"` in `vad_kwargs`.
4. **vLLM Integration**: For production scale on NVIDIA GPUs, use `AutoModelVLLM`. vLLM solves the "Time" problem, while larger parameter counts (7B+) solve the "Quality" problem.
