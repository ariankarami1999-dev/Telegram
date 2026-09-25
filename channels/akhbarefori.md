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
<img src="https://cdn4.telesco.pe/file/hM5rYHFbH5Hy4hoUtW3tGtxrkQXvpGcloEQyEORrzs8SMzWNtlFBmw0ZKDMLTtANMuU5zcDl1LL-oim7L-ubYZUZOUQiv4SphL5SnHtm7OKX4mPrrJGBzL7Sy8rvDnFAfb3mxEXu-F5UEKzYt-aXPjudGCm5-6c4e7hZaPjQ9ct5MdFmDdYmsJD2YI29SD_kYmolJYBHRy6UTmozBh1nmcSARWxX1y9MM7YdMZ9vRohAj1Fkqrekj4MK5QXsZX2ZuIwm8zl0iTFzQK222ntOSbuIpLSM-Q9sHUyYPuLcq4zZf-nncacEorAjhe3RsT8220VuA6UlITMaTy0z1ApRWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 09:47:03</div>
<hr>

<div class="tg-post" id="msg-692835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
گوگل از قابلیت Live Avatar برای هوش مصنوعی جمینای رونمایی کرد
🔹
قابلیت جدید Live Avatar برای مدل Gemini 3.8 Live است و امکان گفتگوی تقریباً لحظه‌ای با یک شخصیت هوش مصنوعی متحرک را فراهم می‌کند.
🔹
کاربران می‌توانند حین مکالمه اطلاعات را روی صفحه مشاهده کنند و سازمان‌ها نیز امکان ساخت آواتارهای اختصاصی خود را خواهند داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/692835" target="_blank">📅 09:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رویترز: تردد کشتی‌ها در تنگه هرمز به زیر ۱۰ فروند کاهش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/692834" target="_blank">📅 09:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d6992b64.mp4?token=b1DFZUlvLWDEmdUe0q6tzP6wJOYgwD7Ung7F-65MA7nPHEDOf1fblm66ozkdfT8qdnFk61ohtHfDIBcnsy8up90fzBs5aKpzMf4oJPuw0X2LIZReOqKM5M1sifABEFfMlNV__b9CizrEaaSkDjGRuGPSh6LVHt1cDytLITyu9HdzBPBrO7Aaff8Ufpaanv7cPZUTtElR-8JbwWCHF7bb_dyJ2SLQ0oQQo9_Vq_vXt3S1PmXMgXWaG28QZyPyItbOKQ_AvlEaPNxQ9CqnvWgksFz9lUCznQBU2f2YFPtDfep6wBcL4IxucV_CQxg37IA6VXw7D4G8OYnTUJjGgI68Ywp7md8KgwjQuDACfi1TN4GChgsRhLWGTE_t1y84e7vE-fJjBfR6KRJRB6fke411i4LGSFWE6dgBcZAl6U1lNfTxxIOFhMTjk0Mp79s_EgBAOL-E5fI3eb-b05pEJE1gyZgcVEkp94rx15UPNbN9P4ElWpRyRzgzFB-REaqwraUyypsc8glBHo6b01G7OiQO0nkXWISrjaF8fAggWakanIbcRel_uDvK5G25uYUrYrsS2KAPFq2Xa6zZuZ99JJnpsCWJGnkJgHk-SblkI1pJaa-WLVYCl7PuCMYJHwBSoEkco3xeX3M71Yx9KBZLWT2aLfsEJ3PRDAzdso_CHrbXBxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d6992b64.mp4?token=b1DFZUlvLWDEmdUe0q6tzP6wJOYgwD7Ung7F-65MA7nPHEDOf1fblm66ozkdfT8qdnFk61ohtHfDIBcnsy8up90fzBs5aKpzMf4oJPuw0X2LIZReOqKM5M1sifABEFfMlNV__b9CizrEaaSkDjGRuGPSh6LVHt1cDytLITyu9HdzBPBrO7Aaff8Ufpaanv7cPZUTtElR-8JbwWCHF7bb_dyJ2SLQ0oQQo9_Vq_vXt3S1PmXMgXWaG28QZyPyItbOKQ_AvlEaPNxQ9CqnvWgksFz9lUCznQBU2f2YFPtDfep6wBcL4IxucV_CQxg37IA6VXw7D4G8OYnTUJjGgI68Ywp7md8KgwjQuDACfi1TN4GChgsRhLWGTE_t1y84e7vE-fJjBfR6KRJRB6fke411i4LGSFWE6dgBcZAl6U1lNfTxxIOFhMTjk0Mp79s_EgBAOL-E5fI3eb-b05pEJE1gyZgcVEkp94rx15UPNbN9P4ElWpRyRzgzFB-REaqwraUyypsc8glBHo6b01G7OiQO0nkXWISrjaF8fAggWakanIbcRel_uDvK5G25uYUrYrsS2KAPFq2Xa6zZuZ99JJnpsCWJGnkJgHk-SblkI1pJaa-WLVYCl7PuCMYJHwBSoEkco3xeX3M71Yx9KBZLWT2aLfsEJ3PRDAzdso_CHrbXBxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش عالی برای رفع خشکی و موخوره با یک مایع نارنجی براق
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/692833" target="_blank">📅 09:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692832">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da67660fae.mp4?token=HhQAgWuyuh1xFpQPRbyeQjTRSp-mSaju337zbyuJIqCpvMsgzQKutwoxicPzVDUdqAmTeD2MM2E_voRY5qIDDQshWBFrOax0YNfgznpZ3gcc4Box-9Ho1anB8a68sYfVeUC0kWqUj-8UD_M5bcUe8lcykm-3yQaqn428nQAMAaLR1-Ag7m1GDKwJF7KFmkjm0p4Kfjcl_tknPETTBXYumWyPulYUTCTD4MwfFgwRr1ZKQg7Tt6bwbxKnJ8B_KzQ5Uuky_WQnOcSP2Ziyb_qU73IrtxppwLIS6x6il_5991Iu9op5MPbNHS8JyTXsHvufWvcucDlKfpOetVpTD8zwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da67660fae.mp4?token=HhQAgWuyuh1xFpQPRbyeQjTRSp-mSaju337zbyuJIqCpvMsgzQKutwoxicPzVDUdqAmTeD2MM2E_voRY5qIDDQshWBFrOax0YNfgznpZ3gcc4Box-9Ho1anB8a68sYfVeUC0kWqUj-8UD_M5bcUe8lcykm-3yQaqn428nQAMAaLR1-Ag7m1GDKwJF7KFmkjm0p4Kfjcl_tknPETTBXYumWyPulYUTCTD4MwfFgwRr1ZKQg7Tt6bwbxKnJ8B_KzQ5Uuky_WQnOcSP2Ziyb_qU73IrtxppwLIS6x6il_5991Iu9op5MPbNHS8JyTXsHvufWvcucDlKfpOetVpTD8zwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مین‌روبی بدون تلفات؛ پهپادها و ارتشی از زنبورهای آموزش‌ دیده
🔹
دانشمندان زنبورهایی پرورش دادند که بوی مرگبارترین ماده منفجره جهان را با شکر اشتباه می‌گیرند. محققان با روش «پاولوف»، بوی « تی ان تی» را به پاداش شربت قند گره زدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/692832" target="_blank">📅 09:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692831">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نتانیاهو و همسرش بامداد جمعه و تنها ساعاتی پس از سخنرانی در مجمع عمومی سازمان ملل، سریعا نیویورک را ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/692831" target="_blank">📅 09:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692830">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
محیطی‌زاده به‌دلیل کفش غیراستاندارد دیسکالیفه شد
🔹
فاطمه محیطی‌زاده در بخش پرتاب نیزه به‌ دلیل استاندارد نبودن کفش‌هایش دیسکالیفه شد و در نتیجه از جدول مسابقات هفت‌گانه کنار رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/692830" target="_blank">📅 09:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692829">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کنایه نخست‌وزیر هلند به ترامپ و نتانیاهو: اکنون که دیوان کیفری بین‌المللی (ICC) هدف حمله قرار گرفته است، نشانه‌های خطر کاملاً آشکار است
🔹
به‌راستی، چگونه می‌توان با پیگرد قضاییِ فجیع‌ترین جنایات مخالف بود؟
🔹
و به باور من، تنها یک پاسخ وجود دارد: باید گفت دست از سرِ دیوان کیفری بین‌المللی و تمام نهادهای دیگری که حافظ نظم حقوقی بین‌المللی هستند، بردارید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/692829" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692828">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه پنجم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692828" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه پنجم؛ کارساز هستی
🔹
نام مبارک
«الْوَكِيل»
با قرار دادن انسان در موقعیت «سازگاری» با جهان، او را در نقطه‌ توکل و حمایت الهی قرار می‌دهد.
🔹
در روزگاری که اضطراب بر انسان‌ها و سرزمین‌ها سایه افکنده است، تنها معجزه‌ نام مبارک «وکیل» می‌تواند کارساز باشد.
🔹
نماز اول وقت و اتصال به ساعت بیولوژیک هستی، باعث گشایش ذهن شده و جان را جلا می‌دهد.
🔹
گسست نسلی و نادیده گرفتن تجربیات گذشتگان، جامعه را محکوم به تکرار دردمندانه تاریخ می‌کند.
🔹
پیچیدگی‌های رفتاری، عدم صراحت و تعارفات کاذب، عوامل هدر رفت انرژی روانی جامعه هستند.
🔹
خداوند تنها وکیلی است که خود طراح قوانین و قاضی جهان هستی است؛ از این رو، سپردن امور به او، موفقیت در آزمون‌ها و بن‌بست‌های زندگی را تضمین می‌کند.
🔹
پذیرش به معنای انفعال نیست، بلکه به معنای انجام صددرصدی وظایف و سپس رها کردن نتیجه و اعتماد به حکمت «وکیل» است.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/692828" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
رئیس جمهور چین: با ترامپ برای ایجاد روابطی سازنده و باثبات توافق کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/692827" target="_blank">📅 08:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
معاون سازمان سنجش آموزش کشور: نتایج اولیه کنکور سراسری ۱۴۰۵ تا ۱۰ روز آینده در نیمه اول مهرماه اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/692826" target="_blank">📅 08:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c634382f.mp4?token=J-Q6ygyywm0hAqKDiMaSc_nPL6M9NfvgyCFlVVKX-wP4xhgWdDYRQIkdsg_fugMpLAUR_hHDuFoJpK3wuZEA5vKX4_VFkVi_1boUcVByoVLANxhep4Bg8nRfaunRBe_Zvgf-hwW4RYZoI6_3v98nvex95Jskq4hJUgmnJaKULUw9gQuemydPCXKvFgDNsCUWgP-PSG97W4pUxFAmACyK0vjFwhxWLSCjpRL2cAutCLZs2vJb-ytnJA7xwpBYaPiSXbhx4cN24Ufwc05PmwWCa6r3NWiKejMrxbuKS8Sx6mKKg_n3UIdrMmp0Lye1ch_n0uJcxWsLoZpjXc77eCcIUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c634382f.mp4?token=J-Q6ygyywm0hAqKDiMaSc_nPL6M9NfvgyCFlVVKX-wP4xhgWdDYRQIkdsg_fugMpLAUR_hHDuFoJpK3wuZEA5vKX4_VFkVi_1boUcVByoVLANxhep4Bg8nRfaunRBe_Zvgf-hwW4RYZoI6_3v98nvex95Jskq4hJUgmnJaKULUw9gQuemydPCXKvFgDNsCUWgP-PSG97W4pUxFAmACyK0vjFwhxWLSCjpRL2cAutCLZs2vJb-ytnJA7xwpBYaPiSXbhx4cN24Ufwc05PmwWCa6r3NWiKejMrxbuKS8Sx6mKKg_n3UIdrMmp0Lye1ch_n0uJcxWsLoZpjXc77eCcIUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلغم را این‌طوری درست کنید؛ یک نوشیدنی گرم‌ و عالی برای روزهای سرماخوردگی
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/692825" target="_blank">📅 08:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ان‌بی‌سی به نقل از عراقچی: طرحی از طریق میانجی‌ها به مقام‌های آمریکایی ارائه شده که در صورت پذیرش، تنگه هرمز در پایان هفت روز باز خواهد شد و مذاکرات از سر گرفته می‌شود
🔹
این طرح می‌تواند به‌محض موافقت آمریکا آغاز شود
🔹
یکی از شروط این طرح، موافقت آمریکا با مسیر عبور دریایی از تنگه هرمز است که میان ایران و عمان بر سر آن توافق شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/692824" target="_blank">📅 08:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6879a05fe.mp4?token=LBcJ5VfPkqqA9ZesRNVpiSV0rfi9NRNghYDfV_SEDPHIv9IYhXQwcJvDnx-L8dD9QgeLzZOUVrlC_ngh8BfgpRvSvxH0p0-ASc0gSaV1r3mMX_zCGNvY71KFTwCdj73SED9SSIlBPuqCFuTatnZ-BKdQWwg8SBLmV8psEBBartf01qS3P_bRY74YKNN3eWeCNAVgFa_iWnc3HNpI5Zldn7SFu-Zo_ahiRu5ijFPessIxjl_kioptn1dHm2LnZHsSrmhpQ5O_6naIrvH8i1r5wURWdn6gV776VWbWRTrhlT_Ay0Ljvk9wXkLJPeBHeY-1Fi0E6EMBLlMnDAUCX8s-IqqGaCKTxs6eqDtFnsg35mV7ww8qmdJ6lQrmMGrdsDHPQdzo-gIzDycGbhg-5xWjJPiOnxWhbiv8D4G9Q_lJP0uVHq_sAKHZgMwyR54cmhjjw51eU26poXXfSMnFS_gFcO3EaQAHK5kgGsoM6W23KOW_iiIMA4dkVJMdf2hSrXaa2YGi9DGDsN089hV7We19dLNzTg_OiMeM1voLvo0AwOmujDy2ZbBwlE8oSzq81CaglPAUWI0yuf2RkN8j0St6q-pZIJ6F1cTtiptCC6na7g-MbYGhYN0UfmbAi-VnWicWQ2ui9fqOzfmQ70ypyfGbiRHVa0oOh__xg0U3hBHcJ6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6879a05fe.mp4?token=LBcJ5VfPkqqA9ZesRNVpiSV0rfi9NRNghYDfV_SEDPHIv9IYhXQwcJvDnx-L8dD9QgeLzZOUVrlC_ngh8BfgpRvSvxH0p0-ASc0gSaV1r3mMX_zCGNvY71KFTwCdj73SED9SSIlBPuqCFuTatnZ-BKdQWwg8SBLmV8psEBBartf01qS3P_bRY74YKNN3eWeCNAVgFa_iWnc3HNpI5Zldn7SFu-Zo_ahiRu5ijFPessIxjl_kioptn1dHm2LnZHsSrmhpQ5O_6naIrvH8i1r5wURWdn6gV776VWbWRTrhlT_Ay0Ljvk9wXkLJPeBHeY-1Fi0E6EMBLlMnDAUCX8s-IqqGaCKTxs6eqDtFnsg35mV7ww8qmdJ6lQrmMGrdsDHPQdzo-gIzDycGbhg-5xWjJPiOnxWhbiv8D4G9Q_lJP0uVHq_sAKHZgMwyR54cmhjjw51eU26poXXfSMnFS_gFcO3EaQAHK5kgGsoM6W23KOW_iiIMA4dkVJMdf2hSrXaa2YGi9DGDsN089hV7We19dLNzTg_OiMeM1voLvo0AwOmujDy2ZbBwlE8oSzq81CaglPAUWI0yuf2RkN8j0St6q-pZIJ6F1cTtiptCC6na7g-MbYGhYN0UfmbAi-VnWicWQ2ui9fqOzfmQ70ypyfGbiRHVa0oOh__xg0U3hBHcJ6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معلم شهید ماکان نصیری: هر روز میام مدرسه؛ شاید خود ماکان بهم بگه کجاست…
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/692823" target="_blank">📅 08:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQp4ErBEoq6ScV0BozPoDL5xa8bPeRod4Jrw2-f_11Ke_gsPTUag1LEr4i8iLsWCbglGaBKLHD7iIcbOyLTUOq9hGZtZk5W3wIK82NYa3yT5JXYabIgnvH20YlJsONgjRedCLMWch0uNs-B_mHEJxVjj87BJhcEXAMmYgO4zNo4Vx-_QdlO3VJkXDpN6Ilsm17bZmUsIVck4tf-U9a3kedKMUel2PI50fIK_hU8npUHfqaosjErwRXEKVB02uH-oqWEk_spRzOYSQQDTuBZoxFSHl7UU-WkMXeIpRwR4ssAh-xrNAfoOvyLv1WR-pmo3Xlc6vRRZvbxTVQ1y1-SlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلمبیا به طور رسمی روابط دیپلماتیک خود را با ایران قطع کرد
🔹
کلمبیا در این بیانیه ایران را به آنچه «ارتباط با گروه‌های تروریستی بین‌المللی» خوانده شده متهم کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/692822" target="_blank">📅 08:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
قایقرانان تیم کایاک دو نفره ۵۰۰ متر مردان ایران و تیم تیراندازی میکس ایران در مادۀ تپانچۀ ۱۰ متر در رقابت بازی‌های آسیایی
مدال برنز کسب کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/692821" target="_blank">📅 08:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
آمریکا ۶ میلیون بشکه نفت ایران را دزدید  تانکرترکرز:
🔹
نزدیک به ۶ میلیون بشکه نفت خام ایران به ارزش ۶۰۰ میلیون دلار که پیش‌تر توقیف شده بود، به‌صورت بی‌سروصدا در حال عبور از اقیانوس اطلس به مقصد آمریکا است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/692820" target="_blank">📅 08:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_PAODUNar-AM3qpepI18WfYbo2Mgzh9dJAwILHU2uUuFyXmbG9FzkSQltQDHz5bv6Z0bjxZH35hultVHfulrTKxRHz3v0O-bihp45HrlhVqzvF5nrJ3Off-Xn2VMtbkM0feg32i8bl8KUaosNtUM8sZVsw4Jzdew_xC121IQvz9SnmM4pFFdTWaXwuexKQP2QFhJ1x0vsLAzzhF0fXgOvLqPE4vdLcAk51_4ieuqs-VHSau0iOYZUycRrVDelgUrI9v6vS2TErJ-hUY5LVxlTWclNfVqsiivw-MELhniQn78z36ofZ-hJL5He1q2mrnHK8EdsWUA5PqrSXr0Zvmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۳ مهر ماه
۱۳ ربیع‌الثانی ۱۴۴۸
۲۵ سپتامبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/692819" target="_blank">📅 08:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXF1_1IKzZrq3I-F1L3YZrfjLqS-RysJCnA8wLYDMpEgRZKQsK06bSqG-ddy-aoG287vknyq1vP4w2GJSllKduzV_eKiZfrnB5reodDnd7DH6llPoMwLFTrMpz7tW9-o-iFQLAvhVLiGz0uz4Y1g1itbcF2QMpmWNMYF2iC5dEg-IXNyjI1U3w05J4mUttCAF2Z8E2JkeUlwXdkRwcCLvvvXupLklXi1QHCKn0evKh47P8jXC0pNiwUIxdmBjRcp3Gsjyc3EbcL4ArboSwrTXfxS7yqkDs-GhUZ0EJD097txMrcmrepDy7QQ3VQSYAPMPhAbkTekoG8GWmDsnv9xiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پکیج جذاب استایل مردانه؛ کت چرم Artim + نیم‌بوت Rad
🔥
✔️
کت چرم مصنوعی با طراحی مدرن
✔️
فری‌سایز، مناسب سایزهای L و XL
✔️
نیم‌بوت مشکی با طراحی خاص
✔️
کفی پرسی و دوردوزی‌شده
✔️
سایز نیم‌بوت: ۴۱ تا ۴۴
🔴
قیمت 2,580,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/63697/180124/</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/692818" target="_blank">📅 05:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irusMr0OIT_oRf-ho34D41FfZyYo4sw4IVMXhRpnVbsC4wk_ZShEF61wI1Cs9981tgaw_tRPcrwYAPzaNFQJ4us7uowsiNxuQToAGU4K5ka0bgY6Nn2L-azA3U6g0nnNs4HvRgfD_mh8hXOEJl-P5Cib6O72l4f9L_iS37mVt4vQ70Pckw1V2FUiloCJyLQ0u0BVBmhgN1KPZ_83ZKiYQlIui7cccWavpdNK6PKEyAYgGrSvi2YTDgXQJyP6PtNEcFZE7HZQNHAD9dTb2gubzLZmRMDgo0lLy6jn-eMkoLJgEMS_Jbrq9s83P0MUwEa3Bjkz3sso0YLpXzDC-XVmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به وقت خانه تکانی!
🔹
انگار صندلی‌های خالی سازمان ملل امشب  خودش همه‌چیز را راجب منفور ترین کشور جهان گفته...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/692817" target="_blank">📅 05:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692816">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
می‌گویند ایران ابرقدرت نیست؛ اما قیمت بنزین آن‌طرف دنیا هم با اسم ایران بالا و پایین می‌شود...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/692816" target="_blank">📅 05:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1089c60204.mp4?token=E9UxgC__deNvgb0tUPxJ1RRfa9vjW7PyymZD_pr3CZQJon5zpEhogWPeHQZxtNNK5-k6Gj1CkE-a4B6bV_FsaGIa_FRqeaRHtaSMjMlqNq1qLtEg0VtZM3eW_R7PZG_vjTGUK8RxGfipfR2pOdZkL8KbK-nOnJ_CkbobRRjBJt0gMfnpgSZzeXSDVOYjY_45l3wusFE6QCio7nBJK3Imu3Ct1O2ubga_kF6-DQAGBRp76JA55spk3CJ7tabsJV3DqonJDUx2aCdsuGIqVcPDRTFKkGvMJ0mHjeFFd8sCcEtpI5XAEp_npzU-pqTFcj-qDuZffxzvd8OUxvxSDrXDGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1089c60204.mp4?token=E9UxgC__deNvgb0tUPxJ1RRfa9vjW7PyymZD_pr3CZQJon5zpEhogWPeHQZxtNNK5-k6Gj1CkE-a4B6bV_FsaGIa_FRqeaRHtaSMjMlqNq1qLtEg0VtZM3eW_R7PZG_vjTGUK8RxGfipfR2pOdZkL8KbK-nOnJ_CkbobRRjBJt0gMfnpgSZzeXSDVOYjY_45l3wusFE6QCio7nBJK3Imu3Ct1O2ubga_kF6-DQAGBRp76JA55spk3CJ7tabsJV3DqonJDUx2aCdsuGIqVcPDRTFKkGvMJ0mHjeFFd8sCcEtpI5XAEp_npzU-pqTFcj-qDuZffxzvd8OUxvxSDrXDGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واقعیت سخنرانی نتانیاهو در سازمان ملل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692814" target="_blank">📅 04:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYvBqMvnqI1g7vLtx-GmVd-GTc1ctiTJxWcjOgTos6mm-DZxD7ZNAOw4v4UdYOdg1LYR4NsD4IYyknNxAclO9MaqZ2z-L9kQtgfzKneA5acle0zuaJHtHi8ue3TJRz1ROrqJATNPVhcfY6y04ld7xxS0forAcMnXcwvzfoDC4WWSDYITbEStipbaQv_Xdm2QvYgp7HmMShbiyAjbRzfopbNQpPHDjRRUuZp7Z9jvlKzG0x_eDEt3F_sxVRIAsALg9A6UpBIPOso4a_0b78XrSwDVZGFyeGMz4leKD2Y_Pju8sVes_kkwTYrgO_e2LTpw-wdmh-UL6J4Yc7jyGM_ViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان با خبرنگاران رسانه‌های  آمریکایی رویترز، آکسیوس، فاکس نیوز، وال استریت ژورنال، نیویورک تایمز، سی ان ان، سی بی اس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692813" target="_blank">📅 04:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نخست‌وزیر ارمنستان در سازمان ملل: روابط با تهران برای ما بسیار مهم است و خواهان تعمیق روابط با ایران هستیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/692812" target="_blank">📅 04:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBOse8Pybtiu12ci7dhkr46DXbKmquqp5gbYNMXKfQAYdBJmEIuXTYEs9GrvkTmohB-ZBkH3l8q_S_nx3_1eNgUc1DTSdZoWxe1VTAweNSPn4fUAAAjH7NtRPWqiTHjD3B_7hrdo0a8NO0J3Qsd_ELcLpR0aqmMGGhYt3b1QOHeQazX4ERiFMC2DPHxCsYkUNZhn2U4MV6m7OA4hYUxvLaN3Xg5rA7ZczjaCtWEST0HkcBu7_HuYLi-AlTDXPZLO44hgYFrBPPjN58EW38OdZC52CNNS6JMiBxz1miNIgyIn0cASn4_bGw2KWahvJbEGUBkTqoexndIj8NHeff-Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: یک سال پیش، رئیس‌جمهور ترامپ کشورهای اروپایی را تهدید کرد که اگر خرید گازوئیل از آمریکا را افزایش ندهند، با تعرفه مواجه خواهند شد
🔹
حالا او به اروپا میگوید که عرضه گازوئیل را قطع خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692811" target="_blank">📅 04:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پزشکیان خطاب به مجری فاکس نیوز: سختی ها و مشکلات اقتصادی وجود دارد، اما ما مقاومت می‌کنیم و تا آخر خواهیم ماند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/692810" target="_blank">📅 04:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز:پس آیا ایران جنگ را انتخاب می‌کند یا توافق را؟   پزشکیان:
🔹
ما جنگ را انتخاب نمی‌کنیم. جنگ به ما تحمیل شد. ما به دنبال جنگ نیستیم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/692809" target="_blank">📅 04:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بیانیه کتائب حزب الله عراق در حمایت اقتصادی از ایران در برابر تحریم‌های آمریکا
🔹
زین پس از کالاهای ایرانی استفاده خواهیم کرد و مقابله با محاصره آمریکا علیه ایران را وظیفه شرعی خود می دانیم
🔹
روش سیاست‌مداران آمریکایی از زمان نابودی قبایل سرخ‌پوست و ملت‌هایشان و آه و نالهٔ کودکان عراق در دههٔ نود قرن گذشته بر اثر محاصرهٔ ظالمانه چندان دور نیست ، گاه از راه مسدود کردن دارایی‌ها و آنچه «تحریم اقتصادی» نامیده می‌شود، و گاه از راه خفه کردن فضا و بستن مرزها.
🔹
همان نهادها و شرکت‌هایی که تن به تسلیم و خواری در برابر تصمیم‌های ستمگرانهٔ آمریکا دادند ،  فراموش کردند مواضع ملت و رهبری خود را در محاصرهٔ دههٔ نود، و حمایت و یاری‌رسانی به دولت را هنگامی که داعش پیکر آن را می‌گزید و به تجاوز به ملت و مقدساتش نزدیک می‌شد.
🔹
و در پایان، به مراجع بزرگوار و علمای برجسته این پرسش را مطرح می‌کنیم: حکم شرعی کمک کردن به دشمنان به هر شکلی که باشد در محاصره و گرسنه نگه داشتن ملت مؤمن ایران چیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692808" target="_blank">📅 04:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC4G0CzqmHTryiCZ416sri1RjCNwk6t2aMe3p_IepWlbf4XwZo910ojZZPqULcSwdbatOruKwOQeRAEcwHTIz83G1yxqJb1LSS6VvSq4O9QFKdf_yNPxR7Kv3RnuWQPzUoax0gn_Shdzzh8znxTn4yw9i90q5cf8xKd2Kf5UQrTdBoZuS2K3rEBKuWZ2rucZMKrrz6GSlQQptG9ts2BEVij_uT8gRfs_QHeoTQPUljguxV9tahslrSBlMhuGJ7kkqCRbHp_iafAOC93UxE3hfOToHVxPr7LkUG4Cr_XKEtXTk2-MpkfWggq7Md6ronLc8iHDqSGZNm3kVW1vNq1jqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرعباس فخرآور ملقب به عباس جفرسون، از فعالین اپوزیسیون، با انتشار تصویر ساخته شده با هوش مصنوعی، مدعی دیدار محرمانه ترامپ و پزشکیان شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/692807" target="_blank">📅 04:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692806">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdaca992c0.mp4?token=Gdi0NJZI0AJndrFEBc0U9HTJAT-j8o5b3Jh0DLLp4QUpTadMqs6vz-rzMhI7NJr2eL9nnsNGae9lVJgxS6nZUBO9i20C2OPZcMV-tsjmAQhO_Qw4v662ffgy6hvfBp02Vvu3pFeblKb3aFLSnKEA3cBzutBu1FdUBXNLe84hfV0tU0OCERC_BWIWx-yJ4bbQy-ZNxpdGcFi-G-eRwES2KIUzuN4T6Mr_eGjL3eDnesKkcsU7ifuTTnnaLghJMW2HkpyplVWPckWcEiIW80Ywn_oVgRhIwpTs9teLhNunGyMFA9M4qwZfrYR2DEBNnjJiw_UPdnNXlqs6ORilh1pheQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdaca992c0.mp4?token=Gdi0NJZI0AJndrFEBc0U9HTJAT-j8o5b3Jh0DLLp4QUpTadMqs6vz-rzMhI7NJr2eL9nnsNGae9lVJgxS6nZUBO9i20C2OPZcMV-tsjmAQhO_Qw4v662ffgy6hvfBp02Vvu3pFeblKb3aFLSnKEA3cBzutBu1FdUBXNLe84hfV0tU0OCERC_BWIWx-yJ4bbQy-ZNxpdGcFi-G-eRwES2KIUzuN4T6Mr_eGjL3eDnesKkcsU7ifuTTnnaLghJMW2HkpyplVWPckWcEiIW80Ywn_oVgRhIwpTs9teLhNunGyMFA9M4qwZfrYR2DEBNnjJiw_UPdnNXlqs6ORilh1pheQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز:پس آیا ایران جنگ را انتخاب می‌کند یا توافق را؟
پزشکیان:
🔹
ما جنگ را انتخاب نمی‌کنیم. جنگ به ما تحمیل شد. ما به دنبال جنگ نیستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/692806" target="_blank">📅 04:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692805">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=HTpH3G1RTbuYOK5kV2n8ieX3HpTAV839QqMYmhlIeZcJOliB6tibHcSfnTqn3mU5hIZ7a4rXPEUS2lI4QK4E8ZtQ_lAnSpcpHckQgy5g0pPfa6WLovuP9ngARrlr_KVxbSp0wx8_rzXaTWs5mPY2w0qkQGl8UKYPUuia3JUU-Co0lwA5qSoWEClY7Ac4dc67dY2WXG2jq4bOg4FPpald5z8YRuAmghl6auK-SEty-_6I5Sqk1CDTEUAnbQVqQy9UQHdD_N-m9HkARBPOp54A85JwVALfuhYO7n5dLFzaojkxA1-12VQHktg6GlKqDnMF7gXYoILQ8p-ccTJAgm9dsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=HTpH3G1RTbuYOK5kV2n8ieX3HpTAV839QqMYmhlIeZcJOliB6tibHcSfnTqn3mU5hIZ7a4rXPEUS2lI4QK4E8ZtQ_lAnSpcpHckQgy5g0pPfa6WLovuP9ngARrlr_KVxbSp0wx8_rzXaTWs5mPY2w0qkQGl8UKYPUuia3JUU-Co0lwA5qSoWEClY7Ac4dc67dY2WXG2jq4bOg4FPpald5z8YRuAmghl6auK-SEty-_6I5Sqk1CDTEUAnbQVqQy9UQHdD_N-m9HkARBPOp54A85JwVALfuhYO7n5dLFzaojkxA1-12VQHktg6GlKqDnMF7gXYoILQ8p-ccTJAgm9dsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در پاسخ به سوال خبرنگار فاکس نیوز که ایران را متهم به حمایت مالی از کسانی که آمریکا آنان را نیروی نیابتی می داند:
🔹
یکی از مشکلاتی که با آن مواجه هستیم، مسدودبودن پول ما در چین است
🔹
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه رسد به اینکه بخواهیم از آن منابع برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/692805" target="_blank">📅 04:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692804">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پزشکیان: ما هرگز به مردم خودمان حمله نخواهیم کرد
مجری فاکس نیوز:
🔹
اما شما این کار را کردید.
پزشکیان:
🔹
نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدارس ما حمله کرد؟
مجری فاکس نیوز:
🔹
من متوجه هستم، اما در تاریخ‌ های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
پزشکیان:
🔹
آقای ترامپ خودش اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده است تا دولت ایران را سرنگون کنند.
🔹
افراد نتانیاهو اعلام کردند که نیروهایی از استان‌های کردستان و بلوچستان وارد مراکز اصلی شهرها خواهند شد تا دولت را سرنگون کنند.
🔹
آنها فکر می‌کردند که این یک ماجرا سه روزه خواهد بود و دولت سقوط خواهد کرد. اما دولت استوار ماند، منسجم‌تر شد و متحدتر شد.
🔹
حتی کسانی که در برابر دولت ایران ایستادند و به دلایل مختلف با ما مخالفت کردند، اکنون از ایران حمایت می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/692804" target="_blank">📅 04:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692803">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=VfE-Xcov4mJdSwQPeOyQDBRqp5vKxA4He4D0KlgW-e0gtru8t8ve_T3mhID1ZmoWDXO-MLVrxpr4s5JRTakgrhtZ7_6a1d5RoW6pNF2EEP1dxOB1QfNVosYqY8AzQVTXkz3a68_iZolfaaCIkjPuGfkV98bEzznRa-G4BqAoC5j9i5OrvP_Zo7eahE2ky7OraOIZG6K4UmydXHqB41rB-8tvNQmuD4xb1yvzJaXgShTPf4TSaloXY3b934BmkX8zlCt8wywHZQ_KkYfVg8HrfDEUNGNETCGTFQQf9pO6jLqc2xB2GXT6YUsv5BTozlxJ-TSiHOMfstDVYdmGdynQ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=VfE-Xcov4mJdSwQPeOyQDBRqp5vKxA4He4D0KlgW-e0gtru8t8ve_T3mhID1ZmoWDXO-MLVrxpr4s5JRTakgrhtZ7_6a1d5RoW6pNF2EEP1dxOB1QfNVosYqY8AzQVTXkz3a68_iZolfaaCIkjPuGfkV98bEzznRa-G4BqAoC5j9i5OrvP_Zo7eahE2ky7OraOIZG6K4UmydXHqB41rB-8tvNQmuD4xb1yvzJaXgShTPf4TSaloXY3b934BmkX8zlCt8wywHZQ_KkYfVg8HrfDEUNGNETCGTFQQf9pO6jLqc2xB2GXT6YUsv5BTozlxJ-TSiHOMfstDVYdmGdynQ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسعود پزشکیان: هر کسی که بخواهد اعتراض کند، کاملاً حق این کار را دارد
🔹
ما با بسیاری از این معترضان صحبت کردیم و با آن‌ها گفتگو کردیم. اما، استفاده از اعتراضات به عنوان ابزار، موضوعی کاملاً متفاوت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/692803" target="_blank">📅 04:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692802">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0973ebac78.mp4?token=lod0Mc4S4IWGXdlD-Wz3K27CEqOpUrbj_g_XenS1UFgRyR5lUP9mXi3IF2KGcUtg5voBWn9r4tHnwDkNfDYWAfjJwy9hDLRaXrDPKULBvmbF-dNYirg0FnlkB1jCjlmkwWBWUExm5cyn_6lpFm8lDezW1FEaY30_n5aAIwiuoIW9GeUY06YKS4ZZWMBLYUvuBTK3bXrmxC4ePvPQfB21Mk5SmKJMe1rDoPoSL9J8atJ9IPO-uCl36R5vVIw7tu2cxoB3JVgwJ9FlpMua2Y-ByJaF2oUI-IOvPioHosq1SUCta_oxMWzvNOBpP3WWE_zwy801pivW-axBAdoef_8E1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0973ebac78.mp4?token=lod0Mc4S4IWGXdlD-Wz3K27CEqOpUrbj_g_XenS1UFgRyR5lUP9mXi3IF2KGcUtg5voBWn9r4tHnwDkNfDYWAfjJwy9hDLRaXrDPKULBvmbF-dNYirg0FnlkB1jCjlmkwWBWUExm5cyn_6lpFm8lDezW1FEaY30_n5aAIwiuoIW9GeUY06YKS4ZZWMBLYUvuBTK3bXrmxC4ePvPQfB21Mk5SmKJMe1rDoPoSL9J8atJ9IPO-uCl36R5vVIw7tu2cxoB3JVgwJ9FlpMua2Y-ByJaF2oUI-IOvPioHosq1SUCta_oxMWzvNOBpP3WWE_zwy801pivW-axBAdoef_8E1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز: چرا ما هنوز ویدئویی از سخنرانی رهبر عالی‌قدر برای مردم ایران، در مورد این جنگ، یا حتی در مورد رئیس‌جمهور ترامپ ندیده‌ایم؟
پزشکیان:
🔹
خب، این یک فرآیندی است که در جامعه ما شکل گرفته است، و آن کمبود امنیت است که ناشی از اقدامات متجاوزان است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/692802" target="_blank">📅 04:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692801">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=ZS2tpFoSaEu9KVxNjMYhaxHILtyX-NqiIYt3w_cM96sQZV9l6WlMGtkNP-_gBnVP0uFNGHpxGB7LRsI_PL-CGZtUB18LrWIileX33woanmpEbC7l0V6NIwKlwDhQqN5E0dXk7UCWmWW0nt6gqJfAOuazIAABSyak1Cjp1QFOkgeTBZrK26Coy6-hcUkQdMDpu0N3qv2MEwe5cJsHGnJkXd8wz6S8DN6l5-gvCS7IriX_pbJ3vSOVUG-r5iYCdM-oTZ0v-m_2FL1_f-BVpOsl4dhvf8vwZdtCqQ7DP1zOlsGfsDd7Wpm-qovZm9WZ8CU9d02v-ZLtIJ7s8Q_j0sInLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=ZS2tpFoSaEu9KVxNjMYhaxHILtyX-NqiIYt3w_cM96sQZV9l6WlMGtkNP-_gBnVP0uFNGHpxGB7LRsI_PL-CGZtUB18LrWIileX33woanmpEbC7l0V6NIwKlwDhQqN5E0dXk7UCWmWW0nt6gqJfAOuazIAABSyak1Cjp1QFOkgeTBZrK26Coy6-hcUkQdMDpu0N3qv2MEwe5cJsHGnJkXd8wz6S8DN6l5-gvCS7IriX_pbJ3vSOVUG-r5iYCdM-oTZ0v-m_2FL1_f-BVpOsl4dhvf8vwZdtCqQ7DP1zOlsGfsDd7Wpm-qovZm9WZ8CU9d02v-ZLtIJ7s8Q_j0sInLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز: آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
🔹
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/692801" target="_blank">📅 04:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692800">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e602d4c4bf.mp4?token=QbyeQtMz5fk8AAoNnUEYZ9WeCz8KfzdnR9RWU1HIYTMtwnXYaEWMLx9KIsrI4a5ux9MHwLGLAsNFBVsShzXl_x94T_qMz0PX65gQLd7K05n-rMq5OWfiFAmx8ObCxXxUah9RPRMtifbTul-JG5vKPdBbKY5MyPGyCePDY2z0KJs8MZ0jfVdsf5Ifb_q2J5NvjjnqA68XXHijErXRBgx33sklm8PaxbiFqIikv1VvGi90I-XAepdJc5lgNfN2ooT1-ydqKChGzCJeHlFju-bnCYDcmNGMa8dSa-5T_RBkjJxyTUtFNJIhRHQM0U3Y5TL02tCCkQEllRr9GMOpfdgkHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e602d4c4bf.mp4?token=QbyeQtMz5fk8AAoNnUEYZ9WeCz8KfzdnR9RWU1HIYTMtwnXYaEWMLx9KIsrI4a5ux9MHwLGLAsNFBVsShzXl_x94T_qMz0PX65gQLd7K05n-rMq5OWfiFAmx8ObCxXxUah9RPRMtifbTul-JG5vKPdBbKY5MyPGyCePDY2z0KJs8MZ0jfVdsf5Ifb_q2J5NvjjnqA68XXHijErXRBgx33sklm8PaxbiFqIikv1VvGi90I-XAepdJc5lgNfN2ooT1-ydqKChGzCJeHlFju-bnCYDcmNGMa8dSa-5T_RBkjJxyTUtFNJIhRHQM0U3Y5TL02tCCkQEllRr9GMOpfdgkHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز:آقای رئیس‌جمهور، منظورم همان حادثه ژانویه است. شما جراح قلب هستید. نیروهای امنیتی ایران چند ایرانی را کشتند؟
پزشکیان:
🔹
ببینید چندان هم دشوار نیست. می‌توانید افرادی را به آنجا بفرستید تا حقیقت را مشخص و احراز کنند. آنچه فلان و بهمان نشریه در خارج از کشور گزارش می‌کند، با روایت دقیق و مستند از وقایع مطابقت ندارد. وقتی می‌گویند ۱۰ هزار نفر یا ۱۷ هزار نفر، چرا دست‌کم دو شماره ملی ارائه نمی‌کنند؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692800" target="_blank">📅 04:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb1368f28.mp4?token=eYkdD9iNJpa-SEmYO6H_853A1iq6Qj0Uzc1HQF9ukPXq9vP-DJjy60JQugSMZPDtHJvKw5pPylc5Ulsps3UBI0SirxfMfzsn9IpaDNHBBJ2UFM9ulSso2OfjDgKsy5UgkLRaNm1UFRgfiRjzfTNIjU_8BGu_D0zriCKpZSv3t_tiqYq1URzYhQQD5uvTmQ0STrdaPb_k2mX0Eu6gOglHbXoKIvZUft03QhD4XbXc1bVTlwYG2OHk3fTH0Rr2R4YU6snvvkFhQoQFaA-86QtzKz8XVZYIQ0qCzc_z8CGVbmCPLL1IFMUvA8oOB-qkNfczLNKd30221VwwfwsOOrjfrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb1368f28.mp4?token=eYkdD9iNJpa-SEmYO6H_853A1iq6Qj0Uzc1HQF9ukPXq9vP-DJjy60JQugSMZPDtHJvKw5pPylc5Ulsps3UBI0SirxfMfzsn9IpaDNHBBJ2UFM9ulSso2OfjDgKsy5UgkLRaNm1UFRgfiRjzfTNIjU_8BGu_D0zriCKpZSv3t_tiqYq1URzYhQQD5uvTmQ0STrdaPb_k2mX0Eu6gOglHbXoKIvZUft03QhD4XbXc1bVTlwYG2OHk3fTH0Rr2R4YU6snvvkFhQoQFaA-86QtzKz8XVZYIQ0qCzc_z8CGVbmCPLL1IFMUvA8oOB-qkNfczLNKd30221VwwfwsOOrjfrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان به فاکس نیوز: رهبر ایران در سلامت کامل است و من یک جلسه ۷ ساعته با ایشان داشتم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/692799" target="_blank">📅 04:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/692798" target="_blank">📅 04:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bca2a5e28.mp4?token=Fg2-45rCSo2xxkgdJXA-UIME4ILjq0iBEt_xsAZTG7-ssrD6nhoo3aXQUYYHmjD5TmdEAJeF5Pr2peDEMxo2CBZtenEBaQe6J5U9MVW7JHttagVMgJDn6C-BqHFiSzxz_2FnGAsABkJxRimqw72xocDnpcm07vUU3-_mUZmjhA6UWCwxHXYdFUl45o1TnRCZL-HGiqBsdgsIsX8PFxCQNf6wdZD1gKkDRubZAYOdgtUjK8cyeh-ZUdkYCIlNEBFIKB7bYOX844euwH-4jLtAU-jbzU0TChbODOGK8L8PVi__kM2vZ_wPp4pC-pMq48kqSmavFTHqkY1pzIjBCBdCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bca2a5e28.mp4?token=Fg2-45rCSo2xxkgdJXA-UIME4ILjq0iBEt_xsAZTG7-ssrD6nhoo3aXQUYYHmjD5TmdEAJeF5Pr2peDEMxo2CBZtenEBaQe6J5U9MVW7JHttagVMgJDn6C-BqHFiSzxz_2FnGAsABkJxRimqw72xocDnpcm07vUU3-_mUZmjhA6UWCwxHXYdFUl45o1TnRCZL-HGiqBsdgsIsX8PFxCQNf6wdZD1gKkDRubZAYOdgtUjK8cyeh-ZUdkYCIlNEBFIKB7bYOX844euwH-4jLtAU-jbzU0TChbODOGK8L8PVi__kM2vZ_wPp4pC-pMq48kqSmavFTHqkY1pzIjBCBdCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساکت و مبهوت ماندن سفیر دائمی اسرائیل در سازمان ملل حین عبور پزشکیان از جلوی او
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/692797" target="_blank">📅 04:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRXlMSwyxCizX3lS9pgW8GcGqbGyWHsxEdxdD1IERvPZl5n-BXlTg1ZFTYtkTNuJzmwNIfvGT5gqUHgCS64VSJC0PZZIgeb151WTGXKl79Ar3H1hdyIX6OXuRdsJK_T3QMZkQ5YqUT_F-jK4dc9jyLS35amHXKwxQXsbgT6p_Au5X_MSMOo2cABQ70120XSUMSitI2x3Qfx13GQzgUESavY5UuRIYjXRZS3w6rhvC9MkqRWzeIk7s6ENq8feg85LrvQLEFxcniJGYhulXCvIBvNqshE_mlUsezzRLcfvlFKv3JoVWjJo0UdrFruTmydnzUKmxSxLhIsQYwLEnJEitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پکیج جذاب استایل مردانه؛ کت چرم Artim + نیم‌بوت Rad
🔥
✔️
کت چرم مصنوعی با طراحی مدرن
✔️
فری‌سایز، مناسب سایزهای L و XL
✔️
نیم‌بوت مشکی با طراحی خاص
✔️
کفی پرسی و دوردوزی‌شده
✔️
سایز نیم‌بوت: ۴۱ تا ۴۴
🔴
قیمت 2,580,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/63697/180124/</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/692796" target="_blank">📅 00:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔹
از خبرهای جذاب امروز جانمانید
🔹
🔹
هیات ایرانی نمی‌تواند از نیویورک به تهران برگردد؟
👇
khabarfoori.com/fa/tiny/news-3247541
🔹
نقشه پروازهای ایران تغییر کرد | کدام کشورها پروازهای ایران را بستند؟ | احتمال اقدام متقابل تهران
👇
khabarfoori.com/fa/tiny/news-3247657
🔹
هشدار: قیمت سکه به این عدد می‌رسد | نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3247593
🔹
تولید سریع، مزیت تازه برای رقابت در بازار جهانی
👇
khabarfoori.com/fa/tiny/news-3247497
🔹
همسر دوم بهاره رهنما ناگهان سکوتش را شکست
👇
khabarfoori.com/fa/tiny/news-3247553
🔹
صفحه اخبار منتخب خبرفوری را اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/692795" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ولیعهد کویت: ایران از تنگۀ هرمز به‌عنوان برگ برنده در جنگ استفاده می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/692794" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876e946901.mp4?token=a2pksIn04Y8OzLr4Htuq2VO2RudWD1q-5laX8ibdl7WIG7SaFSS9gOdj78OgR9cBcEOj5kd-pX3iP6BMC9OJiwng4jJjxddDlAL-Oo13Y1Idwz2ohNlNsnIjLQ8i7Y9bus6HSe3t7DGDB9Ln-fS301bWRXaAaqGbjkWtmkeCnfyQAMYtOS_-TEQrUFcvQ-1NuZvsAkkhZ2g4YOP-zR_HghyoGirYyghGcmDlWQFLwxLFhdIAhle2Y-hNY0QmSVDuzQjKhRj-XnpXo8_mMe6MjyFsWOLCvpf121pn1a-n8Xaz7nKmJNvGfWzoE9XtJBhF-JIhh1KW8TyfT90ROGIQHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876e946901.mp4?token=a2pksIn04Y8OzLr4Htuq2VO2RudWD1q-5laX8ibdl7WIG7SaFSS9gOdj78OgR9cBcEOj5kd-pX3iP6BMC9OJiwng4jJjxddDlAL-Oo13Y1Idwz2ohNlNsnIjLQ8i7Y9bus6HSe3t7DGDB9Ln-fS301bWRXaAaqGbjkWtmkeCnfyQAMYtOS_-TEQrUFcvQ-1NuZvsAkkhZ2g4YOP-zR_HghyoGirYyghGcmDlWQFLwxLFhdIAhle2Y-hNY0QmSVDuzQjKhRj-XnpXo8_mMe6MjyFsWOLCvpf121pn1a-n8Xaz7nKmJNvGfWzoE9XtJBhF-JIhh1KW8TyfT90ROGIQHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون، مجری و تحلیلگر آمریکایی: قطری‌ها به ترامپ یک هواپیما دادند. و این کار چه سودی برایشان داشت؟ هیچ سودی نداشت
🔹
ایالات متحده از قطر دفاع نکرد؛ بلکه سامانه‌های دفاعی «تاد»(THAAD) را از منطقه خلیج فارس به اسرائیل منتقل کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/692793" target="_blank">📅 00:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LawMoiIXkFpb74kJfOQgFN0FZJksXXRdagzF2IWw9rjh5MdcBe-p9Nu-VDcTfD21hmSk_sz6BzRm52U1JE_lVx4b4WeDBtyk_9kG5Kbfcr0wVYTLL5AmdEUD9IbL8sOb3-ec4ESS8ebFmECi5jn7KYCqnN_x5Vpp9yrjDukH0Xp-u9rvrbeILTYC0AU2f1NAz9iJ1cHgnX-Mn20ykAwce4zfKfArpJm992W_PxUig1M7WLSmJWiYsvw_1jRWymP08x0ZoD7tv9UKWFtdeMwQ67pLwsIdKO5LlmROwIuRTAsYmSS0E07Ek_nq0MxYp-1aCux0l1jCiPlmsLyq2KtFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اسرائیلی: تبریک! ما یک دیکتاتور پست و مضحک روی صحنه‌ سازمان ملل داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/692792" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692791">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: تحرکات فشرده‌ای برای دستیابی به سازوکاری جهت توقف هرچه سریع‌تر درگیری‌ها و بازگشایی تنگه هرمز در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/692791" target="_blank">📅 00:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692790">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام کاخ سفید: ترامپ همچنان برای گفتگو با ایران آماده است اما نیازی مبرم به مذاکره ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/692790" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692789">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رویترز: عربستان جریان انتقال نفت خام از طریق خط لوله شرق-غرب را افزایش داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/692789" target="_blank">📅 00:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692788">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e20b2386.mp4?token=A5xtmEhy5iuE_1uf3y3XJ5KHvArWA3AJ0bEYk8qAjpr8GvAb7FHvo7ejBKY7T0DcS24Kb-Z44iCiCZ08cBPk56MLL3wZiaKZOuEOO5FJl5dguxlfOAh657wr1fD0PlAfEIkllRMNesqqUO_nydLBA9Hwqiv6IhWVFEV1wW_sgL9anEn8el_X_Z1RCj_xChdtttET8anZQkfVnUEwOvub1kvNzwf8Ki3-vDdbAk-ka_MtngAp_-eE3NJnbVkivRUxpvduX6sEKvaN4q3un0709ojRZgV31pt4sCghwmglvZ7Pjjg5Lz5oD6cxXYzZvKxlohVmxKbdkl-PYjtdYvOq3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e20b2386.mp4?token=A5xtmEhy5iuE_1uf3y3XJ5KHvArWA3AJ0bEYk8qAjpr8GvAb7FHvo7ejBKY7T0DcS24Kb-Z44iCiCZ08cBPk56MLL3wZiaKZOuEOO5FJl5dguxlfOAh657wr1fD0PlAfEIkllRMNesqqUO_nydLBA9Hwqiv6IhWVFEV1wW_sgL9anEn8el_X_Z1RCj_xChdtttET8anZQkfVnUEwOvub1kvNzwf8Ki3-vDdbAk-ka_MtngAp_-eE3NJnbVkivRUxpvduX6sEKvaN4q3un0709ojRZgV31pt4sCghwmglvZ7Pjjg5Lz5oD6cxXYzZvKxlohVmxKbdkl-PYjtdYvOq3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت اساسی رمزارز با پول ملی در چیست؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/692788" target="_blank">📅 00:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692787">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkC44mRkt71n2jFvuMjHa7o93LlERBOi2gtO-2XYUvTjrLx7HTfxqp2WmhHxAmAvFCwXHbsgOQp6UbiuQaGxJ6A3b41aTlD7XrhpXYgmOdn9LPsumyq8oj0bfnffBPpdwP5cri4mFzPkhdfnoTge_doSykBw4dkVSvmqT80CTDu3Hom-0wsFmTui8ZUkrZrdQ3aLT8Sjmp00aG002n46MeixljFSTsAdUHfujbITAfkhHp24yoEskPJBd7xr5JG8rLk9qsYWOeJwtd2PkWSDcNzSkN-qcAYlKEqERR2r6Nooj94MHj2PSTnVsH1pYftzSUgIzN859LfkOkocFrxLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آمریکا، قانون خنده‌دار است
🔹
اگر علیه رئیس‌جمهور آمریکا شعار دهید (مجاز است)
🔹
اگر علیه هر مقام اسرائیلی شعار دهید (دستگیر می‌شوید)
🔹
اگر پرچم آمریکا را بسوزانید (آزادی بیان)
🔹
اگر پرچم اسرائیل را بسوزانید (قانون مجازات می‌کند)
🔹
در نهایت شما می‌توانید هر مسیحی آمریکایی را توهین کنید، اما اگر یک یهودی اسرائیلی را توهین کنید، مشمول قانون ضدسامی‌گری در آمریکا خواهید شد. این شوخی نیست، بلکه یک واقعیت است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/692787" target="_blank">📅 00:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692786">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ab0c03cb.mp4?token=Bu0PWd5PjckplKHqi6ESRKU-Qjw7Z9IQhDSb92dysto8ZcMiutglnGrXbsOzpxeRZN76ITlQx_bRBg77_43TqC4FdrPgOB0E09O-DJgp7uZ6UZr0irAdyhBgoaBGQ6f2BwNQkq_HYKZ0RqzOBsyWZ4b1gWGZJZqntHnwfVGX0fWpUqWQROu683a1qTML8nCtT7BJp77baACu7xwgNtijU38a-pdwcm3ARhYOSo3pJ3dTDPej2c246yLoADXrN7nWXMVsX2ltpCJM8FfYfJZrEV7FPI_mmjJyM7K7IJ2qnOg_P0CkcUhQg90oeLnhUW3aaQ37OjoO2m6AwPmVO4lksw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ab0c03cb.mp4?token=Bu0PWd5PjckplKHqi6ESRKU-Qjw7Z9IQhDSb92dysto8ZcMiutglnGrXbsOzpxeRZN76ITlQx_bRBg77_43TqC4FdrPgOB0E09O-DJgp7uZ6UZr0irAdyhBgoaBGQ6f2BwNQkq_HYKZ0RqzOBsyWZ4b1gWGZJZqntHnwfVGX0fWpUqWQROu683a1qTML8nCtT7BJp77baACu7xwgNtijU38a-pdwcm3ARhYOSo3pJ3dTDPej2c246yLoADXrN7nWXMVsX2ltpCJM8FfYfJZrEV7FPI_mmjJyM7K7IJ2qnOg_P0CkcUhQg90oeLnhUW3aaQ37OjoO2m6AwPmVO4lksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشین لگویی تمسخر سخنرانی نتانیاهو در مجمع سازمان ملل توسط رسانه‌های جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692786" target="_blank">📅 00:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692785">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IshCtEdFNe8qlx9FRRxleXT_h4JTwFfxx7ucHN1xOKT5-PrRvld86cmrzQpVm1d2ZR27RBRX52o_2boorilA4VRx4neHyJnXrBQfSnNbu0fR6GcqIEYaWC6AuGMNnNl4s623pjyioQAyCkuwGNtTEqZIVdC6HteJFd6Nd0KbP50a3SxTwHVff0KSuj-dFfAOaSg3hjYRWZH8YMHMGIjJp5HEVAnj1QnE3LLUg3PBwdBvVrOrFIhReEmqArxX4mJlfYaOaxyjJtaJnHQPCAuIGGY0vAimJH5lx1iyJU3m-g6Ff1p8IHoT4UBufQ_yggIEy6LiP8TlM4UlNmzUFOMI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692785" target="_blank">📅 00:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692784">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOjU9kaH23ZHAn5Kbuad25R80HIMS6kPd6TKWgV6hGjqJV84R4FSPT-ThgfZq8Vu8OhcDdZtPOkD9G-EJwRDQI8rjv4OzeLOc7KSA8bs4DnA5xL0FBsaz7uCPbP1Od-pyM3TaYr_NpnydDRb7r7GWr3NjhS_Iw3y9CqWtBnji3a5lW66SvWvDwpC1jSzRLvMy6MH6BiuFpRfVZzlbOhxxfKAeyNp2wl1Qi28ABSy4DGMz5sC7tuggx8rdAHh020wYUSPRkiZ0EcEq944mgOlCNHeyCWcFE68QYiSXK_It6-xxMLndIt_gnJi9ONV2Ow4x4TCXUVGzSEPJv9nVZGACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: فاحشه خودپسند و کثیف جنایتکار جنگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/692784" target="_blank">📅 00:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692783">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
معاون امور زنان رئیس جمهور: پیگیر وصل شدن کالابرگ و یارانهٔ زنانی که به تنهایی مسئولیت فرزندان را برعهده دارند، هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/692783" target="_blank">📅 23:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692782">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نتانیاهو علیه شهردار نیویورک: از زمانی که به عنوان شهردار این شهر انتخاب شدید، بسیاری از یهودیان دیگر در نیویورک احساس امنیت نمی‌کنند
🔹
همسرتان پستی را لایک کرد که عملیات ۷ اکتبر را می‌ستود. او پست دیگری را لایک کرد که می‌گفت تل‌آویو نباید وجود داشته باشد.…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/692782" target="_blank">📅 23:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692781">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed-6l0Px291_hTQjipC-ejNFN8J0PIdz5NG8enHlgJy9E5bHxmO_jVF5HyGepAJF1eLZ9xysvaFXUb4pDgiZWV-YMHD0DehObKkxuEgNR1_pZgIRDJZ--At9vJHcHROwxsKkPLuNvXXAuMgYxuyv9yE5i5BhjZ8MrP1ACM5IYiIwTGIl11odlaRDjlA5TSRVcMzWS8GyjVReLIY6nMC3yaocSoSakM06Wf9Jc2YvuHFJZBB71Z-oH4fcNj66cIJ6Hk2czuvX_yZ7XRtKHrufK3bulQ0KLtTfj-OM6ACND0T4opgZvRVQxP5hDnw7ND9Pxe-OrPaAlo76ybjUWvCWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوزان ساراندون، برنده جایزه اسکار، در جریان اعتراضات ضداسرائیلی در نیویورک بازداشت شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/692781" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692780">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io4ya4tlCLFcQVUOz5fz6s3uOfyZT4GPTua0UJm4eGPGlcKbtNnypE1dOjDrqozMTteotjvXwWn4bwIVa7MobBa8DTz0N7GNAlBuAumAGtALPCu8oKeHm78oM8NwDJ8QpXAm99lNrkwiJ04vvrJF1i4axBy1d5TD7Gx8V90_tShfBAwFs7ZVInRcU0iqKyIrhJGhTBqX49OGFaRMmyMORkTnsZSmKQSPqOBPtHB1UHI7Cq4SJl-o7JeiSdH__QCtnT39G_bFVsV0OtE3HhPi1-6peHMpFLGC2z608ZIAuq7bFUBkPgMmcIsP2aKjLkXtlB3oLe0uubHAHdIQa7poQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ایکس گلوبال به روبیو: «تنها دلیلی که ما در حال جنگ با ایران هستیم، این است که اسرائیل ما را مجبور به این کار کرده است»
🔹
شگفت‌انگیز. وقت آن رسیده که روابط با اسرائیل را قطع کنیم و با آن‌ها به عنوان تروریست‌های تشنه‌خون و انگلی برخورد کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/692780" target="_blank">📅 23:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692779">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7616c58484.mp4?token=iwyf7X4iOR96TY9_r208eoB83YgPEtvwC-oa5rNWPaS4sg8YDLpPCFOee-yF26sypAkPU_6GoHKxmHXXLfduQM7cAwjS9ROVtSpJLwcz73-Zraw1cmTnEOi1Gm6rq1pXqZ5-RvnSTWzPrgVK-Tob8dFw7swcq6h31pmXJC8OZA6nocsmMT2gIJy1pq_bL5VEzPeZDNhA4kFr5AiofKVivWzYXncp5HBLem01roymBdbyzlsrFKo1EtQjxmJaLkcReMkisT__o25UfW4NhgvCiu3fQYCNC7BksKzCCiSp_ykIkBtB51cAdO7E6Z3ogtyliTFN4H0T0XR5K-EyEuDl6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7616c58484.mp4?token=iwyf7X4iOR96TY9_r208eoB83YgPEtvwC-oa5rNWPaS4sg8YDLpPCFOee-yF26sypAkPU_6GoHKxmHXXLfduQM7cAwjS9ROVtSpJLwcz73-Zraw1cmTnEOi1Gm6rq1pXqZ5-RvnSTWzPrgVK-Tob8dFw7swcq6h31pmXJC8OZA6nocsmMT2gIJy1pq_bL5VEzPeZDNhA4kFr5AiofKVivWzYXncp5HBLem01roymBdbyzlsrFKo1EtQjxmJaLkcReMkisT__o25UfW4NhgvCiu3fQYCNC7BksKzCCiSp_ykIkBtB51cAdO7E6Z3ogtyliTFN4H0T0XR5K-EyEuDl6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غذاهای عجیب چین که آنها را خشک می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/692779" target="_blank">📅 23:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692778">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=OXo6rEY1k3p0irEf0sUvYy8fTiYkSBLucGTNydtACf3KYGtzBvGHXaZpFKZaI49OeXc0EhaPobRRd1OSmNebUk9qWYdde1JFi-BYH6UgynIqYU3EHYJaSKHk8nZrx9PHcdpPZZSX1rciEodS76LUXbvE0d4-MVgpGI3Bf7MLJzZ9NFWZnBf1bC9hSn5FmIEnZyVz3h0h3GL4WHN-sh_tSUHv7bOaZ5BpU_fW1-FBs9MSorBwgPueqZOtoAEcDadE3Z2hHh1vqAnKsbd2jmX7J86fL1jcxbxROv-wuuKzOdOAcmuBgyDzF3yzdtZwRAMjWuMEoGYbiWj2UpOI4StfzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=OXo6rEY1k3p0irEf0sUvYy8fTiYkSBLucGTNydtACf3KYGtzBvGHXaZpFKZaI49OeXc0EhaPobRRd1OSmNebUk9qWYdde1JFi-BYH6UgynIqYU3EHYJaSKHk8nZrx9PHcdpPZZSX1rciEodS76LUXbvE0d4-MVgpGI3Bf7MLJzZ9NFWZnBf1bC9hSn5FmIEnZyVz3h0h3GL4WHN-sh_tSUHv7bOaZ5BpU_fW1-FBs9MSorBwgPueqZOtoAEcDadE3Z2hHh1vqAnKsbd2jmX7J86fL1jcxbxROv-wuuKzOdOAcmuBgyDzF3yzdtZwRAMjWuMEoGYbiWj2UpOI4StfzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
جارو شارژی خودرو با مکش ۴۵۰۰Pa
🔥
این جارو رو می‌خوای؟ قسطی هم می‌تونی بخری!
سبک، کم‌حجم و شارژی با ۲۰–۲۵ دقیقه کارکرد!
⚡️
اندازه جعبه : 16*16*6 سانتی متر
مکش نیرو:۴۰۰۰ - ۴۵۰۰Pa
ویژگی های خاص:قابلیت استفاده به صورت خشک در خانه و ظرفیت باتری ۲۰۰۰ میلی آمپری
🔥
قیمت ویژه امروز: 1,389,000 تومان
🏠
پرداخت درب منزل
✅
امکان پرداخت قسطی با ترب پی
🛒
خرید
👇
memarket24.ir/product/brief/26903/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/692778" target="_blank">📅 23:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692777">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8efda3679.mp4?token=sMscHIDmOk__sEiEbu6uw8Sd97mOYyXst9vMaHEEcadj5aHwFsLw8Z2wz49-agUoTBTrIiM9ipTKWtUzQIkMbXytQhIaSV-yXSjPf9TCallcKTGxfGMGW01CzaUewU8iadBFsRcdr3cj-PXM5CW1jQQg-VmGxS_1QBxOgx2LdQBXtG3gdZM9_QHnStr0DOtxj5bMomPglPQQ_Hly0Pwob9_73us2tovMno-ldtB9-ItLB9wATsmAPdr8BPDgtknRXwN_BZE3h0EsldI4reMo7YSJp6upW6e96h0Sq1LUTc3MvxbUNUHWWBxpwuaQFuG7QOqqmzb6PAW6cEsxjpnvSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8efda3679.mp4?token=sMscHIDmOk__sEiEbu6uw8Sd97mOYyXst9vMaHEEcadj5aHwFsLw8Z2wz49-agUoTBTrIiM9ipTKWtUzQIkMbXytQhIaSV-yXSjPf9TCallcKTGxfGMGW01CzaUewU8iadBFsRcdr3cj-PXM5CW1jQQg-VmGxS_1QBxOgx2LdQBXtG3gdZM9_QHnStr0DOtxj5bMomPglPQQ_Hly0Pwob9_73us2tovMno-ldtB9-ItLB9wATsmAPdr8BPDgtknRXwN_BZE3h0EsldI4reMo7YSJp6upW6e96h0Sq1LUTc3MvxbUNUHWWBxpwuaQFuG7QOqqmzb6PAW6cEsxjpnvSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی متفاوت از اطراف برج ایفل که شبیه یک جمعه‌بازار شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/692777" target="_blank">📅 23:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAQkR2z80212kK1RwmRw6Uw6M-50-_5JJ0UwobPueKU5P76Qx1P0O-hwU7aPfitZJLsFeJxZO5LgbcpCGbDyan3BdpEzCvRwHUQYzba9uo0yF6miWWk43P-ZYqbsl7p5YWj6Wa-IYbH3wzIvb3GdwhLuK2eVkELWZzZC_EPc2ARUjboPBGb_-XYMvjH6nD2uBY0z_tIuxVU4XQbO5G4dd1S6phkvYy7vkPttZzrUn2BQ0D8x1_MVd_WCheSL2U9BZRG58uTHa_J75HUoFSA2Gk1PRgBjoHlAuMzkV25rw2Q27iV8HzA5I5UQnVxt-wVhLrl10_B1YDCkf0WKid254Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKolCrodTXJMxQWvwyLqieMxVbVLliXfofSzy6jedp6D7dcXVVUnMeeInF9qGHAhtyAWoLBjGbYWGBNqaE6AClkLVu7bYq81MHbG4y47KuImcaj3U8NPNvTdsdxYEcL4MSTCTXilSfFMGwYPCmm_zrxDbGLOH6gOW_5hBMeP2lpzT7oFRXfSAXz-L6i7SYl0AKM9sJWm9je-supxw72cSMFv5cKz2sSC5VNkPTN4QATrhwWb1zta0tmB7lkojGb9oGrOyES5la_iJL0Sc8CULDaJFk5XHn9kyUARjIW2veoV3SEOJVsOx2QKTLU7SUipnsV7l0Db_r9a9KkMhG3qow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DamIdtjili89x683N_3do_F6RK3iD7X6PrXpajKk0ijosP1Jha18EVWXHVZSW21lH26jNno9n-YIgUBThLMLi0wLJmScaa5nNRgchfMKyUjbmj8jRPundEsvnlbtoHa19oDUb11aJHeSxolhTBdCWqH-ve8XS5Mv9wAnwvQU2adQ_yicNw5VcIZCxFPXeU1beZrxTqhI7I0UsqLQOPFSn6cTIKT8Gy83ReifN1DbXTAbqxyH9Uu4Rc0_IkIsKcXw52Zgcu9c8SmkZDB94zbwRDhFiocYgmcworPoNxgVc5Awj5fwxcAA71ru9M7_5Oewi_vjwEmdnGS9y9B4E0b5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6RutdsdV4W2m_lGzi9pAZM13cw4fUACAOceDSdWGt5oBCorzHa0n7IW32VN59zSwh5ow3Sz64iEurTjvgTsn7JVwY-4WS2J_cI12vrHKzkjJy3eTuhKOpH_cdXLx_p2BEj-gJMjnk-6SJYlCW_RRl-FUVzhmbKsM32Z3cB1pDKyKL-muXKwIVEcbHyjkgwu5Db6B5K0d4muCp9ecVJ6PMtzM3LwyxStlXthECTGgKzLE9DEh9by-vtL9W0tRShFR7txYEXQKAwO2FSVfb05IpM3EP_g0pgsbISEi1MOg4H6wK189xw1lucpc--ftWnW4aJZ0FbGZESHlJ8m-uzSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sv4mWdMMA4KZWI6Rq2LnqtnHxGeJLwLY-40sbaDaQpwBRii1rFzMPiK1t8LxrK4xvYwFbjGzjEZWombSqDAiz5q-0sq6HWhZGFJN1hrXhwEpnOoc3yZf3rIkEEcda5u_RRecE5EhK2UpQ38ek2pkH8qsbwMjvuINub7WQ8Eup9CiIlG4cvi533rgznuo0m8xq3CmM-Gl7v4KkpdP3h1w5dP9opuhcZzatsRyS0TEw8zA5jsS7aJxapgRVC_LShNRwoF5dNH34IyabPemZgVOMymgobpUQbqBVn6OUQX84V9ipPo5Sa8mGnvW0nRTik3oR__qOECKmsNnnOKzEMwx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VY4lZsGAfh07Dx3XyRy_c0eDj5VFAkyZgp7QhGfHY1OIzm0YbLuuV8ZXDNyxgFIXmJkywqjUxcfIRCsUU0V80yvMOJlDk_To_2pPnKUSTdbBOb7V2iwbnsSMWYAF7F9zGR3JkBYH9ftFsF91JL03-li5o4giRlrMvl-GBCE5JA0cOT3KWIy9kPQaeWuEY8R6M9QLvgYyxz-tDkiMxLxtCri_yM55gMfMrnaDX79l0HpMKC9qs_Iqujix0hNd9En0uS-6quTmIqFAmyar8rg_ytHG64YdwJM8-a5HiTnljgQiRR7RVcG2e6eeo6dpJppHeW5VPInyC08tB6BrO1I_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUlkeVUfDiKaePmFuv7WC1YcAiVOJ-3m6aznPWhwUbjhxD0CVU21KQnkCSxWl9tyf-quYC6nTt_ADF0n2Njjb_quy79UdmClbapOg6LNOP9UaHZNNsOnYgyA2-89h3LBmkHsd6quNzMhHH9HjGB21HnJZKxuUfNi0ZuEgyNpda4dyqBw6NhXKUyFvA91Fkwr7oXe9Hwy2PXUKuMC9AY3my0t81Q_aLsIm96t6ZX97Bd7gEIOjoGS7014lSl5iVm6x-rHRTkPgN7PZwg52SaTbMmnUj3YC5L23Y54pEB_8eJUrnYwmMtM6X63QLFm0TSzOiOybtG79FeOFshYryAP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTfB0IcLX6XfjACUT5jtsGipoOD6gdTYycRdAxyrb7UF0y8iyrqj01MzdO7p2gWqN7c9CvyYBq9-DcRgHBb5farMSSZbjI0c_9l3FD3QopXA-pEfXbumP7bOSKQD0IWFIxQ-og5xV9VuEPHMATU64xkXh5BXztUEixa7RpZZhcOnTpRWWQFiZ2BJDIZ5i6N8LBLdn77D6-a-ur0l5H-WhEzjlyg3fUGWywCh-vxtO1LFrKXL8Ds8PBZOVfqPvrTIgE2NsEhvJy5wLBuFK1PgzS1xX99St--PzRa2WsKXWdYj87G-j2244ngpOGXbOdZ46qknFvN3PiojbCcLtqJiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4lBfJqRlgPKLLwhIYrCo_yaNPnNSIJjX0GDK7oy8PZa5tWc9l5xSCqS9051urOslSNLNTf8R4CS4I_3a3LlzIdyFu9N9X0Y1exB6n1Qe2HAGNegya6sI6khacJkSzKgy0X0oI7w-1eJZE8qKDL6hlCTXW6immPaob_wQ797ep1Z839pSR05SEbNmklZEtO0v76pwkhfY4oFp78SM5fN8I7zm5Qwl7pkFR5qfTYE0uWIpneXHK2S4sa0z2YlZdme1QKWkX8QYALXtbXBrQnPqW3GfuRA5rpuLzfX9WWi9q0JtkfgQbuPaR_8JOii6bdeTaNLJOmIIVoFBJIeTNvBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQWmJIBNvAbL5jvRPQoEHvT359cbjd9zK9DB0WUfAbCYc0ntC5wZpyjlcig-bfEFxVRIRZ4TOw-jxk1dB_3-Svtcy4mpB0qChAnQwL1H9IAmt0hapCc_HkjcB8XnNiZfM5FCVZuruR2R5ImpcmQc52WoPM2e9pE60898V9a5cPQ-rqcSBx0DuN5OmUMe_36kG00MkD14vwrd02TY-TwmjK5ip7F_T6KhXpUoEaVRjrX9ugwbxMm7v3fxRalkTzTkdqh4hEdee6Ik3h9IL3lpF9XGmEivvzBD5_X6O_kQW37HbIuqdLBkKxcbVpzmA28_mMigl6pYOgoJjx-oiC6Fgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و چالش‌های  تأمین داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/692765" target="_blank">📅 23:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
در این کلیپ توضیح داده شده که چطور کوچک‌ترین انتخاب‌های ما می‌تواند در عزت نفس و سطح استانداردهایمان تأثیرگذار باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/692764" target="_blank">📅 23:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692762">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
بلومبرگ: فرانسه برای حفاظت از پالایشگاه نفت عربستان سعودی، کمک‌های نظامی و نیرو اعزام می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/692762" target="_blank">📅 23:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692761">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه چهارم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692761" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ چهارم: تفسیر دعای فرج
🔹
دعای فرج به‌ عنوان یک سلاح و ابزار حفاظتیِ طراحی‌شده توسط خود امام زمان (عج) برای این دوران بحرانی معرفی شده است.
🔹
دعای فرج  ترکیبی از «اظهار وضعیت وخیم (شکواییه)» و «ثنای الهی (اعتماد به قدرت خدا)» است.
🔹
ما انسان‌ها در ظرف «زمان» و «مکان» گرفتاریم، اما حضرت صاحب‌الزمان (عج) از قیدوبند زمان خارج است و به علم لدنی دسترسی دارند.
🔹
محاسبه نفس، گوش ندادن به «صوت دجال» و مراقبت از نیت‌ها و کارهای روزانه، لازمه‌ی عبور از فتنه‌های آخرالزمان است.
🔹
راه نجات از رنج‌های دنیوی، دست کشیدن از تلاش‌های بیهوده در عالم ظاهر و اتصال قلبی به امام زمان برای صدورِ «فرمانِ گشایش» در عالم امر است.
🔹
امری که خدا برای زندگی ما صادر می‌کند، توسط حضرت ولی‌عصر (عج) اجرا می‌شود.
🔹
رضایتِ قلبی، قوی‌ترین حمد و شکر است که راه را برای گشایش باز می‌کند.
🔹
در تمامِ لحظات به حضرت صاحب‌الزمان (عج) تکیه کنید و بگویید: «خدایا راضی‌ام به آن چیزی که در عالم امر برایم رقم زده‌اید».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/692761" target="_blank">📅 23:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692760">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABMvX0sQivCtEaq84cjRiYe-tbNrXmivb-bcOGkWZY8JkcQylieLSQJuaKZU8Qfqo-hOp4YNElJzpe9gPa6jf20fCF50fkeLGLFJ34Fo8e1flZYYKz-JO2zyLwHTuPiz_YPS84zGa8ftk7ESJ8YV3Wsu8zMMU-SiDUgP0LKN0SSwZVkZgYodDWQ3jHcfDUZlABBKZZmty3EwkUu2lpyY-79Q9tkKt0U_YK0e2FGsWwgUJcVj9FZwOpr3QC1zXDKReHeUauYy9dRfJAnjmvJ-7-x9nVNrsqiPLbOHqHJp9tzWI9nTPcqskTqnXgdyZWyBbAWshBUkUvpJdvck7ntWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: مشارکت اروپا در تجاوز به ایران بی‌پاسخ نمی‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/692760" target="_blank">📅 23:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692759">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtiijgaO-XK_3a9_MXOj1omz9njLlW9c7tYBELMml7UsSgSmAuTHJehtfpBVXP4JSaaU4gipkB68XlCL6gcr2VinHaX1R9-PiTyl3P2d7MBGepSYiRn1SJYFGCN7j0jw9aLkk3JwAjK5sBF3Cc3IekhInkxHkDf1kIP8xrwDc7wkRM5qU4Fsy7jBzpVKW9KA5bCt-r5BaCXo5rDEiZ1DHur-Dx4anBq-zIOOqh2HJt1bix7Xwlf7j2wH1nO2RnqZFBO0XxBFy7CetrUzoSo6z3awNmfgviOZMA2LfCldOqY1ZtFFFfNNd7E3VDeho8x9q_Ur5Ndnawh5PT-apsFbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☎️
«با ثبت اطلاعات مرکز آموزشی خود در سامانه ۱۱۸، کسب‌وکار شما همیشه در دسترس خانواده‌هاست.»
🗓️
از اول تا سی‌ام مهرماه ۱۴۰۵، فرصت معرفی مدارس، آموزشگاه‌ها، مراکز آموزشی و کودکستان‌ها در سامانه ۱۱۸ را از دست ندهید.
@tci_iran</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/692759" target="_blank">📅 23:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692758">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe0cd02cb.mp4?token=AtdReLnDW5NSJHrp3MTcswODkE0qyq2urMCGvDTNs0kuRO55cGNeFry30cvLqFhIwRfGdg9BSHOqu0K3wyId3IVXM6CMOkJBVKoUcqzZIU_fCohsU8ZN7RDk55ZEhzmpN8kukd8Tfk0IIq6r9DaM6D5BtW9oHPnAANU5ipk5sZE3TYFaFGYREIGI3H3YnN1XKz7TlbUvVNoMqRvhdOrNGjVFMeafaa_cH0hjFZEZYr8bOFhreVYtk7HbQxJgK-7l9y7Gyj_dqPKghA3QcldrFdBSz7Go57-aZ3P1Og7dmLRquic1mIil4CD8V27m5T13QRLhcsJAw9mSxz5OaxWrZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe0cd02cb.mp4?token=AtdReLnDW5NSJHrp3MTcswODkE0qyq2urMCGvDTNs0kuRO55cGNeFry30cvLqFhIwRfGdg9BSHOqu0K3wyId3IVXM6CMOkJBVKoUcqzZIU_fCohsU8ZN7RDk55ZEhzmpN8kukd8Tfk0IIq6r9DaM6D5BtW9oHPnAANU5ipk5sZE3TYFaFGYREIGI3H3YnN1XKz7TlbUvVNoMqRvhdOrNGjVFMeafaa_cH0hjFZEZYr8bOFhreVYtk7HbQxJgK-7l9y7Gyj_dqPKghA3QcldrFdBSz7Go57-aZ3P1Og7dmLRquic1mIil4CD8V27m5T13QRLhcsJAw9mSxz5OaxWrZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رپ سخنرانی پزشکیان هم ساخته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/692758" target="_blank">📅 22:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692757">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q63wTA2sOF7Fk8A6hRFxQMRqNGeY8u4b9JQA1exfSRPTKXz_gl1kwUtgCJxKRppgm1dH34Xwkvj6_PvIPj9gAm_6glVRvN4RXhL8FgfnOTkmyXFah6x2JvfvFSMf55P8tJnur8c5NlbHpfV0Q9k62UIq5MoFJH2tJh6SuAbPPqIVJupc0dAKqXp7wd4UU-OhbhsgEI1nyQMw8i-44SFnwdsi9xk79Jiee42Wi1wU53DaHV75bBIr0KfyyBvGE6BVXD9oKdqQ1ui6xXmHAQf4jGHgqikwQd91d-f7vUes4PuDwZktMf_53TNPROLDax9CXruz-DnqdYmiQ7D766t1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکهٔ فاکس نیوز، که محبوب‌ترین شبکه‌ تلویزیونی نزد ترامپ است، در جریان سخنرانی نتانیاهو، دوربین خود را روی میز ایران و تصویر حاج قاسم سلیمانی متمرکز کرد و این تصاویر را به‌طور زنده پخش کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/692757" target="_blank">📅 22:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692756">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نخست‌وزیر رژیم صهیونیستی تلویحا از برنامه‌ریزی برای آشوب و اغتشاش در ایران خبر داد
نتانیاهو:
🔹
می‌خواهم یک خبر خوش به شما بدهم؛ اتفاقی باورنکردنی در ایران رخ خواهد داد. روزی که چندان هم دور نیست، حکومت ایران سقوط خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/692756" target="_blank">📅 22:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692755">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e2919c55.mp4?token=Xe9V61cr1eN4NA7Rg0o57oZRYIK6aQXGILsBTB3UKARwjZVBq8NDRlk0lemMVr7tGkGiYPW3tCAUV97OA9J44YNg0gNb6iaKehtuH9-pAE8orfsW57Yd5uCxwV7vGMWwr70bj5B5ZXSVznDsfjRSpZ8t-AB13Yg0As_xHc1Al9j4NgAheoRksAYaaZpOZdqBgZ4-lZnTmSFiKAoHRcLhIPfbvFOBwAwC9ivaKPiJDi7bpXbgPZjJWvC9FKjBY2LhSVwE2l3K2nX5QMOn0cMkn7oYlK2-ZjQJRkawKyXrS2rfGNo3WcAkygUMuwIpQwAny69zPmWaDMcHFIpboXBZvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e2919c55.mp4?token=Xe9V61cr1eN4NA7Rg0o57oZRYIK6aQXGILsBTB3UKARwjZVBq8NDRlk0lemMVr7tGkGiYPW3tCAUV97OA9J44YNg0gNb6iaKehtuH9-pAE8orfsW57Yd5uCxwV7vGMWwr70bj5B5ZXSVznDsfjRSpZ8t-AB13Yg0As_xHc1Al9j4NgAheoRksAYaaZpOZdqBgZ4-lZnTmSFiKAoHRcLhIPfbvFOBwAwC9ivaKPiJDi7bpXbgPZjJWvC9FKjBY2LhSVwE2l3K2nX5QMOn0cMkn7oYlK2-ZjQJRkawKyXrS2rfGNo3WcAkygUMuwIpQwAny69zPmWaDMcHFIpboXBZvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رئیس‌جمهور چین به توهین ترامپ به بایدن
🔹
در این ویدئو، شی جین‌پینگ، رئیس‌جمهور چین، با خنده به پرتره‌ای که دونالد ترامپ از جو بایدن (با کنایه به امضاهای خودکار) نصب کرده بود، نگاه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/692755" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692754">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCh8yzx_NuepOKgUF58jrfYCO5IZDnMCvE2AvXTKoc3EJvwKkqxIwrXzI6605_mPmqMPKkQtRlxLLrWFV8Q7M_v6NgpBRQpJJQ-1Irc7ILZFW-idwHznoPnrcFkje3eGj6JSpz6VQAPhQ96AaZCMDg2bjwOpctttUdnusVsAhHrnyVwEtzwaHBFr5bviYcGY3Qf7-fVt51QK2iokYBYBpEM1Etd3j22K3B5ASCzYKuRvTMipJoyHpDGbUNU-Po8PoyJM8it020ifNrOaC0xEXIfJdZObXEuXo6gRlgYMi4a9ZHQ40LhR-_Xxdl8d4jEQFp0vMeev-H0d-N8Jf4R7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال سیاسی آمریکایی: هرچه بیشتر با منفورترین کشور روی زمین متحد بمانیم، اعتبار جهانی آمریکا بیشتر به باد می‌رود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/692754" target="_blank">📅 22:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692752">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01569f344d.mp4?token=OW3tqAs__ts9xR6b2-ZgVyG_N5zfrvFBNKlpjPwJjVJHnEbDiW_mEgTbFVfL8x8QD-0EZuuWLNU7qAmLftt71A7Um4oNjQfBAF6Tyay08fGzTIFjplt8Kgsu8qtHCpggHF4wIoLkl8Xr8_ciF09t0i8PwO6zEO8xEUkgA5r0kDyjgxnYyoI1brQjc8VzWgxN1sP61H8Ydd3QAcqRnvrXLf4ta56JSNJvTfiSiW2w93g5U5zPtxOcK9II0PIP6OaotR20_j4MihUS9GP9-VIK0MGcUWM3FIqYRS8aIsz6e9_tQLBME_jqMcP0lYdXMBQq0YHe3KO8KUjtlI0_pp5fVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01569f344d.mp4?token=OW3tqAs__ts9xR6b2-ZgVyG_N5zfrvFBNKlpjPwJjVJHnEbDiW_mEgTbFVfL8x8QD-0EZuuWLNU7qAmLftt71A7Um4oNjQfBAF6Tyay08fGzTIFjplt8Kgsu8qtHCpggHF4wIoLkl8Xr8_ciF09t0i8PwO6zEO8xEUkgA5r0kDyjgxnYyoI1brQjc8VzWgxN1sP61H8Ydd3QAcqRnvrXLf4ta56JSNJvTfiSiW2w93g5U5zPtxOcK9II0PIP6OaotR20_j4MihUS9GP9-VIK0MGcUWM3FIqYRS8aIsz6e9_tQLBME_jqMcP0lYdXMBQq0YHe3KO8KUjtlI0_pp5fVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از پیوند قلبی دکتر پزشکیان و رهبر انقلاب
🔹
سید ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات با انتشار ویدیویی در فضای مجازی، روایتی کمتر شنیده شده از باور عمیق دکتر پزشکیان به رهبر انقلاب را بازگو کرد.
🔹
دکتر هاشمی گفت میان این دو، نه دیواری است و نه فاصله‌ای، آنچه وجود دارد، پیوندی نزدیک، باوری قلبی و رابطه‌ای عمیق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/692752" target="_blank">📅 22:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692751">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن از انجام دو عملیات تلافی‌جویانه در پاسخ به حملات مستمر ائتلاف سعودی خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692751" target="_blank">📅 22:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692750">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=P5e7W9R8gkBR4FFOHjKMqK1TMz-gZG0w7T8zbHeoPo8iH0R9kPp9pBL3fTeEGQDx2VT-4bNOAzMi7sq9YLSPgBDVdMP-6vuzO8TB5MalMXaYTBWLt6XlvZw4XjVYqnmDaU1TMtOWlsbaqFaMVxC6ordx39xtA3DvajIa-EH-50MFE3ly4F4qtTufp3TZsqQdiAKanz4nNkEUygtmPGsUidwbg4284FXt9oiZisBHfhH8e3JgHMZAjsYSlQuBOwaUzXX5eDkVDlUfL2mhjAnYZIKFg_5iKz6m5qrrCaOqJPY-BWMOhXidTapf0M0FNzanOS-dUVqXXWnxE8prvTbAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=P5e7W9R8gkBR4FFOHjKMqK1TMz-gZG0w7T8zbHeoPo8iH0R9kPp9pBL3fTeEGQDx2VT-4bNOAzMi7sq9YLSPgBDVdMP-6vuzO8TB5MalMXaYTBWLt6XlvZw4XjVYqnmDaU1TMtOWlsbaqFaMVxC6ordx39xtA3DvajIa-EH-50MFE3ly4F4qtTufp3TZsqQdiAKanz4nNkEUygtmPGsUidwbg4284FXt9oiZisBHfhH8e3JgHMZAjsYSlQuBOwaUzXX5eDkVDlUfL2mhjAnYZIKFg_5iKz6m5qrrCaOqJPY-BWMOhXidTapf0M0FNzanOS-dUVqXXWnxE8prvTbAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه فاکس‌نیوز تیزر مصاحبه رئیس‌جمهور ایران را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/692750" target="_blank">📅 22:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692749">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBOpnEpkukB-tjtCOc5KSkj4SRRmY27bKr1bBazMJbyzcUH1BdJFW3Xa0k9TqGaFdJ3IE_hXfEjMzYDuA7lxQuSBGb0TcrJsr5aPmAQWo8IMhLge8YXbnA8qiOt142JT1z40stDcQfUz8rs9Kwq2wwZMdIO55z2dASrwClOChMdyP2dv0-iLYGFsQYLUK5sGoy5UyscsWmVGZCEAQyfyLmFRZZmNVI7zPtu4Okt75EqVJVp80YlfZjA5NRHHjyn41fd1i7xUtrEAydCcvjPTtxbroiiaBeYCLhiUF8345QU7YfH_-FhBvf7wxWWZQF4XYME8YXkZL92fU0uE8T8rPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون: در جریان سخنرانی بنیامین نتانیاهو در مجمع عمومی سازمان ملل، سالن... عملاً خالی می‌شود...
🔹
این پیام نسبتاً روشنی است که اگر اسرائیل می‌خواهد روند افول جایگاهش در سراسر جهان را معکوس کند، باید رفتار خود را در عرصه جهانی تغییر دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/692749" target="_blank">📅 22:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692748">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMfE2ox-eYOG1Jv96AdWfVd2NOlJXP2FLNEeplgHD9I2eKy9dBmiSf1p69BGbZm13cf4ILZXTFBZeeK_0mebvp2FRQ6537iEJkfHb5kxDuha0mX3WNwj5tZdXxHSvCTxBG5CWeCDqkOMSR03F8uwRRYaDjHlE61p4cFBFI0dCP997M8_9SYDOeqg1u70PykCFzbGBHKcUnqV1ZhR07kI7wQdeS2k9vWl60FVJ4v-gaHkXlDwFX7vPTah0ZKBJs7ND_lKfcnJotgn2VjRukgyh5zaXHnjQrxHsLSc8Fpry3DCdEABMOqbR8HEUjK-efUfarPWPXDEqvNtcaErYZ_rRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۷ هیئت زمانی که نتانیاهو سخنرانی‌اش را آغاز کرد، سالن را ترک کردند
کشورهای عربی — ۱۸ کشور
سوریه
فلسطین
اردن
لبنان
عراق
عربستان سعودی
قطر
کویت
عمان
یمن
مصر
سودان
تونس
الجزایر
لیبی
موریتانی
سومالی
کومور
آسیا — ۱۴ کشور
ترکیه
ایران
پاکستان
افغانستان
بنگلادش
اندونزی
مالزی
برونئی
مالدیو
میانمار
کره شمالی
ترکمنستان
ازبکستان
قرقیزستان
آفریقا — ۲۰ کشور
آفریقای جنوبی
سنگال
جیبوتی
آنگولا
جمهوری کنگو
جمهوری دموکراتیک کنگو
لیبریا
اریتره
چاد
جمهوری آفریقای مرکزی
ماداگاسکار
نیجر
بوتسوانا
اوگاندا
لسوتو
اسواتینی
گینه استوایی
موزامبیک
نامیبیا
کنیا
آمریکای لاتین و کارائیب — ۱۷ کشور
سورینام
پاناما
ونزوئلا
آنتیگوا و باربودا
بلیز
باربادوس
کلمبیا
دومینیکا
نیکاراگوئه
پرو
سنت لوسیا
باهاما
بولیوی
کوبا
گویان
برزیل
شیلی
اروپا — ۶ کشور
مقدونیه شمالی
سان‌مارینو
اسلوونی
بوسنی و هرزگوین
اسپانیا
ایرلند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/692748" target="_blank">📅 22:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692747">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وزارت خارجه عراق: آمریکا پایگاه «ویکتوریا» در فرودگاه بغداد را به عراق تحویل داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/692747" target="_blank">📅 22:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692746">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نتانیاهو: رئیس‌جمهور ترامپ بزرگترین شریک ما باقی می‌ماند زیرا او با نهایت شجاعت در برابر خطر قریب‌الوقوعی که متوجه ما و جهان بود، ایستاد
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/692746" target="_blank">📅 22:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692745">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtpSdZNL2mPR6-cGanna3twOeEfhozrrM16FayiuVQNVGbLkyE93iK7E6wkkfXkSsKDBlELnTOekiPYI8Qseob8g7aQ_5HVDP4U6ANh5zx2bshx2-55rKmwDnr3jC8ORC2050of64NsU3dkCOoRI3DoieRfcIbCx2cBKQ-THsbl40EGjtjN7mcBk3fulCuhkhzOLacsS1oTUMclVoQaNswEpbFUYfqANiVZpDMlW1A0BJpJc4r_LczLGB57WEUXDn6pXhSmrbB7Je8iOGEcr1l3lmaHXLGBB9JIsziPIpRSKLujGG9vfi-GaccueF1p0D5m4awUgLSI0doszRFD28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از سخنرانی نتانیاهو برای صندلی‌های‌ خالی‌ سازمان ملل
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/692745" target="_blank">📅 22:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692744">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
نتانیاهو یک دستگاه آنتن استارلینک با خودش به سخنرانی آورد و به دبیر سالن داد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/692744" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692743">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111bb640ed.mp4?token=WKSWYI2bQt9Zt0ZaEF1q15-rG4SvNY6eegXAI7Cfl1ArgPNABwspckTD-VDcEWgHz_jYszPBWyho937WKUouJJFAs_oAjwTcMNg1G7aknVPBHvvd1npk0_X4l2eCkd1p-v8Lb8MI2x-14--hHkrtR7-gUatmuB_v1ly6j9mylbGXysmy1_M2ydMb1Vuqj4yVacVDK5NM4F3Q5vFzCFectS45mnBrBt99gYuYUxB1gF6R35UHmgp6dszsDCgbI3wtz3pOFlBiA7yIbyCLuEME7s9ZfjU2Aa--5HGit4IrILR4n2yOgqoUG10vykGPwJ46oR1UjrshZuvd813KuxfInQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111bb640ed.mp4?token=WKSWYI2bQt9Zt0ZaEF1q15-rG4SvNY6eegXAI7Cfl1ArgPNABwspckTD-VDcEWgHz_jYszPBWyho937WKUouJJFAs_oAjwTcMNg1G7aknVPBHvvd1npk0_X4l2eCkd1p-v8Lb8MI2x-14--hHkrtR7-gUatmuB_v1ly6j9mylbGXysmy1_M2ydMb1Vuqj4yVacVDK5NM4F3Q5vFzCFectS45mnBrBt99gYuYUxB1gF6R35UHmgp6dszsDCgbI3wtz3pOFlBiA7yIbyCLuEME7s9ZfjU2Aa--5HGit4IrILR4n2yOgqoUG10vykGPwJ46oR1UjrshZuvd813KuxfInQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس نتانیاهو از موشک‌های بالستیک ایران: خانم‌ها و آقایان، شما اینجا در تالار مجمع عمومی سازمان ملل نشسته‌اید
🔹
آیا می‌دانید اگر تنها یک موشک بالستیک یک‌تنی به این مکان اصابت کند، چه اتفاقی می‌افتد؟
🔹
آن موشک کل این مجموعه را نابود خواهد کرد. در واقع، دو موشک از این نوع، سازمان ملل را به کلی از بین می‌برد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/692743" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692742">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5d82671d.mp4?token=NwoYk1_wqRtjs3HZIhOKFX4f7ynB-v8TM4WCJ9iA3EJcOnKddPDUqyxPDjosPykjlmF3IwgGwCaGpewg9tqMgng7HctRWthlDjE2QXTn7yDxTFdK9fyMT_8FlsMcJ9woywjcbBsFS4q0eK2_izycUYQHXNPEiiSSgiggL9mWN_9Hz437xozmVFJmI53APvf8MhUoz_ut56sHBoquB6kRncpZomLkqNWHY-w2GvE8jRlm472pzyN6ToU_dokJC5o4SuKePjg-xgBy7lIqIp4FoN9OcZtun3yI0S1dv7_xWKNY-YsraLZewMbjshu98WTzK_inwPbbLUuwi3XkckmzBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5d82671d.mp4?token=NwoYk1_wqRtjs3HZIhOKFX4f7ynB-v8TM4WCJ9iA3EJcOnKddPDUqyxPDjosPykjlmF3IwgGwCaGpewg9tqMgng7HctRWthlDjE2QXTn7yDxTFdK9fyMT_8FlsMcJ9woywjcbBsFS4q0eK2_izycUYQHXNPEiiSSgiggL9mWN_9Hz437xozmVFJmI53APvf8MhUoz_ut56sHBoquB6kRncpZomLkqNWHY-w2GvE8jRlm472pzyN6ToU_dokJC5o4SuKePjg-xgBy7lIqIp4FoN9OcZtun3yI0S1dv7_xWKNY-YsraLZewMbjshu98WTzK_inwPbbLUuwi3XkckmzBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف نتانیاهو به جنایت در کشورمان با همکاری آمریکا!
🔹
خلبانان آمریکایی و اسرائیلی مأموریت‌های مشترکی را انجام دادند و دو کشور برای بازگرداندن گروگان‌ها نیز همکاری کردند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/692742" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692741">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: نتانیاهو برای دیدار با ترامپ در نیویورک تلاش کرد اما موفق نشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/692741" target="_blank">📅 22:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692740">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اکنون رأی‌گیری سنای آمریکا در مورد قطعنامه اختیارات جنگی ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/692740" target="_blank">📅 22:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692739">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d7b5c9e7.mp4?token=qc8ViEx7ihXnatnvMtablgMc5p7cTGHUp79PL8p8md2i9w3twoe9d5WWSNMrOqxuQsM3BmcOUJcoml9NRUn9YiYl6qGqUd9NSl7BFt1my7FXqHK9cIngrmr8eZBtss5qpKYaonl_nhQujXksDbrwBpnX0bN4cEjKyLet0MqFrMmrjZi7JaygCI_FwdYgigFvIncj7MJ6N0VnhuS_Fu1bgPzTfV_C2RTVPjfSYJbgYbuM059V_7Rrw2DO-GAYPRb3Ps5_RAlvG_5BTDEZPwo2kg0qqIfhefZs5-tVlmdj-AkwW09txO4yVbKVWBGF7_My4_iw4_-b9L6TE0OOeJr4BYRKIRwgWFoOywkNZDtc_h0go_fuewIgi8665iK47-5Pp39XC7nyBgpLXxQwvn8UXmSZHSP4n0TbzRGJvAVNY0i-DkGniz2L3ytV-f1k-OulJ6_xbDyRCDZRu5X9Tu34I5MlqjleRYNM5mwTOI2Gp7XVooJHP_t7cQ_QpWDfURr9jR7nfYqpnKeHsdfkbHlKdTv4UKsUx0yVhwHJXYI0U47LbyBuWqG2zsYvpKDJyhCvirFOXOfuhVrsHL-n_9oq-kNvVX-UCRTlJTTEaqMZ9VvlHp_gdFy0g6MvQxB-Fl-NvpRNIR7KtIxJ3RXJFpbSSLo75NVHjvlBjrP08MTeooE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d7b5c9e7.mp4?token=qc8ViEx7ihXnatnvMtablgMc5p7cTGHUp79PL8p8md2i9w3twoe9d5WWSNMrOqxuQsM3BmcOUJcoml9NRUn9YiYl6qGqUd9NSl7BFt1my7FXqHK9cIngrmr8eZBtss5qpKYaonl_nhQujXksDbrwBpnX0bN4cEjKyLet0MqFrMmrjZi7JaygCI_FwdYgigFvIncj7MJ6N0VnhuS_Fu1bgPzTfV_C2RTVPjfSYJbgYbuM059V_7Rrw2DO-GAYPRb3Ps5_RAlvG_5BTDEZPwo2kg0qqIfhefZs5-tVlmdj-AkwW09txO4yVbKVWBGF7_My4_iw4_-b9L6TE0OOeJr4BYRKIRwgWFoOywkNZDtc_h0go_fuewIgi8665iK47-5Pp39XC7nyBgpLXxQwvn8UXmSZHSP4n0TbzRGJvAVNY0i-DkGniz2L3ytV-f1k-OulJ6_xbDyRCDZRu5X9Tu34I5MlqjleRYNM5mwTOI2Gp7XVooJHP_t7cQ_QpWDfURr9jR7nfYqpnKeHsdfkbHlKdTv4UKsUx0yVhwHJXYI0U47LbyBuWqG2zsYvpKDJyhCvirFOXOfuhVrsHL-n_9oq-kNvVX-UCRTlJTTEaqMZ9VvlHp_gdFy0g6MvQxB-Fl-NvpRNIR7KtIxJ3RXJFpbSSLo75NVHjvlBjrP08MTeooE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف نتانیاهو درباره ۷ اکتبر: در آن روز ۱۲۰۰ اسرائیلی کشته شدند
🔹
اگر این رقم را بر اساس جمعیت مقایسه کنیم، معادل کشته شدن ۴۰ هزار آمریکایی در کمتر از ۲۴ ساعت است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/692739" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692738">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نتانیاهو: ما قانونمدارترین در دنیا هستیم! / شهرک‌نشین‌های ما مورد حمله قرار می‌گیرند درحالی که قانونمند هستند!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/692738" target="_blank">📅 22:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692737">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
نتانیاهو علیه شهردار نیویورک: از زمانی که به عنوان شهردار این شهر انتخاب شدید، بسیاری از یهودیان دیگر در نیویورک احساس امنیت نمی‌کنند
🔹
همسرتان پستی را لایک کرد که عملیات ۷ اکتبر را می‌ستود. او پست دیگری را لایک کرد که می‌گفت تل‌آویو نباید وجود داشته باشد. شما از محکوم کردن آنها خودداری می‌کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/692737" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692736">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
نتانیاهو: اردوغان دیکتاتور است/ آخرین کشوری که دروغ‌های یهودی‌ستیزانه منتشر می‌کند، ترکیه است. او می‌خواهد بر سوریه مسلط شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/692736" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692735">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd22202d3.mp4?token=JCMm2gFPGPSvs8XrOlpLVsF5s2BMm0txOTqq9VI5MiGXVprc4idEPUXn3_fPHVcsI2b9tNu9-vnHE3O3r-pzgt4SYHlUqKQZQ0U4JPe8oTnFpU2aekPqFkXgDegPbcp_Oo1crhGbUzYhd-BVbSVfdxxqIX6Zf_0uQbHpHWeuPBoLiVT8jEgD_FrPMk3PoU2rBxlV21mAudm8xhEDq_XLxLzo0DmLJPq9DgXc0MH29C89ODtsZtf4JiK6ppwf-FRwZNX5Dw2zck0j6gUeajfd_VuyBJlK6OPl9OdU9sSTCjD0GRsJ_jVMIyh_GGdQ3BmawNo4Vf9W7KM2CzA5FK24MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd22202d3.mp4?token=JCMm2gFPGPSvs8XrOlpLVsF5s2BMm0txOTqq9VI5MiGXVprc4idEPUXn3_fPHVcsI2b9tNu9-vnHE3O3r-pzgt4SYHlUqKQZQ0U4JPe8oTnFpU2aekPqFkXgDegPbcp_Oo1crhGbUzYhd-BVbSVfdxxqIX6Zf_0uQbHpHWeuPBoLiVT8jEgD_FrPMk3PoU2rBxlV21mAudm8xhEDq_XLxLzo0DmLJPq9DgXc0MH29C89ODtsZtf4JiK6ppwf-FRwZNX5Dw2zck0j6gUeajfd_VuyBJlK6OPl9OdU9sSTCjD0GRsJ_jVMIyh_GGdQ3BmawNo4Vf9W7KM2CzA5FK24MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاتل بیست هزار کودک غزه: متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/692735" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692734">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=YSgkWl1lHn5E4hT6dbWEybqiBFoYlvxT5oTjQSRjqZdXyOauX7y2r9XdYv-jsp6uSdqdrTMXjWeUaAf_wrDA9MD34AQl9F3CI3yPmPVcpabLjoAOPGwc_1qDgg5xvNTPSYiGZ4Un2xAfbPOQjpgidYz5AB2N_Zobk2TETAe-CKcaD1hNtOg3NzHpIsnQLSUInwEk5HyEV3kYcNH8wzl_wQjH6OJSBDQ9MrdMFgfaOgxXzVomtixaRoWRBThPCQwmdH0Dm7Tr32olcHTKzir8OQw1Q383qbukR9rVyX7vYIqCWj0vRk9ouxU9PKvQl8SzUDHyzwp6zQCk_evz8ZovBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=YSgkWl1lHn5E4hT6dbWEybqiBFoYlvxT5oTjQSRjqZdXyOauX7y2r9XdYv-jsp6uSdqdrTMXjWeUaAf_wrDA9MD34AQl9F3CI3yPmPVcpabLjoAOPGwc_1qDgg5xvNTPSYiGZ4Un2xAfbPOQjpgidYz5AB2N_Zobk2TETAe-CKcaD1hNtOg3NzHpIsnQLSUInwEk5HyEV3kYcNH8wzl_wQjH6OJSBDQ9MrdMFgfaOgxXzVomtixaRoWRBThPCQwmdH0Dm7Tr32olcHTKzir8OQw1Q383qbukR9rVyX7vYIqCWj0vRk9ouxU9PKvQl8SzUDHyzwp6zQCk_evz8ZovBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مضحک نتانیاهو‌ جنایتکار: اخلاقی‌ترین ارتش جهان، ارتش اسرائیل است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/692734" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
حمله عجیب قاتل غزه به یکی از شرکای مخفی خود: قطر "مبالغ هنگفتی" را برای تأمین مالی نفرت از اسرائیل هزینه کرده است: "هدف آن‌ها کاملاً مشخص بود - شستشوی مغز جوانان."
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/692733" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhRtz-3R8_GmtB7sazWgJXZ1LZ8qat0gUyNUZ11xCexX3wAXfj9Vlbfrq8aNWXB9ar1DexDO5vVRfDSSe0jaVHz1_ABGUDbjQ9lQFPgyAJ_kFOjl8typlz1sihn44u0GC9KdozNl8QQ90ECQv-LcTGcN5SjXrUoUVJMPyRTnVQ81wvZ-OPyhe9hsk4vOVlPdd13toFIpt9_KM_G9Ad_4yOb4psaYJgDrTLeh31GqRD06XcFgZW93xKMu6jumEJ9AC2CJbHZT8QN1HTh9eCwFtEWjFVm656TF2EOyJl_7JeUeZ_p91Y0rIwbSLZxsCA8inKiqyOyEoIk_BBom2egi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو یک پیجر با خودش برای سخنرانی به سازمان ملل آورد!
🔹
وسیله‌ای که منجر به شهادت و نابینایی تعداد زیادی از کودکان و زنان لبنانی شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/692732" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
گروسی: با طرفین برای بازگرداندن دسترسی به تاسیسات هسته‌ای ایران همکاری می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/692731" target="_blank">📅 22:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c840c0f046.mp4?token=qT8N7uygAh5o_a9HU3QNz7YeFQkbNJkJ09lDC3fBnFMIiMpyOWuLNFTZrX3APfBSSSkym0EL4EAEafgRKBfrDTEoztYiEN40Wi_Vs2TLx5nZ_eNy7-zCC1KI-CeTOV_7nLRWxnndoz_cAZJ5YdF4IEDDHA8NWe5DnEzozyZd-YhGHJcgNxEs5txNVXAUzYYCStFyyISJyz0ulz40kgpI2MY39IrxGBH5KXGw1nfcYrvtHsqWmJ9GNGy5LVG3ULbwzk5-NR1HFvsix4ShSl2EpV5srb8clTyNt83Ln81Z3S7MNnaDg9DM1i8eSMKIDXBHhmQqi1jx7KHbTsc78KrfjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c840c0f046.mp4?token=qT8N7uygAh5o_a9HU3QNz7YeFQkbNJkJ09lDC3fBnFMIiMpyOWuLNFTZrX3APfBSSSkym0EL4EAEafgRKBfrDTEoztYiEN40Wi_Vs2TLx5nZ_eNy7-zCC1KI-CeTOV_7nLRWxnndoz_cAZJ5YdF4IEDDHA8NWe5DnEzozyZd-YhGHJcgNxEs5txNVXAUzYYCStFyyISJyz0ulz40kgpI2MY39IrxGBH5KXGw1nfcYrvtHsqWmJ9GNGy5LVG3ULbwzk5-NR1HFvsix4ShSl2EpV5srb8clTyNt83Ln81Z3S7MNnaDg9DM1i8eSMKIDXBHhmQqi1jx7KHbTsc78KrfjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: اسرائیل و آمریکا برای نجات تمدن، با یکدیگر اقدام کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/692730" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46547643ab.mp4?token=l1OK3yN3V0XVczq_CgWQNSNKN4keNe5G7mU41PrRnTouHg1a7X0VYaJL3dt8kIokmSCOIcr8kEVCzbwqfuW1cSYQxyXgrdHFua8smpj0_bVOPrMhyruWucraNgEOMqdE2sH3A8tudNlmHY5DxJAuJ-l6ib2f78KzxHlP7Fiv9frpyuS66TsS2aafMjOeT199aev-r0TvOPOgsJk6AfLx5ozV0f02_3HXAU_-n3XEkWKY7btvn01Sc_ye7UVOGHuoOkbPBV2csN2GI0qpd5XBA80iwonrzbX4IKneuORD1X67CLTeJwAS1sCWuk1en7zZ_BUCYi48PaHRRjfEToNUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46547643ab.mp4?token=l1OK3yN3V0XVczq_CgWQNSNKN4keNe5G7mU41PrRnTouHg1a7X0VYaJL3dt8kIokmSCOIcr8kEVCzbwqfuW1cSYQxyXgrdHFua8smpj0_bVOPrMhyruWucraNgEOMqdE2sH3A8tudNlmHY5DxJAuJ-l6ib2f78KzxHlP7Fiv9frpyuS66TsS2aafMjOeT199aev-r0TvOPOgsJk6AfLx5ozV0f02_3HXAU_-n3XEkWKY7btvn01Sc_ye7UVOGHuoOkbPBV2csN2GI0qpd5XBA80iwonrzbX4IKneuORD1X67CLTeJwAS1sCWuk1en7zZ_BUCYi48PaHRRjfEToNUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو یک پیجر با خودش برای سخنرانی به سازمان ملل آورد!
🔹
وسیله‌ای که منجر به شهادت و نابینایی تعداد زیادی از کودکان و زنان لبنانی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/692729" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-CAkrOx1afuMWmpF1iMbLZUm8Em2oJ3Uf0-bM5x_9wW43z_lIhjtYgGGWAhiWHJNbAXLEYyz5EM90dI470Q1Ve6vRP2ZsEJAvm89pRIvAYcg9yUcrQfmGlxCAFKBCKc8WtPyreZOf9k1oTGYWXmRNytY6VHYe1LL3Au7akxVF9VdBAiX8QTE4-PgJfzZW481ghpkXx0iDRefxzRJiCuoFdWoj_APvSIn2cC0GAHZw0OXf1YsiZ8zY2KCqM17fcN2WVzYXowm-vr9zqjIjO1jLcdRnCIDLdqXFCMB0tdXoUnxXdsWmqQKA09FBY9Ikx2L4SNbZxdak6o6IrMAucMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرار گرفتن تصویر شهید سلیمانی روی میز هیئت ایران همزمان با سخنرانی نتانیاهو
🔹
رسانه‌های عبری تصویری از محل استقرار هیئت جمهوری اسلامی ایران در نشست مجمع عمومی سازمان ملل منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/692728" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692727">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
نتانیاهو خطاب به انگلیس و فرانسه: جنایات امروز ما برایتان خاطره است
انتقاد شدید نتانیاهو از انگلستان و فرانسه:
🔹
انگلیس و فرانسه، اسرائیل را به استعمار متهم می‌کنند. خودشان این واژه را ابداع کردند، مستعمرات آن‌ها کل جهان را در بر می‌گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/692727" target="_blank">📅 21:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692726">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
نتانیاهو: آقای الشرع، یهودیان از زمان موسی در بلندی‌های جولان حضور داشته‌اند؛ می‌توانید در کتاب مقدس بخوانید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/692726" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a4488558.mp4?token=HqdPv0nzXZz7demqNGBOP6fGvRLfsuX_LVkr968qdFXRrz9AMqLYsy7o-nt_T7oc7zC2q3XYUH0XORFtxoSCqggp-DQD9rmP1E-Inva6OQkoq0V9BraDJlH4ELfwjV5dj0eEMSmbp2-WMS2m-WtDgWPVQlP_4HPKMGnN7ET0hNq8FpFnriqf-0_k37FQfzlMDWtG9Ji1w1eN3_fI2tcE-_fMfaX4GAeIwbS0mIKLhnECCa7eCFdDistCJ6JtUXPSuD8DwU0od7IoYNaEQcNnXekzV9tV_jnHt8Ct8aOyZm175rOn14xEm5B0WxfYTGD6LKc1cjKbqujRDplLldrxqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a4488558.mp4?token=HqdPv0nzXZz7demqNGBOP6fGvRLfsuX_LVkr968qdFXRrz9AMqLYsy7o-nt_T7oc7zC2q3XYUH0XORFtxoSCqggp-DQD9rmP1E-Inva6OQkoq0V9BraDJlH4ELfwjV5dj0eEMSmbp2-WMS2m-WtDgWPVQlP_4HPKMGnN7ET0hNq8FpFnriqf-0_k37FQfzlMDWtG9Ji1w1eN3_fI2tcE-_fMfaX4GAeIwbS0mIKLhnECCa7eCFdDistCJ6JtUXPSuD8DwU0od7IoYNaEQcNnXekzV9tV_jnHt8Ct8aOyZm175rOn14xEm5B0WxfYTGD6LKc1cjKbqujRDplLldrxqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای دیگری از هو شدن نتانیاهو و ترک گسترده سالن مجمع عمومی سازمان ملل همزمان با آغاز سخنرانی وی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/692725" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692724">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
نتانیاهو: وقتی اسرائیل از خود دفاع می‌کند،[شما بخوانید بمباران مدرسه و بیمارستان و غیرنظامیان] اسرائیل از بسیاری از کشورها نیز دفاع می‌کند، و نمایندگان آن‌ها اکنون سالن را ترک کرده‌اند. این یک ریاکاری وحشیانه است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/692724" target="_blank">📅 21:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692723">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxSW73MYAQ3vxy6U0De1m-9g3r1MH2Frv6_rEOnkYvp_h949EIlrL28nU5WTyHfSvbSxx1FkXibsUzDqCNNNz9ieju7m1paYrqC7KkHuAE6nMfgDW4UlixiDTljsNk2tfEkDZ1wGNTtBIiFpGs0v2RusXUBeqZ5aMvI4cDETGZrfDFt1jnr8ErUixseMHqX5vnvhiWkCBp8tZunxIb04QHo2AqWv7Lu8zf1X1rcTu32dKHc0EfrH_uRDBqIrbiFN9p-U-cmgfNQWSYgEC1BeKaPBVJ1JrNKxkONNFAptWBcMIOXxNT1T16oVhzuGmcr6olajNYDe4xmlN2fUGnmWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی‌رغم ترک صندلی‌های سازمان ملل توسط سران کشورهای جهان به صورت گسترده، نماینده شیخک‌نشین امارات در سالن باقی‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/692723" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692722">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a549f532.mp4?token=UID2yH3fWNcJL4MXgVqmwJZ99AGbFtYgMlW5OSpJCYNoJkiPsaI9-kKz9yd8POzOmVqbCvU4rWIZNmCnjqDhSilYuERs3TBtI2XAiyCgtMWcbXr-pGUx1M6k2aia7eFpmrtpLalDMnpn0e7waostjc4ARnt64phdGuNELKwlIIsSwr_KkE8i4NTynXu8Y7PedW_DVdSaBfHyg0R-FlPemJ-8_6JNvw3eHicYdpVoG8BT3Scvz6i0c4STKenJA2CSgJeUxsUvKZKYFoHnEi0h8Pox_EyUo5q3JWfC_bv9uc-j8gWbl9SYYPjZ0B6c0t_alTHqlinOt9rA5f-PIQF6_QNcsmbQRgTuWqTaKVJCpEZndPNKEcacnUGQHZazJtaQ6fa67aFBaFaZnB9k_CtGYO_-58BUAQ-cbsb_Z19mgVX07jlV_Xwb1zfCYSDiQDMBCCYPtwJfjMn1UZtkti0ZcD_SxshkONDygFOQ3BiDyNI_Fs2oEBZ2l1y-0qWk8ImHh4RrDjWJ7fLKVCHXqb4rFYYNqrN7v0o70nLhRV2pFnaLhGnnCur6bxGa4AQz5l9JhmpkufO5bpOrzjytIkDNsk1REQKX35ECRdRNddfQ9ZaBZvsgwXzIRCGyCtm0jkVjae6fiufLhRe69clnCihN-v8M6cUbqRdLmOFQ8j-0dhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a549f532.mp4?token=UID2yH3fWNcJL4MXgVqmwJZ99AGbFtYgMlW5OSpJCYNoJkiPsaI9-kKz9yd8POzOmVqbCvU4rWIZNmCnjqDhSilYuERs3TBtI2XAiyCgtMWcbXr-pGUx1M6k2aia7eFpmrtpLalDMnpn0e7waostjc4ARnt64phdGuNELKwlIIsSwr_KkE8i4NTynXu8Y7PedW_DVdSaBfHyg0R-FlPemJ-8_6JNvw3eHicYdpVoG8BT3Scvz6i0c4STKenJA2CSgJeUxsUvKZKYFoHnEi0h8Pox_EyUo5q3JWfC_bv9uc-j8gWbl9SYYPjZ0B6c0t_alTHqlinOt9rA5f-PIQF6_QNcsmbQRgTuWqTaKVJCpEZndPNKEcacnUGQHZazJtaQ6fa67aFBaFaZnB9k_CtGYO_-58BUAQ-cbsb_Z19mgVX07jlV_Xwb1zfCYSDiQDMBCCYPtwJfjMn1UZtkti0ZcD_SxshkONDygFOQ3BiDyNI_Fs2oEBZ2l1y-0qWk8ImHh4RrDjWJ7fLKVCHXqb4rFYYNqrN7v0o70nLhRV2pFnaLhGnnCur6bxGa4AQz5l9JhmpkufO5bpOrzjytIkDNsk1REQKX35ECRdRNddfQ9ZaBZvsgwXzIRCGyCtm0jkVjae6fiufLhRe69clnCihN-v8M6cUbqRdLmOFQ8j-0dhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه در شش ماه فعالیت آزمایشی «مدار» گذشت...
🔹
تلویزیون اینترنتی خبرفوری با عنوان «مدار» شش ماه فعالیت آزمایشی را پشت سر گذاشت
🔹
این ویدیو، مروری است بر آنچه در این شش ماه در «مدار» گذشت... @AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/692722" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
