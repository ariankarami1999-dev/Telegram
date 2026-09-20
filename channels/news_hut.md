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
<img src="https://cdn4.telesco.pe/file/Dg0WRgoEdKlhP7PkANmk30b2tUpDP2uTWXcP_2g0PQTAYNGRLZ7wxRcxfFbDvfL1GQKUek1aiZLQ5k0KGbIZEt6qHlKI7LMcIQBpHpQQc33iAykfZdNp_RbMrFsK8bDl7zaxL00WKL1Zn0DWsZKxfIjvq3uddGLuQu34st6Ht89nbr8_HRYSR5cexZ0ysWLKSXxR8XjqF62fPMobkncO3UbPIjStevrr2E3c6DJrarmNqfVPMC8dcQjjvWMK_3td4_rNaadVH5_rzqctO5bIz8PAoBqU9JvcSDfDoDk7VqjqIwvXIAxZpF60KdXmKKOCtk2bGMXo3qxiDWne47L4Wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 23:31:04</div>
<hr>

<div class="tg-post" id="msg-71965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=fcCfyksF52fcX6gn0WhaeGtiJyPwCFSGXCYoOTb14vJa_xXg6R07-RtLoirpBgDELbZUqcxRHHBj6aZs7dDb_RQYZqLLvLTjx-Og2FVN9pdiaRIeV9CXql9hPVKKlCjZwsy0FAo7G2SbqBPaPTh6GyIor5ij3gaTzzVKIlFWU4quWgeZhccDa2dv93ZKmp0PaTwjGCjng7ZMkAH2sYNoGQ3h6hzRYqHgaW_lHlgULWIQHzpacpQ_CoUoFDlEsrx1d6_d7RDXYE2nYi0K1J1KoYzF15ffiWd8NbOcT79iXkW3Iah2oFG3-FbNtrgiyNqpiFnG1m6iYMuYljGrt6pkQj3shnBPLQxWUzbB1C0yK5imi3nvW2zy9zFfgemlw_Kg1sBs5xEZaw-Qt5ONfutdWNpyXTFj4R9cNbQJnlp4Mv4smetkqxRTBtes5zN2UMFDGMr84CE10Akc6V3Y8UEWUNrONPy4hdfF8mNFR4YjCvbrzB52wojXc3kcGWYzloMnUCNjoNnDs6ViE8GdZfD-q2701aRpCigZ2xXzC6XnSLo0i34sEpieVpP_NYyXhMX7E_DIG8A9TvRsD2BTjVc5c8PgHnCBdHWiPuKf9L_dbF04H5ZIgR_D_0N_VVqYLJUFm0crFaV4cd3Sg_ooTgxG9cdw5vtYKB-LbvudzJl6aF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=fcCfyksF52fcX6gn0WhaeGtiJyPwCFSGXCYoOTb14vJa_xXg6R07-RtLoirpBgDELbZUqcxRHHBj6aZs7dDb_RQYZqLLvLTjx-Og2FVN9pdiaRIeV9CXql9hPVKKlCjZwsy0FAo7G2SbqBPaPTh6GyIor5ij3gaTzzVKIlFWU4quWgeZhccDa2dv93ZKmp0PaTwjGCjng7ZMkAH2sYNoGQ3h6hzRYqHgaW_lHlgULWIQHzpacpQ_CoUoFDlEsrx1d6_d7RDXYE2nYi0K1J1KoYzF15ffiWd8NbOcT79iXkW3Iah2oFG3-FbNtrgiyNqpiFnG1m6iYMuYljGrt6pkQj3shnBPLQxWUzbB1C0yK5imi3nvW2zy9zFfgemlw_Kg1sBs5xEZaw-Qt5ONfutdWNpyXTFj4R9cNbQJnlp4Mv4smetkqxRTBtes5zN2UMFDGMr84CE10Akc6V3Y8UEWUNrONPy4hdfF8mNFR4YjCvbrzB52wojXc3kcGWYzloMnUCNjoNnDs6ViE8GdZfD-q2701aRpCigZ2xXzC6XnSLo0i34sEpieVpP_NYyXhMX7E_DIG8A9TvRsD2BTjVc5c8PgHnCBdHWiPuKf9L_dbF04H5ZIgR_D_0N_VVqYLJUFm0crFaV4cd3Sg_ooTgxG9cdw5vtYKB-LbvudzJl6aF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
من به تمام کشورهای عربی و همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند در روابط تجاری و مالی ما اخلال ایجاد کنند، ما دو اقدام انجام خواهیم داد.
نخست اینکه قطعاً به شرکت‌های آمریکایی — از جمله شرکت‌های حفاری آمریکایی که فعالیت گسترده‌ای در پیرامون ما دارند، و همچنین شرکت‌های تجاری و بنگاه‌های اقتصادی آمریکا — حمله خواهیم کرد.
ما آن‌ها را هدف قرار خواهیم داد و اعلام می‌کنیم: این حمله‌ای به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران است؛ یعنی مقابله‌به‌مثل در برابر حمله.
از سوی دیگر، به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما نیز اقدام متقابل انجام خواهیم داد. اگر کشوری همسایه در اعمال محاصره اقتصادی علیه ایران — برای مثال در امور مالی و فعالیت‌های مرتبط با ما — با آمریکایی‌ها همکاری کند، ما کشتی‌های آن کشور را در تنگه هرمز تنبیه خواهیم کرد.
ما بر تردد و عبور و مرور آن‌ها و برخی فعالیت‌هایشان محدودیت‌هایی اعمال خواهیم کرد، یا در زمینه همکاری‌های اقتصادی، اقدام متقابل انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/news_hut/71965" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=vod6_ZsE-GFhOMo5jjKkcpSJG-yDT7sEj_h1X9sMkY2oJ1ri8opxF5pO4ah2-Eiu_465spmUt6CUC1MBNk2i4F94HL07SbOmykBAMS1hXKE37B7uZvjlEu7dJkE0xkXLgROry-giUqsbKTARRP_hBAq3IcS828aiPiWzUGLvsQtNn7VZuW3cPXxPsT7KrEmMe07NiQuMGOjjH-7qgBfLJhZcle3WvM4vwh4FZMMFiQmD7a45Jco4fZY93rurKvetjTvpPx9wLgpYNWBUbqIvj4eOhrI6JuLIG9C0cgrzfInwwEJszcXBYZK2vt3hZUgAM0JwWv8qEFTL7pg2BCa8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=vod6_ZsE-GFhOMo5jjKkcpSJG-yDT7sEj_h1X9sMkY2oJ1ri8opxF5pO4ah2-Eiu_465spmUt6CUC1MBNk2i4F94HL07SbOmykBAMS1hXKE37B7uZvjlEu7dJkE0xkXLgROry-giUqsbKTARRP_hBAq3IcS828aiPiWzUGLvsQtNn7VZuW3cPXxPsT7KrEmMe07NiQuMGOjjH-7qgBfLJhZcle3WvM4vwh4FZMMFiQmD7a45Jco4fZY93rurKvetjTvpPx9wLgpYNWBUbqIvj4eOhrI6JuLIG9C0cgrzfInwwEJszcXBYZK2vt3hZUgAM0JwWv8qEFTL7pg2BCa8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران دختره بعد از اینکه پروفایل اکسشو‌ چک میکنه و میبینه اکسش رفته با یکی دیگه درجا سکته میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/71964" target="_blank">📅 23:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=H1mEbWHirMKf3sfSoQ4UPk1-GaZRJHoHfrL-WIfv057t2FbSlDuYY1GFJ3FkaHtwXRDgQ_7Z2Sz00VtwvBY2BrlqWaCwE_uUlDfv5RthTq2l3HYYsnTZL7bRmj7LsFBciFggH39aKFSGt0PN_kb7eVREok5jmeQLrHNrnUK2sNu9HQuHP7MawC2SU523qIgVkadNIOBNtX9u2xYLiNWXrupH5UdNP8oW9t6vdCWMeAgR6_FHhni2sU1xZtoiWuT1lb9G3sAPOx_Fe7-FnynahpdpHgfC3Izt17LFQY3Rfylmg3xN0BwiV9r8uWc50rccIdSIR6NJ7RHZ7OreM0uZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=H1mEbWHirMKf3sfSoQ4UPk1-GaZRJHoHfrL-WIfv057t2FbSlDuYY1GFJ3FkaHtwXRDgQ_7Z2Sz00VtwvBY2BrlqWaCwE_uUlDfv5RthTq2l3HYYsnTZL7bRmj7LsFBciFggH39aKFSGt0PN_kb7eVREok5jmeQLrHNrnUK2sNu9HQuHP7MawC2SU523qIgVkadNIOBNtX9u2xYLiNWXrupH5UdNP8oW9t6vdCWMeAgR6_FHhni2sU1xZtoiWuT1lb9G3sAPOx_Fe7-FnynahpdpHgfC3Izt17LFQY3Rfylmg3xN0BwiV9r8uWc50rccIdSIR6NJ7RHZ7OreM0uZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی چند ماه پیش:
کیرم تو جمهوری اسلامی! کیرم تو قبر خامنه‌ای، ایشالا تو جهنم میسوزه!
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71963" target="_blank">📅 22:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=ncEBJqqKuqSIY7H438Vtprvigrq6BLoo5GhThYC9-HBgTS1fRlYmWoJNUMAmz93RB5mNgsyWu6zzMOn8d4t77l_XKd6o7gfEd1GmnAAcvtSZFBaSoLIZYRrGptsKjy08zcjmVzemHFbjfgly0ZIpFZHSCQR-ohspl0sz-infRATD4pnHwQ4cjiVJcwcHyc7ZE01M63mLEaQ4Tp49mFZYebwXZgrpWyzkFvCsn3IBNpWMJdR_i9DwYL0pMqA90ub9QDiZCZi4MrcBWVGUz4cv1Zy8rMZ1uxEpz4qGmgLg8i4t_QEnjlOmHze32y1Ytg_JSFw6xfAkZLrCmXip6oX2xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=ncEBJqqKuqSIY7H438Vtprvigrq6BLoo5GhThYC9-HBgTS1fRlYmWoJNUMAmz93RB5mNgsyWu6zzMOn8d4t77l_XKd6o7gfEd1GmnAAcvtSZFBaSoLIZYRrGptsKjy08zcjmVzemHFbjfgly0ZIpFZHSCQR-ohspl0sz-infRATD4pnHwQ4cjiVJcwcHyc7ZE01M63mLEaQ4Tp49mFZYebwXZgrpWyzkFvCsn3IBNpWMJdR_i9DwYL0pMqA90ub9QDiZCZi4MrcBWVGUz4cv1Zy8rMZ1uxEpz4qGmgLg8i4t_QEnjlOmHze32y1Ytg_JSFw6xfAkZLrCmXip6oX2xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانومی تو تهران میره به پسرا پیشنهاد میده که با حساب خودش برن کافه، اما هیچ پسری قبول نمیکنه و دست رد به سینه این بانو میزنه.
آخر سر هم کلش خراب میشه میگه پسرا پرنسس شدن و تنها میره کافه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71962" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C646lXkvnREq2QbN2wWtYp_zS6VFw0hPV8QahfngKx0WzH1H_573ATD0oJkVQPXJ-5EtWsBNOl-WRAY2EtlJEHV8Jb8OrKayKtLgYpUKG7VwQxFq2aUpfi8WLTWcCx7jeJOwrEsBuLfrrauwrw_wMNaGMVw0-8nG5_0ovjrL5-lnoNcnU2jJILS0ldoUyLnA0mQSINW-MU9hsPCk4AORaxexzIQo7MRmwfPF579vAZEtDmBQPvTobltmjbYFWZFcWQ45jn7bGnA3sV9g1CHhNKubnGRWnxu1GLlqknvdp4hBhCTZzAReB7OWvTDgs5z10732m8LlCZNx-zee_Tm4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71961" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=e5WPSkHxLlq6At_iAHddtvY71HYFbxmIqiI5Tgx1Ei1vzogR2mHlRoTwYqN3XaUZaVKHECD4yzk_baY9NN7M4bLU-7606oTairYwdG8bCN8WFbdhh8rfMBtxxDoeTm1yzjlydEOGiy6njVwXJaTmgvbQ_ec5fQiwEqzCz3qGZCvVB4tg9_vD7YoNlb7pM07VL5Z456ChhDL4tb1yvoi7_UJReuRdHE6oy6-OnuuDPxY2O2ZtHMi5Ffw_zykNFCojXQ_XjAVDyabjbPCpjDqro-no3DvqN4uLwok3gW_ESXC58ytlVLeAb-TKGstLy0DqWEOPzp5m5_-pzZJlrt-g0yP-AvOWiG3aUvXxZjX4AfoGb-_351UHymyPkyG-fVO6KtIjronfLv9v-fupH7oPXmFCqL3xGdhBp4_sCtrHry28pDv0Q0Qzk4YlAg-uSbAo370sS7Zm8ve6GOAmJ2A6gi4OsW1PvQ6pgYDZRxUj8mWxHj-rx_L0iLC7V3AIupomzG5OSY0baRqQp6v4ngVY6xt3qI1hVqRrPZ3HYdCsC67wTs1W1WaBflFNd2oQhN3jHWXniQLCNJCg4fr8YshYPhwwLtecsGGrYA9PxFHOnJuDC2ATQ2xHRmf-unuovUceJ5Q-pgDqDin4dFuhFpvmsvPHlQv3pft7gkXM-tn8mVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=e5WPSkHxLlq6At_iAHddtvY71HYFbxmIqiI5Tgx1Ei1vzogR2mHlRoTwYqN3XaUZaVKHECD4yzk_baY9NN7M4bLU-7606oTairYwdG8bCN8WFbdhh8rfMBtxxDoeTm1yzjlydEOGiy6njVwXJaTmgvbQ_ec5fQiwEqzCz3qGZCvVB4tg9_vD7YoNlb7pM07VL5Z456ChhDL4tb1yvoi7_UJReuRdHE6oy6-OnuuDPxY2O2ZtHMi5Ffw_zykNFCojXQ_XjAVDyabjbPCpjDqro-no3DvqN4uLwok3gW_ESXC58ytlVLeAb-TKGstLy0DqWEOPzp5m5_-pzZJlrt-g0yP-AvOWiG3aUvXxZjX4AfoGb-_351UHymyPkyG-fVO6KtIjronfLv9v-fupH7oPXmFCqL3xGdhBp4_sCtrHry28pDv0Q0Qzk4YlAg-uSbAo370sS7Zm8ve6GOAmJ2A6gi4OsW1PvQ6pgYDZRxUj8mWxHj-rx_L0iLC7V3AIupomzG5OSY0baRqQp6v4ngVY6xt3qI1hVqRrPZ3HYdCsC67wTs1W1WaBflFNd2oQhN3jHWXniQLCNJCg4fr8YshYPhwwLtecsGGrYA9PxFHOnJuDC2ATQ2xHRmf-unuovUceJ5Q-pgDqDin4dFuhFpvmsvPHlQv3pft7gkXM-tn8mVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی «لوچینگ یوان‌یو ۱۰۸» با پرچم چین و یک کشتی باری با پرچم پاناما در نزدیکی سواحل سنگاپور با یکدیگر برخورد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71959" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=YHHZ_WUWtzqpfo1t4EhQG2iex8A2sIvAk-NIa0aEiW3ifCioJl7-v8bgKyFAgJqvXRFm79xHkjatETUmbS8Xjic4XfGpI25nX027cB67Z4y-iqUaVs7T6zT8o4nFkTFiTze9vMUEY2HgcMCDDMM6tOJf6gUFf_4yfYS6D0knUvTIri8PpJqPyk6EQ7pcXzxgk7s8jsEBwmLdgdGvguH11P0ItFYY0kXTRFlLIDxO1Rq12FGaXKrLPTrIxl-PJgNW752nGY6p1ZwN59fbgM4cZSVYtHKRZi4kSx52KDVY1buaGzhZfJ83MFQyI8ImSLgioVgEob5EGatvPddxHl7TUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=YHHZ_WUWtzqpfo1t4EhQG2iex8A2sIvAk-NIa0aEiW3ifCioJl7-v8bgKyFAgJqvXRFm79xHkjatETUmbS8Xjic4XfGpI25nX027cB67Z4y-iqUaVs7T6zT8o4nFkTFiTze9vMUEY2HgcMCDDMM6tOJf6gUFf_4yfYS6D0knUvTIri8PpJqPyk6EQ7pcXzxgk7s8jsEBwmLdgdGvguH11P0ItFYY0kXTRFlLIDxO1Rq12FGaXKrLPTrIxl-PJgNW752nGY6p1ZwN59fbgM4cZSVYtHKRZi4kSx52KDVY1buaGzhZfJ83MFQyI8ImSLgioVgEob5EGatvPddxHl7TUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن به مایک جانسون رئیس مجلس نمایندگان آمریکا:
لطفا کار مربوط به ایران را تمام کنید
۸۰ میلیون ایرانی منتظر شما هستند
مایک جانسون:
میدونم ، قطعا و علامت پیروزی
✌🏻
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71958" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mm-VRpXzZM5LZvXTSumZsVchx32ynCpBxFJvySTxtSa9GCru94ukN3dG_lQSR-VqLCgYHW8ifCD4RgWbZxUEq_7D12CMGsOCvepu2zNC08DKm6OaQx0UmUEQsOp7AJwHe5k7AHC_Heula37hVjKn4Xxx5Dgy6mxStIlSepOdvimVQXJtC_sLpPvrBZFI6WgSWpB2rLANBVPo5HEgVRxUPpeq2_x0SCC_bNj9BzL-OWtCdjxKa6h_fmWlOE_fdi8YhxfiWYlqCZrsjkaaQbrK6f3J8SYuqEutkYCDfu9P9FMXmHnhbnPmOoz7mNNwPElpg3ID1cYUO88lO8QWLuIlzT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mm-VRpXzZM5LZvXTSumZsVchx32ynCpBxFJvySTxtSa9GCru94ukN3dG_lQSR-VqLCgYHW8ifCD4RgWbZxUEq_7D12CMGsOCvepu2zNC08DKm6OaQx0UmUEQsOp7AJwHe5k7AHC_Heula37hVjKn4Xxx5Dgy6mxStIlSepOdvimVQXJtC_sLpPvrBZFI6WgSWpB2rLANBVPo5HEgVRxUPpeq2_x0SCC_bNj9BzL-OWtCdjxKa6h_fmWlOE_fdi8YhxfiWYlqCZrsjkaaQbrK6f3J8SYuqEutkYCDfu9P9FMXmHnhbnPmOoz7mNNwPElpg3ID1cYUO88lO8QWLuIlzT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، یک موشک رهگیر پدافند هوایی اوکراین در حومه کی‌یف موفق به اصابت به پهپاد جت‌سوز روسی «گران-۵» (Geran-5) نشد و این پهپاد لحظاتی بعد به هدف برخورد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71957" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12842b3342.mp4?token=YDSovQHnlPCwZkz6q4pNALB0BlGdh7sa1WMlgfiES7wtynH_L8taV2qeci1drSvWZyKebfy6GFWe0W_dHfRszkrmof7hZiZhw_2GxjmyYTBcr2LlmH--eLjOFwlEMlH2DMeK2VnISLKatuDVReLgeokFETZ1ub-Wj_ddW5CtlvmfwC3Bp_PXzONC2WAXF0we8vEEEsqfRD5BApgNxckaxcxa264foLAGFTYfKS3CE-SbBStjuCQFNjIfcFUNXpGbYNGgZcXBqVmXVUHtP4zOTu1Tr6BnyR8101rHfWPglnM8Fb8I0y-WRVS3UEBn-NJ5mt6rLpQ4SEC9cnInTxY6wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12842b3342.mp4?token=YDSovQHnlPCwZkz6q4pNALB0BlGdh7sa1WMlgfiES7wtynH_L8taV2qeci1drSvWZyKebfy6GFWe0W_dHfRszkrmof7hZiZhw_2GxjmyYTBcr2LlmH--eLjOFwlEMlH2DMeK2VnISLKatuDVReLgeokFETZ1ub-Wj_ddW5CtlvmfwC3Bp_PXzONC2WAXF0we8vEEEsqfRD5BApgNxckaxcxa264foLAGFTYfKS3CE-SbBStjuCQFNjIfcFUNXpGbYNGgZcXBqVmXVUHtP4zOTu1Tr6BnyR8101rHfWPglnM8Fb8I0y-WRVS3UEBn-NJ5mt6rLpQ4SEC9cnInTxY6wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رویترز، سامانه‌های پدافند هوایی در اربیل (واقع در اقلیم کردستان عراق) یک پهپاد را در نزدیکی فرودگاه اربیل سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71954" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند و آمریکایی‌ها در مسائل داخلی به جان هم افتاده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71953" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71952" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXNg0f7PiuyHQk6vuSmcUNfc_nGY-x9TZlK-qeknxZ4-Hn2jvdwjbckGKjPs8pbaWvDPum2nf7Yv8AB-2r3iPy5psk_hbsJ_HptvuoCae4hMufGgvH3_NH8zWAu5fOKZD-76IZ_iAXf76J72Hjep1VNe7Hm7bDMHNZPzq_plcFdOzMU0McRr4JVDMTjR3zVhqFTARjB89y-BzLoyfFiIyOY7zWSiS-4nWhLDyI24r4EufdHkK_gA7KxutxX79M_g7M7ZuJuPwdX52v55-77sHM5wq0Yp7Lqkn45iKFTR9zn4pnsaMRQto3BafWrxQ3bbUvfyR0DohZSYotYT3pw2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71951" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=EkcGwG1jW3i-Z6rbPlQM5hrE9HN6PmXS_sfpHqtx0cYkB6qqO21AJv52WMgJv3cpuKEO7MXvc7IABRzsJikmmY5S9PyNe5YeLoirR6gzN_tSe5UoQ4p3MABIOyfFk_yct6uVNJg3Io3vGrS5HA7sveFnF_HIJkoRJ7X_ESE9i-YP-4JkFFuUeq3JCZEP8UEZ8MknUlBBofFES-07tTKA9dtvIerX_oUP4yRlH2PmDk9YnNhWf-RFvrb_636p8EzCL7Fy47U4yNU3zz5g7xSEVfPip7yvOo0O3doqVa1jD0iHj2bjCdnXXe_vcYuRY1Eq4D0rYwvlPGZ3P34zaaUulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=EkcGwG1jW3i-Z6rbPlQM5hrE9HN6PmXS_sfpHqtx0cYkB6qqO21AJv52WMgJv3cpuKEO7MXvc7IABRzsJikmmY5S9PyNe5YeLoirR6gzN_tSe5UoQ4p3MABIOyfFk_yct6uVNJg3Io3vGrS5HA7sveFnF_HIJkoRJ7X_ESE9i-YP-4JkFFuUeq3JCZEP8UEZ8MknUlBBofFES-07tTKA9dtvIerX_oUP4yRlH2PmDk9YnNhWf-RFvrb_636p8EzCL7Fy47U4yNU3zz5g7xSEVfPip7yvOo0O3doqVa1jD0iHj2bjCdnXXe_vcYuRY1Eq4D0rYwvlPGZ3P34zaaUulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برخی از مقامات ایرانی همچون موش‌ها پنهان شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71950" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ درباره ایران:  در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.  گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.  بهتر است درست رفتار کنند!  @News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71949" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ:
ترامپ می‌گوید «احتمالاً» برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل آمادگی دارد
😂
پزشکیان هفته آینده در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71948" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.
گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.
بهتر است درست رفتار کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71947" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهراب قاسم‌خانی نویسنده سریال پاورچین :
تو سریال یه اصطلاحی بین مهران مدیری و سحر زکریا ( نقش زن و شوهر ) بود که درباره " کوه رفتن " به هم میگفتن؛
مثلا زکریا به مدیری میگفت بیا بریم کوه، یا میگفت تو اوایل ازدواجمون بیشتر میومدی کوه،
ولی اصلا موضوع کوه نبود و داشتن درباره رابطه‌شون صحبت میکردن.
بعد از 5,6 قسمت مسئولان صداوسیما متوجه شدن و دیگه اجازه ندادن این دیالوگ تو سریال رد و بدل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71946" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=vgyGv5E_b3phTBtrCHAhylLzJB3w2icZgiaCzMArL8bbrJM4n77TyXSpbSr9eWlJG3We3lvgwQFUQcA-vtIh52JYh9N2LDVM0J_Rm_zgvjKZFOGzifyxz0YdpbzTXWKie83APdtno11hvDE8xFoEkrxsw-VLyiddD2yQjVWGzn90F0s9n8E0_prPNdIPARZ1PXzK7RqLxzuu0FJvRu45i7-qD_WEF5sGpjGf0zfIRCUhfwtGHzSaciThbcHUH379AuQSnID56Dm-6UMB-6y7lvXyJSIMzIE9mAYh9nNRGBbc9Ip82wFqlibqPZvSAkY1icGj-mhzJyeG4s5C60H4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=vgyGv5E_b3phTBtrCHAhylLzJB3w2icZgiaCzMArL8bbrJM4n77TyXSpbSr9eWlJG3We3lvgwQFUQcA-vtIh52JYh9N2LDVM0J_Rm_zgvjKZFOGzifyxz0YdpbzTXWKie83APdtno11hvDE8xFoEkrxsw-VLyiddD2yQjVWGzn90F0s9n8E0_prPNdIPARZ1PXzK7RqLxzuu0FJvRu45i7-qD_WEF5sGpjGf0zfIRCUhfwtGHzSaciThbcHUH379AuQSnID56Dm-6UMB-6y7lvXyJSIMzIE9mAYh9nNRGBbc9Ip82wFqlibqPZvSAkY1icGj-mhzJyeG4s5C60H4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی :
100 میلیون بشکه نفت تو مملکت گم شده !
کسی که مسئول نظارت رو این موارد بود بهم گفته که 100 میلیون بشکه نفت رو نمیدونیم چی شده. نه تو دریا ریخته شده، نه امریکا تحریمش کرده و نه دزدای دریایی دزدیدنش.
به نیروی مسلح، قرارگاه فلان‌جا، نیروی انتظامی و ستاد کل چه ربطی داره که همشون دارن نفت میفروشن؟
اطلاعاتی نباید نفت بفروشه؛
اطلاعاتی سواد و فهمش رو نداره، درک نمیکنه. اطلاعاتی‌ای که 50 میلیون حقوق میگیره، میلیارد دلار، ترانزکشن، بیمه، حمل و نقل و این چیزها رو نمیفهمه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71945" target="_blank">📅 16:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=ZCWXrDVBOtwqQtsLOGhvLNjF7PRW9993APlb7hJDlEOyGoC3KPCqEX_Rj1NMC9EC5mevckeQG0aERwJV7bUy9lUaql5eb4ZUg0nuHayQH5y8juoyhxFXag8jIks9UWmmTQliJ05gHjW3TfDpC_vn7GtJbI_LhvhFNZMHx2IuuhlY2xHu8daDgGusHNz4K30lohvmp7LmvrkE0luIuNe65qWIE-Z-Q3QPXKIHXGCUqVE9Q94BRigXAJSoML-FP402igLATrB5PiPGrSGIRi872Cn_-usu-aeNjZXDuFDYSnxlTdixNpEqm_XOdLsMJ0WsvJARzrHb1Kdflz0GH59Z_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=ZCWXrDVBOtwqQtsLOGhvLNjF7PRW9993APlb7hJDlEOyGoC3KPCqEX_Rj1NMC9EC5mevckeQG0aERwJV7bUy9lUaql5eb4ZUg0nuHayQH5y8juoyhxFXag8jIks9UWmmTQliJ05gHjW3TfDpC_vn7GtJbI_LhvhFNZMHx2IuuhlY2xHu8daDgGusHNz4K30lohvmp7LmvrkE0luIuNe65qWIE-Z-Q3QPXKIHXGCUqVE9Q94BRigXAJSoML-FP402igLATrB5PiPGrSGIRi872Cn_-usu-aeNjZXDuFDYSnxlTdixNpEqm_XOdLsMJ0WsvJARzrHb1Kdflz0GH59Z_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71944" target="_blank">📅 16:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حمله گسترده پهپادی اوکراین به پالایشگاه کاپوتنیا در مسکو، روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71941" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=g9Fomp5AgfjyUHDeYDf8lNqC7B2xoCwLkLHHpTZ8m3rDfzsLi83uJLJaQDwuOhzLRV1OHhuqJouM1nePjFw_8VT7lJmHoTFO1GlrIf6IpN9Y1QPb-pw4ErERvMIJsj6oi8adsbVNrkWF9RY1cDwLPPTl1XpJdg2SYOhM1AcP7HF6MXD87Rj2YXuZ4Jm2feSAc4zVXeQme44xBUB394NTiUgJPOod3GeypoGdhoJcL0YGtVtcv6yZJXAoUatSu6_XilJhkHKaHn8MnRD_iuaN_CHvPwsV2Gq8ODMm8GTmi7NwY33BQ2T8QIlZYNUcy9d9QaF6pJgXKSW1GI_v_tCPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=g9Fomp5AgfjyUHDeYDf8lNqC7B2xoCwLkLHHpTZ8m3rDfzsLi83uJLJaQDwuOhzLRV1OHhuqJouM1nePjFw_8VT7lJmHoTFO1GlrIf6IpN9Y1QPb-pw4ErERvMIJsj6oi8adsbVNrkWF9RY1cDwLPPTl1XpJdg2SYOhM1AcP7HF6MXD87Rj2YXuZ4Jm2feSAc4zVXeQme44xBUB394NTiUgJPOod3GeypoGdhoJcL0YGtVtcv6yZJXAoUatSu6_XilJhkHKaHn8MnRD_iuaN_CHvPwsV2Gq8ODMm8GTmi7NwY33BQ2T8QIlZYNUcy9d9QaF6pJgXKSW1GI_v_tCPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانگین آی‌کیو یمنی‌ها:
یه حوثی پین نارنجک رو کشید واسه اینکه نشون بده خدا باهاشه و نتیجه شد این.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71940" target="_blank">📅 15:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
هرگونه حمله به ایران، منجر به حملات «مداوم، مؤثر و دردناک» به تمامی پایگاه‌ها و منافع آمریکا در منطقه، «بدون هیچ‌گونه محدودیتی» خواهد شد.
کشورهای منطقه‌ای که با تجاوز آمریکا همراهی کنند، شریک این حمله محسوب شده و نباید انتظار خویشتن‌داری ایران را داشته باشند.
بر اساس اطلاعات دریافتی آمریکا با چراغ سبز متحدان منطقه‌ای خود و بر اساس هماهنگی‌های صورت‌گرفته در یک نشست اروپایی، در حال برنامه‌ریزی اقداماتی جدید علیه ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71939" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=ZinFbRDa9inN927KQMWa-1lksf0xeEE1Ndcwvxsy9M3EbKTqTRCVGbGYvZyQzG6WTMYnacZhjJXChQbrndNaGy-8JLO3OAcUIaSGIlIYPsrVjtRx3Et56WnxlUADbd9166HsIkt7UwsVeKVlr3AD8wXKtW_1yciU1PkreMKeZy6Qr0Ka8X3eFtHcmM6JQ1yOiiCYbNYHvorAMVzYL1lfVlT488d5rSjj4M_7SWPlCYYvlyasWpEwiXhibKRczloAfwb054AWWy5-vlBzs4zrJ3Rv9op95rPiyIoUwjz3kI8Qu0VCUlJey87mPmdltuWPh5tvaS8VXi8mKY5Etao8lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=ZinFbRDa9inN927KQMWa-1lksf0xeEE1Ndcwvxsy9M3EbKTqTRCVGbGYvZyQzG6WTMYnacZhjJXChQbrndNaGy-8JLO3OAcUIaSGIlIYPsrVjtRx3Et56WnxlUADbd9166HsIkt7UwsVeKVlr3AD8wXKtW_1yciU1PkreMKeZy6Qr0Ka8X3eFtHcmM6JQ1yOiiCYbNYHvorAMVzYL1lfVlT488d5rSjj4M_7SWPlCYYvlyasWpEwiXhibKRczloAfwb054AWWy5-vlBzs4zrJ3Rv9op95rPiyIoUwjz3kI8Qu0VCUlJey87mPmdltuWPh5tvaS8VXi8mKY5Etao8lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=QJYaXC6kWv6UAtlL5YEwZ-RG2W79Ax4hnUFrpUz9ncz7CeuuqCFf2-H6kKdtgcmCtN1CXy8oG7fIbfMzgC1Uo5FoZ2OhbqbVJP7AW0k2OjmyAFAyhbjUsnvuIJBbEjHGmb0p5YqwV1niuhAgMfUxBqSYnb0x9RSNiUo0s7Z90cxfvZoT93_jtTJhlv9h7W_1Fbqyb1OlFx2n5Lih3MmYw_3D_NTeYD2pF8bTnczTOwwBm8-HktWw23jB3tETFushazabG3b20DSo1gIRr8EhXUSNUDY_M_TTIdt842kZPmuL1IDuKhPK7mOfN9nn773Ao6UsnaAfeZke2doTIipoNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=QJYaXC6kWv6UAtlL5YEwZ-RG2W79Ax4hnUFrpUz9ncz7CeuuqCFf2-H6kKdtgcmCtN1CXy8oG7fIbfMzgC1Uo5FoZ2OhbqbVJP7AW0k2OjmyAFAyhbjUsnvuIJBbEjHGmb0p5YqwV1niuhAgMfUxBqSYnb0x9RSNiUo0s7Z90cxfvZoT93_jtTJhlv9h7W_1Fbqyb1OlFx2n5Lih3MmYw_3D_NTeYD2pF8bTnczTOwwBm8-HktWw23jB3tETFushazabG3b20DSo1gIRr8EhXUSNUDY_M_TTIdt842kZPmuL1IDuKhPK7mOfN9nn773Ao6UsnaAfeZke2doTIipoNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=U_NszTG3ff_9APg6bPKKIO0oQb-7-mp6h1qlsYUBDT0ojnCpBXFY586plMoH79pl93vOWrjHJ73yqmbb213MWb7lXZwdzbsLsuGmiYXyQ-eBBkcvR2tqJE2jkz7FdBBA8a-Ti0ZmsPY8KmBVc-giWJNqmYccJ0q2PjoofGHS0JhB11arEwWwJs77_bxD4QJ9WWjdh8M2S4L_Woy9WTrn7y3D37mWfgDuIU1DF52B2mX-EKiINa3nAIYiadIA2u5zoA4imRKAlCRkshiPdZAOaurAIdeo6yJFgkF1Sp4_hcos9qgFFmacAr59Jsaze7nQBJj5eYHkZcI8lskhwlca6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=U_NszTG3ff_9APg6bPKKIO0oQb-7-mp6h1qlsYUBDT0ojnCpBXFY586plMoH79pl93vOWrjHJ73yqmbb213MWb7lXZwdzbsLsuGmiYXyQ-eBBkcvR2tqJE2jkz7FdBBA8a-Ti0ZmsPY8KmBVc-giWJNqmYccJ0q2PjoofGHS0JhB11arEwWwJs77_bxD4QJ9WWjdh8M2S4L_Woy9WTrn7y3D37mWfgDuIU1DF52B2mX-EKiINa3nAIYiadIA2u5zoA4imRKAlCRkshiPdZAOaurAIdeo6yJFgkF1Sp4_hcos9qgFFmacAr59Jsaze7nQBJj5eYHkZcI8lskhwlca6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=XWky-o-Cvf4unH26Ak6tA19rOnHszgzADUhXHSGfHHZD2UMcQ1azWnG_CfT0SWsAZZiJqmEu9sBhvznKZPSI446dEX2SYCqi2F-Z9B3fySBpkt--3CmiPq81ROQ00V0cVT-o2g4LRHHebwlvM1v7jmQV2NytJk2scXLAwZNWexWJpN8fmjy8vktvwRRjUIR2eNifKfFd_7UlQwyN4zXpIrlDp8N5sLpnrVu5pW2vNINwuYcse5UHyC5giYOByoJvhgWQmWEwSmAv5Zlh_fLxjHU5BrNXCPhtWrhlh9MXsdx0bm675hOw03yHPfTckizFgqL_LZKRt9E78HgBHXXaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=XWky-o-Cvf4unH26Ak6tA19rOnHszgzADUhXHSGfHHZD2UMcQ1azWnG_CfT0SWsAZZiJqmEu9sBhvznKZPSI446dEX2SYCqi2F-Z9B3fySBpkt--3CmiPq81ROQ00V0cVT-o2g4LRHHebwlvM1v7jmQV2NytJk2scXLAwZNWexWJpN8fmjy8vktvwRRjUIR2eNifKfFd_7UlQwyN4zXpIrlDp8N5sLpnrVu5pW2vNINwuYcse5UHyC5giYOByoJvhgWQmWEwSmAv5Zlh_fLxjHU5BrNXCPhtWrhlh9MXsdx0bm675hOw03yHPfTckizFgqL_LZKRt9E78HgBHXXaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfy1NraChOj_nt4BHRIcPonkOGGeODivqds4yYU54sKfyt6JLsAS2xK3WGtICVpMOgV5m21nDOSFz6Uo7WKJxBBeZASKTqL4XmW8Qfa_xQyivdiMRrLpdcb3wslzIMOG6Ur4DuUPy14oMM39TGMy5ZKOsS0bKMK6F0hnE5ZcAxLqB2Tt1jvmSC3k_LSc4iZ76OQlrjxEuLy0aq-ZMSDtodsSQvyhOPOBUXn2GFVeLkGs97dFxRGJ_f7eRYo1Due44j0tMuR-K1LbajAlK2-SIVTLR0k302PV2WnYQBLFaLBFegrietD5lxMpFGl5Hw4lQqk6hjE2Y-bgFWqcQWgaXjeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfy1NraChOj_nt4BHRIcPonkOGGeODivqds4yYU54sKfyt6JLsAS2xK3WGtICVpMOgV5m21nDOSFz6Uo7WKJxBBeZASKTqL4XmW8Qfa_xQyivdiMRrLpdcb3wslzIMOG6Ur4DuUPy14oMM39TGMy5ZKOsS0bKMK6F0hnE5ZcAxLqB2Tt1jvmSC3k_LSc4iZ76OQlrjxEuLy0aq-ZMSDtodsSQvyhOPOBUXn2GFVeLkGs97dFxRGJ_f7eRYo1Due44j0tMuR-K1LbajAlK2-SIVTLR0k302PV2WnYQBLFaLBFegrietD5lxMpFGl5Hw4lQqk6hjE2Y-bgFWqcQWgaXjeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=HvKBZQwrakJyIVFRc1bFE0nXLCHy-42sL6vQ5BxzmHHLSmw1cLP2Hw6l6ngFSBw_QWy50LIb0n4-nE_W3Wm-_6C0WM3fXTgy0ZfEucikSXJj3RPe4Sqw326JUasAQJh0g8kFYA3ACyEwqjsgBW_Jtq3f3bFez-kBmmCnT6cHxMg3hdPPM6kRdTOnjkcqfmAFJCO8QVvCWw2GWteUyq8vt2IPnD2hirm8sE6tXctNNGqe5n68z6vhWWvUJLdBU0u3_5IfW3N7MoIVE5uT52xNgCKALEIMEOEIFvgi7rnp8uU8gl8zKAdsqunbTorx5T0vTeeosowSU-m_xg4bUa6Fkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=HvKBZQwrakJyIVFRc1bFE0nXLCHy-42sL6vQ5BxzmHHLSmw1cLP2Hw6l6ngFSBw_QWy50LIb0n4-nE_W3Wm-_6C0WM3fXTgy0ZfEucikSXJj3RPe4Sqw326JUasAQJh0g8kFYA3ACyEwqjsgBW_Jtq3f3bFez-kBmmCnT6cHxMg3hdPPM6kRdTOnjkcqfmAFJCO8QVvCWw2GWteUyq8vt2IPnD2hirm8sE6tXctNNGqe5n68z6vhWWvUJLdBU0u3_5IfW3N7MoIVE5uT52xNgCKALEIMEOEIFvgi7rnp8uU8gl8zKAdsqunbTorx5T0vTeeosowSU-m_xg4bUa6Fkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4RUVMFR45u3ENIoqNMfDFx6Ojp9nlsmcsf3sbfNaklBFnwhSn1Fg1ppq1gKUyt2p7iDjvEVcMHjwaw5WGvoigFn_ry1NN6OxzZXPkIc4VYulCTVTObYMf6ZM41App9Yaq6aYtquzIltoz5ia14MV2GPE9vpC0UxCe-iWin7XUwExZE2TMGzywucVuQAZzU1iUqDEUB9MbpHvKZqaOQyPHtCE12INCrt2NHyLbfkjl-KvCdiNeOww2h_3lEVpTr0yEHzBJMBe9xf7BQRjcCHlgblGfbdLam6ucKMkyGBrEWTIqK3BDGhe52ceJrSEC0wPtrz3ESUeLbarabzxFk1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=WL9rILCcY_OXaJyvfIuMKagjovr_8ue3JWLkUDzS2CnxQeiWBUZvr4bIVq1VCAmQe8D2AmIvxZjW85M9eM5IJz7l8YGSjVCEdfDMMU4Usq2n1Tw5cMIeieXQFz_Q6rdUxWGYXc_IinGGKYYtjOjy_pazgHVmxqOX2zcIegK5thEoNR6EKrXYWGjli7RBCSydzz7AOEWuuvyt-nDU9P9fyk1pqH8tSGHXTblczEqeroDYiCOTg91vVmOlyq3e6LLYWBVzY7Ue3aXg88vc23_mztf23z-AGoe9p2lOOKCfmGfAL0mvf0Pn8bwXyhCjPfBDC0vpcHzkvtZ_pqYK3CcfgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=WL9rILCcY_OXaJyvfIuMKagjovr_8ue3JWLkUDzS2CnxQeiWBUZvr4bIVq1VCAmQe8D2AmIvxZjW85M9eM5IJz7l8YGSjVCEdfDMMU4Usq2n1Tw5cMIeieXQFz_Q6rdUxWGYXc_IinGGKYYtjOjy_pazgHVmxqOX2zcIegK5thEoNR6EKrXYWGjli7RBCSydzz7AOEWuuvyt-nDU9P9fyk1pqH8tSGHXTblczEqeroDYiCOTg91vVmOlyq3e6LLYWBVzY7Ue3aXg88vc23_mztf23z-AGoe9p2lOOKCfmGfAL0mvf0Pn8bwXyhCjPfBDC0vpcHzkvtZ_pqYK3CcfgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=DrASmAoPCcF8HLEfvjw_N6mGZO5ilidqv6qAB5CJESltcP_w51nj10eobsVAdLYLgWhHMhuuo96KAfvDoCbucjv5ZNMxBNBPhdQmXS4ZUAQSTbR9MgMj8An2aLtxWQSy3V-2A9k3M-sMguk4vVwLyFUaYu02zY4TVoXjgIBq2C0kzy2w2tYvWy0oW7K6Bn1OtndsXBTup-HRm51hlwRqz6heaSZ9-MpgxG_Y1oH89oF1EpyMlMtWRS_hDtWMUs2bnm8ixTClGxySGpxaNUsJhnHMXH0JV_IWBewJDPlrzvbieYUqxgwUgZu9z-E81-7pHSHln7PtN2V_gaAElC5LkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=DrASmAoPCcF8HLEfvjw_N6mGZO5ilidqv6qAB5CJESltcP_w51nj10eobsVAdLYLgWhHMhuuo96KAfvDoCbucjv5ZNMxBNBPhdQmXS4ZUAQSTbR9MgMj8An2aLtxWQSy3V-2A9k3M-sMguk4vVwLyFUaYu02zY4TVoXjgIBq2C0kzy2w2tYvWy0oW7K6Bn1OtndsXBTup-HRm51hlwRqz6heaSZ9-MpgxG_Y1oH89oF1EpyMlMtWRS_hDtWMUs2bnm8ixTClGxySGpxaNUsJhnHMXH0JV_IWBewJDPlrzvbieYUqxgwUgZu9z-E81-7pHSHln7PtN2V_gaAElC5LkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=SSo0f0Xbp7l00wrVc1w_JH2HI1WTJWRfS8XgNKpnq0N8Jw8_ImIcYnamfO3Z8Ms2771kjF9StsywipTbf0gHeQ-4c2Jlb9p5q27uB5Xro87D3_SjAS6sc9Oc8sMdStL6JuI6XqD0vd6GHHCffp5ItPrqod3qMHuEtnb8d_m3pG84otU1kg6-tpaTsd53K0RfFVx3HQ2ZC6q2vp37i-0YvHJ3ATWUMt1V152NYMS0cqp5cuuq-bzQRYrV8GDvOfe2Zv__fILWOZ_yF6Ve9N3pxFsXcBqS6qoX6l10Q8DxU4zdY-3RxZL72MzhNgFcNX-xk4gjQUW726CLenHF-cKqtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=SSo0f0Xbp7l00wrVc1w_JH2HI1WTJWRfS8XgNKpnq0N8Jw8_ImIcYnamfO3Z8Ms2771kjF9StsywipTbf0gHeQ-4c2Jlb9p5q27uB5Xro87D3_SjAS6sc9Oc8sMdStL6JuI6XqD0vd6GHHCffp5ItPrqod3qMHuEtnb8d_m3pG84otU1kg6-tpaTsd53K0RfFVx3HQ2ZC6q2vp37i-0YvHJ3ATWUMt1V152NYMS0cqp5cuuq-bzQRYrV8GDvOfe2Zv__fILWOZ_yF6Ve9N3pxFsXcBqS6qoX6l10Q8DxU4zdY-3RxZL72MzhNgFcNX-xk4gjQUW726CLenHF-cKqtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=usiT1kHJmz0Rknipg5cu7djaauazoB9J8NqzQN8vUktZftIszfrtP5d7Vqvx3-GVR-IFGO1jQeFSUUKelPw1lW0EdmrfZ4h5fZHV1BGpb03xNFQBxQF0ptQXuass0dyScU9HMugwvSrdHBoai6DG727YPMRBqQzHFZ357Ot8yiKsCy1JVWx-0EFefv6Y4yKyfT_HNOU31y-hwVALovBQHrcETLNSdfzr8Gag9tzhb51UoKglx2X-NRYf_fD6lF-1Wtl7DvYaSzbogqF6z2q5eDkaYGRGvVcc6Sm0rK7Erf0FSsWLc9mh7rBWWP9WGRKsnkei7Wdc5KxDCnt2bhgYVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=usiT1kHJmz0Rknipg5cu7djaauazoB9J8NqzQN8vUktZftIszfrtP5d7Vqvx3-GVR-IFGO1jQeFSUUKelPw1lW0EdmrfZ4h5fZHV1BGpb03xNFQBxQF0ptQXuass0dyScU9HMugwvSrdHBoai6DG727YPMRBqQzHFZ357Ot8yiKsCy1JVWx-0EFefv6Y4yKyfT_HNOU31y-hwVALovBQHrcETLNSdfzr8Gag9tzhb51UoKglx2X-NRYf_fD6lF-1Wtl7DvYaSzbogqF6z2q5eDkaYGRGvVcc6Sm0rK7Erf0FSsWLc9mh7rBWWP9WGRKsnkei7Wdc5KxDCnt2bhgYVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=SYaXG6WmNAF-8FKZmnA3DJOm57v2CoIqNg-oXyJnd44WhcCA_-mGR_Z5Bjd630SvRXnnXYmYU7tKh4jn5ldW9xzRv6tXKW5fHgKKhRN3LZQ5m03AT7kpTrszE4r3LTp_fqr0YxzG3WZOBb-oC8gQJ8GRAQyuaK81aUAI4GmFv8t6RXuN7OHh-0ERySwm-QzxAlI-55H9vH403XTvAgNEBNXtTgEaPmSir-1w0CrM2ENEn2HJxRUfEScu572NqtcEBbR6FLBjMeDQ7c3SkyDxNrCSnJcpI_4OPY-MqEXraYZL_1ADzEYDmZ5wB2w6sHGfOAnfSgbaMmIJ-pNWBmTYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=SYaXG6WmNAF-8FKZmnA3DJOm57v2CoIqNg-oXyJnd44WhcCA_-mGR_Z5Bjd630SvRXnnXYmYU7tKh4jn5ldW9xzRv6tXKW5fHgKKhRN3LZQ5m03AT7kpTrszE4r3LTp_fqr0YxzG3WZOBb-oC8gQJ8GRAQyuaK81aUAI4GmFv8t6RXuN7OHh-0ERySwm-QzxAlI-55H9vH403XTvAgNEBNXtTgEaPmSir-1w0CrM2ENEn2HJxRUfEScu572NqtcEBbR6FLBjMeDQ7c3SkyDxNrCSnJcpI_4OPY-MqEXraYZL_1ADzEYDmZ5wB2w6sHGfOAnfSgbaMmIJ-pNWBmTYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6UeezFl-GCAEB5nPaFmpPNVQ7y8iRQLOI2FyKTdDm81UDSa0TvZSmZqSG6RmshNzCenHc9NlIXtSTvKkmXZDEXbSUGdPIxpsCQmmlZYNyR2AjXLQC7Xup_7mqAxxakqKyfAHfCcVhopMAuYT5ZvL8-ELEpgmjMaYUxx-CJZ3BMJD-bVU37pYXR2gvhPLCMcwo5w6ZOuaiihYhBDGMXTvnC6G2avnJRR7Dl23qvfFVGdCDweLzs4hNm_cObEBos39E2jSAGhDf97riMYFIXmigC9pzoDiSJzjKqk_CVtMrBnyyObdrMgonazkN4Fcy2eGS-bP_Rf_w6MAH8l9ClbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cefXF-fbxtp5crj_ubWQHoHBR7Wj0zfzEQ4n9GFMLP345IWBZJf54aVYw5F2FOSCrjC3pNZgC5cVUrGr9yyDil-FpcwDe0c-SfoEaTi223F6x8YVXy4umqSmipVXzsRzQbE37gbeI-NGSSuuG68QtnDLo7s08JfdHnnLXcbFzgr5ErkJP9PLSxgBvuzyNNLE-HbiMhXyo0JqDFLWU1OJHDvjZCMcNXNMrdFyG_JMAuQsR9p4qgKuLupWxuk-eRNw3AcNh2mmM55Ks598f2iKBuX72QuCPrIOSPHwMl2tLXC4y6obWHTllKaWUJw-dyUv4tJlwvazPta1FmNis_mgLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ldmIrap8ngIdMqB11skyeI9xTOKHD1bQodBbqG4GsFJn73qCMQFE1Sqgnb5Lcc3_pkZEhgCp7BVVxmnfX7nyk7LwATvEyt6ylM7D4AfcjWCnaUS5AQDH5P1feii6ZdhEAVJGB2sSK621yVeH4o8H-ZdhK9Hc5AnnBEAp3Q6j8wSdNC8qEmo2ZeINx06D4Y8-bdZK8Jxz3eGdZNL6GlvPw4JvI98BGQlUJ6898D2Z7nfcOwBk0ZGCxeF9wdzJ4PhJXSPAgtMZagC8mkL_TbmV4xEwrsdkQaGufRrcoERc-raL9yzeN4n02AqyXvDJuYkfeli0bMG9TgKDf4RkN1BxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=UNpgDMfeeOWy1kkvy_yaDrxBxFfxK4AcIhfCzgNIsXBIyuv-uaC7HKPkLKCYXopR7X4nz82fqqOlv6KEPiQR_1hUvD7r8cmuZQWASNFHSmxZARjc-Kh9Q8SqMFl7lyeRcyhyzMYgA_Syuq72Z0ru2jFLSMV656iFWNem9WRzaBInqkWJY_m--CQ-YkMzCGRdH6or5uM9RierskyMrrWKieTKWqNv93DDEZPSfMv5IF6H1V0KzHv9LpCeH5LiBHkaEuYdx3HvDSEyltNNnV-q-c6UCSrXml2gcr6NBwZv7cmJ5ua_y8baF7gFw8XBpNaO7gXe4GH-rlGsGcYracj4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=UNpgDMfeeOWy1kkvy_yaDrxBxFfxK4AcIhfCzgNIsXBIyuv-uaC7HKPkLKCYXopR7X4nz82fqqOlv6KEPiQR_1hUvD7r8cmuZQWASNFHSmxZARjc-Kh9Q8SqMFl7lyeRcyhyzMYgA_Syuq72Z0ru2jFLSMV656iFWNem9WRzaBInqkWJY_m--CQ-YkMzCGRdH6or5uM9RierskyMrrWKieTKWqNv93DDEZPSfMv5IF6H1V0KzHv9LpCeH5LiBHkaEuYdx3HvDSEyltNNnV-q-c6UCSrXml2gcr6NBwZv7cmJ5ua_y8baF7gFw8XBpNaO7gXe4GH-rlGsGcYracj4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COGEuK6x-Z4XAmXYDjPFxNsurt9WhS5iHxc3YP_3q_HzC-X60r1ASdKi5Bljx127n7s2rbB-v_Kr9-Dw5PD-MbMJo_xOPtzJ9Lah6Vevh8WXKRKmhtQiUYWZ61udD8UT2ps1XaWnFB7l7gQZmt2THVaMzBX9F3ok5pklgH_Lp7BfHWlgXKXldPPRO2OSo2K74h0YSOstuk40vdxrt9o7MjcUBFVteVp9Be4wwuCglTiVsMRZsM5z7Jq96nSaz0HeDZ1DKZ3Ne1OrAaocCbD0XLHPU6cM5Kq1Xhj47-2jUdMOfJAjQWIaB8HBLE61Lk5oleedHPuVa3r_q5IJ-5uQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=VvmNnU50Hj5uiDUg5bXVU032N0cFwVClasOuUpcSOXd_pF2fJKJ3qhmr3kzTp_WlaRUl_jTd09Z2wZn7uU__icEuDdz_bDpRZnE09bGTUZKouNKy-R-NRhZnX7bqjWTAcRqVFtxJO71T8HL5nZM_Jps_gLMboRC_GQZ1wWfHIcywDJdcOLKEc-_kl8ST3xrmovcgJF9PT2_d_4Lpwvsm1yZQN3K-l9Ul5bwkrN-GDUomJ3_TmNvnTb3DnRUlrWT5ld6-b6UmYjJV-L2t423eOzX-mikSOFcqtVmKC_yzP7BzELwKOUKOK1pWzccgGD2tSe1Jl0uNNMXTRUo7uLcGi5wU-W3o7IwqFpww-tsWg_SVBXaQLjhnJuKZx5EIBUIo0XH-wC4gE1IY7f0BxqGaw3q4k-yjC_BxERHlEsT_3EBYk_9vQqnoGhfDpbgHdPX_IbbF2oj_UHofhPAsZik3boyi8nbDIs_se3yrFHVHY5x0OYg_o0Ou0nnD261Q_cdK9NRzEU14oQQ8ve4ktpd8JOgUGfDwr0w_PfKEDnlr5N-3UKZ8GzbiaC1DiIW_x90zyMGS789k8AspBfdgEnHyVDn0-GJbRSeWIAA8Z08WlHiSF87zrEKOnNDFfEGTfQ_lCkdyJC3niZ8ZpmmEAOR8cUHcDNYSvUTqAjx2jsJxSYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=VvmNnU50Hj5uiDUg5bXVU032N0cFwVClasOuUpcSOXd_pF2fJKJ3qhmr3kzTp_WlaRUl_jTd09Z2wZn7uU__icEuDdz_bDpRZnE09bGTUZKouNKy-R-NRhZnX7bqjWTAcRqVFtxJO71T8HL5nZM_Jps_gLMboRC_GQZ1wWfHIcywDJdcOLKEc-_kl8ST3xrmovcgJF9PT2_d_4Lpwvsm1yZQN3K-l9Ul5bwkrN-GDUomJ3_TmNvnTb3DnRUlrWT5ld6-b6UmYjJV-L2t423eOzX-mikSOFcqtVmKC_yzP7BzELwKOUKOK1pWzccgGD2tSe1Jl0uNNMXTRUo7uLcGi5wU-W3o7IwqFpww-tsWg_SVBXaQLjhnJuKZx5EIBUIo0XH-wC4gE1IY7f0BxqGaw3q4k-yjC_BxERHlEsT_3EBYk_9vQqnoGhfDpbgHdPX_IbbF2oj_UHofhPAsZik3boyi8nbDIs_se3yrFHVHY5x0OYg_o0Ou0nnD261Q_cdK9NRzEU14oQQ8ve4ktpd8JOgUGfDwr0w_PfKEDnlr5N-3UKZ8GzbiaC1DiIW_x90zyMGS789k8AspBfdgEnHyVDn0-GJbRSeWIAA8Z08WlHiSF87zrEKOnNDFfEGTfQ_lCkdyJC3niZ8ZpmmEAOR8cUHcDNYSvUTqAjx2jsJxSYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGjc33OSveOsCiyvZsN6S-mfzwqyP7QXGAIQQ48RY2vvNqc4EbmsaScOdgatZ1A7hbW7ro1pisdKbjto0B_CqlWbFJOqsXsyi_lZBKxOiQ40B0elahY6UkgxC9nAQID2kYhIiAd3ZEnZlUWo-bF6cBvlbWFByZg_DpARtTBCesZYLUnvNOV3znbo-eaJdFoGvqfBwzkaSsy_5nmjhq4EGtuNA5Zoa4fdT8sqsaMYNFe4Jv_IxuXJl8gFd4nQUTpFvob4gtWqDqAqcXEa0Crdfqp8zTGou5yrVBM9ulSpX0Wpz5VQ6FAb_igm20negeRd58CRtCwOiVZDJjxRGwL6Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBhI-MLqGTnJc1K-JVm-BEI8H2mgseEwZ8URT6yaC0bRRDF0KaTnY-WbTO3PwzYdZF_peEs4BLJLiOgVAGZYjEbxD0GV-1cH9wTZhPxKXbW-nFSl12NMgvGWZWQtnhTHr6bDciV49ka5-6DRh7P-DZD9PdJj5zTueg8wVbwKzXnacPEbs_zc9qf0ZcpCA0ocEdtnFFbiMx0ipH-5Tr7VXCl8ZAYwItjkLp6sLbSh8woOl7XSAK7USsHHYMyWNQfHSsr7DDj5z2La4ETd98YTUKgtXub9tzgW0GuB2xh9pO_FfZXoHJVNKVgbF8vuS4sCG5ryV8ttdtt9J_8cAgKhxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=DWshEN9bTM4bySK9ssgfZsdZPmoRB6SiggoNU4C5vjjlzbxDjRDP3WLmc4rfEuz2nZnRIQaTbyDWV3sbO-93_GkXvHSRjLAzJzJEaqjjF83cfcECWJ8kX47mSD1oEmgjXHdj3wFPPrn4ipx8kdpgsf0s-3yZUXfu_o0qt7saHfo6Qbv5IC65Otc_z4pHfFsN3_DnN6w2lJIy7RhARtjxwEjYdRj88J2CTLoHlpdA-RmljZ-rnbawTN9cioVh86x3U7dH95yveILLjFFnu1smY71NZt-G_6yr6d9iPAfVsmxRg7fdkq1r8rzqrnpqvXZwZllMmn5WDLOVd0MNU6-cPbszXCk_yeTcfVcC7pxtQXIkQWOPSaotBNVpVDn1Oe7Af-0M9njRj4X9W91dc5f5avPpAB8oB2E6JL0jm3GuleMvTKninP3J9gQh38AANYEUJJ5x9UZprqaLkCzXTvsQ2sI0RiTn6F10xgiySRz7coq4BaLLpr68Zrfhmzjfy1Roi_cy2lCexpA3KpkOQ2y6Pp7gwuL0kJNOe_r4Mqge46c1ppjRNIYlXek550-88F82EPABHG0EX0FL16Rhmf9XU8Zj-WynQtAeJle2p6W-FSLH1YzEskW2hQF-KMXEHlD5XpKds0czCYSVJKYw8pz6VIe4X-j7bf4uJf_dZpxzW8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=DWshEN9bTM4bySK9ssgfZsdZPmoRB6SiggoNU4C5vjjlzbxDjRDP3WLmc4rfEuz2nZnRIQaTbyDWV3sbO-93_GkXvHSRjLAzJzJEaqjjF83cfcECWJ8kX47mSD1oEmgjXHdj3wFPPrn4ipx8kdpgsf0s-3yZUXfu_o0qt7saHfo6Qbv5IC65Otc_z4pHfFsN3_DnN6w2lJIy7RhARtjxwEjYdRj88J2CTLoHlpdA-RmljZ-rnbawTN9cioVh86x3U7dH95yveILLjFFnu1smY71NZt-G_6yr6d9iPAfVsmxRg7fdkq1r8rzqrnpqvXZwZllMmn5WDLOVd0MNU6-cPbszXCk_yeTcfVcC7pxtQXIkQWOPSaotBNVpVDn1Oe7Af-0M9njRj4X9W91dc5f5avPpAB8oB2E6JL0jm3GuleMvTKninP3J9gQh38AANYEUJJ5x9UZprqaLkCzXTvsQ2sI0RiTn6F10xgiySRz7coq4BaLLpr68Zrfhmzjfy1Roi_cy2lCexpA3KpkOQ2y6Pp7gwuL0kJNOe_r4Mqge46c1ppjRNIYlXek550-88F82EPABHG0EX0FL16Rhmf9XU8Zj-WynQtAeJle2p6W-FSLH1YzEskW2hQF-KMXEHlD5XpKds0czCYSVJKYw8pz6VIe4X-j7bf4uJf_dZpxzW8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQiIf-q4wnu5SuMfVLEmsWRwIjfLhi4-wkuJ8KuAeYpXewT7EwXY4BViIVvANN07gtiF-8_KKcC0BKQcLPl-VjBvb7Nggq1LO693eK6rCF3l9woEBGQYsLeN7VxyUk55h6C2re-qxo2WDwfY-Y9FgD2lUwVbTQSkwXIkOGElASYORwEtpRBr4_H6EbWB4ZQpDiY7cOO3PwlFNF4KwNEYQS4-XQpIlqLZFFXoN5XnXhMDDKuWkib-eE4Dat1-vKrk5HcWXj02yK3WT_RbPngnOvQjjL5TjYOErAyBcsDtvhlWEfKD_H2M1xLGKJzZ7hIID3RkOHyHAcPouHnKq7v8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=rOwJBSZTq2AeNJ8qW1WJkUwC6wTASKw5GfGfMsdH_MyyJ990asU-e_vurNK3TlGP_VawCf-qtNwhQ44J9R3C536Wkq5KzqwUnxUaSRd24pOVqBd-OWZCYAp2Q4WHnonUJUrLbR-2pkKb2-fTKH3P6tB2IT7bMkNea8Sz8A1KhtjNtBy4pAY-wMHp8BOFWYCXMw4z73CZZisM8JOgQ36VV3pp3gCU-_sAgdUgG7kPIVHhh1JBpHC_sjeoYgdKacYBTe-gEl4VQnKuWurY0R_e6C4yerfBm0-3u6paeNCKUQZTxuGPgQr5JA5XtVPi3R9mxrqoTxuo39cM_PWqAamcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=rOwJBSZTq2AeNJ8qW1WJkUwC6wTASKw5GfGfMsdH_MyyJ990asU-e_vurNK3TlGP_VawCf-qtNwhQ44J9R3C536Wkq5KzqwUnxUaSRd24pOVqBd-OWZCYAp2Q4WHnonUJUrLbR-2pkKb2-fTKH3P6tB2IT7bMkNea8Sz8A1KhtjNtBy4pAY-wMHp8BOFWYCXMw4z73CZZisM8JOgQ36VV3pp3gCU-_sAgdUgG7kPIVHhh1JBpHC_sjeoYgdKacYBTe-gEl4VQnKuWurY0R_e6C4yerfBm0-3u6paeNCKUQZTxuGPgQr5JA5XtVPi3R9mxrqoTxuo39cM_PWqAamcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH2qhbrsLa1tqBSe9aYnjRYtFyqEjs21-xVxadMauFrHREpNQ0IfDADuC-_XY2SnCWw4w-uH2v9uzi0Uf0hG8L2lldmB4z11XPCYdg2SqsFC2j5XAnZX3fHmJOrU5Ph9ZlnrPy2-lSz5TDlCXuCJPEaAPUb5Sgex8zuyO26sHH3U-qxoTtMLpNBgQS9lwd8n67W7dmO_vrsI5p3HgrV7nptraAnnickXEKGWct0W6gsZ5wYxeYRMsmjwVc-1LiC1d86877NShl7Yy2eO3ChVweQO_HSEYm7qQgnTw5P8dx1kUefbQFMBjMVbHnVAQ4BySvG9eLu1LD38S4hwY7Y2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q038DY8KgvCPc82YfXOfk8bdPk4LwEiQwJQ3jrG8C_3T-BOo0ixe6afQrBNrnm6eMXh-PAsn8xAb0EZ9c7cw9AbonalxDN9dZCbFA3wNywnYwYY2YRhu0BUlP2RwBjZ8SWIvns0YIaUrK9syfOZOpIWcL1MqnaKlUcvabMaKvvngJncLXbfVNPlj8oeYrZgAx86k51mgJtC9Zwwu09VIOAyQaSXzAq8aYcjHhcB4GrVd0RcRAT6lmgoUqEcXXCNg8y840404WTEPcWxRHHgCgK2XELk1Qg3hEy5RhB0qsSe4dfmDIuHq0TATbcb9lkWpx6z5u8ZZ2dZX16Zsea1JLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=pBxujmV8qh6j6qMn8GLjsuxWS2u4fWgp1U9Fzopd4u2lxdSjC5KOWLzU-v-pX2EPdHniMyGISD38rq97K-_f_6dQbjqgH3pyGQS14XxoHB_nV-3JKpx3b0q6jeUPQwax9em7gx2wwbygEc_lZUyzOdkSB5DX7wyqMfYSUZnm6bUkCeRKoBccZ_1f6iN_JdyvONDZBtEZ6D9fNFvVUSrgndnxrCSa8shkADS91T9mw2KeQDec6F3V_I6IIKJcJXSsxbcf32ZJXfLeLVSfb8XIzKGBt7euaXd2aMQPve3JuhvYG1xUXKYXsVhq6nRimj_VnnJL10_f2VkvohoKUK8f9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=pBxujmV8qh6j6qMn8GLjsuxWS2u4fWgp1U9Fzopd4u2lxdSjC5KOWLzU-v-pX2EPdHniMyGISD38rq97K-_f_6dQbjqgH3pyGQS14XxoHB_nV-3JKpx3b0q6jeUPQwax9em7gx2wwbygEc_lZUyzOdkSB5DX7wyqMfYSUZnm6bUkCeRKoBccZ_1f6iN_JdyvONDZBtEZ6D9fNFvVUSrgndnxrCSa8shkADS91T9mw2KeQDec6F3V_I6IIKJcJXSsxbcf32ZJXfLeLVSfb8XIzKGBt7euaXd2aMQPve3JuhvYG1xUXKYXsVhq6nRimj_VnnJL10_f2VkvohoKUK8f9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=cHYJr-nVH0jCbZvu8h1kcuSa_DCtimGtBF9W_cVCV_eMxJkDpB6CGO8IQR8lbeDL0oXCmomwoeCJtOiE8GzXhMQ2QZ7wDvY1Uvm_EQa-H7PoHbfnjsEa39ZmSyND9ButrHaVOQeH9dh8g-iU0EXOKzvTC71b1iVCFTwsScCqqphClvT_3VKrtoX2x4Ab49XuZFBGewthc4JWOwyGFR7rYOuq5PHFuC0qT0e4GThJcsoOPqKqKFCRJQKH1vrVMR-4Mhsz7hrs34yXR7wGH4rAzXoG6GKpnYwLa2r_eLF0ioFzFbXGoxbL2o8jJPeC0ok-rSXQ5oNgXnycyAKdLAGoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=cHYJr-nVH0jCbZvu8h1kcuSa_DCtimGtBF9W_cVCV_eMxJkDpB6CGO8IQR8lbeDL0oXCmomwoeCJtOiE8GzXhMQ2QZ7wDvY1Uvm_EQa-H7PoHbfnjsEa39ZmSyND9ButrHaVOQeH9dh8g-iU0EXOKzvTC71b1iVCFTwsScCqqphClvT_3VKrtoX2x4Ab49XuZFBGewthc4JWOwyGFR7rYOuq5PHFuC0qT0e4GThJcsoOPqKqKFCRJQKH1vrVMR-4Mhsz7hrs34yXR7wGH4rAzXoG6GKpnYwLa2r_eLF0ioFzFbXGoxbL2o8jJPeC0ok-rSXQ5oNgXnycyAKdLAGoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=HW3q6SLyW3ZjLwOBaQ28K8mfGLo6X8bCJaZuMnZtGXA4cc7RJIS1eX9kIi-qbrcsRjh1wYK8zV5Y5P8ZwAoA09CqYadrl8wwxGAbdBFYJePzRM0XL-fWfOUTRiJnZpzjDIc5hU9APb0ZWZnoOQns2SDpN9Ej1WrAOXqe0aMgSUgJLF4BpYqXkhG5_75w3RwGIVzsSvl-FVqunxKYmw9AlAeC3FrBcNZjSHBE_tT7SGHkwDXIzQQhG_Qd-OIAVJUH17iZ3d1_eMEwDnCeOHYQWy_FyKXIpIrVILPncPLL8UtkKEkZjSdhV6aSSfHMaB_4fgtfTbtJcmFmJk4gDlVYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=HW3q6SLyW3ZjLwOBaQ28K8mfGLo6X8bCJaZuMnZtGXA4cc7RJIS1eX9kIi-qbrcsRjh1wYK8zV5Y5P8ZwAoA09CqYadrl8wwxGAbdBFYJePzRM0XL-fWfOUTRiJnZpzjDIc5hU9APb0ZWZnoOQns2SDpN9Ej1WrAOXqe0aMgSUgJLF4BpYqXkhG5_75w3RwGIVzsSvl-FVqunxKYmw9AlAeC3FrBcNZjSHBE_tT7SGHkwDXIzQQhG_Qd-OIAVJUH17iZ3d1_eMEwDnCeOHYQWy_FyKXIpIrVILPncPLL8UtkKEkZjSdhV6aSSfHMaB_4fgtfTbtJcmFmJk4gDlVYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwpKfxCLHZF84IVUvTh-VxIrCXVOqe7wdrJl0vJhW8k59TQKVV-bsppjRcEnJWDy_tSgXvZ4ylw3sRX0n8VCy4dY9_3BgaaKfcotah7u5tq13ajskFB15MfT85rwnSMN28cHoC3tzdFgxlz5B4jbiOgtgDnvEQVHQTsYPYgeiKTIHIBoG_YNM10XGZE_PuvaiQUUhVcp80AvfHtERytaQTD8reqSUv_ThG9OyKnCFOM70T8UGoDeDor0ja3Ajm8RKcOKCSBzxquLGuTetZpCiFkl3CLceY5VSV4h4DoIqskEpF3cleJDm78TXjqTlT6zz1lMQCOG3ynRAaT1oyk5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=hlK_Ssbj-ahJzO_PBB8zB7obhlvzlgqZlu4Qtt9UC4fZ3HKI5BTh_3wjzHjQn0OPIm72K3zGTsOYQ86IgaUZ-KGUCMJlD6bsikn7paopLD7qCFarMHCfNiCCM7Q-mMNTSozxiVQxlyS5FE6agu3PWHCl_wgoEumVTuaodmiuBSUStPTpxUCc5Bsil-hD8VikRylWV7W4_6AekevpEuuEpKJDmvqkaAFStHimUCCrvMyCp4hm1Fd5k7tb6i0pszo1fzUAfAYLtHaicBWxicbBz55gwYw492_E55Kat1o-F9CnrxoPKRjPkOxzCkE3RcQ6HvmegX5k0I4k17ksL4gKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=hlK_Ssbj-ahJzO_PBB8zB7obhlvzlgqZlu4Qtt9UC4fZ3HKI5BTh_3wjzHjQn0OPIm72K3zGTsOYQ86IgaUZ-KGUCMJlD6bsikn7paopLD7qCFarMHCfNiCCM7Q-mMNTSozxiVQxlyS5FE6agu3PWHCl_wgoEumVTuaodmiuBSUStPTpxUCc5Bsil-hD8VikRylWV7W4_6AekevpEuuEpKJDmvqkaAFStHimUCCrvMyCp4hm1Fd5k7tb6i0pszo1fzUAfAYLtHaicBWxicbBz55gwYw492_E55Kat1o-F9CnrxoPKRjPkOxzCkE3RcQ6HvmegX5k0I4k17ksL4gKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Kee9uh87VbKV7eWzpUrGDb5Hl7AO969_K-AIncTGdSFsYvG0Shhzg7LayttT3rVYIPdIDPnudDWib16jvUFv1uriV7O372TUA0VEplpGYKT_h22rdssFmXzhpWIPTvS8sTuGPxFvMhsI1sjctSeVq1QOu1H690bR_6t8HMs1qeF24zDSofc3HOEf7N9MXlH9ZZnitrPcUGBPfNIdiyQ94vOJwy9ytcYFyHCu8lAKCLyoLhZBDOZ6VCLTTixfYHhhRxzlhGxQiNkPT8rk6K70_ojQtziX9YL3oFIEOV4NjT9kT_4gZCOBGHtXTJ1CStxFq98nmzas6V2Bou1AxN_CEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Kee9uh87VbKV7eWzpUrGDb5Hl7AO969_K-AIncTGdSFsYvG0Shhzg7LayttT3rVYIPdIDPnudDWib16jvUFv1uriV7O372TUA0VEplpGYKT_h22rdssFmXzhpWIPTvS8sTuGPxFvMhsI1sjctSeVq1QOu1H690bR_6t8HMs1qeF24zDSofc3HOEf7N9MXlH9ZZnitrPcUGBPfNIdiyQ94vOJwy9ytcYFyHCu8lAKCLyoLhZBDOZ6VCLTTixfYHhhRxzlhGxQiNkPT8rk6K70_ojQtziX9YL3oFIEOV4NjT9kT_4gZCOBGHtXTJ1CStxFq98nmzas6V2Bou1AxN_CEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdxLPgK_n_h7Kwq5LX_4PT-_PiIWCdO-jdWopVhrMVRXQR-9ZxaSDl-ZWuJqt6AdvEnlhzJUFiI3HlH6_abcf983MO9DtBI5K-pal310jk2oM4zPUzLW6IJqVygeoDZx826iOe2iAWwDrTPojgTW8VEQ5f-GYXKCvEB8l-F8B8HShse3PpU_V2Pc_6ggTzFs8YvnbDMaSZAva2Z5qgRVaRmQZKd1qYdY62iQFXOTyQyQm4nETzGV2RHJwtIIW_Aer8KnA5C8j0vVLON8JM2zyecnaSZ2G1ZybZTV4KM66bFMn0JwQg5J-qcbe2VDE-JOyOX7bAq2l9_OqBYI0s1rCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=RnQ4Hle2TZGNBur_vTVx2n6uJRI5ayELlVT6WYSNIW7t5-nzu3XfuG4kZAa0_RIpCiossN1vSNEiZee1PCymjjuDeOLhpoZFRkK7uHMC3vomuBKNDeIKcJxgOnao9mkmwAFvZJiKB88a0UjuYzbIh8wqNCUxdB9PhrA4GU46QIlsEQkw7xe75D6I1dIxO4f3hLFCoLJ4sDkc2zzPTestqhflUAjxe9VLIBY0MHgR7jKhJ9ohgInP5XmNTgaGp4CsBTmKUVP6_LbESQtnOaimMaWxzhUIgoWM0OVp18lGNRXauiXxgRZeuMSQhx5U-nWIJzMgJgD_RyewUzftPNlqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=RnQ4Hle2TZGNBur_vTVx2n6uJRI5ayELlVT6WYSNIW7t5-nzu3XfuG4kZAa0_RIpCiossN1vSNEiZee1PCymjjuDeOLhpoZFRkK7uHMC3vomuBKNDeIKcJxgOnao9mkmwAFvZJiKB88a0UjuYzbIh8wqNCUxdB9PhrA4GU46QIlsEQkw7xe75D6I1dIxO4f3hLFCoLJ4sDkc2zzPTestqhflUAjxe9VLIBY0MHgR7jKhJ9ohgInP5XmNTgaGp4CsBTmKUVP6_LbESQtnOaimMaWxzhUIgoWM0OVp18lGNRXauiXxgRZeuMSQhx5U-nWIJzMgJgD_RyewUzftPNlqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/saEzSVdhYGIRsoLss-iUhHwk1bSJHewgg7KSjW2TVOLNL86uzqlJ3iNtLDdhAKxAMC5c7SdKJsLSI3wOZB522_6w-ZhXYbgFq_UQWtVg3_PgDO0rxj7YSBK6ZslwPxfDMPpC0hmzhHug06BcFvm-t-y1APVsBcYVzILzgbQkCcuJTmedvlkDNRZk6TNdXL7epRWgIiYhwBKbFPqrgFAwSvRy_x9j2DmgGJHdCrP12n7eq80uBsAajaU_Jg7l_F7Q1zc-xtgWivVMsN5DFTMUlfwHd9GqQmtpN3A-EPsJmWIL6LyHLRrNEC9W2YQBmU5bvfoz2NZMyuiXgc-7K56IFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Oo9l_dEI6mXGFUTRt8_ebhgWvE86fWeghh-aYg2L4LQdK5-DgW7Le8XmT13P0tlJE9IeNCY8juFYl4PpR4wg_DVbn4zMnUifLbUDlMLQ1ZTCOb4V1s8gzpHOEcm1Ohr_FFxnnRXZ3PQeXLv-r3VEeLn0wm5VRac9ijABnUOJejfn-EL_51V550g-5WG1kq7Gac3UYwpbIZiK9abbbLVWLUtVdeADRzqoEwhY-Jh4F-bnSK9K87AZbJthTFdNbcGroEX-dBddw3UHi03ntAQ9gK-PUdfNRxM4u2r0qYVMutNb0HHMRPxdRnOkRP7dGjX6F-bxhZxovEuWo7IUpAvkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MYS9qwJCuNJQstz9X-rDWRr9LHsv827w3hfqUKaLHWMnwUVgTkBmfWhH6X2YgWxk2Ckh8nwTYDJjUT493INelT3JiIPCfqE78pFcUMwOolB9BcEd0LfO9dYFtZWhIaY2UG4ESg1LyNXEBwCmIyFza1KR1FBDiLdYXDjDQwQrIXeCWJSwwU4DLneLazw6wjeZkLwl88ZZO-h_hurlbc1ann-gSnX2ofV4DMZ8cYrg-RtOp0P3VSHJUg32okh0v0rr1F6fVCmvDDG7nyYDqzTtQpM9IAZ80gYsABrLCytbfzIxQUiFERXal7GCbpo9keFdcfqWph5P2urluU3HuWv5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/txsKahGfJjPIgtz0XupDXJYVK8nkbi_83FlEWKuGyPAxvHvkQ22KodE1ER1TEjvAflUmPPRPPVdEEAxJPsZ-ykrgaMQiKKJD5HiRUO4LLTAweakwL5SXIl8eUDhJwn3KKdl_QvT9B2_MDOY_MmFxynKZWSflaLjLhognooWnE4PAXu7e03S4zmQd5InGtoWreu9eEEx10mH9pKZEfyt5I0eDy7Xtnbk4JcQ3-nLRyfAnF9uORPsQJaqMwvGq7upndJHXCfQORgUlD88lAqsUuzEbGdDSiVnNuBDIkf_pK6l2xwko-sn-wPdX_djE6HbCxGJ5fN8Mkfigj9XgFoiasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fq48_6_xaojbfow7BZWw15oHsJx-35zFl6QbrM49eSKlPiqYMPQB6ogC0Kow91zAZBJI9tRIsta2s-pOJbvVEvdixup24cBwcfhjBoiKtQcbq2_b3ygPTdWMmJCKICzz7KPPKur8RIHCAEWUTAejSldYVPfClwiEwYgFO9szxCL1hOm5zxw-nw8SjTz8XfNSUtGU7RbZsIDy4EUBvrzy8pi4t55a0c-y5B7sWxFQkpIy3eSoKgxT0dOSBbjnKMDLnsY1VLntqVjpUu9ozdv_qoNWjXxO6Th1Qq4d1QMNNhBWrprXhi5jw_E6Ic_PMcQhi104frU2GKpJJt0wq77_gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHidly1hkKibPP1ZBGS5NkkoDjigDivWFlU8OuDvuMD2iKYLWAjOSe_HpQ9xU35RhzVg_MrLOyFwPCTSq8isV7qP_rU22kaZOL3SOpRm2KhYNxIjeuRWAYUsoExhbuysEeab6t3UBYmPvSCdDnFaEQW-1Mqw2CuC_fanzcxKdSuy4O0RMGUBUbaABDaErIDzchocrYlWHi_x0Nch3Mphdu4gCmMjFsozo8LP6h7hkL3RZVsAWbXvSqnACKa5dM3P8VsKcjOnXLIyS6rKVdp03s3QbXsMdl0cx_044FWdy3iX0xM1qS2mKA7qtEREGLcH-guDg_DqPxQDzRm2ey3Wag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QH93IAfYfo0Eb6-vpgFwJbzAke-Lf99grt4LJE7yJONbEYVWvZ1bfSlDzYRZFMuGVFE2EuajkFihM8IrTN7iwlrPXE6op6mxUlVPSTnErWM25felQQXuI2nRJG2bTwcPA4F8Ilpnpf2Hn3mejft8L-gVK4OJ8PUUq5FdnQza-jMWwIKffwqx0lqBnNosMCYhxE8G9QayDDVYXgb86gs2VEjJ_w0UehTKBWg47haeDN7m11Q6iXD1It2XI8xYu5uY9tm4YpQAZNEKjkBr6MndTbiHNlTpZpMfKI5uY9wIyzdpaqiEMMTCj7uvj8kCkG4GIktzQ3JZpDt7mgyAjXbvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESeo0NcTlnN6jR7Wo3tmTKCNP61EXsIpWZF6NjHc27B2q2QMvkvJ10aVqJVWmMiyCKbrIh1aNLMU3sxedGriHlHG90sbRsgfGMMSmLvndlqqn30-nmZBfD0CV_v5gWid7dMMh39eNEuxD_WdsYOFqnkK9inTKs68wppCoT7mXUofdUH2zugi3NfF7VIglvjbB8_y7QCVRjUycsV-iN4L_DhZBLHRzJk8vWjjolF5O2vTqJPN5uZEXhdTXgZCuseKKAgiqtulvOUxG9k7rc8kZ8PFBASCG7YnHIkSRDPLQf1SyQWAivbTJsyO_e9MK5nhnBsU6YJ9h7J4uRdboD0ijA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=a7XgVnkNnk585Qcy_jkgSLOS9izzqTeFvfQVG0Q1wvOSmhpO7gIAYPuFn1ucdJNyVCXbIj8n5vyYa47kCV4JazhxhYTh3Z6Hiq-FExqb5JoRtmkDx0ssLki7I-ejT_pbwHdEImHKvP6T0zAnKqc11K6M9K4R8H1sTZDHD0aFB16jLnuiCLZ1LDyjNFvthsWNNmDILVleLOFtzec4N4zKdOh3l_oDA3Whw0mIg88MYe9LZ-lSfQHknlDix01Ntu6eGKMrcdR6b6dopN8HFcRatTF4elel2U2k3BF0frQ-myioYEhZug5heGBSpOLpyenXD75LWXFEMPnRrqwoMC6d-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=a7XgVnkNnk585Qcy_jkgSLOS9izzqTeFvfQVG0Q1wvOSmhpO7gIAYPuFn1ucdJNyVCXbIj8n5vyYa47kCV4JazhxhYTh3Z6Hiq-FExqb5JoRtmkDx0ssLki7I-ejT_pbwHdEImHKvP6T0zAnKqc11K6M9K4R8H1sTZDHD0aFB16jLnuiCLZ1LDyjNFvthsWNNmDILVleLOFtzec4N4zKdOh3l_oDA3Whw0mIg88MYe9LZ-lSfQHknlDix01Ntu6eGKMrcdR6b6dopN8HFcRatTF4elel2U2k3BF0frQ-myioYEhZug5heGBSpOLpyenXD75LWXFEMPnRrqwoMC6d-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=QNSGNT0mIZLlV7u67nsOhnB_nmql8fRFopA4C5rIW2Q1Hp_Wc3ebRt-Id5MWudWyN2zxxe4P3GsI5hNNqve0nfFeJZMRZKv6hfQ5KuBTlZGLuc3tSarkszsgxjrukhIsGiLVIoqGlVyC4aPArECL_JthAoCuRWGYUXjZ2U_z_04MBXo88MlvanSV1OCVqCxRj-4q1GbdVYztpQNktOSeFd0_EqGHNMoPjIcHxb6Uy3YtMiNQQPYwqeDg3pyOIGm-xQDEd8KcoyNyK96kLyl1ml5qXduIlLM90A41ItZzNteSJdncrn6SSxu5ldCeLbrJ4lQnphOvTTmFVVUF16fW-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=QNSGNT0mIZLlV7u67nsOhnB_nmql8fRFopA4C5rIW2Q1Hp_Wc3ebRt-Id5MWudWyN2zxxe4P3GsI5hNNqve0nfFeJZMRZKv6hfQ5KuBTlZGLuc3tSarkszsgxjrukhIsGiLVIoqGlVyC4aPArECL_JthAoCuRWGYUXjZ2U_z_04MBXo88MlvanSV1OCVqCxRj-4q1GbdVYztpQNktOSeFd0_EqGHNMoPjIcHxb6Uy3YtMiNQQPYwqeDg3pyOIGm-xQDEd8KcoyNyK96kLyl1ml5qXduIlLM90A41ItZzNteSJdncrn6SSxu5ldCeLbrJ4lQnphOvTTmFVVUF16fW-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=FWx9hncapsvGwjK5YQfqj4DNsTWERbxtPbzUQkJHDH5qkijv2aZuTWrmDlEu60XlPI4Eju63o30dEWzJLURhmi4aeUZPWAamlkO8dJ1G7TFOoW1sHPbGGSW8sKTQt6YauPkQDzjfpoBLeqrefjib73d1Wnm0vDgraTN8emDPQed5mfjWPOLWP-5uROG_nnlz05PKa1Br98ychMy3amBVS0QxG0zKos7Rv30_8QkWTJjKmYV43ydWBI8yf43gEyRfIlwhdFeS0Jo1j9EHwZsj7UZkXjPlEOXEZjb7ouOszp9p9_stdJL4dm4X266p7c1JFKke-Es2RqnQWVmaSCEseg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=FWx9hncapsvGwjK5YQfqj4DNsTWERbxtPbzUQkJHDH5qkijv2aZuTWrmDlEu60XlPI4Eju63o30dEWzJLURhmi4aeUZPWAamlkO8dJ1G7TFOoW1sHPbGGSW8sKTQt6YauPkQDzjfpoBLeqrefjib73d1Wnm0vDgraTN8emDPQed5mfjWPOLWP-5uROG_nnlz05PKa1Br98ychMy3amBVS0QxG0zKos7Rv30_8QkWTJjKmYV43ydWBI8yf43gEyRfIlwhdFeS0Jo1j9EHwZsj7UZkXjPlEOXEZjb7ouOszp9p9_stdJL4dm4X266p7c1JFKke-Es2RqnQWVmaSCEseg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=b4qtOTh5wr55zxL8cvt2lI91alOvLxjtn2ASeyKQL9qfXpg0sdyh9iFn8pWmZE41Y8bOzOd-R3D9b7UlW9KCOpwEHJG-DOJNKISSfmkYq00r1GN-Wi6bBEdBVGHBs4kfJVd7AdZ1YBd7mvs3gMP97oLt0KEodWYcrjIgpzOApWC0tN-Jn9pCX1vXWjXJsEhpLNcYokL6QlSBeF-UUNtTgPOM-Z0s8_cUd8wJbpxkO7ek5LcB87I_0iD3YBWWOtq1bcIZ43QUSOW6WyeauUnaG3V2BBoHs69MmU7xx-i_CV5_eYPCyUV6Ffa3Xv6DRhX6oQMeqMLQYeOXbe5or6NR1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=b4qtOTh5wr55zxL8cvt2lI91alOvLxjtn2ASeyKQL9qfXpg0sdyh9iFn8pWmZE41Y8bOzOd-R3D9b7UlW9KCOpwEHJG-DOJNKISSfmkYq00r1GN-Wi6bBEdBVGHBs4kfJVd7AdZ1YBd7mvs3gMP97oLt0KEodWYcrjIgpzOApWC0tN-Jn9pCX1vXWjXJsEhpLNcYokL6QlSBeF-UUNtTgPOM-Z0s8_cUd8wJbpxkO7ek5LcB87I_0iD3YBWWOtq1bcIZ43QUSOW6WyeauUnaG3V2BBoHs69MmU7xx-i_CV5_eYPCyUV6Ffa3Xv6DRhX6oQMeqMLQYeOXbe5or6NR1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5cXsy9zoJy3_H0FkGgnjadwUIBy3TW6oW1KowjCSIuNQZuLKkLTmIFYfGKpLGgIxFCV6js53-a6L8Sbbe0JT2y5wxMsaO0HWhoTs5K7iV1w9CudtBO6qY-XvYQ96qnAfPjVaAfDLBHsmPyLRwrQCfwqwr1X_05eNY6Ez_hGixWWUDSNfavoJh5z-UisJPFXXpfSg7rrrOyTd9Zxi_DOet5hCS3C2H1z519OuVla6k20EI0l19KQinQ-ly3m77H7tqNWn8IdA3-g6xkM8bNoHj0Z4QYnN5_vnbTIWZE_lyWAW8OLaB39ifzgFyP1n2SwoyBiD0kRhaAkffWqQzTtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=lVPDD5FCk7Mnk4dkgEa6AOUm8XN9y237N7ysH6RhOQiXHel7_jzswE0PgH2cSif0S1nw-Fxz3Q-chQhA_hpVLRwxs7bLA8tKdAaTjdvJRL6ehkR-F7_hCIM2JriQQpc46Ey9of2fnR2oWazFKr5p4PjqLQ_HUbssjBHUJBQH7mgOMiMFATk_HDNQEMJx-6FidROcvpgNa8lF5ngxgMJXm8bTj4zWfn_8sr0lboFra0mNJmcJ2TtcupsapLxEl1Rn3dpOQ9tSc3tYBYA4FztE2eYmmf2yEqNpJ_f9HN_8cPkeWVgq5Zptqo7bf565SmscnKjFn53ucBm2KIS9NW7xaZ-bXKKWlaaue6LRGg6II7sWYZhw0j3gUvuvjjm6ab6mIiXKtzGRAJ8rpmyFqQJ7BE9cEATQS2jghmxAtCebyHTauu83S8tbnF_iCotz4MBqLsnuLFEqrNs-AeUYJjj4MV3cYIlHPTUbDU1usbcz9Mdq6kpe7rif30MWSOd8Ks65l8KRFi3XgkuS3H4v_Axo2JSBM90nWm_7bWyAV3K0K0brhEJaxkpCzTeUaHBxb67g1TYb5KH0jt9Y8SOZ53y2MudDHaWcOKwihnNZfMejDrIYfvZ8W7nXdJzMFVI6AsA3sDvIvwftFYlY7D8bEEtBJciMUm7JreBj1PxUb1pE90o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=lVPDD5FCk7Mnk4dkgEa6AOUm8XN9y237N7ysH6RhOQiXHel7_jzswE0PgH2cSif0S1nw-Fxz3Q-chQhA_hpVLRwxs7bLA8tKdAaTjdvJRL6ehkR-F7_hCIM2JriQQpc46Ey9of2fnR2oWazFKr5p4PjqLQ_HUbssjBHUJBQH7mgOMiMFATk_HDNQEMJx-6FidROcvpgNa8lF5ngxgMJXm8bTj4zWfn_8sr0lboFra0mNJmcJ2TtcupsapLxEl1Rn3dpOQ9tSc3tYBYA4FztE2eYmmf2yEqNpJ_f9HN_8cPkeWVgq5Zptqo7bf565SmscnKjFn53ucBm2KIS9NW7xaZ-bXKKWlaaue6LRGg6II7sWYZhw0j3gUvuvjjm6ab6mIiXKtzGRAJ8rpmyFqQJ7BE9cEATQS2jghmxAtCebyHTauu83S8tbnF_iCotz4MBqLsnuLFEqrNs-AeUYJjj4MV3cYIlHPTUbDU1usbcz9Mdq6kpe7rif30MWSOd8Ks65l8KRFi3XgkuS3H4v_Axo2JSBM90nWm_7bWyAV3K0K0brhEJaxkpCzTeUaHBxb67g1TYb5KH0jt9Y8SOZ53y2MudDHaWcOKwihnNZfMejDrIYfvZ8W7nXdJzMFVI6AsA3sDvIvwftFYlY7D8bEEtBJciMUm7JreBj1PxUb1pE90o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=MoJhzxSNixmQXj8hEENU51WaJM88JOXANsUBngx7yieDgDaeZL4svZTu7bW4H6b-e3U6jwQFkWUp7SQH53i6Yu3BP76IJyxn9pMGBsWO2mcLn2WvfwcAznV8dbnZaAxeT8MY-Uem_6HUD30fgifZhMKW52AS_fR5YDfcxNp4PQ2Iwehiwzuhcj5wea5cQUS8f2jnf_yJR4Y674nrMMHpk72g8WmZIQrKlAmIPiqIRGlIcb-L_4B5S3I7LRy53iP6kaK8xJ7ThzOXjEig7oHh1xgedmFP2uBP6MKQPG9QrCtW2U8fTb4OCLrlMx_4pVuesrg9Q7OmIXXzBkfcxp3UJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=MoJhzxSNixmQXj8hEENU51WaJM88JOXANsUBngx7yieDgDaeZL4svZTu7bW4H6b-e3U6jwQFkWUp7SQH53i6Yu3BP76IJyxn9pMGBsWO2mcLn2WvfwcAznV8dbnZaAxeT8MY-Uem_6HUD30fgifZhMKW52AS_fR5YDfcxNp4PQ2Iwehiwzuhcj5wea5cQUS8f2jnf_yJR4Y674nrMMHpk72g8WmZIQrKlAmIPiqIRGlIcb-L_4B5S3I7LRy53iP6kaK8xJ7ThzOXjEig7oHh1xgedmFP2uBP6MKQPG9QrCtW2U8fTb4OCLrlMx_4pVuesrg9Q7OmIXXzBkfcxp3UJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=iEC4wiYGSFdxd818AVOMF4EDqUeDKm1jHh7m6IvTb4l5Qrub0gwjs3i_b42Iy8OJlu9u7e-HkMzKQUsGMSO-pG20Jlwi9hcxrf2Rdd4Enxzh-j4Ox8gHZHOYgsffKdz5MBcP7bXnp1blBpFdyDQ9X167nNUwVLGfr3tY_bwNt9M1umzcuEi4qnwdUpSXxbR7A8S36MIrdvVB-Wa-s79YErIVIsZvhBwBVEiZ02FI1-Nqf94D0q97TBXCp2rDy_9qj6SEPNP4-YP5cDCb-byiGYaTLyLiq4gA8FFb8_8oSixPkoC_lH7lieZbE81hL7O7b-LR9EGP99tVyebNRA1DVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=iEC4wiYGSFdxd818AVOMF4EDqUeDKm1jHh7m6IvTb4l5Qrub0gwjs3i_b42Iy8OJlu9u7e-HkMzKQUsGMSO-pG20Jlwi9hcxrf2Rdd4Enxzh-j4Ox8gHZHOYgsffKdz5MBcP7bXnp1blBpFdyDQ9X167nNUwVLGfr3tY_bwNt9M1umzcuEi4qnwdUpSXxbR7A8S36MIrdvVB-Wa-s79YErIVIsZvhBwBVEiZ02FI1-Nqf94D0q97TBXCp2rDy_9qj6SEPNP4-YP5cDCb-byiGYaTLyLiq4gA8FFb8_8oSixPkoC_lH7lieZbE81hL7O7b-LR9EGP99tVyebNRA1DVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=tdLDTsOCl6mAHsClmtxo7wMosEikfr9gepUUGcBPIsVY1M15RWyNVF9jHNDhT8D1txO7UXaLMXznNkI30hZQRPZCptDztgWUgvvQG_hAZ1jYhYsOu_-zJ7eSjyXKbMbfbXCF_03GV3oGAyE_KUM7ICDvotB7hvJfaMBJhrpxhAn0jIYPyK3NxIE9dUInJLs738lM1Zr8jUapfqDaNexpOpZaCCjsPrdkUYt6I7_yfx6qUqrkk9QhiLeWLfSdBlkmLK-CtxSuCfUZKDEHK2xIe1Vmfxg4o6vFOc7C6YT579jwOwLhabVpqeI5ze-2Wrim9W7aL4CA4leZSzhit3YBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=tdLDTsOCl6mAHsClmtxo7wMosEikfr9gepUUGcBPIsVY1M15RWyNVF9jHNDhT8D1txO7UXaLMXznNkI30hZQRPZCptDztgWUgvvQG_hAZ1jYhYsOu_-zJ7eSjyXKbMbfbXCF_03GV3oGAyE_KUM7ICDvotB7hvJfaMBJhrpxhAn0jIYPyK3NxIE9dUInJLs738lM1Zr8jUapfqDaNexpOpZaCCjsPrdkUYt6I7_yfx6qUqrkk9QhiLeWLfSdBlkmLK-CtxSuCfUZKDEHK2xIe1Vmfxg4o6vFOc7C6YT579jwOwLhabVpqeI5ze-2Wrim9W7aL4CA4leZSzhit3YBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=JzBqtuLkp7q1MTY9lgxzik0neIDVmth6VJKxtsfHu7rvVMZ_pBRJNwlJwvQ1O8Ni9rV7VLfmB5v55wIvJ0jViQMj9ORbotHanHFCuqW_NVxyso5rPqj3mLZfn25Ap0SCbEQ8fezsod0jEixdOpWV5RK6lp3oNMFlqrf20ccV1_YYXhc6KVPq-SYRKkbXn0FkbAAWvLcayOCU_UxkFYY9RZsRlHFepOk0vQzD_P0Kh2E6u5DBoctXhcwNt0ms6thOPIlR5-z3ys3DEWRnfpWvElAOhFIRpgOxBtBezYdOVHWdEqsD2Sl5YciSItHDcoURJT9pcYDObNcPa-bAmTBmZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=JzBqtuLkp7q1MTY9lgxzik0neIDVmth6VJKxtsfHu7rvVMZ_pBRJNwlJwvQ1O8Ni9rV7VLfmB5v55wIvJ0jViQMj9ORbotHanHFCuqW_NVxyso5rPqj3mLZfn25Ap0SCbEQ8fezsod0jEixdOpWV5RK6lp3oNMFlqrf20ccV1_YYXhc6KVPq-SYRKkbXn0FkbAAWvLcayOCU_UxkFYY9RZsRlHFepOk0vQzD_P0Kh2E6u5DBoctXhcwNt0ms6thOPIlR5-z3ys3DEWRnfpWvElAOhFIRpgOxBtBezYdOVHWdEqsD2Sl5YciSItHDcoURJT9pcYDObNcPa-bAmTBmZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=kUhkJyDE3WvNCE4Zpd7MsTmUCbBynYeTSsciQ5anDduHBuzMDRbjDjSB9YaXxl2c3uChKwtdX0rER92FdB5VRNjhBpw0I5NMZDNYUPvA8Ymg_et_Rr-0zxCeudh8_JStE5vo9MPszc7uMg3eJop9EOnOKp9Jhb13ZIZTyv4uQTIa8Oaz3G-KgqFej3q9s8FeagE2ktzq_x0_ct8k1V3VAiuTtA5fR_I2kYWYTBDVPhIbgNynpoO9VblK5ZJfkYc5-98Xe4MMF5Yw9U084pGMAkjeBjSfPJKKGlZWcYVq-z9Pdq-En6UqyrikRt8mXw-ps0gl7YvdBtgevkb7Ett58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=kUhkJyDE3WvNCE4Zpd7MsTmUCbBynYeTSsciQ5anDduHBuzMDRbjDjSB9YaXxl2c3uChKwtdX0rER92FdB5VRNjhBpw0I5NMZDNYUPvA8Ymg_et_Rr-0zxCeudh8_JStE5vo9MPszc7uMg3eJop9EOnOKp9Jhb13ZIZTyv4uQTIa8Oaz3G-KgqFej3q9s8FeagE2ktzq_x0_ct8k1V3VAiuTtA5fR_I2kYWYTBDVPhIbgNynpoO9VblK5ZJfkYc5-98Xe4MMF5Yw9U084pGMAkjeBjSfPJKKGlZWcYVq-z9Pdq-En6UqyrikRt8mXw-ps0gl7YvdBtgevkb7Ett58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=qmuAN3bGlEJJNMpuvPhfcT8GJpzXEokpPVJc2tIAjO9FylgtLXp8rn_IWKfmZ3QaBcRGwcjzg8QXyHptqIFeHL37qDhZAFDoYNQ357M3Fzf99s7F9lfItZho7LI3fc7MRZt72or2xV74bILeAhAi2cJcygvESptMDev8Nndz3KOA85WlJMrc_PYGcKb3HUxH7ywCbK9eiwCvc3ojFF8pHvczj2E2DbZdNuY1iJouLCq0jUw4ltEpYUauC9Y9KqhMpp2NlOIk0jK5W-_SO7_p2RPVw_hSnpL0s-3Y0fwAHRtjjOUYUAgpRvYm5lxE_rGNldkGRZe-6p_aIVO8IXb_cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=qmuAN3bGlEJJNMpuvPhfcT8GJpzXEokpPVJc2tIAjO9FylgtLXp8rn_IWKfmZ3QaBcRGwcjzg8QXyHptqIFeHL37qDhZAFDoYNQ357M3Fzf99s7F9lfItZho7LI3fc7MRZt72or2xV74bILeAhAi2cJcygvESptMDev8Nndz3KOA85WlJMrc_PYGcKb3HUxH7ywCbK9eiwCvc3ojFF8pHvczj2E2DbZdNuY1iJouLCq0jUw4ltEpYUauC9Y9KqhMpp2NlOIk0jK5W-_SO7_p2RPVw_hSnpL0s-3Y0fwAHRtjjOUYUAgpRvYm5lxE_rGNldkGRZe-6p_aIVO8IXb_cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz4rep21z77URbMev9MyrQkL8slz6fB2Xd2_qm8qIGfnY7ebJmhaFpfp9gsKesuRlREwru9dDl4flv7GF1JFCeUR4StwaTDpfgAzpcXAVbG7HRah4X5G9QCKZJB0AlsRWKwkAy_u2WmoMcyWZd16U2RoePd9ojfFaMxY9LP54CcbDuPtJBCJ34_MYmCha7PnG3MzFbZDRa8QR6OX1jy4xp-6KaBx8O7ONbUm3A0Zqp-PoR69TM2jdBOutNi35kjhga7DAHPxVkWaoCE2PbWcckxDirUypDnM9k3bjoNf3Qhe4iuNiflR9CzRyyrdXL0SzX0FgqqPRvVG6RdWZZhOANFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz4rep21z77URbMev9MyrQkL8slz6fB2Xd2_qm8qIGfnY7ebJmhaFpfp9gsKesuRlREwru9dDl4flv7GF1JFCeUR4StwaTDpfgAzpcXAVbG7HRah4X5G9QCKZJB0AlsRWKwkAy_u2WmoMcyWZd16U2RoePd9ojfFaMxY9LP54CcbDuPtJBCJ34_MYmCha7PnG3MzFbZDRa8QR6OX1jy4xp-6KaBx8O7ONbUm3A0Zqp-PoR69TM2jdBOutNi35kjhga7DAHPxVkWaoCE2PbWcckxDirUypDnM9k3bjoNf3Qhe4iuNiflR9CzRyyrdXL0SzX0FgqqPRvVG6RdWZZhOANFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTmZkpdPF_eTq2nCnnbva9GYuIfaHya8hrlx0FZpJwQ8GxL7j0gKMOROQ3n3pSEq-RNbUMOof4hV-Haf-0_YR8nsBNGEZ0TxAVV4MbOTJQkAWzyj9lZbCs5OcEAlp6ZjUQpz9o6XPIB1zBSGadGkdX_1Y6Cv_H3Gdq86MN04TMn3Djj_rAfrOW_rx9yjmAnOdhidf35vjm2iqSqeKYXIjzpAi4v-l4M4xOm07kcQWUFg_Cu01KXEm9nUsM-4jjlO0_FqShzxw3pIH35QJ6sfp1veXUuKnUypiiyZa6-gNpnQkmPBIY7ViCiAlHXW9jPD7DWlsK1mHojxwGm8_Aqocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN3ob1AmsVNwfwLz2w9jePnZPbCEQRoSunAt8B0pxKemo1dtvNKdH7-l3u_LJqQp-1fxW7JV31ngVq4LWi8NKLR2UPX8JRzdZzsY6jK9t7gETkeBjyCeBlTjp2srx304N6EC8ivzCMik9RE2TKNCiVZZDWiCsmDwI5H4Q_0kEmNTzKgrlwNquJc5pzPNL0GfgNpu2LvlJM4Lm6pCO7oIvQOZzmya6glEJT7j8K6TYMt4FDYSe49ktXYUFA5XQ9ib_jE7n36vhRHX1hVFusBTUvA4DSfEXg330wh2E28oaw2PflwXKwKVvsBiqvHW8zGxPl0dAZTE98LrSZl4s1m7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0ok3L0xQWaDO5hitMJH3ovWvTw92raBV1lo_nljt0HVyO2CHpFm4KUSxoigKshK8qMx5_hPBcl3C3QtfmCz0HliXq-6nSrhp_skt1PWRSgdG7PsrxWa0VQtGt0zsckmXOQhKHgLbMacb2S_9TTsO4n01AgZzZDSfoMJPNAnie1WJ4vMcjQwSZ7y1rIILIvKKtmLFSUR-ajqAE9sOkQvm8wsJdmdzqvwwMIUxfDvrLKvLO7fXNoKBdnCWEBeH_UulyK4JxyTIf7GpbdqsRXs27sRlFG82xesIULeOW1iZgbEKFXR6apu0jlyWn2hXoXVgHIOkIvdkv8bqioXIAlQFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVjecwaucdw5IxIbKipZ3F66RQFtQlveevk57QEN50MT31Ls0yEkatv25x1rQ1L5nq-72ikiUljF13Qn2CVYNFM8zheQTZ51MpzbRTWOyBCS-c5CXpzV5SwtKd4KFkrLQwQQrSK4rubDCOiVJgDYtjZcCPKq8wW6cv6zluub-Ub6aJ6YY9iJpCq1cdPtPgDzLpKrANy7xS4nVS2OG3cES8rdUntYgLhsitsAAcr-hihbboZxsvIUspslWNrKSLh6iBTnhaOAN1G2VZL-sIWkziTaFF1r7vsldRxVRWd2m37okZKDaz4CwnfmgmjQuGl275rk1wfaDK56y6Oz_M61Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEI-7iIkgF8OFOORclZIOlryEEeLYrD-sgZkp5pnb-8oszAcvHgetgszYK7q5JKrGvlDpi_qiq3V7nRacX03x1s083CvA1icbeIE-FjkGbxRIwUpl52jq7vIeUIYoUrwXCnYXWMQX22ioZYk6qWbLBypQm4M-o3PDJfp_4KnB0gOKPrahPyrsbPuT8zQVSMo2ihFFmDhcZmSt35uNNW7Zb3xUcysHRifWPZ4jFOlnCoARPzeDDh43e48OZfGgjQ5yZxPqeomfBzYBBur6JttYRzNbAXy80O1p074YDcyERhpd8lcNwIfUcmUKAeAFCA-ijaIZNB025WbkPtrV4bvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBvSWp0w9hCz4LEmAts1d-51d4wC6lDyfQNnKl5-duNqJFwTk8407nVSIFNYHKbI8av4-C5h2vgjGdxcAz3KtpDz4wxk0HluOT529BnFX7Fhu6-SGiWxqc-ovEae-9WAqRp04pWvUcamp791ALfUc3QfEZ0AwEnySH4T3H7sJmGYH_TZzGZarqGpQU1MeroBlgAEE0_CZFFOkpTaEoYFjEnmWLytiw54Z0Py8IkpEr4anBqMvb6JVK4CLSqsRGJERsmUQRBoLbOE4UEMHCFfqcpnYWmAAlRQlbEWzUWLpJv5-v0gJdt801gOxPRPAZxJdr-3XXDozqzmEPQXGARx_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=s3tLVheMp_dMFOH3E5P0Q2pTmwtxVt6IJGpok_0MwTBDso6XKSN1XgXoUi3kgtdCLR-Wb6lLdL6r6uuBx7ZLUkcu9k6mWqZROcdj7sTBEJEq5IRl2Q1BTh6P67HQqx2Hm5S0JVhAeL561Lf-lx6RQdCP_lAV0er9nrh1d8yLExo1_6JNA1Xj-aGUyBmO3iPcA_zkIW6LgJUZs0uRweqgJB9naeDvj0akBTTHR2tkMZMJfmF-HVL-BGs2CFbfbw4jyrxQMSb10G7dLc-JfmWS_Kf9heWs68CxI9DXJd3mq3-Yop_RrQpdO0q0fgmvVBLgQBfelyP-D2Aj82uosW42vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=s3tLVheMp_dMFOH3E5P0Q2pTmwtxVt6IJGpok_0MwTBDso6XKSN1XgXoUi3kgtdCLR-Wb6lLdL6r6uuBx7ZLUkcu9k6mWqZROcdj7sTBEJEq5IRl2Q1BTh6P67HQqx2Hm5S0JVhAeL561Lf-lx6RQdCP_lAV0er9nrh1d8yLExo1_6JNA1Xj-aGUyBmO3iPcA_zkIW6LgJUZs0uRweqgJB9naeDvj0akBTTHR2tkMZMJfmF-HVL-BGs2CFbfbw4jyrxQMSb10G7dLc-JfmWS_Kf9heWs68CxI9DXJd3mq3-Yop_RrQpdO0q0fgmvVBLgQBfelyP-D2Aj82uosW42vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=Ygq2DEKiKYi5Ggg1lkeFg1tCIDNfSKcTCNxPCwPmxvXrdPy-699mPsuXWbtJ6GKE5etpFe6X5g7MIjILkRwmOfs4jQL5BoS-70DSEBEBxdBc3gWNGe2v9dl1H7zoEWwQIcsTRPAcou78OxV93zmWKfmrUKqwfSCCyJa0v3XutBzF1XwSNKap_4N4PVZ60zYm2u8plVOjbPFtMBmzdho3K7ONORibWFM47jOf21z4LECwZyxaIWA9EoQdZisqMhRabi8A7ooR8ShZ108EkvvRBg5AEG_xSHAiwQ81CmkWB_DjqXVuu_Ye45W9HGnbP3grvXIybPJpbPWdH8DE9u2QsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=Ygq2DEKiKYi5Ggg1lkeFg1tCIDNfSKcTCNxPCwPmxvXrdPy-699mPsuXWbtJ6GKE5etpFe6X5g7MIjILkRwmOfs4jQL5BoS-70DSEBEBxdBc3gWNGe2v9dl1H7zoEWwQIcsTRPAcou78OxV93zmWKfmrUKqwfSCCyJa0v3XutBzF1XwSNKap_4N4PVZ60zYm2u8plVOjbPFtMBmzdho3K7ONORibWFM47jOf21z4LECwZyxaIWA9EoQdZisqMhRabi8A7ooR8ShZ108EkvvRBg5AEG_xSHAiwQ81CmkWB_DjqXVuu_Ye45W9HGnbP3grvXIybPJpbPWdH8DE9u2QsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LC2EZN6PAvOMqs8pxJPSBJZQe9GlAL0GRnkFfhDFlcDGGM2WkuxaESLIx2-upDBunz3osv55zRlHtULjciBEDkYwqyH3usbU534cfZZ3bIpRFSUV4IVD29E69JZzh8JlrtpfZlrgrSYwdTrwi2v82trAwSrN2rKI7OFzQXQW3P4GpBO4tuEoDyMab8XdwIfwxdkaTH-sVEUyVut4_TIy9YwaqjUxMvho288R6Mv9DRzGc4BI1ah-8Ax82WGpoqM37bTaChymu9FcYrzEb4NUSWEx1eRwnCrkIWUNDhCpL-y8zEYz_oOvU9H-6JbeLzQ4KN4SpWc-7sSRqaKR25Q84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eji4absrdzSPZXGySHjU8k0hsDCIaiEh0hSCe6wq_8QD9sjdMrYg93ujZ_7-X6wdj31HSIA1-cpW4TasZrZ2JZfF5MQ_7TTklqLpX41I32K5AEViOZcVU3ePSvA7l4dCSFIP2ofZo4cFAL85DAIxic-JAY3GmOmC3fwmxPMO4m54BC8YcurXr8aM13B9Ir7uMc2agxXpt-pbYUy8_1BO0Zn6bJDqB8-EoXmz0Lbm2sOM9Z0YfB_FqEPKzvr2fPqNQ5Ef8MWQcIi3h1wXK5X0Zjsz-7Q7NSpgMMisiytW066-cFIBwk9uA43x7xYCR-X0HCOzkdWB61P7n6ZbWMGlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS_hLX7_S-Qey-K6uOBrsCUIQh80KKozgKCIZvs3CQW_vrnxiaxOJe4r1o9I-Pt4C3KE3e7Lyz7Vs2677ApnrJ8DXgnb2HfivFMNj9k4zZG-XxUalDpwGXVuadlir64XlNSQ_6BA9Jj7Uz_V8dEEFSSC8xWkX0pr2PQMvCc36W7ARj09i4zZnWQ9MVxs9-A0tmChWxz4GYIMiosu76nEc3zU-c3HQ6aWGqboKCAI_mkpClTqI5Z2zdTZ_fV5q4FXrTeKC7oVtj6dvS-lB3GMBp3GQxZva6xx6l9wgcGJ6Jrbm_Afep3xvJZPm5sONtZ0hscjxpGY-42r9UXp6mTMoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=UAZodKQKoGrwtoT1oWur9BIRAbEWKvChAdbIzV59YMFSxM_1OkdntnaNTiNb2mZ3U344EKZy8TsrxdYFVwtIesg9AsWhgwIY_eF5WKYEOHcH2rVGd5paMF2AMHePI5MKPODUHZvksgOovl3ayqjJYrDSIoxPZSYRZjrlroy_miqp6l7nk9fN4YGIwqIWdPAEOHEnpyLkv145bSj_-jnZchkAwQmzmNK_pE7vxrF6nnhPzL7wUJSA7SkL1OJZyeLEq-Timb_Tm9iUsXj4HreOoLAkEnYCvJKgboetIRsJ-iAHugHSdFUvdwr4cJ4lAVW1syaIap1mYnYT--s0Fu8xog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=UAZodKQKoGrwtoT1oWur9BIRAbEWKvChAdbIzV59YMFSxM_1OkdntnaNTiNb2mZ3U344EKZy8TsrxdYFVwtIesg9AsWhgwIY_eF5WKYEOHcH2rVGd5paMF2AMHePI5MKPODUHZvksgOovl3ayqjJYrDSIoxPZSYRZjrlroy_miqp6l7nk9fN4YGIwqIWdPAEOHEnpyLkv145bSj_-jnZchkAwQmzmNK_pE7vxrF6nnhPzL7wUJSA7SkL1OJZyeLEq-Timb_Tm9iUsXj4HreOoLAkEnYCvJKgboetIRsJ-iAHugHSdFUvdwr4cJ4lAVW1syaIap1mYnYT--s0Fu8xog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=J02Ih1eQlBR8f41Oh9KpWgvJhV0Uhjjj2cYQ8bnZiBZLKFdOuXLjhzpTcEqSmr6pUqIJvHhJYJ_hnTGQXEzKMA8NCSQIMEy8tnkzmYh9IGT8HD3djWsSCHWQLWQNhvup4Fxpxw5sR6PULeZOJZA8sIPgUmzUMmXH0D4ov4F0IdEsHQoczrLiQ2m1nAgxntn9z7VEdOCbOefoDPrRUTNbcV237hBEd-WCm5sF1zhZ3sSc0fYA20AjkEgD_iWUtIYyN8k4J057AyC8LZi4F_xdBBuO4SiY2A2oeecTS0w4HG-Jpcp3INgRBIiQ_Vu0PjEPeigiKv4NW6vs3vJwsZwBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=J02Ih1eQlBR8f41Oh9KpWgvJhV0Uhjjj2cYQ8bnZiBZLKFdOuXLjhzpTcEqSmr6pUqIJvHhJYJ_hnTGQXEzKMA8NCSQIMEy8tnkzmYh9IGT8HD3djWsSCHWQLWQNhvup4Fxpxw5sR6PULeZOJZA8sIPgUmzUMmXH0D4ov4F0IdEsHQoczrLiQ2m1nAgxntn9z7VEdOCbOefoDPrRUTNbcV237hBEd-WCm5sF1zhZ3sSc0fYA20AjkEgD_iWUtIYyN8k4J057AyC8LZi4F_xdBBuO4SiY2A2oeecTS0w4HG-Jpcp3INgRBIiQ_Vu0PjEPeigiKv4NW6vs3vJwsZwBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=UO5zeEekGP-DLheCc5JcWHd_kvA9Qf9Flj8o0l1FAInc-UNC6OiJkFdni1Em4pWSg4js-qocFsLCmM31uXcTJgNF0jb_jwhxr03_YKsWHcSIQAmg7nESJNxnJgIDsceCKpiWPuIrsJDoo-lW3LIJIgwwGBWp6fTBkjh6vsmuocB_nHDRJT98gJ6R_UprIFi1AAfmJ6TCrNSruB81kMS15jfDcZNUfcwKPGWzVgh9XAWaSOt4ldft92fwf28F5r7SHk6R2uF16NT3-BlOJdZyWKyLbj26W61qHl5FiI-4ybrVjy5Pj9it-CyqAKw13DQZEvspdNlDTmNfJLrVoAb9WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=UO5zeEekGP-DLheCc5JcWHd_kvA9Qf9Flj8o0l1FAInc-UNC6OiJkFdni1Em4pWSg4js-qocFsLCmM31uXcTJgNF0jb_jwhxr03_YKsWHcSIQAmg7nESJNxnJgIDsceCKpiWPuIrsJDoo-lW3LIJIgwwGBWp6fTBkjh6vsmuocB_nHDRJT98gJ6R_UprIFi1AAfmJ6TCrNSruB81kMS15jfDcZNUfcwKPGWzVgh9XAWaSOt4ldft92fwf28F5r7SHk6R2uF16NT3-BlOJdZyWKyLbj26W61qHl5FiI-4ybrVjy5Pj9it-CyqAKw13DQZEvspdNlDTmNfJLrVoAb9WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HeEWMvCl25iovCcYZphhkBGW0Z---ObnLkY4SKgFqpdes9NmjNM2--KvvdJbbRwNCCbGTwslIbT_9RfCih_bTmVM23Sm_ZVwfKKm0BuhAIv8lKSwB0go_D9WoweOX8MoHkTaeUqknokuwmvYdD-KpMYSBW9KE_6CnxjVZU3TtUjNsI6tH3LxFOVfXUYh-LsX4rIutJFDoXyKHiQ3BNhPSru4zAQpE7M2QXmRoQEQFo81uF2PaV6LrlZBHiFF-cegGcV0qiP_dSuFSFpswhwPr6rEJLSXfCnuI00p9eASQP1vhpvJCaOcxZ44DKiUX_15UTwNG5cYpkRyMqIvTt0-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT47XQE66VkJFTFbmHrG4GganrF3N7TaqhVsfoKKrVtYgeRI_Z1KMnmruXa2HyHD_rVndZ5XVXW-cJYE-fIhxbpxdk0He1FwCG-6jVrstZUKllaRNygEUB7DJu59pfeEawm5eppBpK3xDWiSdwru95vktiT-RBQvJhOeq8nSbSPZFQY-u7d-E3CiiO4lMAuLIV43EDDe-wmV4yviAs9s7hhFXy2gwxVyiDCNYe313rgXLckt4aubVnSwNNmc_RE1S8bdl1FbBDDl5Igfrq1llzsOoqdsaHn8ydkNZjqb0Ked38psTpU079qKJt9n_WO7DneeKB73EZI38FnBVg7Enw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=UMLySyLwOrZxyTS-mJVcx4CoJqUK46qKOoFR1Cl-868EYBc985TW-w8b5Amj5f_b_7_VN06pCZCt18PjqaLe_OuM6L_6S5paVfgo0rJ9nXqKXro0F6hWhkXXeSRldWCUA9yBd5urfKTLh9sBix8ptyzoNsdCvVi8XZ6d0c2iFBmLk8ALslscVOFtn6SgxWqjOXqoYkmfOypLBWQVwlUArTxQvw2kf5L300uNOhuXQkPgzEf9dBX2XuvUAQQcg3iR3BDqJ_CdYQOvs7w9QTE8Kviz3C2uCAwq9aH0EOLbQURlidXzSoXg0hF-TQrFlypwJGIL151Md2Hl6KPLq6P19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=UMLySyLwOrZxyTS-mJVcx4CoJqUK46qKOoFR1Cl-868EYBc985TW-w8b5Amj5f_b_7_VN06pCZCt18PjqaLe_OuM6L_6S5paVfgo0rJ9nXqKXro0F6hWhkXXeSRldWCUA9yBd5urfKTLh9sBix8ptyzoNsdCvVi8XZ6d0c2iFBmLk8ALslscVOFtn6SgxWqjOXqoYkmfOypLBWQVwlUArTxQvw2kf5L300uNOhuXQkPgzEf9dBX2XuvUAQQcg3iR3BDqJ_CdYQOvs7w9QTE8Kviz3C2uCAwq9aH0EOLbQURlidXzSoXg0hF-TQrFlypwJGIL151Md2Hl6KPLq6P19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjKCvnL4200NZfjE1a5DSI3r5O7mbHeCViEpyy-GN_xzpVP0EiHJpViLb5FkTHqbUA8s_EZJpMJ9LaDoKn6MYF0u93TJBLaTBOdfD4Ky_K3EodyynCAwAKF2OUDeOsTahme_Y62Ticr6RmQbluIIMf9hMKg5Q3IiLB6zgP7r3tN9hEowbo4WbIHJaka3ttX15XXLN-RepJ5tCfq38gTYCPhfl81-l3cAw9qIMxTglzJm1gBdwwDvi6FAGzeJF1Kh-uKL9vmLL00W0cWmWJyZLOESBKYZaEY-EWo3vxe1nbymaJc9xA8-p2bliNY-e0gP4hiQX7D5MWRWHAhaO_KauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=phDN499r5z9reEba-zkjGHnVPW9GPpRKmynWKCPDX-vTVvWRnqT2GxgpwP9A90Vdp3ST8dwk3RjJ0kNbKMR-76Tw3X3gGUMG3uqGYOp18euQeekwNeqFPylN3lmQGs_5d7yEYNkyZHu2e5j04ejqB9cK0Tc7ReCD8lAFcjfiZSZMN91XTdVhX_RXW3elWKI05ZwHWcoLnO40f6M-FE3qdcPgG8-60J4JhZ8GegvpZvF_5lXVnCOeCUQpoRb-h4UP8-ndAZpB3zOamim8H-FzT57rkh17cG8U02s9HQh66gtvVW0-BEtp4phMzejmBF5V2MgWfaW8VgGNzAfFV3PCmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=phDN499r5z9reEba-zkjGHnVPW9GPpRKmynWKCPDX-vTVvWRnqT2GxgpwP9A90Vdp3ST8dwk3RjJ0kNbKMR-76Tw3X3gGUMG3uqGYOp18euQeekwNeqFPylN3lmQGs_5d7yEYNkyZHu2e5j04ejqB9cK0Tc7ReCD8lAFcjfiZSZMN91XTdVhX_RXW3elWKI05ZwHWcoLnO40f6M-FE3qdcPgG8-60J4JhZ8GegvpZvF_5lXVnCOeCUQpoRb-h4UP8-ndAZpB3zOamim8H-FzT57rkh17cG8U02s9HQh66gtvVW0-BEtp4phMzejmBF5V2MgWfaW8VgGNzAfFV3PCmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jes6xjwWdnOuoMu7v3oTDh_DMV7SPEhbBPsp8lTJX0IwqqDZhFvcXLvkBQkFqUlnwoXOQ9Pilqstmwa5_7lysiXED2snoydaa6bH_glJOxI-Ih7NHF6PQr3gQ1UKpwg4s_p5KBecqldyri6okDUDeLV__H5u4GDU1Y4A7mX-JuvE9yQo6kGtwxa56n4rlju49Myef0PdTl7Cb-3dNltq1WIJVaKAvvDdt_u9ePvTtdhykRHRS9ydOXMlD-jtEpuibAa5E7GqdQ96HYthmiRjJqL41-6jg_FEOTIVKCbOcSMAV3Ah-NZXHpWU8zPv9LkJIrwSLK1uVHTby2cCDWq_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
