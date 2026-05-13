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
<img src="https://cdn4.telesco.pe/file/Ketya-euPyOJs1jelSXmZEXRhDjwcy5WyMSY5PwHXeQTd12ZWr7pZLSDenEbwUJXKSFWAto7742aUZsxdPQAi8QjRlxWoZewBQxxbNLGwzlKYbZWFZj3tPDQtHML5i30XANU41YtK4Mw8O2WgsTK0sWvvWWU6oWwpviRvc1uhNf8GikwsC8CfROMmWQkygYplaYiMN9CRbC8JmMUfP--bSwDaOz5swhiDD_SUR9rcTA7MkExr1DGZVQpnozKNan_4rUtl-nVqQzXisZYEd9uJPMcYav5r40YzssyBiV_bjaSX5UCsbDgBCOvsffZ0qQxcFL-A0sH7nBPnLqxb5lHmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.56K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 05:55:22</div>
<hr>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 400 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apQogBnh3WZG7KB-cRr0DnhU77JQq1C3TGphnZxfsB7KKRhVNFfpSS8DVG9tMXh8c6fw0ZA6RXHmNpT0iIT-ydHsSI5VO2ObyKOoMNWfGE4Q8O0D2THyw_RO1aqtLNjc0OYZEVomtT-H6We1xYAW5a-Td9P5k2LouAflAfVxHtVJPiiMl7beRwgda85IPf5YylDH98IxH0OJd254nFaViB1npb1nzTo19D04GM2lKJ8miwQfMFbJlBBNk7PKbHTMXS7AlXjoX1FVpDiD47icEMXsPXq9joA1fQOYf-1FPCuvbCtYuov7GmImiefcqCpNYTzDuzcIk-HW4yopl0R4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 404 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 575 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjm_-Zc_q3B7mXlIGZ9wl9EHYG6gpTtfaj95pOR_2k5ubEf0TKwrtI8eRlK2jYohFnUjlDnrplCRBl0u1Ge0PLrYv0fr2kwHALKxE2KXwaXCVVtpdQ3ZrfOslGgdkofpuWOh3PJPLzDgHx9KTd9ZC2-1eSbgKUph4egn89jDm7ZETT-QvJW7toP1_3ZNO7k5E3PE8xrMzG5Lt3En4M_UG2EEQK9j_fLOJAxrEJHIf46pmkoa3mWjAd-y3h8gVoSzx-9KEeCzHxVfFrfDdOFH9YgfOdOHs0juE9KWkwR2JZV2UVYVJz7xvg4QEOxzQQIcttTzjxOeph5qSPrinxwHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOfcAY4rhbzGbg4hOO3c1gViVqGR-QSzjHTNoq0r_APX9VsXtBHVBISK1buggbVw2BhDVIscl7qTM28LdUg8dm7jsftvD_2fjogN75NxxjF7D6L0tkzWL7WonQO6LgjFhmkDZb3gfJ400nFO9WT98opQGF9RwXe_vm8cywuoe4jhUubi54xzBaqkmj0mLptkO5SvlRCi1kmg761m3bO-D-8mkWLmlxIRaIKan8cLEk5q2NfWLCqffuFfWcijlMa_5YFabqY8iCzGJ8pPbXCXDrm0a0bACxFxMEKZQdiETT6Vr8qnWlpSAILtFFmYIHREHT3ngwyDaYkd9mbBajmg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwAmbMraIVx4BMplm6-kPlRqxonH1Mr8VPs5n9zVV6-poGSnxwn9HgS2PppHgUgwl4JaE5ucVi7p-4pnyJKmN2f6h3Pb5IkYWgZr5TkJQnMrvZbtuceYbPhBMsg4igiDw18CqXTquaPdd5I2DqL3ZQS-UuJAQHvF4_BegmxtiOwrNKCXPgG_rK_znMjGkXfJJINlmrft-K78SmSceSze4ck5MuFobdWyF_X-aKUHD8xrDMTMMLloIn-ZAIY4uuxwDdxr6ssRgd2c5yzuLFT3Qnnqtii5MO5zey-G4iWtRx7J4Z6M_pHImYI9GmUpDPfq3wFCfIz5DFDBouSj3jNJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 738 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm9L2p_YvBvsTIkVFg6gGU1VAcxq-ZBQP-GfRv736UwcrB93_xPihmLKBDHnAgpckJ4drKyOHT9B2XZbSr95ZWmIF9mDl6ofrf1qlwKKEGWsp26oaQnZKMCMylHdstfhbzeT3NLDLZhxOxXAbP-seB1orANAgxoD6W2YbaXbcqCcwtCoCNkJZ8xPsgmqHEkQMdIXEeGiINXTnn_2ABQNwip-sZL0L7l6r3MMurBvf-VunKQ0W8EtffBdmDISHpGPWzWR_VzSTR4f4aMrzv-FHOasHtNG44Eos7-h-EwFt4jaL30BrX0q8Wqmq0UNWAp0fPmFukw0zP8XOzri4iqnkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoeKuMOir7bzmLrjvSKzCSgLi43527JGo-tJB3FRAmvimpsLu-O98RFI0fKsmE0IkrVjnkJIT_-74XMwL8J7F3dRuGWf9khOTj79nXgHfyJ1cCsxO1c-aUvUn7hPgYp8Jvf5v1mTyXKVSQzhFEhXSVfbT9SLnOjkxqcm9P-XjsMcaKZ5tOzX3bCTQBQkIIVpWg6M4mTTLSsIsCR-8KCh6prOwk_HnfAG5uJuXLJpbe-vgV4JIpFS15PZqbfHHcMIRk1gXsw5o136rYpQdcGXrJaQm3zz0A7KTEOi15DsXXlSqUPBAR61nf4_bxKsxJKVgpMCwSm5IoqjIlUdBZG6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgXeP9qy1UtXfILEFfJbYP7nt-XDOOHnxNyKIbqvYUfAJtYaYcBbNSnc4Dro20iwM7NejzTJ83AKHBZwqljqQhH13G_vd8xRc0QJO3n47OJz_WIOg8cuptFri_8xKryckMsO4_NvGJuid-sKnftnyY_XPY5b-cYhoz4Zu_D9JwryR2M9qf0PcOzzgKyfKtByFfQg4ljjhOA6FKr8W8ltv5Fr6sl18DuV0skGG8KdYnPsialOZjprY0zeYUxbbtavpMdDiIAlYZmmJcBq81FpWhKWWbxAb9QhuQew_ie3Z5kaaXL_1W6BEhF2rgbMDr40FJqWp56PbK0qZWjjR29FUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0jowj2gfd7L0UN3_2BZruzjU0KoUWm5Vktjqz8TWq_D5H3MPczAN0CtNi_dIXROaqh8YXaf_feaagRzoI5sJRiaoL8HWC0fdBVG31RRKFEDKNfCC7Hk68Uy6bd8E2Yy2j-B3QdMpWNp4GjYI6drbrDLHgsw5lyP_dSBxpbudegTKpsSgCH59YZRx8lB0G5Awdqb7V2p4Qtgr_rCjW_-InElujXQUcmhdLjKd5tFZp5JzT5WoN_hmPRfycIx2gaoTKz0km4lZkjmNJfub9gIjcJ0_X_ozZLeIAFUJ6EF8luUsf_g7i6KTFOSOW1GvRaH3pmBreZoJogNHdNkiMEMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvkYTX-jYPp_NE9IXnH4GGtYUJUJ68zYXxkNNcmke9_LRnz90BJVNP8jUCXoG8zBd4WbiPaVZ3a-T75NfbAxMi1E_rlmBKp4XhZZKeaM3tFZX3Wei7qbolIV9f1G1zDlEerZd_KAyytlr5L-hRvvFe6R-h07XrRaU1gJrRl2Q0-v2q-JZyNtVdm8rvgcPdxCWFO_1KtTnUL3urZhfMGjdkXdpPOvz8FEsUS0JhNThXExJQy4Qlh8o-nK6NX-8vCkSa2z4q0UzIywWZsfXGYeQISMBmq7feLzsOBELTdPqgY0LWCM6ae2Oy8flQVthEIga2wfxpXsAHmPBSySVhv4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 748 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6Il8Lb0r_174kDiVFyuQuKVX9MQL10Vu261zMZmQe2wMP2pe2jj4bbeji-L6BUB4CPWP5Zm0hSoL-PR0Ly-a_q4dCdeudjiS2m-OqKghEr1sqdhEq-TJLvtssF05QoxC3PC8ZdD_VkVacJyek-7FaJkvhXcWLxslXW6-8MnB-PUQc3u2SLKiijozkQNeKIKAU-4rx7BVg-Kfd4hR6kTwkyIWG9p3zBvIPhEOXpMPsJTgnHiexrPl_xMoxHJs4_dgavsU_nIB31-c7FmSj26xrAQfEOoTBoxAJgEvv5z_Q178HObOTcTlowOs8br8ypfBd_t_9QKEtksBQeMbka_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYiMH4p3msnKwQGJ8wf5OuCIoa9Zycx6i2qHhw-uKMPKrSoGo-bKAcSsrONolWRkPvbvc4Bt-7-pNr9ETAk40rASRi76efrEM_qwPMPuYkpAFvegQMdwuqZWjQy1cA-aCW8NVUJKNZuSVXAkCSDuCI7O1bBMoEfNc6rCVv3d--LPJkMZtVu7IaaI8xc7hi1Ruh0JpT4tAYaZOoKkfsTOIWnVFPHpqxhaDWV9Iij72x_9X1UKglMHXpbjg6eEHV-hOvPjygWyMaqBmvA3DifaajxGjIIrJu6lnSvrEddvRnZedRljRncjBzr9NI51JEQp4_WCMUFsIKYiPuHxgV2bMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHs7wKRP3vkjlhM9tUXT5aFKLM_MiwI8sFuSm1xmi43O_ND58DIUmjejszk-V_X3o7ydByY-wD1Qgfd068z2Cd1qTxXhvxJv9XyTeqzm6jHkClKcmMNRiau0PnqbZ7g2Q9fAeKJeJJ3A7x10d1q9RaNpivNoYeHEdiSynj0wk6vmTSwDFE5EfZg8ohe5xAKJdMd5AFWeUGbkjkJD4Xx5dtwxT4OOSnJyXaIBM9y4JG1jVGutiqI-Dt1GqcGxITfvjwzi09A26rkTH5QaeytChFSvm-Wr9xI1GYAxYPQXPQ-M8x-6PD7LGDbfDyN8rZm997xheQBSlbnkSozwOxey1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEtcPDisMeEHqAsv8dXHmPfqa6FPDcrsFwiYUPphMNgRaYauaFrmBQ8wMx8lGu__XbzBrxEbbXGN-jMdxa2JqsRpDAPEVurnnRU--vIglgO40U9GbM7XN0Q4y2zzAg_PaF_8wh32IJEW0kVdINBZXV8erA9q34Ic5wsWaZTA22Sod3WnuAbeiWpjYzSGUp3giL1J8BnCYen8SV8p9CWpnH-ytZLKFjHuwqIdvpLeQ23cHQii-CpnXOiMbpWNazYbfx7-e7AQKlE2T4gsuSAvpy3vJGoLkaEWDJusDorcFRD7_r3J4kxPvh-2PPR-KaFwjQVwBUrJPYsfBHgBFuBUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPNrZ8_IXcc8BJyxivPHeSdXtT3gDIJJSTuv9Qfm_WNDF-miS5X8A53vII_lhEpqNtyWWR1gBtepRGh7HG6r_kTBT3FHpEUZ1XSN4qgTHmaBtGOfnw16adnPCZ2OOWLTwJsLdXZlqrDn60W9KEzZkIS2ynHFxbciVYtL3IdsI1-ZvdkamL3WcPpYV2izi-Tw1MBaykwpRou62a6JiwWY4elf0_T2qLx2VSLfAee16-YyhIWxMpHHqePavQ7CXBm3s8Pet397btW2kf8B7TBDOe8bBYbpJu3v8udEL9berivdZOdZ1vQPORUS2dEreKzFpWoHFrJ4oDjqk10DPjvaww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtjOfU3pWwuSWrW0wLIE5V9ZDyY5ZMDrwPp9n3JfEy40Kbbmb14LgLHsi22f09-hUY3N1dXu16V9Odm5CSIgA-6gmKQrRAGAcSFFl5vSEIjU1F9KYU030PCdejEzEZMED09vwVbhP1KP9n41suMBkhsj7XiOMlctR40tZVQrWqvOpLstBkShHRf4YI-bWdO5aND_CBpV_ikEANade8qkHamVDsg8mALo5bDph1JkyGEera3yKmtGDlSAZYprFDIi7PG9mvkVRRqwCX54_Rt3PnC7iCHW5S6X2dHwZBFW4PMg_BjtdL3q4zPm7bgw5ueDIMcqJ-TpPSxmXG0vXet81Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOMrjrj5BxHqE0w7ltgdoMOOPHyHUP8YzP8xtd-E5pR6k4vtn4EVaDqSkaWCtHHzjUXY58h4lWp0NzHqpnEAMzFRzAkemjFLWKGdXvs8pvwbQ3beeVpeSDESNP2aIKxEeD4_UMFxHWyQ8ZZnJBAQQCLY5cyYlMIQ4XXLLmdSHqhc8fJn0dOQ8fK_hIVNioID2IbmTCsyUzcDB0809JBHR9ZUOpTsiksRFZQm0DzqVWlqv6vIvvVRR5vRuKiuR-vlQqXbNPpvG-swIy3qjTCh27-lqMhpYJCW1t-kzh6V5nTd1YpFt-7mtlDGHNGBOmvntygWpjvcYwcw-0-1MDQNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=uhH_3D_FjstNVFUVrPxyzJmktagL3VHItdeiGEMJvFKXeAizW5hbBMdw_LRmhxk80UjLk4VXsE0p4GhMvh-MUG6aIMmQVR11dUCSyWd8zMzEfTljPfryScchgGZzLzXyyzInwMAw8nuOV7yH2HwS8horrzmHaIfcM-jHSJrj5zE7Ip9anF0CNeH6yZmOj_Nl6MNutHLM_1F7JiFr-Gqvg4757lnJ0uxxGWS1ITEYbmbhIbm8sjsKX1iBY5HwcnVwQb1QffMTrX4aBP3dpmWhlABb4Ngwl-dHKn1GudLuV3qiHK8i-EaqKRSWfoQPptNctXPs5rAYmDFh5Eetei-Stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=uhH_3D_FjstNVFUVrPxyzJmktagL3VHItdeiGEMJvFKXeAizW5hbBMdw_LRmhxk80UjLk4VXsE0p4GhMvh-MUG6aIMmQVR11dUCSyWd8zMzEfTljPfryScchgGZzLzXyyzInwMAw8nuOV7yH2HwS8horrzmHaIfcM-jHSJrj5zE7Ip9anF0CNeH6yZmOj_Nl6MNutHLM_1F7JiFr-Gqvg4757lnJ0uxxGWS1ITEYbmbhIbm8sjsKX1iBY5HwcnVwQb1QffMTrX4aBP3dpmWhlABb4Ngwl-dHKn1GudLuV3qiHK8i-EaqKRSWfoQPptNctXPs5rAYmDFh5Eetei-Stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHPXpF5Vpe38C81l3iOoI4c3xJ0l_GIxVnOCxaKpkwjB9P9HTvW3G-hN3JynL8ThyqqN7P-0yzzJrzAlrniicM2qSToLUR5QMIS5I70g8e4g04-VISocEjt2Ve5zmw4UlSw6_uF2wRS5WIXUFmBWort3P-5cSOenDm_fTA0zx2U9o72QBd16sVkXw5rCsSbZOVoSDi7QniT-KXQ9c_aBTYXhAwUBgG11_vyrBLou2JJHQXks__VRqXH6mBD2S07x8Sj40uFa4J-tgsYNNVfcVFKNA7ZxThP0bcGC1Ah4Hj-OhQby9Wdg0tMFR_Rn0WXCX2yI5vvWRlxs2wKdCBM9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0SQl-23Z3x_u5-vJdoqm948EwClcPBrBIwNBEg52oy5ebPF5Qta0wFuSR9gpp0X1l11FsOHilW4EYaps5g5BG-2MBwj-KyELJ6Oeu50mbaZHsfN5QEJAN30xihTH2ziGsQt_zxl3nrMH6J4TZKvzefnEg7vZ7XaUdWEwOHo3hmceN16qScuEpklNLxjI2m9ZKZeE_6BHqIH3ylo4B4cTCM0lhEsDU8xg4xhNgsu4-8QXDG03l9a-F-VJjtfuTRlxltO_qYp2jXffy5reLD26VTVpOA3rdEatLIYRoiCKrNGilkCHG-s2Sb50sUm_ktxl5JHIts08Ru7A6Imk-yzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3XQkMSmuA-r3HPXUQ5YxXoqZsZp0OKrpjDeV42TrhXjM4WJ8ezIIEmwt0f2IuZs4uarRmHVl87XpSSAujC2ljv8p8_FZ5IqKxAQnzogEUuFPqegEI6UQgpAfJ55Gi_HTV5VhnDC89HUB2KI-gXwJQV5zbNYZe48FO4Pl_DPuCucz94zP4LDmqnQ05QuRjRfFEzEiSK0NTt472rZyvfDqof86yx49w9U_Z5Z0-v4NuWTyJYx0dTdleA4gZ7dAvLLHhjEFmuM9iu0DBVHg4lbGLSDNOK5KmiUOY9iIyI8pKridmFdHKGd9tFHBmi6Y1cSsiqb1VUIPRc4yYXKwOqX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apUt7MYMT53yDTpeo1fMAEyuim7A0Ue4JfW0uBNLZeL-ydBeZwbrt1xXUS6-4wYubtd1hUXQfkJAUB5Lb_isEwPJ-v_MJBYBb1QS-9MRrUXU4XcuCysn9WVMVEEUrTaU-voV6WNQ7CkSD7T-6jVFcMOnUy_a0qrQ2ZlXdq5sM4O27pR1WzASp9XhLsZd8JgYzrrafeHgBDJ1npTxQxuMUwzgJNB2WQfYjeP43NAkmws6uuI9KJYbbRQHivrhM7DRW-3Id4W12yje4zznzAQnGjffhgHv-jo8t8yHcCFxnfd_jxTBLiol0CcAJMWOsMQ0PVghSpdqetuPgoSs0iFDEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8HXJZXxzjY2wi8QHpn7K7DBUJAk04VlQ9pg5S_6OktWHqRGPXkgQqKhbu24n0-Pd5cEHp8eiUFe2Rcx-OkcW7c_lR0wq66Vg2PrzTbMTq0TyTZthbYI8XQOSf9T9nwwz4wr0bIBRG7pUybTwvHxfKjYCtoHaLoFrrboRMMh8oLVe4VMhkZuqNCEeBeM2NhpFfSpq66lHC-uNVo1hRkCFzMOziL2XdutvmtUmSUKVXhouuKtrDS0XcGU65C0gOI587F9C77E9twKQHOcvJmtHeLMSudKQpbVmwNtXMu-A3WyV46wIHTS38-3eA2_zxYZELIpn1HStUHTZyfRBKEGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHWu1ZUzeVdZ3mweR0HUgJC9WnXn74j9tR9zYAA-LIJMgxav4RKpg5atBCMsRdGU3zv2KFhH2bCPVt0k7099a-gs3MnAC57LI8xpy6YG9ubgnp9WI9tGj1g8YWzPEkAboxI_9XFbSCb4NAP8YVytqdRxZJ1n87Ih41axL9RI3u-wERxJmIu0MiKcREA-VzouhKW_87TPL2zpgsqw8K9jsF8YriZkt1rAMdb_2F-Cf__oUX35k35spxvhOjOJim_9ssWzBZhHqTbEqDV4v9tgOgMSE3bwrcviwO9UrOgO-ArszGm8WPeNXjWGJ2hV8dtbBrywqyzkhwSm7t9C5Z0U1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 739 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkvIXJKvdmufWgq658yvOgDiTGv5mClpW74MbLYlLFPcA_Co4R9sYPLzzNpmt0zYGsV6g3IGPlm4a1GpXpdWhGAxJIcnv_bCgIrV3-fM6EhUMILpMYM69aTE1ePvR6yAY-5i5mXFLVDu-cZGgR3zOnjagkXEzyVOksYzA2zBkL9AzMBLjStnQJ9pD8lp1QOH2VJucdVUJTfJk9qv9OzJIyFk5rjKf9tN3nKKIMiMDI48qFc_ZAZjwKsZI1udu7JSnXDk7B301QWTGWStgGm2xtRZUhEHDYbmCCdLUIZxNYX7SYp63iMRGQMpkp_FLNDBBsUaahdB9z_nnsSQsFlfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwNkUkj7Y0Jkav4HOexLtJZSbTyaaK63jJpgVw9AQQiDVpVYWsXCXETKYjy8R0JIC9RZpPqbsXkX5HGubRbKav-snPEf4rMYn0Kssz--0Srv_AF4digsObmWXAX1E1R_Y46ZK8Yvy9ebopHtpQMqH7MMIYxT0Ugp4IZJ09b_z2k-Y_Oum1-D_4EDefnNaYcSwu4EFlLC8Xy9D5dI5Olf74rUM4QL6zYjSBLYb0Rnyfddl_EMEQJq3NPrlz9xOze6g8gOKEJmg2HqyB-CdTYN4Xe6vyjtye2aE5n-B6z0GS2bTUvfjBRO6rV8o8i7pkwy2Q_duZwzHkPId3znAa8_Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-GV9iRC6wZX2oNHBEaC1SK2B8W8udMVcxa-w-Klcyx1DI_nMO_sQW75_k59oIA1xZKm990Jsi7bIde_JoeT4p9QEdPI5RA_p9EmVukzs_jPo1jUGXRou8ihBgIm9brFwx5C4hW5-JlmexJd-1PLHAwaBIAzAbV_GOaGDPm-1KNvr1tKVeC-_sl8hFaPLYhexEI6BL6e0Sc6aA0batnywL6eTD0WKMKmqSGf8sEBG0Ag36keLMga2Fm1cqVwexAO8XmcjmOdiJtGMadLXxEgC9bMtXHejBmN0EKmDzlqDLzT5h2CqFuxx2L164gwvwrzgNJ4BAOXLgIFo_t2AJ_p8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KT2Bz7YHTjtu4idw7Ky72FpaVNL8wCV9piugiVYYvuIpAqGWoROfBghikdiIW8sI54oFDTAz38oONL74cBnVb5katIHwIYTeM97qTabn_kxxWmAmG-aXCewam9dVyEln54gOsdJbfiNGhuNazeUPz50I0haXcNxE934Kdjz0HCpTZrGAlKehEkvlhRqOPHhinMXChFKxdQEP1QxDfvJzmY20GQHkuuhjXrxt-CJNQVAWTJJ7eiY7Sv8ry0wfIh0Dyu6Bmc0ZQYBMNgzbLFeJtvoT8PQVyrDJqAIVS_q7Eq-J3qv_e0ZhMhxnBLGqOhkG0ftN1HwtVoGROi2CYaB-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL_55KWE7qPAoyMh5piKTPUeAMmMU-sM0joDbTITrBkynckZnlGgUaqPWuoWTdeRwiA-ZpvE_zv57qtHwMmIczjZR3QjfjHWq0ulki16x3D495wgmvaMpJ1NDyfS8c68Mwvtoky-qGyawF99F5LQkgBz5uqD4Isqya5yUZSKtxsHae6mTX3vAk8mJ79B6DdQuFIPLIzG17Y3_C4HSV7XleYjrXVeVvo2CfjMGz8MqbvPOHh3X7NzB3ApYcAAGVA3by1OHsBcrDWkPAPXVW5EQGS6jQU01yupW1EE8sFDqnl-HQX5mMqrPXDg5FBPLAcMEN19MJ3zQaksNGo0eKFcpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spl6w0OTRVFzMjCXG9MXjrnQxw4enUiZfHhfup-rXx_JrDdOC90fU096SugJBMawrMqPJBRfXTjsSEexB_vqDOjMsPLPVevurfWtHR9mvt1szcttGW5InWAlZrv_s7E8AXOaTjC6fvEujb_9g6d03h2gWvZe5T5g3U8vISoi6sbC0kMOKUNWebDUQIs9nA-3-U2Kh5pmmINwKuVH9dFHeq2xpI6DWkzP_xhcYvOW42yYbWlmveVAe1P047QU4IesBHQ34-69E6K9fhsPXbbakUls9jkG5iB3SEO6U-nl3w3d-eM_ns3MQdBIuUhhUBGauckpNlq9o27xLfGLwzjEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_Ihzr1s6UPnBGvzI6JYBzZPBu996BkFBiSJ--Jk3KBycNMqtDn-OO32Tz450zXAUUdQkrTlkRlpTZZtX2pk1KSSg8Zi9SkM5BNBEx2ARhbhh1I-yMfrrs9cNbD0Cr2MF31u07KIc3mgTEHn6WwBhOBtrovD87x3PaHieXE1ojplkBKObdTEnsaTqjtgHeDGmW-hUAKcSs1UB1FcpHQorm-dOhjZ4V5o2RYxxj2X7a8QEWwZ1T2fxzHVD8dK-BBzg_oqwVOVm0gXwbExJuUZ0jNpVDVjwANcyFm1A2ssswty5q8s4hbj1ncxb2ml1StxZ2HDI4o-pQF9xPfJJ1VfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzF4xgGL5MmB7Z4Ooe0IMAI6tXcR6FtMgZ4RiACLRMnQqjRnEUXheYRqF1uOB-_-LHICfvkoRGLEl53HHND3f0DWXMdkDYuJlfto5o5W2uBd1hd9_h0yINkEJr9HA1MGc_3fY3_LstIemQgyHqVvADaDXf9g-3WaU3cZwiYJaxIlGyrcNl3z1YuQyFaHUSUM93UMRdREAPp4GPZCxzwFAStf4MXfE78JVbbOj-nsk79lZevbB5GFQPC3Sy69FkZ7idB4pWlcfQ6LW3HyR2JdX0H_yl1e9dRcqklzcCQ9AwO-x7-2Dd-YVCpZTTx-X6MpuFABt1Bq5DeH2rTeeTppPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgpNC-P8PcbcIJxasJr4ERsg80owchoBMv6yHBo2OELcQN6nINudeW1puIkvs2Po6cs3BPMXYhQGwP4C_XaCWoN6KQsqizYxOXiivL9HS8B8w7oJuEGrhMnQsKEO8rchFLNGVYotSbBl0YBuRViHLKEo01hsfALwsoUdGkwZElhVswjt95ZCTlXjJRe7pmOH8nL9XhJqyoA_-apUy9ltBLA1wtERz8l96PsJ0o3zgJT7X9WtW4JP_D7LlsLju7jwW9eTAOESFSb1_z7kFFBBhx-pmjAYK7-y2PHZpkgKGpWF_5YFJ0qu5_vzO2KN0U1STDJ4HhrnaRYhbI8S-JPK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnnQJrBHH_Baw6vkvP23Q-sxEIqGEBMP93mU81w56gFaDUmM6bt_TdRGukzC3exAbOQA5UVczDuqKdEOUNcgwJ2mdkilGZBMSA8R6S46yyF7ZmHS5x2Kk4XVXiilT_Zs0O6vYb2CN_RsU0QzwUFQvZXwtzMiSSppN22G3iSx1SxwhNoSvF6r3qfFoUpq8icm8aq0mcPb3CrjErVHufK2x6RQDh4SQ9qht2nmvE8HjcsA0jSi2E9-HN30rV0RUXiR6fwd1urgersCMDyRWDykL1SM_2LXtfy-Do7DXZu07uZX7WSmdon0y2czkCohgnjF57Lhg_s1FxHnk9QZZs5YEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoHksM4XmF_utLpRBJyBrayqcYWEKuJEezXEHbVSS-tiVNFkiJofOuxjHD5At41I1eIlAeOAIq8L1FFmTyN_MT-I8SFsfQETaoP0Hz0cxeZmtHIi0Pe-bIINKAZagxBI2snTnUkOX7Z1cxsfo7hsasrLpok3m2ih9EYxMEX_hZdO69cFDBfxeuHF2Dy2y0vVao5iJi7A8s8TAkdUmSw3QGTvodt2ElITnyJEsDvzBtGffRia6rXlAv2I7bgxNhCGyhvDwt0A4TCvZSjGfVHO0iTyfmE4DCEweXkPuuPPD548jTu0ODxdZ6V6qgiin3AaB4zibu3CQfQauojwT4Vh3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwXH7Gy2ncRmFW9qEhzhMq0-7wgbhD6WUN2bZBV_bH2dJN4sEZxJ4ofiV8YsalrjSPXvUT1ehL6VEVgB6irkfQ2ohwGv3KohgdFr-P3NJV3s1gx_wX28pF94xFBFrk-WUWTshKe6k-Hw2u6vbumMIHmxhi7lbGZmivbyQhtpnpWSfBz7PVCKkByKeKWM3cxHfJzs98PyrdRAGnN9S9u9Eu6sFC5zKdgj4BmjZu--V6Vkt7yxrOLEq7Q1hjgTbv34OW3L1DiMMU05Rf-31fqThPuVC0rFULpUwqlEDO2TH26WJdARZm0uLcSY1XOeP07VBb9f8uHktzjhZjVZvuF-Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDPk04HajOL-tLK7m9dupWLDmVKejRhCGdPhX1gCRMKyrkISYqWLoep6lsxPjPkCgNpF_3E_OX5H7vHIKe3lvhqbqcIBJWGaZAMzzAC9ojnpgrUSZtW9wMWuq3rdOFeE9Y3rmsM9WXY0v0y5HEI4rDXoH5rP3ElCMPf9PThZu96zUIyVsU09bGYrQbrX5VQtvNp63s3Nevb4xKQAswopiZT-5zc_Um-moZuVsmUf9LFJGwsSUthACV1_nJE6MuN-dEpHL1CYUAzyWl_JIreElaLLS2v5G_kjNdkAULTrgPr6Di2hEyoUaTUJ9tmkq7UHzv7aKYErDH-WbrK7AjDXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se1IemZAiWKAtVNWWSMx89VEWrlwY4QO9nKx1rHpbSULsD2ZD7HYnmBl6VBaATb1jy89YUd4ztpUDSCk3VGVWRuBoNEma6e6uk4gxZD76Ppw154lmQCDCMEtj_0JmzlbNuinu0Njok05VQ9WIkH-xf-Sn_48M877Ydm1PMWZ1wIHK-HYeIrH8fUehZcJfyq_JCzV_qBRBaFUZ75q6Vo-cxAfy8miTx4dkSksQf83K6cNQELUxX9JhDD6lBMgzznOgGouxSHDSepXWt9vmn6DVrh4Qa_-3fjCiInQsC7UMK-MGuVkwp1W_CmAWTi8dmkt-v67_8ePWqSAxrPIKqdieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ8mJKmX8VDmpMmThL4MR7J4TvmRGD-WQ-3opho_0I783ZOmBsIYLVnpW2jVeSPSD75daAamdc_m_lFQI3M2lqUgRJu7PuIpGFoqci6XNI3_ThR1NgQibThBJ7HfThHtrOPjMj0z9Je0vFEJIODjqLgt7_SDjuBzg0QaucxfUllSYJsPh8jd3kOZA7YkkVpx8XUdXGl0wCVVjtFMzZg5nY_Qx_opKwPs_KrFwE3I9-TlKACTVQrH7AgTOvOm6fmhnrKT_TXPV8xdYCGYsnLixjF_Gev5jQzX7R_fS6J3gQT2m7vAXfGQ12NJ-sdDuFMAYvVpOGrDMuno1YBqkdk0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeCCNgyJIPt47tZbAy7_DrGS3u-dQ6HMl5CBO3qwKR8unzUGpbKKsKafdIXntTa-xEiXfwg3eOVeBNv1YrWKezzEPPaU6iK0nrpP2AZgUA7TnPN4_E8TB3HkjOn6-CnvudfuZbg-pfmTcWGXwkUpU_le66DsWV34xVqGCn3De1WA1jPFVlPQ1mfYCkaU-Fzi3ovPIOJYRmjzp_5gvoqP3RvIeVTqK33JNSr_YQ0YZaBPfIlBGmZAsD5l7lAriPIqad3qIX3hZ_RNCVD0wV9CabVmCAOu8pyG_lYamiOTCpu2SPFpS4-pHSOy0zpeWobJxZrKhs0eLMQVEQJb3bMidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTP5C5cuTTvluodT3FZ4KHXm2lOM_QL4yBuWOJqA_DCrLzfFamdzarhpiPTVYW4P-5FO2PlhfC2fhCg-5bYgojkyDmbm9FDB_a4mX6VJN3MWgBY4PdozNZ8Rw2ng6XssvgFrUe6uxAYC9XGDnks7i79DUSmgojya-4iikhhyt8ubWQ7y2oPSoyZDy63YOqV_N85LAKmKDNNNMAQI8-uhm9TRzlsTM5hAUJRxK9bfCKq0M-9bkPkN4cK7lkgn4CJOt_iWu9SRwH_lAacYNN2Ok7dsfC3_6ndwGLNrtnCgwTthfW961gySYncu5XolaupuxHZhXUukOGxuxu0zZhptkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSQeMHItpWmb5b6YLEP0j6PiHnRU5OYbkB-jff6DNNr-EpyYzwA1cAXsdawmodctr2fjmCCvoLGbLDJ92mt_ATSdZNAAqHMIO89m4LsXZAG5W93kX85uINYoblK-0Drr-h6O_bSojvZ3gTzq6W8YHmBK-ODE7MT91UyKfRgkybt9gW1KipjLXIOZo4H28gcrID4sQVwkKo8z7APO802by9jph5gM_dsyH_20qqotug_xRSwHGmwyVvKgfpTM4RicbEWTqgPXL_rxBmV0y76fs_dkfLVFg8qmABwSuRHPyUyOO6ghq4AHYgT56P6vpmlTcXwsU75N1SMG5DUeXEf31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uanMjNP9VdM78zULIgEHwHgTdfUhPiWFnduvFuTs93x83Niqq-nkevT_dERVaxqkMS3by4ioo1zrVfHuql7sR_lJ9NorOFEXnriYOUp7sCJJb1qCsQy0a8KDW3xyFXic7bsEKULSdOcSNJmNKaeXahjbVnhazwvUzfIVH8_54NYU9RrGrsXaofJBHeIG0W4auDdtgxrpWkogkci0EPS81hbf5fkcX2y2bEIKurNHu7TwzZHCY0UvY_YEln66JD9Y2-cqnNgyIQ86NOXbzXGx-rGurH4bJvf3CZgx-Bl1fhVceOn0Z3OtV9-AL7TgBAdghTXpgiE5LaOJFzbg6uhp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_UZVvjqKOzPZlGKRR_SOF7PGbX8EEYRjZ7lRMEFpqxZ80efXGMs8A4Ud7ABCbnPNsi_G_zI0ZRD_YTz-2poFw-g-qhfaC5TA5WvWV09-gsiD2HZqXEPMxGZ58B3XIKuef0Ja5tFc89I39cAusAL3p6veAaBLbxHQbNiZVLzQOOrv6CbxRdUYHIhDYLyIvFpq9CxOMUZIl_FnU2maxpNH54YXYbXIg6auyDcWKJ6y-_xdQb0VWTGJjyDkb4-crpgPPU20zdxnP83zMfvoIHvBysRWclOVGz-7QqlG1q7-4ZxFv2NJcPnxGiOL3HAWpD7LqFBF2LblNndaqvpylglXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvRZ1n7W_kh8WDYRk2qLg-44DMfVyFPsq3fYziW4RktQB3lqnDiUvQD2KXSO6z4sis2_KZPh5qkpYGWjDZ_PsMNriTxWCefplgm5z94gDCSgEj-bQgVf8ccndzuojskYkDsxh8z65q9R89Pec1U6kQgP25jM-PdfDMP9O7ehwXh67Yn2lPH7egVNBEwwr87ADfBbAOdYqUNYkhJrXx5BixD69ItyJE-J0C44Bjn2nE42idGk6-sVABPneEmPqZ8MIGheSudqzeljTOlUtRu-d3z3ES-y81SvuNYb_oE3ZqmkuOx9nLy7fKfBwCyurTqZ-REyHLTmsznLyGdoRM5Bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRZEZEcZmBnIUywcEnX2AXCnGIzehVSmbU_OSSGDhiaAJqV1ClfiEJQ_dvu00G5cRAdIQq9dPRjnMgMHvgo8tVqqTxdtsDkdACf15cFcm_9bF0AwEBhJZb1yZ16M_QZxlILCW43wORGk3V3cXakzS7yCerc1JqESDawbZ_Uf5GxSDNhvTGMoQKbX6FCLy_CNJkYhc5lTzcL5mrXwWZj-cG4N473iLQLq3SZmqkcUd6D2TzQkfDQPLovPzkkYCWh3gTqNI32YoElceTqGdThnpQgXtJlICjE2zREYPNxsmm9bfBCAE_8GCOET7KscdaqocD42OuNWKUH6OEqxvQCZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 541 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4e3LY6BsCgfag2nt01uv77ronI7LbdI1chbggwvygnIpplZquS3hU0uApepl9rAc3MAT7PAmupDze30I0CjVejXpIXBp_ABE8feovEIMQAWwp5C41Thj5Vc80WPOsBF3ZnWwrHZzJ_X4tnlegGFhDjiYIZlEgBHNd7YbFQbrTET0HPK63rMr1j6l2BVNhQ7p0FUnNu3XLHYEqjPgic5FFbfrTrz51esCpmNIZjBkZCaz42zN7qLrUVznJLxHrp-Szd2e3JEXMslwuefxwpYJB9qmBo_rdbeQ1CmWn-K7I7YIP40lXxlBSY2cK367flN9UImTiCQAJME21qHLUfRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvphgceNXwtsuK7FGREe8zx7EexFNPMsUCuU-nZ0lDsXsdJo0fJlVBfn63sCNftte51YjkbKyUnTcPLnyhgku5ZBBgtXBEGQIq-YdpZSB-Zjdy0Mj7DWRJ_FSDnkp3med9aov_ak_OJKiYghXzfjZnRHQIVtyhEQihdFsNrh1BioaEyUyhiCPSz7R6TQvlv7Axtis_H3R1TZhm2h_DCAk9lxxNB66-cgZvsaGWNToTtH73Xuankej50O0gjlyfmrbKhbW262oJ1BlCp33m-jBCFEANE4UvaNpqxYdHudzdkuQIipNa-1R0gWHHUoWPx7YnoZjiPnpm-4Y5D0nwqJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 678 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txj6Gd7lajPJesQPuyYXudgIRvChNiYyJr4hL3OgNINnu-j41HMef5ItG5pOvYtNc6bxLmO_8K-uqFiUU6bvX8BoD67CnoIaH3AlmlfyyTyOkFGD01BGCaEmPVaUC6jFce77g1LC_C7pFA6iQTwxF11R1ySSp7728QXJCGAj9qhBoY45w3zlx0UQvZddyUQ4Q-MRcs7sHpLTxOicble2YTmBRYTbw2Q-K9exgRJgrf-_d6zFml3NdE5l2MHq--BmpuwCZ29DV20fKjvqIH8S9FaUZ6bSUw64iYW_6W1zYon0jEI9yvTpqUKih-o3GiKpkrdXLgBBXZwq6adepuZwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptZsdQvQf5nG59GwNgLICs83URkBPAbjsDWHpAnGXclDpcQhMA0sFhy8CqpgbFb-6DFIl5hQiYrU-YPkNHZhp2-aJlCCm_x6DyHvhNpVXUXB8KSjw2A50OWQbwzoT12Mgm8tT-wFDXzJentD2XOJ1uqRR8wWumR57wsM-z8VC6N4G-xWT4TJYorx0PZpJ_tf_SeTLG0YMtbKodjr6sFkklVT_Evax7JAsaGCHzSZqjTFRXPHiSG0hsQvXICSs1rxZccKwufug7C5LrHcu83nivHBFu2c42LVYq3isWOSAfeGIL5KJ7XDM8JwzFqGc78irn-jJkJm88wZZCCKlfgcvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJVX69ggi2gQFTy08LxAqTU9dpypSTg8GNck9vn1ss6SFwGR8jX3OTGocwZDkyLKEAkTCFXgThDHSw1064JZAkKcly5kXKB61yQoMZUERTmuIIrNDzcsrvMgTlIpB2eNm6osk7ugAOwBy7a_BKV74zaA2WW2Tqtud98SNM7t321z5bEzBQcxBzPudJx-5_-0oLwe1I63ApWXeOoz0cKIp3_wJajcNcVjT8ObOMquBzmXLMcg8sZJZb_6CqlmXMPFHO6gDhj7WITsB-EeYrPf4trzwZ5MrJxob3Jvc0kyEAmkwrkfCky3e-5wriDx-NfTKRWmZj5nU96ip6qregu_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpzwBnEfQmRVKH94gFKaHfnar_2oBTZCGv5gBANQD79WGCMc20qUgt-SyKFFWd-mE2d1yuivU7LaP77r8JzIOZiNS7D7WEqQd-1qRsuWrVW08Yh05pwJRNkrMjG1dnVZjfRsrFKCMPX7elDXmtBF-SFQWSfdm8ot6ZYC-VMcwemx1LFIIa4WLfsDWwv4EauYhrJoVOkt5T4QfMipjIFMqqOAtbYWoWkLp9zi34aedpxCVxxWbOUYIvLmHeeCRVy_0Kfn3BUVtfRez2f8NN1yYsxivplPJFrPZImviWH3BWVqbKOBCPa00zq97Cl_RFHkwQtFFoGC7R8jSwO9Lhb1GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJvHrGvxSi0GBQJ9Vh0n838tSbpoYAggaXPzF9UvpMV2CXPkKgHFyB4oCgmyRjGJact3nJ0xtiLuJzSqT-o4pQSS9xQNg41YMe74969f_YnEQRBNf2usDBPfqUQFZ58IsObr--9WP3ysZNIxIe5iiZgv6_oo5Eps9s0himQZHCJjbnl31gmevGv60sEPOjKQK5NAbo8PXBEOd-WdDRN4id3P-R6GyHJKNUDafsEkS0Vmos4BOOSBNHsLtLDHBOzFOU_RyLNk4E-WkqIwo4sB99XszsdqRx4qOvDyentLXz9-sAHJeQqqTGcJTG4MZgY-8eg5BCry6GHVNURhBHjxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ippj1n4XLhXqaOsoo1zXfSTl2MTU6PF6dPNu-AFxCWvMIdhS93H4AnmiG4GQqNgSaMBnfjYzZcjM94L2gaz2YhFV4ii8Rnllcgx1ARhJLLkyHKHW3u2Jp9Qtqna1oqgVxmdK3pwj-8uZRWPTtnN4CUgCxVwQ8WrxKYdfqKzOl6mET6i8boQ5bLE0Z2ojlLotdnF7kdkijT7fmZyuJTwDW5_3Q9qlPLxPvDJt3Wl0h1VlLcYVbhf7WFY-9AnJiZkpHUniS7Ofr4FW9y0erKm4YofzbAm9A_v5IWvodr9tk-xqLhWu-5CnjNPhqjqlml5Wm5Rp_U0AKO4v3lRX-TAStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBdbov0RFF1YBdCnBbcu-DlmDs2Bm-4iGFj5LtcNobxIGmDUBKRFffaJCSapF9OEKbypVyRBTDkqDLasvHiwDimD-w6wNA-gFyTVvQYGinMHakwH3-IhGxbua0T58-tw5im6WSRlWX52cCowTazbvKhdviQ_ZOdLao0cfyUbd3rnCosC1nr25H7Ev2XcZ8GjswaJMUPS6KsQuFYcmnwYjJAra_SY32NpIZUirhccAv9Zm9CYLR4gNtFtd7oz9Mgn1PnU808N6myjC0FIKsUhIoAxsm5LyWOcbj4NBF1Nvwem145oYsl275ggNVhLydq0Upvxfemd0_Jkm62WW-OoDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsBYvdquHFF1HtY2-YUCAIj8hz2PNohD0m03rdudhpzpp1kM86v4vRhaV3NwKQ2FHrnoggwFyeAxPgQwoIQVNIsMoH9m1kND16gmTUv2aRMUPcW0z3aPEP7RcenrEQQXPaTKQ6tRE4BHNcEQtPK9No-fxaaM2PKwcOY2fxEuxCJP3snZAW9__Q3Lc7zso62byCfSodW06sDpT5jKfTxKjUxvCuKiwjn3IAmnIgdxrpAc3SWZJCkEgr_TfFaN1tVc9GEHlaG52R4ySNv_bIIlXjGewcH_naH8sjKsuymJ3efNW9dWbdrQ_gj9v20zikrjtuB8CSy4YQXJb6fYEGomOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO2Pb97wbW2be80pzmgiBW9vJrMj7xMxF1sgQWHeQ8g0XcltjukNM1FNj190IzKxJk5SGmKhbSKFR_QlDQrEC26DIUCgP9O5oebcnPURaOQeB1Ep3fUsgEXY0ZJZ_BfQ_fxLWsjrdYIYRDzEeuqeRad4zYVNzkS0Jy2cOymQ3sgkp0ezIOxGiTu_FGjMQmsYjBmyfLn2SCqgmSQJgJUGlHe9u7zjB6ZG2u9B8Ho6iOakhCBxwU3d27WWyCBAOhpx-tm-97TwF_G845b3uLU8FHJuFhWYvCyb69Sxs89PWlDTJRLuHnVRgzMxXZP6kB8J4uJ8gJBDxV4hOYdNhPegEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okp70wZNFDGGAhkrOm5TX1f4H3FNipBjuoS3jeRJv9Fiiw3yaBhJOxCdJyXdvTr97SkYErbjG9s360MxC1Qo2rFuAJnmGhhnvxSvSrX9H5FE7r10KLTqPvE7JApbtxOkrtu2o9PTeHdgp4QFisj2F7pBZbo8lU64JgTfBxIVcJM77OjXl6aZDzyVpCHGBb8VdadZqx4YaRGNft1p3Kz6VFGjTl9F1CR29Jrn-6hln_lSC0DrZuQCnakQAjcWEybpEiGshR2mL-NhNLDKN9lF1eH7IPj7NBwrxlJ9K5VTmEVP1wCkuqzwb23fxUgezSQik2h2NPZ6cXxWmozDFQ4JXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlowrRv2gT9xzBeZthum2hUii1Wn_kzJW2rkSfyvlJG30OfX1ew_OLuH1rJYVcvbYy6IjSOpeE_U27DF7sTB8MYLFQJvfOYMscF_aGrobJg7LShClSzqmcX-x1rsLgiTbR5dVPSVeIwPQBwJd-CNWbT8kNUOIqFhlUVgkylH_LFAdgw_g1h1FesQTgQiEreepeJMvY4iriSVtMssfPGaSsd6nxFKKH9X0V2cRhaSSlsAadTP4wl-aUg0bZwGHeYxJaxoRt0fylvtoRBcm8N-YyqsXwatsb9BotbsTGujG76PYFiO8waZ0szYUZ70grJ-ImscWtegAnyPMUQLzrK4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mib9xftRoTzIUS32LXQUYNHUPlQNDZYyAGJFFYZT2dR3L1qRLWWm3pZk2_LEyp2YlRUCF3iCx9rcQkOV-hBHUi5rs1YO6e7Hsze2T_Bxtsy8MNX0aquPlVPIz8jKw7MiKBYL0arZ56k2Z3CL9uB9nKnDLUjvf31PKAJ1dR1_UFvkem2zp1xclArxYbO_zwtZ4V1H3cSuct2fw_DbFVrSBBH-aEh60koMW2v8YZ6Ym9-qkeJOCxRy4Mn7yL9bJUJA1nBdp-HPdZgHq0DAhW3rcMNw3KzfW-aywIMEqPWDHM3vTx-m9FGuJTixxEGY90ehRJ6gFXKMm2gyNcTW9ZKlXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gihMyrmizLbZG6dcFL6VSTpkBQH6lJjqwqjVQ9o_9wyaNSPNxKlTbQagvq9cmQRbWqb1r436loNCsgu3XnXT_yRMPSeMlSyBpscUn8a-wa-z8LBD2o2f_AHPhb7PnjVN01cZjpQj_5JNDrpnuTTsB_1tPsB_hj7ABoTZov4UUcDg46elLQ-s1SXYe8iGoKfziUZWQ6_eaa7jW74joFZSU4LcjkP1-KzS1MfRWf4VYCHdiuQxVBgcNa2hkLFIuGjMuNTMz5pcILizDRuO3YBpYw3Faaow9C1YdhuFJHv_1A3PxcO9QWoRcKTBDdP3ZZodx2MnE1XzqPv1QXKF93RCqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 620 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwqjNy6Fmlc48qZOXyC3atXQ6HlvigHE1Ih4JcP2jrRQ5sWHgI402OGhS5X_KQBS65sKAJ6QDxovCZxHqGFNbxDP2AAw4ID7Iy9VhxIQiiLXm0hSHysDfZjSO4rnqFHL5rSIAFl1OjbeLPX8XtQUFcXmLppBp3rYCqJMCjkNFS4uDtyH69T4zKA4wbOhIQ5Jw1nJ1wPyCyZm1kp6E4tZ9dcvNig7EXnYFR0AtZO_Ms8uG4F1fZvylcNZc-02AnpMD-r99kR_LhEq-1o9eOYU2gag0lWibhmmaJexB8KvMdReRgVFfVAF9Ytw8XQIkZnTy5kjs8Cyr0YT1Ra4uLB5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrsKvfmw-29n_mOPUCpDXeNaehcBdAG4MBPx-CsbtNoGxTsUKI1JxIiBJ2k8OYhV5YMqGxdmNjzoDNmYPagpll2K7ujM6ENPTGR44nfskSp1qlC9Sl5gYW2IQkbUZdVzEojAdSf2fRqBXEib0y_RJRpCZKaQRXnsP4s5EY-EurocZXItTfbHALquVh-lDd5RU1MywIaop4BJqfiXwFP7QLpQHnEZ1kVwjYtcaAL_2mtV94pU6IjOTz-rtQfHTTMa0n0mJOdX6P0rfl2sD0bwF7CesCdzmA5VcPJudyngmzB1e2dyLEey47Dm25FzQC9MFPDALqCUKvEbELUaS5PqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeSPXDAfQFG4zs9-2JS8F9hHvQgmyk0SDrsHiUnGYcbAAKpCgB_M3yCc_pdq4Uhj7nSI-h_9ZqH-DWoiuWH_Y0EBQVmw2cUjbbTTR6ODiBVAaffwNri7kjP9WAdTurNfrWe5JmvRbeBCs6R8G61uu9FIP9y7yOfUDDSlm2bD4OUbjC-29Qqd8LEx8NJ_22c8Nta7kgwn1wyWZOoV2kGx7kRYhJElk_ed98Ov-6Yp-mAoCUFdh2uvsO1JatZmxlH1avs4mY_JBSmfsoD1q8l1P1Q7bwv184LV4cDnKPlnHkawfGYW4n6Qra60rI7pgAPWKxukt3uBB69wUzeJaqiaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=u8B88pxrk0opS-iFaMu92dYGVl1RllxQWUqGv9JQY-koF88gLSguS7T0PokKybeXuoUdUfwFSFDyjAz-MKJAwGg_Oi3m-FG2ojKy9JqlOGhTAgJVBA0e_BC1uBx-F2IpvlZ-Re9SqXOhG6LK_krMLSlxdOyOXB6ydSHdbq-YfXOVMazjwjWHEgnWWttjal8y4y4WJEKgc0ydCr6F0vIxgNd4b_89qUtgrkX7E2VNLORlRVL1JWAeDKlLG58dPwqRzE5K27D4N4t2YQwU0X2dQNO8_e0GK1Oo96gc_nBDEYkQwzO7JevIG0at8XG_IS2KGc8UueUzveJys88NwqGEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=u8B88pxrk0opS-iFaMu92dYGVl1RllxQWUqGv9JQY-koF88gLSguS7T0PokKybeXuoUdUfwFSFDyjAz-MKJAwGg_Oi3m-FG2ojKy9JqlOGhTAgJVBA0e_BC1uBx-F2IpvlZ-Re9SqXOhG6LK_krMLSlxdOyOXB6ydSHdbq-YfXOVMazjwjWHEgnWWttjal8y4y4WJEKgc0ydCr6F0vIxgNd4b_89qUtgrkX7E2VNLORlRVL1JWAeDKlLG58dPwqRzE5K27D4N4t2YQwU0X2dQNO8_e0GK1Oo96gc_nBDEYkQwzO7JevIG0at8XG_IS2KGc8UueUzveJys88NwqGEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9aeNO3gu795ZUujTobHHRhBhi6DTueS5xX8QiGJ4CSXLhaQtcyUknO1wwZwUioDpFrCP9_idKx7hJkrKnkzzvm4a1H8gLdkuZp-fOH8cKlPwGjiiT4Nq0aPWhiKVSNB0KUK4K1oPd5NEI29Af6Ngh5aABwFyTBzl47zdLtreqxPTlGgyjm6q0_n9YsFQwAlBDkA1OOfW9xo1FMqQWPgX_Jimvsm5Zja8oYC6LoT5BG3GWijDkoQ-Z5KjeTbik5qIK8hqemU80TEaYvNXMXvbLfTjSlywyLVpN_UNb5eRubEvjT1xZOQhdDhyX-n7N8X1dkNdYWGPBbxD4qtq43hdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btQR0gtlojXoozaSVzgCdhTgTpDh9kS3ua9T_WfE3eu2XDGIK2xlMI1OtTn5SwbUzn4Pa2sKsFkhW2gEpGI-6odp7hPrGh2JrG-nz78tO-iOPfMSmkpJybCYRZrGeJHL_W5P7iEwJ34RRiU_w0SdvfIwUobf5PuDJRd6wEhITq165jcfCpVbWvW-BTHpIbw21Mc9ywUkGNW1k2IliH_-jM55yLJoAsorMRAgFh2o8E-4bKoxaEQDLQL1wLOcskq8FghDj21TcsKJM8pglxNnxnrvzBTLX7UWYSvN7-nQGCKqJ_ygp58I2q0g-hRba5wFstOf2MN0gkWk4g275qw9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cayfp2wvVVqbX8HAWtfiOXlXWeDePtSaSDZsLg3SkE-tPdxQWhCccfXsOBWm00_IyKrhHnJuSLaPzCMpVEYvjpsVxVZ_rLCFzCVkGMHBsmAnehWRBKrtkqsvH2NtSKHADhuWJyovL4oZhM_zhLC20tZPDcy5NjTp_YJpvwOyNZ1xxbGT3CHNdoPk4ddo4U5K63GFxfDmTdwXh_jKrKzBzM8cR5kHa1peZkg77fMVvwftg6qtpkBK5Pl2bskkDJXW3Q1LMq-JdIU1GD_NqMvHbPOHtS5TCE9oB-LGOds6M0zM9O6v1UIlGEhPYWS7vKuqjNtXFc5Mu6b96jtsP5kRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PtPraRkR3xDBmDj9Ef1UkvRZaE2DK8zRJqqT-5jlWBXFu6oUsIqb-NlOGFcDd3dtMf1EA2r0BRyrOQ53-UchTneN-4uT1pig-NKAhsuLQXcOTlUytKU2CzLEP1rpVE4gCYJT3FQlQv2zIm7zK28C-xWhl8h-EIE0dumlF178TD4jKiUAH_YmG2Q4oK6bOnZb01Rq-MiOuTuKtdnCUEJZ_YBcuE4oYe-Cjmneq9K6o_qWwyoWFx8NHo_5hzrcCA_RgJZM5sH_YCkbN5_O89WzntNEiNDo58CC61tI1A1GXw0hKkpyo6-28G3SGhO1SN_MwBqouNoqJ-UWJ63-ymHgfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgUozVEbPgaxeTCgFf_m0V3LqmoTuEd7d-fk9XPJRYqOg3d4y3of3nCG8xAOZg00AYQ1nPCXMpSpiB5wuOAbAMtq-p1XC3Ya-N7D7ASgSVqaa5Q7luo9oUfwdhq583WcnP1vUBVVf7mYph2QjM653g7Hm4CXvaRTtacPaNYPcqBTaUVArwB5hH6_J20wL55FK54MfkPn_Az_gXCzydGi6IBSnTi2q9_qX5at9cJtaxMnjJXZ7z-VDWhStZA8Q7AiwZIXiEjika7EfQWJU5D38l1oRm7xDNdLMbq5xqqtKFm1U8XzjwUgZpdNEgXxhjBEeprVXTMIP5xrDtLeS0I3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Az4u3xIVx-wvUKNGqX4ULg31C1RfvuQQ3yB8xsqLpxUrFQG25iAJTDJT_LBatRsPr_pg8KSH8rRuW2UXn1v5SLYMvaDZR2Mo0hK4NkwS2yDCryASolPZTKSPIXEAoEEsT5F1vgQWdQd5RyvOvOw_iHq3AK-uxZ3-GpahW7yp19ejd1CGWwuLMLdaNtROzWWH7nuN5ta5Y0a31egUmDVNyAVZQvlej-BBtqREs-6qsmB9grQEDzWh2ppb67aE4hCH-KAEq3iaYBYS6oh9s-tS3_4mJnacPzPSoinTcNyc5q6KbXtGRwdjqgqh98DZJ210Ava0eMJI-i6Bc8nDVE36Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0vMRcI-3uQZA-aEPjSIH-lMn4c1fBM8q4OOmM4jEv2GHRnAu1BTX0gsp8K0_5tvDCA850AHBYaTOduKbsynJbjI18e_iXYQle4ZR1UvoaAavKjHOjZZqykjbWXgurgEGhV2YxhhhgOelELgC9j4PZUdVI_Fs_R1LKha9Hq_Jx7PTQcKM3erhMbR5v06v6-cRdRTBn0XRu2WkQSVXuzesNKg3tS6d_cou3gAbH9Tk1ifLE8t12at2FOsfEddnpTeqr84toyCXog3kou-7mymWaMdH_pC-tbLNRQfjP8EY33cnpqMZhcPpcrWsEUsEhSuUOSpvT7BbeiSVNk45aMBYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=i3c3NBv63k9Fd7AN8Irq1j5swSH-6qDFetdf46GKzbRSP6iXzd95N5BLqT9CJqS_iKBA11pzkf_nNZ1L1xGx7X8mex66boB1w9h2wbAhp6_FHXpPPT6UqTDhwTxyUcBz3WrIy7DUsCFeGJ0AMJshe_KLgUDbGjr4r8f0qiHaxwdyrzbUjK4JzlX-V_neEUZFYmkn5jqtkY0L5siPMhEygy0BmV55shd1ER1iATmwuQ-ykcgDWvyFiorKFVw_LaeTA2cTvwbOrgM5HmZWGB4scRdANXJmytoq7thK3dzIZu1vrwoNuxH0PoIxy8lhmZ-3anICyAQwIPtPmm-O8Go-PzgHcMHJ-k82A_i-j52IHp1xMwztgsKfs-qdrUQR-KXXFKpQXA-ULCXGBBb0OxOZver75h0tGsEI9YTFWTTpLIHoZdEuz6gQofPG0tPwURhKlj5VSrPyPbgW9W445FCQr_ssX_zMqwYmYG2tj5Rzde7BWOBB89Wb0xYD1_pGej4e6IPN6b1yS_VlK13AvFTQ1uhSD_ykG3SBYxmUGK4tTLFhZwqcLv2OkJ7-27pnoWT7vpcVYGPzVV7QCqzRbOsGUrpDpUIMXzRtC_5DegJEsNggQYNMVmTdYT_NnBnPsXmmu9rH5fdxHfnh9lIhF1ZPyR24FrpZxCJ0eeh_DeN5rMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=i3c3NBv63k9Fd7AN8Irq1j5swSH-6qDFetdf46GKzbRSP6iXzd95N5BLqT9CJqS_iKBA11pzkf_nNZ1L1xGx7X8mex66boB1w9h2wbAhp6_FHXpPPT6UqTDhwTxyUcBz3WrIy7DUsCFeGJ0AMJshe_KLgUDbGjr4r8f0qiHaxwdyrzbUjK4JzlX-V_neEUZFYmkn5jqtkY0L5siPMhEygy0BmV55shd1ER1iATmwuQ-ykcgDWvyFiorKFVw_LaeTA2cTvwbOrgM5HmZWGB4scRdANXJmytoq7thK3dzIZu1vrwoNuxH0PoIxy8lhmZ-3anICyAQwIPtPmm-O8Go-PzgHcMHJ-k82A_i-j52IHp1xMwztgsKfs-qdrUQR-KXXFKpQXA-ULCXGBBb0OxOZver75h0tGsEI9YTFWTTpLIHoZdEuz6gQofPG0tPwURhKlj5VSrPyPbgW9W445FCQr_ssX_zMqwYmYG2tj5Rzde7BWOBB89Wb0xYD1_pGej4e6IPN6b1yS_VlK13AvFTQ1uhSD_ykG3SBYxmUGK4tTLFhZwqcLv2OkJ7-27pnoWT7vpcVYGPzVV7QCqzRbOsGUrpDpUIMXzRtC_5DegJEsNggQYNMVmTdYT_NnBnPsXmmu9rH5fdxHfnh9lIhF1ZPyR24FrpZxCJ0eeh_DeN5rMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMvkDpZbVIsBaE-iZX3Pjx--0Ga39ZyihWgHCHR9cBf0IXM3DYyO2uJsYkPuLQePpjqzJDDVSVCochuOlX1CRD6zgORGSVd6Uul5-PiijaKG4SD_cBbfPTA5-u_30ud-yRsldxm8tpJgrkwgnewqGcBsZ6TSpsqU_rB09TwpF3QKxw9CDuXthh4WZgHXdR_iJ15xTPu9-1jEIs_x_dorNfypwvoRTGYt39jWxi01w7SwU_SESxo9l-xf2AH0cs-OKESIoGh7R6taqt3_tWSF8PhyoixBZ8KjJU6vCuMrIwtUi2zHfnB4Lui45mBa9PXImN7Q5gPjrUGJ1X9oHggx1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuhmvxK4baCgtufjgm8p1T0BNE85kuJqjRv6eLVau9PsT550HAGv8YQhhJi9AJZ-0sktpwFH-KTuvk6gWbQK58JIf_hLJY6nJ7ci43FWRPYFixc7xjCmR-0fbeSnTJN3wNp6sRmEMz_ZAl5bekUBvS9D5WNYwilv_yt7fI8lO3SRv-WVkOHTlQfFOrkaWOLKryp3r4GrLwY8awgK9BJ1IjXUdp9hJOjoVDYdSuKScF_uamJl84yy5uiUzlB5IX4j4CLtM78XtFIu6W_gGGbn0DtUNMjDoI8dojRMBblSeQrK0A2Se9YKQAseujV4Yk4-kFWZdoeUIUPAxUkMKcT8Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tem36HQ80BdZWfxkvcIs-9bFN_Ji3bLWlZpBV8hIK9u8dgmWPGB1NEKIwgEg9i0OTLp9PQNL69GQ7V6icY9f0vn-OG9Q02boFKavWAm65YlEHbYpqE4chLOyzSaMixflIRemckO6b_VOTy5c7WTfmoVQIUY-sKXDhgfQVOIgbQOZKs42W7XqYyDOLCC3ndSfigHnzDNsaTNoQJtXiSraRn2__L-obXY32Y_KPRAyYVwzhwgBPvzk1JRc1GArJ3bjYlXRadi8AIzh9yGk6JRrbLYAhRdMqlf-7y7MAzspGPnF9aWXSMeDWjkHspWhg-x_ZJ5XpOerBcj6gTbWQ_J3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3NYsmmdS-fD_aJogpFhFZnHmA0VCBjDiSFqM0E9l5IFLuv0q1pwIAz5MITHHTEG0P2XOVDKik9C9rVv-2MLUGLDnZDiC3E5sEORJ7YRB4kd0C1CfveIifImEwr0W2Q1Jn-iSEUAmPKJLannk7Iqwp0LZ59_4ybNCOneGWzCibz2kE-xvZZ__OUvyAlNvItaZdpTji50f6-SggzcNk9s55u0JqQYAc080VMbZMgCfgBJp_qb2kovb4XxG3nzxVMXhnZ1NZbkmWsUbKWufvOW5iWRgyklva6WCvgw20v83JuNybCKfYoyz0DjLnQCNz6mirc0HqMc6Nstwl7oDa2z3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvxU34XCLbV1mnekoNAitYM_2kWzsVJTsTyo7QbOzM7kz46xGc4VU6O8cUif-3l61nmDv187CYXfS2yupeh3NVFNDqnDFNEbpXL3elE-u_qSNsWAlLg4W9YBUSYBEXM1y6OgN2hQBd90_wvEbAsA-Gm4uH3nG3ceglqWp53R6NKf6Pb0mk1QVyPbWQk4PBufoYVpSl2WSX1wewNODA58pwA5mDqwrPGNR78MrRPEs70rvgBA-ihZ7eRhoiBdY3XwrcnSNop8QZn-74Ex_VOZSxBQTbPrIWK1AMvhIJsLtUj42Z7Vs124-QORaDwDHWTXuQEz26ElhAG10hemdRd31g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UCzIYW9ZGVAVXvgUlQvhtlG_qiBnAqVRKffa3Wb2Y6q1BNJUmDnHYdPqiIxR0AFwrc_aRVMuoPpVbdhYFuTIRX8ZRJbbfEkBXycr3pZ-QJqmrvpkN8IlRgZJ3euUxWW-87-JfH5oKJ_rResVNT-tXBn15UxepwGOXcKX78fIwbCvYXMPwLt5E0U9XZiRh8zypT3DaTM6dn_QtzUXFnGJH5iumz77T6Zk2Aqh-v942SpL_6vZIYVTqU9-UsIGEPuiu2Rn-3Bt2FvSzoCrIm72vTdow3u0JFebSkm7ti6SjKkTkHXc2yfdYSwTipA4umnG46xdCO_CEduGSlpgwjCetc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UCzIYW9ZGVAVXvgUlQvhtlG_qiBnAqVRKffa3Wb2Y6q1BNJUmDnHYdPqiIxR0AFwrc_aRVMuoPpVbdhYFuTIRX8ZRJbbfEkBXycr3pZ-QJqmrvpkN8IlRgZJ3euUxWW-87-JfH5oKJ_rResVNT-tXBn15UxepwGOXcKX78fIwbCvYXMPwLt5E0U9XZiRh8zypT3DaTM6dn_QtzUXFnGJH5iumz77T6Zk2Aqh-v942SpL_6vZIYVTqU9-UsIGEPuiu2Rn-3Bt2FvSzoCrIm72vTdow3u0JFebSkm7ti6SjKkTkHXc2yfdYSwTipA4umnG46xdCO_CEduGSlpgwjCetc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrjenlhTy7IU-VFKizqqmteRD788_tBi0uXQvyfeLXskiO9tX-BdqBA4CAZS9Md7ID8aHYUhJ88MSWAm065FhxvdEZgFI4cRTGkjrY1FJm8ptFmkD4UhajrfKPwbMitIzvyaO0TzCUZTJQr5EnKpjVIXRKn80Cei934uw-OBAumjeT0cqhH0sSU0yueCnX1m4_Z7C-_AHZlSz4qrjwwBs7AILeOJ3CAowfnSeuIkBmwJmmBZbYrO969NaEoQeXSfMOGqK2C8htuBYMMwNp-A23eBAp5vYiPhOW4DVa6pHOrQ4NgVOJpFfk_-Ehy7bA2cyALT69MwYxuHqayjir6kvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haihDtePrd9kiirmGUCBq-dcBApHRYKn6PpodqoknssVF_goXVyu0-fOEeOU96HWHHJZ2Qf3IoZ3zGdwk0KxukziuTsypcD8hsZHtTIssDXZqBZAcrDRlXY5WIOIFCH6bY4P7bgv5-YQvnBklaCnApBQfhFsqmxwWhETIL9eySgW1EVg3ZaNeRhw6v9HglU1DWFbcwsbGbColTuHFvHEHeYVnRDNofX4-GdMpa70g4ihFTXSyEkSJCiYLpZVthlHwsITmPXCL8GSVXfEEzuQ2hb9ZK2dxBMNVEmMTHdnVGPNkmpSsvZcfdWmpnxc1QrMaL09V-Pjb_UvZgK-k3YOGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjneBnAq9UYqMnnxgK_9jZeLwI8OMZfJut-89nZBF8zUGIdBYbzuDMOUj2xmX3argMZqmUPkLsO1MNBJgjOs8lmo0fXNYS0qubWB0OwXEPoIMjtHgFk-UPNmSaPwF8Ssm-GI-PRn9bvVdUlNrW4m41SeMdDHPBICUGYdMRzl5NHketTUvWBLs_iFfWMUVUb6ZGG892y5Z87haznYE_vnZGvID33qasdz2VqRB4l3xwfAjGDLCzOb85NNB-kTe5w-LSNM5HpJskf6RgtIXrz5qw-DpTLriE2l-JoH_HpS9o4ad-Yb1pKvjz-puNpbxAXB4dsFzHXdnjC-i7tP9KD0xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_7iMfzqU3q1YrZYHMdAgL4U2p-C095rRVL_td0Z5YhVVacoiQ3RklTN-PrHuFwPZUX7WdBI2Wovicfwx9iAZTkXW4ht-kUgho1ciOv-qW16KnaJXmL9-R37R7xGEQb6TBo4gUq_6kbR7Yr3FnsOjOAcWog7LHhnlz2aS7rv8Xd9LKHTui3-Tiq-6Q5xkyS10ONWrX9VSx3T495-2itwWOr5eU3K8M1HZBwUYz0rImAYDeaE8nkvPFyelYKmbhQ3Uc69fNNNVR0PgA19Y9JMuW10RRW_ZAzFQJBQnFk9XS9kEvHlXCPkKWMrjMNx52A2bMhG1Mt7eeDxGFkP8otcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFlFIyuvCRqE7BP83fS4Hw_w6GBkhvvbK6LmHDTcnzw-ys3t01pW4zZJvGvLJQsUr-TUvmqEuXKdrlJoigL-Ftx93LCkhmWvzf70Tk_JOwBBg0TLTIcc9kxPksFR9Zd028Wj3X5ld6P4Ee9FrdSIANGDBNtCezCDb7dralf-aFBS9w7Bkl2BJyKsGEZ4ClJtq8klxcfHvVxhxAALA4LkCScp-zWdToGWrHXqgETVPkTsK7WNiHDsUpDlhLrI0S2gJ4iMhin0ypllt89CmqZRxjAgdbw9GxIdfCR4-juuF_F9YnYPDhobF_qAqGi7Vb3DFaxOcMb2TjGjdOPdM8gnGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن استراکچر دیتای قیمت خودرو در گوگل
💢
داده‌های ساختار یافته جدید خودرو به وبسایت های خودرو اجازه می‌دهد تا موجودی خودروی خود را برای فروش در گوگل به کاربران خود نمایش دهند. همچنین کاربران می توانند در این فیچر جدید فیلتر هایی مانند مدل ماشین، وضعیت فروش، تصاویر خودرو و قیمت آن را بررسی کنند.
⚠️
در حال حاظر این فیچر برای مناطق ایالات متحده در دسترس است، اما  در نسخه موبایل و دسکتاپ نمایش داده می شود.
♻️
به علاوه گوگل در سرچ کنسول، گزارش جدیدی از این ریچ ریزالت را برای نظارت بر مشکلات و ارور های این داده ساختار یافته جدید راه اندازی کرده است که این گزارش موارد معتبر و نامعتبر را برای صفحات دارای داده‌های ساختاریافته برای نشانه‌گذاری فهرست خودروی شما را نشان می‌دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/danialtaherifar/808" target="_blank">📅 11:47 · 26 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XradJX4FMpPXStL88FW6hvDInB0vh2K0UM4MTObyQ4_q_kkc1jOcw-d9Lt7v5Pua-G1GSG6NmgGGvxHO56bYTUkVnPwbXgm1X6Hy6fA8hkQuZ5YjvVtW4JV3TI4cEQyAzp0ZBXzndHUdAIwXYxQt44NWSL-D5spdOgvoQvCE3bkjeBVSXIqyrHD4ZC3BGQAz8fQiJ7GMzXkly_x2lmnYkuFRUpsSn9wHr6W4enDghbX2gY6rItzmc6X3K5D9PpnTivF-o1ae0sCyl_2IvQqYywAiRJYQGk29jYUldl1rQB1-hDLCOv-FridG1yzJMdPERg5N4mtWE5VaOXjLgarlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آزمایش گوگل دیسکاور در نسخه دسکتاپ
💢
بعد از مدت ها انتظار گوگل به صورت رسمی فید دیسکاور رو در کشور هند به طور آزمایشی فعال کرده و محتوای توصیه‌ شده مانند اخبار، آب‌ و هوا، امتیازات ورزشی و قیمت سهام را به کاربران نمایش میده.
♻️
فید دیسکاور روی دسکتاپ شبیه نسخه موبایل است و به‌ صورت الگوریتمی درباره تاپیک های خبری، سرگرمی‌، ورزش، امور مالی و سایر محتواها قرار گرفته است. اضافه شدن دیسکاور در نسخه دسکتاپ یکی از تغییرات بزرگ گوگل خواهد بود چرا که بیش از 20 سال است که صفحه اصلی گوگل بدون تغییر مانده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/danialtaherifar/807" target="_blank">📅 22:07 · 22 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-803">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Yoast 20.4 Package_2.zip</div>
  <div class="tg-doc-extra">8.4 MB</div>
</div>
<a href="https://t.me/danialtaherifar/803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود رایگان افزونه ی 20.4 Yoast Seo Premium
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/danialtaherifar/803" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">elementor-pro-3.12.2.zip</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/danialtaherifar/802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه صفحه ساز المنتور پرو
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/danialtaherifar/802" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Rank Math v3.0.33pn&1.0.111fn.zip</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/danialtaherifar/801" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
افزونه سئو رنک مث (Rank Math) نسخه 3.0.33
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/danialtaherifar/801" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jannah-theme-6.2.0_NULLED.zip</div>
  <div class="tg-doc-extra">10.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/800" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
قالب جنه نسخه 6.2.0
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/danialtaherifar/800" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wp-rocket_3.13.0.1.zip</div>
  <div class="tg-doc-extra">3.6 MB</div>
</div>
<a href="https://t.me/danialtaherifar/799" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه راکت wp rocket- نسخه 3.13.0.1
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/danialtaherifar/799" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-798">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wordfence.7.9.2.zip</div>
  <div class="tg-doc-extra">5.5 MB</div>
</div>
<a href="https://t.me/danialtaherifar/798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود نسخه حرفه‌ای پلاگین Wordfence Premium نسخه 7.9.2
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/danialtaherifar/798" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wp-schema-pro_2.7.7.zip</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/danialtaherifar/797" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه اسکیما پرو نسخه 2.7.7
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/danialtaherifar/797" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
