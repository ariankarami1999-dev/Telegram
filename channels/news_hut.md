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
<img src="https://cdn4.telesco.pe/file/RL43ruEtqcGwsh9m3dN0nKxVwM1sKBucpSi8Q22f3XoVqENTABM93ujHpiFWU3Y6vr62Z81K1W7xbp4HFFsvbdtucW85XOSjCcKx4B6ujTd8EVszlg0Oub2ZuUVyUbnR-csxKH6izTDLeSkNLbUUca1YQo9kkwcJ-vfz2qqrQsNIgUybYkfxDiZ8ZPCp5kohv-C2Bs_QTFsst3LjjJRYKWy70GCjwaugATcb60toIV8SPHacc8K-9LoeTDWJ7P7xQT1XLPeRZ5_xHCKa3zwNpTGPdAa_yMxNGlIjxXKEQGTWXB3wm-TPhny6RFixkc6TpA22x9hFzIfo7UrfECH-pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 212K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-67230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Utxr6c3baWsNa-mSFCkFYGMEgCIsHEHmFs6TI2aG2uhsXToBlyZf4pvHqY2dbiQPXRxJbZCuRvi3ei-DIczqsz1WnoWzOzImLnQFG7180Vnmrgv0gCdPzuQ8q4cLQ0PzcRAybFI05S5c_ZQdSIE36ochHt2jvpmeg7UZ9EKvhLTyS1OQscJiskZpwZ6SNuS8SBbGMzsDDHVVU2SS36xxR6LoHKBI4XumUqqNwcwLXAi3q20u1hKDA4exv3YlUftKukDnFAaaUWKINXPbz48p9zXDe_QSWbY2tyMRr7u4U-iWXlP4gAlggl_q-xpHaP-LnUxBwNMyUUlt6MaltwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رادان: یک بمب گذاری ناموفق در مصلی خمینی تهران شناسایی شد و خنثی کردیم
با برهم زنندگان امنیت تشییع جنازه بشدت برخورد خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/news_hut/67230" target="_blank">📅 12:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vngU-gluAq2W7NrN-XrlXjiU-py6pVm8p2c3OM87UcorsBppSzzd2Bjh4IuEINnOxslNxipm7Hz7Toj-ubB7FodO2iQqg__75eoQxnKI4C8o9PALuY6wByL6jEqJT31n9MkvHUkkpODg7YUif645cp1zfT6XdodH5i_N1DVMbXA6lXbjgCo9-FoNQ3wHK5zSpO_1L0BlH9Qlu5dzdm0UibkxvIoQw8n5RKKvadCFywvT-ayW-9LUccOiJ13ZhSUPB3dkVZavJDp1u8GZ4OVN3Nq-zVnkW_WQ2-9GHiW1Sk7vIyM4d8q-UHOJZbq6NezfcxVFDRqzP5Niqnm_ARJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkW608S4bQ927Sx8P9ZG-VBQ8gLIRWq6mtJiF-qgIp36m6z5abIC-0V5XQBqZeJh2H_BKyBEGMP8-VnuaYWBPGa92faMHtJ2X4UcHv9VC0GeYymbHwoA-GHza2_MahDGSDtmaClsuZqsxb0KIvm8ZQD4Gv4m8PewKRILh1iex5qjYvOvhn9keVzK9Tv5EBj0LHn1lGPLQJtVnoBwdYspEkpiBEnJABPbZ9bN0LtNrsJnyC-xsSRWqhnMOFrgOPywKY4GEJaMdQIn8PjXYkv4i0PmBEZ5XAMzELA4J-7XkcAYAkb6bSvr5eJn8_MVC9xWt7ZWZLe-uYPbnkg6m33_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE9hlzuE6wHxUBLtmlUUvV6NbH-y91Gh4DyiKbA-bCYPyhaIWid_xqSYSIAPHFq0AkAxSZrfrmybelu_zSl0BHGW19P_QIardt4J6kCmOCtaB4GJ3Pxrv8Z3Al73QvpJ2VSZfAtweHZeKtR7tgagRyPZaRS8lZFBARsWedxEyGBPFgtCol7mbV_rx9zq1g2E-mhAoZRqhY6I21lAGl96Nxy-U66ySmFgbWJJtBiMcEgs7xE1FwoCGg4yeClFX8qjGezGXDcCer5C_00s1XIcYa3hE36DYsXftMn0Gw0i2_6-vVnQ7VQ2Ezvomc0eW8jZQNan6tZ4ib0Kx2uui65c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYIhj6ck1AJSyZn_Ato6ALO1k8t4lzJfkYbl2qH5Wz7Nu27HmE300pd8NbV43QkZjaOzRbNyYNUp78TkTLfY7Lk6D7jHu89qJ307rkZ1u7XcEqHU5s5y2HZIfKtfr3_TeAhw8lju6Wuwov7a17TP8ftz4p_Xz9y1au7VRXz_ArdEsXds7IVp9Wvg7t8R-LoUAoD6J422DNXo545MoRog9o0Al5DXlHnyZakFByP65LhbedtCT2TGh-XwygGTWotgCJxukNprFhNNG-oTV-O0cBDScJNKJPzJNtxkuI1l9NU7J5OyKhmIOngW33Y5s3TGTHlOxtcReHI71k1CM2RNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHNBOfObDhohgiOJ2eTtJrHwocUrIerEjuSUK8UoaoxldZT1ILI6I_-J1ec5dAm3iT04duOiDSQ-5jhTbub-inkfW8n7r56l1_IaBVr4NTqzgm2CbNrK4umla_Dg-KNWy31yoCw-jvpaYSIsioMGApnSz98ySp-Qtj97yW4VJGGkb6URkAEEadKw0cHdqbaB7PwI7b5PKx2OHfoPMWPBoGSHmEGqP_QkFJzD5P_AJdQRjuNqJP9IdE6L8NhlSDnFo4b2P1jzKdiZI9TZPa3qSgOO2mI4DrTjZIpjJn4izOAKHXQAS5oUPi1Oehd-mwIRnAI6CoAA26q-QmrN4wtVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WnMkFW8uuNJdoL9KyJ4ULuTB1w2a8gfXlq395jR-TcM5S3UeG9RYpaVI2PvXembJIm4eSadMHqEU9q9dEetSbL87YoljBnF37zDNMxSabv1NHkbKN0oeM8BvN5M0ORJGgNPbt2Emf4EykeZnZzFvsh7ySTkohRkhQstx7a0Oe9J_8EZDPhWtMYDrvnNxjxQF3vVf6vthPEy68FKjK2kRkkZvzNcYgO0z-rniSvkrVlx-ImglECT1Jk7BShtIvRs-ibciLXOFDwQmoyO1L-vgntnBTMNgO5I_4Jqf5bnO4HlWgqD9aYd7AV6lRZJotThEg-jOJPDmKsjd5vfC-s3g2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WnMkFW8uuNJdoL9KyJ4ULuTB1w2a8gfXlq395jR-TcM5S3UeG9RYpaVI2PvXembJIm4eSadMHqEU9q9dEetSbL87YoljBnF37zDNMxSabv1NHkbKN0oeM8BvN5M0ORJGgNPbt2Emf4EykeZnZzFvsh7ySTkohRkhQstx7a0Oe9J_8EZDPhWtMYDrvnNxjxQF3vVf6vthPEy68FKjK2kRkkZvzNcYgO0z-rniSvkrVlx-ImglECT1Jk7BShtIvRs-ibciLXOFDwQmoyO1L-vgntnBTMNgO5I_4Jqf5bnO4HlWgqD9aYd7AV6lRZJotThEg-jOJPDmKsjd5vfC-s3g2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Aq-ZC0wq2-h4KQBeFB6anT5PWywcVADVm9T-i51K8Q5cJ59sI50w0YVXh3r60XO4uos7BegUhype4r1RUJAJhGBJoSjBkRZ9r9Yf6JyXQE6CJyzUxJ7_cb_GWXMQkooH8LL56YbVDU6VTT3FS8MgWir43rzNO4XAUKvoYiqZ11EbAv3ci9veuBqJr1PZNS8Q4vtzsBQuYB1RJ0mTBbF0mE00WQxZGyFwKyPZw8r428RNQZQ8LkwquiTpDrV8VDUnm-1IDOLcUy6rfjQZTfHU4EbJ9exNuGEqga8Ck9ndaPk64LCbB6RZ2-fmGajm7OIZ-Ch-wRTcHqmhOdcJcsk5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Aq-ZC0wq2-h4KQBeFB6anT5PWywcVADVm9T-i51K8Q5cJ59sI50w0YVXh3r60XO4uos7BegUhype4r1RUJAJhGBJoSjBkRZ9r9Yf6JyXQE6CJyzUxJ7_cb_GWXMQkooH8LL56YbVDU6VTT3FS8MgWir43rzNO4XAUKvoYiqZ11EbAv3ci9veuBqJr1PZNS8Q4vtzsBQuYB1RJ0mTBbF0mE00WQxZGyFwKyPZw8r428RNQZQ8LkwquiTpDrV8VDUnm-1IDOLcUy6rfjQZTfHU4EbJ9exNuGEqga8Ck9ndaPk64LCbB6RZ2-fmGajm7OIZ-Ch-wRTcHqmhOdcJcsk5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Z7CQ3heON4lsdB-xac2276fQc8-_NkhZGllNrFJBlpAum4JB_Yge1SSTDJlI68s6pnDuv5rvRZcGxvPjYZC6Y-Sh4lAXry335Q6Txo5CtJ-mTNW89k4wJxLlhksrLwIat5jBmhL6vMd9U_Eh2Pq3RPmCDF8lKX0lby_SrxVH3237xBH1nUHNZnOz7_G6kck-LfyxWL6gu_gyVUuvOXpC4AIqEwzoyfbckYQtcvi8GQ28i8i9v6Q8PZdS-dTo-HgOmSWRNlA8hPg3IiXXwANEnTAmkhuxqVeKrpbfgE9GtZ__e5L2zqX3-2wp1ytqpiz_6dvI5Dd3PBQKniTuUWVoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Z7CQ3heON4lsdB-xac2276fQc8-_NkhZGllNrFJBlpAum4JB_Yge1SSTDJlI68s6pnDuv5rvRZcGxvPjYZC6Y-Sh4lAXry335Q6Txo5CtJ-mTNW89k4wJxLlhksrLwIat5jBmhL6vMd9U_Eh2Pq3RPmCDF8lKX0lby_SrxVH3237xBH1nUHNZnOz7_G6kck-LfyxWL6gu_gyVUuvOXpC4AIqEwzoyfbckYQtcvi8GQ28i8i9v6Q8PZdS-dTo-HgOmSWRNlA8hPg3IiXXwANEnTAmkhuxqVeKrpbfgE9GtZ__e5L2zqX3-2wp1ytqpiz_6dvI5Dd3PBQKniTuUWVoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuMgUcNhEA2vQq2LfW_K5o9h8H3Nz3Liv7rmjnyDYkSSA6sN6qsT4bKhGyUKHyV5w0du8_I1_Qphs50pfSLDim7jnATibj3nSHD35aNnqZoWRohesqFlgGKwBCRkDXIXHJSa8CsmBwAIaCG2He1CiFhfOylU4IL4uJ4WkYSMET6pTX3F9sFMft50r80ADushpFG86zQs87fQMXFb_Xz21yjsvZusTrV23ZC4mTH6A_y3qGUEeSrXizc-85ErXHU5mRkwt470so76IOxg-bOLD_nwIIlMRo8G2wTcGDbQozsvRJgj6fwk6hD2fmxcFvi3HIdozi7fqyZlF2qo8q8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuz0732779nWRs8b2cUuUDWdgS68-oCsUm06cdpwdqBuH2J-k9_sQ248bptz3ss0XZ3qS8ubrSUIU5xQlCV08czd1XAV22JhOH-svqCjDXZ5yEa6PwMj9GPifGIPgCnMy-lPN7ctKHHhirdZ87iaCEl5XnaXvcF6WICObR3uqp_6oBTGzUoVEU8-N66KQ6gjLMyWVneznkxfriPOHHcPvTjPlGNy1klCuA2TdyawvqLjAnXOU_qO4Cgw1XoaHuatHYNpa1b0wwzjPzWBfrslzsqaNYcIleeQD-jSm2XMAI-dBNQmdiMttIkWR3KoZyGXxFxM5XF63yUrZyRGTjXIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQzLW12fcu_3tWKsVQa9HXzX4CchRGQgUhEbfiwPqosOD18R-ABbvvfcNGM6qdBnepHXhIOCA-cf2BoFQYckPz74Mf46InfqMX7rheGDqhJ-EI6LGpf-AfEkNhLWxiykNH98GdxdM5o1PygHzLNho2UjvgEt-Y9bqDpAcntAqws4-UdlxUSVmUhGbrTv4PjRdDH2sku22gNBAdWU6ljetXtXEa_kh0hPpCtBgIM8DofPpZlJi1nuzst-tFa1f8PuWGsEgb7VzNRJAC_4_Qyn1aPiPWdS3uh4jpkYMZxdpjNKBWUSc2pufo2qyvVdSQHCe5aZ6FEciqTBL-06Ep4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IMd6PvIQtfL95x9JoCWpAxXEkyBUaPtU1jPdhIMcGj3ZEwSTS7MwwsgYR5slKPC8GImtfwSXedf5Pu9SwP4lSXw_AI-V82fpV5zrSywt9D6V4gTblnqgIyn45ldxQWBk93VMFR9yl1itvIqKL059EHXRnhPvJGi3umD89wYe2oXe5C6TEvEq0x4ajj8deUVB5TEOoL5RQXLSz88g_XSJJXZaT-EdeGJe3jOk7qHcwB4MkPlVnBwsoJNKrvu_cwJpIyfK4udfmRjCTELoAXoiETPGOHR9s7GB9dhQ8s3CNQox7Gkt5SksilDg93B6v93Z8oPyqj94r042MbNKKoH_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSaI0hksBIEj3BxMW2xqHeIFfxG0Ey75XbiaGyWasBhcPdOcrSIYlLbGQc3Oq3Q9vak5XXAJrRJ5Z-6-XxZPQ5p5wz-x8N3InAXq4jIhIWOwc_TM2QKX1IeQeWK-QMRadwad-GlilSYEK_-Ay8G-YcbrJbJK83-DTtZ7fhcIcrcIYXj9mzg5UrsAYehYnBCJbwFD6RNAMHQ4fD5vyCP9nXOkvhQMKgr4V4Nt5C7rlc3BxxBd5JK_6aaNBOViEejskyRYpfPHkqU2Lqzhe4P_a2KnUf-rHoq3d5YdOE2DVgZYMCHluDb3F9z-zNzAopcF2tS9GzjiNuv0_m6SnAP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIMDjFAkbnSqgNKc4hMlkn2Vv9ODgjeQDRgWt_WwZ9XO-Em7uMsE8CcCo-79bRVIgQaaL9REDf1-jhHheG5aiP_qkZxGrwmiqMWgYwhiyHkBnT7_FnXOdgNNuHzbRWoUO9c3VS_1YdoTRU8tQkVWQSWqlG8mhg1qIFHURxZ--ao5OmB4K24MBMCS_A42e-nDfzPrUxW0COTbOm99CE8pczo8pkbEowD2U7sE6roaWdZ95e8k47vNmc9S27QS2I1KWGq_BV3MTBbzonGBJyhl3SfNCsK-B7wU6vV6gmifLDoIzqM7kXr-CMHLWJBmGcraWZYQsa47gTIW01NgqA7img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZlUCuV8Br1MVBvjZtYPf2PYxbqfzC0FjRZsbTzgoUZQNIQQUREjNQAdWboF1Yp0fJfVC6ysTGNq9NVwlGYKVWqZuofb5lXJ7dtuNDypnvPloOxAzsZ91GfCdqmveJaH8_lSeRViCN-O3N_rdUAqfCU1o8VyjYnaYFGuSe8lwmhQ893P3g5f5eXlYqRQ2-Om7u8znHk8oXQfDlnLovFV1hGofIt95y93ftnpXtiaQxz4XwTuxSqrjKDPl9doAHCWUjjD6CFigHy67a7rM9pXkVrgyr4OSq9V1dVTd3CJ_6GL53L0byW_6-lZ4n-RUBsjAVqCyqufu3zNUDpBgj82vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU2Cguk9eer6Qmt3nyw4KTOC1UiVWabBYUoa_xeTIA-ONq1RNMSXELp98XzRwDvUfrZMfk-eisDnYgt6KgmSCV54fYzg3kOirN8P82DqIKcDayp-f_PWRBNlgBEGD92i-SW5H5_S12btL-sJty89Hvf8gqLjxWocl2KNX1YbyPBHH2NF5STu744DPZWJDXWOL0PeXmntjh6kKOdfzn22f0IhqBieWdWG7DXYKwEBpkWxw5qkPV7cs12xyDEGAjj3Otrg-92ZUSYu5tB5mAezT_OQFceAEOFhvB7an4qZlbINtWAvymweKy-OQvYOhfg4egxTboTDnldMG__7i9pn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubb6o-OZHTABBLm-2T8ihBwimfYmXrF4VN1ZWRiSKvYtj98joJCfIybbpf6RTCjN9KNaQZhMy78tkTKisU6cVAi54X6vxNweiPa0blS59lqND9eCA1o_SJgnMRIq62kKy4L1OzuYD9Hl8G0BNYoYdQuxg-BShtTLuCsCxLf_n0lK1oEpyL83nJyUKhmO32JbIURWM7ngPgb8kGRW_dsK9DomjYXmqMHVaYUsjGWPh7LrLvbqpdwg8o5x2_s5SpJQWudUDHopqqliay81iqHjh7G5mxYR0QsU4a4_w4yQb9MaoBn6iNLbxgbhtdtUXD4zvbc3ZJbAEQQ3EpYTOFDCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=gXMnY6GsTcu9Z2jdvnwBbSRTOHR3_xmSFfAunCwcT9d11I48WU2rN9xaQAwIEoIgfX2LnEkEcp3w59AALOqeqPbkwNodlWGI5SavcW48TzjNo5mGEDIPMhQIaXSKD__eW0RBS6SBrm3hXKLH6_ZkM4n8NfIY-vsq8hxCbqMeIvyTLLX7rTV9DVR67tpU1jfqaBhIhYRPm4OBY_vKmwpuaM-unI_tNAfbl3lqgO_cMc9bnJb0ZYIaj6W6OqbCFRXMrRIw84Lx805yVvK53AkgHod2ZWJO5CVQLmaiR_sFmcZPQ6XXoDCYx_sWOAB5Q-6iM0K6JPkZsM6F8HMtZoGf4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=gXMnY6GsTcu9Z2jdvnwBbSRTOHR3_xmSFfAunCwcT9d11I48WU2rN9xaQAwIEoIgfX2LnEkEcp3w59AALOqeqPbkwNodlWGI5SavcW48TzjNo5mGEDIPMhQIaXSKD__eW0RBS6SBrm3hXKLH6_ZkM4n8NfIY-vsq8hxCbqMeIvyTLLX7rTV9DVR67tpU1jfqaBhIhYRPm4OBY_vKmwpuaM-unI_tNAfbl3lqgO_cMc9bnJb0ZYIaj6W6OqbCFRXMrRIw84Lx805yVvK53AkgHod2ZWJO5CVQLmaiR_sFmcZPQ6XXoDCYx_sWOAB5Q-6iM0K6JPkZsM6F8HMtZoGf4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=YeERrFlqNQukmfZkfAATk-BEj0MTbt4gobJZ-PtpP0pxq3WMZwCWY-4t3toBugp1iFP-cmC-TcCU6Qf0Ipw0BKEAbS2yOBNGWnOi_HCYvI46FS7_YoBZpQn7Wc1CpsTYPG4XpZUICLVs5_fO42Kq2ye2XUBEuTNf2x7NOwY7h5jMnyQB9QCrPNp9L3bfdWXcU-ZXZ7UEMAyETmBQWfUNGpQI9svw99BnhS27CtgMLIkKT1uAu5oSOcykVPIsDCbRJpvjkKQ-tu_hH_fIlNekiQc8jtC_nfTUemz364EBgLbL_qlU3rX8dtvAe7SJongghTP-IghOrqIHhSgNvKAQaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=YeERrFlqNQukmfZkfAATk-BEj0MTbt4gobJZ-PtpP0pxq3WMZwCWY-4t3toBugp1iFP-cmC-TcCU6Qf0Ipw0BKEAbS2yOBNGWnOi_HCYvI46FS7_YoBZpQn7Wc1CpsTYPG4XpZUICLVs5_fO42Kq2ye2XUBEuTNf2x7NOwY7h5jMnyQB9QCrPNp9L3bfdWXcU-ZXZ7UEMAyETmBQWfUNGpQI9svw99BnhS27CtgMLIkKT1uAu5oSOcykVPIsDCbRJpvjkKQ-tu_hH_fIlNekiQc8jtC_nfTUemz364EBgLbL_qlU3rX8dtvAe7SJongghTP-IghOrqIHhSgNvKAQaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=lEfpNv-9r1UzGUVR7MrGBewfqymQ3NjMxhx31eQBZ_prpQFjyU4i9HgAN86WjzHyvbw7flirhYs0UeL4_ehExbAcNyiNK3X08poiXTHKi1nWGnbiKNcbPNxSM6ZYlY3D_5qpccJkOhBrRYHPB_Xq4JRGEk4-6zMCrhvezARZBDdByY9_cIuVqUc8QndYsqjBcRFCQvmpYHC2wLqCC__JKGLIVuvMd8OMu8Q4kLj0Rt8IjgPYJ5YGgNup-ON00ELrau2wjhRrapEMBW5I4n9e_8ZGrTtueeMjoHa4tdMAeZ8kLRiwImsDQV06StXuNOSXalVYJZa8ofknc0vH3AZA2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=lEfpNv-9r1UzGUVR7MrGBewfqymQ3NjMxhx31eQBZ_prpQFjyU4i9HgAN86WjzHyvbw7flirhYs0UeL4_ehExbAcNyiNK3X08poiXTHKi1nWGnbiKNcbPNxSM6ZYlY3D_5qpccJkOhBrRYHPB_Xq4JRGEk4-6zMCrhvezARZBDdByY9_cIuVqUc8QndYsqjBcRFCQvmpYHC2wLqCC__JKGLIVuvMd8OMu8Q4kLj0Rt8IjgPYJ5YGgNup-ON00ELrau2wjhRrapEMBW5I4n9e_8ZGrTtueeMjoHa4tdMAeZ8kLRiwImsDQV06StXuNOSXalVYJZa8ofknc0vH3AZA2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvbI3A5eZ03EW_oJ77YkCki_MbHtXmAmX4KXH3-vqdg3IuI0KJkxtjdpuEBQZknxsZiraYzY5-r3-P7B8BV1ySghnPFGGR-mWSAFo3eJdiyRYBRIZqnM_RPkfZpz2vndCGxsGyD9OAMvuRWm6xKW1lM5pU0fxx-v7qNZiCBoWsvtNvf7H875Z3S_KC-3gmqY_PWY7b9P6THzm0oX7Ola4su09iddXMOaaqPSntl8fuxVGqnh5ChsZaNshA2WrnAditVPaXfBU6JEdjFBAnUD1MPIPqND0z8ee20vdJRBOL4W9jqPlL27ReAB-6Terx8jq0Pj5QqV8PJNd-xlyFJCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFtB9zwHTzrFvgBrUZu7bz9Ov98daVI8jz6dJ8Q-mWxV_oKWXBSTtxbHfIC4bmF3W57RprhoqUr011Wwt2gGdefw8sxfxFhS6yWxRgTnUTd7I8VAgccqkc7Exbt5f6S7J7Rp3XLANzTMmOG4Nn3Cizy7DDTpizWho-Xghfmz0sBP-m_T6p_tO9Ac0FZYr6bJX0E3trlIHowHLIcMz3TphuGV3vulSCUgzna4530bqtFuL7UAtgfwgjNwj1AlNwhZb1FfPof2F57WkcSCDBAkDEoUxmaPSNjxxNSzhWCYihRiLM8Sd4W1cnzibt3C_vtqYM2oHoniQDgSlzAWVToLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLcEqUeB59sYe8m2iWRpsPfgGNV7IO9nQY4m6BgGSiLyXKKDzNOVlNHXQfEdbAZ-ZRQR_W3FvH9qMQwhUoKfToLhpy0GcO9_kIktmRIwBwoeNEaU3_wpW-uCEoCOfEckzj9RLkEzLIGPkMtg7EnEZC4cO9PAYlLyjKtPFJg3muYn-iLWtoMQzhCpDmwvYNaPmbyf3mHkoqUdAeMupVsxlUqCAzIhfGMBLC-uxSGFdJqKWKxMBXu8_zLZgYl44n823Dn7w7xVKeF42yjgJuAa58wygugfFcAejr9L1ZmOxAYepQFkUSm51XfDZNOcooFvWDekQEROeUlzPVBIyaerQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=sIN6j8O3NPaAV7cIOyq6tM2Y8WC8RRAAPETWUg1xZpAvoCDzZRaMQd9Iqjye2sa0fvcOuLLbqITbleeJMyz2BIRfib2zphzDceadqrGOSlNmpQmNrMWVhzDgbB-65Vd_heRs2GUejYKpujU7Ggvqd9-jN95gYVYygtuVymw156j9mdgwc9C-vmFTpq0RBGZGtxvL0jqqQgXsnR8ylypPFfMXHON-lu6k6eBsuyjAGfonsJ-udregcuwKcsVFwihzimXTsGSGLG33EuoB5wwgMTWq7IBpWoURdUPDBWg1_sSTsu9wGjxsCuf1g_JSLQ8h5lTGFw-1RR9LTsZX99Unyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=sIN6j8O3NPaAV7cIOyq6tM2Y8WC8RRAAPETWUg1xZpAvoCDzZRaMQd9Iqjye2sa0fvcOuLLbqITbleeJMyz2BIRfib2zphzDceadqrGOSlNmpQmNrMWVhzDgbB-65Vd_heRs2GUejYKpujU7Ggvqd9-jN95gYVYygtuVymw156j9mdgwc9C-vmFTpq0RBGZGtxvL0jqqQgXsnR8ylypPFfMXHON-lu6k6eBsuyjAGfonsJ-udregcuwKcsVFwihzimXTsGSGLG33EuoB5wwgMTWq7IBpWoURdUPDBWg1_sSTsu9wGjxsCuf1g_JSLQ8h5lTGFw-1RR9LTsZX99Unyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=sqiL6ZP5btqXCfwv9pPOojrP6DNFEikqT0nlxfiu-BSg98hzoE1Sq9Qf4pxGNoyEozL1-RfShdPxJpPx0i4pO_evlUsbNRAHkrEeDsk8kYLLK5AkNmqmd5wNLTYBDh2jGOUho6SbyGXir6bktBVVSyJe_k7ktEMmf3QaTW2B6gYYxnf4r5d23BbU-BHHgXTE_HP__dIX4fmXZ2ls-VDOyGkMDPFADoqZ2xGM675hIiAk4Rug7X5JyMO0g6HhO4inNytcPx8tn_n2ApL9VMWslhXsDfODscOn5cIi8ZXwxW9OLvqrYCibmGrGujAgyDZxpPMBXMa7IspmWbZIuG8_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=sqiL6ZP5btqXCfwv9pPOojrP6DNFEikqT0nlxfiu-BSg98hzoE1Sq9Qf4pxGNoyEozL1-RfShdPxJpPx0i4pO_evlUsbNRAHkrEeDsk8kYLLK5AkNmqmd5wNLTYBDh2jGOUho6SbyGXir6bktBVVSyJe_k7ktEMmf3QaTW2B6gYYxnf4r5d23BbU-BHHgXTE_HP__dIX4fmXZ2ls-VDOyGkMDPFADoqZ2xGM675hIiAk4Rug7X5JyMO0g6HhO4inNytcPx8tn_n2ApL9VMWslhXsDfODscOn5cIi8ZXwxW9OLvqrYCibmGrGujAgyDZxpPMBXMa7IspmWbZIuG8_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=KQj-YkWo53hxFAcYy8GrOi74mLqgaVU2OWimz8mc-XL5mrWYcmS_OQ2CZn9SPSnIWOFoHmtWxnCZJQgTvVLrmQEYrnb8_9pzkFYRksvGifLCMRfPoQ0cPIzV_zRI_3J-SHhGaoYjFqtFVS_a0LLmP7GSW7nbRu6rKusXcbyE3cE-UGzN8EcR-SrGGolgfi3Xx_xaXlvgq7P4RUuBoqtBq4FFMsU95i9eiWLPPXKSi93-__r_H1cGj8cCP9j284l3wLW4N2QY55PVrfuPL63mSGDlMAgWP3uOosT8mlmt-E0M_cDjkDN8HYIQYvNoXUhAfQPGq2lbO8OlwDZgmF89uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=KQj-YkWo53hxFAcYy8GrOi74mLqgaVU2OWimz8mc-XL5mrWYcmS_OQ2CZn9SPSnIWOFoHmtWxnCZJQgTvVLrmQEYrnb8_9pzkFYRksvGifLCMRfPoQ0cPIzV_zRI_3J-SHhGaoYjFqtFVS_a0LLmP7GSW7nbRu6rKusXcbyE3cE-UGzN8EcR-SrGGolgfi3Xx_xaXlvgq7P4RUuBoqtBq4FFMsU95i9eiWLPPXKSi93-__r_H1cGj8cCP9j284l3wLW4N2QY55PVrfuPL63mSGDlMAgWP3uOosT8mlmt-E0M_cDjkDN8HYIQYvNoXUhAfQPGq2lbO8OlwDZgmF89uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=kLFcqwNHWHZEvX9wuFFu3bsoZExqKGmwghGpfzAg1C554dXDGg3Tk-324XTFocZ6hunlPGsvyVIT1LyRTafImHNvx0FxzaaauQ92l06HEC0s40mnk3buzf5xTZF7iGYfVYOfxuDm1ddj6jOANBfWC1Fiw3AiXJLzVhHkSFmXMfw_E69VRyiBvDIONeZMA_vWwpSJmvsfdeFvFz90ZNlhngWCQw3riCiewsNBQk67OaYhXV0iit6KG69DkwEf0I2G2xa2wRtsEKBTpq4ID0F0ruK_2YYwSt1ttA0pLk9IFFAUlGpFHzI9Ub3P7JQgREW2nlHqyPECvvMLggEeLV1FFHMTBED69zOZdDul_xHs4RsZ9zKIYAgsJhY1rYjzZ1EjDt9qgytuFXVZP4bmedlzto3mt7bHOmSxsdvEjgEUW1kCjxVe6TM0T9zsAgmR9b1Hd7QVs4cALLRMbyJXETm2y4J7rxnIhfXyvh9eGw03eoq7R-taVrqgpHlsLdD-b2PSkqi2RPU4C7vyTs5n8M-ixt_b6k-2Mlhn9Rm1uvVQXF4kQMUny3GLXbGsJfF3E_j1PGoCunXfA8g190XJDVAct6fUJ91s3JjRDxs1hwEeE_6KXa2W_ul8QybPbIxesp3G_9ETEeWCfWAj75mZn0KQ65mZF71OXZNIFYfubL9WfdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=kLFcqwNHWHZEvX9wuFFu3bsoZExqKGmwghGpfzAg1C554dXDGg3Tk-324XTFocZ6hunlPGsvyVIT1LyRTafImHNvx0FxzaaauQ92l06HEC0s40mnk3buzf5xTZF7iGYfVYOfxuDm1ddj6jOANBfWC1Fiw3AiXJLzVhHkSFmXMfw_E69VRyiBvDIONeZMA_vWwpSJmvsfdeFvFz90ZNlhngWCQw3riCiewsNBQk67OaYhXV0iit6KG69DkwEf0I2G2xa2wRtsEKBTpq4ID0F0ruK_2YYwSt1ttA0pLk9IFFAUlGpFHzI9Ub3P7JQgREW2nlHqyPECvvMLggEeLV1FFHMTBED69zOZdDul_xHs4RsZ9zKIYAgsJhY1rYjzZ1EjDt9qgytuFXVZP4bmedlzto3mt7bHOmSxsdvEjgEUW1kCjxVe6TM0T9zsAgmR9b1Hd7QVs4cALLRMbyJXETm2y4J7rxnIhfXyvh9eGw03eoq7R-taVrqgpHlsLdD-b2PSkqi2RPU4C7vyTs5n8M-ixt_b6k-2Mlhn9Rm1uvVQXF4kQMUny3GLXbGsJfF3E_j1PGoCunXfA8g190XJDVAct6fUJ91s3JjRDxs1hwEeE_6KXa2W_ul8QybPbIxesp3G_9ETEeWCfWAj75mZn0KQ65mZF71OXZNIFYfubL9WfdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=g2gj86FH64ni6o_SjDWrG4kN7e4ghD9cSM6njvQM0B-3IwW8ekT3oqbUI05irIg7G1oC4S7LPO7a2BcRvz8lWbWz4H-6lv5QT2PqW3SxwRaQKObD7D58lvZq9aMFy6uOgc4D0mBp_Pa4PIw3zzyja-x0RFzD3X4VZpgw7aKZTlUM8qTGUDl2CgDWoPNG3q1Phx1WdvbU1-Pxh7DyTA0RKm6d77EEqJC5ss0DzdAy1xDHLcEcamkWm3HiYbSfnKQBNjwLUviExsP8khPisXBs3jwhaWawoGbmKf1eaxhp-RmBFfR5yH4eNO0uyOVUYGv4NasZCYepG56uzlMGlZHFGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=g2gj86FH64ni6o_SjDWrG4kN7e4ghD9cSM6njvQM0B-3IwW8ekT3oqbUI05irIg7G1oC4S7LPO7a2BcRvz8lWbWz4H-6lv5QT2PqW3SxwRaQKObD7D58lvZq9aMFy6uOgc4D0mBp_Pa4PIw3zzyja-x0RFzD3X4VZpgw7aKZTlUM8qTGUDl2CgDWoPNG3q1Phx1WdvbU1-Pxh7DyTA0RKm6d77EEqJC5ss0DzdAy1xDHLcEcamkWm3HiYbSfnKQBNjwLUviExsP8khPisXBs3jwhaWawoGbmKf1eaxhp-RmBFfR5yH4eNO0uyOVUYGv4NasZCYepG56uzlMGlZHFGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=c02auFHO9y_-GJMp9Im6robl7zkr-GADphRH_gnAwnRtx80Lc39QxmBNJaugH4P0rqLz2-BGiLR-JQ_fbwc_WmAeud-W0QQm9jRrvDD0UG1vf6q34lsbTx5BmtQj_-8HVNsaDiWFcNqg_s2Gd-Ys6Xha8y3UCsbMn76grSxxVJgxGLQ3iI4XY5SQ50wIWImanGzxxNPNT8uLgBMCkbfdhMqJswDX1NzHFw_SG2R_MhNCQhK1ILPFBnT5mDyU27tjHNaNqFDRMvq4SlMoeK3G7D115MsZwar4sl-fwobv0tdHRLPwdysjWMiLUHkyyLJ9rNix1By0n_lnhLATokEmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=c02auFHO9y_-GJMp9Im6robl7zkr-GADphRH_gnAwnRtx80Lc39QxmBNJaugH4P0rqLz2-BGiLR-JQ_fbwc_WmAeud-W0QQm9jRrvDD0UG1vf6q34lsbTx5BmtQj_-8HVNsaDiWFcNqg_s2Gd-Ys6Xha8y3UCsbMn76grSxxVJgxGLQ3iI4XY5SQ50wIWImanGzxxNPNT8uLgBMCkbfdhMqJswDX1NzHFw_SG2R_MhNCQhK1ILPFBnT5mDyU27tjHNaNqFDRMvq4SlMoeK3G7D115MsZwar4sl-fwobv0tdHRLPwdysjWMiLUHkyyLJ9rNix1By0n_lnhLATokEmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWbL_MhGFgo6AJ0UOQ1BbXJfXKyOnkL9mBoy2a7Rn_-puSucaIWF8GjvI3iGtExCkP9ZH020_0qV4B6bjxCk4aBTrCrQmG8COmxwd3Nc6Cg5h5_yZ8ztn-InayjdUQYRS3zZ8EPeA4AFCNeHs8mlY6SHz7SnkKPUX5lsa7kSZCFI7E54WqXVKvnv1UdEYglIb5-4T7oLAI0hQ_Yj7OjO7uqyN0w4pkRXi0CUeB8MbFpNsN_NX0zIuvOetNoDBW5WKga03xHgjz2ttver9-Di1pJ4NM7_KC0vAcV0-_4vpIMLejX-SRNwOeL5tesODvmT8PwQjiArbn3F0yAtZQIutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxCduRM0S5LzfPVZoJ2pQHCefrnoZQEXuLk-1xjhjQmDgd7NcxphT2kcvpNR3nXTmNtBq_RcizIuqIsBc0WW0UeOo3Zovlr-hfrFtQmiX_1kn0HmGNTQR6GadLsep9JIASuHQkkhL0y1QnuyIpW824-ML-yU31hqLr37cpyNQG2Gy2KyYWqi4uR_hveFDhBwAxm5LBHQgZK77r6YwJxroLlmUGevocpGvaj-C49Naawjcy9Twnw7LZC4bPWQ_Tbb0msUegHccgLhoJ7GGlYCsVC2XhUElGjUhimpG5Yk8DbySQZeOD6GWkjF8VB4bzFBp-Ksj57EkFbPLGiDc5_gGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=VC6aAFiDjamUS1sjpxL-Cglo1Z2qcz9KK2Zb7DlO5ISs-_Lr_3S_PO5avGmERf1e846Xwapb7AIkOW4i8s_LQH7xwNWjtp7AOixoX5Y0gHS8Smk9thfo-L4LtCq-6G9qn25WYcXh_XMlobHReb2RywUu_BTiX0SzpQdjQRyDfuOF_A1SrmaPqKWgXZ8nFyVwpLDuYKY6b7uNDS9en5bpYukjHUVJn2c6dwrQxk0w-XLcIutM3lab80MUq1pU7Xc76-BZ-k-b4BDYPmajzGTubnNWXJFQj-zQ-1Sdcguwr1pJ6u5fM6GbaUv1I2OKvAt8wtyw2A7WWpPXTp_2cMYH7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=VC6aAFiDjamUS1sjpxL-Cglo1Z2qcz9KK2Zb7DlO5ISs-_Lr_3S_PO5avGmERf1e846Xwapb7AIkOW4i8s_LQH7xwNWjtp7AOixoX5Y0gHS8Smk9thfo-L4LtCq-6G9qn25WYcXh_XMlobHReb2RywUu_BTiX0SzpQdjQRyDfuOF_A1SrmaPqKWgXZ8nFyVwpLDuYKY6b7uNDS9en5bpYukjHUVJn2c6dwrQxk0w-XLcIutM3lab80MUq1pU7Xc76-BZ-k-b4BDYPmajzGTubnNWXJFQj-zQ-1Sdcguwr1pJ6u5fM6GbaUv1I2OKvAt8wtyw2A7WWpPXTp_2cMYH7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=do6cabBZ6QWjlP0u_AV2_DAmx-c0syiozeDokUD2Il8IZiGfS2EceRjfT2eH9tRCiocFKeoj3VYgSbpFnlwAr-6KDGWgXnpXAevHM3f3wKeK80DuXUun254AphWb1lOTkcwKhh-n6-9X3ykAlLOwxSCHO82MsS39VOMbeI6j9YfkYRRGlda4-KNHMWwK-ywz7qjs1aSp1vsFnx7ign8X2CNNiz3H7vMoKX00yIhOZziqekA0fD-FuXUxbn7ZxsFL64MDQaPelXrYMZ1uayA2quU7GJ1LI0oAcOj-Ob2KdMxc9DZeGVwQ5bGT7HUYe-i2yJbU4rzPhG6phC5_iS7yfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=do6cabBZ6QWjlP0u_AV2_DAmx-c0syiozeDokUD2Il8IZiGfS2EceRjfT2eH9tRCiocFKeoj3VYgSbpFnlwAr-6KDGWgXnpXAevHM3f3wKeK80DuXUun254AphWb1lOTkcwKhh-n6-9X3ykAlLOwxSCHO82MsS39VOMbeI6j9YfkYRRGlda4-KNHMWwK-ywz7qjs1aSp1vsFnx7ign8X2CNNiz3H7vMoKX00yIhOZziqekA0fD-FuXUxbn7ZxsFL64MDQaPelXrYMZ1uayA2quU7GJ1LI0oAcOj-Ob2KdMxc9DZeGVwQ5bGT7HUYe-i2yJbU4rzPhG6phC5_iS7yfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=O3VPxi9ELt19ehpiGS-_XRW3DX19zttfaTOhWJVsRy3zErBrBXeCA0atQHNUgLyAKyBDGsHl4uIdP2-gX1OOQJ3TCkleqmZzk9DsoAOQDNP8m8CWOEbrVKS0Zu5Rt2t8xXuda1lBPZbcAcEFJiHgPc-oWVbFd7v1nDnwcWLOidqDj5qaAv7z13Nb7MlTfYAs2WHb5IBwjM6QAjuYPaDOEv2yd3_JXuXapRCxTDJrwJ3aRDoWyLZWV4MUZTooSlNunbLh9bqTb__gfn0y_oybvQaJ0MA70NzuHZ_uDTS8Lw2B-aJ5597Wzkeo26Ch544dwXjoaeov3hbeaU8IwDIjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=O3VPxi9ELt19ehpiGS-_XRW3DX19zttfaTOhWJVsRy3zErBrBXeCA0atQHNUgLyAKyBDGsHl4uIdP2-gX1OOQJ3TCkleqmZzk9DsoAOQDNP8m8CWOEbrVKS0Zu5Rt2t8xXuda1lBPZbcAcEFJiHgPc-oWVbFd7v1nDnwcWLOidqDj5qaAv7z13Nb7MlTfYAs2WHb5IBwjM6QAjuYPaDOEv2yd3_JXuXapRCxTDJrwJ3aRDoWyLZWV4MUZTooSlNunbLh9bqTb__gfn0y_oybvQaJ0MA70NzuHZ_uDTS8Lw2B-aJ5597Wzkeo26Ch544dwXjoaeov3hbeaU8IwDIjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTvEEZjq81e5ws4TVaTnUjctb5_2uc9y173d5vz6vb3CqynhGoVaAcYDssfumCdITvlBqaL86OlgI1jlCZZ7TI0So6G-dXSa3yaPEaqBr1t2kM87h_aV6zkwiJAN-as7fdMOmYb1LAbSY-mX7_LkskOpdVJ_AbopDmggnw1bfpZubhHihlbii4w-IJjjNJcS3NQ_05WXH0W9mcyKTq-v6OUk5lZe7TT3w8dg7r8cizoEzyk1vibxv3Cda7MZY7Omq07x5Qnj82TZSavBYjrZ87h85MTqEM8ITQuL0lANcntAOtSeujLfvsUp8opqzmJ04Ga7B4LCmIETcQfYjCmksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=H8_Yy5351laia2BaJfaBLzVM4gIUAzVIBVIyiOJ66L_n8VGbHHxWK-SdozhdKCBMunrDgGSDOKh2BrdSVow6FrUNIyWDiqpeLkqvqEa4YFuNis0S4V39DGbjC_Gd0kJlLb9VQqaGIljqlyShrXxW74yOOctLbsV7zpDRMNTilRJD6WImMppFT5dc8PlRC8hwrOgSQJJ-dV5mGFFWJN56UD2HSuGIPmeYSeh1A9ppVa4okt7VKewcuKVQk7ilb6GrOpIYbcpLTXkpD-6XFJgCBg48affe-qkKjdb0m4tj7Eo8jOz1VvTSUpjNq1tbWQztirEMaQPS2oAKrWcSucnXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=H8_Yy5351laia2BaJfaBLzVM4gIUAzVIBVIyiOJ66L_n8VGbHHxWK-SdozhdKCBMunrDgGSDOKh2BrdSVow6FrUNIyWDiqpeLkqvqEa4YFuNis0S4V39DGbjC_Gd0kJlLb9VQqaGIljqlyShrXxW74yOOctLbsV7zpDRMNTilRJD6WImMppFT5dc8PlRC8hwrOgSQJJ-dV5mGFFWJN56UD2HSuGIPmeYSeh1A9ppVa4okt7VKewcuKVQk7ilb6GrOpIYbcpLTXkpD-6XFJgCBg48affe-qkKjdb0m4tj7Eo8jOz1VvTSUpjNq1tbWQztirEMaQPS2oAKrWcSucnXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=Y5Tkpzb250BB56NMIW0Bxnu-MoEbAamw07VW1gPVW8y3NPntZF2HxUw0qe-qK1MPBtuzIc_Z8qWS13okyBOoy8g_QPS6T-ql-_YQPFzVBDmWGMk4kdsjCub3vbSbq7pkUqbP2KwlHTt376l8srdlNAWNYA0Cq_Nnmtkxk5p8ktPzehbXI8WseXcSrFet2yLmI5wnrZsmVgTueSflZLradwmDzPcxYicFRlFzvm7PDEGFQjWftVz1JqJ9f5MIBnR66uzwSGkvvTNy9Rf4NJi5BvzoodV4_DVOAkyrHMjYrfs8vC9Hk0E5UPUgFFCffqFfQBKwLDbKIgm5woQiUXT_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=Y5Tkpzb250BB56NMIW0Bxnu-MoEbAamw07VW1gPVW8y3NPntZF2HxUw0qe-qK1MPBtuzIc_Z8qWS13okyBOoy8g_QPS6T-ql-_YQPFzVBDmWGMk4kdsjCub3vbSbq7pkUqbP2KwlHTt376l8srdlNAWNYA0Cq_Nnmtkxk5p8ktPzehbXI8WseXcSrFet2yLmI5wnrZsmVgTueSflZLradwmDzPcxYicFRlFzvm7PDEGFQjWftVz1JqJ9f5MIBnR66uzwSGkvvTNy9Rf4NJi5BvzoodV4_DVOAkyrHMjYrfs8vC9Hk0E5UPUgFFCffqFfQBKwLDbKIgm5woQiUXT_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=u_bb4usuSOaTjx2t9pX3X6qmcDYDo093djqbGre13JrrBNQvA42u5fnw94zC76tpSpzjG4KFReGVSPyHaf0DzLUp2RhfXLHuWJRjruF31FkGcgUmvGJWlu7Kgfb-S6DCfQgkWDoRZ4iEXDptyl94kjgysY5gZmB9kEr8xKsi1z4wVOhMXue_zuR24XH2HYeFKy7dXck_wbRrZQ3gihw98xAD03n1UhJpFzdmVhNcQ5qp3KxBhmUQhGYGLuK7KmYJLvPp2IPMvJOpuh-DtpLgDnw6knfgNE0a1Dx8wqSc9JtJUZq6HImgr8opJk0ayDYmGKOFm8rtUpVj-0Aj3Ke7kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=u_bb4usuSOaTjx2t9pX3X6qmcDYDo093djqbGre13JrrBNQvA42u5fnw94zC76tpSpzjG4KFReGVSPyHaf0DzLUp2RhfXLHuWJRjruF31FkGcgUmvGJWlu7Kgfb-S6DCfQgkWDoRZ4iEXDptyl94kjgysY5gZmB9kEr8xKsi1z4wVOhMXue_zuR24XH2HYeFKy7dXck_wbRrZQ3gihw98xAD03n1UhJpFzdmVhNcQ5qp3KxBhmUQhGYGLuK7KmYJLvPp2IPMvJOpuh-DtpLgDnw6knfgNE0a1Dx8wqSc9JtJUZq6HImgr8opJk0ayDYmGKOFm8rtUpVj-0Aj3Ke7kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=TQQOay7ikv1GZj3OvEl6aoCtpeWWOeltcmDS7ZsreC3xMmtU9Uxgpu6m5nREHFrCAJt16y4us4iUzUHdZzTVRug_ZvlQkaLc3xpEI40X6RQkmFRsXakYY6VSabI_r9NdmdMDjxSLqqgoGmVxo5u1GR2RDbhautC73UAeNzTpmubVkf-OWDcPVVtNkVSQjVCPdhwJ9IchsH7_Cy1_uIqCqjT-Xd-TXs7GbH9mMwK3bAHNcCC3cuqVDY05rmgCMZVJpJ7geJDtuIr4-SpsX5SqnBmQvpa9OKFleF843rB7-vpDy1mKbtVKYKNpVgzbHnnGRM74Leb_d5s-ydL56MEL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=TQQOay7ikv1GZj3OvEl6aoCtpeWWOeltcmDS7ZsreC3xMmtU9Uxgpu6m5nREHFrCAJt16y4us4iUzUHdZzTVRug_ZvlQkaLc3xpEI40X6RQkmFRsXakYY6VSabI_r9NdmdMDjxSLqqgoGmVxo5u1GR2RDbhautC73UAeNzTpmubVkf-OWDcPVVtNkVSQjVCPdhwJ9IchsH7_Cy1_uIqCqjT-Xd-TXs7GbH9mMwK3bAHNcCC3cuqVDY05rmgCMZVJpJ7geJDtuIr4-SpsX5SqnBmQvpa9OKFleF843rB7-vpDy1mKbtVKYKNpVgzbHnnGRM74Leb_d5s-ydL56MEL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=TGeM6WTSfOgBxtkUMzUUrFdqFyxgvDkjonpa211WKsIQqpiPAHY3l2HvQrd5lX_dwVjWPGjT-tTTELqtiIDYvC1xP0CzlqYa0TCMKD9TCjURBsquAwqQ3aijcXQcGU46VoyF0hTnaym3glQJYuS4sB6lL6KezJeq9hISeDccQzCA4lxQGDFJ5BsBLGybLug1IlZHkL_FTq2FJqXCHB_vekyR2re6hk5_YUsXfrHWUDnfyNM2oaxNmUo6Gj8F1d7Cf4qYtiWbHuZPy00mEo_gLM_LrPDL6gC17DY_mYfrCoW7n8KBA7BpSh3KeJhhAADF87BN6VAOpoeHh6KxLLWTqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=TGeM6WTSfOgBxtkUMzUUrFdqFyxgvDkjonpa211WKsIQqpiPAHY3l2HvQrd5lX_dwVjWPGjT-tTTELqtiIDYvC1xP0CzlqYa0TCMKD9TCjURBsquAwqQ3aijcXQcGU46VoyF0hTnaym3glQJYuS4sB6lL6KezJeq9hISeDccQzCA4lxQGDFJ5BsBLGybLug1IlZHkL_FTq2FJqXCHB_vekyR2re6hk5_YUsXfrHWUDnfyNM2oaxNmUo6Gj8F1d7Cf4qYtiWbHuZPy00mEo_gLM_LrPDL6gC17DY_mYfrCoW7n8KBA7BpSh3KeJhhAADF87BN6VAOpoeHh6KxLLWTqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=CRtqnQe6AU7a6XI0W7BEkCwOIHe82x2wNDVNuROZ9rOROwU7mkQbpHZqKgWIo0WtVbnba5KJ5GafrSFmQywrpvkic98xToDlDO0Ri0ilIrjEEt-Moi50nc50JZDywSh99imgGSLq31cMKYU2h17l1gbHYp1t-Wgou09B0TMmlOeEeayHDT70cUUkkzhiyoxiBc0yQclNz5OPctMIZ6caVkX0guofgQOUrt-W1JsBCxXxqLfmf_4aLniccoFY0hegMgxu7j7kFitHS6HvFsYujjd7sDZEdQhvr6ECSMcY8zC4wA6fyMWI5gVTYxlT84a_l9dYI3sa8fZZ88iWrF0dzmmqKjBFd8KbtXgYQm8CDq7OBDwGC228jOmyT_o5OqKD_rd6DvAWHCn9K5g8WbrOKGHF5jNNf7fR4W4vW3YZyAiz_HAsTwkzYvRvditw9XNMptEyeKWVOHmUhUzCtfrN2s7TsQo84V3NzCB6ZRZqR3WE0cCP3uPOqTsxGT0H7PKo5w66GutCNp1sUGUfHXRkru-uNgOd4syASpHU-767_n0OO3SdWMeC8ltxpUydNQEew84aen1XXug8lVWwEmDNWGfUzQc4-TsC1xmBMRxLHGZ4Fuxyu-DKr7I7jFNKXlDi54z0Soxy8Rla43UDZypma-p-ut7WZ5sPdeWiu-_l6ko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=CRtqnQe6AU7a6XI0W7BEkCwOIHe82x2wNDVNuROZ9rOROwU7mkQbpHZqKgWIo0WtVbnba5KJ5GafrSFmQywrpvkic98xToDlDO0Ri0ilIrjEEt-Moi50nc50JZDywSh99imgGSLq31cMKYU2h17l1gbHYp1t-Wgou09B0TMmlOeEeayHDT70cUUkkzhiyoxiBc0yQclNz5OPctMIZ6caVkX0guofgQOUrt-W1JsBCxXxqLfmf_4aLniccoFY0hegMgxu7j7kFitHS6HvFsYujjd7sDZEdQhvr6ECSMcY8zC4wA6fyMWI5gVTYxlT84a_l9dYI3sa8fZZ88iWrF0dzmmqKjBFd8KbtXgYQm8CDq7OBDwGC228jOmyT_o5OqKD_rd6DvAWHCn9K5g8WbrOKGHF5jNNf7fR4W4vW3YZyAiz_HAsTwkzYvRvditw9XNMptEyeKWVOHmUhUzCtfrN2s7TsQo84V3NzCB6ZRZqR3WE0cCP3uPOqTsxGT0H7PKo5w66GutCNp1sUGUfHXRkru-uNgOd4syASpHU-767_n0OO3SdWMeC8ltxpUydNQEew84aen1XXug8lVWwEmDNWGfUzQc4-TsC1xmBMRxLHGZ4Fuxyu-DKr7I7jFNKXlDi54z0Soxy8Rla43UDZypma-p-ut7WZ5sPdeWiu-_l6ko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsGFAoX6-mXpfySBwRKE_oXc2rLN-I6HIo6RViXj7pGIP7VCceaFEe01WQuvWwNfWGc0dyKYfMEpsWW8EnN862mAJO7gzwrKTdcJtG0jVKs-iHlG-WRa1oN9brQxf1ouBK6_DxH7sBNpo4t4CV8kAyF7nccbRs1Q6OROgu6av9cWNuooiCPC-olrZ_KnyRu1O5cl5M4T9KUfUkuJ2dm9rvAY1d4OF4zJy-LbEga3Q2axho0_D2__F7Gd_t3agvWYcSzc_TovjhdZi3A-kLQqGWssvKyo_jWp6mvjoT1OwPaWOuLfLwp5wAdiAdFC3YnMi_ASkL_hNEu8UU4bpvhzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jACqnB7NnuUeeoYKO6RWf2e8cH2RPHjAy9fOFr043fv9T3k2BunryIMVcxf0ZGlIVZiuCYa02oURr-6TrlaTqQQv0IazSaz4eqLgfj1aamPU3Ywl0OI391SzITgHkDDzr2ys9mV9IPcmJ1L9SC4WQGfcgvUGKeGsZLNjl5hwmFNqMUczP5L8SUcsQWO6RM6gdi4Lr1IVOBtr3f3wJl1XczF3BZdijTTiRgSTMLh3GmZf_yzYGUaBJPYGNxF0QLy1h6eI0CidDk_5ACrCvypQBaYJ2wxR370hVKuvgR6M8wIz4KFZXN8SAriHL6B1evx6CfIt65i0-9BtyXAm23KAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8a9epvhoDOl70O5S8aEvCvZQLjdag0k7iZJtpySKdiNjW2GFNjFjy6sy1e9fGaKQKwMPGihJxMp7tgTkQycPV9nVGuppidSilqDJPWTJIaL_bOoW8pubOmoGXu2L-kC6dDEprPUPyAMlwIcqAqI2C5iyXeKf_UyluuTQHgrhi-FFd1dw7N38qPEPSw2vd3qQdIbEh65CwsYIND99k9zkMOHuRZQdUkDFjjVtj_9R1o1RyTvBaiIEZ6jj1OZhSWrpRi_lTBmqXRJG1wh0IJOgMZvvZ4XvOL4X-MPmpA12NcOf-hKcPoDpQ9ryaDWG-HmAjT5plfSJhGkBNi6f9C03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=V8hXFmZlH3LzPg61RzBLj8N0z4vtSITI5H44mKrWeOd8hP1EkPFI1wSGoxL2nlamYDUH5PnjdWaro3jUvfKJXelgtxIwN7WjJn3mCyQS1uArN3l4y__HFQXz73fU_56dJRsvvt1JdzU_j1w9rNMJcflftLvlUpjGco61JTlWUQspT33XMARwqTrmFd2KKdp3DxVGm0Q9k-EW83mAxmg_xLoOdLcwDEcc55dhkGBcHfjKegFb78EO3dJB9K3pN_1WLcI6ZRuTryT2iGxbPNVd4W87HTWeZKn5n2ZgfpPqw6aY6X8_cxK1KNqdNWCVO9iq7jwKFCcDLLCXk9WhclxqOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=V8hXFmZlH3LzPg61RzBLj8N0z4vtSITI5H44mKrWeOd8hP1EkPFI1wSGoxL2nlamYDUH5PnjdWaro3jUvfKJXelgtxIwN7WjJn3mCyQS1uArN3l4y__HFQXz73fU_56dJRsvvt1JdzU_j1w9rNMJcflftLvlUpjGco61JTlWUQspT33XMARwqTrmFd2KKdp3DxVGm0Q9k-EW83mAxmg_xLoOdLcwDEcc55dhkGBcHfjKegFb78EO3dJB9K3pN_1WLcI6ZRuTryT2iGxbPNVd4W87HTWeZKn5n2ZgfpPqw6aY6X8_cxK1KNqdNWCVO9iq7jwKFCcDLLCXk9WhclxqOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=AKETaaUW1LqTTUu_Wt-AZ3hZlvke6Wv0NKgfu7hbptq_mwhUnGmrrKp5o3WxuTYn0M6jXzZwubVXOZnSRCsrOKMBVDWXVRIlXFxhiHBw4wjsw0DuhtVJi5NGJF90gU8-utficgHA4-pXHCG-QOxlAnMNYucuhLWU82thXnTwaZMgBAmMN2nN8TlB9KJL6CbpwbX_kdXUQAMjCpJeNTnrPyCiu0AdAcL46vlJBpYFwVWRlPoaEmtUXvIA1S9jXkRe9YoFckFL1bnsXDObvbFrGodyP9snqDf3cadiRah-fA3CVVyhnvm0O4tEcY5ukIU5nUwd7axxmvaSu71VDG-jeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=AKETaaUW1LqTTUu_Wt-AZ3hZlvke6Wv0NKgfu7hbptq_mwhUnGmrrKp5o3WxuTYn0M6jXzZwubVXOZnSRCsrOKMBVDWXVRIlXFxhiHBw4wjsw0DuhtVJi5NGJF90gU8-utficgHA4-pXHCG-QOxlAnMNYucuhLWU82thXnTwaZMgBAmMN2nN8TlB9KJL6CbpwbX_kdXUQAMjCpJeNTnrPyCiu0AdAcL46vlJBpYFwVWRlPoaEmtUXvIA1S9jXkRe9YoFckFL1bnsXDObvbFrGodyP9snqDf3cadiRah-fA3CVVyhnvm0O4tEcY5ukIU5nUwd7axxmvaSu71VDG-jeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=M9JNmYPaLHbLscLyY3PEGWbnEZIyiq0u09cjC29KVIVH9-mQ2l9wfiGI0r5vw3fYy93Q3WpLq_5sedzCtZVzXec19Ff2y-tmcySnPayDKofLwkCJekH29M24WEtBuw7wSICdPM66JcP-ZE7WVWJEPt1k1WhhPpFE_ZRcVQcfKPKkBku9cBJjr2D8y-ZggX2EMqjuxqBKW-dh4Nx8QBb_WyG5tuuHjbGyxFum94STSPse61LBhvh9h_taMiYKcdCHvDrGUbame0V40M57kljBFnYpU8xIVy20SltaIiqT3pO1co5ae9rO8eFGT6OhS8jleXnro1W1Vo7A9e-v3DBuNoe117f-GqXrwZ5ue0nC-OcxFl5XdaZhRndZgkY4eBoH7ydriDkCbcgEUJ3c3jQ9gnKlEoVs2CfyQsYOTha2jb3EDRlJD-t-ToHNWBIa2ooax1ZryLTzlgftshbV4mdM9g-CHjZD2k05VEeo9LekfiOLG6gnCGUU0hckGxaeCkqJeiiC1kdJ-_0D_JtmdTbW6AL_UQD4MgV4j7k2BqK3bRCaeygOljCRXItZG0NRqDymrX3yuxP3Rotjmzgmvtv-co-nXvZ1lfiLwngtxw7FRWcjcoEYHDkpr8W_byFNUkwTPwSdovlDrEKb8cIdtaJdZB6MCOKwxn71w5lgovEcvC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=M9JNmYPaLHbLscLyY3PEGWbnEZIyiq0u09cjC29KVIVH9-mQ2l9wfiGI0r5vw3fYy93Q3WpLq_5sedzCtZVzXec19Ff2y-tmcySnPayDKofLwkCJekH29M24WEtBuw7wSICdPM66JcP-ZE7WVWJEPt1k1WhhPpFE_ZRcVQcfKPKkBku9cBJjr2D8y-ZggX2EMqjuxqBKW-dh4Nx8QBb_WyG5tuuHjbGyxFum94STSPse61LBhvh9h_taMiYKcdCHvDrGUbame0V40M57kljBFnYpU8xIVy20SltaIiqT3pO1co5ae9rO8eFGT6OhS8jleXnro1W1Vo7A9e-v3DBuNoe117f-GqXrwZ5ue0nC-OcxFl5XdaZhRndZgkY4eBoH7ydriDkCbcgEUJ3c3jQ9gnKlEoVs2CfyQsYOTha2jb3EDRlJD-t-ToHNWBIa2ooax1ZryLTzlgftshbV4mdM9g-CHjZD2k05VEeo9LekfiOLG6gnCGUU0hckGxaeCkqJeiiC1kdJ-_0D_JtmdTbW6AL_UQD4MgV4j7k2BqK3bRCaeygOljCRXItZG0NRqDymrX3yuxP3Rotjmzgmvtv-co-nXvZ1lfiLwngtxw7FRWcjcoEYHDkpr8W_byFNUkwTPwSdovlDrEKb8cIdtaJdZB6MCOKwxn71w5lgovEcvC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbrX9DoRfjkSKegp6wgtK-kWtqAWQIbIPNSurLRInH29S4jtuE1RWTDtgpKJYIhRbMPbueC4g9xO3ieyp8K21WkYDaKv3n4WaueH4Cfuf5BOa50W7WnOfTCaV7u_-VCmXbSNkXBucTl5nO6v1ZgGl1329fr0Jwa9Ni5Xk_pcDuIUKMQnJ43BRzcb-n_Vd3w7Yp4X9JS4VfcLSmvp8LHIwzB7GyXStqAekcUtTbi07FHrE0a4DScclTpUAsyE7WWX0ira7iIi0c_EQDzcxcW0I8xPrpkNiL5edD1_XoRlrPBSFpMC7GWDwFROMfgHHmO1CrrVuqrduxDsLs1lzlJwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=FswLSEw7vz3RYRIXLf5Z1RvEl7uPV9nlennTYiviVxDAv2rVrm9O8wTXyMRVozaYMOaGLfQ79nN51uVaNMZ2t-F4bUUVBkX6opocF6OelHixJa7AjsxBbGVO2KxjGzYh1WpdgL9PBsbY4bAPm2LBHk06ZtUCd_APldm_ijdlidb6jKVPW5ORAfh8Fj5lINvi08nMtRnh4pygbensyZE4lMugoDH3zq9qqet9q2TtIRA9sDjUnTtpFKXzWqWNIZLduICjiaPb8rWECPiK2ZTpejLE-VTeLMap7lgn0b2vyIUrzA2x6yIYEQT0cihDR_XMbG14tBuHuTrEhdw9aDROMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=FswLSEw7vz3RYRIXLf5Z1RvEl7uPV9nlennTYiviVxDAv2rVrm9O8wTXyMRVozaYMOaGLfQ79nN51uVaNMZ2t-F4bUUVBkX6opocF6OelHixJa7AjsxBbGVO2KxjGzYh1WpdgL9PBsbY4bAPm2LBHk06ZtUCd_APldm_ijdlidb6jKVPW5ORAfh8Fj5lINvi08nMtRnh4pygbensyZE4lMugoDH3zq9qqet9q2TtIRA9sDjUnTtpFKXzWqWNIZLduICjiaPb8rWECPiK2ZTpejLE-VTeLMap7lgn0b2vyIUrzA2x6yIYEQT0cihDR_XMbG14tBuHuTrEhdw9aDROMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=pdx1BYvud6KjeZKQUZ26CyWVgcmcnrHLllg54fCWarj3uRJDmEv4SyNFUvPvyOBiL3t2zK740z87Oe5HWGvyyAElBCmqji3o59T7zsPlkLS0wACe0JPpG9WLYcdj3uiEFvBq8J7MbZalv3u1Dt1oEHeXInm4qfEXpE6z6qQ0S9W3OY98q5M50ri4VYE0urz0JXNu3GPROf7bmM33PByEqgVrn3Aolw-FyigaXi5WiKQ3OzkMo1fD79inOQxu0mR1wAYng3TSCJWWUXBbu5JBxiiwMG1xOe_Q23CHFd9yn561_loCRbwfb5Cu646eriHWTFQ8GIUtXZZbz7NGHSHxcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=pdx1BYvud6KjeZKQUZ26CyWVgcmcnrHLllg54fCWarj3uRJDmEv4SyNFUvPvyOBiL3t2zK740z87Oe5HWGvyyAElBCmqji3o59T7zsPlkLS0wACe0JPpG9WLYcdj3uiEFvBq8J7MbZalv3u1Dt1oEHeXInm4qfEXpE6z6qQ0S9W3OY98q5M50ri4VYE0urz0JXNu3GPROf7bmM33PByEqgVrn3Aolw-FyigaXi5WiKQ3OzkMo1fD79inOQxu0mR1wAYng3TSCJWWUXBbu5JBxiiwMG1xOe_Q23CHFd9yn561_loCRbwfb5Cu646eriHWTFQ8GIUtXZZbz7NGHSHxcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=JL_GmNanfAFAoKIylUFemarQkFnNEPQWu0_Cs55ew7NCDwP1KlCRMnPEvty78q7GELTadgDOXN906LMJFBqvct7bJIXtjBTogHZdkwiJrlBCqk__UbTbyu0HYxX-HpG56lpb3TS40bvQsH-3k2utQuF-x-8DAnrUdoGwmSZuLmXj4mLxzVQpmiG1g-frQy2cNX79_Q5xpRbWuY94p4JAhG4v5PrxQCo-zXcpkFXcNZ49Wy7EIbf4cSSKHbhDtAeoHmi6Sxk8kuQ4d9OOWTpRO3F0w9qSgNi5u0Sjua_YD0a0aGMv_uxJEMqY4zenTyz3PV99RGPHhLn0-e14fkUrgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=JL_GmNanfAFAoKIylUFemarQkFnNEPQWu0_Cs55ew7NCDwP1KlCRMnPEvty78q7GELTadgDOXN906LMJFBqvct7bJIXtjBTogHZdkwiJrlBCqk__UbTbyu0HYxX-HpG56lpb3TS40bvQsH-3k2utQuF-x-8DAnrUdoGwmSZuLmXj4mLxzVQpmiG1g-frQy2cNX79_Q5xpRbWuY94p4JAhG4v5PrxQCo-zXcpkFXcNZ49Wy7EIbf4cSSKHbhDtAeoHmi6Sxk8kuQ4d9OOWTpRO3F0w9qSgNi5u0Sjua_YD0a0aGMv_uxJEMqY4zenTyz3PV99RGPHhLn0-e14fkUrgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlURh5tfsOitSAnsyD92Uy8dcVMY3xVHfnih8WZAj50J6MyT28NKPdK0p9cbR8cU81LYl7UN4MuduAUkJOc662vuycr2Ue5ATxC2pva_RgvCJ5Os_HyK4qAMwdZavcb01x-6_iB-uSR2J9uB4ZVLlSa3vPD7HrWrW7JYnw_rZd9LEtrRB_IWXjnPWoYHkq89plldZSckbLIHudzq6OOejZ7dJCzvlpYcjbcX6tZDFA4WCknOjbu1yiG2ivS8jJQXIrtoAAKJvRz-PMtPp4b3jhJQB08vC2C2hMTuilhVG9WP3vRSstDuayp29b94ZWE-PXK5-CEEWQKb_rgh2KgEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=VYwgY-Ech5wexNo3rm8jXHIONUF8ZHZ2rU74-qQItFHWmkHX4Mi2wYPjTJO3Ko9CYAuJKP0z7_Z-YILgk5XUciHDol8Gf1qfcaX9xts6BOh3ckWRcXYr95vg_rehv6ojdKi_Puq69peHD2QRTv1k85B14zAaZsvh8jd97FNK6WZJbNxsDLYJhez3aJ57z1jRbTbZMhVIfiaFMpMgPUdBMIq5RS0-nLWXKOU3xcnbCsdwUlMsGh5DemI2R6nZ6y-zKphQjdgFWyMOuv0Cqyh8xcKbnokKF_R-yF-i773k1fUhaEkBQnnBdAGQdGishfBR87OJUSRhwrv31XES0VQ_tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=VYwgY-Ech5wexNo3rm8jXHIONUF8ZHZ2rU74-qQItFHWmkHX4Mi2wYPjTJO3Ko9CYAuJKP0z7_Z-YILgk5XUciHDol8Gf1qfcaX9xts6BOh3ckWRcXYr95vg_rehv6ojdKi_Puq69peHD2QRTv1k85B14zAaZsvh8jd97FNK6WZJbNxsDLYJhez3aJ57z1jRbTbZMhVIfiaFMpMgPUdBMIq5RS0-nLWXKOU3xcnbCsdwUlMsGh5DemI2R6nZ6y-zKphQjdgFWyMOuv0Cqyh8xcKbnokKF_R-yF-i773k1fUhaEkBQnnBdAGQdGishfBR87OJUSRhwrv31XES0VQ_tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=cNd5ynby9r27T52C17rwxoDp635xo5H_Os3EV1LC0U3TIAMNTM0LqsnWBsoxbIiql92I3-iYaysyGASnqp_ry9_TvGQ_7Ft_lstBz1B6fQpnqH1P8PdR2kHqy2IYEpMptydz7ohrYZhwpBA7P4rm4NkDqVrFJ4fbSjN27ZS428oyor8l4h_eaYZv8EfqiLZZdC63UdQWp2y7Y_v47XgwuFgX_TVw9ISHhdH-RtA1aRwhSg0oUdMdX160w4BBnqHfFcBTuCGpOiMES6feg4FlU3j8aiV9q4xxMghlr8hVzHn-yJ0IDbEQJcfAOhR31Wx4BveBjv1ZvBVsMyNj3sHaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=cNd5ynby9r27T52C17rwxoDp635xo5H_Os3EV1LC0U3TIAMNTM0LqsnWBsoxbIiql92I3-iYaysyGASnqp_ry9_TvGQ_7Ft_lstBz1B6fQpnqH1P8PdR2kHqy2IYEpMptydz7ohrYZhwpBA7P4rm4NkDqVrFJ4fbSjN27ZS428oyor8l4h_eaYZv8EfqiLZZdC63UdQWp2y7Y_v47XgwuFgX_TVw9ISHhdH-RtA1aRwhSg0oUdMdX160w4BBnqHfFcBTuCGpOiMES6feg4FlU3j8aiV9q4xxMghlr8hVzHn-yJ0IDbEQJcfAOhR31Wx4BveBjv1ZvBVsMyNj3sHaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=bhFy1P2bSoyhVP43rpQpz6EHtLlpqyPW3OA-1ibj8_sWA_Z2zu9QddFpzvESHcAAywQH8Q8N8dw7n2lBlI5iTg1FtoSVOHL9g7jjfbRRhBROZD21xQAHIy6xbPeWnTEgrsSpJoHR7KzgMGWU_5t3w1zh7ZMuO5QJbUNAziOofC-sbmW6KDRSF9pYc9Z83PPOUtLryOFYRehM4mFjTXrAiVGYJLhS0S_XrTCehbx7aGyFmMzmHYso67XMpFtAon6ULIBNZgS6Xo618qoiS9tMEDev4VSJuSJOJBiv6hXKozJQ3J1Z-ICOmSNroV5N6mGkLmKtVrtmMWP9Yuh5S3lsnZKEGGZoOg6exx-QzS-tbLl3KkFExBzsS_qx7vgWnPtykZJoWulFPpXHnFlOJbL0yGg2lcDY_OXiS2fXK4AViwcvfoYhxe3fTW5iG5z3oFw7YSeFmta3Gn0dhZBQHS83XFrjqqezkkkSJmkAP54qu-BimjOVasVZE4_Cuv5wA56qHswR5WeIaIw_lRwgWhxpkkh9K7qquUgNoIJDh36X7kjKC55gatHgFuSpEmURxSYf3xf8B_WsMgt0aMUCUeW2N98fruw0RH5F5OAFooSPARZ51qfR-0sqlQ9mRlUJNzdoAkD0Z1N9vmC26LHp1B7RqC_C4Oc_JVI2wdNAJ8CHQVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=bhFy1P2bSoyhVP43rpQpz6EHtLlpqyPW3OA-1ibj8_sWA_Z2zu9QddFpzvESHcAAywQH8Q8N8dw7n2lBlI5iTg1FtoSVOHL9g7jjfbRRhBROZD21xQAHIy6xbPeWnTEgrsSpJoHR7KzgMGWU_5t3w1zh7ZMuO5QJbUNAziOofC-sbmW6KDRSF9pYc9Z83PPOUtLryOFYRehM4mFjTXrAiVGYJLhS0S_XrTCehbx7aGyFmMzmHYso67XMpFtAon6ULIBNZgS6Xo618qoiS9tMEDev4VSJuSJOJBiv6hXKozJQ3J1Z-ICOmSNroV5N6mGkLmKtVrtmMWP9Yuh5S3lsnZKEGGZoOg6exx-QzS-tbLl3KkFExBzsS_qx7vgWnPtykZJoWulFPpXHnFlOJbL0yGg2lcDY_OXiS2fXK4AViwcvfoYhxe3fTW5iG5z3oFw7YSeFmta3Gn0dhZBQHS83XFrjqqezkkkSJmkAP54qu-BimjOVasVZE4_Cuv5wA56qHswR5WeIaIw_lRwgWhxpkkh9K7qquUgNoIJDh36X7kjKC55gatHgFuSpEmURxSYf3xf8B_WsMgt0aMUCUeW2N98fruw0RH5F5OAFooSPARZ51qfR-0sqlQ9mRlUJNzdoAkD0Z1N9vmC26LHp1B7RqC_C4Oc_JVI2wdNAJ8CHQVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=r-B6zna5UJBWW7-a2g9Y6wQ54XCSyERuULiHScOoLwo5zj6I8T1O7gTIhTy-1T-SIdjngcx-F193VtGjuoJcH_5GJH-XhkkAwH737SSG-1j3UhwGmFnyw0b1gtorAQ5k7Wgu0YAvsc4x3h1KRTFkaVnB0ZGVWo2u1h2t2ymcWy-htkYQncloNfPqCIeJ1Lnq8kgi7ZXfGrLO-aNNnJBaCEQhEWwtsIHg80v9EdskzOijp-96k4_Fjp0TqQ51hBvwwmlrutbxT-HLgdnRkJO7zhjgS4EghvseFLjnLtsSdwR-DL6ykpvEBiD7xAMIzBPhmfZ0I41OEjnTYBhSKsi-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=r-B6zna5UJBWW7-a2g9Y6wQ54XCSyERuULiHScOoLwo5zj6I8T1O7gTIhTy-1T-SIdjngcx-F193VtGjuoJcH_5GJH-XhkkAwH737SSG-1j3UhwGmFnyw0b1gtorAQ5k7Wgu0YAvsc4x3h1KRTFkaVnB0ZGVWo2u1h2t2ymcWy-htkYQncloNfPqCIeJ1Lnq8kgi7ZXfGrLO-aNNnJBaCEQhEWwtsIHg80v9EdskzOijp-96k4_Fjp0TqQ51hBvwwmlrutbxT-HLgdnRkJO7zhjgS4EghvseFLjnLtsSdwR-DL6ykpvEBiD7xAMIzBPhmfZ0I41OEjnTYBhSKsi-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdOstP9iasDekxULfI97fZZiLYYI_aFhRi4Trf_zTU9CaZLM_Fh2fXAL-hzCnX0A6d7A7mIQg8qNMlkKZ-eCK4s0efWW1d9NY2eDT99KhkQXlJnlJkBpRur_gCHmlZP70bcmgY2BZmxq0E4DfDwOsdYLyB_nGLsCTToBp0AMR-AJgxsg5TSaZN5ScN5AYfn0d-ZoQwzqDlTJ3BD53RiWs6vDi6sX7NAuSQ9x8jwUnVAJ0_k73JHgnHY9TUc5DeiVEcWyar23Ssn7iKSUr9KTKm_vfFR5Djex9uI_HjdbqZvYxTeVH22X_gD23AzVvmYpCZuKCR9VvNo58898UEkE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=HYuSOYssiQ4Br9rGRMYqV0uLrMEaTZu4p876_t07DrIWcvN26Yt-RWW_8rIbtIbHEfadrrIadIt_PpnXpJA23DcrNmna52EyyVunNAU03F1QHnEN0WK-wvDiBNWRHhh2NtE0NNSLDIJmvvxuvwCM8ZpOSnN4vEnh-ld7Sg-_s_vLscfmWXjcJFoUdDzq0b-7e8YOzJ3Xr3B0qf-nOwD5D92vMpGQ2JaEsI7ia3pmmW4-QZ3Lu8ZY6qvF8vDzwPhn3IqafDA9DmGkteO1PI1t-a4rBhHbZ2k30UF5vxdbqc6EIpcdutYMY6rbuLD06eZA-HHbFVloy9_Auz-n5dArSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=HYuSOYssiQ4Br9rGRMYqV0uLrMEaTZu4p876_t07DrIWcvN26Yt-RWW_8rIbtIbHEfadrrIadIt_PpnXpJA23DcrNmna52EyyVunNAU03F1QHnEN0WK-wvDiBNWRHhh2NtE0NNSLDIJmvvxuvwCM8ZpOSnN4vEnh-ld7Sg-_s_vLscfmWXjcJFoUdDzq0b-7e8YOzJ3Xr3B0qf-nOwD5D92vMpGQ2JaEsI7ia3pmmW4-QZ3Lu8ZY6qvF8vDzwPhn3IqafDA9DmGkteO1PI1t-a4rBhHbZ2k30UF5vxdbqc6EIpcdutYMY6rbuLD06eZA-HHbFVloy9_Auz-n5dArSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=sD1QMj6LKf0SNH3WEEdYOxjVHbFfskKtDO4bmJfi5Or7_8Jk8IIwZnMOjpFgGtoTwJKG9g2tG3yS8-i8dIo7sQmDhd3rLcNSwfLN_4CzqgDyK-QhsnoiA6PGV0qQUijEdutq02szE9JJ0rwHvqb-xmNR7MpW5GiMYsIWBoD1lQcchbLY-_WZBXDkF6GoJBv2pcM-oo1kZxMs_sUjsBOdUXUIlA0AOuRJ3lrm0RO1WJXCkzzG2bwOpRUpY8Mtz8Xfg3Fuoiw9e21TlOC3JzVyN-BwQ-kb5Fqjss-sIWdcp_xGMLel-n2w-GkLjhwMwzQwnDbmKeOAr8QATXVTwbsRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=sD1QMj6LKf0SNH3WEEdYOxjVHbFfskKtDO4bmJfi5Or7_8Jk8IIwZnMOjpFgGtoTwJKG9g2tG3yS8-i8dIo7sQmDhd3rLcNSwfLN_4CzqgDyK-QhsnoiA6PGV0qQUijEdutq02szE9JJ0rwHvqb-xmNR7MpW5GiMYsIWBoD1lQcchbLY-_WZBXDkF6GoJBv2pcM-oo1kZxMs_sUjsBOdUXUIlA0AOuRJ3lrm0RO1WJXCkzzG2bwOpRUpY8Mtz8Xfg3Fuoiw9e21TlOC3JzVyN-BwQ-kb5Fqjss-sIWdcp_xGMLel-n2w-GkLjhwMwzQwnDbmKeOAr8QATXVTwbsRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=JwJXJcKPx9fGXK37X7nUuObMe6Japy5j0zdDdjZGFscuZnBNuIB0wMb255kQReTzmOfE0ubYOkhkIkbFrqqvN5vjn3q6AHBLRL96FReJ1jg43lT4S8RGpBLzX6YQ9h63Ow0gmrSKp_pcRtVIeETNxBjaqe-PINl5PB2X9VlKFgjD3Np3pPARqaDT3ubWGM-T5jwm310zu_R3rkgUH_7yjUw8CTAPV-wGIHOzWcQQ7roBSCf0JSKYWyjknmCeoV51IrUx0iipvaaiGr58yCFvBiceAWCIKRvdlQ4UzNLR3tFhtFkSNKnyGH9KtL7xeBOwUmdpP2ib_e8mKhAQkFJeLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=JwJXJcKPx9fGXK37X7nUuObMe6Japy5j0zdDdjZGFscuZnBNuIB0wMb255kQReTzmOfE0ubYOkhkIkbFrqqvN5vjn3q6AHBLRL96FReJ1jg43lT4S8RGpBLzX6YQ9h63Ow0gmrSKp_pcRtVIeETNxBjaqe-PINl5PB2X9VlKFgjD3Np3pPARqaDT3ubWGM-T5jwm310zu_R3rkgUH_7yjUw8CTAPV-wGIHOzWcQQ7roBSCf0JSKYWyjknmCeoV51IrUx0iipvaaiGr58yCFvBiceAWCIKRvdlQ4UzNLR3tFhtFkSNKnyGH9KtL7xeBOwUmdpP2ib_e8mKhAQkFJeLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7FJa111A_EAL6NpoSeEHHZn2MksIS9JEze2T_O9RXxrYsaV-IW-jIl94rl3_hn_ZF2AkpZvrxUxZ4IQukBr009yDROXJZq8n2LhuytIhGzONGd5Guojt1icpUaSGYtqCnvzMtg2oe6z1bUouzu8Q9PnXsi8GxzIEoZt780dw0YlrhL-HW9fmCPfQW0JZJXxeq9DinRDFzBIsEbqH_VyhMi91q04xS_2rS9jisWwlgCpnGXzv82EHeM7SALFaI1j7tIVX28r9QS1I-wBU4q5NOPOOMk-8XNdSl1JzfcGSXHwPsCZJzt8red0QXJ-UlK_Olb-NNwCqistP8UeTZPdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=ku_Kxke41y2xAuK-mbEPgifgTevPlbCoc-x9YWUR9S3gtbRpS4v-tyhcMvKsXYphlPsLANHQMwKv-uNquFU2ooDpkry2p5i8xqel8tDmnsIkXT1zdD63x_KEQsgD9AHErB4UC8n6Lh7aGf4kPJ86nAFXZ4V4CdPE1UkgclM_ZkenN4ssa9Awn8Rc-3pzwabI5aeZpYzA0qlA0DkJFCClKpHN-aBrYAzFwC9dsOlTCDPsVE-OppxHphnW5u9xCc2Zdmn5TYCIHx0PaAf03gRxw3pQnB45l5b0F-2ckRfnqgLx9vqLZ8J1OeJOVgDcfsg8pl_ZYZn9-Yubnph9h9T2Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=ku_Kxke41y2xAuK-mbEPgifgTevPlbCoc-x9YWUR9S3gtbRpS4v-tyhcMvKsXYphlPsLANHQMwKv-uNquFU2ooDpkry2p5i8xqel8tDmnsIkXT1zdD63x_KEQsgD9AHErB4UC8n6Lh7aGf4kPJ86nAFXZ4V4CdPE1UkgclM_ZkenN4ssa9Awn8Rc-3pzwabI5aeZpYzA0qlA0DkJFCClKpHN-aBrYAzFwC9dsOlTCDPsVE-OppxHphnW5u9xCc2Zdmn5TYCIHx0PaAf03gRxw3pQnB45l5b0F-2ckRfnqgLx9vqLZ8J1OeJOVgDcfsg8pl_ZYZn9-Yubnph9h9T2Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=Lb4urrlYLXZtAqeUnBjVAF3xXZsXkVKQxg9Sh1WKBXeZQd4EoOWwfWuQAFAtC1AOUjS8FEO-WB95bEuV5DMWiq6RJpieCFuyYVjjHsqRZPOEBmk9Mi1caSvcisigrzUHmNissu7mVhoqAbsRJ0r-zX9XBzsvwduP7XS1wQU_yzJxzs-oIT4Wzv29bqnkfNQAtw5cL6ys_rITaZGDwyFn9tSz631K7gyscmEKw0guxOLWdLz0gzTqkVEviUxFeCfF4U3IFIxHgjZZEBXraKyjeCcT71TlJ_xN7IyhXASTk1ri1G8Vwm1w_5gb_5aUKvYMEsrsLq4YDNY2ivmwSndKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=Lb4urrlYLXZtAqeUnBjVAF3xXZsXkVKQxg9Sh1WKBXeZQd4EoOWwfWuQAFAtC1AOUjS8FEO-WB95bEuV5DMWiq6RJpieCFuyYVjjHsqRZPOEBmk9Mi1caSvcisigrzUHmNissu7mVhoqAbsRJ0r-zX9XBzsvwduP7XS1wQU_yzJxzs-oIT4Wzv29bqnkfNQAtw5cL6ys_rITaZGDwyFn9tSz631K7gyscmEKw0guxOLWdLz0gzTqkVEviUxFeCfF4U3IFIxHgjZZEBXraKyjeCcT71TlJ_xN7IyhXASTk1ri1G8Vwm1w_5gb_5aUKvYMEsrsLq4YDNY2ivmwSndKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=FHCQ5VGCBSwXxDvJpNHYD8jsXFCFsVIHEKgdfhoLBC7jz5bbqJiPvkSpTzuG2g3QBxnR7N7w1MYfEB3zStRtubk0UfBkIU0MRR03-pdLqGFgtQkUPvj5fMQf32hvaLkmjn5qGQVNNJFQAaVu7jZUWp-w_eUWjRCYBsZUf1xaJCrt_FSTo2Q1gI-LCIH-8E2agU01SX8-PBCjMmMg4uj08iPCyGrdVszkeytGwTRDwtc0VjT8f7umV65x7z2kO2jMoledSJqkzoflhXtA2EPpzhbm4lkeYFKQSj9udWVU5XJ2gitqrGasLN1jUoubBpiwNJ47Es3AtpTEEihaWMHx0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=FHCQ5VGCBSwXxDvJpNHYD8jsXFCFsVIHEKgdfhoLBC7jz5bbqJiPvkSpTzuG2g3QBxnR7N7w1MYfEB3zStRtubk0UfBkIU0MRR03-pdLqGFgtQkUPvj5fMQf32hvaLkmjn5qGQVNNJFQAaVu7jZUWp-w_eUWjRCYBsZUf1xaJCrt_FSTo2Q1gI-LCIH-8E2agU01SX8-PBCjMmMg4uj08iPCyGrdVszkeytGwTRDwtc0VjT8f7umV65x7z2kO2jMoledSJqkzoflhXtA2EPpzhbm4lkeYFKQSj9udWVU5XJ2gitqrGasLN1jUoubBpiwNJ47Es3AtpTEEihaWMHx0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=c4_STyfiOi-vNijEFBLr28veWadD-RQ3JP32g2zRy_Lm3wcNChPf48I6InO3tLd1JZLkWO_pGDkj2WuKrJDw_clIZsMeaXvPxcaG4qLOgmNiR0B0RwH8pVw1dbC85nEgH9IM5b73M1B_BsfCPNUWOP-oNsZEoLOSL-9sk2ID1Hsa50gCBY0IUYciWTEXG3ZeXPoBl7Gj_2nY3IT-vgjzqsDSFYUVXyWDIau57W6bxblyB2zorOoTf0mMEy3UBNA-toLb61tGf04RHim44iOe1Tfrweok-2GTIBS_n3iXgTyIJuUBZBgHuv6ThLsWqe_CIyJ7Baetc-0TdhyP4XS7Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=c4_STyfiOi-vNijEFBLr28veWadD-RQ3JP32g2zRy_Lm3wcNChPf48I6InO3tLd1JZLkWO_pGDkj2WuKrJDw_clIZsMeaXvPxcaG4qLOgmNiR0B0RwH8pVw1dbC85nEgH9IM5b73M1B_BsfCPNUWOP-oNsZEoLOSL-9sk2ID1Hsa50gCBY0IUYciWTEXG3ZeXPoBl7Gj_2nY3IT-vgjzqsDSFYUVXyWDIau57W6bxblyB2zorOoTf0mMEy3UBNA-toLb61tGf04RHim44iOe1Tfrweok-2GTIBS_n3iXgTyIJuUBZBgHuv6ThLsWqe_CIyJ7Baetc-0TdhyP4XS7Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo4wQj1sCgVOqsdAUPkLt7ZTefQ9dFop0-f9ILKKMR7cOuC1PAEHFuFKjvLR6HHZwKz3xJOKLLzwALC--DYzjpldLVkvVvkxhR1DLTcODAG-d_5Vs--GwLclvpatvguUW3sWRlF_fZlHWixuN5BU40zus9HgX-yGAwBihMjZYKCIWhyd1WtQhFU5C07ldFdLhDb2TDIhjoMII2y4SPpyBwYvY-3hfFDlQh_fPKrFAhlwQ8St0s1P26hxQdR3khhLf5q5I3Yfv8rrL1rjYy06SI3YuqQsLimtXdEuNMya65BizWDk6rfkTSIDR-uxabNcx9NQPEeG4WY3GDua6e7xAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTEkOnBYYeHbxp6LsEy1KO7espv92eCsvrAf_-sjJMpVDTrm8uPSGuvRNeOLQ705TuVTrUAAV8uuKaQkv2PGrmClkH1BT4f4TQTPB29M_pNwzSFFGISUNe0AwMyyC7GZe1YqDUbVOFDC21IPpfMwaHWTMlnTbU-tJHl2vg52k9M8mdkQpUAD0tTY012X11xzMEUdkFX0Trp4hbLwfCnrxMEXaqUm2WUnJmrTRhL-dJWSilYqMe1TMFKv5ZwaD0EwMjv2bmfyqeTFoCIf6F-OrL89QfelcovmNr99j4q6EhD-8u25EO0atRJQe7RvPTZ73-1O5ji0giita6zIZbaWNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-8oWqzSfkJOJXvI4G0Q_k8ye7QYO7dI7j3xXGXfjBiu8KJ6on0fb7z9NcsoPpC9S6mG4D1Avlm--UTrRp2Wgz_l6g1fTZJQi4-xjryO1b6we_2gQIcgtePlS5llgv7Iap4v8aJ_hDECGHY3f6XuHGO-uYXeySDU94igqOfPvDK_PpucEb8WRAYIsaV23zAU2nWWhtnPnI3aEWaZQ2S6s2Oc7ipC7u_u5MIWEcYhAYD23MsznRWx2sNWETg9VloZdOtY2Av0vhblUjO43NS6cIMWt1FFsTlci5kvaV8g37jkmdAlEMIQ2ggeGCChi1ToBvf0XvE_XHx_xEbnsdjodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu5tcUDTB69vVPUMHH0FLMahaCuGkzInRgAYD6bq1v0bVT9ITOMxyOQUIgkNUktiKJAO1weRvnQQbSk-ilu7ImePmbab5nm_05aOqwnUK7_VsJndh5kgLfpHecOER4CohjAogbrldSRFK8jvYlV4QaRWlL4gL7Ol1tchNci7sC7E7ctl5-mQVe0ImB2nbTLGTT1QArNDD9G-SCjR1fnWEpNtTVSihkWGtoEg2szppSm5PLrJ4TiXWijMH0HSSWb1ivRJ6UKVsNIgJauq_OTxX9I_4Rg-vBlqPx3mhjKXC2TNRF42avMUH870XqallxpTPlLWn7_Dj61Qko46eMxQhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRH3moI7Vq9TgvUMeSJ4ys8z3FliTVzOx1jH-s3xYS1r_4A3CIpjY6CISfjHlnwbtq5ncGnEPLrh8-wxs-e--oZcyjYDkpCjxAkdLjuStEWGvbxRNc_szW0VE0vuPYqkegVnnyVUMK_oAnOr5ov6Y-ozmMU_I9J0sh3vulzU7m-ugZDiZkiuGNSF_8847dn4zBO7c_lqvttxbWaXVrQUqv1fMRM7WZ81ZkpWcGP6ibO2rG1BN04ZAsTIwDjEfLAw-PrTx_mv_GbJykxR2g5lcojd2q9fQeUFcmHwqPQiU7Cv-lQpjV5r9QhdVSY6co7GRXNFb1TBrdlrnyvQi_RCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=n7utg5EjXpTqnaG-dgwwuGm3LxAoLV5fEErOCGJcsbSu_F1h0zcvoVfD05o7oXPQdv5f80l_v81WCZNzYJnZP6Jc4hCCuJKZZdtgupVhXReSbEpTehhbw58qcBmqRNyhiCk3L4ogxEJlFwxwacLKZjqBPUCMHhIOCHsrKikOPoBe8uLWMc4N3vjpZXPF5szDXXDOzDRjAMPKgk-b1QbuNkd1IhufoZavEvItK59Hvu1PlY7IlMSk0DAtVLZtNuBoY8uejowau2hj7n3Vx440ISVtn7NpjuCazn6Hm65tyjazYV-zWg3B4PYo1ZE4f-9dmj8PoLyyHAWek_MoYPOHvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=n7utg5EjXpTqnaG-dgwwuGm3LxAoLV5fEErOCGJcsbSu_F1h0zcvoVfD05o7oXPQdv5f80l_v81WCZNzYJnZP6Jc4hCCuJKZZdtgupVhXReSbEpTehhbw58qcBmqRNyhiCk3L4ogxEJlFwxwacLKZjqBPUCMHhIOCHsrKikOPoBe8uLWMc4N3vjpZXPF5szDXXDOzDRjAMPKgk-b1QbuNkd1IhufoZavEvItK59Hvu1PlY7IlMSk0DAtVLZtNuBoY8uejowau2hj7n3Vx440ISVtn7NpjuCazn6Hm65tyjazYV-zWg3B4PYo1ZE4f-9dmj8PoLyyHAWek_MoYPOHvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YN8aN7WWemlN-BEO35w8o998TNY9_ur5BQZlyxQgSJIhDeqQjqHNJcsfNPBas_wMZ_5Me1YMeddFuZDZMQ5-zWZ1kNB7VMdiaTD7cdli5GjSsQ9V3LdN35CjpNA6FnzoOcIQxZAA-XHurYG0yNIN_2VZRWDNjD0g_8GPVBRG2-CmWsQX5rFzYucsTlRk_UwQ9qOSKt8dsaLgvXjqRlqMD8xZAW6l40uuhpJyGqtyYowgtRV_5ZcdFvqCS_HYNVlpt6ThUP4YXXQYnZD2Ur0G5XmQrRhDkcmlYrOcAVqbBAxPMmAtsmUIO5-qXWYXFVuj3MSwptrnmgKJsS1uC7lujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZObgtS9fzV0ws7MiSA63doC00obXrx23o0pNMeUKUbEfxQHgHwjvhXyrgBkgKrN-aUaK1AKla72Trr_hTA0sO7HgOQc90RqYXMERL8yZyxfG59NsL70az8s6MhD3CdJs3AqXa3OP0yYavxHYnQ31LrCZKEj0RvxosviLKMainVjmmt_nAgBBw6WO_S_rf7YB9hanEkP2IdiKIxa9nEjE17aI700DbtWmb-rzu9d4JJ34Lhn42DAqWkwbkfwji6xqH7Q8re5_BL_JmggAQ_3ipK66UQGhw8zeJ7rQcwx2TBwn4XfITL_PLYbBsj6VQqcTFovcGT6a41nHQwugZn85bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=QmatS4LNoltax3_68tv6ltYrxxTPt0r8QkD1f8YZ6-6M4KBB3fHEHbSTMCDyDEkOJMescuFlesQodYbdxazBh7MwkcnlEfCWYXotU7pmpHk4dg_SGl_GYtOiUPoXdoiJFIGwyRTWn13k85Z5iiZcCOQPQa7LHq5E5fiQWB07iScgSyZygppGq5wmMhH5OvZJqDUGr-J_SK5676zqOKUQPYYH5jRQEDQgFcTp68GWp1AbCsI5Tg8BKPG1bYvbn7ajh_CksjEi0C1HqhrpzewE3u_z3uwUvuvtjw5gqupA6hQM3HSMz1eoUx60bFxOYGVghMk1YnIx3PI-kn5GKFSzKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=QmatS4LNoltax3_68tv6ltYrxxTPt0r8QkD1f8YZ6-6M4KBB3fHEHbSTMCDyDEkOJMescuFlesQodYbdxazBh7MwkcnlEfCWYXotU7pmpHk4dg_SGl_GYtOiUPoXdoiJFIGwyRTWn13k85Z5iiZcCOQPQa7LHq5E5fiQWB07iScgSyZygppGq5wmMhH5OvZJqDUGr-J_SK5676zqOKUQPYYH5jRQEDQgFcTp68GWp1AbCsI5Tg8BKPG1bYvbn7ajh_CksjEi0C1HqhrpzewE3u_z3uwUvuvtjw5gqupA6hQM3HSMz1eoUx60bFxOYGVghMk1YnIx3PI-kn5GKFSzKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=visVFETSmjWKs-B3Dzde-0WZ9ECgW6UXJbNC6HygzNfjkOnZpYykVvZwLwUp4zul5PINiM8pCYEmXAB50zczIcj98J-tIUPTOY9ZxeKLngOoa6gctBc_3R_2VO6iXiRbSgOqLiK1NgCMoOKzBkZHHlGzk4U0PZaNmMK3GDQTUZSAfMZfVs3gvx5etEq5Na-UIt_9AtL1NLHV66V77wDaE2NzuU9ycGCzcL0gGsshTNYY0fUMrTvpuB5Xmqh8cFswi8fO5EvZRSKRhvfJ0AwrsLukPc9K587NRDgk7kVDqBo6pyeqzBze4Xvug-iyg-OiuIYej5jHCWjQRPIC-1IBOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=visVFETSmjWKs-B3Dzde-0WZ9ECgW6UXJbNC6HygzNfjkOnZpYykVvZwLwUp4zul5PINiM8pCYEmXAB50zczIcj98J-tIUPTOY9ZxeKLngOoa6gctBc_3R_2VO6iXiRbSgOqLiK1NgCMoOKzBkZHHlGzk4U0PZaNmMK3GDQTUZSAfMZfVs3gvx5etEq5Na-UIt_9AtL1NLHV66V77wDaE2NzuU9ycGCzcL0gGsshTNYY0fUMrTvpuB5Xmqh8cFswi8fO5EvZRSKRhvfJ0AwrsLukPc9K587NRDgk7kVDqBo6pyeqzBze4Xvug-iyg-OiuIYej5jHCWjQRPIC-1IBOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=WnyuxayEguYgxZVRj7MXkHmAM8oVxLNbfJDVLLw2Dd0EB_XyDm-BX1r0bhdjqZn5cJOOr9_wu8Y__DLLZrkfK1NX4eixWRfre0Bqs5ECXjSnXgV2INb4Lxky3R334BfM7kqZPKFEHQqyRkMFnbFISKKPfvhIarxx89KbtuZwaZgxXmOIUA0S9WTxJ401PgCeZBBsJu-KBmsg653rMf1dzC-6JjU_-UhWf69_SfstqFasUa8Q3W0CXVjRtk5fT2Q2ku1liaeIkj2YXfMIn2fOkfBqjkSWXB4F0S9Y6zfoPeFKXk1ixPT4RAcgw85WOVyMS1pw8UTU9YqLPru7sBKjfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=WnyuxayEguYgxZVRj7MXkHmAM8oVxLNbfJDVLLw2Dd0EB_XyDm-BX1r0bhdjqZn5cJOOr9_wu8Y__DLLZrkfK1NX4eixWRfre0Bqs5ECXjSnXgV2INb4Lxky3R334BfM7kqZPKFEHQqyRkMFnbFISKKPfvhIarxx89KbtuZwaZgxXmOIUA0S9WTxJ401PgCeZBBsJu-KBmsg653rMf1dzC-6JjU_-UhWf69_SfstqFasUa8Q3W0CXVjRtk5fT2Q2ku1liaeIkj2YXfMIn2fOkfBqjkSWXB4F0S9Y6zfoPeFKXk1ixPT4RAcgw85WOVyMS1pw8UTU9YqLPru7sBKjfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=RCWJ-kuNKWNXQ31l19GCqUmUweRK4DgAATLutWXfDTtyUIu2ZoXh0F-4BFXxzWdLu8OwmpfKAS5qswTJ9JrDWjpABD7NkC5_VhT1vZuElvej7K0J6rDyJszy9kUxsbZfHOZkGF8aJXmvZOcSRoRRbM7t45o9iIyLbOUUP3wfT7Oi-Umh_1J9MEaoSaHIbQCQ88012lDV1johl0zKS1ICvV_nM-3H4oCXe4lQg7dAGAbJsnjJfspI43OdQ0oP0a0TOsEwg7Z2Zq-HC4mQIy63Cl-E_e1XyzDTpvlBLr5x-Rzkx-wKyAEeP-vF9jaNtT_xYSdXK2Rid3MC5po_FjYCwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=RCWJ-kuNKWNXQ31l19GCqUmUweRK4DgAATLutWXfDTtyUIu2ZoXh0F-4BFXxzWdLu8OwmpfKAS5qswTJ9JrDWjpABD7NkC5_VhT1vZuElvej7K0J6rDyJszy9kUxsbZfHOZkGF8aJXmvZOcSRoRRbM7t45o9iIyLbOUUP3wfT7Oi-Umh_1J9MEaoSaHIbQCQ88012lDV1johl0zKS1ICvV_nM-3H4oCXe4lQg7dAGAbJsnjJfspI43OdQ0oP0a0TOsEwg7Z2Zq-HC4mQIy63Cl-E_e1XyzDTpvlBLr5x-Rzkx-wKyAEeP-vF9jaNtT_xYSdXK2Rid3MC5po_FjYCwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=TlV9Of0vmQBc7c7ZxN0j5sNMO8Cz6hP3l4vkUj1RdmIqghXyy0KOn89nkSfuuiZ7RSIhDn0p0-xV_IElwXV1seu3jQJRLPnc-PadkHI_kUqyeCJJ4M24KTNkrRuhUo7z3mXrFxstzftD26raO-LYoXkZL1lVEzdiM8GTyVn_QlU6VTMo590S32_cwI1eXf7Pm_meNZQQIsyxvQf318XADxqywa43-cwBkDMjD-zEMxRpkx7iUQr5fLIb4vu3zs1j8b6c4WX84BW0OIyTt93gvVv-zZc2VHv-edgyLT6OxlHNNcJ4T5EU6tospvn0d8WLTH_IsAcrRZ0lx8O5sOBrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=TlV9Of0vmQBc7c7ZxN0j5sNMO8Cz6hP3l4vkUj1RdmIqghXyy0KOn89nkSfuuiZ7RSIhDn0p0-xV_IElwXV1seu3jQJRLPnc-PadkHI_kUqyeCJJ4M24KTNkrRuhUo7z3mXrFxstzftD26raO-LYoXkZL1lVEzdiM8GTyVn_QlU6VTMo590S32_cwI1eXf7Pm_meNZQQIsyxvQf318XADxqywa43-cwBkDMjD-zEMxRpkx7iUQr5fLIb4vu3zs1j8b6c4WX84BW0OIyTt93gvVv-zZc2VHv-edgyLT6OxlHNNcJ4T5EU6tospvn0d8WLTH_IsAcrRZ0lx8O5sOBrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc6wZ4FAyatpw779VLEgr9h9j89zmtKf0k7DNJcuIPyX-RpLRtD0JzyBHxi7jiup8wih-327L4w544dFDRNhYRvqmO6H0LlgNc9Kfr8jxhQ_YAZBWd5TNr7dCzPBnBNnmDBGacPyhT9lbXvdoD6FrXRqsHWxbFwQ4shuVtRzjuwznncEifBMzOZUO0d-HoS6NJr_hGYriAJCGmvFUBBLM2NRfMWQxXNgM8SVuSNdr8TQJ99OoQPM8Nq_HfFUQrwAe9a28DruuLOyAWZ-kFlyJWteN43yw7GjMwRXWd-oReR6lO-sfAAts0R8QaA0NjUgbNB2BjUR_WUU8DidXRpBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmQsP1mU4b_t6MOXYpomCAz9WjrwkIeNal-16BuG8Klco9EB-6baXx121-8jzb1Lg7A34dh66mVmm2nj6Ytti89dEJqIspkueox3yF4vV_et493mKk1C_O3QAHkEC1XFSdhqm5zNcJg2d1fIVu1jmE-PmH9AbhnSt5WhVSDwN5KPB6EaHfgDrwvtXHHyFaqj3aciPzFyvvE5CvhdEjR3H5iq7yd6HMhKcPSe_fmkXSNnI_ly_QKZn97L6StzYsEd1YX2xH26L98oOlonoCVpvHgozvoMXuBAZNVLefOuWKH9QTDukiJyIzTwvT0JyFvlL64-bo8R3Rl7H1-UYTNaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxIvTzl48USTeTAnY4Kd5Z7-JStmFlZcDCx4vqeEprOYyFY6pZewdfy716FQXD6fGBj099oLv0wfWArXNkkSijREvkX6w4xeoqZPoeD2OXnl7mXiyhUz47sDB4cD8_ljSN0SO6_ajqbbTKaQ9OPK8KCo1QEvGTW_uN5k3YUcZtScr2D1jKx13Rm2QQvrBYBmhMXrX0GA-sb5-1qzeK-JZdfcoAykC_dLqn52KSPx0zqiguTkbN5hUKligquTSh_89e0cUasXWqRf0B8fkCGYQDQ_IM1ykD585uJabOlS2jhWlmsdBlIdHiY2gBXNy19RKL3aUnRkdrQ8tA-NM0auTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=rw02NzuGeNLUxLr4QbUxNnGAFg6Qz9w3jeMTNux_QRhoSZ3AusRebfSqXpC8R54qXjlDh5Oi87nXQ8-0ahVliFQXNP3HhV9F5xFkq40HPE1q8-_JW8oGG-6mk4zh7huw25xXGf4iuc5vN-dLudSTx9ZQYXFCdLtVX2rEH11YKsTGZvY4aD9Ydf7oMqfVfLpNAnctJEtGlg1EsnRxOCNIfSsEqyHC1GrQaS2L2nLb8Ds3kERerP_fAB5s4ebGQiYaiXvRv11lqD99fEZcKP-BJgfB_S5ZKWqXVgqhY60ZGUso6bg7AZlxYyopToBpSTGO6lKwk8ueU0GJnHtKjY3xag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=rw02NzuGeNLUxLr4QbUxNnGAFg6Qz9w3jeMTNux_QRhoSZ3AusRebfSqXpC8R54qXjlDh5Oi87nXQ8-0ahVliFQXNP3HhV9F5xFkq40HPE1q8-_JW8oGG-6mk4zh7huw25xXGf4iuc5vN-dLudSTx9ZQYXFCdLtVX2rEH11YKsTGZvY4aD9Ydf7oMqfVfLpNAnctJEtGlg1EsnRxOCNIfSsEqyHC1GrQaS2L2nLb8Ds3kERerP_fAB5s4ebGQiYaiXvRv11lqD99fEZcKP-BJgfB_S5ZKWqXVgqhY60ZGUso6bg7AZlxYyopToBpSTGO6lKwk8ueU0GJnHtKjY3xag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFjOgPWdk5wmVmzVnUdtjFr2pS6xl_lREesl0miplbMN_1XI2lhjfd3d_8rh3dGcHylWtiu7d1Fb_3U77h_eEKqgqnAOSBtl0Ck0HncRAo7_YqiV-DLpjiNfAgf7bpIA7-71UwGhiKjSjJu3_jAvuWp-vXjScSU5Uyu8Xbuf8MwiNbDY68heUO4LlVTFoIYNI01sWtMhA-qT6ekKzZfZQvM2GLEvhF-ySwWI2zctZNun2gXItbPRuBbbPtsGwWQYDI4c8TIHxvHovXibzhpAbqirXCG4MlWXXaH_R1XoWlntOzkwvUZpoyggUJz7ljRSy8XvHkffEGgqbQScUPxBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
