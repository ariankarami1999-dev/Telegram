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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-692899">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz3hRO-lj11KjrCatx_SPxOgx0ZWct7OneZ7paSjKbOC4AngLJi3-J3r1IXMQCAVvpR7fuJ0iTQXy1JGaUAxS5_xEb9r1cbdlnKcC4dab6MeUbPXjqqKKl9jbTn9lp2W2xwp74IPGX5EwT6XvG-Jw-tiIYThM2Z_hXSJBZGd5axzI23nYyXUa05xgAdmT_gHYoDYqPSNcoTdtk0jJ2fFiTlHSev9P9EEmJQPRGbbbZNbryGv8b4i7pTU7LXMzJE53IRrvX6dmhT4wNlrCIX15H_DNKy5xnW995CpsZorukZjp8M7AhlQqrU76eSwiGEiS_VdFz8opFrixl3rM5rxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فکت‌هایی درباره تخم مرغ
🥚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/692899" target="_blank">📅 15:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692898">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تصویری از آسمان شمال رژیم‌صهیونسیتی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/692898" target="_blank">📅 15:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692897">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
خاتمی، امام جمعه تهران: کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/692897" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692896">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
قبانجی: عراق نباید تحریم‌های پروازهای ایرانی را اجرا کند
🔹
امام جمعه نجف تأکید کرد اجرای تحریم‌های آمریکا علیه هوانوردی ایران از سوی عراق صحیح نیست و از دولت این کشور خواست در این زمینه تجدیدنظر کند. / خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/692896" target="_blank">📅 15:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692895">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1aTPufjNGNqMq1yHHOk3NwispYtOo6CeO0zFSJ37fbll-ZCRynDgJGrZIADL53AiATOvp7_7lcNKZxu_EDn3wfq5zZhZ6HneDdBzzRR7v9KejuNMCNo_qCwWYxcGvu4RtJq1ufao4DqT1i0DlZnS81OOHI7ekr4C7pUwefWLil6dM6jp0vicRMax3JDYHl7bIMAvOlUI_ss54CBmEUcSWdeD4rineN7rdl4UdzMne5yIIDfFO57oaFFf8ni2xk4LsRF5oL2HS4RfBYbvrUDuvxU_sDvPfRS-49rBvLF2xHkfp4i6sm3PP0pHxgHnl9A7rkiOi1Uwu0E3GmMp-Eo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور وزیر راه و شهرسازی، پل‌های آسیب‌دیده هرمزگان به مدار تردد بازگشت
🔹
پل شهید مویدی (گریوه) به نمایندگی از هشت پل آسیب‌دیده در جنگ تحمیلی سوم، با حضور وزیر راه و شهرسازی به بهره‌برداری رسید.
🔹
بازسازی پل شهید مویدی، دو پل در محور کهورستان، پل نیمه‌کار، پل سه‌راهی منبع آب، دو پل محور بندرعباس - رودان و مسیر رفت پل رودخانه شور در مسیر بندرعباس ـ حاجی‌آباد به اتمام رسیده و زیر بار ترافیک رفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/692895" target="_blank">📅 15:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692894">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره پشتیبانی اطلاعاتی چین از ایران
سی‌ان‌ان به نقل از ارزیابی‌های اطلاعاتی آمریکا:
🔹
تصاویر ماهواره‌ای و پشتیبانی اطلاعاتی چین به نیروهای ایرانی در رصد کشتی‌ها در تنگه هرمز و انجام حملات دقیق‌تر علیه پایگاه‌های آمریکا در منطقه کمک کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/692894" target="_blank">📅 15:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692893">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COFGBt-cGQzvzMNSjZCcuAAsn7Dd47CbfqxNaQw-tnrWVDcDIpO-vAgqv62zdDw75AY1KKlJ77GGPT-Ge1Q0wHSANn0l6fNG-zJoroXXdBmmXEftoCZa_Q1WoBdQv0JEA-UH9df1ovVvcywdkQAQk1f59Yj5BS3KLCTS4KTnJX-5DQfX9oaEvP_e6G6qGQK3JFjLlTjkOGewbDWiLiRlm8zjJwUHFnJUeOcVioFKNxFtp-gMXvWNmmZP5FZmV2H7TFBu68KQ9oM3P7hm_CDpQ633jm5jVGdKrGB6Ytp8fuyk7HQwJCkkVbnrdBP2VPtzKsw4tLnPlP7PfrdCDiEM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام اسامی محصولات غیرمجاز حالت‌دهی و رنگ مو
🔹
روابط عمومی سازمان غذا و دارو اسامی تعدادی از محصولات مراقبت، حالت‌دهی و رنگ موی غیرمجاز را که بدون مجوزهای قانونی در بازار عرضه شده‌اند، اعلام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/692893" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692892">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ویدئویی از مراسم نود و ششمین سالگرد روز ملی عربستان سعودی در تهران
🔹
کیک سالگرد حکومت بدست گرفتن آل‌سعود با همراهی معاون اجرایی رئیس جمهور بریده شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/692892" target="_blank">📅 15:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692891">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
قبانجی: عراق نباید تحریم‌های پروازهای ایرانی را اجرا کند
🔹
امام جمعه نجف تأکید کرد اجرای تحریم‌های آمریکا علیه هوانوردی ایران از سوی عراق صحیح نیست و از دولت این کشور خواست در این زمینه تجدیدنظر کند. / خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/692891" target="_blank">📅 14:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692890">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شایع‌ترین علائم سرطان دهانه رحم از زبان متخصص رادیوتراپی
🔹
توصیه های بسیار مهم برای دختر های ۹ تا ۱۶ ساله؛ واکسن HPV تا چه اندازه می‌تونه از ابتلا به این بیماری پیشگیری کند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692890" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692889">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqJtLFxpHaRnjbuNRCBRIloRKG7Q20Plrl0rq0zh8x0oQTdFuwUAB6pU4eb9na-ipqgGuQyN1XfWWem5qznVEE4L55FBhUcXCvSUMx9roGFzYC9E2PLG-ZXNCfQvFZUzuiWb2tKvFJxlrymoPftA2I0rRxAtOpJ3wI-7xsoccSWTQFJDqlXMBEmeWUGQk5NNZ-GxKNhyq-4RQ4a9vY3CDeVz9xZ5KiuumfAqRAg9UaO8xX38JpjMs2DhJ5yM8AJfqeuX9nRTd5cENPdZbPJqmwMMkWtNAh1xrWahOoIPD8u5FqOdCgDlY4ewqPu7WIPGaRJyUL1NgDLIU450BWQrtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عربی از شنیده شدن صدای انفجار در شمال فلسطین اشغالی خبر می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692889" target="_blank">📅 14:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692888">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: بن‌سلمان خواستار ادامه محاصره دریایی ایران شد
🔹
او اخیراً به مقامات آمریکایی گفته است که ایالات متحده باید محاصره دریایی علیه ایران را تا زمانی که تهران به امضای توافقی جدید وادار شود، ادامه دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692888" target="_blank">📅 14:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692887">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5b367a5d.mp4?token=S6T-pVoI1HItjA0zfDz22uvJDYoi4wzcUCN8yXyjDRJyxsDOEk8UYu1OYTxxvB9DWD9d-uAGKyNrCQ7eRX_Zp9T4XZ2gbc1ljOU3_d0SmXsRAfwGUkSB_2ZzuKKb0c6CwoAaCFNHDCOf1JKQpcHsSH9HxeH0JbuU8X0HTxeFiE3m-oqsTrnTlT9rp-WTX3Z_dQwhIcPnwFbizWNaE8QzFf5JWu_sAmlYAQ9f3hnrXn9f-WxzbgfySpG5djQzX9vB0GqwAt7u4quuwvTYD2yVOsa7RBi9_9WQjhVnxrQ_HP3UJu0cJDNZV7aOHLuPSvD7tj8oJtJRNfVKlfWzQA_uiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5b367a5d.mp4?token=S6T-pVoI1HItjA0zfDz22uvJDYoi4wzcUCN8yXyjDRJyxsDOEk8UYu1OYTxxvB9DWD9d-uAGKyNrCQ7eRX_Zp9T4XZ2gbc1ljOU3_d0SmXsRAfwGUkSB_2ZzuKKb0c6CwoAaCFNHDCOf1JKQpcHsSH9HxeH0JbuU8X0HTxeFiE3m-oqsTrnTlT9rp-WTX3Z_dQwhIcPnwFbizWNaE8QzFf5JWu_sAmlYAQ9f3hnrXn9f-WxzbgfySpG5djQzX9vB0GqwAt7u4quuwvTYD2yVOsa7RBi9_9WQjhVnxrQ_HP3UJu0cJDNZV7aOHLuPSvD7tj8oJtJRNfVKlfWzQA_uiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از مراسم نود و ششمین سالگرد روز ملی عربستان سعودی در تهران
🔹
کیک سالگرد حکومت بدست گرفتن آل‌سعود با همراهی معاون اجرایی رئیس جمهور بریده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/692887" target="_blank">📅 14:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692886">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رسانه‌های عربی از شنیده شدن صدای انفجار در شمال فلسطین اشغالی خبر می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/692886" target="_blank">📅 14:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692885">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=XrTMx_BXk0qVlsQziM3NGlTJNmbcLSgpoXFdo-3evmk1YxxgZTjVpWCHGOygXcKwwkIuZO19jThbC8ZYaHKc7z7ARg1-QNnIK-Nje5k4qf1ZzHKBv062Oh4rsq_j4tEjzHHhU2pBzENljsj8s18LLh8M203yaW7NJn1viFhO5xNctPIRt6Tdt-PLYUgzkGklHFD_vohnGOu1G7egNz2avioAh10T2nxk3BcH0DFwxQrMDsPfHTDQVC5V6Eq4CEdvkZvaM8ojGhyIiUdetQvYyl69W5RXM_DDLtIELEr0BD1xKfmKkW8eW7QP9FA-Fbw2a-IeuRvwHk06TKhBryOFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=XrTMx_BXk0qVlsQziM3NGlTJNmbcLSgpoXFdo-3evmk1YxxgZTjVpWCHGOygXcKwwkIuZO19jThbC8ZYaHKc7z7ARg1-QNnIK-Nje5k4qf1ZzHKBv062Oh4rsq_j4tEjzHHhU2pBzENljsj8s18LLh8M203yaW7NJn1viFhO5xNctPIRt6Tdt-PLYUgzkGklHFD_vohnGOu1G7egNz2avioAh10T2nxk3BcH0DFwxQrMDsPfHTDQVC5V6Eq4CEdvkZvaM8ojGhyIiUdetQvYyl69W5RXM_DDLtIELEr0BD1xKfmKkW8eW7QP9FA-Fbw2a-IeuRvwHk06TKhBryOFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیرهای تنگۀ هرمز همچنان تحت کنترل ایران است
🔹
کارشناس شبکۀ ۳ با نقشۀ تعاملی بررسی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/692885" target="_blank">📅 14:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692883">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/becf821128.mp4?token=mLt1JHUReor1QZ4Bp1Qz8nF5jo66b645nuBf-AdHxARs1JNK0Nu8mvK-XvqHJMOwpELzcGlhyySxzgFhzo5mGevOpmG54zftq5qaO8LkyZwPc123ZkOZ90Wf_0z3XatN2YI4DGgQAtTA65l1Nq6oMlAOjodcoj5xeu6kefjIHGF9YApakR0r40PxHz3dANd2nUSArQQstYg0iT4o095_fYjr5k94LHf1Ax9cpS1ZAmKJjjPUvVU8PkLJ5TG_43gI1WUn3RYhWDwWuljR_cr6LpU2t3jhj7F-b1tvmdgwsmN358wkadw3CrOsYRk7mXo0icsCVJ2blWC-HzU-JBBudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/becf821128.mp4?token=mLt1JHUReor1QZ4Bp1Qz8nF5jo66b645nuBf-AdHxARs1JNK0Nu8mvK-XvqHJMOwpELzcGlhyySxzgFhzo5mGevOpmG54zftq5qaO8LkyZwPc123ZkOZ90Wf_0z3XatN2YI4DGgQAtTA65l1Nq6oMlAOjodcoj5xeu6kefjIHGF9YApakR0r40PxHz3dANd2nUSArQQstYg0iT4o095_fYjr5k94LHf1Ax9cpS1ZAmKJjjPUvVU8PkLJ5TG_43gI1WUn3RYhWDwWuljR_cr6LpU2t3jhj7F-b1tvmdgwsmN358wkadw3CrOsYRk7mXo0icsCVJ2blWC-HzU-JBBudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال عجیب استرالیا از تیم‌ملی برزیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/692883" target="_blank">📅 14:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692882">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔹
کرونا مثل یک سرماخوردگی در کشور همیشه وجود دارد و راه مراقبت هم این است که مردم توصیه‌های بهداشتی را رعایت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/692882" target="_blank">📅 14:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692881">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxa52ycJaY8xghlGaTnjIJItZFLGcYHV6VsUdreW6r3yUL9yHNWA1Y0zIIeWB5WtrhpqdQpBQbAVFPXTTMXk2275hrUWonVpUPX-zzLpZG7Gz3qMXlEVFGuETunD-e0c5Gd4kY6TCWntcEN5NPihflB8vxE43Rd_6n5dkdiZFznSrLTgfZT7ASYalvDdnSTkftjYkiwXH2TTnWwzHel7VY1d92mVy83o5JkVWH15qt1bJEiOgSoknjtTTqIzcOMWBlXzYMjtsAwfzCVnSGfTq8dLAprjXVyhrkSrCEWyyodjryZ6y3PWmDAnnhiaXW6KcR3GKfSF88LxrpaNR5IEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر، مشاور رهبرانقلاب: پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/692881" target="_blank">📅 14:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692880">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رئیس شرکت سعودی آرامکو: شرایط فعلی انرژی وخیم است و در بدترین وضعیت قرار دارد
🔹
وضعیت انرژی وخیم‌تر هم خواهد شد زیرا اختلال بسیار گسترده است و تنها به یک منطقه محدود نمی‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692880" target="_blank">📅 14:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692879">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: میانجی‌ها از جمله قطر در حال فشار آوردن برای برگزاری دور جدیدی از مذاکرات بین ایران و آمریکا در اوایل هفته آینده در عمان هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/692879" target="_blank">📅 13:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692878">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/692878" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692877">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d985672499.mp4?token=XNadIY41Lj9EVC_NOz-Rm1k4wUmBNhtO823yGsMY-1XVwuflsmUYDQwcohM4yBaC-0royWILBLBa2RuLqt5xkmeKiL-3brV9a0S2LNmAizVUaJZkFofpwfkgC3WrKxIidQPdAoc4c6H4J5FbAY5UKbhNjY3U2xMG1siEnSD3YAZ5vfcHZrvgvjwuMW3Tf0DopnHlfc7GeYJo-QgzZD7KD9bbbZlS4jo6VdNISZEMlrB9gNwsjY3_RqDJ7_JA8mWTMW-h2pXNwKQVMHfi8qql5J6YcJmaAtqbrLR9kP2ApHfKCNvgN57QMtuipEhM6RwFrqCOwxKLiCqux9UVMZpzgXgU6CnzC9O6aLbjmpgmU82m3SL80IGMbgYBxkvClx6Che9BQO_1YW5blnV94qb-30xEnKmB7aMk51hvJFEzxi5NqGInaIG7EubzFkztQnjv4YbVtqOIfSUTOhlKkFihpor-uAKoj0aTCNPOYllwiPuY6HqgqXGizkmU_qilxe-aDBUlkKQesO5mlIcbGbgQP0Dn9bCdnOviiN7gdM_Q0TB7JoVVQ-XKyiJzy1J3k3VfI_VJ2uQ6M1-YgeNuIPPwoWLhngnV2Rv1Rq5NxVG2vYb93gTLwT3_TESjlNAH_5enshGjVKQX1CvrN1IEJ1dTMuctIxnOPu1eAjGxaeatxms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d985672499.mp4?token=XNadIY41Lj9EVC_NOz-Rm1k4wUmBNhtO823yGsMY-1XVwuflsmUYDQwcohM4yBaC-0royWILBLBa2RuLqt5xkmeKiL-3brV9a0S2LNmAizVUaJZkFofpwfkgC3WrKxIidQPdAoc4c6H4J5FbAY5UKbhNjY3U2xMG1siEnSD3YAZ5vfcHZrvgvjwuMW3Tf0DopnHlfc7GeYJo-QgzZD7KD9bbbZlS4jo6VdNISZEMlrB9gNwsjY3_RqDJ7_JA8mWTMW-h2pXNwKQVMHfi8qql5J6YcJmaAtqbrLR9kP2ApHfKCNvgN57QMtuipEhM6RwFrqCOwxKLiCqux9UVMZpzgXgU6CnzC9O6aLbjmpgmU82m3SL80IGMbgYBxkvClx6Che9BQO_1YW5blnV94qb-30xEnKmB7aMk51hvJFEzxi5NqGInaIG7EubzFkztQnjv4YbVtqOIfSUTOhlKkFihpor-uAKoj0aTCNPOYllwiPuY6HqgqXGizkmU_qilxe-aDBUlkKQesO5mlIcbGbgQP0Dn9bCdnOviiN7gdM_Q0TB7JoVVQ-XKyiJzy1J3k3VfI_VJ2uQ6M1-YgeNuIPPwoWLhngnV2Rv1Rq5NxVG2vYb93gTLwT3_TESjlNAH_5enshGjVKQX1CvrN1IEJ1dTMuctIxnOPu1eAjGxaeatxms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو پربازدید از کنسرت کاکوبند در جزیره کیش| دیشب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/692877" target="_blank">📅 13:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692876">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e23ddb2a.mp4?token=Du7PcXzEi_9LTrLPRHoEd9nBY-tC6iYhvaJKwQvChewKK37hewGxobGES2kM6NrMd7qug8EN6WbUtlywUl9w9BZmqxU6wDk2FkvaXGrtsAv8beIq94WB7H7XcTieZx5OCQyR4t9acGlNXhDDQAyCKMyBIWNGV3qTBm_Dq20KFf8ETtnsGrRcrWx5Ha8ga6oh1WOKoVGEPk7g0LyzoNfdKUTL16txV9pKUM3btTV5M9_mc7xJcKfiZ5rjh1OfxzW-vkr6agU-p-_FJ33lsYUDGBGntBdsGuQgdJxNuKmyJe7FHMZqNmcYPmaWk_nLlg_QKnG8tuG4xpzKjUeOcRBmCjX2fGklxWw361S3KbuDF-G5JTgs6wu_YtoyO1qL3c0UyhczlINMG1wk3oqF0aGXroSQfQhBa_KJql_DEb5WwsfZTBfSAyjy8mnEm0ht116xc7Is2KgtUSYm-gwk44eIoA0SktleR7GkldlK7ulqznAgy4hM0-vN0Zwp87Vh2tECnw4W1I6wtCKFBWYvrceTVZsUvZXM-cK6fNYubYN6zjwEYUn9A3ltJDrxFhGHds-eTMc1eRF2jZuwi7sYiYF0s0XWsSeWMx2AQP9QZ03m9F9hdlpkqOZSzgMx9ZsXH40sOTbe_MbA1M3LUFvV7vTiS-HA7SNyT5Rcr_Sy0DdllYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e23ddb2a.mp4?token=Du7PcXzEi_9LTrLPRHoEd9nBY-tC6iYhvaJKwQvChewKK37hewGxobGES2kM6NrMd7qug8EN6WbUtlywUl9w9BZmqxU6wDk2FkvaXGrtsAv8beIq94WB7H7XcTieZx5OCQyR4t9acGlNXhDDQAyCKMyBIWNGV3qTBm_Dq20KFf8ETtnsGrRcrWx5Ha8ga6oh1WOKoVGEPk7g0LyzoNfdKUTL16txV9pKUM3btTV5M9_mc7xJcKfiZ5rjh1OfxzW-vkr6agU-p-_FJ33lsYUDGBGntBdsGuQgdJxNuKmyJe7FHMZqNmcYPmaWk_nLlg_QKnG8tuG4xpzKjUeOcRBmCjX2fGklxWw361S3KbuDF-G5JTgs6wu_YtoyO1qL3c0UyhczlINMG1wk3oqF0aGXroSQfQhBa_KJql_DEb5WwsfZTBfSAyjy8mnEm0ht116xc7Is2KgtUSYm-gwk44eIoA0SktleR7GkldlK7ulqznAgy4hM0-vN0Zwp87Vh2tECnw4W1I6wtCKFBWYvrceTVZsUvZXM-cK6fNYubYN6zjwEYUn9A3ltJDrxFhGHds-eTMc1eRF2jZuwi7sYiYF0s0XWsSeWMx2AQP9QZ03m9F9hdlpkqOZSzgMx9ZsXH40sOTbe_MbA1M3LUFvV7vTiS-HA7SNyT5Rcr_Sy0DdllYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترکیب زیبایی و ظرافت و تکنولوژی در ماشین؛ ۵۰ سال پیش
🚗
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/692876" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692875">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHBj8I-4PXxQv8ZLujK268CplhHvPo5iH2MORYhEKBntioW6kY-YS02L9jT35F7vM2DxJ0-F7CSFZwBLguNVTHE-Jt2oTqJ8rHvlvW2pcS0TN4MjRbQnbzUtB0IO01USWELskBL1MrB-LsU4qEvuuxT6ipZi_hNQ-zDFaslnRN2uOuVYL3dAHStrx0z6XWeBAeCRQJUxELXEwQ5FrtGgdjpiFvhPEk_Ey0IOydIzWt7qR32FgT5854c9MdrqFpo81r5Yud57uQSHLyCTA1MUfgFTyZI0EqN_2ApZn18mBkfKusSK5SrucTuvNOJsAf7uJL10Aun1LZ3lE-pw2U8RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد ناطق‌نوری، رئیس اسبق فدراسیون بوکس و نماینده پیشین مجلس در ۸۹ سالگی درگذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/692875" target="_blank">📅 13:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692874">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgZQjCIzKOqxxzXQzFOHxNjqBcqJqvCG6kAsicNbJyvkklQcM1R3kCy5NXJ-2IMMd8sPQcYM7wsuKgKTJrtocXdePCQEMxyZ5psaaL6vQdOZ1YT7fnu-eYw-Qw0i8nWJuctq9tHNNb3XmPsOU9wNziehCutpJzJeMvvcPecNMEQkwVj6SDyjMoy60I-lfRSi_rdyntx114ai5gpl4pUVyRBXzbin3tCoU5iaLWVIEQiEImIH0Y3R1DPzeysFopHyhWtWvXYe2FdjTW29RgilUFXfZWL182Lw2Djdvx5AP4VnML_NMc4wfEmrbMJXCmL3OPOXc7Ago_UF4YhnkIxh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
جمعه‌ها، دل بیشتر هوای آمدنت را می‌کند...
قاب کتیبه «یا صاحب‌الزمان (عج)»؛
یادمانی از انتظار، امید و ارادتی که هر جمعه تازه‌تر می‌شود.
✨
مناسب برای خانه، محل کار یا هدیه‌ای معنوی به دوستداران حضرت ولی‌عصر (عج).
💸
قیمت اصلی: ۲,۱۲۵,۰۰۰ تومان
🔥
قیمت ویژه: ۱,۸۷۵,۰۰۰ تومان
⏳
موجودی محدود
📩
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
اللهم عجل لولیک الفرج
🤍</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/692874" target="_blank">📅 13:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692873">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
امام جمعهٔ موقت تهران: نطق رئیس‌جمهور در سازمان ملل انصافاً نطقی منطقی، حماسی و شجاعانه بود؛ به‌گونه‌ای که سازمان ملل را به دادگاه تبدیل کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/692873" target="_blank">📅 13:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692872">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
برنز به تیم بسکتبال ۳ نفره مردان ایران رسید
🔹
تیم بسکتبال ۳به۳ ایران در دیدار رده‌بندی بازی‌های آسیایی موفق شد با نتیجه ۲۱ بر ۱۰ فیلیپین را شکست دهد و به مدال برنز برسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/692872" target="_blank">📅 13:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692871">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dda635642.mp4?token=W4ioXVVHBmVRoGwC-uzZyC3yBjEU5QPHv_eIKNOx0nLu3NTeFXCh2oqxuuZpHsAnwJD_NEYt4rbtdrkqraMhkjqWxhb8T2S_Z2Ri5mNMCj907NhEz5iLyalh5PkrjEcl8LbyLijqtWON7RjUt_wsvy1YDXTExxdpp-GIhHuhG478KEbWAMSJWQ969AtXohhVpVHG93ZDaU_Ctkj-UR9mrJ9IHI1MTkKD6JrVIhfMS6ojTcqHwaHvyP82ttTyErquxFHaH8chzTdGmIOg4FAkzYUoPuiZYETt2MGWB7RDwS1Gg93ypIbLe99ftz8RD7P_KLZX5Np8jEvN-hshMZmwJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dda635642.mp4?token=W4ioXVVHBmVRoGwC-uzZyC3yBjEU5QPHv_eIKNOx0nLu3NTeFXCh2oqxuuZpHsAnwJD_NEYt4rbtdrkqraMhkjqWxhb8T2S_Z2Ri5mNMCj907NhEz5iLyalh5PkrjEcl8LbyLijqtWON7RjUt_wsvy1YDXTExxdpp-GIhHuhG478KEbWAMSJWQ969AtXohhVpVHG93ZDaU_Ctkj-UR9mrJ9IHI1MTkKD6JrVIhfMS6ojTcqHwaHvyP82ttTyErquxFHaH8chzTdGmIOg4FAkzYUoPuiZYETt2MGWB7RDwS1Gg93ypIbLe99ftz8RD7P_KLZX5Np8jEvN-hshMZmwJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند دمنوش فوق‌العاده برای سلامتی
🧋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/692871" target="_blank">📅 13:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692870">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ماجرای خانه‌نشینی احمدی‌نژاد از زبان قاضی‌زاده هاشمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/692870" target="_blank">📅 12:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692869">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران: در صورت حمله جدید، تسلیحات متفاوتی را به کار می‌گیریم
🔹
شناورهای آمریکایی از محدوده تنگه هرمز ۴۰۰ کیلومتر فاصله گرفته‌اند؛ این یعنی پیروزی بزرگ ایران.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/692869" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692868">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0893dbc.mp4?token=T6rowx8kkHqkhKycb_Zq5tyy1p6AkZS3thK7gtszA6F1OyZiIPigA2itf9kVEX-_bYrObi_JgMk1o-FPnQatgGysBnPRLr1ha3tnN9huuAatT-lzklOrhtslWppOk7VGIA_2holk1lCvJy4bFAeRjZicpKHu3breqvgPG4h0vF2SbflbTMA8Rcol7xrtXCJg1DD1iFBgYcUcakDxRgLiCQ-2uIUQQJq868S8KADHTT1kRg7LIg16sAwfOXiOz70r-iHxyK0hRhv5LyTZs-kkJc-3-l2uiJ4ejTHk4uuqFPky70dO8TeKzcB08nJ_p1chrfb8qof5_u0v8VEw52cBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0893dbc.mp4?token=T6rowx8kkHqkhKycb_Zq5tyy1p6AkZS3thK7gtszA6F1OyZiIPigA2itf9kVEX-_bYrObi_JgMk1o-FPnQatgGysBnPRLr1ha3tnN9huuAatT-lzklOrhtslWppOk7VGIA_2holk1lCvJy4bFAeRjZicpKHu3breqvgPG4h0vF2SbflbTMA8Rcol7xrtXCJg1DD1iFBgYcUcakDxRgLiCQ-2uIUQQJq868S8KADHTT1kRg7LIg16sAwfOXiOz70r-iHxyK0hRhv5LyTZs-kkJc-3-l2uiJ4ejTHk4uuqFPky70dO8TeKzcB08nJ_p1chrfb8qof5_u0v8VEw52cBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاکلیدی متا، ابزاری مجهز به هوش مصنوعی
🔹
شرکت متا، مالک فیسبوک و اینستاگرام و واتساپ، جاکلیدی مجهز به هوش مصنوعی به نام میوز چارم را معرفی کرد که دارای نمایشگر ۲ اینچی، دوربین، میکروفون و حسگر اثر انگشت و قابلیت 5G‌ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/692868" target="_blank">📅 12:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692867">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33232af0f9.mp4?token=bMXiKAnYYFxTJjPEifIsnTMALCvPtOvJ6eEss4U8r11W85F29tOvYeBfuZVbQgc454jS7gptZz5ajexHhWY_Av6WmVysMTaCyW4ZiVqCPUp6skgtFb3VC1nYn6PheiLFzd-uIBeq3epAlYspy6IgIyiMZf-CakcL5oheyz3HQnWX9VKb-nki4_BSz0p08WWAE44uSjFE-U0R8L9Eoq0O-rGy-v1lPXLw7OqaoC9EchnpkokubAv2u-4YDwvZh4hSfCtUJLqN7OWk_yL9fQqns54U4a2VjYbrD4xYQyPvxP8OTcHktt2dKTFcrUoUO9FK9mCIik13DOyRqZzlqYh3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33232af0f9.mp4?token=bMXiKAnYYFxTJjPEifIsnTMALCvPtOvJ6eEss4U8r11W85F29tOvYeBfuZVbQgc454jS7gptZz5ajexHhWY_Av6WmVysMTaCyW4ZiVqCPUp6skgtFb3VC1nYn6PheiLFzd-uIBeq3epAlYspy6IgIyiMZf-CakcL5oheyz3HQnWX9VKb-nki4_BSz0p08WWAE44uSjFE-U0R8L9Eoq0O-rGy-v1lPXLw7OqaoC9EchnpkokubAv2u-4YDwvZh4hSfCtUJLqN7OWk_yL9fQqns54U4a2VjYbrD4xYQyPvxP8OTcHktt2dKTFcrUoUO9FK9mCIik13DOyRqZzlqYh3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های عجیب رزیتا غفاری در مورد مادرش: زیباترین لحظات زندگیم، لحظات از دنیا رفتن مادرم و پذیرش مرگ او بود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/692867" target="_blank">📅 12:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1746d180.mp4?token=l_Xx5iB5DIsBtrJpOsbuGhFo02QokTj21G4aurzwQuZfCTbBPzr5Ewtj2BWXnGnOqVm5sgRm5Gi0lVtb-rVdlNrg4LUdkfiH3Sm-O83T95MMOLVVU3kQsp5sDq1l88ynZtQBGaWQc05YSLMinJnIpKYrZtkGqmAxyVkiMO0oNxfcLU9-dPshCGEVU5ugeyAdPixGnI1G-rhMqJhQ9h1jK-hPcMjIRPbyux5TMS6CsVI0GcX5VgqFaEN44tpmkBvGyZgpcrn0UhIQh8Z_y_2zLWN7gd8_bQ6CPjrIQEKNoJ8aBlNrjAlDqSU0Mg9NR05FVUfdi_UpUBU13MYjHgeQMwPODuopD8HgTQEYNdBasDdFd0G9RfUk27mfTPLwKq21H__o51xncpqWi0HRWN-fUUvrLeT02eEJgZiLkC0W3DejOcri9eCT_CqQLio7T2T40YY1eDjIzhKNT9I0MD5SwHHdm8PF6unJ3gnjv_O8VJnLcMUlVPabCzS-CW_lKxW7zO16dJauK9IKtsdMoAQC875hyaauc1NIALPokyvdXv4pjWpBkjAJabpGTO2Z2N3t25AWWLHbIzyM97GeOKJgvFx39wqM9hJ5ckRz6_CAajmFc_vGDTDPD67iQG3YNiYKkS0-PIbVUYRyP3ef5INZ3_unSRspC9Md3EpwADt8ImY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1746d180.mp4?token=l_Xx5iB5DIsBtrJpOsbuGhFo02QokTj21G4aurzwQuZfCTbBPzr5Ewtj2BWXnGnOqVm5sgRm5Gi0lVtb-rVdlNrg4LUdkfiH3Sm-O83T95MMOLVVU3kQsp5sDq1l88ynZtQBGaWQc05YSLMinJnIpKYrZtkGqmAxyVkiMO0oNxfcLU9-dPshCGEVU5ugeyAdPixGnI1G-rhMqJhQ9h1jK-hPcMjIRPbyux5TMS6CsVI0GcX5VgqFaEN44tpmkBvGyZgpcrn0UhIQh8Z_y_2zLWN7gd8_bQ6CPjrIQEKNoJ8aBlNrjAlDqSU0Mg9NR05FVUfdi_UpUBU13MYjHgeQMwPODuopD8HgTQEYNdBasDdFd0G9RfUk27mfTPLwKq21H__o51xncpqWi0HRWN-fUUvrLeT02eEJgZiLkC0W3DejOcri9eCT_CqQLio7T2T40YY1eDjIzhKNT9I0MD5SwHHdm8PF6unJ3gnjv_O8VJnLcMUlVPabCzS-CW_lKxW7zO16dJauK9IKtsdMoAQC875hyaauc1NIALPokyvdXv4pjWpBkjAJabpGTO2Z2N3t25AWWLHbIzyM97GeOKJgvFx39wqM9hJ5ckRz6_CAajmFc_vGDTDPD67iQG3YNiYKkS0-PIbVUYRyP3ef5INZ3_unSRspC9Md3EpwADt8ImY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نان رول سیب‌زمینی با پنیر، ترد و خوشمزه
😋
مواد لازم:
🔹
سیب‌زمینی پخته
🔹
پنیر موزارلا
🔹
فلفل قرمز (پودر)
🔹
فلفل سبز
🔹
نمک
🔹
آب لیمو
🔹
نان تست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/692865" target="_blank">📅 12:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سفارت مالزی در ایران: پرواز مستقیم ایران و مالزی برقرار است و به‌ دنبال بازگشت ایرانی‌ها هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/692864" target="_blank">📅 12:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
متهم پرونده اخلال در نظام ارزی کشور در پیرانشهر به اتهام رفع نکردن تعهدات ارزی ۴۲ میلیون یورویی و فرار مالیاتی ۵۴ میلیارد تومانی دستگیر و با قرار تأمین کیفری روانه زندان شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/692863" target="_blank">📅 12:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692862">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNXujUoFw2GBgsHtd527XTIc7Q7yHI3xDk66FAlZiMoHE0uCihPi45mPLzkWD09CtKTxZchnpaJznUamvKxpfsbtXDvx4z8FhkBqhG3DY-3hCSEoFKSsfmEwKkxmOgvdZpv-Ly0wjg2N34RE8M6P8mAHB_OIiKVppWD61NHaGC8LGSgr7t3V9WfTBEMfb-wYWg1j4BgggZpuR4xqwkZH33dRe0hfmkA8w291dj9puJqYZfDIuG0JNLuwQxZbM04F-li1JLskU9RX28VdcCCMC2OmZht8Qu7ZXl45sGpCNVOD-useAdPNJ87IjFDwHRYbxHXlvRbZm-dL2cCeXdz8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری پربازدید از صندلی فرسوده مجمع عمومی سازمان ملل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/692862" target="_blank">📅 12:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692861">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqWWBePmxXny-rkkDxyM3e7nPcGLyu8wy56C9bqJxqz4gMYMIkXL2GWQhhXpsdzW3Ggi5KU_H_2tkMCOWcbrUs12PgSuuWbAvN2yqfZnuNRFAEyLVRMGhMOSFNY71dcx6cNVxWC--a0CfwwIY1GFs0NKr373jJ2O6P_bVzpPV3Jah9pVqdzcCig28KMqn6WpKSFnkb_IlVW-Np1g7f9KusXZA5V-wgkNIy2FgcMraooKq8cDXn8hEz2JXcLK7qJywFeh8dnLTAu3_sHx55fqWRq8Hp8NZYqKMVOj0rYzjz_IiNOjfk4bAsntNLeApx4UrisRPDwXBP_mNMPiw6Q-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
دعوت به مشارکت در بررسی چاقی و سبک زندگی
کمتر از ۲ دقیقه از وقت شما می‌تواند به شناخت بهتر نیازهای افراد در مسیر مدیریت وزن و درمان چاقی کمک کند.
از شما دعوت می‌کنیم با تکمیل پرسشنامه «سنجش چاقی و عوامل سبک‌زندگی» در این بررسی مشارکت کنید.
🎯
پاسخ‌های شما کمک می‌کند نیازها و چالش‌های واقعی افراد بهتر شناخته شوند و مسیرهای مؤثرتری برای درمان چاقی طراحی شود.
⏱
زمان تکمیل: کمتر از ۲ دقیقه
برای شرکت در این بررسی، روی لینک زیر بزنید:
👇
https://survey.porsline.ir/s/yNDyEfGR
https://survey.porsline.ir/s/yNDyEfGR</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/692861" target="_blank">📅 12:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8066ae876a.mp4?token=QQQcfwlLG56wF--PCQSQog0HY-DuHuRENHmMAY5tXMpnW0WoHCKew4qJTkOK_aH7ixb8wSc_ZZ9lZrmlP2vnkE5vRoVkb1XhAh8pUMsNNFWB3gOi774wrQ_MDOa5MOg3Re0gObE-bfKBCD6a1z9I_f79tgT7C8GXBL5VZWWkjj-xKi2yi4yC3uvD399QFw2-tLUya7GL6Gt1td6y5xtlyujTXfmMLqc4U5Hdpw7S4gZlZF08K6hHIEwLjzFIwSRDkWzpCglItbKyFGXT2cVOh1Ip2g4vODcLdOdEI_oKY4hhHM0cV6lH8QfUCHg7xoUBakcjWSmKb0yKHI9BQ3-F2mI8FdpywedXvgju1HMhrFktJzdTkhNjPtv77Y0saIJR4xi6XK5riBQeV6KcQqYjSiQiTtMLDpHx81FIYTHfFTCcoWT5a6NbD2yckQHAoAVkcv0hwFzLgh-DqFsKANMmhUazdpL55i2q09789Dn5HfhvrraDu-9ePUg0H-uDbJjqlLHtsZjMqqSSTJkiYzrm3EE59LDsQf-wpch9rOOGLzM4MqEP7dTXmVR12orXcY4WYGowMtzZb4ZxnyWHy4U2ga4o3Wp0K1lT9tYAP282_Szjl0jSby3wLrY0GomWnL-2qo1PMCRYyt7A0U4E2jMshvSE6ILwTxuAF3umAQsXpdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8066ae876a.mp4?token=QQQcfwlLG56wF--PCQSQog0HY-DuHuRENHmMAY5tXMpnW0WoHCKew4qJTkOK_aH7ixb8wSc_ZZ9lZrmlP2vnkE5vRoVkb1XhAh8pUMsNNFWB3gOi774wrQ_MDOa5MOg3Re0gObE-bfKBCD6a1z9I_f79tgT7C8GXBL5VZWWkjj-xKi2yi4yC3uvD399QFw2-tLUya7GL6Gt1td6y5xtlyujTXfmMLqc4U5Hdpw7S4gZlZF08K6hHIEwLjzFIwSRDkWzpCglItbKyFGXT2cVOh1Ip2g4vODcLdOdEI_oKY4hhHM0cV6lH8QfUCHg7xoUBakcjWSmKb0yKHI9BQ3-F2mI8FdpywedXvgju1HMhrFktJzdTkhNjPtv77Y0saIJR4xi6XK5riBQeV6KcQqYjSiQiTtMLDpHx81FIYTHfFTCcoWT5a6NbD2yckQHAoAVkcv0hwFzLgh-DqFsKANMmhUazdpL55i2q09789Dn5HfhvrraDu-9ePUg0H-uDbJjqlLHtsZjMqqSSTJkiYzrm3EE59LDsQf-wpch9rOOGLzM4MqEP7dTXmVR12orXcY4WYGowMtzZb4ZxnyWHy4U2ga4o3Wp0K1lT9tYAP282_Szjl0jSby3wLrY0GomWnL-2qo1PMCRYyt7A0U4E2jMshvSE6ILwTxuAF3umAQsXpdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیمای ایرانی محدودیت هوایی آمریکا را دور زد
🔹
روز گذشته هواپیمای شرکت وارش به علت محدودیت هواپیمایی کشور واسط برای رسیدن به تاجیکستان یعنی ترکمنستان، مجبور به بازگشت به فرودگاه امام‌خمینی شده بود.
🔹
حالا خلبان این هواپیما در ویدئوی منتشر شده عنوان کرد که با همکاری‌ها و بررسی شرایط، انجام مجدد این پرواز به مقصد تاجیکستان موفقیت آمیز بوده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/692859" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/692858" target="_blank">📅 11:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18d6e2a15.mp4?token=uMOkrjAaYcQ-sal4lesu-sshS8sLcb0E_E7t0dUWawKcaZf8CVkqsb4RX_j72SPHVvNr9ypVaB_nCUEOsaHFBV8Hd2HRZO7i8pgQMcVOCZ6NwtiaeXpKURIErwENwBr5j0DNEYPj3UNKLsLEpB02t3uxaM0Cn3XvLRZlIg3d8vGFSeUFcFy2d2SJo3dGSdTiw9Ia04WylAmTN9KvGHiRvZNFI9WnaWVRE5syFH4XwOgj_MDxoQ81Hx0cEXST07HOIGGhlKRtyJQvljVpNPN2hjBcclGes-vuIS79nFaKduluGRA9FDImFudtITiUnfxK6F_six1b_cY91rqu7311gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18d6e2a15.mp4?token=uMOkrjAaYcQ-sal4lesu-sshS8sLcb0E_E7t0dUWawKcaZf8CVkqsb4RX_j72SPHVvNr9ypVaB_nCUEOsaHFBV8Hd2HRZO7i8pgQMcVOCZ6NwtiaeXpKURIErwENwBr5j0DNEYPj3UNKLsLEpB02t3uxaM0Cn3XvLRZlIg3d8vGFSeUFcFy2d2SJo3dGSdTiw9Ia04WylAmTN9KvGHiRvZNFI9WnaWVRE5syFH4XwOgj_MDxoQ81Hx0cEXST07HOIGGhlKRtyJQvljVpNPN2hjBcclGes-vuIS79nFaKduluGRA9FDImFudtITiUnfxK6F_six1b_cY91rqu7311gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلعهٔ کَنگِلو؛ عقاب پیر مازندران
⛰
🔹
قلعه‌ای باستانی بر فراز کوه؛ یادگاری از اواخر اشکانی و آغاز ساسانی است که از حمله مغولان جان سالم به‌در برد و بنا بر روایت‌های تاریخی، کارکرد مذهبی زرتشتی نیز داشته است.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/692857" target="_blank">📅 11:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=RxeQc5OP2E5tdZm1Xs_CYxYtaFe6Jqrah2TR1agl9vZiMUUG3GOhGpatXWiFHbIuYBaeaKFVBhtz1UbyzwKuzVOsJPgwwGMgJaC-jQiYVkeoHTcM8wFQ7lXM8hKbx0IBtBYfUlEimBMdHaSac2AfWRbsP5JbzwYVQ0rzgK72FMrrRnWX0Pj6qZ19hGKfG-J4EzPL2E7lCwqEXbw4Lh7qeEAvqrIvX2Ad4Dj4SAMTiahCLOh557jt0eSdaRIDkkUvivxVRY_VZ5n2uQmCFM-dFneG_BQqBXrwO47300-JzJl4Oe9oHpnZ3Q-TUUJ4HoE0xCuI12bzZf212dn1LZGNmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e294a0242.mp4?token=RxeQc5OP2E5tdZm1Xs_CYxYtaFe6Jqrah2TR1agl9vZiMUUG3GOhGpatXWiFHbIuYBaeaKFVBhtz1UbyzwKuzVOsJPgwwGMgJaC-jQiYVkeoHTcM8wFQ7lXM8hKbx0IBtBYfUlEimBMdHaSac2AfWRbsP5JbzwYVQ0rzgK72FMrrRnWX0Pj6qZ19hGKfG-J4EzPL2E7lCwqEXbw4Lh7qeEAvqrIvX2Ad4Dj4SAMTiahCLOh557jt0eSdaRIDkkUvivxVRY_VZ5n2uQmCFM-dFneG_BQqBXrwO47300-JzJl4Oe9oHpnZ3Q-TUUJ4HoE0xCuI12bzZf212dn1LZGNmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب قهرمان کاراته پس از ورود به ایران
مرتضی نعمتی:
🔹
برای گرفتن معافیت، تظاهر به داشتن اختلالات روانی کردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/692856" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436787d0d.mp4?token=XA9w0VDu28Ke10p6Eedm_82gUv6sincpiBlan1478k1PJJ1l1uNQBg8myMYp_z7Lm-iSLsettqhGN4SldlN3QPhD9003rGJ-w1GZMJbXHUFI4elG5wZkceujWpbr_rnB4BafcdNYxUAjwF1f3oMu5uSS95IYlZMnNxkBC1BJZx14iWueUMxcNtvcC2pUYA70OdEfd3DXdbcgPR0owHo4B072Qran1S6Nwdf76jRwXzbUYvKBgKSwtU6tJTAFOI_7Pi7GWl6veD6uO8sokpjZMjep1kKM1aZDZaJBBJ4CTRAMN31ea2lmM8cWftcP1Pak6I4F5purqy1RWK0EzimwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436787d0d.mp4?token=XA9w0VDu28Ke10p6Eedm_82gUv6sincpiBlan1478k1PJJ1l1uNQBg8myMYp_z7Lm-iSLsettqhGN4SldlN3QPhD9003rGJ-w1GZMJbXHUFI4elG5wZkceujWpbr_rnB4BafcdNYxUAjwF1f3oMu5uSS95IYlZMnNxkBC1BJZx14iWueUMxcNtvcC2pUYA70OdEfd3DXdbcgPR0owHo4B072Qran1S6Nwdf76jRwXzbUYvKBgKSwtU6tJTAFOI_7Pi7GWl6veD6uO8sokpjZMjep1kKM1aZDZaJBBJ4CTRAMN31ea2lmM8cWftcP1Pak6I4F5purqy1RWK0EzimwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: مشتی احمق را برای مذاکره با ایران فرستاده‌ایم!
سناتور آمریکایی:
🔹
ما بخشی از احمق‌ترین آدم‌های موجود را به اتاق مذاکره فرستاده‌ایم. ترامپ باید کمی فروتنی نشان بدهد و بفهمد قرار نیست آن پیروزی بزرگی را که آرزویش را دارد به دست بیاورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/692855" target="_blank">📅 11:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpmMK5LWM84XJQnpcYe1_GDIMZt5wLJFaVrYc6hjBuorVfWM6Xa3HWKUSSiIyZ_T6dfNUUmqTKVf-_IUZPwUEoHkCqpa38gf4ZnAMJgettBJzNlWnqoky50gBeiCtPICS1zw8WK6gQhS-pnX96_Fi0bdIEq77ON6N59vp_zHIuMiIvaTnzhK7capu1BZjadFauu3Iu8ncDyyN_GiFL_MMRIO07VCg6JH9cpOuB0KrSsvobJLR6_nyWHwUKJ8VI0TKINMr9W5_osQA5ns0l4xnpIFXcW6m8xT2BowfUKQAkTFJkSad3MStAwq5jGG71XhdJzY6X3A3i68_ARqj_Gwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترند جدید؛ تصویر را برای ChatGPT یا Grok بفرستید و پرامپت زیر را وارد کنید
"Fill the bag with things that resemble me"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692854" target="_blank">📅 11:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS4bkWFZu_ZOE5j_njO8ojFhQ8I-IIly0kPwe9oZ2Y6j7N6q2PGSl06RrzH32zMKWxPdLE0Vpke9ATJ_xJnb1P6NxvFlmxwf3-KGvVsTn09xM3p3vCvPkXMoFNbERZA8Pb918DHfX80-pRf03e9MTdzEZ7Nu1bkgg3lZDfK4GstxQz5LVEmUxP5QppycQtNw5AH4V95fhRJY3gET9PKHU-WgmyJHk5Wz2XfuOxeo0LGqceOdN-LVK5Vl6dgQWRmJw5XRmNmIRhk6zpf8G7y-S1ZTHjmUY1QnBOhjYWUzHIBYYPXzik2cgmbbG-3sOHWy8oRfbg8j_b358u-yPVLWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند نرخ باروری کل کشور
🔹
بر اساس آمارهای مرکز پژوهش‌های مجلس، نرخ باروری کل در ایران طی سال‌های اخیر روندی نزولی داشته و از ۱.۵۸ فرزند به ازای هر زن در سال ۱۴۰۰، به ۱.۴۴ فرزند در سال ۱۴۰۳ رسیده است.
🔹
این در حالی است که طبق پیش‌بینی برنامه توسعه هفتم، نرخ باروری کشور تا سال ۱۴۰۷ به ۲.۵ فرزند به ازای هر زن افزایش می‌یابد.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692853" target="_blank">📅 11:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692852">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59fbb714f.mp4?token=ep5zwFGkG6Hk9GR-aaKITVgMDy_OJ047YV-zr2p7GXBJa7yuIVK1D1FhGV54Vj7wqMwv7G5_C4r4om53q1RUXZ39VwCN4HkK5ONJWlUUXc_WlbrdIo_kLayMYY56Gnh26rBJTxUmNEoJGSgBaa_GW88_CqQ_WYmvd7xAeytWgr-XmutDM_U93QMSQEUNo2yKarefG2Y1eAEd-gRaeqSbyDp1WgenD1vydgVq62AKZ_d8IkbOiCa1046oO7iHyYW9NKhBy6uy9psi_YPqkKkOECiYEZ1QZL4IkHl9EUc5FWw40ahZJXKddp_RofaEW_rInwo4FM9Nl5m7tmEzoIMdyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59fbb714f.mp4?token=ep5zwFGkG6Hk9GR-aaKITVgMDy_OJ047YV-zr2p7GXBJa7yuIVK1D1FhGV54Vj7wqMwv7G5_C4r4om53q1RUXZ39VwCN4HkK5ONJWlUUXc_WlbrdIo_kLayMYY56Gnh26rBJTxUmNEoJGSgBaa_GW88_CqQ_WYmvd7xAeytWgr-XmutDM_U93QMSQEUNo2yKarefG2Y1eAEd-gRaeqSbyDp1WgenD1vydgVq62AKZ_d8IkbOiCa1046oO7iHyYW9NKhBy6uy9psi_YPqkKkOECiYEZ1QZL4IkHl9EUc5FWw40ahZJXKddp_RofaEW_rInwo4FM9Nl5m7tmEzoIMdyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعجب مجری شبکه آمریکایی از اعتماد به نفس نماینده ایران موقع سخنرانی تهدید آمیز ترامپ
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/692852" target="_blank">📅 11:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879dae5f66.mp4?token=v-9-2fzbuGGmGaID0yyBAIEUqb_QfvdDABRHUhX9I-vmRRERxhoQWVzzr3XxiESKG8sXTvQFvbQJ5hrUG19V5ebdDU773tIP_u5LQiQJ0FujA1yR8RRJ_r9FDQS03_QQSH0Sfd3tRDkcU6tcrPbop7tQ2AqaT5NiXolOniotrwUdcCiOUUbmyKvq6d9e96G0u0s9Pb25wyqcT20vxKwKxm5fay6tRLL18MNVgBxlTz7L46FtQvrgJwSq_aRRTQUSPSj9aGRWGEl1x7vkVAOVg0ebn-d9Ff8-VQziMlx4WwLKYe-pWwEO_q5NWpJ-BgcHweY1HZ_Q_8VIWnGD55TIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879dae5f66.mp4?token=v-9-2fzbuGGmGaID0yyBAIEUqb_QfvdDABRHUhX9I-vmRRERxhoQWVzzr3XxiESKG8sXTvQFvbQJ5hrUG19V5ebdDU773tIP_u5LQiQJ0FujA1yR8RRJ_r9FDQS03_QQSH0Sfd3tRDkcU6tcrPbop7tQ2AqaT5NiXolOniotrwUdcCiOUUbmyKvq6d9e96G0u0s9Pb25wyqcT20vxKwKxm5fay6tRLL18MNVgBxlTz7L46FtQvrgJwSq_aRRTQUSPSj9aGRWGEl1x7vkVAOVg0ebn-d9Ff8-VQziMlx4WwLKYe-pWwEO_q5NWpJ-BgcHweY1HZ_Q_8VIWnGD55TIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل متحد درباره نتانیاهو: سازمان ملل متحد برای حفظ صلح و اجرای عدالت تأسیس شده است، نه اینکه به بستری برای جنایتکاران جنگی تبدیل شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/692851" target="_blank">📅 11:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b117449cfe.mp4?token=QVm638ANhP8tf0OzPsWziaEoDWx7TU1gNCh-MSlTZryR9-jGcqB2Z420siyGAk8Olu_dtO5tjQbhSFYOa2WAiq0BxDOH_OywcFkL6qrxUDGrfHMk2FhMq8nQe3-iuad4QXhT84eXWHN7IG74fQ4eJJGzKfinMvr-vjgVsK4nH_p9ZIW_E1X9T8Fosg2FlALtdyfZmBx_LNLPHJuXA53JywFLreP2ThuWUkDNzq6wvahpKxSFE_C_VoxzTFFO6sQ_CRGBHxS7y2ylGTwh5fb8yHoYqzXqACKysc6IbI3V3A6plXqJgqjZfWN5hCnnUo7ZxhwFDBHUSOTpdsIqvBT7WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b117449cfe.mp4?token=QVm638ANhP8tf0OzPsWziaEoDWx7TU1gNCh-MSlTZryR9-jGcqB2Z420siyGAk8Olu_dtO5tjQbhSFYOa2WAiq0BxDOH_OywcFkL6qrxUDGrfHMk2FhMq8nQe3-iuad4QXhT84eXWHN7IG74fQ4eJJGzKfinMvr-vjgVsK4nH_p9ZIW_E1X9T8Fosg2FlALtdyfZmBx_LNLPHJuXA53JywFLreP2ThuWUkDNzq6wvahpKxSFE_C_VoxzTFFO6sQ_CRGBHxS7y2ylGTwh5fb8yHoYqzXqACKysc6IbI3V3A6plXqJgqjZfWN5hCnnUo7ZxhwFDBHUSOTpdsIqvBT7WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه باتری آیفون ۱۸ پرومکس و شیائومی ۱۷ پرومکس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/692849" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dfff167.mp4?token=klQ5WwFb1pFdBXiioJdJGtRN7Wuz_RhC3OSlsyzk7r9l4o7L-FWRSeebJnnYIrEkRUFW35NB73GzTgDmGHL9qcrLd7YLbOg1cNTU-C2pOdcXQINlS57T1wYVmsyWDWX8Rlw-pBjCeYOIT85d8bgJK0PWccsYZgPd1cJKu1Wc-aTdjXHZLtuLpu58uJ5JP3cjrH28N9M3rrBSdu2Bpou7-3mcvh6gCOpW4wsvF23OGwmvbKatMpgziyQVA74SBN8c1Sb1-zLILmBqOJevn4ni5J3yr2QQnAwIJbL5glzR9PF6O-_z26uCUPiAsXO1wC9A0sIH2YvgzVWQAMg2fHRQJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dfff167.mp4?token=klQ5WwFb1pFdBXiioJdJGtRN7Wuz_RhC3OSlsyzk7r9l4o7L-FWRSeebJnnYIrEkRUFW35NB73GzTgDmGHL9qcrLd7YLbOg1cNTU-C2pOdcXQINlS57T1wYVmsyWDWX8Rlw-pBjCeYOIT85d8bgJK0PWccsYZgPd1cJKu1Wc-aTdjXHZLtuLpu58uJ5JP3cjrH28N9M3rrBSdu2Bpou7-3mcvh6gCOpW4wsvF23OGwmvbKatMpgziyQVA74SBN8c1Sb1-zLILmBqOJevn4ni5J3yr2QQnAwIJbL5glzR9PF6O-_z26uCUPiAsXO1wC9A0sIH2YvgzVWQAMg2fHRQJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: اردوغان دیکتاتور است/ آخرین کشوری که دروغ‌های یهودی‌ستیزانه منتشر می‌کند، ترکیه است. او می‌خواهد بر سوریه مسلط شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/692848" target="_blank">📅 10:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692845">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0HxjnPHe2WhbnOwphltTVw0OoqcERuWcQR28HTg04NlbDucNtRSfbxgTcUL4T-bKk0HUBiIMLnUcbnBOmDnp0Hp_Ia0f6FlPIs8lGwluaC3NIV_GMkluJ6FbV3VPwiOvo8xOVxUglEk-uScdiMX389iHiX3Y3rWO2GsCrKUmyyDlcqLYNn1ftYqEWn5P6YC7J-CQAHwtarxFOdvblmJ8XLGoUuTG9vshfd4t8aBdLZRwwLGpPQpIXNhoHaVWZP8_vGwiAjNlNlg3T97_Ejo7R2N-ek6_CIuxET92PAqP1A1ThwYHMigR5z21ZtiTsE1c07nGZbO4lj7K8qZPsMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش غریب‌آبادی به ادعاهای نتانیاهو در مجمع عمومی: تاریخ درباره جنایت، اشغال و تجاوز قضاوت خواهد کرد نه نمایش‌های تبلیغاتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/692845" target="_blank">📅 10:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692844">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsBwVyoONWVMWPiOoYlqUoamGEg9_5oPn6Pdhwf8PLSWIQnTlY7NBB4cXBHaUgt1ZrcsQUwuOVfUQ3lndeR3dlGHXBrsihGJWGvBYYLqCMxcEELJjCF387RfaMj5y0JMQtjsK9zhFsFGvrAH_vlvf2ix02RpZiPdRzjy79oDUFwEYO6uqIqL4bHdY2I1L_HmkyOdUmmA8PckNOVZx9Vu4BmRdD602vzt4-o_kZOrkOtuBjxv4o0e3IL7fjURsZxu5dI8M41dWShJKJDnziZ0Z2zs-LPFfruRQSySo-VCFYdVPUF_kwyoo2hebNPQdpwhoXBb348q_5NuxyQc1VtdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
افشین خانی در مراسم آغاز سال تحصیلی مدرسه استثنایی پویا تأکید کرد؛
✅
بانک صادرات ایران در کنار کودکان استثنایی خواهد بود
🔻
همزمان با آغاز سال تحصیلی جدید، افشین خانی، مدیرعامل بانک صادرات ایران، با حضور در مدرسه پسرانه استثنایی پویا، زنگ بازگشایی و آغاز سال تحصیلی این مدرسه را به صدا درآورد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692844" target="_blank">📅 10:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692842">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOYfqwNTwjXTlok4zPvRZmzllgpKVRoZxluXZLEzQ2jA6wEhpNAuq5uqR03si3I3BeBZ8vzWPhZL0_-R_GXK5wpM0T-w8wuv0nYcqDoeRyWjO9G1QDxBWxElXIeJRKvFqM6u8duUGbpOPI448Gd4SJYP4RNsiR0AB3zR7CDjXLG77kHragycEx0Hf-Kj4zyiO_nRVw9jO9xF2_sGjyjGlmNSJccJO8xXWbEBa2Y6LmqRjwCSFJAOqaWcWdrXCnBMnu_TRM1Xw5UaNd7BuQBoPyAoE01b1l7MXZKcpAScfAHUW1pMHFc_jIdpPrBUpQXJFDYljA-MwHYWMZtelK5QIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای عجیب امیر سلیمانی؛ ادعای ابتلا به سرطان با روایت پلیس زیر سؤال رفت
🔹
امیر سلیمانی، بلاگر ایرانی، پس از چند ماه دوری از فضای مجازی با انتشار خبر ابتلا به سرطان بازگشت و در مدت کوتاهی صدها هزار دنبال‌کننده جذب کرد. حالا پلیس اعلام کرده ادعای بیماری واقعی نبوده و تصاویر مربوط به آن با گریم ساخته شده است؛ موضوعی که به بازداشت او و مسدود شدن صفحه‌اش منجر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/692842" target="_blank">📅 10:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46744a0a55.mp4?token=bg7puK2ev1Wr9l_4rI-uTlfBY9Am8FaJ1BQi4fOXWaxHMkmdLH95CQBxXetbFvSdqVVu64GA4Fkz-gHAQyoOVtVrsUPoAtiIZhbSDW9B9Qv51AxTVZ82AlfE7O6BCou6G3C4y-S1JWy4ibJiOOvVMflLOAcVbQGXaA6eThIMgbaGHzYxPvlCvbIcbbg-EHdNofoM9gB_eZk_uTjIaed42IInvsxDteW9hqXSPDjg02pEgp5fkBqalxL-eH5F3VI6_XuoM9t9lrWvvii4jIPOM8vWHFUfohFJyCPhIyvkLmUft8KMaNiqK1zsZFMZdCIIwHlM9kt1UDUpQ-Vslz0PhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46744a0a55.mp4?token=bg7puK2ev1Wr9l_4rI-uTlfBY9Am8FaJ1BQi4fOXWaxHMkmdLH95CQBxXetbFvSdqVVu64GA4Fkz-gHAQyoOVtVrsUPoAtiIZhbSDW9B9Qv51AxTVZ82AlfE7O6BCou6G3C4y-S1JWy4ibJiOOvVMflLOAcVbQGXaA6eThIMgbaGHzYxPvlCvbIcbbg-EHdNofoM9gB_eZk_uTjIaed42IInvsxDteW9hqXSPDjg02pEgp5fkBqalxL-eH5F3VI6_XuoM9t9lrWvvii4jIPOM8vWHFUfohFJyCPhIyvkLmUft8KMaNiqK1zsZFMZdCIIwHlM9kt1UDUpQ-Vslz0PhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای پزشکیان حفظه الله...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692841" target="_blank">📅 10:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBbVFDbqK59i2BDhBoSQUBfqFlOeUS_0pdQf1M4bS_5S-bxPHMba46zdRdYTTGXCUBfUcfU-Bk3gKbumEJvzrOxtqlvAS_aLDBp5dwmlNLRcih-1cSQQBt3KJtz5o_kMYZGeAVdeOzO9zx9gzPzOlkdnZjHmeieSM58mAM3s9RAnWRxxuuSKzn_6_guho3CJnbSlSlprw9oBOsXfSpHSOfgk8DX6GxTvPApJEnuyc7KhX0mb1rsVPnWtfddjpuHdPVNgc1KskF4O_S2-OZQP68eAqwyrsym6eAC-bg5FzXEZ24MwrYgtWVsnVorv2wCziDsuPLU7jQ8-jrCWq31OVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا آمریکا خط محاصره دریایی را عقب‌ کشید؟
🔹
تصاویر ماهواره‌ای و داده‌های منابع اطلاعات باز (OSINT) نشان می‌دهد که ایالات متحده آمریکا خط محاصره دریایی ایران را به نسبت ماه‌های قبل عقب‌تر کشیده است.
🔹
کارشناسان نظامی و تحلیلگران OSINT آن را ناشی از حملات موشکی ایران و تهدیدهای موشکی ایران علیه ناوگان دریایی ارتش آمریکا می‌دانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/692840" target="_blank">📅 10:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
«الفتی» به مدال نقره رسید
🥈
🔹
مهدی الفتی در فینال پرش خرک بازی‌های آسیایی با اجرای دو پرش، نمره‌های ۱۵.۱ و ۱۳.۹۶۶ را به دست آورد و با میانگین ۱۴.۵۳۳، تنها با اختلاف ۶۶ هزارم امتیاز نسبت به نفر نخست، به مدال نقره دست یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692839" target="_blank">📅 10:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcsTb1ZIShIheh-_iitsqhrIZVaDCBrFfIr5TdTkEEgmGR1HcnUJKJDemw2bABLcjXjMZsgG_OnWlfT9XC8Ylri-dJPe1mBLHmDe5Jvd6Vwrvq_8G1j1XAb74FOkKgxcajupFGWv-QQldgw0LTDggxDD6AXJ9Z2KpjV2ypt_6CoFS6TTOrfZNAQaahSoA027-sYgvqNp8jkFoRJmtoYG_TZQJ19yk3DO9dc8HHDgLNXCpqS5NAdgi7c-tmwTn7P0IQZY5WWgS4GhnWJ-euI41QGjmkwZHPolDBFMXa4zsGTgEJmstPTnyFMvNzn0tfPE4NQN08f8scgifcTb8MbSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه سفارت ایران در غنا به سخنرانی نتانیاهو در سازمان ملل با تشبیه به لرد ولدمورت (شخصیت شرور مجموعه هری پاتر)
🔹
«امروز در سازمان ملل، لرد سیاه برای جهان از اخلاق موعظه کرد؛ حتی مرگ‌خواران هم سالن را ترک کردند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/692838" target="_blank">📅 10:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای رویترز: مفتی اعظم عربستان از نیروهای نظامی خواست برای فدا کردن جان خود در جنگ با حوثی‌ها آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692837" target="_blank">📅 09:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
قیمت گازوئیل در اروپا رکورد زد
🔹
میانگین قیمت گازوئیل در اتحادیه اروپا به ۲.۲۳ یورو در هر لیتر رسید. دانمارک و فنلاند با قیمت ۲.۵۶ یورو در هر لیتر، بالاترین قیمت گازوئیل را در میان کشورهای اتحادیه اروپا دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/692836" target="_blank">📅 09:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
گوگل از قابلیت Live Avatar برای هوش مصنوعی جمینای رونمایی کرد
🔹
قابلیت جدید Live Avatar برای مدل Gemini 3.8 Live است و امکان گفتگوی تقریباً لحظه‌ای با یک شخصیت هوش مصنوعی متحرک را فراهم می‌کند.
🔹
کاربران می‌توانند حین مکالمه اطلاعات را روی صفحه مشاهده کنند و سازمان‌ها نیز امکان ساخت آواتارهای اختصاصی خود را خواهند داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/692835" target="_blank">📅 09:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رویترز: تردد کشتی‌ها در تنگه هرمز به زیر ۱۰ فروند کاهش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/692834" target="_blank">📅 09:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692833">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/692833" target="_blank">📅 09:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692832">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/692832" target="_blank">📅 09:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
نتانیاهو و همسرش بامداد جمعه و تنها ساعاتی پس از سخنرانی در مجمع عمومی سازمان ملل، سریعا نیویورک را ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/692831" target="_blank">📅 09:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692829">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/692829" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692828">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/692828" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رئیس جمهور چین: با ترامپ برای ایجاد روابطی سازنده و باثبات توافق کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/692827" target="_blank">📅 08:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
معاون سازمان سنجش آموزش کشور: نتایج اولیه کنکور سراسری ۱۴۰۵ تا ۱۰ روز آینده در نیمه اول مهرماه اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692826" target="_blank">📅 08:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692825">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/692825" target="_blank">📅 08:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ان‌بی‌سی به نقل از عراقچی: طرحی از طریق میانجی‌ها به مقام‌های آمریکایی ارائه شده که در صورت پذیرش، تنگه هرمز در پایان هفت روز باز خواهد شد و مذاکرات از سر گرفته می‌شود
🔹
این طرح می‌تواند به‌محض موافقت آمریکا آغاز شود
🔹
یکی از شروط این طرح، موافقت آمریکا با مسیر عبور دریایی از تنگه هرمز است که میان ایران و عمان بر سر آن توافق شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/692824" target="_blank">📅 08:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692823">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/692823" target="_blank">📅 08:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692822">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/692822" target="_blank">📅 08:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692821">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
قایقرانان تیم کایاک دو نفره ۵۰۰ متر مردان ایران و تیم تیراندازی میکس ایران در مادۀ تپانچۀ ۱۰ متر در رقابت بازی‌های آسیایی
مدال برنز کسب کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/692821" target="_blank">📅 08:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692820">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
آمریکا ۶ میلیون بشکه نفت ایران را دزدید  تانکرترکرز:
🔹
نزدیک به ۶ میلیون بشکه نفت خام ایران به ارزش ۶۰۰ میلیون دلار که پیش‌تر توقیف شده بود، به‌صورت بی‌سروصدا در حال عبور از اقیانوس اطلس به مقصد آمریکا است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/692820" target="_blank">📅 08:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692819">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/692819" target="_blank">📅 08:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692818">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/692818" target="_blank">📅 05:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692817">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irusMr0OIT_oRf-ho34D41FfZyYo4sw4IVMXhRpnVbsC4wk_ZShEF61wI1Cs9981tgaw_tRPcrwYAPzaNFQJ4us7uowsiNxuQToAGU4K5ka0bgY6Nn2L-azA3U6g0nnNs4HvRgfD_mh8hXOEJl-P5Cib6O72l4f9L_iS37mVt4vQ70Pckw1V2FUiloCJyLQ0u0BVBmhgN1KPZ_83ZKiYQlIui7cccWavpdNK6PKEyAYgGrSvi2YTDgXQJyP6PtNEcFZE7HZQNHAD9dTb2gubzLZmRMDgo0lLy6jn-eMkoLJgEMS_Jbrq9s83P0MUwEa3Bjkz3sso0YLpXzDC-XVmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به وقت خانه تکانی!
🔹
انگار صندلی‌های خالی سازمان ملل امشب  خودش همه‌چیز را راجع به منفور ترین کشور جهان گفته...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/692817" target="_blank">📅 05:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692816">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
می‌گویند ایران ابرقدرت نیست؛ اما قیمت بنزین آن‌طرف دنیا هم با اسم ایران بالا و پایین می‌شود...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/692816" target="_blank">📅 05:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692814">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/692814" target="_blank">📅 04:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYvBqMvnqI1g7vLtx-GmVd-GTc1ctiTJxWcjOgTos6mm-DZxD7ZNAOw4v4UdYOdg1LYR4NsD4IYyknNxAclO9MaqZ2z-L9kQtgfzKneA5acle0zuaJHtHi8ue3TJRz1ROrqJATNPVhcfY6y04ld7xxS0forAcMnXcwvzfoDC4WWSDYITbEStipbaQv_Xdm2QvYgp7HmMShbiyAjbRzfopbNQpPHDjRRUuZp7Z9jvlKzG0x_eDEt3F_sxVRIAsALg9A6UpBIPOso4a_0b78XrSwDVZGFyeGMz4leKD2Y_Pju8sVes_kkwTYrgO_e2LTpw-wdmh-UL6J4Yc7jyGM_ViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان با خبرنگاران رسانه‌های  آمریکایی رویترز، آکسیوس، فاکس نیوز، وال استریت ژورنال، نیویورک تایمز، سی ان ان، سی بی اس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/692813" target="_blank">📅 04:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نخست‌وزیر ارمنستان در سازمان ملل: روابط با تهران برای ما بسیار مهم است و خواهان تعمیق روابط با ایران هستیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/692812" target="_blank">📅 04:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692811">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/692811" target="_blank">📅 04:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پزشکیان خطاب به مجری فاکس نیوز: سختی ها و مشکلات اقتصادی وجود دارد، اما ما مقاومت می‌کنیم و تا آخر خواهیم ماند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/692810" target="_blank">📅 04:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز:پس آیا ایران جنگ را انتخاب می‌کند یا توافق را؟   پزشکیان:
🔹
ما جنگ را انتخاب نمی‌کنیم. جنگ به ما تحمیل شد. ما به دنبال جنگ نیستیم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/692809" target="_blank">📅 04:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692808">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/692808" target="_blank">📅 04:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC4G0CzqmHTryiCZ416sri1RjCNwk6t2aMe3p_IepWlbf4XwZo910ojZZPqULcSwdbatOruKwOQeRAEcwHTIz83G1yxqJb1LSS6VvSq4O9QFKdf_yNPxR7Kv3RnuWQPzUoax0gn_Shdzzh8znxTn4yw9i90q5cf8xKd2Kf5UQrTdBoZuS2K3rEBKuWZ2rucZMKrrz6GSlQQptG9ts2BEVij_uT8gRfs_QHeoTQPUljguxV9tahslrSBlMhuGJ7kkqCRbHp_iafAOC93UxE3hfOToHVxPr7LkUG4Cr_XKEtXTk2-MpkfWggq7Md6ronLc8iHDqSGZNm3kVW1vNq1jqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرعباس فخرآور ملقب به عباس جفرسون، از فعالین اپوزیسیون، با انتشار تصویر ساخته شده با هوش مصنوعی، مدعی دیدار محرمانه ترامپ و پزشکیان شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/692807" target="_blank">📅 04:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692806">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/692806" target="_blank">📅 04:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692805">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/692805" target="_blank">📅 04:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692804">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/692804" target="_blank">📅 04:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692803">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/692803" target="_blank">📅 04:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692802">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/692802" target="_blank">📅 04:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692801">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/692801" target="_blank">📅 04:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692800">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/692800" target="_blank">📅 04:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692799">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/692799" target="_blank">📅 04:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692798">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/692798" target="_blank">📅 04:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692797">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/692797" target="_blank">📅 04:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692796">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/692796" target="_blank">📅 00:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692795">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/692795" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692794">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ولیعهد کویت: ایران از تنگۀ هرمز به‌عنوان برگ برنده در جنگ استفاده می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/692794" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692793">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/692793" target="_blank">📅 00:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692792">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LawMoiIXkFpb74kJfOQgFN0FZJksXXRdagzF2IWw9rjh5MdcBe-p9Nu-VDcTfD21hmSk_sz6BzRm52U1JE_lVx4b4WeDBtyk_9kG5Kbfcr0wVYTLL5AmdEUD9IbL8sOb3-ec4ESS8ebFmECi5jn7KYCqnN_x5Vpp9yrjDukH0Xp-u9rvrbeILTYC0AU2f1NAz9iJ1cHgnX-Mn20ykAwce4zfKfArpJm992W_PxUig1M7WLSmJWiYsvw_1jRWymP08x0ZoD7tv9UKWFtdeMwQ67pLwsIdKO5LlmROwIuRTAsYmSS0E07Ek_nq0MxYp-1aCux0l1jCiPlmsLyq2KtFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اسرائیلی: تبریک! ما یک دیکتاتور پست و مضحک روی صحنه‌ سازمان ملل داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/692792" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: تحرکات فشرده‌ای برای دستیابی به سازوکاری جهت توقف هرچه سریع‌تر درگیری‌ها و بازگشایی تنگه هرمز در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/692791" target="_blank">📅 00:18 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
