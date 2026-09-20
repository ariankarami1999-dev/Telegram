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
<img src="https://cdn5.telesco.pe/file/eRSeeeySrNGfWjrabe7o3KWU7ceNymieZ__s1q_MOjfO42DGhv6rqap40I4-myINheI013Le5g0HGYxVXBPC-9Qb14N0InbWd_HWgOqqbYVIszmJXkX-E4rQX2Ge7-hrNTzO4BGJklD8c3BDBS8RQh45b8BhH4j1KHeW4s08DSt3pq09w03rkcd7HLct2eoI3b0bOGk4bQEUvgxfVsthWExpvO7kb7-JDWE84uzHvPD3wy7VU2Y0zMe_CJcPEWkx-LXo765A4ZsTforpfSVV9MA3KAGZvVVrsUKD6p-G7T9yqyTRbP67iOmSfYe6dVm-i5xWfdA_dEpr4HzcKDJlCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 407K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-106928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15GtKUD0HvUTmdzT7M4lIOTGksS0bRRBCgSCO7L9eEsAWfSanO5fVOIWJHcsrk-ej_vkqaIhftDkpmRMBMApe8T9ayU7biIp52qhXLOqCYSk7f6f_0mzsIsdk9xRMWnKhdDkOyAOwJSViD4ZYgZOWkah1PcADqWOr32DGsheuEIVZa5lg0iFO_i08emMAwcLzDn2hZvObaw_Du2zR7wSJ3XBect9wkTUHrlWNRD9EeAz72PAOKXT7NshBD4n-INXFHl8pvPdOusmP7taJGGH1kKR1C6WQn_DUiQLohfYQKLZM7qie6IyGj39Z1LgnBGpNB7QpjVLVeSrYfzB6s54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشون زید دیومانده هستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/106928" target="_blank">📅 13:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=JhoYQtNv8GcS_9jNrTW6qtwmha6zqXY1wi4uIqCXy8vY89iXtCYGPFb0BRm5WK6QaB-s7IYdVt5Jwg6vo2EGDQaSwQ_ql8usuCod2yoS3QK3ItqRph9_-krOixB_6vpWzNYtpdl3n-jkcXpQHBEehTk7DPoQl1YWEk7uFqNT7kQGtxShxc03MQ3XzqHLd4nRKc7DCf70BjMoi7ZneDRk7ZXCCEvhWodRN7iLc4FudMFLgaPG97ZwEq8rJPDkj99VLAZwpz1RZA0odZTanuPSRrJP0j9Q1eL5plFErCpnsWMqElsp59xXEmuUtq5bBxT8Qa7VkBF2-MLrHEX0aFdqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=JhoYQtNv8GcS_9jNrTW6qtwmha6zqXY1wi4uIqCXy8vY89iXtCYGPFb0BRm5WK6QaB-s7IYdVt5Jwg6vo2EGDQaSwQ_ql8usuCod2yoS3QK3ItqRph9_-krOixB_6vpWzNYtpdl3n-jkcXpQHBEehTk7DPoQl1YWEk7uFqNT7kQGtxShxc03MQ3XzqHLd4nRKc7DCf70BjMoi7ZneDRk7ZXCCEvhWodRN7iLc4FudMFLgaPG97ZwEq8rJPDkj99VLAZwpz1RZA0odZTanuPSRrJP0j9Q1eL5plFErCpnsWMqElsp59xXEmuUtq5bBxT8Qa7VkBF2-MLrHEX0aFdqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رختکن چلسی بعد باخت جلو برنتفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/106927" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=ETF9-mpnCwieix9wbTmewedhxmAlH_ouDkwn6XydJbErHXhjcBguJQLjdp0xM-yCOB1meT3Rxz6ySz2mg4961UpTAYToDc740-Lv8ru0wWDC21Yr60brlIqnjo216A96RyFAml-U_gehlhzMEw0KqRQP12dwmNEM8dJ9TmqvXOaPH30G0_XB6Iu-m4YrB6EJobxp_7z2qsZYndu_4tpzA_1gE_t6HTS90FBKMX-cZScSAkdUrLNdl_MRYHrCUgSXbZZ3iGr9zyHtVbHWZl7raszNYsAGeMvIpb-MSszMGmsohNojpoPLxMouwA9QG9FjWj8-1FuWjhc1ZRcgd-0KaEUQx0tDl12YLYyo9G0I6AIctL4nHylfMl4tVTuS_cBlNgPYqPeXdLjsQ1v7zO6FOID2rrdrl2erCSV6ISWzXEvAADQWwAvlrOmvcs8WCd9ejGgDOGp3macPFGpsXXxknOTWF-UiLFV8pL5WqatvIr48kyUaoRjrEpICQsy786H_VjDxhQYyml2ti_UYO1EBZCQnHLgaoEpHb_aCrfwZK6OhpjaojmZzLGGLkHI78Eps4EbJez9UDmxlJQ4PN3kvrExK8z9lhWoj877lJjbgUG1oM-vJ2fX-C0of7MPF7CP-1_N84OvkcW8MYjEVUma2nqVx07vKCtBu56CfVI6UDR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=ETF9-mpnCwieix9wbTmewedhxmAlH_ouDkwn6XydJbErHXhjcBguJQLjdp0xM-yCOB1meT3Rxz6ySz2mg4961UpTAYToDc740-Lv8ru0wWDC21Yr60brlIqnjo216A96RyFAml-U_gehlhzMEw0KqRQP12dwmNEM8dJ9TmqvXOaPH30G0_XB6Iu-m4YrB6EJobxp_7z2qsZYndu_4tpzA_1gE_t6HTS90FBKMX-cZScSAkdUrLNdl_MRYHrCUgSXbZZ3iGr9zyHtVbHWZl7raszNYsAGeMvIpb-MSszMGmsohNojpoPLxMouwA9QG9FjWj8-1FuWjhc1ZRcgd-0KaEUQx0tDl12YLYyo9G0I6AIctL4nHylfMl4tVTuS_cBlNgPYqPeXdLjsQ1v7zO6FOID2rrdrl2erCSV6ISWzXEvAADQWwAvlrOmvcs8WCd9ejGgDOGp3macPFGpsXXxknOTWF-UiLFV8pL5WqatvIr48kyUaoRjrEpICQsy786H_VjDxhQYyml2ti_UYO1EBZCQnHLgaoEpHb_aCrfwZK6OhpjaojmZzLGGLkHI78Eps4EbJez9UDmxlJQ4PN3kvrExK8z9lhWoj877lJjbgUG1oM-vJ2fX-C0of7MPF7CP-1_N84OvkcW8MYjEVUma2nqVx07vKCtBu56CfVI6UDR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اقدام عجیب و جنجالی سیگار کشیدن مجید واشقانی با اردشیر رستمی در برنامه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106926" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1S4Iw_slfXumC44s0F5NrewQFjcTfHDpRtFwEOHoVg7bYxOzAfroQ55pT2yJqcCiMFWyMnhb3HUG2btbfNXO3pOeZq-Miq8pGqsJTJ2xVzjCYKMxK6waqy5QqEsTI5Pax8gdO8nURWyaJpEAvsGHLuTwnpV8iBe6U1Tqv8MWxb_9EpOAcTd5lTn8CTNcTERZOo4CrBbTDn6uxfkCE5lRuoARt7aPTrEYOBcKyxpVxD0A9-W7UBkQ-ToqtB9szjPy1qXUCeZeNfZphBofM5J_JeRIXUO9DRUBS6ltynF00aB1T459Hcfr-aE1xTYUwkFZ2E4L_DtCzK7g9Kes6huGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106925" target="_blank">📅 10:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز متفاوت و جذاب از تاتنهام که برخلاف نتایجش، فوتبال نسبتا خوبی ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106924" target="_blank">📅 09:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=T60kH4uVgFNqSyp6D19b9dEVbmpDWvjqL20fyi16nIHzXusKHMzRK5db3EnZG1vvaumvIFrHuiT9OveX22Q_SOM54iF-RewsgNNLrrli0anwkrKzZwGuB053hzARZmQSh609VGn5uiIq6F6_w4hU-knLHD8ujc61aqbPzPTkieTgKuFXBIU-ymRFkC3HB9pZhAkRIuhlFA9-tEO1tKZEsHHi4wavZdvKGB499Ie2UB0ySSVfFMlWh8TFb_Up89EnwFTNRYM54BzaP0Xb8uuZcVzVFsykSn78EACWLXAACM4B88id8zBDZxpGpQTdQIYzxFbOZd6E6LvBOoEHsSzAlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=T60kH4uVgFNqSyp6D19b9dEVbmpDWvjqL20fyi16nIHzXusKHMzRK5db3EnZG1vvaumvIFrHuiT9OveX22Q_SOM54iF-RewsgNNLrrli0anwkrKzZwGuB053hzARZmQSh609VGn5uiIq6F6_w4hU-knLHD8ujc61aqbPzPTkieTgKuFXBIU-ymRFkC3HB9pZhAkRIuhlFA9-tEO1tKZEsHHi4wavZdvKGB499Ie2UB0ySSVfFMlWh8TFb_Up89EnwFTNRYM54BzaP0Xb8uuZcVzVFsykSn78EACWLXAACM4B88id8zBDZxpGpQTdQIYzxFbOZd6E6LvBOoEHsSzAlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😢
جوآنا ویتژیک ورزشکار ایتالیایی در مسابقات چین یهو وسط کار اسهال میشه و بی‌اختیار ازش خارج میشه اما با این وجود مسابقه رو ادامه میده و قهرمان میشه. در نهایت از مردم عذرخواهی کرده و گفته امتیازاتی که گرفته رو ازش صرف نظر میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/106923" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106922" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNggQyWyHlEyUiSuL6gVNQmdaaeTcYvRwwEDK9BqVAFZyxQfNomWhP8B5iu147aHwzJz0qrUQPCNRbZFmegJyGBoRPZeaIWQujrYPwgPdDTOosJYFVUuZ1rR5AkifXcdco0imGyD_8EsKS8cALxgK6xbeJbzl7vX5yrqosZw2jq9oWm8VbIDocCPo0VIyiANQYjVqxjrsUyBVRG57kturJR-xtlEaeu_Fthx-f4KLY2QVAipWU9qgpXLDsZO0uffHme7Pzfnp1ufeA1aSIT3plokITRRff5qvCSVQzekLPC-3CCNuG2GnR4JJaVXg8BWUTtbquhbk72NsMGKtupFvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106921" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
کار جدید حمید سحری از برد امشب بارسا: واقعا کی میخواد جلوی این بارسا رو بگیره؟
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106920" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iitqhZeAqWIL7H_KMOnmjdmZ3fEaet__KvmJS1KyvjQBe1KktfUtty1hCqq_UemIK1gMmUm99c4WTA5Wr6jm9lj07YV1dcBfJmwkyUUUsNJG4XuKDah0AQ9XnI9OjcnL9UOnB7k6LwC176CK-AZGZ5ZIYkLxT1ecOsdo_tcoGai3QYFwF13-rzRFsJ8ZVpnk2je6WSDWF9qFRW7qC9q19HcmM0ulCvoc0oGzz0FX3LH3IO7E0Pd32PVsl8JBNhft1aIJvRwrYpFurLJt0tMPgcJQN0CXqRdPUGa0um8XzjlIjLSIK_gI8LwCNaY3HgoSb0XecLklsVg4dYZ8wucZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106919" target="_blank">📅 01:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwoqs_iI-79DrxjjnDtZ3mLVFQ_C5hfc_nlfxsCnqMI6Ck-RJa7adSvAxejqH8Vl5Ik75_J8K2HWuSynizQWiFipwHXgutceLapuuANsZfN6whWOab_i73e_rrkUq02xRnSVrAH9fe23n0olu3RoeA467QoA0yHT1VyDhZONKG8awq_vKbUJySAWfTP0PkvD4H0nGhvURfA7uVND4JnGPeoh50i5kAlleP5eWMs8Ml76rHGjXEb9B_Gcl-jjHyxSj9yAROLtcInmD6-BFarF-OMEr0MUb1n3tAW2UTTdg2OFePYis5v5dZD5iOn9HUhWbwFcEnvZfIUG6-eQonz2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇪🇸
هانسی‌فلیک: شگفت‌زدگی بابت عملکرد رافینیا؟ بله من شگفت‌زده شدم اما نه امروز بلکه دو سال پیش و هنگام اولین تمرین با این بازیکن. او و لامین دو عنصر فوق‌العاده تیم ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106918" target="_blank">📅 00:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxuVVLkRzcX3ijjOENM1cJ1UlJ1L6Vo_hUOUrg81cA3_u-d3tZDWmC7ocpPg4OuLBTvdjQ2Qk9GJjWqa1C3sSAWlZpMRiFXWGxzvQ0VoYqesmg8Lp5TfPLra_iGf3drEKFem4LuWrnDTKaaRSXFp6Ai6PsRlrGNxqminchyXBwEqgCrlbO70OT_NXZ3AwQW5N546ZxrJqJO3ft8POve-3KIe3pArT_fDITdD9ktxJ4zyYc8MYtlOOjmtLSKWpCsUJfDjwGBahv_dwoIptgrqjjAUlRWM3RlSzZ9SBjIO2xHLRSPLBpLUbAAe92zWDdYW12zQtFg1qIq30OVe4IAPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد بارسلونا از شروع‌فصل تا امروز؛ بازی بعدی تیم وحشی فلیک ۲۰ روز دیگه مقابل ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106917" target="_blank">📅 00:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnUR6Y4X_iynVwb0WEWyzDD0lpgme0PZS8qaaw4FVBGjNKQJl1V8Wh3Z6H8Lswg0VdEwZ7X7Nr9x3ehhDoP0a6we2KScQ2h7RHR-Idn3a6OZXXqdJjJhoZ5PDr32VnWBdpfNJ-x4Jg9bjvd-BM-0Z4ND6faF0rBHQJZimVhSF2cFNozIbexYTERe3G3P_XopgInwE7z0oNddl8snbP1c3pZ0mo-W3fGpp3-z8WcUaWWR3uJ_maoqj6UTRcyRkMpCcV2Gx71_fEt-vw1P5S00abcyppjYJv4ebMbzedT3kV-ZLf05XNI29BiF-JI6_4mz1jGOCmeejasy1HpTIpyc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
هفته‌هفتم لالیگا اسپانیا|یکه‌تازی غایب بزرگ بالندور در این‌فصل اروپا؛ بارسلونا با هتریک کاپیتان رافینیا در جهنم خانگی سویا برنده شد
🇪🇸
بارسلونا
😆
-
😃
سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106916" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCmLAhIwuF2UKEfLAoM4BEwQWXH_b-UZUWjikJv0Rs0-Z6G0_0fDSOFa7zC6xfN2jQg6lE58TmVWUWqLwqbt0KJGdrj2_VNkY3-pyCPbo2NA71f0Q1_xHXrSUq-8gF-G1ffodHDpSUVIa39mK45VTY9FyRvLzvCwKWMFBvBSxepFuGz_aI08Ey_cKME8880ywb7vuic0Xa_4QnRU1SJmJoLVQuWTjrgtKh6Yukgzw6VBD3Q_ensnxaNa03jofvnCrjCqribI8kywsmpRGMgGqnv34nMtGvU5Pod-LsuRQnJ2_rnoBEumm3C2c9FVvsfVF0YvVpx8VEnDF6Y87CKJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
😳
😳
🔥
🔥
🔥
🔥
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106915" target="_blank">📅 00:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Govy1_SgFGvkumRjJvsfQXntfChtyseBKPyd74-1QpvYQ-jtjXEB2mJGrDAtY4YIdWHLL5oJFHmuSW-L0NZdS3iUhcMnNpl6S_7CkBmwbDNses-a-3G-L12s2iw7RzwpQd222a_HkscC6Fl_JezDIQEXY5Q2vqb0ld-NzamNByEGDzgycMfVi5_Q4Iokgx1aGjNg-ugwduZ5pU8w51Bs6JGNGBqjs4bMrOT9t3rkLfRRzmTqQAMYU305yaaavYY5lsl6Stm6t4TRcZukL45sQ6wJOmBy6Y3UKxNO1qQ5KV2xrBkohcb9f0OzF5PPK-EqejEJoMbXNDzma0We1wpRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106914" target="_blank">📅 00:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCgQKh7g8MMhzLFpyuvtZnVU8T_RohyvRxoXUS4hdVoWVUdmeXHHeBBm4D_g_7msNHjucC2cV7NJ2kgrU15NjytYNcPmKZReIPiJURzzAJajteQAt_8iP2mtEXp1IhlClSibf73XlpjdzV015239THeryDpYPpgnnLTs-d677-F1xH8DbL0jVoD8GpANDjwzCfoBE1F0Br4nIRTespROx6ZcCTxYvxQt6IKY2_ZynTJOoCEtQ8uNFVlQMwG8iEVh8NpCnCxB1q69eZYEaklJKszOhJtjsbDhtq4SaILdNIpX9foDEWQwRLiW-LUSlamfDbQ3MnaTJskuOsz7vVj_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106913" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چه پاس گلی یامال داد
😐
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106912" target="_blank">📅 00:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چه چیپ سکسی زدددددددد
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106911" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هتریک رافینیااااااااا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106910" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106909" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=Is5659bkYTbO4cukg2euVoh2QWMeyPSLXbfWfKYOm_zlq70SV7SCXs24U9grzbY-Hmh7THvA2v4aMGafUe6bmNMXhcJ36mJShUzE1G_hGmmcmZ-Iw15IJEpCnj0yoxgVVntBKQ3eZbeT1c-v3bMQV6k8ij9CUVJW9Y-LDwdDBpdEEl8VE8y2mhHlWNHnNJHQJeM9pkpDO19Pwikpi8cw8vw25SZA8ZFGmXZ1-CHwoh_EIxmVCJFJie8LdvzXJm8xRIoTik2qOOFciQtgGnRb6xFqkFypiPA2b3T0YPFrJjVT5SlvGL4XidF2lvd8L9A0xgmb8ZbhlD_njvrgKgKm7xoy76Rxcn1F9_dsKKOLvGwgApYFYpMfkLGwfSYwxNBfi3hyzKjZFv-8oRG8txL_0w4bqDYk_HLPLD7kFXLG5sZ_UpWZTifSgSTsk9sdPjzlVAM5_lAAMRsPrlHjPOpFLNN3apT2fGJroiOs4z_3NF_zLZBWR2laJwCBQKwBwarQqeIKfDGt0S4LCNml_XGNyCcQqjCWGp3WZdkz3Q9TTai9TMu0VHFdSBEzV0vq54LrY7hwXHrThnnC2shX1vLw3NkJSELBX6QTItkEJEliXgiGlQTjdA4xB14TtP78qa32Iv0bxasaHnbUmiOCjbDz_uw8yC92TRCmlmK3_WOeNzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=Is5659bkYTbO4cukg2euVoh2QWMeyPSLXbfWfKYOm_zlq70SV7SCXs24U9grzbY-Hmh7THvA2v4aMGafUe6bmNMXhcJ36mJShUzE1G_hGmmcmZ-Iw15IJEpCnj0yoxgVVntBKQ3eZbeT1c-v3bMQV6k8ij9CUVJW9Y-LDwdDBpdEEl8VE8y2mhHlWNHnNJHQJeM9pkpDO19Pwikpi8cw8vw25SZA8ZFGmXZ1-CHwoh_EIxmVCJFJie8LdvzXJm8xRIoTik2qOOFciQtgGnRb6xFqkFypiPA2b3T0YPFrJjVT5SlvGL4XidF2lvd8L9A0xgmb8ZbhlD_njvrgKgKm7xoy76Rxcn1F9_dsKKOLvGwgApYFYpMfkLGwfSYwxNBfi3hyzKjZFv-8oRG8txL_0w4bqDYk_HLPLD7kFXLG5sZ_UpWZTifSgSTsk9sdPjzlVAM5_lAAMRsPrlHjPOpFLNN3apT2fGJroiOs4z_3NF_zLZBWR2laJwCBQKwBwarQqeIKfDGt0S4LCNml_XGNyCcQqjCWGp3WZdkz3Q9TTai9TMu0VHFdSBEzV0vq54LrY7hwXHrThnnC2shX1vLw3NkJSELBX6QTItkEJEliXgiGlQTjdA4xB14TtP78qa32Iv0bxasaHnbUmiOCjbDz_uw8yC92TRCmlmK3_WOeNzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا توسط رافینیا با پاس یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106908" target="_blank">📅 23:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رافینیاااااا دبل کرددددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106907" target="_blank">📅 23:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگگلگلگگلگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106906" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoFnbas6Ion6k_QIntLDPFx1hO6tuDfuqyeiWa3ky50M5RuTXYZzhpRrajbNYN2vENC9lq8ecQE3WsEFiAw1p24rilDZfNHwwubLLGyPFGtbfPFs_UHUOh_wALNEQHudlMQ3X5lS-dzEYrHy_gXyqtkSny5up43Shth8l5xFvHNDoO7Jp4v3MRXkgDbrN2dgYJunDNkbDZGD7s-Cd7YyybJizJbM0d1ird2RNs9d4ds6EFuudsLDVhu0euDH6E_GywOtnsikS2V8GLmkOh-aK3HGl1Ll7OgIaBqfxxqFfXxOkJ3-BKSqqceZy_H6pPHbvm_kAXH_o0TInPakK7wt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید زلفی و نیما تاجیک ۲ گزارشگر مطرح و باسابقه تلویزیون به پلتفرم اینترنتی نماوا اسپورت پیوستند و از تلویزیون کناره گیری کردند. پیش تر محمدرضا احمدی هم از تلوزیون کناره گیری کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106905" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106904">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e51312166.mp4?token=RXxvGg-HLyyARdktzuHd-hyBn5NqwiXAe5Foe-T19U720VfENo8h2vBAmnq4NP2kk2ydRSIzkVyqcjumnUb6MsHRbOGnf_q2esL5Yx8vhSpR-1LsqBB1wjcDJEYRFUKSEubv1C_qSt44Hh-gyt758bFUxbjfnveiYLx8VubMWeItX0jv8FapKQ9m_o1qAqOEsNjjE7h0Yvdv_byy-gTBRrwu9ewz3SNLNIH8zNNJ9EiflxRpBFPJfuyfa5X-gnQqY-KOluwmgNYOho5XIyxxgEl86x41jN12skeJMoeEgHyaP6DHLIY3Ir4O5kTJqbOy3UvtH29gT66a78SqsVV3omtuSd9lW2HKtv2cb6y-5YBSeaplbjA0ypeXKz088BkNYB5fYCY1INhpYZ6Ixow6euhCBBIrGav7tSJ-o0wAc5Wg6SyDkhS6knxE4dw0jtppnbgSnqFUQrxOTOR6QNu2D_fHfJzZPlWDDpf_CC1DD9_veY8pqHCVidi82df_PtGS6MiS_qU6oqA4sPju3jmNOVBpdzo19FleeNcOi-_Chf7AJpjj_JSP8980GBNdsBh2KrXKy-3TQUIJd7K3PxqYz9xL-XB3dMC7Xl7KxV8zcIma3ZUwBLnESZxH7yayZ0bOxsIRZcNsioQdvYKsEjaPbbeh42CKfDcJ2wYiS9OnR5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e51312166.mp4?token=RXxvGg-HLyyARdktzuHd-hyBn5NqwiXAe5Foe-T19U720VfENo8h2vBAmnq4NP2kk2ydRSIzkVyqcjumnUb6MsHRbOGnf_q2esL5Yx8vhSpR-1LsqBB1wjcDJEYRFUKSEubv1C_qSt44Hh-gyt758bFUxbjfnveiYLx8VubMWeItX0jv8FapKQ9m_o1qAqOEsNjjE7h0Yvdv_byy-gTBRrwu9ewz3SNLNIH8zNNJ9EiflxRpBFPJfuyfa5X-gnQqY-KOluwmgNYOho5XIyxxgEl86x41jN12skeJMoeEgHyaP6DHLIY3Ir4O5kTJqbOy3UvtH29gT66a78SqsVV3omtuSd9lW2HKtv2cb6y-5YBSeaplbjA0ypeXKz088BkNYB5fYCY1INhpYZ6Ixow6euhCBBIrGav7tSJ-o0wAc5Wg6SyDkhS6knxE4dw0jtppnbgSnqFUQrxOTOR6QNu2D_fHfJzZPlWDDpf_CC1DD9_veY8pqHCVidi82df_PtGS6MiS_qU6oqA4sPju3jmNOVBpdzo19FleeNcOi-_Chf7AJpjj_JSP8980GBNdsBh2KrXKy-3TQUIJd7K3PxqYz9xL-XB3dMC7Xl7KxV8zcIma3ZUwBLnESZxH7yayZ0bOxsIRZcNsioQdvYKsEjaPbbeh42CKfDcJ2wYiS9OnR5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌اول بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106904" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106903">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چه گلیییییی زدددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106903" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106902">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رافینیاااااااااااا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106902" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106901">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگگلگلگاگگاگاگاگا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106901" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106900">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگگلگلگگلگلگلگلگ اول سویااااااا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106900" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXmoTuQ_xTWnqUZvNyJg7NpG6RPtt4BCpQ130rjmOEF_9nU6KqDytP2shUa7niBKjQ8fbShNOjaNeltWNXPoMozbA-egNrI1a8HFggQ8LH3sas0c29JTR8qkdfVo10ovmS15TPxSOCY83F-leV9QhecGUknb1yomP_RDnUP4bY3PhVKkH_SzBzYJuAg8CpoK27rE9QCxWauqr8zFpU4DTTJ8i2fYqjJEpUlk5kc6GGOxyLWBRHttgK83-WmfaUrOqmtAIzUWbj4Si8t1y9CUcnm8wSMglOOAZU6OLs1Rf4y7kpRMChJxMeDCCNnRTWFeUz4LUK86s0-RwlW-6Ev8rYI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXmoTuQ_xTWnqUZvNyJg7NpG6RPtt4BCpQ130rjmOEF_9nU6KqDytP2shUa7niBKjQ8fbShNOjaNeltWNXPoMozbA-egNrI1a8HFggQ8LH3sas0c29JTR8qkdfVo10ovmS15TPxSOCY83F-leV9QhecGUknb1yomP_RDnUP4bY3PhVKkH_SzBzYJuAg8CpoK27rE9QCxWauqr8zFpU4DTTJ8i2fYqjJEpUlk5kc6GGOxyLWBRHttgK83-WmfaUrOqmtAIzUWbj4Si8t1y9CUcnm8wSMglOOAZU6OLs1Rf4y7kpRMChJxMeDCCNnRTWFeUz4LUK86s0-RwlW-6Ev8rYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوووووف صلاح ببینید چیکار داره میکنه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106899" target="_blank">📅 22:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106898" target="_blank">📅 22:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106897">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlcsvUzMdmg5HBJxGprtXjWciRn8uxbBuvSNMOXvcdIzRhvuP-tOx0NLKvnrD-1HetEUX4zByKtjviX4ZQlP4hUroNXF-K6s_AwPTRgCNhNrNIDex2XCvPJV9_i2C85YaOviyL4EH34vwgso1IIx5qZkQYbuFitFr0evSww9WcREDDvBt9ywYjHvy6vbuVIeHG8L_t8AhgwSMHAyVhSA4ykdl347jmo5smUxR-Jmf40lMQQlENbYKJuJhB0Ge5787YVISyYsbhsWEjxzFFTa6EjyxlTymw8JMUGf1OH9HbJEznt3ZjYzXnrsYe-wdYesI3BFCdGRifq4afcMfb-qGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حمله شدید دی‌زربی به بازیکنان تاتنهام:
🔻
ضعیف‌ترین تیم‌تاریخی دوران مربیگریم رو دارم. اصلا نمیدونم این بازیکنان چیزی از فوتبال میفهمن یا نه. اصلا امکان نداره یک تیم اینقدر بازیکنانش ضعیف باشن! واقعا براشون متاسفم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106897" target="_blank">📅 22:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106896">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=IavIAsB9Ut04PbXvnwZonH5gAs-8FvQOZzS2MWrSC60tCN4D7v4O-f3ckhcigTuZ3WX5-FFeCxuJm7WlpznHdlGDSDEND8Fhgc0T8FN5nGkIJewdU5EYUZk-bojJXyzElQEi78PG8pGsOvDXr5aD1He6_xjRJN1lhgZnHM2G-RWccPWdQG516LHXPvKLkamyRdlyoPewqIxrHMUJlyIRYMzu8z7qJfxnvyA9K6JYLUUMS1LP8OG5a3rn4MLLQL09ONTv4PwfIjwR0jJdwjIoWs0MpFDkgn8fRBrONdfBSlx-8oEgFEbR4u05oCGCxuSE1hMarWLpEyMzd30yL0L6Or7jhSrA4jepnfKPJhdnPZf0v6Bba-5BjrdFCy6xhBzlwAoIOgaFdtk6hXwk5FG4wXKsNMDTXpQTp1Ry_FALQgXnl5gTluFxnLKP4uIBH60mu2NY5yuMR059PNVzux06fo0J_UnUAU_xli_-6Fwb3afec4eZg2yExs7N6ax8c2MsPOJZr8el06xBjdi_YKbPiIPnAIPI7LNbWhxpmEa-7PqC3r_hICroEBAreQ6Al3jlWBFUyG444cwMt3X82sQkQMSqg5ixx_UtatMcoODG1LrsfWJYA7rtl90zzUo1bPoYsC74Yz-Z-T_gaSQrRDZ2BugBANyMcrD2OPUlnFbpUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=IavIAsB9Ut04PbXvnwZonH5gAs-8FvQOZzS2MWrSC60tCN4D7v4O-f3ckhcigTuZ3WX5-FFeCxuJm7WlpznHdlGDSDEND8Fhgc0T8FN5nGkIJewdU5EYUZk-bojJXyzElQEi78PG8pGsOvDXr5aD1He6_xjRJN1lhgZnHM2G-RWccPWdQG516LHXPvKLkamyRdlyoPewqIxrHMUJlyIRYMzu8z7qJfxnvyA9K6JYLUUMS1LP8OG5a3rn4MLLQL09ONTv4PwfIjwR0jJdwjIoWs0MpFDkgn8fRBrONdfBSlx-8oEgFEbR4u05oCGCxuSE1hMarWLpEyMzd30yL0L6Or7jhSrA4jepnfKPJhdnPZf0v6Bba-5BjrdFCy6xhBzlwAoIOgaFdtk6hXwk5FG4wXKsNMDTXpQTp1Ry_FALQgXnl5gTluFxnLKP4uIBH60mu2NY5yuMR059PNVzux06fo0J_UnUAU_xli_-6Fwb3afec4eZg2yExs7N6ax8c2MsPOJZr8el06xBjdi_YKbPiIPnAIPI7LNbWhxpmEa-7PqC3r_hICroEBAreQ6Al3jlWBFUyG444cwMt3X82sQkQMSqg5ixx_UtatMcoODG1LrsfWJYA7rtl90zzUo1bPoYsC74Yz-Z-T_gaSQrRDZ2BugBANyMcrD2OPUlnFbpUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
در هفته چهارم بوندسلیگا، دورتمند با یک گل مقابل اشتوتگارت برنده شد و به صدر بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106896" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106895">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gheOMi9XghpkbWQjKmEYjNDBD5tTIFpu0qRjETk9kzpn7iwBFtyw_kXTaDq9zF9rK49OvtubZUDabXA9ZlIZuC02fGfXj6DzujfdW3ykigURTSpFGvxL5L82u0iaNKxTwW2D8TmzFgrIumrq0HXFWXZm869-eGtVHPEsaHi0l0BSDH0rsj1XiQhehTY1LTc8tLubt8Vm1kVEKjZFK-nUryEo8I69_CoiywAFn1eJaOntdSwrZjficImw52jUaCMXPSNY0flYhClvgpYYFmbaWplUQEomN6g3zpns3nyU2kc99q5T4AkXSAu9gk8b5Bx9_HXvAlirY-s8pOSOzYxhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست اتلتیکومادرید مقابل رئال‌مادرید با حضور خولیان آلوارز و غیبت سورلوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106895" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106894">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
نبرد اینتر و رم با تساوی دو بر دو خاتمه یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106894" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106893">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106893" target="_blank">📅 21:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106892">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otG_JQIKR0z3YzyhuHRZoiuVszbKDzMao5ieRBtiGJnATxT7A2niKbkg2YNnmLQa5-jQZbpyia1y-4L8HRCKCr72Yv4UeAc5AllnHblmEJyd-Y3hH0ZiPZ2i652NJI2gxHWdHRMwX5j4Y73SMwH2zPHmrOjPab_q_sMaCq9EzGql7fnOsqOdeofHKduYJX0y39L5DTGw2uXXg2S6-bNpHbO7Cjezd0jerch_zLK3zc_IiTCof8536SpDrgDMc3EhM-pgEN6kc7TrOhUXVZGdCGVkx62FnOpAfutRnvjmPfi8nbtToIFkbsTu_A6023wXOngm8bSBkZOC5Jn_0AMdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
شماتیک ترکیب بارسلونا مقابل سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106892" target="_blank">📅 21:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106891">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d419048b91.mp4?token=du-mIYskChyWehxF9-mU1OfraLzcITw5MElDHu8QZXttJFhwmFHXmbXCXPlm76USrgQraSUULjzbHG0-FeKi2TH3KGQ87Y7LFSTazMGMOXZ_He8t-EL8HmSv6rjyJ_JopV1ZoBEQrOG1SibsMe6-oLCXbXXkEBjHnndAhdipA7IO0eF74GCWAIzdcm3-MHU4P-JgbHbsh-nlvjlWCbsVofp-Qzty1M0xQ4UJeyC7DcUmVDZxUVAd2jj1Vy7FaWpUvA21LvhfwtzRyBjrC37hqlHD0by-Cz8KYbIStyVjI20P9u9vtqs36fW1lrmtUboJKZDr02ZKl3XVXmp-rcrkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d419048b91.mp4?token=du-mIYskChyWehxF9-mU1OfraLzcITw5MElDHu8QZXttJFhwmFHXmbXCXPlm76USrgQraSUULjzbHG0-FeKi2TH3KGQ87Y7LFSTazMGMOXZ_He8t-EL8HmSv6rjyJ_JopV1ZoBEQrOG1SibsMe6-oLCXbXXkEBjHnndAhdipA7IO0eF74GCWAIzdcm3-MHU4P-JgbHbsh-nlvjlWCbsVofp-Qzty1M0xQ4UJeyC7DcUmVDZxUVAd2jj1Vy7FaWpUvA21LvhfwtzRyBjrC37hqlHD0by-Cz8KYbIStyVjI20P9u9vtqs36fW1lrmtUboJKZDr02ZKl3XVXmp-rcrkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
گلزنی محمد صلاح مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106891" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106890">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WZ4XmxY3NopF8HYEFociujC2H9zj-27uD-ZJkqdyVMzEvjFKBEkx_XjyPFtzdeDngdom8WsD6YEbmJE3j3jxFvVglRI13rwtoh7gNTR6h9bTCZsoSUPihsNAyjuR6CPGyDdaBTqzUD0emG4ODOrqpc8MyLk-gf5J9OPthycDy7Ydgd06hmfNXZRpvbVEJCX7h11hCcgM1-FDWTYKfaAjQMW2A4Q4lVq6e_JU3bb_MJBH4HaAizMZbWAD30w0Mq8aOuBNNhHca9gbWMrPOHvdnhQc7Fgw9eIOTszHXjac_b93aw1yzjx1SbAzvRNvu8lzT07DAd599NQGnPYHwyNnSFZfnMbbgsKhW3QgNFjmoVFcQebvfV2kr0ArGi2YHFcee__JJPXwDsg7nCZdyrgvHWf5C4-m6zRTMWMXAtOWYkmKzauTbdy4tTb5D_bShg6nx2RJ4kxe5LJCeUdXeO4foL04flYak-yLkBTGULCrFFkuPYibdecRyKsLZFCALEu70OigFLkYxrsxsg81BZzq2W_gIce6YqIShSc8B9KlLrmGM44R97aWc8Vj95Mj9kklU2mRs6OqFXHO4VP2PFI7PUUdRzi0GX9OU5rZWP01R4EIjL7oNn06A5-Bki2KVikPTsrxo5r8H_dbaF12ERBeteIMb4UmzhEqvpoIrW_tWp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WZ4XmxY3NopF8HYEFociujC2H9zj-27uD-ZJkqdyVMzEvjFKBEkx_XjyPFtzdeDngdom8WsD6YEbmJE3j3jxFvVglRI13rwtoh7gNTR6h9bTCZsoSUPihsNAyjuR6CPGyDdaBTqzUD0emG4ODOrqpc8MyLk-gf5J9OPthycDy7Ydgd06hmfNXZRpvbVEJCX7h11hCcgM1-FDWTYKfaAjQMW2A4Q4lVq6e_JU3bb_MJBH4HaAizMZbWAD30w0Mq8aOuBNNhHca9gbWMrPOHvdnhQc7Fgw9eIOTszHXjac_b93aw1yzjx1SbAzvRNvu8lzT07DAd599NQGnPYHwyNnSFZfnMbbgsKhW3QgNFjmoVFcQebvfV2kr0ArGi2YHFcee__JJPXwDsg7nCZdyrgvHWf5C4-m6zRTMWMXAtOWYkmKzauTbdy4tTb5D_bShg6nx2RJ4kxe5LJCeUdXeO4foL04flYak-yLkBTGULCrFFkuPYibdecRyKsLZFCALEu70OigFLkYxrsxsg81BZzq2W_gIce6YqIShSc8B9KlLrmGM44R97aWc8Vj95Mj9kklU2mRs6OqFXHO4VP2PFI7PUUdRzi0GX9OU5rZWP01R4EIjL7oNn06A5-Bki2KVikPTsrxo5r8H_dbaF12ERBeteIMb4UmzhEqvpoIrW_tWp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول اینتر به رم توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106890" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106889">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/102cd70646.mp4?token=UFNK658DMZEnI3pe8UFKlIhguPIpiCeJNqVDKemE1jk9jvNaYx6Eln4tIc9XaGaINWODczuUHjTPzsilCsNfnSAOQZ3TBJ9Iz7m97XQaR4ofBFMBBG2sVoojCu-CnCsONeiXPCRPHC3bKYa0YrlQ2J_2z7mKrxhl85ii9zb6PxGI9njU5nwaWtDOkGizc0WXHPi7kat2-ctRpfVF5vk2dby03PHtEPVnt4MCn1zLvfauqW-2CAQi84TaBMmNRrIQcgStjGSeNx6YVBHbY_OpKI66fW4KODPZZdY7-_IWysnh4T8w_duy0LMuNNt1XGLnQwjt-7esnBcXDCYYqQD7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/102cd70646.mp4?token=UFNK658DMZEnI3pe8UFKlIhguPIpiCeJNqVDKemE1jk9jvNaYx6Eln4tIc9XaGaINWODczuUHjTPzsilCsNfnSAOQZ3TBJ9Iz7m97XQaR4ofBFMBBG2sVoojCu-CnCsONeiXPCRPHC3bKYa0YrlQ2J_2z7mKrxhl85ii9zb6PxGI9njU5nwaWtDOkGizc0WXHPi7kat2-ctRpfVF5vk2dby03PHtEPVnt4MCn1zLvfauqW-2CAQi84TaBMmNRrIQcgStjGSeNx6YVBHbY_OpKI66fW4KODPZZdY7-_IWysnh4T8w_duy0LMuNNt1XGLnQwjt-7esnBcXDCYYqQD7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106889" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=V7g-VbFPqjQ_TEqm0CBsmeK_cLGgm5M8VwSBYAr819dIhu7KPfUvcg7UNLV4xCKS7Q2nAiDwc36XGjfCuywatgTG7JRM_Bm3Nh-0xUGL7qc8zvZKQjoAMX71oEOf1m09n2hyUcAhdSgsEgH2jqqiQXxUtnZb9hXG5-qHAKoJDuri47ml1Keaem88iNQsZ9vMjecmEY2qcmGJqzj6IVN278KNvHxDBgK0rHwsEAlkTzJJp7-Gl119cxoSGYBjhxvk_ZPje07RehXJr5lVpmhP_-lDruotmi_3V5LuMBt55hRucH5fWJXw1Yf3uRaM_D9mrMGnt1wZr85nImglmOYNioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=V7g-VbFPqjQ_TEqm0CBsmeK_cLGgm5M8VwSBYAr819dIhu7KPfUvcg7UNLV4xCKS7Q2nAiDwc36XGjfCuywatgTG7JRM_Bm3Nh-0xUGL7qc8zvZKQjoAMX71oEOf1m09n2hyUcAhdSgsEgH2jqqiQXxUtnZb9hXG5-qHAKoJDuri47ml1Keaem88iNQsZ9vMjecmEY2qcmGJqzj6IVN278KNvHxDBgK0rHwsEAlkTzJJp7-Gl119cxoSGYBjhxvk_ZPje07RehXJr5lVpmhP_-lDruotmi_3V5LuMBt55hRucH5fWJXw1Yf3uRaM_D9mrMGnt1wZr85nImglmOYNioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
⭕️
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106888" target="_blank">📅 20:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=qwyBd4VVRzLNRvsMD9z48ll-UR4dZUKx1p4CafgvbeIjqGXBFatDQwxegDgK8uK8xwM8CQePtwcs9n1vLatt3ejbeyPwtn7dAJFSb4LDDFN3rWvGg_sRqvr5Pa7ktsGaVQ91CA0cYEVzAcZYJ-07jsyGyRWTBgSJiSoASi8jHA37eMr_QlDvR2C1AJKRj4jm67wEASOzN_xGG91iSR8xVqO07g3ajrBCxZ_nj7OnEd9m6gqSdcdIOH7AV73URf7rYIDJWKrCpYdPQCDFCmO2nqJ12JUyBc-S8vrX6ww1Xvxy7sjbGQc-__-tCmEeBEmpU92mLp6KKw6k68__Bu_BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=qwyBd4VVRzLNRvsMD9z48ll-UR4dZUKx1p4CafgvbeIjqGXBFatDQwxegDgK8uK8xwM8CQePtwcs9n1vLatt3ejbeyPwtn7dAJFSb4LDDFN3rWvGg_sRqvr5Pa7ktsGaVQ91CA0cYEVzAcZYJ-07jsyGyRWTBgSJiSoASi8jHA37eMr_QlDvR2C1AJKRj4jm67wEASOzN_xGG91iSR8xVqO07g3ajrBCxZ_nj7OnEd9m6gqSdcdIOH7AV73URf7rYIDJWKrCpYdPQCDFCmO2nqJ12JUyBc-S8vrX6ww1Xvxy7sjbGQc-__-tCmEeBEmpU92mLp6KKw6k68__Bu_BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
انتقاد کاویانپور پیشکسوت پرسپولیس از کامنت‌ پرسپولیسی‌ها در پیج السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106887" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzLSCkUPUOCvzQuI1J5zAvKAOSzBr5PduBJEQ4v_ACmMCwHRrYrW9k_ZYq9860QRIVvu-YaimdYVpnafZtdFtWi18N3KiXJQalVJBLlZDKZv0nVsgIQhZ0sWfYhDoA-6FhGA5ke-jMgEfvqPVu_kBGbc0pzTFO_sMXXkriEfH8BoKXGlCPffUEqEQ679yUA4pEZu6dTBpQBdCJW8T37PZtc5wRscvysHD0XO1rnMvB-NbdAXH85o3PHGkNHlo_gvdTqVtulFIe8iRUSQB8Qs9SYKEBXf5L4o3RerS-eilS03vsryqYQP5ieKQcQXdO2hT2_FoVrDqVpkaxz5bpfkSGXI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzLSCkUPUOCvzQuI1J5zAvKAOSzBr5PduBJEQ4v_ACmMCwHRrYrW9k_ZYq9860QRIVvu-YaimdYVpnafZtdFtWi18N3KiXJQalVJBLlZDKZv0nVsgIQhZ0sWfYhDoA-6FhGA5ke-jMgEfvqPVu_kBGbc0pzTFO_sMXXkriEfH8BoKXGlCPffUEqEQ679yUA4pEZu6dTBpQBdCJW8T37PZtc5wRscvysHD0XO1rnMvB-NbdAXH85o3PHGkNHlo_gvdTqVtulFIe8iRUSQB8Qs9SYKEBXf5L4o3RerS-eilS03vsryqYQP5ieKQcQXdO2hT2_FoVrDqVpkaxz5bpfkSGXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل‌اول آاس‌رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106886" target="_blank">📅 19:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947613cda4.mp4?token=gxKdZq1BF2J0U6l7j2MJzj2soGp06snFlxE_PEGSucffrhHX9uOe2CuMM6d5JHTfzuAt4fHZsIpcYZnq3pO7WOQ0Rtwkd11neU9BjNLfCymccVQCAJQIHHFNz9ntvbfenSXTSXZ4YThgNlmdwKSWmEObU1KSP3Rv1xPnhs3aQfsUVyxVpYEaZv5MYI5y1Fy4F3bGjuHjH_bZHsGNY-czTPNE0GlCJAXXDFgElsHLcyodj53nJmhkABC9-00C-ETddrkF0reWyF8LTfkrx_Mh3e9Hvd8LcoyvWJzHifDmwJZwyYiVklI0NiIo8RXlnyXqKmzo5rcYd6dFFH47iVHT5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947613cda4.mp4?token=gxKdZq1BF2J0U6l7j2MJzj2soGp06snFlxE_PEGSucffrhHX9uOe2CuMM6d5JHTfzuAt4fHZsIpcYZnq3pO7WOQ0Rtwkd11neU9BjNLfCymccVQCAJQIHHFNz9ntvbfenSXTSXZ4YThgNlmdwKSWmEObU1KSP3Rv1xPnhs3aQfsUVyxVpYEaZv5MYI5y1Fy4F3bGjuHjH_bZHsGNY-czTPNE0GlCJAXXDFgElsHLcyodj53nJmhkABC9-00C-ETddrkF0reWyF8LTfkrx_Mh3e9Hvd8LcoyvWJzHifDmwJZwyYiVklI0NiIo8RXlnyXqKmzo5rcYd6dFFH47iVHT5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خواجوی گلر پرسپولیس: الگویم نویر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106885" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DgIvbhrLafWsHGnxq2tqK6gKQBlmMPW_i05AjIAIZ781KkKp8hw2pnZXy1llT7rPjMTw7JohdQouQI4NNQ4oHtYUBPFUYrk-lDlEPuTzURSF3dC0NMKpJB7oWhlCN1AwfYDmVK6FNBZuVTSe3HTNzUadv-6FExE4seKsOlu-HB9nseGYHUSVdYp7uA-Q7RW2xljcdIEEOiUFiFGws0Kfd-4uO-_DqfxeL0wkeqhl4uhEyETphITtvL5wHIG7wTpMahcYiUlA6F8ZTusJ-6a6wwc06T4d_dYTTYDoFdLC2dciPvQB_yZ3I8QceQrgvMrqu7wXV3ZoKhYNzN14fyAxWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DgIvbhrLafWsHGnxq2tqK6gKQBlmMPW_i05AjIAIZ781KkKp8hw2pnZXy1llT7rPjMTw7JohdQouQI4NNQ4oHtYUBPFUYrk-lDlEPuTzURSF3dC0NMKpJB7oWhlCN1AwfYDmVK6FNBZuVTSe3HTNzUadv-6FExE4seKsOlu-HB9nseGYHUSVdYp7uA-Q7RW2xljcdIEEOiUFiFGws0Kfd-4uO-_DqfxeL0wkeqhl4uhEyETphITtvL5wHIG7wTpMahcYiUlA6F8ZTusJ-6a6wwc06T4d_dYTTYDoFdLC2dciPvQB_yZ3I8QceQrgvMrqu7wXV3ZoKhYNzN14fyAxWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جنجالی یاشار سلطانی خبرنگار، درباره چرایی برهم خوردن توافق پایان جنگ از سوی نیروهای سپاه و جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106884" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ernpZntuzOA3X4jMjo03t-faV5YcnRh5dQ22Udx7F49YkcS9vKFaFm10QBqitRnVgeXBK9JJaI36swU8FQgL4vR0oPz6iexl9ovxUySrHQvYa5_r2V6E-EYn4jiD0Mw6_o5WcF2FI4wGawqx_BIcc3CYAVOfvWw91Z3S6cXcrn8W15YV1bsy3OR0EaLp001C38UnZlsTIjoN1PgYLhIitRjC8uXWEzaGfzy2gF23WPKySWQQW19vkK_XAYRUQXYdCtaWiKy3jsIOeajwqKqgCjtZ-M3yMsXI4SUvQS8nptbUyeXEw9ZZ84HCj-ncK1KolGtaTplWE_XNGMKfaLuHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار جدید کاربران برای تأمین نقدینگی به جای فروش طلا
🔹
با روند صعودی قیمت طلا، فروش دارایی برای رفع نیازهای کوتاه‌مدت نقدی توجیه اقتصادی خود را از دست داده است و حفظ طلا و استفاده از آن به عنوان وثیقه راهکار جایگزین بازار است.
🔹
وال‌گلد و بانک کارآفرین امکان دریافت وام تا سقف ۳۰۰ میلیون تومان را با پشتوانه‌ی طلای کاربران فراهم کرده‌اند. این تسهیلات کاملاً آنلاین، بدون ضامن و بدون چک از طریق اپلیکیشن وال‌گلد ارائه می‌شود.
برای دیدن شرایط وام کلیک کنید
برای دیدن شرایط وام کلیک کنید</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106883" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106882" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA29D2CZK7CUnwbHG33gmjvQIvfKixf7jBGgHxGGhN9Emg6uUepO9RnHARwYHzjrQWHYu-hY9OJkH1_Pnh6GzXcyjdk7PAYucRV6O3dUt2sWLuvWuxyRFsY_t05YM0loL0CoR-mukeAO36tcZ2Ra35jcECjFZmg0WO34dNiNn10Bh7JJTXjFMAE8hXE5Lpmt1-scbO5eZifE6utS_hoWc7RLKtphg8H-HOJUntz3A0_H0MGOj91TK9qL3E99FpMaMhM0_DR5yeOo8qNeHmiENd0jf9nPgiEoq_wD0YxKTozJq-DLm8scBFhGIVSYu2r9fTeVBtTHeTY1Bm_U3MxcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اینتر مقابل رم؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106881" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106880">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106880" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلگلگلگگلل آرسنال دومییییی خورد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106879" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3613208345.mp4?token=hdNXK5QNlypi028aJaGDDTY25RN-KrPStCOHbijdUDEVCclYVDr9pQEPzq7EtwH6KqEYoixPhbXz-yIjiCMTncT18LGvRT9lbRyGR4tQLFmHaXeIiYiugIpi4eEm6-gh4eZNGC6p6clc2y8hzpwtxUlH6x5JwS-vy2gONl9sSznDw2lT1Yoc6UJHv6FyZtIjwi06BC_RMx5chQi9HDZD9cPMT1ZtgBe8hFlr9_ce8op8exG8zYKyuej490JGplqCXCeaytx3MGswlUvidnUtmhz9W_YSsVbvzH8BE30oiL5f_JO6kwfum7ts9LpkapMAPkMlpIS8D5R4eA9phc4zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3613208345.mp4?token=hdNXK5QNlypi028aJaGDDTY25RN-KrPStCOHbijdUDEVCclYVDr9pQEPzq7EtwH6KqEYoixPhbXz-yIjiCMTncT18LGvRT9lbRyGR4tQLFmHaXeIiYiugIpi4eEm6-gh4eZNGC6p6clc2y8hzpwtxUlH6x5JwS-vy2gONl9sSznDw2lT1Yoc6UJHv6FyZtIjwi06BC_RMx5chQi9HDZD9cPMT1ZtgBe8hFlr9_ce8op8exG8zYKyuej490JGplqCXCeaytx3MGswlUvidnUtmhz9W_YSsVbvzH8BE30oiL5f_JO6kwfum7ts9LpkapMAPkMlpIS8D5R4eA9phc4zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل‌اول برایتون مقابل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106877" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ-vInd77-nmJGDM44vL5SasSR3_6W_6JHcF2UarmUNBV-9R6FAiGxjFiDRLmyahJtX_oZuRHZS5uLcnZdCrH4Sad1rGWukK3BJJ1DQwwueZm28QvFrLc23LmD2cRrkVJ18qDL6o8wWEow1xpT77C-Qd1Y2-o60ywM4vZBXpreTJY9K6KwA4nLj78RuZSwR3jB1Ej1CerqVoEff7TAmNYi8Wuvvp7vyklHsg5_ONx7WiEiVZoKy7fd0WXG5huPbfQgQMoL7hx8WecYjeMj6tOY_GONnL6G6qyQL_IWtmzgFP6iQxKHza4ySWHqPefcDKbpk9KclMmlIBIlHSqq_WKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106876" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTNbwHE135VFlN-Dzuc4roA6qw7eM0Jh6yTpRbbwHxpYvzikhZCNCqCehdgIIq3faIP5oSjrr1cpymRPi0QEsW2uwruzQOQ-nPyzOIA9fnrFddC-jrrJp1zPCZIOjSLEGlRfAX44JRV07NAnMYcQI2Cc6_ZSgH2yVd1x4LeRt_rJmeCuMZ_TNmu6dqgmsnSJ0n3ErbxkG7vRl-FCpyDOj7hKRHdZbjMOswqOXmxA6hyRBaQjlwHXhIH2bCfZ1sfxbAGYpiF5cFRwfN3A-jiZpwqZtdKmWfd2obl6EUp1OGGihwUt6JzaP86cJsqxZbUp8AdsyzwJ4pXEcD4m9C2h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106875" target="_blank">📅 17:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=EBLmgFXnFrajBtEAUlUvnPDD-Kd579SkGY6U4icN608tc4dHa8kkgHHHyKkVg6_jKVCQdriKuz_raC4aGvgcgJU7Z_BPt_bx8A3nsLXzMCQPKdAGHZ36FgihX1cBQ8mAeI8byAQnijirtH8LfHitgYTaUCtPAfxhj07LeUqFrdeBiEkU7yi10ewiiAFmSykSDrZi77ReRKfyePRThOmequVByUN50F43YDVhlfK64GljKxC2z9kdlYlHei1W8tk6s5Eggumj87IbSRoo-ghDcOiKzXtzK5M1-yeiubJh8YaTchKJBJiJICHsQYtJ2FexCEgxQw19-6Gch-0piVWImE1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=EBLmgFXnFrajBtEAUlUvnPDD-Kd579SkGY6U4icN608tc4dHa8kkgHHHyKkVg6_jKVCQdriKuz_raC4aGvgcgJU7Z_BPt_bx8A3nsLXzMCQPKdAGHZ36FgihX1cBQ8mAeI8byAQnijirtH8LfHitgYTaUCtPAfxhj07LeUqFrdeBiEkU7yi10ewiiAFmSykSDrZi77ReRKfyePRThOmequVByUN50F43YDVhlfK64GljKxC2z9kdlYlHei1W8tk6s5Eggumj87IbSRoo-ghDcOiKzXtzK5M1-yeiubJh8YaTchKJBJiJICHsQYtJ2FexCEgxQw19-6Gch-0piVWImE1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
‼️
🎙
ماجرای دست رد مهدوی کيا به قرارداد ۲‌.۵ میلیون دلاری!
🔻
مهدی مهدوی‌کیا: مدیر باشگاه داریان چین بعد از دوگل من به این تیم پیشنهاد قرارداد ۱.۵ میلیون دلاری را مطرح کرد اما بعد از جام جهانی به دلیل عملکرد، خوبم آقای عابدینی رقم رو به ۲.۵ میلیون دلار افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106874" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106873" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106873" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUolS0Mv22Sz64Kdi34UwZetWcmneG_ycamxq0V2UH1aq3Gn8gwM1t3SRvzn4S4kFYrhspCbadF7HHxcA82IWhJ8zVVXp4_cUlNJ-bZ2z-RAuMT_5mz5_TgxE1LRljyClhI-h8OQ-MvHSyr2u5Nsyz-15hddfs3LlVdbCaPN1wKuPWJ61ianh8lnmDqkhfD-ZPt7IWP5Q_1jZAnHPWSeMV50PzE4tv0OEpR849wIAmvNVkueotmMRpp_KVzj-2jkkw_M9hXTuZTV_OGf40kz2m2-lLrmjnonhKiOXMvKbCvIt4hbhoU8r7-4JrFzVr0Z5CmAZTp7bCdDvfhJydcWgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106872" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ETsltDtERTkeJz5Kh0ChpZvOuOHM7qYqWvkCT2bAjN544SuvbaHZGdCEMmOCPn4AFyh8R7mHfneujFpB7RgeSyBGRJv5-KDv8nKCBoEG2hg-mcXQjcf9ZbjuE0wrWvhcIkaQt6MpVEAQpQMUz_vbuv0IY-3walNsqz11zk4jR_lxFQZh882nRP189s_VysHj4kkMcrxOD9Y6BbpGJZPOplfiE31ciFWjLCcSK8IpHx0BbcQaKdZtRPB-mf6o_LMKinKuRpPAUN7GxDD7XuBzmDMx70zW3HMm3hXLGTUz6CBx4m2mPHdbR1hHK6qyqMfpz2IQHr-GebmZmOicQNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
ژوزه مورینیو در پاسخ به اینکه آیا از شرایط بارسلونا نگرانه :
🔻
از نظر تاریخی و فرهنگی، رئال مادرید قابل مقایسه با هیچ تیمی نیست؛ بنابراین من هم خودم را با هیچ تیمی مقایسه نمی‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106871" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB1NtDKvXYRsos5ZnCZLM1xpj57_DNUEaKgwqQvjiHfYrLEKTdmuj5p2bqI2t722zVuCAkVHzqVkNrlUmUpC1LoMRHB6Psd26FGJA71R8i1YRyilqqiDeVVAWU8GhXrQCWHu20TwmTETHUJDe_nly0ebTZkkKCar8-ywOSTw6tQmzcuOlLGng1KEKK8zbb-VvpimLQX4BDqT6Dzt7nnKyatYQ-N-fGzAWpxlXXvuxC1bTSfELB4FuQxt6BZWQkn-D-HzS88df7of0cceM9KZVdbdKGfsZB77jb8_lXTSH1kKt_bTLBx3-uf69mqgusobu5PxPaRMqoT_blGZiGmOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❌
رسمی؛ مجتبی حسینی با توافقی دوجانبه از نساجی جدا شد
📊
2 پیروزی - 2 تساوی و 3 شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106870" target="_blank">📅 17:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf935413.mp4?token=qzGfjOUAkFfcZBsMOR8AGbPZZe69KdfLbCylrexsbcikrXd85oT4fCNg5CeDmJ7Pp_VfpN1YIMYYEF2Z5XpHhRhskz0YLHsRwAu87PJpsLzhkweTeK0Jb2ktW6r5wXMC99M5fDPYw7ftpg8iSm_rHuPsxIabyiYdtjeYKiVhl1TQXvr6PQBnFzYdUieF_2jYQHQt59pMPCO9cmCB5V0Bka3rNE0CwEGZvs0Oq8OTcgct2fqXVSnRWlCy_0PO1rQ4KCP-AqLtH5cSauSL-8Vgw3foTMtCGYxxQ2CcyuGCCHYjyO7x7nTvjjE-Pjoo6dNiQtJon9gksUpFbSD7h6Rh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf935413.mp4?token=qzGfjOUAkFfcZBsMOR8AGbPZZe69KdfLbCylrexsbcikrXd85oT4fCNg5CeDmJ7Pp_VfpN1YIMYYEF2Z5XpHhRhskz0YLHsRwAu87PJpsLzhkweTeK0Jb2ktW6r5wXMC99M5fDPYw7ftpg8iSm_rHuPsxIabyiYdtjeYKiVhl1TQXvr6PQBnFzYdUieF_2jYQHQt59pMPCO9cmCB5V0Bka3rNE0CwEGZvs0Oq8OTcgct2fqXVSnRWlCy_0PO1rQ4KCP-AqLtH5cSauSL-8Vgw3foTMtCGYxxQ2CcyuGCCHYjyO7x7nTvjjE-Pjoo6dNiQtJon9gksUpFbSD7h6Rh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
سکانس‌جالب از قسمت جدید مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106869" target="_blank">📅 16:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=fXL2n9b1vkc4yaqIExJxSPPghdFuu41gSG2ltISVSpEtaLpqF5fB2cO4MudlDqAO9rFHbBmxv6pryhhHx6NF_OsS4zPtsbylepxofLbMANktKDTIRgkCNgW8TDfBnEQSzi_7m1zW5YYT2fM1S8Wao7bfVujRGwmKVjlHW7TVFTnRl1nfxl_fZNW4YDe-T1pAD6GTjBUxYMqbXjIcV2njCmYygJJbSeiLfPyS9hnhACJTiHTaMqeAVZJ3i5WtHTYyQh_IbQv5e7UpGx1hXv4BZ4gvboRMdihHWlZqUqemsPtnE-RuplVvJeDrRKD3sn380OO5LuIRk-wwbmHIeh2Rdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=fXL2n9b1vkc4yaqIExJxSPPghdFuu41gSG2ltISVSpEtaLpqF5fB2cO4MudlDqAO9rFHbBmxv6pryhhHx6NF_OsS4zPtsbylepxofLbMANktKDTIRgkCNgW8TDfBnEQSzi_7m1zW5YYT2fM1S8Wao7bfVujRGwmKVjlHW7TVFTnRl1nfxl_fZNW4YDe-T1pAD6GTjBUxYMqbXjIcV2njCmYygJJbSeiLfPyS9hnhACJTiHTaMqeAVZJ3i5WtHTYyQh_IbQv5e7UpGx1hXv4BZ4gvboRMdihHWlZqUqemsPtnE-RuplVvJeDrRKD3sn380OO5LuIRk-wwbmHIeh2Rdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ژرژ ژسوس سرمربی تیم‌ملی پرتغال:
🔻
کریستیانو هم مثل بقیه بازیکناست؛ اگه عملکردش خوب باشه بازی می‌کنه و اگه خوب نباشه، بازی نمی‌کنه. آیا جایگاه ویژه‌ای داره؟ بله، دوران حرفه‌ای متفاوتی داشته و پنج توپ طلا برده، اما آیا این چیزها روی تصمیمات من تأثیر می‌ذاره؟ نه، اصلاً.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106868" target="_blank">📅 16:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=lwH4eCeO6a1w_55AB88xtwPwa7PJ3hDJFShQIT7iCpwTvZC6lUoxfj25WmJQ2MEqt3ZnTOe8f1STrz3K9aK8LpNhad70P-_9pIg5AGMb_PzJjYlH0Dzo8ZmnwoeuQbISgtc3imPUoJocBjA4FhUIsiwFEQCUJBFPE4qwIiyUjiu-Bw8SubxPSHrvWPce5VR2oA8nOaphCd_j3v77pwlMd2zvLHZpzMpYlkvS1PjMlb7_sUrQX-GTlEh7Jy27zUE-1Dm6UpYOr8WL3ynsAZA72y_F9q553Q1xYTU8GzzjZm56MtpFATe0wl_-IZJ_YNVAXtVeKpeMnItV189NPl0tlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=lwH4eCeO6a1w_55AB88xtwPwa7PJ3hDJFShQIT7iCpwTvZC6lUoxfj25WmJQ2MEqt3ZnTOe8f1STrz3K9aK8LpNhad70P-_9pIg5AGMb_PzJjYlH0Dzo8ZmnwoeuQbISgtc3imPUoJocBjA4FhUIsiwFEQCUJBFPE4qwIiyUjiu-Bw8SubxPSHrvWPce5VR2oA8nOaphCd_j3v77pwlMd2zvLHZpzMpYlkvS1PjMlb7_sUrQX-GTlEh7Jy27zUE-1Dm6UpYOr8WL3ynsAZA72y_F9q553Q1xYTU8GzzjZm56MtpFATe0wl_-IZJ_YNVAXtVeKpeMnItV189NPl0tlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
جمله قصار فنونی‌زاده خطاب به امید عالیشاه: با آدم بی‌ادب باید بی‌ادب رفتار کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106867" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106866">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvyPpW2abqWSIBLBSxmLNecQrApHhCrngneQHZSQSyF6QuYauDax4BZ9Uao5he28JJDjd9lluL5WLASlNP00LQb0-XJk5QsMiPNITxybmmKBtddt6O7bMHxv7k1FF6oZKeO7ihhy6zDIWs71TEV4c_4XHQL_0ZJ2RlQyEKl0pJBV8k0Zq5rfrwVO345XG5sLsBXl0eFqeLz60TNh-RDb_WUlKKrpOkubbqZIdtCWNJk6g0jZldioc_QuvqxowxBw1um9jZ7MLw-beEv1BGOxTHYwUrv7-rJ9nXb5tClO-Cug8R_DaAFrJiT9LE6BUlCWV7r21BytJ_uBNODbBtp7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد ضعیف املیانو مارتینز از زمان حضور در باشگاه چلسی:
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برنتفورد دریافت 3گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل هال‌سیتی دریافت 2گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل آرسنال دریافت 2گل
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برایتون دریافت 2گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106866" target="_blank">📅 15:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHPHGaeWRNgUSWAyTgWVILn1osuqoC-0keDsvFa3sqnecLluOi28vva9TXw2DP1UZr_DuPgZq-PftdrHy5YUPJKoLZ4bm0BRX6gy1CJK5UL2P2mtFfvfW6-88x0r_WWshMsqmsqEtIzMr8OcmNgd_jsU5JGfsR5o_PdcIi0JFy8SoGlEzlascIiq41MRfOxRvARJSErv9_AvhWJLsMMA_YZWlJOnr5r21hhpSUypcPvLo5XUaOpznTDqISS4ktKoago5NB2i51uWg1FsYDjs-TYgpitAazUnL0vz465mYeAqkT8aUZbD5t-bDWgfRKAk67POqanS64gSh2bCre-0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
لیست‌تیم‌ملی آلبانی برای فیفادی بدون حضور یاسر‌آسانی ستاره تیم‌فوتبال استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106865" target="_blank">📅 15:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
سوال مهم از هانی رامبد؛ برای رشد پایین تنه حتما باید اسکات بزنیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106864" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
صحنه دلخراش مصدومیت یک‌بازیکن در هندوراس که پای بازیکن در آستانه قطع شدن رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106863" target="_blank">📅 14:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔥
👍
🇩🇪
شب فوق‌العاده اولیسه در برابر یونیون برلین با سه گل و یک پاس گل و هدیه‌ای از طرف نیمار؛ بایرن مونیخ ۷ - ۰ یونیون برلین⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106862" target="_blank">📅 14:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjKRgm8ElLqQnTW97dI0HMDh1-RuOZFykByxBqvz7m_wptvK4F9pmLLwrqdKniLfozisTBJF_FDIHktShnGj42Vz2EwaYT47IiHe8SItLOSFz-ws6896aUfsowahzwvkQRJ0YtAMGXoRWSVb5IaFwwKkCTCJRDAhzKfEZRQSLej_4nbu6FYqr_zGbzNRMskwGTDdb4jD0RVgbUpgtL_WFP_Jw78IhepseuqJxcENGhMO0kje_mRqGgKl6m9vR2Wxs7Egni_E595JxXJZFrlgSrceFzOC67wZ51RCwyEa7UqerleElxKmAT6KHbGWXu2YxKruOLGkbmIqL1K_GESK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌پنجم پریمیرلیگ انگلیس: ترکیب تاتنهام مقابل استون‌ویلا؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106861" target="_blank">📅 13:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=B1OhwRViktOvL2ELXUjoKzviVkLLjt7ootZv1-eZYYMed0G_0HVW8GTVC9LR3SLwnH2Qa5FnzCSX2brcL5325My4bxQRqW-yVuGwmwUsHIts1sCJNfvUJenk3DjRhq0kRTgTKBIjH8ngJhqRxzfVXIOr54IB3lLbfK28wp-clC8QoJD9H6povsxy77TSJ9gHI42FSMC-BzMVlkcnM1cWv40m3-3poF1-6TZ0kqgw6sg1EEBVMKmK_RaxkrrmrBa4TOK2tVpiO7MRBiZ4_voXcSSU1OobKQIsO510FrwbUVn1zdQsAeEr_lXHl3p8P3ugljxlzrY0OqgxxGdwmR-U4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=B1OhwRViktOvL2ELXUjoKzviVkLLjt7ootZv1-eZYYMed0G_0HVW8GTVC9LR3SLwnH2Qa5FnzCSX2brcL5325My4bxQRqW-yVuGwmwUsHIts1sCJNfvUJenk3DjRhq0kRTgTKBIjH8ngJhqRxzfVXIOr54IB3lLbfK28wp-clC8QoJD9H6povsxy77TSJ9gHI42FSMC-BzMVlkcnM1cWv40m3-3poF1-6TZ0kqgw6sg1EEBVMKmK_RaxkrrmrBa4TOK2tVpiO7MRBiZ4_voXcSSU1OobKQIsO510FrwbUVn1zdQsAeEr_lXHl3p8P3ugljxlzrY0OqgxxGdwmR-U4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
▶️
ابوطالب حسینی با این ویدیو اعلام کرد که دیگه تو کار ساخت برنامه فان 360 عادل فردوسی‌پور نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106860" target="_blank">📅 13:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcBFikQrRxBSEl_gGNNrZ1r4KdcidUPyLkTLVaOZrA7hxVtOgJRWWcMy8wX8qLul_vFKu3TpE_dgORx9HPAgi4dFD5dGbAKuNINAV2iRexje9M7CtxBv-69suLH6LsxXLjyyG-pW4RObUX4r5CTuQKmBGuxmnjZbFdaBGAYVHKf4fdcW2_c5t5-2wHR4zVoDMWVtUapIg-82fVaMiDqSoti1IQqRXpZCeGIMROUNppxG8FiLdyM-0BfCTywUPX1rm06DyjnEHF0pOhWkidCh11vFtZF3DKIwJYYpwO3vYf6KzS-OnLN1aI50lnUUYANBv0s4t_DJHM4WQcrmRHqhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
رافینیا: بدون‌شک برنده توپ‌طلا باید یامال باشد. او آمار فوق‌العاده‌ای داشته و قهرمان جهان شده. مردم حاضرند برای تماشای فوتبال او هر رقمی را بپردازند و من یکی از آن مردم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106859" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106858">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGsTo4WVjrMMZsXK4rkbMWm5JzDKQsFVMccR7ADhYJGs6NsPPZzlHpPaBpCEVYbLeKOpOpJo18X3txLbZKmM4aGNikuWKL-jGXjZVJkPmod29zxQXjAeYCXX4p5dsodKcbFdonh9C4gDPJaMdj73seUEvP69GM76RQ8_pPxHKFGoCuh4ab_5xmrfO4gPHDMXuN0Ssp-UpeBLz_R-AyBlhQqKAgKTAo-9_UmuXFBvmVP8T47TcXCTJlxyhzrGsB2d6dvQmSl4DKVM5WhGcRZROgE-OI4JlaTLMkI8QWM95juEfdowcrny71zQsxtIP_6Q6ytd0HzTYtpbiihxgH13dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
رافینیا
: در ابتدای فصل یک‌پیشنهاد بزرگ از نظر مالی به دستم رسید که مقصد عربستان بود. این پیشنهاد می‌توانست آینده من و نسل‌های آینده خانواده‌ام را به کلی دگرگون کند اما بخاطر عشق و علاقه خودم به بارسلونا به سرعت با پیشنهاد مخالفت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106858" target="_blank">📅 13:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106857">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=nGc0e4i5ZPsSSyCkZ1gUxtdnaP5peRXzfGPLug4IUz1uABUcCTH7QIrDP8cLaIZBQEneVFeW413fB6lhTMSVrIt_6Yu5--GCPT1fCjMr-AgzZt4JKz8WK7skeYZfhrXGyoyxucS0qcD3kbss6SAxIXD3BwTytOK8i2JqPDWefQHxoTEHcvB9e5xptCXATmRxq4hHSbBsPnPBd2LngTQv2FfBTkYx2Ee6QxgLx8OokdtHe0bYhxBeyp5jVog0nSpsmABqCq0LQLV0Q-0hIuzV-aSl4a00wx38EQ_qrHIPmF-X-FVeKsbGn-V1unyxGXI4HcO3JPOMTJiuZKJ3NxZ7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=nGc0e4i5ZPsSSyCkZ1gUxtdnaP5peRXzfGPLug4IUz1uABUcCTH7QIrDP8cLaIZBQEneVFeW413fB6lhTMSVrIt_6Yu5--GCPT1fCjMr-AgzZt4JKz8WK7skeYZfhrXGyoyxucS0qcD3kbss6SAxIXD3BwTytOK8i2JqPDWefQHxoTEHcvB9e5xptCXATmRxq4hHSbBsPnPBd2LngTQv2FfBTkYx2Ee6QxgLx8OokdtHe0bYhxBeyp5jVog0nSpsmABqCq0LQLV0Q-0hIuzV-aSl4a00wx38EQ_qrHIPmF-X-FVeKsbGn-V1unyxGXI4HcO3JPOMTJiuZKJ3NxZ7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
رژه کاروان ایران در مراسم افتتاحیه بازی‌های آسیایی ناگویا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106857" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106856">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwuIOrJ3fAt9-V29t--YliEByIj0R8pgMJnvyCO3y_FmiIgje3UWG4heSPtDK9noZEDrvpyUC4jOHFID0LCklZqYqRjQPVEoOSa5sDgb3FY5Z_m52Q2u5rZUrpAVMpnXLNBh4Igw_a7yfHxp6XDmdzfzD1cDdqMVS0wAK3NznYYT70GfwddrtzLoDNW746ulUA9tjE3GDXSXnWK_nXRkrCQ6u8DXtcHvl8UnzLdNw5enws-NqoFBCzFEYjyDZyCFxQ-zegYjlyCXn90T1FQRXW_5KCvUsKaNciZHBbT6sPvOtCsTr4Ud_97WkWBJEz2bvzya3uZZOSNRGMW2K1bJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
نتایج مانوئل پلگرینی در تیم رئال بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106856" target="_blank">📅 12:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106855">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZgmG0BGB0z3SuZGN3B9X3CP6_XUiOHausyXA-L2bWQ_hXR7-09w2ezao-oGSkYbtBWzoLqNk-rS80hduD74hVw1tKZA-Hy3Cg3WU2h512tFzJCGKlZ_kPsNQR4-5Yj-7oQ35_iEovqXDp3DyJlzEFngVnOlH1Un_vz2Pm4pghkWAJ1k2qGjhFPRIArop-f9DTduS2M9fOl_pZbsqbi1pmEfIWxuXLgfeDriwYK-YbNfAYNxqNFBK1DjOhQqiLB7JIY9pJyDlqP6Kvr06M9lQGJn8ae98n0Oi8rY_NlZAORH0Ff8761AoOmKZtSwZj18kIHQMBBahWPLnK-k2t6riQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🏆
با برد استقلال مقابل السد جایگاه 5 ام ایران حفظ شد و سه سهمیه مستقیم باقی موند؛ نتایج مسابقات استقلال و تراکتور مقابل تیم های قطری تاثیر زیادی روی حفظ این جایگاه داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106855" target="_blank">📅 12:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106854">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvNsNrrfUFd_I_aAwf_sIvSgSPFvIiaq5qydf7HDzOiEVVDQ8hC7q8_Ox33yPE1J1vVWND8vP3B_-fpSp6SfBA1LREXgYGemN_gJYKPr9DTIPQu-yHXWPWTUG7W0FxbOBezyi7b0Wab5i5GugYKYV0LGFV-j4IH8OpZx9aq4uW2HAM1qzBEE8lOyrnThIA9vMH7E6mV7aoYyoau6kpZDJh2qtyJwH4R48CE6q-cG_OEMdxvnqdKOu8W08TTgMx7tsfqaK450it3g9sKRxjNbvD6lHCXgkwDRQJ-fZzeEINLVTWRSShdUwK74t9u4oTb6eH4ho6LepwA1tzpY_DTsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
لیست‌بارسلونا برای دیدار امشب با سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106854" target="_blank">📅 12:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106853">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMkCqHtAHIPAbFpW3soZEzjPFMF-DWKClawU-7r9XM96hQVe60qO3r09LZJX02i1ZjxV4KsQDte3AOGLNDdwxNMvnsMApWdH3rYe3zIBXezKA6OkkMZmY1FwfG9WsyK6lLlIttHIaWe-aRikjT5xTc9hSQOyoL6rNqbrDlr0npaELe-i68QMys3oIf1t9BrwoIsiiVVc8KTTv_lB-938UpYiY2x71zWmSQ8SrtFMwYXcOWRckQzHOEY5CUqqIyTUDK0ArNQuggOmkvZlRde2mc5tX0pAQD_Msjx-4VA-EeToWMZxtXxVEvRJpp2dY2BdfFL1_wjrI1Jv7fLoKXSNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106853" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106852">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106852" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106851">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMiJ0Zy9JHFQMX1hXKRhCQkno-pMzJZAjoDWgWgW7DQA8rN20AphC6bWY_YgZou8h2CwBBw0cM2uY7lTEQsbBeGO6pvMXiSyMvom4xuIELrgJuhV4O8ASg2FwqaHIjEKllDpr5VeLXc0YyUUHfLI2X-5nX_xFMdrCODlgjMJ7IXbC6M-fCm81Odp7hKebc-wqgQdghCGZ4Cbili50OnLxlJ2D8TzEKQnR3xbhdga2wb_B4evKKE2rEyEhibsskt6Vd-AsViRb4sYNoJCA3A99guK_0VFjUg5xItBXHe6w3Akm-9eD0B8lfzzgPalzN5OmtSLtRx7CvvAvV_7HGYhDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106851" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106850">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👍
▶️
🇪🇸
🇪🇸
در دیدار خونگی رئال بتیس برابر ختافه، ۱۱ نفر از مسن‌ترین و باسابقه‌ترین هوادارای رسمی باشگاه، بازیکنا رو موقع ورود به زمین همراهی کردن. این مراسم بخشی از برنامه‌های هفته افراد سالمند بنیاد رئال بتیس بود که با هدف قدردانی از هواداران سالخورده و یادآوری نقش اونها در خانواده بتیس برگزار شد.⁣
از اونجایی که بتیس توی بازه اصلی هفته افراد سالمند، یعنی ۷ تا ۱۳ مهر، بازی خونگی نداشت، باشگاه این مراسم رو زودتر و در دیدار برابر ختافه برگزار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106850" target="_blank">📅 11:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106849">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkCzHb0gOyw2x7lpdHAVVJ1yILxfldKyY0dL-dU96knta-3NXImx_kaM8N0hLQljInbFSVvsZE6Km30zdWh1fzRPl-Z74iVgP7bw8uw-U8ethwSkJz67me9SPAMc-eAapvdp1AR7EgZ2zbqJeMuHqLMCve8mu-1p49vBq8qozV4nhhk6W6nG3VqTCIQtcbZ4nUxpldTJckDbsnuK5VfT9bXFe9ug9oX0KnGvSEGKpMmlcnBvfthDdjUszMtfpyIQt7guikiRfoycd5Si9eyAU8wtj0iP8BsaGDCCG6yPpXsmQnocz1H4dm9WkrMqSjBK8BsPGa434tspKjEjuJfz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
😆
وضعیت سه‌فصل اخیر اندریک در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106849" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106848">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=AQ49WFMTHc6r-ILl0I2p3Pi4j7SBKsVTnOLhTuYoOFURrZ-b_pH3W3_6pKBIqInx36V_ujDFp6ogqLhen4GW9TSB7mLxXaOWwH4tlANGUsKu5GzcmOYsIMPtfREfjsRJjsJtakSfllIFKjulfzxstldnK-4k2IUrHesV8kLi1DnvokpZ5qqD91vFgEloitXsQ4sSHdt-Ql0azK2BEvQ_yPHfyyiKBT5h2rGbvRAp5aBbmFj-p5-fy7SXds40i_wP0kEWariZ9nVcYnSlF8ny8sreDAEIVToYRd__ipGIGvv7oUSvQqJWUR5hmGJtJzltgV6ttNTXinCfMVyJyo4Mww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=AQ49WFMTHc6r-ILl0I2p3Pi4j7SBKsVTnOLhTuYoOFURrZ-b_pH3W3_6pKBIqInx36V_ujDFp6ogqLhen4GW9TSB7mLxXaOWwH4tlANGUsKu5GzcmOYsIMPtfREfjsRJjsJtakSfllIFKjulfzxstldnK-4k2IUrHesV8kLi1DnvokpZ5qqD91vFgEloitXsQ4sSHdt-Ql0azK2BEvQ_yPHfyyiKBT5h2rGbvRAp5aBbmFj-p5-fy7SXds40i_wP0kEWariZ9nVcYnSlF8ny8sreDAEIVToYRd__ipGIGvv7oUSvQqJWUR5hmGJtJzltgV6ttNTXinCfMVyJyo4Mww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رئال‌بتیس که خیلی شیک‌ و بی سر و‌صدا خودش رو در جمع تیم‌های برتر لالیگا رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106848" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106847">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=WUHjkxpCjdLZGRrSUqrar7RPSwhi_Swfygujr47r_iLRI3c4qlQHWgnefitbDuP8xNB8r6y-n8l-7Tw6TDJZlDUWWeoLrMpeLo_Dn_n_oevbh6gjy8ABr1hjl2_VJcG9diAfktprtj_lhIddrNte0UFpeR2WF32Q3NKpk970xYtjhD270Too3IogmjqYfZ3QZ8s-BwnarNf-wqmUxeLb7VErO7xmb8PjaWjgWz_6KsWXWkk1k_Ic0REBvzPbdmWcf0oht3j-ed7JTkQWBE_DtBXOhrZNs6-1kuejKfKesX7d0d_Of_zvy4qdjrYheQ-4yh2F4P0VOhAHQBwAZT1-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=WUHjkxpCjdLZGRrSUqrar7RPSwhi_Swfygujr47r_iLRI3c4qlQHWgnefitbDuP8xNB8r6y-n8l-7Tw6TDJZlDUWWeoLrMpeLo_Dn_n_oevbh6gjy8ABr1hjl2_VJcG9diAfktprtj_lhIddrNte0UFpeR2WF32Q3NKpk970xYtjhD270Too3IogmjqYfZ3QZ8s-BwnarNf-wqmUxeLb7VErO7xmb8PjaWjgWz_6KsWXWkk1k_Ic0REBvzPbdmWcf0oht3j-ed7JTkQWBE_DtBXOhrZNs6-1kuejKfKesX7d0d_Of_zvy4qdjrYheQ-4yh2F4P0VOhAHQBwAZT1-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
استادیوم آرامکو عربستان که 2 سال پیش یه زمین بایر بود حالا تبدیل به ورزشگاه لوکسی شده و در مراحل پایانی واسه افتتاح هست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106847" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106846">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sa5OXiBphOoJTGYMyHMkLkVKutvoG52POIrwMen0g2hj4xyukhfNliseVH6p2yZ_gslL8KVC7C0is90MfHAOjug_tRVHIEp_YSUDAVmIJSgkV3oh5ZjbvZWJZYbsaQbCLgYyJ1pjQx_qgWaaDNVuv9M6lhwVeNyu6mRbqIcjMdoXmIOfGit5E1yi3IgzBJPvg8FufKnNGufFOq2i2N3VbBgmxb9vwDjwT5nqqdikhg_2_kTxetviPSUq04Yr6S0wJ03Px8q50t9bQfZ1m8lEQxzEqMIBFo8BZaqXyuZNM_Bj-Z491xffq96HCO8xNTT-UYRK0J6yvZOz81w9OUiPDFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sa5OXiBphOoJTGYMyHMkLkVKutvoG52POIrwMen0g2hj4xyukhfNliseVH6p2yZ_gslL8KVC7C0is90MfHAOjug_tRVHIEp_YSUDAVmIJSgkV3oh5ZjbvZWJZYbsaQbCLgYyJ1pjQx_qgWaaDNVuv9M6lhwVeNyu6mRbqIcjMdoXmIOfGit5E1yi3IgzBJPvg8FufKnNGufFOq2i2N3VbBgmxb9vwDjwT5nqqdikhg_2_kTxetviPSUq04Yr6S0wJ03Px8q50t9bQfZ1m8lEQxzEqMIBFo8BZaqXyuZNM_Bj-Z491xffq96HCO8xNTT-UYRK0J6yvZOz81w9OUiPDFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
🇮🇷
آنالیز فنی جالب تراکتور در بازی مقابل شباب الاهلی امارات که باعث شکست نکونام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106846" target="_blank">📅 10:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106845">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=Xr9UGo49sOBecVIF4uvVGlX1MyLhwBrpDfvW3E5C4zxAhFqRiMXQSBuJE7qccA9xvWvY9Ef6Ztp24Zy3HXpicaQgF9u-BOkbTWA2kejiHFDehRQEZz0-2n3aqpDdhgevs02wCaytOtXEpKmvL8wYBNqtIxI4LSXy1dvpow9vXZ7P2UQ9S-ZkgTn7NhHy2nSu6ddQ_AyYkzGmgjt5lObVmrs38-kYb45qg0OwIr7zNR6LZ0qjvJD7S7KvrdKXVtlEZ9VhXuLOHlWwCAQFlDWwYlKecMJShu-Yk9y3LA1VVqUgOCI4GsndA5thnK45Kk9bBkbP_OixTMW2sUTpusB30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=Xr9UGo49sOBecVIF4uvVGlX1MyLhwBrpDfvW3E5C4zxAhFqRiMXQSBuJE7qccA9xvWvY9Ef6Ztp24Zy3HXpicaQgF9u-BOkbTWA2kejiHFDehRQEZz0-2n3aqpDdhgevs02wCaytOtXEpKmvL8wYBNqtIxI4LSXy1dvpow9vXZ7P2UQ9S-ZkgTn7NhHy2nSu6ddQ_AyYkzGmgjt5lObVmrs38-kYb45qg0OwIr7zNR6LZ0qjvJD7S7KvrdKXVtlEZ9VhXuLOHlWwCAQFlDWwYlKecMJShu-Yk9y3LA1VVqUgOCI4GsndA5thnK45Kk9bBkbP_OixTMW2sUTpusB30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
امباپه: "اگر میتونستم، کریستیانو، زیدان و رونالدو رو به رئال مادرید میاوردم. من فکر می‌کنم آدم کیفیت و مهارتش رو هیچوقت از دست نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106845" target="_blank">📅 09:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106844">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2879MJ5Nama79_wZ2ygpAZOwZoCz7chl9I5FW1HkQDs9olLnEvjZue3u4qRMqWx0lG-pkkHIQnOwmvcx_za19bMtJ9dD2J3GtJs7HvD2uJPSHhzVtcoeb75j6xKSb3zhxfti9d7b59853sAdZJniR5E3rEf3IjFgsoLKlinJfDUxeF1EjtnSTw8zTme2FMuk-Rko4zJodxX4_hLR1Djto_DtUimpUWby0xBReKPrMUPQTIyOr6hkTEbb4UQU7dbB1S4EzmIpuTGAwTkPNkDECZMy4ZGFievCyC7E1L0a7iqNv8LGmTI-RqVspKR3knDY6-gdSF0iecvjcBxv9BlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
از عجایب مملکت؛ یک‌نیسان آبی با ۹۵۲ میلیون تومان خلافی بالاخره توقیف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106844" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106843">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=AtpEfzPWXpyuKLQuL2BatwI6BmqVxNi6NU938mLxIcgjkmjEzfQqcw5wIW3ExJIkr4-XRkwX5rgGKMUqErjzaZRAtRu14URWu4kdH-mQujNvW8EObqMG7eC0gZ584vzec6B3vmQMdSvn7VTores8SScGLhmSJUciBg79F9MIaAqZzhMrY02nEDnupOstzTGFYaoCHN-W2s1bE6D2_gIREJt57194s76vVhoLtK0m7LgwFqhUu8qh5RbRxvGmwhE3UXRt-qdHhiG3s-_6fQrrwn_lQEZX05SpPY-PwLnL8dteIM0c_1ARSHTD-bYixtxe5D7aqacPhfeQWrtH_KzCXY7mPAplaxyJPuRp65ZoyAqBdZ2JqUGx6Sy3b7KmCI-1XNQjVjAyZl85pNwp8Pj0QmbiTZ740O7c_e0MUzedvAQBAi9gKQ24_IDqD00HSiwndA6aRkE15OHKGZ1MfmtoP_0svPSm1cL88IFx7wMVAEpw8byoInvmGXBduWadw9MonPeRjVjzPNgKmZ2i4q2Tsb3ssCu4RCuJFIQl29Mr3oe4INo56zvcvL8IZLBxCzgM3kYbEkl6YBihogOWwdLEZkzgbzqqAPTWam3UUHfT-o1Rov-bBYkbI_ofS12759KpuLiUj6LafBYF1MqyLJeOW66GhMzYKS6OGMHTtzQKBBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=AtpEfzPWXpyuKLQuL2BatwI6BmqVxNi6NU938mLxIcgjkmjEzfQqcw5wIW3ExJIkr4-XRkwX5rgGKMUqErjzaZRAtRu14URWu4kdH-mQujNvW8EObqMG7eC0gZ584vzec6B3vmQMdSvn7VTores8SScGLhmSJUciBg79F9MIaAqZzhMrY02nEDnupOstzTGFYaoCHN-W2s1bE6D2_gIREJt57194s76vVhoLtK0m7LgwFqhUu8qh5RbRxvGmwhE3UXRt-qdHhiG3s-_6fQrrwn_lQEZX05SpPY-PwLnL8dteIM0c_1ARSHTD-bYixtxe5D7aqacPhfeQWrtH_KzCXY7mPAplaxyJPuRp65ZoyAqBdZ2JqUGx6Sy3b7KmCI-1XNQjVjAyZl85pNwp8Pj0QmbiTZ740O7c_e0MUzedvAQBAi9gKQ24_IDqD00HSiwndA6aRkE15OHKGZ1MfmtoP_0svPSm1cL88IFx7wMVAEpw8byoInvmGXBduWadw9MonPeRjVjzPNgKmZ2i4q2Tsb3ssCu4RCuJFIQl29Mr3oe4INo56zvcvL8IZLBxCzgM3kYbEkl6YBihogOWwdLEZkzgbzqqAPTWam3UUHfT-o1Rov-bBYkbI_ofS12759KpuLiUj6LafBYF1MqyLJeOW66GhMzYKS6OGMHTtzQKBBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پورن‌استار ایرانی که در ایام‌جنگ اخیر با دختران خوشکل و زیبای اسرائیلی رابطه خشن جنسی برقرار می‌کرد، دست به توبه به درگاه خدا زد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106843" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106842">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DswcDbWfGULuUXulKAC0G9_gCV5EwzFRj330OmZ1w43Xm3QazCu2egzLgu-cgKcFuIaW_z48FKzPGkzru62repqT4aNDQDuAqkk9yn61z1SxUY1hgVChxSLEmsnOdp-5XEkrPmkHCM6UxuRDB4xUgdDb1ZseQFsszaa3Bi7esiCWGZ5tr_BrfeuLxxmoY1MmrsMaImvHXWYvdb4YLGF-6BU_boA-COCHnP8z_7LIvxrOmiS5jbT7u0lVnyeXqnP8ComH5RgQyNZZdJJ9BHWQSy5R_yO6GD1FVC31NA20bD3gYUPcTFtjVoT1xxw1AskajA8HIzi8Bc2Z5gfkz75FLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
فیتیله بعد از ۱۱ سال پخشش رو دوباره از شبکه ماهواره‌ای Fx2، شروع کرد.
هر جمعه ساعت ۱۰ صبح.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106842" target="_blank">📅 08:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106841">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=R53kJ18ZxjizlXUW8zcjOmRxGhScSiHDuS7tS-nZk40Te5rTdlqHhgTgtJv05ec1MsLerZh3L3JEs14EDaEvHM2f-ZoH0vJRul1d88FYlXwtQFOpMDCi1cPiHgxr8TtqtHdZsGugt1EPcs2xB0Y4Jw1z7XpACadXWoh2WFg6Ytmu6iQjCDAQPlCnB4PYl-9hH4erL_wKKPcE5f8dHfMR2GLc537Sl30b2wpO_zyFd1eLEWbKm7EKEERhGTRqq54PZ-ZhEceLPj2SlsGb5l-4oBmvC9qQNo6ztwYdTIvlZ5d4CGRMOoJO_L1b4s1rC62_mlGGyLjG7BEgqb1Phd2cJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=R53kJ18ZxjizlXUW8zcjOmRxGhScSiHDuS7tS-nZk40Te5rTdlqHhgTgtJv05ec1MsLerZh3L3JEs14EDaEvHM2f-ZoH0vJRul1d88FYlXwtQFOpMDCi1cPiHgxr8TtqtHdZsGugt1EPcs2xB0Y4Jw1z7XpACadXWoh2WFg6Ytmu6iQjCDAQPlCnB4PYl-9hH4erL_wKKPcE5f8dHfMR2GLc537Sl30b2wpO_zyFd1eLEWbKm7EKEERhGTRqq54PZ-ZhEceLPj2SlsGb5l-4oBmvC9qQNo6ztwYdTIvlZ5d4CGRMOoJO_L1b4s1rC62_mlGGyLjG7BEgqb1Phd2cJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پاس گل جالب دنیس درگاهی با ضربه سر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106841" target="_blank">📅 08:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106840">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106840" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106839">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106839" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106838">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106838" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106837">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMil7Ckf3oHGfXqSWTikekOgVHRpVQeeINa-tMFkITaz9aSP1h59zH4HUN-HbkM5H92t95qoP18svk7WDl_jzZQcnDtiRZebXkq5pr9OtjE5iNjtkLxllSH3T4V4uEyW1ZqFqgAvC20pUVCuPLEmp3faFXL_PvAheGz2PSCq0uTeC430z8FAc5r5_j3wbDvC253HgB-mJZcf89Bh3NwII0GVPNlVa9aUhY6t7Qahz2m2R5jJ3-HmhcJjifrQsuOlkyRJqSdAh1ZvQ5dV6uUI2cn5lDqYUDfe2wKXzwxbGZvepoO7FmrJjRyoY2gIfVfdcIkCiDweIc7X5vLhgD8voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال درباره علاقه‌اش به نیمار:
🔻
همیشه سعی کردم بازیکنی باشم که با خوشحالی بازی می‌کند، و نیمار تجسم واقعی شادی در یک فوتبالیست بود.
🔻
نیمار از آن بازیکن‌هایی بود که فقط با دیدن بازی‌اش لذت می‌بردی. نوع بازی‌اش باعث می‌شد تماشایش سرگرم‌کننده باشد.
🔻
تقریباً تمام دوران کودکی‌ام، صبح که بیدار می‌شدم یک کلیپ از دریبل‌های نیمار می‌دیدم، بعد یک کلیپ از گل‌هایش... او واقعاً بازیکن خاصی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106837" target="_blank">📅 00:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106836">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfvWi4sG2iDKOrxMVASePB5ew7e3mNlIE08E765JNN0VGuc8T1HqV3mFYdDDDcrcKm9LZZFVlt6XJMvuXHF0T0sl9-rnyd0W7p_LzYS99foBQUj1upz0W1aK1JJ0t1Jedpte1DY4FJHPyBSLtUvLbYU3EpY2-22I1XuhIR4NNzNT3XghF6VAOEjHSc8ZNmRU0Xa_87uI9K-AM9QWDwCW-1GyXDajWtpCmHMrUsv--1t9fw1pWp07O47Wbge3R_2H66aRruN5Ie5ScXTvRfaPpKOHDloootDy_yWQ1LQWQEkbQZNIxjLK-nERzyZcYVNezCdlsZg9osuxwnKvtfHjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
يحیی‌گل‌محمدی و تیمش دهوک در هفته هشتم لیگ‌عراق مقابل حریفشان به تساوی رسیدند. این ششمین تساوی یحیی و تیمش در لیگ‌عراق بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106836" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106835">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGOmgahTmEVvAoWiOIZA7JODkNFnv9mg_98qlLwgQ2x9Y8e7WARMZYIgspkzesi4ljakTD2U1-S-1ItpHRNzl632mBzAqSuxCf3BfxTM_8Ce9B28JI126AMeW859YGNurEJRdZk2C8dKg4Odmt78VNM8UMdV1VpB4kWatmqW8uCHIUWJPdxxuX3myGUqtmfyukzg2TCoVtJWxHniIqX5Ff5zuhTEzj5BjRWtvnv_JmU7-q4kxSVUYat-EYYeef1ofxMpD3O8iec-CNPl9K2_ZnCYUmhH4mNHnBShG2vRcpkD1vYr9XpG3AFoxdKs-X0bnoA-P9pF_Km15UynWnzppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
‼️
لامین‌یامال: تا پارسال پاس گل و دریبل زدن را بیشتر دوست داشتم ، اما الان گل زدن از نظرم بهتره ، گل میزنی و تمام، کارت را انجام دادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106835" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106834">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=KUY3o1npoJZuQPyPIFaqO1dN9isi8AblqZaZKIpIeH52-S3y0fWXeIA2iukM-C4WmbFkRRBsdSaOu3DQRAsdV19HQksYWQ0Zb09ZF1c2iv4crF4TPVyXriRk2Ib0A4izayoGI7JPMLKpn9QR7OouIP5XZXqfqhpmiGbfFwvhSy_1RudY24SOVrgHiFc8_WxJsUdExTfu0HzR5jxTabYu1Qcauif--YdKPKbu3H2X7nesO5T4BtX3M5ICBK3mfCSsd701NpGPYkcWQRtSevc4KqT0XcEs97tuUhNr49sL7e9tST2d0456s6yGlHcjB6caNNos9HvzXOqsg2FtFYxSQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=KUY3o1npoJZuQPyPIFaqO1dN9isi8AblqZaZKIpIeH52-S3y0fWXeIA2iukM-C4WmbFkRRBsdSaOu3DQRAsdV19HQksYWQ0Zb09ZF1c2iv4crF4TPVyXriRk2Ib0A4izayoGI7JPMLKpn9QR7OouIP5XZXqfqhpmiGbfFwvhSy_1RudY24SOVrgHiFc8_WxJsUdExTfu0HzR5jxTabYu1Qcauif--YdKPKbu3H2X7nesO5T4BtX3M5ICBK3mfCSsd701NpGPYkcWQRtSevc4KqT0XcEs97tuUhNr49sL7e9tST2d0456s6yGlHcjB6caNNos9HvzXOqsg2FtFYxSQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمد تقوی، در برنامه هت‌تریک درباره پیروزی استقلال در برابر السد در لیگ نخبگان آسیا گفت: «استقلال نمی‌تواند در لیگ برتر مثل لیگ نخبگان بازی کند، چون نوع بازی تیم‌های ایرانی متفاوت است. دفاع منسجم استقلال اجازه نمی‌داد بازیکنان السد، به راحتی بازی کنند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106834" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106833">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=PqCl8IHja_4ZIwcyHVQt67b4APkWVsK1XRP3nIDN8DzWlgRyS3mq4xfZjzcHw0Uzen_M08G1-84UgyiNvrhgU-fQw5s5G9FLDg7bFPDbTdRr5NNKKAuWiUeNO8m94EMwFc7MLIVUzCg8Zcd-lYU6eGmULvBpRokj7nySJnaP0_G0DqvbkwoVY3ucuK_3k5l72Oswyiwl-tx6ZvPwAmZEyIYuy6lwutyqHAO0Bygf5_Ur8YMhqQilXrftkSlf8nkUqmtcm9psZVpQ0JNlDkHNlEW1KCStiaLRUKQZKYMlRK9tyl6eJZEere3eq0QC4P54jYPAJYUqw6RIiwUAXnpUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=PqCl8IHja_4ZIwcyHVQt67b4APkWVsK1XRP3nIDN8DzWlgRyS3mq4xfZjzcHw0Uzen_M08G1-84UgyiNvrhgU-fQw5s5G9FLDg7bFPDbTdRr5NNKKAuWiUeNO8m94EMwFc7MLIVUzCg8Zcd-lYU6eGmULvBpRokj7nySJnaP0_G0DqvbkwoVY3ucuK_3k5l72Oswyiwl-tx6ZvPwAmZEyIYuy6lwutyqHAO0Bygf5_Ur8YMhqQilXrftkSlf8nkUqmtcm9psZVpQ0JNlDkHNlEW1KCStiaLRUKQZKYMlRK9tyl6eJZEere3eq0QC4P54jYPAJYUqw6RIiwUAXnpUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
گل‌های دیدار بایرن مونیخ - بوینیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106833" target="_blank">📅 00:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106832">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=fSXu8H_fVxpZmijrx5fd8Y-RU_VnkAN1P3PQYWjq7ha_bkpOP36qvISkrywB52-mQmdtFA504MSuwL8xxtPxq5TkIYp25Zn_C5CRyUCe_9x5LwjVWq_UfumnenAJDghQnUUGmdstPHpegAl4cVKWDejj2y0DdHSww_3TndURMQ9c6FKalw_iJh97OKSl-yO8O53avYzPSfHpOKKhM7PdGxxCR3VpK2mTUR0GPnzp9X7dOGbuykU_kEtOVsEwHFW60ubhDFN9_RL18by-NVClvckKdIhSdwE01h_O9aY878-huBEVJEXQZU_IaAfzZJZi0nG0d6iV_0Ni9HFzk5EGPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=fSXu8H_fVxpZmijrx5fd8Y-RU_VnkAN1P3PQYWjq7ha_bkpOP36qvISkrywB52-mQmdtFA504MSuwL8xxtPxq5TkIYp25Zn_C5CRyUCe_9x5LwjVWq_UfumnenAJDghQnUUGmdstPHpegAl4cVKWDejj2y0DdHSww_3TndURMQ9c6FKalw_iJh97OKSl-yO8O53avYzPSfHpOKKhM7PdGxxCR3VpK2mTUR0GPnzp9X7dOGbuykU_kEtOVsEwHFW60ubhDFN9_RL18by-NVClvckKdIhSdwE01h_O9aY878-huBEVJEXQZU_IaAfzZJZi0nG0d6iV_0Ni9HFzk5EGPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇪
سوپرگل دیدنی اولیسه مقابل یونیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106832" target="_blank">📅 22:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diDwsJGKpngk4KAVj_XCs5wMAp-thGIo93oOpzjDQJ-GtRBgMSwG2GM8uLPTihaDb4SyE-X2qOoBX6iN_5nQM_tIPIbWalqIG9Hch7mBTjY8z12FYaGGXSYhDffFH3QOHj81AJjr3gJmAxeSXOR6e-OQNuQr5D3dm6dx5TvPtthB9GgpTBVCX1emDS_QwuKWj_tq1d3-KJ1FGaTyXhbxYcRccnM6kd1Y0AW1UoyaEa5GyctLnzhxxILbIuEgLzkHSDwz-nQJS9N3aVli-6G_XTQNMdNxD05FfWBiTbFL7uvFOYqRmI8SltxzfqjDeEF0Ix9vCpVoNsMsLEJKHaAl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
🇪🇸
پس از دو بازی غیبت بدلیل مصدومیت، آلوارز به دیدار یکشنبه مقابل رئال‌مادرید رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106831" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRV29eaRiQXVl4YZRWauTrBqRvc8kkRFVWVblvgsSbvxSGHH0LFDZ-ZYudBzF_0adP5SJx3eI-z9wtBUsCRycLhFP_ETlTu7K39w0yeXoVb9nvPLtPKMaRliFVz-81maFUhOISkK3UMjyEorgGWs8BoenMg_eN5VmfmeZozQGbM2__rvZgcYMJFh53LPZ0C6i7kPhVJJlVzQ_5Hy2h0grd5MoSSedBwAF7GYSoutumE-sepA0IfgYcaW-NStnZJN-V79kTTF3ubrId-hC5nDteLrXu2BXqB-bMyzYsdKeqRlagQD7JNg_O2a-B-kDuvWIVV8LuZBT1zcotTMaaHA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
داکنز نازون پس از عدم موفقیت در بازگشت به استقلال، راهی النصر لیبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106830" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106829">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=XD4wq-sEA_xPGT2fWhmXIkbuyU_gMOUYNhbZ4eG8A2acBlSoo2Iul_8Cq52_4B7JOoIAwhSRXkAo5fuMYO5zSh7Q0qSps_uWy_BZdhQsiD5ejppSn7yO7BEZPFicYe33Cj3IGApjLxv2Z-brNMF8FHrxi6QHSwSpgQX25stxseFKtwBK1gIyDmbVKKvvTyIaQWhaVp9GbFLVZV1Z2SPqaQpoiqBX4cKSeyM_W7ZkCRSoQUObOGXHTPmUPAGEx2n9Jf4VoReO4ynDvJzuOjNDKN059eii7Flh8fXzS4KRW2bK6qtgBFbQq9Xjs4mhiEWN5KKoIS7yvqvjuatkwvEnWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=XD4wq-sEA_xPGT2fWhmXIkbuyU_gMOUYNhbZ4eG8A2acBlSoo2Iul_8Cq52_4B7JOoIAwhSRXkAo5fuMYO5zSh7Q0qSps_uWy_BZdhQsiD5ejppSn7yO7BEZPFicYe33Cj3IGApjLxv2Z-brNMF8FHrxi6QHSwSpgQX25stxseFKtwBK1gIyDmbVKKvvTyIaQWhaVp9GbFLVZV1Z2SPqaQpoiqBX4cKSeyM_W7ZkCRSoQUObOGXHTPmUPAGEx2n9Jf4VoReO4ynDvJzuOjNDKN059eii7Flh8fXzS4KRW2bK6qtgBFbQq9Xjs4mhiEWN5KKoIS7yvqvjuatkwvEnWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف‌فروش آیفون ۱۸ در اولین روز فروش رسمی‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106829" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AinvI137bMbjHZgPiV0RuU6BEjS1-gZkihZ0jlZpZVpjR-nTt63g8EiRge6muV8gMzZfpRUJ8UWtDi9YzW2u9CN769dJxs5I0UaEOu5kyQNJHDY_Qh_ibumC_xqq10-lOQCBxkV_j0SwUqAAbN4oFwf_yrh3DX0zl15-j1YaDtk1BntE0831B2kQQ_g3P5M2j74PN1jujJS-3RJeSuJ-KNNM7uamzUScNXwBNGYbb-DBgzC-7R8KAaySwdpc6PFb9V5TmoIvohgEsGW6kImMFw9oosEmXJGG8ha5sjXPkE1CYu40oPlAjqHZENyUcXUCMhrJUcxSaCfucSM5AaDcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XnbtvpliA3DrlJfN1PmYEzdS6GR2rZ0blT1l-X9lOK0ZtpIw4KmIoSC3al9EclMkebsNwdgj4GX0vUSGi43cIPUJxHUrAkn4RKnVfTbcDNBXFUMHVyG9EBM_ArfBqJNYhPz9eQV-6R13p4YChP4G6r4jJaqEA8Dwtx4GDiZ4e4GTzAtFE3-tc-HWQCey6SNWJ6QAPhCRJ8lj41D5NDufq5dRALr0iivtD0RVpE451AuiZF-iOFPscb3jP5AOwUh8BiH3uvXkoDSB8pCo1fdzXnC4nvcRZIcgHvGOcpXtWGP3Ht406hZRtgWkoUssWwsdYgOlZKthbu64HimCXCk69A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🗓
سه سال پیش در چنین روزی
رونالدو برای اولین و آخرین بار اومد ایران و دوتا بازی بعدی النصر تو ایران رو پیچوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106827" target="_blank">📅 21:26 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
