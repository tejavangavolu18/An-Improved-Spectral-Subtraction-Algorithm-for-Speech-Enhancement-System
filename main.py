import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# =========================
# STEP 1: CREATE SPEECH SIGNAL (with silence)
# =========================
sr = 16000

# Time
t = np.linspace(0, 2, 2*sr, endpoint=False)

# Silence (0.5 sec)
silence = np.zeros(int(0.5 * sr))

# Speech part (1.5 sec tone)
speech_part = 0.6*np.sin(2*np.pi*200*t[:int(1.5*sr)])

# Combine
speech = np.concatenate((silence, speech_part))

# =========================
# STEP 2: ADD NOISE
# =========================
noise = np.random.normal(0, 0.2, len(speech))
noisy = speech + noise

# =========================
# STEP 3: STFT
# =========================
S_noisy = librosa.stft(noisy)
mag = np.abs(S_noisy)
phase = np.angle(S_noisy)

# =========================
# STEP 4: NOISE ESTIMATION (from silence)
# =========================
noise_est = np.mean(mag[:, :20], axis=1, keepdims=True)

# =========================
# STEP 5: IMPROVED SPECTRAL SUBTRACTION
# =========================
alpha = 1.0
beta = 0.02

enhanced_mag = mag - alpha * noise_est
enhanced_mag = np.maximum(enhanced_mag, beta * noise_est)

# =========================
# STEP 6: RECONSTRUCTION
# =========================
S_enhanced = enhanced_mag * np.exp(1j * phase)
enhanced = librosa.istft(S_enhanced)

# =========================
# STEP 7: MATCH LENGTHS
# =========================
min_len = min(len(speech), len(noisy), len(enhanced))

speech = speech[:min_len]
noisy = noisy[:min_len]
enhanced = enhanced[:min_len]

# =========================
# STEP 8: SAVE AUDIO FILES
# =========================
write("clean.wav", sr, (speech * 32767).astype(np.int16))
write("noisy.wav", sr, (noisy * 32767).astype(np.int16))
write("enhanced.wav", sr, (enhanced * 32767).astype(np.int16))

# =========================
# STEP 9: SNR CALCULATION
# =========================
def calculate_snr(clean, test):
    noise = clean - test
    return 10 * np.log10(np.sum(clean**2) / np.sum(noise**2))

snr_noisy = calculate_snr(speech, noisy)
snr_enhanced = calculate_snr(speech, enhanced)

print("SNR (Noisy)     :", round(snr_noisy, 2), "dB")
print("SNR (Enhanced)  :", round(snr_enhanced, 2), "dB")
print("SNR Improvement :", round(snr_enhanced - snr_noisy, 2), "dB")

# =========================
# STEP 10: WAVEFORM PLOTS
# =========================
plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.title("Clean Speech")
plt.plot(speech)

plt.subplot(3,1,2)
plt.title("Noisy Speech")
plt.plot(noisy)

plt.subplot(3,1,3)
plt.title("Enhanced Speech")
plt.plot(enhanced)

plt.tight_layout()
plt.show()

# =========================
# STEP 11: SPECTROGRAM COMPARISON
# =========================
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
librosa.display.specshow(
    librosa.amplitude_to_db(np.abs(librosa.stft(speech)), ref=np.max),
    sr=sr, x_axis='time', y_axis='hz')
plt.title("Clean Spectrogram")
plt.colorbar()

plt.subplot(3,1,2)
librosa.display.specshow(
    librosa.amplitude_to_db(np.abs(librosa.stft(noisy)), ref=np.max),
    sr=sr, x_axis='time', y_axis='hz')
plt.title("Noisy Spectrogram")
plt.colorbar()

plt.subplot(3,1,3)
librosa.display.specshow(
    librosa.amplitude_to_db(np.abs(librosa.stft(enhanced)), ref=np.max),
    sr=sr, x_axis='time', y_axis='hz')
plt.title("Enhanced Spectrogram")
plt.colorbar()

plt.tight_layout()
plt.show()