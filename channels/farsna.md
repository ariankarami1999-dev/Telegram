<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/r5kromcne9Nj0cZiR-SZRkIKjSK-QyDxwMynKPhCn79eqt8lo0uTxd7vQlbPbkgjVZw9hfWzZHXd-mRXl63H4WQBinBEa1rEa63r7J9wtik4DMJq9kLlLgpeV6aXN_JDk65mBeIQTW41s9MF3hkJzgBO7HPNaT-3MPiCEesuHt-vm0GGDHOfzeOkyan-orJvTiblcR8_3r-i31kcBl_8lAGGAIFmhEsPQkGVg6K50AG75pNXqSkNWYN0jFfNGBOqpzsYyAHR29d4ASHaOlbTisb_uwk2ETqkpJXjWi7CZJ-Lu3RqEUPt003Vm-ZK3_ZR78ucdrcffkFpVoVaQaMyqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-451248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1NOI8LZDVhChIWIy5iw3Dc0UFI8ZgycmVgLZwWSNRnMgb0zHeLHOzZvF8fvChBWKmw4v5uLmxwxVMKZSUoZGqNUDdwy4ElI-fPeuNu79cgG3FarIQ9GMXVnIaRl2eQzGejFEwG8jDDJv0gPR3dNKcpJDEIzO97vK2mt-wRuxeQg7waVpT8seQHvKT9_v8XQWPsJLwLTAMYGsPDtGlTp1P4DZY0VDKwnGZHh9ysPlxz8ftiCYQGagt3ttrfJIThmQP9KIELoxVG4v0djtQDiTHvN04uTd8odHQ4BndVUNOPdftoBO5l4k4KmMF5KwQ-s4PHJnZk0DxlOEm2Fmg__GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسرت مسی پس از نرسیدن به جام  @Farsna</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/451248" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451247">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/715b127338.mp4?token=kd5JqqBieJBR_Ullst8USeyR_ibca2ztMkMUDHxN_RTq-azhrZ6mstvtHIkJSKiDN2DAypaRLXkygDXeTVCE-oNRSgcCHL_11Dz0N98hk-XXfta2kbKR21ZX-3AW_WW7Ci9P27iOAtXpLKOl6fQ5xuxe4cH3J1bAc7wq6z889g0xwuMRe7L3brIQ7vTU4AdFPKLnkmp3dnS8mtidYXR04uc_SP1nfBGqrqU83558Ms_ExeLQGG89bbFRlP4akwnMXIGgQmh0T0t-CZL6Kclb4ELFuJogRs3C1eWwdpm2jPUSnbeG1tMwYo7-48iZBJfjCeG8nNv9TE3U2mjVcpMWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/715b127338.mp4?token=kd5JqqBieJBR_Ullst8USeyR_ibca2ztMkMUDHxN_RTq-azhrZ6mstvtHIkJSKiDN2DAypaRLXkygDXeTVCE-oNRSgcCHL_11Dz0N98hk-XXfta2kbKR21ZX-3AW_WW7Ci9P27iOAtXpLKOl6fQ5xuxe4cH3J1bAc7wq6z889g0xwuMRe7L3brIQ7vTU4AdFPKLnkmp3dnS8mtidYXR04uc_SP1nfBGqrqU83558Ms_ExeLQGG89bbFRlP4akwnMXIGgQmh0T0t-CZL6Kclb4ELFuJogRs3C1eWwdpm2jPUSnbeG1tMwYo7-48iZBJfjCeG8nNv9TE3U2mjVcpMWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوشحالی اسپانیایی‌ها بعد از سوت پایان بازی  @Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/451247" target="_blank">📅 01:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451246">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef11a7213.mp4?token=vvi2cXk7-e3BBF8W21d52jpAQ-Sa1yM-DmX7uPYv_cclkf9d2sS-zQFNsitMXSkl6bbthHMbKf3Pyy3OcTjZgZjr9UZ7Dn_TCO3RSIrnh721tAR1GBxEDzT7DU0fi0-aUh4kgiyuHsvBGjzRW7vwf7_jRCbnFQc-HYPJVU_xF8PDH5GzYb7Jy-Rs7hf3RT6A_nbZ1hnaDCvrdFAgxlDA5xoaBNktwINgfyal82CfOd5XPPVXO_-M_6-sE1LKct3szsPK9Sf7rIyHmxwpt7YYxYSigjOAcygsTZteWRTimAfyJC6QHXtJJjiD5R6iHEGuy98ioBI4j-vvAHZvNEtAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef11a7213.mp4?token=vvi2cXk7-e3BBF8W21d52jpAQ-Sa1yM-DmX7uPYv_cclkf9d2sS-zQFNsitMXSkl6bbthHMbKf3Pyy3OcTjZgZjr9UZ7Dn_TCO3RSIrnh721tAR1GBxEDzT7DU0fi0-aUh4kgiyuHsvBGjzRW7vwf7_jRCbnFQc-HYPJVU_xF8PDH5GzYb7Jy-Rs7hf3RT6A_nbZ1hnaDCvrdFAgxlDA5xoaBNktwINgfyal82CfOd5XPPVXO_-M_6-sE1LKct3szsPK9Sf7rIyHmxwpt7YYxYSigjOAcygsTZteWRTimAfyJC6QHXtJJjiD5R6iHEGuy98ioBI4j-vvAHZvNEtAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا فاتح جام‌جهانی فوتبال شد
⚽️
اسپانیا ۱ - ۰ آرژانتین  @Farsna</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/451246" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451245">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuXEXGa5pvckU71A364m3I67FXWU6UCD1hRc7bvbF1m45IhGVM3xO1bQ7loE3_IOor7mRJywqntGZChBMv5w2RUSxis5hfEOiFoArqIF4sD6EJ_fash2prturV2IaV_samDmVSmU_yZuZCwexH42GLsgJa3aYu8VgRHKC9yem73-aHT4PaMhqKDeXymLMQdqzdQgYefdbemc_KRwb3kpufEoA9SjQ4rKR62uzD-vIc2s9OLm4AAn6ccZs0H8M-gsTiLc0W0jn9jhXyGKb4ykxlvN7xhuF-d515oEtYb6jvGuGSgMcNbjGiEOArVoWTKZQg3jHv2sPCRlLBTrQNLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آرژانتینی‌ها این‌بار خودشان توپ را بیرون زدند  @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/451245" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451244">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46057c427c.mp4?token=MzWlpLoRGHQbNND3yVdrjKQquyEMEeJFwWM82lMCgQkqxSAAjEQI5XqkbLs-5IUa2SBpls2qAcGkCvL-aHHD4kGJCc8zb8rM1o5kv3gV4NaFrk4IUdrN6WbguI1b_43sTrtF2iYS8sXeDTFA4GDUfJIxg9oWL3U1isVmTl4Th69hJXOgxU_Rg0hkQriOLpgko6ahd1fy8r-s0MXwZci-UGtIPI8s48KDapoaHB4vVRPla4b63ifbYzjhSMS69rh5XG6XJG9yOrHnLe5aqEeugchxykv5VhadmQKdJhb2S2KM5IYY0lgyoitoMM2dOH5qATqXtfyIf04Y-IV_fy8zIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46057c427c.mp4?token=MzWlpLoRGHQbNND3yVdrjKQquyEMEeJFwWM82lMCgQkqxSAAjEQI5XqkbLs-5IUa2SBpls2qAcGkCvL-aHHD4kGJCc8zb8rM1o5kv3gV4NaFrk4IUdrN6WbguI1b_43sTrtF2iYS8sXeDTFA4GDUfJIxg9oWL3U1isVmTl4Th69hJXOgxU_Rg0hkQriOLpgko6ahd1fy8r-s0MXwZci-UGtIPI8s48KDapoaHB4vVRPla4b63ifbYzjhSMS69rh5XG6XJG9yOrHnLe5aqEeugchxykv5VhadmQKdJhb2S2KM5IYY0lgyoitoMM2dOH5qATqXtfyIf04Y-IV_fy8zIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توپ آرژانتین با مقاومت اسپانیایی‌ها گل نشد  @Farsna</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/451244" target="_blank">📅 01:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451243">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fba22ecb.mp4?token=G_6MuQLYGy8RXRv7V63ukq1XvUwdkYqf0p1ufvMGvAsxyV3BdtOmWrPnKZhG8Iw1EtYPE1eBM637BftO2XXBUydC4-3z7a1kQ-OoG7EtGFEziBYeieia1yVavd8O90aRVkQVZkX01g2kPcr-H7XVs5psAbzrZGX7-36xDfUzbk_q3bz_78qxxXrkoMZ-oRyiFdaw442Frd9ayjuY4gVhHOhONiGXyVAwbD5FEl-QfUxfy-eiS7JgxAZvbsdBzXBXwXA3XJrbqB5PJ46ChM_EqyasHfDpfXb6Gszeh5nBeilSGExgdWIh4BCZ1ro7KRWSqV0FBiRhpiwrfe5_Y2LS2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fba22ecb.mp4?token=G_6MuQLYGy8RXRv7V63ukq1XvUwdkYqf0p1ufvMGvAsxyV3BdtOmWrPnKZhG8Iw1EtYPE1eBM637BftO2XXBUydC4-3z7a1kQ-OoG7EtGFEziBYeieia1yVavd8O90aRVkQVZkX01g2kPcr-H7XVs5psAbzrZGX7-36xDfUzbk_q3bz_78qxxXrkoMZ-oRyiFdaw442Frd9ayjuY4gVhHOhONiGXyVAwbD5FEl-QfUxfy-eiS7JgxAZvbsdBzXBXwXA3XJrbqB5PJ46ChM_EqyasHfDpfXb6Gszeh5nBeilSGExgdWIh4BCZ1ro7KRWSqV0FBiRhpiwrfe5_Y2LS2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک مسی به صورت مرینو برخورد کرد  @Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/451243" target="_blank">📅 01:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451242">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c479a78e.mp4?token=vi-XW4_efgClpT943JYf8fYyXSyMiWfmb7V5HcF9Ne8jrW3doTchlpjozzbCG9UwC7UNeKN0jg6fhO4Q6nBxK8KnGJsJQsgX6vLCX6OEFuX8jzb0qRorf8OP-NrJfEVs5ha6gWp2z22SyQo0iKUzA_Fot7fJu2P9EVp3PEmqh4xpbPVh7NbogpyOm-gIPxQEc7yB0YjwcNAbqmoEi3rJllt1iO0NHjVKmEuARYxv0CDic9LsK7CO_5-2l5OOuQsurrlgAdG4J9ofC5Df4zq1weR3TmqAgzw2KjYIKr0FLk61fXFbieq-loS8HnzmzUgKh30r8FyNhCNvUMhkWWeYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c479a78e.mp4?token=vi-XW4_efgClpT943JYf8fYyXSyMiWfmb7V5HcF9Ne8jrW3doTchlpjozzbCG9UwC7UNeKN0jg6fhO4Q6nBxK8KnGJsJQsgX6vLCX6OEFuX8jzb0qRorf8OP-NrJfEVs5ha6gWp2z22SyQo0iKUzA_Fot7fJu2P9EVp3PEmqh4xpbPVh7NbogpyOm-gIPxQEc7yB0YjwcNAbqmoEi3rJllt1iO0NHjVKmEuARYxv0CDic9LsK7CO_5-2l5OOuQsurrlgAdG4J9ofC5Df4zq1weR3TmqAgzw2KjYIKr0FLk61fXFbieq-loS8HnzmzUgKh30r8FyNhCNvUMhkWWeYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/451242" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451241">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ab8e15f5.mp4?token=CTaNCd-BRJG4Y5e7wp15QxA1ey9LndEg6XvF0CdNa4-NJNja4F4Gr6SUgLjZ5vvzv7dhuWnOZhZ_zH6kVDfA__tY3E4yurvFINN614KkUeVt53JhK-7vuRafo8u2kP60J0D3NdfLvyM8sE3YLX6rJyaJIa9aU8tHS_ZYC6_uV6kmsJhKGBcb2WSdvPepRzolBViR_2BpZGd2J4dsgWE01PByokMciESYQImSN3MZFNw68jE79JDV2yIpCRXMq1LSMJFUafGgkeT8J7g2h23oLiaVPMjxHzxdOxUdH6LzFkM5fTI5_2truRnMjqEUu-2A94TpLzG44w4Q1NuB_AUApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ab8e15f5.mp4?token=CTaNCd-BRJG4Y5e7wp15QxA1ey9LndEg6XvF0CdNa4-NJNja4F4Gr6SUgLjZ5vvzv7dhuWnOZhZ_zH6kVDfA__tY3E4yurvFINN614KkUeVt53JhK-7vuRafo8u2kP60J0D3NdfLvyM8sE3YLX6rJyaJIa9aU8tHS_ZYC6_uV6kmsJhKGBcb2WSdvPepRzolBViR_2BpZGd2J4dsgWE01PByokMciESYQImSN3MZFNw68jE79JDV2yIpCRXMq1LSMJFUafGgkeT8J7g2h23oLiaVPMjxHzxdOxUdH6LzFkM5fTI5_2truRnMjqEUu-2A94TpLzG44w4Q1NuB_AUApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/451241" target="_blank">📅 01:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451240">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a07464492.mp4?token=G4ZhumYKzvUOy4leYTTrFlRHMSiYU00R3L2_AMTe3X64BQDnr1vMbGpeTE1Mt9VHl72V4MTc0f5i8eqzQEVPS2UjYeXHwH6ZlaDWavwQo-m4gXQ2SsImUWFVivdTK2lCTJfRj4U_RnAONZ4BiIgDtvDWiZEDudXMum8Pp9tRw3D3FdmIYIHsrtRuG2IH9z8X60nUAqTnEpcadb4-RVI8PpXdKutn5mcAnLy5Ni3loBBXXarASeuyXEaxGUI8Vd72JCjz2hAPoTWQFGMLXs80cj8xz8RkJSjZo74e5yk5QLrR2_wunT5v5QoX9IF_QYDYgexrdeI5TgkjFP_FOIhvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a07464492.mp4?token=G4ZhumYKzvUOy4leYTTrFlRHMSiYU00R3L2_AMTe3X64BQDnr1vMbGpeTE1Mt9VHl72V4MTc0f5i8eqzQEVPS2UjYeXHwH6ZlaDWavwQo-m4gXQ2SsImUWFVivdTK2lCTJfRj4U_RnAONZ4BiIgDtvDWiZEDudXMum8Pp9tRw3D3FdmIYIHsrtRuG2IH9z8X60nUAqTnEpcadb4-RVI8PpXdKutn5mcAnLy5Ni3loBBXXarASeuyXEaxGUI8Vd72JCjz2hAPoTWQFGMLXs80cj8xz8RkJSjZo74e5yk5QLrR2_wunT5v5QoX9IF_QYDYgexrdeI5TgkjFP_FOIhvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به آرژانتین توسط تورس در دقیقه ۱۰۶
⚽️
اسپانیا ۱ - ۰ آرژانتین @Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/451240" target="_blank">📅 01:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451239">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
منابع رسانه‌ای از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/451239" target="_blank">📅 01:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451238">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833aa9b679.mp4?token=Blt5fjBLAWUNUJoE9EUN2xjD3_KYvX_9rxsr50-Hjexcic0H0YqLN3OUN5P_KoIdtJY_sLYEPjfcaolhj29lMobfce5Q_n0XJBdjSAJ-xjKVdt5ICpcuTIQUUOiDFoIOtv7GrgfR15ujYNYZyIY7u9184UsyFJpem98VsNagNg-Ix6u6w_KkzT28-9msXytnrwSeDX0Ftdxk9skIUody-CAPHsaevjUXGK9ulD4-djtyD1LHka-N_gb9Vf4BGmr1JrE1ZSNKJjsOpi0mp7DHuBJha1qlsKtmGt3mezkgSPvboEC18FfrfhT3pipgZthwG16gb50-uKa7lRYp86SpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833aa9b679.mp4?token=Blt5fjBLAWUNUJoE9EUN2xjD3_KYvX_9rxsr50-Hjexcic0H0YqLN3OUN5P_KoIdtJY_sLYEPjfcaolhj29lMobfce5Q_n0XJBdjSAJ-xjKVdt5ICpcuTIQUUOiDFoIOtv7GrgfR15ujYNYZyIY7u9184UsyFJpem98VsNagNg-Ix6u6w_KkzT28-9msXytnrwSeDX0Ftdxk9skIUody-CAPHsaevjUXGK9ulD4-djtyD1LHka-N_gb9Vf4BGmr1JrE1ZSNKJjsOpi0mp7DHuBJha1qlsKtmGt3mezkgSPvboEC18FfrfhT3pipgZthwG16gb50-uKa7lRYp86SpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربه سر دیدنی مرینو از کنار دروازه آرژانتین بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/451238" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451237">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a809a6b06a.mp4?token=L6Jg6lFF61Rvr_KUjqvMfLW7H3_-wddsDK5deB74gQnm5Efi_dsLAHn0qAfW55XPwwd8CZtSWMAFoxjDRlegGf3_BvU9jxlKF6NvSjpqlpSjjQw3ViFg29gjjL5SsiWid7WFqRv_Ls2AWkpRGYEuth5a06BOEmHbv9ly5IdCdsiBNkE2oDr0my3xCnDz8vSxHwtz67tYpC2nyG7RDQr62OBvvjLOqlW7VZ9JPW-j4QiJTYdKBA_DM7TXpt55PsYY0zzLwoyQGEW02dM-mfe-D0xDXzkImzh5Zmdft07jbeNJt0pkX-6heot0GHmvWAEcouBT3FVI-wOYPohOi12t6l2e9A-ZE9-zdBkL8LrdC8D773Q7lswYOX7nlWfp-rc7vSw_b-CNu3q1mPH-QAS_U29xf8hI0AC33pWZF-eElnOmVUETwfCkwuAjfpj7tIeUHaYfziWX0A2ny6EEyPblpiYBPQQ6f1ADaGim3H9G6_qLZqs22gb8LmSoAwbFPy4btm4Ksgd0wKt5PxmMberI6P-9JvzhuOctgcgy3LKs14rWTxYpmoaOj7nfBLYIQxnzGT5aCEzxDRqxmuWxH8B9tABCCs56MlCDTYIPVUir9ano3XCWEYfqHrAJ80nuIlVgqkqvQvCSVZDAmO1xRVytb5WlchOGI9pJREi-3bkxK2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a809a6b06a.mp4?token=L6Jg6lFF61Rvr_KUjqvMfLW7H3_-wddsDK5deB74gQnm5Efi_dsLAHn0qAfW55XPwwd8CZtSWMAFoxjDRlegGf3_BvU9jxlKF6NvSjpqlpSjjQw3ViFg29gjjL5SsiWid7WFqRv_Ls2AWkpRGYEuth5a06BOEmHbv9ly5IdCdsiBNkE2oDr0my3xCnDz8vSxHwtz67tYpC2nyG7RDQr62OBvvjLOqlW7VZ9JPW-j4QiJTYdKBA_DM7TXpt55PsYY0zzLwoyQGEW02dM-mfe-D0xDXzkImzh5Zmdft07jbeNJt0pkX-6heot0GHmvWAEcouBT3FVI-wOYPohOi12t6l2e9A-ZE9-zdBkL8LrdC8D773Q7lswYOX7nlWfp-rc7vSw_b-CNu3q1mPH-QAS_U29xf8hI0AC33pWZF-eElnOmVUETwfCkwuAjfpj7tIeUHaYfziWX0A2ny6EEyPblpiYBPQQ6f1ADaGim3H9G6_qLZqs22gb8LmSoAwbFPy4btm4Ksgd0wKt5PxmMberI6P-9JvzhuOctgcgy3LKs14rWTxYpmoaOj7nfBLYIQxnzGT5aCEzxDRqxmuWxH8B9tABCCs56MlCDTYIPVUir9ano3XCWEYfqHrAJ80nuIlVgqkqvQvCSVZDAmO1xRVytb5WlchOGI9pJREi-3bkxK2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مزار شهدای دانش‌آموز میناب در شب شهادت حضرت رقیه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/451237" target="_blank">📅 01:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451236">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375b535f54.mp4?token=iTpx55hyd53xURL__wfZ7aNTH4JmRkV8bx8qxK07SKvih-EVFFwhhIpKNueu-UKaGW3Kfiy0lZVARTolaYY4iKABkAM2q2WcvAURoYGGvrf2VfId_psMScUjvyPZUrDdNmMa6qv0rzBPU-HnPmDub2MoU0H9Wo09alNAjTo0vg8gpMuntaLGSbd4aCB_d-0vQVpO8ZGcBg9rpPVwwIGGy6kbv0a7g3w8FTWOL4aiARCnitVgcMvVX17qgdulu1zQVQzH0XVNqafOSkEyQ5pKX1mrQK_c7rV3FzSe0HCkAfjLS7hW6U_umTKaN4PaX9lWSwe_9SM7Py4sbr4oTqncSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375b535f54.mp4?token=iTpx55hyd53xURL__wfZ7aNTH4JmRkV8bx8qxK07SKvih-EVFFwhhIpKNueu-UKaGW3Kfiy0lZVARTolaYY4iKABkAM2q2WcvAURoYGGvrf2VfId_psMScUjvyPZUrDdNmMa6qv0rzBPU-HnPmDub2MoU0H9Wo09alNAjTo0vg8gpMuntaLGSbd4aCB_d-0vQVpO8ZGcBg9rpPVwwIGGy6kbv0a7g3w8FTWOL4aiARCnitVgcMvVX17qgdulu1zQVQzH0XVNqafOSkEyQ5pKX1mrQK_c7rV3FzSe0HCkAfjLS7hW6U_umTKaN4PaX9lWSwe_9SM7Py4sbr4oTqncSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسپانیا گل زد اما داور پیش از آن خطا گرفته بود   @Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/451236" target="_blank">📅 01:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451235">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d04aa0f0f.mp4?token=AXo2JGsMDTIlhyQl2uQkPqB0kXbUItI98i2tFZmKwXlMCHMnFefelmvkSjeEavOZTD8FvHPpAlPeRuDFGo7x5agAEFChr9lVOe9RjOQbpjT_yHeEcZIGgv4OvywNKJL5tap7XD7wmVHaYG19KhtVzzdSp2atIDJEvEdqGTj5PP9ZSv6Il0BWTrCX-ubLmt_qmvIRbSvYK1aU5Z2bjBOPw8fDOurZFd98AGHa5znHhiawROrS_i9Jtq6vV_PeX5IFxKlpGVDxCfmU2vUm2bsQKo6qbIsCj3-pY4rPat6DhSBE9binC06Uy4AtdCil7o4amMNwLNo3rW4Q8r1BFYLtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d04aa0f0f.mp4?token=AXo2JGsMDTIlhyQl2uQkPqB0kXbUItI98i2tFZmKwXlMCHMnFefelmvkSjeEavOZTD8FvHPpAlPeRuDFGo7x5agAEFChr9lVOe9RjOQbpjT_yHeEcZIGgv4OvywNKJL5tap7XD7wmVHaYG19KhtVzzdSp2atIDJEvEdqGTj5PP9ZSv6Il0BWTrCX-ubLmt_qmvIRbSvYK1aU5Z2bjBOPw8fDOurZFd98AGHa5znHhiawROrS_i9Jtq6vV_PeX5IFxKlpGVDxCfmU2vUm2bsQKo6qbIsCj3-pY4rPat6DhSBE9binC06Uy4AtdCil7o4amMNwLNo3rW4Q8r1BFYLtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان آرژانتین یکی پس از دیگری موقعیت‌های اسپانیا را مهار می‌کند  @Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/451235" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4511c12bc.mp4?token=GCWn1HCT6JYL5HQBdRFJ4qCwYUcifNAMmaJtAXno6IuNLEHc-9YGFaEfbCdB4c89TxG3v8BOYFth5pskDyjZLoyzMYFBXU5X9YnGViIwqGG7LLUzWDXK0oOiKE4LwesLJRKC4DygNjKefkmgAvFQu2iVgWVgupIheP9ZCWB41kVYG-D4BzpgWjon3v3lazAQsprsEUGPulNkzgDQ9g_vzMmmLKr2O3Df_esWXCxmjd6bsk1-1DCfRtXPTEBPmdTv3QaZvBym0DGnZeaJ7YWhBmfPtcY7L86sZJE0M34mp51CH7qiTPnGUXPNsgsrc1OBiQrdTRDXVdKFKci6pVum2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4511c12bc.mp4?token=GCWn1HCT6JYL5HQBdRFJ4qCwYUcifNAMmaJtAXno6IuNLEHc-9YGFaEfbCdB4c89TxG3v8BOYFth5pskDyjZLoyzMYFBXU5X9YnGViIwqGG7LLUzWDXK0oOiKE4LwesLJRKC4DygNjKefkmgAvFQu2iVgWVgupIheP9ZCWB41kVYG-D4BzpgWjon3v3lazAQsprsEUGPulNkzgDQ9g_vzMmmLKr2O3Df_esWXCxmjd6bsk1-1DCfRtXPTEBPmdTv3QaZvBym0DGnZeaJ7YWhBmfPtcY7L86sZJE0M34mp51CH7qiTPnGUXPNsgsrc1OBiQrdTRDXVdKFKci6pVum2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان آرژانتین بازهم اسپانیا را ناکام گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/451234" target="_blank">📅 00:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
مقاومت اسلامی عراق: در صورت اصرار دشمن آمریکایی بر گسترش حملات خود به ایران، مستقیماً وارد نبرد خواهیم شد و با تمام قدرت و قاطعیت، تمامی منافع و پایگاه‌های آمریکا را در عراق و منطقه هدف قرار خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/451233" target="_blank">📅 00:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
منابع رسانه‌ای از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/451232" target="_blank">📅 00:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451231">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb709750a9.mp4?token=GRHNtlUZyJTT74bKaCsuKv5WK19sleio3d9rKA3ZHOB0JzQlN8sKa2-899-2S0WSTE7AQownr4DC4Y_MDCWEGMHjEYfkS1mArlBQs8Tktg8sq1V5MvVIyofkaYXpgoqBLzNLihIwbM_tYTt1b4um5b1-tjYS40y6GRUwbYH_LXVHvan0bDl3wiQWTB-YLhraw29BCsv_m4ZMbe5k2rp_1AhYRXLeLqxpigt9QJdu7Z-VX3ZY2g4EqcxyMR83l71Qr-iyLncS8naTEgGyCiU6nYEA5I996ZXSesYHXga9q-jVSIUoml9Rbqsz765CJ_-0y5aixLfe-kWfAfwlo4yfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb709750a9.mp4?token=GRHNtlUZyJTT74bKaCsuKv5WK19sleio3d9rKA3ZHOB0JzQlN8sKa2-899-2S0WSTE7AQownr4DC4Y_MDCWEGMHjEYfkS1mArlBQs8Tktg8sq1V5MvVIyofkaYXpgoqBLzNLihIwbM_tYTt1b4um5b1-tjYS40y6GRUwbYH_LXVHvan0bDl3wiQWTB-YLhraw29BCsv_m4ZMbe5k2rp_1AhYRXLeLqxpigt9QJdu7Z-VX3ZY2g4EqcxyMR83l71Qr-iyLncS8naTEgGyCiU6nYEA5I996ZXSesYHXga9q-jVSIUoml9Rbqsz765CJ_-0y5aixLfe-kWfAfwlo4yfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرژانتین ۱۰ نفره شد  @Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/451231" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451230">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f33f7f43c.mp4?token=AWcx4yT7vo65QNoHRvQLNWNeJDZo3suCsq3cBEyy9UGoIaOEmoe4r4nGJFOugRYSRstyE6mCiZ2YBWUSYAqyA6yU-9KJaS1iEEmTmv8eBu42HCjfTa20mjypTC85G_aZck7ilDpBFGWie8FLok4uZiMApBx9ov-IfDukOvknsSW1vQK_DWPWuFJhiMLknF33hCS_xI6hYN6Iw365txrv7GhayGn52yUKmf-7fkLP8ciro8PqAdXg0XWasF4r6jsCQVQM8NrFznlSPCAYKPIAw0rS2jrjh2bokFOMGZUTigdQrdJ6WvoV0zHiF5WyA9oYzvGWmPTALqaifoHxuWuufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f33f7f43c.mp4?token=AWcx4yT7vo65QNoHRvQLNWNeJDZo3suCsq3cBEyy9UGoIaOEmoe4r4nGJFOugRYSRstyE6mCiZ2YBWUSYAqyA6yU-9KJaS1iEEmTmv8eBu42HCjfTa20mjypTC85G_aZck7ilDpBFGWie8FLok4uZiMApBx9ov-IfDukOvknsSW1vQK_DWPWuFJhiMLknF33hCS_xI6hYN6Iw365txrv7GhayGn52yUKmf-7fkLP8ciro8PqAdXg0XWasF4r6jsCQVQM8NrFznlSPCAYKPIAw0rS2jrjh2bokFOMGZUTigdQrdJ6WvoV0zHiF5WyA9oYzvGWmPTALqaifoHxuWuufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان آرژانتین این‌بار ضربه سر لاپورت را مهار کرد  @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/451230" target="_blank">📅 00:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
منابع خبری از به‌صدا درآمدن آژیر هشدار، و وقوع انفجار در پایگاه‌های آمریکا در بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/451229" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/451228" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451227">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صدای شنیده‌شده در اراک مربوط به اقدامات آفندی است
🔹
دقایقی پیش منابع محلی از شنیده‌شدن صداهای انفجار در برخی نقاط شهر اراک خبر دادند.
🔹
درهمین راستا، فرماندار اراک اعلام کرد که صدای شنیده شده مربوط به اقدامات آفندی در یکی از استان‌های مجاور است و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/451227" target="_blank">📅 00:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bec5eee3.mp4?token=q-heD6VpZ6jvJ5JnWqHuko4d9zNHGH6pxlXV7o1meN_4eJO3oDvkXB4KzTSVaPeJcPxI5ojC5YBe2Rsmm4a30BO-5T1hJzDmUFWLIKimGPmwJck5C7AqObCYaJ8LdsnPccgA4AdZARcC3o3imhEHgBv9guQc2_mwtHEuE204aBdPC7s4fJVHi2YtV7Kk2V-SRxMdJaeDZ-ucbv2vU7Sw2TmJKiqMjaIGhTJryLEi6yA75dXflrc5Y_GGUgo03LwHaWYTrwU7VoMhwJ5xT3oEJ0qNPwa5YMGj4iavXYHWBB0AfAeHGKPfUOFTeP2Ust3IElaYmeJ3lzglekL6qs6yxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bec5eee3.mp4?token=q-heD6VpZ6jvJ5JnWqHuko4d9zNHGH6pxlXV7o1meN_4eJO3oDvkXB4KzTSVaPeJcPxI5ojC5YBe2Rsmm4a30BO-5T1hJzDmUFWLIKimGPmwJck5C7AqObCYaJ8LdsnPccgA4AdZARcC3o3imhEHgBv9guQc2_mwtHEuE204aBdPC7s4fJVHi2YtV7Kk2V-SRxMdJaeDZ-ucbv2vU7Sw2TmJKiqMjaIGhTJryLEi6yA75dXflrc5Y_GGUgo03LwHaWYTrwU7VoMhwJ5xT3oEJ0qNPwa5YMGj4iavXYHWBB0AfAeHGKPfUOFTeP2Ust3IElaYmeJ3lzglekL6qs6yxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربه سر خطرناک فران تورس با مهار دروازه‌بان آرژانتین همراه بود  @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/451226" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شترسواری دولا دولای آپارات به بهانۀ جام‌جهانی!
🔹
برنامۀ اینترنتی «دری رو به جام» از تولیدات آپارات اسپرت، در حالی پخش شد که ایمان صفا بازیگر حامی کودتا و اغتشاشات دی‌ماه ۱۴۰۴ مهمان آن بود.
🔹
این درحالی است که این بازیگر در ماه‌های اخیر به‌ویژه از دی ماه ۱۴۰۴ به بعد، بارها مواضع صریح و آشکاری در حمایت از جریان آشوب و اغتشاش داشته و همچنین استوری‌های تمسخرآمیز و نیش‌آلودی را نسبت به کلیت نظام و سیاست‌های اصولی آن منتشر کرده است.
🔹
همچنین حضور اخیر او در مراسم ختم مادر داریوش فرضیایی با لباسی که یکی از نمادهای کودتای دی‌ماه روی آن دیده می‌شد، اقدام حاشیه‌ساز جدیدی بود که مورد استقبال ضدانقلاب قرار گرفت.
🔸
در شرایطی که پلتفرم‌ها به‌‌وفور نشان داده‌اند اگر جریان پایدار و مستمر پایش و نظارت ساترا بر تولیدات‌شان وجود نداشته باشد، از استعداد چشمگیری برای بروز استانداردهای دوگانه برخوردارند، باید بیش از پیش، بر تقویت نقش نظارتی این نهاد تنظیم‌گر توجه و تاکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451225" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8bce10f2b.mp4?token=GIB6kZSFIO3tNMP4j4RZHbQEdnz5eWjo0p06adbX5mOH2dir-vRN992UHWFdgRnZ8OkEMmkREyvXOSwzg_u15Cw0u8y4LtSiYu9oi6a5lVaXC_6VXwaCQwAvXrCdB5etrq7kLQ_oLTLPXBoFc2y0BksQCmHrrjCmFNjdgsCQsc79-yt13Azt22KLl8sEUkBX8jsM7yeNtWyE9pATuS_5CbyZBCvadnw3BhDwGwL4T-9bE93ygJZtH3RZ4-XBYFN7hK3ohWGFymGsdrI6WrDDyhyy4LIxIS1on_IFhiOfH0m9tV_V6iq-kK8VGzwujAh_lh6hHCQ8zGZyoVLCF-u4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8bce10f2b.mp4?token=GIB6kZSFIO3tNMP4j4RZHbQEdnz5eWjo0p06adbX5mOH2dir-vRN992UHWFdgRnZ8OkEMmkREyvXOSwzg_u15Cw0u8y4LtSiYu9oi6a5lVaXC_6VXwaCQwAvXrCdB5etrq7kLQ_oLTLPXBoFc2y0BksQCmHrrjCmFNjdgsCQsc79-yt13Azt22KLl8sEUkBX8jsM7yeNtWyE9pATuS_5CbyZBCvadnw3BhDwGwL4T-9bE93ygJZtH3RZ4-XBYFN7hK3ohWGFymGsdrI6WrDDyhyy4LIxIS1on_IFhiOfH0m9tV_V6iq-kK8VGzwujAh_lh6hHCQ8zGZyoVLCF-u4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صداوسیما: در بازی فینال جام‌جهانی فوتبال هیچ تصویری از رئیس‌جمهور جانی آمریکا نمایش نمی‌دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451224" target="_blank">📅 00:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آژانس بدون اعلام محکومیت: حمله به سایت دارخوین را بررسی می‌کنیم
🔹
آژانس بین‌المللی انرژی اتمی با صدور بیانیه‌ای، صرفاً به اظهارنظر فنی درباره حمله آمریکا به سایت در حال ساخت نیروگاه هسته‌ای دارخوین اکتفا کرد و از هرگونه محکومیت یا اشاره به عامل حمله خودداری…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451223" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451221">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌ اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله قرار…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451221" target="_blank">📅 23:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451220">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=lRNzQhnUxANcllOqKQHaN7oAhLPzTW001XcTzDI0F13oAL5W6Nnw6UG0Bo0PJ6QHlQS1cxXZnnB2gIwJEt_XZqfLGCwzcSqivecyqw6JtbtBNZAa20CpXfMk9GSREXBqWsg7yHZinb9_L_5oGrom6jP1wqD541k21VAMedI6PcThRmOKrpR1cp65RC5w_LED-P9KGHeZEZmQoc142o0K6fTfhzQtUUF025fHnjC8l-bj2k86QRtyseVRJMDXm3aMoR82CO-OiEKIpX9M_QFp4AsaZwpon9t3XMZveqlQQ8SPD1TR-qxwOj6q2iwM52lZ51xyFsQ7LCCGt72nrGfP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65067a3a3.mp4?token=lRNzQhnUxANcllOqKQHaN7oAhLPzTW001XcTzDI0F13oAL5W6Nnw6UG0Bo0PJ6QHlQS1cxXZnnB2gIwJEt_XZqfLGCwzcSqivecyqw6JtbtBNZAa20CpXfMk9GSREXBqWsg7yHZinb9_L_5oGrom6jP1wqD541k21VAMedI6PcThRmOKrpR1cp65RC5w_LED-P9KGHeZEZmQoc142o0K6fTfhzQtUUF025fHnjC8l-bj2k86QRtyseVRJMDXm3aMoR82CO-OiEKIpX9M_QFp4AsaZwpon9t3XMZveqlQQ8SPD1TR-qxwOj6q2iwM52lZ51xyFsQ7LCCGt72nrGfP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صداوسیما: در بازی فینال جام‌جهانی فوتبال هیچ تصویری از رئیس‌جمهور جانی آمریکا نمایش نمی‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/451220" target="_blank">📅 23:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451219">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93984c2740.mp4?token=ooq4eLdypAZQhb9yxQG6vhLj9PX6ZuBj0cMRqVrLzKhlshgQTdAkwVbgUwFoVP_X5g2RyhSVMjXM6Qht-vNG-kzRLvlKh6YnZo7E7HywPW9RdmDw5jMoXR_5JoqkKLyO6zI3qUniJNXccc1xC6s-XHc7h14gvh-5uLJNBc0yIo8lPRqzZBqyml6HqeEb4-PFGXjcOCkL-y1xaAj_2jH5YmLILJmC1jZ8_BCycBrF4TBaYtMsGGVvM-LgxuTWWav3AF_7wLw2SvSDFGo5fVQ5zcg_4CUROrVZWrmEt3axw3A0QUR2SW1ehY58iNklO-DYyld_4ZS50kM8HSDLO3JPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93984c2740.mp4?token=ooq4eLdypAZQhb9yxQG6vhLj9PX6ZuBj0cMRqVrLzKhlshgQTdAkwVbgUwFoVP_X5g2RyhSVMjXM6Qht-vNG-kzRLvlKh6YnZo7E7HywPW9RdmDw5jMoXR_5JoqkKLyO6zI3qUniJNXccc1xC6s-XHc7h14gvh-5uLJNBc0yIo8lPRqzZBqyml6HqeEb4-PFGXjcOCkL-y1xaAj_2jH5YmLILJmC1jZ8_BCycBrF4TBaYtMsGGVvM-LgxuTWWav3AF_7wLw2SvSDFGo5fVQ5zcg_4CUROrVZWrmEt3axw3A0QUR2SW1ehY58iNklO-DYyld_4ZS50kM8HSDLO3JPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم اجتماعات شبانه با ۱۴۱ شب ایستادگی در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451219" target="_blank">📅 23:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451218">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iefmEgovkPQGwDN-ISZK-kzJGR8pqGHliSZYbqsjzzp_w_lxto_VC1WEqaR2gUFDvCx-S78kufyZBcBtBSgfI9Cu1m3mlUUL-UmzE6vfQlnnQgxrDaOon7i0xk6kIVPvyu1zgtu0aAImPX9DzgskdX9swV8eT6ZJjIOovRQACHPidVF8cmYkA8tdagLW3QLNZYXFVvnpXU73mS9P0x7xbpldef6-Bp3KGX439k0PzHqfXk_R6bW2YWkabaefR1cECwUgC6v9jTjZ4AIyUUMTyDtvjKMpWYx6PC2oLX0BDo62CntDn7njuEhGVPmkdY7Q33ZNgWaIWlvDrT_TtXeTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ترامپ از پشت شیشۀ ضدگلوله فینال جام‌جهانی را تماشا می‌کند
@Sportfars</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/451218" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451217">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBcJMXyLLRSBOhwL2RXHIc2478zMym7EHIKYKQR1ty2fP-G4TnQ1xww1caJBLh1AeMeblM93luV4nuWK5_cXr0gktH7nlCVgiH88hBIHqb1P3ms4Bpz-A6PJUZi-pBr6ShghglRWp48Ucb3xJP23ElHU9ST3PrfeBsvdMwDvtM6ddwJtEKt1wjjVAw9qqVcy2ZHym5uUxDumf68Uml-_hI-LDIHRTqEsdRTf1vX9e0IOvWVa3CUOT6PsVn7pFQ76f8J6kBp9SY8FShjLQrF1QOdzVChx_2454dorNj9SjfykO6Q1y4_WWATreDrF4IMYrDGoKtROFEglO_rUk3czPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر راه: تمامی خطوط ریلی کشور فعال هستند
🔹
در حال حاضر هیچ‌گونه انسدادی در مسیرهای ریلی کشور وجود ندارد و تمامی خطوط ریلی فعال هستند.
🔹
ایستگاه انشعابی راه‌آهن بندرعباس نیز به‌زودی به مدار بازمی‌گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451217" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451215">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG9QHyIilcsI8qXXyD8ZElNB1KeopW0b3k9gaW5cB-LGEHgtdwhk4V07SaEjoIPYsnqWSGD1PBFeJnbKVst1m2zo9x6tHhkdheA_sDj_qkTUzwtoXT8sR3rHNPhMqp369yk-ElnfnqTa8410YyF1ZzsEc22D3s2CTYTniL_evTiMrRnlic_G5oSUDPiRVClFrRupm9He285ci80Sc6iQWHn_nR6OueyPc84WLeU6G_rxNYRpn9bH-RCWFghKUtCryVKlmQZ5i6f77cwDmlaTBW2hlTNqSxazgpGAmEX-9lcGxXk06sV-rXfBVhDHQQ3cGeJDvGQregs2cMtVYcijZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9uXu151oIck5K9mx9S_KqAZKOgCMEWSulBa7pMKoN8EHzTMRqxd2VO6iHib0NfIo6V_Xxwitd7ARTOWkN--PN3zDXoG7jxZuHSNHlhvNnFLTXqTK7RIcRFqa4YXxqg3-4CQ0qK6zO6dSoCoCKsfMCh8XS6xYV1gXCZZhfb1K1dwEfHOxfv_KdCMGAYBLOgEvq4bNdXms-Ci808j-0BoFkPu0u8cOgHhqsYE07yJjWtvudlG1c3TkVe1cN54Kksl_TRRF0ZiHG2HsRX0Lx9q65IFZsekokGmP-pE3OHHdXIfa0AUfgQmJl_W_-4MGIMC8L9XsGsUgfy7m-AF-eGMgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451215" target="_blank">📅 22:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451214">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: یک نظامی آمریکایی در حملات ایران به اردن مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451214" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451213">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
اعتراف سازمان تروریستی سنتکام: ۲ نظامی آمریکایی در حملات ایران به اردن کشته و ۴ نظامی مجروح شدند. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451213" target="_blank">📅 22:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451211">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrA7HWeq7WWu_YEz7BZp-aTHJAdcZFifchLvsVFALt-xNoSTOeiPK_VokfgSYy9vdgchXke12Gtc0JhXAjzr2hGHUTtSWJOGIF5mA6tGfAuYApGMz5BEZ_64s9dpbvbfKvtVIwyTGhQV2OwCBnq--EiAfl6Ix3tj3ZXfJvhCS3D2y9sWidyqKORQKq4WibX8KXE1hHZWMshIiX1qIqlHM8ed7Ynvk4kOpIAdqAid-jOLYVuTI8kNrV56b0PROrBMlajUauqf0PasgVUwZQzw4I_t21mFjOcUrvlGrg75-rw1p-1HxmZzqyZw52Vem7NNkZc1B8L4CoVWVBKlvDoD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقابل چشمان ترامپ
📷
نمایش پرچم ایران در استادیوم مت‌لایف کنار پرچم ۴۷ کشور دیگر پیش از شروع فینال
@Sportfars</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451211" target="_blank">📅 22:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451210">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
منابع عربی از هدف قرارگرفتن مواضع گروهک‌های تجزیه‌طلب در منطقۀ سلیمانیه در عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451210" target="_blank">📅 22:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451209">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc36bb3b8.mp4?token=mSJ7B8nSz5EDU6LCoyf53vUoGhCDNg2ohEWZoF_pZezuNm51zxw3vTJI0eote05FDWnlnxQcKefm_DVLck-oDsySvRwrpBucPJZT-8MZEhz_5XM3iGfMLTgUeeHdDJLYxCx-ccYV0V5YJZCoSC3-vMO3--3vc6RbEpzRHvjSxVPSCRF2YSWm86OCuBBv8pJD7fJneL_3TCtj_o6M-79fKPx6glMcdyT_NEZVI9V2iXd3p-BaEYS-MrLOH-Q30QghJah5wrJP08wSpwaZihxBpkFFMmq90WedPqQWB9yi-12Kkzveane-EwJFIIyT3gutGZDxHrg9Mq38yFwH2uCLIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc36bb3b8.mp4?token=mSJ7B8nSz5EDU6LCoyf53vUoGhCDNg2ohEWZoF_pZezuNm51zxw3vTJI0eote05FDWnlnxQcKefm_DVLck-oDsySvRwrpBucPJZT-8MZEhz_5XM3iGfMLTgUeeHdDJLYxCx-ccYV0V5YJZCoSC3-vMO3--3vc6RbEpzRHvjSxVPSCRF2YSWm86OCuBBv8pJD7fJneL_3TCtj_o6M-79fKPx6glMcdyT_NEZVI9V2iXd3p-BaEYS-MrLOH-Q30QghJah5wrJP08wSpwaZihxBpkFFMmq90WedPqQWB9yi-12Kkzveane-EwJFIIyT3gutGZDxHrg9Mq38yFwH2uCLIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی آموزش‌و‌پرورش: تا این لحظه هیچ سهمیه‌‌ای برای مناطق درگیر جنگ درنظر گرفته نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451209" target="_blank">📅 22:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451208">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آموزش‌وپرورش: امتحانات نهایی پایهٔ دوازدهم روز سه‌شنبه ۳۰ تیرماه مطابق برنامه در تمامی استان‌های کشور به‌جز هرمزگان برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451208" target="_blank">📅 22:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451207">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5VIb3atx2Hl1757OH0ySZSz2zdJ-EaQ5d6vDvMZDAGaMboy8fnw6KTeEqoY8beyblve45ZXuGADe6iaihab04nBnb8PWoEka-58oG5ZLMVXARTWCjwk7tFYGsmoIYz3t5RZzEoTEuu06bcOU7Fupc0KFpDRMw9wwVFoGqK9TTjnCmAs5ifIW4loR0HoEqtUa5cm1Bjw9-HXZEdawKZR6DMYuxYefmlUcIIFoFfl0qm9ZrpU45Tmh4kXTy7Ixd5Ca4F8TFA2YLwBTZkMClF5tEfckO4wTKsNsUP9lrtIei3DOM0O-yldvAKZp4dD6mY31wbrs-R2IJMXvwG9Nis5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رونمایی از کاپ جام‌جهانی ۲۰۲۶
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451207" target="_blank">📅 22:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451206">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3576da499e.mp4?token=HwJnsBQaYw0BiHPAMkIVOc9v9X0Q9tZHbiHNNq4U5jh0ANZA1Po58T-OtOKGIcxADH20FyxDutRPzJD548TJ9dNtuuSrxMen3mlfaOJuYMuc-X0BGKNPFGQIV0eTQLnXxEvyesktVhWESFYwDDaxCQ6pnfiiHYM64s6wGIiPUU0fc4sNj2nAjiLuv5b6hNJPFJwR8y5P6LZH_xWUP5Tn2P-3Vr54BcH4rEAz6WT6qLyuU-te7f6oEFZzD62zqmK3Z0xg8-szuI-yEiMM5YSsHD6BQ7YEof9EUXWYc5rRHDQwLYBOfuPgPbDTd8IZz9bsebRTOy8FZY1cKbvhuGYWww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3576da499e.mp4?token=HwJnsBQaYw0BiHPAMkIVOc9v9X0Q9tZHbiHNNq4U5jh0ANZA1Po58T-OtOKGIcxADH20FyxDutRPzJD548TJ9dNtuuSrxMen3mlfaOJuYMuc-X0BGKNPFGQIV0eTQLnXxEvyesktVhWESFYwDDaxCQ6pnfiiHYM64s6wGIiPUU0fc4sNj2nAjiLuv5b6hNJPFJwR8y5P6LZH_xWUP5Tn2P-3Vr54BcH4rEAz6WT6qLyuU-te7f6oEFZzD62zqmK3Z0xg8-szuI-yEiMM5YSsHD6BQ7YEof9EUXWYc5rRHDQwLYBOfuPgPbDTd8IZz9bsebRTOy8FZY1cKbvhuGYWww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف مردم دربارهٔ دلسوزی قلابی این‌روز‌های برخی سلبریتی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451206" target="_blank">📅 22:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2d11e6ab.mp4?token=oJjGvVgeYBa4jv7yeHkBlzHDa5fHLXjHbb7Ezoeb-ewqMP0oMOyhb2rbcTYqC1sPRjrJPIPrySiP5UMZhVHaFCKgyqNfAJcev3f3AaWN_ezKx8xlwdIwjBDD1EqH7m0FMKyO1MAKP5g6CWKf2n8VdrA5HM5dKkp1OSUy4fjg6wFpqFrw_l9elgv-tTJ2OuxigkVkQDnIy7QXtSYlWwNKWG-ea2Sk0uAJuBo8opirCKREKoQUohXn9goSWX1QwiXcdY0zIZCb5wIoMv0spH1dSJiCmcXMQbIF-1tQD-3TnvQx2jwi_fWwspbUfWk_h1cz9TpCslZJ3t845haxOlbSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2d11e6ab.mp4?token=oJjGvVgeYBa4jv7yeHkBlzHDa5fHLXjHbb7Ezoeb-ewqMP0oMOyhb2rbcTYqC1sPRjrJPIPrySiP5UMZhVHaFCKgyqNfAJcev3f3AaWN_ezKx8xlwdIwjBDD1EqH7m0FMKyO1MAKP5g6CWKf2n8VdrA5HM5dKkp1OSUy4fjg6wFpqFrw_l9elgv-tTJ2OuxigkVkQDnIy7QXtSYlWwNKWG-ea2Sk0uAJuBo8opirCKREKoQUohXn9goSWX1QwiXcdY0zIZCb5wIoMv0spH1dSJiCmcXMQbIF-1tQD-3TnvQx2jwi_fWwspbUfWk_h1cz9TpCslZJ3t845haxOlbSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: در جنگ رمضان، حدود ۴۰۰۰ بازرسی سرزده از دستگاه‌های تحت نظارت در سراسر کشور انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451204" target="_blank">📅 21:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
وقوع انفجار در اربیل عراق
🔸
هنوز جزئیات بیشتری دربارهٔ علت انفجار یا تلفات احتمالی منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451203" target="_blank">📅 21:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4303a24a4.mp4?token=e8pyq6yNxFKRG0AQEhTmpULoAR466MNLf-CySCqg3az1kYPk3PAnY7qRKIu3CKhxST9zQPQj1U2fSaOjHWz9AMVXa85429dVUVrCYzwrTyA-I33ceCF6Sc6Wv5YEgjV6agSbVgvG7XDzhImWvMILQEuaY_Lmsm-uwyNs_5X8rJqQBBs1unwHk3MtvKUvf19nr0ycGqkvKOEBDFEJZ42Yj6TPbKIx7yvOLx8NH-RioaEMr6ieeSPppx6n53WtiYxTFzXE174K34kcIdYCpRcslRDPJ3mMn42iGIDzJFDcQF--Jv6TLtD8RN2u6yg3bwqPxBS7Ad3AWGMvp6-MpUd-lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4303a24a4.mp4?token=e8pyq6yNxFKRG0AQEhTmpULoAR466MNLf-CySCqg3az1kYPk3PAnY7qRKIu3CKhxST9zQPQj1U2fSaOjHWz9AMVXa85429dVUVrCYzwrTyA-I33ceCF6Sc6Wv5YEgjV6agSbVgvG7XDzhImWvMILQEuaY_Lmsm-uwyNs_5X8rJqQBBs1unwHk3MtvKUvf19nr0ycGqkvKOEBDFEJZ42Yj6TPbKIx7yvOLx8NH-RioaEMr6ieeSPppx6n53WtiYxTFzXE174K34kcIdYCpRcslRDPJ3mMn42iGIDzJFDcQF--Jv6TLtD8RN2u6yg3bwqPxBS7Ad3AWGMvp6-MpUd-lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرج‌و‌مرج در ورودی ورزشگاه مت‌لایف
🔹
درحالی که کمتر از یک ساعت مانده به آغاز مسابقه، هرج و مرج در بیرون ورزشگاه مت‌لایف به اوج خود رسیده است و برخی از هواداران بیش از دو ساعت منتظر ورود به داخل ورزشگاه بوده‌اند.
🔹
مشکلات فنی در گیت‌های گردان، بررسی‌های امنیتی اضافی و دستورالعمل‌های نادرست از سوی مسئولین برگزاری، باعث ایجاد صف‌های طولانی قبل از رویارویی اسپانیا با آرژانتین شده است.
@Sportfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451202" target="_blank">📅 21:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfbe95180.mp4?token=Dm-_i1l10WoyJBS_xyvawxrAfwFsSBCPlMSWEKrNhjfilWsZKy0kR52XRxF-XtqmYFFfafutDJTIaTgflKjzrGe7lFSxsxbX_AfXw111HGp4fu10pzq5-fantgD52hDJu0XNsRmQISPl0O2EZ7kCY-9xNnK-WE29bUuKzQgkzJkkHERFi4ICIqFHs83drNEAT8yvv-djw-XKIxS570GyfZC_VmUSlsClApvwYOjnOUhkxBthq4Qjb6sogBOhOpza1eFc9dsb4b_dmW9oB_vcAF5KxAEdVRFMFZ491ESjE0yUuwBNLwIWlmLI-bZF6dr6yjGDe2itQBeh4gV6Ty9U6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfbe95180.mp4?token=Dm-_i1l10WoyJBS_xyvawxrAfwFsSBCPlMSWEKrNhjfilWsZKy0kR52XRxF-XtqmYFFfafutDJTIaTgflKjzrGe7lFSxsxbX_AfXw111HGp4fu10pzq5-fantgD52hDJu0XNsRmQISPl0O2EZ7kCY-9xNnK-WE29bUuKzQgkzJkkHERFi4ICIqFHs83drNEAT8yvv-djw-XKIxS570GyfZC_VmUSlsClApvwYOjnOUhkxBthq4Qjb6sogBOhOpza1eFc9dsb4b_dmW9oB_vcAF5KxAEdVRFMFZ491ESjE0yUuwBNLwIWlmLI-bZF6dr6yjGDe2itQBeh4gV6Ty9U6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: آب شیرین‌کن بونجی جاسک به مدار بهره‌برداری بازگشت
🔹
نیروگاه‌های آسیب‌دیده از تجاوز دشمن در سریع‌ترین زمان تعمیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451201" target="_blank">📅 21:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31e7d7dd1.mp4?token=VstyjU50t5AqFMXbxgWf-cycBow61cwPzUWbeVPqS3XgAh4BaIwlMandHMv2thqgdv3TwArn9VGMSHjOsPkpzF9B4K2GaYKbrtdUtIbK6_N3o9tTr6cWwZJjLEm9yX-u9JXr7lxeDvOqT01tigBIarpgCFcSic9A1zcE3JfMNsSXfkRuwjo62OeinjY6FRmNZvXqq46yAG07kZnBdOUNS-uWdWVS_k_Rfa0Cnc5tKbG8pprxCcHzfWuVLgqa94ENEyeuTv3f7yysQeolgpvJa0YCjjBKHHfamonOutRlokK_lI5BTNvecOvDAAAZnEltNq5KERnEgkLsMmRUCgT-YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31e7d7dd1.mp4?token=VstyjU50t5AqFMXbxgWf-cycBow61cwPzUWbeVPqS3XgAh4BaIwlMandHMv2thqgdv3TwArn9VGMSHjOsPkpzF9B4K2GaYKbrtdUtIbK6_N3o9tTr6cWwZJjLEm9yX-u9JXr7lxeDvOqT01tigBIarpgCFcSic9A1zcE3JfMNsSXfkRuwjo62OeinjY6FRmNZvXqq46yAG07kZnBdOUNS-uWdWVS_k_Rfa0Cnc5tKbG8pprxCcHzfWuVLgqa94ENEyeuTv3f7yysQeolgpvJa0YCjjBKHHfamonOutRlokK_lI5BTNvecOvDAAAZnEltNq5KERnEgkLsMmRUCgT-YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بچه‌های ما همه سوخته بودند؛ بلااستثنا!
🔸
روایت خانوادهٔ شهدای میناب از داغی که آمریکا بر دلشان نشاند
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451200" target="_blank">📅 21:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0538e2ee.mp4?token=HE07t8fCL0caP1kDQTmVPhgTYSY5jLqmDpXoabwNeqX2lTyX4fl_w5n3FPIIo2BLBv4kQ_yqovf0REFoHZPQB0tXtKz_d61s4A018XrzNfcfoB8CJ1BruTK5b4c502o2KsUhAlHMHgYEwJ_TbMREhGBhYE1xKkGOZRHLlC_EWKzz4xh8H0Eur7gL_QF-YpVzCQffnyuPyKVOFglsw2CJmJBwL4xYUK_haWoql7c7QM_QFUfQct30no2BM5JBkYgf1tc5ISHYevlnyoKLxayKEguT7pBLACjYTTLqZQ0tYRKPZe3xNBplw1TpGsVBfU1KHl96mb5-nzPT6tSoYO5d4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0538e2ee.mp4?token=HE07t8fCL0caP1kDQTmVPhgTYSY5jLqmDpXoabwNeqX2lTyX4fl_w5n3FPIIo2BLBv4kQ_yqovf0REFoHZPQB0tXtKz_d61s4A018XrzNfcfoB8CJ1BruTK5b4c502o2KsUhAlHMHgYEwJ_TbMREhGBhYE1xKkGOZRHLlC_EWKzz4xh8H0Eur7gL_QF-YpVzCQffnyuPyKVOFglsw2CJmJBwL4xYUK_haWoql7c7QM_QFUfQct30no2BM5JBkYgf1tc5ISHYevlnyoKLxayKEguT7pBLACjYTTLqZQ0tYRKPZe3xNBplw1TpGsVBfU1KHl96mb5-nzPT6tSoYO5d4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این اتاق برای رهبر شهید، شوق انگیز بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451199" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a8cb355a.mp4?token=NRE_JUK6u9J0pb0_UhHBO270b52W1-Sys1kB915xnvgyVPrkj8f_Y4expdfiQJSqJp9zoiSnlYfWF6IfmRNEJz26o3FmgGaDyUnEHoEQpDxF2u0da5bXk72Ap2WkwTlAivTJNWJ1sj5ag1NeOAygO6C1CJ35EI9Khcz6-hkiLa7n3ZetLfrac1r8qIi6dLmhr2TPuaYCvw47tNhvDJXKpBvBm8yLqHD8-G7otoEZuDKyhgAx0b4vF16LehrWHDjpUXRKJiv83at0hSgiUsbQigmcwf_ru3psho8e0KwQXVZRCd6p-wNtjR52PjS4Cg2dB7ZQHDUwGy2o1MxhqFn5-50D-J3OjmcRjw7fdm8dQxMaJaYgHXaVMTuoT0NEb-JSAkTM8kAdopXm6uZ_AeiXJCdxBTHULhcz6ENUB44g11aGg6W2VsImDY609K1cRlLpqBUSHMOeDblcdAWXOLwhYCY3-V6vUtFLck_WHwaIKrYC80RyyWwQ-CMPxYS69hZnVkQFSRhR6FLfVjENU80S4eqBSrBpvpW3ejfN-25b3HfQdx5psGunnH6ZFUzzfMQ5WnvSmKnrkMjA9Y145pAmOfIQkAVeRH4VcDnq7sI1y2dS_3HsSoa6eXFw6DYdEnrqONSjE_f1WXXz5x9qlUo1msZ0BYd_ZW8rdCKcKtGBidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a8cb355a.mp4?token=NRE_JUK6u9J0pb0_UhHBO270b52W1-Sys1kB915xnvgyVPrkj8f_Y4expdfiQJSqJp9zoiSnlYfWF6IfmRNEJz26o3FmgGaDyUnEHoEQpDxF2u0da5bXk72Ap2WkwTlAivTJNWJ1sj5ag1NeOAygO6C1CJ35EI9Khcz6-hkiLa7n3ZetLfrac1r8qIi6dLmhr2TPuaYCvw47tNhvDJXKpBvBm8yLqHD8-G7otoEZuDKyhgAx0b4vF16LehrWHDjpUXRKJiv83at0hSgiUsbQigmcwf_ru3psho8e0KwQXVZRCd6p-wNtjR52PjS4Cg2dB7ZQHDUwGy2o1MxhqFn5-50D-J3OjmcRjw7fdm8dQxMaJaYgHXaVMTuoT0NEb-JSAkTM8kAdopXm6uZ_AeiXJCdxBTHULhcz6ENUB44g11aGg6W2VsImDY609K1cRlLpqBUSHMOeDblcdAWXOLwhYCY3-V6vUtFLck_WHwaIKrYC80RyyWwQ-CMPxYS69hZnVkQFSRhR6FLfVjENU80S4eqBSrBpvpW3ejfN-25b3HfQdx5psGunnH6ZFUzzfMQ5WnvSmKnrkMjA9Y145pAmOfIQkAVeRH4VcDnq7sI1y2dS_3HsSoa6eXFw6DYdEnrqONSjE_f1WXXz5x9qlUo1msZ0BYd_ZW8rdCKcKtGBidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف دلِ مردم عراق دربارهٔ رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451198" target="_blank">📅 21:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=YXGUwlfEBTB15tr6mtHL76fEwSlfJ7q_ctdmQ1YRMqAsUvnYCLIBTJPhOp2Zy_zEHkXK_jShzkWgqyQXKuZ5mB9IiZG1OfnC02YABRanar5Vu1DgC4Yy3rxQRjzJnHvDtPCY4i8jzc7A12fd8rRJ255tGJiZXcAWV3b9pkzmhME9fm12x0bi9enKYwkCaYf0f7QIkywa1K6SO3IpB-aYgqrIPLaGDwHA4Jhs1jrHeorOzB_yKTovn77WZjeZJztxNV6clYUrtnWLzBVT4z4j2f8tQXupvZtcALMJNKV-4IidIGYZtN97nz1FX8yEvJDWvNxoMN_2y1n_M5lVGzb9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea4ba715d.mp4?token=YXGUwlfEBTB15tr6mtHL76fEwSlfJ7q_ctdmQ1YRMqAsUvnYCLIBTJPhOp2Zy_zEHkXK_jShzkWgqyQXKuZ5mB9IiZG1OfnC02YABRanar5Vu1DgC4Yy3rxQRjzJnHvDtPCY4i8jzc7A12fd8rRJ255tGJiZXcAWV3b9pkzmhME9fm12x0bi9enKYwkCaYf0f7QIkywa1K6SO3IpB-aYgqrIPLaGDwHA4Jhs1jrHeorOzB_yKTovn77WZjeZJztxNV6clYUrtnWLzBVT4z4j2f8tQXupvZtcALMJNKV-4IidIGYZtN97nz1FX8yEvJDWvNxoMN_2y1n_M5lVGzb9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحید شمسایی: در طول تاریخ، خاک وطن را قهرمان‌های گمنام اما شریف حفظ کرده‌اند، مثل همین مرزداران جنوبی؛ ایستادن کنار شما بزرگتر از هر‌ جام و مدالی است
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451197" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=ktotWAEFUzNUt7ajStD_8zPVRhNr-cdR-eiWV7-J7X0XOr1UTeMw9RhGzDmzmV4HTAn7yY5j0_k2jgce3gQ_y7SS_sNjZr3zqXJXzUkepn6uVBSUidg40YQItp_E0Ip7G71r8zvmh6qWhd2U16_djZ_nMD-WGLSXmYTCZk5YolHi_PxNAsvqN0Oa27BqNC18V2byWCPqHguafZ-Edx8W8TXZs7oLvF1Vd9AYqAQXjDiUFN4h_hXEcyxFOY4Ym1q8X1xhjfGLIqxbs6PtgzvKMFRenpuyDsG9YRuIsWYPVmLNAIBVhPhY6ybAhrIv8QYD774WE0cGWvtOk1RsCk2o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=ktotWAEFUzNUt7ajStD_8zPVRhNr-cdR-eiWV7-J7X0XOr1UTeMw9RhGzDmzmV4HTAn7yY5j0_k2jgce3gQ_y7SS_sNjZr3zqXJXzUkepn6uVBSUidg40YQItp_E0Ip7G71r8zvmh6qWhd2U16_djZ_nMD-WGLSXmYTCZk5YolHi_PxNAsvqN0Oa27BqNC18V2byWCPqHguafZ-Edx8W8TXZs7oLvF1Vd9AYqAQXjDiUFN4h_hXEcyxFOY4Ym1q8X1xhjfGLIqxbs6PtgzvKMFRenpuyDsG9YRuIsWYPVmLNAIBVhPhY6ybAhrIv8QYD774WE0cGWvtOk1RsCk2o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از طواف پیکر امام شهید بر گرد ضریح حضرت عباس(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451196" target="_blank">📅 21:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451194">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iiy3GBgn5tXTMdg5ZxKu2UJQsZL-clmwbYpEB5pZTD96Gs5kKnCKPpkc6r8H-M-x7cyB1HtUibhyCPeP-edQT_i0ZrSRfK_4dLVd0cpNZJ4M2IQ4OtyZN7vYVvlF81iOnc6mJKgJS713uvAheFBkTP-DFlSfR3uXEf8w9C380kpQI9kJiP398fi7wbxxfUrP7wcDYufCOaQioKFReT2N9mXpKU7ZzhLV3SVAw33MOGvNIkKsJdp7yXMWeXPbaafpN_jbkNFrPKHCnySgwRnRwbSkT32p3MlPxccrVTdDwmkymFlZ694qFLuDWFr1SN3cJ-gnAjLpfWbgl_pZsNqksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9ZYyEXISSXtDqgmqHI0jVpwwXv-0MiI5Sp_T12YWAinktsNU7kXjTTH9cib-yGzoxNLUBG36K4RZd1f3-H21-njd3pkr1-CwEvH2Wxz57oye9U-Xld1Jl2kDhRgrzu6kAfgADwe8yeC84GoXrgAFNZzjfRo1sxclpb5dsf52jbZzPaN7T6RWNjIcSaemWJSi8Xwpg4UGCkB2Nwho3-xDcI8nPODISBqzNa6vVslXIz_PAVPtuHeAFYFMMA2qxrXrsXcfCo6tw_jI6uhOj3YQrvoumRoFtvcgKxOoiIVdjSiLYp-FTakQuAJtiVd6np1X3C2HtzHiHXljijseR1czg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ترکیب اسپانیا و آرژانتین برای فینال جام‌جهانی اعلام شد
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451194" target="_blank">📅 21:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChLYB8ovwnzaNlEPOaHTgssplDFuy00yE5kF9KKVd-XH2CaHZHU-dT-BguF68frYTbxJML7uvAJ9XYkOdq8SnBOP4bqNBg3eYhmhr-q4H_kGEnYrciBDc_f3O7j3ToUAv_PqsdKySkBNbMVBH-ZcppMLj_M2cNLMPLnETMYNiCMfy2uV2FxETCpkhJMktyYnSq7-TqBQIUA2_tQneBFKFTAvMvWGIu_7M9Xq6WDEf5GzXei2dibxZc08CKEq54BR5aHNaUy6m09FwwvHuuNCQ2ogXEDjOMc6LXESDtN011NC3o4KrnfqKyi_brSKxJcgxA_Lje8bIOfPkQfVBN6ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق(واع): علی‌الزیدی، نخست‌وزیر عراق آخر این هفته به تهران سفر می‌کند تا تفاهم‌نامه‌هایی برای همکاری‌های بیشتر امضا کند
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451193" target="_blank">📅 21:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d34164886.mp4?token=GNMpFnJlaKYySa8yeWEkaMfX8pygkrFbiIlO1sJcmw4lHtWgBl5eZ0erAZsgUwbRYhc11K3DkYSgco3yP88_6UvtYXX0ZN-_OfCE9NfI9lMoVCBTR6E85x2qH-zP2Mu9YPEukkFg8hbms6DTiMkaP5LfTrLZHDRUu_MsM9jEi6MPHFgWGNU_F1bYhaaX6jTdg7Xk92gOKGW3a_L3XTlPfuyu1acq_aFEs2QFAx9IYqv9SVKrKRC6MrBMwR_rMifsvzfMqILhB01Y1zTkNQ6XsfR5YQdBMT0w1flyT7Ro3pTfmqubyXw_itWCgl6WCYVXtxqU37hi5H0QKR1-S48XvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d34164886.mp4?token=GNMpFnJlaKYySa8yeWEkaMfX8pygkrFbiIlO1sJcmw4lHtWgBl5eZ0erAZsgUwbRYhc11K3DkYSgco3yP88_6UvtYXX0ZN-_OfCE9NfI9lMoVCBTR6E85x2qH-zP2Mu9YPEukkFg8hbms6DTiMkaP5LfTrLZHDRUu_MsM9jEi6MPHFgWGNU_F1bYhaaX6jTdg7Xk92gOKGW3a_L3XTlPfuyu1acq_aFEs2QFAx9IYqv9SVKrKRC6MrBMwR_rMifsvzfMqILhB01Y1zTkNQ6XsfR5YQdBMT0w1flyT7Ro3pTfmqubyXw_itWCgl6WCYVXtxqU37hi5H0QKR1-S48XvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‎قضائیه: به هیچ‌وجه نباید بدون حکم قانونی، همهٔ وسایل الکترونیکی افراد ضبط و بررسی شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451192" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451190">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430b6db9bf.mp4?token=be_I0eZY8YJfAuyJK91_Cy_9frLbTlfZgTSmg7ZrUqi7bdoo0DoReO2fiosdogz7bAQbnyrQiSqUPjqQ64Lg9kELXY4NcH7MS8GmknLhcWUEIE09VTWCTUMt7DehKNaSn8llRTxgQa8_in9HCxVNzp5OSSTgPNV815ZGio9wAgPVoo2VOon-4P3k4U9euDVlnRnatugJDejE3oOdrS7-74EqhrU4nIsaPbJhu9-OZmw7zydwlx9ZSVE5p4WQS7uhHmzyvdQG8HwnRrxuziNX-j4E7l_-eoOYNN6TUdMuToBdcgmgeeJuxnK_Qe05wvuVedx2CPAzvZl0W4cgHWeYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430b6db9bf.mp4?token=be_I0eZY8YJfAuyJK91_Cy_9frLbTlfZgTSmg7ZrUqi7bdoo0DoReO2fiosdogz7bAQbnyrQiSqUPjqQ64Lg9kELXY4NcH7MS8GmknLhcWUEIE09VTWCTUMt7DehKNaSn8llRTxgQa8_in9HCxVNzp5OSSTgPNV815ZGio9wAgPVoo2VOon-4P3k4U9euDVlnRnatugJDejE3oOdrS7-74EqhrU4nIsaPbJhu9-OZmw7zydwlx9ZSVE5p4WQS7uhHmzyvdQG8HwnRrxuziNX-j4E7l_-eoOYNN6TUdMuToBdcgmgeeJuxnK_Qe05wvuVedx2CPAzvZl0W4cgHWeYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضایی که نماد بدعهدی آمریکا شد
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451190" target="_blank">📅 21:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451189">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e321f95076.mp4?token=W-VpXQsWi41mZAzDAj0LKmq9iMcG6REH4uX-wvDPwBr0JUIgprXCIbZwE9mo2CobWAaXPDiw2-IEQanBIrIaw_2cuCPsXiGKLbY5_pwUEPWcuKgmJKIzXSr2S3GumqxguRNpHzOTfVwBZBnCABdHgLaiCIG3dE7QtS-0W6uNinv_vwLptWnTjc8hYn1flJXoi9R1aAKWvZLbyIv1p5glDDsfENRpQi8RpPKJwpg7Dn3H60AUm06xw2-11Sh6mVBPFB96yUswrFfUns6BPaO0ZEMLRpkzhKRzFsiRSpC25rkYupfGpuj2Cu2jvGWSWtmBfr1hy4zLmUx3r3MfjoWDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e321f95076.mp4?token=W-VpXQsWi41mZAzDAj0LKmq9iMcG6REH4uX-wvDPwBr0JUIgprXCIbZwE9mo2CobWAaXPDiw2-IEQanBIrIaw_2cuCPsXiGKLbY5_pwUEPWcuKgmJKIzXSr2S3GumqxguRNpHzOTfVwBZBnCABdHgLaiCIG3dE7QtS-0W6uNinv_vwLptWnTjc8hYn1flJXoi9R1aAKWvZLbyIv1p5glDDsfENRpQi8RpPKJwpg7Dn3H60AUm06xw2-11Sh6mVBPFB96yUswrFfUns6BPaO0ZEMLRpkzhKRzFsiRSpC25rkYupfGpuj2Cu2jvGWSWtmBfr1hy4zLmUx3r3MfjoWDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ۲ نفر از عوامل بی‌رحم جنایات میدان شهید علیخانی اصفهان به دار مجازات آویخته شدند
🔹
قوه‌قضائیه اعلام کرد: حکم اعدام عرفان اسفندیاری و گل‌محمد محمدی، ۲ تن از عوامل بسیار خشن و بی‌رحم جنایات میدان شهید علیخانی اصفهان در کودتای دی‌ماه، بامداد امروز اجرا شد.…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451189" target="_blank">📅 21:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451186">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d20f8910.mp4?token=ga_LNhVhw5KsJ-uPF0w2Ro9NMKEyjug9FfedRsZxnTiYeNFKY1i4LOQ7Qp2dC7-W-HXjdkvRtGGMTJVsI_1E8qfAUwP9wj74X9ZdK4IxQ2TQvrsR1kAV3ajrU93zH7Lkp-pjdBGyFZEYb6Vo26d2eqV8trcmdkniYfod_8fp1ARSKG3Aaie35bQc8-4Gg385WBQTWPGby1arbY0JEUdpZQtPevsRRKAPrsQC5Hd5-7kxJ4wahng-Ot1T22zjcXJvGLtBXe74pVQ465tELGs4F6QyssCxxALozCNBL8j-mDxhwFZtqiGDCSZyFAuViVyeoOj1sjD78B8k2XHcwXKuZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d20f8910.mp4?token=ga_LNhVhw5KsJ-uPF0w2Ro9NMKEyjug9FfedRsZxnTiYeNFKY1i4LOQ7Qp2dC7-W-HXjdkvRtGGMTJVsI_1E8qfAUwP9wj74X9ZdK4IxQ2TQvrsR1kAV3ajrU93zH7Lkp-pjdBGyFZEYb6Vo26d2eqV8trcmdkniYfod_8fp1ARSKG3Aaie35bQc8-4Gg385WBQTWPGby1arbY0JEUdpZQtPevsRRKAPrsQC5Hd5-7kxJ4wahng-Ot1T22zjcXJvGLtBXe74pVQ465tELGs4F6QyssCxxALozCNBL8j-mDxhwFZtqiGDCSZyFAuViVyeoOj1sjD78B8k2XHcwXKuZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندرعباس، ۱۴۱ شب خسته نشد
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451186" target="_blank">📅 20:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451185">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
منابع خبری می‌گویند چند هواپیمای سوخت‌رسان آمریکا در این فرودگاه مستقر بوده است.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451185" target="_blank">📅 20:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451184">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d153b0845.mp4?token=s5JWrDewBocvKdsvKHSAk83F8D9zRE6rGdJCDwDLg-Cy3a05LM2HTQ4TqAdT_lB6EPC3V3o7uSrKz9vw_izT6NdaBzbbb5lozzcpX26uUNcvp8hoMUvqz3YTV1rBMOIcADLE--pLi0VS-_Cj5Hkh1Yieyg9qsPoLCxOWJCN6frqJCVL73CT2fU7odIzLx3vsfkjRmTw86yheKEUs7R7lz4OHjXXvhNNaAuk7rq6FMgfgCjvU9SayRyK832ESonRkj4v6EGHaKNP1sLrfB2Uq1Irk5Keou6PIWbzI2EmQRycZwTom89I2bpGXV3aQuIfHLuW5T80PszmddOt0eK3I7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d153b0845.mp4?token=s5JWrDewBocvKdsvKHSAk83F8D9zRE6rGdJCDwDLg-Cy3a05LM2HTQ4TqAdT_lB6EPC3V3o7uSrKz9vw_izT6NdaBzbbb5lozzcpX26uUNcvp8hoMUvqz3YTV1rBMOIcADLE--pLi0VS-_Cj5Hkh1Yieyg9qsPoLCxOWJCN6frqJCVL73CT2fU7odIzLx3vsfkjRmTw86yheKEUs7R7lz4OHjXXvhNNaAuk7rq6FMgfgCjvU9SayRyK832ESonRkj4v6EGHaKNP1sLrfB2Uq1Irk5Keou6PIWbzI2EmQRycZwTom89I2bpGXV3aQuIfHLuW5T80PszmddOt0eK3I7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتش این‌گونه پایگاه‌های آمریکا را زیر ضرب برد
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451184" target="_blank">📅 20:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE6EIQ-wyr-2S_o6B-b6ZWcT8kT7gsbxXUDDtZqlUH0hO6YmJzP-vi1uuoA-sjYe5iv2dDiVY0nPCDPJa5I-CzKtM3iloN_kMnxP20p2udQCPkq0Hq5LCUFJ5FBlmoe6ta-ukZtEErPhUZURPxFFUoDG2zh6TcXiVteWt-YJI9p7_i0tBYyc-4mCTd-juxjNE8FcX_8RqlufU7zFaZwxIjjUBOJARrt7LBYrA4ANyX6A7cKxWTgL98Z07jdpofdJdDYXOxZDtjinlksRbeAh7_HRrTHkKHltLvV_IHRkGQOi5qxI_Hn8JkXuLA6d7lXgjpu6UYCp7Oz1rOLBG0KQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLi7vu_JlWjIqLXBJnTLATb8ejWls1KnVx0PD7h24uePzqqtbbGRUnxUyENAIimb1z_gUEE520QW5YhF3QoCG-_4Q4un9DMevU9akdlbumeR-25rqIG8N3rdL6OukK3zTTvoU_oeux3lJTqpbpifJ6jvLlvN4zRT_uU7lPsQzNTc3FLvOUGuFzemsUBK5ASHr3TCQM2btK-euEkcMYiXQ4YDUFISN-aBBPTXb6HHdqyunc5u1s3QUi0HXfzeHQvD6w5f4js6mjQXso21nLVtGHusoeVNEDBtDuML4G9JVOa_snj2hXCCdRU7A0VWmX4kg3K5RBiK3WNr0nQojzWbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cy66lxQLvZN9IVTAbIA2VGeq4LFDacwUSu3WF3fo7FqoAEDsfJUrJ2tGvvtsdbQuzMTy6FJ33G8ie8nHZDlw7VF0S7o3aoH0z9oYVwK9p6iXCYvruicEuVUA4yhgVWM3s5kqRVrKRnx-fZf3g9rmxmtac5ole_rFOBpj5L8c8GKdET0MCEYAKcuRbPEaLC2EbYBmq2J69ZYJqTOkGcXYv8lUOrHp7uBFdN5m-jkOqTnP9j3mq67FsJOVAzKGe0DYW0wv-md45qXximAW_aukzqDlkAe1Qp33XHi2etQMRsT8uwBr5O-7e-mcdY4-l-O1xSpA17UxFJxJNsl4Y_srtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMupx-u2-YuFCO-ioRLzsoxIvAMW20_Awu9OF7av9gDI60KCAB5wLrxh-HzuI5VhlgG2cuJg7ifExecwkk3dNGlQ5Wdx7e2m-1ET8bZ1OqsABFxTz8RIqYMdW9W7awBM9x2KYv6Y5BwONgkXN2-CVrMDLQJ72G8xuDMc-vMmfsWySiRmrNuY1_Soc-h4ZGLlIDgGh34fb_3m99RRZqsXrhwv58K8tCtytJs26ftPWstGkiDYSSoxzgtf78kzVw5IkeUoYs0Y5W8eRKWLIMmiJZngqtaORVStBj4T5MrapVy9K9xUQs4-BqsTVoOBN3_yjQHp1Fu0bFwqbtJSYfw-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWW6WX_qKjuoH-XhOwg2VZLC9n6qStGg0TqSzrabw_E0-JUUPc4u2QFD08_pcWIQkuKaViDuYEVEKmli5bpbid8163Sh8Q5RkO_H0rqltmiJ5BU5J6DLMzRoZ8-c6gTeTlUTbCgRp4eRRjL8UMGyz_SN6B7_M_cgR7xpYv4fipsbq8jc2QgF0BgW9aJEr05aIPUFIcCI6OeA736quDCquN6HoB1488a5y2Vj9nwz5GEKp3fkQhOQylzMF7Khs960zOiww8BIP5qxkXb80SCII1JD4UjsBAuZazcfiaIBIswWH3uLPDp-gYy7KvJvTl_Na2Bq2T3tTQgXWrKlh2WY4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قلک‌های کودکان یزدی نذر زائران اربعین شد
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451179" target="_blank">📅 20:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451178">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUrt1ZK17FXmB9wKzhcCuCcxMg6oti9mZAkjNtNhhRWh1qHEjFmag1nPCzXfEGrWhWWLbSiXRpwNBwUDONI3Xb6PJJM10Mn7DZA1KLpIOKLSvbMOkvfo8WIlgyePz19FEYBI6b8VjrsrtA5ob_Ob7OYrc1qWR_icJtEs6KcmjQA5NNCMB-Xv5L_C3Bnw5J92XV7XrSrgqDHUjsj5nKDYM76jb7W3COy8s4oMRu4IKBD2RtLIyvGag0R4NL6beAceHRADa3Q7RapLiORFkNBeqLYrUo4kDyrye1lGC86hgwZY3azRS4HXQ9BNasbwdhNWxh44lQdxlR6g2QoNLf2Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایزدی: پیام اخیر رهبر انقلاب باید پایان توهم اعتماد به آمریکا باشد
🔹
از ابتدای انقلاب، تفاهمنامه الجزایر را اگر نگاه کنید، بند یکش آمریکایی‌ها در سطح رئیس‌جمهور تعهد می‌کنند که در امور داخلی ایران دخالت نکنند. اما یک روز هم به آن تعهد خود پایبند نبودند. این سبک آمریکایی، هم قبل از ترامپ بوده و هم بعد از ترامپ خواهد بود.‌
🔹
پیام دیروز مقام معظم رهبری پیام مهمی بود. انشاءالله بعد از این پیام، دیگر اگر دوباره صحبت از مذاکره شود، کسی در کشور گول نخورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451178" target="_blank">📅 20:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451177">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزارت خارجۀ اردن خبر داد که کاردار سفارت ایران در «امان» را احضار کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451177" target="_blank">📅 20:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451176">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da94f714db.mp4?token=vQqrbZCQmDLf7CB0WyAyObSmsABOcoqIfgv7prUrxLvsiptzOPLtpd62vbtk5rYW3-hUWjVrUZfGbwJQobxfsT7urGaRJtjEzlQ6I351Ws0nrv62TKo1s8CtSUArwypvl0Enxq3t93fgJVdrxvW61OO-0tCNUwjvcFP08zPYxmcyef-sP6dbLIsBUhT_m5-rExKWXVmPKIbm-FUcNLjfEd4mM1V2eGwHBKzbHnrqpyQoibep4m8SUbt97vG5RaqegHb7D012bk0NZ_jq94uuBDTjYnEnLMzna6aA2acnNLNiHOFvfXAhUTgy_w4kBs0Aj8ZVCRE9bku4Ahx5nZdKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da94f714db.mp4?token=vQqrbZCQmDLf7CB0WyAyObSmsABOcoqIfgv7prUrxLvsiptzOPLtpd62vbtk5rYW3-hUWjVrUZfGbwJQobxfsT7urGaRJtjEzlQ6I351Ws0nrv62TKo1s8CtSUArwypvl0Enxq3t93fgJVdrxvW61OO-0tCNUwjvcFP08zPYxmcyef-sP6dbLIsBUhT_m5-rExKWXVmPKIbm-FUcNLjfEd4mM1V2eGwHBKzbHnrqpyQoibep4m8SUbt97vG5RaqegHb7D012bk0NZ_jq94uuBDTjYnEnLMzna6aA2acnNLNiHOFvfXAhUTgy_w4kBs0Aj8ZVCRE9bku4Ahx5nZdKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید بشیر حسینی در مناطق مرزی جنوب کشور: هر نقطه‌ای که نیاز باشد، همان‌جا محل ایستادگی ماست
@Farsnart</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451176" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451175">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۸.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/451175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۹۷.pdf</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451175" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzvV4bHHBUdvvwJbxpqUmwfXH6sc1RyZmM0wPf5MKi1N3RLd3i9awm3oV4oa-pBHlcXMzC0DZPS9YMjyYqVPYCUUXrn-mnUv9vMeujxy3FPFunuYIYG-pnoNgfbDLs5YLkXDHmZciZLT1ZCZdeWtWjZ2Lk5hjgcPdGmhCSc9esScBeWIo9VKYRSv8NNXjVLolKkpPFBH_XxNbhsShXuAr0y_gu-iIqIAoRsYr1Fnxk-yRsfoNS1ZO26qhxGoQWHqRSzat7yCQJ-mDDvN87Ota8EV1vt4-u9aAKyiSaqnG7iNFsnFTkgrSqfoaOU4TQl5hFph3mw8f4rMXzEs9R2OjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCThbSTCtxAo8MvpSDO5C88Tg5CKdeqfJ8o65tSm8JJ_lFuBvI618W6alwmbZVdnaG9QYzBdodUZtGzUrj3lTcu3ybUkWpCmFI5a8O0m2AktIDv1pDfCqLkmrs51nvqSwJcnLYT_FeoNrWl1AVbBjdSMYdtGMNRmOERRXnAURqT2lX22co6-2heYAbaUIO9EdbWDMzqatIwyu80CFNxG6I7NQuLeQmSlJsfm9qZmmGbNJg3g3fxtQirlCsXn82Rn4GQIJiOT_iIgPE57DcmuJkU0Q7GxvPpxJjmm8KL9T95TMJ8gaNk0jOxSbQu5zX2SDMmX05h5LXUGiB1GfKQNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tk2SYkyP7K8QBe5zEz_JQVwdy1hq8jIGKj6-KGTB98qmq3KaGfeBpjCH2Y8v-r3GNVjatL9HTDYzh3biEkxbqgxDe9AsyyerYw741TsIa-vrq7SYikT373qNxEjWGhNHFOfZY-quc1dL9BxcmzQCythDYZcRbbftnxYyUf0QGlwkQkOhOuwVpJ3Gn8C-NpOXaYbdUREeW9cInqTbD3b7sTydQ8Kc-XuQECroseVOZGGKIlq-ieR5TQunbCygxJfwS5w4e3YhbHR5LhdEidjZWr8T4cxXHgLgni02gF12UqiTCpw2kW6RzXaIb2W5FrpcZ_aizmQZLw5llH90iXcM4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انهدام یک فروند موشک کروز دشمن متجاوز در منطقه غرب کشور
🔹
روابط‌عمومی ارتش: ساعاتی قبل یک فروند موشک کروز  دشمن متجاوز آمریکایی، با رهگیری و شلیک موفق سامانه نیروی پدافند هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی در منطقه غرب کشور مورد اصابت قرار گرفت و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451172" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451170">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXOYpHpzbQ7ZaDh10e0sfPyq-uZz0Akpb0pyQbBFCJ89nImibePbstOZ2ofxbopmwGWJEOMWJqjJ--HL7o8-bl0WgNRSyncS8jrly7nPEzFhk-njLCZhnT72UzT-JyN4bKuEbIkMn0QeompB-RfXHxvaJcfZ7sckVfSgdERF3qV0yXJQjFuBFNx4nYeaCO3F6r9BtnwYfY7liPYnaIN5iIagSAmANtMg49qk0ZJhzoEGm6yL0MXaoqoashvASzwLYr0sQjQBWsZZMG8DZdx4DN4DJXOkJyv83RBcCbOsSNvtw9W4wWfLOI1vY4DWBSfYL4aTYdYu05fKJqgtTnq3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNX2yn-rPx1HjiX6X0I2I_DJ_4auDIEAOVtiIhyOKaBmdVOdHSlVtJ56mYzoRhhLj7glmLu2JK6GGWfy2y6u20Kl63eX9RBB3hXf2o_CGk_rFCuvoo5OfH-Jnc-MeHhb4d-ke30u0B-yAoRhekzFmz-sID6PvYHs1Ov6GyQyDfcVumEhSwP5Le7_U1XSa_ZbO1P5z3Rzk8hCqPogNz0Mz41aoSymsy4eyDtS5ig1VIqWl3WVfxa96bJKXC6GqBRrWt_UA35idtqrguo__I9PNQlfCJXXhHPjeEsNZgNPiPAxIYjHqsvNnO18BeminhSX45x-OEye4azpVpzjZPl_sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیابان‌ها توسط آرژانتینی‌ها تسخیر شدند
🇦🇷
🔥
خروش هواداران آرژانتین در خیابان‌ها پیش از بازی مقابل اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451170" target="_blank">📅 20:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451168">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568a93e9b7.mp4?token=ttZ7gW6ToyMEgxirt4YqZy8uD_1YwIyo5tZw8HrunvP0EYVbQ_dXig0EP6fT6Di46tkQWeiXqGnZyC1Vz3ZFoNLheg2GU7XHpOOC9UhYQslS2D4FLG_fdRmFZkzE3kIjsvsSeNBg96xCnfUqeKw0fGuNQsZjcDwIATwRdWsNEGxWVDwhzJNVZUimSwo5HPycyLBk4EP5R9ukSsDZ2kzLT9axY3fNrViCGNj1HuoxNvJwkIkDUY0yzZK8dPjptvF6BLji4XkpKdhfLjAUYGpso6L6i-0IdgWzqKWHoEr0aidRnuHck1N9KDUFzuYdEDvP2OKqd5pCYzIl9fe2o0vDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568a93e9b7.mp4?token=ttZ7gW6ToyMEgxirt4YqZy8uD_1YwIyo5tZw8HrunvP0EYVbQ_dXig0EP6fT6Di46tkQWeiXqGnZyC1Vz3ZFoNLheg2GU7XHpOOC9UhYQslS2D4FLG_fdRmFZkzE3kIjsvsSeNBg96xCnfUqeKw0fGuNQsZjcDwIATwRdWsNEGxWVDwhzJNVZUimSwo5HPycyLBk4EP5R9ukSsDZ2kzLT9axY3fNrViCGNj1HuoxNvJwkIkDUY0yzZK8dPjptvF6BLji4XkpKdhfLjAUYGpso6L6i-0IdgWzqKWHoEr0aidRnuHck1N9KDUFzuYdEDvP2OKqd5pCYzIl9fe2o0vDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ کره‌شمالی در دیدار با پوتین: تا دستیابی به پیروزی نهایی در کنار روسیه خواهیم ماند
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451168" target="_blank">📅 20:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451167">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6662bf6af9.mp4?token=BAseufjoUxXtYOFoH_ihCheUgnEM9RoOyFqj1W09DNyThtnuaiaAEUjxhUimQ4vXiVsXxTdyzlkEP_Q_8Q9aTbrZXxZ_Kai_LRmtzSozpTFWAXhCbTh__c4Z_U9cSp3F4PKo5ZibnsrfMPMepEauIqIx-uOlIOuKUKXnaAOmkYZfVVD6USls0MHBfuTxw_fcd96xdBwmLUrV5SEHQbaZ9K1fv-_mjKvRotA93oUT2sotAfBM_W-i0uoRLb2Y8eLTidXs-aPZr-qXismQy8Ge9MqZZvrt1SzIMVdBO1UbBuRYBiDWsFrzoRrn1Wf2gpL1lKsaJLVHzOT2Nl0_ZM-FFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6662bf6af9.mp4?token=BAseufjoUxXtYOFoH_ihCheUgnEM9RoOyFqj1W09DNyThtnuaiaAEUjxhUimQ4vXiVsXxTdyzlkEP_Q_8Q9aTbrZXxZ_Kai_LRmtzSozpTFWAXhCbTh__c4Z_U9cSp3F4PKo5ZibnsrfMPMepEauIqIx-uOlIOuKUKXnaAOmkYZfVVD6USls0MHBfuTxw_fcd96xdBwmLUrV5SEHQbaZ9K1fv-_mjKvRotA93oUT2sotAfBM_W-i0uoRLb2Y8eLTidXs-aPZr-qXismQy8Ge9MqZZvrt1SzIMVdBO1UbBuRYBiDWsFrzoRrn1Wf2gpL1lKsaJLVHzOT2Nl0_ZM-FFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار! چاه‌های نفت را دریابید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451167" target="_blank">📅 20:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451166">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f03328b8b.mp4?token=psZInWBj00sTjXh8ubJKUvA1TseDEY-h-a2A-qjUFhzY1EBnYoyswtu3TbDDByStmgqDLDfysfiNyx9jUnuAYPJxXCLDyCUCvgXIiBRbkcn6RCJOtByDk_PS2ItMe0ePzeuRu_qOpt0Scu329PQ-f7Apv5kiCOQs2V6fdxBpgdlmAZmUIRJOCX-MT4vhWKcHFqgbrzokix7Ny7SCwqGmA4bi5gTJvIceK5WxeaJVw81hUgAqaAKX35VEuPsQ-yVbhhEXfEzaeSWTzx2vAkxfMO3J27-m2IEHMgY4SrIQPciGM-PLLe3tVZkMIWr52mYbaMr2OmAPu82BBSIML2i6vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f03328b8b.mp4?token=psZInWBj00sTjXh8ubJKUvA1TseDEY-h-a2A-qjUFhzY1EBnYoyswtu3TbDDByStmgqDLDfysfiNyx9jUnuAYPJxXCLDyCUCvgXIiBRbkcn6RCJOtByDk_PS2ItMe0ePzeuRu_qOpt0Scu329PQ-f7Apv5kiCOQs2V6fdxBpgdlmAZmUIRJOCX-MT4vhWKcHFqgbrzokix7Ny7SCwqGmA4bi5gTJvIceK5WxeaJVw81hUgAqaAKX35VEuPsQ-yVbhhEXfEzaeSWTzx2vAkxfMO3J27-m2IEHMgY4SrIQPciGM-PLLe3tVZkMIWr52mYbaMr2OmAPu82BBSIML2i6vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از اردوگاه منهدم شده تروریست‌ها در شمال عراق
🔹
شبکه خبری المیادین تصاویری از یک اردوگاه متعلق به تروریست‌های تجزیه‌طلب ضدایرانی منتشر کرد که در حملات موشکی نیروهای مسلح کشورمان به سلیمانیه عراق، به آتش کشیده شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451166" target="_blank">📅 19:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ief53_xHSjTNkWS055cvWzxz5SaLx95JeyzyZyrBKdChNBwJ8_CECGX8tVW8cjzvACb7_69cFkWdRdwFoPAQxSF_p1tkPJdCo5a0l2T6WVSyt9Dg_3ob8MdKm_wOSrEwdHgHqiiZmF6vpX-H5COmvtyOZ452qVRFOv5_S7oiGY8fue_CInqGj_VtY2MfpieVKVKdFiQDb-BqS-HH9v1IifkvYFlykcDkkVOZwPEkvt6H5UDZ9Ckp3jjOxjmjA10fe0xygV_LXClzworHU9DScaKR7WkXKoUr_JFjsKnDmqVYpVBHzci9hOex1GEXIhoXtvcH8y0MQ33olxpHs3Wgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTzJVTWgiFC62hRt6LyIq8DoNDviAOKJG81_-Df5_BAZBohir94DT8ShlpGM0BwkSiaux45hKqUtNgTGDhnhO-aygNhRvqaHxl_-EDA7qlB3tEoHkpgHH_3UmqORm2iGEEnozCy5iQ63OGpOO5XHN5pFQWWwZo7xWKqgdUEmFtuwisNv7zIm8Wzzt-T0fWIAgiLbm5CkDPL3CFu0WAS1h0aCZeXfn8zuwTNw2e1MJ8uksUP8FmLGR5lCSQl5zZSbzcWHS7SZUF4HgHJXW9n8pukQFbGXK_IUR5O36aT3PpJAk_cpDGCmqeJ2KEkyiL0hCskz_XiuQFKY_ysG1xQbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icFfh9QCIVdHYXl3VB-K8yWWxnnkLtsvJNpmsR3LaFVKDq04F1Cew5p2Eob48Y-UHhC94-suXoY6dVvBLt7ozNbrMSMvhh5EH6a6XYroW0Q-dgKLvKFekBrdS7uw89CLWKMg_tyt5AhRC2mTV1RSGhOhC50WHZBrNtTfSdEUcHQm1q9Iqu9-PxQcMWrEG8JSqhHNY-OtpJ_D-ObKKRxYvRro15lhwDtDA8-3g2W7NKAUrPv6IsmbJQMNyxqE_dQRwOdye8L6fKpTCo5Upy6XYZcTSmJK8CrhASwH_G9psbEOp3P2c1-6an5r0yNpBN806DisaBC38qJnws7ZQ-wSbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بلایی که بر سر انبار لجستیکی آمریکا در العدید قطر آمد
🔹
تصاویر ماهواره‌ای از انهدام انبار مرکزی قطعات لجستیکی نیروی هوایی آمریکا در پایگاه هوایی العدید قطر. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451163" target="_blank">📅 19:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfFSqjjWkzvRS3L05-Omy0MKGxkTzSAh-J2VWLdAJSJGMAC17_3ZhaLKw6N5DW_BL5h50T3EiFp_jtoN6Hz3AuGZoeKTMr6sL-sN8mKZBL39UaRdTbzWx5o1R5X1OKl2l-TrOnOblgYibnlsGxQd46AmpE4KtM-IovCc4ns-5cvBw5LkmtCYmT0GU6l5PLnH-BXCer9lrGifwN2b8q4wXzmrPQbgj_F42Fo91yIkn3vJNv5-pXf1-XZP4-HEuG9PBtlre-wyooH8BiQWL4YK3qZzql-cbnz0mjMot7vsLyeWuTTlQLhxGhQr90GbQ44HNL5l7sEGYpH_m4T0--ZGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار پهپاد جاسوسی دشمن در جنوب کشور
🔹
یک پهپاد جاسوسی متخاصم بامداد امروز توسط رزمندگان تیپ ۴۸ فتح استان کهگیلویه‌وبویراحمد در مناطق عملیاتی جنوب کشور مورد هدف قرار گرفت و به طور سالم بر زمین فرو آمد.
🔹
این پهپاد در حال شناسایی و جاسوسی از مناطق عملیاتی جنوب کشور بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451162" target="_blank">📅 19:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پشت‌پردۀ روایت «ضدجنگ»؛ بازسازی یک دوقطبی انتخاباتی
🔹
در روزهای اخیر، برخی چهره‌ها و رسانه‌های نزدیک به جریان اصلاح‌طلب، با ادبیات مشابهی بر «ضدجنگ» بودن خود تأکی و در مقابل، تلاش کرده‌اند رقبای سیاسی را به «جنگ‌طلبی» متهم کنند.
🔹
در نگاه اول، این موضع جذاب به نظر می‌رسد؛ چراکه هیچ ایرانی خواهان جنگ نیست. اما با اندکی دقت روشن می‌شود مسئله اصلی، دفاع از صلح نیست؛ بلکه ساختن یک دوگانۀ سیاسی است؛ دوگانه‌ای که یک طرف آن «طرفدار صلح» و طرف دیگر آن «جنگ‌طلب» معرفی می‌شود.
جنگ‌طلب کجاست؟
🔹
نخستین سؤال این است که اساساً چه کسی در ایران از جنگ حمایت کرده است؟ اختلاف موجود، میان «طرفداران جنگ» و «مخالفان جنگ» نیست؛ بلکه دربارۀ چگونگی جلوگیری از جنگ است.
🔹
یک دیدگاه معتقد است بازدارندگی، قدرت دفاعی و افزایش هزینه تجاوز، احتمال جنگ را کاهش می‌دهد و دیدگاه دیگر سازش و کرنش کردن در مقابل دشمن را دنبال می‌کند. تبدیل این اختلاف راهبردی به دوگانه «صلح یا جنگ»، بیش از آنکه یک تحلیل باشد، یک تکنیک سیاسی برای برچسب‌زدن به رقیب است.
تکرار همان روایت انتخاباتی
🔹
این نخستین‌بار نیست که چنین دوگانه‌ای ساخته می‌شود. سال‌هاست که در بزنگاه‌های سیاسی، این پیام از سوی جریان موسم به اصلاحات به جامعه القا می‌شود که اگر رقیب روی کار بیاید، جنگ خواهد شد.
🔹
اکنون نیز همان روایت با ادبیاتی تازه تکرار می‌شود؛ با این تفاوت که کشور تجربه دو  جنگ در دورۀ مدیریت اصلاح‌طلبان را پشت سر گذاشته است.
🔹
منتقدان این رویکرد معتقدند به‌جای پاسخگویی دربارۀ کارآمدی تحلیل‌های گذشته، اکنون تلاش می‌شود با بازسازی همان دوقطبی قدیمی، مسئولیت‌ها به سمت رقیب منتقل شود و فضای سیاسی دوباره حول همان ترس شکل بگیرد.
تجربه تاریخی چه می‌گوید؟
🔹
واقعیت‌های تاریخی نیز این روایت را تأیید نمی‌کند.
در دوره‌ای که دولت وقت شعار «گفت‌وگوی تمدن‌ها» را به عنوان راهبرد سیاست خارجی مطرح می‌کرد، رئیس‌جمهور آمریکا، ایران را در کنار عراق و کره‌شمالی در فهرست «محور شرارت» قرار داد؛ و بیشترین تحریم‌ها و تهدیدها در زمانی انجام شد که سیاست دولت‌های ما مذاکره منفعلانه با دشمن بود.
🔹
تجربه‌های اخیر نیز نشان داده است که حملات آمریکا دقیقا در مقاطعی انجام شد که ما در پای میز مذاکره بودیم و حتی بسیاری از درخواست های نامشروع او را از جمله تحویل ذخایر اورانیوم را پیش از جنگ رمضان پذیرفته بودیم.
بازدارندگی؛ نقطه‌ای که حذف می‌شود
🔹
آنچه در این فضاسازی کمتر دربارۀ آن سخن گفته می‌شود، مفهوم بازدارندگی است.
🔸
تقویت توان دفاعی، قدرت موشکی یا کنترل تنگه هرمز و سایر مؤلفه‌های اقتدار ملی، به معنای علاقه به جنگ نیست؛ بلکه بر اساس ادبیات راهبردی، ابزار جلوگیری از جنگ است.
🔹
وقتی این واقعیت نادیده گرفته شود و دفاع از بازدارندگی با عنوان «جنگ‌طلبی» معرفی شود، در عمل یکی از مهم‌ترین مؤلفه‌های امنیت ملی از فضای گفت‌وگو حذف خواهد شد.
🔹
شعار «ضدجنگ» زمانی معنا دارد که با یک تحلیل واقع‌بینانه از عوامل بازدارنده جنگ همراه باشد.
🔹
اما اگر این شعار به ابزاری برای دوگانه‌سازی
سیاسی، برچسب‌زدن به رقبا و بازتولید همان روایت‌های انتخاباتی گذشته تبدیل شود، دیگر نمی‌توان آن را صرفاً یک موضع صلح‌طلبانه دانست.
🔹
آنچه امروز کشور بیش از هر چیز به آن نیاز دارد، تقویت انسجام داخلی، حفظ قدرت بازدارندگی و پرهیز از دوقطبی‌هایی است که می‌تواند هم افکار عمومی را دچار خطای محاسباتی کند و هم پیام‌های نادرستی به طرف مقابل مخابره کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451161" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451159">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXYTIn6yl8Nyk6f_yINuerpjv8tTVKsoZ2dvk73eGa-JZqNaZ0XObauYw7zIrGNhziQo7bAClClSbJqfwHW_0OwBqsF0YYMfzTVihgUHEHFj7nLrfbJOEOyojcMSHY-WvcDxueybM_3XRoqKl44aKKdfEFAopwd6f8RX62ttyYI9foPGPdcEflM6mLbcATIQtC9cZEa5W9uhvmqfdCVaq9W3FZ5nxuWaXrrDoAjJYprlzgeeq1zkW78k6Gl9aphMG0RBKMi8fHTdqSUpgGveUdf0WBY_mwZq_M-LQs4FSo13D0bcV6-v_Jv9XDR6tLuhTO3skb5Xaqo7gA3O6DWozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gae8B8REBhq496Hy5J7Zo0XuqH-cCKuCE-Uj7mkvp0_g0ZKNp_U4595gt6XAZvo9liqmA_IljH5cZCa7r95gNbC0MukO9oDXWGtpvueye5fwFZEwJQaSo3qin8AcOg3MNuH2Mnsst3s448XOdmioupmciz-CZU10dca-7oBHPvz7Xqa8QDzPJDxG_lXZXOb-ywQw28SvdPLUJMAgPHM3ou7SAKYi8tnd5sRPwe5fwJ83JYsA92VSqlZiICuEa5ny2VwOlYRAC09ELJnXxLzynyDYl9i8CbKiyPJs5kvRDFhc-zQIaIsQJI-kZ4Cw42iGwG7LLYzl8L5k0xeg-RmCHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌   سپاه: سامانه راداری برد بلند و چندین فروند هواپیمای راهبردی سوخت‌رسان آمریکا منهدم گردید
🔹
سپاه پاسداران: در تکمیل عملیات مقابله به مثل شب گذشته رزمندگان غیور نیروی پرافتخار هوافضای سپاه، در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" و…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451159" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AniKjaGlKQyb67CjKZOUf64JpsAxjPjAb9L4bf8fqdnb0_o73lEon-ONuTxW-VY0GeCJeOUDrZDwhdUaGqHw5AsQZCEq0-JjUxsEHYayujCcsF48qZKYXKgs3asJiU2Vx8Fm-gqBqlWyE7SzHRXWC823INgQdPr7a7GOyiVSXWVk14KTQdjKwVouTV9axVPkC1MoP3aQ8Xce4dzaJ0jXboS51Sh0KsRyImbdp_c1bgMBPt-aUDZPpoOTx9-DBamtvaPC3tYPOHzHjX3U-4dUH-jP0tvRNdHMrZ53pVva7hodpsq6jo3RBBEo68Lg1-JSncEd86Htfxx_cumo_6wM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9lcDx_J8rEao9OXRjqbJrwDxGg96x4zenxfxFsTWUZBdDq2FtNKOg0fD4_y5wBgoKCEc2ZFePhzGg9AeMLZE-PVtx7yvb76mXzZZqUarA2fDrDjx6k8Vj9EK8HAMDaf2JzbDRnFRi4P-Q6ILRpuarVWa2wtW1950QMwHnOaxBPw-s9Tog20VQmGrSqXM9eRff-fXup-vuBuDYqcPi8z2xq5JejbrelpCg3G7eQPGF0Q40UTJBYqT6I3nTaV-c_drtK9qCNDan7PL325w0sijoIhKROrqe5szI45B52ymUhBZ_6Wx7yoWD_jOmQGlpB3Kj1SEPKbJOlHXgwpA_gzRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همچنین مرکز اصلی هوش مصنوعی بحرین که در هدف‌یابی دشمن برای ارتکاب جنایات جنگی مورد استفاده شیطان بزرگ قرار می‌گرفت با چندین موشک بالستیک و بیش از ده‌ها فروند پهپاد به طور کامل تخریب شد.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451157" target="_blank">📅 19:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451153">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dba6c54c.mp4?token=GxvQyvHrCHLAO0RI62tZe5vdRvCz0RaGLiwNfA1hCpejUiw66hLmWWGb2E8OydEWJtvX3BFneGjcWBQ35-rL5zGFHltVHWAQsTaQ8ZJHS6Ns9BmlcwFiH0aWx6igBN2xNo_deIETTXLo9u4gzLQD_rBxRctjFV89hBVfzzBMfDq46JKXMXQxUODycH0k14JHd-LjKZRjwX80VemnLRplbu-UbAUdb_bEygU21nFUgxRI9S55DNZrCI7DN01a-w3_WXNeL--_5foVTfsrYThAoL24AUNMZ1q1ytAFfo37FIDyhBL5sNlukMMCTUNHiHWMjYDF26Xk8y-BtXDgFWVIkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dba6c54c.mp4?token=GxvQyvHrCHLAO0RI62tZe5vdRvCz0RaGLiwNfA1hCpejUiw66hLmWWGb2E8OydEWJtvX3BFneGjcWBQ35-rL5zGFHltVHWAQsTaQ8ZJHS6Ns9BmlcwFiH0aWx6igBN2xNo_deIETTXLo9u4gzLQD_rBxRctjFV89hBVfzzBMfDq46JKXMXQxUODycH0k14JHd-LjKZRjwX80VemnLRplbu-UbAUdb_bEygU21nFUgxRI9S55DNZrCI7DN01a-w3_WXNeL--_5foVTfsrYThAoL24AUNMZ1q1ytAFfo37FIDyhBL5sNlukMMCTUNHiHWMjYDF26Xk8y-BtXDgFWVIkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آتش از مقر گروهک‌های تجزیه‌طلب در سلیمانیه همچنان زبانه می کشد  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451153" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp80RF4XkatAW73VusUeXyt16EBHplwURB5Jl4HVTVDuqVJh-nkh5znuMTIUOOll4Qy1887T4W-JSnE349H7PF80XOZ5GEWt2xRwqxoaFc_fDPze_SuKOmnmHadd2zykQ-3KEDcNXp0GXWaOAhHdyJ-B7hI-Wbea5XKQwYKHyvhR-TmxAhFULy54V9Ug7z_hdHQEYP-DsCrLLgD6bGxHfPUkG3BMXOuI3K1Nwxd2grgQjmBlwB7_R6_drABMAOlP5ZWgxK90otTYHAUHxqHP6llMCF0ekdQ80gs5tQKJqzE_Vh2qdCqcgXhAdnMw5y9jsSK8WuBtzkU2EX2J3jOyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع عربی از هدف‌قرارگرفتن مستقیم یک نیروگاه برق در کویت خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451152" target="_blank">📅 19:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ac9f0f42.mp4?token=WAI9u0xF6Kya4AvEGW3f5ekTM1GycXUX-74_1Xb72NxLA2xHfzeIdp-D2dAsW-BSdA3I0CcOA9tyQF9YGEbA12sw4tpYWaq57AO_6_lHpyP4_WpMLPVj-rt5JyhPtsTXnrhxRuP6R-JMDIbGM2lSIackM2ZaXDlhDxAFgLJjn5DgJvxCGkW9lTFBHEKAHnOpydruwf6dMu68QjalmAXX1CLPpr0O3wq3iSkjDbHn_7cmChsIj9ZxW5Xo91L3w16TQO7kkKERZKS5gyBrWaccLZ5Puc1QVE7qH4zpaxjio1nna1hET_eUQ_zMPzY93tGgn9-BiaH5u7nfiQplo3xRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ac9f0f42.mp4?token=WAI9u0xF6Kya4AvEGW3f5ekTM1GycXUX-74_1Xb72NxLA2xHfzeIdp-D2dAsW-BSdA3I0CcOA9tyQF9YGEbA12sw4tpYWaq57AO_6_lHpyP4_WpMLPVj-rt5JyhPtsTXnrhxRuP6R-JMDIbGM2lSIackM2ZaXDlhDxAFgLJjn5DgJvxCGkW9lTFBHEKAHnOpydruwf6dMu68QjalmAXX1CLPpr0O3wq3iSkjDbHn_7cmChsIj9ZxW5Xo91L3w16TQO7kkKERZKS5gyBrWaccLZ5Puc1QVE7qH4zpaxjio1nna1hET_eUQ_zMPzY93tGgn9-BiaH5u7nfiQplo3xRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: در شرایط جنگی ظرفیت‌های خود را برای خدمت‌رسانی به زائرین اربعین کم نخواهیم کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451151" target="_blank">📅 18:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDKIm0XLA-Ile98jLRXB1PPcw5duZ5T_-DDsyBcB1n9V58lQFSDT1t8f1mvggHxvv0Zl7Y_hehwEwlukv_K6SFse9pXXSo0inwVlaJIr8eUlueWWAxsBMUJ4Nasnq9_BaWFHMzZQCgFZ8Wnl2FirmnXBk9jnEbTpYDrOv_VhA-Sacr1sMB0iZejEPZSSKV9ebU1iAgekEmz12yvmmFwC-opfGU9_ocoZulnRRRDyMBmfG-vOxcjcEKlefcHWXH1TCTC7DZ8E3i1Tb3gfR3J37hFLEHnAwoGbtxQ8MsTZzsZd7wp6NJluQzCHTyWUjuMIs_7mFsTo-aZ8X8oIBGNRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار ۱۵۰ هزار تومانی هم صادرکنندگان را راضی نکرد
🔹
قیمت دلار رسمی در مرکز مبادله از ۱۵۰ هزار و ۴۰۰ تومان عبور کرده، اما معاون سازمان توسعه تجارت امیر روشن‌بخش قنبری می‌گوید صادرکنندگان همچنان از نرخ بازگشت ارز رضایت ندارند.
🔹
معاون سازمان توسعه تجارت می‌گوید دولت صادرکنندگان را ملزم به بازگرداندن ارز با نرخی می‌کند که با نرخ‌های غیررسمی اختلاف دارد و همین موضوع بخشی از سود آن‌ها را از بین می‌برد.
🔹
در حالی که رئیس سازمان بازرسی پیش‌تر از بازنگشتن بیش از ۹۴ میلیارد یورو ارز صادراتی خبر داده بود، معاون سازمان توسعه تجارت تأکید می‌کند ارز صادراتی به کشور بازمی‌گردد، اما الزاماً وارد مرکز مبادله ارز و طلا نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451150" target="_blank">📅 18:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40aee3acff.mp4?token=j6MvZg4JIKTi3ii92TqW4RVQqJNO_IR7uHLmgjoNATwMIjw1aWhFYXLbbzZUaQ4hsE62xdeWubQ5HTg1Nk5z0hY_x5cP8jOlDndYMWZhktKylywV8WhK7qH5Q_te8qDYnxd4B9Nuq1OId5AnnWFszbybZ-FiDVM7USQIzGZgKXJl_nifjcq9MzlFgkbtgNH4rjy0JwNFDF6dO1yrCKUsanLOZieI5vJgVfVf9eT6WdMSY0dGlZ3KUQ2EHYaPZxryLdgDZXR489pBsyFX_GWWtKOE0FvRxdLeeH7H0-uKx0FNEpnChgPbHaFBcNan2bUcsgWlyZin1a_AqDkOpm7Hrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40aee3acff.mp4?token=j6MvZg4JIKTi3ii92TqW4RVQqJNO_IR7uHLmgjoNATwMIjw1aWhFYXLbbzZUaQ4hsE62xdeWubQ5HTg1Nk5z0hY_x5cP8jOlDndYMWZhktKylywV8WhK7qH5Q_te8qDYnxd4B9Nuq1OId5AnnWFszbybZ-FiDVM7USQIzGZgKXJl_nifjcq9MzlFgkbtgNH4rjy0JwNFDF6dO1yrCKUsanLOZieI5vJgVfVf9eT6WdMSY0dGlZ3KUQ2EHYaPZxryLdgDZXR489pBsyFX_GWWtKOE0FvRxdLeeH7H0-uKx0FNEpnChgPbHaFBcNan2bUcsgWlyZin1a_AqDkOpm7Hrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقشهٔ سلطنت‌طلبان برای جنوب ایران!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451149" target="_blank">📅 18:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFoD-ExAfbpDF2Z5ewUCO5sXABdcGQnEqfLbohIvIMbV-5i1aKWyt_i7EFROJt7Eb6EUsusYRQEjn6N_2uYD-yHX-nNhBTUZ1HJfgW8GWLhDf8X0HQuqM4n7iDJzkaAXhRMyR3cC7C0AsW4m3Xf6pv-ELyjK-JU1si0yrsCuLSOg8R6gwQElvNpFVSsJVtDT63WaBfxrEBWm3XMef4dLfI_5kCfDnxs_ayMHkrXWt33RybCLc37b5Wosfrkbkq2TMwMB9De064XbvYMhnBC1CwBBZrm9Id-s6qTmRJxGCqQ1GAd91gckF_s7hNQ3dCd9v-MzkNIqpx8UJed5HUXL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: در هرمزگان خاموشی نداریم
🔹
در جریان حملات دشمن ۵ خط انتقال برق آسیب دید، اما این خطوط در کمتر از ۶ ساعت بازسازی و وارد مدار شدند؛ هم‌اکنون مطلقاً در منطقۀ هرمزگان خاموشی نداریم و همه مناطق درگیر کشور نیز در اولویت تأمین خدمات قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451148" target="_blank">📅 18:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451146">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جزئیات طرح جدید بازار جدید انرژی
🔹
سند ۱۰ صفحه‌ای به دست فارس رسیده است که از تولد یک بازار تازه به نام «بازار بهینه‌سازی انرژی و محیط زیست» خبر می‌دهد.
🔹
نسخۀ نهایی این سند تیرماه ۱۴۰۵، توسط معاون رئیس‌جمهور اسماعیل سقاب اصفهانی تدوین شده و حالا نوبت کمیسیون اقتصادی دولت است تا آن را بررسی کند.
🔹
ایدۀ شکل‌گیری بازار انرژی که هم‌اکنون در دولت تدوین شده، پیشتر در قالب طرح وان توسط سعید جلیلی مطرح شده بود، هرچند این دو طرح در جزئیات با هم تفاوت‌هایی دارد.
🔹
طبق این آئین‌نامه ۱۰۰ درصد سهمیۀ انرژی مصرفی بخش خانگی به صورت سرانه و براساس بُعد خانوار بین همه خانواده‌ها تقسیم می‌شود و هر خانواده در صورت مصرف بیشتر باید انرژی خود را به قیمت آزاد از بازار خریداری کند.
🔹
این طرح یک دگرگونی ناگهانی در حوزه انرژی است و عملا قیمت‌گذاری حامل‌های انرژی را از دولت به بازار آزاد می‌سپارد.
🔹
در یک سوی میدان، کارشناس انرژی رحیم احمدی معتقد است که برای اولین‌بار، کاهش مصرف نه‌تنها جریمه ندارد؛ بلکه منبع درآمد می‌شود. به باور او، اقتصاد بیمار ایران به همین داروی تلخ نیاز مبرم دارد.
🔹
در سوی دیگر، کارشناس اقتصادی مهدی پناهی زنگ خطر را به صدا درآورده و هشدار می‌دهد که دولت اول شوک گرانی می‌دهد، بعد پاداش؛ او از دست اندرکاران این طرح می‌پرسد، آیا مردم اصلاً توان کاهش مصرف دارند یا این طرح فقط یک قمار بزرگ روی توان فرسوده‌ترین قشر جامعه است.
🔹
مرکز پژوهش‌های مجلس اما پیش‌تر درباره «شوک‌درمانی» در اقتصاد هشدار داده بود. طبق این گزارش اقدامات شوک‌آور نه تنها اصلاح نمی‌کنند، بلکه با آثار منفی اجتماعی، راه هرگونه تحول را می‌بندند. راه‌حل به اعتقاد آن‌ها، تغییرات تدریجی و کوچک‌مقیاس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451146" target="_blank">📅 18:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451145">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea066cca8e.mp4?token=XWtEVwEGTxaWNI6yeC5g1XaLbun2hSxAjPJeu6RdrdVKYNKcKlzgFZ3fX6KrCMfC7OniRMMantOe-KWeVdc3OGqYAA5zMwJ_LL1PbEEYYdkckwStrBaNRQnW8-KeIy-Hevd69fF2La8k2JaDBayr7Avteie_pG-I5fR7lKU_-wVYZMgwPbEGfPDbUMflbQ8OT4hZgyWxAFoErqsI6R0_CPuvNRsndiQIePszNZRAbUg_oeVTYiJkTtCscBJ6ZrIEi1VhZ1KZliso1AJNzBVdKc8XqJECKO255bINn3yPUTb3EkRlD_B5kABtzjcT0hg2OKb_IbhWu0wqQZF7VoBLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea066cca8e.mp4?token=XWtEVwEGTxaWNI6yeC5g1XaLbun2hSxAjPJeu6RdrdVKYNKcKlzgFZ3fX6KrCMfC7OniRMMantOe-KWeVdc3OGqYAA5zMwJ_LL1PbEEYYdkckwStrBaNRQnW8-KeIy-Hevd69fF2La8k2JaDBayr7Avteie_pG-I5fR7lKU_-wVYZMgwPbEGfPDbUMflbQ8OT4hZgyWxAFoErqsI6R0_CPuvNRsndiQIePszNZRAbUg_oeVTYiJkTtCscBJ6ZrIEi1VhZ1KZliso1AJNzBVdKc8XqJECKO255bINn3yPUTb3EkRlD_B5kABtzjcT0hg2OKb_IbhWu0wqQZF7VoBLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  تعطیلی بندر العقبه اردن و فرودگاه رامون اسرائیل در پی حملات موشکی
🔹
مقامات امان امروز محوطۀ بندر استراتژیک العقبه را به طور کامل بسته و فرودگاه بین‌المللی رامون در شمال ایلات اشغالی نیز پروازهای خود را متوقف کرده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451145" target="_blank">📅 18:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451144">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/venpTkL2dPFneiVKbJQEofBPNxUaRH6SYXcyergMvC6TRi9RbTHzzGWIZH8kynCwHqRMh3imvdNpPQBMBGujSU3TYU8d_wWYHfjoyQ_40Ut5ozY9YcDvai9OsvI8jI855KtFxqDQGwkQzPHsPcz4RIZC2OpUPwBkrljFgzJNzy1b0h9OOmrcr9Zq42U2uuAO6D6wnKqWF4kc6oiASkWWz4GDwWzPKZ0CDG465jLLm4sno3oWrZLv2fS2n4iOOV-t0IgGHdjEsmWq0Z4on-pirgcGgpXUMy2M-b7K0LN1v7JCnkBle3j_-XaQ6f5mTMfpzSE2XY40XDKFCP5izL2O0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: در دورۀ زعامت حضرت آیت‌الله سید مجتبی خامنه‌ای، مسیر نورانی و پرافتخار مقاومت را ادامه خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451144" target="_blank">📅 18:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87473a57e.mp4?token=iPllPF2vfv9xsQKkdv1aBg4tgDcc0dq_A-erxrKXCB0dD3dYdKAV-EzVDse6weu96ZSZPVY-1ob32YiJv4rkSRxo2827geD0blGet6xrbscDARMEvWOE9nznm1_qYWATiXoxsGN0ShOWBJkGZbxPn8sUIx7AMeoGidB_x7O2DZ-BmNY9nCl11s4GLuo4Juy2-Ynnfmo6zmG_kqOYAqAfAArrgKyPU-M-yDcZhFI-yMh0UXX-wrsgvA29baCIlp15NlQAJAJS3DPYi_oHL40fwY5VuY4Qi7ZZho-VGq_F6DQm-vGT5XuzbBnI2iJanlGngvz_HUHgNHhgrdE1atI51g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87473a57e.mp4?token=iPllPF2vfv9xsQKkdv1aBg4tgDcc0dq_A-erxrKXCB0dD3dYdKAV-EzVDse6weu96ZSZPVY-1ob32YiJv4rkSRxo2827geD0blGet6xrbscDARMEvWOE9nznm1_qYWATiXoxsGN0ShOWBJkGZbxPn8sUIx7AMeoGidB_x7O2DZ-BmNY9nCl11s4GLuo4Juy2-Ynnfmo6zmG_kqOYAqAfAArrgKyPU-M-yDcZhFI-yMh0UXX-wrsgvA29baCIlp15NlQAJAJS3DPYi_oHL40fwY5VuY4Qi7ZZho-VGq_F6DQm-vGT5XuzbBnI2iJanlGngvz_HUHgNHhgrdE1atI51g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: پل‌های تخریب‌شده را فوری می‌سازیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451143" target="_blank">📅 18:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10883cd0fa.mp4?token=mMuH7WgSP9mP4eCVlTueGy0_lIKyZI978zOmshwWJB12ZFqfBpFPxPHzBgnAjrN2jOtftIQlnENHZBkiRz9N6eCcRZINl0gTIzUN10ma50dIG3RmSKtj6v6_Y9pLvq08N8gEdjyrOZHLowIZ-J8y2cLWmneOmgcdQrsEpZ1Qots_E7FYCNk7_YQArRZqF2LKUy9x_DGjN2KL87KiXH-crw2hZeLlG4WR94NP7l1UrC_PrYKEsJBHV-SuZmhEyNu18wEfs1yaK-nNvt5wNolXDtLHCN4Fe1G1pX8fwtvuYKZeWyc7XuAmmPEU5uIpXZfXSpMPT52sDCDCxmzU4U9gFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10883cd0fa.mp4?token=mMuH7WgSP9mP4eCVlTueGy0_lIKyZI978zOmshwWJB12ZFqfBpFPxPHzBgnAjrN2jOtftIQlnENHZBkiRz9N6eCcRZINl0gTIzUN10ma50dIG3RmSKtj6v6_Y9pLvq08N8gEdjyrOZHLowIZ-J8y2cLWmneOmgcdQrsEpZ1Qots_E7FYCNk7_YQArRZqF2LKUy9x_DGjN2KL87KiXH-crw2hZeLlG4WR94NP7l1UrC_PrYKEsJBHV-SuZmhEyNu18wEfs1yaK-nNvt5wNolXDtLHCN4Fe1G1pX8fwtvuYKZeWyc7XuAmmPEU5uIpXZfXSpMPT52sDCDCxmzU4U9gFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: عملیات نوسازی ۲۵۰۰ واحد آسیب دیده در جنگ آغاز شده و طی ۲ سال تمام خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451142" target="_blank">📅 18:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW742tcQa_suSApGFm1TgbusgpCLrVl21bfJFJoMtz3bIOo4_zqZne4FWiFPWpaWM4mZKQ9oVaw2fEhwwZceQSo-v6OiFh8ehvihOUBI9j9eYeYMNQBxWwO2sirAE4zNjcQDto5KcnEZPH1JoNPHWCo0SHExe0FFiBL82aXYXe2kQmjPOH8WdS-dZehrGRx_AR15h6smojXLNPnJf4foW4xhAF3nGKzh0oxQN62titKIDXAtEDim2zuJU-BclmI2bqYsTCltsDr01dp4fcjqw1b3250VsZHzxQhmRMHDthvvByJMQBm-B5SVmGQ8HIeMqhuwU-_DtVlLopPhmopesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ آمریکا به سایت نیروگاه هسته‌ای دارخوین خوزستان
🔹
سازمان انرژی اتمی: رژیم آمریکا بامداد امروز (یکشنبه ۲۸ تیر) حوالی ساعت ۳:۳۹، با شلیک چند پرتابه به سایت درحال ساخت نیروگاه دارخوین حمله کرده است. @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451141" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451140">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4176f63ab3.mp4?token=m9gjVgPP2BBfLHya8Q-SYP2LGVR5Q-mKkrSWKfQ5CagPG3elMwRzfBClOThipSrEkddkyv6bfy6QjvPTzospOYbifL7wQxd1cs4fF_igAHYorhsoMjNkMKJ1iYyUynX_VN0PvWbSGfWguFqqS44QdhJ6hoiq4bMx_wYDbQOGNWg4OItRrh0qWPfiwIfwS1ZecLto_P54GMNG-GSpy-FN6MizJVzn-j8HrBPPaTFdAr2ZqqAE6kMvKM74g_nXbhIOkRSwlS6VisNAt2Uwl3XVB_EM7o5zvLavVArg9pp29p3hqFLq0fgp0M40r9GCCZMHCgDJ5pw8nd3ibbQvYYsOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4176f63ab3.mp4?token=m9gjVgPP2BBfLHya8Q-SYP2LGVR5Q-mKkrSWKfQ5CagPG3elMwRzfBClOThipSrEkddkyv6bfy6QjvPTzospOYbifL7wQxd1cs4fF_igAHYorhsoMjNkMKJ1iYyUynX_VN0PvWbSGfWguFqqS44QdhJ6hoiq4bMx_wYDbQOGNWg4OItRrh0qWPfiwIfwS1ZecLto_P54GMNG-GSpy-FN6MizJVzn-j8HrBPPaTFdAr2ZqqAE6kMvKM74g_nXbhIOkRSwlS6VisNAt2Uwl3XVB_EM7o5zvLavVArg9pp29p3hqFLq0fgp0M40r9GCCZMHCgDJ5pw8nd3ibbQvYYsOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکایی‌ها به این کودکان سرطانی هم رحم نکردند
🔸
جنایتکاران کودک‌کش آمریکایی_اسرائیلی با حمله به بیمارستان شهید بقایی اهواز و بخش کودکان سرطانی در شامگاه چهارشنبه ۲۴ تیر، توحش خود را کامل تر کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451140" target="_blank">📅 17:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451139">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxI3ProAGIlHSLX4bZnPLjQKPvUSlgy4c2eyii0dvW_fm2O53bypaI_moiLzH1ea56Pv-HcrXoDXx9VytPAoqQBR52ZJGPpBSAGrEK7JlL2TVWeUd13ftnpN3GFpMna6sgD8LtVyuCpZFs3vjSIyHaDCvGVzfQAgyx7rPLuXlxv1OnmXv0rP11JlUBm2Ki77Mpz6uaYnQcIT6HDnRtZ8pSVuFcapylEs1_AC4lgNqQj2cUNisLZaM4T5ENJjucMWKocwFCyV6g0S1VTUFwdsm3ypenf2-xVKNX4-Q353EeutB-ObScgPHK_Pt9U6O8SAuQNWSJI2uVCZEwHQqMNJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار پلیس فتا ایلام در خصوص لینک‌های جعلی درخواست کمک مالی
🔹
رئیس پلیس فتا ایلام: مجرمان سایبری پس از دسترسی غیرمجاز به حساب‌های کاربری افراد در پیام‌رسان‌های داخلی، با سوءاستفاده از اعتماد مخاطبان، از طرف صاحب حساب برای دوستان، بستگان و مخاطبان او پیام ارسال کرده و درخواست کمک مالی می‌کنند.
🔹
هرگاه در شبکه‌های اجتماعی از سوی اعضای خانواده، بستگان، همکاران یا سایر مخاطبان پیام درخواست کمک مالی دریافت کردید، پیش از هرگونه واریز وجه، حتماً از طریق تماس تلفنی یا راه ارتباطی مطمئن، موضوع را با شخص مورد نظر بررسی کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451139" target="_blank">📅 17:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451138">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMjfVzWPNe5nzNUIeCrWi2Yt1mkiBp4yzx-o84BLXWGlxXuJJbbH4KLG8pAf70O-W3HoMqrO5AVi34oA2QnRDtIjU_3YS2P74Gc-MkQhjovUDtDqw2Z3rcIYX3xSWG4YetRxB4hRIgkjwHFi3fUWprUbzmaokSgMiDtUwz7iY20kPB-UyNus2QrA7iZD3SpCUU_d2-gsQQr-5qAZk_2SAA6fnjwM1-C_2cYUFj_hD0sRW3uV_gOwbRw3Z58X2hMHl5_3XzrHNYadmYyJen4PI8_kb6kVmfHkXQLGe-WftfdLMPGwtAjPpqa6SDIJOFWlS9MD0MHQkjVC3ETE82Sm2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت رسمی بلیت پروازهای اربعین اعلام شد
🔹
سازمان هواپیمایی: قیمت بلیت یک‌طرفه از تهران و استان‌های غربی به مقصد نجف یا بغداد ۱۲ میلیون تومان و از مشهد و استان‌های شرقی ۱۴ میلیون تومان تعیین شده است.
🔸
نرخ رفت‌وبرگشت از تهران و استان‌های غربی ۲۴ میلیون تومان…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451138" target="_blank">📅 17:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJNrzBixQf6DiiMFZxDeFs8sa8bIluhDFIlIW7eNH7-wgU8O_Yg039W5t-YftNiM07vwLoO2-N2wOt-PHkCLEoxL2tfCOGUleHP52IKb4ueCoOGEBVN7_QXhr5j4q-C9IpTsNjhC0Ckpj_ZlRxPBdVmmDHEc6FPI_o1DDcb0I9XsdpornVQoxK4rFJc29jmRlTIjeBIkPKBBFz4Ri-tu9cCLEVh95l8hvReWrSveMlFRO3wf5LhYO4WGDgb5DyRI2T02v87JTg3_mQVYbLD14TCYyQ_3HKIK_jt2iYDhHnjl2v_aYBJdWLSVxoCAVKlIWP-_Fr2n5FMiJoTG8YsWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برنامۀ «طبیب» شبکه سه امروز از بیمارستان شهید بقایی اهواز روی آنتن رفت؛ بیمارستانی که طی روزهای گذشته هدف حملات موشکی آمریکا قرار گرفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451137" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451136">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ba567704.mp4?token=IkLE75xFrcJ7EoSuUmUfuEpQMmyre-PmnTM5-XRtoSdDZz8DGmS3aVw021QXCVt--ZWeahnWOFw_gciHx9TDk7HQHkKRdzvAGP91USJ-ZCvNrEsZ2L4ZbXFxa6bGVDJD71aAE3cKOMU1Pd5NWNKf1b08T9azFj51nsXzGoo5ZiKWlGbhiTLv9FbT3BUczw8ggGnNGHG4jwe_P-HC-1sn59ekaLV4jya13v5MuBJZc078Be5Abk_BtxwIQAwHSNjzdIZd2zAfxH4B90tpXE9OHZ9VQCIWyow454HCDCRhpaNdjrd1jX3fSx9MW_tsA6oX3C8egJBPJnDpZgygtGBy-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ba567704.mp4?token=IkLE75xFrcJ7EoSuUmUfuEpQMmyre-PmnTM5-XRtoSdDZz8DGmS3aVw021QXCVt--ZWeahnWOFw_gciHx9TDk7HQHkKRdzvAGP91USJ-ZCvNrEsZ2L4ZbXFxa6bGVDJD71aAE3cKOMU1Pd5NWNKf1b08T9azFj51nsXzGoo5ZiKWlGbhiTLv9FbT3BUczw8ggGnNGHG4jwe_P-HC-1sn59ekaLV4jya13v5MuBJZc078Be5Abk_BtxwIQAwHSNjzdIZd2zAfxH4B90tpXE9OHZ9VQCIWyow454HCDCRhpaNdjrd1jX3fSx9MW_tsA6oX3C8egJBPJnDpZgygtGBy-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاری که مردم نتوانستند برای رهبر شهید انجام دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451136" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1lCjIQrssJ_4RNFUYj3c3GTF8hNAjIQ-vK5ZanrjDbZJmGA_7gGzOKqHjaT1Oe7k7oXl4FbO64K5Sp_DDf31mg5f-pBvWtoHBNbC_erSQ3Ok6AU-y-LQOYvbiLs_TEI27D8k3GWvTP4uR21pFdhWssDAOa0Vu3klG0cRUmxFX-b0xJl5mAN0BQL0txK-yVH28MmD9lHyma0CAMinzJS4GEC12k94eooLRAKWPofyZLa3rJQoqt5kXmZjg9sOu2LwvJVEkRnA8P1bS1amxZjdIFVfED97-MTFiPOVfnDu3sml1DZL0oVefANJFYv3OHDRZ8vlxPxDeASDZnrs-L9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک فروند پهپاد آمریکایی MQ9 در همدان
🔹
دقایقی قبل یک پهپاد آمریکایی MQ9 توسط سامانه‌های نوین پدافند هوایی ارتش هدف قرار گرفته و سرنگون شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451135" target="_blank">📅 17:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451134">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
حمله دشمن به یک نقطه در اطراف آبادان
🔹
استانداری خوزستان: یک نقطه در اطراف شهر آبادان دقایقی پیش توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451134" target="_blank">📅 17:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451133">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=MBn3rQBUeKtQPLFZSvurXxuyIGDMSU8NjZhzMD66sAi4JgCYk37Jrh4qY6bJaEpe3R_MnqW0zzC8I8020c9CJxWAQwZl9wyfVPca5mJdpcyhps4kXSgfk5BlUyO3pgmOmeijhxk9CDT4s6qfs9JbJxJpsbvd9AvXcA6gyZfSZaIILUIr-MNUzGSt-vacxfjF3QeRmv0ORDjELYofHf7mRAasX9iUXjMikEe4KE0MoOq0M05i08wbP9trAkXbU9z1IvD0eJJfKO0gTQJ823ARyCc5SEWM7ftlct0xfxQdFygRXbtfaFVn7Ma1k9aT7KtPS3sAF-dl23HhLFohwfT0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=MBn3rQBUeKtQPLFZSvurXxuyIGDMSU8NjZhzMD66sAi4JgCYk37Jrh4qY6bJaEpe3R_MnqW0zzC8I8020c9CJxWAQwZl9wyfVPca5mJdpcyhps4kXSgfk5BlUyO3pgmOmeijhxk9CDT4s6qfs9JbJxJpsbvd9AvXcA6gyZfSZaIILUIr-MNUzGSt-vacxfjF3QeRmv0ORDjELYofHf7mRAasX9iUXjMikEe4KE0MoOq0M05i08wbP9trAkXbU9z1IvD0eJJfKO0gTQJ823ARyCc5SEWM7ftlct0xfxQdFygRXbtfaFVn7Ma1k9aT7KtPS3sAF-dl23HhLFohwfT0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت در مناطق مرزی جنوب کشور: ما به لطف قدرت نیروهای رزمنده فهمیدیم باید از چشم در مقابل چشم دشمن عبور کرد
🔹
پاسخ حملات به پل، دیگر زدن پل نیست؛ ما از زدن تأسیسات و نقاط مهم میزبانان دشمن ترسی نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451133" target="_blank">📅 17:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451132">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqpEJ7iqd4CgkCmusFw0DcWkodAjaaSshLD4lB2B3UeEYd_hKhgC1vw6HxbVI41K8krxmT3BU9lLtOc7hDLMZuCjPzbFV4JZQIq225nLGQjI65shAepPLuPQUERw_wMzcbNGGPazlpqM0BtUJ7Rz2juM-x0yzc7ZdC_cja8s5nGTB9cjGrKvhjDXZmTMKTUROIsYcF_rCG_ey4oH9CqItMi7UM2FJsAj1U426AtmYmiJzstpeKQJF5zIo-BJfe3D5HXMsb4sy4GZ3iGhsvL3lO_VGrwUoCN2n7pq-X-TZBY-CulYGranWweH3Qi0LIk5z-KjuCIK1ppLpLPxdSoOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکلیف زمین‌های تازه‌متولدشدهٔ خزر روشن شد
🔹
سازمان حفاظت محیط‌زیست: اراضی تازه‌پدیدارشدهٔ در سواحل دریای خزر که درپی پس‌روی آب ایجاد شده‌اند، متعلق به دولت و غیرقابل تملک هستند و هرگونه تصرف، واگذاری یا ساخت‌وساز در آن‌ها ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451132" target="_blank">📅 17:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451131">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGaA-syrqEnyeXLCVisAaJInN51wDw41H-tkIu6-oWSfZd6Y38H4P6hKj28C3jD11oOAwipOJOQiDPZW1femhVP4HPQO_ZG8FcaUexxeyE8UlIXxj15fYMv4qUWvyrRnptrmiRCzfKmVdgKNdDAZRPjnxJHM49lwQqCK78odChcStHmLYA9v5WqegBzLsVXRPxIDpE2y0gkwp_sNRuNVeAgwoOJMD7G6eSzMVKiSnZudAMuvFZ_52hTB-8apeZqzm8sXmYcbuzzGQZ9OVCqqyCqiaGQyrhSiZxxXZ09K5e45FaEdHPuxZk7zoUl9NS9cX8_fzYVjlNG_hvm0OqAHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین پرواز برنامه‌ای هما در مسیر تبریز-باکو-مشهد انجام شد
🔹
هواپیمایی جمهوری اسلامی ایران، هما، با راه‌اندازی اولین پرواز برنامه‌ای در مسیر تبریز–باکو–مشهد، توسعه شبکه پروازهای زیارتی و منطقه‌ای خود را وارد مرحله تازه‌ای کرد.
🔹
این پرواز که از امروز به صورت هفتگی در هر یکشنبه انجام می‌شود، با هدف تسهیل سفر زائران جمهوری آذربایجان به مشهد مقدس و تقویت ارتباطات هوایی میان ۲ کشور برنامه‌ریزی شده است.
🔹
«هما» پروازهای منظم تهران-باکو و باکو-تهران را نیز در روزهای دوشنبه و پنج‌شنبه برقرار کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451131" target="_blank">📅 17:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451130">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db42a1728d.mp4?token=WTsyqvtgq2yHgE91WwyeKAPf0HJwTBsZgGuoijaKebPGUXpgadtd7KD9LtM6nboCTqZkt_n38A1MN3OjGhrONsaHbIAX5GHWBXYng8-_kSmttThv2Se7ZtNRAxSaqGbOBw7hx0n0fRSaX2ph92lyLwrFfl1GSb-4ObXWBYqJu8GoYZISqnUJaCOyJOTbt4dEqjJYmwzWeDg9Cig4sCSVnC7X8nvHPg_ya3YWjVnIuFF0QFs5d_PrzUXwa5gXAExoLubbG-8MRkuD3Dtto90i1Gey7RwJV2eIz4RGC3aTgyLHFpWFB-EjGVctKi0Z3iR2XiKe_Q2j9un5L24Jdfe-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db42a1728d.mp4?token=WTsyqvtgq2yHgE91WwyeKAPf0HJwTBsZgGuoijaKebPGUXpgadtd7KD9LtM6nboCTqZkt_n38A1MN3OjGhrONsaHbIAX5GHWBXYng8-_kSmttThv2Se7ZtNRAxSaqGbOBw7hx0n0fRSaX2ph92lyLwrFfl1GSb-4ObXWBYqJu8GoYZISqnUJaCOyJOTbt4dEqjJYmwzWeDg9Cig4sCSVnC7X8nvHPg_ya3YWjVnIuFF0QFs5d_PrzUXwa5gXAExoLubbG-8MRkuD3Dtto90i1Gey7RwJV2eIz4RGC3aTgyLHFpWFB-EjGVctKi0Z3iR2XiKe_Q2j9un5L24Jdfe-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داور مسابقه سرآشپز در مناطق مرزی جنوب کشور: آمده‌ام و حاضرم اسلحه دست بگیرم
.
@Farsnart</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451130" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451129">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrCY_qbfAfoGRV0jCLFEOWG3JRauDOpLXboNeenyJD3YThMCJV00C5GmFekGc4vUQzhOxNqYXjqr4FJwszqz_wPm6096zhMT0wWdIyNtE5MK8N7nYFfzONBfP0Yu2xWQLT2kIZP8RNm-BPTtvQ-hqu3QUCICfD9cD7PCKhA_CZ0RWpPXavU66BPkFRZT3x98woYUGczwwYN9zhFC-UkiFycXXJmJm6NC1_ZHS47bI5et_dpFhUUeQQzHVu0MU56IuxVXCW4LJuLOuzmdaVaTkZWI7deK9iXoD767Emzxf1dnv-sgXJUIGwMkiKThEyg8VKLSEtMYmZDv8uIAOyErNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب جالب شبکه ۳
گفت‌وگوی زنده با ۲ عضو کمیسیون سیاست خارجی و امنیت ملی در نقطهٔ صفر مرزی و روی شناور در روزهای پر تهدید مرزهای جنوبی
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451129" target="_blank">📅 17:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هشدار قوه‌قضائیه دربارۀ انتشار محتوای خلاف امنیت ملی
🔹
درپی تداوم اقدامات خصمانۀ آمریکا و رژیم صهیونیستی علیه ایران، انتشار برخی مطالب، تصاویر یا ویدیوها در صورت احراز شرایط قانونی و تشخیص مرجع قضایی، ممکن است مشمول قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی شود.
🔹
براساس این قانون، انتشار اخبار کذب، تولید یا انتشار محتوایی که موجب ایجاد رعب و وحشت عمومی یا برخلاف امنیت ملی باشد، در صورت عدم شمول عنوان افساد فی‌الارض، می‌تواند به بیش از ۱۰ تا ۱۵ سال حبس و انفصال دائم از خدمات دولتی و عمومی منجر شود. جریمۀ نقدی این جرم از ۳۶ تا ۵۵ میلیون تومان تعیین شده است.
🔹
همچنین ارسال فیلم، تصویر یا اطلاعات برای رسانه‌ها، شبکه‌ها یا صفحات مجازی بیگانه یا معاند، درصورتی‌که خلاف امنیت ملی باشد، بسته به نوع محتوا می‌تواند از ۲ تا ۵ سال حبس، انفصال دائم از خدمات دولتی و عمومی و سایر مجازات‌های قانونی را درپی داشته باشد. جریمۀ نقدی این جرم نیز از ۸ تا ۱۸ میلیون تومان است.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451128" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28df5059a2.mp4?token=TaRgoI3XIXhQPs8OSSppMRFZ51ykTGx4TgMgAgyg_airhlSpCUqg5Rtr7us4gO9zGwK11C_jy-jjA8Tk0HnyKTdPaVxTgBnPu5cLw6UKcU0tPDsKVBOSMbUhuV4F77Ww7DYo_1VYjvAhyuBbGxJ9OluoqYVoDQXz4_nDcCSUdbQmcJDNOBTj1towQyg7ql7jtuyvBaBQxYaov9TiTQrx4YR_VbW4j4q3KIrW6OcsgioLJUQFbbDRBjVZ-89KZaQ5mwJQWY29VcjKkTbIX6rPy-u3KSWTnA6gxltEEAPNUQU_VZb5VbtDCpL6ZukF1RcAmRZl40svJ1w4trAmxNH6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28df5059a2.mp4?token=TaRgoI3XIXhQPs8OSSppMRFZ51ykTGx4TgMgAgyg_airhlSpCUqg5Rtr7us4gO9zGwK11C_jy-jjA8Tk0HnyKTdPaVxTgBnPu5cLw6UKcU0tPDsKVBOSMbUhuV4F77Ww7DYo_1VYjvAhyuBbGxJ9OluoqYVoDQXz4_nDcCSUdbQmcJDNOBTj1towQyg7ql7jtuyvBaBQxYaov9TiTQrx4YR_VbW4j4q3KIrW6OcsgioLJUQFbbDRBjVZ-89KZaQ5mwJQWY29VcjKkTbIX6rPy-u3KSWTnA6gxltEEAPNUQU_VZb5VbtDCpL6ZukF1RcAmRZl40svJ1w4trAmxNH6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساعتی قبل یک پهپاد لوکاس توسط پدافند ارتش در جنوب کشور منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451127" target="_blank">📅 17:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=oUTNXsJxMvlw4hOUzppvB2PiRtV3iKrBFwIukjCRfUNXTpX069nD_nhVQdHJPAKgBOJPuljJciAaBbBuyMVOA1lnd1AnoG3effS8QpqMjo-hj1KE0pCUQbefqf1kYVRDAPkEWhVb27ebS7KogpwsAoBRzVNxOIqWvOxkltaCYjYbX3YE3EEqQwsPci0SXI_ski4_Km1yWkVVgz5eLjEZK018CzdYotnXQN8I9OiGy10Hdsn-HmBZ3L2Ef59Lveu4P1-0XdXeJdSyBmsTtKuOfwrNHGuEmCj2H2H-wNZ0h1nfNuRuE4lqzV-9lAkuLFS7HFDx2r6v1hlA_qzRzSa1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=oUTNXsJxMvlw4hOUzppvB2PiRtV3iKrBFwIukjCRfUNXTpX069nD_nhVQdHJPAKgBOJPuljJciAaBbBuyMVOA1lnd1AnoG3effS8QpqMjo-hj1KE0pCUQbefqf1kYVRDAPkEWhVb27ebS7KogpwsAoBRzVNxOIqWvOxkltaCYjYbX3YE3EEqQwsPci0SXI_ski4_Km1yWkVVgz5eLjEZK018CzdYotnXQN8I9OiGy10Hdsn-HmBZ3L2Ef59Lveu4P1-0XdXeJdSyBmsTtKuOfwrNHGuEmCj2H2H-wNZ0h1nfNuRuE4lqzV-9lAkuLFS7HFDx2r6v1hlA_qzRzSa1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
🔹
سپاه پاسداران: مردم حماسه آفرین و شجاع و بصیر ایران اسلامی! در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451126" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از آغاز تیرماه بیش از۵۰ نفر از هموطنان در حملات آمریکا شهید شدند
🔹
وزارت بهداشت: در حملات هوایی ۶ تا ۲۸ تیرماه، ۵۱۷ نفر مصدوم و بیش از۵۰ نفر از هموطنان شهید شدند.
🔹
در میان شهدا ۵ زن و ۲ شهید زیر ۱۸ سال، در میان مصدومان ۳۵ زن و ۱۹ نفر زیر ۱۸ سال هستند، تاکنون ۲۸ عمل جراحی انجام شده، ۴۶۸ نفر ترخیص و ۳۲ نفر همچنان بستری هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451125" target="_blank">📅 16:57 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
