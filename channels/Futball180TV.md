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
<img src="https://cdn4.telesco.pe/file/LqoIAsZGMD8vZ99jof7rp0L3ax0M-39cYYtbHvnw_sQ35tuiiiUPqA2pWX6VbLz0WXvFh_0_Rtqmp9qq0X-OVXWFWXtmWz7f8FIP4SHOKfd3u7O2ytW4fNEuY31Yf-HiLcQxSYejPdE-GptiYVhC7G_N6645GnTibJf-lk0b__g_rtfN2OrjHSdCSrSdp0zB88WFlKJbGa4iVBbygBlo2jqvgXAbepptdSkopjCiNpBpqMxA5jZzfX-BqJvrpa2U63jTmwaFej-WHDHaqr5OXkt0XYkQK8-J3l8BUlQV1p21FcY0Sp3zuhnm11e_CMVDMB86XF4daJuLZdm_bB7z5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 161K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-90690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2IZK2AaFvJELp-xD1nBuQN7G9UN7dkGXE50LlWrP8itMGkf7sEmz6BX-wc2RIfVv-Z23Jcgu0yELR9CFfVAWeWbtJ_ms9Aa1rVujDT-1BfEAJ0K8-Pow6ZaP5GjxpwXofeu-U0t2AuB84Si4efBc_nALyDL_Ok9nNa3qt0TiTtm23GPqWtT3L7WnI9mgAZTYxcBQtIsk-efVMhysNnJJnYsUgquu8htxZhyxEqHbb6afy285E99tb4pByI2aO_TZVKTVoWOBOezBS0P1Ih99Es6SkMF31LDuGfr5fgTfj_HF6fnHzbi-4xsAE6E8EHUqBCKXeZ0YzLMyWCEuMmKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇧🇷
نیمار و مامی در حاشیه تمرینات برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/90690" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90689">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/90689" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90688">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9DSqRQOlSfWczAFAEzHpVRlIjWR7FHzPOFVzDjZ0dKlbdm-0xdA1a7vwmGHZKTClW-8Dh5OWmFLAIDKYIFa_CZkitrem01CF2BW0gJimr7WYO5WzEQccfHmL7Uh9MFjhavRnS_sGUxj3vA3114CNdqV2b6XRdh-de_HTTuOMrp45X5Te8rJJluf8_uBYP8RYqJAxNjfvyqWktcr3BjZ4vWKZt1dU5swrCwUKl6RbKAIz9htvG6QCndvlL7FtK-1ha9czLZnrTBrHITtLZ3rQ-4vtNQPXCseqnU5RPss6FrhXJRj6Bac7R-Uzs6nIZKzE7inYJ63xEFHfL9JjDspZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/90688" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW1pt7f_eq4HuOwWjR82iWfRL7gHokOoXH0sZ4Y-brrCELYrFbBrgIFZF58o6J3i84GZ6TCx3B0LEUek6R82segD52bY7m2cPr3R_tjxMWND-J6NaIjR1iRxWH4SLGKxu72pnOq1itSvWSw8t8EKU04Zdjs3svAixugV-A3MQRpXTWq4dVS9f3Nj0hp_68V3DX0CcscgDWKGbgTcivDIwTpiI_4m1KAe1zz465ocG4iVWrIZAmZciKvenpQYPT9fU5RL0rw-QWuD1TpI6Di5dwOzQQZ37-YbTTDkTJZUYC_39KrnWiHtt0aNjlLxWWfbYpytN_5GWQdeaHG2CPOdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇷
لیست‌نهایی ترکیه برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/90687" target="_blank">📅 12:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90686">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=FR6yZQEy0KNtByQP7kY7Mab28GKWblIHMMiKQhODC-8TT3YmqnDxZRxu8Cgvqjv4G9Rr-IfdI5pEVeyzN2cyujt5XuAiOkVBtHOado2YQH4lJZqVwnJCp3axw0yZvaqZ3uqDw3OvEro9RG4xuB3mrSbpTaFjjOxayPGVo01KKuz9ZhHopEZJn5xPkIABy3phKawItqrCNAdTTEpXPktBlr4_8SPAFSMVDZtsNXsPvUYn9T107NfTW9Yn7dwyf67J_JCzT70cqIZNtq7i5b3hfoE9pelDb4D1xr9hOCwQ9vTwsNnL-lT5nV7mlFAGlglEQ5YaOiSnz-ifGu0pyaiM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=FR6yZQEy0KNtByQP7kY7Mab28GKWblIHMMiKQhODC-8TT3YmqnDxZRxu8Cgvqjv4G9Rr-IfdI5pEVeyzN2cyujt5XuAiOkVBtHOado2YQH4lJZqVwnJCp3axw0yZvaqZ3uqDw3OvEro9RG4xuB3mrSbpTaFjjOxayPGVo01KKuz9ZhHopEZJn5xPkIABy3phKawItqrCNAdTTEpXPktBlr4_8SPAFSMVDZtsNXsPvUYn9T107NfTW9Yn7dwyf67J_JCzT70cqIZNtq7i5b3hfoE9pelDb4D1xr9hOCwQ9vTwsNnL-lT5nV7mlFAGlglEQ5YaOiSnz-ifGu0pyaiM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
⭐️
یوونتوس ده‌سال پیش یه ستاره‌ای داشت به نام آرتور ویدال که اینجوری پنالتی میزد و رد خور نداشت سر گل شدنش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/90686" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90685">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/90685" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6tkA-q6Hqpi8NcIfSmFP_-kDeEQKkHteEglo4wWBelim3-_Sh6vyEdHw7vZZglaY8O93ablJPjXfvZGEKSyUKw4oBhAuNDZbnqIZ9AN1XWxrRQnpzRW5lNd1dm_J1L57_HompWD8jRACh_YAmzDPQNiihgmycSiBoa3ZKv3w-GcG47Eu4ifshcqzQQgfz85HxHC_ILI6FVxXiebY77Pv1bQfsKpxde5zDquhlj5RWAk4R8DafJz8ZVVKXxhywGh9bi4GPJ15j-sqII0_INLE-fG8SCPvNvK4mGubaDqO1xL8L_ifTk5ZFHChvsUmQVNT2isgc3PuiO0NLqcSJEPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/90684" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi_Px6QDG4iPcfiRDv-Yf0tUC29dXqjOoXWClp-wK4z9ca-5wrSACl6Gn2LpARgYrJ7Hyxb__SSTC8nKheIzeVc4VXL65iYly-HRIwJjaGe6LrSjSRISyWOUdAATLy5NYjaldJaxvUgZeduOBcLO0srMfuyc8kSccURg9Xluszjwc7OcGGv2NGRcfnykmvGkN6dmagdMrbncdw-iTz35T6EYvcS5xjD-winNISlf5jB5s9fQCbYe7DjoqBsMKBUCW4OUO_G3xwwpbRP9S__uwzHBBk6K5ALHmV3eObZW7tLy7qYYOLrlyXH2HPYyXJUlwrkEByFVCjr3Ka0sprWsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو: آندونی ایرائولا به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/90683" target="_blank">📅 12:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYn08tf6IcxxI2hF2MzysqeavMHMdKyFoIjn8yVEQ7Ak-vTPVE19Co5MUqmKoXmK9K4j3s7HMuKhEznqzBfrHHQx6LVuv96oHaHV504fYYlnR8bdmYskNV9ok7t9fiuKigL6vS-1vbtF09goHmzQUIPSk0TwXjZWrR0krCmYfAYvR0zjZGgscxe7GI4yOecTqk43L8GfGT-FlMoRxB0TqJxV8Jc_89ezzEgFC7ZGHlsX-dM_eVbk1mhOo_7mmR8AR7nvGpmqG_d3R4Mfjc464j-lrNRzC8oi45Clwp9eN04Q69mvW1S7zyefzJ_bRuTAK8AwpgbRHJKHcj-M7slqhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90682" target="_blank">📅 12:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=AMidSdx2ELF4OpKYsraRLW24fedXDAO545GBzepHUjnWubA3cVoE982yAY-UAyQqkxZ4NB2KrDYwk7fihaOds4FxGACmjuO8RG_ex_yDz_f7_w-PAH10rNrKLCUeJkpRW5FEdMTqkufyFV5dhtOmhLOk_3b82nOJlBp5tz1xvrVP1bLYTYXb6y-0qqlm-eKjFKyKNrZmAVDgNQhcqdHorkzrC90hSU3oiNC7ZGCxjs_jNyQRfIk7sFfkqnEZzyhUI5JY5uEFwuj7DtXsSl5Od96HiOOyyhiaXhvaZG2ztr3Nzi5SBhKDrszgcQlwlpSJTqmAzcKrHGKhyqd9OLmFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=AMidSdx2ELF4OpKYsraRLW24fedXDAO545GBzepHUjnWubA3cVoE982yAY-UAyQqkxZ4NB2KrDYwk7fihaOds4FxGACmjuO8RG_ex_yDz_f7_w-PAH10rNrKLCUeJkpRW5FEdMTqkufyFV5dhtOmhLOk_3b82nOJlBp5tz1xvrVP1bLYTYXb6y-0qqlm-eKjFKyKNrZmAVDgNQhcqdHorkzrC90hSU3oiNC7ZGCxjs_jNyQRfIk7sFfkqnEZzyhUI5JY5uEFwuj7DtXsSl5Od96HiOOyyhiaXhvaZG2ztr3Nzi5SBhKDrszgcQlwlpSJTqmAzcKrHGKhyqd9OLmFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇽
مهدی‌تاج: ما کاری نداریم مردم مکزیک مواد فروش یا هرچیزی فروش هستن
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/90681" target="_blank">📅 12:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw3buVRaegPUwq9VHNsmWGAhDNy-jC9M9axH9O_bW3IbXf-2JD11fdr_4yKY1PZShIeQ5xCYL85YlgX7Yy4IRH8ihZi-JNke8kGljQoQMXWzTWlOhImQM-HwJuu67uctVS8J8uu6CkV0zNoU1Iz6aerT533xfn2ZIINhJbQvmFnCayd48-LRAt77rnZM7sG5D2OqNt_PBJaxf-sTP6njm58z4CiXvL4idKWrVEDoOeGAUjC6C5EpzBzwGS1z0CsvmNXOLiuUN7LE-P2RV5Imc60-D9dCseNszRWnf5rqTwgkt_7fd2R2IRNywrwS60_Abiw-_e6CPv4JYmuBIHFf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که جام‌جهانی رو از صداوسیما دنبال میکنن باز باید این دو تا نچسب رو تحمل کنن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90680" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=hrdKalsruWuP9UWLpPKa3YOlHUNeV5U4mqBEakHKevlxjpNSBhst56Xi2cQ-cJuRj-N-WASZviNo4oO-h5YsFqoeY4GSJU98881NllA6EG5ENlC6Z-TaPDH61ZoJEAsSR75obByjBVom49ABU1CyMftsIiEVef4uuv7E5K_5jVelaf5pIeLUtq8zlUKcjyc2RdNm1nfpgs4ZpU5NNdykjStRWFJk8Jmj2qreiw-HtA7okpW-NYL9DtfcjgfNcnntS46_EKw9yZ5pHRTCtRd6-nfbjkl8MR9k6O94qZtUbAPGXZ1e1jii8oV8bsZSet0NqD8Oqvzz6WkveU-Pj805TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=hrdKalsruWuP9UWLpPKa3YOlHUNeV5U4mqBEakHKevlxjpNSBhst56Xi2cQ-cJuRj-N-WASZviNo4oO-h5YsFqoeY4GSJU98881NllA6EG5ENlC6Z-TaPDH61ZoJEAsSR75obByjBVom49ABU1CyMftsIiEVef4uuv7E5K_5jVelaf5pIeLUtq8zlUKcjyc2RdNm1nfpgs4ZpU5NNdykjStRWFJk8Jmj2qreiw-HtA7okpW-NYL9DtfcjgfNcnntS46_EKw9yZ5pHRTCtRd6-nfbjkl8MR9k6O94qZtUbAPGXZ1e1jii8oV8bsZSet0NqD8Oqvzz6WkveU-Pj805TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇺🇸
فرهاد کاظمی مربی سابق لیگ‌برتر: وقتی شعار مرگ بر آمریکا میدید دیگه نباید گدایی ویزا آمریکا رو داشته باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/90679" target="_blank">📅 12:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=jm3xPntwevJvXV2vQ-V3VrVDgVgAoqpVdMLIR4YvyvdedF8xfxTDj39dxXv3uXzP3Q5v8Gm3D3zZ5RhcGdPiYd9k30rgfTCUywIYzTZtuqpeBQ5vUnZEx7btslY6Vb4e21Bu4RmH2Deh5NSwRV8dmR1tzYW0DyUoIi41fDa9lVMsnXF-2lKd0__C_G5udB-MdCRnJ7S-f5_XkcmsVc47j3yV2txaG7RbSahEDBPfx0UWUitaAWOTjxMCcgpEFAhBQTD9uJ-oi1UuHssW9YfDvmOSlmpj3J6e_UTonPpMTVSuoyyOAtiw4IfX38Flr-qcxxakjnPnOzuNqTZLcnwhNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=jm3xPntwevJvXV2vQ-V3VrVDgVgAoqpVdMLIR4YvyvdedF8xfxTDj39dxXv3uXzP3Q5v8Gm3D3zZ5RhcGdPiYd9k30rgfTCUywIYzTZtuqpeBQ5vUnZEx7btslY6Vb4e21Bu4RmH2Deh5NSwRV8dmR1tzYW0DyUoIi41fDa9lVMsnXF-2lKd0__C_G5udB-MdCRnJ7S-f5_XkcmsVc47j3yV2txaG7RbSahEDBPfx0UWUitaAWOTjxMCcgpEFAhBQTD9uJ-oi1UuHssW9YfDvmOSlmpj3J6e_UTonPpMTVSuoyyOAtiw4IfX38Flr-qcxxakjnPnOzuNqTZLcnwhNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب خداروشکر تو این مورد هم عقب نموندیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/90678" target="_blank">📅 11:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90674">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ef18n9K8WNVnH92lCrPqIpSBTAtQf7q1NUz87_wZ8xkm8l7_NRsdyiz6UDFs803u84PaFOCVBe5I4w3bzqvw47BZJValmIuF35erjoC4bpbJDDUtC-NNP2uEr60WNb4K4rdxXdK-LXlNu7XjYdZtKYlymrhSz1GNcU-wnI1YUnBs7fDPNeMthTxEusPJr5ZIiQWuK8nt0ULwbuRvf5cveVyXEcvgWrIKpEqmmcBtCx0jP_zWeYMvUm5oDeX1UECo78LEDaZKXfy07---5A5JoKSFAt_14q6eiJh0dbWCGRh0kgthWYuzQHmXeLQVEjucSzoVFgd1lEtVE04bb7MZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tjuReVv18yZb39m1RrkUGxd1gHt6_Rmh2vZ8T2uMeieDDyzQ6bOsA8Q93fmvyaZTLufXZhX5gbXxRGXfHpYyf3e7p44wSHmd36ZjfnO1ZJs0VoCohuTrKk-GOFgrKUcU7Az6KEs9j4b0P613tfVrtN78_O-k1lbDBYh7atJNem3VtWPwBOJ17oOKmrBj9LuIgBWIK5iIl4Ag4YsjQXXIkxtjgOyw0tpdTb-zmkQD6B3_0PGX-vEpWQQ3Ft5K7IucbTdKLwpLTE7mLtovMvvRYFEespCryLIKGSpL424rFocBKIyiz8dTlDG-bKJ2F0g-pAq3XZsogS6vl7FbgE2OLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9-c2KtEdGgqpF8g6LLs9zpdF2g2FC0MQ6h7e11rCML_86S61JvEBRTPk0-vohz9Tzm5d-SjWwnz8NgLU8HN-hBDgXEt9PcZqGY3Q8Ot-BzcOE28n6EfSd-XWXbu0sAsnQyX9NaqHyocDr8tpT4o8stNDrXjDn1lwF0kS_6U97eSAa5IUrEF607hze1FJR-TPSDrZr5d4togtEZeiJFGh6WJB-PlmBbrVqCx_Tp8SWpkfw92vTF5EyKD8IkRrwBUMjmdun3It-fInEjcFbybjDBWGnGIRpgd4K5dBmP68LhrZSjYFL6jPnXFkkKkFIftcTVDOAK97GQIPVo4mYFxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQU3ZuOAxiNvkeq8uMb3gkdjqUVSmAQBpBnuZZ7i1pmrxO7M7Nip1_e_HvxFs2woS31RQVX_83xQHCZ-dnhcxvPEjBgm_dNYZ0zPU9wcCSlDTm2i4z9FuqFoso66IlCc1jSysy28F4h_xH6SkHTEyZ8nrwCFcdhtmADdFH976wZqQibrF_XhmDvioXL0uIopItP7WKtDx4BAh77dnMTICuXUvdU98ogZDReXG3hFumTEnY8eSAQEvV6sV-72MSi7IeQuU8V5qlJX8XJNbiwccsPwtr3eYLKRKsJvQid1Np-_9ZnMTjYxUxViLIeKxNzj1Dea3-uNfvRm_xXqBvdnfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
آدیداس از طرح استوک‌های جدیدش برای جام‌جهانی رونمایی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/90674" target="_blank">📅 11:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90673">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=aE6D2XUqeEqGsXksDgtXu6y93Z9uYMzrcbcOth216F10z3bzs-5jsmCRVV85UbGIhnWWUw8NwXbcwTyvNZmPAADzvCLNw-O5EXwbcCTyno2rDgXo0TMb7CrrUj1Tz4eOz6N4-lO6uczYK2GRGr9L6r0aWQECegkY1Z2_tKD27fQW960oyihCKx1OB-F-M1IPw_DmFH6YdEvh7XRVGILKaO1j2AedhBcrkd1ypSXJUgnyrXZ6Z2J_ZuyJIo1BQFo8bvFSzh4qStqEQMKiTrVJZGTadaaSZsG0B2HJkd6ILrQifpl5XpwgMKBK_uIvC4xK2TjLR4u9CHBT-_yIj_3IYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=aE6D2XUqeEqGsXksDgtXu6y93Z9uYMzrcbcOth216F10z3bzs-5jsmCRVV85UbGIhnWWUw8NwXbcwTyvNZmPAADzvCLNw-O5EXwbcCTyno2rDgXo0TMb7CrrUj1Tz4eOz6N4-lO6uczYK2GRGr9L6r0aWQECegkY1Z2_tKD27fQW960oyihCKx1OB-F-M1IPw_DmFH6YdEvh7XRVGILKaO1j2AedhBcrkd1ypSXJUgnyrXZ6Z2J_ZuyJIo1BQFo8bvFSzh4qStqEQMKiTrVJZGTadaaSZsG0B2HJkd6ILrQifpl5XpwgMKBK_uIvC4xK2TjLR4u9CHBT-_yIj_3IYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بدل‌های کسخل و ایرانی مسی و رونالدو:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/90673" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90672">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHVoUU1r5iDfuddU4Pwlvwbxw1IoXXgoFw68_PJcnkZcKLDq0g0ssGAbJp36W5zYf16GnGseQoUs2P6KpohVzPDwDdazxh6k3rhGqQFdAyta4ibKsjAo7hOuXDx1E7Wi8XMXXRJiVCgsTxnW2cl9oMLvvITSK_RAItHKbhH5Jgr959gxquC-lBj5CYnD_ctFYkb_T_gcgdekSM6W5sZgjWIGah6A4yLwW7q_Kr2ohsKsBtyy55-GQAobEO7Mj8vP6lN1GQ39wjYc30qI3RIRnOJeYXj8Fn9l8Ka4VaPYo3UQ14kXjQ8sY0d0HkFhvRMOeWQjcJHPeNr_CJE6KWoLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی سکسی گارناچو
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/Futball180TV/90672" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90671">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=ba57hU0clsd47O0HeCxN-XRJuzHrrwwzhkKBYTUYflE1OITu2nyGqZ0BRw1bZyNFqGqNUdQa8-OPDic6X1-Ch2K292ykpI1lq7glTA2w4KXXn9O7NrBB1mq7h_rLi03_l2CZ4Erre960Evj6NRftWOI-WuVnFTdUfcoxI1VhcMPGCkc7VAbdeCfOTRP5uHbsolxN4NlE2y2wFLaAHF1PIiLfWyknmAi24H7MhKAr01t-uFquUE6t7wK6MJbIw_gj_URbU0ZDFn6nCq-HUeLjygqSMCrhKbiR4Fib--SBlJVHbKU4xxTJA5dxiNqxLzV7tarZvAHRM2J7zJgT228_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=ba57hU0clsd47O0HeCxN-XRJuzHrrwwzhkKBYTUYflE1OITu2nyGqZ0BRw1bZyNFqGqNUdQa8-OPDic6X1-Ch2K292ykpI1lq7glTA2w4KXXn9O7NrBB1mq7h_rLi03_l2CZ4Erre960Evj6NRftWOI-WuVnFTdUfcoxI1VhcMPGCkc7VAbdeCfOTRP5uHbsolxN4NlE2y2wFLaAHF1PIiLfWyknmAi24H7MhKAr01t-uFquUE6t7wK6MJbIw_gj_URbU0ZDFn6nCq-HUeLjygqSMCrhKbiR4Fib--SBlJVHbKU4xxTJA5dxiNqxLzV7tarZvAHRM2J7zJgT228_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
🇸🇳
ویدیوی جنجالی از بازی پریشب آمریکا و سنگال که شدیدا بوی نژادپرستی میده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/90671" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90670">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=pIMyLM8wEu6-FFu-wNgc586diaLWanI57A8w9y7GdpPUkyg-nA4LYq0UfnMe7aNTZ3VhiO8MFzHR5TiW4qOMuAcE86I4nEuU7bebIyvHZRI4DsdAwmc1dzwJagywPQDQTU75J-NwLMSPGAjnfzCCGzKIVlc3u3HYRIvHEFNh4_9dLaT-9jRUax4PQ3XzpOL_qX_SoV0-n5qFJprWnzl_2Gq9u6JBcAs442SgAm7dI-GxB7FkKmKlyslgqzWZkisv5HDa2_li3HAQmpiv9SpmDgTJM5ucNESeQ2qbT_XffFH9DZMePBuf8Bp2w4RIA1jSom_61m5KDBDFR788uxwd4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=pIMyLM8wEu6-FFu-wNgc586diaLWanI57A8w9y7GdpPUkyg-nA4LYq0UfnMe7aNTZ3VhiO8MFzHR5TiW4qOMuAcE86I4nEuU7bebIyvHZRI4DsdAwmc1dzwJagywPQDQTU75J-NwLMSPGAjnfzCCGzKIVlc3u3HYRIvHEFNh4_9dLaT-9jRUax4PQ3XzpOL_qX_SoV0-n5qFJprWnzl_2Gq9u6JBcAs442SgAm7dI-GxB7FkKmKlyslgqzWZkisv5HDa2_li3HAQmpiv9SpmDgTJM5ucNESeQ2qbT_XffFH9DZMePBuf8Bp2w4RIA1jSom_61m5KDBDFR788uxwd4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇧🇷
صحنه پاره‌کننده از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن بود
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/90670" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90669">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=bR1HwwHkpp1oMmYRxSmAKd8Lu5zNgJLv2MMI694l7KqSfz4cNRKjBGOK36rfSuy9gTWcENQLY9svsDJVrwg6V116-CxngV4qp1XhDzqirrs4EyCltlJeTaTTdGSoKtlAP1ZF_zSmDipJx5Vu0_wjdScd0qPA1jOdh6BiGR7mD2P-NB5seotsbR_yfmoWZEtYuIcfI6HQI_k5XQRY7glcpkRDwDHn270Qw78mWBJ6IX7-ANBZ81_5DRqmJ7VlqtISyId0vPrJDWUKt5vXi9xSlMSuEeoL_CvT3VwE_1iHnkFp_B59HLgVBpju6NAXN-zrLdS2vkqokbbXQkfpjZq52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=bR1HwwHkpp1oMmYRxSmAKd8Lu5zNgJLv2MMI694l7KqSfz4cNRKjBGOK36rfSuy9gTWcENQLY9svsDJVrwg6V116-CxngV4qp1XhDzqirrs4EyCltlJeTaTTdGSoKtlAP1ZF_zSmDipJx5Vu0_wjdScd0qPA1jOdh6BiGR7mD2P-NB5seotsbR_yfmoWZEtYuIcfI6HQI_k5XQRY7glcpkRDwDHn270Qw78mWBJ6IX7-ANBZ81_5DRqmJ7VlqtISyId0vPrJDWUKt5vXi9xSlMSuEeoL_CvT3VwE_1iHnkFp_B59HLgVBpju6NAXN-zrLdS2vkqokbbXQkfpjZq52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید هم واسه جام جهانی آهنگ خونده
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/Futball180TV/90669" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90668">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJrd3jqbGv63LbER7R7Mb1VB-gzS7B28imAl_nRTLAef7aQg8ntdlN9iYJV7bnsAQS7NS1QF2JXCRBAZfnqZ6v-TSly_l_aCgJ9JdvPQ2AuYw1t_lnAwNdkUhSaedLUHP6KHZROc1jcjelS4rIMPrJZUh3YXJ2k8odDL2qzB0g9PeGzfksT0FQ-NG8hTwUR6PgVSS7iILVuSN0XW614NAjx0FuncHNRsRSIKZVGtx0RW-Bh1tsq9qXLr-3rFCCoM-mqxYqDfEwynhe0R-yCgZAXQ8snbhKkfSYxJwxDrlyO-XZMG4F2btmHXGfKpVITJurU0RhsQXDPoAhjhxfZnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول چلسی در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/Futball180TV/90668" target="_blank">📅 10:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90667">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW6TB8OiZUHPArBFPkbq2Qa8uytvHVp7ofoXS2AISP2YYIBUb5eAOsCj3Gboq3R2TB5szEXGMWkgI5VpGoqgv0pO_aqXUyy6CbKsCT4BMN_C4IGr9OzeL2Cr2gD0I7lyylWaY9DYUGlRVeelbuRTwm150KMMku6_fHz-odShcZgblxbJxku2QXZv5qB-BGgGscyUNkUH6wZap5ngGNOzc_P8pRDEE2Vo2muNnkbkP4gPYtZRlcOOE1WOA2lK0vuugJs9jARBG1TfEAncct71TYkJREOkhfv2FnVmKRvk3T6_JWRkU8D5nTdrwNwY39B9DVLuENbidvBEV06MGM32zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد دمبله در سه‌تیم مختلف؛ معنی واقعی شفا یافته رو در تصویر می‌بینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/Futball180TV/90667" target="_blank">📅 10:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90666">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=LWAxBatX1Ey3ZWMD3vLMNcf_sfPNqdOwaqnvL1Yu3wTR0UpRseZH2qsuDpM9Zlm7XLBdqX_xlDRaQ_ivVN63bSpoiH3BJdGmF1TV3La5NMGVwM_3Kzn3ehG0qQ7StwqsELWFgQtsudfr1Ow-JDifkbFEYDVMJIaOdjehzAwvhLWUCaR7rfnJYND-dQZLfXe5g24NF7VHOACI1OXKmn5uIpbQxsjkTIGYBvrugo7WX3PKv2oxxn8mYRJyV5Ryw3hM2HHZ0TJv6vkIP8692ijar_x1gL6ZiXoE6_2e7gm4eE9Mg0uY2o9K0_hJ-4MotuNk7AJ9lAZqT41wF0GWC_LslxDvRGWi6kVpfawJm4kE7nH7c6Is9gVpndWKXHFplD1852uIRQGdRjq1rdFTyvAgRMlSQLZpVqseFebd8hTWq0lWWRCsJbAQm1Y5-bkqu0n86G3DfRjJ8CPXn3LM7hk_RfSOvcDIS1jCP_Q5K-iwQBU50zwP2OW9n3F8m4XiT5TFn-Yuq14t3G56bwA9ZuAOKfUtakgDhM3z53GgzoHCHmKBQix3li80I-fY1kOx4kx8QXgKnXhwHNebFKuJvj5DGZ_nNRKHg4IiF_SJOKWZoNedb-c5v3SM-IbP5VirS-NUkOk7gMtGRJOC3jcsMvkTTGJ27lFn-csnUYAylUxPo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=LWAxBatX1Ey3ZWMD3vLMNcf_sfPNqdOwaqnvL1Yu3wTR0UpRseZH2qsuDpM9Zlm7XLBdqX_xlDRaQ_ivVN63bSpoiH3BJdGmF1TV3La5NMGVwM_3Kzn3ehG0qQ7StwqsELWFgQtsudfr1Ow-JDifkbFEYDVMJIaOdjehzAwvhLWUCaR7rfnJYND-dQZLfXe5g24NF7VHOACI1OXKmn5uIpbQxsjkTIGYBvrugo7WX3PKv2oxxn8mYRJyV5Ryw3hM2HHZ0TJv6vkIP8692ijar_x1gL6ZiXoE6_2e7gm4eE9Mg0uY2o9K0_hJ-4MotuNk7AJ9lAZqT41wF0GWC_LslxDvRGWi6kVpfawJm4kE7nH7c6Is9gVpndWKXHFplD1852uIRQGdRjq1rdFTyvAgRMlSQLZpVqseFebd8hTWq0lWWRCsJbAQm1Y5-bkqu0n86G3DfRjJ8CPXn3LM7hk_RfSOvcDIS1jCP_Q5K-iwQBU50zwP2OW9n3F8m4XiT5TFn-Yuq14t3G56bwA9ZuAOKfUtakgDhM3z53GgzoHCHmKBQix3li80I-fY1kOx4kx8QXgKnXhwHNebFKuJvj5DGZ_nNRKHg4IiF_SJOKWZoNedb-c5v3SM-IbP5VirS-NUkOk7gMtGRJOC3jcsMvkTTGJ27lFn-csnUYAylUxPo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
استفاده از گاز اشک‌آور توسط ماموران در بازی دیروز بندرعامری و شهرآرکا البرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/90666" target="_blank">📅 10:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90665">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QanqcNjQQUjTzVLVtOa0wCwS6LC6p21NjUiDwT6qx7E1EbDWCaD-os_pVcUobaPrbWPP1psQ90XsrPCfo8dXuskP9iAMTyc-3pBmdmh59_04yrsxYPJxxYwZ8uCMUnLPoTuEwf31uiM4CxYQpQomy4Yy5j27C9op47dNzlRxCP1GXb0BMOmSzeW4Gb4NwjVNbY4V6qFnsInUgacI5jmRtTK5usfGMuX-KAe34TojiNJuqTa6gLDvY7lxbYBOlBRMQtnVv9H3gCKw863DW6x4rkN3Le4mM5LNvImHMGPnaSuSZIeg_eJ0iCvBlGwpwrjLIgWth2e6pYR3A-YZZn9C1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 بازیکن برتر حاضر در جام جهانی از دید FOX
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/90665" target="_blank">📅 10:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95b443280.mp4?token=pzu1LAmaLCG7YPARSY_TI2_QPdknq_TSYOe5q0FU1Fw1nia51jn3RuTz7ymbhWoSFtgFdbTGDMmo-OHuSHHCAGLUS3tuala3Pz0hgSKPUIgLOnA-Rdl_KctQNGkeUTwS6yXhIYLfQG1gjDqTcnxkMWkcd0LCYlBvywu0HSUU1JxOc0LUbPN2bZUPqFjw3fCNsM1Yofu0pgG-5tPw69Ive3XM6nSRbMVAHA7km6JCKupTVJPfQljoYtmX3yw0HP6SEB11bN35kihBLo4_-CkVH_U3UzVF03-gYrbvCYtbZnuw2mvJlnPZ3TLH4NNrGlbw_2q9eJ8iBXRBU63ebh08vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95b443280.mp4?token=pzu1LAmaLCG7YPARSY_TI2_QPdknq_TSYOe5q0FU1Fw1nia51jn3RuTz7ymbhWoSFtgFdbTGDMmo-OHuSHHCAGLUS3tuala3Pz0hgSKPUIgLOnA-Rdl_KctQNGkeUTwS6yXhIYLfQG1gjDqTcnxkMWkcd0LCYlBvywu0HSUU1JxOc0LUbPN2bZUPqFjw3fCNsM1Yofu0pgG-5tPw69Ive3XM6nSRbMVAHA7km6JCKupTVJPfQljoYtmX3yw0HP6SEB11bN35kihBLo4_-CkVH_U3UzVF03-gYrbvCYtbZnuw2mvJlnPZ3TLH4NNrGlbw_2q9eJ8iBXRBU63ebh08vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از لامین‌یامال در آستانه جام‌جهانی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/90664" target="_blank">📅 09:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90663">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7uYGy6gkTlqlAIY-yxoDWi0JUXa4ucVXrpg7i8LR0EGMsb5eXqcfZVBRVNV3KCTfyZ1ubrJ7Yp_bIZd2n9gL91N2rok5CZF0qFpjSH5R_rF6bnkTi1fY110AG6GCVma0yokW5cHyDuQrOjRu9_u5c_ujdWqishCtouYRWGxd6MKW-ekE40tryxBOUTRvN_4hzvlI47H_1CepvIMlYkt0tWmhgZ58h5FVxOWNLPi-AHIY7KNqWarojyoxu6K1yag8vwC1dFxjRBAnLrbAMAN-8SS2bx9g6ml2y2D7GqrvjdRs2z6arEhMvlt3I1TVdRVwWoJqXvpGD49IpjcQyIgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⁉️
🏆
پیش‌بینی اوپتا از قهرمان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/Futball180TV/90663" target="_blank">📅 09:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90662">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏆
نماد کشورهای مختلف در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/90662" target="_blank">📅 09:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLhg5yLbX7kEFYtdNmeaGswwndVecN7X1BereawayZuO1nZ6vfu2P3viUQziZURmzKgzQCcwD29aKaU46EjQnOaBPVyDFW2nL2SG_1aA0or2squZ7bQGP2sMC2CdH8JgQap7In8qBbJCCINLSk0xXNUUHR3D8zf5VjZZ1dVlSA3emQv5toN0y1IhnpWZE0P-xRsPAChVK3ScDnCyjvPDk2-A0IlYjlYZ4SQyv6PbvGlM_5wzCoth5uXFj6DDC4GYK5PAkE6ePNGSt9dttP_xvwEJrqMsIsATqq9Zpv1YVetrM00pxioeAuBuC6s9xD978EiOhfnxexqJKkHUS4BO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال و رقیب پرز
: به محض انتخاب شدنم، خرید رودری قطعی میشه. هالند گزینه بعدی و حتمی هست که به مادرید میاد. سرمربی رئال کسی بجز مورینیو انتخاب میکنم و از بین افرادی هست که الان تیم داره!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/90661" target="_blank">📅 09:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90660">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=ceLg2Aaxa0fMTqH4fBy_gf3v1R-Sw8IcQ8UCB4b6itqs2m9izf2HbhH032LnFwMDcKG8JSUo-wpDa79zEJbWrBiLfXrma4KuQuwMa0tN2dcx_OvQf14VysDIBVGxicOvkfen5Hd3Rc4QsAX0d32fggTAkf2Qg65MiMEOohTt-yL1RpCcAIH8sbX6rOuMWqM7so26FELuvYR5QmnzFhKu2aSdnqO_rJa7IFMMQOE-mpYxFfnjIhAbQLl27eTPXOsdHa-y-INA54228_y4odfxaZR1tsIg-Xx12ybSGHRFjS9JtlU-jHuT8tsaOuPV1SCsAxzrJi5Pdo6lGeiuV7nKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=ceLg2Aaxa0fMTqH4fBy_gf3v1R-Sw8IcQ8UCB4b6itqs2m9izf2HbhH032LnFwMDcKG8JSUo-wpDa79zEJbWrBiLfXrma4KuQuwMa0tN2dcx_OvQf14VysDIBVGxicOvkfen5Hd3Rc4QsAX0d32fggTAkf2Qg65MiMEOohTt-yL1RpCcAIH8sbX6rOuMWqM7so26FELuvYR5QmnzFhKu2aSdnqO_rJa7IFMMQOE-mpYxFfnjIhAbQLl27eTPXOsdHa-y-INA54228_y4odfxaZR1tsIg-Xx12ybSGHRFjS9JtlU-jHuT8tsaOuPV1SCsAxzrJi5Pdo6lGeiuV7nKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
ویدیو منتشر شده از یک زائر ایرانی در مراسم حج که در فضای مجازی وایرال شده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90660" target="_blank">📅 08:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90659">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=VYff1E4bBh095A0x3V4K1wRcuLoTvBMHlQw_rGNG4PLWlNjFUuhhPOpGXsmKkM99HP2TTViszNZQ-DT9xoImCS3Pi0dAJWpZJexymBko34RlIbHKsITcWVy7JF_o_xLW61e4IUpw9_XzBx8gOsvXKsvpq5EYyjS-Jr2NMoENqovs19_lxtahzsNVRWvVfdp37h-_htdy5CemLsDO-0S9x6_gTR9niyNkl6Ing35MINpkWuPeiVqjlL3AvBeJZ_-525n50Qa3jcIIQKvxml1YJihogFHV4AI0a8og1BM3zDo9pUD8HV4AUmMrQTsLLk67FkSrY7-FC5SufalOMurmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=VYff1E4bBh095A0x3V4K1wRcuLoTvBMHlQw_rGNG4PLWlNjFUuhhPOpGXsmKkM99HP2TTViszNZQ-DT9xoImCS3Pi0dAJWpZJexymBko34RlIbHKsITcWVy7JF_o_xLW61e4IUpw9_XzBx8gOsvXKsvpq5EYyjS-Jr2NMoENqovs19_lxtahzsNVRWvVfdp37h-_htdy5CemLsDO-0S9x6_gTR9niyNkl6Ing35MINpkWuPeiVqjlL3AvBeJZ_-525n50Qa3jcIIQKvxml1YJihogFHV4AI0a8og1BM3zDo9pUD8HV4AUmMrQTsLLk67FkSrY7-FC5SufalOMurmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
حمله شدید‌اللحن مجری بی‌ادب صداوسیما به مجریان معروفی که قرار است ویژه برنامه جام‌جهانی را اجرا کنند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90659" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90658">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsgcYzipWjwxdNfjK5_0Y9bYuWQse2VOZIlokDm_tiwTsUv-tqJ5HKwveJtFNrNCxYxjoRu0dy0vAS-pgXg2KJONxC79ZBVYU_BKNl3oK210sXZsGvFvApN87csQHU2Vtre_nLTNmwozI1sgP92Vf2Xshko-Q-EKPp4kIY4hcWXSzM3-5Y0IoRshhS3dkLFr8-ZQBA3caBz_Um8z2u8ktT_5ViCm_xavT3zjsqvtO2kVrsZ8uhV9Jqo67N2RmqdS3dU2iRmkXx1j20X0ckyC5aeyRZep4ZNTzK0AtmozRkiVUbmvb8nnXeZruZaHQJUR5n4AOJ69woHv7scUBMeZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
یک‌رسانه ورزشی برزیلی اومده جام‌جهانی رو پیش بینی کرده که در نهایت نتیجش این شده که در تصویر می‌بینید. موافقید
👍
یا نه
👎
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90658" target="_blank">📅 02:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njCRvZ5AF5hhHDHkV1EnCjxZ0UV_ZqWEw1v0DpEJFf_YXZCHaHob0bu-qgeelcfZHwCmSH5EP81_kLPT8DKw7d8ZqDKOBNoNxxv9kD6ySCgm4T3qK3SnKGTVwRITxPPjnAYfj1KmjhmKgsDsdp9l8RlC3mVZFq16gT57-LoTS-nGJgAWk72YUL8Ac7gMlzFxmgzCXeI3PhNSuYZL2ptBTF6UAcUsDaLJz2BxO69rFJZbU3rG2FVOHaTgxj7scSrvTQmR1AqlGPVCrcmwx2FIT4JDwpGdoiaCp9-XcQuyd-FG-RUWBzV4r2CqcK-el9_yRqjtIJc2gGfaYg8gcVCmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚫️
#نقل‌وانتقالات
؛
یوونتوس به دستور اسپالتی خواستار جذب براهیم‌دیاز از رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90657" target="_blank">📅 02:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90656" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=eFwZ11JW3hUOtHa7ZjBtDeXkXkf7RikgRmMIf6omD1P862MGRS4XVwQzFy9ip7amkDn6ADv9uCv8aHmpXQIVLc8SS6kPmrmjgi1qeZ90dssFFUyhaVNfoHhHNMZ_g9QKwOlubmocvvz6kxsvejgyEFaA2E_CZ3kpDTYU_Acz2zuhtBYzbcoxGRtpgJ3bxWWXRd6jL0MIN2Wdq3QznQvdTPWNCuL5E80E08o53AOYQt-2lS_FCsRAhshv6tWhy9sHzdAC56M6Fj1ANJdkD9lodtTS2XqSzCi50OIxVBU9zH66_sikuMwxu4KGAbEAaFuDdLSXYZ3N04sl0QMnd-ymxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=eFwZ11JW3hUOtHa7ZjBtDeXkXkf7RikgRmMIf6omD1P862MGRS4XVwQzFy9ip7amkDn6ADv9uCv8aHmpXQIVLc8SS6kPmrmjgi1qeZ90dssFFUyhaVNfoHhHNMZ_g9QKwOlubmocvvz6kxsvejgyEFaA2E_CZ3kpDTYU_Acz2zuhtBYzbcoxGRtpgJ3bxWWXRd6jL0MIN2Wdq3QznQvdTPWNCuL5E80E08o53AOYQt-2lS_FCsRAhshv6tWhy9sHzdAC56M6Fj1ANJdkD9lodtTS2XqSzCi50OIxVBU9zH66_sikuMwxu4KGAbEAaFuDdLSXYZ3N04sl0QMnd-ymxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e11
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90655" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQoRQ2gym5OuEpEc67CLiS2y9u_kZxgB11rf9xg06HDdYhUMdXrIiApuMdyy47ZlT7ZWJx5DJOj6tslHJ-gatuhL2FUyhK0-E4UQ6yT_oCiKS1SIb0afHA4m7Tpfk4-wJcVWdXN2_QIq9epm6iQPmXOWmMvBZFUOiuJ7raMkIpzBzGqCt42WCxHRqBWwy5Y4vJsUcjSVP1V8xS-BnODvoX4K-ci8-w7gFW31WIJyElnVN8Kx6_-iCViHkx-2kI2z5gia4O6FbVLBx2J6yE2IQm-yUiPXGz9aRki1z-2UVXTM7-adZHSZsQpxpI8uE03SQszQ3BVP4VlnBtMxl3NoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ال ناسیونال بدون اینکه خندش بگیره گفته رئال پیشنهاد معاوضه والورده با فرناندز رو داده و چلسی حتی ۲۰ میل هم حاضره بیشتر بده
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90654" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
ملی پوشان فوتبال بابت برد مقابل گامبیا پاداش دریافت کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90653" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کونسیسائو رسما از الاتحاد جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90652" target="_blank">📅 23:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khd7lorgeAkcm5iKKaYpnNUZ1xAHqxyFhuwEeEsITubBXi0dl4snu0qOkXps9wWVBB9EO-q3lFSxq1A1-a8KJZ6i-9L4kJec2gXIa4KNGnhFGve5uz4HMTdWwDJw08zs09P5fV5fhbF71UfjoUeyZY-yP0J0RBqrXRIbkKtpvSm12ytzh5MOZ_Y4pJTBwqwo4Cf3mLd4JUaLqEwKyEtaoouqGddiUHFjcdZcURYctVkml-I4kna51jmz9wH6sFcGNOurQstKwAqHVAzSixho2u69_fv6MeYOXNkbDuv2JfTL-mId_w2RcVCnMZ9atiFvlUfidV8D50IHv-1ccuWFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوبوسلای به این شکل رفت اردوی تیم ملی مجارستان
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/90651" target="_blank">📅 22:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_lFtjQq8yb4pWU1u3T49NEI6smAtGrFw8VnGCpED8uIsxVENlu04rtfhnfjwVPsbQrVqsJuuunEN1jX4-2qzWYM7pcLuoCU1oGyA8AhB-ObGWrFadujSu9Qr1uZkpLQeA2FQrl8TdIIVRLnPbCbse0erK9xneikNBIYjHj49XdoM9x0EJmDygxCtZNPjcFhJJhP5y8G1GrIABH4ny2EnT-LdqQZ0j-dBjDpt9BRhs7YsUUMStLxwGoqj8LoEhlZC5pvRaVEeiyzCKnmtJrkm9odKOLaBR_ZFyhAd3T1JMpAoNOh9lI7MYPy1I7sVw0K_6Ln8W9l8ovTri1yRzEtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره پیراهن بازیکنای اسپانیا تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90650" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJkxqjJ3tKiv71csyWdYEWZNIxa0s0XajEdy9qCScD8c7YEIuOS5KgS901M37m7eYgx0IbdP5ZWokpGn90qsZqPhuKKfP0LDHz5aDrfBcS4iAEWaVkBEI73mB19_MzANb95DZ0VC-SJTcwtpUlmYkEc4mjGYVnqbpX9GYZmPcg8DvsYZm8nB46bEB8uiJ5hfBqv74pWLKzXvX0ScBhRWzHUvEaEJrZf2xx6_Uk-NT4u2GnqqwgCyrMzgGIDn3QFRIXggYTj6gSYIeR8goaMLesrFjyNF2w9sEdQ587xsVyBXTyxusw1Oe2GsCLyaCx8cJvLSTWjQs8bT5e7uUoY8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ورزشی ویژه اتصال به اینترنت
🔥
⏩
به بهانه بازگشت اینترنت ایران به دنیای آنلاین جهانی، روزانه با حداقل دو میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی میکس معادل شاٰرژ ‌حساب بر روی رویدادهای ورزشی مورد علاقه خود، بدون توجه به برد یا باخت، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/BACK100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/90649" target="_blank">📅 22:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHAKF13nXgQ4z3--oNDEUipzUVuj2GeQXSkKm7lYvjlIIFd1QMasB4zONjVqYporB6iflz-PpW0qftA5HtTc6Kglb29LFwRQTxtUWbauIxRAUaeLY5FLtv2ePqWPRIkz2lEKwm4A4hSR_tZPEYOIG-OjCov8j5LperXzGD7kczy7G9_z23Nu-7o-lQnu4IIs0lZLpDXWs5jYvIPX-cNtuZe8goQAezBrXjSw1j0ii2RLDOXH29_Hzx6lfQi31RUD4t_P8OugTiV2M9CPSd9kiXDb82J91uqJHxr2WiRRBnszVDnMdDJbLPXasyfW2foMsMybxq3nQarkf6axxABb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو به تمرینات تیم ملی پرتغال اضافه شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90648" target="_blank">📅 22:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=k0t5AOnWLy-iT4WHuan0yatyr5jpbMq7V5TLjCDwt_-HnDZO9XGqj36Le1s8vCYNyuSbTgEtuGpFOcmtx8wv8jRHqA0WLATRJAbv4OiNkBaE1kHPYmTG4CKjwB-dYRJi9p7fnFtAxMjzO7LV8K7RHqamRYL1QoAHB15POIchSaCz1pSPPKIH40JG5ueRIZqcQYCLSl7hhyerx5cryT7tmtxtifjM8X5CGlkLFk5fPCjrVzsA_YNTmJbVpy8UDWIVMsZ-RRiDnlyogkdZ-9hObFmr6_5wmfQm9r1J88Wrgy-xff2Nq5otIv9bvTEnJ0lndAtqK9mI3xYJF3jibc31L5ulAS5KswrqSl01B_kXQni4FpkzyAKgirpsMxS-R-gOazfQHPXc_ULxIgzxpVfO8MqKe8DpC5dBZ3T_f-Cao-jmhp9TTWhFUCPHejL6Jbu8uHdlxtTW4JJCPwZQ9B8Fo66wtlFPNwbCm3pWvxyfvteaaBSQonerlgRMR2_bDCklHwSubUDcVbQ0tx7npF4Da91juwtMX7Cm_wLXaeIhF73eU2kzXeFtfn6qMmSTMtNoMTmh2CKaLR29vKcA1yFeo_4-AX-TYox2sA9Zux3UwJG1mz-qHF-_95LD-cKk0FTuOFvkM2_1jjeK3fdq5z-9GuBxLABVyGc_qrKaG4eeai8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=k0t5AOnWLy-iT4WHuan0yatyr5jpbMq7V5TLjCDwt_-HnDZO9XGqj36Le1s8vCYNyuSbTgEtuGpFOcmtx8wv8jRHqA0WLATRJAbv4OiNkBaE1kHPYmTG4CKjwB-dYRJi9p7fnFtAxMjzO7LV8K7RHqamRYL1QoAHB15POIchSaCz1pSPPKIH40JG5ueRIZqcQYCLSl7hhyerx5cryT7tmtxtifjM8X5CGlkLFk5fPCjrVzsA_YNTmJbVpy8UDWIVMsZ-RRiDnlyogkdZ-9hObFmr6_5wmfQm9r1J88Wrgy-xff2Nq5otIv9bvTEnJ0lndAtqK9mI3xYJF3jibc31L5ulAS5KswrqSl01B_kXQni4FpkzyAKgirpsMxS-R-gOazfQHPXc_ULxIgzxpVfO8MqKe8DpC5dBZ3T_f-Cao-jmhp9TTWhFUCPHejL6Jbu8uHdlxtTW4JJCPwZQ9B8Fo66wtlFPNwbCm3pWvxyfvteaaBSQonerlgRMR2_bDCklHwSubUDcVbQ0tx7npF4Da91juwtMX7Cm_wLXaeIhF73eU2kzXeFtfn6qMmSTMtNoMTmh2CKaLR29vKcA1yFeo_4-AX-TYox2sA9Zux3UwJG1mz-qHF-_95LD-cKk0FTuOFvkM2_1jjeK3fdq5z-9GuBxLABVyGc_qrKaG4eeai8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 سال پیش تو چنین روزی رئال مادرید با شکست دورتموند در فینال لیگ قهرمانان اروپا برای پانزدهمین‌بار قهرمان شد
تونی کروس هم تو این بازی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90647" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90646">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF4pGB90MuccL4T0gp1voqNYjNTkW0ISQSmCiIavzNf4LA0qFkKgHV_Mwb35BbVOglO-AjrrgPZIiW2vfwGj_HJOfwRuJ12fJWvNlm1AtlMnk1ljZ5JLGsCmm4b93uWqs5r14nxVu9ScPKU-HUP2j7ugmjWnaz76kFAFyWfmg6H614IY8bUWiNEkBOS_q4B574tVaMGaYk-kjlMRrL_QRiwJrn6KxiBBgwRiDhtgVby7b-rB4Xw-meOtO6EIO88bk0CPBYcERN--lcDF_2hkjCjoQbIKGWQzJnTHrRee8ehM1_TcrxnAnINhzyukdnx2XE8QM8h7TOrUU_ip667F5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
فهرست تیم ملی کرواسی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90646" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90645">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=ege79axSErF9DRPPiyAQI9OzxrpTI830YNVVdqfyMXqU9QUF8oBdTTUUU5fWYioALWoBVU-x9KB08XzXnulC5p4jsi38aQDJn1Qjxd22rCzpf8pM3er9pyCvh820Il539TnfPvStyhLZojEj-MOZsdrh7j7u8PHTHGEjcyuwDIBrJBsigB3ZZlHQXM_Zjb6WihXR6m6zWbGB-gIXBYUeeSZqF9MNGgpP1R99fm3BQB3i1wX7FOYaTe_902v8UKke6j0-lgWjcRTpigKnz63TVa7iK-RdYB7PD18T4DhLxnqeaUgCiLZ9aa6SOHpiq7DWq9heKIbk25XCGkWtXaKcUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=ege79axSErF9DRPPiyAQI9OzxrpTI830YNVVdqfyMXqU9QUF8oBdTTUUU5fWYioALWoBVU-x9KB08XzXnulC5p4jsi38aQDJn1Qjxd22rCzpf8pM3er9pyCvh820Il539TnfPvStyhLZojEj-MOZsdrh7j7u8PHTHGEjcyuwDIBrJBsigB3ZZlHQXM_Zjb6WihXR6m6zWbGB-gIXBYUeeSZqF9MNGgpP1R99fm3BQB3i1wX7FOYaTe_902v8UKke6j0-lgWjcRTpigKnz63TVa7iK-RdYB7PD18T4DhLxnqeaUgCiLZ9aa6SOHpiq7DWq9heKIbk25XCGkWtXaKcUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که رفیقامون از باشگاه رفتن یاد گرفتن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90645" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90644" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90643">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UveU-CMuX7Bjzh66QB7bwL1x7BLRPS0qhUZKIhYdEIbdHYZa3G4J0pGDYV8IXCAzwqO3OCae10vKB80yt9KbbcCgU2UCqO3SWRxevA8kOkjQPwCvGYjNi5Jc9Y3FDWGJX5iYAWj5SjdBMUota6U_LOPXMTGopv9jRlbTPpROL0xFSUYIzuoyijEgGa-hZaoSRLwxlxGjENkbdmpyTTOm4qRy3FTbMU5Y2p3_yEgiRz4tTG3QxNyMNnaJuSlokfLsfhSmMoHE1VX8uQ0GGR6Qs5oSiHgfwEbGpK-7nsgHh96dER5x_WOTOSwnQtkJbjbFmoeRRCY4ttF0TTyr4tK7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk
https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90643" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=Gq_0Vr4p8SLsvB_rKgo3Zbu7Dqq092d_WozSpLJcHB8K2zftkg-6ObRoupNFJkCFyOtLXNk1XpziJJJIuZZZa8CDmAL_X3mkrjSUU1kQR8mxHLoP8pRkUA2qRDlUhXmhYcapOUGUi_E1xA5g75nn48KONwZbZajUPKmz4QlBvDPCza1LchNqJQyPksXIaNLs9vfaFAEWy5L1UemMEz2FdACONyA53yBo_3YMB0PcvDEdaFNDzy-m1E1HizAgQtukW7MOYc63Gv6Gp55ho4hLYhvyQFgMF_cIgEshIBpfHhg5FCrw8XsMM1HRF1JHKu-pRe6InuxxFU-f3UUqMz-PJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=Gq_0Vr4p8SLsvB_rKgo3Zbu7Dqq092d_WozSpLJcHB8K2zftkg-6ObRoupNFJkCFyOtLXNk1XpziJJJIuZZZa8CDmAL_X3mkrjSUU1kQR8mxHLoP8pRkUA2qRDlUhXmhYcapOUGUi_E1xA5g75nn48KONwZbZajUPKmz4QlBvDPCza1LchNqJQyPksXIaNLs9vfaFAEWy5L1UemMEz2FdACONyA53yBo_3YMB0PcvDEdaFNDzy-m1E1HizAgQtukW7MOYc63Gv6Gp55ho4hLYhvyQFgMF_cIgEshIBpfHhg5FCrw8XsMM1HRF1JHKu-pRe6InuxxFU-f3UUqMz-PJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
‼️
دیشب نیمار حین واکنش به تشویق هواداران کونش پیدا شد که آلیسون زحمت کشیده شورت نیمار رو کشید بالا
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90642" target="_blank">📅 20:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=JQcta9gjg98ajbNf9o2qHE11Jp1fBybPt607J1bVFYASOHoF7XDaR4JFtNv--x05SjHaa5qorgCSlcVGNMFCJ7KQUnkIBX5MGJ-9GERu8HNOywb5I3j1VuR0F5GVV3ph20bw4_vE-zqgwr2C-xSfHN18gJzJ1XfTWUl4Uy7xQav9Qath4BNquzu2_jMrGEXR2aNTBCWZpIBUA-XvEa35dQy-SHczupl2Eq8sWTs4AdS-3Yf9OyZRsKL3QJhAsX3ZERRd_p9HuFe4yzK7e2EI5WYgz_QVDFbclFrpntlSJ2Ev_lHBS-3qqJzl2XL2UtVQzOFhmTe-azmegvpGCiKqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=JQcta9gjg98ajbNf9o2qHE11Jp1fBybPt607J1bVFYASOHoF7XDaR4JFtNv--x05SjHaa5qorgCSlcVGNMFCJ7KQUnkIBX5MGJ-9GERu8HNOywb5I3j1VuR0F5GVV3ph20bw4_vE-zqgwr2C-xSfHN18gJzJ1XfTWUl4Uy7xQav9Qath4BNquzu2_jMrGEXR2aNTBCWZpIBUA-XvEa35dQy-SHczupl2Eq8sWTs4AdS-3Yf9OyZRsKL3QJhAsX3ZERRd_p9HuFe4yzK7e2EI5WYgz_QVDFbclFrpntlSJ2Ev_lHBS-3qqJzl2XL2UtVQzOFhmTe-azmegvpGCiKqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرین‌کاری اودگارد در جشن‌قهرمانی آرسنال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90641" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90640">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/90640" target="_blank">📅 19:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90639">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
فرمانده قرارگاه مرکزی خاتم الانبیا
:
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش های شمالی و شهرک های نظامی در سرزمین های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/90639" target="_blank">📅 19:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11054c811.mp4?token=gwf1-LIburJpIfHNhFt6_bDvLFF6Pl8-pMyd6IF7_FyUYCH4luXAg3wqO4xPYb4CySp8w8e9mWMJ9P2-n09CHvIigBWA4cePubecYhhPv48CqqwLtJ7tvz81sUdnSL7TlagiaiTxaUd1lphE0Z25n52qqOUfc5EatJIJlnqOPwD1XlHC3JHcM2poMJPHzYPzJgxduyg5LVUv00rOOUa9COblY_o2wIG0P5EwMEkzxI5WoTzw0QtPj2OyZSGpTgHuYeuoXBy8OqeubIBkuspzn5bkpcp3tinmeVkty0so67Rl4P5E0U_IHCUKE3Y9Obc6uS7Lo58C6KplZQ6aDqw7UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11054c811.mp4?token=gwf1-LIburJpIfHNhFt6_bDvLFF6Pl8-pMyd6IF7_FyUYCH4luXAg3wqO4xPYb4CySp8w8e9mWMJ9P2-n09CHvIigBWA4cePubecYhhPv48CqqwLtJ7tvz81sUdnSL7TlagiaiTxaUd1lphE0Z25n52qqOUfc5EatJIJlnqOPwD1XlHC3JHcM2poMJPHzYPzJgxduyg5LVUv00rOOUa9COblY_o2wIG0P5EwMEkzxI5WoTzw0QtPj2OyZSGpTgHuYeuoXBy8OqeubIBkuspzn5bkpcp3tinmeVkty0so67Rl4P5E0U_IHCUKE3Y9Obc6uS7Lo58C6KplZQ6aDqw7UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جام تو خونه میمونه
😉
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/90638" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYxgtLDq92ABw1eTEP3HPSAm4AUJH7Bc8bi9hUz0LTypedG7DCD_fg6QX8rMqzeDnyfcFC-sZWdWH9N1TcKvGxzTva7p2Gtj1-f1Pph4XYZy25vtTgGKp6PNftwqN99q2028x77QslAPzoSVkhQxqgKW2LFYApYg_iBhJo86wpfZY92FMQyXtCJsMtXruV55sC1SmUU5vFat4BpTOvvn345pIE8qPVomibUl0_UX-UBTJ89xHp7ESb7gDkJj3GQfArwg2BzzxhtrA-kaWaO_GqdlVjqmckcNwdxF13t61RknE6gbUkf1myRTyjZPYInodwRh6xNHKYIejGaCX5cp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بعد از متصل شدن اینترنت، معاون وزارت ارتباطات برای اینکه پیام رسان های داخلی ناراحت نشن رفت از کارکنان پیام رسان «بله» تقدیر و دلجویی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/90637" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90636">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TG8l6xNtBH6xB9vYXB7gsYtQAY79_1EHbJ2xfwPyuDX85tHx_3c1B3OPwH70scdnRNTuPlWFiqqbkEErdiCx62fmf2HwzOKpczFALD2KnvI5AVaf1fP4iU7_aBNrW7jbT6i_sLI2tSi1zBKhcxL2Zx8VX-yHnQt_Iv6z0MsphPW7T4riH5DJGJLo8cr7qDm2hwJnXURzAuTBN0060NfXEx3Fd7FC7NdBExa6Vxt4B2s31iL_V8FvcbvPRhDKmHhfuUdGDg8fgYanfVReKl1j65F7XsnmPvILzfc16L9uvfD5HUNRzpm8So2aEeM6VRrt-4F-AAt8f_xjf4t0dot2FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد قهرمانی هر کشور در سی‌ال:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/90636" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90635">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=RUYEUvG1RWLrzfnTX010hmefXGZnmne_uYJ6uQiJIuqRB16AdToPn4eDXV0rsaMuqhfrVGEfwOj3NX2DoE29S-hKDrgDsmuLRTeB2IyOjzzQ_o3ZUeGaVE21JWghzURRdr-ftg64Ghi3f9kqa3_tA_Iopn26uZ6n93MDSlRcaphOI4_ecc09uWb3UjKUP11LWwEw8fHZ8a0Mat8BukWYFDjtM6_VdSMP6iiI5YgxwAos2ihyxxaZH-vbZ7s9NDNUdPYSWCPu3MztLgMxMS2Ildu2AN4Lg4pGrcVfj6POahtCG6U20Wtfp8Ti7KG_XOu7_NSzIls4gBXCfnjG0NJR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=RUYEUvG1RWLrzfnTX010hmefXGZnmne_uYJ6uQiJIuqRB16AdToPn4eDXV0rsaMuqhfrVGEfwOj3NX2DoE29S-hKDrgDsmuLRTeB2IyOjzzQ_o3ZUeGaVE21JWghzURRdr-ftg64Ghi3f9kqa3_tA_Iopn26uZ6n93MDSlRcaphOI4_ecc09uWb3UjKUP11LWwEw8fHZ8a0Mat8BukWYFDjtM6_VdSMP6iiI5YgxwAos2ihyxxaZH-vbZ7s9NDNUdPYSWCPu3MztLgMxMS2Ildu2AN4Lg4pGrcVfj6POahtCG6U20Wtfp8Ti7KG_XOu7_NSzIls4gBXCfnjG0NJR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
Vini
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/90635" target="_blank">📅 17:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90634">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=RoSAxFLCdP3FeRvDNwmNXPHA2Ll_NKM_RmIrk7L7nRt0Vwtv5H4GG0UEsgOUg-jTcZ5_QIR84Uhq8zCFjQiJoVjKcOStKki4RTC18x_xJ9WJo4ujWB67zjasK9QEr56Rc_D3DfcdHJ1Bx88EagOG0pqzvdyNyz3viOoPmRdqBtrZGtTKKU06gk5yjaqM323Rz5qpBUzkwSDupmaMAWWkHWhlgNgIK2MgUQ-Y-paVDwS2-XpZCCUCPUnZe0EyjVOkm3REIyT0MO_8RdSDUbtRQje2-jGlxWFy0J6V0vUIjtUnCDRwf-SWm5fjkKMX7l0L5WMxP_P2dTBKDP4CLzBgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=RoSAxFLCdP3FeRvDNwmNXPHA2Ll_NKM_RmIrk7L7nRt0Vwtv5H4GG0UEsgOUg-jTcZ5_QIR84Uhq8zCFjQiJoVjKcOStKki4RTC18x_xJ9WJo4ujWB67zjasK9QEr56Rc_D3DfcdHJ1Bx88EagOG0pqzvdyNyz3viOoPmRdqBtrZGtTKKU06gk5yjaqM323Rz5qpBUzkwSDupmaMAWWkHWhlgNgIK2MgUQ-Y-paVDwS2-XpZCCUCPUnZe0EyjVOkm3REIyT0MO_8RdSDUbtRQje2-jGlxWFy0J6V0vUIjtUnCDRwf-SWm5fjkKMX7l0L5WMxP_P2dTBKDP4CLzBgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حدود ۹۰۰ نفر در جریان ناآرامی‌های پس از قهرمانی پاری سن ژرمن در لیگ قهرمانان اروپا در فرانسه بازداشت شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/90634" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90633">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90633" target="_blank">📅 16:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90632">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=DqJKdwD_idhHP8VZBiAqNP6NLRRW7DAHpheyToCpWiYh8G-nGtlt8Eau8FQouJFokILlrkvulOOk2jxuVcl_x1gmiq_Xa7rNZMXEvEOVXxzmDY1akOB0L-Hf-jQ37JhqLTSA9412KrQ8sqgbo33nMiGHo4ISN9AA-_0UtoZLCV0hCspChqHL6cFrl6KISjRXEe1BGpGvtCnqF6J1UBZOMytOs8sXgzFR29fGi4EfP8ylWc2Evv6Y1rEtF_Od2JnlvzBR-c3y0QfLH__nJuFF-BbD2Z6q0AOjBfrlplhPvA_w-vwokkCqKqkQd7ESIT4cnAAd8YOFiSEb1u8o0YInPDuSI2_gCLFIfobCXXbfZWKhAJxAEq_StDHxzmDn6SIGjYl3tWNUC1AMcxKetEeuWmmXNpKrcgBz4ecnWoRwHfbP15obeiiYr70PyzfO0mewYnGr3qCCjc4rJ_XlaYvIuY8Fhn5Bb62X4wq-uqtsHVcJFzsohbXX6BcX6uK_VyCT0gmD2K8N6qjONmVyRe3Nf5LAUB8un3I-kkIqiJ47ShSx4qqXZOqS4J4eab4oeB5m-aIrYcV-kF09bygwThbsYaQ2woXVpY8oU6Bxrtix3G7Ds6aVE-TawCQDaqtOP1fh33hhM5OdyJ31KMYfas9lJJEb4l8ZL5nd-5BQGvYUGLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=DqJKdwD_idhHP8VZBiAqNP6NLRRW7DAHpheyToCpWiYh8G-nGtlt8Eau8FQouJFokILlrkvulOOk2jxuVcl_x1gmiq_Xa7rNZMXEvEOVXxzmDY1akOB0L-Hf-jQ37JhqLTSA9412KrQ8sqgbo33nMiGHo4ISN9AA-_0UtoZLCV0hCspChqHL6cFrl6KISjRXEe1BGpGvtCnqF6J1UBZOMytOs8sXgzFR29fGi4EfP8ylWc2Evv6Y1rEtF_Od2JnlvzBR-c3y0QfLH__nJuFF-BbD2Z6q0AOjBfrlplhPvA_w-vwokkCqKqkQd7ESIT4cnAAd8YOFiSEb1u8o0YInPDuSI2_gCLFIfobCXXbfZWKhAJxAEq_StDHxzmDn6SIGjYl3tWNUC1AMcxKetEeuWmmXNpKrcgBz4ecnWoRwHfbP15obeiiYr70PyzfO0mewYnGr3qCCjc4rJ_XlaYvIuY8Fhn5Bb62X4wq-uqtsHVcJFzsohbXX6BcX6uK_VyCT0gmD2K8N6qjONmVyRe3Nf5LAUB8un3I-kkIqiJ47ShSx4qqXZOqS4J4eab4oeB5m-aIrYcV-kF09bygwThbsYaQ2woXVpY8oU6Bxrtix3G7Ds6aVE-TawCQDaqtOP1fh33hhM5OdyJ31KMYfas9lJJEb4l8ZL5nd-5BQGvYUGLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
ازبک‌های‌جذاب آماده رقابت‌های جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/90632" target="_blank">📅 16:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079475458f.mp4?token=GHxxRDZDLjlqXX5nk1mCJEJw3Ifq2gE6BFL6wslJDg9vjUMxVcfBNt2Oh-sQRd5G_b-JLrWytyqiYXEGGl-p7X4wdcuIx3nqGkY3pHi1R6GTynu5R2pi10Kgs8HipiYzrYvvY-B7ExU0VS-7YTbQbDACtF5uJXlhfjTy91nZKFO8V8VBpuwVxbSnEbsjOyjJimc-Ttm80guFlAtgUJ-yBI2s-rUnIstkaaPuHmseo0vKPwvOJQGp02YwR6u5UCmzYIzYurFOlyjlYdG1fdkJOqWgoHDgzKqWtt6V1EkuFHCmB1rf9OPRIpNJRvliSwmKQ9FAsn2yxtOpv9WnnIaQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079475458f.mp4?token=GHxxRDZDLjlqXX5nk1mCJEJw3Ifq2gE6BFL6wslJDg9vjUMxVcfBNt2Oh-sQRd5G_b-JLrWytyqiYXEGGl-p7X4wdcuIx3nqGkY3pHi1R6GTynu5R2pi10Kgs8HipiYzrYvvY-B7ExU0VS-7YTbQbDACtF5uJXlhfjTy91nZKFO8V8VBpuwVxbSnEbsjOyjJimc-Ttm80guFlAtgUJ-yBI2s-rUnIstkaaPuHmseo0vKPwvOJQGp02YwR6u5UCmzYIzYurFOlyjlYdG1fdkJOqWgoHDgzKqWtt6V1EkuFHCmB1rf9OPRIpNJRvliSwmKQ9FAsn2yxtOpv9WnnIaQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همچنان حاشیه‌های دوس‌دختر امباپه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/90631" target="_blank">📅 16:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90630">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=s8QWXrOMPG786LVRA8wRAorUHo6kwtWzyaowPOCl0qhHeZqQJkT1nZJ4NGtAN3BXVX91gVgbGkKsTYVZ9ZJuSfB4ZDehYEj7bMp-PkYea2RNn5zVhYzO_MlUUURnGTE5WXwwNScoSrKSnqCom8ASW073YzsTwIQ_9t_0fp32HOWNCvVAc1uRDpVomU7RQOcxOLfgHvdlacIwRGT2l_8vieTKmgmHPLhSFmfdW0QaB36bD83LkW16aElnXsv4pcPIW6LVrdIOFA3lF9pGwZyYj0VeFxhw8cs-KHq2uxDjFW87N8rrJMpebRBPpikPXkr--cpmkw7FGLbvf3ML7HiOsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=s8QWXrOMPG786LVRA8wRAorUHo6kwtWzyaowPOCl0qhHeZqQJkT1nZJ4NGtAN3BXVX91gVgbGkKsTYVZ9ZJuSfB4ZDehYEj7bMp-PkYea2RNn5zVhYzO_MlUUURnGTE5WXwwNScoSrKSnqCom8ASW073YzsTwIQ_9t_0fp32HOWNCvVAc1uRDpVomU7RQOcxOLfgHvdlacIwRGT2l_8vieTKmgmHPLhSFmfdW0QaB36bD83LkW16aElnXsv4pcPIW6LVrdIOFA3lF9pGwZyYj0VeFxhw8cs-KHq2uxDjFW87N8rrJMpebRBPpikPXkr--cpmkw7FGLbvf3ML7HiOsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیشب بازیکنان پاناما بعد شکست ۶ گله مقابل برزیل برای عکس با نیمار به صف شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90630" target="_blank">📅 16:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90629">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/90629" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90628">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_wq5sYf531oy3_rIskBJF7N0Auc9YNMLdH-OR9mOOy2hW8RvF663ueR_bZfmzFgR93dcINvL3XDyQTPed6dhE0i-xB974FNT9Vji0C8_syraGHIWa1UO63GiVXKGI52DgoP457fUrIK9qyQpdrDVYaZuoNZ6aE5sqcLEvabUgVztqL4ktTW6FbiJ0li4gFD8KFxywV-wn0D2KQI8y9DHtsdZkM06pEILvJcQuysJTEE4yuE413gmG3yJN44HJuC6jGMKIEqxEmpj5OvQMtF_qXLSscW5Em8UT1QZxHk5xuhw9dTrzby5h0hrPZSDcSMGDaE3gGI47t_sHg2SczB9s44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_wq5sYf531oy3_rIskBJF7N0Auc9YNMLdH-OR9mOOy2hW8RvF663ueR_bZfmzFgR93dcINvL3XDyQTPed6dhE0i-xB974FNT9Vji0C8_syraGHIWa1UO63GiVXKGI52DgoP457fUrIK9qyQpdrDVYaZuoNZ6aE5sqcLEvabUgVztqL4ktTW6FbiJ0li4gFD8KFxywV-wn0D2KQI8y9DHtsdZkM06pEILvJcQuysJTEE4yuE413gmG3yJN44HJuC6jGMKIEqxEmpj5OvQMtF_qXLSscW5Em8UT1QZxHk5xuhw9dTrzby5h0hrPZSDcSMGDaE3gGI47t_sHg2SczB9s44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌کم از جنارو گتوزو ببینیم که دیگه بنظر بازیکنی تو میلان و ایتالیا مثلش ظاهر نشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/90628" target="_blank">📅 15:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIxCrhpUeCgzhAdm1gAcjiYGe6cHy3k9jQCMvvE5BBVntKSzvVxkVTZRietAB2EgqcM7pQjsGvGesdVAMLhJlKe6Eb596JxPct-0FszVVGmterDKCBU-u4f8wxQxZOqcAlShuYBjDkYLyapFgT1e4sZMx14U3za6389gvhAMGWlM-Gss2p_SewMUvxxi4oTAWrlczhLA4Cio1AMNqYioBTqSFj0FZcJ-E-4pt9Kt_LYx6FhJWwo6HkGh0jiEDHFjM5Y_JYezaXtzn8fsHTPyD0NTRBtGvT1l-JCXY3PouHfwck3AwyRnGUIBKHaIVgNWZRqOLLSVyZ_nI5R0m4Uh_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90627" target="_blank">📅 15:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=jy4s4olXV5cJVatWo_ryONoc1NJVruUFf9YjvQ6eZFZV4TzLHyqGywbRW8-Q_m6-wbHZ2mPLcLrr_mtE74NHhbmT6rEdAvIz4cTbrG4wmo-WXUfola1Ik3bR2krpdSyilK1vPiVtf8wUEk6r4KxxkOxAe_9iMdxrOSiY4PFw99bn-NWyRuuVc6bx6p_aNTrG4NR7_CEv-KvGfMR6vp2fCl64YxR_OiR8wY5_cwp8Ko2Z3-c-jbr3mJOqFdHzVoPFVasSGPOeRWKjUVUjVwuyqPnCbYYv1QjxuHJc78C5x6m-DPrF5niUAj-CggBYzhF7GX9Z1mwYrkHH346EvDCbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=jy4s4olXV5cJVatWo_ryONoc1NJVruUFf9YjvQ6eZFZV4TzLHyqGywbRW8-Q_m6-wbHZ2mPLcLrr_mtE74NHhbmT6rEdAvIz4cTbrG4wmo-WXUfola1Ik3bR2krpdSyilK1vPiVtf8wUEk6r4KxxkOxAe_9iMdxrOSiY4PFw99bn-NWyRuuVc6bx6p_aNTrG4NR7_CEv-KvGfMR6vp2fCl64YxR_OiR8wY5_cwp8Ko2Z3-c-jbr3mJOqFdHzVoPFVasSGPOeRWKjUVUjVwuyqPnCbYYv1QjxuHJc78C5x6m-DPrF5niUAj-CggBYzhF7GX9Z1mwYrkHH346EvDCbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
کشور سنگال با انتشار این ویدیو نوشته که ورزشگاه لس‌آنجلس یکی از میزبان‌های جام‌جهانی مشکل جدی در چمن داره و خواستار بازسازی فوری این زمین شدند
در این ویدیو مشاهده می‌کنید که توپ با برخورد به زمین ارتفاع نمیگیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90626" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90625" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90624" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMbke1ZBsL5LhS6UjRnBhoQBYjbK6-oLzUo4ARaOZ9XJSiaqeUu6sXsh6z2gduMx_eBwYyslff3t_Oek75tD0K84Hd9Bt-kL5tUY94k7Ru9ec-Akmq_qTMR_QMglgsclaIPfbyA9BXE5Qu5PnNiPBBsknGpT9hASPWo7GyiJpaGc74j3J0a3mZbvBHm6HjBFFUJDfoOcVtFVMUyGfTmh0Xb3Th-4N3sUWrlw_iycP2B2LyW3LgjGrE94zLtmFAXhaS78kCEHoWne_B3OX3yvlsexVf5HU32E_AEhcLgSKHUjZzX4ayDNOyi38ZF0O_L7T-95omsFHP8Co9uRwm_d2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی و بادیگاردش تو اردو آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90623" target="_blank">📅 15:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR5sfcWiDr16Pogxk5ylRhDdqZpQ5o4gK97CTk8_TqHrJOkXmjRicwOPe8CokwPeXwi3hWbexKmDyZTEa57BCz_J1SY2S09YhNi4ws0uyLftaDQuIAQl3oOrufZQ6WvFvR7kDnICQpSP1D08Et8cNlbNqMIpp4ndxHQck3lUDuRemWsL1AFsYNh7s72b3rhYjv-_1s_hvm4i1CQJDqy8Vph2e0WHYTtKQnXmg-Qi5H1uOpoRjOGdFeIAWhqTxDhqBtyNG3REO61QH7lhlQWkoFpiZlpWriqudHMcmJN26-56dyYkOFUxfhZmbRiL_tLdUzAO9AmB2OHxChxUCdPiAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فووووری
؛ با اعلام رومانو، قرارداد آنسو فاتی بازیکن بارسا که به صورت قرضی در موناکو بازی می‌کند، دائمی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90622" target="_blank">📅 14:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=fknTLkspSSYXAwtJp_waaaPaZELDhDHhCbWTi5vgbU2EAkRvxX_lZL0FmtMJtZKP1CkUzPu9VTZ8jTLG55K0OqPSyKDghTwag8Xc4usAngpfuAVPN5Dns0KeK_9_APl2mG2yhkG5XDBX_URAo-X9jryC3_hickib3sh4t3rFXxWOWIkpbiGbJsWfRc47oBPsdNStHc9qX8fubDCcXB6bHwbmZ9GLCWeoanSMyaxYOMY9RpyfmDvM96gTh-kng0qFJyMThKcqVcC2jCx1jSaEeHgTQcfuETA6edUs0zgPdSMao2xDef8fNBhccKjofQy61bXXKePy9hYGuiJ-UK7vhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=fknTLkspSSYXAwtJp_waaaPaZELDhDHhCbWTi5vgbU2EAkRvxX_lZL0FmtMJtZKP1CkUzPu9VTZ8jTLG55K0OqPSyKDghTwag8Xc4usAngpfuAVPN5Dns0KeK_9_APl2mG2yhkG5XDBX_URAo-X9jryC3_hickib3sh4t3rFXxWOWIkpbiGbJsWfRc47oBPsdNStHc9qX8fubDCcXB6bHwbmZ9GLCWeoanSMyaxYOMY9RpyfmDvM96gTh-kng0qFJyMThKcqVcC2jCx1jSaEeHgTQcfuETA6edUs0zgPdSMao2xDef8fNBhccKjofQy61bXXKePy9hYGuiJ-UK7vhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه بلاگر اروپایی اومده فینال چمپیونزلیگ رو اینجوری بازسازی کرده. حتما ببینید عالیههه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90621" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ6gAKmVg5rb0FBJImXvKOA_PaaLmje7LrJZpfPdcsgMu2eKZwIlcbfrYCjYUqmuCGuKwoXqy9KOV8To0kHLiJVEaH9WmxsHO8OWcCGTb3UgmkwJhV9MtkfXkzpd5MhMg_-aAEa4iI155lywptJXT5ZJrD42q6-ea6chPam8WY7x90Lqt9q7T2xHgFpmE6tDl0Zzyx0cynl29FtUKgBKhmaJTDyAwbk81Tf1TaU9GqfymaZaf-kzQoS0j6UFgz8o_2gwQT5iy_wcNJBjthYxkD9JtBDYQ_3yTgSueX8VIBPe_UGnSDcJoSgCmmcNVHtpzLTxVHDry2Fn-ObKebzoTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#نوستالژی
؛ سال ۱۳۹۳ و همزمان با جام‌جهانی ۲۰۱۴ برزیل، بسته‌بندی خاص چیپس در ایران برای تزریق نشاط و تماشای مسابقات در ایران...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90620" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
سرزو (رئیس اتلتیکو مادرید):
«جولیان آلوارز بازیکن اتلتیکو مادرید است. نه فقط برای فصل گذشته، بلکه برای سال‌های زیادی در آینده. ما همیشه در حال تلاش برای جذب بهترین بازیکنان برای تیم هستیم. تا ماه آگوست، وقتی لیگ شروع شود، هنوز زمان زیادی برای بررسی، پیگیری و انجام خریدهای جدید وجود دارد.»
﻿
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90619" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz5WbzhwIyHVic-OnHk7uUf9bKJrrJF6kYzs9xze7f_Z75NaeoXkzhlHi5W7FPxyXD3CZgeLc9DEvvpdiiejPHAd_tguTRLhypGLQu1CIID-S-xpo8d2ud-MvvYDgUAo42nwQa7sM2Bbo-xa4iT6YO608-MCz_Ox50DfehfIjw3cl3yfKK_iYeYTkeSIRfY5XvXzrS75oQqOwT_MPXqWZHVxCPmj4JcEc5GBIvVSm3YkY4FaJNSHd4eywhewSqc2loe4eEwrFo6BioZYe3EFUGANuWHZcxSTSt740VcBM6QyWTyhLLjvsVbcVy9X_EgX0KYYwD2xN1Ebtfnh7ZCXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⭐️
مقایسه آمار دزیره دوئه و لامین‌یامال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90618" target="_blank">📅 14:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=oyc16323jAYEsLClMbbaiwO822fMMMzzt9rkKO15reCrixTkwgD-VnbI9VqbVC99BtsdOcGq_NYiE_xc2Ah1A4dIU5DwTgJ0cooiOBQ1fTmgAhyRC8uDv1P3SdDG7qi1PF6Bg2cGxaWDo1ODJiMGW9m1NQ2k4DWhNcxyyHT7eqKUEEr10q1yBKyGp7vrcC_SnHl_wzTULUYsfoiV9uiCbSC_m0XquYuH6NZtpfQaCfi5gLuirP5Y6Rlcwa_LMcaAnC5ZXvNy0xO_7fsEJIu4Y68-gj2suU1sBQPMSRLj5lnC1md2uSz9K225D3Elll6a6LRDir8jLYRqLiJDO5tmz4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=oyc16323jAYEsLClMbbaiwO822fMMMzzt9rkKO15reCrixTkwgD-VnbI9VqbVC99BtsdOcGq_NYiE_xc2Ah1A4dIU5DwTgJ0cooiOBQ1fTmgAhyRC8uDv1P3SdDG7qi1PF6Bg2cGxaWDo1ODJiMGW9m1NQ2k4DWhNcxyyHT7eqKUEEr10q1yBKyGp7vrcC_SnHl_wzTULUYsfoiV9uiCbSC_m0XquYuH6NZtpfQaCfi5gLuirP5Y6Rlcwa_LMcaAnC5ZXvNy0xO_7fsEJIu4Y68-gj2suU1sBQPMSRLj5lnC1md2uSz9K225D3Elll6a6LRDir8jLYRqLiJDO5tmz4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بالاخره یه ایرانی هم پیدا شد برای تیم قلعه‌نویی چالش اخیرا ترند شده رو اجرا کنه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90617" target="_blank">📅 14:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDp3_eEkMkDk4rLIiegZSm8F_24sVTgR9eHsH8Mrmqgy2y-K2uw2tm0CoKKRr66YGNqaH76cyaT4BEPY5B84KRT1ozMI6452pM3gRY5IPTp-s4SmK7ILAj9eHIJ7J6vCcv76VUVWr5-p-vkmzB-xuMAKhVSVKKW4BvJpiXH3_WWfSk7eo8Lhcj3vaZIFZVutroyWL04bwRKaw5QMQITRd4f43zrsz1JjHhEDhKfd7cKwjdH7xpp_3nz0kNYzz0CxirI5Qau3s9WwQT8LddYnDFy_MignSzkcsLTTrRdUcLNjQlTTW41q88s0r3QzpJ2Cik3sdKXAIBLjGI3BuAGxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داویده آنچلوتی به عنوان سرمربی جدید لیل فرانسه انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90616" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
#فوووووووری
#منهای_ورزش
امروز حوالی ساعت ۱۰صبح در دانشکده پزشکی قزوین، یک دانشجوی مرد در ابتدا همسر دانشجوی خود را به ضرب گلوله به قتل رسانده و سپس با تفنگ، به زندگی خود پایان داد. سپس این دانشگاه تا اطلاع ثانوی تعطیل شده است
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90615" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=gp6DOlVY1_rIGVJXY3pkHwhoCxuG1p1rTXgceyl7SaXefiDkIZlAf7MXvbeDXiPqEg2RRQo0LeFiFHyOhmVR_RB3EhJekHTBxZy8bzHojAHrjPOrOzxFLSeYObEpih7tzRbnL1lQvrfvcKD2equNzs4a8sSclh7U9jKqOisE5zFSPs1L1PztT8NV_rbmSCp9DU2tPJbxPKHAv8Y6VwccxqUxWwvEhOA9Ht6gDRj2oLrumz4HnahB0Pe9hecepwPpltEV1csOrjuxqgCYg-_hkHDtpJCro9GvYppVeUkrhvs_2-W-VIyVeRO4tkR3vETH3V1bPNfs8yCOuZjTvGdwxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=gp6DOlVY1_rIGVJXY3pkHwhoCxuG1p1rTXgceyl7SaXefiDkIZlAf7MXvbeDXiPqEg2RRQo0LeFiFHyOhmVR_RB3EhJekHTBxZy8bzHojAHrjPOrOzxFLSeYObEpih7tzRbnL1lQvrfvcKD2equNzs4a8sSclh7U9jKqOisE5zFSPs1L1PztT8NV_rbmSCp9DU2tPJbxPKHAv8Y6VwccxqUxWwvEhOA9Ht6gDRj2oLrumz4HnahB0Pe9hecepwPpltEV1csOrjuxqgCYg-_hkHDtpJCro9GvYppVeUkrhvs_2-W-VIyVeRO4tkR3vETH3V1bPNfs8yCOuZjTvGdwxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بعد فینال Ucl بخاطر شرایط جنگ در اروپا، استفاده از پرچم روسیه برای سافانوف گلر psg ممنوع بوده اما دوس‌دختر سافانوف با چنتا تیکه پارچه برای شوهرش یه پرچم می‌سازه و بهش میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90614" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8n3JtPVNxChMi63JedCgOCL-WM-maylItfkho0rdiNmrldQl9DnWy9mkFZ9eoXt-e6FmsgJC8fABZ7v7JlvYDBmyeM-ypE5TJSUUla33baxjyIFEy-3a1daP0IcDB537vCeEyH9cmNmkS5p9zo6R_U2zI6nwpdGLGJSHeIc8_D8NAZzFqZV4ywwYmLkf2VdlfdIvQWxQ4Ho7iwSlea7oLSA18XYJU16H9LCDzNoNw_Sxl7Kg9JcVhfOy0O5i1Y3xfiaDerG6MVUvKXBxs1069Ur4ypcFp9cjBUrSaWhZ5X6KvMchkBAtympwPe9ze99FtcltzqaKBHTPOgd8EtroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|نمایندگان انزو فرناندز درخواست رسمی خروج از چلسی رو به مقصد رئال‌مادرید به مالکین شیرهای لندن ارائه کردن. فرناندز گفته به هیچ قیمتی حاضر به موندن در لندن نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90613" target="_blank">📅 13:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90612">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmTvsuPOjDppbpXrgy-Tw9XcQ6NCzApGIvPzcVRb-qI6RmeT-HonUxzqJD51gJnz9jo61VKwEhUgbyuYeCypjq0HX6f9tC1lqM0YjogA3RdzhhRYDs1ar83eCmcUuMQ34el5RcPjKPq1Mdz8_aakmw76aKCZRDQx92zBaKnnFbGCM06qz7cFZRKX0b0B_Vc73lSh-2BOxRQJQNR-nFwQN-3zugMXEHNTk_GRHyyQpoztFuXe9BDcQz2l8D9eeWbiENMYFBEL246ShL4eaH31b7yFjOrorMMyfRF7sIXST9LQk2Ddw39xyXQ1PnwYFcwTKbY05cU1cUGc9J7i4uTaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مارکینیوش با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90612" target="_blank">📅 13:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90611">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/brWyNcuz1nKn_T0BpmKWLOmRon316qhAXvp8mqV-ixXLkA0C37ERxfje-_j_8kPgY7toUgmX0Pfdnuc0kK93etZRhuPhcFqPY10GOvLHt9AjFzbr-dc9hP_QCzKvkH7UIcq8wSDL6dfwTYzERDGuGjP7iEYdPi8AwlVX9jCWDyPtP30ZDGBRpo7O4M4tzWVm7OrpUg2e3mCUHVejvY2oQ_0HuXGr-qOaJgZVOJ2ozBEETS3mNCtIwfRq-Lv5h_zscOUqht0fmzDH3XlOJrmlA9irTQjjUXpgdzvyVZKgK_7G_ItTK1GvMlhTLoAAxXSjAMS7P3Ok92tLqsATnPOPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
داستان خولیان آلوارز تا الان:
❌
تصمیم نهایی گرفته شد: بازیکن در اتلتیکو مادرید ادامه نخواهد داد
🇪🇸
مقصد مورد علاقه: با بارسلونا بر سر تمام شرایط شخصی به توافق رسید
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خارج از داستان: آرسنال و پاریس کاملاً از رقابت خارج هستند
🇪🇸
فشارها: بازیکن و نمایندگانش با تمام قوا برای نهایی کردن قرارداد فشار می‌آورند
🇪🇸
🇪🇸
موضع مدیریت: بارسلونا پیشنهاد رسمی ارسال کرده و منتظر پاسخ اتلتیکو مادرید است
👀
🇪🇸
طرح جایگزین: بارسا پیشنهاد دومی آماده کرده در صورت رد پیشنهاد اول
✅
پایان مورد انتظار: اتلتیکو از تمایل بازیکن آگاه است و نهایتاً مجبور به نشستن پای میز مذاکره خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90611" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90610">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0ll0nn08hxpV9XKDDh7sRCXurdMmS1-YWLdNnA3-oR9YoRj_vvURVHeBeIm10z7j2xSMKo9i_3NEwKiIfz0gq-VIQkF2YD68kTkkk20IsYpNjU1kgnt1o2c4TfgXVX1cUKnTtUF-7b96FyKuaBmsUI_uEfRgS57GVvui3Xqnsi6OKHb_1LqJbSvWq_6rmjHPmk435STXWwqbrWPbD-C3GRb4FEBei211xiXPrJ4IDhMVZa3VcxDDP6aEM3516h1TfzwlLwlHvQcUWaW1dMa8veiz7dFhtfa_9TauzXUxweBmaXkEz7spda4Q6XVTwy4bP3K92MkRT6ZkJDf9P7NLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سافانوف گلر پاری‌سن‌ژرمن و همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90610" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90609">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90609" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90608">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skAMG8_QbwRy8Onxf5r3Sp0VXBtwKH0TiDjZdWTJZTHUgR-KFMiWy17yzi0NDFcotJdkj0cS3bPUnGK_uDAaMhzl1vCbdgYITW0gmNrbf5u9yN4BUd-5cdkEHY1zFfgwZddtEF5JUzfg-zhHsMgWwx_hJ0DFECQ91fKKkojITK7cKY_lexdNWuTmxk1HTW6mhhaOms5dVY1OaLKKiJrV_JuRxYD3-dMI5PStRxIHrgX5Xl3THwfeW-TrcqlqoK70TdTD9I2k6l0lKxSGXaM1e9XTnFfClsPr8C6FtSuA_w6yN0TB2r8e6jWl9KhzgCsMY69LF5sDN9caqac_p1LrOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90608" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90607">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=OPItXwMXAMS5iO3rjjDiU5jenlSSwjWl0NImuUAmHHB0d4ZmCDAiEAGInnOfqRDU7T4-BN9spQWizXGisw-v_DCD-Qrle1Gde_fqKiyEsyd8H8Hqeh5GlNQiZULkma1HQzl4qTt3zERUVrt7USO-OVvwFyShDh38bR7iQ36ExPAXSqTLCidjwkFHjZtiaCz0ObuuThOAKoCnzEpiz8dPYb6MSy6B48wfYkFO0HXcyJOab2Lg3Aj58WgmeH8Osc3TMPlLRBtZd4ATeRvZqJzg1z4OLUslWONR4blguXKh8UoexQpldFtK7MjQ7YIhLZWeiOVohtM15So79I2pkeuPbTdJRfzXjhnWR2CiWAA_HQ4gQMMxFNOeHdtB59csz1p69eFqYSqo_PkJ-0qp0x0HoTGYmRpLvvcNZo-6TpfPliSS1FzoYjjQDzAGRRvz5Ka78GApgzn0p1Rx5DHWqx4VPEK3SJLkjYHccLB2uefiX-pTU5kXrN3H7NKUzT6fMZh9g3TiUGOHmq55rgoNfRRZJxyiRjz_UObg-B_OopsnpaxKWoMrpgg0aV0Vaeq-mhyDvBtENuzakgeYyh1Lg2pPzVDWRfDezYwvT-d7IQzHRBYUVmj6Som8dm4fWMRG98UZ2EtXCDuK8RhWVWgpWRCN0e4iegv1dA0ReiXch-hy8uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=OPItXwMXAMS5iO3rjjDiU5jenlSSwjWl0NImuUAmHHB0d4ZmCDAiEAGInnOfqRDU7T4-BN9spQWizXGisw-v_DCD-Qrle1Gde_fqKiyEsyd8H8Hqeh5GlNQiZULkma1HQzl4qTt3zERUVrt7USO-OVvwFyShDh38bR7iQ36ExPAXSqTLCidjwkFHjZtiaCz0ObuuThOAKoCnzEpiz8dPYb6MSy6B48wfYkFO0HXcyJOab2Lg3Aj58WgmeH8Osc3TMPlLRBtZd4ATeRvZqJzg1z4OLUslWONR4blguXKh8UoexQpldFtK7MjQ7YIhLZWeiOVohtM15So79I2pkeuPbTdJRfzXjhnWR2CiWAA_HQ4gQMMxFNOeHdtB59csz1p69eFqYSqo_PkJ-0qp0x0HoTGYmRpLvvcNZo-6TpfPliSS1FzoYjjQDzAGRRvz5Ka78GApgzn0p1Rx5DHWqx4VPEK3SJLkjYHccLB2uefiX-pTU5kXrN3H7NKUzT6fMZh9g3TiUGOHmq55rgoNfRRZJxyiRjz_UObg-B_OopsnpaxKWoMrpgg0aV0Vaeq-mhyDvBtENuzakgeYyh1Lg2pPzVDWRfDezYwvT-d7IQzHRBYUVmj6Som8dm4fWMRG98UZ2EtXCDuK8RhWVWgpWRCN0e4iegv1dA0ReiXch-hy8uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
برخی از برترین گل‌های فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90607" target="_blank">📅 12:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90606">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrWEQbpZiLkvX_fTMRoDlMKY4FjzCNBT1TvDchSXmcy8xZKbBA5ID68iZQQE6lSPq0OncHohNHgXjXObpOt6gjTHiQY8Xo7Mpp5VGgtn0qT8hN2koqgWrYBUOVVOs23k7Dvty0Se87A0mdYb2PlRBK5J_bTT6sfZomu-zmClr9fbCfDqLgOwACsGFIA94nbC2gd4nmDSdwpRLHuy_8arOICSyIzXSqe1eIeR89BCdEggudAFQheXNnV2csW9htq0vjXKlnvbTr1p0cdyqulJMOF80YaliLAXaM6z2VywPsvrlT_fXjQGh7QhDgdoNBFv-4j0tRc6mgvF_muAyXYcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
گزارش‌هایی غیررسمی از فیفا:
❌
فیفا قصد دارد «تمارض یا مصدومیت ساختگی» را به عنوان یک تاکتیک در جام جهانی ۲۰۲۶ ممنوع کند
❌
دیگر اجازه داده نخواهد شد که از آسیب‌ دیدگی دروازه‌بان به عنوان بهانه‌ای برای توقف بازی یا گرفتن دستور فنی از مربی استفاده شود
❌
بازیکنان همچنین نمی‌توانند در این مواقع به نیمکت ذخیره‌ها بدوند تا دستورات تاکتیکی بگیرند
✔️
تصمیمی که هدف آن افزایش سرعت بازی و کاهش تقلب است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90606" target="_blank">📅 11:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90605">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEJTLijKJUpSjbiwjKad3JVoNngbCIAUx1nAOK51OVL7egIxgyIaUw-aOAxI6M5FyeaS9OLOPBiVPon4N0iR2yGiUrCknG_87yEhw1yaSxCdho8NehrAN96IJnnXyPVDa7BhCWdcJJTiQpJs7lmJjg4_-UyVKlh8OqtsgS6xUa379fc0hSViRIi_76Z_mrXq2jDONVwQtnHcx413susiFYuNm39PeEXrtD5lfA9nrqTDFBlecwWsnFPJkdmHat6NI34TWAZHewtu7OWNW-PdmuOvsFCqz7RzCPMxWsO4j6nm9TNUVSLBJPNXRwKBVVjoca65RQCK0QtWP7CVZVHB6jfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEJTLijKJUpSjbiwjKad3JVoNngbCIAUx1nAOK51OVL7egIxgyIaUw-aOAxI6M5FyeaS9OLOPBiVPon4N0iR2yGiUrCknG_87yEhw1yaSxCdho8NehrAN96IJnnXyPVDa7BhCWdcJJTiQpJs7lmJjg4_-UyVKlh8OqtsgS6xUa379fc0hSViRIi_76Z_mrXq2jDONVwQtnHcx413susiFYuNm39PeEXrtD5lfA9nrqTDFBlecwWsnFPJkdmHat6NI34TWAZHewtu7OWNW-PdmuOvsFCqz7RzCPMxWsO4j6nm9TNUVSLBJPNXRwKBVVjoca65RQCK0QtWP7CVZVHB6jfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پشت‌صحنه فینال لیگ‌قهرمانان در استودیو گزارش‌ ورزشی که دیدنش باحال و جالبه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90605" target="_blank">📅 11:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90604">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=Eg78LZnDHjUjRUQZaNs3ATOLWoprsGX3snIp4Z2IG5c_s9RJEGYC5HsSN3Lg5yEHab63EbzLmwxZtNSMU0AKTDW2twmFAfw1VFpj8crFc7SQIsaVWMDyvx3OtSHiSX11aG_XdRs-uRPBVnVwtyRu0qIHEt7wbxtO6Y2d-5kMSer9TFrKh-NhN9qKSml4FvIxvFFYtDSJLFRporBRx384oYkoyyalUU6oIr5w1CfJlthyAS8voCU5qtkNb9HxF6Lz60IJwU7XpfNhwkHFnYXeCUkoLaoCvMRcP1_SdmmFeYsFrQ3q9rvsvKy-mKNsBG64M1TRcOHGCpXixWfvFIUV8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=Eg78LZnDHjUjRUQZaNs3ATOLWoprsGX3snIp4Z2IG5c_s9RJEGYC5HsSN3Lg5yEHab63EbzLmwxZtNSMU0AKTDW2twmFAfw1VFpj8crFc7SQIsaVWMDyvx3OtSHiSX11aG_XdRs-uRPBVnVwtyRu0qIHEt7wbxtO6Y2d-5kMSer9TFrKh-NhN9qKSml4FvIxvFFYtDSJLFRporBRx384oYkoyyalUU6oIr5w1CfJlthyAS8voCU5qtkNb9HxF6Lz60IJwU7XpfNhwkHFnYXeCUkoLaoCvMRcP1_SdmmFeYsFrQ3q9rvsvKy-mKNsBG64M1TRcOHGCpXixWfvFIUV8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اکسپوزیتو زید جدید امباپه درحال قر دادن در کنسرت دیروز بدبانی!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90604" target="_blank">📅 11:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90603">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSVYxrsaXdOsl0XdY_oTnv-QbSjZegu5saBWYWnowuc5T9whFIevvpFxxM4zz4QGWkgijTtIod9oo9Py7Y1lP3BGplTmoaSWBhgaRkkeh0wn117dQ-dcbtlsEdI8IkO1GfIL4Re72TUvFyVKjgyyRgAhcNZam05jBqoZR9BJZnoxGsU70ZWqYeYk8zvTaNVDAqPumuEDLqLmct6XvdbCZtD1_uu2ajHVqZHTQ2EXnQ1Zm3c3aAbLLa7rL-aazfQpd5Shu5XqJaiyqauWgNd1B_m1tt1bwW167CKhTudanwejHcJZKlXAnypU56NEiFc8Gp7Ous7ovFm3IzGW6idLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
👋🏻
جیمز میلنر ستاره سابق تیم‌های لیورپول و منچسترسیتی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90603" target="_blank">📅 11:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90602">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZaBQdD1VDrs0IKWYRmlSRRymvCMfmvqLqLgAb29en-HCdgEfUMliELpiG-eZXXdYF3bBKbTH3xAp2QHBN0ROSMzAHvNi6UNALzV2310RAcR7sH-7YhFc_Yju5-ey0uPAKZtCkPs1Yfy8WMN50bDyptk0wTnui1umlhuzIPsoriI9BBNWcUwTtAHRWqn3lZiMwUb-GffyN05iew3mC9wQUyWz_qQiiQ1bYi8QnaeVSXHrV0Fge23H9WV5bT1uSgYdI4BzsYip05A_1e4d-of3F8zEYfScXcJqlGa99f6YpblnymefbQKqrmejQDMqUw16bstAt0UT1xWMo0uzdJDkDik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZaBQdD1VDrs0IKWYRmlSRRymvCMfmvqLqLgAb29en-HCdgEfUMliELpiG-eZXXdYF3bBKbTH3xAp2QHBN0ROSMzAHvNi6UNALzV2310RAcR7sH-7YhFc_Yju5-ey0uPAKZtCkPs1Yfy8WMN50bDyptk0wTnui1umlhuzIPsoriI9BBNWcUwTtAHRWqn3lZiMwUb-GffyN05iew3mC9wQUyWz_qQiiQ1bYi8QnaeVSXHrV0Fge23H9WV5bT1uSgYdI4BzsYip05A_1e4d-of3F8zEYfScXcJqlGa99f6YpblnymefbQKqrmejQDMqUw16bstAt0UT1xWMo0uzdJDkDik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه صادق درودگر راجب مصاحبه و مناظره معروف و جنجالی شبکه خبر
🤣
🤣
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90602" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90601">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=M6YG4S0RUaz4MTfX6o-jdYgL-mR4bCyfK74H82YIJcZtRBFGi7ERo4cNBqMWnQWafnShoGRZS1MzURf-l-vfMK38L-zXuM0bJYgPRwgqLEvXhX9TFnlj5J4Xsc_bOo4Dj5xthYFL67KaBaE9AQURHz2Mb4RvlJVlBMfTk9Zzf2wzQ0fF8EJTSYMcbKzA02yL4y-Qm2LAOhU1voU8ldTIPV77qPzmsTk5JKA-B_QtX7ZvF08gu3iwJXGVZd_uZMTMXeTzhJuhm7Nobrfre5CzoZUi-jgcCN0q-fTQT7XebbrPndpeNeRdugx40BVBKRu-hrU5XMnvNHWZlW21LiucXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=M6YG4S0RUaz4MTfX6o-jdYgL-mR4bCyfK74H82YIJcZtRBFGi7ERo4cNBqMWnQWafnShoGRZS1MzURf-l-vfMK38L-zXuM0bJYgPRwgqLEvXhX9TFnlj5J4Xsc_bOo4Dj5xthYFL67KaBaE9AQURHz2Mb4RvlJVlBMfTk9Zzf2wzQ0fF8EJTSYMcbKzA02yL4y-Qm2LAOhU1voU8ldTIPV77qPzmsTk5JKA-B_QtX7ZvF08gu3iwJXGVZd_uZMTMXeTzhJuhm7Nobrfre5CzoZUi-jgcCN0q-fTQT7XebbrPndpeNeRdugx40BVBKRu-hrU5XMnvNHWZlW21LiucXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
#رسمیییییییی
؛
گل فده والورده به سیتی به عنوان بهترین گل فصل لیگ قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90601" target="_blank">📅 10:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90600">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4qnTVle0F_-Ta0eScPjI2aEEwfpEwKbxoVq42bZ4YpPMP5InExieOm_xSKizxfgCksYQ6hXCyutq-V12Ch2i8zPWGk1Vy8MVpL-0sAT3zubqjU-W4BxUdadq63_9N_WbGcJd53HGvgkkfQiXgYH8tn-VEoP-UUrvgs3mBrCiqApgKlXZnqX3aEz_Or6aCCNvMiW-8yxKRixdiBvFlhX_bu-OtEgueoKbaU8hdA7Z2xg98M2Dqil3OaUJAVtBkB4hQlPmL6DSgLMH_DQ9ntomTwrX26L-D3_mgWzvP5PNWTaftNuTHhrtLyyB4iFxUA9notxFG3PVmVl7kK7onzuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
علیرضا فغانی اولین داور تاریخ فوتبال با سابقه قضاوت در چهار جام‌جهانی مختلف
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90600" target="_blank">📅 10:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90599">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90599" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90598">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVU8QcrNxnCf3Qqjx-ncHLDYy4S2moPPOTAbbyrTDfaOutXz0wtPGIq1uz6rxVGJ8gitYTylhvYIqjaVmdHz9hDHTI7jw1hV1QpkOc3j2xkrnvjTjxS2hGVsaauXOI7ZZ3TD7rnotpQU16twkPo9KL48oIu6wNoXj64Tb-X80ILrFzWxANrp6TOALLM2md94AMp6MjX4dPOes6wuqop1Mbh8JTDnRdijE-5AQf_mE7XZilmIflTYp3RQLz6iZCl94AERgeg79PjlOvImNdwe7-8lbluf9ehXzc-wut2DI_h4qoGa5Ck9OhcG56tG-T2E2VLXe9MXoTWw7VTdVohyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ گستون ایدول خبرنگار مطرح آرژانتینی: با جرأت میتونم بگم که آلوارز در نهایت از اتلتیکومادرید جدا میشه. پیشنهاد پاری‌سن‌ژرمن بسیار بیشتر از بارسا هست اما آلوارز فقط و فقط به بارسا میره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90598" target="_blank">📅 10:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90597">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=sMnveafMz07SYNr0e3GgX3fnWJB7XZSHa5YzyQgiR33ZfwTwqWfMvI8xqPkIbxGRmvOnkqeZ9yaM-h7L91NEUx6qUeM_DePUHa2E9t3kSRPV8j3WpxYSHIvPX23g6NjeIKOP4ipyZPBYlclScmDPHV9kESQ7mgZ5vE6od1pIZxV2hkfBtdOZQavZnCgdH07ndXRXsjOQyU1Xz6X8XOwNl983TCl4Yg88O4GwNqeKVPQ-AXkbCBTF2JqEGZa2oHKTUbchmniFpqImeErmGg_rryRYxUzcUMtnnDYZ7SfC6_wrqxpBwotQYYOqoa7fog2Dt7lF_-oLath2PIWyziMK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=sMnveafMz07SYNr0e3GgX3fnWJB7XZSHa5YzyQgiR33ZfwTwqWfMvI8xqPkIbxGRmvOnkqeZ9yaM-h7L91NEUx6qUeM_DePUHa2E9t3kSRPV8j3WpxYSHIvPX23g6NjeIKOP4ipyZPBYlclScmDPHV9kESQ7mgZ5vE6od1pIZxV2hkfBtdOZQavZnCgdH07ndXRXsjOQyU1Xz6X8XOwNl983TCl4Yg88O4GwNqeKVPQ-AXkbCBTF2JqEGZa2oHKTUbchmniFpqImeErmGg_rryRYxUzcUMtnnDYZ7SfC6_wrqxpBwotQYYOqoa7fog2Dt7lF_-oLath2PIWyziMK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیکه علیرضا دبیر به پزشکیان بخاطر پوشیدن تیشرت
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90597" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90596">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq6YFZfSmhHCvJMiYjUMSMbzIf4SRGp5GIDJnZBtO6EyDMrfSs9KZ5C24b79hGkTs9tRm2Gf2R7lVOeDAtD2Ud47Bxj1e044LOJoknnYhV-uZkV37-vFe3qh_ypTNdwOWWP2c6tkHk8fN9yn66TfcaqtdV9WQI0ReLUiZactkUwhSj-1bM1Wtv5qJlVGlr8ljagVbI6RV_n30KieUpDvMqeYjixnZhc6_6AVqKObb9LRIYFSfI8GR03L-Lzcy6wzyu33NXteEX6O82kTDorDgH6-YGTkA9zx3dKNWvkvD3BuKwrRs8kXsHEODoAU541gZUiT8tcsrH_G6herOH-Q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
تمام استادیوم‌های جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90596" target="_blank">📅 09:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90595">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2mU_f9O9zUTgjwgicPi94XtcWnwaGJHoScfYF1nUzuLJww0hkH9LCqEM31z8oSMde0CWnaQjY62KC4q-uCtqom5Lw1-dHafSl8zHy-sOIbaZwwbWM-mTVGGOSBLsD87-AlUYWQmW5GVwKq3OeBeEoRa2hOWp1EHHcsxL8FUlRjR8Xb-c-0vanIJ3nBUonqm0I6_BJurecF41dM-xgG2IoOpq7cvNBngjeFpk97cxZkwFIXoCn9bMigabhHze8T0FsWWcO-SHr_K1KP7rgO0auCdF3ZIKjp0EGOTunWsV-Kyi0YBAgGOAXtdMoBImXaRBPgAdxzyARBCcofs8GzqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابراهیم‌کوناته‌ستاره خط‌دفاعی لیورپول از سوی صندوق سرمایه‌گذاری عربستان سعودی رقم بسیار نجومی‌پیشنهاد دریافت کرده تا به فوتبال این کشور ملحق شود!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90595" target="_blank">📅 09:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90594">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=aNmji4rvUko_Qw1Av5EZQqj4mONIa3MC9IiRftRw_a7_NIjv0wH863Nbo97XEGbuhzHM0nda2O6M1vlCHfhDNx34pY_zrah5HODcdM-3Kmv_ngegrLt3k3NAhcOG968klNq37w_qz8bl_y3VuDbltTTR2GnAJhFV1Vxftw27VQn4TFLrbnsSbvvPf9EuIAFMHk3a-jIGQOiQ_yQaavhpRoivgGrDQDlL4zfgSYfZr6b4DidrIM_buAtCEaFJUkZvKeG47KSV2hRaT8bji02XmaIGIWergL65eNLDU_NzPDMdNQZ1nDuDjjOasD9wlrDqMzRr1Q17FlQO07zWD_882g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=aNmji4rvUko_Qw1Av5EZQqj4mONIa3MC9IiRftRw_a7_NIjv0wH863Nbo97XEGbuhzHM0nda2O6M1vlCHfhDNx34pY_zrah5HODcdM-3Kmv_ngegrLt3k3NAhcOG968klNq37w_qz8bl_y3VuDbltTTR2GnAJhFV1Vxftw27VQn4TFLrbnsSbvvPf9EuIAFMHk3a-jIGQOiQ_yQaavhpRoivgGrDQDlL4zfgSYfZr6b4DidrIM_buAtCEaFJUkZvKeG47KSV2hRaT8bji02XmaIGIWergL65eNLDU_NzPDMdNQZ1nDuDjjOasD9wlrDqMzRr1Q17FlQO07zWD_882g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به کون هینکاپیه پرداختن
😂
😂
بن وایت میکروفن گرفته دستش داره اهنگ میخونه هینکااااپیه کونتو نشونمون بده
😂
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90594" target="_blank">📅 08:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90593">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=PyMtfyM2AMuWXCOpijVdGvtVKJNp3KZcYLXPIGSd8UcZDm5v0A3Gk_avhVt0wdcdP0K6PVx7XPv6Zd9q4GIMac2_3SHg4ViMAexi4W0VnmBI43KdtlVTUV2Fm0L5So93GK-sAHSK2D8zzl2ETe4TZr0Fchw9EKCw81jsZ0O7lxF3NfkNSnEzlVWt_mrMc7jsNBRNvl9_TMB0c5PGtfUhfM8wvWZlcv84T4yAgacTLgUOLIKOca1azV80bheMDvVfavlpvgNmiyqSUvXsKemBhLPcm3dt4luY3ougODj0eDitC8fMaU6y9LWqJGy4X22arfDIwsgcoBvk8-pBGIZq-w_oWKNZSafrWDLhJdIEQtuCWeXjUbGY5BOiN88NY_ldKT0GWBCbRoZNeabvTARWR3XIWRrmwOUPlYicejZBnyYOmkkA8pq_ij1OY8K-8A7l555rEuJZD3u8pn0s3uK3O7qCreQhYGS43DSosKlpbrqqsvheSbOKXdmXgfqfS42oZUuEVlnDAH_cgv6MUzTjlbwHuH6W0hWdfT9OdOve7bQBD8Zqz3imjacKJae0NyWRbRmmndgd5Tt52vYUHiBptFkWGE3IJyG4C9_MBssYlpiOzEE6rnU_7JsvcNAVNoOKSZdgo6BdTGaR7RkvL1Y1F6dNQReY0hM8ANXTpPXT47w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=PyMtfyM2AMuWXCOpijVdGvtVKJNp3KZcYLXPIGSd8UcZDm5v0A3Gk_avhVt0wdcdP0K6PVx7XPv6Zd9q4GIMac2_3SHg4ViMAexi4W0VnmBI43KdtlVTUV2Fm0L5So93GK-sAHSK2D8zzl2ETe4TZr0Fchw9EKCw81jsZ0O7lxF3NfkNSnEzlVWt_mrMc7jsNBRNvl9_TMB0c5PGtfUhfM8wvWZlcv84T4yAgacTLgUOLIKOca1azV80bheMDvVfavlpvgNmiyqSUvXsKemBhLPcm3dt4luY3ougODj0eDitC8fMaU6y9LWqJGy4X22arfDIwsgcoBvk8-pBGIZq-w_oWKNZSafrWDLhJdIEQtuCWeXjUbGY5BOiN88NY_ldKT0GWBCbRoZNeabvTARWR3XIWRrmwOUPlYicejZBnyYOmkkA8pq_ij1OY8K-8A7l555rEuJZD3u8pn0s3uK3O7qCreQhYGS43DSosKlpbrqqsvheSbOKXdmXgfqfS42oZUuEVlnDAH_cgv6MUzTjlbwHuH6W0hWdfT9OdOve7bQBD8Zqz3imjacKJae0NyWRbRmmndgd5Tt52vYUHiBptFkWGE3IJyG4C9_MBssYlpiOzEE6rnU_7JsvcNAVNoOKSZdgo6BdTGaR7RkvL1Y1F6dNQReY0hM8ANXTpPXT47w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
وینیسیوس دیشب با این گل خودشو برای جام‌جهانی کاملا سرحال نشون داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90593" target="_blank">📅 08:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90592">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfleCoC_Nz2viuRDZHNjUvjQ7pdJxIwa9Vu0QAGYtWuqTtElxP-lk98P7_03_eeuW6LnXfSg3raE_YOQMxAV_ZuUKrlP8ncoWH06pDfWQPA_i-6eoaKr3Kw4q5-d10QrdRHZM_80-NNjenbGyf12K0-4TU_ymKykwa7X_IS8uO-NWAeR3006affS15k42RdzuW36ilbuV4iDQQu0ETX_YKDhEAujWv5EH3JpMsFOGk_Rxdab34XT_YNAUPNEN04Lhccd6KNeeFlXqlQNYI3FjaIxruE8viZHGMMA2_ztGcV5lLhqUefVHsWLXdtvQJWdIVjfmYqxsXzhPqVuf6C1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🔥
ورود به ربات و مشاهده :
👉
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90592" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90591">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90591" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90590">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXb2-3vYnJ1Dy7ERpUUYtKl6OHhSYv_Q0gs773FyoPsNemFB370dA1xAp02bD1X24YVRGfPKXKxFh9480JXbb6DL7YwkHOELCn6pIeHCVuXCERWjNZWvK6vIbeOujNu1F8lt-pS7lfwm41Tpw9TmDt3cKySYJHG534VcyRlQIy1Q6s9ZufOrla7x1jdzUBaMjOCoc4-V_lyuf8ttTEC8IaQnh1F31HHU0bnFkGvwDY64piBgbBVCIZjgDLQSqdQM7mN23gL1yxpj1ksHeHnOY_MWmTymOHq6nZ-BgOzfSGd1VaYrsOhWu1W_x6ojR247eq8PZkoD9DbatGsmKd7zAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90590" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90589">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1B4F7RsKehTEXJFZ3UFww4ymtjYMseIWRce8kiRuGXzen85kYrjE9ardCNkx6fk4w2tJ4MbROFyMuibueJ6hpoLJt5hjiTINoEwyxJO2kjl3OcpzZcdbjryzWDwpky42VUqPHrftNeOVoi6bkYO_vRffvfdhgkyPuWPSoofuyFJ3uZtkLd7EMvUaC8gN_AMEvA5VqHn9VJ54Yi4kR1p149w8aFWn4jEHnyTYS_w8hOlHup8PxA8tpKvDhTxlMfSlJhhXBuGeDdHzacKQugyKgzJGGtCCDOQRsJMN7xes37Pw8HiASE9pzzK7OgskmCaYxauH9eYuyz0VcOIR6ZOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید از اسطوره های فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90589" target="_blank">📅 23:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90588">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎙️
مهدی تاج:
بازیکنان تیم ملی دنبال پاداش و حواله نیستن، هدفشون از صعود فقط شادی مردمه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90588" target="_blank">📅 23:13 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
