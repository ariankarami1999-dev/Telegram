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
<img src="https://cdn4.telesco.pe/file/Z4wiiuiVe61UCx3MfhDVZoJfvttJy6ziEJxQM6q0EBAqKuT1xPMaaA5zmyWug2XWvUsibuGr8ZT-vkAtNbtCDDOkDsNMaAsK1PhgWtWmXzXuBZYfzqeC0Q_Ly6YanQnIKTOzLe0ZsznJ1XP-PSmZIr9Jh931rOU7xL6JL53I-8fCFju36Vwh3E5DG6jqMxUYr0nCs_UQf4as2ULk75ITWkRWU4TdaaGXj7h-yS1GZiHvGonYKB5yujj7zYLyizQlRpJv1RjKv_sfxvswYiAB7k5C0N0DSQBsB3I4jpL5atg_ne1sa_DFGQCfJLiq9ZkdTpAasb3MAEBxOi7NIpCzFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADUewyMLtkbS6r0yJr2o_5q8XCijdHuKiUA9hKY-DGXnXyNR96NgFdiHNejDPa64a1F6IQya5Rjl2ce4zTKLE9tvOWNuAZBsMqW1WCRQV7zKoLTGrCRL6HxnZRIYgX_UR8C6nJxrhMHJor596FTXZ9HjTX3Hpg9M-iM38GCFrTZqjlKt9QSom2_QMOHAcQOVvUGedFtaMRS1KyutpCqYgC6TwlPLASjxcgeyDO4ajDKk5k05Oyluz1cw8WUNlB-vrOSlNkgNmicnriYxYQcHqw9gyqzLswAYOKRgBT-uqn4iluYA-SKBIGG5s89d9HT2IIVSmgMunE3vKg41uZ3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWGfMfxSbYpyJ-d3OUimRnWnd5xCyF7vSLyAkM5gSHubV3fBwRjMGliw2xf071tY_mYUzLhO_uXfWol-S-2XvKpEyvw-p1hvnZTlYMRGOBdQCxRlJx2cO5e67YlgQnxVJnH0BVhSBnfP9JheA8lQLZpP7uSgbkO2K8d8zIIRJh21gZjALdf3Wa6hWFkmzbxeIlGr9TVYfoeY7CY5CNxndzC3bydtwaJoVMlWatdyQjEIyaA55MiJc6Lx0PzaksZbY98ZMJ1cskYXUHKTXPVJPuRgqE7T_UT76WiYEIXgsxaxm4ova0STtPevRWZNgw856ngo69cHHII_ZzhFqCmc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYPH6B9NTq2OOGuDuyIp5zKhHRktqySza1PlT_cqg6gOv5mkv9QccFI2O1yNUiQ9R3jBAwjXsPxLEAJAgYN2FhWpgvcu-OG6y5jos1yNk-5ljsvN-ih6TtdCQ95MDPw91AUUohHfEddc13b51Y_-dGtOlSscSUPRSnr2YwSHlZcIar0BUcg3e_vMNlo4gxbzSCwzCqx3dtyW1rbbByTNeN5RUeMVxvoU7HL_jLDL8nv-dLGtLpXeAzRFq9ji75IIv7IxdxftBVKsXIa1cWo1QmFhhE20wVmly2k08ym7IHfqgxNq2hAiRvCLndtnmR2l68Em3JSc7HhDyplQ8Pmhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=GXOjyDTTlKTq1FsI5dFfLjL3HGdzMNkVHR_7VruxDaVCXjnkphDunqSwjcbU1xPnCKMp3LWqxIkYM3xh_QGAQ7Pgq8slLXWyKS0iYWY4EjUfYZ3aQxCZjOWUo2t0ZKOt9Zirjti598Gwi2EcRPYQPRGRRsNhhfJj8wnIPVGLCrfuwJdLSUnSuDpklvMsTT07b4TIbYx7VS4O5xGlE3sNCtUMHER26J-Ddaii6qZtHhmeiG4R7O_Z1S8xSYldP1QD4dppn9Megif-cZQsb6E0ggg0yK-gBi-vZrel5OjSIM4H70cL9cXLcOTP9Rm61c7wLkGbDAmzXSa2n6YKkjmitg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=GXOjyDTTlKTq1FsI5dFfLjL3HGdzMNkVHR_7VruxDaVCXjnkphDunqSwjcbU1xPnCKMp3LWqxIkYM3xh_QGAQ7Pgq8slLXWyKS0iYWY4EjUfYZ3aQxCZjOWUo2t0ZKOt9Zirjti598Gwi2EcRPYQPRGRRsNhhfJj8wnIPVGLCrfuwJdLSUnSuDpklvMsTT07b4TIbYx7VS4O5xGlE3sNCtUMHER26J-Ddaii6qZtHhmeiG4R7O_Z1S8xSYldP1QD4dppn9Megif-cZQsb6E0ggg0yK-gBi-vZrel5OjSIM4H70cL9cXLcOTP9Rm61c7wLkGbDAmzXSa2n6YKkjmitg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=RvgOThWCk30BNbhADIwMoqi5QeVsm9vkQKFrxWZUe9M5sV6YjE0OC0z3cl0VNs4qnw6s_J_Kdzl5Qk2H95f9SmQ7txlM0JWoAUiJis1Wv2SXj2daEZUsBu56QvOpymv-C-JU2NPwQc6uaWpRBGw4B12Otv6w04UGc9ggiXsm-GwnGgu4ceU0IX7aoBFNm6URamxC3eDWaCcZCeEXAcljEhXCO_dMnCO58jdWL-zq6Xr_Zw7MHM-OlkoaDGyrhLm0H4O1WdsWZOb8c3zf3BctVqODs6il-ejkPScM8wc1xdAe_3ziwZvik1FKnrUZNbeQFFSdHaFsyhws4pIslm0jPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=RvgOThWCk30BNbhADIwMoqi5QeVsm9vkQKFrxWZUe9M5sV6YjE0OC0z3cl0VNs4qnw6s_J_Kdzl5Qk2H95f9SmQ7txlM0JWoAUiJis1Wv2SXj2daEZUsBu56QvOpymv-C-JU2NPwQc6uaWpRBGw4B12Otv6w04UGc9ggiXsm-GwnGgu4ceU0IX7aoBFNm6URamxC3eDWaCcZCeEXAcljEhXCO_dMnCO58jdWL-zq6Xr_Zw7MHM-OlkoaDGyrhLm0H4O1WdsWZOb8c3zf3BctVqODs6il-ejkPScM8wc1xdAe_3ziwZvik1FKnrUZNbeQFFSdHaFsyhws4pIslm0jPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=PgiT8J66GuhSYCyzzcnzOWQIP--SkJZOgE44OZ5O4J9juGHhrZ4EU-9k787XsKUtc0Fp7NFxBuylVk9d5g2zeHj4ebkKCX4qmcTaMqwdth3PsW9ZgnBIyfXzPJ_CfEmSjGl3BkBXAWuzJN6iPQeV92Zh8wkVUgstRedbU7WX4MFa3Yzn2wMjIgT81MlZrNJ8F0Lli3K0qQ7aXek-QLgObgcafVvoGy1EtpA1j-abwAiII5Yi3zzKf93UYVa77zSV9gbZ2kbSYnfdmO-SuGFN6ePv1HuJasJCpFZbEe9PkIeuApKDcfXk1M3SOeNXOBa0DChqxxd8PKVT2dCQd_2f4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=PgiT8J66GuhSYCyzzcnzOWQIP--SkJZOgE44OZ5O4J9juGHhrZ4EU-9k787XsKUtc0Fp7NFxBuylVk9d5g2zeHj4ebkKCX4qmcTaMqwdth3PsW9ZgnBIyfXzPJ_CfEmSjGl3BkBXAWuzJN6iPQeV92Zh8wkVUgstRedbU7WX4MFa3Yzn2wMjIgT81MlZrNJ8F0Lli3K0qQ7aXek-QLgObgcafVvoGy1EtpA1j-abwAiII5Yi3zzKf93UYVa77zSV9gbZ2kbSYnfdmO-SuGFN6ePv1HuJasJCpFZbEe9PkIeuApKDcfXk1M3SOeNXOBa0DChqxxd8PKVT2dCQd_2f4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=fQhnPMJmzMItG44aVNnVnpqBFGNwJqyJOpgy22Y8h_FGbO54zdhDra5OkaSXESTEpc6uEWPDW5gEIeFkSKDApK-JH3FKsYtzkIamPYbGD7EPhXA5nHAzLweJGlOHrtEK77FfdFWNVcIfNRWu5GVyfHMGfcDR1gH_0gcwM7DDquhLIvRrpm8M4w6U1sOxWv2iSnxKfAl1Wm8fYQyoT0dn-bDNlPn86qqQy3SE_B0cWIk6bne0KVyTeccYVRigKMYL0uW_HgWG06K8IO_JrOgwTAMyOhN9416Q0gdSne7uDhTwpG39puedTkd1MfGGUdW1mD8DKSE1lB4dYJ9mM_xYX5BLXP4NCn67GsVExU-U_jSpsm3BuIt5EtjtiU98-lfkYbnlzgpQW648fBRJQ3Qd6D-I9PsgjUeUk1UpDV31cmxoh2n7xSlEJx7tl_8bgBi4YRpcq0LUnQBivgo_JETyRXFL0LTwvg2iJUoXk4g93heYLmkZUfBpoQtqFE_iirb3zHQEAGR4F5ljo0KVDubsP2SiGHieqLynSl3cMVD09IzfSP0Z_y-KJbaPfRiy0vlN8B50zNAgoUq11CozUys7Q7985sc5lhZGWyBYCc2-FvP42ARZNCRXUy_f3673YPJt2E5lKDGen7KwVkgaQWF1QK-k0f8E7lSh4J2Cdnmz10Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=fQhnPMJmzMItG44aVNnVnpqBFGNwJqyJOpgy22Y8h_FGbO54zdhDra5OkaSXESTEpc6uEWPDW5gEIeFkSKDApK-JH3FKsYtzkIamPYbGD7EPhXA5nHAzLweJGlOHrtEK77FfdFWNVcIfNRWu5GVyfHMGfcDR1gH_0gcwM7DDquhLIvRrpm8M4w6U1sOxWv2iSnxKfAl1Wm8fYQyoT0dn-bDNlPn86qqQy3SE_B0cWIk6bne0KVyTeccYVRigKMYL0uW_HgWG06K8IO_JrOgwTAMyOhN9416Q0gdSne7uDhTwpG39puedTkd1MfGGUdW1mD8DKSE1lB4dYJ9mM_xYX5BLXP4NCn67GsVExU-U_jSpsm3BuIt5EtjtiU98-lfkYbnlzgpQW648fBRJQ3Qd6D-I9PsgjUeUk1UpDV31cmxoh2n7xSlEJx7tl_8bgBi4YRpcq0LUnQBivgo_JETyRXFL0LTwvg2iJUoXk4g93heYLmkZUfBpoQtqFE_iirb3zHQEAGR4F5ljo0KVDubsP2SiGHieqLynSl3cMVD09IzfSP0Z_y-KJbaPfRiy0vlN8B50zNAgoUq11CozUys7Q7985sc5lhZGWyBYCc2-FvP42ARZNCRXUy_f3673YPJt2E5lKDGen7KwVkgaQWF1QK-k0f8E7lSh4J2Cdnmz10Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=neSr7lUO0bss5hqV_mnBkQfdcw3smCYFKqKv10RnqVE3pEW5e3EQu1XteImYOeHjc23xFd5v8dRdFebmwTSkMSJGDMy60QG5kzAqtt0sv8ur0LsVT4cQFpr-83IYGINlCeS6TOSLzyWn3qabLtNAWlfSozYolnrFZE80Rt76l5EFQ9kSkEuFlaMAe4Mwj6jLaTWnIFEMlSIODRog3gZEgK71O8ggT9MXytsvDcLtlhxcbk1WglX3SmRJVuWsqsKRAYZXBteHvLXix0OTmCwrNd-e4aXXAbLYlyigMTmpZzVpSg-xXrcwcGK3w5alBWbnHNPOFp1O5gVmqcSUFFxYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=neSr7lUO0bss5hqV_mnBkQfdcw3smCYFKqKv10RnqVE3pEW5e3EQu1XteImYOeHjc23xFd5v8dRdFebmwTSkMSJGDMy60QG5kzAqtt0sv8ur0LsVT4cQFpr-83IYGINlCeS6TOSLzyWn3qabLtNAWlfSozYolnrFZE80Rt76l5EFQ9kSkEuFlaMAe4Mwj6jLaTWnIFEMlSIODRog3gZEgK71O8ggT9MXytsvDcLtlhxcbk1WglX3SmRJVuWsqsKRAYZXBteHvLXix0OTmCwrNd-e4aXXAbLYlyigMTmpZzVpSg-xXrcwcGK3w5alBWbnHNPOFp1O5gVmqcSUFFxYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=tUMXReSKukfGoFVL21oLNxgP0B1uWW7DBM_jbCehHIRoKl4T1f0SB5N2X9oz8ZCaV-PqUnapyw1AQQnHSuUuTbPx6Bk4whVMvvQWnX4TxCJxT86ZkE97zPnRYHT3PFgsSiaALGGNTvB0-6Gk2HxH8S997JlPs-xRwLAlrcjQ8DPf9vt1fGFqRrGsFSXnrmlZhh42VUP-T3Q1crZkxcTB4K25NrMZh-UMkr2xOWJLCDTIw0CCy1CjXwrrU-SSgbUl8cgDPlQWd9KMBGsfprW6nXr0QNKK0_PFMRPjiekEPkKtLMgYR0SmSwCvwyV0noh4oY7XG18wMIMkzx4_sBnI3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=tUMXReSKukfGoFVL21oLNxgP0B1uWW7DBM_jbCehHIRoKl4T1f0SB5N2X9oz8ZCaV-PqUnapyw1AQQnHSuUuTbPx6Bk4whVMvvQWnX4TxCJxT86ZkE97zPnRYHT3PFgsSiaALGGNTvB0-6Gk2HxH8S997JlPs-xRwLAlrcjQ8DPf9vt1fGFqRrGsFSXnrmlZhh42VUP-T3Q1crZkxcTB4K25NrMZh-UMkr2xOWJLCDTIw0CCy1CjXwrrU-SSgbUl8cgDPlQWd9KMBGsfprW6nXr0QNKK0_PFMRPjiekEPkKtLMgYR0SmSwCvwyV0noh4oY7XG18wMIMkzx4_sBnI3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSE6IIzfNzfo6leLFDoaUUbKY2phQ6O_zsIZqIQQbugG60XIx2d_fPYxXpO6gXyPJxkeGHDohYcrJJzTAiCMhOrkNiAAtqU3F3QeaX9V3OjL7GjVoDr0mbaJv0vAYaBaVo_itZr0GhscufbX2FCct21lF2iU6xbLgkwqZt6O1VEFbjIcm3CG8cXYLPk1C8fPJClcAd2hKzmOLU3VhRSuUtanNnNRP4xXWlRjSeyUXnzRk5Gw3aHxaXZjhHtoXgwpFEIWrfjw9nxRIwctiDvK06sffGNH8DscvlHR6b8McPL6_0J3ca9LLLS4Rr4xarHuM_i-qUjOF8SLkRCOu8jqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3CYmMUTgLJkeP_Ct9PQcOr6oSE0S7CDBN_oQ8ArlJ8A5YVHbGOIM5okPFtJNdM6Ptyk4grSws4au3hTuZd14NzYB80lj_t6rkXkqTO_XAq2R6Kr3tOmWelv4IQx00jEB-hCh-5RGaj2cL_E4ppFFKLpRNhmiKG8zwKcgdvoRF8hETarS3RANrTVGOqA4hoEwx0jxTLYP4ycSR2kl6WFATl7we3Zgdtw2yn0sT2eH_lDDC2WbMpch-ToFmEznU_txEBhcbiLJVoD2wKASMak3oftEd11gDPztqZ6boE2C-iAV2h_OteJUUorP3IzOyb-J_n8My_0bCYPmWj4obDrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-qPjVziPUQ3lPRnrB_tngLxhtP-gPe-wYf-XEHNeoNgrqVRuhO6yVRDVEQBLhSnQcVUN-B-vssdhbwW8pFQx0pAmFYybBJfZqHutgkQIQ2k6DoJAWve83lmeF_wnl7FJX0VSHj8nuPt8LOa6ZT_80IwHFJdZInxpvrgZmKAS7htDZ4VxvhrelqLrEDhnUBkcB0Fk76KlzsXm5Nz_yqHyNwREzLDOJZv1PGZvqQ-maCxO68rn29NVbFr82XduNc7WexUMMe6YDuZz7uF-YSa2jQ2u91_nBSjN7AmrrJWUpb_xcJ2USPoMlAfHtuCKQxe8_widxe1Iz2roZdiFTfCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkEyefNagd0kJ0n7k02Sp6BFLnowPMduf_pCoUulqhY0YnDsb8xorot4s-Rm1vhw70ARTgWWdAP5gy9isbu7rQsLxJRfskXm9tJTTY08Cx_JODacSldPuRsEQvOjJTsGzTh_DmooGWvgJ9Cut7r3-74CtaaIQfB4VWsf8rFzdHTMYq3y5nB4hnMo9Wm7qHE-8KZti7Ug9JLb3PU9hErYfu2fbEspheZPKiqMRy-Z_RS3dGf5IJMyCrMUpzDMEjV4H_LrmO8EQUxLWdl5poEMx2LSMcOLuRr7YL2VIt51KAPsqQTtjKBuQlZmb2QTeBZx5uzOEqtgHSVnGjVAQfNEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=FTrc_v0tooxTKGeMJU_87uZfdMI2lB_VNdtjbYKB3sgbg3-LInyR6YVLQ_IczlWwUmRYxem-Ku83_GRp5-ZAwq8A-ZyE5ZUhc2zr0A6qiwhmJnM_d_kDTlvTaFEVdNwwULTHFKRSxiU7LK8kcyUXkDDqUPwaZ7NOcKm8f0VyZQC2OgF2pclawcJe0nWqNIxvgjjmTtnjqPYIJ-qpMOecclzLTDxOFy6lSJ-YQH-V9DgpJubM-71fGeV3LA56I7oy3rxJ-FJlMXEGpGf4WHtXsP-1TGz7jkRtfkqMz6-B7YZybrFZCZPuAqU3Vq4chseP5_sF_WRzdYrr_S9-XpbzoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=FTrc_v0tooxTKGeMJU_87uZfdMI2lB_VNdtjbYKB3sgbg3-LInyR6YVLQ_IczlWwUmRYxem-Ku83_GRp5-ZAwq8A-ZyE5ZUhc2zr0A6qiwhmJnM_d_kDTlvTaFEVdNwwULTHFKRSxiU7LK8kcyUXkDDqUPwaZ7NOcKm8f0VyZQC2OgF2pclawcJe0nWqNIxvgjjmTtnjqPYIJ-qpMOecclzLTDxOFy6lSJ-YQH-V9DgpJubM-71fGeV3LA56I7oy3rxJ-FJlMXEGpGf4WHtXsP-1TGz7jkRtfkqMz6-B7YZybrFZCZPuAqU3Vq4chseP5_sF_WRzdYrr_S9-XpbzoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=ERVSWZnS0iCTdi73-UscSWDMPdTL0gcn0-ef1srfJSV7_F8xvVMFnbx1FZzQC1JnUSeUYPQFU12gXw1F1G-QuMgJ8DxN5p4YDiIwOEPdg_AyxW-2ugRkZz-I6k8XLnvgQfBWcLOwDeVSrC3tQlDDJ49sxm-2YUA7BwFf75eK74Q6fdVWoQivPozTTzI5rK8LPXFsrYRZ1G50CW22QgKMpnE_mluDktx_J-IULKZDvVPIzWApoM52xvovSZotFPKLlG7PRyk3od8yKrVLmJcOyBuP3AbsRwOM281Pn3MFxekpNZphW-AFF5RFlxzP9UfbcNgLElySfGkPS6oxNcQrhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=ERVSWZnS0iCTdi73-UscSWDMPdTL0gcn0-ef1srfJSV7_F8xvVMFnbx1FZzQC1JnUSeUYPQFU12gXw1F1G-QuMgJ8DxN5p4YDiIwOEPdg_AyxW-2ugRkZz-I6k8XLnvgQfBWcLOwDeVSrC3tQlDDJ49sxm-2YUA7BwFf75eK74Q6fdVWoQivPozTTzI5rK8LPXFsrYRZ1G50CW22QgKMpnE_mluDktx_J-IULKZDvVPIzWApoM52xvovSZotFPKLlG7PRyk3od8yKrVLmJcOyBuP3AbsRwOM281Pn3MFxekpNZphW-AFF5RFlxzP9UfbcNgLElySfGkPS6oxNcQrhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=dYZaQS2WJ6XL4xGRcHK725f2Bo6PBmMO-6wJtdMzQmz8vEgtHf_L_M6u5K1uaABtXXKBMmuDtPKbLFr6sihK5JXjh_g8L3n14s7MHAWVrtjFa8YeMZ8H_UxVTvzZPdUnGi4gOD4N4wsnuc70cZ5i4Opxa2CKa9kW7mmjTPScLNoUCt5SvyG1KfQClhU7wNAt0NrU7ZI0AsW0La3hHTnaGxKS3gQ70Wk2jeGqYhRPN29BOQYbx4nGF0nSyeNXirAiMmOD0_WAkOyEdcneIY8y7sSz_eUCDhLr0qnFNuGlzRFBI_JHBN3xgzbCpIBqLDm2Pzrdj88Vxdsz0pKXfhdnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=dYZaQS2WJ6XL4xGRcHK725f2Bo6PBmMO-6wJtdMzQmz8vEgtHf_L_M6u5K1uaABtXXKBMmuDtPKbLFr6sihK5JXjh_g8L3n14s7MHAWVrtjFa8YeMZ8H_UxVTvzZPdUnGi4gOD4N4wsnuc70cZ5i4Opxa2CKa9kW7mmjTPScLNoUCt5SvyG1KfQClhU7wNAt0NrU7ZI0AsW0La3hHTnaGxKS3gQ70Wk2jeGqYhRPN29BOQYbx4nGF0nSyeNXirAiMmOD0_WAkOyEdcneIY8y7sSz_eUCDhLr0qnFNuGlzRFBI_JHBN3xgzbCpIBqLDm2Pzrdj88Vxdsz0pKXfhdnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se0Jp_BZ9FmpzRP2-D4YiES-Xm4zizUQtZpIMVfByk8J3pj1Cd6RtE8acfl0UKE0C_9uA3XzARGEWmYBWpqESsdE5j_u-z3o_XcorfNoXSj-DZKFBpOK2pAVguVcy9Ayeye1L6Q1xzq5v9uNudyxsy8dR7dtjATj0ohadSyuJVnLhyQTnPmbJIUmDIHo6BpgFmaU-cBVvy9awmTgBLlx7bQPvbkOaMm3M84577d00MpZgnG4NJexJWaiJiHpxA3C996etVEiSL9RkGZJBZMxKAFYUmWHwKavArRkXdkyFu8HE3KF6zJAJgFR1vdBI59AkFKorA45cy1wzQP9i_c40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=UwpPaeBVav9JFOMagTE3D_XQRH_L34uSHbhs5y6OjkcVTGEhxR9WpfDx8sHi20ht4B8XZ6g4AdznDAmHclXNYI8-EzPJyAawfxi2MNk6bX7cJCfkPjBbZnxH_ckLy5q8Ege7pup05Zqt87KS6CyMDg3yzQLCdXdaRA0X_tE5J596zNC37gWt2NLxiFMT77lNa4xKfFKHJNlvuyr4jYQBgD97kkQwHwAUtt3KP7V0471WI39B3wJWBao5COP9_vYCBiYfhY1d_FUizM8GNWLf0iDjptBAga4zQU2nDZZ6B0Dw3_2eawacBE0Uo8gZn-XeuxulKjgsbA41u2s9Vk5LZ5Ix4gMc27VErjl2bCc7l4tIJP-VxUwO-xM8ecsF9FMZtk1o3SvscMZaMDC-yv8mT5TjhpDO_B1pVjHut6HgncNNZjhPjcluS-XF8C2hIvOuDbgUAoA0MMHjL_t2tLQeuuZ3PGLHrqQ5wmkCwbmwrHkaCuDeW-mSED6-0S0tUL0MWVwuWuKfQH_rHkwIWsxDvEB2TpJAp8A4QdJ-hngXZchcWqPMM8cr9-OiXmqn6inwMAxbI5AcJODHHOMFFzexeZIEvTYqudzOOhS-QNogDMFomqD-BXBtff5_UGgxusvfOSOU4YkUUXecEqpaiAQvVOLU7PfzEM7Mr7oaKjeFz34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=UwpPaeBVav9JFOMagTE3D_XQRH_L34uSHbhs5y6OjkcVTGEhxR9WpfDx8sHi20ht4B8XZ6g4AdznDAmHclXNYI8-EzPJyAawfxi2MNk6bX7cJCfkPjBbZnxH_ckLy5q8Ege7pup05Zqt87KS6CyMDg3yzQLCdXdaRA0X_tE5J596zNC37gWt2NLxiFMT77lNa4xKfFKHJNlvuyr4jYQBgD97kkQwHwAUtt3KP7V0471WI39B3wJWBao5COP9_vYCBiYfhY1d_FUizM8GNWLf0iDjptBAga4zQU2nDZZ6B0Dw3_2eawacBE0Uo8gZn-XeuxulKjgsbA41u2s9Vk5LZ5Ix4gMc27VErjl2bCc7l4tIJP-VxUwO-xM8ecsF9FMZtk1o3SvscMZaMDC-yv8mT5TjhpDO_B1pVjHut6HgncNNZjhPjcluS-XF8C2hIvOuDbgUAoA0MMHjL_t2tLQeuuZ3PGLHrqQ5wmkCwbmwrHkaCuDeW-mSED6-0S0tUL0MWVwuWuKfQH_rHkwIWsxDvEB2TpJAp8A4QdJ-hngXZchcWqPMM8cr9-OiXmqn6inwMAxbI5AcJODHHOMFFzexeZIEvTYqudzOOhS-QNogDMFomqD-BXBtff5_UGgxusvfOSOU4YkUUXecEqpaiAQvVOLU7PfzEM7Mr7oaKjeFz34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFz2Dw8LYdzSaDugUlzrDj4aECjNmH4c-781vh3kkMvlqMeS__75oxAVDPcPYWh0N4rBeHywxnL0ofwzESWq6FfckUOXs5w7v1Fv7HuSghz683dMcVEdkZOAdhJCug4plqNqrks-Mnp5yFAC0rs3Tgemwi85QX_4elDOZ0UMx33fmkS93dBT2K23eUvaEmZnX846bPeGDtwRFgejoSMDupFaPasSXzOwasb2Br_55d3UP8yn6EnIW-kXANqPkP0z50D7-e3keq3qJDIb7nZJjUhXXw8ZXuurhvk0NLnsOtiq1VoZymqGZrK1M0ey0NsXfZ91JVJqYDnKPt_8j8NsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=sjosGhdDXA69lGyK29PC4N5BfRoeVbY81i6O0A_4K0B6uuTsKirYidAt0QVPo82AVYj1Fe9t8pDKa-RR6EFMrSoV4VtK8cdjn2zL613jd5iEavaepBBS54CrkACzMlXO16rTJm6ax9VOZx8B9hi15FW-JGH9ToI-xUY0_JdxBP_Gnp95RPuvIgafm0qzH59gErKakwya0GFwjYgAEAZvmGvJgIpXRFd_uhVsXG54lQ8pIwXndDUE2DPMECKD93SXakBO-CV-mRbeMfsd4uGUsdT9UASzNLZkZggMs7beHF5HWDXqyfLIzZAg5iSQB8lw5eJ2ZdDqzFFQ4F1L4qkCcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=sjosGhdDXA69lGyK29PC4N5BfRoeVbY81i6O0A_4K0B6uuTsKirYidAt0QVPo82AVYj1Fe9t8pDKa-RR6EFMrSoV4VtK8cdjn2zL613jd5iEavaepBBS54CrkACzMlXO16rTJm6ax9VOZx8B9hi15FW-JGH9ToI-xUY0_JdxBP_Gnp95RPuvIgafm0qzH59gErKakwya0GFwjYgAEAZvmGvJgIpXRFd_uhVsXG54lQ8pIwXndDUE2DPMECKD93SXakBO-CV-mRbeMfsd4uGUsdT9UASzNLZkZggMs7beHF5HWDXqyfLIzZAg5iSQB8lw5eJ2ZdDqzFFQ4F1L4qkCcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGilnfI2Kivge8xUJ8ol1NCUUbmjB1mcIBnzpdv6OKmDe-f-BUVmRTGjyxBgWPoR2qt-F_CitENqgt7pCXXcOwIde9PtsTrR-dLs6CrAo9Y4CnISpO60RQhsDJhSTfBTo6B0IBwZK4zdbu0mkn8DiqRqazMMTMlpOgw8F5ecwdym1MjroU66IikF8wNeAzPzx5Y6k1kU6KldrPwppShOUBOpYxZqhtznWYi1gOiqzU2Go_-ZEeNkkaE94Ts26TmyC48wASuIJM91wQaPz7GNofb7dLYYjW19CXdZ9YAq06zEgKbGXpeKOCi5VsbvTeDfco8uOap3sls6u924B2Pc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNasQau6gx7s7vCaIvjgcszxIzm0eMjXdwQ_5uZdHLlwrEWT09gTKO1-SOFs0ZiHdKIJdWU4zRlAsoyRpjPmR8ysNF_avyaPP4ByIeEd6Jjd1otFdX-Bj6OKbpZQ-gPTsD5M_ujGkshRBg0J-9304Cu-iC8nLP7lz_MVKcFZatk7YPDv1cgBe_I9erm5yOOVRLQUO_wY80vr5sfJYqeI3-xBM1dtddj5bypvXrfYblFBq2jQSR3lYSSQoZBJmpg7p-GuVUgjDMdIeaUdFMaWO3lEmMzjC9CL6Tev_Vt9iJ0iNiXFdXp6XPTGrJhN23lHDE9AlhzuEa_jgSfsQy4h_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8VjKg4pCXPONO68D833xUTcqLKlXv5Z91_vIVvb9CjEET_I8DFuJgAQLWjTsMlC9t6dIWGe3qcm88hzE_EfGJT-3gttU5vMfNIP0zjAw03tyzL2feH0JcO7u-hq9akF_rJITAgIdyRxZrlfLQNr1VYSepsdd7-kOhWtAKtnRl-I13iU5yivCPKTuhD9kuTKS8WI-l2odlWzwdviQwAWWpyld7p8bL9qDrbP4iD87o-f0tdS31BXCePvCI9PsglGmapSfSIK4Zfe4T2oHgTvLCK9UtQ_8Fc78vxS0OM36_XH5KRJBr2mrTnVHoTC91xVXg6X7cb-Rfm0n7nMA8JeTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=NiQzES2AMegkXltJFd8DrFKiOjCK6hDmJ9W5uGt9kfajO9e-aPhH63IDl2dEo5d2FncVGyBwT_C8q6B3fERtxkmPJQDc2YkNjqSn8A-K1AsjwXnJCLL6ebHCJiGl4hLVQYOosATyGUyCzFVC7vEVcDplSiHV0JIja2mmAcpuHwdFGhPWur4tq91j1meuZU3CzpfLYRmB3GoT5SfsHs4LcaLlBZUBcVMZBK8CE9nduinKRZcaLmSBgKYoKzm2yCXb5pyp77Ch8pKSsis5sIFuCTe-fW6eE3-GkVxWIwGUniRXX3Gl_bhxEO8ip8YuJYa5p1MWGrzEWvYT4YCaZh95rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=NiQzES2AMegkXltJFd8DrFKiOjCK6hDmJ9W5uGt9kfajO9e-aPhH63IDl2dEo5d2FncVGyBwT_C8q6B3fERtxkmPJQDc2YkNjqSn8A-K1AsjwXnJCLL6ebHCJiGl4hLVQYOosATyGUyCzFVC7vEVcDplSiHV0JIja2mmAcpuHwdFGhPWur4tq91j1meuZU3CzpfLYRmB3GoT5SfsHs4LcaLlBZUBcVMZBK8CE9nduinKRZcaLmSBgKYoKzm2yCXb5pyp77Ch8pKSsis5sIFuCTe-fW6eE3-GkVxWIwGUniRXX3Gl_bhxEO8ip8YuJYa5p1MWGrzEWvYT4YCaZh95rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=gynWigRZwPV6sHpBC-gtarJfeEQwUL9uCGUeYbuXiercBk2-sJluXB5pOQN0eWSRXts31bAfbkeV9-j0aCOSdZT7aRTCmtrDfm7byrYymbxcjU8caJiR5RPyVpODedyWL0CFWA35FOICmOhRBfSr7hLnuXOKw1V1sWs1dbFjyvMnPm36G1QT05bYwuFC_1DN-9OERE7ff1X8oOcHO0Zd-onlTGX5UGtpmwtR3Rq_j04QQCMlQebIN20FcPahSZsfCtMxvCAErCRI8Jk92T3MpcZxU_3r7-89jpytjpzYyINohUokrJ0xJMQdDsvNHstX1-ZVPuzTY26Pz_lwkZLwAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=gynWigRZwPV6sHpBC-gtarJfeEQwUL9uCGUeYbuXiercBk2-sJluXB5pOQN0eWSRXts31bAfbkeV9-j0aCOSdZT7aRTCmtrDfm7byrYymbxcjU8caJiR5RPyVpODedyWL0CFWA35FOICmOhRBfSr7hLnuXOKw1V1sWs1dbFjyvMnPm36G1QT05bYwuFC_1DN-9OERE7ff1X8oOcHO0Zd-onlTGX5UGtpmwtR3Rq_j04QQCMlQebIN20FcPahSZsfCtMxvCAErCRI8Jk92T3MpcZxU_3r7-89jpytjpzYyINohUokrJ0xJMQdDsvNHstX1-ZVPuzTY26Pz_lwkZLwAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=WUM7I5Lla7fZPVrtAq-zvWsC2SbhRDIQtouUMx-gHamjFu7gXfir9iKHtyewNTj8e_z32tr1MMTx3bsJyxmIFBFsvwgiL1BrXbx3997vkpBrJDlOrcw7TUkUZkWjDxw7rMxrI_-tdTYVQL7blYc0kbmBtH4m5GkeW4v_oiNMx6pLJfhk2VrpTbITcLxk5x_7GWftRjtQuFKkZlPrpOx2oQLUEjEcN0NcM02kxdrvVDI0G2z6UA2qQpDKAlZXIeZvdasF5YtEjdzgE4OkymLtAnxKqa3MFHV-2YggyWTR1Y7LGZNWwDfBBKsQmup79z-oS2UPvdx-vGgBUpNLGhPNKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=WUM7I5Lla7fZPVrtAq-zvWsC2SbhRDIQtouUMx-gHamjFu7gXfir9iKHtyewNTj8e_z32tr1MMTx3bsJyxmIFBFsvwgiL1BrXbx3997vkpBrJDlOrcw7TUkUZkWjDxw7rMxrI_-tdTYVQL7blYc0kbmBtH4m5GkeW4v_oiNMx6pLJfhk2VrpTbITcLxk5x_7GWftRjtQuFKkZlPrpOx2oQLUEjEcN0NcM02kxdrvVDI0G2z6UA2qQpDKAlZXIeZvdasF5YtEjdzgE4OkymLtAnxKqa3MFHV-2YggyWTR1Y7LGZNWwDfBBKsQmup79z-oS2UPvdx-vGgBUpNLGhPNKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=Wqb5BThX0ETGYSxwfEM9Hscbrmim2iR5plT0mCLBbmlq3FpoDwgTtr7tBe7E1-4z2XJq8JnRMrp9FcUPgjnEgchBnRGvhzkPlcFrk6Qr6-x-s1qvL5KtHdgZP0IQJMGbTQv7SLzFJ0SiyH6zNUJgmYge9zUWhWzOR5EUOD9k_AqWB3CNylZF9UWNraMRSoH4qU0bJTBw19VtgVwkuE7OmMQdARNGtnSTE_-_mAUGefHnlw4iBfDIuAcLWPCLIkDO6HFEVe6m5AujYdylvAIAchFNCvG7ftlNa2VgKj1QZUcH_wNIs45hzbsR9kQMvVKXLkfqRPZIE0Igr06WRxMjDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=Wqb5BThX0ETGYSxwfEM9Hscbrmim2iR5plT0mCLBbmlq3FpoDwgTtr7tBe7E1-4z2XJq8JnRMrp9FcUPgjnEgchBnRGvhzkPlcFrk6Qr6-x-s1qvL5KtHdgZP0IQJMGbTQv7SLzFJ0SiyH6zNUJgmYge9zUWhWzOR5EUOD9k_AqWB3CNylZF9UWNraMRSoH4qU0bJTBw19VtgVwkuE7OmMQdARNGtnSTE_-_mAUGefHnlw4iBfDIuAcLWPCLIkDO6HFEVe6m5AujYdylvAIAchFNCvG7ftlNa2VgKj1QZUcH_wNIs45hzbsR9kQMvVKXLkfqRPZIE0Igr06WRxMjDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=RFQ7PkzFukVZgOm7iP3bbnT24syThewG4MsuaywxYkF-QBHYHuztNHxjPQAxt3CYnfz0_Z2TnERFiVTXu7MxhfE_3Jt0OhUbpgRMw3kGqB93vCICme2nWjsYoX1WSRbnc_DrX7Lgogt5_6nPzmfDIOoRr0fU6sYFqrD48gbONBgZ2v7h6HBWD-_cPp_qvTJCBYMQOvQo3rT_pnTo8XbhKGf4UQxQyyeHLp8dGoiUq8-QfjYkPuRyyiF1rYwiRoEuXEKGHCrk8jKrFr2SlMYyWRDIBYpuYmiW9hwdjNvumgBLCC1uKooOZxM6OY74pC7_v9bgCbM_RZ0wDx-nDErSdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=RFQ7PkzFukVZgOm7iP3bbnT24syThewG4MsuaywxYkF-QBHYHuztNHxjPQAxt3CYnfz0_Z2TnERFiVTXu7MxhfE_3Jt0OhUbpgRMw3kGqB93vCICme2nWjsYoX1WSRbnc_DrX7Lgogt5_6nPzmfDIOoRr0fU6sYFqrD48gbONBgZ2v7h6HBWD-_cPp_qvTJCBYMQOvQo3rT_pnTo8XbhKGf4UQxQyyeHLp8dGoiUq8-QfjYkPuRyyiF1rYwiRoEuXEKGHCrk8jKrFr2SlMYyWRDIBYpuYmiW9hwdjNvumgBLCC1uKooOZxM6OY74pC7_v9bgCbM_RZ0wDx-nDErSdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2NT3cN782BX-KJfBtIhRIJ9Kb6otm6DfBoUWGARAGQJuAz2huv3eO9Jg0QLEruxZygyhNXr9nCYfct49B20WlVUO5DZLxQqPwK1sBa5lonA38g0UtCCa5Y3pcMKeI41aljWMDdUNOwawWO7gAz0dE8s09S3O8d1p2cZTkDgbfffjimgN8tM357fjbc-ZIiHhXLYqm-0oWaXfdJ7v_Th4a1edjgkIEPQ-Bk6LU56TsT6vlMq9cf9DFPoDPOonvSa6Y6x0dccfAGxZ-oOEuiQT9xT9XvwmfNaKWOmn3aRo_TRijRghmjVPbcfNNSmYPWlcqo3TpuSqR1MRJtYRA571g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y26GZQA57685tGLkQDs4JpU9p45HdSHtPerEeYt0VL5wtmFSIEvaDf7vsjzNETksWIKFLfUBNBG_535MaBFXfNXLkgZUSUHsU4Lo1gBuipWcb5FsoYpnewbP3Dw7gZKzP7XQGdg5IGM0UGVBOBtK8cPZ2bbvP6zM0jBfbtgN-F6yWG6smPbb0FfbwXY400OH00-39uUh3PUbbPYbRDSad48C8fCQLfjlCWwNHCJLyQSny7iV-ULShrSM1tAr022rpPZtLb7dakj_rQVzZlXH7jbnZaCI3bU0rryiIIUBX9ZQiFNPOy6LA2GdD0hFKfYU3AjTolRCoepkipHl0Zme9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjOuzUdseJd0wIUfLka2x3zu5NQ4AqLEms-IRaVWEdGmCu9HA4QQrjUXqLDjS-5GzymH0XJgkYbaj6bGWPUuqAMSJDG3fmdQqJ8_4OwKsrw4ubGZed8VhNJD4onmY2oVnDCMJgGzZlumhVAMDlA_voYQlvUXsUY8_1O5f5XuBoM1q_CsObyWm5B8YnK3AgXoU4PS71BRu6j0dELPZeEqu45rExi4owdZFaIcd5Nyqh3ai-_T-bbyo9J8aVqDqoJU5kwR3bkE2yx-zKVSDwckp3cu-gdedANBtGCxWHsVrzRKBvSo0eBaiU15rEJPpEGgXHHj92Rd78edz9mPMSDBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9mVYMfAF1O-DVSd_DXJoTtlD-7pK9SqCvEoD9tVSyevukt3HInnqFHVgk3MxVJw7EUJeK-xBifRM5a1b-5UdNQOH1bEHwudI3bLaFZSU_kHGL6rj0zlLomXN_xfzTVVjvY02Wt252HFQj5scFx3nG1NSFsKCr2oTI9lZfrRyWVRJ4cHYxOmHCUkTST1EqopuC_V1EmGuevOLIMDvjF0wuhBkqG2GdA6wWWcmp4p1T9fYb3WcJBnlIszNXbA9U_iHEzlQQ-SxyY7TU5Vw8uaAqFes6paSM1WmXUp8f5BDjAXJ_a37AmPx3TIzQTPFuwMBPi_8aJLSeEH90iac2Gcqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=fUyReac-pSCo8myY8v9o7SQXnVSKoYn8DGhA2IjRZ_T7j3GjqQmfoDYiTY-MELPrbmPA9SGYKObkiDSqcpDjJCUVpzGnQ-GVzd9J3r5g8MynrVMUxwVTqxrdwd5dNbQUuckOMRhZNdNQqSXlE4THkSmn8YK3Lcs4iTcqCVfhxyIlgAvqfTopF7P-r3PRBUjDd7zWFuwA_uEABLc2L3b-lwKcNT569vtCXmDA2JklgRoi5clxj0PXt9VHKYAYgqGnfRT_sMMzr0sxuyERGcLjEutTyc0AcpTq-8eM2Obq5oSwom2fhPyEUPAo3dQnVAaAfJRinw4ssv0ZoBgi-68e1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=fUyReac-pSCo8myY8v9o7SQXnVSKoYn8DGhA2IjRZ_T7j3GjqQmfoDYiTY-MELPrbmPA9SGYKObkiDSqcpDjJCUVpzGnQ-GVzd9J3r5g8MynrVMUxwVTqxrdwd5dNbQUuckOMRhZNdNQqSXlE4THkSmn8YK3Lcs4iTcqCVfhxyIlgAvqfTopF7P-r3PRBUjDd7zWFuwA_uEABLc2L3b-lwKcNT569vtCXmDA2JklgRoi5clxj0PXt9VHKYAYgqGnfRT_sMMzr0sxuyERGcLjEutTyc0AcpTq-8eM2Obq5oSwom2fhPyEUPAo3dQnVAaAfJRinw4ssv0ZoBgi-68e1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCMsXmvLM14bxSavHWNEIXo3QwwfzRl8UCmrxxxBHk1ijpV6Rj3IlLXzLQ_LlvAuTVjnixq4H3BDj9atFxq6pmBaJoUeuZzWDv60Okeob7AO2ya69fuzh4ZL6h-8eCPnhTgW9bcN0fgoEfIJf-yIpwSpJYdiqBJgKt2qVf8kG7BbJSYFMgb43C5vYxc50eZnkVfx0DOBLWtBGVYnBEaDxYgbQV5125qMr88VS2g5pzj9VkJ9_KUr9WKTjc0X58FKyFkcJsP0f9ZUotBEjDZv8x0tzKsJ-1RWf9Lxb7B2QeYGDSAYPTOjCndy2dHpcoyVXKemSfQIIQVK4HIJEP4vfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=PT29Sp_r7mwkjFrxATlC7tP-dCYj5c93awaaBFftOrD5vd4m5qkUOYvSPWuuvtoODmI1d15VcaIHKVGcH_9tRy9egRzbRR6f6rd4U_ahv7Y0GTDhIRyMZUJgallfpmTLcQmviKW9EmQKQRF8Rxtb_mI-la_n5LeXkPFowSLMLMAIqbw5SEF3yxIMOFdcWo67Za_oXXPALEcAaLEO_6BdXU6_uYtvSuEIBWYI-PdP8nBarn18agYVHGUWIKP8tV9agdG4DGSSSAMl6lqon17iWNOzDeQk3dd6zrMakmuY-4dF8p5AvAPACfo31MFpqKZVcV6Lol6bD1XKtuL_UM9fTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=PT29Sp_r7mwkjFrxATlC7tP-dCYj5c93awaaBFftOrD5vd4m5qkUOYvSPWuuvtoODmI1d15VcaIHKVGcH_9tRy9egRzbRR6f6rd4U_ahv7Y0GTDhIRyMZUJgallfpmTLcQmviKW9EmQKQRF8Rxtb_mI-la_n5LeXkPFowSLMLMAIqbw5SEF3yxIMOFdcWo67Za_oXXPALEcAaLEO_6BdXU6_uYtvSuEIBWYI-PdP8nBarn18agYVHGUWIKP8tV9agdG4DGSSSAMl6lqon17iWNOzDeQk3dd6zrMakmuY-4dF8p5AvAPACfo31MFpqKZVcV6Lol6bD1XKtuL_UM9fTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTX4PVHt1Oy-JwJGjlEFl9UVNbn7hW468G6Qn4R3y5qEkpRby1CVe-K-V1jNv3bLfcx9_MOWRIOpJcy2K3cZTsO2eKGB-WlqNYOrq-EqH8q2OHxPMIMXium_twQn7HGx7U6YbUPFwW-_uSriuFfXWZUXcBlfXiOGaDrYzCew1CEs71p1HxGrZOBpAAkhbf1NOqfmpG7pSjy1hLPJfn6E8Axo-LTXsZLIhuJMF9bM9NK8eE1XO6feBeQyrwxzrRfI59whq1PpoBNqc1DolAJCfDVEkAsw1lGxJoNHVJebIA79EleFqiDfoVZ0J0HeZ_g9E16tEUEBtgDDd7Hwn3rv4myk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTX4PVHt1Oy-JwJGjlEFl9UVNbn7hW468G6Qn4R3y5qEkpRby1CVe-K-V1jNv3bLfcx9_MOWRIOpJcy2K3cZTsO2eKGB-WlqNYOrq-EqH8q2OHxPMIMXium_twQn7HGx7U6YbUPFwW-_uSriuFfXWZUXcBlfXiOGaDrYzCew1CEs71p1HxGrZOBpAAkhbf1NOqfmpG7pSjy1hLPJfn6E8Axo-LTXsZLIhuJMF9bM9NK8eE1XO6feBeQyrwxzrRfI59whq1PpoBNqc1DolAJCfDVEkAsw1lGxJoNHVJebIA79EleFqiDfoVZ0J0HeZ_g9E16tEUEBtgDDd7Hwn3rv4myk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=fjJ5FMC6hYAwVw13_jRk2xvXluHF5Tfx0BLsdt8Ni17dj2dkqYsm0kb0oo_y-y-rV1_QxBcghKpeexeiVdUPTOxhyQkjU9rGq9mHydeVXXF-IYW_9Luf49WZgRTvOGMQuYJE2xXPvZj2VSo43HEESgrdtHlCnMRPCBNDsi0-2939Lz-i-hni6XH08Wl5yPs3uS3l-3YkOqmwWGVgGD5C9skpdvspDkZ2-v2H-_C8xxr9CpMMHQIjaZyvNhrZ9A3M6tcDmBvcb8n_0mlb3hqxAs51mqLZAOCI5kdAwjV1jA64b5TS_dTuD0lUlR8ooNCHIu1lIMETppBfFvlx-MuWYBKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=fjJ5FMC6hYAwVw13_jRk2xvXluHF5Tfx0BLsdt8Ni17dj2dkqYsm0kb0oo_y-y-rV1_QxBcghKpeexeiVdUPTOxhyQkjU9rGq9mHydeVXXF-IYW_9Luf49WZgRTvOGMQuYJE2xXPvZj2VSo43HEESgrdtHlCnMRPCBNDsi0-2939Lz-i-hni6XH08Wl5yPs3uS3l-3YkOqmwWGVgGD5C9skpdvspDkZ2-v2H-_C8xxr9CpMMHQIjaZyvNhrZ9A3M6tcDmBvcb8n_0mlb3hqxAs51mqLZAOCI5kdAwjV1jA64b5TS_dTuD0lUlR8ooNCHIu1lIMETppBfFvlx-MuWYBKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vvL4ogXVg4CKP8I5FooN19EEBeVktVU2o1AUT0NUXXAmYsVYOq4EijPL2t1IM52kaxVYSA0LwixdP-2WI0XgL5rhDE4uETITSDAOor1RpfxlnDWGDBlwZBXPoggJo6j5fkKTAg9ReS5n93jZ4a02F7z4XnXODtBFvvffjU4dk8OQwGKfFGZWzzoHdd_aOg36jUx5t4LYKtiMz-lvAZh-9r8Khm24YmGck0hNeItTSG3oEV8VcDnWAGalKCFpaNUhL4X5IdspyB6QpxKAN_o5Vl-IDCjpR2VAfXjIz3Ocrefx3zuGvUvU0Dau0QxJ3-c8iinO-jSye1VC2NKU_WAXoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vvL4ogXVg4CKP8I5FooN19EEBeVktVU2o1AUT0NUXXAmYsVYOq4EijPL2t1IM52kaxVYSA0LwixdP-2WI0XgL5rhDE4uETITSDAOor1RpfxlnDWGDBlwZBXPoggJo6j5fkKTAg9ReS5n93jZ4a02F7z4XnXODtBFvvffjU4dk8OQwGKfFGZWzzoHdd_aOg36jUx5t4LYKtiMz-lvAZh-9r8Khm24YmGck0hNeItTSG3oEV8VcDnWAGalKCFpaNUhL4X5IdspyB6QpxKAN_o5Vl-IDCjpR2VAfXjIz3Ocrefx3zuGvUvU0Dau0QxJ3-c8iinO-jSye1VC2NKU_WAXoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYSRwMuA4owrBUy11_F91A0-NFX2S9DKxcjH6Rpi08pRepfJdIFPniEN_-YIdMmH43bYTcAyPXY50fD-d7KcWtEupvU5ylzoopGI2tqq6t5dfm82HWHlTpbn9FSvZBnz0oBRVCcnxwVHBXjQ-V5axFsgsFbtW-71HYMR85Krn0ijIKbN91h5BspIm6OewsovN8JpIKjvuTLisQXKcamwwmDNT7mzwE7-wEq7fenTaDYb3qT9kWrbTq8tU9WafRDj3jPJoYTmDXzNDejhMULUAcGRV5tEIzbdu-YYUJ4Fn6s_dyaTJE_6hUhH1933O_0ZA0oK9pgaqhScNWK5PjBq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=dxHf-S_34taCbjQYaAzyXP0R99pdh_WTcG_-j61sAxT1Nw4cVkUuK8ScDySNCxCz-mv5EEvH9xPyOjb_TIk-GJGTSTr2HCNBhO3PDpb28_d6OUJHWhcp2dPDCIG4q1sqXUvW4lNqavK3odSPpkP1DMv0YLTb0TgwvYkK0jdGZ4sgmHNThNQnHUsFcrcoLzxA0duZ9IWL7mjc_zbpBx1N2HP4CYzw3QStCurKlGqcJ_ZYIZuNH5vuHm_Oq6JUeFAt8zeyRR4cA7IYTLZWp_pbqfHLDhIKGU7c81XMWhot4FYG9SndZgVNkh5kfDME4w4li1Ken66LqR83_2rl5Ju9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=dxHf-S_34taCbjQYaAzyXP0R99pdh_WTcG_-j61sAxT1Nw4cVkUuK8ScDySNCxCz-mv5EEvH9xPyOjb_TIk-GJGTSTr2HCNBhO3PDpb28_d6OUJHWhcp2dPDCIG4q1sqXUvW4lNqavK3odSPpkP1DMv0YLTb0TgwvYkK0jdGZ4sgmHNThNQnHUsFcrcoLzxA0duZ9IWL7mjc_zbpBx1N2HP4CYzw3QStCurKlGqcJ_ZYIZuNH5vuHm_Oq6JUeFAt8zeyRR4cA7IYTLZWp_pbqfHLDhIKGU7c81XMWhot4FYG9SndZgVNkh5kfDME4w4li1Ken66LqR83_2rl5Ju9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=PL6OobCZfggWP04_IHLZwVqGT1Ov0B4EO0CMaQWVP1ghtyzjIxoOyJKHqEunxX-Oa6Xa-1WJhVKYmdGZGjI11nk4YkzW_dgNgwn00jiTYmQ2eLgWrenf2bXIexcnXBWfWrMg5pp_Sh2qmTuMOaSFRGaNMDBzwIMkoP95NdqFDjJsyGlaj-0ZV86d1q-_nqbs7M813WbEl8noaOCauOei8p2O5MFqFAEM3Gju3LsEYgQB-5Zpp536Jjj9fybOilWPWWBnS7dqoxkKNl0EG6AQAPsj-0WtkIr4Z9VmH235HBCF9Mz2Ul8lmml2jb46UdMycOHoy37fuhchPnN9wTujLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=PL6OobCZfggWP04_IHLZwVqGT1Ov0B4EO0CMaQWVP1ghtyzjIxoOyJKHqEunxX-Oa6Xa-1WJhVKYmdGZGjI11nk4YkzW_dgNgwn00jiTYmQ2eLgWrenf2bXIexcnXBWfWrMg5pp_Sh2qmTuMOaSFRGaNMDBzwIMkoP95NdqFDjJsyGlaj-0ZV86d1q-_nqbs7M813WbEl8noaOCauOei8p2O5MFqFAEM3Gju3LsEYgQB-5Zpp536Jjj9fybOilWPWWBnS7dqoxkKNl0EG6AQAPsj-0WtkIr4Z9VmH235HBCF9Mz2Ul8lmml2jb46UdMycOHoy37fuhchPnN9wTujLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=KsRjtF687aDo_1u3Bvgv8d4LXbbabMDEnnFiyl769szR5rfm5wVfIkVzUb-SRqWvZOp0xCzl7okKiDBLpUM4vuvsUp3LOtoT_xI1omCUvMmrICcy-6QCnrcKU64b5qmu6TEX0a9WPTwajJIC_TNXerqpDtsWzTPPiZYG5EQjkW0QPkEvTMWX2oGdruUYYV75X9ZZ8Ozp3Xf3Ls9X9oZlStWRSCYAei2LoCtHxkPvyt_I1RC5ARYnZ5neDJHo6QjOP5sFdx0NAue-orL2xHt9vVKjN6-9icUBnbwg6QzDyfcLPMxAzznIvVpHVOJ7hbTJrdbG3qr3H1kfk0yHz6Ag3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=KsRjtF687aDo_1u3Bvgv8d4LXbbabMDEnnFiyl769szR5rfm5wVfIkVzUb-SRqWvZOp0xCzl7okKiDBLpUM4vuvsUp3LOtoT_xI1omCUvMmrICcy-6QCnrcKU64b5qmu6TEX0a9WPTwajJIC_TNXerqpDtsWzTPPiZYG5EQjkW0QPkEvTMWX2oGdruUYYV75X9ZZ8Ozp3Xf3Ls9X9oZlStWRSCYAei2LoCtHxkPvyt_I1RC5ARYnZ5neDJHo6QjOP5sFdx0NAue-orL2xHt9vVKjN6-9icUBnbwg6QzDyfcLPMxAzznIvVpHVOJ7hbTJrdbG3qr3H1kfk0yHz6Ag3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HojDcdEF0w-NfHZMfl2WoH7QGz_jHyOhc2EvRiKtkHJNovVMw8LEhqg5_hVdcgCPzqQUMjX9gPDx9c4xtrQfotThRe_SLke-6kGrWl0z_kpZ0au3-mVrk9WrizMEtTKjh8LNqKmaDsIZfSUkbrkSnro8bKWLWxnEVbYfhthTYC8fg_CZDuR3pWnivSTdkwc2kuoPyCpgXYSQAqPeS-lyOoNiTtcB67g22atPBmXOsa84TxggAZXRI6syueLOG1OdZy4XMU_sMkmGCut74qxcxMJQhaN-oP7mxI8WL_5Y1J2Sq67iRdWM8XaqUt7W-eX0R_-DbIXFAyQufuFkBuZiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiWb2nzhCk8bu8GtCowZjf-JSC_p8RYNmPeSxqaJF7vtlqgCQGpBoGJqgabjLwqc-wmPBTUk9o8PEgVQls9zL9ccRexyE8dbTVNgU9l7zHqHBcsg98_kllQx1wJOFOy80NFznaguOb1RcFVFF0Ry8roKQ6n_ZNXnGF-rAKJ0VnhTzf6J-KTIEbEwSPghazIcu6iUlxz9WYUsPj4nDT0j6nNZ0lRab7F5_GxFxvGmRpbKa4Eul7I9PGferIN4USf9cfvzwHuB6RJ4xk2nV8kvZFWkZ3OMmuf5eEybNgHmeuvk13DkgwfZSH-KcefGRleoK57Z8gfhTkSK9DxAZmRbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0lkDxlQmfqnTpL68uVfF_ATpsbTa69YNZTfgi__HNR9YsYjjJdmP4roCI9WFYQ91q229cCy923fKAfOxmfQM3DUUBEIwQUNN9Ogv5Je-n8MTscIH_XkgVVbcsSefLqjDTtphvbfe5usefichxVENe_E4HjxpXyn3PtZYQAL_-tupWiO3TNFRWa_hfffezVU2O8vHsznousbqThso36lTXytx-_w-5_wNC9ackOVIUzcx7P3dv52JFZH3vjjDobzXAeiu489NkIihXNt6CaA3Fll6LV8Zv5xwcHV1X3WmyioyJoldeF1CqKy4wDHs9nzEJ6sv2RPMiF3nvvwnsc43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2fKZlLEzmdOyf1tV1-Blk1Cqp_nGpSODsPWvD8zekas6SwL5xhrqZ5uNgOOreapt7zSAg4N-r4dSpDEsPCmr5FAFBFOFAZmPHmvH7Y4NVrtMpy8U_ViHm5xv56O9GgKP3F6Xj8HXTf6VtIpfQD9gInbkS6OS9mVSbP3n8bEpUM1s4WgwNCHoXXIBTbce9He60b0LSAUsk5hNXOtY7p6io-ttyveHXs656N2QxlFqSJ-uKqtPZMbrNazVLA0awY6JC7b1JcaMQtDw513ZsDJgVXDG18BrePEFu0kAZRrdd76tWeAHZBErjKAyU7a2fJ4220Brcn3PdXwhNAVdLOEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rE2G6BdNYZN9rUMnbtI-BAB2TCUhu0mAqIcgH8_xGqp-jkYnR1F58DZkQNn2d23_jTZhZ5xD8ye49l6iG55qzacPXu8S0mH85hGgJqFHyyRuzhv5KyXb1OXqoakyLc0koMxGAePid4hCDjhRS_JwsoOzbWfnM9TLNpBQ1W5ATVYKi5hkC3CHCcJQQQgQcMsXCFqLaMqWRr_JjctsdgLRw-Q6Plcage7zxROcCALmzkZBU5kUZxpIkwYMcV1Fv3AbIGGQXh9dscA24DUoRJPiOCHk7zofbk_YinaeO7KOkzGExpnH3uz0rnYXOWtdD7Wcy2IyXsQekMWCLFL4DRgJHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WXfmMLwn0l9Eo_91VgC28U1A0Y1NAm7VjdW7hwUlu4l2d9GRmwU7ZWL96GI71lVDaZ1RSM4ZcjEf3Wd1FdFCuxr7cLKutsIkshnpkGpoS7TI1DC7d2GazS3K9uQEvYql1ilSdBto9QHi8yy81yE-ZIr9LmFadwmVaR9xRBzMGmOv3vfQKNXesWDN7m2QLmUHSY9wwDjCL3OIREgkJd22KuxD5uO8OD5-X_BBRoNnaANvsdFi84UzQJoak74-QjreF_wAvZoDu2Qr7DtXGlVeF0WwW5h6FkY3cVHz1_CStCw70nO54Slrl2pKSG3r0qbUOouRVVpgRd4dPvwlW7mPoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WXfmMLwn0l9Eo_91VgC28U1A0Y1NAm7VjdW7hwUlu4l2d9GRmwU7ZWL96GI71lVDaZ1RSM4ZcjEf3Wd1FdFCuxr7cLKutsIkshnpkGpoS7TI1DC7d2GazS3K9uQEvYql1ilSdBto9QHi8yy81yE-ZIr9LmFadwmVaR9xRBzMGmOv3vfQKNXesWDN7m2QLmUHSY9wwDjCL3OIREgkJd22KuxD5uO8OD5-X_BBRoNnaANvsdFi84UzQJoak74-QjreF_wAvZoDu2Qr7DtXGlVeF0WwW5h6FkY3cVHz1_CStCw70nO54Slrl2pKSG3r0qbUOouRVVpgRd4dPvwlW7mPoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMRdm9sHIafCbtUw05mE3iT1Q8I5zA22rCyGOCqP4r36FRUvlwdrNdN0ZOq8PHwon2LTq4Hpncy01muaD1a1-bmNUHy0iQ2il7gI1YRFAS2gpeUHcr9uZcCMCNNcMEuP_d44ZB5hdRQA0Gl6nEaq-odfYyJafitiI6F6GqAAvVZ5WEDmQnY7VmIWhAluvF01kpBclPHLaU5YQre4zaUOxeiaq27vBhqz23Cf9f13n8_FiqkHkXGFuBJVOwaBjTKhEgpeQFiS7PuAV0_hFp4vtoPmwOJ7rTkRVvLOMAiHZS1dOQkz-tE9yKvpXaY0rA1_pjN0ftijRNXX8Rw_30I-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqxW6mYs3ShVDzgoOxUXi5AzNPt16JgmQIhswYcfTJnHFuxdjasGOuqiT6KeQnbsRunnUKXQ3QOs-WuAPmJdSDZrmK4XW_Oac5Z-VCEjd-MzaALOZyhMjFRV2MlblBFV3ui27dQ4wh5s_sfc7gB-g8gVJ_tOYgVD8mhE37K1HjNwL_jjAkyx3nc24i3DGtPFppYDQIXzEOeCefVwXTVBo48c-QJk3uQJGJxXLD1SpKXyT-6dguNF4irJg38zuB4r2_lxijbJ7QI3QvLoHevErYo8t1d2dgKVIC35BqKNNFEf9CAmmnxV_QAD6ufcKyqV16ge1tqui0jaz3uo0gdzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBc_Sr-lvnKfrnSSQRqSKDwUQa1JoPLUr148YagWebdhcQHKfep1BdPw0APFLdt3bDkXoxN1NaV2D8P3ffJi5oIl3XBjddHrUAXvpLh0qrxQIeRMq1EM9N7KPUJP4moO4vhKUqKnsO-TMRcR4QAwZnDg_Ppzcq-wb1ioK_A_8ic4CLUL6bSIFa-eCT-wpfbb08hFDuA4juvRZr4tqdBJWNZ28PuyG_9GES1dc4tnH_tIhCiTbB2E-5cvfZeb6AT3mQ_rBXRBShHdVgJKrFrUnWhVtQlwM-T3U7GgoiRtL6gIuENXpKn4pCG9Z6e6SPE4h0YxSto0n8BYGZmbv9hjmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=GVPC31tjmT1QA11ES_W80M3ypAezOvQfhDA8b2-WR6_JOECPR96jHLgymAnzLtqbivdPbh9l5epjHXw-EHfiyakRv8WLDaTgdaVFBKM-frQGj02K7sRxnL14V6KapnF4-2PkbBJnKk1rDGnmeRdLRWW5yVHraDlKSME4Rr1LHRuTHdcgXL_hX1oCCgctWzQ55H1CzSEs-ssu_VLnE1Shs3qjcjOdls3s7MwHNovfhstInsAdoS-gbwbzJQW2SjAV1Gal4K6WF7fd4HFKoOBELaLvyGgPGsFyj7deBxOVuny_UF2Y6TuRB8gF0lE_JvwSMC-08XPXdTH-c9Zo1amikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=GVPC31tjmT1QA11ES_W80M3ypAezOvQfhDA8b2-WR6_JOECPR96jHLgymAnzLtqbivdPbh9l5epjHXw-EHfiyakRv8WLDaTgdaVFBKM-frQGj02K7sRxnL14V6KapnF4-2PkbBJnKk1rDGnmeRdLRWW5yVHraDlKSME4Rr1LHRuTHdcgXL_hX1oCCgctWzQ55H1CzSEs-ssu_VLnE1Shs3qjcjOdls3s7MwHNovfhstInsAdoS-gbwbzJQW2SjAV1Gal4K6WF7fd4HFKoOBELaLvyGgPGsFyj7deBxOVuny_UF2Y6TuRB8gF0lE_JvwSMC-08XPXdTH-c9Zo1amikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=CEK5UP7gxDk0F2RFRoJxNjTPEoYNWdoZVlmtupZ-t7hCbC7GdALQkKCGj8TpYHdobiJdBPecJqwPPfCnQ77rFK3OgvFnYfFqhJwnkD_AQKYZo0aO8WY-H8hYaDz88Q-K6J7hxAAvuT4lIiTOOWpHayL7Xdcq1LpAMk3CKeaV10DKllJuK8UreZ602OYkO1XCXRS4RmUgwdTaUFC54wKb6cXxWwJ01OrVHNZzXC7OcxAzZTJl4osTpuKuLUHSOvi9SBef9L8vAhgGv800tiT2zVwRpB4MImMmc4EmJNLV-DkGeeDZ6G3UsPMUg4U_W2jrKJW4f_5TC8bvFCkgpBX1ozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=CEK5UP7gxDk0F2RFRoJxNjTPEoYNWdoZVlmtupZ-t7hCbC7GdALQkKCGj8TpYHdobiJdBPecJqwPPfCnQ77rFK3OgvFnYfFqhJwnkD_AQKYZo0aO8WY-H8hYaDz88Q-K6J7hxAAvuT4lIiTOOWpHayL7Xdcq1LpAMk3CKeaV10DKllJuK8UreZ602OYkO1XCXRS4RmUgwdTaUFC54wKb6cXxWwJ01OrVHNZzXC7OcxAzZTJl4osTpuKuLUHSOvi9SBef9L8vAhgGv800tiT2zVwRpB4MImMmc4EmJNLV-DkGeeDZ6G3UsPMUg4U_W2jrKJW4f_5TC8bvFCkgpBX1ozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJy3-6qElq1VUS9Yk9F_0NUXk0kidQwVIyrNf6AY62qiBogmLFmI6ITuIE-mwFnwJirBSEYvMzO9T1jtQM_qcj1u1Pg1kyhIFb-SLN9UdMzJFJHrrvbFK61a3u7u59lOAIs0nN76s9AobhqR6ta2HSoUvlfLTIlDYxRsmY_5M-U-KWV6Md6Fz7OnMoO3tJZHOR_oGlWh1rarw6bDp0ns-_FYjnmuzmrGuuEma2RCxJ1agW2qzwqyoVRDd4mKkYBm90y12Dad1pr8Qrbsab7gGnn9Vz_oNhy1vArqkGKyAZeaYO34TGPBC_gZtS5bU9xCM3ZjTLHrDulwcG_r52g1sc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJy3-6qElq1VUS9Yk9F_0NUXk0kidQwVIyrNf6AY62qiBogmLFmI6ITuIE-mwFnwJirBSEYvMzO9T1jtQM_qcj1u1Pg1kyhIFb-SLN9UdMzJFJHrrvbFK61a3u7u59lOAIs0nN76s9AobhqR6ta2HSoUvlfLTIlDYxRsmY_5M-U-KWV6Md6Fz7OnMoO3tJZHOR_oGlWh1rarw6bDp0ns-_FYjnmuzmrGuuEma2RCxJ1agW2qzwqyoVRDd4mKkYBm90y12Dad1pr8Qrbsab7gGnn9Vz_oNhy1vArqkGKyAZeaYO34TGPBC_gZtS5bU9xCM3ZjTLHrDulwcG_r52g1sc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtnqc_UF_8pUvNGl0OPDGu3Do9xisn_rnUkZJlHsBmYeS_ytvpOoyYPItyyCI89RS1p6MRlQdRNL1ONWY3yS5bcIwgH5lpXyFKfaM_TxVYkF8LvmRg6V4E507rqw_s1p_JLLagRXQ7mxhhD2Cy98je4CqpWQRVHW7mGaS141v9Q6KjzHzq0trccy5V33NnVwk_f8FYI_ers-P8zImImpd0NyaTu9EIeFRycmclOjoKUG0KGogj9IJ_K9nSnn9ELYRYB70peE-OH-v72rjGxZDifZjn8xlRUA6Z0Zw7oEz2i3ELCE06qXh81UkWJWIYpopIXXrr2z-XUAJ4ZTyGFHjHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtnqc_UF_8pUvNGl0OPDGu3Do9xisn_rnUkZJlHsBmYeS_ytvpOoyYPItyyCI89RS1p6MRlQdRNL1ONWY3yS5bcIwgH5lpXyFKfaM_TxVYkF8LvmRg6V4E507rqw_s1p_JLLagRXQ7mxhhD2Cy98je4CqpWQRVHW7mGaS141v9Q6KjzHzq0trccy5V33NnVwk_f8FYI_ers-P8zImImpd0NyaTu9EIeFRycmclOjoKUG0KGogj9IJ_K9nSnn9ELYRYB70peE-OH-v72rjGxZDifZjn8xlRUA6Z0Zw7oEz2i3ELCE06qXh81UkWJWIYpopIXXrr2z-XUAJ4ZTyGFHjHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owjWa2c621myK9MLtNdmeGupBZFvKk6STRWcGgSgiPk6TAiBKWsA3N6UrQtSzQ-tKw9rcfZ_lAi1tZIkJJD6Rleezbt0KAHI78yB-7Q1V1zNkDjA1Ob9tGQjKBDia3sRAkZgiyo5iPK9RXusBKFGaZBA0bBOUsv312mL7P6diSyn1Gf7z0S2QAdNRoGfvshx9jF9naijZ1iqi2aefIQzFLVa7I8OT9C_QbtcwbH6NhbWptEKiNHhQIS1rQsCZHU0IVQbPyluCuaSlrSn5wIqtEmF5qGO9xgFqjZLSoZmXh88oTSqA5_dXoEX2nb_G6SM2osvmq8bF782m97-nsltQrcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owjWa2c621myK9MLtNdmeGupBZFvKk6STRWcGgSgiPk6TAiBKWsA3N6UrQtSzQ-tKw9rcfZ_lAi1tZIkJJD6Rleezbt0KAHI78yB-7Q1V1zNkDjA1Ob9tGQjKBDia3sRAkZgiyo5iPK9RXusBKFGaZBA0bBOUsv312mL7P6diSyn1Gf7z0S2QAdNRoGfvshx9jF9naijZ1iqi2aefIQzFLVa7I8OT9C_QbtcwbH6NhbWptEKiNHhQIS1rQsCZHU0IVQbPyluCuaSlrSn5wIqtEmF5qGO9xgFqjZLSoZmXh88oTSqA5_dXoEX2nb_G6SM2osvmq8bF782m97-nsltQrcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=IYIanX2C_M-iFnQJhAWOsgbzIxg_bZFI-70icSwlPDRbJrVT5pzGQTRjcNq-iKKJaxRk6oQjLpSJEgRoG3U3LYxbk_gmL7w0V5V5PpUTykz84XxFtedeuOMGIXgXyPFXH1OKkNBG-6PxSQyn6mjT7Iuu72SkGPluTpw7YuDmY92sJdza_FwbuOnHBpEd7HfU7MkD4ExuLYWDMAMOiwsx2xWpY5ZfJExu11kGSxVIncT2JCz05evgDdEOYqgo0DeCUXxM9AxpNNv0kgifmaUX_hwcsYX8c1LNUuyxyplQ9irSucmk79SrMC3w3rJon06773JweOhFxzA7Fk3ySsBRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=IYIanX2C_M-iFnQJhAWOsgbzIxg_bZFI-70icSwlPDRbJrVT5pzGQTRjcNq-iKKJaxRk6oQjLpSJEgRoG3U3LYxbk_gmL7w0V5V5PpUTykz84XxFtedeuOMGIXgXyPFXH1OKkNBG-6PxSQyn6mjT7Iuu72SkGPluTpw7YuDmY92sJdza_FwbuOnHBpEd7HfU7MkD4ExuLYWDMAMOiwsx2xWpY5ZfJExu11kGSxVIncT2JCz05evgDdEOYqgo0DeCUXxM9AxpNNv0kgifmaUX_hwcsYX8c1LNUuyxyplQ9irSucmk79SrMC3w3rJon06773JweOhFxzA7Fk3ySsBRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=efVUD06qFMMJMudH5jJ9IG4nAG8kf3Qdja0e86rKjLHkoMj-vd43fLmXOqgfEtbh3WgsPf7ZXH2V0otxfROBaQcPm_n6YNwrjHdI01kPGN8GDogcKbXZG8iwLfAEg1hxIU4b7jT4AZmfYISX9uZ4g-jQpnYppGWYq9pTMktbrAnao5bUKCG-40UDEVz0pgdnw_tAm7t_fFimCq-08l2aGGUK0kW4g1k6_ZQqKPDeIIjTsMUimojUSRjX0pSicKxqH6ITSDKZqH12K2tIwrfEFSBzFKDjszrfyxU2jYsB3byfdOHrFTwAbwacGLL6SMLkDuyI4olRAqUCoSHxdrTB5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=efVUD06qFMMJMudH5jJ9IG4nAG8kf3Qdja0e86rKjLHkoMj-vd43fLmXOqgfEtbh3WgsPf7ZXH2V0otxfROBaQcPm_n6YNwrjHdI01kPGN8GDogcKbXZG8iwLfAEg1hxIU4b7jT4AZmfYISX9uZ4g-jQpnYppGWYq9pTMktbrAnao5bUKCG-40UDEVz0pgdnw_tAm7t_fFimCq-08l2aGGUK0kW4g1k6_ZQqKPDeIIjTsMUimojUSRjX0pSicKxqH6ITSDKZqH12K2tIwrfEFSBzFKDjszrfyxU2jYsB3byfdOHrFTwAbwacGLL6SMLkDuyI4olRAqUCoSHxdrTB5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=rMg4eJhGrQoGYVspsxWEF5RvGqlABdL4f1PuR_rFCFjBLY7ecFWqLjI00hvKSw391n0RKl_WBFOqpc3gmuKos13SdCFE5mDmYY_xpCkQ66gimtAaBPhwa_iEN3pDg8qOXW5TabGLFl2ko5viTWm8xdCLlk9mcFsUBsl3uglo6l0uAlrp40bWWxn30c5gHdcanJ5h9wxPG4B3j-sbbVCTFN02cIdiG1q6pAJmEuEQLHVRdlHkhBV1l99YDzDRaNtxyywmF0b8LXsjzflNbgcrlX5Bqkj8IALnc90x4xGE8NYgYqkW-Av3MZ60uuN0bpx7S8k6jwt1y-0cuy-nU41Rdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=rMg4eJhGrQoGYVspsxWEF5RvGqlABdL4f1PuR_rFCFjBLY7ecFWqLjI00hvKSw391n0RKl_WBFOqpc3gmuKos13SdCFE5mDmYY_xpCkQ66gimtAaBPhwa_iEN3pDg8qOXW5TabGLFl2ko5viTWm8xdCLlk9mcFsUBsl3uglo6l0uAlrp40bWWxn30c5gHdcanJ5h9wxPG4B3j-sbbVCTFN02cIdiG1q6pAJmEuEQLHVRdlHkhBV1l99YDzDRaNtxyywmF0b8LXsjzflNbgcrlX5Bqkj8IALnc90x4xGE8NYgYqkW-Av3MZ60uuN0bpx7S8k6jwt1y-0cuy-nU41Rdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccMkpKqCr3cofHo8J-YnkOMkXDQhgfj9JkpR5i97zQQxwUfNdt_53_nZRTmETeMP1Ln2Iqo3dL0fXpsg-4XdazTnROiYmrCggG3_rQerzOJmwspUeEMytgDMp8IlhEmO39uBdhbz0i0qidmZrb1WhiPnJUnzp4FZYsnPeQIw1yZiFwudH47gRm5YHN7k1UsORsDe__-9rhmtEvRSzWM3FeKJ71NtvH2ukq3dfIKyhOO1eFntq8NPDXIP3mG3MWs6oWdmYIOhxWoZasAEVdNdgyxudZn4sz9A-2LrgGBWxY2iHrelNVKXtHaJu_4pXIoPrXyEzzmHti6xrNLolOdr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=iQPB4dxYIURKn8OqrW0K0QcUq9FIuBqmC2ZDZaHWjbsB2SgdNFkBXMwjKLKfRIIcr9jhtmvkJzFqtQ-A1zF8VlaOJndYftJVtev7-iAjJaDQHKKnOF6BaSulLzOUJE2ja8Xnm6qUewPvCN8dbuRcXqWbsIP6wL3jdv_CX1nv9-phtNKfqNLthiqUp5btDTUqi_KsHcI_PrKMb5n7K2JlqjsHELKohXxiWCpzXZ7sdSy46DfLr2O4YHA4oq8ojC7priUhbFdFRBHvOX2ClFJcqRLNC85UQH9UVNgQK5ynGQnnPVrJofumbyM73QqFzlDToj9bn7YEuw4TQ8trqMnYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=iQPB4dxYIURKn8OqrW0K0QcUq9FIuBqmC2ZDZaHWjbsB2SgdNFkBXMwjKLKfRIIcr9jhtmvkJzFqtQ-A1zF8VlaOJndYftJVtev7-iAjJaDQHKKnOF6BaSulLzOUJE2ja8Xnm6qUewPvCN8dbuRcXqWbsIP6wL3jdv_CX1nv9-phtNKfqNLthiqUp5btDTUqi_KsHcI_PrKMb5n7K2JlqjsHELKohXxiWCpzXZ7sdSy46DfLr2O4YHA4oq8ojC7priUhbFdFRBHvOX2ClFJcqRLNC85UQH9UVNgQK5ynGQnnPVrJofumbyM73QqFzlDToj9bn7YEuw4TQ8trqMnYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HXMrmEl26zM5qx-IeIyCkmOcAPWpchJOXQYn3-H54Lgq59qqGQsoWZp20pDSZ2T7I1xwPSRIYXCyklUwTMsfDfT3YQ6Mi3AN4T82eBGZ5cB6Yjn0IFsUIMAL5D0fn6ONvigphwcSMwVBinD_9JEqNJXR1ivpaQGDXIDYd3j2mjOQfJUcHS2d5-wkjounG96JoHyorGpdmzJt_gFWAwa0JWK_CKAX8VXsfVNwNNHWdfvPU7jhthWJ1uYWAypi780HEJbdZC7j59cyc2DlUwS4epgzElVFifvGxPjBGeGl4ZDuupOeZ22R5_DEbEarxeOg4hzyfGeCuuCE2q0Mcb7vGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=bDNbumcc4DFE73nI44egZ2Ek1jfmcdVi-ht9r0a9WPIjgQury5vY-reK9bl9fU2mfJq6ACdtDDjgkzqr7DwGb5Dp1Q8oDwUQSJAeDr_PLzdHYebuYqQgocp5ePRCHOzgTskOlzeQLd3QxHbDa7QXV_SOXdg8khRutOYbPwhBp1W7t10l0gFF_lT6kX2TDqLqSlMaQvEGXrqvznXXbRLK9I9f0QxqaTk-etKiS3f8c-4-5ap2decOsm0e_pyZro38zzfe5UKA5yspINZCZEdaDH-nf4jvVxy9OrSxs24ikJZyekBqwiNHsw9Ynh0z1ZZFPTVK3a6A6d2j80PJXJqc1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=bDNbumcc4DFE73nI44egZ2Ek1jfmcdVi-ht9r0a9WPIjgQury5vY-reK9bl9fU2mfJq6ACdtDDjgkzqr7DwGb5Dp1Q8oDwUQSJAeDr_PLzdHYebuYqQgocp5ePRCHOzgTskOlzeQLd3QxHbDa7QXV_SOXdg8khRutOYbPwhBp1W7t10l0gFF_lT6kX2TDqLqSlMaQvEGXrqvznXXbRLK9I9f0QxqaTk-etKiS3f8c-4-5ap2decOsm0e_pyZro38zzfe5UKA5yspINZCZEdaDH-nf4jvVxy9OrSxs24ikJZyekBqwiNHsw9Ynh0z1ZZFPTVK3a6A6d2j80PJXJqc1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqRgEQSu3f1l6HepJ7uq20dDHoB4BIZB7clf6n8G0tG1Jj3wjgnPxOLufY9_3fOBhTf0U3hGa5JkJ8QDg0xmmSRuAwIpWpoIZ4XW8UIwnDVD7K6TcQ53FMXvK1PyppNmRNCr2C3KXH_ukBSfPCDgnN41w16Rk_ZKqH5zWPj-WuOSkqkRslrs0fwf8lUcAG8AR5pyrR39qeRdvJ01M5XGOPrOLsTFmTgMY2K99E7G1lPqFFGfElqgxIcfEH8SIWt3IYtokXdsvdN6gMv228zZDqUItOPSgwXl8C9Twrb8-E89pD_5bu_4Fn5Qs3K0a6slh-Mt0ff1Pvrnlh66Ey1mKJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqRgEQSu3f1l6HepJ7uq20dDHoB4BIZB7clf6n8G0tG1Jj3wjgnPxOLufY9_3fOBhTf0U3hGa5JkJ8QDg0xmmSRuAwIpWpoIZ4XW8UIwnDVD7K6TcQ53FMXvK1PyppNmRNCr2C3KXH_ukBSfPCDgnN41w16Rk_ZKqH5zWPj-WuOSkqkRslrs0fwf8lUcAG8AR5pyrR39qeRdvJ01M5XGOPrOLsTFmTgMY2K99E7G1lPqFFGfElqgxIcfEH8SIWt3IYtokXdsvdN6gMv228zZDqUItOPSgwXl8C9Twrb8-E89pD_5bu_4Fn5Qs3K0a6slh-Mt0ff1Pvrnlh66Ey1mKJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=dXE6odFJdYUBkSVj9uas1oBfkqZkExFKs_vwYAmfMoECvj8Uj9zfiZkRc8tf-uPxIj-nSdNFwpk7ZOJG7vE88Nv2qZfsVDvxyuS5pB-oTcb6UoDS9BH4PzeVo5PA2y9-Twzvzt2BXJy2gF3wy2rTVTd6OG62wxNZiAQ_cdrQAeIiuf60U3BYubpIZgAcL4menFftIKX8IWzch1YbLZ6RLsodxq1h7K8tlunswpcUpf9jm2NIAnWapHaWR9LuDH-6KC-IeUXV-QgQKN33fRqnvdFdU7E-BLgscg2B3b8V8Fxgk9haQBq5I7dPfkXiSnygCslWv5ZR5aIZK4HsEyYulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=dXE6odFJdYUBkSVj9uas1oBfkqZkExFKs_vwYAmfMoECvj8Uj9zfiZkRc8tf-uPxIj-nSdNFwpk7ZOJG7vE88Nv2qZfsVDvxyuS5pB-oTcb6UoDS9BH4PzeVo5PA2y9-Twzvzt2BXJy2gF3wy2rTVTd6OG62wxNZiAQ_cdrQAeIiuf60U3BYubpIZgAcL4menFftIKX8IWzch1YbLZ6RLsodxq1h7K8tlunswpcUpf9jm2NIAnWapHaWR9LuDH-6KC-IeUXV-QgQKN33fRqnvdFdU7E-BLgscg2B3b8V8Fxgk9haQBq5I7dPfkXiSnygCslWv5ZR5aIZK4HsEyYulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=q5YWV85UGx5LQfC24iUsZFsfoHSCBV2Gy3yS-nM_lXObxPwDKXAsZr-YEE7WLDb23O4gGD3yHIP4TB4HJq_KWA2VMSDLaCakFhJL7nSgcfDdXa_JjT0E5HaAigc6rGmuDti8xCak_i1SLrneO4d4rxxIcZ23Q52lR8JiVNF7K0xbXtZ7BXjja-pSVc4HR0rnxpLve8hVrZ1KMYIk5ybbdmbWquICh-a_aE-GOx6sycIxqEbnRPjTwqTe34BUlWQiAms2NX6NIdPa4wMb_DWvSXDUXdOfjlBCgAEMIZrI96yGWVtKUbKLXjqP-GcFHj9ao9HZNnDdzLOCN-SBSfNLJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=q5YWV85UGx5LQfC24iUsZFsfoHSCBV2Gy3yS-nM_lXObxPwDKXAsZr-YEE7WLDb23O4gGD3yHIP4TB4HJq_KWA2VMSDLaCakFhJL7nSgcfDdXa_JjT0E5HaAigc6rGmuDti8xCak_i1SLrneO4d4rxxIcZ23Q52lR8JiVNF7K0xbXtZ7BXjja-pSVc4HR0rnxpLve8hVrZ1KMYIk5ybbdmbWquICh-a_aE-GOx6sycIxqEbnRPjTwqTe34BUlWQiAms2NX6NIdPa4wMb_DWvSXDUXdOfjlBCgAEMIZrI96yGWVtKUbKLXjqP-GcFHj9ao9HZNnDdzLOCN-SBSfNLJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKfr5G1l1r15l_zOiBNP78qsFCScNcei6CPgFP8ZyS_w-toferf3Q8nfUGllXLDkD2IqN9Wg-kvv1NtPG-hswxk1wijBl7nWj_Ae0BQ5Z_GyDtgJL_PJv8ZRDqbsRVxiPft2JCEEKmmlwo_6ivure7Yh-OWW65JHS6ozLTb4iX6LJB_ha2fvUb0XeeKFzvQpMIiVvjgtT9JHqyw4n3vDMNfYNW_Vw9ltpgZvzYPfMzmG3OtDLtxQXxZDVj1CrXha8TdV3KlKqJAu03b_GDAIBxx3ziP3TVQUBK9FAr7os_UyQIsRuD3VWWgGgO5L2t9VuWVRSd_0OBL49yVvxz7Pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=sPYljx4kDCck3bDipM0aBpKuqXyvvlavv3p7IP91nBD43k3W8OPRcBL156kkE9i9NQkGEcZ3mYua2c87D63Dj3Tk_g6J82yagSWcccSlb5r1X07h43jO_ohUdd5ghWgFOlvOb-DZrRpJA--dN4cNvAJTyWdoUnrcOVKaaS8RG1w83AgjPzbnVK1-eN1hmn3QvrNaReRTl1Fiu-EbanFyEmYgRzplLKkOrhPjNXjC5t9KERbHg6QOiBuJhL9_ADNQjKBq0smzlK34FCWLKr-DI-vteAoZYYN8CNAUIWxdjrlcPOHSybjMw7EDBR9I7gkXkeT8g-5JssbwdgiLEnuTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=sPYljx4kDCck3bDipM0aBpKuqXyvvlavv3p7IP91nBD43k3W8OPRcBL156kkE9i9NQkGEcZ3mYua2c87D63Dj3Tk_g6J82yagSWcccSlb5r1X07h43jO_ohUdd5ghWgFOlvOb-DZrRpJA--dN4cNvAJTyWdoUnrcOVKaaS8RG1w83AgjPzbnVK1-eN1hmn3QvrNaReRTl1Fiu-EbanFyEmYgRzplLKkOrhPjNXjC5t9KERbHg6QOiBuJhL9_ADNQjKBq0smzlK34FCWLKr-DI-vteAoZYYN8CNAUIWxdjrlcPOHSybjMw7EDBR9I7gkXkeT8g-5JssbwdgiLEnuTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMB_tB5iikBKEYSJI-B-b_Xlh8L_lKylyo9S4kOAtBOc10XpNsINxlUw5ap5sA0IU0nHYLRPMjGjdy_QXOrkjo9lKUrq_cq-SQMVsiqyhhS8pSZLvsw2eARAZM_Fzs0QCXyZKwtnLttxu11f110UIAdx-4KTe7WT55a5E2KiEJtIvH07CUDqSEZg48jzbJj5aBy4j_fPwYQQMlVQnpxkm2sdb7fhc1NHtiZUSMCsFrCgf89DROA5xkSXM7me5WdzoDvgoC0swXKAeFrPa5-XCTF7_xvt8NmNppVPhENdgHHC03Nf4KOqcnLLv5TqGOoLoPSLrDKEPDpcxxfrLlGw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=YEg9fnDHJrlOxYiklL33BjEVXMsGgAgI8oSLmqXPybvLGvGr6kwQ5QoIhP7Y2sYOYbjxi7cGdzRV009xb9bLrz0wHp3z_QkTIpSts09PGCwulnVhGHJKsLfxrEONCN7AdC86sy4e9MsNvJKV7kmBVN3iRF_ltNC4zr68Nt3KZYCn1sTieZ4I8vsLiX7d2F4fCm6lxsGkz8Il7snDJ3B9W6R1IyflQz49s2a3dP_Zdxc3ns2OimJN_mB4YIv0Vx1KS3umfyLmbh9jKJYgYGZK5juUWHAdmGjxrIZlsqBirx6Uh-VhFB1xiZ1f12OAZJL58ZsUSy69LodSI7lJ_FCzqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=YEg9fnDHJrlOxYiklL33BjEVXMsGgAgI8oSLmqXPybvLGvGr6kwQ5QoIhP7Y2sYOYbjxi7cGdzRV009xb9bLrz0wHp3z_QkTIpSts09PGCwulnVhGHJKsLfxrEONCN7AdC86sy4e9MsNvJKV7kmBVN3iRF_ltNC4zr68Nt3KZYCn1sTieZ4I8vsLiX7d2F4fCm6lxsGkz8Il7snDJ3B9W6R1IyflQz49s2a3dP_Zdxc3ns2OimJN_mB4YIv0Vx1KS3umfyLmbh9jKJYgYGZK5juUWHAdmGjxrIZlsqBirx6Uh-VhFB1xiZ1f12OAZJL58ZsUSy69LodSI7lJ_FCzqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=R7ffTpANTnvTGjcuQUa0m1g0IaoN8YK7nG01FAtbjmskVz8KnP32zUxUjfwalkEUoc3BaSA8w_Sib-jCeYDzjX9C0l_0BAwL4oH7WPyPwKhxktRAIatEzn4qY1UlWJmhsuALgNOKkt3fCCidXrp3qOv8R3nMjQQc4TxeWsReO_T9VCDygQgmAi4RIMkPBefOfhndnP-8rJqRDAFBJQPo1SK_ezBidjd1PCi67sFg_FsampjwXHF2-YXN-Krkdi-X0K6F0hxKoDN5ehNG4WswrSuDZ4MIFuImB3J67Bd4tBxXHhF8zjcBsJuVQLckXkwFKs2_Bb4QVXYyHcsWJt-SSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=R7ffTpANTnvTGjcuQUa0m1g0IaoN8YK7nG01FAtbjmskVz8KnP32zUxUjfwalkEUoc3BaSA8w_Sib-jCeYDzjX9C0l_0BAwL4oH7WPyPwKhxktRAIatEzn4qY1UlWJmhsuALgNOKkt3fCCidXrp3qOv8R3nMjQQc4TxeWsReO_T9VCDygQgmAi4RIMkPBefOfhndnP-8rJqRDAFBJQPo1SK_ezBidjd1PCi67sFg_FsampjwXHF2-YXN-Krkdi-X0K6F0hxKoDN5ehNG4WswrSuDZ4MIFuImB3J67Bd4tBxXHhF8zjcBsJuVQLckXkwFKs2_Bb4QVXYyHcsWJt-SSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx2hLAwyYkgPeb4QB3cK5l23xx_UKM9t_a5R8xyUGYJ-zgC6F4V3Qdcn-vdD5yXFgAoEXzZhkIXrKMzoiaQ2sUXUgkzXcKcsnGYk-O8x_WQ1dn-SqhZnAnXRHgWe1DrjLxuSMa4_ej9752cQlOJmdjMaOSKw1EJ2D-TVooOLmdRlPNWZCPTfwtGvMQtr2Vesysscr2qo9siV6YBjVwxHrxFa61-OdTuVefOrSLChZkiNJV7se31H8K6l_G9IVycXivgSobFY5cGH2HhHOGjHs4ivTDE5ZYC2WpMQRAJ6BRd6UsuqFdQrq_ejJBdvaot_SA5-yfOCh5BwAh3fwX7GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=aLvTpmcAFDWqmus7UBrgMxw4xrit5zPTPWXFEk0wROTyHyyLb9gQXGpB2tmJeGTWShhKBkPMvHjTuDoCP3qUPXFES9udW477b3CbwdE8TkQbNymao5gikvgwi217mr0oDu3QVs2xNcopdNM8Dgs3Ym5VLx1ft1bSbFMX3DHgux9bhOnuRUU8SiCGqgzIKg2i-nBQluTsWFAxEPzAOBtHuZoZhxnEt9TKtY0SJfBZ1Ijn2N1raeXk_l0HPOhH0lowEMaGQ-ACU-7iVOraYc9tVuJIxObo2kqjSE25tinuL48uZp2ZyqXLV0hoUdLAespMqPyfz3FBWqiVHjbGpbLTow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=aLvTpmcAFDWqmus7UBrgMxw4xrit5zPTPWXFEk0wROTyHyyLb9gQXGpB2tmJeGTWShhKBkPMvHjTuDoCP3qUPXFES9udW477b3CbwdE8TkQbNymao5gikvgwi217mr0oDu3QVs2xNcopdNM8Dgs3Ym5VLx1ft1bSbFMX3DHgux9bhOnuRUU8SiCGqgzIKg2i-nBQluTsWFAxEPzAOBtHuZoZhxnEt9TKtY0SJfBZ1Ijn2N1raeXk_l0HPOhH0lowEMaGQ-ACU-7iVOraYc9tVuJIxObo2kqjSE25tinuL48uZp2ZyqXLV0hoUdLAespMqPyfz3FBWqiVHjbGpbLTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQgb7uARCtF9yopdJ41IFTPL0zFs6JWU-gbe3pqd5U4wYX31Fjp9XZSAy1qXBJLdVOHqnaa14vmCe8CjaiWyOogTL5j5uiQWea46vgkh82QbxDYs2nzXq7WqOaPJkUDN1FOnV5YGm0zx_fL0ihOoPmsKfsqbmO6Jx2l3GnfVpkyz5659elf-cDNrdOs8LF2d8LO2C3ODqVWvaXhmgviKLkI0CNntRz3jQmnc5sfFxtwOgJDKlLNP6B0v2OU3WM421Osz0CBgkaBTPMeX7vqU-qaY8mcAyeDaMfh_tu5Tpf8TGM3FrCroV--qv_UX6aZ2YcNh58TPcddBiOkSB0lznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=cAcfs2AvlFxTRf02QPaeHuSFbPj-EZJ6Rdive_1yaJe0ZzXzKMh5pugTw_kbV3pw6xuFEYWZSl7LcHYwX-_yZbVH9Ul_sx1ziifnCKs3y4yyR-He36WZgUcitugNPMdvXA01jij7XGAt751pE289mjHJmlBDkH72Lj36aC3CuIvt8zylqbakgTL4h0-0W3yWhucTRah8sOUJpk1FyZOMFjM90QTYDaw26I1uoHqN6_8325SdJ9xwGQdlFozlUR9u8_wEMZmPxi0jqcHydU_YkdLr2hvnzOBQ3Y8H4mun6jTbO3A0AvAUn46rRK7z1wcT-k3-GbEmf1mOgpbgAxcBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=cAcfs2AvlFxTRf02QPaeHuSFbPj-EZJ6Rdive_1yaJe0ZzXzKMh5pugTw_kbV3pw6xuFEYWZSl7LcHYwX-_yZbVH9Ul_sx1ziifnCKs3y4yyR-He36WZgUcitugNPMdvXA01jij7XGAt751pE289mjHJmlBDkH72Lj36aC3CuIvt8zylqbakgTL4h0-0W3yWhucTRah8sOUJpk1FyZOMFjM90QTYDaw26I1uoHqN6_8325SdJ9xwGQdlFozlUR9u8_wEMZmPxi0jqcHydU_YkdLr2hvnzOBQ3Y8H4mun6jTbO3A0AvAUn46rRK7z1wcT-k3-GbEmf1mOgpbgAxcBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5EwShHYpYpFk02eeTVQmeqizg18_GkNozOVr8rLJ8hoF8yOIrylGitVmRt2Kr3wMPnYufBwkUyeSKSxoK4mlXdi_BZF68xOANARHnOlgv_WdW0lq-NbqVPO185-eTFuH3ppnAF_IbqshjqUxV3ScqpTFBOkEveYGThgSx0GA7FysLGc27Tg3HLqUeSBxaRf2ClAPPj9hkSv_OjCyiGmbvt3DFsGf6egQxhguRKDc3-muQAH3mQleSrDhxyPZ1Y543uxNuQEM9kGEcjKWRpvw-HAa7aCAffuqH90tU_BKMK9U0ypGZ8wJ9gacY2X_-O_EXOIP7cXcd5me0E_0lqyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
