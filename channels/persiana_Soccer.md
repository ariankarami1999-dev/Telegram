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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 610K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 15:21:00</div>
<hr>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ld94ilESsDqG4MfwlMjKWkRyFdR4Io3mxHVnX0E482NuEqIu7rZWmB7WG9uouvBNywXCOkQraqMmW6Q28-DYwyyqh6-tQH142stsrsAdYriTo5qoDjmzy25Ajk58oXvHmLcqob4eGWxXO6rRjXfEGUWBQ4uvmv7meVCpeXgz3_t55hBWqG2ArPR9TYD3xBJlDV62SHBWVubDpNsxi0WVh5bAqbVpkl1ekYXdyW8Mz3gK-TgM4OiM3DszfZoFjnSyFb2WdGbUrfvDiOUWZcAd-FiF0vzL5VFfnfKyK9Famea5qmdGAEUnrIbW-ohiIUCwfRKO3cpaMaZRnp_uFnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJUwjSWx7IxA64IMU_-N05J-3WFsKAS1TCwtxnPTATNtkyxXTECbxiPu-xtTCwa58hreidLMS1FhabYYp78hbVOMRolUvZX_4u3YhIvk8WA_HXsQWvk4tSfPA_KCc-ER72h_nFWAYSxlJ_5zcDgz6jEsNCYTrCSlBdAHaJVo5sMSlO2xi11ba6fnp-kIolx1-vATR8hf_sqo8I6qFAW3C2RRJnXuYUzq5wt0LyQa_WxjG_7T9BlxcgAI2vP9tCDBV3Hjvp70KDOVkJ6fKrV1leP61ObPh_llwQRhd5b3CYxxgHZH-WRIS9CBVUbMGpXdMud-1ISV7G3sxuIiC6ZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBXiVSnDKqMYhlnCCM3WhmCWu1dT0EXB3p3Wbw-EK2jV2f_0-cKt0vEKZ4xfmiu9VPSVhUjq-SaS-yG6e7gBIpB7IJeabMmtSNQzCsXGJeo8S5-K26fkToVQskkqdmAonss9GaFiGTiYbCHhM_PP92UG0RzDtT1nuf4oJDrE7RG0EMs8MsPabMfG0M9ypGWA5212DGp0wg0tDQ7FrNeZYhDohVFvvqjbQFBLdWkOmjWPuKhQUV3RcGeqwv8Z7nP8skwhCrRpe-3t3h192WUnUKeDRm12MLRPFcmykAyjtafgEsJda4Hj46dBDS_55Yjnc0h_RjaFOjE_iKq1KtMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7LhOHECopCBunuZXulm-XmUww9iv-6qDXYY9_40uBMP4tH9BLaEguQ8dsIqrh2XcOvs7dZqxd0Qhkz2ENw8Xvp0IKw5qnHTYqC-kmgXmBeQ6yY6y_xL5OFwhLfsIRWxBYE8LalIY2Tg9rDsUZUfuHmR4pGlea0vylHOSwF5tipNRJ_KpNjZ_I8YfvDXOVP31dbtSRAJ3IoUb4NSKCrUdnn5mrN_zUTR6j89dMu06txU0lRQFfIK7A7zScMBEd3QFj6MWewK5J7HuzTOBk5xunGUkeRREzUL4NtfSB15haXJLC3ospK5f2f_SglcTSBg7G_g8lnkhofl68BUITjCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZi6PF7VZJWzMFzkZKh1qn9FsssHnQ2Bqxhs04kqfD6nFywy--emJ3MFsuRAW4DV_8ARMPuXnRZ4npC7-tSqQWWL9OINw6-28wPVUb7HOB3cFyAHAhZEkOV8xidQ8m9EjoYvugoFeMsOQh0Qhe9rbf432EhQR5fIywhNsQwSRG3mfA5j0Ef7VmN_m6DlwsGYPimajwzJWoDhJMDJReUf_-j8AlXJeK1PNd7sXKr00QxmKAFWAEujgJ9lxuRwgtkayB1rTH5etuDayOD2JLEuM5-BAgDvPhW9Qz2ye3hTeCtRcZ-CzXixNM1HqCetFfMyDEJgwNzl53hFCbTL5zVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UikECKDFSrKlAb3urrHBCyT5tFNVx29R-tDqJ2lr-vgT1e4rDf09UWIzG99YRKVPD--hF7NZ7_r7DVO0kaG_Do-RJ842LTY6jRiEMlsqnn_3p4AFREQg1Z4Q5WFt9uG23j_HUtmqz7jwvpM-gMbf7Obkr1GK6jCF9jAcCORAggfW1zYxIab4qhZD2cW18PKtxHNO4HakPrYJtfBvvRVZRnVQ9KJ0PyQNsfHcfY0zqPEyXXoKJcOYsh7Q3zmiIBTmAtLfayRicuH1-PpxFRFMqo3wGP2MyAijWrV8Mw8O4XT7SUsO7IZQLQ7eqiR6hgkOfB9NeyX6350BN3gdKWJsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqXzCkLIMtXGKhY1O97RiCxHAooruwT1CcydwUKIGR7c4kzrrBavHDWbMtLLTzR2tzxQdWMZ0fWuHxP0y0pGK4coEfeeeO3F1aCMUvC-FIPU0-urBOZvPgulxdWVdxrv-hOSWdXYXEz2C_FoqTYBNn8dz5HVZuPH24nYC_WfPaa3XurURkApQHkOmC2a4efCI2NvJISFrd8anb1Mnx9VWdxYixmCeSrpPcfgHeVCgqmBiohzf2NF5xFxBhZSshqxXWWGYpIUntpXAqnzl1kT-xpGkIHn4BOEuhtryABfgPR7BPMWm6hrUQO7HQLFKMO4Xm-WswM-y4ZU7LvCDYmXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKLAlL-ExMUGqoAsMb5D-v1kRt4HxjhzSKljxcWCJZXjRFCBhlm2gqXHzfRlpwPVv6GohTe9mIG33ONT4D0gtlkaNQSs3EIn3ltzS58iQLY3vLb5oul18wZ9f2Bkh0KJ6Yv0OmOVV2raLhkcBhMFWjKuBQLarQsfQbeFTstkAqXsvk_BFv3Q-Y-Unhvl6LgBD5ikwuyXgBlPTs9nV1g_6LiJFaoM9xiOWpy2FPDr2dZvhfktSZrpmHtfaQ4UQ1NkvHlcAADss3my_qyyDIbNPUmHAFRxs8lEm3-DQDIZfgJcNY-ejKCmQR3AqMD0POElobLEcDL2zEM5E9cnso4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4HoJ6m5_qruuKxpO3Lnp1nyXDdFHOqijscSsCV1Z3cIJ_cO8Wyy2AQs7WmN4CHgcdcuCmTJWOSE1kLEQ-mHse6bdEttgohjXYmEOQ7O36WRDcpraF-K7rA3BioLgd_7DeKZNdz5phiBR33Bfp7QMOGc2JUHhdQ9tDEveP5oiY9ZefyOSJXr5wKzYYf14f2z_qo3NDshZnBAbiyFGwb8sVdK-n9u2WQn551aQOIlmBflamwosMULxmbT_feZL6gI0LxEWHaG3fsVXL0809h9hlqv167D_eZI-J7lbcWkgjDXIrJwJJeaeJJVRRSDXZgAiPLDGNM5e1O_OA7Dg099Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wie6JgANgoom_Avx6vLpS7p1oZ3mO80-tZKsFuHPjHewAKJa-do4LufBgpbrbsA5sNkmONJiWSsUgXkoQpQfEH8G9ZyjZ1xgssGcHLKtp3mmIO7lfmVPDQWECpVCETddFxIiSaNokaZ3I5I0tc1PcCqyJ14MM0J1clnpcmbZjTIggne1rg5XmjugCNX0QchUVY6Ev2gaoZ6K0edn7y2K-g0QBX-dNfLX1ayOEq7ecrofYmwh_IcO62T5nOded7QoieaeBX6qrQh0XQcH-oLq5dQDXQFd37q3iG1jrBnJ8yidc3EVmZ6tDTkM_H5MwCXBmmdjgzwsHWs5RA7mJwYy5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GswMRoobA8GYonPTH4oHbCoe6yezwLNzbhfFqwXfX87e1xwTNJ9ZppJBVNez2v8kMCmuvOJ4hxfA8QLz7AeUS4HzY9baqZch7YGGHUuRtMlwojURWya-4ahPILku56Rqy-ch-Qza6jIZLE-xc9PvSxlNb6KlMBlynb2EiVXnkUEkj4lsNK7wwG7jeUCzijdfGuX7T0EwkyYa50dsCHstLSN7EyYRL70aUd4v4mIgOYihDxLr8bhpLwK9BhOeCv-OgJQaiGLTgOEbUa7ZgV8TY4VGAQYqVihgYYpxZIth1e-g1tM_a_360iqpjH1asF-S3MWIyQvFcuEI8BQ9btD0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJmTNGFdA9fpcR1jWhaSfqZnSfHboihMhmR6TcmxB01FPHTyIM7yD7Y85Fqx8e5yHYFaOSlGUWnBSrUy_OYA4adXdoBA0RIZGt3gIA1uXnfivcfW0ZEiuj6rO_D78p27JWtsNiAF0js-ELF8Kr8extCa8ITjwZcJ4Sd8W0XAB84UA2EqJFXxSKlYGH8toeoFJKCDGiNaeAVQmnSGMmlN87CcZz4aMKBsvH2rbdxtlN-XhZw3KAMSI7JHoyluBrV0jt5KJil9yZuzMhIitou46ApVk3nEvdTY_IdjZ6v3bSFj57q5kA7Arw06NNq6iUaWKCXWBBHqSFAx_UnSx2fPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOiSCF02LdkNe7XeUEA2OX8-fI_9HdyCUxMvf-adhWYKxDYDzOv4g0s396P_Dxp9k_CRDGIAbG_K_fIuLMx-ps3JxqU6wvEvpyHfFM2WoVOkYvYZ2qRfoU7WN9jz8EslTQHHxzE57sdn0INz9DwNEaa4EfMv2x7sAoD-UVsIJLeO1i8HDl4uE7XquBKi1JwJv0BrNXMLOnDF1zgtrb6rbtLuQnaMxO-Xf5x-WfBGqG5RCdnZgOGBriPBSpgZ_bAjBicY5g7e8roM71C4ymBaQPlNiDmEC-AVeuHF74x5K_tnyoaJR8ZVNAvqIZb5IXDU5vypKsZSQuyuCCOwYr_i0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOxe1LFexCbOHlVa46EMKe3whmsUYawgjtFT2tnZ0H5u_SsCUIIeyZ9DwdSgvwgLwq8ccuDkTwfpeY2igQyRYbTv2kH-zgQrQ-u6QdZEqUnPT0inNnZjBlgmirQACuZ72H2Xk47gOkABq6Ho-Eq1mmuGoNPIi_YCa-q4ZhCzil7fDmSzFx54TMFqLuAN3npiFgMkmGemJwczSKi7JW4dHAVOyt8eZzCsk4WhxhTDuXvuyy0W7l1XjkkliyKr3hkYXu2WINXuHCFeJO4Ax_7pJtH2RnlG6E4mImtbvXjIKdwAHisI9fgDGldCfToDMxtdDoLwcXuXsmuwSQvrrgVIgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbR00GFTRWAt3QXqCJhSjEOMiBNkyuRXHx8Z2Ay1ZnOxvWhgGyU5aZD-GaZRWbOBs0mPSVgcy0Tmo0L2yCRlGPIlmDbpsp6nMQW78gK0FiXMB1uOl7mJeXZk17jidD7YWS8Ipv7gEBt5JL5O0m6qWFZyxFR_h4-aYwfjU5kqj1PiXP83PMo-jDQL5USA02D3mppjKtaiwK138yO_oF-vphHPkO6G2FHuF4885zUGsKu_LEPm83Qghbz0nYi8KrXLtHkKKk-prhuKbLuxndDH9wft9m4ndydh-JhltHEEDdjvBmue-9WSF8CPrzwsjemRWAcR0feVPVPK6K1Cl-RcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi-4SOOeMmEtmquHY5lqGqFJlbqG1N1rotZbFboVSDgjt6Z5bf2gNPVqGp8RnU3hedYUElT3bmyRMwJi48ZY3rN4usDjUdYKJVW82se5slxSgOp8JcSsbBye8iTjMZuN2ES1rsuOiWmEFRqi1QmDG301W3sFhloiSe2vTbiBwhQgEzG-Dg0e7QiUfCUTo486xMSbDyJReodhhrjtcAmzHzQR0d4oqW2pC3dDTSMjfeGg-YC9UKkZxXuxdSNL_3iTv1OD6PEDf7vc095YYpF2XG-Gp-JJdMjpKX0a44XAyuDYpgkzFl-bmRduz6FR1P4fJCJR7waQXEF4zZbKjSBCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEYuUktl0rcezwmTOJfF0NLqzkxLfKLLd_hSwkb4PjxZTRB8i82cyjbr2svo5rqybgRHaNwJ37svPvTFZgBwPm3nm0EaZIz0Ct7Yi21Q44-yCcqGKqYp1bPi-3wXKyurxihNPNEwRfpXMnodYo_s2_6-yfUDtZh514MXlirbSx3JoA0pVjG-RiPiC-AxuqVgxNh-oSNsKo-mtEVZ22X-tqXd8vzbI9duW-sKltZ8O22K6_b4_2tdRfxSUpngxXznqbGvdTfUS_NdxKMb9x4dFSIqEhjqOD3ATU2qmwS8Sduy3GxeCCYnVc8EJtVtxVHuKwVD3S0wUbeNDiVT19DN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWzOFoFdeadkCYEQBbuiMg2C-4Y2fAMF8BP7SQhpyZ7N7tubH4A3kZ9TqHEer3Yi-evVfK8-6drIARVWAzsCHAtUJSbJK-d3iSqOPSNDhgFGV4-4k9m01bRfqtOZxmWwlxIvP7pbGgXoNM974OnSw-0rXx9bdmIamEI5n63gWc7Dax7YMMau7XH-kZiXE1CqixXbssB_J8OXuZVf9ZLgq_JvRZUxW5BGjfmogLA3xBouuoU9fUoTgHPHXoDlOY-6f26ZnUa1a_DRzAbBWcsV8mnwl0O8nbGBzaWKSXpyiqiENUfhR2VmzZtmPcu6q4F3w-kPoENWU4Wk6w01d9ch5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhPEm4GfwBGNvOgC-cWcee2XiRZQFIaM2k_VJDa0PUt0PPunEfG0hFY4vpBZj7_7EhUBatX4PlkWCpam4rs_HKtuhrBzlwR5cfVFgOzZVpnWSVgbJ77-SLJ-3iqjlAV2ayKmxz4DssVEtNEia2pICH_zyuNTkqxAqsiz_lHesyKv22u52mAVp0ZdpyQgS-CI9J1YVDtshL2rjKdhBnqHYg8jlwERe51peSj2FdeASlGi0zyyiLFvVFIQXRMvWXk1uAhKnGZQclikKoMiVGmm5SwyD-_kzVzyIX65TG4mat5CA2zUxCFGz-js7G9Bfx58q29yd43ZU17_ppkMbJ-DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_yEyu3UHNpDbgVpKGUoQNbTr3QiYDo7rQFYGgf0v8Ni-Gtr2LdEwH8Es9hs6LGMfySuZceKY3L355KeR3KG6dsdX2ixGk1Q9hUm-sUeuP3ttfdFn00U7mwvJCIT5ZnWuuXzEzxcI3btemFFsDFoNXVHewrMLsnHO3q0sC4qn8Nz4aPGN_vXXhGAI9ZZCnXT2wagPwA_ZHtC2T--jWA2xP2v35x60WCBF0iI3t31uWJO3XGiyrTfExVPtxSwc26qkeboB60sd-CS0qXlf2hNpwMEGNwjMIyJLgC_kQEQRBa6G1BA9dS8_TjKCMlc2tRsR52uDqXUrkq14zd_nMRxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-5EqE_RYy4lJsLVyPd3IuJYYPjQWeRvtSY4eRrtNp_UMoIyDmqQXcG-0OqVofnJGBTnWO-Ygpp_PFONJBR0ozbpHq1WY9hWUnHL9ToezAlicI8rr4uspGlcIqIphY0DjRgDMuBY6YanF4-nd_Q0ISCX5_aupNy7Mr9LYIVAbvF_dviIuIlOeFNRXnFBxYoQ1uLMZKjhxHFOG_yp-cIRPfm_CjANQ5ST6re3o9HYWEvo5HqircPh3CIL5fgkXTjO6MBPo4THQw2ez6GNcgNVcSsTn7O_A7vfB16IVJ_27DisrlDtpwj_WhR1xaS3jYXSXzudLXB8YEwjnf3Qh7yCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7CqaYgwhUBWAiyBVrHuHGD2s1X91ciAoQWVG_d9iPZnrFcGCYNTrJ3hiaoKayABak08BshTlRRHMYZrzJKpTBq2CD71dmbugF6VT18eT_7Gn0ICFwiZtpPCu9ErXWbcg6a6lusM_pb-DlBW1O0edNBg61QJZfwcLKpAl-YkIhDH-rEPjlVHWfQ0EVTJSwy0rEBeAfzc4JmLMK7zo-J3zTNOXlmLlZbqkLJHfmS3HpJM_1Ur4EWHkwu_uP2zzWcl9xhBt0YSfWY0IqAjECRxz7JT0pohVxvpfwyP-sJC0sLzGyiRpJzFjxiGADf91J0Y3CPKIXSI07mk1cNiLqa9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=lvvrlSamV0dbe4Xdpcj5j58YX0duzjZY-fO7xx63IPxPi9g2iCtNm71daN05l39mtfEo-nObmrU4Z-I437uGtlk3YoGigEXGYeuyXkXAvlMUg2DsF4oWGFEP2LZr_IdxPAS0KpYpnFuxb8gDuFRdIdn8j8MvSFOHn--jY0ay4b3y3JuOB4gZ6u0C61A5wNBlu0Z8m8KZW2UPsTewNMbc7e_Lr_9e576e37Dw-XO-DeSjNnxvJZiisGt1URqJlRGYQ7vO619hkgF6gBr7SWIbjInOdL8wF1H8g808BMLt4BkkqmcEXMoY4JVVZ7K00kSheSdpNAFpdSgiwqv6kAFpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=lvvrlSamV0dbe4Xdpcj5j58YX0duzjZY-fO7xx63IPxPi9g2iCtNm71daN05l39mtfEo-nObmrU4Z-I437uGtlk3YoGigEXGYeuyXkXAvlMUg2DsF4oWGFEP2LZr_IdxPAS0KpYpnFuxb8gDuFRdIdn8j8MvSFOHn--jY0ay4b3y3JuOB4gZ6u0C61A5wNBlu0Z8m8KZW2UPsTewNMbc7e_Lr_9e576e37Dw-XO-DeSjNnxvJZiisGt1URqJlRGYQ7vO619hkgF6gBr7SWIbjInOdL8wF1H8g808BMLt4BkkqmcEXMoY4JVVZ7K00kSheSdpNAFpdSgiwqv6kAFpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA4dII8JPLK7MJeBZyaRyq6gXtRkNvbYcvbGmIjX68eL_q5UlxR-uGQesBpOac6qN6VKe-1SSusJ2xctmZjGPCORsoc3qUT3rTqkwb_Tx0O-IVisNfwh1UWZ_DsQvWo1XDW_WYdGIVYNtJv9P73O3o7QGsiQ3gHusv1uPR_85llgENe3aoQRboHAkIwYNz2lvlvRrB0JuqsubPcgSDyIv5_p1bhOrNc5oDcHT5E6jZ0u2K-juOP6UzeVAkNmn2Yo2s8hZV7tgtywevmJtmNB6AUkI-fFQ0nuzK0VMstWXhIpCCfgOxx5WTE3t39n8fsaNulcXOPy0ohjdcH4xJ9yNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp56qTSJVvcYCOX_5_1eEjRN8fmxfXItRsi8iHg0g1j4isB4H9QsTR9UOiBj4nrFMFsAVusRkW8O-jD6l1KmLawenkkuhoJPVqStXAzN-9Y2JsPrjAa-a-JL_3vbtRUX-EgF4QNQx3OTdAXtVfgkT7HZw-2ISb5ITyrV2Ti2_jhjKzlTu6jMMJQNRlyX655vyx9eQVftqGKzxXI9eMt_vih1ppYhi0aooSyypRz3NPVdPdmWDIjG0tOsh9ukWEU2ApHEJJjRv627CKiHGpt8zptGaC6Ftk0F69q1ZMczIvA2yZHzMM91_noUm9nuZI_-e2_7-k_Q10enjD3u5fkM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=G715Vc_S69ivvqLHyPIHgU3U6nA5V4cbnwzvkPTUtXjNo-jD74ETtCwDph-sd4bcN-GPSmHCY-rASGYZmzVQf94-WX0g-J05Dz_1G2iD-RGK1T_h2tunsbJDUzx3eS-ddZdf9Nww_P_bZUFhVgkXQInQwAF3tmbc0f40ex4tJ8HUphuG41qlRCTQiP8KBMTGLHvE6ofUgmWoSy0fZoWUlOPX4zJtOE5c5irnrNQ4m7ObQQpOJYdXFeCiJ9UjcuB5LKcjutWaCXvjJlCcygE_CJACmOhmxLI-cc2hLoy-1wYSMDfYJefegM92WfRmW76GEwAd3Eh3SPm8lYO29Dfjjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=G715Vc_S69ivvqLHyPIHgU3U6nA5V4cbnwzvkPTUtXjNo-jD74ETtCwDph-sd4bcN-GPSmHCY-rASGYZmzVQf94-WX0g-J05Dz_1G2iD-RGK1T_h2tunsbJDUzx3eS-ddZdf9Nww_P_bZUFhVgkXQInQwAF3tmbc0f40ex4tJ8HUphuG41qlRCTQiP8KBMTGLHvE6ofUgmWoSy0fZoWUlOPX4zJtOE5c5irnrNQ4m7ObQQpOJYdXFeCiJ9UjcuB5LKcjutWaCXvjJlCcygE_CJACmOhmxLI-cc2hLoy-1wYSMDfYJefegM92WfRmW76GEwAd3Eh3SPm8lYO29Dfjjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTwQTeDZFEgzR93qNWtLK1CrRHx9cpQNVasD8ep_IEqI9QTWC2LhvgZpFi1f9kZW7o_uVEe1rgfAI-KGNCycZCVBrV-9gRSoKej5bxP-LLVPXW7cyPYfN2_J7RxL2gv6rPn5KbBFe7HV_l6FTiRh7l0-Q8ZIJNKB-1Vz4d7wCSS4v_8aZ5GBcveE0QG6fv3l9lkN_lBKCSx2gPIPP0wDrK4-Do6kUYvI2kHfEyfijHeXyg0y8NHXALYQTEIUNZuAasIBSwXMkvGLlwurDk0Fo0dPahKGbmn7wgSZJBlxmmZotEspp1ufcxx-uoH8TSEkqCfQzLoaIVtZizBta1VhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpokXz3LU4HweNx8-kwILcG7xXDRWo8OzJe4boZxQEM4nuj4QusYxAM2pRioe3vlVbPx916yE9996zq_YXBYse1v8JEByL2SV-JqjO3gjBwE4zq9dk0osSHptA0OfQYfYpiWtJnC9XT3MalrozuARCXCI23DtfYbt8W_o4T_8nsCyP94cSPlsTdlad5iKWACUPusKXh29anVvd5LjCIUbRnDrZTdMrkaboa1dFPJgF9nt5u7TCV4-YA3wCMK6bCtHbfglp0b5Gjcg32vx_d17k4n_RJnC-y-4UqtkMtXI5DGqXtZI4n2Jh5QU2iLQ_55CQnrP364kCATnZql_E3PHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utMCMk9BmKdamdUXKcj5isBgVn5dCDbIMKs5vDH110naVCtnZ3EqX7D_h0rC_SzUvpyi0N6l_beE_TY94_AStuGoNgzeqwzR53s319iXRrlsfub31yZ1puuGtjhWPZGt99z2UtDhGZ5PmcGy53Bc3OUzme3QVQ0TIdkdxLDM8e5w1jzXcYmGMBn264DZ6jJkXyhd79WSIR0lNBjvs8fisqct9MC6WRxSjjmFCcjngaol7gkC0eKvDjzLMl1FhS1KOnm8yiR69OB6Ip7JfVJLfqy2MsqcdY7pwOz8r0uZ_BCJkEptWlbmntgeCA6b36Tz0ByVcr9oQhvRKpsQjnWtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzxOi6K07trL7ro0ivf9dq0h5mmr9TdN9hPxtjrAD6Z3G9BCXPjUuXV9kBFvORh1TBCOb8TYW_SHM1l_4-YvlykpXS4ixKLDlz0fJbnl9Nv73I_ZJw3jEjOg1l4Slt8jz6C13vT456eBLipFXNXL_2SEHkS6aGSvECnlf9wXRvJ-nGsr61Wmh3k0YxBfIt0W-dMLdK5Cjzbusfat6ZSOXU42cIoOnU_NRPs_3ijAyfBLHeDG9wHWA9GNaqw_EW2qBx9_FQBsunk6p3htCLug8p-9hyL0DL6qPDyaV_wwO5bsQsOzvJPdSyg7vMPRd_P4wg238ZQ4vHbsdzm2CNVWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rer4RD2Rh-Bwwc2vExdpvndxYAhuV2TJeXcz7Z9rNMnIBURgI-dVmGvTD7Gr-DshQB6D2PqwZC5EVGvy5yAXu8G0RiYElWP7J6HBFWEQH_rg-FMQMN5KZNbxl3ce4SAu_U6dzAAEndjtaIX6uFC0VNe1WkjO7JkbBHcXetGf3BIgF5HTjrbdaQDRBZp1hblzdXXUbuGnCNCn4Qpd9xtYNW1BDx1ALqzYnj1vo2HAoI2umARBs-aPXKjlCTbskYcp9y7Vi-k4qG8IkNBip6mTf_DSeeR4aXRjn-de2vbn-uh5ltf0CdqOugwfbqvMCSC1ULdl5vgklJ_MxnzeJ64a4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=MYSKVGNiYFXZjhlqS-qJIrthm9XfCI5m7erP4AtsVtyK3tSAFQsLQeTrdJ1jnA-QIMMfxFmaRaGd6_kDlYxKls1iQ5iuXvDRN3Up4ChHkSpV6-obUoNGWpgUaIoxah_pyIkZMao--giSFMHbF17kP5U8jSz3DYEqqCqdW0cMjPXMygWAuFNADiOBs3STUIyn2ZbfJIJtee-ijF0NIsaGCTg8MTN12l7dnNiAg04AqbluhBHVX2XV61ab91HkvQNOmZhv4OjuVqf-fdc4uyTnT7ect9oHEI8kaAi5qXfw2Qw3orwk1CiacAvqrNzLMW-36nOzdiTV7WQzAX9KS0TyjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=MYSKVGNiYFXZjhlqS-qJIrthm9XfCI5m7erP4AtsVtyK3tSAFQsLQeTrdJ1jnA-QIMMfxFmaRaGd6_kDlYxKls1iQ5iuXvDRN3Up4ChHkSpV6-obUoNGWpgUaIoxah_pyIkZMao--giSFMHbF17kP5U8jSz3DYEqqCqdW0cMjPXMygWAuFNADiOBs3STUIyn2ZbfJIJtee-ijF0NIsaGCTg8MTN12l7dnNiAg04AqbluhBHVX2XV61ab91HkvQNOmZhv4OjuVqf-fdc4uyTnT7ect9oHEI8kaAi5qXfw2Qw3orwk1CiacAvqrNzLMW-36nOzdiTV7WQzAX9KS0TyjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_tcceaNL85DLA6najnbZdzawisvUTpYEC_CnYLYasp2tiQdAIcof07YUz72uUekwJKkFrouEvxUIexQpbvzuYvOu8HWhYr6LP_ZHhfKUq4Nga3PD7eQUXCRj1I7q_LjEdu4rWm4h-a6RT7uJHInExRt_Jr-qdAVu4dBqBEnInUPgSa7i5212v2ug3C75OP9d4O7un7PZBeBfuIIva7UNe-QHGwv8HH2mjMGa-6NIhx0mAzOstSxtD60KHJ_Yf-NzQaTLcEx-UvG0gh-Pk-8neCDR7ZCTNwakbLoWIzlXD4fDk-4Ag6qYKARaJBzjk1aqN2Hm3C-r_efSBrnoBpyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPsjJVuqXIu_mQmVbf87h_ZpX7vxBxsaocMQNJl4ezTrkDFPmb_vV5RoZC83Ny55TTD0vqx3gg-v7UtDB3r09inuNcV9IaL4IClQCRtk74UMRRoWlB4IXnL1WHwHt2iiBPCpDgTWxqxwy9uh-9HeOR5jgqs8GZY8uUWfQuxD1GIXNFVP21uOybwCaKQ7cd-Wmf4oMNNqT1IZYQuU8XXOugIhOrHAXFzu1jo83J8ds4PAgdMnn318XjThtcryXhDWz0c0ZTfCFFsd7nUhFB3FfVrdsr5r60LqbRpMIdOnwYVyel0M_a0kcShwAyAZRKM0YIya2dGGkq4G4WQaAMD8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=KtKk66i2FUyb0-sJcgaVTR6HMywVfB1kPhHtzZEDoBFLzWkbOF7fXRviQkwNEwE7F-PlgYDpVHWvbsGPgcUatIbl5KzRRp85h1Bew93Ew8wwTy-pRIpsVKmtTvZZkJYiUCz3NIaw14XgxA9lcWpOnrosnYpzNO7u4bQ5_tb0uXW3lILVjYDACPZHpJj8YShYSi7y1vDNhdppmsehACrpLAL5QtRMYunYlnGj_ced0huPGEn59XQ0Pypg1i0F1BSQBbRjYmVTejzcxs8QBfODTOj5cubvHumhTXWZ7OamfA3xRUOB6TpUWkGGKetLgMxDXpgWoRU9hkUK24TOLrFUIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=KtKk66i2FUyb0-sJcgaVTR6HMywVfB1kPhHtzZEDoBFLzWkbOF7fXRviQkwNEwE7F-PlgYDpVHWvbsGPgcUatIbl5KzRRp85h1Bew93Ew8wwTy-pRIpsVKmtTvZZkJYiUCz3NIaw14XgxA9lcWpOnrosnYpzNO7u4bQ5_tb0uXW3lILVjYDACPZHpJj8YShYSi7y1vDNhdppmsehACrpLAL5QtRMYunYlnGj_ced0huPGEn59XQ0Pypg1i0F1BSQBbRjYmVTejzcxs8QBfODTOj5cubvHumhTXWZ7OamfA3xRUOB6TpUWkGGKetLgMxDXpgWoRU9hkUK24TOLrFUIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntz0VHEdSmnatTIwhqcw5UL0YUnH7bcRNr4cYsH-jwr3yhZb6M7YOlNY7ECNyZaoGCK6Cuov5crYeFSFHN5Dei3Slb9KibH-D0m7e4LbZaiO79MNMLfYqH-_bE2DvoDXseNBCcE_KI0O6W2NBfRZGQdb92NZ_a6UgrBDA8P3M7gC8Nez1c9W4XUc-ak3XV_KFiKGzUEuRF5xD-SRah541mgLa-6mw_nl8Ml73MDIaLD9tldOaiREI06bO6DMsWfJqhRQYap56JSTeTmGg1NPN9w0Yu98kZHKgnsQBi4uvdHWPnBFsxHlkX7Z6MCxKYkssJB_d-escHhj0FyOaOL2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ5aoC5JzxTiJA2Hq_dhqeKfEQQB-MmDYTTkFTmfZJVZkBVr-fe9ir6n8KRB2vt3gxR3Y8cWbqg6cbcbEaiHvHI0TYEduUTQeCGwTfT3biQMun0d9XyFyXIENfcF3XV1BRxSJBdhpCXtF_HvtOE_Ra3mWY601KJ372nC6XCDghdii419XI5BBLT_m54QxVHZX-gzSjK1QELe9yKg6RVSD93vHeEaGWAOWmClQJnHtm25tiVfK2cstKhacZksXC_XTJ4-EMijZuHm9MWvPPzboX8sVssl3wescbr3wyZA119VPFJgrRGVeDJc5N9CSGz-aw0G7BE1SqPAK66rmOdzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0CImbfxixVjZHuEuJfof1Ta1JgclrbPwUFVLyMgembNI0ndpO_YfsbywfM-86yQqmgNJsSTGf-85KNGypUtZMlvzwpKcSlIWQ1qtM6-ScUmUyv2FyZMZGG9Hdq3vY-p-AyEGS3SGfsmk4jw4SJcK4jEqZ304FlBXI7VdSj9Lrl-dkAzngZEOfuqodqUdG0E3p8I8PBmWvizMI2ep-dJeBrU69rb-Yi3uIs_sxG4ocYxrRLhIZqNTfJpfcyc9gduLblKOeVeqYB6Kz-mAD7EBEjBq5_wkYDPFrOtgRLAOXgrsx6m3jyqonUhsN6xeSuzgT7priD82EGYM4UEmHCroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVyC9kuF5ebhw_lhDy9jL7T8mq52GhPb2l_7G8Te3_fd1iufYCpRZeulnyeeNu2ooix4bYrngdrsav25mjzB5Ms2KRB0vYT5LrAYWVvGOgMF8m94Hal_FuUCot4JYDIHNQewnVbdKDBnt2ZtteaiS1g-SWX0xZ06FJK09guGaHRzpAS9H3_vo1pU7w3TGk16bf64y4zqt5biKpJl-hHTTgqs7Ftl1sA6zXIpW_abL0FjSfQ6lSg4LO9F9XZJQtiqEIQdPoWpsRr2hm8RkQLBg2UXj_42OEIBNt6gmjEKjSZSneIJmNbI0JAtdo01cWpe-i2lUf_BZyXYrq9Mfarf5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4Z-0Q-ndKPD8fUVmvJZfOXroBAEyUGSGKm9XI2Ezsg_FiZcKOolrNbPK4dzoOb6zq_ZJn-_plFEJ5y8lddMpLBWpVWMIyiLDSqFkZiWJ7WSBayBzkngKrrRG2eUI19QrznP-ooMNJTXKLqj7ypMj8u3Fj5lHbCdsH-1lzjvYLTMxwj0NZ5pqgSo_hg7_xiecn9REdaPJQYE6V7BI-WIVFZ_MbTCMbfHO30yrcUAVfOM1kIuMcFSEq9CF-wCb3GJiYRJeJT5MKGIs2JrI-SQZYr3g_82yKpqia094sDjmwUteL_K8BKldykT15SjdTlJODhIF2hBZ9x_Vil7ifQOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ZurWFa5LbLu4DdeCnf5_y-N6dI6-FZ7zA99HM2d9bHwf_6-MQgiiAObozQpBnwoU33YNVivkD3SUNAqzfnoK3TQiAMyh3t_F7KorD7X7M-koTCulWdPhak1bigpdRNhVsSFAigirN1oGrB6h0-aWvl64VVZl6HS0qIgJ5qIYlr9j9GNqetIoGFYE35OVgalhfaGj5Nvlr0Yhzs79C31gk_-yTDHrT49vW0g8X20Q3GWJZnz8_yJg-MVp_mII3e6HI-A-NJXTa4LjHifCQuq-TPkvWbysjDSA6nAuTOBQydRhsfQWj5R4OfAhVeB60p0fyYdadgWwLU7ZnHMBH1SV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ZurWFa5LbLu4DdeCnf5_y-N6dI6-FZ7zA99HM2d9bHwf_6-MQgiiAObozQpBnwoU33YNVivkD3SUNAqzfnoK3TQiAMyh3t_F7KorD7X7M-koTCulWdPhak1bigpdRNhVsSFAigirN1oGrB6h0-aWvl64VVZl6HS0qIgJ5qIYlr9j9GNqetIoGFYE35OVgalhfaGj5Nvlr0Yhzs79C31gk_-yTDHrT49vW0g8X20Q3GWJZnz8_yJg-MVp_mII3e6HI-A-NJXTa4LjHifCQuq-TPkvWbysjDSA6nAuTOBQydRhsfQWj5R4OfAhVeB60p0fyYdadgWwLU7ZnHMBH1SV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHztopCygXBpHeFyOwazErwDjBWXEsGOlVCFTN5EzYj2LkeHwZlm1QSR3OKWl6oqepdGUeN1GN_Bp3OJsgRosCNnPaliOqdpcIgCCvcrsek9QvVIyFKgJfdYqbdBSer8AQmqD029atj1duHl8y25OGRQMSDdziF9o-q7mkFTP6oFYeAvebIqjX3plcDrMwNDKrSNApvVXDc50j3qwiweTMwcnQZg2DaoyFqtX2hootLO6xOGCO59aIiI15aqVENonftTmMY-wvzQSOWp7zfs7lKp_OpKVctGqT02KR4U1LZgK27fXYNsdsN6pAom5WJJlE3k2-ZWacVL1Cj-x-yLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6S1PCqmTidcbNw8P7JfvBePa4aCwAQ8sFKfosD5yk7vUoshVRmxbyG8eoWZeMGN37n0mpRJn9uYg4NwV1DoA4bwFTlDH75gNzJNCfPFoB27haHpjSwShQ4Wb1jObX-v0TSDdyCI-9qJuQ4Sp9PIy0lh-64OKbW2HbnPFlDEzf2t6mb9ocBb9_Vnf27ggod-jqXQfmybXjj15uh9lK8ZvsoevkjIVa18Ijh9lUfUoQlE7cTLK6aWrRnyoIFzQvd5nZTI_gLg-kkRwccT1DX3jTJeTt9u3hi4x-6Ceqzv70qIq6F5JZUJim3lAmtqaSupzawQGTXygT0MYi38BMjIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=rNIg5OPST-7a918HaA8tgWQJkxBU3BHIEvbOvdKLfbh1KsBgLMnXQUYjlSYx3UXcigyQ2Y-yx-5G7757PMmtgDJOW1Ohvq1EqAy_oLuRVEhvSF_bORgqyYwfA6pMDK_o3RBZIdBwn3bJNUQjOAiI1b4fSUUQM_cNTPvSXFq2jlRXqbNrTr7FYNRdNi79hDiLBZ5Tn_lLbqIjsDI-7xC3xxuhqqbdpTTEXPvT1Ck1CcT46Xx61GBIjJsXznk7BpdfMsBYNV-yGTgBLjG87x2IZkZ-IzLDmBD6mlMg8wtuP5_C2GO6nryJ1an9PaZ4IUP7cdHyjoGwq52dMB83nQl6jjytVw7Q1hKvofN8QllHuVin55cnYzp8yHX9Sz-kA7YkHxu4r9-6U6Dp7yhXmO01upAhX5dbDsviMW_ehTjEDCd7DRtI6oKBQTr8MnXq_spBObKLH6TRlTC_njP5S2QjwX58FfeCbDIIXySGJLN17DXrnPbvaMsJTY0u_dNSB-8PtwdjmRX1ep1BBowmGebqqG4uiKsvwVutqelsJ9fhjYdgUj-RlXQtjitK68CndVuO5rc5B0TKWV-PscWbP7gC-o_O1JLN-mbVwykS2M9Eheu-UhfxXgfIcSH9WJlrpFsSkMmU1XF5WQIDobqn4kf6avJQSMkK8PG18D7rfLah3GU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=rNIg5OPST-7a918HaA8tgWQJkxBU3BHIEvbOvdKLfbh1KsBgLMnXQUYjlSYx3UXcigyQ2Y-yx-5G7757PMmtgDJOW1Ohvq1EqAy_oLuRVEhvSF_bORgqyYwfA6pMDK_o3RBZIdBwn3bJNUQjOAiI1b4fSUUQM_cNTPvSXFq2jlRXqbNrTr7FYNRdNi79hDiLBZ5Tn_lLbqIjsDI-7xC3xxuhqqbdpTTEXPvT1Ck1CcT46Xx61GBIjJsXznk7BpdfMsBYNV-yGTgBLjG87x2IZkZ-IzLDmBD6mlMg8wtuP5_C2GO6nryJ1an9PaZ4IUP7cdHyjoGwq52dMB83nQl6jjytVw7Q1hKvofN8QllHuVin55cnYzp8yHX9Sz-kA7YkHxu4r9-6U6Dp7yhXmO01upAhX5dbDsviMW_ehTjEDCd7DRtI6oKBQTr8MnXq_spBObKLH6TRlTC_njP5S2QjwX58FfeCbDIIXySGJLN17DXrnPbvaMsJTY0u_dNSB-8PtwdjmRX1ep1BBowmGebqqG4uiKsvwVutqelsJ9fhjYdgUj-RlXQtjitK68CndVuO5rc5B0TKWV-PscWbP7gC-o_O1JLN-mbVwykS2M9Eheu-UhfxXgfIcSH9WJlrpFsSkMmU1XF5WQIDobqn4kf6avJQSMkK8PG18D7rfLah3GU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq7hHpMyS6CqNK__DWQaaJAkNxMCfwCWayzwAWdFeeLjtf44M1RJ-KvMXgS9npYXwxd0JJQux_7qouvRVilYm52grnSe2wtd6PoJsjhnKp2cWMT4wcm6l7imVAAkQ9pBMUSt9NSqYf-4rGV8TS8Q71YMoBYTfYTsx0VqMC3jx6mcKOlvP7nj9feFjBW0X5dY7VgtQjHeEbyG8dGjjOMdisB5_2qH7YLLQH273jUHY_EJeDyM3HtyAVmDMbLnij8mBp4Ds8rDqhkLch9lkbVlS6CSFJwkXY_FWBMY_IBUBYbau4S587moR5MCeB7XBWVTZV9Hhe292NqhKZJ_hV7lBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crobuxyxUpyfb2N9Y7iWLPo1jmBT6oPsRXD7cSqIPEkbZrCfRtyJ-XxRANhm3ztMMPIjtsLGmHr7n2h9rl9WdeJpBFqpM7_T3sjzgqOKOOh95MBbcUo3fEpv8j6qGYI12c5DnhIuVUPawrMxZgf4MLxnOY-p1TYj6oNfLJrYBof8idS3azaS7JACTGHxrzMoeKryg-eLU_79tn4yHDCcWdqvErN6466_Mw8EbrmYJHhCyteEz5JzJiknLRP2HgmcS6ZmAqfdbPgupz6sx4RLUCFxzMFrffjIHHDUpmlRMPlRpVyh8UHLBEn1KaSscSR033E32NkwAbXKrnLXFPg6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=tDzKKep9YkxHkUQGboWRBbkbyqcnIrUqg4CZ0c3tx0q-BH7cJGmBqUb8ULJyPJEnjl7vwu0WuFVWOD4NIja0ucKEvRjQVylrpOBq_Q9jgCnqNR2a_iXtD69GSQ4wuDun4BPZaG7WEW_zaWQUkIreitGL_ds1UdWNryjdiBMZaLwXlnnAqf2qX5cbuSjnSEmZc-6Z5F6mqIMAi6ZyFonrHmHjHe3zVA8wIz088cYqr1xkQ-nzOPgtV5P4RkFUoe-1p_ac6QKqnqy7bru6vwAe1Wqk7ajIvOuQbPCr8bwfVo97djw-GJ57iDv-OkSClXimUNL0ena2G9bBGWqUAeIYyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=tDzKKep9YkxHkUQGboWRBbkbyqcnIrUqg4CZ0c3tx0q-BH7cJGmBqUb8ULJyPJEnjl7vwu0WuFVWOD4NIja0ucKEvRjQVylrpOBq_Q9jgCnqNR2a_iXtD69GSQ4wuDun4BPZaG7WEW_zaWQUkIreitGL_ds1UdWNryjdiBMZaLwXlnnAqf2qX5cbuSjnSEmZc-6Z5F6mqIMAi6ZyFonrHmHjHe3zVA8wIz088cYqr1xkQ-nzOPgtV5P4RkFUoe-1p_ac6QKqnqy7bru6vwAe1Wqk7ajIvOuQbPCr8bwfVo97djw-GJ57iDv-OkSClXimUNL0ena2G9bBGWqUAeIYyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=YK6ZEMj8tQGTzPXtuErU5gxrchWmPxNOaddfxYIaPlATmJjsUYWBtzppJcFWwSN5g4WlAqgCu85o20wTPFEp4e2gLw0LZxZaKDdetJtfwFasa4VWarfhhL-RuN1N246heMkB1O9LhmaFEjyJhC8Bu8RYPkx08rA1sCEqu4_WuKmCVxVPfwNJlNXN3JqV8m18oFfI-zv1by_qOfHeN0QR2EcO0DwnvgYUNkTeHPubJHKJ584OpGsuY5YGFqu5U2IUlmrCkhCiRCDsRMqAvdv7kjsF_yoXokmAk3ZveLlHCg9n0tMX3qDxW-r6fbaXrxJf-T9bFsz_TSGIrYF3QyZcng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=YK6ZEMj8tQGTzPXtuErU5gxrchWmPxNOaddfxYIaPlATmJjsUYWBtzppJcFWwSN5g4WlAqgCu85o20wTPFEp4e2gLw0LZxZaKDdetJtfwFasa4VWarfhhL-RuN1N246heMkB1O9LhmaFEjyJhC8Bu8RYPkx08rA1sCEqu4_WuKmCVxVPfwNJlNXN3JqV8m18oFfI-zv1by_qOfHeN0QR2EcO0DwnvgYUNkTeHPubJHKJ584OpGsuY5YGFqu5U2IUlmrCkhCiRCDsRMqAvdv7kjsF_yoXokmAk3ZveLlHCg9n0tMX3qDxW-r6fbaXrxJf-T9bFsz_TSGIrYF3QyZcng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlB7_6BtL1UC5QISl8Rsxs-yucRsdItyMOozJkXXXlF_737h-I70l4bCr1NP8RdO4uDIJr4YJVtHl1y8OpJFOP0kyTBLvi5AyWhJsPozlzZ0zABKKh9jlNr0cOrxxTP1qtrdmaB10QxpL_oHVdTDYeItNKL-jeRYCUwATHOpmJneo3pkoWLK-tJdA6MHsWopbvs6sB0H4kAJRFy2MCx2M3AzREbyI7ESPHMVLxety0w7qfEkd1xIVD3oc26IJcoQO3SQoIpKHMrE2ouZlMBKQwb5duQpo0zV3_L1Rt0und9uuvLtM_jFbOFiFQzGRBnrQr37kpvf5EQFVBrO3W2fPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O19T9uiQPp5rAwZyj-XYualAwPzczftDtkNFl75SrRcVXIXL0gLu6ZkgiP7NxhibLRTXx_QA2HsMv6oenMd-hHqGRAb5YrUPASmfHqhuFaVIsSVfZF35sHxeNDY5vTWgX6rt-b5IKchYlCTm_Q7jtdERAJec2QZM2f1CMXVTJ45c0a-7Wwek56s6eB4BCcWbU5WD4sEWEtPS9UpPkrX3_YqSJUYjW9iZo4acfffSeWEzHk9a-mpef9eV5FWiqsiojGyUJn0diqE-vUtropDECo4LP0l2lXn6vf44c4zK4xxMN-x6VbI1g_nLnvStpTW56LS-kpIUmfsbXHVzXmxJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy8PqapSc9g6aK_Cd-ObkttGG7kV-wVim6zKO9pDgQwQyLqLlweMfya55AgiUIVjiWo-lGbTynSY0JR-_V1iuOD0iCJdGtftEf9o0ASAfwMcxlSmGB7LHLpbBqFhMp3VDu1mqf8AtKth9wIyRHDv11JoQ2q1UCEpRY0leKmmtqpnv9lQRJIgdh1nCw3EKcUoEYG92BshKq4Xig7dT9iDMv0xGETPMMaPdE9eIuFiz0e9x1d2a2Etu9VYgyVwaHbzJzWA9kY9HTMMJrvVx4WD2Ws0nhO2n_mlXB5Eo8xJOuiiu3yst4mcRalU1rVsAodT9I2Dcq78-6iZ3_4UD8SCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=ngDUC-gxorXl23oO6adnfQbkk9i6JGbP4lfkbtaf__YYmaJGAsnef3dUCavYZqpA-VXJFJBpC8LGW1fbkNO18Skk6nSu_Rjb5dTPKeENJDYvz-pxsIM51OdeK52gbbs861mY6SEsM48Pppnb_hU8m_2NVvFeuP84cpsLN7auJNJB7wyRr2DCXjWf4ux5hX2Gtm0Glpj93qSYJpVburFrdaWln4S5re3rng_VynWuhc3vwzkJgkokl5ig7LwWsmtAQMuPMoBNP8apg0M-y-vxRPUgVYFNyPZ7gqAixKTFg38ajr3LJ6dvtVNSi63Ujbu4x2o9arXH8_DOShbxj590dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=ngDUC-gxorXl23oO6adnfQbkk9i6JGbP4lfkbtaf__YYmaJGAsnef3dUCavYZqpA-VXJFJBpC8LGW1fbkNO18Skk6nSu_Rjb5dTPKeENJDYvz-pxsIM51OdeK52gbbs861mY6SEsM48Pppnb_hU8m_2NVvFeuP84cpsLN7auJNJB7wyRr2DCXjWf4ux5hX2Gtm0Glpj93qSYJpVburFrdaWln4S5re3rng_VynWuhc3vwzkJgkokl5ig7LwWsmtAQMuPMoBNP8apg0M-y-vxRPUgVYFNyPZ7gqAixKTFg38ajr3LJ6dvtVNSi63Ujbu4x2o9arXH8_DOShbxj590dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=UyQzqNWCzG9BECe6nJIeliX0_NSPpNEj8xcQoS5zFORY7AA4_Evq8QSzSf4FrYIN9h9LT5v55rbcI8bKdUf4pocEpe4MRv-vAfjn_Uut701IB6tMudZmCyXIP8_Od0fp-9HPzJILivjL7MMNcatp0zqSt4qemBn8He-lwsiXPOVvbGocPL-DKVg_6Br6bzFD_1mcBZwmUieFB6j-5p2MuD-HWVCyQq4BPm97bI2mfaNxSmVtVSxcWjGsgfuYhjTtbWcQdDBi8FU2bVca3r7QaUYCbCc7XcfiIMc4gwKqJQRRJGAcVzemb-RuXQnnyvg-BeO-c7vMWyNDxKJqQnyqJKvboBKTtfuN6f5932Y38E3k996r8fQTV0j6nA1Dd_o7-zw_zSoZAwZpMuvNxjSWCUmYMnk_TA7eFk2Wg6bFduO_N4r6aiuNjJD3-0Bjm9EYs8T4rL-hQYUQCZDoJMV2Pfggy9Mf-HSNuubag4VNF0mOhnrslMpWXWvN7Xm0YBB7GLx6tYQjoJQQ7DQxD46wWlSRbJJKEd23evwy7_LXQqN-ZmXYfhVWpzKudM8kzAjYoIZGty50DrSQ0NNrX3NOtgTjkBdEJT29ADNyg8cAwCAFmN5fzBobIn1Fpi3MktwtgFD_37joWJjPW-5IURF6Xs6mIqsDGYYWIPW9n1tRnHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=UyQzqNWCzG9BECe6nJIeliX0_NSPpNEj8xcQoS5zFORY7AA4_Evq8QSzSf4FrYIN9h9LT5v55rbcI8bKdUf4pocEpe4MRv-vAfjn_Uut701IB6tMudZmCyXIP8_Od0fp-9HPzJILivjL7MMNcatp0zqSt4qemBn8He-lwsiXPOVvbGocPL-DKVg_6Br6bzFD_1mcBZwmUieFB6j-5p2MuD-HWVCyQq4BPm97bI2mfaNxSmVtVSxcWjGsgfuYhjTtbWcQdDBi8FU2bVca3r7QaUYCbCc7XcfiIMc4gwKqJQRRJGAcVzemb-RuXQnnyvg-BeO-c7vMWyNDxKJqQnyqJKvboBKTtfuN6f5932Y38E3k996r8fQTV0j6nA1Dd_o7-zw_zSoZAwZpMuvNxjSWCUmYMnk_TA7eFk2Wg6bFduO_N4r6aiuNjJD3-0Bjm9EYs8T4rL-hQYUQCZDoJMV2Pfggy9Mf-HSNuubag4VNF0mOhnrslMpWXWvN7Xm0YBB7GLx6tYQjoJQQ7DQxD46wWlSRbJJKEd23evwy7_LXQqN-ZmXYfhVWpzKudM8kzAjYoIZGty50DrSQ0NNrX3NOtgTjkBdEJT29ADNyg8cAwCAFmN5fzBobIn1Fpi3MktwtgFD_37joWJjPW-5IURF6Xs6mIqsDGYYWIPW9n1tRnHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PToqU2GcWBAHZAV-f3dcPW5uehCby_nfMG7reD9MZ2-eaeCsVms-dDxdOcPjieJbbzaQ28n9egRwihm49TsMd0SJJa7-yT81sBWF3vfyXNgkCisZGhA7Uq90nNZh7XKb3ji_dPpE7GlF318mwc11FPguLwBUCPDcYFYkGugAmpVhjARXIeMnnQd42Sw8U334m5z9pA7S7v8tgHef45aFzaizoJ26Mp2JyGfC3tuWLszhKYKtYOxtAItrl8YQHNzK_9IIOlz8AKnjoLAl3rqACR2CwX3hNBRih72IXHp3yhzh1BZLcwMukGKoPN6SJN6HbHsV0W9z9OhQINeYezOEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A29NBXYi4MRjv673pgPusBjykpY7stMzguQL7KC59O41F-cbqIuCfRg85V4D44eu2f569QEKZPt-31EUKZN6gKDMG4FPwTFM6h5V7_8HsHo4EHfb4TG_AtvFUlYm30Lue4T2LZcIQnhMeWZNpkngnC4eaogOEO9IyKI0KKiDYH-c-qN-KThVQNrVvGvZc49tQowNhY8vUMgNbRReIGZCcchltJUBwUfYP199fs8uZPGUeAZ9qsBTzjhUM9R5qSKIzCk6BpjVatQhTmbJsfcTNVjbOd5FxJvo7600E3pV4EMqy1AXMff5EzfO822fwmjpEEkDuzTwLrquizb6gpPKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTdiA7MPwVhLknPZrCOOxT8D4S-i_Al3Kkf6Hs65wHXvAr6etk9MtgZEmUquFmuBYEmDNVPMlCo2ljdkx7Y9kHBIYkxCirlFKcYmn_m3S-Ha-X4LZhCPfhTOi_YrbJglf-BDogDGe3B-Zh780t5RTFIMpnD9cXihcrATAFXIgSlV--dCeV-aqEUb3myM1KcPlBD4lqxGtu50dcizgPUM1SQQIh4oN0780P9tAYUXHu5LLAIzHggzoJpxG4xnRR_6k4h5miBS8ILumpsfHBAgJsGBcQgc6vUria0D0vvMX_tpICChSxGXOZnawbYj6BwEiR63lsubqI5m_teutOzELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYOnpBUUAA5m0Dq1mEVC-yr87KAcp0nK9RVUBE_Bdt__Fd_E4iAMUMmmuLtQdHp_QTHbBoWQiTEti3nV9yacDltqK7T1YHoy-qLfASxs8zKQdES2KUW3su2srDcIMAAwUv1NVit4JSKblyU6gCEMS_L2ScHYG_h6SHNrFUm4fqKE5wXov6JaohMucE-UpQdx-A1o5PUSfRMY9hUp8QejBDqY2uNoWZOmOdW4lxX3IDXvdzJ0ea1wrPJFHKfLpd4qG5WdUniDLKlh-9RA-svFDKt69sIzTf6QWwLaGjhNK55iTOQo30hBBtY9vmg0lgZFYOM1t8rYkiK0UV470Fd6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HP7QTq_aEcazJjk0IywQENC2PyBLpIDab2YKJQunAU0OfvmFVqGoVlfKRGXNULgvGfGjNqulwuzcI1k6tsYUAjqOprixZFNXPGXVElraJgQ4a5c30iSbv9xYlJppIj9avLQZowAS5DXkQ-Ax2Vl8PHCcffrRF4bdd0iY7sEjatNYokXNsPt-AGnTj-Yk_sPqPnXzarS5tlrqEIAXipA2lnwmty3qMCyHEVVLX-LXZfRlM-EcTWqDUmlWdErqJyX51dU1JspobEkdEeDXNKOwg6FKQ8npUhA1S3Ks_oL-5K7YmTkzIe8tT9GsH1XrMW9d1Fm9KHv3Ove_6rnC-5mBbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPVn7JsDvKylOE0iqX7J-NLzd_o1dxe-PiBWUPGkbR8g2sQpAwBHkya3H_np3tAAkPguo_ma1c26EgyJUznJ3WQbvJJpZ6050OTRZ6ufC0k3j6gxfZUOXrfr4ZYv1qTyjFqEZuZSgbkAZ7ued7Vt6rhv9UFNYW_JgkiferwpRmuNT_zv846q9jaAVzHRAeOuLVzbPQr0e9S7rV0vbccMZSmlqm5NjJ100XDzWHS1xb6aNzx_Psle_hn5Dvj-eCEgZRIMEwJsaRwZyri97__9QZI6bm8ZOCZSF7C-h6q3HDdS__E3Q80kh-FHpca5qvRmLtMmeyUf7z0PwxTM9qcqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFOTAT6xbz1HKc7-aa0KPpdDuxjNyiCBB-kp_iVkT-qQ7--4ID4522Hhl5BvUyZe68jFvitcZNVD62TVD4BF1g-qn4g_zGz0xt1-HoLCTWXmyTGnPHN4ouAIvDzVaOKJ9wRkkcPrSFYWLvbuoyaVqLrzfODV--IsdmgDWS-bsOZuwQM2jxn6JgL_MI0sr7n4xilh_bV9UfZg-ScmeGb-0nqYPClJohFdf05k7NfAnf1Sv0qFuiP-y1Tc7KYgS8LFBXGv8wxkRimY1Ngw2E0rr6b7MRc97oG0ip0EIcsPC4bXGQWbsf7vbYme4WtOirNJ6BfF7wrVDI_WcCd3Y3f0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=Z-FCz_GnxwOl70FyPFvGJbBh40-0q3zuv5WUVjW-02-RI1s7vKPQ5e0NwODNTcAnLy05ofmTqIXi4898E85b4CyqbKiwXMNDymHo1_HGpcphBM1itWjpN_dnENSg-gHzzRjggBWBKqGrcLRujFHLiL2BbYgkpsdmckTW_p_6BShA2UQ1LkkkBTIdnFOOoPhHDaRFR7axqmVtvt7XWl-DFzHsCTUuAUk1Zv7SxRZsil6rr0vgG_x1D94anmGShvcwGu5NB6F0_HFjxCPS13pFw8hkovofaVQNwJ-38naTmDhLDkXA7hCH4bHqSJ1PfK2iCiOzNOovduUbW5YXGwuBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=Z-FCz_GnxwOl70FyPFvGJbBh40-0q3zuv5WUVjW-02-RI1s7vKPQ5e0NwODNTcAnLy05ofmTqIXi4898E85b4CyqbKiwXMNDymHo1_HGpcphBM1itWjpN_dnENSg-gHzzRjggBWBKqGrcLRujFHLiL2BbYgkpsdmckTW_p_6BShA2UQ1LkkkBTIdnFOOoPhHDaRFR7axqmVtvt7XWl-DFzHsCTUuAUk1Zv7SxRZsil6rr0vgG_x1D94anmGShvcwGu5NB6F0_HFjxCPS13pFw8hkovofaVQNwJ-38naTmDhLDkXA7hCH4bHqSJ1PfK2iCiOzNOovduUbW5YXGwuBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa0A966xRgBgcTOHNc1-NpPJbPx2xv7kB4Y7AhCsBPrHMyKKswKA3dxoEaJZvBnTRs-49AoozCYj82jDov4a-BSYAHlhj3ybxlC7GwzLDHQvwo1riRNQ-WPdVth4oDLIH28GK7Z-jT9QTl2VmA46QqRLUhkWUScJ4z96b5aYolSzTEj6TPbXs2TcJC_KR1Lk5WayDJYaMzH-u3uJBEbA2hZvY3B8tuFfz3EuDQKkh8JVXa3wRAkPqnxKr_ssO8QEaHftuYwSSW6QnCbvG3_F_qmgx81F3xxZ9lPmA4hg2BRhOBBZySzTkjFG1b8itzb8HZIcdugyxIPvT7u2wXoRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJfVYa3mvoBb_GYF2xYCCHpK9MAVG601dW8i7osbq-qmokzkhGqKErswrDi9FLAe_TuRk4TqayJq3BlTcNmeR666PYWe9Te9fKkFoUPkPjpfdEkdof-5qjjWnVleBqIsi88wZQTaHe_pWjOPZlgSSu_aAjLPcXIqXSbV5gFi022MBua2s95WkwvYlbVq0B1Wklr1ZFBZuLgCzoiitPGx3TbfnK-rrY6xkTTC6LI2gFQpqF3bP6J_kslcopDkO1qg33btgU0vHM9OzV1psxOi-NHIQ-G6ALzREpfZFtCYnaWCKRs1U5gpPCxNO-Uquoo-Ts_vKSfsGxk0PTh6ELl7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2usbUpa1RFsQgMRXktiuPbOGZhivJ2S175DyeUxY_sYyXeBjBwEkIexPMbQJGgeopO12MmmmURuaoqdOkemjG9xG6IOmc_SiDWnmsymtCa4lIBVJjH0Y77unVElXIDrfMMXNjCsJwUyNtWf1V6FRCh_Ox1bUmVgFhNcqiJO36Mb8gO8AHcEEUjIBFGVHJgbX7iA0NQaGJU0MaimaYAeCnvCs5ec2wE__yh_wlFcGOoxuWcvIzpiZsbUw0NUbn6nCDuQGz4jz2vObIz8sxymjn0VLVpA0v4jc3gL4YB1-fCk6b4bsW4QT2o44xsIKUWiiP8oFx0IWY6hQSOzNtO5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPZk8sekLl02UmqTQ_JIkDecG1r66xL3nQyj-wN5rJtnEqJ8wv2finkW_IUn3Larz8BcoJL_lRAjps1h-hn3uO7LhUF3KtzYp-DQ1TkT91AAy0fC_hjukjs_PmEWAjKL7blJv0k8zhGAG2pMoE42lPVPlhpTQCzVxRCBWokKGP2fenYjW3GZKCvzNGblddl4EOgCHerSZKCfSSbL4A8P4PnFmSFI-Sbk7n9pmRJFbxL99yfsFs0-Zf6AJmxE-xLUD3V1GLEphptApb_GBowjrZMChWpJN5YZBw-swRtQ1deusvb3PNj5b6iWqvWMnmUibPp3zqGyxsv_ycImGAddQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=XccsoFxO2X_5YrLaZvlk3JM7Sz5z2SA1elYfL3Lz3KQ6rMsBoizIyHs8OkIAjAVHFBOWvzEsZ9OMwBjqbAno8Ba1vQlQu1lq4SZfv6Nl_lxNgy-FqlylYCux3dxGziVtuwBUJ8uy3O_Z575GJCkntkStcuHgSWiSSu47AMGxayrnq3pM8HWBmuLUASUTDXC3XnJEsdyAv76V84l-BnDfpP_-e_KPRD2nggnMjW7HXTfvccndj3JUmrpKl6GFfZQCh2cM9VWb9xdsYj--ZAqaxYKOIAqaZwVdAzwDwN5DHZ2aLQ0YXQaG08vk4dnJP33kGDGdXol4nfp8gk0FHIfuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=XccsoFxO2X_5YrLaZvlk3JM7Sz5z2SA1elYfL3Lz3KQ6rMsBoizIyHs8OkIAjAVHFBOWvzEsZ9OMwBjqbAno8Ba1vQlQu1lq4SZfv6Nl_lxNgy-FqlylYCux3dxGziVtuwBUJ8uy3O_Z575GJCkntkStcuHgSWiSSu47AMGxayrnq3pM8HWBmuLUASUTDXC3XnJEsdyAv76V84l-BnDfpP_-e_KPRD2nggnMjW7HXTfvccndj3JUmrpKl6GFfZQCh2cM9VWb9xdsYj--ZAqaxYKOIAqaZwVdAzwDwN5DHZ2aLQ0YXQaG08vk4dnJP33kGDGdXol4nfp8gk0FHIfuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrbcmIQpxSCx9JsVpsdPuVyZAnC5ehtFI3PZZIED35tx0qw2T1Kmjf52-judSvIGmT2uLopO54zD7o6A2K2P3B-RrMp8OFS-6AMQuNzzlviiVU4QfUPKkUFcoOGrNt4oX74S5cmlZbZTz72GVF5Zh5pM_hodRVXDiu3NgQ8msU9N_5na_mJeHqLW-9W7kDekbj_MnCDscEXcl2_A9qzX8fnYnzgoPEXl6_F3vCutZfr6LshiD3b9_zm1GMY68Wy7LfSiERNcqKGG5K-iN1xpjAWupvCuvfLwsfnW3_UEn_dmbR4j-xmoBA7Dflzqr1IBnLnyGkTAHmx9hvPziKBMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXzOidtImPGxczGoUB0z7zEgtSirUkN8l68PKrjgqrA3os3m49-Sz3eXyWZWTPA7QRJ4nsEfJehOkjFHdkEn_vDUrgmA9BymfN57PqMaMYp_pzvkEhnDqSwgTx-e3ms-lzLV8lMqDHOHvNiOCFW6Rdsm6V-0QI_QPHwN7t0RwOgPfWg_cxb4SGDAOQlQyj9oZ-f5VZi5dUKMDJXwOvXAjc1VLfMdvJEwOXZsfDp2oEkPLrDh1IXD3lc1RbTMB76lk-Df3zHp0yZneak1H26s-iFZYkmTPxsg2XUUihWWaXeQGhTr-X331NDAhwtaAd9NH22TP1gONojj4MB3ly_KKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1N-1fiuvkoeXHuAL7dZTOIBiYfPkxjzF3ejPkFnc6mMvO_QXLnjOP8xvURYgFRzFhA78lhoKFF_y64p7miXRpHRMEr0pOdxBXvj1FeOp8qkJzyPqD0lrX8idaxZZOINtto3Z9b3aBvPQqeXk-KyiOJx-GZmp6SapGRTtI5E2hwy-PEM2uspR4hGUcQbT4HH5fytqXn2JUl0yPxY2TT6QY2FBz7h-AWYBB7BMTVCwDn0RMApQ97IfBr8c3wSneVO5iQYXMeuvDOXEZe9EEksttKJZsiLJEEX4kBWvT3Ruvlzx85QjbEYiHUpOZPnu8i0KNObS40QqTv6ZmByIEl47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=liBaxB1X1OHpDRMr9V1dCTa4mqTj0fsJbqwKEABzBeJGIlolGfoTH1HG8QiBoBWE_OrAkl1tFkuJfHU1_7xC9OCM5pz-h2atRWURyFSAH_bz18okF9EK3Ndv-ta9Lxd8nCGjn6_AkVMYshy2NW4PpqFR1m-SCXTWk5fMIsC2muTGZ2IJa2pBO6WzeQSRlrbF7s1yJ-tGv1df3Y1YDl1ZGnvZ9CeQ5RJYSF88MiKRompO82bsEHMQiRxBxNhOgsrj6m9KfSI2_sJljbtz5vlwiyNms3h_S6Qnvk0TBa3_WhA8IMOiT3Z_N69oIXaEW5pMEqMDACBTJ7i8zZ2GCfY24w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=liBaxB1X1OHpDRMr9V1dCTa4mqTj0fsJbqwKEABzBeJGIlolGfoTH1HG8QiBoBWE_OrAkl1tFkuJfHU1_7xC9OCM5pz-h2atRWURyFSAH_bz18okF9EK3Ndv-ta9Lxd8nCGjn6_AkVMYshy2NW4PpqFR1m-SCXTWk5fMIsC2muTGZ2IJa2pBO6WzeQSRlrbF7s1yJ-tGv1df3Y1YDl1ZGnvZ9CeQ5RJYSF88MiKRompO82bsEHMQiRxBxNhOgsrj6m9KfSI2_sJljbtz5vlwiyNms3h_S6Qnvk0TBa3_WhA8IMOiT3Z_N69oIXaEW5pMEqMDACBTJ7i8zZ2GCfY24w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=G73QocZLO4doyM9g_iHZb3kac5UdcR3YFSEJ2UYp8AWCkZRrn7OpRt3I1AFaRjbUgyCIxocz1bfuDmNxOYRO5gr-WFOt2Il3--FvvJBytldPRgaHdmptfkn51c8EuykZrjIrjtNLfjmU4GuzFb-qH5R0WgHCmN7a3LPuY4BABgO25u-Et8566bsKfsBgu4bnnD121hyWYzkhFOV0cSfLwKt0QnLKmhIv2AeokfrQ0F9gsYGMbMA-CWlbJn5LCKQFLNzgSPom7xAI4yjPi8fhVuBI9nQPmrBsQSrm6UP1te7F-Fe_fu9OrZM4WUBFAX9GdfPnOuBNQ5bRSfKV4OWCTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=G73QocZLO4doyM9g_iHZb3kac5UdcR3YFSEJ2UYp8AWCkZRrn7OpRt3I1AFaRjbUgyCIxocz1bfuDmNxOYRO5gr-WFOt2Il3--FvvJBytldPRgaHdmptfkn51c8EuykZrjIrjtNLfjmU4GuzFb-qH5R0WgHCmN7a3LPuY4BABgO25u-Et8566bsKfsBgu4bnnD121hyWYzkhFOV0cSfLwKt0QnLKmhIv2AeokfrQ0F9gsYGMbMA-CWlbJn5LCKQFLNzgSPom7xAI4yjPi8fhVuBI9nQPmrBsQSrm6UP1te7F-Fe_fu9OrZM4WUBFAX9GdfPnOuBNQ5bRSfKV4OWCTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TibGVGcSM6fYW39IMSC0NfujHhygLmmW3tKY9QKwRfLaAc0G8QU4gMtF0q26VBQbCpEfWybtTe4hTg3hEJbSJrK-SjLsePPPJtn8b8I_YV_JNYOOnxUBkcKpsZkUmjEu72tqeTab3fHIDSwDoC-_Stro8Ql0GMljZL8ZC2KuvRkeaTpvfN_ic_4ioM8HPKXXrmhnI0OU3OYHeSKAQqpQPjypXeVPh_O6hzQ5cdhROPAOc0FhVVGnxlZ760EYkQWQGj6HAVW-xTXi1JTtQQbg0wuSyfVdbNEvDPOMfgMY2phM4b4mSSuYak7wjxJAB5Ur6q7OdGHx12h3Z3XWo_iR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSXuT3tMpgt36006BGEXDrJqdtsa-7_LZUk8qqVCElcz6y5HhADSEBpNN5RZPewgGJz0oDS1mwnDh1YrA9U0gM82T0hg_3fVy1JqUCoFpsyNSrjW22uHy02lhLr8jJ1Oz7ldFqGjzb-zNdAAm2oYXFm6bUU8QTIT38hK7hs3fKEGRKXTduN9oAGDhvrdC_SQR9lHpNbg8fXxDL3N8r2_yuLQHVKOoNUcfys9ZGLLpBxS-RYxHUsAcRryH08PXnOQZUSrD7OEciOxvoZmOi9B3cw92QMSJuNT0p-dtc9IX3CkJMReOsAG9T4_jyOeLBKyADepWweI_QetHBFKVLn2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=Y6bH-trma9ce8YbmTWPw3OeE_TUOTJdUwZFIqxRyAXbeq87EbBGOPUHW5Url57Vfd1uKc3Z8sCGdLnJJAD_c8f883yJaqAPj4AwvdhZjgk0ETu8SfdJM_2Z4gsCP-ecTeqVKI5zxduG0nhIltPFMDDRdbyl4yNFjUBEfN1JQiKpZ80eMbuJweRA-J8gfnFYq9HW6ArR46nvu-japVz-FR_Rys862N1TwkKxI1B23qmk5JztzZnYXogEIM5YmmaXyGEIxaHCRJTYP67pqHU3GscAP9g4n5brsaYfchFKRBOMQVoMetOqCllYVH69Ezy1JJq1aZHtfZWOk-2t54adWJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=Y6bH-trma9ce8YbmTWPw3OeE_TUOTJdUwZFIqxRyAXbeq87EbBGOPUHW5Url57Vfd1uKc3Z8sCGdLnJJAD_c8f883yJaqAPj4AwvdhZjgk0ETu8SfdJM_2Z4gsCP-ecTeqVKI5zxduG0nhIltPFMDDRdbyl4yNFjUBEfN1JQiKpZ80eMbuJweRA-J8gfnFYq9HW6ArR46nvu-japVz-FR_Rys862N1TwkKxI1B23qmk5JztzZnYXogEIM5YmmaXyGEIxaHCRJTYP67pqHU3GscAP9g4n5brsaYfchFKRBOMQVoMetOqCllYVH69Ezy1JJq1aZHtfZWOk-2t54adWJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0bd4R-fxIDyzu6h5VUV1di_lEi4M5N0QAtma4OZ7_OqtHLr3AjCrHiwzGjQY65Xmzzybmo-Ggzryd2YM0ELgird0huY1Nt4EKU5PC3Aig07SJyfMnldzgNB7RauyHGIvVjmryWGC3LbnqOb9ULUNgNm0AISceZpiHpeabiKwSbEai7BndukK3YcLKxVTfjoxXYCDGacSnR1l7e8qTWh30JqqXaMQ_-14GLp3Uazp5XmT6emGedLiMwSCqdXoHQQ4J0YkYaESTAZ5HAA3OJk8R6vLU_6Nogqv6v7eePh8Lh5ef9CGRIfQ58ZJ9Btul9q9i3LW7IckbdKQoQQTM2flw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THCH6fyMA8GrNIYYSnT4nblbQLFM9wIPiav0A-yZA7rSOK9LSSutPqrKI5v7COSqDTpkW__Vnw4xgQ-pvvYSXsLqjo2mTeyWESx9lFsejGoUAflCcLyVtjL3BW6MSJ1ZxEKFKJVnIJLl3gKoHpjPXWqQr9AqoKcyh2xrYFkZ-BhXMS-g-TDtqfDfJ6d37lAqZQd1SzvGdp9jDZ21h4AZKZv6ia0-3wJwiAy3cZYy48PoJvQCTeE-N_xL_PqmLyu_ciXHeUjroDRXtJKtujhapjVMElQdtR53wf375W6f7Qh_xhqOg-kGUwlnQhDXjpTAEM8F0WBCfi-vN_Bf4DrxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5-aue5F8H-bFlUDrSk7LL_pzYYe3WIUO_ifQpgC5fRvr-iPRo134eaO-DYDHa5aTwohsKtZJCf6zumbZCGDCTxwHHXHB3wnC3EzXUHMXjwf12iRgzL6qtTtZm66rFsBPRaKEJLLCCjZ87IDkPNm4np2M-cJoaAT8KQ-CeVteyBeOX_XxVyY7vhJHka3e-ilhWUs7nIzFkhXHRJZhTbcovqBzXLCtrnSpa3OY9tAApWL_2nyxSb-kJRTCWAApw7bvCwakT22Jj1HPSrsNpiUd6t00IcQG5WWfRZbq4A_rUT3cc8DzkpHwsHvmKWYyu-WaxEpwRW-7PE1u4MXB_2BCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=W-7iObjeDjNOfbARYLNkG3RJvJPaEmSVMErqS52fqDjsJpYuwtwPibHgK1CInEqdFf0_b87AAF6MeLbqbCXdI3r5kZDlc8nGdZXUodYprJbKdtdsqB8YmyMjy0tfrdseSurDMqAQh6B9ZQmy-ROVkewJHyYBXndAb1wx30xsDnBZTS89x-S_iq13FdYA_wavr19NA7FG0zXW7dkrpPLZqb8sJ-vIaEOzX_1O0d3bbpUmEDX0T6Q4V7nmxEZ-Z-lHfE9wDGbb5pdknRZn1v7vp6lUuPurJN_GbQvC6FHEmzuM1xab5NffEUzguXUwQHNvlO0SHguyIB-hGo1fLbgLcIZ-JrlEg85-dKzA5JJ0b1ACtKU7xHaxeAlpPl_4KncRfM14cjbWDn6Iv512MWW_1V8hBsaKQKb_iYCkwSJHI06_4T9DrIg2F4EKs3wO5B681rSACJVSVm2jU_0vF54g2SHzLeTFTEasonXf2BwgkKit_djvGfsKVXW52iN9nbrlKD0scaBtUnSPtQTQyaNWUTv2aWbntmFFZJd9uUV8psV27lFa_0EtQFGeEfAEmObnAtXHovv8T7W8HhPsDiBriYk6gzbKadOqCFpTfiy7BPpdHuBltH7mLQzWn5F_1AwrxP6x02sbjz9c9MT0fsdQrsIozlCWW8Pg_fgfSWctpK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=W-7iObjeDjNOfbARYLNkG3RJvJPaEmSVMErqS52fqDjsJpYuwtwPibHgK1CInEqdFf0_b87AAF6MeLbqbCXdI3r5kZDlc8nGdZXUodYprJbKdtdsqB8YmyMjy0tfrdseSurDMqAQh6B9ZQmy-ROVkewJHyYBXndAb1wx30xsDnBZTS89x-S_iq13FdYA_wavr19NA7FG0zXW7dkrpPLZqb8sJ-vIaEOzX_1O0d3bbpUmEDX0T6Q4V7nmxEZ-Z-lHfE9wDGbb5pdknRZn1v7vp6lUuPurJN_GbQvC6FHEmzuM1xab5NffEUzguXUwQHNvlO0SHguyIB-hGo1fLbgLcIZ-JrlEg85-dKzA5JJ0b1ACtKU7xHaxeAlpPl_4KncRfM14cjbWDn6Iv512MWW_1V8hBsaKQKb_iYCkwSJHI06_4T9DrIg2F4EKs3wO5B681rSACJVSVm2jU_0vF54g2SHzLeTFTEasonXf2BwgkKit_djvGfsKVXW52iN9nbrlKD0scaBtUnSPtQTQyaNWUTv2aWbntmFFZJd9uUV8psV27lFa_0EtQFGeEfAEmObnAtXHovv8T7W8HhPsDiBriYk6gzbKadOqCFpTfiy7BPpdHuBltH7mLQzWn5F_1AwrxP6x02sbjz9c9MT0fsdQrsIozlCWW8Pg_fgfSWctpK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv9qWkNIjSIhCSTqA-THqxCplxsPSNTc_PKm41MEEqt6d1tU9Xi0MAFdG88_Oq7IJ6kMC8d2-YSowBj-_b5Q4ZEjiBekNTNFFBDXYpDtMZcbb2f1ankvd9nHk5XVrJnqRFuETK9JvdSr9aIw8vE6jdLbU8frTpVO0KohSDA1xnNoKs-4B808AlZCroDK4slm6hCxgcznq-o069CM1xCWbcOrZhmuRKAtclOYCNGN3d9MkXewDvLWtrHMBdLy1tINseQs0AZWQACVyUC5mvQ1KGYb26Pbq2c2gul9YMfbRuVAJH6PoBSmERnuGNZPc_51AaZC63kpT_D_fxhdVwe40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
