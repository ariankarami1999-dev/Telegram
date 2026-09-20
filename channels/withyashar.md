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
<img src="https://cdn4.telesco.pe/file/D2MBelVTSvrvcdkQmlH1G2ecDqMFTw4hTw_YK09b2DIuid47tV_7AC242yoah_4XR7-EVVUtbkxSUMstu83Clnl7MqdTCBk-C6BkZ3GcihwsOjMA2tyJbXm77SE-jnEyFqFuC7KxLA9YwgbZPoS8UMv4l2FQ83lf220wq_LMegGqFoKRRqWospps-vCzjg-eBDNM0LUMEencf5fvTfyUBZ34DjWpO3viHvwk-k3IZhddsGZm76ga7xH7p2WVcDEoMN4Xm4BYOQx9BqqRHD1j3CXgFBn4F6T8vsOby3LQhjCMBflQYvgn2WNgp-QxwLXkJw_JNSJys-g-7L6NhlMa6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-23615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ به فاکس نیوز : ایالات متحده با حوثی‌ها در ارتباط مداوم است و آن‌ها موافقت کرده‌اند که با ما وارد جنگ نشوند.
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/23615" target="_blank">📅 17:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ به فاکس نیوز: با وجود هشدارهایی که به شهروندانمان در سراسر منطقه داده‌ایم. این هفته با هفته‌های دیگر در خاورمیانه تفاوتی ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/23614" target="_blank">📅 17:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز گفت: برخی از مقامات ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به انجام یک توافق باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/23613" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپبه فاکس‌نیوز: من در حال حاضر در "حالت تصمیم‌گیری" هستم و اتفاقات بسیار مهمی در آینده‌ای نه چندان دور رخ خواهد داد. انتخاب‌ها اینها هستند: نابودی ایران، اجازه دادن به فروپاشی اقتصادی آنها، یا امضای یک توافق. آنها باید رفتار بهتری داشته باشند! @WarRoom</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/23612" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cbef80a4.mp4?token=t3vDMao6f7yDdGDXCw3lMBINUzwiINWliVw0kVFwnZWGMB80egp4ZJHTLUdKSpJXWyr9EjrrpI7SijeZcMo74GweI5Xu3vROLW1xmVkA3_HM0jBfH-1L69PdLc6EsXojnaq8kChSlEl_5ksSQL5I1-EZ-T653Y5Yp2LVah3NPo9C9oTeWOKg-YM85ba89LI9rZlo-Ro2lxV6uCrmWlLN21KeiJXR3TV4ut-UvE0kCiY39K8ots9IURQhwQJLABrDMp5J6T6MVMwMnGThqk-4k3oJTvEn7uiN9L8I56vdLuka5y-BtyCeDb8xyg0lIzchwQ9Xx0DH_fwJFO9tu5qbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cbef80a4.mp4?token=t3vDMao6f7yDdGDXCw3lMBINUzwiINWliVw0kVFwnZWGMB80egp4ZJHTLUdKSpJXWyr9EjrrpI7SijeZcMo74GweI5Xu3vROLW1xmVkA3_HM0jBfH-1L69PdLc6EsXojnaq8kChSlEl_5ksSQL5I1-EZ-T653Y5Yp2LVah3NPo9C9oTeWOKg-YM85ba89LI9rZlo-Ro2lxV6uCrmWlLN21KeiJXR3TV4ut-UvE0kCiY39K8ots9IURQhwQJLABrDMp5J6T6MVMwMnGThqk-4k3oJTvEn7uiN9L8I56vdLuka5y-BtyCeDb8xyg0lIzchwQ9Xx0DH_fwJFO9tu5qbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/23611" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/23609" target="_blank">📅 17:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/23608" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رسانه های عبری : انتظار می‌رود ظرف چند ساعت آینده حمله‌ای قابل توجه از سوی آمریکا به «کوه کلنگ گزلا»در ایران یا حمله‌ای بزرگ به حوثی‌ها صورت گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/23607" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZJ5RydnJEIdV-eiKf80Qn4GhwdqsaJm5NCWO0iDw2TYsQ6k3oSHU6np8hBGWfpmxpMwUoiuMLfflQdLpvRaEZOnAXRltjeQ-vkjJsiWeo6S2qgriUrb_f12GoJCGct_7T7JNvZuprlHif_gp-xaO8p47a_u75oQhexR_WZvDxY66cC6zNhb2bL9upqV4q2oA46G7Xl47P2c6gSjXEQlyqTiuqx_8DwGPHlkVZPsH_4sjXWMjVfvvBccijn2n1KCiZU-7cOfk3OEmSCTlKN678Dl-K8OPAAbu1-j-ew1oI6wnVvwpuFEjaEwFMdqknKfATTOQ6GUx44cUgt1ZC0inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس تصاویر ماهواره‌ای «سنتینل-۲» داغ داغ امروز، پایگاه هوایی «العدید» در قطر مملو از هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده است.
این وضعیت نشان می‌دهد که در ساعات پیشِ رو هیچ‌گونه حمله آمریکایی صورت نخواهد گرفت، چرا که انجام چنین اقدامی این هواپیماها را در معرض خطر قرار می‌دهد.
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/23606" target="_blank">📅 16:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23605">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">معاون سیاسی پیشین سازمان صداوسیمای جمهوری اسلامی اعلام کرد که در شب ۱۸ دی ۱۴۰۴ ، معترضان آزادی خواه به ۱۳ مرکز این سازمان در شهرهای مختلف حمله کردند و مرکز
صدا و سیما جزیره کیش به تصرف
آن‌ها درآمد.
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/23605" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">العربیه: مذاکره‌ای در کار نیست و فقط جنگ تکلیف رو مشخص میکنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/23604" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz1fs8z4lNu5gaasbHJPoyknIrcDoLhK4ogeIv-c_H-GZcXRUDP6yj_Xe6QhENw-CpLbpuQCYGKaXja2lKizkpbwcMVX9r1ZcSoMdzcvx8iaKxNIG07SjY-B0i1suHDyscBCFXxWzLmZ4dMc6qMggomLq5WZEmx_TnSyE1GN06TB17faPL1GD2eVzmj3dzcKmqVopQh1HV3rM5ieGTrtcc8QJaaeAr3HwmDTdU6GUwD2R3e4f6ppWoroF_hsQP7Rt6ioybwXMpcvcLRFctmY2vC5cnmFj5FGwLQCOs_B8PHh5013YMJelgt92eUOUjrnM7OB8ZUo1HDsQhSklVumOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
در‌تروث
:
به درخواست جدی ارتش آمریکا و با هدف حفظ امنیت ملی، موافقت کرده‌ام که
طاق پیروزی باشکوهی
را که طرح ساخت آن از دوران جنگ داخلی آمریکا، سال‌ها پیش، مطرح بوده و در
میدان مدور مجاور پل یادبود آرلینگتون
قرار دارد، به یک
مجتمع نظامی درجه‌یک و طاق پیروزی
تبدیل کنیم؛ مکانی برای استقرار و نگهداری و همچنین امکان استفاده سریع از
تعداد زیادی پهپاد
، به‌علاوه
تک‌تیراندازها روی سقف و در محوطه میدان
و همچنین نگهداری و ذخیره
مقادیر زیادی مهمات تک‌تیرانداز
.
هیچ تأسیساتی مانند این در هیچ جای دنیا وجود نخواهد داشت.
از میان ۵۹ شهر و پایتخت بزرگ،
واشنگتن دی‌سی تنها شهر در جهان است که طاق پیروزی ندارد، اما حالا خواهد داشت و با فاصله، بزرگ‌ترینِ همه آنها خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/23603" target="_blank">📅 15:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106a710ba4.mp4?token=hbaW9qltzvJ4TZ8EKbBAyCwsKtUz_HfxAQGllwXYVEIe0juF5BPaXSakJ72Q7pray5bXU-jz3b4w5rlKto4e7Veu1VfJX04ZM3ABfuUT3UCN0yeC69NtjJF-eXdPH7v_vzxC9EQGg9wVfOp2FAUoW9D7ZSMyGrIQDSka429957zNUm-nGG2TqlX_NrrX0QtKWLaQUWs0YT5DX8vq0LuH53Cu2prT709bfXcFseqkIJkGXuLrR9S0ohVEUbZLPGFa7CDtPfr5Fi21jv277TbYXT6gy9TMYWpLJeq5lQdtf1Nr4ePeYZinqauCAOxKhIhNFuvleIPgVvs5Hcw9afBk9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106a710ba4.mp4?token=hbaW9qltzvJ4TZ8EKbBAyCwsKtUz_HfxAQGllwXYVEIe0juF5BPaXSakJ72Q7pray5bXU-jz3b4w5rlKto4e7Veu1VfJX04ZM3ABfuUT3UCN0yeC69NtjJF-eXdPH7v_vzxC9EQGg9wVfOp2FAUoW9D7ZSMyGrIQDSka429957zNUm-nGG2TqlX_NrrX0QtKWLaQUWs0YT5DX8vq0LuH53Cu2prT709bfXcFseqkIJkGXuLrR9S0ohVEUbZLPGFa7CDtPfr5Fi21jv277TbYXT6gy9TMYWpLJeq5lQdtf1Nr4ePeYZinqauCAOxKhIhNFuvleIPgVvs5Hcw9afBk9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی : موشتبی مفقود است
@WarRoom</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/23602" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6RgLz3fkoaKkbS8CgfdlLmXukOaW7r7KMbLQSjn21vglyZivfLPx9SkwjFQii3Nf1ckP9jj7ybPaKWU1_V21z_XzNcPQDX0VJgi7G5cBcbZQVOI312uiU-FukPYDHQjZ_q2DaTCRmr3Ek5KbDaLIxdf41OBnlWCKNqZSUs0m_oYbmXg8bU4u-eGMdFfiqNuBb7uhrkRyLdP2PN0DmZwMMs17VD2Mafrv3AKXsYwCChBjUlURC2dKTbdyQV03vMYo4v2GyPMdvRaF8_InUavZwZZspj2RE32gpsTUPtGM1ytP6aAxynTEe5G0oT_8AXd15QoXmD1J0JR6tfxyzgHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن در جزیره گوام مشاهده شد
@WarRoom</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/23601" target="_blank">📅 15:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز: Anthropic به‌صورت مخفیانه یک آزمایشگاه زیست‌شناسی در منطقه خلیج سان‌فرانسیسکو راه‌اندازی کرده است. این شرکت هوش مصنوعی در حال گسترش فعالیت خود به زیست‌شناسی فیزیکی و استفاده از هوش مصنوعی برای پژوهش‌های دارویی و زیستی است.
@WarRoom</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/23600" target="_blank">📅 15:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مهر: ایالات متحده مجوز لازم را از چندین کشور منطقه برای از سرگیری جنگ گسترده علیه ایران دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/23599" target="_blank">📅 15:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کوین‌دسک:
بیت‌کوین بالای ۸۰ هزار دلار باقی مانده و بازار رمزارزها پس از افت‌های اخیر دوباره تقویت شده است.
در آخرین موج صعودی گزارش‌شده، اتریوم حدود ۷.۳ درصد، XRP حدود ۸.۹ درصد و سولانا بیش از ۱۲ درصد رشد کردند و ارزش کل بازار کریپتو به حدود ۲.۶۶ تریلیون دلار رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/23598" target="_blank">📅 15:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/23597" target="_blank">📅 15:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبر گزاری صدى‌البلد:
جان راتکلیف، رئیس سازمان سیا، به‌طور ناگهانی وارد قاهره شد و با عبدالفتاح السیسی، رئیس‌جمهور مصر، دیدار کرد.
طبق این گزارش، دو طرف درباره همکاری‌های اطلاعاتی و امنیتی و همچنین
بحران ایران و تحولات امنیتی خاورمیانه
گفت‌وگو کردند. جزئیات بیشتری از این سفر اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/23596" target="_blank">📅 15:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">محسن کج بند رضایی در گفت‌وگو با الجزیرة:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا حتی اینکه اقیانوس هند را ترک کنند ، در هر نقطه‌ای از این اقیانوس که باشند، هدف حمله قرار خواهند گرفت..
ما سرعت موشک‌های هایپرسونیک خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تاکتیک های دیگری نیز در اختیار داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/23595" target="_blank">📅 14:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: نیروهای امنیتی ما در حال حاضر در تعقیب مهاجمی هستند که حمله را در بنیامین انجام داد. هیچ مهاجمی در امان نخواهد ماند، همچنین کسانی که به آنها کمک کرده‌اند. ما همه آنها را در غزه، لبنان، یهودا و سامریا پاسخگو خواهیم کرد. همزمان، نیروهای ما یک مهاجم…</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/23594" target="_blank">📅 14:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیانیه قرارگاه تروریستی خاتم‌الانبیا:
اگر آمریکا علیه ایران خطایی مرتکب شود، تمامی مراکز و منافع این کشور در منطقه هدف حملات مستمر، مؤثر و دردناک قرار خواهند گرفت.
همچنین کشورهای منطقه‌ای که با اقدامات آمریکا علیه جمهوری اسلامی همراه شوند،
شریک این اقدامات تلقی خواهند شد و دیگر نباید انتظار خویشتنداری نیروهای مسلح ایران را داشته باشند.
در این بیانیه همچنین آمده است که آمریکا با چراغ سبز برخی کشورهای منطقه
در حال برنامه‌ریزی برای ازسرگیری اقدامات علیه ایران
است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/23593" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نتانیاهو:
نیروهای امنیتی ما در حال حاضر در تعقیب مهاجمی هستند که حمله را در
بنیامین
انجام داد.
هیچ مهاجمی در امان نخواهد ماند، همچنین کسانی که به آنها کمک کرده‌اند.
ما همه آنها را در
غزه، لبنان، یهودا و سامریا
پاسخگو خواهیم کرد. همزمان، نیروهای ما
یک مهاجم دیگر را که قصد انجام حمله در سامریا داشت، خنثی کردند.
من دستور دادم
ارتش و شاباک با نیروهای بیشتری در یهودا و سامریا مستقر شوند، محدودیت‌هایی اعمال شود و عملیات و بازداشت‌ها افزایش پیدا کند
تا امنیت شهروندان اسرائیلی حفظ شود. همچنین دستور دادم
خانه این مهاجم به‌سرعت تخریب شود
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/23592" target="_blank">📅 14:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پولیتیکو گزارش داده محموله‌ای از قطعات اف-۳۵ که از استرالیا برای تعمیر به آمریکا فرستاده می‌شد، در میانه مسیر اقیانوس آرام به هنگ‌کنگ منحرف شده است. سه منبع مطلع گفته‌اند برخی از قطعات این محموله ناپدید شده و پنتاگون نیز مفقودشدن تعدادی از قطعات را تأیید کرده است. این اتفاق باعث نگرانی در کنگره آمریکا شده، چون هنگ‌کنگ تحت کنترل چین است و احتمال دسترسی چین به قطعات و فناوری حساس اف-۳۵ مطرح شده است. کنگره آمریکا اکنون در حال بررسی این ماجراست و هنوز مشخص نیست این انحراف چگونه اتفاق افتاده و آیا قطعات به دست طرف‌های چینی رسیده‌اند یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/23591" target="_blank">📅 13:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رئیس مرکز امور بین‌الملل و مدارس خارج از کشور وزارت آموزش و پرورش ایران اعلام کرد
دولت کویت مدارس ایرانی فعال در این کشور را تعطیل کرده و مانع ادامه فعالیت آموزشی آنها شده است.
او این اقدام را «غیرقانونی» توصیف کرد. جزئیات بیشتری درباره تعداد مدارس تعطیل‌شده و دلیل اعلام‌شده از سوی دولت کویت منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/23590" target="_blank">📅 13:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کوین‌دسک: وزارت خزانه‌داری آمریکا مدعی شد پولی که کشتی‌ها برای عبور امن از تنگه هرمز پرداخت می‌کردند، از طریق صرافی ایرانی «بیت‌بانک» جابه‌جا می‌شده است
؛ بیت بانک از ماه ژوئن مبالغی دریافت‌شده از کشتی‌ها را منتقل کرده و در مجموع صدها میلیون دلار بیت‌کوین نیز به سپاه پاسداران رسانده است. آمریکا می‌گوید این صرافی تحت کنترل بابک زنجانی بوده و بخشی از زیرساخت مالی ایران برای دور زدن تحریم‌ها محسوب می‌شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/23589" target="_blank">📅 13:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رویترز:
سقوط بازارهای خلیج فارس پس از حملات حوثی‌ها ادامه یافت؛ شاخص بورس عربستان
۰.۵ درصد
و شاخص قطر
۰.۹ درصد
کاهش یافت و سهام آرامکو نیز حدود ۰.۶ درصد پایین آمد. نگرانی اصلی بازار، گسترش حملات به زیرساخت‌های انرژی و مسیرهای صادرات نفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/23588" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WArHbAY18X4bQl2aHWHUUunbPWU2iJn3q_iUx_TUmVxogLBvlOQRvwD_gmw6QCQvjbZJ52XMlkYNWl0yfuO6w3xH-2Y6awsqxfXJMxMlZXW40Re7pnCQwWL7IcTlobKYampaq0Xkbw3Ngzm20qwKFpsdQG3Ja6BCD3LuScOAfOJYDLIim7vVu0gmfsTl3OVaIomT31rlLbhUvd_TcpmRzN9iPn0lT8gLYsXj6mkKTIFpefZHTQuHhuU0bRk39xutOI8s0WauVxJO0Q50F5ScFzintY-w4WNUbKVSFrWZ2hhuXM4XSZ_9mkhAqUsw4YrOpztxsw6plEORynwYYW4QIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تصاویر ماهواره‌ای جدید نشان میدهد ایران در حال بازسازی سریع تأسیسات طالقان ۲ است: تصاویر ماهواره‌ای شرکت وانتور از ۱۳ سپتامبر ۲۰۲۶ نشان می‌دهد ایران بازسازی تأسیسات طالقان ۲ در مجموعه نظامی پارچین حدود ۳۰ کیلومتری جنوب‌شرق تهران را با سرعت…</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/23587" target="_blank">📅 13:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dih8RRZP-Vw36KxjRW5ATNEgVJ9KSKolXHlIcI4Ynm-ycQraV_vlwIVvL9kr70CEeUJQBy5eA2yHBb9c2qsjOFlVbHFxTzkVpubQC6umPewHOp6xG0bYZiOg0_xK4PmBLLWYaN5ESlE6ndcvJhcTKeLxUr9La6Hv4lJygNjiMZNNku3o8QfPJr9jsTwkf6uit9rn_i2LCq6GEag_FGwvSENWzJoPZ1M0ifRuOwu6nWJPVPh1FMzzvajBct0pntUWFUVmXoVlCswWDI49MUwwpc5n3dqembLXg7TUWqva24yz7Qw-UKY9AUu25YMGW-UO7CjRcAlx758OS6AXlI_Y8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری جدید برای مقابله با طوفان‌ها :
پژوهشگران با بررسی حدود ۳۰ سال داده‌های هواپیماهای موسوم به
Hurricane Hunters
چهار نشانه را شناسایی کرده که می‌تواند به پیش‌بینی بهتر زمان تقویت سریع یک طوفان گرمسیری کمک کند. این موضوع می‌تواند برای هشدار زودهنگام در برابر طوفان‌های شدید اهمیت داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/23586" target="_blank">📅 13:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پژوهشگران پس از
۵۰ سال
منشأ یک گروه خونی بسیار نادر را کشف کردند. این وضعیت که
AnWj منفی
نام دارد، از سال ۱۹۷۲ شناخته شده بود و حالا مشخص شده به ژن
MAL
مربوط است. بیش از
۹۹.۹ درصد مردم AnWj مثبت
هستند و انتقال خون نامتناسب به افراد AnWj منفی می‌تواند باعث واکنش خطرناک ایمنی شود. این کشف به شناسایی این افراد و پیدا کردن خون سازگار کمک می‌کند و
سیستم MAL به‌عنوان چهل‌وهفتمین سیستم گروه خونی انسان
به رسمیت شناخته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/23585" target="_blank">📅 13:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسپیس‌ایکس مجوز بین‌المللی Starlink Mobile را دریافت کرد
؛ کمیسیون ارتباطات فدرال آمریکا (FCC) در
۱۷ سپتامبر
مجوز فعالیت بین‌المللی سرویس موبایلی استارلینک را صادر کرد. این مجوز گام مهمی برای توسعه فناوری
اتصال مستقیم ماهواره به گوشی‌های معمولی
است؛ فناوری‌ای که استارلینک قصد دارد در نسل بعدی آن، تماس، پیام، اینترنت و خدمات ارتباطی را بدون نیاز به آنتن زمینی در مناطق فاقد پوشش موبایل ارائه کند. البته برای فعال شدن این سرویس در هر کشور، دریافت مجوزهای محلی همچنان ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/23584" target="_blank">📅 13:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رویترز:
یک پیشرفت مهم فناوری در چین اعلام شد.
شرکت چینی CXMT اعلام کرده نسل پنجم فناوری تولید تراشه‌های حافظه DRAM این شرکت وارد تولید انبوه شده است. این فناوری با فاصله ساختاری ۱۱.۹۵ نانومتری طراحی شده و چین می‌گوید می‌تواند تولید تراشه روی هر ویفر را دست‌کم ۵۰ درصد افزایش دهد. این تحول برای چین در رقابت با
سامسونگ، SK Hynix و Micron
اهمیت استراتژیک دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/23583" target="_blank">📅 13:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جنوب لبنان صدای ناله های حسن خرسی میاد @WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/23582" target="_blank">📅 13:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تایمز اسرائیل:
اسرائیل در حال بررسی نقش احتمالی خود در دفاع از عربستان است.
این موضوع در پی گسترش حملات حوثی‌ها و فشار همزمان بر مسیرهای هرمز و باب‌المندب مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/23581" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز:
آمریکا و چین امروز مذاکرات مهمی را در نیویورک آغاز می‌کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، و هه لیفنگ، معاون نخست‌وزیر چین ؛ این مذاکرات چند روز پیش از دیدار ترامپ و شی جین‌پینگ در واشنگتن انجام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/23580" target="_blank">📅 13:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یاهو نیوز :
ارتش تایوان برای نخستین‌بار رزمایش مشترک با چند نوع پهپاد تهاجمی برگزار کرد.
این رزمایش شامل موشک‌های ضدکشتی بومی و سامانه‌های HIMARS نیز بود و رئیس‌جمهور تایوان گفت ارتش در حال تطبیق خود با جنگ مدرن و افزایش تهدید چین است
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/23579" target="_blank">📅 13:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز:
ایران اعلام کرده تنگه هرمز تا تحقق شروط تهران بازگشایی نخواهد شد.
محمدباقر قالیباف، رئیس مجلس ایران، گفته بازگشایی تنگه به اجرای تعهدات آمریکا و برآورده شدن شروط ایران بستگی دارد. همزمان محسن رضایی اعلام کرده تهران هفت شرط برای آغاز مذاکرات با واشنگتن از طریق میانجی‌ها مطرح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/23578" target="_blank">📅 13:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رویترز:
رهبران جهان این هفته برای نشست مجمع عمومی سازمان ملل به نیویورک می‌روند.
نزدیک به ۱۳۰ رئیس دولت و کشور در این نشست حضور خواهند داشت و جنگ ایران، بحران اوکراین، بحران انرژی و خطرات هوش مصنوعی از موضوعات اصلی هستند. ترامپ قرار است بار دیگر در مجمع عمومی سخنرانی کند و پزشکیان و نتانیاهو نیز در برنامه سخنرانی دارند.
شی جین‌پینگ به نیویورک نمی‌رود و به‌جای آن احتمالا مستقیماً در واشنگتن با ترامپ دیدار خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/23577" target="_blank">📅 12:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فرمانداری دزفول اعلام کرد صدای انفجاری که دقایقی قبل در بعضی مناطق شهرستان شنیده شد، به دلیل منفجر کردن و از بین بردن مهمات بوده و مربوط به حادثه یا حمله جدیدی نبوده است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23576" target="_blank">📅 10:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23575" target="_blank">📅 09:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23574" target="_blank">📅 09:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23573" target="_blank">📅 09:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f301cc57.mp4?token=cSRCdeT3Y00sXl9OPX9vRv1UPYvONDJmEfHoRR5Qw1ys6vdsFdDMCI8VHdr_8H8p2FUh9mBt5kcslvR9GbdPQeamdHwpWAPGiOYP8POhyvKO-NxkapQjTAip5c7olhQcA5AfodY_fJDiWzzOk_Yy-2qm0iysECULYk0KZaIJeQ8XdxsaK7072UmeqJKTt9wCD9eBDmRwvCpdnhzAv1GYuu1C7YaPVTmpNs1I1PKsWlaU_dWHBax3FqT0ITtgLdsTRgXn9HRRSTvR5Ojl7Ljhzxex_n6vqrOdwiNNjb4ztvjiYPOvFKXDZecyeJsPLYSbtsQWSmfApcgyLcRoSEXEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f301cc57.mp4?token=cSRCdeT3Y00sXl9OPX9vRv1UPYvONDJmEfHoRR5Qw1ys6vdsFdDMCI8VHdr_8H8p2FUh9mBt5kcslvR9GbdPQeamdHwpWAPGiOYP8POhyvKO-NxkapQjTAip5c7olhQcA5AfodY_fJDiWzzOk_Yy-2qm0iysECULYk0KZaIJeQ8XdxsaK7072UmeqJKTt9wCD9eBDmRwvCpdnhzAv1GYuu1C7YaPVTmpNs1I1PKsWlaU_dWHBax3FqT0ITtgLdsTRgXn9HRRSTvR5Ojl7Ljhzxex_n6vqrOdwiNNjb4ztvjiYPOvFKXDZecyeJsPLYSbtsQWSmfApcgyLcRoSEXEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» یهو با صدای بلند تو خیابون شروع کرد به آواز خوندن که یه هموطن اینطوری رید بهش و با یه خفه شو کار رو بست تا مزاحم مردم نشه
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23572" target="_blank">📅 09:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb269a37.mp4?token=a5ZlesRgkiN_bp9SylyKr_5a6Lv7uHlEr5VqPubkHuz_94hiJZzAgTFW2bH6Q5GF7BKeS6XNLvQYYT-689y8qvrhvneMuSUuTHP3M7DOmU_MGgwLtwH6HLWFZQF9SCFoPCsTHebZKzZyODggvvCV7l6P1SHv7fNbFGtBP5h6wSB2lf4Y7K1b-qO4U8MV3liYiNQ6BNUv4RU3kbQW_MjUHYmY6PN88uqDlnRm8cjANZPAhMY-UPz21NKix3w9FJ_U77365kLj4m4LsEbmdfiCjoX00nnB90ttIB8NYHR0W2iYMarCg-AgAgMrXB1oNrn0VZUQWk-aj3sks7VJLrJrRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb269a37.mp4?token=a5ZlesRgkiN_bp9SylyKr_5a6Lv7uHlEr5VqPubkHuz_94hiJZzAgTFW2bH6Q5GF7BKeS6XNLvQYYT-689y8qvrhvneMuSUuTHP3M7DOmU_MGgwLtwH6HLWFZQF9SCFoPCsTHebZKzZyODggvvCV7l6P1SHv7fNbFGtBP5h6wSB2lf4Y7K1b-qO4U8MV3liYiNQ6BNUv4RU3kbQW_MjUHYmY6PN88uqDlnRm8cjANZPAhMY-UPz21NKix3w9FJ_U77365kLj4m4LsEbmdfiCjoX00nnB90ttIB8NYHR0W2iYMarCg-AgAgMrXB1oNrn0VZUQWk-aj3sks7VJLrJrRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاله سینا اشکبوسی جاویدنام ۱۶ ساله در مراسم کوروش کبیر دو از شدت تأثر از حال رفت
@WarRoom
💔</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23571" target="_blank">📅 09:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e48ca2a7.mp4?token=tG-F3W7PaMYfhQY-CZZmLAKDm-tMJB2ogjOHC_mPBLA4pNMvfd9OuBnBtQLP9wQ9UyBe18dmm0vTNvJ8RyIUwQdusnmxwmUa2iUO6loVojkLRuM1RTMI3oe9_qPfldDEkZPg37TN40ekrm55pzS3R2eslLzzQG6ghQ4v25kL61RMn4uwHk-hXaflt6qa627jchgBu3GPtPr1vDvmZaIqD0cyKK0HF8EcvBfe7FTVFSqeVGKyfWnNR1RSqws_lNIrbCZqLS8j5ElixEuUbvJwQo0iZR1ffFg94qihYQ7N2w6_Gbcy898wHp97wfSYqIY_E4SZZfOuDX8Yu9IJmnOlGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e48ca2a7.mp4?token=tG-F3W7PaMYfhQY-CZZmLAKDm-tMJB2ogjOHC_mPBLA4pNMvfd9OuBnBtQLP9wQ9UyBe18dmm0vTNvJ8RyIUwQdusnmxwmUa2iUO6loVojkLRuM1RTMI3oe9_qPfldDEkZPg37TN40ekrm55pzS3R2eslLzzQG6ghQ4v25kL61RMn4uwHk-hXaflt6qa627jchgBu3GPtPr1vDvmZaIqD0cyKK0HF8EcvBfe7FTVFSqeVGKyfWnNR1RSqws_lNIrbCZqLS8j5ElixEuUbvJwQo0iZR1ffFg94qihYQ7N2w6_Gbcy898wHp97wfSYqIY_E4SZZfOuDX8Yu9IJmnOlGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن با غیرت از مایک جانسون، رئیس مجلس نمایندگان آمریکا، می‌خواهد کار نیمه‌تمام را تمام کند و به این رژیم پایان دهد. مایک جانسون ماه پیش هم در سخنرانی خود در مورد حملات به ایران گفته بود که
ما سر مار را زدیم
و همچنین در ابتدای جنگ هم گفته بود مردم ایران دهه‌ها زیر یک رژیم تروریستی استبدادی زندگی کرده‌اند و اگر تغییر رژیم در حال رخ دادن باشد، این می‌تواند برای مردم ایران فرصتی برای چشیدن آزادی باشد.
مردم ایران باید برای به‌دست آوردن و حفظ آزادی قیام کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23570" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=OkX3BX1N82vta4zuVJIxxB3XKyLdceXP3iKLZ84qxRpyx4nvaxBvgzwekjbkiGk4pYNBFypeKZVuwMoE8oDBBQi7QrFqR0Umfy4iuZ-mEyHWSOY5TFUdc-culFHNf0zjAUPX4ST9w85jh6JnEmeGKiJ-S_LDP6kHvGYFpg-SbOZom5lAgIdvQ46jxvtmr-YE-sbUWqRa88e8FDUC4LS8kofPPtLDq1cyhBsSb3H-lbseFCSU-tpACJFWvZtPksgIB8LC0Ds08-qZ-dOA_UETVgaPkdvxeT5h-qZ1u9L8vkBneXPZXHHClhtIcbNFB9ARvxGfsFlARR9BEOG4HnZQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=OkX3BX1N82vta4zuVJIxxB3XKyLdceXP3iKLZ84qxRpyx4nvaxBvgzwekjbkiGk4pYNBFypeKZVuwMoE8oDBBQi7QrFqR0Umfy4iuZ-mEyHWSOY5TFUdc-culFHNf0zjAUPX4ST9w85jh6JnEmeGKiJ-S_LDP6kHvGYFpg-SbOZom5lAgIdvQ46jxvtmr-YE-sbUWqRa88e8FDUC4LS8kofPPtLDq1cyhBsSb3H-lbseFCSU-tpACJFWvZtPksgIB8LC0Ds08-qZ-dOA_UETVgaPkdvxeT5h-qZ1u9L8vkBneXPZXHHClhtIcbNFB9ARvxGfsFlARR9BEOG4HnZQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد..
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23569" target="_blank">📅 09:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فیزیک
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23568" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ویدیو اختصاصی زیبا از دیشب
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23567" target="_blank">📅 07:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دیدبان اتاق جنگ : ديشب چندتا موشك خورده ب قايق هاي سپاه داخل قشم  جزايره ناز سوزا ، شايدم قايق صياد های بسیجی بوده که میرن شهپاد های آمریکارو بدزدن بوده معلوم نيست ، ولي برخورد انجام شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23566" target="_blank">📅 07:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=NUk7rBO6WUXbuc3nSXTME4LF5n7AN4cqXS7Am-9dab1tFXsf9PvmgboAI9tLS_lD8kOR6RJexEXF26S6ciVKm8AdifMgPAHQmkquBlbvsRgjKV7b08hWKocqFly1O6qjCwtz0UoI0C79K0aTCCgf1di8JR-iJMJNc82rwPEk9O4SGE9pC-3h-29RfGIo1BKkhpa6Dt8prHM4kkh8WFUBxFerAaf1zYvfh3P9RGV4dX6HRwq5pzqzS786GDYXaPC48VJN2hQgcAWPpZNLO3ysCwkS2FiXg6t9QPBO95OoPt7OpswCGoAYhGVxUtSiVPjSvHBK2VNQNCyWPIzTsFX-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=NUk7rBO6WUXbuc3nSXTME4LF5n7AN4cqXS7Am-9dab1tFXsf9PvmgboAI9tLS_lD8kOR6RJexEXF26S6ciVKm8AdifMgPAHQmkquBlbvsRgjKV7b08hWKocqFly1O6qjCwtz0UoI0C79K0aTCCgf1di8JR-iJMJNc82rwPEk9O4SGE9pC-3h-29RfGIo1BKkhpa6Dt8prHM4kkh8WFUBxFerAaf1zYvfh3P9RGV4dX6HRwq5pzqzS786GDYXaPC48VJN2hQgcAWPpZNLO3ysCwkS2FiXg6t9QPBO95OoPt7OpswCGoAYhGVxUtSiVPjSvHBK2VNQNCyWPIzTsFX-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن
B-1B Lancer
آمریکا امشب با پس‌سوز کامل از پایگاه
RAF Fairford
در بریتانیا برخاست. برخاستن با پس‌سوز معمولاً نشان‌دهنده وزن بالای هواپیما و احتمال حمل محموله تسلیحاتی سنگین است، هرچند در پروازهای آموزشی هم استفاده می‌شود. حدود
۱۲ فروند B-1B
همچنان در فرفورد مستقر هستند و این پایگاه از ماه مارس یکی از مراکز اصلی عملیات
Epic Fury
علیه اهدافی در ایران بوده است.
در اطراف پایگاه نیز برخی خبرنگاران و عکاسان هوانوردی شبانه‌روز در مستقر می‌شوند
و با هر پرواز سریعاً عکس و فیلم تهیه می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23565" target="_blank">📅 06:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نوراد: یک جنگنده اف-۱۶ یک هواپیمای غیرنظامی را که وارد حریم هوایی ممنوعه کمپ دیوید در مریلند شده بود، رهگیری کرد. این حادثه ساعت ۱۵:۲۰ به وقت تهران (۷:۵۰ صبح به وقت محلی) رخ داد. جنگنده برای برقراری ارتباط با خلبان، شراره‌های هشدار شلیک کرد و سپس هواپیما را…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23564" target="_blank">📅 06:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزارت امور خارجه ایالات متحده:
احتمال تشدید درگیری بین عربستان سعودی و حوثی‌های تحت حمایت ایران , آمریکایی‌های خارج از خاورمیانه باید سفر به این منطقه یا عبور از آن را به طور جدی مورد بازنگری قرار دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23563" target="_blank">📅 06:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=iFIH5e2CGH5kM18oPYdVpxbPYGEbpUUMAChqHxWoEwp-Ro4lyRU1fTXqjUIaMxYzaGRGZZgO0DXD8ZZpATU5kjs4g5LfCLYpro3L6ZCXLbjyJAdkb1PubFwpOJjCU9GAdet0ZQYCNCR25PF9aqy7NU5PZwnp2BstjraWPR5jpNzL9D-mpU4FZ2OmJjlh9WS6WGJRMyb3xEs8Gmzun5J95-lnOedq0q86Bg14HCtfiWog2VsvqYUj8n4Qe-E8D8xI10P4G2C9gPe_axCl6tUs50fxiJedCybm7z-Cfb7n8bfh7OD6gORrXyGWBWMpnMZaIA4uctowOyfKiT6MYWel3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=iFIH5e2CGH5kM18oPYdVpxbPYGEbpUUMAChqHxWoEwp-Ro4lyRU1fTXqjUIaMxYzaGRGZZgO0DXD8ZZpATU5kjs4g5LfCLYpro3L6ZCXLbjyJAdkb1PubFwpOJjCU9GAdet0ZQYCNCR25PF9aqy7NU5PZwnp2BstjraWPR5jpNzL9D-mpU4FZ2OmJjlh9WS6WGJRMyb3xEs8Gmzun5J95-lnOedq0q86Bg14HCtfiWog2VsvqYUj8n4Qe-E8D8xI10P4G2C9gPe_axCl6tUs50fxiJedCybm7z-Cfb7n8bfh7OD6gORrXyGWBWMpnMZaIA4uctowOyfKiT6MYWel3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در رویداد «کوروش کبیر ۲» در تورنتو : «حماسه دی» نتیجه یک هیجان زودگذر نبود؛ پشت آن یک مسیر طولانی و پرهزینه بود. جمهوری اسلامی که در روزهای ۱۸ و ۱۹ دی سقوط خودش را قطعی می‌دید، دست به یکی از بزرگ‌ترین جنایت‌های تاریخ زد. ما امروز از همیشه باتجربه‌تر و مصمم‌تریم. هدفمان مشخص است: سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد. چهار اصل اصلی ما هم روشن است: حفظ تمامیت ارضی ایران، جدایی دین از حکومت، آزادی‌های فردی و برابری همه شهروندان در برابر قانون، و اینکه مردم خودشان با رأی آزاد و عادلانه شکل آینده حکومت ایران را تعیین کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23562" target="_blank">📅 01:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سفارت آمریکا در لبنان، بغداد، بحرین و اردن نیز هشدار مشابهی دادند. @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23561" target="_blank">📅 01:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23560" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efc866236.mp4?token=tD7TalbxxuVWrVKc_HQxb-IXzSjB0Y7jkO9CMeAq75MCvdxxCgqGyPM3Vhp3e-s6AlekSdkBwgYbkIBhHLbiXXiPfEgsrjS6w7LN-FxoKagGh9TsQxl3hwqQh-K_nJL4pl7KZai-zcZnL0p2DdJeI2hD-ULSWZBoKAlQWRx6KCT1L5gZwvRLlYgYxrxusBaTf48A7jWlSqHiQ7u-o3njhX1HvmzETcbA8-eYiS2iROcdMMJVG7nbttCTz_rQm7Ud-8eZHuIVQG0ooD6CK5HIhjDlQ8YPrgnst0ADNsTOUG4jbaMoNamrVidHVxvAXbf_aEIssBd15KSHHhgekzumVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efc866236.mp4?token=tD7TalbxxuVWrVKc_HQxb-IXzSjB0Y7jkO9CMeAq75MCvdxxCgqGyPM3Vhp3e-s6AlekSdkBwgYbkIBhHLbiXXiPfEgsrjS6w7LN-FxoKagGh9TsQxl3hwqQh-K_nJL4pl7KZai-zcZnL0p2DdJeI2hD-ULSWZBoKAlQWRx6KCT1L5gZwvRLlYgYxrxusBaTf48A7jWlSqHiQ7u-o3njhX1HvmzETcbA8-eYiS2iROcdMMJVG7nbttCTz_rQm7Ud-8eZHuIVQG0ooD6CK5HIhjDlQ8YPrgnst0ADNsTOUG4jbaMoNamrVidHVxvAXbf_aEIssBd15KSHHhgekzumVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23559" target="_blank">📅 01:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23558">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رضاتون کجاس حرومی?</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23558" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a9813c09.mp4?token=k8EZCuBVAIX8Hwd3yLITiZZ6Dgk105ze0epI9JcsJSBKiqrEoZxa_8UN6gePtgN9p9qSe4GVuMLJXg0jC1TI-B-R0UHZZnGJiPoaRHLxvweTF9sTKPr8FRYmYWcy2awJ6O4b2l4Gl9yKGZh99ZMRAW9asBCI9Zmtl11yIrGz5BsKDIEDzFpI_71a5r6GOyODqdOQgfrj-b2_zZWem2qugEUrGvkN6vV4Shdg0K9U_jyo_hpTZIDxTWyy4QiYQalc3z1xr4M5qGHudnW6uKIAqUDjl98gzzPzuQTJ7ya-LLydh2UdGBncCVVvF1VMBSmNb6usxWsWMfPEZP3IR9E_CU5bCFypcy0l9IePHDNQ7f_Ozdf6ALKbY4zCq216cx69ONxSyRE_su25dprPSUW0N2lEH8wURs-yw-7L4GQrhfp6NGz7nvfTBQA4-xneJ_ljS0ZTjWJKeoJ-TyvPphmtEJeLprYpLmQioMOxA0PaqyZyZiZtU_d_iHNlJcxCFpLsof2D229OSHrtWdT9pZjg4MvPfy7X7XqQo9T3i9Wq7jE8IlLesHqw4-FKWIgOu9Cr-xu7XcRuLdbpHO_4mr4yAPHzX1p_or74DymQull4WtJ6781HVamMRdeqcLrCUTcsHBQMJ3etZfdr5DcduzmIhsa7m0D2G4L94toS1Pxol8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a9813c09.mp4?token=k8EZCuBVAIX8Hwd3yLITiZZ6Dgk105ze0epI9JcsJSBKiqrEoZxa_8UN6gePtgN9p9qSe4GVuMLJXg0jC1TI-B-R0UHZZnGJiPoaRHLxvweTF9sTKPr8FRYmYWcy2awJ6O4b2l4Gl9yKGZh99ZMRAW9asBCI9Zmtl11yIrGz5BsKDIEDzFpI_71a5r6GOyODqdOQgfrj-b2_zZWem2qugEUrGvkN6vV4Shdg0K9U_jyo_hpTZIDxTWyy4QiYQalc3z1xr4M5qGHudnW6uKIAqUDjl98gzzPzuQTJ7ya-LLydh2UdGBncCVVvF1VMBSmNb6usxWsWMfPEZP3IR9E_CU5bCFypcy0l9IePHDNQ7f_Ozdf6ALKbY4zCq216cx69ONxSyRE_su25dprPSUW0N2lEH8wURs-yw-7L4GQrhfp6NGz7nvfTBQA4-xneJ_ljS0ZTjWJKeoJ-TyvPphmtEJeLprYpLmQioMOxA0PaqyZyZiZtU_d_iHNlJcxCFpLsof2D229OSHrtWdT9pZjg4MvPfy7X7XqQo9T3i9Wq7jE8IlLesHqw4-FKWIgOu9Cr-xu7XcRuLdbpHO_4mr4yAPHzX1p_or74DymQull4WtJ6781HVamMRdeqcLrCUTcsHBQMJ3etZfdr5DcduzmIhsa7m0D2G4L94toS1Pxol8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شاهزاده در همایش کوروش ۲ در کانادا، همچنین ۲ جنرال کانادایی هم در تصویر دیده میشوند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23557" target="_blank">📅 00:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">رضاتون کجاس حرومی?</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23556" target="_blank">📅 00:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جنوب لبنان صدای ناله های حسن خرسی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23555" target="_blank">📅 00:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چند گزارش از فعالیت کوتاه پدافند شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23554" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال
بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد
وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/23553" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پدافند شرق تحرک ریزی انجام داد قطع شد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23552" target="_blank">📅 23:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انتخابات پارلمانی روسیه در حالی ادامه دارد که مقام‌های روس از
حملات سایبری به سامانه رأی‌گیری و شبکه‌های ارتباطی
خبر داده‌اند. مسکو اوکراین را متهم کرده، اما برای این اتهام مدرکی ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/23551" target="_blank">📅 23:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نوراد: یک جنگنده
اف-۱۶
یک هواپیمای غیرنظامی را که وارد
حریم هوایی ممنوعه کمپ دیوید
در مریلند شده بود، رهگیری کرد. این حادثه ساعت
۱۵:۲۰ به وقت تهران
(۷:۵۰ صبح به وقت محلی) رخ داد. جنگنده برای برقراری ارتباط با خلبان،
شراره‌های هشدار
شلیک کرد و سپس هواپیما را به‌سلامت از منطقه خارج کرد.
دونالد ترامپ
هنگام این حادثه در کمپ دیوید حضور داشت
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23550" target="_blank">📅 22:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رویترز: دونالد ترامپ اعلام کرد آمریکا یک «نیروی هوش مصنوعی» تشکیل خواهد داد؛ طرحی که به گفته او مشابه نیروی فضایی است که در دوره اول ریاست‌جمهوری‌اش ایجاد کرد. ترامپ همچنین گفت به‌زودی یک «تزار هوش مصنوعی» برای نظارت بر این طرح منصوب خواهد کرد. هنوز مشخص نیست این نیرو یک شاخه نظامی مستقل خواهد بود یا یک نهاد فدرال برای نظارت و توسعه هوش مصنوعی.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23549" target="_blank">📅 22:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رویترز: کره‌جنوبی اینبار اعلام آمادگی کرد در بازگشایی هرمز مشارکت کند
؛ وزیر خارجه کره‌جنوبی در دیدار با مارکو روبیو اعلام کرده سئول آماده است «مشارکت اساسی» در بازگرداندن عبور آزاد کشتی‌ها از تنگه هرمز داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23548" target="_blank">📅 21:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آسوشیتدپرس: زنان بدون حجاب در یک مسابقه دو در تهران شرکت کردند
؛ صدها زن بدون حجاب اجباری در یکی از بزرگ‌ترین نمایش‌های نافرمانی اجتماعی در سال‌های اخیر در یک مسابقه دو در بوستان ولایت تهران شرکت کردند. همزمان در همان روز تجمعی حکومتی در تهران برگزار شد و زنان محجبه در حمایت از حکومت و جنگ حضور داشتند.وزارت ورزش از یک ماه قبل مجوز داده بود ولی دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23547" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الجزیره: ۱۱ سرباز سوری در انفجار انبار مهمات کشته شدند
؛ انفجار در یک موضع نظامی در منطقه عیّاش در استان دیرالزور رخ داده و ۹ سرباز دیگر زخمی شده‌اند. علت انفجار هنوز مشخص نیست و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23546" target="_blank">📅 21:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق روایت و ویدیو منتشرشده، چند جوان در خیابان دانشگاه زاهدان با خودرو در حال تردد بودند که ناگهان گلوله‌ای به سمت خودرو شلیک شد؛ گلوله گردن سرنشین صندلی شاگرد را خراش داد و از کنار گوش سرنشین عقب عبور کرد. گفته شده حال افراد داخل خودرو خوب است. در مقابل،
خبرگزاری فارس
گزارش داده بامداد جمعه حدود ساعت ۱۲:۳۰، نیروهای امنیتی به یک خودروی پژو مشکوک شدند و پس از مشاهده سلاح در خودرو، درگیری رخ داد که در جریان آن
۳ نفر کشته شدند
. درباره ارتباط این دو روایت، اطلاعات مستقلی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23545" target="_blank">📅 21:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واشینگتن پست: رئیس‌جمهور ترامپ در اظهارات علنی خود همواره تأکید کرده است که سیاست‌های انتخاباتی میان‌دوره‌ای بر تصمیمات او درباره ایران تأثیری ندارند.
اما ترامپ در محافل خصوصی نشان داده است که می‌داند تصمیماتش در شکل‌گیری فضای سیاسی نامساعدی که حزبش با آن مواجه است، نقش داشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23544" target="_blank">📅 21:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: متأسفانه دیوان عالی آمریکا شجاعت لازم برای «دوباره بزرگ کردن آمریکا» را نداشته است. آنها در شش ماه گذشته با تصمیم‌های سیاسی، نادرست و مضحک خود درباره تعرفه‌ها و حق شهروندی از طریق تولد، تریلیون‌ها دلار به ایالات متحده خسارت زده‌اند و برای همیشه به نحوه شهروند شدن افراد در کشور بزرگ ما آسیب وارد کرده‌اند. این فصل غم‌انگیزی در تاریخ آمریکا بوده، اما ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23543" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ixz-glnQ4UPtXPStuGdxo46w9l8SaeIDUPW_pX4C09q9UgMj0E3YjfMnlMQOh0B3zMkqoScfrdbcGpPJzHNsPF6nIsluAYDdLujofQrWZT1T0HrCcE1vYm65PI37z2DrFpYLWA4gFLPePo53K7ZC08DvQB3SDskVmXOYQ3ASm-TWjYvw9DcOKDyLy8AOjtlw0Yg5U04fLmvAQcybQ_lKh3XfOS5LaqvtXVrwjD4d38be1dj4s0yu7TSB7zoT1zIO765Iyhj07jbUeKKRXo53KdUNl9J6_DSV33D0NRsgONjwE07jWXX99v94QXMAFGCn8S5D3j-oMkAgw72ZJQnPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژه جن فدا ها ، اخطار اگه تصویرو زوم کنید ‌شب ادراری‌ میگیرن
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23542" target="_blank">📅 20:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال 13 اسرائیل:
قطر شروط تهران برای پایان جنگ را به آمریکا منتقل کرده و ایران اکنون منتظر واکنش دونالد ترامپ است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23541" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرگزاری i24news : بنیامین نتانیاهو سفر خود به آمریکا را کوتاه کرده و برخلاف برنامه قبلی، به تگزاس نمی‌رود و دیدار برنامه‌ریزی‌شده با ایلان ماسک نیز لغو شده است. نتانیاهو اکنون قرار است پنجشنبه مستقیماً به نیویورک برود، در مجمع عمومی سازمان ملل سخنرانی کند و بلافاصله پس از آن به اسرائیل بازگردد. در برنامه فعلی همچنین دیداری با دونالد ترامپ وجود ندارد؛ مقام‌های آمریکایی دلیل آن را محدودیت زمانی و تفاوت برنامه سفر دو رهبر اعلام کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23540" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک لوین بازنشر کرد
صحبتهای
، رندی فاین، نماینده کنگره آمریکا:
شبکه‌های اجتماعی، اینفلوئنسرها و اعتراضات، همگی برای
بی‌ثبات کردن آمریکا از داخل
طراحی شده‌اند. بخش زیادی از این اقدامات توسط
روسیه، چین، ایران، ترکیه و قطر
تأمین مالی می‌شود. ما باید همین حالا درباره این موضوع صحبت کنیم تا مردم
قبل از اینکه خیلی دیر شود، بیدار شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23539" target="_blank">📅 19:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدای انفجارهای کنترل شده در ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23538" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آکسیوس: جنگ ایران باعث افزایش شدید قیمت بنزین و گازوئیل در سراسر جهان شده و فشار اقتصادی و تورمی را حتی به کشورهایی که مستقیماً در جنگ دخالت ندارند منتقل کرده است. دولت‌ها اکنون با افزایش هزینه سوخت و فشار عمومی مواجه‌اند و در صورت ادامه جنگ، احتمال تشدید این فشارها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23537" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">محسن رضایی به شبکه الجزیره گفت:
از نظر واشنگتن، پذیرش شرایط ما برای خروج از جنگ، کار درستی است. تهدیدات ترامپ هیچ نتیجه‌ای نخواهد داشت و ما برای یک جنگ قاطع آماده هستیم. ارزیابی‌ها و محاسبات رئیس جمهور آمریکا درباره ایران نادرست بود و جنگ با تحریک نتانیاهو آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23536" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=RkFz8YHQexy8t68VqX4IkuVQHtywvMz6L_ChyHJ2vFz8lTp477KuByn7Gew8iVbP3IBdGcCr757jvNxgHjdXlcy-qH6Vj7pMKR3qek0qPSiD4NVZcfOGP4GJTUxdCDyJdzpQ9_xVIwjGiNk3dzOhWQ6aaM2Db8zgYq8ZEEsHkmuMQvKxgZaAJR1_CoOCLUBhx3ezF2zfv300OlecRqxR0HoIMia1m1oEetQthYshy_eUIW3DUvepq8JnqxTekXDRJ_gw9HiT2-kax4PZxTuACNPIb6JKukm5ZdPN50j3nzsDO48V6aT2WoeUei-7CA99_3wxYRc4hBBgcbYsSHCOg0eywP0kY8qOm_OKdrmJjhJztn4nIZLldz5qbmW7RLn8MzeUqhUUkWuOsjQfB1GXmp3eqmbhzmnmaY31IOJ8C0edhZKRwCGByKjdCub10hV77BEwAkmnK6h2eh3ArmzdqUkif1lpjSy-bWtUmlmZLTIi0i-VmzM_3XTdpcdCT87-sARVJ-xy47ZEwSNtdYmEFhw0oFHBXatViuwSsnFBq6QzhmuR-pOH248g-Oq02a7NXQFjGTMZifR9y8vVHbFGLgtqzSVUuO9Ter8bnq1WBU4tbQLEX6xxoAscYZiYmlyhN8GSjbJRwJ968AtfyZy4jkenFbSWiZFNe2IF61BBdLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=RkFz8YHQexy8t68VqX4IkuVQHtywvMz6L_ChyHJ2vFz8lTp477KuByn7Gew8iVbP3IBdGcCr757jvNxgHjdXlcy-qH6Vj7pMKR3qek0qPSiD4NVZcfOGP4GJTUxdCDyJdzpQ9_xVIwjGiNk3dzOhWQ6aaM2Db8zgYq8ZEEsHkmuMQvKxgZaAJR1_CoOCLUBhx3ezF2zfv300OlecRqxR0HoIMia1m1oEetQthYshy_eUIW3DUvepq8JnqxTekXDRJ_gw9HiT2-kax4PZxTuACNPIb6JKukm5ZdPN50j3nzsDO48V6aT2WoeUei-7CA99_3wxYRc4hBBgcbYsSHCOg0eywP0kY8qOm_OKdrmJjhJztn4nIZLldz5qbmW7RLn8MzeUqhUUkWuOsjQfB1GXmp3eqmbhzmnmaY31IOJ8C0edhZKRwCGByKjdCub10hV77BEwAkmnK6h2eh3ArmzdqUkif1lpjSy-bWtUmlmZLTIi0i-VmzM_3XTdpcdCT87-sARVJ-xy47ZEwSNtdYmEFhw0oFHBXatViuwSsnFBq6QzhmuR-pOH248g-Oq02a7NXQFjGTMZifR9y8vVHbFGLgtqzSVUuO9Ter8bnq1WBU4tbQLEX6xxoAscYZiYmlyhN8GSjbJRwJ968AtfyZy4jkenFbSWiZFNe2IF61BBdLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
کنگره از چه زمانی باید وارد عمل شود و درباره جنگ ایران تصمیم‌گیری کند؟
مایک جانسون، رئیس مجلس نمایندگان آمریکا:
ببینید، دولت این را یک جنگ در حال انجام نمی‌داند. چنین چیزی نیست. آنها در تلاش هستند یک عملیات را به پایان برسانند؛
عملیات «خشم حماسی» که موفقیتی بزرگ بود.
من فکر نمی‌کنم در شرایط فعلی نیازی باشد
دموکرات‌های مارکسیست لیبرال در کنگره
به فرمانده کل نیروهای مسلح بگویند با ارتش چه کار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23535" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=ua21sI9-9qm8aYyjSqUPGC7c1OTEdf_wbl3dzBTnb0QVI8eG9yawpadVY1SnuaYMdomOabJ7Z0gtX562p-DzUv2KyUO1dyIxXdm_p2hPcrDeuKwh2T7HT-1S9HSrMDHa3uClk1wbcDkhKf9ojNXfr-h28OT7R-fXMi969MnKSlt0PIPdAKBmHvoGTN-XZhaywcJ9Ozoe5XX9yUCqdPAhTZ4PvHYEfCLzxihgqqEsVYMSKLv-djkmCUD4-1S2SHjcao-LJ8ShWATh141bgypbHIB7XqJeCZU9AHQz-KH5uEY5su8kwx3pvqbivprQUIL9J9PbyyD65rI67xkwrQoi9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=ua21sI9-9qm8aYyjSqUPGC7c1OTEdf_wbl3dzBTnb0QVI8eG9yawpadVY1SnuaYMdomOabJ7Z0gtX562p-DzUv2KyUO1dyIxXdm_p2hPcrDeuKwh2T7HT-1S9HSrMDHa3uClk1wbcDkhKf9ojNXfr-h28OT7R-fXMi969MnKSlt0PIPdAKBmHvoGTN-XZhaywcJ9Ozoe5XX9yUCqdPAhTZ4PvHYEfCLzxihgqqEsVYMSKLv-djkmCUD4-1S2SHjcao-LJ8ShWATh141bgypbHIB7XqJeCZU9AHQz-KH5uEY5su8kwx3pvqbivprQUIL9J9PbyyD65rI67xkwrQoi9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلاغ پر بازی کردن ناتنیاهو در سخنرانی :
نتانیاهو: حسن نصرالله کجاست؟
جمعیت: حذف شد.(پرر)
نتانیاهو: یحیی سنوار کجاست؟
جمعیت: حذف شد.(پررر)
نتانیاهو: اسماعیل هنیه کجاست؟
جمعیت: حذف شد.(پرررر)
نتانیاهو: علی خامنه ای کجاست؟
جمعیت: حذف شد(پررررر)
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23534" target="_blank">📅 17:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رویترز(کل ماجرا): اروپا در پی تشدید حملات روسیه به اوکراین وارد مرحله تازه‌ای از آماده‌باش شده است. روسیه حملات موشکی و پهپادی را افزایش داده و کشورهای اروپایی نگران سرایت جنگ به خاک ناتو، حملات سایبری، خرابکاری و حملات پهپادی هستند. لهستان امروز برای احتیاط جنگنده‌ها و پدافند هوایی خود را به حالت آماده‌باش درآورد، در حالی که حریم هوایی این کشور نقض نشده بود. بریتانیا از مردم خواسته برای شرایط اضطراری آب، غذای ماندگار و وسایل ضروری در خانه داشته باشند؛ سوئیس نیز راهبرد امنیتی جدیدی تصویب کرده و ذخیره آب و غذا برای شرایط بحرانی را توصیه کرده است. فرانسه و دیگر کشورهای اروپایی نیز حفاظت از زیرساخت‌های حیاتی و توان دفاعی خود را افزایش داده‌اند. با وجود این اقدامات، اروپا رسماً وارد جنگ نشده است؛ اما سطح آمادگی نظامی و غیرنظامی در برابر احتمال گسترش جنگ روسیه و اوکراین و بحران‌های منطقه‌ای به شکل محسوسی افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23533" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=KTb908ArKJlDoqakKjRekUiYgc8gbfdr9yItZvglcNsl-x1kK--HkWrOEXrDOrsdrZCLf2RKYKbVY_90hjwCFk7abR2SQZqXriuPP4IA8BjTQAHsYO7UbdWNMIZAPNn-y96ZR3OVqAk6xXMJ37o5v87rZEK7ZBvHpS5HHCsiatTEdKhKYeG2Zc-EisUjNk_CugbLGWZUDg9Dz5D0ogCuyx76S-8b5wbkFSYluKgw6ioNpHvICiZyKcvnRGmNvvHcNFcSQzBSOshbJmbl0ZuxAdOz9V6nJobpE6fzrsADZNuk7xbPyssw8tSsRaX1YML35lc7zOfXxBA95fov6iiAPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=KTb908ArKJlDoqakKjRekUiYgc8gbfdr9yItZvglcNsl-x1kK--HkWrOEXrDOrsdrZCLf2RKYKbVY_90hjwCFk7abR2SQZqXriuPP4IA8BjTQAHsYO7UbdWNMIZAPNn-y96ZR3OVqAk6xXMJ37o5v87rZEK7ZBvHpS5HHCsiatTEdKhKYeG2Zc-EisUjNk_CugbLGWZUDg9Dz5D0ogCuyx76S-8b5wbkFSYluKgw6ioNpHvICiZyKcvnRGmNvvHcNFcSQzBSOshbJmbl0ZuxAdOz9V6nJobpE6fzrsADZNuk7xbPyssw8tSsRaX1YML35lc7zOfXxBA95fov6iiAPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
ما با تمرکز کامل و جدیت به کار خود ادامه می‌دهیم و با نهادهای مختلف دولت آمریکا، کشورهای عضو شورای همکاری خلیج فارس و همچنین شرکت‌های بیمه و کشتیرانی همکاری می‌کنیم تا
حجم تردد کشتی‌ها از تنگه هرمز افزایش پیدا کند.
این تلاش‌ها نتیجه داده است؛
حجم عبور نفت خام، محموله‌های تجاری و گاز طبیعی مایع‌شده در دو هفته گذشته، از هر زمان دیگری در شش ماه اخیر بیشتر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23532" target="_blank">📅 16:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=e4T0kkyEYVUhMg-BnZlJhtOgvkCeJVsOaqj8WTq82L6TM4ilE4rxIkUBBleTLxMPUi1yM6JlAqKI09NHlr9jyK-Zvd0FsKi_pp76cYFNvKoB5BIhcVanN5fZJ5KV9DCMkGM5SIdhXZxMbcm-vrsRNkRbiRIQ5mMsKEq_mwllma0CPPK_cfkfxc8Tvl1Q5aaguIuKIB9s8gxudNmwcS1MQBpAcW229SHgL9AiilMuffcA8KOlt79GgmphXw92ZbOwG6hSCBOWf9Zqqe9r_e94xO0dsSpxaYeb9LgK7xz9dDs690_ctqaUjO5SDF2uktZEMB4zF-xhoDh0ImGZtZhQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=e4T0kkyEYVUhMg-BnZlJhtOgvkCeJVsOaqj8WTq82L6TM4ilE4rxIkUBBleTLxMPUi1yM6JlAqKI09NHlr9jyK-Zvd0FsKi_pp76cYFNvKoB5BIhcVanN5fZJ5KV9DCMkGM5SIdhXZxMbcm-vrsRNkRbiRIQ5mMsKEq_mwllma0CPPK_cfkfxc8Tvl1Q5aaguIuKIB9s8gxudNmwcS1MQBpAcW229SHgL9AiilMuffcA8KOlt79GgmphXw92ZbOwG6hSCBOWf9Zqqe9r_e94xO0dsSpxaYeb9LgK7xz9dDs690_ctqaUjO5SDF2uktZEMB4zF-xhoDh0ImGZtZhQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
نیروهای سنتکام طی دو ماه گذشته از خروج
بیش از یک میلیارد بشکه نفت خام
از خلیج فارس از طریق تنگه هرمز پشتیبانی کرده‌اند. سنتکام همچنین با تأمین حفاظت و هماهنگی، به عبور
بیش از ۲ هزار کشتی تجاری
از تنگه هرمز کمک کرده است.
مسیرهای اصلی عبور در تنگه هرمز عاری از مین هستند
و هزاران کشتی از این تنگه عبور کرده‌اند. بیش از
یک میلیارد بشکه نفت خام
از کشورهای شریک در خلیج فارس از طریق تنگه هرمز صادر شده، در حالی که
ایران به لطف محاصره کامل و مستحکم آمریکا، حتی یک بشکه نفت هم صادر نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23531" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری i24NEWS: جزئیات بیشتری از پرونده مرحوم حسین پدران منتشر شده؛ طبق روایت مقام‌های ایرانی، او از طریق واتس‌اپ با فردی که خود را «بن» معرفی کرده بود ارتباط داشته و متهم به انتقال اطلاعات حساس نظامی به موساد شده است.  @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23530" target="_blank">📅 16:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حکم اعدام حسین پدران، فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23529" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز: بانک ملت تنها تحول مالی امروز نیست؛ ترکیه در هفته‌های اخیر تحت فشار واشنگتن برای تشدید محدودیت‌های اقتصادی علیه ایران قرار گرفته و لغو مجوز بانک ملت در همین فضای فشار اقتصادی انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23528" target="_blank">📅 15:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23527" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙢𝙞𝙧 𝙎𝙩𝙧𝙞𝙠𝙚</strong></div>
<div class="tg-text">داداش دیدی شاهزاده یه چیزی میدونست از اعتصاب کردا حمایت نکرد</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23526" target="_blank">📅 14:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23525" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363a420621.mp4?token=GXLb4Ke6hSD8yq0SsRlycA8FZ6Us5-qcbzkrxtwHmH5TLaJIIX-qz2Unh5l6BQiRgWsHFUSKw902rqb-M-M-RgfFi9lqsC6UU9LQ6ex5qAG0SaUkjePQRmmd9ia8XuK5dyYjx82HFsqxl44Af89TqCWjESPteebdHY1Sw9m81XS-RtgbredSeidYsslPm9kaCM2gY_tby6iVkDVGgP9F-zNaecs3UqgwFTV4Nn7rsyYOprlkgXjG2HN2FCsDiDEcfjI1F8FFUwL76Rd3fQ0Q2yY2ifiIu-vtOWSFsSYy9sCCqD0K2k5vQu8MlfXBUwpUmVqDONqpIdafigt8pZoSiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363a420621.mp4?token=GXLb4Ke6hSD8yq0SsRlycA8FZ6Us5-qcbzkrxtwHmH5TLaJIIX-qz2Unh5l6BQiRgWsHFUSKw902rqb-M-M-RgfFi9lqsC6UU9LQ6ex5qAG0SaUkjePQRmmd9ia8XuK5dyYjx82HFsqxl44Af89TqCWjESPteebdHY1Sw9m81XS-RtgbredSeidYsslPm9kaCM2gY_tby6iVkDVGgP9F-zNaecs3UqgwFTV4Nn7rsyYOprlkgXjG2HN2FCsDiDEcfjI1F8FFUwL76Rd3fQ0Q2yY2ifiIu-vtOWSFsSYy9sCCqD0K2k5vQu8MlfXBUwpUmVqDONqpIdafigt8pZoSiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی دیشب رفت تجمعات
😂
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23524" target="_blank">📅 14:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بانک مرکزی واردات خودروهای لوکس را متوقف می‌کند
بانک مرکزی اعلام کرده است که برای واردات خودروهای لوکس مانند لکسوس LX700، مرسدس‌بنز کلاس S و بی‌ام‌و سری ۷، کد ساتا صادر نمی‌شود.کد ساتا مجوزی است که پس از تأیید منشأ ارز صادر می‌شود و برای ترخیص خودرو از گمرک ضروری است. بنابراین، خودروهای مشمول این تصمیم تا زمان دریافت مجوز امکان ترخیص نخواهند داشت.این تصمیم برای جلوگیری از سودجویی در واردات خودروهای گران‌قیمت و کاهش فشار بر بازار ارز گرفته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23523" target="_blank">📅 14:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ان‌بی‌سی: مارکو روبیو، وزیر خارجه آمریکا، برخلاف جی‌دی ونس، در طول جنگ از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده است؛ رویکردی که ممکن است از نظر سیاسی به سود او باشد. به گفته منابع نزدیک به روبیو، او در تمام مدت جنگ یک «دست پنهان» بوده و در تدوین راهبرد دولت ترامپ نقش داشته است. این منابع همچنین می‌گویند احتمال نامزدی روبیو برای ریاست‌جمهوری در آینده می‌تواند همچنان روی میز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23522" target="_blank">📅 13:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حریق در انبار کباب‌سرای محمد در تهران، در خیابان دولت (کلاهدوز)، نرسیده به سه راه نشاط (پلاک ۳۳۵) @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23521" target="_blank">📅 13:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23520" target="_blank">📅 13:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش‌ها از کشته شدن ژنرال فراق العسّار از فرماندهان ارشد حوثی‌ها حکایت دارد. این گروه در بیانیه‌ای از او به‌عنوان فرمانده تیپ یکم کماندو یاد کرده است. العسّار در جریان حمله‌ای در جبهه کَهْبوب، در نزدیکی تنگه باب‌المندب، کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23519" target="_blank">📅 13:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Tp07EaZIqiJV-1pQJ52SWv6VtTLW4sNgaGIT27LNpnLeWfgxAs4uzjGue5DaEjbY_WrTaYgDAa03ACkbkPSuo9GNfLI6c9-lloia0SQV1qJUPgHeIhxc8_os27nhWwbmsoXPKkfKdp4NzNKf_vNLh1WIhY56bsqCXc1-M1Mon8PyS0x1ThUHizgDwznAXpCj2Jj8XYKBCN5kbZ7U_82NV-FJIL-BSzSwiXzZ2N0iXVQ7O4UPwJ94NnWTSFJ2hCnpwv78LvXA14I2zdbRH2PUO2UmJGeQi9vSna---I9xWIaJg76x9_xrDv5rtw7FWXQ-N72dgNHCC9LnswDo73xhUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Tp07EaZIqiJV-1pQJ52SWv6VtTLW4sNgaGIT27LNpnLeWfgxAs4uzjGue5DaEjbY_WrTaYgDAa03ACkbkPSuo9GNfLI6c9-lloia0SQV1qJUPgHeIhxc8_os27nhWwbmsoXPKkfKdp4NzNKf_vNLh1WIhY56bsqCXc1-M1Mon8PyS0x1ThUHizgDwznAXpCj2Jj8XYKBCN5kbZ7U_82NV-FJIL-BSzSwiXzZ2N0iXVQ7O4UPwJ94NnWTSFJ2hCnpwv78LvXA14I2zdbRH2PUO2UmJGeQi9vSna---I9xWIaJg76x9_xrDv5rtw7FWXQ-N72dgNHCC9LnswDo73xhUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر پزشکیان: من هم جان‌فدا هستم
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23518" target="_blank">📅 13:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23517" target="_blank">📅 13:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23516" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23515" target="_blank">📅 13:05 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
