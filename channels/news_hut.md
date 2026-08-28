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
<img src="https://cdn4.telesco.pe/file/nAoUaUe18-iE727LGw5cdH1szNaQMb_wdMfAr5th-guQLtdz9XfypOWqg6fGZCVKOQETjNe9nxRz5OR4kvcuWFUfTp4JALy1mwvWGnDgpZwJtSwdPrBSN1M5BYK5plIZq5EIYlCHGf4n3YedQmgbIw071kK8HafGmsUS784jmWbIRjHzaTGPdkoublatgI1CWSis5P9qlRQRESK4gntu8HScfYqnVEPmApVTn4ddXLQA_P6o-YChFA3BLvRb7feauTUce85tdXYWOCxgOaHQLo5s6iRzyQRCMv3Yg86YnSdl06cWNWgOCe0ShG6i5vGndO5NH0Xks178_NRg3YNTuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 117K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiSkjyur5HRoSZ-Wq00frx4DtxiSI2jv-YNRzwTYRRCUl0lM0F3r-r5IbghBB4JHFMi38DB7yPwAtbvBjJ7o5u0d-5Om-2M-FpOg8D9GREf581VW4Gp53MxXos9CWh5q88T9KoTDerrkeBcqwbQCOmXGHCEOhX4SzAGvR-9QvGcL38tbUPQcVenV6CTGwjkX882h-9Ua_5WRIBSfrKNep4W8zE4CTFhW41ZdVUbrqPLmMlFJuP1gblOEJUkgbTfn_z2GMcu5nVnrTK-lpmvJBiIBAUXQeTxx9eLyMy2CqCilJfZ0GjTVr38_9s3RV3uJW35UM4AD1tAq5QPX1G22yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLV3rDmyoVBg7dxWwRvJ7SRpSNW7z5wke2LtM4CcMQ9oSrHxBmKhb4b7a4HaP58gG_uNQoa3H4977F94uHmkQmonzytcmnD-SDpgdJNyNPVyuaiL20GBkldcICzTUL53QEjlIx5b0XfI-3GKEIvxRtg0GZnC4WfmQNdd41YRpNVUF1t3Soqq0Ob8AN3xv7-fgwEr4TKMGlmI86j6ZZyPa5g5UX3CAGCNbNdpMlFbmUjGNqfW4ld5-QVO9LAhlXTBwi4u1SM0NnZAoqnEoS1rnEsav6jV2W4ltBIly68RPHhpwghYHxoAgF0fIfAypkHBoEDGUZjxZek75yFDsewRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF9k0mPFjJPiOxfc0pXIGHk5DIcEaBgdb7ReSpEXO2C0pJaemN5w0IIA-zKxtJHymYVGuXrNRaEmpuZqI17urTjIRffooyFPllIWTKQo8lR-BreNc0bM363TocBeeDPSpNKsYk9dcAJNL75ShUVHfqqyQRlMknDrFmmU8fvFi-5NNocHBOZ2coBZL-B0KMuqfVV7kzhf3ZmMAp04cVKsP69xTiyQIDXTQMOt8eSBnP_faYQZQuSfRQM6bVRSlp7Cpc9-AemUnjMyVdFDMQFzze9mQeNStWtrBErKLTiO73iesi8hhttsGpa1vxsMW-902n8i3u_4I0gYtBVBBXtDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
تریلری که راکستار به صورت رسمی از GTA 6 منتشر کرد
💢
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/70687" target="_blank">📅 00:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70686">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFY97xaf7BS6pSzSM12qYUfkvP1MxsTFUy0-9siKPYmdZLULcGQ-GxDY9vOWJVU9myRhlM5qHf3ArlTyNDLftlbcUxABlde_jRlbrVn1vgKzWPbFblrACZzcI5FF_9A7oaMewlaGaHhaNfqBNBGnebPf-uZqNmd4nPaeURjXdNVRZhjxb97rO2XOpRTqviIQgE99j8QRw6lDrUBPFb4hFJ8fGKjmh9XdMGOH9RMHHvcef3wTr86Bd5AAhJnCd2bIXjeWDl4Y1X7Pf4ywJcMB68f_VFbdARTIrSniHI7xnNE20KBZFKl9lD7oVrSFbfKJjdLxUyGubaSLBvpwdOzZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
درحالی که دلار به تازگی از مرز 200 هزار تومن هم عبور کرده؛
دیروز پزشکیان به مناسبت گرامیداشت روز کارمند، از تیم اقتصادیِ خودش به خاطر عملکردشون تقدیر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/70686" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70685">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=c91WoR_GP1idgBl178VCxkBVJiGZj4iRTDDxzrCdO8w-Dp56Ds8MzZcmopPylKw82M91m7uNXn1JsMIiu9ErL9u1FUe65qU7fLQW86QBCUtlr4EriqIxZIfmiQy7FTuWGNE3bCXItbyr5AAgHae_6KEvViNM_igECMOucmVkT_sRjxEdJ0f9-KMySJUOyMoLbBjkzFmVkzLVM6HjxSopNbPh-lSRAlAuMYD01xIMSGmjZSKeSTRnQRc60FVHqouEA1i-i44Da2vEHl-wkaDCmN-nm2nQVRzMQ7izpUUemkovXjGbizY9IfK9F4ac6pxsCPJv9jU99YBe_k63w_PhvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=c91WoR_GP1idgBl178VCxkBVJiGZj4iRTDDxzrCdO8w-Dp56Ds8MzZcmopPylKw82M91m7uNXn1JsMIiu9ErL9u1FUe65qU7fLQW86QBCUtlr4EriqIxZIfmiQy7FTuWGNE3bCXItbyr5AAgHae_6KEvViNM_igECMOucmVkT_sRjxEdJ0f9-KMySJUOyMoLbBjkzFmVkzLVM6HjxSopNbPh-lSRAlAuMYD01xIMSGmjZSKeSTRnQRc60FVHqouEA1i-i44Da2vEHl-wkaDCmN-nm2nQVRzMQ7izpUUemkovXjGbizY9IfK9F4ac6pxsCPJv9jU99YBe_k63w_PhvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بخشی از یک موشک ضدکشتی جمهوری اسلامی در نزدیکی سواحل ایران
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70685" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=FzauQqyJkDN0WOCQxpE1n-Sr4esy2oJ9U8l2aq0oReL8LodM4tdkRf2JMLfvFwnNz8pZZq6at7iMMi8lQU14bLyOvFjKw1yqfDuxts7tYO8wahKZfScW_03E7a2rPNLEx4kwwzvq0gs-pMV9DWhhQgx3KtuK6DmE8Z9iJlJA_0nWzKeBmFFxzdYRvpUuNKYn1tVZYd8PnNN6hExfSU7X0GCEJlQKt1BW4xG36Be01j8z843Cng3ggdStPP63pvP1-UMY-O1yoM3a88ltl5ooS6LsvMbwFKkdDb7cE4G6K_LmbPYf1NynXMfhSzMID5fJVHdPmZLzH7V6C60DIVea4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=FzauQqyJkDN0WOCQxpE1n-Sr4esy2oJ9U8l2aq0oReL8LodM4tdkRf2JMLfvFwnNz8pZZq6at7iMMi8lQU14bLyOvFjKw1yqfDuxts7tYO8wahKZfScW_03E7a2rPNLEx4kwwzvq0gs-pMV9DWhhQgx3KtuK6DmE8Z9iJlJA_0nWzKeBmFFxzdYRvpUuNKYn1tVZYd8PnNN6hExfSU7X0GCEJlQKt1BW4xG36Be01j8z843Cng3ggdStPP63pvP1-UMY-O1yoM3a88ltl5ooS6LsvMbwFKkdDb7cE4G6K_LmbPYf1NynXMfhSzMID5fJVHdPmZLzH7V6C60DIVea4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت در آستانه آخرین روز کاری‌اش به عنوان سخنگوی مطبوعاتی کاخ سفید، سخن می‌گوید؛
«احساسی آمیخته از تلخی و شیرینی دارم. تلخ است چون شغلی را ترک می‌کنم که بسیار دوستش دارم؛ کار کردن برای این رئیس‌جمهور، یعنی رئیس‌جمهور ترامپ، افتخار و موهبتی بزرگ در زندگی‌ام بوده است. هرگز کسی مانند او نخواهد آمد.»
لیویت پس از ۲۰ ماه فعالیت در این سمت، کناره‌گیری می‌کند. دلیل این تصمیم، تمایل او به گذراندن وقت بیشتر با خانواده و دختر نوزادش است، هرچند او همچنان به عنوان مشاور ارشدِ خارج از دولت به همکاری با این مجموعه ادامه خواهد داد.
«آن‌ها در مقطع حساسی از زندگی‌شان هستند و بیش از پیش به حضور مادرشان در خانه نیاز دارند؛ بنابراین مشتاقم که وقت بیشتری را با آن‌ها بگذرانم و در عین حال، همچنان به عنوان مشاور ارشدِ خارج از دولت در خدمت رئیس‌جمهور باشم.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/70684" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174815597.mp4?token=bNA8MIC2XJGxFJVY6ZptqdlHIe6TMRsMyNYYG1axWKo7wLqYynHZM4IAGbVCXam6mPPuAtm_qnOBaAHsyI-lrGIy_gICemISy_lLsYPs65wCiLsu4UyJZog2eTB11tB6DGn_YfAYZwt-Yy-1_NoBM_PtBpEeyXZetVaFJcUfuIpnGUsoEWLPxOP1dlFyhzh8cuJrABwnxbmP3tVahkctdHaNMj4rnMYnJiL0EmMdDypy6Qk5UZQVNreZeoQ2ACV21Yw2l9xHNr4zn2SCxynKOUOErgwMglF9y9LGeXETK0hZ6SmM_hLxfTdDgI9tnwBdEZ6detGcD2uLDc-swMqlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174815597.mp4?token=bNA8MIC2XJGxFJVY6ZptqdlHIe6TMRsMyNYYG1axWKo7wLqYynHZM4IAGbVCXam6mPPuAtm_qnOBaAHsyI-lrGIy_gICemISy_lLsYPs65wCiLsu4UyJZog2eTB11tB6DGn_YfAYZwt-Yy-1_NoBM_PtBpEeyXZetVaFJcUfuIpnGUsoEWLPxOP1dlFyhzh8cuJrABwnxbmP3tVahkctdHaNMj4rnMYnJiL0EmMdDypy6Qk5UZQVNreZeoQ2ACV21Yw2l9xHNr4zn2SCxynKOUOErgwMglF9y9LGeXETK0hZ6SmM_hLxfTdDgI9tnwBdEZ6detGcD2uLDc-swMqlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای این فرد که در حال وایرال شدنه:
الان که رهبر رو زدن، مسئولیت این کار زدن رو گردن نمی‌گیریم، جرأت نداریم رهبر بعدی‌مون رو نشون بدیم. به هزار تا داستان دیگه داریم. ته جنگ‌مون معلوم نیست. نمیدونیم خونه هامون میمونه، خانواده هامون میمونه، ناموس هامون در خطر هست یا نیست.
بعد بگیم که آقا ما دست‌مون رو تنگه و هرمز گذاشتیم. خب حرکت بعدیت چیه؟ بعدش میخوای چی کار بکنی؟ خب من... شما پنجاه سال این کشور دست‌تون بوده، نمی‌تونید یه تورم ساده رو کنترل کنید. ادعای حکومت امام زمان رو دارید که میخواید دنیا رو برای ما بسازید. خب خیلی خب.
بحث ساده فرهنگی‌تون، آمار طلاق‌تون، آمار احتکار‌تون، آمار دزدی‌هاتون. یکی یکی آمار، یکی یکی دارم میگم. میدونم تمام کل و هزینه سرمایه این کشور رو برداشتید. همین آقایان استفاده کردند به هر قیمتی هم باشه.
من یه حرف رو میزنم. همین آقایان سپاه رفتن میلیاردها دلار هزینه کردند، عجیب و غریب و زندگی من و شما و بچه هامون و نسل های آینده رو به فنا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/70683" target="_blank">📅 22:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=ewFiBzYlLsWRSR-g_kzoru3IFGH7Stz7BJjCToeUAtTKt0rlgUTyKAaqCabfaKxuaDDqEwHOZttfFsRrUb_WfQQohTDA1EyCEvwWC0UnjkXJfIVVcV4UGVJ1JAethPHX1Uzh-C8u778DjTr5YgEdVl7qlxU7nmlQchoLfmqiwoEzva-NE4GjrgY2vCQ9ABNY3K5PUxvUHGbwR1--KhdjBVb8SO97H6-z23gpAGFr9BbXkum97WU_stblyxqyo1uuvG9mBPo4cSEOOmZWPaltaCTHxmkl1X8jtT797uKOCsRN34XN4zHU5afvBxc66GC9Eta4UqyvUtyk5ZXHXk6Plg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=ewFiBzYlLsWRSR-g_kzoru3IFGH7Stz7BJjCToeUAtTKt0rlgUTyKAaqCabfaKxuaDDqEwHOZttfFsRrUb_WfQQohTDA1EyCEvwWC0UnjkXJfIVVcV4UGVJ1JAethPHX1Uzh-C8u778DjTr5YgEdVl7qlxU7nmlQchoLfmqiwoEzva-NE4GjrgY2vCQ9ABNY3K5PUxvUHGbwR1--KhdjBVb8SO97H6-z23gpAGFr9BbXkum97WU_stblyxqyo1uuvG9mBPo4cSEOOmZWPaltaCTHxmkl1X8jtT797uKOCsRN34XN4zHU5afvBxc66GC9Eta4UqyvUtyk5ZXHXk6Plg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سر دادن شعار «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی مجلس
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70682" target="_blank">📅 21:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=hk4v7lj63T6TUMVrDDQqTIb8IoSyqwvHv_3SOjiR8HKVQs4DMdKchXHAozWpOLApFwJAFI5SgZkh-HFvatnuOFCQi30lA314fvZ5RvZXn6VpttxpZ7RV9p9xGkpzsSMFEieE0JJcidk06p8PZw7IPMf-fBDocyO0t3rs57THBsP41c3Y3Aq8H8TU3-PWRa1RCLEZ9FP7OtiCExZC_zZ-_pCNj7x3r7Jq1g56TkzW1UMLLdM9y7jzSUCklhqRNcE3bmIJrPJznSOInrqg-FuCDDPC3J3ieZU53JX31kb1fldfnmr5FvQKCitMILFViHvVeNs0pp-wXGDDvqYsj8d0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=hk4v7lj63T6TUMVrDDQqTIb8IoSyqwvHv_3SOjiR8HKVQs4DMdKchXHAozWpOLApFwJAFI5SgZkh-HFvatnuOFCQi30lA314fvZ5RvZXn6VpttxpZ7RV9p9xGkpzsSMFEieE0JJcidk06p8PZw7IPMf-fBDocyO0t3rs57THBsP41c3Y3Aq8H8TU3-PWRa1RCLEZ9FP7OtiCExZC_zZ-_pCNj7x3r7Jq1g56TkzW1UMLLdM9y7jzSUCklhqRNcE3bmIJrPJznSOInrqg-FuCDDPC3J3ieZU53JX31kb1fldfnmr5FvQKCitMILFViHvVeNs0pp-wXGDDvqYsj8d0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ما یک خلیج داریم. یک دریاچه هم داریم. حالا چیزی که نیاز داریم، یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا آرام را تغییر دهیم
😠
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70681" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=HSWXsmUPNHkuC04Ig11fCfOWrwjQRUyp1Kr6OYUHX9uU6Mz8-7iZkTj0Y5fKsfVSYjAWZgBxp8EdLBG_BeSON7laMzKJJwbScf3gmhpsWQooowiMy7PEVAClu1N2LTr3CJLQ1yKQIbs_-4luz3-eSwt6z5PjTPU3iNk9z7cAz1UhL_bFYtV-FqAcc29gGwFJL1pZtG3dn4q_WTv8om5kkobbCEVsAA3svF866nU1Qrwa1mKKNEPYdEVWdbuQIoURBNJBJ22lR3Eq_L7IkesmFx9er__T1eHViXspKzGjNNZ_Eg1B0IdLlTA20_x3U06q5K5PRGNDa8yD8A1TKArYODBbh87dt_yh0IfVtBxEApM-t-4H98RlOCRn61yZHDwJQdugGCe1pf_nk3_d07OtVRte2GJaVvDMLm10bwZHQmahNL1-YRl4HnfV_mXYy4spJ8VBoH_qOz7sQWfXhPd9dHxREuc7S5tpBZLrKtW1GH8RWQGi0DL64CgaETocHO8fzl9hCNt0toHhEtyK66U5IR2h6dGtA3bBMt124UtoWn97IOYHjzrDzF9aAFPZfI0NOQPJnTssKYfGLj5wQhHXw5OGgro1fYF3FBDMblrWvBWGhadhGcXys7acdlvPCaxecdXxG01KWGkYisqYBw60KoBFQl1AWfttMoXRhXcDZ6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=HSWXsmUPNHkuC04Ig11fCfOWrwjQRUyp1Kr6OYUHX9uU6Mz8-7iZkTj0Y5fKsfVSYjAWZgBxp8EdLBG_BeSON7laMzKJJwbScf3gmhpsWQooowiMy7PEVAClu1N2LTr3CJLQ1yKQIbs_-4luz3-eSwt6z5PjTPU3iNk9z7cAz1UhL_bFYtV-FqAcc29gGwFJL1pZtG3dn4q_WTv8om5kkobbCEVsAA3svF866nU1Qrwa1mKKNEPYdEVWdbuQIoURBNJBJ22lR3Eq_L7IkesmFx9er__T1eHViXspKzGjNNZ_Eg1B0IdLlTA20_x3U06q5K5PRGNDa8yD8A1TKArYODBbh87dt_yh0IfVtBxEApM-t-4H98RlOCRn61yZHDwJQdugGCe1pf_nk3_d07OtVRte2GJaVvDMLm10bwZHQmahNL1-YRl4HnfV_mXYy4spJ8VBoH_qOz7sQWfXhPd9dHxREuc7S5tpBZLrKtW1GH8RWQGi0DL64CgaETocHO8fzl9hCNt0toHhEtyK66U5IR2h6dGtA3bBMt124UtoWn97IOYHjzrDzF9aAFPZfI0NOQPJnTssKYfGLj5wQhHXw5OGgro1fYF3FBDMblrWvBWGhadhGcXys7acdlvPCaxecdXxG01KWGkYisqYBw60KoBFQl1AWfttMoXRhXcDZ6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
🇨🇦
ترامپ فرمان اجرایی «تغییر» نام دریاچه انتاریو به دریاچه آمریکا را امضا می‌کند.
🎙
خبرنگار:
با تغییر نام دریاچه انتاریو، چه پیامی برای کانادا می‌فرستید؟
🇺🇸
ترامپ:
هیچ پیامی.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70680" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=SCwhuysz27xQB6iXSeA_pIJwtHR77nbDGFHEyhF0gpXp3DPG3Q9ETj-J1VgggpwQOJVAtRWqcRIQfVPzyzDyTUbwlHXDYJ7H4rVujn04Ar0unlo0psjk2YrIqTo_faSCVFyF-ySEZUjuZa7kNLLYR-qkBKmadwQc6ldDNM9vlmCNVTPNtl6tig-xEt8Dd14r7kxWCCw0tWBILN44yBKfgXmL8ag0C_GYaOdqK9kMuwhx4jbGdgPKR3WOi-I5BXBzJUE6W2R7h_6OY80YUqYs4Iri2ZIJFm-jyq5dhF4lnOovbVWxjDaWgY8L6c0VE95LRp9UfUziPzxLhKkWl_11XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=SCwhuysz27xQB6iXSeA_pIJwtHR77nbDGFHEyhF0gpXp3DPG3Q9ETj-J1VgggpwQOJVAtRWqcRIQfVPzyzDyTUbwlHXDYJ7H4rVujn04Ar0unlo0psjk2YrIqTo_faSCVFyF-ySEZUjuZa7kNLLYR-qkBKmadwQc6ldDNM9vlmCNVTPNtl6tig-xEt8Dd14r7kxWCCw0tWBILN44yBKfgXmL8ag0C_GYaOdqK9kMuwhx4jbGdgPKR3WOi-I5BXBzJUE6W2R7h_6OY80YUqYs4Iri2ZIJFm-jyq5dhF4lnOovbVWxjDaWgY8L6c0VE95LRp9UfUziPzxLhKkWl_11XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
چرا بانک‌های چینی را که با ایران مراوده دارند، تحریم نمی‌کنید؟
🇺🇸
ترامپ:
چه کسی گفته که این کار را نمی‌کنم؟ شما نمی‌دانید که آیا مشغول انجام آن هستم یا نه. لازم نیست همه چیز را اعلام کنم.
🎙
خبرنگار:
با کدام‌یک از رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟
🇺🇸
ترامپ:
صحبت خاصی در کار نیست. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه باز است.
اقداماتی که در قبال ایران انجام میدهیم به معنای منتفی شدن گزینه نظامی نیست.
گزینه نظامی همچنان روی میز است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70679" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwFMNhrfhWNBEjJp_TJ9I70lspkD82TuA8fxxTemFro7Af23PqyvgHk_eHv0rfuc0QoOdJ1PUEO0DOzNDzTfpy7jsrzlmwTU2W40Ggs3ZZAQa60cQrMKBx0dN33_attGqBl3KYQE_qJWTjVJ5Eqajp2krDHoDewxyzDj4YKiQYiJ4Qf9aVOFz2kd8SyC-wfky51srITynoUm5HkUIOEH-FsoNMMAfeoxYrhS2nMOztM6fmI4I-mYYypiYPKbDKLebEHCeBDFNVkYqZoPIcpzI0G96AeUPxB5Rd2Of2jmLYUq5wFx_60jhgeb88kzGRag7wKKhC9iBlODgPEFzmzqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇵🇰
کویت و پاکستان یک توافقنامه مشترک دفاعی و همکاری نظامی را در اسلام‌آباد امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/70678" target="_blank">📅 20:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtpRWO_NBZCLfFjB7vn-zxMlT-ccwSfIdkA5ajKvcZBJCDM-6y2xGxxb3KqUUQBuSA8anEjjwOC9FOqxYlm6Zs-UzoazCGOTjY6DrzprfVZoc_sS827T9lw6gUtxylsfscr4SqlnMVLcYdEa4AOjEn2NEW5Z3Qw0CHyqhYkJBOvUEW6UPGF9ID_fML6I2I-d8gmDoWDqXN1nko3IsG5oiP8bqr0FJKp9CZltRLof4AZp8L-1zVt5mvLAn0IbIiB0_3i048H0gtiLBk_5h4g_evWNLp18J4E1heQLZiNYwnjFQVehefbEA1zmd43QDGZjlap349BabOIlN_bFfQAtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=RN9jvkpuoXyrUbxXIVuslWnochhlcNE926QPN8KYYv9csCIvZWtcO-I9ZQMv5Ua2XuyaZPgCFfl6pDwYMFesV1ae9m-YD-4h1alAs9_5U0mxz5C8IvXRkIfeNXVD0dPGlsPqBegvvsHIHhK0B5Z_MmHA8nLHeSoNLBQaz5K4-lkqnmmrhsQeKRYiPZMP-6l8ZSthNgWlJTPOWPuPn2XODYiX-o99LOVPheJaJOogLhfHGcT2a18X5dPgp9sbqG21r9sY-q5s2SmulS_tWAFHQOWlwWjHZ_a_jgtx093o_QZ_vqbXi8-fC8rKOYBpoL8cshvXcGXnj7ZBsl8gcayfUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=RN9jvkpuoXyrUbxXIVuslWnochhlcNE926QPN8KYYv9csCIvZWtcO-I9ZQMv5Ua2XuyaZPgCFfl6pDwYMFesV1ae9m-YD-4h1alAs9_5U0mxz5C8IvXRkIfeNXVD0dPGlsPqBegvvsHIHhK0B5Z_MmHA8nLHeSoNLBQaz5K4-lkqnmmrhsQeKRYiPZMP-6l8ZSthNgWlJTPOWPuPn2XODYiX-o99LOVPheJaJOogLhfHGcT2a18X5dPgp9sbqG21r9sY-q5s2SmulS_tWAFHQOWlwWjHZ_a_jgtx093o_QZ_vqbXi8-fC8rKOYBpoL8cshvXcGXnj7ZBsl8gcayfUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxmaCiPU3Ry-PRD9IvZWLi_Q0UU2lSed_x5CZhFmPKcbUrkefa3ITzr6-R4ghRxQa2bEURWrO2FihRZIthOmw_xtDtK-JdjuPptd_QWdevve4UnBR8cVsr1-JKQ-a8cxMgnGYoxUEVICMB6LArRoox8f7r94CLOOhEPKBvhrFtno-fncHV5I1f7mNJ5FRUqLHp9baoKldCSbEir5g7IPb9sS4v5agyQbvnq2p280YArjXjcu_R5UE7a3MnMH2EDai45VfUtrzOrsayUQfQ-s2458IdzM9leiE11lR04TGZx8kgfnNuMD6JcnSfde8_XhKTQNRr92_Fd4cXALUVb0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=Y8KD_rg59JsOpmxNSMlegEeXeUkQ4MUNVqnGh4s65s8R1n3Wr049S3WE_WBQi4ox4kIB3N8yS6POenJfUDWekEBqc4KK7VFTUmPhad-bqlNIfFMmXK9LA7M1knjckElRAFIVC3GRHerl_LpCBjzziv6zlokEmrq2ekaJSbHhtwD1olavRZiubguplFxkdHJ3BApaOxtQvuZPHHMQF0PWg5FG_Apb_18syjtNwAO6xFcTQo-l8S_f_2GvWpRLR4VmHyayikVs-vD_LwfCw56dpLhCS3dfncPSb0-WgWADVRCBFg_SLXhNiOnV199zqA7JCE5Y71o8ZWAHe4CBfjkysQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=Y8KD_rg59JsOpmxNSMlegEeXeUkQ4MUNVqnGh4s65s8R1n3Wr049S3WE_WBQi4ox4kIB3N8yS6POenJfUDWekEBqc4KK7VFTUmPhad-bqlNIfFMmXK9LA7M1knjckElRAFIVC3GRHerl_LpCBjzziv6zlokEmrq2ekaJSbHhtwD1olavRZiubguplFxkdHJ3BApaOxtQvuZPHHMQF0PWg5FG_Apb_18syjtNwAO6xFcTQo-l8S_f_2GvWpRLR4VmHyayikVs-vD_LwfCw56dpLhCS3dfncPSb0-WgWADVRCBFg_SLXhNiOnV199zqA7JCE5Y71o8ZWAHe4CBfjkysQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=A8RMRv5eMNIyg66aGPa8LGGZYmPUc2ZFiN11dtB5yWlr5WwMjUdCsiIqCRzQOFwVs1XuaLo0puvKjkHGhfEJpGmNsDJsAFAztjIsW8xChksSep4TFY0aQEj_H3xweHhkSRdCrQb3GQ99xkbGMm32UGkoQtgcDLlWYt7iaoGMhq6V8ycmQgl4SDxcDQLOelnKvYmwdVLp0T9CNV4MLtSHTykNGxpY4EyMAzRYDDYA40UpSyiRSW4qkTUhKBouRfwKB4uDuoUB3Qg1vNrdJ0cIE_HUKvO0uDxs5ynv3IiQBi36ekCzJE1fl13J2qoOUi9xBqTnei0gLHD5T9f4RCXIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=A8RMRv5eMNIyg66aGPa8LGGZYmPUc2ZFiN11dtB5yWlr5WwMjUdCsiIqCRzQOFwVs1XuaLo0puvKjkHGhfEJpGmNsDJsAFAztjIsW8xChksSep4TFY0aQEj_H3xweHhkSRdCrQb3GQ99xkbGMm32UGkoQtgcDLlWYt7iaoGMhq6V8ycmQgl4SDxcDQLOelnKvYmwdVLp0T9CNV4MLtSHTykNGxpY4EyMAzRYDDYA40UpSyiRSW4qkTUhKBouRfwKB4uDuoUB3Qg1vNrdJ0cIE_HUKvO0uDxs5ynv3IiQBi36ekCzJE1fl13J2qoOUi9xBqTnei0gLHD5T9f4RCXIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHUf-UGTYythln1xXRRsJm2jhny-NqK_wkDxyUKUuik6-h_RiPWYfcoDVz2rv6qWbO-6VgYWtV97AF6PlAdjnSLYRJuGOj8i7go7Xjw9c8XPp_yCSb0dIsqeIAjr51DsQDbe1LAZCuAJt86aB9zdehFFH23sjwLlDURJAxzeP37l-FtTlyeBVhn8bYSeOo-Nuv6fg6ouAdhfi1l4-Tf03eX1X74tYQm7cRAAA6mVhBYw9-qAFAeHF_0-WUDtP10fTnoN6QnbHV4tC3YcxPYgwrvz499fh4vGWfuqda9aTe6JzUPStVXL-fwcsgj8pCNx7x7Aodi2oL9uVXp5RTZHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=QCVaG3MI-tlGwL3sEbhhFtsOSP2NL7kYlAzrMs05o0ImQZYE1p9O7XrU3X6FFP40x2qANVghQqwvCoST6W8jv1--9Rc0pD2WaaP247YY0MV-RaWVVvMDKsPEBjZngK6kfpuyZ5_q-5KcM5V3Ar4B1quqQBMZcJTIu-TztrXCxjHVgxjpmyKqIi_Zne95UW02CTEhAJxQRtOPYRY7_WreWrxP1zi_RmVONND_z-he-qMWU_PC7FMZZ_x0mR-hESVZHr4Kmv6TYzvGWSoW-Ic8TSjj-fSnp_BuAGXKzCHikRkYGB8Mcxi2_ffWkzzKgrvGht8tioawIoFeZYVyOD8dBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=QCVaG3MI-tlGwL3sEbhhFtsOSP2NL7kYlAzrMs05o0ImQZYE1p9O7XrU3X6FFP40x2qANVghQqwvCoST6W8jv1--9Rc0pD2WaaP247YY0MV-RaWVVvMDKsPEBjZngK6kfpuyZ5_q-5KcM5V3Ar4B1quqQBMZcJTIu-TztrXCxjHVgxjpmyKqIi_Zne95UW02CTEhAJxQRtOPYRY7_WreWrxP1zi_RmVONND_z-he-qMWU_PC7FMZZ_x0mR-hESVZHr4Kmv6TYzvGWSoW-Ic8TSjj-fSnp_BuAGXKzCHikRkYGB8Mcxi2_ffWkzzKgrvGht8tioawIoFeZYVyOD8dBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=UEfHslhE6AH9nTrx3BmCVyHU5A-pXLLeiRS1tlm1w7YszdeUR6LCfk9hzS7s6sfF0wY5R3MgodvKlq58tSKFTFjx47koNwD60UxtrkcheHRQCefUyO2-Wl1QOTd7--Hrm4CpSZXSHCj1jZq3ZLWcCitbkqJeLVf18BNPt--wlwNhmuUNzq18C75fdKLKm63Ukf8hVJIVjWbmu34MqqO-8C40Dm9yngv4If7t4zXKuXVCcWZnK5s2q1uCSN40HhRXeIMt6ZIy3GdLSY6prumBBr01OLg92eP4Eu-0syBYhcvNSSZhLWUU7hG7knydufDQvuSSpWUfg28bCIN4yX69EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=UEfHslhE6AH9nTrx3BmCVyHU5A-pXLLeiRS1tlm1w7YszdeUR6LCfk9hzS7s6sfF0wY5R3MgodvKlq58tSKFTFjx47koNwD60UxtrkcheHRQCefUyO2-Wl1QOTd7--Hrm4CpSZXSHCj1jZq3ZLWcCitbkqJeLVf18BNPt--wlwNhmuUNzq18C75fdKLKm63Ukf8hVJIVjWbmu34MqqO-8C40Dm9yngv4If7t4zXKuXVCcWZnK5s2q1uCSN40HhRXeIMt6ZIy3GdLSY6prumBBr01OLg92eP4Eu-0syBYhcvNSSZhLWUU7hG7knydufDQvuSSpWUfg28bCIN4yX69EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9LfVuWY_3QUK3yiDYs5f7Iav06s8K72pVr8Fz4GOdev72YveJmnNaiesImpVO4_BKVJxCPMnu1VEj7243eUEdezt4YLdN6nuONJcCfSQlH1tnyeFxNNeEduDXx5yG5Y8rLIeEPj7E_zUbRCfa8oygQ7GfEyBt1PRWJOjvVK69DWTY78jKDinjD9nX1B6fx2frclgVjR5rYpQuaWzB5QGDCZI-uoI0vgQZeTATNE1tTmBG8q6o2ymIQbQxVxqRFyreRzsOfnLHO7s3ysr5mf8xhFXS7sIRUXeEvNq8X01bo3Bh9oF-rSQXjRQ7zPU6LP4OvCNhrWYgjqZWQNjAQTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=UOidhZPUaBQ9tZVdMUUHgVWZKaB03o2SYnznC_b-sh60Mt5Eyx4zkqCTYEuYVyHYUfSquHRetgs5yugAFs65gZzK6DCk2S3kS528_1VbxWaQDzXU1__ahEI4TGoHm6jPYcUunI6G38F3RFt-YrGrk0T4KKo80CPqOZ2ZTk-uQpDFHpimVCc9PIlYk2F0MOXyPtjEGGyF0q9C3jzYYjxqNTltZpavPhvDlWH8WfPGw6K6b1hS6vbcz1rXtr8Ii5Y9QzU0mwbj9jU1XATiPr5Y4TI2T6Ly9gDLgqiRxzSHiIMgeTEgYMXxu3lIaC6m5A5aAyfOs4kXoELycCAE1Srosw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=UOidhZPUaBQ9tZVdMUUHgVWZKaB03o2SYnznC_b-sh60Mt5Eyx4zkqCTYEuYVyHYUfSquHRetgs5yugAFs65gZzK6DCk2S3kS528_1VbxWaQDzXU1__ahEI4TGoHm6jPYcUunI6G38F3RFt-YrGrk0T4KKo80CPqOZ2ZTk-uQpDFHpimVCc9PIlYk2F0MOXyPtjEGGyF0q9C3jzYYjxqNTltZpavPhvDlWH8WfPGw6K6b1hS6vbcz1rXtr8Ii5Y9QzU0mwbj9jU1XATiPr5Y4TI2T6Ly9gDLgqiRxzSHiIMgeTEgYMXxu3lIaC6m5A5aAyfOs4kXoELycCAE1Srosw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بازرسی امنیتی در مراسمی که تحت کنترل حوثی‌ها در یمن برگزار می‌شود.
آن‌ها به دنبال کمربندهای انتحاری و مواد منفجره هستند.
همراه داشتن سلاح‌های شخصی مانند تفنگ‌های تهاجمی و خنجر برای مردان یمنی امری عادی‌ست
😳
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70668" target="_blank">📅 17:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe281d624.mp4?token=A1BE8ee72Gx69Gx9lXQhMm8KYayg77NyehL0iVrM4tiNTR4HZKXf4vXfoEsVqr2Nkwxir0nOwPRVx_DJVQ34BN4DvwMZLyGKszO0cam0y1knko0aELv55AXAqjHGEuxI98uOSpIrwirWU8q4wTn7e3P4NW00tXFkLXX983iO8-VXtIA2yHIPZg0uoXXNsdta7LNgT7h68HE_5cwffH5DzpUwIUrHBb6m7iwYomh1K2nfsFTlFXV9r7QSldiJvSegz1Rt8drsieSAF2EUj1YA3hUcWmG9Hqw-SZWb1NXTl5R9favXVUXTv_oqlDo-3ENNldX8I_VvQHZdswZZvx_UtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe281d624.mp4?token=A1BE8ee72Gx69Gx9lXQhMm8KYayg77NyehL0iVrM4tiNTR4HZKXf4vXfoEsVqr2Nkwxir0nOwPRVx_DJVQ34BN4DvwMZLyGKszO0cam0y1knko0aELv55AXAqjHGEuxI98uOSpIrwirWU8q4wTn7e3P4NW00tXFkLXX983iO8-VXtIA2yHIPZg0uoXXNsdta7LNgT7h68HE_5cwffH5DzpUwIUrHBb6m7iwYomh1K2nfsFTlFXV9r7QSldiJvSegz1Rt8drsieSAF2EUj1YA3hUcWmG9Hqw-SZWb1NXTl5R9favXVUXTv_oqlDo-3ENNldX8I_VvQHZdswZZvx_UtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خنده‌‌های علی مدنی‌زاده، وزیر اقتصاد در واکنش به فشار گرانی‌ها بر مردم
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70667" target="_blank">📅 16:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70666">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=ETCwnZX7HiCePNaYkwYgT12OMg_hbNVW2wI2zp8_1gUHQZ4eyOoRpedq-QhOmKs30vvDnZKg0JHE38wbYJtbHLfwvbeKX_Oe5yfNn0rQip_bipJ06rRKonz7ZRu9Cbpk4BHBKjFDacQfzHLneWKyYnoSbri8z-PB1jrWIeDakchp4w9B_0jZ1_RE57S19LTjHuuGx_7AJg3E2KctJpr04KzYTShGNQyL5QbObRAcplrNBCfmNF89t_bRy-kADSWGX9DPuLxww97fZ3C130IUk-hXoBH3_E7qORkhTNB8nwZ6_aOlCJRes7gc04RZnDxHBG5KOuaUzZh6cqrpccwXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=ETCwnZX7HiCePNaYkwYgT12OMg_hbNVW2wI2zp8_1gUHQZ4eyOoRpedq-QhOmKs30vvDnZKg0JHE38wbYJtbHLfwvbeKX_Oe5yfNn0rQip_bipJ06rRKonz7ZRu9Cbpk4BHBKjFDacQfzHLneWKyYnoSbri8z-PB1jrWIeDakchp4w9B_0jZ1_RE57S19LTjHuuGx_7AJg3E2KctJpr04KzYTShGNQyL5QbObRAcplrNBCfmNF89t_bRy-kADSWGX9DPuLxww97fZ3C130IUk-hXoBH3_E7qORkhTNB8nwZ6_aOlCJRes7gc04RZnDxHBG5KOuaUzZh6cqrpccwXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یک طرفدار حکومت :
قیمت دلار همینطوری میره بالا و ارزش پول ما همینطوری میاد پایین
ولی این میتونه به نفع ما باشه چون برای اون خارجی محصولات ما میتونه ارزون تر حساب بشه و بیشتر تحریک بشه تا کالای ایرانی خرید کنه
این یعنی فروش بیشتر بیکاری کمتر و چه بسا درنهایت مهار تورم و توسعه اقتصادی!!
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70666" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70665">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfy--TkM2zG-_QXdvBiSeF1HK4ieY7ccu7QAArQm-otHrVLhc8XBM4ILX9fqmaFULN5Ukn7F-zacqQUSZmJ2QVq0Iw1-w13vWLuhTOExJu7qkthdk1w8XcWfhtVW0g1PkAUfEvSFLdNgxkut7Sx_tC8RnoKUtwbDp32RN55grVNHQlyQhGxWTSgNtwMRTA_3RJm-YKUCjmQRr0KJHFdK9hRerXZOlGF29PYBcJsHuDt9caiOPrsKaoijHTSFS1mIoiuLM7kVzoY-BFYpTYiRM6m3q0cFmrmKvzkCuv9I5ROenI-qH91BZFFsYgVLgnx9kjQEAspXHpZK6tcQd0zZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
📰
سی‌ان‌ان:ناو هواپیمابر USS Theodore Roosevelt همراه با حدود ۵۰۰۰ نفر قرار است در هفته‌های آینده به خاورمیانه اعزام شود.
این استقرار حداقل ۷ ماه پیش‌بینی شده است.
جان پریمن، Master Chief Petty Officer نیروی دریایی آمریکا، گفته خدمه می‌دانند مأموریت بیشتر از هفت ماه خواهد بود و فرماندهی به آنها گفته برای ۸ ماه برنامه‌ریزی کنند.
این اعزام را در ارتباط با فشار عملیاتی ناشی از استقرار طولانی USS Abraham Lincoln قرار داده؛
لینکلن بیش از ۲۵۰ روز در دریا بوده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70665" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70664">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=K8w_PK1dODZY2rDT4-IiUug-GeaySMtw8TcIjm5jA1cfKqlH7-MpaAJL7DNrmvpW3og36yn21n4FeHzkNDpwNp912DXUfi-G-UWFGhqC-3UaAhyXBIF8bXi2sblnPl40Oll3XXz9G_1_iH1eZlaxv7OtHGxFgVD8cIcF8p7hdovGGfRuOB1K7PsqOlIIV9PJVIpSef0HADWnFyg27wSEiJ3LHNf9I25Z_Oj1FbTI3C-fegTi5UebpiO7BFzraLqsVNEKg2PS2X9inY8kvAP83SZgVuQ3T3TCxMFdM79LGlwfcp4wsPLk2KT_joO3xom7MHJnKz93Wo1Fr3DFGAvR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=K8w_PK1dODZY2rDT4-IiUug-GeaySMtw8TcIjm5jA1cfKqlH7-MpaAJL7DNrmvpW3og36yn21n4FeHzkNDpwNp912DXUfi-G-UWFGhqC-3UaAhyXBIF8bXi2sblnPl40Oll3XXz9G_1_iH1eZlaxv7OtHGxFgVD8cIcF8p7hdovGGfRuOB1K7PsqOlIIV9PJVIpSef0HADWnFyg27wSEiJ3LHNf9I25Z_Oj1FbTI3C-fegTi5UebpiO7BFzraLqsVNEKg2PS2X9inY8kvAP83SZgVuQ3T3TCxMFdM79LGlwfcp4wsPLk2KT_joO3xom7MHJnKz93Wo1Fr3DFGAvR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیزدهمین فرزند مادر ۳۳ ساله بدنیا اومد
؛
از مرده میپرسن چرا این همه بچه حالا جوابش:
اساسا بچه ها رو دوس دارم من ، هزینه هاش؟؟ هزینه هاش با خدا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70664" target="_blank">📅 15:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=jlbg68jatG5XawU-A7JuGc5LEWh0M5W934j9NM3pMO_S9MV9QD6TwxKHgSrlgJxVXkV4ELyHYXBDFd4_9teXLdz8YMyZf0_7MFGdXTKRsrEMzfM99YUHUnZhasOS-yn7orQLDLhGHtnx9Yo0lHCI1Jxv_b8WLllFgdIDuuYJRHGbZVaDj3DvfglMwMq_0TlW5tqx8eGIVmFkP9kVzkq15kM1cjUPo9F6r9BNwbqQcu91U8YBX-KUhDZaBR_VqPDyRjCDtsZ4ZvAKzHe-QarcbtsgBmBWCa45BYYz9zAvtEoeoNKc98bcSU7zQAVoII81vqPFKv2G2thQt6Z0QvaLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=jlbg68jatG5XawU-A7JuGc5LEWh0M5W934j9NM3pMO_S9MV9QD6TwxKHgSrlgJxVXkV4ELyHYXBDFd4_9teXLdz8YMyZf0_7MFGdXTKRsrEMzfM99YUHUnZhasOS-yn7orQLDLhGHtnx9Yo0lHCI1Jxv_b8WLllFgdIDuuYJRHGbZVaDj3DvfglMwMq_0TlW5tqx8eGIVmFkP9kVzkq15kM1cjUPo9F6r9BNwbqQcu91U8YBX-KUhDZaBR_VqPDyRjCDtsZ4ZvAKzHe-QarcbtsgBmBWCa45BYYz9zAvtEoeoNKc98bcSU7zQAVoII81vqPFKv2G2thQt6Z0QvaLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش یه دختره اومد از خودش ویدیو تولد بگیره تنهایی که یهو یه 207 اومد کنارش و سه تا پسر اومدن وسط رقصیدن و تولدش براش جشن گرفتن
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70663" target="_blank">📅 14:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70659">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9xolXzjVf0GZR9oYai53nuo80o5wzaVhKxbUSn9uMIg9JlA00WvV7Ew-j0oRJetlwO0Q7YFgehvjNH170n24jOya92HXDdED4Ac2R_jljCHNd_7v_qw4GgjVpaRO6KM459NmqMhXsIa-fpGNeBhxq-s8dDJLCbTmY2BrWoKdRKVLkwebWSuqdSjdz9bE3F-9xbGqUyMpJWbPKoSoenkRMWUezx8KcvppH3YaUAjbbknr48AdEOJeEYdnHfbqmagtp9QCiBX7qXhqgw_sWjlCvacBRFip1djhaD11zjN1lBkD7IqOWj7xBMElxLX3d8Yc9SOXVo6BNkLOxJBdHOO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bC8OrpnNgaNEqFbVF55_I93RjgWnjSSdoz--HuGeCllvrSgBoAaDB-F_KmaBBmHORcJKS7GGZSN_bpyiLKNW1rV2lYLfc3Fw135dfozP7zo_NXr7VoL32W130lIxecDLGn5yeswhW1MTkGpBOOfIlpNXZItoCP1lGrVMTldu8khMjirMLv1BUhDZFAQ7BaHq52iMUT0CS5iqaNUdOIoJz6AwX9_pxnqfKEcKfQmYC8jjAWDWuRJJfipQ54wcZNg7zqLH00gyZo-_kjweRps5YgbUQuEuqhrlV_Wne9Tb8dM6aEOhihBk1CQJXgukkHTQEXWUcGadOaxFQYAWc7lpnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=cETFojY6oR28x6Hk1VW0YI1LvLofMDb4Yz5aTb-qlzO8BhXAz_bEW96YXJ3fjypMLFfNKlfnwAWPyLAeu_nRL0cmbqQ3bjHlmNZburQLV1UF14fp4etYWGNt-mLriLTQZLsnAq12sHRrbWCEPj9ADQGGicUOI5jvZoTHGdf7PEay8i-gBRUFpPSJX4fxVEDdNSycAiW4sZhWCrFsh-ANxxh4OaYok4OFAlDWQIiG4jNfEaUujczI1VQFLg8dGf1upc9DWRa9u60YSiW--D6bZrBMxFMGNwN7LL4NQWpZ6f86MBP_xuvOyaj4kfbqh4tX9NTEaXsVKqvcRHLNfyHqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=cETFojY6oR28x6Hk1VW0YI1LvLofMDb4Yz5aTb-qlzO8BhXAz_bEW96YXJ3fjypMLFfNKlfnwAWPyLAeu_nRL0cmbqQ3bjHlmNZburQLV1UF14fp4etYWGNt-mLriLTQZLsnAq12sHRrbWCEPj9ADQGGicUOI5jvZoTHGdf7PEay8i-gBRUFpPSJX4fxVEDdNSycAiW4sZhWCrFsh-ANxxh4OaYok4OFAlDWQIiG4jNfEaUujczI1VQFLg8dGf1upc9DWRa9u60YSiW--D6bZrBMxFMGNwN7LL4NQWpZ6f86MBP_xuvOyaj4kfbqh4tX9NTEaXsVKqvcRHLNfyHqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ایرج مصداقی از نزدیکان شاهزاده رضا پهلوی در یک مصاحبه درباره علی کریمی صحبت کرد؛
صفحه اینستاگرام کریمی در اختیار شخصی به نام امید دانا است.
بعد از انتشار این صحبت‌ها، کریمی در چند استوری به‌شدت واکنش نشان داد، از مصداقی خواست ادعایش را ثابت کند و شاهزاده رضا پهلوی رو مخاطب قرار داد و برای اظهارنظر درباره این موضوع ۲۴ ساعت مهلت تعیین کرد.
⏺
مجدد مصداقی در ویدئویی جداگانه به واکنش‌های کریمی پاسخ داد و اونو مخاطب قرار داد؛
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
⏺
علی کریمی هم در ادامه اومده گفته؛
از اين لحظه به بعد؛
از هيچ شخص يا حزب سياسى حمايت نميكنم.
در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد.
این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.
به اميد آزادى ايران و مردم نازنينش
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70659" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70658">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLLm_gAbnYK3hStQN7S7_LqEUSMDQqu4KnlrIMX9XPBJfoP7iTgCmpm6NoCOa2s5sjxd7QfGvmSd4xdd5_EiwWzAkl2tY9gXkzf7_yic3l7VNNmr_5XcEPfXlRYsviDBfNQdmYtSyBDjCjjWIzKlVjkZECi_fkEmeG_vyCwMqhj2w6unvy_8e-WBofwaQsSKvhDDpcBCgGbLuOYMgAk_R_7Vmfs5tjWWA8QGEK83CiCeg9R6zwNfID1-3gTzybCBzeRqrHxjAp7SrUsix0hitZs1mS4c-nwVXMMrul0A7NfMWX0TeOP4didW74j28QbxhlL9cdZDqu4FQ6LBKITc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
وال استریت ژورنال:جان رتکلیف، رئیس سیا، این هفته در سفری غیرمنتظره به مسکو رفت تا به روسیه هشدار دهد که به کشورهای عضو ناتو حمله نکند.
این سفر در پی ارزیابی‌های اطلاعاتی جدید آمریکا انجام شد؛ ارزیابی‌هایی که حاکی از آن است که پوتین ممکن است در سال‌های پیش‌رو، با انجام حمله‌ای محدود به یکی از کشورهای متحد، عزم و اراده ناتو را محک بزند.
مقامات آمریکایی نگران سناریوهای مختلفی هستند؛ از حملات سایبری گرفته تا تهاجم زمینی در مقیاس کوچک که به احتمال زیاد یکی از کشورهای حوزه بالتیک را هدف قرار خواهد داد.
آن‌ها همچنین نگران آن هستند که کاهش ذخایر تسلیحاتی غرب — که ناشی از سال‌ها حمایت از اوکراین و درگیری‌های اخیر مرتبط با ایران است — بتواند بر محاسبات مسکو تأثیر بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70658" target="_blank">📅 13:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=AXSazQeBqp0hSequvDk6ojrUOI0C2esF_sN5KGuyOBE0p3gn7Ir6WXqQm52yd_9jJYZx2vdz-A_eqZv-3HtUa23WpkfSKlS_p0x2iy_2z-VFsYe372hQ7b0OWpOPwOPAqUGT_Y8QA1w1f1H6H4RuNR0gQEZ0D4zhvkPx5UVYHNmuglfc4_RVKapte9tbi-PvYOS47ojqBxfGyrJgcVkHMnFhg58_2RENEIh0Ps5hViMoQpjyFcwd99YBpW95eYj8CiDHL9qtx3LiE8OjHW961KoBOH3fd-oA8Xt0rgT_By3RIYEgJuBj0MglxH6OWmqJzdqkSY0uskFdgYJl_V8sMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=AXSazQeBqp0hSequvDk6ojrUOI0C2esF_sN5KGuyOBE0p3gn7Ir6WXqQm52yd_9jJYZx2vdz-A_eqZv-3HtUa23WpkfSKlS_p0x2iy_2z-VFsYe372hQ7b0OWpOPwOPAqUGT_Y8QA1w1f1H6H4RuNR0gQEZ0D4zhvkPx5UVYHNmuglfc4_RVKapte9tbi-PvYOS47ojqBxfGyrJgcVkHMnFhg58_2RENEIh0Ps5hViMoQpjyFcwd99YBpW95eYj8CiDHL9qtx3LiE8OjHW961KoBOH3fd-oA8Xt0rgT_By3RIYEgJuBj0MglxH6OWmqJzdqkSY0uskFdgYJl_V8sMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از خونواده‌ها میپرسن چقدر خرج کنکور کردین برای بچه‌تون؟ رقما به شدت عجیب غریبه.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70657" target="_blank">📅 12:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWHFg92jGlWmkD7fkqT9TsTUMJT2hKgYKzfEt3ZzgAefYTkvGQ1XgEYDLli-fJSLdR2fq0vGkeEQ-chQPNwbISUy2_c39gzGpBBW8wluqJeY78tqsiL4s9hVIY-XH0s0RsbhJSbeOXyqWkJC2VJ_1riWCbs7KCFKd1lUKN2XJCMGqPWy72TboiKakD4aGNy6LRcPhWAyxyTUk6gA8bnobrle1_vk1OrgG9b6sE5oZtiKe5DsRfXwrvoNHlSKljWBnBgDf2veZS11MCxC7muuk2kUB9LHliIE7AVghZofHT-ePqA-X3lTuwmBSjyWzRAm2COeHbft1L7eY9N8ec-y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی دریافت کردیم مبنی بر اینکه یک نفتکش در تنگه هرمز هدف اصابت یک پرتابه قرار گرفته و در پی آن دچار آتش‌سوزی شده است.
آتش‌سوزی در نفتکش در تنگه هرمز مهار شده و تمامی اعضای خدمه در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70656" target="_blank">📅 11:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=VKFFNYfEEVbfH5GVq6iVe0bp_ZA4wMRY_UG5KdqOefRMoCVQl-_B-VYxMGo5FX6JaxpbPE3a0U9SQ1TsTu6s7Z_BsY-ViixhvCR3vJrsVRwwVe1Bap2pCbJPkapE8lNoaSmoltAVGn19fZFMEqi0PgN5Bk51wS9MEulIeFbzh0LXSEnjfC7kMOFOUvZHmUdElO7dCcLpYfywoITIGeSrJhkPDD1x1hGLHUS0A61VK7V1DBTBVV83kHUF8ShCK7a2qS-FLvuyEqWIxD_a9WfMujYuyFT1ZbYiZOvyRG23e7Lx084qgDxgyxusJYQqAwI5b23_XWNS8yG7ZbNgWGQI0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=VKFFNYfEEVbfH5GVq6iVe0bp_ZA4wMRY_UG5KdqOefRMoCVQl-_B-VYxMGo5FX6JaxpbPE3a0U9SQ1TsTu6s7Z_BsY-ViixhvCR3vJrsVRwwVe1Bap2pCbJPkapE8lNoaSmoltAVGn19fZFMEqi0PgN5Bk51wS9MEulIeFbzh0LXSEnjfC7kMOFOUvZHmUdElO7dCcLpYfywoITIGeSrJhkPDD1x1hGLHUS0A61VK7V1DBTBVV83kHUF8ShCK7a2qS-FLvuyEqWIxD_a9WfMujYuyFT1ZbYiZOvyRG23e7Lx084qgDxgyxusJYQqAwI5b23_XWNS8yG7ZbNgWGQI0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇴🇲
🇺🇸
کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، درباره دلیل و نتیجه نهایی مذاکرات عمانی-ایرانی:
ما گفت‌وگوها را با عمانی‌ها آغاز کردیم تا بتوانیم به آن‌ها بگوییم که حداقل در روحیه همسایگی، این اقدام برای باز کردن مسیر جنوبی می‌تواند یک‌بار دیگر تنش‌ها را ایجاد کند، فرآیند اجرای توافقنامه‌های اسلام‌آباد را مختل کند و حتی منجر به شعله‌ور شدن درگیری‌های نظامی در منطقه شود.
​
انتظار ما این بود که با کمک دوستان عمانی‌مان، شاید بتوانیم این مسیر را ببندیم. با این حال، فشار آمریکایی آنقدر شدید بود که متأسفانه این مسیر جنوبی بسته نشد.
​
سپس آنچه رخ داد را دیدیم: جمهوری اسلامی ایران تصمیم به بستن تنگه هرمز گرفت و در ادامه، شاهد درگیری‌های نظامی بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70655" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=cXs35ozJFsfV0znQTVL3G6LijnKpFxzN7EMA5e0vgHQr_iUb_6wedzmYs_i07B2APKM2aZiLkJu5Aq3FZ-cR9IXYSzjgA93HO3r7Pkk9ZuAmPFKX5V5x5vYohlrxH3WvrPgpqByCFaOfsxt_34ymDOZRwPSErjIrqDC63ST_rVcs1qUV_elFli1fSF5V9NZEwQtNXxKD5lT1pqJ2s9xZNSmUGaEp-cenKh1EDsfY6WmDIHQkrf19O452ZyIQQOZ1zBt9mwmrrR6WwX6nRaZKWRtqPFckDbYYx1h9KfJ8dK2fCIUUhP78AA6L-yY5y6tCcdI3SHL_9mns_gx6RDiDGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=cXs35ozJFsfV0znQTVL3G6LijnKpFxzN7EMA5e0vgHQr_iUb_6wedzmYs_i07B2APKM2aZiLkJu5Aq3FZ-cR9IXYSzjgA93HO3r7Pkk9ZuAmPFKX5V5x5vYohlrxH3WvrPgpqByCFaOfsxt_34ymDOZRwPSErjIrqDC63ST_rVcs1qUV_elFli1fSF5V9NZEwQtNXxKD5lT1pqJ2s9xZNSmUGaEp-cenKh1EDsfY6WmDIHQkrf19O452ZyIQQOZ1zBt9mwmrrR6WwX6nRaZKWRtqPFckDbYYx1h9KfJ8dK2fCIUUhP78AA6L-yY5y6tCcdI3SHL_9mns_gx6RDiDGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعارهای عجیب حامیان حکومت در تجمعات شبانه:
دلار شده 200 تومن همتی
یه کاری کن میگن تو بیغیرتی
حیف که نمیشه بکنیم به تو بی احترامی
ریاست محترم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70654" target="_blank">📅 11:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45450621ea.mp4?token=iIW_Opgwql9m1IHoG4SAKHheqM7md8D2AvHC7Jnr87nLNdhRKfqyqHDD6ZVGe7PhGO_UAFM46PzwAg9e5JumRh0qfo2sPO6bd06PzK5BPwKRrI2GNQWXHaDL2tb_grdEkyE_sucjDb5_ZDnreKZ4X_qLBXMLx4L36SxJMD9sAbDw6agg53n8JYGDnR-efKBZxr13GV32-LZGu_uHcWlu_SGpM4QDJS3IBUZPYJGPGuErbMcq7xsp61EUpVpJbXcQKzC-ilpc2pRsb5u92XkC1oU0FImUphW2e8ZwrJ87SGD5szouLLJv1FfQRukHJ-mPIE_ohuwfpPS7yIlaaR_6mTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45450621ea.mp4?token=iIW_Opgwql9m1IHoG4SAKHheqM7md8D2AvHC7Jnr87nLNdhRKfqyqHDD6ZVGe7PhGO_UAFM46PzwAg9e5JumRh0qfo2sPO6bd06PzK5BPwKRrI2GNQWXHaDL2tb_grdEkyE_sucjDb5_ZDnreKZ4X_qLBXMLx4L36SxJMD9sAbDw6agg53n8JYGDnR-efKBZxr13GV32-LZGu_uHcWlu_SGpM4QDJS3IBUZPYJGPGuErbMcq7xsp61EUpVpJbXcQKzC-ilpc2pRsb5u92XkC1oU0FImUphW2e8ZwrJ87SGD5szouLLJv1FfQRukHJ-mPIE_ohuwfpPS7yIlaaR_6mTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
سخنان جالب امیرعباس هویدا و آمار ارائه شده توسط وی درباره وضعیت ایران در آن زمان .
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70653" target="_blank">📅 10:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
اعترافات اندرو تیت (بوگاتیت چه رنگیه) و داداشش تریسان تیت :
اون زندگی فوق‌لاکچری که از ما تو فضای مجازی می‌دیدید، قرار نبوده واقعیت کامل زندگی‌مون باشه؛
ما داشتیم یه نقش بازی می‌کردیم، مدل کارمون اینه که هرچی محتوامون عجیب‌تر و اغراق‌آمیزتر باشه، بازدید و لایک بیشتری می‌گیره و در نهایت پول بیشتری درمیاریم.
اون بوگاتی‌ها و استون‌مارتین‌های چند میلیون دلاری که تو ویدیوها می‌دیدید اجاره‌ای بودن و اون سوپرقایق تفریحی 50 میلیون دلاری هم مال ما نبود؛ برای تبلیغش پول گرفته بودیم.
حتی خیلی از حرف‌هایی که درباره ثروت عجیب‌وغریب یا داشتن چندین پاسپورت می‌زدیم، بخشی از همون شو و شخصیت اینترنتی‌مون بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70652" target="_blank">📅 10:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=MEjWkGtd0kWih5G8OVaRASr_yYpv3Eccd2oVIwCft_d541B_iE12OTyWo7lcyOQb2n7LwIzh3tltTviQnKnp195yCoSJ6LlrFEyrvIoYuFn_pix5ZRjN6l22RAftutFiDoEl0jRGfUGSLBp_aprkbbcD7Vny49e9Sa27DZN_ikKKHheN5dOim9PqQcIMRtLuW17hY_YHScxgNyZscOez2WtDWZYSSDibE_JYlqBVab9EHkzjtluKalrYPzKS-yFgPAjBjxUlCKlG4lhCRd5Z92WKOXrQACTeUPB_oDR6Roc_2AF-D52ZxxaOgZ3A_6K7vNXIsf4xWt-ylpGk-E7v7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=MEjWkGtd0kWih5G8OVaRASr_yYpv3Eccd2oVIwCft_d541B_iE12OTyWo7lcyOQb2n7LwIzh3tltTviQnKnp195yCoSJ6LlrFEyrvIoYuFn_pix5ZRjN6l22RAftutFiDoEl0jRGfUGSLBp_aprkbbcD7Vny49e9Sa27DZN_ikKKHheN5dOim9PqQcIMRtLuW17hY_YHScxgNyZscOez2WtDWZYSSDibE_JYlqBVab9EHkzjtluKalrYPzKS-yFgPAjBjxUlCKlG4lhCRd5Z92WKOXrQACTeUPB_oDR6Roc_2AF-D52ZxxaOgZ3A_6K7vNXIsf4xWt-ylpGk-E7v7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکنا گزارش داده یک فرد که بلاگر اینستاگرام هم بوده، عاشق ماشین‌های مدل بالا بوده و توی دیوار دنبال آگهی ماشین‌های گرون می‌گشته.
با صاحب ماشین قرار می‌ذاشته، می‌گفته یه دور تستش کنم و بعد با ماشین می‌رفته!
نکته عجیب ماجرا اینه که بعدش زنگ می‌زده و می‌گفته من دزد نیستم؛ چند روز با ماشینت دور دور می‌کنم و بعد سالم پسش میارم!
ظاهراً هدفش فقط لذت بردن از ماشین‌های مدل بالا بوده و بعد از چند روز هم ماشین رو سالم برمی‌گردونده!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70651" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=Nfw0vxK4Hktt5bG_afof0rQR2l-ZWmSYRLhMrZqAiU_Eb5mlr7-Zko2UwRrA2cLBE4hBdLj3FtZXUAQ9Iq_yj0Q5GlSbggUrmRLOE_qCntsABn4BRxg6x_JL7vRkDvzPrx7Oz4mPgTlXKxtBVk8uvThrq-2icBcJuYPMAHWM3KwKIE3WMBh-orUB4_0ikvKQKbhHpJMnSCpRysm3pbZNpSfJsE_T4EMX8qWqgoc5JazcKGBu5iTcPnFlAgGKVuLInnqULl6-KDcKB_1tdpjULwPFXDHgEPT8OqL42x2AwPR-99Saqp1MiYUNc8anvVdAL_6AawVi0Ccdv5aT7nvD2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=Nfw0vxK4Hktt5bG_afof0rQR2l-ZWmSYRLhMrZqAiU_Eb5mlr7-Zko2UwRrA2cLBE4hBdLj3FtZXUAQ9Iq_yj0Q5GlSbggUrmRLOE_qCntsABn4BRxg6x_JL7vRkDvzPrx7Oz4mPgTlXKxtBVk8uvThrq-2icBcJuYPMAHWM3KwKIE3WMBh-orUB4_0ikvKQKbhHpJMnSCpRysm3pbZNpSfJsE_T4EMX8qWqgoc5JazcKGBu5iTcPnFlAgGKVuLInnqULl6-KDcKB_1tdpjULwPFXDHgEPT8OqL42x2AwPR-99Saqp1MiYUNc8anvVdAL_6AawVi0Ccdv5aT7nvD2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
یکی از زیباترین سخنرانی‌های محمدرضا شاه:
هیچوقت به زندگی فعلی خود قانع نباشیم و دنبال بهتر کردنش باشیم.
برای بهتر کردن شرایط زندگی، اولین شرط خونه و سقف بالاسر هست و بعدش قدرت خرید مردم.
محیطی که در آن زندگی میکنید باید شاد باشه، غذایی که میخورید لذیذ باشه و لباسی که می‌پوشید تمیز و لطیف باشه‌.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70650" target="_blank">📅 09:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70649" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=LUEtFl1ynN82yDmGMZFVDx7U-1xELvq030Y-aQtWTC7haXr1bwLKQKyI-uxYyBtL2alBFHVX9hN-tFvafWB_wu_R0IzmgSeRDdqP6wf1pQ0aUpYkLrqU1Zwkz_rDfqd58AVahd39Ic_GKb1VhcRN-KFMn26_SUrEupfm8aStRhDb0XRNrHYp-x9L3-vP9W4Js3FKHeGZeODYj4BR7nYjxTNdUKBaDgfKNK-NGFcGcKKnxv86pa4kKX_mZJ0MWz8CVsvv5crcHrliElM2pkRijQbHynChh_NFmek5knVHFn4jMCFce6ZoISy5FPtLAo3BDiGGvyDTEgLfgvSw-tOgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=LUEtFl1ynN82yDmGMZFVDx7U-1xELvq030Y-aQtWTC7haXr1bwLKQKyI-uxYyBtL2alBFHVX9hN-tFvafWB_wu_R0IzmgSeRDdqP6wf1pQ0aUpYkLrqU1Zwkz_rDfqd58AVahd39Ic_GKb1VhcRN-KFMn26_SUrEupfm8aStRhDb0XRNrHYp-x9L3-vP9W4Js3FKHeGZeODYj4BR7nYjxTNdUKBaDgfKNK-NGFcGcKKnxv86pa4kKX_mZJ0MWz8CVsvv5crcHrliElM2pkRijQbHynChh_NFmek5knVHFn4jMCFce6ZoISy5FPtLAo3BDiGGvyDTEgLfgvSw-tOgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a4
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70648" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70645">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff574e553.mp4?token=VTdJgmeolbMwoFk6Oes3szNj4sT2TrsozsMVgjnx25hJDpeSU0o0Zh68CBlOsLhXMakflDj40_75EqBHMOSho2E6-mjqC5HEqz5JCmwNas6zGGd1SddZfK7eokHjVH4pLY7Nm3hGZdFnjbTk1R37reJ4ZxdEw3AdaNv5844xEYGO1RMnM0HcpTDUGTVTT4iypTNZmXfmVZJVCfeTC4Gu7zoeJ-CC3lpEE5do1N_LjdD9wbqqUvEqnRHcev1U6OTkTVo0HMd7wAG3MZrk5OJpqVprbEN4m_EjW7jNOC9SByr6V0deGZIM0KUZalXPZnDOXkkd8w-j8l_KR_jsXnS30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff574e553.mp4?token=VTdJgmeolbMwoFk6Oes3szNj4sT2TrsozsMVgjnx25hJDpeSU0o0Zh68CBlOsLhXMakflDj40_75EqBHMOSho2E6-mjqC5HEqz5JCmwNas6zGGd1SddZfK7eokHjVH4pLY7Nm3hGZdFnjbTk1R37reJ4ZxdEw3AdaNv5844xEYGO1RMnM0HcpTDUGTVTT4iypTNZmXfmVZJVCfeTC4Gu7zoeJ-CC3lpEE5do1N_LjdD9wbqqUvEqnRHcev1U6OTkTVo0HMd7wAG3MZrk5OJpqVprbEN4m_EjW7jNOC9SByr6V0deGZIM0KUZalXPZnDOXkkd8w-j8l_KR_jsXnS30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهروندان اسپانیایی ساکن منطقه "سئوتا" به ساحل "ترامپولین" حمله کردند تا مهاجران را بیرون کنند و اقامتگاه‌های موقت آن‌ها را تخریب کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70645" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70644">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJj-j-Ezcc_9o--dvE5jA2BSu61k4W2gMCA2LRwUWcPx0tRC0tMYFnMJYxz5LAB-HaaY4ZSX-L4RFKMyRwJD6Q0FmW7LZN96Ps8ubuuZ-7PPCehmKvSKHhqWvdJ3Kj_KPFcmCxaxhvXFlzXzA8HSQQEEQhiFP0PODc5i5dNQKLPkJnl5fVzblq3DeBNalyzC7x0mauqOBGjZX-H1aHh8IdJm0Mki2fMapMkSyVQSixrj5UNtl0JIFjsbERq4FcoYOFiW3P6Ove8ayzpJTdgI0PbBbjp1ncsYtbIuxSF6s47KZlmDjlnFdmDouViB5f9kNnrdSzZT28HiZCrdS3U3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا ناو «یو‌اس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد.
پس از ماه‌ها جنگ — و بیش از ۲۰۰ روز بدون حتی یک بار پهلو گرفتن در بندر — این ناو اکنون برای استراحت و تجدید قوای خدمه، راهی تایلند است.
مأموریت: نمایش قدرت.
مأموریت فعلی: نمایش تعطیلات.
«خسته‌ام، رئیس.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70644" target="_blank">📅 01:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70643">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3143921715.mp4?token=Jg5A1qSF9X0VqLRjNYh_zVfEGeQZkZagAaG_dTin8o4VqMjr6iZsN-QNd69p5-CSqsfyjJru0x_3QNLj5rhGo96ySSxObwFUO9m-HJ3UE9pNARoQzdKiDKtIql99B4y3ZIHpuoWlksrwwvzq_Q-SIQPLijZBxFMNB70nVtnHTu6rGpgmR5YV8a0IfislOVtTuzux-mqkYBwadJ07_lFQP0wcScs2I2N48IOGOhScZWeAnEd5NxDldP99fZ3j8qvgmHRGqy9JT0bOHq74MljR-2DAFFYjn9yKV9mJvwnEmr_o1kjPNGUPnxKhxKRf__rWVbZDx8CevRqrav09lPSD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3143921715.mp4?token=Jg5A1qSF9X0VqLRjNYh_zVfEGeQZkZagAaG_dTin8o4VqMjr6iZsN-QNd69p5-CSqsfyjJru0x_3QNLj5rhGo96ySSxObwFUO9m-HJ3UE9pNARoQzdKiDKtIql99B4y3ZIHpuoWlksrwwvzq_Q-SIQPLijZBxFMNB70nVtnHTu6rGpgmR5YV8a0IfislOVtTuzux-mqkYBwadJ07_lFQP0wcScs2I2N48IOGOhScZWeAnEd5NxDldP99fZ3j8qvgmHRGqy9JT0bOHq74MljR-2DAFFYjn9yKV9mJvwnEmr_o1kjPNGUPnxKhxKRf__rWVbZDx8CevRqrav09lPSD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شکار شکارچی
اپراتور پهپادی روسیه توسط یک پهپاد FPV اوکراینی کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70643" target="_blank">📅 00:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCXhGP5lqy8I0m24MrpoFKr4P1na36_-ya9Tsl0bzlWWb6JypwXZ_Z77ORUQc8mE1KMS_bs8UefpolWFkRA2jcHfxix_YpPHCMm9-J2ISWV1dhVFDGAJ8EtIi1KSeVPE0HZg7LpO034rTMBTML3_aVnRIqzvZzfX6ZdxkXB9oRSFcUzFNIv3tNQXUT_U6yda54apaL7l9LnRrgPfCGGayev_1VI0Ch7Awvw-vmqrBdvEz7jJ6DS1JkWCMTOiLG5RLvjuiM4-uN42aGHw-BnqART4M2z5qOM_lwIb9ExfJEw5SN3sM61uEfvikZ0CK-Y04nh4Pab2Fdnm4-lTgPgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=DpOFPb1U05tM-LjPRM4GTJxZmxEWucClTsezWEp6-b52J-zfS9lybparup3NsK6AIjb004PjOakfdNbsEGeyO4dP6C4neA5aYEUBIi1Q7zLDW7XNrWjssYloEVffUrzRUel0LRX3ZjIwg1l479qVN1J6sIvgiwtXbqhUFOeXTuKct4_4-gju2OiacFV4K5GlcbWo0aVHFWM3QgWf6OMQb0ZvNRblxMzG8JZJ0tx59YJSZpItBSBGdBsKZLsqOMXMcOQXRsL2SMkK6rIIWOPaCdEYHXfboBnxmU91TxH9NXO8fflMZgqMtu2hFYzJveJwL1sV9kft5OlwLGcsjEwafg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=DpOFPb1U05tM-LjPRM4GTJxZmxEWucClTsezWEp6-b52J-zfS9lybparup3NsK6AIjb004PjOakfdNbsEGeyO4dP6C4neA5aYEUBIi1Q7zLDW7XNrWjssYloEVffUrzRUel0LRX3ZjIwg1l479qVN1J6sIvgiwtXbqhUFOeXTuKct4_4-gju2OiacFV4K5GlcbWo0aVHFWM3QgWf6OMQb0ZvNRblxMzG8JZJ0tx59YJSZpItBSBGdBsKZLsqOMXMcOQXRsL2SMkK6rIIWOPaCdEYHXfboBnxmU91TxH9NXO8fflMZgqMtu2hFYzJveJwL1sV9kft5OlwLGcsjEwafg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇳🇵
ویدیو هایی از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
ویدیوها عمق فاجعه رو به خوبی نشون میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70640" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=NqrW57DRa9rhj0t1SYdCcNiKiaxCa-0LDASVkHQqDRiltbaj477obGrgJbfJ4xpdAmILPfKI5OtrXKNP3I6mOABfo7lSiO1PQhEHimehDPKutPQZJIa-ht5P7RsotZYui47tdqq1KyGMiocvJBh8PuuU_sSUdIHIQkwVCYVVnfk68SsfCWTO-XsYRuLy6qxv9xZ8pZf6w_ofWXF4hHo4Qv8rEL3rGzHz20mk13oFGsSxq7pkh6hD5_N86wpj31JTcmseVyt01PieHHyMcmnkCTui0YWT2Qo40o-lm1YHRL2r-oqlcunRutQikTzry5H6JqgsJFNKv237MfcinuaHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=NqrW57DRa9rhj0t1SYdCcNiKiaxCa-0LDASVkHQqDRiltbaj477obGrgJbfJ4xpdAmILPfKI5OtrXKNP3I6mOABfo7lSiO1PQhEHimehDPKutPQZJIa-ht5P7RsotZYui47tdqq1KyGMiocvJBh8PuuU_sSUdIHIQkwVCYVVnfk68SsfCWTO-XsYRuLy6qxv9xZ8pZf6w_ofWXF4hHo4Qv8rEL3rGzHz20mk13oFGsSxq7pkh6hD5_N86wpj31JTcmseVyt01PieHHyMcmnkCTui0YWT2Qo40o-lm1YHRL2r-oqlcunRutQikTzry5H6JqgsJFNKv237MfcinuaHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالملکی، وزیر سابق کار:
دولت دروغ می‌گوید که پول ندارد و نتوانسته نفت بفروشد. در طول جنگ ۴۰روزه، فروش نفت ایران افزایش قابل‌توجهی داشت و درآمدهای نفتی کشور حدود سه برابر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70639" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=r9hD8uSO6liKPqlylKTDYXd7dHe9rA0S_sz4b4pY7ynKQB0_jHE46FkdCN3mgy2OWHtaw14sIgDdtcigal8i58tL532A3wuoA_aPFcf3owOuFVaNp9ME-5KDEuqdmsh0cILc3MpAfbDMXy-UYfCxjHlF7icz1Tyxmz-9Hb0NdkTAbc-PJREwHPIX7ZE09_du06e1a9QFhkB7wB94_M3zCXZXcV6wSUcpQKa5wwYz1UfSLintgwo3Uw5YOCg2U-FY32b2WsJCsMRH2a6WdfWh_BWUjjGFE9fYMsufjZioUgrrTSSv5kSXZnwis5JHKRB4hThBnP4sRyYqk8R5uUBiWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=r9hD8uSO6liKPqlylKTDYXd7dHe9rA0S_sz4b4pY7ynKQB0_jHE46FkdCN3mgy2OWHtaw14sIgDdtcigal8i58tL532A3wuoA_aPFcf3owOuFVaNp9ME-5KDEuqdmsh0cILc3MpAfbDMXy-UYfCxjHlF7icz1Tyxmz-9Hb0NdkTAbc-PJREwHPIX7ZE09_du06e1a9QFhkB7wB94_M3zCXZXcV6wSUcpQKa5wwYz1UfSLintgwo3Uw5YOCg2U-FY32b2WsJCsMRH2a6WdfWh_BWUjjGFE9fYMsufjZioUgrrTSSv5kSXZnwis5JHKRB4hThBnP4sRyYqk8R5uUBiWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دادگاه محاکمه اندروتیت اعلام کرد ماشین های بوگاتی و استون مارتین اندروتیت اجاره ای هستن(یعنی مال خودش نبودن)
اندروتیت یه مدت بخاطر ویدیوهای انگیزشی و سیگما طور که میداد بیرون؛ حسابی معروف شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70636" target="_blank">📅 22:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70635">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scOLlJf7qoXYns40GTQwx5qgm3PH6V1QGiZ2xhKQBYXS5ViGUvxijsk7a3Se8NUr85DOAy-eOOckIKNtx7prPf5I-TkT6GIBHvuUXr_Nt_vZNDqPzNA8vW_5KSP1N4n6F2lyxAWekMMTnH_ZwG0BE40O3_Ix-fyzPZmfBhurC-fSc2OBTIZ2PvS4hVVEFzHAzXFDg3mhJDZjNvnt8Q2jHZ_dRyDn5IS3ddcv3ZCL8_hqWnMrRTENt8729T0ApLZctmo9GT5EItnc9LLWYLsPWO6Fhamq_dpZ5kHKEKKVmQr1UfNVgsomx_mtJ6Kvx6oBH38KsMExSSzo7VtDedT7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
ما از بیانیه اولیه چین حمایت می‌کنیم که تحریم های غیرقانونی علیه ما رو رد کردن
مشارکت استراتژیک ایران و چین بر پایه احترامه و سازندگی و یک دیدگاه چند قطبی استوار وجود داره
این رابطه نیاز به تایید هیچکس نداره
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70635" target="_blank">📅 22:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66110614c2.mp4?token=vtU7sAutkFispL_5-pzd19ljIuCeH-VcIJc95AjNbs4qsoOOL1n0cyULa46pacJXltkTawlsCwJyQdb_clmoFkJoaC65dEBIyA_u-fhdDT9i4MA935Uj_QDU-hj3LapUdHFTS26fdsx4NCkQCGjwQJEKEsqYDhv1Y1BCVT-R3Z50Ys_hzHt88VcrEsHoqRDjRzuWqv6uV7lXm-b9FQ39Bd4PtiCwfHt-Q8r3OatTsuQePDTRrbs5SGasQTlOvXzHxAYTtsjoJr7k0Zh3YPstwcGfF0s21CMaH72w8C-R0BRlmaONRTElay3OMmIWTv35bB37_kNXY1ygxv8QhGAB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66110614c2.mp4?token=vtU7sAutkFispL_5-pzd19ljIuCeH-VcIJc95AjNbs4qsoOOL1n0cyULa46pacJXltkTawlsCwJyQdb_clmoFkJoaC65dEBIyA_u-fhdDT9i4MA935Uj_QDU-hj3LapUdHFTS26fdsx4NCkQCGjwQJEKEsqYDhv1Y1BCVT-R3Z50Ys_hzHt88VcrEsHoqRDjRzuWqv6uV7lXm-b9FQ39Bd4PtiCwfHt-Q8r3OatTsuQePDTRrbs5SGasQTlOvXzHxAYTtsjoJr7k0Zh3YPstwcGfF0s21CMaH72w8C-R0BRlmaONRTElay3OMmIWTv35bB37_kNXY1ygxv8QhGAB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو‌ ارومیه یه پسره واسه دوست دخترش یه لندکوروز سری 300 که قیمتش بیش از 70 میلیارد تومن هست رو خرید تا سوپرایزش کنه.
تازه، زیرش میدونین چی نوشت؟
ایشون نوشتن، تقدیم به زیباترین دختر ارومیه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70634" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbYr55ajzPzk1sjILUY2XA47TVusR43ajZ146aERrrGRxqrzE0-eEpb-FYrZ8J-HSb-7oHfL_uzylToaEdbNTQ9PE22a12gcwiCB0TAPz827caxQ0I-lIuQBQrHAfmb18P1ydjV2_EAPHoZxb-ZDHTHQFARRqlHOIt4iWXuWk8TveV9EgRTzb5EkqkQmCRkZ_Ue88AjYYZiD6RBkkG7sDx9JHW7TzhtVNWOE3tOpPj25t52ExVyZD23yIENExkAy-mwVJhbC9c7GAP6JgRqmpQBMfZf5my66AN3HPzk2-jsCxu7idxitXLbRNkW1HpYxnf9kqNEga-u8e0qZvUx3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فارس:ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70633" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0sWdoz0gZ-wSARPFACwaFgF4Q0DB2DZ3NZ4rEAiMbVLyhDVCZGnwaUj0zaCV1HiB0T85uRnY542UpQG9S8E6_WQllI0_AzpQ26m0XtSV-y4Vy7gJJzU88v1C05q5vAiv_xNO1U0wNBLOSnhb8kpAduAjApC6polRtnl5UjWWMfoplkMugkeNWq01tbNRvF4EJmygc5h6avxJ4UWNVm5Xrrn3pz661exowB49VCo9BmPf_bgpyBxcl10PxDbmGJeuwmzbg9Nc--X5jrfHuwFFKIFUk35SQE62wI7qQSg9CEgYFPBrU7H3x7EeQkVZeGh8R2vmMsR5bQrbKcKlQFUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70632" target="_blank">📅 20:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ℹ️
صحبتای امیرمحمدزند بازیگر صداوسیما:
حرفم با مسئولین اون وره چون این ور اگه حرف بزنیم احضار میکنن و تعهد میگیرن اخرشم‌ممنوع الکار میشی
قبلا حدقل زنگ میزدن میگفتن ممنوع الکار شدی ولی الان زنگ هم نمیزنن خودت باید بفهمی جلوی نون تورو گرفتن
ما ایرانیا با دلار ۲۰۰ تومنی و طلای بیست چند میلیونی و مرغ و گوشت و .... خیلی مردم شاکری بودیم
هرچقدر هم اقتصاد بد باشه گرونی باشه جنگ باشه میگن باز شکر کن سالمی حدقل
بعد که مریض میشی میری بیمارستان با هزینه هنگفت میگن شکر کن حداقل زنده ای
طرف میمیره بهش میگیم خدارو شکر بابا مرد و راحت شد
ما ملت ایران انقدر شاکریم خدایا یه امتیاز ویژه برامون قائل شو
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70631" target="_blank">📅 19:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
مهاجرانی سخنگوی دولت: در میدان ولی‌عصر یک خانمی به من گفت الهی بمیری!
رسایی سرباز نظام نیست؛ ظریف سرباز نظام است
رسایی منافع ملی کشور را نمی‌فهمد!
جریان پایداری خلاف منافع ملی حرکت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70630" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=Fr2PIcf5lk6NWLEW5LQddHTqpMqVBgPOTGPkYuXa9fv7PgTPPm0KulOSCReq2iUTE6JDoQrmRWz0i4wK1HQ8L_N87UVDH98A6P6Rw8ogjd61rKYj0t5NVLIgQVv50hGmm9M9MtYHTZesXFDecp6VaTnuzR962vrF01q7xhUBFmb2dJO5zq7EbBXdUzXNPiOG6yYkCH72zDPVT9hclBDBP9hUXGrYaoqZEhKBv8Zp0dAGovrcudss2Lv3YKDcdO972EK1wd8YYsjENn4-hadbwZbJNNLKm2OaHX7oCrNFEDK0ZNpGkejX3xRjRDscYi2GXQ5bW3Pgek3A2UM4RgLm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=Fr2PIcf5lk6NWLEW5LQddHTqpMqVBgPOTGPkYuXa9fv7PgTPPm0KulOSCReq2iUTE6JDoQrmRWz0i4wK1HQ8L_N87UVDH98A6P6Rw8ogjd61rKYj0t5NVLIgQVv50hGmm9M9MtYHTZesXFDecp6VaTnuzR962vrF01q7xhUBFmb2dJO5zq7EbBXdUzXNPiOG6yYkCH72zDPVT9hclBDBP9hUXGrYaoqZEhKBv8Zp0dAGovrcudss2Lv3YKDcdO972EK1wd8YYsjENn4-hadbwZbJNNLKm2OaHX7oCrNFEDK0ZNpGkejX3xRjRDscYi2GXQ5bW3Pgek3A2UM4RgLm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای این دختر در مورد اینکه تو این جامعه، سخت‌ترین کار پسر بودنه، به سرعت در حال وایرال شدنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70629" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70628" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOApkKkjxobcAlVkJeLYhYampsRFD7kwkrcAWTTUDro1u8O55M9wQxMWVlfAPoRK8wffwIO_NTcj8On1MHf3UA1enjkJBOHNyDNOIHJpyLzjyRu44ZVY-_oVSxfdvVpQ0e_Gbr5RY0rE79OE3w_AY1UIdE_9mqjc01xLUHaFLCzqsex9GgoVDxpMsfj64pUmtayCTUpNUNWQlQKe-58e0eK0o05A8ybMhBcWBg0-PWwE9eLUeJ6F6lTFjOkt-RzVsFHXnP3sXUoXLw8Bhx1U3AhnYu8EIRL16wL9usRQu2xtS9p2EdQZrbgnRNvJF4G80pmLj70FOvtgLnkoNNhmuH-h8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOApkKkjxobcAlVkJeLYhYampsRFD7kwkrcAWTTUDro1u8O55M9wQxMWVlfAPoRK8wffwIO_NTcj8On1MHf3UA1enjkJBOHNyDNOIHJpyLzjyRu44ZVY-_oVSxfdvVpQ0e_Gbr5RY0rE79OE3w_AY1UIdE_9mqjc01xLUHaFLCzqsex9GgoVDxpMsfj64pUmtayCTUpNUNWQlQKe-58e0eK0o05A8ybMhBcWBg0-PWwE9eLUeJ6F6lTFjOkt-RzVsFHXnP3sXUoXLw8Bhx1U3AhnYu8EIRL16wL9usRQu2xtS9p2EdQZrbgnRNvJF4G80pmLj70FOvtgLnkoNNhmuH-h8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70627" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=JcHvirtvScC-9QKfB4oBG-XWzg8QJBNeD1tci0R_BftMUt-K0z8zzpXWJEHGLmZGAsrOertP_XkQM17bUGawsnpMYJW3kYqrazzWkA3113exqmU1_vI8GSEAOmzCAT1hwaw4Z4a3VbZySf0abtmYEgGiPyWuB65VrQ-7rj8JLjNyrlLb7AhnqyJPP2HyehCOe85dptBYnQzVctQ1RBOSRaMhzNjMfxyGI_QQGeuJlm6J013_BDdoWykDbdX19jFAMPDj4DslqRnVkdgltNmOqxC959cQNC20FO7lGD9SyKRTepyiqwwoifwyJJyuvY8VQUebDYDJggWXqy7mvHjJoopEB7nLZVwf58oQYVSxMh1Q62pSfJMY_IXHOM_7FxSuL8lxihMxXF9pva7mJmIv8q_51cRyGrPELZXb8bo4GVdqWZpp2ZYL4Xo5PcSuBDGronwZjgQMJk9g0FpbqJ924mfOlAQQDYJAj3g2ZDV8IS7n1HnuOJMHX0-zDCwmJrargiLN_myXrjCm2FaVtcbpXbWEeD0pKz7uwEFRBSVErwaLdkaLYuzEp7ZLIHhw86Eo8dLsmZJHlnysh3KkwIkYVvCYagqb2CEOmR89PpiZ9ChpqSwf-_K6DKwRF9iGarOt5v768rOvmL8dum8X6gVtBH-gVVdHgUvLmeC7rjKFU8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=JcHvirtvScC-9QKfB4oBG-XWzg8QJBNeD1tci0R_BftMUt-K0z8zzpXWJEHGLmZGAsrOertP_XkQM17bUGawsnpMYJW3kYqrazzWkA3113exqmU1_vI8GSEAOmzCAT1hwaw4Z4a3VbZySf0abtmYEgGiPyWuB65VrQ-7rj8JLjNyrlLb7AhnqyJPP2HyehCOe85dptBYnQzVctQ1RBOSRaMhzNjMfxyGI_QQGeuJlm6J013_BDdoWykDbdX19jFAMPDj4DslqRnVkdgltNmOqxC959cQNC20FO7lGD9SyKRTepyiqwwoifwyJJyuvY8VQUebDYDJggWXqy7mvHjJoopEB7nLZVwf58oQYVSxMh1Q62pSfJMY_IXHOM_7FxSuL8lxihMxXF9pva7mJmIv8q_51cRyGrPELZXb8bo4GVdqWZpp2ZYL4Xo5PcSuBDGronwZjgQMJk9g0FpbqJ924mfOlAQQDYJAj3g2ZDV8IS7n1HnuOJMHX0-zDCwmJrargiLN_myXrjCm2FaVtcbpXbWEeD0pKz7uwEFRBSVErwaLdkaLYuzEp7ZLIHhw86Eo8dLsmZJHlnysh3KkwIkYVvCYagqb2CEOmR89PpiZ9ChpqSwf-_K6DKwRF9iGarOt5v768rOvmL8dum8X6gVtBH-gVVdHgUvLmeC7rjKFU8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
وقوع یک سیل ناگهانی و شدید در منطقه مرزی میان نپال و منطقه تبتِ چین، خسارات سنگینی به بار آورد.
گزارش‌ها حاکی از آن است که در پی این فاجعه، تاکنون صدها نفر از غیرنظامیان و نیروهای نظامی و پلیس مفقود شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70622" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
فکر می‌کنم ۳۰۰ [درصد] باشد. شنیده بودم ۹۰ درصد؛ اما به نظرم تورم ۳۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70621" target="_blank">📅 17:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70620">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=A9UIEJO4dRmeIk0fOVUZNcecOkm4gr3hrpptX_54iJWpOM9nTXfIftjxF_h0akGaWhLDocu3m0TqrsM3sIEcVMSVrNQEiG9OcfPoWyjV3QfztrhyFD_hFMV-6Bc-EBiFICR3SxBAYPvCMqH5C2xvJ4WvHPP9sUwBuUQre0dvv1ltgfbEkq-WN7YRCEbX0RLVoFr1A4qogD9RJ-4Wowz0FHE9Zrml0oSll9cAeIeOgI3AwQ-4N2A0j2RmF80jD7FP6BUWPFmVluFoVBWTftXg1zIqUeAzb7SzQ0uJshS-RPDDG7QKu6PYtu7Ee9uTxFxYAu3Txy9eJj3LfpJMBkRynQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=A9UIEJO4dRmeIk0fOVUZNcecOkm4gr3hrpptX_54iJWpOM9nTXfIftjxF_h0akGaWhLDocu3m0TqrsM3sIEcVMSVrNQEiG9OcfPoWyjV3QfztrhyFD_hFMV-6Bc-EBiFICR3SxBAYPvCMqH5C2xvJ4WvHPP9sUwBuUQre0dvv1ltgfbEkq-WN7YRCEbX0RLVoFr1A4qogD9RJ-4Wowz0FHE9Zrml0oSll9cAeIeOgI3AwQ-4N2A0j2RmF80jD7FP6BUWPFmVluFoVBWTftXg1zIqUeAzb7SzQ0uJshS-RPDDG7QKu6PYtu7Ee9uTxFxYAu3Txy9eJj3LfpJMBkRynQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
وقتی کسانی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است؛ به همین دلیل است که آن‌ها اعتراض نمی‌کنند.
و البته احتمالی هم وجود دارد، چرا که آن‌ها بسیار تضعیف شده‌اند... به بسیاری از سربازانشان حقوق پرداخت نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70620" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=YOwmUy-eElJ-zCWz-HyWTDPLZ9kqli52gXsuHtnIeiD-H2xTOXgcwBzjP0jh1S0oToeKmE7Y-Mln6QPNJ8yFT8qiZw1bHO8S5p8BgDraTFtzOnJ0gCmRftHRZBCqJmblqn6xtHCmFMbHQZ3XpbzOHQnYnoIW8C8GkRWfxlOdJ9lGFjeP24W7vnwk6Yv1UnMWLYR8NMAaJn7zvUuZvaZCTVKogXP_Qj3JuFusVwz65K31IQgYEJq1zFryXL6opjaSh8Ua0ND7ch2ZVoB2dDnDICf9uB-OrgadR0jtCHydzJ7IgETu3uj7uBeYYc1JONvH55MljEQyOb2ZaXsebEA-xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=YOwmUy-eElJ-zCWz-HyWTDPLZ9kqli52gXsuHtnIeiD-H2xTOXgcwBzjP0jh1S0oToeKmE7Y-Mln6QPNJ8yFT8qiZw1bHO8S5p8BgDraTFtzOnJ0gCmRftHRZBCqJmblqn6xtHCmFMbHQZ3XpbzOHQnYnoIW8C8GkRWfxlOdJ9lGFjeP24W7vnwk6Yv1UnMWLYR8NMAaJn7zvUuZvaZCTVKogXP_Qj3JuFusVwz65K31IQgYEJq1zFryXL6opjaSh8Ua0ND7ch2ZVoB2dDnDICf9uB-OrgadR0jtCHydzJ7IgETu3uj7uBeYYc1JONvH55MljEQyOb2ZaXsebEA-xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما از شر مین‌ها خلاص شدیم. اما تنگه هرمز... تنگه فعال است؛ یک تنگه فعال.
بله، هر از گاهی پهپاد یا راکتی یا چیزی شلیک می‌شود، اما این تنگه کاملاً فعال است.
مقدار زیادی نفت از آنجا جریان دارد.
دیروز ۱۰ میلیون بشکه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70619" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=M-nHSmgS2cHM3rwdr2iAD2B0CrrRq4DozjrCYHqSt6O-LtFo5Ljax__79mK_oAvRU4KackLP_lVKtN_XFe7alLCwM7hSEd0BBsSyQ9C4LDsNGL-32vi59pLsu1ztKX3b1Zj7T0ikbDlJ_8vsieIL_tmXzx-RzjUjxBTGdgdjW8dBRCFKPX0DB6n4JXxLs8HthpvF6H8eQ5OLukHEc0Cot_Vhq8DGjc0Jr5umom99228pPjulVNvsjzdlFMmz3elQkggX7vmt0Tprvlo1l_8e8DSfx3D1mhvxyDGwM5DErk7zvdLuEBmR9qIxVw1yW4krQzqU8Cm8BeOuLiMBwlBseg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=M-nHSmgS2cHM3rwdr2iAD2B0CrrRq4DozjrCYHqSt6O-LtFo5Ljax__79mK_oAvRU4KackLP_lVKtN_XFe7alLCwM7hSEd0BBsSyQ9C4LDsNGL-32vi59pLsu1ztKX3b1Zj7T0ikbDlJ_8vsieIL_tmXzx-RzjUjxBTGdgdjW8dBRCFKPX0DB6n4JXxLs8HthpvF6H8eQ5OLukHEc0Cot_Vhq8DGjc0Jr5umom99228pPjulVNvsjzdlFMmz3elQkggX7vmt0Tprvlo1l_8e8DSfx3D1mhvxyDGwM5DErk7zvdLuEBmR9qIxVw1yW4krQzqU8Cm8BeOuLiMBwlBseg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«باید بگویم که آن‌ها اصلاً گروه شرافتمندی نیستند. و می‌دانید، ما کاملاً قاطع عمل می‌کنیم؛
دیشب ۲۲ فروند از قایق‌هایشان را نابود کردیم.
آن‌ها سعی دارند محاصره را بشکنند و وارد شوند.
نیروی دریایی و ارتش ما عملکردی فوق‌العاده داشته‌اند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70618" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=nwL85kDSbquEmHUeeASeAzhPVxCozuCBbT5PiIGNbPLqtbeLltr2ywd-OL6nzndXO1v0tkQyPkLoan5MkPTJtEb3JHTinDW7s8DatlIXYoVX9kjbtfoBTPkhgHPvMU62O7l_LK6dq97pL8WAoW22kZuQJ3oLII2U8l5ge_1M1IBRmQZcK3vtt1bi6KPphNxYefhn7zg_Eqa3zNu0AbSxJRoP58KfyR4UzkLhMBts6461e8T_a-4hHx94MWWuZ4LLU8AzQD0F0RMuyj8QdGeiKEypxDNN9NNGrrprB6pM7usnzr_oeF3qG60GTS4eTPC1GObUhZ37MWVcsxrYq0nbzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=nwL85kDSbquEmHUeeASeAzhPVxCozuCBbT5PiIGNbPLqtbeLltr2ywd-OL6nzndXO1v0tkQyPkLoan5MkPTJtEb3JHTinDW7s8DatlIXYoVX9kjbtfoBTPkhgHPvMU62O7l_LK6dq97pL8WAoW22kZuQJ3oLII2U8l5ge_1M1IBRmQZcK3vtt1bi6KPphNxYefhn7zg_Eqa3zNu0AbSxJRoP58KfyR4UzkLhMBts6461e8T_a-4hHx94MWWuZ4LLU8AzQD0F0RMuyj8QdGeiKEypxDNN9NNGrrprB6pM7usnzr_oeF3qG60GTS4eTPC1GObUhZ37MWVcsxrYq0nbzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره مجتبی خامنه‌ای:
فکر نمی‌کنم مجتبی خامنه‌ای مرده باشد.
او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دست و پایش، و تمام آن ناحیه آسیب جدی دیده بود.
اما گمان نمی‌کنم که مرده باشد.
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70617" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70616">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=b4lE9JM_7RVlYIRTc3CsdMz5Y89Ic0WIBmWqtCd9RVb3A714VRr77P5aH-sFiL5Ck5ZzcNyYbNRD_n3hQJn7-ssrDNEsTFJ316uWvSNw3Udzcpma7oKrbBz6n1Elqhew_wWM5MZBYMfYufslebqawFn-y_efaece0O-kzxed55eCc9fv4qY48is0vveh5eMhZed_9oFnKrN626e3Kc6aJklXCCGUeele1jrSjtgML31EpxcnHd5JOa5HHQRP3TWPhsPaAERR38uktBeA9gL3ialex0O208m-PpRIvUK2TAjqhBcBE0zL8KCi7aNDibqQPfHft-4yg_LR2gnfLQxWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=b4lE9JM_7RVlYIRTc3CsdMz5Y89Ic0WIBmWqtCd9RVb3A714VRr77P5aH-sFiL5Ck5ZzcNyYbNRD_n3hQJn7-ssrDNEsTFJ316uWvSNw3Udzcpma7oKrbBz6n1Elqhew_wWM5MZBYMfYufslebqawFn-y_efaece0O-kzxed55eCc9fv4qY48is0vveh5eMhZed_9oFnKrN626e3Kc6aJklXCCGUeele1jrSjtgML31EpxcnHd5JOa5HHQRP3TWPhsPaAERR38uktBeA9gL3ialex0O208m-PpRIvUK2TAjqhBcBE0zL8KCi7aNDibqQPfHft-4yg_LR2gnfLQxWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز 4 شهریور ماه، زادروز شاهِ شاهان؛ کوروش بزرگه
.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70616" target="_blank">📅 16:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b4425472.mp4?token=NZGqH2lAoYjiKaVNfRhzYkJ0cltdgvbyRpBSNQ1P96rGCzylyrjfCn6AiFIDcKco67sYpGDAGL2fFAt_iRm8Vt6a6SqogPakkchlN0GiN4WJZUQoi-d_4kk_4NzRJYnL88EATBEoyJbGAVDZew5npOb778g-zLxsHe-Znb_IaXQnuXgL8uDKe9uOgUquL6ObiPw6a5g50FghiyNmbsABhmSWyUtMXBw74sqf9qFScFLW4UW4YpekZsF3_x1mwDSGICPB34f01Z2z-FjAumkkrcGPCYJl0mz0Vk0R_SV8j-v2oV-JyYXoa46rstDIJwoAc-1QkVDGs5np4QrtKDTsuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b4425472.mp4?token=NZGqH2lAoYjiKaVNfRhzYkJ0cltdgvbyRpBSNQ1P96rGCzylyrjfCn6AiFIDcKco67sYpGDAGL2fFAt_iRm8Vt6a6SqogPakkchlN0GiN4WJZUQoi-d_4kk_4NzRJYnL88EATBEoyJbGAVDZew5npOb778g-zLxsHe-Znb_IaXQnuXgL8uDKe9uOgUquL6ObiPw6a5g50FghiyNmbsABhmSWyUtMXBw74sqf9qFScFLW4UW4YpekZsF3_x1mwDSGICPB34f01Z2z-FjAumkkrcGPCYJl0mz0Vk0R_SV8j-v2oV-JyYXoa46rstDIJwoAc-1QkVDGs5np4QrtKDTsuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کوهنوردای ایرانی موقع صعود تو کوه های آرارات، آیفون17 این دختر آرژانتینی رو پیدا کردن و بهش تحویل دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70615" target="_blank">📅 16:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=U8wrNfDUqJ6fXKjv1Mk0Z3pAhzTJE-S-nzhwo_akCWXf5QwjwieAJrObl-3xh8UW0BLCJCkDH4t5jufflcobAYF9RRQ2gY9O1pKnCIZ2Xb-Y9vevkTJgOlQ1V3uygPQ51uSJG_7ldXz9GuXKVo4Bzg5vJynegi2gamSlkxHGnD86ezTqxYBz9LHpUqUaSrOQudriX9vRl6dGzbGSohk2XF7Y3qrLt22gdIcXoimgA1GsHxORohv38xYr1oFQPy_mYIJ3thgt1bJL6fBcgzcT3Z9CRIodJgGo0z56iEmDXoozjIpTNCjSY1gLNubCfYe8jhJVmaMT8711Z0SRByEsRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=U8wrNfDUqJ6fXKjv1Mk0Z3pAhzTJE-S-nzhwo_akCWXf5QwjwieAJrObl-3xh8UW0BLCJCkDH4t5jufflcobAYF9RRQ2gY9O1pKnCIZ2Xb-Y9vevkTJgOlQ1V3uygPQ51uSJG_7ldXz9GuXKVo4Bzg5vJynegi2gamSlkxHGnD86ezTqxYBz9LHpUqUaSrOQudriX9vRl6dGzbGSohk2XF7Y3qrLt22gdIcXoimgA1GsHxORohv38xYr1oFQPy_mYIJ3thgt1bJL6fBcgzcT3Z9CRIodJgGo0z56iEmDXoozjIpTNCjSY1gLNubCfYe8jhJVmaMT8711Z0SRByEsRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی وایرال شده از نوجوونِ 18 ساله‌ای که با موتور کار می‌کنه:
من روزانه 8 الی 10 ساعت کار میکنم!
امروز یکی ازم پرسید چِتی میزنی یا نعشه بازی؟ گفتم هیچکدوم.
با خودم گفتم من باشگاه‌ام رو میرم، خرجی خونه رو کمک میکنم، اهل دود و دَم و دختربازی هم نيستم.
به خودم اومدم دیدم از خیلی از هم‌سن‌هام جلوترم واقعا
تویی که از این روتین خوشت میاد و سالم زندگی میکنی، به خودت افتخار کن، چون مثل تو خیلی کم شده..
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70614" target="_blank">📅 16:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=VGMLUco-g2ci_qFK3R_Df2GXfe1oer-q6cM9abJu4cq2aZXfwCa-S7PI8fLsnqtzI664ekFof_874_pDvhL9CQyg2-NoXergM_DGpffS9phcb4QzWjRkvnblWx4rv_9XJI9BuSr6c5MKAyXlNdDakdEsAOu6tKMVomegXu39xv8BIP9kZtD-P2IluzW7cXYXkqJWX0BHqyKiGYIFxAl0taBpqcAaj81ggF5t1C-XijAh1MQ8cLxxuGzQZKubV4QOW-eEnP3h81V4tFRFUX4-tY4ebW37jVXC0GtEVP7C-QVwK1AF56BZQXKue8M-8FIDJJ2g4aw6aiv76kjc6NDs3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=VGMLUco-g2ci_qFK3R_Df2GXfe1oer-q6cM9abJu4cq2aZXfwCa-S7PI8fLsnqtzI664ekFof_874_pDvhL9CQyg2-NoXergM_DGpffS9phcb4QzWjRkvnblWx4rv_9XJI9BuSr6c5MKAyXlNdDakdEsAOu6tKMVomegXu39xv8BIP9kZtD-P2IluzW7cXYXkqJWX0BHqyKiGYIFxAl0taBpqcAaj81ggF5t1C-XijAh1MQ8cLxxuGzQZKubV4QOW-eEnP3h81V4tFRFUX4-tY4ebW37jVXC0GtEVP7C-QVwK1AF56BZQXKue8M-8FIDJJ2g4aw6aiv76kjc6NDs3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ هر ثانیه بیشتر سورپرایزت میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70613" target="_blank">📅 15:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=vOM0oVMXpGWepV1fb1ctNR2-Q9SGrzZnv7wN8T6SNmjok8iN33QSftgUMdkzg8eH_Pejzxm8mjnKp7GUyQt5LmZQBlvEd4KespkQA44cVv_rNlbDidPx1JVeAtyproX7YSgrP2CQZy6IsCD7qz-R2JJCDszRNWNJs1B2uBuXY6Mt_1l0qCUcROJC4tL_r2gee3BV_xJj_kCXsaDc7Qe1cpPf7fTdRjMLmHXLmQiO1PBDa_QZuoHVYRM__zBGRKU5nK42sL776ir74fVWTcYpE-FFPEQawsdn-oCNr6HpE6ut7z8zLmvlw6kTfgIUIJCcgoMTRIBEaERN0fz5GinnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=vOM0oVMXpGWepV1fb1ctNR2-Q9SGrzZnv7wN8T6SNmjok8iN33QSftgUMdkzg8eH_Pejzxm8mjnKp7GUyQt5LmZQBlvEd4KespkQA44cVv_rNlbDidPx1JVeAtyproX7YSgrP2CQZy6IsCD7qz-R2JJCDszRNWNJs1B2uBuXY6Mt_1l0qCUcROJC4tL_r2gee3BV_xJj_kCXsaDc7Qe1cpPf7fTdRjMLmHXLmQiO1PBDa_QZuoHVYRM__zBGRKU5nK42sL776ir74fVWTcYpE-FFPEQawsdn-oCNr6HpE6ut7z8zLmvlw6kTfgIUIJCcgoMTRIBEaERN0fz5GinnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
لحظه شلیک RPG توسط سرباز روسی که جلوی پاش میزنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70612" target="_blank">📅 15:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70610">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=eCCvdu7jyfKz3Bb9WxqQ8YwbLBmcrBIT4_6QDZzt4r62YWz7Gt5KwDZRY7KiXb8KBnz2j4TSghI6asbzrk_-6It9K7mMjDmN6yYiR2S__aVVWjIytr6VXpEV-m34QnQYLEmow7uwxsXzIwH8ZBTJurHkIBtMx0zvw0UKjSionsDF27cmSUe8vu3lo2fyj2PnsLNStXI3_RqnOQ3XDslrbrSzMs_MiW4Suva0OQQjJD2glBMA-gmwDTw9g9CmCwHSsfgXpD_9xJGNFsFjAVUuO4Y1uT5N03ultWHh_-jOpbmvRcFDgWjD8432bw_ss9UI3I7772GuPObfE5f1rhBnSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=eCCvdu7jyfKz3Bb9WxqQ8YwbLBmcrBIT4_6QDZzt4r62YWz7Gt5KwDZRY7KiXb8KBnz2j4TSghI6asbzrk_-6It9K7mMjDmN6yYiR2S__aVVWjIytr6VXpEV-m34QnQYLEmow7uwxsXzIwH8ZBTJurHkIBtMx0zvw0UKjSionsDF27cmSUe8vu3lo2fyj2PnsLNStXI3_RqnOQ3XDslrbrSzMs_MiW4Suva0OQQjJD2glBMA-gmwDTw9g9CmCwHSsfgXpD_9xJGNFsFjAVUuO4Y1uT5N03ultWHh_-jOpbmvRcFDgWjD8432bw_ss9UI3I7772GuPObfE5f1rhBnSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این زوج به اسم مینا و رضا بعد از پنجاه سال هنوزم عاشقانه همدیگرو دوست دارن و پنجاهمین سالگرد ازدواجشون رو به زیباترین شکل جشن گرفتن و رقصیدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70610" target="_blank">📅 14:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70609">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3yvzRC1y3vUaXCBWVDOvn2ZJO8NuTRlIjHRMD0pLeVJ1LOfxKr4i1h9ZxnWgyn7Rq4i3I19YEskekIiYgLWeAy9Hg6mzSjJQppYI9p92z3YGJq1REmFGKd2benZ1ODA9cDTGQsjjR6n6icWaGBbv6k0qxF4G-IAUBYwHB4sQhUR5_SWuVdb5oZlBOFkcz8F_J4nnbZLADhaLohthxEgj4ou1ggzmDfBZVchR7CrBswMQY8LRAXp0miqBd2nVNcgpHjGtlpch_10NwiqNLm24JfAMvH0RhFBUnUPNYC2jY46N3UIwu5WjzpSUZpkhJUhbxeH3HnV0-lVaX8X-tDXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زمان شاه هر اسکناس هزار تومنی، معادل ۱۴۲ دلار بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70609" target="_blank">📅 13:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70608">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=EY5NYEBgaYshSf0nC8bRpmE1uDXUYUDhL4o6ecT5IAsKHa0khWOkJjgj4y45Rpj7VnjxXiVsEh4u-FvFxkDL1irHeGbOubmDNQA_A7vjngMu9h86puCLM6r9seDZB2xo1x-rx5EUnULVv8e0P257RxZX0m3upinw7dsAOa84AU5Zop0VjjFLizFbKWhDc-1tUziOaET2DJRzhx-Gs5pTfN8DPN6w-GGshekV2zrgs7eoJLjz0Y8k-0xpfVacH-vP7SVUsk0Eph94K6MBoxN_iu3ORigccrqD-GXuGH23AMQ0_tCPLkW1wtWpQUGaY-KvHLGxmZ7X73ZwNWrgbPZkjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=EY5NYEBgaYshSf0nC8bRpmE1uDXUYUDhL4o6ecT5IAsKHa0khWOkJjgj4y45Rpj7VnjxXiVsEh4u-FvFxkDL1irHeGbOubmDNQA_A7vjngMu9h86puCLM6r9seDZB2xo1x-rx5EUnULVv8e0P257RxZX0m3upinw7dsAOa84AU5Zop0VjjFLizFbKWhDc-1tUziOaET2DJRzhx-Gs5pTfN8DPN6w-GGshekV2zrgs7eoJLjz0Y8k-0xpfVacH-vP7SVUsk0Eph94K6MBoxN_iu3ORigccrqD-GXuGH23AMQ0_tCPLkW1wtWpQUGaY-KvHLGxmZ7X73ZwNWrgbPZkjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70608" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70607">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=B-k4x2QpAut1eh-BT3NSGn-W6nxDXwfDMHke17XokxlM1vlAMlFqy9GccKvrhIM9QpmTStzF8J7bxOyHZnoaEtY5nHyd_xwP31rP1F_X6pi4bh1Vqvs7hFRDQnlPhb2XfBHk89SU9G0ef5r6Wl8ZVz1DnZY_hFzOiSOjfJ7elJmXyApq6hti1nRsw1ItowG99z1_bvjyf4Nty3AJlMo2NmR1uvfkR33IJ6Nq6pNPCfda30AVdArGSGxozVaGBrJLnFoXVAvARTJOTf_aLNJzWxjD-tDzAzvhHtXXO-Rr0BJ3-4H5kArkQs0uglvMl_wv8dYC3BptyzJJdpDPErAxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=B-k4x2QpAut1eh-BT3NSGn-W6nxDXwfDMHke17XokxlM1vlAMlFqy9GccKvrhIM9QpmTStzF8J7bxOyHZnoaEtY5nHyd_xwP31rP1F_X6pi4bh1Vqvs7hFRDQnlPhb2XfBHk89SU9G0ef5r6Wl8ZVz1DnZY_hFzOiSOjfJ7elJmXyApq6hti1nRsw1ItowG99z1_bvjyf4Nty3AJlMo2NmR1uvfkR33IJ6Nq6pNPCfda30AVdArGSGxozVaGBrJLnFoXVAvARTJOTf_aLNJzWxjD-tDzAzvhHtXXO-Rr0BJ3-4H5kArkQs0uglvMl_wv8dYC3BptyzJJdpDPErAxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما همچنان با چالش‌هایی روبرو هستیم.
چالش ایران پایان نیافته است.
ما همچنین باید کار را در غزه، لبنان و سایر عرصه‌ها به سرانجام برسانیم و برای انجام آن مصمم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70607" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70606">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=tmDUWH0uLhIW_Lc7FCPvQA09UekdyC28ZlIUxwcXw0BP008cCa_VxJjsK8AdsQ825WTOAlkxUpKllCFansFQn4TDO7RgXRqXqj3Afrwrw-pyAP4v9hfoP30FEKGlrVf40TATDa8Px006lZ5ZSjMCqkZnV-1X_vdWFf5IZ3fpTtaNyCXH-m0l-6zzvx6u2ukSfcON2xMKO3tzgfrGfapoiwpodhrjHvKhcMPqJE7w2Odkk9pYx-fLasD4Z2n7VdQD_Xw74gioQfviJN4uVyhUzvr2bpzMufrKugYEkuKFxC-rXnUWgS5wMBAmdA21xKz83xfe4bQUSrlTQXkagat2bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=tmDUWH0uLhIW_Lc7FCPvQA09UekdyC28ZlIUxwcXw0BP008cCa_VxJjsK8AdsQ825WTOAlkxUpKllCFansFQn4TDO7RgXRqXqj3Afrwrw-pyAP4v9hfoP30FEKGlrVf40TATDa8Px006lZ5ZSjMCqkZnV-1X_vdWFf5IZ3fpTtaNyCXH-m0l-6zzvx6u2ukSfcON2xMKO3tzgfrGfapoiwpodhrjHvKhcMPqJE7w2Odkk9pYx-fLasD4Z2n7VdQD_Xw74gioQfviJN4uVyhUzvr2bpzMufrKugYEkuKFxC-rXnUWgS5wMBAmdA21xKz83xfe4bQUSrlTQXkagat2bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
⏺
و من به ترامپ گفتم که احتمال سومی هم وجود دارد: تشدید محاصره.
او دیروز آن تصمیم را به شیوه‌ای بسیار بسیار قاطع تأیید کرد.
اقدام دیروز رئیس‌جمهور ترامپ، تشدید محاصره ایران بود؛ نه از طریق تنگ‌تر کردن حلقه محاصره خودِ ایران، بلکه با تشدید فشار و محاصره بر کسانی که به این رژیم — این دیکتاتوری هولناک — کمک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70606" target="_blank">📅 12:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c258982c.mp4?token=XCjl2cpTrzvQRKV4xz23UqYdd-fpTdP4DNz9pQn0lfn9_SnNWkCnudWFHdfKm85IvMKKILEr8gXBnk6dKV8bvCSZIBODbXs8JU58SgZitCKaPNEK1Z2vhiJZkcsd8x0P08VGk2cqsMwfUhyxN6ihy_bdYd8Q3jfNuZVEgVzOnSXoyT6dfbURTgzu9Tes4oyQHcfL2gPnXrCxnYHjtKfXrqfkVo28sAi6gNhIaaq60IxJ0gY2_hCt5LIzio03lv9DiS-dPx9JyRRPVzJj2tH3YF3H_oxreAGiImtqeQhOFmmSgfNqDlzjv3qCZEk_knOJP4cg6wMZCHWUMqpn1VIe5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c258982c.mp4?token=XCjl2cpTrzvQRKV4xz23UqYdd-fpTdP4DNz9pQn0lfn9_SnNWkCnudWFHdfKm85IvMKKILEr8gXBnk6dKV8bvCSZIBODbXs8JU58SgZitCKaPNEK1Z2vhiJZkcsd8x0P08VGk2cqsMwfUhyxN6ihy_bdYd8Q3jfNuZVEgVzOnSXoyT6dfbURTgzu9Tes4oyQHcfL2gPnXrCxnYHjtKfXrqfkVo28sAi6gNhIaaq60IxJ0gY2_hCt5LIzio03lv9DiS-dPx9JyRRPVzJj2tH3YF3H_oxreAGiImtqeQhOFmmSgfNqDlzjv3qCZEk_knOJP4cg6wMZCHWUMqpn1VIe5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
⏺
به ترامپ گفتم:
البته یک احتمال این است که شما با ایران به توافق برسید؛ یک توافق خوب. ما هیچ مخالفتی با آن نداریم.
اما تردید دارم که بتوانید با آن گروهی که آنجا هستند — با آن وحشی‌ها — به توافق برسید.
🔴
به شما می‌گویم: نمی‌توانید با آن‌ها توافق کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70605" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=bXfARcCVKlvtr7QwoABUmbC98lC_5sZRcD7b_ezCXPK26JSmXnlhwg2Zf0Hq0D8xdabqwO7e7fcvhIkNHD53m_-Tay4Whom8KQr_4dWJx4SaecRqThCO3HIgK8XriPfcTiQsMwq3FjybXjgNl1ZwqclGOjvJkNJtauGn6IyKeE5I2nDBY_CY-_rvtobp7T89cM9BcD2OzeApfnEQ-iIiYvETOc8kGbnYoFzfyfo0jubv6Z5bnyX27fKQrsxC8uJVmxukVBAJejLutj4-7qcaqK7oUuD-3iaGy3R9rWwKLgTffWTSfbIjjos8ZPWjfEfM7blE4oGpCPyvUcAzg2s_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=bXfARcCVKlvtr7QwoABUmbC98lC_5sZRcD7b_ezCXPK26JSmXnlhwg2Zf0Hq0D8xdabqwO7e7fcvhIkNHD53m_-Tay4Whom8KQr_4dWJx4SaecRqThCO3HIgK8XriPfcTiQsMwq3FjybXjgNl1ZwqclGOjvJkNJtauGn6IyKeE5I2nDBY_CY-_rvtobp7T89cM9BcD2OzeApfnEQ-iIiYvETOc8kGbnYoFzfyfo0jubv6Z5bnyX27fKQrsxC8uJVmxukVBAJejLutj4-7qcaqK7oUuD-3iaGy3R9rWwKLgTffWTSfbIjjos8ZPWjfEfM7blE4oGpCPyvUcAzg2s_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفسنجانی سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست .
الان دیگه مردم دنبال معنویاتن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70604" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70602">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=ZRSmOgyIXs0YRHJiieOF407iA7IC52VUoewCFXOSNKYSF1kDF4Wci1G_t8vxPKLJeC-IxBPeA-pu3O0edknCvefwrzELaAuQvCA16dc2pNHADugvPy-YrIJW745o4Y3VcYEQS3CVNKd3cEnDaIrvFT-CfL1nyC6Gz7G_BewdgK3UNjvcA_Gani9ct_YuDIpISNUgh76BXTA-1aial--WmMI_rp48gi87iOQ25uYG4cwDvb3e_csdM0MlvRVwzCKLDyMXOEukX7trTbHpfIoQB0BvHJGRtO2NUgLWpB9_FkIMtDgbKPxj9Oy6K2LPMMZJv7rSBY0_GgSfslhCtQ4b0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=ZRSmOgyIXs0YRHJiieOF407iA7IC52VUoewCFXOSNKYSF1kDF4Wci1G_t8vxPKLJeC-IxBPeA-pu3O0edknCvefwrzELaAuQvCA16dc2pNHADugvPy-YrIJW745o4Y3VcYEQS3CVNKd3cEnDaIrvFT-CfL1nyC6Gz7G_BewdgK3UNjvcA_Gani9ct_YuDIpISNUgh76BXTA-1aial--WmMI_rp48gi87iOQ25uYG4cwDvb3e_csdM0MlvRVwzCKLDyMXOEukX7trTbHpfIoQB0BvHJGRtO2NUgLWpB9_FkIMtDgbKPxj9Oy6K2LPMMZJv7rSBY0_GgSfslhCtQ4b0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مدیر شرکت «فردا موتور» داشت واسه ثبت نام کنندگان خودرو توضیح میداد که ماشین نداریم. دو سال و نیم صبر کردید؛ باید چند ماه دیگه‌ هم صبر کنید که مردم گفتن «سیشتیر بابا همتون همینو میگید» و ریختن سرش.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70602" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70601">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70601" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70601" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70600">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN-TEGX6WWfieUqLJ_U2jakAcOdTYX8JnV9BIL5ewY2OT5KCv8WO2eg2NOLa4ddSfL9zbquwbRsEZVmAFbEKuLxU9_eKuhkPaClftIyYgckhEZcalVAKGmDcIYsQFU5CSqLwWrCReCfyDPSNdwT7kxZQM9hQjHOHN9kwu3GM8jRsZm-fL8SkFpSSBUGJsgpOKMJqRbZb8khsH2fOiklWvz19QopPMMOfdQC3Qle-xL3EKb0MQ9ar7rs9gdMaSPqh91GfNTkbBvvHXbBpr-fSXnkUoM83BaC1O46GQhaMJTzYl59zlPgw3dUJqG9DPOjmUnf6I_bKioAr5Y0tXvJbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70600" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=rI78F7cPuBy7hYrkY_1bJ40We9zjX2cDPaFw4FqJMIp8Lc60nKyPXgqcULDEytwBxB6I-rc6N1rm3p4IMXwCsqz4-vPW7Vu3litLAYTCIjOocOjCgBcNKCAksLKqCyVnS7GrmpRFyMjyMKPQBkWkm9aF_ZmkXKd5uOBZiUZ0ctZoI4y-LaDbaCxjCtAZPxowXuxABZtCbEmEzgemwnVDPgkJquGTRrXj5cXWCctxVrzGWz7RQasFH6zh8QFnglD33Vu5vHW2VbPReq6oPiD5eDRbVPjn4AIi138zFT7YwPBr2kPUHgUWj9K85oTxHAKDVsA0VOhc7apWJf6POWW4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=rI78F7cPuBy7hYrkY_1bJ40We9zjX2cDPaFw4FqJMIp8Lc60nKyPXgqcULDEytwBxB6I-rc6N1rm3p4IMXwCsqz4-vPW7Vu3litLAYTCIjOocOjCgBcNKCAksLKqCyVnS7GrmpRFyMjyMKPQBkWkm9aF_ZmkXKd5uOBZiUZ0ctZoI4y-LaDbaCxjCtAZPxowXuxABZtCbEmEzgemwnVDPgkJquGTRrXj5cXWCctxVrzGWz7RQasFH6zh8QFnglD33Vu5vHW2VbPReq6oPiD5eDRbVPjn4AIi138zFT7YwPBr2kPUHgUWj9K85oTxHAKDVsA0VOhc7apWJf6POWW4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای یه آخوند طرفدار حکومت راجب حجاب
:
اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
چرا اون کسی که میخواد به زن ها تجاوز کنه آزادی بهش نمیدید؟ آزادی باید بهش بدیم دیگه خودش انتخاب کرده که مزاحم همه بشه
اگه مردم آزاد باشن که هرجور دلشون خواست بیان بیرون پس باید متجاوز ها هم آزاد باشن
چطور میگی قانون باید جلوی متجاوز رو بگیره اما قانونی که باعث بشه لخت و پتی نیای بیرون نباید جلوتو بگیره؟
چطور تو آزاد باشی اون آزاد نباشه
هرکی لخت بیاد بیرون حقش اینه که سرش بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70599" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=Pj4_GZC2MiRPylm5kEJ3hib-5TJaJC4_HN-hWBY3dG2bNkNqIqQrk5WxRrv9URwXmunxKqvb3JWk6Cmn_tvr1GDXlxStYc9mnl6lELfrvhtadySY_WbkVjcwHb7IpDFuLbdwzz502s7hhgg98zKEyZc4S1WxbhNsAF7ukhb5JYpecGuWkuBzRTOVT4FYCXzta-L4VxIp0syXHO6LPq360uox1JGIqwrcMIf4EJm-vIXiMDe8eASRIP94txBEUssHOP_5Z-aUeI7MiEEs2ws9x5JS6WFnseWE5j8NOui4s3il2idB_ySmnxO2GbKYDOPf-tEMz9OPR_jC70PxIfOXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=Pj4_GZC2MiRPylm5kEJ3hib-5TJaJC4_HN-hWBY3dG2bNkNqIqQrk5WxRrv9URwXmunxKqvb3JWk6Cmn_tvr1GDXlxStYc9mnl6lELfrvhtadySY_WbkVjcwHb7IpDFuLbdwzz502s7hhgg98zKEyZc4S1WxbhNsAF7ukhb5JYpecGuWkuBzRTOVT4FYCXzta-L4VxIp0syXHO6LPq360uox1JGIqwrcMIf4EJm-vIXiMDe8eASRIP94txBEUssHOP_5Z-aUeI7MiEEs2ws9x5JS6WFnseWE5j8NOui4s3il2idB_ySmnxO2GbKYDOPf-tEMz9OPR_jC70PxIfOXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این خانمه داره مشاوره میده یک فرد چطوری با رابطه تریسام کنار بیاد
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70598" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=UxHGDo_qYSzo2_QnXzsjdrgwOKb432MDWO0tsKs-wO9f96N3l36dkNwvyoDLHgD-CcRDmR28knhYaGuD0IlSz6a4l5UqujIxYagHWRLvVdkQIyW-z8yDI_8CUmQ8watIEyJj2-ObOgWPUEmTH0tB447Z94yk1W0aiG7wfpnYSNLvPBH1EWXPtElsZaMA2YAk4LRiuK8hfi3JrS4zpFZD-YyDFwJJ0mOXCQV1VFx-X8_vYiz_6iZk6rmW_FQJaKSmGsFfFRiyd3IbS1dmaiiXeGXEdHUVYQRP8w7LJQvfzM8W5ndopknLc2GyjFjImSWdZ5jqzQShmit8rOW0hmj4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=UxHGDo_qYSzo2_QnXzsjdrgwOKb432MDWO0tsKs-wO9f96N3l36dkNwvyoDLHgD-CcRDmR28knhYaGuD0IlSz6a4l5UqujIxYagHWRLvVdkQIyW-z8yDI_8CUmQ8watIEyJj2-ObOgWPUEmTH0tB447Z94yk1W0aiG7wfpnYSNLvPBH1EWXPtElsZaMA2YAk4LRiuK8hfi3JrS4zpFZD-YyDFwJJ0mOXCQV1VFx-X8_vYiz_6iZk6rmW_FQJaKSmGsFfFRiyd3IbS1dmaiiXeGXEdHUVYQRP8w7LJQvfzM8W5ndopknLc2GyjFjImSWdZ5jqzQShmit8rOW0hmj4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
همتی رئیس بانک مرکزی :
علت بالا رفتن قیمت دلار طبیعیه و نوسان های خاص خودشه
ما نمیتونیم بخاطر یک نوسان بیایم مسیرمون عوض کنیم
مسیر ما درسته و خوب جلو میره
اگه این مسیر ما طوری باشه که میان مدت دیدیم درست نشد اصلاحش میکنیم
ولی من معتقدم که این شوک هایی که ایجاد شده جوسازی امریکا هست و شرایط مطمئنن درست میشه و رفع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70597" target="_blank">📅 10:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
ویدیو وایرال شده از یه جوون ایرانی خطاب به مسئولین جمهوری اسلامی
تراپی خالص :
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70596" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=dYupi9KvH8MhUpIdEu3w1spDKiO4EF7YJoyoo9ejMu22mKzECYKeeQ9k9DX3rEeDj2g6lHp4prFjFILHRfbstvcHtppdNQWtKZnkY3ZJgiu2Y9QDQoggwr1aYZfl9ITcTQAqNpfm3C96eJLdvcPFI3zRwHdMhy9rUDybVypLayHxDliuZNYnvKRKDHl3Zc6SHh5_CnylUFtBlzfieGE0_0bvjKutSjYtCV8AbfljT-Yg0aiWkUFDvX1SQDxjcYEswBq4I1bh1HR0yNT8YZhzrOR8bpBifkx0nbzxi4Q79GKj5CM2MZYpwZgZ9Rmg1XcAdeasj93iXF8sPT9uqOFs1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=dYupi9KvH8MhUpIdEu3w1spDKiO4EF7YJoyoo9ejMu22mKzECYKeeQ9k9DX3rEeDj2g6lHp4prFjFILHRfbstvcHtppdNQWtKZnkY3ZJgiu2Y9QDQoggwr1aYZfl9ITcTQAqNpfm3C96eJLdvcPFI3zRwHdMhy9rUDybVypLayHxDliuZNYnvKRKDHl3Zc6SHh5_CnylUFtBlzfieGE0_0bvjKutSjYtCV8AbfljT-Yg0aiWkUFDvX1SQDxjcYEswBq4I1bh1HR0yNT8YZhzrOR8bpBifkx0nbzxi4Q79GKj5CM2MZYpwZgZ9Rmg1XcAdeasj93iXF8sPT9uqOFs1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
غریب‌آبادی، معاون وزیر خارجه جمهوری اسلامی:
چرا باید همیشه منتظر حمله آمریکا باشیم؟ ما میتونیم پیش‌دستانه اقدام کنیم
بازگشایی تنگه هرمز فقط در صورتی انجام میشه که جنگ در همه جبهه‌ها تموم بشه، محاصره برداشته بشه و وضعیت یمن حل‌وفصل بشه
به فرمانده ارتش پاکستان گفتیم ما توافق رو نقض نکردیم
اگه آمریکا میخواد تنگه هرمز دوباره باز بشه، باید همه شرط‌هایی که ایران توی توافق گذاشته رو قبول و اجرا کنه
ما هنوز در وضعیت جنگی هستیم و تا وقتی این شرایط ادامه داشته باشه، تنگه هرمز هم بسته می‌مونه.
اگه آمریکا به اقداماتش ادامه بده، ممکنه قابلیت‌های نظامی جدیدمون رو هم رو کنیم.
تنگه هرمز تنها ابزاری نیست که ما در برابر آمریکا داریم. آمریکا نباید فکر کنه فقط خودش می‌تونه به اقتصاد طرف مقابل ضربه بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70595" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70594">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70594" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70593">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=o-8b_q25Cvy1Bp1pf31V3ZduUR8ubPrAzAS9hIBsGayfD3b5LSsMJ6-cswLsTGa6j9aUjdgmnD3NVIbJVTrO0Skhm3qNLcw8_NRnT9_Lbb5p4dgKReYk9VH3ogr8h7INInlrs3QDhj93UUNJJ807mB0PHSuH86uCHY8GnWNcSQHQBTJ3_YXNJ20xGkL8ylc1NHHpTb7NzqSCU64yEbYfs-sLh_QO14MWbqXixgjkL8H8bkNbrb-SY1gJnm5h6bZMVNLrKaE8OxSqaE7LqteHkDY7pHgMec-iO-lfvRmYtxrMyzjfQR2d5ytP864us93ryVDxvX1IgvJaxgl9MIhqpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=o-8b_q25Cvy1Bp1pf31V3ZduUR8ubPrAzAS9hIBsGayfD3b5LSsMJ6-cswLsTGa6j9aUjdgmnD3NVIbJVTrO0Skhm3qNLcw8_NRnT9_Lbb5p4dgKReYk9VH3ogr8h7INInlrs3QDhj93UUNJJ807mB0PHSuH86uCHY8GnWNcSQHQBTJ3_YXNJ20xGkL8ylc1NHHpTb7NzqSCU64yEbYfs-sLh_QO14MWbqXixgjkL8H8bkNbrb-SY1gJnm5h6bZMVNLrKaE8OxSqaE7LqteHkDY7pHgMec-iO-lfvRmYtxrMyzjfQR2d5ytP864us93ryVDxvX1IgvJaxgl9MIhqpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a3
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70593" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70592">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oehItBXRBpEOpQkQM1CXM-g8e1NedfmFKkUHZMYn6-UWWxVpZ1CiDWPuNpXNpmKml3ix834J21_5bwSxQt7pAoOF1kyQZQ8QYR8ypn5q15tnxEtdhK85lFB7gj9v33AyaebM1v8zHjp0QmotqkTix1u7a6-BYeAfWz0o8XbTrN1Finy4qUsPGT4HcOMKdhxuHZN5bxuwK0-axb2-zg8PeAShDphc9uy16t60SP_aNamya4MH_DR9nvGV7aewdc7T91v7N9YMsGkvoreLY8dcBMPCu_qBjOZ2ey5WFWD73hX-KcOqMcsnE4HrZX0XkDT6ZDqPwe-Xvp5MF55xvm2PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وام ازدواج برای یک زوج ۶۰۰میلیون
⏺
یخچال ساید ۵۰۰میلیون
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70592" target="_blank">📅 01:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70591">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDQ0zCBuFUm_YAbu2plkflJkDR1CoVXnmbNEgUY1yruP_KbuVZma3Z9IgpQ6xBEo1TrV1TL3ZnLvO3kWbMgxLpIjA0r0GQNys1vkfy-mMpv380DgWA1bG0GeUMtOlKndgpvX4AHsSkaDo1d9RFN71WoufousqRU4RWr2Y_BfCMN0rbz3LMdCKjaRCT_-1V1G-7RaX1U0uKreMaHxTFiYIWrtWOgkF7yqdtkdAndwN_Wc8XrqZCh34thT0zE-bPp_qZMwVXP6jiYr9-ED4rrT2uPn-HXl0DlZhms9PSehKUKzG1-OQhsyVEmmU5ZnWbim-D2XeKBI0r0HjsiZUs-nKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
اکسیوس:مارکو روبیو، وزیر امور خارجه، به چندین تن از همتایان خارجی خود گفته است که ایالات متحده «در حال حاضر» برنامه‌ای برای انجام حملات جدید علیه ایران ندارد.
در عوض، دولت ترامپ بر اشکال دیگر فشار، از جمله محاصره دریایی و کارزار تحریم‌های تازه اعلام‌شده، تمرکز کرده است.
روبیو اظهار داشت که اگرچه واشنگتن برای بازگشت به عملیات‌های رزمی گسترده آماده نمی‌شود، اما در صورت حمله نخستِ ایران، همچنان امکان انجام حملات متقابل وجود دارد.
انتظار می‌رود این سیاست دست‌کم تا پس از انتخابات میان‌دوره‌ای حفظ شود؛ زمانی که ممکن است انجام یک عملیات نظامی دیگر مورد بررسی قرار گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70591" target="_blank">📅 01:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70590">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV7VO1yFkRZBqMDa3vatzF5Lc-Uf5eWjxZdWZBZO7vbpj4_MOuPYzP7u1tDzBaDQVWFb6aKTtc1vJipyqa6n0S8ttuKkAKNfomz4EB7cVtfWJW_dqt3gu_zangJhU8mf1FQMZKLY2fWhs5bYr-Vf3d6aqRJy1pkyFygtaOxsdw8qhcuugxXW_JxjpfMBRLjmrymIUZArQt061rPj17LS6FMAOOGPlWXxQ0qr2Fw-9GH1QGN39fyJcVo9XMIH4xAbDws8vyT-I_RI6i9qVy-3jFatNsESF_eX_VauCeeh30WZDORFDTdgDOhQuH0g-zS3-BJ9vic8Ziyh3v0MQE2vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خروج یک هواپیما از باند فرودگاه مشهد
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70590" target="_blank">📅 00:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70589">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⏺
🎙
وزیر نیرو :
تا دو هفته دیگه شرایط آب هوایی به حالت عادی برمیگرده و خاموشی ها تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70589" target="_blank">📅 23:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70588">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7NnPUitdVlrvel0cgBJLf1_m1jXxovh8ci3J3vnXiwGpm7DD9WDSCRI15LluRqQDWyOTtvyBccuO7DkFkac65VtDhMbxIyqw64-Vgl9VZy5rJ4Vp8_xtYljG9hZB1on9kRgmrFDpANIf2OMlOQnusoHAmnuMSCjfADcPNO_SGeoIzRjEzYkKUin2YaGr4mqUEG2SNgNncS9n5EjmG_r2ZUg8z8_QlgmWsxk7nYJCttMzjiBKacqxsG3P6R1XbTrOmrbRL9KAbqJvzS2DOdNyz8OMs6vpfU_y3F0NNCXUe0k6YX4OVOAqSEhV37FOyHadzNmWNdov-yntOurjhlEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇴🇲
بیانیه مشترک ایران و عمان: دربارۀ چهارچوب ادارۀ تنگه هرمز گفت‌وگو کردیم
رایزنی وزرای امورخارجۀ ۲ کشور بر ازسرگیری دریانوردی ایمن در تنگۀ هرمز با حفظ حاکمیت خود متمرکز بود.
🗣️
چهارچوب پیشنهادی شامل این موارد بود:
ایجاد یک کریدور مشترک از طریق تنگۀ هرمز
اجرای پروژۀ مشترک برای مین‌زدایی از تنگه
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70588" target="_blank">📅 23:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=TTMRqxybcGMpx2lv7tE4PNclKtryRLRIN_Y5po9dl4ND15skgpVAYYI5CnTTfwJw0I8SBcwCGQ28Qyzu1Uutmoi161dgZ7TA-XeSBS6er6xBqsS13zcu2wtPSbTQAM5q4KMfVRZ3DY7biWGZ-Faaky3XvjGmumEa8Qmi6l7foJPVX611I2jX_Rs2Y9Z7LQMDmFs8QWSFBHjNHnxC5RPiX7fBe_nex5P6oYngXN1KL0JMYWqnmZakpILpqHfMWRxQbUitjeZ56BF-pWhRxGShsxG9ESfwr_I85-qlr-7whqdCJPWBB9bdRRumdIfAiaP0uYOgMBpXw-PWzR1VH51h8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=TTMRqxybcGMpx2lv7tE4PNclKtryRLRIN_Y5po9dl4ND15skgpVAYYI5CnTTfwJw0I8SBcwCGQ28Qyzu1Uutmoi161dgZ7TA-XeSBS6er6xBqsS13zcu2wtPSbTQAM5q4KMfVRZ3DY7biWGZ-Faaky3XvjGmumEa8Qmi6l7foJPVX611I2jX_Rs2Y9Z7LQMDmFs8QWSFBHjNHnxC5RPiX7fBe_nex5P6oYngXN1KL0JMYWqnmZakpILpqHfMWRxQbUitjeZ56BF-pWhRxGShsxG9ESfwr_I85-qlr-7whqdCJPWBB9bdRRumdIfAiaP0uYOgMBpXw-PWzR1VH51h8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به پالایشگاه نفت آفپسکی در منطقه کراسنودار روسیه حمله کردند.
در پی این حمله، آتش‌سوزی در پالایشگاه مشاهده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70585" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=ir0ZuCx-cy2QGha-S1-IIw_QCk0v3cTRRM6-9b-BCy-CnlFVV7D_txbMJqQ61Pj7VB_8bHrDn2llg-dUKlCVDc-UpnmiuTikEh0eERp4dGyim58WJjZDH24oFa1oGBPX5OFwAqHDkLFUuvi3-4I_NQCiLoqB6hWKOapr_tgDyedJ9g_qVvsJdnXURvWdfTmorhpMKetCr_EOCK1tG_iqLiqIcKkFuPvCVQ3ycN2p1UGgkVtwQIdXtCmMs8dR2a24Liy2S0REfYWCSVf9OmMlJ8Y1mCZqwEl7ae60Re_f5eeuDsxSji1VmmULSlpWyXUnAY3p8ITpbdcGswnU09ko0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=ir0ZuCx-cy2QGha-S1-IIw_QCk0v3cTRRM6-9b-BCy-CnlFVV7D_txbMJqQ61Pj7VB_8bHrDn2llg-dUKlCVDc-UpnmiuTikEh0eERp4dGyim58WJjZDH24oFa1oGBPX5OFwAqHDkLFUuvi3-4I_NQCiLoqB6hWKOapr_tgDyedJ9g_qVvsJdnXURvWdfTmorhpMKetCr_EOCK1tG_iqLiqIcKkFuPvCVQ3ycN2p1UGgkVtwQIdXtCmMs8dR2a24Liy2S0REfYWCSVf9OmMlJ8Y1mCZqwEl7ae60Re_f5eeuDsxSji1VmmULSlpWyXUnAY3p8ITpbdcGswnU09ko0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مستر‌بیست(یوتیوبر معروف) یه چالش خفن اجرا کرده که باید خودش و دوستاش از دست 100 تا نیروی پلیس به مدت 12 ساعت فرار میکردن؛
برای اجرای این چالش ماه‌ها زمان صرف آماده‌سازی تله‌ها، دوربینا و مسیرهای مخفی شد و حتی یک شهر رو به‌صورت کامل اجاره کردن.
خود جیمی (مستر بیست) و دوستاش به مدت چندماه تو یه شهرک نظامی، آموزش‌های نظامی و امدادی دیدن و جالبی این موضوع اینه که مستر بیست برای خودش 50 تا بدل درست کرده بود تا پلیس‌هارو کصخل کنه.
این ویدیو یکی از پرهزینه‌ترین و پرچالش‌ترین ویدئوهای یوتیوب مستر بیست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70584" target="_blank">📅 21:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70583">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=p3S6tbLvabmRGmb6hM_tqxCe7ZsilEfjwzj4Kr90uq1IC5Yz771h60LPw9oZ68LIYgdsRnZgq94j7bqaRu5NayltrUhwUaHz4jJnuhihE2D0Fph3WdczpCFUo3oosAfgSIQ1AreRy6aqE5HSD0Dz48biZzqGge89ZnVL9grgsSxDTtiWysALNKnSI01Z5vEoi5dm4JsMpZluY2vVE6whc1mAz7vpczBgFRJhzulfNu0DuDpiMva2CvnjJz7KJOiNCOoQXdZCq3Z9mQyLusDHuIFH0MJ2bEN3KreOzcNtlwDwaCwGsetlwdyM1pTdupJSkib4CBUGy85-ENNq31thlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=p3S6tbLvabmRGmb6hM_tqxCe7ZsilEfjwzj4Kr90uq1IC5Yz771h60LPw9oZ68LIYgdsRnZgq94j7bqaRu5NayltrUhwUaHz4jJnuhihE2D0Fph3WdczpCFUo3oosAfgSIQ1AreRy6aqE5HSD0Dz48biZzqGge89ZnVL9grgsSxDTtiWysALNKnSI01Z5vEoi5dm4JsMpZluY2vVE6whc1mAz7vpczBgFRJhzulfNu0DuDpiMva2CvnjJz7KJOiNCOoQXdZCq3Z9mQyLusDHuIFH0MJ2bEN3KreOzcNtlwDwaCwGsetlwdyM1pTdupJSkib4CBUGy85-ENNq31thlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سوال خبرنگار از شاهنشاه آریامهر:
فکر می‌کنید در کشور شما کدام‌یک تاثیر بیشتری روی زندگی مردم داره؟مذهب یا پادشاهی؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70583" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70580">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYgtapIw-rKaF4fVNGoTZivFh6rJ7JFqhIwGQEZMiXD7E9opVEjdTf6v9dr4o9BMsyb8sd8R-lZ9Q31OvyRqFsnG3WGGeW6WfktjbZep-2mkngb-KhA0GKqUr_ncG4aABGr99OOgdl49cApSMf1OKpqH91nvTUeBGFnltZuiT457KAa0OGvSolZTCt-3iBhMbqr3bB8YdFpfS92D3bVE3Bj-d5_MXxpX7pMiOyQahdaDIhlF-CWmBlxU87yDA9rrkoUEIJfiwgplOKeixfKp-wxrTJ9-KkG-UcJjDpoE8S_CtIwilMSNiketCr6iUQKEmhOfEP1bkvwzQtgA0dyEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfYFxFtOahQjhWrsUaZtgcrBn5R0R93SjGhLioWvcHfKKgLb593pgj66_Loqil0H5p0OD7RiqbDgLHsoNaMlFKxeNcrkacNqpXC3p_Xef6tclGjguwtUVso_gCNrDbfgzccOFfdyB9aQsy8mr8HJCWgLUT43DJ4W0FGTJSxrdMRSTqBindiqc3-eqDgE8kBLRskR71pMJQvdv8K2B4J6JneYNZIK7fMXQzRqa53708J6EOoQG8ZSWOWzFx6HfzsNlHxnlGbzcMI3rhhPjVPgPnIhPxuYENoHdEPyvKEE9U3ag8OisyxB5M-bJ_Jq2D_L8C8VuklOLnZcGD1AaMHiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pef8gl7gHZoge4zm4Lz0bFAU5V_qKz7SDc6JgCfR3OUWIqX4SLNC4IPRLswYUpBbePrjK0qMVaEolUGiAAQqLdMvgR0vooXV4re9DMibOdtzAyZRX7OoB0NH4zXMtKosOFL2RVxYnrdwh1qC--lY7MzDiXHIJzYaonJBCyg2wsfyh1x5aDVzTVvoj5rQzicC_jxdja4tqThyDC9SF4998hvIktuQbduBlg7GvNTnxb2ZgBHciziIB1HTPl2PpKd3aw4KmWGrdo7lCJXa_Dnf46q2t6xYB7Oq6HtsV7go7_mdVY0BN1iJq_beqLMb9hVIOwhv54NyL00CzzRx8qig-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
〰️
🇺🇸
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
🔴
رهبری ایران به واقعیتی اذعان می‌کند که اکنون برای جهانیان آشکار است:
فشارها کارساز واقع شده‌اند.
🇮🇷
مسعود پزشکیان، رئیس‌جمهور ایران، ضمن اذعان به کمبودهای اقتصادی کشور، اظهار داشت: «جنگ باید بالاخره روزی به پایان برسد.»
🇮🇷
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر سخن گفت: «هر چقدر هم که قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و خبری از گردش مالی، رشد اقتصادی و تولید داخلی نباشد، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری همچنان به قطع تمامی شریان‌های حیاتی اقتصادی که این رژیم را سرپا نگه داشته‌اند، ادامه خواهد داد تا زمانی که تهران کاملاً منزوی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70580" target="_blank">📅 20:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70579">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YsyvOPCS5LP2PSZ-IIL2u38rvWRHcq50Ts7LhdyQL7CXab277W8UVDBhnyf76qW_Eg-FrseHEWAehhL22U_SKQGh8CkFKR4xmDXMjcOrvQTp2iZ7gjW7Jbc00WHRJOn_GaZm4Pu8R90bQ5zna2GJq_TNkj9VviCz3RDItNe2b48vznXP8gBW4_crsPvtsI86XdVwjfMZybJHIVfhL43geeNTCSONts05bQEGE_pu15piX41x9lBxDuuCNlVfoTRsGJd757WqImD75LymUvyzNZadiX-CkfwBzRXGanuQ8CivEcyXHPRNGiGsD9Tcii6I10wEEGQ2n3tjtphH0Kt_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
اکانت رسمی تلگرام در پلتفرم ایکس :
امروز به کراشت پیام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70579" target="_blank">📅 20:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=fubmqoLDrRRkY8dL-YzwhKqwL7PmrHsO9OoD-Nat8r7GP6trBUKGOr6i82jH_f95lROcO4C8cb3sUZ4ER0ui1b6SHt30Ot7PzOU7Kks0_UbEjjUkQYL4JD81LqeIeHGEXil22yb5FMyiSQh1w19k1jL_96irLQqpYvS0Ks4PlxmcOiuIKX1_MrTdgEEqnwgA4Fo3AeaNCBJIkLNvsjXUXH4Sx7cqUeI1fnTVrQ0vh8Ly7OvdclT5HYVh3jLDAVObBvHiNQPj9jiJoewkqcYWdY6GSwP0bBpf8Tp4N6CY2K8zxJ3uTCL5Sc2eLfRsAGlHv4GbOdo0aB4LgQU3_8sdAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=fubmqoLDrRRkY8dL-YzwhKqwL7PmrHsO9OoD-Nat8r7GP6trBUKGOr6i82jH_f95lROcO4C8cb3sUZ4ER0ui1b6SHt30Ot7PzOU7Kks0_UbEjjUkQYL4JD81LqeIeHGEXil22yb5FMyiSQh1w19k1jL_96irLQqpYvS0Ks4PlxmcOiuIKX1_MrTdgEEqnwgA4Fo3AeaNCBJIkLNvsjXUXH4Sx7cqUeI1fnTVrQ0vh8Ly7OvdclT5HYVh3jLDAVObBvHiNQPj9jiJoewkqcYWdY6GSwP0bBpf8Tp4N6CY2K8zxJ3uTCL5Sc2eLfRsAGlHv4GbOdo0aB4LgQU3_8sdAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر ۱۶ ساله رونالدو و دوست دختر خوشگلش:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70577" target="_blank">📅 19:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=TXan-ANVazypR5fB98_jUYUNsGJU_4e9EGgMjim6LwEug-N0ayIEU5x-hrWqCscGnmYr3dzDx4s9k9Zzm6PTVxZLfYmtzFOPjpuyqR782dEMO02sOq4kMrU6MP-Hmc3r_gnqYNCPZt9jbxMZeD6_tmzopWKcZtdM0vMOjXRF63G9FVspTQdLp_SbfiH_ouCbio8A4wttbj5Fg_FfD4CSXSTpAFY3-7MdLqtBEUj8okfpdGPb2J5lm9XkMEI8f60Bzh-nMkkDRHr5iy496uelbrAMmWmRY6Wt20wqdyDFN5ebW6RxoJNtrqOnZh1eHoD5WYQlXOTbqqPASmN5gfyJOz91YUcu6rA3uJWgirqtIWwysdesbKwAnedVEk_SkQ2hnZBCwr_SIY00YkDzXQW1kLBvUDtEQhUMpnzZ7V3qUYEL565lKHg4uzpx4w00ofucqWC0oqIzEspFIKbo_a9c5e6F6ag_HdnCK9DIeg9f4nJFhatE1_oVet2a3epkGWKlXtOagU0zvjYF8VLa2zEgJTbzBFVOMhd0qQa2LfIhNA802hPuR_hR28OqTtyYDzGzgcv36JsMR6Pglj177C4B5aBoGSdX4YEugSsoFuo8yk-S-gk4W9ds8pQDG7vTAgQRza8CqTMGeRbOvlqpHCVvTQz8BkoqDcIvlcLsO4IRyZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=TXan-ANVazypR5fB98_jUYUNsGJU_4e9EGgMjim6LwEug-N0ayIEU5x-hrWqCscGnmYr3dzDx4s9k9Zzm6PTVxZLfYmtzFOPjpuyqR782dEMO02sOq4kMrU6MP-Hmc3r_gnqYNCPZt9jbxMZeD6_tmzopWKcZtdM0vMOjXRF63G9FVspTQdLp_SbfiH_ouCbio8A4wttbj5Fg_FfD4CSXSTpAFY3-7MdLqtBEUj8okfpdGPb2J5lm9XkMEI8f60Bzh-nMkkDRHr5iy496uelbrAMmWmRY6Wt20wqdyDFN5ebW6RxoJNtrqOnZh1eHoD5WYQlXOTbqqPASmN5gfyJOz91YUcu6rA3uJWgirqtIWwysdesbKwAnedVEk_SkQ2hnZBCwr_SIY00YkDzXQW1kLBvUDtEQhUMpnzZ7V3qUYEL565lKHg4uzpx4w00ofucqWC0oqIzEspFIKbo_a9c5e6F6ag_HdnCK9DIeg9f4nJFhatE1_oVet2a3epkGWKlXtOagU0zvjYF8VLa2zEgJTbzBFVOMhd0qQa2LfIhNA802hPuR_hR28OqTtyYDzGzgcv36JsMR6Pglj177C4B5aBoGSdX4YEugSsoFuo8yk-S-gk4W9ds8pQDG7vTAgQRza8CqTMGeRbOvlqpHCVvTQz8BkoqDcIvlcLsO4IRyZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صادق خرازی:
به آمریکا در افغانستان کمک کردم و حتی فرودگاه در اختیارشان گذاشتیم اما جرج بوش ایران را محور شرارت نامید!
بیشترین خدمات را به آمریکایی ها دادیم و حتی خون دادیم
این نشان میدهد یک جایی در پشت پرده محاسبات دو کشور نمیخواهد رابطه ایران و آمریکا به جایی برسد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70576" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=SpGSgETDmuR_CS5kz9Kah8ix0kKUhB55CBMZYxOcdJDwlDpsDd2m3-lpy4jAfljPoEST71MU9rxPPqRV3PYejie5aYbjfN0GDeO8CTkOjnwvy6bl5JFfS8ISNboIucCH_j4z65ep1Wecl3Sv712Mvcnu8cofxb4Qk394FLIxPL9no11d41xGMbdFH_GvDyQpbI32zeVhQTnFW6X1S9C3qGhcITTcAqUJAbVRxM1vGNiBOO_P_7JlAo23URZxCuHF1GaW_WrfwdXal7xLw9h03xTiBIXQF1J8iM6ccYMeZ4Ux8X5DvaBHCtjNYkv_TASksbsJ1QB5PMSUZGpr4nVa-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=SpGSgETDmuR_CS5kz9Kah8ix0kKUhB55CBMZYxOcdJDwlDpsDd2m3-lpy4jAfljPoEST71MU9rxPPqRV3PYejie5aYbjfN0GDeO8CTkOjnwvy6bl5JFfS8ISNboIucCH_j4z65ep1Wecl3Sv712Mvcnu8cofxb4Qk394FLIxPL9no11d41xGMbdFH_GvDyQpbI32zeVhQTnFW6X1S9C3qGhcITTcAqUJAbVRxM1vGNiBOO_P_7JlAo23URZxCuHF1GaW_WrfwdXal7xLw9h03xTiBIXQF1J8iM6ccYMeZ4Ux8X5DvaBHCtjNYkv_TASksbsJ1QB5PMSUZGpr4nVa-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
نگاه هویدا به یکی از بی‌شعورترین و بی‌سوادترین مخلوقات زمین
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70575" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70574" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAg-Nupk-o7R6RAADUkgaXSev_hb-Az9ZMqEuAlOnTuSHA94-rDCp2xl8qHXRKrIoAiK5fu-QLs2HQNw2-sxSP0AJRuOXpb-YV_hV0_j7ngTmuTio9M3AK3T88YRcAvu2ljTDUOHL2q1xamxGat4U2YApX9kBdULZF7cBnlTSJt43TygYpQSUpTfEtNTg5PWmzHbvVLj7k8-ItOd7cdd_IOKDMdlfbFKZIlkmTfLQsftVkX63KwJAHHLL93Po9XX1cAkMY1nWM7wjSKJo4zLJaCYIMg_IbTVh3o7NBWGxgALTNyKtOwfqsxWoF9fb58lNFeXJts7UUxgQeKWN30tlY1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAg-Nupk-o7R6RAADUkgaXSev_hb-Az9ZMqEuAlOnTuSHA94-rDCp2xl8qHXRKrIoAiK5fu-QLs2HQNw2-sxSP0AJRuOXpb-YV_hV0_j7ngTmuTio9M3AK3T88YRcAvu2ljTDUOHL2q1xamxGat4U2YApX9kBdULZF7cBnlTSJt43TygYpQSUpTfEtNTg5PWmzHbvVLj7k8-ItOd7cdd_IOKDMdlfbFKZIlkmTfLQsftVkX63KwJAHHLL93Po9XX1cAkMY1nWM7wjSKJo4zLJaCYIMg_IbTVh3o7NBWGxgALTNyKtOwfqsxWoF9fb58lNFeXJts7UUxgQeKWN30tlY1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70573" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70572">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtVNxj6nEQUJB9obDJX3KaD4I_q2xchFEp36K4MFTwe1vxCwCJX-JpEOZC1Je_KQKjV4hkUkoA3WIv_zPNCVuFWJRsIFAfTqXlyfOxXRqAVmw-JI7n2N4-Csqk7FJ8EA9rfTdwIV7LuGWl_zSYjIfHEB8lgTaZPzbN1Zsmdae88eYLyV19u8pztUPYeTjukYHtfarS8ZGjjm6317HZ7W1z4FLuQHzCfRemjWtEFrWanFA_2RCFDjLRDY9LLZPRNnZsmpego51McpqPWlI7xkJR9tJ4XVutLsgHvHla_H39g9PoBK2AbLTmjVOUqVyQ3PB75hrMjz4XifPLhVx0dwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از داخل آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی را در آن کار بگذارد، فوراً و به طور سیستماتیک منهدم خواهد شد.
ما از طریق نیروی فضایی، هر اینچ مربع از تنگه را زیر نظر داریم، همانطور که در مورد کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند نیز همین کار را می‌کنیم.
سیاست عدم تحمل در مورد مین‌گذاری با تمام قوا و به طور مؤثر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70572" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70571">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=d6qscwA1J9sN_G7yhDWqJYrNNQo9uAEMu2OM81y6YHr87ltDbQW9fv037Fv8e6FDv5sWNWt3PudA_Oz0fA1Mry92X3RtxexS9y4NIH-GAIk9u86rnfj8Sye4uTqNKngyxEgsa-CddbF8jUsUrPKfWKhmHWAo_tNSD5jXIGWxrHiKvr1Ba-O2ms_G_kTvDpLiS-DQpcurd8T7YEtVbrTnCXaZiEodaIp1lHp1HpXttI5aGVnuIACXBx79EpGdABlFBVPri2cSnmzYMO8SgfdcMABs9jg5bHaX1PRk-BhJ2W4zytp-BH1hPOygS_6XngtfECTDP5jpn_OsQbKpBV3lBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=d6qscwA1J9sN_G7yhDWqJYrNNQo9uAEMu2OM81y6YHr87ltDbQW9fv037Fv8e6FDv5sWNWt3PudA_Oz0fA1Mry92X3RtxexS9y4NIH-GAIk9u86rnfj8Sye4uTqNKngyxEgsa-CddbF8jUsUrPKfWKhmHWAo_tNSD5jXIGWxrHiKvr1Ba-O2ms_G_kTvDpLiS-DQpcurd8T7YEtVbrTnCXaZiEodaIp1lHp1HpXttI5aGVnuIACXBx79EpGdABlFBVPri2cSnmzYMO8SgfdcMABs9jg5bHaX1PRk-BhJ2W4zytp-BH1hPOygS_6XngtfECTDP5jpn_OsQbKpBV3lBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید باورتون نشه ولی ایشون بخاطر اینکه آلت تناسلی بزرگی که داره، گریه میکنه! میگه تا میخوام با دخترا رابطه برقرار کنم، جیغ میزنن وای هیولا، چه مار بزرگی و فرار میکنن
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70571" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
