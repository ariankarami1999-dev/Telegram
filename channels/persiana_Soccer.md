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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 611K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgYaaYBnWFtM6wUjaRHzFLtGO8oS9gzx5wIj9YN3rVKepHmnMoWGop6Itud43n6EMAwDmo5OTId9yXkhc09NKVxyOwSwebSoitRULv9XiuHVCb2Cvv3jGe3wp3Q_ch7jq_QLEvUSeF5tJ24yJa7NG3IWQN10jLqdaYuMLNYhl75iYa9woNlJr4OFYldAKTmcslLNkE5l8nEGKjzbUOnDHZuS0rWuHI2Ojszh7N2qxFDRpa0rBYhD-yIgP7IkrwXIhUCLZLSVh6yx4-v4NHADs8iccWIonX7OXkkhLzKQ8DdXk6OfisNT4_LLXl3LD1ClJffc6gI8LSg8FoaaikFDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TygFC0OghHbh1DZGDKMU-7YuKSvBObKUg2QPeEOCUz5DrEbdQwCH_LEibbJNoxVQS-fNM7ontFLiVpK8nHTp7y8QMl6Mh6AtbDswEao5tzCRe5NQxjDElqxMRoKtCO6dt6VgZO4QlHq6wZ9-7Bu6PUmdauXfjUrN4AqzJf1qSW9sCGQ5eXPr9aAN_hw5ZLKM7fpADrHI6UDKw4hXKKR-SXErXVYRCtgSRCK3MBdPau_elwot2O9jVLBBA0B3ICjG-M-Y28zL3J3h4CNLpStGHaOFqQYyrAprO9xcMEnIyRWcYuRN_PWnhMZ674uC1jlnh2PbMcecRAWoDNwstR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMcHg-jxHzgFYIIZF1vt-mo05SEU605OoB2GIqYVxMXEjI2ZBFnUugydd5tS41-1rqun25317wvUMnQhNMJhrB5YmkbwMxOyxUGYUJVY64ktP3oXwh48jH4bGFbNS9p9hHVitCGryNihZHytDsECEWFFIClqTmPKO-wn5Dk_-W6lmEmA-Srgos7xZYXfBUNk8nCeyQUusySGF4M_7GydBznsvC6SzOtD_s_k2piMq3F5-g7vIeGWDC9obt9AqfsHlbCPZk-t5So_aBYyvD97y-YIpRb9GfptvzaOZkgC0e_-ZpEmHFwcCieU3G1rWpDpCzvaaYCiA8DMvBjM69r5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26700">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QclHNdLBiBVTEbLtWC-zNWhLhbIf1x0bggpXPW8Qz2oYnBQniz9bF40qz3JWJvr1V-j3nCYhuclUISJwSrt9I9urfZr6-7hoqGEEti-KTDhqyhRhnXZPb3Zsr703ZLEWw9qjQ6-DbPZ32R-gjU-b3Doj3tvoqXDLQt30oHgZz3IKis81GJSMd_8LLbQH8GjVc0vRMcZoo06ZfDM4rmnE_UInkUuxJZtY_0Mmw1FNFxHJg-2ztXAFYILFw30OOXaIZwNlW70mUZcmXxXs6N7O3EMlrhBDFI0XPfym2gtinVNzKgGtlHxt5Uo8F_IDdHQ6goxlPF2ahIUbQhrW7AemgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/26700" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZgrqZ830FfA4cDC7KmXrsJv9aPRLpR5dmlRIb7VVuAkABhV0iuH5R4ODfMo3m5odAwvI_9Rqb2DW3BDXO3wDTqfohgVddOXjVTxTd0OmW4T3HEfEn9Mw-K_d-fPBZUX6MShIODUkDVuK7BOgzSFISNim6VzG4r-mi_OMo17mhbcefvownxltGlbmkWoYmxRHd5_ky9AD0IVqzyrQmtaTnhrFdnahuFz_LjaNb9lZrtSeO2QhSi8EjedmItwLuX8q0d2uhBAR-k6Ssd5EFU2Fb025sawt4MXulu3479_U2246wX4h3DNAviiRk9g8D1n2R2s7-twgr8beiYZIt6M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B357tKHCB4INedvy_8hxa-KwJZRMvDhJhZ_eEAFuPjwoDvN7MnPDhOO9SRGLMhvm7DBh-FEUwEt9fDI_1-pPh6nex6-Nq4h_fzrI34i0XYNEZLhmoJFvXZmSwwEV4OarV6WOSLVeT-zwnTYWicQtUTSEfKTSdnYQWpRdf1NlPgczikzDA6pThLrrZkG-RNvDWSiq4RKAKVjRhe-qX2Cxn81PSKYDXG_HCuk9YRxVrmRodW6A-wuGhDCawt8MCz1Zc7WD_-JArB4xpchleRvXpCZdO-FKoeyO_gf5F-DlSLzHbiSfC4-vrbMZR68ethYEiyvrps00eF1EHFmo1jjYug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOM7tl8D_8ZMYk3uvCSXnGA4r_VG-1_VHqagYpNzgjQ9Pvoqh8XIZe1nyz5jSzXMyJuHs1hzela7LIHfH1fbJKXzXa7pTpu3gk0y8b3aQ6BaTPhkThjPiag8PvuKYld7kMDHC4iFpyas_C7W303Cuj4O8Q4UzqAkjCpy3kwz2CxqsURKhvD2qxdbbJh8WbWrwkeN3cRuDQCd_yu0S7u8Vf1ihBJOz1VGB_MAKtpQVLCXelmXCBMjpjQDCGAoJ938piwicj0CC673UQFYHb9g3eTTCD-PJTFl0h905M1jzhqwMWMWjB9WA_CsuUgWGsXi0Cvb2XImqH6qcO-gwN8iuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEZDrSpZi__Cz_PkyGd3Kijqvrla5kmi7hZXTQz13KeQJfgMYP5NCLki0C-5pDEnTse1k1YZ0f3c3n65xz6sMqz4_hzteJV_pS1_SO54WefeC7DE_cybdhNU7-lO4jhKImUzmx5OGSItMFa3uDiLK4lV0WUGnasnp6o7FTr4JLps5y5C6T8lgQE80-2CMH_keFwgD52wqq4obrxMJU06XANnIg79nAnVkGsFeEd4iCuFqeSSY8HMAZoMgfd8YtzECNir1PM7U1YktEF4uObproxvfyr8GZmonZgPThaBho2v8zpt__XPw2QBwToR9DZLuMsYbYB1p-PmoOB6kC1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izdm8cA1pw2W5z-7tJUn-biYbsCzEbXtcC0RPtd5tEZl8odOmq-zfQDVvDdBw_RiOHM4TbQ8bookna-04QIVkgcuoyf2aIU5ga8t2xsI5mK_Ous3_r23exOJ-lv3vAlrJVyQdB9nZvbV9DHxQLijUiBrQSLdLG98sFBTo9W32y08eCRHRMy9wQan_8wgIYTDh1O50y0bOcgfaiJUYHbmx29MqYyxd_tghyFilUV_xGu2QbVMvuPhLO1elVfrGbflM_erkG8qV1EqQPyvYFpdNxlUhOZv5LM36v1W9EC0u0Na5dRmeEkujmiaYQ6Jy__Aa-VPdJHUyk2r_Qi24zMTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=nmoUds6rczoHpOShT1EKN3FJZZc7axDf-ZXKIVZO1bhAOqWvAhXHMaM8YtwpF9GYix_Znvc99Eq9ZQrsPmTczuu6joYnxZExAppk3Dk7VzaeFm9M1rc3g0tttUVkJwOHL9prgG8B8BAJfzqnEptbu1UhdLGE9ESA12THy7rfouxT9g2Ygc5a_3uEYJXR63DcO8jcfV6nzIftafajW_RmiCR5TNlREi_z3ybP-rhNhB9ncf8ASh_0b9lCENjsciOgdX8mGGryId8DCfDHbUGxT-Py1uyTdN4HWCqOQzmdYGBIeRisu00Mxo_3m6QmmHSE1iKGRi4QwSpnlhIUvFs3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=nmoUds6rczoHpOShT1EKN3FJZZc7axDf-ZXKIVZO1bhAOqWvAhXHMaM8YtwpF9GYix_Znvc99Eq9ZQrsPmTczuu6joYnxZExAppk3Dk7VzaeFm9M1rc3g0tttUVkJwOHL9prgG8B8BAJfzqnEptbu1UhdLGE9ESA12THy7rfouxT9g2Ygc5a_3uEYJXR63DcO8jcfV6nzIftafajW_RmiCR5TNlREi_z3ybP-rhNhB9ncf8ASh_0b9lCENjsciOgdX8mGGryId8DCfDHbUGxT-Py1uyTdN4HWCqOQzmdYGBIeRisu00Mxo_3m6QmmHSE1iKGRi4QwSpnlhIUvFs3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0yPY4D-v7YPaAXxBH0v82ESKkI0qH3bU-OmLZQkZYDfFtUvYzptSkGOvtYZ9bgKsRdMxS5TEzB43A4eJqI_eih-W7wLsJkUbAVhMuh5nqnuS4vmnwMDoWa02AVQYCFElDAjQ6b4pc6qzQ7fWSBs9ZHNyPeuBf-J6VnhnENa7yduQy_SzMTnkteaGt3BS3N7sQNMPb4xTk36-xSQ_tslGKfiDN_K0zmSvBLlTDcVTu3XQKOB_4qPA55dmPU8c-wZTanTY9jlbOvbN2w5fsM_98D_jDgQsXGpv_M_5yVdT2344a1ywqCkzYOfeSabS4_UX1m9IL-kcTiYh-DXwhkOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYqoUW_4JOCrDIdea6eVgBK3UuqYLILK5keZk7AYm-nmBQDS0qarZg5fI5u_NaYUECP6OGdxTF8bfCOeBleDR1CnIkbg6gudYWO3xIHyQ0xIttcry6amx6dS0qMMJl5CQysJoT_ekVZigY7hp8kzabOtnICqozbuzHdIlwK1xx10mjn6gXtbcu_TDAZ3GJPBerb8A44q0n7DRdaEfUqjbv3vlHz7A9btJVG8dA7ouZlEAsnGqC-apNEVLru-Q3lQVgrrnuTPhD17nGyinoV34FO1APOx4gN55fUanV57wZRwJ7d-pG4tSmFCNOpNMHuZHKzTTNM8pagkov1pqUjg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8LKrM4_iBx-NhmGtl9Bfs8dQJxstM32T0gc87kciglmArUaiLEdMpO8NldGjxHtXojfFFva0sJF7LukedNGj8iR7EEgNTYlJY9k5VJ0s4HULPSXx95xf9lucET_iq0zMIKwYLyTpAsaqIlJOS-xyqjC6XnlKDz2XoAb28j90yJokEMZ8rHo-OadKs_jzgFZa1bPqETLE-wZnLBDiR7G0l3u0LAe1G0C2dW-OAMP7611fcNQOKdDYc2QW3wtVc_nGh3A2F6gScjE8uJLjY5oyCk9oQz8iacKn9vD3IOsUKpLNaA-tEFC4hRkTghkGnNHTHosQD01RS8wYzdUpiP71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=r8IbanOygJJkEVJ0KHmIjeGV3hI1eJC8BPnpbpSsYO6PYbmteBz96sMkN_HgGoTHHL8m6DMhyCWNQxv2iClkHf1jz4vtoARIBoY6xfZ_i91yT0O_Mo_RNV0EtAVBLIIVtIQJCXQ5tRrUsuCE3KIeEAeHv31iAoAjqHNgvtU7xp8EjUBlrrWs4MzcSfxwqkHH2zR4p9IXMtDG7-CGo_3Mb2oSllbyprCqYtxZ9xHFphBCgKVaciEbJHQEFUhAPrBMDf2LyIroK1-59M6ekuMlXoJdpf-OdhOGJErHBS2w6T7LW6BSu3SZxB7djo7lGedMH06a56V5sUgQGfZyQJuDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=r8IbanOygJJkEVJ0KHmIjeGV3hI1eJC8BPnpbpSsYO6PYbmteBz96sMkN_HgGoTHHL8m6DMhyCWNQxv2iClkHf1jz4vtoARIBoY6xfZ_i91yT0O_Mo_RNV0EtAVBLIIVtIQJCXQ5tRrUsuCE3KIeEAeHv31iAoAjqHNgvtU7xp8EjUBlrrWs4MzcSfxwqkHH2zR4p9IXMtDG7-CGo_3Mb2oSllbyprCqYtxZ9xHFphBCgKVaciEbJHQEFUhAPrBMDf2LyIroK1-59M6ekuMlXoJdpf-OdhOGJErHBS2w6T7LW6BSu3SZxB7djo7lGedMH06a56V5sUgQGfZyQJuDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW-QpSOMkBtsuYc0qeOlLH72-tfv9qfb1ezWpFmS8JjvmSsm-EU8dUwknxWUA3RXimabdwYO2XDlxBuR-sz2YesnCL6A887k1h6G2FQeFE1SN_nxYXuKSRa07eMoirksBbp8DLBS2rbccnjdickJA0Mbx0IYvJzGnHwKRMhi-6hv9Pwu7vbW0ibd-nM8a3bdaBsBCm_i4LFKUB5h9nKQiHS6c03IVQDFp7I03WCmOpsrWdXM8rk9u0JTC78ADP_UUUNAZ9KoC2-j3qxu0VvE83SgKreBTcVsXcz3qmrWMoWDzrlnti7LJXoQ7HEVRznPSodjUw9yF8pyyYwUCjnGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3fWqGRMGuV06tdwIHXzYzoH_-KMhDpgStENOjEkFgfMVwCquCVxL1NyO4fSKo-FXEJRprZCTdetHLpF00O_xzQF9EPM49lJ3b0NUc2Nmyhj19WzkdjQJAu48pDyiiY7X9wKNkRki_I27uFkiNXPzgisg8q_d52kzyqgOCyDr0h6Yxyb_Gb2PZrrigiFon3ShmU4vWfZdJqccFxW3nOi7YLvJdVV7RV2XjHcwrmCKrpS1GBo4YHCf4WSeB_f1emw8x6Gj0Zg7D9NvHR-k4qxVRgaS_XSpo3yvDFrzjDIvfp3G9ooISVvVLHD8v1Mf-OhV6tJRKWhaBBjvNo814p0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJMZpcLWgyFHxk4FB_kjFHi8_C3HGZ2MCtrux8jfen_S7hmjb05OHc3Vm14bBpG2AKG4val2pKqTGbTQgk3q96SiBKP9-zEfiGE40iQ9StF9HTdIpJsbydWrZ_t_FJlybO1WuBEBCMxaK-_OGLq-0a0bVewSnFVrRkGJkDRsGxJG3EV_X7wrmWob4HrZKS_o4RMYEXRr2F4m5nsk96Df-uqiQJImdblxwfQVZLlQQz-xlAF6REdH74yGmrVCWTaAsUDcMMmGdQnkirD5iRBOe-aogxQmIgyoEKC5E5tf5mrnpmcbZj0u7anq1biH_3QQd5n5pflaS-cEcd74nueL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYqaXIXvwEOXFYptnQHQQWKwEk7ip5sYroQGmG5A-qVTwns_uokgT_DtbIAtvtLsIUYuB1AC8mnuU7xBSZHl7f5oRliyOrb6_H_-ORj39XPpUk7DZWHhifOrIIyGjxhPurCN7IIPSFDgO3hjfY8Xbjbasbk08RFMfT7UwJ-C78SxOcaHfOCa47pkU7J_t_-YRaHDveZUg_47lc6VrtgB6mjyCY_sRQExzHyhfUA8gRqgjDgI-t17fl695-c8itgiFJCMgXokFsZ5jGIm4tXGFcEIUtkfUy8MBSSoGFZlHQOvKgzge1MDreQMMTOnq6JCZASEiOi1IX6ZEve95t7_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXw5MtLHgvgsQPetDJObSyDcRvV1OLByA6JBfgHWx_PRTNVKJttmibtVToK0OjNXDVfxSZ6FM040LemutNd2blNQnkGhseVLxDCY0d2dLJSUza19cv53f0xsiy9IqhURGCfvbMepM0ZHznQS9HpNU12fWc-q-ALS3Oa-WOhpDzbjcIQ86OhfvOhwSq9vcVTL0QlJhtSbT_DfDaqVgugMBXCgRkuSv5FypW-7VeLvG3sfHvM2RqvjT4LU_L6GagORu6_jl_3T2k7387ElYzgw87pN0smV5t8yc82_-cJyQICw6m2SnaCMi8rKLmPUZ9vcqRg5EJCfWfygkmq5a7ornA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnLD1k3LQDhoiQDI8E2jjRj2viqnyjLEZ6_Oc4vU0l01UTIOSHutNTJJd6nJgl1j8o7cWDHR1KSs-h9wFUTQS8-KNtlP23EtcmG5QWEt_QS5LFcUQegcTzTDJ_ZXwM4V2pHhqeSjDsBzRx2Kh1pbGagI_avKYKdoYAg5_r7Uy2ztZOlxvJ5KRd_hrG2P__h3ih40uAobEmvkG8qLx8j2YJQV5wO8MpjuYZxi6Z9Jxz0ZukxRIo1igvZMGMonLtXTA0qRkQ4FlcnioXKK4Bylb9rjZBD0BmMVSwIrzPcY-qfvEhW95M4qDve1CD1xvJmRWiBxS9ONYD2hByRVENP2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4AaVFtqXtydlyobnuiQKV-NN3p-Wg2EdZ-DI1Qk0lmiH7M6V2ARfh2zlBgUuszcYRjOYTIA_NnWv4MDN3aSTxlwqYSxhr_KXSbuwqL4X5ANnSeVSomODAOj7X1qBUihr3IqPIA95LngYWY4q-H3I4juOOqPV1EKJSYCfl5yCEAtSgmuLR4pQtnHumX6xBjmEROGBp2iBolFW8dzsZZxISRKChtv6sY1ZXikiTf7xNEyWEjr-foNQyYmy6c4K3FudNDhkcNZy2sI2GD6r8qCahepDOsOKXw-cYqw4aUTEw-hlo0DfjdS89NatLQml5vJ-qPYPY_jkfwGYhbHUPBEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2tYILvFmFo70hzR9P0MNyrj2E2LpYpbLNG2AjkWsWjYaj0IIVO5kVCPKi3jQCfCuXTvbDYgFJ8-k4YXbkEbN8Z8BOmOawsLYiq5X8kqyG6Lr-EYDdgxRePQCOY2knr8jUWRm_TdEJQ-7qYzY0JTYPo_bgIT_nH8WMP8l-mFNWrsmzcj7PrXEOCTz_ebeq61SqtsUe2Ij0Rcu75wv1Pop1P_KCENcGNREck4CTU5__PYl-AWQgMKk42mwN8k4t8e-W-yfPGJlmjR4vrPlG-nsEpedAPTOgJZ_lnYyliuKPcyNSvD3TwP8WFHvhhKpSJjSHk0FyQT4GBwbEixVj2ZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-jruXWwQac-cDhj01TRfsoiIlgfFRyL-MQRXAiPhYaSZ-Mj7RR0XNEMM6QLMxHFQaMneRjXcPrGuefXZZHLBiGhijx5J2gA-viYYACDcAO1GSpBqQ9Yn522wvi_-PTdbmrAWRJ2XP218ZcWPskA8UqnP2hP7nQZ4faxhVGT-PhPdTe0iMUIkKLD_-S1iFTO9XuRSfG6P1bPXzuRDshnJjZxbuS_v3GqT1GoCTumjU1U14t7Cev6L9yCUkzk-s-QBGyRuPh8E2K9MlIJT7Q0w46qNADnKz1fKBQdYthRj3hMkWpeOIsUpjLsXuvfI4XGnGBWy5qRgND-3pp1mqKvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gioTHkulBy2ba-rQ0koi4FZGYVRXh6WSOzneU40V36RAq_RJhWkYVUwG6ygUKByTpMFQfhSobaDTX2yD1DiM0rSrWqtDIqpdrkDpW2hBrCemm7erv1zyrxRD19eAPVWY_j_qEWdzGNQbuP2XAtqE5tY85ZIsiMgTotj2RpTVYpqZlKSYJgjFtdvcWSQiOh5dzBEC06zmMM5xZIq4htBfv8EaAJKRPfGb6qvg5to7ZKosFhegjYI9PjZRXBh702t6MMJsAxJ4mx1vmLWciOxM3yvqyd-mIremH6XwsEGP0MH3hR0-TQ5wORz0OlISSzBZKEyHbhH17NvJ48Dlv1ikTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_I0HK3_siwNlgg_UEAeL1uqOXcr0TecIV96vcx395cL-cjAcPbIPdghqg-I-2kjx3XSnxCmBpKt54sAVcnbil2prkHXD3klDBQVRS6XKcldLVxxWWKcxLtXXxoOleCp4Nvc_rMIVrmpMfbbxS7EUok2BT_QupAy70VuvMLyIQNUbHYOfMkL0tf4t7KFgKQydI2pHhHwiMF0M4GO6srAA9xoEm-aSn7wtPrdghYTgYc-N-hgvapo6bZol4gHpSjViPVoASwBaiKLZJHRcmEjm9P29OkgrWETwzcRMlJ68unhXifwv5oIvVR0Z-l_EtydPUA0IuSWcD_pqtwueHlbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfAtp2NwqpNorMP-c4SS7esh1sMyHrwpok8DH4sJZDPMS8VLgzULZjqkXY5qjiHNzW6fy3MKz9SmgsOF52HyFDpmgIVxH5cydUHqnXoxi0NTatiAkGBF0pLfGYL8PbGPsJuT2dfLS_40jRXSbPMsBy-sgiTR9wCTUOa5HDMSWR50QcZSg8Y2WqQY2d6eRZ_8ZrTtLH5B3ttnmVP70ijPoxOq0EDk_qTYWR7qKZcPKCLc9ypEM84vfW6FgtML7E2CBfkZso0M5gaZvC7xoTXXm5IrodFHxQJolPCnU0A9Uwt6soTAk4zZyLHxFxYcuJhOBAS-2clICzGkPTFJy4G6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKnH2uvswPXzS_PNqzKe-u9Vmq4PSC_dGSxuC4JnincKNnIwoeYb3FXx90udiq60dfjwMkKEF98fbNQv4LUbsVL-bb--CRoTM0Fb8A9TPzoHbXEJOOw34FEB-NnT3MDXeFWGW7cDMwz4BbP8jpuWLqwI27vDuTCqBVIpwTvEbC5xhsqRnfqroqPyu1xD5NwzNUdSWWaJbqcgCu6dSlICQbGBlyYnRWPWb-d9B89TTVG6CpIu0TelhsVosQImLjtXfEbco9Zy3nRWpyHx2GhFJ-vyfW7zhHwFFmOdWsDUuQgaub_fPMKTYnWIJ8r-66iE_E5ZzadSrGiLEMTP8t-wyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6BHKnm79gjEBfJ8ElbmL9c3CVsNuGgXIPTVkdX8zRg-ta5vFprBmN8mMTNw-XH0RELajr3Q-PuB2i3NS-aOOygbdZMRtey2a9c3sAaq-F6Lzuc5cNmxHRXJaT4n7gLSod2bzPsvqGq4ORUK07GVsl3r-ILMtKBcb49kN6X8VgrN5Bfi9Z6dQd00DI7QlGe2C3doSo2b4GpC_jSpgdwE8fvdeDQAUhkA_N9gig4AU8LiJiw7zEul6SUzU58EoJ75Tohb39ZiuuQNW7rIjAfe5PBKglFS0pz3QzfqrL8iZxwFvedcSzILQUTI6qcU-qjbiiFDv_gwPRgI4DNDe8VFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIwTSOWrBNNjqbgmjE0Puzcp-fTcd1s93gwBqkGCeFsZG9FMWHmc4lI8QhI1z-5TjqI2LQOD_cGK9aKYk72NhwRZ_jrqIa6chUfbEjY5_HnFbOAASeIYvn0ZDlDhaSs5j1eRPmBvYyaslIQm9ZxfetXBINmboU6ssgx1CLhVd380q0S8fJfImk6bXmnzPkAXXcuDOW4MPAkxUpdOo-DUeg_VAEewKtPxsvAE-jZI9KzKCEYM6T4ImD671tD5jZYfG24urvJ0XjykAbYKNhkJyRWP_TbbsKll56RpSbUq80Te5TyGNeb72wHXCqga4F3VZaD7-Cl6Ju9bflO5QkFDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq35Sgnu8-uBWFRQg21Oo8QtnYwsVKZOXztQuRNBY5zloy8qGkZWkByWtp0y_02GZHr23usw0ltP6vyOkJbvL5PoT98pxGM70v2EKLkGBqD3_kLzZN5p3v0aPSFSZ1kbqteokVzYbWlFAa_FP4RTenPrDHA6o-bwjgwFMZERiAyr6JWTKF_6a9PT3H-QdhV_V0it8FUy3ZmKA50zEPMmXALhgX24KKAs9-3sln6xzt81t-5Nu2VW7EhmC6y8ydTV55XbqdUQde-Mj22dskd7lJue0P4aBZ0mH0fPGfFthB4YcC3SAo2teW4Tf9-hYUp4Jkop7yECjnJ0DQkbem-ZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH2la9Fewv550c2XredFBbeEOExIdL8o-tNu_nqO3FuuUg0ZmbGfIxBO_m1k4MSbhnotbB-Dbvdoj4W0FEznPLwsTIKOoDer7iRMSoUpTQaqyu0wXKAkCM6jjxczG3hVaKgCapIfPdw9Eb3737ZNH9aVPpvCC7uf1cdBUG9-x7DIFtHhRDMjeF2j07F9YqgmsBINZmgoJmrqByPf6ZHfRnMSlo0H1u7frn-d7pswspCfUY3qFw0ch6WD1qsW5-x5BaZ34cxEzbV35OFGypqVzjA9Cd3OlRgzYzH2CNwSl3uuIyFZtzZSc0TYprfsfO_qDy1hYPrSHJroMkCWuvj9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=QmJBVvw91SrfGJrx3dW9rDtF0HppUm5LeLy7lvmdFRpmAWx-trHEyIkdpABRN8YNTKFweX3JncPdgkEA8lkCfbG90SqvSPyqCFkidymwK1OOM-Jg19BqY21PJ0pgdHv6u_uzwcm0QUWuyFksWBObtG26Nd-6ZEIy8xhgmgFi3gwTa0IwEROPjec-Bxkq7uFN325KSqnX-QMOV2G6dk62bKCMBjqW2vrqfrpo10fpaOuj4YmVgMgRetpjn5bzWDFn-glSZZnP5LlFGgdWTkHQtirqepoQBgdyssJA4MumHAKzZIrcfu4b9lAHR4oiXU9HhnQN4pxSwt6NpBk4tiHvZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=QmJBVvw91SrfGJrx3dW9rDtF0HppUm5LeLy7lvmdFRpmAWx-trHEyIkdpABRN8YNTKFweX3JncPdgkEA8lkCfbG90SqvSPyqCFkidymwK1OOM-Jg19BqY21PJ0pgdHv6u_uzwcm0QUWuyFksWBObtG26Nd-6ZEIy8xhgmgFi3gwTa0IwEROPjec-Bxkq7uFN325KSqnX-QMOV2G6dk62bKCMBjqW2vrqfrpo10fpaOuj4YmVgMgRetpjn5bzWDFn-glSZZnP5LlFGgdWTkHQtirqepoQBgdyssJA4MumHAKzZIrcfu4b9lAHR4oiXU9HhnQN4pxSwt6NpBk4tiHvZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26670">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای بت هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26670" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp3IsqscX0dTtbyHSEXZDVEE4nZ42AKFso1H57mssfRbdOmZPZEE0ITYqicVCTZ3SixM6MST9Dxs1l0VxcuDOehOErdWVYwvSxv_pNZ2FrIzxGLFXONyBRHFITV7OsVtsrtJGiMozTYWrsngfjgWaBnmSrjm5XFSkZriRRrWIV3-l55mAa-v3ZViJ0LTU7-6NyggFfQb_7QiXPy3ISSTVtwBoXMhWiHzcV9PjdXq0v_apkCYDalyQqQ96ZdCnO9TYA61swZh6UeB8M4e_rVKt9O1fwtSMUitjRMh1yaA2idJGLFdGlNrc7axwJXOGTZP3-0b3AnHQKY0yrlEpPhzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4SczvTLZnQPB--UaMZFUaAuferm5AYK2OkQRDBumtSdPGkOfCrV6duR8U0fKE4f9_qKOFbhrt2umNGtw1ZUZ87jpmyLzjkkpSEkciHdT4AeG6SYP9D2MpHq84LpPWZOJJUjqZToyQY8g-MzpXaGc2XYURm2RV1_AwMWbBK-ckF1sAOImVj-JBT_3YC10bH0BqUxcEUs3_sdSXgqOL62Wm0KohkMunxFFhX5GLyVWlv8IniBQkLHZ2ZI-J0A6lbYmkuK8AdcqXQOMMY5O2_YnXa21atjrkxIWYXBehgjCfQT0lt8dqXUwvLP72HINb6aD342txNSFjNUDcF1iA6T6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1z5Sz391KUDJ--Opal7FfC_6HUB5enBYnzmVi-_o6GAbnuO7-_3x0ZErdDco00SaWf1861lDG0vr-QzbT9h3GKXFyMSzHPRCiD-xenip88L0lH5rBvwihUoIRvpY3PGOFr3sqJPsxx5jNgUWvVMRxHvDAIt-ckdsqtkHvVprorcEg5ZbEQdUux65HTUroZBlDlDdm-RsZLnEPJeRHfHRTHMwNRU4xny_MD9plI7QGUKYpZf16Ryti2ARPFG0jVA2sw0Lneafn8TAzc16WSH4zi3Q0WErewItJNK52OKBf2hxCquJU6t5zVu5QuojiYQ9cz7wvcK5DWt63uelXAXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKmKYSihFxcb5BcRdtx6UwtoLWV2FczP5P9iuHA-erVAbtK5_MDlSUlcjCjLvSLMrY6wTGQlQqxy2ZPzfi5_eH8ULmwA8Higwa1GTekGBhix80AVCrYU4VZG8IoIIIF1FHtjPGf2UIIgZ1QFj6ilYXylHhWoH7inLeRpPJPiZ1pUR9Gm8brCmcWIO5aDDTJhjL6Pn1R8meFpDDE7trWWGBACM6Nik--Hr7UkHGNHXEScBEDeTyIhAxion5W4Q2Km1lpFPhC33HaHu3r6KnMXqf_w3BEjlGBjHxFtIWpFtSEDqafup5nDDE_E3I2rlFms7fb56ycMz5kY9bQupNQl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWouwpLlvUekbUK4KDUPuZ6-YdX0WylQV288me3TktQW_8GHy5K_S_Bzo1HSyTghcYtYqRba-0bSfv1UVEHPrU2OirjqlQTroueqpmoKDomJnEep3Y-U7YKxhEEvt0QugR1-ycIdwdCeESwc-PwwZjRNxDk_KKpTHKuqxY9TdJ_wyYsU0wvoOFS7wXpYeuzX3vPLF8BJEXcX-kzEISCnIoyUqYQ4WPIrUKnDhFxswGKIjzkqDouxBhysdjV664_dsvgvj3ycXQyOyQxkIMS7R20_s-IqsvOtSga7uQIDHRVq-gc9tFO99sMyEkmY3vas4dcKKH7Z_oEyPmS1FfQd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHbJGP557MJn6kXmshVxbkwpuA--j2UkdKrvtyE30uQxZG_VW71mElKGgQdjlUbZXPVzMUJ2Yj_J8daiAv6VssJCIoPSAJFRWQzsXl2-BJlBVHx4K2l2EgCTjFsgwpOXkK8D9qmqw37WZVIsDhEuCg1YEk4VizdmC_bgMTtDmFt-Nek0wXygf3tMbxDqYc8xmb7ho402WrfPgj2MXcL0Bw7Szyb-Jv6tjILYMXfCgMVENfj3qWdLqrpFJK1hQgtSumQOplKK2D7_aPzxt68cktxXLkNncogeCmYV9FyC7_aWIWy2IhTrfa_Tpol32boexYevOvanYtio1GJpLXFJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw2FABgG0afUcalsMy_JbzihtrQIaqmaUeZ7CfxirUrpsBv6nvwklFSvSGcXSiw18OLDkqNZGQkfkg3oipOX0WrsXFAXBrvf-6FjC8j5bJOtRFrDkY6vCRzX_3owmm1vonmQeBwONr9ygC3Ztwh7bSnMEgHu_Oo1vN4hqD5vcbpnZxe2a_SqhzvhcL8e83Hk-7lSTDk4Dwmpom1jELAakF4vvoIrKy2opEjllWOx5VanhmGhHtUykOV5ozeysAYphdiOIr5lgNVViXo6XdL4CDqlfhRXtUh5BKP0F3Mzk232Gi-zSImCrMIh2NoptvJkHaj69AZqLW3HcvtEB99tGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm3zLiSe3sI6mny6F0aFoAG-p5FD9gtG1wbWmQSGttRyxv1_BrIA2Eu23LMpqtD-E7hUcnvQ8MpeU1ZXFbVBoAuV6EKoAladluq_7raiA5X-QsDEeWcRwdxcq-axTFcgLOf7AuvUoWXbZekwcYFRR6UTx7-xagIkjTJNcQArz2jLWZ0w__X4e7CtvJyM1YC7fp112GLbXfP4chZf2Fy33xAIfD1UuwJVVxwsPXJRV7EKfUH77PmZ0StrUHeJBDpZ1puM3jPPAuuMWw8w7jE5-34PsLo5OA8lp1KVQQ6zMQ7xLcKnhIrbtU1RdhMh1jWFnMykje6U077wMW6yYtRmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Luj4ImWq5Q4BabB8Gd93b0JNDJATuEKf_g4h2Ap0KADEv9JXMGG-0Riv7ng1xYIeWghr0Uz3jGVnZ6x1mAkPfMdRs9J9JsXqzFym2sM_HZyotaR7kO5k5JZr0IsgLy9m5cVZwnvHLWSWME8DsJStwEJI9N6EeJzliSHoFWHgkpqfRni6I19RVcK4X-W-NHPQ2CyCmprJlJg5KrW9NgFHHMyXMMuu2I8w1r6cujPG-d0GL7YxMcow47kEgaHPpfjNCIMApOLHBS3nhrcFavgqAqVBBv3wSgxKWrZeC7_Kgsg6aOfhYtbMILnR5RcrzveKtAUkcWZR-4RKFeStp620Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=eKM8Ep0tCccTO7E_zyFnOtYqrHAbC1oPplZEq9KnU_BOpxMsnNwYBXulKcIYUtuXYiMPB5RhMr5swYXhRYvZ8uBNCMQL6ncqhkyahM_U0rVsCe8RU_s3k3h63JJV9CtA153wTK-zwQfLxrcMAGzQmKPA5ReZCoTJfhn4IaV2YD5rCdlYCbYrBcvjNND0Gtmb0RQg5aYE6h_Xjl-1732jKNRkzKy8yqZZp6PMXbE57oNJMu7ug6BsWLNo-tlE4thHCZNtwHdZ1xBsiDaS561YKVPNtpsHPDXUD23AC_buXPF2CanCa0CrU_Wwp_JqSRPS8Fs8xfHTLcW3vFP9uI7xZk-QWBbUG-FgtLCkFShWqUB0VgfVdiSo7Tf37oOFrUpZjwT25uDfzMYjIROdsdMto8VevaYTHJBMrk7EV84LmGgYvA-fhpxhSAWyXrhVjO2oNduizrntRgwL7xY3mQwVRrgxCzdMc-FyWxMiebTdVJ7r1cLPu0cwN8D69mC7B7bRdleLIPKE-bZtyuAUsjXFOWVxVcj35ohBEEBonKut7GBMb7bu6dEa7PJK4Rmtb_UHhcIbXTpJeUogL_d2NlX37A9Mc2Lb4hh8OhjUgA1y4eikGYdIr8CnoAVCCsunpFVTaH98zIqNAqNqntbWx4HgH6eUsKFSd59qKMhk2umhkG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=eKM8Ep0tCccTO7E_zyFnOtYqrHAbC1oPplZEq9KnU_BOpxMsnNwYBXulKcIYUtuXYiMPB5RhMr5swYXhRYvZ8uBNCMQL6ncqhkyahM_U0rVsCe8RU_s3k3h63JJV9CtA153wTK-zwQfLxrcMAGzQmKPA5ReZCoTJfhn4IaV2YD5rCdlYCbYrBcvjNND0Gtmb0RQg5aYE6h_Xjl-1732jKNRkzKy8yqZZp6PMXbE57oNJMu7ug6BsWLNo-tlE4thHCZNtwHdZ1xBsiDaS561YKVPNtpsHPDXUD23AC_buXPF2CanCa0CrU_Wwp_JqSRPS8Fs8xfHTLcW3vFP9uI7xZk-QWBbUG-FgtLCkFShWqUB0VgfVdiSo7Tf37oOFrUpZjwT25uDfzMYjIROdsdMto8VevaYTHJBMrk7EV84LmGgYvA-fhpxhSAWyXrhVjO2oNduizrntRgwL7xY3mQwVRrgxCzdMc-FyWxMiebTdVJ7r1cLPu0cwN8D69mC7B7bRdleLIPKE-bZtyuAUsjXFOWVxVcj35ohBEEBonKut7GBMb7bu6dEa7PJK4Rmtb_UHhcIbXTpJeUogL_d2NlX37A9Mc2Lb4hh8OhjUgA1y4eikGYdIr8CnoAVCCsunpFVTaH98zIqNAqNqntbWx4HgH6eUsKFSd59qKMhk2umhkG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4xAQ6KNXO9CfaKO7HsGmS3whreast0lQttRQsXsJ-i21kTmgKdiYLzgGBAwLwquYgX0S2HR_SpkRxGzEY9IzsJd7r10sZjPwCG9Wo9GAgZmlZcPUiDrmHtehQn5EfUYbfU9QFIJUXgWUcBL0cgQ_zwI4LqJdtJRvqa3oAderxVkz7iMOW1UaRG7L0pgTe98Km7c-YsUrHUj58xWao1LKp9lkmV0xW3t1WvQ5qKd-yGna-IFR_louB_lNhPSOuVVPusZuQogkx2uX0opGErsBiiUBk-bA1sqzkU30JgmC8bR61VicF5W5czUlAo0qVNjtCxKRm9InicVcZkuC1AMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqFbqQMS8IsfoZFGDKo_pp3zoz_zqbH8ZyeBmt1kluM7dhsDOY8rn5mPqvgQAe0Egup1h9LvlL_YDZyyT30FBlWPt1IM2r7WHnoLsaDHYZZf2ND7mkcQw3TgyDsIwl_8Z9XpQ9u4tcXQesJ-OI1kPZbYX5cBSZsFdcS1W4k8FwkrUX2msjyNx5bzWBEHhdwutfuG7sx0V1INl20JDMX_iP9QK-hvFtBbJM-COR09SiPzaGj9ziFMB7pgtHkJI17acG7KYvR-VcQqzQfD-5gfBvbQpFpC4Wgad8ada5EBJyI4s91O4lbSI7ZEsVfS-5xeXw-J92LMaCK-eRjEGP8cPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=l_iuRu0AXBYKNKfDrj4fAWKrWliUmu3rWKY0lgFfo-0vhTtrofxXcPCtW2V2JMf4Muw9v7SzbxufXEkemUkkknCCjeuInk7q1Yzmrz8AX43DCMG6GyE9TUPeQSjmaS4GEi68EnCGpsc1ZZJi6YF2jZej5PGyzifT1QTNafi3u9grr8R6hAf-r9xTBOaiCeE-pubQMeB_9OPVzch2AE0e-4WJ7a3jeH-7dLDD-4DUUuE45zGwIvxYR5WrQSfh43RVz3JBTMgVcgbyLQHfTQdQiJxqhZtgTKlP1ZiSznHGWL2BcLzsASO4zb8iYxW6YbnX2kFiM2XcKRbb2_A7blV97bsRlRqZA3IF34zVdkyODzC1-nk3xyYXEEwZyfFokzXHIMH3dAP_ffXq1OjCMvNPu3vWOwuWHRnWj05FdGo-paWWQ16cmXwg4ufgA6M6su__0lOM_YEi8xgWLgPT2R-unvESWbYwz7AEtbOcWUgHWQe1SR4FmNhtQDFBZlM2-8Rt5HD_YQy9rBK1z-RNAMLX5XW7WSX4ta7x-TQbU5Ruqw2YL-Wou66Z2a5HPGveOioEwIUD2KyMAoXQNR0IsiTIQg1cQIdUPaBYZ5d14RHsNO9n9PslyClHko40e77q5wrBuaG5CRyIjFW6-xK2jwUy5Opt4fI4sZEbH9-jMHC7Ey0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=l_iuRu0AXBYKNKfDrj4fAWKrWliUmu3rWKY0lgFfo-0vhTtrofxXcPCtW2V2JMf4Muw9v7SzbxufXEkemUkkknCCjeuInk7q1Yzmrz8AX43DCMG6GyE9TUPeQSjmaS4GEi68EnCGpsc1ZZJi6YF2jZej5PGyzifT1QTNafi3u9grr8R6hAf-r9xTBOaiCeE-pubQMeB_9OPVzch2AE0e-4WJ7a3jeH-7dLDD-4DUUuE45zGwIvxYR5WrQSfh43RVz3JBTMgVcgbyLQHfTQdQiJxqhZtgTKlP1ZiSznHGWL2BcLzsASO4zb8iYxW6YbnX2kFiM2XcKRbb2_A7blV97bsRlRqZA3IF34zVdkyODzC1-nk3xyYXEEwZyfFokzXHIMH3dAP_ffXq1OjCMvNPu3vWOwuWHRnWj05FdGo-paWWQ16cmXwg4ufgA6M6su__0lOM_YEi8xgWLgPT2R-unvESWbYwz7AEtbOcWUgHWQe1SR4FmNhtQDFBZlM2-8Rt5HD_YQy9rBK1z-RNAMLX5XW7WSX4ta7x-TQbU5Ruqw2YL-Wou66Z2a5HPGveOioEwIUD2KyMAoXQNR0IsiTIQg1cQIdUPaBYZ5d14RHsNO9n9PslyClHko40e77q5wrBuaG5CRyIjFW6-xK2jwUy5Opt4fI4sZEbH9-jMHC7Ey0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St-uYcbinAh-FeGacTf7h7koZccO3c3VGYhAUBAbI2Il_nVd2tJtW8PYmwxj1DgdBMBEDvd5MzwCjn6pJ5-XzJ70qsZMreNWwQIj0h2mr0rdOLLE9CSZhTKc-qpsOjnXDNcyRbrC8kz9Du0isn_P0LheTWu2cnH7_zwVb4yi6eEYHfWDjCBu67zqo4ax7m5fG_0RLdGBLw-9ekdk0qKC2OaHXw83pgULP2hdSgNUNSndyhpuENJDSpUXYn19gIKGo1KzgDa3e-nDWmd9kpy3PsC6AarvY-om-UNb9ycfZPH6cHdEvX8Enw9egYZz4q-w3cOHPig20wSX3TsgE73Gdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BudPLWttiU381lyZKeTuQdKYgqppiVSB1LNkdUln17c1Nt0FqIn-c9-abiJgQl5ZkfuRuxv6JqS8ouPYnnR0dYqxsOsyEES4KrmmILSS2VhHSBBG-EhKeOs7UQyBrQFxMsuirqaXHpe5AJ7eZXWCR9IgOxqmgmzIg7tOTER8pygK00o9Fki58W1k38P7iqJww_2bC45LzgFoHkk-xgLRFHGCT4laD9_AK7tA6hVekHX7AAae-pOoOIySbx3MUP189cXtKuQcZnFydeDjamm9kT7-dn8dSwivMHBzlEk6ZFnH-aemBAPIjgrKjyT8rJ0e5W4LRgRr0jM8SuhmUWgumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW70tAP9A0_0O8pfUryhs8obk7jbx1eP7-Hacx517_jHCfnMq6DxLHhjW1MCtyV5SEWVDQwbbLINR7z3WrSfLvyJNxXlcodYnl1GxKH5s5hgFOIA3RtuBJZf9hWKpYa6ZIMpjb6EHida0_UqtLG2tW9Hl8YqDsHalifNOXDCvu8yL6wdUPDTGBtnNNY6Ahnq1dyfZeteK0exx_TPsOB-Mf_R1yUqvgpzqI-7_uRdEqzs70wqjxdn82924z8M8YbYvvNIiR7Ae4Iuc0hCCSyy1jiYUzwf-nbZ_PV1bYjcRUNAU4AvOjy1wnrzB9Cf3zJd-2A0O9ol74q5G9oIj3obwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=Llryoc-WYFPfaA0-MqKDh0fvJaHwCZ3G6EQDI-sEgoFpEjqMNAPN5r6H1COYFHzUlvbFubCqgoAT9v1jnJ8WjCd0mMB6-pz5zu0h4vYL24Qc-h9ui2HQheQHth0iPdGsnTiJMBNp4kYQ8HkM0JL6fPZXnKKi3e6gxzs8fjAOUTWXTscFYfRz7_5Jn4I7fsvmRApZ1VZZHOgJ9_cHk2pB092g7-VWzCrYSMSQVHmKczOud3Ex3Wa9SFXsZpjwFTYeMrjO_WwtxHKm6qyPNrQvN6j3Z9IfgGeDPKBJApEqpe-8wvaceJKzfub2u1g8CF_Hv7JjvSPivrg2c_rVfU2y9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=Llryoc-WYFPfaA0-MqKDh0fvJaHwCZ3G6EQDI-sEgoFpEjqMNAPN5r6H1COYFHzUlvbFubCqgoAT9v1jnJ8WjCd0mMB6-pz5zu0h4vYL24Qc-h9ui2HQheQHth0iPdGsnTiJMBNp4kYQ8HkM0JL6fPZXnKKi3e6gxzs8fjAOUTWXTscFYfRz7_5Jn4I7fsvmRApZ1VZZHOgJ9_cHk2pB092g7-VWzCrYSMSQVHmKczOud3Ex3Wa9SFXsZpjwFTYeMrjO_WwtxHKm6qyPNrQvN6j3Z9IfgGeDPKBJApEqpe-8wvaceJKzfub2u1g8CF_Hv7JjvSPivrg2c_rVfU2y9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXlUxAGfSIOfzsF0DMHhIbNVpatVfWr8XdOzOUJejW_PFaS0JZHWL3LATwetz4oK0OZ3JT0UrQv0TqM9h3jWcytnK_jK4OvNnfNI4zPvMhJbI0qqzP1uPUlCU-rS16Bo1TG-MOOBmJQmVO8QeopILjead1vP8xSRMnhpwh-pO1efkIfgBw84glZxAl4iRa3FZiHu5P0JR5QBjcw7u9_k-A98-8ZieXBQz8scE2r_Y-2Vq5EwYuPD3yVXMNkgKysvVtae1XRrMFt4B34oxcVrFCD1TBiHnFdAytGTZU4IlyaZgKaoXUtAnCGK8vtKwsmBUcPL0vueM5KKK31w7UBwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt9xWY-04JyfRP843rrmqeHJ5Aly8foJ-Po97yvGEWANaozqmlMitYtIru2AJx0VS4Scs6EyQdY1GRUvWvCtsiSJpEpftHyeXXMhuh_yLqMKsw4bG-RNlLxnA3pKak00nRZfknkkYOSXbMjUwr3Z7Atkh6LaDaXBYxbpPf4_wRbwN-vps6CGf_0bv2KW0IZcNTM3aVvAdcnugkI-4v0pdqBXILwC9yJV7P-5NBw3eEaKL0qA_1PYxjVG-mIBVRoz8oilNyJ2BJCcpTNHU-1GrcuNJF7KsUKyCeW_H6KeZqMn_IvfGnsVT7UYVngkiSxb03QuKTdCOLixDQ-toYywkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2v4QyMuWij30hNntYVLmGPjzufwMptPLLxg2S92NiCIWRfIzBmShskbVv5aKDJxeEkq5TlCrQqbR5Ws9CPOgd9-vgiFr0X6aZiK7X6UfbUG9hXiY9nhvn6-0QywsmkePSwOENBenrzDHr4IoiRzg7sAnWALmgv1V4ZBqBhhUi4Xzm9OhOPZL76dq0QclxoQppcmRbrghst2EMfjI4i9lYzYj38OY5UPuGV1KvekrQSdEbdWf7LNYNgTVgm2Jwhm_b6lyfCyfC3M-vPmMk8ZHmZadXx_Nuwh94HbHnXlpYyPVnhmKHTqeVMdmyim6hF5eKCGrovhEo4YiGblgO4j0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=AimB5uDrBrh3U11yiCgKvntJ0xfWfwHtm3d4CBVgrttIk3SWoLmRgmi20agMXFchBIcb46DYZsm8eQSp1EhCMmX09a1Mhh4hCdJiznf5lLxdG4gPLjJukEZWRS0IkkRrX8C2i6ASXlOwYZ_Fk_7VQqNBRNWvs9eHLUcG8kem0VxTxgSyV2X6ilctKS2DlT5L5jvMSlNNNQ3cbX8duDnHuzCaE34t8JOYIRcIdJfov1xCd-10uvDFfFiHAjYBsCIawaNtGK4y_XUdAtSlIrf7TqbOWhtxxL3NS9qrc2wrcZk5bePF7aVUaiEXBwEs3baU0NTCXTvL8ODt3m3ZqF-2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=AimB5uDrBrh3U11yiCgKvntJ0xfWfwHtm3d4CBVgrttIk3SWoLmRgmi20agMXFchBIcb46DYZsm8eQSp1EhCMmX09a1Mhh4hCdJiznf5lLxdG4gPLjJukEZWRS0IkkRrX8C2i6ASXlOwYZ_Fk_7VQqNBRNWvs9eHLUcG8kem0VxTxgSyV2X6ilctKS2DlT5L5jvMSlNNNQ3cbX8duDnHuzCaE34t8JOYIRcIdJfov1xCd-10uvDFfFiHAjYBsCIawaNtGK4y_XUdAtSlIrf7TqbOWhtxxL3NS9qrc2wrcZk5bePF7aVUaiEXBwEs3baU0NTCXTvL8ODt3m3ZqF-2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP3fOJb-v4unQI048wvqFdTXCvP-Izjub0Hg4hvsWOyCz9Em5FsLvukk1jWBgd93FMsBIgXzpatXDFDW8DSaOFN5cJPd22ZvKt1LqMHuaIGR9OQKlag7eBNgLN3qaK6sNK8lHSY6YNNKx786u66LnKrOfAmVhqZoH8ngfc1FP_sY53q-2n2K7wykS30rq3n2E5ve1P5XB8fs9Qfy-fvWELNa0_fUL4B30NNamzgJAoX0QfADwcrccJfFtQXRsGAs4KPBc9hBGkY7XcL2aOCmNhXF0bEmnvbSANWLrd5WuWYxj17O8Sn1nAWPP_nlD0jv6uDbVG0bv4pJxHW0vZ_kcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WruCcE2k32CvlFR5JpS0n68a6hGD41L2DcIJkwALQ0hiQLqkcc87UyK7VyR0J5BmHulpV0QPEAdbjy1C2Z2sia_5yzwhSgEIRKA90opR5iFv06esVLWY5KRfqCHA8Cj4uumIlYmqL0GonmwoNyxUMrKkZOGRb0JCjdp_jED6_Uozhs_mv4MkyY8hsoOuSvKIThKQzLFD-I9Tj5IyQvI_qG_4W-z-8auw_8eXd7sjMmx1c4pcSSqXasjvMNpuN4Snk0td8cLz_8WuWr2E09iFl1KFJ6d3TwIwCvL1SugM5jAi07wCvmDqxfFhwNuFU4febc0XqmCQSFOzUDgAJsotlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz1CqyFizwDjciri07vZFbifpaWLzx16j0jmnclwID9y2GglbhGzx6Z450jGgSCoXRSKIVnMZbCAA45hguyj131nm6X4r5eKQqZEhPAbnJDG31YSajqZy050qHd2daJw5Gz6joKYvNrz74wpu1qbkuCfjPfmsFd7Ot61uoy6u-i8msPHKyWyPeuoGXVKC64W8Neksl5Te1fXwyWtnN2jyvHZf8dwzpUANIrjso1ncgHNwr3n3YKX9sBN9Pf1mis_geVoOif5o9_Q0rsS_SrKBMenT_ky8yHsOMKczn9tJfUqpwx-XOK24aZIuJkM76Ccpj0eph4oEginp59OXf9pwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6JodcGwB-HGIOJIbfrwgqopXmwrYqywDfMNGnA_N6q2RstbqliryKZLPx5nMaFx9OFgCFeVWDY7OYIsxtEKF1Y1VEIPzKqor5c9yVS5EZ8t82LCF8D8aMMVk-2ulW4ETvhEay4CxhcSiU8uAgb-ct4uTLMoZjhndinvWxfvg8I7TZVisF7uWzyuY14gQgjii8juMIXrJV1yCYGdLbEipiRxeL2sLjHGECuJlbf-LeJlHKB65KnK64HyNPU0wo7gXeUyMBIoR1bPpB1O8BUU1Jgby3FgfQdP3Q3Ed6X5DrQ9LNcnVLmBWkBkzJSn_1pkrkyeeqib5nAYV_Nc0vmrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dca25BGMRkwfWOXfyeA7l-OYWo9tnBz24Z9XkMvxo7oH5eGqfEKu8OYqX1h-Pe0-_QEUM-muAmofDEe6XKQa-PuTFPr9t6J-qr2LDsTVY2D5bxawciz-rrPQk-SmA2R71nTHTod-CoXoK9ElxvAWvRH3T6zT6nJIe7dL1wxGKjk46R4MkkI2XyaShLDNXOXNmoqe0w5ooSJXRsXRpGFb2UfIUl9hgIIIlFVASY97IoFFwQRGcWABUcq5T6TrqSXehyrY4T6amOiJVmnHBBzhx-6VaXh4i5IvWE_x3Dl_Qt-tv19OgKEwEh23AJN1xyeAT7Lng-ULV7cD_gZ_Uhmb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIynpSBeBbfczoUMSUZywn8tSCb0jOclVZ32FLDe-p4RIom_YieDL28khBoSEI1Qi8tEQ_r-_mZ_0jx7DN8-V6Lpn1AGVFLErYasnphk7bpIsBSe7XVfagwj7IKL1so3U1nXyyuBrtsLOOtfbZW6h6qnKTTCFIvbWIsvzVxAXJnYN8HnelX6ce8SJza6nq-agevtA4UwAHY7hF1S3q2N_XGxnmeJ-YAvf0g9_EJvgQ9RgF2LSu7CWtNUFMOfmS1GqSPMXPZ_rVxf29Bib4vfNwWVTy9zSkQ82hnDnisgxeAmwzF8Vvo6sq2UKJK96MpDzEFgNwD_hWrz0bZ1Hu9QYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdOCvOtRURbm5Wr9yP_tv2JJ8NXYAEmMfZE9cYiOd9uCYumy5_FntAVCZTRLX4gVSl1CO_owrsaOt2TEP7nMU8FFDZiAHJ8nFLUiFJyYq_L-Jav4V5J1Zc8isKIHzvn1fcR8t1KL9ThzlBDqT4symBpGku0EdCaDb-oXSVva2oFmfBmeFWeLzlhgzfepeuWvDP98e7io-AnDWGc53EpG5XAF0RB3FhdmM5PxtrWk85Ol2C_5Jnhaq-plejQXbAgCHEJMZjXFQFauH3qQ-6a-d10QQUHQxVH9Y9igEIPRSwkVIAj4RxthINoM-ZONKII86pwHqoNYd6gOxpP2TaqJrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVAuEVeluGe-7O-qrw08Gx6HZUIpx8AUspfliXAiXDHcdBDzFhUoVKD74G_oV8Wty_YzeO2AnrwiJ4twc0t0k2_lNUfklq5LFEtNvBcWhARvZyc-0BwEsMYc26nXTAjTLoVUI8ggt6RjW_deJZLT-zsFkGhdz_1DK_u1EgvblmDdTpt3J9WKxS7kfdrUrPC8mlIIxFCXMzXssN_YN6TNsRMdQ7FAQduQ1QgkkO6AtEa7IHxN0bLWrWn2MADtnldnk-ssnf-jZ0yxNve36PabusvK5sOmaKx5IrvsErODnBOnkKTdOkE2eVs2Venr6gK1wzAbmcvHux1TxsATCTsBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLDtlXJNlztD9LRzQE2c2J8oRT5HBD3jcOS7iFZpXUmUkdH2CkKOH6PnMyhK1Z0yK5ys2Lz7OvOnxVquqQjgUlbn-qnhWmAA8n14ZLTQ3D-umTANh0Vq4GIMWV8K-xTF4LTKB5E_3eWzQHftENxyTLJfbdWRxvmaBEjwl5PIMdgnvQS-QyadGoBaucrfvL5ng8JkjpyuozyCZLvzS4MSCuSAmck4cXEAfJKBzv3HVxGfDoIGRX4OutGp-qck4mFw-8PpYH5DukMdzW4UmVK10gtvRIxMW9--2_DDSwODtlPHMrPTYH9EGUWUrW4gDsfGDTxfwGGHIpCHo_83xcqlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Biu-iwMuet7nP_AS83cNc02w6CB9KqXZbW5gjmBLahTlAtE44nK1h2NICqo_TEsL7vrxmdJa7HW8pFzi1d8lFeP203hVB7jnSz_sPkacshGq0jf-cBYpOU_MZDufx5LbghmcFoMnF1gnTwe8HGkUmy_PrV7zgBI3PIv8F6P4F_sDdnXBEvi6jfmAe-AV2C4WIJI3EJGzUX-pu1AWhGfG9--cCasOdarUC8X1Y27jITMNP7kHDQmcptfMoIc8S7yge1sCTIiZX34soYRNExbo5WbZvNjt9o613hGy_Em3gPcFS8RoMwqtdiYS4_pYAbTsbJ9XlDOvW3jeBqQSoewqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAZdabNJr-0rzSp3zz5Ez0hboFIinDjoSR9nmDvXEDirMkgZUTLmjeSV6A8DQfXxK7WFDfDxpWjzz6dlOTVE4GuK-mgiNPg3nUkNrY3Xf08nM_jrSHHhKPr__ZoKMAR59EPEtTqFOafkPejtwJwsJh-IuIwLUM6PfrZUPL7UPb-I8vNRkzO_H5ZgdwGC8K-HywvBKHJSmqgjJ7UWrH8fcSUvtUKkKsT31ZNMIzUbk6jYo8WOKLXVdOrust0lsetACgTFJPrVmCsP_7auMzZ-2ND-Gh_-K7AaEr6hn2LMEABno3_1-1Vq21lVeQFakJNkkpPGNmFdh5bB2pxAk5VOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyeoYsV3881fCcnnqq9VphF1JBlbkxH2gt4H5fBdVXecUggXUG8HYSttNPdGjicD2BhSAFdzNGTlz3JbJN3-MeQ862uCzTDwZYGud6gTpAqYPWfRP48GcCcJMpmQF9KTQObcsX-vA1Ne14F8Nux5eQeTPwO3Cy1IZ_GwoxcIxuxiASdGR_Od8AjAjEuYEV3I6PYUcpklaQR2iWUeawTG_sXTxQyjsnWo34InzeBpH3pNaK06K8IX6Bw8TZU3x7i9NGSNXM4B5FcbOw6pHQBuSnceEvLIbQcv7oksPKpFRUPbK77r55sU9RwSJw19y8_D7NEXFKTXyKnIdXowOAKyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPU4HwL_ewaOsUVjJhID3iWKnZxuv0moQ2qvpUJ3VRiJ4eKatWnzEPu_c-9Q9Ds6ikGsmMCAzx97ie9XEcI0L3ybaK15vZQg_LlcqIDbkuX2u_iVhuqoJAHELVml9x1fJHNsQq1qmGxyHrfYKFiwQecr9QZo4aEl3zzo_NJ6ytf5zqSyhofrI07Gt91J8lr91_xYa_VuyD9I-Gs3bIvvHvHmmDrhYXWtJVI57qg2Q3r6r8YygJpMHfNp9337EGZUIpHbS7DH9ag3tifRMt19XQsF3n7AcSMmigLtIJKhqOisQtBm7lyZVqgT_RHT3uGjBY3lC1UNco0U7JxkgHagyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXLkXs94xFX5e6dNq6WD0mUADN7WO-4iiSm_7CQ9h0E2UHxPn_VGPAaB2tkc0Jq8PMLlz1GnW3TH7ulGuU-86o7JtCZnEQFDyMqeEemUZPbvF6hbGVR3trCMygXDJ8vylOKv4Cwkzj0_WqUTLaPwRu6javrn5alcrZTC38uuAtQ2qf6yo6WyFrQ-Vpr46IVPWQMD7uxkntheKWgX-eftyrF9Sjpx1CfNtvofwDeMnSKyg6RwGXx-YgasGGccsK7p3st0NmtMnbLAY7Iug0U9ONcsfGHvS4-gKDLkLX3Q8skAZrASoFPCiWHvOBLPWFaZhvUI2y4YNStvdvgCtNi3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tyr4I2MvNI-ywjB5qnteEFj5rJkUXtYAraUNnC6NCBgJdcWW3murbvBYrBTqKVoRmK-l-Jqq3q20dlHtTxlCNkF-G_TiNg-DQ96bXYfS7AzVAV8UxpzTJmfZ1NLLa6Nn_Jq-fNXLgUloPSDUNNJGMcyywBzENpDASdRQ1BZjZm6KHfBEA-4kjTvFoK3XDl9VnmXIo4Lf1EpQLJ7PaMybEFoMbiyKVMVOMuZzvd3V_pyvRxIQBZo39BVOfI0Aiq2pbKdWMD8E7B8pv48lT0p3vbikluoJpGSRKgqArT0HaMm0UHU5awJqWHhmaA-R1IrfzIkgi-_hNfsd1jTPvjPjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVOAh61QI94QX_RxzUB0D0KcI4ybr2GyBaq4GLb2TRLWgkrNI5dasrl13PHb5XcRG2-0cd8RBraIl94-sByNe_QhstqDh5fvUHllDqQef2u2w6y0TVjBkrqbjg3-1s4-tnKGB_PyJD_e-RWgiI9OdzVkDCskebH6rbQ4l3PQ30AeleJYVytpGveBAi_cJphdd9Pne73RY5TnLNhC2oEZCgQEiLyZznN9vUwYXo7lkcux-YCFsc473h3PzlDddsnhKIcgbYI5cDpGznV1AiSXBhDZEVfRMJpqMK3aZy-tc6e3sjgi1xuEIB6EPbArj_i-n0DU--bl77weBcDdohoadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_jOodSkShCS2E3Ze59d-p8h-chAogxacAuIQilxzYTx2bc3JiJ8WoPHwkR0a_XH03XOuYFAxRmfAuo62YGqvIVuoOz0vugLkskQ1f31p1B9D6SzsdqyQw6Z44xVQSy5qIkRy9wBb7_WwqgdteBaPpNaAKLhV9GUDAvc5TGSUNZ3Tjct93ssfps_rRFJ9oLd9cc5wIxNVJdBFeFWj24eUJW9YPUW0LvkB4g4idCW79CmUYKHMqqUWTNIz1umRkE-SXmYmJl3CcTGfQhnA1f3Q6q-n-47OMwVWcQsO-OAj5EzI9i0L7OZ5B8Kxg7CWGDUZ3vj3Cgc_V7kxiGB-awP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=v_4eHYmBeaeM6ycUVd9wlVAFYttVEL75jCK3-Lv6C916bTkIPur3kykPpr2aID9e29JQJbZE_GjLK0p1yJycKYw7qFGlVYxkU42Qvu0-PPr-aB9NUQS2RorRfyXqk2FkdKZP1Ya4SQsCxXo6uRBBUgMq97uvZMcnE7z33Qv0vAJh8HtH8jMrIUN1T6xe4vSoZNv4r-g6TT9j8ZkY2qBmkJbTLPiVvfMyQWchdCzna6rjjEuaQbg13kZAESyPuyeouEDjiB_0Og8YoSOnaz6RQTwLLXCXSk6r0P4tRdtlF8StdESRvvaQ_a4IImVz20F6350l4yHLW6ywqtDI85MSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=v_4eHYmBeaeM6ycUVd9wlVAFYttVEL75jCK3-Lv6C916bTkIPur3kykPpr2aID9e29JQJbZE_GjLK0p1yJycKYw7qFGlVYxkU42Qvu0-PPr-aB9NUQS2RorRfyXqk2FkdKZP1Ya4SQsCxXo6uRBBUgMq97uvZMcnE7z33Qv0vAJh8HtH8jMrIUN1T6xe4vSoZNv4r-g6TT9j8ZkY2qBmkJbTLPiVvfMyQWchdCzna6rjjEuaQbg13kZAESyPuyeouEDjiB_0Og8YoSOnaz6RQTwLLXCXSk6r0P4tRdtlF8StdESRvvaQ_a4IImVz20F6350l4yHLW6ywqtDI85MSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=uluND4cQC_O22rzaHHN_Fkp7Ker70Z8yGr7MP4pjKFNVTMW8GDuwLNxTvn7IY8pHlolN2Y8q5AsdrVi_nljjEMGoXR2-96bctBOT45izg5X-ljJ45BpcTVPA6KZxi-TN0aIQEUeih-gwpFDh8C-sQanygqH41lS7qVRgDilOMkhd-whuClqIAXQOxWLztmtAWKyvruxLTTGwpUDynOIPW5a2iw6cDquzn5z6UeNwIWX9M5x7iHhxIz2jdEV6OlXdOrK61lXSDSXsofaPow-rh2bdajLDiWL5uaZcCi-8ws3P3HIiJNVJb6k3zwIgdMJyD6YtCkOjuJQ9uEQfBriMKHRqcHW9kIQpEoY6uwul--_9JvXLomejj_gWd2Gr4yoRgukCwxLtSEVLX8k2_3yn3p-yEn7L6aQwS0DqW6N3-xnQV4wn1U7H_pFxUE_xdBo4GLrdfKjf4XpLKe9_z18G_Fqc5jHd338Y0c5SAb5Ni6_s5x4aGSx5_D_FG2o2r5_EfpT6WZ7fnjrArcJmV8bI056JrtGFBaMABQkHGppwSxoY91x8Ur4QDgQqF9R-VoOCKfDluP3Q0IA-whM4Loc2lbxOjp0qs7Z2v_BgVT6dp4K8qDRT5Nbza9lBjfp47VFfo7p8P8EMHBTvh-8DkZUCcRaePewMtLlCwOft_3I1lp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=uluND4cQC_O22rzaHHN_Fkp7Ker70Z8yGr7MP4pjKFNVTMW8GDuwLNxTvn7IY8pHlolN2Y8q5AsdrVi_nljjEMGoXR2-96bctBOT45izg5X-ljJ45BpcTVPA6KZxi-TN0aIQEUeih-gwpFDh8C-sQanygqH41lS7qVRgDilOMkhd-whuClqIAXQOxWLztmtAWKyvruxLTTGwpUDynOIPW5a2iw6cDquzn5z6UeNwIWX9M5x7iHhxIz2jdEV6OlXdOrK61lXSDSXsofaPow-rh2bdajLDiWL5uaZcCi-8ws3P3HIiJNVJb6k3zwIgdMJyD6YtCkOjuJQ9uEQfBriMKHRqcHW9kIQpEoY6uwul--_9JvXLomejj_gWd2Gr4yoRgukCwxLtSEVLX8k2_3yn3p-yEn7L6aQwS0DqW6N3-xnQV4wn1U7H_pFxUE_xdBo4GLrdfKjf4XpLKe9_z18G_Fqc5jHd338Y0c5SAb5Ni6_s5x4aGSx5_D_FG2o2r5_EfpT6WZ7fnjrArcJmV8bI056JrtGFBaMABQkHGppwSxoY91x8Ur4QDgQqF9R-VoOCKfDluP3Q0IA-whM4Loc2lbxOjp0qs7Z2v_BgVT6dp4K8qDRT5Nbza9lBjfp47VFfo7p8P8EMHBTvh-8DkZUCcRaePewMtLlCwOft_3I1lp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACx3rAn6Ua2k97RN-doi3ThMmUQZBSDbC45ub36krmSQHeynecvrHgzm5UGjtKmdhj6vK1Y-AWfRIuIrUfLZqy45qTthgJLS05ExW01nnrjANRjLMivlYyJCCYIPCgWgTXI77pYRQ9tY4L9thN_-0wq1MmdCNdQ-jjk74JdeEWzqT3Sfk4WQ6aZCM78zxoXqdxg1B3vK72Lk03G6kVq-ocZPpMxNRxaS4dQyzjUaVDn6QPy0fcxbYQdFd9pqgjb0IM1POGpXtNX_uiHHWRuSTplwW1BIS-uv3VVP3RLqUICwWhnHEu7qP_o_Qo608ftcCPPLcD3L3C5EZ2xSJTbFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6VM2lHLSAMvF27Tau-IxQOfQ6hEsQJ-xCb-w8YbfTU44gCthBKVWUm3MB1Jgcg85Bg8yi9RBgZnZ_eC9Q7QMmFrpF63Gf415YoNyb37Yzcb9J_65DO_GAQXMA6ulpCvk5bKoPCiSi6rH2qr8kBvTPaJbO2zXeBWTyQTsLe7lfksYtB6sUbFyCjl5Any9JeItVywgS24b1o-CTT9b6SJO0o7_vULTaPl2zydHTZ9VyPQ8ZkiFwkj3f4YeR9eeKS64gpaXmV5UzhLBlbt5IuLKlWSVaj2iviJkl7O8Ddrth7BJybTDgs2eureS9uHYcsKIEKC0aTA6M16qg5I1a670A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxGOoQJgYm1z40-a8Dx5F61ZU81L1T6O8Ww6TRqZj3hecESzzDHOv4gEZ8JIhBDkhTjpSyqsw2-3Knlu_s9q1eq9ulEpHJd4ijIhSKB5YLc0WKpqfv4tGudufB_2fMtLDJ7A31Rtp9PbibeCzGgO0cgTWUn7YiiNQtTrHpnIzjWVzVQUwi-t3kt5-p-M_3vC7YXlaIt-8UgrEvOo4_D2fr1SiFsPW2z7kL0prmxWfZFqKKSBQmcFiBhlGKE4V93clcDAvyB_TlirWyfRrVzlpniMfOSNOdJmuM6SjjxiG6OgqpD3ZbUU5w3DNkJDcU3dPFMG348K8uvtT9YQu6hkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-E7X0WieXS8HX4Bzv-YlWYBVNu1CYMbGiRKlGhOe75JjB6NmhWm9n1NGGGt30PtMKuuyfNTWg6dXGby2skC30yGHRy5MwXzWYgnV_MxaEZSFtze5ByTPA5i25Nu_NM5FPFu7XPLzfDjaJKhOviWu3UZfXYAYVNYSQDJN-KhQ4aqpZh2ZSJqJPOWOIG5ED8Sm6mnYjAfbF4dtZ_VhLzUbQ3VWhnCLH9kfd2nI-RprlcSpX-SUG3jt2VsMb0GssQsEWADLoeRp75CZr9uk2OglB7YEbhLE4UrS-R__BqtPNGLxbIDfwFvxkE8kWlaQ6fSXz4Yruuyrstt-H3og0Ll0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=dqcfv3JW1f9gNVuQCP1pI2ZF_Gxer4bESFjQuGn9xArBlAtGPrTTfUEK5Gy7g2kLvI1SsRD1We2eBSh0hNC8qs9R2Tx9ic011kerftVmixFI_sEYktR4bIN3wHPDtDmPrEAgSMHOMp5d4Z4VerKluUHWjpdnnTy8oI5eyNKbfHfOOO1W9M3pweHLMsvMDTuDWH2UN0vmJyYtJ6zuE1Bt9pZC8Bh_RXfdJBbDhuvtMjVMRF3yjVkpP3sPazG1lZ1LLA2Xx5xk5R7RPdxCztEzaOozj2b45__GMStBvlQw-YUpLPvi3g8zBzVzVGyBvgDyfNZEfb2XL3a2uqH5wMRlXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=dqcfv3JW1f9gNVuQCP1pI2ZF_Gxer4bESFjQuGn9xArBlAtGPrTTfUEK5Gy7g2kLvI1SsRD1We2eBSh0hNC8qs9R2Tx9ic011kerftVmixFI_sEYktR4bIN3wHPDtDmPrEAgSMHOMp5d4Z4VerKluUHWjpdnnTy8oI5eyNKbfHfOOO1W9M3pweHLMsvMDTuDWH2UN0vmJyYtJ6zuE1Bt9pZC8Bh_RXfdJBbDhuvtMjVMRF3yjVkpP3sPazG1lZ1LLA2Xx5xk5R7RPdxCztEzaOozj2b45__GMStBvlQw-YUpLPvi3g8zBzVzVGyBvgDyfNZEfb2XL3a2uqH5wMRlXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtnsUOUbGxqlhmP2vCzjq8tMevWzL_qlVVRWHroRxLs4yhZr9c-78jEyUy-SI9SQwfof6-H9DOz6KZZfq6XJAKvpOSatUI58Ey8YgU51wKD7UXJUQ6jsLkdbg2F_bpVrcUbXqMN-oMjFCGucaOv_CMNZ3PGkcjMKyl7rqhlD_2sCC1CDSLVi5NzhKtOKeCr6Ch35S4uA3O3GFEAiyYNNQm23VVyk29D2-YIa_uo5H0SGAW3xVpGX4N7oJ8FpKrywETbAtKaKYWvy6Gv5YhuapZSZWRzsk5lrf0OUt0qU1TQxuJaBNucdOafYAOmbilemrMTduaOx7--qg7y3W4iTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMpvfiL38mjLefE3oc7_fDPA1tktq5x02Q-DpRLuJ8ifmeLX8Fm2KMmbXOEWV9DVmPFgXcOMyX3EPGQ34p9zfPjdntJBsTWgiH56CVLU5qjHkVRX2j--SQm8km54Z_rCVeJ8VMbbmgLfZZn98aA3PmMCgMaYWko1pyoYb-lqii2fDReEhg90Q5AsBbYmh8GvllcmFvrzZmn_bT09pT95i5yfaqOwlL9fJd_8792_lpFpQTs_7J3z_0rGSwEM8ie90ZHi7SN7uzziRfGrUvL3k6vzCIf5CEl5Tt6Vv_5c1wCyUloqJITIyz8svq-kgM1kOrRShlMNiCRQ1m-liYE_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv2mUMMlnroLS7PHsbaDS-zn4eyK2SD-qSPbOHtEVI6RzMciteOTtcq-M8qAoFXQ1ocQxm5lA-cV1adcQXIP2qF-FjSG1IUqB81VzrFBAk24-K-sJGW6qPAmd34VK6vmsgyC9EJld664deZJ95hPDla3hpZAD7NoDlmSPhZrZFrzDYStuGb1HVUNkneW4Yu7uzi_mrxsogG6huwusO4V02IKnzlJttxS1CddRBlQlbViNmWkLd__IZ4E84o9THG3F5dXbgFfdh2AZ7E0-U_3kVaxcNNPodTo-NT2GnxDT-U6JGP8EpoGdvtJRcIGFtlDNaL7JLm3wYyR0ZdIYX19Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co70_O7ucfV1rtyTT7PJmIRQSKaA7bL9EC22fzezHNwPWrfSlMN7bNa1ovJ9EAtiCFq_PIzeXmxRZc_2crgUTTEnxBOhRhPiAxvWiqWpc6SY2dUzHHG0Tc3hGSDu0qwfpk3L7MVx7SHunvGHhuLfe1r_C149tl6PxkgB08i1koYDgLaYqjISGkePTFTz3uwOHu6LN0RFuaj6H7v0pKeZUyfaKnQg-UGHyz8L9TXBjy8yHHrzl5OPJq-QOfil4idVi0hmVWZ5M7o4KztttO2yxNSizASXeNEzmk9hEp5FdgI-UYL_4cG9Go_FsoQthbSqs-auT8HsLFpC9odsRVDb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA-amFCXXvmLKCKbpjLe0n_2OcrP5Bd8DQe5Eyd0-TCzNzRZ1wBcKyPTdlDmC6j_28GgX4fPZhVQC6nD0b6Dk9Hmqg7UBZ9PiaL6JKqHXRhLucmEwjvxwi8SUl9ftISI-1cntMPRzPn02Dyv2duHALyAft7y0P3Nh3CPLTsLZn8xRtsEDWoEWCdYI6bkJWFIJo0BK8LiXoOdunoiEvp5zSWFYu02NctPN0pG39BeVJamLT-UBbNyo4ADnxOMCYtqAxiwCNEuoftlydrqzYuygBz-LDf7rdpl8dJ9nZeWx37B_IpJ2A9Z5DhAra8-yE-Bd1DybKMkOUSYOZ4ng-UEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3cDh602LN4_chH_xxi7mrmuD9VfgXyTAZDdB7gTxda_JfNdDfpiVriwlfrpxinxurbjx3y0owEGPsnDgzKTLDx5YfA3fW8KVIU97r-9kAVqlQvlMDP1jKA1XijMPS7-vSJaLz9IFuUp7gJ93SA6RRe3xbSfjACe-mEMlxIpOHr30DLzcJ_NMiHl75Ge1l9wYEpt8xXrJu-Mx3ghhzRQ1jM_pLayYL4ODpaO3kfM8kd24YyQVi9-K58Etf0ljjqP9iASSiRYIMzqEHDgFCdvJJ65akXF-LHo9YdRfobPRE2lJCCRZYRU3Sy4XBXKRl1DRi6pWL7ZOYJ6J568OLoWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4yjMFqdVDJN6wM715KHoJJrI0sCPQq1F9BeBP-GCbJ-ro1Uk56lq4SHQh5fgDb1ENPzYhuVDDargh0TjNZAjHdHNQVYgk5tRYzA9lQADE7TiW5rNLeSyU3RfzP6_06fHtHmDKpdc6bFeX-pJNoKbFaRQLrgLg_27V7qxA6J-Dqo1zVn1moKh3xMHpX9j21-H1dB4GQITVZhGLI_H-TZUfCf4tpzdEt0N6xdtFBEyshKuVcklfnsPJK0ye3kdKytFIgmhsEC95357ksBTKXvNNnrN1OkqUH6KT5pBqS2hlL_HkV9EjWB9pO2zrNBFpigYjNb4PTEfTWWB-7ym17e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALbHyb7Hu4WDiYDmfqAR6dclWgX2KqoKG2lRzsUSjS8I95XpCttzo8izDWNSS1n699JtwpscsSVzACr94WULpci8VN4cwn6XexcMbC0Mii4XExrKTIcQRAHigmvcchyKFGkUmJ8bBaAH22YEAnKj0BWnOgHrZECAlujw2lWii5IMkaSwkbysm6jn7QA6LxX9N0e-U7xZ3vEdvKhaF-tTZ1Y-XB7J3abdic0oahgNMEesGhxlCl2DDWxs8l3G5m-hmEji0tPr8SdqzY64OY0cIlnfVJDF72f-ASUoDXyu_f1AR8_va26uHrNyCyTcpeB1TJvjcvselyiNYBqvKuCLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNw_OMkOk-_vzkoGKrD1Y-I2yKjvMIcSRbY8btxTHltffoI__crBcPslToEBMY9Ym5wNu2PGlyEyIP1oHo_XGVaa5IjGTWCZZwEMrILbsspx2G5eBcCCl4RtEKJhLYBQqbQoU-5yz_sl8XoBWftseIee3VSLb4vHoyutktAQnokCS30_2SyOiIqzbjwbO3WEuBWPxPOucTuEIBaakYKGcM8icG362DF1ain-ecH3uQQQz76FpCgH0ItrOePCcw9LgWmO6EKHiOzaJ9C8pRyRgaaWX7gjCo2S3HmkY0wRi1GuozS8wJswHsjd3F2QBAEBaqjuDxwbAtvQAm4WC8XpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=ugutTIivudW5DdwzFGez-naUVDRy9IQevgc-kjHBeZzECfAR6X0-eqvGnx71HxbV2xrJbeASzdlI_x08Qb_r6npzeh8x-Mf87MONX2Vm8to_rjapGhIkZKzXP2y1WT83IIhBR2XQgHK7dixo-CLbuPQqaMrRWzznoj7Lpyn2dBzTZsYXwRVeGdrrD4zznhOtpOAkwfTlK2f9hKUiPbV7hcdc6b57DFQdjJ4JspOm2dCeHP3TC1_bwLxJFPFLG15otZZhQ-QrR4pXyeGdxXSA6fICO6uHctDEJMA-IV3MCePH-WoQqPdEZqiAt6tIff3sIny00bYBLuYx0NK1g14Bkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=ugutTIivudW5DdwzFGez-naUVDRy9IQevgc-kjHBeZzECfAR6X0-eqvGnx71HxbV2xrJbeASzdlI_x08Qb_r6npzeh8x-Mf87MONX2Vm8to_rjapGhIkZKzXP2y1WT83IIhBR2XQgHK7dixo-CLbuPQqaMrRWzznoj7Lpyn2dBzTZsYXwRVeGdrrD4zznhOtpOAkwfTlK2f9hKUiPbV7hcdc6b57DFQdjJ4JspOm2dCeHP3TC1_bwLxJFPFLG15otZZhQ-QrR4pXyeGdxXSA6fICO6uHctDEJMA-IV3MCePH-WoQqPdEZqiAt6tIff3sIny00bYBLuYx0NK1g14Bkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGgqBImbmSsvliqZuTHbY4qIpL7LEKW0Qa2gca-GbbTBiBZryV7gCh_nAgCSyYd7SitQMKBEIbZSnbaI7x6ANPkZSCfeHbPHgy-IZz4V0d0I-Sg3_mQGC-0aEE9OC6RdyOzcqDxNvzOiikfI_xG_bT3FQL5xcK7XqOUaMxngA3ZPozk-8JwKhTqgIeM7jB_OHbOQ5XKAymsO-CGSuJc58i2vZ_ORwR_0By7EbIgfgUkl_lmEhpGlMc-cgKwCl3wrPq_d9AK_g1m8B4VkyYVfWGEy1x3Uy9ISZcBr2DaIlfsQxazUjTvHSKiPG0I_OsVZQdNGLdAjJSFtdYm6HGzs9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgQLkUBLJ8MVKrjjD2RLgPiLJ_9kqf5vEt8GpKPWsVwZb8nMuzVDFoobHhK8tdsUbw7_v4Pb6GY5PyWZ9zXSUNRz5KIsGG26OQ0DVC2hoWrnTWKRPWXYU1eWNpT2ZQsWyhfAeGCb7JbGgo9rLVEM5B3gPpDhT4pOqNFGezUwJaRTp_ztVeBvcrgfbPlC6cnewOQdQuRh057l3EpvG7WHurkbh98LqnO7SXAV_fxMUL-FO0yB_l5Zr2_D4kAbY9FJ_xnc2eRnHnTsC2C86bHFqustNfQb_0hDiagcJVRIpuOhaMh05thhKgu-fXf6huKY-6NbwMqsrUwNeqr9p5NW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs2m3o1lNwNNeikhQmOpATJIBM6gKOWfW2JyRHCV3esdo3uJ15fMmQySoLZEZlInYZEkfzIb8zo_l-YuIMo2QZehcL9XxQ-s7UqHr3CyUccBb8k482AnyC92sIXHAq9vNtj_hm54ZI4M_ASWUKwfqV8FUtPU23cIOBCd0AGJnP25J0n3QseQLxTSoYbZPj4SkWGBw-R_GAZOxW8S7WBKQJ8zJ7-aAvXhpoGtQQQpXnxTPXjysp9x6LW7Z3W34sUnFZJX6McqxkPO60HYgASIQvTwU-jh3h6o9rDCyyB6jcmp7mo5kbY_-ghEHJsShjV-qYdDOwsukwa8jv73Zim0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSoJQEIOLsk_Okcv7G2nBecDqZUfx7emM_xCCbUcAi5cTCc3ngbqFmUiwtu-XJlKGU2wuEFTCgt0BE9quodbhqGz39gTU68hE8sg5TjpvNCqgJp6FRUrSRYRiumLkujIKFONLKSv5lHLGBSN4ydVI5N85GfyWoVcwhhpNzrQvKfUaVM_8RUgpqdPzEgcREmpil8M6S6pSxa08bK00g9BGER5COWxEaoRoSiRh-bLYe6J140kjskhYDnfkTHOyWrPuxRXnGR-1WUUiRkS3EkRWeu7O8e-srK4-PYB11k9j_6RVPvEPFEB6hc70Q3_CIS6mwDnoaLRzBUThHihfeXB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfSIe0tx-cxd3GSmrlNYDMAdJZ3Qk7rMO6mqMa9nihOmqYyxLoTRCcB9HA98d9hLNX0XokXEg5fpMffTSk-R7yVPqIDkebVOD4MohcAWLtyaDgcDlKShqznNBD8cXYuAXMKP6okV0Lp8T6dkOMF7B93gh74IgQEMWw2U_1q4r1GV-uIy8xj4eH5s_U6UNl7FavQETiZnBjiHVFTrCFeWHMnQU6220ZM8fy4-nA5dXasVEcudCnw3dGc28y_lXBy49aPjoGzrPvuCeY-Lg2vwrH_kLx_nGVO9CxeCzGJ4ZFvFHu-GcXaWdLABqOaMsIuMrD4eMnEiHU8ioiMqDBB9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=W7dSfINVyFzGvoaQSfDx7tZZnro2jBG5ZNncz0ZEiXFTU5D7UzYritA9OOdvA5STIGUVd8KFnnbGEX6dhaSQo3JOk7TUd2CdhH8tONKLyeYb8NrySYlo7-9MvW6-yn8M-PHByOmmLjeOcd-9F42D4vjlK0_Vdg8LDeheCvq1PaOsYQCizHb-MqQF9bwdHYTRx97bqZJXfqx66Vjr8du578beQyMbGk7Xlp7D5chEfjiKdEHDxlws-X6YTg-XO37OHEGEdVDhvqbAkh4tncX8VC1qKpiNb5e3HOqTYWw0wGvE94wPtTcJfgjIZP0-NoplJxwJMGiZo6NadahoapDZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=W7dSfINVyFzGvoaQSfDx7tZZnro2jBG5ZNncz0ZEiXFTU5D7UzYritA9OOdvA5STIGUVd8KFnnbGEX6dhaSQo3JOk7TUd2CdhH8tONKLyeYb8NrySYlo7-9MvW6-yn8M-PHByOmmLjeOcd-9F42D4vjlK0_Vdg8LDeheCvq1PaOsYQCizHb-MqQF9bwdHYTRx97bqZJXfqx66Vjr8du578beQyMbGk7Xlp7D5chEfjiKdEHDxlws-X6YTg-XO37OHEGEdVDhvqbAkh4tncX8VC1qKpiNb5e3HOqTYWw0wGvE94wPtTcJfgjIZP0-NoplJxwJMGiZo6NadahoapDZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLca3pfop-Fiy6H3XwC2x3TO3CTm1lfCXgxSIROhTBgBLwzboa2eDyujWyPtHpp_DMIX-ra0HJBhrf7akkKxxaG6dnOtDBuBtlb7AIas914DzwOjYxOmEEShc_W9Eb_jOq3i7yrT3K67K5gjaZcoPDST_2nvPdx0W5bxl_3OxhW0IzypTAzx0NqR6n96_idpj0mfXiRIu7KaAeKNsDzarHC2vpVLWxdsfiHXjWQzDxF0QFj0DWJoQkjR6G88jlHHUmgpyEciEzHtG4fuWTr9EmM_i11N9xczPdSd1WJMua6YySZeNrTA2LPgxle7oLK2DkJNe3OvPc6yMgc2xUxE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFMI5lJ_fpm5gzAqNki0Nq132uZVoemogWzNfeh7Os9jCeY4WvkTvRyY3b0lXaRsAdzMj1uzgkd5-Gx2hqQsS7CVMTCXNoRaiSUnDvxEnnSmJCHeKk581ZlC7frM-9rZU_B7K_lAWj3PLzxsT8tCTeKc2QqgSYv1_79GvFLzSU_M0WI216CkKriXgN0gbegJRe88JYGYDpYpkAyll1Ch3DQJYfAtTUUkBRDS_xUw-tYLo2E3x5HRiM_PPKvyNUmguXSdoN7cixalwWNmM2LZHMk7mRk3jLOPfVpMZLmr16O9X2JlewxNkiCabB0MyhJc4WAZSQ4GjUc_RTDQUn1ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqhsM2_I6NY-zovAV6NX0vFC4QDw75iweDizggGSvAoELdEHnnM2KtSsAd0Xc4a6tZ2EYonjCJjxTnASrMrPNsAbNVAMUvXMDgG16820owIjygm8Zcq-hUdgt9mdNazhjXtqR5RhDxR0MpqJJ8GyVcdz8-lkc2jMk8yJcOQh3BbkmboeWmuHfGhmNetpWslYtGa71Mo3oG0XgyohZqfpuYO0R7b-z3_-Hrvq6PdS1sLkkfPpRJCMLyxfrxBAFFIQBgXDiqC1LoOkEgRmzzLJH3ZAMFvbKUA606Ou7nWtzc6PS4TnncoQ9oTbs_tVZcxvnKI-QTqNWuXEW0oAwvSWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdf51cHkGGUU10AjvztzhrkF-7jyKGpS2FrcvBRWRf_bot4oYR_OGep7OUEnLj_m5SIWJF0Jcpsz7lI78i8bF62CAA5rT_oO2RJC-3Fs0TpsvwETBhROJS2gNCBPMZ6PeevwZtm1WRLwdEfkqZ9LQeestgj3cy3SnQX4kO84GUJbgCBYRs4jt2BP8DhMkrZRJIX-By4qpXWn-L8LpmOo2nAbTY5-S06UWEQna-lH6ctOE_cF0SbHjP7AA74dHt7AM8IvuXUZ9v6LbsulYGNOIctHILFVcAqiN7UyjLazBIRjswJro3nvyhAAvrvDe7YsDITZ41DqMVOpRQjwhGmcrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
