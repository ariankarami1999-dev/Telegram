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
<img src="https://cdn4.telesco.pe/file/UgD4taVn6tasnNnMPlqW0VrASWKVMSO_K89Ti9xtekBRXjLr-jxxCRd3u929sFc9Tr6g5CGI1nsU5NCVjIGR-kTH4ePf2cOuGHyMWu1YjMp3tJKVJa3dRHsMK2-HhRjwa31UVlFQefGfAnPVs4FI5wWVmnSAMx4TNQmsztHlpqjmG91a14kWfUcM7Tt8cB9IIHmw_tCVl2-D4XN_8ZCyRbzpr-5jECJfV2-Gvc9KdNIAZzWD_xjDzRdCnl7JoGtKDVtMRi3d7UfKI21av-MCL1Xo6OVjFUdi8Ki9bmaS7mVwJNkuoPvVM1tCTlAThCzqNvXuZ9Dnv6xiAzjXuEDE7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.56K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 425 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpHXDD_Ak60a1rVqfjdUNLov48stCOJR3bhlTviZ7oCEanYujaUH9oX0A5O11BDWUW6Kg4kpRnjtGHXzyLy0jKamHJ29kMkU-U8YRdKWAN9yYzZ1bPG8pO3WE0fqVZBcphiLVDUzVx_g6FG6KQsYNE17pJjTKp6g4-xz76g6UcmJuUpKFnNpBFGPgxOfPJdXsqTM9BYp86gdeVsJFWzfiXLWqZ_TFffL_x5xY2HKeZYhK4yekJePOEhkpP5Fu-RQRDh0DJLVgIhVpx6-eeMd40CphdvHZJf7Zl8zf3rH7qEXdBw8s805uhsUOPaylz77YS6JKuHVAH0UCKzvs2W4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 430 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx5bKwxSqe2MpTgpOtTafPClEGQukMac_FjPXxxmIF1zhOUSduLxpNK9Mz6cnNrsr0qX8gnjE_NQuvvFjYn9ez4P0sPDzR8jc9xlGkT8JXQv3qscz-qPTOaUvus-5OXFC4B4WELm8VRY_fcBr82uNAB6zb2MSGpgekm66ZqtNmf13ajuWHJXmxsDmPRKQr7pHhkcjvB22egShaS3D82o4NG_HZoFpUIH_QPeu39a1Kx4TecHPsY3QXQEoB7tXZvL-b6WP2YJ_Hfkjc2Xw09G_qWzK6KT5aTGO0T-ZEtYLHQkhhJYtPqdNWT990k7PpEvh1Gikvm2i2Vn6XAkl_EDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0w5a2ZTLTaoHNmnerzOa_saFdICCWUi6UvXDBbQT3yd7W6jSWzf7togwejxK9jH1eZR3SkJ07F6CIjZlS08GDVkweD-8zsE5fgPaeL-tpbOvA5f1nOzbPuTm-CLxnL5hYtXOz7ENg6g849B5CQxoVorP6rV0hXj87VUgqkMt2ccDe4x4um19efCJCeKAoB6ewl75xFqO5IQYdVG7HyP52URe7e4U9wXjbG3crX7CAYjLt1eto71PRO2GwMcYXwOrsoKwkcORhr3CIFYqTyIFdvT-gau5b6nNKrnVXunt_-f32mezyP5-D90ruY91F-TJRa4S9XR-glfBGg2heuGJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeA2YYJU3cVodRYjRFFXor1I8WK3j4d5IQHhjOWCQG8cKAbnUW4gbSMg8kqAiUhkQLI9sJJPrwpxFF5efNtpWY3PbFf8shXOKrZ2eS5CRBxS4fPmcV03h9ynF4EyuoD4QF9_loC6IGX9bN5ZCAv9K1tlhVl8Z6QkZZuizbGIaQWnTfIEuwb2g3qoJnv5zcXJ7iZ4FeNKJhld3i8hn-M2MNwmqZM1_UDhET-uo2f1BHAVpMLodaPkqmjlc6Lb0xXFmfWe8YX7_VzEICbb1rlvY-3_jNdY4a7wDrNZP3D5TAn6s7khWI5OaLeBm-wvrIG2udy-2My26RpZGDk_GwfNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNyDAKNqPavS9gtxJObNRIX1CiTq3XlVpaI31YciIathu-upJg6BuovRVdMsHB2i1k2jlwhgyeubYCMRwT9lKK4-RndERAG7PSQFYeg11og49elrQHClgsQHvGmngrjik8DPMAuAPkTiF2nK3ikm1tWgaI6YYgntJ7QSbJHs4VL3mwe83KFBnYtNmKi6rvumNVMGIpfJqCeOx9FtoRdRjNU_SqZBvUoV-JT0DKxtOLUpJyvqZ6gwIyKk8zXbNoJ2M3yTQLKSPPrNUdzooF7VzHk_pKgWu7Y9Vebmx4asnmbeDNaQbUzIUPMYGsPjk9AVaXIQ0r3j77MVeQmgiG_nSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrKHP1gGWaty9WYagW_8tVFnyy1YDO8rZbapecX-ISTzALbt6UYmC1Tr3x2SsJPrhToj07PhQgo9p1xsirfj1w-RvjLpGm2TCgf_y1zZf6dotGGRdDF_N56vga-86jHxg_n-Kd1aG7zb5c0byAWAfRAHfVC5raFsMiX0La6J_jt-SWYRj68xMGQZ56w2tSaa3o5SXLjPNXaGW1pIbuWfWq6HnQ1jNJWHUIkJf0HBJr2sYueKcKpre4Flsm2tzVhyfQnX-iU6m5jgXQrRYXRcbxlXO-1s1YByllCDhyosgX1M1sf4W60zICsHqoHQq3iZ2536Ybz-nqh2apauBZFAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRLM7Hc9qDtM5ju5B0SFl5Fx96aJr1vLdqekTxlZF12zvYJ9LlJiEFCYYx-9C8g6QAJljcOayFvWfr9JIp-TluNu9lbKsEBSRMk7aPXTZUu-hX7eAMJXtsEk5GNCiHFkPmgJtwCPiyNUgcjGvm-wYa-AG7oUoWbRFg3kqwHQt441G6dIQeCtbX1BCYgNg9jaltyhqukWL2InQWZWQKA0_C7izl_k1xI1Xs-EU_27bq4NUbsaw7cMZK532tzKtuWO9hW9gtDizgR-19u9k7VSNO07otik8--UETIp3SsGtZvWgiMY67j9FoKiVTKdkMTAsqxy2MizsSlVAPuCPaf6uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R937dAd9hW27O2jwq4o5oEVTA1Hg3ubBEkHFSvyXNVUuybAnFIB0R_tqNK4mJw7XWty19t3O1E6BpXv5JgKY6jrkGWLKFOb_9neqAcSqLiI84WxrzHIyiWioIrGZ0B9aDmrFKH6WPzu5chGGoTXa_DRkwwd7aRNUdEpz9qCpPeYqG57ffQFBqcM4a7mcHHvA8zaTQ9PGiHaG_aavbFLr8CjpV2dXBHrFT0uBIYwgFyZWw5AjUJnoqmI5imCU9zkoO_dAm5rLbL1_EB4wZkMhfyV-Tzz4XFCoPSvQjnzzws7Asv_JHS-QyMEQBtRU-5_RSqVuGeNhuaAEY_Vif-fDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 911 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmL-7r0piQdFDiGTgCGsf9LrVwGXkKQnf6Xj6Xq8NJXsaHvu4W8x9D9okSe9U73_HFt_pbdRk7lwvNWFmCDGny-TRILfiiBiBpSVkF5aTsNsZLn9EwfgZCGVU0LcO0cnz1cmG1nlQiq7VdIUm-v4rvXt_Kyr5Mnj1IFOxghB5gZ5xPrGENoX6fhkUbuHm0vRsyCLNd1dBlbb9p-g5euKr1dotY23RR8ziwpH8xNmXcmchJfzPDYbF70y7dRZqhdV1dO38vvAbs1EyOg5wk_aKXXti20MVA2bpccynA4PHUkFHGwwaRko7Q4RYwtOkuI_6gdaamY_mOdrYOeBV9v8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZaTQ6DhEo7No226ytcn89La78uYjCpjxYl_A1bbtDDtKf2lnfeZQkiqh827xBbP2urlUrYYLw_k9R1mdFotHt5YwW8C6VvefjOnscpoSZEJsLUsR4lfkZBFUfmwe2heb6y1cljbDDwjZchXjm_5A7PPiVDyi34rQbhD69MUy8ZlVLQCOvk_Fm-JtOMpkXqXuvyYvFRNM2lR8HAaAxfi0wnFylPD4sbzr8l8clvae1nsDHxF7A22SabAUH3opltthRnUGL4p_LmhWVtsbDTtGvPbJapC-tCnyUCfl6fJidnLMJa3-GjGlbN6DTq0A1YFvAAQaIbUYHnl_QynO3ukbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwlBzWnMjhYTZpsyKcXNHXMV_i-qiaSN2odD690jaXzEgpqsGp5_aJEwnCeGnm-Oo5WwRad20RrIvd93uhcQIAM6lqoDQ06xEt2RCds52lkzpZE0omBiOgTLkkHx4kUonT16r91Jz8ajEJM8mqYoSnjTmhVhdgFXsluTknH-pAPPx3Guhny_iTqwpRvw10tzscCoUz-2iLxrDXZfmXsuY9uH0DXeS4EzsOF9nT5Vy9IWDkcEpHXu9z348P89YRGVGANldXjK4zwrjpidFahYI-XrOCeiutWqcj49uLWNBgQnw7cIhzo0jj_6NzbeePIBFfquii-m7qoA9dQCKenVmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_0GIpz6NelPI2P6-Gl9Hp62OVfxs6kfQX2OCj6wVzSh-56hZSvlJKD4X_EYPkSAg7D1RXbnS1tTrhjlT33FqLF1lyoAHJwfekHXFZkAiGsmV5nDBB4JxtDsn7KaadewnPtMDCBwE9t4VwGfG5LhP18Feu9hLbeTw6gwESCYEqEFuSjb7PmIR5nzZNS2h_X0plGD9Kg2lLxnCVBdINVu6b-lJoc42rZWJiqc1KfGQ0XJftZufisAEBqhWl9cKLfPY6HtKeJ5gxk7InvCpjX3eD2rEdsR_fpUsJBWasOTZzP1HlHqTIrXdbkQ1bXsuKm30kvwctQD8Ryqs3OOPDZhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sf95ZbEM8AlcOJ7v2EZ0dW8d48OfktqbTIWzm4Wa-sRri5gbsGxtzhJs9ywI1CLkXUcYwnylFoh2FRbGF5sbXSSfPrs5S_0OQWkBb-VdUqTMuRVZ2h7Oive9ZZWA4WUua0JxpKKSluseZtzbd7kjPrbFjWzVxFix9yPmwvESSKLYEWTsF7V5yAOC-v7jiywaQDZ1dafeJdq0XWO5ASBsZWH1jS_DMcr4LL_yz1FtgIYygNELBlmMmKTLLlsUvM7Zar51Pzf6OJe5ZC44deU4M8eWE3_GedvrznOYMQQPf-kuFJEjsogqquG5PNJgYmqN6Z2wiHL5OwcRh17KkIKTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVzbpem-HCtl0UDoA5zAw-Jp-xm3ASU1Zr9HIZgJQ1eaHQvI2f1I_-I3YXq1WB97vRaeDU0WOm1jwyV6KHZF6n9csa9L0l8AVvyZA8Rakcz0VXCKY2pxzO0jytPVaoBN0F60-9MxOn030x3M6G9GLfihm5L9vNb4oPTk-zOM_j6h6DitmkbA0RvzhseTYGQFDLgj5xEVrV7kg2SVgEUtshRtIqQdkE_aOougVna1dHD4IaEjbbthNJOm700YYWkFd3bVwOfme8ZWiciJBDRDY5lvab2QmiJ6u6VzzDdd8U3NmDwsk7ZdTuG2LPZ_6UuYFmVV4jaJPi5oFH94sFtGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPPU8Of_lgi01THxWB7azxnrucIFSwnJWiq2xfCgCAd168d8UPDwr7KqRX0w78gOTbrrOhiTen8T7bIKavbLi2QiCIPgVcddyXH3U_Esfd6sRj_mHskWnY6YmCuCQ0_Ux_LL9uiRr7fnq4M5cgJs1_pUrNOlhnKJq1hjKX-Uyj9Y1wVOFXu73VhCFPq1zjyZv1-EJCbU9g4FAhxPpPk036ddPHN4zeLkCdkJmKUkPNQtVIekmubau95ioCc_683VfFpwBSWu-5zGrJEfUHzG2FWfIVBbUuRZwq30VGfQg5Uhx_he3cWLA7FEflYY_K2CJS1L_gSChtzcj1ztaucNRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQjcXBqcxK808QNL04oBDrt9reJTpc22j9SIA8o7F7ewtvef2VvFMnN6YSR3uKGHjJzJAyMKgXitKIm7rrd4UO3QkBNe1a64icBrzbJGYz5dhvzF0-NX1jp6-hRd1WEfEOPhx8O5WSu1FT8yvJU61wa8wOVg0_1HbcPdtAp9BAJT9Zp_CQJLirho3vV3NCrDW1wMWBLV6KOUgT0hwUg23VC3aZbxU_Ld3QaacuvHGPraX8crQ1HdDSRMQ123NTYn-o4oPramECXEwyG_ePdbUMeNXvd89C6MJaBvakLAMpqtCjRlVqgRjIgobLIzXgtbcwk50DMxvtjrYZD2RrVC5A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=aBex7YxFMGe52H9mpIoYe0g_7-dz8duU_Ie0RvMpC6JdlX-5rn9cBqorSxeZYXSfum_c3sfodOnMz1vH43VjCVmB-90TiCuIHzslazpzNtQ8HbwSYtQCJc0KooYvAxmSXpwesWwKarPQy3gyWDea_MbyKz8Zgrc3GZ3GKGBLrcLtlBmIoR1FYiLZo2OrzMiCa5Y8MOlWJ6xD_nmUZ720tPB6LSsWRWMhWOdnzcnTpRJreJZWVJR6XNE_lQ7_0QdXe-04WSs2VrLOFkQ7Tk4U_qhytcJFfdf4R27FFi6RlOWjac9wC9qMCvNX14m2OZ8UX8uu1I8F3SwABFVfSQY1xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=aBex7YxFMGe52H9mpIoYe0g_7-dz8duU_Ie0RvMpC6JdlX-5rn9cBqorSxeZYXSfum_c3sfodOnMz1vH43VjCVmB-90TiCuIHzslazpzNtQ8HbwSYtQCJc0KooYvAxmSXpwesWwKarPQy3gyWDea_MbyKz8Zgrc3GZ3GKGBLrcLtlBmIoR1FYiLZo2OrzMiCa5Y8MOlWJ6xD_nmUZ720tPB6LSsWRWMhWOdnzcnTpRJreJZWVJR6XNE_lQ7_0QdXe-04WSs2VrLOFkQ7Tk4U_qhytcJFfdf4R27FFi6RlOWjac9wC9qMCvNX14m2OZ8UX8uu1I8F3SwABFVfSQY1xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1GXN8DecXhnjN9Tb5Qu4FnsldCC8gADKEGKQVgU9TcMDGEGRFt8xWIJHme1GcMMXfHSdibs0l_FLmsJOLCU8tqkxi14SJn3TUrqkntDNDh-xR0fBVUrtmYUPgglo7jw6T9nNOaU8GAft-sxtTqCYd0LkUmm8fbiOiMKgSwcQdx3pEfnfvudHHDF9sAUf7H8ARK6uH1IsTTL-feRmKmNSKWCttwBsdGfVo7WP6mlg6Z_cZkZ4GZaRHpruFjiZ9h77NE6hCcpQ9HgsOEquqN_Ggj0qpp9twMGktdiLhP8m44SXmwpUxyuePmJ9O_ve2cnKsKpQh1SZMtyvSe64DDj8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 920 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAGJOeq8szGAI1yxVkce6LPoFG1V_GGwY0LOXBLLE5d9HvmIpg77oAnaHzCAqmm2Lz4CpX_qmNeA0ewFv5UQHPC7wXl7m9AKX3AvSV_YaGdR9guVJE_6LJPjmvCGOhyF0Y0N8_EKFDkMGVCK8C6y7BEww3-ZT5O6DoQdTlm9PKfK1dsjQQzyB965srAL_H1QxaeLh7lQgU8iDvIbIV9BzOkK7MO8vuSwtFZ4iDHpu8QHCAQnTamApTmeo7baUIh17CR7Xa_omyKKLo5QMwwUyJvju_8FR1srB85CfvUCpRN6RYC-SvATLgLa04FkDKZr9Z4n5jPnskcUBIpZDMG9_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fU_cCVmEcIN5uszhEt9el_7E0yWGIG5khnwxZbZfn-DiOapgDV3kyZ2r3i0d6IYdtN8F69vV4CypWcW0aWtbj0jPYQMYCr-PQfb0uXFrplF_TfofHmH9wpu7qQAWjsZ4wfXMOx7MGzMc11nkWDK6MfRiImMzZpgedwwu5yfWc-yVO7rj0QwPYyfPsU1RgWYQZ1y2DuKKUbgiSz4cCH1qUUhBV0_dj89mzVFMALjo_aeJNzGL6qIzNH20bGD-ORnHWeX2rKKfuddQknY9iBkUnRn3OkYuZP8OYtcEFwhliMk22xRh8wvkdQjRZ8wX_YfmiUfuDBWlZmyr9RaTcAgzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkHP6ukcAEGtyzS9-wN5NsXxrLLI8i-L7sn3Qe-5rk2vWJNR1jZpvF8Kejk9IIYdSXHNhdiStiqqmxEajEJmNSX-8z8HUxbKQQyldASSw_9_kQKikZHR9h2vXQfs1c7a19_EwY3akw8971O0lFI2LsGW0T75pGeZ69JwfYIumkCbUz-QfLfP8WZd72cJxWWV9oKsNrUbq4CkWQgFXaQbKIKY5lbhw-wulWcwUg3En0-7GMZeXPvh0Qg7Zq3yRlf6HRZCCVyWON3v1DZc-ZEBFZgZsYPJJ0FWy3TL_FfAp6OxX0wKLbZoOSOp-LeMo6FWpeCVe0wnsZs8kXQP5Sw7gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 981 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhHgcIHQyAFBqWqwN0rIHEr0MpxFjol_k7L48hvg1K3wA8vkGJ4-5E0ZN1ZJgN4bkJm0Fq1ce0RXKNWSub42-8lyrlahLF3AEE2CxxqE1yF9eHgLeyhPo4fxVf_ohWkfnAholSbzMoA8QaDcS3OOLwQ6SzkUYMwe83cNhgDEXeYpo5nM4R97E7BBICo2yiTyc8IX4FXUm7O6_qPsyjjuMQuab6bgxSwbtvETzO5ekevpgxS82w8IyELlfsxPtKD8KiYQEfe76vni8xXvGodU9TFAp0nIpKnBCzwvDPzvJ8rC-oxkRBjQ5RWIjsmasLIbC07OLN7G3raA1nFetNYQ-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 918 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuHLCF4g9gvSD-0AI3pYHBTEJNmdSiR3m9lFBnXX2TqT94z7ezVxDo8e19gjm7chzv-2SK969kksvRIECk-7bp954hoQM3qnNz28h9LWLDwJGD-PvjwRGD6v8xVMWWz7gIxVW2VO8-SxbWOoxA0uELc0h2F7JrlGRTY-EhUgaX_m26M1jAzJ0lODKhB54cYxyVfEslAkAQ1YPilcjYbejcWav425k8R5F2hc0fOr9CpA7G-XQjfhonHetqNXQSz6mt-eMY2Y-I0GOoUT4RuU-v05d-9i_hDL9o7ZiVnvUM5vHyNTSVNQ626SM6B6FD8N56myoIIOA9pJippYYkdcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGfVQyAyw1HPT9NafEWf6W77HxS-0zckPenqtDqYAoAGtqCxk499amV2YJdyevHkpHq8pHRnUZM5CkKhpPNnN8rTFSQpx8qvXKih0SVoH3GI0IBkFM1jPzjOWlzM0tlrSEpZDbFm6tJphBP8V8_RUiaJMJ1MRz8e7MAzGvm_UFeGR-_B1uOGokaDow8JmDbp8vnVVn8Bn4dCMySmpn1qd3pqw4yVe0CI28LWjcl5Me8SJk67UWzNxxVMC04VPPjlCDVNBJQbR8Kf0lX568M9qFaxDMBEhVsvMFoS54oSgntWAlreg0eqBoOfgDvn_gQm9MwD-xeZ3fZzZhb-gPRQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TX4DyWckTFU-JBsth21RFC6MbWggQrbnc_-r8pmSHfnOcIBGhgmdzIbq1Js_V9wqnZw49k-CVgNAUlTtB7bEMZsjcgoPJNZrYhJ0G2-uGXqB2gjgnbZn0fS1VvrWNfc4XhoeN0nK8MM7z4xeztlDKiGJrV0zAl3oSiipsOuIs2XwtbU6RG1BqL3XfsPS01AEFLLWhqno8HPJdMgvUSrhaHeAhwvaTXxSWh_Ud4PWTZ2MSwyL-aUfZcxKfsQsETsib1wDQlItFJIbantDNaP6MZuRvnVS0Y9DlVbipHL1g4Dosxmxl-evhc9vh4ngakyF9hc5k0l-bWEXUSlJEMqZyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giOBEtWuSpRLOPCXTjP_t83denLzMr1As6_Gzmz0nb2o0PxOPVNQI4HD6JXcjTrTw1F5AjrRz5L7K0rIzJ_-3jlsXLhNVuCgZAKZdrA-hcNG8UmLkWR7nQTiFKXNXvvq9WpH9a6j4m3RHiutGRlDffjFopq4Ab4EI-joK9956C9q1tQUP6v5aklKD7b7vUeqGeM1C3umfMLpciYX7JlZju6uYOskZUbLG8wjDm51SvyJMFg1UQg58aTIgyOKUx0mkdedVijmE9xOBsefcGeMyHQ_uWQWG3IMnK12QykZORpn--oSyH7fhKoMqi2DTxFXre45LISvZUUNTVQaa8X0Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7mMqln1PtUzy4Vnv1kOpVvOWn8Bz1_VakIpJ0atZnGcU5ki6_Vgps2C0hDcKV_hxjls2Z_8Bj7QORbuYTUEusNkpHtd3IsZTw2johMiQjQ1IwF0y67Br1KF19homvRuF11slJ8OjqTkE2-P5jVGTFMN2WoWEGksUrJCHh-3FDA5_Flnj5DbqAJgTDEte97G-T7TfrtGKIVG-SBAEY1117KtdamKQX222VuDvS0VPrhWi4SulyaNS09OiRPbw_c-s1WTl9x_FgqhgOEpvRJeeeITys55tYJ2bbeoYZTsJAR-D3S3oorQfINfUfyRZR20C-A1ZXFgtCSBKw9-zUye2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWIleoCLri1nrp-gZVeKj8vQ26tBxLE8HEGhi5aLWdLjySSWUdr-bMsfYi76V5qb0Yd0xASkq2Z4LkFNTY6souaKjmP_z7rrskYflSO0uZ5sD2vJ8g6eFiylRurmPZCJvZyp4OcSnhjNyD8BTJnHr5v0VvngNFqQXQvMGDC2AWLkyqIpY38JlTUeVVGA1cEgpot66bfJsuxrOKXdwOE_NTNXCg00PZIbfKXDUDVfrlJOdzd4n7EcuX0gC1tFqWcDAL7xdpPO5WzLCspH51paRiEDece8WMVF47GnnIz3UmpUQILKIwl2Y1mwAdjtGtSUnfE5dJwIcJMF4KW8tfeyYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7y3KV0k23zTd3rtFZV41bE7_TH00y_PIbvv0-kZMRyby_-intVMhijq2y-QxoqaI6WhkVctpN8YfFv3j5tCNVH1_Jc1BdaPcqY4vnMPzqLxTpAE_O7HCXYRpomzrE9LRDaqMC2uOr3mH6oL7FIAcylUb5yeuyUiEE3jORyIWcmoimM14CXLen5BywJAiBZjZQHqLSyKMV8s_nikOEvDzfNSlad0c_Qi0G72_M9yXW9u4xup6aiR3QwPn53ePWe4O9W_1NWILMjA0fb4QqkY-y3FoVYmnwh44KFQnsgDEzhhW66G6NIMpx8te92pkMrCXfsJW5KQxvygAPgk6TkMog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHQ9-ayL_9rmj7J-eUnE_0LRfu49f6xsFf6ntBIY7hXuiqnu8pSSlvPKUvlZWkraTkWCdg1APZcu4rtJyxIgJTRIWrIjxa-EtDO1oFtAbs3hiL0Lowfw-v-D_SbgtbhUkHajer-7YYREs5BrhtoWBt-S1F3UE_o1WmBp9JsBJJuOsoUCSUPEoM558ASxjR5Df0Brq1BpW79diKINhLpAYMv9ObsEsRsVmEFK-WYLEQwMrsNQ35tHwncQcD9OK84PS7NrthBNGPVLDl7siEwkNzlcbyf9QUWoFkXDpEw-aAnW2VtpAc6EucpDnUb1Gmb1s8x5wQLwZ5DML2dliLThbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwWnT5vlQwYbJPl-UYg-CnXib1LwM87744hpBg2QT7tuFp2HJiRx-gACIQRiG7cVXuBjg59jG5XJZjmmFIfEYHpeSpy2LTQOCpAsGQE-F_lS9oZu9tnxNd8WRSIocCFoaohnhGOB5kPm4PUaVIud_4GezRSjH7Rx9ZXh0QmlQ6Hociix8Pn95jWRx5SE7h65THnuUZ2Mxr3oHeECe6YXFvwzGQmJrcvzfAQX2heYXs6Ie0diyjbaq99UjXPwgaEZXFPBiBkC514wOC-q6qhKgv4eoWoAmv3YMaUATPzP5tzqyOHOySo1Hdf9lCE6353EXjntgQkZt_icHrlN-2DYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XImJmAFsBjtU4DCc2AKZU47LLfmN6sdZInr2fkCGOb_Bjyz9cchTZ1M8BJZZvVX7lOOz4KGRZ9kZC8tUo3f8MFtLUIlds3HrNIC5JLYf0DEPnGaJkbnRBGmhGECm6bHAc67PvTUr7pS9jgDcMWLRHfAKgp_L66VOTVhb4AC73dhiYv7Eb-Py0i14lcf3jAqqPcRAL5RRgWa5XHSuC7Cf_mOkaCxaYyax7rNfWMpKvCA87VPjWAg3Qf8TQje3OK54COwOHPil8dN0K2WhlojX4V3EzMfblIG51zLSH_hXyK0-Bpgnep8ts1GVNrn06xZUmww7R6M4WXqB7ewv3gLkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEzl9pjSJOGsOFrO0AoCRa1jS8cBykOto8ChKUKjmU_A9_13GBoT0ZT0moA7o3vEpsXIfgAlzvvzKeXDHhx1X6rARVrAPfcDAGEpFOOJt4PhyuXgHYYLLQzNm5dWjnztvzWbRn0OvJsDVf5M4bAtp0vwxrp4keBGQOMeMGVofRkBDSgA1jDJ2tTOWRvDKHK3TH7POCbt55TNptRrwapSP2sTmT3ongAGuMXPfrt3taQCGV6X9EGObxCIq7yNYgS3xn4mpRtgyDY3vXEk-Rxf47OWT4GRTIIHMCWxke0SR6rnsq8ZOyzs7HnQrMxYltLQsjO5trmH5vunOTbXWDgRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXsO9G1WYG2CKsAgFjFAwyYp16Tfvh78dSuc-Tsu5HAlgBxoX2B85re0RTMLZtXSRH_T1yd9684DEPMPX2wBvFkcNjuD2IalvzS8AXOvEeMFA3pB-nnIFEbo0s7jFS19J8mNWjqANvnmWqf9SPM9fLspDJiEmAYV8YWnFIYBUSdFlxxXEuA7QEHnmX_Cb3dGim3nExIuo13xQz5Eh2fOfpPchgMdi04zFw6jwz-lOxW19jnOc_yHfiioz8ZQlni85nVlt41mvsSa5jIUh1lfKFxX2cZKw2IAXWKhJoowJvPLCr_gLiweiCNOmRBlC8rpsXrO_onflXQjWycQ762jVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8js5sdHonRkeNQmWMcypEGWJnm52f3qlhXBoraJ2PDI9CxZG8CLfgdkCTlEgAIDrTh3Dpru3wUJGh1h1ouq2gq1xwDe7LCmsBgaqDrU3LiArnDVULRX-qq3IJUC8I3lb9bIGSJ8mdr1YJSUSNuvvR2EoWdIGq9Cz5zjKTAgXjz8T1-gNP7XWGzwOYTzyOJxMrkUgg1D1LFZDL9EkdbhFFqPCylmsqRytpPYQbiUgIkUtq1-wcpxhZ8wmp_UidwbUMsftt0MLKT0SQg2r8MhMJ1ZDPPW_I5Q03wAblksurHSIc1POSBCH0_jMxCka0Fx5-kHCqNCs34Ngrs_NxQGlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWnv3U4yhG_vq6MQTl5o8EtYqYBADFDkfJ_U4hHf0Rg_d9v0eT93Abjr1WrqksOc67296jcFVcEDBNTCqrhy_J4YDYqqHw4seqhyQmx5hYyZxJv8ulUNEC1RDU-kEr1AE-n5gNGWGLWpVmCqK8qXk1ip6kNOduQ2VoKBw6GFSPp0bhwXDI0uSfv1LwkU0dLr4FeDmb2Zrs3DloSrwh5roImlmJXp3g4aOfgsXpdzXjI1ND0wP2ky7Zv5K85lT2AqtOv5Oa2eGzSi228qgheTPN6B-oRvwyB5FdUmIy9drUPkMxwn8R86KOeY6rnRrFrOivVMDdd98B2Yjjv9mvKk1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPE0FFC22C6ptgCPImZ8AF17aykT-eEG3g0ENTnWh9YyJMzcjiPl1PQ6ca4GNuwayif9VTPOrjNlelKQ5hOv-Hs0fH1CGD96HFf72tFjmoHC0TD2FNmTrwF27TZzuU9gD-vV9F3c7aDG-T1RU7el28SZzYy4TyZFgZwQh5zWg9aNsjyiSRLXVUx-lkj2mCfoyjcoe9UX6Gk3fPxdRkb8r0IboMnsA57rX0Nu99q4bOxbUz00L3c9HFl71wYMxmiX4g867PM9R4CE_aXmVOExV9PlCMbHIE9Ma8Y3y1Cu6SPODwl44G-ldbn2Y6FFH0eYj2xzzg0qAh7NgB4UvFZOIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdOpKab3z7d6G01v5dAI1SmOixERUe6wDjLZulZS6NO-XGwINRLcAwSwjTej0CO3lI2yWkqo7QHq4mpHW3XHVqz5d2zIdaA1FIwiG_ucT_KI0c126zm71fuGgUKwXKY_0iFsdz96TnkBM-DJvJFAWit89meGmmymNRpw_ojDeRdszh7dbPJrlz3z8Ap7GyzCrRJc3teIlF3upyhawIhT6jwKHXODLktRLcT-bhGNP-VC3HJ_kboQEez2Ae60a4GKrKdYCbVsfEyGEur7sYQ1NJtmUHotQYjW4YOZKJyJUVwWHGdGg0lbldcK0apON6npvNIYHzF2-GqHkiq0mrGAHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvYog9rrqPvSOyGu2XRqTFgl5NEYB9fcamUZRgF_qrzJndhS3dkpjlU0dyrcUVZNUyWbs9D7I4Fam1oRm_Tb76efsBGajBcK7vfQC9W7Znx_lmPwF8qPfcUj29LSiFi1X4u8z8PFN-M6k5Nq5XyJ3IV9x4kQLJnuVQT-RBh2HrC9np1MRlXMAZBj7GQybiYn2xLMpr_5EH4-p7xL20VDFvwt2bmgG8WowIvsw_ZmyXRu7Dw6llLevetoRtYzFEJLHCFhfBpux2nnqYc1Rgkh_OEtcG2kZ8raTviouqKBgvrNkxIByzvlAkCLPGZ0WeWZ_9SgfbTKb2D0fzpF1Fkhlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSfykwkvPeQSvD6aHAg_Le3eyy_oApEuQL9Tky1-eeTqruy9HuemT2EE3Gb5ausV5ze2wqo7QMZ1uK5cmS8oD3IpyxEkduO5KtZIGRNSv_iIQXf4LOI43bl_3MP0U4CTpTlT-eXSvAk8EhpWkl3cLFHbG6RN30af9UrdBuU5hrk1S_aeGi3mdZXHOUS1gIqPY7eGKMEzY_itHJ1f2yaxGf824t_zJVwpXWeClteNA5R9Au4a-kmDTXfbwj2dkJpzfFns7iDnPGqnaq8XOCkzfrLt1B4A2Ki1jCxRtnqRRfPEinShasSwrKktC-RgKOarlSXPtZ4_I-Z-_M9myKDCfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCJd3rXA0xpmSdena0CJpQ04ag3mIxU4moDMtIoECqtBonqkqnEQ9onv5updWBsRLMFLidWKRwjtpbP7Kd23WZ8ezrNkCAd2N8td2VIePZgzXHZGy7XMMe5hFBlf_LewDQjsLOS-SYRBWiswiGC90lhoDvle7GPYgIxf-dSFFmn9vM5exd7TOpJW2Indf7V_WA8WQ_f2fJ94gu7akE0FvwHRS_6YjDUSLIFewugaNXkdX9hEhav8UwHT84rxLjO16IkJIJ7E6vOZ41O6l8P4_Hy1jQ13_-6XBMx7wcrJhPm3dq-c0LpxKnSEQEAeT73Y9Q73JIwLsuUpw1QHxLK6RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_BuJa-UNrlmGa1wDJGo4qu2jNjXuusQd8p7e0cy77dt9pk1Q-RYsoINc7Ya-jTByrCDUYKnG2Jry-CE0Rl1b5pDLckfQUNyH9ymgBK25wxDYDmw0fHRe73NjfykRgnQvsQvrZL_ydW_YX4g-iBe9ASODzMBH6-H9j8G0wFCrEvyrZeClCfpiyEMmGjymGs-3RrKuTuW2Zdah5cvWjj3m2W6Jtsr95m-PBDTMU3dt21KoWkJMcdJkIi0cdQ7vkSL4sB1LvFlGqrrMJEFUak5S_RQEuiXgQdHf-ah2Lt3KgdysN727UYyNtDK4x7agRWmUGgnUHBUh_TBp8WIZSoN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni_2-TkjS0edk-rALCKiVih6TD4J_CYlq6s7ohuMj1FtxoaxoYyp3RSgW-UZEo7c8PtBaC5pq1BINTvDViLLfgOTrbjFwGNfFdATkEqM3BpE9ov3SS3fydrV85M0Uo2Rb-GVsDhm-lztJA_RljwLyxyFRdkKRjNmtdM-qGMCmAo-DTz1OEHJHDurut0P5XjRlsIoUyNSQcAMLcoYL-p9JO5HaKO0LZINUJBwacI5hEHQglQKQ3mnEN4CrmWJD4YHaUmPiCOh8GUPQTVPINbdUkkWKCiN5D7_GEjk3Pt9_7f35rV1Ntb9GgpqCt2xzF-vAUSSI0FEcQlHKDklgWfwWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCoM9JOOZGLyiprxFXa0h4GE5_SHqppB__w0kvQzYaS_sreAO6LJVpk2cDlHtxN8VS_f2IC6WAAZszAvB99f3eVO7quLeN2raagSqH3fPZkcY9eJ80aZKnIC-J65RYrsdqe7DUVux0YnLSyHGL-L090zEya5m0oGzXCTLNoTVdIlQHadAodqD6KzHHnrdSc9D9myArSy68pKtOPUL4C2t0Q-j8ofsVgdZd_ICQz4kgf2MYgWcIavr06EqUnwNDljhBEZybhE_vj4kfqkp406vgAQUpOALwhe7dicAdpjBo8sfwZEwjDqRLFh9FMHC1fYdLzdUqwlZoQnH-9W8_R2dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t39ITk3557h5D0BuYLHPoGud78R83QYnVOTPeeYibUtwvr2LQ_QlmytJzQfdPTeXfsZQ3S6PSkwh95Ggne4DNCO-QUXGnSZOfP63fb3_Ehm15Guv7xAdGoXA9LiPMBCuiKVh2eqlO61cebfkFWsSXkxMhvxEe94dUazI5VUJCyJxZm142_E2X59kxqAdIYsviDksyUYiKeMO5aXWxesiRoLA8OyAmUVYtKz7ul0qmtDsR4vF8gpna71PzjiEWiEcyZdQjD2b6pNpFZzbLOh1-1p1TDzrQzRNX32ZykGDPP-rWBMeKR1nrxkI_oJ5dxvrzTi4ym5NQmi7Frav9vxr3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8cb5uJlF122tAxZyuP1SdtgSsS_kdY97rdX1FhOsF9PLsTnmTJreyMpwXRiBzsY3sv7lMgVhdXJk4FpveZJ-AHVal4E45rZ3AnjO5gnmk1mg9TDlpVkSjQyaN2p_7GiUEHZkf2FFN0KPj3GLDp1zjbdQHC0JQrQoMtISYhqxGwFsvDo-UStSBIfUh9dTH7e7KQ9LU4jkoR79YkgOiZp1yLM-IRr8OfIyEqitt2I207V_Om0pfwwX4-xC8ETHw102sBRSgyiuOvwm7mP8J7Wc3o67rVExVYrGbqi465ZoHxeeLt3Ph68uF5V1EKTUv2ZrS78N622hY2MyJQT3x5KeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwdWAuw8IYvYN-WH8_lhhdC4OyqgZCHonPeozGKWKu11jlloTJ-fxzRwYLOL5Mflpsvpn96dg3Qpfle4zV2m7ogah9WghfZyYPM2A3NXcrtyPFe7tF71p9FKmTf_JO9RmrHQTXf4-fBLevkmipWJBgVMsVu5rr1I84n75H3lxvcyz86-ZzRjJhebefPT3XoPn1peDb-7QKYtmIbE-p9Sxf12umdm5tOQw52agwxmYviT_PDHG7b7MAq7LCoSIiNx7ntDb9cdg1dFbqkAJI4laXoXypzyXxthi0zABwWt-Xra1cz03xxa68lzUMEqIP-hGdspnKebsZSmgUWAo7Wt_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkpuXCrLvPwoADaepSLTS6KkZYeGtMnS9ymtroBbq9gzQnOd2O-60kgLKLsLyVC7RCZktoXiJY1vk2ZvLzpf4Uk4CNj_Zk_ZEX8lpNXcuVEMJ7cIOrp-hf42vWnglDwgJunsTvZ8cwECJI1O-pV9dFYBWnJym7MmTRna1OFTrIFml-dxLmR16KV4nybQRUa4NnNvZWy_oXGcJ6KuD75L3_JWK6K1jkN8vSZoYjCBpyUKZIptrzct9v4CEwSUBk3Yva0DvVP4DiY7n5tp44FTrCMZFGNCJ-3I-29SAYl31uPk3YSDpbt-ILs0AfucalUj_PK3PM2spjs2qEtlDAMD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGseMVwy03PotjZOUqteQQOUPqrTPi-8s7hDsnFX9Xv8_9dETRt_M5j9ueyvOEItAUfjI010fC6bVZZHVxxS3_q4pJ_jmWfePI0hi8K5bB1V84AfkjhoKgnGjW6HPFcin7X9CwUW3o6qqgYjlFJE-LD43JPT9SYecVTVsmrJqS5GFYmrMMUG7bRYWHKcxzfYgUVzJIL5biO7UlwJQhDvKJXBWtj3d9-jqghqKNZN2wRFQafXOtYCyvijDuWy5tX7inJXsK30GNu1YJxH8vfzrcovyQireO4PbVdq2I6IKJ_2q1hGeTdtgmJ94MAREwlajxYuZvbs4Z_qYFVSMxKAlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pw8lOMbTCNhjQ4s2VTdP6d-ltJlR2azDAXkcCT2WL6K3Ob_hyAkfqkjk7Y9e74NXaAfYI6jdRzyIUbznXhXGdoClAhjeEMncbOyJ_XivlHDloDAyDWrID3FI3Nemwj5BmbRsL97O16KR-ubK67ftZ0Dk8t0Uz4E9bc_ttAfZi3DXSSE_7sjOD-7brdOqeScDn9jLuBgCH7Ky_xqEfUw8DhPrSpvuPOKm0CzrJle3EURgHbfjQL_IghaKRW4IX4-iC3eeFgqlT-kN-LuFZ_1gmy3DoBmXqPXGaVxeQc5vTsppU8iIWakCYPX3zDKb2Azp8crkudHeB2aUAlq4rsu26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGNd-7VJnJErxbtq2A8gd1ItZHtfiMQRgxxapohoDZ3T-Yu6SZLyPlJ7jMRAqH5XWKeGu0UQ4z23LD2aMKRlMF-jd-HZeL-PtugkR2z3GqNCb_FEoGyZ4t1-gmg981iR0PJ56HzyFOC1YxD4j4lhg6x8YkHvfzOATQYK-CLGjpC01Y-wkxN9nJjha5N4IZNoTHab6oRrXiH8b24ScNNM9KYaQfp7pqUh9MRR9Pm5rQ7qmTkXn6k9CDRj6cC_jMfRCgN0e1RyKOhn981S2tv9H4EKPcIkHvLVBGOjDKyjslNoBiYWXYlz75K6BLWqXae-LjYcyJTLiazJZx6gEcNJsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEl72ycIyrS2uaQh5tJ32sTxvOVlzF_pvCuil7phFgRyQvpuagny3wKRoMaAz15HHH6OsLc53a2dTorStfCcC0pz3q0N0ZwZ36mnQJRiqxfgarjJHFY1okZUFQIslAvxgIUKPbBFxtLR0p3GND4yE6J_YSXmAfZs8QX0LsdTp7W7pYxXSMRpMI4QDlks-UP9hul9SAnlyBn_A-AJNxVmCxHMjktSqZqhzZvDB7p1ho8UFqCXh4cvMvZ2HDunep8oBHuuSNdsvl0w-6qdPcRNnKHjsW7BNOyD2YtWbtxR7QacjAhJwhsJ-lwimLY45yNSoywPy_rIZsrLUDOfE-zH6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpKV6jM_Inggum70ERPv8tz7CgBwjPnTIdSVesgRWLOd3eaYRsyoFTDRc0WjJ3a8mocrxXZ_D5OfAETl02DP2wmtESv5S9lTkQepbr6aQE-otCAdI2ajdiQnjzbjdV-glrqxkLQEK9Gjq0_cvileHB0m0DeA6KuE-6kYOFNFW4JHH6oijyRmu8jHGVIYVt5flNVEJ06i329ROFsEirjCl3vb_BIbjk1uSO0Hh_4M1qk8WB6XZ-xJK9TCU6c2PBJPVpoXH1rVSQVU65dVCjcetfDcXvitYroOte4DtCDHHTsopgUF3HG9JmWH9eAZ38rsMf_kFB_bwFO-STurD-zpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-I8Q7bSzC7KvC5tVyS9eGWOktvZOaMi9_PEnFkIUKQVTtH1ZseQ0J83lUQm9fYyiKWzHVW0YEshv9bpZ62rnlGwxftQAZkR1W39m7iGh5kbq3nOqm74OwSYI0FUJdX7GYtZqnoCv7I2YjA76yi3T8u5L9G3wzdj7RdXEHyHugUly-4i8YMvwT11kiZNQdUEOjOnpiiBeQLaGCku_tOqBGl25RnoPqUAGn5xF1JBOEfIZIqnECEJ4uCdQSaXsr63QM5ge5QYduQgTsmSRgq1-ayzJolHoMdqBMA2PUsrJu-iGg-Hll5w2D1fYQZ2apCJIHXEkdkWeicnniasMrk9GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlloSqkgWbXMDSC7Ol7BR8HtEhrFmy3fgQs4YHJsPllW_tzYghd_MuNwUKMvRRY5hfDTRXZNdnI_v727R1hjQsm7gWMmyD_utdgTld4wKAJBWbishwZkQAAN_lwNwIWDon9HmaZ9n-X92CYaWB5A13O0rsVIBH_1EwStx09f8KX8_VmJCFqNgYZUlRUxdeHkxQBgXXPOgzF7zdrv0uVQUU1JTgh9Wg-XkxzdZiLK4KH6SVMvp3S6Lz7BbBOFIICIyTLNdys3WrhWjWKgWOckdYMLqkdICsryCwf2TGZzVwOWrtmJDWFROhhnQ7GY2FFQt6tEiOTZPKlw47yJ1YtMlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX_WZpXT-leMv_sKEEc-tly5YiuUfaO_VrWJsctc9d6dJ3amNcniMHw7NrwFRxdYjUhT9WL1mPkHqJFHxcZbOJWxvXEjfeAhLeEJ8u_IPPOh7oXbJhxzpKxAvcMp5AScV-PcxdsrphquHkjqfRykKcOGOq7P-MhjAsgEe1jgiqSo1ogOYuFGuO2J6xHIT2KnUfkTX06TubYWv0LxoLMubdg8u_sxv9NOlHXxRMbiF2U-S7Yg0TAVeyoRajZhrFldmp69s9aZbL7yBZ9xDYBwfFIDAXiHthGCMwDIiy5YjgLDj8QS0aA4NjHvZQbFX3RTW2FKErzmrDj-9JQ8IC_mPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtHg1uFvLfFXB3KGYQe9uFbGlzb9UmtY93tZv6X_z9xMfNHzDeDx0dAig2UZ1_mmrifpnto9EiNAj30tm3NJR1rnAe2jq0Gkh0Tn3BYZZsSP2uczWMG-Z8FPbZI7HXPvrcG6rEZ-UJ5BWgftyZD4lL0KeLyEA_RE6ErxvaUlgxa7mXmFWc9Fjfg92osmrcDLzviFUAH1xVBjCyqb_ccMYMp9OvFv9rViW6qfvY5XAqDSLA50MOr28mMDdcJgzyOVvgrnsZwDAYj7FhJkq43RjHwK0NyjIW5OI0Duxrn2xsphL6jmoiHgeAD_YjGxfXEsaQHwxwR3DGDg7aoWpjRNcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7rKSmLoaJBMU2Z2X6EhyNCkppyJewPwyKm1XFbpGRT68n0DIVhQwpAiqefV_sfXxhqKQQsjsrNROX2F7pz3BmvbjUgFQz0Hy3addCj_xpuhFPCCMzQ6iv4s7zLgtc3aLa_NzDc8Nr4ILi5zEIj7Y4Jx9ThNM97mr914a35CRQ-i_MJIHMdMU_dOwKvhjv_4UJqvk6X40Z3L7vBOw29MWLnono8GElR1v59zkU_fTXJ3Hy1hO8ekwpeUskDVqzZPNG1uR1u2Fbn2R7Ycr37YJSnM0YDnz5eGSFDhvFY_2EcddlPYmMmEUAczf3rWNVZnc5RNeDaowc-kvs6yyofdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fK9Yz0h2-ePpkXGCR0j6hkPh13EmiiHTwNFsG7BrYsOvqLAcQFBGkpSfesrRsS6CKEGYScb-eNaPomQRfE9Kbd5pxOimj1pleS4yEKz_ZKk4vbYYou8ULfmw9Z_-wgYlwrTEatY2HngCNjhLwZsfgH6z07BYNs_JrZZdnzshH9ZLmfRbS389xjwcBwmVVME0mmrS6yDfCLWAF99EGdIA2cKtsPVpKJdL1XYxT8eDenoPSuYd4OH6TWKqEMGTlNBO6h6cr_bd632mZk1AWFfA_axWvSsZX-qVem2-iKYmxVxUaKWwqnHNLL5urV9nsMEfC1mwgPmYmiNJUaTP_qeVcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8kDpbuS2rHbGhuBZR72obPoskfUsqdhK1HM0WEMmSTPBINNXUp6uue45fo9Vnmx_C3o2fJbvjv7eGIqIVg29a9bUQ_6sxI2NW7HZzusdww3CYZwQuCB4Qc2pqG6F-VyqVNeuVgFSApe3wX8mRtv27ROVtD1fAPQeQvxHZ_iVSpdbKmuwXPji_XCkSO4xV1IfbxC47MbhQNPFbg16BQoWVYsx3bQOu8PSeebP6n7zTjSdwps3UqKtfm7Iz1EgUrHbrwDawWeD-lMbHH7-ouumuLkrb4vIOaqrubFjKSfoJ7eginHwEiE355-3Z1nTXTwwc0w_qNAOeRC281DGf6DiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt1IFujj-NKvItKDMEstipkHw-JwdSoPnYDYMlNyFLum0mx98OobcIEZ_Mm_Oex0KuBL02NYeufctNYxKRieTC2quaW8R6_nILRZhD12cRhFiiE0mhlP0BwIFdMfZp_DwNGaBgteYd9YHwEE7D0XVLJuu2fxjz5Klq1ocT1QjmAmYUSN4Vm4n-_ys8j-gsUmLH2TrsX5lEcOxSUOiJNzNuGbhrB5-6HBKxsmoErxnHaEEtw5EcXXmEYTLc4hNxVvE76CXqNFWbUAYZhZkmr_6iLglBDLfw6mblljdMyBiJTFYTfmOYzliOIKppoLCunrgEx0BeLIidGrUn0JbkqQfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIOFarSiiOFuU4FEtU0VeWXG9uPqpWSuCwNOSQZFk29uBpQ-ybyZERyMWCtZxAMVwv_V1eIF1lU_p3l5pshoM0CHNSkq7rKwZVNCtCa0uYOQFxdNSaWR9rWeOwsN3FMatUnDX4roJzYQf_P8mmrR66v1u0UCaWwcy_TMnGRJmNS0XMeRASAaWstR1xDbnQFcv2vy05V6H_VR90VlrdEcKcfl8Opo_TPLqdfYohCNTfmSQR40t3tWmyN1t3DBLcz8H6-M2sX3I0GlKBJ3JjDvVMEz94TKaA7EoisRO3EFp--WDki093dxQH8iLbf4Zav4MJz5S43gNnM52X8l9EOJ0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYdt4Gi__JRKFfVCVk63XSu13IheaJJrPqzc7N07DaMt1nI0GLK79gIfd4CXXgZLLz2iY7xvatXIMsWTcpf2c8i80w686OQuevKQqfBdE1yBvHAQ-5SCBDhRH2nsBhm546WSOZwBEO-mm7oOV69iMxC9IEKiFMsPL-e1UUHP8p4HkflXUCi_7OpUSj9qLKVtyO4V19RHg4f-AGX0t36qSR4pZNI3y3gsuZQQ0vhE-Erv-VQKFUlumcNt69plh5P3Dazh0h1Jl6M95lcOsKYyWQvoV-SMp5lpNOvYAayD1ltIuev2N7IkUlD_N9A8DAOZ9vMKPCgOMdDnNNXi7Jq7Ag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Xb6NXm_Zt0-JAuwtwbPnPEHmifh5Tr2qLYiBMGYe3UpV4JWAGlcQtHbSKDOB5jShBOaBg_P-_TGjYN3JGFREFI10ruMRoelXpct7EpYzWOonTHIe9Hs6xairoLIzdyFHi07E_5ZT46NYlqmX-GmEFUoKg53Dab4shyXJcytiCu9OsIzxphWnLJ-3bREAJ2dTKh9myOX9g6bXviwpLS1tqSRwACdAvuBIJSAWkMP8prWZakrS7gPca1vZYwse0nTe8sY0ZNH8aTOOpELcrWFg32QTFagFrUNxZhS4Kz1eVM1jrus4CWDGJkG5fAu0G0xXqvq0u2ks7rbxzYG837w5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Xb6NXm_Zt0-JAuwtwbPnPEHmifh5Tr2qLYiBMGYe3UpV4JWAGlcQtHbSKDOB5jShBOaBg_P-_TGjYN3JGFREFI10ruMRoelXpct7EpYzWOonTHIe9Hs6xairoLIzdyFHi07E_5ZT46NYlqmX-GmEFUoKg53Dab4shyXJcytiCu9OsIzxphWnLJ-3bREAJ2dTKh9myOX9g6bXviwpLS1tqSRwACdAvuBIJSAWkMP8prWZakrS7gPca1vZYwse0nTe8sY0ZNH8aTOOpELcrWFg32QTFagFrUNxZhS4Kz1eVM1jrus4CWDGJkG5fAu0G0xXqvq0u2ks7rbxzYG837w5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2IURqzRegDQxwJ06dcfFu41T-oATI3x5O_TArrGQnaVb8R3y4h8re5zlxcXYYtED7hCDRyESFC753wX3QrmELCh4CaU-au3Ai_pimN2aX1o1Vd9kIauOGj0J7h1b15_R0ijwI9n2C2jAy9_3P0C-7KTneSKndZtnamRksZf_WpE57YVyoEKrrKuRi824rEWydDRkWBMD1kotlkVdogtjzBKShocTMxgNpX_Og6me9dRUcdmsf7LRvz0j-G1edKRDON3zyZ-ODmDlzWeMjlUtS0dtqnAmK8sJ2XaFp9u0YmzurFcpdUR5uyl4uxWT4dlthOOhfGbHbkqcK4Hoo39_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMhl90WbNobXCPNPZIPXbO40B1ycJ6NZlr3OL0TzHOVysVgAnwQI28lYyoIiBN6MjWKKBEFZxE2z1vw0FWeKW9eJ1nXXuh38ARxknAVs8aU4ZKyDJ0Kitz6ukEy6PzradU8YCNGhVl9cB6JUw8lLTbqv94ws4UHNhRD67D3OxQaM4p-D3mMEcRJEvYxfvmOReMUvRHzj0jB2FQyDeE5_QmtMyuGZ0YpBI4rqEL4NhG3H7fumpjcQLa7hNkOzJhGpiOMIQ4FSPa_yIfffshTJ5ofi0K1Zi_2s1MRlWT72bC2tg1tMSRQeZ6Vod65OMliG5GBhJNSSp3wnfDNaZkcYbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrIAnBlbx2wOMAgkTGt7l2bRqjPU9WtTMdizulGI1pTBwogsK-QdNNW2uLrXSarnC_H9LhdZADvjvGX2qH_9Ep_u2OdNkkplx8Sx5eGrxDs6D6IsWByqVtf4rSpiyjBVer5ap32LaQ6vKw4oZ6x7nNkBb2h36hQ6M_L0bSDN7L6qHYpBAJxDGENglUI29LlB1EEQRf4GqgaMwD6YJ5nC3rscOxJRL8o7Yywz8ZjHD0IL3vgAiGz8W6tG6_Se7kzzEMjWZHtrCeA9BJ9_4oDC3yZ1FVcw-CbZEk-sbBX_ZkdBa8uUpjwO9RnfVc3YugkXl94Dgq4rO7O9n3bGq2HaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZRWU_xz3T6pdnpi0RQ7tW_yxwMbYAezQZ3sn3fbY4IdiAYCq-XJryyDp2cNrBedPFW1su23svTWaNlPftlOY50ky8mZThNorbI3Uxe4COYBosU5j3KlmINNeHwbcVwtrXnqiCFrBbXqdwlkSLxN8mr64oJTPFZolNrF_FvK51I6OhZ9vOAIzf-rSakyszILKfDQkznQV776YXmSR2n4stjhlN1k-6e3B1JugeUMswdkc8ZIccW6Xp6FQIxQNQ4YtnXfksTBBgqaFXQDdC9vZnsENyIzZ1SniU8nZia3x-xwu45-uG3yOYX4ny_KsCuq7pKSoDquZ19b0CIFXYcMzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CubPzXPKHiSzVsPiBo7myPUiVE_CH1gdpJmD4ChsqsS06iUQ1cLZroeZywLXzDWNrd9bcTZdrWFpYFBRFaMcgHITqAJlUWtblTnerO5tsKrw8GgETRVlxpod5VDNytSjUAisNM8NivQgtjkwqwM1vNnw0ykNU8ftiIrap-Fu6rTcVg_LRG3H-PsL5H8uM5R9aSZDoGQRezio6AT-IGDB9QwIfUATQ4-tUEOGmmDous2S__8T7cDZTTnmcYdu1p6ZMAI70UF0rApBuxlwbBpVP1EDzshg9wh9SMa38FItqa9QrbnCDuIHMeKF-1sTyKN_c68Z9lO-mp8ngm3JXbxnbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6b85cHvCXMLl86AIpxhM0pouU8bU7FO2kCz_gMPRuwRLb2hCnhyOAx_VutWzv6-4tl6F0FUqsSHtoBaPDCxjZ-654fGRPZgXFB9r-SKX5wg0ApBmOR4p--P0G3NhAeFforFiXGRTOyp2OYHw0EjbtW--i9Xy1egL4EtwyAqRrMivrHuByMRDDUCMAciJR4cKJNEXd6_pX2C34PUAnxRnt1Dn8InOVzphrGmjfXUUTG2vnX7cHQNr7NRnZcwuSRxKs0q5aPUgGLB78w9r5Zm5P0CdXYRnEjIktQlI7GlV0Dse1_tTZG9qkGPZHE3A3mE8B4CoUgaWMMXEkNmF3ptbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTgWRVGlQWvsrSpJJD_GPAcwaNxaGQvEwq4-tFMCkKOSSM7s0rzFy_kYQfd3mkK5SydQDyC-_lQKdLoyClU1AUx2noLG1JbCI73_22riGmJfbbGKwmwH0l6rVexHUoMNqP3-xrF6sTi_og-Q1ukNJvP5Sw8nV8pQjCCwcyDt0sWomann5TCGMRgoLzu20EyFgxtOsUFyqgYE6ztHLSafcLBIplmty9jeMxkmDSOZIjtMEpX7kYRcBFZ6a6kfZ2KKdZIoC99Ul0e5RLQuK-EAzqJOthT6-MNZ2yiIBKnMIub8HW4Q1zaqTJmipN6jWfGEivmKsGZzQRVgYCJTN7oVyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rMh7Kl4dmOBMo_7OlytnzDUDV31jPidssQ71GJyQTHO75v4SEI7UaoSOS531frXGQTz4IJDT0VwZhtb6hGDmA9hN8_UcT-Sp3gXFvZ4SNq7Y15FHQv8CYZRaxmOXTboyF45XqQuYt-ZbgFkkb_74Jj0zPGiKvjoRUt3mcdDbxCQKwXwpTqLN_btKLn8pNVKpy-R8yXQX-AxJqDSGG7EkWiu0fbVQioJ3qhO5d62YOdv7aAI7CB4g37mJH5sGixxA_XBaaXd9WUNzzzta1bOjbgKLAwS-jeZ6SK9pDi8AjzZ0JiMvKQDNSMak6L_S3X3bsJF-OklMM5n42asaVfcQVU2_6zN27e5ENr8OoGPu3s3HU9rQBraO78w6wg1qCy4VTX0xSgfZ_h6SrRT2TbsYPpvBqV-S7B8jcyK_Z2QT2T_wFWaH_Nykhl1V4PN2Xo8qp4pYKX1E0sejgunGrLGwvLOp9XjPpznddPCMjAupLQF80mMKD1qOB1BSqq94R8dg16CoH07xQjgpeIjIlXgUQDYeOZmDMfyvQ8aposkW_7rZ3HhwfPjYCJeS4SvckL5bJbRkKz2oGIUdlzriY3vspjaHQX7plckj1Xsibru70kPuCKEF2u6Hb_dV7Rj7W5uDd_QjdZI8iDrsUQkkbZt4Yff1cyTT8rR4u6e0uEBgeL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rMh7Kl4dmOBMo_7OlytnzDUDV31jPidssQ71GJyQTHO75v4SEI7UaoSOS531frXGQTz4IJDT0VwZhtb6hGDmA9hN8_UcT-Sp3gXFvZ4SNq7Y15FHQv8CYZRaxmOXTboyF45XqQuYt-ZbgFkkb_74Jj0zPGiKvjoRUt3mcdDbxCQKwXwpTqLN_btKLn8pNVKpy-R8yXQX-AxJqDSGG7EkWiu0fbVQioJ3qhO5d62YOdv7aAI7CB4g37mJH5sGixxA_XBaaXd9WUNzzzta1bOjbgKLAwS-jeZ6SK9pDi8AjzZ0JiMvKQDNSMak6L_S3X3bsJF-OklMM5n42asaVfcQVU2_6zN27e5ENr8OoGPu3s3HU9rQBraO78w6wg1qCy4VTX0xSgfZ_h6SrRT2TbsYPpvBqV-S7B8jcyK_Z2QT2T_wFWaH_Nykhl1V4PN2Xo8qp4pYKX1E0sejgunGrLGwvLOp9XjPpznddPCMjAupLQF80mMKD1qOB1BSqq94R8dg16CoH07xQjgpeIjIlXgUQDYeOZmDMfyvQ8aposkW_7rZ3HhwfPjYCJeS4SvckL5bJbRkKz2oGIUdlzriY3vspjaHQX7plckj1Xsibru70kPuCKEF2u6Hb_dV7Rj7W5uDd_QjdZI8iDrsUQkkbZt4Yff1cyTT8rR4u6e0uEBgeL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUn2xkmTea7I6oirsnqA2VBYp9piwX6Bh-gvzJ-x-kAtTDwMKJkc_Bw7qg1VefjQP8BxcFjPWehtaMBWiPtbG_OOJVuMNvVhX7BPmlDOP3nvZTQzvoASo6b3JFWoBSDESHglWC_R_qILlANhbolPYNqcVwIL7t0_2TgMt9lzpfNuOJH72n1znarGxpO4PlrRR0iBbCz1dSwyryrvnRW-b4zwmLr349nUem3DsoYE2hGXmIAzHRRCL8HF2eURjzMdYdYJCKWDA7DPVqemEv5jlByBs2-TRYTb6yL0rPIuNJfPycMeA-RdezpQKIY8iMasvrmDnZXGyZgdMDvot9hjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLUnG7fjlCwt--dMIg1eA3iFsfGNHypmxhDgAizpgB1eZYqnC2jjBXVY_9Y3kvN8BP4LPUYQyek4I26EZk8WUUy-pxW-PL60quF5hz4XyVm1N_iVVbmDBSn7hO-zp7Cb5btRVZSHujzqajzNHLnzVW0XLTOutprrT9PrphE_lkqFVFGdmpcKluu6ShY_BEgGS-UDYj_iQEOI8-feAfwjnzuZ42kwA9rOAURjy-bQjrx6-VGOPDPxt0WlOIgy-iw6999IVAGXU6Bh2Uk6PVkCrl4gILjkWLzX-J-NndJJ4p6_dId1MnBcY1YMFDNKLNWQpFiI2gj7ObiDHhyU7IRV4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEWT63tcY-awFSOm8IW4e98cu8BDrEH-LSDJZTyhjZ28g0zGv5aQ_18aOmCNj3Z0QXTBmKRnWWpwLWVa1OOWqctXLLflSzQBJzN7gZRx30Iz1hMuM7MR4AWJ433I6jSI4IHuj5G675Ggr_WzK4rDjDiTyZyEcObf-uaZEGp5ufcopfFWGd-y5DRkahLxvqyRVNtr17AcyICQbY8QIwaT9EQn-_TjtCrCdBCKuNC-XR89d-TvTxpAImOoRDo4rI_YL_8JFYWcyVWSetlFAGr2-b33lOLNxOM7-L-fo6EkBKdYcyNQVah6yixV1ETC32-ANG3PGSZh4Z3tLrGDHL2qCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzWOiaGOntU1Dcp9Xvxul_DgVkohuRT9d4z0XErNPBcuRGxPv4UtgJSijoYEcWtzgVORFWkpef7c-drBVpSqUYfZc-l3LYQAw9SF_CRYI8_krNv2Sc_hbVcmDEEwWxPArlIYG0DH29lldZywkkycAJ56dvl9SIn1hHsKov6mzG9unrunfTamS1jocw8xVWj6th133fj5YqFv6eAfQfmMzugFY8RK90IkZB7X4snqUECVgDdvMID5rikd6AkSmzrbOg3QI-ndxmvKz_zUP-M94jlaZ126H1E0Ixfzwo1bc7duE3SpAMATppA4SPyso4azszmTNIdvEjjvqKR1GN41Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaZ2NbcK1Mb6PZJdq751YR9gChmfu5KlLlWKgArJYpyPYQdv93Vfk6ziy5EXBj0t-JS1y0z_BnAhZc4c1qnV9G6P6yMIv6VHb6ajjfWN7SuzlCfuPj56EwDBD9fQXq8mOrggoF1VEQxN7u0Q7r0XPum2BOuPcou06UcBX5yG2ON-cLA2Ild8PVhBqwIoZtonMrJTfmbMq7bd1v_7RhSlkqAsMB_Ef--OeFzvSbWbPekcF1Ju5aJGL5S-620feiYU-mUbbuwjzY4uqlatK8VAlTnszwrNiMNlZY9Tf_uuufO61T3wbHwU1eXtDdUO7ObZ_gdJbCnYQaw26pPwF97fkA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0X7KCeOVEG5nYBiaeXNs3QnF8CwZiA9emT1744kGzYv_bebcRdTBDRqzYB9_OBZbcesa-Jgo0-uEXPhKU4dE1ePY6Jh7aKUo9E45AEeJ9glAqi-l84DUSIZiMrGfArtvRs39njW2X-p5LtDtKkcQIrmTn480MAFyM_OL7bOzjNWq9Kyy15s-7rwOFnIGnzFd4OnQ_hGo33snPvjetpsstCmB7Pf8pbWKyMNPARb0wYRiT-IbM3hYuaqJBY7bQovyBZA71q1Shpj6LC7rEx8he9ezX8Jx-YyLBgN8pUwUfbTxdmm6pnPc-9V_JstB51REinaUsCbo1I8yq0U8Xj3iq7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0X7KCeOVEG5nYBiaeXNs3QnF8CwZiA9emT1744kGzYv_bebcRdTBDRqzYB9_OBZbcesa-Jgo0-uEXPhKU4dE1ePY6Jh7aKUo9E45AEeJ9glAqi-l84DUSIZiMrGfArtvRs39njW2X-p5LtDtKkcQIrmTn480MAFyM_OL7bOzjNWq9Kyy15s-7rwOFnIGnzFd4OnQ_hGo33snPvjetpsstCmB7Pf8pbWKyMNPARb0wYRiT-IbM3hYuaqJBY7bQovyBZA71q1Shpj6LC7rEx8he9ezX8Jx-YyLBgN8pUwUfbTxdmm6pnPc-9V_JstB51REinaUsCbo1I8yq0U8Xj3iq7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKCN24h2Zz0PcJSsgfrFzjop-nSGKySKIruxAwadXT7qJF1S5At8cQDDaiLlZEiFQKGo9N6Ww9vhwsd0yophwyazCRuq9Y5P1S7KYxVrpsy3rezY2uivDWS1zIswXe7zbHcVfXv5OQ8d_i-pjZ0XuJ6Eg4kaCOgR_Y6nvhviRZhozp2zl8Xi8p8tGGlR6qnELPrAssArE7sY5nvv88wfSxQal4Omdug9y0qIauVL5NvJrciCjGHqVEvGzMhtkZTcoH_mGbRIG3Bsg-WJGk1lxBKIw77t_4V1hVvlfF2ukkhdstjgcSOwYaPWpqXRgZ4Lj5bHYu-mViipbOHiqACXkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7y0JjZeYpNgcIleKvvbeFHDGWdaVSEyaJaqMd5dood27oL3An8bRb8jtjG7u6G2ZpdmqcMlCaYupFrTjtqqdNWgZlayv_Wlk2dA4AyyFB6U_2ePF1_UVd2bg0Stv92_AyhSYn9a0iWe9iDYM-JaCIE8kBN1O4beSHeQM1uSfNpS_K0s1peKRV1V1PqNNpBGHkllaEL8iZULBq7AcFR3UPOfam17htPT01gDmz8uavS-eAxzwqdQzi306bSfta73YPHhv3PO7nlp1whxIZoFGQUdtI15m03uPc4rqbAI8ulKjdzSXz2rKrbodIEeqCUU610W3wUHbcxneexQMGk49w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8Y1sfA1jkkSckycMCNFmlkW-7ZpLJCMUiK01tUW5ypfUhk6fSncqK_btdY5riIoCK5xVnnarKiQMguBNp7n-1bZXwat-BxLR4bXtKcaUyn1_n3UFAqZHYzRJFm5kkFohBCu83bE4Ay-8lMwopNpwszcFTkghQgr35VQNPO5sID_Yv66L7JIv2-6O8uHUHRrFMC3G8IbEsdaq977_f4i0QIy3LGhv5YyyFds99jTJRA6Xu1N0Isz9OXakRxi3ndjemBdQTSbi-1DLGBVZ91jnr15MkDiJtDAbj8TTb04VMCrqfZFADwd7luSt-j_f5TouKe2pAwLXgSK351zYk95Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkwxavzPvPH8hGAM7XpENX6mH_upRhnWaj_bAhFNJfKr7Ke_PMk1k6SuZc8QuTQ_l9Q8PxAi7WPdKQYf1ZEo_qHzwuT_yFAIgo8fLT9VgEj8iB4gLz_MABwoXq6pNj9gG6ZE3eAy8-oSvYivYSFr06ntXej0vlPlkf8WwoF60fLkgg25mNlpyLr76yqkeI3hnd7Aoc_7bN1v8H1dkcBvQTzjKnlES_NwqmF2WjB8t-HAggItWTqz5eH9H37aw-KXmv1VwWp-hh8KEn7Q30Wyy9mqtsbm59UqyoOSaJtdKH-tTQzWHrWrVjSm-EUA3LmAAX-01pmNil-BDKpyFEac_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m021rx3m4fBoLzJ08hRVzKvp02JdfZXxZhekl3aYMBz8fJwcgbjzgTH5haMGp0wYn8hPcW8unr-Osu1T1cPbNIHmoFA-NXBACvfgr5PTV2eQkDUrF-DMNtyJrNnoANaL4ZZ-CHxyVYtwYGezbjLZyOiMv3NVkzKvu-giDVJV15hBi6jXP6fNVeeLX71y76DgcoWY1MinGTA6YnSFMjqfoafDfIEeGAYD0x9Ukgr2o_J_EF6gtmtXjiLaN_iqXEgLH-IFDDnvMDfIHrsm1P091LCC23UGQYJOJuFUhZdVlMvnc99lFd-XLXenGlPr6a95O0VoZcMiXN8NhooxVIHd3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp77rNDsFWVvpe8eH4Chh3ksmiNfiLycqhe8s8c6fTeHHBOi0Bz1C9gV8FAVOGQaN3mVKzxeF6_BVoY7Xr7FKVnNPxrCP39DjxnrC2mk3R4PTaVfE5FZkM4s6P04MzjnOYGONhIQskxj9SAlTc_TvxyqdDNmG9h3OItf9HyzqAvs07r9uBqUGqH9qMQc5cj-kHpQ-K1r7Glnb7cBQTsd6t1vjhO476aXgEIg0iR02VukbLIhVjxVKZj0HrcMDcp_-7qvisO2JPr0O52ro2p1DYpOTcPFZapu6bgSE1Ns0WpLx76l6RrbvaA7owxhL5sHVpaLQtZ2FEMvKcgW9fqyaA.jpg" alt="photo" loading="lazy"/></div>
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
