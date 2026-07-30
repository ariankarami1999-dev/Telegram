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
<img src="https://cdn4.telesco.pe/file/hkrjOUuyViZ1jjCuqIc5TQOzPN2GPYLfNrJcxx3WrsjQ6BUhD-liLfk7oKMaTa7UT4PFsaTSDkP1VwKdpuJeZUXITLCuOy6OUskod1Aj8PxSJZbXhQDxi8AzkM4b6CCvop4PhEmAoMaX6RG-usuhJFJHzTr2VO8eU3SYr794TUtkLLr75ub0se212NSQkwsBmU5UBljNcRDXs3OcAp3khcL_gII6deVcw1vaK69EmXV9kBucpevIIm2nJQbZxJndjdo1kIKc8uN8obIQV1vf4dfMnlo4q39LeXGZ2I44xv7DEtIxHj_GbG92M6b23t19xyouISdl7NlZQFLDKElZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 19:02:01</div>
<hr>

<div class="tg-post" id="msg-676721">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc2c7b75.mp4?token=Y5MHxaepTs6hZI9VjAG7SQsZc_BgsgYkAzBSVki9jtIjf5TKyWSVvYkBNojkZRvO0iCyU5qQAQObucA6twYkV7qr4cBMIbRb156kZERCZPCXyuOotdb3n85UTGNXTOOLxgalaV2GLQDhORyOVQIesdHpqX2SgObIuFAIUaf1TGYLLBKVinw79lJpaxH11i0g1OvRHMw3IZd6M0KMHxJlGK-45gH3naPeeW9oEfr9l2ykE5aKCtmmmvWnNlRLMYZZki6_HOu4e8wk08cwhcbc4oyrycPua0KaK6dYjGLyn6LjhkG5agPg9wsvQPT6-OpObq_qL5ckF_k0oPxRQ0I60g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc2c7b75.mp4?token=Y5MHxaepTs6hZI9VjAG7SQsZc_BgsgYkAzBSVki9jtIjf5TKyWSVvYkBNojkZRvO0iCyU5qQAQObucA6twYkV7qr4cBMIbRb156kZERCZPCXyuOotdb3n85UTGNXTOOLxgalaV2GLQDhORyOVQIesdHpqX2SgObIuFAIUaf1TGYLLBKVinw79lJpaxH11i0g1OvRHMw3IZd6M0KMHxJlGK-45gH3naPeeW9oEfr9l2ykE5aKCtmmmvWnNlRLMYZZki6_HOu4e8wk08cwhcbc4oyrycPua0KaK6dYjGLyn6LjhkG5agPg9wsvQPT6-OpObq_qL5ckF_k0oPxRQ0I60g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی به صنعا تکذیب شد
🔹
برخی منابع یمنی اعلام کردند خبر حمله هوایی عربستان به صنعا صحت ندارد و صداهای منتشرشده در واقع ناشی از رعد و برق بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/akhbarefori/676721" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676720">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978530fc01.mp4?token=Ve5snL6_SFu7Hh7R_lPwbaL6rpoYWPZOitGlRQoWOFO-9wO4dGiuXQW02wnEqiMHucEsPb11LeEnRNHk1CUWYh6R3HDO6h9IY_2sAz1_IS73qDNdfYC5EobWysEGTJqM4RzIOGmM9-5CARkK9lFoe-wqCBZaAz55QgKAUrpW5XrDOA4PJo4K8o1Z8KfUKR-mzYe-k_bHKTPb1Lk1zH3Bn2m1fsFeRqxv2xR1PhsusdtwXtq5hKhSkfNMBO8dOmW2D2Oa2Pt0btdiusElKPo-Tato1Ei-TEpn_r1SnUlLhaipX-2cw7lDh9K1LGT4ZeiJGqmBdkhySbcZng1QBcEakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978530fc01.mp4?token=Ve5snL6_SFu7Hh7R_lPwbaL6rpoYWPZOitGlRQoWOFO-9wO4dGiuXQW02wnEqiMHucEsPb11LeEnRNHk1CUWYh6R3HDO6h9IY_2sAz1_IS73qDNdfYC5EobWysEGTJqM4RzIOGmM9-5CARkK9lFoe-wqCBZaAz55QgKAUrpW5XrDOA4PJo4K8o1Z8KfUKR-mzYe-k_bHKTPb1Lk1zH3Bn2m1fsFeRqxv2xR1PhsusdtwXtq5hKhSkfNMBO8dOmW2D2Oa2Pt0btdiusElKPo-Tato1Ei-TEpn_r1SnUlLhaipX-2cw7lDh9K1LGT4ZeiJGqmBdkhySbcZng1QBcEakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان رسانه‌ای خبرفوری در مسیر کربلا
🔹
کاروان رسانه‌ای خبرفوری روز گذشته وارد نجف اشرف شد و پس از زیارت بارگاه نورانی امیرالمؤمنین (ع) پیاده‌روی خود را در مسیر نجف به کربلا آغاز کرد.
🔹
اعضای این کاروان این روزها همگام با میلیون‌ها زائر، در مسیر عاشقی قدم برمی‌دارند…</div>
<div class="tg-footer">👁️ 324 · <a href="https://t.me/akhbarefori/676720" target="_blank">📅 19:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676719">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbb8c9ef5.mp4?token=VBWaw4m70XL2lNsBt2t9DWDkwEM3Aomrst4ER8_sk3FRJd9OLCkLjdTTdE4TmvvOygilYPXneRTEXp3hprkmxhBKCOkYBmMGBEhQG886uZwpUbblrd9vw_-BfCZCtGeXzQqCkvOMq4mY9-6aogV6SybEh0VxLUz19Z8u0fvPWRnMbqHuJAYWbh_uaKWgHuSo-4hXpvMARwmDcIZTXzKvL1ltNd0H997RAOihoODJIEod6-753vLIdWZz4IWMZLaKOJIlfNMY229HWBNhEwlFB9K-a_Kel6PR-5SuDKbZyNGclFi79udi8keexJp_ImHxK68NvT7j5-dn23vzLanhQF0rxhQ65QpjgA6te0JQ851QcyHFITod9i3mMsWMVvD4Rhkn5NlLDGUzZf2CV_ykINGQZdx2cBppPKNDtEfy3aVXfUX9zwI2ZxrZziZ4ghK97xcjyaP8dv9lmOpbBbOFuJE-qSYc8nhNStn33uiy2rqS5oZrPOura8AZBQKmwykghr0GhyA6QSKZokXVaJKtjdyxeBUYkD-HMQ5-oa4lIiQGbcYeKZkUH8Ch3WuNLE2NxNT1Ff5ZfhMlwMelVuX4FSm22A_8pT8tk34pbHa-lbjXJtNPcFIt9xtrZqYWXh8zaEVaWvvnPAcYo7064MBNnyGE6HUnQTDaWGGf8YLPGm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbb8c9ef5.mp4?token=VBWaw4m70XL2lNsBt2t9DWDkwEM3Aomrst4ER8_sk3FRJd9OLCkLjdTTdE4TmvvOygilYPXneRTEXp3hprkmxhBKCOkYBmMGBEhQG886uZwpUbblrd9vw_-BfCZCtGeXzQqCkvOMq4mY9-6aogV6SybEh0VxLUz19Z8u0fvPWRnMbqHuJAYWbh_uaKWgHuSo-4hXpvMARwmDcIZTXzKvL1ltNd0H997RAOihoODJIEod6-753vLIdWZz4IWMZLaKOJIlfNMY229HWBNhEwlFB9K-a_Kel6PR-5SuDKbZyNGclFi79udi8keexJp_ImHxK68NvT7j5-dn23vzLanhQF0rxhQ65QpjgA6te0JQ851QcyHFITod9i3mMsWMVvD4Rhkn5NlLDGUzZf2CV_ykINGQZdx2cBppPKNDtEfy3aVXfUX9zwI2ZxrZziZ4ghK97xcjyaP8dv9lmOpbBbOFuJE-qSYc8nhNStn33uiy2rqS5oZrPOura8AZBQKmwykghr0GhyA6QSKZokXVaJKtjdyxeBUYkD-HMQ5-oa4lIiQGbcYeKZkUH8Ch3WuNLE2NxNT1Ff5ZfhMlwMelVuX4FSm22A_8pT8tk34pbHa-lbjXJtNPcFIt9xtrZqYWXh8zaEVaWvvnPAcYo7064MBNnyGE6HUnQTDaWGGf8YLPGm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت ۴ ایرانی در حمله مشترک عربستان سعودی و آمریکا به کربلای معلی
🔹
پاسدار شهید علی اصغر آستانه
🔹
پاسدار شهید ابوالفضل متقی
🔹
پاسدار شهید مرتضی اکبری
🔹
پاسدار شهید امیر عباس درهم فروش
🔹
هر چهار شهید اهل کاشان بودند. / صابرین نیوز
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/676719" target="_blank">📅 18:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676718">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUrue6hcV8KbG2a1VFQypNhmb9XDWwSswr-KDjew8WJEcUH483wCZrK9TG8D3Kk4o9Trc39K2pNlHRUGn-73Nj5ryqUQv3BeRleRdOOGY6qdPzET2tsn8KjGKSjOaFB1gvRMiu1AQzLLxCLEBsmRLBit7PzWHok8FdxR3yfQXHwKGZaWr03Oo2JrJ4CLtU710Cgp-hkb0F7vzFzTnO0JJN3p8TY9WSlOfj2eXE6L5yYaa04q2zYY6n9rCBhD-HsAHfsMuoZElJaTtLy9KScVlsACarPm7eOZM8TdN6JeqrpCTX2Rw-r3Q9yvDcF0p1ChQ8dXHXt_WhhlLjlzSIl67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی به گوترش: چرا نام آمریکا و اسرائیل را نمی‌برید؟
🔹
سخنگوی وزارت خارجه در واکنش به اظهارات دبیرکل سازمان ملل، از او پرسید چرا با وجود هشدار درباره نقض حقوق بین‌الملل، از نام بردن از آمریکا و اسرائیل به‌عنوان عوامل اصلی این وضعیت خودداری می‌کند و خواستار ایفای مسئولیت سازمان ملل شد.
🔹
آنتونیو گوترش، دبیرکل سازمان ملل متحد (۲۳ ژوئیه ۲۰۲۶): ما شاهد بی‌اعتنایی نگران‌کننده‌ای به حقوق بین‌الملل هستیم؛ مصونیت از مجازات در حال گسترش است؛ نقض‌ها بی‌پاسخ می‌مانند و هر نقضی که بدون پاسخ بماند، به سابقه‌ای برای نقض بعدی تبدیل می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/676718" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676717">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در صنعاء، پایتخت یمن/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/676717" target="_blank">📅 18:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676716">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در صنعاء
،
پایتخت
یمن/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/676716" target="_blank">📅 18:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676715">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
♦️
رهبر انصارالله یمن: عربستان همدست آمریکا، اسرائیل و انگلیس است و در راستای اهداف صهیونیستی در منطقه فعالیت می‌کند
🔹
انگلیسی‌ها و سعودی‌ها قبلاً تلاش‌هایی برای اشغال یمن انجام دادند، اما به دلیل مقاومت مردم عزیز ما در برابر توطئه‌هایشان، شکست خوردند.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/676715" target="_blank">📅 18:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676714">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4de5c727.mp4?token=agIGVlocWVBUWf2UD7SZ6_ydXRcEaSJScijmTtpL9SxGIrtS4gBxpRNlWxKkJMLD4cxufXFcyTeOI2g7CveKxjQpCwFjLTKeB5RJRuVUAUng9oqCzKqNkEPEepVjHTXnPyx_eOpe0kh840MiIqMCGaKnKkBdrTHBl84iCR1ug_oGmaQ-ft1ZapXEm73jZbMKmlMNu11UHgaIxaErDbdw0SGjdhQB2G-7NdnRgFZOlLl-h64ujSdPCrjdJQ_fZ2RMvhFuzQHfllBR6ykJctP7w6cN9I8MJJR8wW6_C3Slahv7TCV7fJuxXe5P4XOZN-KCWhohfT-RsXYXryyjk27v_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4de5c727.mp4?token=agIGVlocWVBUWf2UD7SZ6_ydXRcEaSJScijmTtpL9SxGIrtS4gBxpRNlWxKkJMLD4cxufXFcyTeOI2g7CveKxjQpCwFjLTKeB5RJRuVUAUng9oqCzKqNkEPEepVjHTXnPyx_eOpe0kh840MiIqMCGaKnKkBdrTHBl84iCR1ug_oGmaQ-ft1ZapXEm73jZbMKmlMNu11UHgaIxaErDbdw0SGjdhQB2G-7NdnRgFZOlLl-h64ujSdPCrjdJQ_fZ2RMvhFuzQHfllBR6ykJctP7w6cN9I8MJJR8wW6_C3Slahv7TCV7fJuxXe5P4XOZN-KCWhohfT-RsXYXryyjk27v_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای: اشغالگران صهیونیست مناطقی از جنوب لبنان را به‌طور گسترده ویران کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/676714" target="_blank">📅 18:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676713">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c5c37a15.mp4?token=H92XHUT8kgS0ITAtnjbbfurxQSSidx4agG6KKi9p6qj1HyIL1h2TozD1LfgtQh43aWCrJvYzchaShsjKKINqsOOCTBU75TlAz_ANgD5WBrD1Fm93oXhiZ0Wk01-JG3X1pHZL3JAZFkxWVkmgES1sCFreFiW6w3CSO0yIKnCx9EWHDpuiasX4M4cyd-6iNExqPDOcKcXfgkPKLfom3yC1BIwPEKpF7ZRXDbrfeBKacw3nOHV3Yv2RVLWcUpn353YDRJ4lhW7dgxiSLVCyxcmOAV2-if9quKujkyCpik2YriOqjZYMdjYdrwcS49Xwkw2JKje8ISP3YEehqURoeH1NTzNCfSQuwQFrDpE6mZC9ylQe0FTTORwcGUiQYeSiD9yb6VuT-wqLPydHL6cMbYi6LblhSBbP-3gkAqTQePOyCx6DZBTCrqavPRmERdwms22P1QcqEirmlVMw2c4Luekyo9GkgOCqVS-L8z2OVN3mL7q6QpEElGF8Sni4Ne9pWaYaCgWKu8fV3dBfLeTK0wkFnXgVgbDRTth-Q7UXHMRm4LIqxVmplI1uyq724YSPGvv6q6OQ6mgwDIUERzt8kSnD2ryGydoiG2-FQeAnoVMhvE70SZbz2ZaH20JVMH5XIGluHjlTYCOL5-UlEmCCvGpbaj8PAMd5eQF2XNTZAJHbbD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c5c37a15.mp4?token=H92XHUT8kgS0ITAtnjbbfurxQSSidx4agG6KKi9p6qj1HyIL1h2TozD1LfgtQh43aWCrJvYzchaShsjKKINqsOOCTBU75TlAz_ANgD5WBrD1Fm93oXhiZ0Wk01-JG3X1pHZL3JAZFkxWVkmgES1sCFreFiW6w3CSO0yIKnCx9EWHDpuiasX4M4cyd-6iNExqPDOcKcXfgkPKLfom3yC1BIwPEKpF7ZRXDbrfeBKacw3nOHV3Yv2RVLWcUpn353YDRJ4lhW7dgxiSLVCyxcmOAV2-if9quKujkyCpik2YriOqjZYMdjYdrwcS49Xwkw2JKje8ISP3YEehqURoeH1NTzNCfSQuwQFrDpE6mZC9ylQe0FTTORwcGUiQYeSiD9yb6VuT-wqLPydHL6cMbYi6LblhSBbP-3gkAqTQePOyCx6DZBTCrqavPRmERdwms22P1QcqEirmlVMw2c4Luekyo9GkgOCqVS-L8z2OVN3mL7q6QpEElGF8Sni4Ne9pWaYaCgWKu8fV3dBfLeTK0wkFnXgVgbDRTth-Q7UXHMRm4LIqxVmplI1uyq724YSPGvv6q6OQ6mgwDIUERzt8kSnD2ryGydoiG2-FQeAnoVMhvE70SZbz2ZaH20JVMH5XIGluHjlTYCOL5-UlEmCCvGpbaj8PAMd5eQF2XNTZAJHbbD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حوادث پرتوی
🔹
هنگام حوادث پرتویی کجا باید برویم؟
در صورت بروز حادثه پرتوی در منطقه‌ی شما، باید فوری به داخل ساختمان بروید.
صرفه نظر از مکانی که در آن هستید، اقدام ایمن آن است که:
🔹
به داخل ساختمان بروید، در ساختمان بمانید، گوش به زنگ باشید.
همه‌ی درها و پنجره‌ها را ببندید.
🔹
به زیرزمین یا وسط خانه بروید. مواد رادیو اکتیو روی قسمت بیرونی ساختمان می‌نشیند؛ پس بهترین کار این است که تا حد ممکن از دیوارها و سقف ساختمان دور شوید.
🔹
پنکه‌ها، هواکش‌ها و دستگاه‌های تهویه‌ که هوای بیرون را به داخل ساختمان می‌آورند خاموش کنید.
🔹
دودکش‌ها و دریچه شومینه را مسدود کنید.
🔹
حیوانات خانگی و لوزم مورد نیاز‌شان را به داخل ساختمان بیاورید.
🔹
منتظر دستورالعمل‌های جدید ستادهای بحران باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/676713" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676712">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4338ef0bcc.mp4?token=XoUTCF-aFGEyqiHNMkmY3zktFXYT6U5RiPL0_4m9BX0sSVONSO02zYKoAYgYoKxNzD4FWGWWOcFF2nisuU5YvTGnaUWjMuYfPbSiUlyMj03Eytd1-z6JNYELfFkHujQXnRkzSrCPWoN64JWs-_k221Cby3R-21ht8N-lqXAKoynhuX2ChdPbkfRlYn89X4Eu6dr6tU7EqdTUO0iV7rkATfyCHmjELdloF16eSyKV_IJ14o2nLaS-6808mPbR5zkKQRWlmKhDuuEw92y57ztobMhfIcIuwqRq0O3XQidxVgyptVYKG8gEZbUl0g84NrpWZdMDE36rKSE4ZMeIkO9tdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4338ef0bcc.mp4?token=XoUTCF-aFGEyqiHNMkmY3zktFXYT6U5RiPL0_4m9BX0sSVONSO02zYKoAYgYoKxNzD4FWGWWOcFF2nisuU5YvTGnaUWjMuYfPbSiUlyMj03Eytd1-z6JNYELfFkHujQXnRkzSrCPWoN64JWs-_k221Cby3R-21ht8N-lqXAKoynhuX2ChdPbkfRlYn89X4Eu6dr6tU7EqdTUO0iV7rkATfyCHmjELdloF16eSyKV_IJ14o2nLaS-6808mPbR5zkKQRWlmKhDuuEw92y57ztobMhfIcIuwqRq0O3XQidxVgyptVYKG8gEZbUl0g84NrpWZdMDE36rKSE4ZMeIkO9tdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکذیب حمله در ایرانشهر؛ دود سیاه ناشی از آتش‌سوزی دپوی سوخت بود
🔹
در پی آتش‌سوزی یک دپوی سوخت در محله غریب‌آباد ایرانشهر، ادعای وقوع حمله و انفجار تکذیب شد.
🔹
علت حادثه هنوز مشخص نیست و تاکنون گزارشی از تلفات یا مصدومیت منتشر نشده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/676712" target="_blank">📅 18:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676710">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
روسیه ممنوعیت صادرات بنزین را تا ۲۰۲۷ تمدید کرد
🔹
کابینه روسیه اعلام کرد ممنوعیت صادرات بنزین تا پایان ژانویه ۲۰۲۷ تمدید شده و صادرات سوخت کشتی، دیزل و گازوئیل نیز تا ۱ سپتامبر ۲۰۲۶ ممنوع است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/676710" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676709">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یک مامور در درگیری با سارقان مسلح شادگان به شهادت رسید.
🔹
مهلت ثبت‌نام آزمون‌های علوم پزشکی تا ۲۰ شهریور تمدید شد.
🔹
معاون رئیس شورای امنیت روسیه: جنگ اوکراین قطعاً با پیروزی روسیه به پایان خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676709" target="_blank">📅 17:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676708">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-U5LfKb0GVfNYNyWEFIvuvgk4ySaqxuanW-FUEUpNwMi5rYh_GDI7QEvVxd3mwy8N1JXVbfTM-h6bMkEmC2WCKhbzrzYrHi9Z15Pri8KWVgrYYMSjqAiKvpW32loX__taCy8vwdtBS6eoM9GNhksuoW-qrv4tiUSs61juarddJ7ynyH-fLTQ-CuVBCS5al01cCYx5MuJ-mPlJSSH6BSOftfDU-4a3TpTFiZKKctCZoyy5N9GnWt81uD5PkQAyG34fZvNwHdj4dgcspv8d92RUpXig0odmKYS0lYQiXkt-HqtK_HF3-_hDxaRGrJGzcB3M1GhSA6v6x5uUtu9jLV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوبارو صابونی؛ تاکسی نوستالژیک سال‌های دور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676708" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676707">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DguXsuo_JdYFk7lK7Yer0wmfDsiLPByLjT6APRIKUsz8YrvdgP7TV4Q1YS7KPVLYesSwM7f47qC3_0HhQ1LXcWkjxJP-bYpyEcOjYk__DNbCtsoFlh-GuRbaGSxHkPH5hskeIjFv1jgXC8uN78R8Ys3lq1LXQPpNnenXSjjI1iln9chfdi56BwCTh5uQPcRtQ7A3Z7_BMa5wCm0CN4Rht6RX2WLhnKB532vsqJtjfKAsLeyLbmCeQjalB70VI7sLQPLWb6-YTIDjpffXxNyusv8dWwJ9D_2f6Dibh-GhRLghItosHPs2tOdY0G8A6zLWvni_r_HShufH-Hi1otT17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مناطق مسکونی در شهرک طیبه در جنوب لبنان توسط اشغالگران صهیونیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676707" target="_blank">📅 17:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676703">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSK8liriGlJqfyXjwvPujchmpHHvaYnYf_DGQmJ4aHmS133GJdkWNAx49Gshc93iY_ccfGg-W9P7pN4Uc-M9gyMIuEZncYS-Z65jB6uzzz-7q_gzz1GeO1CzGe8BUxC2s23_zTLyIco-oEk3689GQ5thmsR7NUdmFgvSLmqN14gpCn_OBDNTASVAi73FJ2s3KLQFX8r-Q3Omv75G9Gt7gOp82gc76xLvvyabf2nUXJVjcOE7oTwtijrXR7JvvKgNWQYdPQ9XlzyJiBLwVxyCUJgMs3FcbJFQnT-1QpNh1-IPg4dkiGfO7y17-BNgW9EzP4c4ROpEPCQ-_9-wEuhMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2VELCc0LHQBVG-nhYA1jiQb85bABknAhUW1hNzMLfNk3pw0QbW4UUniWRDcwRP6zQ9tEJ3CpWT5e1m2fPk-LFtqs9aDz5pM94XEKo9iirU7fm7VqnnxUCjrXzm1acu8E-D5NqqoHJYbTCBwxhaih9UyEM-E7e25cLDbqncVqETI6ZFkbzItKqBtDkX8ivOuEqEu_jW43W8x-rl1r_ACXmmbFZsRjfPEKCVGIYi0zvNpASnLhjOwlZSdlJ-qOg-b39bp6vqATQVOoqybljyNTAyFO1t_HSmQ5qHQWfnKdui508Kpzk3SyX9P58VmnyTuIIrCnIlQY0o5VVZQZPa9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMT-b-JPaRm6XfhBG9vvaTPAiTt_hBTYrbCOx-rUBVzFgtH1-5TeSk2OEKsFvislKBEnntpaXdsjAHYxi8Z25g5xlwk7vw4uL_OIqnTZncpFQMMQCPb_V6YRcn_HlBt0W866uwK1CS60WVXl6fDq8aMgxnV_e7lF1qFTEhPokw2-KBKeTAjeIGWxQLtNQHgkUTdzKoxAmt9da9c1fM0twDzCqJaAFglkte3MUwve3WOP9lKdpSuxyHUd6FekL88CYDXMmbxExR0PlmUQcNBSamdPJajwizzpcHO16gilNmIY0f8ACKmNk6JSJWY0axnyJ5zEDgoKWEEEq72LrYdLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5Qe-4jgbak-RCplF5sGRDLbVNlR-MPouicg37EiRJiZRTA-M0pXw4Cn30NSEcGqo5nL7vLIm9_-XpMDQp10okQwwoiYEhC-7jE428nqJs5ZVaWnl0ACyHz9P71_6M_32CVaQQ7bCC7n1_XwDvhBKUg_o_jdOFddjrFmkypRXP3i2PHYQSmukDTMpiu1M1V_WJCGv5QZODNlXiQG5_G9l_8DC6Vt8bCWigMrq4kUFkUkuwH579Ug-TDbYehmUyPlVyBm5EM79YQdMeM2JhZJWofLTFHrE9GodFQar8PdwvnRPTCC8mZOaMLMIffvjjMq5zzQJiFzHX3UYd_LwT90hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
با چند اقدام ساده، می‌توان از هدررفت آب جلوگیری کرد و به حفظ منابع آبی کشور کمک کرد.
🔸
بستن شیر آب هنگام مسواک زدن
🔸
کوتاه‌تر کردن زمان استحمام
🔸
رفع سریع نشتی شیرهای آب
🔸
استفاده از یک ظرف آب برای شستن میوه و سبزی
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/676703" target="_blank">📅 17:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676701">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b70a4d890.mp4?token=sON-VG3thSoL6C4Je5y_gPUnCsY3FwXpJph-hc1LlsKRt4zFzH9PSfqgINpvR6dWql9eHMNHpN_9wz7CiuyBYo9PrO2kbS1-g7kf6n-2rMdfZ_KH_hCrF-5ioxylp96ghqOrq4LzVhsCb7PcoQlSr6Txhg-2V6bcpl-aFvmXB-tSR_dPgckgyaKxdE7u7f2j8uywmojjW71wvLibKEb0QmErZjo6D5Y_LzgJ35LTlswS68yqcBrXQppcbV4IK3qhqWKkpCHF_xcZlwOApOx3Te8zEgIoCHDeYtcXPqDL_tP7Q5tu_L6JzTGypIx006K-9qju3GKuUEx1JdGrft0Ryw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b70a4d890.mp4?token=sON-VG3thSoL6C4Je5y_gPUnCsY3FwXpJph-hc1LlsKRt4zFzH9PSfqgINpvR6dWql9eHMNHpN_9wz7CiuyBYo9PrO2kbS1-g7kf6n-2rMdfZ_KH_hCrF-5ioxylp96ghqOrq4LzVhsCb7PcoQlSr6Txhg-2V6bcpl-aFvmXB-tSR_dPgckgyaKxdE7u7f2j8uywmojjW71wvLibKEb0QmErZjo6D5Y_LzgJ35LTlswS68yqcBrXQppcbV4IK3qhqWKkpCHF_xcZlwOApOx3Te8zEgIoCHDeYtcXPqDL_tP7Q5tu_L6JzTGypIx006K-9qju3GKuUEx1JdGrft0Ryw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنسن هوانگ: دوست دارم تقریباً در همه پروژه‌های ایلان ماسک مشارکت کنم
مدیرعامل انویدیا:
🔹
این شرکت سرمایه‌گذار xAI است و دپست‌ دارد در اغلب پروژه‌های ایلان ماسک مشارکت کند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/676701" target="_blank">📅 17:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676700">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از جنایت شب گذشته ترامپ در قشم/ حضور در خانه‌ای که شب گذشته در قشم هدف حمله موشکی آمریکا قرار گرفت/برخی از اهالی که خانه‌هایشان تخریب شده در سفر کربلا هستند
/ خبرفوری
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/676700" target="_blank">📅 17:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676699">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZYaKK0EqbDd-sMdYkoIaa1NghTKXLRRuQGxm_xKA4pulmewUOP-eHyzkzJf6LX-5vkapeJ5zeL_bwJDjgLI-hY20qSiPIJswc5UFbVS3fVPLvpe9SJLL5QuOUR61otdRK2ITtCdfPhLjpxMaheCSneMO7q092_a1rQv-hc9GNKU8HkZssMs2jkUoPFmfCK_Y2KfMq4tHB-dv2vnZsMMGZifjQB75Rh2W0X-5k9y7pTFh3iqEhsf7LtTWVQjFBfF32HLlJtaBl-NLDHcaCWbMI8ThWfnAag5ip5PrNsuybWv_GvA5CFkEHErX545TgaD-0eadtJCvQkIw8ukg0qP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام یک از موشک های ایرانی می توانند به خاک اوکراین برسند؟
🔹
بر اساس گزارش‌ پایگاه «دیفنس اکسپرس» و تحلیل‌ های نظامی غربی، ایران حداقل پنج نوع موشک بالستیک میان‌برد در اختیار دارد که از خاک خود می‌ تواند اهدافی در اوکراین را پوشش دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234300</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/676699" target="_blank">📅 17:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676698">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: با ملت و مقاومت عراق همبسته‌ایم
🔹
سید عبدالملک الحوثی در پی «تجاوز آمریکایی-سعودی» به عراق ابراز همدردی و تسلیت کرد، این اقدام را محکوم دانست و بر همبستگی کامل با ملت، نهادهای امنیتی و مجاهدان عراقی تأکید کرد.
🌍
تازه‌ترین خبرهای ایران…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/676698" target="_blank">📅 17:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676697">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAMQzpKg7p3s_IAYK6mzTj_gWcnAaUQM54mdFk4nKftuf9lNCcp_q9BoNX8QLE5ddCQEuei_tkPdFfyobIsN-5w10IsQRpKyhsBYfuWJlNJLRCaI49o34dvH_XbJ7QLQP9q3o9Sdk1fqXaQ2bcAS41Trz_UVQU-Wisq-JgFz1-5hTKC1vyebtSl35FWgs6GsDDZw0holiYcQt090ZrQUWeTi7ELo-cT9FSQyN69_vtFpYIgdDoGIBufJm8VHCVN3O3_COAw7e01YpUGD-ZZvxlg9ErVntm3epV21FjlhOZvuYlVi6GqIk2oPoG6HMySo8eedELFNWN0fYNtd5Ts-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنبور جواهر؛ شکارچی که سوسک‌ها را «زامبی» می‌کند
🔹
گونه‌ای از زنبورها به نام «زنبور جواهر» با تزریق مواد شیمیایی به دستگاه عصبی سوسک، قدرت تصمیم‌گیری و مقاومت را از او می‌گیرد.
🔹
این زنبور سپس سوسکِ مسخ‌شده را به لانه می‌برد تا لاروهایش از آن تغذیه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/676697" target="_blank">📅 17:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آمریکا: به فشار حداکثری علیه ایران ادامه می‌دهیم
🔹
سخنگوی وزارت امور خارجه آمریکا در مصاحبه با فاکس نیوز: ما به ادامه سیاست فشار حداکثری خود علیه ایران متعهد هستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/676694" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5687d130d.mp4?token=OrIxkZvYAK23X253P9ZoIuoXv-DIQg6TrutB06bFpd5TWLQVgh-ZYOFlC_dZ7_UzpegWzQRmFmvtKCS4j-x3ZYT9Lei4CuVA7658yRoIcYuxi7bFBquG7D3gu-usI4islMJUKDVstcwUoWCwu4OyH0B2p0QsdWd81EBxqIbxeLCYAtdOsKFIhgJAusct-VCLGC6pMTZPv2b5iNZJXNoaOfnbPmKg6N4NTTSgsRrvfqZjI1FpuERy1MqfIYoPjlWNPNmwzzvSmoeHfkM0PfbZRzDjp9PLyineJ3xM_OyKPeOsMx-cPBiJ-PUSn7iO6psyHvqVqEh2nsD5h6CRGqrAAogxjqH0Q-9cdS1LL7v8k1NJiFIqJaw-t-eikksPFRWvOcwhnbBD_iB52Mk-5HiG2ojr3BS45xXfjSPHa3iNKa0lH3FUPe1qFNkjA3hWyt-nX5918DlEy6vcSvO2QXpgTEXSDuJqZZIfPN1l_igqDUr4yOOSHtvdt6583KYR71nGTv5LPSNK7_kCWu-JWY_s3caM53r96ShxfGLT7iggdijaatFthoeY-8hX9lVlXGY0KPGFX60e_rBpFECMqrlU1pARGFYdQJdHuSgD3SUumXsQhEQGuCOuRAtftoM5K8W_JfRTBKOJgU-GXNL2sOPgMfFT46OVjJC8r5TFkUNXHZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5687d130d.mp4?token=OrIxkZvYAK23X253P9ZoIuoXv-DIQg6TrutB06bFpd5TWLQVgh-ZYOFlC_dZ7_UzpegWzQRmFmvtKCS4j-x3ZYT9Lei4CuVA7658yRoIcYuxi7bFBquG7D3gu-usI4islMJUKDVstcwUoWCwu4OyH0B2p0QsdWd81EBxqIbxeLCYAtdOsKFIhgJAusct-VCLGC6pMTZPv2b5iNZJXNoaOfnbPmKg6N4NTTSgsRrvfqZjI1FpuERy1MqfIYoPjlWNPNmwzzvSmoeHfkM0PfbZRzDjp9PLyineJ3xM_OyKPeOsMx-cPBiJ-PUSn7iO6psyHvqVqEh2nsD5h6CRGqrAAogxjqH0Q-9cdS1LL7v8k1NJiFIqJaw-t-eikksPFRWvOcwhnbBD_iB52Mk-5HiG2ojr3BS45xXfjSPHa3iNKa0lH3FUPe1qFNkjA3hWyt-nX5918DlEy6vcSvO2QXpgTEXSDuJqZZIfPN1l_igqDUr4yOOSHtvdt6583KYR71nGTv5LPSNK7_kCWu-JWY_s3caM53r96ShxfGLT7iggdijaatFthoeY-8hX9lVlXGY0KPGFX60e_rBpFECMqrlU1pARGFYdQJdHuSgD3SUumXsQhEQGuCOuRAtftoM5K8W_JfRTBKOJgU-GXNL2sOPgMfFT46OVjJC8r5TFkUNXHZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشگاه و حوادث دی ماه/ اساتیدِ زیرپتو، در حوادث دی‌ ماه سکوت کردند اما در خفا درگیر کمپین افزایش حقوق بودند!
/ تلویزیون اینترنتی مدار
این برنامه را در آپارات ببینید
👇
https://aparat.com/v/ocrv3ab
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/676693" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رهبر انصارالله: هدف دشمنان، تغییر چهره خاورمیانه و ساخت «اسرائیل بزرگ» است  سید عبدالملک الحوثی:
🔹
تجاوزات علیه ایران، لبنان و فلسطین در راستای حذف موانع طرح صهیونیستی در منطقه انجام می‌شود. وی همچنین هشدار داد نشانه‌های خطرناکی از آمادگی دشمن صهیونیستی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/676692" target="_blank">📅 16:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
رهبر انصارالله: هدف دشمنان، تغییر چهره خاورمیانه و ساخت «اسرائیل بزرگ» است
سید عبدالملک الحوثی:
🔹
تجاوزات علیه ایران، لبنان و فلسطین در راستای حذف موانع طرح صهیونیستی در منطقه انجام می‌شود. وی همچنین هشدار داد نشانه‌های خطرناکی از آمادگی دشمن صهیونیستی برای اجرای عملیات تخریبی در بخش‌هایی از مسجدالاقصی وجود دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/676691" target="_blank">📅 16:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/od9iw8AqwF7QJ-6JemH7ZIQyC2joJ7KsMW_yvX0b4BLk-HMldpVJV3yq2WZpdOPTAqRduWJ5Z_oP6oSOxrEePKvR0i_g1dI4SK25ojok5ylVrjjs5Oy1Xx0_V58tOLqa04nT17MdSkuB2XMrWxOO6ShLKjnFzzYb8acg4QpfpNr2IgWjeRzAjdCBa5ng5bvH_JdWkjjt3R9eXLxMlzBZlRcJm6QMBK395gesUuPwLynyEkDZJ_q79mh4RlBt4aFnCKnyCllQoNhvdtRse2jVi1CeSRdYVr0W6K50xWA1ql-ri7MxpQY9TkUKmvB5nBfGSLAQvnZQ_41zNWfoGGg6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۰.۳۲ دلار کاهش یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676690" target="_blank">📅 16:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7b788314.mp4?token=M4xsDNUTrLqiTr1DTdTbi_VTpZ3qPFfqBS_Vo01jJ4xycEA_cm1HzuQGz1aC0FM8rPYtAWucNBalg3-zKScwQo7h5SVgLpr07mWETYhiEyfeKFk4apc8mTw17_eiP7pDhZmTyQQ93u51irTY0CIZXKCV4wi4y8gvy-A-ijz5-i07Q1j5vjpDKowB_v6kVDB_ppcXH8bBqQ0Arkg8V_KIvjTQ2AeBAlEz40i_bwvWD-rNcVKZEjgLKGf-q2bSBHJRFwrbF3dQa2HyjzHTzCneQ_qF83VnC0n5wgWoWouUasVaJorAc75aaXyQaXZlI9NOi5ypzZFZm_YF0Kv-NUn7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7b788314.mp4?token=M4xsDNUTrLqiTr1DTdTbi_VTpZ3qPFfqBS_Vo01jJ4xycEA_cm1HzuQGz1aC0FM8rPYtAWucNBalg3-zKScwQo7h5SVgLpr07mWETYhiEyfeKFk4apc8mTw17_eiP7pDhZmTyQQ93u51irTY0CIZXKCV4wi4y8gvy-A-ijz5-i07Q1j5vjpDKowB_v6kVDB_ppcXH8bBqQ0Arkg8V_KIvjTQ2AeBAlEz40i_bwvWD-rNcVKZEjgLKGf-q2bSBHJRFwrbF3dQa2HyjzHTzCneQ_qF83VnC0n5wgWoWouUasVaJorAc75aaXyQaXZlI9NOi5ypzZFZm_YF0Kv-NUn7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۶: دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/676689" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
راز نگهداری خودرو بعد از باران؛ نکاتی که بیشتر راننده‌ها نمی‌دانند
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676688" target="_blank">📅 16:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQgRg1SYZW403jMK67uXC5ZP1hvPTh9D04jG6liM94AMbrfnjtBZZ0cv_agmoKYjHPT6tPMnaX8Qy05B6hnkXVwPSMZWmD1mb6pBmk5_TnhXJZJpGWT-Cp6kfVPcnWWgQKkG8MFwcMgZSpgqSoo_EBKG6BPU5WFevAQdKGQjP4_qlh-znP40ujLb7xblA8Mf63p0rxdorhSr0IhstMPIXnFBAPCbZOvNUd8WXbmecB7jJOiwkboki1AcO7SsZiAyjdP8iNNl0OKF5AMeUI8x-hnh82-rwO_Y2Qo18iT5n00o_pFxiewoqlFDwd02AtutUb-3lvEQDcdzjFUl9jAcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات ضربات پهپادی موشکی عملیات نصر ۲ در کویت و اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/676687" target="_blank">📅 16:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7cc9288c.mp4?token=u-L-VxWU9lZaWupNYY7NCgQ52h2n14bI2WoulVGWBk6tGp2jSViOpit4LLpYYDjDxNa-jiPgDE5dOuiJOxbO7ZdGMelopvlI7bitXfH40x4ic025ImdjSCB56ra9SKgE99-e4wf9bn0CmqB3d2dR6KTIQh9iITxPyYo1L1WksFZePCigAMqGUAGfUAoRynoX339TXidnhEVJ_vx0kuVy1jc_fPc_RKL2xpoMsgo2W2HWLjgaG7BFJz7pf9f9uMXMc1nR0EjFjM-zgv7qNpHy64SB-STH7gqKeuC3dQr_u6rUEIiin9am-yTUBN_Rb8bWUFlwlfUZwSFwOVpJZrjJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7cc9288c.mp4?token=u-L-VxWU9lZaWupNYY7NCgQ52h2n14bI2WoulVGWBk6tGp2jSViOpit4LLpYYDjDxNa-jiPgDE5dOuiJOxbO7ZdGMelopvlI7bitXfH40x4ic025ImdjSCB56ra9SKgE99-e4wf9bn0CmqB3d2dR6KTIQh9iITxPyYo1L1WksFZePCigAMqGUAGfUAoRynoX339TXidnhEVJ_vx0kuVy1jc_fPc_RKL2xpoMsgo2W2HWLjgaG7BFJz7pf9f9uMXMc1nR0EjFjM-zgv7qNpHy64SB-STH7gqKeuC3dQr_u6rUEIiin9am-yTUBN_Rb8bWUFlwlfUZwSFwOVpJZrjJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر آخر الزمانی از آتش سوزی جنگل‌ها در یونان
🔹
در پی آتش‌سوزی جنگلی در جزیره کرت یونان، صدها گردشگر از مناطق مرکزی و نواحی توریستی تخلیه شدند؛ شدت باد نیز باعث گسترش سریع شعله‌ها به سمت اقامتگاه‌ها و مراکز تفریحی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/676686" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
جدید‌ترین تصاویر از حمله به بندر دمیاط در مصر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/676685" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۶: دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی از منطقه را مطالبه می نمائید.
🔹
همگام با شما، فرزندانتان در نیروی هوافضا و نیروی زمینی سپاه پاسداران انقلاب اسلامی در میدان، نبرد با دشمن متجاوز را با قدرت و شجاعت ادامه می دهند.
🔹
صبح امروز در ادامه عملیات نصر ۲ و تنبیه متجاوز با حمله به پایگاه هوایی آمریکا در علی السالم، دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی را به آتش کشیده و منهدم کردند.
🔹
مردم مسلمان کویت بدانند، تنبیه متجاوز تا پایان دادن به غارت ثروت‌ها و منابع ملی مسلمانان و اخراج اشغالگران و غارتگران آمریکایی از منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/676684" target="_blank">📅 16:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETljda1B2iC6Iwi0FvUcAon03eAWtUxHpNpQuaUl4Bt-myItVps7pFssMvaaPtW3o_1nNUFweS3Xi2TPcfsVnL6nIVgik2XU-sDCxzgK67b8WBzoVlPhoz2MfQxUGEY0hi4OGHQBMzjyH2lGbtvf7wZ-_MViAJmuKl3kJpPh0rpVH0j4onWBi2M3rUaeNAXbu_IGdQtfJFek0fE16FBmfKcwnVEQB_W50CclWRF4E5Y1GAuLR1GKqwDnZbNGyFVyyqHpNZ4a_Dm67UjfMZcY7ctEv_2y5u7ckA_eJDzAD50TIJYtmWKk5HDmzn-PzMLs9SISxbFgLqVgb-k-WYfUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBLrZUP8BTTj6NOSQgIu8X0H5qk7rf0QLpSYmBW_IBlUwbQXsMW7KUhRVBDKl07HHjWIPWIq_nG5nRXS-6LWsEJGx-m1m9olvTTW23OuvM3nSDbXKh5KUcATZMtyQIZOj91ER6XchGTdnD_wyHMRdsUbSIpkSNt6XC-_MrmbcDJMQ0_OumV85nRCg6nASt-5x0H4nPapKhkzcubE8b8I3ig2naqYddx5DkdMBMKCpAfSIbtupT-HQpUnpAFOeJkoPBUHH6pfUuyzhOSaKgqyqfvsxKIwAuh6RqnY51t5y82bZvxUonFe8FDsoOton7RdSNTzuoUdyMQ2iG8cyl3EUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaieIU5chDfnwieFYCpZnW7s4F16MPvAWU_2XqZGahzepplEa--9i26W-VNo_unRFlnDRXqvHsng0Ve6gZrsIig4s3zDvvu3VZhUoD2WiYA4BmVuLrJI8PuPWIPcxvCAVQm8fj4E5CUti4AYjMxVlDM_oopxloxOKympsuIg8gc0COpVzKz4ZXrVangkzg4xX1BR_QNHvffCZpTS3rfO3imKxkjUiZSIlCtllY07uyu9w17LxcEzFJ_DCmlaYJB8HEJtKK4UqmnZjDH-yF8AT-ksi4lI4TQzMapNObPrWv4L-14Qh3NEfk7UQq4YNaCknLk86WT44DAF6orGJ5l68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jH48vkXBCmHX0HqgUSNwJiodJuxvswIGz1IwTlWFkPzDSN4pp0lX3ZQM8sZnQV6p_yxvgSS8Ejj50n8VQgcOZa6RkXNNNXKZ1ynbM1DUIiobza9aHnePQHEUphTMM0uAeBeDUgjY4hWsFHOBeh-cVhhcdEFV91KgGyzoZW0sljQb-jjioejvgeWWAqf3jl97J6S5cPfkFTwFfzM01eMmOUEprficPaOGxI0OAO7hwTChHPFH0UDGjF91mi7ie4_pneYZ9sqDkTvT3ZwH-po11Wwohbk01DpyrYzm15EmMfNfs3fGZwybV3TBBsHRAs-iuKBFbat4ikhjlxMkuvGSBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر علاقمند به سرمایه‌گذاری روی سهام هستید، این ویدئو رو از دست ندید #دارایی_هوشمند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/676680" target="_blank">📅 16:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cef79cdb.mp4?token=NNU_VeMNC1zARNppLSge7f4ouGQO7D4puZW4hJuFFGAdyjDNfx9DEyihrhyjGUo_oZpFap4URD5ZfoJNgSiYQHw3sdCrRgSw-XgMocohWW1bLup926SgpDYvuclx4cq3NREjOHax9wu7OmfvWBh4Fk7shTqfYoSPdBlp6BiK9DgrEFnXoZD4u_CESPgLAcLowgJkEx6RyQpkbcu8aMlUTqp343qVtKsdSKek2sF9NPj8IlaYGvw8zCGGNgnEi8KYH3bLHuxZJAahB5L6_m73MCXOrsk6ILNqsMGiJuTyTOnkBIT5ztBFBf8U35uDdKNZUmojFu3ccm9WlEQTUgFaiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cef79cdb.mp4?token=NNU_VeMNC1zARNppLSge7f4ouGQO7D4puZW4hJuFFGAdyjDNfx9DEyihrhyjGUo_oZpFap4URD5ZfoJNgSiYQHw3sdCrRgSw-XgMocohWW1bLup926SgpDYvuclx4cq3NREjOHax9wu7OmfvWBh4Fk7shTqfYoSPdBlp6BiK9DgrEFnXoZD4u_CESPgLAcLowgJkEx6RyQpkbcu8aMlUTqp343qVtKsdSKek2sF9NPj8IlaYGvw8zCGGNgnEi8KYH3bLHuxZJAahB5L6_m73MCXOrsk6ILNqsMGiJuTyTOnkBIT5ztBFBf8U35uDdKNZUmojFu3ccm9WlEQTUgFaiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا %𝟖𝟎 تخفیف + هدیه
در مهمانی 𝟏𝟎 سالگی «چرم مَنطِـ»
𝟓𝟎% تخفیف کالای اول
𝟕𝟎% کالای دوم
𝟖𝟎% کالای سوم
🔥
➕
𝟑,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان
«هدیه اسنپ‌پی» فقط تا جمعه
آدرس شعب و سایت
👇🏻
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/676679" target="_blank">📅 16:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676678">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a32a231.mp4?token=RKGEQssOo_EY32O8_kiaHW9WO8mhPH2Wev634154SiOEPC7dNuQFtDJnMdt7lYttctr-qpMbxb42LWtYeRZB0nZ9E4w19PxGmoha7FFAp9b_EhAHdtmqDL6txUA_iice_3jAK-KrId3sW3DIFEWvtGcucAJRlR34UEORwfuKWAqNwYCMSFP8TO5Wn1ston7AfwILTYVdeWA0y6hdKAHY5H_9QaPo3QEpWok8ZeAv6FfgEjY4qbpNyWSNLYWHy2UWxP7haZLPF_PzIV8n1xt9RD2hkxgDpjmrhgio3n0kGg0PMhHqf-OpE9mchT8W_xqvJKScY2YzIzwCnrrPEYmnn6J44gUh4aphrs2fuvEHYZ7GW4pO_vmQjpDNewX6yuR--tWIQF2XAPa68dbkZZ3fkQYZrIm4zrf-l38Z6UA5PuCglIW_G3lgKCfKoHArhsDwJA3K5alhqhrYL0V8EA5CQoEBdEoYVp1RRFX6Pdj32bUFv4h_HKC3z0P5EaRnyb3UM6eZQteNSEmrRGehSxLq64ryaqhwNl4kO-9LlwMA73JaFbCq_hvY13lPSOQ8D5kkL7q2BASDXQbKDr3norcKN5WxMIEixkr5Xk0jPROMgXhfRY-9ipa72q3rbO3YTk5MQvnw86C0XLME4evdyIutEuPGcuxZM4_3_504lS4Tt0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a32a231.mp4?token=RKGEQssOo_EY32O8_kiaHW9WO8mhPH2Wev634154SiOEPC7dNuQFtDJnMdt7lYttctr-qpMbxb42LWtYeRZB0nZ9E4w19PxGmoha7FFAp9b_EhAHdtmqDL6txUA_iice_3jAK-KrId3sW3DIFEWvtGcucAJRlR34UEORwfuKWAqNwYCMSFP8TO5Wn1ston7AfwILTYVdeWA0y6hdKAHY5H_9QaPo3QEpWok8ZeAv6FfgEjY4qbpNyWSNLYWHy2UWxP7haZLPF_PzIV8n1xt9RD2hkxgDpjmrhgio3n0kGg0PMhHqf-OpE9mchT8W_xqvJKScY2YzIzwCnrrPEYmnn6J44gUh4aphrs2fuvEHYZ7GW4pO_vmQjpDNewX6yuR--tWIQF2XAPa68dbkZZ3fkQYZrIm4zrf-l38Z6UA5PuCglIW_G3lgKCfKoHArhsDwJA3K5alhqhrYL0V8EA5CQoEBdEoYVp1RRFX6Pdj32bUFv4h_HKC3z0P5EaRnyb3UM6eZQteNSEmrRGehSxLq64ryaqhwNl4kO-9LlwMA73JaFbCq_hvY13lPSOQ8D5kkL7q2BASDXQbKDr3norcKN5WxMIEixkr5Xk0jPROMgXhfRY-9ipa72q3rbO3YTk5MQvnw86C0XLME4evdyIutEuPGcuxZM4_3_504lS4Tt0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند عالی برای گره زدن
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/676678" target="_blank">📅 16:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
هشدار عراقچی به بلغارستان درباره استقرار هواپیماهای نظامی آمریکا در «بزمر»
🔹
عراقچی در تماس با وزیر خارجه بلغارستان، موافقت صوفیه با استقرار هواپیماهای نظامی آمریکا در پایگاه «بزمر» برای پشتیبانی عملیات را «محکوم و غیرقابل‌قبول» خواند و خواستار تجدیدنظر فوری شد؛ او با استناد به قطعنامه ۳۳۱۴ سازمان ملل، واگذاری قلمرو برای اقدام تجاوزکارانه را مصداق «تجاوز» دانست و هشدار داد هر طرفِ مشارکت‌کننده در حمله به ایران باید مسئولیت تبعات را بپذیرد.
🔹
وزیر خارجه بلغارستان گفت کشورش قصد مشارکت در جنگ ندارد و بر دیپلماسی و کاهش تنش تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/676677" target="_blank">📅 16:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676676">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455426b2fa.mp4?token=tqMYkbepA71k0nPhdrIuULObhrxkLdTAuA-WQEGHfHe6cx9nIOIh--FWUUVBqs2rIeY5dyZZuv55fVot66Stws8kpQ3mB3sb5YGrRSYZHlhKKJc3FVx346gzfmf8dD5-6JlejNUGXnVWzzSrqrjLx0M9D_DIS6t-vQlVHpoWn5KVJPb1OS7HxOVcx_iTAVpSe018f2I_XxrNF-5x5d7lT3qjqCwx9wZBooJdkBFFQOEMXq_72f_Y6r81ksPJpvGjGeI1LR3wd-JjP0MCHTNmVLskztY_yTEl-nP9C9xifnIBu5Pyd7TjrUqXKBDSrfD2S725XnbFpLCJhHeaF6VaBUnxd-QZs9dZs1sn8PjJMNDjytqAsRAe2e-QaPmkeNhxtQPWjoIPZTYIpeLMxwu3KB_vJr9wURiQ6mB9X1Lpdbogfgyu_luOXpv0M-exRTwh-L3bOfOm2xlCZugxLoJS2mpqoGqVxzG8npfi6LZlC-IFbkl_Tk98GskZB53L9OCGTytbu_Dhne6OzkoMCaWrVJTMnpdEb49tXbHymadSWGlLU8d9VPfqCh7rpuBQZB7-ANXrEXUAVXi56XcGHvp4hRX8t7b-aNAdz3uFSLavDZm7Lh0oYovV1IWCcgRgHo5M6v-TYtB9SYDs1_A-iiMH3CvqJziqAWXwxzeACF8QnrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455426b2fa.mp4?token=tqMYkbepA71k0nPhdrIuULObhrxkLdTAuA-WQEGHfHe6cx9nIOIh--FWUUVBqs2rIeY5dyZZuv55fVot66Stws8kpQ3mB3sb5YGrRSYZHlhKKJc3FVx346gzfmf8dD5-6JlejNUGXnVWzzSrqrjLx0M9D_DIS6t-vQlVHpoWn5KVJPb1OS7HxOVcx_iTAVpSe018f2I_XxrNF-5x5d7lT3qjqCwx9wZBooJdkBFFQOEMXq_72f_Y6r81ksPJpvGjGeI1LR3wd-JjP0MCHTNmVLskztY_yTEl-nP9C9xifnIBu5Pyd7TjrUqXKBDSrfD2S725XnbFpLCJhHeaF6VaBUnxd-QZs9dZs1sn8PjJMNDjytqAsRAe2e-QaPmkeNhxtQPWjoIPZTYIpeLMxwu3KB_vJr9wURiQ6mB9X1Lpdbogfgyu_luOXpv0M-exRTwh-L3bOfOm2xlCZugxLoJS2mpqoGqVxzG8npfi6LZlC-IFbkl_Tk98GskZB53L9OCGTytbu_Dhne6OzkoMCaWrVJTMnpdEb49tXbHymadSWGlLU8d9VPfqCh7rpuBQZB7-ANXrEXUAVXi56XcGHvp4hRX8t7b-aNAdz3uFSLavDZm7Lh0oYovV1IWCcgRgHo5M6v-TYtB9SYDs1_A-iiMH3CvqJziqAWXwxzeACF8QnrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر قطره آب مهم است
💧
🔹
شیر آب را بی‌دلیل باز نگذاریم و زمان استحمام را کوتاه کنیم. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/676676" target="_blank">📅 16:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676675">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نشست اضطراری وزیر دفاع عربستان با ترامپ و ونس در کاخ سفید
🔹
وزیر دفاع عربستان در کاخ سفید با رئیس جمهور آمریکا و معاون اودرباره تحولات منطقه به ویژه تنش فعلی با ایران گفتگو کرد.
🔹
گفته شده خالد در دیدار حامل پیامی از سوی محمد بن سلمان، ولی عهد عربستان بود.…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/676675" target="_blank">📅 16:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676674">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6179d2b13.mp4?token=KX43iOI6FIjh5TiV454bArSMtVvTw0CWL-hkZYVPqRwY-rvAv6RSftPe5lMyiYPr4TMFqnjNX2_gTb2g4tDd7M2JFGs_8XREEmLVU-gdMpp3sn8L_JaIkF8DRdVoXiaodukKfXoBpBuzQBCUhCURy8jozlEweKCb7zwqxbB7r7-U-gHjCDcKSF44dyjodDUat2ouFp6InvqZtC73EujHdAEot7sHvrm2g61IyoOK19ZpmRs7zQherwt7bGfiCPuQnd6vV_bZWNYDrWp8vpArtmuWyCb_7rpBpXErUP1LBX5-m5fEKpzoRuLUIUd61VEA0cGmwX7rlJfhDBiaoh9zgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6179d2b13.mp4?token=KX43iOI6FIjh5TiV454bArSMtVvTw0CWL-hkZYVPqRwY-rvAv6RSftPe5lMyiYPr4TMFqnjNX2_gTb2g4tDd7M2JFGs_8XREEmLVU-gdMpp3sn8L_JaIkF8DRdVoXiaodukKfXoBpBuzQBCUhCURy8jozlEweKCb7zwqxbB7r7-U-gHjCDcKSF44dyjodDUat2ouFp6InvqZtC73EujHdAEot7sHvrm2g61IyoOK19ZpmRs7zQherwt7bGfiCPuQnd6vV_bZWNYDrWp8vpArtmuWyCb_7rpBpXErUP1LBX5-m5fEKpzoRuLUIUd61VEA0cGmwX7rlJfhDBiaoh9zgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند انفجار شدید اربیل عراق را لرزاند
🔹
به گزارش، شبکه اخبار عراق اعلام کرد که پس از شنیده شدن صدای این انفجارها، ستون‌های آتش و دود از منطقه قسری در اربیل به آسمان برخاسته است.
🔹
براساس اعلام رسانه‌های عراقی، هم اکنون سامانه‌های پدافندی کنسولگری آمریکا در…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/676674" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676673">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مهارت برای آینده چیست؟</h4>
<ul>
<li>✓ هوش مصنوعی و کار با ابزارهای AI</li>
<li>✓ زبان انگلیسی</li>
<li>✓ برنامه‌نویسی</li>
<li>✓ مذاکره و مهارت‌های ارتباطی</li>
<li>✓ مدیریت مالی و سرمایه‌گذاری</li>
<li>✓ خلاقیت و تولید محتوا</li>
<li>✓ کارآفرینی و راه‌اندازی کسب‌وکار</li>
<li>✓ سایر</li>
</ul>
</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/676673" target="_blank">📅 15:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1gq08bVWL0XahT6yhTv6nJz_EbIZBZRoiJp19-Q0xRbIpKoYHEnGKhs_2oC-254h6L0THBI8fnp6BS8cOqRnqsPhMcD6hEcQSiATzro26xivQLqJZxl7hYzXLjagh6DMgovtXCwHOs7YLHIDU7buEYez6PmJZ2_n53BC3053aVSn5y98bCkp0tgOaI8M8CVgGqKXHpHeySkzp8LxpI3XMfqHTIKVL8RZmwRnXtyL8Hki3UhyMqIH-zsMt4V7SV8a7PFVocBV1svK9IZJxhqW0Md90zmYGvG9ty8qilgb-huRjJmnW1JkXs7MqFB746yQOufwapmDsOoqoi9AeXS8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مدیریت تنگه هرمز واجب و ضروری است؟
🔹
از گلوگاه تنگه هرمز، علاوه بر نفت، حدود ۲۰٪ گاز طبیعی، ۳۰٪ کود شیمیایی و ۴۲٪ غلات جهان نیز عبور می‌کند.
🔹
اگر ایران می‌خواهد سایه جنگ را از سر خود دور کند و اقتصادی بادوام و بازدارنده بسازد، باید نقش خود را در مدیریت این گلوگاه تثبیت کند؛ چون هرمز هم ابزار قدرت است، هم می‌تواند برای اقتصاد ایران عایدی و جایگاه تازه ایجاد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/676672" target="_blank">📅 15:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9d7f24ea.mp4?token=B7z0cqhUhGwqysKacCpyF4WI-0pfnk-p3Su5CXXSbQOccsLQUvyqaDfrax_M3l4XVnz8oxrxw5z98SmavEKkpIEg3dYV0w0kANdH82_TezU6H2mssx-_gLIJ3pWilByOi6gXZJ2IoyoZ66dhtAmR9Gg-CwtFN8-VSzpf-NcqS4CR1YwMq61IOwVvVowoN1-OX-IIWJsxtYvjM2hfymg9SNw0l3REVITp_JSQRX2ZFm34iV_eszWttvBYjh0Ak66XcQtE6e36fc_aLgIEAV5paXOCEO4CLCkjPPTHV3mwchFAxsFImCOsgSqgmw5ooIJQN1H0pngpFRylQTAGumvGVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9d7f24ea.mp4?token=B7z0cqhUhGwqysKacCpyF4WI-0pfnk-p3Su5CXXSbQOccsLQUvyqaDfrax_M3l4XVnz8oxrxw5z98SmavEKkpIEg3dYV0w0kANdH82_TezU6H2mssx-_gLIJ3pWilByOi6gXZJ2IoyoZ66dhtAmR9Gg-CwtFN8-VSzpf-NcqS4CR1YwMq61IOwVvVowoN1-OX-IIWJsxtYvjM2hfymg9SNw0l3REVITp_JSQRX2ZFm34iV_eszWttvBYjh0Ak66XcQtE6e36fc_aLgIEAV5paXOCEO4CLCkjPPTHV3mwchFAxsFImCOsgSqgmw5ooIJQN1H0pngpFRylQTAGumvGVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهره‌های رسانه‌ای و هنری ایران در عراق فریاد مرگ بر آمریکا سر دادند
🔹
در حاشیه حضور کاروان اهالی رسانه در اربعین حسینی، شعار لبیک یا خامنه‌ای و مرگ بر آمریکا سر داده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/676671" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676670">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quUSHcd7qmk2k_-Hn7IS850INgw8erd0nQ8XtM9AnOh_t-SgVIbnpDkfUxeCrVpvdYWFmwcv1aHZQp7T4UWU9v4qFenrg50Kt6JDWuyLyoHwDfmzqTRD6AmXJvfBDjeGJi_JTQ2JPlfAXbvxc53gQnJo06Y6uW3W6hyqaI8IsGwoU5lCF0_FPWHEZZdhSyVJF1iJCgnCDoZ53DsZxcz0XTvTvbCmeWrzZWpte9XXCPlYp6_ODTBQvK-B4dokZLJ2_mNX08D9M0yi0_cYVsHhDonOlTNZ5HpEnlWp2lQjifT9s-YWn47rSa9QSF7n5FUSSGbDqT6g7FCOxPCnV966Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/676670" target="_blank">📅 15:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676669">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtpkW6UoCjtjRNo6QHwyPzDW8poaQR3DzXyDxxADnXvSBrx24Oz1UTyTpfptAGrPY_EgE5kTtXs9EMuy011jGEd9giaHwnm2c2jFn8A-8pcXR314QumV6T9VWCvNq8QFwQPNE5HXHaqZS3TyXmsleIosiL7CkYXGLZWYFAK-KALkKdJFdWIkifzzlsTKkF9pifYQjYr_5oL1Jk8HqEbuTIIGIZx4pS1llottvLnuM-sPisDrCepXm_zOG37nvoeFOme3cz4jF7IKk7NZ3kXDwIzz63qmol7lPuQH0A2spGL4yUAaw8wY3ct2-7cMsqlJT_gIU-FnipmNoQq6n-WDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزبان باشیم
🔹
هر قدم در مسیر اربعین، داستانی از عشق، ایثار و میهمان‌نوازی است. پویش «میزبان باشیم» از سوی هیئت قرار، بستری برای به تصویر کشیدن لحظه‌های ناب خدمت عاشقانه شما به زائران حسینی است.
🔸
تصاویر  خود را  با ما به اشتراک بگذارید
👇
@Ertebat_gharar
#میزبان_باشیم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/676669" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676668">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ba4faef6.mp4?token=TyRPbSwrtRjoBEW98_dbxneill5roHpokkfefshs2aoV0-SD5a-F2x_iTIH3pGmV6aDKIFfOR3yYvU7grlPnuwssJN5y5UReyF-6QtR-uUygeNyJIYED9tfe65VRI6mR9XJM9IUBA_zbMEV8JNkvx04qLJ0L49qL3sQk76xVhWjSNeZSLITM2EBayTg1Hpom67sgzMJ4QF4dXuQe3xxe7uKowNIcQQ-jORqjIRrw1l0Sz_FyYXQw21V8XkJZ8rXGXCT1B9dELv-2Gn6H7-paKKYy-o0eg4ORbOQHmsvvwmKYVpxtAM6xkMZfy9XTMo4psC0e68fc8sToGvomsN6Ifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ba4faef6.mp4?token=TyRPbSwrtRjoBEW98_dbxneill5roHpokkfefshs2aoV0-SD5a-F2x_iTIH3pGmV6aDKIFfOR3yYvU7grlPnuwssJN5y5UReyF-6QtR-uUygeNyJIYED9tfe65VRI6mR9XJM9IUBA_zbMEV8JNkvx04qLJ0L49qL3sQk76xVhWjSNeZSLITM2EBayTg1Hpom67sgzMJ4QF4dXuQe3xxe7uKowNIcQQ-jORqjIRrw1l0Sz_FyYXQw21V8XkJZ8rXGXCT1B9dELv-2Gn6H7-paKKYy-o0eg4ORbOQHmsvvwmKYVpxtAM6xkMZfy9XTMo4psC0e68fc8sToGvomsN6Ifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرسش‌های خبرنگار رویترز از رضا پهلوی درباره ادعای رهبری دولت انتقالی
خبرنگار رویترز خطاب به پهلوی:
🔹
شما فرزند آخرین پادشاهی هستید که در ۴۸ سال گذشته هرگز پا به ایران نگذاشته و پدرتان نیز پس از یک قیام مردمی علیه حکومت خودکامه‌اش تبعید شد.
🔹
شما چه صلاحیتی دارید که یک دولت انتقالی را در ایران رهبری کنید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/676668" target="_blank">📅 15:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676667">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt3lcWyG5xD8-6nC_bWSzs3D8k5U5_SBs0TaAD89mlvB_qh9doiGmz3Siv1azt1CLg6A18uU8PFdgpq2oNvourtruiVrHL5-CsvRB35p1gojfqJS-C3YuUafB72EbKQQ2kbQJPzuGsFvuxECu-utNMqE5i1x9txOirE1nPEQMigVqdSRmMbQDMbfY6mEGfKykHLeeUsrcWvZ7vs3Nv8GEGcCcu16UCayvT_940AjVI1Hmnq1IQv_EEayJlIz_A6_k46ifsZtxZA5CyaFW3cYCWQlfuXWmDX_Y2PnHBVy_esYQu3-LQpEfBwTgPX7abm6Kq2HFcQSVPmw-IEHOfuF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شورش در پایگاه «سدِه تیمان»؛ خروج ۱۰۰ نظامی و خروج گردان از چرخه عملیاتی
رسانه‌های عبری:
🔹
حدود ۱۰۰ سرباز گردان «تسابار» (تیپ گعواتی) در پی اختلاف با فرمانده خود، سلاح‌ها را رها کرده و پایگاه را ترک کردند؛ این اقدام، یگانِ در آستانه اعزام به غزه را از توان عملیاتی انداخته است./ خبرفوری
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/676667" target="_blank">📅 15:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bec21e8e4.mp4?token=AgVK4NGUJZhz46doIJvrpWBp0-qhZo7Fw42a4BUztyymQIbTvSA70CNmMkAzKLLLWM4VQqFxWD3W9qi7AonhfZG9QhIwZqeyfCFzRx3Q0FuydqtC8yHXs3MxUepxlIX6T1enLkWZRjUX15BRsXbwOiWJBfVOUXdyUplbx8AUKQcQefIX2LfL7fnyg9LLcXtSa9AuVKthWuZI7VGDLI7smIyb30bvqxEvqi85y0lXlZlhwoeVXVkBRhkDFbhswgZA791AAt9_D0y_3kntRXXqKkCcbvNDCkyyz7STpU-uWEnokvEcWWC2p-vsQMEBARw-hX5u573dyOZeEyKWCh00-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bec21e8e4.mp4?token=AgVK4NGUJZhz46doIJvrpWBp0-qhZo7Fw42a4BUztyymQIbTvSA70CNmMkAzKLLLWM4VQqFxWD3W9qi7AonhfZG9QhIwZqeyfCFzRx3Q0FuydqtC8yHXs3MxUepxlIX6T1enLkWZRjUX15BRsXbwOiWJBfVOUXdyUplbx8AUKQcQefIX2LfL7fnyg9LLcXtSa9AuVKthWuZI7VGDLI7smIyb30bvqxEvqi85y0lXlZlhwoeVXVkBRhkDFbhswgZA791AAt9_D0y_3kntRXXqKkCcbvNDCkyyz7STpU-uWEnokvEcWWC2p-vsQMEBARw-hX5u573dyOZeEyKWCh00-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظامیان صهیونیست با زمین گذاشتن سلاح، پایگاه خود را ترک کردند
ارتش تروریستی اسرائیل:
🔹
تعدادی از نیروهای یک گردان رزمی بدون مجوز فرماندهان، پایگاه خود را ترک کرده‌اند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/676665" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انتخابات شوراها در پاییز برگزار می‌شود
کامران پولادی، عضو کمیسیون شوراها و امور داخلی مجلس در
#گفتگو
با خبرفوری:
🔹
انتخابات شوراهای اسلامی شهر و روستا ان‌شاءالله در فصل پاییز برگزار خواهد شد و رایزنی‌های اولیه برای تعیین تاریخ دقیق انجام شده است.
🔹
انتخابات تناسبی شوراها نیز ابتدا در تهران به‌عنوان پایلوت اجرا می‌شود تا احزاب و گروه‌های سیاسی فعال‌تر شده و حضور مستمر در عرصه مدیریت شهری داشته باشند و زمینه‌ساز انتخاب شهردارانی توانمند و کاربلد شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/676663" target="_blank">📅 15:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
اولین واکنش الحشدالشعبی به حملات هوایی آمریکا و عربستان سعودی  الحشدالشعبی در بیانیه رسمی اعلام کرد:
🔹
صبح امروز چند پایگاه رسمی سازمان الحشد الشعبی در نقاط مختلف عراق، هدف حملات تروریستی نیروهای آمریکایی و عربستانی قرار گرفت. بر اساس اطلاعات اولیه، این…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/676662" target="_blank">📅 15:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07805a2c36.mp4?token=j_sgUA0AJH7qXQxY-DC6lKYzGPAx7d1YUBmyKY_Gk2EQOaNYcLUqzeFe_i8ZnTDQXZvBbsjTLsDfeeEKmdzhAnZEhtmayBZ3gwrujwhrfSN5T2vG03bxmqvb0DGhU52XyTy3Zzh8xsW1U5s1FQ10NJszgUBaubrgzTNned_RjOfgoN-oQBbXyZ-UPFTEF5Z2kNqw2rFlIgbYWl0bYbjFRaEFwGkVxh5WMPcMunnRxmK-YKG1xBSMlM3ZfeC3oyXBIzrcCoUfe43U9zi0OuqmF0mC8EUZrHHFMkVPUsbBMAjDXkDXf_FsPy8xvA6I_L3U2cagE0RptjYsJHnmGno0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07805a2c36.mp4?token=j_sgUA0AJH7qXQxY-DC6lKYzGPAx7d1YUBmyKY_Gk2EQOaNYcLUqzeFe_i8ZnTDQXZvBbsjTLsDfeeEKmdzhAnZEhtmayBZ3gwrujwhrfSN5T2vG03bxmqvb0DGhU52XyTy3Zzh8xsW1U5s1FQ10NJszgUBaubrgzTNned_RjOfgoN-oQBbXyZ-UPFTEF5Z2kNqw2rFlIgbYWl0bYbjFRaEFwGkVxh5WMPcMunnRxmK-YKG1xBSMlM3ZfeC3oyXBIzrcCoUfe43U9zi0OuqmF0mC8EUZrHHFMkVPUsbBMAjDXkDXf_FsPy8xvA6I_L3U2cagE0RptjYsJHnmGno0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندی برنهام به عنوان نخست‌وزیر بریتانیا منصوب شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/676661" target="_blank">📅 15:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تیزر قسمت شانزدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید حجت امیر واقفی که در طی  عملیات جنگ با داعش در سوریه، مجروح شده و بعد از انتقال به بیمارستان، روح ایشان توسط همراهی چند نفر به آسمان عروج کرده و تلاش چند باره روح برای اثبات زنده بودن به نزدیکان، بی‌نتیجه می‌ماند و همچنین ایشان شاهد صحرای عظیم مملو از جمعیتی منتظر در جلوی یک میز برای حسابرسی شده و با اشاره یک هیبت نورانی ایشان بدون حسابرسی وارد دریچه‌ای به سمت زیبایی‌هایی وصف‌ناپذیر می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید حجت امیرواقفی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/676660" target="_blank">📅 15:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نخستین کشتی حامل گاز قطر از تنگه هرمز عبور کرد
🔹
داده‌های کپلر و LSEG نشان می‌دهد یک نفتکش حامل گاز طبیعی مایع متعلق به «قطر انرژی» شب گذشته از تنگه هرمز خارج شده است؛ این نخستین عبور ثبت‌شده از این آبراه از ۱۱ ژوئیه تاکنون است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/676659" target="_blank">📅 14:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5wH0kvNf7cywgKXMFshPe2kzIBwpPRL8PpvG4gSVUK43O3xJRFlTieXxBGKOU9n7BqSAi2mvPIULMAT323mg6lWH6_RE4NRa5Ykv9-lbL2UuObDKQuRZ7XX839zvBKKSMMPW6o-Wdk4Un876rshFiFvvpR6cREeG7P3HZUfGD_wl-M3Owlso3PJYVza4XI9xHdAqLiZFyapd2havgkZHbT22PRvUWV9d4OHWYAFzAe4uLqMlXkRZx9c1MtSHeol7yL3tHduB-YPgzb9A96xxAZqDBLGUfEXR1kWKY4IkeFd1TcNH5UkKro5LnmIg2Y4Ri143rPBJxIIvLUWU474Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر روز ناسا؛ حلقه بارنارد بالای دو آتشفشان دوقلو
🔹
گونزالو لاسرنا وارگاس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/676658" target="_blank">📅 14:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJBLkNtxGZToxHRAp8ol6cgAtj64yVna2NzAcfPq5o4Pi49WxYgpo21UN0Zyou6DPPan8XsgbZp_Lz1FmW6RgxpwztHeww0NJTYWJDV-TJfxN0Pq49YVW1pKYf5juvzyYDBqMDj--UzJeauZVACCF30ZHDiZh4EJh4ELvmYoQOdBTBBALrfoJtqZbA2ZpN4um0oJYbbXqXWAThbIje75BFngtIXUB8xjN_nANW82n9wIneXRdynYGZ6_Vh3vRoPMQFH5EthGG7kpN006ceE4Hst3hMY8uaXObrkBPRev7HEuel7xCN2bqs2lI43vO0DNS-g7MdMrEeigZrUUopBqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHxOK1yhVrbo_9usjekfDaMoJeutPFyPpfEHUUYjNU5mz29StAQhvV3Nuo4D39X3d5ObVBzibnGvN77vK06WgFyPiXlNYGBDFqZwpQvYlMLyNqafqM8LHGafpELuQjDwWx8ixumVmaQulCmE49DFvYNG-UfJI0oieNvftC_NYofkL5g-BAFnQ6EdrWcau6Q8H8mYjKrdpf-NdIbyAUCyQgrnc-reg5l-Cr9XX-gydOxsPWwedSRdPs-EPXC0ZvWFNYK7gsnGS-X2eL9QbqZdqaUwodyZMAEWJsLjh64qbLeqjBTwSGzBFx-M_i8Yt_8yvjODA04AWD3pDmoDuZH30g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وزیر ارتباطات با حضور در موکب «فدا» در عمود ۸۰۹ مسیر نجف به کربلا، از خدمات داوطلبانه فعالان اقتصاد دیجیتال به زائران اربعین بازدید و از تلاش‌های آنان تقدیر کرد
🔹
در این بازدید، رضا الفت‌نسب از طراحی سامانه مدیریت زائران گمشده اربعین با همکاری اپراتورهای تلفن همراه خبر داد؛ سامانه‌ای که در صورت تأیید وزارت ارتباطات، به شناسایی و بازگرداندن سریع‌تر زائران گمشده کمک خواهد کرد.
🔹
موکب «فدا» که برای سومین سال متوالی با مشارکت داوطلبانه فعالان اکوسیستم اقتصاد دیجیتال کشور برپا شده، علاوه بر ارائه خدمات رفاهی و ارتباطی به زائران، امسال با استفاده از ظرفیت فناوری تلاش کرده خدماتی فراتر از فضای موکب ارائه دهد و نقش مؤثرتری در تسهیل سفر زائران اربعین ایفا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/676656" target="_blank">📅 14:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
درخواست گسترده در اردن برای خروج نظامیان آمریکایی
نیویورک تایمز:
🔹
صدها شخصیت سیاسی، حقوقی و مدنی در اردن با امضای طوماری خواستار خروج نیروهای آمریکایی از این کشور شده و حضور آن‌ها را عاملی برای کشیده شدن اردن به جنگ دانسته‌اند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/676655" target="_blank">📅 14:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
انهدام پهپاد متخاصم در آسمان بندر امام خمینی(ره)
سپاه بندر امام خمینی(ره):
🔹
در ساعات اولیه بامداد امروز یک فروند پهپاد متخاصم در آسمان شهر بندر امام خمینی(ره) رهگیری و منهدم شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676654" target="_blank">📅 14:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtrw0sVyYaix2deDIj0RrqcMHZRrV3LF_tILZ-IFQ7O8c6YM4NOwWF-HFEQcNjQr4TWAKEfXOssentkhki0NeB2xio3slxNIpsoRW53Esfl5SDiLhIIfmlYOh9_vzpSOu3KkC6CSggAyBtSNsqCjLqVK9ml8yNMtnY5FtqUtyrBfNKo3DCQ1NShA0sEt78q9jYrd7rwMm4O4f5fmG78s-55RaUf4PPGcocbv-VpNTGGmdldUzKLQYHZq0FciP1D7-TDCtFl-y5px-JRS0A3sXdHGFwDe6xApi_f1qhJ5SGgT7vdS7QOwpSB3TH6LnrEzWgAaJesVNO1yYP4AIATTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311ed5f16b.mp4?token=LCtz-Y29QpY-Y31CDIZvlgCiaHs8G9Xu6Pck36eCEJvgx8Wl2labdmcDchPDb5TPyrkc7oOuXGRgFPAXoqF6k34DmM5-F9kSw96vm3VWwncQtfFPjLEP0ibiPCDUbsrFh-e6XY4N9HFl6ANCWmpJnfNSzeyvvItdRN78Kb2LEgr1QICPGOlOdWNDm6nNsW5ZAGpx7Pm-zZKq_IcYS4rbGyfHblN0T72yqpTeEldGfv6nEF8WJjsjWI1PFfR2TZIqRo_OaycZa0_ZBKRN68C8t_jS5ZNT6TiCJuh_FJePxHlOHEyfTUMbJUeteEhuswcEigpV3riCCRis4POYmUDeULkXypD1zDUS-O7ZqOw8guRxOlrGndjDWmJ16RyWXnuZeknnW_RtyFBNUSLDvSdzqB2UOLZ-fU94VUxZ466y4q0U0Ios4tBazEcGC_Gy0zEAgl6ttDqWhNRX_UnEKrvPuxK7RHBUATh7O3xTG4UigTacs95PoFTCiOKLju02pkog0l5aFTH5yCTh_apIkYuCVo0LOxC5NCANvIhVmyo71DRKWuUg37aaK9-Kn6IRF2sfUtDglXo2_30B1QmTDauH9DcZL-GNnvSo9GD4IwsOI6kS94Yf8lgwKfdt7EDMfEr0XMZuKkjV4nt0gRcuqybnXgxffsekIBYlHbETq67sQEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311ed5f16b.mp4?token=LCtz-Y29QpY-Y31CDIZvlgCiaHs8G9Xu6Pck36eCEJvgx8Wl2labdmcDchPDb5TPyrkc7oOuXGRgFPAXoqF6k34DmM5-F9kSw96vm3VWwncQtfFPjLEP0ibiPCDUbsrFh-e6XY4N9HFl6ANCWmpJnfNSzeyvvItdRN78Kb2LEgr1QICPGOlOdWNDm6nNsW5ZAGpx7Pm-zZKq_IcYS4rbGyfHblN0T72yqpTeEldGfv6nEF8WJjsjWI1PFfR2TZIqRo_OaycZa0_ZBKRN68C8t_jS5ZNT6TiCJuh_FJePxHlOHEyfTUMbJUeteEhuswcEigpV3riCCRis4POYmUDeULkXypD1zDUS-O7ZqOw8guRxOlrGndjDWmJ16RyWXnuZeknnW_RtyFBNUSLDvSdzqB2UOLZ-fU94VUxZ466y4q0U0Ios4tBazEcGC_Gy0zEAgl6ttDqWhNRX_UnEKrvPuxK7RHBUATh7O3xTG4UigTacs95PoFTCiOKLju02pkog0l5aFTH5yCTh_apIkYuCVo0LOxC5NCANvIhVmyo71DRKWuUg37aaK9-Kn6IRF2sfUtDglXo2_30B1QmTDauH9DcZL-GNnvSo9GD4IwsOI6kS94Yf8lgwKfdt7EDMfEr0XMZuKkjV4nt0gRcuqybnXgxffsekIBYlHbETq67sQEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران شبانه غزه؛ زید ۱.۵ ساله در خواب سوخت
🔹
اسرائیل شب گذشته مرکز و جنوب نوار غزه را بمباران کرد و شماری از کودکان کشته شدند.
🔹
یکی از قربانیان «زید محمد نوفل» کودک یک‌ونیم‌ساله بود؛ مادری که پیش‌تر سه فرزند دیگرش را نیز از دست داده بود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676652" target="_blank">📅 14:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
استاندار خوزستان: در حمله شب گذشته دشمن آمریکایی به شهر اهواز دو مجموعه خوابگاهی دانشجویی آسیب دیدند
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/676651" target="_blank">📅 14:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/461cbd54f2.mp4?token=Tsbb22GI91Ba1Buvv7kla4zUPvQKqBDdyJI6dEYl0XDLMa8oM4iWBO3aWPqXe06QMXhsB-5UE89TBAz0wxLMSla0D_UxP2l1WuFUVUh1IhXsswv8WtSNIb38qR0PfVRUYPHJYVYnhtXnBHXXgcNFT6YOOYe-AX_3QcUfpFEUOSWCU6Xe0aoLkVxr8yjailMV5b3KTvr5r-xhAe0L-0Q0_VI6vqptbcjbdd_OwEuTiYfQ865qtrwmfRBpgOYaQJrgE84CRrdSKB8zzkROwy2fgYnUYEc_VL_QFBkP6tmcSfwK0tP69B2BhMRqpOBveKs3PBlUWIeGPisagou7hKm7xlp_LHwijUC5Si1pwontzfKSKMEx2dQSJTyz7LqHoo2H6f2qbtZgCj2c9yYnnkrO-yMiF7dawFwrML3U9SrvfpKyV_8LP6dO20byky74PQ9ytfwDtK76vgb5uVfr9jeQVdFa6ULljQ0qQ3L4LQgayAntNTeuHiQDV9nBLwVPlxzKMW4P78rFERm9mVfiDxvMJz6jN_39glsxDEOiC_i0sBwxM9fr-3-LEYsd2VkHOQmDFCmo3vhIJC8sXnG8uvp7oy5WMWS8SNjC3-pt2lj5cQhwci0jUoeJsEIgc5st7YByhB-gYlSEHMdOLkiMSECKCsgosP-sNHXn7qBsnTXfssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/461cbd54f2.mp4?token=Tsbb22GI91Ba1Buvv7kla4zUPvQKqBDdyJI6dEYl0XDLMa8oM4iWBO3aWPqXe06QMXhsB-5UE89TBAz0wxLMSla0D_UxP2l1WuFUVUh1IhXsswv8WtSNIb38qR0PfVRUYPHJYVYnhtXnBHXXgcNFT6YOOYe-AX_3QcUfpFEUOSWCU6Xe0aoLkVxr8yjailMV5b3KTvr5r-xhAe0L-0Q0_VI6vqptbcjbdd_OwEuTiYfQ865qtrwmfRBpgOYaQJrgE84CRrdSKB8zzkROwy2fgYnUYEc_VL_QFBkP6tmcSfwK0tP69B2BhMRqpOBveKs3PBlUWIeGPisagou7hKm7xlp_LHwijUC5Si1pwontzfKSKMEx2dQSJTyz7LqHoo2H6f2qbtZgCj2c9yYnnkrO-yMiF7dawFwrML3U9SrvfpKyV_8LP6dO20byky74PQ9ytfwDtK76vgb5uVfr9jeQVdFa6ULljQ0qQ3L4LQgayAntNTeuHiQDV9nBLwVPlxzKMW4P78rFERm9mVfiDxvMJz6jN_39glsxDEOiC_i0sBwxM9fr-3-LEYsd2VkHOQmDFCmo3vhIJC8sXnG8uvp7oy5WMWS8SNjC3-pt2lj5cQhwci0jUoeJsEIgc5st7YByhB-gYlSEHMdOLkiMSECKCsgosP-sNHXn7qBsnTXfssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه: تخریب کامل سه فروند هواپیمای اف ۳۵ و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم  روابط عمومی سپاه پاسداران:
🔹
مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به ویژه مواضع صریح گروه هایی از نخبگان اردن عرصه…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/676650" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bac1495d1.mp4?token=JE4ZDlgC3A4ja8SCLSJLnqbU1xOCY6Uw1fLtcr2adXJBnL3jkbEDW-lHMk-pvTwOKbYIh74ZHbnB_QgwmEwvawdESm6VVW223aB4VZyoqrXt6HrqcTBjytd0JdIfoL1fRRGholQCKPRaMUMXX9X6Qh-B-xDmviubkui6GuO4pm-nA9ljBIwKb-Mq3mmKSwD1EqqjPbqU3Zj7sNOAzOnF4C4hvlXtYHIrlnCTQGzQ1LS_P-FXKc86UroMCivj7fS971rzmOhs-hlr5EgcW_F7cNeLWc3E4X2uW8CrUCqABnsBktI7S63dHyznclcRfBlA6jTUDxq0pb8Hjh0Lc10iig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bac1495d1.mp4?token=JE4ZDlgC3A4ja8SCLSJLnqbU1xOCY6Uw1fLtcr2adXJBnL3jkbEDW-lHMk-pvTwOKbYIh74ZHbnB_QgwmEwvawdESm6VVW223aB4VZyoqrXt6HrqcTBjytd0JdIfoL1fRRGholQCKPRaMUMXX9X6Qh-B-xDmviubkui6GuO4pm-nA9ljBIwKb-Mq3mmKSwD1EqqjPbqU3Zj7sNOAzOnF4C4hvlXtYHIrlnCTQGzQ1LS_P-FXKc86UroMCivj7fS971rzmOhs-hlr5EgcW_F7cNeLWc3E4X2uW8CrUCqABnsBktI7S63dHyznclcRfBlA6jTUDxq0pb8Hjh0Lc10iig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب ماهواره شناسایی ارتش آمریکا با موشک اسپیس‌ایکس
🔹
موشک فالکون ۹ در قالب مأموریت محرمانه
NROL-95
از کیپ کاناورال به فضا پرتاب شد؛ این چهارمین پرتاب اسپیس‌ایکس برای نهادهای اطلاعاتی آمریکا در سال ۲۰۲۶ است. جزئیات مربوط به ماهواره‌های این مأموریت منتشر نشده است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/676649" target="_blank">📅 14:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOfzmEyANmw2bn-SGyAEnPo-2lYj24DA8_wRf7cpWFeKOV1xLpuyjx_JN9hTwsjyFi9ukNvqJ8a0QCdS9Bh4QvEbz5uUJEP3mmsy9yszcFj9yZ1o5puKRRiLAoIDV0fEJQsCLN1QacuQMuStqBy5g66xjCzr6B0k-K-vP1yIOKm2LJP7eWNq0ylPuGBdssgvuKxxrTeeJvLQIZd9PW9B3YlSzkUQi1xWc6RTZLm48bb_1hcoC8t6jZ-4pvs8OZbZfBQSc4mKTaU8Vdj3NxNl8HbbKMD7DFPhy7-ACWZKxQmjVBMZq_p-k7dw5cfBfUDO91VGexVwUP1jSctlQll4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کشتی ایرانی خط محاصرۀ آمریکا را شکست
🔹
کشتی کانتینری نورا از خط محاصره آمریکا گذشت و وارد آب‌های آزاد شد؛ این کشتی پیش‌تر در نزدیکی قشم دیده شده بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676648" target="_blank">📅 14:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رسانه آمریکایی: سناریوی اسرائیل برای فروپاشی ایران ناکام ماند
رسانه آمریکایی «ام‌اس‌نَو»:
🔹
بنیامین نتانیاهو در سفر به واشنگتن بدون دستیابی به راهبردی روشن درباره ایران، کاخ سفید را ترک کرده و پیش‌بینی‌های تل‌آویو درباره تغییر حاکمیت در ایران شکست خورده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/676647" target="_blank">📅 14:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0R1VG8RtA80Wf1Am0NgpCwzfT8_PJvE4SsALGE4bdplWKQ6Sny69efiTgHgyevf2URPgTpofjSHJG6B-TbQef9QzubVKXK6QPrSnorL4nazzA1yh_f-dHQjFNcsB5RC0tIUDXi-r5wJ7Ymxia3KqT5Ln01hmS1a0CAQO06qTCBkuCzeIBs20JEcMQDFSEY8f39RC1wHyNkwRz0F5lWV2Wq17fzWpTTwhFKFnap-u83KdaDWMbvdIYkVmby4EN1EVfwLBEL4923D2uenhxHkE6yHbOG89EXazv6HHFtaUmY8v5czKnsbltssU358kSAbbUitwaqWmurw3kHeQd12bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این آموزش بفرست برای کسی که عاشق شال کشی و استایل کردنه
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/676646" target="_blank">📅 14:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beded2c25.mp4?token=u9p7onJ_GGmYCtas3ScUlw41DLwfryn8JbsraEMFN1cCNqtTR_C0lrMv3fUdZXOs6En3wYJ1sLN92Y8tlS3xIQF4v1hYZMp46SDsKkBLGB-7r2EixAYqHvqCKy-l10Mw6Sy0wt0BawAr1B5TYPKWZi8LDEUQAfG4Tqt1dvxPauKGriIb_XRdyTdwkOY7BT3S02JvctrqzdFSTvO6PXUZMzFZNuWEP5gfaVVHjs8xG3o51NQmdvBkdyifJG-YzolyoBVPqcDJdHjxiDWo7FLWAxg_u_B472xZD453xpWR8Jtg4LC8blOoGraSRbrYAFsbehSdIC4bca-_lJ3k20-AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beded2c25.mp4?token=u9p7onJ_GGmYCtas3ScUlw41DLwfryn8JbsraEMFN1cCNqtTR_C0lrMv3fUdZXOs6En3wYJ1sLN92Y8tlS3xIQF4v1hYZMp46SDsKkBLGB-7r2EixAYqHvqCKy-l10Mw6Sy0wt0BawAr1B5TYPKWZi8LDEUQAfG4Tqt1dvxPauKGriIb_XRdyTdwkOY7BT3S02JvctrqzdFSTvO6PXUZMzFZNuWEP5gfaVVHjs8xG3o51NQmdvBkdyifJG-YzolyoBVPqcDJdHjxiDWo7FLWAxg_u_B472xZD453xpWR8Jtg4LC8blOoGraSRbrYAFsbehSdIC4bca-_lJ3k20-AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زمین‌گیر شدن شرور سابقه‌دار عامل ضرب‌وشتم بانوان با شلیک پلیس تهران
🔹
پلیس اطلاعات تهران بزرگ در پی انتشار فیلم قدرت‌نمایی و ضرب‌وشتم بانوان در فضای مجازی، متهمی به نام «نوید» (متولد ۱۳۶۹) با ۱۰ فقره سابقه کیفری را شناسایی کرد.
🔹
این فرد بامداد پنجشنبه نهم…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/676645" target="_blank">📅 14:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ef75004d.mp4?token=uvY9mtwPWpmNQbRPyNnS8BVcsuZH3kNCcrJz5BJTJ7hkwT5ZEVicTg0rUEYP92DmiAzH9Qbu0AOExbcn-TY2--wtJOEaUb7sDO2nYxWxvT_HRytdLzqYTQH0FwREDDr90Dt-7HGzz1cFRQZiVqvL79LkewvbNruLX64l3nk0nERzTan2cc7-kVriOyBm1Lb2pGdWEK45WAmrrHUOqQePWxu-HEG97YGdWjWtgrrv_YScGWXIIsQvbjVhkvk95gPNcKlrW47NRmWjsrhlVDUBayCmS0ih2Hz282G1ZEhdPFbrssI11zZqvJ-oaRFSO9yDC1n4kytMantLLVhCtkyLfmABVxwAHvxrbXmp735tY-osTkNU0TAM57NOVUwmXiholFU9d4RP5iw_FA3GmVc5fyMi2NmXMqMSNvzYEFcrx2qwBZi4xj82pPCdr1J7JFdzUxOgPFwO-_e6-Epqh9V3_VWsvoHqC13x9WCcmLL13LMyQ4TlNrxNJvcV1V98O208VAZDMCuM7Cgws1o3nK3BGjkBln6XfV5pCJ2exYsM2kOhJyD1gzK7UfT52Eesd8yBIDLS5j3_Z4yMUG62oFO5mfFh2ob0Ye4f4XT0rcrNXVh26q2PezNc6VjedXlwEWvU7oBCA6bSAHYVglp1Y2c6GKd1dfhNkwHhtZRMCsnDwPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ef75004d.mp4?token=uvY9mtwPWpmNQbRPyNnS8BVcsuZH3kNCcrJz5BJTJ7hkwT5ZEVicTg0rUEYP92DmiAzH9Qbu0AOExbcn-TY2--wtJOEaUb7sDO2nYxWxvT_HRytdLzqYTQH0FwREDDr90Dt-7HGzz1cFRQZiVqvL79LkewvbNruLX64l3nk0nERzTan2cc7-kVriOyBm1Lb2pGdWEK45WAmrrHUOqQePWxu-HEG97YGdWjWtgrrv_YScGWXIIsQvbjVhkvk95gPNcKlrW47NRmWjsrhlVDUBayCmS0ih2Hz282G1ZEhdPFbrssI11zZqvJ-oaRFSO9yDC1n4kytMantLLVhCtkyLfmABVxwAHvxrbXmp735tY-osTkNU0TAM57NOVUwmXiholFU9d4RP5iw_FA3GmVc5fyMi2NmXMqMSNvzYEFcrx2qwBZi4xj82pPCdr1J7JFdzUxOgPFwO-_e6-Epqh9V3_VWsvoHqC13x9WCcmLL13LMyQ4TlNrxNJvcV1V98O208VAZDMCuM7Cgws1o3nK3BGjkBln6XfV5pCJ2exYsM2kOhJyD1gzK7UfT52Eesd8yBIDLS5j3_Z4yMUG62oFO5mfFh2ob0Ye4f4XT0rcrNXVh26q2PezNc6VjedXlwEWvU7oBCA6bSAHYVglp1Y2c6GKd1dfhNkwHhtZRMCsnDwPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس عربستانی: حشد‌الشعبی با زور در پارلمان عراق به قدرت رسید و سازمان دولتی شد
🔹
مجری عراقی خطاب به کارشناس: میشه تاریخ آخرین انتخابات عربستان رو بگید؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/676644" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سپاه: تخریب کامل سه فروند هواپیمای اف ۳۵ و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم
روابط عمومی سپاه پاسداران:
🔹
مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به ویژه مواضع صریح گروه هایی از نخبگان اردن عرصه را بر دشمن تنگ و آنها را مستاصل کرده است.
🔹
سحرگاه امروز دشمن آمریکایی عاجزانه از رویارویی جوانمردانه نظامی با استفاده از پایگاه های اشغالی در کشور شما و حمله هوایی به دو خانه مسکونی با بمب های سنگر شکن خود، دو خانه ساده مردم محلی در جزیره قشم را هدف قرار داد که پدر، مادر و یک فرزند خانواده شهید و دو کودک دیگر مجروح شدند.
🔹
در پاسخ به این جنایت و کمک به شما برای رهایی سرزمین اسلامی اردن از نکبت اشغالگران آمریکایی، صبح امروز رزمندگان نیروی هوافضای سپاه با حمله به رمپ استقرار و سوله تعمیراتی جنگنده های اف 35 دشمن امریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، سه فروند هواپیمای اف 35 را به کلی تخریب و به سه فروند دیگر خسارت سنگینی وارد کردند.
🔹
در این حمله همچنین چند افسر و کادر فنی و تعمیراتی دشمن نیز به هلاکت رسیدند.
🔹
منطقه ما جای ارتش کودک‌کش که اینگونه با قساوت خانواده های بی گناه را نیمه شب در خواب به خاک و خون می کشد، نیست. مبارزه ما و شما تا اخراج آخرین اشغالگر آمریکایی از سرزمین های اسلامی ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/676643" target="_blank">📅 14:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
گزارش های اولیه از پرتاب موشک از ایران‌‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/676642" target="_blank">📅 14:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نخستین کشتی حامل گاز قطر از تنگه هرمز عبور کرد
🔹
داده‌های کپلر و LSEG نشان می‌دهد یک نفتکش حامل گاز طبیعی مایع متعلق به «قطر انرژی» شب گذشته از تنگه هرمز خارج شده است؛ این نخستین عبور ثبت‌شده از این آبراه از ۱۱ ژوئیه تاکنون است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/676641" target="_blank">📅 14:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8-wbkA5hELDRmrIsNGyEdpIZ6_5btk6F6YEe5RlR5gREnNKJqe493sUpVjeSRwK_GAujyn3tfdBBC7lJKpx528lcKHsMrYlufChkWtZEIvRvc_u6beMgJTUwXW96F_GpB_UryHBddd60acyZAtQs3PEKzoWW0dA3KGMXo__dBQkRrjLOle48db0HZm3PbgaTgOcz9AXheWs7V-NohtEQKMvC52Dl13BnY5N7cL23SRzSDZx9m00f7jasH6ORgYafZeRiXJ0kb0JAY5CbNafghoPCAcN0AduhNmeDfUjCbaeVNJORJUGGS9oUsrs5_Iwe3fsnLqKoXoB0sRnIJVLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خرید قسطی طلا تا ۴۰۰ میلیون از ملّی‌گلد
فوری، بدون نیاز به چک، ضامن و اعتبارسنجی
با سرویس خرید قسطی ملّی‌گلد،
می‌تونی طلای مورد نظرت رو همین امروز با
نرخ لحظه‌ای
بخری و هزینه‌ش رو در بازه‌های ۱۲ یا ۱۸ ماهه پرداخت کنی.
✅
بدون چک و ضامن
✅
بدون اعتبارسنجی
👇
برای مشاهده شرایط و شروع خرید قسطی، روی لینک کلیک کن
🔗
شروع خرید قسطی
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/676640" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THWgOUZNWvm8USmloinGVtKYXp5E6mnkLHjwR5ibeagoegWd9iOBkISqE9YqpS9wEnX4hghe0uJtIJPb8vNTpdxJM75PbhCk2GUHekLLtujHO0Kua3SKsaVOgM9FMLBXosh63U_gPcS_MVnDjKgCvSmPLenfKMT7-6WaT3-zVmqZBG2H7qRp_qIsuYA4Jt7sZyB_Zillg3u8zGVWzTO3WJ6N6FUXNGQRojjErlmXuIPTartiJY_GTREKbpAkuUM1jsszuDOqVr4r6GqIYeuNjtyP0hTowkxcZJYubdMWfnsR4Uy6dOJ7XzCwmuheGqcQBTKAjIxJlf-l2ZzpaUUobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
شهرک صنعتی توس، میزبان 226امین شعبه بانک اقتصادنوین
«شهرک صنعتی توس» امروز میزبان هشتمین شعبه بانک اقتصادنوین در شهر مشهد مقدس و سرزمین امام هشتم بود؛ دویست و بیست و ششمین شعبه در سراسر کشور و نخستین شعبه بانک در شهرک‌های صنعتی.
🔻
اطلاعات بیشتر:
🔗
https://enbank.ir/s/mfa8Ji
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/676639" target="_blank">📅 13:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شهادت ۳ ‌پاسدار استان زنجان در حمله موشکی آمریکا
‌
روابط عمومی سپاه انصارالمهدی(عج) استان زنجان:
‌
🔹
در حمله وحشیانه رژیم تروریستی آمریکای جنایتکار در ۸ مرداد ۱۴۰۵، ۳ تن از پاسداران سرافراز و غیور  سپاه انصارالمهدی(عج)استان زنجان به نام‌های  محمود ملاجباری، محمدرضا چراغی، جمال امیری  در دفاع از مرز و بوم ایران ‌و مردم ‌به فیض شهادت نائل آمدند.
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/676638" target="_blank">📅 13:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
حمله پهپادی به یک نفتکش در دریای خزر
اتحادیه خط لوله دریای خزر (CPC):
🔹
یک نفتکش در حال بارگیری نفت در یک ترمینال شناور متعلق به این اتحادیه هدف حمله پهپادی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/676637" target="_blank">📅 13:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-myt9SpaqGhFc5vER9gLcaj-X9qmOFUPjygb1Lausnh2qE3RWmehY8BJYBfVR2w8cw3FBJHTu_W7RXcUC2nLb8n-LBlojDqTh4FgsIFHM04h1PoC5MfeH_SJrVMhgBJkVjD9-LMk-mpcOlVFeTYHKrixh2ORK5wAVcHgDM99O7IhnCn2ZxUI2EnDaPWOgfh-e547wGPHCbAgGkn5kU51Js-F7Yw_gnIERophLAunGhrMGtTwkp8c-MmcmxxsDiveGuOcZYupwRacZpMP4yUi-DuDVPGGhSEihhy8g0E6SPJA2ggSvGpRcFiAKVO0zlJ8nHynckXj-G7F3oOuTUhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: رژیم ترامپ در حال خاموش کردن صداهای باقی مانده از ایران است
سید محمد مرندی، کارشناس مسائل بین‌الملل:
🔹
رژیم درمانده ترامپ، ایلان ماسک و ایکس به سرعت در حال خاموش کردن تمام صداهای باقی مانده از ایران، مانند خبرگزاری تسنیم هستند.
🔹
خیلی دیر شده، جهان از خواب بیدار شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/676636" target="_blank">📅 13:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz1gAVbKdr1EGHC-ApYZeUE0wEX1sROUamdvj7jx3Ytl9CVdMiRZauIN3yxxRZUVRsGPZon1Fpo_wMgg2WIMf-bBbN-dPRvIsNPzryiciyH8mSkq-gkQZKOSjjMkAXZW_CSepmDROtWODSO3w-xBymeO5Hhe2GMUyw5s1Ip12l8sdMFQabwrR17iwM_y3lxTto6vh54RQ4vTVwct35MssatHvkZcgNkum0KGSqPG8FvgY7IBChgSQwwMKiXBWlU0nvXK_RVg-z8IkWjfo-Lkv_ClcJZ4Xy6Ui9ZJ0CJpjuqpR4wl6DA5Iki5udt3P-tqck0bNh66VM7gHtpPz1aQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از ‌حمله موشکی‌ آمریکا به منازل مسکونی در قشم
🔹
در پی حمله موشکی آمریکا ‌به منازل مسکونی در محله چاه‌تنگو شهر قشم ۳ عضو یک خانواده به شهادت رسیدند و ۲ فرزند دیگر این خانواده نیز مصدوم و برای ادامه روند درمان به مرکز درمانی منتقل شدند.  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/676635" target="_blank">📅 13:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iucTGjxtHPGljVRtfXty4RBVXKJjO41fYv_iRJ3mGIBIdqP3IjM6dZPoIEPzqgNqk0nO5d7oniOycPVxBt_czGlQKVrqTX6Dbyc7xZYExzrvf7PJ7VU8ga3SHZkVJ_-iA8xfoYggKcL-S7xi3cVlqE8oRzqVvI8Z5vRCSOj6ln6BlOImMYLb6ncKfGwaRlaHoX3MkWb67YFElEbRdD7PTYyBBtJV2trjfMnvZqZezwDdRDkqr4CBxktC3iTzpLTDTImGTKefczwNu_jORProZkFE-1Jm6i4KxZlG_GaolWBL2SBc35dWyUNntcDiKiQiwfCIKB5X2KH3acSMbfi43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۸ مرداد ماه
🔹
بازار طلای امروز نیز همچنان با کمی افزایش در سکه تمام بهار آزادی و و ربع سکه مواجه شد.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/676634" target="_blank">📅 13:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پکن شایعات ارسال سلاح به ایران را بی‌اساس خواند
🔹
وزارت امور خارجه چین، گزارش‌های منتشرشده درباره ارسال تسلیحات به ایران را «نادرست و بی‌اساس» خواند و تأکید کرد که پکن همواره نقشی سازنده در کاهش تنش‌ها ایفا کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/676633" target="_blank">📅 13:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بازداشت راننده آمبولانس در اسرائیل به ظن جاسوسی
روزنامه «یدیعوت آحارونوت»:
🔹
یک راننده آمبولانس اسرائیلی به اتهام جاسوسی و انجام مأموریت‌های جمع‌آوری اطلاعات برای ایران دستگیر شد.
🔹
این فرد ۳۴ ساله از دسترسی خود به بیمارستان‌ها برای جمع‌آوری اطلاعات و عکاسی از مکان‌های حساس استفاده کرد.
🔹
گفته می‌شود که او از یک «چهره ارشد اسرائیلی» که در حال بازدید از یک مرکز درمانی شمال اسرائیل بود، عکس گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/676631" target="_blank">📅 13:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676629">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بغداد: هیچ مدرکی درباره انجام حملات به عربستان از خاک عراق وجود ندارد.
🔹
مقاومت عراق: گزینه‌های انتقام از متجاوزان آمریکایی-سعودی روی میز است.
🔹
با اعلام AFC؛ عربستان میزبان دورهای نهایی لیگ نخبگان آسیا برای ۳ دوره بعد خواهد بود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/676629" target="_blank">📅 13:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds5g0OhaBany9ntXKmvc-tRLRcCUGjoAWWehXPMHYKvOMZ-bWDZEYIg4Zp646MOQsjSgOejy9RfhbdMz1Asw-AItev01g1BKzYWAomXkzHPmCxEbe7oZJxG6Eg5O3-nI-b4-07RkW9-hObPDQdho11baNiGcnUb8XFlyrhpMyZMfPjoJhl18MhO-SQomz6qiDEzLxbpVWIQ3gaeWHeVpuMj6m-x14Mg6QaXwNEbFq4ugpMft-6hcOvF8LMDn80W2-mzCnsx4W8C-zotY9ba-cW4zraxVVw_5TseDAsZKunD2JBz6lNQRWdrpK-u1Fhrvo3RKmsaZKmIJ60_Yqyq1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای سلامت بدن خود این نقاط را روی پا فشار دهید
🦶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/676628" target="_blank">📅 13:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6af8976a.mp4?token=gzt5sLi9QTk8GM7uTroem77mvOw0_5j7qy7eVlVjg6BZeSly3jH7-tQFGIt8etjHM5m2dDUXVz9HJxITFXSPHbLqniRhIPX5pD8Jqg7sU_kmCJWUXLKqfY5ZWeuWfK-i3_IAEmvyEbOfizBh77mg_ewY43eR-54PfNF3erjsMXzqzgZc9n14vBR7Lp0kwyOFdil_SF8IC61sXb7r7Q-fhQvJYmbHOk1dAUOi_Pk8siAmYgkTcriUUupNATX6DSZRMzZZo0ybBKY_syhTkjZssdHi8WYFgzn-snHSqFP7oW1E11kB3DdhzhOid58p0Sb2TzcG3Gedo7Clxz96hB_CCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6af8976a.mp4?token=gzt5sLi9QTk8GM7uTroem77mvOw0_5j7qy7eVlVjg6BZeSly3jH7-tQFGIt8etjHM5m2dDUXVz9HJxITFXSPHbLqniRhIPX5pD8Jqg7sU_kmCJWUXLKqfY5ZWeuWfK-i3_IAEmvyEbOfizBh77mg_ewY43eR-54PfNF3erjsMXzqzgZc9n14vBR7Lp0kwyOFdil_SF8IC61sXb7r7Q-fhQvJYmbHOk1dAUOi_Pk8siAmYgkTcriUUupNATX6DSZRMzZZo0ybBKY_syhTkjZssdHi8WYFgzn-snHSqFP7oW1E11kB3DdhzhOid58p0Sb2TzcG3Gedo7Clxz96hB_CCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدیه پوتین به رهبری در سفر به تهران چه بود؟
/ تلویزیون اینترنتی مدار
🔹
قسمت اول گفتگوی متفاوت "پلاریس" را در لینک زیر ببنید
👇
https://youtu.be/RgUM8McWe-g
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/676627" target="_blank">📅 13:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b785ba8cdc.mp4?token=M_xEc6GkyNTry65Insg53wOb4_t_QIAYfy72rqPAclmTAflOJb6WVj7ysyVhnGH59nTae_eSCx6JxuIK6L4PvprSG_6FID4WSelF7o4JOj7-k1__IUE3BN2r3mRj3dsE2juUKBq3RdGvtuVygsHCIzqsoiyMSmszDZ6YHAWl1Ui9ShcY3LX9XFK_DICSlCyyjWcu2Jbgv_Ibp-6j0sb-_Y58yNaKGf2bitT4RpjnwvkzocjHC28QHNn_E5J7QAxrgpsWzyJTcMhS14xujOyvooPzAqEyxvWkryJJj8OfpKnn6qMHMoDl6Bpm5agAG9VA4W7XzdQOxpYX205EYqTWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b785ba8cdc.mp4?token=M_xEc6GkyNTry65Insg53wOb4_t_QIAYfy72rqPAclmTAflOJb6WVj7ysyVhnGH59nTae_eSCx6JxuIK6L4PvprSG_6FID4WSelF7o4JOj7-k1__IUE3BN2r3mRj3dsE2juUKBq3RdGvtuVygsHCIzqsoiyMSmszDZ6YHAWl1Ui9ShcY3LX9XFK_DICSlCyyjWcu2Jbgv_Ibp-6j0sb-_Y58yNaKGf2bitT4RpjnwvkzocjHC28QHNn_E5J7QAxrgpsWzyJTcMhS14xujOyvooPzAqEyxvWkryJJj8OfpKnn6qMHMoDl6Bpm5agAG9VA4W7XzdQOxpYX205EYqTWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت تلخ و دردناک نخبه و ریاضی‌دان ایرانی در آمریکا؛ پرداخت مالیات به کشوری که مردمم را بمباران می‌کند، بسیار ناراحت کننده است
🔹
شایان اویس، استاد دانشگاه و ریاضی‌دان برجسته ایرانی: برخی از دوستانم به‌خاطر پشتیبانی دولت آمریکا از جنگ مهاجرت کردند؛ من هم به این موضوع چندین بار فکر کرده‌ام!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/676626" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86381f1826.mp4?token=oKk6E37pwFxKGt9vOjzc9cFy8474zYa-0tC3d4lQdyXO7wtqQIzYQoLkThwoNSKAYnSRZ6K96ryICqR1v6ROQMqoN909__jHRjIzHiRxsokyKvIABGV5LJjn6IYEHVYDm4WPXEyAkkztDQsihOIIjcAt2XBYAWpqMq5p0TVdZEfA_aBoXEpJArgheCe-V0YFoDYaZ4AXG5BMliMv6XjvBgm9JIgANLfdZKqR58yZUkY9Gw1lI9OYax8YkDxsv2886-RdmG7FapJrolaUCtCOSdTs7J9edVXELMjgwfPoGwBlCee9dikrEl01hyi_Y2OLVLKgZg8ymMfRZa_787sOVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86381f1826.mp4?token=oKk6E37pwFxKGt9vOjzc9cFy8474zYa-0tC3d4lQdyXO7wtqQIzYQoLkThwoNSKAYnSRZ6K96ryICqR1v6ROQMqoN909__jHRjIzHiRxsokyKvIABGV5LJjn6IYEHVYDm4WPXEyAkkztDQsihOIIjcAt2XBYAWpqMq5p0TVdZEfA_aBoXEpJArgheCe-V0YFoDYaZ4AXG5BMliMv6XjvBgm9JIgANLfdZKqR58yZUkY9Gw1lI9OYax8YkDxsv2886-RdmG7FapJrolaUCtCOSdTs7J9edVXELMjgwfPoGwBlCee9dikrEl01hyi_Y2OLVLKgZg8ymMfRZa_787sOVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز زیبای منقار قاشقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/676625" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ef1a4574.mp4?token=j24B82P7osvz4JAGUoH7Bx6_8IPSL2wnB_WvGMX3vrg812PDOGZJkCCx3Zfh28Mb3tempfTM9E7d0Cio7BI4zUNbVHcN9ztww1Wfu2Xocd770o7CJ5S3gA2RE5H2jY6Iz5twpumihMiTDAEB8mHbQS0OWX-emFenNY7v76pgutkS3-qXFhmkScoLqC4OrU9O__71P_91tPl9Sr_R4DciG49YQ0KnswFXD46hCfWtSafxcsiLENMGLR6wFp_CE-7snUNLj9WhNfpc3oulLFNmT9zQBvVTt7qi2nO9J6ZW353NLcMF9ExRsTeeFybIgB1hSU3VeprjCpw2u8P---WqjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ef1a4574.mp4?token=j24B82P7osvz4JAGUoH7Bx6_8IPSL2wnB_WvGMX3vrg812PDOGZJkCCx3Zfh28Mb3tempfTM9E7d0Cio7BI4zUNbVHcN9ztww1Wfu2Xocd770o7CJ5S3gA2RE5H2jY6Iz5twpumihMiTDAEB8mHbQS0OWX-emFenNY7v76pgutkS3-qXFhmkScoLqC4OrU9O__71P_91tPl9Sr_R4DciG49YQ0KnswFXD46hCfWtSafxcsiLENMGLR6wFp_CE-7snUNLj9WhNfpc3oulLFNmT9zQBvVTt7qi2nO9J6ZW353NLcMF9ExRsTeeFybIgB1hSU3VeprjCpw2u8P---WqjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معادله عوض شد
دیگر صبر نمی‌کنیم تا به ما حمله کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/676624" target="_blank">📅 12:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG9oZG_W4in7P3zWL13gi_qnDNRshv1Ct28jQuFVu07kWRwbajLBZUHiIpiCj90wE_pZXXEzGOfuVl2ixpzA_jzj--6O_rSrBn4ns_iP0Xsdd-M56_QVkr2AQbcAg8XH41Nz6zW093XcsHdLmbJych2Su4wtMRCwdDbonZUjXoIcq3uGa6oG2MJJu-HhXiZJgUhQqFRfqbk7K_FkcXFuIdjrRvlX33rQg-_vVSgvzqPdv7cQTV6rpdLoXVIgmg4QmqwcIHdR-KvxrrN9sHcaUDUGpveCDcLe5bf2D10IwSrdxiuErfdC8-DWM5Prfot8DaawiYLZ39QKXdD4HYtDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gW99nm300oBq-A6cgRTJD5FIn-zUXWWi-viMCB0zHwz3wmlf_l3cymqbSofu2X56uVA4yxFyvIhEPcGnQ4QunOQavTwgokPX4UL9nudkqOndcxHc2-kKnm1IOTtr4uxCk7qfKwd8_jnJI7aGuRMklbD2z53RSoBv96c75A0wZSnaHJlk52fNRBaTD_-pzIO6Gh4nfwII8hq0gyZBjqiskapDm-NhFVlGrbvfSHGG7qxbw9Jt68u8n3EvAVEw7yh67RBWJ-JCh_gmKCk6S6ARI2eqFNjIxvf7wTXVF2lYHWO87kgJujrd5NU_oxAcCe5Dqyza0kjD5vYKvUELv-QVjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ایران به ازای هر نفر حدود ۱.۷ سیم‌کارت فعال وجود دارد
🔸
ایران با ۱۷۴ اشتراک تلفن همراه به ازای هر ۱۰۰ نفر در رتبه ۱۲ جهان قرار دارد؛ یعنی به‌طور متوسط به ازای هر فرد حدود ۱.۷ سیم‌کارت فعال وجود دارد.
🔸
ایران از نظر تعداد اشتراک تلفن همراه، بالاتر از کشورهایی مانند چین، آلمان، سوئیس، فنلاند، بریتانیا، آمریکا، ترکیه، عراق، هند و افغانستان قرار گرفته است.
🔸
تعداد اشتراک‌های تلفن همراه در ایران طی دو دهه گذشته رشد چشمگیری داشته و از کمتر از یک میلیون اشتراک در سال ۱۳۷۹ به بیش از ۱۵۹ میلیون اشتراک در سال ۱۴۰۳ رسیده است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/676622" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نشست اضطراری وزیر دفاع عربستان با ترامپ و ونس در کاخ سفید
🔹
وزیر دفاع عربستان در کاخ سفید با رئیس جمهور آمریکا و معاون اودرباره تحولات منطقه به ویژه تنش فعلی با ایران گفتگو کرد.
🔹
گفته شده خالد در دیدار حامل پیامی از سوی محمد بن سلمان، ولی عهد عربستان بود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/676621" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676619">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9b2bff6b.mp4?token=TBoSnqpIwDvJ96delQeVKYipjqBPOCaKqPXh-9svftiTtSoWpzJ9mIvRkvqmzqds-s1wurwIE5FWy71t2SeHv7VqTx_YCr1c3hWY5R7BTjWdqDnLrrJTq2h7MyMmKoQ87R1WaPLI-tVraUhdSBTd9YTU4HjlqlpK-8zdwxcZpAs4YrhLfbzXcmkvysTVwSTwlUeKBWDwCyLjXXQZh_KtbnNqR2uR1EnTCs6JAMdAvJHVfmcXHgrc2RdqJW8EHsZ7jTgltCgMjuOEQQa8O4kOi9OPjgFgGhC85ZODYH6LNJ0EC83g8QHkDcDr57C0L-ujcyz9FhPpKSwscGNFY6YVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9b2bff6b.mp4?token=TBoSnqpIwDvJ96delQeVKYipjqBPOCaKqPXh-9svftiTtSoWpzJ9mIvRkvqmzqds-s1wurwIE5FWy71t2SeHv7VqTx_YCr1c3hWY5R7BTjWdqDnLrrJTq2h7MyMmKoQ87R1WaPLI-tVraUhdSBTd9YTU4HjlqlpK-8zdwxcZpAs4YrhLfbzXcmkvysTVwSTwlUeKBWDwCyLjXXQZh_KtbnNqR2uR1EnTCs6JAMdAvJHVfmcXHgrc2RdqJW8EHsZ7jTgltCgMjuOEQQa8O4kOi9OPjgFgGhC85ZODYH6LNJ0EC83g8QHkDcDr57C0L-ujcyz9FhPpKSwscGNFY6YVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/676619" target="_blank">📅 12:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676618">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59db64932e.mp4?token=IM8XDSTInANPZtqa-wv3Ra3QJqAjiKczdbHMgd8Y3WSC48xykHK2ljOcMY05SwhP-au0BI0_Csb5ZGy8SIex-Nc7sSzMDdC0wKXatxiWmideqCo0gFADo9JdoWanaFIXf0gOMODTiuEMTLYAXyvc7-Oz_RupxoKhgY05bUubdS5X2-bs7Fadk-b1nM2IvHN4tQUL5hwSl93wPLbZoUz4g_lbbEmeGWzkIw2VW1qgQfivAPZhl_lbQKNCYnOA_6bk8i3NBHfmtcIAlRXkXwO6tnYNNlai9hpa3D3GAPBEKMWV5ZTjGtnoyiZa53l8UydpUPkX7X3TSpyfwhAL_exRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59db64932e.mp4?token=IM8XDSTInANPZtqa-wv3Ra3QJqAjiKczdbHMgd8Y3WSC48xykHK2ljOcMY05SwhP-au0BI0_Csb5ZGy8SIex-Nc7sSzMDdC0wKXatxiWmideqCo0gFADo9JdoWanaFIXf0gOMODTiuEMTLYAXyvc7-Oz_RupxoKhgY05bUubdS5X2-bs7Fadk-b1nM2IvHN4tQUL5hwSl93wPLbZoUz4g_lbbEmeGWzkIw2VW1qgQfivAPZhl_lbQKNCYnOA_6bk8i3NBHfmtcIAlRXkXwO6tnYNNlai9hpa3D3GAPBEKMWV5ZTjGtnoyiZa53l8UydpUPkX7X3TSpyfwhAL_exRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه آرامش‌بخش است دانستن این حقیقت که گاهی پشتِ گلایه‌ها و اصرار بر ترمیمِ رابطه، نه خشم، که عمیق‌ترین لایه‌های عشق و دلبستگی پنهان شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/676618" target="_blank">📅 12:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676617">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8fb1206a.mp4?token=Wc8TPKw0HuddZbsGgaWCc0HawsEsknjQls9FVtGRfrX8QfBu1LRD2Mtuuxj1cSoi-HjObgLcLNOxxyQWwTl35PL2Eb7Oz_bbTbvDYJiLna_LH4TynzgaDIdJfdAxqhBsH_Gcj22tO_ikPfFT_hyodReHVAu94ZgIzp2wFSFUpOjK6Vul9v5gTsZSXfyFVg0BAFsEANkWCECwTMhIBrJvqUWpL3OLJhWZ_Z2D8bezycWv1kv8CroiX86AOwnHaXRmnCbc8V8pNS6eXql6LHuKadUbvpOqPAwoz0n_eAZlqtTcPYv7E8n4_E-jng451tRAHnE7COzkbQdGzQmnHRvxzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8fb1206a.mp4?token=Wc8TPKw0HuddZbsGgaWCc0HawsEsknjQls9FVtGRfrX8QfBu1LRD2Mtuuxj1cSoi-HjObgLcLNOxxyQWwTl35PL2Eb7Oz_bbTbvDYJiLna_LH4TynzgaDIdJfdAxqhBsH_Gcj22tO_ikPfFT_hyodReHVAu94ZgIzp2wFSFUpOjK6Vul9v5gTsZSXfyFVg0BAFsEANkWCECwTMhIBrJvqUWpL3OLJhWZ_Z2D8bezycWv1kv8CroiX86AOwnHaXRmnCbc8V8pNS6eXql6LHuKadUbvpOqPAwoz0n_eAZlqtTcPYv7E8n4_E-jng451tRAHnE7COzkbQdGzQmnHRvxzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ‌حمله موشکی‌ آمریکا به منازل مسکونی در قشم
🔹
در پی حمله موشکی آمریکا ‌به منازل مسکونی در محله چاه‌تنگو شهر قشم ۳ عضو یک خانواده به شهادت رسیدند و ۲ فرزند دیگر این خانواده نیز مصدوم و برای ادامه روند درمان به مرکز درمانی منتقل شدند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/676617" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8pZkopDVH6sEyT3fFt4KNpAhb6824y34qX-PSmmj3oukjEeN8MWrxhZ0LrB3Nkx-15sYSRO4pR_J74VAMLyZaF4l3zflThK1dMnAjR1DZAyRklZMm7ySRxwGh4EtaA51p7NnYGiTa1iJkXoFY0ATtb1R7prave6kIQjnLFCeDM2Ppnc5chbdYFgod68yHc1m1wuLjXUfYzATUWJG0aV5x9uPVHCbI626OAjOhoblvDQEkdcg1CYuvWB6rAGxhbF8CSx6RxXab-ZqJavG-CnuR_jo1XrJTR3HIw-cC_lZ90e8-YzuNfXQp9MaP6fsnSQ9M0nToAGscqzwvXg6BvT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلاگر متهم به ضرب‌وشتم زنان در لایو اینستاگرام، بامداد امروز در خیابان مطهری تهران دستگیر و روانه بازداشتگاه شد.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/676614" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFbKHPqxqMU-3iaBkY7F-NnUvjrLd3EiGOO_swOO9PvSD4eYmMKOhy_NHnchhUkTeB7pA3ua-9xBBAf1iI0Hg5WizSOD6xSf8bNJjav22Fyeab3agwwBmQJ71qc4qYpfPaYeT0dypjmlaJ1ndWwrY8jC7Mu6XlDI1psXOcfawdHMwKZxfqRIiPmfiMJyVAItKjyydQsBHoMW7UERSzIdHxmz7Unj1Sdvvo8rvHOROCIQdr8r8rST8NFqjDyylGY8XutbgRokTB1mYJ5FlV97N4NZV80E6745xw3XJwsrfzrh1Lwm3X-sLnrbA7HTGfoQuEPU3J7mZjBhbkB30XbSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyL7m9YDeZLkNN9iPtmGIT1_bMxcUuv_xfcKJCQDaVvDHDg9vaA6A9_0DXNJeIZjLWL5KTXpojAsmlKoUr5jkP_xphzBnHukKYxWex58MvSgE7BWJFOblHslKY25skgzalE2O9P7z9yJJd8qiy8M2DLNnW6tdlZh8jIAbyddeMjrf8F4HW4Eq7bWFIIG-EsxzMkiRfzv9Z0LHae6aP0UU2rnEH0WJ5YIypOjJlr8_KppgqSdgTgF3XVj0pN6sG9EJJle2nl7EQ9FWdiJVW5qbLmlxy15ypRQiQizI5iGR102WFM7xSiaVYxm6i_XYUgcGCaJcogMsX86-mAB8CDEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpEBIhXYayzwPrDIB0-ta54tXDqSRNdgdNM0Uxa4JQRDdo0X0wPHkYmprtxk9b2sFo9_VCHqWn2HvZ_pXzdg5Mcddmj1Wr3UZN_Wr1E27aQ-XBl7TF_4dvl9qSl4GVe8oALY97B181E5nFVFQ2RWLivnxex4ZgDvlLbkqLLxkZxFVSw0yejn4ywILmCPOeQbLbJb5c9_EVFmT8kvF_AGuvZUXrQ2dyWh2lw-KEWOtTOl-8BXTDUQbngw7frRqwzNq0j12B0rt5CqX3BzRL70z0RlKdnYzIDi6CkvjulPeb_2hv2fbI3o9_eEVJvk1S65p9XFDcqa3ZMns31zyKvp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxJBYtoJl-LSfXlYJxafS6Obn3Th5mjUKQ44hnD2JyviU4sG1d0wV38CUEXgS3QrmzbNpPViPhpxmnkB9d_CirYbDpqKQsMYAh41305QGTOy-d-iX46_KxywlsVMjuWc0HGrVs6HH3MwfMQio1ywpLQmkLRCXCOAXBilMpZ-2f0wEkj-oRPuES_JkdA2tkMSYQM4TfIjs6H2QF5R1ZMZEymKTcq17SFAztLM3SiHhgECwIc7z108rUrWCOuQeYo9v6aqS92RpOY1Ogn2nRFwauumaNDdMwdm7M0Uk7Ll30T3YYoE9Xq454mLn-SFICme3n8NaqyY_CdsHp4dGvT33g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بعد از دیدن این ویدئو‌، دیگه خودتون رو با دیگران مقایسه نمی‌کنید #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/676610" target="_blank">📅 12:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676607">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693addf9fb.mp4?token=bB8GZ74rZL32Sm0fsvsEUCJihou1FUz_phPQHPAxk3dCS5WAvV7Nkgcy_mkb41zy2BJ34kIDi9HMjSNjVxeeDy_zs_GSR_L_-DGpUxsSfJ-bJcAfOjTSKMqReEve0o0V2fT8wQtmPlri6SnZZU8-nFD35VpwTy-I2YmaNBK40WtyJjn3FCOlTRJcyigAg0h6qGnqNIdvRFM9rgr3WaNTKBOh43WGtpywetStx_Eiwr9gvNuqtI_Zv0XPAxOTX5CkswSZk-RWDWO3LDAtB2maIU3hHT2uKz0GXW4_q7anIt0YlfD_wPl7dYLNu4ki7Sk2Z0RgHbG8FZnoFqajPqXSLJ_Jg3d6JhEZLIBEd7RSbv_RH9YZd9dYLQX56WFrDGDaE2-fLbau0FQ4JReEdl68gGnNvbWiw9gZzciej8Y_SZEWZtiywM_0W3GTLXdXxhYqZUQft_wSl00Vxux47l75ZiWapqrQWUnb_9mPrp9v9y_kUCmmzQY75jaPtQT67cQoHpr-0x5XNv4B7WgyM9GFM0ME1tp6oQKsIEYGPtT3tDiV21BlYqXp1h_oTtWpuVvhQBrXwbHBCBd7YOwMEwcwRIaYs_G05-FajO8vd_1-ZUh6MEjsNAWhhc6ndcw52Seis4MQVWSz6nU1OAfG_vw8zUu6oQM1xRzjG2IVZI4c4fc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693addf9fb.mp4?token=bB8GZ74rZL32Sm0fsvsEUCJihou1FUz_phPQHPAxk3dCS5WAvV7Nkgcy_mkb41zy2BJ34kIDi9HMjSNjVxeeDy_zs_GSR_L_-DGpUxsSfJ-bJcAfOjTSKMqReEve0o0V2fT8wQtmPlri6SnZZU8-nFD35VpwTy-I2YmaNBK40WtyJjn3FCOlTRJcyigAg0h6qGnqNIdvRFM9rgr3WaNTKBOh43WGtpywetStx_Eiwr9gvNuqtI_Zv0XPAxOTX5CkswSZk-RWDWO3LDAtB2maIU3hHT2uKz0GXW4_q7anIt0YlfD_wPl7dYLNu4ki7Sk2Z0RgHbG8FZnoFqajPqXSLJ_Jg3d6JhEZLIBEd7RSbv_RH9YZd9dYLQX56WFrDGDaE2-fLbau0FQ4JReEdl68gGnNvbWiw9gZzciej8Y_SZEWZtiywM_0W3GTLXdXxhYqZUQft_wSl00Vxux47l75ZiWapqrQWUnb_9mPrp9v9y_kUCmmzQY75jaPtQT67cQoHpr-0x5XNv4B7WgyM9GFM0ME1tp6oQKsIEYGPtT3tDiV21BlYqXp1h_oTtWpuVvhQBrXwbHBCBd7YOwMEwcwRIaYs_G05-FajO8vd_1-ZUh6MEjsNAWhhc6ndcw52Seis4MQVWSz6nU1OAfG_vw8zUu6oQM1xRzjG2IVZI4c4fc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سنتکام ناخواسته مرگبار بودن حملات ایران به اردن و ضعف سیستم دفاعی آمريكا را تاييد كرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/676607" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLKVghMN4pdolkDTtymDZfTXUDsMs4MeZKRVLmuTCn3IDz-oIlbpk8o0esh5fdS1VNZnfRthJsXV-5ZOuNGBAoxF22koSbzGeu-LjpT4recIqLU1_XWKv8cF6l_inZ9C-cQsYOI4hua5ABtqSLsm-8O6X5V_VCrttDVZKOBEcizqFc6tYQdGqqVTncKV_oFhUPKB3VJkoxMGB92vTPIg0fn8g4cyCJ2ph32jmikSL0U9qAPqJyBsGKPFtBqBcn0pz9FXxe9RwjZ01PTd6ZAst1cHht8xCjTAoZxinnCzjktk1ggnJbENQWBGb40MwwZNup9qM5CDuo4fJ5mnFKMnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ درمان خانگی مورد تایید علم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/676606" target="_blank">📅 11:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a3bce682.mp4?token=Ws3I3D4tIoCJwZRCHMLRDi-GvShaGFJ_4tjGh7gWUOnpMPR-tg31uk0OmtAO6Y4u8e8PBnnm88VOQnMB3UGyQksR23eYLecfhmKrWllSrdqTND4cHZtcOXO5PPmlPVxHQBbRr-fPTOHCrroMzdWsjp5HjjShOmWZMZKb-vEOwSiYXXDIf-Ri--ZbTvnyMR5Arif5blenqMbA0tkMgNaSXi2C0jM7qKYEp-PH1ko12mvO0lqq8KKrCrPov7tyuIEJHcBuGqkTsGm28iKBjhT2PdcEYjhhdB8P-ZMGhTQbngaNOp5kbOS3W_NdgFZyRAC-dJRkAhS1push7egTMiYpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a3bce682.mp4?token=Ws3I3D4tIoCJwZRCHMLRDi-GvShaGFJ_4tjGh7gWUOnpMPR-tg31uk0OmtAO6Y4u8e8PBnnm88VOQnMB3UGyQksR23eYLecfhmKrWllSrdqTND4cHZtcOXO5PPmlPVxHQBbRr-fPTOHCrroMzdWsjp5HjjShOmWZMZKb-vEOwSiYXXDIf-Ri--ZbTvnyMR5Arif5blenqMbA0tkMgNaSXi2C0jM7qKYEp-PH1ko12mvO0lqq8KKrCrPov7tyuIEJHcBuGqkTsGm28iKBjhT2PdcEYjhhdB8P-ZMGhTQbngaNOp5kbOS3W_NdgFZyRAC-dJRkAhS1push7egTMiYpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یا حسین ما انچه در توان داشتیم گذاشتیم؛ هیچی چیز هم نمی‌خواهیم؛ فقط می‌خواهیم ما را به عنوان خادمین خود در اربعین قبول کنی
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/676604" target="_blank">📅 11:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676602">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3790cdfd.mp4?token=olVCULxvasTGsbcc4__DOY-ArBehqP9-8awHLMcpM6-v9Mv4TaxyGF3PT-SFbbmZg3dj3sKf5FfS-FA9-M6XLsUSLL2AhYtfXNHDl0QFlsnKXC7EMGqRjk2o2cfWLHRZuRuFRIbYWWyFLwzV3iwlxceIRbrUlOYvG9ai4NGuFGn4n643AJDcFqqRZDvyTSkqiH1MXQR3NlELd9m7BmC75gQeMkqcO18G_LbA6ipxjZlXa10vc-qDybOtdBmu-gcj27fOpclurIuycTGKmE55i36VyGrqSYvPqb_98PXQJx8pjTJtSKs30akKGsDanFFMeLkaaVbhREnGTxYtxL7tgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3790cdfd.mp4?token=olVCULxvasTGsbcc4__DOY-ArBehqP9-8awHLMcpM6-v9Mv4TaxyGF3PT-SFbbmZg3dj3sKf5FfS-FA9-M6XLsUSLL2AhYtfXNHDl0QFlsnKXC7EMGqRjk2o2cfWLHRZuRuFRIbYWWyFLwzV3iwlxceIRbrUlOYvG9ai4NGuFGn4n643AJDcFqqRZDvyTSkqiH1MXQR3NlELd9m7BmC75gQeMkqcO18G_LbA6ipxjZlXa10vc-qDybOtdBmu-gcj27fOpclurIuycTGKmE55i36VyGrqSYvPqb_98PXQJx8pjTJtSKs30akKGsDanFFMeLkaaVbhREnGTxYtxL7tgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ظرف سفالی، ماشین میوه‌شویی ۳۰۰۰ سال پیش در ایران باستان بود؛ بدون برق، بدون صدا، فقط با چرخش آب و قلق مهندسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/676602" target="_blank">📅 11:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b537f120d.mp4?token=kslR4CP1-DhFcXH4mJ6nMroLutxXz7ig9VbgOv1ngwjZ5yWNS7jd18VWBez3tF_4twlqMtlHZeWoRTSgdWnoTGWh2JN30KL44nAZXzU_lDtYzycnxv2PgxwRLZdYSucYFUWnHfozt2uTYLQ89ebcy_wTO9V5Yzmp39ssZfXSBUcgRQaBICptQOZQOrbhL3Tpxe2RuNqHMzASZfNB7uayF4rUSFvrhe-F1m2uWCn7IgOWYUTenKO_pqLTy86OUlA5CXcY2MDd1rh1CWR_8kWaplnK1enb2Mz9gtA7vx0gmYOB3EVgtjYgeCqNsftOyBrtk16gEquJdkRRtO341AC4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b537f120d.mp4?token=kslR4CP1-DhFcXH4mJ6nMroLutxXz7ig9VbgOv1ngwjZ5yWNS7jd18VWBez3tF_4twlqMtlHZeWoRTSgdWnoTGWh2JN30KL44nAZXzU_lDtYzycnxv2PgxwRLZdYSucYFUWnHfozt2uTYLQ89ebcy_wTO9V5Yzmp39ssZfXSBUcgRQaBICptQOZQOrbhL3Tpxe2RuNqHMzASZfNB7uayF4rUSFvrhe-F1m2uWCn7IgOWYUTenKO_pqLTy86OUlA5CXcY2MDd1rh1CWR_8kWaplnK1enb2Mz9gtA7vx0gmYOB3EVgtjYgeCqNsftOyBrtk16gEquJdkRRtO341AC4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از عادل فردوسی پور و وزیر ارشاد در حاشیه مراسم یادبود اکبر عبدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/676601" target="_blank">📅 11:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2ZiNTusisTcoUJj0NsN9CCZH7WuboSGEGtPV_gTaML6iwGkNdRGuCqkTf-efVkU_CupauzqN3G00m7__xcD36I760rouswR6kvR1v1oKC-2IzM1O3GkKKnEOk6VAoZ_qBhVauS2SHZFlIc4SaahNKDBJvav_6Mc3GTMl7nCOU6NORXNaVxNG5-uPma40goukYSFZvZb7RygNnUsLzFo4v5coAV1rpEdl8-EiGtVnEzCXG7tvHQN6s20hnnB_dVjo1z7B7_PtZFZm4D6vI-uYxVUD8_AvZHL2bfo5goIiGblM8WvJUKm4dTt8lL-ttQ-3UQbaMAP79t4ZsAJSKINeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موسسه واشنگتن: تنگه هرمز به قبل از جنگ بر نمی‌گردد
ادعای موسسه واشنگتن:
🔹
اقدامات تهران نشان می‌دهد که ترتیبات سنتی حاکم بر تنگه هرمز عملاً فروپاشیده و نظام جدیدی در حال شکل‌گیری است که هدف آن تثبیت کنترل ایران بر این گذرگاه دریایی است.
🔹
ایران دریافته است که کنترل تردد کشتی‌ها در یکی از مهم‌ترین آبراه‌های بین‌المللی چه میزان قدرت و نفوذ به آن می‌دهد. تهران در مذاکرات آینده نیز از اهرم تنگه هرمز برای تثبیت نظم جدید دریانوردی استفاده خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/676600" target="_blank">📅 11:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رویترز مدعی شد: نتانیاهو پیشنهاد ترور فرماندهان سپاه و ارتش را به ترامپ ارائه کرد
🔹
خبرگزاری رویترز در گزارشی ادعا کرد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل طرحی را شامل پیشنهاد ترور هدفمند فرماندهان ارشد سپاه پاسداران و ارتش جمهوری اسلامی ایران به دونالد ترامپ ارائه کرده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/676599" target="_blank">📅 11:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt_v_g-BLFJDkGSAR7OczQLRE-nFJcrYDgi49hCWsrodHH1K55rNpeoYzBG_Ctv4IuHP2DUWwfKSsSiKA07xKEjOImp_iHDsYnNX8uAd8AT0_X_MSvwHDdQqOCuckoZeag7urtD2ei5b0k7b9beXaT8Cho74TT7qXd6wL3cN5px0c39ASjwnQr8WU4i6-vs0V2iFKEQaWflFzHqwl_VtAmX4nu01j2GjdhQ-lVhfZ3nXFPVU8sURi4SnKAxjgOgQP2ZXywEVoTYf0pANjNNs9xaope17EB9b_urHOyvtx130G5X_qDpF4FH27uZ1Jre2hMAPA6i4Fpfje4yA_myvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: ترامپ در جنگ با ایران وقت تلف می‌کند
ادعای اکونومیست:
🔹
آخرین دور مذاکرات به احتمال زیاد یک وصله ناجور برای یک توافق نخ‌نما خواهد بود. جنگ بین آمریکا و ایران متوقف شده اما پایان نیافته است. تنگه هرمز عملاً بسته است.
🔹
ترامپ از تهدید خود برای حمله گسترده به ایران عقب‌نشینی کرده و اکنون ادعا می‌کند که مذاکرات به خوبی پیش می‌رود. او در این جنگ گیر کرده حالا وقت تلف می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/676598" target="_blank">📅 11:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد  روابط عمومی سپاه:
🔹
شب گذشته دو تانکر نفتکش با تحریک پرنده‌های آمریکایی قصد خروج از مسیر ناایمن جنوب تنگه هرمز را داشتند که پس از وقوع حریق شدید در یکی از…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/676597" target="_blank">📅 11:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676592">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e83e267a.mp4?token=OxrnmmfnyNALoUzo3fsDvv69ERqRECLBmanGODfe7uJo8-vRg5SMr3xLkCGhAbrpRiA93cVDtJLwlgOI6ce-sR17ZzFZfl_aojZCxIiZWVZFY1zCd8Q8nCveeGytICzy-GI1XntXcF-AVFxqyMNIhhTwY3z06bvaXOJUVBxfiM5UFfqXFa-0nqql94r0fUlowVPD81D_s_5TWD6BqNDyYi42Q8eGuOiBs6XmykrtbQLppjbQpyRt5jMvum-_V3s1PToCXFiDkA-RvYqFx0DxNn9hhBcT7qYMXKthSvR2dRpUzQqZCffqXfEoECD4PKG4DrGPLwhJhBAMInSBQi1IGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e83e267a.mp4?token=OxrnmmfnyNALoUzo3fsDvv69ERqRECLBmanGODfe7uJo8-vRg5SMr3xLkCGhAbrpRiA93cVDtJLwlgOI6ce-sR17ZzFZfl_aojZCxIiZWVZFY1zCd8Q8nCveeGytICzy-GI1XntXcF-AVFxqyMNIhhTwY3z06bvaXOJUVBxfiM5UFfqXFa-0nqql94r0fUlowVPD81D_s_5TWD6BqNDyYi42Q8eGuOiBs6XmykrtbQLppjbQpyRt5jMvum-_V3s1PToCXFiDkA-RvYqFx0DxNn9hhBcT7qYMXKthSvR2dRpUzQqZCffqXfEoECD4PKG4DrGPLwhJhBAMInSBQi1IGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ایران را دوست داریم؟ #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/676592" target="_blank">📅 10:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyxmjOCVH3cp27U3rKnYWkm6jnomxewQwwcqzOD34jzqds7h-7hzDdG5K_7anjn1gK6MCW0ij-aqdbsTYBEg2ySeiWRT5CERR6znYidGouApJqZXFCUZujBtuzCt215y762UrBZgOcPriPmiqCF7qSvC4bqA6xPcoNGOLbhBMiIxPpTpWP5J4cChBU50tlMgQSoxGD_6Z0ZwPHwVngn8VpaspGWR827Usiers7wUL9sTsRce4WraNBnri5JHyePEYqY0idH2Pi2ymSjqyK2fi7gptpV-VYlnVVxViApQoUFF2duNbWUmQT2sWicaZG41jBZERWmML14wi_mrQD4CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا بعضی‌ها راحت می‌بازند و دوباره شروع می‌کنند، اما بعضی‌ها سال‌ها در یک شکست می‌مانند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/676590" target="_blank">📅 10:35 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
