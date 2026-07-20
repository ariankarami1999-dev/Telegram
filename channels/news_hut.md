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
<img src="https://cdn4.telesco.pe/file/bXca-b8SWx0tTpih1-aWrk_ISuEviuD6adU5B5HPnDPgTUo4dYNkWkX11Ad6rPLAfkUU_12Zs6B6-lRcfvS__Q67sMkXfUw2WAa43yvkzwjKTgHjEOHqoqwAjrukIdM1Il8WHLxkeLWuNHSmsW5ecFXlnQnHtacB5lkhp8CTg0-lWCcKxld0PmpWOOwSZ8Gp0A6fWYrObFqvT7gKpcMgMaWWifcYZeF3M37_mpDtiSdJ3GajspuMv5GUIAHBoNjKs5A9xvRz1axTG4FEaqwqNJsBkWYlNd2FGdmAlVu8l53L0yZKxjjSuQqzSTzTkihcI-2n77rETxU8f6flWfuxsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 158K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBv1k09jaXvFsQEkmNUC2JNkDNzUI9eT9Khrt2JE_7uZE19M4S2W4UDDVRng53XEyjoTBMvxHsPWF8Ujg2mJCxarkD22Z7kpwNxKXnQrXqEiakD2RV9bDGeW7014dX10bTtGmTdQTSTZtLQg1WxVuSdvP5LAJgYwX5AtmrqF7f1E60JJzmq84RpZsaa9cReha30i2OeGvHVKSY-BBkpdN-2hBsCRgkxEA8M9fwKfe6mqF0R5EZfpYai9dYAT7p9DyrouCTN8DYg3Wp8EdPMyDvxoC_UYP3tgst5Mihba_AMQFGsMNGfdGhOgcRdeq93KRn5IedHUh3_NLr0asgYQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=fgFvFkSOaEcZ2PFDqnuuVpKHA3COgFuYsn_9afzlhe1YK7ifNopx3oPhq3Al07O85D_L0RgoFuppZAF_l0r_AVtoSdYyOqijwNiKPvzJeVw_beG6zbX3YHU9_jYDxnwdJ639IJPSBgBSSRVxCoVpWO2c6e8tdtsWtE9KZLbIiXcR7wWo1DcGXBMWdo1xubi891cCYThaRnBtldrVeCBVKV2DQ0da3DhUQsuRqWBu9eH4qqpTkmdixaKOgCIoS-X6qCEkpM56-0RL7eWofi8XRquaT7lVCLkpw8MNRAkfcCRDhuT5oXfm21otXHZ4DeesNr29oXedBPXTXQWZlg7GaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=fgFvFkSOaEcZ2PFDqnuuVpKHA3COgFuYsn_9afzlhe1YK7ifNopx3oPhq3Al07O85D_L0RgoFuppZAF_l0r_AVtoSdYyOqijwNiKPvzJeVw_beG6zbX3YHU9_jYDxnwdJ639IJPSBgBSSRVxCoVpWO2c6e8tdtsWtE9KZLbIiXcR7wWo1DcGXBMWdo1xubi891cCYThaRnBtldrVeCBVKV2DQ0da3DhUQsuRqWBu9eH4qqpTkmdixaKOgCIoS-X6qCEkpM56-0RL7eWofi8XRquaT7lVCLkpw8MNRAkfcCRDhuT5oXfm21otXHZ4DeesNr29oXedBPXTXQWZlg7GaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=fksMqsEzF41YNTDu78fgjx8PSlWeZiVyWk7WHYY51t8Gpvj5lF3jIWHmKeQBxv20Elc6V7TNFSczCs8FkLqCV3zPp2wwA3ozkyRoAI-6bQ7E1BsRn3b-LaRhkb_VgxC5-Lqx34wbNt_p7Y2LlKq3z6EbyjLzd48UQTnZ7gfstS9EoWZJDk6bMxX3Fs46cB5GkZkFyCH-eHyEEVptRJdZxngRb-W1PiPHylogHxxCEPecJRDdj4UbnVFqrEe8pUcZ1x03Un_YA_LAynq8vHGpZgmJMidEfrns3sDGBXN0Gy_Asxf3ZruGwhgmO0PG3oo3_-41wd3xeM2__YhESXj7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=fksMqsEzF41YNTDu78fgjx8PSlWeZiVyWk7WHYY51t8Gpvj5lF3jIWHmKeQBxv20Elc6V7TNFSczCs8FkLqCV3zPp2wwA3ozkyRoAI-6bQ7E1BsRn3b-LaRhkb_VgxC5-Lqx34wbNt_p7Y2LlKq3z6EbyjLzd48UQTnZ7gfstS9EoWZJDk6bMxX3Fs46cB5GkZkFyCH-eHyEEVptRJdZxngRb-W1PiPHylogHxxCEPecJRDdj4UbnVFqrEe8pUcZ1x03Un_YA_LAynq8vHGpZgmJMidEfrns3sDGBXN0Gy_Asxf3ZruGwhgmO0PG3oo3_-41wd3xeM2__YhESXj7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=cd-67mLRbYmdC4nQdCPq9YhHNtjgah8Y7xk-TcUSTQEn3yESPFLOwCZv78aIvz8Cc-pxOdVEDyIQ5eYg9wfFmBL1JQQs-mL4C4AY08zJ79vUo9FYlPqbQWSs0lt4ePCdQ2HxLvzfLGC71aZyBFkiYU368eZb1hOoqv0tZ5HzP9fZ-S8PXavY7f4DbA8rNoeoLHf5vEBcQJbA3C4T6UtmMxWEo5vtdQgimhx4W9EVDopBLbjqCVU_7dPwAHPs_jgnSczjaNXSaOyGapwuwJEnmOPrU_UXg52lV9FyX204doVo6avRC7LxkfUjLuC69pe2zGprVt4joH7DhPxP8Kl67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=cd-67mLRbYmdC4nQdCPq9YhHNtjgah8Y7xk-TcUSTQEn3yESPFLOwCZv78aIvz8Cc-pxOdVEDyIQ5eYg9wfFmBL1JQQs-mL4C4AY08zJ79vUo9FYlPqbQWSs0lt4ePCdQ2HxLvzfLGC71aZyBFkiYU368eZb1hOoqv0tZ5HzP9fZ-S8PXavY7f4DbA8rNoeoLHf5vEBcQJbA3C4T6UtmMxWEo5vtdQgimhx4W9EVDopBLbjqCVU_7dPwAHPs_jgnSczjaNXSaOyGapwuwJEnmOPrU_UXg52lV9FyX204doVo6avRC7LxkfUjLuC69pe2zGprVt4joH7DhPxP8Kl67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr9vzrQR-g5iR6_u3iim3Ve9Vr5LzV09-fl8neG05_uKsbhtk--cYDvy4qgBQSBKg9Q0mnP21Tr18GEK3k5tEYGnrIwhwzU23Vh05niWLDmjx0V84St5n10WJ94zbUeTMin3mtpMOP1KVao9VRH-UHX68gM6uCXhZlbZPYp8K-yNJPk7yby-zZspeGALrn_n7UMIHmBw5MDv7mfcNq0QzGhos-JvyorXObBjQ7ZDgK4qsXpTKnWgAlmoDLmINre4FFA-oJmLW3lkvY4s_6A9wo-yaMdkb_9uyROcAy5XkahjixzOKaz6arHMb9do-T2i4KbfZPKj9fKOEiHeQz-jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bJyerNeJsP27ZSYsOjiF8qK4aml3lyYawl8C63l_ke6EzN9zoTayy205a8RqMEUI0esY8EpvNAzur9HhN1FswDfdnUdYpv_2BITci6vHKS_1H6stzn_ZyVNQze2Ix-xTMJvi1Ykzxh_jHy0_923oGbNnYlg5ZQiTjM5XziDqdhp7lVm56Ntxpp_0BLJrcV6yuA7KIuOWXpqhJhlg1Tn7VSd3nwmnpH1cOsZ-A_I1VgJz2Je8sTSLE7g33XqyCmvtwgtltuLqmftBBMkO194FGHvT9bjH3vYpY9o_F3T9Tdcj6foBmVEvWZ9CiQsHAQBmTipbwGKGHdrU_hczvJMR0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bJyerNeJsP27ZSYsOjiF8qK4aml3lyYawl8C63l_ke6EzN9zoTayy205a8RqMEUI0esY8EpvNAzur9HhN1FswDfdnUdYpv_2BITci6vHKS_1H6stzn_ZyVNQze2Ix-xTMJvi1Ykzxh_jHy0_923oGbNnYlg5ZQiTjM5XziDqdhp7lVm56Ntxpp_0BLJrcV6yuA7KIuOWXpqhJhlg1Tn7VSd3nwmnpH1cOsZ-A_I1VgJz2Je8sTSLE7g33XqyCmvtwgtltuLqmftBBMkO194FGHvT9bjH3vYpY9o_F3T9Tdcj6foBmVEvWZ9CiQsHAQBmTipbwGKGHdrU_hczvJMR0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVi4uW7x6J6g69-LaYnhYQa12tUpi6VdUwpQSAm7RIdXzMmQTANKOs_M8C2HMq5WQudL3A6q9_J3PPSyP0HMTc3fTdNRYNZW9YRbQagNR5wRDnLWpelKJ6btkYMKAKvdl3AhCNasXghonyZZwED-zJQtG6Dk6-XDJSIU9RyKa-hJM8hmzHQZKteQSFW3Hp0QRdG3DRD4Q24kW0uma886p49bXbxEJaY-EI2NC7nLDP7N7D6n8icGkpBAyVNlPSruWCt6JHZn8W71zMCWjRTnHBJY9PKwUL5YTt5Vm6Si1s2iDCrXFP7WhIe5nyh9wWNLt9V7N2Xiejpk6G_rPliiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU2mQgwPPpyeadnPaC7b8QjEsJbE4SGsgk0pZCAmweuXdJvWlpoQZ431_lHBc7ei8xTtVnHPtaNo7xF6OvPtkCHPyGGdSG5hm9SebhwDYphxyHp-lV1iKwr97AfBIW7v32EL8gGfPMFBb18JPUb7sD0uqeGX7SKCjHAYqFsxWSWCOa7h-VFWstCDzzlswvLKhm6PSyn5p9t_n3rWbpbvmHd3GEZfaC5N5LVeMd4RHb8OPJUD59uUFNpPjSgiBwElPRTfclFj60RbXKSf8DDarVo8uXH7YyqMLqHaAntbFYswAwHhsX0e5ZZn-s8enOeyccNsDFx1lY3ObPAeRRCSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGZloMVydgeS1So-w3InX_MysJTwgdgj5ihXKaxRsL-muESgz-cffLjSkX_l4uID85gYwl7FGAe-Y485YbKrRySb9BoR-h2w4QoLOQsZj72PIUXuvSGRetyZphq44OMaDH12d5fDLvkFbhCEXvfVJC-quevNA4g65viNrY4klUl48Dtq_qQ_4LkQEfL082KskGlEPU4tGYCsxMljY0LwthvkPzp-ynQM1RAVQGFiI7infu7k2ATXgxui0SdLccqXjugaBcLGf8XNlDhPchhv120CYIJzgqCZHsO0wvlII-keBeWEiiFA0isffYJdwXe0eeyhJ1kvHfFYkIjwqGlThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Er1DmuGkSa8oiaMfI3eR85xoG9kjgtC51y9XBHnp2-IVBHwUv0q6f_gOx8oQ6idy8Zo5Buzsoby9asIQKDU0MYPJYHzjWY56MoFz_qB-Dv7jFqruH8Rae3U6mqYnfQ9F-B_sV98HRlNQW0K0LlCKyrjrwW5oSZcFX6MEftD28hJfkNNdfsnDf8UKNFEkQdJFef8gQLhOhifOUlCkVCyYM2_dFis3lCT4wHD9oBzuZkhF6xLx32o2hHVozNyLNyrGVFFGWI_VJDpyab9-EQqNpRMN_2P2GSpNqNM8MdqhFt_Ca8ec25nPlE1nTFJXSLcy_AAXJUSMNeEdmVBdusiaVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Er1DmuGkSa8oiaMfI3eR85xoG9kjgtC51y9XBHnp2-IVBHwUv0q6f_gOx8oQ6idy8Zo5Buzsoby9asIQKDU0MYPJYHzjWY56MoFz_qB-Dv7jFqruH8Rae3U6mqYnfQ9F-B_sV98HRlNQW0K0LlCKyrjrwW5oSZcFX6MEftD28hJfkNNdfsnDf8UKNFEkQdJFef8gQLhOhifOUlCkVCyYM2_dFis3lCT4wHD9oBzuZkhF6xLx32o2hHVozNyLNyrGVFFGWI_VJDpyab9-EQqNpRMN_2P2GSpNqNM8MdqhFt_Ca8ec25nPlE1nTFJXSLcy_AAXJUSMNeEdmVBdusiaVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deY1RE5tE3R9RUCd_2JlCn2BYFJkoyO8zv2uWCZleWPmY7Fc3Yg7WewL60DmFhGMzplTm7dr_zVjqBXDwmiGaAv2MZNNMX5DjH7afAzrcJBFE5uicbef2mrWJgCagI3HOHpAbxYkwA_uCcerRmSZMLR0T1ZHNE5NuWA5VUb7OZx3Km2kg-Xwa9ozevewGS_ZeYoI7c-chotKps6Xl7g8MfOu2OoztwQ0_TS98fB7uZwIzSYnor_Ji1LRup-aAreOdbmMH95ddBFpxH5lRAs6ry24wgqIC-j8FPPnzV2FMF0XRBTTt_u9nTMPsQFU-1pSLMelLB5_Rc_SyjuK2-QotA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=Bom7YbBR5XqB8O429GDuRGUjWGyf-pcXD0FH7or1dyFKRHAvdGK9POqNvb7MJeJdWgfdQt9OntU9q1XOgvaT_dKDNSoPF_vJO7XUabiLDtVp4eSQrMJwI9ZnYJwUzr7OxHS2YxFnKptxMYJ0yw1S63mQn0duozRUvYZ2BMm1DA-jYILB5OXIc_XOFwRnjDrutzzX-7xkl6phjhZgn-gAAk_4jg0KSk2CnJDBTrYu2twrQe7X7801QR0z8WP7GttaZnYnqfNFLXHkeQWpecdJx2uOT1jXUi0tV6FyznxZEJ908JlaoRbkuC95rzOXd9IIxA7IoQS4QgKak7eGrFkIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=Bom7YbBR5XqB8O429GDuRGUjWGyf-pcXD0FH7or1dyFKRHAvdGK9POqNvb7MJeJdWgfdQt9OntU9q1XOgvaT_dKDNSoPF_vJO7XUabiLDtVp4eSQrMJwI9ZnYJwUzr7OxHS2YxFnKptxMYJ0yw1S63mQn0duozRUvYZ2BMm1DA-jYILB5OXIc_XOFwRnjDrutzzX-7xkl6phjhZgn-gAAk_4jg0KSk2CnJDBTrYu2twrQe7X7801QR0z8WP7GttaZnYnqfNFLXHkeQWpecdJx2uOT1jXUi0tV6FyznxZEJ908JlaoRbkuC95rzOXd9IIxA7IoQS4QgKak7eGrFkIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MhmGCduy0uk9iA_8VqqvSm72l22iOMf5Jz8WYdAn23KUWIbm-uGcT8GF_hzEOIVOpNNU410UbsrItjuDLnMMrQiRyvUs5WolVtfscqGN8vd3z1DxBoKxcjthlbZlVl6nrF0SVnVLNJ5BBGTsWg7XgOHJr2e7FgNM98Vw9I6hYbVoRTrzzN00A2y5WAmpCzltooffGq6vb45DMXGsZN0cHQc5mhx-sN2G6kC3BKi01_PCoSBKy7OSPtbL3IlnNAMICBmBGpLwC30sd183cWRY4LUGBv_gJuT-m8cQk5iBgoAPUCmg5TqLYqM47LDpNjPYmqvhwWq0nHZxi52bJroVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MhmGCduy0uk9iA_8VqqvSm72l22iOMf5Jz8WYdAn23KUWIbm-uGcT8GF_hzEOIVOpNNU410UbsrItjuDLnMMrQiRyvUs5WolVtfscqGN8vd3z1DxBoKxcjthlbZlVl6nrF0SVnVLNJ5BBGTsWg7XgOHJr2e7FgNM98Vw9I6hYbVoRTrzzN00A2y5WAmpCzltooffGq6vb45DMXGsZN0cHQc5mhx-sN2G6kC3BKi01_PCoSBKy7OSPtbL3IlnNAMICBmBGpLwC30sd183cWRY4LUGBv_gJuT-m8cQk5iBgoAPUCmg5TqLYqM47LDpNjPYmqvhwWq0nHZxi52bJroVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=agAe8SdOnYU7shf7uP_PiF-W6jYl-kpBnk9ccQdYtECT9K22pxMy3aWzRj1ut1AvnahCSWiXI9j8zOQUsZWwkkS24kKuOnuqSCOksTUE5RYznqLt3Y0BeXwNqz-rqQhKyLqj1WmwZ_XnWzT0RF0bRm2-aX8MFV_mgPgGSf0XqZ8uL2C4HCsKaneuoXtKYFVk69rIjGmxl5ro5pLFbUJKSaW41oh2pQSEjTzXin2AxrEk9LGoMoxDIeOjjBl6KJ_x0lUhNAeUaknMUiz4Uw49A5SLnC3fOT9bb_02mp7jvI8zSvHtg6PSwVwYT5sx1wlMW7OPBiXp-epzLyGQjYg48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=agAe8SdOnYU7shf7uP_PiF-W6jYl-kpBnk9ccQdYtECT9K22pxMy3aWzRj1ut1AvnahCSWiXI9j8zOQUsZWwkkS24kKuOnuqSCOksTUE5RYznqLt3Y0BeXwNqz-rqQhKyLqj1WmwZ_XnWzT0RF0bRm2-aX8MFV_mgPgGSf0XqZ8uL2C4HCsKaneuoXtKYFVk69rIjGmxl5ro5pLFbUJKSaW41oh2pQSEjTzXin2AxrEk9LGoMoxDIeOjjBl6KJ_x0lUhNAeUaknMUiz4Uw49A5SLnC3fOT9bb_02mp7jvI8zSvHtg6PSwVwYT5sx1wlMW7OPBiXp-epzLyGQjYg48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atG9ZHCGTq-XCVYfg0CTojV7DvqX5QTW1Y0_xtAsgwhVTRRJE-yGPdMwjKcjBBFFqpPKFSiL2Q7mEMPj7PFfdbfkCu_bZWJkixU1zw3D2utnFUFDe7AMfpz59_pqm5R12VglKhjDn17BDHk8aRZfr0QRB3MLJ3oNYoQUiM5MiKjW7UzV5YpoCsUsodV1rUPtr8XeATLUGMZXFQ37sQM3WOIwH_fjs0v2V7_z-DwPUkVMse6CPMafzhGWdFhPmJ0UhwNRhl5jEmcAOxRAs-XSzRe2Q5HBuHU84qyD2hFnn3SA_KeTVUyo1o6ar9na1Qlw1i_dnDacYDywftNvcC7XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=UCvii3ZG-8h8-JcwlTT4es4v1K4Em15pI8h8dlRU0WM8S2WM2CVNDa7rroSulFZwnCQ5ZcesrZ8yQs_5TCTdX6ukUlFHvltxJuyTCbpxq3xwSWSEQp8HT8iqBmfbvbmbZLYcOPICDVFZbso1EL06Gy-oLivYUgaW13GIPQTAA5dZrGGTs9kL4diGIet-2eRTV4kTY1CmnolRtf-WRTtkj2WnITZrlFepMw0cD-qb8Ktfw6u7vhXfroAZ98Q54Z-VI-t3YjvR-P3pTXbGi-P5_DHoQl2SfEGXzD6Zl-AULMrxlO023RjN7l54pNHPv2QALZ75eADFQvxdHG5KxVPXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=UCvii3ZG-8h8-JcwlTT4es4v1K4Em15pI8h8dlRU0WM8S2WM2CVNDa7rroSulFZwnCQ5ZcesrZ8yQs_5TCTdX6ukUlFHvltxJuyTCbpxq3xwSWSEQp8HT8iqBmfbvbmbZLYcOPICDVFZbso1EL06Gy-oLivYUgaW13GIPQTAA5dZrGGTs9kL4diGIet-2eRTV4kTY1CmnolRtf-WRTtkj2WnITZrlFepMw0cD-qb8Ktfw6u7vhXfroAZ98Q54Z-VI-t3YjvR-P3pTXbGi-P5_DHoQl2SfEGXzD6Zl-AULMrxlO023RjN7l54pNHPv2QALZ75eADFQvxdHG5KxVPXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyMcHg42qPJxOvL91jzjjq1Cggdiot2Ea_8eryA_OLYGjssIEkGtY_XDYLgy2eMc8N_mzR7O0M1Rr1Dxt8L-IwPL1dHuJ8ezsNkwpmcvP8Qssd1MGcdmvrO9Slgc0sFvtht5sL36z67D2pUaO216ff_zPw0fDWTWw3dAvaX9rfMjsFjPAWtOuBGfLRPRzmB6bwQAso_-Ed0VhAtkZrLuH_JsmwG0CsndtCnG6jdnDIu_H8Wc4fGJuxUgu5C1NHnI5pMbsEg3KNsQJS9fV1i_c13bSa14SsUeMtXRQ9hd3ZDatiNK-a9ZPeNXJjfKOVwz0JfTZfSxBs7_Itn5Q4KbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=Zpuav29pIRTwEGncH9g8-PCkO6qi6r_L9Mch_EI0qb1vIsLFexIPhM6bZi2FcIxdScig76rHbmSXeSQ8Ag6hSDTm_27C7bMaTxH_c2iJvJfid1WOzN7v7_cGPB4bFVGwYV8a4tY9XqW9CRAcsKV9jqJfE-SL_0DuPk6Totz6e97jptumKx1IOxlLU944dzm3gbZDlTbO-nEVr_fl1WbguiXbx_HF-l8YQ-N5TU_MTSq9AG2zyndPscuJn4_6F2OHGJREh4EjslNuq21rqHym5qfZ-Kk06IXJkbj2_NBGKiS6pQ1Prdrpa7hVNiAsuW8YKB3nhrSf4bX0x4tmSsyd-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=Zpuav29pIRTwEGncH9g8-PCkO6qi6r_L9Mch_EI0qb1vIsLFexIPhM6bZi2FcIxdScig76rHbmSXeSQ8Ag6hSDTm_27C7bMaTxH_c2iJvJfid1WOzN7v7_cGPB4bFVGwYV8a4tY9XqW9CRAcsKV9jqJfE-SL_0DuPk6Totz6e97jptumKx1IOxlLU944dzm3gbZDlTbO-nEVr_fl1WbguiXbx_HF-l8YQ-N5TU_MTSq9AG2zyndPscuJn4_6F2OHGJREh4EjslNuq21rqHym5qfZ-Kk06IXJkbj2_NBGKiS6pQ1Prdrpa7hVNiAsuW8YKB3nhrSf4bX0x4tmSsyd-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=NwOh2l0qFtgsPT2CVp5kU8WFTP0sK4WhMLKH5vi3TGoGykKC3cqKlud7pCalucpBODcdHY-7WK42cZptSQrPYprRZ-uVzJdEYBsyYgXPXCo1Ja4Wbd5xPfOePetVqpU5ANcVYbfc53l5mCWYyOIm0qZ64yZEGbcIo1XT9MqtVrTslsa4eA5T739L94__94uP3417mqy3Lf8-nO0QHuE7jJ25ISLnDSvLFSL4vsktG7vtUW91qwy9Tjmrd_-NcPv-Hq1UUYHzNCmovzE6Cl6sNXsHtnIs-guxJw9Hslls7PNIglMpO4ZRssNzTfPRwk5qPJL7r2PcA-tq9JXLA1nJfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=NwOh2l0qFtgsPT2CVp5kU8WFTP0sK4WhMLKH5vi3TGoGykKC3cqKlud7pCalucpBODcdHY-7WK42cZptSQrPYprRZ-uVzJdEYBsyYgXPXCo1Ja4Wbd5xPfOePetVqpU5ANcVYbfc53l5mCWYyOIm0qZ64yZEGbcIo1XT9MqtVrTslsa4eA5T739L94__94uP3417mqy3Lf8-nO0QHuE7jJ25ISLnDSvLFSL4vsktG7vtUW91qwy9Tjmrd_-NcPv-Hq1UUYHzNCmovzE6Cl6sNXsHtnIs-guxJw9Hslls7PNIglMpO4ZRssNzTfPRwk5qPJL7r2PcA-tq9JXLA1nJfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=NPhyrqirqU-x3VMlDrI9m8izl4dJR1KkMlWr7X-ZC0j5O4x5a8MD7FzV0LX9o5zm8uYqY3ahGBLwIdg3bnrWxzEbtDmn2OOUK1mJ59fZZ0MRU0xM_TX4ejW2xuC8BKfR-lVCvtSPksLunQvI_q42Mao0CduA69j_C4pZ_TcbH_FXHQiJXoGybtbRidupm9YehVr2lfl3dtUzkQhD2oBIzkRWBRiVCrl952qZxIyyZ4nTWJiFzZYzpolVpT2pC6_CY3yxNNxuTKropdnkMfGIuFe6x-glo5cP3FAZZ7dBNAcRIUojdJ3IfLf82D2RUpADu2XiXBALu14U4wlbFskWng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=NPhyrqirqU-x3VMlDrI9m8izl4dJR1KkMlWr7X-ZC0j5O4x5a8MD7FzV0LX9o5zm8uYqY3ahGBLwIdg3bnrWxzEbtDmn2OOUK1mJ59fZZ0MRU0xM_TX4ejW2xuC8BKfR-lVCvtSPksLunQvI_q42Mao0CduA69j_C4pZ_TcbH_FXHQiJXoGybtbRidupm9YehVr2lfl3dtUzkQhD2oBIzkRWBRiVCrl952qZxIyyZ4nTWJiFzZYzpolVpT2pC6_CY3yxNNxuTKropdnkMfGIuFe6x-glo5cP3FAZZ7dBNAcRIUojdJ3IfLf82D2RUpADu2XiXBALu14U4wlbFskWng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDBxc1YV0waSAb3YqO6fC7RnSYBUSRwYiCyFb6g62P6BpybJ8IyEhNWuaM5akUxsI1udpmCuovB2y_vGAN43mR0k8Ay_DhnrhKLQlBi2aEdc82i8cWFFojY1gC74vCOGAI6myRONq1Pn6yfTvsU6adwFsD9Rp-Y1nUk2XjCPx6uxL_PRhmq5axkWO1KxFxYjOnUBahP2GYWceY-gfOySd2dnM7ua8g-N7kuVMZTtfCqp5ukyP-e8KsPh6GGVJjIGAlswm_Y1lHYxJFH3T4az9AjDX5_At_jnLRgFgH9Y5f8sJbwnUqR8nCswJeBLdj7qMDS30p_a-WOXKSiDfyAs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqDKaOPJQr7FAnwUN-gN5J_DYGbEWfGPQcOWWwblzzGZfXw9LwGPOq4J_MjJ4oQXeqHKuxT20b8PHZcSpDrdJTekewJ2SWYUKfTt10ZF54WEvAuOnHp1U7LRwhxAcjgFdxblfKxZSGcXEzb3mQVDcr_-9uXSt6ZBXJ6KoxK1pbx0FV8uXnnptx3ZOHs6SUTICyXHYIqLjy9-V8q9i0HS1uz5Q5hgRvWVL4qyb_zEB5HARZh_7DN1qwvCttxI2sMc8EQ7FuonI9QjKObyTSa3WxovmXQnJv21rkvQao7l4iubibDuO4fbF3ps_JT3JuInjexJ-h_-rwhcd-but_HslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68589">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب سنتکام نمی‌زنه یعنی؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68589" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68588">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaXC7OmrvgMXsvlKWbRdc1kiVgNRi_W4wfa_Qj7_IKvVs_eZey88BPDtUFGyYjCEdM0VpXnioSAjGOeL43XGnVNyxb7DKM61bi0cAV0Q6GILaFidZEZdMPs08DRh6fnd-bwfjOvgcRbD7uYZ4RPPqmDFK8yNKIVqpmSwPf_WYkjT1umvjWUGL-gUQp864kZZwazkH951lgA_dKPoZb9pnIMrR2qURCULAosOCvCahHwtznXztOEf_DcSw-J4BjT4vMfaJCBQ02FCG-f3SBJ9rsu-5h0HdkW4kGmEqq9BEEReVG5X_0R_HHA_-7fqJzIH6jRbWMUCQXjM9tiHBxivPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آقا تموم شد به راننده بگید حرکت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68588" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPRxR1fxo0Icm57grzU0YKiMLbF4_e_9StNqXMQTCN7SvGkd2asn_Ev_HG7mmWjGjIhBQBwXhk85BVGpoVV2ZYSCTVeACxgSbAHAHdo_MC2oETKyMPZgquExw-XFbVPMQbmvdhUXCYkj4hIiq7_6Mx4pFU2ehfBNfonlf4gtk0pJ3bUJoF0x209ajS5MlN3i2THjpmYrnEIQ40hOa7rlq4j2YMJnZltugrL4cGQcWcYfDpLVqsVVu98x70XB9O1ZjL4b4sAuTK-Ws3la3PUt80Oc14ZiG_F40gxQNhCjhD6UasF7egIDsYtrjczh-z_xAH6GZFe-AKEmZFKDHdvHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 هم با همه خنده‌ها و گریه‌ها تموم شد؛
قهرمان: اسپانیا
🇪🇸
نایب قهرمان: آرژانتین
🇦🇷
مقام سومی: انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
🇫🇷
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68587" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68586">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0OoqNpbn-JjEARnKucn5dVw8ItODbuTYskJzsACoC3bFokSJqrdDAmQUnUFoENi34XFibeO2zQ18iHP9eoJfFXnYSt2PuxN1yW2pLphqIYNyKwPurH2tjPq1C74WdVAmHfrcsoiPiubkMpZxzggXaJP-TRcbmcA8ebNQqIOPRLjNng6HOavU6NmM3GgtaPkeQcnEv9pvd0NhmmF-rzdP-_tjhFN4uK_o1PXl_1e9w--6iuu_KcV7sZQfXLKH1tAyLi4PiRu4BQZC6RjQ8UovpNHuJ11gxtmqa0jYVH14XVilfdh7MV9G5m0N9WR8jzOSikzOANNAtlLd4mmglIgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
🏆
تماااام؛اسپانیا قهرمان جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68586" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسپانیا خیلی بهتر بازی کرد انصافاً
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68585" target="_blank">📅 01:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68584" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68583">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
گل اول اسپانیا به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68583" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68582">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3txMzwpoxFAA17KMdQAbqR-dNhivMzbuex9LPSxJuR78tpuxGtq4sAwTjtBY4C_omXp9yLXPXy6HHgRL1--QfPQPgzcMygUIrpa3Vn9AbfsJisRuBnj3tZlvg8rClNwLjGFBlxOo48fQQ2zYMVrm26B8sKJtXKCYFoJLR_QsPSoOq1W14SOCeYiRgyUL_ncoJXkI4qsBHd7x_msAQ3tfGYJsSq4PcoQ9gvH6hfHbglHgo1IBZT4fU1PVKoPCikcjsqh4lsgXvF2ICDMYwKxip36vqhv2LQTMMk-xLrbt_u8nUDvdFFp3L9Sfsf87mMeMUd5S2z1rjtKRzx0x_A9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پرچم شیروخورشید در ورزشگاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68582" target="_blank">📅 01:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68581">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بازی که رفت ۱۲۰ دقیقه، نیروهای سنتکام هم دارن فینال رو می‌بینن، حملات امشب، نیم ساعت تاخیر داره
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68581" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68580">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
آرژانتین ده نفره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68580" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68579">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
آژیر خطر در بحرین به صدا در آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68579" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68577">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=Hz8Xv0m5mF4DXlqrT5YFltDMvz2frub7VoFL8QZ7UX9Hjpg54B6Z4o1HXSBwLD6Rl81C68Jl1emCtaH9DeZ1pr67EPuMzJ79Q_En9aZetHU4mN-v5yJhj1ALg8goW1cQK3oqOvqj0tvHDU5HCEUcshN9PMszRuT-5_LDs2foAiD5J4_8cGrdSEaXAooEcf47nAZaZQGz65te9EFHpzyi2N2EDOnZbGKFMOF6a2LV2WThOwyECQg04tRgoWSIpb8x16Cg1NuMzaZoko408TD1oj5_oxIgyiwhz5VQbhjdkPwhJZfZNDJOnZmUwK85ulHEP8uGcgxCmId2_SdqIXbYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=Hz8Xv0m5mF4DXlqrT5YFltDMvz2frub7VoFL8QZ7UX9Hjpg54B6Z4o1HXSBwLD6Rl81C68Jl1emCtaH9DeZ1pr67EPuMzJ79Q_En9aZetHU4mN-v5yJhj1ALg8goW1cQK3oqOvqj0tvHDU5HCEUcshN9PMszRuT-5_LDs2foAiD5J4_8cGrdSEaXAooEcf47nAZaZQGz65te9EFHpzyi2N2EDOnZbGKFMOF6a2LV2WThOwyECQg04tRgoWSIpb8x16Cg1NuMzaZoko408TD1oj5_oxIgyiwhz5VQbhjdkPwhJZfZNDJOnZmUwK85ulHEP8uGcgxCmId2_SdqIXbYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گویا از قم موشک‌ پرتاب کردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68577" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68576">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr7hy2VFHXwD_U26XeUQztYlOF2mmdPVqNGj5Wd1K0XspmRvt6wLxHF4ecPiRESaqg7tMr45TfLULHqhTbYRzhjhx3ZmYmADehVjLzLL8zsEUD6PcMuiJ2Nj8U9KtpRRx_kKn34nSVZqoseaeGC5yF9DsbjVFnyhksO4EGGFwPyf3ONHKx4iS-cCLsoIGvO4UucQQAWxunbjmkglKeezzASTYyJVyjKwr2Zk1rZvjNnQIS0RQlJmtZ1jdjaiL_ji5BPzWnopfOmgJ-T-RFwRlWk_ICKs1LRbNE2sq13D8GhGCAH-6_gekbr_MiIpU89bHXxkAryTNBV6Cl_GEGsBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بیژن تو فینال
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68576" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🏆
اجرای کامل شکیرا در بین‌ دو‌ نیمه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68574" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏆
🔞
🇱🇧
حضور میاخلیفه، پورن استار اهل کشور لبنان در آمریکا برای تماشای فینال  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68573" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68572" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68571" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=kg1TwtScrN8Ma2mKWoB5BA2wK801TJdm-dIfQAdtRY5IZhjlbYNsQuTcgEJtJF-Jnq1YdofVrqasM44rLYvhgAJRwbqrTWgwL9wRSkbfWrXmZjGr1fTbpVbOsh6PG87tehhGjxmz-msyHb3msyHjdzrKM0glSEi-QCw-1Nazd6Y9UHxHnyvYPCVQ2ukDCwcPi4Q82ewRWxYDKbSvMcy4ksB-fAo_Gf9wqllci5uES5U522NOygHavKDBTwcwEAKt5XYzO78SkgSbiSH0JX9pQVkSPh6lH7rUPHH4hxb3PzamwfzrFMdZ7TYihVFhLpqxcQjA9zbJaxSn2f2CmfXVaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=kg1TwtScrN8Ma2mKWoB5BA2wK801TJdm-dIfQAdtRY5IZhjlbYNsQuTcgEJtJF-Jnq1YdofVrqasM44rLYvhgAJRwbqrTWgwL9wRSkbfWrXmZjGr1fTbpVbOsh6PG87tehhGjxmz-msyHb3msyHjdzrKM0glSEi-QCw-1Nazd6Y9UHxHnyvYPCVQ2ukDCwcPi4Q82ewRWxYDKbSvMcy4ksB-fAo_Gf9wqllci5uES5U522NOygHavKDBTwcwEAKt5XYzO78SkgSbiSH0JX9pQVkSPh6lH7rUPHH4hxb3PzamwfzrFMdZ7TYihVFhLpqxcQjA9zbJaxSn2f2CmfXVaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
اجرای عمو بیژن
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68570" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGEnMDEcGMsoLP9bydJgxYhpk_CRWXRLF7OwASb02AhzQN9fy_GSU5p2hRx5BtEFyEM2jxvAezpeWkaxiK3_o6zHjbNX0esBBKxO6JHlVxB0mmbCH7IRWrsJC9R7HF0bCcsk3KYA7iRKPdXOlJrLBEvY4YfNQLsrD4FvZWTSTPrkW8QZeU07dS1AXHqewXfUgy572mFlJFmgBLAe9leNGKwCPxe2-NLn_ho8BRONJUC_PYTXkEdJkNVNrBAiLqhND9pf4LQEECwunp3sk1-Y6mJuiKtJWRE7FCIBm2hRg_ZoKGVC3SZma_37jpukG9yx2kERmWKelz6Ynbf4rTCzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه آرژانتینا دارن کامل لخت می‌شن
🔥
👀
🔥
🔗
مشاهده ویدیوی لو رفته از دختر آرژانتینی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68569" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzc9AWDdCmyVNmNYQX1mloHdNOgqQ5Y4LdEJ4UaQ2TiNmeotaBlAcAERBU0woRLaTrE0I-SS4Of5G8lFsZ-J4lW5_j9hMvAXyW85ENoEy0FRQHeeSDsbAjCgWPwlUTogueSiBtbk6NxTNKzUHmbMvSsl8GmeLHhs2VziUdWp1IHpHCcDpMJDeUHnMoZMX0LAg9SRL_rir-Iefli1UJul6c1SFcoYjRTQuwTGC8jpCdNo_fXcA30SXPmbwWgTA6YPU4CHp39JVgTBOqVBjZNu8S2uezLJWmQ8Rgr5QyMIAwHMjkJwns7xGgMkvFMVcC5sJU-84JLVujRORnqqEmIcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
روز گذشته، فرماندهی مرکزی ایالات متحده (سنتکام) خبر جان‌باختن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر در اردن را، در پی حمله ایران در تاریخ ۱۷ ژوئیه، اعلام کرد.
پس از یک عملیات جستجوی دقیق، نیروهای نظامی آمریکا امروز بقایای جسدی را که هویت آن هنوز مشخص نشده است، در محل حادثه پیدا کردند.
فرآیند بررسی برای شناسایی و تأیید هویت این بقایا در جریان است.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
نظامی دیگری نیز در این حادثه مجروح شد و همچنان برای درمان جراحتی سطحی تحت مراقبت‌های پزشکی قرار دارد.
سنتکام به احترام خانواده‌های این افراد و تا زمان تکمیل مراحل اطلاع‌رسانی به آن‌ها، از انتشار جزئیات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68567" target="_blank">📅 23:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIpIRvhUoj8beDbpiFPeyZJhhlGWPA2lep-dnRFw7t0TnJt3f-vwuIyBxv2j0O1wb5m_IzQTfdcn5LHLuu0M_zru90r8xhOYAhXl4JEusdM_gdZF6OuesDklcn_RQKxsvxsqi21A931sy2_N7KsQ43_xOk1xkcazrB7zVjKslRO8McG6VJN8VmIkYnR08Cq6UeTc-V6WGrATo3jMLQGWAGlEkDNwaPPmZnTDf0A2sctgJnaGDW8KpdciSYKZF5u09RGqSnSBIg8hp-EyEdlTAjqJSbbx_d4TwDyOyp1v7PS2MdDPlDmNfTNKAG8nlNGVpZ2fXgyh0v7nVtU09Ps3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک #hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68566" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=XB06ziZAtrA-0J7ESs_KSwaUAEOGjhcuS38TwApdK2m7cf19lSn40-q1MsvugKDSoyA66O8a5_4Tgc3GQL_psVcq6i-ahmUT1UghZxEF2-2INZmhArSb9OcAzzKEcoW25KKAFYz2xShvqYXVcDUIyEw5pyz-rIcjuzkNz_sF-O658Spfylw3gs3JIVH0yqnHHPlowZORmCARTl7kdBgwI_TvvkS89YmTUbOXJK1ic2WNSB2ilZXlH84T1dM6JpPiKZxjHJWfQ1U7VUM06n8gea0kLvgqrrcgvv3n5iMwFqxAEZWdaR8nwG1nhlSERBN_lUUfebnujKUkWRJoyyg_NlBwPtCDusPfcZLL-7p1-2B4wuFu9M7thleXxR243k1wY2zImlolsET4gZnYPZixpEGDKvqYY0QtdnZ69cCWiiO-oTqlSfZ4COOZuwAzBpHTFVjJkbUk182XQslL80lDMrq-CX9nKGbwKXuH_WDEd6kolsYFN4MAZjB7qAIuSirfurl6N9uhEma9D8FHUyoUZPua1EDeJcS4fv8aV1zWWAiO6Tan1Y7XqP0WSdgeQA7gKaFk6gXFA5cWlIU1sFU8P13vyK1-VC0d2HtnhwAyTuziqKz6rTHH28w10Ty2I4Am3XmZ4jFenEExtgx2SnaCBczbWagWftS18MzG50je97w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=XB06ziZAtrA-0J7ESs_KSwaUAEOGjhcuS38TwApdK2m7cf19lSn40-q1MsvugKDSoyA66O8a5_4Tgc3GQL_psVcq6i-ahmUT1UghZxEF2-2INZmhArSb9OcAzzKEcoW25KKAFYz2xShvqYXVcDUIyEw5pyz-rIcjuzkNz_sF-O658Spfylw3gs3JIVH0yqnHHPlowZORmCARTl7kdBgwI_TvvkS89YmTUbOXJK1ic2WNSB2ilZXlH84T1dM6JpPiKZxjHJWfQ1U7VUM06n8gea0kLvgqrrcgvv3n5iMwFqxAEZWdaR8nwG1nhlSERBN_lUUfebnujKUkWRJoyyg_NlBwPtCDusPfcZLL-7p1-2B4wuFu9M7thleXxR243k1wY2zImlolsET4gZnYPZixpEGDKvqYY0QtdnZ69cCWiiO-oTqlSfZ4COOZuwAzBpHTFVjJkbUk182XQslL80lDMrq-CX9nKGbwKXuH_WDEd6kolsYFN4MAZjB7qAIuSirfurl6N9uhEma9D8FHUyoUZPua1EDeJcS4fv8aV1zWWAiO6Tan1Y7XqP0WSdgeQA7gKaFk6gXFA5cWlIU1sFU8P13vyK1-VC0d2HtnhwAyTuziqKz6rTHH28w10Ty2I4Am3XmZ4jFenEExtgx2SnaCBczbWagWftS18MzG50je97w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68565" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwNehpQ3ERAbe1Z9IF4HVy3DZ5GC9jG8-memgVLHrWEcaf45CQCSEhYubytB8NK31RO4On-XmOeUDF94LMSSRGWuo1sa9BusI0tpQ3Hgj6tKfHqVUdCW4SJUswc0CiLFQfxatnyBDstmI8FO70jgaeF0Y5dpOC5Bs7CNKxpveVx-69rX9PtGG8-KSdEUSl41WvrbvBCAXj6ooS7MHKstN4vY3clIM75_MHkevVvB0Lgom-LNnjl5MCwd0JqNkBJUwsoxI5SodBWHZY0-XXnhOqxnXxq3ml121S1ZCEbUsNEUmBi84_Bu0GfwVKo2arLG_UZ2BKNPKFMaGtzry9eHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
گزارشگر صداوسیما : هیچ تصویری از ترامپ کودک‌کش و جنایتکار نشون نمی‌دیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68564" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68563" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upW0E2dDsREt13AXh7VUu_7ytjokXhLs24l0UbTvKs1I45kWSYHb_6zMRsud4rBNkveD6kMV9FAJcpw1OOrT_EPxcVdIRWSO-Srui_-zusBZkxEqB8bIQ1PSgCqydWXbb2tAhL9RwkrEHk_LEFGrMEewrq3dzHS2ymzipksRP393SBTO8tIgXgvvNGTBlB3xzBsEPO330ynkr6wZcIVMEZpCGyaBYx_6J1HFObBD-K4CbbmXRBw9qqlv9_Ada2YBZhQ2yxmQ_GX9laRK_SUFqmYkQIhwKhBlfQlDGnvGNLzTffzs880XAbxZSG_yr_ctfcvlyEvbFFOwhTwDLUBU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون ترامپ پشت شیشه ضدگلوله
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68562" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od0Ug-rR0jdcxFYov1XC-KclEnP8gqfbXt-MMpyVbpJzW9Eb1O4ogn0h7xDCphXO80MBmiv91eIMTQUhj_UKZJYJwych9OB-UyYR35N5WmeWSCZXUESnrp8zB7EWB0bDAIrtd2z7mAu-bziG0W0LWOoVNWrObV8c6c1GcdzcML5hWz-KWJelgS7JktsLBZT9VV6YxYyySyCPBoIg_IM97EM-hyFtRNzExRqKu8U2TerQJgKNLXwOa7O615wka1lMqvu0z8kXNymR_Lj4S__ACiQT0uY3JAOrJyxNXAJIJRTKPouDqQoZHnVyD-7d8Lxqkk6L2DLE2OxAV2H5ubwjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام جهانی هم شروع شد
سپی
یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… همرو
بدون سانسور و رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
https://chosefil.com/fa/programs/318
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68561" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de66012.mp4?token=t22RCBqlxu549pPb1cMozQnCMXRZ-3OCEYUoeuVQQ9qZlrtKHKZA8Qulb09yf8r06ftrZgSbHkx9xhpRmeJMqCFjoXN4RZVHH7roiQZY6KzOQARTBhyDnYxRXy6z5lD88EH_FVBc_rjXBxh06NcU4h4SfIlmX0M0-rTJVdTEwn9J3UdTIz3ciLswd0PjND4X1y6ekzRM2dPnDsFKfT6rpESmnw8O1SNV8Vc3uZX9B-tZFfgPgvKL5VBoX-MIgIWTsjkr6drhi9ADS-V14Rzn3LvgwfOReMFFF9sqshmi13fzTXT8dWWFdfoRV7ivGgNaPJ1xPUU1CklbS0c3CwxdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de66012.mp4?token=t22RCBqlxu549pPb1cMozQnCMXRZ-3OCEYUoeuVQQ9qZlrtKHKZA8Qulb09yf8r06ftrZgSbHkx9xhpRmeJMqCFjoXN4RZVHH7roiQZY6KzOQARTBhyDnYxRXy6z5lD88EH_FVBc_rjXBxh06NcU4h4SfIlmX0M0-rTJVdTEwn9J3UdTIz3ciLswd0PjND4X1y6ekzRM2dPnDsFKfT6rpESmnw8O1SNV8Vc3uZX9B-tZFfgPgvKL5VBoX-MIgIWTsjkr6drhi9ADS-V14Rzn3LvgwfOReMFFF9sqshmi13fzTXT8dWWFdfoRV7ivGgNaPJ1xPUU1CklbS0c3CwxdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری حکومتی:مشهد در18و19دی پنج ساعت سقوط کرده بود.
عراقچی: اصلا انتظار اعتراضات ۱۸ و ۱۹ دی رو نداشتیم، جمعیت خیلی بیشتر از چیزی بود که فکر میکردیم
.
مجری: ترامپ درست می‌گفت، من رفتم آمارش رو درآوردم، مشهد در عرض چند ساعت سقوط کرده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68560" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=PlPd-VyiIJOpyMmfIfUVJUQMMmVLptg794fI9FqaqR4EJuDSUUXLCnoOqRw0IVMht-1FGhMXQXyaHZSR4B4MUkG0YaofP1ra7yMgow4kH2rN12osGKUYeilbPaqsoZbbKo5yt7awcDZctuaYe-8anB1zMobgavzmfBleWfKlpTMOl1nER4hMeRtaswo7izOrxGqjWfRoooEU7KJjPfWRbjQSoxvLPTW5ngIFuA4TVudbgK19HAAVtyb5brqIfVEv9sXirPcIDqsX5adlN0dfpKBtqa54Ejxk7bU0rgSn5Tmt3FpUZ6Khkj9xmawoX_fAeA-a3OoEADXki8M_fXojtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=PlPd-VyiIJOpyMmfIfUVJUQMMmVLptg794fI9FqaqR4EJuDSUUXLCnoOqRw0IVMht-1FGhMXQXyaHZSR4B4MUkG0YaofP1ra7yMgow4kH2rN12osGKUYeilbPaqsoZbbKo5yt7awcDZctuaYe-8anB1zMobgavzmfBleWfKlpTMOl1nER4hMeRtaswo7izOrxGqjWfRoooEU7KJjPfWRbjQSoxvLPTW5ngIFuA4TVudbgK19HAAVtyb5brqIfVEv9sXirPcIDqsX5adlN0dfpKBtqa54Ejxk7bU0rgSn5Tmt3FpUZ6Khkj9xmawoX_fAeA-a3OoEADXki8M_fXojtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_kxgxPJiZ6XouSN6XnYLSTo5aGqsxmWpLjX5vJRPixiTE04inExSdWVzZjtq11SAkWyXhPQXm-9o7cs9ftv9w4_qjiQZrOf8-2jL9oGJtl045AXkyarBrHTsUxTHWb1yPMYWZxJoW2yTbpRNsOaGsQK7lF1Wma2qLmG6-TnOgD9A7uvqaQLU5otdAUPixmtYjKTBDlcwcQphLnnh6vWi0xsrPHRxWkXZLgfd3bWsgZsUg-ql2WQgtzU5mDFej1EsQNWqEJGZjKbAxvBHpH8rjIDLVYe9jZbO-QDf1caueaAlyuOkPoAqvBDHj6MD4nyry785X9k4kvPxP6sMxAPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERf4hPRExkL1BEh6tG7UD9vSY-dgxcE8zi1qYyRGRScmsPTK_uyBDnMKZ4BR6W0n47hW-stwInn-SVSNFwYWjpXwOYX8O004lFQC1kZUE2esZMizSij71kTBZuTWY3AVQCRTcFHOfrA2MB2Smu1h3eK-7Pb8T2TdZSokDlwZZH1lNqg0BXjipleyt0eFj4vYZCdkS6JEDMXNA9c_gSm7u6VeKN6ZA7AL2wscCMsaVMcq5EYFrOcGMz-Q3dJ1d94niwKHaQH66isk9m0qaWpp2nxwUqVMrnhZtsut3AmZv3tNa2DnMr9yRsSGadP2iFKh6iyqYgz4FlvLQ0BZl42qrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=hkNESfpMRbChGDP7oKHrBAui0zRlEaiOcuMEpfD5cwH1PAIiszM3_HNtC8-V5wA8Z7xZTvKCAs0NRaHO3NdjiVt69nGZZJVf_TdJPoR-2T1yWxhDv4ZB7jIWEh2HtyPZ25uKfU3W0QgZ6k4l5Yi4tAAcpJ2RhsKwuC7dadYi2-fbHj2sLTjAVEsH3lu0GVb-32bX0zGoUB1e23O_RBmH9eK6CoaI_sGoitMBBoh1Sgn_-A6q-M2NIxc7PVqDvxem1oYL45a9cfkjw6mg8Iz6z7D1yITJ4y0H66QgF9mXPH6i5aE1Qw12c-czMY8RfX4qBsV2L7nW3RyaorIRHXYpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=hkNESfpMRbChGDP7oKHrBAui0zRlEaiOcuMEpfD5cwH1PAIiszM3_HNtC8-V5wA8Z7xZTvKCAs0NRaHO3NdjiVt69nGZZJVf_TdJPoR-2T1yWxhDv4ZB7jIWEh2HtyPZ25uKfU3W0QgZ6k4l5Yi4tAAcpJ2RhsKwuC7dadYi2-fbHj2sLTjAVEsH3lu0GVb-32bX0zGoUB1e23O_RBmH9eK6CoaI_sGoitMBBoh1Sgn_-A6q-M2NIxc7PVqDvxem1oYL45a9cfkjw6mg8Iz6z7D1yITJ4y0H66QgF9mXPH6i5aE1Qw12c-czMY8RfX4qBsV2L7nW3RyaorIRHXYpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=PwjJC2FCiUnFFYdNrL-i0bYxGElHu2rUQWieYJNl_loutcNu70pLGXoiyH8U5a_i3DFxw8mrztBZ77xuokouSgMfV5fD7LhaSCxVf1SkRtkDGxTHHWXQULOGiHXIyn_dUmBtaF7n1VUDbE28sYQ9TU3CoMLRosPLKy1-bbw2IwRAV3ngX5r9pnecbFVDH3KqDKwB-_Lf6kSudZZkHYyAkJ3rWMpUMf2GZBwPpG-xcXKDKaB1vnHleb7RRI2w5emoDwRZFs6Omj1dDrCjB59JVcWo536hBtCeIL0zqz3y19GNVX9kVUiJum8tYy48nHYfVMq_513VDohAgtDegnDXJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=PwjJC2FCiUnFFYdNrL-i0bYxGElHu2rUQWieYJNl_loutcNu70pLGXoiyH8U5a_i3DFxw8mrztBZ77xuokouSgMfV5fD7LhaSCxVf1SkRtkDGxTHHWXQULOGiHXIyn_dUmBtaF7n1VUDbE28sYQ9TU3CoMLRosPLKy1-bbw2IwRAV3ngX5r9pnecbFVDH3KqDKwB-_Lf6kSudZZkHYyAkJ3rWMpUMf2GZBwPpG-xcXKDKaB1vnHleb7RRI2w5emoDwRZFs6Omj1dDrCjB59JVcWo536hBtCeIL0zqz3y19GNVX9kVUiJum8tYy48nHYfVMq_513VDohAgtDegnDXJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9jsKHIFCwFrovADLA_GLFl4Li9Mfn_5bm8aOEMQ11JaeEBbpof0G2IS1EZqWNbNTQHoI0U3wg6R4KecfeufTTA1DoIJQwpmDWBTHbYToIihupyeeflFZO4TLtZgWYSWVOVCho-PxSZb-9LwV1RnheUrWpfEEEMHL4QtTwMzwscoAS1dBuoka08C8onDLCAO8JHNk9oyp6qI2YHqOHtWNsE0KoxnjQz0E3AKcTUJtmQxRJSLCMl7SnJxWUIIlofTYvEKOkGelgj8XYHolcthiF04PT6SpVa5IvzdJK7KSmWu1ba7Bf8iVyMLn2PMPhgrV5Leib_glp30fkA07Fjxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anQ6T0RgjZsgBvsnGOq8y3y7ClYsDpApEsFhkyphdvA-LbmYI8n4KrahY3YgixdeeKfy0sANAX2_LBMWwRRAIQIiA4n49og2-WzHIszHnrSoSjXEnWy1mpUb6VkidaPtkHmzDJTD6aKaTSktGPs7Oxb4F7Oj98AIWKpFN6eqBij3JOYQ9v-IrDFH3mz0L6bvy4IZg_06pIieBCQa9QjDcZaM1SI_Qcvo7_EI5eCeTd0kf95-NicjBbM5_FhiqQKCYflGBTb1fxHathWte5x3hXqnQFLEZloJh4ehFSIlQPiQGUScVBOVk3JTss1fVNL7kDDF5KhfVYjvpCVw2dBk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=MnT8cDfnLdN2c_7KXVwJ34ueozFr_v5tIirtFGPU7yP5KI6Vt1_MLYioLe7pwe9e-ZA5kx6LGSwbWIJsg-gi7GR6nIQwy_3zQHwFweU5kcdU7e3XMhXn9fi6gb0qLpfM5yrJdwcQ-qpor8roOmvTy7OqeTt9EFdltOZ0YKaxkeJap5j137zTRQhIShErIrLZGy9iMyZh0NWgeAhNC9-v684Rei7xPIg9JOo-kqP7CVc14ZfgdFfH7aJBJC-ILNX31V685DgIRilF8A73AS01U1Hm7ze7eHnfp1_-O91PTkPzP-6FONEbD8Z9lMxJNiDBZagWFdDztakkHFk5tzhtNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=MnT8cDfnLdN2c_7KXVwJ34ueozFr_v5tIirtFGPU7yP5KI6Vt1_MLYioLe7pwe9e-ZA5kx6LGSwbWIJsg-gi7GR6nIQwy_3zQHwFweU5kcdU7e3XMhXn9fi6gb0qLpfM5yrJdwcQ-qpor8roOmvTy7OqeTt9EFdltOZ0YKaxkeJap5j137zTRQhIShErIrLZGy9iMyZh0NWgeAhNC9-v684Rei7xPIg9JOo-kqP7CVc14ZfgdFfH7aJBJC-ILNX31V685DgIRilF8A73AS01U1Hm7ze7eHnfp1_-O91PTkPzP-6FONEbD8Z9lMxJNiDBZagWFdDztakkHFk5tzhtNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaPfbiXBcL_otGzILC5uRtzWST3UZ_mptq2s48Hy8WKWN2K-NGT1Ngjw9-1kWqYKxiXCph6XNWuK8h7VyuxbhCQpX8qnQEspw5V5kGohBK8C6_zN9Vz1zZrx3MQgtbl2zB_uOO4QGjnoO8shoCHuoxUk5c9UZgdQvmlsce88vWsEc-BMi8myZNrCMU04wQ3q28OvauVTgmnRboeqD2k751u1QCDduwm7prozPQS4IdtWpDwreTx8Z9V6VAyz8vaKSY5sftyKJZFivGS3zxEWJqDTLQAPTJgN9_1IMRqRJy0snxeByR8v6EygOJ9s9UThpM7q2LAjVRIO34EGQTkUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=P4VH4Wikgevl1RRIWmkkesXoVlLN2gMrg4c3FZ1B_7ctYjsGuZKfxBjaOedbETzPRIdYr9s00YlHA9Es3CMh_8FE0-PR9BJDuPFt0CA2UFUubd6q5vQH1Tx1BjRSs8PJ_3UiF8os6iba6i7dHCovUkkWqajqccU6N0viCPEXXXJ9eit4ctFBibdFhoFURqebJ1_A0Lm7NGyrXU2deguGY28nBdBxF5MtHDG1yURjRXfEvJIQbnYi3vpFoU4be3mKricTd4wa1H9_4qcuiYStXhzJHHLSLD3qRU74OUCzBHpLyRX7fZnxplbOqDr_d3jE4nwFGzy_3A0187F-D37UOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=P4VH4Wikgevl1RRIWmkkesXoVlLN2gMrg4c3FZ1B_7ctYjsGuZKfxBjaOedbETzPRIdYr9s00YlHA9Es3CMh_8FE0-PR9BJDuPFt0CA2UFUubd6q5vQH1Tx1BjRSs8PJ_3UiF8os6iba6i7dHCovUkkWqajqccU6N0viCPEXXXJ9eit4ctFBibdFhoFURqebJ1_A0Lm7NGyrXU2deguGY28nBdBxF5MtHDG1yURjRXfEvJIQbnYi3vpFoU4be3mKricTd4wa1H9_4qcuiYStXhzJHHLSLD3qRU74OUCzBHpLyRX7fZnxplbOqDr_d3jE4nwFGzy_3A0187F-D37UOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=nkiyBEPqBmB-PRjj2IhYQ9uenM-JPjQqBeqNxul9HWnjQ9lE38qgrYbQG5E8VuR_EWWldztJhf0xGX95ndf8J3DvdlmTF-WXUcdExWvfHIQFGBXw8eulDe8dgx7znuqUjFY1l9qmsmgOQ5jZD1aKttpz7itbm8P2TZe4SwIOb80-fjZPcntxY093hXL6jbwZeW2VI6CyI0ReoLnUMWX9pCl0srNCRevouOzb4gIRECmh7TcquNsZ48I87IR6A3rAD8HtTn3zBAiZl2aHz5EC3Iqj7FB1UEN6uOcAnuW2X5BAyVAwZTtRDLEeO0vFQQpA3a-g0qR9U5aR0R-TEHt_LiipxmwfnbuR5VjnExypCJJllwbaR2QNZ77uW3V-xnDdSyHYgISsoVlVy3ZesfhZEYbGT-Vh97ZR7npcnMqc1ak74WffUI-7R0fiLBTTVg55ndziKi5MDvbX7H8arMfqhJtxaHqLCV030XlM16ozh7VgQ0plqdOPSy_84awce9Bm3553Tb4WkR9G38h7WaM0jtQ-nuunSESfvpAVA2_6NlsE5Li6qnnA2tJUlX83yTItRizGc4VLElTAgQsFQWgrrGQNN8eIhEiZW-sc9uEqTFyq1UKvKm0TDAnD5LKEkiS6NTy4p7C0qTeza9NcERd9yR9867GANcRWCxua34nCHzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=nkiyBEPqBmB-PRjj2IhYQ9uenM-JPjQqBeqNxul9HWnjQ9lE38qgrYbQG5E8VuR_EWWldztJhf0xGX95ndf8J3DvdlmTF-WXUcdExWvfHIQFGBXw8eulDe8dgx7znuqUjFY1l9qmsmgOQ5jZD1aKttpz7itbm8P2TZe4SwIOb80-fjZPcntxY093hXL6jbwZeW2VI6CyI0ReoLnUMWX9pCl0srNCRevouOzb4gIRECmh7TcquNsZ48I87IR6A3rAD8HtTn3zBAiZl2aHz5EC3Iqj7FB1UEN6uOcAnuW2X5BAyVAwZTtRDLEeO0vFQQpA3a-g0qR9U5aR0R-TEHt_LiipxmwfnbuR5VjnExypCJJllwbaR2QNZ77uW3V-xnDdSyHYgISsoVlVy3ZesfhZEYbGT-Vh97ZR7npcnMqc1ak74WffUI-7R0fiLBTTVg55ndziKi5MDvbX7H8arMfqhJtxaHqLCV030XlM16ozh7VgQ0plqdOPSy_84awce9Bm3553Tb4WkR9G38h7WaM0jtQ-nuunSESfvpAVA2_6NlsE5Li6qnnA2tJUlX83yTItRizGc4VLElTAgQsFQWgrrGQNN8eIhEiZW-sc9uEqTFyq1UKvKm0TDAnD5LKEkiS6NTy4p7C0qTeza9NcERd9yR9867GANcRWCxua34nCHzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صحبت‌های وایرال شده سرباز آمریکایی خطاب به مردم ایران :
اگه حمله زمینی شد بهتره فاصله بگیرید از نیروهای آمریکایی
نه اینکه بیان شمارو اذیت کنن، چون ارتش آمریکا خیلی مواظبه از سپاه که بعضیاشون لباس نظامی نمیپوشن
سپاه میخواد با اینکار به نظر برسه که مردم ایران علیه ارتش آمریکا هستن
سپاه اصلا توانایی نداره علیه ارتش آمریکا بجنگه
پس اینا می‌خوان پناه بشن بین مردم و حمله کنن چون اصلا نمیتونن رودر رو پیروز بشن
خداوند ارتش ایالات متحده و مردم ایران را حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68541" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029372426.mp4?token=Nn168MOsgFr0GHgloPuDG8CbUuD_UEExVCh7TGcYG5dX7Mqhl-WQA_pVpcg2tT_SxJmuqP3wxUEjIPFZyayTnavamltpmSrY64L0WmIEli5UWW9Io31FG-e1PfLaoGP0x9nE0RnFyAmCd7qIJ-bqqdTJbPgj7_BAIb3SQ1OgtKIygokdMpirm-BAk8Ghfx3B8F8DjjaCjIH4k1VAW49x7xSA59PTkz3EUYUMuc5uwkVAvpGH8_WzKXkp4_9UpdG64YGYD9IW5bKmxzfGSR4ctQ6z12-mNzJVXNwJE8RX8I_C3Xn4b1M-pUjrbKGNUFOCi5Fq3fm2maz4U0nOdRPpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029372426.mp4?token=Nn168MOsgFr0GHgloPuDG8CbUuD_UEExVCh7TGcYG5dX7Mqhl-WQA_pVpcg2tT_SxJmuqP3wxUEjIPFZyayTnavamltpmSrY64L0WmIEli5UWW9Io31FG-e1PfLaoGP0x9nE0RnFyAmCd7qIJ-bqqdTJbPgj7_BAIb3SQ1OgtKIygokdMpirm-BAk8Ghfx3B8F8DjjaCjIH4k1VAW49x7xSA59PTkz3EUYUMuc5uwkVAvpGH8_WzKXkp4_9UpdG64YGYD9IW5bKmxzfGSR4ctQ6z12-mNzJVXNwJE8RX8I_C3Xn4b1M-pUjrbKGNUFOCi5Fq3fm2maz4U0nOdRPpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این مجری که اخیرا زیاد در صداوسیما حضور داره گویا اهل کشمیر هندوستان هست.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68540" target="_blank">📅 17:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgjhkjGLC1uTlTgWAiUN_bkgfTEkgvrB_sBxq_ZbpeuzUFSf6s-JcrLQzUIzUZ6oHrmHOO9WhwdAKE8BSGxTqxwoK8bF0534nqQ4wfs2144aeLCFo_i0tVM2ILRKb4A5Lu6VOaD7vtDZeDFrqVdIH6Dmv2n-ngz0RMRV6mR9CvMZBH_V0ekg3EUVaMSlfD8_pc_DYGlZ8vrpxcROs3cNDE3UJyQnn7Gud9x4Gp0snM506RIL27VDEayUkV5PGdIB8wjgvBaqnmOT7bYCYyAMfWTIF-GYy4H9tg80X6VfGR1VQkgBkak-WsXpvUe5ZlQMoeKnU9uoFxOA7-TNxpZipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان انرژی اتمی جمهوری اسلامی:جت های آمریکا صبح امروز با شلیک چند موشک به سایت نیروگاه هسته ای درحال ساخت دارخوین در خوزستان حمله کردند.
ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68539" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=ITQG___TVqJGSbY0xyi0qoXOf7MLJ9wI5Jj3buK8zQKREmzVNoflLqcQ9vcpxAEJe31yqLCnEi9gR2FyYRTMf17-BUSPN8pAwaBtmjxuS5LP1B-oa9Vx21H2VXQDP7ZV10tzgCEkW_Ovq5p1OJVSXc98pf0vLpwosUPGjaavNlxzEF6z6pB_Rzf8EGzqVOSaBGIRbHPU4Z0jSocLdxXg1x_WfTw4WGsWvRs6tPpi6vHa74QkBtRbxhzT8u4EzF4J-G2p7963LXxrirRHnkvIHdmxqbAsA6u_MCOQP0qnI-jJLt8WWNg2Caj66ZysCVJtbaVyDdMfMYEg1Z7J-zurCLtw5EcF3f12CIw3Ofm-JnnHdklw_JSLk29le496lx4QTGPmrjZ07GB0MtEFLXfaA6iH6z9o9ovmdTv1cAMM9o6sdCimMbq1HINd6Mx5Si-G997IucYux2Lzg5UezQVDaFM0oaoj8joFFoKFN0ay8Pd8xzpmtMlTT-94eQbtlFQpmRF3yUdTPVvQrbA_c4imlynR4f46VP6Hi-Q0Tlr35EY9KmYWTKlf-4FaKfiePrbJ51gOL5HhDX2S91Ph7VIIDrrDpXxpvfUSDNhqMRZyjZxlBYQOqkKjw2cBaPKMlkdg6ONnyESbE77gLZCV0TDD_CTdr44xUwHk21aeE8wpJVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=ITQG___TVqJGSbY0xyi0qoXOf7MLJ9wI5Jj3buK8zQKREmzVNoflLqcQ9vcpxAEJe31yqLCnEi9gR2FyYRTMf17-BUSPN8pAwaBtmjxuS5LP1B-oa9Vx21H2VXQDP7ZV10tzgCEkW_Ovq5p1OJVSXc98pf0vLpwosUPGjaavNlxzEF6z6pB_Rzf8EGzqVOSaBGIRbHPU4Z0jSocLdxXg1x_WfTw4WGsWvRs6tPpi6vHa74QkBtRbxhzT8u4EzF4J-G2p7963LXxrirRHnkvIHdmxqbAsA6u_MCOQP0qnI-jJLt8WWNg2Caj66ZysCVJtbaVyDdMfMYEg1Z7J-zurCLtw5EcF3f12CIw3Ofm-JnnHdklw_JSLk29le496lx4QTGPmrjZ07GB0MtEFLXfaA6iH6z9o9ovmdTv1cAMM9o6sdCimMbq1HINd6Mx5Si-G997IucYux2Lzg5UezQVDaFM0oaoj8joFFoKFN0ay8Pd8xzpmtMlTT-94eQbtlFQpmRF3yUdTPVvQrbA_c4imlynR4f46VP6Hi-Q0Tlr35EY9KmYWTKlf-4FaKfiePrbJ51gOL5HhDX2S91Ph7VIIDrrDpXxpvfUSDNhqMRZyjZxlBYQOqkKjw2cBaPKMlkdg6ONnyESbE77gLZCV0TDD_CTdr44xUwHk21aeE8wpJVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش امیر رولکس به حواشی ساعتش در جام‌جهانی:
به جا اینکه بگم فوتبال با ما سر ناسازگاری داره از کلمه خدا«داره مارو میکنه» استفاده کردم.
چهل چهلو پنج ساله ساعتمو دست راستم میبندم.
اگه یه سرمربی ساعت می بنده و لباس خوب می پوشه که اشکالی نداره.
اگر من زنجیر طلا مینداختم  و یقه پیراهنم رو باز میزاشتم آدم خوبی بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68538" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBAwf68H4p0-RSzS_qwyip0WD_KKorsWhvJyToEgQiQ3v2ZnHZccyU58NQEGJn-HQNq56Dwu_e0n9GIGgUPgUkPjrr9It7Y7CtHfVXhsOyq6eLERlfhGf-DixVwCCcPKKHsQ6D7ZgGgQFRjo6GJDjeUaONQ18aUJYpmBoqFsu5rqmE6x-iNvVO4d8VDqw_o5qThRYjeRZvIXyfVaVPLGl2N39hZhLrSUumqUT2tF3yiHb2-0IoWAmtl_8AgkElxTTbjbpq_FHEgz4vUgcRibu4oRXuioQCoOfMUhj8qczItpGoNn-XQva74yVRH7r2vvVPD0q8-FCzpIpxFWg9nqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پرزیدنت ترامپ:
جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندزی می‌خواست انجام دهد و قرار بود محقق شود. مهم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68537" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUCRt9jonesTjtkK5vegvTcB5Xl6RVJljE1FFTRCtdPbk8hw9Evxo5FFIzZ8DM96BSt_3AvuLvKyx2EcPJxJrLcr9d4SgrYqIwQqwmjv7dnCVzG4FtL-cotwaITiO9YKyItl-tsiJKMKMtK4HjPcT2GLC5_cPr3e3vWWxy0rs3aIejDpzKXdAKpuIl7e2LTdEoZJLpWPz6dJtVkjsAtvQXxd-CV44k1NMYYTSy3QRuVvmG2l1MZxBW6AR4aovFSByPq8AP_NIxocy9g2-qXznr-O9VyAaj7_tlMjVxt4yE4OxM2qFFqMfr3YbnLGk2IaAHTUAao1XQ8fpMYFgTnZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=Vl0TKxMzk3m58Ok1eif4ecdpLuqTsY3CJLKar9s8_VAYRZW4hhurOznqEfyQVVRIxHgg3PhsSdIBE66Aa-QnqfXIHwsrU4V9AZWQq00xuI_-TfHofsmWhhy_CLrwWI5zynOYkCh_e5K_Qi4pRN0z3nCKvMjPRjl_2M5wQMHSOhrxb_hCq7ptq-1MfHi9cfO1mCugUieqZJP4E-TnrS0ce70OYx5ZQpee9WlkvT963hilmoT6AgGDyoZw5Pb89G11DAujIk3CKx9YParhIWjJXpKjYPFBHDPua7vA-KKSoIkSqqH9cE4vLjN6-MzjrwWL4Hl5lR4kV-a2n6b4pumF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=Vl0TKxMzk3m58Ok1eif4ecdpLuqTsY3CJLKar9s8_VAYRZW4hhurOznqEfyQVVRIxHgg3PhsSdIBE66Aa-QnqfXIHwsrU4V9AZWQq00xuI_-TfHofsmWhhy_CLrwWI5zynOYkCh_e5K_Qi4pRN0z3nCKvMjPRjl_2M5wQMHSOhrxb_hCq7ptq-1MfHi9cfO1mCugUieqZJP4E-TnrS0ce70OYx5ZQpee9WlkvT963hilmoT6AgGDyoZw5Pb89G11DAujIk3CKx9YParhIWjJXpKjYPFBHDPua7vA-KKSoIkSqqH9cE4vLjN6-MzjrwWL4Hl5lR4kV-a2n6b4pumF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ_JT_uaV2ytqeDQBxAvjVCdI-upeY9k4pn2CXRkRMNXFxjI_XTnuJkMp793NVhnr2wdvPjEdjxj3Waq5d6HG4-wdeBevG1ptVYMjeWlc6q38qC2DWdZzWzQkQYmdHAesUR8_xQjgdHLmZWZT79QxGNqS_-kBQbdIrK3QbqqlOb3-OjTRf1vb99vTrw4sh0o2Mv9KLcdfrREStGuwsN5qYnbGbXsJKe0IC8gbwGiGLVBJeOCx7_4N2JV5XEcSzoEB4Fxcq6LAza7gD5XkUzh0Hqi9qcFH6d-ERE814KEL_f3JDgRvl9SFHXrVqOku8pvuHkiKqg3QdtKT1raiM84Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68530">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326d421018.mp4?token=YWfo2OBjsy3Qnc6nzb8_KnlfPcaghR6Ra8KiHS6kvhLbItu_c93JB7x0te0L2c9lNlpaSK-7OPjtewko7jOp_c2GiBLdik6RRkX-mv6Rp-T7aPbOGAuBPw6vPS59XkLnJFyZxHjj_FPp25rdOmwCuupWCGrC4RQoLg_lCDdVTqk2SL-u3u5ba6JnZS4PVU3OXxtlShWaUfSr3z0b_TI9jQQ5LWISw7_gJZiC_r2I8CeY1vSlsw5CWfSw2VhX9s6jbqeOVkltOxvDDlnVv74oof_0-h06yY11RpYCymkcC6YmAMBGEsIN3IgKo1zk0Hnxep4ppxJXNiqaYQ0rLyTJSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326d421018.mp4?token=YWfo2OBjsy3Qnc6nzb8_KnlfPcaghR6Ra8KiHS6kvhLbItu_c93JB7x0te0L2c9lNlpaSK-7OPjtewko7jOp_c2GiBLdik6RRkX-mv6Rp-T7aPbOGAuBPw6vPS59XkLnJFyZxHjj_FPp25rdOmwCuupWCGrC4RQoLg_lCDdVTqk2SL-u3u5ba6JnZS4PVU3OXxtlShWaUfSr3z0b_TI9jQQ5LWISw7_gJZiC_r2I8CeY1vSlsw5CWfSw2VhX9s6jbqeOVkltOxvDDlnVv74oof_0-h06yY11RpYCymkcC6YmAMBGEsIN3IgKo1zk0Hnxep4ppxJXNiqaYQ0rLyTJSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای امنیتی سوریه یک محموله تسلیحاتی دیگر ج.ا به حزب‌الله را توقیف کردند، این یک کامیون خیار بود که زیر آن ده‌ها موشک کورنت ضد تانک قرار داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68530" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68529">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
ملی‌گرایی از نگاه خمینی، بنیان‌گذار انقلاب اسلامی:</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68529" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68528">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=M2sB9uMkf3D91whPzRn8ccUXHJIkpNuVYLAffZQjf-eYnA2GOi58rq7hAEAEvCsdwa9PgD2uvHCzrzcgvO581U9--gjKS0axFWrQjUgQUYLOfuuIorgJTkiM8-4127P2dmbaK8qHU0XDIU5UG0kT2-yhehPbIGl_SM-41oCUlWQp_px5c6-FuWDF0YVDn5VUkPyd3cNDrkFxwrBtAgPvYQj50QRT4rRRT5rTrSbkSElBcSDsl6f6Phwv6qpB1heAiSS2ilxmwyiEuty1HDPw0Ra5wkRQezfeUOBK_U1ij5Kk7hxItuc-GTOvobTdbHRGPulnfHeeo8l_4zMTEljyWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=M2sB9uMkf3D91whPzRn8ccUXHJIkpNuVYLAffZQjf-eYnA2GOi58rq7hAEAEvCsdwa9PgD2uvHCzrzcgvO581U9--gjKS0axFWrQjUgQUYLOfuuIorgJTkiM8-4127P2dmbaK8qHU0XDIU5UG0kT2-yhehPbIGl_SM-41oCUlWQp_px5c6-FuWDF0YVDn5VUkPyd3cNDrkFxwrBtAgPvYQj50QRT4rRRT5rTrSbkSElBcSDsl6f6Phwv6qpB1heAiSS2ilxmwyiEuty1HDPw0Ra5wkRQezfeUOBK_U1ij5Kk7hxItuc-GTOvobTdbHRGPulnfHeeo8l_4zMTEljyWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آتش‌بس با نظر آقا مجتبی بود؟
🎙
پاسخ
عراقچی:
این چایی برا خوردنه یا دکور صحنس؟
☕
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68528" target="_blank">📅 13:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68527">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران:
ساعاتی قبل، دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68527" target="_blank">📅 13:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=dDostrmmuyTYR34ZaVVtplpTFKXP7J593f3XiQA-eBR4YyyVr1qIYA4dsHM84nQVqT_60CIhxrQD7UaFbcwmuEJk7NRf2QBAzUpydo3pGinI1nXctxUuc3_AtOQ2Dtj_89way8WJ5Hmi5LHdWeL8HMaK7tsoOEaWvwTqvWLkGh9TtaRFDgNG2tySDM0KvWp8hVymhulLesxIzEwwgSye6KsFMhtgNx2-n5FAv0k0lmcv67nXYxIPUOzfvS8udvCda1WeuAQnC-m2AI5sF995YrosKElPs9UMYgtVF1orJbP_iGynXoo-n_sPOTqPx35OcXefP0HBjHpjVQM3XSWpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=dDostrmmuyTYR34ZaVVtplpTFKXP7J593f3XiQA-eBR4YyyVr1qIYA4dsHM84nQVqT_60CIhxrQD7UaFbcwmuEJk7NRf2QBAzUpydo3pGinI1nXctxUuc3_AtOQ2Dtj_89way8WJ5Hmi5LHdWeL8HMaK7tsoOEaWvwTqvWLkGh9TtaRFDgNG2tySDM0KvWp8hVymhulLesxIzEwwgSye6KsFMhtgNx2-n5FAv0k0lmcv67nXYxIPUOzfvS8udvCda1WeuAQnC-m2AI5sF995YrosKElPs9UMYgtVF1orJbP_iGynXoo-n_sPOTqPx35OcXefP0HBjHpjVQM3XSWpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpl7i8B0ASsIqfEcJJLU0r8dR-4tt8ztRj9lO8yLqWGLzQD88NbeBO_ClLxAt4FsMt2Hn0wHf4w52Ma1qWhm2N0aj7uoebV9REUNsu88VwfxXukLWfwVUAGOCdr_kiKvqX3S2mFoQYkp5630-HgFD5o3n17TsQf3NTLEVkRX_sRX7Nj2e28dJbShXRNdnH6aH-3_RhWLuzjuuLVk4OE34PfbPhE12F9mdmAnficCDFu8EJf01Y3sx65oryc7vp8IiwDIlmkFVAH3iklXzq0XVtQU1TOgvkTFLTrTBEEBbSTCBDVesNDmU13elCtKd_sRS3-n0VL_uWnhjJDFKIhmUhaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpl7i8B0ASsIqfEcJJLU0r8dR-4tt8ztRj9lO8yLqWGLzQD88NbeBO_ClLxAt4FsMt2Hn0wHf4w52Ma1qWhm2N0aj7uoebV9REUNsu88VwfxXukLWfwVUAGOCdr_kiKvqX3S2mFoQYkp5630-HgFD5o3n17TsQf3NTLEVkRX_sRX7Nj2e28dJbShXRNdnH6aH-3_RhWLuzjuuLVk4OE34PfbPhE12F9mdmAnficCDFu8EJf01Y3sx65oryc7vp8IiwDIlmkFVAH3iklXzq0XVtQU1TOgvkTFLTrTBEEBbSTCBDVesNDmU13elCtKd_sRS3-n0VL_uWnhjJDFKIhmUhaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=HYqQ8EaQ75dqbwSOFwctMLsLhISrpKpxlCpsiZBdGCZhcFaUW8aXyHkvlmj8r0mhJf9o8pUirkcejGfKig7RXBpXekrV8SNKOQ0KWx0nLOEdjP8_OmEkrLFlQn4i2jdMg3WLo4LAyETIrVppDOMiefUEvBPhQrfvH0ug8pB93luO-GMTjKgw4LtaAozFW8CrzXhqGyeUOzGkA-vcjbXx2Mp0HKA9pC-JxiSQCUtYq3YPIR-wiaHesTEZf2igB3gv4s_27cfOWccD5gXdhnVH581bixL7YttM-qgfpOH5SvjN2pTSvAOTZ0CPOxBQXMLUZZaGmt1OfSOr9XGvWCLxdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=HYqQ8EaQ75dqbwSOFwctMLsLhISrpKpxlCpsiZBdGCZhcFaUW8aXyHkvlmj8r0mhJf9o8pUirkcejGfKig7RXBpXekrV8SNKOQ0KWx0nLOEdjP8_OmEkrLFlQn4i2jdMg3WLo4LAyETIrVppDOMiefUEvBPhQrfvH0ug8pB93luO-GMTjKgw4LtaAozFW8CrzXhqGyeUOzGkA-vcjbXx2Mp0HKA9pC-JxiSQCUtYq3YPIR-wiaHesTEZf2igB3gv4s_27cfOWccD5gXdhnVH581bixL7YttM-qgfpOH5SvjN2pTSvAOTZ0CPOxBQXMLUZZaGmt1OfSOr9XGvWCLxdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
