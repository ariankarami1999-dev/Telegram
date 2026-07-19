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
<img src="https://cdn4.telesco.pe/file/RRTaupuqDauoWbi9cfF3SbNaVVYm6TlIOdDsjHS4YI-ONRs3ioEeO4ZAisRTHCMpM-JUZ-RClLNoqXFjNF2dGWXjpNc3KTaKBRFSfWggJFlfrgRy6dM81fbfcfeZXrs4PzKQC9qpJx5nF7Tlm8pKXBfW-wttNP_x8hSUcc9-QLxP9YQWT9i8Q7A0tVmXGhoZE1w67xDKGEA498wGbQ7jzHQ-Wr2lL2p3H7yQNk2wj4RRJrXUrVs6h-bR2zA8s7PHZHLP4GFz1LpzMmDNorTU9LsInhWSSsCwpElx-Sq56kZUe3yVie2fpcmKqlU4-jiXGpM2TpBC6Npmq5_RP51_TA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 17:28:51</div>
<hr>

<div class="tg-post" id="msg-672993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تکلیف زمین‌های تازه‌متولدشدهٔ خزر روشن شد
سازمان حفاظت محیط‌زیست:
🔹
اراضی تازه‌پدیدارشدهٔ در سواحل دریای خزر که درپی پس‌روی آب ایجاد شده‌اند، متعلق به دولت و غیرقابل تملک هستند و هرگونه تصرف، واگذاری یا ساخت‌وساز در آن‌ها ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/672993" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672992">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه تولید هر کیلو برنج به ۳۰۰ هزار تومان رسید
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
شورای عالی قیمت‌گذاری وزارت جهاد کشاورزی در اقدامی غیرقانونی و غیرعُقلایی ممنوعیت واردات برنج در فصل برداشت را لغو کرد.
🔹
هزینه تولید هر کیلوگرم برنج به دلیل افزایش چند برابری نهاده‌ها و ادوات کشاورزی به ۲۵۰ تا ۳۰۰ هزار تومان رسیده است.
🔹
با این مصوبه قیمت برنج در حال کاهش است و کشاورزان با ضرر و زیان سنگینی مواجه خواهند شد. از وزیر جهاد کشاورزی می‌خواهیم هرچه سریع‌تر این مصوبه را ابطال کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/672992" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672991">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✂️
ریش‌تراش/ماشین اصلاح HAIR CLIPPER مدل GYT-999
تیغه استیل ضدزنگ
✅
| شارژی
🔋
| مناسب اصلاح صورت و بدن
🔸
نمایشگر LED (نمایش درصد شارژ)
📊
🔸
شارژ کامل: ۲ ساعت
⏱️
🔸
زمان استفاده: ۳ تا ۴ ساعت
🔥
🔸
شارژ با Type‑C + کابل شارژ
🔌
🔸
صفرزن و خط‌زن برای اصلاح دقیق
✨
🔸
همراه ۴ شانه اصلاح + روغن + برس نظافت
🧴
🧹
🔸
بدنه پلاستیک درجه یک
💪
🎨
ارسال رنگ رندوم می‌باشد.
💰
قیمت قبلی: 1,698,000 تومان
🔴
قیمت 1,398,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/672991" target="_blank">📅 17:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672990">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
مهر:
هم اکنون صدای انفجار در آبادان به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/672990" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672989">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
‌
پرس‌تی‌وی: گزارش‌های غیررسمی حاکی از آن است که صدای انفجارها مجدداً در کویت شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672989" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672988">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a15429d.mp4?token=na-Hzq9SDzc8r0Iuv0DeySGe2DIgCihJApdVnr9fueUJKZEwiCbhkguVI_QXj61slIBDWNQJs630Ki6aCuFg8Ak8lse2Ig7ZL49Jc31V3HM7ycSqLCipdQs0e52AgvVCv2Exhl2XYXrvxs4W9onlocdt0RLAqpOxn2vxyoM3XtOkmEOuBYkElK_8OD4opF2g4IkKUa0mnnuqcUAb99kI5uIG9GFZAB4UbIGUgrkvnCRXsU4A1QknE4REDIOQciCxAzQAnRK80BkrB8Sk79ZknFFd0e5Gp417m9RjvvI-olaRK8EyQTqfdBygZ8cGz_W-Tt-ZgXKTMu7MtlxSCc26bRKmTOu8WIVQfebWeolFjRDi6iQuxx-HpWW_0MOaNcWREtYh_8n68GD17-GtqARlbSWgA4dXXsbmMkaDqDeZsRugFr17dEfDcNMceNywrV90m5PYSz4SmaDO8dtB8iCmxJI1qZISGMPuTpQK6PihrKxeWJp54jMzdhJAiZ-7ps8BbZgrMJVaxnhzyZe7mvTXSWQooW5aJT7AD5KnnWHVOmZJ6dxTrrmJy84RV_5xg_gfkqCWa9C4gxULdHyaRePvC0xqEU1rQrjTLuYgd1gvJawzG_x0g1qgZvLGRQRQKpSWWNRc_eBr-S-GNOQReXnKIqkggptmgZ4KfwHRoPZSQs4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a15429d.mp4?token=na-Hzq9SDzc8r0Iuv0DeySGe2DIgCihJApdVnr9fueUJKZEwiCbhkguVI_QXj61slIBDWNQJs630Ki6aCuFg8Ak8lse2Ig7ZL49Jc31V3HM7ycSqLCipdQs0e52AgvVCv2Exhl2XYXrvxs4W9onlocdt0RLAqpOxn2vxyoM3XtOkmEOuBYkElK_8OD4opF2g4IkKUa0mnnuqcUAb99kI5uIG9GFZAB4UbIGUgrkvnCRXsU4A1QknE4REDIOQciCxAzQAnRK80BkrB8Sk79ZknFFd0e5Gp417m9RjvvI-olaRK8EyQTqfdBygZ8cGz_W-Tt-ZgXKTMu7MtlxSCc26bRKmTOu8WIVQfebWeolFjRDi6iQuxx-HpWW_0MOaNcWREtYh_8n68GD17-GtqARlbSWgA4dXXsbmMkaDqDeZsRugFr17dEfDcNMceNywrV90m5PYSz4SmaDO8dtB8iCmxJI1qZISGMPuTpQK6PihrKxeWJp54jMzdhJAiZ-7ps8BbZgrMJVaxnhzyZe7mvTXSWQooW5aJT7AD5KnnWHVOmZJ6dxTrrmJy84RV_5xg_gfkqCWa9C4gxULdHyaRePvC0xqEU1rQrjTLuYgd1gvJawzG_x0g1qgZvLGRQRQKpSWWNRc_eBr-S-GNOQReXnKIqkggptmgZ4KfwHRoPZSQs4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد «لوکاس» با آتش پدافند نیروی دریایی ارتش در جنوب کشور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/672988" target="_blank">📅 17:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672987">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: هواپیماهای سوخت‌رسان آمریکایی پس از حملات به عقبه در اردن، از فرودگاه رامون تخلیه شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/672987" target="_blank">📅 17:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672986">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
از آغاز تیرماه بیش از۵۰ نفر از هموطنان در حملات آمریکا شهید شدند
وزارت بهداشت:
🔹
در حملات هوایی ۶ تا ۲۸ تیرماه، ۵۱۷ نفر مصدوم و بیش از۵۰ نفر از هموطنان شهید شدند.
🔹
در میان شهدا ۵ زن و ۲ شهید زیر ۱۸ سال، در میان مصدومان ۳۵ زن و ۱۹ نفر زیر ۱۸ سال هستند، تاکنون ۲۸ عمل جراحی انجام شده، ۴۶۸ نفر ترخیص و ۳۲ نفر همچنان بستری هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/672986" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
هشدار قوه قضاییه نسبت به هرگونه انتشار محتوای خلاف امنیت ملی
🔹
قوه قضاییه با تشریح «قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی» نسبت به هرگونه انتشار محتوای خلاف امنیت ملی هشدار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/672985" target="_blank">📅 16:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz2iECusU5LwE6Jcz-yePL43coXVBDl1X_tdepVS516o7Rq4UxFh0BQXVl0Y5Rlpia700unkzEF-fpIaa7mnmYj3ukdemDQUPYJI9rm_9-2UI840lgzTR2IS2FS68eHcp5yi-rXX6xMxpHWX2A4epP8Qpw6kQgaHK0OFUubFQKtm_Qi--G1iqIAf5eTrPI3noiFyAWcY4TJgevC7ufvXiAcNpu50fZhuuwJ5nPg7rpmyh9EMuxXgf0asbdThepz1Szw6pd2imiLZirkNrE-_oWBQbMqQnM7KLHfBcTOO8x_SOfTr3RoqLzrfhp314KdDItqf-fS-4xEPZGO5WHfsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از چیزهایی که در گینس ثبت شده؛ قلمرو ایران در زمان داریوش بزرگ بوده که ۴۴ درصد دنیا رو اون موقع شامل میشده...
🔹
ترامپ وقتی گفت ایران رو میخواد بفرسته به عصر حجر منظورش این زمان بود و خودش نمیدونست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/672984" target="_blank">📅 16:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6295645ce.mp4?token=lRRrqxJVX2Z_LQGBTgkTlas2fdX4qXYdUP2pt6iDTKca3H_Tad7cASErM4XF4trT2cnQ9ZhRp7TZjX_57iuW-0vUF2aEGQIvXOh8OO_KdSrXCJDtn1Z9V4jyFfGULN8eqWTxtI7xatnNfvOKIqs-w6WPNh2gUhwuRTUpvENGLAg9p7Bg7NBZTDPUTYEcmTitaBDZunrMwVr2dJItZmabcXJfplkICmKa9bezoouDbFbI5UGy8sbcJ2mZzVIg7mIa0On4BQW40mKCvY-CKkwEmrp2Ir3RBAND0qvHiczRwlqk3Y6Uoxywys0MpZ0Xcfz4uq-CK0WzJVg9qoGyMqj71w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6295645ce.mp4?token=lRRrqxJVX2Z_LQGBTgkTlas2fdX4qXYdUP2pt6iDTKca3H_Tad7cASErM4XF4trT2cnQ9ZhRp7TZjX_57iuW-0vUF2aEGQIvXOh8OO_KdSrXCJDtn1Z9V4jyFfGULN8eqWTxtI7xatnNfvOKIqs-w6WPNh2gUhwuRTUpvENGLAg9p7Bg7NBZTDPUTYEcmTitaBDZunrMwVr2dJItZmabcXJfplkICmKa9bezoouDbFbI5UGy8sbcJ2mZzVIg7mIa0On4BQW40mKCvY-CKkwEmrp2Ir3RBAND0qvHiczRwlqk3Y6Uoxywys0MpZ0Xcfz4uq-CK0WzJVg9qoGyMqj71w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب در جنوب لبنان
🔹
منابع خبری محلی در جنوب لبنان از حملات نظامی جدید رژیم صهیونیستی در مناطق مرزی خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/672983" target="_blank">📅 16:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شرکت راه آهن: پیش‌فروش بلیت قطارهای اربعین از فردا آغاز می‌شود.
🔹
عراق و قطر خواستار اجرای مفاد یادداشت تفاهم ایران و آمریکا برای امنیت منطقه شدند.
🔹
ارتش: انهدام بمب‌های عمل‌نکرده فردا در شرق تهران/نگران نباشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/672982" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHTZ6BjEYobde3m1x31ZaZOYdk9kXcJG7Kkg8WHWwxCrXCt2Jku79UiYMX00Bmwk0v3xJgSs_b1qU3zjOVp2tHsi1dTBsZrA8o7VBIpXfAltG3quItiLNWTOkpQxcE8gDVEr4OIEnKGD-pjcegUAOKKLEpeBO56iucZR5dBlU9PmOE-sE-9v9dc4O9He67szp2lFb0NordK_U3mLI1xdZ0HR-8-d1hdq9zH_D182A7lExy086Yn2-xOpS0ggPVGWEaGfmcWzmIIcLjPyztLiDmam-Wl8acLK1hJfhO0IEW-_6Ug5xjjC1tC22F_mHnmKJ4gUOk51bXhodY24puLVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیاتزا و شاگردانش این‌بار مغلوب ترکیه شدند
/
پایان تورنمنت برای ایران با یک شکست ناامیدکننده
🏐
ایران
1️⃣
➖
3️⃣
ترکیه
🇮🇷
۲۵|۲۲|۱۷|۱۹
🇹🇷
۱۷|۲۵|۲۵|۲۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/672981" target="_blank">📅 16:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672980">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a40c4dcc.mp4?token=YKtRybkc1LOAgVENiQRjWgq8JqZbSvyJ2SpsWTS3mJcHmsmRQb6rmB0y7XuOI03jpWeuRv_nR0eIrWlYDbQbSjfMl-3EWlLFcuW9sqdDhQeGUwv4PQCqNJUBTQhcSiBD34BmwJ4vNJQCLL2e6Mu8yNl_dJuj6at6VBRmYik5wXsvAgoiGpq7V-4liqNEb6RX2BasoKYc9uMVP7Qw9Fglk12pYjezj52fx3CBoVTX_pMnGBE5Y04XpQZbqRqUR6RSSpNb-MkyUYwk-sz_5vLoUx6fR80pxnfstkJkazHGCfEf-1zpcUByLE9LsE8adhPdb4GM6Hft1QJFqkvGXtYzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a40c4dcc.mp4?token=YKtRybkc1LOAgVENiQRjWgq8JqZbSvyJ2SpsWTS3mJcHmsmRQb6rmB0y7XuOI03jpWeuRv_nR0eIrWlYDbQbSjfMl-3EWlLFcuW9sqdDhQeGUwv4PQCqNJUBTQhcSiBD34BmwJ4vNJQCLL2e6Mu8yNl_dJuj6at6VBRmYik5wXsvAgoiGpq7V-4liqNEb6RX2BasoKYc9uMVP7Qw9Fglk12pYjezj52fx3CBoVTX_pMnGBE5Y04XpQZbqRqUR6RSSpNb-MkyUYwk-sz_5vLoUx6fR80pxnfstkJkazHGCfEf-1zpcUByLE9LsE8adhPdb4GM6Hft1QJFqkvGXtYzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار رونالدو با نسخه کودکی خودش در فضای مجازی احساسات میلیون‌ها نفر را درگیر کرد
🔹
این شاهکار که توسط هوش مصنوعی ساخته شده در فضای مجازی نزدیک به ۲۰۰ میلیون ویو خورده و خود رونالدو هم لایکش کرده
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/672980" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672979">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مجلس برای خونخواهی دست به کار شد
جعفر پورکبگانی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
خونخواهی رهبر شهیدمان در سه سطح دنبال می‌شود. اولی حضور و مطالبه مردم در میدان برای خونخواهی‌ست و دومی قدرت نظامی ایران است.
🔹
مجلس هم طرحی را برای خونخواهی در عرصه حقوق بین‌الملل دنبال خواهد کرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/672979" target="_blank">📅 16:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672978">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
مقامات رژیم صهیونیستی از تعلیق کامل پروازها در فرودگاه رامون در شمال ایلات واقع سرزمین‌های اشغالی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/672978" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672977">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34979e300a.mp4?token=rdnro6Ej1LEl4zezh5cEmR4AxexAWswb8CHnSDQoOzKK_Ld663JEwWeyXliHdUfdBq8LES4ltGAkIwJPRwG4xQ1MZp0oKDKi5APJwYbGuxulZoNrWdFwKT-bTMYndpVMNDDvM6Uc9bxupaVFgcCojthdQvNie84RLN7KD0qzf2yg6p0EPIdoJWLGsEgLt0HcFrVQ49K1nWPRZ2-PpfGpHY5ZPAoyIoPoXO0mB-4TipORAwX3InldIz4YSqVYaphL7_3ARkd4vmkCVEY793YYjHTL0M-BoScEvFFVXSPsjzYkFkRgXfE1N4A3J9d9LH0BZge7Dp9Ct1JPnX2X0GCvgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34979e300a.mp4?token=rdnro6Ej1LEl4zezh5cEmR4AxexAWswb8CHnSDQoOzKK_Ld663JEwWeyXliHdUfdBq8LES4ltGAkIwJPRwG4xQ1MZp0oKDKi5APJwYbGuxulZoNrWdFwKT-bTMYndpVMNDDvM6Uc9bxupaVFgcCojthdQvNie84RLN7KD0qzf2yg6p0EPIdoJWLGsEgLt0HcFrVQ49K1nWPRZ2-PpfGpHY5ZPAoyIoPoXO0mB-4TipORAwX3InldIz4YSqVYaphL7_3ARkd4vmkCVEY793YYjHTL0M-BoScEvFFVXSPsjzYkFkRgXfE1N4A3J9d9LH0BZge7Dp9Ct1JPnX2X0GCvgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمام داروهای گوارشی در یک جدول
ذخیره کن؛ حتماً به کارت میاد
🔹
تاکید می‌شود که برای استفاده از این داروها حتما باید با پزشک مشورت کنید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/672977" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672976">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پلیس راهور فراجا: تمام مسیرهای آسیب‌دیدهٔ هرمزگان بازگشایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/672976" target="_blank">📅 16:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672975">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11f8aa326.mp4?token=pwxIn_ihI1SRzfHlHP2A-LLidNmIMLOyNVK8VexNot-S4jsr3jL6dM_tNMJkSqhU4D-DBjhsaMkn0WkupZnv4t58yzscnSQsT6QFojRryINKzi4eesfLP4amtY2Dl99MtjEglYK1fZQ_qpF3u8fdBevafMCTLNbFxl4hu8W8zyCbEMxpiTe-dUxRhDEZ2UQ26iGGBKy_V84uLgxblB0paLPbERpp4HKXppbh2y6z0ddfBu2Hl2oSxg9F-PM2P2zwBsPt09qe8JjcaYRW4s435vuf2lpfUYm4fWrEASd_3iKNybbuXNHm9U760Kl4-Q32_bD8OXkfZRhvVASJPN2t6qlzxo-yqXj8l35RyMs9yRAy0wri-SaVN4Kz2H4O19O6twhN7f_DNmDjWF_iRYZ5glXGpkMA7jArX0YPU2TDh5Zbu-hUjHXszgL3SRHIuclwqWrC40I1Bqg9WUufnshxa6OSYIDew2ze26NWZlQSHRVTemxuS-mHW0tv6cBvaEWAe3e4KXl3JOD_h8nu-hVfSyrA6VfUWMCbej4Fh4rtg6RCLg5cTWB3bjNAaxMEHLnxSA1tx49v3FMGDtGbW78QISXtJ6h0zYXvXKAKmwYlEhvu1lLMaoKLKyfzQK1lllJYtc99pqD3XvNDtVudHTzIlEnsf03SCkaFkpEtjXDXWs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11f8aa326.mp4?token=pwxIn_ihI1SRzfHlHP2A-LLidNmIMLOyNVK8VexNot-S4jsr3jL6dM_tNMJkSqhU4D-DBjhsaMkn0WkupZnv4t58yzscnSQsT6QFojRryINKzi4eesfLP4amtY2Dl99MtjEglYK1fZQ_qpF3u8fdBevafMCTLNbFxl4hu8W8zyCbEMxpiTe-dUxRhDEZ2UQ26iGGBKy_V84uLgxblB0paLPbERpp4HKXppbh2y6z0ddfBu2Hl2oSxg9F-PM2P2zwBsPt09qe8JjcaYRW4s435vuf2lpfUYm4fWrEASd_3iKNybbuXNHm9U760Kl4-Q32_bD8OXkfZRhvVASJPN2t6qlzxo-yqXj8l35RyMs9yRAy0wri-SaVN4Kz2H4O19O6twhN7f_DNmDjWF_iRYZ5glXGpkMA7jArX0YPU2TDh5Zbu-hUjHXszgL3SRHIuclwqWrC40I1Bqg9WUufnshxa6OSYIDew2ze26NWZlQSHRVTemxuS-mHW0tv6cBvaEWAe3e4KXl3JOD_h8nu-hVfSyrA6VfUWMCbej4Fh4rtg6RCLg5cTWB3bjNAaxMEHLnxSA1tx49v3FMGDtGbW78QISXtJ6h0zYXvXKAKmwYlEhvu1lLMaoKLKyfzQK1lllJYtc99pqD3XvNDtVudHTzIlEnsf03SCkaFkpEtjXDXWs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس‌انداز و سرمایه‌گذاری فرق دارن، و این فرق می‌تونه کل آینده مالیت رو عوض کنه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/672975" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672974">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری، سقف نرخ بلیت پروازهای نجف و بغداد را ۱۲ و ۱۴ میلیون تومان اعلام کرد
🔹
نرخ رفت‌وبرگشت از تهران و استان‌های شرقی ۲۴ میلیون تومان و از مشهد و استان‌های غربی ۲۸ میلیون تومان خواهد بود.
🔹
این نرخ‌ها برای بازۀ زمانی ۳۱ تیر تا ۱۶ مرداد اعمال می‌شود و برای بزرگسالان و کودکان یکسان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/672974" target="_blank">📅 16:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672973">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مقامات رژیم صهیونیستی از تعلیق کامل پروازها در فرودگاه رامون در شمال ایلات واقع سرزمین‌های اشغالی خبر دادند
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/672973" target="_blank">📅 16:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=JX3zFmXlV4k6uVaEMhKgHKGVHrE7HsRm9xU7b4rORr7YPFfpyDXiSaAr-WLsLczO1c1MEmiRg6RL0KVHpTALvE1cQe-ejUiOUeFzVnf6DtQk5aWaV6uGlTiwpwaIzSiZN2liNFy3Xjef9BG9CuZScxLTxixSc9VjakBIwjaQWYo28Q4QQOJHcIdNliI81lqmn5hiPxryM7z7laYU-YWFSDv5cn3gK6ye1C78gtTcpBFe0JooCZiWcaIPJgyPj-3uAzDUJ6D-2sKDhu1mb-P4inPUJIeNGtbKaPRKdcHClLo6BluTubkThsqV12fV8o6kZp8QMZ5XYH_h1QklSvmQNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=JX3zFmXlV4k6uVaEMhKgHKGVHrE7HsRm9xU7b4rORr7YPFfpyDXiSaAr-WLsLczO1c1MEmiRg6RL0KVHpTALvE1cQe-ejUiOUeFzVnf6DtQk5aWaV6uGlTiwpwaIzSiZN2liNFy3Xjef9BG9CuZScxLTxixSc9VjakBIwjaQWYo28Q4QQOJHcIdNliI81lqmn5hiPxryM7z7laYU-YWFSDv5cn3gK6ye1C78gtTcpBFe0JooCZiWcaIPJgyPj-3uAzDUJ6D-2sKDhu1mb-P4inPUJIeNGtbKaPRKdcHClLo6BluTubkThsqV12fV8o6kZp8QMZ5XYH_h1QklSvmQNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر در مناطق مرزی جنوب کشور: سلبریتی‌ها در این وضعیت به‌دنبال فالوور نباشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672971" target="_blank">📅 16:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTY269NVRx-Hf39KHg9Y7UENNRpG9llvQ9YQ3jQrqp23CUroLhbVLj0H-tCvqR-sRRUWllASjGybXUxQ35Pn9Oe8xcjsqcA3B0lMIm0x_dzW3U3zFb3eKFYb0pk0P9lIdAwveqk57Pvgo6eJl2mkBqLACeefSlMiHH56hhAvNaDIo2ry9lqlqTa3FlkYWTQ-MfI6uIjUlhrQpD7JH_ZyaJJcpsjxkowaE00dDOO1dO3eZgEn4OevF0jCtBak7ntXKpY71uwv0kfNUgC-Yex4VcB8i78zHPSC7rzxfoquOwg24pWfwuX-DfkuvKW4Lt6EPPK4rrXiUnpkiM1aUSpq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک پرواز از دبی به تل‌آویو به دلیل شلیک‌ها به سمت اردن، مدتی در هوا معلق ماند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672970" target="_blank">📅 16:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم صهیونیستی: شنیده‌شدن صدای چند انفجار در ایلات گزارش شده است.
شهرداری ایلات:
🔹
صدای موشک‌هایی که از ایران به اردن شلیک شد تا ایلات شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672969" target="_blank">📅 15:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672968">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a19ff62b.mp4?token=t70gcBfUKzYYP1mpoKyeBXXXjv78SrdTTadaylPiFYPDfUVwTDS2ljYPDDT9hhtroelb99lZMj6vXNoXIhkYVf2ZELfYVCc4t_1NKpmSDJunFn4hg_o5Yjn6A20TfiZWQ8khX1O7Vn6XL0fii_sUVHC8EU9m4IqInpRGR0AWkEZ4b4MMnEWyeN3qNTYdDlaubNbNIzvqKgh2iQoAC-vNTfXCwwGcSJtFDLTBJRQAssQgHLKQ2--O9DWwZtKxBzAQm8qyiKjcRUuLhLJZZMt3SqWGt6VkMQLGSpNHX8FyagBWHcGYXwNt5v124Kv_AMgVRcCvPBlQccHZd2HdK6Djfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a19ff62b.mp4?token=t70gcBfUKzYYP1mpoKyeBXXXjv78SrdTTadaylPiFYPDfUVwTDS2ljYPDDT9hhtroelb99lZMj6vXNoXIhkYVf2ZELfYVCc4t_1NKpmSDJunFn4hg_o5Yjn6A20TfiZWQ8khX1O7Vn6XL0fii_sUVHC8EU9m4IqInpRGR0AWkEZ4b4MMnEWyeN3qNTYdDlaubNbNIzvqKgh2iQoAC-vNTfXCwwGcSJtFDLTBJRQAssQgHLKQ2--O9DWwZtKxBzAQm8qyiKjcRUuLhLJZZMt3SqWGt6VkMQLGSpNHX8FyagBWHcGYXwNt5v124Kv_AMgVRcCvPBlQccHZd2HdK6Djfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود از شهر عقبه در اردن به آسمان برخاسته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672968" target="_blank">📅 15:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672967">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3d8e8d7a8.mp4?token=QDIOCs00WlvZhxfwdNmZCnW9oA_wL2yoZbAcFE8BxQkzj3LwFNRMn27qvCXgC2A7fx3R-coO_ho1rmxeYdGR3_g4MXrEtXAV1w79H3GddZErZ0CAh9vEZHZK9Rs1uEJzlz-_ZL0S-OyOI3DXBc2w9nu4eqj_NPsDM98ubyQl05gYk3fRARJsJBqmXZJ35PZYcAHh58HOgOqDRaS81n4nQhhngjaE-VX5hfiioB6l95znnJ804eGrelQjhJgNtaOgKVM0NsY6lw3zfu9OcZrmm_1JDUbf2y3ujkuzSRvIYw6WeYdIDX2x7e9-mKT9DjcO58BeunvqRysR90M4weg4ulnlAtJbLEa8o7Ef9rKyBWrqmUOImC8Zyg_GGSw8dihJEngu8nSgOu97mLHgv5q1sltvGnvfyz3NonX3zdCBXkzLFNgRlDHgU7nVtzqpgil8RMtNFNzX3PkeUf3qfxNqamz8KYjYMYJxqTNvcsCyIdDeIqLCWQfPqxk77tfnvBSNBsJq8aUDe_8WRQb3LwNl_u8qr6sz5E8NPHSif6TwV_zlvC-UYx8UqRkXvr6mFJhj9LKxo-3Yigl1w3MWnRgqjGniObA4qLq7Fkd3pUqbL0h7VfeJ9csxBw3470jGCdUVHYC5Iypo9Dzst1qTnOOwmzPnLfCmRIp6LnhfHnnrc20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3d8e8d7a8.mp4?token=QDIOCs00WlvZhxfwdNmZCnW9oA_wL2yoZbAcFE8BxQkzj3LwFNRMn27qvCXgC2A7fx3R-coO_ho1rmxeYdGR3_g4MXrEtXAV1w79H3GddZErZ0CAh9vEZHZK9Rs1uEJzlz-_ZL0S-OyOI3DXBc2w9nu4eqj_NPsDM98ubyQl05gYk3fRARJsJBqmXZJ35PZYcAHh58HOgOqDRaS81n4nQhhngjaE-VX5hfiioB6l95znnJ804eGrelQjhJgNtaOgKVM0NsY6lw3zfu9OcZrmm_1JDUbf2y3ujkuzSRvIYw6WeYdIDX2x7e9-mKT9DjcO58BeunvqRysR90M4weg4ulnlAtJbLEa8o7Ef9rKyBWrqmUOImC8Zyg_GGSw8dihJEngu8nSgOu97mLHgv5q1sltvGnvfyz3NonX3zdCBXkzLFNgRlDHgU7nVtzqpgil8RMtNFNzX3PkeUf3qfxNqamz8KYjYMYJxqTNvcsCyIdDeIqLCWQfPqxk77tfnvBSNBsJq8aUDe_8WRQb3LwNl_u8qr6sz5E8NPHSif6TwV_zlvC-UYx8UqRkXvr6mFJhj9LKxo-3Yigl1w3MWnRgqjGniObA4qLq7Fkd3pUqbL0h7VfeJ9csxBw3470jGCdUVHYC5Iypo9Dzst1qTnOOwmzPnLfCmRIp6LnhfHnnrc20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از چه زمانی به کودک درباره اندام خصوصی‌اش آموزش بدیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672967" target="_blank">📅 15:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672966">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادارات استان فارس دورکار شدند
استانداری فارس:
🔹
با توجه به پیش‌بینی افزایش بی‌سابقه دما، تمامی ادارات و دستگاه‌های اجرایی استان فردا به صورت دورکاری فعالیت‌ خواهند داشت.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672966" target="_blank">📅 15:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672965">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شلیک موشک از ایران به نزدیکی مرزهای اسرائیل در اردن
🔹
ارتش اسرائیل اعلام کرده ممکنه آژیر خطر در اسرائیل به صدا دربیاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672965" target="_blank">📅 15:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672964">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت اتوبوس‌های درون شهری ۱۰ برابر شد
مجتبی یوسفی، رئیس فراکسیون مدیریت شهری مجلس در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت بلیت ناشی از تورم و رشد هزینه‌ها است و قیمت هر اتوبوس از ۲ به ۲۰ میلیارد تومان رسیده و درآمد فروش بلیت پاسخگوی هزینه‌های جاری نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672964" target="_blank">📅 15:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672963">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69e0e2749.mp4?token=UTurxs-JIX01pI0Ww8d0riVE--R7ggpwtshFFarERAe-Mf3SKnc9vD2MpIU1aUzyVT7zf477yScAGCaW0ZXj_qXhitZ_8Fav7khxtH-6aFN92NvwK59eUXH41pzwDQAbQWnSQK-Waam-9IqQ6AgdKU_nF_BN1Ulu-gVPYMt96DHVSX0LmMCdWtp-xm_gelHVlxNyRp6YpfnAODe01ozDi5pv4eQ8Mn0sN70ezcji8VFFbUYniOf08hGDZWARVhT7VTkQ-qMRA_Ima_WKNzNBNBNCwd8c9rJi0AoCg2g8Sg_eyKfKpT0C66TEnuVzvcPFqqjSrSNgbpcLV7Y64LQpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69e0e2749.mp4?token=UTurxs-JIX01pI0Ww8d0riVE--R7ggpwtshFFarERAe-Mf3SKnc9vD2MpIU1aUzyVT7zf477yScAGCaW0ZXj_qXhitZ_8Fav7khxtH-6aFN92NvwK59eUXH41pzwDQAbQWnSQK-Waam-9IqQ6AgdKU_nF_BN1Ulu-gVPYMt96DHVSX0LmMCdWtp-xm_gelHVlxNyRp6YpfnAODe01ozDi5pv4eQ8Mn0sN70ezcji8VFFbUYniOf08hGDZWARVhT7VTkQ-qMRA_Ima_WKNzNBNBNCwd8c9rJi0AoCg2g8Sg_eyKfKpT0C66TEnuVzvcPFqqjSrSNgbpcLV7Y64LQpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش قلعه‌‌نویی به تصویر ساعتش در جام جهانی  سرمربی تیم ملی:
🔹
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد.
🔹
اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/672963" target="_blank">📅 15:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672962">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شلیک موشک از ایران به نزدیکی مرزهای اسرائیل در اردن
🔹
ارتش اسرائیل اعلام کرده ممکنه آژیر خطر در اسرائیل به صدا دربیاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672962" target="_blank">📅 15:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672961">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev4rM63AI84XDqhw2e8lvgZri_sVnB0-BWpoOCz57w4aO8T141QNCbFO2PDksXYgeR2XlAFS3q9OTkRU2l8dOTUpk9x1ELk0M1zwomN2GHEdfYD10GgIFulxCeG-a7LzJvCZZkOdqiDbjdLhQia6S4oETq22Nyh1YvLcgDNF0MSRCaA_oJ6nbh8QK4FVGba8G2zJ7kpXJt7Njg51gh3XptUhNNOHirrdZOffjtvgoXr3XpG6gSEI-aH9tuaiq6Xs7HsYTQhU2othDAH3ei89rBK1ISZO-ta8Rgh5O0iZQnVjuedr6-NJUAfrPLmJ4gSQTSOcCWiSptHqt4V_cNYCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیطان خون‌خوار: ایران باید به لایحه تحریم‌های روسیه اضافه شود
🔹
«جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندسی گراهام می‌خواست انجام دهد و قرار بود عملی شود. مهم!!!»
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/672961" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672960">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال/ پایان ست اول
🏐
ایران ۱
➖
۰ ترکیه
🇮🇷
۲۵
🇹🇷
۱۷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/672960" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672959">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=bcUOR02YFhrX7Qqx2OFErMJo_rkAJwd88lkSQYEq_Brms77tWRpKQB06wJfzeHpg65bIyGIuFfLL1yUj29dF9v7B1CkmWNtMWAXNVNZupanHZPLJxjE62iciCthANUfKFXWrmLbJo-tmTEjolAZ5jdpwoKVBOG3qSo30L39tf1vkJXbeBsrr2MJkfhHEzmOuiDkkPepzwLvY5lsx4r0bGH4Sk9-KssI2jkgxnYrno-enuN-Wt9gSwjm3A_HxMZ725weqIfrxSYqYxQUoRg7-eRy8Hgjx92Nvj3b-e8DbiJg_MHIDzYRMgkpaKT0E5OhSUXq_nXLmb60xRLAFZLlNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=bcUOR02YFhrX7Qqx2OFErMJo_rkAJwd88lkSQYEq_Brms77tWRpKQB06wJfzeHpg65bIyGIuFfLL1yUj29dF9v7B1CkmWNtMWAXNVNZupanHZPLJxjE62iciCthANUfKFXWrmLbJo-tmTEjolAZ5jdpwoKVBOG3qSo30L39tf1vkJXbeBsrr2MJkfhHEzmOuiDkkPepzwLvY5lsx4r0bGH4Sk9-KssI2jkgxnYrno-enuN-Wt9gSwjm3A_HxMZ725weqIfrxSYqYxQUoRg7-eRy8Hgjx92Nvj3b-e8DbiJg_MHIDzYRMgkpaKT0E5OhSUXq_nXLmb60xRLAFZLlNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود/ حملات از کویت را حملات مستقیم تلقی می‌کنیم و بدانند که به‌صورت ویژه ادبشان خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/672959" target="_blank">📅 15:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672958">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
منبع مطلع: تا زمان ادامهٔ شرارت‌های آمریکا تنگهٔ هرمز مسدود خواهد ماند
یک منبع مطلع در نیروی دریایی سپاه:
🔹
درحال‌حاضر هیچ ترددی از تنگهٔ هرمز انجام نمی‌شود؛ هرگونه تلاش برای عبور از تنگهٔ هرمز، به‌ویژه از سوی شناورهای متخلف، با برخورد نیروهای مسلح ایران مواجه خواهد شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672958" target="_blank">📅 15:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672957">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdqsG3vx-BpU1M30sIUDITm0usn8v99XJBFitFw2eHCbMJMjV_EzweET_c1XsqChURfFWMKDwupvJNJBI604J_30KDVj2gH--0tcG4lghTD9WxwJzxTBmBAnHL71GJ_pnKyhiSUrIKyg0EGYSNemNdCIAq-aam1oRx0coQERIHZXtk-vZuuOKBxbQJ77vIlZ0X17UmFFwucH5s2s0HJR_xkzVzDpPYFZfe_pMpLqOprPqwyygWoMH7Tof4wXtR0EHakChLZB-DLcOHxTfqfweW8xyKk7lZc0MmYF1yLutStIAYoOh7nMadPyPLnfIFcB8ZmDvLHrNcqLZJtcL-CXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدال مسی و یامال سیاسی شد
🔹
دیدار فینال جام جهانی ۲۰۲۶ میان اسپانیا و آرژانتین، تنها یک رقابت فوتبالی نیست.
🔹
رسانه‌های صهیونیستی این مسابقه به نمادی از شکاف سیاسی بر سر جنگ غزه و روابط با اسرائیل معرفی کردند؛ تا جایی که نشریه تایمز اسرائیل آن را «جنگ نیابتی سیاسی در زمین فوتبال» توصیف کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672957" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672956">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9af66466.mp4?token=JKox0ET1nyj-Vjrnhagb8WtCIcVbNiLxlrw4TAm1vOgEqIk6D64gdt_Eu7T1settDoUGuQDjQ9BIYMd1lpzXm08G9SqrtHPBSt3PqWM_uaLqkDiWTXK5oXRMzJGUP4hIaLp34I662DhnY-_en_aldGIyGmpFUiM7D8t8lCk_6Dx2H19n8pXTyhKB6JPOuxor7AKM3eCM36NvJgV1Fvdd91pj_n73_m_N5b61MSj6yhmTSr_oSvR25BiDvDlbsSJxs2i9_4DBfFajRRoqBiEUrV-ETBWmvDt3D4DA6ZRdiSk3FxSw-27pc-40CMftQ-2J0yekZc5BCluTsAXuTIUlFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9af66466.mp4?token=JKox0ET1nyj-Vjrnhagb8WtCIcVbNiLxlrw4TAm1vOgEqIk6D64gdt_Eu7T1settDoUGuQDjQ9BIYMd1lpzXm08G9SqrtHPBSt3PqWM_uaLqkDiWTXK5oXRMzJGUP4hIaLp34I662DhnY-_en_aldGIyGmpFUiM7D8t8lCk_6Dx2H19n8pXTyhKB6JPOuxor7AKM3eCM36NvJgV1Fvdd91pj_n73_m_N5b61MSj6yhmTSr_oSvR25BiDvDlbsSJxs2i9_4DBfFajRRoqBiEUrV-ETBWmvDt3D4DA6ZRdiSk3FxSw-27pc-40CMftQ-2J0yekZc5BCluTsAXuTIUlFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت ۱۰ میلیاردی امیر قلعه‌نویی در فوتوشوت‌های جام جهانی سوژه شد
🔹
این ساعت ترکیب رنگ آبی پودری (Vibrant Blue) در صفحه دارد و بزل که تداعی‌کننده شخصیت‌های کارتونی اسمورف است. در حال حاضر قیمتی بین ۴۰ تا ۵۰ هزار دلار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672956" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672955">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995fd9d2e5.mp4?token=qDUtXp6RXYuLUWpcxaRTngH9po5ATyV0ArReHBbr0PcnEFYuLGzhbpFgrRqIkvUYTIudry4V_ysolzTitysVNUKemvzlwMxd5AKO0uEGoCdVb0LANweAieNE1XLNGLFNMDZJGrQhsGbMYJqHICUoztz9HDDpxFCXo6CKXKYW45wjAC9bGVu21Gj4vIfmDZJoybOx5egM16-fQGuklvkoCthYMFeOl93vCBXx9h07zlJZcBRCylePer2PRpyFKAMaEYW7sOeEAoNVygg74fyXo_fKlwzVgW2uUXUdUWS8ptBoNenUuScjyEaiq7xeQDQWOCUC2Ah6BVJ8zOyDYLWn2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995fd9d2e5.mp4?token=qDUtXp6RXYuLUWpcxaRTngH9po5ATyV0ArReHBbr0PcnEFYuLGzhbpFgrRqIkvUYTIudry4V_ysolzTitysVNUKemvzlwMxd5AKO0uEGoCdVb0LANweAieNE1XLNGLFNMDZJGrQhsGbMYJqHICUoztz9HDDpxFCXo6CKXKYW45wjAC9bGVu21Gj4vIfmDZJoybOx5egM16-fQGuklvkoCthYMFeOl93vCBXx9h07zlJZcBRCylePer2PRpyFKAMaEYW7sOeEAoNVygg74fyXo_fKlwzVgW2uUXUdUWS8ptBoNenUuScjyEaiq7xeQDQWOCUC2Ah6BVJ8zOyDYLWn2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عشق تو در وجودم و مهر تو در دلم با شیر اندرون شد و با جان به در کنم! #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672955" target="_blank">📅 15:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672954">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=GiP06afaCqz2nj3Sc9LQo_943rPa99SI_SXrSq2pHC11gE4sgzTY_ykoKCq0Kq2pXSHaS9Q6MBU4giBdbbex-ZJhfzkJ2jng2aXledDTPHcqEWKcL4ARD6fLLb_3ubtoBbvYhEEWpv2yq5pH9rfVmHnECqMdeCB30P8Pok4vqClTCRk6nZiQcYClHDYSl_dgLbvlf7wkcbiD3Jk1z4An6xUrjusiWO7THr0jKwaCL3x0zfG7YsjpKD0aecybKW4HuwLPiIyWKsgSn6TEFRp1JuPpy8Sfv5xBiI9gEF9WhQuQ6zpWY4Zv1DnmJIa9qdyyK_XiVRMEReOqI4pwohH0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=GiP06afaCqz2nj3Sc9LQo_943rPa99SI_SXrSq2pHC11gE4sgzTY_ykoKCq0Kq2pXSHaS9Q6MBU4giBdbbex-ZJhfzkJ2jng2aXledDTPHcqEWKcL4ARD6fLLb_3ubtoBbvYhEEWpv2yq5pH9rfVmHnECqMdeCB30P8Pok4vqClTCRk6nZiQcYClHDYSl_dgLbvlf7wkcbiD3Jk1z4An6xUrjusiWO7THr0jKwaCL3x0zfG7YsjpKD0aecybKW4HuwLPiIyWKsgSn6TEFRp1JuPpy8Sfv5xBiI9gEF9WhQuQ6zpWY4Zv1DnmJIa9qdyyK_XiVRMEReOqI4pwohH0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهارمین سوگواری آیینی محرم شهر با حضور و اجرای بیش از ۵۰ گروه هنری از ۲۷ تیر تا ۱۲ مرداد از ساعت ۱۹ تا ۲۳ در میدان آزادی برگزار می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672954" target="_blank">📅 15:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672953">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دبیرکل اتحادیه عرب خواستار بازگشت فوری آمریکا و ایران به میز مذاکرات شد
🔹
وزیر نیرو: اولویت تامین انرژی با استان‌های درگیر جنگ است.
🔹
رادیو ارتش اسرائیل: تقویت ۱۱ سایت نظامی در مرز با لبنان به دلیل کسری بودجه در وزارت دارایی متوقف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/672953" target="_blank">📅 15:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672952">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سی‌ان‌ان: دولت ترامپ موافقت اولیه خود را با اجازه دادن به عربستان سعودی برای غنی‌سازی اورانیوم در خاک خود بدون اعمال سازوکارهای نظارتی سختگیرانه معمول اعلام کرده است./شفقنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/672952" target="_blank">📅 15:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672951">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مدیرعامل خبرگزاری قوه‌قضائیه: هیچ زندانی آمریکایی با مشخصاتی که ترامپ گفته از زندان‌های ایران آزاد نشده است
🔹
خانمی که مورد بحث است نه زندانی بوده و نه اتهام جاسوسی داشته است. ترامپ در شرایط فلاکت‌باری قرار گرفته که نیاز دارد از هرچیزی دستاورد بسازد. حتی…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/672951" target="_blank">📅 15:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672950">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال/ پایان ست اول
🏐
ایران ۱
➖
۰ ترکیه
🇮🇷
۲۵
🇹🇷
۱۷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672950" target="_blank">📅 15:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672949">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_K3Ig5UPqg5rzfl-e--OhbYbbysnh-FN5-HQuPpok2I1PNG2wl94ID1ZyhKyvr69u0UFeFxJWHSfMgKiaP1QcM5ZPnCz-TK8NrDhx2h0kVqrm8iGH2RExMn9XPa0C9wOaUijmMpDUpbFugpnZ3m3JAPFFfa18wJtXPo07CMWF2ijQC6fJIHm_K0V3DIG_wrD-PEH40q3LxCtP2V_Csole5b8inoWjcV32RRh5iseJvnAlFkkeW-N9740HPBPlSz2GBxLvq5t206XQjfNRwjR0kxFEGmcT2_f3xCkv0C10PZM21ue9SUYmjJc88dkGn8ivbTW8Vb0r0ZKRHJoG0VzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمایه‌گذاری حرفه‌ای در طلا با صندوق رز ترنج
🟢
صندوق طلای «رز ترنج» امکان سرمایه‌گذاری در بازار طلا را بدون دغدغه خرید، نگهداری و تشخیص اصالت طلای فیزیکی فراهم می‌کند.
🟢
این صندوق با مدیریت فعال ترکیب گواهی سپرده شمش و سکه و استفاده از ظرفیت بازار آپشن، از فرصت‌های بازار برای بهبود بازدهی استفاده می‌کند.
▫️
برای خرید با حداقل مبلغ ۱۰۰ هزار تومان، از ساعت ۱۱:۴۵ تا ۱۷:۰۰ وارد سامانه معاملاتی هر کارگزاری شوید و نماد «رز ترنج» را جستجو کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/672949" target="_blank">📅 15:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672948">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
حمله مجدد به نیروگاه برق و آب‌شیرین‌کن کویت
وزارت برق کویت: یک نیروگاه تولید برق و آب‌شیرین‌کن برای دومین بار طی دو روز گذشته هدف حمله قرار گرفت و دچار آتش‌سوزی شد.
🔹
تعداد زیادی از واحدهای تولیدی این نیروگاه تحت تأثیر قرار گرفته و از مدار خارج شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/672948" target="_blank">📅 15:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672947">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d463819eb.mp4?token=SA8ASZrNYMFc1CTw14vYwR6wQtN5BhU_N_sK0jlHm0dN6MeTjeYQbYQSq-ubz4w1DF00wAzJuog6tRIsaw4FybK05q8Sl4SgfTlGRxZl-xaUUyJbU9BCwCkIRLig7EErWdflEXIHgTqswdO40Px04L_HytFtkKXBDjK7IEQP0tAxndsWMgNgTwWLkxD4wKLtjpBz49sE_BMIsR4NJ0qTGy4JwOUYh44jrB-lFEXt608Y5d7dicAiyTxL3D5LFqTeNo1A2fpAiBJUJp8_5wnyV2_3hEwmU5_OAykzVs9-ew2T-lmvF_LMD1XIbLfVECCMzoYWFc1gMuPTv_t5rhA6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d463819eb.mp4?token=SA8ASZrNYMFc1CTw14vYwR6wQtN5BhU_N_sK0jlHm0dN6MeTjeYQbYQSq-ubz4w1DF00wAzJuog6tRIsaw4FybK05q8Sl4SgfTlGRxZl-xaUUyJbU9BCwCkIRLig7EErWdflEXIHgTqswdO40Px04L_HytFtkKXBDjK7IEQP0tAxndsWMgNgTwWLkxD4wKLtjpBz49sE_BMIsR4NJ0qTGy4JwOUYh44jrB-lFEXt608Y5d7dicAiyTxL3D5LFqTeNo1A2fpAiBJUJp8_5wnyV2_3hEwmU5_OAykzVs9-ew2T-lmvF_LMD1XIbLfVECCMzoYWFc1gMuPTv_t5rhA6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مکزیک زیر آب؛ سیلاب خودروها را با خود برد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/672947" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672946">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3595950301.mp4?token=bgUp8r3eM--csrI3ZF2QI-VSbvFdUX1j4XGhQLAVHEghVN0LpttI2VUGqSQZ6e7QcW6HFOLNCY4Vx6TfwFfEDQkFCZD_ixHgfRHmXJPf1nJiOmEazuvu-WhC080j7TN-LBQGFJisiTqD1W_gCa7tnBoxTMM3QdBr8NIFpPWrfYHQ3JUmjshF6vAp0lVyikWPiFETrkBm_NXG3ihe5FF_NBWdfqcPeqfmP2T0XvSQJS2IhZwPQQHQWaXw_Oqw9OdmBmueK9whWy85ebuF0ijIlxqgGPpdy_9QaYplwlFKKQxF-fgXT5B0o8BlJ8KKMP9Cri4rXQXvZgg4hrm9Hd7c2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3595950301.mp4?token=bgUp8r3eM--csrI3ZF2QI-VSbvFdUX1j4XGhQLAVHEghVN0LpttI2VUGqSQZ6e7QcW6HFOLNCY4Vx6TfwFfEDQkFCZD_ixHgfRHmXJPf1nJiOmEazuvu-WhC080j7TN-LBQGFJisiTqD1W_gCa7tnBoxTMM3QdBr8NIFpPWrfYHQ3JUmjshF6vAp0lVyikWPiFETrkBm_NXG3ihe5FF_NBWdfqcPeqfmP2T0XvSQJS2IhZwPQQHQWaXw_Oqw9OdmBmueK9whWy85ebuF0ijIlxqgGPpdy_9QaYplwlFKKQxF-fgXT5B0o8BlJ8KKMP9Cri4rXQXvZgg4hrm9Hd7c2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی: پاسخ ما به حمله به آسایشگاه ارتش در چابهار برابر نبود؛ بلکه حداقل ۳ برابر بود/ تلفات آمریکا در سوریه بیش از تلفات سربازان مظلوم ما در چابهار بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/672946" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672945">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
المیادین به نقل از منابع آگاه:
وزیر کشور ایران فردا برای سفری یک‌روزه به پاکستان سفر خواهد کرد
./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672945" target="_blank">📅 14:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672944">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dviPsx0H4QZszkbPjxLC6A4gldOE-o_xS4Im8vm-Mm3Q4znWL7HRerJVMlUkh1zSi4hhe-OXjClOxX3xGldy-4BkIvbOEImFBGx2Ymq0QvPpR0RDTSx4l5A_RXoIYD3RJkfwZYzuz9hqXhYgCEtTf5hQltazfmPtB06odW83aSoNG-E1U2nsHnO7-Ql0xjigRjQ_ToSHGoJP3jT1PtH7m8vVcy1l5Dicsfmeovo8XgR8lTL_HdkmsP7Ng3aUJQKl0WQ-mFa8XuHYY2AQZT1Yeuxr9qSDy1_jV6s6njgy6-BZHox2rpdkkmG6XQ3C9Bvrwtc8xG_O9mWcAIYyvboRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل خبرگزاری قوه‌قضائیه: هیچ زندانی آمریکایی با مشخصاتی که ترامپ گفته از زندان‌های ایران آزاد نشده است
🔹
خانمی که مورد بحث است نه زندانی بوده و نه اتهام جاسوسی داشته است. ترامپ در شرایط فلاکت‌باری قرار گرفته که نیاز دارد از هرچیزی دستاورد بسازد. حتی خارج‎‌شدن یک شهروند ایرانی-آمریکایی از کشور.
🔹
این عکس از دنا کراری امروز منتشر شده، بنا به ادعای رسانه‌های غربی، او دوسال به جرم جاسوسی در ایران زندانی بوده است اما مدیرعامل قوه قضاییه ادعای او را رد کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672944" target="_blank">📅 14:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672943">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4nyU7bVv7nR987BJRys0U6j_viaZxJiVABmkk9qpy4AysfXFMzqY0c1_9kWHPLVbT1DykQKaQsSEyKXycMrkBlizTnEPou_iZFJvAQaN3EnRIfW9sULGNvp_x2nmZgJmhnoME5iBVXGiEhWNOM04E_Ees6gODUywvv9sX48T2RihR3isP9erlt35_2UaPMBm2giPPKxkakCe8nIlP98DF8OP91phEJbY6hJgdlEF6dYv05x7nyclkOvAhLjfmny5qr9yL14KmYyhOKIggbq4yDJumzawZfUTX7eJaTMb9c3j9QDhpMB7i8qBZsVOOnPFlIdBiGZhbTbHVVNDOXZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وریا غفوری به شرایط جنگی و تأکید بر وحدت ملی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672943" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
هشدار امنیتی در اردن؛ فرودگاه و بندر عقبه تخلیه شد  سفارت آمریکا در اردن:
🔹
مقامات پادشاهی اردن، فرودگاه بین‌المللی و بندر دریایی عقبه را به دلیل یک تهدید مشخص و معتبر تخلیه کرده‌اند
🔹
ما به شدت به همه شهروندان آمریکایی توصیه می‌کنیم که از سفر به فرودگاه یا…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/672940" target="_blank">📅 14:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=tNjNOYMZjeaKCkMlQhjFvOiGDXihPaKkdP-IZeQ0OIJa-4D5toF_6e2i79Z0gTb0iC6qwN4VDX37Pf7AeAfLRrVLBxv4obhePyZDjfUoQK3wubhFMuFPzUx03w8YXK39pklzzxWkws3at-vuEddswqTIQSFXVwV89xlAsorNvzbiTQdOLSTC3mGNjynfpOJPiJr40oWUaxxmCYOQl1trYw9bg03K7_3F4IekSsZJ862astlYgiioWwn7ZK9-JBOzVyG71mEdKBffl-6ElkiVPEda0AX-kgUz3iFnnhnFNU5GokJ7L2e_4qUAWGWH564xS_oaVbjPBFHcueaZ-lX6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=tNjNOYMZjeaKCkMlQhjFvOiGDXihPaKkdP-IZeQ0OIJa-4D5toF_6e2i79Z0gTb0iC6qwN4VDX37Pf7AeAfLRrVLBxv4obhePyZDjfUoQK3wubhFMuFPzUx03w8YXK39pklzzxWkws3at-vuEddswqTIQSFXVwV89xlAsorNvzbiTQdOLSTC3mGNjynfpOJPiJr40oWUaxxmCYOQl1trYw9bg03K7_3F4IekSsZJ862astlYgiioWwn7ZK9-JBOzVyG71mEdKBffl-6ElkiVPEda0AX-kgUz3iFnnhnFNU5GokJ7L2e_4qUAWGWH564xS_oaVbjPBFHcueaZ-lX6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی: فلسفهٔ حضور ما در جنوب این است که به آمریکا بگوییم «ما آمده‌ایم که پدر شما را دربیاوریم»/ حضور ما فقط برای دفاع نیست. طرح «پاسخ پشیمان‌کننده» در پی حمله به زیرساخت‌ها در حال نهایی‌شدن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/672939" target="_blank">📅 14:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e259eddc1.mp4?token=rXRs6nwZpXZ1470SzU7q3_uaCSUrDxh5z9mIJQPYNta-Uh9soI7lDqC6CvZbMRGgjI5F8WUmCzYlPbZ_f00Pp5SiDwQuoLDMOVdJ5XY9NunYIJ-zYQEUgp18PfSBM7WWUEsiGafTVdivdUzHMBAJhFBA-bpj5zWqjy75Vuqo25IamY-2jj-HkTzJ9kFP5l6ax-DZ2OEK7l1lOAmAf67UglL9zq0p4X6XY4YIhUGMH00ccmiH3rbo9_J_Q-Qa41ftashphIZrQz8333XRpWlu021h_9VzqcxJY_niEN1FVyPSo2LGls_EJm1ePKompX8RRuv7E4J9oIKrFKsKq_gIF5oIQ7-AcIi6n0So-Z6so6K0xh3pOd1K_oz60mpIyOyL_7PZXn8NYgwmNJ-_w3w6w_c9vh_AZQDuJfkIxvTiHD7i6TEY3aAkIepioYVMsaKdiX_eO06gykI29srg_lrtqyEQ5QOiarwJmubDCA0aKRvrAX3Yfi0Sx6TwQiWQ2fdVg1bzxaCXjtCcs3mzA83NZsGECx41FBrgQn8H7sgn8SB6FfJn4Z5AIA-QznGA3_D_SGLGO8vMNiZEbcCfKFnCg9qdHqhcir3rMXbEcNrXUz71GB8Q5Cs1HbJjY1ZppL4_6SfGhaPBFlIIcu6FJL-JvCVL3g0cA3Kd4xYTLbO_sjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e259eddc1.mp4?token=rXRs6nwZpXZ1470SzU7q3_uaCSUrDxh5z9mIJQPYNta-Uh9soI7lDqC6CvZbMRGgjI5F8WUmCzYlPbZ_f00Pp5SiDwQuoLDMOVdJ5XY9NunYIJ-zYQEUgp18PfSBM7WWUEsiGafTVdivdUzHMBAJhFBA-bpj5zWqjy75Vuqo25IamY-2jj-HkTzJ9kFP5l6ax-DZ2OEK7l1lOAmAf67UglL9zq0p4X6XY4YIhUGMH00ccmiH3rbo9_J_Q-Qa41ftashphIZrQz8333XRpWlu021h_9VzqcxJY_niEN1FVyPSo2LGls_EJm1ePKompX8RRuv7E4J9oIKrFKsKq_gIF5oIQ7-AcIi6n0So-Z6so6K0xh3pOd1K_oz60mpIyOyL_7PZXn8NYgwmNJ-_w3w6w_c9vh_AZQDuJfkIxvTiHD7i6TEY3aAkIepioYVMsaKdiX_eO06gykI29srg_lrtqyEQ5QOiarwJmubDCA0aKRvrAX3Yfi0Sx6TwQiWQ2fdVg1bzxaCXjtCcs3mzA83NZsGECx41FBrgQn8H7sgn8SB6FfJn4Z5AIA-QznGA3_D_SGLGO8vMNiZEbcCfKFnCg9qdHqhcir3rMXbEcNrXUz71GB8Q5Cs1HbJjY1ZppL4_6SfGhaPBFlIIcu6FJL-JvCVL3g0cA3Kd4xYTLbO_sjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار غیرمنتظره وسط آب‌های آزاد!
🐙
🔹
هر صیدی داستان خودش رو داره؛ این بار مهمون قایق، یه هشت‌پای جذاب بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672938" target="_blank">📅 14:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تامین اجتماعی: حقوق تیرماه بازنشستگان بدون تغییر از دوشنبه واریز می‌شود.
🔹
آموزش و پرورش: فرآیند برگزاری کنکور سراسری و پذیرش دانشگاه فرهنگیان ادغام می‌شود.
🔹
نشریه آمریکایی: ترکیه مذاکرات با امارات برای خرید اس ۴٠٠ را آغازکرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672937" target="_blank">📅 14:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حمله آمریکا به سایت نیروگاه دارخوین
سازمان انرژی اتمی ایران:
🔹
آمریکا روز یکشنبه ۲۸ تیر ۱۴۰۵ حوالی ساعت ۳:۳۹ بامداد، با تعدادی پرتابه به سایت در حال ساخت نیروگاه دارخوین حمله کرده است./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/672936" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64f806a19.mp4?token=Rdd16VcYGz_Rwz6gH7G4roTcAPAbLnsNFEfYov1zKXbOSgRLMflaSbGXR1FW_WEajCJJFYfMBzWbdbq89vU54_y7vyMSxbgbrhZ-QN9X0a8ZkDSkHeesWBO5B-gRWSb8noV3zXsiesq3vH5CrDP9z6FQg8DcGMq9ZDcFXO2f7sEnmH4xy3BpHEQaVk5NihiCttIkFgBAHl4-n9LwPeT4aLx3SRq6f5sJ-6KAAIabcqhv2kYMmYn_dSoT2clVFcoJQj5fSLI6xlarPUxZ1_iSBHBk4v8OA9SQDenDblv77e3JuK-4Zdxonm1umXmwVcle6pcfoqEVwbUX45SzrRKX7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64f806a19.mp4?token=Rdd16VcYGz_Rwz6gH7G4roTcAPAbLnsNFEfYov1zKXbOSgRLMflaSbGXR1FW_WEajCJJFYfMBzWbdbq89vU54_y7vyMSxbgbrhZ-QN9X0a8ZkDSkHeesWBO5B-gRWSb8noV3zXsiesq3vH5CrDP9z6FQg8DcGMq9ZDcFXO2f7sEnmH4xy3BpHEQaVk5NihiCttIkFgBAHl4-n9LwPeT4aLx3SRq6f5sJ-6KAAIabcqhv2kYMmYn_dSoT2clVFcoJQj5fSLI6xlarPUxZ1_iSBHBk4v8OA9SQDenDblv77e3JuK-4Zdxonm1umXmwVcle6pcfoqEVwbUX45SzrRKX7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پل در تگزاس آمریکا به دلیل وقوع سیل فرو ریخت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672935" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تیزر قسمت ششم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای فرهاد قائدفولادوند که در اثر تصادف روح از جسم جدا شده و در حالتی که جسم در بیمارستان و در کما به سر می‌برد، روح نظاره‌گر دعای مادر در زیر باران، نگرانی و زانوی غم پدر و بدگویی همسایگان در مورد خودش می‌باشد و با وارد شدن به دنیای برزخی، خود را در حال دست و پا زدن در منجلاب عمیقی رؤیت می‌کند اما در پایان توسط آقای بی‌دست کربلا، دست‌گیری شده و از کما خارج می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فرهاد قائد فولادوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672934" target="_blank">📅 14:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اختلال در تنگه هرمز پس از تجاوز علیه ایران؛ تهدیدی برای امنیت غذایی جهان
🔹
روزنامه «آسیا تایمز» در تحلیلی هشدار داد که هرگونه اختلال در تردد کشتی‌ها از تنگه هرمز و دیگر گذرگاه‌های راهبردی دریایی، تنها به نوسان بازار انرژی محدود نخواهد شد و می‌تواند زنجیره تأمین جهانی، حمل‌ونقل کالاهای اساسی و امنیت غذایی کشورهای وابسته به واردات را با چالش‌های جدی مواجه کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/672933" target="_blank">📅 14:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHwtyByG2KJijutR0MjMEOoZnCwxPBhRM9w2THu9j5RmvUedbH9hF2md0yOrR5CP9p2tYSieXWTE5mn69VPr7j9lBhSfnlNYPup_ibsMMF3xnP2_38WXufJhNwxRrb9ysLQse9_0kZcq6NOxyGRKNF9a955gu4MOz1f_2-OM6ipHUsi7G4vo4fUilWORyiOcSE-rqmiiU_6qvQLS47zA8K4R-trKjtlBDWRJJFN3f90_QSDCmKxfBh2yme8UTa6BF2IgWX5halyjng8RpZXzltMPEhedEFZfujND55NywYJBgvj7c48VW0iCQ3PESwt9YGF1W51YOeQIJXPTWr73qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQHr2XSiP_9rGxIFLYkslAzPjpJkY1K97IuYtd2oJgcH4eP3J1fSkbYjDONXdrBt28t_B3dHC_HRldo81e4SANV54XPSifMdfZtAwUdeC7exfmGcnDDblDqrBQai6jr_mnLTAXFO_3E_7oIbwEnc3vbwlygwcmd7MDIMiyNTK_4VGDBYmhPHcUTbmeVeyBSNecQydfr4YTInQXBcj1NJBrE5AlPBbWKP5SEosUFOFhvLSeTVzQqyG3TDTgasxg2pWY7_CKdhYn-L5jV43QVFlznMK_j6AQTbe4savedt-ZC3qdQGPVFS4NFijzbdPY9BybbZ9mAwlSK3kWNRn5g3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VI2jqqag7LOgFns6iPT76D3VdJuMnCQC5R84dx_JNi9tiY1rSL-E7J3HXrcYjYpTHmZotuarxI5KRgS173SWkJjNUK1cMT0L_ETSoTzQQOUwGieRQ52Aoi2Y5-Q8wz-KZdv-xl9PHre43cwe4u5qxTKh2zA_6ccJR0ok9ICy7uYK6_yNiIgyQwzdH4C9WW3iWL9biTSnshx_nFbAph1B3_l5qeOLXWGhFm26_FGY47B-OZ75gUm_JaF2OL4zFHoEkg85HvH7M9ZGHHd-Re7boj2bJSPb7kOsinqxPST232A7aZbfCEB_BXUnXbEtRwbly4YI9NbFfnaCnIidp2eWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7bvS72DXTH9iFCG_LyM0mItkCFM9GBqKuex1FIaeL627rh8Z0EB2FsLr-n-VBvlfbl5hTht8meP2WLs9VChAXy_L_tjrXNHCVArx-fGc4YjZe9cOO0M3UBp0sB8Eb_rc34oEqwPqqlZyNpKddLq4XTX0JDnguovLR9PpD1oKNKp6DSQHkoIFOlEJnp22qdNhV6Vq45Xka4bjS8K3d9l4Qet-l6bDHwaB6lQo--iFXbg0LdmLmP26A9HiaIcflUj19b2MkuZoYple0y96qsd8GcpNx_YygAHekdAu6mOHuz4Ks3HW0RmcAEmYMsa6HNC85WoHtaV_JQNpU_rldz24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFaJd6i-WauH743Gh8O3cd7TwgMJF01AOKTLVsEEEmaM62kZTNKJv2QVqKRVgyc2qWd6vS71RpxEkvyo2trD1czgwcJSTnIspYkG6t1-HKDL0qYaaUb4R8u_3qs8m5ASqaaMOaA3Rnq9HbVy4lWtLsAGCzD1ipo48YMw2SyfNrw0pa1jhU15UD6wq7qWxzvNQMTuxn4HhSA2subXhRcMp-eF9_YQmMjPrfurfAzg-IrXDBqXLewrIBOHqf3D3F9rHWHr2VhRIpo4bOv0HJRiDz5JQWBv8X1hEFhJ4Ufxo5loYPHWkjLLVMtxvoObfMeAKP-H03lxSz1KGMi7wI8YeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtI9_ZnaXSse9o3OXhBZIR0yNq_dcpfUGGsL5hrlHzP3ZoNCHKxm_QhScujo28M0B3VxcgJZyZIDgl_Bff3oTNIobNbgXVTL4Q0lYrGzsddVlMjg_77FUq3S84q0Mgbpz-r2jGwwNPsMT4MwHeDck5ThC9vyjdmdPixXiVB9NJ7sIIV9DohtQO-OCFVIEIYUAKMVbvZPFe55TXdcJQoKW75kwPFNP8arM7BmCwDDcPsbYGTHM7FVpcDe396kxTzsn0zR2ffKb8PkTIrvdvKrF-E75yAyIDLvwJyvcndN-QLEDr6AOltvmniXA0p8Cm3pEw13dyOSNcld2FBiapVerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVOoP89s6x104A9XTC4mQmOFS4c7MUQGOb8l8x7oM5vJKi75jlbB6Qxaht2lnzEFVBdHEOJ-xo9kYStFzJDCeFBbhOpZZoMEjQLkuYQEcSGM28eFGb-LwW0jLYo4kj1cW77DO_F8sjiKNfhGCUH3Nw2ZfSQi0iSWfn0Jtl9Zls_RCVZCQNjtSsHz1xNlO8FQENq3xYWepSgWWsjQqHOSFddQlF7dgN2TkZs7Nq0mXgsa_G5xYzPNkHmOtOAEY88H-oGhMze8xQ4eRIBSsQjplat92n4Z7vv_mZKNFIW7uOOOHSIml_5wY2BBu55cyMXrWarM_TEJVtQndAz3oYvtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-4KB86trxOkOyNA5M4nCH5g0C7fUsgItNOtFL_HKjU3bpPhtdXlYEJuG5ePZnKrBUYaCOQSIxvQcRqxMoAQnF9GQBf9vawr_Vo2KzcfLa0yzDy4f5iuIzaYIXgrzkvPyGWDdcmIuBNynLEjFgfCHSN41btcZEIAosew5_YJxCFprvMr6wW4mTMu9aOlfFXOq6W_cQim5azAXOO106OaifkZ61xVlRh6qcHBNUjfBZ64FDBtVrg5AcHlyrGs3I9aW1RejZZorhxr-uJzKf0X0zDBo-mseT3PE_zQd4rSMmM-vJeVl5eiT3ox-THQBCUOK8lyjCDRs42388Fb9x_NtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nx1u2AFmZ1Zxint1_n0jJTCQ1DRVkuJrs-KnOiwfnxniUSYmEh6GLemH4fA2YMJeBJcRRTnt1Y5DC5ABza5DQkfXDCmpvBeIMbAjHCc9EHHKadI4KET1AfYplR--j1j74kXttSQyyV3QS5D9k1sbig8g-yGRgohHj-BFT_rR4CFBM0vuRdsyCY4ynzIAHaImphbeMuoABU6Z8Liq7sSfZd5keLXerIF1Lq-Q8hnfuJzK2w89E84cbfPDFroCfUiY_GIFfwv_Y1SjoWHNgzMy0tz88nRm9Q3kMJukPSzpHPdm20yiwaNzZJ3ve9y_4J0NDQRhfN1NnOPsIVNeXSeDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQaYY482fZFYlLjfCgDYvKodXQB-82icLOxEFpmn_iVtQQ_wajmFNi51yjZ8EqK8LyE-CG5ztIDEcukhaZuUPUvCJu5dXT9T-REIA9PCFr7zesBcxuDzZ-MmhRA7j18vq9ssFoH3Y7cIek_KUS62ODpQNaSGH5VQx6z2676catOzITCKc8g-43bWm4WAMF1bdsIEgBjGOEcqi5Fa45SuaDJWN9EuIrJV7Xrn3L9yl9ZKhuUCeiuKP7qykiK2xZTjQq9zCx4_M8E2Q6ODaOQFxdANW50thYvnqNokvmuo8awoq8t2UPixvEV1GFjcekEl99FXKU0Fy_gR4D8ONginkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر نمی‌دونی با هر شلوار چه شومیزی بپوشی، این راهنما را از دست نده #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/672923" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672922">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c485db783.mp4?token=WeHbEDA7ofqUje37nXx9aEvyBEO2qecikn7fdrE3ptRk6Qb93ZtFoL90ahq2Irirvt2i_yhDcHRXAf-vezvRZIMyX6i8EhPHqPxVK4Tw5exhOn84vQZIjeW5LRb0xh9-kyigxKrUwQssz8TvOMYrJ_4dOMuGTZ25mIdCjp_SbmCuvoNzTtHl_ZzYERbqBBAriNZLoJWumv4hjhZM6qFn-6Bw2X1bV7nnbpv9lnP6TVhywYRXkKEXJaRBwg2qHhoEqd1cT6g4MvovSX2Vou95tGpyeKdDtDR6EU0FVWOR-TmE0f0K1XK0d8aaAhONrFrd0btB4rVnnMqlR_w53no2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c485db783.mp4?token=WeHbEDA7ofqUje37nXx9aEvyBEO2qecikn7fdrE3ptRk6Qb93ZtFoL90ahq2Irirvt2i_yhDcHRXAf-vezvRZIMyX6i8EhPHqPxVK4Tw5exhOn84vQZIjeW5LRb0xh9-kyigxKrUwQssz8TvOMYrJ_4dOMuGTZ25mIdCjp_SbmCuvoNzTtHl_ZzYERbqBBAriNZLoJWumv4hjhZM6qFn-6Bw2X1bV7nnbpv9lnP6TVhywYRXkKEXJaRBwg2qHhoEqd1cT6g4MvovSX2Vou95tGpyeKdDtDR6EU0FVWOR-TmE0f0K1XK0d8aaAhONrFrd0btB4rVnnMqlR_w53no2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشی وضعیت لبنان از مناطق مرزی ایران!
حسین پاک از خط مرزی ایران: پس از سه سال حضور در جبهه جنوب لبنان حالا در جبهه جنوب ایران هستیم. جنوب لبنان و جنوب ایران باهم در یک جبهه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/672922" target="_blank">📅 13:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672921">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
قیمت نفت به ۱۰۰ دلار نزدیک شد
🔹
قیمت نفت با تشدید تنش‌های منطقه‌ای، احتمال انسداد تنگه هرمز و کاهش ذخایر استراتژیک آمریکا در مسیر صعود قرار گرفته و به مرز ۱۰۰ دلار نزدیک شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672921" target="_blank">📅 13:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672920">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsnLE49XdF0y4YlxOwuoztTNOWTbc52g6BVUuaSVSwbd7az7zJCOc6JDFywvTama8dr67DhUu0I3h0YvTdKNmgBTY2OANhB-_A3OSkqZwdVFPfbgc4WdkCpC5KiCKdPXDelAPEblS6YRoRTOUv2oD-mIMYEd2UdiJc5BwZtFI7gcRpMAxFp9z1NyruS5_PSVtEpUixQ-ZdtKtcz5nGZUXt71mT4dhrNaRCtRfAUjLtEHnUy6HILgeesFqEQZFq8tVo57IobTWXPtysV-x98RAYMaTLyTeZ74kE7_sCi2U2lOlMwsQqdlQBhuzRGhwvWhUS9MwJVnj9J_IvvSGZ4nOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸۱ سال پیش؛ بمباران آتش‌زای اوکازاکی توسط آمریکا
🔹
بمباران شهر اوکازاکی، طی ۷۸ دقیقه ۱۲٬۵۰۶ بمب آتش‌زا بر این شهر فروریخت. این حمله ۲۰۷ کشته، ۱۳ مفقود و ۳۲٬۰۶۸ مجروح بر جای گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672920" target="_blank">📅 13:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672919">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030701a507.mp4?token=hh5d8WmG6wD93AnSg4QY_XCVsVytBoLCd8pT4YViy-uOqqqKVQ8HFYBMmQYwJXs0e7eRgrOApIGPMgGrPtiB4I3Ml1hpUOpVRN-nRZ6aTW0WouT6P80ZvVOPDurUXqE8DlqVEWbUVgp7KNxVwDqSmrle86WUIK0gDnFSKHwrMuKiq9RfWatAEmf4HbvNJ9RIupumBXgCLNvMlS5siM0fta_PnvwcRcFn4F3H96MlyJ9GdprLSUx3EXj30hO5Br9NQez3pVxgM2CHw25wE6j_mxo30BKufBWWjjwzLQ85Ap65U0V5ayTNNPnb4k8I68IJnCLyPNNFPG92vn2CxWd_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030701a507.mp4?token=hh5d8WmG6wD93AnSg4QY_XCVsVytBoLCd8pT4YViy-uOqqqKVQ8HFYBMmQYwJXs0e7eRgrOApIGPMgGrPtiB4I3Ml1hpUOpVRN-nRZ6aTW0WouT6P80ZvVOPDurUXqE8DlqVEWbUVgp7KNxVwDqSmrle86WUIK0gDnFSKHwrMuKiq9RfWatAEmf4HbvNJ9RIupumBXgCLNvMlS5siM0fta_PnvwcRcFn4F3H96MlyJ9GdprLSUx3EXj30hO5Br9NQez3pVxgM2CHw25wE6j_mxo30BKufBWWjjwzLQ85Ap65U0V5ayTNNPnb4k8I68IJnCLyPNNFPG92vn2CxWd_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نباید مسائل خصوصی افراد را فاش و یا به آن‌ها ورود کرد
اژه‌ای:
🔹
ضرورتی ندارد تلفن همراه فرد را در اتهامی متفاوت و غیر ضرور ضبط و همه محتوای داخل آن را مشاهده کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/672919" target="_blank">📅 13:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏆
بهترین رده‌بندی تاریخ!
فرانسه ۴-۶ انگلیس؛ باران گل در میامی، سه‌شیرها با طعم افتخار به خانه برگشتند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/672918" target="_blank">📅 13:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=vAdKPqz0nCvMgN0qb49iIMXxexQO1ov_Aue_A33l7w4YllsDDfmbcSY-RN5Nnd4Lnl1szUvyLCyzniCmsmWz26thX_331NlMHW7XTq1YYGiPc-HdldVucFthqC2InydV4KTLAS3Vvr9XsUrdhDSNenj9QkMhXtJNwrQM7a-uharb6JaxJCEdxSSE7MmiuGsOET8VuKiWCrB5MnnccPmDgICmDnLTuMSzG2feA9xZWWagvkr61BTypoRzLhe0fs1nfQE1tb4Ase7T7FvwuPZYTl1jMYp4RYf6uv9BejOT-RCzrw9Eaf18B2lvdsNhS2sldPcZMz6pPvkvjqrzfGCsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=vAdKPqz0nCvMgN0qb49iIMXxexQO1ov_Aue_A33l7w4YllsDDfmbcSY-RN5Nnd4Lnl1szUvyLCyzniCmsmWz26thX_331NlMHW7XTq1YYGiPc-HdldVucFthqC2InydV4KTLAS3Vvr9XsUrdhDSNenj9QkMhXtJNwrQM7a-uharb6JaxJCEdxSSE7MmiuGsOET8VuKiWCrB5MnnccPmDgICmDnLTuMSzG2feA9xZWWagvkr61BTypoRzLhe0fs1nfQE1tb4Ase7T7FvwuPZYTl1jMYp4RYf6uv9BejOT-RCzrw9Eaf18B2lvdsNhS2sldPcZMz6pPvkvjqrzfGCsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مناطق مرزی جنوب کشور: آمریکا که قرار بود امنیت کشورهای عربی را برقرار کنند، امروز توانایی دفاع از پایگاه‌های خودش را هم ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/672917" target="_blank">📅 13:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiZzwVX472FvVbohdbW6JXvHGipKWkLuhGkWWlqG6lbTp4Qtqo2uU6vEhT8eknC67njUvutxa9AyKc4X-0PF3vRnwMUsj_6IujYuFsRFcOg1zG5TlvkVb-4sUfwbImkcKHhPomOQBDQOcUVvSAYxJuKfyZYm_Wv4ZdEmvyKfjUF2Ib-AAjfuRpuFs9-vrnKHaLYS1yv0F-V37fdvKVjA669Gogy-MNum9EHu3qgyNqal7jKvUGoVI-4BQafQweZtyqPfEmIZ_tI3osFduGw6LI8B44KdLS0AHNz8SlArlqmEFBK-wC95pzK-fq_eOyTLlovqUHIbUQx3T9LKaa69mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور رهبر شهید در آب‌های خلیج فارس در تنگه هرمز
🔹
در جمع دلیرمردان نیروی دریایی ارتش جمهوری اسلامی ایران / مهرماه ۱۳۶۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672916" target="_blank">📅 13:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
هشدار امنیتی در اردن؛ فرودگاه و بندر عقبه تخلیه شد
سفارت آمریکا در اردن:
🔹
مقامات پادشاهی اردن، فرودگاه بین‌المللی و بندر دریایی عقبه را به دلیل یک تهدید مشخص و معتبر تخلیه کرده‌اند
🔹
ما به شدت به همه شهروندان آمریکایی توصیه می‌کنیم که از سفر به فرودگاه یا بندر دریایی خودداری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/672915" target="_blank">📅 13:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
۲ تن از عوامل بی‌رحم جنایات میدان شهید علیخانی اصفهان به دار مجازات آویخته شدند
قوه‌قضائیه:
🔹
حکم اعدام عرفان اسفندیاری و گل‌محمد محمدی، ۲ تن از عوامل بسیار خشن و بی‌رحم جنایات میدان شهید علیخانی اصفهان در کودتای دی‌ماه، بامداد امروز اجرا شد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672914" target="_blank">📅 13:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672913">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8faf84a6.mp4?token=slAjXSpiics99YlgsTK-SnQnGWCdjcOF7D7eQ_mkz2HSTNSHYYvtN0_Dn_ron9tCS3yfquWJiiYxMIkn54OkFmvSrstEDyIvFeYNJufY_bMFlJBfiS3i_7CtKn05ExBMraWxlI7CaPtCOT6spf1RaiKefuKah1Z-jI6IxdlPfN5LHzGlqDdZflNhJ0HsFosn2SCKvBKeI0Tb5LDmo1GskOMz3vdmi94B-mSvkTT8VQmnseRLUjt25lHk5AkO1G8PswWR8biaonu7FEKp1ba9LRbmJ8IwW9DVEHKK28mUHTg5chRUC1q4CV3ultnXwksbj6U431ZW4IhvvX-Wrop0RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8faf84a6.mp4?token=slAjXSpiics99YlgsTK-SnQnGWCdjcOF7D7eQ_mkz2HSTNSHYYvtN0_Dn_ron9tCS3yfquWJiiYxMIkn54OkFmvSrstEDyIvFeYNJufY_bMFlJBfiS3i_7CtKn05ExBMraWxlI7CaPtCOT6spf1RaiKefuKah1Z-jI6IxdlPfN5LHzGlqDdZflNhJ0HsFosn2SCKvBKeI0Tb5LDmo1GskOMz3vdmi94B-mSvkTT8VQmnseRLUjt25lHk5AkO1G8PswWR8biaonu7FEKp1ba9LRbmJ8IwW9DVEHKK28mUHTg5chRUC1q4CV3ultnXwksbj6U431ZW4IhvvX-Wrop0RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک میدان نفتی در کویت دچار آتش‌سوزی گسترده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/672913" target="_blank">📅 13:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672912">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b42b0015.mp4?token=gu-01ayOGfbSaCVV6xuoYHPGPieNVVKNBUtYYfG3CjoVyPDetCmJLzdUxPa_Jq-PnRV6T6ZhkKKB5fEGjggM296FtpCMMe7OSPzL49RUAJvN9RHvjLFpcyeQMpBgkTSsi5H0hxY5Y6CwQYlnkspBlwMZr_jZraenzwDWg3pWt7PO2sOo4F9Hi_hUrlpsnfRvVX8BYYYXYc1yYMXuJwlv50gDD7fh7A-bYoetjpFa5-e8Bw5gRorDR5ZFtcKZ2dW-R0MDbbRmfU-6Use_kssgaXbh0EC4ZVd5YxYqXh-yy6_8z9YUDNKlTNV-lK-igDG4nxy5se42HHg459lN0aAMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b42b0015.mp4?token=gu-01ayOGfbSaCVV6xuoYHPGPieNVVKNBUtYYfG3CjoVyPDetCmJLzdUxPa_Jq-PnRV6T6ZhkKKB5fEGjggM296FtpCMMe7OSPzL49RUAJvN9RHvjLFpcyeQMpBgkTSsi5H0hxY5Y6CwQYlnkspBlwMZr_jZraenzwDWg3pWt7PO2sOo4F9Hi_hUrlpsnfRvVX8BYYYXYc1yYMXuJwlv50gDD7fh7A-bYoetjpFa5-e8Bw5gRorDR5ZFtcKZ2dW-R0MDbbRmfU-6Use_kssgaXbh0EC4ZVd5YxYqXh-yy6_8z9YUDNKlTNV-lK-igDG4nxy5se42HHg459lN0aAMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید، جنوب تشنه خون شماست
رجز سعید حدادیان از خوزستان: اون دست هایی که نرسیده به تابوت رهبری می خواهد بخورد در صورت سرباز آمریکایی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672912" target="_blank">📅 13:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHAVq2pPey-rYltT0QtcYhIfYeD0ws5w6P-1ONe10iv1F3zxZe_FPQA-kdS1-CpFMLPr3FzeL1v0jUcpFrxgLFptEuE6RoOVP1dsvUlq_xN9Sb0LTTr1CohxC63YuHuvWCnPAOZshOt8jXLb-FNkejiQqBuYzTScVwQ6UAf7uxA7a1zCZ6KqeTkZ_os5KJBysMnMEoKYtLJ_g7_DydWeIGJxcqVAPIyjWLCvO0MRIu0zqFfIye8iun-YsCgvZk9hU_mdxXuRp27RStbwBXi4yKhUv-bRhNEXI9Gzx9RuWD8qqGox0csjnH_wCO_-3EpMbDp-9X_kiYnBKM6Jg1NDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnzjzkkELShU0zWUXd3wqVpkIPTK1qEOWTa4cnuwI_Roq4vsz9qeK8TYU03gdKEgvC7G8mUuVm_johNVQd3YE6uEmPCoM9cXZpsYROeS52WM0cVHJCF314q-Z-z8XFF5k9m3tPNadTYrXt1HgOqd3GDto4OEfvNC244cArtjd6mEanQehldLPu7H3THEWmfrkOYbMlRXUEnvTVbD3sXzjagGcc73FR8Fj-Pze4QQRGWl6S6SYZAiIWrBgZr-rhUVUOZy7RVfYR8uMWEzHkatQh3wXBHw16xRL1CgIwvyjZTPLLaMT6sCnDpi568YWor_a-D8_ylIF1ONF8BoZhT6Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اقدام عجیب مارک Dior که با واکنش ۱۵ هزار کامنتی رو به رو شد؛ وقتی پوشش مردان قدیمی مد روز می‌شود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/672910" target="_blank">📅 13:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyJ4WbbfbQo7HkabYE-Ib1_w_K_7SqwA-eck8chihxxqBsFj7Ba1YKjI_EfKONqbOSMVFDUFjnpPga_6P1gRsEZP2T_fQSdhmbixmIi719GzqI9-SkGUhhOzvuW1s2j09hoqvkzlVpkQBvvUnyEjhwpohcJ7FOjxYJwjfEyDnOS1UgbnLYDEaKQBZ1Ee9YXGGMRZBwIZu_yGIdLs7LGVPl4RCEWsNaYu1261qn_GEmF_dGZ5XQvDJIwGqbVIrSOK8wVHeb7VRj0j629wgHVbXE7UJrjaTDmhV21Oq2gAiDIMwvONilBRyroqeOxgvf0gmTYzYqMmwpX1NPozrO1ylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتایج تمام فینال‌های جام‌جهانی در طول تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/672909" target="_blank">📅 13:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672907">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9323938ddd.mp4?token=JpHu_vpop7av1qYGDi0egXe34yjwzStcFkFZNqfHLlHKk5MkboGzwsWXaXpA99UbbS8kuuFb0fckMsNNfWO_ebNZJuy1VSmrhzMXeldQ7t-yt3gAG4J55HfdwErOv-sPsnT1BS7fc2zJLLDFClzXM6il3v1E6nFqUWvjv_pgM7XofpopvXtJz3adKO_stEn9NnqWOELdGWWP97uPDksEnl6rJ6yGInViphkSYBYelnZAltTzMRVMSCzKikB6x8i7vn3qmNTIYBKILXr-cNwXUDSoXo0sdQPIEAFbFtiKYbTucGepB5YOCHURhdfONwpALJOfapc7Pb9Da5jHlAc_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9323938ddd.mp4?token=JpHu_vpop7av1qYGDi0egXe34yjwzStcFkFZNqfHLlHKk5MkboGzwsWXaXpA99UbbS8kuuFb0fckMsNNfWO_ebNZJuy1VSmrhzMXeldQ7t-yt3gAG4J55HfdwErOv-sPsnT1BS7fc2zJLLDFClzXM6il3v1E6nFqUWvjv_pgM7XofpopvXtJz3adKO_stEn9NnqWOELdGWWP97uPDksEnl6rJ6yGInViphkSYBYelnZAltTzMRVMSCzKikB6x8i7vn3qmNTIYBKILXr-cNwXUDSoXo0sdQPIEAFbFtiKYbTucGepB5YOCHURhdfONwpALJOfapc7Pb9Da5jHlAc_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسمت چیه؟ احمد نادری
کلاس چندمی؟ دوم راهنمایی
کارتون چیه؟ "دفاع از خلیج فارس‌
"</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672907" target="_blank">📅 13:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672905">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=NoDLYEGemEphDYKi0Z9YK-NIrAUhkfOg0tyhDkoO4_IyH9KlOb8-t6c9ge4CN1JnuUww1yTXNeMbXnJm9UshkCvMVi1UHudhEVYrmpFUf89VoLKhsugDWxCQPveVRfDscze-AjJykFkdj4UckJRIsosDbs9l5TJU1_Wlo0AhsOHjW_hf-OSFjruZ8LAnu0ly5b1JbA49QdKvCnftukm-Cns2tl3khzYDeyCgj35RkMD2hSV7TcB9qvpmdlkYrGGqpmcgG9zI5yYgap0GFrZkHY5VcrMkJa9xRfhc4bhRh0JglRw-DNaJQlbUwaEHgpB2x6zC483Z1b7v1IqIrIOEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=NoDLYEGemEphDYKi0Z9YK-NIrAUhkfOg0tyhDkoO4_IyH9KlOb8-t6c9ge4CN1JnuUww1yTXNeMbXnJm9UshkCvMVi1UHudhEVYrmpFUf89VoLKhsugDWxCQPveVRfDscze-AjJykFkdj4UckJRIsosDbs9l5TJU1_Wlo0AhsOHjW_hf-OSFjruZ8LAnu0ly5b1JbA49QdKvCnftukm-Cns2tl3khzYDeyCgj35RkMD2hSV7TcB9qvpmdlkYrGGqpmcgG9zI5yYgap0GFrZkHY5VcrMkJa9xRfhc4bhRh0JglRw-DNaJQlbUwaEHgpB2x6zC483Z1b7v1IqIrIOEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدادیان: رهبر امت به ما وعدهٔ پیروزی داده/ مردم‌سالاری دینی در دورهٔ رهبر شهید به بالاترین حد خود رسید و کار را به ملت مبعوث شده سپردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672905" target="_blank">📅 13:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672903">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD01RZ5bgryfC7hzhbYWMNPx9l7bzz0ZJyaePHBN4nB9jj0HzLmx2MWFoEk3jT5Uems0AnoqgNBdhj-DcwV_aPnp3UV8a-W4bgiLNYs-ubNjgcTR1Tq3obm5eShykTe49B8LozYBMYBUJXewHrEzUxmcr2gkoNcp0qxk2vseWv-_pCG1C868Ud-jVGJwRvrIx1--bBsscfGru5dVbEXq2vvULkhq8cUkMmS4k3_sdQEKXEEs9h3zSezJjSRHep48JQVhIWbXdlOt6_ntBQtyf1zkFs1wfYmNJMjiPBXy3Kc4CnYo4Vn-5mx1rbchg6q9irJn2yry9SeI0O2Nk2f7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: اطاعت از حکم رهبر معظم انقلاب در اصرار بر اتحاد مقدس، شرط ضروری پیروزی در میدان مبارزه با دشمن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672903" target="_blank">📅 13:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672902">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDSfIGZDO8FNMbguUngfipVwq3oVP0uTVlcfe1QZu11TInQQn9qrACXSH95s490fBKvSJG0Mp3k722r6pH2yHXAsr7JRqXmnI_xNfsSrSEA5l1OG77I9pHp0IU6SqqBftlUJifVh6sZ9l4H2Y-C0nlGgxtlK2gDI96HRD8Sc3hSqtr0Pb6k5njyvixEDT56PJ1oRRewwBpnC79Fk75sbO4X8qflV6hRN8O9z5EJd4S7xnG7jPg4nQShwfXtWukIyxvv_JPYXNLkFd0uQ0JQ8RwuOYRFBhwii42splAWvu1VgqhcTn8wnS-r0c5adx5wPvPet467zMYSmbWL8TM7fMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام و فیسبوک از دسترس خارج شدند؛ مشکل جهانیه، نه اینترنت ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672902" target="_blank">📅 13:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkYDzOA89Flb3duS2KRILc7ZY_tRvPzCQjINlw--TQMcmFvo4qMZ0ily96KKUhCZRSkpc1ulm7t0i35LBfm4Tc5x4D_rvTx73rwCcW-mnDSYcq_AhLjE48TJKG9tuwhKEhGXy3sH9Ahohcc1AB06s7d1qoeX7RrvNppV13_mrST8gVrN-hcWx657cBp0kSYdE8EYBM_Jg9dWTR20Hncmpih8_dfr2mqW-9VCXWJ0pYydzjmFyfegTv7-WvbfeFKVjrS4XYEUBHFlApVm2RV1rt_FFBCc3dqGDyI624JnOU1K_VcepApej7vohgQ7ygbmkCD0wpjHIWaEzjWEk6cMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۸ تیر ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
دلار امروز روی ۱۹۲ هزار تومان بدون تغییر ماند و پس از ورود به کریدور ۱۹۰ هزار تومانی، فعلاً در همین محدوده متوقف شد.
🔹
همزمان با تداوم تنش‌های نظامی و ابهام بر سر تنگه هرمز، بازار هم در فاز احتیاط و انتظار قرار گرفته است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/672901" target="_blank">📅 13:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f055e0bca.mp4?token=jEN1MC7mtqYI7GBK0RIdgCrQIzYGVfVPsLrvyuwkOFuiiR_LkAuc2SQq05ImCFYxL7v81s_7npLTTUl6fQ-w0QLvzHk03IOYfvEc4ghD3F2JTRvfZAtUP5C5F6sNaEkQJd16Of_PZVPOXlTqs5yb8VmIIBFXR89xV6eqb_H8VGFrC6-wJph8EZUi6q1bAobP-lPI2OpZQ7JUQxz7xQZ8sXScTFdfkd5ZaFCeyoxCVxGz_uxANkiktjsfK5rPPXHzm4lFOLh4Vfb3nStPvMJREij_3BPEam4_2H9Cr6SrPeSeBAUutu3mhZq3-ZJ4RszJrm8GvmUGoqbTBfMb1VCR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f055e0bca.mp4?token=jEN1MC7mtqYI7GBK0RIdgCrQIzYGVfVPsLrvyuwkOFuiiR_LkAuc2SQq05ImCFYxL7v81s_7npLTTUl6fQ-w0QLvzHk03IOYfvEc4ghD3F2JTRvfZAtUP5C5F6sNaEkQJd16Of_PZVPOXlTqs5yb8VmIIBFXR89xV6eqb_H8VGFrC6-wJph8EZUi6q1bAobP-lPI2OpZQ7JUQxz7xQZ8sXScTFdfkd5ZaFCeyoxCVxGz_uxANkiktjsfK5rPPXHzm4lFOLh4Vfb3nStPvMJREij_3BPEam4_2H9Cr6SrPeSeBAUutu3mhZq3-ZJ4RszJrm8GvmUGoqbTBfMb1VCR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه دیشب بیدار نبودین، یکی از دیوونه‌ترین بازی‌های سال رو از دست دادین؛ حالا امشب نوبت فینال آرژانتین و اسپانیاست
▪️
قسمت شانزدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672900" target="_blank">📅 12:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672897">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b96146359.mp4?token=I81pFAhZ2e4pyL0yw3QGkGSBcglhSKFOP3LZvCnE7h6Dp49mdRuB5t2EGmsnX-To1eO7Q3uvs-JczZGISxEQDOmi8Cro8_XNa3f7RrGR7asi-QjmXfOgfXa4_lYUm7aengXyONXqW4Xl3pPYsV3D5mHsQ2-twSI8Ygm34YFp-zpCpdVlmr3RweyY-PgTX4fgH128bKXO3ZoMrKnZkDN9-VtvuQMw8xfLkC7HP-GZ-jCDghYlK6iI3bfxFQHdP55oeRVJdlzb6AI822yayVesyoelDolXxHx9dM4IBZgM0tP6KUq0mYyy7BXMmBEc79yuHtLxPCyCx8Yi0HsQAccU0RQlzFWynCjZ_9sJmov0HjlAifFVUQHJdU2UjhmGZ0CcWetwqvFERVzaIJVggSINdKAjvpDbvphyP4ekydrLznMrmd6V49GxuBZ-vQ0epoxC3f-MJUAuiQFsGuwZ2HgyNXCafYr8Fbt0gbqqSA7jt4cGTGG_gxdyEZelttwSP224Qlsln7x4ThHBA3wPI20biAV_aTaWyWIBLQd93Z-GrtYkrqn70FoMVYgTg6VM_f6Mqcm42dKYl99VcmQWFPt2OjzGoyJtaICzVROfB7DFtMM_z0Ag2VcWDG7sY-ugkEJbZC_M1y5U1wTuhzKNrEtsWHCFt_nJndMdVtLI7tuRkQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b96146359.mp4?token=I81pFAhZ2e4pyL0yw3QGkGSBcglhSKFOP3LZvCnE7h6Dp49mdRuB5t2EGmsnX-To1eO7Q3uvs-JczZGISxEQDOmi8Cro8_XNa3f7RrGR7asi-QjmXfOgfXa4_lYUm7aengXyONXqW4Xl3pPYsV3D5mHsQ2-twSI8Ygm34YFp-zpCpdVlmr3RweyY-PgTX4fgH128bKXO3ZoMrKnZkDN9-VtvuQMw8xfLkC7HP-GZ-jCDghYlK6iI3bfxFQHdP55oeRVJdlzb6AI822yayVesyoelDolXxHx9dM4IBZgM0tP6KUq0mYyy7BXMmBEc79yuHtLxPCyCx8Yi0HsQAccU0RQlzFWynCjZ_9sJmov0HjlAifFVUQHJdU2UjhmGZ0CcWetwqvFERVzaIJVggSINdKAjvpDbvphyP4ekydrLznMrmd6V49GxuBZ-vQ0epoxC3f-MJUAuiQFsGuwZ2HgyNXCafYr8Fbt0gbqqSA7jt4cGTGG_gxdyEZelttwSP224Qlsln7x4ThHBA3wPI20biAV_aTaWyWIBLQd93Z-GrtYkrqn70FoMVYgTg6VM_f6Mqcm42dKYl99VcmQWFPt2OjzGoyJtaICzVROfB7DFtMM_z0Ag2VcWDG7sY-ugkEJbZC_M1y5U1wTuhzKNrEtsWHCFt_nJndMdVtLI7tuRkQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: به جنوب کشور آمده‌ام تا از مردم اینجا دلاوری، سخت‌کوشی و میهن‎دوستی یاد بگیرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/672897" target="_blank">📅 12:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5gCi2PP8wn1fXf1JhgyiQoBKg7XJ0iw3KL2dWYw35GAjjshDk5STdnRPLkTkiG4smmWlkrBKBCgi5IX3JjdsK2_zPQZo0p8KT27iFgVS3ea88cOyfwv6KQiMVLBWPaw1Lrz29zsznHg6UcLVpPczX-rQDEjxVg-fvSlGesJ7FIAneGgXuaYeU9osWwBvqYl5EypW9qEdxSa025R6LxxJm_nh8K-bbzxWAv4X0enRVBF7Wxefmrg8GKODFJCVDPD36HfUxKbBhVWoZYLQFmyqHjKJ05U_qRLlk2T_oKZHjpArpLeeqEhKLYqMklAzNubeH0rvpKtDB-gihItJRIlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدون اعتبار، بدون ارزش
🔹
نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است.
📜
بخشی از پیام رهبر معظّم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور | ۲۶/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/672894" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA643PKtxfsvgqrBBEGtmo2BIUWJRz01ZV6wjc44Ng86yDbWid89T5I94pzvQt5haw9iVb9mVqBGKFdRQALXxoO0QYivfxeLFQx0-iIEeQVAdaoEg6sH0xTVonkjPoJVurhISwpvxJqeC7k0BMgLDFoSXAkphy7tvTTS6AS5u2fxc92uzoYArDqPyXsOeDws67kZs2JT74pzy5K_RMxAIU1WrfKyVT6tJKTw66uSg1bO--CLw3VwKMatZV0QrLII60dZG_4-5pRne7hEw_jG2yC59koc9GdktPKaYMFrHhC0miaC7tJdnSor7w3HuRQ0rMb1_0bN6liFiNKraT_OhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتو های عجیب روی بدن اوتامندی بازیکن آرژانتین ؛ بوم‌نقاشی است یا کمر انسان؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/672893" target="_blank">📅 12:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f18e2d1e.mp4?token=if-pYB749KPp2SWWzeReUMpLzvltP7jhHC5sOMLV5OGDJMZQb5f2Prr-Ukdha-WiWguscvoMlGmh8h2LcoNb7ITteTyNz3tGG1U4iAvvk4TlNlhgYMWPjTpJY1-G7qZQ0wLi3rr5oGPzt6l9OHmgTRQh9EPpwKG6pTjFkNSLPYtbEbp7kpAwMtpnpWVwQl1b18Cr6mHYRJxtssPtKb46k4ixwjlDvRshXb5rT_LITu4rItZIDsru9CFzivcA1bbq2kveHccXaTxpGrKezW240K6YynTmz_clAS3jvM4vMCZv_zmdaLIsBVWDzyvQ4u-9wlT_86GSrmPbooOGv2yd5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f18e2d1e.mp4?token=if-pYB749KPp2SWWzeReUMpLzvltP7jhHC5sOMLV5OGDJMZQb5f2Prr-Ukdha-WiWguscvoMlGmh8h2LcoNb7ITteTyNz3tGG1U4iAvvk4TlNlhgYMWPjTpJY1-G7qZQ0wLi3rr5oGPzt6l9OHmgTRQh9EPpwKG6pTjFkNSLPYtbEbp7kpAwMtpnpWVwQl1b18Cr6mHYRJxtssPtKb46k4ixwjlDvRshXb5rT_LITu4rItZIDsru9CFzivcA1bbq2kveHccXaTxpGrKezW240K6YynTmz_clAS3jvM4vMCZv_zmdaLIsBVWDzyvQ4u-9wlT_86GSrmPbooOGv2yd5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای یک‌بار هم که شده، به خودت باور داشته باش #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/672892" target="_blank">📅 12:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672891">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
پایش شبانه در قلب شریان‌های جنوب؛ عزم وزیر راه و شهرسازی برای بازگشت نبض جاده‌ها
🔹
فرزانه صادق، وزیر راه و‌شهرسازی، در پی تهاجم ددمنشانه دشمن به پل‌ها و تونل‌های استان هرمزگان، شب‌هنگام راهی این استان شد تا به‌طور مستقیم بر روند بازگشایی، بازسازی و ایمن‌سازی محورها، پل‌ها و تونل‌های آسیب‌دیده جنوب نظارت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672891" target="_blank">📅 12:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672888">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d10d920.mp4?token=N3GVkQ-etnM3GqUwuujyezA59mm_Q4rbLvhOl7r1EeLbUKADTdv9Wa0vuJ5T1jY6T00As-BQhnD05aDq4_dm3UtC4P-tfoYIt_XOV-_jX0kVk1BWSgkqUIjIiCQocLRW5pdzYO7OvyIg4UMXESxd3Eo4HBOUH1GwMJXEg1mPo3dEq4M3BTqdf4iYf_4nUaBwK3jy2-wes5m4c3JmCXTWLV1UfthZlLsd7oew11jKTSE_1ds-_mVphm7AgQhLWBED8fvbTOuOHEuhjJ9Q1BWGq-sQRJF8R644mCWoUHVdRy4_KNfh7CsB7OcGBp5y2kT89Q2F74-8CgcPNqTI7U7I2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d10d920.mp4?token=N3GVkQ-etnM3GqUwuujyezA59mm_Q4rbLvhOl7r1EeLbUKADTdv9Wa0vuJ5T1jY6T00As-BQhnD05aDq4_dm3UtC4P-tfoYIt_XOV-_jX0kVk1BWSgkqUIjIiCQocLRW5pdzYO7OvyIg4UMXESxd3Eo4HBOUH1GwMJXEg1mPo3dEq4M3BTqdf4iYf_4nUaBwK3jy2-wes5m4c3JmCXTWLV1UfthZlLsd7oew11jKTSE_1ds-_mVphm7AgQhLWBED8fvbTOuOHEuhjJ9Q1BWGq-sQRJF8R644mCWoUHVdRy4_KNfh7CsB7OcGBp5y2kT89Q2F74-8CgcPNqTI7U7I2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر انهدام و جمع آوری لاشه پهپاد MQ9 ارتش تروریست امریکا  توسط رزمندگان نیروی دریایی سپاه در عسلویه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672888" target="_blank">📅 12:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672887">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7764fe68bf.mp4?token=JHFyJMF1LH7JtJEqrDge8vK_Tjw6OmLthWzmj2SN9zEqgUik0xXcQmKUvxTEFAMM38ZbjMmJFpgg6Mw1pjnfFJC7CkupIl_JJpTTGmm3313rTDHegXndWgcodkSndKk8ru3BBoom1nIoEw7yWY_Mg36DMqU7ILJi4ozkxAa4LtjCOHt7biDcS6POdzvby9kPtvUa621iL46wad1rzYdqGwlcqltNfruKDf84CtcNFiQhuuZHaElraGalwpTQbc6Vzfg3rmkmyQ_MCNJ4MQgN4AqEJUsfanR0He-vUug91spc3PNpQ6EWiIQ8lpj6nacl8HwP9IVsENtlH7kFWVEESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7764fe68bf.mp4?token=JHFyJMF1LH7JtJEqrDge8vK_Tjw6OmLthWzmj2SN9zEqgUik0xXcQmKUvxTEFAMM38ZbjMmJFpgg6Mw1pjnfFJC7CkupIl_JJpTTGmm3313rTDHegXndWgcodkSndKk8ru3BBoom1nIoEw7yWY_Mg36DMqU7ILJi4ozkxAa4LtjCOHt7biDcS6POdzvby9kPtvUa621iL46wad1rzYdqGwlcqltNfruKDf84CtcNFiQhuuZHaElraGalwpTQbc6Vzfg3rmkmyQ_MCNJ4MQgN4AqEJUsfanR0He-vUug91spc3PNpQ6EWiIQ8lpj6nacl8HwP9IVsENtlH7kFWVEESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز روز امتحانه و در روز امتحان جز دفاع از خاک راهی نیست! #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/672887" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krFQHisfU72ouKL8CcZmsVdhbEKMnIwysF3EPG4Vnc1nytuwD6gba41CisCMiE6FuikkK-POobua3XPK6yMUjIbh8ovft5JpZ3_WlZ5Bcoi1ynIHamMTax5HdLCV9gFx68vHzH4xlhELnAitn0_Yi4i46-yyR2J6vQGsJMmWLXs--bCw1IVy_cpqxbz1BKaJInMDocyhCU4j59xNh1eB2e05vHsWXHovnhBl2LDBauHtPr5y6CqxjaGr4Qb8huCl3XRxt6ydu6irFhRt0gMHSVW-mJ_jjr1oAVl6JTuxxE86zG7rmJqmd3h8-PwLY-LH0oYfs0xgv1NZxh14hh-sFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن شما چه ساعتی خودش را بازسازی می‌کند؟!
⏰
#سلامتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/672885" target="_blank">📅 11:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
عبور از چالش‌های مالیاتی در بحران با مشاوره تخصصی اتاق تهران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مالیات، به بنگاه‌های اقتصادی کمک می‌کند از ظرفیت‌های قانونی، بخشودگی‌ها و تقسیط بدهی‌های مالیاتی استفاده کرده و فشار مالی ناشی از بحران و پسابحران را کاهش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672883" target="_blank">📅 11:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2e93e791.mp4?token=vT_FTuSX3CczT7eAR0GFk9NbxjQpyLcvYhZx_AYpYLQOe_2sO1QDKFrl-Ai9EABXqqFHTcfuY2BlhvQFfrfWIyAY51KTfZ2ByPyC-i7t4inuNanDqmoLDRdLj66WGMeLJoWI6GtAPrwkCMlQdOKb_2hx5O92zx4UAJKKncVnpfoqKemVaaJMjI65vpIvksmrc5qogzeuDGXMajKRwnmlWLY2UXcBkyZWpgtUHC1e5mFmBMCj-8mWXJdzpKUICnUcr3KRB4RtXZKay8tfjSH3Zzpm6Uy55uYXNqtvvNHTSpZJB4UPx9q2WNRX7XsnFFqXOPCrBzKdCpDnU2lz0XwBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2e93e791.mp4?token=vT_FTuSX3CczT7eAR0GFk9NbxjQpyLcvYhZx_AYpYLQOe_2sO1QDKFrl-Ai9EABXqqFHTcfuY2BlhvQFfrfWIyAY51KTfZ2ByPyC-i7t4inuNanDqmoLDRdLj66WGMeLJoWI6GtAPrwkCMlQdOKb_2hx5O92zx4UAJKKncVnpfoqKemVaaJMjI65vpIvksmrc5qogzeuDGXMajKRwnmlWLY2UXcBkyZWpgtUHC1e5mFmBMCj-8mWXJdzpKUICnUcr3KRB4RtXZKay8tfjSH3Zzpm6Uy55uYXNqtvvNHTSpZJB4UPx9q2WNRX7XsnFFqXOPCrBzKdCpDnU2lz0XwBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من به کشتی گیر آمریکایی باخت ندادم!
علی دبیر در خوزستان: مردم اینجا محکم ایستاده اند‌. ما هم آمدیم تا در کنارشان بایستیم و همه را دعوت می‌کنیم تا بیایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672882" target="_blank">📅 11:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672881">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgHv0FgBlk-XMws_rsMbrWWygHY4g_oJMR_OBExGRSLpvkQBpuQDajcV8ZpKd7OtayrSr9KYNrkDfKeepiNjPyEuRB_vkJHlAL3Yj6klYISplVN93SP5OBpD12YS7jcXc8O4s0fsQaApAZUTZOWhTTdtuGY8bs7b0hcSFz94YhuXoayLc7fUyu9HfpRSGyETzQq-HMMrRSj5I2LaUdStrH0UncKj6utpno_XeBa6fwI4yuGrOaUuMYiMcDaTcnIyWxZuQUVmOiMK2V_KXWOX5azVaU7CbKxNSYACR9IcS9f--muLkOrx_kbOtgFpQIxYCPbUT7GWm_LYZCoVqFAIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم اسپانیا قاتل فوتبال زیباست | چرا معتقدیم یک فینال کسل‌کننده را در پیش داریم؟ | این آرژانتین یکی از حماسی‌ترین تیم‌های ادوار جام است | همه‌چیز درباره فینال جام جهانی فوتبال
🔹
برای عشاق فوتبال، فینال جام جهانی نهایتِ آن چیزی است که وجود دارد. یک بازی که هر چهارسال یک بار برگزار می‌شود و تبعاتش به اندازه چهل سال می‌ماند.
نظر شما چیست؟ گپ و گفت خبرفوری دراین‌باره را ببینید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3231456</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672881" target="_blank">📅 11:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCauXsbvn9iaaYxvUjD-yuebd4sRP2pPr529ArhPqw42-u3fc4xir3aUcTz7h-754onIppIjbR_Plu7EMUwa9hjOqpBY1XhC8gFjzWJIggNmra5iZAIAtLm51-0TbZ8GpJEVt7J_Y2grQ-EKXjyfyy_7xi7HXjbPNNR80g2RcGyGzZH03PC_h3AtyBGnvWCCRZ6qMddkWfox_HrmN5qZfpJq4oq2kGTaMnDW2W1d3ziEF5nXHoPJC7UEhYz-tnk481NMhu2Coj6DpLYKy6uqXxEZwayPZirkmxmFjR1KZtGU0CwzXwNjPKTwadujAZwoKgdbzuAnIhRUN488HlBs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از انهدام آشیانه جنگنده‌های آمریکا در اردن
🔹
این آشیانه‌ها محل انجام بازرسی‌های پیش از پرواز، مسلح‌سازی، سوخت‌گیری، آماده‌سازی فنی و رفع عیوب جزئی جنگنده‌ها هستند و نقش مستقیمی در حفظ نرخ سورتی‌های پروازی دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/672879" target="_blank">📅 11:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO3cOh9MtMgUH1CymUI6dkEXY5diuSDvYjnIRg6gSBiHPWDDSOEuaFL4o6V2TzGaybfEqv2lAYcm-jzMOLmfkp2sTjJDmYyikdc_Bu_yklzRC5sIbtwia3irkdhPTePwIIPrrFjOZeWf35EzR7H7dU3D2nldM5GR9zsrmeVqEyKzhzreetbexioyXiRnx83Lg5joItoOq7RTeCF32PQ-LhiSFkbjfIcv7ewu2I0YmZjRcq4QIqRQR6XMFot32NUt7lwMLvg2eskXqcGVh9-vGtF77n2lr7xalAqo_8ZDVsyG1mZIqC684qQTEpYyc_ziirfxUPwGIO4HlCZU8nhf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر مهم برای خریداران بازار لوازم خانگی و فرش
🔹
در شرایط نوسان قیمت‌ها، شهر فرش و شهر لوازم خانگی قیمت محصولات خود را ثابت نگه داشته‌اند و با اقساط ساده و آسان، خرید را برای خانواده‌ها راحت‌تر کرده‌اند.
🔹
همزمان با جشنواره بزرگ ارزانی، خریداران می‌توانند از تخفیف‌های ویژه، هدایای متنوع، جوایز ارزشمند و هدیه در لحظه خرید بهره‌مند شوند و بدون نگرانی از نوسانات بازار، با قیمت‌های ثابت خریدی مطمئن داشته باشند.
🔹
آدرس شعبه مرکزی: تهران، بعد از میدان آزادی، روبروی تهرانسر شعبه مرکزی شهرفرش
سایر شعب در مشهد، ساری، رشت، اصفهان، شیراز و یزد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/672877" target="_blank">📅 11:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌹
دسترسی آسان به فایل‌های تصویری برنامه "زندگی پس از زندگی"
داستان افرادی که از مرگ برگشتند
#فصل_چهارم
🔹
اول
🔹
دوم
🔹
سوم
🔹
چهارم
🔹
پنجم
🔹
ششم
🔹
هفتم
🔹
هشتم
🔹
نهم
🔹
دهم
🔹
یازدهم
🔹
دوازدهم
🔹
سیزدهم
🔹
چهاردهم
🔹
پانزدهم
🔹
شانزدهم
🔹
هفدهم
🔹
هجدهم
🔹
نوزدهم
🔹
بیستم
🔹
بیست‌و‌یکم
🔹
بیست‌و‌دوم
🔹
بیست‌و‌سوم
🔹
بیست‌وچهارم
🔹
بیست‌و‌پنجم
🔹
بیست‌وششم
🔹
بیست‌وهفتم
🔹
بیست‌وهشتم
🔹
بیست‌ونهم
🔹
سی‌ام
🔹
سی‌ویکم
🔹
سی‌ودوم
#زندگی_پس_از_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/672875" target="_blank">📅 11:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایران؛ قتلگاهِ ریپر آمریکایی
🔹
سرنگونی یک فروند پهپاد پیشرفته رزمی-شناسایی MQ-9 Reaper در آسمان اهواز، بار دیگر توان عملیاتی و آمادگی پدافند هوایی ایران را به نمایش گذاشت. این پهپاد که از پیشرفته‌ترین تجهیزات شناسایی و تهاجمی آمریکا به شمار می‌رود، سال‌هاست از سوی کارشناسان نظامی غرب به‌عنوان یکی از مؤثرترین پهپادهای رزمی معرفی می‌شود.
🔹
تحلیلگران شناخته‌شده‌ای مانند دیوید دپتولا و مایکل کافمن بارها تأکید کرده‌اند که MQ-9 برای عملیات در آسمان کشورهایی که از شبکه پدافند هوایی پیشرفته برخوردار هستند طراحی نشده و در چنین محیطی با خطر بالای رهگیری و انهدام مواجه است.
🔹
بر همین اساس، انهدام این پهپاد را می‌توان نشانه‌ای از کارآمدی سامانه‌های پدافند هوایی ایران در مقابله با اهداف پیشرفته دانست، سامانه‌هایی که توانسته‌اند در جنگ اخیر بارها تهدیدی با فناوری بالا را شناسایی، رهگیری و منهدم کنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/672874" target="_blank">📅 11:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKE941khMiPYbMzBf2N2KMKdluFE6FQS4MNIFPVcvxB1QLygKHdsBKjP2KKZzdWhKmyStrQhLBjZUfXyqwR3Py1eBxkAOiFgu6dMVoFhYPG3Ej9yD-ZL4fL_wkIPjfd4aCnNXwxljnmGjWEjyMihorXhoMMEmg6IxfOKAYf4DmnQCGPtg2AFSzezbJwTs9Wkakz8jOPKm_S1FGFglStpD44PSi5gdPjSlTtC536CynS5s43kgfh6AjQPk9a9G39F1iklsp_LaF-6LcpxrBsT_QTmndnGjRP5uSLEOrkV3XrDHo_7WjaKe-EODLufekE0aB4xGSAcTF7yKr2410f8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت آمریکا به کمترین سطح در بیش از ۴۰ سال اخیر رسید
آژانس بین‌المللی انرژی (IEA):
🔹
ذخایر نفت خام آمریکا با کاهش به ۷۲۶ میلیون بشکه، به پایین‌ترین سطح در بیش از چهار دهه گذشته رسیده است.
🔹
برداشت گسترده از ذخایر راهبردی در جریان جنگ با ایران و کاهش ذخایر تجاری، نگرانی‌ها درباره امنیت انرژی آمریکا را افزایش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672873" target="_blank">📅 11:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672871">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pblsvR8OtxrW-88kDFWpMKVUkr8wjDt_9qjWC6NHYfL4J1NJZQ_w0WXTT0kBu-ds1LfYCkC9qnXRmVJOT8WyAdpfVOA9FNtjj7aq9rVGvbaG6QJj2pehzzDAHiubUmRvSTyDvZkl6ZWEl7XRwEMo4u-GkX58-yIPv2AxIYhOtDOL78syFatHkj17aImS7qadZBHKl0jTFZx-MB-gEkTKJ9xs8ddtg8XmEavdtOTjnRUPW1g6CTjbCcn0iNO9I1rBm6GCR_cpKg_3Mjs2fTwnX4WULESvR7FJFCKdZ0nO7TGDk4cKZgzpe_V1KCXNILNcc2svhCmXkT1cE0eQAD-uYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید گاز ایران؛ ۲ برابر سریع‌تر از جهان
🔸
ایران در سال ۲۰۲۵ با تولید ۲۶۴.۸ میلیارد مترمکعب گاز و سهم ۶.۳ درصدی از تولید جهان، سومین تولیدکننده بزرگ گاز طبیعی جهان شد.
🔸
میانگین رشد سالانه تولید گاز ایران در بازه ۲۰۱۵ تا ۲۰۲۵، با نرخ ۳.۷ درصد،
بیش از دو برابر میانگین جهانی
(۱.۸ درصد) بوده است.
@amarfact</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/672871" target="_blank">📅 10:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5597b0e4e.mp4?token=DHzXb3k28kpMFHtzVwpE4VGyEBJwIdr7G1QA7F9OKnpj3Oa43BCsFsv1aRhPmusqQZpvXHCNzzEaIcGaxQeLiDni6_tGnaNaE0SGoV4aZAhkopvuTmuaAMkSfgWuuwze0EKAj99V-vUAWMMKXhk2Nzj79Lm0i2a-k4W8kRuovnJGnt0nB2GCalN1RnUgl0QMD5UlYMYv2fIz7ysTUxT-yv-f3fTGHYLUSqsrlRXZYT2NIInCa0XuGtYLFMTod7G60yMAvM39CpgaeBqIm-tWlohKLbZTfdFareu08wXwTMVMlPWWFaXtG0zBLOZsJGX-NLtN5pheAy6c94H5pZfevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5597b0e4e.mp4?token=DHzXb3k28kpMFHtzVwpE4VGyEBJwIdr7G1QA7F9OKnpj3Oa43BCsFsv1aRhPmusqQZpvXHCNzzEaIcGaxQeLiDni6_tGnaNaE0SGoV4aZAhkopvuTmuaAMkSfgWuuwze0EKAj99V-vUAWMMKXhk2Nzj79Lm0i2a-k4W8kRuovnJGnt0nB2GCalN1RnUgl0QMD5UlYMYv2fIz7ysTUxT-yv-f3fTGHYLUSqsrlRXZYT2NIInCa0XuGtYLFMTod7G60yMAvM39CpgaeBqIm-tWlohKLbZTfdFareu08wXwTMVMlPWWFaXtG0zBLOZsJGX-NLtN5pheAy6c94H5pZfevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ایده جذاب؛ برای داشتن آشپزخانه‌ای بی
‌
نقص
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/672869" target="_blank">📅 10:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672867">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e43d0a32.mp4?token=DNlzfdjGJf4C-0EM5xYDNdOJlis7KZWWadBebveK2z4aHb7J936HzTrMFGXl1QjNYnKTDDiURpB_o0O_bjopIm0aiXOjAHaMfiS9eC30rC3CLzPq8Y1cMQ-xadHyTFYaBeo2U5PNYWrx2Q9M5QEsz5QzTqmqFOpJqUghNKgWIuwRCi7JOECHkSjFhPo24-WKUegU7iGp17z5AWuHlQmMXjwjq16auSn1ZgFaGf0Z1JGsTf34csmqsqJdeEaDqsGFbI_OH5jjwsII88qRhhvvSi1MitI4w8gBZtCQ5oIIRDvN_ruigk3jWLbBMA9GpeDefCmXeVeN2lZ6CQ9uDqS2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e43d0a32.mp4?token=DNlzfdjGJf4C-0EM5xYDNdOJlis7KZWWadBebveK2z4aHb7J936HzTrMFGXl1QjNYnKTDDiURpB_o0O_bjopIm0aiXOjAHaMfiS9eC30rC3CLzPq8Y1cMQ-xadHyTFYaBeo2U5PNYWrx2Q9M5QEsz5QzTqmqFOpJqUghNKgWIuwRCi7JOECHkSjFhPo24-WKUegU7iGp17z5AWuHlQmMXjwjq16auSn1ZgFaGf0Z1JGsTf34csmqsqJdeEaDqsGFbI_OH5jjwsII88qRhhvvSi1MitI4w8gBZtCQ5oIIRDvN_ruigk3jWLbBMA9GpeDefCmXeVeN2lZ6CQ9uDqS2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز موشک‌های ایرانی بر فراز آسمان کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/672867" target="_blank">📅 10:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672865">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8401e7c6a4.mp4?token=cvtRz6_1LJowkjm2ggO494YdU3yfgMWKm07IwWzoqFTQGHgIBJ5zGjoiWhKOMCCn3XKcp_m7cPdsff1ifXECngGvKuSCBaPMgZuQwiU19mt5t49Hv0gC7dVRpf64mVNUg39icfw--ezDmdFe-ZvG1V8-YUwVHCRDDw_GSNv4mF-yQwZUXt5PZz-CbAGXxssQdytgRjfIBLWFDCFl--8F8Vsc0OAflq5-1010Brk4QOzSq5o7eWlNUNEBUk3gp3IKS3S9eUEKnU3EPVZtBxhvQe1tTWvpM4zsh45Ta2EJVZGaCGEvdvX0TiFuGTo5fGMoZe5--JYzPvUXyNsPvq5pNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8401e7c6a4.mp4?token=cvtRz6_1LJowkjm2ggO494YdU3yfgMWKm07IwWzoqFTQGHgIBJ5zGjoiWhKOMCCn3XKcp_m7cPdsff1ifXECngGvKuSCBaPMgZuQwiU19mt5t49Hv0gC7dVRpf64mVNUg39icfw--ezDmdFe-ZvG1V8-YUwVHCRDDw_GSNv4mF-yQwZUXt5PZz-CbAGXxssQdytgRjfIBLWFDCFl--8F8Vsc0OAflq5-1010Brk4QOzSq5o7eWlNUNEBUk3gp3IKS3S9eUEKnU3EPVZtBxhvQe1tTWvpM4zsh45Ta2EJVZGaCGEvdvX0TiFuGTo5fGMoZe5--JYzPvUXyNsPvq5pNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶
🔹
برنامه بازی‌ روز آخر مرحله حذفی #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/672865" target="_blank">📅 10:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
این‌بار پاستا رو به سبک انیمیشن باد برمی‌خیزد درست کن
🍝
مواد لازم:
🔹
اسپاگتی ۲۰۰گرم
🔹
گوجه‌فرنگی ۴عدد
🔹
سیر ۲حبه
🔹
روغن زیتون ۲قاشق غذاخوری
🔹
ریحان تازه
🔹
نمک و فلفل به مقدار لازم
🔹
پنیر پارمزان اختیاری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/672864" target="_blank">📅 10:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdd44b039.mp4?token=CLAxzj_OBOqlbKwXjCJZMQDYdCMJS_iQ778WY63Pt1yjS0Yevl5PHcGz2hc1DCkAhBKuWGRrOaPq-7mwsCIeHxClNnJHVDKwfuXxR4a4cDaHWpf1qCdMOufgCo45dIH8fcEudKR2iy3Bamngu63bFvC6XgePQ-_FXSBh8PyKRAKuj6ie0rDFQes2BXc1uhca9Kicvw69Fxn-dHHWhXO__s0uRvF9C9P5lpH2_neVuv2R_cUONFhxxav-G4xWsqrZ0eH5xQJ81pxfyxtQgm6CZNK2EnAfbT7RsWn1QLAa6tMGrraOEShWsadsbUDUoLmGdtjgkKNTINSz7uHakBanSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdd44b039.mp4?token=CLAxzj_OBOqlbKwXjCJZMQDYdCMJS_iQ778WY63Pt1yjS0Yevl5PHcGz2hc1DCkAhBKuWGRrOaPq-7mwsCIeHxClNnJHVDKwfuXxR4a4cDaHWpf1qCdMOufgCo45dIH8fcEudKR2iy3Bamngu63bFvC6XgePQ-_FXSBh8PyKRAKuj6ie0rDFQes2BXc1uhca9Kicvw69Fxn-dHHWhXO__s0uRvF9C9P5lpH2_neVuv2R_cUONFhxxav-G4xWsqrZ0eH5xQJ81pxfyxtQgm6CZNK2EnAfbT7RsWn1QLAa6tMGrraOEShWsadsbUDUoLmGdtjgkKNTINSz7uHakBanSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ضبط‌شده توسط یک سرباز آمریکایی در پایگاه هوایی موفق السلطی در اردن
🔹
حداقل دو سرباز در این حمله‌ی ایران کشته شده‌اند، بسیاری زخمی شده‌اند که حال تعدادی از آنها وخیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/672861" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
