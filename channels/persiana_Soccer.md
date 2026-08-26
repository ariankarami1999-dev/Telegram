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
<img src="https://cdn4.telesco.pe/file/XjeLtBYYcbukWyZxQEsOZrPo92up8E-43-Y4Ed_F5q82qrJ4E7vmMjm7oBKaFmr8uj5Cd0f9f96N5vnVy7GrRV8mt1-gryKsEJ7GY_-uX4n54NV5rlN1xGO6Yxjcz5JcXPJPIhchfsjMjGqv6jdPhDv-Fgk198m3IqV5QjpWqdWTViIpqt5PC6CxKBauPuCCLi4CIC8i0214k-jv82m4ZcDxhNBPFegq3r3cDDqNImvS7zfO4HesJ9KoTHmiMohJN2fdCMztfmQAvreKB3XZlOmzuZAz95AEdALqFXtna_oMl0Nck-YtMxH2Yv2Zp9nOdlOiJJXzar7LFeZvGMAMsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 623K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
<hr>

<div class="tg-post" id="msg-28546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9LxRFTr4m4r7rUKMbhBKuWYbWtNVQxFo8EUNJ2YYBAnYvDaJE9MTD5TKFEj9DPvSpqzcvgyWn0LeBgEip1oZHxuPMNJ3Xkb4xSf5_LbTk7PNm4xWmqoK3QpVkkjkFV3WRz2hfysYtPoty1YXg6LMdwzBqnvC6jymMEpotBk572Idx_WrdiF7NrviGkpjpzyRy_4TBjpSyC-7a2k0VfCrHhrVVZuP3Eo4-pTfglnVpIQ5g8-CetvsJ5VkBsm9OukTtbslEL4cQ0RmdxmUiS6CcwPG-TRPMmAEf4oTDXMadUTIHiuird6E4-aNW-NCpT0Rl8XveSHpVOYreEEMBS6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌هفته‌چهارم رقابت های لیگ برتر؛ شش دیدار روز جمعه برگزار میشه، سه دیدار شنبه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/persiana_Soccer/28546" target="_blank">📅 23:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-mJs06mM00Die-srGcuRdMSil056W9BSW1X8n4XJP5tkSLBbiAxvvcnkioXvzgUsYOPTE04WROMHZDD5h37CgVIHxEA8i0fCuFGzm2XWGlmkL0atne7qeeaNlmqMv7ZmNvX5Ob8uGMhVAwH8smQLHuL_bl6mAjLLXuaqcf_YnO-7AGNV5LxY-XrDrBIjwasZxx1E8xgAXK292PIPaXMofJCwbDLv5BdgotcydY3BbX6F9x-7Fs9gl_7v_rCHzxRtwSIOwYRYh1yyquZ52jMgjhiJsGxhI8UrBVOB9m0Tt0M7KVhgdfcr9awlziB27f0Jzc7EZJFbdVs5iKybd27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌پیگیری‌های‌پرشیانا؛‌پاسخ‌فیفا به درخواست باشگاه استقلال برای‌جذب 3 بازیکن آزاد بعد از بسته شدن پنجره نقل و انتقالات تابستانی لیگ برتر منفی بوده و پنجره ابی‌ها درنیم‌فصل رسما بازخواهدشد و این باشگاه مجوز جذب بازیکنان مدنظرش رو داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/28545" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🗓
#تقویم
؛ 3 سال پیش درچنین‌روزی؛ لیونل مسی تو اولین بازیش درلیگ MLS این گلو به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/28544" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myg-FReLAecaJmrpUn8EkyzppJxul4exOAS7QCZhmLP0qPWPj6BA9MfClfAN77gtqu-jVgSb2WASH-V6IxbXtpJ1VM5AdHmJQbab2JX5IKx_6YeLCx5So6VoQ3eo6NUHMOIc8qRpVmcIkVK7_Kv7p-o3VlxdwCS4ld63oEmHnWwoYY9mQmUVUlEDOIDTTt1H53sgmV1sytLyEgfNIkNlyfogbonpzPpLLS8AyQDMfS7aFt4U1F3U31t4dEvN_ZUgMRugGXHRauPVukxs6Kn37bQCpwcCSI6UulfeVcRRy0QVF1PDW9UtSp3W4q-flcrHBuQalNb55et-kEch6OyPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/28543" target="_blank">📅 22:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gJCxRs739SZlH7xtOyjH-fhVBAlGHF4_TFTjLYQUz0hINCrKYCzFkDSHAnvsiQntEB5M1eDhx4icNzBTp1QVvYX25vECzjYy4g3Q4fjSWi0Xqlc--LVcA-zq_lNVDTKRgpk4f1jfevpTxd6cNXXfxQLVvbXNNTejIGGRHl8n4MkEv7WS30DkPAH4x4FvirZVpCcylgcDfix7aFjyfu9WXJoj_cgI4ev3QkyL4uQBtrKBuASI5htwaDZGwGB-L3xNlM7SGIXkgwrUaTg2hc7-lnxXb_pS117UXUQJsMcTILL0ByW40mPH5yNJMCkOhNtBJFH5g6Z-fNO_2ja3r-9ttQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gJCxRs739SZlH7xtOyjH-fhVBAlGHF4_TFTjLYQUz0hINCrKYCzFkDSHAnvsiQntEB5M1eDhx4icNzBTp1QVvYX25vECzjYy4g3Q4fjSWi0Xqlc--LVcA-zq_lNVDTKRgpk4f1jfevpTxd6cNXXfxQLVvbXNNTejIGGRHl8n4MkEv7WS30DkPAH4x4FvirZVpCcylgcDfix7aFjyfu9WXJoj_cgI4ev3QkyL4uQBtrKBuASI5htwaDZGwGB-L3xNlM7SGIXkgwrUaTg2hc7-lnxXb_pS117UXUQJsMcTILL0ByW40mPH5yNJMCkOhNtBJFH5g6Z-fNO_2ja3r-9ttQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانهTRTاسپورت: بعد از جذب لوکاکو، باشگاه فنرباغچه‌بدرخواست اسماعیل کارتال سرمربی ترکیه ای خود خواستارجذب رافائل لیائو شده و قصد داره با آفر سنگین او رو از منچستریونایتد هایجک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/28542" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmRYA1eH35MvMx3mh-8NwOQGkuWmJXNEV8cZjyf2St4Y5KBPf3xNE20GN5tIUqqcV3mPldJ-ZltZvzGBegHgHrIehywDAZKhMdp3Oz9Vss51d3X8ZELjsN3UwXr1YGdYbBOBHI71_sm1khfOqmqWAAgU8k5liLGf75QqMzltTLoCEjwHstcIWD5Yip954mKt3sJFsVhL_p1qj1oSEkUVyjFxj0Gr8cTfDT7CWmZovGIqvOoUyvYcPqthQrZIPm56U5vDv_VR7XSVV0961AoMbsJpv_a-WR1wmgoN9kZTvMcQOOIvwanCybzF7mOT4Pvbu2RAv8i-9tRutWEi9z0UNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
آستون‌ویلا با پرداخت 65 میلیون یورو به چلسی نیکولاس جکسون ستاره‌سنگالی این‌تیم رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/28541" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUV4cRuZb0yKpjHXQFYkfLTnKtqkgUspZPGUasg2TSPlhZfml-gPE4WYCW45Z2Bcqu4rRxIbAzHClqYhs49EfcdTyXMLDhbNB_y26mS4q_3LBCNxGzxZmgJpxn06ZYORhVJdbXV_41kHQqf3GEYkTAJHGGTobK7HOx05kpblgY8HBps4KVxczKRGiEu8wOj7RHZ5ZLlt15iM66_Ij3XMgVeCsDXkp7H5OWE5m0d86gr3Z22lEBwkpkcu6TjxTB5DkAIhFavMFYqDZtLlrXRFYyq4AC5w5pQWnZoVbqseqwZqU2tsACkZJx1e0L8K1vt34s5xVIq8e2kFIm7dL7fHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/28540" target="_blank">📅 21:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l02FQgFFRp58fPQamp_-gzxzkDV_1AMtqikpMYSMUe5fE2xewN6OZyTJj3emkxEa3ROK4NX2K923wPX4yHk6kZVdLeiokP1ntYeHEXY13g6H_YgZJeZvS61IC5dPgwhRfaAKXFfFJAXE8BHcu7gonoW5RGSsetocQ7VhdAmCngYSdFlw8-m7ZOtP85YBZCEtMDwFtjFqe9li5FlO-kRU9lmLppcJ7WvB47-Kdmtf8qMGdtHb8KAerZPex04JU4JIE1QTnXXTVRgvm5bnVm8a0uT68LNnBBTTBTuDxO5PkhJ7Go5D6HPW4CJGgfe2HOyTZ1ZZJPMDCycSvRU118P4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مقایسه‌قیمت‌دیروز و امروز پلی‌استشن 5، آیفون 17 پرومکس و سامسونگ S26 اولترا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/28539" target="_blank">📅 20:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmSVsPABr6lPpmg0zm_1Wz1eV8z4jkF0PDfrQReCn0zZs-NOj9h5yKiP9gRmcJCDaNryMTLT_QT5igYl1QjZyZJ5zir1Z1ZK3OYYUGvuSRcKweSIQSq8zOQuBNDpUG9xfrJFspRd8QuJ-pc1sJoD5XtwpKsywuURDxwDBJa2ZTxHYR2vAPetdM1_7dgbxv9HVfpuQsM9hFudVop7Iu3MBTdt-l6RfzAO1EwEpyNtNRUFje2ePDbREbA5oTj0H2OHqpKEHO35QP3cgJ0x-FT29UFun0CIpvF7g8Nn4w4yML52NdPo-cEPTvqndRx8Ae8PODwQKb_qN_-Shn_9GoVQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/28538" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03aba91807.mp4?token=k28jhiiqlssoqoa1mucgyu6jZKhYZol7WNbrtrP0PqfdmvMoZwu4nDt4Ahcl7oPdXs0I-78jTRtIX-BAUsAhXlJ-uUwb-NbayuielTH-vR5RwBTHmLzWVu3Wmz07rn6x4__QNuY_h1_FGqaql-6ngPwLsxaMGswQdxILERA5G6vVMDApxQvNYyIoPEMbHsljBYFNTwiggHzxTD2omMsg3SCcYxpbXAtaIzQNlrcm84sA8ENwhktqVGW351NGVpd5zFFDC-i049Gjymc_8npD8H-mIZgms2_EGR2HdIjR9-UwIv1ZfndgMfnqHSGKHvMrAjS0nV8DbGiJ-ppfakEleQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03aba91807.mp4?token=k28jhiiqlssoqoa1mucgyu6jZKhYZol7WNbrtrP0PqfdmvMoZwu4nDt4Ahcl7oPdXs0I-78jTRtIX-BAUsAhXlJ-uUwb-NbayuielTH-vR5RwBTHmLzWVu3Wmz07rn6x4__QNuY_h1_FGqaql-6ngPwLsxaMGswQdxILERA5G6vVMDApxQvNYyIoPEMbHsljBYFNTwiggHzxTD2omMsg3SCcYxpbXAtaIzQNlrcm84sA8ENwhktqVGW351NGVpd5zFFDC-i049Gjymc_8npD8H-mIZgms2_EGR2HdIjR9-UwIv1ZfndgMfnqHSGKHvMrAjS0nV8DbGiJ-ppfakEleQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی از سیوهای حبیب فرعباسی دروازه‌بان بی ادعای استقلال در سه هفته ابتدایی لیگ برتر که سه کلین شیت برای آبی‌ها به ارمغان آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/28537" target="_blank">📅 20:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=pQ_vbqOBQypj-tqg-1ug3bdTqdecush-ortLKfqbu0BIZslYHPo18ddoxkGA1CDkLBk5fzOWyOPzrePiJ13pzb6NCK2DcVy6EFtLcExinkXU1e1Vn28zqcaGjy4UdSqHOG6iNLXZC4p-C3rOrW_aYx5Hb3mr64mOCfvbttvwFmxj2arA1GMe3miLyvxE177KxoCiFgjbXFTYd1OgeS8z2c_jMSeHd3-o4Zow4734B_RxTxxE624YTmnHqkdRFEzCuvWL_UMWrV-CjAGCcXRsUn6G94JPiwOSY0f0gbXrYa0WsGnnKpTLum4EKRJvUrwo4EzmaW6e8oHjfM_KWLcAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=pQ_vbqOBQypj-tqg-1ug3bdTqdecush-ortLKfqbu0BIZslYHPo18ddoxkGA1CDkLBk5fzOWyOPzrePiJ13pzb6NCK2DcVy6EFtLcExinkXU1e1Vn28zqcaGjy4UdSqHOG6iNLXZC4p-C3rOrW_aYx5Hb3mr64mOCfvbttvwFmxj2arA1GMe3miLyvxE177KxoCiFgjbXFTYd1OgeS8z2c_jMSeHd3-o4Zow4734B_RxTxxE624YTmnHqkdRFEzCuvWL_UMWrV-CjAGCcXRsUn6G94JPiwOSY0f0gbXrYa0WsGnnKpTLum4EKRJvUrwo4EzmaW6e8oHjfM_KWLcAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد رونمایی از اولین آیفون تاشو با نام اولترا باشیم. اما احتمالاً خبری از مدل استاندارد آیفون ۱۸ تا بهار ۲۰۲۷ نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/28536" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_aOKQRqVglyn6qnaNtDI3BHsVFmNpcudbDpXt-NuYJYMcZ8WoLS7H09vuJMoWFAZU7PMtUrv2zaC0pwYszLAWNYMrhLQ97AaBkFW-smLvXQ7eOtKICdI7mb1y7ZXe0TUGy6hPSnKy3sW7MN4bih4dUNM_dGsQETIpUMlzYtG5c1MKDimJ6mx6zay-LIjA7elcZPYFZ-RvhmPkO8ZDF7A3oJGZmKZYS6EcpHYQwBR3msNR97LW7U8SIIde_3-dfcFqyRs85N7vXxB2llkjscCKCBdNgSgNY4KYhezf5ftcCtNGsFGzgFuvd3BDlGLP4a_GxaeXpDFzzY5HG-I56xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ هکتور فورت ستاره جوان بارسلونا در آستانه عقد قراردادی چهار با دورتموند قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/28535" target="_blank">📅 19:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ou---jP1bEGLeZBa4X6SQD6ld97iRKZEDUgrlWdfFjwZEhte6nKntAX59xCBx4xOBn4EhEo3qrJnMJE8uxE1_kTBrc4RBUvRPdS6mFemjNx2981ORDxP0bRKlzuv4SumvfTa4EoiYG8tK-Ey-BBhZeD8q89T0XtNftLiMovFEWVtqtW3ew8We7rAaK7I8XHdEobSQRsK0ZRlK6lrDmgcddXxDMpKsvxA7VwJcapGSkCNpfwJyduxDRvGjb61UMFLuTzmSXvQJfwf4g0vv5DhBaKdY5Vt4c9czPPjhjZ5smkM9nje4UzFGpWbydYh18a0X93fz8IMT2t7lkRN7Sr2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ou---jP1bEGLeZBa4X6SQD6ld97iRKZEDUgrlWdfFjwZEhte6nKntAX59xCBx4xOBn4EhEo3qrJnMJE8uxE1_kTBrc4RBUvRPdS6mFemjNx2981ORDxP0bRKlzuv4SumvfTa4EoiYG8tK-Ey-BBhZeD8q89T0XtNftLiMovFEWVtqtW3ew8We7rAaK7I8XHdEobSQRsK0ZRlK6lrDmgcddXxDMpKsvxA7VwJcapGSkCNpfwJyduxDRvGjb61UMFLuTzmSXvQJfwf4g0vv5DhBaKdY5Vt4c9czPPjhjZ5smkM9nje4UzFGpWbydYh18a0X93fz8IMT2t7lkRN7Sr2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صحبت‌های جالب عادل درخصوص یکی‌از پیمان کارهای ایرانی استادیوم 105 هزار نفری نیوکمپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28534" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4qqFdrJFsCao6fUG-Lfu0OTBtT-8f7Z-rhFuoDzUOMylIn3xxx50rGTmwcRet8jpFOTSvytx3dnuWNuE6Z2K74XYfHYzuFOCsCb3toh7Jsd7tC4MBLmVxuedo8y8f4o5Ba048nqyJLgAwZk8mG5pGYOwjdOeod6fNUUQPZZN9gU4gOuefU0iSox-4Z0FvmwdjrFI2yh0fmLFtbYCI3AG7f7pnymq1SGnT_fqqv-PaPcTa3nDH9tcWsmbDThBiIRRIcqWJEbnUNpj9FXCBJ5LnTcVXmBvhBaOr_MxfcEfzmLw97ympH4CPCeOI6HzEyQkKi4ENDN1uYlQAO-dlL3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عمق اسکواد بایرن‌مونیخ در‌فصل‌جدید رقابت‌ها؛ این فصل آخرین فصل حضور نویر خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/28533" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLa1tLP_9rF6o9a2pMqB2gRwHG82tIoEWPgIFwhwo098nn4_WOrEj2pdQXPIA6wNeW32vfrfvB8Yw6yWtgjJsHb6bEEx2viXRmLWhVTfrB6RaiGpKPFNPOYxOVKyMsOWGW6sKyQaq0t3WIAZzmPCUUwp4JrxVd8HZYkov8k4i3gS6l3CJBBarAT00QWwdpjPL7gXYC3ItuDZRFQYCtfWMXtDCkkVSTQ-7qKjYro_ayuJRRvXwx2N9_Zmx4KsXm-Zl7tDScVQDa3gzmvHs7-D7jyh_xJFTqv1MSLkxTk4mlOXa4YSGOlse_TDw7ngI1N-LGB2YWRsKgbrv63dd_UxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پلی آف لیگ قهرمانان اروپا
🇫🇷
لیون
🆚
فنرباغچه
🇹🇷
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/28532" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSkzQQYTCdoqPOchKV0DhBo8nlhqCizIYQDdSHQF9zWDyEwjSULacmrooYyOMiFi0hUgMeHA9nCnK4feXAcJcklyKdcJuzHsnuLP5M_LppHGcF5jfqnQjBNwmFJdbwQhrDeB7_04cjD1aAX77laD92bkdjO_GeGeamhNuwWeFrw5nXK0OruwgGtZbT7Z_x4cNUSB0BQLIFx_Wvr1sP6dASIGv3_BQ11OunEMpm8x3kuzJbLI7ERlVqtXE2CIHZR6Bd8axBna5NbSPBhESA_qh8oT9UW8BGggka8wRg7o2rTftjs8Fs8imY7WzUcxUwTOA-iRFuSTPYT6E7yUMygCZIaj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSkzQQYTCdoqPOchKV0DhBo8nlhqCizIYQDdSHQF9zWDyEwjSULacmrooYyOMiFi0hUgMeHA9nCnK4feXAcJcklyKdcJuzHsnuLP5M_LppHGcF5jfqnQjBNwmFJdbwQhrDeB7_04cjD1aAX77laD92bkdjO_GeGeamhNuwWeFrw5nXK0OruwgGtZbT7Z_x4cNUSB0BQLIFx_Wvr1sP6dASIGv3_BQ11OunEMpm8x3kuzJbLI7ERlVqtXE2CIHZR6Bd8axBna5NbSPBhESA_qh8oT9UW8BGggka8wRg7o2rTftjs8Fs8imY7WzUcxUwTOA-iRFuSTPYT6E7yUMygCZIaj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/28531" target="_blank">📅 17:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7ABhuDYJDP1yAUhOcwFYZhbnXdFwX-GBP8oVT-imkZs_34P04gS0rHEYAHpC7l8XaO3Frer5z0X0wafH3bsdePt8pZcVlzBBo5DXYbmtTMDPiz4R3vXfoz57yWxnu17aqTIyE50JqUcbfxoQKX9M69SYEfemqeyTUVFBi5vVntSdTDFaAtiI67uMTy7qpWig0OnKV5FZlt-D9k9cjFe2h_a0X_8cvOTiyhhJw4PqlgDvHk5T7ChMdXs369enfL1X_p5NIhmp7JOb-EJyvirMtVRdYeD_8QWvqmNNhhYomCZieVndqXw6FpmZ9IpmJwMqAyLPMLCORnqelegQmi88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28530" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=lLbbdA1yQ4-tJqFLdNycbump89GA_lz8nI5ZWvHDzdzXmkHQqkFta8DGj8Ib3znZvI-F8IhrcIXHsiBV4hsY7DRSdA8riO7oTaSD-F8QLjGIkMRVRGhGQ80yug_BqRUefFtG0LYHEul19R5oH0YYby6Eo4_W1iDiCMMZmTLJICAuggZWBILjoYTVd-ayyYQTrtYJ8sMFeyapkBt-mEV1O0Zi5QyZXIftoirtNN3ATeH5vrBc074B8nKaD81ilyTMe71EfCUuMDFWh9fuvPm725sC9_gFbWzVIF3ygHGY9VfjSl0UQdAZJFXnZjxjaDQjr4QFLr0VaqpKe3K_he7IQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=lLbbdA1yQ4-tJqFLdNycbump89GA_lz8nI5ZWvHDzdzXmkHQqkFta8DGj8Ib3znZvI-F8IhrcIXHsiBV4hsY7DRSdA8riO7oTaSD-F8QLjGIkMRVRGhGQ80yug_BqRUefFtG0LYHEul19R5oH0YYby6Eo4_W1iDiCMMZmTLJICAuggZWBILjoYTVd-ayyYQTrtYJ8sMFeyapkBt-mEV1O0Zi5QyZXIftoirtNN3ATeH5vrBc074B8nKaD81ilyTMe71EfCUuMDFWh9fuvPm725sC9_gFbWzVIF3ygHGY9VfjSl0UQdAZJFXnZjxjaDQjr4QFLr0VaqpKe3K_he7IQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28529" target="_blank">📅 16:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQngA9d8Hcnoc-fzENA_LtcDxjs2EPfpCAhTJEcuqUcpeHRjquKj3UiosdzuKCc9xNTupvBFnedQDTRpRiqccuPGgUndXL6qHaL3mA-k806mhI3DPIKaXz11PWBNq4_57Pdls9ueSkFLUFPyLREajAElEoKE41eugLTx_ujdF5OnWEdHBlBY8mrmzOSBVoYlyq86e_OC0rW1DrDhiqyCmQuvpA1ICJXFftgdHvL8qhFCKDuSQqMVL2QMXQA-bVfkUmEjYHKNeL0ABtkoBMbAUp2Dux_emB_LqA1v8yZ_earYBERZWaljYlpOM0WxgtqXHSHlFNFwuG7Y9rQt4dKhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌روزپیش‌گفتیم‌باشگاه‌خیبر قصد داره که ابوذر صفر زاده مدافع‌چپ‌جدید این‌تیم‌رو به شکل معاوضه با حسین ابرقویی‌به‌پرسپولیس بده که همون رسانه‌ای که خیلی‌ادعاش‌میشه که از همه چی باشگاه خبر داره تکذیب کرد و گفت اصلامدنظر مهدی تارتار نیست الان زده تارتار گفته…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28528" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWibeUhgeDsjs_N9EZH8BRvHxt8K45RS0tGRoyxWJ4Fsd6e_keoW32V6P6bn_gE4rvJQ934A2ncI1a6t8b6s5cjaOFhXCRr_YmyGhf50yekiyrzmhpVxAN2UCeacsb8_knc3XYGXstfavbqjyEedPJ7M8u_xsgcAF3sf9Ckwbv_MpmBWnXE_WGYWSJBVJAAQ5OsTbjlM5OrXqKR3T-irfuzxvJ1HwpKCNp--z3FmHr9GkuurmfKE6SNZbfJ1H7mg3O2LrD3vaCv-lHEVx2ONCYCZqMIiisHM8M3jvBJyUAlFuYHktkxxk3SE6gFerqcDJVdILd3nlgeCWL3usLnmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28527" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhtl2nOFMkMnGtRB66siXdc8zamk7Cl0H-qO7A_KqJb-nPicql0CB7wWFe-TuoiD6jB0hC_DpLfMVNkK6vD6xxC-vRFcpgqhiiHQwIq4R7rg0WUItajx1p7H0jvz4dmUSEB9vhNUMwIB3iLf7ZgXIfoY-y5JdjkKIFKpX9drZM3FwEe15cyJp4DTJzqVLCWhvUQQ-0uPdQJOuEvuC5NQUL37G2yOf94LJ-hYbkHQiZucvOYbEJBSjKsiQF1uUP88p37wnhfGCF7hEEd_eUySbLNI2ReWUFMPQ1GDODQLDqvpg_y26pmfCgRDCtyFNRH-rZ6RezP6UtItSy2wflGq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل شده. زنده باد مادرید!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28526" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDMSZhXqv4csaECS0RGzk0-kVgIozwKIJnoKxU6hrKYRdWLvZ3Xv6bwJ_tXUfOxQi6gJblV9DRqI93TNnY_eKFQBgYoejANdy8Z9FC1UBjE5tzQOsZ0k7a4wmfqYA1zbSKT_I49sEL-xK-HveRevS9WFwmb4Tc45yeNazm00VsEoTvpN--Ym6IaDZy_LQibNy5hl3buPJZvowdz3nnAmfmwK3DWANqwZFLQrsHgBs9NIbepgQMNfT4mtgz0zUx_xJM5y4qtlho2m69HeVtN2JhPtky8J-Mj8yRPefL100TTEbUmYt2plvvRRplsotXLZlqewOTwhXzQfNjuCNUalZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛نیمار اندرز مدافع‌راست‌سابق لگانس که اخیرا با قراردادی 5 ساله‌به‌استقلال پیوست بعد از توافق بین دو تیم باقراردادی قرضی شس ماه به اس. خوزستان پیوست و نیم‌فصل به‌جمع‌آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28525" target="_blank">📅 15:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=n5I0PIxC4SmTzyduawhy2ljSfOA8Z6K8XuOVU-pr8ImNfQsLq08DR4DFNEhwN4EplYlSqDVxLl_PLhtJB87QaJAfEM16gFZcGIVcu8rFkxCA1zGL-wjiPdLLELv6z81mX5ZBr45uQPul3qJt53eVY24kDq7BpD_YoNW9A5Am14dls-uwpsoJKdKwJWDYuvEW3ZcYgaDg0xgSoYrMKerghm5ZqrRdOWCmhBN2X_KpF57uxiZIz87Tly6MgdiggsVXTvSGarS-in2kUA2vTb1TRn1nReKlb46Wrx0ukoIcWKb2hOq7nT2g2lMHoXgVWSmqLhie4A5kF6qitJQyufKXnp6aiKUiQje3yJNscaqzH1ENHJlXLpA0x_jOdFxLIUoQh4KTiZ7nmUjUCj49lA2-9zEp0ytR2pNrdANqHjF6N0lBbjuyk2hlQC9ybhBXHJAjQOjIbHyIkBjwSHD7CHv0Km19LPLhQtVKyibku2ct4VpYIkuswv_j2apDI3JxAUquLWtMeHvMcbUGgGWxFYAtEl9BI0C-5CDRPc3beK9AQUl00k1JrP2-afuD9Kxbw-NSjlfPb8Wmzrn-GqJbNoVrdFaQzTXaFNjHeVSIc-bIg6P1WWKM0r-fHG9OqMy2_JtvbQxD5pv9_Q3_7t2OR1WWI7MHXK4_GgExSIFZfpwvSn8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=n5I0PIxC4SmTzyduawhy2ljSfOA8Z6K8XuOVU-pr8ImNfQsLq08DR4DFNEhwN4EplYlSqDVxLl_PLhtJB87QaJAfEM16gFZcGIVcu8rFkxCA1zGL-wjiPdLLELv6z81mX5ZBr45uQPul3qJt53eVY24kDq7BpD_YoNW9A5Am14dls-uwpsoJKdKwJWDYuvEW3ZcYgaDg0xgSoYrMKerghm5ZqrRdOWCmhBN2X_KpF57uxiZIz87Tly6MgdiggsVXTvSGarS-in2kUA2vTb1TRn1nReKlb46Wrx0ukoIcWKb2hOq7nT2g2lMHoXgVWSmqLhie4A5kF6qitJQyufKXnp6aiKUiQje3yJNscaqzH1ENHJlXLpA0x_jOdFxLIUoQh4KTiZ7nmUjUCj49lA2-9zEp0ytR2pNrdANqHjF6N0lBbjuyk2hlQC9ybhBXHJAjQOjIbHyIkBjwSHD7CHv0Km19LPLhQtVKyibku2ct4VpYIkuswv_j2apDI3JxAUquLWtMeHvMcbUGgGWxFYAtEl9BI0C-5CDRPc3beK9AQUl00k1JrP2-afuD9Kxbw-NSjlfPb8Wmzrn-GqJbNoVrdFaQzTXaFNjHeVSIc-bIg6P1WWKM0r-fHG9OqMy2_JtvbQxD5pv9_Q3_7t2OR1WWI7MHXK4_GgExSIFZfpwvSn8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
صحبت‌های محمدنوری سرمربی صنعت نفت خطاب به بازیکنان در رختکن به سبک نقی معمولی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28524" target="_blank">📅 15:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28522">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUpdZTADbNCgdb6qvd3TD0Xwu9oawFYpA9cHZGYlMQYJsaOacqLYzcEbE2DbWd3TEXGJs6SPdscS8YW9a5iown4eV6WguVhCLqI2P6t2-aaXDKw6qN9LGx5JBlKhKkb7VNdrLagE4GCalbtR15j0SXldrOXcWUK3mAfufrrJQ7x8Cl5t2M5ehThnn-wPaT8swl0kZycG7Q-sJgRrVoj15GCIhw6aR5SchDiXmrb0m9Mk3fML5Yx3K0S53TgjhX7nsGqwV1M5WPfo2yzmtsYR3MHw1IGXu9aiPUOUnvbvtNqKB7bMqRBtQqGAbU9hYAruKu_oiPskYukUJzy9Sj66Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaHkp0q2ZpwPPIurcgvOvTUc8bEKS20fDwBBxv5HdYiA3vAgDQvX22duREQYIgzCCfL6EvXK52sonYgGRkj2KEqsvTjil5oIsKV_gv7perGKfnXVlnXpyziELnQNqS6bItXr7fbK2KprnXrL867RTYF4uv0FlFtotUEIyAJbErUkmqUlmBc_4fYRlIoREtWXkoRzBCt_yXvmQvEx1REZu21BFTQsfwTKb-e-o7k3aLGddYlDjUBAysbswGev1Pw_owzc5U1jBsVEXvQAd4nOEak2nPcW9PDiB8CP8lb8s0ZkzDB165RuMjsjOPhspGPo37gTnmRzYJMFU1OfFZCFkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28522" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOzANpcasWpaDtG07eMpwY0QQbiXkczGsNXXCEY2aHAK5rwYWyQr_BsuQYo0SGqCXS6onmPSkK-dYdktXSr_NXUSAGOaO5x8oAd9Td-Vc_mlDQ3DffjOqBUXU0WYfWz27gp8LlZuxkxcEY5FVkFkEfz8ayyqTLwATEAuVIdxAwXQEevXlgxfuknFc9QdqMMe24KoV9NdvbyjcT_if_pLA1e9DrxSYW7XBDkrhINM68yNRDVADflos6KdRAgmpRSOdLvu8H5VnK95GIX4xDzXUjh7roo6jReBzY0Lqn1punff7sw7j0_vdqktt6DV2Dj4LPFWAnWbFBsSupoq5bRfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8oTVhY6uLsn-HVeLuHRZA61VbUTC_4I02wYP4LE8S2TqXZ-o0rNeGBDED_cI6MfIzQn7xgBmSVVDFppze2WxYI_m_bGM6WPAhEVavnBZSEK6EZIghHwN8MxlXbCsCfT6MV2Q59ir1Hw2uL-0DkcWVgnKYbcdT01IBQ37j_THUrbEHCxIyc3QNIXR5L5UxKvrNJAzOvkgB6h_gZJKOnIbdBCTvfZbFYxzHAWLQ1OKN83Kz_MJdK7OiG2kOY6wyVmvZyov8FwCfSYpc2GQyUvnsvPfLU3tuw10QxiT7fALM4JP7qAkvvFdGtwvdYmTwbn9o8u0Z1YoGIA2Y2uajkqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTqvw8m0_mpT1dSX8YNQM2lTFAy6GEHHI_f3qmyB1oJxPFpyygW0-LS_QfvmmRYeDKjCxvuYuIwrETtR71gsqMERgeoTKb-UndQVUgxAu8iQBw4U3TJn45_zmxkNaSMeHeGRijCYHjB1DZFvnOW55MKmE9GitdmUoC-FHxNsFLbNjSKbOUqLd50-WKCd7JE4Ti2WR2Xss64IW_4OeA6fKw1zmBIYbu2eUcE3aAox6pfusyDvWLdQLZ8FCkh2UC9rmk_LF1pFqcJbAx5PokLFuK5WLrK44wWeBuAaiGYBHzOAXZfQrUIftAkMqWCKGhDDFrTQJQjH0kN2XDoXfr20Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSiQ3rEwatCE1nGxHOzkYZYOvrvHjIulvArJvsreg9K24jjQUBElEICILBcx7UIXHsGQTFA79b0Si8APVvLLCG-KCrSAL6f9FcFSDo74Pu4I8Fkt8jszHGnymj5JvNj8HIiighmZNd9BbLE1v8ZodT1UJSLMsEKupIvG8Bnq1AZbDHRbWbCBXUM3SLk2pADSD6QeNeGxNg42U5dRjw_Xe0-d0IzrJhSvJeGdM-SkGaiuTC9sE0tacFgVKik_JkPKRIlr2EZXgIrG7rLEl_H-0q3UuoQh5v-50TU0DZ9Y3hA69XPFth-VoZLIKtBsJTbg9_ePCxItjtWww9Bi0syUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=YHcdiwNuUluOnsJtpcEtLk6-smcPHfSytAtEAEg_FAnOM72GyL4MHWh6AG0y3ojovhtSKGDLwBj9R6Byz7bX5UKxKAZHy88LRhEXF8avERCNQq1xAUA9yO11eFVUfKSwyxqp919ewgs84PV0mVe1ySHK27Hfe1coo_n0NAyhGDXJfOAxoxKXu6XSlEUbJ5HM1RdObQLuoHo7p6Qve1v9sPNdRGFJt8Wv3JxRzmdX0SUmWzay3-n7TMHi4cbBA4EKyFIkbeyV54NCjix-l4hW50mwREvSD9taeJVjLUYHZoZbFRGC3s0hyEFdZWp_HVJN7Qp7b9QVcbEEc1mTLpUgzilGoMexelqb-d5HxquFxcKL2z6NR8tRpkx9ub0xX_DSGSx_clCWeAQliv-t5SeTSIceDQNB8k3G8apmcEAHpHkOZaFsaBMaYz4lplDiPH3OvWMESu_LwLx9ADockprtXjgwxwmVDni_cWarFOhU4rXjzmM3J_bP2qm2-_9BnKH_PBrrYefDHr5oERHsGTxjGhB02dGg7B4QQ2txoAH_XXA9opPLwAEjx0tGU7GFMFgATt3SMvhz8LBeMxJoqE3cRJYwZ5pMG0VG3mujb0OgVysS9MHjJwT0AcybdA4a6prQFUuC_yZnxT0hNjJwB500VncC8_8HQCIEIM1hJKpqL20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=YHcdiwNuUluOnsJtpcEtLk6-smcPHfSytAtEAEg_FAnOM72GyL4MHWh6AG0y3ojovhtSKGDLwBj9R6Byz7bX5UKxKAZHy88LRhEXF8avERCNQq1xAUA9yO11eFVUfKSwyxqp919ewgs84PV0mVe1ySHK27Hfe1coo_n0NAyhGDXJfOAxoxKXu6XSlEUbJ5HM1RdObQLuoHo7p6Qve1v9sPNdRGFJt8Wv3JxRzmdX0SUmWzay3-n7TMHi4cbBA4EKyFIkbeyV54NCjix-l4hW50mwREvSD9taeJVjLUYHZoZbFRGC3s0hyEFdZWp_HVJN7Qp7b9QVcbEEc1mTLpUgzilGoMexelqb-d5HxquFxcKL2z6NR8tRpkx9ub0xX_DSGSx_clCWeAQliv-t5SeTSIceDQNB8k3G8apmcEAHpHkOZaFsaBMaYz4lplDiPH3OvWMESu_LwLx9ADockprtXjgwxwmVDni_cWarFOhU4rXjzmM3J_bP2qm2-_9BnKH_PBrrYefDHr5oERHsGTxjGhB02dGg7B4QQ2txoAH_XXA9opPLwAEjx0tGU7GFMFgATt3SMvhz8LBeMxJoqE3cRJYwZ5pMG0VG3mujb0OgVysS9MHjJwT0AcybdA4a6prQFUuC_yZnxT0hNjJwB500VncC8_8HQCIEIM1hJKpqL20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تقلید فوق العاده صدای گزارشگرهای فوتبال ایران همراه با نظر خود گزارشگرها درباره تقلید صداشون. جفت ویدیوها عالین حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLv0ZJL05F6gxH5HV1Cj1JGbBNB7zoRZ7lSPQejQ84vnyOqfkrn9WdlaKZTdvJxpci74qRSjHo47KTTZw0KpXwhiLWBz7C_D2J8hChAq7MbwpvfjNjew7PoVULNuHO01ikirx2GvGga2DKOGIXTn2HzdU3fDIHLiS7zMEfiVvjZNqInY7DE-1fiC3ISDvuJpgy0PdE70cik5r7FfLlheSyhJatZ5Uu8stIeZY95nwqqKC5XuxHTCyV6C9fwMraVGTvkfcZdRjG2CAegXWg_TPZZ8aiUmvNzZX3pxe7wsEmXE3aPxmYdGuLdcI_KmpU8agQJgOQLGOyphrGHeB4zpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28514">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLamjnhyljdFRFYQ2Dmy5DFzKBr-1iPGsc96lBtx6TLPHGU2uR1ZsdWLEN0jdBxwpiG8fgzfqyHdVfjM8P67z_P6ggCNruOQzs23b4nSOGSZ6zfOKjehr9Vt-hCoGdncx2vNZC4rko8TqvrjxaJ9MZqEkYQiv5pwVc5fEC-OtHZlfsBYL5L_K59wa1ahTuFxWN3ZIVwvKHLjbBQMcly5gXEm5szGwIiSxUqRNdpk6LqSqOCFG3bM4ZPfxetkKfHCAI0c2S1dl-_5n4Hcob5IwCLxemea9aoTC5uvCT8f7N_a6zU3h3v15FG1OdLKj24E7Uovs1ev5bH5L9keltbtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28514" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o29H2HI29GgM0P7rfBiOaSCSZ4_eu59mklRMzmV7VZUSuO-a9fzeRXxe65rKM6GHGXu_adx-8sjeoHe5MhVMTNgeRBdtx3ue4AEcnIBquktDbwt_ytu76x-uwbZuXar7MwL2xgMwAbunrH-CYRFBbWYloRjGInZoYAPq4921QVUH0dGelkXkj5Ii7xlNkB3D85fHjVOdobCLGPIrdKwIxyrtCQxIlsfynCiCzwkBfh50o2v-0IGFDSfIW-NjzOHbQ46e9Useo_KZyOQFh9uAMiboLfQQus_JeMi9YPrD-8upjMZSa4xsMX-s7jSjQG40FnO_CtDuyRcLiPuqBsGe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28510">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi1tFuY05nnL_I9PHGOeP4dUSjMPAesYpnwCKAtA-277gnP8kSi9RduFdmlOYUgMrDDHEdTzGRgpYgQGzD6r7JOwZddRZfcV0AjXU1taA8-8Ev_nth4xLiPT5EggeKeRhOBz0s0kjx8zAC941KXL7HRKxkxs95aPs8z28xFKwa7YKr1SKme0HS5q7imcsD2JPVkWm1-be6V5xnkjC7b3d0lG6WAooy2n4LS3sU7Ttv0q19NVB3Or8C23TwkgY_7NM9bPbuiaAG9X7gGhEVesWGBXzdzC1fywbDl63iwHsmEfJHnmMdFJ647OpgYfYcl8XOBZd5CWPJlxmi1TMaVLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28510" target="_blank">📅 12:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBU5TEn6Qe80cAEkVyF7HdfldDIh7Nsms7dcdE852TI3UGUO0EsIrgttevzKOsqnibo2HlRRtHoghDNEsHtqHVVDpCxoscYF7oipaOIcK7Bvdx1aJG7uKNdijtnPAPTksvLbRmNb8mpGNnHbEWwHK1-dX5Ye5REfMkofXHiWK-ywxYSvJxF9246np2CUMRK7sT0lEkcbou38qAl1am4Buik8-QcqcoCrKXQ9DRsy9epmdAltJa3D48bO1_Y9X6P7xTGSc_wZJ57At-s7RsD0610T088d88eEped56uKJWkQAJeP6AmwYNL5wGjMQCZhy3UJiOZuH-7F665XA1qJcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28509" target="_blank">📅 12:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGz-JuqRUVxWXWN3lSfgxxEU7ZNHo03YmTqlxUaH47Bbipgaj9FB7VFzcIR6GY71tGHUxaqXla4eStS4BL-GQ3gI6ZVLe5k-EcVMp1Vy67dvs02aE-ZiiJF5X28kdWhVMYwkHGfWCD_RdX00rtZwrfz3MsiM7XGbNlVthCGQIpRJfv1gt_5qCT-DV5RdVhG6Bu0eUBybFEqcqtwUhAE-GuBJ_4RwlThTuiD6pJPtVZjEsHOFFjY5cyAXt3IzrMocjPUsWLC4U-rObtRalxGToPX10D32tySsYIguVZ3wLL1z3C65OiPTWi1AgjA8H5Rypt7xUzvPxEfVW2-v_EcLIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار کوپه:
آدمای داخل باشگاه میگن که تو خیلی ریلکس و آروم هستی. مورینیو: عه؟ پس تو یه منبع داخل باشگاه داری. خوب شد که بهم گفتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28508" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=gHcl8j2kHO7m2kiMm9rP-a5nwpHTh3fH7F-FMwvYiLJQXeHSjMdTZ7RrzgvnCfIMbt6Zj_QXZH7F79l_JZBg2qZNl3kOIaYOmpkNcuLrhlcZg36lJ33-7VJa4gbfvZeIduNcw94msaMkWSuLjpIbTC4Pe6f7qo6Bh1Gav8E-IfWpIaZH2cRrvCBqDGKI6Gl5508-ViHoo4t_kxxdIC7WUxMwiE3qVRzs3-QnTlOpr_tKh3R7rapMi17jnsfuWKdRRC6QVjAxxtCjJj4CrW7jneKJDPeGiouSy_JI1gjLUrBwasGFocYrAY8A1B2l0TRNKlQ57iHjWRsEHE6LIDjSrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=gHcl8j2kHO7m2kiMm9rP-a5nwpHTh3fH7F-FMwvYiLJQXeHSjMdTZ7RrzgvnCfIMbt6Zj_QXZH7F79l_JZBg2qZNl3kOIaYOmpkNcuLrhlcZg36lJ33-7VJa4gbfvZeIduNcw94msaMkWSuLjpIbTC4Pe6f7qo6Bh1Gav8E-IfWpIaZH2cRrvCBqDGKI6Gl5508-ViHoo4t_kxxdIC7WUxMwiE3qVRzs3-QnTlOpr_tKh3R7rapMi17jnsfuWKdRRC6QVjAxxtCjJj4CrW7jneKJDPeGiouSy_JI1gjLUrBwasGFocYrAY8A1B2l0TRNKlQ57iHjWRsEHE6LIDjSrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
گل‌های دیدار فوق‌العاده تماشایی و مهیج امشب دو‌تیم چلسی
🆚
فولام درهفته‌اول لیگ برتر انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28507" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-mMkNxyse1oouyD1PaOxJUJd24-ZBtlrE9WsQZ9dqpxehn7fVjq3ccDhkpos0LIQhHxS5NttOSFPfN5VehmxycDPJrry95dlyLCWD9-vrPvdDgOXO1YRQsWvp-M2M4ErCV77HeU6BedSElSLVD82-GAeUlokNe_HjEc_Uwf7nrcU_9VRcPRW85zsigOfEyIRkobW9MjSrXoxbJnTbBgEwTExjpKFo1jgYOO-x_9wCcilb_wTsD9_3IrzON-BTbIb8zFSuSFd_MRmSyQXDxZhr5jpT65R32nR94BjE-npNrd75MksGX30lLxurqEVFKItNJYdvJSrd2AbVfovPKYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28506" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLNrgkQoDF5bQ34XVVWZnQUhl_uUFyn7tPwSQ-CK6iFvYs_NJGmiDTJ3i3SopwXofHOj38X1xWngmXSiyAQdfYItKXa7X28_N2CkwFCiey4Zbrg3TWj0vsdHYr_AOvYRgem4oljCEJlgwGo-Bi_9knlJIyYSAt8PIK7b6cCp3-mnt4CU-ZMR30Sd82faIC0AO9iRy-UYeJ3lmVFXgRdG9vbus8mMKeSapYoYGObA18V5iH0lP1VbGdv964xs47xbVSB1BtFEMt81CDhPZQ8IK8WZTKyT_Ug7-TMo_wGulnu7R8ReHGYTBLxZ-_2TPZKExdwEjwwN-ABvK59cTVPCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فکت؛درصورت‌پیروزی‌استقلال دربازی روز جمعه مقابل فولاد در اهواز؛ سهراب بختیاری زاده به تنهاسرمربی‌تاریخ‌استقلال تبدیل خواهد شد که فصل جدید لیگ برتر رو با چهار پیروزی پیاپی آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28505" target="_blank">📅 10:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtibm8SaIU1fMMxiYWx1fLP9gVkIj6D_xIitu8KRdsSMBnCilgwpcE3DtWPjcOdgCx2fKId0dxFR14wm0XW9e9GIT_r7yRR8k1CrhTHFJMcd285mM7yHKFYkozvOlx0rPqzi9eNtXpWw5sUwXkFeJ5Bnz76xxcJ1hFbbVKOuyTqsUwmMltQW46OywG2CQyrlf3L5ldy_GGXw34Rh_kDJG_a_ftyAxrBjTVVHoLDEulfgbZPExwONIE4X79mvdBqFp1VCXco0OMv3HrUzMw_k4pkStnT2sEZHbAvVzRadpoqyKCdw2FUFUoZIpCmnp4mj6u96zA9WndPW_nRU7gByQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌چهارم رقابت‌های لیگ برتر که روزهای جمعه و شنبه پیش برگزار میشوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28504" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK9qoLumiXGP5QdW0mvQwrc5ySwaobZBdFdsmpc7a1AKsNtOUE3eiGYHqgq8pC1B4-MHTsAd2zTBStRqY0K9JX13PPYztX8umopQdAqlBnj9LZCOGyPpBKDl3olFpWS1CuKMdgKBUMjX-o_OboeAvCXSlVynU2m7_vEsRf6mOGBml6m1LQp3kA51kQMbWX7iEbbrJg5espz_gV35hLDsRsS9tH5JYEgMNHC6dqchJ8TemDNMmr-Yqn710ov-KNh6pW5Pnnym_nq-kdw12ixtwdR3D4fGtZE9vjB0m4ckleKrCtk7ctgaxxiINKLnbSMwiTPCSSRmUIdrYxt0KeROBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوانگی‌مطلق‌درسوپرلیگ‌بلژیک؛
رویال آنتورپ با نتیجه ۴-۱ مقابل خنک شکست خورده بود و تنها ۱۰ دقیقه تا پایان بازی باقی مانده بود، اما در اتفاقی باورنکردنی‌توانست‌بازی را برگرداند و به تساوی ۴-۴ برسد. سه گل در تنها هشت دقیقه برای‌رقم‌زدن یکی از باورنکردنی‌ترین بازگشت‌های‌فوتبال درفصل جدید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28503" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0UDle85qkdy9mCmvztQSVtuUgGKqmvlZdjJC6NlT1f7ZBfZMa8H2kRaFqovGpshuKXwiqRcCrRbkRBqjD-tj2Wlh7xyuDjRgu8RXJZIGUncLkC76Z_0OVGNtoVwGl5bXlrN_kk3CZZ25QzBky8-m9D_wg1zuVWgbnTsAsLPgj_rrCJVPQQwtmOG4zGlxLKx8JLOAOqBOfitwRaLTiC1K2UZk0ARCTdPeCbmLzQw-D4pqUrEbR48ZCwFg47IMlr0zFboK5UDTBON3W18S9aKg72TJHVX7nG8iue74ouhHvEI9DwMXm1VeJRZ8vCXz1mDix_Al04uaIpLXBWpiDj9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت‌تیم‌های‌حاضر درلیگ‌برتر فصل 1405/06
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28502" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwTGlDUntWDXXype3Vsi7LegZwhKcg2RdOdT9j4TKxw6fwKQv4hK25dv1PIZ4IL1UghPAd8ZdyYwZ-xsg37v4mkUbODL3DSOudBVkiyxnuAHWi9kCiLrqrTKGOsLktZ8CHnZLm1Wo7MLLM4zTGSdLfocQtQ9OpvEPlofGRILZz87ASijhCkPsWwXxXKDgC7Pc9H44syY33aBBmf3PhzNJ490sm0dFNm83eTyqif4COVTmzU304ZzM9NCE8q-WcZcoqN5GkxWwAQRZuHSXf2S1dxOFUbWPVJzlwJezlzZUk3NtlpVlH2aoD2bCYtikeTnSz93z28E-5Cge-WFPtZNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVCLYsSIur27S8xQ1cajbIX0Nw0o0mPgexdg01rj3TbZStFrIefi-gFdT-HIP6EAgqCVskEO0hvcwnMq6BUbwUpo9azOLOjgBJ0wloSay1UO77HJnYD6vg5T2fsJtf4td5Ub-vOtHMYSJgppTE8cvMKfjdm_BWR38ggl8YYTPaxctp2GXQt2MtaWod2dv5GbEf5cPO98oe8NztwheCVwWcB_eMrPSnkfxwqIXKdg6z7wGWQt9PMlKbgDBPH7jE4zbwsk-mhLnunB6VsaZ74J7PQ-BPQpU-St9iye1CdNdcgb43wWQdp-i8VQAFYWakHhI4cJexr9OGPtXlYv2IlHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn4Cz7pCANg76ayc2R5JnC-hExskle0aHzH7cbU89hZtJUMojie3BlZ0mwySPbfFksDZ43bOjZMVb0q5eQURHNgfJdWIPgr2uI75VO-Obsv5-3z6uDXsdA0sdYy0Jc-M2Y3tyuUQv8omB67orfvfORpEPtpSr0I1uHoT-s1XyxTXhLabubbhCj5kDowB6QkYdZFlhjZX_kUcm2KR2iLn8K1mdDq8HX2Hww0kp7juu_ZGYKU1-D7svfMR1XRyuTGZTns-7FMRZgX2MVyoI2Y9QkyB_I_mn1DyCDi8lJd1xRtuGm2ifFmZJBMONrxiw_v0tZ3XEQYYUhQgae8QvSx62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAwl_AEL3mzmy7A69V4Jl0IDWUNux1Qi_CbESZL-R2yQLV-4gdGrU5eDR7j5_me7LtX991fNBTMJdbRf_3aqwW3WDufOp1D8haCYP2iiFX5r-xozvvtxh5d611GOHNgyBq0ph3s7xU8-HWINkJou9Fz01aZzTJwC6WOSIn7uej64niWBtTxdbjYKlZBJejRgFhb2R9if0dL9XTPQC_1in-rO6SEf0wdTcWzrB1tJaG1gJSIMHU7yesY4CRM3hvjnOukYvKEgOWGVO5CV590ddZllYOrxmWNotPNFtD7tFnVFbnvYgAFCMzvufQTXfLwvLa4b0Gbf9xqFEsufLihGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=jkLzGvrXdBDyB784HqC69pkTBbPZ53TqwdoOt92fZOXMpdBX_2GidXSY3xj2L081NfrNsfmdrGD52121qKMhd3Ds1PSOEi60Iv-BryWA4ZALwj0_Stt-6qCpcC1OKN8qGKmySoxGP8QuJLpJLXxAkFXYQmqLHUY0M5nG7liuw2IWDh3ovw0QMas2ILNvdYt88re_FgH5wEriwN1XszaThlQhrVUSm21dNCzSZjyU9zC_f95spYebZjLCl1VI77K1NhEQZerE7cZiByHrK5FaDKwZtIHCKI1ivqzcLXD2W0L03fRLXhJhozZDChu5tYT0T5Y6DSgXZEFNtZ2_I1WQrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=jkLzGvrXdBDyB784HqC69pkTBbPZ53TqwdoOt92fZOXMpdBX_2GidXSY3xj2L081NfrNsfmdrGD52121qKMhd3Ds1PSOEi60Iv-BryWA4ZALwj0_Stt-6qCpcC1OKN8qGKmySoxGP8QuJLpJLXxAkFXYQmqLHUY0M5nG7liuw2IWDh3ovw0QMas2ILNvdYt88re_FgH5wEriwN1XszaThlQhrVUSm21dNCzSZjyU9zC_f95spYebZjLCl1VI77K1NhEQZerE7cZiByHrK5FaDKwZtIHCKI1ivqzcLXD2W0L03fRLXhJhozZDChu5tYT0T5Y6DSgXZEFNtZ2_I1WQrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=Fz-Qt-srgIKi5G7U-1MZGP-WUw-nrXEbualo2hU_H_arkudq8H_hQ7dJk5FUo-NMzRqrMIc9c9ZcMHHVXSoZ-QFgiiRbRfAvC_fs6Iv7yMs5nX0VR5LbKE1JBFACKw1O-ofI96OT12HpIbxid_IXHrbBD3m4Hw4BSQ4BjSGiJvdpgImAREray2LM2skW-36IwYZpObD4ZgimF5jrG7xXLXYXlDsdG-Jz_lRemhK2fU_rjZFQIm5zOsvqbL5CVis1GGrBJ-Jcv4KGgrVw9Xv6MC0zZSPnoShK2tyRV0c1PYy1GYwUEK8btu155ZqfqT5Fdg2z8sPwNKVXX0KYZqPZcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=Fz-Qt-srgIKi5G7U-1MZGP-WUw-nrXEbualo2hU_H_arkudq8H_hQ7dJk5FUo-NMzRqrMIc9c9ZcMHHVXSoZ-QFgiiRbRfAvC_fs6Iv7yMs5nX0VR5LbKE1JBFACKw1O-ofI96OT12HpIbxid_IXHrbBD3m4Hw4BSQ4BjSGiJvdpgImAREray2LM2skW-36IwYZpObD4ZgimF5jrG7xXLXYXlDsdG-Jz_lRemhK2fU_rjZFQIm5zOsvqbL5CVis1GGrBJ-Jcv4KGgrVw9Xv6MC0zZSPnoShK2tyRV0c1PYy1GYwUEK8btu155ZqfqT5Fdg2z8sPwNKVXX0KYZqPZcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQS3K2Axu7t-gDoqPRtLOJReWm1EKcqPun0pHzjfsD2KsASvrIuUF_u4P3QScNM7iHa_VJdkoYbud6sQFhbN_PAk_me7IuRUuxW0E3NtuoN2jv943wenm6bTBR_-5zi6cqoXCpwNm8tDqC3mj04UbOt9SvHENOGEfnC7T9oBJ8JXqDonD-d4KO8KOrUNbrUvwdiSKmX8MRGX0r4JPk6hJX2r3NVlAnw7n9BtW7VYRi4GRBXIJ-6x3NpPtq30Lj7u50E4ssFv9hVcPkjUKv2n1lNoj6KqwGtND99iqt8eqUcCAqyzySkNahF_9PFYFOrupltDtVL5nmmrYM_xam0Jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDMba78_QK74aXTVAR4meoNTMlXJvY-1PW4NFzawwb4gcr8qv86dbqUnTOIarcNFLs5oyw38ULeJ-dAkoImC1XFCTL_AyNlt9klEZYnwHMBcZZHi4W3PG9YCMhmsqC4j--iF2r-hIbb7RIYeZtnD3L67r1Hh3xzO5d0yuXRO1BgjKKdxznBVRB-pi-D6-DaLq4bVGwnS1dDVfC3olZwZEdyvCgMbc9qo-sMtUGowkO4J1QibIKNTiZasuQXXpgWNP83VP6gtNjQ10VO9tafTQUi65MniUPlWBMfxtqcjRDXyqUVy2weT1faXzj0oaN-X_Dk-rBWtsuEKLWu02ULhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGEeWsuC4M7fICcU00QoSkDox6rFGkAv5HNQF9iVAgJEkOkFMY-8llTj-a5xIMveugSQNJyHlQrTFjYIDcqgakaUOpj9k4cgvNPVbsRFeVC0YdIvz80xjirmLsZ9jREmT9fIi6unaF7h7SPBxIL_pKviL0zsWW16YZPKbDIQ_PLnTAwlyrtPgTfnIn6MtB3AkG0j2cRq9DQ0Z_NzE1yyNasq3VBd1UjVdY9dkaiYiAsi_U5Li0SfAPxR-qoXBB1QJ5KLyvVoUBVsY0iDLAJdYrICeSpxxAgZV9NXvlBpfOokdaHuTA4Ie38dnh7ZNS9rTqJj8I9kxS36d3g8XCpzNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfW_7KpyXxd7iOYJHVPV2w7AF48sF4lF7lq9WcYcAABXKLFVd3gr12NWBkhMfI3GAI_w92G4O1Z_3Ys-rAKJknvxmIqSeylfTaAM8uPZuh1Iq6gQC7a_piXI0VWQhjbiaaDsY1IVxocTUCMPwAohUNymjlStheiy9KmZ1J0tIvmpgvDWGhfkLT166S8HsCAuwEX0MXF3Wcybnlm4H18lAHBuQRmcKGqF6O4Gu9baaLxFDofMjrJX4xgvZTbeIJX7Cy2R-hfQwiAOBpvElUtbmsZHkwBOcy-hZA5GA06S06igLqw-Csvc5m1BGUzjbYCevVtQsNtUJmJIoivzSpfQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d926debd47.mp4?token=hw1C7dBY4ZD083Ka1bqsce2no06zHsSu_7Bf4aBZJbnsy7fNP4RXXyEQeGZkd6n6TdJqseAe5-v0JupyVft_aj3_F3HjDbRmVk6gmMcfDNPLPRJllZ7NoimuP7Mod4qo7zbd9vTjl-1VI2BKUzRF_1kgL52TWyp3vxsELFB3tMuwNLAPyjdLy8llF3NnUXmHiiyIzLX-Jo_RR07UMIUMrWVOMuApGqZSNbpnLjMyi1_Cd-REoD_jcYYT5ea-tu2G4-obXiNfLo88Lt-nEjw0SSJl5fcJq34EaKYoy3GxbHicifaxncNncKUkVTUubIRaL9J0uep4EixqG9LMq-dkiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d926debd47.mp4?token=hw1C7dBY4ZD083Ka1bqsce2no06zHsSu_7Bf4aBZJbnsy7fNP4RXXyEQeGZkd6n6TdJqseAe5-v0JupyVft_aj3_F3HjDbRmVk6gmMcfDNPLPRJllZ7NoimuP7Mod4qo7zbd9vTjl-1VI2BKUzRF_1kgL52TWyp3vxsELFB3tMuwNLAPyjdLy8llF3NnUXmHiiyIzLX-Jo_RR07UMIUMrWVOMuApGqZSNbpnLjMyi1_Cd-REoD_jcYYT5ea-tu2G4-obXiNfLo88Lt-nEjw0SSJl5fcJq34EaKYoy3GxbHicifaxncNncKUkVTUubIRaL9J0uep4EixqG9LMq-dkiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28489" target="_blank">📅 23:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4elalfaGQcanB09lkM6OfuAVJU8fPcQ3H2oFzY6ZpUw39ZJzqyGg1HB6Pk-iTaK00ZBegqg4x0hvVoEsMIjFA2nORKBCS2chbARLYkZrrZIUR0eS-Zhbd2JLRkvTLGjSXwB1lSCi2tT70m9eXXi5Uln3VzKWcB0QNwP1PqqXCYhQmOMT43AwQVZoe9p4XJkGm8zoS6IuBRVmoS71MYqWFQkwTRxXxdKB-NDWtGQKCM6lZ7Du4j-s9cfw54a9fz_jM3o38PV2m_ta6JP6a6tvezc02tfnvn4Qy8n0RcTA2rBIV-6Nm4BW6VjHAs9awbamCo_eY7puBDLGT4j1pr8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
برونو فرناندز ستاره پرتغالی منچستریونایتد بعنوان‌بهترین‌بازیکن‌فصل گذشته لیگ جزیره انتخاب شد و جایزه ارزشمند خود را نیز دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28488" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28487">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv7zvPFIlr7uS0lYVUNTAvfaMA_YOPkfPphbRydj6ERCm7KxSlPZQ_GZv69TpbanoLYP6a6sgDU8VclyU_gGWozec2_keTBkaf64IcYvUmA-bDyMmTQC0t9MJ-7Ci2hKqsctyV2P_BJn2xn3qwX9vVqNmIuz9t_3AlZsvp5726L5j1OvcIBQHbzXVES8dqeG-1tNQV1V3FbtJ2Jlh9KxbM8GSS9_zbOQ2HM5LV4-LDwr4t_8oBWvjk4SpMNruK6AjbS8ha5jrQTFuQYs7qbeZ4zGdiLdd-Cqe1v8P4CRZNgplAO6nWal-g6vw4Y1YRUGU4_oYqDgrx96UuTCNykGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ترکیب‌تیم‌منتخب فوق‌ستاره‌هایی که فوتبالشون رو ازباشگاه‌پرتغالی‌اسپورتینگ لیسبون آغاز کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28487" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28486">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=aiMUOCVP13bQsz-NYJ2jVD4ypPK5Ae-x4aZjB4iNIHs3fzhGZjLEz81nS0xPEVmpfluV7BAmgKJO6oEjZGR7u16WWbOKjsXHXPolddRIlT8AQvfXVHO1aZNHqdUc2mHhHcLqGhl5oSuizPbaFas2DCnR2JAp5oS1JWfS7dl_GSBmvQ0ioob5rh8LGuz_cuK1OC-bmEIZ5zBmbiEd-3QlR84vt25VMlWLvI9QVrxGTIj1E6zbJVSPTR3j5Qd2l_gPcxh_-m19TpuxpQyvmK2ihISHU2EVihkGUxapGlG-vO3BpSqPJ5GckcrQSV5HgaMYn8pIoOOzarTBug3_KVipflaQ7_iqOE5oABNJjwgDYn6cML7506p0xFpjUGp9W6MtGhJ78IUDrYVsuzMDVVQZcAqmOuKFs0oS1maLaAj3LC_ooYVoT8b04E9tpLxzTttamw_Ear-pM2rjb99m03tBkC7sbv_EeLjXOPies26gfL839SLbfSiZdguiE6iAQR01XB9BRI_Tr-ZS_FIkT5YUkIRshI4LrMI_aMnZGdb7OrrcnWBD5KK649MbzfNepjSc1CyrNQYV1ZzrmdV7myjkTFTIWFlOmgC5GMO9wTTSjMz7yIRNm3_8zApVMI_0wjtT9afI3h_DupJc068P-jsL69wQcDy3oQ6Rs-wbmB9-iSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=aiMUOCVP13bQsz-NYJ2jVD4ypPK5Ae-x4aZjB4iNIHs3fzhGZjLEz81nS0xPEVmpfluV7BAmgKJO6oEjZGR7u16WWbOKjsXHXPolddRIlT8AQvfXVHO1aZNHqdUc2mHhHcLqGhl5oSuizPbaFas2DCnR2JAp5oS1JWfS7dl_GSBmvQ0ioob5rh8LGuz_cuK1OC-bmEIZ5zBmbiEd-3QlR84vt25VMlWLvI9QVrxGTIj1E6zbJVSPTR3j5Qd2l_gPcxh_-m19TpuxpQyvmK2ihISHU2EVihkGUxapGlG-vO3BpSqPJ5GckcrQSV5HgaMYn8pIoOOzarTBug3_KVipflaQ7_iqOE5oABNJjwgDYn6cML7506p0xFpjUGp9W6MtGhJ78IUDrYVsuzMDVVQZcAqmOuKFs0oS1maLaAj3LC_ooYVoT8b04E9tpLxzTttamw_Ear-pM2rjb99m03tBkC7sbv_EeLjXOPies26gfL839SLbfSiZdguiE6iAQR01XB9BRI_Tr-ZS_FIkT5YUkIRshI4LrMI_aMnZGdb7OrrcnWBD5KK649MbzfNepjSc1CyrNQYV1ZzrmdV7myjkTFTIWFlOmgC5GMO9wTTSjMz7yIRNm3_8zApVMI_0wjtT9afI3h_DupJc068P-jsL69wQcDy3oQ6Rs-wbmB9-iSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تومیسلاواشترکالی
؛مردبازی‌های‌بزرگ؛ اشترکالی مهاجم 30 ساله‌تراکتور که شب گذشته در دقیقه 80 بعنوان‌یارتعویضی‌به‌زمین بازی اومده و در دقیقه 90 گل‌برتری‌تراکتور روبه‌پرسپولیس زد. سال گذشته نیز دردقایق پایانی‌بازی‌برای‌تراکتور به میدان اومد و در دقیقه 90 گل‌پیروزی‌بخش‌پرشورها رو بثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28486" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28485">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alwrlOefa3BvSeha1-brXE_kf1Cwv5Dxb_67e-Yijm4UsPMlaO29MRuNoSeGOyb-wjRvjFwWa94win2e6bGa96O_brYwJkOOnA_cnvF9Hx7v83fjcNzg8lJzvNK_jAnMjnXOkomGl_zK1Q_NmuWmPM-_BBZz2rmAk81kycTL4o4hBvggkZf2Qxw-jd9mFcK3yh1EVMob1W2kHo51ZNZKoppH2QB7RzcA-gl1vluCG_iyGdmtoToEiT-mCXro22b_hdoOjBR50dFlO9PYD5NbL3M0N98zh6SXY-emfViNc691SXEPMBPRNyb0q52bNvjmRF2PQ4Gn2wPWuSaOWauP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ انزو فرناندز ستاره25ساله باشگاه چلسی در یکقدمی پیوستن به منچسترسیتی فاصله داره. آلونسو گفته دل انزو باموندن درچلسی نیست پس بفروشید و 140 میلیون‌یورو درآمدزایی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28485" target="_blank">📅 21:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28484">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKwpFFVZWIC37HF-sDjLwmPiPpolXuAvQwQf1VVcQclMrj2oImHnTHuwAHQz0wlyNu2_ZamRCQQwMgOTwJllj63FnxN_C0CGZKWMnHHKfhM_V3RuQj084tVfxKv8gv6nT8LjmFMpLeGwFj1c8t8Rp2xzCRS-CtFmfuhlYxvoB_7oaNrj-TYj1p_veNN3pNDxPYIznLFXARPwvAvk09TggowWcmS-LUuKEbuiiBpSoIUDaft2bHpDbCJZ7xC9QC1rQw2mfgNEIFdvBegksSssgc26NCcDeSLwdlg1ceUx8VUt-OIkfr8ZXZevsqzxbEiS8R7o2X-ljO4MnM6vUxKVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌میلان باموافقت‌روبن‌آموریم؛
کریستوفر انکونکو ستاره‌فرانسوی‌خود رو با قراردادی قرضی تا پایان‌فصل به لایپزیگ‌آلمان داد. انکونکو از ستاره‌های فصل‌گذشته روسونری بود که روبن‌آموریم نخواست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28484" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28483">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF7a9CWrdKeWf1kUAtlzhYuDtJ204RfTprYsW9ttLOFAY8vx8YFJinCjAkszqAGGQ2X4P2TKODKxzPi134fPcThf5ybz6XfsOwaBZNjSw4pQnMG4RquwuTRS--BZn9Qo8NhYbGgkjsXi4-0xTM-VVSUglCisQkVz4YpU7I3GSTfXegdbdiL3CMwM2D-gampoS6AEnXkr0-BHNAmSDCBO9NwJH2vYYIvFJDWfGww-BE1Xujz66sfs5XHbVT9C68DRYK1Q1NGELHu1Kio4VnNzj3lb7eM0mBT1TEpeMbX4WzdN-RGM9eLaYxBLMbA87H_LKlbpNL80-jrCmP00mo_7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28483" target="_blank">📅 21:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28482">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRoBIvU-6tpLLZfAAedauAZJT8U_bT0QZtZuBYoNpOBsvALpgqlh6zlktOukmAqfIBywMYJz5WdvJEaPqmQUq7RWJJ-AtEmaAyOfOK9Fb4IKe79sUKyCw_CzYcDQvXmAzCC0bOLg_y_UIzqmPZkQ_F2u1PaCxlfVroMDUzXG4QsRlw7DvTGqouUhl3DU4iowBNk32jQY4t4Oi9Qkyax23zHUyXh0KhvfflHxmQzAf4EhYpDv0CiNsgDjR_KkULL5JGNLFa5FLvw_WUutYW1Op_mwEO2C_EfQeT8n4z86r1BtAuEz3LfALBoqNormcFgmtD9PBYo_fTmSG34YRfq37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛
با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28482" target="_blank">📅 20:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28481">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG62dsIelHEoZ3Fio20hD-g9ZAGudfrN1PdxdyMgEncT5FatsHB_15tcsL-O_b1ZTmg-lxsofrHx24W1PbBVuerzmfCCfhAEe9XnHh5E-nm0P7AXfc60qCuPJ6Cmdk8gJVnoOVimGKUPCYoaSvT4BeN3gXjrJQZI4F0Bi4Gl5vRocWauCj8dwnlHHcyVZGiR4Ix5_QR-QFXEmbPGESSYAN14lfOIlgXZgSQdB5aFQoPtzzla7AtVmkDEQTvSv9aZDl9QGh4gG2L8SEXKMghDJko0JBQ0PybOyJugXA1REEOA7VAuRS1GeDwzCWjpa-kiei2dcW9oJ1aqZvb8cSuX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28481" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4eeOsnk5M6eoh7QgfbwrvK2K3oeu7us2DLXCQ6an7Qjvbdb7dTFZrypjNhIkFZuWTBIawMfZw2pyqmqFqRv5ZuxOG1nqCqMzehoJvuTLjbrg13ZMUrDzf22eHwZ7ZeQJH4Fol8pD62A4o97bLsrYbSb9ma_znL_cYJrzPVLRd4noU6IMK1QPwvgNCiCRz3Yx6XtW6GpnmpYI90VTo1auAj306gkj6qBwsNB7stOPp829QTY3kpfaGTxgaZqQzD90obumjeymuje7zlUbgkoZqwhVpYqT3zL5okRCFpcSXihNwYQzKp6PrECebWFRMiz2FG1F1YQKyw8wCBcHcGYdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUvGZ3X9tHKR1xisE_HkbJXiVJ-GsCEh5jHIst3Apl6AWhYT4M0Zmhq4HDxiLcfyvBRKzBulg7bo4oZ0WdXx9O7p1UiDFsD06JLSZN7mqm3y-wf0vUMi8aqEKlwSwXUSpMSa8YauKDPWjhlrPL-RJgiZHqa08PDNcf22GmxP7lnEdZGeBM9XhlrUVdDNEKDQ9rI8AWhtPTizAggm1OnmsIBkj6If8DKN8MPmweQ29klcM9WNpAZjRpsRWtNJSkkbNxtUZlC6DGi-loLZGM5lrMiDRHspDilJ6-K5KA4Wi-_5L8o6C8owiryAnJI_iXfjf8bvIH_0xfndwJbkZhJu7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28479" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYDtgabeiQV9QJneMAt92FMbQFMG8vFUMzEbbktuKjo7wQLqBxJ_EdpbmeIMrOoeIbch9E6UwlyzEfECzn-blxRd9nbE6U30eTcj_uekI_Q4QS9VaTYrDvpES6STTLxz4TNO9m79Hm1YbholLGY2xxwWfTki4UyB0Ru0T3H-ahH-PVR1c5G2_9zBw-zbJBNiI-g3tVSO46FQznQl7b-MTJWlEufVcL2SjwMqC3opFqcWxMDhgLjss88Uh2PbvVYsZavtYJk4Hsjgas9mMXo63ulLSs9deU7kQs3DzUptGT-F8OrkCzaOGNIYVQh7CvNxdMcNOxPnBtrQVdUHEjmYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ هفت روز تا پایان نقل و انتقالات باقی مانده و هنوزسرنوشت بازیکنانی مثل بارکولا، آلوارز، انزو، مینته، امبایه، گاکپو و پست مهاجم نوک برای بارسلونا و وینگر برای لیورپول مشخص نشده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28478" target="_blank">📅 19:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFMZOu6vvePw2hXBmbXE143PBUN8lRxarMLV1UYFHawrt2gUEhGx0bazkvKwuSIbz0ZsoEGQSQJlH57hVmfcCXbT3X3I8SEyjYLYvfxchQbHJ06wiexz2dnYEf_b032wV3IafKM-zU4JntYS7eFfYL6m4FXPpzb6RcuQsDBhIQFELZ5KxNct7E08tlCaPiIGfuS2TkxIEMX9XlgJaCrOWP2zvNSFXbnn4GXGhBZJGbHh7H_RXZpvwtO0sc6BQikAc43cc4BIZvjzpciILAVTlwzxHAc_Ajw-gj4DLZiYQ69e6PvmRrvI6DHAwqMdVs4-6dJvICZjQ5aAxF-SB7uoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28477" target="_blank">📅 19:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0h2kGnuZxp-m23DrKnE6FaXGWooNa39-HOwAouCkYJz13BaFLVmMXzNXfcP_N1NmySGvUS9N1fV5unoQ2NM6q1akdNz9-XVoIp_k4B-fXLlbRnBKGOjNleGBMUJRwA_4sKTIwIM8poEaFePoQr7gSMxN4GGqlNlBkUpJbFbYGMqgdUlnpuwhOi8tTtSLa4g8qH5DfCLYi7nDTTKLDXsBfXV-NAbyLfrFyFECFbPVFn3trc_zOrCEtDfrAnsjlZnWU6d9S5L0q8qFpi0rWPZi_sctMsYLDXgIlgextrNTcD7s_B6BYnbKTwmOuJHlS6LP5dPmv9bRwMJPhSHbldfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28476" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
قیمت‌موادخوراکی‌درتنها 5 سال‌اخیر رو مقایسه میکنی آدم‌کرک‌وپرش‌میریزه. کسی ندونه فکر میکنه 50 سال‌گذشته و این‌قیمتا تغییرکرده. قیمت خودرو هم که بماند همین امروز روهرماشینی 50 رفت بالا.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28475" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbtxJNW2e10ySis32jZzHCggeyDQv3Q-wUHYvqMmT4aWGuexkWiwLM-vgDKCIPmySJrkT_ZxSNwZ2XRDTcxLfFa2cX0l2TvpnaXDq9WnuaaLO1e9L1MNLdzwrh0AVxN2Yv8Qz-XFB0uXDDeWu_GOubueVxuql_TSoDgbqcXFSylJ7iAP2OpTnTOOVwS9ZxzNcNPBSWZRRv_H0YQkU7yIic3z_LlZrtjnyFeKXKg35QC_TCkdbOcjjn31iDh6PdahIptjpTo67-oHjmQzzB1YBohTYs5GIQhGPCspw9XMpvYobU7GobdyxlZhBXd0GcCUi9DriwyNJrJV0kkHM-ZAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2017 در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28474" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28473">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOfZznZRGD8OaURG29EADKmVl92nTe_x8IvUISO0bjcTbBJ1dJHQZv_ooTYkwVt6d9jwfWyn62kNe8XcFe81SvhbBMY5S9atICXBsxbcHz98lO-AIvnIaixHqxf8TOPl1bL927h-rMSjcZ3EoYUPkN9VtpfCCfLyI85FpExvoArcJ9IqekGJ_I-64yFM_5BPCi5MS4sD-AIb3DCOgnUsLiWAgW4xDR2HpjecEtTshlCZbGgoq68bdI_ZNFPiFes6tsPYZFzOIYEdPIYYYhWYPrmRIoWpMRVtKeG6npTpluSahvV6ZCXBQTobGhI9_VjyJSbU0hrI5EqEKGKel25L7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28473" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecKRnXrJzU_iGD7TpgQPqiZLEY2rGrR6IuXpLxGT4alxuTg-xEb92KMNXeDWB3_Lkkkni3gbf00tozuU7CJWrkkMSi4NCBhSsGwKpx0Qm2U1hnYzmHLcR4IMKm69CMx1wzR1OipE3qRgaucaP7cyumjgJ2wPfZJk26iW6qHaHDNrWcTxtjOZEWmfH3I_LlDLOcbnPhwSIKUUrNwMOwfaD6-GgPpfSyK50-yhZiiEpC2wUHcvxDem1HR5dvDXSkqdlp7eP_3dTThAlW02KylZKt_95frmzxvhce1ItR9cnrOBunrdIrdb3QaHpIb5ajtNVudUGT-h8IoDW2VsY1fADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ترکیب‌احتمالی تیم‌اینترمیامی درفصل جاری درصورت پیوستن‌پل‌پوگبا و آنخل دیماریا به‌این تیم؛ دیویدبکهام‌مذاکرات‌خودرا بااین دوستاره‌فرانسوی و آرژانتینی‌آغازکرده تا درصورت توافق‌نهایی باهاشون قراردادی دو ساله تا سال 2028 امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28472" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Koa9UwQDWyV2zlv9Ot0zug-4XxSgHRl1z_gKO3c7UFrOdluq6ulesVFVyzn8TdGjSp0fYWJ3nLTOtsTtVsSYpB-MqTONYmofVMaMiRk5zq4ubr7zgD2ix7_JkIlAVuOCn8ZUdgmLO_pF1wH1PxEgYo21Focbk6lCr70B2nXm58tA4yfzawGVOkjxc7AYpbpvFHYxiWBnrufujcUHEBdPOO5L-RY7Gd3eKUfzTAhHo_XsFSbVMCd7cdkqHCJbwJ8o7vlAsWIrdWBkqIB9v2mDmvBqptLxfZZX_mxWDwy7uBIPYU-7J6xIkRES5sWhL39RDuBXW9nKdoC6JUTHGkirAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28470" target="_blank">📅 16:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=ed4JSZaadNZFt-Wo24ZAfwsr5ss2qVMMdDaP9NEwXfe6RSesDgbwX55Z1JmUdc_fR0kvXWAEqbFsZBDuF9um3qRSCpXHI6ujZ5NvVWZtelblrqN0SK5lKeVM2UJWrDnSdIgkg6CRRGscjGtDliUNoaely8dzBexoylxRewvyAWFL1yO5S-f34yTd__zlXClZhwDdNDpYUmKzIc2dP6uRihQqPNOsLqB5H2TQUxQxJD0g5bsuZvtH7c94CAxIEhy38U6Gej3qZLEva-mxvEmbef_U61DACWZ_7k7NcTzM3zaB7uFJ00uhPM_TYlCDIn5mIoOJnmqrdiu2K9ZtT-Tlaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=ed4JSZaadNZFt-Wo24ZAfwsr5ss2qVMMdDaP9NEwXfe6RSesDgbwX55Z1JmUdc_fR0kvXWAEqbFsZBDuF9um3qRSCpXHI6ujZ5NvVWZtelblrqN0SK5lKeVM2UJWrDnSdIgkg6CRRGscjGtDliUNoaely8dzBexoylxRewvyAWFL1yO5S-f34yTd__zlXClZhwDdNDpYUmKzIc2dP6uRihQqPNOsLqB5H2TQUxQxJD0g5bsuZvtH7c94CAxIEhy38U6Gej3qZLEva-mxvEmbef_U61DACWZ_7k7NcTzM3zaB7uFJ00uhPM_TYlCDIn5mIoOJnmqrdiu2K9ZtT-Tlaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28468" target="_blank">📅 16:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rokLwuEXuhsn91QScF9bTOoTLRh29kBNMPYM--y3oHP2Rg10Qr-W9CI0LlVKS7jZ6XVkIxkYCplJgEcPcX59kRpUTuMueTxPgk_c6NbM1RZFbTRd7mO1YEmJnL-J-7djvedBdvbhaWSZHduDYBiCw_HUVy1N40MGxO7EjbLnd3qDG9oaiiCYXxA1Rj2xLUKPF7suJrpkF7qRKoRTrpjNGxTw58b4mblM-BJ79znq0WcNXRakmnjYVjkIyQ3CruMin_iRceK7ybIKgB-KyNDienTedMHRjF2xyMRU_6JqlSzsJ78SqY8c_ZSP88MxWyJntU7xCut3m9LgjdUnXkmd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قانون 90 به 10 در دربی بالاخره اجرا خواهد شد؟! بااعلام‌رسمی‌سخنگوی‌سازمان لیگ، طبق قانون باتوجه به میزبانی‌استقلال در دربی 107ام 90 درصد ظرفیت ورزشگاه در اختیار هواداران این باشگاهه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28467" target="_blank">📅 16:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28466">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAnlQSH7AKlkTErST9JExecCOPXbooMMJjUP3A_rd85IpSR-nYA12FIqHNWlaKBf4wuzFUnW_fCKi5cDzXO5xWvB8WE9fdIwJG2uxkTBEJEW4ubaHNqIcukbbjWjlSHnkAU_5PL_OlIVy3gHmmPoBREPd5VCxc3NXbDQOj81ZF7dqynnoplCRqxXKGUWaba7U6_ZZIxMV66Zs0jdoeQBcI07d_xWTCUvANEjlBhHNRfTg-_aJG5HTiarzVCS3K0d7knVKuqzT28_BuRqm9smw5_g5_Yrg-g-YLLcbk9UAlvKzKw7BVv_BWNIVPu9ZEOqjdw5_T4q0FcXHnCnlCOu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عارف‌غلامی مدافع‌میانی‌استقلال با قراردادی یه ساله به ارزش 8 میلیارد تومان به چادرملو پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28466" target="_blank">📅 14:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28465">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEUJ3rTQ0dz0WtBVot4Z9ya9JRdkAXoKAKHLsQK8qWiyzdLPcutkaaoGT8pcZL5coGu4mGydQ5t-0VhZF3-TKbCyegmxW4DYY6Bg0F6gBJXQd2w2UTJiY-yP6quDFa46i3RE3F4lidCFy3JG-7FBQedwoROEqMulO2GE_NRZotiXBz1gG71vi2IUdGrKbLprcnFe4liMp0hyKv0BD1qlnZV6eDwaweSfZmdesVWJByWu59Wp83Ue_AkfzcYsFpCOC1Aio7MwGafjcSMuh3IxUvA6SMUtzJSfN8_gM-IRnTdI36EZwPBebalMhaHQXbIPDI14KzqvmAH-AOymGcW6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28465" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28464">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP2J6JtxvVfKmqLgp4GD9dExcegUYbBIT4w98OSFLXc5PrCTJ1HXgu39dWPDHWu5rMMz9ak_EZnkbmsrMmU2xgzZT6Ti7UajL6XLaa_QyS0MC_vKzIK3dcWHLdoM0hKX78yd9L9edag4ub7oVoL2l5uQNK9ly1LYflioe7jOztcNFCLNBRzHihsfV7bZV1ENnMpA291xnzuNbSe0Y8iNrv5ofIzVEUfeJ0Tqa02iybM4hZvVJ3kmHoH_MYF_qe_Hg4PndJd-Ery_oCPoWrzDhhm2KcS1C6n-assP0ZlKCs9WOOR2-e_efgx5UrzvEDhc-YN6-33r7llTvrGeJCdwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28464" target="_blank">📅 13:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28463">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP5XClXlCqjuLHzfTA2V1BcUhPjBOe3GYrIAnqnpbEoBathCQw0jwg5dB5gfi_CbT87dOm18xXsetu4jL1qi8WO2Z0VWuD115viz-7SMXGZjHFSw5qa83YlHENNBgd9HiMh76VfyjNIVyD4IoAMKIu5W2JfffnkIHgVnud7XAzLItJP7YGaysxLSeARv3vjdXSD71_pAMtxBcqV75QkeLrwQgtTADyAPsWqH107MWsQs78r7grj515CqkIvkskK6PWosJ91K5_i2QUIWVFOhwvdaWxUED3Qf6TlqITlnPjKhNnsUXbh_KxjNGYqwCnUB_ks5QhZUqoK45JUMEmRYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توورژن‌آمریکایی‌فصل‌جدید عشق ابدی یک دختر ایرانی رو دعوت کردن که همه پسرها عاشقش شدن؛ اینم رفت همشون رو به ترتیب بغل و بوس کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28463" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=Tb0nQDp3gBnQedXYecdB2B1zgjLzqPA_GNBh8yPCZOc8eLr_ehCl3MurrM5YpzLQnnEGlDPoC5esjyBK8o-zWFdhZPHSGoaDuETTAgB4u0-1pAO0qqh5xSV7DdDo6_kab_vuNjkbPUTsiR63ZNUyCgI7uykONoFwt-xkEQay_1z02MHBUiGPlEebIOo8AO_5HtzNAkDwOMZmvJpY1rmxzX9_HaeTYqbdhboyS80TxNq_y98B3q2GbIsdcmkKeNh5gf7uvJuMjiyKGovXsMyjJaF4MT91ZgHB5XgeECOXsTiYBuyGtfJsjXtEY9cqnXVJEtPHRi9SFzcCRkaVantRxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=Tb0nQDp3gBnQedXYecdB2B1zgjLzqPA_GNBh8yPCZOc8eLr_ehCl3MurrM5YpzLQnnEGlDPoC5esjyBK8o-zWFdhZPHSGoaDuETTAgB4u0-1pAO0qqh5xSV7DdDo6_kab_vuNjkbPUTsiR63ZNUyCgI7uykONoFwt-xkEQay_1z02MHBUiGPlEebIOo8AO_5HtzNAkDwOMZmvJpY1rmxzX9_HaeTYqbdhboyS80TxNq_y98B3q2GbIsdcmkKeNh5gf7uvJuMjiyKGovXsMyjJaF4MT91ZgHB5XgeECOXsTiYBuyGtfJsjXtEY9cqnXVJEtPHRi9SFzcCRkaVantRxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28462" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEIy27RzvrzNIm1tXt73zpeSdqEZ24-w0WgCWCFj3zElVe_2nM0w5gJX5_Z317_vMbbU8H-Sc7RamFWSCdsNCsQd79NIjR0PbeKx44CpeCElRhFWeojLl0pw49TnClGrN5aGo7vbAKCcOa2Xmz95XVA2mdaOESL58QBf7Na-ofCIG5tzkB25mtdnyH9g5q9LyXqZowOdGxpkid5grOMLyPZwZ0ywNqslfhtUEdmgLNy0RaMupLXaFVjS99R-LL087yXFfR3vMcPXhs9LcU89YlDGPaQL5NLTPD8oZle0Gn07yupQQirEZCbhZdwN8qfgB74cfN1lEnE9AoBaO3eDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28461" target="_blank">📅 13:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/my-IweLIWGkq9ShbYVZprfyAUCsgDPzPwxPEO9I9KffhQyH31l3UeaWBJQGvsHgbhSvJ2B67hwDfaupVGeWpP_rIl-EJw9RXhZUVuQxl6yoIWqcNBZMGiXQL44yucAxi6tzhagW0vyO82stPoMGsbzPNzu1sPnjCkYuwB2z1zclrWj6cmFZ-kjYg1VnyflErMtMT_RrHT1kZ9qyN2W52u5PYLyFUw_nskSQ34eL6-aaExGni-mqq9xl1KlWaLkZ3Ap0Liu5bB54UHPWeFOnwSEcXlseCe3ZbQBR1BFnz8r7MGd8BGfgxT7TkElm5C-K70fInuAq90EEpr7sCdoUR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwKAvINO2YwVK1sYwwrXx5xv5GZwqdYQE4zvfMYts72XlDYmTBGjHiGRQfIe0Xh9mXN0edBXZb0g19NVu05uVBkxt9jsypaFqCV4oIW0B8_dg6BSktIrAjUE8cuO7u15o4i6SOXHIAogOV7CaqE3WY_9WJnIyM7d5Vbvbga350PAti3TiMo4J44rrM4kGj1Actl7u06gEgJrEbTrpBMJnFNp1Jccu42F2DaudYQqcO1E1d1iUjRcauJBByO1IKcd6J5qahacV0sQEvZ3LfyNsa5VX4ALGNC7c1sHFJEH_CrmlPxCk02PrnJeQ0PvvAaPgZVP0SrVkZAlBmvPP19STw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
از مربیان آکادمی لاماسیا؛
که حسابی به بازیکنان این آکادمی رسیدگی میکنند تا ستاره هایی بزرگ به تیم بزرگسالان تحویل بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28459" target="_blank">📅 12:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Em17mCWmXgjlql9TZwzwBPY1hC5pAmPdZfFUs11nLfz-QL3mL2Hq-8IXLUNDOfapT_UEOAlS8oiQeGhmrkHQBjc4nA-hA0fMcksAmVx7Zwq-kyE11fTPi4KjVCdSG6Z3I-ELclS4eVMBHOnOcTdqTgWVrXCh8D4r77ajbW_R1APWv-_ps3mPO1c3-4PjKTWvpGGEu2v7_cohpUYQsnAsJh29q__IAW8yXgfLIsCudYODAIm3h1YUxG8R03OUCQFS_WGOJMSDv_3t3w_RlNe6CwrrZI3P2Tyo1mOHS7VBgUT415e39ioiZWkWBdB4JuAD3ksDJDbaTRI10H9dS_g1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Em17mCWmXgjlql9TZwzwBPY1hC5pAmPdZfFUs11nLfz-QL3mL2Hq-8IXLUNDOfapT_UEOAlS8oiQeGhmrkHQBjc4nA-hA0fMcksAmVx7Zwq-kyE11fTPi4KjVCdSG6Z3I-ELclS4eVMBHOnOcTdqTgWVrXCh8D4r77ajbW_R1APWv-_ps3mPO1c3-4PjKTWvpGGEu2v7_cohpUYQsnAsJh29q__IAW8yXgfLIsCudYODAIm3h1YUxG8R03OUCQFS_WGOJMSDv_3t3w_RlNe6CwrrZI3P2Tyo1mOHS7VBgUT415e39ioiZWkWBdB4JuAD3ksDJDbaTRI10H9dS_g1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال:
باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28458" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPYRtWTVVKoGuxmTTHf1jVXuN-dCv1G7_u_4H19kN830zoXkrxRs5J0sYfiyndNnZxTWGO4D3opN7KRTbwNy1MK1PbqM6h7nvzw40aTuqdDC2OoYgJGOWn0UEOgnNJ9PqIATfz24f_uqkyLAIBx18lt-_rNaehrtd5UsNOnQED8L-Iwq7B9dozAsW4pTgmFTE8HHsmoqHI-nCEnqn5Vy56AAnk5QQb0-ME_VLDikzI-Uf-iqVnE0nMjxq1JvNjejcWwYl9whl6pTheT9MpsCI0oIXs4tgjjyoxStvTf56ui_nZVLoNUqH2zDvFC9KYN4F-24q-m_4fnxDx227UkWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام خوزه فلیکس دیاز خبرنگار نزدیک به پرز؛
اوسکار ناسی مدافع میانی 21 ساله گرانادا با عقد قراردادی پنج ساله به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28457" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28456">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNV_J9BZVG6niafVx5OPEEhwAijVSaGibzlrtWQbIUvJqBZkTQGor1Ks7GJZISQ2svDYv2tuh_7TGRzgNhDFYo50d00TqSDnaFcymH32KVeqCSTHe-euRTQPmFOB3n42CXsdH4ajWeCzfD17kD-v_UBw9i059846V2Eg4JPONkM9qBtZ3q1k5gRBmKLXxIS9L4UaGEYs1xHtR_GfN7gY1JgysnSoyBprKOTHTBDQmoQ2xLYVWRab_yTjuAMsNh_ieJ-8SJa9-qoS3JIYYgu0Y2qZ89elc_3Gwb43ll2L1cZmJM39cw3HuIBytDv-ntgF64CTUy4nEs53ByCHPLOBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی‌از حرکات‌خفن‌و‌فوق‌العاده برای در آوردن سیکس پک‌های شکم درکناریک‌رژیم درست؛ تو‌ کانال دوم تمرینات‌بیشتری گذاشتیم اونجا هم جوین شید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28456" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o599F29wrPI7zxfchlEcGxWHf5XTScjoNhen3GVcTPY-YFPzvOL_CSLg_RrMUwzwYi2Tty67Bb3XF0Fc_4hfTpgD7R38FAzNhWEAa7e2K7aLQeEE8dwDMCdmZhzW7aIPEi5kcoLoomGHEaHb1x7zzJLX-T_LcUUlByxzIhCxuF1IAY2Y54JG7ne8VVf2Dpj6xM3YiRTiZM-o7tHW71YQywODrAZ_R74avQblRYfHsDTlIb-DbyyNoqzwh3aC0F968pzal1aorJ-JE1u4HzYzjtOcqsHEqdgLCFLSrrKe31vDXJaQTWAx3nZbhpIno9DApbNarkNULkHHZ2N5IuSDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمیدرضاگرشاسبی‌مدیرعامل تیم فولاد: باشگاه استقلال یوسف مزرعه رو میخواست و مذاکراتی هم بین دو باشگاه انجام‌شد اما کوتاهی باشگاه تهرانی در پرداخت رضایت‌نامه و تاکید آقای حمید مطهری برای ماندن مزرعه باعث شد که این انتقال انجام نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28455" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBZgaVgdVX-Gq7sN4qXEGDI22khW8IMn6XrkIahK0xqzD6Aftw6b469cCfbqPO5I2l_ajNQoP1POX61KXnEmjQU635y2ruV2DCB_gg1jwxqMfcC90-Hz42QwyQHKLC2NtpAQgNj6XivmQuJmT0x5w9mWRyll1J5v_-yuGNnjaKTJr0lws_s3I7gLkIut7x_rJTWjFCTpXaFqOhCyaEuPFxUxYHtrp4IskS2qh1UFENleCIp69zU-Ce8V8iOCGDRwi_LhXMUFSqNjg-rtE-_9gRmjEBVEtlUjm1x3NIykD62XRcb0Vjvbtlxu0wammclCdxBlU4-Anue4hUJR7AXnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28454" target="_blank">📅 11:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSI7hfOLEVUVQ_s05syA4ghh0gYHGiqS3f3oaAfQLiAKArf3-bqvJp1pcsWI8uz_x0y0rXggp9DYQfVIEhbL3fMEuLMSlN_pekeHIfBvfw-FbW-1Z3x3MHdRZWKt1rqNMgHk542VuUd6DZYFMWDkLHBrfRMl8H4NDk4r8IHJ0Z1w-BzsnxHkh3G1pDkrZPkx53cfSZnvO6VaCmCv7wkyYr5t_KqyMo9s4TYlvPkuUR9RqnBhYQ3bYf8JovsKIDE06Gt4lFzfVBV-KfAjEJv8KQD1_zvMLCw4O6JAHkjpeMprH7dHgKisKZOsP9SLVX0VfpWdqaIa12ilZD-OIlFPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛‌سران‌منچسترسیتی‌بیخیال انزو فرناندز ستاره آرژانتینی چلسی نشده‌اند و مقصد دارند به هر شکلی که شده او رو به خدمت بگیرند. انزو در بازی اخیر چلسی از سوی هواداران بشدت هو شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28453" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28452">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_Ppm3grh90L1bC-iiAsoqhrhkzvaJb_h06XsUjcQ0U-0aCM0iY89vqLfSg0SNSfAcFmWwfWvywmTcY7Yw0AG-5lhGLstEmJdkDADvTYH-upYrcPKwaLmj6IAKveqgq-ygcwAMhQ1gLAPaZqDhR1LTowtDjomwnT26PN0qYSFOVNSywv_jm2StRxq0-nldiuKU_ThWNCxvsNitRtYq8c-R1_6WnN6iNBIIM-xqp-QJugr998dlYZkIIlYe41XRt2EDITsc_sVDQEYtg_Ef7ZiBa9LAw8uJA1KZxVBWjN7HcTrgrSQvZobvSvyBO7S_pZnSQyso-krYpEsKYVNtYySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی‌تارتار سرمربی‌پرسپولیس گفته ترکیب تیم‌من تشکیل‌شده از بازیکنان 22 23 ساله. براساس امار رسانه‌ها میانگین سنی تیم پرسپولیس در بازی امروز مقابل تراکتورِ نکونام 28.5 بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28452" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpi4TT-TbsppniPfydFpTF7XUftTU1LzRlX24aQZTLwbwzsD-AG9PbyizEzXEK5tQtUOEQ20RzdO8FT0uM2V_1Uyn8lHfQ74Jv8vxNUoE6FqouKMmEmg3DQSLRCHnJHq0e5YHCogx-iLczEsitByBaC182zT7R4ZTeDl9zSn97MIbjDdB81EC3OC-7fQ2SEF4a7Y8RC0dmTbKlkgl-hycEq6i1ycbM9IQKJKgLPy-J7hAq35RB3F85mxK_rkCz0w_unY79rjfNYoi97N6QLBVODnHTfIHWZw67msoqpdexSIW1DNxCqPhGnZjZbIFkC7dOLrthjON3SCK-QlZDPIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28450" target="_blank">📅 10:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=Ru2APWxhWekKDZZ6Ys3xx4q1HIw31lk_0nS6iig1EYYuDNPeNr-I3-KBZm3mSbi2p8il59s2P_Ga2dbQaDNBLiPvpNr5gO6JtN4WsClDlDH-7LgGCetg3Jk8V7zwYsglA4omLKZy0D5tqCt8NhHO5XUmOSwgwEa2YBNmB3gspEXWcNthob39Ek9FZ_l8tjn94w8iQhymPBHU6T_68icAVbSr8TnStAjhc_MgCzOfOD8qyK6DqN0N-2P0g8Dpu4n5ye0R45Jl5q7_jvo6k6oS8nlpxoEY_-Q2Wlz1JbzL3rwZTVzfAdvb7tpBzEpYFJxLl6YMmrPJuPrZw0e6KvOY7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=Ru2APWxhWekKDZZ6Ys3xx4q1HIw31lk_0nS6iig1EYYuDNPeNr-I3-KBZm3mSbi2p8il59s2P_Ga2dbQaDNBLiPvpNr5gO6JtN4WsClDlDH-7LgGCetg3Jk8V7zwYsglA4omLKZy0D5tqCt8NhHO5XUmOSwgwEa2YBNmB3gspEXWcNthob39Ek9FZ_l8tjn94w8iQhymPBHU6T_68icAVbSr8TnStAjhc_MgCzOfOD8qyK6DqN0N-2P0g8Dpu4n5ye0R45Jl5q7_jvo6k6oS8nlpxoEY_-Q2Wlz1JbzL3rwZTVzfAdvb7tpBzEpYFJxLl6YMmrPJuPrZw0e6KvOY7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
مجری‌شبکه پرشیانااسپورت:
جدا از شوخی سبک‌فوتبال استقلالِ سهراب‌بختیاری زاده یه شباهت هایی به‌سبک‌بازی منچسترسیتیِ پپ گواردیولا داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28449" target="_blank">📅 10:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTnaq4ZyreYo8FKvUUhOSHK0z64KfmToMQH5sk-YeRGMBeIYqEeHm_y5a8eh_U02DcSanKIMs8qr_2sVKzHKdyoQOr6nT_rUin4QJMx-3YFCrxJMFqS8fcfUzcCOlyqxGuMZnm2bReY45Rioxm9FabN7Y6xNPNZIL509GQGO4b7EyB0B7wPBxfUEBTZJLaUuacPJi-iCWYZw3Z356Rk21sjukhU7Wz_wetBLNBi_UYXDyu8CV3yaBnongLp8_YIr0RGjIgHH8jaUfqL1Q1XG-w91lknpqifXNiXy0KJ080mWNlAIZo6eCT-o8xCX-iEdaxHJsrkSrCxsvC5eLxoP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه سپاهان به‌نماینده محمد حسین صادقی وینگر جوان تیم پرسپولیس اعلام‌کرده درصورتی که بتواند رضایت‌نامه‌اش رو از باشگاه پرسمولیس دریافت کند حاضرند که قراردادی‌چهارساله با صادقی امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28448" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlYFFalexd9tKI4JHHQfir-M6xUYB6hqi6-3vO68_PxXlDBVqiU8yYb-4MCZPd0uKG0pvIBqpKTNS3xzBN5oNvYMjhnQzdAB3MxCa5efBwEvewuK0VZOlRrJxWM3ayR9NIb38RX9ATuPGrLZkc4H4t9J0YWRTkf8oNs0XQI4OlL2jsAjpymOBXlMujOTNXrYzmRJ5PjWzE16JRDG_DUAJjidYa8z6L8825f6DjwDPbNjdOeACnbChETeFw6LXhakgVcQKGEYrQyWHoNlFHuUDpW5-naUSJW--i5AagTDdBekZzM2LOibsQgaecg9vc-xQeVeXn6v--zxHA3gF330-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgeOcC4XK_1b-bjbjWm6pFZjW0qELxmydxBFI3UcBM5t0Uw1VYZ9SB-p39tffhx5nYIhaa1hLW02Mmyv7bh6PAxGZBg7RrS8_W-g3lKjjCf2-KGG6x2c_1nw9JRr6sJrj9ZGcl8peysrgfra5DjAEBG_C3W4qErYvEg9qZWLLhfXabinyir46S_qHWxEVWGOK9RmQAGJ66Sm0b5OdJAkTSxktjbCMHpQRAMZSHCUO6N5XCdtt-lT3w8GpNPXaa3T5nObJgLiHLn9ELtWL3Zo1FJdaObglwbzDXGqMthlOCApLxPaqTp_hfNHuakIGNY-IcoWU4Q_HsaaXBtwkevJGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
برنامه‌وزمان‌دقیق برگزاری دیدارهای تراکتور و استقلال در لیگ‌ نخبگان‌ آسیا؛ این پست رو یه جایی سیو کنید و برای دوستانتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28446" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK4mFhxEoSK8JR5ps_Odv-c3Xw_AADWqkG8IRm2iz2uaAQkoHb_5Rnc3AW0nzCn9Vg_olqXoMGliHPhnp_f1Vp-Qo344MJrF0kV9DE8hoXPWgFhQdUNh2Lh9DBr0u4cUQjgPmNy6wa_LeFIJ9l73-3_jTUSnG2AKV28TnopqDO5HH-pKYrtdWWh31cOB7eCfebcAjFfzoeuK8JFKGMmo6ZJYl_DQBCAlI4zOSvT1ZmugGvPQhnZi-KYzqFVRnYG_kgxqRBBX1gxJWkF2H--jm8S_8rGAJDSvOiTG7lAmv2OH9S2jA_czenCXxYNjoOy6237wSZMO_nrPKC5frrcipAro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK4mFhxEoSK8JR5ps_Odv-c3Xw_AADWqkG8IRm2iz2uaAQkoHb_5Rnc3AW0nzCn9Vg_olqXoMGliHPhnp_f1Vp-Qo344MJrF0kV9DE8hoXPWgFhQdUNh2Lh9DBr0u4cUQjgPmNy6wa_LeFIJ9l73-3_jTUSnG2AKV28TnopqDO5HH-pKYrtdWWh31cOB7eCfebcAjFfzoeuK8JFKGMmo6ZJYl_DQBCAlI4zOSvT1ZmugGvPQhnZi-KYzqFVRnYG_kgxqRBBX1gxJWkF2H--jm8S_8rGAJDSvOiTG7lAmv2OH9S2jA_czenCXxYNjoOy6237wSZMO_nrPKC5frrcipAro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موقعیت صدرصدی که دیروز شهرآبادی در دقیقه 90+6 برابر تیم‌تراکتور خراب کرد اوستون اورونوف فصل‌گذشته دقیقا اون موقعیت رو تبدبل به گل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28445" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlRezzGwf-swu4j8VMCEyAIfIqOY1epUUSKWdsbtXiInWXguGBicZsVp9J5N32tJOxmv3rvqRn6dGTfP1ZLH8roG1IC_YTOlSb6PzLVeV0747W7FEHxq9b_39K6auYBy44vEjV9SLrGyrl7B7o05LbLWPVwHUFxWV6PunO5yr7BPXtvuHlV4djHE9lMzGGbvrV0tGvRAGsN5GqJcK9jFT-7kDhTiObrZHpd9U-vPr_jkaGDi0E5ca21LUgdgxqqATFQzKHLcOEjkcm4UCcoXhdCJa0Y5c7bwc0SWB6pllNey6F6WVKtZsBbD7rHfVE2Pm3v3eUb7pyAD68Q6isGGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی:
کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28444" target="_blank">📅 09:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28443">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNsz_tbsS2wNjKLzz8jCGdtfzrRIF7fnmnLu90-GtENa2g1n6_EGz-c7d_fQvA8LMfi7I4FXc77uHkkoyxfaH6cpECJRZckKnmI4BlcvxSCbgZ2b5deugfMRrcRN7htO0SyH2D2_GFjcu5TnwrYrHlEj6CqajYtGn2hmDGoJsOhnCR9Hl7omo18HEhrgRpe5by7r5ryztcyQGuwotLxUxUju5yQBCCEnm55YQQR-8Yvzv5W8BcV_Lokw7PiNUxzFsWl2wX0GnBH1UKzO4m9wC0Xi1EyNSDQpUIyHHeEZTN_mDZjM_wK7JwzWGtM5hkNe54pxkYU3vwS0rK-aTQNFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28443" target="_blank">📅 01:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=Ldel7drWStYvk1gW2WH-uiMHvaU9JMM5Lx9V5RPymhu3jAWRjkxra1uSemBbjz-VjDQJA9ZCRnsE7FceClqRafFlee667sGnNoZYXU3OVtOWPmQw5xoIhkxIb0zZew6POp0OrEdCDzXxxDvB3mKvRz9qTlB5c7q21RywFNEHRnq5LNivbf5WJL1uNfY8tuMeP_F5t7S1iBkn1bGLoJjvej4J3AdV3mJ0F7ntG4YSD8BZlg1uiBDjf2ogWalqP9W8jftowJ7drlz8WATZszDBPuDemp0ghmNGSCKDcoTA4Q0hkM_lkADvU1FbHXH9Kc-oKl2bxHUfjpenl7erSSBRV50XhN999ZqeNzQxDcqmxXIpxc3m5sWF8uTRhaQKFEFYAKz_iuENyjHuRnPQLvBcUxvhdPECYEPDhou4x0TtDZ54yBO6KjqPNQcRhmqDRA_vp6hqFKZm7nSjKVtHAJkdWlqmgDPf7ckoAjbPYj9wqS6cC00LvSDi2J4IvnNzEzvDVhOJ08Emms5QQSbXVVjDT5qb1ncyO_jRVKgqptacqZZ6dWLtnSGew4sdiUXUfw5H9thUH1uvY53TzWoP9YT55eUumpmzbQ-Tdt7rYlyDA_OM9Hrm0XJQn_XHsXysnPMFJ7KyHvsm_qbSvNSs2JJpNiftt8VS7JBYhrSDxqZdWMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=Ldel7drWStYvk1gW2WH-uiMHvaU9JMM5Lx9V5RPymhu3jAWRjkxra1uSemBbjz-VjDQJA9ZCRnsE7FceClqRafFlee667sGnNoZYXU3OVtOWPmQw5xoIhkxIb0zZew6POp0OrEdCDzXxxDvB3mKvRz9qTlB5c7q21RywFNEHRnq5LNivbf5WJL1uNfY8tuMeP_F5t7S1iBkn1bGLoJjvej4J3AdV3mJ0F7ntG4YSD8BZlg1uiBDjf2ogWalqP9W8jftowJ7drlz8WATZszDBPuDemp0ghmNGSCKDcoTA4Q0hkM_lkADvU1FbHXH9Kc-oKl2bxHUfjpenl7erSSBRV50XhN999ZqeNzQxDcqmxXIpxc3m5sWF8uTRhaQKFEFYAKz_iuENyjHuRnPQLvBcUxvhdPECYEPDhou4x0TtDZ54yBO6KjqPNQcRhmqDRA_vp6hqFKZm7nSjKVtHAJkdWlqmgDPf7ckoAjbPYj9wqS6cC00LvSDi2J4IvnNzEzvDVhOJ08Emms5QQSbXVVjDT5qb1ncyO_jRVKgqptacqZZ6dWLtnSGew4sdiUXUfw5H9thUH1uvY53TzWoP9YT55eUumpmzbQ-Tdt7rYlyDA_OM9Hrm0XJQn_XHsXysnPMFJ7KyHvsm_qbSvNSs2JJpNiftt8VS7JBYhrSDxqZdWMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛ پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28442" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28440">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr919tqYAGThE89u3jB4gqTzFSzDW_aSkCl7Mgch8VUbwAZ2AlD7PZXiHKcjBOf5m1SXcEI2G-YApqzdisJmIgfKolLX6T8QTD7vXC49EYwF6OwmZ-PHohBdKVcbYgwkR-OpFFR37tRpjP4ZDsxPu6iKeYv-3GBoIUnmQvXiSSEn1lXqi6KYMJp03ML7ztCEEf25u6n3qbaOTbD7-Au4TL73jZpiF-7zhGvG3BuGaeOgHrxF1lzvdKX2zTJM5lzpNEN5SZTQRfeMjJWsnY9UkzGWlMMgN3B_CfT_K6zDj69GaF-1YxszAes9KazRdo-DERbWBJd0j34CUlM9glYEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
فرصت صدرنشینی یاران کریس رونالدو با جدال مقابل الاتفاق در هفته سوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28440" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28439">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBerIplkiUyeAhKKnPEcKHLTT2GEANlLZAF6QAAm2ebhfsMIpvgSKsTxwgxzS2dPwMmz9Fo2puSaXGB8Qwe8Y-pwAySU-K76hWp94O9_D5rr2gEykVoP2vmqc3t519wlsnRonOZ0pJAJL7HmqbKOWEz0rk4Bh--Fe8EBi5IOWbNWEXtG5PYHsqIbwCE_8exbnYpLuauNFVf72J5MtuMoy6ws_7AANzpzgWtmmJreW6lakOpay4lpQXurgWHB6ppRMsir4Ss48TzCq5GpcpbKfIvpjteGiqWjPjeeU4j3V1F7DtNg3hcYGWYRMgwyB4imePtdDRjqh4nHCQhvnpJZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
شکست پرسپولیس مقابل تراکتوروبرد ژابی‌دراولین‌تجربه‌مربیگری درپریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28439" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28436">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=cFw9IvxoigiyT7wOJvQisJSGsh8hz-0yw17iK_n-dKjRQaQuMk0BAo801DHmn7ROcM8DKOGRX9eS5OBexfxpnImpawDu5KVVbv4Dq82CSJ7taiMNK588HNANYnno-JUmzkdPGTjaVyhVzDdqMqW_1GrwGwZVNgaLHnqvdB1OU5-bphOG2b9oTFlMLM9797mzgoTE6SVtbmOg0PVq3AbHYeygxfvLjq0YpF5q_9t1ddREWYQgpaH9qLrItOhIHrdfNWX3V2fdlWskodV9GKy7KjSEHikALMuoE1WypLyR6UAooPXaFmmNt87Mn91YPQxlawDj9-jolH_5f2Fg7MgX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=cFw9IvxoigiyT7wOJvQisJSGsh8hz-0yw17iK_n-dKjRQaQuMk0BAo801DHmn7ROcM8DKOGRX9eS5OBexfxpnImpawDu5KVVbv4Dq82CSJ7taiMNK588HNANYnno-JUmzkdPGTjaVyhVzDdqMqW_1GrwGwZVNgaLHnqvdB1OU5-bphOG2b9oTFlMLM9797mzgoTE6SVtbmOg0PVq3AbHYeygxfvLjq0YpF5q_9t1ddREWYQgpaH9qLrItOhIHrdfNWX3V2fdlWskodV9GKy7KjSEHikALMuoE1WypLyR6UAooPXaFmmNt87Mn91YPQxlawDj9-jolH_5f2Fg7MgX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
رامین رضاییان در اولین بازی‌اش برای فولاد به این شکل پاس گل داد و فولاد به گل دوم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28436" target="_blank">📅 00:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v65fD8bwItbKbxMDlLbE_tASLsxoBdz9GS-J0-AonoqDCaFgiBCHMdvu85A5sDs3L7ZCsEoLFctLmbpGuEho6-oIUlsNNRjw3aGfuTn8iy_GaVJjSUjPNvYJa9UAJ75CM45hOMmuFgGKeRUIEb7HCAt01sXMtbluipcdXF3-H-LdFaUiAxwJGWzF0jRWLr-jDn4KHFByayZWEg1DF0M5BkAnxr8P1jOGhuq9jEK-323ABA07ImxTsGFKyONAAgCFDXca-pqmaKwggEOHLgFK5BcKdb-uTp4N8O2EhflktCukZcEOczO3v0zIlYM7mPYo_ms5zkcoXYXNagBZy1kvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nz9qEA-d540dbyRjIORdoiq0XzytrK6M1Hg1WP14cdaEqKTa3nNyMNu1Y8rylnzETziH3bWNowJsUnSEoOJPYwy7RY0SLeaoRk45NEpzkn4_Ya5ogYjAnDqTF_d_VsQ4WIEQyo_spmV2dY4nbKr-VEA3-kFmFZOjydLdXIJNigvNLrTJJ_xa2VmzFCWzTY0vSZ3d7n_Opshv7Qx4PiI3VeXZgxNMyGr-CXhgPfyqAxc3553lBYer9Jv61BMu4WJcgWxcIainzuecAIQ2iU3u8bE2KM0nxfFKby-q7l48bCNq1FLVV9zj32z1Vj8VqTXYkVM-KIUuDazmeDFO3hzhcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛
پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28434" target="_blank">📅 00:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0N2iQEszvly7ISQrON4hmfwibZTYGOSS5ZSMg2ObNT31NTjvaGX6uBiRWaQKNy9xgmdRlEjF1VTsieuxDdLyb8uCmDVoLwlX_P6w2wWPJWMsdIqT35Oo6tRPYk7gZ8BtO2IU58vWnLmVbxRNcNpKdHFLWy6S6yixsuFkGQnCPuFlnwAmD5NbZa1euoboCabRlMyVAfuco3jA2hdVHdBO8b78iGhQSw6sPXFc_MCYy75LvawAD0l7rc4AvcgS48DnjSY0kt_2JHfve-nnEopA_2uRfFycDtlDRaVcpSmZdpbf1EAFAhoEMofdVVPrSvJNV1UqJZ6_dEdbffOspuO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/28433" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGLaN2xhhmMjrJTrAcULys82_hcsdwgOFyiWLNUe41UKUXvlq4S668mjA9QMf4NIz7AeRGPy4QBOcFssK3PZNGkETzwlc6Taq5kuTc4xXdMt5vb_Gic5CdtHSDH_86eDIx98pMrYKxRpMW42Xqr54cPP_l_b9SRWSFuW6mj425WKATHP3IiDJfOFS_15SG7nSi5lH4fSSANWoiLb7XzXUBMClT1L2ZsJHrRPI_I6HL7vDxur4BwTPnWdJgDeOj6x9_KSYdtpVOL6ikbfbeUO8i4dbwjEkEYIZvPOwdmvUed-VqL0680chW-1GrqbQ_Y4HExnnSQ9E4RkWXMPFNvKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مدیریت‌باشگاه‌پرسپولیس حمایت‌کامل خود را از مهدی‌تارتار سرمربی‌سرخ‌ها بعداز شگست مقابل تراکتور اعلام‌کرد؛ حدادی مدیرعامل تیم پرسپولیس اعلام کرد که کادرفنی تحت حمایت کامل اوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28432" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-ASx8HX_89CB_-Iq_eOH2GRp4W-lSbjyp_R3ZNX15hD3nYaDE6eeO_8mOd46a_Zg58hdnvVL_kzRhPpM9il2LGkFCZDSS3AaYrE20w4tAhkTkF3Wlh6GxfDviz1tGPpAkKUZ88laAPVmxojAHSVUo3bDj-h5693dnPWt3djbwmjkPvhzIX9lUybPkcTM3sI16me4pEyv1rV0SnTiODVKJ_5WL5EtIZcZe_0P-NqZwz_J_mce--gAtkUS1MewQHIK4RUchrMCD81V5bM1FWWFt_8UDZKWQC02jZ6vKtNmKUEvI46wv4gNZks-JxKt6_6zo7PJ5mHJOjNI04PUfd5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28431" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
