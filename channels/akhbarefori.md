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
<img src="https://cdn4.telesco.pe/file/fFAGFRpolZR1WQSVV6IGYMwwxEaRKNgBS_lFnekThVtFj_Gbzrcl1seWFVQ4jvUu9IIyFnfpFmHVCEvUCVaIG7bk1_GpdEDkXhejmfUYGQMAJYbuncPHYDpZDFSok-35VQuDfC5yIqOwiJd82WvllL8w891hOv-n3-IymlAY9C3qDiVzQwQOJGDrsf2RGzjSkom5j6uKMDOcpgfQOQ6GIRPmPdCc99tXbmAOhV4UiUox_E8cJT6XGRdAejG0FU2ECDaI3NwGv1zeRwBcfYfru5JAg2txRzcaprPlMRRRumWOOoqJPQGP36LTvlxqOQ7uBnMdNebh1AS9qb5_9st_Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 21:12:19</div>
<hr>

<div class="tg-post" id="msg-681499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع عربی از هدف‌ قراردادن مجدد مقرهای نیروهای وابسته به سعودی در مأرب توسط نیروهای انصارالله خبر دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/681499" target="_blank">📅 21:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681498">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
منابع عربی از هدف‌ قراردادن مجدد مقرهای نیروهای وابسته به سعودی در مأرب توسط نیروهای انصارالله خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/akhbarefori/681498" target="_blank">📅 21:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681497">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYm28UWFG0maBgCPU2eEkRZoC_Mv1tVJ5qsPdaidR-4T5OXLR4zSfkACsuGnsgKDG6hesLFX_ah3jBJG2BeEUtz6D-iQVLG3hSHA8AJ6gyR8Kl1F9SqXRJjXlTn5lB9j4DjMa-SPAYPf4GFA87W075fD1rwZtkEP83LefGn4vykfC4LX4WZRwSqqePy0b5_MXG_uEVFxZXl5fq7CYioEd4zF58wkqPa5NsLoNnCGL3Ds-Ka5oVGffuKP4WCgwCtEJsWZ5KCstcWgb5Bw9tX7mtTQb_gOtpBPnNBDcsatioeukdbb3ggCjfjBpNzIZIusjuizXKJdVx9Yn4SX9lmTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نگران تمدید بیمه نباش؛ ۱۱ ماهه پرداخت کن!
با امکان
پرداخت ۱۱ ماهه
، می‌تونی هزینه بیمه رو راحت‌تر مدیریت کنی و همچنان از
پوشش کامل
بهره‌مند بشی.
این طوری :
بیمه‌ت به‌موقع تمدید می‌شه
هزینه‌هات بهتر مدیریت می‌شه
نیازی به چک و ‌ضامن نداری
✅
بیمه‌بازار
کنار شماست تا بیمه‌تون رو متناسب با نیازتون و به‌صورت
قسطی
تهیه کنید.
👈
تمدید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/681497" target="_blank">📅 21:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7w4Lki2DH0IMlz_n4WxxFZXfeAPatg8I4pb7YOGFaujJs26SDEChzm8VcCgtfC-HPXtj_7Eiq1wlcde8p-qa4rueUiQrfbcLCzZwHwgf8pdKjoFiHnQXFXMoW7X8dzgnf6HwNzZB2__CbbDlmZ5laQ2WK87xx3sR6qhvNUTK6dztg3SM6QWJS4l_s3vVamQcHl04ZMFImdEw0ZCuvKjZUp4uKALr8DuF2QRpDyrS-CKpEJOd-EdCYOoF9aC0ImNH-lrKL0s1xoHZqPwI9vS8PvwCSRxqCXfz4BflehpB5mGZgXAVai_UZtdZSRqeZfJFu-_5psXC954bTHhqus7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد رسول‌الله (ص)
🔹
کارگردان: مجید مجیدی
🔹
ژانر: تاریخی، مذهبی، درام
🔹
بازیگران: مهدی پاکدل، علیرضا شجاع‌نوری، محسن تنابنده، ساره بیات، مینا ساداتی، رعنا آزادی‌ور و…
🔹
خلاصه داستان: داستان از سال‌های کودکی پیامبر اسلام (ص) آغاز می‌شود؛ دورانی پرآشوب که مکه…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/681496" target="_blank">📅 21:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHri-GgPn6EknY4zSVZG3wvlZQSZZEzaf1lkcpF2G6uchpX9YRcsT74GXCjy2AQFEej7oL54XritAiWPwg7LsxY12YKiptAEC7Ql34d9FhL4hDaHD0GZOAMnTtfOEBsX4-FeoVhakD0SSTeMG9ciFXbZp6PrHREC7SSAH2JrpLYP_iNjyRdN36SqUL1ZOoQwk1IBf4W7fA9wOvwLefw2bHprqUxVdYs32nFsid62hSAVUkay6eww6v43hcyM2nwlKtWxyPvVd2CBN5Uq-YrJhxBD5b6DKEGEX69CthDmxPGOBrKLbRvz-HDRd8UdXv-hm-rhrC7MeQWQ-bCShArONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3AKy8LclAUh8eVY5TnXYRrIt_DGNioxDOau4dvVKEeEe9m5c0npx-e7wE9sMYX392DCQrqCQi5CzfjZ8u8cUaQgMMAUkZMunEU4evsdk15adQzeG3AsjffOaP6jKr8-Ol7IAlPIqXgWm3bonpbNskp3lidSUk_eexLK8VX0KEiPxsLLM-wXFxERTAUVY1UseC57y5x9qgHxshxi6rBDAoo_S9-QrfTGjkTtwMJ9L-yVzeDo6SGLBuoEUINC6a_vwixRvXJH1jqsTTAdi0UwgSCcHzYrh01PsCxfAmxGzfKtei5qHanVv8LOhJp3OZsjdGcAYpZiE-duaLU8aIIqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6UAgkkoxojt4YA3BfM-Ul26hiTVIJc40OvgPl0cpGVGoWHbjOayIhU2lYAK4tDRRxizg3oqIpSFyhz9tzQXucm0X4rrQuMJq3YPN9aJ5H4I12zzW2VNukLreDKoFvMrGxYjKUlegelVfdHok1euW__gQBKJ_2Jsg-yCJPzmSWM0RC4Z5fvFkwc8-4ix3cwiAGc9PdR9gCJ37FyCUTrpr7l0MTqhAWFRSXhK5H1pF4RZYa_TN7S18N8hxetEaU4Ea0pBgQ8tE34e6-Syk8CgBZ7Y1GM6bINjwQ5_uIPSlos2GuSj3G0GgO8xkzbu_F9GNFNe1t1C5xGJGL99KzhOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNDjWgFq2eKgdZq4frkv7eE2HEuclm_7dAqOUs0T8oGXMhel7mU9XlRLc0TAqZdDeBrcurQuMOcJ2s2-4bldgb2Kri3QIfEG6clGE0t92hv-URR6BHVkyNRrL5KpC8CXtRRkgSXSrW3GZNFY3uWI4Dyv90VZEGMHVf0ctqTSisUokfvUWMR5lUy-vbeIa-IccSSEwst7BY3EqBSaFC88Lb0EUKBLmbdmbVYFSLtoY7VIeJ-z6MsYavfygGJ7ncxVBmdkw7YsFvhMgeSneWwP0B7skbygKcSBGkL7mcqDxLaYktWXrYp5zis1WpI-8CK_NJn_mqZZNH_Z9R0IbNgKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMpd2NAKQPljd1_jf4JUfs9RRQKe7rb-SLX0WDqkI1iB3JjvPmvE9znNn2d7wL9LUUkbA7EftFAPp5yOivqemQRjpqKxFTwvSZ4ywS6Z9Ndyc0-EHW4udKGvadaNbnybUheqx_mbHTvvpdTeYT6MoYnXyeNgnOJRCsGTQhFAgkt1Q0cVjgnBRtOw9P62_JJXSDBrHHEVoQUq2z8Vu6KEwalujZ680NNUFNBAnaGLhFwjvCVouJ17z3kMUWWrQY9rxUOZykITn4w6_H2Kdi-kwSkBSUiwtp5-hNmbDMEfHodD28lr-VBjedH1U2igP2wCfHuXUG-EjuQ337R7QrFc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIzXePdw1l3mq4vpV0NqfJBgvKdgmbqaidpZ4fIauh8cSjnqhtqxglRH0LQSFcftS8YV5iMsBZPqNGb30bYM-6HgqRB1o_SNwGHzkhhxKselXi3QhddxDDSrmD7cnTtys3DaY5Q9Zwx6x-3dldbLP2GrY43NtNmlwjVUgDhNB-UcX52-Oc6rkT2Vb_R0OgMOcQbEF2_AE07fmhWzaHaiwB8vrBYQTy5c5Ety5RTBWI2BdfU7eRbPC1GAj2xstl03ylZBNdKMVE5KWPa51oV4eIUlkBUZgvY7uI-9WxIIQu3LRvEY2OqLLpxvxrL8FlGQ_gc-Ud2nbb2I0QV0G2gUCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هلال ماه ربیع‌الاول و نمایی از گنبد حرم امام حسین (ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/681490" target="_blank">📅 20:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وزارت علوم: امتحانات ترم تابستانی حضوری است، اما در محل سکونت
سرپرست دفتر برنامه‌ریزی آموزش عالی:
🔹
امتحانات مربوط به دروس ارائه شده در بازه تابستان بایستی به صورت حضوری برگزار شود و برگزاری امتحانات به صورت مجازی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/681489" target="_blank">📅 20:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حماس دفاتر خود را از قطر به ترکیه منتقل می‌کند
🔹
روزنامه معاریو در گزارشی امروز مدعی شد که رهبران جنبش حماس پس از ۱۴ سال در حال نقل مکان به ترکیه بوده و این کشور به مهمترین پایگاه حماس در خارج از غزه تبدیل می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/681488" target="_blank">📅 20:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgKtx4I2zb8jMNHlmDaUURRnQYxvDtNUV-G9dm6iIn6nulXaYz5cRHg1L-kP9Cl7kl8wC5szvMhYNy4_1ac0r9_z91CJbf6WTTqIYnUZ2YTAo5ch_2i6LsYVSivx87fzn4DOYKus1ZPhDNMVbSyzD9OVruR3uIndotdEpxPX4kPm2gpAg0XVP0diQ0tJM4wXJv9Q6aSL1yTEKWPg-Atnu7OMoPkT97FAhl29CWA3-9yDHLMzC1jR3xMWM_3uhg4Tyi4dF47xdMmQLuVh1_NjqDdFjDt6CJWDpLZyjHbZQH67eM5wnuTK-isj8zJErozMOEzxqYMf4KKTJ2BDpBRcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مضحک رسانه اوکراینی: ایران از زلنسکی می‌ترسد
ادعای کیف‌پست:
🔹
حاکمان ایران، زلنسکی را «دلقک» و عروسک خیمه‌شب‌بازی غرب می‌نامند اما شدت واکنش آنها چیز دیگری را نشان می‌دهد.
🔹
راهبردی که بر ادغام تولید اوکراین، فناوری اسرائیل، توان آمریکا و سرمایه کشورهای خلیج فارس استوار است و می‌تواند هزینه دفاع از متحدان آمریکا را کاهش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681487" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
روزانه ۱۵۰۰ دلار درآمد ارزی ایران در مرز افغانستان از بین می‌رود
رسول نصیری، رئیس انجمن صنفی کامیون‌داران تایباد در
#گفتگو
با خبرفوری:
🔹
با وجود اعلام حذف عوارض متقابل، کامیون‌های ایرانی برای تردد به افغانستان همچنان باید ۳۰ تا ۴۰ میلیون تومان هزینه پرداخت کنند، در حالی که ناوگان افغانستانی با هزینه بسیار کمتر در ایران فعالیت می‌کند.
🔹
در شرایط فعلی، ناوگان ایرانی در بهترین حالت تنها دو سرویس در سه ماه انجام می‌دهد و بخش زیادی از بار در مرزهایی مانند دوغارون و ماهیرود به کامیون‌های افغانستانی واگذار می‌شود. گسترش ترانشیپ در مرزها نیز باعث شده روزانه حدود ۱۰۰۰ تا ۱۵۰۰ دلار از درآمد ارزی ناوگان ایرانی از بین برود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/681486" target="_blank">📅 20:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681485">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وقتی شیطان در لحظه مرگ وسوسه می‌کند؛ روایت عجیب یک تجربه نزدیک به مرگ
🔹
00:08:00 تلاش شیطان برای انکار خداوند هنگام جدایی روح از جسم
🔹
00:38:30 نفرین شدن توسط فرشته‌ها هنگام دروغ گفتن به مادر
🔹
00:52:40 خوردن سه سیلی برای سه دسته از گناهان
🔹
00:56:45 دعا کردن و قول بازگشت به دنیا توسط روح جنین خانم باردار در بیمارستان
🔹
01:07:00 علت نارضایتی انسان‌هایی که در صف‌های طولانی، نان و شیر و خرما می‌گرفتند
🔹
01:10:00 تأکید دختر بچه سه ساله به خواندن نماز
🔹
01:16:10 نمایان شدن خورشیدی بزرگ با بردن نام علی در اذان
🔹
01:18:15 توبه قبل از تصادف در شب سوم محرم
🔹
قسمت سی‌ویکم (این چرخ گردون)، فصل پنجم
🔹
#تجربه‌گر
: سیدهادی سجادی بلالمی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/681485" target="_blank">📅 20:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681484">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2689297ea.mp4?token=qTAnjWUCMrQptz33-smhWmqYzznjQk4WdiaZWpWtUw4Sb_elQXQ-DcP4tFCiy-5BABK9SeTQ8zDroY9RhLHAHmca2S7ZI8Z-h_Vsyc0g73O0ZE2JOtRreNAiX7p-qHQtGAAQqludBBWOaCeeW5QMd6cwfmsVQp87nW1SbXkSWmhV_IHoVbpX9mZhfO4FLdnakIW74O9mMcXBk0WB6JGkySTGo2E27y_kw8B8ZB1eLvxZk1Cvm3BbHLMMvs3Y8pjBNy7_7_Z9P0MluvojO9Oh-GWNbBKsgee7jxbreCoevAMGCzrbGrMK7QEplc9HKKARfWWIq6MtYt2bZaxOvmHbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2689297ea.mp4?token=qTAnjWUCMrQptz33-smhWmqYzznjQk4WdiaZWpWtUw4Sb_elQXQ-DcP4tFCiy-5BABK9SeTQ8zDroY9RhLHAHmca2S7ZI8Z-h_Vsyc0g73O0ZE2JOtRreNAiX7p-qHQtGAAQqludBBWOaCeeW5QMd6cwfmsVQp87nW1SbXkSWmhV_IHoVbpX9mZhfO4FLdnakIW74O9mMcXBk0WB6JGkySTGo2E27y_kw8B8ZB1eLvxZk1Cvm3BbHLMMvs3Y8pjBNy7_7_Z9P0MluvojO9Oh-GWNbBKsgee7jxbreCoevAMGCzrbGrMK7QEplc9HKKARfWWIq6MtYt2bZaxOvmHbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با دیدن این ویدئو می‌توان تاثیر پیشرفت علم در سلامتی و کمک به انسان در بقا را درک کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681484" target="_blank">📅 20:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681483">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj7mbPkaCpIUYpki-WkcMQx4NByD2dSZL1NjA_GPGz8uTrCaN_Yrzyhc9MeTuXsGFcSAMeUDm1AfjWIVcWj0ii8dVnXwcJm9KqfmNtf_q-2bddR8cNbgXBSY33tGp8IDDiMcU5gXDkVDuWqy8uwR2nGXvPPkiVY1QHu1wV8m63R2JgnJ3TUeFa-Uy9GfajnE3FVz3pLFT9aTBnhpP0VCH_fHjj5DMq-SInlfn2ySNcpqhAmODXdwwCyG1VnRqhOUmTC70NTxi1hcevNCQmZI7Jw93wRvGDm28NepFHpKf-aFUq5TojDbzhMMlmbXNoSkOzVUMzz5-BqP-wrUjYSC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم مراکز داده از میزان مصرف برق جهان
🔸
مصرف برق دیتاسنترها در سال ۲۰۲۵ به ۴۸۵ تراوات‌ساعت رسید که معادل ۱.۵ درصد از کل برق جهان است.
🔸
پیش‌بینی می‌شود این میزان در سال ۲۰۳۰ به ۹۴۵ تراوات‌ساعت افزایش یابد و سهمی معدل ۳ درصدی از مصرف برق جهان را به خود اختصاص دهد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/681483" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681482">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سناتور آمریکایی: جنگ ایران غیرقانونی است؛ نباید حتی یک دلار دیگر برای آن هزینه شود
سناتور دموکرات آمریکایی:
🔹
جنگ آمریکا علیه ایران غیرقانونی است.
🔹
کنگره نباید حتی یک دلار دیگر برای این جنگ اختصاص دهد.
🔹
این جنگ محدودیت‌های قدرت ایالات متحده را آشکار کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681482" target="_blank">📅 20:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681481">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmniZKa5rYietQ7MRPglZRDGkNXEv6HYFEHW5HQaF2AFubdTaQRp9BekKdi5TfTApEzjsUZ7NajDgbv7SQN58mH9UCP875W92NykCjdGjN0MQuIbw-GqnaxQruO6UQyPJAe1uK7UkpHl70hy57xvJn7yEMAOUq0_VDjKjziSENke_Cx4Kox-5wXZFMWQ5T6uAOD_0-C2rHJGMaZ0WuLcOvi8iVtf2u173ip00RyKuUC7ySMwd_cDfPysmyPeMQ8aIPh-D_c37g56O1sqWxGU5Sx80-eJ2XpaEGDciHdesuvFcm-Xox6QQ5lWVr9iW4RxTe_8nATSa8Pd1cf5HKNMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم
🔹
رئیس جمهوری آمریکا با انتشار تصویری از خود و رهبر کره شمالی مدعی شد: من و کیم جونگ اون خیلی خوب با هم کنار می آییم!
🔹
با وجود نگاه غیردوستانه در این تصویر خاص، تصاویر زیادی وجود دارد که در آنها لبخند می‌زنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/681481" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681480">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9f8e13d8.mp4?token=O1PuZfRaUSPXDHTlKuDHMvvniYwd-EdOC6aUzNEbLO74qiDptfT2l4keuzNaPgodPIjzPqdF3l6R9YoOKtHmFfS278W2-qbGZydOnPAyMhwuqZ4CHe6ZKyBmcmgjVtpIAGRhQp81NtppxZhkdS69zrnr0oly2wZoHC1NSBmEBVaDmLEIlQvCdYGYK9d-RGkKqsPyuNXOO8ULc69vrtZa01Hs-po9-nnsNxmi5a1CN6vBbNYHtClQnM2OHGxDWHadXPPO5oFlSRsIWphfiZmjq07n2MeHVY_XY1tdXlHTuijMHWXyBwlIsrfJzUcUg_VU9tzpnoMbQ7NA_u1Deu0GYUq2u0xEsZbn6q6FEZ0wuwnzES9dEDfcJ0WZtFsLxRGSllGtdaRUhZyEyEgL4Fdabq_tYc11IKrbtGRaeVOukBfJ_EbnYBro6jZYCznQNAQo37VRxiEk9MnQGl9UiptoXgtPtEA-5dlvYYz2XOKlumeIyELffvrPwl2Z9hBKqf20aX4Esqpdyy8_-Ys_TVU_ubiBjVlJ7HCMtUqK7clhLQ3u6ywHaX5EcvRj9BF3ILD2ibx_5H-kYYp3_hF9KhdIh4JmKrV7UZ0My8NjjKsLyurVfotTPRFc04wDX7Jmosgdpe1NlROmNDzGsLIGdQKRcbHqjvyuDlwzfBDr7m-Ynew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9f8e13d8.mp4?token=O1PuZfRaUSPXDHTlKuDHMvvniYwd-EdOC6aUzNEbLO74qiDptfT2l4keuzNaPgodPIjzPqdF3l6R9YoOKtHmFfS278W2-qbGZydOnPAyMhwuqZ4CHe6ZKyBmcmgjVtpIAGRhQp81NtppxZhkdS69zrnr0oly2wZoHC1NSBmEBVaDmLEIlQvCdYGYK9d-RGkKqsPyuNXOO8ULc69vrtZa01Hs-po9-nnsNxmi5a1CN6vBbNYHtClQnM2OHGxDWHadXPPO5oFlSRsIWphfiZmjq07n2MeHVY_XY1tdXlHTuijMHWXyBwlIsrfJzUcUg_VU9tzpnoMbQ7NA_u1Deu0GYUq2u0xEsZbn6q6FEZ0wuwnzES9dEDfcJ0WZtFsLxRGSllGtdaRUhZyEyEgL4Fdabq_tYc11IKrbtGRaeVOukBfJ_EbnYBro6jZYCznQNAQo37VRxiEk9MnQGl9UiptoXgtPtEA-5dlvYYz2XOKlumeIyELffvrPwl2Z9hBKqf20aX4Esqpdyy8_-Ys_TVU_ubiBjVlJ7HCMtUqK7clhLQ3u6ywHaX5EcvRj9BF3ILD2ibx_5H-kYYp3_hF9KhdIh4JmKrV7UZ0My8NjjKsLyurVfotTPRFc04wDX7Jmosgdpe1NlROmNDzGsLIGdQKRcbHqjvyuDlwzfBDr7m-Ynew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا طلا می‌تواند به رشد تولید ناخالص داخلی (GDP) کمک کند؟
🔹
عبدالرضا عسگرخانی،هم بنیان گذار و مدیر عامل داریک (انبار هوشمند فلزات گرانبها) در نشست تخصصی با عنوان دارایی دیجیتال،فرصت سازی و فرصت سوزی در همایش چشم انداز اقتصاد ایران 1405، از نگاهی نوع به موضوع رشد شاخص GDP کشور با کمک تکمیل زنجیره ی ارزش خدمات، پرداخت.
🔹
خلاصه ای از این نشست را از زبان آقای عسگرخانی بخوانید:
« ما به این باور رسیدیم که رسالت‌مون فراتر از یک ابزار معامله‌ست؛ باید ارزش افزوده‌ی واقعی خلق شود، ارزشی که به رشد اقتصاد کشور هم کمک کند. و این اتفاق، تنها با تکمیل زنجیره ارزش امکان پذیر است.
🔹
با اطلاع داشتن از اینکه خرید طلا یک تصمیم استثناییست، چون سرمایه‌ی مردم حفظ می‌شود. اما نگاه ما به همین یک قدم ختم نمی‌شود؛ چون از منظر توسعه‌ای، صرفِ خرید طلا کافی نیست.
🔹
برای همین، انبار هوشمند فلزات گرانبها تحت عنوان داریک خلق کردیم؛ حلقه‌ای که زنجیره ارزش رو تکمیل می‌کند و تاثیر مستقیمی در صنعت کشور می گذارد. »
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681480" target="_blank">📅 20:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681479">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bafc011c98.mp4?token=ANDF6yUw99Six8yuRlBoHgPf6Y2XtCjv0ggeudMvoakdDGG3xDlbJGNNiQ223mgr2_UHYEq8ofbPFpZHjdhK5Bd_Dtl121PXQ6qpY1SlcfWUREMpYOVN-5yy7Vjh20kPZcdBZ80q_mLheVUXDJvoJwh_XNIZeUplLW-tUpQvCTP71JdliGs-gkJiyKawFlCCXs7bMrQDwMibffKheiOgIwscCIUVHLVwup3Jw0Q_E0-SCddsN_AxZRfziaQansP2BUkuXeGoYQoOxDx5tYcR5wg76hQHePfj87skucE4eOa4b0PZdmbUHtV8RCvnJ6GGVhz0J-m9UWJY0ZHpMsTyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bafc011c98.mp4?token=ANDF6yUw99Six8yuRlBoHgPf6Y2XtCjv0ggeudMvoakdDGG3xDlbJGNNiQ223mgr2_UHYEq8ofbPFpZHjdhK5Bd_Dtl121PXQ6qpY1SlcfWUREMpYOVN-5yy7Vjh20kPZcdBZ80q_mLheVUXDJvoJwh_XNIZeUplLW-tUpQvCTP71JdliGs-gkJiyKawFlCCXs7bMrQDwMibffKheiOgIwscCIUVHLVwup3Jw0Q_E0-SCddsN_AxZRfziaQansP2BUkuXeGoYQoOxDx5tYcR5wg76hQHePfj87skucE4eOa4b0PZdmbUHtV8RCvnJ6GGVhz0J-m9UWJY0ZHpMsTyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زعفران خوش‌رنگ و خوش‌عطر می‌خوای؟ این روش ساده، رنگ و عطر زعفران رو چند برابر بهتر آزاد می‌کنه
🌺
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681479" target="_blank">📅 20:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681478">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب‌رئیس مجلس اعلای شیعیان لبنان: دولت باید فوراً مذاکرات با اسرائیل را متوقف کند
🔹
حمله هواپیماهای اشغالگر اسرائیل به مرکز شهر خان‌یونس در جنوب نوار غزه
🔹
المسیره از حملات خمپاره‌ای مزدوران عربستان به چند روستا در استان تعز یمن خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681478" target="_blank">📅 20:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681475">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leRHJGB5J74Jq3xIPX-cfCSXHgYbw8-I3akzR6UxbZoNZIsNsYpdeQzc5ARPn08Gq8kKbneqfl7ezSGVMFQUkZ1cmMHaYSs_VAPGq4WtcuNmlcRilba_zdCBP3RK1eU0BPq1_d202G2DKqF74-JiXJ8IEFOM96-k0ckpf17khJnkexXPgfYTV4libwUdPijFh5TaeUPRB4C7Ux5Oz3F7DyvijrpoxkOnVPhqyXsG_hgeR8MqjE4GeVRwGxn55n4uo1qiX0qMGKfb5kc2EOpVFC8N7mb35ENfpMbSvXc75KB4DerrRXSKLP0XBfLaEY_DmbAP2UL35RO7RXL1e36c9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلوف پیروزی در اوج استیصال؟
🔹
ترامپ در حالی در اظهارات اخیر خود از تداوم فشار اقتصادی و کنترل اوضاع سخن گفته که تضاد این ادعاها با بن‌بست میدانی در هرمز، غیرقابل‌انکار است؛ واقعیتی که اِی‌بی‌سی نیوز به آن اشاره کرده و اندیشمندانی چون جان مرشایمر هم روی آن دست گذاشته و معتقدند کفه معادلات به نفع ایران سنگینی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/681475" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681474">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3a7791576.mp4?token=k48bHoQ5_SXnsiNkJ3wT2pOWHN2GMAe6VxPLsztsGfKwkMKEMLlN6R2AIauCUhb3sA5N8SO7BWK_gAr8N9eXJr-QewHo0TyRGgiggg_OMRgOY3u-aqOo8hFwy8izEHNXOIxDO8qmZS3Sc4uS2iowP-bd3PQRr4jJspU8O_TwsCJQr5O37pWk5f-QN1_qLUQYX7P-TuR1GmA8bTjD6P8vq-ljYk9qAOqImegyLlHP6GbVLWT6kaGmByjsys0KbtSwkC2UnGCbv2eyQIHhTMyvpHVhuiQ0QkvuQuU6elBwqMSv6xoUFtIpz5vcB-Ql0o0Fh-3HyvSVbVTw6QCMFOwrPzlUlwxzSOOsgzuKV3DOPEketFagM4ouu6epekgk75Fcw36ga8r_N_98KzYFMv3d7_-8lxvQVxE8kPB2tPikJnub8_IxZuyp-hf4hm1DyKDaSnEaNOlcif7VnbtYlaRaqjOArFkmpYcjqXOsS6LfuBJMdqr-xRSvZKO7Qkrf8PUGCCR0vE0HijVQAEB0yRixg30y3qdeYExQVBNHGxyrv0XtVjN60rQXEROd1VUGJ3GDE0zAQ0QGplcuyCP6NnSK0hSC69ehMnAezGAr5Qmytk0cJYZX2mSBxihufIFJelK6TrUnwusoozbmLIFw4u4mndTZ0m_ZygWNOY6NUcizC04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3a7791576.mp4?token=k48bHoQ5_SXnsiNkJ3wT2pOWHN2GMAe6VxPLsztsGfKwkMKEMLlN6R2AIauCUhb3sA5N8SO7BWK_gAr8N9eXJr-QewHo0TyRGgiggg_OMRgOY3u-aqOo8hFwy8izEHNXOIxDO8qmZS3Sc4uS2iowP-bd3PQRr4jJspU8O_TwsCJQr5O37pWk5f-QN1_qLUQYX7P-TuR1GmA8bTjD6P8vq-ljYk9qAOqImegyLlHP6GbVLWT6kaGmByjsys0KbtSwkC2UnGCbv2eyQIHhTMyvpHVhuiQ0QkvuQuU6elBwqMSv6xoUFtIpz5vcB-Ql0o0Fh-3HyvSVbVTw6QCMFOwrPzlUlwxzSOOsgzuKV3DOPEketFagM4ouu6epekgk75Fcw36ga8r_N_98KzYFMv3d7_-8lxvQVxE8kPB2tPikJnub8_IxZuyp-hf4hm1DyKDaSnEaNOlcif7VnbtYlaRaqjOArFkmpYcjqXOsS6LfuBJMdqr-xRSvZKO7Qkrf8PUGCCR0vE0HijVQAEB0yRixg30y3qdeYExQVBNHGxyrv0XtVjN60rQXEROd1VUGJ3GDE0zAQ0QGplcuyCP6NnSK0hSC69ehMnAezGAr5Qmytk0cJYZX2mSBxihufIFJelK6TrUnwusoozbmLIFw4u4mndTZ0m_ZygWNOY6NUcizC04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه آسای یک زن آلمانی در آتش‌سوزی ساختمان در طبقه یازدهم
🔹
زنی از طبقه یازدهم حین آتش‌سوزی در یک ساختمان بلند در برلین به داخل سبد آتش‌نشانی ‌پرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681474" target="_blank">📅 19:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681473">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8908695220.mp4?token=sZ_iMLpjQ0BEAQJt9ToPxX-c_UI_XA5loIGlI2Pu7ajgYhgJeGnGkZP7qLFbz2wCAcEnbXYPLUA-zoqBY_vrpjBcxJoqRjnjOeLcNgL_44CpVrg_gSbnVtJn5rHVjog1qqPmvt9JpHYkQO7aDvsBXWHyuoZ4EqthfPPkOw_ESN0JvbI41syYrxeTp51lsNAlLGNPFYg4OXwp9rN9EjKxn6UrwRxtIYZkbwaJYhXw4N7sBKCAede12rPWte6PaMY_okhh5BcE8YKy0RbBAksh-w7NOPFGW9TlIJ2HnAbCSW2aNl7N5H0LqtWL5nkxyIf2Asbm5Bl2mB8zYA0MB-CJEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8908695220.mp4?token=sZ_iMLpjQ0BEAQJt9ToPxX-c_UI_XA5loIGlI2Pu7ajgYhgJeGnGkZP7qLFbz2wCAcEnbXYPLUA-zoqBY_vrpjBcxJoqRjnjOeLcNgL_44CpVrg_gSbnVtJn5rHVjog1qqPmvt9JpHYkQO7aDvsBXWHyuoZ4EqthfPPkOw_ESN0JvbI41syYrxeTp51lsNAlLGNPFYg4OXwp9rN9EjKxn6UrwRxtIYZkbwaJYhXw4N7sBKCAede12rPWte6PaMY_okhh5BcE8YKy0RbBAksh-w7NOPFGW9TlIJ2HnAbCSW2aNl7N5H0LqtWL5nkxyIf2Asbm5Bl2mB8zYA0MB-CJEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به شمس آذر توسط عمری در دقیقه ۱۶
🔹
پرسپولیس ۲ - ۰ شمس آذر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/681473" target="_blank">📅 19:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سناتور آمریکایی: ترامپ درباره فناوری ناوهای هواپیمابر «هیچ چیز نمی‌داند»؛ بازگشت به سامانه‌های قدیمی می‌تواند میلیاردها دلار هزینه روی دست نیروی دریایی آمریکا بگذارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681471" target="_blank">📅 19:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOKWFht1fV5yo9N4WFoUtPngP9uu1i8FZh-ss0W8hyiJ9IA7ZIDBGi0RnEtNjYA-lPIL3Gn-SlNSUOKxwAzIJdAC_CRD6dOrUlwMGAiEIPTjvKZFvZvWB2wlV0uz6mjuwrtBEKRzL8jkMmOOC2np6Ydz36xfPWaNOhSCsQZNGVaXCiUD7y5bmEbUafYM7KmMfMCULyhMnoyxhCp_xSRNHGG6Q27SWTCixd6xSHT3BknvUKQZc09y2yhqC0Wa3NtHjVyXBHKK5wD0P6SEimY2k-fcEzj-Ddp9gLSEMZEiaOws2vMkqXmoKXiA-CAegJ6jh7vd0s35D8oy9-yjTo2Cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴میلیون نفر در سنین فعال ازدواج مجرد هستند
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از دلیل تجرد خود برایمان بگویید.
🔹
برای حفظ حریم خصوصی، صدای شما تغییر داده می‌شود و هویت‌تان به‌صورت ناشناس باقی می‌ماند.
🔸
روایت کوتاه شما می‌تواند بازتابی از تجربه‌های متفاوت مخاطبان در این زمینه باشد
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681470" target="_blank">📅 19:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-pPOZhsxihmD5322IaN7xiwRjwcTEcxzaMtSmY3Y2K7BeXv_DDa0TWi5thQyARzltdOsLbXe2lJl3SPOMHPIcLanrBhqqUejdZ0o8YUZbwU8suZ8rCtdUdrJC-YwpiYYbnIkQg5bdGNHdSnquWI4STT9AUA3-rHydHd2X3kucv7u2AflUJCB3ArjkN5ObUUhMepK4YsZkuHi7j4XVQBWGQYQjOl29Fb4FVQOTKYc4oJ1cxEWil_wjdJZewCXLc48dDNUMH9tyXTav6dRLNgZxJXjX8pDJnP7ElfdQvQ3oeDyEVKpx7oXo1QA_6B26a-_kijxZ1U8CtF6JH1JvZudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیس و دیس بازی پرسپولیس و استقلال در مورد استفاده از نماد شیر در کیت باشگاهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/681468" target="_blank">📅 19:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فایننشال‌تایمز: تبعات جنگ به گردشگری ترکیه و قبرس رسید؛ هتل‌ها مجبور به کاهش قیمت شدند
🔹
فایننشال‌تایمز گزارش داد نگرانی مسافران از ادامه جنگ در منطقه، تقاضا برای سفر به ترکیه و قبرس را کاهش داده و برخی اقامتگاه‌های ساحلی را به ارائه تخفیف واداشته است. طبق این گزارش، قیمت اقامت در آنتالیا حدود ۵ درصد و در مناطق گردشگری استان موغلا تا ۸ درصد کاهش یافته و رزرو تابستانی ترکیه در یکی از آژانس‌های بزرگ بریتانیایی همچنان ۱۳ درصد کمتر از سال گذشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/681467" target="_blank">📅 19:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
‏بغداد: انحصار سلاح شامل حشد الشعبی نمی‌شود؛ هدف، گروه‌های خارج از ساختار رسمی است
دولت عراق:
🔹
انحصار سلاح در دست دولت، شامل حشد الشعبی نمی‌شود؛ بلکه گروه‌ها و طرف‌هایی را در بر می‌گیرد که خارج از ساختار رسمی نهاد‌های امنیتی فعالیت می‌کنند.
🔹
حشد الشعبی بخشی از نیروهای مسلح رسمی این کشور است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/681466" target="_blank">📅 19:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYgMPRNVflzx1eqdq9GsL9LU-PcTzSVJZbc_v-gAqKooz-JgOXreNXja4OfMaCGA6rOLsgaccTMmSpRj-7mbyJEJnHChhxXJNAPUqXWdcJOQoofane3lUAXV4RG-3Kl_d6vSG6SyjVY0jqp5Qs0i2Bf_e_KPgAFsJVxqVodXy-NFY-92dMQxADrdHqrc6WKRrwm2jjgWmy9tNxVN4E6sQE6mzr-VsRXaaMi7zaeWSpI9S_W88uYbLvDocYBKUUCUML0zqkMVuexTnkb3hLb2_JmPJTWJHLVZBTPPysc3z96aR83TLYDR5Fn6HPXqkSmLFodobP-jr4ZyO5EokHR7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQIQpexUqvaYb9l7QwhPDviX06deBImfkH9KChCbxQsUBI8apUYL2SmBTk0P5tiStCCEoeea_oqRfheAzRBcdFX3_h_R4fAXJm-vSArt2F8fcp1iPrsLXcq883LuYm_bC6ijif0SLqQLlHpt_ttYTZsNh1NEaJV5db8rwcymMAI-c0lUX39G21XJRe1JuKwiSB3w9mnuAWx7fwRWMuHALIljlsuuOi3zt8LKXcl0ueNAhPaWZXfBgkCQOJpVpfHylVNi-5dN0y_CsYiic_ExilbDrPT2wOoIuNWKwuom3lF09bEVX4wthdpPHWwDK3rjKv-Xk0qr_DTIRP45adkPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELg2PdhhowxqpWLagK4RSSwY3GkrciLlao8j5CutoGjFa0wagcWjhbKV42T4IYuH_rk1cu54JvzIZdt4RCGKvANFTqhcyy9cKCdQLIMIXXDeo-v5_-m2ANkcVQNijH-iZ7bWpaAQO2r8c2EQIfts5lG5_CtE7IRrw4fx1ggQLro96lGkuvreqrpvgZbY5XwpmzhmyX1E00-U_JYl0-RKszxsa1zZu9saORu1-xMzWtzZfZC3EuXZqBxUV1RRr-89G1uug6auqvvzfNdvOMiw2_tb3_w3l5ZwxtgYahB0PfVqL1kyWPK8xLAay3u2nOLjvusyZfjI_afYbMl86JhJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hp2KMbQJ5NFpExkLb8GrKMPQSX02bq8pqJvOLYWw2T6PU9vOn9iA4NYhR-9Bcz4HepPUMF6C4lfNCAOoFMGC9FmvSexy-TGfsaUhGz88jdZoi6NoxwUIgo83SrwfGEXnUeWH8MoBRx5LEItN-BgZISNuKmmIed6cNU6PWIvhdleCnZXH1kd3PCjgZVcqhYp56YE2igTZVapwtqVc98cQK6NrYHQsts-hghUYQLIATJNhhGtRV2VH8hbi4exxfhoRXlp4UJi7gsSRQAC4HLKT-SRi-e-HsQuky6zeytEmP2nrH4zHUx2u583RG5T4f-tOBf1pZF2iudzHAs1g5Lyqkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر بخش از یخچال برای کدوم مواد غذایی مناسبه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/681462" target="_blank">📅 19:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
وزارت نیرو: بار شبکه برق در روز‌های آینده به علت افزایش دما افزایش پیدا خواهد کرد/ مردم رعایت کنند.
🔹
نسخۀ الکترونیکی کتاب‌های درسی جدید منتشر شد.
🔹
شهادت ۱۱ غیر نظامی در حملات اسرائیل به جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/681461" target="_blank">📅 19:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQX6YcZekz1Q8y-4_el3OZ9jrs7bWfi23rNEzJ2clLtEsHmSeyAVBo22qj3n4cqHvrtgqukI03-VZeiuTjtrzhZcYpubwaqd4a1i5pamRvVokUZaB9Mm9GajvZ3pddy1VgheisuJcMa8phOae_cnJQ--YHHSh_4WqgoB7O_DTY_fMvMSPgQz4GN-KnSOEHb5DjaBGxFZyqBWQQvwBKrdrkpPCRAozXaf2ZgBmQOI7B8Z6g_tJkBMVank-S0SPzi57ixUJ6e7IZ6DS-rIsyKgfQK-Qp8UfUFJCA6MyHYQh9zs08BzwffG0qrQ8Py0dUPP-XpNbSeEC0Po0mNtBREatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت‌های تازه از جنگ رمضان در فصل دوم «سرو، سپید، سرخ»
🔹
فصل دوم مجموعه نمایشی «سرو، سپید، سرخ» به تهیه‌کنندگی محمدرضا شفاه، محمدجواد موحد و آرش زینال‌خیری با ساختاری اپیزودیک، سراغ روایت‌های انسانی و کمتر دیده‌شده از جنگ رمضان رفته است.
🔹
در این فصل کارگردانانی چون حسین مهکام، دانش اقباشاوی، مریم اسمی‌خانی، امیر داسارگر، علیرضا صمدی، محسن بهاری، سیدمحمدرضا خردمندان، امیر ابیلی، علی طاهرفر و حمزه علیرضایی پشت دوربین رفته‌اند تا هر کدام با نگاه و زبان خود و در قالب داستان‌های مستقل، بخشی از روزهای جنگ رمضان را به تصویر بکشند.
🔹
این مجموعه محصول مشترک سازمان هنری رسانه‌ای اوج، سیمافیلم و مؤسسه فرهنگی هنری اندیشه شهید آوینی است.
🔹
«سرو، سپید، سرخ» از یکشنبه ۲۵ مرداد ماه
ر
وزهای فرد، ساعت ۲۲ روی آنتن شبکه یک سیما می‌رود.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/681460" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT5PHl0I3ZEvCODWuPm10OlenbGTD91fX_0hyd3FQ98Acb57PEwr-seTC6heK0GcngJ1JpkJV-GJJw9Z0sk-tQBSF-CV-Q9hWuKuaB71_sY0tI5UIaFnbiftHZT1w7yb6LlvLE-GgjeCa3dtG2NmEHrjOOFFzf0Up0kk-4YyfH7ObXm5ePveE4AFHkkiSLdC3Iocm6tQd4EwBCxXBEsi_iOhHze_wsiNeJdev-glHEze8ygXeB5hmSIihd7M3O9DUTwqdsjirB5I33aT4cD812BHdg7ryk2GJ6glNV3bbZ7kYx2eWgGd5mfJBoffBSkJqECuN56wd1DeUgwBXIP9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: برخی از روحانیون ترجیح می‌دهند اسلام را فدای خودشان کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/681459" target="_blank">📅 18:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681458">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469a082088.mp4?token=cIF_DGc-t6Yw57Hdc1MUq8RWH-lmJ4FZ5lh8g3oomUKuC8DD7xV_mx11ea7VTgwx4aHn1LejA7zZfV4oBnSrS0KHvDpk1ZA-eTWN_pdacSlwjhrwg-NiBa86fbvSBL8fYre4t7XK6tCol5YQ0JTQlP97E1O0N5SGvTsvo8yk1sdfyF7LIlzEvoZvcM4ISDyZxzPRgYWttLA7XP2XeZANW5TcL1ly_3aiwp3YNINK8ttxADnvvndAvB8lEeqwGtcCCXBSdrRS2MeNEOdQ4-I10g3hmQB_ldSh1PNNb6HdwDMEYWblCAU6K_qoaypnfrW8ffw5VTcElo-13xILxC4Xxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469a082088.mp4?token=cIF_DGc-t6Yw57Hdc1MUq8RWH-lmJ4FZ5lh8g3oomUKuC8DD7xV_mx11ea7VTgwx4aHn1LejA7zZfV4oBnSrS0KHvDpk1ZA-eTWN_pdacSlwjhrwg-NiBa86fbvSBL8fYre4t7XK6tCol5YQ0JTQlP97E1O0N5SGvTsvo8yk1sdfyF7LIlzEvoZvcM4ISDyZxzPRgYWttLA7XP2XeZANW5TcL1ly_3aiwp3YNINK8ttxADnvvndAvB8lEeqwGtcCCXBSdrRS2MeNEOdQ4-I10g3hmQB_ldSh1PNNb6HdwDMEYWblCAU6K_qoaypnfrW8ffw5VTcElo-13xILxC4Xxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اذعان پنتاگون به انهدام ۲۴ پهپاد MQ-9 در جنگ
کارشناس پدافند هوایی سپاه:
🔹
طبق گزارش پنتاگون، ۲۴ پهپاد ۳۰ میلیون دلاری MQ-9 در جنگ هدف قرار گرفتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/681458" target="_blank">📅 18:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/681455" target="_blank">📅 18:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681454">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19612db87.mp4?token=FIUvy51RbNPwemuFtk5t-XJp3977moitVDT9eLQ-PZN3qZ4bjzk_My_SXTkWtakUfCnjiIDx3mh7cihVAQZYA3YAZ_i4Z08xoISNjRBOjFk-YoW9lE9Et77v8mNuQ2Gkl5qd4TXVQdGX-Ksv8IfEUrH-DzG4iktH0-n2V6fyk2jYJwXnQnx5nQyWwdYZKc-efg3ynPKYAwnguRb2A9mE5uwLXthjOlAQZKScne1OQrt0eOxnSoZqSEGk5O32OiO3FH8hjpXSBg7YRSK4kRMXvlLK6yrMo4Y2-Rfo5HoB-TuPytRJIFMdZB3GL-S2-4o_n7r7mqMEcbmNNUNhwnLW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19612db87.mp4?token=FIUvy51RbNPwemuFtk5t-XJp3977moitVDT9eLQ-PZN3qZ4bjzk_My_SXTkWtakUfCnjiIDx3mh7cihVAQZYA3YAZ_i4Z08xoISNjRBOjFk-YoW9lE9Et77v8mNuQ2Gkl5qd4TXVQdGX-Ksv8IfEUrH-DzG4iktH0-n2V6fyk2jYJwXnQnx5nQyWwdYZKc-efg3ynPKYAwnguRb2A9mE5uwLXthjOlAQZKScne1OQrt0eOxnSoZqSEGk5O32OiO3FH8hjpXSBg7YRSK4kRMXvlLK6yrMo4Y2-Rfo5HoB-TuPytRJIFMdZB3GL-S2-4o_n7r7mqMEcbmNNUNhwnLW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور شبانۀ پلنگ نر در منطقۀ شکارممنوع کوه سفید دماوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/681454" target="_blank">📅 18:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681453">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استانداری تهران: منتظر اعلام رسمی پایان جنگ از سوی شورای عالی امنیت ملی هستیم تا فرآیند دو ماهه انتخابات شورا‌ها آغاز شود.
🔹
مورفی، سناتور آمریکایی: جنگ با ایران از اول قابل پیروزی نبود، ترامپ فاجعه آفرید.
🔹
اردوغان: بسته بودن تنگه هرمز به نفع هیچکس نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681453" target="_blank">📅 18:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681448">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYte3zEUdyRmgHRTQo0AIAUbv7PmYOEOxOgNbYIqx6OztmtOrvpmydyMDjMHnrzfZN_EwTAt236h_Zpcq_vme6V8mBL1z9dRXBpmq0hQLqe7KMW87dUmyxaXb4gMMv7ICe_SLewMKSSQqDsbU78Oz68GBqvmsWM_8U6JqierkI733Utsj8_AVbjDFtyoKrmuc5Iqe1aAhwVGf7LQVLZVO7FeumnzOEpeonrEPkWCCx4PkUbVAp8kB7br9PFeltoRT6jLNuPlNLSc_hl6MX3v-ohwOcEtty9f48LlX0ULeR-Gmfy7juvOBc8Mpxq5QLWwQ4wgJUFzncMRxcj7OxcG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJtWWUuQg1Ikh3mtIRTVI9Qg4k8cEoR46vMHxTSsJMaQ4xkZNSZcCHZsa0XuQxjo3MC-nlCMC--fuRvJs44AiJT-Js7D2jMaiBXPFtgmggC4caMkIywN2wbPO0lMIYsK7ABX-LF0xntooVMNDsJCZyrxvBD-pPGXXEoxUlA2_wYaCExoGu2m2j5MJjxhs6GHqD_m6ZU0XvRe4UmCQxKjnSSjqWo7HtcWtf-AIHWuJwcxQQ913WiM4zM10UL8Czj5pNxJX2Ehp8xJ5WOMaW56lSlB3vSpaOG_XHRcSHrU8t70-QAfkL6mrD8a4xGAL2NN9lwXogKc2ll1AFVCmTDGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SahPDlO33Uu6co0Gx4nWWcA7SAYM4BDJHwaP08tSUlC-jA3IuSy-UQkVhUTwbXFXpsGkeZRU0LurWZ5RoWI5rD95XcifDAlhQZ6lM1AKvRJCruGjn-EPYQFMENRmE3VdEc3kt84zP4S6MsmdNLyolJmfXZWBdqfbMB-Q_nqDfKcMnmK7d6j3lu0Ndwz32kbPBbMaHGULvAE6inPmlsdIAtXzmDcDjIUG1JGvehd1cbfk_san21_FOUZs-F4EM80pI5IydsvdwCGXI135KqCBElj7U0CWeqs_Wz8gOnz3DtQhfTfVeK1_wNCMExQSXC_NDnLfstW2yazo_8wWUA1Q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IM4z83PmkIgghFa1CKXCZPTFGHHtqQ0ZB59TQrq0RsmmAia_FtqavJGbA9DY3qG-Zo53QmCNbAZSvkB-EWVqV7-Oa2ixhR0aKgoK7saafQuk1jyYBFhYWGmkk3dWADWb1z8Yd7HmEOKwzcL2URMX0OTbQTKopYvVgFzxFho8fxJs1nn1sLQhSwzxWO5KdDYZu4IOoNDSIQxXbq3eflGRbbkjpbJPZNoaRWTSuWRw4949KQe-syCUvF8zkW40veAnHdkoHN-QFOLLJwHn0nhTqGXiZL6EOZ7HG1hPBXaxPnje_Ca4e1eh9ZfUCsNkQaR1dYDjKWUyf499tmjNsmDQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEZq5fVbMdKZ6Wmv8XspxJRAhln5yzU6UBXsWLZO2TyDUxn_6yS02_n1ej-Q-xSSGc-9cuDmTz7Avmwn-SfnDYHbgbv1aWgy71tTzapRiaEqYSRQZtDOUc5GypkvJbq8E1m97xfuQrDGrkZmvsWt0EVz6Ipk6rKbihWvs__vD1wrpmXir_cNU-XiBX0TFBzbQORup7HmUJjsZ5864Xb2vZ716WLeL91QL6BkmAdnoGpW14_A2Gx6ebNXhrCBiM88qwonmObjzCcWnCnkmipiPNlMr_8CQsgnpJgCFt8fPzewWRsSgcJ9gWTVQkOrZ773fJ23HE5HjCZaXKB1EptnBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر متفاوت رویترز از خورشیدگرفتگی در اروپا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/681448" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681447">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFziUu_Nqv4uIE19d7zhV5gRMXw-imzUoYlymPv1nVU9_1x8saEa4-UFxDUZpgBfUvrPGQnCvX7f-eNr0mfLyEEc2WHgGdOWlFyzcA4Me_gAI9md3in-xk0cVT1jC6yI5dllGX4uEHaXjt-4uRkLQkz4svCCuGSGBNbPH8BB3hRZj5NQ4GjUjwKhuEO4EsVOV6PwrfGhQXYDsclb9aEojd9THECdjQqr5LNkJd32C4MUXLIvEjS4EAvMwHyZGhCfsKJNPOM4w83pDfut4Wb8zD0LClI-PxgnI29P8OWmicmTey9J4WOlLNP_lAmXm_66ZjLobDfs3oFj2hX_80Wqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری جلسه سران قوا به میزبانی رئیس‌جمهور
🔹
در این نشست سران قوا ضمن بررسی آخرین مسائل و موضوعات روز کشور، درباره مهم‌ترین مسائل و اولویت‌های جاری در حوزه‌های مختلف بحث و تبادل نظر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/681447" target="_blank">📅 18:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681446">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
گاردین: انتقال مخفیانه ترامپ نشان‌دهنده نگرانی جدی واشنگتن از تهدید ادعایی ایران است
🔹
گاردین گزارش داد مقام‌های آمریکایی در اقدامی کم‌سابقه، ترامپ را در جریان سفر به ترکیه به‌طور مخفیانه از هواپیمای ریاست‌جمهوری خارج و با یک خودروی خدماتی منتقل کردند؛ اقدامی که به نوشته این رسانه، شدت نگرانی واشنگتن از تهدیدهای منتسب به ایران را نشان می‌دهد. با این حال، گاردین یادآور شده که مقام‌های آمریکایی تاکنون از کشف حمله‌ای در خاک آمریکا که مستقیماً به نهادهای امنیتی ایران مرتبط باشد، خبر نداده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/681446" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681445">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC02MBL9zlkh6fWZj6TnUYfI8mdKPKhuFiZ0facf03wUReJIpC12pAAZuXJCkWTt3gWfsI71pd5ss8JulSNB41-PIDC2Yl-gAJ9fPdxYbCrRn0ShY4Yk-MvJmBEGVzL_GVSRUmbAoabnSbSgce9tMyS1bd9yb0fiM0AyQnoMO_LIhiKY0gsLKRVDwyN54ClrKNu7-CqurchmVxY8DxLEBEWXYeTVNjCgbK4SLrGLTOh7KUlkkSDsYM9FZQXOmpaOswe38HHKxw53Sn-i-Ako5_m8JNOE-F4H4ax9dx_6gCVZn7Hz_Yfjipg53chTWOcES84yRYGLuiKmSBYYn19Iqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روندا؛ نگین درخشان اسپانیا که جسورانه بر لبه‌ یک دره ۱۲۰ متری ایستاده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/681445" target="_blank">📅 18:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681444">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDeg6GGuEuXhpX_E-jkosvYlfjYzz8U_ID30aFjyeB-065LxXc8D-vvOyjZWOqCj1pW75Rx0mlne7nNrU1Ska--8wOFs_wMxGKzquhfPzxZdq7ma2MWUwV05NafvMDuVtyBmdjVcgVrC78T9t25EwSxe5U-X823kPXO0LvLkqh47SIOJRIBdR_qDp5oGp69RUVvSKAKGr3_FOzG9hXlqbsAQZH4TU5sza2PMZf7OVp9_Z00OKzemXgVMikkb8pDV2Gqv3D8kibs5kfQQQ8ANspksuLmlXnHfePaAgSKi5ePU3h0y0mjOPz0EvBvemOWjDnVW3e6N3XgmolNaQ9E0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندی که نامش با جبر، الگوریتم و پیشرفت علم درآمیخته است؛ خوارزمی
🔹
محمد بن موسی خوارزمی، از بزرگ‌ترین دانشمندان ایرانی، تنها یک ریاضی‌دان نبود؛ او از چهره‌های تأثیرگذار در ریاضیات، نجوم و جغرافیا بود. آثار خوارزمی نقش مهمی در گسترش علم جبر داشت و واژه…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/681444" target="_blank">📅 18:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6tQEtSk_8bhXPRjC1WksVHYeuHrfgQsipA9HjjKwyvQR0yvR1XY7SLC7ZkEBkcfp7cZND8oL245fVy_yjWxnZASKO9z6BzZf-4kS-W8Jd47H6lvSI8ja9OVZ9MYqBg8erW-W5i9dlG72Yaicz7hWwYXbxhMEW6Xmnw22Kw8BjIVHTf_sy5_-CIlV5nzcW9al4jmabl79it8OV6FnitwyAMG8OWTZf8SGGaUJKA_GCGFaRyyXVrRrepySYCXLxl0x1nCx33mK0DLyzBV5nYhD6VD5oXC5AP5kg7sV_fuchT1m69NQJDB6YwapV98RVJReOT7RhJ38q0q7-CAIeYBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-SsE3EK_frSKLgopMG2VdZ4Rq76IZzF0ed0RQHdBJx-0ChOt6Ch2FuvSfkpqQNOAIJZ0BLPgdhMvYlQ6zJlAsUfYXtMK6hci_1wIMLkLnjKLGAHmOIhRb1cVQEo756DARp3274n_-2_BqDRdVQ-lx4cQOosqTlpavvfGI27O9ERHs1IPdsndSruGiNcV2XSh5fQUn8HA6pKbaamNlLWeNnz7By9G6zw7g58q_Fb2CVeG9h-HhC6ct1UT62zCY49mhfAP6UbLAXqcEHUCodJNaJ25xSDmqJLDZXiHFdZovyeJPnHO_4cSch289mtQ1Sv9O9wYLJtpN8JibFPZF5CMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آدیداس و دیزنی کتونی راپونزل طراحی کردند؛ سه‌خط‌ها پرنسسی شدند!
👟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/681442" target="_blank">📅 18:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بوی تعفن راز جنایتی را فاش کرد
بازپرس ویژه قتل شعبه یک دادسرای امور جنایی تهران:
🔹
مدتی پیش بوی تعفن در یک مجتمع مسکونی در محله نواب ، راز قتل زنی ۳۸ ساله را پس از چند ماه فاش کرد؛ جسد این زن داخل پتو پیچیده شده بود و آثار ضربات چاقو و خفگی روی آن مشاهده شد.
🔹
قاتل پس از شناسایی توسط پلیس آگاهی دستگیر و به قتل اعتراف کرد.
🔹
قاتل ۴۰ ساله:باهم زندگی می‌کردیم‌. بیماری اعصاب و روان داشت و چندبار خودم و خانواده‌ام‌ را تهدید کرده بود؛ عصبانی شدم و خفه‌اش کردم؛ جنازه را لای پتو پیچیدم و تا صبح کنارش ماندم.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/681441" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoyHmQ9DHh-aTQZAUnhTuU7YcWHxik4PSLGHmnTqkNOCpc3MIfydrJ86QKyF7ptQ-XcF_XVFblONC-F6eA9uMraXedkcOYgJvUE5N9EdDY47LGRBGK7L1puRSfvdsuMcsp8XmXQNKG-ycBpsBLsJIeS9JJMNODqSNtwoi_7-EvKevzIGXBpq36cCyRUwbl4nxUAwXzQ9Y7H16XV1RopxbIbCo1jWnINeAt60N6fci9hY1f6TPogEXLUNQFZFlgh_W6VsMMTDbemhFyo8eUNgNTb3N6gHILl5Uz5lt-O8oz69-id0jJHpGapsvARAy8YbPscStWx42LN0NJms_ho0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر خطر کرد
🔹
ستاد کل نیروهای مسلح امروز اعلام کرد که ۳ خلبان ایرانی پس از سقوط سوخو-۲۴ در حملات اسفندماه، ۶ ماه است در اسارت نیروهای قطری هستند و اجازه تماس با خانواده را ندارند. اعلام این خبر با واکنش‌های تند و تیزی همراه بوده است. مسئولان ایرانی باید با لحنی صریح و قاطع، خواستار آزادی فوری این افراد و فراهم‌شدن امکان تماس آنان با خانواده‌ها و نمایندگان ایران شوند. دوحه باید بداند که ادامه بازداشت بدون توضیح روشن و دسترسی قانونی، تبعات جدی سیاسی و دیپلماتیک برای روابط دو کشور خواهد داشت. قطر نباید جایگاه خود را به‌عنوان میانجی منطقه‌ای با چنین رفتاری خدشه‌دار کند. اکنون زمان اقدام است؛ خلبانان ایرانی باید فوراً آزاد شوند، در غیر این صورت ایران حق خود را برای اتخاذ اقدامات متناسب و قانونی محفوظ بداند.
🔹
هشتصدوسی‌‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/681440" target="_blank">📅 17:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09430cfdc.mp4?token=C8kZYnsF_S-spDD_vd53-5OAfHexYO5X3NRyq35UEbgugVnvJ_rNnoBgj7c_d1nYZKdewe3-TcdQaJTiykrinvJVL0zvKpmmtY-4o8Xw9gN30yCbxU3JceYYhpr5KZmtjS_48oqqox6m1HOp2EFdei9tCkdVdQBrCOk_WDbs9BkdNs6NObEMJHeNZoiSzuGQOQ8cL-OIvNuCsMnB-Fa4mHOmHK5o3HPDaJZcQsdCMBml0GtsW_Kn04MsaLu-_lFxNuk2WebqmJ5l1tkgCqb6oh62EYzw81vOUO_orsCNnB3xqu0BfV2WekScunaSrBG-uJa1RlRKXAmtHAXBgI-1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09430cfdc.mp4?token=C8kZYnsF_S-spDD_vd53-5OAfHexYO5X3NRyq35UEbgugVnvJ_rNnoBgj7c_d1nYZKdewe3-TcdQaJTiykrinvJVL0zvKpmmtY-4o8Xw9gN30yCbxU3JceYYhpr5KZmtjS_48oqqox6m1HOp2EFdei9tCkdVdQBrCOk_WDbs9BkdNs6NObEMJHeNZoiSzuGQOQ8cL-OIvNuCsMnB-Fa4mHOmHK5o3HPDaJZcQsdCMBml0GtsW_Kn04MsaLu-_lFxNuk2WebqmJ5l1tkgCqb6oh62EYzw81vOUO_orsCNnB3xqu0BfV2WekScunaSrBG-uJa1RlRKXAmtHAXBgI-1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو تله مالی پنهان که هر روز تو رو فقیر تر میکنه! #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/681439" target="_blank">📅 17:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
اسکن مغزی؛ سگ‌ها احساسات چهره انسان را تشخیص می‌دهند
🦮
🔹
پژوهشگران دانشگاه وین دریافتند مغز سگ‌ها می‌تواند احساسات مختلف چهره انسان، از جمله ترس، خشم و غم را از یکدیگر تشخیص دهد؛ چهره‌های شاد نیز مرکز پاداش مغز سگ‌ها را فعال می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681438" target="_blank">📅 17:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681437">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آمریکا هزینه جنگ را از طریق متحدان عربی خود جبران می‌کند
جلالی‌زاده، فعال سیاسی اصلاح‌طلب:
🔹
ایران بیشترین آسیب را از چرخه جنگ، آتش‌بس و مذاکره دیده است. صادرات و واردات ایران دچار آسیب شده و آمریکا به هر صورت با هم‌پیمانی با کشورهای عربی، زیان خود را جبران می‌کند.
🔹
مسئولان کشور برای پایان دادن به این زیان، باید اهرم مذاکره را جدی بگیرند./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681437" target="_blank">📅 17:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681436">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIvSF91aoxRvFSI2W30AfieA1oin4sQgGtQdQ4UOhorJMcPUW6owQh8FXEYQDsnkAAPQTszO-R6B9i1KQ5OdXlrN60QmUzRzmfMNJMmYkv_69XM4PCqimu0K_zBKrsj5gtMVuAAJ9yDyhEkDQlaiDodJUhnkhM5y357OAWb7FAObsJ9ufRuize4YS3uFilUUoZItborX8sf1Ul-Sy_1ekHPABJJlkP1t4m3SwDdgbaySwaYPSAfZOOu6zdj1xhoDEV6rphfHnDL2KwBjklTOazlgp_NePuDWopOF9-SvdfcH4CiIvJk-_OsBJ7URxleLml22_tozjzAzoMmLcV-FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/681436" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681435">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c55eef2cd.mp4?token=oQudpL3LORKYmgeXuUDfAi1xoig9Oib-31kMcwwvYNjw76O1PL0jCFPOyBqX_taze2QyjPkhEadkEjwMdIOY8Bj7eY3rzQbPbFXw4rZcL6Y_jeCGmImI8w4rYcBcy2gWqlfrowyxVhCT9DVo1QBulN_ALlPR_UINzfdju2qB7Xg-oG7w6TW-R0keWqfitugGA53X6MKig9OhX2fIfnubl53k0JCcULT1VgDy1BIARa-apHwVHWPnaL2--jRPo2W8u3hwZGYLIAGf_TjNHtF9RJU2ERIImNiRk5ge7UVS_NIiFfj4FAhv9Ka6xtezJ_KMaAEGtyecXILTV2L4r_JRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c55eef2cd.mp4?token=oQudpL3LORKYmgeXuUDfAi1xoig9Oib-31kMcwwvYNjw76O1PL0jCFPOyBqX_taze2QyjPkhEadkEjwMdIOY8Bj7eY3rzQbPbFXw4rZcL6Y_jeCGmImI8w4rYcBcy2gWqlfrowyxVhCT9DVo1QBulN_ALlPR_UINzfdju2qB7Xg-oG7w6TW-R0keWqfitugGA53X6MKig9OhX2fIfnubl53k0JCcULT1VgDy1BIARa-apHwVHWPnaL2--jRPo2W8u3hwZGYLIAGf_TjNHtF9RJU2ERIImNiRk5ge7UVS_NIiFfj4FAhv9Ka6xtezJ_KMaAEGtyecXILTV2L4r_JRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین مدعی حمله به رقیب روسی استارلینک
🔹
کی‌یف مدعی شد موشک‌های «فلامینگو» یک مرکز موشکی روسیه مرتبط با شبکه اینترنت ماهواره‌ای رقیب استارلینک را هدف قرار داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681435" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681433">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deedd68fa3.mp4?token=VQbsrc9_rhixmir8KDEblXLFIXFJG09PUVg8pFsmXD5kbKFhtEvSGDKWlbBj7OHVXJMOtoDw-4lp0eLD9JTPCyLESh_22qBom4VKpG-soSAiYqaGh9TxlkrTIjjMCHOI9Z646vGiBnUMMPqC00UCBtdbeFQcMeV4g0uvgZf2TALLyzQjirVG9T1LDhKH3iJPelsqAsfSZ4esHS0-pyTfwTRGmNlieVVTphzeO7p7Ewuy9dzPMPTxbq9jvc0i8MIlOfTsIrD3zGXi1TiJIV7_yCy6DudXr2OL1qXmrqGwKuqErGQ2TQxNklMeKk6fUEGK5JCx3Ke7_1SD5KFFVNoYYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deedd68fa3.mp4?token=VQbsrc9_rhixmir8KDEblXLFIXFJG09PUVg8pFsmXD5kbKFhtEvSGDKWlbBj7OHVXJMOtoDw-4lp0eLD9JTPCyLESh_22qBom4VKpG-soSAiYqaGh9TxlkrTIjjMCHOI9Z646vGiBnUMMPqC00UCBtdbeFQcMeV4g0uvgZf2TALLyzQjirVG9T1LDhKH3iJPelsqAsfSZ4esHS0-pyTfwTRGmNlieVVTphzeO7p7Ewuy9dzPMPTxbq9jvc0i8MIlOfTsIrD3zGXi1TiJIV7_yCy6DudXr2OL1qXmrqGwKuqErGQ2TQxNklMeKk6fUEGK5JCx3Ke7_1SD5KFFVNoYYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار نیست هر چیزی که در اینستاگرام ترند شد، تبدیل بشه به معیار زیبایی ما!
🔹
این روزها بعضی دخترها از سن خیلی کم سراغ عمل‌های زیبایی میرن؛ چون مدام با صورت‌های فیلترشده و استانداردهای غیرواقعی مقایسه می‌شن.
🔹
شاید بد نباشه گاهی به جای پرسیدن «چی رو توی صورتم…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/681433" target="_blank">📅 17:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681432">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEyOXclgbvIKqU47mcNnAZp0rnrPLSYgJtkftL0K0gaeVTZPcODnCaz3IeDpDbb2XnIOkF6_wsSnMR8DIve_AAYdH9l23KhAvyA9yADeITrgtS0kjydKfDeJnnAUQGBA2OiueLQeOOm--AHvBBBhycSe-HXwR0VLkwUR21BZtCQzll7LRNg-cyuf9HySmTGGWKhh-Ji9FaK5VcBfUuQ7HvZCxGXUtGuWt3zD9EgLkYhb7U7UM_h-bixVr2-yUuIqqytvaUdKiXdjobta1kh8OZGqw230aY52NQ9UmAb5jyj_0VwDIwspQ91mz8fH-T3s_UFbJqNv9TIlTqOfaHberw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترنج ۱۰۰ همتی شد...
🟢
دارایی تحت مدیریت ترنج از مرز ۱۰۰ هزار میلیارد تومان عبور کرد. نقطه‌ای مهم در مسیری که با اعتماد آغاز شده و با مسئولیت ادامه پیدا می‌کند.
🟢
برای ما، بزرگ‌تر شدن یعنی مسئولیت بیشتر؛ برای تصمیم‌های دقیق‌تر، مدیریت حرفه‌ای‌تر و خلق ارزش پایدارتر.
🔵
ترنج؛ ۱۰۰ همت اعتماد
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/681432" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681431">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU64dRK9SnBqLXsnRsmjzvASJdzUEFUEz_CC0kUKSxts3oJ6v0IznC3UhzIEI-qdd8J1Xp8Ko6gGMxXKBT9hkXn-HNMSIxisa7bv9s9auHyMLA1CC6bJBgI5XCwuq3SxpoQjmvI7ZyAzsg2MOakxhTnCXoTn8IYwxvnPfJkhAsvaP68eaCBC96fKElc_-t-3J51J8aOntBFXMZVbxSn8hmcBHh8At0L2EaW_mEMAlryiUhY6PKzrEGci1oq21cSZwbuV0q1M7ebSKr40i9INzWfajeJswuXopdy4qN_Y3tvzGcSnAA4CgpU5grKby3N3U2XNMUChHi8NhRxgoDmZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدت دریافت بیمه بیکاری بر اساس سابقه و تأهل
🔹
به افرادی که ۶ تا ۲۴ ماه سابقه پرداخت بیمه دارند، در صورت مجرد بودن ۶ ماه و در صورت متأهل بودن ۱۲ ماه بیمه بیکاری تعلق می‌گیرد.
🔹
همچنین برای افراد با سابقه بیش از ۲۴۱ ماه، این مدت ۳۶ ماه برای مجردین و ۵۰ ماه برای متأهلین در نظر گرفته شده است.
@amarfact</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/681431" target="_blank">📅 17:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681430">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca86c810ab.mp4?token=hz3T8vmkQOFIkD-G_mImgOuS7pXmSHoUmIHIMMoC8Z4OARMcPpqMum0th2Yx4pVuZ9Vlk0gMZbRYO3IgDajl-CNH3pX15gGTwjtKarfYbcz1PPaaOcUP8C2YTtQoozTVTl8LTy9-X8bj4ZbICapdct_UAdtEjaklTda_zi98wkOdtq-NR3MtbPkUcxjT9ZgY0M2iMKUf8IkTgHaJYHFZbp366mt8pVvs6K0DIZjzi97yNKAU2O27nSzu-ktNVK1JyKVgMaDkJJLXcj1yYePIaVW_ytBDNZk_aQ1j5492SBoBt70FmhPzPmmG_aOMu3eCmbYI6BTxyfyejCGe61KGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca86c810ab.mp4?token=hz3T8vmkQOFIkD-G_mImgOuS7pXmSHoUmIHIMMoC8Z4OARMcPpqMum0th2Yx4pVuZ9Vlk0gMZbRYO3IgDajl-CNH3pX15gGTwjtKarfYbcz1PPaaOcUP8C2YTtQoozTVTl8LTy9-X8bj4ZbICapdct_UAdtEjaklTda_zi98wkOdtq-NR3MtbPkUcxjT9ZgY0M2iMKUf8IkTgHaJYHFZbp366mt8pVvs6K0DIZjzi97yNKAU2O27nSzu-ktNVK1JyKVgMaDkJJLXcj1yYePIaVW_ytBDNZk_aQ1j5492SBoBt70FmhPzPmmG_aOMu3eCmbYI6BTxyfyejCGe61KGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نادر سلیمانی: رضا عطاران در دوران ممنوع‌الکاری پفک می‌فروخت و در سیرک کار می‌کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/681430" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46402bb50.mp4?token=DgFs5Esnd6hUIgJEuUNu4MTBTOuu8YD9jBg4LD1LCn_8t-LxXW4353Qycg-kezpnAdDhhax-cY_ee8K_R0baXlbI6LplhOySfdlpTUWl6g0uZU-HQyOv3MmDm6gD5UmrwrPu1nl0RgBdJ_oPE6GZ8a_62ednuCWkanChY4Q-922VVIPjM4dP8W8D7wFl-dArF2-ZHTgahhsoTqdbkCUvYmNUxHVj2elg0gQccBUqlbl8KrqaGTL9-nE3VDZQvT9T1aS-Fm1T0xqhGDVkqaQD0nkRibv1et3MRBeVgzSlKloVQdZ_wY9himduzpsN2tdGzrEQpHttXaI9_WEegnoAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46402bb50.mp4?token=DgFs5Esnd6hUIgJEuUNu4MTBTOuu8YD9jBg4LD1LCn_8t-LxXW4353Qycg-kezpnAdDhhax-cY_ee8K_R0baXlbI6LplhOySfdlpTUWl6g0uZU-HQyOv3MmDm6gD5UmrwrPu1nl0RgBdJ_oPE6GZ8a_62ednuCWkanChY4Q-922VVIPjM4dP8W8D7wFl-dArF2-ZHTgahhsoTqdbkCUvYmNUxHVj2elg0gQccBUqlbl8KrqaGTL9-nE3VDZQvT9T1aS-Fm1T0xqhGDVkqaQD0nkRibv1et3MRBeVgzSlKloVQdZ_wY9himduzpsN2tdGzrEQpHttXaI9_WEegnoAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنجاقک؛ خلبان ماهر طبیعت با قابلیت پرواز به عقب
🔹
سنجاقک‌ها می‌توانند هر چهار بال خود را به‌صورت جداگانه کنترل کنند؛ قابلیتی که به آن‌ها امکان می‌دهد درجا معلق بمانند، ناگهان تغییر جهت دهند و حتی به عقب پرواز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/681428" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ذخایر جهانی نفت تا چه مدت می‌توانند جنگ طولانی ایران را تحمل کنند؟
نیوز دات کام استرالیا:
🔹
اختلال در عرضه نفت ناشی از جنگ، حدود
۲.۶ میلیارد بشکه
از عرضه جهانی را از بین برده و نگرانی‌ها درباره دوام ذخایر اضطراری را افزایش داده است.
🔹
برآوردها نشان می‌دهد ذخایر دولتی کشورهای عضو آژانس بین‌المللی انرژی، با کسری فعلی عرضه، حدود
۱۸۰ روز
دوام می‌آورد؛ در حالی که بخشی از ذخایر راهبردی آمریکا نیز به‌دلیل مشکلات زیرساختی قابل استفاده فوری نیست.
🔹
این وضعیت نشان می‌دهد طولانی شدن درگیری با ایران می‌تواند فشار قابل‌توجهی بر بازار جهانی انرژی و توان کشورهای غربی برای جبران کمبود نفت وارد کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/681427" target="_blank">📅 16:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230c5d55ac.mp4?token=U78a7eua9QU2BMANPK57Aw5zhzZgOGqSyQPHAHbWjh8x7hyLQClAL6bUmn-b2nZKmqK_lSvY93ttrKbUtqTCPpsrZKSlYJ8oONBz8V3taA3kWLzuZbUVBVLRBRIywK6TG1JpY-VSR6pitZ4BXCZ8e7ZcvgUMkOcbliv-QjAOdYqpIZ1RkpKOCp6pjB2mWIve3JgoFNEH3AA6rU0dKSgPDUZJw2wZCugh1hoh2ifBbhtW22FCyAZ0NNWWcovvA5we6kyEtQNNIge7TPHAf1pF_9xE-6DcvkKS2MVqWq9r5Mh1V1vBELysk7LsiAzmjF-EkknoLvZqGRLGSM2T-o1-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230c5d55ac.mp4?token=U78a7eua9QU2BMANPK57Aw5zhzZgOGqSyQPHAHbWjh8x7hyLQClAL6bUmn-b2nZKmqK_lSvY93ttrKbUtqTCPpsrZKSlYJ8oONBz8V3taA3kWLzuZbUVBVLRBRIywK6TG1JpY-VSR6pitZ4BXCZ8e7ZcvgUMkOcbliv-QjAOdYqpIZ1RkpKOCp6pjB2mWIve3JgoFNEH3AA6rU0dKSgPDUZJw2wZCugh1hoh2ifBbhtW22FCyAZ0NNWWcovvA5we6kyEtQNNIge7TPHAf1pF_9xE-6DcvkKS2MVqWq9r5Mh1V1vBELysk7LsiAzmjF-EkknoLvZqGRLGSM2T-o1-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز از دید شاهد
👀
🔹
انهدام یک ایستگاه توزیع گاز در منطقه چرنیهیف اوکراین توسط پهپادهای انتحاری گران (نسخه روسی پهپادهای انتحاری شاهد۱۳۶).
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681425" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpmZfHKOxXfmZPWwut5AEP7hMMaVwHbvePazPf9uMqTxdI5fqlw0O_7GUeAYHi_GhNwhOivr-o1e-aY77J5fvF9zA5xgZ9S9viJUwMO6BnNErf3iwrZW72CLvAMKAkpZ2AqWxeII6kzoxOPrl10GcAZh7NDbqk995hjTSwUxTL87oQ-0RhAFGDtO0Lc-AnKLqJhk28vdq-3O32m_hGIWQDgwytcqs54fseEM3_eSCT4sCHK5vYlMVxlJzUymt04Bsxo-eUwAAAsyoeLrqCWf91A5UcSpMIlJAnsrLNFY2_AQ_CS10gruBdZWn0VQgj1xp0DzuIB13gCRSNPf5UPz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی رونالدو برای ازدواجش
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681423" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpzK9rPl3SMwGIbuNi31drlJwFNPTtosJ4zsBUJa2PxX0NbzB-stX27ZSQUNbAvgVxy3_Fh5jUYgfN_09oAfETVdPeWsEatpnjinQ6SvThXAbG2vq0DmUB-tp19G0QIHC9fdxTHK37OFQ4dFUCWTW32JJBdToyN3xFFGzUnTDpWvqj6r2-9UCYRnIeaIMjv8-fTMWb7SyHf2kWfHzT5K8It7jpWfdXw12lHr4sdOBHM2HBRiwixxMNbN84tmu27-1p_tzY-Kf74zCEZ6ieT6FWtULBUWQnTL8ZtZyE_KHzlGe7OPRoc-mRQeOLwdgNGGQlwOmjsZ95ClpxQKZcLTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: تلاش آمریکا برای ورود اتریش و یونان به پرونده ایران
آسوشیتدپرس:
🔹
با متوقف شدن روند مذاکرات میان ایران و آمریکا، دولت ایالات متحده تلاش‌های دیپلماتیک خود را گسترش داده و از ظرفیت کشورهایی مانند اتریش و یونان برای کاهش تنش‌ها و بازگرداندن طرفین به میز مذاکره استفاده می‌کند.
🔹
رایزنی‌های اخیر مقام‌های آمریکایی با وزرای خارجه اتریش و یونان و تماس‌های بعدی این دو کشور با وزیر خارجه ایران، می‌تواند نشانه‌ای از تلاش تازه برای شکستن بن‌بست دیپلماتیک باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/681422" target="_blank">📅 16:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
بقایی: توافق بر سر نقشه تردد کشتیرانی در تنگه هرمز حاصل شده است
سخنگوی وزارت امور خارجه:
🔹
با وجود کارشکنی‌های آمریکا، گفت‌و‌گو‌های ایران و عمان روندی رو به جلو و مثبتی داشته و توافق بر سر نقشه تردد کشتیرانی حاصل شده است.
🔹
این اقدام حاصل یک همکاری جمعی بین‌دستگاهی با محوریت وزارت امور خارجه و مشارکت فعال بخش‌های دفاعی، امنیتی و زیست‌محیطی کشور بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/681421" target="_blank">📅 16:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
گرانی وانت کار دست مردم داد/ اجاره پراید وانت برای کار، ماهی ۳۴ میلیون ناقابل!
🔹
در حالی که قیمت پراید وانت در بازار به بیش از ۱ میلیارد تومان رسیده حالا شاهد ایجاد یک بازار عجیب و جدید هستیم. حالا بسیاری از افراد توان خرید وانت ندارند و به سراغ اجاره وانت برای کسب و کار خود می‌روند.
🔹
به عنوان مثال در یک آگهی پراید وانت به صورت ماهانه به مبلغ ۳۴ میلیون تومان اجاره داده می‌شود. البته نکته مهم دیگر اینجاست که معمولا در آگهی‌ها ذکر می‌شود که باید مبلغ اجاره به مدت ۳ ماه واریز شود./ خودرویک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/681418" target="_blank">📅 16:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681417">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23620ece1e.mp4?token=I8fE2LPyVUX7oUlyZp5jQLXWtNyqCY9c6i5IjoHvhlwLx4kZScaaeZh16RYhXf2BU8lufSRlZk5BwASzc117H8Mv0yyf0_CQjWTJsEfp_5HYhIEwyXLM0jHQMpWKhjD7A2YG3CtWYCsB-ogdN1jlXE1jxWCOUgmBgC9D0UUrevWB-uahR3FctH4eQYg57gQvORpODEK0LKlQF2Yne-52rVykFtbm8-W5JYE4Scs3o1yXoSOJ7Annrcusy1bu-hg9XcLZ-ksGHhpKvGYhnU7ZsQY7DEV36dghAQpfT73-j6CyIE7P33USXP-a4zldMY-a-8R6T-q0J0bCp7wkZ1xXwb7dGC5v1cwjLrWEeyeooWCEbwRRPi11NznCUB0bZFOnbf7w7_Z_XI-P9s_wUOg8nYU4n7_yyX6upfT_L9HWMWQB1352faRDyFGPIvaAnolJjepp3j-KUex4SmmYHiCfZKtP3egKIZ9Oa6X5Ix7eb0XOhQv0kOtcRi36CCmJX92GqLddKw7shWPx5Kdg1VlhUpH54sUtBHfGwUnL0AKcQT9MI9DMFQt7mGh7virNH9teol_zczZHwoPemeZYMpQt_8Pj_f7gtx-jERzaNBbHYgNxJf67GDTo3WXk2JkG-lDitc4jDgn1MWA7UPO5rdE4ba7bfN4aWfIkN6whmGBEMI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23620ece1e.mp4?token=I8fE2LPyVUX7oUlyZp5jQLXWtNyqCY9c6i5IjoHvhlwLx4kZScaaeZh16RYhXf2BU8lufSRlZk5BwASzc117H8Mv0yyf0_CQjWTJsEfp_5HYhIEwyXLM0jHQMpWKhjD7A2YG3CtWYCsB-ogdN1jlXE1jxWCOUgmBgC9D0UUrevWB-uahR3FctH4eQYg57gQvORpODEK0LKlQF2Yne-52rVykFtbm8-W5JYE4Scs3o1yXoSOJ7Annrcusy1bu-hg9XcLZ-ksGHhpKvGYhnU7ZsQY7DEV36dghAQpfT73-j6CyIE7P33USXP-a4zldMY-a-8R6T-q0J0bCp7wkZ1xXwb7dGC5v1cwjLrWEeyeooWCEbwRRPi11NznCUB0bZFOnbf7w7_Z_XI-P9s_wUOg8nYU4n7_yyX6upfT_L9HWMWQB1352faRDyFGPIvaAnolJjepp3j-KUex4SmmYHiCfZKtP3egKIZ9Oa6X5Ix7eb0XOhQv0kOtcRi36CCmJX92GqLddKw7shWPx5Kdg1VlhUpH54sUtBHfGwUnL0AKcQT9MI9DMFQt7mGh7virNH9teol_zczZHwoPemeZYMpQt_8Pj_f7gtx-jERzaNBbHYgNxJf67GDTo3WXk2JkG-lDitc4jDgn1MWA7UPO5rdE4ba7bfN4aWfIkN6whmGBEMI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گن سکه حباب داره، دقیقا یعنی چی؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/681417" target="_blank">📅 16:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
هندوستان‌تایمز: ایران با وجود حملات گسترده اسرائیل، توان موشکی خود را با سرعت احیا می‌کند
🔹
این رسانه گزارش داد با وجود خسارات گسترده ناشی از حملات اسرائیل، ایران در حال بازسازی تأسیسات آسیب‌دیده، احیای ظرفیت تولید و تقویت دوباره زرادخانه موشکی خود است. سرعت این بازسازی نگرانی‌هایی در اسرائیل و میان برخی مقام‌های غربی ایجاد کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/681414" target="_blank">📅 15:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRVzZrXkuAXW3-SS5RDnDBvm9MUCTnKVPhzeD4thJ7VenMvAVWtLXQoyBQoVqfg2ohX5eMJuCQUwhb3ffNUHB7g8w1TpyGjkH5J9v7kGTnCPbEjuLOhuvt1r08PsdpbTaTgHL1hEFkUXtYRO9yA2uFTcIxdNXEMlbNWibgWWG5DSbmLTxHlgAyZ6NoItRbPtwtgAgJ2xGtJCW7jIBmexeCaXQX4aGir2tkmXWdUexdupKjkVSawXFn-4KKxZ-fUmJtau-EPcXsIkUcXtgQiQZq90nmR2kjX3EfHKM13hw4iwM_9dgPwb_VyQc82qhkwT5QzcTUeGSZLjgz6lGTsD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9lxh9l_W1q1Oqee3C141VQbN3USv0EOm_-ua2Uz7tnyXjcYKYO3vizJDcrLS0fTe2I4qswjh_K7kbwo0D8qC_hmXubIDZnJK-64zv-TS8byyeoR0Ja1gbRggs7msravCf9Tr9N0oduX1y6roIBICUfwx-A-VTAj2RETbNMjcRBcsFSOBGHQM4HU9abpOqv-2JNh89aW2VagjALOVUCjK3c4UIpdVrg0aGjCwJb6mqENknMjh4GFc6N0rID5Kl9fkph1XbXNvfE60CmvDmYlg8fmMT-qMW5kCDtV9YK5osbFczbbqvaT47ICp_z1tLfSlOetv_fvB-7m5KdhDDjvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX2NrY0XaAgVHJy4tsRK7yIUXJMqWzUfyP6qwZ9ZZFjwT5kWfZQGQHHGUznhpb7ueOgK4qty_0sQAPk0XbFfxCsj776Ceun5BbSncIFo7Guqxa3bfa89c2uD_QHsj9fTYZsTq_ilKZjnAQ-mqeBqXWgU7P03cRiAjLx07dK1LT3e6FZ3RcYdG_UxsEzi57YYR5BbLcS5sQudjmzcEzyIL3wOziYeTsPen0GClQYBUlQlQeDHzBH47lGtbygGu0a4TlP-MfVLGmGfs6mBMJ0r1mCl8bUhOGf6wrg2IDkl0NydDfXAFGH7tPB4LVBcfTazi2YmssSiCIMwumYZs81Ddw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
آینده فرزندانمان در گرو صرفه‌جویی امروز ماست. با مدیریت مصرف آب هنگام شستشوی ظروف، حافظ این سرمایه ملی باشیم.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/681411" target="_blank">📅 15:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa3785379.mp4?token=hrW4qSo8p_BdJvHamkTI_zC0IPXWs2fsOzkEMu_IR6no6458U4ESiph-ZFe6fI_o0gbOL2GpRJ4qoEXLoPXHje3pq7-OJneSR9iu3eCZs_1p_wrMeX0SrCsFLg__T-BDuWrzfSjNKyyHKpEnQd7C4r6wnVdmQhPAnX2ExYIbBE_nF_me_LJkKY5PyOvkcKOMFwuptuvmrllN99KWRYGYZBjJajhjP4_HR_sEF55KewOT2SA2YJuqAv9FbhnviEV3hd0KSwKA7lCUTHGdxkcxQ26OFIcoco0eNz3cgJy4SKqk20dpeE8lP3t7fIGcEKqoVAhc8umozhoK3mbWI4h6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa3785379.mp4?token=hrW4qSo8p_BdJvHamkTI_zC0IPXWs2fsOzkEMu_IR6no6458U4ESiph-ZFe6fI_o0gbOL2GpRJ4qoEXLoPXHje3pq7-OJneSR9iu3eCZs_1p_wrMeX0SrCsFLg__T-BDuWrzfSjNKyyHKpEnQd7C4r6wnVdmQhPAnX2ExYIbBE_nF_me_LJkKY5PyOvkcKOMFwuptuvmrllN99KWRYGYZBjJajhjP4_HR_sEF55KewOT2SA2YJuqAv9FbhnviEV3hd0KSwKA7lCUTHGdxkcxQ26OFIcoco0eNz3cgJy4SKqk20dpeE8lP3t7fIGcEKqoVAhc8umozhoK3mbWI4h6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی دیدنی از مادر و جوجه‌های جغد خاکستری بزرگ؛ بلندترین پرندگان شب در نیمکره شمالی
🦉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681409" target="_blank">📅 15:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMwrEJnSS_DNsJFk9WkqldWGSkIqdTcDNznMOVIpygkYHPUhLKIK-1xJ_hJTYMxU9K5M8FvOQOMH0Y0RO8A7wSSK6Q3_CmVCXHRLYdR_DgrwWW49idWq1FQnZuRxzx-BleUSsth5_sfd9VuFYLW5Q6wgLnMm_W8OCKEOo11RONDW9kvNm6QRh8SCkDQT3oS0ozetZN5vxcdMicaIIqNddO6W_RGsSuuawCJ4xwv3V8WL9dovuSVN5TLcrf74z8H1VYxKYH2aCE2At7C7DEAoiLPbDcN6M00ew-W2T7i0G1zYtiy3dJMr4i11hMpUOr_8RCb4ISQYgOWSSXx3e1Vs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران»/۸
🔹
ثبت رکورد ۷۲۶ همت تامین مالی در سه سال توسط بانک کشاورزی
🔻
حجم تسهیلات پرداختی بانک کشاورزی با شیبی صعودی از ۱۸۸ هزار میلیارد تومان در سال ۱۴۰۱  به ۲۷۷ هزار میلیارد تومان در سال ۱۴۰۴ افزایش یافته به طوری که از سال ۱۴۰۲ تا ۱۴۰۴ با رشد متوسط سالانه ۳۰ همت، جمعا ۷۲۶ همت تسهیلات پرداخت شده است.
🔻
رشد مبلغ تسهیلات پرداختی هم زمان با رشد تعداد تسهیلات، موجب شده تا متوسط مبلغ هر فقره تسهیلات نیز به طور میانگین سالانه ۳۵ درصد رشد کند.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681408" target="_blank">📅 15:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681405">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuBb1rB4lU0GF6VReKSnEO99JffTC9LIFg4l3PG7EyX17jbWFmUXsCUEs2bgHGjsbgnhvjMk4UbpUAy1I88LLabQT0dOunno68NMpA09MAXw-8QTi9NF11RERO9Pg9pGNKvNl4eCw5FEa6JU-Xa_JdbFLrCCDq514yKyq7kXSIkmfo6xW4YwItkQRQ_8QjtUHCOmVZhR57dmmUbuVhUh2sF4MwYQv0w_253W06FUCWG1nD_O4qexLE6AHBZljHB_CbEieA6iuo4Q3f3B_S_iiQV79J3LnLTpi94hu16wBPMakD1SuqknrCTy0SUpmA2f8btnfy7Ozhrpc7G524iB8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون هماهنگ‌کننده نیروی هوایی ارتش: چهار خلبان پایگاه شهید دوران، مأموریت بمباران پایگاه العدید را انجام دادند، اما سرنوشت سه خلبان هنوز در ابهام است
🔹
تاکنون به جز تحویل پیکر مطهر شهید مجید کاظمی، خبر دقیق دیگری درباره سرنوشت سه خلبان حاضر در این عملیات…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/681405" target="_blank">📅 14:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681402">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c91565062.mp4?token=aISubj6YBbbU-R75xoFXnhnLPQeD6PbmnfHDopiZHsld3TDE_uck51QYd-88YXVJWOgJRC_0Sy7FcMELBUJMEkdtqjdiogQb7sOyMh7iDcxbovFqBxOcqrDG3z4dnNPp3_GSCJL4sjzBjZywWSZjo88qoZ7Xyfc8aXziVDDbUH6LIRwIQ-4071vKpOyNLMXZyfceYnSSf6iu7kkfsWLMAZ6v9weE47Ha8n63ADOhsnUfMITo7EpKKWO4AGrgeaEBox9e3JB4HJ4zwcPvFmxCD9VTxWyA_dLiQ9GJY9yhmbiTTAt3OGfPgMwJ7t7KMizkUu2DH-GEpgkyuq-KdqPvfhz5J4YrZAsIoHxWi8arnOehPbdo1MIyf0aa5kbk5GI9gb7J6th9Nv8Lmbd040Z9tziLZz0Jo4xiYnEignHssTFxmJWNrs5BpDntldHLm-xknG4T1YAbH7yuknPwKK1yw2CxBIrUSkrekc-HEpvZDxY8cuhMmChEBNM5zuxbqe6xdLtUqdJxOS5FBDlpoM_11iVMvv8TwFcxisZXjQk238-E1k2qfzUvyBACFSHe715ceE8suJEWyGTnrkdjQ9vawTNJ-fqCMhXcjCRcrkZlU9Nc-CM14WZIguQxkReFaDNxp8edWA-2Zu1NNwoJK6tvoZNBWpcQxI5NIHokgVmRcVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c91565062.mp4?token=aISubj6YBbbU-R75xoFXnhnLPQeD6PbmnfHDopiZHsld3TDE_uck51QYd-88YXVJWOgJRC_0Sy7FcMELBUJMEkdtqjdiogQb7sOyMh7iDcxbovFqBxOcqrDG3z4dnNPp3_GSCJL4sjzBjZywWSZjo88qoZ7Xyfc8aXziVDDbUH6LIRwIQ-4071vKpOyNLMXZyfceYnSSf6iu7kkfsWLMAZ6v9weE47Ha8n63ADOhsnUfMITo7EpKKWO4AGrgeaEBox9e3JB4HJ4zwcPvFmxCD9VTxWyA_dLiQ9GJY9yhmbiTTAt3OGfPgMwJ7t7KMizkUu2DH-GEpgkyuq-KdqPvfhz5J4YrZAsIoHxWi8arnOehPbdo1MIyf0aa5kbk5GI9gb7J6th9Nv8Lmbd040Z9tziLZz0Jo4xiYnEignHssTFxmJWNrs5BpDntldHLm-xknG4T1YAbH7yuknPwKK1yw2CxBIrUSkrekc-HEpvZDxY8cuhMmChEBNM5zuxbqe6xdLtUqdJxOS5FBDlpoM_11iVMvv8TwFcxisZXjQk238-E1k2qfzUvyBACFSHe715ceE8suJEWyGTnrkdjQ9vawTNJ-fqCMhXcjCRcrkZlU9Nc-CM14WZIguQxkReFaDNxp8edWA-2Zu1NNwoJK6tvoZNBWpcQxI5NIHokgVmRcVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگ کیسه صفرا؛ مهمان خاموشی که می‌تواند بدن را به دردسر بیندازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/681402" target="_blank">📅 14:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681401">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ویکم از فصل پنجم
🔹
در این قسمت تجربه‌ نزدیک به مرگ آقای سیدهادی سجادی که در اثر تصادف شدید، هنگام جدایی روح از جسم، شیطان برای انکار خداوند توسط روح تلاش می‌کند و روح حسرت اینکه چرا در دنیا به دانسته‌های دینی عمل نکرده را می‌خورد و شاهد قطعه قطعه شدن آسمان و نفرین شدن توسط فرشتگان در هنگام دروغ گفتن به مادر شده و ۳ سیلی به خاطر ۳ دسته از گناهان به ایشان زده می‌شود و گرسنگی طاقت فرسایی که توسط تکه کوچکی از نان و پنیر دختر ۳ ساله از بین رفته و با شنا کردن در رودخانه و گفتن اذان فرصت دوباره زندگی به ایشان داده می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سیدهادی سجادی بلالمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/681401" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681400">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
امارات: یک کشتی ما هنگام عبور از تنگۀ هرمز هدف قرار گرفت
🔹
منابع خبری اماراتی به نقل از شرکت ادنوک این کشور، از هدف قرار گرفتن یک کشتی در تنگۀ هرمز خبر دادند.
🔹
سازمان عملیات دریایی انگلیس روز جمعه از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/681400" target="_blank">📅 14:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681398">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrQQ46OwJ-_OuqdLp13P3eQUXP2TNgjESoDr2ukZEYHPchUpTAPdu7TRK-GKjwoyonUlA4UwkpG8TuZRmRXDelzbvI-7Y0SLkE_PM7kMx0y05i3wMt3cr-85VQY3aUVRvPRV5r5wra2IEmhIEvTAL1jkLCBHcOTB8kl-EwwpKy9gDHM17PjGg62u4huQg1_RRPLRWVFFKWLZPSCkozTL7qE4F6OcNADATqwCW0GMFOBqVo5oqzAor5B3kquef-ZPAj4JfT2JNCw8VclaYVLihUtBv-A68eR1MwjOkCI1MA9Dsgzh1vbjcNwZ8vNJn11Pav4S-IkxGkpeGWthTi2IUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش بیش از ۸۴ درصدی عبور کشتی‌ها از تنگه هرمز
🔸
پیش از آغاز جنگ رمضان، روزانه حدود ۱۳۰ کشتی از تنگه هرمز عبور می‌کردند که این رقم پس از جنگ به حدود ۲۰ کشتی در روز کاهش یافته است.
🔸
از آغاز جنگ تاکنون، حدود ۴۰ درصد از کل عبور کشتی‌ها از مسیر تحت کنترل ایران انجام شده است.
@amarfact</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681398" target="_blank">📅 14:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730d812ca9.mp4?token=NtLEq3twk29qMaFsR4ciEWmxKBdrKQfzmjXQR-fZpCdrCowt8VRiPQ53rHkZlJzVZ0fwzgwNpB1QB6dy2x-kx4x1b-36HaI3hHm23pVW-1OWL6S0GtAcht6DrJ9TDEafvljGtUiKOHXDwGJlPA38qWH9AZfOW2FHqRrMSi9eSGyKTq4iateHlGCLyIt67PHJ04Xx-Z8VUOtpt1ljmDvHIAyCRMcC4uzHNYb8Pw8hVE6lZ159nNCUL6_zPVPTgzlLumrjI_CKlfzMOqRu8wa8AYyTc66qdwO9axt78ZOkybnq5-0fv2HB6Uvtfel4ZmIkZdR6YMidCGyJuVQbUVXRohV2UA4Iw6lKCTMoClNbpGCG3bln7omAKUa1cQROlntCvhD7Y8ZSXzUBTPQKLQha1azcwo2XqqgMRd_APMWaK55ePMXM-KRqMMfmY9jQ3ql8B7BGs5L4Mc1g8kRwF-Rilfx2DBrKbrDdn16HfK0g289uGWjOGSGITcjzKi9tuAeVShbYU2tSYM6D8knRTbE4MmyNTaVmglDQH87Hp_PoHp4d5LXeEO8ZJY7ifWaIUPDc3YCGhw4t5BceBgfaH1FwF_qufPRv5VA2p_ydb0GhQtz6lDXs6KEtaCq7PXWVQgyinAZY64NVDYnr2bv1pxycBhOljueEz9n4RaOjLydwidk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730d812ca9.mp4?token=NtLEq3twk29qMaFsR4ciEWmxKBdrKQfzmjXQR-fZpCdrCowt8VRiPQ53rHkZlJzVZ0fwzgwNpB1QB6dy2x-kx4x1b-36HaI3hHm23pVW-1OWL6S0GtAcht6DrJ9TDEafvljGtUiKOHXDwGJlPA38qWH9AZfOW2FHqRrMSi9eSGyKTq4iateHlGCLyIt67PHJ04Xx-Z8VUOtpt1ljmDvHIAyCRMcC4uzHNYb8Pw8hVE6lZ159nNCUL6_zPVPTgzlLumrjI_CKlfzMOqRu8wa8AYyTc66qdwO9axt78ZOkybnq5-0fv2HB6Uvtfel4ZmIkZdR6YMidCGyJuVQbUVXRohV2UA4Iw6lKCTMoClNbpGCG3bln7omAKUa1cQROlntCvhD7Y8ZSXzUBTPQKLQha1azcwo2XqqgMRd_APMWaK55ePMXM-KRqMMfmY9jQ3ql8B7BGs5L4Mc1g8kRwF-Rilfx2DBrKbrDdn16HfK0g289uGWjOGSGITcjzKi9tuAeVShbYU2tSYM6D8knRTbE4MmyNTaVmglDQH87Hp_PoHp4d5LXeEO8ZJY7ifWaIUPDc3YCGhw4t5BceBgfaH1FwF_qufPRv5VA2p_ydb0GhQtz6lDXs6KEtaCq7PXWVQgyinAZY64NVDYnr2bv1pxycBhOljueEz9n4RaOjLydwidk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری تازه از جواد عزتی؛ این بار با روایت هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681395" target="_blank">📅 14:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پلیس خبر داد: دستگیری دو زن در پرونده سرقت مسلحانه شهرک غرب
پلیس تهران:
🔹
دو خواهر برای ملاقات با دوست هم‌باشگاهی خود به شهرک غرب مراجعه کردند که ناگهان زنی نقاب‌دار با تهدید سلاح، طلاجات و دو دستگاه آیفون آنان را سرقت کرد.
🔹
دوست شاکیان با سارق هماهنگ بوده و انگیزه خود را انتقام‌گیری شخصی عنوان کرده است.
🔹
هر دو متهم برای سیر مراحل قانونی به مرجع قضایی معرفی شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/681394" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5332f54efc.mp4?token=TvBkI-R1ZDoEacfT8sFRvG7UJsqTXBvgDfNjGz6GGQx1mO042XilKOszMeHsGfxiChZ3LHbMFkAnbe3CC0YrmAG8-CJDqt45LbPKRM15k4SidVAPpYujtAhyvtT4hSPp63GWLBcLp3uJDK4tUpRvKqV88xeZ2el7t-eWO-bk5mglLhv1FGGC4wn0VNZPhdFU6zcgxPI-Exs3LsZkWH6qShvmhbRwtFv8T1Vwbdksz9drahhU1BZYOSnJRFnrkXV1jR_MyZ7muNHAdeNg49D1qagbWttgHSf5-avOPgs2gHKP3z6WHGvgsaGMPCY7uG55IWC9a6Oex6R2hn3pFLP9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5332f54efc.mp4?token=TvBkI-R1ZDoEacfT8sFRvG7UJsqTXBvgDfNjGz6GGQx1mO042XilKOszMeHsGfxiChZ3LHbMFkAnbe3CC0YrmAG8-CJDqt45LbPKRM15k4SidVAPpYujtAhyvtT4hSPp63GWLBcLp3uJDK4tUpRvKqV88xeZ2el7t-eWO-bk5mglLhv1FGGC4wn0VNZPhdFU6zcgxPI-Exs3LsZkWH6qShvmhbRwtFv8T1Vwbdksz9drahhU1BZYOSnJRFnrkXV1jR_MyZ7muNHAdeNg49D1qagbWttgHSf5-avOPgs2gHKP3z6WHGvgsaGMPCY7uG55IWC9a6Oex6R2hn3pFLP9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر کتونی مناسب چه مدل شلواریه؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681392" target="_blank">📅 14:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
جزئیات استخدام نیرو‌های شرکتی اعلام شد/ قرارداد مستقیم فعلاً منتفی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/681391" target="_blank">📅 14:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB2iCsRFDbzgOcqDdAyJ23eWQknYVF9APkZv7nsaigVRXhWgYL7IPORXE_-83Rc0wfiAEA0FdnIn9yNigVbqphklGGm5K5NIXpcZweMHdYP1hjhFTVH2sszxiYcEjATj5bf-jRozKa1SALsxbVwKxQ1EHBInReYoAsOwV1R8WR8ZLlXC3eMq9jGFYxzogLBCX_7XBQtcDjG688IYJYexpMhI30souRE4eHeOaXzBzMQDtrFe6yAZFJl3nm2ICt3nuVMRGXUd91RLw3TDbOuyIkzmtkGv8fKVNi0a1IMEwEybo6oZov1YInk2EXPt6avC5J1gumx3856Nvfcuqcw0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روح‌الله حجازی: سطح هوشیاری رابعه مدنی ارتقا پیدا کرده
🔹
حجازی کارگردان سینما درباره عیادتش از رابعه مدنی، بازیگر سینما و تئاتر که به تازگی از بیمارستان مرخص شده، گفت: سطح هوشیاری ایشان  به‌مراتب ارتقا پیدا کرده و خوشبختانه حال خانم مدنی نسبت به قبل بهتر…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/681390" target="_blank">📅 14:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
کارت ورود به جلسه کنکور سراسری ۱۴۰۵ از ۲۶ مرداد توزیع می‌شود
🔹
کارت‌های شرکت در آزمون کنکور سراسری ۱۴۰۵ به همراه راهنمای شرکت در آزمون از روز دوشنبه ۲۶ مرداد تا روز چهار‌شنبه ۲۸ مرداد از طریق سایت سنجش آموزش کشور منتشر می‌شود.
🔹
آزمون اختصاصی گروه آزمایشی علوم تجربی صبح روز پنجشنبه و گروه‌های آزمایشی هنر و زبان‌های خارجی بعدازظهر روز پنجشنبه ۲۹ مرداد و آزمون گروه‌های آزمایشی علوم ریاضی و فنی و علوم انسانی صبح روز جمعه ۳۰ مرداد ماه در ۴۱۵ شهرستان سراسر کشور برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681389" target="_blank">📅 13:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc-98bf4GdUEg9kxIlxEttlDbdf7TcStk2l_vIEWItpUNyZyicwAOy9lIDUCzc8uXQAysGBYSYpcnQlP8ud3h3PeWSUXbhOrNjurc6u1fzQRVCq1TnyuC7DrWXYS4SvpjatqqyMCBCtr7Ihjs8ov2I4mQoClik--I2MVnTB9I20ZeADSAOTp77rrBSQCpfHHG4qB7SwUqGEyH2oxQCxrCt--OfXoWMgVEIh47RMorrFNQrSNAenmtvOdyLAE_SKv4lfbFIVVJJeB61kBqSr7T-yI5jeyhcrp_HB4vmxxPjaRJRu8c0mPtlDSuDo7oUO3MCi-AEI8CCrVS5CjhKiFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از رهبر عزیز انقلاب اسلامی
در جبهه‌های جنگ در سنین نوجوانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/681388" target="_blank">📅 13:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681384">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3185ce41e.mp4?token=XAVG5lu_eGIeok3N6uSRm-IQsIecZRnNXRoYbNxEjvrMOpm2wqYtQT6Lmf3Y6Dn3l_vMvo0SBZiHLuxEOvyi7LnIkrVXeUEBluZJ1dKackB-fIxmHsepPlgSNWArw0wRnCl3i0KnEZSRILuxILni3ebXUB2SSishDcSfTtS29Xs3HTOtrMSqz0qJEsLh8yBqt1NXsugDUlS4Q6S5xXhYGCZVfDOUiUh-vO1uZvvNX8p7BqiU13QUP9CzC7ohEWgokDLLsYBzhju8fpr8UEFQZGaTbB5bbNCXHjACjc8R_ktOBICDCLP11LOe_ysgf7txIZlHq_PBOxj60YkN0UdhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3185ce41e.mp4?token=XAVG5lu_eGIeok3N6uSRm-IQsIecZRnNXRoYbNxEjvrMOpm2wqYtQT6Lmf3Y6Dn3l_vMvo0SBZiHLuxEOvyi7LnIkrVXeUEBluZJ1dKackB-fIxmHsepPlgSNWArw0wRnCl3i0KnEZSRILuxILni3ebXUB2SSishDcSfTtS29Xs3HTOtrMSqz0qJEsLh8yBqt1NXsugDUlS4Q6S5xXhYGCZVfDOUiUh-vO1uZvvNX8p7BqiU13QUP9CzC7ohEWgokDLLsYBzhju8fpr8UEFQZGaTbB5bbNCXHjACjc8R_ktOBICDCLP11LOe_ysgf7txIZlHq_PBOxj60YkN0UdhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یه آزمایش اجتماعی که نشون میده ما مردم ایران از کارکردهای مثبت بازنشر در شبکه‌های اجتماعی غافل هستیم...
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/681384" target="_blank">📅 13:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06827928b3.mp4?token=kv4Kp1Ea_dfn4JwSO70O1pLaGpPi7WUXvXhSJxtO2_HSnpnvB7lfQpEljuUWlJja5yiU1Aw_USLW-_sAFCf16uTY6Zq_WumnNWGxadBMhWac_nTxbWdx8HT2da-bbJc8xrl7bCjHgLZjZxSMZ5dY82h3cFGiS3ghC-LyTgbs3L9svJAtaEv0dvkVPteiYwbHpE1UGG173rY9jgPXCJ3hinuEsYI1QUCX7fIt3WGPlnWsh9Kwm3_sX9XXmO2Ad34FNTzjHZDafTvbU35RzKUy0Kb6UHps47U_28VqlspDJfKx_KPkr_X-UzIYkEj1YEUE1VAbkiWE03jepwawMJJpJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06827928b3.mp4?token=kv4Kp1Ea_dfn4JwSO70O1pLaGpPi7WUXvXhSJxtO2_HSnpnvB7lfQpEljuUWlJja5yiU1Aw_USLW-_sAFCf16uTY6Zq_WumnNWGxadBMhWac_nTxbWdx8HT2da-bbJc8xrl7bCjHgLZjZxSMZ5dY82h3cFGiS3ghC-LyTgbs3L9svJAtaEv0dvkVPteiYwbHpE1UGG173rY9jgPXCJ3hinuEsYI1QUCX7fIt3WGPlnWsh9Kwm3_sX9XXmO2Ad34FNTzjHZDafTvbU35RzKUy0Kb6UHps47U_28VqlspDJfKx_KPkr_X-UzIYkEj1YEUE1VAbkiWE03jepwawMJJpJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروپف بامزهٔ یک مرغ مگس‌خوار!
🔹
این پرنده در بیداری فوق‌العاده پرشتاب است، اما هنگام خواب برای صرفه‌جویی در انرژی وارد حالت «تورپور» می‌شود؛ یعنی بدنش به حالت کم‌مصرف می‌رود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/681381" target="_blank">📅 13:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681379">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
رسید جعلی، پول واقعی را از دست فروشنده خارج می‌کند
🔹
رئیس اداره اجتماعی پلیس آگاهی فراجا با هشدار نسبت به کلاهبرداری با استفاده از رسیدهای بانکی جعلی گفت: شهروندان و به‌ویژه فروشندگان کالا نباید صرفاً به تصویر رسید یا پیامک واریز وجه اعتماد کنند و تحویل کالا را تنها پس از اطمینان از واریز قطعی وجه انجام دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/681379" target="_blank">📅 13:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681377">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ercEHOBeGiE9DtOQBMRZG256NEDJxG2vxKJG7OqNn1VHH0OhgqnNItghB-Q4ZGlmLCuD61Onyt1pJz_g5NNNn9seGCyX9jSrzOTQenRdzVZunip2Duk4frmUBSGS6nMXlfVml4ww9trZGcIHXxImdqBh3WN-ZT-_6qQQgz8ojnrcrnA5oDgBgBiKNpvH6ZLLXMIa_rYP6KGYsfDFiV-EnU4ZyQMmi0DYiu9qqdr93ELO6H3RH2jmm6xu1F_TAeEwxFb08XvlT9VpuIAEKC0pEwlQM_S4OA-SuG20n8iyC6oSVSR7lDZF1DNYhWDBJ7aYkxI2bvBqmuo1U6mgXX2BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوک‌های خزری یکی پس از دیگری تلف می‌شوند! تلفات به ۲۵ قلاده رسید
محیط زیست مازندران:
🔹
لاشه دو قلاده فوک خزری در سواحل بهشهر (میانکاله) و محمودآباد کشف شد که با احتساب ‌تلفات ثبت شده در سواحل استان از ابتدای سال جاری تاکنون، ۲۵  قلاده فوک تلف شده است.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681377" target="_blank">📅 12:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e032fd3c33.mp4?token=p4masViTHgN68_uq6-ikbh7B2VgNrAq13R9HrAktqToMXDE64Y51yNB0JikVNvEnlgNwWimKvXWAD-FUX_ndeDFmqVLx5gjxGRygHJS8Q2y648RJpOhRfy4vcQwz_1ybfex3KPtfquMm-TOZMWTtsvDELJ_gFRVB99h8P0qiuKG-7u3ZaUYGbzrDj0M4yJq1FiB4cqfANzsh4WenGv85PV1yGSkTqNvuRGQbEhsrHv9j12tuwUtEy9vgcEuk5MAzfU9Opby3nnWxpe2lj3QXaF2YWbxnahrIHO-EsKwOEO1MsaTM_U-Y6vP2zPp4WQzr8JthSW5X3894c2rqi46K8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e032fd3c33.mp4?token=p4masViTHgN68_uq6-ikbh7B2VgNrAq13R9HrAktqToMXDE64Y51yNB0JikVNvEnlgNwWimKvXWAD-FUX_ndeDFmqVLx5gjxGRygHJS8Q2y648RJpOhRfy4vcQwz_1ybfex3KPtfquMm-TOZMWTtsvDELJ_gFRVB99h8P0qiuKG-7u3ZaUYGbzrDj0M4yJq1FiB4cqfANzsh4WenGv85PV1yGSkTqNvuRGQbEhsrHv9j12tuwUtEy9vgcEuk5MAzfU9Opby3nnWxpe2lj3QXaF2YWbxnahrIHO-EsKwOEO1MsaTM_U-Y6vP2zPp4WQzr8JthSW5X3894c2rqi46K8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند هوشمندانه معلم برای وارد کردن دانش‌آموز خجالتی به جمع
🔹
معلم به دانش‌آموز خجالتی گفت: «اگه کاغذ سفید رو انتخاب کنی، به کل کلاس نمره ۱۰۰ می‌دم!» اما بچه‌ها نمی‌دونستند هر دو کاغذ سفید بودن!
🔹
همین ترفند باعث شد اون پسر بیشتر وارد جمع بشه و بچه‌ها دوستش داشته باشند.
گاهی یک معلم می‌تونه زندگی یک دانش‌آموز رو تغییر بده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/681375" target="_blank">📅 12:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94ecc8f64.mp4?token=Ptv1XfKXKOzOn5LjW0DcUuBmKPdvd24rodIFwVIaOR94EeKDh-t_2p_u-w32u03MdMoJvkQclEQ70nCC0WvuCc22YLWkcclBhydhan4xhCBocXKZjnVVu9JeCDtzX_eDy6Qhq2rVLPCHMori5QGHAl7-pXi0n1naMIutR3aAFzTVR5u0xQ3uGhCLU43Q1BNQITByqDP5q2EC4oTewKuFg18UV1WaC6ZbsDhjYBO-JoA1pW_rXzbg154GM0X9AX3qZAPQYD0-oc1kOYxCvh45I2iDEfZMOeN9WS2u1XH17c42Rc48lGvtUhs04-KpM13PDbyA3Ufuu9s9P91bqtp4gYcdOW1cgV2qgbADSz5H0hOpGKr5USe2dMCmq5WXD4mOiYL_cjiDqECL5Rte8bKal5KhrOjs1IuwAm7f7H1kQxHN5D8l3HBuTsFOAOorWLM2dEQs4H7Lw-uIv0makwgPGFJDHispAjh-3HT39bhjeaWBZA7ZoUwUIPGJOFDOZ-NUvlCGU-FbG0WKhG84APjzGWQHIINfvUZvWhH40_BQng4QVGN79MCfUslQEMDWqi9Y9HcmG6rb7DaJpPfF5QoFfFCIq9ZNdTLNUaKsMyOlD2I7oLDjrovU4csgfSgou7yshULbDWjC8dFfuy6AEA1dYqMTEc76ni9NTtZU9TPZ-AM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94ecc8f64.mp4?token=Ptv1XfKXKOzOn5LjW0DcUuBmKPdvd24rodIFwVIaOR94EeKDh-t_2p_u-w32u03MdMoJvkQclEQ70nCC0WvuCc22YLWkcclBhydhan4xhCBocXKZjnVVu9JeCDtzX_eDy6Qhq2rVLPCHMori5QGHAl7-pXi0n1naMIutR3aAFzTVR5u0xQ3uGhCLU43Q1BNQITByqDP5q2EC4oTewKuFg18UV1WaC6ZbsDhjYBO-JoA1pW_rXzbg154GM0X9AX3qZAPQYD0-oc1kOYxCvh45I2iDEfZMOeN9WS2u1XH17c42Rc48lGvtUhs04-KpM13PDbyA3Ufuu9s9P91bqtp4gYcdOW1cgV2qgbADSz5H0hOpGKr5USe2dMCmq5WXD4mOiYL_cjiDqECL5Rte8bKal5KhrOjs1IuwAm7f7H1kQxHN5D8l3HBuTsFOAOorWLM2dEQs4H7Lw-uIv0makwgPGFJDHispAjh-3HT39bhjeaWBZA7ZoUwUIPGJOFDOZ-NUvlCGU-FbG0WKhG84APjzGWQHIINfvUZvWhH40_BQng4QVGN79MCfUslQEMDWqi9Y9HcmG6rb7DaJpPfF5QoFfFCIq9ZNdTLNUaKsMyOlD2I7oLDjrovU4csgfSgou7yshULbDWjC8dFfuy6AEA1dYqMTEc76ni9NTtZU9TPZ-AM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات استخدام نیرو‌های شرکتی اعلام شد/ قرارداد مستقیم فعلاً منتفی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/681374" target="_blank">📅 12:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681371">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a639a2889b.mp4?token=voek7Rwg7ZrxYEz6oYe0Xd2UEBRGhnEkcw0aqLCxvQ6sOGguxopVdZWR0zD1-6SevHm2gSdcZReKhrJEjVprjQVI_Stes-jVBXBIbjU5BoeihVNiPLDXYERhIuxGc0TUUSV5wxys0ne2I97k2z43SZBoMsnkX6DDpOOAdMjwpoxEY3sE4xFEOPX9nEOKmRxUeOdWtjOO73D3AAvClNIbOpXYrbaq_cJ5aHxze_ZcWn65g1ZkLhtlWrn1S_mBBLiWFyZp7Xgd4gRr4tJEuAKxq7ESxi6H7vC0fEB1owASNKEKaYf4bfPVNMiOhzUVW1r7poZ1vXJeHHxU-XJbwJ2law" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a639a2889b.mp4?token=voek7Rwg7ZrxYEz6oYe0Xd2UEBRGhnEkcw0aqLCxvQ6sOGguxopVdZWR0zD1-6SevHm2gSdcZReKhrJEjVprjQVI_Stes-jVBXBIbjU5BoeihVNiPLDXYERhIuxGc0TUUSV5wxys0ne2I97k2z43SZBoMsnkX6DDpOOAdMjwpoxEY3sE4xFEOPX9nEOKmRxUeOdWtjOO73D3AAvClNIbOpXYrbaq_cJ5aHxze_ZcWn65g1ZkLhtlWrn1S_mBBLiWFyZp7Xgd4gRr4tJEuAKxq7ESxi6H7vC0fEB1owASNKEKaYf4bfPVNMiOhzUVW1r7poZ1vXJeHHxU-XJbwJ2law" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر عزت جهان طلبی، قوی شو/ پیام رهبر شهید به روایت رئیس بانک مرکزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/681371" target="_blank">📅 12:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681369">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLA7bB7MlzIIh1AVrObuitkdoPvrYcFhqgUO9hN54qImboqbnd-XtmErJxoY9ON7sglDgZDNU0VlBGyltYjJ-nq8JaEbRfk0e3r-rqixj57d2_c388QIcEFwJflsU6M8ZLz9TkH0-APKDoMCQnqzLTtn9YW4JtPlMh2OZzbVEfhpUWIusRahkcVuy8pBAD97lNR5GMl9hkw2IRczYvY1detXg6_BUI_BhltBZzH5LGscHbvcBWH56s3D4mOMAa2al7bLhPyHNGb16oBbXUqhnV8s7zaTMt0ANXTgv5d9tMlTMpEO0RjoWpZWgcK1viq0UbVOS2xO32pA5_5hUT-gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه جدید کارواش خودرو در ۱۴۰۵ / روشویی تا ۶۰۰ هزار تومان رسید
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/681369" target="_blank">📅 12:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681368">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8eaa4b02.mp4?token=oGrMg8Hx5wAV2mJ0q7uqClznUGfOsIYPKsz2qywiwpvbwEa5DqbLE6d9lfuUvdXtDQBfIRotXXX5wFDVv1Oq6iva1PVgLlK4P1-NnDCKrM6raCUWpwNC-xgwhZewx7VaIYZLEC_jZ_hL4zf-k_Uzi3EslfBihS5Opr9gYxufLA36l7V0FiQm3kgeAcpTk2gzu7Ijqz56ECby8yRB84Dt5V1_BcoQwKw8J5Gq8k9fC0v1UzxhUb5Wlm2NmYNU2eFjdo8eaXBN6X6aZG6iE60HIhY0p-K2t0ceGJDYtWCd2c45jCERxbUUqRfhdIeuofKPXVbt3H5ZaTLp34yzazKDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8eaa4b02.mp4?token=oGrMg8Hx5wAV2mJ0q7uqClznUGfOsIYPKsz2qywiwpvbwEa5DqbLE6d9lfuUvdXtDQBfIRotXXX5wFDVv1Oq6iva1PVgLlK4P1-NnDCKrM6raCUWpwNC-xgwhZewx7VaIYZLEC_jZ_hL4zf-k_Uzi3EslfBihS5Opr9gYxufLA36l7V0FiQm3kgeAcpTk2gzu7Ijqz56ECby8yRB84Dt5V1_BcoQwKw8J5Gq8k9fC0v1UzxhUb5Wlm2NmYNU2eFjdo8eaXBN6X6aZG6iE60HIhY0p-K2t0ceGJDYtWCd2c45jCERxbUUqRfhdIeuofKPXVbt3H5ZaTLp34yzazKDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی احساسی از واکنش یک فُکِ مادر به زنده ماندن فرزندش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/681368" target="_blank">📅 12:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681367">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تابستان هم حریف قیمت تخم مرغ نشد
🔹
گزارش‌های میدانی نشان می‌دهد با وجود فصل گرما و کاهش تقاضا برای تخم مرغ، هر شانه تخم‌مرغ در مغازه‌های سطح شهر ۵۹۰ هزار تومان و در وانتی‌های کنار خیابان ۵۰۰ هزار تومان فروخته ‌می‌شود.
🔹
این درحالی‌ست که قیمت تخم مرغ ۲ هفتهٔ پیش تا ۴۵۰ هزار تومان در هر شانه پایین آمده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/681367" target="_blank">📅 12:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKn9nTTdVgJD7W1RcwGBVYIDdJJ2G7zZncKQ9oF8oQa4Z0MpHJkIwbWkWHR3C9tPUiQDVS0npYpw1A51ORHR2BF1FCMLKmmF-ePY4fmwex4yK6GkztEvR9ARW7yaR1Sir5j2wqKo5SB9ZCZzSCjkoqMz0ecak1PkbfAzPOoRR-RrIKjUn63ePht4yuQwoV3lMPkm_FcTnqe0E1RgcA1s02nA6vXXpFXC4PllfL4CP_bREkSiqF_aMdrwjN7UuSUdpIYoadmOh8xjnQQLgJk5jPvRseVD4ATNwKWpYq2CbjZhfsBOk2-NyYq6bghTeKY-v86j_601XfXPTehIoA-klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اثر مسروقه «پیکاسو» کشف شد
🔹
یک چاپ اثر «پیکاسو» که در سال ۲۰۱۸ از یک گالری هنری واقع در ایالات متحده به سرقت رفته بود، حین تمیزکاری یک آپارتمان پیدا شد./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/681365" target="_blank">📅 12:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e1d5d72d.mp4?token=Ei-wZDTDaMJthJRN1lqlIESDlpMvofE1_g9xhYdAgvDpHGwlhS2AwkAl99p02269kcBicCLczJC2k4X8QVw-BP_xBZUyv7Y3-R-bVBac0MftqpXG1kuBuQ5RGaak8glJOjDrToe_7xsn8fyZXgTfKNu9xtOgK0DcBdMHKUU-iaryBGkfQ6t0eVSGR1XLBte6q-RZxIjCFEr7FWM1t0PyWu0PQNzfqmsjqMFghvhFbxEs2l_sVjwDjSoKIhR66ha9bfXJh_enUhwO7ff48tjYbfZ6dX9kwNBqDK4NnCAXha2hieMej8KTn9iR1KXOC31jASvXEK7yk81T7eccBhLvmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e1d5d72d.mp4?token=Ei-wZDTDaMJthJRN1lqlIESDlpMvofE1_g9xhYdAgvDpHGwlhS2AwkAl99p02269kcBicCLczJC2k4X8QVw-BP_xBZUyv7Y3-R-bVBac0MftqpXG1kuBuQ5RGaak8glJOjDrToe_7xsn8fyZXgTfKNu9xtOgK0DcBdMHKUU-iaryBGkfQ6t0eVSGR1XLBte6q-RZxIjCFEr7FWM1t0PyWu0PQNzfqmsjqMFghvhFbxEs2l_sVjwDjSoKIhR66ha9bfXJh_enUhwO7ff48tjYbfZ6dX9kwNBqDK4NnCAXha2hieMej8KTn9iR1KXOC31jASvXEK7yk81T7eccBhLvmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک تکنیک سریع و کارآمد برای کاهش نشخوار فکری #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/681364" target="_blank">📅 12:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681362">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMT_qwycx5s0XSFvch3xy8vcWVKlons7Vqrr6mDW9xY10BwVal_kf_dpKr-TWZwwR6ifGCDXd05tPkRo-_uMOo_dVB9LB2tA0wCnyQK7f7VJo-5gy2lYLO9LPdeXfinOuvd9U-fYIGj6lf6dRfDlhOLBzhOAXdTpcTE3eRhm9S6qrYB0GnT-v7b5awj6_ZmIVo3ZinXbfVSkSY3rn9rIQwbrMS8OzVA5nMrSVKDgI0hkDvEM067M8xslj-bF67rGQiZGOjAtP0-RLsixd5kI3F4JqJJPTIS_pYQomu7QHTXqy3Bvv7ppjXDqncx45WDi8m_0XU53Xyi2xqu--JY5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ اتحادیه طلا حوالی ۱۹,۲۰۰ تومان معامله میشود
@Titretejarat</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/681362" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681359">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c47a7fe1.mp4?token=pBufGs4_3hrXeqoReazsPUnIQ1n2MQhDj9VLbFeHebmMSq31utlwAkZnqXHdmzJvXzF0rLk8ZIloCbYqrRog0BOJ6pVKG5-Vyu0dLhwT-C--mr50YohqsOAevB9apA47-gL588-JrI_Xl38hLpNfYrEgDjBK8kT-MEpWDqYGynvJRFYE_lo3n4xo4NC-fn-Aw29VXDaeGMEdOXxRuD5GCVKGrensj2OasQstfWzerT3oXtf3CZtdf7uhA2TBvP0m18PBr4Q8C0cUKG2-JOXNiYu-mnrhtTsBGvmmvfC6wvByG2OPwqMXMxdUcPEcqXPLmEyIlddlvJ8cx4k_YlKlqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c47a7fe1.mp4?token=pBufGs4_3hrXeqoReazsPUnIQ1n2MQhDj9VLbFeHebmMSq31utlwAkZnqXHdmzJvXzF0rLk8ZIloCbYqrRog0BOJ6pVKG5-Vyu0dLhwT-C--mr50YohqsOAevB9apA47-gL588-JrI_Xl38hLpNfYrEgDjBK8kT-MEpWDqYGynvJRFYE_lo3n4xo4NC-fn-Aw29VXDaeGMEdOXxRuD5GCVKGrensj2OasQstfWzerT3oXtf3CZtdf7uhA2TBvP0m18PBr4Q8C0cUKG2-JOXNiYu-mnrhtTsBGvmmvfC6wvByG2OPwqMXMxdUcPEcqXPLmEyIlddlvJ8cx4k_YlKlqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ژاپن موزه‌ای از علوم فضایی وجود دارد که به شما اجازه می‌دهد تجربه کنید اگر روی سیارات دیگر بودید، چه حسی داشتید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/681359" target="_blank">📅 11:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJaXkiUt92Ck4nklearC-5OiaSAQPXyShEw8N2kWVRDWfChEUbZK1Lj9ym7u2xt8pii8JhoR63gsZx2dADAz6fD9u6I-n1W--DneCAb2CTGJVH2ZIHWpm641ThGNGt99PQyn_qI6Ma154Uo3DjfawIm-8eCM0FE7Q23ln2C0GAyEBPKMhnD5ojPp9fkCnJxg9ZX_7BuwDB-5PcExatZ0f0tUvsJ1yo6jCD0TqCJIbYFrikMuGCBV8xHkwim8DlZzeSjbmD5cM6MKUr16bEG6tHazyzrx90ln5iTb4jJjud1rHNuP1vLXRSwPm1NgfV6rhlkVGnuYdal21cUKsZU6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEblpK9m11qILRQQnIvTucf_xHJhD86fe3rCFJhaLBO5roneIJJGeiLb8zXMPDj_bbzmj3iA1b5bP1-g7c26fEb-0cWOi_wGEY5ft_4XwYZveK-rloxZ7unDIVLL4-Fm8FtLpNFUlIxB6BS3BeUSw7Cz0F7QUJnlz4_dcH195N7yeUuACKn4kqzFRzIMtjXgCrqACu2RQc_NhFFk2p4jjiTPbLZQS4bvCHzpWaVShfaajsRkbUqNFaFIbLZCVsNbSJHFdsaR8gToEYeYiM7XNJqV1ae8cdYCpvoUnMcoiRMBxi5mJwibUAL-GY8rlqaj99bUen5tDhGgMbIlR5LKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuycZJePUwX4-ZBChZxbq6bn76vJ_6Za7SJcvLXB8MEdGkcRvV4PPUPNMOFrM6Kihb3KYGx8ROcRV1fS3Vu_s1JO3g50rXylcWmlykH7eiUhPpo2egTQsnXtrVW15XSIAddn_RVyqwZiThzGkRY6-GG0Hhj3JEGuCVW_h4Y_zkIj3AVUb42dADXmQYhrym7d4_8UoyKZBDxbr9REGUo53-xWT7hRLV1mtihH_NezrV6eMag8t9GQGYZ9C8pYXFF5YZHoWLk2Tk4Ka2NqMxfhjl8VVb2W40xWfYVsL5JR0IUDNnx_EdmKyusc93HNYzbbIDSW_HN1EozJIhyRs-Kt5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نرخ جدید کارمزد خدمات بانکی الکترونیکی ابلاغ شد
🔹
بانک مرکزی با بازنگری در نرخ کارمزد خدمات الکترونیک، سقف هزینه‌های بانکی را با هدف متناسب‌سازی با بهای تمام‌شده خدمات ابلاغ کرد.
🔹
در این مصوبه، ضمن تعیین نرخ‌های جدید برای تراکنش‌ها و صدور کارت، با رویکردی حمایتی، خدمات بانکی برای مددجویان کمیته امداد و سازمان بهزیستی تا ۱۰۰ درصد رایگان شد.
🔹
هرگونه دریافت وجه مازاد بر این بخشنامه تخلف است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681356" target="_blank">📅 11:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ساعت کاری ادارات دولتی از ۱۵ شهریور تغییر می‌کند
سازمان اداری و استخدامی کشور:
🔹
بر اساس اعلام وزارت نیرو تا ۱۵ شهریور امسال ساعت کاری ادارات از ۷ صبح تا ۱۳ بعدازظهر تعیین شده است و بعد از آن در صورت درخواست دستگاه‌ها، تغییر ساعت اعمال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/681352" target="_blank">📅 11:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
چرا ستادکل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا با هم ادغام شدند؟
روزنامه اعتماد:
🔹
قرارگاه مرکزی خاتم‌الانبیا طی بیش از چهار دهه گذشته، مسئولیت فرماندهی و هماهنگی عملیات مشترک میان نیروهای مسلح را برعهده داشته و ستادکل نیز به عنوان عالی‌ترین نهاد ستادی، مسئولیت سیاست‌گذاری، برنامه‌ریزی و هماهنگی کلان را دنبال کرده است. اکنون قرار گرفتن این دو ظرفیت در یک ساختار واحد می‌تواند نشانه‌ای از تغییر در معماری فرماندهی نیروهای مسلح باشد؛ تغییری که تجربه جنگ‌های اخیر، افزایش سرعت تحولات میدان و پیچیده‌تر شدن شکل تهدیدات، ضرورت آن را بیش از گذشته برجسته کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/681350" target="_blank">📅 11:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681349">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR1o7uRboNoGlnOkdN2HJQDHS6owiScxNBajlYb0MWRZUe85NsOpDOvcvWQ7HHmZwXYCX_d2fK_Wgm3JQBa5I1ilfvwEouObWZNNEUdi4-HmEVMjWU_CCAb6jRrIERhE8db27ipocDfBXZGgiwkkaMpIp_2Hxk-I4NGzHRrQ7is_ze_LOY_BcQJcbdLJJpiKGWU29ayx4rCvyCPDTOdIeMxa2UL2tXHDWydaYZAW3HpLEPVtMMQp2c7usxG-HCCZZWZAJHkMb3N3OGWUV42qmMdjwr7x6fr-ylYB7dP5x1WEQqQAmqdqI0b_QFaZlMk8nL8m3f4a63G0YBHGGMQhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
همراهان گرامی؛ اگر با کمترین بودجه کسب‌وکاری در منزل راه‌اندازی کرده‌اید، روایتگر مسیر خود باشید.
🔸
عکس کسب‌وکارتان را برای ما ارسال کنید و در چند خط، تجربه شروع و نتیجه‌اش را برایمان بنویسید.
🔸
روایت شما می‌تواند چراغ راه کسانی باشد که می‌خواهند از صفر شروع کنند
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/681349" target="_blank">📅 11:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681347">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آغاز فعالیت مرکز درخواست ویزای ژاپن در تهران
🔹
سفارت ژاپن در تهران اعلام کرد مرکز درخواست روادید ژاپن (JVAC) با مدیریت VFS Global از یکشنبه ۱۶ آگوست ۲۰۲۶ فعالیت خود را آغاز می‌کند.
🔹
از این تاریخ، درخواست‌های عادی و دریافت گذرنامه عمدتاً از طریق این مرکز انجام خواهد شد. برای مراجعه نیازی به تعیین وقت قبلی نیست و متقاضیان می‌توانند با مدارک کامل، در ساعات پذیرش مراجعه کنند.
🔹
آدرس:
تهران، میدان هروی، خیابان موسوی (گلستان ۵)، هروی سنتر، طبقه پنجم
🔹
مسئول JVAC دریافت و بررسی اولیه مدارک، ارسال پرونده به سفارت، دریافت هزینه ویزا و بازگرداندن گذرنامه است؛ اما
تصمیم نهایی درباره صدور یا عدم صدور ویزا همچنان بر عهده سفارت ژاپن خواهد بود.
🔹
سفارت همچنین هشدار داده است استفاده از خدمات JVAC یا پرداخت هزینه آن، هیچ تضمینی برای صدور ویزا یا تسریع روند بررسی ایجاد نمی‌کند و متقاضیان نباید به افراد یا واسطه‌هایی که وعده تضمین یا تسهیل صدور ویزا می‌دهند، اعتماد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681347" target="_blank">📅 11:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
دعوت طالبان از آمریکا برای بازگشت به افغانستان با پول نه با سلاح
🔹
پنج سال پس از بیرون راندن آمریکا از افغانستان، طالبان از واشنگتن دعوت کرده تا با دیپلمات‌ها و پول نقد، اما بدون نیروی نظامی، به این کشور بازگردد؛ وزیر خارجه افغانستان از آمریکا خواست سفارت خود را بازگشایی و در این کشور سرمایه‌گذاری کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/681344" target="_blank">📅 11:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681343">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDjT9f9BM--hnyKdJpUx8jRw0JoOMcaLDM1LpYHjohBV6aF17oF_TwIZEXtY6wrx216h8Dwm9-2OKUwFcl0hKiNj6TzW71lEnUC2-NKxsSn442y14VcPjr1j5-4t1-_RvQ_-PEg_oaq3AIlpmLd2mnocg22mRsRWGLEMv9WumQnmnIQDSgx0AOdwKOk7MFxUVIZ04E0IuTXat7Afl_wdS0peEVCFBFcIAnXaFTtBYnvpBpRSXdi72p0mUUtuiHSeq2ta9DVMKilcwUthFfGHU5LYZKrBc_YOkSqqAmmainNs_kHZKr2UlPm5JbPb1PKHsUhZwNUQoA6kp-wt5VqXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هلیا و ۵ توله‌اش چه خبر؟
🔹
«هلیا»، یوزپلنگ ماده توران، پس از ماه‌ها جابه‌جایی به همراه پنج توله‌اش در محدوده توران و میاندشت، حالا وارد مرحله تازه‌ای شده است؛ آنطور که معاون محیط‌زیست طبیعی و تنوع‌زیستی سازمان حفاظت محیط‌زیست گفته، دو توله از مادر جدا شده و مستقل شده‌اند و هلیا همچنان با سه توله دیگر در این محدوده در رفت‌وآمد است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681343" target="_blank">📅 11:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681342">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f8e5d284.mp4?token=AGi3GOVzLVS2mog3YeNXw9SdxbGw1kowl6PndabEEuXXF2q0jUFFWMe6IWv4m_KRryfdV0HXpG-Z_9QICFUS2gC_OeC8LO6geGZW6hCA6efDhnfe6rE2J9EwUvC_skdITVZr6mMm-bF16mUaXNmfy8MzH4PANGE3_z7HaIsGc_4rdNH0yrohMq7m-_MVIj2j6J3qVpPD9-1QPxtYoAVKnKi9bSiN5oohcIedj2kzPYVzs2j3r1i-MCvcF6XlvuZcyAGTcjdqRbffdeA2Vn4TQ1VmtHzLpAOVveNZX4qW4HgZk6b2eJ52POwwapA6lMvbkdHuea1XsT64uikog2qeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f8e5d284.mp4?token=AGi3GOVzLVS2mog3YeNXw9SdxbGw1kowl6PndabEEuXXF2q0jUFFWMe6IWv4m_KRryfdV0HXpG-Z_9QICFUS2gC_OeC8LO6geGZW6hCA6efDhnfe6rE2J9EwUvC_skdITVZr6mMm-bF16mUaXNmfy8MzH4PANGE3_z7HaIsGc_4rdNH0yrohMq7m-_MVIj2j6J3qVpPD9-1QPxtYoAVKnKi9bSiN5oohcIedj2kzPYVzs2j3r1i-MCvcF6XlvuZcyAGTcjdqRbffdeA2Vn4TQ1VmtHzLpAOVveNZX4qW4HgZk6b2eJ52POwwapA6lMvbkdHuea1XsT64uikog2qeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یک بوئینگ ۷۴۷ با سرعت ۹۰۰ کیلومتر بر ساعت از کنار هواپیمای شما عبور می‌کند
✈️
🔹
جالب اینکه با وجود سرعت سرسام‌آور هر دو هواپیما، به‌دلیل حرکت نسبی، هواپیمای مقابل از پنجره تقریباً آرام و شناور به نظر می‌رسد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/681342" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681341">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سقف انتقال وجه بانکی برای حساب‌های تجاری اعلام شد
🔹
بانک مرکزی در اطلاعیه‌ای سقف برخی تراکنش‌های بانکی را برای دارندگان حساب‌های تجاری اعلام کرد؛ بر این اساس، انتقال وجه حضوری از حساب تجاری بدون ارائه اسناد تا سقف دو میلیارد تومان امکان‌پذیر است و سقف انتقال وجه غیرحضوری و خرید کارتی نیز برای این حساب‌ها تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/681341" target="_blank">📅 11:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZcC7uF0OTF6vtuoTouAFgO99jD0ypM27jOZ0zEGxdPjBprkJbuS7JJutvqNGysEDzN1RVMpKKoHt9mxm7JyPH5DTpcpjcWaS4ngYp32eL0DdbLCkzAOur6T3107-G6kmFIUxHZJ4gU-5oT8qgR1PsTbRs8wIdWWaUMmcDRBHvyDk-MOg5WlZiONa3i3urJ0Ute7ZfbN90WaLSsHQQTpk74rZr_J19e_ZN6WO8j7mTd-8glY6Gq8PSkFmRkYiUs67WQxTdPKjqULbwT55yNRS40lEFkQXYPNYs0fwJ6mhjlS_NKyEnD-yfUlahmX9OP2-Eydaj4sntJPphs8_BVwAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7dVV_KZwsmFZebBt_OsuhBI_Qd_OnL3xGArwUqcbn8O6i6CAcZ2R-czXdbYT5hwIbsLc7fhab2cNazDnAIb_E0TmhMrs9E9-t3m8gbxdWM-MLT3Voi_Jn_8T8vFIPo1hLVbzWOnLcG72Vzec08oGFMjiqPTkJEgazGWUQWTjNz7NBs1yl32idJueq_eu2rH-oxOqTPHfvvSRd2yt0Zl4qsaarTLE7zUp7K13weUj6TfxO1hQYgrOMfw1NHzFJn8HvMMQzuuCvq9EjwM0D7x3HSUo8sZPf3UJ78KusTDqNB9t12tuTCLdV8J_HipzRBvbjWsywkhThulyWP9vjO_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQIvmZgd-BT-jxU-Jgpbx7NStsnQj5hI2bDAvqM4nXo1nv8OoWgNvaOeeSjWuJK0NAkQT1o0uLv7Mrr_IexDnRTAd9TWFsKsgTFnUqFj9Ks7qCBMhe7GV4WYk1GerqBBf3eOhP5T58j0fWUpMxrjCqBD6kVTEUZB_e-fkcmnhbhaVvPDkhlVat9nzYWYRrwEKiY-oHeAn085NBPajjHoADv-Ibv5iwQjWH58RdtZHrjqahVY4w8UFM5538AO8_bT2EBaCvIncGJ5lKlQ-DDqKQ2BBVJqzF8KRO5ruN7dxAaI5Hx_4JHeLT4tJYg4JQW9XSsfRkxexOhPAqBLXfe6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GD-w2vzJQW5nXKFOk9NW0wQVLGrbo3HOj6zn99n6jq2EHkjdmeSPN8lqJv4WOFn8qamerzXQLBUD7CNv6Ts4tcCoTm8i8-LmwqwqyMKeJgt8tUZLJ_kaA0dfKGFfHK502tx9AHRwByHAb3VYM-3NRnWn0sxnnPMVLipxFoBYAioCT9rKI8ONBHsbOO3T45YDTdMbzGuP1YFCFWkhCUgTcKq_cMKndbjLv6MvcUMkeqOJnk7uYNhxJOjOBF5fMrkQi14_qUuSqs9a9fRsc22ZauwvaSQN3MO5eiN1GyNvT1ybnd5MjkHr3eM8orav22a9c0lcxQ8LyWMOatk6xxaGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3f6s-CGOeZgPz9pSoGOH5qgoflmgzeNEmjbhmbprN7m6dVjp121pJ6Xg6UtJN4F0V8cAzhCIVX8QJ1wcVbhgpFjTPVBsbs0zOqDFr2ejXsf0GEcY-iruDa3M6vhCiSfuWNdZTYJfM8rkpYtmCJ-MLPXPQsq_x1imL3Iq0Dj0bGUlFrghlrbV67pogMKWyDcJ9z_4l43ZQsqZvOHOurLTGq1lZtYAOEG1rhlHoj9ROMtX3sC8Fd0rLivpIrXIDt5E41ALm9V0IDRZPTZnvQcp28rlpHvrLSZIe_hc5LupcGrWZcZQ8WL49Mle6zeH1j5CjbduNZjqJ4SQvSUEMzbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTd1w1FaVfwLx3rs546EXNuUuF__4lpCGE_QfBaUKezlCVmwKHOz-OminyAuvc3Tb7LlkyKccv-sw21LZzM7R1hjjLRmMMkPA9jb6lDKb8gBgivwB0CF5m6c0NbOOVH6bp8VAk-X5lFb1ynHYF0K4wQ0sALjwwjroisQBRxKtOycRyVkclLXkZ3PyQX54itOwNnWyxBxJHB0u6A8tu6usgSvXvALr-WyjDJU0CLkGJKDblq3DyUyH7HrcfcEwMEzeal1dp3K9-iZe3vWGITygNDf9YtYGICshtjSWr-_LnKXiys_rTe5qbiW6A6NIVqqp0o1u2G4YBAQ-wHuHxj6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVcP5nXkny5pVqFwqAdkvqDXMuju9Nu19FFp0v-p598UpqIY-c7V_zo1FPe5RP5Z7NQewzOZpi61pqjanRAH4UmTAsjPfRdyNXQgkyrnkVrm0rJdjZCBd1NX0bRLC9EoYEq48Vy1UAIlrlv5CJTTO65kvPFbptAVtx4oFWR2qubjtyukXOMqGC5WaejoIgxC_t8lAot-3mGS58jwdV4QbPzi7Fs54y3vj1Ld7FKWV9_le1C4L7JVpm8JDAYQAsv_nxTZKmCpknKLXfzXcva0aiV1ToyK2iy8fvZAUogEp6MwwGDGj3GGixwV-1DI3awbQeUK5CXGbI63pPgUr6FlOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شناخت رنگ‌ها با الهام از گل‌های طبیعی
🔹
در این مجموعه، طیف‌های مختلف رنگ‌ها با استفاده از گل‌های طبیعی نمایش داده شده تا تفاوت تناژها و ترکیب رنگ‌ها راحت‌تر قابل تشخیص باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681334" target="_blank">📅 11:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR8AvE6TZA6pn20stcGTND5S24UJyAdNmhqDLh340vXwBIs4QkZ3Npq18saocyKGIUCJV-hkYsUfWJsEM7rB0C6C6rx0sBBwYzRGelM66txWp4Je1UlaHvwFIIIkg1jiIV9PozYKmgBlL95aiNYavYtFdSbHuRTPH07tWHuWoXRT45mKc8gv6Htx76YI_khzzSppHyG4X-Kb6PYR_enp2-mS6jfX3z_FCTGYm8cO9wJ5_a0vbY5bIvy6LB0VwLmThK_zBi4LrY63cpY65pftDagoeDqO0Qc_pKMnoJk0GYJz7quSkMeGNcjXuuG4rwTpT7x358g4XKzdM4KFdmvk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانی‌ها جزو ۱۰ کشور پرکار جهان
🔹
مقایسه آمارهای سال ۲۰۲۴ نشان می‌دهد ایرانی‌ها به طور متوسط هفته‌ای ۴۶.۳ ساعت کار می‌کنند؛ رقمی که ایران را در میان ۱۷۰ کشور جهان در رتبه دهم قرار داده و افسانه کم‌کاری ایرانی‌ها را رد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/681326" target="_blank">📅 10:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681325">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2576faf18.mp4?token=fnTpceOCLSMt1kPLDFxGgO3yETXcTpMZNtnCUFuE4SdYv-lwPH4RzM_D9d61ASpT6ArhJa-l3C_DEYt2S1UK8gRZF5XMVvo4v7c7VvUng4PS8Xb2E_-nRPc6DK96m1y3sTnX8N_WOU26vuyqhlcTgrTuTMRH3Xz-TJbDe0ncdNO4vTCtYge-2_g6ntzV7ToSa_n7a2zynl07GEIRSZjBGCEeDlCa4fdsgMM_diRXxhs6TugGgfnWrUe9JAeOrCC8I7UcYcy9wttLWrqMMOlmr71T5-7hIEmsSPnKX7lBlMfdBwzHJblxD0lktt7F0LZ6p2g4foi8OvaypH-pmdbghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2576faf18.mp4?token=fnTpceOCLSMt1kPLDFxGgO3yETXcTpMZNtnCUFuE4SdYv-lwPH4RzM_D9d61ASpT6ArhJa-l3C_DEYt2S1UK8gRZF5XMVvo4v7c7VvUng4PS8Xb2E_-nRPc6DK96m1y3sTnX8N_WOU26vuyqhlcTgrTuTMRH3Xz-TJbDe0ncdNO4vTCtYge-2_g6ntzV7ToSa_n7a2zynl07GEIRSZjBGCEeDlCa4fdsgMM_diRXxhs6TugGgfnWrUe9JAeOrCC8I7UcYcy9wttLWrqMMOlmr71T5-7hIEmsSPnKX7lBlMfdBwzHJblxD0lktt7F0LZ6p2g4foi8OvaypH-pmdbghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری که می‌بینید از دوربینِ لباس پلیس ثبت شده؛ سریع‌ترین عملیات نجات گروگان‌ در تاریخ!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/681325" target="_blank">📅 10:49 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
