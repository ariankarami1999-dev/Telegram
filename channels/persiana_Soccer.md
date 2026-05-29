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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 23:22:49</div>
<hr>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwL56U5IWcqFyW4p8Ylt40AHaIEm6VZL2qEspmccFVsuTKojE7K6A_Fq4afrd_2IbQcwGYfUmg_yR-E0oRWHvC7NNH48_ecEQveCLTmrN-jLYeGwHrQrJgESiC3NZJKiYp0tBv3_c5yu6fAhFv3JkbploAioAGzLla5fY29ypzTyAZ4kgrxdwyYGg_wG4-GYkbn0DwKQKU3fsKibbvLU1qakaPf9TfBkffWGEN_-hqGpLeBhrXX1nv9fyrNbnsvykBWvUWsc0Zq2fEli-SjDYKjfeb3wSZO5Webd7Nqf0UOiVvkv05_q9AksSaJbSCnbrRIdMHLNc2p7qfcnyO6rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHWQqevTT1jCmTRzMt7TDYwS36FOj0SxWfjfBy-15x9OkzOHQ16hNUOr3BnBOmh4HmLFgCU9jIaP7fmbiw6AvD-RTf1vzI9trI-PM-6GUYbfToEkOTXJgjr3nv8eUo6JXmYZSqks7VO_GTykXxhCogtcHN-ihi8K9Ev-n-zqH3eozpFrmFi3zxid2IzyG_tkRDBlOu0TV5E95snVtiE2a44pjbhU1xylIuK4Fxmr_Lt8uhjlQbs4HQNiHey82tnCk9-OmTtnekFRU9azuFHEBOoTk9cAn015yDx16ieSgdZkAVnihdfucaKuPgyQplpE0mcmyx0IPn-Qobn9TqF0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW77n8e_ZwS-Pb2KuC29uSKvyAu0hp6d2T_VF-qV4f_GrkKtQ-WRAmEOWodb3W4IcI-vHKLLk_gfulvEZmNYZzqh8y3qiOpw4naYUSD6MP17Hhe8w8DCO_bsb5qS79jic_aM0UXWZ5dhHG4f8Iy3U63JvxRTur3T2DzM64vGJG-DQOHrRPi00OWsbLbCl46qT3kZzP4poDx15tXqf0LWkmpeXzajVhG_BjNQEvneUiz6TZxx0rVsETj5hGcXdUaK6JewE3eFaN3QklxR6YCZOXNHJEAcFKTgGYOZRW1JOHIVYiBaF5vcYrSWgVCFgZ_IGRkAjZOb5PaU3sFmsTKwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22434">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22434" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaKsqDwJasLNPJqlVTR4JVElWmdZaJPNZVtfnjNd-iob7xzN3alBy0wrMoDeS7okjDOIsADAlD6DuI79Rsol-6FOG3Aj5giDscYnHxjdC-FtHFBNI1ZTzDPVCv_qsds2embHC-YI8H4e8ll_90v6g92SzACsQXqia4GyaenzIg6KWKonwESyptaatooLzxOJBiNAtr8VNxAlL2YtRMPObyWGVLn-UcmYvs1W6C9bPQSTRUt7ykCkX5dX-X4p5xePzlBqr80hF-L8zz2eqAnrHPj4t5QDKiCCDoqLncF_Aao__NeQWcb15o4736H9yAAEvpcdAqPSJ3xJGCH7yvaZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwjgUcFSFOFPzKQrM-yClfi2ak1tvJKKlytZ-2sRKXnolqtfYnUER90pIhKWVY_VKq6DOAAbq81-_5PcnC_9s6P0Mh4RaV48JCrhUMUo9KOPPEn9k7ULDMpkeWHiGnmeOmF4MxsQTTQFqNvue4T9ahZ0rJlXadqKRIET665V7InUMfaHOTvnoRtRYC2KSqOqaut6agLXCTy5_thAw82b82_rwd0odpBjsHXq7R_iCAg7lg5vuXYcS1HqASo1mQuMt3-75DcXtVFt9U9XZ8G_3T0_0A7PKfDwTjRqn5ft_yg9dY815hyRwg4ddqMmER3dUzmWuSvBcB0Bdyy_g0gCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgBrESRFP9q5GIeTdEOGNqn6sTDoKUlXBqEH0VZejMQocHJv0d740VvfeaH9rIVIDos8IyHIMz4Pw01xWBECT9f6eWkOFYZ57yWZGVNhO32tUJaOpKFXddVdiKXkTmdGOwToTsAGaXVNYbrsStZmHbtA4eONwYyg0A-Hn3AixAj1NlnqddZXK8NygGmcxixmB7TfpN5aU6DP7TlrR3zZuw0fuRmYFLV-KZ32AeQu2RTN3RWhijZzuUZaE876Hex3Bp7FAQ9mkzP7-1t2cxR-c5AjT2GlUtULgYnehh6PoP60QXl2hHxq85PskrX4OCri4fTTufalSnzM9RspGpXNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7qVMwCp7dABu3R1AEFPC0jamSJDVlFOv3f85jGIuhyJrRdViiUOZEyd07rtgmtolfTd0Conm5tWvI_dzYWJbvW4LuymOi-nMgwowgtP59_buWHp5Q_0MdHPhxAPMYZdh1b-JN45zkVjcxbRyx7D2f98Yr8YGRY1lrbjwcTHP9QtwKvXB-tkn9sRSL-aKBW5mH03VoCgzdkJQDjhBIa0En9izrt_JcKnmBJCURVOvF0-Q4dneqZdiyACYsYYKakfU6uZ5f1b0OfwISazKf6SN5TyXecfyXe-eQsEThDRzQTrO1AiOonEkb1j-qJAnmdjf4i3b_58BqrJAWr2V9cLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsNPDERe-6HhVbcImpnQOs86DRNEDnLy4SuB611GEG8j7ibsgyQYHs82tcJpHuuT5mwVEeY0FL4AEt6J_ph93-gH-EjKlxdXswLWdJNUHR-p-z9_IK6kldzTJ30vUQ9cg1uWF9GXJ3IFmJ96NqovIy8KY2glF-kc7LHN6FKxozkE2K_WVbzdxpTla7xxxn-Mwkno2gd1YsQbR_YM7SQR45RflrsgIoW-AMTc0rW1F2IVn46bbNarui6gUDCGzTybBaAeSNd5iv88fylXMAiC4qxKRSrw9RdEzg1_WUN0CydPW7ZgzM-zemwBZ1pMewecQZH-qrrNPzdIHJBlf965Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBrd6wfgM1mT-JfHt986eUr_FekfkunGY1u_F7xMjBR8osUYOWPJDMSfuIx5oWjvY3hvj3Rd5hYlg_g-0GwnbzC8Mhb0smqKnv_9DpM2u6XcdgFh5hd9OzgLiKOvUJ5oQOx-Dd8BEAe_6EiZhb7uru_8Ezh3RfdXiw4oZTJQXRptmdeMiDES_RDguj1-PsLlFRxEQbfch29yhEyQyfzr5krf2nBvIGY13vUFZLiNJF5oj3QbHPcsaQY3zn45dMEkqc2v57bdp5MVdMxM0gcqjryxESajnfmIGountolJchOODcT3ZRVFWeZoEiFhxTIG9poMBCXw6rx8-mew7pEH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHkZE4Vrc6Mf2PYFRK260rshwUXmMHerr67CuDAp9XxmBNxFi1wSj4yXvoZhj7BlMcK_GsQ1yZPjl2P_F9hx97hnRJolGGesvOTOjzd8M4KY4kLEQg4jixCQgRYQjb3k64x9AYwIZOCYoYBqrSuhwFu3kS5laJHQsgLP5gIsGTPIamTqEq4OVBdN9BPqPU-l5WLNyndLgTRjBANryUghScM3wc_JXhI7Q5tbEVKcSJ62ixKjM0czp7tOAhxFtfJFGCXSbPJ5Y4w9lhF6O6z-nV0uPTmI9krirrC9esBczy93rMW1vKMFgh47-hmHHd8SAFMgmU88IjrQk6CSQlwDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA2QeNw6AQYtn59xWNq8LZfiFn2I-osK2tHQRtVacn_vgHrBRO8IH4DshTc2N3DrKMDK83XZW8mkPBkJMiH1gH25sp9HAVhFDJi1Wk8sfPyH4enJOMSlARiRfU4h3sUjxxVjElbObBs1B_Z9y4J9kTgbnOvAceGlT5vzh1qISIEPjCFhZbpK__6BfcWL1joUbzwkshfU0bET9pUmDUW0qmbUfxnKlgK5_UAZtPg_DuFhUhShrHrdY5j5fhKCarPjdk2RDflZO_-vNXlht9bLFJln9nsSZCMgjqufcYhqU1-EF3AAPB_iPZzF3sl0Gl7QJwiCpM9ljzqSwuD62wqrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4m45Yt3X5m91rb3bqMPtd-FgRJjrwmmvppRunJOebxfp_UNyQ3xYV0TBWKtolNwxHtlfdUFvmsmkll00EA9fgPEE7GerBwhS43IVwu68HJSmjoPk9fL0qom0ET3safwaaM8judu67LYnni2RxX6ELaKd1aK3deApB_8T-61R-VGIQU1Vr4pQ54uG1K6okPlswqvR75_EFJq_CIcCF6sR7c0E6csWVWevlxGPjpTaBVrx77cOMO4FR-NBT3fykO6t2V5BD84unfutcFT040lD52KwCkspT_FLZhbk3v1yxtrUZhzQTJtkOFYnuTjhS2BRmhvwATM2jHmeG_cONZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5jpgXcipW6z4Vwg4OAETnl67lundILyPe8hYIcXLj4xOzr6Yj--9avJLLpygv130LfkVej-M3ghLlvZldNSPG1wYHhf_9gu6Su63zIHOS1Qs9kIzyKnSwy7A_5udfme49vEka8tpdBhyvPWWWXCugxeDDrQvgFdWHBN1yvnzrTeeVCFEKUdC2NQ5FrLzZ7JyBlsXT7PGPowTdfhjum8l_JAXchchL0NsEUz0MSNaf2BHOxDcg8dxRs0IpR3vznC6Ur3_xcWyVpF225K8JdIQ1qqqTSUIvl73iBAo75R0CtTYFsGvPdoy3eiYjjvpHj6p1wCcGriGNnEWq2PbRrpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq4b441M34tyELi16tz4F-N3OHz2lzWN-OK3j8ncDJ8TQcA9AzdvkP5ad17YLaxZf7y1KX8EcWswUseL1uqExrWLpSZNfSr5B7SE3E2ItPDK5OtFXpa_KvfkoBWC51lE1e1Brx0lg7VDAf6PRmigpv1um96Sod9JAF_2YJ0evzFHGZu2j5-CzQgErhmqiFf9a8cixPaRUCvnKmDAfUwfnCAJ3Pnkpc-zsuT1I_Rc8R5pgj87uqDUOlVUbpjagr1m7J-yGX0qyGSqNDaKdmLSCHQ_a5ndPTib7DNlLZicy6KUJMjMkyhWRX5ULhgLmd3XykIw41hq-0d-6qquJTCc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uim-hmQB83m5MwaH5enr-yZJVVTh3gmBOfoTUZ_ELE6RcJIE84yFbcwVDj-LKo-fBDSqKEskSiokH2Ed-AqoFO9M3BtrXcDFO7Zt6UNbGO9hnal2EtrnMadc5zUs2W_0Xuc7cTwmTEY6XaZ6uKRSnjymsh24HoKEvksMTEFm9WadL2NEdtNW-EYup4_w88nuMt5LPq_GdrSHQNXx1izO0rlo09L2KyMdb6sMH96_U9mFf3jXLgelIw8g5p8O6X-0bBGDuM1A-ATU5HGgUU2eLVf9D0r4EDEZlgfJmUf18hbCYNcxWaQ0ClVukip-kzBIt-fkXdwLP-rWXpxcxCrgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej9myXIU1TvvAqXoWkr48rV0TAwQ-6FYBXgezSnUZh1W9ULuQoWUIKH-f_SPrqOiEsXxr4985HpxiwW7ocGmq91QPBE2aH6Eh4KEAxiK5eOxejgjQ4SyZkLPtmrhpy1IjbuiMswTGTlk6FQPWeJpZ8pglUPKmplZ-pIMlhpNsKhbcmCADvcSqKadwk6E-te8VcC5e2oWTT7qFo8PS_d4GZ9Ewt71rhDsz-JCYwd5_FWz0gWsq4kbK6vF5ROiSfRDkxwJ9TdM28PSzMBV4Fdz9XNhlRjX-lTje3SOA6SCfbsfhDLQ_HicWdO99VtdliIairROo_NZUJZ_5-We0WX-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djM8NsMnK4eKisCZKTOgSf9J-INEKfyRLkYdMzC4EtIunnHOifZmRjVbKLOBhuj8p6_RC3ZflDvnDFHxvbOtMZtldyp14w3___FxWgRsv72lGhcghTCvBoEMhOZGKERBJ-UgGdzhoUjCzoWdeLXdnTZYw_q3dlTdV7GgwhHxoUKNV6qx1xEg6YSVkrbzgF63mHKhZVHnVPgs9yV8PJV3Qi-EQ1UzRTP32Npy2SBHhaXef3GkaXNyEBY180zgFdeQVB2Bin2583GZrKGsuQijOuxqoWtx6eOeUW4IO4b8b4_ymc_NeL6DXwxpEXhh5vHcGzPszdJjbcBA8_jLkSExKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW9XU4YtoyEKX7bLJ6TE0Du-W903flX7LIE6vA0CHDZnHB1VihaTH9Zg-i-ZciOBObMqMCRZVpyIYElF4XvEFjujYpjiitQF4UkCXL94VLFz2LXCWuneRgfN4X1vfpb8aJ2SytIxF7i4VfMKl7aDpR2kWQ1KVlekcayHKxNIhVTfx7sCeZ5BK3K6yWcEuBvwaVI5tuPvOLPHtBTjqcnVUpBLutyiQzzsblYBoA2azxMYmFX4_mk_TqxKNl2MIV1umH9T9wO_gAp1SKRygsB12LubfNxHWu1wedlxL-QSP9NerT3qS8uAJYbELMpYsN_Ezcp8EEpQt1Bfd4tKBS13ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzK5EvYf0kBk6lZoOkkF8183_EIGLdXxmSWEhVAUDs2b_J6W8iW0_wk4dyK1JvhAgNqykjmVIEbeaLQdsYNbPlJvEzhdDTkt8Fa224_nVHx0Nm5Ean-ZE5mi2enuM8DVv8xGBPc2TUssmdAk7F0PecsOsrXXguzg-Jer771_f_JxHSgpNmfih-iZqUWTOPPFcU2Il6DOP2rZqogWFqHaCH51nOv8zh8w0w6dRBEiZpTv4_R-3WWFEZCH7vgINaKZEZNpCpH3IWdT12QIkYjsdrrSACRlzg7oh1_NLCisfI-CjOZ-6Lu4pr_3_1BI0DIxDw8MLArHQ7IrIxUsUQAk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT7s5HO12TUkbw8DN66cHcPK7snLxGa4KzBkepkYqh2-T4BNL0HtLcwE2Ukkko0MbUR7GIM767U-yjeNZ2fKeCaTRTA-R5ebRcuCin9cHnZygsWlo0kJ8BnYyiQ_pG5fo7xu0EDd03BlVKrMdCMzAsr4QLCzFk51QNwV8P6frgJw2aKCt8xNaslVRk0fEHH1LJkkqydIIryNTDnEP2BXZV162opwPPJ7Q7cjIs3hUHTha9tc4Fz9W2oV9d3QfTm6i7ds7HplSc0sddroTdAk33CmhaXdJiUYswLRXX8TR9cElSFxaF9VmM5zKj5xzWIiEmoZnLbLWmpreww2lD58Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22413" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfkJXdVRy9CW_JMITsWKbCTqtY4gtIrSamvbO99_QoNZhbg5Sr2yoWrDk0yqYWwACujQVPfg_vSjIAXqCmqcpShXp2u-hBimRKOmMZxxZezCE_Q-wjQxtvMrU2mW0WBxM3SiHPbOj_C3Fms95sPpCRqxxgoLTcyXrqUbDBEfjt5DzftYEVIhZtA7pPqcXtRAB85J-zoyfUrYb9dCSPwVr8skxh5aXutb5RIJyOGvoXojU_OY5YCZtr-Nib7khfcBgxeBicMiYyWUDMYlfOiWsPAdUpfVkULcouxVTFyA7MDKQlx_3T8gUOJeP0mxXk0v-NU0s0hzJ5CO_gjYQI1usA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=r5gYfHEA62vdn4DoVtl3mLH0j57XbIHTbC7cgeA8EGZKzs_quvF0I4gdJjMJ7lIE6hEekkjksGzmd_6SlRKMmgHDqH_SNDC9EcIXpCfng2ElsVr6wRiGnIBj-NpvegnnOcg1yKhuBU_fnE6opGLbQt_LnASHmjOSu0XjJh4rbr1naiHXs9BPlbV6xK-_-_3YFx8Z3QVouxxz02sLy9E-eoT69ww5h6l7-Obary12teHd1J4jxK6fNNlJnaOtxlUQfliwwsMyLptlKLSVDRr1EoZy9-HOOyGh1mvH-Vaf-lxP4SYSJV_gack40H_atIo042X6iN_vLP2XcGQTKx-mfw0d0eetsyd_hLXNSkgemRjXP8NW_YWVt6I1TuyWqebt5rBYM_DUj0IFhL1WFFRW6EbCWUl8xdfaeZ0sO162gFFY4kN8JpfsYClxaOCBV-43wPPpEeHoDEXwvVzN17KFIU2wgltvAn7HiWCUqNseUU0FwBe03RTGEJ_y7vBohbIzhKQESMZbAu1RN2erLhgXiG-B4SqyzyNQZfTXDowCDPV-NW8WEYazppCiwfB4iqdFvOjj_vE8iajRVbqItqzFKJ2LMxXKPO4ap5bRi_ZwrspS3qdKhidPBRr4iXaecbSCeNNPWN43ZyZ3-GRPlODMczV5VI2A-iPLyrDqGqU3FLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=r5gYfHEA62vdn4DoVtl3mLH0j57XbIHTbC7cgeA8EGZKzs_quvF0I4gdJjMJ7lIE6hEekkjksGzmd_6SlRKMmgHDqH_SNDC9EcIXpCfng2ElsVr6wRiGnIBj-NpvegnnOcg1yKhuBU_fnE6opGLbQt_LnASHmjOSu0XjJh4rbr1naiHXs9BPlbV6xK-_-_3YFx8Z3QVouxxz02sLy9E-eoT69ww5h6l7-Obary12teHd1J4jxK6fNNlJnaOtxlUQfliwwsMyLptlKLSVDRr1EoZy9-HOOyGh1mvH-Vaf-lxP4SYSJV_gack40H_atIo042X6iN_vLP2XcGQTKx-mfw0d0eetsyd_hLXNSkgemRjXP8NW_YWVt6I1TuyWqebt5rBYM_DUj0IFhL1WFFRW6EbCWUl8xdfaeZ0sO162gFFY4kN8JpfsYClxaOCBV-43wPPpEeHoDEXwvVzN17KFIU2wgltvAn7HiWCUqNseUU0FwBe03RTGEJ_y7vBohbIzhKQESMZbAu1RN2erLhgXiG-B4SqyzyNQZfTXDowCDPV-NW8WEYazppCiwfB4iqdFvOjj_vE8iajRVbqItqzFKJ2LMxXKPO4ap5bRi_ZwrspS3qdKhidPBRr4iXaecbSCeNNPWN43ZyZ3-GRPlODMczV5VI2A-iPLyrDqGqU3FLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=JM1wjP43AGPIWN4vttMNelB-oO45PVdURxtEqDCjSCWLfsz5Xtl7WGMuBWG4AKi9YM-BQhsCb1DJDJ5eBLZox8sM1Q9VpjDK7slRui7xBc5JSveM53D0d1WSnADJR8zbJ7g6FR2pigHuhLDf89Sgq7Ps0Sj_dLuIEsbNdsPV33otW9IY88HHu-o-2LqaoikG5C1yb80YmBF4IZC-OrBVMgG5jXtdFK6tT2SqtOwp0TD_LkBGn-3it4AVb9HkLdAMd3Kf-CGtMCFxqUB7fL4dJzfqXKi5KT7mQk1POAv1lXRGYUzRBllg-OApu_ycXeVG1qoCFryWmBbS4PV78QXDrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=JM1wjP43AGPIWN4vttMNelB-oO45PVdURxtEqDCjSCWLfsz5Xtl7WGMuBWG4AKi9YM-BQhsCb1DJDJ5eBLZox8sM1Q9VpjDK7slRui7xBc5JSveM53D0d1WSnADJR8zbJ7g6FR2pigHuhLDf89Sgq7Ps0Sj_dLuIEsbNdsPV33otW9IY88HHu-o-2LqaoikG5C1yb80YmBF4IZC-OrBVMgG5jXtdFK6tT2SqtOwp0TD_LkBGn-3it4AVb9HkLdAMd3Kf-CGtMCFxqUB7fL4dJzfqXKi5KT7mQk1POAv1lXRGYUzRBllg-OApu_ycXeVG1qoCFryWmBbS4PV78QXDrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8j7lcbDamyAitgfrvvBP9Q3EKr45-RO2_0JzvR__h8-xomCbaPfKZUwoQUgiQzvP2RIsRBV3TLocpV2giG9nkfeLT2Yk6UmI2kDcNe491vUyRP8ggBJGoqpGWWOd4NAuBR1tPGWLIjdVh6aQ6MkWndG8wbzujxkDUzhDRsdQ1L4iXNyLMCjbaqUjWZp5FNJx4hYX6xlq8Lfhl_Tnz9R8CXtD1DIC6RM7wp-iIVQ_niY6Uab39PuBmThgPFJFhG9SfBu0XIyF03AGf4uQ4u_ts_qvr4vUcm1boRe16zqKmgwGWOb5LaLSFeZTOuYVTy5iMu_-8qVCaTlHC_OxfhXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUNa06tCecPMXpV1qfTENWcTGKX9dDQgAvI84K5M5IwpQgGkO-s6JDhLHAA_Y3Z3DFaPHok4VgQcAuzStYYI2KmP8doArgs3fIN7ivURzyyYMu7jJyjW_IzCLcxV8XGwhDYg23ihp8oYszELjW6D1VHAPCLH2xKEUUE8prX66cqDiwFdxhoQg7HfjpvOGAIDM1bfGN1JlJFBASaow936Fd_rRAVO8_KNYKGEOuY-7fPcwc-wFQ0uUAai1IBy7bPLJxr_VNO5wdsxoxJDpBTu7RG6oRXRFZ_rr8jPCgRXRSQGU8RQHL5UlMeaLkqX6VxhHlpGDhMsFXt19gK_gB5HKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-9CwYve22jzaRCnV2wQBErlUXdbVTsWVCNc7Fxqij-y17B4AhpuBHgxyhT_CF6SrAxp7ytEXDESQA3pXYJFSCPURnnT96q_zWo-MdSDqg4HN2c3XEEGiol35p6HXIW2kNYyCIcfdChB3QP-4Z9D5A9HKLQB-hAYZv1Wcbuboq_M7mK7jL6mPfj5MhX_iPz9gLBDx3YQKl411MPyHI5Ch-7X39oaMwxP_fVSJ9e_TWaWX6D-Et6QD4Q1kfCBhYUS6i9IeXKVW61l5olu7QVUnqVRmAb4J7eshMgB8ZqMHfF67rAx-l1QkRKdDl7hRimPhKrLjb0vfbDlBTWwybRQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhztGGHv6SLjhBHYcij82yA3MvpwCjeb1lVHdY9HjzmSm59bMV-JLI8yWDBTVOteoQJhzfKrXUEUkjQjcWPm1RH2NDCXxHj1sWj55HeNwj6sWOn4-yVKhZgTApjReW3MZSvTXdXEbfTwDPW9shGu6NlX1fsNNewQdBjS8W6mjecZix-X4RsXJiGO_l_r0L3eaSduvpc9w7EQ_4hAN1j3kflguNWe4D9xef04RwtUf8taiMMYhq6JCfOutd3_pevjI29BqI7Ziu0IiV14jMOukJDTkAFdI1mssAvH1bPMuav0p9lQr1kblGknTaXq5lhxMEnRtn_0DjnWZm7Va8OmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMYLEa9Ad6SOiB72IvxLORDiPPorAdgFoQEqUwujNfLruHPpfIxpb-AMJ8TfbsNFq9x1wxZ29B8R0_fhpEi0wQKXYJIaCwItr6JVJu3nF6TTDVs8mMAH5iwQaT9pziiFxBFZ3TwWGvEKZSMMADJ3kAzPtex_j0VzdCKyiKg-JsIPzEGHLkMYh1bMoeqKyMsUtp1Bno8iSfVRQ8NmEiD-9iY2g6FDyiiaz840gRUtl6mhKcSQARZOT4bcwWRlJ2xaAgMtNnqhbOh3eGXtrah9RQf4cp3HfScnRKoMifcXmS3IXmOmIz-RVHmFuyPKfWTi5br4R6uWkdLYFmjVI_Yg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsU4JTj6aCBJWRQohx1PJGiNoGm5TpOmzG6PaxBW30Au-ecGpum-cA2dA8A_ZPOX8Vkj6QSiVbxtFNOKAJ5wTaEex9-dMxrvtVVnswhw1Nf1XoalPmvy57GreyibXuotJvffHF2yWJJCBprXuFxE89m7pAd7Ll_P-l3X_IylQ1y6TuG2S8_ofZO3KP-lAh8GyXrq3Yh_y78sSQbOyM6pRP6EDnzZB85o7jwCxQaj1UbJmOrNuqcoWLp5mW2OLfI5YBd7sGplU9GLq_xOXxxBzVlqJN-I85-NwTWLBmfT7KWgLjUNWk4hB3hmzJrICBRPJuCLSuWDGyOqlNfsUg2BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN1vRXLNyswqOPY_ibbglom3t7smlGgfASds8ODY6vBCM4Zxo1VzaDDdkR1hZQHsRa_pGWjxZXZhlYS6RC28OfRjNmA7LJma9_JBoi-RVGjagZvemnKPMCQGHi9OfdHabehKyRbuz_1RIFIzKwEyaM-lzVEQzgu5_wh5M2HJZGkvsJjHkP9l8_3ZrZJ7amC5vsIGow6jXUwe0adLqQlIJxXdNJDXScMT_ITJ2iMvIV_bS9ccEWfVeocXR8Ms45fFIAileCdhItqf1qxSNHv8eNhiXETRCE0vPzaTfiLgeFwpTW5dmqpdHbavf5sGKTegRiOcgR6z1aY4-ksWOGqAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL82k6PLSRJYx7YeX58jLfZUXC5fA0cmnwVPrbJovK1Ijla6G_wx4fxCIgQ8eWT5VCLqhCHAqRIwzWyEvXOXqI5Hsqh70dvSyiouCwGCCGASvoH0lH-lIf5YQghI5MbwaMdnk0WMg-AltvChrdCm7jWBH1_ywnEJGmE_Nvsiq4aTK5BtbhbD6rEhU4n8dptpQdjlI4wMPz49qP4MRZ9Qu9YuR-BRc0-Ufke32nCPQhRtnUjkHlmqgC-6eZljSEwbwhu_zQ5uhbGdIObUS7R6fZsSf-fzEla5-JEtCAAIK4enQV0W523coTxEaBfmZI21Q1abURsiFg7A2GUreJOfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMzF8ojxMCPFVkq64Hdbs9_N7RHGyTXjxtcWxHdnet6y-iOJjMtTMDbv0hSOtgZ4oEQfbEKnEfi2W0d8v0xZnlbYZXJucZN1WX-ZXY33vDKdSg53-OY8FLIehVZvvqmDsSJY76Ia_7NOf9FXRpI9ZU5gSzSxYN-uJJ4ksbMTEFqn9BOqzknyfZWGvCrNPCmKnzTbF5MstsJqFf1SMiV8ATyp04Pj4r7qkKcX8m2S4BuolO3y5_bay8ycrgiWmB-8wu13y8zSJFgZ2DzeZWNxLjpkjLl9XLKJNwgE8aoH04zaEv6DXa-HrL8bZE0iDLwLgP9G1oNttb9CsWCOLTPj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=ZmTzx2sW265DSXXM_0JjIveVu0YxZWz-f2cZQnBpbYP_u5UPVV8aaW5LWAGym8GiP-4SOmw2vKTyhBjriH-NNvwUcSfr36AIlja19V5gnWXGAdoxLYPts9QXhf4L6ovJfbkuZSK3lXKNkfLinbSXAluQ3xNnTlLiL7qRH33j0RrropO6DE6ZKWoZturuy2oJnc5HKe8b3ynLlOkUj0ikJvdhVW8saT4CeLORJL1IgDNFpu7_pbuxG4c9wI0LkybW4d-b0yKbHhQAU4DVP0ADDA5ptwMPzjQR6CYt3lAOC22q_KwVAYBCzxxXwezCndAPOc1Zgsd43xmKpDJop6TSew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz3ss6ulW24k6tNogVv6Rwi9kIYWisBb461lPRr2VPAzfY6sKHi-mVx0QLIYl15fEfA4i-i0n5sLBXx3KBZS35JSLrG7Hp9xcLSmezmE84A2VT0CXMAuJwrQL2xh928pJq5afAgjBbKmscT3geItSRc-KAXmBh1bJ6y6a3SBZCjDbl9s1QO5Ou2cCwr_VzBrjrIldr0toQerkErZHiJ99fYABP95-Cvr0RIG71EEz1MYNfF2usU7s5JpY8zsrBuF1I_9QCfE-khEYvR0EW9GS5NCbi7emkwtf86YBiZuJv1M5Bcgixe2KX_k5Covg7dKSirvXonTzkVNYnhBRNR2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=dGRG74md_aidWTtrEna8nP_2V3DbAwlzxSvOl7X6DHe0EdH_PyEJg1alvHmeznSCe3S7YSh8mbQiySAaZyA5q02v_5i0igO94KxKbwMImLPjZKOeJ9MfYWMhuIZPVzTklEkO61gSt8obAgPMQCilpSXfBI_FX9nVIhrKICkLn2j_k_1jD39ie3aLxv4SrbsFqCg3qlxBsMSe8GrDh65vvyL7EQfzcsTU47GTRGaD9LKHEQRVdQbk8ZV5uQ11XVJcKnXvlVckArx2JKidjQq-aTZzL2BpnmqJAOV7jr1XsPH-Xfjf2l9sIYisqmR47CWVDNqEoGx2nXt790Ju5Dyv4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=dGRG74md_aidWTtrEna8nP_2V3DbAwlzxSvOl7X6DHe0EdH_PyEJg1alvHmeznSCe3S7YSh8mbQiySAaZyA5q02v_5i0igO94KxKbwMImLPjZKOeJ9MfYWMhuIZPVzTklEkO61gSt8obAgPMQCilpSXfBI_FX9nVIhrKICkLn2j_k_1jD39ie3aLxv4SrbsFqCg3qlxBsMSe8GrDh65vvyL7EQfzcsTU47GTRGaD9LKHEQRVdQbk8ZV5uQ11XVJcKnXvlVckArx2JKidjQq-aTZzL2BpnmqJAOV7jr1XsPH-Xfjf2l9sIYisqmR47CWVDNqEoGx2nXt790Ju5Dyv4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEXsFYJiBma-icMcSCUMwrpPZKfO5OwQU82w6EQp1SRTZgHBZ6h66ODh1IETdiWSOfp6ww5oreTujnMmmCrKt0VoJj8jsCkP9rbHn6ixxn4MkIsXc9A21Up8hClYeH7m97hRRaDhc2lOEMGO5ZfExak20D81yBAJehpWz1AoCmJNAnxJjjfePrDBpiAA8OPJCgY7AVLuKHC4UIKbG5ZKphsAmcuqYRpWbxcDq6-GufwvXZTgPmzEXj1xCvjD2PtJh9jNG6Lv0tjH-FtnI-VhS5A2MZRoXTxK7wpkqkk77Oq1_Y0p9g95LwfHaLVBFu5TiKhAJ5gnF1ws9XjqeMNJ2THU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEXsFYJiBma-icMcSCUMwrpPZKfO5OwQU82w6EQp1SRTZgHBZ6h66ODh1IETdiWSOfp6ww5oreTujnMmmCrKt0VoJj8jsCkP9rbHn6ixxn4MkIsXc9A21Up8hClYeH7m97hRRaDhc2lOEMGO5ZfExak20D81yBAJehpWz1AoCmJNAnxJjjfePrDBpiAA8OPJCgY7AVLuKHC4UIKbG5ZKphsAmcuqYRpWbxcDq6-GufwvXZTgPmzEXj1xCvjD2PtJh9jNG6Lv0tjH-FtnI-VhS5A2MZRoXTxK7wpkqkk77Oq1_Y0p9g95LwfHaLVBFu5TiKhAJ5gnF1ws9XjqeMNJ2THU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDhEDKAtbY_BEOb_TK200ih5QjmOxj6eOIeo5agG3jIZclbMX4C5iHdnlIRJFY06ETFSbvkArhAvq9wRSzAqqJrOxwAB5NotMYbRrGAJskhEBEQW2pVrakzXtgtkPLwwcKZw0pEC1g_ScMSGnMfwg_e1HGoMPaAPiQeLaWK2vYxz-lIDN5w4p2farDDeEXGBQ4YtMlk_LMO0PAdaPmkkNxI7-8AHLdt0c8AIxuXrM-GTOpbshDg3s9e_EBcJl-zb_mkWeV4BBubAXytn_wPg41RAyYRiuBWsXdsiWzEiMY0kC67dgMZhclGUrMs9v4JRY5a0J2KndtGaWbTWT9mOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5toBP14Af-6apVxlM8e9ayrhzvqDamTssz9tvHujmrDYroqcsriIU6QEwXry703p6ikRxJSuyt61QaVDDbu65BzkZ8S2GQmb0vKfiFAZPjEmpDyPh1R9PV23uMwmFQHTLMx4rzJ4E1HOp0jRlqU2wTyXomfpQGbtX_PCMP_M4RfKTc7kHpefwjCikAczBjlyCf-YFxP-B4Krtjrv4itWlnIS6Eyqk14jZ7iJ8LuQzCREuT06kYU7XeVyChkecUxGS9LhJR_yIqULeMRCulQDqRajmnkCv3-bBY8Ti3oajAQeqx_8VntGvL1pCf2fKg6_rvmO6-c2SDOUfcPX2j6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvUJGo370wH97KeZF3iMZUnTKbPiHYJUpY9Qcch7G8_VSKthpdd0GpKhWXygW4691TFTK1i4nJYPgSZ5_Ruc7hAnbAn4d0pgeUcnWaAGh-lKPyeJZO78O3N34X4NKTYnMWoGYzqawLM0OUvJcDFaWVpHXsr-IwxAXuW9-C7jkpQEx28rxiDu6tWlkGj0RBHMQsLdcMArgi8eM9w-cNU6wCz8oFK7H_C_9AuLO6dOOljwaoljoNoIg_ef2DG78Idtg1DGTQdd_7Nz-QJ-92ybnHBraMCeOjA8Nfc40CSuFdlp96GIZ3f_b226Accgt1Brh-6di0MHicLMpYKF54utlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmAzViG3FnmdMxpe1MCW2KcobOHbJ4JnxPCXPXYzcip7Py1syqjDaAUYM0CF_GmIaXlWE52oF44UJQsl42Zq4hcq7Vp-K44xDnvYJ6N-ZrqHDggy1dekfAJ6JgIti7UzElX94UBvPCqCLCRIpIxhXt-uREYOShaBkkL2M7QgUOO9rdanbRRfzMajoqar0onM9N5G0QUaiQm4MRgvctHn0hC9TD90DcD6tgz8QHCJEQY1l-9BdY7SYR_kgvi9-kRLZWy5LfDYVxkua0e6iK6IeKy2hCPBPAdX_gZQC8dZXffxT5wThUHWicULRTQXa390MSnqPuPGdVByL0AQIvVDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APFaPjQmi_TdoTixp8FkKfbY_lz7DxPXWU98Ud2aYmxntE-bh2LCuNzknCwh9xLg9yhZwLq2j2tQcw85FW0--1l-_Q_8ANewKoxH_T0EUD4JRZEOoEOgyRUQdYchPe2cE3vH-Q1uYF7aFhMSeceYOgJHU_5YN9emjAYXrZMXQV-aUETe2TRrfWl5Kj2qm51hzVkxFmTRSNWGCWvGQPUSklhhqSNKlWf_z2NzvcMTZHeTl4vMxKBcN-seUl7lhiFzaxSBnuQAtb8p5O_nn9FTyp7veue5Iitr4-9gzl2K8JEM42ytaP7ydKJxk30pmB18H4IUB-neYMdSl-sovKkmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUf9vEdjjF3oMexsS4pqZtNyaSA_CMQRAnQnzO6NTPj5Xio1bEw6HoLy70YhKyJtVuqh1FwLTTmyYNNz78dkWquHKmupHOScu_Tf1sSMGh18u_RA19HScUzBp9jSIkTkqVDXdSLJmuaGKxaE6Q_Sb-ZOyOlUUAqRouTpT_vnGWgHyhCmcflDfr0upexROs6IHebFC6GgfWT_thLyd9r62whbMuH_r2Az-7e-ADatQFntjDeKSgSrg4UlMm1admiW5G0zeVTuEWhTu2GD5ilcDroYgREddn-OM--qwJFnJ6JN0x9WyZBxPbYg-WdYyblFtLjqUWlBrtx-VAEx_eBQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce6G1U3kk6gObw6EDLOmpBhySy_Rdcm80Mip7YTgfnVSOxWHAxpdmVUE14gO7HiNE6HTC3I7edcDH1NPiHgDJ4ZVzP4fq1VCuqcdVdyvvIGoRat8z3lrWAyWvvMeSgqi8YYgK1nSlYyQoWIi-5MfBMI1_gHku76TWZ2Sbu7oGi5zXo_JSVsYYGPttpS9AfMCjEWRS3HY5KhK4FEHE7d5wlFF1mAaKpOLRqznrVncvDmipRSrDaTxQ9EoMNIW_kiCN37OOKPQR7dn5ClhLhgclL4NqpNTcomm0QTW0A-7MPs6rVBCZEoRVJW7KvfUxur_37RJ2y7tkdS3QcIJPjJnhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuurJ7cNquiYIivn2QoH8oXimQ5BN5xKCPxrIqgYZL1qEyEh-J-9NAPYgupTEJWDYS-Lnmd27PSS-CSDZFo84-xboOd0qj3l1B94RFvL_RIFsfiPsaI-iRNlVJCSd_m2xu40AE1TJHs-tj_zsbjjG0GXsGw4uhyKk-X6Q_w416bopZHZjoC-qR30euniTEE34KfsbRF74F07io4wjQVbXgK-iw7goNjX5toQSRxp9SWROBstUU9MEfVB0PcHIAxxMozD_8xEfcL5Ld-8x8qtI4MbaQ9LYVQfMnwJySrX3b8LKABRA2BwNbqlJ_X_Mi6LGshu_zgxlmItIMKn3bZAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZapYebBNxdnatBNJoMfjOySnnhlj_EHoIl9UH1LHnhoejathrMCx9P7icgujmAZN9WytPiqf93R1IvtaaX4RvzgzL95Ll6L_VSyp8JVgtuxfnflQ3iaoKFPf1IEbKJHeIcDT7qX8EgpFNOxGu5VpolbKbcTSgN8HrNKgmOtnPxcvXEt6vvcacgLc_yRRmvQOpSYs1z1F_umeDXZDKA83OD_9hpuCZTLXFXX0Z47UnSCiOiG0jXyIdaD8J_R05wZmROIxX6A7ODG2mGRaK8HMHE5BA5mg-XTIZoGwJph072wtBBJDt9hqnRO8Lwnj1N52huUb9oJ7VE4h1HFkQrTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gErH5fvbAYRUPl6mlRYwejRUEN3wK3A8rXWAxuiYK-_SfikTM6txof_P9CL1SDh3jYRs1kmbTvqAla-wo8UdRoAVrfwuBeA9USD9EFehP-VZ_BWWclVs-_Rklm2t4Te77Pq01Iw1Eb0X4erGAm6y5OT15Vu7Vhku6I38i3xo4xqw4z0XZPMnApJp9-iX9gbYgDKEGMA-9pCpOQ23XI6HTv8huTXViDOHMs5zXrJtMuzbeuLZz6Kp-ogig0HHrJBCZrETzLkTsErGt4GfD7XCrODQXYLtoUdCcyjuUWDdxpboW_7jLUQgbdk7vM-eKOYGQN_i1Z58qx-YNPQetB_CRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXknrXlgraCT6NEwnmd8vy7TugdgA0oJaWhi1S3U7W11yIoyUxsDakdLxPP4cvHD17hRivTU232I6WSHu4Jdbik5qgp0X1oh8XTcS9vM5dkeKbvzFqNKX8ycuD-vaHFiNWmOW9aiPWidMDWkafBp-3N5IUpXbYzKTnkU_ZW682ogrCXbvCd6MR0QcOiPOSjv8zp2QKCeiIJh--oCVQv0J8wn7ygQpsepszaWT1kp9eqz2ZuNxXVX-RBK8-6KqchFEMv1SeyQt5xeB4-c80ieNa1oyvVCfUXCE9W-smgRwBt_jgbFge6y5_rblRGgUh4RIGrdK0zrDZxdXRolY297mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=W9ihidHE2OdgwXS7riXIUYJiip2DbpdSib5cYU01e3r7eA9nCIEmmuRnI2QEv0CQ-UHfRFkd2GQ3C-8HE-I8V7n3ZMJ_AT5ghSZLVIFrpx0505YdiuFF-pQVY8LOKv01AVVyVSdAnj7JqWmAWS1qm0-TabEhkmLToh6oruQAO2uWclup4HuSJ3x6bELH8F2QkFQkBA-3kefMwajyG2ZV350bUhf9TTA2WuFnQjntSPKTV0muOcyAOxhbN8rChWbeIZk8S0-5X18P10bU2UAUNl3KQuImKqlE659m8RNRsgFDVIVpaJ5e6NSHNROcGdgKQr72AO6DUdNj4RUXtDcObg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=W9ihidHE2OdgwXS7riXIUYJiip2DbpdSib5cYU01e3r7eA9nCIEmmuRnI2QEv0CQ-UHfRFkd2GQ3C-8HE-I8V7n3ZMJ_AT5ghSZLVIFrpx0505YdiuFF-pQVY8LOKv01AVVyVSdAnj7JqWmAWS1qm0-TabEhkmLToh6oruQAO2uWclup4HuSJ3x6bELH8F2QkFQkBA-3kefMwajyG2ZV350bUhf9TTA2WuFnQjntSPKTV0muOcyAOxhbN8rChWbeIZk8S0-5X18P10bU2UAUNl3KQuImKqlE659m8RNRsgFDVIVpaJ5e6NSHNROcGdgKQr72AO6DUdNj4RUXtDcObg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFNaubRfDNIWI48jwfMk-32z0YZllFJubPDHKpaxlVH-APsWuIE_zridwo5Zi_OIxkDj2A2zoNXqTqaUvQ0Ud9LzVESrw_RVpWubDNHKOPuLc5zw_jkkD5Z8bZz9K3r-OH7YApKp6kyhhwYFN0JqN9Rmxm0Igd6uKRjG_jrBj8g9ufjWpuVM2EPfyRzWqGt208gfOnoZV2sKdDMWg-cL_MUpOoUEXT5oBRN7rQy3HdqqRqIMdznJzmLqyY61aEt5aMrliZXZeCSgg-H_YFiQy45m8dSoOkQv_X4dqHwxIT_ep4XVRuMoxHqDw9SmzO6yamzR9EK1DNzKc8UaqrE7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0UfnFQ4-1ukxH2DIyTWSgFDKcCWRaiHKYcURnOYQQcJFkQWR7enRbPuiPYve4g4Mn5ovmcpHXXuDHvkSVD9Fzow9bCNfQpc6aoPnVS0qH4l84NvP3sPCAYa9Z5deGUwCMUMS2T_MyTKQgtbB_IjEhlwVSwBzJPCgv1J1QFKQzHHwahy2U1CHnSbTk-crywu6S_hyo3R4yndxa3CXjFXh33Hnb2BcDFPa732RwgL9bLbceSbLTlX5bjm3C_QoQZJ203wG2LVph7yGudxH86UMwR4TnWbiqjH139RzIVhDdaSgSLIWDP9GP6KdnWnf47WSMPV993UBf3h9dcOi80KDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwpvgFlRsPTBYKbfQApP1PRDgTrexNHx4gPLiYIaCnqVe_YSoRLe1U1vKznZF72fS_faIKdbYRicwPliEKRbTaFF4_uaWQO4Q9CDFjvkJMdli1-aJyPSZro9KgBUd60RKqzgSUAKzQsOM-MXO0-et7u6OiOYXwitUbR1gAEH82IBnkwf3-0uzG5Pj1YwCNYR7hTXfItQJjyHvLz-wrlze2ewRtVt__finBxxDPIhWSLlWgXRLQgAJYHfy_XjXZb72DxNpgs0OnzvzYVLCUveAcnFT69WJasmmYXvqzfaOm4eySj3wuVktUGSRP_0jgg_rNU36I78GSaUUrGLeL0BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6AL84Zhbq_t8XqxxMe-wDZHXTej5EkX5qdctYOYVnEqtEWa7GTecbUZjTcaUz2sRKYqfP_j_cpUbcMUzIh3_a1ZqU4k5Ha3o4TCcPqr8K6S2dbtmsvGZTqlrn_8FMLZE7o_lEHZQ01GeRmXfW7QZbUZ3G36XGFjM8UfuC_o1sOcDA4VUdUSoODeECUzevFU5LrD8qv2eepleE4g1ByXgmp4vF3iADU4wFWVTK0VgOY9V2J2UiSGWeBlHA9ZzAE8l-Ed81p-gAJ6xu7g_nHqpHuQtIIDTQy76Eb63ipvC3XdfQnhstlj2JkVQj5q4wsEDvy0sbLy-kVaRRiTq_boA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=biy087cP6YxkjvCSz-hn83W9LcqFXeZn0KFGJdzgfPwI6t0J_NZyILV-y85bl3-spVlmqlSzFeCAuJ-ZCoFBJKMdqiqsD4SCf6U7ts1tWsOdm_uVCIIdg_0Tf-Ysnl1Tu8nRE9xb_e5xTQoogdMPkZ2xUq9AK7HnAquo5skIEpexvxSXUHQ_w57JxB7cCHUUOYdxJzAH224i6BxCIFSiMMV5gAVCaewNoETquzb822f4Zs2TcqpCp3T7M7sY_JaLXc77TOZMNCxGvcRzLcp0LgAAtoHkHVFACjZbGP3afC6iV1PB9VqKiptmPFRcKCTq0CQzUJIS1BcRF_H38e3lZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=biy087cP6YxkjvCSz-hn83W9LcqFXeZn0KFGJdzgfPwI6t0J_NZyILV-y85bl3-spVlmqlSzFeCAuJ-ZCoFBJKMdqiqsD4SCf6U7ts1tWsOdm_uVCIIdg_0Tf-Ysnl1Tu8nRE9xb_e5xTQoogdMPkZ2xUq9AK7HnAquo5skIEpexvxSXUHQ_w57JxB7cCHUUOYdxJzAH224i6BxCIFSiMMV5gAVCaewNoETquzb822f4Zs2TcqpCp3T7M7sY_JaLXc77TOZMNCxGvcRzLcp0LgAAtoHkHVFACjZbGP3afC6iV1PB9VqKiptmPFRcKCTq0CQzUJIS1BcRF_H38e3lZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIffjfA2PRkWTMQ1sOrkRMBzxQ0e_dXJuqmadUG1GlT8bq-zJ-aPrq41emf_0Lawu7ewU0gqH7ecAEVsoNiyK5Nlstr6cd8-y9YQ3MIGMPO4FVXCQGLjHMCJYK3sLmOpompr0saKu0tjdXo6osq1Lpa-9rJ0NMNDi0_6xTxcUo1ccTd0nHabUjSIBnihU_VI6vrguH5k7AS4Ep9vPtNzSSWeaKEpcXLDmUgEr3mWN-UyF2yUa75MldQR3VE4844PrkbrgI-mi85WSdxpfuZv4HXt0NNNAdS8NalzGmfoHo-QaV6rBhdSDtyZI-6TkFgZ_FQgNL4R_TLpjCpz3ZYCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFTkIZJQaLT_mexs6HiG1oWJopudag8QI11zRBVCyg08RioPPCSsp2pp9R7tCNB9U9xWJdyO2ALRoDuSivKj627sn08poPZfHUtcgLeS_63G70U8MmYiFzAP2D0Sm6e3zuZ1pLqqTXT-CZSUo95NB-WdA_lNX0SAoBOKHaxZvvVrq9A5z4eepEAMzyjgY_mND8I160lvQXUupYTcCGexKiwaLNPt7n8CGTmOeon0ExZun9a2WSA_AITLG6RvjPfKhIZgzQk2CK0cvWcrTK5rCXnd1vqd4bEV8M6ZBTxLXHjQ5FGEjVwI_Dwgn1oBWs1lLnmE8jjBHaeJrf5h2bMCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdIBVa7SKY-xbJUsFANINTX6RsN_sPR_ovMg8OEVAu8ajHJ1yPmOKv7PIDhlt4HziOCDPTiYZzKXeIbaEwTLd812y5J8a3lCI13C1w5jbeVm7dOUCyG6uaiNnoJcdj-qHmT-oxmPjD_Vzqx0SNuyYesWVtnq5Jk4Gi_gZzpS-5hgIfAjP2zEDfooATrfdVSc5fv09ued7BV4sF9brXTRHwJFcL_2FRtVGe1OEIDJGrVbCI4fqzz0HZYfgZULx13o0rZNTAQyiq_r1mAQgLKYEzh_7gsN9am73lE7kSVc7vC3rBNcKwZqmtlkIS9swT3fxINxSHlYD67-oI4jCoRSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=qVBSSxZYzOtZIGXHDED8K2UMk3Kql_hXagEvfIjNQozU9mwCnD6DXsvyhVCnNSPD1JaxHic811Pi4lkzSJdNjfwmC9ojUQ21mR1-ntldXqQJDco_yH81sBNKoTpELUqvmvhRRAfD0N1z5DaQprXoFWZkrn5N_oadsO_X4euPb4QsKTC8jxDnQ3X7QzF6HzNt6rGxYVv-MA3B1XRwGCOugxWWw3YE3-y4ktDNJlZxQpIpPq3nt4v9w5rW7vCHqHMq94opZmfM388s0NXyrJWxr1KM_0R_w3DDPRDR5qmYlIcRgnOpIA2tqfit1edbDVGl0rksuV8iyDjFZCIgTdF5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=qVBSSxZYzOtZIGXHDED8K2UMk3Kql_hXagEvfIjNQozU9mwCnD6DXsvyhVCnNSPD1JaxHic811Pi4lkzSJdNjfwmC9ojUQ21mR1-ntldXqQJDco_yH81sBNKoTpELUqvmvhRRAfD0N1z5DaQprXoFWZkrn5N_oadsO_X4euPb4QsKTC8jxDnQ3X7QzF6HzNt6rGxYVv-MA3B1XRwGCOugxWWw3YE3-y4ktDNJlZxQpIpPq3nt4v9w5rW7vCHqHMq94opZmfM388s0NXyrJWxr1KM_0R_w3DDPRDR5qmYlIcRgnOpIA2tqfit1edbDVGl0rksuV8iyDjFZCIgTdF5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7OMmPFFn_fUV2BbqG-ACMwTmZXYBYIpxoEGUGvS1a_MqWoNkzSkDu_U7SCZ0ErF76dVRkXq103QfwNl8KDrmUXJJt0PHTOcbEsBi77SqmijdGXn_cNdHwVGIOib9ZSIz5MqLkTcU7iM1WBJKJozIbNszPTzlO6ldMU7nkwL3seHMvyRYR0NB-k1Y3T-JJJcw8LSWBVrGg81yIDEwQIyfyxN-9Hfyb7u7ok8mGcT8WBiXLfgJA-rMyFFs1Co9A7mwIAGQCYpxUJIk4WtFM9b1lov4bXpaOEE_B5zt6oACGVTUoHqKFqV-4tNXuu5sA7WAXO3oR_cE0gTY6sABpc6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D33q4o_IxEkvQbXH5vGnk6mlKPKhTshimyC2GHmcF4yYNXZae1msSmB5V0s9vgRBb1RfjEqxWGJDGOPMwQuLT288aHcx6g5aUD7snZKvRmBzixzmgvTJMJrkEL38pcGQ0eqsr2m6UTqskFB3LxeM_2F39jtP4NLtNGfqmoQoxNP8pYRDu9p6coNlCJDx8gDwZS0DXrOPrqUN8NfV43d9phF0-BKQF9o7ookc00HGAhZVd8nIeYztoKXKpvJ5n2nvm8n34-qPXrVMNM3LixjqwNdeEjh0t6xBaRtxBYMOI2z77xULWFjbgVTrxAdtm-7JI98Q9k6BfKR6c42o3AWDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po7jCAeNk_JGYydgeJC_IY0hwmrsWH4UP2KCglJEgHn0HAKG3CfBadbbGkSzgwOMWmSXEUHCP5N0SURQUSB_W7-G2vgxZCCa8PtUahW4EPWCPySWHOgkmogtjURKLSyphRCFmvPcyH4ELknPVyREClqjS2-bkSNwlQI9DQbUzQvUvWD6NzcEGD_gkY_02cvTiDxxxGsxLW44Yz3Xkp0X9ULBpmmjjc7_RtPDkKB0XrbmxKPUVm0oNm3h7zWjIzHen2YfCn2ThvVeq8I3hfJ1IP_wvDuM6ZDV02S3KzK-MuRuGtIsBgYejen62IHzYk8pDnFTMhUEpfRFvKbb_V5bJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6IyRPCce1TsrfatLhT0nMZeLoH877ObdlhgYLft8mHVVPvyzL9oOAjjAViHGPUG4NkKZczXxLGRqbpYdVyhdpqtwZZKbeTwlEEHe8DXD_yBntd-FQ4vqb7NIHbPWr0ZVev16Z5GGalqQ8g_3_Yyz2ArN_9dyphfy2MHnxAj0jX0g-Y29a7p-Zmce5nP2E3BXtI-ev0VbRg5-4uQy2jHbnc18VTwub_I36vSGONLW9H2ywzDUDylpQhYwLqgvmi6TLpX3pcq6rKyopbrmW2eCBO-RfEN932UE1meZNhXSSQ6QUMZfSDFaU-9uWodGG0491FhjtXeT8S__-EQ8DsJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=cQywQvwReeOpkPtYRWcHFBgxp8ce8EQ9iqlOBIMrhsZV47xGlOW0YxryK0NIvCG1nkJGgoc6AQLboLX2FofccWrACVyf1f---KKWXf6eCEqXFS9LDqoddmVwl28zL-NdEBpsHKehD9GtsDr-vmuDmNVOHm6u3PzW2eYEWoJJuJplZeuYbcRVMAAj0yvoQNbPtaQy3Mzcui4PTRfh6iulcUHb1d8GNWLbsP1luOCWUG416EvEOyvFI3Cc5SP1scwI6SvsU1hNJszzeJgmYKbzXNKWXXyFsX0dYEgpQzxkYWtMYwffCUSvg7qW0OxpZgVgqbkvSiGRir64G8NZHDyX6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=cQywQvwReeOpkPtYRWcHFBgxp8ce8EQ9iqlOBIMrhsZV47xGlOW0YxryK0NIvCG1nkJGgoc6AQLboLX2FofccWrACVyf1f---KKWXf6eCEqXFS9LDqoddmVwl28zL-NdEBpsHKehD9GtsDr-vmuDmNVOHm6u3PzW2eYEWoJJuJplZeuYbcRVMAAj0yvoQNbPtaQy3Mzcui4PTRfh6iulcUHb1d8GNWLbsP1luOCWUG416EvEOyvFI3Cc5SP1scwI6SvsU1hNJszzeJgmYKbzXNKWXXyFsX0dYEgpQzxkYWtMYwffCUSvg7qW0OxpZgVgqbkvSiGRir64G8NZHDyX6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOA5lh5D_QyWyFY5CqfAKpKZubl6XGm8w1_2hWeHQIvMSy3srFgO-2qnyE3Wk5ZY9WLdzGA37z7NWp6rI6Vd00sqsHlkFk_mK6_1ZH1skTCYCeRDOQ8uL3YyQ_wYspf1Okht9AwNE_5-wRRRISbmWtrMeSoHwHK41V9Pz672PhUSu2rM9PyB4w-mTSUOzf447XepPZpozqvYsUkHE_DyiRMLZnyF92u-VlTOHKYA9-f40zHzRczkqaYXif1cCIMGZZPSWn4Q72CVuETLVHaktBTOYwLM88_AulErXFchQmZsB89lUdp8DGO12Wgf0iDX0FbHe2i0oDqUEtVIZbyJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=fhpAxTMxXKM6vLs_cmaf43CrJw4TOPba-NMQKjdoYsaa41qkJPxFagPWGFTKSGL_9Onfwk3Qe1lhAR26N28DfstRQLo16OvptWl3eNFXaRuY0fqVLgzKsywvJ_2j8u8jEcyS-Du7M6Gj0qQaCAVwKbKyQ-3XulQVza_FroWQ3KoIeku7S06wKx4Edv2R_KpgxOgMR62uttaCrDJM79qiGSmtGxJQXd5MQDFqRpLKa0wjXK-FtZWYTZ5fi7ZfiYkI_rZH5IYijMHs38PvXwvtn-2DHz_rPy7oE2PpgfDLRkFctawOqaq2QNOe9t_UJpxtP8gICJGcSavKvdL0pgM5xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=fhpAxTMxXKM6vLs_cmaf43CrJw4TOPba-NMQKjdoYsaa41qkJPxFagPWGFTKSGL_9Onfwk3Qe1lhAR26N28DfstRQLo16OvptWl3eNFXaRuY0fqVLgzKsywvJ_2j8u8jEcyS-Du7M6Gj0qQaCAVwKbKyQ-3XulQVza_FroWQ3KoIeku7S06wKx4Edv2R_KpgxOgMR62uttaCrDJM79qiGSmtGxJQXd5MQDFqRpLKa0wjXK-FtZWYTZ5fi7ZfiYkI_rZH5IYijMHs38PvXwvtn-2DHz_rPy7oE2PpgfDLRkFctawOqaq2QNOe9t_UJpxtP8gICJGcSavKvdL0pgM5xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epP0FHeuEE_qqUTqjGb0YbolwI3hA56_0SovPFcNc-Dw-64BxlMBMOvoZ-N30J8s23r1TbXdF2gfp3B4OJ94wYc2JdBNNgGIozjB3BVABoq3viRsxLLgcCifLGTmrQDru7z-iLehs3-usBTeWkJPsep1F9_5kPKmjoFd2W-cS1H8zfv_vHp_FpHwP6v0yeEVy01voTagquHL4MjysXQJ_8HabaTs3qKpQnpQIbAfVl3w__y3jiwQXiuyApshRQsf4nybRvV7WHO81k-c9Lj0Ya_dxmVvz7kkQ5l9Px7DmdMrfUd7AGchC63bf5hZDzLQR8TD7lSWQaupMtU4Hrb7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBsdj-vMcEUctJ83eLgE7rlHDYcUtM_zMk9lMe8z6sIN8eWXaLwUyePQxkckpNlGUWGq_YeBhDNkuAtlfpIaIv-EEdlcGS5nSaaWOZBPjTaSmHZLlrx3v5b-fDUaeToObNWxyqSWSWhh-s2bBpg2eeVtCt4TIlDOO-oK11vBT-eix-SZKln40tgy-2T-dmupRwUMxAqN_0Vxzs94EYIhO0fp5IWFEoqdfyvLFvqVEKfSswNwa5IE5f1V7EW0ijood72b4aI_bDoXGG4GIxbTrcn2M83JTvfP6NBCrHhQ7BH1ELaGFRgoHok4yCioaGitaWIcHSTU2HhGr8nqZx6k9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qntdM_SAtOhfH2c9dO594pVTJrbVvzZ4ao6cZWZeTmCYMRrdFYBy2p7lUhjGhwxe4W2bMQecvmGRM3slp66f6Fg0OfHvAzFVmrwTeIM2pz_f3rb2d2qZuXC9TJX0BVp2FaKTRNikP1dNsqJQco2eYIcVf96gkcgL9vhSHGha_zPrSalnrm2zuTjOOW9lQtYyjm62tHVpl_ReOkbk5-i0UhOR9N4vrHAOIUEDx5qoEl0yIhWFjxWvQ2bwJ74GBy3yeijJiA_kzvTyNhMLxwd6921uuDVMzRqQu17XNYh_wRSZKZBPfC8oN9Hsd8ux3-C-YqUoN5y5LTrEMF0tZtX_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttc8Rrqu1nD7N9i6YiTpfblTewP55PMmhyrpkHh632sijeTG5_6VRZcZ045jJSSFm7c8yeEGkdT2NYBJmhxnr0b2mWiv9EYocdm9Y9nnJJzDo3UZNnadPy63WeS9hz3WNCoM27UWGuMLrRxLal9fjREnkgalqGy9RzPYvahiTlWyM9BQ-MpeL94F9P_l2TEj8dqB2o2CBV3_lIyWapy5ziEqJHYYbgGtqwH-2GE2Jvfd87uD9YmpBuS8lUsj7Jx8L35jAuGPtfMWnLSZV2p_eX50bdwpcpVZNrlTfNU-oEFGcWPSB4mw57LqAK5RdAFOEelyKyOVQhtyBgoqjl7w4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR3gX7rYFjNwnIvSNHsf46EOJ4soBzjvMuuSIqpCQ5E7henle5k7d4UpBN6FhOF9qMTo2GmVOFvboHbUVRvl-P7bDE9799qLz1ZYiDmxyFTMqm0ZoxKqOFAjgP_rJFLJK4-57EqHLaTB_EimKoYEhBoufa2lYoGPiOiLEGk1WFyIEmCmMGeEez-xkJ-b26V54T-Cs4vofecfJyhZVZYfMMOJnKUmpUPbVvfAvwc25kIGx_s2cXwkvE5PrmPvjinOldr3AIKqnVZ-j3wncgPkpOSn1POG19mqbbYYvLwpyrS-7xHeWS1wexAlOmqLULEtKa3NbMw8jSV21MVZhRbyuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=E6I6d7p489JFvfiAvrQNeGAwRGNgq7x-tYZiY66RwMG_vU7zKgGiM4TVKz00ZjAI-OnWd7FZSpT3iOLOR0q43Ub-1P_uOs79Ll2A2hEpJtzDU89t6Qgi0LAteSyaGqiQX9_aOFeC2sGYo5xSXdeAtGO3p_iW3ZDQ-CViwZfZKdvJ_zTDE_LPuYHl7jgRQWRuT98zaP3W9_6Y7zqgv6w30Vm6D6MxbpDA8ANPp4bTiDgwb7Y-FMIZDVmMri_MCFx-n1taHVaqX_Qy0MbjXCxju1KJnjrCktNYm4C_8awpjWx2feuRsxtV1qkbkY41XargjXSWr1VOkC0LmqfwkTPgSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=E6I6d7p489JFvfiAvrQNeGAwRGNgq7x-tYZiY66RwMG_vU7zKgGiM4TVKz00ZjAI-OnWd7FZSpT3iOLOR0q43Ub-1P_uOs79Ll2A2hEpJtzDU89t6Qgi0LAteSyaGqiQX9_aOFeC2sGYo5xSXdeAtGO3p_iW3ZDQ-CViwZfZKdvJ_zTDE_LPuYHl7jgRQWRuT98zaP3W9_6Y7zqgv6w30Vm6D6MxbpDA8ANPp4bTiDgwb7Y-FMIZDVmMri_MCFx-n1taHVaqX_Qy0MbjXCxju1KJnjrCktNYm4C_8awpjWx2feuRsxtV1qkbkY41XargjXSWr1VOkC0LmqfwkTPgSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng0_qQAyjpSdh-sZY8XBsy0e6EL17i9Yzi_IzAoZJZd4kB87Vrzv9CkYQJ4E9mENPqnNZJFXDC0bCP431VAyp2gdP_YM7sQISqljfHlnc10_J1R_5cn2byw60hHmnWSY7GItFQgKNQUVe3bGb_e28vrsP97syW-TTNijd2_Sb0WVFUEm-3aNq800ykcxXw4A04DeEKeIMZB2DdmbAhyXhXLy-Ous1YmkvtoC8N9mjSA7bf-oC9HDx8Or5rr9-WLckibgJxrWPRWOaeYilUs4epTTfJMrLiAbmwdLkS-pwIKG6TK_s3LpXpUCXEgIlCB5GSlmFy9X36IhRouhVs2w1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRDahCaR7On32HPeUjsJ8AG4bi_E3Ctsc4-dR66J9rc-9JnrUXU7-fB4pG1lLniqdPraHDIE_G25FUvk4yqjM517XPbFaxsWs1yA7fEHK7Zbp7qFqV4MdZ8sFxOzbxUza1vPvEyLHDGPod2pbbipOuPvht151qwois995zwDQ70avQ0Gs-sODGAXJHlO5TkVebQrF3UfjFx65Ny_XVbSt_RzjxteJPIiKu2knI6o-WjKU1NM0iWjP4_4_cb0wsk429i0TjgRJwLIucm-SjZbURW2l9ngqWmpqdeUqcsx20nHlueCatSxV6KsgriLsRc3aeTAl1RdhFr8-hdS5-ESCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=F_0rqlD00jZg6hJYdgpTJzlxZWcSSl15cgiLptBMG4gk0YDUMhzVhZvLffNl5tSLh5EXTdDR8k-lEIxUx4C1uUevq_3bibsPihLRIK1D96Gd4QY9jJNy73lW2glG5JqvbqX96lyRB5k3V4fic3czayiimJOM1r9iait1Swvg3WSr8G0VZd2Ziqoz-uKKzUQ2OvW9AVRDu1dfhlDs81bkOkbwdNNFYBE4n7NJA2ogBnfB3KrbYt0xTuz06p-_9oPTfInBpb0tDq9CEaSRrUydsL-iKJEmMF_miwLev646UejHUAHaiPiI3dCzynoyXfAnim5FEMFnrCwzCR-aL6WOeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=F_0rqlD00jZg6hJYdgpTJzlxZWcSSl15cgiLptBMG4gk0YDUMhzVhZvLffNl5tSLh5EXTdDR8k-lEIxUx4C1uUevq_3bibsPihLRIK1D96Gd4QY9jJNy73lW2glG5JqvbqX96lyRB5k3V4fic3czayiimJOM1r9iait1Swvg3WSr8G0VZd2Ziqoz-uKKzUQ2OvW9AVRDu1dfhlDs81bkOkbwdNNFYBE4n7NJA2ogBnfB3KrbYt0xTuz06p-_9oPTfInBpb0tDq9CEaSRrUydsL-iKJEmMF_miwLev646UejHUAHaiPiI3dCzynoyXfAnim5FEMFnrCwzCR-aL6WOeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gyqcq1JGjHDBCSxFV_G_7eGSIz51gsElQmCpfgrDL1aeiLQWycXAZxIWhzNaLiEZ-mUEPF4UAnZemk2_KxrStJotA7FsOzTysCinPsc1mKRRU8d0mt3HUSWc7iDdxyS3ASZQr3fQFq9kCl8mCUNM1r5Hi6LPvx9zcTMs0ZSihhhGYtYMCmYoNUas5Gfe6Ft9bAsgvdp8wEtzl4ER7kxIf3bwEWCS6FXuQ1ZNrPi1w_uoBZblXGvT5fIr7P-IOoF-L-5Gtl-yie_9tdQIHoVGaZd7i12T6msmxATk7doCGAYY1SCkkh827iiTeWTKSrOEJzFCdFJwJ8FWwA_Y4gW0SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usrM0jU__g6ndx2MuRZd_VaRmjDeCkdO10Gf0SrL9o-GycMnxPgnHAB46_bjvgeYklY_umPQgFBiqiaRLXJzJko_e9j7Vaf-teFyuUp6zhLg0GTBvZVuFUqXwSWfluhgZfF8l8eHPHxADDfLBHs1wNcxss4bFfYTLWPs6qKCJMIsosWvngPzj1flRSNzqJ-__LY-6HyR9E2JS6nUeN2z1WMWt-eMu0wTOhnIPQwF9yRgyq-40vouSSVI2lpgWgOmtbSxSr4Sp7MdhkI9m_cuBc2AoF7AO07Bs2KKapDVcWVyyRp72kTfoBnU61P3_Ehc8rY4oyvhOkw61hb5fWK_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drw7aKlQkV0b1QRjm3erQm4XdNjDI0c2qW246M7xI9Li13u_2RaPoqR_cM8NfL1ILI-g83LeO84alBZGwWrcueZOuhOKDFmeK5yZpZilVYIXFyGNjH32y7jXHnxHZkhLSKh__co5C2O46Bs2yskxHHqQRN8OcFRyq8D_BIM_x3N-zXQIuKhn3zeEMU1GOOv-4hVYwvOYpqIilt-eACYCNKH064EUrxQmfv49zBSgsDWgB4UhIuJkgKlNZYdAgzP46eAkAw_3LzJ0ggXt5GvG7kSJSywCpUTZTIzGi8wdJkbqObuOvTaICmZDh1UL3TGm7QAIG5Zk6uy9uUj5R5K1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJBwole9mC9cYDKnqK7nGCbEUgI6ZObjZ1wmD1JRfEgyAJlnGT0iwkil18D0Z6eidmV0SDaJF5_V62YQ0bkurI3K15TR_HnppqHocNkNGK0KV6G-0Rjm5O9L0phrHb8jezrJi0fDjlZfTDup45hWzorI_bopQFLWwd9crM9EY8k8sR747yRa-MUw-MwT0nZPwSOR86JtoolT_YE3j3ZNVLhQaVhXRfMLxkdyK1eWpImrQHFQ8_iyQgdiImj7fRAqRpG-DD9X0QU-kzclL8_TCxW-ONcSfiYwH6i8UFxSvKVU20-raBtxGikKb5CujFB9QMGdnghpVhbopDzE9FnPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YundGz_CsW7YVVS45LB3ckgHu_FVfppfP7Dhi4XiZr05XeQQEdXt9Hlddg6ral4DClwgwSNNGVCdVAmDQYqUgE9WlpVz8VKK68RDhfsj-jj9lHjA8YfvR3ojXS7s4PT0DoeHvROGLtHoGaQwFBG0G1jGBTsMcWe1g8FroW5E6JnoK9b9jSrUNxe71XdROCtG1pKdy1oOPNVvmiuij3Nl65VcrTH2buWzTCBIAp7Kn7tMhOZ0peb0dxNBaWwDTj6Xacr-yuPj34MV8FszeZujkgd4v1IMHkTz6C8e-yjC9J0QbjTJiZHgsxtdw91enxW3OgZuhoR07_NaRuWRN6SSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDxh-twiwUw9ZfOqzuqZuJ1G3Kxi1MCOFVSElRxaqPB9AynmAv_kOjolO51sx6IFG2XmKUxnm2lE4dWNPZfEZCKbJM3CNQlW4LqE36x9jnAINtN2zc5TEDBV39XEn70HDdtRr588-ZpRK_9G6dTwkMyQYXRTR_ygaRZ22hnsJdcndJruZRAnY5zCQuenPptstvSTwH3yq_qHkslhvJP5lfeZ4TissXbhPLt0INnN77sEQb9xV1VQBX0aCDl0Pxm3f0ihRJqQLkl-nzKw-FUE7Cyj1WOe8ORwpqKZf_EOk4vy6Ej5g_fXoaSSWmlaxxslVJV015cYg6R4M82gPwPiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyDXExvJI6ItBfdSP_iYXsdrfG4mTKPNR_LEOcTVikkMmqZpZ-LR88Re3m741KvlopqizIBm14fPtfiyovtwegLENgPi2-FDzOi2XKdEe2WfmRXjRXwLbXX5v3Dt4oXdxg8VX7zlKIF4s5bmkILVTT3JwuHJWUlXQFg6E0VFBF2kKNwG5kdvK9915L1BJZ5tYXkm3VEbjmeII14euH4VX4TVTHDSYNbyEMTiQ92XyGdYEEYEqYPLOlGMPF6VapLgUNMKVHGQz2ew2tHs6MsY7L1ojc7riqh5Tg8OWq60CLyu1FsIMHOzO3xZjp3DYQ-Zvpmb4hX4xXWQohEgYktpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVcuxB8Ec-9s__aTtf4MWEao7QhESxh6FQb4ra4lWlyEx-p8zG8KC4r1UBmq8JVhZGH45XKijmR47Ysycw4ih45GFaY6iIKgECpmlvJ7oY9snXDeAzb50Fif8oNInMuJzcYazPIz0PNErfU-Ls4T-dlJgwvx9PZ-a6ASoh1jgB0yPgkrtEVROpdeSGm8z3-V28Pg3tbu2r96R1zyTQVwp_2No8az3dq3AV00GF_SrBBPiAnvlCmJze4qIiaWnBoo6LOUmGg8-BP5-6Na4CHKQbTGjPDPu4ZUlY5bfHfJdcutFv71OdlxEXtvrMj5NNcSNct8goZgr3s1SBMl63S5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZMx5VxiwuNeFI1TS59UmiJXjeDEr0382xV5f0J3AB6YR2OSddOqsa2-HzVvGnMxWXDVZkweTa_kX_6OeAVFZPoxH4KyycmOSgzvf5RUaIM_xM-6sa-QipkRp0O3YBtumBiusvMzwUI0SeBDhJ7ATf4aMyISZFj7eap2s9t08-W1sNL5X79WWL5ZAHKDxgcNW-mebucR7YEaDtp7jHVPmRFrzyakpwz7_9n4N-80QOZJewGdRzBLHkPBM_n0JsRTkEuTpofm1CFd1XtCc6WJThgsmFpidNSwXEFcoi7kzN_Qbi1_MpY1dlCbDmLdxxV8-zmUwLzEB3ADnpk-IKoC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azm7iMH0kyITxer9NVrXC9kD2DU7TM6rcyiC5FamEAxxIIprwb3le91fe1oYt289w7E5qXPXv7gTqB7xUVY6MRkMy3PwA44v_YynbzcTCqh9r2VZP1UElK_6ATlXamTSadGUos75hKAx1u4cESN9xHjleDwU8X5sNLYRVopdnChuh52XjaaakvXsBId8w1yiQ703Xq2X8MOVQPBGGbj0ZjSNYRXejFIMSGybeaLP-R7iyLfZog9hUXtZSSAUJdHu_6y0GKmp6eiEB7cdyZ-fIj2LpDX2XgM5TNE2rj1ftk8GP3ioIMxZJuA4ZKFWKzis4qWXm6CUXsKPWS-JzKaRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=XMHaBu6IFYVp4mTkv8avzYx4yFDJsJvN5Khc6N76aLQPah6-Pnucfz9WxPH29tZiJOiEEKBvxOQcVSjQBZNJsiako-Dc8VWjWWqolsEzWvQat6iXiLP-Dm0G7rUdD5mojO0bo45sKVN42l8Mlu3KD4mb-CZcyzyqW53rsdax48pFqk4jjjv8IqWOwaDICS8-sxEonhrCaBt4AbGPxxaeTQQvwZ5cmbsLGL-VMrFBZotiSK1IoHDD-lcO9FXJARerrTWsvQrm1BSM8Tfr6569F8zTzOHeXgQDGzB965QFq7obOtbovBMMfJXSDBZ_fqE-xuB9l_N4o5WeGckKoxOtvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=XMHaBu6IFYVp4mTkv8avzYx4yFDJsJvN5Khc6N76aLQPah6-Pnucfz9WxPH29tZiJOiEEKBvxOQcVSjQBZNJsiako-Dc8VWjWWqolsEzWvQat6iXiLP-Dm0G7rUdD5mojO0bo45sKVN42l8Mlu3KD4mb-CZcyzyqW53rsdax48pFqk4jjjv8IqWOwaDICS8-sxEonhrCaBt4AbGPxxaeTQQvwZ5cmbsLGL-VMrFBZotiSK1IoHDD-lcO9FXJARerrTWsvQrm1BSM8Tfr6569F8zTzOHeXgQDGzB965QFq7obOtbovBMMfJXSDBZ_fqE-xuB9l_N4o5WeGckKoxOtvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIZNdcLSFB1UCqwoQHl3cJ1s0PCXULnkarZVM0HnaU7bN2cLauSOOP-FKFZ4AfeceM5ZlH0mKvnm1Pz0REVtOfU9L8mZ0vCPElvHQVjClSIr9fYgiomdyYpIhmZkMOIqDnN2AFRUpoSik557BNJ9NPeDEePfOYL4l5Ge936HBe7VJf3jp4Fpk6aZeSrxrqR-Dv6K53Z2cdy6uS00iNCIlKt1TmBDoUxW5bq7_0TrS-kgtd0dyaij-uyeXCTo4T_X07Qt2FtpvcbP5JrA7cHbdTxiq8Q0CjOT08Y4mATleHccBj4aODhuWksQF5BeSRApNvJ39xHWoNkgKK_a3vYx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUu9AL-PoXVQJWgJeLv7ctr8gp97bjHwLGdjG4CnNGFFv3GQYnnBwGbBCcAp0U49vyrs6ActWb2U6WYImK5Hn3gbG8eGGWu0wf8btJfJ7HyhdyGtz-_jf08Qs4eBqhWrPdl2KzGCFG9Jdi7hrhHbvATEh5Azm4b4_YwXED3Cbb8ymWDd9nSUz9ZBZNPyzEa1VCfmlHcgEVGVuJGAS5XJjKrcQi9MrtQYQcxmuEHTu7wgauWmY6p4G5D_i2D7KIPDAlkf87kCDfUilUs5JQucOdJCwtrdpH-03iQdiXXEXQvFw_PgbFRsyPKFcbVKOi3UzsGcUKJ8YLpbSaYTDA8h8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGqZiQfqLd8W4SQJRED1sCZO4wAt3QTc8xI3FzeVaqplopFVJU0XsRZd5EX2Ycytm1Nvu9JxOOvDjZTWQ0Pc4wsyO5tN36I7tBfmzRkgxOxUrXz8vDOZDm-aWo5jXtr3sjeSkpk9j262mIg8I-c3tuqjbPy6uSTuU5Fpd3vG62QD93qpUFB1E3JjEEkOjRfapeC-U3oXT4BYw2dhusHn4dGycUsj4B1AM4SfBdVMAWKE8jXCAHLJ6JyjhgzKElld9mjOeVL37pP5Jm6Wuwm5x2LtkP7PgTkmCj6-fYxYs1eZeWGldLxeHKmr5eFWKiGmfyfwWl3HWnE_2IiHPrwXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVrCM-7X1Qq9QUxYQ2AzOYoVzoegHDjwnmFQkuMm_idkzhXu9yr466P_WQ9Pr9XCGsAqg8R0cxJIakxZJCIw9UDW6enSfCQZ3n7CtkiGVwI450yAboZkLIiuw95Csf5gP2N-S7ptb8oaBNB-boI5uEbhyLf31YRzemK05ZGTXFfRSEUSUPZ3SlZaK_uHdtiVjlIj7vbFK-t-YJB7ReaUW0Ivc0DYm5BTdlvsL1njxrNwCKlL5hKO-Hl64QvgrBrQNwPKJCmXjDFKGYBa8zASbbrHMEKtcsM-L65wliG2ZI3veSXshn-VIw5YhQrv3iz7C6kIVwzgtLKIAZ_6f4RI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVdk7L-65dNskF55nT1wJuU0K3kJUqWEjRvuTQqy6sfa83tXG__QEJE0XveYwG5Gc-wIPHVdXV3xuQA3P5RO8x9ic3mynHNNJPopRlPod8EvojliO9Sk4q4f4kIMXWI0UiYfrrgh2I0326usa9H-ub6pl58Ks66OMuscRSCzlSJ4Aohv3sV462KunXz4i8mzA8I8rMIb_Qps0zmCd2tJdaq5AYjbyTrHOGNnKwSe09COEpydQGXbu9CBJtWtSlrT2ZsYtxT6VbqBIgQ_jjHoUJqhxaRrgGv-EWwOLn8SX7gVLX7eqLFTBrB69Rp-wM0X8UaSIuO9hGVqwB1aW54m1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcmHWSqeqnyGp7VTWTLGJ-sxbTfDouCADrbkYO_lKYymo_ItOzQpAOMxBfvei4_jYRkJB7Jw1Q4f9EgKkVUKla5IWhZOSWA75CeULhIqqKNvglDfImoTlPGWL3niLmowf0rEkTwts4gFtSGldvVYAWMfia0KVMbJ5BtywFesnMZ9A-5gQtJk9oJm7zK_p8swCsBNENR2E3S8JY6stvNjeWj6rvINsPemBs-28bjDW66tWPG8i11duNHT0OoUscNelC-_NFYukg6al9FlS_OtLQdlvomyiSDt6jSXxEuuZZLlJ9gqdDw1ACDPmUewAcAKJ9RLcOLK735tWsL31AKqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
