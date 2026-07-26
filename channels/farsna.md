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
<img src="https://cdn4.telesco.pe/file/hifPu5GDa8jtfV0viVJp9frf4UCPGdMol0Qdg98lNebRu7rTO-o5EIqIiEk8r5jsr6hJCX0A55l7Z7yi41xrbjoB80k6cSkpmBdjXqg90xGwHy57ZFRemzfZwRCM19OzfmsYKXtfUNuVHynWqjevyu0ILe4CTBCg3AoqxjCWWDZ9jzXUQqN3PPhSy8tUFvxmVv25XCShb_-rrrHQOmDDQ5z3S2L6A71_He3z-kTM6iUwforljftFbDTaE9hdsHQ2ah4n0pVH_psXs_kP5qYJQBgCOhB4uzY8oTOx9zBNYbubpCl0Tj5QuZzKy-CT7p7BUDDmHOWlVZaFdx3jPjjZvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 16:05:54</div>
<hr>

<div class="tg-post" id="msg-452678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=jCGaGtlJDGdjkroiGiNU7Y-o0HAITZAg5KGuIKL5leFAm-8MQ7Y4RDwdjvZvgIVToJcjNL7xhVJ4cGCVEYBrEBS99roBL779PjO-YRtMBDIyTgz_lazP3bWvk1Z0CJ_HYWTqQVB1LjY-13I-1gc5uetOoTypmx1TWNdCVIh91tk8_A0Wb46QFcpLcnLCa-XaUiqEMs_BCgk87km79WmuFvb4q1CIviASI6YaQ3V8tERRpYWvOdeSgShIxzDXezh_eAlOLjmlgUCdssBT7_4dNMPTaWRkNlcHkb21kMbG9lqltzUD7cAp0BHFLgop3_XxgrpT3ZxBMuJDWpAnG72Xbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=jCGaGtlJDGdjkroiGiNU7Y-o0HAITZAg5KGuIKL5leFAm-8MQ7Y4RDwdjvZvgIVToJcjNL7xhVJ4cGCVEYBrEBS99roBL779PjO-YRtMBDIyTgz_lazP3bWvk1Z0CJ_HYWTqQVB1LjY-13I-1gc5uetOoTypmx1TWNdCVIh91tk8_A0Wb46QFcpLcnLCa-XaUiqEMs_BCgk87km79WmuFvb4q1CIviASI6YaQ3V8tERRpYWvOdeSgShIxzDXezh_eAlOLjmlgUCdssBT7_4dNMPTaWRkNlcHkb21kMbG9lqltzUD7cAp0BHFLgop3_XxgrpT3ZxBMuJDWpAnG72Xbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی: دود غلیظی مناطق وسیعی در اطراف پالایشگاه نفت جازان عربستان را فرا گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/452678" target="_blank">📅 16:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">۳ محصول جدید لبنی یارانه‌دار شد
🔹
کارگروه امنیت غذایی ۳ محصول جدید شامل شیر بطری یک‌لیتری ۲.۵ درصد چربی، شیر نایلونی ۹۰۰ گرمی ۲.۵ درصد چربی و ماست دبه‌ای ۲ کیلوگرمی ۲.۵ درصد چربی را به فهرست کالاهای یارانۀ لبنیات اضافه کرد.
🔹
با این تصمیم، تعداد اقلام لبنی یارانه‌ای از ۴ به ۷ قلم افزایش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/452677" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
سپاه: دو نفتکش متخلف با قصد عبور از مسیر ناایمن جنوب تنگۀ هرمز، بر اثر انفجار دچار حریق گسترده شده و متوقف شدند
🔹
ساعتی پیش دو نفتکش متخلف که با فریب ارتش کودک‌کش آمریکا قصد عبور از مسیر خطرناک جنوب تنگۀ هرمز را داشتند، بر اثر انفجار دچار حریق گسترده شده…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/452676" target="_blank">📅 15:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYQnNXpUiZEPI5fHUKMk-9AUdqH0LdsDjehBOPrk5PGkBXhkXnfPn3odwyOPiw8LoxKJQXMIItf3vJxFPpA3BzsVmV9Mqt2e2TRnGY-0O7njqH7CqnzGwQKbHuvY8zKnKJuIe4kDvqKd59U4SQQmIS76WHOM-PIiCpIrj8lUvv_AyvvV6D1QxTSI2nwIyIqiZ0z0-lEanu6s8v3OADQiUch2Qi3PWJEpYCbAwxk_m1vTM78qJDsU4oQRr7pmNJws0dSLOAhqEyGgJruuOJNlooraMTkGOS354hBkGOfRYKr3h-nEOvPJRTdAFfoLUzDiai3YwVGSkFG8KASg1NzWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد سنگین در جاده‌های مرزی تا ۴۸ ساعت آینده
🔹
راهور فراجا: تردد زائران در مسیرهای منتهی به مرزهای اربعینی به اوج رسیده و این حجم تا ۴۸ ساعت آینده ادامه دارد؛ بیش‌از ۶۰ درصد زائران، مرز مهران را برای خروج از کشور انتخاب کرده‌اند.
🔹
تاکنون تنها ۲۰ نفر از زائران در جاده‌های کشور مصدوم شده‌اند و خوشبختانه هیچ مورد فوتی ناشی از تصادفات در سفرهای اربعین گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/452675" target="_blank">📅 15:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPPyWK-p8pAvsroTiqvvrOvHK0qN4pWp7aBJAjSZs5Okd1x8UoVR_vDpHcpg81aHni3izcDBD5zU9qUmGn4GJWMjLIP0JFFDqack8hqMa--KZESWT4nUvQ9RVJbapXGMXCd49SV9D8GPtxGO2hFnfstir-WqGe62zHFTt9cqttvlw-2dGlgzDetLaSHdldVXunTE3qt6A45DvMBv0McJAQk973clr3klQ-2wg6ACnG9VVUVoidF12wycVpfhLaQorJyeC4_A33KEM4ko9QfXGwNX06XpaFTNWG1c8GT574zmTdOEy6-DE8qio_d2ym23Ad8dwwOsWDjFm9kruig33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nraOxyXEE0BDUZAJjwkPzyqAJx6xaM5BbByq2yFW2-MtaitRBHgOJ_2hPQhCD6PaoUTZrOE9K9-zxbsqJpqbhpHm5FqwrrvPG7xoi2yFiX3Vyrkj9hnJx6ALHjK6PpROPY6VQ6raU0-9u7B-tVPCfGBpjRtj7HOffdZW4c4YXulEbplFELch09nTJmCrDcLij-YjNXrtUNo57MH40cdjuNRzwN7eZfar4Tb7ce3Kbzj3Hw-ZRQbRPiVK8uKaVENccfQoLu_OtXsisRqivtUyXFSD0Y2esuL-lyEEojdhW87MBtS3PWR_m7iZkpqV3qTGs_q3YFvZQAFkLBWhgWYVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTG7d30sJGcA4hOp0MA0p_zypW1MSTGtuNv56ia8lUKegsLhcD2qzTEDOClKkzuq6I3m7RpnkmkGEiX5WATOiLAxaCDT4sxrWJfBl-_rotkEY6F5t19StopsS4CcFbGFBRLUNU-VvDZERMnEKX6pUzUdW8qUHHLjZHKvCsYs2kek4A0iKK6solYXxDskxM5g5znaFkwnudUDOeMIBCA8hici7cA7t2IKbq1k1Se3unAPpMfL6P9Du7jkesAcrfSKjldyJmaJYc8poltiNVWA3-RST0EyPzRZwqdpGWeSceomdM6wIcUtRJL5pu7esjQEQoyk2XxuS-BWS04cE20hqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpZ9ErKld7NOezrNcYPnTCSQCwpd8-iqlZLAa4EME7GxC64HXrhT85NJFk9KbbBGByeA3Em7wZz8-0MAE4oRTowvuC72KWXxW4-GwyXqnwTrCkH8MFa2OsLbe5ygtSw_8jqXXT4VP-6T5pHDKkmA6HFBXnq1yXqSw3MQuhYiVyAUx4sUejOcBa0EydGg3x36mXB7zEbbs9Sx4E8SA0shAvlnjiaE5rgfXPcgAHtBc80p-TNbzm6bLKWeTwI5Rtb9Jdc6UG396mZWUV_ax7z2Hdv4A-H36LBcOaC1eAqYCk7rmI0M1VMEEjq3IQ-Cp4DjXxUL1DOo9ru7bQ4N09CddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1agOuVVzmOPrqpGVbFNg5ybLQhRvg9wN6IvypXM3sdnJ3gFNQh5qUoTd7seobn1fjcxKkMDlgy_1lfs3OwnBENfgXRRa8rqoNH3bqltMIJQPxOG9fL-1N8wuN7hlwG8t8YXuZ6ICiqeoP9BTV-siIqUAqpO0jaMkmxm7uKY24F80qbI6ZherWkczNqBYwn2fQHIRAHIGNdWfPNi5GCTSNmRlTm-LzpR0epY1UrWkZXWd4VB-ehoO2hlsYVEU-fuZyJUEtZZUxx3-Frg_mJqapy-wZq0fGwHiXJtxMv0dcY937jAX_GhQkLFIjA2n-s45o5TkSBgYrWkFgPWDxtL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8J9bJNF8-N1iSnUWtugpbBDjwSndXJjtgDfH03WpV7U9kPDopaH1RqHlKazqHpVoud9IAtby2KpkkiT3y4fSNde7ZV27CLlm4NXDWE0RP4rEi_5K8Su-wvBjBym7WDDxGXfc2TbIl1KyPKRyskcmaUj4HNuxJlh4uwXsXXp6-mt6_o1QW8qW0gP2WcC8LFw_RI6ZhlFTh261YLwh3xtBqmX28XVWMtL7oBCkizBSRjv50Y4brbYe4lsYBeDDK6X8-BKLunQBNqQolge7Zr_SCIRc7V3kkpn3V-t6Xpu0X6BMYOLapyrlmuHBmJBw7b-VznKTuo9R-HpazdYfJFeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFFkSi4jsmwpd0F3ceSb_rnmRWTm3uVZG-ml_-yBGhuJyo-nZ8yMKiPdWDSALr3V7deSofKQ5971dVBjD11zeXc_m9QEgXmWfvM4fR96Yacxjmvyos6q7V9KHwWFMMANcaajsXWTGQewxGzPxeuckmsQH6TUqsHwPIJkDjDQiK8M3XumGLgSSmTSsq6_lTUQJ-mrbNZE_XmyYM2XYBtnFLn8RFkzvJpfv_JLWodzi5eeTkjxBuD4A8cDgPOaCIpBMhpEJ260Nw0wvvQ5K8-Wk5e-LI-htZPLZCbzrXXmRypAzVeLuoXjV185GuSjUtd2Umt29YfDBmcgeoFhLQ4YpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میزبانی گرم عراقی‌ها از زائران ایرانی در منذریه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/452668" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY0zL2r-0wPeFN874mpx-e_D7KHXp1Tf3MnCQA5nIgNIGNk2A0B9tpJbZF33pc3CN5AjPjBVwjCXsTIOaP1vBhyegdj0M1UWh6b1Kg9tVoHqgJmY1mL7-ksntGJq-cjYpLQaogZ7O1OgXvrGM_sklgAYv9mpXy2o7R3UsagPhx96YYzVxh6mAVlTzzhbgPsPi49tgKjcadVstJTP2GB_FU1d_a9we3BS3WyLc9DLgCybKLG-p69A3UeB1H8d4rEBwiiMu6_P3VWF1Gn2EFdT0E56wpNXpFbSaPvggAqAZ-5zsp0VlnfKYlrOzKkBvC3M4Tx01b2ysIgPrj12MgWybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری خوزستان: ظرفیت پارکینگ‌های مرز چذابه به ۱۰۰ هکتار افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/452667" target="_blank">📅 15:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896bc839db.mp4?token=Gvzm9klzkSDFDkgYfAH-Pc_pFl9-B1LaKXiuWBwc5-xZpNQFL465Q9kJpHAOvNLYYW48YEa1mMTiIJ6GWjQTCqjttfBw_6yEkqFlrfdta1_f7vHxqsIgMpgAVmHw6OUSKDKgS6gvPwmdjyet3HjCA9Dsxn1NTMEBdYbwWJzxVpw34lEWP0kFkDQoP3xYGpgqRuLoDhDO559YHJ-qv_SBmt-IqSxY3LZC6xqq55A57MopdRuxUhRoHywuh810OmrZYK9UKsQGpFKDS0jy7SK6m0bw-pqcFKaQZPnLzwKrdEDt3xusPXog8hcXMs3fftXV1S3psz3kn0jDfFmwz81zDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896bc839db.mp4?token=Gvzm9klzkSDFDkgYfAH-Pc_pFl9-B1LaKXiuWBwc5-xZpNQFL465Q9kJpHAOvNLYYW48YEa1mMTiIJ6GWjQTCqjttfBw_6yEkqFlrfdta1_f7vHxqsIgMpgAVmHw6OUSKDKgS6gvPwmdjyet3HjCA9Dsxn1NTMEBdYbwWJzxVpw34lEWP0kFkDQoP3xYGpgqRuLoDhDO559YHJ-qv_SBmt-IqSxY3LZC6xqq55A57MopdRuxUhRoHywuh810OmrZYK9UKsQGpFKDS0jy7SK6m0bw-pqcFKaQZPnLzwKrdEDt3xusPXog8hcXMs3fftXV1S3psz3kn0jDfFmwz81zDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تشییع پیکر زنده‌یاد اکبر عبدی  عکس: محمدحسن اصلانی @Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/452666" target="_blank">📅 15:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exIoewVM3rP-RLrnAKfBcWQafM31bWfMxg3Vr5Z9TbM5NlIyQJeHcm6UW5hoZzTQimgopNbT3dx9GrWqc0kyJo16CMXZLriU4fCDNFX5Ku6A1kMCqOnS07miPJj7S0NqDrKU7-4XpnkfWv7cMaYiZMcmkPxThMeFnf4Z0G7aEQBVI9BGupEPYwMA_pGmtaUOXWj8VzFd-R66Q3QMa1dgA6lNnc-BBmax4fZBe_isMm5pVGM5evhBqQosTuvr8iAJG1g4RKtU8Vd95W6MzalU23fEy68TN75cQN403K7IJ4xyy9nol-veiOzku3HV_ei-IHtsRQp-sdgH7V5399qomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثهٔ دریایی در جنوب دریای سرخ خبر می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/452665" target="_blank">📅 14:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=XaKzszxjLh7T0C_humIv2qQIc1MQA1b4nDJoe-p6kTaUBufGGIWmzHVh42hjZA_yl9-1CZlue3Bf5M6MevHPp0s7dVhd6Ev8p0ex9nnaqwrZ1w_s_5IvXcyEPiOYDWmEuK16djgEKx2yDPs6ACb9iaPXRnFhoYj3E-jP3Kju2qEE33FHureA0xyOLxyTChCOQ7GFdimFPqcX99LU8IaAvKhDKrycpg2gMgjADtpZZNXkcaHk2Y7BJgwMt2KXDp3LpLbzSuo9oMkKwissly2oAWABufQQvhWniW-lBr8jDxzZIowX9wCCpQRBjX8l-tQgX1BSJobXitntgWCxLoJzNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=XaKzszxjLh7T0C_humIv2qQIc1MQA1b4nDJoe-p6kTaUBufGGIWmzHVh42hjZA_yl9-1CZlue3Bf5M6MevHPp0s7dVhd6Ev8p0ex9nnaqwrZ1w_s_5IvXcyEPiOYDWmEuK16djgEKx2yDPs6ACb9iaPXRnFhoYj3E-jP3Kju2qEE33FHureA0xyOLxyTChCOQ7GFdimFPqcX99LU8IaAvKhDKrycpg2gMgjADtpZZNXkcaHk2Y7BJgwMt2KXDp3LpLbzSuo9oMkKwissly2oAWABufQQvhWniW-lBr8jDxzZIowX9wCCpQRBjX8l-tQgX1BSJobXitntgWCxLoJzNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف‌قراردادن کشتی ترکیه‌ای توسط روسیه
🔹
یک کشتی باری تحت مدیریت یک شرکت ترکیه‌ای در نزدیکی منطقهٔ اودسا در سواحل دریای سیاه اوکراین هدف حملهٔ یک پهپاد روسی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/452664" target="_blank">📅 14:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzAT0bFWWD4KixtC2gzT_v0sQCJzhm_2buSNQXCm8d3WThD63CwdhU0Bikyh9JyyUlFVfFJtjJq_cbXxTWtF1QDlpP44xsHQBgOPnmzYrL84xu12mPyGI58HBPACOWASsxEPQH0G6ID7S3D6c774uuCOdZwky9QNdi0wHQ0n2DI1YA1Wfa6MsEuQM8-yzcIssPdIvIAWd89MvuqkFpz_rPayreTkGtaRhLYe1-mJmZsjV8KZIrPM578syIxlnNUrQH_BvURzMCxNtiZyzCJl0PNry2U0CNV2c4jP6svkOZbydKFJvnhKlR36Vtgtc6a13v9AZ3C0J87ceFuENCFApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنادر کویت و عربستان خالی شدند
🔹
پایش‌های ماهواره‌ای از کاهش سرعت بارگیری محموله‌ها در بنادر کویت و عربستان در ۶ ساعت گذشته حکایت دارد.
🔹
تصاویر جدید نیز نشان می‌دهد اسکله‌های نفتی الاحمدی در کویت و جبیل در عربستان تقریباً خالی شده‌اند.
🔹
به‌گفتهٔ یک تحلیل‌گر تصاویر ماهواره‌ای، اسکله‌ها به‌تدریج خلوت‌تر شده‌اند و تعداد کشتی‌های بارگیری‌شده‌ای هم روزبه‌روز کمتر می‌شود.
🔸
این وضعیت پس از حملات یمن به تأسیسات نفتی آرامکو و بندر ینبع و همچنین حملات ایران به مراکز پشتیبانی آمریکا در کویت مشاهده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/452663" target="_blank">📅 14:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1b66c659.mp4?token=dQ6tQHKm7Nc8SVXAYA26NO_LZF8d8czpoBFrrmnYW1sFtTDKFnRT2dHiWxjav8ORnuWlZy-aOTiPkcE-Ny4ZdLCbWqMcX0wPZdjuvS935Ub6l9CufcEWRP106ZECPwXeDWYJOewigE0DSdqP7fZVTlAmfqoyBRe6O5KRd9owJSCpw2oAwOywkbyjcEfpkhu2Yng3LnEA0iFJhYatLculXwuiRklnAYv6QSn1P_KRTTNXeUnjD0kapWedUgaU5jrbiPLDx32FjENrHKEa6KB5vZMxyzyRAbpeS6OyA9B1yUswhqFtAcR9q-q_5P-aqjpR1SlNhcOLrRGiwj7tIbqj2CBaTPvkLLxA9gqB9kOVCB4Globhl4Al6oMT082KWGtfWKPjKkR-SNlf29wkJ7iDN6v3tRDlEe7P4iuZlBPgD-vE_h_nTArwPIstXA499rYFI02cZEh9AoxjzaGfGRPYv_3q4DQSaX1kW3Sw3naiMciwBZVxrG5xhZlIMRroF_JAfnzk_Ml_NICneiyNO2CpM-LHn9Jaqjr6BLtr3SiqXgLcIAhtLqgzwDYbNbyIRiXT6IShG8SZYPRPwwBuauSoikCZ_TQUwL8lvCXZFWZ1mirtn2mS9Lgt7lGdEvwqjEuW2M-MkY8Pkl_dvrewzC6b-biF6pkUL5wzR5aIrSqIQGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1b66c659.mp4?token=dQ6tQHKm7Nc8SVXAYA26NO_LZF8d8czpoBFrrmnYW1sFtTDKFnRT2dHiWxjav8ORnuWlZy-aOTiPkcE-Ny4ZdLCbWqMcX0wPZdjuvS935Ub6l9CufcEWRP106ZECPwXeDWYJOewigE0DSdqP7fZVTlAmfqoyBRe6O5KRd9owJSCpw2oAwOywkbyjcEfpkhu2Yng3LnEA0iFJhYatLculXwuiRklnAYv6QSn1P_KRTTNXeUnjD0kapWedUgaU5jrbiPLDx32FjENrHKEa6KB5vZMxyzyRAbpeS6OyA9B1yUswhqFtAcR9q-q_5P-aqjpR1SlNhcOLrRGiwj7tIbqj2CBaTPvkLLxA9gqB9kOVCB4Globhl4Al6oMT082KWGtfWKPjKkR-SNlf29wkJ7iDN6v3tRDlEe7P4iuZlBPgD-vE_h_nTArwPIstXA499rYFI02cZEh9AoxjzaGfGRPYv_3q4DQSaX1kW3Sw3naiMciwBZVxrG5xhZlIMRroF_JAfnzk_Ml_NICneiyNO2CpM-LHn9Jaqjr6BLtr3SiqXgLcIAhtLqgzwDYbNbyIRiXT6IShG8SZYPRPwwBuauSoikCZ_TQUwL8lvCXZFWZ1mirtn2mS9Lgt7lGdEvwqjEuW2M-MkY8Pkl_dvrewzC6b-biF6pkUL5wzR5aIrSqIQGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان کشتی‌های متوقف‌شده در تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/452662" target="_blank">📅 14:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452661">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7f0c9700.mp4?token=tyLFXzDvhpOWSGzqKkyGgYI0nd9nxdEwDBu2uzHk1TmECMSziWRYoIcDpDLjCJPXFfoVcFHoz2586P68Gj3jUa_w0TJem2neKTunkyq00HoxZYBKCZ0bUGuH-95DPWMHbFt5Zq-FId04fSz_OgYC5NbzO70QOIWskge02yKMwred_BQ2XQ4-oZFRHoRV1tg4FH7IjomMXBpSevSbw7O0sRfoLE4RNme5h6AZSJgic6Qc4H60HPXlVuD2I62lvVhFuEOsFucv2MKNzvYN6YWVmMhjUScbe9I0m4xyMeGajF5tLd0vcoGbW4MstBrepT00hBTyM5z_iSCd2_4sDkw4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7f0c9700.mp4?token=tyLFXzDvhpOWSGzqKkyGgYI0nd9nxdEwDBu2uzHk1TmECMSziWRYoIcDpDLjCJPXFfoVcFHoz2586P68Gj3jUa_w0TJem2neKTunkyq00HoxZYBKCZ0bUGuH-95DPWMHbFt5Zq-FId04fSz_OgYC5NbzO70QOIWskge02yKMwred_BQ2XQ4-oZFRHoRV1tg4FH7IjomMXBpSevSbw7O0sRfoLE4RNme5h6AZSJgic6Qc4H60HPXlVuD2I62lvVhFuEOsFucv2MKNzvYN6YWVmMhjUScbe9I0m4xyMeGajF5tLd0vcoGbW4MstBrepT00hBTyM5z_iSCd2_4sDkw4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برق صرفه‌جویی‌شده راهی جنوب می‌شود
🔹
در پی ثبت پویش حذف خاموشی برق در
هرمزگان، خوزستان، بوشهر و سیستان‌ و بلوچستان
، مطالبه‌ای عمومی مطرح شده است که با توجه به گرمای شدید این مناطق، حتی در صورت افزایش چنددقیقه‌ای خاموشی در سایر استان‌ها، برق این چهار استان قطع نشود؛ مطالبه‌ای که
وزیر نیرو
نیز در واکنش به آن اعلام کرده برق صرفه‌جویی‌شده در دیگر نقاط کشور به مناطق جنوبی اختصاص می‌یابد.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/452661" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452660">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfba51605.mp4?token=qMtry7gfnniVnEilkmAjKepCuUVKyDRruGxHpn-f-B7AvQIHOToXbAwQA_pzayTf_4ggKTGgHlSTRf-Uy6vBJP0fXOCDHh3EggXoeU2VVTudVIPePq8pZf_rcl58eljguylA1hi2gMbGFSPrDrfR7MbPAv7drdujcgVe20BppXq8ZpK1gDx7YuWHo3JBWTJHHpRntLnJ_3fCmVakMGSnPStwZLR1EwuPp5xNUSe9jqv8X5_RGd7rwfj-MpcB7zQ-ra4jM2JxkEeqJ7c6EDl3SpAU4IRUbkYUUrZ_ERTHCiwR_ihcEc15TH4SznjcU0u5jGReEoDWFBW6MIOq1oNMjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfba51605.mp4?token=qMtry7gfnniVnEilkmAjKepCuUVKyDRruGxHpn-f-B7AvQIHOToXbAwQA_pzayTf_4ggKTGgHlSTRf-Uy6vBJP0fXOCDHh3EggXoeU2VVTudVIPePq8pZf_rcl58eljguylA1hi2gMbGFSPrDrfR7MbPAv7drdujcgVe20BppXq8ZpK1gDx7YuWHo3JBWTJHHpRntLnJ_3fCmVakMGSnPStwZLR1EwuPp5xNUSe9jqv8X5_RGd7rwfj-MpcB7zQ-ra4jM2JxkEeqJ7c6EDl3SpAU4IRUbkYUUrZ_ERTHCiwR_ihcEc15TH4SznjcU0u5jGReEoDWFBW6MIOq1oNMjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در جلسۀ علنی وبیناری امروز مجلس، کلیات لایحۀ مقابله با جنایت بین‌المللی با ۱۷۰ رای موافق تصویب شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/452660" target="_blank">📅 14:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452659">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/johQJLECn_hjRcgXwZFaC4g7f6rU9xMUd1BExVyyF524ovElwCRqQGvMDk6gbKgGX_HjgbOlkEW-ZShiCK-RKoTmexJrXLhlvSTbOWwlgaxr2T6w06328ebfym7WAXGAuqlEdF0IrwhAVEpsSOqbpGDtQotXgQt6Gss7HnR5PCrol2q_Tapy7BrmPD7IFjRXrxf78UUiiJtOxSIqq0uXN4w2FErFRyL9M8IpwvT_piGYNfMz8i-KC8Hn94TB9PkyTuyKu25B23Qlrc9IbfVW4dubwD4jfDdWqOGgHRrVG50vg_p4IvZZlYC9cQYvFOaN0PfJ2nz_BqGbZkHR_7P_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: مجازی‌شدن مدارس از مهر شایعه است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/452659" target="_blank">📅 14:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452658">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXCNmkTJ3QyaKHXnYwqRuUDi601yUHG8YGB4NHR1dui8z873XpRx5gi3tRUybAhaEQRdcK_WeAvoOLmOE32ozWPcFVGGgfOyWPzDu12HB-vmJnuVsXK6C0pXciiiCNVvZ-e6tMh8hmpXeZ7XzOI1sDjmvnB_4m7fSaoQ-1JSic_Q1gy0UIbn3jwDGzM-X5EsKq-ZttfACUimod60v_TPYHuSlkg3R5I8bXfzXXRBhLnU-WaL8qQ_kqD545UYmU7BzwTsWbBwo4k-Jhe1CvyKtl19CYgLjVaUA7AJqOGTeSLHtiEpuw-OsIx0q1SJ7qNZi5Uf1DQvXsfmzaSceRCY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باند فروش دینار جعلی متلاشی شد
🔹
پلیس آگاهی تهران از دستگیری اعضای یک باند چهار نفره خبر داد که با فروش دینار جعلی از زائران اربعین کلاهبرداری می‌کردند.
🔹
در بازرسی از مخفیگاه متهمان، ۵ هزار و ۳۵۰ قطعه دینار جعلی کشف شد.
🔹
پلیس از زائران خواست ارز مورد نیاز خود را فقط از بانک‌ها و صرافی‌های مجاز تهیه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/452658" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452657">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d6a73b6f.mp4?token=RHavkvbtEhzmdiNeCxal_BBkVSm3asAj51jvpRz_-taXsuVjp83jPWL4qwrALzY5wfguJq9s1oNsj0W8ApwnX1ppP3gjDq4Ag5OwOjL5Yy71esEN61BPmXPa0EdXrR0TB3JnTeE2EBRHVnJDSw9S7UtDSefKdpM2ivnoB4DPhXn6kLFD4ebYsBPAqJd-TlEJuOmu_053KIBBKxJrcPFziqqHtZOvDcJJH47kgyrRF3fS70liKBQ6b3ytvI1ZhW-JYf5XEjLwoZdw4z8mLiPxi0FkdBF4r0_-9Mj7-ajl-SZJnw8eMt8l15LUttb59ruMiDTonkCGWaKIqKHV1s82IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d6a73b6f.mp4?token=RHavkvbtEhzmdiNeCxal_BBkVSm3asAj51jvpRz_-taXsuVjp83jPWL4qwrALzY5wfguJq9s1oNsj0W8ApwnX1ppP3gjDq4Ag5OwOjL5Yy71esEN61BPmXPa0EdXrR0TB3JnTeE2EBRHVnJDSw9S7UtDSefKdpM2ivnoB4DPhXn6kLFD4ebYsBPAqJd-TlEJuOmu_053KIBBKxJrcPFziqqHtZOvDcJJH47kgyrRF3fS70liKBQ6b3ytvI1ZhW-JYf5XEjLwoZdw4z8mLiPxi0FkdBF4r0_-9Mj7-ajl-SZJnw8eMt8l15LUttb59ruMiDTonkCGWaKIqKHV1s82IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: نظامات حاکم بر تنگۀ هرمز به شرایط قبل از جنگ بازنخواهد گشت
🔹
نایب‌رئیس مجلس: هر نقطه‌ای که مبداء تجاوز به کشور و خاک ما باشد، قطعاً هدف مشروع نیروهای مسلح ما خواهد بود و اقدام نابخردانه دولت اوکراین بی‌جواب نخواهد ماند.
🔹
به رئیس‌جمهور متوهم آمریکا هم توصیه می‌کنیم این پنبه را از گوش خود بیرون کند و تا قبل از اینکه شکستی سنگین‌تر از شکست قبلی را تجربه کند، منطقه‌ای که هزاران سال است محل زندگی ما و نیاکان ما بوده را ترک کند.
🔹
مردم آمریکا پیش از آنکه سربازان آمریکایی با تابوت به کشورشان بازگردند، رئیس‌جمهور سفاک خود را کنترل کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/452657" target="_blank">📅 14:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452656">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXHW0dN3gKLgqmolphpkoI-HF7aDp2RsZjVHx2pk7qpy-QvUEuaa3krSI_Cje-wbW6rZLqMo5vFxt5iDiBGJslBil2AiXWDZ5F5M-x_Y-u8PFNanmLZwEqvio6kCsq4SbkTQZdsgvq5tD2HdovwurHJaBb2yFxICBjzpKowkdTmFKc98Fd-bCAsrYbRiK2STNi8tnqpnkG_73Mw5dLntG7NucUw_R3x84ctzaoKnbfoDpcBks56pp7FKWo8OTd9HRzuOeubLQ-1tJhtBLX54L7_80bGmUCF7GLUyPR6yRPSNB3SeLMsmAPcoN4F9aZp1aIj1Yc4jYWXDvOQiA4rmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دست پیمانکار را از حقوق کارمندان شرکتی کوتاه کرد
🔹
رئیس سازمان اداری و استخدامی: دولت شیوۀ پرداخت حقوق کارکنان شرکتی را تغییر می‌دهد و از این پس حقوق، حق بیمه و مالیات این کارکنان به‌صورت مستقیم از سوی دستگاه‌های اجرایی پرداخت خواهد شد.
🔹
با اجرای این طرح، سود شرکت‌های پیمانکاری از حدود ۱۰ درصد به حداکثر ۳ درصد کاهش می‌یابد و نقش آن‌ها صرفاً به تأمین نیرو و مدیریت قرارداد محدود خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/452656" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452655">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6768242559.mp4?token=meyBhbb9WnY4ec8bj_x1yCLIICCx05Oz809OZ5tWXv1bF23Trkfyr-YR-R1Lx7jgjJd8yeIWmDfzPSzjIYr66C-woMrl9uDO3AWetsRRYpoEu3IFAkY6reRsXFD7B0cUiO0-Vtcs1wdrSfiGEsTQ0MdrSAMIrX_PbcAxQf-hww_THgw_8uUnTLJLvFndDweOTEJ7d7RLTuDrT-uwF-9vayah2-X3bQ2pCthSbW_H36OTXe8WspGk1RIitGpl8hwjIRKKG8aJXcCkoULoCvh_LFSGldPU0752zL44WwOkGGEtRHGVRodVtitFj7b4HifELsW92XozZSej1GD1lrrLH3ZZXJR0kkFalS6-kv_q5btnZBh6KLt-ftWDG3Y3Aj4yQqsA51bLzjyPJBXuUo75NjQJsVe9ZvE2OxMM4HPlflOEibgtm8BpXUQbp22MfgBzstcXV7W-DcH58ltJUyE6WgFEm7qpiISFwYRBNZdz7aMZacfzXPzQRHuxEiXhX0XbekpQuGWiHbyFOBQMmv2JxFsPlZyztzk1z_WfzkAccnhPPpjpjyJynJak8Tgc4ky7hUzYSjX7XHct15a6oL6eF5lnzuJVRH31Va4RmIGMbL2n0LQLaFt0cdjei6dgwLl4d2Bp5giOwX4Lt21HT_KEiXNQrak75pha0QpgO9FnZnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6768242559.mp4?token=meyBhbb9WnY4ec8bj_x1yCLIICCx05Oz809OZ5tWXv1bF23Trkfyr-YR-R1Lx7jgjJd8yeIWmDfzPSzjIYr66C-woMrl9uDO3AWetsRRYpoEu3IFAkY6reRsXFD7B0cUiO0-Vtcs1wdrSfiGEsTQ0MdrSAMIrX_PbcAxQf-hww_THgw_8uUnTLJLvFndDweOTEJ7d7RLTuDrT-uwF-9vayah2-X3bQ2pCthSbW_H36OTXe8WspGk1RIitGpl8hwjIRKKG8aJXcCkoULoCvh_LFSGldPU0752zL44WwOkGGEtRHGVRodVtitFj7b4HifELsW92XozZSej1GD1lrrLH3ZZXJR0kkFalS6-kv_q5btnZBh6KLt-ftWDG3Y3Aj4yQqsA51bLzjyPJBXuUo75NjQJsVe9ZvE2OxMM4HPlflOEibgtm8BpXUQbp22MfgBzstcXV7W-DcH58ltJUyE6WgFEm7qpiISFwYRBNZdz7aMZacfzXPzQRHuxEiXhX0XbekpQuGWiHbyFOBQMmv2JxFsPlZyztzk1z_WfzkAccnhPPpjpjyJynJak8Tgc4ky7hUzYSjX7XHct15a6oL6eF5lnzuJVRH31Va4RmIGMbL2n0LQLaFt0cdjei6dgwLl4d2Bp5giOwX4Lt21HT_KEiXNQrak75pha0QpgO9FnZnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌نوشتۀ ۴۰ سال پیش رهبر شهید
انقلاب
🔹
پس از گذشت قریب به ۴ دهه، دست‌نوشته‌ای از حضرت آیت‌الله شهید خامنه‌ای که در جریان بازدید تاریخی از بیمارستان صحرایی حضرت علی‌بن‌ابیطالب(ع) به یادگار نگاشته شده بود، برای نخستین‌بار منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/452655" target="_blank">📅 13:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452648">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aA_TKECl6ErXAsCEHGWbD5hZM1ZCQytnoLsdbiYu5wp2ZRkX4fSVJTSbMhIkY5xD48sxlOtC8Er6VQlNOyinH038lWPC1kcg7i6V56OhLSKRKECLsyTUZNXhh0SlkEZ3o9Qr11ZrfnJFtoMBmFIsbkrxaOKKYZ-v8BfK9L7gA4DbNqiZi4ut_3Mf3hMaYBl9ci83gC9Ef2dTloaOnSmKxvd5r3jwDASW0FTgMkCs55QkBGKHDvg8u9xlrWXgX0hvzfWXxYEfEitVe6r9_vKSBj6lNr-L6aNJe--5ueFpJpxCRhJZNJnBj-aJb3mgNxXMFXqzFaYx4vxUsKS63uS15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLNd2geuJ5AAihI26dRyOxWmxCLGgJTziV9hKrPlaMT9kEQdahsNoosSEnI-Xr9knA8jzD-_IhiguYa5LY0O7Eni5ED9tWXTR7ck64XNiTPnPwIjEEEdZXY5bHdDo_tivHkZhndlSSXCIXIEk_wmfyBqyOyCIo0jGEiRbmOPXK3v5m3MfMcLsZOl623NzNbYEnyAL7l1Vzoj0W_fjQ2SRUwow8PMjW6WYG93L5ktbwxG62C7N3RmwAFIB-Bpx-jpSpHRsyso4pc-pHGvM9lRY3wuQSL8o2fQrcskUNZdmBGi8gscoPaWMlcQeYdY5htmXJZsK5obs0x-dd59LNF5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uM-O5x4KqQajnaIqcYHHESOfzsPrp9oIL6aRxEIV0j-XwMlJ9Azk6K3Zd7fzvNH2DY6ivOawQ6QnbQK-e-jeOK79DwOQ1L44Io6CZ33p4GBspsVQdVRllQAbpv-534b3jaHjeDOUXqO4HcK4C4mJzpaT0PHUAWTpdsUHNY6jG8mHN2WEgdMPiMzZLHqQ4ooNk9Ml1tIe-6MLNu9fvIYqgkNHkNBQ8KtzZ_qtNbs4OUzjF_goZxtUeY9Q7_l00Q4SVzTXwpE9U4NTZq35cyz64rP2rcTR7J2JfZ4WZEjKYFR3AVQI5MNqGAyxkcQcYj7Mg_exqOZUt3ihiHW0ryXZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nhjcj5HGrGvValF8kzq200Af4Au_wmbe3JhlekWSnZXU-NFcmXtbDjm_GB-uJz_Qd5uIu5XEqjBYeC-1TRORjMfmqWmrKkLxGV_p_kjIIs17FRR7jMChmKhY5KjUbXkOnUpEmWP3c3k1TQGVtDu3ta8k0SS9XT5WgoFvVbihCdKi7rfQsq4TiJ8z4uMGBW5C_de21CRkZxdsYIuJ6ywJ8d9f6vKESnpOKgOdPFr0LzBjH1KL8Dgl0IZL4bEJ67NiOdu4Vy4oyl3tmFtC0_0TXpImM7ctiz6i3nliznDDt-ULMTAO8MzMmJX4EKM5z7X3wjDf29zFPTQXLhUmBoO7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovZSYBAq7SDBqBwcFHxBjBePJrgXmHC_8QdR7LpoyiTZP_gCkUtWkPXAJRdcJx_jz4fRN-7G7gsw_0c-P1Xp7nRO0s4IT2EvaS_WSdJkkUKvYwzSLkGnHGzMXDF5mr8Oi18ImQCaPUdC29jcVjOyiIutuGkAKyRhsn2Gso-6pLo50YMi1QEI_oq3JuhEx8urpw0eM0HnylE7-edd14VsAt1klrj3RtnKNfYFtmEwqva_4xKDqsn0SCoHXG1A2Ar3h-81JTqAQplsm5tldQPBzjYCVOCbRe5PI2LSO-aeYiMHy41GytH6_lmdKxHSYpcu76v9BPdEtB0WyYDquCGeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sveer2u4gtGaTuxLtzZ1lN_Sv0hQ5lVi1rN-x2PeTUlNuDoHx528mp7tfOshiWYiwDpL7KUZvg9TZco929Ms5mQ5Nz5JdzoVJWDLmH9VVahXnLKWlYpKgd6enj-idWcSZ9B1QApaZydlSwQZ8us78Al4HtW1ULlPGhrB6ez4C0nSkE3WOvV3wuvBanYyfcT8dx8kBlS5xcduuVcwuacmsamSZNqDjFVjztl9JVJW1NjhaZ1B1mnCObuxSlNyJxjQ9Bahtpq6H6vCCH-l1J8OGzDrVIVtbTTVbSu20qiUgGrqYZ5AIt9W8_p6PBhIr1UnUydBLQfktQyfl8_lmQhCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lotxqaCEhDuWi7IT5zr845eM9qJUHtLXywWUopiSsQTtzqKctoQWB4uh_S77SAVZlxvkklsILX76QzkpDjEJpuy2ArvbbwTF5SBjw0_7zQkqUuL-MzsTpKIyK38YPtO5yBEOlF-essfCSt8SfcePIPdAyUo1fOxEYXmMofTuM6r29ZR9_wY7rMFF7Q_EBKdrWiJeDynMlAYw30BAf1mNhj7ak5JwcpGeJvgU9kAHvVBs4CTzcz8XBhOLKhcigexfwK93ExlrdKvF2Wptl7bXNHGqsSrwjSUlsjO3mnT47CIt_uWuZYd4FrcxNBgFQ68mHZYUBS9zCunc1jrSYUB6Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تشییع پیکر عمواکبر سینمای ایران از مقابل تالار وحدت به‌سمت خانهٔ ابدی  @Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/452648" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452647">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMoMs6lVNgiaC7hFU8NDIXkxl7bGJeQkqasV_3YfUxt1uGQndotGkd1dtIyzOHImeRBkBoXmGC1tLk8oYKaB-9dET6ig8JmnnKYfOrT461ezhFnmBSKjhb8jIjA290CjHdBd3xJrW-Epmo3c3s_LX7HNHbPOOWKyVqrAEJ6_GX7F1kmGE2dDHH3mvQUI4P3WVlwbFdJzGoG7AkvOLqgvUx-BjdSo8OK9spi1rCHTdpopKK_YI2DY8_egeQcZCagk_MMKcIK-sRWVESmlMH3bpzicfW63PxFbKnK03asK5Al27HI6MGrydz7rWTkuG8_e8TzLRaczMLFqaownYBnpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی مجلس در مناطق مرزی جنوب کشور: جولانی بداند اگر بخواهد وارد درگیری با حزب‌الله لبنان شود، مسیر آزادسازی سوریه برای نیروهای مقاومت تسریع خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/452647" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452646">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd2k-xhgxm5pRF0x_i8brdmyDHFwsUBIKo82vXQJM5XARCC8sUVRxeR0pQEDmy5Gle39mWHmhFoQYlITLtWYo_9rOyLSm5DMEDmXQAITI4uJ251SYm0CEiZqx4NhL-QRRrZQBu48yLmQ2tRDD_h_Soz_MENvwT_WCCRCJr9GMxt0sbLpqwF7HpQ-PaiPY3iWTVEcmtHhWfdqQ94Q570KwenZhRDdCwYlobbjjJIbGOEmUC9062intsw3ATTg1ZSt5bIpRxVhT0XqEc1OD9R39tNLTkgr_osVdafLzt_yhcTqO3k_5UTYx3s1i5qd_l57bEl1fIIZRdViwA0au1ZJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروهای مسلح یمن: یک پهپاد ترکیه‌ای را سرنگون کردیم
🔹
سخنگوی نیروهای مسلح یمن: موفق به سرنگون‌کردن یک پهپاد شناسایی مسلح ساخت ترکیه به‌نام «بیرقدار آکینجی» متعلق به دشمن سعودی شدیم.
🔹
این هواپیما در حال انجام عملیات خصمانه در آسمان استان الجوف بود. این هواپیما با سلاح مناسب و با توفیق الهی سرنگون شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/452646" target="_blank">📅 13:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg7mFfIwCNyR3JZ2ZjqjMmDm9tH6ftR44XRSXssfz2hk7uRMzPPjB0epx1IaTusyVUpE6NoC7O4OgUPeQ1lsDgkMqFvv31YwGqEZo5PdZqElTuQqhMogcWtPYGC8vJfU6-lfQCwhhX-d7YIw4EqLG-FnLWPoVdlpblZPSuzROrBCr67i1N_CA5dTJxNZGeOvN3aKbBf2Y3fBkDijJj4UCAAuCPmVeFk3Lj3o9kIWQtSr9Jyg811j0WpLAzEENL-fOFEvewAreeQfN_P2nZhpHsBPkU1DjbDwkh4k6LkFoW1bNDgWQ8wjOqP1p3kvOE7o35RKDuZLuEBfvvkHbMrxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جنوب ایران چشم‌انتظار همدلی جامعه سلامت»
🥼
🩺
از کلیه کارکنان و فعالان حوزه سلامت دعوت می شود تا در پویش سراسری اعزام داوطلبانه جامعه سلامت به مناطق جنگ‌زده جنوب کشور همراه ما باشند.
ثبت نام از طریق لینک زیر
👇
🌐
https://survey.porsline.ir/s/VoIeBbe8
🏥
حضور شما می‌تواند مرهمی بر درد هم‌وطنانی باشد که در این روزهای سخت، چشم‌انتظار خدمت صادقانه فرزندان جامعه سلامت هستند.
📍
شما هم به این پویش ملی بپیوندید
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/452645" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxAv2S5i6sufsSB7s-qRNDkSJBOsBoXlmJZy5xZ1S8v7NA5KyKfkt7B_rguGO8Lu0UsCEDeHmyWzn9QgtUxwul7fxdt1vAfdHc51aTT3rRwlr4uJWM410hCbmNJS9wuvgeOdMlhO6_PWtNupm_GoNIE4DRiV-AwtPHOJQvKolVHvDuk_-oSnmadp5M16Kz4w-UFjRxZCrgFPvGQQ-4-n7BNNYCQMIRcWu_IZp4seBd2bDU1mjKKSqdEqsSDuBuCE5WA46ozdOn031wr15fnXjL-TCgoAou0EJ652e_lTK4KakcrOck0gzp3cTIf9tgoM2hN-eFAag_p_BI6jwQ8KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود شورای رقابت به قراردادهای مبهم خودروسازان
🔹
شورای رقابت خودروسازان را ملزم کرد در قراردادها و فراخوان‌های ثبت‌نام، تفاوت «پیش‌فروش» و «مشارکت در تولید» را شفاف اعلام کنند.
🔹
براساس بخشنامهٔ جدید، شرکت‌ها باید صراحتا بنویسند قراردادهای مشارکت در تولید مشمول مصوبۀ ۴۷۳ شورای رقابت نیستند.
مصوبه ۴۷۳ چیست؟
🔸
طبق این مصوبه اگر بخشی از قیمت خودرو هنگام ثبت‌نام پرداخت شده باشد، افزایش قیمت ناشی از تورم نباید به آن بخشِ پرداخت‌شده تعلق بگیرد و افزایش قیمت فقط برای مبلغ باقی‌مانده محاسبه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/452644" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5bda3f7.mp4?token=S2A3sf6RjcnScNQRbejdNNsaGQ1wa8plr94kNq-se7loxC9Sxz_th3CXi3_2QiZQ4trywS93suyjRfMQje0ZXBf5skd6X58TNHnx7gdeJ8T4N8frxD0MIdZ2iXmPe0ypltrGuri6QWIC8Ufr9a3V35q7vbU5sMZFvQ5TRBZrOt8CZT3KmYFjVeNF2zE6L_gI7_o9IfloQmCWTwT3lwgZBJLToUozF5dOzE0IilMtpUCavv_Zkkt1xgk38CBTvkIAQdV0NmlWEsW_3c2wj6ctxwxL5HNwR4qHIHSyV4X2i32FCy9raoahVm_kT1AQI68xwwqO8YAax_KgyAcxoXA2KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5bda3f7.mp4?token=S2A3sf6RjcnScNQRbejdNNsaGQ1wa8plr94kNq-se7loxC9Sxz_th3CXi3_2QiZQ4trywS93suyjRfMQje0ZXBf5skd6X58TNHnx7gdeJ8T4N8frxD0MIdZ2iXmPe0ypltrGuri6QWIC8Ufr9a3V35q7vbU5sMZFvQ5TRBZrOt8CZT3KmYFjVeNF2zE6L_gI7_o9IfloQmCWTwT3lwgZBJLToUozF5dOzE0IilMtpUCavv_Zkkt1xgk38CBTvkIAQdV0NmlWEsW_3c2wj6ctxwxL5HNwR4qHIHSyV4X2i32FCy9raoahVm_kT1AQI68xwwqO8YAax_KgyAcxoXA2KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای در قم با آیت‌الله سبحانی دیدار و گفت‌وگو کرد
🔹
رئیس قوه‌قضائیه در این دیدار دربارهٔ مسائل منجر به انباشت پرونده‌های قضایی گفت: نیازمند کمک‌ها و ابتکارات حقوقی و فقهی حوزه‌علمیه در موضوع تأخیر تأدیه‌ها و خسارت‌های ناشی از دیرکرد انجام تعهدات هستیم…</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/452643" target="_blank">📅 13:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfOphL-YQDR03yQzUgNbzel--u__AMhwy-bIlyGS_ImB3hfGWlhwYwToNoXfv3G3b9uatWc6CMnv00euhBqVEuISQqhYmYh8t5va27qaq58CUz4BjtNMceALLattUrofP0Vp4GL-l39xJvdv0DO0TyJKuEuJP79DkidsXSPUN_44TtDLJRktN-LfNyd3ZtjgP53JxJydEKtzW2gEaRjeTE_-rZPl5xc3D9lH5ysljtTey87GUcjie0eNcgRZlQP1KjYR82V75_lhl8RusQ5OKlJkuhmvJKe-RafsEcrwwcVmKHnNYu-GtGV0MdB9ectAYqj0OWGzVRYIi5kAbBoG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه من، همراه زائران اربعین با مجموعه‌ای از خدمات دیجیتال
🔹
همراه اول همزمان با ارائه بسته‌های ویژه رومینگ اربعین، مجموعه‌ای از خدمات دیجیتال موردنیاز زائران را نیز در اپلیکیشن «همراه من» ارائه کرد.
🔹
ارائه خدماتی همچون خرید ارز ویژه اربعین، استعلام وضعیت گذرنامه، استعلام و پرداخت خلافی خودرو، استعلام وضعیت گواهینامه، پرداخت عوارض آزادراهی، خرید انواع بیمه، خرید بلیت هواپیما و رزرو اقامتگاه بخشی از مجموعه سرویس‌های دیجیتال در نظر گرفته شده برای متقاضیان است.
🔹
متقاضیان سفر اربعین می‌توانند از امروز و همزمان با شروع سفرها، با مراجعه به اپلیکیشن «
همراه من
» و ورود به بخش خدمات اربعین، از خدمات دیجیتال ویژه طراحی شده توسط همراه اول بهره‌مند شوند.
http://mci.ir/-S36MND
@mcinews</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/452642" target="_blank">📅 13:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=Dzn7R0hc1Et_ejcSUmkJdgBu1_gdFv2EehIclIXlkk7tsptz1ougZGQHlEBAJcrhExo3f-vDA-VvY-CYbpWabpEB_l4zTomGn-TH41-H1y4AkFQEbaN5EQ0TnU8kTpcx2eR6WjOGzOEOzbd80DKzW58JjqR5w93Ognd3b5_7j_T_XHMytTARnv4FBNr7QBtdGjsdSXD9sBrQNt4qA6VxhEr-50fiPlpSLEo51ym_BICueEZyysowpDAXqRbejHh2qdHUXajeTqjbAL3DwVcsdHxJ55mzzZb0kwkPWL41DCI9FoO_9XwBE00Icb5Fn6PFCqZByomo0h9RF8uMyt563Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=Dzn7R0hc1Et_ejcSUmkJdgBu1_gdFv2EehIclIXlkk7tsptz1ougZGQHlEBAJcrhExo3f-vDA-VvY-CYbpWabpEB_l4zTomGn-TH41-H1y4AkFQEbaN5EQ0TnU8kTpcx2eR6WjOGzOEOzbd80DKzW58JjqR5w93Ognd3b5_7j_T_XHMytTARnv4FBNr7QBtdGjsdSXD9sBrQNt4qA6VxhEr-50fiPlpSLEo51ym_BICueEZyysowpDAXqRbejHh2qdHUXajeTqjbAL3DwVcsdHxJ55mzzZb0kwkPWL41DCI9FoO_9XwBE00Icb5Fn6PFCqZByomo0h9RF8uMyt563Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
💎
تسهیلات
طرح کارنو بانک تجارت
ابزاری ویژه برای حمایت از کارکنان شرکت‌ها
🎯
سبدی از خدمات متنوع اعتباری برای نیازهای گوناگون
🔗
تا سقف ۲ میلیارد و ۴۵۰ میلیون تومان تأمین مالی
📌
📞
برای اطلاعات بیشتر به شعب بانک تجارت مراجعه کرده و یا با مرکز ارتباط مشتریان این بانک به شماره ۱۵۵۴ تماس بگیرید.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/452641" target="_blank">📅 13:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/452640" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQuRQ47MTq0pgoFr141AFDy5D4fSw8eEFfBLexkZP-PBIPG1ixWqyn7FzyQgDyXtJN8JU0jY0le9nyFNI9iolbaFku0zjZo9uN4a13VK0qojqsCQ4BBoh97bpPVGy25mmQvplt4-GR3uz3FPrnbi1P4W6J3PH06djSPHeSBDuWeAQgmxM95JKS_QwJCR-3eWiv-NUSyBUF3QlaUk4AcEQq2n2BbWQbAX5dgHUz5ZofH2WXIWdg8v9RFUeZ2Q4rbvhWLWQRKFoVw0Nl6xBd4Cs4lUV-XIvz0ScXiAlV0Lsn52zvG_HYKWJ-4OZfoGc9AYwmmDQq9aHA4CbNyVdc6Jdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به ۵ میلیون برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۸ هزار واحدی به ۵ میلیون و ۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/452639" target="_blank">📅 12:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b23046f2.mp4?token=R3PomfF2hlgFyaOIZT7GnWvmKLM9PvtbKA-2msUqqkegMV82lNh3u-UIA7bwjXmT2ZbMh8F_73957y_Py5-K3ii_RvWIn9J5PV-dkw8IgmwPmEUr3-AXEIBAt4hfCpKTu6VIIYCRL3-sqFv-uaHe548dhgCFHiX1ohcXszGXn01HysFtgyWU0uHjgyLwAGKDlFl9DZaK2r36waq3EdwIjj1AviMlIRUVIN07LUu3ccqdJU3K0VQnHYCTTbFrfXXTlNlwyuBkTcrkkX00gCtP9BZXKHB_5fFgXjTsoYm3OWdjjz-DNBr88m_Kjr4BhrzBO7DZWf5gMbsWuhEFgFB2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b23046f2.mp4?token=R3PomfF2hlgFyaOIZT7GnWvmKLM9PvtbKA-2msUqqkegMV82lNh3u-UIA7bwjXmT2ZbMh8F_73957y_Py5-K3ii_RvWIn9J5PV-dkw8IgmwPmEUr3-AXEIBAt4hfCpKTu6VIIYCRL3-sqFv-uaHe548dhgCFHiX1ohcXszGXn01HysFtgyWU0uHjgyLwAGKDlFl9DZaK2r36waq3EdwIjj1AviMlIRUVIN07LUu3ccqdJU3K0VQnHYCTTbFrfXXTlNlwyuBkTcrkkX00gCtP9BZXKHB_5fFgXjTsoYm3OWdjjz-DNBr88m_Kjr4BhrzBO7DZWf5gMbsWuhEFgFB2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعهٔ الموت جهانی شد
🔹
مدیرکل ثبت آثار طبیعی وزارت میراث‌فرهنگی: استحکامات نظامی ۷ قلعهٔ الموت در قزوین که بیش‌از ۱۱۰۰ سال قدمت دارد، امروز با رأی مثبت داوران یونسکو ثبت جهانی شد.  این پرونده شامل مکان‌های زیر بود:
🔹
قلعهٔ الموت، مرکز فرمانروایی نزاریان
🔹
لمسر،…</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/452638" target="_blank">📅 12:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452637">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf00e58bb.mp4?token=AzRnv7WT7JFDmWfrs5LDCey6iMgtZLQxNZmC4lALnoLbYptV3yiuPxOqe1dKzQUPyrFUR-gXN9hT68SDcp5ikaqxKuR7vocIeFGEN0_ZnWZmwdo1S6QQUx3pnB1s0YdCdQM939PcAEcVe_A4liy3JYjkQrXI8GEBX-rJ4fR8jhohWrAnjrm4fEIoj0fAhIOi0RnlGqpU0tnRu7gE7MB6_U63jcHT-Gqqqi1AagBeq0A9R4B-gMwgmTEMxRCaq6FBtlXQjA6D9iGvDa_rCF_Q0kzT2LZwrgBXnTOv7cplcmdaTsjy0bet18XyjOH8MPWpXvF2k8HbPSmT0j6w40f0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf00e58bb.mp4?token=AzRnv7WT7JFDmWfrs5LDCey6iMgtZLQxNZmC4lALnoLbYptV3yiuPxOqe1dKzQUPyrFUR-gXN9hT68SDcp5ikaqxKuR7vocIeFGEN0_ZnWZmwdo1S6QQUx3pnB1s0YdCdQM939PcAEcVe_A4liy3JYjkQrXI8GEBX-rJ4fR8jhohWrAnjrm4fEIoj0fAhIOi0RnlGqpU0tnRu7gE7MB6_U63jcHT-Gqqqi1AagBeq0A9R4B-gMwgmTEMxRCaq6FBtlXQjA6D9iGvDa_rCF_Q0kzT2LZwrgBXnTOv7cplcmdaTsjy0bet18XyjOH8MPWpXvF2k8HbPSmT0j6w40f0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراکم بالای خودروها در پارکینگ مرز شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/452637" target="_blank">📅 12:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452636">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ماجرای نامهٔ شبانهٔ وزیر کار دربارهٔ تأمین اجتماعی چه بود؟
🔹
انتشار نامه‌ای از وزیر کار به وزارت اقتصاد از لایحهٔ «ایجاد نظام جدید تأمین اجتماعی» پرده برداشت که ابعاد آن، نگرانی‌های عمیقی را در جامعهٔ کارگری و بازنشستگان ایجاد کرده؛ به‌ویژه آنکه این لایحه…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452636" target="_blank">📅 11:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcg-3zpEYCFDwDBao8UHi3dHQYunw_lQWtX7xABwNI8uJVBhkZa1vjgx0LO12_BvoK5TXBVan1hmBPYqzyKJQk7B3LPQEITHkhenzSAyWJXhHxGK_5gUhXuOGebKIVKBKganGv5tzE4lQ-F2ArkEhxM172kfg3xwxXtpc2rOya4nL9BWVucDGiMInJgaLEPFvnKcPU9G0MUlh0GGq4y2gG2bf0sf0q_KyUhkM694UL0bih_vpcY1dGChiZzjNcihXZf6vEs16l-I1j3VB0a1JEQuoW-3QVUZwBfMybL2PuIv5w7SxRQl82uaOTjVsF_mk7Da8fOIxLld7u-TbQBGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکی ایران بعد از ۵۰ سال مدال گرفت
🔹
تیم ملی هاکی ۵ نفرۀ پسران زیر ۱۸ سال، در  رده‌بندی قهرمانی آسیا با شکست بنگلادش موفق شد نخستین مدال برنز تاریخ ایران در تاریخ ۵۴ سالۀ فدراسیون را به ارمغان آورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452635" target="_blank">📅 11:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452634">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plAoq7eXIDboCZ67CQSQ7DPDrHFDJaK0e3ZCX_yrcXPtaKMUnnQKqi2aXQDhOMtL6eGMk_iHng7521AXw9hr9tur-I5_pW6Se0WuiTtZRlTMqGCG5_lAjQVgA93UZJ-dWyAFQ7qc22UCflBgPzN-DyDouLmiXIBh1b3Tm6ikRW1UiGGmG3Qe5-zCS-_kUl0-7itY-MeEEM58grYKif4JDyQS-bQjB3A0-fdPynh4N1DPCGH7c7u5MPC0VFXgKsOgkcZsJSU1yHF8jAtTce9fiNFew45VTRq9p6t6OJbEZVjN9F13OWuoLEHs2XGMVMLPqvfm4dqmKnMtAbHz712SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهداری کرمانشاه: از ابتدای محرم تاکنون ۱۷۴ هزار زائر از مرز خسروی تردد داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/452634" target="_blank">📅 11:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTy9pWzz_aZ2mOrTsHMA0QfKwVAC7jExBFe_LkAiqvGRo5sfDh5L9sTzcRE_HGMPmlfDXvbe3ZttmaX8JIGBIQxoCLv8wi7a_ZUKGV_BNTz2FipTDsfsbOLNczd3jmfcftQoQ5JYHzddS_r5aioM0gSIp6cSYmfEKscGMGpF1HfZFy24XUR7poRhi6nnvhl2i51HDTecbS-rwu2xNRbAdMsd3xV6lz4bm2PgbTkLb1-JHmbv1VMH85hcjwQwRPUXkL3CP6FXUd8_d9aKa6Wexp6hFdMWtFu6zq87vvYhG-oUN9-Vp_Avww_xFcYCj2TmxR8FAAu-scUYAgH1iCK2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعهٔ الموت جهانی شد
🔹
مدیرکل ثبت آثار طبیعی وزارت میراث‌فرهنگی: استحکامات نظامی ۷ قلعهٔ الموت در قزوین که بیش‌از ۱۱۰۰ سال قدمت دارد، امروز با رأی مثبت داوران یونسکو ثبت جهانی شد.
این پرونده شامل مکان‌های زیر بود:
🔹
قلعهٔ الموت، مرکز فرمانروایی نزاریان
🔹
لمسر، بزرگ‌ترین قلعهٔ و اقامتگاه زمستانی نایب‌الحکومه
🔹
نویذرشاه، آخرین سنگر مقاومت در برابر مغولان
🔹
قلعه‌های شمس‌کلایه، شیرکوه، ایلان و قسطین‌ لار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452633" target="_blank">📅 11:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارهای کنترل‌شده در بندرعباس و قشم
🔹
استانداری هرمزگان: درپی خنثی‌سازی مهمات عمل‌نکردهٔ حملات اخیر، احتمال شنیدن صدای انفجار در بندرعباس و قشم وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/452632" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7gNc8CypRIh3tVf_YRCiILoAhlEwJSULbVtjpYduM_3MJcZ8YuvLaYaRU3W8Lcv02wIxKfM3LH9EEBjCfnHxtuRv32-E158bD-aALzz7_1inKJjK9H2kKzD1EcB4lsBfoELjmcq3SimcL4aZoLwmqCeIF3rC8HjbOq-7QJmn5yFz60RH3Ci2wb6cvQK62T3_e4sESDZuIUtBOHP4rUby9uNQt9u7pU_vmWZDRFqBeHzfIKfuslzl5CAaefJN4k-l4t-UgsxbavMPdedGTnHn7qOINCvWQkVDu0IVEvx7ofTibkEtYk49Qz4EICHE4f4WRMQQ8Am5jo8DBLpeSkUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
درکنار ۱۱۰ شعبه‌ منتخب در سراسر کشور
⭐️
بانک شهر ارز اربعین زائران را در مرزهای مهران، شلمچه و ترمینال سلام فرودگاه امام‌خمینی(ره) تأمین می‌کند
🔻
همزمان با آغاز سفرهای اربعین حسینی، بانک شهر با استقرار گیشه‌های خدمات بانکی در مرزهای مهران، شلمچه و ترمینال سلام فرودگاه بین‌المللی امام خمینی (ره)، ارائه خدمات ارزی و بانکی به زائران را آغاز کرده است.
🔺
به گزارش روابط عمومی بانک شهر، بانک شهر در راستای تسهیل فرآیند دریافت ارز اربعین و ارائه خدمات مورد نیاز زائران، گیشه‌های ویژه خود را در مرزهای مهران و شلمچه و همچنین ترمینال سلام فرودگاه بین‌المللی امام خمینی (ره) راه‌اندازی کرده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/452631" target="_blank">📅 11:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21a433f13e.mp4?token=LVC0NJUki8lTdsRmGKMLRtJAAcnveJY3mfHDB_UDlrpmJz8WnTUgChe8z59goFKLbN9ofauSEX3PMaA2wRbtL_Bw40UmvA4ckNo2-M58NWZ-z1ofG71ThxwNUP48TuvoLGcogpf7TtIFeY4lGQGPu_6qQaTFn-RCEnfi45OUhIa6kQZ2CZDqWbxfxoYb6nHC6NWJvB1b_vrgq8jYnDKJlp6dZ2h-Ex4ObwtJtuI1XhbC1rE_Ai1CUiVKYeuGBhwr7nf-Ln-Fd2sc5J6128P378vyOihjsQsfjL3LlKhsDAFMd29Nihc8Ekkk0o8mRsb7XcJd4QReIgct7TPQVF0tuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21a433f13e.mp4?token=LVC0NJUki8lTdsRmGKMLRtJAAcnveJY3mfHDB_UDlrpmJz8WnTUgChe8z59goFKLbN9ofauSEX3PMaA2wRbtL_Bw40UmvA4ckNo2-M58NWZ-z1ofG71ThxwNUP48TuvoLGcogpf7TtIFeY4lGQGPu_6qQaTFn-RCEnfi45OUhIa6kQZ2CZDqWbxfxoYb6nHC6NWJvB1b_vrgq8jYnDKJlp6dZ2h-Ex4ObwtJtuI1XhbC1rE_Ai1CUiVKYeuGBhwr7nf-Ln-Fd2sc5J6128P378vyOihjsQsfjL3LlKhsDAFMd29Nihc8Ekkk0o8mRsb7XcJd4QReIgct7TPQVF0tuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
خرید اقساطی کالا و خدمات، حالا ساده‌تر و سریع‌تر از همیشه!
💳
با کارت رفاهی متصل به اوراق گام بانک رفاه، اگر واجد شرایط باشید می‌توانید تا ۵۰۰ میلیون تومان اعتبار خرید دریافت کنید و به‌صورت اقساطی، کالا و خدمات موردنیازتان را تهیه کنید.
📱
فقط کافی است نئوبانک فرا رفاه را نصب کنید و درخواست کارت رفاهی خود را به‌صورت آنلاین ثبت کنید.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/452630" target="_blank">📅 11:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/452629" target="_blank">📅 11:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb5HwjpcFipgpRvAID5KQn-KWjoOLL7eRN0hTuilAdvlxEjNJ-KS2G-JMWNsR5qFRvhOovrdw6f242DcBVItjkAiXhXtFgeRcFw8kGBCFt4vnWcWaQy440sPj1OcUXAhXFcCY-ZEgGD0UGRuAxxYlPbImlT7c5m_B8MLHS8yLZERMUPybuDsmwHciiZJQKsp1LKnh5WUWUboWAZCCqFBcaWTzFN3-RS18dfJMHHnq1DRC7_T8_8jvTbcFIIJl25untyrBk7V7GOEpV0EnjsKer6HKFEjkrgBZ9MOaRTICs1VsAglfhjhet_csBZPzyrlLCBLYozwJDwR-ajd_9QrlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زائران اربعین گردوغبار را این‌طور از بدن خارج کنند
🔹
اعتمادی، کارشناس هلال‌احمر: زائران با حل‌کردن یک قاشق مرباخوری نمک در یک لیتر آب، یک محلول آب‌نمک رقیق تهیه کنند و با آن غرغره کنند یا از راه سوراخ‌های بینی وارد کرده و از دهان خارج کنند تا میزان زیادی از گرد و غبار و آلاینده‌ها شسته شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/452628" target="_blank">📅 11:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/452627" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a30fb503.mp4?token=vFUzlFT9po4aPY5M6-XRTl9CDst1Ez_q3shodGBqd5jo3bJv_woBhD7pd4Lfpw7YTSeodSgVE-jQ8L0grnONnbKVsfTbx8d4zyqQLIqmfq2PldMWKl2lbZF5utJbR3EZxfyTytiSa9K1Raq6lW_uyB5rn5qShZ2m2Iy4p8R3A3McQSyfu-BC6tQkvflh1exxMqz78azk9F_Wwh6ZxLDGHM_mGL8DTdng7fQRo8qsfmTghMzEg_3rVA7bLJfhlmYrXjkuD-Zu4gcuFpkIs4TzyxXTcBzKd9OOVfOBgg4TofDnBj2PPn8tPMCBqgfs92s9DDfWvjHkqNNl9X-Phb8e6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a30fb503.mp4?token=vFUzlFT9po4aPY5M6-XRTl9CDst1Ez_q3shodGBqd5jo3bJv_woBhD7pd4Lfpw7YTSeodSgVE-jQ8L0grnONnbKVsfTbx8d4zyqQLIqmfq2PldMWKl2lbZF5utJbR3EZxfyTytiSa9K1Raq6lW_uyB5rn5qShZ2m2Iy4p8R3A3McQSyfu-BC6tQkvflh1exxMqz78azk9F_Wwh6ZxLDGHM_mGL8DTdng7fQRo8qsfmTghMzEg_3rVA7bLJfhlmYrXjkuD-Zu4gcuFpkIs4TzyxXTcBzKd9OOVfOBgg4TofDnBj2PPn8tPMCBqgfs92s9DDfWvjHkqNNl9X-Phb8e6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت کودکان لامردی از بمب‌ بارانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452626" target="_blank">📅 10:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌‌نکرده در پاکدشت
🔹
فرماندار پاکدشت: درپی خنثی‌سازی مهمات عمل‌نکرده تا ساعت ۱۲ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/452625" target="_blank">📅 10:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366f1680c2.mp4?token=hi36CEPr8sL1Kgni9jxCp1qG2QRbTsbVZB6uvUmHzGmNWmH-f5mcflUY1zDJxF9AUCjNCJABbEbtXs0KShUkce50e-8a2LXAcf_Aicp2Mwr0HvFk2cRJdhFLBMfQRRzhlHeomznXjhMlLM7ZZMOGiSHax3yiY4C4njktkXK-zrQAUguCfIV5xvxfqSDf6U2HznVSIhgwL0CJc3YRHTlB-eD1XMkwNQHtoRO1hT-yeAvSqNX9T0RS2jKZC7GTm3YjEMAROLGtC_3trZk1dREqtTn3obA-mUOPFw76AevLjOrQRY0pmqXLzJxyN1pJadeRLBkEABOH8ulzx7DLiUBz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366f1680c2.mp4?token=hi36CEPr8sL1Kgni9jxCp1qG2QRbTsbVZB6uvUmHzGmNWmH-f5mcflUY1zDJxF9AUCjNCJABbEbtXs0KShUkce50e-8a2LXAcf_Aicp2Mwr0HvFk2cRJdhFLBMfQRRzhlHeomznXjhMlLM7ZZMOGiSHax3yiY4C4njktkXK-zrQAUguCfIV5xvxfqSDf6U2HznVSIhgwL0CJc3YRHTlB-eD1XMkwNQHtoRO1hT-yeAvSqNX9T0RS2jKZC7GTm3YjEMAROLGtC_3trZk1dREqtTn3obA-mUOPFw76AevLjOrQRY0pmqXLzJxyN1pJadeRLBkEABOH8ulzx7DLiUBz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: آمریکا آمار واقعی کشته‌هایش را اعلام نمی‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452624" target="_blank">📅 10:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osEm8G7TFkwFdpBs_yBM9ZSds4qp4xrQYSRPTYLQbDjaw4pTTPcua4sm8Ml8WN9NAZyuM4doMf6ITEF7bo4VXs6iBO52OIeKlKGeicKTBVJjs6t3rVK74It3a4JzFvC7t4ps3F71UlpV4Ye_Wol6Crjdul4SL8U9cByr1cfxgGaEyoXZZhkZF2wNuBP_Qc-Yy2Escff4itFEFdqZL_xqyP1xbRabDHdLOX6Irk7XkJrXWyYWeW8p62XECQ9a57cc_J1_OmwBLJ8e9GVpAq7zwivwur4zfDF7sPO_IFHlV4d0_cXYXpxae8PiejzdXCL6mwkRB06JI4zczj9MO97HrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسهٔ کابینهٔ نتانیاهو به زیرزمین منتقل شد
🔹
رسانه‌های صهیونیستی گزارش کردند نشست کابینهٔ این رژیم که قرار است امروز برگزار شود، به دستور مقام‌های امنیتی به «یک محل امن زیرزمینی» منتقل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/452623" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_G0dnyBsrhiiXZKajXH510_gOKG5eTwXWXBMhuWkYt2nWlUvqJaFrNMqWXnk-H9rXmgcgIJhznZCcCjrdGY1D9LCsOfFHE7qCdUa0m1-x6sNu4ppNC1crhsHQvFpym-UX2lIJWtoNfEEXXMnRJlagD1E8CnCRTnECr5d2cht15iacKt0RX9OUeE9n6389m7cSN-Xiefmzz82IvlpEWRvP-ljTcNMgNtv1P-lmrbYf8kaTwpZGoTLXeIHN7oG9qEtPHps8EjtvdKDq09Lvg9fObleuYhFFT9-Mb-N-gxqb2cWHcZkJVmbpH5VTNfVEek1KX1NWhzEMF_ArP0gr7fug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پُر ایران برای گرفتن سهم محیط‌زیست از تنگهٔ هرمز
🔹
سازمان حفاظت محیط‌زیست اعلام کرد با توجه به عبور سالانه بیش‌از ۵۰ هزار کشتی و نفتکش از تنگهٔ هرمز و نقش آن‌ها در آلودگی خلیج فارس، نظام‌نامه‌ای برای اخذ هزینهٔ خدمات و خسارات محیط‌زیستی تدوین و برای تصویب به دولت ارسال شده است.
🔹
براساس این طرح و با استناد به کنوانسیون حقوق دریاها، در صورت نقض اصل «عبور بی‌ضرر» و ایجاد تهدید برای محیط‌زیست، ایران می‌تواند متناسب با نوع کشتی، میزان بار، سوابق دریانوردی و سابقهٔ آلودگی زیست‌محیطی از شناورهای عبوری عوارض دریافت کند.
🔹
به‌گفتهٔ مسئولان، خلیج فارس به‌دلیل نیمه‌بسته‌بودن، توان خودپالایی پایینی دارد و تعویض کامل آب آن ۳ تا ۵ سال زمان می‌برد؛ ازاین‌رو آلودگی ناشی از تردد گستردهٔ شناورها، فعالیت‌های نفتی و حوادث دریایی، تهدیدی جدی برای این اکوسیستم به‌شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/452622" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اداره‌های مازندران فردا هم تعطیل شد
🔹
استانداری مازندران: تمامی اداره‌ای دولتی، نهادهای عمومی غیردولتی و مراکز آموزشی به‌استثنای مراکز امدادی و دستگاه‌های خدمات‌رسان، فردا به‌دلیل تداوم موج گرما و ضرورت مدیریت مصرف انرژی تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/452621" target="_blank">📅 10:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c464d4aa.mp4?token=uSEC2wxaPHKzOLab-MQgt_TD3CGqZZu0NQWCQrMgvoaIqXgauuhl3iKVujbsGAGHgXAyLPwVF4Q1G8NfcSU8Z4Co9JuSF5WyiyszgvULr1LsZT2RyKnwAuyRjSLvK-pNy8FVdU-hYkhyOS6zcGm8QlbMAiB--HKVQjy2OZM3mWCONzDCbNu4nt4-Mgk2jggrILa8_yunKBJHevkNdmcRjDwAy-5LLL3e3aaCOzwAJASk6kwjMl-RuCd7xkypHxctme2wjM7nqSdvXXqJgGDHG1njU353HxtHShXnVbLeWBYRaJ6S-8aACGfNlj6Wz3-Du0GxmIpWRf1omIuuVdG9qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c464d4aa.mp4?token=uSEC2wxaPHKzOLab-MQgt_TD3CGqZZu0NQWCQrMgvoaIqXgauuhl3iKVujbsGAGHgXAyLPwVF4Q1G8NfcSU8Z4Co9JuSF5WyiyszgvULr1LsZT2RyKnwAuyRjSLvK-pNy8FVdU-hYkhyOS6zcGm8QlbMAiB--HKVQjy2OZM3mWCONzDCbNu4nt4-Mgk2jggrILa8_yunKBJHevkNdmcRjDwAy-5LLL3e3aaCOzwAJASk6kwjMl-RuCd7xkypHxctme2wjM7nqSdvXXqJgGDHG1njU353HxtHShXnVbLeWBYRaJ6S-8aACGfNlj6Wz3-Du0GxmIpWRf1omIuuVdG9qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز میت بر پیکر اکبر عبدی  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452620" target="_blank">📅 10:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25eda9b8f.mp4?token=ZMSOIjdog7qE-tht_A8bzqO0KBjjxGIpNKFrsvZqbX3RT4B8KmxZFD7EZEFMcWC4YPwK6bWqIQjyeyESIh0i6NSLYQTm3ZpqkjRe405RaCn_sPhEF21WWYq1zZSJzXKIK_OoTisPczLUs1BRbaccRDHLDVZ-X7J4zUbHx8u6UwjNWaYCnALSqds7zcbXYPurxE4TH_xeyBOj4mo6_SY1kn6cVtgkNt6MjdcV2sWizBs0C0d1x-8OqYdVhyp3ERDZHdducIlgdne61NmvNFcdmD3BH_9cB1g4xSkYvgY5oIbdx38j1XXIM8aYqfMFpQXv4O9DWbAtWN_XIuiR0lxeNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25eda9b8f.mp4?token=ZMSOIjdog7qE-tht_A8bzqO0KBjjxGIpNKFrsvZqbX3RT4B8KmxZFD7EZEFMcWC4YPwK6bWqIQjyeyESIh0i6NSLYQTm3ZpqkjRe405RaCn_sPhEF21WWYq1zZSJzXKIK_OoTisPczLUs1BRbaccRDHLDVZ-X7J4zUbHx8u6UwjNWaYCnALSqds7zcbXYPurxE4TH_xeyBOj4mo6_SY1kn6cVtgkNt6MjdcV2sWizBs0C0d1x-8OqYdVhyp3ERDZHdducIlgdne61NmvNFcdmD3BH_9cB1g4xSkYvgY5oIbdx38j1XXIM8aYqfMFpQXv4O9DWbAtWN_XIuiR0lxeNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ده‌نمکی: اکبر عبدی حتی در بیمارستان هم پیگیر اخراجی‌های ۴ بود؛ اما نشد و داغش را به‌دل ما گذاشت
🔹
عمواکبر بدون دوربین برای زندانی‌ها برنامه اجرا می‌کرد و پای درددل آن‌ها می‌نشست؛ او حتی اعدامی‌ها را به خنده وا می‌داشت. @Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/452619" target="_blank">📅 10:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7084eee8df.mp4?token=Q2wCq7jovbux-mTT10XDinG7uPJI3nFJ_js5QmyUpPp47vnD5mwOSK22o6dhwwLMV9OswApCaLmSGeXLYsn-D5SdjYsazyFa37AnWtkBE1Yv0bTwtpxCp1sTX8X3X9KUdaeY3JLQh4NiKIoAabDoONmMnexKwBczheLj3_3VX4rIaIs-pE3gjmWLQo8ESFTg8u3dXr-cD4b6iJK3lrr2axwi8a8koHJtTGbWQsQIbOAi5nhrapZGMXCs0zQrEy-nXkj_IDMT9FsT_ieFvBFcss4KF762HIyVQWVcKD4RlR0K36rR5zoKUBzxrIPP2OmispO-rSU0wRdCG28XYcalOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7084eee8df.mp4?token=Q2wCq7jovbux-mTT10XDinG7uPJI3nFJ_js5QmyUpPp47vnD5mwOSK22o6dhwwLMV9OswApCaLmSGeXLYsn-D5SdjYsazyFa37AnWtkBE1Yv0bTwtpxCp1sTX8X3X9KUdaeY3JLQh4NiKIoAabDoONmMnexKwBczheLj3_3VX4rIaIs-pE3gjmWLQo8ESFTg8u3dXr-cD4b6iJK3lrr2axwi8a8koHJtTGbWQsQIbOAi5nhrapZGMXCs0zQrEy-nXkj_IDMT9FsT_ieFvBFcss4KF762HIyVQWVcKD4RlR0K36rR5zoKUBzxrIPP2OmispO-rSU0wRdCG28XYcalOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جعفری‌جوزانی: وجود اکبر عبدی عبوس‌ترین انسان‌ها را به خنده وا می‌داشت.  @Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/452618" target="_blank">📅 10:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13abc8fc1e.mp4?token=So1mWNKg776Smg2CSvV5CuK3bvPxcJGxBRl8dD-BciK7O8F_so7CTmKdyvC6n4yAm_Q-PJjFhBrngKVP_VZreDyLAsBH33hgwedgsW-eH3y0BaHmmKCw-9wa0rqrTQLm62ottDLuEKd3xzgkkt7SIbTEAG36rQhnhU8KCgifUJP60HUIwZJO5XWdvUBouo8gddPFf3bosVUhm4jWVLopqb8Qv1yc7bV3rXkZ0RW4ode5HaGTKRO9fJewgOygyw5SEg_tIfTEysfMmcwhjFLlDEZ1F2g11XAw3Q3I512vF3JhMJEx8eQaeae8hPl-Gn8cvls0d9uvz1ZjMFH0tPicIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13abc8fc1e.mp4?token=So1mWNKg776Smg2CSvV5CuK3bvPxcJGxBRl8dD-BciK7O8F_so7CTmKdyvC6n4yAm_Q-PJjFhBrngKVP_VZreDyLAsBH33hgwedgsW-eH3y0BaHmmKCw-9wa0rqrTQLm62ottDLuEKd3xzgkkt7SIbTEAG36rQhnhU8KCgifUJP60HUIwZJO5XWdvUBouo8gddPFf3bosVUhm4jWVLopqb8Qv1yc7bV3rXkZ0RW4ode5HaGTKRO9fJewgOygyw5SEg_tIfTEysfMmcwhjFLlDEZ1F2g11XAw3Q3I512vF3JhMJEx8eQaeae8hPl-Gn8cvls0d9uvz1ZjMFH0tPicIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا خمسه: اکبر عبدی یک جواهر خلاق، بی‌نظیر و تکرارنشدنی بود؛ اما کسی نمی‌داند که پشت این چهرهٔ خلاق، چه انسان بزرگی بود.  @Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/452617" target="_blank">📅 10:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b1745dde.mp4?token=rwcTFi9A7pyVzbgGrRsh6dMIDCHVm3YzhxzZNPut2zQcXYhfxjRPRheVyq-0iMImuRqXcGrKVsaB6mP811QX49u0-RcZ671JTLMW8aQqGgvtRBziRUYG9tC87SyRLvCmqP5ZzN1U7tFpWqEYqCXRotQn1LmB9-Z8yc_o-3qn8GLXIeQ3xHbdUna2KFqjqGPeQUQQ7ZT9SSURDmtfN9Xkrvx3zvxvuUZx0K-u-pWHMjF8rulEhxbbPdzBgyo7R6bz7OcJlqNxRc1Yq5yFMR5ixOCFUm2t7pGZnnFtg10wltoTTZbAwNpUzkNrFtXcBFoylZFfFXCx9VoAkFncxnsRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b1745dde.mp4?token=rwcTFi9A7pyVzbgGrRsh6dMIDCHVm3YzhxzZNPut2zQcXYhfxjRPRheVyq-0iMImuRqXcGrKVsaB6mP811QX49u0-RcZ671JTLMW8aQqGgvtRBziRUYG9tC87SyRLvCmqP5ZzN1U7tFpWqEYqCXRotQn1LmB9-Z8yc_o-3qn8GLXIeQ3xHbdUna2KFqjqGPeQUQQ7ZT9SSURDmtfN9Xkrvx3zvxvuUZx0K-u-pWHMjF8rulEhxbbPdzBgyo7R6bz7OcJlqNxRc1Yq5yFMR5ixOCFUm2t7pGZnnFtg10wltoTTZbAwNpUzkNrFtXcBFoylZFfFXCx9VoAkFncxnsRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر مرحوم اکبر عبدی در تالار وحدت  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452616" target="_blank">📅 10:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_1G2yfJjuN8dIM6umuznGvRtjSgC0N9IlxEwY2TurMVOspE2ORlEcE34QG2wUZVHGmaiE43pejdG5Fop9BnqHzSP9W1o15uR_1LgidHzOYNJNmNzy7Cy7dyZhexgba1StBCQ14tG--oNaeojcvdK5Tc76I1HdNmDGYxZIr8c44__mWdvPd_gZRlnQpdYCV--7JvSw7Ciz6JdSLS5di0KO0sBlzgox78cFC23sdByDV-jRQcW7IB7Nq1UyzWMJSD0sQmtzP-lCCEdaFD-yXWIpwLWXxm6JIE_quzpS79LI6hvlWy09w261BvzJ0GlSSSU3z4nUk2NurEoY-DLG0aKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ تقویم فرمول یک را به هم ریخت
🔹
مالزی قرار است در ماه اکتبر به تقویم فرمول یک بازگردد و میزبان مسابقه‌ای باشد که جایگزین گرندپری بحرین شده است. پیست سپانگ در نزدیکی کوالالامپور که آخرین بار در سال ۲۰۱۷ میزبان فرمول یک بود، احتمالا روزهای ۲ تا ۴ اکتبر پذیرای این رقابت خواهد بود.
🔹
مسابقات بحرین و عربستان سعودی که قرار بود در ماه آوریل برگزار شوند، در پیحملات رژیم صهیونیستی و آمریکا به ایران و جنگ رمضان به تعویق افتادند.
🔹
در صورت نهایی شدن این تصمیم، مسابقات فرمول یک در سه هفته متوالی در آذربایجان، مالزی و سنگاپور برگزار خواهد شد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452615" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUOPFkhRCzhUZmtJhjdh0aGPQ247ac2aWL1q7tsrqOa-XZ5rcaBr2s0hnd26FJnz-dPBVbXKp7WKfjiIwpiCwMFLYuLqv4uTLvHAo1soVVbYjJwP0-RBtlKmmHqURrLpP72cB-LQ_NFtvq6mbO9RxiRY_IOt5dWzJzpOXH1A1fInjk-wetV35-ON7D7s8lQxoPwu3BRa7IfyuAh949aTOMn5W5g_dLZIqSb21I9VmPKBBCEgbaIoegsm9ioUxx5sQdsVMevMHHNVphF9tEATwc_rXvgJfW9CjL1qPPXtTpaRtQwQ-uW3R30UICMMqeA-TWvwpwXZ-309TAfRybuMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین قاب از فراز، یوزپلنگ نر توران
🔹
تصویر تازه‌ای از «فراز»، یوزپلنگ نر پارک ملی توران، منتشر شد؛ زیستگاهی که مهم‌ترین پناهگاه یوز آسیایی در جهان به شمار می‌رود.
🔹
براساس آخرین پایش‌ها، جمعیت یوزهای ایرانی به ۲۷ قلاده رسیده، اما کارشناسان هشدار می‌دهند این گونه همچنان در معرض خطر انقراض قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/452614" target="_blank">📅 10:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d8eab30d.mp4?token=T13Ph2kIM5KssE_I3CO33acaNMcLe9If518HrC4nnQJslsILxzoGDKviRK1vCOWGeMTZZ0OOzP3pz1tA0RCmfQE_PYk3ebU2OFsJk7U1fV9fa5KgQOKyDcT0bmmLBcWFv76Qdq47gydWAwnkRN0yTVZ93ZIN3CN3WfEKh9KJnpAkay-tjIXILGZ6bViJsMS1xFqe0MHdqEqjKUfHHK_Sdpk8X__EXi55VeG28kEumBi6Ekdt17BtXUex5CDJKX6fm846Hxp-immEGISPOxKYdhspYlclf8A3h3MAp-Y8WuXsRKnLhyxJ6_nSzR3Adg-zsuDdMzoZWCm1QNFnunI6sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d8eab30d.mp4?token=T13Ph2kIM5KssE_I3CO33acaNMcLe9If518HrC4nnQJslsILxzoGDKviRK1vCOWGeMTZZ0OOzP3pz1tA0RCmfQE_PYk3ebU2OFsJk7U1fV9fa5KgQOKyDcT0bmmLBcWFv76Qdq47gydWAwnkRN0yTVZ93ZIN3CN3WfEKh9KJnpAkay-tjIXILGZ6bViJsMS1xFqe0MHdqEqjKUfHHK_Sdpk8X__EXi55VeG28kEumBi6Ekdt17BtXUex5CDJKX6fm846Hxp-immEGISPOxKYdhspYlclf8A3h3MAp-Y8WuXsRKnLhyxJ6_nSzR3Adg-zsuDdMzoZWCm1QNFnunI6sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: هوا از ۲ روز دیگر خنک می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/452613" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf07b1f98.mp4?token=J4udMK3Bt9hf4zLsTVbcPwrqFgR-PnBeGi9vOgFe2W36griUgas3IXlLv9nFcC-74u0X0z9yPJlvni_q3DiJDkkkEMl0omAf-MMfMP8ixMB2RSINovONCDL0bce4eJQqkO1PHeL6Cln_etyyDqcEcH31ggzv494xS1211RONJDrHKRaUwDLwnlqNYgeq4EMySkiSk_1IwPMOU88Ya9ocm1Rw9WB3U-M4wdL52IR5HsAvz9Ozf7Da-0sMy7WWL80bnvMcnfw2ijPqtgbm5YYAKBlvdd4Sa8RBdq8hck7-8Gut2KJfrRVA8dtf972G7WgnLz5-8lQ_xRJOQcSDPWxHow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf07b1f98.mp4?token=J4udMK3Bt9hf4zLsTVbcPwrqFgR-PnBeGi9vOgFe2W36griUgas3IXlLv9nFcC-74u0X0z9yPJlvni_q3DiJDkkkEMl0omAf-MMfMP8ixMB2RSINovONCDL0bce4eJQqkO1PHeL6Cln_etyyDqcEcH31ggzv494xS1211RONJDrHKRaUwDLwnlqNYgeq4EMySkiSk_1IwPMOU88Ya9ocm1Rw9WB3U-M4wdL52IR5HsAvz9Ozf7Da-0sMy7WWL80bnvMcnfw2ijPqtgbm5YYAKBlvdd4Sa8RBdq8hck7-8Gut2KJfrRVA8dtf972G7WgnLz5-8lQ_xRJOQcSDPWxHow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حضور اژه‌ای در حرم حضرت معصومه و مزار شهیدان لاریجانی، موسوی و علمای مرحوم  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452612" target="_blank">📅 09:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2418a35124.mp4?token=hYZMGNgASoaTxzykutc7umSYS_fr487mp5_antwM19jdHAEWjIs8m-wAXKSNucBy9W3omU6SiT60f6YGlt6ol3-2HftEWsxjRRX6_baJgPoJwcM2JJV7WMer416rXsBMSRCbnQP3eaIOw-6D_CZnIEPsVg0S4qL8d_mHwsKfzFrqqbVUNprTxQBFYcRnRLy5cM9xds1WkBhwYTdEgi8TJL8iUGtCUJeu0WpayWe32gJA3zfE4GTS6JNTf_JvnhEysfO753ggCVhkdt_RFVCTK0d_ZaJPFAbdh2AQoWlxESZwTu_Y-jlFP7OPCjLBr_yLxu4xX-OsaMKqCFmxgtxQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2418a35124.mp4?token=hYZMGNgASoaTxzykutc7umSYS_fr487mp5_antwM19jdHAEWjIs8m-wAXKSNucBy9W3omU6SiT60f6YGlt6ol3-2HftEWsxjRRX6_baJgPoJwcM2JJV7WMer416rXsBMSRCbnQP3eaIOw-6D_CZnIEPsVg0S4qL8d_mHwsKfzFrqqbVUNprTxQBFYcRnRLy5cM9xds1WkBhwYTdEgi8TJL8iUGtCUJeu0WpayWe32gJA3zfE4GTS6JNTf_JvnhEysfO753ggCVhkdt_RFVCTK0d_ZaJPFAbdh2AQoWlxESZwTu_Y-jlFP7OPCjLBr_yLxu4xX-OsaMKqCFmxgtxQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس قوه‌قضائیه به قم سفر کرد
🔹
اژه‌ای صبح امروز در سفر به قم، حرم حضرت معصومه(س) را زیارت کرد. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/452611" target="_blank">📅 09:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6dd27524.mp4?token=vBDZPN5y-jAD8nKE5NVUEm-bHcVFI0whqkTC9s8hX4hUxpQZOEZDSaGWpxQajqaH09KgDLMVr2FGXHFEPMsHcaiXFZ_M5NAnGzL-k_JLSkiWbiG3pWr7lX6M4gEvfNhc_8L-r47-W7l9N6WuTOmlcoiN3gI-ng-YHZ9ZwNK5t1E9qwZn6CgUYg4YhpsAJ_BVU3nxoouciyZqOG5Y7mhFGi7qmvgxvpJPiPq-4kwT454G0f4Rp6sqvWMtT47-wGh4-6nE9dhtVjZdwzZFx6s6ETRn4PTEotgAWBgnVxXCMTApzzQcczlW6XYZObWaBE1QZ6nCUiXBAbemoXBVC4mXyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6dd27524.mp4?token=vBDZPN5y-jAD8nKE5NVUEm-bHcVFI0whqkTC9s8hX4hUxpQZOEZDSaGWpxQajqaH09KgDLMVr2FGXHFEPMsHcaiXFZ_M5NAnGzL-k_JLSkiWbiG3pWr7lX6M4gEvfNhc_8L-r47-W7l9N6WuTOmlcoiN3gI-ng-YHZ9ZwNK5t1E9qwZn6CgUYg4YhpsAJ_BVU3nxoouciyZqOG5Y7mhFGi7qmvgxvpJPiPq-4kwT454G0f4Rp6sqvWMtT47-wGh4-6nE9dhtVjZdwzZFx6s6ETRn4PTEotgAWBgnVxXCMTApzzQcczlW6XYZObWaBE1QZ6nCUiXBAbemoXBVC4mXyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسعود ده‌نمکی: پیکر اکبر عبدی روز یکشنبه از مقابل تالار وحدت تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452610" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8fd18860.mp4?token=v3bRk5Mqh_TwqdBtJyjEUCokjdHqNdk6r9ENzW-k2CcWyOX3fsZuvrZR1sz6IJ0j6IO123RT8ZeBErPIEIfF4WTC1p7Ztx6l489fvhfNarSPYdGYK6mp6BbxR_xv0Hj5TSDv1ZRQj1OUuTpRnO9R9c3-7oEcN4PKyT0yv_B1GPn_YgSe3BpkzTJEKqxtxcS02kUHLq3tz_0uehrhRo4q6of7My6FuOXayTGlylMjVAo10uyTdQB5MetXjOeobptQLAUO3goiYPex1dipkaO-EP_wStjb4_66titUt7w_mR_I9rTuaz9vsvX-qvRPkMTtVA3KXnmoUCLv_j6Ayxif9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8fd18860.mp4?token=v3bRk5Mqh_TwqdBtJyjEUCokjdHqNdk6r9ENzW-k2CcWyOX3fsZuvrZR1sz6IJ0j6IO123RT8ZeBErPIEIfF4WTC1p7Ztx6l489fvhfNarSPYdGYK6mp6BbxR_xv0Hj5TSDv1ZRQj1OUuTpRnO9R9c3-7oEcN4PKyT0yv_B1GPn_YgSe3BpkzTJEKqxtxcS02kUHLq3tz_0uehrhRo4q6of7My6FuOXayTGlylMjVAo10uyTdQB5MetXjOeobptQLAUO3goiYPex1dipkaO-EP_wStjb4_66titUt7w_mR_I9rTuaz9vsvX-qvRPkMTtVA3KXnmoUCLv_j6Ayxif9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج‌ها در سواحل خلیج فارس همچنان بدون مزاحم به صخره‌ها می‌کوبد
🔹
دستورهای جمهوری اسلامی همان است که قبلا گفته شد: تنگۀ هرمز بسته است و بسته هم می‌ماند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452609" target="_blank">📅 09:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b220fadc5.mp4?token=PMBAd2uu177GiLEO-PsUKgfDCxVkNjGZ9XX26nz9iWGVLf5xisUwFYlYJm2OqHG7tX47kIpPlKsipOCqy7K4KkdDdI3AdHG61Lkf8Q5PW4RxRaZVn54r0cLCxAFJV9REN_n4zAQlpvzN93c8Qxm3e3z8WkBuqEiDVaDSW9OSgrK59ggY2MyucBwK-WdMx_k5FKOn_8l0eVcRzXnpQKKNwR3NPj0g0LF6ZI9caAymCEwUbLgALEcazbKfRcSoFFQ46c03ff5wAKZgIuOi7ys33yfAIDQf8Puhja1vZ1tE7mkcKeaxLo_3Yv5hgyrBi_yWJyaHAOUdKPzNt8x2z4nHLD6mT6Oq51Rv4B6oDZnn1WMokmLkegKAAYxAvGQjedz36o4ST0bYjq0bwAoXP0HhpIcMyymSEuP_IQCJxWa4xTA4kbrG4Isd7UdMDEZ4xzvEGkt3BbmYJl0_ZQYffcKe_Ald-V15tu3fiAqRuxo_8BwqMwE9DmVNzWHZCsPzfWLw8_QOPvwk7UCHnyhqkrsF9y9HJJW2mPu1ufo2I7LYdUcjfIs4uhFDpdtymvaSOahoCFfXDTaqwONvegpR2lT6h9Y5fScE8sk0mzLxzxvb6ca3WY4iPKIQW8iLhlHTV8w1I7mGfr04L1NCF-oYkQkCSIlifnk6ZxoICH4qij0fMa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b220fadc5.mp4?token=PMBAd2uu177GiLEO-PsUKgfDCxVkNjGZ9XX26nz9iWGVLf5xisUwFYlYJm2OqHG7tX47kIpPlKsipOCqy7K4KkdDdI3AdHG61Lkf8Q5PW4RxRaZVn54r0cLCxAFJV9REN_n4zAQlpvzN93c8Qxm3e3z8WkBuqEiDVaDSW9OSgrK59ggY2MyucBwK-WdMx_k5FKOn_8l0eVcRzXnpQKKNwR3NPj0g0LF6ZI9caAymCEwUbLgALEcazbKfRcSoFFQ46c03ff5wAKZgIuOi7ys33yfAIDQf8Puhja1vZ1tE7mkcKeaxLo_3Yv5hgyrBi_yWJyaHAOUdKPzNt8x2z4nHLD6mT6Oq51Rv4B6oDZnn1WMokmLkegKAAYxAvGQjedz36o4ST0bYjq0bwAoXP0HhpIcMyymSEuP_IQCJxWa4xTA4kbrG4Isd7UdMDEZ4xzvEGkt3BbmYJl0_ZQYffcKe_Ald-V15tu3fiAqRuxo_8BwqMwE9DmVNzWHZCsPzfWLw8_QOPvwk7UCHnyhqkrsF9y9HJJW2mPu1ufo2I7LYdUcjfIs4uhFDpdtymvaSOahoCFfXDTaqwONvegpR2lT6h9Y5fScE8sk0mzLxzxvb6ca3WY4iPKIQW8iLhlHTV8w1I7mGfr04L1NCF-oYkQkCSIlifnk6ZxoICH4qij0fMa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناریوهای احتمالیِ آمریکا در مقابل ایران!
🔹
سخنگوی ارتش: یکی از راهبردهای آمریکا خروج از جنگ است البته اگر صهیونیست‌ها اجازه بدهند.
🔹
سناریوی دوم اینکه تحت فشار رژیم صهیونیستی عملیات هوایی گسترده انجام دهد. یا انجام عملیات زمینی.
🔹
ما برای هرکدام از این سناریوهای محتمل آمادگی لازم داریم.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452608" target="_blank">📅 08:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجار کنترل‌شده امروز در خوزستان
🔹
فرمانداری امیدیه: انهدام کنترل‌شدهٔ مهمات عمل‌نکرده در شهرستان انجام خواهد شد و صدای انفجارهای احتمالی ناشی از اجرای این عملیات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452607" target="_blank">📅 08:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b7acbbc5.mp4?token=bDNNpYZLxZ3YNwvCvbN87tSALYv4AqDK57pKbWd_hCWKvCOhact4jfXhPniCv_FF7ucKjL04S9ZIloLKTdeFjLfUKXMyx4ziQWNjJ61UtTYPa1yavZ-2N9-l8AipBWBpPtipl3sod13_hUaKcw0dwxD37z6KbZWY0609gRRY8kqREFOfrh6gkXGvj0Yji19vT4tJ4I_EIQDPvBU0dRMsX3cqka1ZNJ6vp6wyCO-wnUsWAKrWOn3RtzoLcwfIneGdiPab46IhQPWWh41_hLLdjRulnekgjLpIRoJ8Pbwik0GS9xyziqgIc6I-CZP0XoLXOE7T4pGi_pfri1YsI0C75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b7acbbc5.mp4?token=bDNNpYZLxZ3YNwvCvbN87tSALYv4AqDK57pKbWd_hCWKvCOhact4jfXhPniCv_FF7ucKjL04S9ZIloLKTdeFjLfUKXMyx4ziQWNjJ61UtTYPa1yavZ-2N9-l8AipBWBpPtipl3sod13_hUaKcw0dwxD37z6KbZWY0609gRRY8kqREFOfrh6gkXGvj0Yji19vT4tJ4I_EIQDPvBU0dRMsX3cqka1ZNJ6vp6wyCO-wnUsWAKrWOn3RtzoLcwfIneGdiPab46IhQPWWh41_hLLdjRulnekgjLpIRoJ8Pbwik0GS9xyziqgIc6I-CZP0XoLXOE7T4pGi_pfri1YsI0C75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نانوایی‌هایی که پروانه‌کسب اجاره می‌دهند!
🔹
مدیرکل گشت‌های تعزیرات: اجاراه‌دادن پروانه کسب نانوایی به دیگران ممنوع است. با متخلفان برخورد قانونی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452606" target="_blank">📅 08:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXNr0L2SWxza3JITxITi9T5yN9YkuIq03nlOfXj3l9V96FRasqxaLkFWRBl7CcCQHK6dQ3kGyWIjpi92_qeu-Az8931-8Q7mhhZ9A5yLfdUDiMhNndv7CJ05zL19pNgaowdCiATnFZSPE-vZc68hYYULDHtQMkW1Tvexhe8x33Fz9I8WeyN7GZUl-Ei61_hxOvKGpnV8V2OVztA2G-9r1Q4AnI8Tm-LIk9BGGHsdZGUJaiQGZqrQNcapvSb8X8i7UIcNFEJtbG8f_pdxGtMXTXhA3FRyCvAIlL4ZgowufEXweViwlNuT80iT3vQqIh7Qnkccl90E688c1U5ovWHefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: تغییری در وضعیت تردد تنگهٔ هرمز ایجاد نشده
🔹
بقائی: جمعه و شنبه چند دور گفت‌وگو بین ایران و عمان در سطح معاونان وزرای خارجه در تهران برگزار شد که طی آن دوطرف در مورد اصول مشترک و سازوکارهای عملیاتی برای مدیریت تردد ایمن کشتی‌رانی در تنگهٔ هرمز تبادل‌نظر کردند.
🔹
این گفت‌وگوها مفید بود و پیشرفت‌هایی حاصل شد؛ هیئت نمایندگی عمان عصر شنبه تهران را ترک کرد اما رایزنی‌های فنی و سیاسی بین دوطرف ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/452605" target="_blank">📅 08:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJnB1-tY-4ADD_HOK7ffwrpwSIGDb0PfOS1XK528nZ7YD2Pf1CItGvD_gKY1h4onf2vAQYkt6kcgXhxsgQ00u2B1NJYUlxIF0hKT4HrJBOP6IIBSD-k1x8zPgoDJ3NwwfeRJg0IiNRFxZ0Vpj4XmGtW4agiDDYeUQqItDN_31Zf0L4-L1szBZR1uFpMX0ktBhXyfN05Oiy05YQ-zrpIC3RtUTaH0_7Lfd4kkeuj8ZaShp47Cnj3pXsQmuwAYhvHWX5ICCespQ7V3o8DWxpTyUEToC0Zju9tHELmjZIuNDWcbjfYqiECNR1UD5d4wpR6k0FQ16AY1wHEiSRg6udz9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه به قم سفر کرد
🔹
اژه‌ای صبح امروز در سفر به قم، حرم حضرت معصومه(س) را زیارت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452604" target="_blank">📅 08:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452603">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در امیدیه
🔹
فرمانداری امیدیه: احتمال شنیده‌شدن صدای انفجار بر اثر انهدام کنترل‌شدۀ مهمات عمل‌نکرده وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452603" target="_blank">📅 07:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx8KuLOJr8br9CQpsj6D0v7ul-2OYnwbX4KREtljZQRWq62rZmT0m9rUe0f6AmaGVBSZs0bQFfTMmMeAtmQLbZlKU_OPDIijOpyDqE9c4fme_wdRfw58Zdtool8AVvLHnvWl_tKWWu6JtbJuGjRxvPBtvKd1jjiGnzKUv82yBO9_1l8yqs0ZBfp8krPfe5pe3KimnmS90QjsGaMSx6iv3aJESM1dgkp54uzMpSXF3rZbix4mMUN57HD4I3k-uxl3_ndLE_dxDFzub4ipPhg_LUfs2cw9gxQQC2-iLtJT-Ck6tRNYU5XrnJhI-8d-p_HiSQtQecan-AxeNA91YlDNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی مجلس پس از ۵ ماه؛ دستورکار با شرایط جنگی همخوان نیست
🔹
پس از پنج‌ماه وقفه در برگزاری جلسات علنی به دلیل شرایط جنگی و ملاحظات امنیتی، مجلس سرانجام فعالیت عادی خود را از سر می‌گیرد.
🔹
اما در دستور جلسات جدید‌ مجلس، به‌جز یک مورد محدود یعنی گزارش کمیسیون قضایی و حقوقی دربارۀ لایحۀ یک‌فوریتی مقابله با جنایات بین‌المللی، سایر دستورهای صحن علنی که قرار است در هفته جاری بررسی شوند، ارتباط مستقیمی با وضعیت فعلی کشور ندارند؛ موضوعاتی که حتی پیش از جنگ نیز در دستور بررسی نمایندگان قرار داشته است.
🔹
این در حالی است که امروز افکار عمومی بیش از هر زمان دیگری انتظار دارد مجلس نقش نظارتی خود را با جدیت ایفا کند.
🔗
شرح کامل گزارش و جزئیات بیشتر از دستورهای هفتۀ جاری مجلس را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452602" target="_blank">📅 07:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استاندار کرمانشاه:
خدمات بانکی و ارزی اربعین در مرز خسروی شبانه‌روزی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452601" target="_blank">📅 06:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452592">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTyH9nTYcAbTMRgf3YQSafuQDb58BcF7Od4th3UvFKRtTn8Dl7lrsdGbs4dLq4084Ko3Xyi1UR7JKib2hsJvNG8PElJykAZJdpnaUHW9gEtku5Hhyh47pXuj6ID4UCc0VjVvZFFOfyXVxe0P2pyQb5KbvFScT0TS2MC9d9L9g1kQ8W3HicAIL4S_Zu1fqjhyXjBNVFac76EdaBhX2vrfiuJkesm8AMqMC-_sXlbgadw3m8LLKQkt_jrSfQikM_geIStMwpTRiNPhvLLrb3rZo5NNbQldVUZSvQHESQeQ3wmFyqOFBU1L-OyBePIb5-gS0jMeh2dprQEX4kw-p6fGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGPciBuUbBo5ZtPBhrpTVofY5l-gW5FWiQsukGrfYXttKBe3Gz-UQb7Dl2OUTh-6H8TlmcEz6Lj3mvUGnNc6YXZbh13eYH8iQpzQg1uYC7eR1tScgDPndgPd3enPmZJMq8LLWAOoNkcGJaTTbnVeR3__4_wyKacnfzvtbiPmbQgrmHPU18sltzL9X0RYpERgQUfNKzsfdn98fYo8rL0htDnCh5n8AvauGeQQUcyjag7U11uqSlJNxY1zVzgfaIheNkWL3AxwL6f05jytKy1kZVtHGmUnO7gquMEdtkbjz6WmcRwVu48FrrNkRi8jMTUcKW3C1dtNMhF05jNGAE9l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfcAHbgHn4Ebv0Mu_KHW-Q1gLE6ro-pXdZVcBF_itpfRAutwkW5PxwK9B-7ESX6_zHqcv0_Fwl4mk2jXrv145YAbrlNBbbkA5AIj5_qb1QKt9jJzaOtySVbzq7xuqi6lT72KDZ9zpwnsOkceqBsqVXTnI7f-orF5oMY_wsf1sSe2gS_vzCfNYpZmOXDRxrCC8paWO6CCl6mW890EN1LLhHMBJjdijUEESMcrP_Ih-uWwuCMNMrvtsxT-V6rSj7ldRv1fMqKxwr8iX_-ghPTHGKmQ6Ye_nP6J0qqLmYhajauaiYZKyZrwk8D16K0WuD3FRGhm_QRyXOFcveQfJjUKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_roWixKd24xLwCTAQqgG0iCrvxh1QhfdAnS4U5RSqq-IUnv4BsQ0w8pbBfE9ETdbhPxVIDhfia8ufSgjZgEFFa0pQL6sL7GCe8QABmkOK1NPRAtPaczJUWv5UVjfJLp-_HjB0F4HX8R6WoIItgORaPw5gRgkonJp3UlTfszxSRrOXEDHG7z4eYOSrxx3awTyYC69YdCll-G5KwEo8dRruOXRwXvnPvT839BPl99q4_7aG9MmQ0qErPRnUJ6y0pOp0QRg03bSu5lFTEwEsykv9ez5JZCiCc1HG4f8AcQOGDE0WpX76zSAyXH_SKhBETDwZoQUwO4a3uvAsrKZRPCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPB4hFo5KV-4hBhY6SKAp_qGx0y9NNsF3wdwwGwuWeFl9rJw--qgK3XKlO90xc9tHDeX43bMjqBiAR_buLK86fIP_QNW7PfPBMS2LbkUQNcWTKWxfl9tu3SIWEGGqCujEHEDNGnlHfAKG9g91GpWQJcP1sMbxA8DLv__Ehhej2TiQztow1g7Rf4XKHtROlRT-YnRRDo6QVYx-33WKp6FoTBMPlUf-fvYIu_NFZYMJdsd_e_7f6YTbNXT8_TBjQblR958XGL8wawbXJyvBLhAgYS_NXn67-2JnelxRY_Y-nPhPb4wVE3vMxDaXkPWg79IYXDyKUjocQ7xrQlmeKiYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jf6vJEINys1vZ4qQiSRJ-2OtVuMmAbMvM2dRh6NhyWVikGq8PgODz-XdH5q6qtBMgbzXGdUpSKTTXkAzE2b7v4Dx-HmkqGPxjbkEpHal5SIF_Tdxh_biw5f_Iifh3oTuqoxGkQ6ob_trKtx_0Ft6eXp-36ZungBzMfcwj_bgfH4uoFV0hSioQzkTlJ7LtobOxxI86zgcQvLi9YWsqeLZMRd8Xo1npZOpVVMwv6wLB8mIy1sRNwppuLeG-xw-OIIynKylThlLy0sS97o0SoUdu1dMFFDl1LN6Al-j6cNF2nbZISvhn7Kob8_7MsTISKtT3X5XSIaJiG_pBSs2NIdaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8fhtcP-5xBfQVUV5JkDFHSuhe2BTq4MAUGlIETM7_3u03A7TtvmEvOGilUr_Z5YVuncIVxMdaXIIwyJGL2Wu2naqzRcC603czNwoe6ThC2pexizBpASxw8btx8jgDDTkKZaY5WI78DP3-ggMl4akzXTx8DW94joicatwZtCNfPWGbGQxNEdqm9DCZKU8tr12Y7T40ptnfHy--07fv4ULwvwsI9bZ1YbmqQ2T4QQo8O7OORqNbRB1b4PblsrzLI3cozakvEsm-YveDLq6q9hMnlkkVUsdnpNYbeDiSO-fTa-3OJrDnVVuVpYhPjYo5L2ZZyk3nT_16ZEE75XJwoctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1FsaBNU6Hi2WMEAX90hIXw4aM_O8Cw8VLlOconBMiC13upj1C5ocJ4WfG-aTtt7Z2p5ON3r1bndWzntIPWaMrPWf6C5w8FEd1NRggwk7rJ2Wa2_QGibSmgEhNaPhfv8dBaDOSka34TzCaPjXRRw2eEeAZbSfs6mUruGerZqb6C_6Q0scFoS7ZdW6w1qqrCB9oYPMG37GBZfDaVyFDfSls2YfwL-CYReHMwqlgwoO3Rng7Mt_auo4YUbXeuxtUbE2M5Tm4wnaAqYVsWgv9NsynhXlu2qodrd6kyI-SYnwB6yvDl3mxgWSD2QWciA1a5un7GPV09-pP7EL2RnS7Iz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_T3LXz8GDIuWrwjtShKExf0KWy5blJpR5qy8ggKpe26p9ItZxDA-FrIaFXqjREN-leCk8D5v5XgZId3Ckb-36DhbLV0ALQO08huFaWB_ub4a198Bn21Dsr2Tclo-di0jXppGuPVMrTDjepc5bPzjfCBKK2RP78uDoFn0SfyBBl59eVTOnem_herbKKvWP5sqCU6JrqJADdFD9haJmzLeUIq0mqn25WNI-nNJCji4RzJttLzQjuu4sf_8KE_TghunHlM0bLyWYGpJZf1fD-QemUbm8fXcDSBo54tm37zOJE9wUyXl4hTbPB0z8nHk4-qXkwrpsLdiZehjsCoQRYBqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای مواکب مرز شلمچه و پذیرایی از زائران امام‌حسین(ع)
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/452592" target="_blank">📅 06:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e427db85.mp4?token=VukmXH_d9rTIqMYCO6NjUO2-0567psdOs14Gk_596GwCQsPvOciHKUq4-1Pu8ByUd10X1pbyyf4j77NB9a5a3Vgiao7TAUvPZIDS66-rfa1JWoiYOpxsGOXOgLvfl-bs2sQ8CZIyz5kRWBZYqg-W134X_nIGWNmiLhp3k_8Vky-ZHHxGsOXpKgMpbQWey6T4cfQvbkr_3n7tzHyCp-CXAEmRP8u_h-oTsSB0g1Z4RrTON1HzsOvJmG_ZI8IwYrclBxgrtwj35jgrZAk5A923VoqXykxn5sBk8PgMBHO4sMUk5G0JhT0qYYIbdyy6k-AkqUT6fDPqLSuNKz_330UU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e427db85.mp4?token=VukmXH_d9rTIqMYCO6NjUO2-0567psdOs14Gk_596GwCQsPvOciHKUq4-1Pu8ByUd10X1pbyyf4j77NB9a5a3Vgiao7TAUvPZIDS66-rfa1JWoiYOpxsGOXOgLvfl-bs2sQ8CZIyz5kRWBZYqg-W134X_nIGWNmiLhp3k_8Vky-ZHHxGsOXpKgMpbQWey6T4cfQvbkr_3n7tzHyCp-CXAEmRP8u_h-oTsSB0g1Z4RrTON1HzsOvJmG_ZI8IwYrclBxgrtwj35jgrZAk5A923VoqXykxn5sBk8PgMBHO4sMUk5G0JhT0qYYIbdyy6k-AkqUT6fDPqLSuNKz_330UU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میزبانانی که خدمت به زائران امام حسین(ع) را افتخار می‌دانند
🔹
عشق و ارادت مردم عراق به امام حسین(ع) هر سال در ایام اربعین با جلوه‌ای بی‌نظیر در مسیرهای منتهی به کربلا نمایان می‌شود.
🔹
جایی که پیر و جوان، زن و مرد با تمام توان و از صمیم قلب، خدمت به زائران حسینی را عبادتی بزرگ و افتخاری ماندگار می‌دانند و با سخاوت و مهمان‌نوازی مثال‌زدنی، صحنه‌هایی ماندگار از همدلی و اخلاص را به نمایش می‌گذارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452590" target="_blank">📅 05:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2o-ULWNoT7p7DmRBottFXm0MgaUNJD3PshRIHQFBWSSt42N6qSW6xNhvWK_l1DH3vex1NugNsnjR1qxAN30O4yE6puwx50V8cQR4SOTZLaA5CECg2uH10hPa5Gi4hqQL_h_uaXcytjc1ExF4M2HunlOUcv18yHjNHQGvte4AX3YfaPvgIYf94wP8Spw5VSn5JBjNXlV0dcdHV95idM1xahTCumnyV5EZnNMccMKviAJfVpsCZi9rdRUhckrjp-chN0HeiVwhwxlwC9HKtWGYf5vuw66kjtoqSx6ue5_JCA6yBj7jvPXfJdx4hKE_QXGLQnwzlw2n_ZZqi8v8Ipg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزۀ ۴.۶ ریشتری، ساعت ۳:۴۶ بامداد امروز بردسیر کرمان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/452589" target="_blank">📅 05:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452586">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7feTSgJxa6mYaK-spm-lMKLkMfbR4JaeZ5zwKCApWfMUN_vEsj_9fQO5bb4o1CbapBxI1Blc2arKYKKzQ_ixgamNjhpepuOWYHRQnri_A74I9GM3Ss4TCjBRkRDeCv_fyxDcYIOt_kDiMjXnw9UW7C0MEkFQtm5UrKUUhEYfhDI9EtCuXVGA4JKg4_dBH8sR6aP88Oeq2hnO1SaG9WUbdMeB8YoqXE38ixQqm8DTC1w32G-Q9dwbdcwwAzNzKwPF2zvXXCDHRlD5dtAWNGx422Vx-VcRSCPIlwClV-s5qeGgs7j_XHu5lulZ_5bauy__8tKX_rIHy4U1mHDCKLpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reONUq4Ay4kkt2-WmmutWDtr5LwR_98s7EyHVfTZ2TanHbgzUIW55JSsX0vxAcnjZ6ktd7OpjmFqyEDi2scht-JpnDT3WyRuubrrW0NFZq15mNsJIz-iGS0P1hkZQ-bm15BGAVHQF3jLZfJoWRl2PYJocTghVoCiiO_6qnz8nLnjercOrd_S8PAY0V4lHvGlN4vMpYnti_Rxe90NrLymgmXaWgB_wEn7YcoBa75IDEzzoQaBjB-pekaK9g_a-nkkW0M5TF7qeeg2dH9FmsvQ6GvE8arBCtUWVPVxGHt-YtJqNfB9AR5y-vkYgUh9mFRgCnkmT-isnWPFysDH4w0nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ln6kgz91MAGs2r9y5PPFejMX0yff-t_4HxmUQVTC45BoQ-zs67UZ6tFuLeJXTNaXhQPCW8fg0jTXBlvMbj-4YGU977tCnxvDDe9Q_s4D7iLaRQiyQBFxsqvQdPLjHieJY1BzBGBcoO8Z7iSHqSccmm-OMRkKxp68qaKjUniyybPB5oK3USzTjWLLCxQott7y8GJG9kXNGk6__21xy7HyxQOLher9Js4kwCUs8OhVgwjLIWIkI6cskiif0Qk9zG4K9C8dRRll-tFKOd5atu5EnxIOM6coeXzPAH0r3_0vt5P2-4K8Shcs2Hjs8HQVFZNUVSobUx-IqloRauvaEKJfng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از انبار مهمات تا انبار داده؛ چرا مراکز داده به هدف راهبردی ایران تبدیل شد؟
🔹
حملات اخیر به بحرین نشان می‌دهد که الگوی هدف‌گذاری ایران وارد مرحله‌ای جدید شده است. در این مرحله، هدف صرفا انهدام تجهیزات یا زیرساخت‌های نظامی متعارف نیست؛ بلکه گره‌های پردازش اطلاعات و محاسبات، که ستون فقرات ماشین جنگی آمریکا را تشکیل می‌دهند، به فهرست اهداف راهبردی اضافه شده‌اند.
🔹
بررسی مختصات و تصاویر ماهواره‌ای نشان می‌دهد که طی دو مقطع زمانی، هر سه گرۀ اصلی مراکز داده AWS در بحرین هدف قرار گرفته‌اند؛ موضوعی که از وجود یک منطق عملیاتی مشخص در انتخاب اهداف حکایت دارد، نه مجموعه‌ای از حملات پراکنده.
🔹
این توالی نشان می‌دهد که هدف، صرفا وارد کردن خسارت فیزیکی به چند ساختمان نبوده است؛ بلکه فشار بر زیرساختی بوده که پردازش، ذخیره‌سازی و تبادل داده‌های عملیاتی آمریکا در منطقه بر آن استوار است.
🔗
جزئیات و شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452586" target="_blank">📅 04:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452585">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیویورک تایمز دلایل اصلی توقف حملات آمریکا را فاش کرد
🔹
روزنامۀ نیویورک‌تایمز به نقل از مقام‌های دولت آمریکا گزارش داد که دونالد ترامپ، دست‌کم در مقطع کنونی برنامه‌های خود برای گسترش عملیات نظامی علیه ایران را کنار گذاشته است.
🔹
زیرا تشدید جنگ می‌تواند ذخایر موشک‌های رهگیر پاتریوت و دیگر مهمات پدافند هوایی آمریکا را در غرب آسیا به سطحی نگران‌کننده کاهش دهد.
🔹
به نوشتۀ این روزنامه، موضوع کاهش ذخایر تسلیحات دفاع هوایی تنها یکی از عواملی است که بازگشت آمریکا به عملیات گسترده نظامی علیه ایران را به اقدامی بسیار پرریسک تبدیل کرده است. نگرانی از گسترش جنگ در منطقه، آسیب‌پذیری متحدان عرب واشنگتن در برابر حملات ایران، پیامدهای اقتصادی جهانی و تشدید بحران انرژی و پناهجویان نیز از دیگر ملاحظات کاخ سفید عنوان شده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452585" target="_blank">📅 03:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452584">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea8682337.mp4?token=UYJFzJLQjK2ZFJHQ4MhPE2fXiSGp0sG9uYVQoZwVn73oJhMhaMeAamCJNq72s4Jn9aqgNoj3m7F1uiIYjYx2YcWwO1ullnAfbxSng7hTghcigZk4jmgcCbx7ZS3h1VCFUwqkfSzFBk-51H_xCRdvvZIeVUzTRMoCmP2j5WPvkzTGn-j3psdunCRfpcfUvho5B3uxr3BAD-mSghq289OM-GAN1dou_ShkhiPsOqdSN-q_ckbHR526wUcAAkeVRx2yOEYIjEP3WmtmBA9h_JdXFwjLn2ygK386n3ANFrnAOzqlkhtJdnRXPMF7_14vbyleqUVGNDG4QpJfg4SuszxvUy4qnQe8UVJdXqgz4gtlol3Qzqt3HPEDNKkh55OvT8CHH3T-MgNaFuURXqt1QUoTNf2ExuJH0Cr0IJdTOFWRdUu9Jjobh6g8EM_A6P4S6eyrCq4UWtuhLi3WqF-LT6ru0i_czoPVZq86IIYFuS3R0D-2t0WFd8YnVk81xr4HX4FGOoy3h7XHYjYELHscPij7eZ4LJT2Jok_EXOe29GXUl1JPBn4HQ5Pr3l9PotSJikpz8q_qKXpcYdDDU7c-Igpr6zRnaO8LjNd7d_tEJDDdrnVe4fel_tB-Gq4bmHEd2xwZnlek2TYXVp5yisbzT74plfK7suXORhQdieAfU9JTFLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea8682337.mp4?token=UYJFzJLQjK2ZFJHQ4MhPE2fXiSGp0sG9uYVQoZwVn73oJhMhaMeAamCJNq72s4Jn9aqgNoj3m7F1uiIYjYx2YcWwO1ullnAfbxSng7hTghcigZk4jmgcCbx7ZS3h1VCFUwqkfSzFBk-51H_xCRdvvZIeVUzTRMoCmP2j5WPvkzTGn-j3psdunCRfpcfUvho5B3uxr3BAD-mSghq289OM-GAN1dou_ShkhiPsOqdSN-q_ckbHR526wUcAAkeVRx2yOEYIjEP3WmtmBA9h_JdXFwjLn2ygK386n3ANFrnAOzqlkhtJdnRXPMF7_14vbyleqUVGNDG4QpJfg4SuszxvUy4qnQe8UVJdXqgz4gtlol3Qzqt3HPEDNKkh55OvT8CHH3T-MgNaFuURXqt1QUoTNf2ExuJH0Cr0IJdTOFWRdUu9Jjobh6g8EM_A6P4S6eyrCq4UWtuhLi3WqF-LT6ru0i_czoPVZq86IIYFuS3R0D-2t0WFd8YnVk81xr4HX4FGOoy3h7XHYjYELHscPij7eZ4LJT2Jok_EXOe29GXUl1JPBn4HQ5Pr3l9PotSJikpz8q_qKXpcYdDDU7c-Igpr6zRnaO8LjNd7d_tEJDDdrnVe4fel_tB-Gq4bmHEd2xwZnlek2TYXVp5yisbzT74plfK7suXORhQdieAfU9JTFLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران امام‌حسین(ع) از مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452584" target="_blank">📅 02:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452583">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ارتش تروریستی آمریکا: تاکنون مانع حرکت ۱۲ کشتی به سمت ایران شده‌ایم
🔹
سازمان تروریستی سنتکام در بیانیه‌ای مدعی شد تا امروز مانع حرکت ۱۲ فروند کشتی تجاری به سمت سواحل ایران شده است.
🔹
همچنین این سازمان تروریستی گفت که به دو کشتی حمله کرده و آن را از کار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
🔹
در ادامۀ این بیانیه آمده است که نیروهای آمریکایی روز گذشته عملیات بازرسی نفت‌کش «شارمینار» با پرچم کامور را در دریای عرب به پایان رساندند و این شناور اکنون به مسیر خود ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452583" target="_blank">📅 01:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452582">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVvmL6F4KvoR-zTWxxUCSwbNPYN95-HOBIZW1bCkw9DYJ6d-FNd2RZR8UDxMH2D-TzuvfTmmAus6pmBJq-bEjZcpG9mzS1P-Tnuq9Bv5rJD8iO21vZVKce99YiRBdPIeuX7tdwkUewDNzCrHvDKOF7hL4YYt8DyU7esplMeQBVfqbiAJoXgU0B0pGSRVBGiToSkDIclMv_xzZ6T6aUBy2frn2ibr6vUCBrehQuQyTefranKEhihJk50q_6xP8snWK16lODZLQsZqa4zg5ZrRKHOXuX_5fmgoN4ZTUzt_4ffjA5IGSjC0ZIwT63SjVasFEt7VhlZrmwwe0LdvINnZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میش وحشی قربانی شکارچیان سابقه‌دار شد
🔹
۳ شکارچی غیرمجاز که با سلاح بادی پیشرفته وارد منطقه حفاظت‌شده ورجین شده بودند، پس از شکار یک رأس میش وحشی، توسط محیط‌بانان دستگیر شدند.
🔹
میش و قوچ وحشی از مهم‌ترین علف‌خواران مناطق کوهستانی ایران هستند و کاهش جمعیت این گونه‌ها به معنای کاهش منابع غذایی برای گوشت‌خوارانی مانند پلنگ و افزایش اختلال در اکوسیستم خواهد بود.
🔹
به گفته کارشناسان، مقابله با شکار غیرمجاز تنها با حضور محیط‌بانان ممکن نیست و باید از گزارش‌های مردمی برای مهار شکار غیرمجاز کمک گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452582" target="_blank">📅 01:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452581">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDaWaFlFH4TUTtbjefIc9PcWEOAZApZxLJ6gOA1PBDOhQmisPUFC9TY3aAQeIkfu-rqx7n1me-dyxSkJ1m5_l-pT9pRtLb018gdFXqjnEVijfUkak0ZMVQE9HK_57VuvKtcvQNgNq2uEzk-WO7pfq3123o1PwePcZMe5SQnHywCNw5v80nEr6sl6Z2dmoo4pX3Mg9PX8rRFbO9ekxe1269tLDilwYcE0rs24FEfz7KZpHJGj6BDHFpxDhwvyxB_cEe0jqKJPhEFLSlCn3L9wkRGzkbKWaclj1RqksSrHBa5ySKiMz3RDYtxgZ8dEc7mC-BAo8vbbhPMj96r7BwXq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد ۵۰۰ هزار زائر از مرز مهران
🔹
استاندار ایلام: مجموع تردد زائران از مرز بین‌المللی مهران از ابتدای ماه صفر تاکنون از ۵۰۰ هزار نفر گذشته و خدمات‌رسانی در این مرز به‌صورت شبانه‌روزی ادامه دارد.
🔹
ظرفیت پارکینگ‌های این شهر برای پذیرش حدود ۱۵۰ هزار دستگاه خودرو فراهم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452581" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuw3HkNKfUo9YSNQ7AsZUEq6hWGOwQQNNFQ8D_XLd3zz0A1Hf4TAysoLGD8e29hJbUilSOSFBgoAby98sq834G3sqMC1LH7mMzcWrliyJDS5yn5fY9W1bjfOc0rArRf7UR-SQafP1YAZxn0X-Fk80AwgekLi6PxpcrgL6PVdZLvfpWALg52DZPiPY8pnf75z-YwZ8cjt4mgjORTOzcaJv69hCH2aFfasD-jujSLdjulZLIbbRSaZwEJlQkeooxrGeeRC9eaCgtAkCtYlUYGIzOmpUXJG5BSPHrsZIMo-T1pf_6bR8Gt30i-GDVN8sQoOk7OrQpgvbdD45RkK3UuQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9M28tBpLsyn8pfTHoVSQEc3NPSx72ZXiSbsNPeMKQQz47GgCV4Ix8t6rjjCcqE6_4-9jWQHJI3vzYf2YNXSr_fp3Kmmr8xYbJojP5GVZew26J027CcY-7g0fFkobb4lkkUw8MfhuapbjStEzbS5jkyHW2eNDAs81H4YLbAwOVRGjYco0PQDW0Y2qbeDagw0nYoUi5YKOzf5FgM5kF17XnBJkQrkKfqVslDVShoDC5vrm9O-rzTMPAuqY2s5OdLOOGaA9Nxd0pBCbwfhxV7dh6s1zSvLZg_yPNC0jiJHdEPcZrXTVnVBLt9POavbEk-yKj3LtYFivgr0SvlT02Drcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOywaB6ySyF52mQYeztURb_9mtHfApqiwjUswMtGPC-sG4IGO7ceEekp2EIY99lH3y1fhPdhiFywuuJOgrtLWnoYZRHhDWlUGGNqEHDVNesacwsxicUKb3RE7r_H8IyNL10bXGy40TpHo4PR4z_fskZPMm9KAEUMrvVJijoXpB4ElCRCROJCSFjlJH3ycIaqjoAhCHW6UDnRne1sRD03jZQmWnMYODUmGBByZca5PJ9HEVNZJNXcbhxlymYa-OkrCkx3z5wBkH3WV-jI2YMs4X_UuU8eXi3CQ1LwC54tXZaxKdjA7j-EWOioUoDF74qmi9ak5YGcf3URlxdTH9D9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFnJdYniZM7qW-AjAZwM5qdsPugSUUMXGeFgkaexNlL0Qpuq_u_tImM0CfhX4gcP55YZ6wDXgcNm4RowpYBGoDUz6egQeQAlY_ONTYudIDYGROWgOh38KCTqebYU7xsvQIDEo3g1rsBBkKtr_flPbNAOUWii11ztrziC34yUvfsY7-NE7jFGme-WtniPr5n6uwcY5b-8wJC-9qYGrYwYy-PJngc59sVDxFVtIRbpVSFMhaRliLBbBEkHmkul17ilQe822SFuxPQ2JAxDA4BaeF-hJmRb38MA4Fg-ZrRQY_YIvC0ZBcVo5BLB5CtQX0NfajemllIX3aSwsTqL3llang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsXld0g9hKM9lHLJf-oZPlC80BmBQ968FTuuHxpLoq9O3JM3-xNkBf7L6H_85pNzeR4VpE4OuTQV_xsCRIU9bQtxqqp9Yrur0mx6uevsDv24C9c5oUXs_tRQmlpQEXnGzW2Oxgcp7bhSE3uJttj9MyVZtTxZvm60rYvmvQbIVhv630dQPaQ_P0UBWHGdoxCHSmYtEWVWvVYn3qD-uRIYsKuXbW35mfuWkEor18XihwE4g9PBbD1uTSlqLvEc0vNwkQckp9bsv2NydiQayy0MFrVBe8dK-fvl5-FXZ5ulSkxPlHMnxgVSrYVu7nkCGI_fcKGahP5OyK8HIAZdqV8v4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۴ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/452576" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shVBYWoGjSirTUJu96LmhMq7NryEmtSmn3acnZHNn27KU0J_0vWPQQdIs8JnKSd_j9zyzSMf8pmF-U-tj64YnqF6ukYvamQDEhRfkXB6sgbN6vGFmt563DYkA3W_Wcx56-nT6-XREvnLu70gLibBLycWSxFkIXx2j2UzQ3HFcuX5Z7rB8nLoB1GMH3yjCaeon22AGQngKTYUwPiBizTSkqOZXQi71iIeV2haHwGXMVYTPSZ_REhaIZjJeRPwG0kNpYdjcuL5O27lm8228kjgnlvr9pcqCfu0IPwzTeAAHppk8O4UwZptp8cO9SSjKvIb_u-v-w4MAUARw3f0iY49vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdgKK32cDKkIRitn-ueThN2ka0IArXImRcCn2ZTOYzEHSa3XuXH7wuRuJk5QSiqeVKP69cCr9QLRp0SEzw3MRogFamMf1rH-J3ViUvyac_LMrPCSJx4II7SyO__vQk0hxEnTSRNdUIQt_gSpTjgCR6KDN7uC-EdTcvifFa2ypUEvrSB7bjnHI75l6HB4ua-TM0_UpFlc-vCZtCrQ_Pc0lzvcrqw2hDVyzjIKJqKYXXybUZRFtK-oZBIoNYb4utQq6ru3u8SYkwP92fekR5epFdDyNmG9VGh46YfT-DW-cOSTw93T-B-quHLBGrXWSCTpMWxgHfleNEm3P2-XqJ7HVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mr-Zp47LfFdx0Bw_uuFK0dAqbBGYYTj7avl4yVrTZVhTZFk_ADWh0qvomn7ezTwtB5WZ8ILxcH9f-mof19JI2n68WmYQZRoGUUIwQ-LEsQom5FxeUoIgDGCZHmlb0uDNVfuLLCilYVuOHW1piwoiwF5-E0Vg7Sy6GwiPCL9poDhoBf2QGC0ZYcR9jvehprC5HWYbM7UFKPDq-L6WUalkA5RibB4w9ljsHXtVT94obO6Lh4YgtWJ5tZN5RHLWV257GQqIZlq5zXAjQrwod44mKmtKxW1x-0sq6rJqIHxp7iuOg_gUueIeQA0uufiQp6NSCR20wCuI6kgkgLHJo33iMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPNWdpW3-hFHtIxcmyat91Q4pz4YKpyeMcBPFKl2KhZplCWHL_tAXthcd94_ua06Arc-iaUZizoq9oBmNQa77-8dDwzhwuR5285QnLToh8oI522ibNVLHYEIraFcE3B0hX3v0IqUQPotWwlqhjH3XAameZxrHGXi0DyJFtTNyBNRVJCPGAGon7el7neK4KUZfWXoZcN9VTKCvrdjL3wqzCABmHFyyAx0IZgG3fsyFp3eKJtKizgmEIBh9K4Y7M67V4wlvyuyH87dAEpT2yqcLJdyNqPo0_usoRFzLwGE54sbjcCYNRS4p9nrX_ldb-SWHmsN1m5JOwQpeeMQOj8rEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoNEtnMppdnCbm6b_CtVd9QgEKGTmRcZI1B4hmKM0XSQYB_8FBf9EAbjt_IyN_FTZHkEERkm0NRXMiROSC3lLaEYcB3jyBSNPW6_c6GpOU6nXBkP59RTfi0N4S0Who1Sozid8Z9Uh8TyLEgjg3GGRA-Y7oYV3LPjm3I68u0GmLwxWVtjTw2gBfHfSaSrYKMZYCV2oWr0aFmHxwkB_cc5YqF7su1aiFlzW7uR1ZNtDB5EgRGHnJF5V9WWhn5UT38QuLoUyafErl4hqSwPagLCMUnXPAtxenFefRoYdAB9lItbDliRHzbLhxverluS6YKuyzTACruI8dGME5hcuW_1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yn64mAoeh9zrKryIqfeajFLvFfHb0wcOUiP6zq8wP5xHA2u06n98PmxGHGwZ3Y3-Y0vbb7VCyrBu_1rCAq-Ot1XX1HKBsSnyvJ5_NiFcGfmyO74tRH21DZGey5S_zFALa8aVGYCD_YU5bskOkcC_tk6IJKb7-FpD-Xi1mZrRXsEEvPaXZHfZjG-jBYUSjF1_OWkQVVD2FFoUFJbEVkxz29ZqmqazJisUiIHO0Q9AU5O0GQHwWrdB-ahPXh9VPVYFS1kvb0fFFTc-22E2xzy2NFL3xeV2D00UukHB3qHIrzmnFZleb-GKb98DlxrYzToZAejVIQmrBMxlvstv9lZnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8l7ojzzIBqPLnt87KO364v00mjqe_LZ7WJbm_ck7W7fa3OSeTIfQvnB1LwWv8IW5M-MoucG7Q1SsLiyUGeWmQc4G8tEMersZaZyXxGjojE-KieRCkZdDg90DrmWwix4XcqA3yGBxpUXk5IiaFFwuRsyqiV8NY2TLBv6V4O3_7tAfYLQ8iHko6Iv67BS9bhw2dR4z50Pvn2jAb_JJOh5IEvBQ6GrwtzB-HTD-GEnsKeXWHrgQ1rBgXEIhBqa_JJMmR3h1DI5ICHcq7CStfGEPI4w3IkBvP6Bwo6RfCMqfRLoT_dt2QJEmcDLSwYdV31gCItj5IBHGr6dvRC3QHfs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBnGjkteIR4-jvgK33nqEIqSTQsVPEzU4W9Pd17rjKZGfjMDKvsyvF426wRBZHTGgGyf3smgfRoQ1z0nMwJnGZfMNeI5gFhOWJr9mqmoZR0a9oz9aVuSPb9pXrndKwpFmmnCaFP7yFbfN-Z3aZOLEvp0RbAeerUPUbbI_yCNttoo02TWfgvG1OSleSAnfLIXZIjqUibygyQwzRLLzuKj52Sw9g3IxsxDLtkCalbbiqepH8U3vEJxvB19-fpYOlLEu7Eb7NLuMnNdMMYiPCO1YaacqPi650E9aK3pL1AwIKgrAueoKiYdzYJom1CRcJSrrQvNkISWDMEe0HTrZFWsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnyyqH4pyqe-RmcLQPaiUMOcwHucVy_9UTj1yddnq6F0i333Vmam0M719MyUSeq5PSy2ni3p67rf3_HO3UrZpwh1pVLCCgltRuOp1LK5UbA22vA7z7JaBJy-Zz4WP5qDSkgUO6Y-XGxOoPCtE9n0Rt5zJqBH-TyrW3wN8N2R-sI61_i-HZCI5LGdQaQ--68-YR3XiIk8WlD3-SbWtB4eQBCONGcRRnPi78BGa7BqzJfNOGN3e09Spgzh43i6aDnkasGrPrqaplWp-3_RUKxCIPnuPD3tALvYd86z7H26GMYcRj437s4Gyne0cI_oxl4NspGvyauw0bbtwn-keTBl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHfjb7dvsH37r7EMAL4zhsC-zrtn9BM9ofs-F72ikOJI-XtPXIX8gbG7ky6WZDQ4y__hqSQLzaP9rHLJkK9QpqshFBUL-FEpVeP6C_WMxYZa3TY5DfWuaUSGkd7CFbv3T8HpfNQiNe0Ff8ljAfSj39ex_jZvkG2JDDZFxxwcNzbDSjMLBIAxk9eXNoFNmLiKetvab0w3nk7M1afkWfsZqJi2ynOLO3qYyFApc3o_T8bB6KiowI97kqryEcFlkw6NzsMxKdNkMUl1GDQhEkqyCU1RIu1g9H9SzhkCckv8iW9X9vds4ZL7AhCQ3j6fuONlR08sGlGf06IxK2LqLkaFkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452566" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9902904ef9.mp4?token=byXgEdbA2Ft9DBN7gSAyO06HjBhYxQn50QBhsSB_zXrbmB3f_oZtKuv4-K5R6z3UH46fAvkRSFkS09jf8Y4BppHP3VmCYjKLcycIR22CNivXpv8sC6enVau8hAtHCgPWFPVFmU_mIzMd_0d3xW6kCK9ZXW7EwPFUdszPzf2rVS6V7ySFi6iIIzomjFnATKS2rx18jskZ2_Fdz7jCGuSQhpdXqbKQNtXeS-O99EIlJbvh5ZfW3mFYkK7Atj3Bw5GAcDI5h6EdVWImcRHqUWj85j5gmVJjJVycytSRn3AeZ9Vk3N7XNXUZuT_Dlp4U8eKt5npcr-kk1G8Po7jDesPsCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9902904ef9.mp4?token=byXgEdbA2Ft9DBN7gSAyO06HjBhYxQn50QBhsSB_zXrbmB3f_oZtKuv4-K5R6z3UH46fAvkRSFkS09jf8Y4BppHP3VmCYjKLcycIR22CNivXpv8sC6enVau8hAtHCgPWFPVFmU_mIzMd_0d3xW6kCK9ZXW7EwPFUdszPzf2rVS6V7ySFi6iIIzomjFnATKS2rx18jskZ2_Fdz7jCGuSQhpdXqbKQNtXeS-O99EIlJbvh5ZfW3mFYkK7Atj3Bw5GAcDI5h6EdVWImcRHqUWj85j5gmVJjJVycytSRn3AeZ9Vk3N7XNXUZuT_Dlp4U8eKt5npcr-kk1G8Po7jDesPsCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله با خودرو به جمعیت در پایتخت آلمان
🔹
منابع آلمانی از حمله فردی با خودرو به میان جمعیت در جریان رویدادهای «روز خیابان کریستوفر» در برلین خبر دادند.
🔹
روزنامه آلمانی بیلد گزارش داد که در پی ورود یک خودرو به میان جمعیت در جریان رویدادهای «روز خیابان کریستوفر» در برلین، تعدادی مصدوم شده‌اند.
🔹
این روزنامه افزود که عملیات امنیتی گسترده‌ای در محل حادثه در جریان است، اما تاکنون جزئیات بیشتری درباره تعداد مصدومان یا شرایط این رویداد در منابع موجود منتشر نشده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452565" target="_blank">📅 00:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسانه‌های عراقی از وقوع انفجار در یک شرکت سرمایه‌گذاری اماراتی در استان سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452564" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea1b1cd5c.mp4?token=uyKLIIEhnn_U9dIPGaGw1pIOOIDmTixUli6p1iL6jsI8AW6lNKXMaVZ8Af_FFIeDgIYaFsrSIwu2DtDH_aaYpF_z7w4Kp3oYSJ_ambg2PBdOHIbUUCe0Mn9CjqJ29m9p2xRKSecU8Tb5JoJmBI3RrQoCTXPXHdzv-PqjcO8vKvHoLvFtw-A1F3qtycUsdYskjr1XeqIbpgotYqVrnviqzi2q6WzuAXVBSPqW1Cm-FUU-ArLeHTYsEjTlJ0YM4hd91VnIehwBKsScLAYxn1WseiSgXcCY11pzFYMTU28jVkxFa_SGottPIZEnP24Au1EHsZ4hKmyrNIOvp4ZEEu2Gxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea1b1cd5c.mp4?token=uyKLIIEhnn_U9dIPGaGw1pIOOIDmTixUli6p1iL6jsI8AW6lNKXMaVZ8Af_FFIeDgIYaFsrSIwu2DtDH_aaYpF_z7w4Kp3oYSJ_ambg2PBdOHIbUUCe0Mn9CjqJ29m9p2xRKSecU8Tb5JoJmBI3RrQoCTXPXHdzv-PqjcO8vKvHoLvFtw-A1F3qtycUsdYskjr1XeqIbpgotYqVrnviqzi2q6WzuAXVBSPqW1Cm-FUU-ArLeHTYsEjTlJ0YM4hd91VnIehwBKsScLAYxn1WseiSgXcCY11pzFYMTU28jVkxFa_SGottPIZEnP24Au1EHsZ4hKmyrNIOvp4ZEEu2Gxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی: چندین انفجار و آتش‌سوزی گسترده در استان کرکوک عراق گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/452563" target="_blank">📅 00:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادعای کویت: هیچ حمله‌ای به خاک ایران انجام نداده‌ایم
🔹
با وجود حملات مکرر تروریست‌های آمریکایی از خاک کویت به اراضی کشورمان، سفیر کویت در آمریکا مدعی شد که این کشور اجازۀ استفاده از خاک یا حریم هوایی خود را برای عملیات تهاجمی علیه هیچ کشور همسایه‌ای نداده است.
🔹
او با ژست صلح‌طلبی ادامه داد: موضع کویت در دعوت به آرامش، ثبات منطقه‌ای و دور نگه‌داشتن خود از هرگونه درگیری نظامی، ثابت است.
🔸
این درحالی است که حتی روزنامۀ وال‌استریت ژورنال به تازگی مدعی شده بحرین و کویت در یک اقدام نظامی مستقیم و نادر، اهدافی نظامی را در داخل خاک ایران هدف حملات هوایی قرار داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452562" target="_blank">📅 00:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">منابع عراقی:
در پی حملات اخیر ایران و برای چندمین بار پیاپی، سفارت آمریکا در اربیل هشدار شدید امنیتی صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452561" target="_blank">📅 00:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واکنش وزارت خارجه به حملهٔ اوکراین به کشتی تجاری ایرانی: ایران طبق اصل دفاع مشروع، در دفاع از منافع و امنیت ملی خود تردید نخواهد کرد
🔹
مسئولیت پیامدهای ناشی از ماجراجویی رئیس رژیم اوکراین، برعهده آن رژیم و حامیان و محرکان آن خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/452560" target="_blank">📅 00:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b3ee1c54.mp4?token=mCTbDSmkBnQa_r4D5fDjvtkHb6Wio7HXRJIO8kUQLLk45uNhbdW3z9uXH_TfIV6bpJ0P56ZpazKvdmMfM-kplcjF5haotMs0HLkXd2wujPqaV06w-nJBZFdg_NkFEYMe6bSbQuAMSbKYn1Mth8hQTxKfLoGWt7bvLB5XO_HU_ePmmxpIMTxK8LwbMa6emYJzY9koBGQ5CKgeJiDEeb9u2izdZ0R7ujS6LuRzy5FmaQbLkaBgju_Vhk6uYhhL91DqJQKB-Z6DZw2z0wc_9Djcrvx8yddIxAGqqKueJdj9czEdul1K6xfhOTB5NKgFlAkkEz3s-gihI1c6GA-1YmDmtW660a2JuYz6LbN1bE7yZ57Dpp-62OnPmHKX5REXgbNyhI_-aziV8NqDJ1K-g6Sw6SVRj0SslWth5QKN2ykhqTAfd0WHnJA2N3j26hlaiFXMcz7O1qN5DZMDG1laxqWZoe3gkFD-x0hYIOyehIMtz0oqxwBQouFEBCM76rK4x4RKMgIotDyGyDS-dAoMcuQuu1_qOIgrPGlSJBRB5ChU2Dpgnd_hhyiIorBJbOdw58ehEL5v4FysmUlF3w0lYrPBF_rpSWggU3ssikTrNR-mL7cCnJuFMK_F-R6qKgr8LKnx4HQFp5oPUnPUD8TNIl2CRmJRRhmfEImSXP8pcUyifVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b3ee1c54.mp4?token=mCTbDSmkBnQa_r4D5fDjvtkHb6Wio7HXRJIO8kUQLLk45uNhbdW3z9uXH_TfIV6bpJ0P56ZpazKvdmMfM-kplcjF5haotMs0HLkXd2wujPqaV06w-nJBZFdg_NkFEYMe6bSbQuAMSbKYn1Mth8hQTxKfLoGWt7bvLB5XO_HU_ePmmxpIMTxK8LwbMa6emYJzY9koBGQ5CKgeJiDEeb9u2izdZ0R7ujS6LuRzy5FmaQbLkaBgju_Vhk6uYhhL91DqJQKB-Z6DZw2z0wc_9Djcrvx8yddIxAGqqKueJdj9czEdul1K6xfhOTB5NKgFlAkkEz3s-gihI1c6GA-1YmDmtW660a2JuYz6LbN1bE7yZ57Dpp-62OnPmHKX5REXgbNyhI_-aziV8NqDJ1K-g6Sw6SVRj0SslWth5QKN2ykhqTAfd0WHnJA2N3j26hlaiFXMcz7O1qN5DZMDG1laxqWZoe3gkFD-x0hYIOyehIMtz0oqxwBQouFEBCM76rK4x4RKMgIotDyGyDS-dAoMcuQuu1_qOIgrPGlSJBRB5ChU2Dpgnd_hhyiIorBJbOdw58ehEL5v4FysmUlF3w0lYrPBF_rpSWggU3ssikTrNR-mL7cCnJuFMK_F-R6qKgr8LKnx4HQFp5oPUnPUD8TNIl2CRmJRRhmfEImSXP8pcUyifVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاعی عضو هیئت‌رئیسۀ فدراسیون فوتبال: در مورد ماندن قلعه‌نویی در تیم ملی هنوز تصمیم ‌قطعی گرفته نشده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452559" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a48e534a.mp4?token=r2XneW808vxCqBShvP72FkamF0MmAkPBkS1_X6nwsLQj7wfKNsff4uH9IfJwqhebPGezor24XT4KUGYVu6zaa61cw9uwLSYhgtxC5PaM-IY6e-sgcKs3disqle_8Qxl5Z3VHa4YOkbLlrE-3ImWb-ohOQ11Ly15n7vGhS7Gj-ICpDhf90G7LKI35rbvJ_5qVLItuznCO-zG5s138apJOUpAOynCuhYjkxhulZtq2Loc4fqen25CjpG_2nhbzwT6kLcjyzPYpo_-hXRDB_QqYVJhzFDhwhFJzLahy6dNc0qkzHVkT8ex7bdOTRFxZy1GiTvx28U9UacRMaOjuj_oDbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a48e534a.mp4?token=r2XneW808vxCqBShvP72FkamF0MmAkPBkS1_X6nwsLQj7wfKNsff4uH9IfJwqhebPGezor24XT4KUGYVu6zaa61cw9uwLSYhgtxC5PaM-IY6e-sgcKs3disqle_8Qxl5Z3VHa4YOkbLlrE-3ImWb-ohOQ11Ly15n7vGhS7Gj-ICpDhf90G7LKI35rbvJ_5qVLItuznCO-zG5s138apJOUpAOynCuhYjkxhulZtq2Loc4fqen25CjpG_2nhbzwT6kLcjyzPYpo_-hXRDB_QqYVJhzFDhwhFJzLahy6dNc0qkzHVkT8ex7bdOTRFxZy1GiTvx28U9UacRMaOjuj_oDbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
افتتاح زیرگذر میدان سپاه تهران  عکس: ‌محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452558" target="_blank">📅 23:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7B_SGRDcTQWCr6F1RKPm3vca6S9c_NvQil1cLboEuPWPI6_8KCjDdEU8cmockrLD107nfLYpGc5mu0_bRvR71Wy8Es3RfOMkPCQiWc4pZ9zkF5JaovjIuPEaWXyfuFghQ6epJ8VdUtlqcLPJPrhiAXOH16gJp6IJZr1Nk6GpM33ySW5gTFQeM5mGApJOvJy9SdMWe0atasGR41PgdLdU2wX6zma-cfkDMRVh7o7m6NroxzbjN_wib2LgY3nOpaluslBz2YKPeSF1ubZP-VKVwkVxjA7Uvr0QQu-nL4q7lr6Xz1w1DCXvCbbAZ58yTyELS__qONpoepXTREZRnExEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452557" target="_blank">📅 23:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5TYDLaPB3oas45xq9fI9oQ5YJJo6ofspew-TNAMIfgWxHl8cobsoh2wyEBxggaVBbpPcy967wYSXKqmFGoz8O0XPyfkkCHlfzye9tYKE7s2szPusRKi38KEp8_cjpAxwWvtHr8fhRxueOp8TrZU8EcqF7fi72INIlfNcom63sKcbasqtH8RgdCqewePEQ7Q9dO5TNuj1e1gwGge2HfBkeF1jxDvsi-OwmcAOZ6loTn8Q2-Om8VSDfkrLvbwZBjE0CoAbD_KoEJ9YQDQ4zONLwL6AwlAECaOlkZMVmcAnSuYBF96hlq97Jh3GDfYM9IMvJ9dWOoSa02W4oByM-qjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: به کشتی‌های انتقال تسلیحات از ایران به روسیه حمله کردیم
🔹
رئیس‌جمهور اوکراین در گزارش عملیات‌های جدید علیه روسیه مدعی شد: در حملات دوربرد به دریای کاسپین، کشتی‌هایی که در حمل‌ونقل محموله‌های نظامی از ایران استفاده می‌شدند و یک کشتی جنگی، هدف قرار گرفت.…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452556" target="_blank">📅 23:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6eYqd4ok4iT0zkPd5LOWEUIVWiTO8i7l3muEDlHnkXxb2iSREOpKv7diZqwf20EDTYZlUOMeVkxBgTI1eD-pwDo_CLLWOcey0i4Snh6PjC7iUO6_TuNRtC8-2zYuT5PGKIpxZpQljsm1LWpXl0k2CPb0MiMBP65SI9cqsWYdGwCirEtyqiLsrgFgKspcv9IVvpoSdu0wQlc-OD5Mb7AU5_ol4r1cugZM9kSLC5rSDL61bdczm8-aqg0epAPxc6aXSsGpoq8gyPOfzfIZKug5Svsvxwq2jFdOSxKm3ZpWu9etfiQfAkRYdvC8xWUivuRSfnsE9BYn3VyFAISzkaXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تا ۳۱ تیر نیروهای مسلح ایران ۱۱ جنگنده و بالگرد آمریکایی را روی زمین و درحالی‌که در پایگاه‌های آمریکایی در منطقه مستقر بودند منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی،…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452555" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A--UZuXl9mJKWb7xyPFOwsKSm7EBaactFj3Rs-YIbSKzprPR2f3soad7gsKx2M1Hz4kuZrgiVAxuh1qrqHkr5XAhZKTXa6ziypX9CMnesvgmaLa3oKQaU0QvMFjVsYoUiQweqPm6TaCDXxMFs_RrpZg0roNPf3qgIrGSwp85-4wYF3fObb51eyEEyR1NQhufhd8eu0DGnymO30x5tgC8YD27bmEaLQx_x4JObI9MUFzi4PYeGNqN_Royb3Jv3VC7katMJKme9XByae1DKaKRhYDKJOBcGdP1qJkZHLdbK-ztpyWtNY6YvolkY3_YRjWYHR8CGrxl8i5eCvWA-hxBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منزل «بن گویر» هدف حمله پهپادی قرار گرفت
🔹
رسانه‌های اسرائیلی گزارش دادند که یک پهپاد در نزدیکی خانه ایتمار بن گویر، وزیر امنیت داخلی رژیم صهیونیستی، اصابت کرده است.
🔹
این حادثه، طبق گزارش رسانه‌های اسرائیلی، نیروهای امنیتی را به حالت آماده‌باش درآورده است.
🔹
شبکه ۱۴ اسرائیل خبر داد، پلیس و سازمان‌های امنیتی ذی‌ربط روند بررسی و تحقیق را آغاز کرده‌اند.
🔹
صهیونیست‌ها تا این لحظه، جزئیاتی درباره ماهیت پهپاد و طرفی که آن را شلیک کرده، منتشر نکرده‌اند.
🔸
این در حالی است که درباره تلفات انسانی یا خسارات مادی در اثر اصابت پهپاد، جزئیات بیشتری منتشره نشده است.
🔸
تحقیقات امنیتی و فنی هم برای بررسی جزئیات این حمله ادامه دارد و مقامات رسمی در مورد نتایج اولیه تحقیقات سکوت کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/452554" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی ارتش: تقریباً تمام زیرساخت‌های آمریکا در اربیل نابود شده‌‌ است
🔹
امیر اکرمی‌نیا: ما آسیب‌های جدی به پایگاه‌های آمریکا در کشورهای منطقه وارد کرده‌ایم و بخش معظم این پایگاه‌ها از نظر عملیاتی، توان اجرای عملیات به‌طور جدی را ندارند.
🔹
مخصوصاً در اربیل…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452553" target="_blank">📅 23:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIer1zxKeLCSvnKYFMfz4_h2WBkdTYa1uidXClDRZpkKkj28W1OUeRVOpmd6aCKI6f1lYHg7uhnUZUfE632QUVZ7I7uNjwglYQNSyVD7pq36_upRZ0tmdnsRzaYc-ctb2JcBw7pWJ3361NUKK5pdxUm6tpxL3n_26Xa2cHmwG4Qofi9ab3KSmo-D22uNB4OJXt6ZmII5d3ek_yiyk9qU3Bm7YV1-1XW1oBSfYNitfHrmVOgwayRmHUeA2ZPsUkM-5SupZluYebRn4Yx8xIER62H9WVVEUm39uWOZyUAPjYN8oKjgU5RcYl8p6TsLTX--cISei8RuaO1KjKvkZzONgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: تقریباً تمام زیرساخت‌های آمریکا در اربیل نابود شده‌‌ است
🔹
امیر اکرمی‌نیا: ما آسیب‌های جدی به پایگاه‌های آمریکا در کشورهای منطقه وارد کرده‌ایم و بخش معظم این پایگاه‌ها از نظر عملیاتی، توان اجرای عملیات به‌طور جدی را ندارند.
🔹
مخصوصاً در اربیل عراق تقریباً تمام زیرساخت‌های آمریکا نابود شده و نیروهای ضدانقلاب توان عملیات را ندارند.
🔹
آمریکا از توان، تجهیزات و پایگاه‌های زیادی در سطح منطقه و حتی در جنوب اروپا و مدیترانه برخوردار است و تلاش می‌کنند خسارت‌ها را جایگزین کنند.
🔹
در هر صورت ما این آمادگی را داریم که اگر این جنگ ادامه پیدا کند مثل گذشته عملیات‌های خود را تا زمانی که آمریکایی‌ها متوجه بشوند با تجاوز نمی‌تواند اراده خودشان را به ملت ایران تحمیل کنند ادامه بدهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/452552" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4830f3ef.mp4?token=iCyRrqDoj_Hirc_GneyP1SnJ7qO2DYWI6Sd0wk9Pb6RpKp2evyIpSeDuXxyftbQvyrOTWp4SOYl_5isBsdM-MTYPFq1DbxWAFnfT3z6DGVhVR4x2ch4D4h4Mfy8oxTQta9cREv4yhWDaFas_WalvTgDQ3ecaU66xmdQJufo0STTfT2chIz5HJyqKheipTXhC5AqJZkpnNyNTHvhI0lGlcR-fVHnk-zDrKtHy11LnIHiuUAGylR99ClSt5iUKzHSAVTKQCC_GfUi2c-EVapXYTB9-2kMeE-xSHh6wnsgDsGqyrU5Ke0mPDgZvugt70uA4qDKZG28eRBnwNL97EmMJnYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4830f3ef.mp4?token=iCyRrqDoj_Hirc_GneyP1SnJ7qO2DYWI6Sd0wk9Pb6RpKp2evyIpSeDuXxyftbQvyrOTWp4SOYl_5isBsdM-MTYPFq1DbxWAFnfT3z6DGVhVR4x2ch4D4h4Mfy8oxTQta9cREv4yhWDaFas_WalvTgDQ3ecaU66xmdQJufo0STTfT2chIz5HJyqKheipTXhC5AqJZkpnNyNTHvhI0lGlcR-fVHnk-zDrKtHy11LnIHiuUAGylR99ClSt5iUKzHSAVTKQCC_GfUi2c-EVapXYTB9-2kMeE-xSHh6wnsgDsGqyrU5Ke0mPDgZvugt70uA4qDKZG28eRBnwNL97EmMJnYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار و اتحاد، پیام مردم مراغه در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452551" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2SyQ_ND4H7WLe79unQNYkaqc_UU_Tuhw0Fq4ERTeRtIciU5gnZnaNSHuB-AEu2hkSJKqXxdEGoiQnlOLmUO2jc4qsm1p2zv2_BewlhAc4cYqdkEXHUAhz5S5lq9FSrT3RkSni0mjhRPu5T68eF0F0qjOzON3UTS2L5Jt8eFNclKs-ROfhB9mP24qOyVCylRvnU4TYzez_6Aqcs1fQZL3s3X62wR1ZPbpXEf7ME_laX06ylqwfaYSuOJ4_kevt6ZKZGQw-WX36-6GG-ceRXWVp_Y2JCebbIrEVbZJuUdLCAVJygmeO40-SuXO5z_5zSIVFl5deRfi_IQPt2f40f5zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام ۷ باند و کشف بیش از یک تن موادمخدر در لرستان
🔹
فرمانده انتظامی لرستان: ۷ باند تهیه و توزیع مواد مخدر منهدم و بیش از یک تن و ۱۹۳ کیلوگرم انواع مواد مخدر از آنان کشف شد.
🔹
همچنین ۲۱ نفر از اعضای اصلی به همراه ۵۷ قاچاقچی و ۷۳ خرده‌فروش مواد مخدر دستگیر و ۴۰ دستگاه خودرو سبک، سنگین و موتورسیکلت از سوداگران توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452550" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
بروجردی‌ها: سلام بر مدافعان ایران، از طرف مردم در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452549" target="_blank">📅 22:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452548">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c4b40db1.mp4?token=MT9P1rCmYgSrqJBBqb9Lklm2o7qGhOGJOAuIz2londZiMGe2CPLlkRFyubROcsl-t6z19Or_jrsRX1jEbVPwQ58bV1-WjYWJSqLqJ58yQzxnFJLtQvJ-KIQz4GvP2h6h19llbUrEuLa907DBtNM8rDw-nPWuFZE1K59XvUcGc5CIXFLGQggz9X8TIkbddhvD8fXL_EhVLCC8zbvmXfIGFi2J91Vg7R3qOsH5539pQ8XqbVlxZLwHsc3x4xf5f6O8nOZ2i0fRrDNKZCacohp-lSZclMw8BKqncMMEpE5GZ-Ea7lNV8gUIQDwsVZSAUJTwXYjCqYdua2dY79XafSIvpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c4b40db1.mp4?token=MT9P1rCmYgSrqJBBqb9Lklm2o7qGhOGJOAuIz2londZiMGe2CPLlkRFyubROcsl-t6z19Or_jrsRX1jEbVPwQ58bV1-WjYWJSqLqJ58yQzxnFJLtQvJ-KIQz4GvP2h6h19llbUrEuLa907DBtNM8rDw-nPWuFZE1K59XvUcGc5CIXFLGQggz9X8TIkbddhvD8fXL_EhVLCC8zbvmXfIGFi2J91Vg7R3qOsH5539pQ8XqbVlxZLwHsc3x4xf5f6O8nOZ2i0fRrDNKZCacohp-lSZclMw8BKqncMMEpE5GZ-Ea7lNV8gUIQDwsVZSAUJTwXYjCqYdua2dY79XafSIvpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علی نادری: تا کمترین فشاری به آمریکا وارد می‌شود، جریان داخلی آن‌ها در کشور فعال می‌شوند و مردم را می‌ترسانند.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452548" target="_blank">📅 22:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452547">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/239777d5c8.mp4?token=Hxrp1_EfhQ7NrVNnApWUcG5yRqmtEoTGtVdxIl2E34wG2zQ3SVoirenZnWUDz_iMAuE0iPiYgGANJuZ4MEpxdd1FTVRDcuZPXeqn6DCXv3QuBdCuYSJrfLDtYRzoq2hR782dloIkLVsyREpXkIkv6wetwd3Dxt_7TEr6skHV7Tu9LtUlha0fXsBgrZXaVOqZoPiehGSFYwxY559_XefNqmSRTloEx877i71rDIj-OcLNry_TLYRU0XPqfREwLst8bd1Qvw_tTJOSiJfdJ-KuIzB1KGlGE5qn_QcR1BHjL2gJ9-K2XUmk85iOb5edpqPvgghYdfaLXoymCfBp1-NDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/239777d5c8.mp4?token=Hxrp1_EfhQ7NrVNnApWUcG5yRqmtEoTGtVdxIl2E34wG2zQ3SVoirenZnWUDz_iMAuE0iPiYgGANJuZ4MEpxdd1FTVRDcuZPXeqn6DCXv3QuBdCuYSJrfLDtYRzoq2hR782dloIkLVsyREpXkIkv6wetwd3Dxt_7TEr6skHV7Tu9LtUlha0fXsBgrZXaVOqZoPiehGSFYwxY559_XefNqmSRTloEx877i71rDIj-OcLNry_TLYRU0XPqfREwLst8bd1Qvw_tTJOSiJfdJ-KuIzB1KGlGE5qn_QcR1BHjL2gJ9-K2XUmk85iOb5edpqPvgghYdfaLXoymCfBp1-NDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دختر دهه‌نودی از با حجاب‌شدنش در برنامۀ محفل ستاره‌ها
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452547" target="_blank">📅 22:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=KDe0SPMU_EdiMYtiGODCe2stUPHEqbGQxoKC4VCtwPsFHqXYTlZq-d2mz4q2pjHs2FaaMD3OoEMIoDvy8hX8RR0gz_n4o9_26RvhL65xliK1Gap_KAXH8uf5QRs5QEPFi_xMJbik4EjfEAJdXarJ0_EU8-bJcsmFv9hn2UY0buTaEF0aRJDofSgl0wKQ_BUVkQrjE4abchpOhH68imo7H-sV4WylVY24RfuB9WNnIafFjwvjTi8q1GKlovXaWArOzIs2Twwjl9Nw0xeqOhQhYRBNNj81-b30ySt-C2l9Z1sKR4rcgjA2yEEdyxOx3ILOgAmD1kQLWLOYDy1-utmXHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=KDe0SPMU_EdiMYtiGODCe2stUPHEqbGQxoKC4VCtwPsFHqXYTlZq-d2mz4q2pjHs2FaaMD3OoEMIoDvy8hX8RR0gz_n4o9_26RvhL65xliK1Gap_KAXH8uf5QRs5QEPFi_xMJbik4EjfEAJdXarJ0_EU8-bJcsmFv9hn2UY0buTaEF0aRJDofSgl0wKQ_BUVkQrjE4abchpOhH68imo7H-sV4WylVY24RfuB9WNnIafFjwvjTi8q1GKlovXaWArOzIs2Twwjl9Nw0xeqOhQhYRBNNj81-b30ySt-C2l9Z1sKR4rcgjA2yEEdyxOx3ILOgAmD1kQLWLOYDy1-utmXHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس: بحث اصلی میان ایران و آمریکا، تنگۀ هرمز است
🔹
هرگز تنگۀ هرمز به شرایط پیش از جنگ باز نخواهد گشت.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452546" target="_blank">📅 22:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر آموزش‌وپرورش: امسال استخدام گسترده‌ای نخواهیم داشت
🔹
در استان‌هایی مانند تهران، شهرستان‌های تهران، اصفهان، مشهد و شیراز کمبود نیرو وجود دارد اما امسال برخلاف سال گذشته، جذب گستردۀ نیرو انجام نخواهد شد.
🔹
براساس اعلام آموزش‌وپرورش سال گذشته، مقرر شده بود که  ۷۴ هزار نفر در این وزارتخانه جذب شوند که حالا این عدد بسیار کاهش پیدا کرده.
🔹
این در شرایطی است که آموزش‌وپرورش به حدود ۱۲۰ هزار معلم نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452545" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmE9BVJ5xfUGgS54n7XRyORf_ehpvcmBzr5xlY8WZGbFoE9Vs81QXMM4r81yekl3tBvfYblF7VUQXQYRv8nZLOthnaCoXlFiv2rnCbLSShaJID_cWDpRY3OJ3jeLRqpn1Xok51umCOMBm7BnIDsy0gU8STXeTZwluDMCMDnwmNBVYiYAAR8c2x96pBqTQZJhnz_uznWFIdGcHfU293zMqqXmiRnm9-Ov0eKqd3v6WxtVhfU9XMUaLuZ_6SSMjWNa4effX1GDisansXxejQtA4NE1H417GmPZnInBSHG9gSX9lohqcFDG-lwj47b9SvmCYht8cnpcXrJgY4yS9n8Tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی قدس سپاه: رفع محاصرۀ ۱۱ ساله یمن، مطالبه‌ای به حق و انسانی برای مردم مظلوم این کشور است
🔹
سردار قاآنی: رفع محاصره ۱۱ ساله یمن، مطالبه‌ای به حق و انسانی برای مردم مظلوم این کشور است.
🔹
انتظار می‌رود دولت عربستان از تجربه رفتارهای غیرعاقلانه و پرهزینه آمریکا عبرت بگیرد و به محاصره کشوری مسلمان با جمعیتی بیش از ۳۸ میلیون نفر پایان دهد.
🔹
توقع مسلمانان جهان از عربستان، که خود را خادم حرمین شریفین می‌داند، آن است که به جای ادامه جنگ و فشار علیه یک ملت مسلمان و مظلوم، توان و امکانات خود را در مسیر حمایت از مردم فلسطین و مقابله با جنایات رژیم صهیونیستی به کار گیرد.
🔹
تلاش برای نجات غزه مظلوم، مایه افتخار است، نه ادامه محاصره ملت مظلوم یمن.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/452544" target="_blank">📅 22:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452537">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTELAMQZuzXcIhlOfNVr2UyaRAOTsw71Lo1fqbTWA6rkB-MDWB-fhoA22PZtSUYlEFCJeo0kx0LNLbe4bfhJB616OlGBbqVpGJxLVr7UcbLeYRhtr1wfKJUATu6DDymRvJTyz1vppEua_6uDoPWLL9b_HIBFZ5NJCBNNBfIEVjqnpoi2NhUYD-xeNObq0X6Vq0nhdCKoc2mNe9x6fZBIM1vxpWanH6Bi4p33WMkk2e9obWs5TYClGXZZpbJLz-PZzHSdh-NnI1Tr1WXmtsMt4CjTxycnIuQvHwSWnLSoWv2rQLl2d9dHI4k_yGu1tTDA5ZApdKt2aEVHnb4y-BfMNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC87KZlU0MlR9GZxMUMlbqrPErGrAUXF5LUQNV9fyJFSTYSI5Ezb7CxZdKl1kjPHWZX5vKU8qoc_cvX9fUekuSaZ5TsbUCSY8i_2V6Zn1jDJl20dqpUWKmnF2mpdN3LuHyLF0BXnvGZDra-90bPZvAO_eiInHPGjx6HFWsmoaH9UUrAxtuJqUcemh8C7LHpOC-FnvT36mpop_JRxSmyf7e_P4ZUyI7BLGn9nfScue1wOeuvABy0noOoAmE8snks-eRFtNwiz1idszbQb-tOFj7tY_izSKYXS7YKh6be6tVC1acxf71fSuMbS0noYWpXj6THHDziqyNJKemrmj7evzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJrHrnHxviMl2QV7Wq1Jjr8WdooXeF52dVNjwy0LKno7_uyaLcd8jxFPMJQiOVvkLvqgCNIFcGozFokmJZMMAcH463JmYGhZRvzaJeEMy2tMecDajmsNG1zIsv57pYcZdzVFupZmi2SkzkHRqMo1LYaM9xdSkGbSpwoE97xDKNgLxg-bcqjTE7lScmqJFggvQUw6_CGhwh3anCjFM0nY9ds0YMoNpGUm6-Teu2ETRfayl5x--Y1-6nMr2Z3qwbBBY_xEjEFhw6NXYThaDehbD2j_RSnStmb_WGXW0PUSKNn6fhASBexiEjPIM9LRD9ne7AyUZJB6eJp0NzXG1-jMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRurN8aGdErdqeJ467ViTok2ZFfB906tIjp-D0Ht-MKrcMztjoPmKRbufok0QOxqgfnFQ_loyXt6BfdvvW10yZzbH5snm0YZNG1MZxrEiZx1UmTpyv5-7KfqjbrTtZZnrUTpF4Cs6rzpeTRmPXQp2Qhxm7hW_TAyerZJNm81lcCTJ0geyFiso09QsXpLdYcnNtMKRikP5Y3ioW-iMGd9c1uwm_TEQuKqD8SaR8OrYo1GKIhFSiw158fjTAsLPb9YLDqtMDk5-2x3FmZ0JrwfcpUIoH3j-4oVyigxfvlTHkbIMQHG8gjgGsl4P7c4rQ2XC511WIFTEwnJoRtCyDwFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oz6CE0192BeFIgNZO7R04sBpW-j6GTuNEupbxYmzntADGz59RZNcyInYHjgrkKhrpnCGic2LxIcQu98M8ob0n5QXjU9ElOIVxQDQ6siaPiAkiRd6C7pYT4wcnryZFL6KGHyGW6QVdqeD5v4aiM3NBd8GeqnbSS09ifcWeBtYYwTCZFG5ExWvXgIEDf1M7fXNdn_Iy2BVyfK4Uy2OIYSb1ZfDUCfH1dEKlmUXXqGor0rTEyO52zONYaCs3XqHHWIxjEmyjN74Mp9rIRIFp4y1t5JDYIBPgxMsnoh62qW6M4lcvBhLfSHy9ZN3hmfjakDuZCAlxkTPv_URpxJEpTvXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7jV2y6FTkk0RM3Z1Zdzn3nz4NpWrywMFRZPBd-2gGBGI2kY8a4ul5_9jcJm5IuHJC5tLVDWoIXSwd1guN_gCmgz5M9qiJt9hZ5pDdfj45E_xQmIVkzIq47JhnreVvnbWkSO_tYieZmwJKHuIgp66FLQ8k_XNrGzCjHShz-XKz5gYLJ8PZBNjUKXZ54laigGowG-Q1m5X1zQ3UTMDlB3KG_AgT26Eydf2DF6CJc8efmcbVn6iZ6pBxZ9LB47lD5W7AJ1iZEM1_py3XOq6rn4qXvNuvDLa1FNIv01mqBVoXYU1EdCPynpQePsWbYG6DE1oN8nHIB_2I6Ucw_ifyDR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwmh7KLnYnoX8zh1GHxXoCU0_lxFoHd9nDRs4F1XX3SKSqH4hR8tcUNEA-4DZuI2iBnjAGirVsYD_I-_ITcIjIXuA0Ds1JFYaMupZtj8uPOlTfBaWmVDPsjn9EoXOrVhbHGE18we4kr0IKqP8R_jf8UShN4WzqIzBfnH-3JDPQaxsHcxg0SgdiU0OPhyMxp3BbuFHPBpfPvap3H1J_ecjsjhlnfRV22FcUc0jfzw9bYnXC209KVPMWedafTnNVvu5fXvCnbytt3c4kpjKtkodFySjstDZWmGAGnntZI7zcdnEebnEpnvgBG21iSbsuMz7cPrKml2KcUb2GE-WP-yfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین گرامیداشت شیخ‌صفی‌الدین اردبیلی
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/452537" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
