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
<img src="https://cdn4.telesco.pe/file/HOtJqoBTM3e0kQU789dsZ9QWLVuZpxOb9OBJYB8n6-JTA02tLO1rnGrpBPUWZ3wjXRGMzP5iWnl7xiAZJS8xmLxNU0fpj37-XKN7vJfsACaTdK2WLna2xhYm_XtoWMgpVQAK3TV48_3g1qQs0dA6sUe2L8DVelNkYm2MF8Wm23c0n8QoL1z5FHdFLryele4SLoc5pWlK75TyVOXSxaJLrDdPyCXvvdqsfKIuUhqmIYngA_AeHJkty3AXPhYHSR3HZ2hGXHKuFHKHMhsYDJFA8j68S417CeS9ao4-sAjgWafw9J1PsZPPP49OVoaplqSaG4IUIIW1NR9ZT0Lt7YRg7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 280K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 05:59:39</div>
<hr>

<div class="tg-post" id="msg-12834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://t.me/boost/withyashar  بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/12834" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/12833" target="_blank">📅 00:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دیکتاتور مهربون ردبول رو امشب میزنی یا فرداشب؟
👀</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/12832" target="_blank">📅 00:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan</strong></div>
<div class="tg-text">دیکتاتور مهربون
ردبول رو امشب میزنی یا فرداشب؟
👀</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12831" target="_blank">📅 00:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پدافند اصفهان فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/12830" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تسنیم : یک منبع نظامی رهگیری پهپاد آمریکایی را تایید کرد
به گفته این منبع نظامی، این رهگیری در اطراف بوشهر از طریق شلیک موشک پدافندی به سمت این پهپاد انجام شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/12829" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درود بر یاشار جان از جم پیام میدم حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد  صدای مهیب و خوبی بود @withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/12828" target="_blank">📅 00:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407ae75cd1.mp4?token=ccHXDHr9KchtTvk3ixwRm69ouqV6FOXqfxwvsfpnOd53LKSkgxxcArG1ut64RDnyW9WoNDJtJlvIKqmFDxSySaPrie7HVMX4zVF4ZDINXIFwqpYwHgRKelE7nZN3Hk4HTYgOZSQA3i-8TL3oS_sVHDCEIHgxhdGccbT85MYFITcL0ILODYw1PIFo1UVnGoOJRWsIJZ4OCuMoVGqSVpSppd_SeaFdZuNewaC8_5oluVPmKpL00JTnh6w3g2I2D5fXY5hi_El7HLeB2ckqEsQwxnVOXbM-12uL-UxvNfmIe9OVMR5JKxkN2e5U4dxvEtQG84bnktuxLRtTBr2r9hvGSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407ae75cd1.mp4?token=ccHXDHr9KchtTvk3ixwRm69ouqV6FOXqfxwvsfpnOd53LKSkgxxcArG1ut64RDnyW9WoNDJtJlvIKqmFDxSySaPrie7HVMX4zVF4ZDINXIFwqpYwHgRKelE7nZN3Hk4HTYgOZSQA3i-8TL3oS_sVHDCEIHgxhdGccbT85MYFITcL0ILODYw1PIFo1UVnGoOJRWsIJZ4OCuMoVGqSVpSppd_SeaFdZuNewaC8_5oluVPmKpL00JTnh6w3g2I2D5fXY5hi_El7HLeB2ckqEsQwxnVOXbM-12uL-UxvNfmIe9OVMR5JKxkN2e5U4dxvEtQG84bnktuxLRtTBr2r9hvGSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها مذاکره‌کنندگان بسیار خوبی هستند آنها زیرک‌اند اما ما همه کارت‌ها را در دست داریم، چون آنها را از نظر نظامی شکست داده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/12827" target="_blank">📅 23:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivitUi1TDf78BO3X8KRpG_77mtpibffKNhAvscB1Y5EUkO4STb3rVq8vpOQ6A1XIy5P7njR8Qbzst7vAfjntU8e9ZPdAjE8i6JeHq6FgaCnGCjbYxIrVj55qQ2djuO62LYUNOs9palhWc9WiUKlOlosu-0N2H-aA-jqTNoSjFry8d1nG3feWBHBootpZ6Pv4quw8jkpUWXg_g8-UMDPPjgfjHbBH-TH6LkzN5osBfjB2-4CvcScFVPs_rOZ7JD9D8rlPwK6fINo1N-m7LCBq6KYNm_GJzeaClbM_Tw7TWnAnwgDakREsLYvXjvQiVEIIPJvsop5vk--08mDYKn5WKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه CNN:  تصاویر ماهواره ای نشان میدهد ایران به سرعت در حال بیرون کشیدن زرادخانه موشکی عظیم خود از زیرِ زمین است
.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12826" target="_blank">📅 23:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ویو از کانال میلیونی ‌بیشتره، ری اکشن از کانال پوشاک زیر کمتر
😕
بد میگین ما ایرانیم چه کاری ازمون برم یاد بکنیم برات !!! خوب اسمت که نمی افته کاملا مخفیه همه پستا و ری اکشن بده دست آدم به کار بره…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/12825" target="_blank">📅 23:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال‌های وابسته به محور شیعه ادعا می‌کنند که ۴ کشتی تجاری آمریکایی پس از تلاش برای عبور از تنگه هرمز بدون اجازه ایران، توسط سپاه پاسداران ایران مورد حمله قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/12824" target="_blank">📅 23:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فارس:  دقایقی پیش نیروهای مسلح ایران از مناطق جنوبی کشور به‌سمت اهداف مشخص موشک شلیک کردند.
بامداد امروز هم پس از تعرض دشمن یه مناطق شرقی بندرعباس پایگاه مبدأ این تجاوز مورد هدف نیروهای مسلح جمهوری اسلامی قرار گرفت.
هنوز هدف دقیق این موشک‌ها مشخص نیست اما برخی منابع از احتمال درگیری بر روی آب‌های خلیج فارس خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/12823" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رسانه های عبری : گزارشهای رسمی از تبادل آتش بین ایران و آمریکا در تنگه هرمز خبر می‌دهند. @withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/12822" target="_blank">📅 23:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با یاشار : یا موسی
💥
یااااا موسیییی</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/12821" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رسانه های عبری : گزارشهای رسمی از تبادل آتش بین ایران و آمریکا در تنگه هرمز خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/12820" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایلنا: شلیک اخطار نیروی دریایی به چهار شناور
نیروی دریایی در نزدیکی تنگه هرمز به ۴ فروند شناور خاطی شلیک اخطار انجام داد. این شناورها قصد عبور بدون هماهنگی از تنگه هرمز را داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12819" target="_blank">📅 23:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رسانه های عبری : گزارش‌های اولیه: موشک‌های کروز «ابومهدی المهندس» از ایران به سمت کشتی‌های آمریکایی در منطقه تنگه هرمز شلیک شدند.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/12818" target="_blank">📅 23:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درود بر یاشار جان از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/12817" target="_blank">📅 23:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اتاق جنگ با شما : هرمزگان و بوشهر هم صدای انفجار میاد
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/12816" target="_blank">📅 23:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اتاق جنگ با شما :  انفجار تو علامردشت فارس  بوده
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12815" target="_blank">📅 23:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتاق جنگ با شما : یاشار مثل اینکه مرز بین استان فارس و بندر عباس و بوشهر رو زدن
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/12814" target="_blank">📅 23:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترور مامور فراجا در ایرانشهر
ساعتی قبل افرادی مسلح به سمت مامور انتظامی شهرستان ایرانشهر که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی کردند که استوار دوم «عیسی عباسی» کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/12813" target="_blank">📅 23:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارشگر: ترامپ گفت که می‌تواند عمان را منفجر کند. آیا شما برنامه‌ای برای یک جنگ جدید با عمان دارید؟  اسکات بسنت:  فکر می‌کنم ترامپ می‌خواست بر آزادی کشتیرانی در تنگه تأکید کند. سفیر عمان به من اطمینان داد که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.…</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/12812" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b307799edc.mp4?token=NZjWZMiEJHdT7gA2EFaFctpgNB8HWt5Gpfu4ZMe0TqY45hcDkW1Li7CG2CmCmwRYtTJG3xWy3dZMv6wKYgQklXIWp4u_gB6kXJU1e77Uvoaid0ruya3hUaYZXd_LQggS1VNxduQi-RsW0wrd4_b8DTj-caIgC1Fn0Dsy1vvcZPdgUUk8Ognc-NhsXOxHf0lyB1TuskFHAlLDhaNu_af4yVIqj1bXRX1Tp2gtUfFyLAOa9G5d_-LQDf4rPPrdg1Omt2R1Go7iOCF07pbLprdyRkxdRagRS22w47tRGIK2BzVEiC4PMvbA18hzUPTZJToZ5Gdt6TTs4vYdmS2dAaGu-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b307799edc.mp4?token=NZjWZMiEJHdT7gA2EFaFctpgNB8HWt5Gpfu4ZMe0TqY45hcDkW1Li7CG2CmCmwRYtTJG3xWy3dZMv6wKYgQklXIWp4u_gB6kXJU1e77Uvoaid0ruya3hUaYZXd_LQggS1VNxduQi-RsW0wrd4_b8DTj-caIgC1Fn0Dsy1vvcZPdgUUk8Ognc-NhsXOxHf0lyB1TuskFHAlLDhaNu_af4yVIqj1bXRX1Tp2gtUfFyLAOa9G5d_-LQDf4rPPrdg1Omt2R1Go7iOCF07pbLprdyRkxdRagRS22w47tRGIK2BzVEiC4PMvbA18hzUPTZJToZ5Gdt6TTs4vYdmS2dAaGu-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ترامپ گفت که می‌تواند عمان را منفجر کند. آیا شما برنامه‌ای برای یک جنگ جدید با عمان دارید؟
اسکات بسنت:
فکر می‌کنم ترامپ می‌خواست بر آزادی کشتیرانی در تنگه تأکید کند.
سفیر عمان به من اطمینان داد که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/12811" target="_blank">📅 22:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با یاشار : موج مکزیکی رو میبینید چقدر زیباست ؟
😍
🌊</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/12810" target="_blank">📅 21:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای سی‌ان‌ان:ترامپ در‌هر حالت  قبل از امضای تفاهم‌نامه با بنیامین نتانیاهو مشورت خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/12809" target="_blank">📅 21:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادعای تسنیم: یک منبع نزدیک به تیم مذاکره‌کننده گفت بر خلاف ادعای برخی منابع غربی مبنی بر اینکه متن اصطلاحاً «یادداشت تفاهم» میان ایران و آمریکا نهایی شده و فقط منتظر اعلام دو طرف است، این موضوع واقعیت ندارد و هنوز متن قطعی نشده است.
وی افزود: ایران تا این لحظه به میانجی پاکستانی اعلام نهایی شدن متن را انجام نداده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/12808" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">: NBC ادعای
آمریکا و ایران سه روز پیش تو دوحه به توافق رسیدن، ولی فعلا اعلامش نمیکنن
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/12807" target="_blank">📅 21:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfpDAj6gQR3g01g-9jsO4Egh49xjsaGJBaZK-gyLXiSYaqWrbj0_-mvLbvVJZVYXKnF04Js4g-a77Sq25kHWGMvMWBz1gD9fTakeNMHp1JtV3vQQ1dDqOmnfizbu6Je2bv4Ezy-6ZYK6OUpokFRjB1irD8nnDBeSIYZbTbcR8DuXjYJkCpN4fx4RYVsOZGfbFygmv-sqkiJCh078bW-eNVvj_nWkq-ReIE6wnUzEN1jC27DP7ylhYhPn36Pchyvzp5cYAWdyHIgYUORoSulaeAA9Hn0IGCNf8p7o8hdmz7jXd9YH_GQs-pBHSAYfFmoovE0UTR3w7RTdET5NwnoQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDIkXraHZ8YBPlmZ9hfTvyc0ILEdr3-XWvp9hFQssr5Y0uOrD7iumpeRO4sE_VUQsjG8kI13i19qDXU2sS10C0VzaEtEbtbVYcsRLgvbXdYNx5CzD3-WWf8hSmQUQKLGXMO8201XgbuYK6kROZWhqahQBXjjNwAbrB2I8mv2F2V8aa2qH7gSjrJzlLie99lpEUNtH6_O6EFHO_sT461rhx3SfRJCidYm3NIWX_GdWPJgmAc1CzV1IFOjXdxL0DOOkmLAT1LdeTM5Q5ASjIcy6KqrRZvf6K0akzE4J4TMjcMQ99XIglmv2ID8Te3l2b_k3iIIMUn0LCMYbPwsYcYBAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتاق جنگ با شما : تو ساحل انزلی ساعتی پیش یه کشتی وسط دریا یهو آتیش گرفت هی منفجر میشه ، ممکنه بار جدید مهمات از روسیه بوده باشه
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/12805" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12804" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12803">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">https://www.ecolo.org/documents/documents_in_english/ramsar-natural-radioactivity/ramsar.html</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/12803" target="_blank">📅 20:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12802">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">آقا یاشار سلام خسته نباشی
❤️
رامسر الان صدای جنگنده اومد یدونه بود نسبت به جنگ خیلی صداش زودتر تموم شد ولی جنگنده بود
پریروزم همین صدا اومد همینقدم بود محلیا میگفتن داره میره سمت روسیه</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/12802" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">@withyashar
😃
وضعیت سیکیم خیاری</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/12801" target="_blank">📅 20:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آمریکا ۲ شرکت هواپیمایی ایران را تحریم کرد
وزیر خزانه‌داری آمریکا نوشت: دسترسی ۲ شرکت هواپیمایی ایران به نقاط فرود، سوخت‌گیری و فروش بلیت مسدود خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/12800" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک منبع اسرائیلی: رهبر ایران، مجتبی خامنه‌ای، این توافق را تأیید نکرده است، و بنابراین ترامپ نیز آن را تأیید نکرده است. قالیباف، رئیس مجلس و عراقچی، وزیر امور خارجه، حتی اگر چارچوب را پذیرفته باشند، مجاز نیستند؛ تصمیم توسط رهبر گرفته می‌شود. ما نمی‌دانیم که آیا هیچ یک از طرفین این توافق را تأیید کرده‌اند یا خیر. اختلافات هنوز هم وجود دارد، حداقل طبق آخرین به‌روزرسانی که اسرائیل دریافت کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12799" target="_blank">📅 18:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12798">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌های رفت و آمد به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/12798" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12797">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:  اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد. ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم. ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در…</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/12797" target="_blank">📅 17:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900d5bba51.mp4?token=O4tJkaa4SG0kpS3dCfYrsELuTgvWW2qATfEwUl24VEnNnGGI2NZRQea-AnH1dcvHJnmiWkRJJ5seGtAlc2ImjfG2vCnHW4dcL5Kj-9QRdmCDAjvwOzbpihUDIfQWgeDqmTDV8A_lHy3MCCckDYQpgA58B1lzmh7Am922-BhkFCKsH81o9VfcMlvWzmeLwNOjQL9ND7_LUNkowPZD6OQFfMElRonTV2YqrvIBBQd9d9XKWnQlicd5AkhAEWOlVYNhvxkXpf_8MtlVy4E0ujbxv8CbwZ0aG1IEMA_R-Gphq4jSJjf6k9FM6tuu3tAObkRleWAAv3Shr211r1L419GG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900d5bba51.mp4?token=O4tJkaa4SG0kpS3dCfYrsELuTgvWW2qATfEwUl24VEnNnGGI2NZRQea-AnH1dcvHJnmiWkRJJ5seGtAlc2ImjfG2vCnHW4dcL5Kj-9QRdmCDAjvwOzbpihUDIfQWgeDqmTDV8A_lHy3MCCckDYQpgA58B1lzmh7Am922-BhkFCKsH81o9VfcMlvWzmeLwNOjQL9ND7_LUNkowPZD6OQFfMElRonTV2YqrvIBBQd9d9XKWnQlicd5AkhAEWOlVYNhvxkXpf_8MtlVy4E0ujbxv8CbwZ0aG1IEMA_R-Gphq4jSJjf6k9FM6tuu3tAObkRleWAAv3Shr211r1L419GG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد.
ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در حال حاضر با حماس درگیر هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/12796" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو:
ما باید ماموریت در ایران را تکمیل کنیم و من تقریباً هر روز در این مورد با ترامپ صحبت می‌کنم.
@withyashar
یاشار : من هم تقریباً زیر تمام پستهاش کامنت گذاشتم بیبی جون، فینیش د جاب</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/12795" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روسیه: ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/12794" target="_blank">📅 17:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیغام فیکی از ترامپ که از یک پیج فیک ایکس است داره میچرخه. ترامپ هیچ پیجی در شبکه ایکس یا توییتر ندارد و فقط در تروسوشال پست میگذارد. این مسئله رو دقت کنید.
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/12793" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ابوترابی، نماینده مجلس: آمریکا بعد از جام جهانی و انتخابات کنگره دوباره حمله می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/12792" target="_blank">📅 17:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سیتنا: تا الان تمرکز ۹۱ درصدی ترافیک اینترنت تو تهران بوده و بازگشت توزیع عادی پهنای باند، زمان‌بره.
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/12791" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6F74jPEctvB1qWEfuZX2e2hTjHdA1Isv_pZKSAXt1sGrHVmD0V6FF__TDuEFbshRxWguTShIycOPAsCLMZvuXDkHoQMmz7HHoqvAIotH6C_j1Q0HWJK8u6TcmDKbsSebWsd6Oh7DfQqGjVP4tK9XdLSDPO674lgR1Np7t1jDlwSkGyayulgdlnICliyIosT1L7y818eqrJoFB2l-mIIgcKYhgu9oTw7iF4F8B_k57HH94qx4WKauBntOwuxf9q_Az-acct3BEtoRxUe0vepyN_rzLLfr_nXljT0gD2uJGsLMV-pUsEoHQCUWVOOhTIJjNgAf-u7RNJQuNChcL-cFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست
:
مقامات دولت ترامپ، اداره حکاکی و چاپ را تحت فشار قرار داده‌اند تا یک اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور طراحی کند، که این اولین بار در بیش از ۱۵۰ سال گذشته است که تصویر یک فرد زنده روی پول رایج آمریکا چاپ می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12790" target="_blank">📅 16:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل گفت که ارتش این کشور با قدرت به حملات علیه حزب‌الله ادامه خواهد داد.
نتانیاهو اضافه کرد که نیروهای اسرائیل از رودخانه لیتانی در جنوب لبنان عبور کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/12789" target="_blank">📅 16:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرگزاری والا به نقل از یک مقام امنیتی اسرائیل: یکی از اهداف در بیروت یک فرمانده ارشد ایرانی بوده است
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12788" target="_blank">📅 15:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام طی بیانیه‌ای ایران را به نقض فاحش آتش‌بس متهم کرد
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/12787" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE-gRihQJGBCStlAghHzVgQ34HE1bamPBMyw-HGNvETqudv11_EbeZosg_Ih1RlRI6Ml2A9byCP2hH6R4vx_VoHWYUEqwO7LLg1gP0mNWM5pJTT9pecHJUprnsP_e_cuVmf1L9yhsCHdzZT1OdaijErXyR4zASufgp4mwLXdKY1anZNndKYtEuIpVHPc8-60T6zWpiA8VCJfI4s8vcTFf_77r_wV51Kt5iEEagWG4PDfgR3DAMqkpmSjeyJeqUWIA3KmuZa0wweIFuphgFunDyv5hvLhF_rjXaeKDDQXmFDFo5AI5iMfnG9Ho5B5SHoHQuX3kocE5abU7Yqy4wEMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های عبری : «علی الحسینی»، مسئول موشکی حزب‌الله در یگان امام حسین به هلاکت رسید
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/12786" target="_blank">📅 14:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به گزارش ان. بی. سی نیوز، پس از ارتش اسرائیل، سنتکام فرماندهی مرکزی آمریکا هم بانک اهداف خود در ایران را به روزرسانی کرد و لیستی از جدید از اهداف را تهیه کرد. هدف‌های راحت‌تر مثل رادارهای ثابت، باندها و هواپیماها تا حد زیادی قبلا زده شدن. چیزهایی که مونده بیشتر زیرزمینی، پراکنده یا سیارن و بدون شناسایی دقیق که ادامه درگیری رو سخت‌تر کرده
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/12785" target="_blank">📅 14:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNp-Q1AfnVJnFLp8-j1kl8VBie82pEF5lM0-WOLSUZkO9DfR_JGkj5xbfid7-0sKcr9KxAMoVv315RNcBvTccWD5-fwxONUgS84cb2stUOGHcAf6uUlczoCf3kLD0S9HizW7m4cYBO-0G1cNJ0skTAx4oPJAEgKULQeo0EfIlTQuDsXvorjBmpR3dTFUF2E0cgb5v66TjSjoaZqyKx0pZLrQxBquVN079E58zNgJ84cIj6yNdQ1PqLbXin1sXdMsfcc0QQYWUUEKO2JqvwaWIeO37oyDpd5jNa2M2OrW1rpz0syYSG7BxWepdlnLYjS0DVCy6Snw_kJ0zU7uxSs4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک Ai موشتبی رو تمدید کردن و موفق شد یه متن طولانی برای سالگرد مجلس بده ، از خالیباف تشکر کرده و به امریکام گفته شیطان بزرگ همین یه امضا بچه ۴ ساله هم با پاورپینت انداختن اون زیر
🤣
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/12784" target="_blank">📅 14:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUWsY0oLw9jRxcZm5BURYjaDxEKNWb3p1TcX2rWi3bS7Bb-G8oSEFLzRZtBMlH-thxCxqqSJsnK4ixo3UZHsdyNhYSw570dUvUHAZoTXNlTIREFqgLRlGiQfYBKJxnPDJSULsmxrFc_KnqjEiGe8CsH_zieU8alsvC3Ckt7rckYuy9xgV5iWFeP_L1LJCtwyyfcIFVUf3Xrk74ctWuUrXpqHS7Y0UY05NiE_TF-q9u7RiMGi4OpCpxcDfsaN3DEwLiBdVChM75nSOguK9GIsA1TVn62K48kQDgfh1rYhsmFbaAKyN350LV3aIjSMkznjfd1eqMmLWWYj0pjQdot-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«روزنامه وال‌استریت ژورنال دیروز گزارش داد که ایران برای دور زدن تحریم‌ها و محاصره آمریکا، از سازوکاری موسوم به انتقال کشتی‌به‌کشتی(Ship-to-Ship) استفاده می‌کند؛ به این صورت که کشتی‌های تحریم‌شده حامل نفت ایران، پیش از ارسال محموله به چین، بار خود را در دریا به کشتی دیگری منتقل می‌کنند.»
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/12783" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSUVulSD1N_KXHMmbnY7cf5hvDZKEr71ZNo8HrG6fJY_Xgxga0rZ3_vdoECbgYJyY4Zg8Do0uXgHOj1SQFU06cZMmckWrNHQl3zoryGirszxuEAbScXotm1tFOq9uJxPzqRbiPJ6qxWupQwIl7K8eTdNH26CTr9iov2gTEaxS3qmhBtHQF_hYBZSUc_J2W_Xm9va2ocYwZEF4nZR6nWJB0yV5SN1PsV2H8tTiAAVY4wgr6gacX0FHd8opf0b3ZA6j_QJoCUmAFDglFXPH1hl1sLVsQcJtsPlQ4c150boSIWoLdTyLq03XhUKLPz1AoYnrPVQYX7wqIH_F-bLMbNWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل دقایقی پیش مجدداً دستور تخلیه فوری کل جنوب لبنان را صادر کرد!
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/12782" target="_blank">📅 12:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مقام‌های آمریکایی گفتند جمهوری اسلامی چهار پهپاد انتحاری را به سمت کشتی‌های آمریکایی و تجاری شلیک کرد، اما جنگنده‌های آمریکا آن‌ها را سرنگون کردند. به گفته این مقام‌ها، جنگنده‌های اف-۱۸ آمریکا همچنین پیش از پرواز پنجمین پهپاد، واحد کنترل زمینی جمهوری اسلامی را در بندرعباس منهدم کردند.
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/12781" target="_blank">📅 12:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/12780" target="_blank">📅 11:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPRRZKjZKCUFT13NEpn3Mdc5Ld3fuFZfw2DSaPij3mqIRMrovefuNn7eL34E8s-9q49uSyzTokALdzR6Y2r0myXNiobaHWUT7gypElBdAxnQSOG5KbODXyaVvq4jkHSJxBFJJRTl5cjLjoJteJqRdjLvW72px2yO4CBdjWV302yH_qNXNIExMndq9DVvA-NAqxtbopIePaJ-RZH9llJS8obBksAd7mxd6Y2S0W0UV-LpSeq8pqUjk5UIetRoZZ4UMNMgrr6qbrU6rawG-EA6uncYBlVZu6gLPWVE-TiZ3AP2Oe11rCTLr52QOuHdxZV8PfHR812DqKKY4FqBwrvMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم ترافیک اینترنت بین‌الملل، تا ساعت ۷ و نیم صبح امروز به ۵۳ درصد حجم پیش از دی‌ماه ۱۴۰۴ رسیده است
@withyashar
حرفم که گفتم اینترنت فقط با رفتن اینا به حالت قبل بر‌میگرده هنوز پا برجاست !</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/12779" target="_blank">📅 11:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/12778" target="_blank">📅 11:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBHz0XHQLdEmnsmJVFNWZ4dOF4TC3nSTzJm_94tERffksZjoe45NfKCJBc6gnZnjEjiyxRXg6d76KqTRdrJBmhzKrKm3XlSRXHSQEjBLI_-kQA9dTHD0BJFphpNhHAeVPsVNMQDs3LQp8ckYhZECwn3zZA6GELcJGAFog1iB6iXjzQbkbhRnpCF4lbRAVdg_3FDq6fidahdeKGozoKpiZ9bIkraGTHAanlMPA3Wqq_MAEBQyX3fzW1vQb_TPJH3zsjMVmHvNtkhSY3UAGjJD36LaEqHLLQJGhXAhF-0PXcBPO_BBaP-2WOohNxClwsf9kOZ3Qm7q_xsr7gnz9yDeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
👏
👏</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/12777" target="_blank">📅 11:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBeobkUdXKBRghSgsKo84ucGhC9ulTOveRu_fQxFLmtWm0FYkhEicy3V5tfWdGkeotYWmGq6jnvkVUnk7vxHicvKr8EMVykCvpcJw7Tu8buHFhJFVwt5eClDwAfmJwHAnlA-UhS6T4L5XraWvN2RYkxPLenfJ9_B7NO0MD11B2diLChcYjCTssXxPmqB5CgirRNIgtdeqy8r6SykDpl4jyKABSemcBX4zkcsQeOV8yjNtBjtM8JUWTXfYoAuJA-TIDVniHqbYzva_7UFUJ77ukNfS_z5jY_4FliZIjrcNZ2bKGKZWmxyNprQtjbAlJf0pr19wEgUBP1K0GgiJlgOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز بعد از شلیک موشک از امیدیه خوزستان به سمت کویت ، صدای انفجار شنیده شده و ستون دود دیده شده که ظاهراً لانچری که موشک ازش شلیک شده بلافاصله توسط ارتش آمریکا مورد هدف قرار گرفته
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/12776" target="_blank">📅 10:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3p4RtDPzqLje_q8QO-Qzhdy31DXgvex7crDVkuMxXYaTpNJQh2-u2J7le4-D13sS33-Hlrp5ezGvE_yxxY4MpBjhEPXLpwaCXDBCOFRLaCBNbiKzN4Ynvrhz46ujWQ5TsHQY6aDp76af44HPEuMSKKTPiEG93Jmc7OiYa6EaMfYRPS55AUkeyMhLjp_kMRd9pz4xv3t7t2F2-K4Dvw7nl9BidEl4_XfZXG2aB3zAv_S0HpiVkLXK4fergcuQ6orxaP34DUH0O-VKXgvXOIpIp1VzpnsoLgOF1oI0mPpkcQAsMaj6D5-PryNV5TOYx1C6gWlmC-CSpk4r4s5qDp3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل، عزالدین البیک، فرمانده تیپ شمال غزه را به هااکت رساند
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12775" target="_blank">📅 10:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRqevLCi-seJAXXdBDl4zE0YrPPvKa8UNiPXmo_SCaJQ3uCIPxLg9y9s7acVbNvSobK8EHo-aVLSNRoEQoCzCPtRYi051dFdj2WRIT2lelMO_O6UIEOB4eGvszTpiCHWDyKpPJ3D5qdNVRjcqlpsK85IGLxeqy4Z2mOIvTMe0S54CKbLkR8bHCfVipbSuLh-qHMKauPEHD35xLMXhlZkQ9VWgRG9Q7rV4IlLgK-Y5G2IBTUm-2R3kj5A9VRPVDCPiFm3LYenff1upe2sXNsuLDrrYwfADFON7z3eqnWsR1RvN-5cRQmNI3hCO0dfHoz7MUrHoax08qMIuhOwERC_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
یک گاومیش آلبینو نادر در بنگلادش که به خاطر دسته موی بلوندش «دونالد ترامپ» لقب گرفته بود، پس از اینکه در فضای مجازی دیده شد، از قربانی شدن در عید قربان نجات یافت.
این گاومیش ۷۰۰ کیلوگرمی قبلاً فروخته شده بود، اما دولت به دلیل نگرانی‌های امنیتی و تجمع جمعیت برای دیدن آن، وارد عمل شد.
مقامات پول خریدار را بازگرداندند و حیوان را به باغ‌وحش داکا منتقل کردند.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/12774" target="_blank">📅 10:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آمریکا «نهاد مدیریت آبراه خلیج فارس» را تحریم کرد
وزارت خزانه‌داری آمریکا اعلام کرد سازمان تازه تأسیس ایرانی «نهاد مدیریت آبراه خلیج فارس»  را به فهرست تحریم‌های خود اضافه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/12773" target="_blank">📅 10:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=VENfzIgsMpAYfE11TfW5AfgRFyLGGuSySzvE_0ENpvXd_rAyCeOhgEZXTZF1MxD2lz53SXM_o7jKQWy44tpbTc5d6H4z7hrbjTxFzrUuFTZ-V3j0DTwH0cdggYXqMWBbzXdgnUaw_LxkB7bLXdq2onlhLatVEJroixnO23bXwB4aqyYrIw2OgQvZKmBX2Ql6bjb8A7v3zC0q8k5l2YhgKSaTSdnEFBHsQbExAPfgJOHkxNm1Y54ykA0EoQ0DOyizSrscQ5AqPmSvluBfTznqySttKFmyLvz5VXsdkC18D07aM9kX-NypdbjUx7NTKnRZ3yDDMy-tLVhycG3OAEH-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=VENfzIgsMpAYfE11TfW5AfgRFyLGGuSySzvE_0ENpvXd_rAyCeOhgEZXTZF1MxD2lz53SXM_o7jKQWy44tpbTc5d6H4z7hrbjTxFzrUuFTZ-V3j0DTwH0cdggYXqMWBbzXdgnUaw_LxkB7bLXdq2onlhLatVEJroixnO23bXwB4aqyYrIw2OgQvZKmBX2Ql6bjb8A7v3zC0q8k5l2YhgKSaTSdnEFBHsQbExAPfgJOHkxNm1Y54ykA0EoQ0DOyizSrscQ5AqPmSvluBfTznqySttKFmyLvz5VXsdkC18D07aM9kX-NypdbjUx7NTKnRZ3yDDMy-tLVhycG3OAEH-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
رد موشک های ۳پا در امیدیه خوزستان که به سمت کویت میرفت
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/12772" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اکسیوس: ایران چهارتا پهپاد انتحاری  به سمت یک ناو نیروی دریایی آمریکا و یک کشتی تجاری پرتاب کرد  نیروهای آمریکایی پهپادها رو رهگیری کردن و همچنین یک واحد پرتاب پهپاد ایرانی دیگه رو روی زمین قبل از اینکه بتوانه شلیک کنه، هدف قرار دادن
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/12771" target="_blank">📅 09:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12770">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فاکس نیوز: آمریکا یه ایستگاه کنترل زمینی ایران رو تو بندرعباس زده؛ همون جایی که قرار بوده یه پهپاد تهاجمی ازش بلند شه.
به گفتهٔ مقام‌های آمریکایی، چهار تا پهپاد انتحاری دیگه هم که تو تنگه هرمز تهدید محسوب می‌شدن، زده شدن.
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/12770" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12769">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۳پا یک پایگاه هوایی آمریکایی را هدف قرار داد
روابط عمومی ۳پا طی اطلاعیه‌ای اعلام کرد:
به دنبال تعرض سحرگاه امروز آمریکا به نقطه‌ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/12769" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12768">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقام آمریکایی به شبکه CBS نیوز گفت : آتش‌بس با ایران پس از حملات امشب همچنان در حال اجرا در نظر گرفته می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12768" target="_blank">📅 03:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12767">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:   ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد @withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/12767" target="_blank">📅 03:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12766">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/12766" target="_blank">📅 03:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12765">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/12765" target="_blank">📅 03:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12764">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه. @withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/12764" target="_blank">📅 03:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12763">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/12763" target="_blank">📅 03:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12762">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/12762" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12761">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8116492af1.mp4?token=QOzUWeGQHlBSNBqxp6yoPbuffSDUAhTNYHEfSDc5CqpkUV7k20J6QIaz_nm4lvqmpOT4xdJZc9KMUcxA2AbtIdRXmaaF6FRHvELV-dVr7nz0W5ldEXT7yreJUIRlz8HS5zaAROx09B8C8i83SEy8PHFwtCGWNdCqJmiFfD5GpOkfHFqtVkCc-k7Woeg24GqWmeY0R8uDsskZdNDKxOH56ChdyFA-wf2JXZuds3UkkDgahztYaHOTaGS3HTkMsYs_YiQ4rbOEe9lYVxLYTvCgVU74EVL50PSp3RYuUNU9L46ZCZz7ic2YHT5RJRDd7RjBGTecgKwHmQozuQd3hQw7tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8116492af1.mp4?token=QOzUWeGQHlBSNBqxp6yoPbuffSDUAhTNYHEfSDc5CqpkUV7k20J6QIaz_nm4lvqmpOT4xdJZc9KMUcxA2AbtIdRXmaaF6FRHvELV-dVr7nz0W5ldEXT7yreJUIRlz8HS5zaAROx09B8C8i83SEy8PHFwtCGWNdCqJmiFfD5GpOkfHFqtVkCc-k7Woeg24GqWmeY0R8uDsskZdNDKxOH56ChdyFA-wf2JXZuds3UkkDgahztYaHOTaGS3HTkMsYs_YiQ4rbOEe9lYVxLYTvCgVU74EVL50PSp3RYuUNU9L46ZCZz7ic2YHT5RJRDd7RjBGTecgKwHmQozuQd3hQw7tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی همکنون در آسمان اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/12761" target="_blank">📅 02:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12760">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbEzszDikDjDuQgdMqr3XQR7LLU6caj6gDUpHllQWV-qdSBgRAz5o7qZaMMdV2buNvKVSGb-_1wp0HOi8Trx6rKK0a3u0q6MC4aXd1mv5G_T9N8zLnQgcjZFY_1Xk0sFgppYybi2GTAOyjKzH7opA0_Ygnalh7wGXlMf0JYhYjXh15OtjrJMH0uKSGh4I8s26nad72IGKIm4KrT5RWJOULkfJfBbWfFDy69D8x04yqjHJqST0tkaOYFpxkHduU8mw-cT8Fpo648PHY0mObwVcbN_pazRTDV1lNMxM5TydpEtW7QjPLJbavTf_Cr7ldQMuAMStQtpIDEFi1sQMZQyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:
ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/12760" target="_blank">📅 02:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12759">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/12759" target="_blank">📅 02:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12758">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/12758" target="_blank">📅 02:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12757">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/12757" target="_blank">📅 02:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12756">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/12756" target="_blank">📅 02:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12755">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یا موسی</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/12755" target="_blank">📅 02:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12754">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پدافند اصفهان فعال شد !
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/12754" target="_blank">📅 02:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12753">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فارس : شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقه هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/12753" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12752">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبر گزاری فارس‌ انفجار رو تایید کرد !!!
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12752" target="_blank">📅 02:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12751">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تایید نشده ۳ نفر‌گفتن ماشین این کاربر‌ با آدرس گفته :
بولوار‌خلیج فارس یه ماشین رو با پهپاد زدنن رفت رو هوا و بعد پدافند با تاخییر شروع کرد فعالیت
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/12751" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12750">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">داداش من بندرم ۳ تا انفجار ۳۰ مین پیش بود و تا ۱۰ مین پیشم صدای پدافند می اومد میگن گویا یه ماشینو زدن و ترور بوده
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/12750" target="_blank">📅 02:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12749">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12749" target="_blank">📅 01:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12748">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چیزی ‌نیست بی بی اومده یه قلیه ماهی ‌بزنه بره
🐟
شلوغش نکنید</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/12748" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12747">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سلام همین الان پدافند بندر عباس درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/12747" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12746">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارشها شما اکثرن به پایگاه هوایی/فرودگاه اشاره میکنه</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/12746" target="_blank">📅 01:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12745">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای سه انفجار در بندرعباس دوباره
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12745" target="_blank">📅 01:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12744">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارشهای ززززیاد از انفجار در بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12744" target="_blank">📅 01:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12743">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کره شمالی تشکیل ائتلاف چهارگانه شامل آمریکا، استرالیا، هند و ژاپن را محکوم کرد. پیونگ یانگ همچنین تاکید کرد که هرگز از برنامه هسته‌ای خود چشم‌پوشی نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/12743" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12742">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=rre6ZZSOFCNmd32yqfHczycezbLv19PU9qudTieJT95uQ_0N0fZV2uAdtjwxUHQ5XEzFzbXozWcbV2qQhIJDSFhTzKwQNtWTLtTny6AKSjf8Jwe4CQxwfpIiQmMPeJnVIXzPnp28CY4ThrhxvGT263clW93s_onBDdgy-eCxMM0yWaUGdU2PvD_2Xix0KlRqi5sW8FZmwKELGjC87yRZBNN3xeJwFh3Is-oVmGEBB0ljJj5PEAM-X05U_gdqUMLmj2P87lC2JheZQcgSTfdr6dggPU1_rHTbBxSBbZ5FKRcIG4mLEoIQjls4_Ye6CN7bWgPOEBidAoWwg9yhwtNmHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e19195ad.mp4?token=rre6ZZSOFCNmd32yqfHczycezbLv19PU9qudTieJT95uQ_0N0fZV2uAdtjwxUHQ5XEzFzbXozWcbV2qQhIJDSFhTzKwQNtWTLtTny6AKSjf8Jwe4CQxwfpIiQmMPeJnVIXzPnp28CY4ThrhxvGT263clW93s_onBDdgy-eCxMM0yWaUGdU2PvD_2Xix0KlRqi5sW8FZmwKELGjC87yRZBNN3xeJwFh3Is-oVmGEBB0ljJj5PEAM-X05U_gdqUMLmj2P87lC2JheZQcgSTfdr6dggPU1_rHTbBxSBbZ5FKRcIG4mLEoIQjls4_Ye6CN7bWgPOEBidAoWwg9yhwtNmHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حتما با پوشک بسته نگاه کنید
⚠️
میگن سیلوستر استالونه بعد از دیدن این ویدیو فروش آنلاین تمام فیلمهای رامبو رو متوقف کرد.
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/12742" target="_blank">📅 00:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12741">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">علیرضا فیروزجا با پرچم فرانسه نفر اول شطرنج جهانو شکست داد
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/12741" target="_blank">📅 00:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12740">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/12740" target="_blank">📅 00:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12739">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عضو تیم رسانه‌ای هیئت مذاکراتی ایران: سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود!
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/12739" target="_blank">📅 23:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12738">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یاشار جان  احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12738" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12737">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromE R F A N</strong></div>
<div class="tg-text">یاشار جان
احساس میکنم این جام جهانی امسال خیلی اتفاقات عجیب و غریبی میوفته ، دنیا باز هم خواهد دید که ما تا تهش پای ایران وایسادیم
☀️
🦁
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/12737" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12736">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم! و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/12736" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12735">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKnow</strong></div>
<div class="tg-text">دایی جان، ایران همش دنبال پوله بخاطر این نیست که پول ندارن به ادماشون بدن؟ نمیشه جاهایی که ربط به دولت داره رو اعتصاب کنیم!
و هر دفعه میگن قراره پولمون رو بدن تا انگار ساکتشون کنه.!!</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/12735" target="_blank">📅 23:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12734">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاهزاده رضا پهلوی جمعه پیش در نشستی با شماری از فعالان رسانه ای  که ویدیو آن الان پخش شده گفت :  تیشرت های سیاه یا ساواک به خصوص و هر چیزی غیر از تم اصلی شیر و خورشید نپوشید این جریان در کمترین حالت ایجاد جنجال میکند و انحرافی است  من واقعاً درک نمی‌کنم این موضوع از کجا آب میخورد و این مسئله نگران‌کننده است.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/12734" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
