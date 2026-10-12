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
<img src="https://cdn5.telesco.pe/file/QIVchQAkDXl3F0gYn7lZkrjOFCrVseHt-VyFf7_40mzy3nzceP7-mitfJU_sUpxaf1GVTmsv4XStI5rYKrmqW4PRoXBMaHmqy8RrNPFFJg1zzIkrEFxJT7craE0EwhAYiNLZMGadGDllEuwaJ92aYWmJzCU93b0oxRfRP4NYWBfNtz3fzObtlzWQ8rrU9wgajcrRHpudbh50qVF24fvstt6ZWf6MOO6XXDaTIg7XJ61Jva9cRpAuK-YCj7T100qona4vi4fhEN3eht5ilFYmhVorXV0jtfPNFk_PoURYTNMi8dY7971TxkS_Na2ggkunipr95aNbMJcolNOhTMi6Mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 384K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-108528">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/108528" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108527">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/Futball180TV/108527" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108526">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/108526" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108525">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c408292b8.mp4?token=e6Au9IrVh2GKJ9izUVGjf-K6rE-QDFW3M0R8wwLvIrzZPcZsv7Gwfix0avIdjo0UE5qnugJi_W04VbkI0l8AlNimjyxcXF1JDHluCqqHKKFgogDuE4GCcvM72AOvpC3zrzOB7amAAMaeNd0G5L05UN9N5SVbLyuGFak0NYLWvZ6vZ1tDlQjX-p7DH9KUdh7vA1rPh5Yb31-Gxfbwx83tD0Crg32lZMzd2tnuZb2EUEcCJKZGCnI4-Sfc-H5v0L8etpwPJONOUNUlnKSB619R9pt5i4ieu42Y_2S9rdqdTebav0yX971uI0Snb3GwBmJtNmkDWGm2o3J0qY1MrQ9chg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c408292b8.mp4?token=e6Au9IrVh2GKJ9izUVGjf-K6rE-QDFW3M0R8wwLvIrzZPcZsv7Gwfix0avIdjo0UE5qnugJi_W04VbkI0l8AlNimjyxcXF1JDHluCqqHKKFgogDuE4GCcvM72AOvpC3zrzOB7amAAMaeNd0G5L05UN9N5SVbLyuGFak0NYLWvZ6vZ1tDlQjX-p7DH9KUdh7vA1rPh5Yb31-Gxfbwx83tD0Crg32lZMzd2tnuZb2EUEcCJKZGCnI4-Sfc-H5v0L8etpwPJONOUNUlnKSB619R9pt5i4ieu42Y_2S9rdqdTebav0yX971uI0Snb3GwBmJtNmkDWGm2o3J0qY1MrQ9chg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
میثاقی به نقل از حسن زاده رئیس کمیته انضباطی: فسخی برای یاسر آسانی از نظر ما ثبت نشده است و او هیچ مشکلی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/108525" target="_blank">📅 01:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108524">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fda9a24a.mp4?token=R_JEBdWMz4yQEQxHZyU7EfX7oKZjIi265zIn9609A3hpBzZicaTCTGiUibwuyxggmtIGCMqVHGmUkSmcOAd7a-uPOyYm-9r98Hqva-wyOyarm82SOs9Pm8BYPN9pmKZSn8DW_ujnYBplHLN4Cw4NGZyQH2-_qOK3k2-hVZVugOS7vE821e7Uun276tMuIwpBX0GYMIpO_fuXfPD9VJ_0Q-swu6dR19meyVpZcCZiEhVK-e_PSAKOCl01NWNQQLG1g04MXl72t3JELfdF0dCwXlK0XCtxGVPNZxAAbEaepNG1PLE_8YlYRjom-vX-v1_ErE76UEDI34djP9tq0p3tWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fda9a24a.mp4?token=R_JEBdWMz4yQEQxHZyU7EfX7oKZjIi265zIn9609A3hpBzZicaTCTGiUibwuyxggmtIGCMqVHGmUkSmcOAd7a-uPOyYm-9r98Hqva-wyOyarm82SOs9Pm8BYPN9pmKZSn8DW_ujnYBplHLN4Cw4NGZyQH2-_qOK3k2-hVZVugOS7vE821e7Uun276tMuIwpBX0GYMIpO_fuXfPD9VJ_0Q-swu6dR19meyVpZcCZiEhVK-e_PSAKOCl01NWNQQLG1g04MXl72t3JELfdF0dCwXlK0XCtxGVPNZxAAbEaepNG1PLE_8YlYRjom-vX-v1_ErE76UEDI34djP9tq0p3tWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
برای درک بهتر سوپرگل امشب آسانی فقط کافیه از این نمای دیدنی تماشاگران ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/108524" target="_blank">📅 01:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108523">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFr8qinx6KVKaKwj1dX_Fqf98qnxjhPE1hBQb3-zKDyBQQcTQBi9mshQfFhGlz6AyU_b41Og7msk3YqxscdHZKklkysTQQs561J9PL3biaw5Ty3pzrWc_yJjZQnfdPV4RGQfiI-0fXcQVnxaVxR0t6TXuX0FDJuxie-zAhy2Kod9i7IgJsFIDdKMyxe_Ro4bQQndiWZHa9s2Gd5RvD6BhKIRl_yeu9ymnck4-Mf9zLx6sQlpQ4AnU0DoN0PeroOF6CQR1n9WrG2li8pCvBrXgTnNZaqmCYjR5Ojn6T0_fHV9yK13UcGIgdFUfVK1zBl8qy8vsXEbRHxMppDBMiNWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
واکنش تند و کنایه آمیز میثاقی به تفاوت میان سفر تراکتور و استقلال و گل‌گهر برای بازی در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/108523" target="_blank">📅 01:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108522">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f09ab8993.mp4?token=s6IGxsI3QGdApc8GX05J6Obfm25QKy6xUUcbv7pkKUI0AbU8XkKUjC70j18JY-sVgIB7bP_CJgekIoxOD3ZsuIbXMmfRuB9NEwMt2QSzmGiQspPfNGPJOXJtsNxpGTGc-KpTa56QsOc-2BsOgw3bV8gGIIhQGJzxGjcGrjt2OWGhMdwT2VaqzCV2Ef5Vped3OOb8q-Ts_Cl1q5ZpE1_Oj7IAMg1jnGDsSL7dzJB3cPXgHPo27nz7U6LqnFZckFDSljvj9a8k9tiQMHkd8WeFSuV2e5gf__1mVuiokthCmoTkAQ112SvVAkPE9jU1GUwYRtLkzsUJXyAaFk8WozIpX5Ny_pRcsB91IJfp5vdzo6bjaTLU08q_mTmBZnBwPMJAkaHzLQ9fHBg4RiLAseATqnwkuLs3VpRTuNZFyodOGuQfijmomnC6GHqyuriDtce0acgoNAX_-pFiFu-h_8ElekkP0eQloHuEQNanx3k6GTyypogGyPHUPcZAi_VcBdO6_FYhRXolYeXK01lSQxymiHHc-njMGK4vHB5KhC9Vpsgq3JYA52DfmMtnehd0fXOj3JrfiuA3-_JUbab6c0I3X4tKXUBpk1lRy9PBKU7SLBBYbLS_Q7itRTYUjaqvWkXF2_kk5VyW7UCNMUxdfOLMuQrboprlLGLfd7WFOw_68EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f09ab8993.mp4?token=s6IGxsI3QGdApc8GX05J6Obfm25QKy6xUUcbv7pkKUI0AbU8XkKUjC70j18JY-sVgIB7bP_CJgekIoxOD3ZsuIbXMmfRuB9NEwMt2QSzmGiQspPfNGPJOXJtsNxpGTGc-KpTa56QsOc-2BsOgw3bV8gGIIhQGJzxGjcGrjt2OWGhMdwT2VaqzCV2Ef5Vped3OOb8q-Ts_Cl1q5ZpE1_Oj7IAMg1jnGDsSL7dzJB3cPXgHPo27nz7U6LqnFZckFDSljvj9a8k9tiQMHkd8WeFSuV2e5gf__1mVuiokthCmoTkAQ112SvVAkPE9jU1GUwYRtLkzsUJXyAaFk8WozIpX5Ny_pRcsB91IJfp5vdzo6bjaTLU08q_mTmBZnBwPMJAkaHzLQ9fHBg4RiLAseATqnwkuLs3VpRTuNZFyodOGuQfijmomnC6GHqyuriDtce0acgoNAX_-pFiFu-h_8ElekkP0eQloHuEQNanx3k6GTyypogGyPHUPcZAi_VcBdO6_FYhRXolYeXK01lSQxymiHHc-njMGK4vHB5KhC9Vpsgq3JYA52DfmMtnehd0fXOj3JrfiuA3-_JUbab6c0I3X4tKXUBpk1lRy9PBKU7SLBBYbLS_Q7itRTYUjaqvWkXF2_kk5VyW7UCNMUxdfOLMuQrboprlLGLfd7WFOw_68EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
آیتم جالب عادل فردوسی‌پور از کلید واژه مصاحبه‌های بیرانوند: درصد، دلار، ماشین، میلیارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/Futball180TV/108522" target="_blank">📅 01:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108521">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601362fff.mp4?token=iGiGXraYB0tQUNB9MwXU_jwMxhJeHYHpeiqBrlCbfvyIH8hzz_mRU26AArRhyar820DW6GUUJi80QRNiggRb2e1VdqawksU-cqivD58Nim1JwiUQiafS3FgPpOKYcB1z1MnYduM9CbI-nVLARk3a687oxMLnqOUKrpiq5rlqvC3ju9HoOwy6Zr4T8JkEfVqHTC1qtocM2EIicJ1kQbBp6PDVAUaD3J9xny4ZPH4sxRC_1MJXXHy9_5ivvAy15rNxf7M10GOArLBAQdN1gyhDzxbh98Vr4QM8Z6d1rOaqeVlcyt6Df1P56_lyVZUPIqjJLRLfEX_3iYgaTpDE81xIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601362fff.mp4?token=iGiGXraYB0tQUNB9MwXU_jwMxhJeHYHpeiqBrlCbfvyIH8hzz_mRU26AArRhyar820DW6GUUJi80QRNiggRb2e1VdqawksU-cqivD58Nim1JwiUQiafS3FgPpOKYcB1z1MnYduM9CbI-nVLARk3a687oxMLnqOUKrpiq5rlqvC3ju9HoOwy6Zr4T8JkEfVqHTC1qtocM2EIicJ1kQbBp6PDVAUaD3J9xny4ZPH4sxRC_1MJXXHy9_5ivvAy15rNxf7M10GOArLBAQdN1gyhDzxbh98Vr4QM8Z6d1rOaqeVlcyt6Df1P56_lyVZUPIqjJLRLfEX_3iYgaTpDE81xIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد سخنگوی هیئت‌مدیره تراکتور نسبت به شرایط سفر به عمان؛ مگر کور بودند که نفهمند تراکتور و گل‌گهر هم مثل استقلال بازی دارند؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/108521" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108520">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله سخنگوی تراکتور به بیرانوند: برای مسی هم تیم را به هم نمیریزیم. بیرانوند که عددی نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/108520" target="_blank">📅 01:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108519">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab8a7b19b.mp4?token=lhZpolFizXySCcAITv7DSmPnoWuhk4XN31t4MWlSemnTmKlj3Xaf5Yry6ot7KOJk9CxXvFnvjMM9PoT7s59yW_duFR88v8j7zZw_XCQpSQ-RjLx6ZrTn2swPX91NSS4e19QKG5D3rHxHo77KDh8kKiPwRYuFA_q6HZC_DO48DvcUH-NlcrdlnrR6M1DuI4n32zN6X5z8HLPj2fSnwTAoRodltC0lg0w_DSrQzH1qZ1y9OCNi8rZ_vTEY2fOWx05_uuKFaSoX044HRzVbF9g5PFVKuiWcMDrZsUV4eJiBgnd1txUcbZibRMZASHkkJ2u5qpkP3RCfJNvf_Aj5dqd53g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab8a7b19b.mp4?token=lhZpolFizXySCcAITv7DSmPnoWuhk4XN31t4MWlSemnTmKlj3Xaf5Yry6ot7KOJk9CxXvFnvjMM9PoT7s59yW_duFR88v8j7zZw_XCQpSQ-RjLx6ZrTn2swPX91NSS4e19QKG5D3rHxHo77KDh8kKiPwRYuFA_q6HZC_DO48DvcUH-NlcrdlnrR6M1DuI4n32zN6X5z8HLPj2fSnwTAoRodltC0lg0w_DSrQzH1qZ1y9OCNi8rZ_vTEY2fOWx05_uuKFaSoX044HRzVbF9g5PFVKuiWcMDrZsUV4eJiBgnd1txUcbZibRMZASHkkJ2u5qpkP3RCfJNvf_Aj5dqd53g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🙂
شاعری هوادار استقلال برای برد شیرین آبی‌ها در آسیا مقابل الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/108519" target="_blank">📅 01:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108518">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a267abb0d.mp4?token=ftghupQM_beIoAg_tzSlongUc8csGDiZe5t2MnTdVbbOk70uLt2fa7xLIrGOJ2oTnvPR0ch4-V6uyXrtEEpp9-PMWC8Eg_kVaBFWreIxTmagGOiQDxguzRwqDidX1Qkx7CNjDDCPEucMc0JqaERtvI_Sku9u2gJy8pz_q11CkgtFFu4sgbOvtA0caZuDmWuIgjNWQBnYOtjl3CGcprnFt9s7DmK9-CVGWNsDe45cMfQrJr1l6iTEEdUMf_UPZS64cgBPezblfvs8HwndgZHePNK0cMxMwWhafFxOz6QsRzwGSQIqOA4PGRge8vMz6NPn8hONcoGNLPwjZkTyJZYsfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a267abb0d.mp4?token=ftghupQM_beIoAg_tzSlongUc8csGDiZe5t2MnTdVbbOk70uLt2fa7xLIrGOJ2oTnvPR0ch4-V6uyXrtEEpp9-PMWC8Eg_kVaBFWreIxTmagGOiQDxguzRwqDidX1Qkx7CNjDDCPEucMc0JqaERtvI_Sku9u2gJy8pz_q11CkgtFFu4sgbOvtA0caZuDmWuIgjNWQBnYOtjl3CGcprnFt9s7DmK9-CVGWNsDe45cMfQrJr1l6iTEEdUMf_UPZS64cgBPezblfvs8HwndgZHePNK0cMxMwWhafFxOz6QsRzwGSQIqOA4PGRge8vMz6NPn8hONcoGNLPwjZkTyJZYsfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کری هواداران استقلال برای پرسپولیسی‌ها: بروند برای خیبر و سایپا کامنت بگذارند، اینجا آسیاست و جای شما نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/108518" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108517">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW7GbXZncDr2a92zfJYQE-J8TMiSogXxGnqJr_xXTdvBCd1qs3VhuznK92gjBFGor4s3NUB0_uO2h3bwhawnomU8KWfghG0KOEY3hsHkoDnylV9MmOgjGzf7QlBqOxomZceH3nZt2ZmulSl_5sIs7yllz2J45WmadcNEzR05AxCisBd60ZW9MIKSeV7ejdVt7Xmi8kz7n4d_cZ9N6AcwRAxFZF6fFYXsylMbhZCb14x5S0u7N-36yIOdTp24ye5dRcEDSLtUVqlSytXxs71qctngJfWFxN2GVHQlexrNYKEY_1fHdWj_e27-KrlKBFYpLAQxL2u1ypGmoc9TajIivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🇶🇦
استقلال تحت هدایت سهراب بختیاری‌زاده، برد مقابل سه تیم مطرح قطری.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/108517" target="_blank">📅 00:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108516">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217c826d5b.mp4?token=VTjRlpxDnjBjzOY_cUFdClxiObp73Abtn_MY84v-zMsmnLlhasl6INKB_LSBWg67s7OGvSIDh7yoHlSGFXHrSwXYeODgmbK0b6Y2Utq-BEvVTyLP_IZDjpbbsdlrrstpiUOnSEp5Wc3D1W3Ce9uF8SHBdWglSgd2TpqWUtV3-lSHen27geyE6elnhc5l-2Y_OTLhggnloETxVL1lxqcptsJxxzPkw_b0mb7hcPxjZsYbmsZddTXYsIPRIyxQNKGdeCkmHYXsvDdx1cnuTpFjEAruTIUKDTpjAPzx_YxuulLh3edXSIuq19n7j5-APlC7O_SEmGT6m9ab-SXh_8KY2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217c826d5b.mp4?token=VTjRlpxDnjBjzOY_cUFdClxiObp73Abtn_MY84v-zMsmnLlhasl6INKB_LSBWg67s7OGvSIDh7yoHlSGFXHrSwXYeODgmbK0b6Y2Utq-BEvVTyLP_IZDjpbbsdlrrstpiUOnSEp5Wc3D1W3Ce9uF8SHBdWglSgd2TpqWUtV3-lSHen27geyE6elnhc5l-2Y_OTLhggnloETxVL1lxqcptsJxxzPkw_b0mb7hcPxjZsYbmsZddTXYsIPRIyxQNKGdeCkmHYXsvDdx1cnuTpFjEAruTIUKDTpjAPzx_YxuulLh3edXSIuq19n7j5-APlC7O_SEmGT6m9ab-SXh_8KY2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
⚽️
میثاقی: توافق اولیه یحیی گل محمدی و فدراسیون فوتبال برای تیم ملی امید صورت گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108516" target="_blank">📅 00:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108515">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr1sucWCv1aLONOr7UeVKuDLXVNqMCmSXylnxxHLvcfiM4efakNRmOkYuT7L48TJFX7Ul3RgjgNCwZMxGjAiWCmXfVJ0wwsSoYmCl5FCd5ceDmmBCgqtMffM8EPcxCRr3qqhE_gvvY-FGu5yhjdRNIbyWqVA6oBfFadqTz-GJEHs9hgGPCH-CVe4mCcMhtaa9H8ICCZ1aFCDVia4lNz5DuHwxc85fFc_DH2qsV4OttMiyn1mq01dn-901Psz_Bewou_QDWReA2sE_vCuKXZUr6O9L45ZOvT19y00rJllDyMlhTYft5vNmmytbFGVeS-EokrN3kpfS6pDwTXWtxhu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
🇮🇷
استوری کنایه‌آمیز سامان‌فلاح مدافع استقلال به مهدی تیکدری مدافع پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108515" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108514">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648dfd6944.mp4?token=pykUGiHxYFR4Hswdxk5gubCrq_tBuutZRgWwuiDR7iptT11g15JGTe5Rgni0etWb4Z7eifriId4Pcqtd7Yh6fznjFD4DjpPpnIZVtHTy3QnNIJmyieOpCgBHlhIItGkeK7_57sLpJFIIL1WNVTKcQYMC-gBVrBZqnRLVh00aE9OOPHVhubwx7x96ItWV6aUqhZDAjPhq07kRKu837P7qgTVJrPi-ZV2l86gGUMkcjBOGOTlFTMHg3b5ZhgBrUeMhsFcGqLkULUi-OxWq0Q8RbDKiQVPy5k8FcgEnA-73v1LRHGt18wk1-kAaySrE8onxv3ToIeEra-RidyoMGQLgQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648dfd6944.mp4?token=pykUGiHxYFR4Hswdxk5gubCrq_tBuutZRgWwuiDR7iptT11g15JGTe5Rgni0etWb4Z7eifriId4Pcqtd7Yh6fznjFD4DjpPpnIZVtHTy3QnNIJmyieOpCgBHlhIItGkeK7_57sLpJFIIL1WNVTKcQYMC-gBVrBZqnRLVh00aE9OOPHVhubwx7x96ItWV6aUqhZDAjPhq07kRKu837P7qgTVJrPi-ZV2l86gGUMkcjBOGOTlFTMHg3b5ZhgBrUeMhsFcGqLkULUi-OxWq0Q8RbDKiQVPy5k8FcgEnA-73v1LRHGt18wk1-kAaySrE8onxv3ToIeEra-RidyoMGQLgQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
واکنش تند و کنایه آمیز میثاقی به تفاوت میان سفر تراکتور و استقلال و گل‌گهر برای بازی در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108514" target="_blank">📅 00:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108513">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇮🇷
پژمان‌ماندگاری مدیر رسانه‌ای استقلال: مصدومیت یاسر‌آسانی جدی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108513" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108512">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdCW-88zyWq0eYKC2qfGfs2MMY9evXEI9szrTwT2s5S8tJXq9E3E0OIv6-3qluhzvhqyO3DShJu3-X0szNRisRwIt9vI_CskkYI42c-9ARO2QXX37EZ32f7yzWOztsZan8xG73k5qdpVYXP7rkb8uJA0A_VmOkjBgj7DbtLvdXdGP7-oPST9C8sCxr4ULoSZq2SGn6mPXRD6f04mZjLdWWOPWfAQ-Nt7ZYM5JNGAnkhdqksf2CQs693WtI-LIxYLFrBprRgi_-yEsjvcbCZBd7pVWHhBa85ds6s9kv-zWrJnXLqzO1NxES-m2dNO6GxCHXL3kR6vTU-vmrptG323cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توییت کنایه‌آمیز استقلال به پرسپولیس پس از بازی: یاسر‌آسانی به شدت قانونی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108512" target="_blank">📅 00:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108511">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
❤️
زنوزی مالک باشگاه تراکتور: همیشه گفته‌ام عدالت اصلا رعایت نمی شود/ یک تیم با پرواز وی آی پی دولت سفر می کند یک تیم مصیبت می کشد
🔴
نمی دانیم از چه کسی گلایه کنیم/ آنهایی که می گفتند پزشکیان حامی تراکتور است حالا بیایند جواب بدهند
🔴
حداقل اگر می خواستید یک تیم را با پرواز دولتی بفرستید به ما هم خبر می دادید
🔴
بیرانوند جوانی کرده است و رفتارش را می گذاریم روی جوانی اش
🔴
امروز شنیده ام که تیم های دیگر نمی توانند در عربستان هم بازی کنند این را من شنیده ام
🔴
باید برویم به AFC نامه بزنیم  و مشکلات پروازی خودمان را اعلام کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108511" target="_blank">📅 00:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108510">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔥
🇮🇷
گل‌یاسر‌آسانی با گزارش عربی الکاس قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108510" target="_blank">📅 23:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108509">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCUqUme0tv1ULdUcOug-eDtR0oiCBxAlT4G82nC0eKb-SrqeiGJdLHsekSiQWIe6RlZCz1hlYdewZKXYn2tYax6m2QpiIUVZzpGsNL7j_YT6f23n2t8398UxKXz4CiuAmV4VIhRKafiDmG8T5PxYpSy3DGTbflc_Pt4kEFM34rkF9Yi8bdhmzoUzNeyUPwzCVj-7ha5s8DMRfirhk_Et-P9WzhDsvt9ZS3GAVYhV5TCSDMe49xtW2_hSxIt_brSNUdyhr1nP6BiTZmCtSkr2WiXrNR8OT--kkdKFSQhaRe4kGcJpDhvqbTWr5r8mnPvdEqTzyIKBzg651rjyYiUNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌نخبگان آسیا؛ دومین تیم قطری هم مقابل استقلال زانو زد؛ یاسر‌آسانی با عمل به وعده خود تیمش را با وجود مصدومیت به برتری رساند؛ فرعباسی بازهم درخشید
🇮🇷
استقلال
😀
-
😃
الغرافه
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108509" target="_blank">📅 23:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108508">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40f9d30d1.mp4?token=UB0WU1FcVPVD6upIVs5oEHH43XKZPMYik6VmWsvORDHMRQdZbx3n66yxhAKPrG-lXdx4S2PDBM0ZuTm7aW2up7_GWfgSNtUiDT3aAx3e0jKGiP_S0Tv9ubi75x3BZKss3meQ_808j3s4Mk194TDugXmkvlw69zLJwrpYEHuWyaHFjDml7GIPH5o3xB6p4timaZCQBVUDISnXnkS4aGQH82kxj1-MSN5hMVUIBg75DkW_zVGPQ9Ahbq0R_4tB-3z7q_a3A_m6B9ehC-JlDK_GGiw31LizQT2YwqSfnkGJOJ-LKOF0BrkI8XsxV_YiMFbiEWdCLSdMECGUKOiZdksBiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40f9d30d1.mp4?token=UB0WU1FcVPVD6upIVs5oEHH43XKZPMYik6VmWsvORDHMRQdZbx3n66yxhAKPrG-lXdx4S2PDBM0ZuTm7aW2up7_GWfgSNtUiDT3aAx3e0jKGiP_S0Tv9ubi75x3BZKss3meQ_808j3s4Mk194TDugXmkvlw69zLJwrpYEHuWyaHFjDml7GIPH5o3xB6p4timaZCQBVUDISnXnkS4aGQH82kxj1-MSN5hMVUIBg75DkW_zVGPQ9Ahbq0R_4tB-3z7q_a3A_m6B9ehC-JlDK_GGiw31LizQT2YwqSfnkGJOJ-LKOF0BrkI8XsxV_YiMFbiEWdCLSdMECGUKOiZdksBiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صالح‌حردانی امشب شانس آورد فوش نخورد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108508" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108507">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خوشحالی اعضای استقلال پس از سوت پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108507" target="_blank">📅 23:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwaQLE1cQzH4jUKmqbMsXmn7WVtsXEEhoSuqbBQgXVeIQORocA52M7DfwXAMbAlVInQSATSpW0vL70ULzoRUdKmjQOHbFylQ5JFrwYp8xVc-Hw-1uWJKpx79uiFeh4_wAiT3qibEHW5_JBS_9RJpjPrZTIWWcG8RDxOzC-4N5xRdAl2NmL88PViCAGUfF5oOYuLwH9euXvBZsN0BbuGvLH5kTLsdfRoYtNfJhOYFTI9tRSX4J60MMrA4H_oxPWkSKsGx0qUAqT1qpoDA0riyV4gmnaA6Fd5pem6cy9Q_-fo8uyI3Et6HueSAiShWJZt5pAJowUY_IAb6iq29LTMb7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌نخبگان آسیا؛ دومین تیم قطری هم مقابل استقلال زانو زد؛ یاسر‌آسانی با عمل به وعده خود تیمش را با وجود مصدومیت به برتری رساند؛ فرعباسی بازهم درخشید
🇮🇷
استقلال
😀
-
😃
الغرافه
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108506" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هنوز تموم نشده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108505" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب دیگه بخیر گذشت</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108504" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از کون آورد استقلال این دقایق
😐</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108503" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بازممممم شانس آورد استقلال</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108502" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حردانی کسمغز
😐
😂</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108501" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حردانی ریده</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108500" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آشورماتوف نجات داد
😐
😐</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108499" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108498" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108497" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الغرافه زور گل زدن نداره فقط ریدمان بازیکنان استقلال میتونه این امر رو محقق کنه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108496" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسلامی هم ریده</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108495" target="_blank">📅 23:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فرعباسی بازمممم گرفتتتتت</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108494" target="_blank">📅 23:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۷ دقیقه وقت اضافه
😐
😳
🚨</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108493" target="_blank">📅 23:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpYJFhxLsgVQSl-2nEHP497URDVVfyFqeycdJJaxOyVs5-JnRtiw2wjpOErzCKMesBIdRRjTXNhD7cBDFvNWvaP4KHrG4jk1AWFnUAJMRUf844pBlRYI-1vN6GKG6eLv81X7AjlsPQRSVk6-KzeMYy-6nf4VkyIkToWktA7uHkTok5geLWvXQ5_0SDbvRXSeeGWbhtw6xA2xyjZNtJqvX0pDiA6IyvBmwjsesDDOA10QqcoT3f89AqCuu1qob8yud3Fb8oibD6VKtEiAtmW8M0gTeSXuY214vNnGdX5IGUWslTxEUTTuhSID6M2bNB_P8vIFzeL8PUJpxF8xfueoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العین امارات چهار بر یک مقابل نماینده عراق برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108492" target="_blank">📅 23:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24051a9445.mp4?token=b5rbmrmHemGQJgfxjjDZqDcHGG-oyVe0N5yKGmFoxkirssqOW_C6QHGGk-bpIzinlT1D8qbIONrjqs97tBiJkWDBikanjjdcg15RjCrLriYYpCspISCAR8ylg6m9ZJVgX_WFmAWbapAHGySBywBj4625RWaqiwQj5g7F4XN9CZNfZXAQdgVTGhEUrORg8_io4JDZcoIQiMlBkRHODhoGDRc1xletJSfztrLUYWPizeENED0veO0zyz3rl2lcagFur_lCAPgNFHf5jRIwkYp94vsyxyJMyGYtEtHZ7npnvSvQOJ-s6Xk_iAO3no8VGc7OMPBFaVwGXgVxpNQaB99RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24051a9445.mp4?token=b5rbmrmHemGQJgfxjjDZqDcHGG-oyVe0N5yKGmFoxkirssqOW_C6QHGGk-bpIzinlT1D8qbIONrjqs97tBiJkWDBikanjjdcg15RjCrLriYYpCspISCAR8ylg6m9ZJVgX_WFmAWbapAHGySBywBj4625RWaqiwQj5g7F4XN9CZNfZXAQdgVTGhEUrORg8_io4JDZcoIQiMlBkRHODhoGDRc1xletJSfztrLUYWPizeENED0veO0zyz3rl2lcagFur_lCAPgNFHf5jRIwkYp94vsyxyJMyGYtEtHZ7npnvSvQOJ-s6Xk_iAO3no8VGc7OMPBFaVwGXgVxpNQaB99RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپر سیو فرعباسی روی موقعیت تک به تک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108491" target="_blank">📅 23:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سوپر سیووووو حبیب فرعباسی</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108490" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1974c7b3a7.mp4?token=haK4BOs3WTTyp77k2-Xao0hpy6DPuI6td8n1zfZ4cttEw1bLZehUujhSxcIGXKsLAZJYL39sN18nziGU5cDyQ8FBy65AvWem0XYRe7-P3q8veLjhg2zHt6wW9S4Jx5iqXqrsFq_tJ-IFAcxf0Rs2E15K9FPYDLSb_VHmz6mB0eEmXvPBO-TWk_lxBAkyxO87Alzb8YX3iU_0o8szJC108nfs1NsyxwfW09TDV8VsP7BL9vKntiqTyJLuYKE9ayrEukAjkjxa2qvslAy91fPO6IRGA5M7s_3jBT-t9vpwzzPjXk6rkFiLeAn57GCJNEcztCuSCWohlihOwB6OuxCePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1974c7b3a7.mp4?token=haK4BOs3WTTyp77k2-Xao0hpy6DPuI6td8n1zfZ4cttEw1bLZehUujhSxcIGXKsLAZJYL39sN18nziGU5cDyQ8FBy65AvWem0XYRe7-P3q8veLjhg2zHt6wW9S4Jx5iqXqrsFq_tJ-IFAcxf0Rs2E15K9FPYDLSb_VHmz6mB0eEmXvPBO-TWk_lxBAkyxO87Alzb8YX3iU_0o8szJC108nfs1NsyxwfW09TDV8VsP7BL9vKntiqTyJLuYKE9ayrEukAjkjxa2qvslAy91fPO6IRGA5M7s_3jBT-t9vpwzzPjXk6rkFiLeAn57GCJNEcztCuSCWohlihOwB6OuxCePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سحرخیزان عجیب رید امشب
😐
😐</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108489" target="_blank">📅 23:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سحرخیزان بازمممم ریددددددد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108488" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=lAYyKca9KUx_za5ulLhE0P-uUDP3Imdovm8TBx5tArQajxObLkfP7hvNUhUhbCeMo1r0y-RylttaNwF8xouyaczzwfL56m0rwcbvUifTiPT7bXzEWEd0W3pESNHjjqvRF6ksfGxYC672y48goSc0hybCk29AmnEjk0ZSAYR3ACov0fh-bsHmd1BFlXxZPrZstr6zTMxIDDUiT9KJJHv07snabQdI-59O2FLx1wVobkHGXXrS6W5lPKNvxRp0hpaU-ZJJdMBHNNNtmOkhzcURUElnkx3-4QSMIG0hRBqvcs_7G41lZRteh5-_oElY83DtAqJdbinh8nh5znfsgXFqng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=lAYyKca9KUx_za5ulLhE0P-uUDP3Imdovm8TBx5tArQajxObLkfP7hvNUhUhbCeMo1r0y-RylttaNwF8xouyaczzwfL56m0rwcbvUifTiPT7bXzEWEd0W3pESNHjjqvRF6ksfGxYC672y48goSc0hybCk29AmnEjk0ZSAYR3ACov0fh-bsHmd1BFlXxZPrZstr6zTMxIDDUiT9KJJHv07snabQdI-59O2FLx1wVobkHGXXrS6W5lPKNvxRp0hpaU-ZJJdMBHNNNtmOkhzcURUElnkx3-4QSMIG0hRBqvcs_7G41lZRteh5-_oElY83DtAqJdbinh8nh5znfsgXFqng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108487" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">استقلال کوووون آورد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108486" target="_blank">📅 23:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108484">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رونالدووووووو گل شماره ۹۸۱
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108484" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">النصر دومی هم زد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108483" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استقلال سه تایم مختلف تعویض کرده و دیگه حق تعویض نداره</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108482" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از حلال بال سهراب بختیاری‌زاده نیاز به حرام بال جواد نکونام در ۲۰ دقیقه پایانی هست</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108481" target="_blank">📅 23:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">النصر یکی به نفتچی زد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108480" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آسانی با مصدومیت داره وسط زمین راه میره</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108479" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108478">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آسانی با مصدومیت داره وسط زمین راه میره</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108478" target="_blank">📅 23:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108477">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79f4a95ed.mp4?token=oSHRBeKQ0IvwSGzCBJeh0sn9_2Wc5DJr6YF-1Py8dPztrfehYlR76KocjyDNoTi7ns6cn7HTfM3hFc9XrthXkyY3DGaFk9_m49_4Ki5DrF1O8gOWfXnSRcQLxG_Wr1bF2W3GZcV15gTja2TMxjjgpcH7vNC6lFZU7RjtyKOfVrkdFYFKSA5Lq1bZpZd_wK9L6NISa3Qs_qlWlZRuLYZwQlpySUXfOt3oCZ-E_mXz1rk8WlhC3UrnCcRAYBWwp07k2rx087jDyG4M8vjQtSLVbJAKUpegZyVgYm2ESYdPj5ZhVs_XoAhSHV_HvHmT2nZUsKQhhe3d8YNmqQEpLTXOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79f4a95ed.mp4?token=oSHRBeKQ0IvwSGzCBJeh0sn9_2Wc5DJr6YF-1Py8dPztrfehYlR76KocjyDNoTi7ns6cn7HTfM3hFc9XrthXkyY3DGaFk9_m49_4Ki5DrF1O8gOWfXnSRcQLxG_Wr1bF2W3GZcV15gTja2TMxjjgpcH7vNC6lFZU7RjtyKOfVrkdFYFKSA5Lq1bZpZd_wK9L6NISa3Qs_qlWlZRuLYZwQlpySUXfOt3oCZ-E_mXz1rk8WlhC3UrnCcRAYBWwp07k2rx087jDyG4M8vjQtSLVbJAKUpegZyVgYm2ESYdPj5ZhVs_XoAhSHV_HvHmT2nZUsKQhhe3d8YNmqQEpLTXOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
گلر نیمکت نشین الغرافه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108477" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108476">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یاسر‌آسانی رو به قصد کشت دارن میزنن
😐</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108476" target="_blank">📅 23:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108475">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ولی چه ریدمانی خوبی کرد
😂
😐</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108475" target="_blank">📅 23:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5ed1792.mp4?token=HH2lqT9GefBRs5DHU-lH1rsdwAyOKV-lUs5z4E38P70qOeXR-y78N34-9KIqpbsGDlMaTXfuAOI523_kDhU0_C9LZZ96kC-Gwe_JqpsBsoNuHDvoFnlXpUAZzv7dzdHBJb4NMI7WLk7lDoDLhLMB4js3CG8fUFByJ7KBEhad9c0gaZf110hwQnNMxGdQEqmUUg6qIAnRSuNopDkyjMvQFCSTRd9WUgKrrSnD1WdSNBkFMnM50AqCubHAoEioxpjZjIUXSvNwsFeeb6dWzqe8wJc7EGHeXoOVNWcxrAGT_9qR9Yi-WiMXydj8hWUKhNOHWa3SCbduFV1yzd7gmCk9pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5ed1792.mp4?token=HH2lqT9GefBRs5DHU-lH1rsdwAyOKV-lUs5z4E38P70qOeXR-y78N34-9KIqpbsGDlMaTXfuAOI523_kDhU0_C9LZZ96kC-Gwe_JqpsBsoNuHDvoFnlXpUAZzv7dzdHBJb4NMI7WLk7lDoDLhLMB4js3CG8fUFByJ7KBEhad9c0gaZf110hwQnNMxGdQEqmUUg6qIAnRSuNopDkyjMvQFCSTRd9WUgKrrSnD1WdSNBkFMnM50AqCubHAoEioxpjZjIUXSvNwsFeeb6dWzqe8wJc7EGHeXoOVNWcxrAGT_9qR9Yi-WiMXydj8hWUKhNOHWa3SCbduFV1yzd7gmCk9pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل دوم استقلال به الغرافه توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108474" target="_blank">📅 23:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108473">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلر ریددددددد
😂
😂
😂
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108473" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108472">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چه شوووووووتی</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108472" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108471">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سوپرگگگگگگل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108471" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108470">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گودرزی زدددددد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108470" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108469">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گل دووووووم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108469" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108468">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108468" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108467">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بازم موقعیت استقلال گل نشددد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108467" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108466">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108466" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کوشکی ریدددددددد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108465" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108464">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108464" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108463">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
آسانی مصدوم شد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108463" target="_blank">📅 23:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108462">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
آسانی مصدوم شد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108462" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108461">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">علیرضا کوشکی بجای ماشاریپوف اومد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108461" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108460">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سحرخیزان بازم ریددددد
😐</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108460" target="_blank">📅 23:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108459">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b597f0d9.mp4?token=O4JMoZcDKpm1T6i46V1fHcYYvcVbddxeJXXmx36h5JeaDUw5VXbiQXk4Ros-T_2P11wY3XkeuYsznRzyFmC9WQA3DoVBRdBmhACqMbQdgYCk9sJ6osYFAlT94Nx6eZhkPmwueqkgPyZpG4kesbVw3P7DPSnt_dkaxevPTVAj0Ctcq74Jtzr4x-SvSKIcrsGhhk_8nZphFum5rKPRSeqd_nAZpZLYS0EAVUTTd-Zv7VqjouNcAlnDqokigwd08sj3Hqb4v6k9WW39apnCiB3Tanxscs3s7HCQxgGi7UShi6tPBurO7hK6mhPCq4JtBGofTfsxZSpE3blJ27dafVAzcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b597f0d9.mp4?token=O4JMoZcDKpm1T6i46V1fHcYYvcVbddxeJXXmx36h5JeaDUw5VXbiQXk4Ros-T_2P11wY3XkeuYsznRzyFmC9WQA3DoVBRdBmhACqMbQdgYCk9sJ6osYFAlT94Nx6eZhkPmwueqkgPyZpG4kesbVw3P7DPSnt_dkaxevPTVAj0Ctcq74Jtzr4x-SvSKIcrsGhhk_8nZphFum5rKPRSeqd_nAZpZLYS0EAVUTTd-Zv7VqjouNcAlnDqokigwd08sj3Hqb4v6k9WW39apnCiB3Tanxscs3s7HCQxgGi7UShi6tPBurO7hK6mhPCq4JtBGofTfsxZSpE3blJ27dafVAzcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول الغرافه به استقلال توسط فرجانی ساسی
الغرافه ۱ - ۱ استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108459" target="_blank">📅 23:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108458">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گل برای الغرافه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108458" target="_blank">📅 22:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108457">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">العین اونور ۴ تا به نیرو هوایی عراق زده</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108457" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108456">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">العین اونور ۴ تا به نیرو هوایی عراق زده</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108456" target="_blank">📅 22:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108455">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آغاز نیمه‌دوم استقلال و الغرافه قطر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108455" target="_blank">📅 22:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108454">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇮🇷
تهدید جواد نکونام بعد بازی الشمال: اگر بازی بعدی اینجوری بخواهیم سفر کنیم، با تیم امید خود در آسیا حاضر خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108454" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108453">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU5olrtkhxejGmrURS-8S7CmIngBfFXcO7VMiYpqZVkE9-RB1bF5Y6pkhA0pC6thXDBxAltooeTjj6d04xn3NE2n0Qjq2yvsDj5PyIPafEYixG3vBMKszLuih8mGjWCvRELRhu8oEF3mHERjvWXuTWg6jOubBCzWtJlf6awIsdxFVwMG3srYPkZwNyYR430q15odIGs8tAHqufyQZFLSvokziPzoWFQjd6xe8ZodxJCIqMsCp5RHn7hoPU--3Kw3nM9CgmaQr13gb-dVYMdt1tkfI4aHgLDCgu8h83V5zAyzKgDtn_5zTZh8O768TgK2O6PqXjP2gC1cae-LnBDpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی النصر و نسف قارشی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108453" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108452">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔥
فرصت خطرناک الغرافه با مهار دیدنی فرعباسی و دفع مدافعان استقلال همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108452" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108451">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c4a7f733.mp4?token=g2iw4pUeHqkTbvjd5IlEqaakmlUuCh665wvMZUaxvmsQd4cvULmsMhC98P5RiDEgxwHYDGa-9MoUAywOX-fDbUjjwy6NcKPJWGunJOLzg0dHXylqvsH82LipTZEi1gvhbLVKL0L7tER921rEkG0Kcf2XfGWdkgbxSE7AgdSNSwtNGfuQpRrdi2Bzp81jH-zULRiSmKftM-W0onNP7KBJ44btsoI8ktKXYuxIYKUOYBpkAW9NCpHd_AlCW3Ma9P7LPLeK5PmgebIs-cNZN9CTGc4EQD24kHl_LyQew6ElvoW0eOsCf_ffuoygcheEfGHOuAU9dWhkAbYJvtzSyLPmKU_f08Y1volCezvtLPHBaZbSSZNbqY7UGEcWMLJNY63vjt5aeG4_u0KSopBZREeagZGnVhY2Ya5Lo7kx1qmIoqdP8EIokvxiOWS9IycDXbn8ldQOHQdhTzSyySIM4o0NN84BvOmZv8DmJgKxI9umpkkN3vgoUuICecqefdwYSYIQ9Ej8GgS9oQs7ZjvUGw9DIZgcHmpdW3rHRulEyefZFs93lw3BPSURnZDU32p6kLMQBwcp6LWsW_NxrVvD6sjtttleyf8ALICSfkNmcKO14LicY6o2nqfFbsyZ9YZWxa2Qfe4_zAXfTVyFm52VMfeto-xKSPIsyFf2zhipEv2qIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c4a7f733.mp4?token=g2iw4pUeHqkTbvjd5IlEqaakmlUuCh665wvMZUaxvmsQd4cvULmsMhC98P5RiDEgxwHYDGa-9MoUAywOX-fDbUjjwy6NcKPJWGunJOLzg0dHXylqvsH82LipTZEi1gvhbLVKL0L7tER921rEkG0Kcf2XfGWdkgbxSE7AgdSNSwtNGfuQpRrdi2Bzp81jH-zULRiSmKftM-W0onNP7KBJ44btsoI8ktKXYuxIYKUOYBpkAW9NCpHd_AlCW3Ma9P7LPLeK5PmgebIs-cNZN9CTGc4EQD24kHl_LyQew6ElvoW0eOsCf_ffuoygcheEfGHOuAU9dWhkAbYJvtzSyLPmKU_f08Y1volCezvtLPHBaZbSSZNbqY7UGEcWMLJNY63vjt5aeG4_u0KSopBZREeagZGnVhY2Ya5Lo7kx1qmIoqdP8EIokvxiOWS9IycDXbn8ldQOHQdhTzSyySIM4o0NN84BvOmZv8DmJgKxI9umpkkN3vgoUuICecqefdwYSYIQ9Ej8GgS9oQs7ZjvUGw9DIZgcHmpdW3rHRulEyefZFs93lw3BPSURnZDU32p6kLMQBwcp6LWsW_NxrVvD6sjtttleyf8ALICSfkNmcKO14LicY6o2nqfFbsyZ9YZWxa2Qfe4_zAXfTVyFm52VMfeto-xKSPIsyFf2zhipEv2qIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فرصت خطرناک الغرافه با مهار دیدنی فرعباسی و دفع مدافعان استقلال همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108451" target="_blank">📅 22:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108450">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
پایان نیمه‌اول با برتری یک بر صفر استقلال</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108450" target="_blank">📅 22:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108449">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سوپر سیوووووو حبیب فرعباسی</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108449" target="_blank">📅 22:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108448">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9b3628a80.mp4?token=GNZy897XGnYtvMUjQmFwES6rQaVnEsDWPfgD-0MVXUottYQmBYBq7wPK5ZiaKTC774tFvyv9vRyo1yoqO9f8fPAKlABSJ69Fuc54bAVv_SU2BlIf_lfgzRBhSnmSrhBPsRJVm8JMqbO067cumpOV7iT0x1MZYf3zH7k7tL2vqHEoY-wgd4FP_hH6S_2fIoeGVhWVTlBWE1ILPIC1ThwS9HauH3ahwOlOGh9HPvXgk2hLS6-c2MJ4E8ZU4u4wTvgGYXOzrfyd0579HteoJaYvoDWINFD51FhVSngrS8lYLUz4QuqYjr--3xxR-NLafVmHTClBsBA4Ta6Ftwf-Qd6rjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9b3628a80.mp4?token=GNZy897XGnYtvMUjQmFwES6rQaVnEsDWPfgD-0MVXUottYQmBYBq7wPK5ZiaKTC774tFvyv9vRyo1yoqO9f8fPAKlABSJ69Fuc54bAVv_SU2BlIf_lfgzRBhSnmSrhBPsRJVm8JMqbO067cumpOV7iT0x1MZYf3zH7k7tL2vqHEoY-wgd4FP_hH6S_2fIoeGVhWVTlBWE1ILPIC1ThwS9HauH3ahwOlOGh9HPvXgk2hLS6-c2MJ4E8ZU4u4wTvgGYXOzrfyd0579HteoJaYvoDWINFD51FhVSngrS8lYLUz4QuqYjr--3xxR-NLafVmHTClBsBA4Ta6Ftwf-Qd6rjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تک به تکی که سحرخیزان از دست داد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108448" target="_blank">📅 22:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108447">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سحرخیزان سوپر پاس گل یاسر‌آسانی رو به بدترین شکل ریدددددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108447" target="_blank">📅 22:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108446">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استقلال چیووووو نزددددد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108446" target="_blank">📅 22:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108445">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108445" target="_blank">📅 22:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108444">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔥
🔥
😳
نماهای دیدنی از سوپرشوت یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108444" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108443">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084f2850fa.mp4?token=pQJ63RYzIPqFGthaVJPrxE94iMKzrpPlemozr30irfVDmJeLxoMujIm0uUTGcaVlMfG2D9rmIFw4poRiqMI0D2erx69yHwdCaXut6EtFs0XZR2GjmscbdmR5biFciiiR5uohQlbxXKw8R2ejN-UMJ0NA98vyYq5C2YrUnjROYHeM7M2kQaHO3R_0EcFznA6sH1pzSeEO5D0A1BDVLhHadT10xf0i7wiq7vk1Ivl7pDTdxst6GHkTNljkKHZTE3nd53CxJa0hU3NTZLeJJgyb30eIqzbw0OtHwVXGi7GVIqGs8JnXlh_WuhJ3vc8NykZDH_QiBtwhmBxvUhmC9vxJ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084f2850fa.mp4?token=pQJ63RYzIPqFGthaVJPrxE94iMKzrpPlemozr30irfVDmJeLxoMujIm0uUTGcaVlMfG2D9rmIFw4poRiqMI0D2erx69yHwdCaXut6EtFs0XZR2GjmscbdmR5biFciiiR5uohQlbxXKw8R2ejN-UMJ0NA98vyYq5C2YrUnjROYHeM7M2kQaHO3R_0EcFznA6sH1pzSeEO5D0A1BDVLhHadT10xf0i7wiq7vk1Ivl7pDTdxst6GHkTNljkKHZTE3nd53CxJa0hU3NTZLeJJgyb30eIqzbw0OtHwVXGi7GVIqGs8JnXlh_WuhJ3vc8NykZDH_QiBtwhmBxvUhmC9vxJ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
سوپرگل استثنایی یاسر‌آسانی به الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108443" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108442">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چی زدددددددد دیوث
😐
😐
😐
😐
😐
😳</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108442" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اللللله اکبررررررررر
😐
😐
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108441" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سوپرگل محشررررررررر
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108440" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آسانیییییییییییی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108439" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یاسرررررررررر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108438" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108437" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108436">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=WAXKOzFdZaaPgQ1tdKF-q_kEqSkZMNSp4YgcHcQYFeCQNlJ3Bt1IoUHwPUiIKdl1DdaUVtSvTnfp7kop-wA6zf-0Q71XvOzZrQrNWFwF7yz3Njbo4inftSMmbzB8_XGZ6NYLDsMuZ3AEqLX0pQrVlqvagyw7MRWJKxjMwhpjU9MyLbXzwqcGFgvzcN3Ue9s0ClaRw25V1D-gXXSHucsbvEPhTTyvSDTCOWfQH4hhTh6GfRzOuc7BACnjU_7lWs4vJZc-h-29yiDfZIpSqD5fiRAGR9fSM2YJgXnkBrcRa03CiDRfA_BehJytLccgNa6p9H3FCLSIYeiHCA5fqBGU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=WAXKOzFdZaaPgQ1tdKF-q_kEqSkZMNSp4YgcHcQYFeCQNlJ3Bt1IoUHwPUiIKdl1DdaUVtSvTnfp7kop-wA6zf-0Q71XvOzZrQrNWFwF7yz3Njbo4inftSMmbzB8_XGZ6NYLDsMuZ3AEqLX0pQrVlqvagyw7MRWJKxjMwhpjU9MyLbXzwqcGFgvzcN3Ue9s0ClaRw25V1D-gXXSHucsbvEPhTTyvSDTCOWfQH4hhTh6GfRzOuc7BACnjU_7lWs4vJZc-h-29yiDfZIpSqD5fiRAGR9fSM2YJgXnkBrcRa03CiDRfA_BehJytLccgNa6p9H3FCLSIYeiHCA5fqBGU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇵🇹
العربیه: نیروهای امنیتی ریاض رونالدو رو از ورزشگاه خارج و به محلی امن‌ منتقل کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108436" target="_blank">📅 22:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df157d6c0.mp4?token=WAl8_xycklA3jbFAdNne8N68pdGecPLLrrIDMnJaQD46XikNZimyyVeKTjWrLYS_br2DZO7Bs2JI5KK0b4pzt--iSc9GR332emZ6nrN-AoAG2431C8KFt-YsJEq96UxRTKAuhf6Q4S9UgI3P4clYyY6EHdECovTFY2Q6_s_rYFAT27geHfD_DQWd7Bv3tP0wdfNBWSr-uOKp7XhMUpy1SGV07QI38chbQB2UOnW4leZN0_uyJp_8njyqbzwvymza9tKsf68Jv6jmXE4PMMV1hNb95leqbWCXAlupWHKHwqEVokdjlrOxJ0VDtvpXdKIaxRVmBTG7L7l89_DNxEqPnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df157d6c0.mp4?token=WAl8_xycklA3jbFAdNne8N68pdGecPLLrrIDMnJaQD46XikNZimyyVeKTjWrLYS_br2DZO7Bs2JI5KK0b4pzt--iSc9GR332emZ6nrN-AoAG2431C8KFt-YsJEq96UxRTKAuhf6Q4S9UgI3P4clYyY6EHdECovTFY2Q6_s_rYFAT27geHfD_DQWd7Bv3tP0wdfNBWSr-uOKp7XhMUpy1SGV07QI38chbQB2UOnW4leZN0_uyJp_8njyqbzwvymza9tKsf68Jv6jmXE4PMMV1hNb95leqbWCXAlupWHKHwqEVokdjlrOxJ0VDtvpXdKIaxRVmBTG7L7l89_DNxEqPnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چشمی بازیکن الغرافه رو زد یارو هیچیش نشد ولی افتاد روی پای رزاقی‌نیا و رزاقی‌نیا مصدوم شد. عجب سمی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108435" target="_blank">📅 22:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
‼️
🚑
امیر محمد رزاقی‌نیا هافبک استقلال بدلیل مصدومیت از زمین مسابقه خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108434" target="_blank">📅 22:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
‼️
🚑
امیر محمد رزاقی‌نیا هافبک استقلال بدلیل مصدومیت از زمین مسابقه خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108433" target="_blank">📅 22:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوووووری از الریاضیه عربستان: رونالدو گفته که بخاطر تهدید به حمله حاضر به ورود بازیکنان تیمش به زمین نیست و بازی باید لغو بشه! فعلا ناظر بازی مجوز لغو رو نداده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108432" target="_blank">📅 22:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
‼️
🇸🇦
🇺🇿
بازی النصر عربستان و نسف ازبکستان در نخبگان آسیا بدلیل تهدید حمله موشکی از سوی حوثی‌های یمن به تأخیر افتاده و احتمال لغو بازی زیاده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108431" target="_blank">📅 22:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTbpzCDvsAYRMfiMMa21T_cGZA5-UZvzIFHAZSTbhiS7jVEvuuiiRRbASwHFIVc2IZV2NT9Wk2sYly8pTKPfUchQg73pjNQS53UGOqx1LwL1Pe9ChAAEdnWIVq1zdEFOHNdsLMBq6Th7Zv6NUIXf6X_w6KJVBm5K1FPbAIyEQ-4AR9NK59XAUwjlLQuV-0yOdDa1SaF_5z3I8lTVa49zwKGk2AivE9OP3I_4-iTgJcoOa19KBqz2alTKWuVi62zcmmepcTM3o9wcMVbv5R8ROV9N6t3bHML2UiPMLX9S-uu0zLXUvEjhtikBaSNv3osjBJY0jBVGQ71dgivMS9h57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇸🇦
🇺🇿
بازی النصر عربستان و نسف ازبکستان در نخبگان آسیا بدلیل تهدید حمله موشکی از سوی حوثی‌های یمن به تأخیر افتاده و احتمال لغو بازی زیاده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108430" target="_blank">📅 22:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صداوسیما قشنگ یک دقیقه عقب‌تره
😐</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108429" target="_blank">📅 21:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
برررررریم سراغ بازی استقلال و الغرافه قطر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108428" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
