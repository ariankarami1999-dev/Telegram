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
<img src="https://cdn4.telesco.pe/file/BfD5Scqb9-lcxgvvsVgL11eeyjZEiEPfFq6aJzYmBaHPtRZw8IkbdBZz9nPD2E6Ai4wgxOO7C6nbPu5uL73MravNhUYyR8-Rw7NyEn7V31dxihfY_Zea8qfiut3M9gMFXua-ZExgkVx1eWolWjAipX3N3r5Lg-t0uqYlm47eGpfPzufKhxa7Gmgsrnlhcyualh2tJWW7zH_i9NOwNQKUs96_Cp9lgSCNmQ2xEQMuT-AgfUewVV2bubCeyiJQDHC4b-5r8ExaCt-pVgFivzopkmcxbs8mH5UckaCYnpnMu_WEr-TOaOX_oQBayCGuK5EgqQPEl9JCRKdfcX61HxXpBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 306K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhMA3oGzf_fABv_x2unfpq3W_IEan2mbPd8VI_HUrMtUJOWDl9DqFHB4r8ypPRIBDV-Xl5mUNzXGTLloY51trAXk3TW-LIAUmtocfj0N5kLXGseMPXKYdB9xBBj1UHvADBfpA1_rge6k9zqeNTTAtNDvnqGJhvFUV57u4z0_T-Z1PI-mtkD-uN6mQLgo-y0UyXhtExVURCQ5ePErYBfz07ChKCnGy0Zdxm7wwfrCsac7W79UCRX0OvPOWQjKGen_RiUSSo2Yc0pRQaKD26b8JCg7nbRYtraR0sY4xCEx1icdfhwjO67kdnhN1rgIY28GG0FO6v0JhjE-m7pYtGqHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-7iQzAvLC9FaONHj8uMzlNzCXJHI3z0D6LGqFe5x0OqXpV48C5ZA6pt9cop9QnMoOwjKphQ2P_Y1K_78RbcpE67PY9Rc5uyDkxA_6xGtk-KYv7_L_S6wIz1gLvRIaZ9w1W5uao0M3UJDlEw_0AxK11cc9SFf7ox1rZWscpaJJu0_0v7k_o6lB1MrkM1WQrspDtrhd9BMiw9BH22zyQfVqqRYO8FpCsJ5gCmnqujaUr_gA4TUI7j6xiZT_I9y1XNnvRR1mzkbxrXVUHDst5zhw9dLq5Fu7FHF4weQGvCM2RtmGA-Yy2D-NTHzClR4s7f2pzN6zfsytbPdppBYVc9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ca0nFq37Tzl7X9b3vjQ2nJp-dYMgKarOriHF-pQd9Qpdpe6qeaOBEXs1RnQL7vwTz3xyM4T61PtU8151wG4xocTPOnqsEMuz5CRDe2nnHtqFhKtRc17TDM3H5ZbzPi3BYujjVbw3Wd1Twygrmg3J8m8ausAISooKgMZ2pQBriHIWS2fxuSAXJQ2ImbzEIL8d2u0tCf8IcVBOSZT-ygjJOnaNJZvT4Q6UEFUj_tIwbMql29RhuQrbt0LcciS9fvNdCW4nolhBEVb8wfd8CdlOZiNOfUJj5e33HQjsGuLytuiUMnYIRGH5fQ8Y_jbfdOE-ktaZUHP6M0U74iCs3EyFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوووق جذااااب
سوئیس
و
بوسنی
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/persiana_Soccer/23739" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adMqRszGFEbWiRZQE10kcdY5VFkYRXvY8cPfv0TKjNW67Ao2MnClSWyhaAIZlkb6HA7qHLSrdqrd1oY4BN5FkIrOaJqNWFUYfOCyF--5Bu1kyoHO-Xlf56XR60KSBNHMwyYKEhTACpi_Cu7A5XXjT1ddVu8VwbCOBSR1y_A5Jp6a4LsEv_9bjRTA8Kqc8eqfrr-GBxRP0Ya9xqYda4Xd4k0WS48q-31R9Subt5QYzg3QknordDOvaz9FDk7kmuSQBTNtKZUzZA1LwbN5EWipC_KBo0W5lVyOINcQJKZh6HslzVICWJIVTevinPpKWW-gPUSjmLkld8yg0yVS0Ap1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Ci6-FrGtU-PXgpWOWzJ4eXbxpjq6lvCGjD18N-Tlc5kUtrskjpEMl-Te7Kazq6suVZrsO84XTtAPv-DzUsYZMGRCvCjxlNzCVWKRiTj07wZ-IWd-HYhFmVWm1kFb7AXB2UuCAbAMKBAIqr-_jo0xIKLe6cFzNpu9gamm3GWptlMHXzeAxsmgah7jnEWImy1DSwv5-VYQFY3kNKk9bqANk9rDs8nprA4mgJcoEK7MPne9rs5JiUrL4Mxogi91ayZExJxNWTQ_Ps84qgYac6MRz3fpgAotgZxPx8Pjd_iZizuxVKk4kFKDPoYPE1TBivLVW3zsIi-DhiE56EwKOSvh2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Ci6-FrGtU-PXgpWOWzJ4eXbxpjq6lvCGjD18N-Tlc5kUtrskjpEMl-Te7Kazq6suVZrsO84XTtAPv-DzUsYZMGRCvCjxlNzCVWKRiTj07wZ-IWd-HYhFmVWm1kFb7AXB2UuCAbAMKBAIqr-_jo0xIKLe6cFzNpu9gamm3GWptlMHXzeAxsmgah7jnEWImy1DSwv5-VYQFY3kNKk9bqANk9rDs8nprA4mgJcoEK7MPne9rs5JiUrL4Mxogi91ayZExJxNWTQ_Ps84qgYac6MRz3fpgAotgZxPx8Pjd_iZizuxVKk4kFKDPoYPE1TBivLVW3zsIi-DhiE56EwKOSvh2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=O8d38wAJyqAhRWlaBzh2wE47ltrShuYHTL24kiGg-AJAq3w__vlBf-bwns6y08wFW5vTWPY7vTwkIt1mlCYS6-wipjHGBtK5g37BaV-ONVCWgZREXsN3GLYRfXfqlB7xhtjMDV7fXc3ow-2mmZk3tm3shcyrA19kfXlLdAI7A0zEnhvzoMzCLQx7YgpieYnBg4s54pwl4GVE0AFaPDlaxvjwkERGr7aWGMkD6r7V76yE61PFcxyEi6YNA8PkqsaUaosic6Pkn-lmqDI8TFGWbVkqHrDLexeh7FGc3cVZgX0nol76s_zd_2w6tb7UqlzzCEZod8Bei9m08HXUantVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=O8d38wAJyqAhRWlaBzh2wE47ltrShuYHTL24kiGg-AJAq3w__vlBf-bwns6y08wFW5vTWPY7vTwkIt1mlCYS6-wipjHGBtK5g37BaV-ONVCWgZREXsN3GLYRfXfqlB7xhtjMDV7fXc3ow-2mmZk3tm3shcyrA19kfXlLdAI7A0zEnhvzoMzCLQx7YgpieYnBg4s54pwl4GVE0AFaPDlaxvjwkERGr7aWGMkD6r7V76yE61PFcxyEi6YNA8PkqsaUaosic6Pkn-lmqDI8TFGWbVkqHrDLexeh7FGc3cVZgX0nol76s_zd_2w6tb7UqlzzCEZod8Bei9m08HXUantVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=Rar9Hi6thFV0-I85gf0r4tvwgBU1GlSXO1HhvTCX-6_6Dah888Zp_FitnioCMuHyURNT6TJuThhE2E3tJ4-4CdqIa4tkxoaY6ns6fPcqtu7g-YPCJ8Z6-s0Ux7xxTlCQQlynvlCD3WzVfiWX7pxtNy9wuKC_ieL3v_YLFbktT7LN4g4TTFZ8VIbc0Aq1mcaOXRKKl2V8_VTTXHIAZsSlblaEZs1rKbKoEY-d3L3QHLy4l__mgjqVfUfnZWNBMP2GiLH6e9nqKzMAsUSb2G_ucKISikbaTYP86rUECa8eHVzmlqmf2uQiC0s0ssjED-IuELQO9lum1hZtHkP5JjIT9bB4PBq_CeuTabhfqRdopxUJPdVJjJfFTeOa6WmdXnWvM9DU9FlRhh0GcUDz0VNYE8rzlbgq94q6tb8awq6dUfbNkRbRmXKL6fL31tTcM6eFJV0IgBVTKIMpMZjpiFj-cazmiu0IhLWZjidjwuAGVsdxK3nP63P23lVCHZPpMEXL_ynyioUpYLXU_Z9UBy639nMIeIK7OC3fBrHOE7ymfLzygxwEvUF5FXC1nzow_BFXm2YANwLB-1-w5KXIklljdGhNcLcw7p8ydlhmrxP2VYk5YRrEz09uQyi0quUcp_wsEt8Z4LRHOq2GP67VBsX4YWN-br3wxVEU6ouf3irQNwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=Rar9Hi6thFV0-I85gf0r4tvwgBU1GlSXO1HhvTCX-6_6Dah888Zp_FitnioCMuHyURNT6TJuThhE2E3tJ4-4CdqIa4tkxoaY6ns6fPcqtu7g-YPCJ8Z6-s0Ux7xxTlCQQlynvlCD3WzVfiWX7pxtNy9wuKC_ieL3v_YLFbktT7LN4g4TTFZ8VIbc0Aq1mcaOXRKKl2V8_VTTXHIAZsSlblaEZs1rKbKoEY-d3L3QHLy4l__mgjqVfUfnZWNBMP2GiLH6e9nqKzMAsUSb2G_ucKISikbaTYP86rUECa8eHVzmlqmf2uQiC0s0ssjED-IuELQO9lum1hZtHkP5JjIT9bB4PBq_CeuTabhfqRdopxUJPdVJjJfFTeOa6WmdXnWvM9DU9FlRhh0GcUDz0VNYE8rzlbgq94q6tb8awq6dUfbNkRbRmXKL6fL31tTcM6eFJV0IgBVTKIMpMZjpiFj-cazmiu0IhLWZjidjwuAGVsdxK3nP63P23lVCHZPpMEXL_ynyioUpYLXU_Z9UBy639nMIeIK7OC3fBrHOE7ymfLzygxwEvUF5FXC1nzow_BFXm2YANwLB-1-w5KXIklljdGhNcLcw7p8ydlhmrxP2VYk5YRrEz09uQyi0quUcp_wsEt8Z4LRHOq2GP67VBsX4YWN-br3wxVEU6ouf3irQNwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8XhYfdKzyI0EpXhoy74ksE4GUjjIv5hc9VfyRNncp9dT0KUw4qsi19k-OsVMFX1w_GBmwpE6YZL3YqJPrE2BqntsvK_v0TVi0yoKsmX2t8wnETo0jWAcxg7dHHoGsXr7ZkAD1INyWEr-tPEip-Kjs6eQ3LMsun1YgtceR3pVT2RYPlmEBuleFJctKLihs07LJr_DaWlSxJ7-IS-hH2RV8yC86mBa44309NOaUn3y3fIjQ3G8CXvEeBWZRSZd8d-20i429UWiqxWETL8IcWywa5Sx6YDUaJZIXu0Exw7pb8mzYwuvgv8Z-YfCU7GoJHBC_6E601J-_8Yp8WtX3tQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOAqdNHMJrp97NOkPD6MqfHtdU_Unx3esDEJjF2JVGt_65h6xruhY76Z4bSUfzMYSruvL610oJjM9DMRA1AEPRzM4DE37V7gy05aQglu14m8LachlVPf31QdH6j4mw7nZC4Kwpdo7O4lt3sB1olGRPKPsAl5VRqHI93jrRggB3ZHg4IOP7TbxgauCUTmunAiHxGERyVHruNP4_yDArEwSxVMePgBdfEWQmJBMHjir8vRVNUeyJTd2ZtwYDnVEdLM_zJPWa5otv1QPJ1AReiLUXaH7Ye8m6o-VxHPKXmg3rcPVq0j9Qr-4dTr8nwUdRrqeADcFZ2AAg0Ix_AZI010nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwZluncTdaAiO845Onmh9R5JKkPm5PxRbtVzQDSVXnKcaZDcoG9ZhLrdeaxAfRHQ_d37fGf6rfiHrje8WxPx_OfFcD8Rt_tD0YlXoF9YkCA67EqF_NL3ORJ1wS24JP0UebVAf6q5btxLqeVyltWBEbfIztpljg1c6XtoZO8voapSsrx17vF8kfcud1jgzkJbUM5YNX8x_8TsdOEhpemh2jAHm_o6Z5ixyUeOchERCtgoFdM5Cau0fxuMUuIcDvRXNNX5-QsUyRohHmJ8nKEbS2iTaPLUAI-C8pb-KbFUSTAK9TdXV9rkw-0LKj34rFfAZgRbQP2H1sajlu6vYMubLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4Nvjwd2ildinOnYlBYvAYTVZNstEtYRGEEmhR-TBHpa_yR0FG0kistLHorST0vuHnvMNXwOJwF-HmosM6rdCnc3zIBwCr4xSQsXbDNz-fpcUiUIJFXOCtE0GZtSB0sP5PpUln7HEf65HRKbw2OEPZf84X1bJzwzNChrgxw_2mv2tkdox-LC2T5vI7Ed5Fo7bm_ie41AyF0KkcMyIi3jCwGnbBJE-wDr8z4mPU3iPzvrdIiWxniWo8XUIMbU3gAkiDgwuCh7rWuYRTh6mbA9z2egUhtFc2lCY4-l_ZYzyNVOILhpiB6LfBIm3FeppMC0aZ4uWoYObDJVQDPb8ul67Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcnHWXrnHohhlXM5uo1OFOJE1kjNolr8i0d6RtLQsZe9Docxo1B-KNQStblCPJ7ucxMnzkZLT9RX7Dsd3s3TTdSqCoXG6HkXa4pMTpC5fWgllanWIekWkGocq6UGXsLuAzHxdUcXFhQps1EK-zfVXyGexuRs6GC9wE4LT4xdq6eRy1PoMakBNwth_ygWabkhCPW3QTKKhgaH664jRSjtubpQ-Ng0WT51xuOYZlksMTtv7JjfDH8YKwQFOntQ41C89f2uzt5MqEsKT-u8YGid476sm_YA5dtgg9fPXJVfB2mG08WlHij81ZxBSNDJDerVtkVEMefrJ-beaTxukR-npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go--l6Llhrv8p6DH0umyvxuKPOmnaQ9FkXn4dELGQ7gDGB3ICSNmp7uMRm0CSUNqpqlSdzbiT-o7BoP7iz2xpUllIOrhRrVEaEXLzSwYMFg5nWYOoxGZF1SjAl5nK5Ne0PFXf3DL_jy7BfiZ1CXuK26Ude4Ra3zb5pbGloIHD2HXY9hh7VcaU14sc5bfmuP9M02lD05huzUf5IlNK3xC5VrtjOhwfxa_uYAaiy_--nUEHPy0e84SI6Gw2Qj6USn3sJ95EK4A_IZh0t8s3cbvFmJaTi8IClvW8jHKj546xrb8-rXWz-KEaNZIfFfZyaFulnDt-xo9-TEGo8v7AvowAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgdiupGwwGmUAKvX7kh5huTGspZ-LiYB2mD0lp4H_X0ClEHzqBkdw-dRaP7z9hlssf0BNoL7950vv1noz0jpfHyrEu6D9ULqOfv0bUKND_HTGdjvlcIKjawFDdbi5EzlE38rRM-qPZRZwlDSaifTZj71gM3G7KndAu0PqH13pBnbTZd-QbXWciswBWq6l5D2oKeMfTcOs_ZXUXJ0s7gMNZSnv_t_jT9bvvlCRJqVd2PGAIYM7BLVCYuJQ8bH8bfIZay5vvvXbYO7AiQNsP2Vg5uZO7JUABY0msQxM-RrK6Bvj0nRmPW80CNaYH7GhXNX_oh4cftjJucGEVaTviP12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDM9uyYHSLHqIrsMySUVuNA2jHBx78YGWmgDWt0N_1uBRx66gBNt8z0S6b2Uo6q5nObEg3qhh-mU3c1cu8fn3ep3LjHxFg-HISku3DOV9jBEy2FAh75Ees6G5CIHWv88DJdjcX_0b8qvqpXFUJzw6d81Y05WwCtK8c4bmRwKOIHHg4MO-91-EtIG_c-m6ruE0dOrdGlSxxYAFHPenfyRUZOsGNZoly_VKM_sjveDJEfvjFUZDXSZlSPrb_YsAWoqi8yuYfiRmUt68FlCAxd51XrMWYHONy6zTgzLy9lkv8ghTP4HOO7qAMKwM0w1MrxGYge06ysen76tIOW6LFJV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=s066E8ekt9FstEUrrJAMNfpC-4VPcsNV-SesdsTLYD6Zoi0mxPSBCjOlgo8afPfPlQ3vGBznLhewcyF1LG9_-E0VaSmkj-3d_NVajz8_vCYK-05DguB6XO7ZKLZ8d3Z-Nd8r0M29AF2xKSBTQmtbv5WR3493Q-JIWGtVuxhzaD1U7ezluC8_ebOYrrv15z8SiQHhmRWqLEoxI1Th4ACAxqUADtJzFkAwT8-E0y6O_I6uKvPhdVjmJG1wFP431qEE65WHv4lQuT7OoTAFbd10WqTmq-GPEJm2rRaiJCjV7adR967sYuNVxKqKUrXPYFvLp0u9qMK2fEllv93We21laA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=s066E8ekt9FstEUrrJAMNfpC-4VPcsNV-SesdsTLYD6Zoi0mxPSBCjOlgo8afPfPlQ3vGBznLhewcyF1LG9_-E0VaSmkj-3d_NVajz8_vCYK-05DguB6XO7ZKLZ8d3Z-Nd8r0M29AF2xKSBTQmtbv5WR3493Q-JIWGtVuxhzaD1U7ezluC8_ebOYrrv15z8SiQHhmRWqLEoxI1Th4ACAxqUADtJzFkAwT8-E0y6O_I6uKvPhdVjmJG1wFP431qEE65WHv4lQuT7OoTAFbd10WqTmq-GPEJm2rRaiJCjV7adR967sYuNVxKqKUrXPYFvLp0u9qMK2fEllv93We21laA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=SEhQnh8J2YyocmhuulCPkwdD7I6vuJH_D8YfhlsjX_OivUlGPuXvIYnaMpKD7LDDgsCBC3lzglv90ByVJpNm0OcBvx-7gsGn4_g43fZrQ0NicCUiUhgBeiIWbeNHeJLYquRGF6oBNaOCWbXHYWUU2-ZzaX6OxJXjJ3AV5wV5xhpeKTbYqL7j1z0_BLVLVCQ09JIQvHI_hjRvH84XdxoiOFIqgq8ywt_l9CEqi_8nRl0bZFFzAlWFWhr4uQ_AIEulifOsSrWolaxAR5s73lerp3F7DVV3QMpbIBunv8miPN6uYqZKPM3cfz5dcIuLsmAJ_S6AifzDtvtxUZZiXGosJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=SEhQnh8J2YyocmhuulCPkwdD7I6vuJH_D8YfhlsjX_OivUlGPuXvIYnaMpKD7LDDgsCBC3lzglv90ByVJpNm0OcBvx-7gsGn4_g43fZrQ0NicCUiUhgBeiIWbeNHeJLYquRGF6oBNaOCWbXHYWUU2-ZzaX6OxJXjJ3AV5wV5xhpeKTbYqL7j1z0_BLVLVCQ09JIQvHI_hjRvH84XdxoiOFIqgq8ywt_l9CEqi_8nRl0bZFFzAlWFWhr4uQ_AIEulifOsSrWolaxAR5s73lerp3F7DVV3QMpbIBunv8miPN6uYqZKPM3cfz5dcIuLsmAJ_S6AifzDtvtxUZZiXGosJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLacYe9USnsabjs_cxiVocP1ZjNUTDF7WQJERm7zCs7evWkwYMFv01lkQWEBq3tPvJ8QkrT_TZMg3KxFtCJ12HnekOmaGWs6k0iC5R1I_qJg0fFE-28CF-KlAwchPkoddsSP5T33W6VYd5Ic6i7UN35bUeb8vmLbCP4ST0q5aTg6vpFN_GdgnwHGGUQXEDMr75AiL7kT-TwwIRvAFqBy8GJaLJ9reRYYE_5DTybyFHquXP1FjmVGLEXm-dE-YhpQvpWP6YdvVGKSWRO6kvxOWCF40N-dC3HiD1gfp-a1sMOAzCvKix78wT-iGidZhlq0oDkU-1W50a49YVbp1C8ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای از مسابقات جام جهانی پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون ea27:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23720" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOS7K5h2nMgWLCuPfHWxY0Sbqka4AZkV4BhPB2ZeAsAVXiRJGWrSBQaI4PnZ2Pbu59g7eDmuf7376ExETkhUscmqS2WtSXDHzLXz8V5-_2PaIhVvcoFM4Fcwp_SJkr90Ou83Rgf3WNuCWXJFbkViIOS9Bko1PIAx23uUTPqjkSYTzY-219kI3A4wxrBbcjOX0BwWQj7Dr6vYuQYQXd8y5uoIFOOx6xvU9d0rmOn0TqiBKWWnsH5n_UTYrmmpqpwT_p0zVXPIRCNfus44nnoue7hlNGpApqSAQhzyujos2pLJKvynGKFlQjANkc_w4AiEnOn07iCg47cpQ4vMf8J02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=ot9yDT5s6uHzNFy7HuqiNKoG3498c21QfYIRpWnbdI4Xz4eI6fvSjxpK7GntoxQdYllcQ6QNUkhBapUPyYJO1r1xMlhbBg2rjkTbR4AF6tyA-UGNX-ZeOp_U7n3ku5DVl9B9VAzEptO1aSPSu4bbQvQdVcL6IPcZ_zHoNhgwhRVq9bW-_gDnzrDVgahHh4kIqrviQ5feFGmwNR2QYKiSyJx2jtXMun9rMKMEM4tSfvzbZZFAB6j_jagd-k-jtYbfIkF7bbkVUQZbD0s4IuRof4X0YAc8dNbIFqXFyDXDVbPa0Zc5lg3ne_VO63nnhKn49B-WeCEfk3cMIGReKQ2Kkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=ot9yDT5s6uHzNFy7HuqiNKoG3498c21QfYIRpWnbdI4Xz4eI6fvSjxpK7GntoxQdYllcQ6QNUkhBapUPyYJO1r1xMlhbBg2rjkTbR4AF6tyA-UGNX-ZeOp_U7n3ku5DVl9B9VAzEptO1aSPSu4bbQvQdVcL6IPcZ_zHoNhgwhRVq9bW-_gDnzrDVgahHh4kIqrviQ5feFGmwNR2QYKiSyJx2jtXMun9rMKMEM4tSfvzbZZFAB6j_jagd-k-jtYbfIkF7bbkVUQZbD0s4IuRof4X0YAc8dNbIFqXFyDXDVbPa0Zc5lg3ne_VO63nnhKn49B-WeCEfk3cMIGReKQ2Kkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lou__zhaBpNlVBPgp6ACeJ-QZk6vc5RYnahWiK_hqAR6Ljfm85Y6vilpvimpJf-t6UwotjgbiSChWDLQ2v2lCFxRfY8zjIX1vejxpO0ATKSOOYm3o3F2QVhsia743o-YJp3iM1PsPVZWVeu--xIrcJ-7f5-nngooSKZI-Ib7sM6bcDTybB2VRZkzijRenUc_SeBaGtuy3qH2DuCqXNLUgVcVgFkl3RYsJqHEM1hOsm9wz9lxETfeF_zzACuSCDzdP4xEovthzOWsFSQHLwbSnW9SpZ22slWd34tgJbq2MdycYEhzX4GLzc4o-yJgDArgsN5-Sh3dQdpkVCgI3DjXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4IVrooT1f1aDlUgTrZOznReB19w0cfScZnFvJSkLuSTBGGlm6ZYPHyICGqrKLghhi2NMJ19iVT3kXbMiOpN7OXf9u3CbWearDQZv7CPJf5MV1Lz1M0IEkKSiT6ENydt0iwg7QkXbAc-Y9_ixB_K_gplnS-_Pfs9kbZ_w5q-WGQa4PCFHBV18PsGN-Dl92-8Tb_5TBI4GgEF8G0XYCvVkxB9kyZcbjS2HvFwVVgaOme-G9mrSzpldQB8DZc8uybAWBniSPME4X5nrAcZBYwL--TSMqwCzXiBBFLyCw4rGHEkSqqzYrshI4gnEnWS8UnTPpgS1aYsYHP0iFZUjzsvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE5IXXh90LLz9kdM6whiFT_s3tbC6RMGlDg30TN8OFEJVyBr2BK4B7aEH6kpbur2twa5UN2Vv88xDGKtSXUs_gYr2CrUz78qncleY3kIAin2Uqbe_R3Dg89Fqp3BMsdi0V_NceSvFEHo1qcTHvX_wVO3Ocq0l2SZMVIuLu1poRPKwAD7p_4dXK6qfd3Bj4ZiIjQ0-M2uENrCvvGWOAr3FywwF7doXKRTsDGpuQfgAmYnKPVEQp5dAEhaMUNlF03Gf4ttiz-jKq13xzH_o3Y9yhBviD5DR0zcckfnSm-XzDQRWWQkHnH_BlieDNLpGoasqwchHzEGQJ4E_7UTGckPpWBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE5IXXh90LLz9kdM6whiFT_s3tbC6RMGlDg30TN8OFEJVyBr2BK4B7aEH6kpbur2twa5UN2Vv88xDGKtSXUs_gYr2CrUz78qncleY3kIAin2Uqbe_R3Dg89Fqp3BMsdi0V_NceSvFEHo1qcTHvX_wVO3Ocq0l2SZMVIuLu1poRPKwAD7p_4dXK6qfd3Bj4ZiIjQ0-M2uENrCvvGWOAr3FywwF7doXKRTsDGpuQfgAmYnKPVEQp5dAEhaMUNlF03Gf4ttiz-jKq13xzH_o3Y9yhBviD5DR0zcckfnSm-XzDQRWWQkHnH_BlieDNLpGoasqwchHzEGQJ4E_7UTGckPpWBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euuuQyDwcQX7zlxN53Dvn7nqbqJvQrsdheug2rI_K0imWh2WYee9cS8sBuQ5yiTYMJn0ReI44wM-TspzUkHSuX2jhDZvetxb-6BaddVesVA_VlnKXTZi_pcrz-e_ECe6m99M3LWPrNwotDZKCswLRAIEhSqiV_gP6OQeDhF9jwdDEEX8j9X9UKUdmIAHrBJw7bz2iK1eHN23JbVYujJ-v3Dzxf7T-prCCrODp_VrfeqzaaOykbaF5iOo9x85_1qiQjv7Km8qK9sBkkwjYrNltQSqD7wC0_tgKOG__oPiyvP28Z1QZzJMJUU4gNnj9rvldz_u0eFUSM-KeZ8M-XWltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lR-_mXngr3SxskxKd18u0xKy4oa0lmmAIausG8d0yZ2VmgcVrwGaJdkzB69-WXzjI4wWRZwR8qPvqCXH8IBQ2TqOKCsruVuR1TEVhSzI8bgpN-2nIGW5-oGYi7XByeKLEbUt-8WhecmDp2cqEovg1ItuUio47WSx-5BUVJ7g1W5hIrYCT5QXOflyiG9gd7Zo_Wu44mI7bSrFGNHhx9RrQ4GigFpHa8DIq9W_y-SmO1xzZryNRLiMystGTemVmE_ykV4bpbv_VHsJpuyQfIkZ8e8z3W3qzmX7yrKww5fGoPGWJjlUI9ww8HjZGPyAeci6IS2Y4TpjBYy-AK21BbLZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bzys081Aqfq_Jy5od3YH0z0FzhA-WNAUn-47u5rAp4WfA2_Zqb2JvQP4gQEhiuzDsErYyGN1aPN4A1aRT49mNrwpCAzo5q7NTTN6xEYfAJoQv4bzYKFwm8YblTRLK9t-yN645TV4tgkQsJ3GDUPJMNTwAm2EeJlLKzN8809bI2qKHkBNcYg0fOTfoI-8ukvCEC3xpiE-2SWxJdEFeVsf1VtQQYQeFaRBOxhpTzbxDYfD8XWB16okAOdIBfRwVgoI-bYRDfgl8bdjs1lYjtEIdMfr_P7yDt8hz0QymII6IMB0toeTEBcV5eTiF0fGxst-Fj5kdZ4szRsu6tseKKFMsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Mb4JZksCo-9wRixBnJ6VJURPHh-OVL20_o53ekGmZnYhBwXyIEDYVP3NptgH7Kbb8Jid8ddFI4IZkZEIYH8zITklV-aBx1odZ5I25OKPHbFs3zWvK9Bu-Dysxp8O-VdsPN38rAvKcEuj0fo1ZXEVUdibs9Z13xFmxirMM5B0Lcs7Znfyfq-g2TTQ5nnntfxiEgLfqSJ0374qhCKx9Ts2-9I9UihwNNQddOvAIA5NX1KaoibEGgIAMMvbFhprA9hq_YmvALrnuUa1QCmAVbvCwcgrdariJIPHRiQjQzgCW3_jMvZR4pVd9kJw6gL_4ZfANERSYVxzZbZzJunNq9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syonq7zymS4ehoMgebP_3xusXEc4h0Q93vgIV7hd-tS_a1vK-VaGMqyw1NTmRpV1WTWwDurclWTGz7hZMRGx7tlGVtyVaIw1efBr6m2TlnoMKSRcuq8zpkKvHvuGQBmCKEmdwAYhHUSJA3V2ij_q59ooBnnmM0NOlTDrU7x_nQNa_Pwbz4KVxPdf1e-oTmJHK1-K29lQJyP0RSFYF8h_AtzxRLbsRb573T_NpS8enhgBidVgLlSmxZEMmDcPgjlzbIwrRwqf81Kbt7MDawIUiA5h0B9CAHlLEfS74lyxz-j1zpFlRIRwVummJIvm2avpuAqxs2kVkfqJOJog54knGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaRS39G5h3S1AvA867v5gCWGJurjInEqw93YyQbhd7kU2FE4K4pHvLSMSslsZBSNIrW18q-PsNDFB0wa2vzGyPeV7-t3Y2MLK1keiNncX3AnqLCtTH1BYSVDyUerjmlAiRTXSnhrzMZDvHqtY3RE3iXfPg5jkCfYu1e-30Eqsr_zSJa3edtFGCC9pkLPaFW_eNHpcRbf9WdLshs62nvmfvMluschPTjwuUE_mWeg9BQMJE4SYapS4wJXQ2uUKOoHgJGfhkSK1LBrNqvpU0waySN8v_7EvU6LxDkAd5tce-b4r-3AkqD0RLtXMY3-v0HUJSmidfHb15CO0XJT6-wA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbfaW6H7YWLHWeZQBNZsVo3WteF_IU_0ByEztxNSG5wc0Wc7OgKeo3m4hCB8cFKkC4Lnfyxl6EzqKj3n5VoBlRNlugEAF1JV4rxXppI8vrpXfSJqHSP1GexgHbOpWZNq6gTPDEwc7Vh29dqdTJyON1se24QC6zoK3c72OZl-Bv33ffAOIxMj34MhnGuDRbC_IN2g2_2gjhlXiBp10u_hWvEd2EAvovlmuixsaSa1HPPhqgwHdTHUJZtcZJu33nJ_4smcK4_b-rHIqmkwZeuSHgVzLJ-QAeJuw7-OmhB1z48hJEjSjObEaAYKAxMoVmmmjvC9zqdOs1uCTZnOW0dmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa7mX2bITL6Nd3C3J-DCS5vHs691eQAQ3qlWE7NPtROfQZ1XIm3MIABuXqMdnuRV-mxrHmZSM-tGjGvPss9jlAZz6FsyISqxS4rhzabHgxJz204t7i3pCLTkvL8XX0h7FrF3412P3F7_T2291sGG0wOzP2JkXzhldzebk3fT_jERpkMrcZYKRNuornGEWhZMUz8g15lrNhbPZv49GjczK0eQ-dDKuWAZdFQ9p80K3Pl9rrYMbJxctX0oiJHt8dGZJuZMBlm1CIGEUDfNav6RR_UrUoRnZHNzwN_Ta2Q93eXLdh83b--oELZNX8cE5EC-eERhavGvIFzH9c6_LPD17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDprcrPkt13CcdzsfOEcctL-dAkFVGleVqWsxQc7IbxJ7IyierK6LWgLe6J0EaNrgUFcDoQyFHlpL9w_nA7yxMIRI3OaxTB1Mb9LDaMkB1vhE83twCo-ge6vURj7h3RlOtTcgucGpwJWZQNDc9Nfh5Qf5iX90oAFINE1c7AhhvmpbCUuudeUaegVyNozDjBnzterj3vlRx-i3oiytk_BUAZYxIl-lTYo7FEuUw3B4qZ72skKerJtXf05PRd_uANa2aFUVX4J9Zj3166a99CLGAOEGoefyP2ZYy41OzF4mBMuVKPcassKAik0_dkybEx3eXuMKvuYbedMr_ic9Qjg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwSXe4L7NIVwcyb4x4-oof2ct5T2cglbSE4BIm0U2rZ8zbMsMrotd_JjdgaN2Jec5PDqE_Dsd5-f-LGBJiEAtGSfgj1outZOjhgW19akhcJBw1LVXGBifm9QGvvx1Dt0CxLOkONhkAGXlx5yHw3mqtdMs9AWcik2f3X9IstSFdZXQFDjWRCsH71DKKp1KLRJD4-6gFHzADVXulXlgkRECOVwhJxNaRH8WLj93aHJMbWz1D2-1ojC--jWjzJKrB5ujaIB3zKgq2DmU145R9Q3hYeCGA9IlbRlNZk-zcJTPkACoj9obiZ3pngNb26FehTppnoIBWYKRTeUP3O94QBzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_G0dJt6PHz3pNmsOY6mHQyKjsEGIF_i9in__j3PpJ0WiZfNb3m0NrgZ7JVXv4eCi1hr_VjqufHyhOAgVlFALi1DCmirS0k_q2j9Kq_XpHwttH2Bq76Frs6Rh65dI4U6yrYC7mn57029rTbLduZ1R05AGVT_M1YjhOgiV6JwFY4Ma-r_ceL1bHV0zoMhUG9UzdPnwCfXpLdIdIHQ0GBDky4ZMWWJq7DHqCA9eNWlhdWgwlrwCTkd1WJr2lDEsn1Fs9CPITxpi5NpSBf-h3OVac4uGtrVtYm1WJs9pW6_lOk1WV_6GfgHVE2IpUVvLmIxe-81PHzITbnkERxrSpmzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyO7Y98tLjDP48s_qGd61MTty7eCF5rFhi5hQo0aTVh2CmV1q0BwvaMibkiQ7flyn2UWHl6zKCa9WjBsYQdbNlH8CaWypts2WMtXGwAJykOXJ_UHq4tZvT8-bH5da-VWv9vIOsRcIAxODXX-lEO2yWqP92ycHoJpmZyv5AxB8XWebg9rDyqgrCtGCGllPGlGckEFOtAdpM3XYIO-OBI3XRdEN8XkGHGgZwGixEAGHVyaXCVrHOLlKSiU2t-1qGql2vozdUyb9G2pmQxfH5hYBYASaiL36d9hi5EHeg8t_TyVrh90YitlDMJA6hTMqyhXDeVwa0IcE8Q6PAB6dMBtyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUlg2jk1xuvWkBe_GzdXjd0YVfhSkOVf9Mg4QFwQHMscTO7222z11KMu_3LuOC_my-dV-Cy42C8yw6D3maTCk0k0Pt-7wFG_rMer39xDeXx5b-_uEFtX1aWfItMkRbq9NJZO2rQqq6MArihDGySN1sLYcN9nj3yCuPurhF1TCR4GtU1RyCUswmNd_wa9tZfji4sLOR1TVHNuE94KWfOd1Y6azKMPxrlrIYJ6jZDrSUgXwbUvQYLZbHQJ1x2VP4JXjoAG4qu95b3SfQVUzJ22mhJRVLLtaaawK5zH33xRXAUVQLQl3NcfAkVFUIGgNUpHEwImBef1PIF3ktEm9OXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlLtgN1mWu1E17iFKdT3Hp60T_g7g1FPwPRRA7jDivHkowAMr2SJBAFiSpuWNsFcq8lG0dYbuP_Bn_L8NOvsAdRbvHlKIJS680JsenpOcKlAXBFVhu3o2i0m9VHGPEwSzIfKZa5vzXGYxpGc-uSeoonB0bWT6YSyhLwQyQn7__HIOSS0z9rFYA6GYBZBV92HOx2pBAh2Tzj2aTHDwUA_Xsxs-OANlCFlUEb0wgdsG2iSKuNCsul2IGmNhX0x8x8csPJWyr1kFSzst9BzMisWcN0YC8GBzyKwfIg85OfLWOKIY0kAxpQZeM2SwiLQeYojDJmuvqeMtWALp99xFF1-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23699" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gc7_O53pU1HNlwKDlmhdLQYZhQkQl6mBiuq8GYIwUGi1uyD0MIGykEhIMlKgVdtASrN8gS9z2-M_wjU0Evq31Cgq6r6w1Igj3FjpocmkK_IZFJS3dE-cqM7FplCWkkCaNlHor-DSoNdv6tC7ZDuyZ5iwvlE2gYwOjsqtfHRqielvUU3dUTf55Jkpe1hiWJOyr6Ebtu5adp3uHChEJj_qt5epbxIQteo-7VQ3h0qIwKcfXS2ZPtebGJbjy_uO0gGtkqMNeXFm-juzvl-_RfT6kcQewZPA5K9TG1CT4v-FLITRARxrktEHAswKZoiBmSLbAGOV4AbRiw-EdZO6mW9D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiRga2NFLR3n3s4jwgASyUUrXYMDNtb5pD8NYcH7TVFINmPiqbVOQcSZNAgWjF1L888HYnN7_nNvkrCSuaZ0PRUMisUxUH3dcPUXYsj3RCHa2ezPzXHKLr526T2zjVx3M296S2dAg777KC056ygBHP0ccDY6DSeAEjf8aXFYu1Um85y-nO7LpXa_PX1uG7ooll_LhXQoLzYB28Y6FsAMbQ24-YpTcQeZOwqkyN90uRLnKef25jSXR6AG-lVStSB43hWwcRTICWNGGhh7GIFuZBMCBMaeVHHwUdYLzY_Xjsj6tz3EmbVBW9AgAPDKVpASp9UXSIAsOJSIDhSqgyuH5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7cgx146aSqW5CGX8K2yFfIh7ljXVX5WVd72hwAB_Z_hGVCZVMc4zdR7qdcbS5VkPTeFpODVgZKYtmKPfscpMM1gmQLUOmNtPOIbaKV_o9p0ixFtNHu-nLhy8UI8-LgxWZvk1wqcMkxlw7-1YUZowWLQztjYNa_nAb3c9JKHcnMDeJHMfZP7wJ-UYy4x2xtx0ii7Us46UMvpBmV7PSAd_ascPogzNQFpMb2PCEXNzw8K4cKk83D3k867w3AMmg4ITqlCOuPX-orRc_FKyWjrthSTxRSBD_txP3-FJcRhCV8wJfnn7Ss3XKuHVc85XHU7VB3PPiBaZziDIZw0_YHFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kikyCmlcmApVOiizq0S9jn8kOS6Zo9mo4YKQcLIr-Qf0aPkkwnAhycMYl7-5Zt8_p4em-fRFhfWGJnhihKKT-Jrc0R8qGoFwbtMyeSoqu5kcvNnXMFNgLf3BDo_PZGGZacEh5qcEuKQUMzQZyYtV29BMHljgaJySMyDwD4ZtI2Bed4MhCY0clHNyZ6roJ3FNzs3oOMUs9dMYmTOfnwmFVa2FNDS45IG1bqij6wJ0MSYehL5028jl1prRhzo7SDKJMjcB5y8cK1rZiMS8SvU2cGPifr2OGtkOY5O0nryHvYxLuSyI8rNICCgdD_36uslmX2Dj_pgrbjUWTSoPi3oUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbdehGEIj9a86zUqw2VP_-WoBjx0QBkjX3Z5RTW4AozgjRuSEzuS-547mi4WdtLFO5EeysWEuPq7gzTOls6OIO7g7aobODwm19OPgqx5eLCdK09CQT8g3oIinfnYEdNHbudmYiZNB5noE7xb5NgA3DtZotcmtv1FlZ_-wftDjG3ts_d007hnv4WPKsLLooio3qkorZGJsPxXckYME7YYkvkoW_DmCPFIZNfCKN43aEuqv4qv34KLcLs1rchbOFVNeL_ECrAvTdLMsjRStPAby8RNyq_MJrPpvqkCEJ3L4sZbZtoxSIFg8U7gN7gMnso7_Y07MHHX-xHxsIr48ZmSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLJAeEFSfXHcu5n82pHrwFu4aOdrrUjPbxzChGS-BkrAtQlwUv8p7fswfuksRO2T__EH304TL19hw_i3vGla-Xe0Lkyq5XR14wCs6j_IXkJCRqq-HWgJxXMG5B7oe3jnbJH3--24P1Gk2fKGpwaW20urYGzG-trBuy_u_Z9o_TWsYVQiAPAwG8DZDxAzz3WMTbJGX3Nv-QeRSSAQKO2-kpqmldNCdI-8hKAg0GFC0ZyuXiPoMbfsBlyWbyEyxf8keT6WMRfveRf2u-xCLhz6IUmxkvWMd1IQ6MXbiuV3fTPQ8aHaOB6kQGXn7JP4--2-_wC1SuXaAkt-rAF35mAt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=kOzU7dN1FRI6SeQliO3ZXMUCmJ_nAOLyNM0U-5cpz6B4z0BpSgxnmriGdP0HVCocke3OMcGQOsNfRYFeQJNK6GpBUuTSO2yYGTQShKqAZcbmBVrXBdtedl-cbcfgDUqUsDzRPnka4fdgst8B1s8mzwS_m_ShIOemkerOUTovnIuCa0z-NbcvnncUMRBQntG4R97uNMeFLMYm6kI1906HEOy6WewZq_lo-OSH3gXbgjEugJJHzu5unTrd2ZnpZTNOitJyimPnBO5JN7TThCG83Q4emhO-9pF44934kN6T32LbJmgLodcyv1MEaWoJgHUHyWl2HXrE7MhBkssofj2KtbhmW-SFwHbaBEatehtSP5lhwZsq_qulUUW77sl_4Ivo0NJo_LFDZMRcOrcmJmXFJtl4oLOgzpmszY0io4Jx0VjxkuzKcuQpPheBKk234F1hOPggmhPx23Ro4AF6gRFPLfnYVN-0aRwG4ZunhFktkZDmverS9G03ldYackeT9ormF5X7cgTp2iMValr4Tg7RDOo38tdlIhu-4j1lwqqlLH4UFq7TAd05gqcAwvhHBeGvg_qHUQ5t2-Y2egZDXJI40oYHNIoNi5Rs_HjBoeiqLjE-2MCE24GfB_QTM2xO593CqKmYL5LRzAD-P4RvToi4J9jgshlJPlto48XH4nKUysU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=kOzU7dN1FRI6SeQliO3ZXMUCmJ_nAOLyNM0U-5cpz6B4z0BpSgxnmriGdP0HVCocke3OMcGQOsNfRYFeQJNK6GpBUuTSO2yYGTQShKqAZcbmBVrXBdtedl-cbcfgDUqUsDzRPnka4fdgst8B1s8mzwS_m_ShIOemkerOUTovnIuCa0z-NbcvnncUMRBQntG4R97uNMeFLMYm6kI1906HEOy6WewZq_lo-OSH3gXbgjEugJJHzu5unTrd2ZnpZTNOitJyimPnBO5JN7TThCG83Q4emhO-9pF44934kN6T32LbJmgLodcyv1MEaWoJgHUHyWl2HXrE7MhBkssofj2KtbhmW-SFwHbaBEatehtSP5lhwZsq_qulUUW77sl_4Ivo0NJo_LFDZMRcOrcmJmXFJtl4oLOgzpmszY0io4Jx0VjxkuzKcuQpPheBKk234F1hOPggmhPx23Ro4AF6gRFPLfnYVN-0aRwG4ZunhFktkZDmverS9G03ldYackeT9ormF5X7cgTp2iMValr4Tg7RDOo38tdlIhu-4j1lwqqlLH4UFq7TAd05gqcAwvhHBeGvg_qHUQ5t2-Y2egZDXJI40oYHNIoNi5Rs_HjBoeiqLjE-2MCE24GfB_QTM2xO593CqKmYL5LRzAD-P4RvToi4J9jgshlJPlto48XH4nKUysU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYjBA6p5B5lmoLReS883mp-Jk62f_Ec6pLSX85DHwAkZdrQWpsWpAJ-XoSsu3nYOxoq6ugXCqNyUnZ8Q49CSeZwZkrJJkgeVtj6ayYOcT5vJ_cpBUJXO8OfRJ7H_lvgb7Q47zaT-s_aBpV8z1eGwnAp1hqIY7wb3oA8VtktRHjqODzU_rAF4Gj35MuobnQM58RkcVZXMbRQdsaOuzN2P5MT-ywUue98Fb0dK0pFh08k8gRryexMcmHb6AoYxIzM9W9seXyahf_0vV3d7m2yKDoa7guQ4znMfdwrWHO3c-bZZuGhPtqzuq1lEtqCSY-3ILGPteux8OhmLMZRwXbuCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLzzeM2w3lUo3cAo6F3qTGr428EqwCMOxqjMdulWAQfBeTW2NcUmfXM_B7IaTB2CN-AvBtjzIrj7P7mk1Q6-4zTz9iNHRK-V-7rjPfe4nuJnmzgnfD0QqEFecEvXZ9FFw9E4DUOguJ7roLYcZ0xDrj5AJRoWtdzQjZV3-26CyAXAi_maUBnLfOPARcO6e9aRd740CNqZH7EKuklEip6aXP5yxSqpFX2Qk4YlicrllX4qBTdAVpjlBq1N70Ya9qVmK6ShdRd5OUcgLo5NrKZpGDgnSQJV4x7j18I6mYBUqfMVkks7t5FFwHDlKY4H8nuzhleyxkEQlhQydWJWrc-lXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnrMEfwRyA9cVNvERH_76Cfo6jkVnGtUrVZVGC91Z9364_996P-SPm9GOUPmFUzXN4ifKpCDgHJkzFRTcSKCReDLiOkqkY9MCm2Dz3gUigErfa__yjFQnJwzjjLXjieJM_7v8LUkpVd_wwSPixWKCecn24clqpWia53eXBJ0YOb5XNEtaOl0e5mR4wn4KzALjd-9itwGALEI9XjK1uemah382iPJ8Ib6NdfC5jUtIzFQysht-qbcu4xdRIiUci2S3gaIupfe3dzS0R07gO4GtxoSyNSliTFAipK_UtGnkNXeLOFxPSFHTRFWHKc9241uHTWXyRIWt-Gs06ytcCNK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=fTri5ExyIB-vX6lPKmKL3x0QxepJ7AxJGrKiYeOrK01NBshaQmPumyurQTPsiH4rdJ392oXVTTPC0JC-E14JiWQgAhoFv91ZWo8TM59KmHrLEbc_OwMYhedR3aXFuehZDItDzjQNN7utuf_llzJj8gPpPk8yIKu-zPgRK5GOQrIeb8MndBQ0nU4ar3pDEeqDbGeeKJ-biZ_iLQiBPLozqML29DMLfqNjJjqNrWBpunIUg5aZ9yBTK4MblU4bxibVMi5_iBMEA7aEVClWVZzB5_-H_d5CvjBZReccO_yp3vhYUenUM_cuh9qQ6HDX8atF0qZvvi4NdA1ZA-E0lELVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=fTri5ExyIB-vX6lPKmKL3x0QxepJ7AxJGrKiYeOrK01NBshaQmPumyurQTPsiH4rdJ392oXVTTPC0JC-E14JiWQgAhoFv91ZWo8TM59KmHrLEbc_OwMYhedR3aXFuehZDItDzjQNN7utuf_llzJj8gPpPk8yIKu-zPgRK5GOQrIeb8MndBQ0nU4ar3pDEeqDbGeeKJ-biZ_iLQiBPLozqML29DMLfqNjJjqNrWBpunIUg5aZ9yBTK4MblU4bxibVMi5_iBMEA7aEVClWVZzB5_-H_d5CvjBZReccO_yp3vhYUenUM_cuh9qQ6HDX8atF0qZvvi4NdA1ZA-E0lELVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWODw5-a8yr1c6HfEQwsA6ZAZiWK4L8tbZ_mvGWVxf7V-H57K0RzeEMWnRwx4AbiLs-vw8RYe5T5e6GyVArjN4UTAYG0xVxohLajJFucbvfTdkKsjEIcov7I7uBhCA6kVRV40f36kb8J0BiOLcxngxnLzFdoznT5McfO6IxFZIf7BgNQKt0spCclse6MXRO-AXpkntO7I7xOrSGPJjCTlbdjVQSYoWQox6-te3CKFGUZzuvYRgrK5vods8dcxXrW_GNGwpwZCL7A57-2R4U32P6aVarwitmh6kDu3gl2voKtCdN4Ah8f0LcWlPS9FC_4lAldaXMJ3WMpqOTZkpfdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=SrUlXBRLjkSBM2eo9uDu9GwtJfk_QlF5aHKXbqfSoa0U-lZzTcDB5bvqWm65laypP8BlVKy5uRC8N61bYQ_RxRagp3lLrJ5aAliZO94Q3rk09PKHewFlVK3S7_p_V0OSpXrpknLwq2KM1-NXDY87w5gUcFFxW7iVNnYWddT6tfyzfa1-XapZ6OSEw8ok6_lvqW11Zk5QuTohwdc_3p_-72XCEF1ZqXAYNuoaigHAQr-XYNjouVuWDJEK-ZqqBZ3pIAq9E3-H2weLaBjZ_woRbyWCNgW2EDQ8uN7lKLHBkJCMJx0zvHEE8budSClqJJVOPng-UKZ8iuJrIZXxHm0oFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=SrUlXBRLjkSBM2eo9uDu9GwtJfk_QlF5aHKXbqfSoa0U-lZzTcDB5bvqWm65laypP8BlVKy5uRC8N61bYQ_RxRagp3lLrJ5aAliZO94Q3rk09PKHewFlVK3S7_p_V0OSpXrpknLwq2KM1-NXDY87w5gUcFFxW7iVNnYWddT6tfyzfa1-XapZ6OSEw8ok6_lvqW11Zk5QuTohwdc_3p_-72XCEF1ZqXAYNuoaigHAQr-XYNjouVuWDJEK-ZqqBZ3pIAq9E3-H2weLaBjZ_woRbyWCNgW2EDQ8uN7lKLHBkJCMJx0zvHEE8budSClqJJVOPng-UKZ8iuJrIZXxHm0oFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=iI7XZ2PTzJf1n5pSJtUTROmy0GyPrh8DvZQAPaf4q4HSDanrHvSKwzVetpTLEznPx6NPspcWNv3ofhZIY8T-1BPsTGwWcqzWUbwrsSCdBeTqvJoKVNvIQ6yEHE5-yh2yqboGiyWTpQ_e5c-uFRX1Buc8Y5Pfj4QHqzW5m874Kp4aweAlN3YC5P8LAVyBKPwwZrkqOBpfwCcGhxb1qMP80lSvvK_lBFIO0Q8-EBi4mo5kutJen-2iS3f49TCreji7bztwnWtPTY93EdyZWfIR_Ovkfb9gcK9eZtT8GIXGAq7V7rcVKVPr3xnnHslaj7QwAVM5t70Ckebk73ypQJwPXarVBuM4_PnWDCCM0ZKyh07Omt4tR9geXDm61iihWMADdaO15P5srLY6Lem2UW7k_X9YsTIPpOlMOdQyrS1-8SmcWR4A90SU8prkzU6DOyYSfJz5WkSr5qSOiLVVGQWhFJLx9T9JAlj5NU8Vkp7QdaLfKfYB45too1fBkpuMtqGwhT1hoEN5d0sEjE8QnlcF4hVqqW_S5M-qB20UJBja4zwcudWLOfdrkJKe19RhaGsOIpcbi-oGvhSlxctn_MVNqBZTzJlbe2bnmR-DaRHrVjlnQ5xnm3VTgDhC2tmZViVaO1Kh_W4H3qURoEzCV8IL173GBR58_BWj8-bway7zA2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=iI7XZ2PTzJf1n5pSJtUTROmy0GyPrh8DvZQAPaf4q4HSDanrHvSKwzVetpTLEznPx6NPspcWNv3ofhZIY8T-1BPsTGwWcqzWUbwrsSCdBeTqvJoKVNvIQ6yEHE5-yh2yqboGiyWTpQ_e5c-uFRX1Buc8Y5Pfj4QHqzW5m874Kp4aweAlN3YC5P8LAVyBKPwwZrkqOBpfwCcGhxb1qMP80lSvvK_lBFIO0Q8-EBi4mo5kutJen-2iS3f49TCreji7bztwnWtPTY93EdyZWfIR_Ovkfb9gcK9eZtT8GIXGAq7V7rcVKVPr3xnnHslaj7QwAVM5t70Ckebk73ypQJwPXarVBuM4_PnWDCCM0ZKyh07Omt4tR9geXDm61iihWMADdaO15P5srLY6Lem2UW7k_X9YsTIPpOlMOdQyrS1-8SmcWR4A90SU8prkzU6DOyYSfJz5WkSr5qSOiLVVGQWhFJLx9T9JAlj5NU8Vkp7QdaLfKfYB45too1fBkpuMtqGwhT1hoEN5d0sEjE8QnlcF4hVqqW_S5M-qB20UJBja4zwcudWLOfdrkJKe19RhaGsOIpcbi-oGvhSlxctn_MVNqBZTzJlbe2bnmR-DaRHrVjlnQ5xnm3VTgDhC2tmZViVaO1Kh_W4H3qURoEzCV8IL173GBR58_BWj8-bway7zA2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vvC6MaXBQEsM923EGlHQnG95JHnxWDZN_qoxXKyPACsJoz9v5LX1upTzO-OgN0em6L-yE-P38E0LW414ppY-FEt9YPcWp-7-JD0VhI49fmm0XAaPaygx_Fh-6ontf6d_5fxN1zRKyDpTZkB5QhvT5cISOHKqnmjY-8r2zF2kbMjmZ0vEQBrLpEeUW4ZgfH4Tn8IqMLOP5fyEkEgmIGIhdfwWEl0ocjazJvErtM1cPcqnBI-01dR5TF5m4CBDiuom9BYDfBULyyKxhynKyhD3hHIdm6PzL4z6Zi74dmHxgYJTVTJyGY-ySJS9RWDoVaINKPWWWpumoELk8F0qz8-R0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vvC6MaXBQEsM923EGlHQnG95JHnxWDZN_qoxXKyPACsJoz9v5LX1upTzO-OgN0em6L-yE-P38E0LW414ppY-FEt9YPcWp-7-JD0VhI49fmm0XAaPaygx_Fh-6ontf6d_5fxN1zRKyDpTZkB5QhvT5cISOHKqnmjY-8r2zF2kbMjmZ0vEQBrLpEeUW4ZgfH4Tn8IqMLOP5fyEkEgmIGIhdfwWEl0ocjazJvErtM1cPcqnBI-01dR5TF5m4CBDiuom9BYDfBULyyKxhynKyhD3hHIdm6PzL4z6Zi74dmHxgYJTVTJyGY-ySJS9RWDoVaINKPWWWpumoELk8F0qz8-R0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Voz4aBbQXDgjeH4NA4IJ6aM_49KkfzzREG9jVzCgIkToZUrbzTrRZRsC7BqXdnzNKPy34NBq2oUvOTCWwbl3iUVdgC9vjfuhjypgl16Jhn2JDIVHsDUDhfKYntvy44jINIPgsSpZO45-CcvpfmwddBoS6aIyXFR5GukimmQTO9o8k4iHTVKflECVvYoQlKD88SYRyiDswYg5XsiP6tCpDzvETv0fEUy5oYIa2AumQwZl5ZVS6gYWpIZJsqiHtKc_7qsMjas5dm7Mh-YBdjiT66kIEaoKJRE0Is2S98pw0vgi6gJRADQ6R_DJOZL6ZiQWDFN6xFxSf3GsC8rKByhHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrcexn35bLD4IxT9KZJv5ri5pLy5m3b80X3bLvOYZ_V5WssKCvQNpG68Dzo29bA2jrKt5i53AFJtTpiAYzZ_GFxMYJQ9xPGE9PeDUTbFyR-uCEAfmXhRiloBDI9dmTSN3pShxz0CcHMRqZmhDFSwRy7J0nkGSO2QL6oILZa-yjB7F_fAv-_LZyjoMawXNGfj5X-DJaK5nfwacvLoEV3BgpLMEtICq1FB1SQCptXIMTMiiNm2RejFhbO_it5fEAuxTKo9x5eRxdgJrRE4SzWoSAb-H47vHdysf-2AEPPQy5oFmVy2K3ppF0Y0Rk06JxQSbjE32nRMGDSswnfRaxHcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdBNRZfHWae0d300VKix1kXlCGQgadTGwCHl39yLO_a2wY0kR_BaFCVpIz-YHpnVdL7AkeSep4__60QepgXhCmalEMUoluqmKMrvpo1lapujbka9Z9HeVCJI7NTXVeKFIGsZrHCkq4cV5rhQWyNG0n3Cr1AvG8u0_8Nk2Jh1KrqbW6b_flElRUDQBeGhI9rzCyKAbCit_bOTN7znFBx6J5jEBWQ6_PnnrJbSHEZCz-zK6MxEf9iaZuyhpXrmVZfXgGsh_KDFex7LjOnYFbjy5aOV4nqp6EG89OBZ-zRB1e_XRM8zfgdU11DeWq-JJOAS2uKeSfU938QlF0CQq_0P9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrZ5N24UG6rd86V7cK9j2wR-hRON4b4cOW2VBiip9gmNz6uvvxXYbYTlcTAhj41IoFOsghnIRAW23zqu0ky6VHTp4MT86cu_1Q1X6PTEqgZLWNurObQQQiBvFcoVfq40yzlEB70_R328pATjBbugHEI1gDVXSF1de-jGA3hf14T0P1g1gJ3NWVmpQzd1n2chnQ3FbkyuZoiXn124pRXNw7RgM_eTNSoJZllyUOdpJTVhKQ6S_bA-BVihoF4BRpJFOEzjWQNcFAZp06Kwv5JFwYjwTLIdZAG9fo2bMmm6u1kGuQjlFTOPebv4bRNVEfv-kap5C1zWwJPaFbttwmDK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy2dDR62gODXxEJixGZxVyVjnlkDTY4Ks1jvsPUwc8oOQaHH1vyTyUGQxSq08_TknTXa_dStvq_h_fz7IM0hksGbPC2bSvFg7pKQY1dWF7xNlJPaZSvQXs8F_BVPgGBReARXkTAo4z8Ka_MUK_4WsJyVDBfHVLnuZJ4W6xe3mQpvE2Ov0Eq9_oycc3O6SdoMzhwgzh2zbUnCB8C7shfsJ_pZFzH1r26FNM89bQ6Vh7ImUngSfHtfYQqZYDCq1rDVHo6USeZBhC2WX4ZdZzB-HXxSlILEThC7oeRCgR6Odtt3Qk4u1SlvtzfJ1v_cIr730A_ZVvzExoW8qdJEQdRueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK6am3OX09ylRbqnt_7V3mE146s_nhUC7fvu00IsCS0G5l52KUTKEJsw5XOPzC6b_eq_jW5eqm33Mp8upp9mpxFs84jrt7LI1F0-U8Vhb02omTZJgQ_qx228Sm16Gt2fdUGANW8hpH4eENn5d3AHj0psLqPX3CgplNrXt6g_SANMt4-1Ed7fvmm54N0RumgLxxIlKflKxhe-VpoV6jiEw0pVuz9efBrpJPxnqHZnIACPNLTSLnpgxM7NHcb-4-TnuHZTwDpCPM3tGVptTx6xPM_W5fx-LTG4AhK_65oJt5ygw9qmdiCguy2EZ544Dq7gmo8uYURJ0bCF5iYo4H3NIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=S0wJ1GxkR8uMSsQu9G-8rVdD2MvVn3Wc_d8fXzEcke4FOWgGcpmoLI6GYwLE_O_JBuiO4mBmFx6HOGfFnjAE9E3q4yW7gh5Tbu58dNMMIuvA5237igqp591_CybbJyqKwY7MyA2LIQ8Keay9Y-O45JkWYR-HobjKHq_r-e9JJ0ugndqJpREhySQb-nsySfRdriOOyefpjWLoxr5yTfe9zpLGtuaYkWnUYASoS87LlVmPXs7CNXHYLwQADRJKIM6z6f5nNI0ESae3tf5StA8MELBqUILeiGmFa1J9YyLt16AEZxihjRfIBKqXSHz1Nw5L-uW3v9aJ3kL8R_yCEFtb0mQs979EEvIyl4Xh5S74o1H7We96_g9Rg9hdBQCt8FkwZsKPY__-_lnfQybbmNXNFa4TfcfSismdEmuJtyNqw66lywmZSoJ8YIiO21TVZPrIzoF5bcD1WuN4Eq5Qb9SDohnyGKrZIkvVFobeJJ4d74cyZIE5es9R8oVWJbF34JFmCy_RLAS131dxZ5wV-mNmrN645L1TJ5y-Mu-dC7WeXHBp54SMbCQAFrIo21nbSejQuZOh4CdQRNeJ0JylipUgCjc-wNcaqTa-PtDFvtIkMAm1VK1sdgkaxk_tdE3Up08YDmh0NnRnYOpm4D1N5eM04PceBvp8eUcLGe52S1YgyK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=S0wJ1GxkR8uMSsQu9G-8rVdD2MvVn3Wc_d8fXzEcke4FOWgGcpmoLI6GYwLE_O_JBuiO4mBmFx6HOGfFnjAE9E3q4yW7gh5Tbu58dNMMIuvA5237igqp591_CybbJyqKwY7MyA2LIQ8Keay9Y-O45JkWYR-HobjKHq_r-e9JJ0ugndqJpREhySQb-nsySfRdriOOyefpjWLoxr5yTfe9zpLGtuaYkWnUYASoS87LlVmPXs7CNXHYLwQADRJKIM6z6f5nNI0ESae3tf5StA8MELBqUILeiGmFa1J9YyLt16AEZxihjRfIBKqXSHz1Nw5L-uW3v9aJ3kL8R_yCEFtb0mQs979EEvIyl4Xh5S74o1H7We96_g9Rg9hdBQCt8FkwZsKPY__-_lnfQybbmNXNFa4TfcfSismdEmuJtyNqw66lywmZSoJ8YIiO21TVZPrIzoF5bcD1WuN4Eq5Qb9SDohnyGKrZIkvVFobeJJ4d74cyZIE5es9R8oVWJbF34JFmCy_RLAS131dxZ5wV-mNmrN645L1TJ5y-Mu-dC7WeXHBp54SMbCQAFrIo21nbSejQuZOh4CdQRNeJ0JylipUgCjc-wNcaqTa-PtDFvtIkMAm1VK1sdgkaxk_tdE3Up08YDmh0NnRnYOpm4D1N5eM04PceBvp8eUcLGe52S1YgyK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQYnG65yFSlWhFwk44E-IRN0-Q62SEdbsYHBVffD0_Y--H8BL2NhI_wTWcudgmLWJvA2_SqarRFLfzmeXqdH1JLKmd9nqqdh6Vypb0o675ErD3TIjsdTXYvE3EM2bqN1q2OQFpUm1f42e02_KobXvllKjc_y5ZBjoQjTYJMiK2Qf66Wm-oO2D5i-xLguUA9V8neEbBE3zKOLnkyRoiFoFSB4t_R5k3Wl4wfiqbxYy9uJNEzKDNGqaZDz9uRV8XYyGDl5oLhj1LSZhOBRVUlWdQV3qUTzB4sSL2B0uHKq_BiWttDV47LWfXuNfPwVNUPtyeHW2qbFqi1pyxqrAcQhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rudstKZFhWGLXogTArKPxEcSXzvEn92yBJ4u2D34fLV7dMEdpDAe8T-zCcWUEetqlB7dwGWtdHxmf6ZD78BDsL43SMVgz5tjiw6Q_PCAmIhi1EIeYKRy9GujzUYR6aVr9pVmQh3J53da2BVZaPoymNmeZTO_aea2Kv8VJHjrL4cWgLJlu64uioKs9mTuX4VuNllGeuzOm5JYCI9rZ4SDkCdQ5kRhfTjejOlyOOAjfyTyY2PGTTQSA3F7SjjTpBaYcBM7cozDUBtdJn75gcqmEo_PrPVyqABpe9BsvFJXxPPWWLVPEDFaGjgDbq8SsD9sXbTsMPunHklPvrBX9tqo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkBRYdw-kttbQCNPB9Dt76Y0UhNMet66fKX_7NsRDDzLJH6KOUvQwYkJy5x2MsxGAVJ8myXiMUghGJwIyFbUvQaeTbfdR7o6JlRx3BCtetCatqhQW6UeI2rK-0_TG8-7f818C-yceao2XWMSgAaa4ttvFL2HgoQyfeTpAGJhkm4mKU0mjdg07yn4WDxrUCjkRCrKCYraBkLg5Jks6T675_NfsxOlgMffmi8xujb11lvSbFuc9ArzJqwaLYYrxkZYf98AurGO0-zCqxHHMRHI8TCZm7i4jvDbdJLTYO0jiK0hK3w_3KxOiFv1vfq0pDwDi_GN9mbbTTjvyFYJt8ojQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLaSQdX097OtwOB_xOmHhwA-bvP8lkZc49xve7_CAZKNebjnqDKR8quzygZvulQfrC59ymsZDWTQIdMqoMwpYrT9lxpvkEXWmOKoLDgVNBqezO8IQs8jdd-CRj6IGZ8DEMCqfDfi_dCTL3SiUcNActM9WLvqLMaScfj4NcyDoN9tNoA_IgDunTdfXSQQfPP26MScJmeKl9cqwvUjAGhii4iA0N-a2_ey34r4h0gH3hycBCATvYbUuEyDOkh29fvwfneAuhH72VkOyGV9xA-7w8dkaMCk6dj1KdSmZ6Tmeabwocc67QVx_fCMKwICLyQY8aTW97IEkz3vfpORqTvm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aes7WTnHT1QZslqGLM1C2ui8ZNTTL1l0J8fJ2PqK7UbyTdBtY9sSKwgGrhH3-stPAs58Cp-wbCjMC1N0fJ_COo2e8zh2LrVSf8F4ka18VWbADrZQ74e5RC8TkViSw23ECjcLyhiN5yjpKOR-D2uRHaCHbz_S9YST9NTSyM8D3vYhcbk3x4Rjx5ql9eZ5F4BcMV2HjCClGBb-gwjbg8Zvo_fBAXBt7uTgKex1ULHoFBy1i76Dc7eraSFtrmeDk93of2_HASjMOqumIs9rj6CU_Lm3RCtv1ZJTm8YeEtJlLbK4kYrmeV5G1aPbOMM7mrPnBSAVVrPIMCj-EuGTjE1QvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8pLm5Syd4pxHuIO_1oSP04UQ5zR8r8JztZWyGiee2TG1g78lUSlgDy3TZH2CpwrzLrA2F5SHdGl5GUFnDp0gQRU8X4Hrew71PTvNcxBRo9cftc4vvKkQenYm_00zlj7L2R0hDgdldJjCZTs5Wyzy56oR0CcHdWUHw7RvuAMH1Mb1cQeP97kBqWJ7lKxrO3KcdZfFd2Kt8Y9VSOlpiZq69e_3QEARsRucLZ0DOELLyjvb6bq2mvzBLCqFXDTyRf9mLm8p_tPtHkf6VbU7k-JKOyF4hvxl_bfKWC8OEfQgBoZbJS_5KmyO0f7JLN0qeoHi5-UaPutSSmD789k1z3Qfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB2k025FaqBemiVR4pOQ94j3uWRpxY7Q2DJ6yKmQsb5bJ1f7gzRz-63qVEbTySuB2clSoJCU-SJp2SGdr4-29JjgA9it-4pZDOZTU7be0qOyIuS_1CcKRXksxZtxvmx7MaORT0hTZOh-hEZO-8SDnYgW3pS_YR9UWvWHwjRN00rfWYfUdie8Nio2nOCQqVuA2HEcHzhV8VWU9ldW5--kPyv23Xj1TaGruZ4BKlsdQ7eNYI_hdWfNyjkaLt6KG1LqfRvnIn1jFVNlFFEa9XgEOdVGF_ZHnHgnLP1Vb7lo-SIODFYSwRJXXKmlHdoFbm0Kl2M_W6mFCPrCwz2qMGiINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwJ3F3z3foWMGZIC4-Ql5I4rq9l5M1aNM1KNE0WRLfRyeIYNf_TWQCjoK-KtMeNq4XtrZZm9xtRojoEpwFHdB_HXQtFw_jQzL_umOynegw_sLivHLYyU4EnL9l0hddDrj2L9EERRxorDvD9IZ7JBLXjk1EtdLqorRie0k41F36-f4HnRtFj4qs7TPM7Q-rTA_QMY3Eu5SMcecKRWL9Il4ks65Tej2v_Jz-Nf9ycozLLrRaBYLzhtIBltk58NqeD6xCYG52LUnK6fpSu2iURfKPiZFF3cyWpjYxj0q-ttzBCOm9I25PB7Ju5xrAq9eb6skvmHhqg1YT5NdyLd5GZXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GftGKJPhFR1QnrdGbwS7PCGxTYNHpnEds81EfToHUdi4vIqFoe0heQJGIhFn08kPkGcMdflYVuop72ysSHA_IztqpgeBCVNRVVA9mfmLtOtB28rMe5eG7Fk3Un7ayqqcYjjsfErv_w30GenCkmrZgMymwDMsTrMLeCkbBp8eVUziT9V4A4b8vctFHNuyiEMRNF7EOoIz6ifA5pHfOOKLi--cgDCa0qvAYtPfT7NtEo7vK_d4bDdhjrsyYNwiMLZdIlQfWxCrQyYO54xTsenM1nCOFPp-gHkCRav9FVAGJvGw0EwH02tJlEe7u0dT9mWRgE2RGljcb1D90jrdOLLubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxpxTmhGP2DFnzMNxOQZIYR2BZdiIk2RlDns3qrN4BQoLGKwB8W-CMbMYKJExeigmEqwe_hcejW6Mr7BskucR06Q-5yc5-fRFSTt8vkAZyI-MbRem9xuUB2OlT9qRQZ7HnmEf97tDNaIjCafXBRs1g3g4gyVE6LoIxaR78NLhKeeZ7wAVNbAqCJxET0y7pd57yNyW6ZtvxfjeMSNG7iscxQgIC4DRnVHkOqwfvFZaQsZnPF1aN6OWoqomV2O3ibGDKVRzmNLzqzLmWBKPUu-gyKAnDbrR1h0_MfPvLucYU-Ww6yO2mLe80CGMxDKSn-NJeVOBV-R3b4a6PCSOgC87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOt2xYrug5EagQ0vOrbbEZBscmY5YgiP9-gn5oTN5S5QkPYTyff1q-4Bzpo_UJi0Myt2gXZvGx_YlAVf0FqArd4GtZ7Ezkiqpliy7SDFxjsopH66scxIIa-LQuxC0kLUYYF1p65bWqf0tqQbXqiXtpCauAtQKs3NCqc3oqSd-DqMLOx1rq2ofJEcn1ZQiNFgupBYjRkfp3oFg7bTtBmoUITw53d2KmjSCDQ_eouUEUs1bJayWMAGid1rllKXvECmDvh_h3MNFtdQL_cxz0lbuu-NVtUWq1iJaYTn8kXyxYjsUg8WVzce8ipcm8Vt61T-5VOnavAVM5ofyjCH_oa5_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkZVKpMlaAY6q42-FpkwF6mKib2N6YdwLGWqJAauORXtYQncnLouGfA3zvdAYRhXBvNUoLu4zCQVWUN0K-bL5t5_7A-B41AxNLHQmHe0ePXEpolPJEXYW3vArlrnHKJhBhc6zqmQLYR_K7GpfS8PfRDLlwWNCMOCy7BPsgQQaysmbgjf4VB_0os8FwH_AQ2-wW_jhlBRa44Vpdpy8koKU0Qg8UAUCozWe3IO-es8AO2J-7BWenzITaom1UR54HIGcGTSrDOxDjIx_uYJxf6VLQWrVEh2ziYV9t_XUhMdMi9D4b7cbXmCpD1SbLyX67UAd18v4jGZfrqVUXQOuiKfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ealq4qE-Y_cFOmWOAqvUWB-szKFjwlOWBt6yx9TJlQr7a0ELtydWzT_DG-_HHdgztBexS5Zer4_t7H552n2uvAhM-eSlb7S_JqCLJZ-pvZzYDPFdsSY32fFOR7ARaXsKXQPmKCQ1hnyljwe977r62fc5EJrmvi2XpIHE6KOXCl1Sb44Fw0b7LlEssKOQFwgPcE6gbJNyKt7FdaUesg7WhFd9uoF3fsqJDTTnHVvRt7yZL1g89Go1hF2AL6uJy_Hu-RuN6jOK-dc2CykZzfgRp7Ly1VetO9IMw5W9sh2tkZwK7M9tCK783GRIX6rvh_6cMlpZLrcDa2zQqG-tj-JFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6QPC_kfLYh4tEloLLRYrAQMkz7iMZTcj0q8ZDyWOp1aAIGBE2TEgi-_9uIT95t8dZSE5qYi9yMBIHSEJqO8se25xkFA134ecKJOEQ7PZf8ltehlKG0i01duda4l5eXVyG86NG2v0Cv_hunboUiO_kJ2cEjBf3QkPYC7FFKe4p7UmF93uhHu9b1i0ZENNqDQAKiba7gOrkGNuX9Zad7RWexwBCc2lkJIh-9aSyJ5DlnZKxveq9dA5W2GPBFNdT3zbrX_g5Lar9ReQx3r5WH8wzXhuhq1xf_HPaWXrUkvmZ78kZTu5z6RDJc0tSRvY6OXYZos08bjfZGhmKPS1Lm8Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=d6N2xlccNuHBR1g1h_kpXJNKYx1JSDcWDsMIKIvEbP0mZ7uDUljcBWh3g5VdpjQNQej9o0gfFN2WA-IoQ-FcLTa3xgVJhLzLbuRC-nZbwnvu8_QmcOoDUGjfv_iKdxdBir75z8BjKCw3XahzajmbkG4Bqii30VU1RGFT9oTPIEDndCWrOIvvm6SZP4DXBF8x69myVwbAIZduo7t3kV6bSDZO2aeHgZl2lSY_cY3z-FUohzJo5Yj2DOzqrXAAEUgeVPDRHmdgBUsGzpOBFBwloVWYCD-3eXn1pLq8h0Zicvjnxr9PAVBroZpJMCr54qAiVGe9gmopEtnN-vsJQBuIXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=d6N2xlccNuHBR1g1h_kpXJNKYx1JSDcWDsMIKIvEbP0mZ7uDUljcBWh3g5VdpjQNQej9o0gfFN2WA-IoQ-FcLTa3xgVJhLzLbuRC-nZbwnvu8_QmcOoDUGjfv_iKdxdBir75z8BjKCw3XahzajmbkG4Bqii30VU1RGFT9oTPIEDndCWrOIvvm6SZP4DXBF8x69myVwbAIZduo7t3kV6bSDZO2aeHgZl2lSY_cY3z-FUohzJo5Yj2DOzqrXAAEUgeVPDRHmdgBUsGzpOBFBwloVWYCD-3eXn1pLq8h0Zicvjnxr9PAVBroZpJMCr54qAiVGe9gmopEtnN-vsJQBuIXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMqRSUISPi2HwtGHkuppeuV5AlIn_Que_sK0gHWUwSTX10v1S2x8TlN-7DlDFcu-f3-0BulCtwKQFc8O4ldBxNeT-Kqq1WiOivYxT_aOYApC14SjQKPb4_4zH71jkV_lctiax0Ukr27FlDOWCJYFZDJqcQdduKw1aZWvUWH8M82M5JbtrGeWsKC3WivRjUWACQ1FlyybDqTMNtvPgG76xuhUrp7GID1sG2CT2ZkvG0PFlNLCSkKKsIaifAVxJhhi5P_L9PpPy33tbRJv9NLBT0j9tQoSSkU9x3GhHNrF2NIm1kK8T1Qf5exSFUvsdgg8w9zQUKrsWy39ZQZuCLwbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVbWff3PzSxtP956IfvAs_MaABSB0G8GDItcAEi6HuVHtDJ0JE5iwP_EJHLIUNlzP7Iulr7izfl-tNxRvfsXcQipgkaouV907n_gGK1omyOpMx1z-GTec3MBJ4axJ1zlMjYHQVnOInswKxhz48CBfVfiCw3_Dtb3DGYF8yi3N_P_4wYUaNeHwrYshjNWGHINvKJOlqwh8Mc8Asm9rAI0rwKuLAchdPuKcSVex6RXYNfwWRoiv3UT4XWQE0F1uNfeps0EXpgJKt8VQXb8kk-bnchQ7EjtqlG2I9pgAPW80yktAFpdHcKcLqNOUspCXUyE2Z7275G7jw2UH7OLZdrWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTFotZmQ1ysvAuMEAmEWYnMuPILbp1sLxPSwU5QsbsuHC-GgS2In9bMvVtgTbsKY2a8YOE50X9SCiWiJYniQ5sck0dZuFcOhT9hTfMy1nTuXEIWwbfgfFx9MUd6z_HdkWyG0u7TZYPgBoRd9L9e9pxl0p_myl-rXQXbJ8Mdf_nb57RqXu6Ppk1_pd0nECoj2Jv7zZAeQssgEmxksPgzLxbb3uaKPUaoGppB2gFLyIPqliYC5x8C2R2QfYCoATDM1qsS07shqBNpRI_xYCMjCOGCrYbhlZX1QB0I6A40r3tO97txNRUk0UABQ3q3mhjaSiYMmPUFn9HPUqUTsTAp5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚽️
خلاصه دیدار دیدنی‌وجذاب بامداد امروز دو تیم آرژانتین
🆚
الجزایر درهفته‌اول‌رقاب‌های جام جهانی برای دوستان‌گلی که این‌بازی فوفق‌العاده رو ندیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23655" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=M_j4K7jpEfodRWnZ67Q3WJmRSa_De89dRlBeM7fQRmpyIYsW6PXfOziWwo4XARJh5QLZZv8iVyj4_9AnnjjCuPutBZf-grwhqgtU_Lk26dPkEuG0lP49ODxxfOgqDjnq5VOgXV9lRT_sACmyacApXxUbHsUukNPOapvvx-uP3KceKpGHtMBSDe8FejiOHp5xMt2RfHzjFwaGsEUvzC31lMH_Z8PUGgJ-Q0AChcPLdpLQssWePrg-FXS4xbWJMxalZDS2gfSwJ5MVSDjhE5Rww_8t54W9r-BuXC9yG6pbBT_odoIeXlCCaFgH5addOfqtBwvTK1Y_onw1jVLRdiQ1QkFXJLfesWEAJln7cmHQs6h-8BDCqVyHuO0BAt4VEdMzJ0DHqnnAffe2aVsOt7u_w6sO9ZdOhnA69Tt3LkZdr7X6_POK03LaJsj-QFHHBKK-3jNyqwK2YjW7VzDIwvbExk3eFsfB6MDqajXSbbDwoPo6MyqzSLEx9kOT0b-es2DlkUNsT7pzl5tWxO-QRYdULtwCL2QBrJCLTAbH-GIy2qY8srdhjwP7-DAYfKFTXyqHJqJTkwTLNBJj-kW24gzXsbC1qkZBxw99_K_t3IbpVQtdclAb7nvK-DOl3Wd1uRUjpLN69AhQSjnVlScsGRx_5dcsCGvzdQvWiVNjJxFMSKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=M_j4K7jpEfodRWnZ67Q3WJmRSa_De89dRlBeM7fQRmpyIYsW6PXfOziWwo4XARJh5QLZZv8iVyj4_9AnnjjCuPutBZf-grwhqgtU_Lk26dPkEuG0lP49ODxxfOgqDjnq5VOgXV9lRT_sACmyacApXxUbHsUukNPOapvvx-uP3KceKpGHtMBSDe8FejiOHp5xMt2RfHzjFwaGsEUvzC31lMH_Z8PUGgJ-Q0AChcPLdpLQssWePrg-FXS4xbWJMxalZDS2gfSwJ5MVSDjhE5Rww_8t54W9r-BuXC9yG6pbBT_odoIeXlCCaFgH5addOfqtBwvTK1Y_onw1jVLRdiQ1QkFXJLfesWEAJln7cmHQs6h-8BDCqVyHuO0BAt4VEdMzJ0DHqnnAffe2aVsOt7u_w6sO9ZdOhnA69Tt3LkZdr7X6_POK03LaJsj-QFHHBKK-3jNyqwK2YjW7VzDIwvbExk3eFsfB6MDqajXSbbDwoPo6MyqzSLEx9kOT0b-es2DlkUNsT7pzl5tWxO-QRYdULtwCL2QBrJCLTAbH-GIy2qY8srdhjwP7-DAYfKFTXyqHJqJTkwTLNBJj-kW24gzXsbC1qkZBxw99_K_t3IbpVQtdclAb7nvK-DOl3Wd1uRUjpLN69AhQSjnVlScsGRx_5dcsCGvzdQvWiVNjJxFMSKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل فردوسی پور حین گزارش دو تیم فرانسه
🆚
سنگال‌درباره‌قضاوت علیرضا فغانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23654" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">▶️
قسمت‌‌‌ششم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23653" target="_blank">📅 09:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23652" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23651" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGMb-OWBApvuW02lsSuiy6SuXiapjRAGLoJbBfXLbiFsgN0hF9ECbqmQeku_fZzfIN5hZmI64AcU6orHswQ0fglHt44y8EHLXpB3A9iwy1mX_enxw4U7Ap6Cfvt3O5d1kI83PV8PMLote8BRCPmxzpbOjv4qc0ahWZb7bgrqFA5tcmRV9IL3U1tHKnEFJRJ7WArphvkFr2lqFOXW1LYnCdXVLOq-aL0s0QKkrQRC1gCOSKZVCuraNsCFoPd2SdjrBvxMnhZrJf9iCsZfGI36ruTzAh6DvYrCWWWha4A9TirjNglULG-7PXcSFD68zw-3WkfwdVSfqLOW9SmedHPSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3oB94qBk7uo5W4dG99sydu3nadDENfEXfs82zFwdPt99nHlE35tBUEKn0Ebq708P1QsQm1_oL_A4IrJZmfVEwZGq8L5jBn7RwdqR2wTmeDaBGx1EplRC9qfRDnWvgCVBe2sPapq1w4tiXfWq7YUiAftaK-1QVdq-9XHBn5KsVUUvHT70xnkYCxubjbSqR6zS6CDsjgVftpkDopIue5A4Gz-uDM5_IfrQFqg-65Nd9VbH8l0vlzuTF4p7suxHmqAVg6j3Qw94IUWyjie7ILy1Zy9xMLE0JJfucoXVO9PDE8gfFf6fqpp4zd0WWwVYqRQXYDk7vLZhmH-RugGnzWXag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23649" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJgbi-se1QMCeQXj-L4RkkREE04Z_GFyJaaeyRkRRtFrxFLS4u9XxBXoOzDDdo2lt1y-bSi4Q8tAe5sEPzPJ9DhCBTM4GyqitZFN3NAh_zVLvfHbFpqTPefkenMS5vv5XFy3Cjt6VpRggfSKUCleG7D_48xDxeIbAAGcscUnYSGvtNdgIWtVj2QrzndFYVrOle0WBiRj1Q8L-EZY_q6dq5mRFKn6co6ShGHHwV_7x6EH6F6K10rT3kWsrj5n3HLjkuwB6d5-SeU7N7Lat_TtYrgMCk5sjypX0x0mztywlR3K9y5kNSkn0zNTDneSJNYNbIROEGJS8yo8LUDJyOJHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23648" target="_blank">📅 08:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23647" target="_blank">📅 08:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPZsMFdce8dHAjE1u39M4J7ADwY7oveyUNckwfOrL6qPdj1qyxRVCeY1Ejjrdm-_aJfj47dwQTv05om8cGsAUTzANXjb-9Y2SV29-0S7HEFISAv6Q4qwGZSB1L8GrgG0bfg0JgvRtaNIvOknpDv1PHtdBx1VJwhrTo4X_yhqla4ZJpBqBfjamoy14SEaJuzKK8hEr1iMIeDA2SRnenvg2gReihdZMTyPx2Kvh6unk5VgNWGMRnOpzwpRVCaKPDD3fJxd6fTrn48X5a_6nyAO8I66quz-NfP6tBsJQXMENM6hO415VEHZeCgtrvCSyiiWtsG3LBlbQWqHWmHs8Ia9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx3Jg3pZyM0tF2iuTgpRMvCzp0-CQj9srRptQQpX5W0E6YsH_4coTxdTKTQUAMo7aaLKLg9t8odK7fA2Tn_8N6UJy54BSKzgJ7XYKR_LnSJinpMg-BZRbBWbKpPAND9oOWT4qcOq3sbFI7n9U7g-RR-BkGgVdZJqYtOpcvNZBQ52mBXZ1bNED0J8hxpP9nYzH64cB6b0FfxJishLjm7q8v_zV_wk5eYG3pTld_ecHm7rojSjG4-JUJB9no4Pq9XXYjRCfQU0g1_nCz1wGeG2DmRqGsh9JVSPiwTVDteJUFhr3ZUsuhkAjO5_quoAQ6aXx3DFq6Ef5ARUE33PpHhbzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23645" target="_blank">📅 08:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=cdRTOprgvCvA_mDX7O76fMWF94dfrhDxlqML6FzvJAIs4MseJewHw5kM1LvUtzgylW7KTZgQAPHjKswBEk51SqfJU4pgJv7paPIADim-OusKUCJEUkIgGTOd4j4ge1cGg52W9xtFFPkRiYY_u9G_vn7pistPwnynVr-zXbZecCzHbKTjXVK3jip-PRR8uyMEcC0IBLLdIq5HXHe6Azg6Nw_mhamO_J5mRcD0wh5lMNp9clR7KLxsPMb-0KvyH3YFGd_d8q-WNaT-vqkh15UrkHPZUjL40MW9Ck2voQebKihW4rOjU2Tmq7aBBkSHHKzC4L-oTrILGKkvK8-mZTh-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=cdRTOprgvCvA_mDX7O76fMWF94dfrhDxlqML6FzvJAIs4MseJewHw5kM1LvUtzgylW7KTZgQAPHjKswBEk51SqfJU4pgJv7paPIADim-OusKUCJEUkIgGTOd4j4ge1cGg52W9xtFFPkRiYY_u9G_vn7pistPwnynVr-zXbZecCzHbKTjXVK3jip-PRR8uyMEcC0IBLLdIq5HXHe6Azg6Nw_mhamO_J5mRcD0wh5lMNp9clR7KLxsPMb-0KvyH3YFGd_d8q-WNaT-vqkh15UrkHPZUjL40MW9Ck2voQebKihW4rOjU2Tmq7aBBkSHHKzC4L-oTrILGKkvK8-mZTh-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNnUpGD0Lrxa5eBsFwmSJA7LPMUq2Y7Mwt-37Tv2KATtO6xrP2qo5ewQeivD52jg4qHd06z-kuoUQPrI6vgoK45mYMrM2JPMgXXOKdxxDPhDJNLF57bdraWL0moEh8D1i3tm5AAhLA1WMJa-Xj1BwX3HO-rwuDKmsIpXONek_caicb39J8L-5BaclZgc0Gw7-jQTx82tCUvFf1JMJqYLmaviOExac4fcnWoYQB_ILrVLA7JVPCs6CUx1HJsE4-SgnpxqCCDXQhQSUwwzZ4Stb6thhfiuKKmRETVwvR4JJFAKVgd83mcdZfFQMv-ucCqGo0yUKVkBG4XBOB2tW7YUXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
#تکمیلی؛ درخصوص بازیکنان تمدید هم لازمه باردیگربگیم‌که‌باشگاه‌استقلال باایجنت علیرضا کوشکی و محمدحسین‌اسلامی برای‌تمدیدقرارداد این دو وینگر جوان‌ آبی‌ها به‌مدت 3 فصل به توافق کامل رسیده است. به احتمال فراوان در بین بقیه بازیکنان قرارداد روزبه چشمی نیز تمدید…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23643" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPUc90YHqYFte8ZXdsH0_dXE1Ermr4ZkZf8GWq-Fxv2pZafnv-kir4SX3FoiveCS5sC1tYsYdXnGpyqBjCA2Mque7cd1hGZ-rUENpCLalmM7Dia7OafeH-35wFByQuxajKUM6Jg1YWVksByS-l_wutE5jD8rHkH0BEEoERNCq6mHsWdnYrRD6Bv9QMAxySDrZsZGKQACwlLQNqmfGgOoRkH9Ipy2IN9pXIiAT73LaFelv-lO0_fc6tIXAVGTPfIPHu4cix7sLvF8qksX6CATSCYemRr1lIqhLKA-6wffgEwVwzSO8XbvtUbnZThQtQ8nLvIkBQuZzgmmNqWzlj5MFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23641" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSUKm-Z6QebaIB50ysX56HIqRNSia72IwF9QixZ0eOMzK1NL5Lqi1xU0O7Ur8OIKXqbK6yQ9NOjqWeOZfBE_oFnx5esoVQFHcwdtLLeE2RrJuLiEe9blSKfdsWWHufpEaRbiy5vQncCa887R6EcrBpsRko62NMDqaHTYHQlWglTK9-W-TU1hoqqKuBRZCo_OGh5eY-kAaXkp4B4JjCe9LI7TWpWGeTHdfIPbucop-ynwin51j07yyLkA9dmTRS7pnPkTV2Zoff8sqBgCaijpyb3i0Ievh7yEjj1QTz2PmgzwT5B3EqSAMrHzfeL-dl8JB_6nLX6NzboUN08hhobfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
استارت قدرتمند شاگردان دشان در جام جهانی با درخشش امباپه و اولیسه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23640" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4wF0CEfKsWqBMj_ID5oV3XHJwrbWmJRM8-WCkMJ8qna02-WXkwjpufSE1yYr2tyrWhvMPmREzeCdQh8IL29g_hAYo2WCPj-MxrYHgXeZMnP8wAumkIfqLRwS7HxNqXlpbCSud_hd1MEjuP_5NL8Vz6FAnlGs8aoP5iMrnEMoPQFBbiyalUWv1shSh-8eRwa9CPh5_lHWH5sOainkRgjVdWTJAMFvSDZ3_gk7c29CjN_YVv8USLuplro-sVeqEH8pvR6quw5uJdsoQBn2m65yLZtDRIEbYpRnE7zsABQDEwnJKZuWLZVMLMfjmSgHRjhb_SHwogeYPQqb_sTgY66Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2xYqvU59ZOQSyBZ69xG9cb5lfzSfpyWlYU3bCmbfN4BWHWu04XGvpbkRfxkDsnxeQNcWeh01r7l8KcxSuZ5wD6PJHT-v9BiKd4h2X3_ayfUskm8BXwuIxg-bc82P1y1sujbYBFV2O_58panJRjC53vtvO9Rd1DNdu7B1OBSHj_6h2x5PO0mHgQT4LLPy1GDT3wwYhOqhn-GGg3DZr-0TYHEXNPVCT0aUS_2p2FEeHH_Fqn6f6-psm37vvn5xLtX0v_SYnDBQKXTLwKO49L2QMiRCG9V3d2ZT7DxrHATanor7qGUbPbknbhTDZHkNYQkL0Fz0E4KmUgoGBBiwd5APA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikrDLEy_EkeEF9Cx23U3M8mIIVS1S44ZMXNIAbZE_rMvZisCpNzaWJFzhdKBcAVqhHroyLIhOHZLyL-R7niRnsG8H8jJhRsqYKochwwuhch5_t6_sul54BJjwiwk7grBOVyo5wWDDx-LtUkhTS2xrEPQq4-2-aivOeSE035KDogcylur9D2qWyhijnXElNSmIzLN_euGgZX0Ukx8WLBKSdPEQHuQSUJebeoDijJveabenK81QnZJ7K_U3B_iJEX2KqlD5XCQkA1ORqtkQz6tEacIC8TjtMDMwesnPap0XV1HXFcKQA0RE4Gnt1cQgHSl27XDKnV7zX6NriFefi1YYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAMKmtLbhkyr6h837v5UAa940E93ndfywNLexeccQ0vfzA6mGhU-vv8rsWXMabmGBLAltPk-BhJwprMsJ7EDZNYK20FRdrNP6h7yPWR74NdBrreIxjx-CAcFlx-rkgSMFkkNpuFMen3H5J-0_6RFesQRcGnu4Y26fSY4QAGILZhhhhmPUxvhczkijBOOlb6dBT5-M_6BN8fT5voFJH0GyydlycZVpgkTeUAzEP4s5VMsF-fldUM-UtgjWRIv1Y2wt7OXk8lpq1VE1tsfnP6_2Hukbeeii1bG5QH0fOoDNYlA3EIGjA3X_3B1veFMYNzu-CSOTF4S9vZsvBgrJUjN_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZFdPZAnhiks3rJ57HTpEDcj6pnWzIb4DctjlbO_QOFnhYyx4DpxJlYQwzEcIugPcvcGEkc3jsxsUbqCqDVJtK1uyZF2beAYVveSquqMooYgzs8_9rOLCnsDKRB5KqcNzlfwSVYPVzpbFvLY78Fac1nq1vgP8Pe5DJlUJrO0NFJOQpRg0_Cm999QR3fDUCEE6oPTqcCH-DhEgdl5c7M2t40ZmrARE5eguLRnI4N-dVILMOGxDkygn6cTl0B93NWw3RyZ1bCJGwsTuuZ4e8xZDOO4LCqnKYXVGru7-7Htd3X87xbg8lh-aa55UT6dV7G9phFNlhuDvEmZmcuQieHtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9nsZbMn_bnLBZELQzs6mV9lRMyspf4UDFU-HLaHTpJl00oKayEHl-E348qwPplAK_wG26Vx8It5chsirjgcQV4WgZa-be4gpqiqQ0brrNMFIU0muj9OpKLwC7113rfzQgcFA68NCkvaQsB3Y4JVawmVvgYW80ITblZ24w5h-LV-oGoDYKSlRXyJvBiW35gl4xFpyFrgG8nhG6OdLfnBWvipO1fGOU5055woc6GTpHu5PKQ4R036PKZsW9uoYy_Zr5_rchQJM5cDnp5YWTm20S7LFp3nANKZGH_jTAAdp3BhKz13eY0ufPucqt20XAEXSnnVdGgG5kzzHJT4Eq8NLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjfCzFvMUPBtZqeFxlyYS4V2yFOjlDRdmVs4jtcKup0Pt1NVtjQ15vCMOBYCJvRb-gffV8HrwklyID886vQEYN-6qzwB5aO6V8u5JYgliEDv46ud1IdoefG0MJZoEZ2ZlCW7a6jpzOpYfynIKVNrdNucl8bw-HaYMDmSKVWJ894ci5VnWkIY_ioIY2wZfa8jPRfGvkDHoU7KW_6cF5JFWEyZChokGZZdBhFcKAu_3TDiCpl3mJeAKHbxXSrICBBafBcdr0ZYQIAKKLaEV7xndIRBDXGo6Lw1vy_2R1QIJArBqaXMZ-gL_pa_MB93_kPG8kUKEU9R16iZuxBr0vWnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fmxs8BED4vY4ZEX9rIeQaiEvc2aBoVbXzBAyZ5mzEIHDiWcGpovuuRq5S7TYtpjQ8RhO3BSdU1AJJ4tCUmZckGpVhZFgtJgct4lTLfzzu2w5ItTYiL5vqNVFMVrbINgHTAOPm6itX-tFIB9Ti0jx-tKJj0FWWw9QHzQfiMwE8Hx8XOQEdc8SBdcEanqy9idwpTyfTnSbcE7zVGQCKyelqyAJeRfcPr4okJhRHYSOmnH336UglrZfC25RPVGp2vqB-KobU2ixGGOVdq5TPyO-ohcZp_GfabCGoROAcWleNrxBnoi04NaPSqM6jBcGczNn2bNO2Wv-NT76Mp3e9zpzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=cY6_-kpDHk3Uq24O0iRdE5iZSkFq0OFILjTwGe_MeHDucVFxujReofiLtQaagl1NH-AoCuX8Zr56s0b3NGOzVdxUcfmp-wGANi5TnVhCZ_LWmmGKtAb0NFCwtG1C4kg7r6KBHCUvn0QrRdoIQhshCUjjE1cR-kp1C22414ma_oVN4zncDopDQOYXakRfuGm5NpGHhrJDIoTHoYgJO8TzPw1RVJO5yN7HcjvZd2U5bFWKeF5CtAqlAZKI7C-7Mp5VuZcymqcTMvB5qkm12Y7EJRfJ1VZdtkOZRJyIkTPFlZ7M3LbbDyx8bpwkNtfBWQOEIa8n9HjpmdfVfPq9LIpqRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=cY6_-kpDHk3Uq24O0iRdE5iZSkFq0OFILjTwGe_MeHDucVFxujReofiLtQaagl1NH-AoCuX8Zr56s0b3NGOzVdxUcfmp-wGANi5TnVhCZ_LWmmGKtAb0NFCwtG1C4kg7r6KBHCUvn0QrRdoIQhshCUjjE1cR-kp1C22414ma_oVN4zncDopDQOYXakRfuGm5NpGHhrJDIoTHoYgJO8TzPw1RVJO5yN7HcjvZd2U5bFWKeF5CtAqlAZKI7C-7Mp5VuZcymqcTMvB5qkm12Y7EJRfJ1VZdtkOZRJyIkTPFlZ7M3LbbDyx8bpwkNtfBWQOEIa8n9HjpmdfVfPq9LIpqRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcme9RoUv-CxhAfkOySjYdzZlJqqb-4s10ZTimDcfeHB07PyfiXOkL1zAPmmX4nwVOmEBJAduaLBjaxLT9OrdVm5rW863cq-4aOwSI7vDHdlN4rC_n2Kl2zSXWAjSxuOVIb53F7XulzWKxE3y4YDqyH9-2mz_MlbB4K1creQIbdeUlKSQQF9O0BRbbnSlDsTBD4GsvL1ZmLRHXFBfikVmQiWuDMOBpeOe-QQxdY7vvUCpCVk1jAcBgeGQU1lOsLXeiC92Le93pBGxUCwHkK4bmpN-CtrrBn8nPy60C67zf9CSyvL-LsCOsCYn9pPQn3EuRk4Dmwm2v1npZIdH6aslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk0dHyph3yuHIgLhQzqmiRm8-EyQY43YWBDavkt5REjYogax4vzpgh1tRjwEbnkYJaRj1FbtVsWueMnr9j7EoidiaTjixS93NGlGbyfRhyjMspmyfIi2C-KmI9C2GHLPMMAN8Tp2QfHyhvhHN9evs1llC7ureaN6FDs9yoJeTGr0cJtz8yTq9uWYRkhkWSGf9JI3nG-2lUWFo4nx_JL-7EfQJozZqiSl1kOARWLS3uuPDng4ds7jSsg0cp-5ARYXRKxMlSdJymXi7pjCjIbINcgZAumpnyuNvTCNmfvBljoH6Ko9G_1rC5B-WFKv8fACp_fTLn5W1O-ikh60q20vbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocUzwuUoKXrSuzahIO94jZkxZhCFCzp-SjpHQsI9qaBZXqItjdMVW-350LhpLbX1bXbrnN4NRALIBCtadXif16B675RldQUiFw2YXg_Yt4l4vbyweepm4M9qtOBrEnvVgcvA-1DgN0JY9XLkLFVlSrc85oSAgHCMf4IQURF62koexSb1DIbjYv2W07C1UMnDtwdWneZWZGKvBzzE2vXj284fe_p0O4QU9z5dVmkBoT4k8hA8L8xAwmVmNS_YdrGCziWDCAoV7op2CCdm2JMZCPqEeKQ9f7fnbsfLMID1XR-7-dMUi_IeS2hSRr_zM1TKzU40D8swV_et50-EZGxIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
