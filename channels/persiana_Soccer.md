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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 20:21:39</div>
<hr>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDEG-_-1ckq3-P6urZ2KnwbYNW6gN4isMWa_QGBM9-GXX8Cq5sf2VKkoe6rpJta-S7L7mGVqKJ90hjJOzSIXRkdr7pq5V6Y3DzyH5bVAFoAr8oyl-kbSdHwHiaHG44MU8Wwi21_Jbd26vQFjwh5KL1ZIMxcz6FRyjG6YQze0CdsouAr2N37wMLHlxqjcfUEwgR_q1bTJf86JbrTr6pjTAIMQcqYif5IxjKLLHeN21-4z1c1GYy_PIkhcnn5HA8bzpZrTwoUjhv-Ka0KQSccmswAJeq9JsEVsn7niLuHx51_QnvSoNB__aI1glgtXbq42OL9pS46ZZwvLKFcQHrN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLBQwS9JAplo0wbukOKW0DqSG2TNrn9ijOkl5KoGNMwAbUOLNSI5Yh7tvjawUH-nHDW-UnbI_8D_82oUjydbVmSOGa0gOfkXdPwsFPaNbUo8rMI7nmjk9VgvIC2BMRKPIyLJZclO7ELbM5WGNQJFocZVq_HZlUaLvzM2pmC7dp1_TeUgtfpOanVvNieWuZkfyMRT-PNb3CjGikY6JaFrg24vgvZiiOgL9Bs3TpDoBGv9vSvzYKo1mEtwnUZCp9MAVNWr07-stf_X5sc5jxbh20qJr-cF2LT4cBaGGIikYXKSpQhXD-IW7p32jAy-UY_q_C2CuLeVvr_r8rMqqeG2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebqqgFHZl14cDl_aQYn8j2DV3w9qpJP1Oh2r6maDOzMM6G__zwfFrkJR6fjVPOck3RKYRfsAtg-24kZ4Q6ye_ItpeNGSkocq53b2RDivaBdc1chYnpaFaEPGLMtMiaqemlzK4ANsywnENMSnemPO8-3eAIfkybUTOaA1-JM91qGVmChBva5B-LnvfHkV9UNgzSgLzRypEq6vx8j7HNgXqnQNsp7Rc2hyPrPUTxrqc1aYppPOQktiI8Aaq1-KzrnUCQDFakbKSo3hfvuNAGwCvp9AeZ7QEYmBUL5T-IuMEbCr5WloFs53ZIwo2CWegZdNPunxlS1z2ERzkXZiOwVtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM0MSqsHGFLHU3HWnJxrlC8LzXq22zgqVqZ_mNLGIWwSg3fYVo6gPC8fLyIIbc1qXzSsOinwPTMM8eYlWsuR46OL9cFyYXxLWzccUoP2rRm4XVKExUSahWNSY3NDq5SjnT-uG2PwoZ5QGKZK58ApH4oRRlEPTBzQ0vhj4xOq1UxneVaWcodZzdbOm4Pgh0L95DGyChGM8-dVoxtwtmkHNuqpbRLnKjamUIyW8DBQQfSnD45ui-7FDGq01_NJKTY-IDQYJvig5_JHLHoRnO5EsHLiShqZBnx22sKAq462woeysKArNAabl6Pbz-fQrreEfWo45d0TZ5ODhEKjBz62Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfRnNJlIPjIdV5eNBGgB-XzM9NnRfUQHKxDP1r2-jUszIumufn6tS7ADKEF5J-dfcPmQpWQrdpPemOMzw_mUs2Y--K2DhtHJ4meZKSDxCXN9FAHKdxgMXrLFwHVcXUC4FhBU2mtYlDQ0u1NcM2GjhohWzn2hdec-W4cLT2fT8K2zqBwrJUltkOuNnc1vqy-oLzDdL6PqeHXLgKLpkgDN_t-J7M75iVRZnDlaC0_xBNxD_Yjy3qsEHS56kpLGR9TrdbEIHMivsBehX3MuHMHstD42uQGZskjZ8UP74Pv3zLwmsnYcFjLFyyXgZoG0DTGb8CgiPrGxJBmKtUtEafSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT39W1SulUzaD2SjX5TC3A0-NjJr3tfeOBhR28fc_m3oqknWIKn0lv38yfCrpAZQTiKntU5d5eTweUCPZHgkc8WzkjwYpqpwmEEzegsfpjbHWvPwL0SM80d5KVNc3AZDv11e68PTVsV3oknZUr-VthkFU5ClcKLEqglAn8NRY9LPVvrPh9nz0mXK5rjU5i5-RI1KLvt9F0M3tfHFL1ihrwW7YEO3aV4RwbZT0A2arieOs3o0PodkHapVHzpOLUWTy53oUModDmWfYuhWGDTRwP1PKt7zPFZWrjSmZVVv4iMMFwv-z-bjU7jsw6myHLpk5-22GrKtaD3L2FjZUyJrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=sfjELI-Q81uLhG5oJ1GW1KRbzGK8pynJJ4kCGXxnm2syrYj6U-tbATM5a-4YcY8qz5j-1NBNhbRKIC_ffeDwpeRVgODBk9HKvbvzARwU20avh8hoxOQuOqgLsNNCJwQHer-keSZ0D6n4Jr8LQDxkpPGEK7XQmEQyWg96BmMLjmUSajBedsTVMU_u7IrUAtTYViBDO1573F2z3zjxjHx3xOHBZlcYxO2UqsDbRo0WtMaDLomKzqduDc-Zyah0NFDc2ttLDiA6EuoUEDogZwqI4j3bjdQRw-WM657RhzuJWl1XRvXZ-Jdbit4won_vqLpVlxHmBCirp2EpqCXhOpcbjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVWwYtqce66Up02mZbMO8WwkhqOZwSd_3dUYKSLFFziRNMcCfYWWYYbCa5TFKc68HO1K3rI4FJpB8O4nX_-1A6gFyqHpMqf_8OHVm1n563sKdbnQIIeOBZ_sVHxkU8GT3TVLuskOP0GW6baVTETkyPzyiKsFHfeR86QbM_vSviY0CbG3vO7t82bMH3VkyCvb4eOV53qE1aA6700LBWt7d3Ih4y1HyMruqXXn1uqW--z2zmGmpk9nTNhCkUN7OYXvfv3q4vyBRXTZf63x0ij_iTweIFKqbD4KV2RcoAcFfGjwm1uqwoz5SqzbpWus9aOfudNOYSh6yXPaLhYrXw60dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/26152" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN-i0CfJ_YCFBMis3ucrnqpkx7jVRb8doAb1JgIoDebFc-X2p8HgUAdDsqShIy2zailyFQUn6Fty_upEZzczx-PT9G2clRp9cGnxxu-38Kl_3h589T8njKQ9K5HYPVfGgLzKoddaOuf8U0KzhgsO94GTTc59PyDKUHkrbAnUt7s4iLiVZud7fhpkVnXZymi8rGSTBa-z_s7ylef1bgrq7vfb5WW2Vd7zZ7k54we_YqWDh6z4TeELUyTzmGFZPO-b8CBX44yyFByXVA80qOrgGsgXEuBO9MRCI7GWwtToVFJ5Wla37gNIDJxx46fOwNg33J6R5g87TrKhZblkgj3eUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_zMz8EJkDzHF0cVYq8yYTTndy9zakXdVviRYjRXNDSkKESs9oxFjqmKFV5Mma3KkPr06z9UxRICabX3sXMBg6QhpLbIOAwOFDdiBQnQnjJEaYv6MXKKbpmA46TI_tG3ersSQwlBej25HEx_3WroBNKEunJ3gkOv27XdEfZY6hjKDcqwaiZLx6Il60rX4-kvYRFxoIVjtdKxT01f6L0UqQuBTCqbOxjbVnADL_Cn5WvbDrw4B4yvHmrAzbTVo3UmLXsDZRwfD-7lvoXgrUupnxRPh9lFPK0flBPejtJtl41thy7he2jtz0LtAUdSP_VX8PFhOYlRYamBLjatI6XN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=fIPsuwmWoYM6UEpL_Q0-jTAw_RvxWeAOzFQipoPxQuaJnKUE0inX4YXKBslwHtIRukn0TPzASx0iRd0PF-BuHUBQ409xnUyLHJm6WhKr--e13LEKUmd_5NssXQpaE1lXxipoPn_5_P103GqZDrYKE8f5PSH-IlGKpQ7_QsVCOSP80y9I99LrN_x6u9xy9NYcjy8YpaOLuA0fkN4Fy8SEw7K12M13mmTYlf7th3j950jhMcvv14XbpdX1re_W-pCnY1jnHOBt53IvXDKHh-D4pROEi6gJbPFKc0OSBpDlbVbaz8A4slSChP209FCAzJgn-touC9DxJy1AXqGsslJr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=fIPsuwmWoYM6UEpL_Q0-jTAw_RvxWeAOzFQipoPxQuaJnKUE0inX4YXKBslwHtIRukn0TPzASx0iRd0PF-BuHUBQ409xnUyLHJm6WhKr--e13LEKUmd_5NssXQpaE1lXxipoPn_5_P103GqZDrYKE8f5PSH-IlGKpQ7_QsVCOSP80y9I99LrN_x6u9xy9NYcjy8YpaOLuA0fkN4Fy8SEw7K12M13mmTYlf7th3j950jhMcvv14XbpdX1re_W-pCnY1jnHOBt53IvXDKHh-D4pROEi6gJbPFKc0OSBpDlbVbaz8A4slSChP209FCAzJgn-touC9DxJy1AXqGsslJr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIoC6dgeHCxKfcGbldjQKzc1w7B8fnugWuFkXCPz8xQphTh6iHNrN3BSA5uNd8JYgFa0mJ2pIFWbhUIYmhVgAtT9CFIukecWcQnSNCbiu1GxSORUc4zwRgHdT8_BDM9ZuUcU_aB1zhcEdiyXhkBG5b2hPxDSLNfZzwzQHmhYqM1CGHPxlwwheibmKPxPGuG4pt6Jy7-no5J9d2n2GDCLhBQdKBaPiEsatFwRE59mLpdsM2OHSsiOiL6k8d8F8YSJ6QOrpBFOAMEiqNF11VdpA6IYkBhJBS-OSveMemvSKoQHdZEF923uBdQ-pyBVUCp4P78XYetlta4uX_cU95WuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX7uFQo1ZBTrj0BJT8X5rvI-IgOdtoaV6Hr6P2Nyg5xiDF7oIVuuLrtclk7c2GHGHkz7lK2Uv-Qj9drKk2uymTpzX0hWW2sl6E_JeqBXYYRVoOy8HUof_9fFZBY4CtL0CnGFMXkawZ1zrawae_rvIlD9ylJ7mUvmmTDNHWv5XLyKWBbp79bDf01-FLicIs0dpFVjfUxBIo3vJa2smkpNfPJFMq2zken7lKJse_un8y-9imbKRlFZUNREWcF4zzZM1Z7vMtlunv_vykWck6yZuR7PHpRYRK9VOa7uVS0sb_SpgIzSFW7sLkWNB-soQWO1d1YlHJd7d7_kyGWDWf94Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6eX1D63Yzj2NHWsx8PFDqO6diGPFkAYWzIwsm4XdYiKazjmth3sA9zW45lNOvRJmlRYWo6ZQNvOaCubxPHEQ-7tZyGRhXZ-s9a9SIuHTEVyyegTN2WkBlDLwgQGnqp61VhTkCA36uDElaPuAk8wfjnH9S0ShzVJDB9fBrI1hlmqJy722kZSNU2FCiz93zN36AuXHZSXb-lPFuPoFN4aYlXyiNYe3ok3Y1HKFHbSaj4WFPh6FTmZ-D1brM8fSruTscBJ_EBZH6RWSp1CvuUfwvX9LpyJRuZKdYb7mmY2R8lM4oVCADAL3z8C9FGygQHdkFvcw3K6OJ67T4iguK9sMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ezu-ih1th5T3y83hWFqPSqrWD66PNyytjAzVDCDdLrgdRPbiHwhwF85nTbWFy-DDv_r_NROl5rWx98Gdgbi_1GUdJNZs5rWFX6fhashxL3AOA1yfQS_Pcwq2f4OSUZdFR9LIxWEMcox-94mf6egCTbo1ig7xLdTmyUf9AI7-_P2cBp85HVGMo9WsSDn-IatMOaOV77wzoc-MC8PQyCLl6VYzA9Df-pv-ozf4obJmkpJ-n_bxc6SbrojtjzcG730qsb1x95yaL8bdgEKn_qHP9aUdidAgbQpWjGFjW3YEF32aqpQmoiuWxmUVFgbA1DsZFyWag6BEy5U0I6-dwwZm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iy3-TIyKME5fXq_N6s9V7-EgLXXJfLBv5RAJE97s0EPWMxlR8KGD6jSbTKHKFvXO1c1Fm9tLHoaHjkqoLjlFkfSv0hEsjM28B57Tfd_96dw70c6yWO3jYSp54sGX3XPpKnE-1kWhEExzAVmskOEDJA076YGjpSDtQCPMfPqh3kjijofYqHVtCfPhoOCRtBTcsHuL4qhvsaVZIBh_LHx8J7w4jT_fx5fFwIn1w5IJO0s8ZABZY_0ipz_Z4odtuXLwEUA3SyX4kf0Xx86nSL7oTYvLYpjyjzNeXibA1guR0xwvoYUg0NRwuJsBw8vLaQOKywhdSvMfMQDLDrxm3QKhXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfSWo4Pg6MXeq3DY-yHM1vuD8Gxu3mFAlqDm5fZl4exuv7cksv_jX1uxjY-Fs9UvVaD5RR6Bf7Ul78dY1nie6e0kHesWv4ztwuedvgZO67wz4KKP06quYQsqDL7zeoYr8zi3GLH8Ukfs2XR9kOLtY-GQRzzkkzYcL_v1spluZkQ0ex8rsM7aozpyaLkfUHKJpKbUdZV5UcFkM-9qzgKSyWjVH3Lc8WU4RhsE_181Wim3yCUxq1wp8-FyqFW1Mos2wOaARmlo7OhPnZDtw1JjJIoLi8lzKb3L5DpzV6I-C68bz15PkhQ_DzelfLozPs3XmenSokNpt0uRwxfuV8gfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afcXrHHHKPR9oRwkIbhzCQ0_KLkd3WOFsHg2sBfTyR-zz4ycSBHJec7saz25o92fgueme0oJ9bEFin7RO43OkS1y6M1u3X40EqddaICIJ9Rk9ZB2BJfYsfehWZPVdQP47i_8o_QeZ_mRbPCMu6P4KFZPrhUU6G1lMo0lfLQHEV9fa4yIZvOQJ0TSTf8sUfZ5mi5H4eT5YBuv7hLbwzELHiOEFUhdjMY5Jcl2_UVrisBfntnDLJQdG4RUF71KXZ2UhaMVZHbhcwqnXJosrVmV1D_WkI2sTrcG8BEMh2xGdVQ4Qm5C2BcT6buGGOQP2VWEOMPdWsGnLnAimNf0zNsR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-L-9sjgKp75l_Ww8yt-4Hxy1_N4euOVcPM79irh6-DIR5afaY4icpQqb_zKj1ZC8Q1PMME16KG0do6OcKeoxxFAyC7FxEGMNlhmpYMI2azitz-i1GKY4MLqrHVw-Hl-EpKdkXiIKbR6WG-IFGIUsC0OQ4Ox0qVShzxDwxfWetZMbfN5-k0Cslzxiz4HpmPzUu4yI0JWer5nCv6za2Z0vHzK1DHBeYSG6AG1hH4_VEVd00tb5yGh-q7MfUhe3QADh6zJ79PhEdwryDnMuSO3vVAa0hS0S2giyDLgiEuafOaR-YR0iHucYWtzLY4s_wbxvdND4WaoX8P19w_GuZ_hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=NhsRYvIW15wRsHeuunSp0QZxX4aox-X15zYxkzXe0GD6GLQg6lW4s6hJItFTzhV5Gpe2fKdv3DR_KV6zoRZ_INYo_1Isd9LpF6nGKPWRXca-EtXaZ76TPPZrT6wkC4gs4qLakfp7VSp5Wz2dKu2e3uManzarFrmf5PSPMNlLmK4au14uXJt4_QhEXnl_agHgvxQDhIKciCdlb9NqQTfx55Tovf4YialkIHCgUskxX3x3Lfmj_I73E5PPnrIcl_DRGqYEl_E62kj--kNfJq--YGUc4Wacj_HxFzPPt_qwj7MYr57XCmY3jEdjksRkkRp5ZAln958uVDr0PYr6j_E2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=NhsRYvIW15wRsHeuunSp0QZxX4aox-X15zYxkzXe0GD6GLQg6lW4s6hJItFTzhV5Gpe2fKdv3DR_KV6zoRZ_INYo_1Isd9LpF6nGKPWRXca-EtXaZ76TPPZrT6wkC4gs4qLakfp7VSp5Wz2dKu2e3uManzarFrmf5PSPMNlLmK4au14uXJt4_QhEXnl_agHgvxQDhIKciCdlb9NqQTfx55Tovf4YialkIHCgUskxX3x3Lfmj_I73E5PPnrIcl_DRGqYEl_E62kj--kNfJq--YGUc4Wacj_HxFzPPt_qwj7MYr57XCmY3jEdjksRkkRp5ZAln958uVDr0PYr6j_E2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHwY2KksjQODTyZ-JknPdBvspQRM1bX9QLZaNxaE4O6_4Sut92v4kdGIHitX4xk_85qmNi_liMiz27NN_U4xpOA9Qnkw_26jInkDjeM7hsHJqYylD1amPWpdPIpPbHHXGxYOlkc38eVJoT6byAYpulFfApHCEusPRBbKLixFV4PiXAm1g_MVNiQohXwsggQ923uCSsyBuevx7KFSF0um6803x9YUL0sTplVFaTNHFUKW6XO4U4lKJwPNKAcwnBwSBlCGzmsObcEoYgo3xmdpk0GuA7wQBJv8LIB5KuXL_0Gpb-HIAwK5u20X_-eLOkFi4UY5z3x9YwI_39N3J7GUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sftX0W9nj_Y6fQEZeT9GLtDijRZkt3w0pJcvWDYA7n4MiRJu3DAIwanVNKpgZhSGy0SZe7MD4BcCPaH_-8z2EWCFxWe-ufmRyIib_4Z2RjDgiKmbnf9LCWulFcwlutL7RbzTDO97jQoDXM1ILj-vKmuQTg2mVffB1Qu9yMP0Ort1WFVraQE6zBPsydpt_5tVtoAiVeOKPgTYORDi6Wy0iCW7_0y_drhHY_HkyVKx2mK_aQ0EpYvun6Ynzlbfzq1kuCpJIUPUNb3-x2pDdFXsbwc_ObV9zrzDRud9SgSMZ07ZALz0I5dZ8EcllQ4liD_0Y_IP86jmNnCa1tWdtIKBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gom1r_2UpwmMSlVfe6YTTN485mJj1PQ6o3XkrksXXPyM7A91GLVinAGSBvIDGpguBOToJvewj0rzgGLIPwksuXsFgRdBh_pDaeEMF3jUEBmilUsnr7IY1ueWS6FglkvdjODS2R1_0mYN4xH5aAuCJyb2ZjyyXTZObY4SFyvff3tdredsgpLjrXAvo9QN2ft0nf9fvxmqHFSnTRPIsPln35GRAxTRgTcwejEnskUhvO0DWid4zWz8-TMFj9ci8_M4rsVrSJDs7g0Nm-jfCAkMw-LqHIlP_H_2DWpULGYAKKjD45ur7OsFglzKpfVWPEpYzpT9LpJvAmg4C5WAFfA7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhc-2nUObFah4qg8Cx-O5ufdDoPWby1OKdZXtBuyuTq5oYzbLjPli_AP4k71_5q47OQYhz6R6GEZlopViSxDiO1T2rjfcDrUUYpkpwLQWLhqTDAPW_e_qLee2BursRRrkw3FGNvwXU8CPftHUhZRIVJ8lEN7VxOuHksHxDynYf4tCPBPT0Lr_K8emkoGjyWGD7d0872XaaCBYbZrIAW2ZrlQcfvVYeaDy2wH_TO1reozQEP5AJOAlphkongBYY1KEgTwMlEqahmVWJOI17ZYx5aDLb4ro62wNMUz9f8EJr6Ovkt0eGht8lhUoYNdN9Usk2W3gSNnT27Iynzju_4btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0kf-0HDe5EhSc5JHWnVIOG0YBa-xrIwJse4zIB9M1IS7cqv_Hz-5Cwm5GzdzPqyEgA2pGuoMPRCAjYnqbbzI4HIbHfQkcvnOueaOY3eWHdlXtIZhS1xhZu_ljQWcH-zW4D-Q-0TJO0cRpnDqJJiQI6oYYqKm0toyrM31vZigWoxoL1USSpCPT8I6SRb2CHJgtASxzQ8bhB9zAn2WL7xMBu9l0RTnly53ySvEg9jDKmsvh3S2fh7ekOXcKF4RqR6S5i-bXP3Pu9hzj7oW2kEs8HgR9nPKIyjB5m5HuIwKX66lIc5beCaNbfNXHv7T7va4K4TqExbEZftdmBHBWtCEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuuRMA3yaYjHAalDRCR2GYI2auDPnEo0oBBZrXRKmNwnD2xnjDswkFM3RHLbu4S70r4wvZIN4jaKUILMbmAwPHr3xWHWQAqzubQ-X_klI0ZEn5MTgNiDT_kev_VPFwkjHkO6rdFMFYIdFMFrFooDTKy7IHhLq6ho3xJ3Y5WsE_ck8aOKqSagAUOTYmwPSN8aSW6ymI1taS-Y7vIpt9X1VdYslpWrIKEXEKPpXkbMjcOZqMuG-jJgn9ljYMdGXC7vft9RMNt5I6Tg9UscgqElbhJBYVESY8KBEgaD7iOVWzFx7-Xy1K52vItjOvlkzKhV9dvgKRWl99cGfqN9RL8_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLLxjvGyMkRdnivswxyzAnqg1uyWlrZfGsYgF77ryU9voIt_GRund1VVdmXju5NNxYwHeTRZq_T5QaH9Z2-9QdsSlkFn2xtQMB7kPOsfMe351chvT3WzGBYf3-AHXXmPrAWXd1c3A44i9mixsGj26Vp1RutTzMauemj2SfEvKWKNtgeDtBie4RcfA05KC1EkxHycZmZ80d9zMvGOHH3pE_3MjbJYwq2MNNOoFynDJm2Ep7ZbiPUo_xqKRrZpobbcft1O_pUw8RXPGYqpVEvtOuxCn8DhwYZkxjMj7QrxlIVkLbT1J40Nt3ZHKo9dDZ28FTIeo4YYWbWdUaI3A9mBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq-nnpX2DK73LF7ma43g1jcYmem_MUf_VV0rlyJ-z1PEtitxCUk9ls4PJheYUi-6PCnKp3UtP7svbSobbop8OXW29rBUeAF3Jn6IpPGrbxH4dBHdrnaaEm8OgYk9mPiOTzvrlTt_55de0wDDfK29K6e7yT7xcAeQmU3Mcl8IzgS-iflOjVzd8A3o5lL-fcFFc2JT2ZfBxt0Z3udB_OHjBF57CuyabnKYgLI0jVMVpvip-gjM38CmQ7PWZ8PmfNR7hKTtzGzV05324sII1L54kfCQygKnS0RWoQtaf4Rlvdyh3XGifpsFGnVOKx52_11glF28Y7io4YaTw1AkhvahMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Jc5h-gSojuzb9ivJPzvhaDXEs2tCuJWiI4Ifv5vLzxk2YJq0kOKWtWyKeTFYQpX5aCpsCU2pLls9QMCl1FFOpm3bfUk_czLi_o7plukLbwI12Ptxs2rCkP5nwGRGBHy7Um_aOGxlfMmR6SQ-f8T0v4xeOG15uq1eRRqidQflJIyAAu9LS6VEeB-EI8zKrTGFcYjTms8JxOanubn5MedZWvKSyXwBvu_nUQssVp2FBue7iEHpMvGaZOkXLIIZ0c1uEQIezXWwXXYlainoZHERPjYpUajoA3ckNbFBiWOt0GuAlTp9dSEcWHJfLGDZZBoosO-KqunVv8mctANPznEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qle8s4IUz0YV0m010xeigYoRFoL6FSnVKJ7ArEdvcDWMByI6etvhOx0qKihIv6LlvsXB4TlL3Jh9oc4TWPP0XtMTezBHRQZH5HvX6wAKquO4z-rW2Qm-aFD_jEWlpjqVpUFWrDLGgsVjJgKHIqWMt0bWsG311eVcqP3kyx3OI6LlLNEAd70dCPbjpYn0MtfUdD7WqEMOVvAaR3hTwaxnKC5c4wPQz8N6VNZ3Od26JOSHYEkVTAc_lrtgU-sfUvIz6cDnLVy6o9DPS9OoPznOWqxP9MWAjQoEeihIXHFhHBwJhZxMAv7kausqWGfxB-7ffUNwhVeL-k-ivvQnuTVIVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qle8s4IUz0YV0m010xeigYoRFoL6FSnVKJ7ArEdvcDWMByI6etvhOx0qKihIv6LlvsXB4TlL3Jh9oc4TWPP0XtMTezBHRQZH5HvX6wAKquO4z-rW2Qm-aFD_jEWlpjqVpUFWrDLGgsVjJgKHIqWMt0bWsG311eVcqP3kyx3OI6LlLNEAd70dCPbjpYn0MtfUdD7WqEMOVvAaR3hTwaxnKC5c4wPQz8N6VNZ3Od26JOSHYEkVTAc_lrtgU-sfUvIz6cDnLVy6o9DPS9OoPznOWqxP9MWAjQoEeihIXHFhHBwJhZxMAv7kausqWGfxB-7ffUNwhVeL-k-ivvQnuTVIVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjvHc9XjCJ3Z86ikbbGYcnQkeiF0kobQ8zsuk7_tNR2QXy3aI4bDfqGfsKX7xsudD2NuqZDrhAcFeJM2bWIJriHwcsefR3bKiwxWNgQ5aODCvtNBp0-3O6S_ub27rtFyDEMNPH4d0KnPfmwetYMvPqzU55dU1V8pi28d8P-zDjc7PwCLOvUIF0NUzYnY4tXkmHBjEtCz8_KOrsYvpLlHwS92GoIMqUma5MTulG_3ruTq4hPuOZV7GUZFqQkyIV7l-6FE0ijPkTZd85Wl2smWaDxTm5BDJ6EbfrENqGai-lQpJkd9JW3flmNDwX1xzot1tg8wIvkU6ls6FPJnc3hGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=idW8rejfOV-O0xOY5DtLWQJsHsgcrCXKeAu5sTIVvNb2yp1Wvd21kv39GPSghEgLRY8OUZMkdrthkGkfkQFRLCG02JNz_bFAfsmBeTx85569uZZCMv31qYeActNVqVYWpblpZA0NaS2nOtNNmiLJ1WbXACrJ2PDAL6ayPQZTXezBNjnxucc8XiqQxaKlPaasi0E68bMXju74S-NviYv22r5CAZcvkcVtJMTXuiv7r6ZFCi8kUaKnwg8CSKz-2WfYtceZHrYLiE56UiYuJKdJX6GBH4uoqiktCILKuusetIyIdunndXDR_F3UwEAsI7dfwxhR20QPW3-b855BR64t3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=idW8rejfOV-O0xOY5DtLWQJsHsgcrCXKeAu5sTIVvNb2yp1Wvd21kv39GPSghEgLRY8OUZMkdrthkGkfkQFRLCG02JNz_bFAfsmBeTx85569uZZCMv31qYeActNVqVYWpblpZA0NaS2nOtNNmiLJ1WbXACrJ2PDAL6ayPQZTXezBNjnxucc8XiqQxaKlPaasi0E68bMXju74S-NviYv22r5CAZcvkcVtJMTXuiv7r6ZFCi8kUaKnwg8CSKz-2WfYtceZHrYLiE56UiYuJKdJX6GBH4uoqiktCILKuusetIyIdunndXDR_F3UwEAsI7dfwxhR20QPW3-b855BR64t3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=oBNmELigDh2gurrC0hnt4URDK9gfomUCXz9sBUUNC24UuToxA1Sy5167zj0ex6I_RFaCfL66Z9ID-Wt2KOJYj-ZUPyYX7AdvRybxIcU_izFs8jYYkoK0H6IOMdx-3c5o1r34X05xLXyo0VkyxvOMC3-fDFAi7ixwUplF2MDJjECC7lg6oqInprsJFih0X5LhluuguGnK2D1sKR3jG44R8rypFFKGRvFDXqk_j7pQE1hfSp_kYoD9qBA0T9_X9yvIUxxVpslNc2u4JKNySkLQZduFAF31NksYcxOBq1CreD6s9hkh36E-DSqRVm-pZs2m9rZow3ZdOr04og5lLrWCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=oBNmELigDh2gurrC0hnt4URDK9gfomUCXz9sBUUNC24UuToxA1Sy5167zj0ex6I_RFaCfL66Z9ID-Wt2KOJYj-ZUPyYX7AdvRybxIcU_izFs8jYYkoK0H6IOMdx-3c5o1r34X05xLXyo0VkyxvOMC3-fDFAi7ixwUplF2MDJjECC7lg6oqInprsJFih0X5LhluuguGnK2D1sKR3jG44R8rypFFKGRvFDXqk_j7pQE1hfSp_kYoD9qBA0T9_X9yvIUxxVpslNc2u4JKNySkLQZduFAF31NksYcxOBq1CreD6s9hkh36E-DSqRVm-pZs2m9rZow3ZdOr04og5lLrWCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=ZDkREQzfOodkyZuuwa1n4Oag4KhDNxH1wq-uN_QIaHxYLegtxiG989EtHqWs0mimbhzVZ_gyg2zbgkPiTTMU3bekF0wn0v4nZmSFtpeBvEUUaYZFoKCgQMe9mvEyoGkCPELhxHwwkkNnD1CJeHZFYZtkdTrsMHucq-pGXlYN6MFBj4kaloIGqyCOhd7cPuvvwTrnIKNoO1wjJpNaj0rpVk4kPY6b6m2JWFPL3E3wE_97tv7LEam1y9zuJPYm8yA0L7KlMrwrOSPBrqSuC0IOMLVVChf1bbpkrHH3CedMJYjGKAVsr9MlUFeX5rbTeX8Gj0TvLBh05gckTYYuy2psnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=ZDkREQzfOodkyZuuwa1n4Oag4KhDNxH1wq-uN_QIaHxYLegtxiG989EtHqWs0mimbhzVZ_gyg2zbgkPiTTMU3bekF0wn0v4nZmSFtpeBvEUUaYZFoKCgQMe9mvEyoGkCPELhxHwwkkNnD1CJeHZFYZtkdTrsMHucq-pGXlYN6MFBj4kaloIGqyCOhd7cPuvvwTrnIKNoO1wjJpNaj0rpVk4kPY6b6m2JWFPL3E3wE_97tv7LEam1y9zuJPYm8yA0L7KlMrwrOSPBrqSuC0IOMLVVChf1bbpkrHH3CedMJYjGKAVsr9MlUFeX5rbTeX8Gj0TvLBh05gckTYYuy2psnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4kM7u7gwLzmwt5Feekunbw3ug4zfpR8ZawJT1-JSgmbLRgZT8yp-wf-bonE22S45iX9Joi_lcy3A79I3Rj7ciJFj1hCg7OagLiER0fxetJyWXwm1gilGoLcRHhKeGBecmfcJl6BEYl9zDB-8xk_rM1XxdkSsLoQRQVZ6g8INkYGnpeOdtiKqhRddJjJIWKj2zSgfytj57nTy5hSPQKwUVbst8SJVZ1XL9d114wBs23a72zPLJzIe2aaUMtk0aBM-9FRwFnogxGl3QzHzt4JUTpMTwhJRGn-rgJndfFB8kcZ-m76Uz6tKJgnSpEN8TbKNF0rr3H1tF8Mm5Ves81vLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZWBOovLgs8m5HR9PZDle0QeG2Akn8fe4VVj5kBDPPJDuE-fgzlzjgXMApkF3fTMN7jzmZ-BmOUdc8L2OZzhQT5nmkQBv6N9vF8ZeyDDLdWgSrnJhZmF0lLrtAYg8q1r9sl5SC_rTcBOwJKiFkhc_GU8Kk0fGITBxS-Nre6BldZBsPdlWoUL22rnsGFmAPE3pXQnN27XOS56NQVj9R4xy3aDK53SBTnR13sUzTWNEKIjT7A94A1Vu7_yL7IQlXUWM2l_vY5QGq8LomfWCiGot41mU_J2UukyO00zykd3GuOJqOW_iPfRCy0iAO8enYO5xk_vF0Jv7a_I5tGu3pFH8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=hL3Ji6dT28oqdD-vmseX0lrgxzqDgxaD7RK6-pNGkPpocNcESEFvbqghBy_0GuGM27WEFc3FfIjHpNrSe0aaGOOeEsJZIzMMsRfANs_dlSZ8FViMaYmn205kQsWYIIhyuCDibJSKKwQRH3ouVm1O4FjsS4q8EbpESv7lTIM0rFW32saagHlJa8UoIx-P4BrUcMgmKcz4Y5nSrgob0uL3a4hVlBQ1yAERel5VS5bzMhOET45X-UEl1KRFUSic4lylh7xGykeBwZyJ_OPp9D8fsM76yWAb62bb9KlttlKlgUNTIW1pvoA439Czn1ZtdKbYbvyHBLSdUaL8CYqm79kaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=hL3Ji6dT28oqdD-vmseX0lrgxzqDgxaD7RK6-pNGkPpocNcESEFvbqghBy_0GuGM27WEFc3FfIjHpNrSe0aaGOOeEsJZIzMMsRfANs_dlSZ8FViMaYmn205kQsWYIIhyuCDibJSKKwQRH3ouVm1O4FjsS4q8EbpESv7lTIM0rFW32saagHlJa8UoIx-P4BrUcMgmKcz4Y5nSrgob0uL3a4hVlBQ1yAERel5VS5bzMhOET45X-UEl1KRFUSic4lylh7xGykeBwZyJ_OPp9D8fsM76yWAb62bb9KlttlKlgUNTIW1pvoA439Czn1ZtdKbYbvyHBLSdUaL8CYqm79kaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=rnQqXwLIWhyVIX7VCFSuw9Dckjw01fHoEfJo1nEASSKhkSizY6P2B1hnnea8Nf9d9xjdRNnwMLPUvS86Zg2KbVotHsz00dyfTG8tN_CvrT17oVranJZ6wxJ8P6s3gQeynvs1DMwFfwx5hx-R9eb41tkijd6OtkSxLarnqKNZSTdLCDrUIBNCPHXGeo8zBaG8OPw8zYIIv2WqvKQFwqA5Slamyr6Y86XoW4sv7t0x52OW8Bk10Di_yjtCntx3nnWOMyO0dbwj9yfk8UfO40bNNYBA0xTwRB6Xopkwk7xlZyDeu1QcQav7YPBRBTxs0h-WReMcktHvzt63e8cHJvKS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=rnQqXwLIWhyVIX7VCFSuw9Dckjw01fHoEfJo1nEASSKhkSizY6P2B1hnnea8Nf9d9xjdRNnwMLPUvS86Zg2KbVotHsz00dyfTG8tN_CvrT17oVranJZ6wxJ8P6s3gQeynvs1DMwFfwx5hx-R9eb41tkijd6OtkSxLarnqKNZSTdLCDrUIBNCPHXGeo8zBaG8OPw8zYIIv2WqvKQFwqA5Slamyr6Y86XoW4sv7t0x52OW8Bk10Di_yjtCntx3nnWOMyO0dbwj9yfk8UfO40bNNYBA0xTwRB6Xopkwk7xlZyDeu1QcQav7YPBRBTxs0h-WReMcktHvzt63e8cHJvKS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=dCCJ6B0IGSEw35lHBaRfSQsWwKvQbt89cxY9jTnzhfzvneXMdBWFFrNfe4CZdu6IR30ky7H1A-Eg7ccAlVVNbGM73_Qmf7QOHWPT1jMsbjHtJSf8dhEd3GNyvCXyZjMr7-JZLlXDjSWUaH1mbtFNphdDAl8c2QTyc4FPba4TpXTSLfkt8YHHBCF1h3l27Z2hGHIG2wzrRlqL2WOtc4gVfZOpqP-dO6nTNnKw194rTWtXz8ScLPfCGZgGATjoi5jIsfo-6ogeN27zF-k7SgXtEoU4eEqCMJ3rz1Qh2ueyWoXoLFKYMnnRgexPSmxHun3ekrdz56AgltFF8BduidgHGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=dCCJ6B0IGSEw35lHBaRfSQsWwKvQbt89cxY9jTnzhfzvneXMdBWFFrNfe4CZdu6IR30ky7H1A-Eg7ccAlVVNbGM73_Qmf7QOHWPT1jMsbjHtJSf8dhEd3GNyvCXyZjMr7-JZLlXDjSWUaH1mbtFNphdDAl8c2QTyc4FPba4TpXTSLfkt8YHHBCF1h3l27Z2hGHIG2wzrRlqL2WOtc4gVfZOpqP-dO6nTNnKw194rTWtXz8ScLPfCGZgGATjoi5jIsfo-6ogeN27zF-k7SgXtEoU4eEqCMJ3rz1Qh2ueyWoXoLFKYMnnRgexPSmxHun3ekrdz56AgltFF8BduidgHGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=af4mGyZqREgB48MTDhaPwy95XAh8lhfvdCddPxXibkNpnIOV7FuL1XppbeI7RMPaRUy84BfCJvdQrI1uJW-IcIeMBk6j7L_WZe-SU8xkYbkd0RaZGrjX4dTITsUmd8sqdRWcrxBU6XXgcVnJhI9FGUf2xsrIdiMu0BjqyKKVgFpdpfHRBBM3cvnUMDDn7Z6bOE6_BLFB5aZoq0QZunK8rEB2uhu42DEnMe7QavsxR_JyY0ghyIcLL2-LvNDQkGz_AdcxL1c_W-VNahaMmUiOtRBA1E7HSpRT6k3kBiq_yOMKPz-930YPtltZxCS1b3dTueOHeZGFexY8Vjk4oC4T5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=af4mGyZqREgB48MTDhaPwy95XAh8lhfvdCddPxXibkNpnIOV7FuL1XppbeI7RMPaRUy84BfCJvdQrI1uJW-IcIeMBk6j7L_WZe-SU8xkYbkd0RaZGrjX4dTITsUmd8sqdRWcrxBU6XXgcVnJhI9FGUf2xsrIdiMu0BjqyKKVgFpdpfHRBBM3cvnUMDDn7Z6bOE6_BLFB5aZoq0QZunK8rEB2uhu42DEnMe7QavsxR_JyY0ghyIcLL2-LvNDQkGz_AdcxL1c_W-VNahaMmUiOtRBA1E7HSpRT6k3kBiq_yOMKPz-930YPtltZxCS1b3dTueOHeZGFexY8Vjk4oC4T5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=Uoa8dPLDygypL5FH9sjGKMUHmhLIHY-YKVPRJqHJINFcwdgefaElEFSqyyAG7ciYa8nZQoAmilix07Nb_GS9T9QIhVJc3wJSvZWkuN10YxPaolGuEK4rSzqCRDt2Fn16Y5hL0U6azs80ik-Vc32UdhkXDZ0Yo94pgia3aycIWFUujNw67OEgcNfFl_xtid6CL2Cobv5E7lMrXdrG7sfRMe_pxlGsGDRjlXkRcvdcVhQ8gkxAyexlHMJDf7wsal0KMoa59EV7nUCNcT8a0ain7NtYbF8DPITv6UJhO_rXkDhB1lr2-iwpQ7sSEsQybKVyeBFmSSDMDE9332C-XonLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=Uoa8dPLDygypL5FH9sjGKMUHmhLIHY-YKVPRJqHJINFcwdgefaElEFSqyyAG7ciYa8nZQoAmilix07Nb_GS9T9QIhVJc3wJSvZWkuN10YxPaolGuEK4rSzqCRDt2Fn16Y5hL0U6azs80ik-Vc32UdhkXDZ0Yo94pgia3aycIWFUujNw67OEgcNfFl_xtid6CL2Cobv5E7lMrXdrG7sfRMe_pxlGsGDRjlXkRcvdcVhQ8gkxAyexlHMJDf7wsal0KMoa59EV7nUCNcT8a0ain7NtYbF8DPITv6UJhO_rXkDhB1lr2-iwpQ7sSEsQybKVyeBFmSSDMDE9332C-XonLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=H79k30RjMov98zg4p6JJliLDLeq_lQFs19IcTfjo12CTPZHnLJiD4W6l_7niX04JogIH1-lBRa23RLHsT8VjaBc5WnTQO0JcOSnJCihIBkaOi3U9FbgN9tnRRgk5pTn7yZgW2wHJJhkUAVjZOZeog-bFse2SSf1jDdLI052vQ1Os_7fC35xN8xLnvwKgHc2sHgDAcs3bzPBvtCb-lnwD5XPQH7UeherK62ZDPO05gr2lqfeEiT44merNyT5rZl8_LQRMJYjRildVBtGCBkOWk52TZuL3vS32fJNX-kjC7a65xf5RHagIWiTXflEArVdd2Q4NF94omHQKRfTEJChQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=H79k30RjMov98zg4p6JJliLDLeq_lQFs19IcTfjo12CTPZHnLJiD4W6l_7niX04JogIH1-lBRa23RLHsT8VjaBc5WnTQO0JcOSnJCihIBkaOi3U9FbgN9tnRRgk5pTn7yZgW2wHJJhkUAVjZOZeog-bFse2SSf1jDdLI052vQ1Os_7fC35xN8xLnvwKgHc2sHgDAcs3bzPBvtCb-lnwD5XPQH7UeherK62ZDPO05gr2lqfeEiT44merNyT5rZl8_LQRMJYjRildVBtGCBkOWk52TZuL3vS32fJNX-kjC7a65xf5RHagIWiTXflEArVdd2Q4NF94omHQKRfTEJChQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X67seC1KEeZJeExtu8jXeP1Ll5G3U_4CuVdsWn5f4Mzv0wKATvLJN4Rq4QnAvXqm8CfWQOCrlYPhTkkTFU9Li4mF4xGkj-2Evk6yin3oOnDIJen85uz31114Y7fiEn-kVuMuXWpdxI0Fmo5jVQ73UUNhdAxaQzm0hqsSx7SFDldhvvDP6CNOOQDOb06kpe8VN73FMI9h_Xx7g-7oTRTR2OFbPsEXO7dPyiqPY1BrksIGsWIyuPUxrPMYOn38DWEwrgD1OIVTQQ8IT61NKE2nVaIYRf4PuJZicEkFJ3EnFK84i3YY7-6aYpATi_N9SCa0lL_iL21qkxa6o4JRnevkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3h92eUZnrZjorGox_4bKVoi67Cxa7YfEg1DTMdD2NofeuBBYoEYcs5Tw7hB2qa9CJ_JIjfI9pF2qMsFu0TSbW56yyGReaT2xEIBduo2RoCxaN6nR-_jALDSgP6PZ7wWUiCWWd_L3p-n9LxwzzPqPqyctUj3vYEs3fx8Bs4f2b49_nR2aH0KLlXGpndWxMwUNTDJJhO_5_5StJ1pehef8d0mHWfkTtrE551z590vxp2YkdgIJSvTyEfpvyrI40oeVxEJh7aFB-lIy1QZ5XSinZ70sTxy8krLTpm3hlK5EDXM9E3HC9edc4rW_LLBNwlxPRYyQ84-LK1Z8PZkElcwdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtCYVNpjcGx9t_Q803kPxLvr471EhBQ429O9jO7wa6wPiaAtNeo67vKFojwlejKHt7-4saeksQ1lk_5RCcMAlo4QLIwPw19co1e4J9CrMmYREMb1AyGWH-aRatBuNTK-XDUhOArD7gYSBHhQyqXHq5dPsdT6lRbsFX3L5i0juGkutFinNgfXB49zdFFvT1r77tOlHOh4Yq4Yr7Dhj1mi-bLWtOmWcQHf3YoCZglFBsJdPAiqn3hse91pgFFB2p1dh0eOZPMWld4UVT8cVpi6K0KYnlA2Pz7jbjPCUtG6E82ixX3WYyUpjRaaZgRFdq_gydw8mfZyF24TBniWbq2brw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLYAKfEiKKjqmIyaPObehjglHFciIkaRmPoCpr1cNGVT1B7Z61f05trMK1B9njai2oRZmHcdBHR64SIV2Q5tk6NdRekHW94ASC_4MeXrYulE4rtB-Pf6yu2nEsQZAe0wRhQsqayJAoQWmrFPzhItGNFTeqHSFlj2rQw6KE4TZinw8AdDtNd9uFweQv18pAdYF_TRd3-P6Xsc3j7ZwAnHqjfBSd8soyCw-BLhGSlTh3tL-Lk-6PMT6vKqLLXJNxC9y_08s1TAG_2QLZ_0SAviCkcLwmAexGgb7jf-2uCG8xAZIWMNcVYPk8b9owNFklpdtwxmaGbXRThhO4BJ10zdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpqCpKZmw0sEKm_l4iFyoawsbZbXYMWkL4voRWaw1S2YmSRxTMUuHRCWyqCf5y7k8emBUoWy5TqV7bjfniHPTb8DZhPHOoej4A-MV32X592LOREPTmI9wYcgQUPBKQ8kp05VE0WXdV_biTxwuh-L1AMUX5llzex9IZenICu6dTfETj-KJMB45yqkgGSInLpTLWImcMxhS8Z2DJ_QY72OkHVWjw8ISsYIbeEGtNhnKXdqdfZGmXkbsbxoboX0-UpuhcgJnLu4oFZv9C5SXWfilDcuE7ixPZDm8HC9tkv5wpguddNcCs5fzRCF5NE7oV6nrTinnY9skFeAENNGgwitKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG5Khyk6nRlJKSwD5_GmJRP2eq3gfYngg0Ns6Es2THnsw36qPBDH2CKRlTaudxor2ZUTfJApM-aqaXXP4aIjxUQndTmB6kJR5shsyD8b2U_5vQhIlTd7LQYxDVWobmMaEXnHKnYfl2pR8D81Mkfa0nvJ71dA7Bk4mFIK-Y1qaODOPY2hlVV7Ii1gAd9T2oRX9kYRdxyesn8UMtAp5OsR7YtlDq6TU1nwLEXdc82o2kojQCBaD3z0kButRWQX-9so6PK05e4u5LEq3yrV3Vjaw9Zmie6ADWLUg5Q2IGUnTSDOMFXrrLuNpPVWzaEInbIv9xjqq5MqEdFnHmds1TwL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOqdedbe_X2xGRcAD6iNNZDQw907S8mdV3p9WJAeFf857_UDOayZutG-mmJ_jL5eL6KTgFI8nux0ITkoimyr5Qa-zI0J7c3cSWqb11BnHSoRpgpekcbXlTTpui8IB6w3wGSc2iSJxeT2a_hS-NCItk0jIjdfzbiFtOl8Z4mjC0IhSsUmOJS4C070AF6aQ-X6u7_jpahMMG_DLEPBDO9KOSKoATUCtm6CHx-LsOUJ3Rgtuh5hpbvJlBeV2PEECRTM_L6aTKhlgq7gb-APdt2MM85gthM-T3fYCMbnYc5LkBq_PkJMNstnloR1LN-UkQf_finLhlnrYok9mLHBpsvz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZqt5DvGtgFXH8TvFD8-ZqGRUmQqpN7G721iyMWzpewzcotUPyaYRZM54sOdWqGjR2DKqma0sWVj4x0hUCPF0rKeMOsaL-xbXXbXRiZecfQIDXnikXPWnyGSvECkSEBgYHLJAQhfAuzd_cvFY2sUQEeR89bfXWjoj70htPbYXiWnjvIiQfmPNPiYGSWS6pVcSL1CuZIJXN6TN9nQ85CdtPtZVnY4ov9ZbklLklVW8uGfmvvG2ABM-RrV_uxTSWc9JdjBF6ZgVrZlH3KLEy52gdQT873eXKIXZ2nRJW14JwyXXxFSTbwKifFR_otu37D8jq_bxNN96j0-hWS3-5DWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvAy7LBcr09-XNCIS1hx7UJF91n4W4pIRRI5u6qUsxSVBEl9PLyH7WJFDkxjcZJ6aOdNGveyzJK2nWoFwH111oUycU1AcYFLn9VtfW0CiB6TSJn_sf_gIh5FDgEkbb_l2K-nPbHXx61zzT739znbzr-RLHSD8pPRaWRsCkpVt6gFKYroOEAG_uw4MiacF7fXZUGCHQh3JYdMVNVd6YhIiwWmvL_mdW7k8qNacQEkPIKUAQeZ5rcqz4_DozZCDC7R3kZ6ujbnxGx83QocCfHssNnfTAlzWLaRDEhdF-BZqwk0cY46gm4bR_K2aGF9TnWIWfBWf62Zbz12y1yk8CL1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0RAcDo4stT35ZghP7Cfih3TVXcHdcVOBhfbH79kWzSrJJHWqcOhhLNmuVTn17xSQEoFZ3e-CySvAePAUG0JiIVNSXVwKsEVUwi-ZEv8NpiRZHVEtc36P_hGcEPygMYEIHgnapbi7W0h4Cs06QuP-562aSH7n2f_QeOWEokoPHdQvJrkl3fK5_TVpunfwjo_mrC-5EaZ9OkOKwGw3uE1nZ_vSQDaZ1fZIFM5Bow2qFcZcz69e3O_EZNKsDu4ELzspv_vbk76CjYhZzZw6f7OU-XKkwVGnlhw9qw7RtC9rAN5_yk7wtV926tM95kc7FfomRuZbjambI2wkt6rlQKHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=eYmy-f2_7UjQmPj0S8hSRYlqaIOd8eU8SFteH1mEEO1hVND7PupweLKtkAQQ-dbrdRTYKOL0KpTTAEaYB7PsqYBVxNtl6loFxqJepralvQMb2QkSc1ZDQBcIoje7FV3VxXbzdI-KsZl4GImCBbQ8LOWTVGbfvDavCT_O4VxITLTVPbPRNLmg9STCu8giLRSMsUziQMgRe4Sv1FnUhHDMT31n9-qtKay8HhFMFgldkcfUlYH2VG83rYyGV_TfKDeSweKvhWp1rna1QYeyL7cVjTw4wRs5aHlRnUMtEN04U19i59NeBX7xX_5BIpsUo5VxkvdtOxzfhpG4gs1Hndm_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=eYmy-f2_7UjQmPj0S8hSRYlqaIOd8eU8SFteH1mEEO1hVND7PupweLKtkAQQ-dbrdRTYKOL0KpTTAEaYB7PsqYBVxNtl6loFxqJepralvQMb2QkSc1ZDQBcIoje7FV3VxXbzdI-KsZl4GImCBbQ8LOWTVGbfvDavCT_O4VxITLTVPbPRNLmg9STCu8giLRSMsUziQMgRe4Sv1FnUhHDMT31n9-qtKay8HhFMFgldkcfUlYH2VG83rYyGV_TfKDeSweKvhWp1rna1QYeyL7cVjTw4wRs5aHlRnUMtEN04U19i59NeBX7xX_5BIpsUo5VxkvdtOxzfhpG4gs1Hndm_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqg5YbhCjUkjv30spxstqUC2cRPrhu57WIhA_2H8ctdRHsWQndC_Z1NTd4H5gix6DMMRR4r_b3D-JogkTaobQn2L_QAhh9B7Zw_f9i82_v14ElSZ-OGAqM4yVB0VzlttuMYblfyi_OGSNp-ypRLNOagXkB9I2EkiaecRPxD5WBmrdbejGpeOz9ngsFCpIlw7VyT0AstXAknbxAXPryjE3oq-Ow6SdjSd7q5-hIl9OP4NjIA81LuJxNh4MuXcUKPf7A6QPBkAtdqZiHgrcLZN2EniGjxa6EYsszH0fKhsLdlonz9zdhpM2zpVwIP3V2J6ysjrChBcWQtWUqg5fUUZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdBYEgu2wqjXVCS2RxRJXFbUsK0U_SFeI-bJB8WTbYmlgj8FZ-N8RHkyYgHO5brlTZfiITc9PFzHXVXexBgbXq4Uqs0_VWpE5w8I7n65RDGVxLzfLPtrhEnZBVZcaPqN3hCe5Yolr2-ukzubVicuG3DY9Bm8bvcQ2t8lHRnGg7EIGRbLSJX98agrsXq8pWIvDrQf0WJpLJm2OtFPyRHAHOo3gyKhbNbuR_GXsNbTo9XVSvvpiLIjxftJpWxGPxVUPfaq9gtAgjcfyWcR3YGCtdzvufT7LB-M_8Ulsg7WLX9F1uwPJRWkgG-w8CsL7y_pBSVq3jN1cdGjMYs9hw8pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gc1VJ_9Yd8nPioPEJonN6F696s5XOKYCdGjvT7e-aJ5svAh18cgaYWbWPoYsZvKL0QJC2pSE2fqAmCdb-ABmP8H-Foat_zpcAUSN66EvOFmgNCyD_dx5ohcP2TGX82_xCVOg1Gm2sQr3CXT-MOOFh4dyRMEFsWV9p8T6b9ITU1EybwyhzHU23oXwzi4N2BTcx-8Knuj-wYK452BpF0NgCcgyZ3Oa87snn4XwHWOEn5nV5uJ9xOdF5FBJiAprcw2VLRq-7SIiBmls078eUSrY0_dA-V2zzinKAcXXg-KNZOu3IYXdBzEvbM1FngdEqKFFlWW1On-T37EzfyzaBHnbOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLfgkWlZL_SI6f0VCOWkmO0HwyWcRTqK-TEqJD3FCoo-adccifMWUfORETGb3wnm9ENpIllmLkhOgb6kQVg8oH9kx2N03om4iBB8EL4cmXpajr7i8kngOdss7lkAuEeLR4BnqTZlosvakkBrnCDvMYWiafD-ZCRtYgJvgSPf08WAi_sySghw1R94XgE3GUgLMADlecNJlLmfA8guVvOXRaAmz8edDEgQlnPWHEJAZCPFdw063h8KrXF9-itDOz_TxnSCI1jfOsUsd2qXndiiEBVF4mWmWo7z3ymJcx4bXtOQemqF3HJiuskfy4Cvp4Qz75uj3Vko4t-Lw1NnZS8cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABD4199XwYMCgO0JR1kKb7sYhlLBDcTGF_Xb9qTeeOCUr7NRrBCgYo7F62_hSNAAA5tMIojrKuOsMj0Mtx8dzmpj7oHXJedDZXrRSepty0BJewA53NsrkRu4odSQO4xgnICdj-moZlr6p9J2ci8z5KVZljB2dnwdRwscdT6BQq_8ZiOvJ5Lyf4yi7JvwHq7aM1cnWYjs8ky5Wy8irni5W5Xcn4Ju_NdnjA_59EC4_kkCj1ouEYE-hq95_BKK7x8bTtZmNioFPFm7yMiKasR-MnYYR-yxV7gXyBZyRg9V73c1UdHcdxnQdbh7zXDcTmSnrNDMvJLvSoqxMXGzCm2yIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeIZ1GzTAcBHfH8mwrQx1-Euwgc_iSz6nIJSfElzsnEcgFfZIREeqkCVFnpf34pTKykSZca4qEi2defLaKF4XjdJO8gSO0lc91tXf0kPT-oDsfHhnI5EAzpAWapQMLdmDsh1p95fcgb_KN9mCdbg9_McqKlssG7aTFaflHtTJ-tMp1iExL0Yw4aq2nmUyeV3X-V0ArorsaBfQvIBGP-RRJJA26qNYkDg7ExvJaffW-POmbKakiNeKeeb-dRoY_TSAgMpxxy5E8JzQsqMY9S6AvFWu8ihWQsa5D_wpeygvTL9jFy2zJnPyGFWsGt5V-2J81KDw3ZC9jJGJt7DxiHLJWWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeIZ1GzTAcBHfH8mwrQx1-Euwgc_iSz6nIJSfElzsnEcgFfZIREeqkCVFnpf34pTKykSZca4qEi2defLaKF4XjdJO8gSO0lc91tXf0kPT-oDsfHhnI5EAzpAWapQMLdmDsh1p95fcgb_KN9mCdbg9_McqKlssG7aTFaflHtTJ-tMp1iExL0Yw4aq2nmUyeV3X-V0ArorsaBfQvIBGP-RRJJA26qNYkDg7ExvJaffW-POmbKakiNeKeeb-dRoY_TSAgMpxxy5E8JzQsqMY9S6AvFWu8ihWQsa5D_wpeygvTL9jFy2zJnPyGFWsGt5V-2J81KDw3ZC9jJGJt7DxiHLJWWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=BXHv3v7zwv_HIjmvXsNwCVRsjlhdWy-3arsKnri6aO--MNhh5I2iJ-5731uVWLmJdhzo2Al_jARy80E3l-aExlyv9tE3Jr3ZF4RIDk7bg4GOXuSo_vzRrGQv3-qRvTIRlHA5KiU4G8rxR1RSJOGmfPlEExLR6zHefPg5IBiTuLovryaEIZMMf_XeBmkvCdQpipuFgTYZMR0Izm0X1zftXQQ5PROsY9bBmMgi5j4zhyaXjRR5IFGo39YDueft-C_cm5peL_Y2yHa1rzH1zWcqHW7MhNnO4EI2-wAZf2oB4CBqwKRLRHDfVONfnwIxu-8ArYrtz8qA-rUqoCMD0ijDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=BXHv3v7zwv_HIjmvXsNwCVRsjlhdWy-3arsKnri6aO--MNhh5I2iJ-5731uVWLmJdhzo2Al_jARy80E3l-aExlyv9tE3Jr3ZF4RIDk7bg4GOXuSo_vzRrGQv3-qRvTIRlHA5KiU4G8rxR1RSJOGmfPlEExLR6zHefPg5IBiTuLovryaEIZMMf_XeBmkvCdQpipuFgTYZMR0Izm0X1zftXQQ5PROsY9bBmMgi5j4zhyaXjRR5IFGo39YDueft-C_cm5peL_Y2yHa1rzH1zWcqHW7MhNnO4EI2-wAZf2oB4CBqwKRLRHDfVONfnwIxu-8ArYrtz8qA-rUqoCMD0ijDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUOHjiPxmQ-BV_dqZEKAwBXziRTRnhYdlUGiqB73Eka7k0_gPxtr5bvUh0RE4cwVfJYHk9vOoN4LWob3Of331_qY3gHZKKbw4dLy8Vuy-nhSUTtCervkjF7SjyonJj6aA_3XJgWTsX-I0bLGuDWKSacD0RbXjQEXfZ22nmWsuv2jh0JpLqrxtTpxmkXd7K-JLj2Kz46PbjJe9OnH8oOMwbo5gIcKUqovDULyCR0C1UusuYtpaqhoGYXeOQSQ5sCtXWofJIIBtVZCnzRSljSFtUNkou4F055UK06piOHHRHD3BdksM4Dpsu9aEX8kPcDK2-F8yRw9VQf3KZqCoKSmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=uFRmP5xGBIoPIJEBjcedyMjF-9f0OC2HGEG7MiyUHuRmexH4BR_xs0HGD1kqNDUs_iVflkGZtMK3CBupxfdBZ-wREhUBm72QSjv8lA3MDSr20VTUyY5xqJOBONbLwNLs7SkcMjBxFtZnSino1Bqs2w3tR-sd9vGPg1swnfSkt-WrpGqxVXliNfW36n3QpqGYCf1cZoU2fTAd3mLb820hW4S778cqTgWGucJ1ULD6zH4PUP8G9fUNwQ0MmhtrldCHNHNVr0dYYeKPoc-Fu-zHUvcxgufykif3dhiNbPq1dNzoiKOFzFT5TaieYYX4TZSqaQcnXzbvp24GSSunnhbDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=uFRmP5xGBIoPIJEBjcedyMjF-9f0OC2HGEG7MiyUHuRmexH4BR_xs0HGD1kqNDUs_iVflkGZtMK3CBupxfdBZ-wREhUBm72QSjv8lA3MDSr20VTUyY5xqJOBONbLwNLs7SkcMjBxFtZnSino1Bqs2w3tR-sd9vGPg1swnfSkt-WrpGqxVXliNfW36n3QpqGYCf1cZoU2fTAd3mLb820hW4S778cqTgWGucJ1ULD6zH4PUP8G9fUNwQ0MmhtrldCHNHNVr0dYYeKPoc-Fu-zHUvcxgufykif3dhiNbPq1dNzoiKOFzFT5TaieYYX4TZSqaQcnXzbvp24GSSunnhbDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9tOaRjJYNTd4VYdBTIKf3LN0q3mzWAZhqA0YUU6jJxJltb33v-bEY960fAFWFqCy5QWq7cUD6CTFuCqEiwDahSzXN9tuRzDJa5NjEtnpd5ejS6sFuhhwDaLhR8hVYQjnCzNOi0FLdUQeUZrco1u-IejGXMyhcED9w1uPFa2TkOTEShNog78Z-S9vvKbX17YHF4AEALaga83vaIlLnOsNGtgn15mHNi5uDYSAul-suwxbOhGwoV-H5zS5M1sXUdzbdpmrvHfU9f0NA3-nnlgPrNgRcYkjO-HSfPnO3Gm7u3JekwG_nhnmO7rbZ_dN9yT65NNC2KqGI-gruDJa8xLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lthX5pUhIby6rNnhLAwb-6r4GPEkLVwB2x5q_1eQOS25eE190toY2xr2IjiSgMGb2xVs3jE3d1G-ijtMDI6ryi8xgIVcWtU1L1s-4eSowIHMexrljLj55zde7cPXZbQuVNGvPCQM0GeTRNZly9rbobKd6cHqpsvIiZWaEZvS_x9_nJtofVGTRyo-FNHNKb5aqYeQPi06FqWyOVhtM6C_ZEzKqB07Eg1y7xRAbMRS17fkqj71asQ_FdjMGf_F_ZJllrMIJgsyxIF7aYYkcUJ3lNlCHKEC4Zy3CMyjlRPri9X4btntpuyfkWBtCMGn0W614bXozqmBAkI2yI014nA93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=lTawUhvDymJMBuha3cj8nH2tM8JIuJjOKCssh-22-91bOcdnbJba-resuVkH0SaeTL9FAqEboK8jz2wxuPW4MKh0XnyfgNTcaQJQRS5-5JplFqDoKZmmA6Y1lcvIvjzClR35Pbn5pAYpjL-A5XMprKnyDfnQuGwI355NLDoeNo3BL_z4EBYVx0uWw7y1MHboEhh7s0ijmF6w7vUUr1V1-cQqtN0330UAISAyF4i3iWVTtzO5Pq8GMbhRh4HxmHu051dFvhh3K6eveXzGQPy5COIwgZyaI3vKsCnbMdqkxY14OQIAa20KwzavgjoRdWdYer22DrEpP_97upICBZOoUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=lTawUhvDymJMBuha3cj8nH2tM8JIuJjOKCssh-22-91bOcdnbJba-resuVkH0SaeTL9FAqEboK8jz2wxuPW4MKh0XnyfgNTcaQJQRS5-5JplFqDoKZmmA6Y1lcvIvjzClR35Pbn5pAYpjL-A5XMprKnyDfnQuGwI355NLDoeNo3BL_z4EBYVx0uWw7y1MHboEhh7s0ijmF6w7vUUr1V1-cQqtN0330UAISAyF4i3iWVTtzO5Pq8GMbhRh4HxmHu051dFvhh3K6eveXzGQPy5COIwgZyaI3vKsCnbMdqkxY14OQIAa20KwzavgjoRdWdYer22DrEpP_97upICBZOoUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bznROxnfrtkJeZaTrrcHRJmoHAk5IMiiEaelsf5FHfztL14hAj8SIoz6TJJ5V5g7FkAV4GS8TwsORnnXL6bwoUQbLuAzXSoztu-2UCCDFvUTtmHtZZJ4ch9yb49WIBjCuVEriwsAIb-tSEKTXnmyniTnhzQfx_653BqfO9gspcrVLiVEbGvBGC-U5G_Owdbs8w3YTUE9CsNIlxHeLIhAvimHRtOAX8S9_nRuPRxJ-D5AGeckC2r-AIj8hgij9--Zk9_WeUA2DQFUfc2mQ8d9_zSZpXLcEtduNFJd1Df_e45xM9C3hOyEFwlvVtVTFkE5OMozlP5ENQT7i5Z7TB6BKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=DeFlVe0KJhZocdiucYftI4RBKrYP2DCaLGE4vWR7YvsgKicoXFQLF-ZE9jFXURJ1DbK_RDKtgEe5opjRGqK3GSFOv8TF97f4gq3pRG2wxPc49DuqnhSYYe_0qDD97Me_onv3Y1kCOQbCYAKKKxuK7Laoam7W61U_o40oHA8QBP0QJNBpYl8A-gTxsqZR3jgFz3m1-m1Au3ge2FuBKcGK-Uwn1KRmhN_ygx5AWoy5CyFDReyoJ00rSU03MbjZNQcPR_UqrkAjA9RVZzevx81zLOtJPgigW7V4D-zgHsR5x0sCMTfCxa2jXEXCMgN7kBdR5CCMFt0r69KME4AaUirwtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=DeFlVe0KJhZocdiucYftI4RBKrYP2DCaLGE4vWR7YvsgKicoXFQLF-ZE9jFXURJ1DbK_RDKtgEe5opjRGqK3GSFOv8TF97f4gq3pRG2wxPc49DuqnhSYYe_0qDD97Me_onv3Y1kCOQbCYAKKKxuK7Laoam7W61U_o40oHA8QBP0QJNBpYl8A-gTxsqZR3jgFz3m1-m1Au3ge2FuBKcGK-Uwn1KRmhN_ygx5AWoy5CyFDReyoJ00rSU03MbjZNQcPR_UqrkAjA9RVZzevx81zLOtJPgigW7V4D-zgHsR5x0sCMTfCxa2jXEXCMgN7kBdR5CCMFt0r69KME4AaUirwtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=sJg1MXTv7QCvQiO9Eg1YrfwzMxWdjKK9tsZPrGdhf7RahKJNCXADFiFterJ57OlA9pi-DPCDzrFqd_q0z52F3woFpFjFDlR33a8ogOEzmpSufO6rH0d0c1PM5tTT_MvYUIJNmcc3Kq1L4fAIu8yQd_yBYfOWxMkIJsBTAGiBdSu-1sL8BVMQZamWT6BLNsRciDXT2wp2I-RHEK92M07q9X5Drm4gwPI2QpSGRnpMKhcIjDjH_kUojhKWJzExbL1_Potp5Z1SkANKO8z_FzVrHXsdHHUt9vJ5CJlatip1mThXvr9x8bIwHaJP95i5i98Ul96CMQA3tDQaTkXbEVnvUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=sJg1MXTv7QCvQiO9Eg1YrfwzMxWdjKK9tsZPrGdhf7RahKJNCXADFiFterJ57OlA9pi-DPCDzrFqd_q0z52F3woFpFjFDlR33a8ogOEzmpSufO6rH0d0c1PM5tTT_MvYUIJNmcc3Kq1L4fAIu8yQd_yBYfOWxMkIJsBTAGiBdSu-1sL8BVMQZamWT6BLNsRciDXT2wp2I-RHEK92M07q9X5Drm4gwPI2QpSGRnpMKhcIjDjH_kUojhKWJzExbL1_Potp5Z1SkANKO8z_FzVrHXsdHHUt9vJ5CJlatip1mThXvr9x8bIwHaJP95i5i98Ul96CMQA3tDQaTkXbEVnvUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElthCOHJMmDilf0PaOt2S-8ns-b9glksLjI93SvSBOKxpskmkcL9oSIHrknNDtUoK7jgBYHKsC7GowDOlD4ZnXrtovQA7dtwASi7AlRgtgn3wHunAMol3KHS_NXpVY9Dfyx-BbYB4ydDr2iio0CavigSPARIWN8UdoUVJQW9WSNXp9Xul19rYvPVFB162yA1uBQClFs3Hom6NpPTalyid5WxEW9r0A6jsV_3hJpNYyBd8ykKafHU6duHPHqRCymvmWVhIsM136Stgfd1dC8O8ARHqwTFaDzA0i3ghTvYXv20EzTBO0BF0YrhSWV2IbCHy6LSpafOUbUlXWbjU2NvhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=IcOWK0EjMU3gieFh0gODFhWIVmazXniRxb1cwDLHeXRfghhCw3D-dc-1UHkC1G8CyjPUTwDy23xxviUqM6kCD2A1ZT78prak_GCeOmPcuH5q0-UMuaNyDZPh5BGFJbTJTOJduRxfD8CSGQ0OKiDY39wz1ITz27DhKt9qIHcEM46KBdvev1L25_lKdQnL-D2_8QFOktQtDIkwf4dsmaFPamiRo4DhJO7HIWaNgcTmY4FtJPfcDBk1mftFt8kQFu2qTKz1U_v7v8xQSm6VxK-u7DbG2a69jP9ZmX8K6RIMObgJjvv6bMsAzv9E-1OlXRziS7Ew9Ere3q8tmichr5ThmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=IcOWK0EjMU3gieFh0gODFhWIVmazXniRxb1cwDLHeXRfghhCw3D-dc-1UHkC1G8CyjPUTwDy23xxviUqM6kCD2A1ZT78prak_GCeOmPcuH5q0-UMuaNyDZPh5BGFJbTJTOJduRxfD8CSGQ0OKiDY39wz1ITz27DhKt9qIHcEM46KBdvev1L25_lKdQnL-D2_8QFOktQtDIkwf4dsmaFPamiRo4DhJO7HIWaNgcTmY4FtJPfcDBk1mftFt8kQFu2qTKz1U_v7v8xQSm6VxK-u7DbG2a69jP9ZmX8K6RIMObgJjvv6bMsAzv9E-1OlXRziS7Ew9Ere3q8tmichr5ThmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V__PKn9E_JFXAeFWadp_CZA2LTfvlQkTQ9sxfCKo0Mp2ydqsik2fTNUUW0wMOPd5_-Jsq632lAvzApe2yKvfrMTbFBQ3OQpoQFKkn-3Ewiswr-ZrOCpQvLLwekBTTJt276DsWntd1rK02EpdMwyaVIYW0xp1wHebnEGmSE818uVJM8NiE-JPzEP8O3x9pZcTD_gSapBaUdux7lCcTHltLEGNgfFV5vc2nLYb-UnrAsvV3YyhyxYOs05iLy5gYrR1CuGOOTXXVib2u-7R1iB1CoAYB_Q7TiOjmSPZyUr-6avnSaqmpZbZvxoclWozSuryIbKV1TKNcOA2_IqQrvWXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQMp7OEg8gZcg40dO3kVL6SiDa2HZ4tY_vZayqsHwPhVLIuQO6-SDINw646UzurBaAPDJYWOs1gA-EkYliTC76ad6W8IrK7dz_Xzb3wKyYGYQMfDSdo0l9j7cF-5JgB6Thu74Qn4kdm1xrgqK-6-UA0W_jE15x9BS68nd-osByC8CYoLINS8RBAgY3Phvl84ss4XOjuBrZlU4jQ3D71FLuxBWBNuNjybp5Vzwtx1Hh52io3tSPWGuIhLEnYu2DuXOjsx6_GTvz68iiSIkBQkwz4l6dwPK25nPaDAOTFq8jzjrdH21Bu_h58KU3xPqqJ-OCZTS-6O3h0h6_uaNh1TFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE1SGVk_-KW3y0KfrZzZFIBs1qYrraT4Y3jHu7-t2cbmwYJCAjevpnFb-SgAGfcSWzAF48RGIcWIIu1t6qZBat7JO568htRD2tZjThiw7kUbZmgSW9cdjru3xlqWc6oqa7Q1ws_4Ppku1pf0AGYkAwfDHqE4RGoLg_oMQw4hPoqAGZ9ETaSUehpiUmhbRzDfALR7dP09udFcqG_aKGwWC3HgcFkIATRA8VRRl-Ey5ye0mzMauujS_7yXebsuEP9vOg4mCfnctQLD7ro3H_irGYHxli2HaYJ7Cm1ou-JUuQ5JPcSrJ7wkcsk-1WIEvOVQCqn0bl4FHi5fE9FWAFVGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eei6XdO-MM7wsEuTgM9odi30BXF7Xicur9c7ogCbYFLcuKJFj-4RRrw14KYAN-uTyJl1fozY_d_n7NhQWdIZ-Vge0e8DgK9LQc6zjP3OmC2FoSSuugzd6hDa1McSVwhu-JmDt3pA7CyVGXB3LQZ1H-7wE_FjHApGihBNFit5UXmN6orrwlJTn1g8JeSFYC4CghckxKu8ErANNywmwn9HfBKCACWhfnqlzWPvVMxMST0r462ACsknKWn80y-rshUla6Odr6cCDTv8JUmS1RFYjfnLD_JGmx5Agnm4E58crdN8bW8X08xcisR46oXyg2Bk3XVeVlRjSLfEkJ5sV9U-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFGePaQY5av3r7GfU5xt7qp01vy-fHDyFyyvJh2Xk4n7IN1amaaIBw7sBJ76tEILXwehsBrIeCPO-43D3ITz2gmYiMJEz2AsvYVlYxyQkE9fHU95WrZFZauElWOqiYOugbSjzz3YnNtY5PyfKOPg5jKzOeP_jannF0irvkyhgk_uuJKfkZvRRKS2QMBl5FzL2TcSAR09Eu43ayz352qsVW5jDa6Rt8T_F9QmRON11qgSTKMCmAQZ0swjaOYDNDDJi2KCchVsjdFozI8nP-VpwlI-YLNO7cNg0ZoQc829t_2Fs5S4bjCniHUV2n_k7jigZO4TUTNt9MzrweVeEHvAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9PDfwq6p9ROzAp7G0AY_ZCCzFPSoSNzYBZS_irlLA9ALYtnQBGq8KgmHSynLpcRrm5KR-1V3zeFmYB_C2lk_TDziSa4A_5wpzjVOOkARNWO-9gyTKjA2esQ8djpduW3nvfgQxBjdPJObzsI3F9YjThPWB4qZTRn3sle3XsTLSeaoKrSHjS4-_-3LYFfTP88q3k8o8goGOLL7PJ1qqcLPibia3uuEwKc3b2gXjzAHLgCbFgO_JQeGXPwtq1L_REjoAHtE6dQitEuXo4XdXQGRf59oP2k2f-BIGaky0OU7-aaA-KOUZeb-gZ8oEbKjpa_tD6uMGVX7YCaHIHftg2NWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csXc48QJBse6OVtV4djT8lP0t5W9yFKBitGR8oRAB1XONMI9Cq-uS0ySS_qAJhGYF9qiLWkM9kXsgQP4c9P5vVWfDiekevn9gON07axLYNTGiHh3ROXF0ssdqmzgGhpR_kHHRHDOfDo06hJvVkN7X4b809LLsv1nFdLPqi9m3asn8LnEMz8P7cSeZNoG7KFiZI5QgX8XZmyJoCaH01G-i1Pjg88sM4BjL34sgkyq8TlR2L1fz8XwU_7ETtJ1NvbbE1FeFdZx08aD2awrq-oox2FwTYH5aJPW6l3tMPS_T0M8YPKWKvm5sERmiSw3wirSfOuw1osqGQqDGFO2IW7Cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz-BHqqSgHkBvy0NWSUL0-EgAiPaxLT6RRawQ-ipoRb6Mrm2T_XdoB7sHgVaiu0fBXvsUcNqJ2NAJZn63QxXV4SZ2Qywh6qKl1FzJMwoLgktjv-otfy0Ztl0DddcFR8W1NVSfRvQw_9AvyCyayuFFXjXJB3-WkUVyoqRhA6aSafWyYLdbOCAC3PMLoS9WfsdejMVnisiHFEeDKKUu3RAFEr9Ot1NSGHZuDorq5BOCAcxx4OAz0Vjm47XCv8C6yEDZK7OR9ahOQQkCmF9dEyvZiTduaJlsjWSnUYBgE-BRys_6b412xOla8swtamfUIR2ZI6hBtliTCuf6XJCfI_TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdlNm0CmbcCIqTvPDiOMR9PiugTRdqA222OFzML9JoiozbrvR2bsuDl-GTvMpqadQOLBy4WT_wg9chBCgEyQIBVZL7d41GQxpguY7q4h-u6_i0zumpwkPHeotmmaW8JsX8Fmtvx_lBT4Z5GzLwDOaB0zeciucgAZm1MTC9-vNAXvTxgYCw1r0ZsAziudy5cQ_rQpyGkQ0qbCy9JbpamgW5OmC4Vfhof0goNnChv1bBVwyJNCSWKGov_1SBR78J86hyr8Xq4j6KiUDgF2fkp3CkvsGHv-N3pl4AfUQKqMUngM8BXIMYXAA7i5gThyXetmDZJF8ZJ0QWlZZrzGs9kZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=AmO4gowIv9gP21ICA6V_SrdNQRzOKZ2t-xmxVLYrtohU8guX8RWg6JjaAVN_AkeN9ZB0GQFwIyEd2WB1w8HaxlXuAkzFtMfQwjhpiM5YZcvPwksQMbzUUeDIspWHxhnu8yfx9TJYn_L1eC6N7opDE3dTs577DuZhjMwGxOfKeo6io3tIhx_mBQK9bAeLAcsz4Sp-VqKFSsCDdmjqWtK6KIIMxoG9aw45S9YlEEs9U5FwpxiTNKUFc-RJQV68s7jPHjdt50z-_Ju1anCOd5iPnNovH1Fk71652NWiwZtrfdqiQnQdXGM58N30zj8nE-jKuUnb0SdlJB6g1Ai7jmy_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=AmO4gowIv9gP21ICA6V_SrdNQRzOKZ2t-xmxVLYrtohU8guX8RWg6JjaAVN_AkeN9ZB0GQFwIyEd2WB1w8HaxlXuAkzFtMfQwjhpiM5YZcvPwksQMbzUUeDIspWHxhnu8yfx9TJYn_L1eC6N7opDE3dTs577DuZhjMwGxOfKeo6io3tIhx_mBQK9bAeLAcsz4Sp-VqKFSsCDdmjqWtK6KIIMxoG9aw45S9YlEEs9U5FwpxiTNKUFc-RJQV68s7jPHjdt50z-_Ju1anCOd5iPnNovH1Fk71652NWiwZtrfdqiQnQdXGM58N30zj8nE-jKuUnb0SdlJB6g1Ai7jmy_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leNP6TG_84NTiX1E5miavr3oj0iQepmoj9yPm6md3eV46mBubpVTlhunBU22rmyO_8tuJKm5rnjajmrpilONcICy7LVtwTFC6gNjN0-3IlLXIhzfbAMknKBpXhf7ayxWZTX3oYihkJ5W9AQ5J49CArNYKinKm2DmDsDlHJemdzTqASWvX631cLAvboMWmE9lUrwsOwsf3G70ebdc96kQ6bhADDWWA2Vod58HwHQAmvjZk3yBUFUOmlmUzKz4tDzaQWSxu9d3A_EVsifzQqprEmOl4KZP-A4gavDdLDzp_OR-VQLRK1Yfu5d-ap4bqrMfDANj01kflQtM5olSLipAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdgc3aKhWF_4XkvBAvWVsnV72GSNInef0zdZ2SUayvKCXlmZSPzjnpuM6Olt2gG6P7R067quI-GIskoBQ3F4ZWAbfn7VGRUA7hQB8GpSViINJkZa9ekxcx7X7tcE29udjk3BoMzpKtfQcJv-ZEWtiZ4tMabqaEMbxulOU0SJZRHcLmLmtoHuHQ9EUpDkcE7YR22i-ghqQLAWfwrToeBCGj8un_F3vw3bxNaHSpmUiFqvKHpAiWYst4sjqqewd9lSVfKZ5dueP1140K63EuclA8o6U8QmDLffxBGdXjgm-IG14vl8yAO_dCniy-VNijeG-WMXx6z1D87UjEM3xG_bbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0JEbTIL2u2seM2ULuUhGa9e0JiYF788y9af6mUVUM2aqyHPcRhnTng_54_VTz5JyW9kMEMcqUEfRpjTSR9AQERzna54zKcfb8ipVYjOljeOMq_RJMYk0enruoZpD0_6hgoutB0knC_xFLbD3_WgsC0nHxDNZbMYx-yg4rJqDTcyTwjYAPY3ykl65Gdue_pquavm04GugwxZaSpvpNoBxkQiugQQ_DyEqhSW-I1YR02CfQk6BffPPdwZ1ZYiRqGc2SKcWWrfC0Fr-PmZDMROdgoA1mStPuo8vVA-clu2w2AVn9PsA_KoIickm81rGB70DbKRglp-4TA9-Cb0y7-pNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=KJD0hWYEKESqb22c3zqsjtANbY8UZlwprYLASmR-xpiVmPzKZvEVMFL-8r2W0cUnCN7E2R2ifZqX0WJpTiVDIPmAxBv3NjOZtifFirzCXi30Y09DjGdS_ZK2ObLBcp304nQ0obUGhF8ErfDyIsz3qkfZXA4NfRjMYH_AyB3hq7fXHjVgJ2klngUYsJDuqJGlPSWMKX9PYauWTfA1MeSx01f5rZb78fEs8U2GWtDOP7sJPn2yKXZBIWriGbzyC2AoRXIpHXfsVcGTjoVO01xrG3dt8OzwhrqyRunC4PZAyB3afJzjE143-u39sjuMR8CmR9i8SlTUFCna2WAAJGmmFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=KJD0hWYEKESqb22c3zqsjtANbY8UZlwprYLASmR-xpiVmPzKZvEVMFL-8r2W0cUnCN7E2R2ifZqX0WJpTiVDIPmAxBv3NjOZtifFirzCXi30Y09DjGdS_ZK2ObLBcp304nQ0obUGhF8ErfDyIsz3qkfZXA4NfRjMYH_AyB3hq7fXHjVgJ2klngUYsJDuqJGlPSWMKX9PYauWTfA1MeSx01f5rZb78fEs8U2GWtDOP7sJPn2yKXZBIWriGbzyC2AoRXIpHXfsVcGTjoVO01xrG3dt8OzwhrqyRunC4PZAyB3afJzjE143-u39sjuMR8CmR9i8SlTUFCna2WAAJGmmFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7Y7AnaDgg81oCtl2N_t1u8NkuaUzAU1yGz4TJs41L5DDOtcR5NQLt_6nvsIsXsSE7Uqlucyy0j7a8bE-rfBh29QJpe9FfE4H-ivcEROzdtYiMccc2EqwDojsIOpeLQMnPrxPh3BxXv7Nsgv9kaODohBcu1z9QOV3URzDzhlalzl8cEKD_ztXeLK6kBR1HveqIZb0aYwUXOT46BrCkmydiG4p-lsimeJBC_h4mlRhbus_w9-UxMiaOf_mhk2g7QGXjkfIaaXXxzcj5uT5jhciJh8-99fwps6HYXv9ZwLgPkebfbuK71jbuaSEJDEHctEKQG6uXNeL9TFuPAiBVwaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=rxFrtUThaik9lmimd2KsVkU8F7rD1_8Z3HAyxyh6pSGGr1EN2cvS3TXLiWih_Mrh1u474NPI33Fb2yQ8quXIIk3Eu02Tv-XTzPTc1gxi5vHsHu8LhULEEvHq0iCbcTJRqknMa0b9cXhpo2nspETivyZN1YRPvJ_ODCC1ojdX0rsqPGne6TnYTfQCwRSEJW-GxAo4Uk3JtremI_UAht94eoiyE1DGkcVxv-jQzmCt4CbheE__NyUPSonpW7jLTp1jovn1U1JPg3KmUnYxHScMZBs_Dqc9W9dq_eenKKRJmUeKoT5KEVulu_brZ8PBcWMKEiczqi925s5anXx5gf6iog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=rxFrtUThaik9lmimd2KsVkU8F7rD1_8Z3HAyxyh6pSGGr1EN2cvS3TXLiWih_Mrh1u474NPI33Fb2yQ8quXIIk3Eu02Tv-XTzPTc1gxi5vHsHu8LhULEEvHq0iCbcTJRqknMa0b9cXhpo2nspETivyZN1YRPvJ_ODCC1ojdX0rsqPGne6TnYTfQCwRSEJW-GxAo4Uk3JtremI_UAht94eoiyE1DGkcVxv-jQzmCt4CbheE__NyUPSonpW7jLTp1jovn1U1JPg3KmUnYxHScMZBs_Dqc9W9dq_eenKKRJmUeKoT5KEVulu_brZ8PBcWMKEiczqi925s5anXx5gf6iog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4yiU3fOgoyr2i0ql_gj5nhXz_-G4mjITjVcVqx9ateUPcHO6XAoPyIqGtE00hOTKWsArYVhJMioiM_YJVKfVU6hjzLcIxWFmcSiRyDR3VzPG5aB2Xhlk3qCHafFtfILouJQB6yn8a_JNMBB_OZC36JEwDBzDxQ7Da7svEC89JSiCwD5D3sHkAjHSmP3pMIWrOJs44FsGvjrbMYk3v7PYnFRvViMe_zJ0CWCp1VFsqTsLXTPg-W_LiUMxeMZaRtaOemn_sGQFXUtKHbSc9hHMJpLV3mD09wCqa1rcx_pc5dQG5U7njd9VLrCKOw720N8ySnRXaKXHbtYF1LgqNiKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5AP4m1_sfXflA4kXw94EczXWyzD0vRZ8H8d_IWALMItZo1Sh-AbB5E3O567_Eg_TBUQbgnNnOaOjfQRnwi-8wnYA9bbXJMRf52OM2Nv446k23442i_oXUPGWTUEBZXAkyNncB-pj3ByuetV9qy2WJ9cTLQwuJ_YKPamHHnTAfbC2fi4hsLGYySKT7DH591C0s7NCV9A_q-5akBSZ_4Fr0NpFqXATzdFpxFEin01X9kDB6d7vbcbvup6iPTwpuIifIWnivZfrmTQLcTmu_Fb8sYybuZ_peXAlkOpLw3Wnv2E4k0VtMm-gUAsZvhk1Wnq7At7aXgzz3Q7rMaXscsjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtKvvST_iO-5oYQdVlrr-eGNy_6ylc3R8mi17pFKfHELfBem8uqSN_Gk-91v-vFT16RtPmhd509Own9VTV2qfsiW8oO26PZDwRa4AXblblSlxTeW1brTB8Il0vtr56kVxD3ruLN_Mpl7Vfj3wQP3cVZ3wjMPbyScdhq1X4m8wgaVpW401Z45IL0jGEXFLHoFL3xRwMcPTnxGZzv23vHVy7gzHtrDJVuOzNnyF4MSDX604IQwfFCGATc_X0WcPik5XVb1ApUn4cFkAoIWy_mXRBaIMDHAsatlkcqn5u4MLzr04jKbET7M2meBqf44aVizFchv2kvNDATu5QuB64Rvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=T-G8rrxHCfC7bYvSuJsEpfO4upoqTm5JgkMV78_AVTc81IFz9PFVxCQ-HBRELVPagvz-PvPgS9UdjlGDzlneSrIi8d7AMKak9tlQwGXuWkk9pYM8zYp8cfE0qsYDs30-0xkq3OuIZU_-did5xAJBRdcfwC6gkEE9-ClG81eu67Xi9RLiLW7KC9MUBWusAZeO6m1JhMd2qx0iitOLP5IacT2Ds3T7b2O0jZPrw2TaJryKKYzuAd3mJCTV3QpzP4EjexOYs3JqN3L8Le6X5QcrgCGb7BJoIbtxOpilI57a9tTlfQ0XNmO8P4q9u8k536eR_isT_g_ye34lAlS0D-AGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=T-G8rrxHCfC7bYvSuJsEpfO4upoqTm5JgkMV78_AVTc81IFz9PFVxCQ-HBRELVPagvz-PvPgS9UdjlGDzlneSrIi8d7AMKak9tlQwGXuWkk9pYM8zYp8cfE0qsYDs30-0xkq3OuIZU_-did5xAJBRdcfwC6gkEE9-ClG81eu67Xi9RLiLW7KC9MUBWusAZeO6m1JhMd2qx0iitOLP5IacT2Ds3T7b2O0jZPrw2TaJryKKYzuAd3mJCTV3QpzP4EjexOYs3JqN3L8Le6X5QcrgCGb7BJoIbtxOpilI57a9tTlfQ0XNmO8P4q9u8k536eR_isT_g_ye34lAlS0D-AGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSlL7SyqnHBc_iL8R2i7V0-nb_xj7HsGBwW6rkf8ORY6kD2W43vf7-J7Wb6-D7SUZrHA8nMjUyFDlOvesxwQ5FN9ouCJdHRDNgPvcmIa4vPUWJUxlriQHvjFigYftBlpI2DLSlyIRsFoGw43TxAr_LCiS_6hVh1iu-RqIKYevZs8IXevXcddNdZ2oO3_bbZIusnnKW88aMgOQqkRjrOYZWgFKbmgiQegVnnhcPO2PAZIT1RMgfqK6KP41HmqW_T_y9ez3i4Fgd5QLM4Fc0ORnjA2v-8BjkYZwBfWuAIitwXT02S7-FEpgY6q2kl_vtZujbJ19Jt-VJLujJ5IFqXIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B91YROEHNLnfIduZRn_kme7z5OTgty5xrR-9mib-WyIpL4L1I4R-m1c44rS9h3omOuhfz4JUAGGKBQMxq9uimdil5qSTp7bH-JWBRwO9hgQWswuAtBfWG-Yr9mC3YouBIn0hohdWdU1yO-8xbqrFIOa7FOmxgwtOd63yLsWQ39m7NgxSEA5t50LF2wjjbftPijYzJOxNBZ4CgTdkmxo-peBta-ypP9ClAyDun6Wfl8MJop7b9LeYbgsh0aBXBxXWCtlmLsMNyQFkBnU_z8kwF05vSf-I1ogudEJjkYHCxgHYE719aTC6SJmS776jRHKh75nlAl981wPT1_FvkcNPHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=TBnPraA64vBmJcOEB6l0etkBnm18dw0HfW1YJD3BNpGGqO7nLQEy76ZGP_s6RYzoG14ghfrwP2x0pUfNTicuQgPBFopCBWUpXicUG2u9Ki_DZyiVQVaxliIGn-COLB8NN0IkoQlUYBHM42PoEz_y4cGthmWKvdZJ3xvRTWbhVH6AUjtbe_djjUCNoNX82sk_WjoSmaeXmaWtthpEQcsxIBWuhw75rKDrsMffmAN1Dc_GSwB4T4GEf5OPUpz-mdOZPCo3uHxVKj0A6Xrm1QjKL0mBEfbagCL_F0df_H790na8wSfiZwUPwnGihuiRbw3RIXKgwNQPiH0op1QhXPCoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=TBnPraA64vBmJcOEB6l0etkBnm18dw0HfW1YJD3BNpGGqO7nLQEy76ZGP_s6RYzoG14ghfrwP2x0pUfNTicuQgPBFopCBWUpXicUG2u9Ki_DZyiVQVaxliIGn-COLB8NN0IkoQlUYBHM42PoEz_y4cGthmWKvdZJ3xvRTWbhVH6AUjtbe_djjUCNoNX82sk_WjoSmaeXmaWtthpEQcsxIBWuhw75rKDrsMffmAN1Dc_GSwB4T4GEf5OPUpz-mdOZPCo3uHxVKj0A6Xrm1QjKL0mBEfbagCL_F0df_H790na8wSfiZwUPwnGihuiRbw3RIXKgwNQPiH0op1QhXPCoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=tyto-oDoCPGvSGsAKHq2D0oxzSEibO-yD1RTPxuvm5AllaN3tRpigLC__1uSGeMKrBwaeGB1MkMyYehbX9InXDiVUhPofH_qM4tqiFEtmSKVtXSYutoWNg1OVs1uvVsfOIIRR_LoYScUy4uG4Xbwn-eIzYudK-u4agCjYJ1UpQYYvJmZxmMXwggYlxJgPatpeIeQsTSteWMkZVjwO1-RZTDT4wDXwkCkOIzJ2B5TirJdLJlGv45_e6cl60gxV_AdaNSs8BX4Aqvb7BoyuE90pq9jloq9Su4T2keBW0m4RL_N33AmksGAETdUkwedtQ6Vb1lar5HyTEkXVM70R1q3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=tyto-oDoCPGvSGsAKHq2D0oxzSEibO-yD1RTPxuvm5AllaN3tRpigLC__1uSGeMKrBwaeGB1MkMyYehbX9InXDiVUhPofH_qM4tqiFEtmSKVtXSYutoWNg1OVs1uvVsfOIIRR_LoYScUy4uG4Xbwn-eIzYudK-u4agCjYJ1UpQYYvJmZxmMXwggYlxJgPatpeIeQsTSteWMkZVjwO1-RZTDT4wDXwkCkOIzJ2B5TirJdLJlGv45_e6cl60gxV_AdaNSs8BX4Aqvb7BoyuE90pq9jloq9Su4T2keBW0m4RL_N33AmksGAETdUkwedtQ6Vb1lar5HyTEkXVM70R1q3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQI8l03la-NHpsjNGCpLrveutLxdPnTUE-oc_BJcs4wrQ5BncDkKWuCLUrFgwVZYgbJBDpXxYmDCwI1QbasvzjayFvCoR6S68y1ldpJ3U7LT0TK9iyFVytYgyNrlzzT6whuzTbDoiQdiOkRYmF-poRSu0gT8hHiEo-XFCszHYRDeJs6s6DLd3r69jHe_yZeh5_sGOk0AgqKe8AV2Qbym66qUdG4y4LX75ZbQNtvjJ_kgtONhpJrmz3NxTxwCl3acPc0fGBeQQvRHityiAkMzTb4R39YV9HjOkDNvHIaVVpEWcN_YaQAWhPYUehJoVEoqLhpLRecxFl42TA9Y8l9dtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8LJ-2XG-FgQDr1U8Xvtvo_R4LeehIF-wYae9fGQdMjQPv3kH1Qq8YShcs4jij8kUTeaf_w0WGFGg3G-UaCiMzpumalCH5FuP9ta5w-aAU7w5NVypXsBQupLKWpp6wT-_FgwMSCrHMORkXCOKVQg--z8-bnMxmjozcIq-QFDQpIyBh98qw6sgCD2cY9rUlLqzuMJbce7bRqJu31pDnTE8VCsElkSo8uGGM0G7GgljU2QZgPZbSOBxkJ8CoID3zSXwubKKa9Tnz1a2KeuFl65yRHd1rqjxZerFh0Tagu6ou3k6-XmRXAcoeLWttH_JyOcfhemiOmpV8xmsT3WhP-_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
