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
<img src="https://cdn4.telesco.pe/file/G-GuC278rNxJUN6LArJVbwlwX1AOTfpiLEJnjsqe8cikC_fgljeYFOGObHTrMUEnLPRapmC3CjJLjBPVCVQNVgbpOu1XI3326vlsv8Y-BK2567hakYKqufy8B7AmET47rN6teGAjjDuQPzTDQpUd5FAusOHt97pywRMPg-zq9u0_QgKYWKfoXFXKlmjKBfAyY90G7x3oLsQsow8wMDTMHRL5rSXHKL_tUQcA4HrGmYKPvvlI6DP15wCpgc0Qzu-v8iar_AobfXHLNqbyM0VHB0JuRuw9Mm-DjSoYaA3j7kP4q3KEYRhH59OWoHg32XGML7GXN-fYw1YS6QDz8ZjmeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 00:59:21</div>
<hr>

<div class="tg-post" id="msg-81932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حاجی بارسا چرا این فصل اینطوری شده تو یروز بازیکن میخره تو یروز میده میره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/81932" target="_blank">📅 01:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gL3U7LwsoV5S2w95vyrb_pVldTZEFtPcWQ1_K_voXRFiDDn4_y_VQDJQJpwuXi8Lg52W1Aa7k5CFRYIzN8YvhQ1FjEpNaY7HTqshv0k_qPuP3oKHqFIdng9uNbqqMOMBFAnyfcRja9c1dk-Gnn8i-9WtbbIIWfOsNXOPYC29waQwXjeKeXN6CNDZkyzb17IwcwnDY3o5o6pd4MIPow3uKTV26MfOl1U2ASTN5GydyRjlv7THq4Xp_VtgS5mOCLmDnh_E5qTqU3TSKfLenvcv2kuO0nlGOviN6YSPevSpMvitfnnyZ7suKsKHc08fbsJIKYghHFR1pQfFtzgnnwkWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnX05-D1EzMp6g6b0ZuF0fUTPYdg4mgqmRJxN82-W-cylfUG-GpsMsMaDpN0LnyAXgKXxfQvh6cUItSu6DCwGh08Lx3tdU8Ct76MHwh9jkZtFE6rWk3CvlD7YzZwJvEtZjflzwqsZY9vSlfN4hPCGvwASp1tZgA5iXglkA5g2usObBI7q9YqU3R9UEJsgX3OHyCu3NbW2_VpQK6YiyVQZblGgt5CRxGq-LOAwDMhbASeIpRFDipdIr0lHhkHMCpKTF5H0l9295UGc41WFRNIweL-0FcKEjKQL-VVp2KURnWifs1X3ei3xBD9RfWdYEby95a3PWdxrFjkBJUIt-S_9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رودری هیچ پیجی تو فضای مجازی نداره، حالا فنای بارسا رفتن سرچ کردن رودریگو و رو اولین پیجی که اومده بالا کلیک کردن رفتن تو کامنتاش دارن اومدنش به بارسا رو خوشآمد میگن
حالا پیج کیه؟ اولیویا رودریگو خواننده که پارسال اسپانسر بارسا برای الکلاسیکو بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/81929" target="_blank">📅 00:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=GZ4spSUlaXlBAyG4dUlZzv0W9CDHB01Yct2DQeZDFXKbceelL0tbyrj4K2D4ETCT4m0a3NYGGsDupeM_DrudBHdH9sOBRdBzxtWb9smcVDpq9qlAz3C09lRsPzvyDPpO-fi-ReM6-Z2h-s7r8EA3z0LUjQB3U2i4PciHW_EKkaj4-siUrFc3i2bb2HDfGFu97doGInA6oVAEnee7VRpIwhWFgH0JRu25iXmAkM9KknL5pH103TxsglOwRpn9AuIlFxpJpQEssvOa9TcUtov4vb2Ew36q2mSf9TNqtn4ZvbdwNZa_n798rlebDxQmxKXaZwbK1OJwSm1qX5AUVbDWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904b3d738c.mp4?token=GZ4spSUlaXlBAyG4dUlZzv0W9CDHB01Yct2DQeZDFXKbceelL0tbyrj4K2D4ETCT4m0a3NYGGsDupeM_DrudBHdH9sOBRdBzxtWb9smcVDpq9qlAz3C09lRsPzvyDPpO-fi-ReM6-Z2h-s7r8EA3z0LUjQB3U2i4PciHW_EKkaj4-siUrFc3i2bb2HDfGFu97doGInA6oVAEnee7VRpIwhWFgH0JRu25iXmAkM9KknL5pH103TxsglOwRpn9AuIlFxpJpQEssvOa9TcUtov4vb2Ew36q2mSf9TNqtn4ZvbdwNZa_n798rlebDxQmxKXaZwbK1OJwSm1qX5AUVbDWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر جور به قضیه نگاه کنی خدایی این یعنی تعویق دیگه.
ترامپ کنفرانس خبری خودش رو لغو کرد و به خبرنگار گفت هر چه زودتر اینجا رو ترک کنید ممنون می‌شم چون ما یه جنگ داریم که باید پیش ببریمش و برا همین باید زودتر از اینجا برم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/81928" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_mYlm86r-XuNgdJvk_OlPraQDKoeFb1oICQSpx_AGm0-zV39i4TtDx6PCOIV7g3xlEGuSzUWypcAyMrO7ZeyYcdFJVI84og8sx9SpEZiwe-T25l74UVp6RzNHh_CQeXmRgAdIR0ePe-4QfQmaWwiUMFXLVqHrbhllKv0mAwtkmWUC-ZbaWXYdHt0SRDrra8rf9e1VcI-mY0BKoiK2bOZMyjrJs2wM9UZ15loHYCduSURFesXVuGDmOR9Vc-JXw65Ea1YSvUVVH08T2rRFdNIpr-UaLGy1_8c12zQTE_D5pzE41zdHW--qk1gFECOGIWNBncjpBnoiFOs6cC8fipjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رندوم ترین عکسی که امشب میتونید ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/81927" target="_blank">📅 22:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امشب میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/81926" target="_blank">📅 22:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/81925" target="_blank">📅 22:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/funhiphop/81924" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فری استایل جدید سروش هیپهاپولوژیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/81923" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdWbtde-voOTGYcHQax7Qq5lBEoA4x3nbiDIiMFuAhX_PKfUg3jR-XPPf-57OVe8eHsaiVCDj5p0jPO8n0MhhF18Z2faJyyXe6SK9HASxsL-JH-FmTFtqoTa52MKXlaDz5lTo3fp6J4VQ2SglDh0lKZV8WzeHYCIC6V7LO5OZMAlhYQeVP_ihARNGa0INBwbyubMuD5rcVh8w3eabYEOF0fC1HBpOSWpUu6BDTqYRXvuXhNA8mGwOmciHOMwW2P4l0jmSwYqRI8q_q_L-1Zz93ZhkGKxLv8xnidJLxxKthbAudYL4wlS22W_7pMZiaoQ9gZHII6GdvrDt_gcxNjHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل البوم دکی هم بزودی منتشر میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/81922" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwIKKIiANoB6YdglXEPw68yleoTHwofoVs2CVui7YH7UgciF4kBnp4P8TIXW0UkatXVgVFQO4UBwp0pcVQopAd9ckiw79L8W1uOAviNAWDATCtd4SO1-C0PxDIOjl8tEgtbLB4FcA_zwQ2k9z4nfJFRfp8N3112AOyuD4a6beQTZS6FlTTub2JZHCt68BpNie5YpcZJYoAWQKrKL9uTh86z9cyXca4N5_egoCAEs6HTrt7GJYZUJBWHXYsmvih90NR3jwB_z2iG4zQP51vQCOR5h_Z42eyq86iLbYvfMgSWRxKUdxivey2CwCQObCIVCE0_ZNTaU-UTRLejgc9zfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دکی از نامه ای که مادرش براش فرستاده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81921" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81920">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=FxXEx5D1v8VjCJodLo8AuX4eB17wJ-80uc9pjhhBmtw-1by8v96iydhVxiDRcWIJ3ulS_L5aFuXd_htgrJY_7VtsWTjzXcJJP7gSJReUQltY54RSkkA1A3wJXs0sQc18rZulJjWa3jcWB5R1UwIoOV31nPgxJ5VhppT7ahXGZzseOu_ZqRf5-v8FZARv_OFHeXINkmlTFw8jgoibPAMW75sqCFDjOx0mvO_dR_FQvyjfcWnedK8Vd_W4uy9YXo-rIQWW9gi60-zoY838Y3mriKHQYUfXW50y3yI6V_UEDORrJBR-fiKdAUMzSqd7_H3CzNcF73Qy0XeeXzCw0xIL5wMX5srZ78NnWzgvMCR0G4PyDs-PgNImmUcbedNujLkcRWegzmWZwntV90SglbFwfrGnIYETsPRUahcKm-3z0hImWJ35DPh9i7xaKDGsFcHFM6wTEr2KSojgb34YUIG_kE9dkuTBU0aIsb2bMKm9Jp2B2mpPjUsn4D26NwAbBc4wuuSRYcAPlsfE1ZOhOfVsMFMBF1WnTwNngxKWk_arHkBCaJcBqIehLqimbNZjzF2TGzsXxaJLlGEKqJ2Y6q83AZ0EojFeCLFqh_e2UWM6rFrJ6ULi8RX9OG2eyhU8vNzpC34F6jEhfrKfXJeYnLI7sHgVPNrLCcO_U4M7rHwFEtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30792ee17.mp4?token=FxXEx5D1v8VjCJodLo8AuX4eB17wJ-80uc9pjhhBmtw-1by8v96iydhVxiDRcWIJ3ulS_L5aFuXd_htgrJY_7VtsWTjzXcJJP7gSJReUQltY54RSkkA1A3wJXs0sQc18rZulJjWa3jcWB5R1UwIoOV31nPgxJ5VhppT7ahXGZzseOu_ZqRf5-v8FZARv_OFHeXINkmlTFw8jgoibPAMW75sqCFDjOx0mvO_dR_FQvyjfcWnedK8Vd_W4uy9YXo-rIQWW9gi60-zoY838Y3mriKHQYUfXW50y3yI6V_UEDORrJBR-fiKdAUMzSqd7_H3CzNcF73Qy0XeeXzCw0xIL5wMX5srZ78NnWzgvMCR0G4PyDs-PgNImmUcbedNujLkcRWegzmWZwntV90SglbFwfrGnIYETsPRUahcKm-3z0hImWJ35DPh9i7xaKDGsFcHFM6wTEr2KSojgb34YUIG_kE9dkuTBU0aIsb2bMKm9Jp2B2mpPjUsn4D26NwAbBc4wuuSRYcAPlsfE1ZOhOfVsMFMBF1WnTwNngxKWk_arHkBCaJcBqIehLqimbNZjzF2TGzsXxaJLlGEKqJ2Y6q83AZ0EojFeCLFqh_e2UWM6rFrJ6ULi8RX9OG2eyhU8vNzpC34F6jEhfrKfXJeYnLI7sHgVPNrLCcO_U4M7rHwFEtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز جمعه شد
زاکانی، شهردار تهران: تنگه هرمز در صورتی باز میشه که تحریم‌ها لغو و آمریکا غرامت جنگی ما رو پرداخت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81920" target="_blank">📅 21:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81919">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSupport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKPTmKtsHG8AVGvraPdYinn7el3zCn65sxyQeGg49MoK0M_Ggxjce0Ga9oHPkMJSMPu9iOfWK0bRnQxw1ZKfnzQUW7J8QMwSmEZbHBP-U2VGdw6y-mkglPateu_y4wqIe-SSNSwwD6Ih9LFimpangW9aEmv9j1X3LjVGT4FVVKiq1O36Wjle74SS8ujNe7Pm454vScxnRLYTcsTicGxBQOLAS8Wn3ks1XAUwxpXUQD-CoW94sITnPvG0WDO2cv1ahky_83ggAKEDlqX-PaRGemWmvtp3PEVZD4jx6hcefhEaS6ywqwzmWB87oBG3V4xgahsJwqgL839rCviqHO-mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اول تست کن بعد خرید کن
🏳
50 گیگ مولتی لوکیشن
🌍
کاربر نامحدود یک ماهه 105/000
⭐
⚙️
میتونید وقتی که لینک اشتراکتونو به کسی دادید که راضی نیستید در کسری از ثانیه تغییرش بدین و از دسترس همه به جز خودتون خارج شه
🕓
💬
پشتیبانی ۲۴ساعته
🤖
آیدی ربات خرید:
@SirenNetwork_bot
🏳️
آیدی کانال:
@Siren2rey</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81919" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81918">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سوپر جام اسپانیا این فصل بجای عربستان قراره تو ترکیه برگزار بشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81918" target="_blank">📅 20:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81917">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ6g0mYgl1cgb9cEO_VukWDEGwhog2P68_cnxxoymSqgJ46WFYhGJHnDYbZ4DkOHEwp97J4FoouQ3iLl4Ara7mdbbphIBrsvboAIx0hhuERIu6AVkP-Lx8WwnrUWf0ksGFQuHORIHXUkL55hAo0xv-25dGvfavd1ocWXupq_7b2AVUu2qLKmizVUbqxezxefnupVYD_Yz7kI6rR-W1NQESIPFK-QnI357A2WSnXQLMVxsx3VyZQ1tsWAlsyU5NvqeCsAU70CEz5g8T9fvzYI39VYNedIqjugWya2hoas6LSIuc3LeZ6ke1YHaSn3HUmoK2QKazggRXKrcTkMnrR5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش این چه رفتاریه با نعمت خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81917" target="_blank">📅 20:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=Pimz_cKXlL9O_xHlfoQBJsPolToMPmq0y5lLeuiXe8SiOlzT54PyJCsMouOLd5_teLakwKRFN6vmT-Z3tz5LrwnNXO69qg4-69uLV4Z6lqh7p7NDCefnHFTarTTeKg1W-fFohOKARjEz_SqemDefvvKX45uk6H8_DyiNU618gcx-hv9U1p7z4FZOly3dYPHXVN4Kw27-tQEvQTSjg4YxLXAj9FYdDHrlN8Lhx1YNOJKaSv5CDP2dK578QkwFsYbH0FcaTlZqeEsf3sXQs6KOO6UPJwk8vUeDfQdhu83h1ML0kPDlGrePMmFVRHyIPo9baihjdRZxM_JlkZGO-NIzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=Pimz_cKXlL9O_xHlfoQBJsPolToMPmq0y5lLeuiXe8SiOlzT54PyJCsMouOLd5_teLakwKRFN6vmT-Z3tz5LrwnNXO69qg4-69uLV4Z6lqh7p7NDCefnHFTarTTeKg1W-fFohOKARjEz_SqemDefvvKX45uk6H8_DyiNU618gcx-hv9U1p7z4FZOly3dYPHXVN4Kw27-tQEvQTSjg4YxLXAj9FYdDHrlN8Lhx1YNOJKaSv5CDP2dK578QkwFsYbH0FcaTlZqeEsf3sXQs6KOO6UPJwk8vUeDfQdhu83h1ML0kPDlGrePMmFVRHyIPo9baihjdRZxM_JlkZGO-NIzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادمهر عقیلی، قطعه‌ی معروفِ گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81916" target="_blank">📅 19:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMlYyA4nd7YSZmAms2_xHMrWwROY_1n4-12qCLXwg29IAYkPqFZ3mXICqFvMyaDwKPdhrQdMqPOGsNTNPtn3AE1LfPVa9MoDfN8DpdUBzFQ_kOUdp3VB3R5-LNBg4QwksEzKA5AikJJv7GmB3YaSnKuMi6k2oiqjq4Xr4ZoL34frL3yIFU2sxX15ncFuA830xKrmL2ndG2i-QLLFIgINiqthL_gKMgpj29JQlsb2yYspdU2joY5VmYJGnHeKwPNd_gGzNfJMPbpvb7cucnMDV5IqILW6knsQJSNf07uyCDstk-msJ4rz0sA2hvCqTNJQyKP-FeUfKAQBqWNfwyFPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دی ماه تا الان ۹۰۸ نفر اعدام شدن، یعنی هر ۶ ساعت ینفر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81915" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81914">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOdEQdQiHdd4G5DiBi-vreHbyGWng6NHTlD1hWCPKcl-ME0NMywSs3_LXF3nK8y1yoCTzMTXl-lo45s0K6qe1ib33xjWCGEiRDi5VSSVRzwExM9NhNly9B7gKA8rG9CIpExZHblKwnpOynMv7jJMovimsa-_eo4xvg36_0KVmYWgTaiahobN1_dFP0WygQ5wlAGL_AMILK7BPuyREs9jbNs_ZguvMAb5LJChHERKYNg42hsxlLEC-t5FGAd0auOGutwOMS-dfRmz9w2PvRi_YIHP9y1i66G_KLxUege2Ab_500WkSM58gLlPJ9jhpviirzYgEq9pgEY13C4DQlIx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز، تا ۳۰ درصد هدیه نقدی بیشتر
🎲
⚽️
برگه‌های پیشنهادی «میکس روز» را انتخاب کنید و در صورت موفقیت، علاوه بر مبلغ برد، متناسب با درصد درج‌شده روی هر فرم و تا ۳۰ درصد هدیه نقدی بیشتر از بت‌فوروارد دریافت کنید.
👍
برای
مشاهده برگه‌های منتخب، به بخش «پیش‌بازی‌ها» در بت‌فوروارد مراجعه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g16
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81914" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امروز سالروز درگذشت فریدون فرخزاده
فریدون اوایل مرداد ۷۱ تو خونه‌ش تو بن آلمان به شکل وحشتناکی با چاقو کشته شد و جسدش ۱۶ مرداد پیدا شد.
بعد از ۳۴ سال هنوز پرونده‌ش به نتیجه قطعی نرسیده و هنوزم یکی از جنجالی‌ترین پرونده‌های ترور مخالفان جمهوری اسلامی تو خارج از ایرانه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81913" target="_blank">📅 19:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igINhkTUiAbrOLELe88NmNcNhGV7dFMHkpajoGxX0PCmdmWpD7ndSyV82At6s9YxmWr0aC50SP11mmHo1iIw-mbVlCrWtbDWyQQxftfxFCJOXQjhaPUhJ_5wGARxlRrc5VoMwn8pWM5to8r-GHm6yPGgXdqBD-BJJEvKek0PZh82VLyXX0AQ7zk2Hyxu3EvNbLxQ6SzU3vVTFrm2QR8Joig4mp7qUtSIkMtmPZjejd1ZOwS3oFxhGzb8EFBhvzbqT2eXoGdPUPY1fiKVQkwUXY8wlSoxpNBO4szp58l9BketQ5x4_2iIi7sRH1Y1EJRQw5BuTZGZg8Vlbd-W88yjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YH2scaeFtLq0aCgBdWXl60UYwmwNqqIWVU2AklEbdG8QD10jhMM5x5BiunWcWH7a08-YJ6hXwQxl1KpR-C6vZFu54OHwZM5RxDnZY5tvaFOm5Dd6YgSk4jwOquLfUTsuuBhOkIQPgaEj3mJLvvRyjGe8fugjV78HK_-5128fDvP7VIvnBha0XBgpsx9dVI66g7I7YM4f153KpAQkFpISyrMcINXp-CTSd81P3nJ3WC12hhg-c3rGIPfYN8fsn4jNBBO55oVCK67QHXPeu-AKpMtBt1-xbD_vAGhny5W8rnvX8e5S_iF4T6SUyR3O-3F4gaqnahyxB2gNrcKiLo1t4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از سرگرمی‌های جدیدم دنبال کردن دعوای تیک تاکراس، مثلا یسری آدم با این قیافه ها دارن تهدید میکنن که همرو میکنن و میکشن و فلان، از صدتا استنداپ کمدی خنده دار تره خلاصه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81910" target="_blank">📅 18:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptnldNaz6V2GR5_ZXQeO5-2_IRvdZNKidexBpKkq02OBUmjdeaqiupd5LePpVeE7IveNNymOISfQy4ye9jQNOx0mee_f7CI1_QADWf9UoAsv8bUSHBxdaibeD5U_EfyqoiHj_Qtm__5-VuY4P5ywaqa07hLF3tYJ3WosNpzpVzLu2eiwlj10f6x7hiAm9-xe5GFDCOO9KkY_U7oOKnLkyuwY3jxf70YTNPlfUlcqUoc-ziGjfTK0Vh802XSzBbdt1V3DXEajNIEgDwjwN3_qDCKFi4S0N1kfZZM0ZaYguxg0LPcZeB4-CI2WK9AGlMc0ezBrfbHzvu8atvSzxTL2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIPG6AqfnfMkalin12AE_kQ20ZC0NJlHSH0x2MnEOFh3GI8e0tNGQBAs2SBcpez9qRZmttmumXvIN6gIS0RigiaqhBY39rUzPtmWDVtcUeJRYttwQGKETqZbbUwuc6-ErRwtJCjITVeq8H6OGWHDQhY3E2tSrGDSXYqQAl3jBi-hPs3Li0WG9GIwzC6uqLz3zKdpspEqyyfJro_8F2a3F2n0U_RudqKgrHN0RrXgzx_aRF9RET1OJhfUAjbXNsmYCovdxbF8mQJ-uMxhneOCUFbnhgtdMLzAUN4jsXFL9dmo2KJC1VjDS_l4UphmYQQZyKfky4naB9BSxO_JFuB-dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از سرگرمی‌های جدیدم دنبال کردن دعوای تیک تاکراس، مثلا یسری آدم با این قیافه ها دارن تهدید میکنن که همرو میکنن و میکشن و فلان، از صدتا استنداپ کمدی خنده دار تره خلاصه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/funhiphop/81907" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVKuaAU5E0xnnZg1N3ssaGHuS7wHR6j_QcYhjvQaf4WSak6nVMpRoghrJuFfkiCZGoTS6u2YAPKeXzo0LaIDJVpomGVh7wUbIL_UM90ucFWc809D7Y1Snh-l6Cotx7G01QooutywiMEqH3XUHZlGe4iwgOldS_OkFG-EGaktNuH5wANai7XmP7kyrhuRNEUia3wkH6MxupFRAdZs5ktyYCo2KNHuC8xFnDrSlxpi_jTuNJi8dmrhn_qpAoHvimmnaxME9hrjaDx-iJAE8em8y1M1eEPH6uioMIlAF80TF13X9Uz8_Rr4kgeOsk2OcfHw5GBimh5hW9vP9uvytcX4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبونم لال زبونم لال یسری منابع میگن حال رهبر معظم انقلاب وخیمه و هر لحظه ممکنه فوت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81906" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIBr4nxbKjwUPzvM4lliR_otjIcXlBJNOU8rQk_9HHUH-tW4FavsZ7YPIhYkCs6Nnp6bozEUTEWBW2EpPB-ExCPolSdAPnlENGg4iYDKuB5hYjTxy1MvWJM9FU3iGv_4nfeDXQWxRPTxnEg4ghXP3-iMJuFGt-vP4DFOWUgsLrRoFodhDK8ZqxEIlJZITgr9nVr2KonFVDMiPKCA3-wnBtibWmYnkq6XB-l72gWFHY8RaoTLlmwnbiYr3LD1Ahs5fb2xlmrJyHLFdr5iVFaj3gbk_eKt4ki7drzy9Yuo2RYsgbsp-7DfrNfRbYZYlQwCL-zwTSLjnH1-ofY0zHphnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیارش خونه ما عزیزم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81905" target="_blank">📅 16:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81904">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همه این خبرا برای اینه که ویناک طلبش از دکی رو یادش بره، لطفا چنین اخباری را نشر ندهید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81904" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عربستان، ترکیه و پاکستان یه توافقنامه دفاعی امضا کردن که هرکی به یکیشون حمله کنه، اون دو کشور دیگه باید برای حمایت از متحدشون به جنگ علیه کشور مهاجم بپیوندن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81903" target="_blank">📅 14:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81902">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZwgty0aUZ54CmkJAfD7fSarolj2PtLL1-nVGCI_850cCQZsCsyJ-wbimCM1c-lJJgu87bozWfw3pNDZRJPDIEdgG5TOPtb0HkNMbuCGR-qgEVA-49o1CvV8BHAY4Si_mC8FlNXxFKgdF9oX7pmapd9KnSnD6TR7qyZAlkir9cNkoL8R--ZKwY0u9Xd8JJZQsNJki6wVnvW0a1qf7tkRq70-JRwrUMrxAhAYbXpvgmpJ0-gMYDbLj4qwaOdiDGLfu4SJXvulnQflqiv96_PL9tTqofbkDf3bOin-N9TnJMCmpdElKXqtO6ZhuW58sfoXmc-rGX3Kb1IbOdjTEGxYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من از خوندن اخبار خسته شدم اگه بخوان بزنن روز میشه همه میفهمیم دیگه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81902" target="_blank">📅 13:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81901">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMb8OaHkEJy7f5iHUOLRrIwV_uc_bdO3dGL-FUUbVuGAeVmWK50HC5AJbTun2U1H-jZAUxBcxbLkw5HFU_QWKiiZsOe5p_1Tmzz1gROnmHi8WmBUY8ccQAKw1MOKa4rIXs5Gzf4iKiSu_vdy7hR9nUQ0kd_slz7lYjPOJwWy_bWudf4sjy7tDSqdCSpNwqxbB8DEJdwbu4CpbOnEs0Vd2oE0qurG6cOg3Bv5ufD4Pk9eqjb2Nyfse1haBPnVaExVthwn_Y0151J7XfsasPOhlfjiYAP0vp1eluwjafBKgkPCXOQFXnbNZFmguzA4nZzWbZTVXq63w4lxGnKD2V5kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah shit, here we go again
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81901" target="_blank">📅 12:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81900">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iphUbZbpBt4azrNeIF0AE1U3gar1m57wPEcsI0ZYWzL6sxA3KUU656xMULo2Ym5ILgMRUcOxSW0Wogmv8mJRVpuZWekTInfu2nmj5p2gOVU8vwEi2OX2EfXuSCrHxN2S53J6gExdX3JlQIXlQLp4aTDihX0lI8DNvSzTXNh8nDtiK0O2CYySRhPIB3T22zuAHSOQDn-IhgeM_DEgP-5ivVwg0z4K4gxrJ9yOjonFV3uzbr5kve_-Wm3LSUnPTNi6kPnW-xlFyUKkx53-6vbCoPO5Y5za95AW5NqleQwEqHa2RUIcBmrLzWlVGpi4pZY0jDTNt4A_jfWEJCqbCmsw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی اینجارو نگاه کن، ایران تو تاریخش هیچوقت گنگستر و مافیا نداشته که تو دومیش بشی، به خودت بیا  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81900" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI67dxcIJes5qauRBbuAJBBk6laKDfH58gB0IEMeQBsobMp4pQssSTV1J9zKawai3zwAM-u-SeOslHJgEEr0Ch1OZsuWaXdfpwisbR_Xwm1ArhR_fXADsTjt0a_Z3twYu2aJSTdmPpiOuJfW22tfNpRFCnBjTZcPx562bn5fB8zme3xZiNVzaD38v_wkLccUN2wbK1R0ZhtLszAHMEVbHPzFzS378qHZQNe29uROwtF-GTeN2XpTT5l9xzEZYquUY0IUXsuhRLUN0F3P72qhGemVUYI11QMJEHcfM292amjVyrhxpxMUMULCNTK3TOnqdWZFFpHADOPFtlljr-syfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز، تا ۳۰ درصد هدیه نقدی بیشتر
🎲
⚽️
برگه‌های پیشنهادی «میکس روز» را انتخاب کنید و در صورت موفقیت، علاوه بر مبلغ برد، متناسب با درصد درج‌شده روی هر فرم و تا ۳۰ درصد هدیه نقدی بیشتر از بت‌فوروارد دریافت کنید.
👍
برای
مشاهده برگه‌های منتخب، به بخش «پیش‌بازی‌ها» در بت‌فوروارد مراجعه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r16
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81899" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">متاسفانه ویلسون یه تماس تلفنی با پیشرو داشته و اینم نتیجه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81898" target="_blank">📅 11:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هر بار حرفای ترامپو میخونم دژاوو میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81897" target="_blank">📅 11:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjYRZ_0zx95L830tuQhLQLjuXN5Mf93I7HNwwusZqIYS5fFb4n_8fAyCFUnlLRgWrep2xkirSuhlGdwOpcds3kgDHWvBRRBKmNQuf6BoUc_EGDKLHiOojJsF13cYLh74_1ZhMAXDaAl0f9lCbNgS8OYqdvQ25MXRRwew6-yZRHxjqx8eyAHF_KkmC2seNk3bv-VBuxsxnSTZavipcGhsjDDHDlwuATCaX-pxngCwxkFnvGghTFZ5WJg5ZffIHypNn0WVHCySIk67LmEizu3b-3CAnUf5CFxCRCS3_ZteAR4N0t9ZfxmeSabLc0uePBTB5W9b2TO_YiqiUlRCTiqVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.  @FunHipHop | artin</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81896" target="_blank">📅 10:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryDkshHO8Wy-dLlxSBEheABPjfzkz3SuEyPp-hcH_9Mn2ISuhpm8ea8LHbEczeI7VEEDv4Ywz4LB69Afh5VUvHR7P72ACuVmS-WKu15hikmt0A4_AQbn29rZFNyvytgXa0qC8Dy1NIVCZYP_E7Cb1KfK0OrxhSJhQ3HO-qJuwc7xHy6SPwd7fQW5kkQ1-17UkO0u71D7uBrKfihzbLascMZYW7s9lc0IAB9dDiWcWkE-64Gv3Yu2r6tKhigzwfmluOGe2yDiOCQy1H5nzws2IWWdF0KFCDBjVD2Ddjjkrwj43wSd9ere_hbmrtAO7HHyY49wZEcK2TYWkRfpTZw0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مرد 26 ساله که با لباس عزرائیل از پشت‌بوم بیمارستان به بیمارها زل می‌زد، توسط پلیس گونی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81895" target="_blank">📅 02:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فوری از رومانو:
بارسا و رودری به توافق رسیدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81894" target="_blank">📅 02:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-MP7xt39ha735hTuV7yUBJth9gmBG1mQ9LF6UhtobVADSPQw0oy1TZuYmxQhSv8Sz_aHqMis6spTbNVZ7YxCg8xVr406bzncc4Mxdr3hk9QtKV2MUdILTv8LzTaossjxIpVWx1jX16ezdxirbIcJkV44768cR8WLSfzLAIskx6F9SfXDHFZ5nfwbqIcfmxQurKxlUySKn8PIHbt4hYWm4y98zua789vDQm7_MTDmigh2RBhk3-Ux-4UdBc6LhLXsziZ0xcDuV52IJYA94hHjG5wqwmnGWqHDDeRV6G6xUMe28r0ac6pUh1Hv-xF5PZBEIA9u6Yu5lpzhDkQfRE5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موفق شو دیگه بیناموس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81893" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diNHosxXEZj-grwW2PdI4XzKoQiV4hc5DWV4AhRTDvy2MJJhCiWZMlmo-gIaTPaJ8lLpRuRMml2Q6FatHInI2SCDzFXI3Lp3tvSbxH3fkAnV_OOcg8spTjyrnmLbRf7DSAwZw6vDdpYVBhFYc9gX0xOO_1obN_0Hfy4r0VKAda772drk9yv1ZJcoCTO3eCt7GhOeKbpafQUKvGgZmlYDEudS4aMLoYsm1zfWbjFwcZ7KeeewjOMB8OjDQChWv_kfsPtZa6i39eC0TD4haPKHtEs001tti8gh08M9Gg3XOUoDIoZ5HqOHlqkjVAj9R4GDNMgXJJw98B7RzZpMvGWCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده نفرین نکن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81892" target="_blank">📅 01:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وینیسیوس تا 2032 با رئال تمدید کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81891" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فک کنم دکی بدهی محمودو صاف کرده دیگه صداش در نمیاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81890" target="_blank">📅 00:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNq_PwbQAFWvvXDf6uxfKwUIjwMpW6w4rhiqJ9sdfdGY9mKhG1m4_5kQBIg-DjZR7khQ-DvRPPasqO3N5cLKJQfGz4V1FMvuFOozy5qgk0l1atzEZ_Vn9E1eO57T52acfXsgD8YRGzgYN2qcIc8VvJr1i0sE4-6z5ayZaaqv58pq_klTQVEv1YjfZ9qknBswAcmEHuqQoIRBgErqO4B7PaE0hoSJLB7laaFLk1CVTfzbZwLAR6oatvsbRkBA5GypnK5bju-mry9x8nURvmCMJd0GE49D7NHzrStCaV_P7jxvK06PQHP2S5geVcZ1dYOmfW-QpjhNrimvmWbAZWJebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjz-4pWvQ_ptnNXij4uHrxY3WFB9V4aZkIpA9FUk7g4TLetGHM33E9bakO9LIuTPvXdNiJznISvItgJL4hxEl0RiyRsiRfjSEUOwV-HvF5lDdWBP6ItyR3i6WFODcbXBfrh0A9JmQxDjKSveyuXNaNoR5_8pfVE8sNY_jBaIp-SAwoL_zPRxx1sKywfhcF5yTxq9UF2YziNkQJ2NEg3F5RRNay3alDHFCVcpwisQZlB3xpKfFRBFXlYJUOna3i7lT9eMruC7EnOo0dzF11NyZBlMlPRg06MWSLZs_r7bhHQciVfrVOKeLvgfnROrmrmd43O2r3ppk8Hf4w_2iEsbqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba914a5882.mp4?token=XnL0fCV3YCwTqH9DO6FbadN9FKq2vfeStzzFcqTIoguVVUsN2K0eqrUY7_JplZC6zvCQGbYwzIwKqY5gI76-IwD9pYPQPCrjAYECe9KkT1Kp01aV-OVcAooXGAB2-qfTNfowcJUtrdA4RTbIc74_YSUMcauHSAA8GKv29Bhl7GXu6VT41ImMx29oPWS97VdK2WmVxVP1vwYVEpuOSuTzGcx_BmZWysESWwMg9B8Puv4D53Np9XaEXb5cJpgNROBtsXjnFdsuFk5ymrQmj9AIcfIIHOTuJuNdHuu7mQ4NroAtwQaR0dqf1mH4teLBbi7eSechcISqpN6awr4WoeDwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba914a5882.mp4?token=XnL0fCV3YCwTqH9DO6FbadN9FKq2vfeStzzFcqTIoguVVUsN2K0eqrUY7_JplZC6zvCQGbYwzIwKqY5gI76-IwD9pYPQPCrjAYECe9KkT1Kp01aV-OVcAooXGAB2-qfTNfowcJUtrdA4RTbIc74_YSUMcauHSAA8GKv29Bhl7GXu6VT41ImMx29oPWS97VdK2WmVxVP1vwYVEpuOSuTzGcx_BmZWysESWwMg9B8Puv4D53Np9XaEXb5cJpgNROBtsXjnFdsuFk5ymrQmj9AIcfIIHOTuJuNdHuu7mQ4NroAtwQaR0dqf1mH4teLBbi7eSechcISqpN6awr4WoeDwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81886" target="_blank">📅 22:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7YC54SCOfFUTZd5Ig80H_0szdI0E48HFUr56sUceamY4AxbmmQ5TcvVsqG_LFHMZssSP-9OnHwQ3IrdBsZshR2ss822ygeLufOhwvnL_lKZwYoEwlGO2J6Rn4W1ssx_5UojolFBJ3Rf_eSG0tRjoTKGAbf6wvlQyFLnfhJC4nCWqbNlnAnSF9j8TS9EHiemcG-jvvXJI1SOV_VU1PwiCh3K0xYnT6XRcaNZFXgVDXqw4Su9c-NJj4aPbazGcATdgBMo-VmIhuWSZRuBI_QZg8Y9Q_RE9wx0bzHqUJA25_JJGVR3G3aqOZ4JhWLDFG9ns1k3_EXyJw0LyDq75MdeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا.  ایسم وارد رابطه شده و عکسش با زیدشو تو تیک تاک پست کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81885" target="_blank">📅 21:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfEsZOW73_q4Qk7wLerlkWD6KyvYQTMMYjwOJe-5qJK4iQviJxtHEQzxlCfUyEDWjPcWbjcwtQzEQwvDtafk_A7Xe2S5AwcA8Cq4f53VW6r7dr-nI3vrrDh3J4wuoMVyCUYucS-uTlzpA-xfW2RHx31147A5CrJhpa7uhZBt-O1K3yD9aoRauKuYYb-w3CZMEMatRCmZS6Yud4s8pUr2qeungPXkgrMhb7zm-v3xn6G7pJIhYMr27pS6a8_Qgq64yZS4H5YKjwWPIln3eHqKhYqdu4szxbxA6p90tWQYyL1pvy09rBuOinBR2f7SLadhqAeiHIy7tt1IBRqBtV2MDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت کردن رو از کاظم تو انتخاب هم تیمی یاد بگیرید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81884" target="_blank">📅 21:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترک جدید ویناک به نام “پارافین” منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81883" target="_blank">📅 20:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hs6VhXn_mCHiXJpM7bqxEiAG3Z0lfWcuXmzyZ_y_0CQPq1cqip-ScfoxCVMCxqrYQB5heWQkKfLBrjsMnr34xeaChLMV5x-rzW52qTBrahP1fi-u2sIuRMk9GH6fMPz3e1a3QmsCQdrJ_g70cMqGpRj6MJSAyVJ-nWpq2ndnUXJRX_d_ovwAxCJna-4yqnCjB1sIkYkdXdblgRPCIeA-dSgd46PP8CmmekCFrQT8FEuecls5hbNqTLL5HbOxhdoZGrprWA6-RsdMMo7tEZKiNREtSDr27Pn0lZUvH1E6VrwnRShkFLyOciJIVpz2pHp06nNdTJJcVqrD-kOt5b768g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام “پارافین” منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81882" target="_blank">📅 20:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2076b95d01.mp4?token=bZM94YFXeqdubRj_GB5tITLtDGmk2EnNmE-t7FE3xHfi8Y-yhIcFxjI52iuY4A5ZGMwKtSpYxnzro76qimFLEYzBqC_1nh9MIDbnLCuPBKlJndRUb7SKGJkLqDQ6U3H_yBPO9UA6BpBRr35YVVUv4bYw8fF8GRtLNS7InF2d7kAyxTQXcvWG5zF0POnHFMXc9tVQqy2fQf4WN9hkEEmGyFsR2wy9n07qKxoZRtkEHfVSb8hpZDiZOM0kdlCP9Z4iDI-IANr5SqT-wPgTEMDyDhdvK5odt7yH1RcDzfQWg7fGHu3NRThrx8BF4vsd3nE1Uj0rMOe31XaqelmMRK6mAXubIvtUr3ieTHOddTBBaf6veFk62AFzx2eW8s9VtOzMBt5I3MnDnvvQe9uOoAgKe4jVtBWYDG4sHmRGG9hdq0nQMYQ2au9KxB-18P3Ii1zMnHT8duXMXD8CjqocGwBWT0URcNsBFM8XqsA8YwTdQXVkKcUc9ens0U-95hu99PjgzcnNAjH-rzjl228yuDTvYmxtZSvYHqD8SXM8DFaTbnDKMKY_-zeVo9hH5pjF8cVHr5KDMxtDJMYwDZCTy0BTcXbjK88azNb53rhQTxvYa5MB3d3u377C_5JxY1Hd7W8hko-0jpK3_voNR9DgpGloqbRQpNVw5wSgI6AA_d8-qdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2076b95d01.mp4?token=bZM94YFXeqdubRj_GB5tITLtDGmk2EnNmE-t7FE3xHfi8Y-yhIcFxjI52iuY4A5ZGMwKtSpYxnzro76qimFLEYzBqC_1nh9MIDbnLCuPBKlJndRUb7SKGJkLqDQ6U3H_yBPO9UA6BpBRr35YVVUv4bYw8fF8GRtLNS7InF2d7kAyxTQXcvWG5zF0POnHFMXc9tVQqy2fQf4WN9hkEEmGyFsR2wy9n07qKxoZRtkEHfVSb8hpZDiZOM0kdlCP9Z4iDI-IANr5SqT-wPgTEMDyDhdvK5odt7yH1RcDzfQWg7fGHu3NRThrx8BF4vsd3nE1Uj0rMOe31XaqelmMRK6mAXubIvtUr3ieTHOddTBBaf6veFk62AFzx2eW8s9VtOzMBt5I3MnDnvvQe9uOoAgKe4jVtBWYDG4sHmRGG9hdq0nQMYQ2au9KxB-18P3Ii1zMnHT8duXMXD8CjqocGwBWT0URcNsBFM8XqsA8YwTdQXVkKcUc9ens0U-95hu99PjgzcnNAjH-rzjl228yuDTvYmxtZSvYHqD8SXM8DFaTbnDKMKY_-zeVo9hH5pjF8cVHr5KDMxtDJMYwDZCTy0BTcXbjK88azNb53rhQTxvYa5MB3d3u377C_5JxY1Hd7W8hko-0jpK3_voNR9DgpGloqbRQpNVw5wSgI6AA_d8-qdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط بیگ شگی میتونه وسط تکست های عاشقانه به کسی که براش عاشقانه نوشته دیس بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81881" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJSMUS-FK2sWUEaOJoHBJ3k3zdvjIm8Ek4ARUUZ-pdU7Y7yG7sxqL-tTU4S9n1D1UX7G6dw3irv2w8qJcyddHeAgmMPcFDVK4Ffh-QU1ttVWU22_Bn5ajN39FkAmQ4TKPRPvTjJMDQaOOis0swhrvnObMWsSqFy1hXBDRFYz6bfips_GwakGeX2t1JjjJt2sWw79vtfRbFS0YkA_Szv16FI9hP1E5kUep6HmnKiKfqAca3rHGeU0k_LXWwGV_IYvCV8uU8V1XJ_0ZewLTsD7mmNbJExbKLWN_WM4PDbh5RhpNDxTzLNhZLN4Lo-VDG4LakA-g9tuFbbgoNgeOxZJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنریا تارگریان هم همینو میگفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81880" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHzIZgXWA0AkTFrsKX4YZU41eylbTlYmtKmY1_z8u4euDxWYRIuBVYnaOZ6wnW_bdHuZBv82mw8Lb24VZT0kpQey_zT8NUDVVTzjYY1X1Y7ZACd7EYeKQ9QLSLgTFB-__BWanHTuB2srYZUd5men4ac9amA9xKsq4_HsYrsNVq97c_kZB_ychLHGo53mqfC6hbRl_qJijpgYENm0n50AKv5hoU-0Og7Ixeq7lSCsGGYqO6kkxoLPA2ekoYZ5oJ6vj_lEmq5LxybrfJeVU8KiCuaYyQl96TbZmuOYEEMPkGGV4paA2AQxNadNnZRWPErWA5ItSXIuecu2_8YLlrLMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g15
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81879" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسرائیل مثل همیشه داره جنوب لبنان رو میزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81878" target="_blank">📅 18:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بارسا هنوز ۱۰ میلیون یورو به سیتی بدهکاره از ۲۰۲۳ که فران تورس رو خریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81877" target="_blank">📅 18:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXL5IuidlP0asFLBTJJeXpF8zYgvh_wjlHGMgWnaVd_C7J7Zaajv9-smtQAdnEmgalojxVwTp-OfTWCs2w9zFT0dv8ny7AWDIBnMDgIW87bUDRQPLjsdZMDAERERw_nuPGdkxpz4KmCw-AO3YYrF61JL5aL1ZuxZYqGaQOUDZwbZgfslu4x5Fwjs7XHt9Txc48FDPcNs-yAGQJxDl8dzUfhV47zwrHrWq8flH7NtlznwM1DYJSJdMqeFuvk59Ol2yjyt4GOgfFNWOb5MNp8HvzaxnTF9ylVEqPTxNCU37zfrvEXMRzycQU77CdZ7a334kOQfGby6kGavQnkk_6DpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس بچگی دیامونده،
بازیکنی که با رفتن به رئال به تیم دوران کودکی خودش خیانت کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81876" target="_blank">📅 17:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یوهان کرایوف میگه
اگه کسی برای انتخاب کردن رئال مردد بود بهتره که نیاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81874" target="_blank">📅 17:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
پدری رودری پدری رودری پدری رودری
چیزی نیست اسپویل از گزارش بازی الکلاسیکو این فصله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81873" target="_blank">📅 17:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ماجرای فروش دریای خزر به روسیه چیه؟
دریای خزر در ابتدا در اختیار شوروی و ایران بوده است
پس از فروپاشی شوروی این دریا با ۵ کشور (ایران، روسیه، آذربایجان، قزاقستان و ترکمنستان) مرز آبی پیدا کرد که ایران اعلام کرد هر کشور ۲۰ درصد از آن را در اختیار داشته باشد اما ۴ کشور دیگر قبول نکردند و درخواست داشتند هر کشور به اندازه مرز آبی خود از خزر بهره ببرند که در این صورت سهم ایران ۱۱ الی ۱۳ درصد می‌شد
ایران هیچوقت این تقسیم را به رسمیت نشناخت ولیکن نتوانست بیشتر از همان ۱۳ درصد به خزر تسلط پیدا کند، حال شایعاتی منتشر می‌شد که مسئولین ایرانی ۱۳ درصد را پذیرفته اند و در مجلس قصد دارند آن را به صورت رسمی تصویب کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81872" target="_blank">📅 17:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOlDTN8cgZkwRlDB3IoyAG8v3Dbn2ToKhh4Bn40fG9g5IHJ3-I3uR6gHMVelJtHpRRZKGr9faevxaMmkDqN6ULzgHZDKTt4KQuQPQurHAg-8-AMAflzx5oGYp7ihYqLXNTLyyDXR_iWm2vkzY3ZkL8WJZeuBbHk27RA-JFu6A0KshaTHvu0qhpHqEUI4Pd3gT7fGlZBNOHEPpLDOnktXequwgk7rkTghvz1X9x-xPJRwEj72GA-yHCx-slfILY5o-RGSKX0FLY3a7k80hLJ_KEceag20bSIEjJcIzsUEGXduKrzmLmDqF_jHIdsDkWhWI96ZRUYhk1Wxb0RwTdLKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان پیوند کلیه در افغانستان رو ممنوع اعلام کرده
گفته چون از یه بدن دیگه یچیزی میزارن تو یه بدن دیگه مثل رابطه جنسیه پس حرامه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81870" target="_blank">📅 17:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آمریکا ساخت یه ناو جنگی کلاس ترامپ رو شروع کرده که ارزش تقریبی‌اش قراره ۲۴ تا ۳۰میلیارد دلار باشه و هزینه کلی توسعه این پروژه ۲۷۵میلیارد دلاره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81869" target="_blank">📅 16:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بارسا نوک و دفاع لازم داره بعد لاشورتا رودری میگیره</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81868" target="_blank">📅 16:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سیتی گفته رودری رو به بارسا ۶۰ میلیون هم میده ولی به رئال زیر ۸۰ تا نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81867" target="_blank">📅 16:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81866" target="_blank">📅 16:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">81 سال پیش در چنین روزی دمای هوای شهر هیروشما به 3 4 میلیون درجه رسید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81865" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQxvElWSHADrobIk2jnbrm_NO6o_T3s8hnklBWjFrslYaPf3dweozGAx1WJCu5hcgOKX9xrSiSUExHRom2retdSV1Tdshbk9IC_DcUtqB8HNS82-PBca1cTQ6tS2zsIHik1VfG_gfEQdZP5L6dReKQZdAZCd1DQntYSMteLOlscAYOhpac5fqIvSLO9wxpcH-cLWee7rTgVRCoTKAV0knnJpNY-RTE-W0RbGAEBlY1fsNopl-DrejCBW4HcNgEbPUfTED6IxCmNwa-ztu4dm1RVVszBb4p9wD1CoyXSu5tEbD1zXQjPOQnErngv1x5JJf-7GXo1gxXS2mBzQnvkBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای رکورد ری اکشن توت فرنگیو بزنید حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81864" target="_blank">📅 16:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9VCzoPJMRLnXXymAnGFceOItpbfO6qaDOW-f5-SSCSvJ_cUYBNo82FvPXK4xG2tNG_2SHnhQfZKKhgkkQRWuqvpx3j2moKLT0RGF1GSgp5XCVverircPdUp5yZ9PxSynNlhnn7x4wUPyFJ5Pj-cc8Ogte_MblyrD908gDSG2jaBupn6GzfTazeO8P3vgDGSMHw3Ngh5_ntRkCfiir1i9Gy7GLvz_h1l19TVJXImAPM1hCQ7rr8W0s7OGu3hd_LC8oPSigf4cxRZAOXkuEUKUE7sXktQZy06dasOVUI1P-RSOjOHUviE-3VscIasSi6swKk7DrrgNDoa7sUftXdBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسری آهنگسازا هستن که بیت هاشونو تو یسری برنامه ها میزارن برای فروش و نامحدود انسان هم میتونن با پرداخت یه مبلغی از بیته استفاده کنن و روش بخونن، اینام همین حرکتو زدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81862" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ما خودمون میخوایم از ایران فرار کنیم اونوقت اسپید گفته اوضاع خاورمیانه آروم بشه میخواد بیاد ایران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81861" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یکی اون وسط گیر داده بود به یکیشون میگفت نه این هندی نیست ایرانیه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81860" target="_blank">📅 15:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8I-o_V177WoHRTSMnFNyr7pRFJ4Fn-B9C4AyN7cfqX3qR56b6TdMQN6JGmATX9IHHTy2ClI9QwWOs9SmJJvpM7jzfM8-B4jXqDq76FKom_2vg89Z1mCa6q8d-rhOk8CAo1M7Wqk2CQdC8YxsGawLbr1JJFshxpgc0aTl2J8-t-eXdpxA1BpIXZJWRntvLyTBJdLpxDtk92PUuzO3685TSR5pxJwi5OKYQDAB3D_eq98H54_CkBE2LbcDdQVQxgYaDpK6KV-bBpDXxXZpr7bns7ChOg0LHOyEBe30M5sLwPoyVX0nUSO2qQXanp_xwfbXt5pTWN52m9ejx3oeNU01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا.
ایسم وارد رابطه شده و عکسش با زیدشو تو تیک تاک پست کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81855" target="_blank">📅 14:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEb7BVNUcTQkwt5VSOcNdF3EkawQDF3N3QSFcM0DpVMh0vhup8J9a-hhCyDZ4RGvSFLWzH_fHp86DshuiBt8VVtyeYnNUwm60_beMD5Znj46QRVZKiUZxLLg3auYvVZD2hDYPXuC-zzYMpVXu0AHIImu5E8q_EMlfmqVznm_Q6ZnA-WRJ3Iyxp5oT4ILiSaPRm7TIQMsKQiaOIQ8LNfoIwjVQQ2N1S5qK6RhSB5DWfD6GwLGCk7Q0HvNm3WCoahyvkVW-yrV3Tzm_GrRNwCpFhK-napHk8H_FOMWpmMfB2OAbKGSA75JPBXpapm_eJu3B8NG432aFgApMDIxlOsjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین چه خپلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81854" target="_blank">📅 13:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ساعتی پیش یمن یه نفتکش سعودی رو با کیر یکی کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81853" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81852">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCrOZS1Fpg7kr3pYvRH4L5wVjl3SdAQ_c4-qSlh49pPU0CYAn0p6KvtIaS9YoZWnDgWwkwXch7y7PmXlAL2BrJPcphj0uRdP7-QIvbJ5Leh_XClp4Pc7VsNcZhb5ibhQYuxLsHJHeY9b6bfTe_3RKVU7XwN4nnPD2FnvQSrlR9o-3P3UiKYopfhHMZ7lvuSnVdBq0uGhH3TPiBxL6C79-iKI3S1adaboOyk2N4duWJ-AhLUwK-F_X_-Nv_AYAfgh6lieB03fEh7cs6gNOgyaYI0mPzALUhERJ9YaJrxKBRcW74hQOs-14sm7jId9tp5G4LzO5DHuQCjupalRF75Nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا به نام I dont Give a Fu*k(IDGAF) منتشر شد
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81852" target="_blank">📅 12:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هفت خط لوله نفتی در کشورای اطراف ایران در حال توسعه است که بزرگترین سرمایه گذاراش آمریکا و چین هستن، این خطوط جایگزین اصلی آبراهه هایی مثل تنگه هرمزن که ایران فکر میکنه آمریکا رو باهاش درگیر کرده
پرتقال فروشو که پیدا کردید، بگردید دنبال چوب جادویی ببینید واقعا رفته تو کون کی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81851" target="_blank">📅 11:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه حوصلتون سر رفته بیاید کصشرای ویلسون راجع به شاهین نجفیو گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81850" target="_blank">📅 11:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187d19388c.mp4?token=IZcODEgLLTEOQfT33lBzWt2cex70blwagabP19Q3gCNH-3oWLeI6KVFuawWxCC62ixhF3dAX7S6vMNiX-nWWIKc2ct5mebWbDp0tMqQzLBM-BI82BuyNM5FDxhfsLzXavs68_-8o1b13vbnirUNGaBl9vCNm4qIwM8KkykAOXg2Hkwk_9TVho-eZ2jkz4h6cbEvQiKKhaGpIRqyQyWxyw5wxm0OvDnK-frDf0oL8AZAoGr0H08unrTjanXZDKAPAgXlILmFuwp5mQ0RGOVs9toH8KbmYDUjS8tBXCQM5TpyEGZmTopGD4JRIISnoIuXvifv-cvklALw6UBlPsdBxQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187d19388c.mp4?token=IZcODEgLLTEOQfT33lBzWt2cex70blwagabP19Q3gCNH-3oWLeI6KVFuawWxCC62ixhF3dAX7S6vMNiX-nWWIKc2ct5mebWbDp0tMqQzLBM-BI82BuyNM5FDxhfsLzXavs68_-8o1b13vbnirUNGaBl9vCNm4qIwM8KkykAOXg2Hkwk_9TVho-eZ2jkz4h6cbEvQiKKhaGpIRqyQyWxyw5wxm0OvDnK-frDf0oL8AZAoGr0H08unrTjanXZDKAPAgXlILmFuwp5mQ0RGOVs9toH8KbmYDUjS8tBXCQM5TpyEGZmTopGD4JRIISnoIuXvifv-cvklALw6UBlPsdBxQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیدونم چقدر میتونه این ویدیو براتون خنده دار باشه ولی من باهاش فرشو گاز گرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81849" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZaJdqF6XrffLGyUTj9ErEjfq0pxyD-Q4n7UFMnniTMPHbBW0s24kx0z5itZli0QDEZmlfhtAQ4jOdIxjioewO2mw8VWHVzTwa1WiaYnapLOHJJt8QgK-bmsrEBX1qjkmRfv1V1eExObzAyAsvQYA2N_NiMHWzplurjyxeFE4G3nslz26wmBR339Jv8p9sM3EeAYphBt8X7jXwM7s33acmgPOCaDrYPGksxKitGSOp0MM6vv_0h2VD1RAESAoAQ2hEvL7eB3_EVG7sPcd4jqY3SwQqJQP1zmR-zce7P3719NImXm9PWtnX8nuN9eCIdEZG1S3_hOlsB0S39AoasWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r15
💻
@BetForward</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81848" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی.دی ونس:
در حکومت ایران افرادی هستند که می‌خواهند جنگ را پایان دهند و تندروهایی هم هستند که خواهان ادامه آن می‌باشند.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81847" target="_blank">📅 11:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Km8isgjCQrP3646DFoykh75VdHNVwqNlLx4rqicdiEv4kVDAMU-H-j6rY3jXk2cLT-CyK51zreXgNZ1jcDxK-fEwggkLnl7ftvZS1KyIFCZu9hRwIwxD1fJKRgpPxB1Y2sEuxdM1naf1M7qWa5SwLX-PrBtec8aipn_p9_6HQv5zCAvqf8e7FhG9iJ0esd--T-t1gzBdzZVmUUgVwsOHJ8gTl51kg4xDkcKMrJlcJHDUNnIE5llay8DYGLf5ROx6o81sWqgH0sdMpR8dGDiUioEFs5v0mwIV3Niljm0wvIUdXY7HqKdiJ6BUUGt4XpMVy8roHaD7da2D9wN6zI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81846" target="_blank">📅 11:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81844">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoS-pMpo9v5xdXmK5x0jzFL3VVCnBX4anwggxv4CVXYFRsgBxexEb9X2lP4v-EIvx8EXVIJLmvsgX7a9_J-d14HBJLLuCzoMz1ACRCS5H9wo3H994TQF6ZsYHTVEXI9btg7V1ZhqjXh3nO4bHA_mLOioTBcaiEHTot2orteaTalIBwxD68bCVIgyByAYC-JpXQW_FVkenU0Af_YW2TSodsf6QAuY-ku3NuUCDZC8lFxOGmbc7bCessDJh9bePZuEcMHoA8jKS6DvK1aDrcqN-rmTxEDAYGDoWh57mkhT4cCLPJciWAS7fr6TwH8RyqFTIK9BJPD7SbvyAqYemARzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81844" target="_blank">📅 08:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81843" target="_blank">📅 02:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حصین درحال فحاشی به فدایی و مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81842" target="_blank">📅 02:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO_j2IGMEhXWcT4kBpz07azMp-91oN1FSf97Pr2yS7pfjqicrjHWgZO6GbSZtqwT5pytIazT09gBeLffVFjbbuG4bjoePOIBRzjI1q-5VYa5Uh5tqklJLneIx_Krxu2rDjxPbV6YHDw9A5JevZjpvDEfPZ58hQiTyoYqTR8qvkcjrHqbJ1AQk8-mdi3_EWDAWfQHFfRqJOcmlE0vCYwY_BwlMrMMNOsSMWR1LyvkGKWH2IJvlllqv-SkFCTCMwpcHOxURs3eW4kpZn3b5vwQyZDH8k3PAu64bh0X8X2ap5fq7KtperhBkp6JlEr1rzOuuczlE1htyiz5OBuUvJVKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپدیت جدید اینستاگرام که میتونید ببینید کی انفالتون کرده، هم دیگه رو تو چه تاریخی فالو کردید و حتی چه پست هایی از هم رو لایک کردید و چه کامنتی برای هم گذاشتید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81841" target="_blank">📅 01:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbcDU57-6dvwl4IPamLr_1JMF5A08oN1iwwofAKBuO2nYvARcQZ1kPrpYwdI3tGpc0wm1C13RP6BcKIv-GPu32lq14uceMw4HmoXH8bcZeqLRUcDdlgTar-nbPZW7dDmpUT2jiiP9b4MkGAm2SULP3jGUp3OW81aff6rE8yRhS258SAgr5Ie0G2DbkYGOtHfThP0Nz-PGlczc05HkOo3GQdW-CfSMoOUzi0LYeFmYauacHw05RO5byUQH8smfvI-tEmMNAEykU5kWgykQ_0OirR_QltBWklJlwqKAvTogL-QGRRnTiMtSIOHw8MDOdmWhZkd9mQZZhRwBvwFlWmN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت یه کاربر زیر پست تلگرام:
من آدرس مخفیگاه پاول دروف رو می‌خوام.
ادمینِ اکانت رسمی تلگرام:
اونو که نمی‌دونم ولی من رو معمولا می‌تونی تو خونه مامانت پیدا کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81840" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سهام شله با کون خورد زمین
ارسنال 3 تا از بتیس خورده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81839" target="_blank">📅 23:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKU2yaOn8xdAzyr88tsypbWSf7W0Mlr7esBhuAv3tcmGTHnAe4sFoybZTGe234alo_MPjhwbv-8tk7Ng_n0T131BYqoiIsUcDBxP_M5TZOum-Su3tRhBl6Fi4C2DECliDEfVqhHtGjKbdM1wMGW3RxuoGW6Gaw4dUCBQcFaFe2l3RvKZK1F6QYQ_xXQ4hHQpJ0fEF4r9rhprvgq3Rry9uwDXTmZlx2X-AlPMed85EU8pNq1m7cO4UmX6bgpTnJW3bAcrcuue5d0K5EVwEJBMl_fSNRRsl1dLFiMrzut8dZyd4jBJxo5MKRUIDrW3OdeL-ACQ3EZR4lQpOA6djDNeAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81838" target="_blank">📅 22:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81837">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81837" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81836">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT2rjctHDikRqfTKhpNL5I64Yv4GHow0dgfHddYBtOZDkCv-litC3bGFABAr4rEbQgSZ-Qjra55IE9fMvincyTw3_iXcTKThJ8Pa5W2-oBgomOSsyJWXO3-J-1APt9kKfZMH8vdPVKUTkrUk0frZrJhbt3mnyrp2BPw_f47bUQ-PIRIsuWAEO1NEfrNppoNWghWeYUe6tmadEyIO6qdqUdX5QaX6197UlQQQ52KohIcM-fbvdYRfYoEDEjdJtPgGx5RUnsIJyNmVBM5NrCgE6OJlMvzhK6vaR8hKH6kmU-QIJ_oqicbAUjAfUhfYDRxnmpifm_oT0NJRs1eVkfsFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری و مهیار به نام "برای تو" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81836" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81835">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اخر نفهمیدیم ساواک خوبه یا بد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81835" target="_blank">📅 20:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbf5tVBVAqhzSV0p-2_KHNEEBk6tF9ja0H5Y4bEIhV4QivuOMyumQTmQfddOsNMPfIEiY8LeBWcZmnRfgdZFk18-vTtvQEs-zEFrGFcNFkntqB9v3tB1M-Z6IYA5d0g29eQUsdJKOtYuj9TRskDfdBbDFE_1ZqdRPhyBM4LgO8Xjn4cZES3krMD-einJf9IM_c7F_wU199Wx9cUvikgkSEPTwSW24DDRtTevaI96tlfj30a6Aa-9Nry1CiAk16XyT4o9RqFNj31oJ6ZLJSGLmq8vcOd_efz61BxGGaxoXrGHUiRpsQR0UE28B3yb2K6l7PwgMPrbYeYQ8R3_zLF2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس قشنگ معلومه چندسال منتظر این لحظه بود یه آتو از مهدیار و فدایی گیر بیاره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81834" target="_blank">📅 19:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پوری و مهیارم ترک میدن نیم ساعت دیگه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81833" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMFHq7wXgZRs-yrxeQgVG_80Oz6bjWTcC1dRrB7Yw4i1fpSyg4G2hQczniXk70S0gqsMFjcEE8qpdzph36N7vh1u2QOvfiXUnzXRzTm_9t2Oeoei7m0yZ_Js4EXPjxpmeMhWsbN6Uaoapr7DXiG9m_e1ygmd2lNfn5km6DdhmqhZVQL3SoIg9xE5w6UzvEDKskKMFahViBndbtowNRmo5BsS9MvYqpR5kOa9CtZEXG1RA0HDzAP38TUo6NK0oXDJetohPluZbHNdY7bHwC88kAREoyEzawuT4zCQgsyBQxpUpLd1SXryuQ5nTq1_SybCEuCmT9hsi9GteHxPAd0Cpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام "EDGEBAR" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81831" target="_blank">📅 19:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd1550d00.mp4?token=mOqg93h5ewNindKrKJcBOhL4tvLsT6FjSJarXQRc8Hnwc0GEiCuu18SOVLq-zF7pzlk7hKJriummX--RWKtJjHBNNj3AMUAHBuymkxFQeNSPL5Rvs-Rrm-FnIEdarz7UQshjxMFin2PgkyNt935L0brVynAB2-cLTjsX-Rq0mPXYt5qhVb4afq1pNPZ9MjbxmsX97Kk21X4Ze7_9dRvujECaycXXC3tFACzGukwK7INWPTaXV7XIB38eYW0WxiZH_5wlrZQtbcF27-f9_uACB_c4mZ2EJjZnK65ZZT-RjHPT6UZACI-Ld7NbyCx6SjclSnlEd1kWFTSv4I3HGrDrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd1550d00.mp4?token=mOqg93h5ewNindKrKJcBOhL4tvLsT6FjSJarXQRc8Hnwc0GEiCuu18SOVLq-zF7pzlk7hKJriummX--RWKtJjHBNNj3AMUAHBuymkxFQeNSPL5Rvs-Rrm-FnIEdarz7UQshjxMFin2PgkyNt935L0brVynAB2-cLTjsX-Rq0mPXYt5qhVb4afq1pNPZ9MjbxmsX97Kk21X4Ze7_9dRvujECaycXXC3tFACzGukwK7INWPTaXV7XIB38eYW0WxiZH_5wlrZQtbcF27-f9_uACB_c4mZ2EJjZnK65ZZT-RjHPT6UZACI-Ld7NbyCx6SjclSnlEd1kWFTSv4I3HGrDrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین فوت فتیش ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81830" target="_blank">📅 19:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81829" target="_blank">📅 18:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsLUhpa8tnkSEMDfXG7J0MBdDynXyGFsaro-vnxOpQJ2YMQnUNhWsTcMd0SBNG8d2fctXUt132KG60Ti7Sf-x-G67MZDrI2JL6p3aDTei6sh_vj7DjHiz4COH8puCJ_m6yl9QYONLd1DkwQ8LsyzzSZz-Gz9rqiraIuKp-0CK1xQ0pcul3fF1UfmJs2UudgskobqigqkOQdXDdRim_uWaxm_3vYw0Q-R4tPH6K5gGCMigp3VRqzFzlBRe3GZ_54W-5sT6C3FN5Z8bO8Irl8y_TXa_U0SWEu59kapMLfFCILJDSH47qYYKkumi23TzigDvJ9Ce4KAyoHKPtvsTAw65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام "میبخشم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81828" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کیر تو رویترز و رسانه‌های اصلاح طلب با تیترای زردشون، تاحالا فقط اعلامیه لغو تحریمای یه سری شرکت هواپیمایی متفرقه مرتبط با سپاه رو تو سایت وزارت خزانه‌داری آمریکا ثبت شده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81827" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9bTkEwAEZXaWqNBJz1CibW3OLO9cANQhtGwMvO7WYuOefxrcknmbPNgRTmVUhPMyjZvgYSnJEFKpz6LlUjc1VA01ed247noAGV_RsKnzwC7czAZDHeAtcg60bDHurj1dQsRQfvU7XJMnJNJEmQXxCEkPSnuUqPnXyXNeFImeiWn9vaIq7padUsMk3hpTvLHWH_jOhgebHbh4nXaZYbh03qvE6xpXWrsrOsOrlPAAQuKBmYoIa3zuM5y40k5dqAlZEMV9CdZn2nACcvHoN6WvYXSDHVG5flu_-rotltLBDjdz6N4EQyvsu_hWeOy6RQNAbWLS0hQFKB1LeedERNv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوریا پورسرخ چه کراشی شده
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81826" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81824">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رویترز هم تایید کرد، تو وبسایت رسمی وزارت خزانه‌داری آمریکا اعلام شده و قسمت تحریم‌های مربوط به ایران آپدیت شده و اعلام شده که لغو شدن، حالا اینکه همه تحریم‌ها یا یه بخشیشون مشخص نیست هنوز.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81824" target="_blank">📅 17:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81823">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آمریکا تسلیم شد. اسکای نیوز عربی:  وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81823" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آمریکا تسلیم شد.
اسکای نیوز عربی:
وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81822" target="_blank">📅 17:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسرائیل هم وقتی توافق ایران و آمریکا جدی میشه میره عصبانیتشو سر لبنان خالی میکنه و خارشو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81821" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81820">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حسن روحانی:
یه سری ادم مومن احمق کم تعداد که با اسلام زیاد اشنایی ندارن فکرمیکنن اگه این جنگ تشدید بشه امام زمان زودتر ظهور میکنه‌
یکی حسنو بگیره تا غرق نشده تو استخر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81820" target="_blank">📅 16:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هرچقدرم بگید طرف اسکی میره و فلان، درحال حاضر هر ترکی تو رپفارس میاد و اسم کاگان کنارشه مخاطب حداقل یبار پلی میکنه اون ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81819" target="_blank">📅 16:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81818">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هروقت اشکان کاگان ترکیو درست کرد که مثل رانندگی در مستی خفن بود بعد میتونه بیاد نظر بده</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81818" target="_blank">📅 16:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81817">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3Uy65jV5roVTDM2cp0KLmfnpPG5_OyajH0wFWRrn32cqVGCUr_jhuvnUAlqkt82kTca5Bf1a_KaBQBR9RKyH1Tr5s2BM5PLGknl9143gRPlMs76rBqIxR7T7-mgHp2xTGJqKJ8nPZdRIBZE0d75wpD_hzkAxmrF1V_2Rw-pBnu6wawgCq34j8EphDe2HPlE5pQNEbQw-VrqHvF8QsRUU8sSRrP80kC3ZH2wiYCjWWq13e4Z62tW1UxiwHisWDsAbWEvv8_UxMQdtyNVb4teGDISCndJdrS1vLl03f8DLENkIGrlNkQZonydtNkdtrvKGN2UQzYWc5e2fM9JtaUlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81817" target="_blank">📅 15:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=aHgb1sdTRywSgIb2DO8lzECpH_BhpLWhtyy5c4liv0L1kNz76Hdi6QP9n_Jq4mXrfkHm5iTVyEmF1CsHX8ut3kNxuQg-yAKZjrhdfsX7h2Km_kQAHpBtTr5Hf-Crn67j9pLsbsYtT_AFZ2k9MtrtW8ZGPucaYC5Kp9y9K4oWWeIvwEFHmBiZ4ybIJ-VgqGNFihHbMTQsww4Q04wH1p_Is4qEnlxHLN8BRplXJZUJU8NWMi8v6_4nXnP7w1OZVGDvsiwmGIwEd0aztUrWsImmBeYc6H4zyAty1dObTaauZLQtrV2mngyWTWPuTueHWniPcIPgkE6n1cVh-RK3Ed8Q2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07a77cdda.mp4?token=aHgb1sdTRywSgIb2DO8lzECpH_BhpLWhtyy5c4liv0L1kNz76Hdi6QP9n_Jq4mXrfkHm5iTVyEmF1CsHX8ut3kNxuQg-yAKZjrhdfsX7h2Km_kQAHpBtTr5Hf-Crn67j9pLsbsYtT_AFZ2k9MtrtW8ZGPucaYC5Kp9y9K4oWWeIvwEFHmBiZ4ybIJ-VgqGNFihHbMTQsww4Q04wH1p_Is4qEnlxHLN8BRplXJZUJU8NWMi8v6_4nXnP7w1OZVGDvsiwmGIwEd0aztUrWsImmBeYc6H4zyAty1dObTaauZLQtrV2mngyWTWPuTueHWniPcIPgkE6n1cVh-RK3Ed8Q2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قربون دهنت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81816" target="_blank">📅 15:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvOunaRcIU8Gspxwm7vR6p2BvjIP2EgULc0kEH568qs8QiRD_Hc28Hg2bT8UxyFJW2s5pXJpldtvfmGmblxHsnKl65LbGwnUohqb57mOoK7f6OSnvkqoaTseeCAYnPSLTUuJggMrNiNOJRQcHKnqBFCQms74sJozvshEWz709R7WhQNOfxDOo_MOhVHfIkoDIDIwAmIdiKpSTkYnjkohSYgVcm0e9oE4QijAVAi-DLvfhL8E0YUzgp_khmb6gSFuNCvdLoZmEZehJQuP-1bVZ23apbvPF9szJ0rw03i2oLEGdy1R4x2EnmdkTAcuWfeVTVcTeDswyJD9U6jvdZc1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربون دهنت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81815" target="_blank">📅 15:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دمت‌گرم کلی خاطرات خوب کودکی زنده شد برامون</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81814" target="_blank">📅 15:02 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
