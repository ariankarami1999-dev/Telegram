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
<img src="https://cdn4.telesco.pe/file/i58JyhUHqgRorKnq0hR06cOP1HlmhmLaf1WZgc_51rUt6ljGSwVDzKAWqDWXz3CmN_twpNIg40yDOQ3PfU_oLn1NT19fjS90MX0wixWFjXJBdTwKp3Tcj2nFW-BwMpVyjJM0U6h6ibjY_R_69D8hm8-7PLJbUrtxn-38GppcDuXDw3z80DSYHthuwmnXRsUvUFeo9X2Xsr2SrEyyntcJwbAjStyQ2owav118SMUaWHup9yOTqCcuNje-xscnlAuUHgdThPnTDMHlHdgrR26YW8w2bDo3cg3OyxOXq1tz3BgxBUkyj4fuYFhT7RtCDnzD3F8HXV1al-5_bzT0Yoo58Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-665236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرپرست وزارت دفاع: توان موشکی و پهپادی ایران غیرقابل‌مذاکره است.
🔹
معاون شهردار تهران: طرح ترافیک در روزهای ۱۳، ۱۴ و ۱۵ تیر لغو می‌شود.
🔹
سازمان هواپیمایی کشور: قیمت بلیت پروازهای اربعین هنوز نهایی نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/665236" target="_blank">📅 12:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f151079d27.mp4?token=Z47rbIiRxvn4dhtPx3yUq_iYrBmX0Kk5Tmdrd7rqBexNZevITmj772WgdI9MzjYZsYaGuIFVP--oPYSbR3_oCUaVtJBNWZf5HTcOb3ZH1A9t9i3bVx8ifrjqUGdJLdi_ruuIjI7EQb_rZhFCDekrBTn6vphsF83Lni0rWTuPxh9ByvNHamSSCZZqmO5XI2YMGyK6OFttOLjzp7NQenr5i_B1s7ipoWAZHN4aWGhchuyjEykZjsT6jYZ7kBpzyScGcRPL5_vN5GDvPkCbBHmo0O2NUPhZrCj1diaC2YWiyWYM-E_xO5Kh_UX4K-99g5ayyvidG2GHu57IN2CZSBCauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f151079d27.mp4?token=Z47rbIiRxvn4dhtPx3yUq_iYrBmX0Kk5Tmdrd7rqBexNZevITmj772WgdI9MzjYZsYaGuIFVP--oPYSbR3_oCUaVtJBNWZf5HTcOb3ZH1A9t9i3bVx8ifrjqUGdJLdi_ruuIjI7EQb_rZhFCDekrBTn6vphsF83Lni0rWTuPxh9ByvNHamSSCZZqmO5XI2YMGyK6OFttOLjzp7NQenr5i_B1s7ipoWAZHN4aWGhchuyjEykZjsT6jYZ7kBpzyScGcRPL5_vN5GDvPkCbBHmo0O2NUPhZrCj1diaC2YWiyWYM-E_xO5Kh_UX4K-99g5ayyvidG2GHu57IN2CZSBCauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی حرم حضرت معصومه (س) برای آخرین حضور رهبر شهید انقلاب در شهر قم
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/665235" target="_blank">📅 12:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d45a19551.mp4?token=soGIj4xZh1dVYVhqsazTbGkvRG8kCuXfIJ7dJMcya0JLAsPyCWY_ETZDG-n4PTI39StOvnBk7QuHrucXQ7DJf2l2r87wzJPkpsSfBZxdomOB6ovSIDKQBIdSl4Krlv2C8d_Kh2TnGxSaFtXTOwmWmOI2fbylJ9-fDKECgA6Kep1YU3jPUQ_UCsl3HbuYM3wxsxndPM_QVPL2HCgmAcIeHUKfV_sJONSRFN_n6SxpMmWQAeUy5kcKhmUfEQZ4qSh6hB7xAFnftjA1Z0xCzDI-G2nEhggPPsuz0xz_RzHbLimOsbqVBtC3GbpkL4oMySQ20lN2-JfGMnf9ZKtqQxQcJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d45a19551.mp4?token=soGIj4xZh1dVYVhqsazTbGkvRG8kCuXfIJ7dJMcya0JLAsPyCWY_ETZDG-n4PTI39StOvnBk7QuHrucXQ7DJf2l2r87wzJPkpsSfBZxdomOB6ovSIDKQBIdSl4Krlv2C8d_Kh2TnGxSaFtXTOwmWmOI2fbylJ9-fDKECgA6Kep1YU3jPUQ_UCsl3HbuYM3wxsxndPM_QVPL2HCgmAcIeHUKfV_sJONSRFN_n6SxpMmWQAeUy5kcKhmUfEQZ4qSh6hB7xAFnftjA1Z0xCzDI-G2nEhggPPsuz0xz_RzHbLimOsbqVBtC3GbpkL4oMySQ20lN2-JfGMnf9ZKtqQxQcJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
نسل جدید رنگ‌های دیواری در راه است، تحول صنعت ساختمان‌سازی با رنگ‌های فانتا کروم
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/665234" target="_blank">📅 11:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pApYr7vitQWiEg3-bfA38a2NwIBB90br_FhXkAPe8eRgWZ6O4OdVpv8_ryWjqzkSU8BIA6Z3N_FtgppgZYgt-Rnn4157wyC4EWcHIddhirSycX7EIKmJCOX0rxJrjmHgMHXVer5N5uIBoon6C5qdf3ZiPeu8OeRA2Lfu52UqeEp_qLw6YlIH7shwBverbBYmjMFauOyC7SnEqvL-qsrn4AMAGpCaJ4xk1DTBfVdif2r5HlCMaNtYWR1zROcPXeNFXhnyt7WMoqQUI03BVt326mSSwD0RjvYqd6RmzPBZ-nDBtg4U1ZyP6W5UvkQEpboNUqNSEGnsryaKSuxt-pn55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: پرونده انتقام خون‌پاک خامنه‌ای کبیر و شهدای مظلوم ایران باز است وآمرین و عاملین این جنایت به سزایشان خواهند رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/665233" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoZ-7_ZinXu72irNtReeRRRvSJvCmOnWIgJNMA9LAR3V--lVs_rOliHkXEuEUlP-iXWNPSJSpxZPAURtEdf8MYEitsTg5jhbHnd4FxdsHjI82aFJWyaFDxhoyMQBBBVipiPHb4j1YV6-r3nTWzGhwdq5ZZKzBBQksi_5agD_UMrXuBeJqVoyASzPld0RorwlRQ_9ugxRFy1o9HocF2IwAyrbKxcOKCAkW8RbfrDDmZIOVAiV7nZs6_K-Sh5NCDBqjhSxS4LNOZyAFdX9k8X2nHirdtXGiIL-EvbJBSRRGw3esCM-c7CaFsbOhCuJaOMOzZSkAJo7p96PdD6Z1GLWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران در دو هفته ۴۰ میلیون بشکه نفت فروخت
سی‌ان‌بی‌سی:
🔹
ایران از زمان لغو محاصره دریایی توسط آمریکا در دو هفته پیش، بیش از ۴۰ میلیون بشکه نفت خام صادر کرده است. تهران اکنون نفت را با ۲۰ درصد حق بیمه می‌فروشد.
🔹
ایران موافقت کرده که به کشتی‌ها اجازه دهد به مدت ۶۰ روز بدون عوارض از تنگه هرمز عبور کنند، اما اعلام کرد که کنترل اداره این آبراه را حفظ خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/665232" target="_blank">📅 11:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
قاسمیان: واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/665231" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv3xldZlyXJluv0aC7m9xk3Qu4GykcN_Wen_Torer2uLg8pOSumI5RTHiMllL2sgtq2vy5d4VPEh4uRpG9-3WCk84FYde8vg05btrJNoVFTX1yOl1TTjbc8wW21cicUjIK2htlGGR9nxrXHdFzM28PmXw6yE1m06SnK7KW_exd5zxdI8xOnX9ZTPm0IRAF5Nhkrs2GRgMGcJMHEClxUAYDUrm7rfUz-iXQNykS35u6FAGEei7Ys1267fKn89r2s66uXRqUXHI0ri2kBzxnTOIeM69pobNykVuwEHHP8rp_CPAnSIOl3jS1U023SzvynCvGLiPhQtEhfEr7lh92_Xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت بهشتی کوهستان گرین نهاوند در تابستان
#ایران_زیبا
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/665230" target="_blank">📅 11:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
اختصاص قطارهای شهری و حومه‌ای برای مراسم تشییع رهبر شهید
مدیرعامل راه‌آهن:
🔹
قطارهای عادی و فوق‌العاده در مسیرهای تهران، قم و مشهد برای مراسم تشییع و عزاداری رهبر شهید ایران اختصاص یافته‌اند.
🔹
قطارهای فوق‌العاده به مقصد تهران، در روزهای دوشنبه و سه‌شنبه قطارهای فوق‌العاده به مقصد قم و در روزهای سه‌شنبه و چهارشنبه قطارهای فوق‌العاده به مقصد مشهد اعزام خواهند شد.
🔹
همچنین برای بازگشت مسافران نیز از روزهای پنجشنبه، جمعه، شنبه و یکشنبه قطارهای فوق‌العاده در نظر گرفته شده است.
🔹
فروش اینترنتی ظرفیت باقی‌مانده قطارها از ساعت ۱۴ امروز آغاز می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/665229" target="_blank">📅 11:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF_9pw5OBEazomwlAbNdNsK9BmwBXYqJ04-skh_RJnppabA1iDn0-s8L1Gsdm6NvESfR6v3K3NEFRMlAb1BfYIpFsl98jkogydYn9qgMtWHwqrYQGE28Wl7mc4NT7yaPhl7gK3xG0rwQ2h6cdVFVtBKK5Kwako7QTVIYcCv6OPfyx2KXVBLhUJFPGTUgjAvzJbLQe1VYBjLfs6C_1D4fwKbDRTqAcSLQNoP0ZSrSTUaoehKFnvQ6tjGCVePrez0Kvv4GD5FYXYt-1-mWl7-bREyZ7IFiirnmTlJ2XfK9UZLpsrWAGOqnWL1rfCjU2aVeBVHYvxdf7RooPYIUVgkKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا پایان سال خودرو چقدر گران‌تر می‌شود؟ پیش‌بینی بازار خودرو تا پایان سال
بر اساس یک سناریوی تحلیلی مبتنی بر شرایط فعلی اقتصاد ایران، روند تورم، وضعیت نقدینگی، کسری بودجه، رشد هزینه‌های تولید و چشم‌انداز بازار خودرو، احتمال وقوع سناریوهای زیر تا پایان سال ۱۴۰۵ برآورد می‌شود:
🔹
افزایش ۱۵ تا ۲۵ درصدی قیمت خودرو: ۱۰٪ احتمال
🔹
افزایش ۴۰ تا ۶۰ درصدی: ۵۵٪ احتمال
🔹
افزایش ۶۰ تا ۹۰ درصدی: ۲۵٪ احتمال
🔹
افزایش بیش از ۹۰ درصدی: ۱۰٪ احتمال
این اعداد چه می‌گویند؟
🔹
حدود ۹۰ درصد احتمال وجود دارد که قیمت خودرو تا پایان سال بیش از ۴۰ درصد نسبت به امروز افزایش پیدا کند.
🔹
محتمل‌ترین سناریو، رشد حدود ۴۰ تا ۶۰ درصدی قیمت‌هاست؛ یعنی اگر این سناریو محقق شود، قیمت خودروهای بازار در اسفندماه می‌تواند به طور متوسط حدود ۵۰ درصد بالاتر از امروز باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665228" target="_blank">📅 11:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
🔹
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌‌کشی و با پارچه پوشیده شده است.
🔹
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ از این‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد. احتمال دارد پیکر مطهر رهبر شهید در رواق دارالمرحمه یا یکی از رواق‌‌های حرم مطهر رضوی آرام گیرد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/665227" target="_blank">📅 11:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6483a8f64e.mp4?token=vt9kITRHg3GfnqV8X0pA06qrs8n8D6wV9uzxKhONGg5y0qfoGvQ52fUbtArImsctaX1uHdsGPZw6ZkFYOPrZQB2-Auc_OCQwwbKTU579WQEWKXjCB_MBvhAVtqp9i0X2_kW2Egr-iPXKmZHWI2QjBoAm2niJCoZWbGaWIYKWj7gLleOnFtj5GPUaaFbHQczS7Y8jM8OIhUsc8Hf1gpiFZ7L0yJmOX1rB3owFZnNXG3q8avs5UIbQWHIi4Avt-W7JHefa_74klVjA_FrJtEM-z5DqlZ8mtN1Ea9P9yfP2nNzFk3ya6E6r56mo6DR7fx_WYH3PvK4KSD0MgSCKRXWpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6483a8f64e.mp4?token=vt9kITRHg3GfnqV8X0pA06qrs8n8D6wV9uzxKhONGg5y0qfoGvQ52fUbtArImsctaX1uHdsGPZw6ZkFYOPrZQB2-Auc_OCQwwbKTU579WQEWKXjCB_MBvhAVtqp9i0X2_kW2Egr-iPXKmZHWI2QjBoAm2niJCoZWbGaWIYKWj7gLleOnFtj5GPUaaFbHQczS7Y8jM8OIhUsc8Hf1gpiFZ7L0yJmOX1rB3owFZnNXG3q8avs5UIbQWHIi4Avt-W7JHefa_74klVjA_FrJtEM-z5DqlZ8mtN1Ea9P9yfP2nNzFk3ya6E6r56mo6DR7fx_WYH3PvK4KSD0MgSCKRXWpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی سفیر آمریکا در اسرائیل: بدون یهودیان، آمریکا هرگز شکل نمی‌گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665226" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏆
پیروزی کوبنده فرانسه برابر سوئد با درخشش زوج طلایی کیلیان - اولیسه
🇫🇷
3️⃣
🏆
0️⃣
🇸🇪
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/665225" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید   رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/665224" target="_blank">📅 11:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8b453312.mp4?token=J3o7tOJMAwPW_CQhT79DmrYKmSRJjnNwtx7uHS_7c0M9qGETcnzpaiPVFPnDWDXEFnYQJhrtymjSbAZJgC5gzY8yPi5_7Rds7CpU6enbyJ8mE3Uqz13H9NkyD2Bhlkk364-BL7ePbNFRGI-5I4wIuZDxBOxqsqMMVWxaECOlpy0PoClp3nuhovvEtM4NoaVTKsjObPQYFl42BmT16dpmXFxU-TQ6AshoG2MPAxbnF_FNySCoBYQiY4ELs32zj5IrV78SeeV2htVBw_lDd60Bx722RKgal94V5B4FOqxQrU96rOmsPkBIeCQwr8iXSqxWeuph-jgpsBBulzFATLOqRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8b453312.mp4?token=J3o7tOJMAwPW_CQhT79DmrYKmSRJjnNwtx7uHS_7c0M9qGETcnzpaiPVFPnDWDXEFnYQJhrtymjSbAZJgC5gzY8yPi5_7Rds7CpU6enbyJ8mE3Uqz13H9NkyD2Bhlkk364-BL7ePbNFRGI-5I4wIuZDxBOxqsqMMVWxaECOlpy0PoClp3nuhovvEtM4NoaVTKsjObPQYFl42BmT16dpmXFxU-TQ6AshoG2MPAxbnF_FNySCoBYQiY4ELs32zj5IrV78SeeV2htVBw_lDd60Bx722RKgal94V5B4FOqxQrU96rOmsPkBIeCQwr8iXSqxWeuph-jgpsBBulzFATLOqRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شدیدترین سیل در پایتخت سه میلیونی غنا، آکرا
🔹
گزارش‌هایی از کشته‌شدگان و تعداد زیادی مفقودالاثر منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/665221" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYsuwpNGZE0HPSHbfe48OPEi_ApVG471fPJqu5jzGrL4y-2OEdrY803OfrTTSDtzPN7tGtkMWUT_uFXbf9L5IlMyOEF75OKa7DP18h_zw8KPyqSbz7m1QLV4TAcP7ALSR613hZ0BuTSj_Y1qoO9r-WK3RVP86wEdx3xuSsbaTXz4Ca12c9kMigHincgJiYhiYdE8ptriDadsZxhN0XyRBXGlkWNFHA5IACSVmZ3NmG86wgPHXMpY8lZ5FJ0nsdTWMK69MCv6mbcy3mrX-7MXWBPffpstvqCzLSKiBa42vKE49qexibTMa6TmF-rgCqreSjBQbIn4tGCg10KrxMZ4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوهی عظیم از دوچرخه‌های رها شده و شکسته در چین!
‌‌‎‌‎‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/665220" target="_blank">📅 10:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حضور مقامات و سران ۴۰ کشور در مراسم وداع و تشییع رهبر شهید انقلاب
سخنگوی مراسم وداع و تشییع رهبر شهید انقلاب:
🔹
در مراسم وداع و تشییع، علاوه بر حضور گسترده مردم، شخصیت‌های سیاسی، فرهنگی، علمی، دینی، دانشگاهی و نخبگان از اقصی نقاط جهان نیز برای ادای احترام به پیکر مطهر رهبر شهید انقلاب در تهران حضور خواهند داشت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/665219" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzF3oqXrvhvupdlgOYL-DuOCljJVcn3JLlDJD7zTGmJf4Tmy-pETQvOBcQwsfaz54OcZCiSwZC6FMdrxhyGxenUa0Fd9X_dUbrjyD-IKzEAC0lKZ3lMq-2Cns3h_LR7LX42lw9DqO-RbokFl8fD70Cd9vQgrrvygKx054o0IHRMCtXJcyWLlVMb_jVmJMaWtWiYYF4vBwm75tk0qg73t0uFau8JijLgUhEQ4EaRi3NpHcI1iZF_oOWK1d8uzRKfNa9BgRf0dS7r-sE-GU4iFVs132EM8Inb6nJSEMOUtU18jmsjiaFqcnfGyMoAggoeTSww7lpLGvho2_AHqpE6vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرجمعیت‌ترین تشییع جنازه تاریخ کدوم بوده؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665218" target="_blank">📅 10:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
جزئیات تعطیلی فرودگاه‌های کشور در ایام مراسم تشییع رهبر شهید انقلاب
رئیس سازمان هواپیمایی کشوری:
🔹
فرودگاه مهرآباد روز جمعه تعطیل است و تنها پروازهای دیپلماتیک و سیاسی انجام می‌شود. فرودگاه امام خمینی در این روز طبق روال عادی فعالیت خواهد کرد.
🔹
دوشنبه آینده آسمان تهران و فضای هوایی فرودگاه‌های مهرآباد و امام خمینی‌ به طور کامل بسته می‌شود و هیچ پروازی انجام نخواهد شد.
🔹
سه‌شنبه فرودگاه مهرآباد به فعالیت عادی بازمی‌گردد، اما فرودگاه امام خمینی به دلیل انتقال پیکر رهبر شهید به عراق همچنان تعطیل خواهد بود.
🔹
هجدهم تیرماه نیز همزمان با مراسم تشییع در مشهد، فضای هوایی این شهر و فرودگاه‌های اقماری آن به طور کامل بسته خواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/665217" target="_blank">📅 10:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
۱۴هزار نفر از اهل رسانه راوی وداع و تشییع رهبر شهید
سخنگوی ستاد وداع و تشییع  رهبر شهید:
🔹
۱۴ هزار خبرنگار، عکاس، انسان‌رسانه و مستندساز برای پوشش رویداد «آقای شهید ایران»، در سامانه ثبت‌نام خبرنگاران، ثبت‌نام کرده‌اند که کارهای نهایی صدور کارت آنها در حال انجام است.
🔹
همچنین بیش از ۹۰۰ نفر از خبرنگاران خارجی شامل ۳۰۰ خبرنگار رسانه‌های خارج از کشور، ۳۵۰ خبرنگار رسانه‌های خارجی که مقیم ایران هستند و حدود ۳۰۰ انسان‌رسانه و بلاگر خارجی در برنامه حضور دارند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/665216" target="_blank">📅 10:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حکیم: عراق اجازه نمی‌دهد خاکش گذرگاه تهدید کشورهای همجوار باشد.
🔹
کوبا خواستار نشست سازمان ملل برای پایان محاصره آمریکا شد.
🔹
واشنگتن‌پست: آمریکا قصد اعزام نیروی زمینی به لبنان دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/665215" target="_blank">📅 10:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید   رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/665214" target="_blank">📅 10:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید
رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا می‌شود.
🔹
تردد انواع موتورسیکلت از ساعت ۱۲:۰۰ ظهر روز چهارشنبه ۱۰ تیر ۱۴۰۵ تا ساعت ۰۶:۰۰ روز شنبه ۲۰ تیر ۱۴۰۵ در محورهای کرج-چالوس، هراز، فیروزکوه، تهران-سمنان-مشهد و بالعکس ممنوع است.
🔹
تردد کلیه وسایل نقلیه از ساعت ۱۲:۰۰ روز جمعه ۱۲ تیرماه تا ساعت ۰۷:۰۰ روز دوشنبه ۱۵ تیر ۱۴۰۵ در مسیر (جنوب به شمال) محور کرج-چالوس ممنوع خواهد بود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/665213" target="_blank">📅 10:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01586d97c0.mp4?token=g2tNQjD2qEhVqH0OYPdJveezdbfAFgMrbOOLE_UD1pT0BxHaSmWhrvyj2kywouXL_PLVSHN9HMM8qZgIkvfDte1sYANYiTfx4JmQ7FmbVDCW8fAhHSdab0lIM14uKLj0r5t-UjACM3xCkbuzcm7BjHM7b5DUibr-0zee2tvPyUz9KJJogBvH_CRGhBafQKJKFOGNVE1mC-8GKlVHi2ywnNaszlPnAO2oaqrkWf3ydSnYd_MUOsHq6E6fD9U_9AWpf-s30CVkjqYe3ziSEXwmrM8tzzs0WHanMA9o1ef_z1vW5192RRwDun00_ea-b1dt28UwjwxJnpI6aCwRebEMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01586d97c0.mp4?token=g2tNQjD2qEhVqH0OYPdJveezdbfAFgMrbOOLE_UD1pT0BxHaSmWhrvyj2kywouXL_PLVSHN9HMM8qZgIkvfDte1sYANYiTfx4JmQ7FmbVDCW8fAhHSdab0lIM14uKLj0r5t-UjACM3xCkbuzcm7BjHM7b5DUibr-0zee2tvPyUz9KJJogBvH_CRGhBafQKJKFOGNVE1mC-8GKlVHi2ywnNaszlPnAO2oaqrkWf3ydSnYd_MUOsHq6E6fD9U_9AWpf-s30CVkjqYe3ziSEXwmrM8tzzs0WHanMA9o1ef_z1vW5192RRwDun00_ea-b1dt28UwjwxJnpI6aCwRebEMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضهٔ شب تاسوعا| قاجار | ۱۲۵ سال پیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665212" target="_blank">📅 10:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
الحره: کمیته اربعین در عراق مسئول تشییع پیکر رهبر شهید انقلاب شد
‌
شبکه الحره عراق:
🔹
به گزارش الحره، کمیته اربعین عراق مسئول برگزاری مراسم تشییع در نجف و کربلا شده و دولت عراق نیز تمهیدات امنیتی گسترده‌ای برای این مراسم در نظر گرفته است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/665211" target="_blank">📅 10:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بلومبرگ به نقل از یک مقام آمریکایی: مذاکرات دوحه نتایج مثبتی به همراه دارد.
🔹
رئیس مجلس ونزوئلا: شمار قربانیان دو زلزله پیاپی هفته گذشته در این کشور به ۱۹۵۰ نفر رسید.
🔹
نتایج ارزیابی عملکرد آموزش و پرورش تا پایان شهریور اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665210" target="_blank">📅 09:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b360968015.mp4?token=dJAz49ggbvXioEFl9c9EVnrHj0W5WWz1Zb3RBRGlsE-XMA4AbUnlMDNL-oQ4tot4FKh61jzmwoD1IY2SZj8jTq9a5Ps5SMN4ZncnZfmN0xqKnBilh-h69MEv06CqTACVP41Ob0EZr8Dv69uZpUlx063a38YBm8SvLS523PfsK_YIuzMVtRMJpjyXBJFOEXQjAYzAVGMWbIpS6f9PLYC1oR6FmfcYSc2sL6UD-GUC_8bIejm7BnK2BAE2BR_BeLSTpHJc0gGDWT-ZhPmaiGzcKNyTs5_1OSx9ykTmN2BWKoc1UMJLbF08ipNStelhyU-pZoBwmuQY55NFxEwSzcUoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b360968015.mp4?token=dJAz49ggbvXioEFl9c9EVnrHj0W5WWz1Zb3RBRGlsE-XMA4AbUnlMDNL-oQ4tot4FKh61jzmwoD1IY2SZj8jTq9a5Ps5SMN4ZncnZfmN0xqKnBilh-h69MEv06CqTACVP41Ob0EZr8Dv69uZpUlx063a38YBm8SvLS523PfsK_YIuzMVtRMJpjyXBJFOEXQjAYzAVGMWbIpS6f9PLYC1oR6FmfcYSc2sL6UD-GUC_8bIejm7BnK2BAE2BR_BeLSTpHJc0gGDWT-ZhPmaiGzcKNyTs5_1OSx9ykTmN2BWKoc1UMJLbF08ipNStelhyU-pZoBwmuQY55NFxEwSzcUoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ ثانیه از قاب‌های که دیگر تکرار نمی‌شوند
فقط چند روز مانده تا وداع...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/665209" target="_blank">📅 09:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حق سرانه درمان بیمه‌شدگان صاحبان حرَف و مشاغل آزاد و مستمری‌بگیران مشخص شد
سازمان‌تامین اجتماعی:
🔹
در سال ۱۴۰۵، حق سرانه درمان بیمه‌شدگان صاحبان حرَف و مشاغل آزاد و مستمری‌بگیرانی که طبق مقررات از مستمری آنان حق سرانه درمان کسر می‌شود، از ابتدای فروردین‌ ۱۴۰۵، مبلغ ۴.۰۰۸.۶۰۰ ریال (معادل ۴۰۰ هزار و ۸۶۰ تومان) به ازای هر نفر در ماه تعیین شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/665208" target="_blank">📅 09:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOeEm-VKqsklAcWQR8mltz6XfiTa1p47VlodA7n4iKRX_AiFXhneIbX12mX6zvMDVwXlLzBfYutiD1f0dwIzh_tp6JYhtK5_Eeqy5VWMZDxTtMUU0ogxGQ8qAgQf9Schzjd3PnPSPK98M_p0Jds1OExVDA_N5v9WD71F8Fjj3-ujh8QvbYrM8x5AnO_q9pc5kB7brDojgiu0ke3aqasjWueJh8d_ElXhdaSbk35whIH5h2iUNml3qFERd2JgwvvtkxSIagmxVy-8eNHQ0NOqLK4460JIcpyWTprevwltfZcnmX2N66roniOweMT-IOJXptbO-lugdFplS1W8NJwCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم ما از میزبانی رهبر شهید
🔹
اقدامات داوطلبانه ساکنان شهرهای میزبان تشییع رهبر شهید برای پذیرایی از زائران و وداع‌کنندگان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/665207" target="_blank">📅 09:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665206">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c3370a7e.mp4?token=dIKa2BA0Eg9LMg_5sD6RsEqiX1TxO7Gc6t1NvXK4ZqZ9MbXo_hxnrzW_2m06hJIggeKTPTFcttxBxNYqTXdbbEsk2jTf1ImFoBfCJPTu3UuZojbLxpaUuELUf3cw2S9FGvowYKMyiI17sq66ya-SSWJYJX6In83oq4yIoDCwSKfLzzl7bNKE08SZFb-Bn99_NvBzyP4lzYJFTY_h4ZKlozNE0oba2R_Z1yjnGtMkzsRtQl3j668TqAev68qOpbXFwPgLDs8uUINr1qehyognGcNK8TA4saoEKw_cMmSazK1g2Xu1p-zHWzMuwx3PHbFzIdPqw9xbjOnCxZQdIDHvMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c3370a7e.mp4?token=dIKa2BA0Eg9LMg_5sD6RsEqiX1TxO7Gc6t1NvXK4ZqZ9MbXo_hxnrzW_2m06hJIggeKTPTFcttxBxNYqTXdbbEsk2jTf1ImFoBfCJPTu3UuZojbLxpaUuELUf3cw2S9FGvowYKMyiI17sq66ya-SSWJYJX6In83oq4yIoDCwSKfLzzl7bNKE08SZFb-Bn99_NvBzyP4lzYJFTY_h4ZKlozNE0oba2R_Z1yjnGtMkzsRtQl3j668TqAev68qOpbXFwPgLDs8uUINr1qehyognGcNK8TA4saoEKw_cMmSazK1g2Xu1p-zHWzMuwx3PHbFzIdPqw9xbjOnCxZQdIDHvMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان در فیلیپین
🔹
آتشفشان تال در فیلیپین دچار یک فوران بخار و خاکستر شد که حدود ۴.۵ دقیقه ادامه داشت و ستون خاکستر را تا ۱۲۰۰ متر بالا برد. سطح هشدار همچنان روی یک باقی مانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/665206" target="_blank">📅 09:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سپاه هرمزگان: صدای انفجارهایی که از صبح تا ظهر امروز در بندرعباس شنیده می‌شود ناشی از انهدام مهمات باقی‌مانده از جنگ است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/665205" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
چه تعداد از هر جاندار روی کره‌ی زمین وجود داره؟
🔹
بیشترین جمعیت متعلق به کدام جاندار است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/665204" target="_blank">📅 09:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665203">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57e7a2534.mp4?token=M7HxZg5Ep1AzfTUEE5Q26IQ8KX3plP1TznnXFlSEOC8iz7qx5wzKS902B6Z4Xq2jByqqV-5EhjeoQoryvl4cBIEL6eO5BWHNlVJ9bUr6HcxluNstpvs2L2oPwaA1BOi8dppMURt3n6egnLRvoLnbognoVKSsSUjQ-OS1XuC5r7RpBm7z4SodgLGA04AFAeweiRhOLp_gC1V5rn-s-OmO3mmXrOkhLo5oRFzDbUqvP9GF5Se3u3Sk55Kx5cdDWo53uzx-OF-r753ER-M0OcXA5C7uBGSNL_GY0JPlZkvsbl6ttj3c-Zb_VEEIWQ03Salyl7WZROQXYThBeL0bAaCU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57e7a2534.mp4?token=M7HxZg5Ep1AzfTUEE5Q26IQ8KX3plP1TznnXFlSEOC8iz7qx5wzKS902B6Z4Xq2jByqqV-5EhjeoQoryvl4cBIEL6eO5BWHNlVJ9bUr6HcxluNstpvs2L2oPwaA1BOi8dppMURt3n6egnLRvoLnbognoVKSsSUjQ-OS1XuC5r7RpBm7z4SodgLGA04AFAeweiRhOLp_gC1V5rn-s-OmO3mmXrOkhLo5oRFzDbUqvP9GF5Se3u3Sk55Kx5cdDWo53uzx-OF-r753ER-M0OcXA5C7uBGSNL_GY0JPlZkvsbl6ttj3c-Zb_VEEIWQ03Salyl7WZROQXYThBeL0bAaCU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکاف عمیق میان دموکرات‌ها و جمهوری‌خواهان در احساس غرور ملی
🔹
نتایج یک نظرسنجی جدید نشان می‌دهد ۲۷٪ از دموکرات‌ها و ۹۳٪ از جمهوری‌خواهان گفته‌اند به آمریکایی بودن خود «بسیار» یا «کاملاً» افتخار می‌کنند؛ آماری که از شکاف چشمگیر در احساس غرور ملی میان دو حزب حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/665203" target="_blank">📅 09:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665202">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96f5db9cc.mp4?token=e9Y5f67QO2fPUef4PHLf-VSXVylIz-TApwGsqYWZbEkLBhVNOXoYdQdN1JZvJA7uaK_h6XZqDW-5BVevd9EOepHNMGdEndhLkMXZnZbjRyTljyXJgVZbpn3bj1D9p1gmvaG1v0Glc9J7iBBBTeO-uExdUCUpB2jHXUCN3fjnsC2dZa_evkV1MVbUI3bMRUV8qOjCtJyIll-qEiFYGzac7LQDjIeYV5sj6aN1vG7c5gCNf3p0wfmdL2nu4TXEKrBhmQBdkKq9meul7SnI59fpoz7S1PaXlYnApxiPQbBCVIPGtRBmtA0NRVyRLogf4a19kCyluDYgn5NH3AqdiSj6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96f5db9cc.mp4?token=e9Y5f67QO2fPUef4PHLf-VSXVylIz-TApwGsqYWZbEkLBhVNOXoYdQdN1JZvJA7uaK_h6XZqDW-5BVevd9EOepHNMGdEndhLkMXZnZbjRyTljyXJgVZbpn3bj1D9p1gmvaG1v0Glc9J7iBBBTeO-uExdUCUpB2jHXUCN3fjnsC2dZa_evkV1MVbUI3bMRUV8qOjCtJyIll-qEiFYGzac7LQDjIeYV5sj6aN1vG7c5gCNf3p0wfmdL2nu4TXEKrBhmQBdkKq9meul7SnI59fpoz7S1PaXlYnApxiPQbBCVIPGtRBmtA0NRVyRLogf4a19kCyluDYgn5NH3AqdiSj6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم فرانسه به سوئد توسط امباپه
/
صعود بی‌حرف و حدیث خروس‌ها و تقابل با پاراگوئه در یک‌چهارم
🇫🇷
3️⃣
🏆
0️⃣
🇸🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/665202" target="_blank">📅 09:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665201">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0dd83e1c.mp4?token=sLq2yLZiPRJ6zEE3R88F1pNFk7Zpdv85p-W1NdbLJ9_W8zv2IMmYzAee7BduvVRL8zSXVFoH8gaLDd3VzpLD2so1N0Wv7066Awd5ev-bpkRcSBX6NQhftSv0mtzY8ri97gOyhE1BksqhvvSzUskY2lloEmwnL877MJUlNHLIosgdDJvXqVzg3ftk8Fi_b2KSICmPh4othLVfxTVYWBKme19MK_pSuGiT6yJDnk4kuCX_ZphrvPb7FoeTvcjkbgsMM6asb9OMv62ROQ9Aze5eoyixICQP9UBd9fAp7KTWrH6nBuY1VbYwFIsA6trNtqu7BV1sZDbK4T2fB6_7zc2rLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0dd83e1c.mp4?token=sLq2yLZiPRJ6zEE3R88F1pNFk7Zpdv85p-W1NdbLJ9_W8zv2IMmYzAee7BduvVRL8zSXVFoH8gaLDd3VzpLD2so1N0Wv7066Awd5ev-bpkRcSBX6NQhftSv0mtzY8ri97gOyhE1BksqhvvSzUskY2lloEmwnL877MJUlNHLIosgdDJvXqVzg3ftk8Fi_b2KSICmPh4othLVfxTVYWBKme19MK_pSuGiT6yJDnk4kuCX_ZphrvPb7FoeTvcjkbgsMM6asb9OMv62ROQ9Aze5eoyixICQP9UBd9fAp7KTWrH6nBuY1VbYwFIsA6trNtqu7BV1sZDbK4T2fB6_7zc2rLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به سوئد توسط امباپه
🇫🇷
1️⃣
🏆
0️⃣
🇸🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/665201" target="_blank">📅 09:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665200">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExE-fMHJX78tpFLMPIAXFTIuZpzXK5c3cJ71oiZtRcPMtbz63t3EXyV0VG6izOQ11XTOEKbJoZKH5QdYjR7E1xsEogBaxIlUe5OYc14SQXaYRGEL7cTIJTjSSg2Qs_p4Y6zjUhbUIxoX70CDYSHcxwE2BkVIhcSLw1RqP7piEiJFT4MkGFTHHzPBE4Uy7fdLq7H5S2F3GnE4AdQbqUDeZZ2yj5YGz5a18iSkVxvtfQi-DMphayoLsSn2tBLceKncDw2g04g3ci5cCqDRZ98dHiDf1G3SaTw7WGWsaKCzp5H40UJVg24THXkew_-jW5sk8ATNBrWbUtH4Gb-cVeaU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند پیشنهاد کاربردی برای بدرقه رهبر شهید انقلاب به کاربران فضای مجازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/665200" target="_blank">📅 09:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سه‌شنبه ۱۶ تیر تهران تعطیل شد
فاطمه مهاجرانی:
🔹
هیات دولت امروز چهارشنبه دهم تیر تصمیم گرفت که به منظور تسهیل خروج عزاداران رهبر شهید انقلاب اسلامی حضرت آیت‌الله خامنه‌ای از تهران، روز سه‌شنبه ۱۶ تیرماه این شهر تعطیل شود.
🔹
براساس این مصوبه، همچنین روز پنجشنبه ۱۸ تیرماه مصادف با آیین خاکسپاری آقای شهید ایران در مشهد مقدس، در سراسر کشور عزای عمومی اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/665199" target="_blank">📅 09:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665198">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z71lPbq1jYCCiyzDSyxIADteUPh_dAIBGRgILnAW1hK3qBCGvB_YnuuVBYDkMnJkLK39ZMKZxZBGDY83zdD6gESKr5bzATjoV45GUffHXY8XZgTwgDZ-ub1YpJs_V0bC3m_5NZDEvxycy-_MWZMLLbVjW5jo1zZyUQpt8eZ74lXTR6E9LzsfsYV1NANBb3_8Rp2iO_50ibWWwAIss3SYS4X32J2C6wij4yxuzexGBIN33gYSoePgQNJpV9Azf8V6zia121qoWfl4VZMjfWm6lHYwSbvxhuBfTT1M9tyzRaGky3dmQDnBfu5du-14E2WOZgpOpqZyiuajP7Fa176hNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه رو اشتباه نخور
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665198" target="_blank">📅 09:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665197">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
۲۵ هزار میلیارد تومان مالیات بر ارزش افزوده به صادرکنندگان و تولیدکنندگان پس داده شد؛ رشد چهار برابری استردادِ مالیات بر ارزش افزوده در صد روز نخست ۱۴۰۵
‌
🔹
جدیدترین آمار و ارقام مربوط به استرداد مالیات بر ارزش افزوده به مودیان نشان می‏‌دهد که میزان مالیات بر ارزش افزوده مستردشده به مودیان با رشدی ۴ برابری از ۶ هزار میلیارد تومان در صد روز نخست سال ۱۴٠۴ به بیش از ۲۵ هزار میلیارد تومان در صد روز نخست سال ۱۴٠۵ رسیده است. رشد ۴ برابری استرداد مالیات و عوارض ارزش افزوده به صادرکنندگان در حالی صورت می گیرد که مجموع درآمدهای مالیاتی در این مدت ۳۵ درصد در مقایسه با دوره مشابه سال گذشته رشد داشته است.
🔹
سازمان امور مالیاتی کشور همواره تلاش کرده است در کنار تامین درآمدهای مالیاتی مورد نیاز دولت، تسهیل فعالیت‏‌های اقتصادی و حمایت از تولید را به عنوان یکی از مهمترین راهبردهای خود دنبال کند. رشد عملکرد سازمان در حوزه استرداد مالیات بر ارزش افزوده محصول این نگاه راهبردی است که تامین پایدار درآمدهای دولت در کنار اقدامات حمایت‌گرانه از فعالان اقتصادی می‌‏تواند زمینه‏‌ساز تامین نقدینگی واحدهای اقتصادی، تقویت سرمایه در گردش بنگاه‌‏ها، ارتقای رضایت‏‌مندی مودیان و در نهایت رونق اقتصادی کشور شود.
🔹
استرداد مالیات بر ارزش افزوده به فعالان اقتصادی و بویژه به صادرکنندگان از جمله ابزارهای حاکمیتی برای حمایت از صادرکنندگان، تسهیل فعالیت‌های اقتصادی و بازگرداندن منابع به چرخه تولید است. بر اساس قانون مالیات بر ارزش افزوده، برخی فعالیت‌های اقتصادی بویژه صادرات کالا به خارج از کشور از جمله مهمترین فعالیت هایی است که از مالیات بر ارزش معاف است و مالیات و عوارضی که مودیانِ مشمول بابت خرید نهاده‌ها پرداخته‌اند با رعایت مقررات به آنها مسترد می‌شود.
🔹
همچنین در مواردی که اعتبار مالیاتی مودی نزد سازمان امور مالیاتی کشور بیش از مالیات و عوارض پرداخت ‏شده باشد و مودی درخواست کند مبلغ مازاد به وی مسترد گردد، سازمان امور مالیاتی نسبت به استرداد مبلغ مازاد به وی اقدام می‏‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665197" target="_blank">📅 09:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qe8wjm1YPwYZF_9iDOmbvufpVfr9RL6tpkFUXMiCJpLhs5qYqCJY1VlTZ-58EI0W4a8Xtm8uficVL1jTQ8mL-Amx6UCJjtTqrefVoTlN3vpbAD2X1wTZ1BLKE3s4x7SEEXCvX4CsGSKaKdWQPLtKKcMxGNeJsBfEGo68jnCirv45NL8t6MoNuKDdQUD13hUvd4P6WNxkHmG383w9plprXVkxaZfh8GGSkdls1nJr75UCEq1R39OfIqtnIlk3FJ3cbW7Ot6pJO_6Ggk5_z9POdv1Sl1GnUuhpQPCI-kMFYYHgo5BeZZr2cKCVmkLDxYp7HI4e2jZUy3OBBnWRvPjagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErQ-V1P0JKyD7_eXVW_6kbu0TOMtAc_TLThgvsymVEYd4oa5aKeuYoHkX7-M7h4umCmEAJtKBNntknlAGyai6XpbGc0YfQsEH9PyFfk1UVvdMXSVgZAsT_SJdExbydKU-wxMhUkNNwSfesrOLWq0lT-nm7Fg7vyRc8dVArIWZQgXFwPJHjo8niXAXvdPy_N1QZKHIcMbxi9MDyTChEZYMn_19z9Q7GiIEkesxLSAKFeru3SAnEpHwaihZSUA-6S4zhUeCZAhlImHkRqnOIfSdJlA5ljtWTNW4YJqrlBywVWpysiKTrU4zLjdp_jb6MxhxDasx7V7O4HX0D7_CkNCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4gxGABB_6GpjlTsIE0PfjVcxYmxRwEOboEVf3pbRvhSrBc4wASBtoMTfKlNYP-RTLN1ONNrCA28bFOhsE6G-_3YbwQbKLKxGBbKfLH2phe5bxju6i0ttxZaX9x1uqQUxhGEk6wU30zDKMGxO9YKZiZSXWLvf1ohky1rahiJd6MyHFfiA9oXOYU5eLCX1KmauVfyTVzcELJgEcC9tYScK1kMj-_MfGZvBnooXtzNu0-G8vFizdLomkn62YzrbDIIUQ5GfiyLqmG4DW94vteMwUD1v7oDgCjpyr2W-g2u3-S6vRGVc7EAVnnqHkAV1PRGzY5B1tHycZXLgEaA7A12fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f47ab637.mp4?token=Wc2Xeqt9DJ1ZHUeCHxwOFM6TbwMKNitSE2UfkHEBMQssIGJ8_-JIqjvd-PRVx1mLyUT7qmz__6q9JAhCTxcVC8PB9PyFhEJIHXUDF8B01EjV4xrFLZr2ccy9zeT4le_uKIREo7-AGP8ap61heAqJ_sEIV7B_2X4hI6RjzYnspOrYy_dhQHQCDCqvTEUYKz-RA6ffdAjgew3V-WnZc9OLZE2fswW_3GlqIMZDqwn5htvNaDHlUmt_nJ5MU7VNUsac5-8W6BysExBJX26pLRVLDnQ13qh1qQmbMORsTYyd89UxnaMNTNbz44v5de7YtLk2QkNi1oD4hkiVvxAGI8LpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f47ab637.mp4?token=Wc2Xeqt9DJ1ZHUeCHxwOFM6TbwMKNitSE2UfkHEBMQssIGJ8_-JIqjvd-PRVx1mLyUT7qmz__6q9JAhCTxcVC8PB9PyFhEJIHXUDF8B01EjV4xrFLZr2ccy9zeT4le_uKIREo7-AGP8ap61heAqJ_sEIV7B_2X4hI6RjzYnspOrYy_dhQHQCDCqvTEUYKz-RA6ffdAjgew3V-WnZc9OLZE2fswW_3GlqIMZDqwn5htvNaDHlUmt_nJ5MU7VNUsac5-8W6BysExBJX26pLRVLDnQ13qh1qQmbMORsTYyd89UxnaMNTNbz44v5de7YtLk2QkNi1oD4hkiVvxAGI8LpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان سرخ ونزوئلا در پی زمین‌لرزه‌های اخیر
🔹
تصاویر منتشرشده از پایتخت ونزوئلا، آسمانی با رنگ سرخ و نارنجی پررنگ را در زمان غروب خورشید نشان می‌دهد. بر اساس گزارش‌های منتشرشده، گردوغبار برخاسته از زمین در پی زمین‌لرزه‌های اخیر با پراکنده کردن نور خورشید این منظره غیرمعمول را بر فراز آسمان کاراکاس ایجاد کرده است./فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665192" target="_blank">📅 09:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌شش | میرمهنا</div>
  <div class="tg-doc-extra">میرمهنا بندری</div>
</div>
<a href="https://t.me/akhbarefori/665191" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
میرمهنای بندری (مزیتِ چابکی)
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «جنگ‌های نامتقارن در بازار»، «سرعت در برابر سرمایه» و کالبدشکافیِ «سندرم سقوطِ مدیرانِ تندخو» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/665191" target="_blank">📅 08:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22dd9a174.mp4?token=sGK5N06jG91lmqqBs7wbeIpwrtwad7BrvnGE-eoUeb8ngazOzhHHyT84FR_ZXbhSp5AXEop2R-gTLPwYAqZF4W_5tFW5nthmumeKK1qbygBua98s2JogEmRGFSbLB8IbO8vgrPaezSm-gCJ4IcnoG0eyTWg1IXMFvWjuU5HV12zOku7ZsmPJo2JYG460YyoAxCknG4pVZERTSI_2G03jQ18pCSUfW9Y4yiAEUnvkzqRiELX3eELdRvTSUFVvcq6shz602nTUjsT0B277jcjCvqCfZyJ9BSnhE8wYq0SgxhEKLSKQ9WAGkJdRoxISDYfBy7nOAYf43K3V4Mf0HoUsPaiL7nPC08spg-0-fpNg05KDXvu_MhLnhT7XActEP-14iJ-CYTgRN2k4lqYClt6tQs2HVmW_7-p8scZnpWNn-VujPACcgauvF9ArV8aEuSIkSnFKhroHbuINbqpdiNXcPX_SOK8wJKJFaKewofClogPMVffciKPzlky4vpXoRNA3LIPvVmwB54SuK2uADEwsqRjAhHSgdJ07fuIsY36GX8YTq2HsaqJXYuTpfJA3IpfTCwIcWLd0e0pkaGNC9TrB6zPPpKDiqgZJA_frcah7NRCWjUAvKVKpUJxFmxpshv3grilMAmXDCAlp1eqi_vsphTLYhjHvG_o74KMnhh7gHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22dd9a174.mp4?token=sGK5N06jG91lmqqBs7wbeIpwrtwad7BrvnGE-eoUeb8ngazOzhHHyT84FR_ZXbhSp5AXEop2R-gTLPwYAqZF4W_5tFW5nthmumeKK1qbygBua98s2JogEmRGFSbLB8IbO8vgrPaezSm-gCJ4IcnoG0eyTWg1IXMFvWjuU5HV12zOku7ZsmPJo2JYG460YyoAxCknG4pVZERTSI_2G03jQ18pCSUfW9Y4yiAEUnvkzqRiELX3eELdRvTSUFVvcq6shz602nTUjsT0B277jcjCvqCfZyJ9BSnhE8wYq0SgxhEKLSKQ9WAGkJdRoxISDYfBy7nOAYf43K3V4Mf0HoUsPaiL7nPC08spg-0-fpNg05KDXvu_MhLnhT7XActEP-14iJ-CYTgRN2k4lqYClt6tQs2HVmW_7-p8scZnpWNn-VujPACcgauvF9ArV8aEuSIkSnFKhroHbuINbqpdiNXcPX_SOK8wJKJFaKewofClogPMVffciKPzlky4vpXoRNA3LIPvVmwB54SuK2uADEwsqRjAhHSgdJ07fuIsY36GX8YTq2HsaqJXYuTpfJA3IpfTCwIcWLd0e0pkaGNC9TrB6zPPpKDiqgZJA_frcah7NRCWjUAvKVKpUJxFmxpshv3grilMAmXDCAlp1eqi_vsphTLYhjHvG_o74KMnhh7gHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میرمهنا بندری،
قصه بازپس گیری جزیره خارک
#پادکست_کافئین
| فصل‌دو،قسمت‌ششم
☕️
🔹
چریکِ دریایی که نشان داد چطور یک ساختارِ کوچک، باریک و پر سرعت، می‌تواند با حذفِ مزیتِ رقابتیِ رقیب، مغرورترین و سرمایه‌دارترین غول‌هایِ بین‌المللی را به زانو درآورد.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://aparat.com/v/xmlax4n
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665190" target="_blank">📅 08:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665181">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fH-uUdBQCP0Nr2lOZ8j6tmUxXJjucpHdRyDVqPIeIZ1SIKJrGLLawgs-HGyJsPoDftfVyaZJjE8ZrN3OxnolXpXEgtlFRnIv8F18g0JBKTan5l_JRZPCEx7xElsjhuauSCkklYjqFd_Ng9TcSqpOSPqoJv467gfmODH62NmZQEBWxwAuGKE9qGu06f90VJxFNd2KWUKFpVHO-qweoHyXM1OvetRVuhC6TDbtT07u0lOaECXyr4gHcvpCnggX1KwzG0ms6x-YaRzNOZz_rGYcsciTdgdD3rrXEXYGtawwcWNGqNhl5yQxw8FxWA3pm5nWgosHb1eZxOZBfBxH1CZrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ac10ZzmJ2XCpM785EhTcUmYDA10pMVDmXDkDdQQTADAmM862KU35-ELyE9U-hGLAvoiPNB1t21amV551jCkfBPvCvxQPQbQ-1vtiSX0we0iWKgnrJId5aTH6nYuHTpgxap5U591ZqbV8zTt0KO8CaTugRYxRwOf0rSSlI_r04HNqinQiTtaB1RXbqSUl9vG2v_59P5hKmoLLL9xIVJ-KzrIbfRdbbCCd8dLfQh1Kw7E6KcHn6A_cOVP0EEkcvJ9Ho-LK7u064yTnK81FVQc_zg5t4rqRbjZvpEoxXq35wk00m8FbwLEufBkJAdlOwdjoSk4aTRu2rUHoG0G4RLQaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GS6_xVHa0bHORtW4a8rG-RWeHgiE1Ysi4aYvmD_pxcrHdo-i6DzkLsmBuyPR2O31KnCu9IaxWofSklbuXbtk3Zf6_nFaax_TddFUPMVa9Uzzp7FFbFs5Uj6_jGxmmmYqXV2Pady9BFFMkKOGuapB_wAx2OHdTdcPc2PFtgSMWjHGxKn4TA1NK1RUolVzkd_7aAMXdlwya-KusRQ2HWtk3CbmU4_4xiYoleB1XKbjHypaH7iecDDePOi8alba7xZAHUHNH2y9S5_yKCOLtJw9mZnlUVgLG38NNrYdqAJSQzK16jbbkwoOSZkx5nqmqlJplGhKzwJ7fdq3noBsVAiETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BifCF1lSyb6zBz3ywnJjkCiJekiM3tEXI1nh8NWQWy8YqbNqrtONq05FCP7hXZFtuZwYbyMThYRGJPyGNdT7OcBLQIKkNYDX7Ak3u3XTrcfTMonnDkgxVsc8ck9t-mPBiScLe3m8jwtKGU8RoEAOqG_WbpmJ70vwn575R7E8fHSqlVqJiOSIp01FQ5ZMi2noRtAIIfXlMbHK_oCSKTNib9MW5tc7pJAbxV36YHyhaUkKbfa90p4k7GQfrEvqNwi2d8y6sDt1LU_CsqFltdxMTwzXzQc5qyUmpVaAu2w_BKyzOank2dw-_XbsYyZ2dxZAHJE8t-1AgrYVfuaQPGLoug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRA_Pt5nIr_UOpDpiA53Vy3IwQd-TJcz9Zp4Zj5H8Ss8NsOMPzmTHL2_6tnuPA6y_4lRvHNfHLDywqb8dkXBqB1JUhU84FFTmS5i7jkQhsJkQWPvSOHZ17RmceqedhLaBJaKgD_M-rhpJGTg7raIz8g20eKAl5lImNLWs6PQ_LbzXGzG6vTfLXGMD3g86uJdugp_G5i57EghbD5ugdiFO56-OknZHIKzrZAtnVJZe_tPY8QY5KnkQu3owexivFDuCpNATsN0OYO7tMJIX7Viy8gyKrhjMsT9TDp5VPHs8T_VwxDLAYcWkb4lgcXFIUL5CmsXOaYuKuAhfRNeU2ApBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JktmHoulY8p9tfinmAn_RLVWH9l6aEm1LGKNeRY29sOE6DwAByv367mVSltIyRlUF6M1X_G2NUNFEl0xbXnzAYII4hRFTbsZXt55WcVWyCx-Czm_oAn7L19HHeUtGpOcdgMvgb1e6ncghWzxGSSLC5qBuGDcHVp0B8uh-PbGpNlU6mj5JA5arm4dXQ4vnrxc_tCMVTGNzl-TDUXljXPfSqKFkGBr41dUKK-1kEYnZYSlYPG83vJ4IjAPjQ7QOLArHYRbtuG1V6dYfeLLFWcXIhjdvJDuaREz7icobRgio0j_ZzcAvKj13HXBrt4eKWy-n_0P80UGqJwXqUHwZqiM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBlxS8QJHij9NCPBXG-0efl7RqSIttnUNHK8hMzu2a18EMKFrNPvoClv72W97wVaipBle4Kw4ed6i4CeizYTZiwdLypxNEiUd77DNbH8TTXF0fxW3nRwEh3ILpGZ0JEeNNomLUzW6lDIt6NJuMPdagPh6AozlTNWWysj0PgV6tO_E0Ib1P8__W79MsJhogcYxdarhzOos-asFG2ZGJ3hx1t0buQ0JledL-ABZXGJFxuiQl3XKM5Vcp2U-khFq-hCDNCsaj96gLYMjOVgxRjR6BAJSpu2ybRhUJVK0I7eYGfnAg02DFfqvTzAxhrt8HBmcR9W1EgUSll8zIy6LmzBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtCvVgg903w0zTBeoMqFYs3lmc2s-s5PYnPqAzOTy3REYdvB3p-yhw1dRl3ROuULxxM5mCa2ejOpLRr8jnZLipqN9JAm_uub6oz0AKB0Y49bQo6sN2Pidsl3jhjNvzHYJfSkNG7NlXfaONP4B-rayoKq-FNm2ct2wxZAs8I4NrmFF6a4ZWE3swToW-1gY7Rp1z6pGLFJIFFnkMbeJQEke9lgcDw12IMhtKTHgJJjipGQQYxhNQqv-ojsWOWVpHjesBBbku-VBGfJb-Pw5NcMn_dJWlCgl_06j835vN3YOkqXX75EZHQFEy_zpC3oIp0EhH5_aMTkDljwoWAu7WD1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-Zq24j9Go2nCcPLf81BPx4qQJUbmSAvO4vfB5ksRGbflQ6xxJDjZLER_TXxf_QXagkEgPJIoF7Ka2I2A6w4iMqC69-h51oysTadTWgpPCSqIIVuEfU-dxIILiPPa4P-mZI-SO6w_GUy0fdeAdycebCd--GX0wLMi0FKqigLToOFj_8hCfQTs_U_yrLpDMZSiQKJE1qgA6gP735zPUJ8UcW0qUQi7aVLOMspnzIHpx2avBJhI9uRs_I44TzefG0k47yHJmJplb4j9kGTXD3DWr4kEXIIpvt7RaoHROWPfeCn3VC_4iYQ1wWwyYRzJpsRbWmU60XXxq1nFHr6qSpD2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر تازه خبرگزاری فرانسه از زمین‌لرزه‌های ونزوئلا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665181" target="_blank">📅 08:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665180">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84fa43fc.mp4?token=XZ-WZM12G3XUS22tyo9FEdIX2AEBaVTg7dQYtxlo4-EE_u01bJ11jdSDe_PGuJ7UqeBLT-UBEa2SOLV9FNV8cLsuMnBvUx9suyAn5VG4GnUKcke3WlUAa0Rb4tf8569anR5DGfyANB_wZYsRDTUPaZfPA5uacI4gwzcuYpohFgFG_34YAVhqA1gg9ecPW57W_9Gidc6-osyUucY9mQlpUuiVHI2G08M85lhN7CD_wFaHvhfHePTyDu8KE_kFb77bCG34GD1oWMtjdzoSG-Rzih59voGF6oWzkSQfeYjv0oqnCrCv6-mBFRaTeizFHk42V_AJd9U5XjABefZe9WlEEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84fa43fc.mp4?token=XZ-WZM12G3XUS22tyo9FEdIX2AEBaVTg7dQYtxlo4-EE_u01bJ11jdSDe_PGuJ7UqeBLT-UBEa2SOLV9FNV8cLsuMnBvUx9suyAn5VG4GnUKcke3WlUAa0Rb4tf8569anR5DGfyANB_wZYsRDTUPaZfPA5uacI4gwzcuYpohFgFG_34YAVhqA1gg9ecPW57W_9Gidc6-osyUucY9mQlpUuiVHI2G08M85lhN7CD_wFaHvhfHePTyDu8KE_kFb77bCG34GD1oWMtjdzoSG-Rzih59voGF6oWzkSQfeYjv0oqnCrCv6-mBFRaTeizFHk42V_AJd9U5XjABefZe9WlEEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب کنترل‌شده ساختمان ۱۶ طبقه آسیب‌دیده در جنوب ترکیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665180" target="_blank">📅 08:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حضور خداداد عزیزی در پرسپولیس منتفی شد.
🔹
ارتش پاکستان مدعی سرنگونی ۴ پهپاد متخاصم از مبدا افغانستان شد.
🔹
ادعای رئیس سیا: جنگ علیه ایران، جنگ فناوری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665179" target="_blank">📅 08:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665178">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH13wPmmX1QbAOLY6Brz6VtEq4-3vPL_ApJ03AuF2kmLxkSUAa394VQfvZNRHmTeMiABHLShN9AoBiG--AmtkQmZ2u_-khINWlQ9LS2R4oXF0ovPJWvj8ejVtqAkyHzRwHmyd930frM7dsrv6A2sTu98OXX43xtOe9-ifA37zFftXWPvr5zuhduDQBCBdmT1mwzNNz4fBGTcMoU7K_GvmHrN7jsyjx8LBi7rvE7aME6o57IXEhzd79kZhuIBBYY4Xdsa8F4_waYIp2_1E6xY9EvN_WHlSaY8rqikOtaVvBS3HbwNMeSUG3sNb2WzUxnEGQmaDm1YT7Lvv5NZC_MkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
۵ میلیون تماشاگر؛ رکورد تاریخی جام جهانی ۲۰۲۶
🔹
تعداد تماشاگران جام جهانی ۲۰۲۶ در دیدار فرانسه و سوئد از مرز ۵ میلیون نفر گذشت و رکورد تاریخی این رقابت‌ها را شکست.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/665178" target="_blank">📅 08:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665177">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ed4e62aa.mp4?token=lcwUJKXIoMuRoooqfhSccZKAaLIFl3GHvenEVDYqbBrDsyzg2vKcpBUNqvhkwQemxbK2L-CkP-p0jDPSrM5wFpZfVyNyqdUR0vv2i7LM5T-mC0l6zn24O1TRVOvtzJ01iS7sZiUOTm3vutIKJKBdxKLD7NbwzJGe2oKJ0MWN5HWHv6xe9rp2zduPXRXixGmi0ShMqybf53IfdIV3qcS5fwkxa3kG4q11_XAggh_zFIr6EayAa1isTxry9G7aTHIPu1k0hgI_6Qh6X2ifs7HYBfJJrNTRmeV_5fE9ZZ5W79iJ2mKoGLKVL6Q4giY6lq_f9R1j1cHLZO7_ok1QSr35HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ed4e62aa.mp4?token=lcwUJKXIoMuRoooqfhSccZKAaLIFl3GHvenEVDYqbBrDsyzg2vKcpBUNqvhkwQemxbK2L-CkP-p0jDPSrM5wFpZfVyNyqdUR0vv2i7LM5T-mC0l6zn24O1TRVOvtzJ01iS7sZiUOTm3vutIKJKBdxKLD7NbwzJGe2oKJ0MWN5HWHv6xe9rp2zduPXRXixGmi0ShMqybf53IfdIV3qcS5fwkxa3kG4q11_XAggh_zFIr6EayAa1isTxry9G7aTHIPu1k0hgI_6Qh6X2ifs7HYBfJJrNTRmeV_5fE9ZZ5W79iJ2mKoGLKVL6Q4giY6lq_f9R1j1cHLZO7_ok1QSr35HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرمای بی‌سابقه در آلمان؛ خیابان‌های برلین را با آب خنک می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/665177" target="_blank">📅 08:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665176">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHXsVWqaB0hgW3dNWAJfE83J3iQPQax4D10YGliI-kWewwMEgcQjeo6FMFOMes0kpPstvfcbWenUScxpCYkK5DuBv55rfGBeMH11ILvz21E-YCJ1YAonoRhS9xMqhPAr_n6z0mnwqjAmshRzfTsLBCwtuQkAw6gOq1raBMGnP2OgiuA4uRLWJjU6im_Hb8MzWBj8Hm_ai9Ud6-e2em9XykkPwf-tV9RpcL0ZjvI0_HodU34v_yxrtFkM7h2LCYMwq6n2N8ho-Kswwm3A89QP5qRFCf0N830DgYH4wbveSIEULVlHSiNE07Ky0--GkJwsYBhW6YVNLJk4K9wR3BL5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیزنکوت رسما نامزد نخست‌وزیری رژیم صهیونیستی شد
🔹
گادی آیزنکوت رئیس سابق ستاد ارتش رژیم صهیونیستی نامزدی خود را برای تصدی پست نخست‌وزیری این رژیم در انتخابات اکتبر آینده اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/665176" target="_blank">📅 08:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665175">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvY76xr4q__gkaMLCejzs_Q8ZmW_f2szspEuhfJILU3pcU6HeijsZlDEL05bpRF5CwoN0-bFQ8XujpKzz9zPh1prBs7dC4JKXHFi7WTIph--3S0gXXfFb_2gx8dwvB7FjgxLqlkgt4zBFbFBD2297GdZqwQ95Xu-ywGE1ZdC91Ga8AGcgqjZFNx6mmXukuiw3bDIINxH27zo38U-nzmOA_HQ8krpZ6v5b1KwwS82c-zVQNEoljMl4ABRA0INCSziBSTwXHJofdjewhXuWHmmSUlPJd_ijsTd48Y9KxYjDV4ldxOmbWJV2lKTJFVlZfJXrJ9R1Jijk0jC6hkGCYfjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یک پلیس در پی ترور ناجوانمردانه در سیب و سوران
مرکز اطلاع‌رسانی پلیس سیستان‌وبلوچستان:
🔹
ساعتی قبل افرادی مسلح به‌سمت مأمور انتظامی اهل سنت و از قوم بلوچ که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی کردند که ستوان‌سوم محمد پلنگی به شهادت رسید.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/665175" target="_blank">📅 08:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665174">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ff8a5c13.mp4?token=rnnKkEohLgGgTNPULr8FK0XuSFMwDYyMWZ9i1XkRMrvrCegirMKYNdPg8jbKHGeSURWSMrQtJtUu1p6zeLMN-ydAa06rAOrywpOHmWvnGAIrAqKTXr-N0b3nvvXkkUWcqnjq0i4AxAIuGWAiHhp758QQMRj4j5slrbbiWMO-jmfgr2FUkRPQWjJMDhtMmvraj4tI3PfqWv0DUm8hk_eHPevHqt6ZFfNifh52y9IMctRMiXSdgl_PJPdmQC4P2flUZ0sX47skkf1oEAJaMBD6uKPwDdpyHINhpSzeWJlISkB1nlXAGnWs0ai4Nk4OCd8kqoCvJC5raZBV5maBZfon1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ff8a5c13.mp4?token=rnnKkEohLgGgTNPULr8FK0XuSFMwDYyMWZ9i1XkRMrvrCegirMKYNdPg8jbKHGeSURWSMrQtJtUu1p6zeLMN-ydAa06rAOrywpOHmWvnGAIrAqKTXr-N0b3nvvXkkUWcqnjq0i4AxAIuGWAiHhp758QQMRj4j5slrbbiWMO-jmfgr2FUkRPQWjJMDhtMmvraj4tI3PfqWv0DUm8hk_eHPevHqt6ZFfNifh52y9IMctRMiXSdgl_PJPdmQC4P2flUZ0sX47skkf1oEAJaMBD6uKPwDdpyHINhpSzeWJlISkB1nlXAGnWs0ai4Nk4OCd8kqoCvJC5raZBV5maBZfon1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتشر شده از خالد مشعل درباره «شهادت سید مجتبی خامنه‌ای، رهبر معظم انقلاب» جعلی است
🔹
کلیپ منتسب به این سخنرانی که در فضای مجازی دست‌به‌دست شده، با استفاده از هوش مصنوعی دستکاری و تولید شده و واقعیت ندارد. بررسی‌ها نشان می‌دهد این ویدیو با هدف القای انگاره‌های نادرست درباره وضعیت رهبر معظم انقلاب منتشر شده است.
🔹
ابزارهای جدید هوش مصنوعی امکان تولید ویدیوهایی با شباهت بالا به واقعیت را فراهم کرده‌اند؛ به‌گونه‌ای که ممکن است مخاطب عادی را دچار خطا کند. ویدیوی مورد اشاره نیز در همین چارچوب، بخشی از جریان انتشار محتوای جعلی و عملیات رسانه‌ای در بستر شبکه‌های اجتماعی ارزیابی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/665174" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
مرکز رسانه مجلس: بخش‌های حذف‌شده شامل موضوعاتی مانند ادعای بازرسی آژانس، اموال بلوکه‌شده، بازسازی، اظهارات ترامپ و پیام رهبر انقلاب بوده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/665173" target="_blank">📅 08:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665171">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aedbee200.mp4?token=OrEk8xwhMzN37fbyvUFAnjW1vjMj5giJOMGSwShZPAszbQvPTB7RJXLQU6jGSAfuEoRY8M1SLVPmIvSAXth_Zbmiy3k35CR2npszTQgaOXLKytbHEyp02DeacpVSOIOJ93epYMtiLJCqv71wmRVwwpwsEJp1pd9OSOuDbJ-_NPi4r1lUURbY0QelbMAuuTpvpUhgPkXAuCsf6a27upy565IGnSSjt5BgpPEbGNhbF5rpJffVA2a2JOhr10WOl-qRLzRfugYf-9EELEhOYIw4VN-ON0bjmIHUmcUeaPXXso_A7ti5dSIbyCvh94MxJEV2KId9_2zKFRI8GV-x9vid0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aedbee200.mp4?token=OrEk8xwhMzN37fbyvUFAnjW1vjMj5giJOMGSwShZPAszbQvPTB7RJXLQU6jGSAfuEoRY8M1SLVPmIvSAXth_Zbmiy3k35CR2npszTQgaOXLKytbHEyp02DeacpVSOIOJ93epYMtiLJCqv71wmRVwwpwsEJp1pd9OSOuDbJ-_NPi4r1lUURbY0QelbMAuuTpvpUhgPkXAuCsf6a27upy565IGnSSjt5BgpPEbGNhbF5rpJffVA2a2JOhr10WOl-qRLzRfugYf-9EELEhOYIw4VN-ON0bjmIHUmcUeaPXXso_A7ti5dSIbyCvh94MxJEV2KId9_2zKFRI8GV-x9vid0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر میخوای بدون خوردن قهوه صبحگاهی، کلی انرژی بگیری و تمام روز شارژ باشی، این فیلم رو از دست نده
😃
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665171" target="_blank">📅 08:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665170">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrGm9X0UBIYBLV75kxMlYHPks-NB4GhI3D1Z1V3hPqySbaPA5lr4HKcInHvhnQxApMUHqWY1tfUKZyZkYNmO4FxpSIKoIfFOzDQBFe8eKKXYUGbeqoa2cHEApYyhkvoQnhXMkUKldOSbypeWEruiYlj8b6q5bPcHaFfykej-kPnYiAuZb2V0RAeZ-lEx04_WYYTtIhrZJV_uLaSnmEv_Rc74AgA2eq6FZu-AMcgYlAGxnHGZ076aW9BGnXjpLDnXHd5BZMdGhya6jAawDLsHpnEcFNK5rAlaQdfoMqP-9JLqcp8a5ERCqEN8SwiiO7363dLIg4oby5HOz-7Oika81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پس از بازگشت به کاخ سفید دست‌کم ۲ میلیارد دلار درآمد کسب کرد
نیویورک تایمز:
🔹
دونالد ترامپ
پس از بازگشت به کاخ سفید نه تنها فعالیت‌های تجاری خود را محدود نکرده، بلکه دامنه آن‌ها را گسترش داده است؛ اقدامی که به گفته منتقدان، پرسش‌هایی جدی درباره تعارض منافع و مرز میان قدرت سیاسی و منافع اقتصادی شخصی ایجاد کرده و از این منظر در تاریخ ریاست‌جمهوری آمریکا بی‌سابقه توصیف شده است./ شفقنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/665170" target="_blank">📅 07:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665169">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwfPKTxs2lUFXq0hWfzXWs5FnfwZw9NRFyOztnuBjOelU3AxP0oL8JW8Hh3eH9ZwlBNa8zD7Rh6tSRU-mWcaczRzwwKm7gFfo7zTNE65YwniTn-NCGkSZqYuBB907u9gVs9wj0zBFbc0P_bvISGvJVgO9wplhQnGzpnu7k0lsjYlq6c4ju6E7Kpu-WWOs1AOyKZs04_Bnx_vPOzeJGMvayi6txksv7TU4uFyf07IgfbBv9C6nmb7EYfZE6Cxhe_ztHZ9Fa0JhZbIEFXybyRpGcfO3AGMje8fyuUTXBjlc-JLRwkeiyRgHOQ0_kJMeiw3IeWMygZjYyAvRoDerbxsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدیدترین بروزرسانی نمودار مرحله حذفی جام جهانی ۲٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/665169" target="_blank">📅 07:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665168">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb2f02597.mp4?token=TMY6B_Wtn5SuAqz3kZqgM2o1AAzILALhjcH5BJqC-qcq4csbmyPnqmn_7dXFWxTKfcxYUUA4Xb260KGvb4oVSigiWx7DbQQUVDeI1D3vFLzB-CF9xuaWvORTvtHrFRpipbh6TSGSXmQkPkn8j4u7iiFdQyWUlFGXykxMoGvfQmmCGm-AP6ifdVasBlHRdwTQRp1dwPSpCJKihwg72ypVDQRmZeR1RxqxksphpSu9dbhqJhuDqCtMGqkvZYAgYKAsbfgJDQMELXCmQN4GuAFvudJvN8mhkbQWf3J9fk25sZgQRtq--f_BMgJMJ9VVh91zU5jXReCpqNbtqPjK49tzQgWSPI6oShJa5oBq2i-EoCcLNUkb7Nh7u1dSQNmNFO6itKu3dsf2Hxbtg-shi_UcVv_xXHEGD8GE8MUu7B0ZKVClRBFKdhW3I_2PYSdDJWMUgTTfpixrDNrviDKQuwEcO5ZWLgBNSI0AcoAOsUKeJDvUxYVALhBrB_CbULxAo4mlh4hUmDM2OWJJ4PuN9V8wdTYZlPPKbjG4mt5GvnDUN4hBidJWPFb-qkv40v0zR3Ztu-s3XHNprVkMHWK28o_decDpxesGBsZyRkDvvxE7PATnhR5BNpm6_Awp_W2wmuZX8SPXv5pwYy2HtNolVvMzx4gSEDG93KRlO7G9cMvV-2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb2f02597.mp4?token=TMY6B_Wtn5SuAqz3kZqgM2o1AAzILALhjcH5BJqC-qcq4csbmyPnqmn_7dXFWxTKfcxYUUA4Xb260KGvb4oVSigiWx7DbQQUVDeI1D3vFLzB-CF9xuaWvORTvtHrFRpipbh6TSGSXmQkPkn8j4u7iiFdQyWUlFGXykxMoGvfQmmCGm-AP6ifdVasBlHRdwTQRp1dwPSpCJKihwg72ypVDQRmZeR1RxqxksphpSu9dbhqJhuDqCtMGqkvZYAgYKAsbfgJDQMELXCmQN4GuAFvudJvN8mhkbQWf3J9fk25sZgQRtq--f_BMgJMJ9VVh91zU5jXReCpqNbtqPjK49tzQgWSPI6oShJa5oBq2i-EoCcLNUkb7Nh7u1dSQNmNFO6itKu3dsf2Hxbtg-shi_UcVv_xXHEGD8GE8MUu7B0ZKVClRBFKdhW3I_2PYSdDJWMUgTTfpixrDNrviDKQuwEcO5ZWLgBNSI0AcoAOsUKeJDvUxYVALhBrB_CbULxAo4mlh4hUmDM2OWJJ4PuN9V8wdTYZlPPKbjG4mt5GvnDUN4hBidJWPFb-qkv40v0zR3Ztu-s3XHNprVkMHWK28o_decDpxesGBsZyRkDvvxE7PATnhR5BNpm6_Awp_W2wmuZX8SPXv5pwYy2HtNolVvMzx4gSEDG93KRlO7G9cMvV-2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبروریزی در صحن علنی کنست رژیم صهیونیستی؛ نتانیاهو اصلا قادر به خلع سلاح و مقابله با حزب‌الله نیست!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/665168" target="_blank">📅 07:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665167">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCEnFSXe1TU-sE8N5M6WgbyuUbAK8nl6hclNtuRs_UMWir1wSbvonb68YD1gTt_dH0aLQwHeY1fpBos8owO9fVWoCQczoK-J8euTA2ImZHApfNRPAo0xmrrEvWnhzB5cDC2eev0LEHq5MdBxJ65U3-kbm2_3JZOdA7rZReFCW8ekC1q1lioLSoiwfYzYZ_8CZEVmCYKRHFr6olfTdOQ7BZpNqIH4qSau0CtT3FWq7g6Y-G7AQI3-A7SwTV7gqwAMLEmN0c3my-OYY8NkpMQLowty6FmnQtbneMNWXyV6n8Kg50ip6GGllVqZMUEM_SLxusoPcSOb221xUtgQckoRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کیلیان امباپه با ۱۰ گل، رکورددار گلزنی در مرحله حذفی جام جهانی شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/665167" target="_blank">📅 07:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665166">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjM_DYGgH81y-3OcrFu3f7U8NEC5F9rWjui5yLpH1Khu_s1Wlf6eaYQVqG-Ydb8a1lq2XrufaOrzVahMxjGs9Nxu62oatlcxlUMy3EogVLuJ7C5-OsM-gr9sKNAReC5ACzg1Xn53Wn_9FD_z3-rT4PHq0FommsEshzDmFsG_9SkhXfNLnWy2uz593UzkacO2VdeIcUN3C2Peu8chNhlNA9bRA-z25oq89WAlwxLqW-144K6J15vRzCwgTOz4GqT2cncSSiCam3lv6SGUHVuVGgM-idza9v8AokyKogJl9kWVH4AY2KQ6nYsYoDvk8LfkvXRegBiSsyrbUowc0PGK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه صهیونیستی: کشورهای خلیج فارس به ایران نزدیک‌تر می‌شوند
🔹
گزارش یک رسانه اسرائیلی بیان می‌کند که کشورهای خلیج فارس پس از جنگ با ایران، با تقویت گفت وگو با تهران و اتخاذ موضعی محتاطانه‌تر نسبت به اسرائیل، در حال تغییر موضع خود هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/665166" target="_blank">📅 07:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665165">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StyLVfkVWUZyDY2Td-Yvo-gQ5RY38vVGFE4dqQ7mmycRkqd27RknEgrb0dtSGJY3NkQZcKuJJVdZr99tS84tcsMEA6ahoE8vhwin8GZbbrrq5PnK_8J2dVmMD2kU6yu1UgsCBjBwAr5NwzO7b6r4hALzAnSUBtPKagLJ68d6ryGVybz_YED5T2PSTHm9xekbKBjPo8db2mH3OVnx9SSk4K0zTLWCe-uNPL4faOPdF_Jrsr2urdVVIWb0jKVVzbWiZ00Fy1gxFcWq9mMpyhtnGg1kICyoW9_yLUlEIBSJzBnv2Yqj5m2DKQaG87XdL7KoUMphRBFxj6H7xEAZ3j5TJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۰ تیر ماه
۱۶ محرم ۱۴۴۸
۱ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/665165" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0riwx0AhSVM1IrEpJugjgW8MomccLkMt1x7HM8qA2VR8aMKAhO5ZqsNEhXcUNIrWQPkBJgzJy2Vp8YM2NOIlBJ9s0-dikfBhSLQE8LadWr-HnmKOAN9u75T2-A2YFPhzmdCtKVR3uzh3WCeumvCv3yBYYfbTmu0NfeL684l2p5LntrlI_rkxO_wsN7ix-cgdwi5QT8eup8DrRMQ51zRSvYX6X1tat7NBPxdClJj4i6yZeYdtSURv6xn6XL4Mm-9CeeLxJwhER5ikkWCvGm5hsVBus8hWj9J4dX6i73n9xJNIsN0A5VWAVLtdBiORsL-kbHHCQbK7oU51DOYsxoAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
طلای آنلاین، بدون دردسر
خرید و فروش طلا دیگر نیازی به نگهداری فیزیکی و دغدغه‌های همیشگی آن ندارد.
سرمایه‌گذاری روی طلا، ساده‌تر و در دسترس‌تر از همیشه.
🔰
خرید و فروش آنلاین طلا
🔰
بدون دغدغه نگهداری فیزیکی
🔰
شروع سرمایه‌گذاری از مبالغ کم
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#طلای_آنلاین
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
اینستاگرام کارینکس
|
لینکدین
|
تلگرام
|
وبسایت
|
اینستاگرام آکادمی</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/akhbarefori/665164" target="_blank">📅 01:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
وزارت خارجه قطر: نخست‌وزیر و وزیر امور خارجه این کشور در دیدار با «ویتکاف» و «کوشنر»، آخرین تحولات مربوط به مذاکرات میان واشنگتن و تهران را مورد بحث و بررسی قرار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/akhbarefori/665163" target="_blank">📅 01:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9789db7080.mp4?token=pRLVfv6KvZvBU5JyeYtxCLie1DWIoWsdQQnKGS0VniYlgj82Zv3zfultcMPk9QORHjaZ8Sopgsm-LG3EF54is1W1lvLwuJYTFIaB3Vkn5flVQwz1zgCYoxwlyEEStSsdUzPYUBFKSv1svPqcv_Ydee1HkPeQwUXedqs_bwPOl2J-bV-4Z8oBcu_aEH8LZo810EHoTxYy0ANb9azIgxiIPebrT8_Pw-r633wk2TiO3qN6ht3OtEkOCErP4I6D0IBvFTLWNU7PWL9CP_KkVfKk4T6G3iUPnQw74X-qZfLXPf2WHmGSoqOW15wb1S3OdSnofY58KwtPTuBJOIEsfsqUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9789db7080.mp4?token=pRLVfv6KvZvBU5JyeYtxCLie1DWIoWsdQQnKGS0VniYlgj82Zv3zfultcMPk9QORHjaZ8Sopgsm-LG3EF54is1W1lvLwuJYTFIaB3Vkn5flVQwz1zgCYoxwlyEEStSsdUzPYUBFKSv1svPqcv_Ydee1HkPeQwUXedqs_bwPOl2J-bV-4Z8oBcu_aEH8LZo810EHoTxYy0ANb9azIgxiIPebrT8_Pw-r633wk2TiO3qN6ht3OtEkOCErP4I6D0IBvFTLWNU7PWL9CP_KkVfKk4T6G3iUPnQw74X-qZfLXPf2WHmGSoqOW15wb1S3OdSnofY58KwtPTuBJOIEsfsqUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به سوئد توسط امباپه
🇫🇷
1️⃣
🏆
0️⃣
🇸🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/akhbarefori/665162" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4d30836a.mp4?token=JOYKMSbd0AlCa-ijNsdhN_6bGGvvPeljrdoUqwD05tR_WnAoP0lDvRZeB6-ftnVcJTV8TZp8WMQmEGqQSWPt_bVN6370v6t5MZLuPYQ12-6jronVSneJOWP7T_xvrksErSWnbwXYOzpRmlty-SJAD9DdRtxH07funOFwBzwgkWLqNSpirulOjtetHMOGrLxffig1Xn9L_N6nPyX6s27lh0dfTg-Qf9bqWZkQqcZrfAqvHhvQY9a5WByfllXmMSFPzGiDhX026IgdkR57w0XkMkrxHTVL697qhitiD5fB2kr_ZKy4jewbNgzWFAtae53ReLAUyn84qxpgzOV7x7kE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4d30836a.mp4?token=JOYKMSbd0AlCa-ijNsdhN_6bGGvvPeljrdoUqwD05tR_WnAoP0lDvRZeB6-ftnVcJTV8TZp8WMQmEGqQSWPt_bVN6370v6t5MZLuPYQ12-6jronVSneJOWP7T_xvrksErSWnbwXYOzpRmlty-SJAD9DdRtxH07funOFwBzwgkWLqNSpirulOjtetHMOGrLxffig1Xn9L_N6nPyX6s27lh0dfTg-Qf9bqWZkQqcZrfAqvHhvQY9a5WByfllXmMSFPzGiDhX026IgdkR57w0XkMkrxHTVL697qhitiD5fB2kr_ZKy4jewbNgzWFAtae53ReLAUyn84qxpgzOV7x7kE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایتکار افراطی اسرائیل: آماده‌ایم شمال غزه را غصب کنیم، شهرک‌های صهیونیستی بسازیم! فقط نتانیاهو بگوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/665161" target="_blank">📅 01:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665160">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
صداوسیما با قطع برنامه گزارش قالیباف درباره اجرای بندهای تفاهم، به‌جای فراهم کردن بستر پاسخ‌گویی، مانع آن شد   روزنامه خراسان:
🔹
قالیباف اگر سکوت کند، متهم می‌شود به پنهان‌کاری، اگر بخواهد گزارش دهد، صداوسیما ترمز پخش را می‌کشد. صداوسیما باید روشن بگوید،…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/665160" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آستان حضرت عبدالعظیم(ع): حرم از ۱۱ تا ۱۵ تیر شبانه‌روزی پذیرای زائران است.
🔹
استاندار تهران: تهران از نظر امنیتی در وضعیت بسیار مطلوبی قرار دارد.
🔹
وزیر پیشین رژیم صهیونیستی: الجولانی تروریست کت‌وشلواری است!
🔹
رونالد کومان از سرمربیگری تیم ملی هلند استعفا داد
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/665159" target="_blank">📅 00:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665157">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
عصبانیت صداوسیما از افشاگری قالیباف درمورد توافق خاص دولت قبل با آمریکا
🔹
صداوسیما زمانی مصاحبه قالیباف را قطع کرد که او در حال اشاره به توافق ناکام با آمریکا برای انتقال ۶ میلیارد دلار پول ایران از کره به قطر برای مصارف بشردوستانه (غذا و دارو) بود.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/665157" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665156">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh7FttZ1pCCXrn2zFq9pradg-QJRjh63zIALo9LnJEiAqsTu3M0M-_ujgHNjpP_gnMLOnLd3z-phYqi7N_ljZ2GFqh60KzEAmwn3qGkuSAq4XnSdITNtwBxFvf6toliBMmMRxE7CdfzHIK_3k-WTNUdU9Nxat8i4yJYFjPB59mTM0vxdRd0UvkdapqooQpKhm-q-2fJiZZJpM3wCU_T9oY78pHl8WKmWaERWPeGm18wGPeZTX5O7SIiWeWYyFRJGkAWKX-M_Ikc5NgD_lQs9YWWnjikvyUzsTGcoys_GuI1IoiMD6cfx3MW3HNYTcMEb8DWeZKk9EBncnT3GODw2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر امام شهیدمان تا کنون نه به خاک سپرده شده و نه به ودیعه دفن شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/665156" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665155">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رئیس‌جمهور ترکیه، اردوغان: آنچه در غزه رخ داده یک نسل‌کشی است و اسرائیل قطعاً بابت کشتار کودکان و غیرنظامیان پاسخگو خواهد شد؛ ما نمی‌توانیم در برابر این جنایت سکوت کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/665155" target="_blank">📅 00:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665154">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5feed3638f.mp4?token=CVttPJ8hUpN52toQEAccE2CvPkDbo1D_Wler0elXlRvaiVKbCqne3nJaXIBUwXOo070txbnX77PdlqxV-YsOzoH6SQ1F2xvbtlDIQuy1qEy3CWwIf_lgQN5iIszbMIX0TMshbJnYv7ujAYOZN1t-Y7vawknmE9b3mR4vL_Y2BW83DQzBQqQUvnECVU6D4IrQrAD_Kp_T0bgm_XmxL4W2FYut5TT4ekY91ODMs--I4jWdoEgnLbKjpzYckCk3ptpK3ignCVU4aStCUeYvj_MefsBJZZDcClOqzXsjyRe7mkS0d8kylDEz12iZQI_wWf8_kMjR6421LUdXT39FhPFrYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5feed3638f.mp4?token=CVttPJ8hUpN52toQEAccE2CvPkDbo1D_Wler0elXlRvaiVKbCqne3nJaXIBUwXOo070txbnX77PdlqxV-YsOzoH6SQ1F2xvbtlDIQuy1qEy3CWwIf_lgQN5iIszbMIX0TMshbJnYv7ujAYOZN1t-Y7vawknmE9b3mR4vL_Y2BW83DQzBQqQUvnECVU6D4IrQrAD_Kp_T0bgm_XmxL4W2FYut5TT4ekY91ODMs--I4jWdoEgnLbKjpzYckCk3ptpK3ignCVU4aStCUeYvj_MefsBJZZDcClOqzXsjyRe7mkS0d8kylDEz12iZQI_wWf8_kMjR6421LUdXT39FhPFrYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: کمک‌های آمریکا را نمی‌خواهیم؛ می‌توانیم خودمان تأمینش کنیم
🔹
کمک‌های آمریکا را نمی‌خواهیم و می‌توانیم خودمان تأمین مالی کنیم؛ روند قطع این حمایت‌ها باید امسال آغاز شود.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/akhbarefori/665154" target="_blank">📅 00:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665153">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
دبیرکل سازمان بین‌المللی دریانوردی به الجزیره: هیچ قاعده‌ای وجود ندارد که به هیچ کشوری اجازه دهد بر تنگه‌های دریانوردی بین‌المللی عوارض وضع کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/665153" target="_blank">📅 00:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665152">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25696b8476.mp4?token=JX8OnDDgN0DthG_acn6EOQ68aK0_Tj5KfTQQslZ9tXgP3aJqqe49IH0irHD9jd3rPcFgk3ahv_CjU_d3H7OsPT_w3AgQrGIzQhb7inzEKffKU0ix6UuzVDwKRLHnvLI_-uWVmmu61AFG_m5WwG6TvF26C_pJbrY-OHxwTNbW0pyGgbTzi3p0hYw0nz5Eti4j676scJ95eXAJMZrgfVMysH_2RFo5zG8p2Q4oycTAzCJGn5jWujbMgIIuE6qDgAQ3NzSG4q-5EcribMpcBphEN2G_N7oCZt40h3qsVzDWIsE1auGbe_x7_8I4wdycJdKSbLZ54ZAvgQSN-x0-h1KusA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25696b8476.mp4?token=JX8OnDDgN0DthG_acn6EOQ68aK0_Tj5KfTQQslZ9tXgP3aJqqe49IH0irHD9jd3rPcFgk3ahv_CjU_d3H7OsPT_w3AgQrGIzQhb7inzEKffKU0ix6UuzVDwKRLHnvLI_-uWVmmu61AFG_m5WwG6TvF26C_pJbrY-OHxwTNbW0pyGgbTzi3p0hYw0nz5Eti4j676scJ95eXAJMZrgfVMysH_2RFo5zG8p2Q4oycTAzCJGn5jWujbMgIIuE6qDgAQ3NzSG4q-5EcribMpcBphEN2G_N7oCZt40h3qsVzDWIsE1auGbe_x7_8I4wdycJdKSbLZ54ZAvgQSN-x0-h1KusA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنرانی جنجالی مدیر تلگرام درباره نظارت جهانی و حریم خصوصی؛
کاربران در دنیای امروز عملاً بدون حریم خصوصی هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/akhbarefori/665152" target="_blank">📅 00:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665151">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b76af2785.mp4?token=aLuFjvRs3XWqO8C5gGwHBQ-SqdPXvH-nXSv2hkLjl6hL6_vU6m9VGCFPQ7aSWmEyUcmd7csJdE2-McNZRUsvTSoNxWEPJmkP3n4uJimOzgLnyrXLmYN1tCb9JeyEoRpO7QicVJYEZ_J7-FDkrjbMM2wjsF17-CRGK0GOS_hP6wXGJem7xDwzCd-m39jBayWu0jTWBNsgsl73QVvM8iF03k7F46KyvpNGqnemt13-wHgQCLQC-o8ClzsP0foQyND9P2npx_8pHy3jZluA9E50PTQ9Tguw-CJjTSkCflySpc6gd5lkGl6lKQc5sFhNSjgRIk6YCoo1LOfBEZ523c2toypBe9QmXxgmOGpZilQmYY8DdMg5kNIiUX-A57wTIUh2RWMhUsuOiP2BKpkuyaLQlfC6rvpydwmi64zRL2rlR-TFMuQ_IEGhvQ9h5J9spI8NZrhcik3czXrXdYQv5UJF8LiICf2BOhGvF4bbFd-5a9AMzQvGNVf-z0sjHg8zLPEbqZpBB3PIMTwTo6LG06uyAcskWjEzTYtgEFvQuaeP1vro5215bnm9xWVWtjo8zHt0P_dV-S25vMvliBQ5cm9Rt7vltzigbTaF3P5ouldlw4xGJguw4UPrkmhD4JJZEXjtsdN6Bra_Rt2OSAJ720Z7-QxG-CN3t8RD047UQIBjPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b76af2785.mp4?token=aLuFjvRs3XWqO8C5gGwHBQ-SqdPXvH-nXSv2hkLjl6hL6_vU6m9VGCFPQ7aSWmEyUcmd7csJdE2-McNZRUsvTSoNxWEPJmkP3n4uJimOzgLnyrXLmYN1tCb9JeyEoRpO7QicVJYEZ_J7-FDkrjbMM2wjsF17-CRGK0GOS_hP6wXGJem7xDwzCd-m39jBayWu0jTWBNsgsl73QVvM8iF03k7F46KyvpNGqnemt13-wHgQCLQC-o8ClzsP0foQyND9P2npx_8pHy3jZluA9E50PTQ9Tguw-CJjTSkCflySpc6gd5lkGl6lKQc5sFhNSjgRIk6YCoo1LOfBEZ523c2toypBe9QmXxgmOGpZilQmYY8DdMg5kNIiUX-A57wTIUh2RWMhUsuOiP2BKpkuyaLQlfC6rvpydwmi64zRL2rlR-TFMuQ_IEGhvQ9h5J9spI8NZrhcik3czXrXdYQv5UJF8LiICf2BOhGvF4bbFd-5a9AMzQvGNVf-z0sjHg8zLPEbqZpBB3PIMTwTo6LG06uyAcskWjEzTYtgEFvQuaeP1vro5215bnm9xWVWtjo8zHt0P_dV-S25vMvliBQ5cm9Rt7vltzigbTaF3P5ouldlw4xGJguw4UPrkmhD4JJZEXjtsdN6Bra_Rt2OSAJ720Z7-QxG-CN3t8RD047UQIBjPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بازیکنان تیم ملی بعد از جام جهانی رفتن مرکز خرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/665151" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665150">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون ترامپ: ایده دریافت عوارض از کشتی‌های عبوری در تنگه هرمز «بی‌نتیجه» خواهد بود.
🔹
نتانیاهو: رابطه‌ام با ترامپ «خوب» است اما اختلاف‌نظرهایی وجود دارد.
🔹
مقام یمنی: اجازه ادامه محاصره کشورش از سوی عربستان را نخواهند داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/665150" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665149">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMHqyD3nxrGa6ukHCdw1bNo6oMShL4QkoMQMf6NcPRwE4G4kEN95X488po-0AMEiDzbGebrrEBQVV0mTi95QxoKZOoCbs7EW-ovQeJxFsnRhaYPiHWisXUMK3pGV4mSaj2VGlFoNR3Yhp-MQy1srE8v2WP_9DYQmsBDMdqWqBSAyp_KoppNRCB8zbdZ5A6Z3mNt1xmO0_4Kxc5RX7cVGVmsi-wSbYSes3K91jQQDN2FyZEef1-jc7FvA2DwfMZTsi-dy5-_-QxrXcRHikV6g7yO-IJwusel17GDZNzEjGrTKg-ExH6QvLSq_kr4wa_98ZOwKbNDVpYBiMFDCtLPWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/665149" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665148">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6276572559.mp4?token=PWTvIuGPdRDGvnfHNubwf1YzeiDbAMLUocwfqgkeUT1yk6sit4WWn2aEw3zLBMg0QF4tvFQxUwNcjtCQtzx1MqL-bg74aaT-WvcGp5nxfG9TTrQF7RDwGRtLPxgEMHIIz7xWsqQsRMfHePgCYhGurfqn5PrM2BMEjazKDMaC8A-kkccdaeLxV6kXErbc6tkro-QNneLLJQ_w1T8cpv4pnOA4sLTUTYohilg64_xAVNx25qmpjJ5epi3gi4_31GpLuTaVH4-Q5uEs8SaIzAVoD_i9ZANHStUJpj3KLVvkW8OkvE-zyCqJ0eNd2CqK3ZfQBTjiHtap5WQuygeIxnCl7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6276572559.mp4?token=PWTvIuGPdRDGvnfHNubwf1YzeiDbAMLUocwfqgkeUT1yk6sit4WWn2aEw3zLBMg0QF4tvFQxUwNcjtCQtzx1MqL-bg74aaT-WvcGp5nxfG9TTrQF7RDwGRtLPxgEMHIIz7xWsqQsRMfHePgCYhGurfqn5PrM2BMEjazKDMaC8A-kkccdaeLxV6kXErbc6tkro-QNneLLJQ_w1T8cpv4pnOA4sLTUTYohilg64_xAVNx25qmpjJ5epi3gi4_31GpLuTaVH4-Q5uEs8SaIzAVoD_i9ZANHStUJpj3KLVvkW8OkvE-zyCqJ0eNd2CqK3ZfQBTjiHtap5WQuygeIxnCl7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس پلیس راهور در برنامه پرچمدار: هیچ وسیله نقلیه‌ای حتی دوچرخه حق ورود به نزدیکی مراسم تشییع رهبر شهید انقلاب در تهران را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/665148" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
چه کسانی در شورای عالی امنیت ملی به تفاهم نامه ایران و آمریکا رای مثبت دادند؟
👇
khabarfoori.com/fa/tiny/news-3226858
🔹
پایان برنامه‌ رسمی مقتل رهبر شهید در نزدیکی بیت در پی تحصن تفرقه‌انگیز یک کاروان که از خارج تهران آمده
👇
khabarfoori.com/fa/tiny/news-3226744
🔹
ضرب‌الاجل دولت عراق به گروه‌های مسلح نزدیک به ایران برای خلع سلاح
👇
khabarfoori.com/fa/tiny/news-3226770
🔹
پیشنهاد بی شرمانه تهیه کننده متاهل به بیتا سحرخیز در حضور همسرش
👇
khabarfoori.com/fa/tiny/news-3226967
🔹
کشف لباس زیر زنانه طلا در بازرسی از خانه نماینده پارلمان عراق/ عکس
👇
khabarfoori.com/fa/tiny/news-3226863
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/665147" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9275accc3b.mp4?token=pnq0IALwofjDymRlRL7Ng5uR2JgRWaV8vxbtd5Vo0cklzSDnHMXm9Aj9CoZjepKe3fSqWylUNg8SxFGPgV8HV6NfWas9AIuy3mTftEDjiw5uVLcoYEf-NcIwg-7JRpXMMuBTxZgH76QmIr21t91LS8qXRjzwse2JY4OE65sD3CMGuovb0YeDUPNETAfuucocnclc3P8XguUOrHXRITbJ7rpJQ9wklzQqCUQPK8VZeSwkDhU9-8ylatXgP5Y5aD7m-Q4vXVERI-3JxEtEikfwh7Rz5JW7c6TauJ0M1gl9B5vyy88xYz_OB7K08iHxetmeveEbc9QDSwuZg4m5IvT3Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9275accc3b.mp4?token=pnq0IALwofjDymRlRL7Ng5uR2JgRWaV8vxbtd5Vo0cklzSDnHMXm9Aj9CoZjepKe3fSqWylUNg8SxFGPgV8HV6NfWas9AIuy3mTftEDjiw5uVLcoYEf-NcIwg-7JRpXMMuBTxZgH76QmIr21t91LS8qXRjzwse2JY4OE65sD3CMGuovb0YeDUPNETAfuucocnclc3P8XguUOrHXRITbJ7rpJQ9wklzQqCUQPK8VZeSwkDhU9-8ylatXgP5Y5aD7m-Q4vXVERI-3JxEtEikfwh7Rz5JW7c6TauJ0M1gl9B5vyy88xYz_OB7K08iHxetmeveEbc9QDSwuZg4m5IvT3Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: دو بار اقداماتی در ارتباط با ایران انجام داده‌ایم؛ احتمال تکرار وجود دارد
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/665146" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
قطع ناگهانی مصاحبه قالیباف در صداوسیما
🔹
پخش مصاحبه قالیباف از شبکه خبر درحالی امشب ناگهان قطع شد که شنیده شده یکی از مدیران صداوسیما که قبلا و در پی مصاحبه جنجالی نبویان استعفا کرده و رفته بود، امروز مجددا به کار بازگشته است./ جماران
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/665145" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665144">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137315edac.mp4?token=ol0dlbDSLX-QK0U375EKjNjEc-gv8dGOYJGm5CS8f5BfuIsw38Sm4iClV5W1W7_Dc6YjrWG2dG87-CZw3ZFWx_wEnbqcBpjHcJRp3qyvI30xrnwygyoVLCcXrF-YWGYmWuTJXTKRSzunymfOppJREtveikh51Vg9MQlJh47xyCI1SEmatalmFq1TtZxATH4LY7BgxxzN9giblRm23c1XbhbFoY0n3eD3nQMurRO8AsBOg3aaf0Tgcs7W1odBUAeqLxTdbg6pZ8CmU3spPYj7yN3s2nFGQdztSaNLpOUoH0ZmPgkxX-uRAy4bfEHioUjeI8MRZaT0PiUy0Glhm1gONg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137315edac.mp4?token=ol0dlbDSLX-QK0U375EKjNjEc-gv8dGOYJGm5CS8f5BfuIsw38Sm4iClV5W1W7_Dc6YjrWG2dG87-CZw3ZFWx_wEnbqcBpjHcJRp3qyvI30xrnwygyoVLCcXrF-YWGYmWuTJXTKRSzunymfOppJREtveikh51Vg9MQlJh47xyCI1SEmatalmFq1TtZxATH4LY7BgxxzN9giblRm23c1XbhbFoY0n3eD3nQMurRO8AsBOg3aaf0Tgcs7W1odBUAeqLxTdbg6pZ8CmU3spPYj7yN3s2nFGQdztSaNLpOUoH0ZmPgkxX-uRAy4bfEHioUjeI8MRZaT0PiUy0Glhm1gONg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این بار هوش مصنوعی زودتر از انسان واکنش نشان داد؛ عملکرد تحسین‌برانگیز تسلا مقابل آمبولانس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/665144" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665143">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ونس: تاکتیک مذاکره ایرانی را درک نمی‌کنم
🔹
ما خواهان تعهدات پایدار هستیم که قابل‌تأیید باشند و با بازرسی‌هایی پشتیبانی بشن که ایران، کل کشورش رو از سلاح هسته‌ای پاک می‌کنه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/665143" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665142">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f386220b.mp4?token=UH08RvY1Y8pg7uwlgBzPBPRs5U54IV89vuGSjJOvMGtRzKpAMcPz_aGFb9IFri3NhztLDB4uuwaI9VphOZRLxCTCG2VMqGQWB26izyhzBYCe5JorrGHsI9V9O067_qAzGdHFgt5jtVNKy_IjoJWIdbB5Sl0bHm1lMk-QF3FoySj6CVOvtJhccjK4DDzJhNBh8m3S8N_WgF00ICREA2kx8wM7HEb411TWSjJh7iuhiHRYH0n9Gz_drjJf_OrW-vfGsxAqVnoYj3QBXwIiJvLtbKk41sSTWIobnxFej_P-y9G2NZg7rsiaQRXwTF_W0GftlAWENy7Zs6jZXSbvzTyXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f386220b.mp4?token=UH08RvY1Y8pg7uwlgBzPBPRs5U54IV89vuGSjJOvMGtRzKpAMcPz_aGFb9IFri3NhztLDB4uuwaI9VphOZRLxCTCG2VMqGQWB26izyhzBYCe5JorrGHsI9V9O067_qAzGdHFgt5jtVNKy_IjoJWIdbB5Sl0bHm1lMk-QF3FoySj6CVOvtJhccjK4DDzJhNBh8m3S8N_WgF00ICREA2kx8wM7HEb411TWSjJh7iuhiHRYH0n9Gz_drjJf_OrW-vfGsxAqVnoYj3QBXwIiJvLtbKk41sSTWIobnxFej_P-y9G2NZg7rsiaQRXwTF_W0GftlAWENy7Zs6jZXSbvzTyXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری پس از خروج قطار از ریل در آمریکا
🔹
یک قطار در نزدیکی منطقه «فیسترول» در ایالت پنسیلوانیا از ریل خارج شد که به دلیل نگرانی از نوع محموله، وضعیت اضطراری اعلام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/665142" target="_blank">📅 23:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7smrcg9rLgnJBibWyf8MYVxtQTgXP-L05GjCVNzWyfvMhYsC-c2wRcNKJTotgxgogm1JMZDWQrHk1g1HfOuIWALbcdsqoJgByNqRKuchwwXAqjA6Vzep7AW98JQWGwLzpnneHHi6p6B-JPI52Rujc6rcrlDgBHBJz-Pt7LD591IYsO3s6ztjcdnD-dyE6u8ANDzQhqdQStTBrn6pYwSlVIHzuizRM2yvUDdjPfbm40Gxi6k6Bud9jzGkT_Doji8W3g1B3gZcO24OL8Ww4Mrefaf1581oa_Cp5GlJtAS70JgQUyFjWGoWlsGCmhRD8htmu1YZYofMkAVvr1Sm66ESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsmypDGgjp1962ofOxlFPMqnTIyeoe_7UTWXdRkvFospgBhU6iS3Dj9tqUuv5rZZ7GFBI3Rnw_8ZzkJ6vO3t22qCR2x977RiEQH7wPQVIXyeXYQuEY2biryZlYCCU5l1jGKtOT44FN1ztYW6myOWr-xync9AfU0qGevK4QtfVVts1wiuukXNL-CloDC8wa38IRDDOJ2PtvWF2PD4iJdeFsJ5uRPW4MvC27bPuNK8cnTsEViAdgYBo22FQ7kBjINlaonDnEH1eAy-x0YfG1kG_j8KIURiYAg6Y2RppsXa2V64DH4XFRUgG85q1VgGExNCkDRCsU0UVk_zmxI031WAVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چه کشورهایی بیشترین ظرفیت تولید انرژی از زباله را دارند؟
🔹
چین و ژاپن از پیشتازان تبدیل زباله به انرژی در جهان هستند.
🔹
در اروپا نیز کشورهایی مثل بریتانیا، نروژ و سوئیس با توسعه زیرساخت‌های بازیافت و انرژی‌سوزی، سهم بالایی در مدیریت زباله دارند.
🔹
در ایران، سهم تبدیل زباله به انرژی کمتر از ۵٪ است و هنوز در مراحل اولیه توسعه قرار دارد.
@amarfact</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/665140" target="_blank">📅 23:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اعتراض آیت‌الله مدرسی یزدی به بازگشایی اینترنت بین‌الملل بدون ملاحظات کارشناسی
🔹
عضو فقهای شورای نگهبان با انتقاد از بازگشایی اینترنت بین‌الملل بدون بررسی کارشناسی، این اقدام را تهدیدی برای امنیت، اقتصاد و سلامت روان جامعه دانست و هرگونه تصمیم در این زمینه باید صرفاً از مجاری قانونی و با نظر متخصصان متعهد اتخاذ شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/665139" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1AduajvwcSXScrt8KcY9boXYqWZYPrTyXlsyzElVv8c-dckRBQWQJ54p-cnAQBk7p3knYlRl3mYrZgpvYrCuSVcGYvdG2o0l4tu4J8BmqELRA94n4Wpm24bf-Wp1dyn815BBFVIHNwwnDknmR05esnXGZkN0M0VxmprEl6jyXgYRv2TNZjAFE6Sig0sm789M8OJzwbcrCKFcy_XbY3Gb7LBbeje0X2wOtD7OGEOOE745XBN6zhieO6zg2dQ31ZkfsBCKGTZa51Nuc33E4hu21M2XE3IMzYsRiWHLeKp8UmtBFVXD9tSIAahws1NwZk_Kl7AfLMv8CPOFnNy2ILDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر خبرفوری از روند آماده‌سازی مصلی تهران برای تشییع «رهبر شهید انقلاب» #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/665138" target="_blank">📅 23:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
نتانیاهو: رابطه من با ترامپ بسیار خوب است، اما در دیدگاه‌ها تفاوت‌هایی وجود دارد
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/665137" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e795bbab88.mp4?token=N55SqugbSJqLjFxFChMj7lJ3CcLpYxGk_njMFinwgjX9XyJ1TfRuIYxPdDmVHVbvGBEoHjlImK-xkPM3XQqMz-Hn86R41XQ-dD5gU4tMuXk8dCGq9HIG-RC_h-QZnEg4dnMvAJ-pV5UmHjxh3rWK1A3gtGGnJNekEbn4C1hhhBUo2h5J-jpmgIQDSnj-pW7uoNPPCumq85ULKN-tyvKCsiEvsWUeSG4fuSsACh6iZxpul6eiXNrovfA6IPfFzJodreDMmh3z6gBpMjAcmTS8VOFQFUz42GrmSFn0xJ24IMpoV6GWSppT4mfDFnef3gV6Gr1t5NEgzvyTbLTN2rZtTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e795bbab88.mp4?token=N55SqugbSJqLjFxFChMj7lJ3CcLpYxGk_njMFinwgjX9XyJ1TfRuIYxPdDmVHVbvGBEoHjlImK-xkPM3XQqMz-Hn86R41XQ-dD5gU4tMuXk8dCGq9HIG-RC_h-QZnEg4dnMvAJ-pV5UmHjxh3rWK1A3gtGGnJNekEbn4C1hhhBUo2h5J-jpmgIQDSnj-pW7uoNPPCumq85ULKN-tyvKCsiEvsWUeSG4fuSsACh6iZxpul6eiXNrovfA6IPfFzJodreDMmh3z6gBpMjAcmTS8VOFQFUz42GrmSFn0xJ24IMpoV6GWSppT4mfDFnef3gV6Gr1t5NEgzvyTbLTN2rZtTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
قلعه‌نویی
:
ما نرفتیم مرحله بعدی ولی کلی دست آورد بدست آوردیم اینم عزتی بود که خدا به ما داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/665136" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
به خاطر مشکلات سیاسی با منِ قالیباف، حقوق ملت را از بین نبرید
🔹
کسانی که حرف ترامپ فاسق را قبول می‌کنند، یک‌بار هم حرف برادر دینی خود را بشنوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/665135" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
قسمت هشتم مستند احیا و حقیقت | ایران امام رضا(ع)
✅
بعضی نجات‌ها را نمی‌شود با اعداد و محاسبات توضیح داد...
🔹
آن روز، میلیاردها ترکش آهنین، آسمان و زمین را شکافتند. هزاران کارگر در سایت های فولاد خوزستان حضور داشتند و هر پیش‌بینی، از وقوع یک فاجعه حکایت…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/665134" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665133">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e21f427ab.mp4?token=ijCKeino_14_N1G2YPaMoaOrUjlk8ARXtaopz_HSyc2-muMwa6n1fiHauJ9UBxh3Ojl3Rg_R_jE2CwhDmN253wdeW1-u0cNsu9pAcYTqYMRw0s0dVVLP53HqQI3ylIO9ld2FHJmeGjJipamoPsScIDNWu5r3NLDKEH1xhLLxly-lVFcAVmV8EhkMQNyXRB_1AYa4bn3sYEd7xDB9HRSMjYjBcvNhEvMIys8tYr0o3QhOAhAUueN3ovl3pybd8CeHzDMRdQI6j_WIOVF_f6i0q9r5fYOzZ3OBxMfCmLg8r784eLxcIwqfpfD0D4f-y8FRzmN3socLq1DQKPr78byCCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e21f427ab.mp4?token=ijCKeino_14_N1G2YPaMoaOrUjlk8ARXtaopz_HSyc2-muMwa6n1fiHauJ9UBxh3Ojl3Rg_R_jE2CwhDmN253wdeW1-u0cNsu9pAcYTqYMRw0s0dVVLP53HqQI3ylIO9ld2FHJmeGjJipamoPsScIDNWu5r3NLDKEH1xhLLxly-lVFcAVmV8EhkMQNyXRB_1AYa4bn3sYEd7xDB9HRSMjYjBcvNhEvMIys8tYr0o3QhOAhAUueN3ovl3pybd8CeHzDMRdQI6j_WIOVF_f6i0q9r5fYOzZ3OBxMfCmLg8r784eLxcIwqfpfD0D4f-y8FRzmN3socLq1DQKPr78byCCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو از ذوق‌ زدگی این دختر کوچولو بعد از گرفتن کادوهای تولدش، حسابی تو اینستاگرام وایرال شده
🔹
به قدری بازدیدش خوب بوده که در کمتر از یک روز، بیشتر از ۱۰ میلیون ویو در اینستاگرام داشته!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/665133" target="_blank">📅 23:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665132">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c252ff6209.mp4?token=MD8T9t9yH5J6Aqjp2KxLvyK4-9DyKnQ5y48_bxIJQAejMVWstWZjET-Cyut3cHD1EMnqLwyxifUbcJx6CJpo4ztnr77paIvwzRX-XS9h31x89sBTeyptdRWfZ9BXaQJnhDkVePzEJJ7aoDSGuwqiogYO5904CzGQ8D920LB8L-4xTNxyKA_L6KosZby4KfWySyY6WObn5UXPv6fyGIrwGLQ5jFZdl6E59OwApo0UMftwfa-tdMzJ-HREg8Wq8QosEyLSKjCyRPdmVrzFrS5mPlQSMsZ06EYlGv0OWUexB3-iYVwcoGji4GwXz8chnOBlH2x7hX6WL0UjgaMhzmtwSFCDFRPRP6f6CfZlBsVW_g_zgX6cLfp85ofbZQvjhiaUrcFUx5vsuVDThDhIlVEAtv69uqlBZVdHX0CN4ImRVKAxigj1aKkJtTFC2vRFaIKgpLsQytjq-RpjHf-KQRTqHM0qcL06wXR_Y2nfvAwBfl0nhQC09nNu6GXlmDW47jE7x88AIIWwzz0_l81O-Fpc7vjJACNQamGFe4o-hEulNkWNLFjPIQJl95f4lFcpu5p2tGIyHbu5wxEy6giIA_Wb0pvguCe5O7en8Vd2nQTownoEOkl6qeD95cyMGoNipFz1mikjI26_H6Gk5StmhwayfK3Phai9qzoODD2ZgKHts7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c252ff6209.mp4?token=MD8T9t9yH5J6Aqjp2KxLvyK4-9DyKnQ5y48_bxIJQAejMVWstWZjET-Cyut3cHD1EMnqLwyxifUbcJx6CJpo4ztnr77paIvwzRX-XS9h31x89sBTeyptdRWfZ9BXaQJnhDkVePzEJJ7aoDSGuwqiogYO5904CzGQ8D920LB8L-4xTNxyKA_L6KosZby4KfWySyY6WObn5UXPv6fyGIrwGLQ5jFZdl6E59OwApo0UMftwfa-tdMzJ-HREg8Wq8QosEyLSKjCyRPdmVrzFrS5mPlQSMsZ06EYlGv0OWUexB3-iYVwcoGji4GwXz8chnOBlH2x7hX6WL0UjgaMhzmtwSFCDFRPRP6f6CfZlBsVW_g_zgX6cLfp85ofbZQvjhiaUrcFUx5vsuVDThDhIlVEAtv69uqlBZVdHX0CN4ImRVKAxigj1aKkJtTFC2vRFaIKgpLsQytjq-RpjHf-KQRTqHM0qcL06wXR_Y2nfvAwBfl0nhQC09nNu6GXlmDW47jE7x88AIIWwzz0_l81O-Fpc7vjJACNQamGFe4o-hEulNkWNLFjPIQJl95f4lFcpu5p2tGIyHbu5wxEy6giIA_Wb0pvguCe5O7en8Vd2nQTownoEOkl6qeD95cyMGoNipFz1mikjI26_H6Gk5StmhwayfK3Phai9qzoODD2ZgKHts7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهرمانان واقعی کشور ...
🔹
این فقط چند جمله نیست؛ روایتی است از نگاه رهبر فرزانه شهید به قهرمانان واقعی این سرزمین.
🔹
حرف‌هایی که شاید ماه‌ها گفته شد، اما امروز بیش از هر زمان دیگری معنا پیدا کرده است. این ویدئو را ببینید و بشنوید قهرمان واقعی از نگاه او چه کسی بود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/665132" target="_blank">📅 23:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665131">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b314ee9d.mp4?token=MU5YDFwPvvCmwaFjXw8NFUWB2Pq9NPGmMXFD3rHQU2vSlL9iVK9g-F1_N5lDmQYXiM_hNuLbhh8mbWVDz_i5xALbORWOJa63hilZ2lYnjdyIucSEUWhjBsyWClYDfKmMHsqmwxbUxFkY_fyE0pMC95RXza6HixUvmdN8Rba4zE76VaC4Dbb4x3kv3Rd8fwhQR0k11YewV1jrlcBuoBuyfNLBjWiX6GEoCmAyGrxvhGT122j8vJUS6j5KeTb-RXCI99begTFr4P_-8UhawAUq12Vtp5uj1xvS_IsHiaGp7Ss0TjHGHAztvr7Cr8TIgroJE0quDo-3pmn1Y1fsIHpjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b314ee9d.mp4?token=MU5YDFwPvvCmwaFjXw8NFUWB2Pq9NPGmMXFD3rHQU2vSlL9iVK9g-F1_N5lDmQYXiM_hNuLbhh8mbWVDz_i5xALbORWOJa63hilZ2lYnjdyIucSEUWhjBsyWClYDfKmMHsqmwxbUxFkY_fyE0pMC95RXza6HixUvmdN8Rba4zE76VaC4Dbb4x3kv3Rd8fwhQR0k11YewV1jrlcBuoBuyfNLBjWiX6GEoCmAyGrxvhGT122j8vJUS6j5KeTb-RXCI99begTFr4P_-8UhawAUq12Vtp5uj1xvS_IsHiaGp7Ss0TjHGHAztvr7Cr8TIgroJE0quDo-3pmn1Y1fsIHpjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حداد عادل از سفره جمع کردن آقا مجتبی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/665131" target="_blank">📅 23:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665130">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b10c272e.mp4?token=nsRgaq7TUqd-41NjUAKtSz4mlZaH1BpDRzOXNqF5Nhyvo88s4R1l-srcH40BuvjmJWxhPKuK_ySIJ-TiydyGyQbQCQRJNVweZiR9fOgtyNcYhAD1gEYZhOdVP0qgpG7j0JStckLGVUDQH4W1NljGNDikb94OYITXQt3nwerLSMhBuc3JWbVu7b3kdzfvssmhf72tG7E45U6mIx3paYLF9UQfOxmfaJYB9wgkqYx2U1iEA7uv7M1E0iNJuobYAlV4uFMrtSvNr_-3eUSu32t0NaDXku0jmGhi89ptcuhEsjb-xxEH8vWPHrruH3eEn2lWNaWw5y9CHH9txvjnfmeBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b10c272e.mp4?token=nsRgaq7TUqd-41NjUAKtSz4mlZaH1BpDRzOXNqF5Nhyvo88s4R1l-srcH40BuvjmJWxhPKuK_ySIJ-TiydyGyQbQCQRJNVweZiR9fOgtyNcYhAD1gEYZhOdVP0qgpG7j0JStckLGVUDQH4W1NljGNDikb94OYITXQt3nwerLSMhBuc3JWbVu7b3kdzfvssmhf72tG7E45U6mIx3paYLF9UQfOxmfaJYB9wgkqYx2U1iEA7uv7M1E0iNJuobYAlV4uFMrtSvNr_-3eUSu32t0NaDXku0jmGhi89ptcuhEsjb-xxEH8vWPHrruH3eEn2lWNaWw5y9CHH9txvjnfmeBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پوستر فراگیر در ژاپن؛ پیام تند زنان ژاپنی به مردان: به‌جای ریاکاری، خانه خودت را تمیز کن
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/665130" target="_blank">📅 23:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665129">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772d1c33e9.mp4?token=kGW2xDKBA8NaAz3qYFyzZiT-MJ2r-zR5qBkqKuErRHmakTDkyjQMjtkuGdle-j3mxKJGKFXPBlYZBVfCr1qsz7JZzcYQJY4_BfSGz0XrVLnoYYDdu9MJxK-8YfAhTVD17jY2sstcyExy3-cXYy6Y1OhsTSRcjIcUUkxwCl8jgQLucw-DsNIaCOoaZtKTN4WPsmGPdVqTlot1t_5cHveh0fafn7L90ld5k1DAarJUD-rhnBgrGPlw9QgwNgC_kY0xKKtsCkY45kFGwAxfZJNbIN5GXc_z5k5souXvSISdUlUlH_nEc4GE-Pe9RxPA9A8m-llJF4ZRAIte7EC1UmnqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772d1c33e9.mp4?token=kGW2xDKBA8NaAz3qYFyzZiT-MJ2r-zR5qBkqKuErRHmakTDkyjQMjtkuGdle-j3mxKJGKFXPBlYZBVfCr1qsz7JZzcYQJY4_BfSGz0XrVLnoYYDdu9MJxK-8YfAhTVD17jY2sstcyExy3-cXYy6Y1OhsTSRcjIcUUkxwCl8jgQLucw-DsNIaCOoaZtKTN4WPsmGPdVqTlot1t_5cHveh0fafn7L90ld5k1DAarJUD-rhnBgrGPlw9QgwNgC_kY0xKKtsCkY45kFGwAxfZJNbIN5GXc_z5k5souXvSISdUlUlH_nEc4GE-Pe9RxPA9A8m-llJF4ZRAIte7EC1UmnqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به خاطر مشکلات سیاسی با منِ قالیباف، حقوق ملت را از بین نبرید
🔹
کسانی که حرف ترامپ فاسق را قبول می‌کنند، یک‌بار هم حرف برادر دینی خود را بشنوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/665129" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665128">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b449e24d.mp4?token=RTAOehEbX4a93aTVLX-8pXQYbQri40lWVzGDPkxVtUkPt46QtBsAVVRqlk46gwGPZXZVttZVho9fJT0J_VZyFpVUL67Y4cC-Q_8BHOEB6WGBRur7vaYJaWH5wgPElNfPNZAMrIfKy_Plak098u8BuecM6ZOJVLet-vfq4Ch_6tZP7dh2T21oVcJ9pmnTBZSkt3qzj1dMAejN2UUfy7FeOYZJYEkfGRP6dRaIvbpn2Ti8smg9_IHogy33UekMdb0YKtV-NABu8hqTxNXQwEYqIx5NNSp7hIRxmV8TNRArmh5ILTxpmayrBVWWSN2D-6oFPtogndwQdWSym6K2IG_ynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b449e24d.mp4?token=RTAOehEbX4a93aTVLX-8pXQYbQri40lWVzGDPkxVtUkPt46QtBsAVVRqlk46gwGPZXZVttZVho9fJT0J_VZyFpVUL67Y4cC-Q_8BHOEB6WGBRur7vaYJaWH5wgPElNfPNZAMrIfKy_Plak098u8BuecM6ZOJVLet-vfq4Ch_6tZP7dh2T21oVcJ9pmnTBZSkt3qzj1dMAejN2UUfy7FeOYZJYEkfGRP6dRaIvbpn2Ti8smg9_IHogy33UekMdb0YKtV-NABu8hqTxNXQwEYqIx5NNSp7hIRxmV8TNRArmh5ILTxpmayrBVWWSN2D-6oFPtogndwQdWSym6K2IG_ynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: باید فشار اقتصادی را از روی دوش مردم برداریم؛ ما این کار را با عزت انجام دادیم و این سند شکست آمریکاست
🔹
بر اساس این تفاهم‌نامه، از مجموع ۲۴ میلیارد دلار دارایی ما در کشورهای مختلف، قرار است ۱۲ میلیارد دلار در اختیار بانک مرکزی قرار بگیرد تا هر…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/665128" target="_blank">📅 23:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665127">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
قالیباف: عبور از تنگه بدون هزینه فقط برای ۶۰ روز است
🔹
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/665127" target="_blank">📅 22:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a1121f6c.mp4?token=RyrY6PJ3o7REdw5w8e3PCauSwuOG1dZPGuLkvz_7Ys3RURTbHNRPIfp7n1qqZPvfmNMSfyvjW_UiyiF7g3I7XXTcRkI2o4o_apOTopLKcXycRosiWGjqWOCqOcjb6dTlcqqZ6__FhDbNy42cDFhQixsC-uEuRsSiTybHhMe88oXfGPEZy0EuuiJc3DssPWMr4Ws2O-bDNfwR9cIUd_EntTdfIHcpyLXm_sXWWxLoAXJ4kCg8aDUbGVwhwuLeEmck7O1EkssOYu2IdHMQ6v3d409nPQZFvwO96uIGYxd2FM7UNVQoN_qZ9e5e7LYJHmxOJ--0Iu5XKKDqZTZjHXFmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a1121f6c.mp4?token=RyrY6PJ3o7REdw5w8e3PCauSwuOG1dZPGuLkvz_7Ys3RURTbHNRPIfp7n1qqZPvfmNMSfyvjW_UiyiF7g3I7XXTcRkI2o4o_apOTopLKcXycRosiWGjqWOCqOcjb6dTlcqqZ6__FhDbNy42cDFhQixsC-uEuRsSiTybHhMe88oXfGPEZy0EuuiJc3DssPWMr4Ws2O-bDNfwR9cIUd_EntTdfIHcpyLXm_sXWWxLoAXJ4kCg8aDUbGVwhwuLeEmck7O1EkssOYu2IdHMQ6v3d409nPQZFvwO96uIGYxd2FM7UNVQoN_qZ9e5e7LYJHmxOJ--0Iu5XKKDqZTZjHXFmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: تاکتیک مذاکره ایرانی را درک نمی‌کنم
🔹
ما خواهان تعهدات پایدار هستیم که قابل‌تأیید باشند و با بازرسی‌هایی پشتیبانی بشن که ایران، کل کشورش رو از سلاح هسته‌ای پاک می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/665126" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcNYYWrbFpR44irP8rhU6zysGvObG7sHyDW-d7rEuXWwoRW4CcDy5ZizUxlEBLoJ9YPnB8qPP6tlq7GHwZc2Rad7iBsX0bEMOosmEHOBvDByHbptsJhCdEZK2FSWg22RS3FJS2pg9nl-aBPpneipZBRRM17O8Pix00bot6NcLA9JrZc1c0oUQAoGdbhjq0VsZHschr7B0bvhXpUZvaIkRoZ0vmlK5eO8oTWv2r-zGid5_y0I0Nsy2tIaB5iHpOCkfMnReZfOyRcfyn3XH8qhto6W26c7d1phMhiuEwa5BLLxzTbpVrk5kFyHKXHG4pre0DLH12m31f15QGc1Q-5Tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسی که عدالت را پایمال کند، روزی در برابر آن خواهد ایستاد
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/665125" target="_blank">📅 22:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=To-pwVz5-8dsSclSP8AZjuwXYsM2PBbeZ1i784JTD8FmlMAc8HdzQM8mg5jwPa5cKP-K_Le5U4hYBS0WvbV5gmB7yERwR2e2hTI10M3JdIBPwjv96bDbFxscqGKBISMWdMyjD71YeNF1MNeNfYZ9d_jKg34bsCybhcXDqZbMbEGuE1-cDiFSbqsJ47C-RE5q-iDtPggWxiD_tXHeKhYkkGuziGjMR25csa4Cz_NWJlTJK8rU4lRnuyMUqdZKy4vbbJuZeBs7gsdQcMWBJJUSLpT1XgTnEHpUZcsfvyqV-_i3hGnyKn0JI7SIfL6s7Kjbgroy-euUZc8V1dmHboCyZiXk4J57TU7mPPikOgE34r2SSzeIDwmopAIJLoP-rVrZ2PZkdrsMnAQgjxTfRf2h3GI3x0eoRjdE8be7PZQUz1N9vzw0WbsRHOBCFWs_0Pi-4w0ek0Weidyp2jXxL69BgLEJxF3LK36nAv67B065A16o_oA-JK8UgJEEE0WEPP2HJXcXcAihO2L8iHq5L3xJ-im95OIwy9-M8i4miMCW2Q2jMkPobzdY6vK79c3PEdTFH52KKcK1QZl5l7aTEQh0GIPGn4yVNB9z1EbliRWl-4pb2w8V51y-z_sYwO7irdiejHj4niN9fcUDPpDBz1eqWeWrSFYjDvg9P1XoibPmsVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=To-pwVz5-8dsSclSP8AZjuwXYsM2PBbeZ1i784JTD8FmlMAc8HdzQM8mg5jwPa5cKP-K_Le5U4hYBS0WvbV5gmB7yERwR2e2hTI10M3JdIBPwjv96bDbFxscqGKBISMWdMyjD71YeNF1MNeNfYZ9d_jKg34bsCybhcXDqZbMbEGuE1-cDiFSbqsJ47C-RE5q-iDtPggWxiD_tXHeKhYkkGuziGjMR25csa4Cz_NWJlTJK8rU4lRnuyMUqdZKy4vbbJuZeBs7gsdQcMWBJJUSLpT1XgTnEHpUZcsfvyqV-_i3hGnyKn0JI7SIfL6s7Kjbgroy-euUZc8V1dmHboCyZiXk4J57TU7mPPikOgE34r2SSzeIDwmopAIJLoP-rVrZ2PZkdrsMnAQgjxTfRf2h3GI3x0eoRjdE8be7PZQUz1N9vzw0WbsRHOBCFWs_0Pi-4w0ek0Weidyp2jXxL69BgLEJxF3LK36nAv67B065A16o_oA-JK8UgJEEE0WEPP2HJXcXcAihO2L8iHq5L3xJ-im95OIwy9-M8i4miMCW2Q2jMkPobzdY6vK79c3PEdTFH52KKcK1QZl5l7aTEQh0GIPGn4yVNB9z1EbliRWl-4pb2w8V51y-z_sYwO7irdiejHj4niN9fcUDPpDBz1eqWeWrSFYjDvg9P1XoibPmsVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: عبور از تنگه بدون هزینه فقط برای ۶۰ روز است
🔹
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/665124" target="_blank">📅 22:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
‌ قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔹
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها و شهدا در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/665123" target="_blank">📅 22:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOjFxBHxM_uKCERe3yVe1sctzC7J72vKKLY9WSQl26NiruXhFSyLODCCVNCIbEvwfD_-O1Cp1q2czF6Ql0zaSxBEPqZRmTdAqHZz6npoA-EwzdJi6X5bAEugmpa1K_zUHXug6xZGoX0muM-ECMDMfg4-AsaIqpGxAHqPnXyqmjoUUyLVzpgUsRKU7D3dKKI6lr9SQJJVmog1DF8dYg5FkMnVbi820p95VSlPSTbaDDxb-uUPk-_fQ7B2LbUsyY1qaBJdiz0fsSOnhfo_7LMTlIoSg2AZEx_iEgfyFZsAZ4W008iLaEfN9Sc98nRqbuSgv5e2fm5f8cZ1HwSFdyn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه کج
🔹
تنگه هرمز امروز فقط یک آبراه نیست، مهم‌ترین برگ برنده ایران در معادلات منطقه‌ای و مذاکرات با آمریکاست. به همین دلیل، تلاش برخی بازیگران برای سپردن مدیریت یا امنیت این گذرگاه به طرف‌های دیگر، صرفاً یک اقدام دریایی نیست، بلکه تلاشی برای تضعیف اهرم راهبردی تهران است. در این میان، استفاده از ظرفیت عمان یا ایجاد شکاف میان تهران و مسقط نیز می‌تواند بخشی از همین سناریو باشد، زیرا هر اختلافی میان دو همسایه، مسیر اجرای طرح‌های ضدایرانی را هموارتر می‌کند. واقعیت این است که امنیت پایدار تنگه هرمز با حذف ایران به دست نمی‌آید. راهی که بر نادیده گرفتن نقش تهران و ایجاد شکاف میان همسایگان بنا شود، همان راه کجی است که سرانجامی جز بن‌بست نخواهد داشت.
🔹
هفتصدوهشتادوهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/665122" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مروری بر سیره حکمرانی قائد شهید انقلاب؛
«به یاد اویی که ما را صاحب‌خانه می‌دانست»
🔹
بزرگ‌ترین تفاوت رهبری با خیلی از مسئولان، در یک کلمه خلاصه می‌شد: «باور به مردم». در سال‌هایی که خیلی از پشت‌میزنشین‌ها تصور می‌کردند حکمرانی یعنی نوشتن بخشنامه‌های پیچیده و جلسات طولانی، او دقیقاً در نقطه مقابل ایستاد و بارها خط بطلان کشید روی این تفکر که «مردم متوجه پیچیدگی امور نمی‌شوند و باید کار را به مسئولین سپرد.»
🔹
او اقتصاد و فرهنگ را زمانی موفق می‌دانست که کلیدش دست خود مردم باشد، نه در انحصار حلقه‌های بسته مدیریتی. او معتقد بود در یک نظام اسلامی، مسئولان چیزی جز خدمتگزار مردم نیستند و مشروعیتشان به میزان گره‌گشایی از کار مردم بستگی دارد. در منطق او، نقد منصفانه و جریان دائمی نظارت مردم بر کارآمدی مسئولین، نه یک تهدید برای امنیت ملی، بلکه تضمین‌کننده‌ی سلامت نظام بود.
🔹
رهبری که می‌شناختیم، تا آخرین روزهای حیاتش به ما یادآوری کرد که هیچ حکومتی بدون تکیه بر آگاهی و حضور مردم، عاقبت‌به‌خیر نخواهد شد.
🔹
میوه و ثمره‌ی این نگاه او به مردم، خود را در روزهای سخت ابتلا نشان داد؛ آنجا که این باور او، به «بعثت مردم در جنگ» ختم شد و همین حضور بی‌دریغ آحاد مردم در میدان بود که سپر بلای کشور شد و ثبات و امنیت کشور را حفظ کرد. از همین روست که امروز، خط‌کش سنجش هر مدیری در نظام اسلامی، میزان وفاداری او به این میراث بزرگ است.
شیخ محسن رمضانی
دبیر نهضت مردمی بعثت خون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/665121" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9174733cfd.mp4?token=PxQpLOJ1a4isBdai3f3Fh_9RsgsU-aw8XKgEOsnmxII1gwOhG9hR3y4APRwdUFvpDze7VjVPISRzlGS8wt9fQUkZCaxKOKDJtdTeMkjllohXst5jOKlwLX_oSlUrFscw4vz50A-VV25lCjMkTCaMUlosekhwjNLoYKEmzNC-hljTnMItNL0d6yYT2HpYpe0SuAfM_rZCbSbxVatvsccQRuZ6BIBhlajzOFtSohyFuA8SwsmivqGs-RW6hs2Bocf7NPNvp59ulT4KAa-MbHpc0uaWpTYRu_C_YnMABnN_jBAipX0_NHBbyQNP4jC73rw407_SV1E7wqgRoWPkzm-K9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9174733cfd.mp4?token=PxQpLOJ1a4isBdai3f3Fh_9RsgsU-aw8XKgEOsnmxII1gwOhG9hR3y4APRwdUFvpDze7VjVPISRzlGS8wt9fQUkZCaxKOKDJtdTeMkjllohXst5jOKlwLX_oSlUrFscw4vz50A-VV25lCjMkTCaMUlosekhwjNLoYKEmzNC-hljTnMItNL0d6yYT2HpYpe0SuAfM_rZCbSbxVatvsccQRuZ6BIBhlajzOFtSohyFuA8SwsmivqGs-RW6hs2Bocf7NPNvp59ulT4KAa-MbHpc0uaWpTYRu_C_YnMABnN_jBAipX0_NHBbyQNP4jC73rw407_SV1E7wqgRoWPkzm-K9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدصادق شهبازی، دبیر سابق جنبش عدالت‌خواه دانشجویی: پسر پیغمبر رو وسط تهران زدن، باید انتقام خون رهبر رو بگیریم، رهبر رو با درهم و دینار معاوضه نمی‌کنیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/665120" target="_blank">📅 22:40 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
