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
<img src="https://cdn4.telesco.pe/file/G_wCbs8BWU0C2nl5NuCqMlHG9PdTL_uDYsRduZM8alQ550Xe-kUonwghcU2-eh6UDipHFBZsRDKFXeBk0ye8RkW3ArGnSFQ31GAs8anRvJSxRCUYyQsq8y0a3Pf-v12WxXoxur0yveGZ2xUUe4pXy93JfWm-HhSqlCXdRHC5lxLikLLn8jvxcWcRAKtfHeKdN-U3FG1LhTmR0uDRgZ5kXhb7aaIT03Tg1HtY7bigW8hg5tZ34cJgZaqcSvO3WTIFqKOk62w5ZCtDiKU_a_8w1XGJ90N7TK3XKWZZuhs5sXBJ4L7nS5FK9kbVi6dPcheD_wFk-zHroE1V7ftG8pmN7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 181K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 20:58:16</div>
<hr>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW77n8e_ZwS-Pb2KuC29uSKvyAu0hp6d2T_VF-qV4f_GrkKtQ-WRAmEOWodb3W4IcI-vHKLLk_gfulvEZmNYZzqh8y3qiOpw4naYUSD6MP17Hhe8w8DCO_bsb5qS79jic_aM0UXWZ5dhHG4f8Iy3U63JvxRTur3T2DzM64vGJG-DQOHrRPi00OWsbLbCl46qT3kZzP4poDx15tXqf0LWkmpeXzajVhG_BjNQEvneUiz6TZxx0rVsETj5hGcXdUaK6JewE3eFaN3QklxR6YCZOXNHJEAcFKTgGYOZRW1JOHIVYiBaF5vcYrSWgVCFgZ_IGRkAjZOb5PaU3sFmsTKwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sk6t0D7bLwps_wajIZRz29VklLhxHcXWwc6U1oa6cONKUJi2e7AShNWduJUqSOfySMVjSTbYitC1GYfwTbsLfWw-gt73PIYLyfHH0fJC1F0XAHHsTE84fF8-NdG-X1GJM8nIBh8PVkOORt6bgsGHCzWCp2ZXYigFOUweSGYOSE4D4VHge36sKJL_7hmBx8Jhg4ircjFVVsLe8kYR5tWF8TAOREkSL9t0PyaNwlZ-KtFEC6liFTjVelE0JY8xQ31oR6s-uZKvwNtp6EfQmBE24KTI_SITFIAdt--E5Db20ZV-cQFs75kMMTXJZCDjdaFgevCOiZDsyk3uZ9Hc8UE8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان‌بدون‌واریزشرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/persiana_Soccer/22434" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaKsqDwJasLNPJqlVTR4JVElWmdZaJPNZVtfnjNd-iob7xzN3alBy0wrMoDeS7okjDOIsADAlD6DuI79Rsol-6FOG3Aj5giDscYnHxjdC-FtHFBNI1ZTzDPVCv_qsds2embHC-YI8H4e8ll_90v6g92SzACsQXqia4GyaenzIg6KWKonwESyptaatooLzxOJBiNAtr8VNxAlL2YtRMPObyWGVLn-UcmYvs1W6C9bPQSTRUt7ykCkX5dX-X4p5xePzlBqr80hF-L8zz2eqAnrHPj4t5QDKiCCDoqLncF_Aao__NeQWcb15o4736H9yAAEvpcdAqPSJ3xJGCH7yvaZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwjgUcFSFOFPzKQrM-yClfi2ak1tvJKKlytZ-2sRKXnolqtfYnUER90pIhKWVY_VKq6DOAAbq81-_5PcnC_9s6P0Mh4RaV48JCrhUMUo9KOPPEn9k7ULDMpkeWHiGnmeOmF4MxsQTTQFqNvue4T9ahZ0rJlXadqKRIET665V7InUMfaHOTvnoRtRYC2KSqOqaut6agLXCTy5_thAw82b82_rwd0odpBjsHXq7R_iCAg7lg5vuXYcS1HqASo1mQuMt3-75DcXtVFt9U9XZ8G_3T0_0A7PKfDwTjRqn5ft_yg9dY815hyRwg4ddqMmER3dUzmWuSvBcB0Bdyy_g0gCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgBrESRFP9q5GIeTdEOGNqn6sTDoKUlXBqEH0VZejMQocHJv0d740VvfeaH9rIVIDos8IyHIMz4Pw01xWBECT9f6eWkOFYZ57yWZGVNhO32tUJaOpKFXddVdiKXkTmdGOwToTsAGaXVNYbrsStZmHbtA4eONwYyg0A-Hn3AixAj1NlnqddZXK8NygGmcxixmB7TfpN5aU6DP7TlrR3zZuw0fuRmYFLV-KZ32AeQu2RTN3RWhijZzuUZaE876Hex3Bp7FAQ9mkzP7-1t2cxR-c5AjT2GlUtULgYnehh6PoP60QXl2hHxq85PskrX4OCri4fTTufalSnzM9RspGpXNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7qVMwCp7dABu3R1AEFPC0jamSJDVlFOv3f85jGIuhyJrRdViiUOZEyd07rtgmtolfTd0Conm5tWvI_dzYWJbvW4LuymOi-nMgwowgtP59_buWHp5Q_0MdHPhxAPMYZdh1b-JN45zkVjcxbRyx7D2f98Yr8YGRY1lrbjwcTHP9QtwKvXB-tkn9sRSL-aKBW5mH03VoCgzdkJQDjhBIa0En9izrt_JcKnmBJCURVOvF0-Q4dneqZdiyACYsYYKakfU6uZ5f1b0OfwISazKf6SN5TyXecfyXe-eQsEThDRzQTrO1AiOonEkb1j-qJAnmdjf4i3b_58BqrJAWr2V9cLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsNPDERe-6HhVbcImpnQOs86DRNEDnLy4SuB611GEG8j7ibsgyQYHs82tcJpHuuT5mwVEeY0FL4AEt6J_ph93-gH-EjKlxdXswLWdJNUHR-p-z9_IK6kldzTJ30vUQ9cg1uWF9GXJ3IFmJ96NqovIy8KY2glF-kc7LHN6FKxozkE2K_WVbzdxpTla7xxxn-Mwkno2gd1YsQbR_YM7SQR45RflrsgIoW-AMTc0rW1F2IVn46bbNarui6gUDCGzTybBaAeSNd5iv88fylXMAiC4qxKRSrw9RdEzg1_WUN0CydPW7ZgzM-zemwBZ1pMewecQZH-qrrNPzdIHJBlf965Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBrd6wfgM1mT-JfHt986eUr_FekfkunGY1u_F7xMjBR8osUYOWPJDMSfuIx5oWjvY3hvj3Rd5hYlg_g-0GwnbzC8Mhb0smqKnv_9DpM2u6XcdgFh5hd9OzgLiKOvUJ5oQOx-Dd8BEAe_6EiZhb7uru_8Ezh3RfdXiw4oZTJQXRptmdeMiDES_RDguj1-PsLlFRxEQbfch29yhEyQyfzr5krf2nBvIGY13vUFZLiNJF5oj3QbHPcsaQY3zn45dMEkqc2v57bdp5MVdMxM0gcqjryxESajnfmIGountolJchOODcT3ZRVFWeZoEiFhxTIG9poMBCXw6rx8-mew7pEH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHkZE4Vrc6Mf2PYFRK260rshwUXmMHerr67CuDAp9XxmBNxFi1wSj4yXvoZhj7BlMcK_GsQ1yZPjl2P_F9hx97hnRJolGGesvOTOjzd8M4KY4kLEQg4jixCQgRYQjb3k64x9AYwIZOCYoYBqrSuhwFu3kS5laJHQsgLP5gIsGTPIamTqEq4OVBdN9BPqPU-l5WLNyndLgTRjBANryUghScM3wc_JXhI7Q5tbEVKcSJ62ixKjM0czp7tOAhxFtfJFGCXSbPJ5Y4w9lhF6O6z-nV0uPTmI9krirrC9esBczy93rMW1vKMFgh47-hmHHd8SAFMgmU88IjrQk6CSQlwDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA2QeNw6AQYtn59xWNq8LZfiFn2I-osK2tHQRtVacn_vgHrBRO8IH4DshTc2N3DrKMDK83XZW8mkPBkJMiH1gH25sp9HAVhFDJi1Wk8sfPyH4enJOMSlARiRfU4h3sUjxxVjElbObBs1B_Z9y4J9kTgbnOvAceGlT5vzh1qISIEPjCFhZbpK__6BfcWL1joUbzwkshfU0bET9pUmDUW0qmbUfxnKlgK5_UAZtPg_DuFhUhShrHrdY5j5fhKCarPjdk2RDflZO_-vNXlht9bLFJln9nsSZCMgjqufcYhqU1-EF3AAPB_iPZzF3sl0Gl7QJwiCpM9ljzqSwuD62wqrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4m45Yt3X5m91rb3bqMPtd-FgRJjrwmmvppRunJOebxfp_UNyQ3xYV0TBWKtolNwxHtlfdUFvmsmkll00EA9fgPEE7GerBwhS43IVwu68HJSmjoPk9fL0qom0ET3safwaaM8judu67LYnni2RxX6ELaKd1aK3deApB_8T-61R-VGIQU1Vr4pQ54uG1K6okPlswqvR75_EFJq_CIcCF6sR7c0E6csWVWevlxGPjpTaBVrx77cOMO4FR-NBT3fykO6t2V5BD84unfutcFT040lD52KwCkspT_FLZhbk3v1yxtrUZhzQTJtkOFYnuTjhS2BRmhvwATM2jHmeG_cONZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5jpgXcipW6z4Vwg4OAETnl67lundILyPe8hYIcXLj4xOzr6Yj--9avJLLpygv130LfkVej-M3ghLlvZldNSPG1wYHhf_9gu6Su63zIHOS1Qs9kIzyKnSwy7A_5udfme49vEka8tpdBhyvPWWWXCugxeDDrQvgFdWHBN1yvnzrTeeVCFEKUdC2NQ5FrLzZ7JyBlsXT7PGPowTdfhjum8l_JAXchchL0NsEUz0MSNaf2BHOxDcg8dxRs0IpR3vznC6Ur3_xcWyVpF225K8JdIQ1qqqTSUIvl73iBAo75R0CtTYFsGvPdoy3eiYjjvpHj6p1wCcGriGNnEWq2PbRrpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq4b441M34tyELi16tz4F-N3OHz2lzWN-OK3j8ncDJ8TQcA9AzdvkP5ad17YLaxZf7y1KX8EcWswUseL1uqExrWLpSZNfSr5B7SE3E2ItPDK5OtFXpa_KvfkoBWC51lE1e1Brx0lg7VDAf6PRmigpv1um96Sod9JAF_2YJ0evzFHGZu2j5-CzQgErhmqiFf9a8cixPaRUCvnKmDAfUwfnCAJ3Pnkpc-zsuT1I_Rc8R5pgj87uqDUOlVUbpjagr1m7J-yGX0qyGSqNDaKdmLSCHQ_a5ndPTib7DNlLZicy6KUJMjMkyhWRX5ULhgLmd3XykIw41hq-0d-6qquJTCc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uim-hmQB83m5MwaH5enr-yZJVVTh3gmBOfoTUZ_ELE6RcJIE84yFbcwVDj-LKo-fBDSqKEskSiokH2Ed-AqoFO9M3BtrXcDFO7Zt6UNbGO9hnal2EtrnMadc5zUs2W_0Xuc7cTwmTEY6XaZ6uKRSnjymsh24HoKEvksMTEFm9WadL2NEdtNW-EYup4_w88nuMt5LPq_GdrSHQNXx1izO0rlo09L2KyMdb6sMH96_U9mFf3jXLgelIw8g5p8O6X-0bBGDuM1A-ATU5HGgUU2eLVf9D0r4EDEZlgfJmUf18hbCYNcxWaQ0ClVukip-kzBIt-fkXdwLP-rWXpxcxCrgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej9myXIU1TvvAqXoWkr48rV0TAwQ-6FYBXgezSnUZh1W9ULuQoWUIKH-f_SPrqOiEsXxr4985HpxiwW7ocGmq91QPBE2aH6Eh4KEAxiK5eOxejgjQ4SyZkLPtmrhpy1IjbuiMswTGTlk6FQPWeJpZ8pglUPKmplZ-pIMlhpNsKhbcmCADvcSqKadwk6E-te8VcC5e2oWTT7qFo8PS_d4GZ9Ewt71rhDsz-JCYwd5_FWz0gWsq4kbK6vF5ROiSfRDkxwJ9TdM28PSzMBV4Fdz9XNhlRjX-lTje3SOA6SCfbsfhDLQ_HicWdO99VtdliIairROo_NZUJZ_5-We0WX-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djM8NsMnK4eKisCZKTOgSf9J-INEKfyRLkYdMzC4EtIunnHOifZmRjVbKLOBhuj8p6_RC3ZflDvnDFHxvbOtMZtldyp14w3___FxWgRsv72lGhcghTCvBoEMhOZGKERBJ-UgGdzhoUjCzoWdeLXdnTZYw_q3dlTdV7GgwhHxoUKNV6qx1xEg6YSVkrbzgF63mHKhZVHnVPgs9yV8PJV3Qi-EQ1UzRTP32Npy2SBHhaXef3GkaXNyEBY180zgFdeQVB2Bin2583GZrKGsuQijOuxqoWtx6eOeUW4IO4b8b4_ymc_NeL6DXwxpEXhh5vHcGzPszdJjbcBA8_jLkSExKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhVw6WSP_THRF8iiwjGFV_XTo2-T2RZB2tt-Nzytp9o_I8qO8QibLl_10js4SF99K6UyNXVx53midcYO-8EP62OIz8x3qFalxUf9dfBK65xoGPFG2gUW6Fr7Tkp-FawotW_P8HdDxR7FEbQzgTpXmygmSxmy1B5O4JSnM0qQGjwO3qkx2F4MAq9PwWi2p5dd6B9Usm8yn6RgP2R3MIcv2eImQhmDxwR6nv_qBV4kS5ify1Ukcmd2EizSKuDYIctO0V_X9IpUk8qWsW9-RVcYdCCvGLhVxPkU2BKcIgn3qwWpE_gZR2G7ueCzbmVqJwPLyPKgm6JzKG6JFyWrJ6SFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEAhzTdSCwalIpWcUUQ5xrPv0HcbVoemG9sWDZDBNXN27IaITR-5kFGioCt2QntTFqCxnudE6lxbymj0bOEbtznK7sGLJzRwO-QVwLG7Y8X-ghYBhtH9IcxNmArQKBvZwt2Oz2aOO3VohD5Ase0SBMIebzGqqwsFYJnop0vTT0KFZMpuwp5kXPUYS16CvGj5VdJjIB3tkO_0zNbJvUkWtmmTMzANjIw4vRO2k84mqoxgIJpeB6_6kvk8arjl_LPcUS6U5XcadmbJlmFXFwqFVjIPC5T62SGewiphoXuCrT246X-zdx9h3jqqH9_85hEsQiaJ-yjIx6XaE5ZoVhHSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgCDfsZT0Y3dc8T6iaoGeMEWg3QudUuEm4j3affHhSeTOE09OQ75vf1mQGhCIHBpE_x4j4QFpZCDrfBc-yb-u6KWwJhHPxX6vhrKZSFNeH0yDHYHOdaA-BoJgFQE-NpN80H70Uj3XjtQU1hVpQHa_1Vk_z6TdN6OjpTJef27d1SR5I1M1NCox3ebdTkg7WPd1DN5-JR72uLvG-VC-17tUsXcqU28tBzJlBq_955bi54LHwkwlNcJDC01JtFZiw23YenUJwsBw5iU4p62aqWk_5yNBLlZk5skDIAQyqoR6Aa_mA6UmBiuNJn3eXkjYeYw4bMeDYK-9vtVXVki6K6DSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI7rrWcaQCPrbpOcv8uxyvD35a0wgge0srchUkaEBNlzDKJsIgOnjMxMbVGQJkXgMr7uL7V5zj_PtrsbJDE7oUV1eqSKKsmdd6pY99DxkJMdqz6fBs11RtbpNnld9FRdtVZab0J7SRQ1xFF3TBLMwN2G7QuHuzkGXSGf28cq6O47oHcR7ReKZU9lsmsw9noQbXLrqE9He4KGo9o_QhcKlwv-VH70Lrualm3mqnIcnZc-UQGKzwaB2Jl1t2CIY_dCbZiCxfMRm3WSuiQWt9Os6Krfm02ljPK1vb9blzCjf_u9lTVunKHr3AEcGIh2kfozfqf2jAa-NRMC3zHkhDPuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰ هزارتومان بهت میده
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22413" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfkJXdVRy9CW_JMITsWKbCTqtY4gtIrSamvbO99_QoNZhbg5Sr2yoWrDk0yqYWwACujQVPfg_vSjIAXqCmqcpShXp2u-hBimRKOmMZxxZezCE_Q-wjQxtvMrU2mW0WBxM3SiHPbOj_C3Fms95sPpCRqxxgoLTcyXrqUbDBEfjt5DzftYEVIhZtA7pPqcXtRAB85J-zoyfUrYb9dCSPwVr8skxh5aXutb5RIJyOGvoXojU_OY5YCZtr-Nib7khfcBgxeBicMiYyWUDMYlfOiWsPAdUpfVkULcouxVTFyA7MDKQlx_3T8gUOJeP0mxXk0v-NU0s0hzJ5CO_gjYQI1usA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=MtIL7rrTqhi8tj6ABFgj5ENoITjIesx5XuBXTIHHsjhV0pVIBlHKnPZEz3jSVhV7zw69m4J0qBQWJyG8uVaAFPvuwb8Yu1oZmskI1ovqNT5qhavJzvoi4HYpq6xAWmjkL4zPP1R1lJxdbETIFtaVtjH8GjrnCIuBr3j43jiWL-Eaij75rwJ619KgoKN6SsGW-Q1MDF3C5r1URdEF3_bvk9WiqTAh_DnNAFkkvcpLBQ_H1o8USHBxfWfGt9bPPYOYEtyvJ5TYMI_8V9OySdwAUhBMnhILTL4uH6JXwFCGuM55xC0BlBPvajygUeWpS-WbKGzVgOCNxloXiuactTBBYyP8wjW8XQAOXOYm1CtxEVNq-TGJHf4J2n199jU_bVcCgxzOTqyki8Rt2xnfTDTbBi0dUnTva7Md0XpVgR7PQn8Wdo7ogcsdZq_thPKifyOT4aMvxfhCGgkqVLyyeYp_mn_lMcMiUbotSp1v1WgxAMlLJyTXzLjTvYt5Ha6aR3Dwg7uarPos2yE0kBh21QlK9yIDaD5ptQ78S7C2675P3CXC4NU5k3s4GOgd9WhvNexu_r3657idtEfS_FlvDlk2OP4FzPbFWu7jYZyY5ROyoNirOu1i6RlU47Bp18u0tnKdwEjFTWttsS6NmXw57moSHUKd-FakGNQdCUkmi4KQTOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=MtIL7rrTqhi8tj6ABFgj5ENoITjIesx5XuBXTIHHsjhV0pVIBlHKnPZEz3jSVhV7zw69m4J0qBQWJyG8uVaAFPvuwb8Yu1oZmskI1ovqNT5qhavJzvoi4HYpq6xAWmjkL4zPP1R1lJxdbETIFtaVtjH8GjrnCIuBr3j43jiWL-Eaij75rwJ619KgoKN6SsGW-Q1MDF3C5r1URdEF3_bvk9WiqTAh_DnNAFkkvcpLBQ_H1o8USHBxfWfGt9bPPYOYEtyvJ5TYMI_8V9OySdwAUhBMnhILTL4uH6JXwFCGuM55xC0BlBPvajygUeWpS-WbKGzVgOCNxloXiuactTBBYyP8wjW8XQAOXOYm1CtxEVNq-TGJHf4J2n199jU_bVcCgxzOTqyki8Rt2xnfTDTbBi0dUnTva7Md0XpVgR7PQn8Wdo7ogcsdZq_thPKifyOT4aMvxfhCGgkqVLyyeYp_mn_lMcMiUbotSp1v1WgxAMlLJyTXzLjTvYt5Ha6aR3Dwg7uarPos2yE0kBh21QlK9yIDaD5ptQ78S7C2675P3CXC4NU5k3s4GOgd9WhvNexu_r3657idtEfS_FlvDlk2OP4FzPbFWu7jYZyY5ROyoNirOu1i6RlU47Bp18u0tnKdwEjFTWttsS6NmXw57moSHUKd-FakGNQdCUkmi4KQTOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=sN2X7RVm7RR-z27ZpaWBP1CoWC1UyMo8-zZ1i6nwiYdPpGZAtNMAv0vmYiKOjHI-IamKBiCT5Z6hk71NtBiWsNda-MG_hcvR3ipl5RdkLgJgI_H40mYAMvfzEUCszWO3YimR0EgS2W0V883R2iIvLR5j08owKRsx22U98me3tOCNV_DNNvaozirU1UVhHHL4Z_XMjoBRZJ-3PsaRmdej83szpeb3tm2ou7jWU_UYvurNLw0njz4hydss2DnSA9rV4khAapmwMzWIPfd7ljRkMuDs8JnQAqiUWjs3pbUZvvuYcd20a6jt1EbhUlF1lEKHM-Bjj9WZ9Jnwyzs-FrevQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=sN2X7RVm7RR-z27ZpaWBP1CoWC1UyMo8-zZ1i6nwiYdPpGZAtNMAv0vmYiKOjHI-IamKBiCT5Z6hk71NtBiWsNda-MG_hcvR3ipl5RdkLgJgI_H40mYAMvfzEUCszWO3YimR0EgS2W0V883R2iIvLR5j08owKRsx22U98me3tOCNV_DNNvaozirU1UVhHHL4Z_XMjoBRZJ-3PsaRmdej83szpeb3tm2ou7jWU_UYvurNLw0njz4hydss2DnSA9rV4khAapmwMzWIPfd7ljRkMuDs8JnQAqiUWjs3pbUZvvuYcd20a6jt1EbhUlF1lEKHM-Bjj9WZ9Jnwyzs-FrevQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8j7lcbDamyAitgfrvvBP9Q3EKr45-RO2_0JzvR__h8-xomCbaPfKZUwoQUgiQzvP2RIsRBV3TLocpV2giG9nkfeLT2Yk6UmI2kDcNe491vUyRP8ggBJGoqpGWWOd4NAuBR1tPGWLIjdVh6aQ6MkWndG8wbzujxkDUzhDRsdQ1L4iXNyLMCjbaqUjWZp5FNJx4hYX6xlq8Lfhl_Tnz9R8CXtD1DIC6RM7wp-iIVQ_niY6Uab39PuBmThgPFJFhG9SfBu0XIyF03AGf4uQ4u_ts_qvr4vUcm1boRe16zqKmgwGWOb5LaLSFeZTOuYVTy5iMu_-8qVCaTlHC_OxfhXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc5xd_IJ1FrUq9wCKiTLeOHdY16W8_YaYeqSYyChhbbYME4HGEFHyBS995OMLiqP-qriS1Wa9PwMGpaLTzVXgTpKnrb3OqpR9aoxIHqwYq99ekzarU9IaMBbt9y0dD5OB0hErf7LchDDXwjYQkpJFNgbGajCF1gpANgQpweF1x0fK4jzETufl3AFvcbG4oQ-ihdci2jY5Cq3EbDyrp49Wa-hOtKxGR0yxL3ozJNjFQhQpHSb8_-uslA6dD9tyspVVJr11Kku0dBZFTNTjmHHdXvQnm5FCh2ssjlHCHWUY853eH2kMd52vHEawO0kQ2GQWZJypuf--Cdsh0ZU0zSgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7sVxc9lQeXQGC4hc9L4Vh3CgMwXP0_017w9DgfHLlo_hp0bpIXJxK9TpAdmn7pRMWcqIlLcgYeE-0ljkAH8OTyUZwoPDqn18z-j_JijdoC_nnx1P7YTaEM5q22oH8iOind5zRoUJTbhth1PbfxcVxQ0bNU5qoS3JVbJhFW-lpmTSeboSVP_CGMdx24Z5TbIpD3p-CwrvO2B8z0LwfvgRUU9SyJ_Az_HkEpwkx5onqlwYGXMU_cvuoMSNT_5t3gauUL3c4siRUsPD3WnnIvtdknUqZ01vgQ3iyQJirhZkG1_m1vaNVt_c9khpSLFlJ6gpC-A4A2uGiooehcwvEJmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhztGGHv6SLjhBHYcij82yA3MvpwCjeb1lVHdY9HjzmSm59bMV-JLI8yWDBTVOteoQJhzfKrXUEUkjQjcWPm1RH2NDCXxHj1sWj55HeNwj6sWOn4-yVKhZgTApjReW3MZSvTXdXEbfTwDPW9shGu6NlX1fsNNewQdBjS8W6mjecZix-X4RsXJiGO_l_r0L3eaSduvpc9w7EQ_4hAN1j3kflguNWe4D9xef04RwtUf8taiMMYhq6JCfOutd3_pevjI29BqI7Ziu0IiV14jMOukJDTkAFdI1mssAvH1bPMuav0p9lQr1kblGknTaXq5lhxMEnRtn_0DjnWZm7Va8OmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxK-8hUXpjdpYv8BNpJcY51m_ORZ2M_NXRhHOnhQd3Lmp4sxi4JALKXDY83oviGMfuVocQENojfSxLBsvx1zdMk5odIBEp6a2why3dhI6dg9WHKcDTGPBT7txBN8Rr2s8QyQHs4o2Eiu8AnDJZ__wgzAgGyFZ-U9tshHPlP-0V_S3-Aj7YNqHcujfv07NPasQdCT5WNfmY70_0w2dK_P_RgBjbh2loReFVXtjKd_GLDvLhbz0Xhmwneggzx2Qg9Lzumt02kVWhMb8t3Bxp0qJI5G_GWWSKZGEpcxe6oLG-x7QS9kt2MBWGl0GcEa1p0y4526UuapYnU0JJhn7y7XWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCcDMFVbVQy2RPQawkhbqsgAyL2MdzfRcd1sz42suAsv3uwO68PlivBzIj4htMOzMitnETUmUtd-xlHRCW3p0DoFtKBJ7mJVa1q8G-I3vr1NQNtP06Pqz5kmwvLc24qz6OKnJHp7acJHCVtrwuiqTVY4cwdxyULnawnaE8hXQt-k8yUcOgKjZOEGvl2Vqav5PuI3zxsYlFOMlb7rtmBJfvEcNSe8CVdp0VwdgbD4Olsm46WNe_f9NiVsaR2bdjIBkXbe7tQEgh1hfOzhaIhfb68_xIdMl7GTiawuKlWl4HzTFuj9ISfRILldjxg41WN42mdLuhzRoCmCVcHG6dG0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN1vRXLNyswqOPY_ibbglom3t7smlGgfASds8ODY6vBCM4Zxo1VzaDDdkR1hZQHsRa_pGWjxZXZhlYS6RC28OfRjNmA7LJma9_JBoi-RVGjagZvemnKPMCQGHi9OfdHabehKyRbuz_1RIFIzKwEyaM-lzVEQzgu5_wh5M2HJZGkvsJjHkP9l8_3ZrZJ7amC5vsIGow6jXUwe0adLqQlIJxXdNJDXScMT_ITJ2iMvIV_bS9ccEWfVeocXR8Ms45fFIAileCdhItqf1qxSNHv8eNhiXETRCE0vPzaTfiLgeFwpTW5dmqpdHbavf5sGKTegRiOcgR6z1aY4-ksWOGqAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL82k6PLSRJYx7YeX58jLfZUXC5fA0cmnwVPrbJovK1Ijla6G_wx4fxCIgQ8eWT5VCLqhCHAqRIwzWyEvXOXqI5Hsqh70dvSyiouCwGCCGASvoH0lH-lIf5YQghI5MbwaMdnk0WMg-AltvChrdCm7jWBH1_ywnEJGmE_Nvsiq4aTK5BtbhbD6rEhU4n8dptpQdjlI4wMPz49qP4MRZ9Qu9YuR-BRc0-Ufke32nCPQhRtnUjkHlmqgC-6eZljSEwbwhu_zQ5uhbGdIObUS7R6fZsSf-fzEla5-JEtCAAIK4enQV0W523coTxEaBfmZI21Q1abURsiFg7A2GUreJOfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRJOIbDv3xdMkhbK7GNR7_kXHkxmrKVKzrLnPuTt-L54rLov94uWs46qW0JZCL177sV-EC-GohpFtWK51vlzIeixQdDHR9d2PH8rlTyrc82Gc7uEX8trkyIy5L2FPTm3PZdMXjul0kUyIJbCIhxcfo6e754mCwN6nbqXeIp46OtdY5LHaugAMJZVmXCV1MNGpCcCpVzDKdmYceKEX9psoZF9Iklfq1L1sfDmhj8cAjYzQVXsE53lx3TjWmvyEsvu1ZoLn_o92X5Ihgpps1eOQaz1DanhVcxOAonfLOIq0MC3_3Hm5ufaoFYHDo5pzfdJ6yEZ0w2knLvb4k0FE5oYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIQQFl8kg189X3TxjRu9lTkaDjsp1sBNrEnHmghSZH-ezROK36AV_7DI0m6Py6Q3z50CLoWiufTRyx-X4MIobQ9hwkpkAd1oARTL-amLCet_vSdWmmZlpceQvX0vsFo9YWT-07MU5lAuVH_uUF55R_HgiOdY-j9DoYve2mW8EwjAEhTR15tOxrPy4NkXlWe560uBpFja0JTY2IWOOZH2jSd1p0FVqKWEI-194nKEFFdgRRPLD55RvWCMNT0ljCidf57MQtxa7epSqkb92L69twQ77GMXQb8OD7CPS5-rDGuLNxaM-9C5YyFzMkiTAsFTrKXC-UU6jhKTAsppb6FuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=rFfe3OUvvFfPBYQwwOtUFfOpCILka7bI9j_W_URluaFQLx6n1YUJcuxUjsc7O-W9zEjWLakpQvtxBJHMAKdowWMDGiYTqpdldKzy3Dr9VAtFJNIw-zo_2Z09KGdauvgMbK01Qh48bDX7Fd77rvYke66hbmedeiz8AqrJl6zgGPJBSNo3_WT3DaXFXRM6GU83hVHHK6VqozWOha2JM99fOYtWyuI9-9v55bAXWdpE-CSPRkFcFXowT0uDY0_JtWv3H9BcDCHiJEpR7HQ8vXNEA2LipWGu3TcXKfFYPKpnK2NfQa8taWx1aYx3ZYDD8CJfqL1MqE_OgRKvrdBdpYyWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=rFfe3OUvvFfPBYQwwOtUFfOpCILka7bI9j_W_URluaFQLx6n1YUJcuxUjsc7O-W9zEjWLakpQvtxBJHMAKdowWMDGiYTqpdldKzy3Dr9VAtFJNIw-zo_2Z09KGdauvgMbK01Qh48bDX7Fd77rvYke66hbmedeiz8AqrJl6zgGPJBSNo3_WT3DaXFXRM6GU83hVHHK6VqozWOha2JM99fOYtWyuI9-9v55bAXWdpE-CSPRkFcFXowT0uDY0_JtWv3H9BcDCHiJEpR7HQ8vXNEA2LipWGu3TcXKfFYPKpnK2NfQa8taWx1aYx3ZYDD8CJfqL1MqE_OgRKvrdBdpYyWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vERIP0CcizQZ5arDPTpFrHqwWUUIVMbhAmvj1uLUvhUJxG8GlEIqEB_ChWQqFxq4wsw7Bp-4Qs2gLk50yqOSm7rdD8EkedpT_zU_tPDQSEW_WCsAYNtcsl-7vf6lbORByL-XmMzMLtn-12VmzLlZhIW93heexKRlkb4JMIEEl42XJXdW2vpA2JidyGtHXF-vU9gJ42qryyTAlr8Y-ngE7RTCy-NkepUbW4vyKZSY7eRt8_zh0JelWC5TcfrJuSNlObu7On69ceOXdn2BNEd8JYCtvH58Z4CPuMYEjQzwKkWyOYcxJ9MlTUtwlEm2VdpyYOSJAlIn8rmgxRVInR9GIvH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vERIP0CcizQZ5arDPTpFrHqwWUUIVMbhAmvj1uLUvhUJxG8GlEIqEB_ChWQqFxq4wsw7Bp-4Qs2gLk50yqOSm7rdD8EkedpT_zU_tPDQSEW_WCsAYNtcsl-7vf6lbORByL-XmMzMLtn-12VmzLlZhIW93heexKRlkb4JMIEEl42XJXdW2vpA2JidyGtHXF-vU9gJ42qryyTAlr8Y-ngE7RTCy-NkepUbW4vyKZSY7eRt8_zh0JelWC5TcfrJuSNlObu7On69ceOXdn2BNEd8JYCtvH58Z4CPuMYEjQzwKkWyOYcxJ9MlTUtwlEm2VdpyYOSJAlIn8rmgxRVInR9GIvH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4_Oq0FfPt1F3rvN8tyybCkQxPiFLLnYz8sXYDp61Pgtcj8ZVGRhMxZm8G36fRwSjbLw7-CCsY4DKwLttEOqvHnzFcnJPtNhIZG6WaF6E2HHm22c4q1VsyS98f76s1QvtGC3R0bd1msDEn-5Fa7za61CERY0AuZ_soZzuMxFetcIzvahChmVhSx8w44TWieY58G4CYyI0l0INH2LVhRhh3_D40BIvghaaMF8j78Yk7tDqnMd-j-sCAvTccySkhzfbJ3bj3vszB2BeAGyI4H-2NhayjV_uf3wpjoWHGGJiJHvLFJTkST3jyQ8rJrLUuTb0A5xgtqCfqXGgp7Q0H6Hyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ0uSjVtidU36yyy2ahE-gy379voE54183J5sIRCvw76ChjeKkx9jFs2LwYsbw2jXzj505r5MO_CUI9cl9oRE9o4ibe2ga4QFalSTgWeaSzOxph2QSKaSov3XhLXxobICfgzGOws5ZgVMMjuerANLtg91x4mWLHkRltHMQByyYa03ZOL9s6ETmpa8WR8WUoxkFYPlW0WOweLyl8Mw-u--sed417UeD4aRnEZ0-I9JEvhKf_ifcR_yIbLs8WPoGhApiWGZFSOKjtCBOrwsLbmPT1psZBlqlnjMwq3GPJkYqPeIuNi00CJTrMFCNb9zWx4QS1SkSn5FnZ_j2w8kYqrug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvUJGo370wH97KeZF3iMZUnTKbPiHYJUpY9Qcch7G8_VSKthpdd0GpKhWXygW4691TFTK1i4nJYPgSZ5_Ruc7hAnbAn4d0pgeUcnWaAGh-lKPyeJZO78O3N34X4NKTYnMWoGYzqawLM0OUvJcDFaWVpHXsr-IwxAXuW9-C7jkpQEx28rxiDu6tWlkGj0RBHMQsLdcMArgi8eM9w-cNU6wCz8oFK7H_C_9AuLO6dOOljwaoljoNoIg_ef2DG78Idtg1DGTQdd_7Nz-QJ-92ybnHBraMCeOjA8Nfc40CSuFdlp96GIZ3f_b226Accgt1Brh-6di0MHicLMpYKF54utlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmAzViG3FnmdMxpe1MCW2KcobOHbJ4JnxPCXPXYzcip7Py1syqjDaAUYM0CF_GmIaXlWE52oF44UJQsl42Zq4hcq7Vp-K44xDnvYJ6N-ZrqHDggy1dekfAJ6JgIti7UzElX94UBvPCqCLCRIpIxhXt-uREYOShaBkkL2M7QgUOO9rdanbRRfzMajoqar0onM9N5G0QUaiQm4MRgvctHn0hC9TD90DcD6tgz8QHCJEQY1l-9BdY7SYR_kgvi9-kRLZWy5LfDYVxkua0e6iK6IeKy2hCPBPAdX_gZQC8dZXffxT5wThUHWicULRTQXa390MSnqPuPGdVByL0AQIvVDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwNJvEyHalhMMEn4L6TLkxU-FxYclAMbD-NkBYy_Q39wKx5iLUd0DS-gtJ0Ur0AgWMGY8cpuhHigbRwuz0pBEhNAClkypmBND7tRX3qFl9ro5H4_jvaPAP8-5XiBuBo27b5SgwgyZxDrnFkzkqPvcie3n-fx28qVP9lBRx-r-O24vB8Fn6fh7TypvjiVpE3cB_LQ3x_JKq4aRvW_nbdofoUk_TFXmiOCR8WZGt5ylqbrHxrynqotp2rPAgbF3kAAZAK_vnOHhPVA5gOQiIq32j6sIu5qNRHCxqQqBQoz4Q6dZVCCTCeth6UJkiisCTZY-dME4_tdAmz2ZBMlPIy4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVhb7JAdKKXB8Rgfd-xhZIpikmIR30-xH8bAFzVSXc7ME8cDg6U4nBqYU0sWkqaN4QplDrPePnx9IIrlyM1S23VyJ6ld5wZSfOb5aY-ahBL5rXXM3d5XSGygd5aQToXRvbQR1L-aPvPH04N6R8N0zMnNIy2f4zBYRSJPNJwPtoTybN4lQPwEaNqKjkzLyfy_WDt5KgJ8TBosomReN_KZsU6by_iiDYAmsc5BiNJBZfdz-HhvuWVose5j6Gjb9mmmqhOxJUz47BpCJiQLF-X55AA6XdsgiTEcd7E9-P87D91kWp7TGpUZm3ErQGCGrhYufyFdn_BpcjDiNM_ltehdmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=sQV_0xIFiKvHbN27vrEs0-24UFMG-BRMxRJSe9d7jlE84KBuNMTG3oLK2nHB6HCIMjDuW0eUeRHJEYmZmL_t-iDkO5hf6G3QBdO8IAZCTuiGtGVKolALfZrV4T0Xr27ubk5Un_THMnPoQVyPd2B8-qkexOvrwbbjuqCCc9l7zX0Hi61P2OcXS6CTAHYs4_arOgTJNX_7iIfZXuQvTZf0eLSkdylwEPR_2y18tfsYeZeGFlqCd3C2FoEe9PB0rV66Npa_xueNDHfcA39-e0KxeiMWCK4mox-AemxLtHWib0UIzNzad5_F2STOQwmu_WfO_jknMdfFBsCtWN76BnKCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=sQV_0xIFiKvHbN27vrEs0-24UFMG-BRMxRJSe9d7jlE84KBuNMTG3oLK2nHB6HCIMjDuW0eUeRHJEYmZmL_t-iDkO5hf6G3QBdO8IAZCTuiGtGVKolALfZrV4T0Xr27ubk5Un_THMnPoQVyPd2B8-qkexOvrwbbjuqCCc9l7zX0Hi61P2OcXS6CTAHYs4_arOgTJNX_7iIfZXuQvTZf0eLSkdylwEPR_2y18tfsYeZeGFlqCd3C2FoEe9PB0rV66Npa_xueNDHfcA39-e0KxeiMWCK4mox-AemxLtHWib0UIzNzad5_F2STOQwmu_WfO_jknMdfFBsCtWN76BnKCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=YTlE1QUJrZe4HE2HeRuD15SSayciz9ZE24uPTryTm41je9375Op4wX1s8llMFLQce5BhCZAtLYcgsSdw803waa_UY5x9CFtyTokmT0-1rWhvxffAirtf-kklhbNLNQSirzwjLbsFB6mjGISRIAThCgLnH8OhvIkIDNPR5Fa6oy_ve_8TzMn-UhbdFLW8YRCGID1L-AvAzNMm0lr1A7OTRevpHDvThvN0WBrevmLANUgWEYDjLu6YGKWo26wj3h2RMvmS9dN0hXRDJj4DH31YE5CpArkT0ggNHb_BzewBGdJ8HPYyj20cAVPr3Dbo6d1YZwqp73gge66gEu9JSPfCeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=YTlE1QUJrZe4HE2HeRuD15SSayciz9ZE24uPTryTm41je9375Op4wX1s8llMFLQce5BhCZAtLYcgsSdw803waa_UY5x9CFtyTokmT0-1rWhvxffAirtf-kklhbNLNQSirzwjLbsFB6mjGISRIAThCgLnH8OhvIkIDNPR5Fa6oy_ve_8TzMn-UhbdFLW8YRCGID1L-AvAzNMm0lr1A7OTRevpHDvThvN0WBrevmLANUgWEYDjLu6YGKWo26wj3h2RMvmS9dN0hXRDJj4DH31YE5CpArkT0ggNHb_BzewBGdJ8HPYyj20cAVPr3Dbo6d1YZwqp73gge66gEu9JSPfCeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_unxhnVy1Er99K04bSjbYzM5d4aVoW-j6FyRgyx-xruAvEZeZl6x0sNi56YeKvo2ZExAN_5ArSNi_Mw4ybQOvKRDstuw9arkmABNgH6imHpNHGcnZWjtF8aRRzu0OZW6ptFghPkqtPs65F0PsqWRGvch3unCgB-ZeHtMw3ZAOADraxC7VebRliJP-vsOzS6r3msHpo7HoGThh6KPtdCAH2NOCF5xwi3Fk5FGf-bpvsF3Omot31VRGQ0CrYxUf8uMJUf3jHajUhwqP0nj-yBJULd4kSPAhqTscQLq976b595fXmTAeh735nHiWFq2_b255gwj22O-2Null8TPzk6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6S556WzArbkxBIyE91ViwG89JwHh8aqB8epFXPg6hpodM_MVcyeGv8-o9UY0fKtFomk2lrYHi3B1hG_0N9FYqRQgVL_vcBJAjkAsejzIbQBkdSCWbWNhOZJGprxGKx_dHX4YjR0GqIFtej4HwEDIe7cVHliMNIhRai2mXQhXxNEMl9mgowmmKa0IH9qNrYY_Lg3J0zWdopAfJiInIR-sBFJt8Ed_aKRQY7o2pG_EMe39R9yDBOEEKv97qxb7SIr6eJl0bO_e0kpZ7I14v61jZSdX8-qT23BK0C_AgLUdeQ4Y_MLImwFwTWpcyzMXFbM8xkVFoMk8GLGwa-xhJpKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZapYebBNxdnatBNJoMfjOySnnhlj_EHoIl9UH1LHnhoejathrMCx9P7icgujmAZN9WytPiqf93R1IvtaaX4RvzgzL95Ll6L_VSyp8JVgtuxfnflQ3iaoKFPf1IEbKJHeIcDT7qX8EgpFNOxGu5VpolbKbcTSgN8HrNKgmOtnPxcvXEt6vvcacgLc_yRRmvQOpSYs1z1F_umeDXZDKA83OD_9hpuCZTLXFXX0Z47UnSCiOiG0jXyIdaD8J_R05wZmROIxX6A7ODG2mGRaK8HMHE5BA5mg-XTIZoGwJph072wtBBJDt9hqnRO8Lwnj1N52huUb9oJ7VE4h1HFkQrTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gErH5fvbAYRUPl6mlRYwejRUEN3wK3A8rXWAxuiYK-_SfikTM6txof_P9CL1SDh3jYRs1kmbTvqAla-wo8UdRoAVrfwuBeA9USD9EFehP-VZ_BWWclVs-_Rklm2t4Te77Pq01Iw1Eb0X4erGAm6y5OT15Vu7Vhku6I38i3xo4xqw4z0XZPMnApJp9-iX9gbYgDKEGMA-9pCpOQ23XI6HTv8huTXViDOHMs5zXrJtMuzbeuLZz6Kp-ogig0HHrJBCZrETzLkTsErGt4GfD7XCrODQXYLtoUdCcyjuUWDdxpboW_7jLUQgbdk7vM-eKOYGQN_i1Z58qx-YNPQetB_CRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrkicTcDAbB3SDmC5EpJtjalUgepAyTBw7cuTWqUHc4myr7aBTknWwu6Ot_tdjCzQ395zYx9Y6w1K-IJxvm2TMnKcbhZ7_QGO6CNZS_YQKLYIEhizOkqnGfdKBu_joTOTJ9QgbI9rYb9pBhd8iBliPk_a1nEkblV9-rO9cvgAGPznU4MptrmX4g7Ply9c8nJIcS3XTo6kgZuwYt4HJyTfxY94wrPbjK_XsF3RCQeY05vQMeICRw7sVk-fxW-giK4BljJoRj0mIyqSTfJcjVC7q_3IBth4yxCHwp2hinegTQTLtr5dFLmU0pQQsIewhhBJriOsAjdtujuBiuYO54x1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=NcQAkjK_fvWDent__TH5JomSXpCpPUpFLw3zzPttCZ92B-t2-2WZb--KEDBnm33bVVsINGKy5EPlyOxeHa92oWr1wm0NQKQ_QSa-x3k5CBGQI9EveMV0hPWiWJ1j-O4woQqojsO3xFCR-dVJ5GMJsrjdQzVp9iPhIXSGTmUBZiGpsP21zKx7tgmej82ILVa6j8Zke2oM4bFO5i0xDRu13xFP0cU9r5NRbCrR_5hQvkwLLQ5w71ie_ZHfsQ7YZYK2F9lmavrP8Z-A9WDPJdhDcVT-aVI5NGyu_4pamA2e5B7U6S_XZcz4wcJWyREt-oRX6BqH2bmWsjeNdBIR1MSKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=NcQAkjK_fvWDent__TH5JomSXpCpPUpFLw3zzPttCZ92B-t2-2WZb--KEDBnm33bVVsINGKy5EPlyOxeHa92oWr1wm0NQKQ_QSa-x3k5CBGQI9EveMV0hPWiWJ1j-O4woQqojsO3xFCR-dVJ5GMJsrjdQzVp9iPhIXSGTmUBZiGpsP21zKx7tgmej82ILVa6j8Zke2oM4bFO5i0xDRu13xFP0cU9r5NRbCrR_5hQvkwLLQ5w71ie_ZHfsQ7YZYK2F9lmavrP8Z-A9WDPJdhDcVT-aVI5NGyu_4pamA2e5B7U6S_XZcz4wcJWyREt-oRX6BqH2bmWsjeNdBIR1MSKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFNaubRfDNIWI48jwfMk-32z0YZllFJubPDHKpaxlVH-APsWuIE_zridwo5Zi_OIxkDj2A2zoNXqTqaUvQ0Ud9LzVESrw_RVpWubDNHKOPuLc5zw_jkkD5Z8bZz9K3r-OH7YApKp6kyhhwYFN0JqN9Rmxm0Igd6uKRjG_jrBj8g9ufjWpuVM2EPfyRzWqGt208gfOnoZV2sKdDMWg-cL_MUpOoUEXT5oBRN7rQy3HdqqRqIMdznJzmLqyY61aEt5aMrliZXZeCSgg-H_YFiQy45m8dSoOkQv_X4dqHwxIT_ep4XVRuMoxHqDw9SmzO6yamzR9EK1DNzKc8UaqrE7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9TWtbVlF_pJE4UiMKgx3ZmtxgjQp2M1ERYy1oD1ijITM3j_8fweT8SGmVZ-TDrpZ8boZyOf72oHdMlUchHGR2V3fEnDTDu_W-sfwwneuLP3Ozw3kDRp1EVxKmcHK3f3T5i5kFcKR2OprTzUAtotSXqBM-2vx10azKxtaVSmRW3wwMkERBDg3BqMAQPKLELCxcRXpGqdP3vKyWFoFqy7zyURsf5dabIhd_EIVZdp3eNytv0ovMS2u95Mwlj-z_hJsyIETo8Ji5LqRo1DY9quGu8zl9KtKRd-qlZCuhhZ6GLOhJRIjUMZJmDtrZv2V46l6cwLbjOYBDVesAeGIbugbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwpvgFlRsPTBYKbfQApP1PRDgTrexNHx4gPLiYIaCnqVe_YSoRLe1U1vKznZF72fS_faIKdbYRicwPliEKRbTaFF4_uaWQO4Q9CDFjvkJMdli1-aJyPSZro9KgBUd60RKqzgSUAKzQsOM-MXO0-et7u6OiOYXwitUbR1gAEH82IBnkwf3-0uzG5Pj1YwCNYR7hTXfItQJjyHvLz-wrlze2ewRtVt__finBxxDPIhWSLlWgXRLQgAJYHfy_XjXZb72DxNpgs0OnzvzYVLCUveAcnFT69WJasmmYXvqzfaOm4eySj3wuVktUGSRP_0jgg_rNU36I78GSaUUrGLeL0BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPQ79dRAyV_OgR5ZiAjaZSiTaiO0cATLW-7NaI93Rhn81wztLJE3cVowrcwdnWt63MA-C0NUMc3fOdxddn_dGkbjYiXbiLaJTIOnDJEvvMyFgoj9GCECLUAV-LRWOs7jwptbROsWTMSMuIl3foZUDdDj3s8W4OWLI1RwN5Kea-0DvqWfM_5Az3UJut1m3nfnFTp4WDdudqi7uSYieZp5nAG5i38GPFzqhzsiBAnglOSwSx2BK9WMvp90imqAzxUgrO0cTagVI3xaDCVuchxViFCfEhSTv6UBC3N9c8irB7b51p-_ySfZlzDS4DjCBPaKlOuVm5UDFRkhHsI7Ft1pMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=AYu2blIDJz6nOrDDre5k9tEQ-0Not4WoZVKdggk2kmt09gXqEqTOxblnuuUbLfdfWYZB9FioiZCmRYXrWHmw9VrcnQK6qhTqA2g18z_LbQIg_8ulsEbGXImo4d1AWoB-Fl_LYtCEIwAVNjkSObrXcdls-xgVb1iyJUagzTtOZykZmMJPTobjpYCJTR4mAZQGA3YpdoO4n-kZAnQUxk9Z5MRuXSs5_9-ccQoror-XBJKRXiElqx-PV69UT3MMj17BkwZMQBowwLaO39KmxfgBDyMAyL0NngEjHIK7A16TVMQ51MlQ9MN9aovmh7K_FhweqgCFsNqn0w6btU-53mxS-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=AYu2blIDJz6nOrDDre5k9tEQ-0Not4WoZVKdggk2kmt09gXqEqTOxblnuuUbLfdfWYZB9FioiZCmRYXrWHmw9VrcnQK6qhTqA2g18z_LbQIg_8ulsEbGXImo4d1AWoB-Fl_LYtCEIwAVNjkSObrXcdls-xgVb1iyJUagzTtOZykZmMJPTobjpYCJTR4mAZQGA3YpdoO4n-kZAnQUxk9Z5MRuXSs5_9-ccQoror-XBJKRXiElqx-PV69UT3MMj17BkwZMQBowwLaO39KmxfgBDyMAyL0NngEjHIK7A16TVMQ51MlQ9MN9aovmh7K_FhweqgCFsNqn0w6btU-53mxS-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIffjfA2PRkWTMQ1sOrkRMBzxQ0e_dXJuqmadUG1GlT8bq-zJ-aPrq41emf_0Lawu7ewU0gqH7ecAEVsoNiyK5Nlstr6cd8-y9YQ3MIGMPO4FVXCQGLjHMCJYK3sLmOpompr0saKu0tjdXo6osq1Lpa-9rJ0NMNDi0_6xTxcUo1ccTd0nHabUjSIBnihU_VI6vrguH5k7AS4Ep9vPtNzSSWeaKEpcXLDmUgEr3mWN-UyF2yUa75MldQR3VE4844PrkbrgI-mi85WSdxpfuZv4HXt0NNNAdS8NalzGmfoHo-QaV6rBhdSDtyZI-6TkFgZ_FQgNL4R_TLpjCpz3ZYCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFTkIZJQaLT_mexs6HiG1oWJopudag8QI11zRBVCyg08RioPPCSsp2pp9R7tCNB9U9xWJdyO2ALRoDuSivKj627sn08poPZfHUtcgLeS_63G70U8MmYiFzAP2D0Sm6e3zuZ1pLqqTXT-CZSUo95NB-WdA_lNX0SAoBOKHaxZvvVrq9A5z4eepEAMzyjgY_mND8I160lvQXUupYTcCGexKiwaLNPt7n8CGTmOeon0ExZun9a2WSA_AITLG6RvjPfKhIZgzQk2CK0cvWcrTK5rCXnd1vqd4bEV8M6ZBTxLXHjQ5FGEjVwI_Dwgn1oBWs1lLnmE8jjBHaeJrf5h2bMCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdIBVa7SKY-xbJUsFANINTX6RsN_sPR_ovMg8OEVAu8ajHJ1yPmOKv7PIDhlt4HziOCDPTiYZzKXeIbaEwTLd812y5J8a3lCI13C1w5jbeVm7dOUCyG6uaiNnoJcdj-qHmT-oxmPjD_Vzqx0SNuyYesWVtnq5Jk4Gi_gZzpS-5hgIfAjP2zEDfooATrfdVSc5fv09ued7BV4sF9brXTRHwJFcL_2FRtVGe1OEIDJGrVbCI4fqzz0HZYfgZULx13o0rZNTAQyiq_r1mAQgLKYEzh_7gsN9am73lE7kSVc7vC3rBNcKwZqmtlkIS9swT3fxINxSHlYD67-oI4jCoRSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=GYot8Ng6WbGIybLkPk7ltSPSpFCGRpDdYcg_-w2akOpWxo3mKjg61Ec5YZBUQZsvh5sUuNF756rD-S3_QK3hfnKSb7E-SvEgtYB3-UfDOELcgztNyP7RhY8ndoDmehB1W4KESqr1rc7OLN_-EjJC3YFZ5nCewxJVtwGWROolJJQFRsY16SV-Ny3a3e08zP3_eQRqySB5PI7K3nRlShXPKITRlh81XIhJXZsawIoAJZJipHftHeMdAAPzUxtkaDXVhI1TfQM4eD1ZUeoh6_ee3WIIwmQSq4kMn-4rAzTCckOb8Uv6A9BmzV4zC8ID7FeSh05oWUgUx9klfXU4EzJCqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=GYot8Ng6WbGIybLkPk7ltSPSpFCGRpDdYcg_-w2akOpWxo3mKjg61Ec5YZBUQZsvh5sUuNF756rD-S3_QK3hfnKSb7E-SvEgtYB3-UfDOELcgztNyP7RhY8ndoDmehB1W4KESqr1rc7OLN_-EjJC3YFZ5nCewxJVtwGWROolJJQFRsY16SV-Ny3a3e08zP3_eQRqySB5PI7K3nRlShXPKITRlh81XIhJXZsawIoAJZJipHftHeMdAAPzUxtkaDXVhI1TfQM4eD1ZUeoh6_ee3WIIwmQSq4kMn-4rAzTCckOb8Uv6A9BmzV4zC8ID7FeSh05oWUgUx9klfXU4EzJCqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7OMmPFFn_fUV2BbqG-ACMwTmZXYBYIpxoEGUGvS1a_MqWoNkzSkDu_U7SCZ0ErF76dVRkXq103QfwNl8KDrmUXJJt0PHTOcbEsBi77SqmijdGXn_cNdHwVGIOib9ZSIz5MqLkTcU7iM1WBJKJozIbNszPTzlO6ldMU7nkwL3seHMvyRYR0NB-k1Y3T-JJJcw8LSWBVrGg81yIDEwQIyfyxN-9Hfyb7u7ok8mGcT8WBiXLfgJA-rMyFFs1Co9A7mwIAGQCYpxUJIk4WtFM9b1lov4bXpaOEE_B5zt6oACGVTUoHqKFqV-4tNXuu5sA7WAXO3oR_cE0gTY6sABpc6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcnv15EBdOmnffzRguC1-a7o4OQaQCDIVDlyuqugmyfbEhtbMgvoOsSQx7_bR75G7u1lP96gMfQAydI7SD_1LisPOqv1cp-Op9N2a5mARWAVyibbGOuDGJymLjFX16S4UjZFWyd7UqntSo_EsVU3h7bhNYCxSIhMwuZwmcSCddS-b3oljaWXDZoEKr6x3T593j7v52vy0ib-TwoE7HWtI6D0gObYA5IdMHIXREhoryDZxxM89w_4W8qElq5ZlVH8FMoo0KZdOxKbYzstJJfbj2KzPK-AfbhKaIeLyn9Q75cKN2NHdxijTwJbN0Irq7yFxk1a3XcB-xgujH0J6V1QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvy_0usP2FiQsebyEqYWanoVyvVNNi2tG044MLD71veDNI__GEqJr4KhLM74J5Y_BNDAr2tsvgdCHd85nkB1tlyO83u3VA3CXXxhQ4dYr-7tFRVH8DVNmIvGydB3EkyYwO7u0V_rmCfnXo9BiPWUkfndZNwinIeBRzwO-jrHkq9BRdinwoz1afznczbhk_Gq2yxh3flS6gNxesRq_lZutGL92kAOXfcqQ8FiHvxWo133vrorepCljMtRvldXgB1WIq1YTnt05_ODaGQMsDvHpho0TxziXyDpARgcIpjjhS0hQpkdbeDd9CUtiOCeOkVsc71suTfsvY8jTD851kxh6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6IyRPCce1TsrfatLhT0nMZeLoH877ObdlhgYLft8mHVVPvyzL9oOAjjAViHGPUG4NkKZczXxLGRqbpYdVyhdpqtwZZKbeTwlEEHe8DXD_yBntd-FQ4vqb7NIHbPWr0ZVev16Z5GGalqQ8g_3_Yyz2ArN_9dyphfy2MHnxAj0jX0g-Y29a7p-Zmce5nP2E3BXtI-ev0VbRg5-4uQy2jHbnc18VTwub_I36vSGONLW9H2ywzDUDylpQhYwLqgvmi6TLpX3pcq6rKyopbrmW2eCBO-RfEN932UE1meZNhXSSQ6QUMZfSDFaU-9uWodGG0491FhjtXeT8S__-EQ8DsJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=eomNrDJ6tzbIsm-iB_EKWyB39o3whP9ql1828frF3M19tjoI0NlFaVHg928LFozFXkoA73vBoCnmMSEjLxH0PzO0lyZ-p8XU_o3pWrxaByod7MxBFkdBh672s7-QBvWvcEPRGtsat7mgHYj6fpmW2Xc4I28OND0gCcsl8TanpEbTuno8CQPSSwuWIlZTjyNSG0WG7_9bB1AIj4UlxgptWmVrl44CIJ7-8CqJ_Zz3Uk26LzHCtMcACR59jccp3bR-OC3JXBGTu-iwOYQsJBzzqKABuDOV163TCdQwzTX8poYXdR0BS0hETXDgRVRep0deWN7dBx7Y4xi6g3SKtcCdlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=eomNrDJ6tzbIsm-iB_EKWyB39o3whP9ql1828frF3M19tjoI0NlFaVHg928LFozFXkoA73vBoCnmMSEjLxH0PzO0lyZ-p8XU_o3pWrxaByod7MxBFkdBh672s7-QBvWvcEPRGtsat7mgHYj6fpmW2Xc4I28OND0gCcsl8TanpEbTuno8CQPSSwuWIlZTjyNSG0WG7_9bB1AIj4UlxgptWmVrl44CIJ7-8CqJ_Zz3Uk26LzHCtMcACR59jccp3bR-OC3JXBGTu-iwOYQsJBzzqKABuDOV163TCdQwzTX8poYXdR0BS0hETXDgRVRep0deWN7dBx7Y4xi6g3SKtcCdlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f66OxP0ALNKvzcwdvPhj9FWH1w_hpKCJIUTW1QDMh6_OaFITmxrE8gLv1Z6l5ZaVtBCgRVGoP9b-McNMC2kq5DEi6RHx70ltWgdALA-77hwv_03kHLhwZKtL36Rurf4EQmBCa2Cnvc2sC3aEIOkZVjKYvs6yWRavlM-2U6iPXbvVii54J1Jj7K_P9EiXCiFAw-29UlBsvWjKSvRSlTn0xzbsmoEp5v8qv9pnNqyJY2omOBfd3JBgi4JOll0yZfFqLwQjFGh29N_X5-ZUg5kDwFWur7GfriuoAisapEL9SR55pKKAIwpMTF5J9sRDEiHbXWpX8dH4RLKiz0ZYE4maKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Ve5UVRZ02k7XahGXdvf-tGvi6x5TeRBhv6dcn8dTjoYfvb4UWeEMYoBYnekI_PKc5c35Hd6DxtuDQ0ESNKXt0OopvJZH9Y_0bGfi3AsVZZHTtwgtaeFwXKGCjaBv1uQremT48MwL8MwshilQG7BDsiXsDDlE3uvs7mup7hhQfPZkgCSVR7IF7pqCwcMIa1OlCnxTLCaTn34DrMvr6wlx5teesBDFBRPx7y4m42KCkTV8MhFC84HTBKckjr0dliw-_ckYtLWUi-zloIwRTfd1SoZoYOPVsPx5082lmoZ_IvhmI3xv1V7TwoFa2p5Brpg-Z8rbfsFOoFjZ_tKDo7rP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Ve5UVRZ02k7XahGXdvf-tGvi6x5TeRBhv6dcn8dTjoYfvb4UWeEMYoBYnekI_PKc5c35Hd6DxtuDQ0ESNKXt0OopvJZH9Y_0bGfi3AsVZZHTtwgtaeFwXKGCjaBv1uQremT48MwL8MwshilQG7BDsiXsDDlE3uvs7mup7hhQfPZkgCSVR7IF7pqCwcMIa1OlCnxTLCaTn34DrMvr6wlx5teesBDFBRPx7y4m42KCkTV8MhFC84HTBKckjr0dliw-_ckYtLWUi-zloIwRTfd1SoZoYOPVsPx5082lmoZ_IvhmI3xv1V7TwoFa2p5Brpg-Z8rbfsFOoFjZ_tKDo7rP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ_kMRMdOaAsghYUGkz9Ddj9MaBlXZ6DWsSKR_H9iuSJn_LGPAWyH4i2EneMn3mdfyBHVsoHf_bxtOyzBC5tNlHo_k7jGgPp3GMW7CicLQiWsYJ08eJ_nF418TnB6JfFgPKYoxHrwv6SqSU_NmCl5cYkLx7QEa9TP-sjhELQIll-IJww97WwEOVgacjkx7_SuMPw88EaLrD5SZVeeOo-LH4USocVLjwNksshm-y_q_UGGReo_JaL4-_-uUkprEyHb3baxgUtnfPcvS2SiYjwQtP0JiOtbI-dy0jelSNelyyK_TCxA0KhEL9Qb7JNNrue_1iFCB5nk1G8h-aW8PLJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwHrWDsPoI4O3-OgbQlYVkQVarUqNZ8edegJIueiVBKiiPzQT1I3GGVbWiBlQDWZhwEa9muAoKGPQyjbCDpOFxG4s-jYCSZHi47ZT38T_MS_uDkkdX2MktcYHEkiNnnTyz_EuQDVGPq3yZI8rSUyBajwiQ9hUzvsCnbcmIOGAvrwT5SYyR3ESeHKFgqm7aUJr1wq4925a4MPD4aUFolxhRqydVQ1_EQpjtC1mE5zIwrGG8km2fkA-DUBkYuNInSrpqgKm_DnMF7S5fuvi8BxNA6sTCAAZ1xfPvfxTBVxeVm8GwGa6d_5LtrkcPSO26MC7uxmcy6oSIlZlMJcE1ID4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp09k7XRAVugOhIWGfgu2-D4suZ7r7E0vi8zurdeT9RBhrNnGrTAe8b4HJr4OG4vh8pUssGeLqKJ2z4o7NkT4ti4UlvVAVOTC4dvI5RBhs9eqsF1snRkSDGRpbeha_fuDgdW-m5nwCw_9R_CaIjYeFmf8BSSkCuru6p8b_-hcuyMGPuGom-Wl8g1O6TwdRmoyW1tY8jgslQFQrq5nvIqxEOWPSUGwDKgkOiOpj-Fvi5fIdEoDLDA6mn9RIg6EZn0Tbsvbak6xRdEfTpEzwAKIDZJ0dQxJYqxbVo75LVaXNCC_yfhRl-gmlk9tcsQHSnaWdxDUD40IlBwuK4xQ1yyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khFcIenS1TxGo6xZ-EBNh5d9tJ6xohrO4zu8LaFa1GIy3F24ydczcu69rAVBTHbj2s8BNEcdzO7OBIeQnlpypbIfsF5WLeW-VENDME0O4ar0jQyAxmWHAsCgJxh3UyYv0yjp_wn6gOZA8X1gjTEmmVxoQkDczApcSkX_9_4A-Sryp9BrkKDWinyFMYX873aj4WDWFtaDxaQ0IPqLWKreSfiagyt8W9K9p_fpybv45pXu9yeSPpRESrhU59lNy42NsbLkDlBJawKSCvWOb-OvZeokItYMUKjco164qSVsxBfXwAqoLOyo1gOQu448QIc7XEx9thiWDvFlEAAZ2qwAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnBp4pHHSMKpj7Yd9-OyarTI9-jYNWJ9jTSRJWIlm_lVoJqTxRypi9AoV_AW-kHMG12Tw07aBTtbtXMgcS5TJwFYoIJh0DZytgUBS4IaY4zt1i57Wa6knq4nTQIvjGcFthybOrFbi4ifHnLoVldjXQowZjT5_c8AAlAkcKacZM6-5WJj9264UzN4CctX2LQA33mab-YPStc3kuRO633TaFwdOY-DqH-70v05RBUxnPyodCC1zaE2ESdyHM49IVMeYgrxo0ibc_3_AIZs5HuDAViNFe4czXNAXeYvFk_HBv-mEeijhOMsjA0SXXY9EuhFzx4dfqUOt5frgb7OxeGpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=iDb_2MrRaXCeLL0vPfLr1Vmjv7Sqo_49zwDKiUa722KIRtpShgrnSGgvT-4FS7GSIVXLF1_YYxInaqEaYmk03S0qkEOHLgm6rg0y7X7_7YU9aNQZD99nH39GnRIkUV-Z4NxOxjhTH_LTjbNliFUCiVvO6jQCooB1GDF1E-DnBV6tAnSEkGCTavQOQJLTTSomE9THDtYOqQ30GdPBUIjLjWlXnEry2VNtW19gU3KS2vHXukCpCbHzv7ueTGtrNc-wVLEYTmWZSNpP683E3pcBINipxYhRibyubIqstO2dle6Uj2s3yLdfTJQm4gwO5BbRz-XpfBV-Q9Q85ejmAsUvuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=iDb_2MrRaXCeLL0vPfLr1Vmjv7Sqo_49zwDKiUa722KIRtpShgrnSGgvT-4FS7GSIVXLF1_YYxInaqEaYmk03S0qkEOHLgm6rg0y7X7_7YU9aNQZD99nH39GnRIkUV-Z4NxOxjhTH_LTjbNliFUCiVvO6jQCooB1GDF1E-DnBV6tAnSEkGCTavQOQJLTTSomE9THDtYOqQ30GdPBUIjLjWlXnEry2VNtW19gU3KS2vHXukCpCbHzv7ueTGtrNc-wVLEYTmWZSNpP683E3pcBINipxYhRibyubIqstO2dle6Uj2s3yLdfTJQm4gwO5BbRz-XpfBV-Q9Q85ejmAsUvuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2tqVYTit3vsGZhbrXT6n37qd15367-d9fPQ20W2j2x3Fat4MtNhRV3im8iMfUklQvg8zgl7lLaKCjqKhYSYSrzIi1W1mRKBlOs4Tx-KE4ocKpE90JN6EhYEfUhFbT5MuvJPY5eNeFATBg6lyf6LwCEb8G6S8B6bQVDsPXmXgY_BOUDVjJd0CpacDf8CF8niQMDJuVgUvLEm-aTJwAhkSgpVYNR1z83yMTtHR9tJH6LBD-MdZZw4w0suUCtyo2Ys0iXLDLhSnZA4HwPIY86Jt8QixWwYXmymedov9SU7RmrqwYxFM4O6I62F61Qn7n3XEyY-QrnLuS3HKX9zV1GFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB-BrU8RkxYr_yoJXPFGv6AOy_lwYn2LYgQ_uWpPy3nzaLWz-vviQ5-cRGLz3qZrn73tohfNXoITFfsrkdNWfW-syUW6t2Oit_Hjo_D2buCTluVMI1G9sJXk48cbO1Y522izZZSV1fFKuosL0OI-5YBAFBNoBsNtO9KBPxj_daJN2ByAxlZ3cboV9DXGpgkKv728xgyFg_fvngEkpIHBZ5dL6w-VAr3wzEiFRK4GT-1AFY_VqkU5FLZuty8k_mfN40mC3CmprcrcjQ4aLMlkrBbgg3pcMtmgbWpOK3PxeXyY-m1KUnz55uNc7Tr9bwH2pPezzeoOwpqMhiZyl6I1fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=lByj1YIeHXXmhzdsRLKO93Fyw69Mk5eOEjd9ELA3fnnqHvRB8pjvK-Lf9aT2rCy1Poup9I483y173699QfKusF_GybbzSe9LnemarnIhKmYzNBlphA_BJa1yyWJy3ZH925aJydkMnnQ0IVpzo-xdKbR82e756hDjIDqlt-njoEZ8iULJzlOaQ2w95aS1uyyNdHRoAG3-ZVTGNIpxwz-nPEQvfvzljg9WbEBowvdpFqkQylFs_uCoEijnKE3v0DuqoWf8N5jiWL-xBVvhxQniv53mfWNUAqezSsUzEcstYi7br9okxhOsCqb9DktsvfT0fKNUVs4JKfIybF9m6ToGeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=lByj1YIeHXXmhzdsRLKO93Fyw69Mk5eOEjd9ELA3fnnqHvRB8pjvK-Lf9aT2rCy1Poup9I483y173699QfKusF_GybbzSe9LnemarnIhKmYzNBlphA_BJa1yyWJy3ZH925aJydkMnnQ0IVpzo-xdKbR82e756hDjIDqlt-njoEZ8iULJzlOaQ2w95aS1uyyNdHRoAG3-ZVTGNIpxwz-nPEQvfvzljg9WbEBowvdpFqkQylFs_uCoEijnKE3v0DuqoWf8N5jiWL-xBVvhxQniv53mfWNUAqezSsUzEcstYi7br9okxhOsCqb9DktsvfT0fKNUVs4JKfIybF9m6ToGeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSP_mtGPn_OW56gQ-SU9dpMsqTFdp8RXOHboZueZmENSKFFVt-Hh4PzGsSl3Nlo4qV_DNPGdRoufWL2sfrl2mjEKld645ZXkS4sXp4awj7XQYfnoew6GBmRtYbpUy9qO-VI4_oQXMaHgLjHmKfQFlZ-e3Xn19UqHOssGV0tbQIlYa6N7TuOu66QWSkvAx9OWEJM5Ws8OKHi1CANQd7vi-66fiDHrjSvIHRH2kyVK0LavddwhwGPQvxGW49i8CJ30i5HA1ni5rerQ48tUv35TYstEegxgzfqlsZjvjmrwzGhYuln6t-2YOYvZtUIkC6Tpd3n5nnlxyiue0sN3KGKfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPpar9K6fLcZS0Qhfh3UnKW95qTP8ucYuCz4NATAniqbaK0BQBu6KGyMbs1Jore4lTnRkHHlAuNENjzHBnurHLDyAeGcsmzXF6nQacUNIit4uiS1GIpicdhZEqbXcCNMG2cdy0ZPk1jatOA2hQ2nnE8rqq0S56dlRhr_IAHnMWHnoWnYpgIxozt3_-R0qi7TrnWDOCFz3Xj-m1BuCPx1s0vvxep_IPOcynme-ysQQU342tMIYQMEgDJN5h2nTfSwa4SO6yuSZ3AT_2UBQbjMMb5JhyVH-EnnEumJ44oOJF805lEM43EbP4qdAzikzAHyQdkeLMeW__q38EPweyU1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV6Lvfg4ovlP7tTlH87gkYOFsGv_7KSBzWX7u2iwK1I84qaXofS_aTa_98AYuQS_fiiFwwjGpHEPt2-sQzM3HU9bK3c6-YroT7oqB8VNQDrBHUbciAuw_nul_pltJGr8Lr9bk_Z8p5bBTyR2jQikPirRYvGCC05cpnPg6qFqpOZjc06g7bx2MhZAEeGm7j60S3YFPufoDdgmPVUOKqcvgxIotRunHcEWWkyYL5NOITM1H5JQpIyGkyWAYDpZruyyJWi92XW9XnconIaQ6PzGycO2jS3w3cvOuTVc_Uqzdj5nHYOCPYrwHnkS1Fnv1uJ1i4-Qm8ZlLX52ZDYPFCeb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRmheCjhSE-QPvpzK3PSNckerjVGOZTpWo-NPab2ufSKCiMjkqWUU2m7LOKQ5Su7ysAiUA9VBdWMS3Tky6lSiC7tpwq_5cJEP88DxEie4SW2i6z8CJ9YfAiN68rKrSn9mrWLIMO_Yxk9JzGcsmfdXIhFxrKMqJBlr85XLCY6dI0oeTPWFWgz4VFpU8oyF0UiFh7hCKeFV30IYpyMoXmttnVZiLd3e0a6OpS2ciDZ6l_sFeStaT5W2MjJAnqDA3D-kNoD3ltdv4KRqcKgESvT8lJeZ3-MhlhZ_yZkYRwZTUE8LgUDVrOdajBtBnEdlWvr9RuNWoz_8Uf8BKR1to-GpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZt_Jdg3Htt6KRMC6BzmWjy0K220K3ev0zmseGwLXKqK73B611s2mPkdIDAxSZIz8Xa4chLi1_HSs2AJorgWO02im1tLmsvj3If79dnlnvfo8IP1BQA8J6nxhXao0afSjY6OrbM-sViD-TqjJT0bFeAubcQXXNrkP6j0vxmjI4ai3ZmClWPaIGR9ba8W4lbSVxgngUwSpICnxHYpuGP1Mk22yU4bzPyG_AJzUbbwQGf_o_8UKPlewu-mVrAVGJtEcXGFvdNQuvz0nCYNJf75TILVfHoTjkljW2hRe2VuAXJYkA9jgHr_45B6bzdEao6-Oa2jibsvRWKS2pxLyRQyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5wAH9OJ7zAdfw9wTQBL-3pIjQ5QXCV8d0S4_K2BvP3NPE23EvQ6DpGZ3TakVIlP0D4CGIa23Gsj12SBlW-76nEypECgR2TFWPOzP3OVRktb-L8cESHovx1XssYtJ3tZb3JWvu8Gx_9dVnFzwVY934guk468bdqJTBMyJTh50angQnUB4NAaj81P-vb75e4hM26lGzG5iWgAxoA-S5lOnb5Fuwb4RR1XE9q-B0s7TdzDE8OR9Q_ZnIdx4yUQ1y3F7tlefuOQ1ot6_DKaWIk_TghB03I3KrwLsqQpOgnMIDwegl5hnxTnBmHxp2JkaZZb6GD0ixAnp1orojzUdNM-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t18w_v7H6DhWLNrKHvV4ZF85Q_UZaJ7LNWljtjCPtCNoJ_xANaOpmf0q11nSBRc50CvCH7tRcCBxaXHksbKMX8e5-TYkZdmqEWp6Ic6IZW-hjriBh3EFGgX8SlqIBs22JM3u2BUNSylME-ZmkH49SPyELxK-2R0l4cc8PtdbI8Pas0r-3zfo2aBxYRA2V17Q7oARi5-n6aChA4YbhGZOJv0WFUxrPPGs4dx2fIOe-qQdyLcHcR1jrZYBYzh4BPyHNpB5WXa3AqSdyuvnzBeqHut2dMlUeR1DX8r3AyDjD3s5fkuR7Pq7sDN-x8X5VbQKNsgnStuTbivScPpwqT1w2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by1UgjPTifrbxTOc4GNLqzOXa-xxnQSV1J9eRgIYitMeD3SS8J6YRPAlJup2wI059m5JlMhhNtAobk1xDxh4l0vp83mAhUVFTPIjEpqUteVudFgOaY7D3FBC9LO5F4WNFEEBhO5FUbUXrmKdc5VQcE5qiJDBI5demdYvwD9Zs_Mns9PyLDmyjq_gJu4gOV9nuxHm2C9FMe1PmlNKBpsM4m-FwW6-Ph_kxl7OX6cpu__O1Z1yzIkNI0t_55npGp14SdDGOz-IwTIzt4wgjcxsSzOzOMWEM0T9L5UPXljuBRDMkfJ0iR-IrjeQxtiqUJqJppsaFGdfS77QZc15_a-3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXYG8Wsgu9seqhD_SQV_94VfmFL6p60_TT4oa7jz0e2EIrqP_BrpTLOfNZQgoEJZvrqg1zZDiwEZWVrJwfEYzw9WCHupxQH2yKiUiq2P3RO7TKRqtWp7z4hN9bwwp5PzUWx5AuTc-G1Q45Ib8ccfUCwnvETxczSY0fzzk20Cs44DEP4qQUUya4eEK3U2HRZCsPprRxnSebb4mUwShtvFCj_nxw-7K1rtfnOZJiKhvFeULw8FX_AAh8Cdm4TNbjYCVeUXcNrnLllvKToYkJU-UqdowaeoahBTaVfEkNZsTQo09GNMHMVVO-7Qk8qQ-x3jNqI-fkP-RQRG3ub3bnCRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLKuuOaKfsUmCYDdTbVq5wCeR5qgs3dDO9Gg_L8XKW8KJx7OaTWGmrhZNdSemjBBbOCuAIsoc-E_cmPeqzLLg1MM9N9n1HhuSL3Ax1PDdkvFrgYj3YrwOrKfvQE__FmhNV-jN4hn0RpAL6CMIMLsM1rQ_z3aA-c6FYv__6Ble3t7q1kZ95CtWoLtTj_xeGLjYFsXTiVGmJMW2lwrEAJrf2fYF2qRhq0tMWvtMny08xjUenYOU9KScHiChWSEToqNqh0WGKBIO5aRXaap70s07IzcYOms4-ElnjprwiwB2MhNze-zIQleVafAxvdcmV-98tmPLwbguZ6ISxXLXhEw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=eiLMvEV9Oc4eQOobNB19oIxoWcnhaPDNl5J4UhVtHa7Y-zeUbXa5yq32NMRhoyInhM-nj9WtU__jc0KFrOQgDkUYP8NnZ-kyXgP2BUyBCHTDzRDEe2XnWZiVts4toewvFtkBPPZas6RzfWfN8ihBieCWh3BF67CarxQE_Z1jF8i-vlmy5dkn9Rmum67P3VZCau-gZPs-e-k-PXsP0Q_CADjnR4Xm6_rh2PH2nlNcmnfZrJmpoFSpyyoccrvgngBudTLu6aqkRdafr8hdJmnNEoKpeBqmA7cgCX154tWv2U1GovKSNSH_n6drKzg92f62b9_Zk-26b6kG-wlR5nd3pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=eiLMvEV9Oc4eQOobNB19oIxoWcnhaPDNl5J4UhVtHa7Y-zeUbXa5yq32NMRhoyInhM-nj9WtU__jc0KFrOQgDkUYP8NnZ-kyXgP2BUyBCHTDzRDEe2XnWZiVts4toewvFtkBPPZas6RzfWfN8ihBieCWh3BF67CarxQE_Z1jF8i-vlmy5dkn9Rmum67P3VZCau-gZPs-e-k-PXsP0Q_CADjnR4Xm6_rh2PH2nlNcmnfZrJmpoFSpyyoccrvgngBudTLu6aqkRdafr8hdJmnNEoKpeBqmA7cgCX154tWv2U1GovKSNSH_n6drKzg92f62b9_Zk-26b6kG-wlR5nd3pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKhJ5d8x-mx9hR76qNFGQBUq4cubJsvkaQISfg6W-BwqpG1D81aXYRihevM_UNOZrHpHkajLC_kRl-oVH6xiWBdlNUA67VJGmT6j3QB2a9sUywHSWC3d1KuWkjrF9q8gEFcSn0ne8LQWPO4b2KYZGMxf2gv9xSd_9Qh4kneoi34aIuqAqys7fsFLVPEF9bUeH_tv3aYxEMCW3TFIJTX5SbDRoDy1aqaAFd7vq0Q5MgzwOFEOsbWyCjinSigKOJYq61v9Bcaw06Xsp7jYeMX2iHzUPhnCgMBNK7NopByKiJEEBVw19YJLC6k4aGaYvR5KMTW1B84IiA2tqPRAhSU_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJIEtrXnRVV11m3QB9d8n5apWfsuHMepYmBYzvC0wrOInAOYaFbfP_pZzXnZo9tG0m9o3M9k2mscxC0kDsy3bXULjzRslbPY06JpBISjS2lD4WxNQbzEfjk1ohVWjfzcx1th3ok05tJWC--QTOcyYAAa48K7zFJg5cX9YsT4fItaMGROD_nIJrpSJ4VI6lI50Ll60mjxmjqXm-oaB53sFaX88M_XCsXGAmbbB7kdRnAIXDwnzSyET-zhIuKw-f_51AtIYRZw1i9Gd3J3-HzE70Wpw8_0Jh0NGbporylP1ghcVpvPyI_yqMFoZgrm6jdZ3QrGwPTMjtaqXzFbor3sMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/torjJMgVUGcGhSauev0_BAZBI4DfZUHa2XN4iIiVeX8kNw5bbnFGJuo_aWx_aUQoQ_3T2IgEDLRBvaO0rSUDww-K2CgZt2NbHdZHU3BvVjrltlKmxXM1XyWyFaf9_VWpy9ODXBQ25GYNIH9MRCFD0ZdizXMv5Xexnv4LvdmXK0W5dJxEJnftHfzIzu3yXe5f5V7RFkGvVD9bK4xQ2xN4_NxIMqQW1-Ya8XB42pIMlQ6ETFvK_DRzh9WsPvlYE0D1uhcKX5zBMoWHvGJE09JaSQ_-2JXD5Uom-p7OqkkZDE6gpeTtoU0M7l6JXtWlC-nWEQF4Vj1STPJ5t3H6rwf6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea6R_RsbYC8wqBP3XVjgoIS0Ux-A98hUzBDJt_rhxhBGlJKUawzczmrzkpvv4MqqPjvFB6csL2Rc2KglMjxPiqyUs7aiVmRWSCXq3fhRCQfvSlhymlaZTuFTEVnbUDIwOBLC8CtwsschmHZ05qxRkmGoA7LDK-jjoT0WdxF7eXLWjxzdUNOFgF1d_PnwQfeOAc4d-5wPP5kNq_yGZ5DatHkxqLxPdL3f83PvOgLrvZDGQ2knZ8pnXOWLy2mAng2zxEf_1BCBK9EbIMjx9DT9PKuR9c7o_dZNrSlyWJJuboJgKYhtD0wnwPDqkrguBfhkPvQ7N7aPuD2xPzOhcEFHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHjixgS1E7rmlZ3t1oNaR4l2rLJCS_z5sf_7Cqkqyj4-GGTw0ZMgs3HoYoYagwLVodLJilVW29Mnt4b5c3kUZNCavCpogkxJL0L8tT168nAi5tLLGSBIwKnm5ck2iRBN1smkO00Zj5XKxodbu9igny7d3gihWChbEb21K7Hi6xeqKbCXw9fqZg_adk6JFf2jA5CJyyxAo-WtR8yVqZn6J6JOn-wjvprgi1s3oEZMAmqLGyfvmfAE2RPd6TxZZTavhrTm2Sm7hXOysBv4uxPFSGyCOpCNCEW4YkoDEz71_J2sz2_9uZtyBPqc-yD-1caiH2U-Gscgiy5ya_dW5e3tgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXsS2hpbZZd_YwHHYThMyRFv15wt-DMVt3mCVsEEQrkzl8reJJYxS93DU08TrQIY2BJu1UDUofXIPtA6fpk5K3jvdrSJS5qfleTfc8xjZnDJkaaAIT9XB03VtXlJ5Sbvk0yfbFx8cCEjEro8HPy3nXgwobfHKMigELx8-BHTNSrGfxL9TRQ4eMAPook8kE0iIbOWtR_hmD9kiI2eb9D45gtVaIPJirVcszoVy17QaiFCDxqR9jRpZtsdAx7Zu2_XTKxL7TcTtIpfE4Z8uZrQ1aQAPCCquqVQCsAgJtXZLRbE1-sl1mJx6E2QJJA2oHpdAgEuzTxCmyydJdoMYG__ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIM9kYRqY3jGXrlhVAhs0Q2JeT75V6n56TJkyKOlXchGFI6jQTXdxkp1VTo4STW3DBOMfI9694Agn6nHqiBRTRPKH2efI46dZWfQAkIIkIl6CjA3KiVbh5fYxKK_rYhMlig8eUz8rHDPmhM3cHVqvQ1deqSnsmPItAYF-e6xBCknY-UjA2ZU18tK7tfbE-aWjso8XJX7h9CogHM-HdAUYTIgq2W4b-Y_UHepZkImOx8M5EGOnWDQvsep6dKdXT2NIghsDpAghaLZV60VilDAoFMkFTPGzZ_0JcBJXvZL0R_DD4VmNxdftm8bZ0xlFCYJMtFAf8YUR5WUgY0D5OM6Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=CIsgkv3He64R2nBbfYGP68X3DYAYMWSDHOkUXQrVboKrYJ1rtbi35MJThEVmRNcrEztK9Jtr-MP4ssH5IUP31C4Fn9p7HVsZqB1yfPElfV0bPumViSdQkzZCEZnxxmnJ45oKryc0Sh1xOr37Hz9G9gO7aOmQVQwJ9ZUPm8ULFL8tQwkKoIAHmvQjfEwpH79L4aAWRpv4ER5pXBcv3yAdJ-NucZySgHtlpGAS5_uzEecT92gOlR8Yd1oRPz6ux1Kk2qnEOZCEafF0ugMI5c7Sy1-AGINJEfMFUIuPUUXs9Izdm8haSys-Y3S-Y06IKIV-7-JVRiwHEnZfqOv5SF27pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=CIsgkv3He64R2nBbfYGP68X3DYAYMWSDHOkUXQrVboKrYJ1rtbi35MJThEVmRNcrEztK9Jtr-MP4ssH5IUP31C4Fn9p7HVsZqB1yfPElfV0bPumViSdQkzZCEZnxxmnJ45oKryc0Sh1xOr37Hz9G9gO7aOmQVQwJ9ZUPm8ULFL8tQwkKoIAHmvQjfEwpH79L4aAWRpv4ER5pXBcv3yAdJ-NucZySgHtlpGAS5_uzEecT92gOlR8Yd1oRPz6ux1Kk2qnEOZCEafF0ugMI5c7Sy1-AGINJEfMFUIuPUUXs9Izdm8haSys-Y3S-Y06IKIV-7-JVRiwHEnZfqOv5SF27pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DERo5hfF8SyPOINY2L2coXS0EiO4RS8_PrRp_9jDetNlAYMJRb5sFSH7Gk1pzmXRzvNdQfPDV831kAvkqxLPr6KYcNkieBDcA2RPB_evg9pEqV2CVxTS3FfZ-MrD_QkDKAX0g3ybQBHYv-xHvPQGx3OpPaL7FMGG0pk-MYGvHSGhpy8CE-LVtXgQTYyEHCgUujrRi48s_DmJ5tieIHywcxF8cf_jyfJfcP5i_rIJP70hKpcjtuC0yw9TzZBOJ722vkn8hYGYlP0Ey9Fo7XhTGsBW1HkPq5RNq8LbbgRJTTq3yvb_M8AF_75cOOgIA_nXGfc160rCJXE8SBZHQoa_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
