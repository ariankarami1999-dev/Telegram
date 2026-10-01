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
<img src="https://cdn4.telesco.pe/file/twB2f5s8u8cxNRFStLaAIydVA4yvXu-8XXfU6EqeAFU8fRKfYnWIJan_V5xbIO2JS1jwU8p-RtnQc_DWSwH1eTm0pq13vqFpTnmcIwIhdIYxxqMfvGcLfSuFE3k_olntFJYSUMnsw7xl_w0lu5Aj1NlsBMkHc1ZqlqtwCue0gy6A4OKYS8mY43U1Bh1IG3Zgo5zdAAleaWYU7aksCx09uOb0dmw-GFg7Qbuu6XPGQTon3eN1StGNWkCpaJ9dCMhwrrPF1X2HKVzAb5Dc82UN4NKjBSm9JalgFBmTBHubu60UM9YuHpEg_dBVl7IkEWFzQeN1VKsjL44hria09xlhTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-72578">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=cVxq3X089acroYzxdr6yQJuqF0PcG_zR4G3WH_fQG_J6kxuLnh9I1Ck-rqtHl3s6vHGtFvwBlm6QJXBsi-auBr4pIUOU9eIDebP4-vKI6lVHtBkaosQ4Rv73lCSDhfy5p63TcUqIvEMfA6e0yphwWM9dHn9nNM5QtAbRWEqXfKcLrI_9eX42dFozumb88qXvFB38uATD-J2u0LcBQfdWISh678kHbRS1so4w4JVy44LcHweD7jHvwUtrx3mBdp4YDxnfrZvslWRmZ8HtPr61eUiItC-Gd7gHVr9KitRFximLG1P_U80nfWDdiuWC3uJr3bUqVQz9lAdsht1PSRHxxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=cVxq3X089acroYzxdr6yQJuqF0PcG_zR4G3WH_fQG_J6kxuLnh9I1Ck-rqtHl3s6vHGtFvwBlm6QJXBsi-auBr4pIUOU9eIDebP4-vKI6lVHtBkaosQ4Rv73lCSDhfy5p63TcUqIvEMfA6e0yphwWM9dHn9nNM5QtAbRWEqXfKcLrI_9eX42dFozumb88qXvFB38uATD-J2u0LcBQfdWISh678kHbRS1so4w4JVy44LcHweD7jHvwUtrx3mBdp4YDxnfrZvslWRmZ8HtPr61eUiItC-Gd7gHVr9KitRFximLG1P_U80nfWDdiuWC3uJr3bUqVQz9lAdsht1PSRHxxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات حملات آمریکا به ایران از 28 فوریه تا 8 سپتامبر ( ۹ اسفند تا ۱۷ شهریور ) :
@News_Hut
| thecuriospark</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/news_hut/72578" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72577">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=v-wdZrwkvs8IuOORtl7PPwYOAhiLuBsAbjHb1Iw6v9fF6hPbA-Uyz1IuqSjMvUVSirAct_wdAo8A1wBKDDTSoRMlcRHPjNbBf8gd9rUhdW-qvDDNJxnOf7XjEy9h-Pap9Tak_jPVdebX46FlZmfyEHIT8HStDAFA6mIF-noSUoiATvauQd6CYmmVE6D-ViRcKOQASkLkHRsVSRpBEats7Bp8f9nPSkfgrMFuCnluvqw5rO1zaRuXi6-wBHMiHH3TNPWtblrK3a4Ws1fR2zMvD6ZLzoVCW8fOh_49zeVUGrVOW5RtkZUtXEfN3x6IueLMbINzwtdHxsWJbj8BUJ-NWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=v-wdZrwkvs8IuOORtl7PPwYOAhiLuBsAbjHb1Iw6v9fF6hPbA-Uyz1IuqSjMvUVSirAct_wdAo8A1wBKDDTSoRMlcRHPjNbBf8gd9rUhdW-qvDDNJxnOf7XjEy9h-Pap9Tak_jPVdebX46FlZmfyEHIT8HStDAFA6mIF-noSUoiATvauQd6CYmmVE6D-ViRcKOQASkLkHRsVSRpBEats7Bp8f9nPSkfgrMFuCnluvqw5rO1zaRuXi6-wBHMiHH3TNPWtblrK3a4Ws1fR2zMvD6ZLzoVCW8fOh_49zeVUGrVOW5RtkZUtXEfN3x6IueLMbINzwtdHxsWJbj8BUJ-NWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو رقص این خانم ایرانی تو وان ترکیه وایرال شده و واکنش‌های مثبت و منفی زیادی رو در پی داشته:
@News_Hut</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/news_hut/72577" target="_blank">📅 16:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72576">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=tn-aCw1HJ3D4qJEoA_Ul-Mgvn_Vf-HeOLXVS-JbYfS0R4-ANmx37eS94nb82duR7L5eHDh3bnIAha8Af3eVazy4Vt11-4vqsnKkfOZagfUc517TjnqHUz27PaiXbRHeIdy3KK18w58MPq-dXZzbURhrGYW4Fykj5BIYv0VFuE612Ozwxx64-4tB6zmeTp1vvCXA9YTyWEXhGWTQJY6A9BJr1jZJWi5_1R2dgPus7q-JhUczebyAaVoIr3WbGdc16dT2KHadiMLKlmr-slHxeYxTignXlWORVr87X2SCDre1BPH5PG-9WvErZB5I8ZezzqeKvkDQF0eRUDhjY4c73Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=tn-aCw1HJ3D4qJEoA_Ul-Mgvn_Vf-HeOLXVS-JbYfS0R4-ANmx37eS94nb82duR7L5eHDh3bnIAha8Af3eVazy4Vt11-4vqsnKkfOZagfUc517TjnqHUz27PaiXbRHeIdy3KK18w58MPq-dXZzbURhrGYW4Fykj5BIYv0VFuE612Ozwxx64-4tB6zmeTp1vvCXA9YTyWEXhGWTQJY6A9BJr1jZJWi5_1R2dgPus7q-JhUczebyAaVoIr3WbGdc16dT2KHadiMLKlmr-slHxeYxTignXlWORVr87X2SCDre1BPH5PG-9WvErZB5I8ZezzqeKvkDQF0eRUDhjY4c73Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب اسرائیل به فارسی در پلتفرم ایکس:
حالا که بحث هواپیما گرم است، یادی کنیم از هواپیمای کیش.ایر که 31 سال پیش در مسیر تهران به کیش با 174 سرنشین ربوده شد.
زمانی که سوخت هواپیما تمام شد و در شرف سقوط بود، اسرائیل تنها کشوری بود که به هواپیما اجازه فرود داد و جان صدها بی‌گناه را نجات داد.
جمهوری اسلامی هرگز نتوانست پیوند بین دو ملت ایران و اسرائیل را از بین ببرد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/news_hut/72576" target="_blank">📅 15:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ اظهار داشت که ایران خواستار توافق است و درباره پیشنهاد آتش‌بس ایران که در آخر هفته رد شده بود، ترامپ گفت پیشنهاد ایران برای باز کردن تنگه هرمز کافی نبوده است.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/news_hut/72575" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سؤال: نتایج نظرسنجی‌های شما هرگز تا این حد پایین نبوده است.
ترامپ: این ارقام ساختگی هستند. من هر کسی را که امروز نامزد باشد، با اختلاف ۲۰ درصد شکست می‌دهم. نظرسنج‌ها فاسد هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/72574" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سؤال: اگر «گادی آیزنکوت» در انتخابات اسرائیل پیروز شود، آیا آمریکا می‌تواند بهتر از زمانِ «نتانیاهو» با او همکاری کند؟
ترامپ: خب، نمی‌دانم. حرف بدی درباره‌اش نشنیده‌ام... فکر می‌کنید او پیشتاز است؟
سؤال: او نامزد اصلی اپوزیسیون است.
ترامپ: خب، خیلی‌ها بارها «بی‌بی» را تمام‌شده دانسته‌اند، درست همان‌طور که بارها مرا تمام‌شده می‌دانستند. من بی‌بی را دست‌کم نمی‌گیرم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/news_hut/72573" target="_blank">📅 15:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سؤال: گزارش‌های متعددی وجود دارد مبنی بر اینکه پیش از ۷ اکتبر، به نتانیاهو درباره احتمال وقوع حمله هشدار داده شده بود.
ترامپ: امروز برای اولین بار این موضوع را شنیدم.
سؤال: گزارش‌ها حاکی از آن است که مصر و امارات به او هشدار داده بودند.
ترامپ: فکر نمی‌کنم؛ به نظرم اگر او خبر داشت، حتماً اقدامی در این باره انجام می‌داد.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/72572" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:
اگر من رئیس‌جمهور نبودم، عربستان سعودی الان وجود نداشت؛ اسرائیل هم همین‌طور. آن‌ها از روی کره زمین محو می‌شدند.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/news_hut/72571" target="_blank">📅 15:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟   ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم،…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/news_hut/72570" target="_blank">📅 15:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟
ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم، اما می‌خواستم پیش‌تر بروم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/news_hut/72569" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72568">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.  ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.  سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟  ترامپ: چون با نابودی ایران، صلح را…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/72568" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72567">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سؤال: در مورد ایران، آیا قصد دارید پس از انتخابات میان‌دوره‌ای، حملات هوایی را تشدید کنید؟ گزارش‌هایی در این باره وجود داشته است.
ترامپ: ممکن است. ما سلاح‌های زیادی در اختیار داریم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/news_hut/72567" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72566">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.
ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.
سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟
ترامپ: چون با نابودی ایران، صلح را در جهان برقرار می‌کنیم. به عقیده من، تا زمانی که ایران وجود دارد، هرگز نمی‌توان به صلح دست یافت.
@News_Hut
| time</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/72566" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72565">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نتانیاهو با مسافری که به توقف حمله به کابین خلبان فلای‌دوبی کمک کرده بود، ملاقات کرد و به او گفت: «بدون شما، می‌توانست یک یازده سپتامبر دیگر باشد.»
یانیو حیون، لوله‌کشی که هنوز پیراهن خونین به تن دارد، گفت که مهاجم را خفه کرده و کنترل‌ها را به عقب کشیده است.
او به نتانیاهو گفت که برنامه‌های تحقیقات سقوط هواپیما را از تلویزیون تماشا می‌کند و به این ترتیب می‌داند که چگونه باید کنترل‌ها را به عقب بکشد.
او هیچ سابقه هوانوردی یا نظامی ذکر شده در گزارش‌ها ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/news_hut/72565" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72564">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=LTqLxdsTQL-sxK0xbwN7QVPR2jhRPL3keJrioXfA1LCn7MR6dlRuDhAKkC7rzqkLIPkCNqQnhQX4H4ZObr61WFkS1CijNUOZLZxDoW6OCnU3if-CDre6blpQVRCCKcBuWzpDZObwEq8dSU6Bxb8ridnlC8qlQL21oHw1gPvNH0YdJWc8G2Xw7OkWSBKyKdpu50PsIZya2c6S4IPkV7Gm7laH405qkpnnEE_BJ-b5p0MXGVobmFGwImfiaIlovvyPGfJdPVZ-6UyeMJ5EqvP9fAWIyJbDwXrShGysnNqTxQDdQ7Fg4JHKdbv27RyRSJhvHl0xywyhzW9PUrJNJZiFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=LTqLxdsTQL-sxK0xbwN7QVPR2jhRPL3keJrioXfA1LCn7MR6dlRuDhAKkC7rzqkLIPkCNqQnhQX4H4ZObr61WFkS1CijNUOZLZxDoW6OCnU3if-CDre6blpQVRCCKcBuWzpDZObwEq8dSU6Bxb8ridnlC8qlQL21oHw1gPvNH0YdJWc8G2Xw7OkWSBKyKdpu50PsIZya2c6S4IPkV7Gm7laH405qkpnnEE_BJ-b5p0MXGVobmFGwImfiaIlovvyPGfJdPVZ-6UyeMJ5EqvP9fAWIyJbDwXrShGysnNqTxQDdQ7Fg4JHKdbv27RyRSJhvHl0xywyhzW9PUrJNJZiFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی آقامحمدی، عضو مجمع تشخیص مصلحت نظام جمهوری اسلامی:‌
گروه‌های مسلح آموزش‌دیده در امارات و اسرائیل وارد کشور شدن، مردم در محلات مراقب باشن.
جریاناتی در محلات استقرار پیدا کردن تا عملیات‌های ترور انجام بدن.
اومدن نتانیاهو به امارات رو جدی بگیریم. طرح نتانیاهو اینه که به‌جای اسرائیل از امارات بجنگه.
+البته این چیزا رو میگن تا تو اعتراضات احتمالی بخاطر تور و گرونی بهونه قتل‌عام دوباره مردم رو داشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/72564" target="_blank">📅 14:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72563">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnSTpFTZuDoyUi4FHemt0t7X39MLBpw56XyFMVbhapVHC88_-dRCOSaY82cuMvTomu2oqqafNv-ca4tsgXQ_cHjN4yTc9wLa1m-XLcYTbCdvL4CAVq7Z-kq0L3HZ061RxcB0-Uszs8QvYWAOTXLlVp5A--Y1Wbo00In4XpS9ivotv26v9qQ8bhOpro_HW805ih18mqbVdLoZlfecKDq9f3blyMMJbaiKzwgU0-6Skb7UVM6onsQLdO49a554hKl2_M92xPD5zy2kHHe3PWD65qRp_pe0c3-59gcPfX6IKFCo579L_0D0-E_1fQi85JpF1elUr8myWBPMiFF4S_gT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: ممکنه ظرف دو هفته «چیزی از اقتصاد ایران باقی نمونه».
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72563" target="_blank">📅 13:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hp68hjuVjD7fJOrw14vokkZMddstzzi4977PcEwZx2D7gnJT_tZj65dVySa-38FQlqKqLh_I9nNN7e9NjrZdwBO4QY62PTpGiNiJmjsurIrHazOIY9DBJfUFBSHE_SEYi2wLfpXFtVMjjPZVKhRQIorCgPcv4UrW0nA3VHnXw2p5J7xO9Q6LWEBB93q_4FiFfReCvjeqFy_MkpfnJswXI7CE5Nfj1PTM-OTzxJsO321L84maeCJUX5bjr03sonAGE-xJUXgWSEwMZB8r3g8FtUeIwhE7p7yvPk7xcNXoXZtNUtAE4Onl-T8fXp2fLrVcPSXx-mKdSTlAcXPMwuUtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKpnn0qjjq1SIQI0nW4VCdkzSIz5PVg8L4PqXTqdvhgpk4A-w68JzjoGj17SdvMMqpL9-4SxMxL9Rp8BvuNu5XvxoMxoeAwr3asTFb40Zv2nXq4mpy6VA2xdz7npfdd7bggIZ9JnVpaPzG2V1PHD15TlOUPrnN_WLWU8IlbcvSMMW2jPsK0mcpufBjYBliV4rDTfJhhc-T7fOvK90eknYJX8XyH00FYWBT8AZoiLxBLcUriFKBre77iEk_ECBLXxY7nRxa2vu630lnjoZNCJPn3ph1atASdtOo3ERRfwzcPMxBGoH9JEcw4ktStjm7Qtllr8k1A1S0OWFf1LpRyIHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیژن مرتضوی که همین دو سه روز پیش گفته بود شایعات باور نکنید و نمیام ایران دیروز لایو گذاشته که اومده تهران
+پست چند ماه پیش بیژن!
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72561" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565ee82707.mp4?token=pQggDQhcxLjl44zzIEbWwg7F0T_sNg8DTN2eirTGDvSRbcAghnRcNfyLQjys78ZhE2RRPO3yxnBKWVwWEVcbUFPOXq-GQyVD1LlS17M5sc29lzZo2cAjVgL28dKZiNb551b_VxwL1dxTWA8b_HapK5vDof3JxOR8JKvNL4MkQu-pV-kFjdoryYHqZcSHYCDHlLjTmxaTiKXht3fT7DE_RO1ucK0XIjJrcn1kku_IWjT0fw8WlhD-wuCaLlSljLKYtYKKZilr2yu3Zt35BuW2i1gU1oXd39uoXTSj11HOKd1Gn8NLym_E0KPB9pizanozQ7UGtPyTjZrnXS6YveL7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565ee82707.mp4?token=pQggDQhcxLjl44zzIEbWwg7F0T_sNg8DTN2eirTGDvSRbcAghnRcNfyLQjys78ZhE2RRPO3yxnBKWVwWEVcbUFPOXq-GQyVD1LlS17M5sc29lzZo2cAjVgL28dKZiNb551b_VxwL1dxTWA8b_HapK5vDof3JxOR8JKvNL4MkQu-pV-kFjdoryYHqZcSHYCDHlLjTmxaTiKXht3fT7DE_RO1ucK0XIjJrcn1kku_IWjT0fw8WlhD-wuCaLlSljLKYtYKKZilr2yu3Zt35BuW2i1gU1oXd39uoXTSj11HOKd1Gn8NLym_E0KPB9pizanozQ7UGtPyTjZrnXS6YveL7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد حافظ حکمی معاون وزیر ارتباطات و فناوری اطلاعات با اشاره به قابلیت‌های فعلی استارلینک و فعال شدن قریب‌الوقوع «Direct to Cell» تو سط ماهواره‌های استارلینک و امکان اتصال مستقیم تلفن‌های همراه به ماهواره گفت:
«اگر استارلینک فراگیر شود، وزارت ارتباطات و شورای عالی فضای مجازی را باید شهربازی کنیم!»
اگر قابلیت اتصال مستقیم گوشی‌های موبایل به ماهواره‌های استارلینک فعال شود، سازوکارهایی مانند رجیستری تلفن همراه عملاً کارایی خود را از دست می‌دهند و شناسایی گوشی و مالک آن غیر ممکن خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72560" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72559" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72559" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3yd9kbvV3alkDHAFw7xTErXxX-By1U9oSkAMrfMZ6grCAeAUdpuh4v3T5fzxi3S-xXfkdIvXJG1xQHGU9ujCPrr5I8cAw6z6kkj1jh6Q3QfnrZYlbPJsLAza5guwtsEtaLUPRThfiq5w6MAF6ouOp-b0I6_XFl2zMbWg_6YXefgTQ894gWSV2woaEYJY0xLHFPGQoB3ktm7SwSNd7qA833sS_r2cSy4cZmij-jlFiQQBETA2r8e8lMSMufw_niFtv-gBR1PLfTBLmGT24sMyg4iE0rbXrIz_6NUjSgHG0raivs8gARTjubdtnRxgQPuNKCyKBEC68hd5lH70ZE6QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
صربستان
🆚
آلمان
هلند
🆚
یونان
پرتغال
🆚
دانمارک
نروژ
🆚
ولز
بولیوی
🆚
آرژانتین
اکوادور
🆚
ژاپن
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/72558" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbA9B6zmL6-EY8UhLv5UCrLE9QKxLNrJvS4oX8fYUsHqXBl1VjG7Z9DcZVvMKnL1vGkw1kvBo8jZLmOkbG5-2ANbDOd0nZan7FcmAoc-vmzctJ9eYHgekV43CYeljaZPfgqSOzDJ0OA5gnyvlcJ9SNPAEYiax2pzC1gsVPI6Zq3bKounJRbovSgEwB6VJ3akbFQUZyqXTbrcw5zcEoPGnQgaShIT3MJ0mtN1Zw8BxHL-9ccMI5JnI1VIAUswnfOIGnafDtNlcBw0x_n269mWbAs9KpQ46DtQRN3nHf0W8nmmQKu5Kgedv6YgXc1IAbRMGPqmGadFnP2my4WxtHW1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد که نیروهای آمریکایی در چارچوب محاصره بنادر ایران، مسیر ۱۲۵ کشتی تجاری را تغییر داده‌اند. این رقم نسبت به گزارش روز جمعه، حاکی از تغییر مسیر ۳ کشتی دیگر است.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72557" target="_blank">📅 12:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=EYkGuOPBA-mqMjlCXyZBAhQb48meDzN6JP5zyw9-G1COn-snFLW_5c7S65IL31OueS3aap48VUpnbSbdLbsep17e4UG4UF_yn5XFDw8vXtM9xI1IEu07txH7M3SxLaM2nGf9g0OQ4p2DvBR3j0CM66j2ORvSBThwr4yptgWbMnBx9yyjPHFqIKh1Iin4U7RfcOGqGs_HwXwp2shpqnlU7F9uEWy9HqP__8SBqwDZgR42V1ghJes0qWqmcgApAouhQ81zeuBqOrAGZw8zdYsBUCJNRMKhnHWJnBAxJEQMcPALqplNILxStyCCd9p9hPq5N0QqEm7Pnt-sxxdgessL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=EYkGuOPBA-mqMjlCXyZBAhQb48meDzN6JP5zyw9-G1COn-snFLW_5c7S65IL31OueS3aap48VUpnbSbdLbsep17e4UG4UF_yn5XFDw8vXtM9xI1IEu07txH7M3SxLaM2nGf9g0OQ4p2DvBR3j0CM66j2ORvSBThwr4yptgWbMnBx9yyjPHFqIKh1Iin4U7RfcOGqGs_HwXwp2shpqnlU7F9uEWy9HqP__8SBqwDZgR42V1ghJes0qWqmcgApAouhQ81zeuBqOrAGZw8zdYsBUCJNRMKhnHWJnBAxJEQMcPALqplNILxStyCCd9p9hPq5N0QqEm7Pnt-sxxdgessL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر از هموطنان رفته بودن شمال که توی مسیر پلنگ مازندران رو هم دیدن:)
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72556" target="_blank">📅 11:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv_ml6-c0wetIOW_iUszQPaVDFwWcYPPWjEctsA6gxJibi90mwVH5a0iMQH_HnUu3zfMEqubHUawy_KXHWgbUvJKcZJKGJKFeR5cPz721j-s_ODnmbvmBOSDR47FdIhXssxkPWsg96Oc1nb36_96woL1YWvhdDt6KEdZCE0gh0rXBkPIp5wevG-OzMXMRmRfS5Ysuj-pBBuElZ4I081wPV8HGaDGy0dMtrMlAICjl1JYi1G_WauL_nuvQ3jKOF6Ulohzg7kWbqp9nyci4lBHX5iy5V787RYQ6rVPVmhSPMc84Qx8PyoR5KtWO2TJ2wxVTsbUVifDS7SVp0dvbH3zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛اکسیوس:مارکو روبیو وزیر امور خارجه بعد از اینکه مذاکرات میان آمریکا و ایران در روز دوشنبه به بن‌بست خورد،به هیئت نمایندگی ایران ازجمله عباس عراقچی دستور داد که فوراً امریکا رو ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72555" target="_blank">📅 11:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72554">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=jVdGYLZbM5j-c678Ty5acfFtRxaXGgIoLKHLmBzNKivJAj47rpR7gQFLEjVEfY5Al341eFVHTRykmdhoixB2NB4ito8jM06VmAZnwplEHG1GPcmMMQoodiTHwdPF3KWVU0hXnEvGz5U7-_RhTHg8hrawPtl-TgmUG1-SLL8b_5YEy925v9BbG6a8pHtBgIwGB4WmD_D16iu5FwaK0l0lkAyEFgFFX2yDAHNvbpttU6g-Zbmn1OMAkxDjkNBA1039HZvsObV402-9jpATvHaP4d5UESkcXt86UxvgansurAliitVnF0DW5Jzy6ihWySwOEmkzyeQJrzero6nN806W1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=jVdGYLZbM5j-c678Ty5acfFtRxaXGgIoLKHLmBzNKivJAj47rpR7gQFLEjVEfY5Al341eFVHTRykmdhoixB2NB4ito8jM06VmAZnwplEHG1GPcmMMQoodiTHwdPF3KWVU0hXnEvGz5U7-_RhTHg8hrawPtl-TgmUG1-SLL8b_5YEy925v9BbG6a8pHtBgIwGB4WmD_D16iu5FwaK0l0lkAyEFgFFX2yDAHNvbpttU6g-Zbmn1OMAkxDjkNBA1039HZvsObV402-9jpATvHaP4d5UESkcXt86UxvgansurAliitVnF0DW5Jzy6ihWySwOEmkzyeQJrzero6nN806W1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از وبینارهای مملکت بین یه دختر به اسم "پرنیان" که پزشکی قبول شده بود و "اشکان" که کنکور مردود شده بود، یه مسابقه برگزار شد.
نتیجه جوری شد که همه آخرش ایستاده اشکان رو تشویق کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72554" target="_blank">📅 11:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HUQIp3RSzu9KUEtG0z1ISXgopql6zC7XQNoC2apnAwqQNGLRFZcLT8DvNfwOlpa2NoU7l_eRyFdH8kO5oqG1sge8kxoOJfBjAC2bX02cKg8iYXbEPcZCaoFogeXD1GB7vkCXXnvOigr94Q6pG6Ze7VFZqol5Hya2KcBdxDvzMJl7FRJlJH3RZOOUBw2FBd29mxzQF84gFd3S_HLsy-liKXwNXutsqjglFi1X6LleAzrOEPiph7U73sj_3O7wwGpriH9OnB_T1MN0sq5_XFMz9hhZRCFR0_FVtHRBVtYEiEMCa99zsWRYieVmwHQJyqaVpCm41PEreGSUdlUgNMr5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G0TeWkITaN44DFR_IqtYQivss3LTFQ1PnhNo4h8dEC6MLym7CjO7A9eQ2u-xz1CmztLaK6rH2MWvu8VWk-8Vw2SPEtaxkBX7vDpMBpF98-IhTwnt-e5IvlDX-1W7qk41BVlwGlTOs4fLCBW1jDsJIWa4b_UTptUMriIU4YF9xsmMo1LfqN5vIhnSlclzxvNoNkll_sDKlZvm4VJ1cLDs4cbE_RxFbgUm74hxuSgMZkvC5iIdnupToPgsV1LhnFxBqHRV20QSrc1AhxbqVphBlCZe25yi0LLyeabQ34r3730XV5ixEiqBqA9ASfJcZUZZ5YYK-jwyciTL3IjNMYMGhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از حامیان حکومت: من 13 ساله که یه بیماری درمان نشدنی دارم، دکترا قطع امید کردن و گفتن و تا آخر عمر درگیرشی.
تا اینکه یه شب رهبر شهید اومد به خوابم، بهم گفت درسته من کشته شدم، ولی مملکت رو اداره میکنم.
یهو اسمم رو صدا زد، مصطفی! رفتم جلو و بهم انگشتر هدیه داد، صبح که از خواب پاشدم دیدم الله اکبر! هیچ اثری از اون بیماری نیست و کامل شفا گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72552" target="_blank">📅 10:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=KX_-eRI0b3S1fROlfwQIiITmePaeeB9U8Py54TSecV0RIOH091eOxMv2bpe2_U4jo7-_XbtLjWMOt0HUAE4qIXd7mBL4EIUJBaQB-n4_USvltaLU0UbiWMy0plokxyzO8oSM3P-9VsSXcIzKHu9etoAwa-RCqynIdeS-IOrWIrYmKXiNlcOno_8Xb5ZbJ9JIJF6qBwNRWYJF1zjw_55Tl3dJvSlX0rTZ1Wi9_8BFAke0CEWT6ySR9mCUUR13gMKw-dYfAfLZUn73LM1oBCeKTMduoShf7uhjon8u0N7kspTL1Hzoiho-LRybeJ6uHlkePZc3sn46qWU7KBCJM0YP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=KX_-eRI0b3S1fROlfwQIiITmePaeeB9U8Py54TSecV0RIOH091eOxMv2bpe2_U4jo7-_XbtLjWMOt0HUAE4qIXd7mBL4EIUJBaQB-n4_USvltaLU0UbiWMy0plokxyzO8oSM3P-9VsSXcIzKHu9etoAwa-RCqynIdeS-IOrWIrYmKXiNlcOno_8Xb5ZbJ9JIJF6qBwNRWYJF1zjw_55Tl3dJvSlX0rTZ1Wi9_8BFAke0CEWT6ySR9mCUUR13gMKw-dYfAfLZUn73LM1oBCeKTMduoShf7uhjon8u0N7kspTL1Hzoiho-LRybeJ6uHlkePZc3sn46qWU7KBCJM0YP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کلاسای دانشگاه مملکت، یدونه پسر، با ۵۰ تا دختر، همکلاسی شده!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72551" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=oSYpYTX3XAHvMPhn-LsAvQrJc9oML01G5Z7A59NgJ26OPRO1BFBF6ORcU8ZjHs3nl8AQ-5gxZ5afvok-2mPexsswQ4BNlAJubJN7P1YHrZuDs1cGWzi12JerFPXZoh08fPdNVvciVGPqBOSmHFNoGn9lhIwEODthbGEimz1rM-4Drd6XhdbTYo_my9-QTTfqnpe5KjUedM-EevGSTyp8hnC9_JZZSTK7r9xC1JvsJ08Mn63MRPN21eqB0lU-ePxX-6YeZsFiNRPEAxs_UmpCGxv_MTbDV_xGwfW_SFSE4WLhgCCX5wOefv_vVN7xMs35Cie_Ici87iTYz72ItO_rsbhwBSLfoCJO2NIaAqy27dl_be4pWKnAOIaEvIeorG6W90jMLASHUxpvwMXt2xz4ExwirxMFVHkofJzEo7xU7ToWv_i2bAp_7gNNLf9Uf6Bw0pI9KaEDSfrAf_PrHLSGUxSP7hslaDRWV8lOyYzejB7TPY2sl_MsCW_ru7cC5j-QslZZXGyahlx-yophQrPkeBGl8EZAldA1oIDLwac8V9VrqqysqBIK6Y6AE-Ia2ypLsBhnrtIJhaZHQ1Tvu5mo0U233QZmnqCNyLjDW7Vgt0ItoGXDLdn2rZbpPCm1bF5lUiQKEGc6Qgl0O05Vh6eeNsTJ45-WL-r7da_zANFolvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=oSYpYTX3XAHvMPhn-LsAvQrJc9oML01G5Z7A59NgJ26OPRO1BFBF6ORcU8ZjHs3nl8AQ-5gxZ5afvok-2mPexsswQ4BNlAJubJN7P1YHrZuDs1cGWzi12JerFPXZoh08fPdNVvciVGPqBOSmHFNoGn9lhIwEODthbGEimz1rM-4Drd6XhdbTYo_my9-QTTfqnpe5KjUedM-EevGSTyp8hnC9_JZZSTK7r9xC1JvsJ08Mn63MRPN21eqB0lU-ePxX-6YeZsFiNRPEAxs_UmpCGxv_MTbDV_xGwfW_SFSE4WLhgCCX5wOefv_vVN7xMs35Cie_Ici87iTYz72ItO_rsbhwBSLfoCJO2NIaAqy27dl_be4pWKnAOIaEvIeorG6W90jMLASHUxpvwMXt2xz4ExwirxMFVHkofJzEo7xU7ToWv_i2bAp_7gNNLf9Uf6Bw0pI9KaEDSfrAf_PrHLSGUxSP7hslaDRWV8lOyYzejB7TPY2sl_MsCW_ru7cC5j-QslZZXGyahlx-yophQrPkeBGl8EZAldA1oIDLwac8V9VrqqysqBIK6Y6AE-Ia2ypLsBhnrtIJhaZHQ1Tvu5mo0U233QZmnqCNyLjDW7Vgt0ItoGXDLdn2rZbpPCm1bF5lUiQKEGc6Qgl0O05Vh6eeNsTJ45-WL-r7da_zANFolvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اولین موشک اتمی جمهوری اسلامی در  ایتا و روبیکا آزمایش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72550" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rMjffzKrxmjaiAApNcv7ciyPldrTAru8nt_C43ZWtigBkXSGsEN4ORxd5uJKfzTts0WBC9gDFhn1y8GID6e-ERU5lHkLbTEIY3mwPgFEG74sciNoOcu0eC7aQUVZ8Z8ShDCmrlc3C013ifKaWb9hrVFZD-zKHk5iqR1wZ0How551qij0UloYoMIAGVGeIr0cDpXVyyHDPU8K8ZTIUsdXju_zC6h8me44gW5Et7ig7T1dM1eZdAWzbYFDqxgAksX2YKTFvyD-73fRet-XCBcGgwObinkdig3u8Fl5abbEEDRfeB6cVRYI-nzOWBHiZcgif-J5fwTX1b43BI1aFVqljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jvU5Sq58kRvA8qkP2D_RUE5v2hLLXz7tpCeAz4UHlAflYViJSSNZ4EMtKwzEhXIgatgr_06dh--qw1pPQhFhmdVy3lJc5tIvnkk1a5kGHWpAhoVm1dX6aDB2QttP74WxVXzd3PXaYmCyqSqwgwhshMVTncN7z42VfWeMmr2edzlap6Yugov4fRxw_CDR0b6kjLUtuffRp6ppqwazzQqAgwlA8dOF5mcQ8UZyrEqjC86LhJL5fNJt9DmMrn-zcYrN9p4_a87X-d6zU5UbrkdGz5I6pgPe-IQVqGISPOc49MP1vMW5R_Rdzr5L7RsTCrRuOvLkexMX1UUXEt4h9E9Q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E5L9N5b0Lp1xdBiLX7d5sa89nmbPNYN8ujPjFK5deQ1bqc3ZoesI8-PNN_NGOypYSz7e3l0nl_JQEG0iLTrl63WUWuZjSF9zY-fFWXYPYPaRWrUlI40NJ3C3GYUCu2Rk_9-kPwPitZQYuA_HdbWqROJ5KMpk1VfoejOKYoc41D3Ql6Ayan2tA2VJgcVPGRcb0pLvgpq7qbedycZgWrucK2qzEY1Xq25KB5oaDNqOBn4mj-HK9ruOJwppJ-DpWQTinKbJ7t1CL7LsaA56UmH8IvH_8hmNO2KF1NaxoTb9I5O29iecBn_wxggKZYvxSF86lZ3m69ypGpcYwLAxuWmxbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=gaiFzJyG8XZWpy6mPbYKSUxixmpveJa89aLJxP1Aulvf3UkuiWsjzFPagrSmZbZXKqDcmDzBaT_o6xR1vuboFVMpAieBuJ64X1R8tsQykumWT3sz0f4OeW4LNJCU7SI9fDl438rnP9lcqRAqNI28sZgJd2fEjh31DzaRO1ZJeVjdI4G7bS1Zo28QMbgS7IqfpG03wOxCImHsrzp4q6NCoCECsutWh3qK35PmK_2BZa4irgRFcrKAMSx2x9xpl9NSOMr7612Xx-clUuNtvLD2T1TU8HCm951wzfVpLZzpDJ9AR0xBmhmDwPG82BTogD2eQLbOE8nIM0mPeO2aNSrD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=gaiFzJyG8XZWpy6mPbYKSUxixmpveJa89aLJxP1Aulvf3UkuiWsjzFPagrSmZbZXKqDcmDzBaT_o6xR1vuboFVMpAieBuJ64X1R8tsQykumWT3sz0f4OeW4LNJCU7SI9fDl438rnP9lcqRAqNI28sZgJd2fEjh31DzaRO1ZJeVjdI4G7bS1Zo28QMbgS7IqfpG03wOxCImHsrzp4q6NCoCECsutWh3qK35PmK_2BZa4irgRFcrKAMSx2x9xpl9NSOMr7612Xx-clUuNtvLD2T1TU8HCm951wzfVpLZzpDJ9AR0xBmhmDwPG82BTogD2eQLbOE8nIM0mPeO2aNSrD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دارن خودشون به جنایت جمهوری اسلامی اعتراف میکنن!
دو روز پیش توی بندر کنگان، مامورا می‌ریزن خونه یه نفر و جلو خواهرش به رگبار میبندنش!
انگار گزارش داده بودن اینا گازوئیل قاچاق میکنن و مأمورا ریختن در خونشون، تا پسره درو باز میکنه، به رگبار میبندنش.
پسره، باباش جانباز شیمیایی جنگ هشت ساله بوده و خونوادش ۲۰۰ شب و هر شب توی تجمعات شبانه شرکت میکردن!
حالا خواهرش پست گذاشته که مردم راست میگفتن، این حکومت قاتله، ما اشتباه کردیم، داداشم و رفیق بی گناهش رو به رگبار بستن.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72546" target="_blank">📅 09:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72545" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/news_hut/72544" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0sC2C4A4dzY0sMJ02j5Wu5lZjTinXRLHcT2wxb6b-LAvz_M2Btz94k0Ix4gSpCyq0gXaQ-kkJ3UfEobR4bfdW42BImpUsmUE4dfLUgtNlZwgYPnoRvm_GpOsWAgGxiOdMyeXqMUxDKlibJqGXhguRR3m_yuVeIATQ6kKTJUJ5r8HIHuB24EpOVOueB5OHFUSte983bv_WSwtL7KVtPnsWvQ2LOgNptMOhE_nXNXxS3zgxxrYxXYezOE4yOtK_r4NmoQH12ABWaQYJs0AYE69XvIcKBdAJ3oOxPxq43aEzl81ycuH7i4iZUkFjCWaF6VM5DedDqy70m0S-TdEXLvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز پنج فروند سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز؛
+دارن نفتکش رد میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72543" target="_blank">📅 01:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=AtFdf9MO4vN6d8fKce0S1aJgh9iifwq7K3KHhzXTpQLkRunvPS06ZzS2diNIVT1z1nx6W2KWCcZjSPILz00Wut95ADGxmiBWD2s0VVocCD1zs1oTu4cDsuDV0gYTFyCqvaJrINPE0XI4ExQOb0YO-XQ3lYXg9vSS_rgPfbw0rabc0QG_dNqEVQUrB6CrQKyUabFEn4IeuvM4FK6POjF5f8i0j8tfqtKVVYziUqr7ijwmKPdaEJCRPWT1uRz_T4Igx5ZWfRegXipbz4iBK_xxfkvVqfshu8ymEX9vJD_4W3aAkc_Md828n04le0CUu2sK34h6HNIHtCksaDNJJ6OnIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=AtFdf9MO4vN6d8fKce0S1aJgh9iifwq7K3KHhzXTpQLkRunvPS06ZzS2diNIVT1z1nx6W2KWCcZjSPILz00Wut95ADGxmiBWD2s0VVocCD1zs1oTu4cDsuDV0gYTFyCqvaJrINPE0XI4ExQOb0YO-XQ3lYXg9vSS_rgPfbw0rabc0QG_dNqEVQUrB6CrQKyUabFEn4IeuvM4FK6POjF5f8i0j8tfqtKVVYziUqr7ijwmKPdaEJCRPWT1uRz_T4Igx5ZWfRegXipbz4iBK_xxfkvVqfshu8ymEX9vJD_4W3aAkc_Md828n04le0CUu2sK34h6HNIHtCksaDNJJ6OnIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:
شما ایرانی‌ها را دیوانه توصیف می‌کنید. چطور می‌توان با آدم‌های دیوانه به توافق رسید؟
ترامپ:
شاید هم آن‌ها را منفجر کنید. ما باید در این باره تصمیم بگیریم. یا آن‌ها را منفجر می‌کنیم یا توافق می‌کنیم. زمانش دارد فرا می‌رسد. ماجرا خیلی زود به پایان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72542" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=fFD9S_5Kp6eykqebKPkV7KLY5pIoG7kptmnXc9MSuVOBbnoBxWVjhjrzDBjZFoUYuHk4t0ARrNxLHC2v2hIDCAXNkoAFz41OrqNm0FwSmkjkyscU6wzPt4x8IeQSpmlolm3IN2zL4wSb_6wvldFEZ1x_wAjGi8vIvezqyOffig-4YAjb1tTUDqOLwbhaK232il56YT2DE65CWDdSgStY8y-4ns4NNJdHU5j58vZMJ2lntcXK8BbvMAjTfrtE4VhStmSnwDoiaWQQ91-2dKjcXWGykKDkE2d9gAkmEvBU-gQGY0_zEc4yxqzPXnxK9qhG8-i4xXiiLcgLB8uw4kucBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=fFD9S_5Kp6eykqebKPkV7KLY5pIoG7kptmnXc9MSuVOBbnoBxWVjhjrzDBjZFoUYuHk4t0ARrNxLHC2v2hIDCAXNkoAFz41OrqNm0FwSmkjkyscU6wzPt4x8IeQSpmlolm3IN2zL4wSb_6wvldFEZ1x_wAjGi8vIvezqyOffig-4YAjb1tTUDqOLwbhaK232il56YT2DE65CWDdSgStY8y-4ns4NNJdHU5j58vZMJ2lntcXK8BbvMAjTfrtE4VhStmSnwDoiaWQQ91-2dKjcXWGykKDkE2d9gAkmEvBU-gQGY0_zEc4yxqzPXnxK9qhG8-i4xXiiLcgLB8uw4kucBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رهبران ایران با تمام قوا برای به دست گرفتن کنترل می‌جنگند؛ اما کنترلِ چه چیزی؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72541" target="_blank">📅 00:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=N1T7eUUYJ883GVqa4PuD3SVpriC-gCeQbuzeLf3cgaKVg7C85DWb9eLZhJ7wdr4ACT9VAmZO0SkgmjHC03hzz0QzfBD77l2fRBg2BxOm8XGlwc7z-MXz8trEWZSz6i5oIm5q24Od1PXK1Ptlm9L7I3NMVaUV0zZ5HrBysGEVTdVDI_ZBlicgzgLa3G-pBb9q0yBw9Hm-vntLLozFge4RFmz9zTRiV5X7_VCpi_j20oF5YwkmNWn1M5fX4XnAc5ZPk01tpYPUxIXYXUu0LXTfkUImSPBMcQztNp11c9pEKhQEQC22Dkqm-dcU7SINUme2q4p0FpPrv5IKMr-vTL0n6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=N1T7eUUYJ883GVqa4PuD3SVpriC-gCeQbuzeLf3cgaKVg7C85DWb9eLZhJ7wdr4ACT9VAmZO0SkgmjHC03hzz0QzfBD77l2fRBg2BxOm8XGlwc7z-MXz8trEWZSz6i5oIm5q24Od1PXK1Ptlm9L7I3NMVaUV0zZ5HrBysGEVTdVDI_ZBlicgzgLa3G-pBb9q0yBw9Hm-vntLLozFge4RFmz9zTRiV5X7_VCpi_j20oF5YwkmNWn1M5fX4XnAc5ZPk01tpYPUxIXYXUu0LXTfkUImSPBMcQztNp11c9pEKhQEQC22Dkqm-dcU7SINUme2q4p0FpPrv5IKMr-vTL0n6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنجاقک‌ها زیباترین مدل رابطه جنسی رو دارن.
اونا بهم متصل میشن و شکل قلب تشکیل میدن و تو همین حالت پرواز میکنن و... تا کارشون تموم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72540" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=U2GCgSFBae7iqf0vdF16aPIAu4FR7wCjm8oyseJFQx9ni6t_AAG7gUC8pHtxZD6o-ez3qRXgkjB5HEHLW3ju2FGtj4e9BcPPhJVO_EhriTzOU5cJLj3JIBaGIYZLbszC-duTUIwOX8JKXuLFeTc7PBPGIlxY9_dy9hITgyWdLxGaza1Bq35U7WBiqA_bDrym0EzO9Gsi5ZOFnt38XrebQzXOy2QqWUapEgQrgWz1rQKm6QRJUaocFn-vlmVFzNSpLDFxVNQqB23kssN45EhIMCRfRq_ojdA1C_0kiem7djd87kmXniuEjMhvIVF3fKTyhkKLSkMib7r0ia35vWRIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=U2GCgSFBae7iqf0vdF16aPIAu4FR7wCjm8oyseJFQx9ni6t_AAG7gUC8pHtxZD6o-ez3qRXgkjB5HEHLW3ju2FGtj4e9BcPPhJVO_EhriTzOU5cJLj3JIBaGIYZLbszC-duTUIwOX8JKXuLFeTc7PBPGIlxY9_dy9hITgyWdLxGaza1Bq35U7WBiqA_bDrym0EzO9Gsi5ZOFnt38XrebQzXOy2QqWUapEgQrgWz1rQKm6QRJUaocFn-vlmVFzNSpLDFxVNQqB23kssN45EhIMCRfRq_ojdA1C_0kiem7djd87kmXniuEjMhvIVF3fKTyhkKLSkMib7r0ia35vWRIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای زیبای این پسر در مورد وضعیتی که برامون ساختن، ارزش اینو داره که ده بار گوش کنی و براش دست بزنی!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72539" target="_blank">📅 23:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIC4HrZfxjJgPvuTZ8pRJ9UYeOsL2cq_gwqqDsbAmGqF8FixPz9sFvsFmTeGtjXjusQHwfl6DKYys1AvResuVrETQXmvgmDbzj7dz9-Ks9VGdDt6rZJ3jT7axfgo_0dxZqnNW92cL8oWuESI-8z3Znpm11UzgKIjlXYB23A10diHCus6FDNCK5a1UsfHATbVsX1xVVWnAqQfGVi_hpi1ydEpmwCmK5Rg6V2Az6TNNmV4qRyC2w5HQAPhbjG1PQB55gJIhudrkCD4yJRYVbalqRRiEqrMnaD-z-cT7N5Mx1p7wZQZLGgR13A3VWaYx42iQC1B6lps9QYNCRXlgquHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بوئینگ با پیشی گرفتن از نورثروپ گرومن، برنده رقابت نیروی دریایی ایالات متحده برای پروژه F/A-XX شد؛ قراردادی به ارزش بیش از ۲۰ میلیارد دلار که به توسعه جنگنده نسل‌بعدی نیروی دریایی برای عملیات از روی ناوهای هواپیمابر اختصاص دارد.
انتظار می‌رود این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین جنگنده‌های F/A-18E/F سوپر هورنت و EA-18G گرولر گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72538" target="_blank">📅 22:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما تقریباً کنترل کامل تنگه هرمز را در اختیار داریم؛ البته باید بگویم کنترل کامل، اما هر از گاهی آن‌ها مین‌گذاری می‌کنند و اندکی در وضعیت اختلال ایجاد می‌کنند.
با این حال، ما عملاً کنترل کامل تنگه هرمز را در دست داریم.
در سه روز گذشته، حجم نفت عبوری از تنگه هرمز بیش از هر زمان دیگری در تاریخ این تنگه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72537" target="_blank">📅 21:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درباره عراق: داریم با کله از آنجا بیرون می‌آییم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72536" target="_blank">📅 21:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=brnUk7YL9oFnYSBpsUX-JQJ_3NSEnRDT_8FlSBqf4hXMIRhjgdd1kH6mXewzs_Wn-s1PGg4E6XEgL9Jx0ugoa_kmX9tT-97adLn40GV5ODyFplUqddszBUTpJpPWK-E97D9DpQu-EkbJk6CfXn-jSHnbd4iCRPQlvPbvaw5yxew9ko8ON1eT80KmrooiGrxGlSE5dlJ_9O3OiXlVUTQt8mllQ-tbFrLfI_XL-1dfLebVDQb6U0BF80jhJKw-fhAZEZfmohZgepRixIP6NPocmJeljoMlr_GN8TW09ugKA325NOtZK84QxjP4mcwTkGY8NrnhN8Gkr9fWlT-MGxpQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=brnUk7YL9oFnYSBpsUX-JQJ_3NSEnRDT_8FlSBqf4hXMIRhjgdd1kH6mXewzs_Wn-s1PGg4E6XEgL9Jx0ugoa_kmX9tT-97adLn40GV5ODyFplUqddszBUTpJpPWK-E97D9DpQu-EkbJk6CfXn-jSHnbd4iCRPQlvPbvaw5yxew9ko8ON1eT80KmrooiGrxGlSE5dlJ_9O3OiXlVUTQt8mllQ-tbFrLfI_XL-1dfLebVDQb6U0BF80jhJKw-fhAZEZfmohZgepRixIP6NPocmJeljoMlr_GN8TW09ugKA325NOtZK84QxjP4mcwTkGY8NrnhN8Gkr9fWlT-MGxpQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فووری
؛ترامپ درباره ایران:
خیلی زود شاهد وقوع اتفاقاتی خواهید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72535" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مَردی پنج ساله به بایدن فش می‌ده که چرا از افغانستان کشیده بیرون، الان خودش تمام نیروی نظامی آمریکا رو بعد ۲۳ سال از عراق خارج کرد
#hjAly</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72534" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsT8xiU7bQ4QZqXbDacSjvyzVHN5MPLk1B3PRlG2v3BTa1joabsEWlKtNHxeVme-DBE6bpwAcHU8dYhSbDjr3mpozOJrxvpOxGB89qjcrPNi7dbVUdVxLTK8OWt2jtx_EgJnn_9wYVE3UHihFuP1_Q7ppygjbdQUBi9aJpvjk9fq-b6K9O4WE9db_vw5FAm77H-jAQRb7U_IBIDbM6FhvMOLuqWP10gX3LhoY0ZEXmvIcGMcPt6kwrRD1j327eDkJCpXxhIVm4KbchRalvGfj1BPSVxUdOCeYQY7RFQx2iVUySivXgTj4HxbzEx7E1x2_L4wjp5pQRtmPqsyC4FLZVxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsT8xiU7bQ4QZqXbDacSjvyzVHN5MPLk1B3PRlG2v3BTa1joabsEWlKtNHxeVme-DBE6bpwAcHU8dYhSbDjr3mpozOJrxvpOxGB89qjcrPNi7dbVUdVxLTK8OWt2jtx_EgJnn_9wYVE3UHihFuP1_Q7ppygjbdQUBi9aJpvjk9fq-b6K9O4WE9db_vw5FAm77H-jAQRb7U_IBIDbM6FhvMOLuqWP10gX3LhoY0ZEXmvIcGMcPt6kwrRD1j327eDkJCpXxhIVm4KbchRalvGfj1BPSVxUdOCeYQY7RFQx2iVUySivXgTj4HxbzEx7E1x2_L4wjp5pQRtmPqsyC4FLZVxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛
اندی برنهام نخست وزیر بریتانیا:
شواهد محکمی وجود دارد که نشان می‌دهد ایران در وقایع آخر هفته در پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) نقش داشته است.
در زمان مناسب توضیحات بیشتری ارائه خواهیم داد، اما می‌توانیم این باور خود را تأیید کنیم که ایران در این ماجرا نقش داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72533" target="_blank">📅 20:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#فوری
؛کانال ۱۴:
بنیامین نتانیاهو نخست‌وزیر اسرائیل طی ساعات آینده با ترامپ تلفنی صحبت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72532" target="_blank">📅 20:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30841564f.mp4?token=Is9bJKBzLC8-Zn2IgQ1vpwv99B8HWRd26-MCw77vDMwpLr-NO1ebZeGj7_blEr2f7Z3mAQHkxvda_WH_olJ1UwKu_m4KAqV8d8E1-QlcBDPKEL6dQl23qMp60-JXE5RMrEvGawHi0YuwtTVxWy_jiR38k8psWMWlCmVOVYaTspZcgsWUbnQcNC0rq5okES2kYtcuDaIIL4YvCLlMfWGoITF54VEEsCisWkQPDaZjle3zLg_FM5PBpa0uC0585QebwLd8SO_jVl5cc4KH5HeBJBFjQFoNIDhq8fKH3OC9rEaXu95Zf_u-wswr8yETCoJwykiQdwrDf5UT9MQwRePCnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30841564f.mp4?token=Is9bJKBzLC8-Zn2IgQ1vpwv99B8HWRd26-MCw77vDMwpLr-NO1ebZeGj7_blEr2f7Z3mAQHkxvda_WH_olJ1UwKu_m4KAqV8d8E1-QlcBDPKEL6dQl23qMp60-JXE5RMrEvGawHi0YuwtTVxWy_jiR38k8psWMWlCmVOVYaTspZcgsWUbnQcNC0rq5okES2kYtcuDaIIL4YvCLlMfWGoITF54VEEsCisWkQPDaZjle3zLg_FM5PBpa0uC0585QebwLd8SO_jVl5cc4KH5HeBJBFjQFoNIDhq8fKH3OC9rEaXu95Zf_u-wswr8yETCoJwykiQdwrDf5UT9MQwRePCnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشیانه‌های مرکز پشتیبانی لجستیکی شهید اثری‌نژاد نیروی دریایی سپاه پاسداران در شیراز، پس از عملیات خشم حماسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72531" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72529">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2S9s6J6JdbStk8dAn3kx5FO5OcihCDsI-WnQhIgkQVGUmZhhTrKtAPruwout0X5VXgdVtK9AOwGbnxEpKeWxoUQDN8HOCT4rTcmHGBFRMgg51fTfTBIHr7I36iMA3Iy7SLZlncuCldp8yrs1ZHrxY8pREgCZBaA8oMnezDwRkw38j_uJ6xk9HTtP_N_2R86lF9aZeNDZw3mhKrXGFeiD8uPnZ83yAiprrDNpK96iKathJln86RLSEbabDjTQNJ437-ExA0R9AuRKbGPF0DTv8gaUqK-h8jta0ihvVDq0Q2Jz6_L8V3--KD1VplIMEBjyDMQFCm3yHB07YTLu79_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAEPyOV-svJpLWDg05BPZ1nNrsXy1sUs5ru_y-0AIoyM5hU1bHrPVfCaB9BJOdh0X64w1DT1RKQZHhQ1qt6D8LQCTG9qMqMY5vghwfllPF-BKwlTGhJ4tBr3HTKJkvdpYYanKm71R8aXohnXh9LKKwxrNJbcQIg915m5BhC_JlRNm8F-iE5rRD8QiBiPRQK-PNJ0-sN3MNnnXiW-V4s668JxTayJlbIxvblW8qO1540UZo2ymra8TpbXAALSTOlnMDGNWwl4bRME3cBVs-IGPSAepaYhkz-PWrOy_CBOfPrNag-RO9lLCvqMn_Ggb8Sjg1FvTwMn5tf8v-XyYrItFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72529" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72528">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو درباره حادثه پرواز دبی:
«یکی از خلبانان، خلبان دیگر را با چاقو مجروح کرد و ظاهراً تلاش داشت هواپیما را به همراه سرنشینانش سرنگون کند.
هواپیما وارد حالت چرخش شد و شروع به سقوط کرد. یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و خلبان مهاجم را خنثی کردند.
یکی دیگر از اعضای خدمه پرواز نیز موفق شد هواپیما را به حالت پایدار بازگرداند و از وقوع یک فاجعه بزرگ جلوگیری شد.
خلبان مهاجم هم‌اکنون توسط مقامات سعودی مورد بازجویی قرار دارد.
به دستگاه‌های امنیتی دستور داده‌ام برای مقابله با تهدیدهای احتمالی دیگر آماده باشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72528" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72527">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72527" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72526">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHm7XL9nnPsVmCWmmg-QsorQJx3Hz0uK5NiW9gXjIeS_1X2CnmSWX7qK0auv7EjIxotAmRluuGpGFsrIcdcyATmUIW0ffr9CZQg4oB8eNaB_lVzlmtYH_tOaonl2nVJYt7s4ZGZtCQpNUDGsqRJLXiOhaOgGL7kZws_DOZ0ncjKYNYyYvji_09bYYgDV4xGuw6NhvpHVCMTEIEL7A2dG-oA6RISLKJ9vCBQX3tbT-TpA5kUfygp7bflNCTgH8imr7Qyp48lDR98stwwVhVfZKG8Rd8cOXC7xgRxx9qknjr-ZicbBrpVko_YjPTvM_PvS4v4yW78GFADpioZVwQK_4g.jpg" alt="photo" loading="lazy"/></div>
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
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72526" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72525">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=JrtI7HMq_zKmx_hvUetpkHLZc3mMAhUuESp-RaWJgw5P1-Kb2sLCemXLCwfW4bkmSbvLwWBUqV23muB8aD23APJrdP0SlttZqkTtRGZ0GzsV8DDEM_F-56HPTxV4xQUxIxE40ipFb9HZl4hRptB3kbexr2x4pVQFCznurx6q3-JKcl-0RIAulGaK5QYEeUL_HnQLW-UdvGAkqS3emBwWQDeDlqwPMO5lcuFhl00m54g9Q-yNE-neZlql0rmdDgoLhAdxfHxkf5XA6mOq4MSPZE-XE4vvCU-AYvTOuCnxx1DlfBLbN_mOgxkEzM4YETEPKvjTQS6ZmmL4vtfSee2wRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=JrtI7HMq_zKmx_hvUetpkHLZc3mMAhUuESp-RaWJgw5P1-Kb2sLCemXLCwfW4bkmSbvLwWBUqV23muB8aD23APJrdP0SlttZqkTtRGZ0GzsV8DDEM_F-56HPTxV4xQUxIxE40ipFb9HZl4hRptB3kbexr2x4pVQFCznurx6q3-JKcl-0RIAulGaK5QYEeUL_HnQLW-UdvGAkqS3emBwWQDeDlqwPMO5lcuFhl00m54g9Q-yNE-neZlql0rmdDgoLhAdxfHxkf5XA6mOq4MSPZE-XE4vvCU-AYvTOuCnxx1DlfBLbN_mOgxkEzM4YETEPKvjTQS6ZmmL4vtfSee2wRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏عاقبت لایی کشیدن در نهایت همینه؛
ممکنه چند بار تو رانندگی از روی دست فرمون خوبتون موانع رو رد کنین، ولی بالاخره یه روزی میرسه که ممکنه یه همچین صحنه‌ای برات رقم بخوره...
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72525" target="_blank">📅 18:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72524">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=Jh_icaghjCy62-rNVigIEwzJsu51zKDk9MpITU726YGf4EPGO5Ct31J-mkQBeuRDdwcqmy0fuFm-khWY7av-rbeGCREI3XZDjR0-htF1xcYs2l8e9ttrv88r2xxV4kzibM5cNMUqTwqQN2UchUQI-eSAsTAB8qrAVaEIVPS0ZnVBUPTRuELoNNYZujgiefYnwXEPhRFdPGOjO-RXmXZ6wtvLITsGk_BR0SN83JhnwV2VxeuMpSjjg3OyceCCE-Pl14xmqyMM_ACsy-iGeIB2uJQayqXujVYJVRZjREQTjB2wc3ZLCNlDDcgTBVob5f-hteF0jyPQpQA0YLvHvQZu8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=Jh_icaghjCy62-rNVigIEwzJsu51zKDk9MpITU726YGf4EPGO5Ct31J-mkQBeuRDdwcqmy0fuFm-khWY7av-rbeGCREI3XZDjR0-htF1xcYs2l8e9ttrv88r2xxV4kzibM5cNMUqTwqQN2UchUQI-eSAsTAB8qrAVaEIVPS0ZnVBUPTRuELoNNYZujgiefYnwXEPhRFdPGOjO-RXmXZ6wtvLITsGk_BR0SN83JhnwV2VxeuMpSjjg3OyceCCE-Pl14xmqyMM_ACsy-iGeIB2uJQayqXujVYJVRZjREQTjB2wc3ZLCNlDDcgTBVob5f-hteF0jyPQpQA0YLvHvQZu8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ بعد از دیدن این کلیپ تمام ناوگان های دریایی شو جمع کرد و دستور داد همه برگردن امریکا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72524" target="_blank">📅 17:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72523">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=gmO8JPIl7mh28vZzm0wJwEGM3ptuY-SbAolUGysrtqaN4uioW5MXPAoye1jXI7VD9ODYzT8ZJcM9889WYVYg5rjyAYrU0hIcDjyXcmoVkyOrflCPfd-vWig1kWG3fxT5CZgbeRbreW4YZ0eVhNLcUykOBXcN9bVWHkKF2dcBOr1NQoIHUbGoehPZEJbWrw4YWqThZTN30jvBhwDjm8WFdx2YXtJafKQ5Um88ILvmxv0CNbhbadJLt23vDOnpcUA1CMbPwBX872P3efwy0NOcfts0R2TUznwtCG89TPb9QI_cKkM-545D3ABQXkn_i7-fya6uBlp-xEJ_c3TsX1ckJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=gmO8JPIl7mh28vZzm0wJwEGM3ptuY-SbAolUGysrtqaN4uioW5MXPAoye1jXI7VD9ODYzT8ZJcM9889WYVYg5rjyAYrU0hIcDjyXcmoVkyOrflCPfd-vWig1kWG3fxT5CZgbeRbreW4YZ0eVhNLcUykOBXcN9bVWHkKF2dcBOr1NQoIHUbGoehPZEJbWrw4YWqThZTN30jvBhwDjm8WFdx2YXtJafKQ5Um88ILvmxv0CNbhbadJLt23vDOnpcUA1CMbPwBX872P3efwy0NOcfts0R2TUznwtCG89TPb9QI_cKkM-545D3ABQXkn_i7-fya6uBlp-xEJ_c3TsX1ckJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر بچه دهه نودی با اجرای رپ خیابونی، این شکلی کلی مخ زد و از دخترا شماره گرفت و بوسش کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72523" target="_blank">📅 16:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZNO2iGVF1Wsp9th21i8wkwCm2vWSW4-w_Ot8STwWU8nliuaYqB8s2Uptnag7rP-axqHEQpJpS2zINIbGO8uNSkzdXvwcPCZ_w5D8a4JiUWe_Joynn5UZK4l_ObYIiw05zl9MU3rHEkJbaR36ehST7X9-5omRPmeLb0Ozuol1U0CVIDZ8CVfnruvdvlMG-ShiPQ7q0NA_Fy4pny3vnHf3XYZNDpYBdM1ChjwKAi23nW2tSlmjossladibAQltPTb0gkFVbdH2dINeoPXCIYb71tRJjrQbUYZtOxF8i1oAF6FknQWhbsMgY_UQdAnFHUIAZMkwgJaY7E8VflkWTx0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=a1jp4VIWaoIxHgEtIk82yppvbec518X1F8wIOLFZqIwEAFycnxuACP1IuI2RvIjAipctV1vvk9tpQ-R6nB2SHa05WsPbzNk7ZtIRY1Rj8U_hQiEydIIKZRCS0zJjoPVpp39A7qMwgTIhJVQhS133SjJbf1dhUw2i-Nfrqe__1zSr6Cl9JeteIstlbOh3HDDCtzd53Cypf19vzs1CwhYdYle4mLBoo1qyWxyrIZUQROGdNPF4ccf7nbsYlPxQ6VDJ3VrPhu7k4N9bZoSN_9Zdn3LzV82TNpA9wO6v7e6Ityf5GEWDlmnfnqqg9tnpBbCYke5ti1pYA_grWTRPyrScgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=a1jp4VIWaoIxHgEtIk82yppvbec518X1F8wIOLFZqIwEAFycnxuACP1IuI2RvIjAipctV1vvk9tpQ-R6nB2SHa05WsPbzNk7ZtIRY1Rj8U_hQiEydIIKZRCS0zJjoPVpp39A7qMwgTIhJVQhS133SjJbf1dhUw2i-Nfrqe__1zSr6Cl9JeteIstlbOh3HDDCtzd53Cypf19vzs1CwhYdYle4mLBoo1qyWxyrIZUQROGdNPF4ccf7nbsYlPxQ6VDJ3VrPhu7k4N9bZoSN_9Zdn3LzV82TNpA9wO6v7e6Ityf5GEWDlmnfnqqg9tnpBbCYke5ti1pYA_grWTRPyrScgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بمب‌افکن استراتژیک روسی از نوع Tu-95MS در جریان یک پرواز آموزشی در منطقه «آمور» سقوط کرد.
این هواپیما حامل چهار خدمه و سه سرنشین دیگر بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72519" target="_blank">📅 15:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibTwMO7IL7zKaR_VEl2OmwfbJZjGhOAGLWyMDvnCvPfLkW9ojCRHc5HLhY84D_JocNX2805o0xaETzYEnfYZuGTKmWCx4QnItKTJ4kpb65cM8PY_MyJKajzolVeohjg3WGFgDEwl5lr2PN715XmgAKqcmB7n0K3oejrqfrwfu0mgLgnrJW52Tb23yTeohuZHbnPjt9yDGiovVS_yjigvWoQzyLeQDnhZc7KKr0_xfIunFW1LxdhXwNsqFpJuB_zKHfNyNF-7Gl__Vp6y6HRoo0f3mvuCUvwopLHy2fCullTNFeB6QloKUA_w2fRBnQw106sATlM3lajn7u0DTqxKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFZ-YVZvwwSsOal_fXgmK-DnEphQV2uXGBMEoTC6bDxlT5n3-fqb9NxU_eQXIbQpqlCflvX0NETYylLEspBXZHQq0Zq2eHabvxvdYCTByqa7VlCoc7X-tajwUksnb9GymWV4XtnSYRTbvrd30ev4rtaYzqQh5J2w-qOmB0xs6oIi06dbZJ96HtbtGfWcYyBjI_hNynIQxee-iCCFPBatkHaLEJ-1XJ13MRqJhnO7URtPR1Xc9nvZ4ocdjmtQCVX233b9LUjT_cj2m3tv32Zf1EHfXWTLwht-qPQQcaX8ZBmVApWhhX6m2UNSkDKSCGnd7BBASnWjOKBHgYL2AOBKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JF_ToIk4lq2JRLjQhViJ-_ONAM_rH7Nn9d2GOuXv_0y1uVQjUZwehXQ3q3cxWjbHHOB0Q67lkqz1HCeCFeDEjryTcJ487sQrQGz1nxmaM295R5NBR7x5Dyi6UXaDvAVqRGZ1JbZ4qAkEG_9J_hJx9Yh11VGKJQcrdyXxT89gWBu7MR8baC2I2WerCycIJqzChJQXwSz2qsE9kNIkadNWzFf0bKY0dkNXMVqp921VuiMfd8LcK-2ieqDUeRxpL7KOhttFFsqM-ATRzq0fenzOPTWSZAHkuXxt-94lNGxv2AaLtpkZoDcNjG-2BXSIk3qTpclbob9vuzeFogJIiNDXow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنا بر گزارش UKMTO، سپاه پاسداران امروز به ۳ نفت‌کش و کشتی حمل گاز در تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72516" target="_blank">📅 15:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjZafBQF7BIh-rNnPQEgd6FOvugYnMUpaNPXWrKhvR1f3xZ25goRzVCNfpcOtUZFYogUQmYOs-6CXFtF-8u5SCDJUHqovu_3v6tkoKQxxzpyD4nzAROyW-4Y7XBCOYPC6HrtcgqtPakvL3jiBgLafxcuvhCCySQRPCToeyrp-GUxG-LArX4ZaADRw1W3SYKvuwOtKBYvJnvuMqn3vW-hlwec2pNqCXUQSNua0e0wkOV668WTzSWqdJ6Ra02cs-fvL2jZ5UjlziJ0aup441LpVoLBLmWIj1bBiSfHqP8JCQYIhMz5M6ROPZGR3iZ7D7ZmafmitQ5zQQ9AsY6o4RG05-uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=k3PMURuQAd2PyT9Jc3UWFt3fLzPERgaW0cLjjpmAOh7IKywfIAf1nKDmlO4-YK4gjzWkwDabRJPpMioqJZAd03CQJi-pmcXSDXLQ15aLLsny03_W6WpOen7FB5sIk_n6zEHvASzGHTsPZHfU4Zpl8rf4cmkaMef5yZ2lNu7s_1PFkMesn-rAQN8GZ3B8tBcizTEOvn9CDl-Y7igROPvPpFcCadtyRdyvmXTXtBzobmHF4Fs31iyYz6WaTpSjQXY18Yv6dy_-O7-6RWiFXLIriokEVbuzpl8yEJkM4Lrr2s4UAn69UoG_L-gRdvDk8Rw3qoveJF8F3VcwFgF6WI-KjZafBQF7BIh-rNnPQEgd6FOvugYnMUpaNPXWrKhvR1f3xZ25goRzVCNfpcOtUZFYogUQmYOs-6CXFtF-8u5SCDJUHqovu_3v6tkoKQxxzpyD4nzAROyW-4Y7XBCOYPC6HrtcgqtPakvL3jiBgLafxcuvhCCySQRPCToeyrp-GUxG-LArX4ZaADRw1W3SYKvuwOtKBYvJnvuMqn3vW-hlwec2pNqCXUQSNua0e0wkOV668WTzSWqdJ6Ra02cs-fvL2jZ5UjlziJ0aup441LpVoLBLmWIj1bBiSfHqP8JCQYIhMz5M6ROPZGR3iZ7D7ZmafmitQ5zQQ9AsY6o4RG05-uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که هواپیمای فلای‌دبی دچار سقوط ناگهانی شد و به سرعت ارتفاعشو از دست داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72515" target="_blank">📅 15:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=Kshqt89VNg1cqgEeGej0HrwBdWOkv39BIIqQtTj2MQuxGjzBQXjh88ksmo5O3WAzKJ72CY6DJOzJkZX3Vq_-ajKzOqbdUMj4FW7Scu7cNHVk3mvvhbSn9-Wz6t0w1sNKEngPWkO8Waa-huF00d8CD2SugBpEb24ngnNJ4HmKolqXy53RxAcLdMEX55FAFdwr50iCDe3K5H3kL-8QyrgHknajflYR72i4yeiaUUu7FwsODEzmOaGAfwztZ4xMkNMaG5HawU7aG8en_ue0eFBKfMnc03GNLA851EN82zEZ9l97z27TbKc2BakxzlwAI4I5jHM-MZYA3nLZq_c4rDRaug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=Kshqt89VNg1cqgEeGej0HrwBdWOkv39BIIqQtTj2MQuxGjzBQXjh88ksmo5O3WAzKJ72CY6DJOzJkZX3Vq_-ajKzOqbdUMj4FW7Scu7cNHVk3mvvhbSn9-Wz6t0w1sNKEngPWkO8Waa-huF00d8CD2SugBpEb24ngnNJ4HmKolqXy53RxAcLdMEX55FAFdwr50iCDe3K5H3kL-8QyrgHknajflYR72i4yeiaUUu7FwsODEzmOaGAfwztZ4xMkNMaG5HawU7aG8en_ue0eFBKfMnc03GNLA851EN82zEZ9l97z27TbKc2BakxzlwAI4I5jHM-MZYA3nLZq_c4rDRaug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این موزیک به اسم «مفقود» در مورد مجتبی خامنه‌ای، فقط تو چند ساعت بازدیدش میلیونی شده
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72514" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آی‌۲۴نیوز:ارزیابی‌های اولیه حاکی از آن است که خلبانِ عاملِ حمله با چاقو در پرواز FZ1073، تبعه عمان بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72513" target="_blank">📅 14:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiyG6vErup1AiIYH021HRkVj5AhXkPknY-4agdwbJ9FwATkas_qKjy2IfbZKuY7SEbHj5df4atoJUPVp8fQyN--ai7ieiPI8sypGiuuecQoI1WMyVl3dWCkL06DWpNKsEAzUXhrnax20ToBhD71fLjF8NQKDYUSMrUxXXYZopQC0CKom4AyAcIH3l6MclRMJmR0RHBVw1vRgSHprkdpoBituaH8Ej4IU7jKZFSmZfNfzY7B2ZKt7K8pzbdQqvE_3NDTzh--BX2J6nrB_doJZwQKJAQtFiGNCezl4LO3ISn2Lb_PSrHlfDvPbuNsDCilCbO_XQpEsLVmrYMB0LLn6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72512" target="_blank">📅 14:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8284df28.mp4?token=ofeBQYv37h4oGj9icJJdKk5wJEi0cWpAKcACaCmg3lwT1DC_UmmV2LwacyJrUeCcuUL_z95W5Z2Ji2TWt5qCU7i0yL7Jai4LU6TH4DM7kfSrsqHMwRVf_XGh2ivFoGUu9DUvG8sEeoOw5lnONYNdt0ewKPKR371cvTFKZ5RROlhkKGB6NP07CrFeSWAkoe1GhMWBQ4BSm5wUt3gxMqHX81QM9ZBa4CkV5j-TgZgmQqY-oIdsfj8XQZLPIQkBOlk8_X3kWyY_Dgyulwb9N6GOh7SZDOZxlsho4zcRxh4OdQoCH30F-vz3K1JY-YU2z1kzvJ7wdLnNpIgonFDurcTJ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8284df28.mp4?token=ofeBQYv37h4oGj9icJJdKk5wJEi0cWpAKcACaCmg3lwT1DC_UmmV2LwacyJrUeCcuUL_z95W5Z2Ji2TWt5qCU7i0yL7Jai4LU6TH4DM7kfSrsqHMwRVf_XGh2ivFoGUu9DUvG8sEeoOw5lnONYNdt0ewKPKR371cvTFKZ5RROlhkKGB6NP07CrFeSWAkoe1GhMWBQ4BSm5wUt3gxMqHX81QM9ZBa4CkV5j-TgZgmQqY-oIdsfj8XQZLPIQkBOlk8_X3kWyY_Dgyulwb9N6GOh7SZDOZxlsho4zcRxh4OdQoCH30F-vz3K1JY-YU2z1kzvJ7wdLnNpIgonFDurcTJ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی؛
علت حادثه پرواز «فلای‌دبی»، مشاجره‌ای میان خلبان و کمک‌خلبان بود که به درگیری فیزیکی و ضربات چاقو کشیده شد.
خلبان تبعه روسیه و کمک‌خلبان تبعه اوکراین بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72511" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=Bm0cuSaJcLFXiLKjW6cO3gQfzwHY9tLSQTKlvxEny3Yn26sRFSixPYhQ6hb6DjnkT6rZUgjFEzWfQfsOhwAmJxpWq4CDLHxfzxshJDGXEHdGEFVnRCYRW2xo2fMkmKqWIwDLjAwjA03U0Z6iULJNVPGeZexh87qDwUQKk6ieaAXms3rH3zYjMMh-b1ZL5Yx_1lEtXqMcB1cwFhUOcCuR9uLHEbgXBOtFhEdwaQD6P9L_EeSnlsm3B8i6wNwcexSKYm3CQjQ-4SgmiuZVgyk535E-iNSvNc5cbGqKtPrt8s5tfXbUx5CQ64AfxVe5QIxpc8bGZB_-Fu1cip2N1c50SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=Bm0cuSaJcLFXiLKjW6cO3gQfzwHY9tLSQTKlvxEny3Yn26sRFSixPYhQ6hb6DjnkT6rZUgjFEzWfQfsOhwAmJxpWq4CDLHxfzxshJDGXEHdGEFVnRCYRW2xo2fMkmKqWIwDLjAwjA03U0Z6iULJNVPGeZexh87qDwUQKk6ieaAXms3rH3zYjMMh-b1ZL5Yx_1lEtXqMcB1cwFhUOcCuR9uLHEbgXBOtFhEdwaQD6P9L_EeSnlsm3B8i6wNwcexSKYm3CQjQ-4SgmiuZVgyk535E-iNSvNc5cbGqKtPrt8s5tfXbUx5CQ64AfxVe5QIxpc8bGZB_-Fu1cip2N1c50SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد
ویدیو دوم مربوط به فرود اضطراری پرواز «فلای‌دبی» در تبوک، مسافران اسرائیلی را نشان می‌دهد که پس از فرود ایمن، سرود «اُد آوینو های» (به معنای «پدر ما همچنان زنده است»؛ سرودی یهودی درباره ایمان و بقا) را می‌خوانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72509" target="_blank">📅 13:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72507">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tADx0eJWhpSB-Z6aNrRhUs11X4WTxN2JPPo5d5LTXjVjWWJMq3VgGPliiz6GIddmwhYdifP_K2GuPIQXCAwheZVDJWUgrq7wAUHIOCkDCCgIYtavjEAZbSC75lDa9V5TZNfmpYEEn7ZBLdvXdafuAjimy_HIDodjHrNZUiGgqYCkOFzFi3FgbS0dFda8egotY5js3DrePQ_R8GlrewCl-hvmDFdOMI1UauoOPFYSrputEvmMX1OaPJB0sK_nESAriR-hmBec_-Dt-CTP6YCtDNbKBe8syxQsj_MLQPvd52ogOy2Je5Od3Hp36-AkNKt_qqZeGsAHOKav2SUrjpy6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/coDLDcb8z1jyHJFYeisBmixFOUJ4yHl2rxE1Idxpn1YXG8p7nXBE985SJwcFrlGXRk-qRqVr-8NT-yA6tjJbt4z2EuILpsF8oaLEMZkZGAiHKnp6jhpMLunXFPmFKn1u9QZMAau3oXAKIKfCXIZETH7bJIspCdfaG5oefZIR3TqFFIZC_m5RQLv6v5bu37cehOEEd1_5aBfmg-MW8uGCVA38l7cj28b_nL-pOAQmmBIpsPET4lAv6X8XUSzCfQQs_-Cd3bA7taFXAiwI3XQ8kXIrVd98DMKi26_rtQfQENnZGjNrw42nnq7Dt5Wx3gT3ZUrpffWoYFPdmeqX00K6iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حادثه در پرواز فلای‌دبی؛ فرود اضطراری در عربستان
پرواز FZ1073 فلای‌دبی از دبی به مقصد تل‌آویو، امروز پس از وقوع حادثه‌ای در میانه پرواز، مسیر خود را تغییر داد و در فرودگاه تبوک عربستان سعودی به‌سلامت فرود آمد.
این هواپیما در جریان پرواز کدهای اضطراری ۷۷۰۰ و ۷۵۰۰ را ارسال کرد. کد ۷۵۰۰ نشان‌دهنده احتمال «مداخله غیرقانونی/هواپیما ربایی» است و باعث واکنش امنیتی شد.
بر اساس گزارش رویترز، یک مقام اسرائیلی گفت این هشدارها پس از درگیری فیزیکی میان دو خلبان ارسال شده است. با این حال، فلای‌دبی تاکنون تنها وقوع یک «حادثه» را تأیید کرده و جزئیات بیشتری درباره علت آن ارائه نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72507" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72506">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=dlr_NNtBlWDU1O3CG5BTGpiaykMJERhAPINxYkxYuHCrd1u7_OmTVhxoy4n10HQ3rcgdJfQdqQP5aEvgw5PPymd_Kt3zbxHmPXdeYzlp97FV2ZkMMOSAEQ_mKTccQwnJdekW_gH1G_G2zBzKG3oTSorOuR1K4LQ7-n6BsbSKuJx-Hmf5Tud-vhcCsJ8ZE6VLECftS2Jv188YJq3EMhed6nOwibGhfL5ssMKGe75Z4q0QeBXREQQeDPnbG4BRank6jhaskVNBCC3mvYRgcnF8AJiuK7ECOTvij0Tiwq38WQNhsuzrD4xqiy5eQIMypV4nCtPuTa8c7e43BQ40uuojfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=dlr_NNtBlWDU1O3CG5BTGpiaykMJERhAPINxYkxYuHCrd1u7_OmTVhxoy4n10HQ3rcgdJfQdqQP5aEvgw5PPymd_Kt3zbxHmPXdeYzlp97FV2ZkMMOSAEQ_mKTccQwnJdekW_gH1G_G2zBzKG3oTSorOuR1K4LQ7-n6BsbSKuJx-Hmf5Tud-vhcCsJ8ZE6VLECftS2Jv188YJq3EMhed6nOwibGhfL5ssMKGe75Z4q0QeBXREQQeDPnbG4BRank6jhaskVNBCC3mvYRgcnF8AJiuK7ECOTvij0Tiwq38WQNhsuzrD4xqiy5eQIMypV4nCtPuTa8c7e43BQ40uuojfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله به جای اینکه امسال اول مهر بره مدرسه و درس بخونه، با یه پسر پولدار ازدواج کرد و رفت خونه بخت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72506" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72505">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8vuFdDjvlURh640F6fn264TgVbF-OCXPmrr4AuPywrHM7yTR2pT_jox0O6UcZbrJVSV_wWMXFeKS7bcs5QBYSdDMN3kYm6pzgbWUuL104qcmWVySH-AjSFTgFahwkep6RBAG5d68PcPEvdCngHuyPyXWcgzN7OwALSScFZVKvnEf4W_Ctrm4mWHxUgiQ8Z98L7bLn-Wv22gUyfRy2G3Xi1v0kWwDJKSFHQ84KcQs1x1CmLzAoXmCfi81XoVmXV_HQJ2-0BImfDktPc9lx59eBWes-9wY5KimAUob87Ub0KOdI5gN_HzyL76HUo4zoZDvv0mJ371bWENQJEKauJEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده و شرکای ائتلاف پس از ۱۲ سال، با خروج نیروها و تجهیزات از پایگاه هوایی اربیل، رسماً به «عملیات عزم راسخ» (Operation Inherent Resolve) در عراق پایان دادند.
پنتاگون اعلام کرد که از این پس نیروهای عراقی مسئولیت اصلی تأمین امنیت و سرکوب بقایای داعش را بر عهده خواهند داشت، در حالی که ایالات متحده به ارائه آموزش‌های هدفمند و پشتیبانی اطلاعاتی ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72505" target="_blank">📅 11:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKqh6K4dMrdd_HRj5Oz5yGEPTIf-v6hUuk-9Ba9WTpSD82eJJaq8y4W8Kst71WUa1qt_PnVwlJR4m7xaIv6JlVMT9gnNvPofsZLD3g2j83Rd7zmHP_Elju-4VNdF_uDc1RcBB0fUG1iz3R7HpnhQQ3G3ZICF8B5tfq8GfEBa11N6uYWP8FRz_kc_UtsrycbgXpArzXz8OGgFuwhPzh8IMDKxj4REiboZzRoUurNj8CYPNiwQMDCw_y9Tb2be7iPKmjECL1cZQr9dJVlLmDBNO5Sr48TId_ZKe4qDos1UboAKq9Xfk2_84oTXHZ-K6mm-s0K-WW8N106qsRn5BpeUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اطلاعات اطلاعاتی جدیدی را به شیخ محمد بن زاید، رئیس امارات متحده عربی، ارائه کرد که نشان می‌دهد ایران در برنامه هسته‌ای خود پیشرفت‌های تازه‌ای داشته است.
این اطلاعات شامل جزئیاتی درباره ساخت‌وسازهای جدید در تأسیسات «کوه پیک‌اکس» (Pickaxe Mountain) بود.
یک مقام ارشد امنیتی سعودی نیز در این نشستِ گسترده حضور داشت. گفتگوها همچنین تحولات منطقه‌ای مرتبط با حوثی‌های یمن، باب‌المندب و تنگه هرمز را در بر می‌گرفت.
نتانیاهو همچنین به حاضران گفت که ارزیابی اسرائیل حاکی از احتمال انجام یک حمله منطقه‌ای از سوی ایران در هفته‌های پیش‌رو است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72504" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72503">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72503" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPuucihTM7W63LcP6djGTZHwKFECQmv26b95_AlGR-GzXEPXWjudb7lzcdwYoL_UmOnU0e_Kgj_geh_zujbYjinvQebNhC8JxxglxWtaHoPHg8G2a_xxy_Dz7fk3IAMvZSkYcNJ88X1a_dva5rf8q9_pKYLZ__IM_nZh-uzqeioq2PRUKtrc5MFt7taBjiuY9zwmeSu4iXwIvGYz8HTCRPS7I7Ny2rIMBcmwK7zUOzIWbNxiLY9z7pP7Crx4oHypyBQLf1NL2NKuUtQu4RqmePO3ByhkLp1pmocuXwqfku-Vg7Bms_Gdeing2cwx_BR6oY3gQ0Ukfuj2d_W5W2XXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72502" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72501">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=MMUfFgSMkjQ2VAy07-gbbPjf9WcMg3ZoXDDnw4jLSlQU39LiFk6Mva_Vs7qzY0B_YUkhzSqALTDkn4dtNDBfV2qox2tFd8daS0r_0AE62XBDmBURiKD0JEFHpXxEMzdP1dYWCuDIO31Gnlh7N80ptw2dPxORZOEaKwkuxXIRmNfqtNYonzwini99rLZUioMzHrc3NkOxDb-tD18fEs3L0vDc46cYk8Y2TEqPjyP4YG0lSbesW7BM_UKVTefIVBr27KJL59FBraLbfoVBxnWfOpCz5rPwWuOZAVnJRe3rm4zhCTaSNTM0DWyKRxKpek1OJ4U4pAi_ekKoaP9m6bjVTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=MMUfFgSMkjQ2VAy07-gbbPjf9WcMg3ZoXDDnw4jLSlQU39LiFk6Mva_Vs7qzY0B_YUkhzSqALTDkn4dtNDBfV2qox2tFd8daS0r_0AE62XBDmBURiKD0JEFHpXxEMzdP1dYWCuDIO31Gnlh7N80ptw2dPxORZOEaKwkuxXIRmNfqtNYonzwini99rLZUioMzHrc3NkOxDb-tD18fEs3L0vDc46cYk8Y2TEqPjyP4YG0lSbesW7BM_UKVTefIVBr27KJL59FBraLbfoVBxnWfOpCz5rPwWuOZAVnJRe3rm4zhCTaSNTM0DWyKRxKpek1OJ4U4pAi_ekKoaP9m6bjVTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان:محبوبیتی بین مردم ندارم و هرشب کابوس میبینم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72501" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=Gys_8KWe1YDMn9LAbJBUBAv8cHr-_pdeVY4EO0X_yllaUf2aZDNgljVScdKUqa7BiBiWbCBr33seSXA0KAH5YaETMI5AFF4QLBRxDr4Khkj0ZtmrJjnSgrbJba2InkhnzfWghSfhioPBGZ2J2qD6zwYwGovLRGtxu_NCdd562PPldKrDeaEKKjl_DjPcv5iqn-IqwRH7qUKvdMYkODGKkyXvrdq9zBehyaM99Ahm1QFJv5qeKNITroKBihh83xmwhdP_eEEyt7kLNoSTB_hS_5W2jRwkhDo1p9ypLce9l7lH9qyaIIFuwon-LUjhsjnAU4AjmiEF6dlh-6PBgdsYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=Gys_8KWe1YDMn9LAbJBUBAv8cHr-_pdeVY4EO0X_yllaUf2aZDNgljVScdKUqa7BiBiWbCBr33seSXA0KAH5YaETMI5AFF4QLBRxDr4Khkj0ZtmrJjnSgrbJba2InkhnzfWghSfhioPBGZ2J2qD6zwYwGovLRGtxu_NCdd562PPldKrDeaEKKjl_DjPcv5iqn-IqwRH7qUKvdMYkODGKkyXvrdq9zBehyaM99Ahm1QFJv5qeKNITroKBihh83xmwhdP_eEEyt7kLNoSTB_hS_5W2jRwkhDo1p9ypLce9l7lH9qyaIIFuwon-LUjhsjnAU4AjmiEF6dlh-6PBgdsYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از مراسم‌های عروسی در ایران، عروس یه دفعه تفنگ رو برداشت و این شکلی پشت هم شلیک می‌کرد!
از نگاه‌های داماد معلومه ریده به خودش ولی کمکی از دست کسی برنمیاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72500" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72499">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=L-Kq8nrPHyGK8JbzVIv8iupdRzFls_CHsdJnClCyMIDFNFbj0qmu8Ov05dYOAbwFrM3TLdNDcvnN2LmhuedMpnbuqCw4o3shn9ebsYccnYi__IbjHKZwQV4D-egjM-OBSBrDKgcnBrTKAgpP9NIVrzLJVj8Y-HLMJ_1q6RrHR4LrrZsqXVz5c7DQIj2i0mfIXAoet3ZkAt3O9x5omea1X0NycSJeHN8Hsubkh7szIIuvmmO898uwKw34hVjn7moYsCWS3Elm-dm5kkvGwKQ5FzMGeoaLOYbbeCf9lGSpVsnGkNvELV_vZd3RScewNMYbkSojgXZd6HglP9yJ9rA9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=L-Kq8nrPHyGK8JbzVIv8iupdRzFls_CHsdJnClCyMIDFNFbj0qmu8Ov05dYOAbwFrM3TLdNDcvnN2LmhuedMpnbuqCw4o3shn9ebsYccnYi__IbjHKZwQV4D-egjM-OBSBrDKgcnBrTKAgpP9NIVrzLJVj8Y-HLMJ_1q6RrHR4LrrZsqXVz5c7DQIj2i0mfIXAoet3ZkAt3O9x5omea1X0NycSJeHN8Hsubkh7szIIuvmmO898uwKw34hVjn7moYsCWS3Elm-dm5kkvGwKQ5FzMGeoaLOYbbeCf9lGSpVsnGkNvELV_vZd3RScewNMYbkSojgXZd6HglP9yJ9rA9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این فیلمی از رینگ کشتی کج نیست! یه دعوای سنگین تو فوتبال پایه مملکته بخاطر یه تکل ساده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72499" target="_blank">📅 09:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=A7jH4G3ik92D5vRyx3EZ3cyo0ck6tb1so4R4IsS7B7EuUVwn9RIjC-7ypvW0kL5qhZ_W0FWd8YRZa2_c_SpgmGDzHMYYyf2rFlzKnUYf_HsRrogT94McfwxkgnANwpCpIwKQrqUZMjVFhbl-Y7BbhkMqJ4jHFevcP1ipeZEkGWechhyZD2pO-scoeft7TXWdZLX-n7CsjO6-mmHZfvbT-pZbhlBLbZzycZ_4N11pmHv6OyTW_WK_BoiVBtSy0AQFnITOBynZtYtaGZHECrsh5A72Xrcb3ZCUwgLidRkTD0k0F00XMzYyFxiy8oz_HXWDATiLbhIWZKOYkXQcZPyWkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=A7jH4G3ik92D5vRyx3EZ3cyo0ck6tb1so4R4IsS7B7EuUVwn9RIjC-7ypvW0kL5qhZ_W0FWd8YRZa2_c_SpgmGDzHMYYyf2rFlzKnUYf_HsRrogT94McfwxkgnANwpCpIwKQrqUZMjVFhbl-Y7BbhkMqJ4jHFevcP1ipeZEkGWechhyZD2pO-scoeft7TXWdZLX-n7CsjO6-mmHZfvbT-pZbhlBLbZzycZ_4N11pmHv6OyTW_WK_BoiVBtSy0AQFnITOBynZtYtaGZHECrsh5A72Xrcb3ZCUwgLidRkTD0k0F00XMzYyFxiy8oz_HXWDATiLbhIWZKOYkXQcZPyWkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره روحانی از ملاقات رئیس‌جمهور سوئیس با علی خامنه‌ای:
رئیس‌جمهور سوئیس به آقا گفت ما ۱۵۰ سال قبل کشور فقیری بودیم، اما دو تصمیم گرفتیم؛ دانشگاه‌های خوب ایجاد کنیم و با کشورهای دنیا روابط خوبی داشته باشیم. سوئیسی که امروز می‌بینید حاصل آن دو تصمیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72498" target="_blank">📅 09:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daZJHwR_5AGHTxgCpXrKZTMP_XCVbI7uFsIkMzaeqA1VV1K4cBaX3Ixej3qv7vussWtS3hn0Md3-I0XRYvUmPKgANPgzVdchQwNCUlUg2J5VdA0P85nNJ4ugeWtLknGl8RfcqsBma_CDkrcZIELkBniu_MuoDFK_CQa2dBNsoJlAIbb2RgGjCJWbMcvOpvPV202NUuZorrYQUtDkO-W0goXvllm1naUgukJf_a4IQ1Ur1Vrl8msCJm3O3futir2rEnMFymj8Zv1x3Vk5TeMuwLJMf1ZG3sAUFCZrZvmJ0miQ7H0LUbmONwd8idRo2avNicXLKaUIxr4IKp_j5bLsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛مذاکرات به بن‌بست رسیده،ایران میگه اگه آمریکا به تفاهم‌نامه اسلام‌آباد برگرده حاضره امتیاز هسته‌ای بده و آمریکا هم میگه حالا که دست بالا رو دارم پس کیر تو تفاهم‌نامه اسلام‌آباد و کوتاه نمیام.احتمال شروع درگیری‌ها بالاست.
اکسیوس؛
تلاش‌های قطر برای میانجی‌گری جهت دستیابی به توافقی جدید میان آمریکا و ایران پیشرفت اندکی داشته است؛ چرا که مذاکرات بر سر دو موضوع — یعنی درخواست ایران برای رفع محاصره دریایی توسط آمریکا و مطالبه واشنگتن برای دریافت امتیازات هسته‌ای — دچار بن‌بست شده است.
ایران تأکید دارد که تنها پس از بازگشت آمریکا به تفاهم‌نامه ماه ژوئن، حاضر به بررسی اعطای امتیازات هسته‌ای خواهد بود؛ در حالی که واشنگتن دلیلی برای کوتاه آمدن و مصالحه نمی‌بیند.
قطر، پاکستان و مصر همچنان دارن خایه‌مالی میکنن و تلاش میکنن که توافقی صورت بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/72497" target="_blank">📅 06:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72496">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72496" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72495" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72494">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56db93255e.mp4?token=V1K0Hrs2aIUuIBrrYHOzNCJInpDqsHMOKcSJhntuskLjV5pEnpzvZzdar4svMDYwLLtj4kGD9V_7woX41WY1f-eRN9Mh-nbWaUiz66SithCf16PhTK6glNrNym94hNYXxXDta1l0b14rrXey9VqxA9ABS0r195QFkmv1KDiT7jfoG-jq1DAEHAHRxWrUBMfDeXr1dvu4ukhORBsbp5oTpCOshNPTiuqd4dxaUn7AV_5iHv72-5-SPxsQLVL0kp__vEmYNB7DrywwIOduVW8a7hjuYie4b_E804PlYfp0bjsNi10Q899esVX8Ti-JRytj_hFTdNxwxVMWud22-JEiVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56db93255e.mp4?token=V1K0Hrs2aIUuIBrrYHOzNCJInpDqsHMOKcSJhntuskLjV5pEnpzvZzdar4svMDYwLLtj4kGD9V_7woX41WY1f-eRN9Mh-nbWaUiz66SithCf16PhTK6glNrNym94hNYXxXDta1l0b14rrXey9VqxA9ABS0r195QFkmv1KDiT7jfoG-jq1DAEHAHRxWrUBMfDeXr1dvu4ukhORBsbp5oTpCOshNPTiuqd4dxaUn7AV_5iHv72-5-SPxsQLVL0kp__vEmYNB7DrywwIOduVW8a7hjuYie4b_E804PlYfp0bjsNi10Q899esVX8Ti-JRytj_hFTdNxwxVMWud22-JEiVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو نپال بر اثر رانش زمین، این کوه با این عظمت به طرز ترسناکی مثل آب، نصفش تو رودخونه سقوط کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/72494" target="_blank">📅 23:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=B8J3kU751JDePRvBlczy_qRYxP4G4KWUuv-b-QhXFu2AW-brneiWOLtJaATa2M203Md6LeUOBLx5Dpc4-_XlZlzRLC9a9B0i4tI1orC2Zz1MHMg9IKNB-VPpauUwpxcTVKEGBM1qPpjC25pEDMBIgk8aeBOW-LsU2M3ebG1K_2YGuV_dSzrxWafD7iGvH1aMhOb9qwiGxBt4ZGxubU3X4Tud49QB5Xt34K-3RU-yvGi_ltrHdCdgBiBm5bJHwOT0Ajj1Jckvu3n3K4ZfKyOnVxIAIpNvDmdoKpSBLkprtUAjMtjmgAPzOWed1fZ51k5JIpHzS9PV83emc59L2wQhDS9na0h2e5xM7nRdJJtdyPWrA_bOj9Jc-NxIgsgxx6mHcEfwK_WsR5Nr9G_TOLbagObErgkhvlSGcnWjVvbZat2_hj5MkkmfhZYn6x33PtkavvJC097pP9qrDxJHLboxusITmXh09nyKFMFD6OPYLheNz4NfuiM7LtzkJVU7yNyhPhuT_URVHhPcA0LEnW5qOmepj5Bc9BxKiWhF0w99EArXLSN_Jabk9zz_zQvvJnCsXMPAbw0a2LVUGOAcUCeeiiqfzcU7_dOwXAcQPIQgMagNIju3O3lXSGKlIBFb9ZEM3oa3YW2ajJHj7C8IDCMb8rZoucGOgezE9usuH24kuWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=B8J3kU751JDePRvBlczy_qRYxP4G4KWUuv-b-QhXFu2AW-brneiWOLtJaATa2M203Md6LeUOBLx5Dpc4-_XlZlzRLC9a9B0i4tI1orC2Zz1MHMg9IKNB-VPpauUwpxcTVKEGBM1qPpjC25pEDMBIgk8aeBOW-LsU2M3ebG1K_2YGuV_dSzrxWafD7iGvH1aMhOb9qwiGxBt4ZGxubU3X4Tud49QB5Xt34K-3RU-yvGi_ltrHdCdgBiBm5bJHwOT0Ajj1Jckvu3n3K4ZfKyOnVxIAIpNvDmdoKpSBLkprtUAjMtjmgAPzOWed1fZ51k5JIpHzS9PV83emc59L2wQhDS9na0h2e5xM7nRdJJtdyPWrA_bOj9Jc-NxIgsgxx6mHcEfwK_WsR5Nr9G_TOLbagObErgkhvlSGcnWjVvbZat2_hj5MkkmfhZYn6x33PtkavvJC097pP9qrDxJHLboxusITmXh09nyKFMFD6OPYLheNz4NfuiM7LtzkJVU7yNyhPhuT_URVHhPcA0LEnW5qOmepj5Bc9BxKiWhF0w99EArXLSN_Jabk9zz_zQvvJnCsXMPAbw0a2LVUGOAcUCeeiiqfzcU7_dOwXAcQPIQgMagNIju3O3lXSGKlIBFb9ZEM3oa3YW2ajJHj7C8IDCMb8rZoucGOgezE9usuH24kuWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
اگر بانوی ایرانی یک سرباز آمریکایی رو اسیر بگیره بهش ده میلیارد تومان پاداش میدیم.
مردم کشور های منطقه هم اگه یه سرباز آمریکایی رو اسیر بگیرن و بدن تحویل به اونا هم پاداش میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/72493" target="_blank">📅 22:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72492" target="_blank">📅 21:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaQcZ8jTALtfNJxCWFdSDfhAQ-Qzk5DsNBJENIt36SJEcBw-OWj2pG6OPVV1kKMEZFCZ-J82YUQuuQH1v3JnsZouuMY9R16azAy8mxxzVGEqkaybZ0gyA6SJku73QbaBjxutv0bR6OpMu9VAX4hERooz6Uur3mxJxoASouwOkfpxekysy_pCnLkk7R2_CUiu_tNuIwKBgyqH3GzU9EvhvOaD1CCKzPn8PdKdmxwvuZAq-UIa8AaYG9w2fSfYeTbDJ5xl6i7tVAJ_GStruBnMKkAUM8I6SsLET3zyf6MZ8ay0KGkPEk4v9T8JcqtkBn_G_sowQL_9oktyaIosawRFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا ۱۰ فرد و نهاد را در ایران، چین، هنگ‌کنگ، پاکستان، عربستان سعودی و ترکیه به اتهام حمایت از تدارکات نظامی ایران در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast) تحریم کرد.
به گفته وزارت خزانه‌داری، این شبکه‌ها برای «وزارت دفاع و پشتیبانی نیروهای مسلح ایران» (MODAFL)، تسلیحات، تجهیزات الکترونیکی و قطعات با کاربرد دوگانه تأمین می‌کردند که در برنامه‌های موشک‌های بالستیک، پهپادها و هواپیماهای نظامی مورد استفاده قرار می‌گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72491" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peswPy0rKPjqljPaPzbhF7HmLnF7TDO2sgmFVAq8Knx9Zvu9kgDvQIa-HjhhMx2F5WsQZwOkyF16-iV_Kv8aeJRSv8zIvNEpFXav9sUrd9R1Nr_mEYGHgsa4I2HnyMIsY84Sr7BRREEr83hUl5UpsHEZ2251tNe55rOCiDsZwhpYfYAaD4ABDBNW5_tLSd1nWCHDfc3zbe8MddgcrjEzy56GWxhmyn5i57q631pkX88i6_TLJZ5Ik6-EZaXFfKlkivxEoDoddzb49yucGe8q_yx1-w6U64Jcvrh0-YeZwI-lpyjMAvbvIFU0VL0e17Ighk5253dMSdm8nIGGqIMmMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آی۲۴نیوز:
یک مقام اطلاعاتی آمریکا به شبکه «آی۲۴نیوز» (i24NEWS) گفت که ترامپ با ارزیابی نتانیاهو هم‌نظر است؛ مبنی بر اینکه ایران یا متحدانش ممکن است پیش از انتخابات به اسرائیل حمله کنند.
کابینه امنیتی اسرائیل امشب تشکیل جلسه می‌دهد و نتانیاهو نیز «یائیر لاپید»، رهبر اپوزیسیون را برای ارائه گزارش امنیتی فراخوانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72490" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=cFKFzjqI7WPf5WDC0YhfwhNb9Jg-Xvvldqg_Foqx4sRmv__kwF33QXjqyXBgz5DoWY-SHdz4NnHeJBSFWLFIGMwFCcVG_0iUsnfj7Qdk4JiaYwUgXXpZj2sB-qvxWCEkFqwgMNRgUGGZgSHrKn1Knr_HHyQH_SgN2UnVGWITmAI9WNL8D3RlbZhlhpErlMqUrxVnAxLXGvwHNKxs9FMkIdWbGk5Jhvj9UfsCHe3y8Ugmxa6pYktM1_Q1rAZEhWfQQjIbrNm1ylvJEhjp70lKk59vsADvXW_ClwuD3oMBWPwcVRrPQVon0vL8iTlUqWutPIjaicpbP2syHvlJa65HCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=cFKFzjqI7WPf5WDC0YhfwhNb9Jg-Xvvldqg_Foqx4sRmv__kwF33QXjqyXBgz5DoWY-SHdz4NnHeJBSFWLFIGMwFCcVG_0iUsnfj7Qdk4JiaYwUgXXpZj2sB-qvxWCEkFqwgMNRgUGGZgSHrKn1Knr_HHyQH_SgN2UnVGWITmAI9WNL8D3RlbZhlhpErlMqUrxVnAxLXGvwHNKxs9FMkIdWbGk5Jhvj9UfsCHe3y8Ugmxa6pYktM1_Q1rAZEhWfQQjIbrNm1ylvJEhjp70lKk59vsADvXW_ClwuD3oMBWPwcVRrPQVon0vL8iTlUqWutPIjaicpbP2syHvlJa65HCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از فضای معنوی مدارس مملکت و دانش‌آموزان نمونه و پرتلاشش:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72489" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=ZO0RJSQkHsU1LPd_NQV-CeAieQqz2re7PBpkwYrmM3WGscTk7The84o4i6BdrQeJ3-dkbVQDr0hQPYMEjlHohY9xmZ1QcjRTK9wosy7vnNdrOJl3YZbexcahlJgw7jn8Qwo8cRdMnfO6vQ0Ts-sU4lwW5HK5nJ7f5fPfMHTLf-b7ZesJ0AS68ulVXIY6qOb70lR5jT3Xg4VikUxxRCm5iiAWiVOzWcVvAnCTEfoL-mRqYoVE1jaMFPs1XAJhkQhgA1Gwdm803D6UnV5vXw1fAcSbQMOwHZt2UyNkcZlO38pk7LOtOUD3a70opqU0qS0HaD-bsVbWfxA60ZI6J3TMLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=ZO0RJSQkHsU1LPd_NQV-CeAieQqz2re7PBpkwYrmM3WGscTk7The84o4i6BdrQeJ3-dkbVQDr0hQPYMEjlHohY9xmZ1QcjRTK9wosy7vnNdrOJl3YZbexcahlJgw7jn8Qwo8cRdMnfO6vQ0Ts-sU4lwW5HK5nJ7f5fPfMHTLf-b7ZesJ0AS68ulVXIY6qOb70lR5jT3Xg4VikUxxRCm5iiAWiVOzWcVvAnCTEfoL-mRqYoVE1jaMFPs1XAJhkQhgA1Gwdm803D6UnV5vXw1fAcSbQMOwHZt2UyNkcZlO38pk7LOtOUD3a70opqU0qS0HaD-bsVbWfxA60ZI6J3TMLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج استعفا در ایران طی ۷۲ ساعت اخیر!
طی چند روز اخیر، یکی از شدیدترین موج استعفای تاریخ ایران اتفاق افتاده و پرستاران، معلمان و کارمندان به علت حقوق بسیار پایین، از کارشون استعفا دادن!
به قدری این موج استفعا شدید بوده که خیلی از بیمارستان‌ها خالی از کادر درمان شده!
خیلی از کلاس‌های درس هم دیگه معلمی برای آموزش وجود نداره و صدها نفر استعفا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72485" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=aM3xn9VZP-rEjbOXjP4vu0DcnPnuAAJKc7yHnBifgI0nnvTHhp3qzPAgarxprAphFk455Ub1jz4AuugEKPO1YcW2RPXOlNze01E3Q7Y5YVCMC85KNznulU6r67LiRKepKT8xaaHwK0x3TqbB3AGIioW6K5XDTuy38intR4jBYDc-5_IrRutCUaJYF1ut7JRVqGxI5DfzF8kD57zDU1R5tRrl5Ye-RY9W64sLA3AZTDDz21aYwCDQ4zP4POcjN6GMRc1rqVFfvQHBnExmrH1bejEWmhF0e4VLM6mQGs81mff8wYeMikvbe0cOjnPB64sW9LYI5_wBZCzDHDTGkt2TqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=aM3xn9VZP-rEjbOXjP4vu0DcnPnuAAJKc7yHnBifgI0nnvTHhp3qzPAgarxprAphFk455Ub1jz4AuugEKPO1YcW2RPXOlNze01E3Q7Y5YVCMC85KNznulU6r67LiRKepKT8xaaHwK0x3TqbB3AGIioW6K5XDTuy38intR4jBYDc-5_IrRutCUaJYF1ut7JRVqGxI5DfzF8kD57zDU1R5tRrl5Ye-RY9W64sLA3AZTDDz21aYwCDQ4zP4POcjN6GMRc1rqVFfvQHBnExmrH1bejEWmhF0e4VLM6mQGs81mff8wYeMikvbe0cOjnPB64sW9LYI5_wBZCzDHDTGkt2TqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه حال‌وش:درگیری شدید بین نیروهای نظامی و افراد مسلح در ایرانشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72482" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488280f6be.mp4?token=UN4cFGQU2Cy5DCBJAaR6ucFCgeujB8jjdCE7GrqMkaT0xqC_oZ0MfqcZROnbEdtb3b7QoF0-XRg7eSHC7LIE3FOjqVkzEnDKTD8QrduCUE-r4TynqA2-7MLpkMOmL_-fSB5XqauV8uOgseVisjQiFxzfdDK-KJEEnxmPYxv4mpWCkiQxm-Ei9LtFfCc2E7eOihYj4Cc3UgDarWq6LWVyM0zb6yFvMVs6j1Hv_6UYrdwcnUzDf7ad_2OemBgGq9nSXer4qVOKE-ceMcUk8d4P4cCvs23JRb7PKHMCnB-9rmltAM9rEKiA_TYtKkmk1mi-txNC8cUu1ay0znGhP4825Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488280f6be.mp4?token=UN4cFGQU2Cy5DCBJAaR6ucFCgeujB8jjdCE7GrqMkaT0xqC_oZ0MfqcZROnbEdtb3b7QoF0-XRg7eSHC7LIE3FOjqVkzEnDKTD8QrduCUE-r4TynqA2-7MLpkMOmL_-fSB5XqauV8uOgseVisjQiFxzfdDK-KJEEnxmPYxv4mpWCkiQxm-Ei9LtFfCc2E7eOihYj4Cc3UgDarWq6LWVyM0zb6yFvMVs6j1Hv_6UYrdwcnUzDf7ad_2OemBgGq9nSXer4qVOKE-ceMcUk8d4P4cCvs23JRb7PKHMCnB-9rmltAM9rEKiA_TYtKkmk1mi-txNC8cUu1ay0znGhP4825Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره مجتبی خامنه‌ای:
ما تصور می‌کنیم که او زنده است. البته دقیق نمی‌دانم؛ هرگز او را ندیده‌ام.
اما بهترین شواهدی که در اختیار داریم، حاکی از آن است که او زنده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72481" target="_blank">📅 19:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqUJMCS_pzCvAAR-r3xZ8wYUKJ4eUlx5vgIl8aBuAPW7en43FNRxfHxeDTvETSfuVgroNBff593-at6kVEA70r3idU0lQFekSQWqR_lpW1C4SY80FHiFld7DucrUad3ifp92DeF8aFrKea-D7HWb92ypc5s7H285go_P8V9S39G5MxtOMJvUb6SMpWkAVvVGhtbyz7GzTWgz8DoKxIDyuTjc0DNad7h4lwxv7G-ANTsWQ30zOmK0aQl5PXIMucrMv6uvp2G3t7oqZLxNZe2VXdUQBjVqqTiLVfZpVKQOu4MoFwaliEAHnPSk0AmVy17BkiSdm_wvaJssRA3vWzH9VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از اصفهان؛هر لیتر بنزین سوپر۱۴۰.۰۰۰تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72480" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72479" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1I1MazQDDcsyEgCS8wkULGXd0DmFqIHBAjy8Qn_bpy-EO2SK3MWLVBOlh5j-5xt25_QfjPaiqDWMfqmjzFFpW9UiCGOANYYS3C3eESmohgufKfuMCCy-Hu6qQU5q9LHuG00hn-vYwO-q6TRoJPIhyuSrZAMwjRPIYrYnDbcwKgUrbrvtKKgSVZibcjsUSaTztmsNb-2oQT16An5DvTDPjYy20m9TP7tB_1ePCpH1F5xn6OPZ8Xc6bpXXxsccr7L5gmpggKQIobPR7V-L2P6XmHhyf_pefGgdRCxUycpaQjGITQalVasuyVuczYFZ38oM_6wXXfdScbspIVIEpKTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72478" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مذاکرات ایران و آمریکا بدجور گره خورده، آمریکا به دنبال اینه که مستقیماً بره سراغ مسائل هسته‌ای، ولی ایران همچنان رو تنگه گیر کرده، این در حالیه که آمریکا می‌گه تنگه بازه و ما مذاکراتی در مورد تنگه و رفع محاصره انجام نمی‌دیم  بنظرم یه دور جنگ و ترور رو در…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72477" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه #hjAly</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72476" target="_blank">📅 18:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه
#hjAly</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72475" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ برای بار هزارم:
ایران به سلاح هسته‌ای دست نخواهد یافت و آن‌ها در وضعیت بسیار بسیار بدی قرار دارند و به‌شدت در حال شکست خوردن هستند. این ماجرا خیلی زود به پایان خواهد رسید.
این وضعیت خیلی خیلی زود تمام خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت.
قیمت نفت درست همان‌طور که قبلاً بود، به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72474" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
در سال‌های پیشِ رو، وقتی تاریخ کشورمان را می‌نویسند، خواهند گفت که ماجرای ایران یکی از مهم‌ترین کارهایی بود که ما انجام دادیم.
در واقع، این یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72473" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: «اخبار جعلی» را فراموش کنید. حالا می‌خواهم آن‌ها را «اخبار مصنوعی» بنامم. از این عنوان خوشم می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72472" target="_blank">📅 18:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXoIzApGIDjXfYulbnMMn8--ts2ElLFTrGvtMg3-sMLqnWoeWsveuOlJnUNKDlR518clTN2EJy9rOLNUrBRX1Wd8etTLb2qD7t_178trBnFUI9L5JsEq8ohvdZAAevww2oPVAlVdOT-PtBLa3qzXsMjFaI__zRMq0deo_aa8DuaB0zFgyjSTXejp5FW5crRhrAtdkOtCgDJdh3JbQn_1x6QdOn81kGZr4Q6VDE766lGvadQVaoFoTc3PRUGeY4RizTTt_Z6j-JKWqOfPh_a4Z4Ob1kX2JstQOz7xLo7PYpOd9wTlMTuU7osRTQzQCzUm50hB6MhkbBRBD1wgZpDA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا در حال اعزام ۶فروند جنگنده اف-۱۶ به خاورمیانه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72471" target="_blank">📅 17:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=i77S36GSrf5Hr7_wArlkR5-kWtYrsf4WHNT9JMnXhEJSizRwM-BZcRrsmwrWFAcPr6PAqQdAw7GhN5QsLna2ZtZvXXg-msDxgOP8H4uU-1Csv7k86oM58ELbMYZdy8AxTeCjigVk4vrKhUX6Q213Edu4BdjsSKPpiLakUI_8cI8qsB8fCF73c6rM4dFQbA7KljVdCjF1xTTxit7yho5NrZsqAx8FefBrMROp9bRJr5-lXV2rtlPIKdp3qqORAjsik7g0f3WiXvynk963FPo17af51XNGVNfkioDxpBtj-7Ko9CLnTadE_mBRmEo3lCFecJdIL6RUR-sQOikCj8u0FA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=i77S36GSrf5Hr7_wArlkR5-kWtYrsf4WHNT9JMnXhEJSizRwM-BZcRrsmwrWFAcPr6PAqQdAw7GhN5QsLna2ZtZvXXg-msDxgOP8H4uU-1Csv7k86oM58ELbMYZdy8AxTeCjigVk4vrKhUX6Q213Edu4BdjsSKPpiLakUI_8cI8qsB8fCF73c6rM4dFQbA7KljVdCjF1xTTxit7yho5NrZsqAx8FefBrMROp9bRJr5-lXV2rtlPIKdp3qqORAjsik7g0f3WiXvynk963FPo17af51XNGVNfkioDxpBtj-7Ko9CLnTadE_mBRmEo3lCFecJdIL6RUR-sQOikCj8u0FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی میلی گلد دفتر رسمیش رو جمع کرده و دیگه پاسخگوی ملت نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72469" target="_blank">📅 17:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=rwaeXvrNe4ICpiBmV4YUkHAUlCb5LACI2_3UtHbBRexuLhJLPhUEoYxEnj1UFmwOkXRcEea8ao-ehOr5CDhPjjUruC-lOyFXBLrHlqMYEHbO9qpnVSlbH5ZDTtYl8JmO5q2vyN9pA0m-KzzyYQAME_k4MnqpkB_cU1tpi1KNiWhObtqIRY9tuVVHSJYE7Jc24T6kdT3awGM3HFR4TTVr_UHp_d2TjnXrHwG2DlFshirYWc75pV2bCUyDOnO7Hg-r-YO66mHPKGg74D8n7BbXFeBzFDTcGCwfR9JWowlau8v02VMWDcDB_7ADXiy8-GhNe5eeZHhofYWsv8Lof0lVTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=rwaeXvrNe4ICpiBmV4YUkHAUlCb5LACI2_3UtHbBRexuLhJLPhUEoYxEnj1UFmwOkXRcEea8ao-ehOr5CDhPjjUruC-lOyFXBLrHlqMYEHbO9qpnVSlbH5ZDTtYl8JmO5q2vyN9pA0m-KzzyYQAME_k4MnqpkB_cU1tpi1KNiWhObtqIRY9tuVVHSJYE7Jc24T6kdT3awGM3HFR4TTVr_UHp_d2TjnXrHwG2DlFshirYWc75pV2bCUyDOnO7Hg-r-YO66mHPKGg74D8n7BbXFeBzFDTcGCwfR9JWowlau8v02VMWDcDB_7ADXiy8-GhNe5eeZHhofYWsv8Lof0lVTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72468" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
نشست نتانیاهو در ابوظبی گسترش یافت و نمایندگان ۱۰ کشور را در بر گرفت:
امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر.
ابتدا دیدار دوجانبه میان نتانیاهو و «محمد بن زاید» (MBZ) برگزار شد و سپس سایر مقامات به آن پیوستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72467" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=XGvBF_nRdFqNWDX7BAu8x4p-0LfXgQ74tB-hkLjzWiuSSFuF-_UoU4h-tJjMlJRjazcVcs0gUsH3FDYHe8TZOc69V1aw3t8BjLvUZUPaYzV7bjinKaR-MGdcUQo4orJBY2AQ78v_Oea29sbnoAjbuxGrWB5gu3sTh4a8OyalxJHlWTVx-38d2JChkxcHDa0TDpjAmwI4511rWXLTKnTOlETw4CtOC6gQTX78bR3yvRoN104D7wxYw4Chf5aoWewMbfdKVcoZ-urvryGjm4jTgvXmOq3ggXqyufjp_38hC1ZCnnL0Gi8eagg_o8VZacosdV_w72e_l27YtOgpRvLg6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=XGvBF_nRdFqNWDX7BAu8x4p-0LfXgQ74tB-hkLjzWiuSSFuF-_UoU4h-tJjMlJRjazcVcs0gUsH3FDYHe8TZOc69V1aw3t8BjLvUZUPaYzV7bjinKaR-MGdcUQo4orJBY2AQ78v_Oea29sbnoAjbuxGrWB5gu3sTh4a8OyalxJHlWTVx-38d2JChkxcHDa0TDpjAmwI4511rWXLTKnTOlETw4CtOC6gQTX78bR3yvRoN104D7wxYw4Chf5aoWewMbfdKVcoZ-urvryGjm4jTgvXmOq3ggXqyufjp_38hC1ZCnnL0Gi8eagg_o8VZacosdV_w72e_l27YtOgpRvLg6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل:
جزایر تنب بزرگ، تنب کوچک و ابوموسی در خلیج فارس، جزایری متعلق به امارات متحده عربی هستند که تحت اشغال ایران قرار دارند.
ما تداوم اشغال این سه جزیره توسط ایران را به‌طور کامل رد می‌کنیم.
هرگونه تلاشی برای جلوه دادن این موضوع به عنوان یک مسئله داخلی ایران، تغییری در این واقعیت ایجاد نمی‌کند که این‌ها سرزمین‌های اشغال‌شده هستند و نباید تحت حاکمیت ایران باشند.
+کص ننت:)
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72466" target="_blank">📅 16:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72465">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=heClltgWfJhz9xE5xjF05e6M8p21Ubnuzph4Zsl9WjgCPZ-QfUy4OUyuwZG0QIL_cOm2eG7XK5cMojHLuLZ5Y5Ae7f2S33tWsdXHHjzBDsE7MngSgBoKvM__6_VhNHBqXBnKmZMEAA70qRTJn2WYw4DjBrk3cK_CpxRHn-PdHGoCQbNqwydTgLP4TbnE5W67LsdljLyOG-trMBuapRo1j4BaP0docfTCa02z6KExjXflYUzo8sudFA9gPqMVUqZUZpXG7ocfD747bsYJ_CqfpUYzhfRwnizzn_JB5Kd3ZuWFntdf8Sow9d4bDn0TxdXWeESyccFJYqVkHNLBmprgrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=heClltgWfJhz9xE5xjF05e6M8p21Ubnuzph4Zsl9WjgCPZ-QfUy4OUyuwZG0QIL_cOm2eG7XK5cMojHLuLZ5Y5Ae7f2S33tWsdXHHjzBDsE7MngSgBoKvM__6_VhNHBqXBnKmZMEAA70qRTJn2WYw4DjBrk3cK_CpxRHn-PdHGoCQbNqwydTgLP4TbnE5W67LsdljLyOG-trMBuapRo1j4BaP0docfTCa02z6KExjXflYUzo8sudFA9gPqMVUqZUZpXG7ocfD747bsYJ_CqfpUYzhfRwnizzn_JB5Kd3ZuWFntdf8Sow9d4bDn0TxdXWeESyccFJYqVkHNLBmprgrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیروهای رژیم در یکی از هنرستان‌های دخترانه شهر اندیشه برای تشییع نمادین علی خامنه‌ای!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72465" target="_blank">📅 16:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=HASHGsM7xYMhbyzoiSvll6_9ITEE-BY1zsmJ2KXW1YFNFwrxJP1IrxWImxWk2NPrX-1v2xcYK2GOJ55A2MLiLAloyDjrbuPVbWn6957d_Wq2_O_ZQGfxuqcthO97BIcdtEY4F1M_XZ_OAFRXjAWPSgx6BvdjbxHtDADeicO8iwWNhT4OiVCy6SI0l4H0LfE9newtG3JRt08mBfJF9L4lYq8h7MJKkxjK3qX7crc93MalyN2c3XIoMW5nN4HQfIPYbve3TgD9d9ebzIEWWqUuhchxIHsHSImcQ8v_zd14Wqn8PInZdGLUaLzawI5yhPLxUAUfXNEVkh8IAu_5tVqszg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=HASHGsM7xYMhbyzoiSvll6_9ITEE-BY1zsmJ2KXW1YFNFwrxJP1IrxWImxWk2NPrX-1v2xcYK2GOJ55A2MLiLAloyDjrbuPVbWn6957d_Wq2_O_ZQGfxuqcthO97BIcdtEY4F1M_XZ_OAFRXjAWPSgx6BvdjbxHtDADeicO8iwWNhT4OiVCy6SI0l4H0LfE9newtG3JRt08mBfJF9L4lYq8h7MJKkxjK3qX7crc93MalyN2c3XIoMW5nN4HQfIPYbve3TgD9d9ebzIEWWqUuhchxIHsHSImcQ8v_zd14Wqn8PInZdGLUaLzawI5yhPLxUAUfXNEVkh8IAu_5tVqszg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درد و دل یک معلم منطقه سیستان و بلوچستان را بشنوید که هر میز ۴ نفر دانش‌آموز نشسته و درس دادن برای معلم بسیار مشکل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72464" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72463">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی ایرانی «کاسپین» در فرودگاه استانبول، به دلیل بدهی ۳ میلیون یورویی به شرکت خدمات هوانوردی ترکیه‌ای «ACM Temsil Gozetim» توقیف شد.
این هواپیما در حال آماده‌سازی برای پرواز به ایران بود که مأموران اجرای حکم قضایی وارد عمل شدند؛ آن‌ها ضمن دستور پیاده شدن مسافران، هواپیما را بر اساس حکم توقیف در فرودگاه نگه داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72463" target="_blank">📅 15:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72462">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Bi4C1NoqkFHYAzmezUiCFbhx7kmjlmm0kcUH0Fvqvht25Q1jhqpqug7krM6d-WkxoaS_tj1vcA465mf6o9sRCgLwWbXU3W26_dCXvC7tMevRSc7VeSF7Ztiz_RMK7daxCwJBAhDAVIf3FiDbShx69RPBtJ2MMdBJbzKXytab-yxeQwvwK3bYq24KIRgKdPhdR91nUXqAWHM0HBVN3IDc47g7DhZZH3TaX37VBeQQNaUrLJexy8-CiHklgBYUahSDF_B8JBYQ7pLCHSHFHCe2ApMYZgqP2JPy-b8QKjq1Q1-Nt_O6Glu_j-m5NSBTeMeFqHg78ErM4GGbtSlVHndX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Bi4C1NoqkFHYAzmezUiCFbhx7kmjlmm0kcUH0Fvqvht25Q1jhqpqug7krM6d-WkxoaS_tj1vcA465mf6o9sRCgLwWbXU3W26_dCXvC7tMevRSc7VeSF7Ztiz_RMK7daxCwJBAhDAVIf3FiDbShx69RPBtJ2MMdBJbzKXytab-yxeQwvwK3bYq24KIRgKdPhdR91nUXqAWHM0HBVN3IDc47g7DhZZH3TaX37VBeQQNaUrLJexy8-CiHklgBYUahSDF_B8JBYQ7pLCHSHFHCe2ApMYZgqP2JPy-b8QKjq1Q1-Nt_O6Glu_j-m5NSBTeMeFqHg78ErM4GGbtSlVHndX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر منتشرشده حملات پهپادهای مولتی روتور FPV نیروهای اوکراینی به سربازان و مواضع ارتش روسیه را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72462" target="_blank">📅 14:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72461">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=LPdHsvy02MkCaPp1Zf3NlCAddhmfarWfu2qoCzAYrloBHzKd3AWOPGZng6uY1Lp5z13pL2kcC1XlzVx4pn_iGQxaqmoq8wC5ga1VvAWNYM2tWzDkxopEt07p2wbhQJGTZbQbrxNA8gUc30yGqOz0HtoKvsk6R7I5KGGrWRE-nM1Y7VKtyrHgsi1ZGw-9DIxgl7kPh-zbyqUBGbKd2K3aOqAdJMOwcoRLyUqINkdaMLFokfQqCyeuq3RNZA5SW10q826v0GU4PYB7rA6N6hOwdIuIMZgWwngxx_Ig_y0RcneRZ1kNgBeqIhrHzlNa2lq04gt3gJ4PPjxGEF506qdq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=LPdHsvy02MkCaPp1Zf3NlCAddhmfarWfu2qoCzAYrloBHzKd3AWOPGZng6uY1Lp5z13pL2kcC1XlzVx4pn_iGQxaqmoq8wC5ga1VvAWNYM2tWzDkxopEt07p2wbhQJGTZbQbrxNA8gUc30yGqOz0HtoKvsk6R7I5KGGrWRE-nM1Y7VKtyrHgsi1ZGw-9DIxgl7kPh-zbyqUBGbKd2K3aOqAdJMOwcoRLyUqINkdaMLFokfQqCyeuq3RNZA5SW10q826v0GU4PYB7rA6N6hOwdIuIMZgWwngxx_Ig_y0RcneRZ1kNgBeqIhrHzlNa2lq04gt3gJ4PPjxGEF506qdq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آن شب او یک ایران زخم خورده را به دوش کشید.
به یاد جاویدنام حمید مهدوی، آتش نشانی که خودشو فدا کرد تا معترضین رو نجات بده و در نهایت با شلیک گلوله، ۱۸ دی ماه به قتل رسید.
۷مهر روز آتش نشان بر حمید مهدوی ها فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72461" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72460">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=n8dtlF2OzDaACTXkx-_iVPweMMWVKOvgMuP02Y3ta6qWcRvRVGpcRvfAgHcvNFbaljycyQ4LSJt43VN5OQIaCsfesqEcoc2ZGTCaIKBVnQaXuMalcyrwG9mqf1X1J5i5scBlYtI2JGWBlXefJUu3kBhhqpI56KorZwy6DB738K1IeItcqsYDY3b2k3MicggYkPzSeFVmuvCJ2bnkWB-qkGOSI7rt3yaC5R9XqYG80xftvbaPz_isd5QBiiDdExdkJmNPhAvcbUD3P-HIY59KErh5lseswGwXqlVnvBhpHFxCsyBoPfQkkbIVA4m2zhlQH4IJQyRNFdIpLsLB6rT-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=n8dtlF2OzDaACTXkx-_iVPweMMWVKOvgMuP02Y3ta6qWcRvRVGpcRvfAgHcvNFbaljycyQ4LSJt43VN5OQIaCsfesqEcoc2ZGTCaIKBVnQaXuMalcyrwG9mqf1X1J5i5scBlYtI2JGWBlXefJUu3kBhhqpI56KorZwy6DB738K1IeItcqsYDY3b2k3MicggYkPzSeFVmuvCJ2bnkWB-qkGOSI7rt3yaC5R9XqYG80xftvbaPz_isd5QBiiDdExdkJmNPhAvcbUD3P-HIY59KErh5lseswGwXqlVnvBhpHFxCsyBoPfQkkbIVA4m2zhlQH4IJQyRNFdIpLsLB6rT-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
افزایش ۳۰۰ هزار تومانی کالابرگ، پول یه پفک هم نمی‌شه.
سخنگوی دولت:
قطعا کالابرگ برای خرید پفک داده نمی‌شه!
+بیناموس مردم با سیصد تومن بیشتر چه چیزی میتونن بخرن؟
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72460" target="_blank">📅 13:51 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
