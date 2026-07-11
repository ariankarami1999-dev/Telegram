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
<img src="https://cdn4.telesco.pe/file/QpmZhgW3Oo61YG57OTGI19WIx3K8XlK3z1QpG-rhYy2ndHUDgbGgVVlzQeqpZOu5C_RRKsEvkrVCand1HpKUyKydVHFK-xPZDEYail3zpYBMKFj76lYopZsNWmF3-y1g0LvWwt4luOBY0aO98KDqit3zpcumvntSXYy0YeALRAq_nW4hNPgxGBx5iVRz08cMTu4DsioFoMKF5hxH_LVyOD8VoQneQzB31ChGjd843hySFuVLX0fCOx3z24US8QXKjX8isnCVuy6Rt8bDpi0DoBz6YO-h4obbIalDXloRrL8HWEEEIaiWu34ylSp4OEDPC_yN13-4JYq_scK_wQRSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 16:28:18</div>
<hr>

<div class="tg-post" id="msg-669788">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8c761bd0.mp4?token=rnq0QunB-awJu24Y2ne_GTDg--u5Esk-7YkcZyMvOslCRWmwsYdoH6jbE9TsAFkwmk2CQf8-TGofTQBsYMQT6yr1zQTh81OCuzCh6z3MXjROaulgGj1g4mSdSUHmXxxG02GM0Q26ScYPN6Sa4rrxXnp5h8aZL8LL8B6f7z4D5A55kP_4_pTXpCUU5_OjezKrLJmrrph1zUTDDMk-MEO6umPhzj7NY25FtzDGAM4dBD1mdDne5g1zMmpwIdc7UDdtpO-jKAm7waqIwl69dxBCxG9P6r1IkIHi3RwNd2SXJqq4uGGaW5c9mI1gXhVX-mNj4R7E8_gRIEfWSmzCpesgVk6N5Fw-v8iF6mDa6_Fw5BZk0FzxRuByJCWS74OeT-JLz8x7drdk7aYot-qp21tm5VZq2-Fs8rpZZ8ilrbDXiu2FJKEltE53ZHT6TeVBukElEZ0OS2abAl3ouO7BenjvFaGd3kVZ547l3J8xS_P9CH9K9ztMGTOh6SudIiTWsfL1qothOZDzRUjq4TWC0-gL0sQ17_xAduZGZW_OcMtC4c-gm93ONRmoD8Cikeb9KszAiDSEhbSOVVga2it8Pfd5B0K9tnqlO__k74ayliBFBnHrY5m97WzRnLpzz8-ZII8ID3YI4MKnn4yIouRKD1_7cxaVbuNqXn6iW0MP83GOsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8c761bd0.mp4?token=rnq0QunB-awJu24Y2ne_GTDg--u5Esk-7YkcZyMvOslCRWmwsYdoH6jbE9TsAFkwmk2CQf8-TGofTQBsYMQT6yr1zQTh81OCuzCh6z3MXjROaulgGj1g4mSdSUHmXxxG02GM0Q26ScYPN6Sa4rrxXnp5h8aZL8LL8B6f7z4D5A55kP_4_pTXpCUU5_OjezKrLJmrrph1zUTDDMk-MEO6umPhzj7NY25FtzDGAM4dBD1mdDne5g1zMmpwIdc7UDdtpO-jKAm7waqIwl69dxBCxG9P6r1IkIHi3RwNd2SXJqq4uGGaW5c9mI1gXhVX-mNj4R7E8_gRIEfWSmzCpesgVk6N5Fw-v8iF6mDa6_Fw5BZk0FzxRuByJCWS74OeT-JLz8x7drdk7aYot-qp21tm5VZq2-Fs8rpZZ8ilrbDXiu2FJKEltE53ZHT6TeVBukElEZ0OS2abAl3ouO7BenjvFaGd3kVZ547l3J8xS_P9CH9K9ztMGTOh6SudIiTWsfL1qothOZDzRUjq4TWC0-gL0sQ17_xAduZGZW_OcMtC4c-gm93ONRmoD8Cikeb9KszAiDSEhbSOVVga2it8Pfd5B0K9tnqlO__k74ayliBFBnHrY5m97WzRnLpzz8-ZII8ID3YI4MKnn4yIouRKD1_7cxaVbuNqXn6iW0MP83GOsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ویکم از فصل چهارم
🔹
در این قسمت ادامه تجربه‌ نزدیک به مرگ خانم خدیجه مبینی که در هنگام خواندن نماز به خاطر سابقه بیماری قلبی به ناگاه روح از جسم جدا شده و در عالم برزخ شاهد عذاب بسیاری از انسان ها با گناهان  متفاوت از جمله رباخواری، می‌شود و عظمت و هماهنگی بی‌نظیر اجرام آسمانی را درک کرده و در نهایت با چشیدن دو قطره آب که در تمام طول زندگی خوردن هیچ چیزی برای ایشان طعم آن را تکرار نکرده است را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: خدیجه مبینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/669788" target="_blank">📅 16:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4c72f6a4.mp4?token=BSJfKuwHHq6pBQ4Pg-NP_lr2NvNiZGc-yvtaPS-VBtr5HmAXinlN8BEIwJZmoJCTP8k88LJgoT9flQFD2h20adjv1iqcEYYkTLpYrGD-DwgorUh9BnJCXHS-654Q4MGSf7Q3zlUhuKlMErTfm-030qjcz68cmHR1xYOahHZ9Ep-7rmEeA6Vdg7pQW6IRKMt81siM0v0mvA2NCOTyy_v2yP4Pa_9_jT9pBMHjTFx9FRquKRV85Sc9u57n1Ajg7ZQ6YkvgLH9Wxzd7sY5e-4tSNcnNgDvCxK3UX24SCcMqna4GkwnEdc5kH90kxcupTlsWxNnopEszenhhseRfqN4iwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4c72f6a4.mp4?token=BSJfKuwHHq6pBQ4Pg-NP_lr2NvNiZGc-yvtaPS-VBtr5HmAXinlN8BEIwJZmoJCTP8k88LJgoT9flQFD2h20adjv1iqcEYYkTLpYrGD-DwgorUh9BnJCXHS-654Q4MGSf7Q3zlUhuKlMErTfm-030qjcz68cmHR1xYOahHZ9Ep-7rmEeA6Vdg7pQW6IRKMt81siM0v0mvA2NCOTyy_v2yP4Pa_9_jT9pBMHjTFx9FRquKRV85Sc9u57n1Ajg7ZQ6YkvgLH9Wxzd7sY5e-4tSNcnNgDvCxK3UX24SCcMqna4GkwnEdc5kH90kxcupTlsWxNnopEszenhhseRfqN4iwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی خاص از مزار رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/669787" target="_blank">📅 16:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
آیا می‌دونستید اولین بار پیانو توسط ناپلئون به ایران وارد شد؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/669786" target="_blank">📅 16:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2632e671a.mp4?token=TZPJ4qgLROcHRa14ssiWzuzNHqsIRI-0J1DKlxRV9E1Y7QxZjAeLTrVuelvOEpFUrOJp81Xbs2qNbAuTSTHvJRXxhT6HmbeP_9xCZn2xNRWHTVlH4NsK1G_6cWeoDdanlVjMi2GbHhoPTXNG3ZTB9ngrCHtSN9pHbjpXRwPRCnKItlKyuAhSYCUKVdmoJYXvWKKu4mY8G-BbeZcsrgu_JSuhggNdilNl0NNet5u9SFa3ELGwOnebKnM2weJh3xAq0CY183pohNjnF6DDD981I7qUwCOw-CK7-y-ewRsOB6S-kEkYDYl4CS5hJQsPLgBDTlYhmffLjqWShUlvFWynWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2632e671a.mp4?token=TZPJ4qgLROcHRa14ssiWzuzNHqsIRI-0J1DKlxRV9E1Y7QxZjAeLTrVuelvOEpFUrOJp81Xbs2qNbAuTSTHvJRXxhT6HmbeP_9xCZn2xNRWHTVlH4NsK1G_6cWeoDdanlVjMi2GbHhoPTXNG3ZTB9ngrCHtSN9pHbjpXRwPRCnKItlKyuAhSYCUKVdmoJYXvWKKu4mY8G-BbeZcsrgu_JSuhggNdilNl0NNet5u9SFa3ELGwOnebKnM2weJh3xAq0CY183pohNjnF6DDD981I7qUwCOw-CK7-y-ewRsOB6S-kEkYDYl4CS5hJQsPLgBDTlYhmffLjqWShUlvFWynWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دفتر رهبر مسلمانان جهان، یک چفیه و یک انگشتر متبرک رهبر شهید را به پسری اهدا کرد که پیراهنش را بر روی تابوت ایشان در مسیر کربلا انداخت. این پسر اهل شهر تلعفر عراق است و با تلاش‌های انجام شده، پیدا شد
.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/669785" target="_blank">📅 16:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کمیسیون امنیت ملی پیگیر ثبت مراسم تشییع رهبر شهید در گینس
امیر حیات‌مقدم، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
با وجود تلاش رسانه‌های خارجی برای تحریف اخبار، ابعاد عظیم این جمعیت آنقدر گسترده بود که قابل انکار نبوده و تصاویر آن به جهان مخابره شده است.
🔹
ثبت این مراسم در گینس می‌تواند الگویی برای آزادی‌خواهان جهان باشد و کمیسیون امنیت ملی مجلس پیگیری‌های لازم را در این زمینه انجام خواهد داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/669784" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS9II3ZbkX22NIHD3oqmc84DKx6HBmU4xdjWzD_y73I2z7EwqBKZn-f-yXviqVRt8qJ8PiqGyrCvV0M5h-5VejiAVOY0NRgVLnNpQZVDAko_SZ1_KQ7JD9x2Ikz9ut7PH6wbCUOZCO4hr7XMMQ_G69eJlN-ynek7frc6qJooJEHoTOPwgmfYgyVxDy7LSxgHJ_hO26X0COStuBlbsz7Fbgdk1Hnnmi9o2HsxC4JC-6Wo_wjpC3zFSd4GOVc9xk4Fv0dYbVVg8IvTT9oG_K-2kc8Uy3RAxCSmdrFNpj-GSXbB4T5H6HHXREEzb_ruATfrgGBSCd4a97AdwtOBCJWwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز پیش‌ثبت‌نام حج ۱۴۰۶ از ۲۱ تیر  سازمان حج و زیارت:
🔹
پیش‌ثبت‌نام حج تمتع ۱۴۰۶ از ۲۱ تیر آغاز می‌شود. در مرحله نخست، اولویت با ثبت‌نام‌نشدگان اعزام حج ۱۴۰۵ است و سپس سایر دارندگان قبوض ودیعه براساس اولویت فراخوان می‌شوند. پیش‌ثبت‌نام رایگان بوده و از طریق…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/669783" target="_blank">📅 16:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پژمان جمشیدی که ماه‌های اخیر به‌دلیل پرونده قضایی خبرساز بود، به بازیگری بازگشت.
🔹
پرداخت حقوق به خانواده شهدای جنگ رمضان ابلاغ شد.
🔹
پاکستان و عربستان خواستار اجتناب از تشدید تنش‌ها در منطقه شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/669782" target="_blank">📅 16:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شوکه شدن شدید ترامپ از میزان شرکت مردم ایران در تشییع رهبر شهید
🔹
به گفته دو دیپلمات ارشد نروژی که رابطه نزدیکی با ویتکاف دارند، دونالد ترامپ بخش عمده‌ای از مراسم ادای احترام به رهبر فقید ایران را از یکی از شبکه‌های تلویزیونی تماشا کرده و حداقل ۴ نوبت در بامداد روز جمعه ۳ ژوئیه همزمان با مراسم ادای احترام هیات‌های رسمی به پیکر آیه الله خامنه‌ای، با عصبانیت با مارکو روبیو تماس گرفته و او را شماتت کرده که چگونه دیپلمات‌های آمریکایی نتوانسته‌اند کشورها را وادار به خودداری از شرکت در مراسم (آیت‌الله) خامنه‌ای کنند.
🔹
او همچنین با مشاهده میلیون‌ها ایرانی سوگوار در روز دوشنبه ۶ ژوئیه در خیابان‌های تهران، نظر چند نفر از افراد حلقه نزدیک خود از جمله لیندسی گراهام را پرسیده و گراهام به نقل از یک ایرانی تبعیدی نزدیک به رضا پهلوی به نام بهنام طالبلو به ترامپ اطمینان داده که کل شرکت‌کنندگان در مراسم تشییع آقای خامنه‌ای کمتر از دو میلیون است و جمهوری اسلامی با شیوه‌های تبلیغاتی خود، نمایش اغراق‌آمیزی از تعداد شرکت‌کنندگان نشان داده است. با وجود این، ترامپ از پاسخ گراهام قانع نمی‌شود و به یکی از دستیارانش می‌گوید که احساس می‌کند توسط جمعی دروغگو محاصره شده که اطلاعات ناقص یا جعلی به او می‌گویند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/669781" target="_blank">📅 15:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRVimbjnxaS0UgknxCAf0BLePcctZu3slbfj5isyztlR59rM9PNzMTziS1Kxzpr2J-lrPbsEzDUkXyMLJmiaYb9DWEY0i-sWE5-Xn8MB0A9xMuAuOJXLaIDRyXrNd1rftOA47_qqGUpFVZyVNCk3Pn5IWcr8dwTfCj-cKgvCjf-iare6gSU0LG5H7xpx5DkMjSH9NaJ1uXJEPu0HuujFWhZ7Z9RgQsKTb65zyymBmL-5YB1__LI9tLefLnYtH0I8RLRAsWNa_35fVlPp-9fzkGXyiY_TrbPqijttGGFBKHqaqLPjenBr1GiS1mx3RUwhq-6crrMS9KvzVLd0etFTFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعجب خبرنگار آمریکایی حاضر در ایران از بازسازی سریع خط ریلی پس از حمله آمریکا
🔹
خط آهن مشهد - تهران را که آمریکا ۲ شب پیش بمباران کرد (در تلاش ناموفق برای جلوگیری از رسیدن سوگواران به تشییع سید خامنه‌ای، بزرگترین تشییع جنازه در تاریخ بشریت) و ایران فوراً آن را تعمیر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/669780" target="_blank">📅 15:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669778">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
روس‌اتم اعزام نیروهای خود را به بوشهر به تعویق انداخت
ادعای Voice of Emirates:
🔹
شرکت دولتی انرژی هسته‌ای روسیه، "روس‌اتم"، از به تعویق انداختن اعزام اولین گروه از کارکنان خود برای ازسرگیری کار در نیروگاه هسته‌ای بوشهر ایران خبر داد. این اقدام محتاطانه در پاسخ به تشدید اخیر مسائل امنیتی و حملات جدید به خاک ایران صورت می‌گیرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/669778" target="_blank">📅 15:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669777">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
اختلال موقت در شبکه ارتباطی بین‌بانکی؛ تراکنش‌ها در حال بازگشت به حالت عادی
قیطاسی، دبیر شورای هماهنگی بانک‌های دولتی:
🔹
هم‌اکنون از ۷۰۰۰ خدمت بانکی، درصدی با خطا روبرو شده که ناشی از مشکل شبکه ارتباطی بین بانک‌هاست.
🔹
اطلاعات حساب مشتریان کاملاً سالم است و جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/669777" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669776">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ، روبیو را حاکم غیررسمی ونزوئلا کرد
🔹
روزنامه آمریکایی گزارش داد که «مارکو روبیو» وزیر امور خارجه ایالات متحده، پس از عملیات بازداشت «نیکلاس مادورو» رئیس‌جمهور ونزوئلا، عملاً مدیریت بسیاری از امور این کشور را از واشنگتن در دست گرفته و به چهره اصلی سیاست آمریکا در قبال کاراکاس تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/669776" target="_blank">📅 15:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669775">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y07xuBpU43iBWlv0JhFlOCDmYPaSj0eXWOWW0vLiU9Sm5xMKoEQV6RfRF-fLQxDLzgaOIhnlTj9IY-4FzqY-Cmj9_W2rMYvU8OuRtImIthe86CCzQ3jjiaunkQMAvYh-jurQt6lqza3C4Q13txTf2W7jtG__0BmllRnlCg32Q8WYHHPwEjuNujjmdlNHwe3jIFNv_DbSXONkrrCpWzqHx4gKekgeCiFUf4gib6gpiRd6yeyTKkN5iRUZvc7VMbehIlvkwut95ysgvWxhP14T4MnY9jhOUNcsXWGjgKSbXg9G89F-ruPMeQHRzJ8J8d1gWJw-ajR6v970474njVqYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عطوان: نقض آتش‌بس نتیجه حماقت ترامپ است/ سیلی بعدی ایران و مقاومت محکم‌تر خواهد بود
سردبیر روزنامه رای الیوم:
🔹
پاسخ ایران به هر تخلفی خیلی سریع داده می‌شود و حتی یک کشتی جز با هماهنگی رسمی ایران از این تنگه عبور نخواهد کرد. از همه مهمتر اینکه سیلی بعدی که ترامپ و شرکایش دریافت خواهند کرد و شاید حتی محکم‌تر هم باشد، در تنگه باب المندب خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/669775" target="_blank">📅 15:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
میدل ایست آی: سوریه، عراق و آمریکا در آستانه رونمایی از توافقی برای احداث یک خط لوله مدیترانه‌ای با هدف دور زدن تنگه هرمز هستند
🔹
آمریکا اعلام خواهد کرد که قصد دارد خط لوله‌ای را که حدود پنج دهه پیش احداث شده و از عراق تا بندر بانیاس سوریه امتداد دارد، احیا کند./انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/669774" target="_blank">📅 15:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f481e21978.mp4?token=GsobhxiGfof0Oq8KEPs7VFiJm7xIuTU8LM_-dQ_buJidojBCDDdQpK1NTOJRZD3Zgls8zAxP6ECT6X4LFX27tYq-iNNPXBklUErewNyXcd6zfPZBYgRAnqb0y7oRE-tT3P7WHu8i10HZBT9ykMjW1sK6txuxVRJqAfbXQkv4SraAHvWNgk2jKDQnG14Tnqv_Ng8tYe59Tl6GqpNiRAM-HmkkOmoucqFNl1KbKctU1-7wRtLeocRy0ysLMvx_3hC-M8xVpP1mcJgFXCXpVUjy8IDJHk7K-VFDsfCTYcYfSz5F2-TavFV4vUmY7TZ8hJhztcRO6lcSHeH2x_aH3wvD5hwDarGBTKyqkRLSzel-7--R1f7BKkJ4h7oPjZ6UfeWF63tmyyQBbKKr_E73gDO65ppfFGUR_w740eY6CJ-sOZoqqQQyDXKXxux8TxEC24Mb9fgORQShMJIzcTdBNTekl8rehCGAl6IjfegFsJMIY35ywdfr_8RnJsrz63z2joxTVo698LIrkEPxp6tH4lAjfFoBkikrE3TKpQiKpAW8n1aOrl7EjyHV0LEtt1yB1dQUZJ_fIEVA2jMHYZzquCKtK57a-h4U1CnyDbVtmYmaCiwkMaXJp6Uws5GlsgGXQEQc_N7az4vN9o4OW4iO3VOF3ldZqq9OCzOaPHmPC3i307o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f481e21978.mp4?token=GsobhxiGfof0Oq8KEPs7VFiJm7xIuTU8LM_-dQ_buJidojBCDDdQpK1NTOJRZD3Zgls8zAxP6ECT6X4LFX27tYq-iNNPXBklUErewNyXcd6zfPZBYgRAnqb0y7oRE-tT3P7WHu8i10HZBT9ykMjW1sK6txuxVRJqAfbXQkv4SraAHvWNgk2jKDQnG14Tnqv_Ng8tYe59Tl6GqpNiRAM-HmkkOmoucqFNl1KbKctU1-7wRtLeocRy0ysLMvx_3hC-M8xVpP1mcJgFXCXpVUjy8IDJHk7K-VFDsfCTYcYfSz5F2-TavFV4vUmY7TZ8hJhztcRO6lcSHeH2x_aH3wvD5hwDarGBTKyqkRLSzel-7--R1f7BKkJ4h7oPjZ6UfeWF63tmyyQBbKKr_E73gDO65ppfFGUR_w740eY6CJ-sOZoqqQQyDXKXxux8TxEC24Mb9fgORQShMJIzcTdBNTekl8rehCGAl6IjfegFsJMIY35ywdfr_8RnJsrz63z2joxTVo698LIrkEPxp6tH4lAjfFoBkikrE3TKpQiKpAW8n1aOrl7EjyHV0LEtt1yB1dQUZJ_fIEVA2jMHYZzquCKtK57a-h4U1CnyDbVtmYmaCiwkMaXJp6Uws5GlsgGXQEQc_N7az4vN9o4OW4iO3VOF3ldZqq9OCzOaPHmPC3i307o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساحل میامی در تسخیر پاروزنی نروژی‌ها قبل از بازی امشب مقابل انگلیس
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/669773" target="_blank">📅 15:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یارانه
تیرماه مددجویان بهزیستی و كمیته امداد واریز شد.
🔹
دادستان کل کشور: بیش از ۳۰۰ کیفرخواست برای عوامل مرتبط با شبکه‌های معاند صادر شده است.
🔹
حماس: حملات شهرک‌نشینان صهیونیست به «رام الله» تروریسم سازمان‌یافته است.
🔹
۲ کارمند یک اداره در پلدختر به اتهام اختلاس دستگیر شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/669772" target="_blank">📅 15:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdk8HveC7UClPrUtfX29-B2rGTsPsjzZ42ph28nR0sGpj_EfydScjyP0LXHZgnQ8AMPPLQmuDWptBfQMhS3mL2KghlIaQeaG-y2BdGR8sWRBHwPUEf29sjb_upNm1SCwcsPmcKD-kf8KQ0rvVJPZukeUU9nZxv1L-vC8EBkGO7luIb_woTLL7jgP0nkEEAmTCiW997U_KsDyfXh3ptipv6vCFQ1Nqwj5eZcvREiZmRO2cx3WZeW4ZSeeUe6dOfyEF6ci2pU_Fc8h_lrGhy4RVOxEFiE2OemcX4nQ14GUEDVjlKo8kQ232akbFrG6FZZLTMfg5GxU8foNHd-QV50nfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور در برنامه ماهواره‌ای دردسرساز شد/ براساس شنیده‌ها برخورد با فیروز کریمی در دستور کار قرار گرفت
🔹
بر اساس اطلاعات رسیده به خبرنگار مهر یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
🔹
قبل از شروع جام جهانی نهادهای مربوط به برخی چهره‌ها تذکرات لازم مبنی بر ممنوعیت قطعی حضور در شبکه‌های ماهواره‌ای را داده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/669771" target="_blank">📅 15:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سردار ابن‌الرضا: نقاط ضعف دشمن شناسایی شده است
سرپرست وزارت دفاع:
🔹
نیروهای مسلح با بهره‌گیری از فناوری‌های نوین، نقاط آسیب‌پذیر دشمن را به‌طور دقیق شناسایی کرده‌اند و می‌دانند در چه زمان و چگونه باید پاسخ دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/669770" target="_blank">📅 15:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9df6c8ac.mp4?token=h_K_SQm7PffQDDsUP89z2At0UasYQN1wQ9xcCUlnjvFAxZCOmDV4hqaL8JcDHsroZ8kD2qBrSGQXaonfpsDOa5iEIC_33kIc-1Awo9YCGGtHn_qUm1O_i_sstRxJF4yvU-j799cixycHkX0eoBUNJ-OC_sGYbE2Hm06CT_g6Jt18HZabI-TCw9t64OoR6YcF7jzogqMGHeAA_0aDeXauTwrwB4enIPztalLazwA19apA0hiVVGW2U12D6sa4hfr5GpH_5N_VxOPbxzl93hOaWygtT8Vej1VGQVWaysZMYdMgKNVH23R1nkdlFHVC2pwO2G-uDu30mAJpXYuIbbbqDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9df6c8ac.mp4?token=h_K_SQm7PffQDDsUP89z2At0UasYQN1wQ9xcCUlnjvFAxZCOmDV4hqaL8JcDHsroZ8kD2qBrSGQXaonfpsDOa5iEIC_33kIc-1Awo9YCGGtHn_qUm1O_i_sstRxJF4yvU-j799cixycHkX0eoBUNJ-OC_sGYbE2Hm06CT_g6Jt18HZabI-TCw9t64OoR6YcF7jzogqMGHeAA_0aDeXauTwrwB4enIPztalLazwA19apA0hiVVGW2U12D6sa4hfr5GpH_5N_VxOPbxzl93hOaWygtT8Vej1VGQVWaysZMYdMgKNVH23R1nkdlFHVC2pwO2G-uDu30mAJpXYuIbbbqDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقف جهان کجاست؟ سفری به فلات شگفت‌انگیز پامیر
🔹
یکی از افراطی‌ترین و شگفت‌انگیزترین مکان‌های کره زمین فلات پامیر در کشورهای تاجیکستان، افغانستان، چین و قرقیزستان است که دارای ارتفاعاتی بیش از ۷٬۰۰۰ متر هستند.
🔹
از قرن نوزدهم تاکنون، این منطقه با نام «سقف جهان» شناخته می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/669769" target="_blank">📅 15:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669768">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۲۹٠ هزار نفربرای بیمه بیکاری ثبت‌نام کردند اما فقط ۶۶ هزار نفر بیمه را دریافت کردند!
سمیه گلپور، فعال کارگری و رئیس پیشین کانون عالی انجمن‌های صنفی کارگران در
#گفتگو
با خبرفوری:
🔹
نرخ بیکاری ۷ درصد زمانی معنا دارد که نرخ مشارکت در سطح طبیعی باشد؛ مشکل بسیار بزرگ‌تر از این اعداد است و امروز بیش از ۳ میلیون جوان ایرانی در وضعیت NEET هستند و این دقیق‌ترین نشانه‌ی فروپاشیِ کارکردی بازار کار است.
🔹
ثبت‌نام رسمی برای بیمه بیکاری ۲۹۰ هزار نفر، افراد بیکار واقعی حدود ۲ میلیون نفر، مشاغل ازدست‌رفته بیش از یک میلیون شغل و افراد دریافت‌کننده واقعی بیمه بیکاری فقط ۶۶ هزار نفر هستند که این بحران آماری، به معنای فاصله عظیم میان ثبت‌نام، شناسایی و حمایت واقعی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/669768" target="_blank">📅 15:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669766">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvjbyxujLTon_ilRv4JlfdOu3smFALJlyeG9rEIGV0LWif7kIde8iMQ4rJxiVCzs7xOwA-sQmUD9qax1puUuSsSCFnVwwNogFl_K9oHNUVW47IA7EhTQcrI10Y1mnE6f0LrDrFzRv6e-HA_E3F7l7wZ73e2C0gOHve4XrxHy9NxeXQesSbffNZMCQxD2rnvOtiKdxG0lSDfMh5GJpH84i8lvhYniCeSmTKNvQrOVZezYDaJJ7tL06jIbG-KJnwHAYTdlQhWzOl08wPLR7TmCXZoGrfiCNnmi8nKL6H2Jl4bX3dbCByzFiRrVGxykowDSXQuvje71Ctt2KRkwFBb0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استرداد بیش از ۲۵ همت مالیات و ارزش افزوده در ۱۰۰ روز نخست ۱۴۰۵!
خدابنده، مدیر روابط عمومی سازمان امور مالیاتی کل کشور:
🔹
در ۱۰۰ روز نخست امسال، بیش از ۲۵ همت مالیات و عوارض ارزش افزوده به مؤدیان مسترد شد؛ رقمی چهار برابر مدت مشابه سال گذشته، در حالی که درآمدهای مالیاتی تنها ۳۵ درصد رشد داشته است.
🔹
هوشمندسازی نظام مالیاتی، بازگشت منابع به تولیدکنندگان، صادرکنندگان و فعالان اقتصادی را تسریع کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/669766" target="_blank">📅 15:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669763">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2RpfBg1FhcQdLy75sRMvE1koq7xHCENV44dFFnnLi64kpCZT5BMWDlE49dHim5nKIAZzk57yZOwgfQgsVERzN6hQDzKZ3a-Li6N0gVL-1NtKYakiDp_-OGi3w8ufVwmDPLjKhrhN23WJpFQ8nYu8Pkiq5RI7PSOxVpC0mHjMHAGNb56AkZRYwEkKNbIQaZiKCqfgrCuTu_tAjq8wUhduHKKxj1rwhL5-c1Sw7kfCp9AbFYKnVs_re17SSnAr1wciHpXN-lUuJxgPdmspl9yT3fUGm7hiIXMm84715rBbBviwLfP__HGQtLpAMgVjlpWEHaPBBXCUJSdxs3wnF6uvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vt1_F_ImSKzbnIxbxQAyRCCvKNGAOZcpfH3pkIf456AcIJNRmDZ_skJPPYDKpzILFU20ly0e-Xf7o4nt4RyrcDy5rytU_GZ_GHXi3js7MhI_ML_XHVBSO5BGLL0-1DrvACDp2KICIbPsccTP1Xe20mP6k6YpA1adv8hhNaNP_GwxDIFA6Ixfc41_S58PnaWrPMvn9rH-36c807d3LD2lDgFxY66Ifhoh3KfUZdU3ftzIlc0pkHiKu3mMWFeFWerKnUL7trm_GmdUZs7MHt3ScjLimchf0EqniVzTxC-hWn-hUAYpM133Gom-dlgQU5_Q7LVfmFZkvei_QwWY_7giiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooYm7B8Glyjl4rhMjtm8iUOKHnAWPUl2RRsdpa3D5jvUlreKxhSaEgv5VfTnli2sLAGVvzf3PRpxANq1fFuARmxw6Qu-ysYDilxVvh_uQvq725ed3YlRm--lrpYSfZSig3VNr5stxave5kfp3KAX_m_ya6cTIbd8j1v_PU-1b_fmHT9oQ0SmuCaesTlRQ0vYgLEYeq3em9GipxaGQzSh0Jb5PRpNEqhhYnJHwkQ7_NjSyjF5GFXldGD-7kCNq_TM0P_ap5A6pE3kLlEOpsUQMYxyTv_p9pCc9p17FvRbtUCxeEwwtohzdwn9vOHNvptiPkq-kGmMobDnljn04uSEvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ملاقات دیوید بکام با بازیکنان انگلیس در کمپ تمرینی این تیم در میامی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/669763" target="_blank">📅 15:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669762">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqebizkH3BNwbw6FqZbTTd_rJkj1OIqqgUGqPrYGs6OknrE5677nyyrLQd2RGNjcoVHAyAv5Y5cilxraWHwNA45FG2zATzW9-T0Jvep27HffWyGRMSAPuUiitl1YdTmfAgt183Kp1jspQou-uwZUGTvEiyc6iBHL-JS84Hwaapg9eZUwdCQBl0ZoYZb1b3xZaauaUY54YQ54NwBwrP6iMkZN9ANvtoVFLHa4r_zuvTz0noKx8mu3j-BH1ZPazNVQGVArJWlMrDMH2BViAlowr80K0HgSazMtD2p7U0EgCAcpihNL60sgKZzvZiYkJ7h6WTQwmhOEUSyj5amUmb8kVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌اندازی پایگاه اطلاع‌رسانی رهبر مسلمانان
جهان
🔹
پایگاه اطلاع‌رسانی رهبر آزادگان جهان، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای راه‌اندازی شد.
🔹
مردم می‌توانند با مراجعه به نشانی
Rahbar.ir
به تازه‌ترین اخبار، اطلاعیه‌ها، پیام‌ها، بیانات، دیدارها، تصاویر، ویدئوها و سایر محتوای مرتبط با رهبر معظم انقلاب اسلامی دسترسی داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/669762" target="_blank">📅 14:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669761">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c6395d50.mp4?token=g8ekYd8vUQBtiqfVblmhJNgIUFAXOExFt0M8VW211oObUbjRNcpNi1Zl_1Iek22xyEGEZAgTm3pK7Z5hZFlFvErtyJv0powDo4OO3S8vlMWatiArLT8y8aWueBhvqfrAxmnXGAQlUaxuINmWvqeGqc0hebERTOn_B5oUA54-92sCjlEf1WHm6Zm7ffxqAXCsJnqSF6F-Xv_9ZeyWXy9BVHEv7_mSf8kuAIcGwdK8rolLi-1moAxC3WGFyK49A_HuBm1xM1xnuCCTIoB3D9tok2do7UxOFqHmY_1SATK-SlmCqBsg2LPQUYRhNStVtxlDyxLSd-zz-yQXh1bSVw6nGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c6395d50.mp4?token=g8ekYd8vUQBtiqfVblmhJNgIUFAXOExFt0M8VW211oObUbjRNcpNi1Zl_1Iek22xyEGEZAgTm3pK7Z5hZFlFvErtyJv0powDo4OO3S8vlMWatiArLT8y8aWueBhvqfrAxmnXGAQlUaxuINmWvqeGqc0hebERTOn_B5oUA54-92sCjlEf1WHm6Zm7ffxqAXCsJnqSF6F-Xv_9ZeyWXy9BVHEv7_mSf8kuAIcGwdK8rolLi-1moAxC3WGFyK49A_HuBm1xM1xnuCCTIoB3D9tok2do7UxOFqHmY_1SATK-SlmCqBsg2LPQUYRhNStVtxlDyxLSd-zz-yQXh1bSVw6nGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ اقدام اصلی علیه ایران را بعد از انتخابات کنگره انجام می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/669761" target="_blank">📅 14:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669760">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb13e8148.mp4?token=V2DJ3cPd8ZVzVGq4RVHv9FViiH8wi7gL9fKSIh1hQnmT39VZ9ust4oEPdcYhN4B3OIfzIeupz6lWKF30bRPnK_k4W2Ld_3FJAXYIG3BJumjrvC-c5IF9T5l0BGgw5ZpXo7auRgxS7Z8HMg_mLtrCOIqC7E2Qimd_dsL5BifYpQKgni2T8tYtpWBebmhoIfA0z4im4Y-cUkJvVOhjPuHUsE4751wFnfz-hTngmIkHWPgF0KxXRlVro9iT9XqRel0s4HoOTE-pwXtzlPFGdDr6b3N0iyjsFfXZIxOrsQ6k3WWyjA_gIYuSeY7kdqeDCzKiUXPCjz_NPzUqwzUXr8GJLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb13e8148.mp4?token=V2DJ3cPd8ZVzVGq4RVHv9FViiH8wi7gL9fKSIh1hQnmT39VZ9ust4oEPdcYhN4B3OIfzIeupz6lWKF30bRPnK_k4W2Ld_3FJAXYIG3BJumjrvC-c5IF9T5l0BGgw5ZpXo7auRgxS7Z8HMg_mLtrCOIqC7E2Qimd_dsL5BifYpQKgni2T8tYtpWBebmhoIfA0z4im4Y-cUkJvVOhjPuHUsE4751wFnfz-hTngmIkHWPgF0KxXRlVro9iT9XqRel0s4HoOTE-pwXtzlPFGdDr6b3N0iyjsFfXZIxOrsQ6k3WWyjA_gIYuSeY7kdqeDCzKiUXPCjz_NPzUqwzUXr8GJLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند مهم و کاربردی برای افزایش مکش جاروبرقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/669760" target="_blank">📅 14:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669758">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLBrbD9pwNKFgIvozIynjWVACj0yQPfWXT5VaZ7YJvusCviFnhkzBcAMjGwJcU4YNbxaUkuCLFrZyrTclSk5yTWN4UIjtMoxw-WyKjMjbx-9sCm4wDluy00h90RsOtTS4KLJJCOStCdVyGGMo55FxMJ0bGXG-_VtRuz0rYKz6gplHDClDDac-txsarJidfn3-0IIOri37LbT8x8NWCjeUhPGqychpDzFayCiKTfYMeN09_xWdHDdzdq7LYkEpFbp_8mxfVm81WRjosz4MnTsn0gc_5Zsh-7UKtfWYeLJdSGBrSCEh49nkFxmJ97GQ2cXKA0OsHrpexvtMMdsF_imJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزار ویزیت رایگان برای شکستن تابوی بی‌اختیاری ادرار
🔹
ایزی‌لایف هم‌زمان با هفته جهانی بی‌اختیاری ادرار، کمپین «دست در دست هم برای زندگی» را با هدف تسهیل دسترسی به خدمات تخصصی  و افزایش آگاهی عمومی و اجرا کرد.
🔹
در قالب این کمپین، هزار ویزیت آنلاین رایگان با همراهی بیش از ده متخصص اورولوژی و نورولوژی از طریق پلتفرم دکترتو در اختیار مخاطبان سراسر کشور قرار گرفت.
🔹
توزیع محتوای آموزشی در بیمارستان‌ها، مراکز توانبخشی، درمانگاه‌ها و داروخانه‌ها نیز بخش دیگری از این برنامه بود تا گفت‌وگو درباره این عارضه عادی‌تر و زمینه تشخیص و درمان به‌موقع فراهم شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/669758" target="_blank">📅 14:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669757">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8NBB3RbLDuJyDl3JZQ_yjJctw7i4SAI_TeUaBcx7f4UlCsZkrrZ06pE_vm5trXZ1Jdnk5BKP_a3l109wtjhT7C43_KThTyfJPeWg7hqpO64svDzqxAIi6eBBCU9X8nAiRLQ3br13AklfATJHSXIodYg4G8cRx5sBe8A7LXfeZUJ-FRZmiJgshHHAr_5q4K51IONlSlWjC3nDY73M8u4U9yFQzfXk2btjIA5fCbb6yd5jJgLtbBc6kgsjqI8xkGaOf2kP_TiP3sf0XGdPV1QltMsQAkrWLTrKZFPbKiOzAv0cJ8fc4iMoWcBVzzlhD0ZC3f6ZZQVtxEMlNqBBTmYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی دولت: به‌هوش باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/669757" target="_blank">📅 14:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669756">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRk5_DHrkO2boP_b-zNCvRoc93JUoQ7l06JnFB3EKAkI6v1FTe4o3TrRn6QUD3DhbyCg3pyggpPBIClVxi0KCyhgtfpVe6Wk8rPY7My6mQUY4FTAg98wtrEjhbJtcKqnA0vtldDtKccYzZgDgaguB-oRn9xMuyp8gZ_i106s7-_TY7APbSnWaCL3ZGxItEOihLGvVfioGfuVkwBAxeOYilL_0lFIybchdGe3TrRVnDTgd63iqjlRuvj0hd3dncJSpPQna6QHhSPKy6egorSGZd2uc7U32UxWFs0QV9moHJOgKB6IbLJcNsJY5mHZKzdhm6U4EgpfKS0Gh-jnQQPTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آستانه مصاف هالند و کین/بیشترین گل‌ زده برای باشگاه و تیم ملی از فصل ۲۳-۲۰۲۲ (بازیکنان ۵ لیگ معتبر)
🔹
هری کین، ۲۱۳ گل (۲۴۲ بازی)
🔹
ارلینگ هالند، ۲۰۴ گل (۲۳۱ بازی)
🔹
کیلین امباپه، ۲۰۰ گل (۲۳۶ بازی)
🔹
۵۵ گل کین و ۳۱ گل هالند با ضربه پنالتی زده شده.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/669756" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669755">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مؤثرترین کار شما برای کاهش مصرف برق در تابستان که اجرا می‌کنید چیست؟ (چند گزینه را می‌توانید انتخاب کنید)</h4>
<ul>
<li>✓ تنظیم دمای کولر گازی روی دمای ۲۵ درجه یا استفاده از دور کند کولر آبی</li>
<li>✓ عدم استفاده از وسایل پرمصرف در ساعات اوج بار</li>
<li>✓ خاموش کردن لامپ‌های اضافی و استفاده از نور طبیعی در روز</li>
<li>✓ به دلیل گرمای شدید، امکان صرفه‌جویی چندانی نداریم</li>
</ul>
</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/669755" target="_blank">📅 14:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669754">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYpF_SoTyxOeWgFxMXRtAdFxFA42vwk84FADulcp6KpOdybGg4I5YToc04486h7OK34wXVIVDLjQSR7CM0NQes8LyE8ZC3mMhei0q5FCRdtIFA0Q4fkBXy49HeEZqBEqn3i07RN8b46a5ZVC4Psi5EBwoaT3Ai9X3_4cqX68YqU-3D-Ifz6WhkSKgeoAZTWFRmEE77aG6Ve-vnUpn1lN0Zwc1MpWDGQancAgE6JD2n3micnBuTFyMzhwP1-THy-FLpyFG5V1kQWn6NY5V5g_Bq6C4cNG7EckZoGcSjCczyVo5OmLk3WoICS8rzTLnaSw3MFc_g4aXdydyyAGhLDxxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احساسات شما با بدنتان چه می‌کنند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/669754" target="_blank">📅 14:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669753">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjoqKjP48PA5TviM_Vc5-rQroZFgFjkhjEFaSNTVUfKPIJRVQBqx0MCxVY4qJvIPjvS9LhQiuBLjV0plt3z-EMeYo7nsmGXxE9LVtnLfqU8GB_3gsIO9fcKfeKh6syAEwLTycUbWhkpTEAxqyMGy7vQ0bpMY5RHiDP4GnltPJftCb0eXsWhjWTxik4wTCIRgx3UsYXiHPRAwFSoqiMFY1uKOMj3eINi4wEh5Ymh3_LjiA8RnW95x97wkM_Ef6QUcBrI8sg6JQjXJ6DUdP7UnAmyPj0T6MrutdF6DQMFk52mHXY_uF98sBIzcl4XNwu-mDzCYwvNWIt9XwEfdTuh38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت گوارایتان باد
رهبر مسلمانان جهان:
🔹
ای پدر شهید امّت، نوشیدن شهد شهادت که عمری در آرزوی آن بودید، گوارایتان باد. پوشیدن خلعت شهادت با بدنی که نشان‌ها از مادرتان زهرای اطهر و جدّتان اباعبدالله الحسین و اباالفضل العباس علیهم الصلاة و السّلام دارد، مبارکتان باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/669753" target="_blank">📅 14:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669748">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R006_TtA3lRYJvusN6RHoNPqgSPA1s7bi9CedOwOdqQulSSXKgdDWZaKllV1ogVYnlPGwvjqDo_-vBFqCRORiEGE6VRLhbAwYitBVWQq_fAZ1xYjIjEHKETh3bReaPM4Mxfms_1pf20zaZsZ9B2E3v9pCOvsB3M3DZc_7tP9WKu0kwjDjybVeiZIdfKCT_EgppbMeFakXBUSIpJxg5qUfCct5MFfRBbYTapoXg3v1oBuHIzaHIZkRzXIZ0HBVnjtagFaLxvuC8bnFLW9DTVZnsVhPVNTpHNKu5bZoz8-9aT1JNdEUN2tee2D6CfwnugCP7dNkxVT_8JClDyQGRM49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekq-FPYzxEk6X5Z-vMTYkYNoTBzT9dFvflZEpO3HNMQdvQdfW5keGVJeATrpwyQLK4k44hyD7Y3jKo0PMa4KDszhLTsMV8zGzpVJC8uJCQNdSTi_UsupNYiS-PqqY0IjCdgwOM6-PYNbw6YgNjSAmZ0klvGwPf56iYdYzuza2i37Z61ABjSAhFRYE5Pi47yoBnKqLjJdyRXt1f4YQe6ADuFerdNl4LWOI9dJ7mv6sSrlIc2awb4N4BFo2FBCVS8Z1nS4uSUlr-pXfAZHB-hIWTAlV0Dlv5UJ-GU0BWdIcNMfPCAcRiMJKWg6u_sEz63SekisQkP1jUhhX3WZW7RF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYnoqB42Ee_Mc1w2Dfu7b8T4TzAOFk3fcBRU7W6v-mI5r0EE4YJxJHoeLGRdT830Ru3nGLEuS2ZStEjkK9cESNqpihSPk9y-SHkb5dLkg2VjLTcLBQM6BRYsnA2myWQzi4S6-p2WWkShtfja3fc44pW_pRYVgFsZ8_WOHLkmsqPcmp-9wxg0brtw39D2ynPkd12k3WePwW0Sx9nn-o8J4Y7PjoAnFSZNyjp8l3aP-14rczII-34mA_T0cCHy3uNzM5l7JHSmrx87zjB8XviAQzxidpNxzSEgrD3HeW9ljQkuaG7qabps5tsKSDroyjC4OxgNrMFSctX-05Gcea5ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaVcJV8z4qoiGlkGiaDyy62wbxyAcMq6PIOnS77bokjNd33qqmMWNbz4XwVXTllhEOEwkqAFg4zU189OGXw4Jo_rgGq9a_Hs4PEGK_jOxzRZ1kIlF8_a5P2fqAprTysOUdXcHkrpZKq0I5bZE03crUEbbsCOyG15Iq-DWa0P37iJ_g87kvm-zUMpB_7HukUx29sfYOLEOPXwiBHrI-aa8W-kDoSXAvXST2jkvxjiHjN7NbpDlA4RnymB3V34Hzqre0PhkxQLOrLbn-xSIaCcW9dYQkpF3lityGPmbTqTlx2BtKKL9HG3fbQYJCUJ1ZAw4p0qyIT5dvHO1j7qfSqp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNYbcshELfpvd1J10wnIwPJMZliEBOTaXFBmmfeQInbvEjq1OWaq12cnK7wGPu6nH7r3WW7Nzo6nPt1k-TxCSPHZTqrBAZ90H2BAfvEeNk_5-fw-wPn8Z69O5hU0TjaU8-TCijzuqy28F03usHgA6MGwg1r41D5mcZC4Ay7D3JuJjL1X0UlBYFVWyPmBcsl2jr6q6Zz-ul-wLD8lzCv9XdLmgbgjdS-OFPTqKcg0ZwZ3610ECGwqDC5bFGXfEcXSHrR-vouBCvOn1TZT2HcTWzPfzmN8AIu9KCiZ9uNa8D6NDQlnvaIFYL5LqpBgZw-CvdR3jF55zT_EHscdy_iiyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هیولا برقی مرسدس؛ AMG CLA 45 با ۶۸۰ اسب بخار قدرت معرفی شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669748" target="_blank">📅 14:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gtr6sACpEcGo34p1XtMOlUiR2VroIzBU8SoXndhSp6yvc7sVws7fXQ1PV4Mo6jBr7qmOnZBegjDcAz4jG6LEFSbDlzw7fdbGAi1tFC4xbjMnZUjq_pZeVV8JqElcyxuShcdEPzlRhV1TWCrBF_A7GLUZLxQJd0Bbfy0QxmCnuNK25UjXzMCSMp9lA6zZljS9ImED8efh8gXD8GWcfp0FlfeIz_vVtyxvuBqyJzKMGeMqGeJxq3Iou1e10V1JzPNztVZHfdPdlZyp-Pglx8Wcy8yAWqnN8DswMS9t454yWk5GL9KbWIyb1X7H2guTP1Kvy_S_r2jBW0hHszpDGW5Sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQ7in2DodOwQR2lQ55bgUtJ1bunEVinCGqYYTheg4Tsbr2n_vr2pNpNBpLCbGVdGmCnpaJ1xmmbhRCnYKQBYdmFJQlXafVVI4b2NLqshqXspv0_X8sQTO7FtZeYtVVK8Kn0ieIchqgU68_L02G69tVDdbipKkcf1bkxztK0LS7KPegqA8Sg4cFDi7-sY7EZThnWeRtJPuODvqvlkR_cpir84jKlekpx5i6H0vLcuj2FzPYreb3XB0hdp4tcrI4oQPBCzv4dYKUKCrzYHirelVY-NDUS6sJ6TnjHIzJ9HDo5QwK3IiVH36IQaHPdWcAqyPqBPNELXY2tfCPhDIP5fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PaVc4NFbowYPHLcr544mn5uDpILKPu6mdVDHfnMMyRrI_D7NeRFK9CPnpuB4ZFz_SVXkzRbyB7CtZkJL6eaNg6OT35mffkiabPe1Yv2TO-TfvLKuhBxpR7YR3PhJYAydVmEECrTCpX4hRx8UksDIyP3qt_Gjbz0Xd4lCqjLvhlKdPQqGK3Ya88kjipQlpqPkGRYRKhN3uvQUK_aaHPcQ2P_4A9LbHyLXEv3meHy4wKbRY8hw8X0fIK_a2S3uP6F1JIFNER1KyWO5Xi_dPkLyfQIKGWzBBD8To738r0aIS4fvbnDsG7LMZX1I9Q7349bypjud8XthKXGSqqiIvVHkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtgW8XwAWs_CveAGOUv_8eWusKBkPZYmL9QyDmSszlbkFvFcw4Uj1z2b1LvMfL0-UZAvwx8b9kvGd3xWVsHc7Ezx21JtZncPGkIbxrSHvUopu8Dz-u0u2QW_y1OnFCGJoSosiMXvlW8iTV06ZsW7r01G4VfPvLBJshvw0TKnZ5eciV0G_RKfgaK0w-RVzszfye8MsBqaAglqdxcwTWlG15rxgSxUJtGDE4X7_wsOChFh3O7VyPMnV-H92rl5qFQ4djIkmzIEs7K3iAo5IiUHCkpYwmrb3U3OFSvD6Qz-m0pImly-OX6okl5P4Ko_63wWaVHlmarRs43sQ0NayDAwjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازپیرایی فضای سبز مسیرتشییع با ۲۰۰ هزار انواع گونه گیاهی/ عملیات احیای منظر شهری ادامه دارد
حامد فیض‌الهی، مدیرکل بهبود محیط زیست شهری شهرداری مشهد:
🔹
بلافاصله پس از پایان مراسم تشییع، بازپیرایی فضای سبز مسیرهای منتهی به حرم مطهر و مسیر تشییع آغاز شد و هم‌اکنون بازکاشت حدود ۲۰۰ هزار گونه گیاهی شامل انواع درخت، درختچه، پرچین، گل‌های دائمی و گل‌های فصلی و جمع آوری خاک مازاد داخل باغچه ها و تشتک درختان درحال انجام است.
🔹
از ابتدای ایام برگزاری مراسم، ۵ هزار و ۵۰۰ باغبان درسطح شهر در آماده‌باش کامل قرار داشتند که بیش از یک‌هزار و ۵۰۰ باغبان به‌صورت ۲۴ ساعته در سه شیفت در محدوده مسیرهای تشییع و اطراف حرم مطهر فعالیت کردند.
🔹
قبل از برگزاری مراسم، هرس سبز حدود ۱۵ هزار اصله درخت، جمع‌آوری و جانمایی مجدد حدود ۲۵۰ فلاورباکس، جانمایی ۶ دستگاه مه‌پاش و ... انجام شد.
🔹
۲ هزار و ۳۰۰ چشمه سرویس بهداشتی فضای سبز به‌صورت شبانه‌روزی در اختیار زائران و عزاداران قرار گرفت.
🔹
۱۴ بوستان نیز برای اسکان اضطراری زائران و عزاداران آماده‌سازی شد و ۴ المان تمثال رهبر شهید در خیابان امام رضا(ع) و بالای پل غدیر نصب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/669744" target="_blank">📅 14:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آقای شهید ایران، حسینی بود، حسینی زیست و حسینی شهید شد
🔹
السَّلامُ‌ علیکَ یا ثاراللهِ وَ‌ ابنَ ثاره وَ الوِترَ المَوتور. السَّلامُ‌ علیکَ وَ علی جَدِّکَ وَ اَبیکَ وَ اُمِّکَ وَ اَخیکَ وَ المَعصومینَ مِن وُلدِک. سلام بر امامی که ندای حیات‌بخش قیامش، پژواکی…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/669742" target="_blank">📅 14:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رهبر مسلمانان جهان: آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست
🔹
ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/669741" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
آقای شهید ایران، حسینی بود، حسینی زیست و حسینی شهید شد
🔹
السَّلامُ‌ علیکَ یا ثاراللهِ وَ‌ ابنَ ثاره وَ الوِترَ المَوتور. السَّلامُ‌ علیکَ وَ علی جَدِّکَ وَ اَبیکَ وَ اُمِّکَ وَ اَخیکَ وَ المَعصومینَ مِن وُلدِک.
سلام بر امامی که ندای حیات‌بخش قیامش، پژواکی عظیم و پرطنین از بعثت نبوی را تا اعماق دوردست تاریخ امتداد بخشید و از اثر آن انقلاب اسلامی ایران پدید آمد. انقلابی که از اساس حسینی بود و با شعار و مرام حسین ساخته شد و بالید. آقای شهید ایران هم با همین مرام رشد کرد. او حسینی بود، حسینی اندیشید، حسینی حرکت کرد، حسینی جهاد و مقاومت نمود، حسینی زیست، و حسینی خون خود را در راه مکتب حسین تقدیم کرد و به شهادت رسید.
🔹
بخشی از پیام رهبر معظّم انقلاب به‌مناسبت تشییع و تدفین آقای شهید ایران |  ۱۸/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/669740" target="_blank">📅 14:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
  <div class="tg-doc-extra">150.4 KB</div>
</div>
<a href="https://t.me/akhbarefori/669739" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر آزادیخواهان جهان به‌مناسبت تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/669739" target="_blank">📅 14:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4MFggWEp5xpTGaSG_l8PI9YzlZMSLn3c282DYaXgqZXwdO2NK2E0dMOmqM1CWwOZ7mVqztCGMRn9MewLwDT1_IGaD4Crwbl7A3UcsFtXPdm1yUoqjxH_oRDcGNCjO8CGGGNCLFQF6UEedbNZYWZ-sQeT7UAFgBJZzPN2Ta0jmMhYHKDqKgRiCFKqjmuHks0xpNbtZWYQCHUnA9kDqBVrO3vr3vc0AxQoCl-wkMTC-uFdxXpdN8Qoy_oH__sCPLO_-hmzau1eT3kgeWhlumkJaUmeTFuxhBhn7Fv5a94BC1N07Qnb8r1v4EBjNT3JQ431DzCAiQKp2ey7TSiOZUREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشکر رهبر آزاده‌گان جهان از حضور تاریخی ده‌ها میلیونی در ایران و عراق
🔹
جا دارد به همین مناسبت از حضور ده‌ها میلیونی، اعجاب‌برانگیز، دشمن‌شکن و تاریخی مردم در شهرها و روستاهای ایران و عراق خصوصاً تهران، قم، نجف، کربلا، و مشهد صمیمانه قدردانی کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/669738" target="_blank">📅 14:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رهبر مسلمانان جهان: انتقام آقای شهید ایران، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد
🔹
این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد
🔹
جا دارد از حضور ده‌ها میلیونی، اعجاب‌برانگیز، دشمن‌شکن و تاریخی مردم در شهرها و روستاهای ایران و عراق خصوصاً تهران، قم، نجف، کربلا، و مشهد صمیمانه قدردانی کنم.
🔹
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همۀ شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/669737" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01a1eb632.mp4?token=OMQtZery07uq_0oKyBQDVWsGvFV2BbM6XOwfaz7TmRpts_-qDBKW0GTfnS_2hyVeUZq7nrwZ2iXgphumZo_zzAHfOmm8FY7-MmvoaTfwRMaec8M-6rhNBj-vE20jEtLO4j3Ew5bMnL9vrbGq5bAEJTWiZw2sbRPrh2qUKAVmfgxOVoD-0qgKcEQvoo1FmWHTDSleZ8nvzc5s5kkxjnzvibiFToSnwCnWWj84xckrMHklq--y5ukRRYeZgIggSjHUGdC99Ka-TTR76Z5HWkfdhpNqOQDB0rN8F2rQVP484PU3HW0a1EpXGlewuwPACnsJ5T2VnfNmoTTSKkMbLkO0UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01a1eb632.mp4?token=OMQtZery07uq_0oKyBQDVWsGvFV2BbM6XOwfaz7TmRpts_-qDBKW0GTfnS_2hyVeUZq7nrwZ2iXgphumZo_zzAHfOmm8FY7-MmvoaTfwRMaec8M-6rhNBj-vE20jEtLO4j3Ew5bMnL9vrbGq5bAEJTWiZw2sbRPrh2qUKAVmfgxOVoD-0qgKcEQvoo1FmWHTDSleZ8nvzc5s5kkxjnzvibiFToSnwCnWWj84xckrMHklq--y5ukRRYeZgIggSjHUGdC99Ka-TTR76Z5HWkfdhpNqOQDB0rN8F2rQVP484PU3HW0a1EpXGlewuwPACnsJ5T2VnfNmoTTSKkMbLkO0UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد شهروندان آمریکایی از جنگ ترامپ علیه ایران: حتی یک احمق هم می‌دانست نباید وارد این نبرد شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/669735" target="_blank">📅 14:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNIpnUHwSaqD_uWgqUXe8399_mi6phaPTqvn9ZKldbCJKdafT2iEB3l_bQkKzKkDiLMC6xZRTHVPJGFMlPWQHV1G5ezcSCYav8OGX-w5BTVhbK76ksxNuagtWrX6SOnodfVs9GpSFdWw0IMxG1okWH9j9cI5NF-ee1pBPkdJCa6Jd61fIjm1iIDvTDNNWfaDDz-PO8XXfNa_lUUBPEUwnBIhNSl1kt9IAb8TFSwkF7mSGYDP-nOzIdvAlyRvAyJSbSgypoQHXvICV0TJr1lzPAVQQg8DGM60ftrwoqjO21tcAiS-tp4UrYXuCg-tM98Whft5RkeMhyu7TE4QDDc8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دود مشاهده شده در شمال تهران مربوط به حریق در فضای سبز اوین است
سخنگوی سازمان آتش‌نشانی تهران:
🔹
در این روزهای گرم سال، روزانه در نقاط مختلف تهران شاهد ۴ الی ۵ مورد حریق در فضای سبز هستیم./تسنیم
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/669734" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be5f3fa344.mp4?token=KUGEhTD-fwRdbeB6c8xIB2BA6sK4tPxN14iuhQUHtSCif_8ny2UJ2TRkafz02UPdRq4qNT7uYL4r1huXGT5LxtGAAhvJhLghHuq3XdFl8C3y6J1hfo9rkRrPvFOjuAv9_yoclCuJeVUTWMihGLNTiBTKIIIQ2MLGM1CJDk81rYO-gsptu8mLR0-24LyGleNg_zDL371QADYl-1zQqIfckmKW6Akj1m-O9519f3SZif9sHZQixHFAT2ARUADZfbF9PT8KTPgIRNej_3enFrf5R_gfO-XV4K14tJ3hwa-2BVCdmH0Vb3ya2ITTteYYjDFqf-NgebtTwRMcVU8uNpZlzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be5f3fa344.mp4?token=KUGEhTD-fwRdbeB6c8xIB2BA6sK4tPxN14iuhQUHtSCif_8ny2UJ2TRkafz02UPdRq4qNT7uYL4r1huXGT5LxtGAAhvJhLghHuq3XdFl8C3y6J1hfo9rkRrPvFOjuAv9_yoclCuJeVUTWMihGLNTiBTKIIIQ2MLGM1CJDk81rYO-gsptu8mLR0-24LyGleNg_zDL371QADYl-1zQqIfckmKW6Akj1m-O9519f3SZif9sHZQixHFAT2ARUADZfbF9PT8KTPgIRNej_3enFrf5R_gfO-XV4K14tJ3hwa-2BVCdmH0Vb3ya2ITTteYYjDFqf-NgebtTwRMcVU8uNpZlzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاملان نزاع خونین طرشت دستگیر شدند
🔹
مرکز اطلاع‌رسانی فرماندهی انتظامی تهران بزرگ از دستگیری تمامی عاملان نزاع دسته‌ جمعی در محله طرشت خبر داد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/669733" target="_blank">📅 13:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa977a798.mp4?token=NLN6t272fu3a_D_-004Ke8DChFJkgbdReJjj1kKKGTpH1S6CF62Z4KnqOyqGIEbDvrKevV9PBoB5zhDpSPkztdMeA6QwVObavASrDgj08ocHq5Rpm9NcUJFEzI83VVlfqS2g7NhCrJORr5rLI_akx8Dj7E93SebdGTRZintBBNvEGmrAg2N3j3czDqg5FI9orfe5zUrjl8Vp2c2_M00sekUrpHA7jS8oOCuLKfPfsHUrGKvAN8Sn76wnW60Dh28omHSCJhhncg2m_vNmeszcHj6dN_TXT5bfHNHQ67g63g8R0vK7_AtOCtPwS0rcjY_8O_JsHFQqez99SXMfQ8uNvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa977a798.mp4?token=NLN6t272fu3a_D_-004Ke8DChFJkgbdReJjj1kKKGTpH1S6CF62Z4KnqOyqGIEbDvrKevV9PBoB5zhDpSPkztdMeA6QwVObavASrDgj08ocHq5Rpm9NcUJFEzI83VVlfqS2g7NhCrJORr5rLI_akx8Dj7E93SebdGTRZintBBNvEGmrAg2N3j3czDqg5FI9orfe5zUrjl8Vp2c2_M00sekUrpHA7jS8oOCuLKfPfsHUrGKvAN8Sn76wnW60Dh28omHSCJhhncg2m_vNmeszcHj6dN_TXT5bfHNHQ67g63g8R0vK7_AtOCtPwS0rcjY_8O_JsHFQqez99SXMfQ8uNvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی ارتش اسرائیل به جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/669732" target="_blank">📅 13:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669724">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
استقبال بدر البوسعیدی از سید عباس عراقچی وزیر امور خارجه کشورمان در بدو ورود به محل وزارت امور خارجه عمان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/669724" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669723">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
احتمال برگزاری صحن علنی مجلس در سه‌شنبه
عضو کمیسیون فرهنگی مجلس شورای اسلامی:
🔹
تاکنون تاریخ دقیقی برای برگزاری صحن علنی مجلس شورای اسلامی اعلام نشده است؛ هرچند احتمال برگزاری آن در روز سه‌شنبه مطرح است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669723" target="_blank">📅 13:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669722">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSvuDFSJk024xCNHZijmj8YGbSx3IVRYAAMUHSyI06KA4Np9aPEoig9fURZJ5DrmVeekAIBMhFpeZ1XAOETr4xIyeecAg4Frrj1T2fCIj1bU2FW5DpT4eg_5FoAQssryBnJ5I0vCNrtrUUiXLMG-5qhdol4Au8CxYuaTDnD0-resmKEgxBFacVEDK8hHADLuwJD7DPOxhTsyG_NlRaWGALp4Ikorles2Fz7mMO2B3pwsNB60dOTVcizmmQWbXmWdz_v25Jmk_TVQhFWIJXGa4q2Q4LRrgZoZb4kOLdMPBkNyZ0FyBzUX758utQE3ZTY4tF0rNDRkgpw1MiaM4Snpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تماشای طلوع و غروب خورشید چه تأثیری بر سلامت ما می‌گذارد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669722" target="_blank">📅 13:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669721">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منبع آگاه: مذاکره تا عقب‌نشینی آمریکا از مواضعش منتفی است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی:
🔹
گزارش‌های منتشرشده در برخی رسانه‌های نزدیک به رژیم صهیونیستی درباره درخواست ایران برای مذاکره با آمریکا کذب است.
🔹
جمهوری اسلامی ایران هیچ درخواستی برای مذاکره با آمریکا ارائه نکرده و هیچ مذاکره‌ای نیز تا زمانی که طرف آمریکایی از مواضع خود عقب‌نشینی نکند، انجام نخواهد شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/669721" target="_blank">📅 13:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669720">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93535b299.mp4?token=re9IINdnX0eGWF_sk0oS-QB8TGYq25_qFO3Yf7X2WFTf7HEi2CREdTcnle6qIBPpVRyehS3MCeFuNovJtfYAFgd5DOoSjUl9Pj7UQnqP0MZm0ZM0RTINYH5xTibbZQ-asMq5Q8tQxDNL98jIWPQQb1vgAFF1-xc4HNC729QAihRE_JiWIYwMABEBzXugfPBe4Kz0D5YWAeLvHO34GKekSFLbchdeNIP8y0FfRzGJIbASwqvV-MguNQR3YXW_G67QyqXqsZ9xqWxz8CjV4uSdjjlJkz4qBtB_Forj6SVd7dfqmOBo7TEiLYpCTKtSFwTq03HZehkoNGNPFYvWTBZy5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93535b299.mp4?token=re9IINdnX0eGWF_sk0oS-QB8TGYq25_qFO3Yf7X2WFTf7HEi2CREdTcnle6qIBPpVRyehS3MCeFuNovJtfYAFgd5DOoSjUl9Pj7UQnqP0MZm0ZM0RTINYH5xTibbZQ-asMq5Q8tQxDNL98jIWPQQb1vgAFF1-xc4HNC729QAihRE_JiWIYwMABEBzXugfPBe4Kz0D5YWAeLvHO34GKekSFLbchdeNIP8y0FfRzGJIbASwqvV-MguNQR3YXW_G67QyqXqsZ9xqWxz8CjV4uSdjjlJkz4qBtB_Forj6SVd7dfqmOBo7TEiLYpCTKtSFwTq03HZehkoNGNPFYvWTBZy5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیزر چک پاک کن، پاک میکنی مبلغ دلخواه مینویسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/669720" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669719">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079f2e378e.mp4?token=PArJb4a7VFa-A2grQQgipqfmg2lV0QbEWbiC-BtaXWpPZa5lLTEM1QM-OPD8KLUDP7Q-GiJpou1STZL1bnoxIBiod-Ud5nCZSah0Ts3Jw3GAiZ-tFqfRIxI3EoGbfc4sLGYXKzXSPTuVe3uzi6bElb7xu4vSwVsSQ9cyqig8UwC7CtZTjgjL-T00I0b3RgkBc82O7W_Wnx7XKhyl6QiB0IJQ5eaWZPJlZEEK-hycsL2lCh1aCVbUv6_dRtNmV85sdVrTbu4Wjc7gUhifxvh0eUMJIPl3uOLQpMFliKyQHF_HtlxBPD308gLtBb4ytCR0soVgg5NEwCExlWV-_jRX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079f2e378e.mp4?token=PArJb4a7VFa-A2grQQgipqfmg2lV0QbEWbiC-BtaXWpPZa5lLTEM1QM-OPD8KLUDP7Q-GiJpou1STZL1bnoxIBiod-Ud5nCZSah0Ts3Jw3GAiZ-tFqfRIxI3EoGbfc4sLGYXKzXSPTuVe3uzi6bElb7xu4vSwVsSQ9cyqig8UwC7CtZTjgjL-T00I0b3RgkBc82O7W_Wnx7XKhyl6QiB0IJQ5eaWZPJlZEEK-hycsL2lCh1aCVbUv6_dRtNmV85sdVrTbu4Wjc7gUhifxvh0eUMJIPl3uOLQpMFliKyQHF_HtlxBPD308gLtBb4ytCR0soVgg5NEwCExlWV-_jRX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
سعید لیلاز: ۱۳۰ میلیارد دلار از منابع مربوط به واردات، از کشور خارج شده و هرگز بازنگشته؛ این یک آمار رسمی است. شما نمی‌دانید من درباره چه چیزی صحبت می‌کنم. در بسیاری از سازمان‌های دولتی، ابعاد این فساد و سوءمدیریت حتی از آنچه تصور می‌شود، گسترده‌تر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/669719" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4DERcnbdXTiP8cgG9thNTIg6MebGz2ymPy0vEJcf7m_65n3_72w5GKGd2ryHCUIMT0rJ4ErkgtgPMb186mvEAQxO4R3_rWlASFnlZPiX20qGf6F78nGXaXa7KQ9qLUUsSuLKY-QsGXovPripA3OtY4s4Eazpu7NZRi0FHMOITouoVPq-sRSSmL8QY83bd9kfx7M-Q_BBjc55y6y5RFTpoNLDADx1E0VdpSmobtk758FQoO3BXussZeav5FegC0uVpSEOCtg-uaCpOEEAypZlCbuN-BPnfglN5AnhJQTNP_pt3dkCDa3n5nwfnfKcWppJf7Yhy3yiRis3Olx3dtqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این پست را برای همسرانتان بفرستید/کلکسیون کیف‌های ساخته شده از طلای ۱۸ عیار فروشگاه سلفریج لندن
🔹
کیف‌هایی که با پول هر کدام از آنها میتوانید یک BMW آخرین مدل بخرید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/669717" target="_blank">📅 13:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a297e6b87.mp4?token=m7GxMxq9wHF4ZvwRctw1GC4apYJmJF23DnRYezi8zx4P8LfkQ1zs48NgSROQXT2g21GjxLMzp3SJ1phaTCrMPCBwCLwrOYLaiKhqC7e7reA9F6c-DJAgU0hlvReS9GOJTeKjdOaG4NJ09_4FXK39eb7Hu6_BzJPNdWyQYi5KGG5gnAmUU675va8nPlIvJDmH0izcuAs6XKHgaqdUM3rYIi3TP6uqioPxTpB3MzdLlyGFYlasDs3L58wuaELPQng5QKzaia0_NhEMQ2k6zoYzPD3g5LPv48gX1LO6dUSjarS0euZMWtS_vnvHUTqB8Cfpup9OEQZQ-x6fXk28oi4W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a297e6b87.mp4?token=m7GxMxq9wHF4ZvwRctw1GC4apYJmJF23DnRYezi8zx4P8LfkQ1zs48NgSROQXT2g21GjxLMzp3SJ1phaTCrMPCBwCLwrOYLaiKhqC7e7reA9F6c-DJAgU0hlvReS9GOJTeKjdOaG4NJ09_4FXK39eb7Hu6_BzJPNdWyQYi5KGG5gnAmUU675va8nPlIvJDmH0izcuAs6XKHgaqdUM3rYIi3TP6uqioPxTpB3MzdLlyGFYlasDs3L58wuaELPQng5QKzaia0_NhEMQ2k6zoYzPD3g5LPv48gX1LO6dUSjarS0euZMWtS_vnvHUTqB8Cfpup9OEQZQ-x6fXk28oi4W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مقام روس به احتمال استفاده از سلاح هسته‌ای
دیمیتری پسکوف، سخنگوی کرملین:
🔹
اگر چیزی موجودیت روسیه را تهدید کند، از سلاح‌های هسته‌ای استفاده خواهد شد.
🔹
در غیر این صورت، از آنها استفاده نخواهد شد. هر چیز دیگری غیر از این، گمانه‌زنی محض است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/669716" target="_blank">📅 13:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669715">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای مقام آمریکایی: تحویل اورانیوم، شرط توافق با ایران است
.
🔹
فرودگاه بین‌المللی کیش فعال است.
🔹
چین صادرات هلیوم را که گاز حیاتی برای تولید تراشه است را ممنوع کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/669715" target="_blank">📅 13:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669714">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhSGCnyh0NGaxCR3rp-6QR9Vp0z9GOT_Y7zPLGyJXalmt22xU5KFgObRfdgdmB0HCbv55qE9nCnlr_4cLL5bY7Jqucph3jwGtJ2iNFN2Qwt0SsRLSxEEeIWDkoHXwDGF_Ouosjsl6ZFgvyDA1ifJB5Sic5IBJxdefbwAJEo9sZjZpEvdaThWBXibmAr2-i--D88_CD0hukmjrsZSieUPuSL4F7Q--rw3h5t34paydbVV9jP8VdvGm717Edxp2_MaJwZd5tqDgICVFTQ_gpZRZ4MkD9VSFWZQxnkzJOu5f7qVx3O40FaUwtqg1Y2zmjUp5dRj2Mx1DWAHuosv-G_23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پهپاد شاهد ایران سر از آمریکا درآورد!
🔹
گروه «اتحاد علیه ایران هسته‌ای» (UANI) برای اولین بار در ایالت فلوریدا، یک پهپاد شاهد-۱۳۶ ایرانی را به نمایش گذاشت.
🔹
سخنرانان حاضر در این نماش ادعا کردند که شاهد-۱۳۶ ساخت ایران به سلاحی فراگیر برای ترور جمعی و تخریب بی‌هدف تبدیل شده است و تهدیدی فزاینده نه تنها برای نیروهای آمریکایی در خارج از کشور، بلکه برای سرزمین آمریکا نیز محسوب می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/669714" target="_blank">📅 13:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تا ساعتی دیگر؛ پیام مهم حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت تشییع و تدفین آقای شهید ایران منتشر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/669713" target="_blank">📅 12:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d50d210e0.mp4?token=hbt_bzuYX9DIgLq9JoFd5HaYv_c4aQds6BrNoJMtN5454X5qWgZFhos4OLmbs_nQO_B3e6N2FPyjetbZvMALwoWBiLQAx_p-STmyvEuUI54pb57fpvtaIMJXLeqQFF_IIHeVx-mVTDegcnQZ8_Bh4hFTQUR57qhCUWA8axr2lXqjeP7layORjbhH7FzVPN0JwZdc_LvBhk1AIfp_ldfOuuQQoIH0s89e1FZRWG1TrcB6ykpH9fXkB42ef1gWtcAPLuVR7VsSM0f53-b1OswvvR9RRJkakKO6zHwv4GVOTtfhNWd3XaeinjnEG819o1V0Zq9wS-koZHk9LjvNO1IFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d50d210e0.mp4?token=hbt_bzuYX9DIgLq9JoFd5HaYv_c4aQds6BrNoJMtN5454X5qWgZFhos4OLmbs_nQO_B3e6N2FPyjetbZvMALwoWBiLQAx_p-STmyvEuUI54pb57fpvtaIMJXLeqQFF_IIHeVx-mVTDegcnQZ8_Bh4hFTQUR57qhCUWA8axr2lXqjeP7layORjbhH7FzVPN0JwZdc_LvBhk1AIfp_ldfOuuQQoIH0s89e1FZRWG1TrcB6ykpH9fXkB42ef1gWtcAPLuVR7VsSM0f53-b1OswvvR9RRJkakKO6zHwv4GVOTtfhNWd3XaeinjnEG819o1V0Zq9wS-koZHk9LjvNO1IFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار آزمون: پیشنهاد ۵ میلیون دلاری را بیخیال شدم تا روزی اسطوره ایران شوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/669712" target="_blank">📅 12:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iscw_AdRHpBxy0xMCSpM4ajWQ3CZq_m6YXt-raw-IIqqqqgcUkVlyz2n1bVMacrwcego1z7JG8fwoNO6LLudbf6FiBy81s7c7bOeWMtq0xv9ahyII6nue4wgzBO3bpBl1bi0nftkNS2awcX-Mf8KKefA3F78LKi6pua8J174Q9KwJaOffmVASeJamW-F1DbKxxfvh7v3KR90YYJxIunOgVVHZqRTLxiyaLkFvz87MzdZHQDs_mTNHVjkRsILWtFwNAAIrQ309LKUVvKF8bmn7f44plUexYufqpKdgFBSNMUtkDPhUyateoqzcdvFsy1LGL8aotXpfSmYJPSshxF18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏨
هتل پنج ستاره نگین مصلی مشهد
با افتخار اعلام می کنیم هتل پنج ستاره نگین مصلی برای رزرو اتاق شرایط ویژه در نظر گرفته است،برای اطلاعات بیشتر و رزرو اتاق با ما در ارتباط باشید                                                                                                                                                                                                                                                                                                   *بوفه صبحانه با بیش از ۱۰۰ آیتم غذایی
* سرویس ۲۴ ساعته رایگان  به حرم مطهر رضوی به صورت رفت و برگشت
*پارکینگ مسقف
*مجموعه آبی رایگان
*استقبال و بدرقه فرودگاهی و راه آهن
📝
مشهد خیابان نواب صفوی نبش مصلی ۳
شماره تماس جهت رزرو :
📞
05132300000
📱
09309902626</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/669711" target="_blank">📅 12:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3KqZS404B2xRQM1wPE5RbpNH8PqCqk_w8KEHsi3y42teT0L6poAa_V0mJEYcyhE8agRJV4N4J7teq5825MR-K8EIFf_OGIk93DkhAclSw5FLflwAQ18bUMQcWe-rhKm5RcE_rjTmiBS1hwLfaoxARuDvVw23TfpvoHGdTPrcfdI7fOACZek_X8JNMqCt5Fu5u-a3uxVM7D2f4b3qhJvAMqQ8lPK07hMqY6LWUNgCQFMJH7NXPlkGX14ansUK9QNnKO4geQFebBhNE0pvTWeVBXlk2hFLESPh0CcqgM1tQ0pYats1CohyoKDslUP8SGotf8NaovrMtcMnTA8J-tctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع تیراندازی در مشهد تائید شد/ دو نفر کشته شدند
🔹
معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان مشهد و کشته شدن ۲ نفر را تایید کرد و از ارائه جزییات بیشتر در این باره خودداری و تاکید کرد: «هنوز علت حادثه و هویت کشته شدگان مشخص…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/669710" target="_blank">📅 12:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0cfb6436.mp4?token=B6dOxhc8CkvoEAuIJns2YCqfyiR38SlgoeRETOJaH9WP7t3rs4H2Uza_vFxt1Qk-IA7U1RmZAw2jWeQGdlqTPDelEtWN8NzZXTy7GO_SIKFE2dGMF2TXPSY3g2JT0d4mdD5FHFM-KgiXUzMXnkWfuMp3W9ylr_soIBSwWUC6kwNOJPB1iYcS7xk4TiXnr3oN6r1AKZ1DaFUKYslirR7Kb1MZT1m878AauL_PGaiKtSYGUn6GQWdAqVoMaidvVL7F3gsUDEbFAObA6OraVIyrmKHHI-706Awc9nKBCydsn5-1ivQIrjQ6ZtpqFyEz9JaOXQEcOrlJEldsOeGauOwgNmqSIg48pw7YZzvyPCQ1mra8H_cGcM-3gvsYUB7ANYgWJ7mEGu7LY7hk6RCL9DjgoJSKiMiXKaRt4DViruNa9c1firS8d5tTzKr4DEjvYl09Gz3UvoHWNV-kLZ9t43ENyTxymM1PNFJbWroa3v3Z_mpbYe6CRaK4UdjEesf-YL7c-Cgut3fZW0dgBrxm0oP392ZuWgHKu4VhPGdkkTNaJw8MlYZLwTq8cgVVhORbZmsOHcbWRpXzjsM4U4Uiz843cCkTxB1IgkH4QJER9WDiOyA-K_uzqDKDhLlkf63wilhIvnmdmzXYzJuxUxAOr2LfzKPYeai2vbvnVYBsOub0uzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0cfb6436.mp4?token=B6dOxhc8CkvoEAuIJns2YCqfyiR38SlgoeRETOJaH9WP7t3rs4H2Uza_vFxt1Qk-IA7U1RmZAw2jWeQGdlqTPDelEtWN8NzZXTy7GO_SIKFE2dGMF2TXPSY3g2JT0d4mdD5FHFM-KgiXUzMXnkWfuMp3W9ylr_soIBSwWUC6kwNOJPB1iYcS7xk4TiXnr3oN6r1AKZ1DaFUKYslirR7Kb1MZT1m878AauL_PGaiKtSYGUn6GQWdAqVoMaidvVL7F3gsUDEbFAObA6OraVIyrmKHHI-706Awc9nKBCydsn5-1ivQIrjQ6ZtpqFyEz9JaOXQEcOrlJEldsOeGauOwgNmqSIg48pw7YZzvyPCQ1mra8H_cGcM-3gvsYUB7ANYgWJ7mEGu7LY7hk6RCL9DjgoJSKiMiXKaRt4DViruNa9c1firS8d5tTzKr4DEjvYl09Gz3UvoHWNV-kLZ9t43ENyTxymM1PNFJbWroa3v3Z_mpbYe6CRaK4UdjEesf-YL7c-Cgut3fZW0dgBrxm0oP392ZuWgHKu4VhPGdkkTNaJw8MlYZLwTq8cgVVhORbZmsOHcbWRpXzjsM4U4Uiz843cCkTxB1IgkH4QJER9WDiOyA-K_uzqDKDhLlkf63wilhIvnmdmzXYzJuxUxAOr2LfzKPYeai2vbvnVYBsOub0uzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ صف طولانی زائران حرم رضوی برای حضور بر مزار مطهر «رهبر شهید» در رواق دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/669709" target="_blank">📅 12:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm-8pqqld4e3fOKoCvobrnBHKedd7JHi61gy1reIbsS7ihJeEfmr8wx-Gt572omdZrfO2EuljwXrmFQixElmrrOuzt4Wcub9FcqI1exAvbAX-eG_By6P1UOJfQiFnobddyUXknb8LRQTw-Hw95esaEc5jAViAUvylkFUfhzhdgI4CHR_4_uqq0gMXql1PKZXS_aAx-PcYQGbGPckO5aLzaqB87-do5mFX3sfB4G84xwtCHIalj6rKyPwUK_vfw5iFfhcW15oFLLl5pk4uCiMbQ2N0lCCF3vg4S3H8LrJffPx2KYvZUJoNi7HvtkjsVP_0gBiVM3juKdLR2h48LAlGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش ۱۰۴ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با ریزش ۱۰۴ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۱۸۲ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/669708" target="_blank">📅 12:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تغییر هواپیمای ترامپ از ترس تهدیدات ایران  روزنامه نیویورک‌تایمز:
🔹
سرویس اطلاعاتی آمریکا به ترامپ توصیه کرده در بازگشت از ترکیه، به دلیل ملاحظات امنیتی و احتمال تهدیدات ایران، از هواپیمای جدید (اهدایی قطر) استفاده نکند.
🔹
طبق این گزارش، هواپیمای جدید فاقد…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/669707" target="_blank">📅 12:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
بازار داروی ایران به رکورد فروش ۵ میلیارد دلاری رسید
🔹
بازار داروی کشور در سال ۱۴۰۴ با ثبت ارزش ۵ میلیارد دلاری، به بالاترین سطح خود رسید.
🔹
رشد فروش مقداری، همراه با افزایش میانگین نرخ داروها از ۳۳ درصد در سال ۱۴۰۳ به ۷۳ درصد در سال ۱۴۰۴ درآمد شرکت‌ها را تقویت کرد.
🔹
حاشیه سود صنعت دارو نیز از ۲۵ درصد به ۳۸ درصد در زمستان ۱۴۰۴ رسید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/669706" target="_blank">📅 12:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
هشدار سازمان سنجش به داوطلبان آزمون ارشد
🔹
سازمان سنجش آموزش کشور با تأکید بر ضرورت بررسی و اصلاح معدل درج‌شده در کارت شرکت در آزمون کارشناسی ارشد ۱۴۰۵ اعلام کرد که هرگونه مغایرت بین معدل ثبت‌شده و معدل واقعی، حتی در حد چند صدم نمره، می‌تواند به لغو قبولی نهایی داوطلب منجر شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669705" target="_blank">📅 12:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669703">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf2db7b6b.mp4?token=J3ksW7TT6BxnxQ0kaD6ZjYpwt7YNPwuDzG8ubtimhn40f2a6mjR86n5QNN__1CZw8_Za7L6gvmcRwUww-VXPy170386MbNByXLFFokLHyyxOPvLaLJCPv0xp5LKyXRVvcIvvWF3hyXb8ZsD7h8_qTzZcpcW43-xKMA3J2taJgxXRXdGjqsZ1nWFfksT-Syt-ZQWfToUiBw30ck-51K_78yVdaY0qX5Um7ayl9-n01bxDaCvrOwesstGU0-I5TUkW8MIT2QHQCYKOUrxHrGzQ6BXtf3sMm2V4mLBHfNI6TVwbWLQi_7R8Fofma0PAQZeRSxfka5fcA2GIJIcqaWSotg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf2db7b6b.mp4?token=J3ksW7TT6BxnxQ0kaD6ZjYpwt7YNPwuDzG8ubtimhn40f2a6mjR86n5QNN__1CZw8_Za7L6gvmcRwUww-VXPy170386MbNByXLFFokLHyyxOPvLaLJCPv0xp5LKyXRVvcIvvWF3hyXb8ZsD7h8_qTzZcpcW43-xKMA3J2taJgxXRXdGjqsZ1nWFfksT-Syt-ZQWfToUiBw30ck-51K_78yVdaY0qX5Um7ayl9-n01bxDaCvrOwesstGU0-I5TUkW8MIT2QHQCYKOUrxHrGzQ6BXtf3sMm2V4mLBHfNI6TVwbWLQi_7R8Fofma0PAQZeRSxfka5fcA2GIJIcqaWSotg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبشار کایتور یکی از شگفت‌انگیزترین آبشارهای جهان است که در پارک ملی کایتور در کشور گویان قرار دارد
🔹
این آبشار با ارتفاعی حدود ۲۲۶ متر (ارتفاع سقوط آزاد) و ارتفاع کلی حدود ۲۵۱ متر، یکی از بلندترین آبشارهای تک‌مرحله‌ای دنیا به شمار می‌رود.
🔹
ویژگی منحصربه‌فرد کایتور، ترکیب ارتفاع بسیار زیاد و حجم عظیم آب است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669703" target="_blank">📅 12:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669702">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73630787ad.mp4?token=spq3HlYQ0bdJ7ol0DJqQXhc2YJ3Q7eqZzibiq8PggPlIxeIki146z_GjltyzwkTmeStTt2TkZ_sbKQH3Gs_PJD1S_ybri_e_J-upwJwJIZhrBuogpOBrui7_XTbMeiN5hW2jDBQgNoRd8wANMa1xT_Ti4jxs-Dq7KoCkyyHrCfkB2qOrY4BZ7GACjHlxvFWiKPUD1oN-NDkQJhW6dpKa9B_d7RS_u0R6MdabRNdK6Ow6nPlDkc8IGkwFtFrs77gKxiCzyL59KhsfgKtDFU5ZOapYX2ZJrIbbFERpGlCQ0-nXHRMJSfe6V_2Ywsnwzn_HJzT30pibISfwg1Q0ARFrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73630787ad.mp4?token=spq3HlYQ0bdJ7ol0DJqQXhc2YJ3Q7eqZzibiq8PggPlIxeIki146z_GjltyzwkTmeStTt2TkZ_sbKQH3Gs_PJD1S_ybri_e_J-upwJwJIZhrBuogpOBrui7_XTbMeiN5hW2jDBQgNoRd8wANMa1xT_Ti4jxs-Dq7KoCkyyHrCfkB2qOrY4BZ7GACjHlxvFWiKPUD1oN-NDkQJhW6dpKa9B_d7RS_u0R6MdabRNdK6Ow6nPlDkc8IGkwFtFrs77gKxiCzyL59KhsfgKtDFU5ZOapYX2ZJrIbbFERpGlCQ0-nXHRMJSfe6V_2Ywsnwzn_HJzT30pibISfwg1Q0ARFrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوانین عجیب دشان برای تیم ملی فرانسه از آزمایش ادرار روزانه تا ساعت‌های مخصوص خواب
🇫🇷
⚽️
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/669702" target="_blank">📅 12:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669700">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLxjERns39sIR2OGjJk_qEwKNKFJAAWRDJCX_cA9I637YYDl5bc9o_bPMKk1QQkN8py5By5t0f_fB_Js6sfLmryJbTAMFF8BxjgEKky4zXZyJjB4AakxUuGyvL9-2y_T8924h_RR_Vwh_9XoATgkrKMQaNh-d7ELGpg3wJyt1cDIjVuvhojF15qCoXaxGJ9XCoeNeC_UNeDczGdLx0IlBXJRfHkAFMSx_2e85d2nclAF5x9a1LeecdwTfYRa-k81LdZUBFdRUfOKmIpdjqEiyOjxlyz-1wqw6TZCtkUe_Jmrt2woEzuvfouQ_6szn4C35hfILfRliAf7663uze89dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عبور از روزهای داغ پیش‌رو فقط با همدلی مردم در مدیریت مصرف برق ممکن است
🔻
مدیرعامل شرکت توانیر با اشاره به پیش‌بینی افزایش دما در بخش گسترده‌ای از کشور طی روزهای آینده، از همه مشترکان خانگی، اداری، تجاری و صنعتی خواست با مدیریت مصرف برق، صنعت برق را در حفظ پایداری شبکه همراهی کنند و تأکید کرد: برق حق همه مردم است و با مشارکت همگانی می‌توان این نعمت را به‌صورت پایدار در اختیار همه هموطنان قرار داد.
#مدیریت_مصرف_برق
#پویش_۲۵درجه_قرار_همدلی
✅️
جزییات بیشتر
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/669700" target="_blank">📅 12:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669699">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTWe3drgL1rZTbfBTJuBCR_ShPOUh9SHplxxbsLsB77YAQTGPfH8O4zcPMu9XXieqAmscKgfOYGxAP1hMGkf3YzHXaruEkxnGE3rB3KLTqw9sG1N9RQe1EBXOeN-5xDGwWoJb6f9zfRnitigM3CQeZA7mzoSHCNVTS6NsxMzB6SuFbf4FRSi-sWO5wbD1x0qP-lL9UctmfvKwZhvYmFCE-9hjKgo-qIXmdZBNdSQYFpPvkcwC3Jq1NQSKSRAOmtci4rJvO9iHPI7SSfCO-VTjrgAHu794UqgBUsGMzAyn7gZ23OOVIeVRY-h0AxjZs_uTh0XvyaoZXkW1LaI5vBGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ‌سازی مؤسسه اعتباری ملل با بزرگ‌ترین مزایده تاریخ خود
🔹
مؤسسه اعتباری ملل از برگزاری بزرگ‌ترین مزایده فروش اموال و دارایی‌های مازاد در تاریخ فعالیت خود خبر داد. این اقدام در چارچوب برنامه بازسازی و اصلاح ساختار مالی، با هدف افزایش کفایت سرمایه و خروج از دارایی‌های غیر‌بانکی انجام می‌شود. ارزش این دارایی‌ها حدود ۱۰۰ همت برآورد شده است.
🔹
این مزایده شامل املاک، اراضی، ساختمان‌های تجاری و مسکونی و سهام شرکت‌های ساختمانی و تولیدی است. مؤسسه اعلام کرده است فرآیند واگذاری با رعایت کامل تشریفات قانونی، انتشار فراخوان عمومی و اطلاع‌رسانی گسترده برای ایجاد فرصت برابر برای همه متقاضیان برگزار خواهد شد.
🔹
کارشناسان اقتصادی معتقدند واگذاری این دارایی‌ها به افزایش شفافیت، انضباط مالی و ظرفیت تسهیلات‌دهی مؤسسه کمک می‌کند. همچنین زمان برگزاری مزایده، مهلت ارائه پیشنهادها و نحوه دریافت اسناد، متعاقباً از طریق رسانه‌ها و وب‌سایت رسمی مؤسسه اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/669699" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669698">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
استاندار گلستان: پل آسیب‌دیدهٔ آق‌قلا در کمتر از ۲۴ ساعت بازگشایی شد
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/669698" target="_blank">📅 11:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22054eabe5.mp4?token=DmJ5r8OtpagNJ1ru6L1AjKwhmD9SNJ09kJMEENl9aQNIk2monyJ1SKabgmcu-7LNZ3CQNvYnP_Shw8yQhUcPc60m8qsijVkFq6w0x9EXLBUN8mYN25xTH7igbM9nT_uKPgbd_ZRMEGK2jrxtLEReLu8kYtKYJ0gdF3ZapatjDIN6_YgAoIxoPzi_sDEsb5tpgnBUUW5YYG9vYCZt5oN-EiGXbQtypnvRNaVv1vAXGXjdUEa1UGXfsyt83_xQAq9v9mHMaMKJ_2oMHRW6A9ZKFRG9euv7yyZeI0D8VdiVyqq1TOVjExGvQUdhwRWRCyl2gyI968MCiUzm6t_Amb00Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22054eabe5.mp4?token=DmJ5r8OtpagNJ1ru6L1AjKwhmD9SNJ09kJMEENl9aQNIk2monyJ1SKabgmcu-7LNZ3CQNvYnP_Shw8yQhUcPc60m8qsijVkFq6w0x9EXLBUN8mYN25xTH7igbM9nT_uKPgbd_ZRMEGK2jrxtLEReLu8kYtKYJ0gdF3ZapatjDIN6_YgAoIxoPzi_sDEsb5tpgnBUUW5YYG9vYCZt5oN-EiGXbQtypnvRNaVv1vAXGXjdUEa1UGXfsyt83_xQAq9v9mHMaMKJ_2oMHRW6A9ZKFRG9euv7yyZeI0D8VdiVyqq1TOVjExGvQUdhwRWRCyl2gyI968MCiUzm6t_Amb00Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد متفاوت متکی:
با
اولین شلیک آمریکا جنگ زمینی رو شروع کنیم و پایگاه‌های آمریکا رو به عنوان غرامت تصرف کنیم و ازشون اسیر بگیریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/669696" target="_blank">📅 11:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669695">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88afe8279c.mp4?token=vKpAVAEwwkH08XKCeVVJh9sRNW9F2VOQlIyZmXy9pI9eo_1AuWNUJV-6-8smL-nGCZeHnxPCf1dc11VHPv2pBYZPoT2ojP9EQotVG1nj8qyN-lTlXQkbnbFU3BSRl2NKv2oOZBE-G9IG5bzRKQkg2bVfusVGfixEc9f01k69K5vKyw6FRjzsKsEka0r9RfyYVTYKPm0VOS3_1zMhW1e9G_lZi4ShvurtEXcLVzm8cC2NkMh-mokKKId6-bKuhTqgIrTtofktGRYu-zgpUGCeVoLE3mmi04M7kYpuYk5vzyP3OUv9tNn7oAE-U_SzEMN4kYG9toAENCFqNPoT08GC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88afe8279c.mp4?token=vKpAVAEwwkH08XKCeVVJh9sRNW9F2VOQlIyZmXy9pI9eo_1AuWNUJV-6-8smL-nGCZeHnxPCf1dc11VHPv2pBYZPoT2ojP9EQotVG1nj8qyN-lTlXQkbnbFU3BSRl2NKv2oOZBE-G9IG5bzRKQkg2bVfusVGfixEc9f01k69K5vKyw6FRjzsKsEka0r9RfyYVTYKPm0VOS3_1zMhW1e9G_lZi4ShvurtEXcLVzm8cC2NkMh-mokKKId6-bKuhTqgIrTtofktGRYu-zgpUGCeVoLE3mmi04M7kYpuYk5vzyP3OUv9tNn7oAE-U_SzEMN4kYG9toAENCFqNPoT08GC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیستم جدید ترازو در فروشگاه‌های آلمان که با لمس میوه قیمت اونو مستقیم میده بهتون
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/669695" target="_blank">📅 11:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
استرداد وجوه بلیت همه پروازهای لغو شده
رئیس سازمان هواپیمایی کشوری:
🔹
در حال حاضر شکایت معوقی مبنی بر اینکه مسافری درخواست استرداد وجه داده اما مبلغ را دریافت نکرده باشد، در اختیار سازمان نیست.
🔹
با این حال اگر فردی همچنان چنین مشکلی دارد، کافی است موضوع را به سازمان اعلام کند تا پیگیری و رسیدگی لازم انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/669694" target="_blank">📅 11:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHVHRxu_zmR3h1O2cTRGNMUpDux9k9IKVLRofRBuTqi8DFR7plt2NPSK7MtGFfqwixcIsCb5hb_OphklR9phHEhD4NN8OJ1bSD0Go6zWOUC_isLna9cSmud9-niGS8bosLbJafVkgqpLrjUbxhr_xg1JA9taEE9aGuJwa1WXpuXKTHGnmKCWwbJtZEqmeQLxWUCvsaVA6Ti5PUKyMmwK9u1dYWFpR4wXbAZoTgXSOWS6LajBYFhaFtuDH15ctS4T5FTKydbemYU8i7VfRJwgeV2WMgifdboAhejioZ_M59CLM8kjxTkfshjrltdaCBbJ4ZR0Vzh_nPCjF-hT1Gf2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/669693" target="_blank">📅 11:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba224ed12.mp4?token=BFyhqVUhj9qT2HNieUIgsb4sx-BMds_CA2lyfjSjUYDpfGq8Na_Yq8CLiPHasbGFM2UF94KhwvdrLRgae6lUDeY8nH4Ivwg1FnIQS-OhGWvYyMKxVCqmCyZjwhi7935Pyz6cdmPeoGg4Ubdq__2PjenrZDVUHMte8nZ-HCLTmPbQMQiEN5G7mOsg_YitWrS5y6bz7UjvKk_ronxmKQ0LjOxdFrKSMHY_tUps9jpdOrMeH2wda4NIw6GZDCusnG9JjHrSrxBnu-_gwmk9VccMPCArMXtg2rL0Bsx0TbazgcUcL0jkA3HWKtXcThyaK5dc1rjvzbqBGCVQrnl-rfv2sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba224ed12.mp4?token=BFyhqVUhj9qT2HNieUIgsb4sx-BMds_CA2lyfjSjUYDpfGq8Na_Yq8CLiPHasbGFM2UF94KhwvdrLRgae6lUDeY8nH4Ivwg1FnIQS-OhGWvYyMKxVCqmCyZjwhi7935Pyz6cdmPeoGg4Ubdq__2PjenrZDVUHMte8nZ-HCLTmPbQMQiEN5G7mOsg_YitWrS5y6bz7UjvKk_ronxmKQ0LjOxdFrKSMHY_tUps9jpdOrMeH2wda4NIw6GZDCusnG9JjHrSrxBnu-_gwmk9VccMPCArMXtg2rL0Bsx0TbazgcUcL0jkA3HWKtXcThyaK5dc1rjvzbqBGCVQrnl-rfv2sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار
کانال ۱۲ اسرائیل: ایرانی‌ها با اعتمادبه‌نفس، آمریکایی‌ها را مرعوب و همه پایگاه‌های آمریکایی در منطقه را تهدید میکنند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/669692" target="_blank">📅 11:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L52tMAkA4eTwHH7y1BxqzuLx5aOyjAfPdv5FCIYA9VgDQ434Gt2HEYsfvLY3rjBgA8nEt8VaN8GRZJZmA4hisE1fxB9AeE5vcmRvhkejVfrAqPx8JllIqJgUKXFxpJ3OxEGe_8PsiQJHuc7kLIwoRu5ycvrYIWlJhVSvxV3UY4nOGFyfLeUT6RrpagZwvUZkbAjrQgFnU89xoi2dGjBEcqHqQc_WkUK9eID41w0PbxfrO1zKhduMFtL5eCgg2myYP4ys-01InciD7CXUfLZYnuSlaSbNsLpqYETxrP7E1P3IuU7x4ZwyHI6RyfMpKv6ufwgAM62s0gy71u6NhZJSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پلاکاردی در تجمعات شبانه: هرکس مانع قتل و قصاص بشود؛ خودش گزینه قصاص می‌شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/669682" target="_blank">📅 11:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#باید_برخاست
♦️
ثبت رکورد بی‌سابقه ورود ۵۷۰۰ اتوبوس به مشهد | خدمت‌رسانی در ۴ پایانه موقت به زائران مراسم بدرقه " آقای شهید ایران"
🔹
محمدرضا قلندر شریف، شهردار مشهدمقدس، از ثبت رکورد جدید در جابه‌جایی و میزبانی از زائران همزمان با مراسم تشییع پیکر مطهر رهبر شهید امت خبر داد.
🔹
وی با اعلام این خبر افزود: با هدف مدیریت ورود بی‌سابقه ناوگان مسافربری بین‌شهری، چهار پایانه موقت با ظرفیت پذیرش بیش از ۳۳۰۰ اتوبوس در مشهد ایجاد شد.
🔹
شهردار مشهدمقدس با اشاره به اجرای گسترده‌ترین طرح خدمت‌رسانی در پایانه‌های شهر اظهار کرد: با پیش‌بینی حجم عظیم زائران، علاوه بر زیرساخت‌های موجود، چهار پایانه موقت شامل «مجتمع آیه‌ها» با ظرفیت ۱۲۰۰ دستگاه، «کوهشار» با ۱۰۰ دستگاه، «نمایشگاه بین‌المللی» با ۶۰۰ دستگاه و «بلوار قمر بنی‌هاشم» با ظرفیت ۱۴۰۰ دستگاه اتوبوس، در نقاط استراتژیک شهر برای ارائه خدمات بدون وقفه تجهیز و آماده‌سازی شدند.
🔹
وی گفت: علاوه بر پایانه‌های موقت ذکر شده، خدمت‌رسانی در پایانه‌های موجود شامل امام رضا (ع)، پایانه خطی حافظ و میثاق و پایانه راه ابریشم و کلات نیز ادامه داشت.
🔹
وی افزود: در این پایانه‌ها تمامی امکانات رفاهی ضروری از جمله امکانات بهداشتی، نمازخانه و آب معدنی برای رفاه حال رانندگان و زائران تأمین شد. همچنین پیش از آغاز مراسم، اقدامات گسترده‌ای در پایانه مسافربری امام رضا (ع) و سایر پایانه‌های شهری شامل فضاآرایی، تعمیرات اساسی، بهسازی و آسفالت‌ریزی انجام گرفت تا زیرساخت‌ها در بهترین وضعیت برای میزبانی قرار گیرند.
🔹
قلندر شریف با اشاره به خدمات ویژه در پایانه امام رضا (ع) تصریح کرد: ظرفیت اسکان موقت برای ۵ هزار نفر در این پایانه پیش‌بینی شد و با استقرار ۲۸ موکب، خدماتی نظیر توزیع سه وعده غذایی، پذیرایی، برنامه‌های فرهنگی و خدمات نگهداری از کودکان به خانواده‌های شرکت‌کننده ارائه شد.
🔹
شهردار مشهدمقدس در پایان با تأکید بر اینکه مجموعاً ۵ هزار و ۷۰۰ دستگاه اتوبوس به مشهد وارد شد که رکوردی جدید در کارنامه خدمت‌رسانی این سازمان محسوب می‌شود، خاطرنشان کرد: این حجم از تردد با هماهنگی کامل و بدون هیچ‌گونه اختلالی در روند خدمت‌رسانی به زائران و مجاوران انجام پذیرفت.
🔹
وی در پایان ضمن تشکر از معاون عمران ،حمل ونقل شهرداری و مدیرعامل سارمان پایانه های مسافربری وتمامی همکاران پرتلاش حوزه حمل  ونقل شهرداری مشهد از شرکتهای بخش خصوصی وتمامی رانندگان ارزشمند اتوبوسهای بین شهری قدردانی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/669681" target="_blank">📅 11:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تحلیلگر صهیونیست: ترامپ دیر فهمید ایران «فیفا» نیست
تحلیلگر روزنامه صهیونیستی «معاریو»:
🔹
رئیس جمهور آمریکا «بسیار دیر» متوجه شده است که ایران را نمی‌توان مانند نهادهایی نظیر فدراسیون بین‌المللی فوتبال (فیفا) وادار به پذیرش خواسته‌های خود کرد.
🔹
رئیس‌جمهور آمریکا هیچ شانسی برای دستیابی به توافقی با ایران ندارد که شامل تسلیم کامل در برابر آمریکا باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/669680" target="_blank">📅 11:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V69GXlayc7Js_G3HaP_lsuqRt-1lFN2Bq85ZFXJEwVCGiAvXTr7q4M8EMIVwpnQ_pZW_1jmvVXDkrdMfMZ9BGzLaXLi2xrap1wFm6iXjA16Yoei_i5QyPG0fVcaoYVSUDmjsGrsvi9BDouK-iWRq9vmHAAh_EM7gffuzfFALZZq7gGg5qWN8_yQSm2shsAfK5LMAuT-pmTZh77hJF_wVSHkbg4qvBy9wX9kd_Kk3fYQiT0oSmQYMY3_DG0oWvBsab_8MORw95V9Z1q_0rGyW8R2dMT3vrKB9QkUWr8eqDtarLJw6UVMVaf6Y8fivOaFy2h99G5E5EwerEQM-wSeDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بزرگترین تولیدکننده بشکه صنعتی در ایران و خاورمیانه
نخستین تولیدکننده بشکه گرید فلزی PLD-9000 در ایران و سازنده بشکه‌های پلاستیکی و فلزی ۲۲۰ لیتری دهانه باز و دهانه بسته، با فناوری روز آلمان (Bekum) و مواد اولیه مرغوب
🇩🇪
مشاوره و خرید
+989134470953
❤️
🌐
وبسایت
🚀
تلگرام
📲
اینستاگرام
🎯
لینکدین</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/669679" target="_blank">📅 11:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای ورود ۱۰ فروند هواپیما از عربستان صحت ندارد
رئیس سازمان هواپیمایی کشوری:
🔹
ادعای ورود ۱۰ فروند هواپیما از عربستان و الحاق  به ناوگان هوایی کشور تکذیب می‌شود. شرکت‌های خصوصی به‌صورت مستقل برای خرید هواپیما اقدام می‌کنند، اما این خبر صحت ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/669678" target="_blank">📅 11:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXEGnUc4FfLUahGwftQC8R5Ajao1PFfvb6Kyf095PfBivuLnJU8uUMYFac8MXJq3KJP-NfdhNOb1VP9LJ-RrIlHfW-th-cNvmoWN7EypRuyNzXXLNG4idqWNrcRcq78A_2ixcdaXicr_yAXjH_KTnbgNAczQDMnE84SWCNpqXnORk4ZC5SRzrHLLpyuFVcdA7W2gGmVVwM5TOwKDfjWhPMzD2URYElK6jMtYY_jey6nHCTZKLc8iAoIuRJKo5qOk_DuHl8E3kT6Z6x0LXI97P4AYJUOpwkkQhyBUP0Lc2BZpQagouAvgUIT3gA8jFLSBnySEcXSYPpZ3vsXdx-e2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور از روزهای داغ پیش‌رو فقط با همدلی مردم در مدیریت مصرف برق ممکن است
محمد اله داد، مدیرعامل شرکت توانیر:
🔹
با توجه به پیش‌بینی افزایش دما در بخش گسترده‌ای از کشور طی روزهای آینده، از همه مشترکان خانگی، اداری، تجاری و صنعتی می‌خواهیم با مدیریت مصرف برق، صنعت برق را در حفظ پایداری شبکه همراهی کنند. برق حق همه مردم است و با مشارکت همگانی می‌توان این نعمت را به‌صورت پایدار در اختیار همه هموطنان قرار داد.
🔹
با توجه به هشدار سازمان هواشناسی درباره تداوم هوای گرم و افزایش دما از ۱۹ تا ۲۵ تیرماه، روزهای پیش‌رو آزمونی دیگر برای همدلی مردم و صنعت برق است و اطمینان داریم همان‌گونه که در خردادماه با همراهی ارزشمند مشترکان، رشد مصرف برق کنترل شد، این بار نیز با مشارکت همگانی می‌توانیم از این دوره با موفقیت عبور کنیم.
🔹
هر اقدام کوچک در مدیریت مصرف، از تنظیم دمای وسایل سرمایشی روی ۲۵ درجه، خاموش کردن وسایل برقی غیرضروری و پرهیز از مصرف همزمان تجهیزات پرمصرف تا کاهش مصرف در ساعات اوج بار، تأثیر مستقیمی بر پایداری شبکه برق کشور و جلوگیری از اعمال محدودیت‌ها دارد.
🔹
صنعت برق با تمام ظرفیت در حال خدمت‌رسانی است و همراهی مردم، مهم‌ترین پشتوانه برای حفظ پایداری شبکه در روزهای گرم پیش‌رو خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/669677" target="_blank">📅 10:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669675">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e773733fb.mp4?token=fdqMerTWhNh_qF5L2vZVmAO8NFk5Ia--ctWws_s4WSvcojAPFiVQVcOLRfoQPT7HzIOrQJfhJ_3AHe7s8ycp9Oa2A4ppRF4bW0_aeQ-JG9EbdWscfMqOTd3j7scXYLNnGwBeQ36zjSqMkydpTCKzTTFe1AEyL0u9FVsx5H_H0PoTB5LnFaXlLesN97Ew2A1Fs-ecYbRgGgHnih9zSM3Qp6bosUb2UrOvRW02AYrHbeCwGXKTnMDhfwkYc2Xp3iZIDBqp3NBmqh2iBDhZoxx5FczVAHXQEQ-d9Ssv9Otyg3BljzrOdQht8ESgdz25BZnIsT4Qt31gTyhsacHYC5Waug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e773733fb.mp4?token=fdqMerTWhNh_qF5L2vZVmAO8NFk5Ia--ctWws_s4WSvcojAPFiVQVcOLRfoQPT7HzIOrQJfhJ_3AHe7s8ycp9Oa2A4ppRF4bW0_aeQ-JG9EbdWscfMqOTd3j7scXYLNnGwBeQ36zjSqMkydpTCKzTTFe1AEyL0u9FVsx5H_H0PoTB5LnFaXlLesN97Ew2A1Fs-ecYbRgGgHnih9zSM3Qp6bosUb2UrOvRW02AYrHbeCwGXKTnMDhfwkYc2Xp3iZIDBqp3NBmqh2iBDhZoxx5FczVAHXQEQ-d9Ssv9Otyg3BljzrOdQht8ESgdz25BZnIsT4Qt31gTyhsacHYC5Waug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با ۴ ماده ساده؛ یخچالت رو برق بنداز و خوشبو کن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669675" target="_blank">📅 10:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669674">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏆
ماتادورها با شکست بلژیک، در جمع چهار تیم برتر جام جهانی قرار گرفتند؛ اسپانیا به‌سختی به نیمه‌نهایی و به فرانسه رسید
🇪🇸
2️⃣
🏆
1️⃣
🇧🇪
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/669674" target="_blank">📅 10:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669672">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qoo8YvRd_pnr8k_lEKJRq01814CgpBXB8EiYMnnsHKLfDgjdRnu1jDZAxyjmAiDNlxMFQ7VA7n5VGNVihyOGJwMXlK_FBOuAga7qmJi_9RHJrzNI-j4A4r4gF1D_ZsGvOT9RfBoDyHZur_idjF9nzzRQ_x2u60TtCY_vzC92GVxhS8C_Ltu9T1jHqhYDuzCEQngoYgBLVinhuNJb0HR1SdYAzj9bkfYe3yb_lJMg2wmH68tGdjctE2bFBEM3nn-UVHhwSLGcWoSJkgoCgUvlJuBhRLnxQDWh6223gIjpXNopovW4sgRqqeemYbOdVLjh3AeoBAib1z1OYLanXnBKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6X1b5JvNUXEVVN7325BCGCrHASpYU9X8rHaPGzq-ZORiNkEYLvK2sMmCQ1TORYcYfGxifT0HIZL03Z983kpmsOs7593w79tyauZ50faepgKsttO0_CObh2h4fUm7wNyxVbGmru5wYz4HM1dsPERm14i-Sm0DQllmzUwSZEYWQKYp2XJprcRyA8b_elY_aZSlWentkl7J1T_gSmb89Ekdz6yEwnNJDdwAYzkDaid4feL4W_vE5Gjg1-nFD59ljK_IN1jHDTWIsUioHAH-pG4hcTgkVhFXHTtAtQPi5-DMeKxbVv8NhfzjAvnnM-832sVKQwIVrCtjdWev2DJGnd6lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عراقچی وزیر امور خارجه با استقبال مقامات عمانی وارد مسقط شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/669672" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d4e2e16f.mp4?token=hHPjtANzIED6p0dLiiBpBM2O6Bb00j590XWzi9iWD5WX48hgcU9TyrbMycYyMQB5VP83zqyw4fgYpiJs-3dAm5m8PYo4iOie6q7lhHGD12q_2oyy-kzx24Am3DaDrJyENP-cR7VyW3TSx6QlJCmAvfYSrXvMyCfH4Q3ohN28_r-0fsoIf4Cs65YiZPWYDKMP9VAosIJedhTTKjZmfDQ3JvTyPG2Vn5QuorMUpWthv-aZNkc3w4wXJmRUVoWR7iXrgAuTdQ2Zxv4wIkbOpCBOeVWFgD0QpDHk4jEgI-CXequizjJpJguFC3zyXyd2uhYfCgLUbLbQVKpk0DBIDUUBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d4e2e16f.mp4?token=hHPjtANzIED6p0dLiiBpBM2O6Bb00j590XWzi9iWD5WX48hgcU9TyrbMycYyMQB5VP83zqyw4fgYpiJs-3dAm5m8PYo4iOie6q7lhHGD12q_2oyy-kzx24Am3DaDrJyENP-cR7VyW3TSx6QlJCmAvfYSrXvMyCfH4Q3ohN28_r-0fsoIf4Cs65YiZPWYDKMP9VAosIJedhTTKjZmfDQ3JvTyPG2Vn5QuorMUpWthv-aZNkc3w4wXJmRUVoWR7iXrgAuTdQ2Zxv4wIkbOpCBOeVWFgD0QpDHk4jEgI-CXequizjJpJguFC3zyXyd2uhYfCgLUbLbQVKpk0DBIDUUBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچه یخ زده در قله سبلان
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/669670" target="_blank">📅 10:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPBpmFk2CBZvNm6TDd7V4CWYtF6sb-9AUhz-Cxgb9fzXD6d8YVmbuiFKAc0ZkuAH9DKBTEOIogJcU-QrIKXekGriJB0S0b4ZgeG3V-VvAUimfhvrJWuCmBNFqs7HNakERF94q99HRW4bnOjMG7hZKtIi7-YJjUFE4ueETU3PS3zTIu_zeVabx_3uWg_TQBPvzQp2lOGVhHGdzhYUAoxp9ylKKlDpAhBIvWawooh_o-k9AopAsWgGmWObRRQPxtAV_77RS1Kimvqb6nxgLkK_mqGc348D3TvMTeFYn52GwDZ4J0mOxZugRxfGx33LpYT91F4Avun61bdkxnQafYzvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669669" target="_blank">📅 10:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669667">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#باید_برخاست
♦️
ثبت رکورد ۹.۵ میلیون سفر رایگان در مشهد | بار سنگین جابه‌جایی عزاداران «آقای شهید ایران » روی دوش اتوبوسرانی
🔹
محمدرضا قلندر شریف، شهردار مشهدمقدس، از اجرای گسترده‌ترین طرح خدمت‌رسانی ناوگان حمل‌ونقل عمومی در تاریخ این کلان‌شهر همزمان با مراسم تشییع و تدفین پیکر مطهر رهبر شهید امت خبر داد.
🔹
وی با اعلام این خبر افزود: در جریان این عملیات بزرگ، ۹ میلیون و ۵۰۰ هزار سفر رایگان طی چهار روز به ثبت رسید.
🔹
شهردار مشهدمقدس با تشریح اقدامات سازمان اتوبوسرانی در ایام برگزاری مراسم تشییع و تدفین «قائد شهید امت» اظهار کرد: سازمان اتوبوسرانی مشهد با به‌کارگیری تمام توان فنی و اجرایی خود، نقشی محوری در جابه‌جایی خیل عظیم عزاداران ایفا کرد.
🔹
قلندر شریف با اشاره به حجم بی‌سابقه خدمت‌رسانی گفت: در این عملیات که یکی از گسترده‌ترین طرح‌های تاریخ اتوبوسرانی مشهد محسوب می‌شود، ۲ هزار و ۱۵۰ دستگاه اتوبوس به‌صورت شبانه‌روزی در بازه زمانی ۱۶ تا ۲۰ تیرماه، وظیفه جابه‌جایی زائران و مجاوران را بر عهده داشتند و خدمات‌رسانی در این ایام به طور کامل رایگان ارائه شد.
🔹
وی افزود: ناوگان اتوبوسرانی مشهد با ثبت ۶۵ ساعت خدمت‌رسانی بی‌وقفه، موفق شد رکورد بیش از ۹ میلیون و ۵۰۰ هزار سفر را تنها در چهار روز به ثبت برساند که نشان‌دهنده عمق برنامه‌ریزی و آمادگی عملیاتی این سازمان است.
🔹
شهردار مشهدمقدس، اهم اقدامات انجام شده را این‌گونه برشمرد: راه‌اندازی خطوط ویژه در محدوده حرم مطهر رضوی و خدمت‌رسانی فعال از ۱۲ پارک‌سوار و ۹ پارکینگ برون‌شهری، حمایت ویژه از خط یک قطار شهری با اختصاص ۱۵۰ دستگاه اتوبوس برای تخلیه سریع ایستگاه‌ها از مهم‌ترین فعالیت‌ها بود.
🔹
وی افزود: تدارکات فنی و سوختی با تأمین و مدیریت بیش از یک میلیون و ۳۰۰ هزار لیتر سوخت مازاد برای پایداری ناوگان و آماده‌باش کامل بخش‌های فنی جهت رفع عیوب احتمالی در کوتاه‌ترین زمان، به خوبی انجام شد.
🔹
همچنین به گفته وی، پایش مستمر از طریق سامانه‌های هوشمند نظارتی و اجرای گسترده برنامه فضاآرایی ناوگان جهت اطلاع‌رسانی مطلوب به زائران صورت گرفت.
🔹
وی با اشاره مشکل پیش آمده برای راه آهن باتوجه شیطنت دشمن جنایتکار، در اوج خدمت رسانی به شرکت کنندگان مراسم تشییع با اعزام ۵۱ دستگاه اتوبوس به ایستگاه راه آهن ابومسلم در نزدیکی ملک آباد برای انتقال مسافرین قطار به مشهد وارد عمل شد و موجب رضایتمندی این زائران عزیز را هم فراهم کرد.
🔹
قلندر شریف در پایان با قدردانی از تلاش‌های جهادی معاون عمران ،حمل ونقل شهرداری ومدیرعامل سازمان اتوبوسرانی وتمامی پرسنل و رانندگان خدوم وپرتلاش ناوگان  اتوبوسرانی مشهدمقدس، خاطرنشان کرد: هدف اصلی ما فراهم‌سازی بستری ایمن و روان برای حضور میلیون‌ها عزادار عاشق در این رویداد عظیم معنوی بود که به لطف الهی و هماهنگی تمامی بخش‌های شهرداری، این میزبانی با بالاترین کیفیت و بدون اختلال به انجام رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/669667" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669666">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
گزارش ماینرهای غیرمجاز چقدر پاداش دارد؟
🔹
هم‌زمان با تشدید برخورد با استخراج غیرمجاز رمزارز، شهروندان می‌توانند مراکز دارای ماینرهای غیرمجاز را گزارش کنند و با توجه به تعداد دستگاه‌های شناسایی‌ شده، تا سه میلیون تومان به ازای هر دستگاه مشمول پاداش می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/669666" target="_blank">📅 10:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLhmRg47uODxIwxTms2qPlrqwZqNnmuJyvjeWmD1scUnQVjC8ws_X2kQSUrlEAvhI0IpwvpugR6IYrRhaXXZ7ENpkKZDq8x_5YO1K0GhuM-w-6L4t8ixllPexTe5uKDg-RHeGGoJTNWBqRQC1rffyE-sqFXQLIexE0pHVF48EVUk4OjyieMXIbGywdabs_xSXfB-02LstlUxWHmkU0PVD515P68Eil0KFsog6gMprBGBOs4fUXR0Ut0a200KzlBboQ8PEb12OZ1fk6ObfAxSP0DtBmrOOIRSLBLUGIMNRDWiEDusgXxoe_wncyuo2FQReTpSGIv6ffdliIDJAcrDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVIdcvZ-QEUwEb_AxwlN-7XQqP267wED7mrcQWVx2TPuZyoYVLbVEgCGxWZkwOtvoCRLIHSElA6AexBOFROWBP0SOxIHg6sf2x11YMj4hAyro6u_4AVwPHyUTirbnIbq2GjSDJ7R393pq2TsyoWsd3UTdemjdrgKpfd1KB6s_7y6rs-cExMp6n2J9nZTrF3hcDu42ya8757K5eMi2eNMrpXyxCRkgSvSG8crqpkIMAwT_bZrrq5CilbeF90alB8sNqs7PPmaxLUhTRb3lNSWBoD4NB__ZDfyfPDT7vOPuCOlyTRWJoJziZQkbxIn6pwzxVGUDbTHlmghB481wfgNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpODiRUFXgMU54b-rVzgFBag9sFOQbfYW4squFNvMWMOgTP5lP1mzuO1ZTF_jwrvBaanX_8vxI8w8djeWuwBYr0lrkj73EjfyQXA-03Md-T9_vVmYpXl-wcVv40uvTX8GdzAnKXmev88APa8ls-C8rjQxEb3oGiEa4G4v4TH33Op22rd_CdnCchJ9hkL1I1rM1m-e_dE4K5_qLTuHJRAg7C2S8NQ0_4Uh6Yr6XFEVYEWCJAQBj5Pu5jILE6Q9lxX5sEELOuNyrJnpiCXj7eDIMLJ9OCoJdj9pgvi9i6bRSyHWlngIViadbYw-w0ODcLni7NbgIQksOeZOb488cyh0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک‌بار برای همیشه؛ تفاوت اعتماد به‌نفس و عزت‌نفس چیه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669663" target="_blank">📅 10:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6d0b0d32.mp4?token=IJEJDhWX1G8u7S-GZH7pN3UJRbX_qb30RrJil1VVsjsALXnFkJz1sfia6ohlXOxbj01ZyVrxg576Uul525UBtdavRAY7vZe42ahHgzMBx8XE7XymHX6AF7riC8e0kjB7GhUHA45OSkLRi9lhJP0z9gI3xNBbnvOgBrdt8S4uLS1yy4d5PpK8bJ1XKFsjaUSh4PyAEslv2qIB6c7cUcJBHo6ceWUbzRUPyK40-1SKtKPlODzrkoooPyA7G1OoY0Ve379CZ9fEeZn-nBXvm0HlwzyqA1kLBCfY7BZHMtYE72uicoKasif7VP342kPIIFi4-_8NjQc12myKjyEVKfXrew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6d0b0d32.mp4?token=IJEJDhWX1G8u7S-GZH7pN3UJRbX_qb30RrJil1VVsjsALXnFkJz1sfia6ohlXOxbj01ZyVrxg576Uul525UBtdavRAY7vZe42ahHgzMBx8XE7XymHX6AF7riC8e0kjB7GhUHA45OSkLRi9lhJP0z9gI3xNBbnvOgBrdt8S4uLS1yy4d5PpK8bJ1XKFsjaUSh4PyAEslv2qIB6c7cUcJBHo6ceWUbzRUPyK40-1SKtKPlODzrkoooPyA7G1OoY0Ve379CZ9fEeZn-nBXvm0HlwzyqA1kLBCfY7BZHMtYE72uicoKasif7VP342kPIIFi4-_8NjQc12myKjyEVKfXrew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنج کودکان فلسطینی برای رسیدن به آب
🔹
در نوار غزه که بیش از ۸۰ درصد زیرساخت‌های آب و فاضلاب آن تخریب شده، کودکان نقشی تعیین‌کننده در تأمین آب آشامیدنی خانواده‌های خود پیدا کرده‌اند.
🔹
آنها ساعتها در صف‌های طولانی منتظر می‌مانند و گاهی با خطرات جانی مانند حملات هوایی  مواجه می‌شوند. این در حالی است که ۷۰ درصد خانواده‌ها حتی به حداقل آب در روز دسترسی ندارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/669662" target="_blank">📅 10:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669660">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg45yChodfzx6nUeIbKLoxg1ZU1dVh-Z92uw0tUtpiWTrGIke2TOv87vJOYSnS-YQcUk8EWi8rMXqatKx8HOB6johDUTFc2R3iFG6zWST0pQWTqm2uvrpD6o2RsMDPvKWGsQgoAl0cyC10WmkD-DL4_xmf_XPBE3qk39BRiB2nA4RhYco_Y7ai7SCbBsvhqQ0afMAmJf6ylIWUosfwY7Lj34LHz0HBuvycwRtLkQtp99XR9YJKr5-HDrDQXEmncagZf4hb3YSDDB7apCbPzYyQ70TkxQcKfnn52UxrjF9GxFYwE7oNp8o8JJFKe354WPgbPxI-hxyUnq0e7OqWJ0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/669660" target="_blank">📅 10:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZMUcGJ04FxLu5QohDnvW_0_9Khk2Z6AwXaUs4nv4QEoI6dpJ7enxKQjGXSP4DxApTMSfqsZKN6cR4pubEFzYOr9ZOVVi1EjR-RZUI5OBz_9sv7UBpQhddni2B2eksdHtsNzLZip8DVEjiS2VVU_sUG_Yxm5OWc8W5gPfueol2LL8JGSKz51_4CXqaoJk1x7QVUS_bQKMvyDryDGVhd0rCSgHWMUvG-Hsf3I6UxBxExWjqKKLiuepkpUep5cz_Y-rNBz2mrqq9HNuGPH7JNU2tuRysoHzg7H05gGI0YJ6pVkzFbQn9U2oitgx4o6NhCO3Ny4_jvcv_hua1SGV9uamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفندهای طلایی برای از بین بردن انواع لکه؛ این راهنما را ذخیره کنید
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/669659" target="_blank">📅 10:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669658">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZZkLtbTBNibpBkxz_kavbSSwa8R2aHHO0NV0jUKFPR_TylEGFd0d8KyHPwd5A0pE9Tz2fgALL2Uu5_ifuafnHgoaYFM0NGTs6RRWJv4kehcKGHs0kA_TB-sHC_RDone2kDkaoE1l1c0wTDOg9qSXamJ05-F1rD-jr-yBGbOM09wvoifFD3D_PolkEMM2cWlVd17N8NopqGcPfA8rR8v3bndh8CZUz9Q-wnBcfuzoGbwkMaxVEAoMQUejx35OR4xwYGR4Q3-w1LrkUEQlwRyuLOXXkFh72sHdrqDlXgqJGb2eu9I4BnhJLQh7hvLSRLLT8ExqSC2uNZgF1UIWcdoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏨
اقامت لوکس در هتل ۵
⭐
سی نور مشهد با تخفیف ویژه
✨
فقط برای مدت محدود:
✅
تا ۴۰٪ تخفیف واقعی روی انواع اتاق‌ها
✅
اقامت ۳ شب، شب چهارم رایگان
✅
صبحانه، های‌فود و فولبرد
✅
ترانسفر رایگان از منزل در تهران (شرایط ویژه)
✅
استقبال فرودگاهی و راه‌آهن
✅
سرویس رایگان رفت‌وبرگشت به حرم مطهر
✅
شارژ اختصاصی خودروهای برقی
🎁
ظرفیت اتاق‌ها محدود است و رزرو با این قیمت تا تکمیل ظرفیت انجام می‌شود.
📞
همین حالا تماس بگیرید و قیمت ویژه را استعلام کنید:
☎️
مشهد: 05132021021
☎️
تهران: 02144673863</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/669658" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669657">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
خبرگزاری دانشجو این ویدیو را از پاکدشت منتشر کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/669657" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4f495813.mp4?token=te4CebcTf2GWtOKo7kOx851kG1EIjFaPP_VuM0iX-5n4GvaEOYiuYLhCzih9LexkxulslfbA5H7e9WtOgwK91bUojLmUMhgWLE8ESQ805rb1XG-d4pNNTqGgqSdQ9mp3Rs6vgQMEA_zr078hWd5N2s-NzmwdXOqWtxfrMbx_rmMCp9oP5cNvjSMDF5ATUxDzaxS5Y0Ec5HeLf5f04L3PaTAsossiMehz3lKzccYGnIjmyXx4l50jR8B8LQpMVVbxLbJKI4CCYwlbZ8atxU8WhhCvqlrRmx1rhXtKn-SOdUdS6A0U1p6OKMdpdvLunQBrm27e9jeFLhS4ifBQk4ARbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4f495813.mp4?token=te4CebcTf2GWtOKo7kOx851kG1EIjFaPP_VuM0iX-5n4GvaEOYiuYLhCzih9LexkxulslfbA5H7e9WtOgwK91bUojLmUMhgWLE8ESQ805rb1XG-d4pNNTqGgqSdQ9mp3Rs6vgQMEA_zr078hWd5N2s-NzmwdXOqWtxfrMbx_rmMCp9oP5cNvjSMDF5ATUxDzaxS5Y0Ec5HeLf5f04L3PaTAsossiMehz3lKzccYGnIjmyXx4l50jR8B8LQpMVVbxLbJKI4CCYwlbZ8atxU8WhhCvqlrRmx1rhXtKn-SOdUdS6A0U1p6OKMdpdvLunQBrm27e9jeFLhS4ifBQk4ARbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند. هنوز منشا و محل دقیق این انفجارها مشخص نیست‌.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/669656" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669655">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8564f3ab.mp4?token=rbFnX-0m_qIlzB1NoiW9kxwmQtEBcDvCdguRgx86-o8xBcDpccZ0wwn7I7PaBFr4fykpIWcJFnOWjALoMyVwT11Ry6-75uMoio6eOVSly-mM0AOAMRGBDpT8Ym0dUrTiTqbGSQBaO11DCCf8jktdiRCOZThngAyDUZwZSEn8y8PlNxZ_6GYPgrrH1amw24VFC4W7uv6ey3Z12hcyFjdcQJYv3LBpEhAoSKDiNvG1mUF3ppn4ZXr6x_k8pbUdtz0dMPen4guDbbhhkuYEMmeTmypPxmpNfpDihAjiprpO5awPwdWMrc10HY10Xa_Ibcw4oSJQPmrw_Y5CQ_zny3ZeT6jiHy-8i_BSYZPDATX1gcSQh0tS9ZLJooNaWXpFkJY3eimcK6tmO7znGkj5zvwclXfhTrDMgd0Gp97vfo71c8_kOIEeBVi9G7SK0dgsnhd7gK31zvOcq8vVZa1enk48wOBuYVPkixFTNp0P3UtMhOv322PHz1ebrxlpptQxs8UYy2N2NV5HIelSn1ofP2QbRZan-DFxMEdzmjgUIhOAppmfeMFzf_v7H4VDmkWlGVO1y5xePTjq0RLAGsMDeshhFqH5r170BkLldetTZPKkP0IXJhITxBH-I1PQCQ5VguTe9e2O8tm7IpiDlCcxAkyhOavkF3Ft9_zZEMU6PROe9ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8564f3ab.mp4?token=rbFnX-0m_qIlzB1NoiW9kxwmQtEBcDvCdguRgx86-o8xBcDpccZ0wwn7I7PaBFr4fykpIWcJFnOWjALoMyVwT11Ry6-75uMoio6eOVSly-mM0AOAMRGBDpT8Ym0dUrTiTqbGSQBaO11DCCf8jktdiRCOZThngAyDUZwZSEn8y8PlNxZ_6GYPgrrH1amw24VFC4W7uv6ey3Z12hcyFjdcQJYv3LBpEhAoSKDiNvG1mUF3ppn4ZXr6x_k8pbUdtz0dMPen4guDbbhhkuYEMmeTmypPxmpNfpDihAjiprpO5awPwdWMrc10HY10Xa_Ibcw4oSJQPmrw_Y5CQ_zny3ZeT6jiHy-8i_BSYZPDATX1gcSQh0tS9ZLJooNaWXpFkJY3eimcK6tmO7znGkj5zvwclXfhTrDMgd0Gp97vfo71c8_kOIEeBVi9G7SK0dgsnhd7gK31zvOcq8vVZa1enk48wOBuYVPkixFTNp0P3UtMhOv322PHz1ebrxlpptQxs8UYy2N2NV5HIelSn1ofP2QbRZan-DFxMEdzmjgUIhOAppmfeMFzf_v7H4VDmkWlGVO1y5xePTjq0RLAGsMDeshhFqH5r170BkLldetTZPKkP0IXJhITxBH-I1PQCQ5VguTe9e2O8tm7IpiDlCcxAkyhOavkF3Ft9_zZEMU6PROe9ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوژه داغ اینستاگرام؛ ویدیوی بامزه و پربازدید از این دخترخانم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/669655" target="_blank">📅 09:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669654">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند. هنوز منشا و محل دقیق این انفجارها مشخص نیست‌.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/669654" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669653">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
قابلیت جدید اینستاگرام؛ اجازه ندهید از عکس‌هایتان برای هوش مصنوعی استفاده شود
🔹
اینستاگرام در اقدامی عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند.
🔹
اگر اکانت‌تان پابلیک می‌باشد، این قابلیت به‌ صورت…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/669653" target="_blank">📅 09:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669652">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
زائران برای خرید ارز اربعین باید چقدر بپردازند؟
🔹
زائران اربعین بالای ۵ سال می‌توانند تا ۲۰۰ هزار دینار عراق ارز زیارتی دریافت کنند. با نرخ فعلی (هر ۱۰۰ دینار حدود ۱۱۸ تا ۱۲۰ هزار تومان)، خرید سقف مجاز حدود ۲۳.۶ تا ۲۴ میلیون تومان هزینه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/669652" target="_blank">📅 09:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLv1YjNZKXg1T2z6UhkDHq_acekLdj056fTUWYoc9eYdsyKq2kN9B_yy98PYxeFrnPVyjd-xxOqlBQbV7_uUyY72MULqZtsozmWbr0NI7uiuYFp8Nro07zkUpCNKHDtobMfk2ZMjbvBkHPciKouwHG1j9Ql_BVAHOxnj_8aFKmLabVAZdwrr7rgIC59SLUfqF_1EOLt4Os6NzxfP-gxK8FoZxOa8n6dJ9ZXfXVoERvSB_vIIBEjITD4YG3rW70SKt6plC5OeALYFYns0WySv_XYuGXgkxWZs6nOsxiICzBFXhs4nLNKbyIl4Mhr02eXiKdCMk8DnUKZhiODwtSQpmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سند خیانت حکومت امارات لو رفت
🔹
وزارت بازرگانی آمریکا سند جدیدی را منتشر کرده: تسهیل مقررات کنترل صادرات و ارتقای جایگاه صادراتی به امارات به پاس حمایت آن از تجاوز نظامی علیه ایران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/669651" target="_blank">📅 09:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669649">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJUD-bmaTl1bIB_1OURNHnQc_c-kYCI6AtZK8JQvLpPztlW1TOamw-m071_5HMkKL9b4Gjo3ZKPYC8oTquKFX8ij6-dO-DqGU4-ungmq0cI_FDjicyaYbXtVWdh2TRFqPeekKrA9uID1V6XnCl8Ong6FdkXbTgJQfYODFcgSKtryAAPxxT3vTirtVbQEXpGG5m0IJTGyh6G7KYMhJsH5Q5cHsqj8tizogViG8oLipCAhBdTQkzkR6ratIq9cgxdI06TYI1NQa03PxGYPao3GcOzRIXY4VxmLqtVuOX1wh8jyuc255to2B8WRNm5s1uA_sVWPgF2E46QCYzpZy9dZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpPDWH2jdb9MJsxokaLqpX-IYUElAV6n7-cjLcdqq3Ily1OO7psh8hLYeEgBH3OKbil4qGZ6EfSPfRhk29tVVvujV8uU8uq5jfWz0hW_oPBjx0eTmZqNqAXLIvzTsmNcexA3lP2HNkuhFg_xbe67JtoKPOaFjcT3owfa1UD4pEk2TwWXOXp2zd_bbAVlOe-G93dkaBdU81kJKA-KhWRDnvPB4gfMtLiN8F-lpzMm3Gk_YuRVY2wbIapdy6IC8iguM97zzKsPDd5XLI6-Cupx3AeIRxEuH5r3foZ6-c2GlAypII258RieFioEfGJjtvZTzQH6FLfxFr9QLu6HOtWHbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عراقچی وزیر امور خارجه با استقبال مقامات عمانی وارد مسقط شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/669649" target="_blank">📅 09:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669648">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08c4f2cc6.mp4?token=eSFnbOwTxx0pvLY3wRjcYFJI1KjDkFOPinR-sAZeqZCqCOVLMDcOYUHrNkoJw5UcDzVN9pEcdS0zLW85VMIYHXZTVYJxM2TBoeFIQ8vLVS_KhnoiGtB9qkRP2mA1F9mcvq8XLzyU72U5mt1eGK18PmqsluMGg8kcjQu1WpoyjhD9Ixwlxnw8dh-zVAS7_RIxOmFMJa0BrMkmxtbHRcaD81s13PeerfSQq34IWwOEkd9W57ReihV0n8B0GcW_Ok8OmwC-CwMTNTqfmd-RZ9cjXyQ0xySqMEX5XUKC-9_uNEh-hBvWydWBMss-e_xDi7BAKHvN5BKGVZ1Z88kqPHNbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08c4f2cc6.mp4?token=eSFnbOwTxx0pvLY3wRjcYFJI1KjDkFOPinR-sAZeqZCqCOVLMDcOYUHrNkoJw5UcDzVN9pEcdS0zLW85VMIYHXZTVYJxM2TBoeFIQ8vLVS_KhnoiGtB9qkRP2mA1F9mcvq8XLzyU72U5mt1eGK18PmqsluMGg8kcjQu1WpoyjhD9Ixwlxnw8dh-zVAS7_RIxOmFMJa0BrMkmxtbHRcaD81s13PeerfSQq34IWwOEkd9W57ReihV0n8B0GcW_Ok8OmwC-CwMTNTqfmd-RZ9cjXyQ0xySqMEX5XUKC-9_uNEh-hBvWydWBMss-e_xDi7BAKHvN5BKGVZ1Z88kqPHNbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک صبحانه سه سوته شکلاتی جذاب
🍫
😍
مواد لازم:
🔹
نان تست، نوتلا، تخم مرغ، شیر، وانیل، مخلوط شکر و دارچین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/669648" target="_blank">📅 09:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669645">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
نمایی متفاوت از مزار رهبر شهید و خانواده شهید ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/669645" target="_blank">📅 09:16 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
