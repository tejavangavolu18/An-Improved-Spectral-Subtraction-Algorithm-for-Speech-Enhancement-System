# 🎧 Improved Spectral Subtraction for Speech Enhancement

## 📌 Overview
Speech signals in real-world environments are often corrupted by background noise, which reduces intelligibility and degrades the performance of communication systems and speech recognition models.

This project implements an **Improved Spectral Subtraction Method** for speech enhancement based on the research paper:

> *"Improved Spectral Subtraction Method for Speech Enhancement" (ICIMM 2016, Atlantis Press)*

The goal is to reduce noise from a noisy speech signal while preserving the original speech components.

---

## 🧠 Background

### 🔹 What is Spectral Subtraction?
Spectral subtraction is a classical noise reduction technique that operates in the **frequency domain**. It assumes that noise is additive and estimates the noise spectrum, which is then subtracted from the noisy signal.

However, traditional spectral subtraction suffers from:
- Musical noise artifacts 🎵
- Over/under noise suppression
- Distortion of speech components

---

## 🚀 Proposed Improvement

The improved method introduces two key parameters:

### 1. **Over-Subtraction Factor (α)**
- Controls how much noise is removed
- Higher α → more aggressive noise removal

### 2. **Spectral Flooring Parameter (β)**
- Prevents negative or very small spectral values
- Reduces musical noise artifacts

### 🔢 Mathematical Representation

The enhanced magnitude spectrum is computed as:

|S_enh(k)| = max(|Y(k)| - α|N(k)|, β|N(k)|)

Where:
- Y(k) → Noisy signal spectrum  
- N(k) → Estimated noise spectrum  
- α → Over-subtraction factor  
- β → Flooring constant  

---

## ⚙️ Methodology

The implementation follows these steps:

### 🔹 Step 1: Signal Generation
- Generate a clean speech-like signal (sine wave)
- Add silence at the beginning for noise estimation

### 🔹 Step 2: Noise Addition
- Add Gaussian noise to simulate real-world conditions

### 🔹 Step 3: STFT (Short-Time Fourier Transform)
- Convert signal to frequency domain
- Extract magnitude and phase

### 🔹 Step 4: Noise Estimation
- Estimate noise from silent frames
- Compute average spectrum

### 🔹 Step 5: Improved Spectral Subtraction
- Subtract estimated noise using α
- Apply spectral flooring using β

### 🔹 Step 6: Signal Reconstruction
- Combine enhanced magnitude with original phase
- Apply inverse STFT

### 🔹 Step 7: Performance Evaluation
- Compute Signal-to-Noise Ratio (SNR)

---

## 📊 Results

| Metric            | Value     |
|------------------|----------|
| SNR (Noisy)      | 5.32 dB  |
| SNR (Enhanced)   | 10.81 dB |
| Improvement      | **+5.49 dB** |

### ✅ Observations:
- Significant reduction in noise
- Improved speech clarity
- Minor residual artifacts present

---

## 📈 Visualization

The project generates:
- Waveform comparison:
  - Clean vs Noisy vs Enhanced
- Spectrogram comparison:
  - Shows noise reduction in frequency domain

---

## 🛠️ Technologies Used

- Python 🐍
- NumPy
- Librosa
- Matplotlib
- SciPy

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/speech-enhancement.git
cd speech-enhancement
