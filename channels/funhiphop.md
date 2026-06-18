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
<img src="https://cdn4.telesco.pe/file/kBp2hlhP7nNusbHDRj09YtrK1v52AwtOaWJ2sh5w6V9w_OTxWRgFE-yI4f_zrqqY43ZoEsnTEoPReXrJhlPPOdZk7VDmflUtzfCsLPrmyNHDqpfPYag2qapdajrZN5lbMnE99lPN5Vw9DcOQEQg0CyGyIHBZ8pK4-heW7qB0u6v6xXB6TynoDnDgODIeMxmAVCX3Prb-vHmAsIjXJyiUi9Y96Qo7i2TJXYcBgGxZN5VXLrDio9m8-sSbC5ADmtR-sDUOpxrAsTBxA6ytXlyKTTg6qQgtFnY4N8o0uGT9UO1dYX8xRFZ8W6LV0T3bgOwA369cFzpESx8KjGpd7lFtVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=ty-GjrLDUXNX9jSUf0CTSQeoKPi4Th0OK5QzmdkeBZp4zUQTFURnv9cIU-m570flFtjYLy8nKmAT29QF1qnjrNhvda3Z6AFBIdHG5Ll2LsfJIlQt7jZCzQQik2sS7YcqPvJhkt-NxZPAHEzauY-JMSLj44XphxB0fBz6mTOGXH7VcaXQfoThHTsgV41pQtJdDq1QZ8EOCJbaKAAHD81aBqLKmJA_8cnSllkf1BWU6qQyT7nClosbowLa3piqBQamBTBGdNwY7TCiHkTUaAGOHeEXbulBH3g2JlgdEZiKd1-eV7K-PPwP1IRSSAUvhFx1Sehd_7PYSWjp0jOQ8xLOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=ty-GjrLDUXNX9jSUf0CTSQeoKPi4Th0OK5QzmdkeBZp4zUQTFURnv9cIU-m570flFtjYLy8nKmAT29QF1qnjrNhvda3Z6AFBIdHG5Ll2LsfJIlQt7jZCzQQik2sS7YcqPvJhkt-NxZPAHEzauY-JMSLj44XphxB0fBz6mTOGXH7VcaXQfoThHTsgV41pQtJdDq1QZ8EOCJbaKAAHD81aBqLKmJA_8cnSllkf1BWU6qQyT7nClosbowLa3piqBQamBTBGdNwY7TCiHkTUaAGOHeEXbulBH3g2JlgdEZiKd1-eV7K-PPwP1IRSSAUvhFx1Sehd_7PYSWjp0jOQ8xLOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
یک انسان خردمند در ژانویه ۲۰۲۰ گفت: «ایران هرگز در هیچ جنگی پیروز نشده، اما هرگز در هیچ مذاکره‌ای هم شکست نخورده است».
ترامپ:
این را چه کسی گفته است؟
خبرنگار:
دونالد ترامپ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/78163" target="_blank">📅 08:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBHZTV5udG-3DUwf9dtQVAeM5kv1vH_O_qgN0RRpNaII_ngy_c6djist7GKwrF5GEPUld0Qfat1Uf4dDGDFtG1-D7srP69QNYk70Y9ZZhp6rC08XAucVBZICKAxCmulPveDEJMTv04Ma1rkHYcttZNB-_euhOAGpYaH48QYoLmzlI78NLT1kDgL7BZLfEDdbhDAZwBZvqO9SFityfPU06HvMgQ53pd9Y7fF-eS4R-HJTdT6_Oilu3xW3iYKppXXTbDf0ychs4_i_-VgdSy0h5boW_Vdv8EQO-1MtqNPxN7gHIzTD5uX29zM-Cs7bE7cPND6bW3CODtxTeZGuMAGN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/78162" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asCWaoS9-zWSyh5jfCkzKgHkLeek0mCuKsshQsQhzdDeVa8H-C4kbvd59Rjuo9tmB217DYhzKCk9r_H8URl5gsZ52Tr05zRIGUmTLd4pYHsWgcvAron05USEZx0vLzW3fsL-8LHMHeVFYQe0XZtNOGHZhfnzSLWbahoPNX1-D9q7NVQlyRsQJ1wFin00NI5APpOiq1klks6C8WREraqjLjKzMzsQGXfO-pxeBrp3pD0rUJJ_i4WZ7V09qp3NUcJh75Puy7d6Q7-i8XA0BtbLCWdZ9sdyhZ60MVXzGpeYilRKFh7RleuO-HhFULW9Q-MEJx1rG2zO99TV7bkRNECwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFhErLMd9h3YXOdjyssmKXYb1GLqeDgeXbytuzJux5rZyYx5pfM2gax8NEyR8iWOgzT3ErMGIYlKlELAX54e5xaKmngUdTBu8_dYaJqXW6WLXsusAD-dQjn47Ej_Cx2Vwz1Grm6qC_qXCGbcMrQCFu1wmzhZajLED2Ohfn12KrziDkNGTtDQoG560_2VzZvpEmzi8h3mmcKh1ag3MNZv2LVJqDx3Kz7I5f3bWO4-3ASRUQRyWvmLF11xLFyNcXEyPQzgxGb_G_yM1MSmlnZiDmFWYMRqUmyARo9A460lHxuuDTqC9i0cie3icXCCCVjglPHPN6aPH1Hp1W1IyVUl3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/78160" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جی‌دی ونس دو سه روز پیش اومد گفت تمام بندهایی که از توافق تو رسانه‌های مختلف پخش میشه پروپاگاندای سپاه پاسدارانه.
امشب خودش از رو تک تک همون بندها خوند و تاییدشون کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/78159" target="_blank">📅 02:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ایران دو قدرت هسته‌ای را که توسط برخی کشورهای دیگر نیز حمایت می‌شدند را شکست داد.
ما شعار نمی‌دهیم؛ ما واقعاً یک ابرقدرت هستیم.
روند تعلیق تحریم‌های نفتی از امشب آغاز می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/78158" target="_blank">📅 02:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کاخ سفید جدی جدی حسینیه شد؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78156" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رشفورد چهارمی رو زد و تمام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78154" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب طبق بررسی های میدانی و حضوری تیم من در ژنو، تفاهم نامه به صورت دیجیتالی توسط پزشکیان و ترامپ امضا شده؛ ارزش قرارداد سیصد میلیارد دلار با بند فسخی که بعد شصت روز فعال میشه.
Here We Go.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78153" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">میگن که تفاهم نامه رو امضا کردن ولی فعلا بچسبید به بازی انگلیس کرواسی این مهم تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78152" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عجب سیو پشم ریزونی کرد گلر کرواسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78150" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بلینگهام گل سوم رو زد برای انگلیس
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78149" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc2oQDv6Hmhc05dC0W1DgUYFIYqaSD6umYcY5V9ivGDJoVeDtizXmrNIqURyDBKVPYgsIpKqQ1UXcDkQ3v4gCCTTl2vdujOYq0j8gSwMH7rAZqZbeJnRoRs0wRE4spZGjsPeCVVwmj5vmlPpNPoC4_fSCwE-j_gYx6rjNI5KAIABLFLNSSCrTwSLzrvNy8GBw6BiJ0gFfb6xtn7uLJCUCzQM8eT41BGIeKSdzUxOwWKTKk5KwGxbu0XYUSuAUIwUeL_1CdylSYH-w_j-Eo9tDPf68JcURtYPYCPYhxAa0hOrxRvadIhQOoqB_w15mGe3yQ4Y5h4s7ULLPKR9OMdgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از یک هفته تا منتشر شدن فصل سوم سریال خاندان اژدها مونده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78148" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxGyPkAkw4sP2RadGzBHQyq_4j8fdzqNFPKCwtmUbSh_OxEDcSb7wWi63vI5PEhPvCz1e3RO_c4kzVrae7kaot4CjYVP15EKyOWb9wWxewnVZ79Zl3zoIAbSo8wOI7srwk-SSG1Mgafs9G2R1Plr0oyBToXkPhCKg125GTGTuvy_m8cTExo3oIjxcatLuSpcrZlNfVg16WipFSib2LCQZmFVeVN1nQnkdHaaO9TXL1EPsQ3E5UQ-p5TPbUtPtnoCo-9Jcub7fJt9DPZjzgtGwiQxabQcPlcVvyxhotXDP8i6bKzPXurGHA_Kq4-1twEzZmONs_sLICocvnpweLlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مامان پوری از مهدی طارمی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/78146" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کرواسی زد
۲ ۲ شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/78145" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مثکه متن تفاهم نامه منتشر شده ترامپ قمبل سیاسی کرده برا جمهوری اسلامی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/78144" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این بازی داره قشنگ افتضاح بازی قبل رو میشوره میبره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/78142" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=cHAHqsTbg-YnpUjF60UTXDyD4mmFmPMmVy4-D02YtcHOkIo17Jix1O9kMkaUaUN5U-M2kFgba8BmN5zJK-VhO9t--YG35TCDL455H6XwTd1JBOlEnuUoLDiAvvqyiqOcByzIfpAmenPtftSfRUV7GAFVk1BUPeNBb5O97pi6T7KZ88x3hedQEz18r7vCyljhXmzQzjlVuTVHNGZ6047E81BzmBX31nnd4ioVeBC1Ik_QhFpcw9zmQR2IHST56h3LZ2TEhA9MJ7ERThuWdO-TdOn-Uk-R058tp6qYUR3QnxskE9fNZgTVifRcy3V74t6MlI31x-sU2khk0hG49EeFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=cHAHqsTbg-YnpUjF60UTXDyD4mmFmPMmVy4-D02YtcHOkIo17Jix1O9kMkaUaUN5U-M2kFgba8BmN5zJK-VhO9t--YG35TCDL455H6XwTd1JBOlEnuUoLDiAvvqyiqOcByzIfpAmenPtftSfRUV7GAFVk1BUPeNBb5O97pi6T7KZ88x3hedQEz18r7vCyljhXmzQzjlVuTVHNGZ6047E81BzmBX31nnd4ioVeBC1Ik_QhFpcw9zmQR2IHST56h3LZ2TEhA9MJ7ERThuWdO-TdOn-Uk-R058tp6qYUR3QnxskE9fNZgTVifRcy3V74t6MlI31x-sU2khk0hG49EeFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خخخ:
وقتی همه‌ی کشورهای همسایه ایران غنی‌سازی دارند، منطقی نیست که به ایران بگوییم به طور کامل غنی‌سازی خود را برچیند به گونه‌ای که برای تولید برق اتمی هم غنی سازی نداشته باشد؛
درمورد موشک‌ها هم همین است، وقتی همه‌ی کشورهای خاورمیانه موشک دارند، خب عقلانی نیست فقط به سپاه پاسداران بگوییم موشک نداشته باشد.
بیایید کمی عاقلانه‌تر با آتها مذاکره کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78141" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شما یادتون نیست ولی دالیچ یزمان کنار شفر گزینه سرمربی استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/78140" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کرواسی لاشی همیشه جام جهانی غول میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/78139" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انگلیس چه خوشگل بازی میکنه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/78137" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: ما حتی ۱۰ سنت هم در ایران سرمایه‌گذاری نمی‌کنیم /از یادداشت تفاهم، بد برداشت شده است
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/78135" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7FBa0YiomJYnVZyTEKYhIZ2JCcW0OcuDi3RULWy74fKu3TJPq0CoFnTQNtNmH6xSElxqUXgYUn_yxovGVxoXcKUG38N-j-i41p1J0KeCYVyu6vo7cKNSCFvGOfY9B87ttEBB42YFldBEoImgsHpMKLxD6THbT7pBLP94dik8RFmKTKYyHB6JyplsiMSR6sHWcjqkHxUBKlHI7dm1_Nh2Sm7YUwCpZiFexCk7XuaX2DNv5q0Jc-4wIBh35Q5uqu2wwe8LpJ63ONDq_r71A8cD5_tm6kWbcF-4t4uISz2LD20niz0GKCqYX98hb9-ZykBFGwIdMTxEAGvBXIMcdbBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوادو
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78134" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار  +
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا  +
🛜
تمامی سرویس‌ها آیپی ثابت هستند.  +
🎛️
پنل کاربری اختصاصی و حرفه‌ای…</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/78133" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
📦
20 گیگ --->
❗
فقط ۴۹ تومن
📦
30 گیگ --->
❗
فقط ۷۲ تومن
📦
50 گیگ --->
❗
فقط ۹۹ تومن
💎
100 گیگ --->
❗
فقط ۱۶۹ تومن
💎
150 گیگ --->
❗
فقط ۲۳۹ تومن
💎
200 گیگ  --->
❗
فقط ۲۹۹ تومن
💢
تمامی سرویس ها
۳۰ روزه
و
بدون محدودیت کاربر
هستند.
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/78132" target="_blank">📅 22:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78131">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه صحنه گلر پرتغال هم اومد پاس به عقب بده به خودش اومد دید خودش آخرین نفره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/78131" target="_blank">📅 22:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تخمی ترین بازی جام با اختلاف
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78130" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همون بهتر ک توپ نرسه به رونالدو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78129" target="_blank">📅 22:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فقط یه رونالدو فن میتونه بگه ترکیب منتخب بهترین هافبکای جهان نمیتونن تغذیه اش کنن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78128" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78124">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بعد دیشب گفتم شانس ایتالیا از پرتغال بیشتره یسریا به کونشون برخورده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78124" target="_blank">📅 21:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تقصیر رونالدو نیست
گذاشتنش نوک بعد یه پاس نمیتونن بهش بدن</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78123" target="_blank">📅 21:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رونالدو مادرتو گاییدم پول منو کی میده</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78122" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نوس با قد اندازه کاگان چطوری با سر گل میزنه هی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78118" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hxh9wQdzZ1qROUAzkOQcbxFgnnNMN3Jx20kh3REqX1z26FQgDdTDfPIEvaV9-x_NG2_VgyNNoTXLOXBLnZtDfhqY9g23X5-MQmCccrVxas02JRB90wPgYAz_7CH-Mev9f147SaD64oktRTbTHQm7T_BfFERkPRQZFKV3rRzUicrgHuwamBndEILivmAXgAZtZ6ifW8qNgk8DG2fZ6Of29TPLHPHK52E6D76e7x5ZuvcuYAlaLqGLrrQPJHQnyFxn5ezbX4JeQBSC-Sn7pnr2irFbzziyQ1KPyOmn10WC8czjzt56020jZT5eQG3JlcYPwjuDxabtIFOkKhDP5QDBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا عارف
تولدت مبارک مرد بزرگ
❤️
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78117" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایت الله جی دی ونس میگه چهارشنبه متن تفاهم نامه منتشر میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78116" target="_blank">📅 19:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نه داداش پوری خایمال نیست اینطوری میکنه فدایی باهاش بیف کنه و کیرخر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78115" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مسئولین جمهوری اسلامی حاضرن هر کاری بکنن ولی نرن حضوری قرارداد رو امضا کنن چون اینطوری مجبور میشن با قاتلین آقاشون دست بدن و روبوسی کنن
فک کنید همچین عکسی پخش شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78114" target="_blank">📅 19:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78113">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=i7hjv01yMOnVSSqLAsMMyH6g8rEkHv-c7FJJIpcis9ulY5RtP9InCPV-buoYjpS52RRE4nGmCGabbPdewnmL33QSHRXDmD_LO0tZfyQHyTUUbesoZsW1Lf51uMAMlFbUs9GffNwU7PnJZoWoHDdkmkGm1Vh-g6gpPWrE-GJK1KxM5dxT1QuBRFiQFz61AeKD9ljTcn6jlSzsxrZF_nYYhEtCSldkuy1uZD7sU8XeT0xUXec9sqkGz7PqjeGnZz3k6Hs9wu7QNTUJ0o_1yWojjM2RVxEYYmGNAB0cAY7ldgzf6OWlF5ivJ27ey0Kh9exNHqUBplVFuNm0jjJua4Lziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=i7hjv01yMOnVSSqLAsMMyH6g8rEkHv-c7FJJIpcis9ulY5RtP9InCPV-buoYjpS52RRE4nGmCGabbPdewnmL33QSHRXDmD_LO0tZfyQHyTUUbesoZsW1Lf51uMAMlFbUs9GffNwU7PnJZoWoHDdkmkGm1Vh-g6gpPWrE-GJK1KxM5dxT1QuBRFiQFz61AeKD9ljTcn6jlSzsxrZF_nYYhEtCSldkuy1uZD7sU8XeT0xUXec9sqkGz7PqjeGnZz3k6Hs9wu7QNTUJ0o_1yWojjM2RVxEYYmGNAB0cAY7ldgzf6OWlF5ivJ27ey0Kh9exNHqUBplVFuNm0jjJua4Lziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78113" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78112" target="_blank">📅 18:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6FXnXhFjYugzVNfbbZ0_zBnbkKpscUwOhytealOizezG43kpRG_Wh3jEVXIq2DuxdWfmVlxp8ZKUsX9jfWdHwyU1mNTlWxZllLvSPSiLW54Ki9dDwD-ErzGmfHf-Ifv0ySgn_cQPS9JjozcSKjbao8nPOdLpG17sh0VKZzn9oGk0POhJkuoCLweSGxOem1oSSZvDEJA9Qjoqpmtb8Ly01y-qJpochw2S84JdLoIUKJhYusmpdJKdtCRV19vPUIbrV_J8sWuFTs9XAegh7RTkHTLFPgWAeyR6QodJarkzcE_mD96nVKkR7yZFH9mThAbm-70j8aU18RcDhQ_sfSQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9tk1V1cYY_l3WkTGk-ZZ0Fn8OJxdgfUW-vT5S3O-OvPfe1Y8pcpkfsr4EEHBP_yF1UhrN8Zo7JkIWdKL3F1Gu_bmZPXkPrUGTROOWAkS_8m4ajZwM50pw2iopa0UZs6CrYX7zIdODrmQfnaTSgcV3LuqAVeXWZorxiaR_e8SVRmaw6iMrwLM6Mb3pZMHMjKgM1NWxpCr_mW1mkEYhDvP6I_AM04TmxnNrP0qv9AzYsGQCg6TihqoPjGuaQUQm87SR1KtZFxSQyWLFqiFcQSigyTWswOovvkK6UQSlmsTiqavXoUEMU96R3gIGmngX6X3K_Lu-kNjZoHf7vnqmcjcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78110" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/78109" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB-4aeZyX8MV5_43F41SuCDSzEmGEgtD24WeiDVpW6vAxP5zx8OENpgTE7n9BXsi-8bdtsk0sNjpzbQpNMeGwfIFehSCaYJXv1KOwfKSY1FcX9IFpBJm91PUMzNnLzfztiFFDO7rmnF6idMzwdOMnKSmu65zkrmuq79JMxMvTAzzNAnqDTPVVEjEWdS-nI2EFNE6kuJZyl8Ugu1_qs36kJntiNvZxOHM0vcndHBjyCltPI2rBr4bq6SIVKyvb6ZtcJhoJHQJxFcAzEtw14NRd7moLc_P9lHkGzYtX_e6gtL3DblkTghzbR8vOQV2JyPUUKCo7fMWvucqKScJiKv4pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g27
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78108" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/78105" target="_blank">📅 18:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78104">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDCNeAFpUimdEKrLCX5QWe7USlNnMpF1yOlwBzObD_qVtC7E9inTwGCaZ9Y09xBSIF7OwFHamUQ_yM6nWWeg-fNveBB7DTptsPI5iMVlCJCEvq4V-AHr4ioWmZI7POqwNBOfqt--lbDUpxH2te_H49NGSu3StyJ5XDIhlgqY2Odp-Qyu59XLYkCkP4b36U6V5zLCSsGvxxzWSDBH-gVN1NUCXSsRW6K7qsPUg9B936F1zH7LQu7VihMC0XU5TF6PqUL3Iaejrqlnft1oZW7EEPo5jPzly3xUKwBLmiPJeWCBn-gbwfxfiBHF5aQyfCAbc3ciy7-HKf1U_CyJ-wK8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78104" target="_blank">📅 18:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=UE0nhpLyhbG1dlLRS1cbeCFB-aaCcRAVVc_XqyiZuUCCUoxt-fig-bJIGtAokqXeLJ9ipqU19vhpKp1n_l4Znxh_U3bHwiyxd_YeCGYwCrFeqwRGMPkoAUYRt1EaJdxNJB6TS9yAZyPJHbHfLacdeB85YwMPJiG2zgaMXz1SjJH0xb-hK7xk7vzoM5Huob8XEYwAN2s92JR16LAfkZeeivIW2517NRq7M9QdTQVUfZGVAnf9d4tm-iSFjt0GSoHofsC5wGsKcIpx6Vd5GAb2WS-YiHgSq7lYko3HRp_7e2BHEhwo1ndvLM9LAvmBso9qqAAPxe4FSkCf0LniOagT9IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=UE0nhpLyhbG1dlLRS1cbeCFB-aaCcRAVVc_XqyiZuUCCUoxt-fig-bJIGtAokqXeLJ9ipqU19vhpKp1n_l4Znxh_U3bHwiyxd_YeCGYwCrFeqwRGMPkoAUYRt1EaJdxNJB6TS9yAZyPJHbHfLacdeB85YwMPJiG2zgaMXz1SjJH0xb-hK7xk7vzoM5Huob8XEYwAN2s92JR16LAfkZeeivIW2517NRq7M9QdTQVUfZGVAnf9d4tm-iSFjt0GSoHofsC5wGsKcIpx6Vd5GAb2WS-YiHgSq7lYko3HRp_7e2BHEhwo1ndvLM9LAvmBso9qqAAPxe4FSkCf0LniOagT9IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسخوش
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78103" target="_blank">📅 16:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مثل برج میلاد بعد ترور سران نظام هنوز سرپام
😂</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78102" target="_blank">📅 16:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ابوطالبو بخاطر این که گفته بود تیم ملیو دوس نداره چوب تو آستینش کردن و مجبور شد بیاد معذرت خواهی بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78101" target="_blank">📅 15:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترام: توافق قطعی نشده اگه هم قطعی نشه دوباره بمباران میکنیم ایرانو
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78100" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: بخشی از تنگه هرمز باز شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78099" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: گزارش صندوق سیصد میلیارد دلاری کذبه و آمریکا چنین کاری نمیکنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78098" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: ایرانی ها به ریش اوباما خندیدن گفتن اون یه حرومزاده احمقه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78097" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اندروتیت ۱۰۷ بار تو یه صرافی لیکویید شده.
الان دوباره رفته صرافی و شارژ کرده رو بیتکوین لانگ گرفته.
اگه لیکویید بشه و پول از دست بده، میشه ۱۰۸ امین باری که اثبات میکنه تریدر خوبیه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78096" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/827713cec2.mp4?token=XqiuxEHN0Sdtf5kZuizvcXZc679Vl1H_MxnKd4uRzQIVEab8o8DG0evDX753bxQ-QWNTEtsYumjsHeb0WCoGGXTIdZ8BwS4Jnhgdy2zSc-cfFhJDIQpRMz4WSpy4CCF8ltMAQxQ-MyW7Ng_qSsKc1sSgZ86RTyk-4nXdZDIEKrkDdbPjloriA9jbALNo7Ggit6PhCPr7-t6cw3cfX8Tsux66jqEs8aCn_YDX07fvvt1Wlx0DjewyEGak_Orl8dxAPmxQZqXSP19Uuivtm9KckZXPWF7J9y88_oFvMpuNEb4iqSMl5EOdgo3jFlcN4--tOVHLU3HRKlnNDDdQIE4VmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/827713cec2.mp4?token=XqiuxEHN0Sdtf5kZuizvcXZc679Vl1H_MxnKd4uRzQIVEab8o8DG0evDX753bxQ-QWNTEtsYumjsHeb0WCoGGXTIdZ8BwS4Jnhgdy2zSc-cfFhJDIQpRMz4WSpy4CCF8ltMAQxQ-MyW7Ng_qSsKc1sSgZ86RTyk-4nXdZDIEKrkDdbPjloriA9jbALNo7Ggit6PhCPr7-t6cw3cfX8Tsux66jqEs8aCn_YDX07fvvt1Wlx0DjewyEGak_Orl8dxAPmxQZqXSP19Uuivtm9KckZXPWF7J9y88_oFvMpuNEb4iqSMl5EOdgo3jFlcN4--tOVHLU3HRKlnNDDdQIE4VmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاااارهههه تو موهات بلنده زیباس
کلی شیک و پیرییییی تو شب کلنگی نیم‌ساز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78095" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfgLOxQFywue0AZmsNycAOUXNwrIlZAzSe3OcvXIf7_pwl1eEelXJq8KmVVwEd7BGlX6FXCAUGdPg_ULvwkrbiEqkXZE9OfsUUjLGpYhJLMl4LDlBphVNS8EbwIv3KYHnNCzqwB3EhJKgSXpyLoAtfT5-bMzwoVkNfKpliGp4LscKTtARWLUA5CtPs-DD648DQnbHDEG85X1BuL_XTKB046TR6stnz73P3gjjBz3snKvakD_WyqLr4TtW8cm9uCW-RJoUrzUmTlXTz3nT440e1_SjJuvnHe9c35MxD7lSFwR_1yo9ItNsuEHGI-7WhYg61LZ_5nbKeh9yNPhrEfXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3WBIInFxVeEEL2UA07DoSnLO2sKIB9BPdP76TnftSG7WOJ_7Qb5zMlFKjfrj8Xlxl1bptSxSRGxhocYa0tab4CAC571OLa3f9HmG5VyDaoNawf1o1i4bZuMOESzYmtAnbIE9lNuJnDi2OSCJD3CFWaQ-16m_uiQ-bKlak9sU4smw8YIVqp8g5GaVNuFwRbccl4htb6zwr7oKtwxWVdfPEK1KtU3sjx2bikaGjUacODItgy1DXVuRp2hqCJDNBPkDXlBazeszPn4nPRKZqDxuZRR0yDu9yijard3L4M86d3XRiEreuTWs2Ih7oUN933gSNFv_2iWkDlvO2MB8tfrOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این داداشمون هم به دخترایی که فالوش میکنن بک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78093" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkH2OqKUFMtsfk9HaoBJ82PfXmXcPoljeWS1G3UnaL2Yr4nHoA1y6NtXXuXH6EFFukm9TVVrRM9z3Z4WoltiNA1Ls7aT1Z2-cyo9W-fNF3WbB5XAgBHkEi2IEc0HdGBgDRLsi5JIOO-jBmzf--LIQFE0-epxvZEcXBmD6mudceVB_P_OAe1PwLMl3-uDK1vmoPQQUPME4YTSHY69CHeDQFrRHBoZhdOmOrqJFU156B_Ea_C8IaJiKt6cIkzH9kWmtkwFh9BmF9XeoijWFCGliPKrLg_WQOIG0aiwbxiFnF2QXa2gMPyGljgqGJLX87dY93FMjus244u05CDeZePnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی چند روزه زنشو نکرده اعصابش تخمیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78092" target="_blank">📅 11:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9JucH_XuqZVt4aJPIoseVzTD_xGyBPw3LT7-XhNcvvFKEv4dYN6SP72_Wh2MGCImfmhV9BseAHtlZWz80ThkCQYpN_zNO9Mh5mXpxqRrx7-ETTGt3wQ5fIwK13jlDiAofvWMplO9QOzBo756XKxaZWrEM_z7h8iNbNj-jc8_v_ZiGczSTiQ6lKXnOHwPI0zhLkY9SZMkI1uMoLP90KWG30ZC__vT7Hl9eJkx1LMJ248aNWDSKfAyYtZtBeWtKaZwDnHd_DXlMZ6BDW-ORclxVNHMqCJX6jotRkJNH2AHd-tYW9eXmUewhiIWkXGKijZ3KZeD6KGUjABTzo4pXrnyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت نگران مصدومیت نیمارن
واکنش خود نیمار:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78091" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78090">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78090" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC35lJKy-vuwGBUsa866sf_5YzrazZZW4NpKshLG5CMwzm3IJbFp4UxYXmOW7qsi3t-UwRyE94zTqBKHAYJCDFKEqFqrijoNhA3kfTl0rUKoXRcQ9myo0eLKxg-lZuawxAImDTHWpaBNv3RB471G-mYR60g9fWREE_W0dRGIUyOkKNF9n1zowBvEkoffi_bHkNpQmB5V3FzvtupOMl6bQ8Qkt1HqsSB71B87UXsiPBAPLAUwbma90y7-TRPuP86VJjJU1b9kTozetVRR3Y8CDcrPawe7fGI2CAAAVXIuOKcMbYF6Vbch5ZONlyN339z2i2gYqJXQBEkBYN2CnnZS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r27
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78089" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CckckQ7j0cDZM6qq4Ra0nb7DK4QBCLcywhc4JwhU5i2mQH82HyNLLtRZ1RocHkwDdTfbvKt1Sc45EhmK0EUIrOHtUb1cRgsS-YFv--0qBXzshUdpg54wdbJvPn-NCHf9N_mOVvD4-GWhexUf7ZP-Rtm-lwEr9EJMi9c0SZPFgGA618HH8ZmeZtA0AqKtTwUWu5F6yNQlTuZ_ZffDkNRTMguJwc8mdlaEDCiko-4auDNFDYmzFjgcwg_n5PcrTfkme8krV3ue3NGrdMpjM8YIeEoCSZ7Fc9omUi6azO7RFMAxetNVrAiyNcobliZhQR_FJEtcbHbvExRgi9Vlav_lIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت پدر از پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78088" target="_blank">📅 10:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC_MFWo5T5ONhwZcTAXtHb8q2E968pzCC1TRy9YcQerKd_k7h7-AkO8gXvATrWuf-spVwYvB7COirx-4Ow6nzQSrweI81Xq1kTfzsm2uOvT1dg53in9XydjL4J97_JGaiR4b2e6k49PW0rPVps6S6E3r3_IvmA8Aq1QeJMUxQO2A6OR8TNkQtnAeS_9HT2s-9C7BBq3Igb7tefpCG7s7GrwYfU2kmhPqjNYLxQ0OdeUrsHhB17mxXwv_8c-gmWiX1nOvqloaYCoMZsB8WBlh5DKPUYVbYIZnwFLD5-KrebFym4UNfAwmaeLszGF3St90cq90C2GCTVkIGmyOmx_3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو دریاب پسر، یاخدا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78087" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حالا رونالدو مصاحبه میکنه میگه نه ببین گروه ما از آرژانتین سخت تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78086" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پادشاه فوتبال تعویض شد تا استراحت کنه و برای گاییدن بقیه تیم ها آماده شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78085" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نویسنده کتاب فوتبال هتریک میکنه
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78084" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گللللل
لیونل مسی
کارگردان فوتبال جهاااان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78083" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بهتره برم اول وضو بگیرم بعد در مورد خدا و اسطوره بی بدیل فوتبال حرف بزنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78082" target="_blank">📅 05:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بهترین بازیکن تاریخ چییییی زد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78080" target="_blank">📅 04:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78079" target="_blank">📅 02:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خوار عراق رو من گاییدم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78078" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هومان بدبخت یسال موزیک نداد مجوز بگیره، تهشم بهش مجوز ندادن دوباره شروع کرد به موزیک زیر زمینی دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78077" target="_blank">📅 01:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfDEBQ3piK6wrsOUlIDdnEmcJ4OmTp4ewtbJeD3uykdRyfVparY5OHbW3UYHaTFVbx6InAsdyHozTWZhLr95t3ebQ2fAb_BvdRxLoMDBxIeoPudSTHEEnFwJdhjpmqXVsctgftqgmNREOrLNMpx7C189Tw81y9C_bHXohM9AjzXSFsojnrbnnlKgBHWprsESy0be6TuuC98tWQv_lNHe1Ud9xFsgE4V9k8nWCVkdrjpP3BIyArXgmDP64AlMyax03GT1YSqTqI0UrbX8zy-EKV7ZyRIf6HYhi_ktX7PbNKBioCyxobtyT5w9boG5Y40xtaYEC0RWrfb_jN7SaUvvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا از مزرعه‌ای که توش کار میکردین خجالت بکشید، یعنی چی صفر کارت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78074" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78072">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قبول دارید کسایی که جلو اسمشون پرچم گذاشتن زوال عقل دارن؟</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78072" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnpYs-6ikeuE5QGACuGxsKrdb-aPiz1ZDt9K8DvziXUF5KANF2z2IfhzrBK40QbJDL0batPhMMM68g4TtCDLVilUWIoSVdpT2JVRkflJ4RbJDwadwrDmtYBxn50diszm2HoLhHbdfjUcPktBauJuh9wQQeMCTWXwHJhSMZl8t7lX0RhlaN_Yfjw8P73OOqOeJFW5EouGlUh6ddftBvln_u_dntqUYmsurGx90pPaRs1NDd1h-C4pgJZY1oCHFOgGjFK-VMbahrIoDIQRaDGVibn6PWVHkLFUzAvrDz1nuqMQwviKIL7YbweL0uI0OfCxpb8yHWdPHSniYfPPtf_qbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78071" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78070">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78070" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78069" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78068" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گل دوم هم زد فرانسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78067" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این جام جهانی احتمال زیاد امباپه رکورد کلوزه رو میزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78066" target="_blank">📅 00:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چه‌ گلی زد سنگال که رد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78065" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امباپه زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78064" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کیت فرانسه چه خفنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78053" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پسر اسکوادو نگا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78052" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRP-HC16Rkjh0si30vqf8nyEuhHpExESoukrxVCfAUQsv5HH-U-axfRosklvTC92uvMREMBOdYzc2Wa6ER5NCGIcMEmQPnCAio6ze5wVluVZDhXZLE-9UBGpAHBqch5fpNehhe5QB6AzyN95pM9r7aNe0jzKvhE9STzfQMcr3sZ-ocUmOV3ijPjA_Tq75avSNRBVHUuQFvl1_lSd2f4DaYgvk45eVKSFhL_lY3nrM6RDH5HWA020W-nrpCll9zFK5cqTHtM1ugi0bLcD7RSro7CqETyJxQGf7k3llB0v8yCldDGncNLhXQe7grzndpbugCveFuQKvlRvF5yNdCqnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اسکوادو نگا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78051" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نامزد های انتخاباتی در اسرائیل تبلیغات خودشون رو شروع کردن
و جالبه که همشون از طرح هاشون برای دشمنی با جمهوری اسلامی به عنوان اصلی ترین تبلیغ استفاده میکنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78050" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78049" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr0_hRrYErzJoMbi1JelOREYqedeO9SCuewrBIwWE21AiUlNC8-JGby2D7vSco9GwrttZQvPU-CHOLA08x9LNpmJMMRVS83YzyH0ZvcLWhZ4uaTY_12rg2_t6ZtDakfh-jjVPpaRi7pUU3al8F3gRI2F2m2ONkPl6FKe8yGgMnwVsx2dKciM1coK_vezSFGvGTMBm1XUdaQ04Hc1vkqqOm1zrVSxk2ihvXhww6fxxeLgG3bk9L8zVxk2saYXPvXjwf1w8i40HTcJkihVuyZeR9KMcnNo38ZV3pw_FrMc4YksHvbQ-HPYKTb2oGCsJ-d5n1X7SNeKhz6fC8LOBX1vxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78048" target="_blank">📅 20:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وال استریت ژورنال:
یادداشت تفاهم آمریکا و ایران به ایران اجازه می‌دهد فوراً فروش نفت را از سر بگیرد و ممکن است تحریم‌های بانکی و بلوکه شدن پول‌ها و محدودیت‌های حمل‌ونقل را برای تسهیل معاملات مرتبط لغو کند.
طبق گزارش، این توافق تسهیلات تحریمی گسترده‌تری نسبت به آنچه قبلاً اعلام شده بود فراهم می‌کند، که احتمالاً صادرات نفت ایران را گسترش داده و امکان بازگرداندن درآمدهای نفتی که در حال حاضر توسط تحریم‌های ثانویه آمریکا محدود شده‌اند را فراهم می‌آورد. (لبیک یا اوباما)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78047" target="_blank">📅 20:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78046" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrRgjxpA7ARtxALTYJg5pdVEberhnh1JN7mKbVSXzgR6xDhzGQuz1t6LAWhVRT7NXwtdqIuNp8BTuWo1osIjVZshWudmC9dS1pulpCahRHovgKDxu4kTsQXsiQXHIrZwR-JdvL3txybJglaOes176_oPLIfSSbk1hcmyaBXpNClDa8qJMm5LUYr8cQS0hP_bwqrjxnCfJddMPAwV3KNx4a4klSTqqR-x7E5p9vz959JAuEWwgTC8jqoJVloGOlNVUMbCoFxn0jqapza9kHGxOifGBG9-kYTIZnmRSGC27wp1O51PDcqfVO5qwvHKHKxy4du9Rev8lmWkT7hMwq-pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله شهربانو ازت میخواد همین الان یک لیوان آب بخوری
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78045" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqkDZXPJew0Jx0xjfjmiTI1JTwmmnzG0g0HQP7pQIIhExeM-QVUm8DNKdupw-7gJqJ-Iw_i7BwzfT-TfX7Tan64NjmPG3sDgfYGU8uHDZDpgAsUYyYhrqk8moN1woMcBvU2FV6a6McmvUzz1XQcSkMDp9TK1E_ynsM9oKJzbPo1zN1UxRMkxCNTmDe0Z4U94VbkT4Zee_DoAC4dO9zQQqxBNum7dcyQMozbfS15Y9omV75XwTc5Wo_6kdANRJSMALUtkxfOP35ixgTvSLZO_hbOB7PNw35WweR3pIC7sbqTAygWTvnMkHrXD9isjGkLQ9h556BbWCz4zE9SQWJ8aDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو خدا به دالگت رحم کنه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78044" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D40NcBmMo-mq3hAO7IJAYxWRp2un796nDuHdxq1_qjhxHyp6OsqRd1FAodpRtnrsdOPDwfsuL00aotweADWdvQnHk1CZJXzB9iLLK_O5s68xzas7JTeimjU9XrPQ613EMkOC78NnMPiRahRjJqiQGD5H6GqXEJ8XcMSzsi3d_hyo1XvEnfqa8fZpGDnSNPg_9bz5it5ljXHIBUS1GLRTLgh1BVG2k9wkSdYGUuL6qNcufM96CK5nFlF0xbEqzqBYFHzw3KFr5A9lPReQ9RDQ4ROb9DYFBxeob-n_d1FDabECY4kRDiKqzuHuwpytXB6s7D81y8lmSAniHC_1ls2mGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78043" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSHd_n5SvOTlrxshPfjqQLh-vsED2K2Glvr32QwdsgWQWVWgfo-Rlgx9-bDPfecvmljd9_Mac5pd_83Yc3zj9o1ngP__5hGf4qOP2IzI5UMpVSh5woIysd640X4zZny-F2HgOz0O3NUQBQJ-2adkoOTfW49t0ByTm4CktAqzfVDCbJkIiaPWFWtICHsl7OVRElnHB0A6A-PTfMZddwmKA-tAA_QjbjbH5ptP3ve3_Gwgt-d6HSUiddStnDduRbytIjA6aLxB2JWEzc1eYWxOwJKBX-ZzNQOTpbddbaGM4ABnWMJEO2WlImir7wl2YVnPOqz6xxFiZ93X6UDTjnmcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه تو قلب ما میمونی
🥲
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78042" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78041" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2yErS0S2HNl0tSCEFyK5PV3p8M5himrySj58dfthNnGRzC9B7PepTU7Q6xYDBelCHTMYWgw_s5hMiWuUz56rtAG7mi2-CX8Pd9m0xVngMz8RZkX86LtXCcVRXfUMdXXSg8FW-qtTKFDlFP4YTmgwaluidt62hpGk-NDrKgGePDCPJO7dzEnHIWEoreJ-byuEPKT-4c3sclPDzFrjYJ_41qa9mThSR2FieeKWyLaV8y5DY39fnvEcYbEHo28C71rulzFriHS29IpZQ3CMlKqhNBGhe6_z90tes28sq2aWQ_mWorNAKcRTMDA7P42jrgouG1fm5pyo9bWo8cg7mMclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g26
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78040" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=UC7yIphm8K3FW_5pZQN-1yvCPHSFG00e3RLLZw03jgaHalw-qhmEbrFmCfB-rODOCcIEkRQqhBrlLiMrwEnKj3ZivQiojeUsN4D43v1m0U1x-5IfkZ_URtcZ-6BoD1zPlmrrbrMH2Q4sU8NHXfefsdDFhNJTItwcSAwaNkL-t4Us-7uYYnD6oEJWqhEtqLLVGyeSNH9-vl1BtRgR8AHRw8n3AK2m_LRmF7uQfRVbh0Os3_-WHNxul1rQHgh7MwQk3DLXh9SryfoqlFJE-3Jwga_vpccA3BNJySUn_PBSWMEaH8xPDBTaDIWDgJZlnWFKNDQw_UthpWwLbDtlsUqOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=UC7yIphm8K3FW_5pZQN-1yvCPHSFG00e3RLLZw03jgaHalw-qhmEbrFmCfB-rODOCcIEkRQqhBrlLiMrwEnKj3ZivQiojeUsN4D43v1m0U1x-5IfkZ_URtcZ-6BoD1zPlmrrbrMH2Q4sU8NHXfefsdDFhNJTItwcSAwaNkL-t4Us-7uYYnD6oEJWqhEtqLLVGyeSNH9-vl1BtRgR8AHRw8n3AK2m_LRmF7uQfRVbh0Os3_-WHNxul1rQHgh7MwQk3DLXh9SryfoqlFJE-3Jwga_vpccA3BNJySUn_PBSWMEaH8xPDBTaDIWDgJZlnWFKNDQw_UthpWwLbDtlsUqOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXevk9EOsAMG-bczwTBm9OAT08i074CyMMDjjZ-KS4MX6cX4eAoC4e85cVqGEqP2-JJ_e31eAOpi8mNJZkSGB33G68jIEf6CwSAzFZe7biwItZFR_45F7Kz6MHn_eVx1g89QYm-8q-FryU4T_ifMQIJDrZqcmqwJ-XpxcVop_we9Zzmx-_Hl3BcSboDbLBInYwHNJDWm0lYMRgZ_g9rWfKk9B8NlH2nAxYQyKvzJxQvCVXIdTlaIre--hC0wtjTR0pR8veWJODxoIsMJrKg6et-nJ503Q6YBuRCj908cZwrF56mDDdwVrqIfwHWlJmZcc38D-JnMjxzGas4ydlYE8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=S8U0GJbrs5UPT6PW7aoxsNGbv0lGBtJCZlyBokwkCLX5uyq7xW-D2sEUMDaS6Pl5rx9jJqFC7SKpcrcJHY24bt0KkzleutuZHP5uia0eS3-7F_CmBp_LyiL9Y-YUajtsoZ7FOorJpcgcnC90qf3DuRSWW9bNhYe8QglT4Z7N3eaTuqMuvTbZQt9RorWPbk4bbmTQ0tGs1CcSIoiwke73BtHaYgvZH_A1gwzS-MKkqYn2-OV5_4pSSYen5sqXYFS_AOUiIzzpKXo3zCmE_K6lspGIoydKVCjkZ6xKIdgab1z6vyyLEOoBF3xsTRNJrZkJi8lugWAwKk8TXrC1qrRp4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=S8U0GJbrs5UPT6PW7aoxsNGbv0lGBtJCZlyBokwkCLX5uyq7xW-D2sEUMDaS6Pl5rx9jJqFC7SKpcrcJHY24bt0KkzleutuZHP5uia0eS3-7F_CmBp_LyiL9Y-YUajtsoZ7FOorJpcgcnC90qf3DuRSWW9bNhYe8QglT4Z7N3eaTuqMuvTbZQt9RorWPbk4bbmTQ0tGs1CcSIoiwke73BtHaYgvZH_A1gwzS-MKkqYn2-OV5_4pSSYen5sqXYFS_AOUiIzzpKXo3zCmE_K6lspGIoydKVCjkZ6xKIdgab1z6vyyLEOoBF3xsTRNJrZkJi8lugWAwKk8TXrC1qrRp4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBiukjdUrlFLfvgr62vh_yu6w6XhbQ3cfMIH4dq00ju8VMFnClb0_-BXwSZs1UKwiU3NyduSZduLF18f7wY4hz-HzsvQMaC0EUnKizYTr1ryM_KHbi8VsYTZiRveSUX_VkZi2RoiIZvV7dxUrN2AB97Ok9tNtTdZGmd0DfVh3Hb4UWiSeWhjr8vclTBD5ma-2LiIxFukh0XaQQrBPC2a60SEQ5NY7N7e4C7UOuszQh6MvhClZw7lO5pMm2OHEpuUkTDaH4BBGyvO2VfnqPJ_P1UXX9jLhja4fYuHlolpjPYfV119ddvLU85j8NzrTHCldI4uKa_oFcrUoDDxDB2hkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
