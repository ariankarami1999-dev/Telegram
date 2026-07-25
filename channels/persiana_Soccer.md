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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 582K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 22:24:25</div>
<hr>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmOaMaI_EGthyf3RM6rUWLPtBAjlt9_F-XHgiQTpJyAlB1Vg84iASYe1PCM9Ed3PGlUmhdbT3igYKInPvlH7HB5nt74lri1oLA12AkLFzB46eZgBQMqy_l0-4TnL0mGuUYbndmeg5_J1o9L9bZkwWpcxfIY8zWrsFNzC5zK3XtUNqKqrw-Fk0HbseHLpD3yvfGp7nBfUhP_iEFHDpJ32kIL5pvRpk6mDOKiX5r7EbeCuh66az43xcceG35fX3jlmqP1O3Hx2EqSIC7fjMvb_mzZKXdBD_4sUBLyBW8O8ul72ec1Z3CBiqa_DARD6a2MxqhCcx_-l4nTAzaoD_ZzOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzcQ81wEUv7e7gRyrlQI7TlrVG9AnOsCNg9pXDNMhiMiB0bjO3Co5Y_kQcHRamaBBBNtwuRJaOTRuTA2esyfkC9XHA4lY_p2VqOqtJycnpe04MCNFkz2_fF2GrP23Y6T1Vd6e-re93OSI4-8KlB3LPa7bjTeM3at3RaznP4CzpfxDlfKgj2jX36_SYFosDnjE5Qb3OqHjwWAo3vuvRG0wefWznRXOW2002W3Kha_n1uoNiLMFWTiSzxOhK_2LZQnClLnFT6LBeG2FBg2gfReknKOsPrG3ybV5Fk_tKbu0c01kR_Ip-BU4RjYXboBm5fBNIgZjJCVlkcU0s6pEQyJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxlcz4Z8xIwXJ2DDb0swBEdKhiOTahe6Scnhrav3LhKSZlt4YxRSWxG-WXexfY7xC-94aCGTotTcIugLf_-Lj8XFOsp0JoPI47Z7u6WUosvlq5ROWl0nwAd0CRgBRglWAWspYhzycuSKK49l2HYo9nCH_iutEJ14paMu4lf9jWGqhucBrz-co4kO1Hf4NKWKSIRxFkuKZjXdiBP-gMyLLLFMtEG30p0x11-RjLpSE2q2EPOsZqFS6-FpJULYdcem1IaaDO4hiQvMo9nfYKcP_ic12M0a0BuYjohlcpi6r6WyG9jCzuXoOHG4UMkP-chm6SNtqoxEMa1ZpOYoCW5poQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EukDkGr7tbfK1-VCL6vxYOGJOoeJBEGHsJVRiDkLW5bklVblWkH8owbtXQ6cp0_ccxmbBET78bxJhYi40JJysi_r4cJWSwsis86xNS7T2S8BwbQktAKf3d-deZav-FA6WARjAWSLNuex99RXHNnpuCfMPdyxZrkrFP9ExT-WjXmQL5N-YjEzayDJQcghDfUo5xEF4hg5jNgp5moNUkzzGtRP3GGxDHWgFEDogjYhk_8Ybb4KXWSQOK7kBj3DPUhF7lfrA25bho0pyk0SI3w6PsKu0OZO2TDrgD9ebkRxu35zphQfQjt3e_zmCfxlVnh0hQ3HwLJ5kdnbZmgrwTj9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFwcKwFGTQCp2LSjhQt0D3JWW5pWEvyCUjhKSIuOltZ3mIiSH1Ftx-o8rdrXX2Y4DMQo92JHpEwsWsDEdUiAuIS3nPwHXGw5hpx6VugBJ7ERMZnEnJI84uqXH5aLaOOgaEfTZ0e0YNTfWxcr9s4ZZ9TbbhTkWVj0LGgfd9Hdp_NDrkGnUBF2A4QDpyT8b3r2hs3bqoMoPPAfglSNx3z8ijiz1eMT3GXGiGplRURPfRMe-dQTDhlw0NoHxoV8SGDpPYwfUW6HWwyCHC1EiN96O_q5UhNqKMzYRxNIFEyAvksNfCFniYSO3PukojGf9OKpwhoNJMru168dg8OhWprP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-T_0vNK86TO3_2rLIVELHIeYzvtK-EY4ZLSOrKAehD6nxbgsZIXR8SoLMNZnpLS1PIKei1H1whbYje61PTCZr47jQANcsBhhrqV49OpeEUiQE42wH9hZ3T6yKi3m_p4J44exeIImRw5FiThr34Inq45E996bToZOYGfo6r2q6hyZ-CLc_O0QSmFUrO1DAyx6MPSwD_CL8zUAJ2__TosS0y6xWEo94WMV3LCtK3EjdUtmVyUHG9zAosM6vunzNPMD92zzTdGPaiq621SgTScK6GACJJFoeEV0QfD6kxPv93Y29phXx87dbzaj_nhvBEFnb4nkACtziJC5d5zyFcc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc_QEPZ_nx1o7Hf008jIpkPjscTlixOqrCFWVVVtNXhDdE27RtRucj7NX89Wtjx0s7iGj37o18hpWTCffSqpyHyrro0-jlTJO90ow85sHQxvlQM7Lm-h7gx_TvG4Sc8NDIkDqqaM5yuTpXj5D-b0HYxkL4T0fiyRvW4rmAo-cb3WwrsLnnTQr-35E1ofzyRFJ5oSRAB_CZ_PO0An2_8PnGIeO3e5pJHh-4PvnhXonVJnSwQf_9XS-Ao1cJnEwN6mMNHUFJQGnElnMVv3f9ewZ0J4DaRHOEYm9Do2r0gkfc0cEbOQINYyfEJdQ73eqZADXqbBwwqO2VsA37LcyczabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0zQaFziDrxD_YNg6l8Hg4cb7-vXMvH2OW0CRhm6k9zHmjm3VHbRQKeF6GSrWBT6PpcLydfMDEOz17A7ynF8juo80DHb7RUTE65oyaBDJbuYqmbFNK1ctSqORDTXUnwfeoqcEGIgrOK8a3r0dFWJztdE4Tt705P25nCfDPSs9bP3yufAnAfsKOgS5vuTAJhQhGvT7G0KmjTSU1Zn48-fzHmoxovETbPCuv1u4XZGVQexJPNzCBrbw0a9U-qXW3OlmEL7hRETdgWFnPj8LdOWnjqzgQlF6VTdBJ3VHE9lv6YtPHhLiCg_XZ2-1VnciWZlszPZ8rDdw8XrI2SI5tLbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAeVOC9i_zHrjFowWhnMy4CtJWOI_HEahnqzACMoRJOlobryrWpQY1UPdiEWUMYT4RnuD8HJZ5Wm_5ibt9EhXTZJ7gRZgU3H-sP5T_NIrloky5LB-N_qgBWjm78vOwJWd8KPqiGDAzqHfzZzOyTIyVe_bIpacX-ezI-6SbfhfYF0gRRCr3h73eYYMQxuS7KdIbn_64p-Qlgwm8A-kqcGwNKJXbkWKqjowmMsoJRDq7VE2LgdIsY008Jzy-QM75NE8Ya4vTBja1VvUZhluIIYMiPdANw050eD6Q05X-Z5lE6k2nGuF2AdP4fOXjKiXb2mCO1CzAO3Kjy1ob0ZTRRnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=o-Re4m_9W39m_LncqgU9TdQwVXy5sILYvpYb90dlWZZbsUkgWAxplhb0WD-D0HnRwqUm3EDAt1GSN2A_TNEq5dZkCGRz16HXeOR2rwLlIpYVk_aLUzwUDDbZGcNhj8UhP6G_b4yuK1i-0GYNWA9PjjsZUVb-rd_-fLE0QuNMGrwAug2Lh-5VTbByeKe0WU5y39tcMpE55TYICQUVFCyv6SjxStRSlzzIgM-2HBHFmx8ij5nWrlx0dXMtJmMiERAeSWHGlHSEcRFuOYMD2buoHrTkQrob4_UcSifUYd24ud1lrJ0FxhcEaiNwM_j42oABz_7UVUpu7EKDi_Ugp0qWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=o-Re4m_9W39m_LncqgU9TdQwVXy5sILYvpYb90dlWZZbsUkgWAxplhb0WD-D0HnRwqUm3EDAt1GSN2A_TNEq5dZkCGRz16HXeOR2rwLlIpYVk_aLUzwUDDbZGcNhj8UhP6G_b4yuK1i-0GYNWA9PjjsZUVb-rd_-fLE0QuNMGrwAug2Lh-5VTbByeKe0WU5y39tcMpE55TYICQUVFCyv6SjxStRSlzzIgM-2HBHFmx8ij5nWrlx0dXMtJmMiERAeSWHGlHSEcRFuOYMD2buoHrTkQrob4_UcSifUYd24ud1lrJ0FxhcEaiNwM_j42oABz_7UVUpu7EKDi_Ugp0qWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SulGdjBtJZGT-dbk2TpKEfARxiY5n_5edD5baP_0KdXpPpkrPy0C7xTyGlbSCB1OfqUjZbedeNXHS6w1LwZe9kWzzII5skV4q4gYukPGjCn6YjsYMP1qC_-n3Zmo6J2Ow6LEVIbNv2BFi__jANBU2LPzNWBD6_SSl1dkpUOLe2PWueXoRwT33Kv2Asgdf8e80e3dpE29MEZJ5b5WecjXECjLiKj3k7VVpvEKdaXMPhbwdxjoQOkWpzAtzgjUHN3cLzfdr15cOF9cKblysws-KJF_oXHL4P_q0gb3NXukt0_M2isyhROdCoQ8CVTEja_QVAg56ApsTNcBBgOqdwpuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO9Zxj2k3c-u9A3MD5o8CW1a_I89bVFDRe0LO3kmO_T2UHbcYCJ14dculspSOtdEpvZuuyrIaiTKpqzNvF9MF5MpXTWyzw0aPpwcBNRrp49uA3HTUwOwiuRFJLdkeBxSAWNNv92QBLZD15hBQFkFyDg7zfPKhtA2mBuLNcT6N1D8W9VZoRxm1V0G7LcbxMSQXzsP26EqVKbthvKW1c8y8bkUzQJGXmYnyifbEwrJ1vIn5QNv7jbDNUZkB8tLoDsimYMTPcfZ5hgbG0KdPz61zXs50u9MFNlAwhTaa0ivrJKEGNyKOixj6jM2QfBtzBBtN6AAUJ8jwhDBKeGRsIXP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1erqe78W6G_ORauvCB4ZcA05hxQCB-MxGvTlXu7ddHa1FnjdoWHkv6MrI0AZMrYJQPqjxRO7kRbwX_7Zr3g6YivNDyoG1mUnUS_Gj2tBvG2V1p48kJ4IWqqj8NjCZSuIrS-8dfHtIPvGjS4WMVT_MeY0snwlcORTXYYGdzA0bDwWSBSoPH6UBLT68fCjkJc6PxTFCfM5rxQI11mMK9GHgfMbiNQrSSLm3oLKjwPulVNuqVZKjVtTaYqEcUiqYCfL8FivSullOegaQDKzSAvQc0ExvT8IIi21vNllo3UfQ8UD0_SE4EppzCa9hfTg3OKV9nJUjUQKNRWho87m39gIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=GiG1vjp0X-eVttawzZ06LMbhWVcjKc8lUtfGkcPlAx-GC2mxXK0Fk0GNK5x73AWdsxZpQXE3JWCBx3zF87C1Nrqx2AQF0-wvbC_E4Bo0Z7GSumOCcM4LRy1_ga2a2PBoKcFKyyuHvxxx-F9BlMy4vUI0IThg6pfyufs2kooYoFSfD7C4Ynd8iTp1drFTJnGplvpicHWV88LeEmS8blq6qA3PuZk7gHbZ2cay0V_V9IVbbq_g5UbouZRUV8tUF9XW6agmRKPZLg6KUf4ysG8tuQ7uRLb9BtCsXUZxKTj8xoG-j3IbzA0dqRkT1IYD5HoIsBGej6l6J5eCvw4n0pz0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=GiG1vjp0X-eVttawzZ06LMbhWVcjKc8lUtfGkcPlAx-GC2mxXK0Fk0GNK5x73AWdsxZpQXE3JWCBx3zF87C1Nrqx2AQF0-wvbC_E4Bo0Z7GSumOCcM4LRy1_ga2a2PBoKcFKyyuHvxxx-F9BlMy4vUI0IThg6pfyufs2kooYoFSfD7C4Ynd8iTp1drFTJnGplvpicHWV88LeEmS8blq6qA3PuZk7gHbZ2cay0V_V9IVbbq_g5UbouZRUV8tUF9XW6agmRKPZLg6KUf4ysG8tuQ7uRLb9BtCsXUZxKTj8xoG-j3IbzA0dqRkT1IYD5HoIsBGej6l6J5eCvw4n0pz0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Od7TfafBQCPLRPITJaJVJ7u9S1iTRXUYJFnVP4FNd7HvCC9bGksI-kXEsEdZpqafwe4hrSt22OTwdvFaPoP46xdIGlqanrGmgIYa9wU1f73G4JtTW3o4VNyTvdWj8YI6g3RjzBKpxT_-DQ0I_dffb21PJf0oD0cTwwMzmrgI4iwgpNJoOnqjbCA5bsYoh77j_vzQdzs8tWq2a-nsFLmJJOZKwe5eGNndrRNzFtEms0MxHonZZ177CvWK_RcBV01Ti11HmaZn3O6-QG8J-qaMh6-bc1TPJBjg56oQqInuk8tPmeeL2oo06GzLkcfHP3DOzTf1whswEYeGuxAIBGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=lvafbe6AtVXiyT44tiQpCo1HnFwfdF1nnTKSEgV3oX-NdcPxmnnaPMCzmKmbvCbmM5aEF9CtpMZU1-PFJNELIdoPD0bEQMJUCvROM8_cJBKvIX6EbTpb2_S1KIKhUkkk5TPeWrEqTGK6cMKaG7jeeF7tXBfUnK3lnM_DlDLSJxLA-AGjvGoij3-fxpFotNkmNPolkTnA_aMBaFrn3hP6s_x56kHacDq2sUdGL6vQTCBiFVq8OLQejhmt7Qjs3EIVxIPRip2yY5qd-mX3nfzHkJYcFN5z1on6vdGQf4fLGT5SRALXNZuw3kSaSOxZdadyfUxiYhAoOEZuKyTrqpmbug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=lvafbe6AtVXiyT44tiQpCo1HnFwfdF1nnTKSEgV3oX-NdcPxmnnaPMCzmKmbvCbmM5aEF9CtpMZU1-PFJNELIdoPD0bEQMJUCvROM8_cJBKvIX6EbTpb2_S1KIKhUkkk5TPeWrEqTGK6cMKaG7jeeF7tXBfUnK3lnM_DlDLSJxLA-AGjvGoij3-fxpFotNkmNPolkTnA_aMBaFrn3hP6s_x56kHacDq2sUdGL6vQTCBiFVq8OLQejhmt7Qjs3EIVxIPRip2yY5qd-mX3nfzHkJYcFN5z1on6vdGQf4fLGT5SRALXNZuw3kSaSOxZdadyfUxiYhAoOEZuKyTrqpmbug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFVeChk_tbt1rW1DMKy8DA8-ROGHsfLvfLd1UoKpEoFIuyo8pCJgT5Alg1TPjmp0x48AYMoiRkoMMuWiQ1AUQKchk9p06P1U-jF56FJn63t5j9xug5733vxEF1aAHHttVWcMMPVfKd3fdBmn4_cJzddKW-muzHooCHAVFh5utHhnZmob5A9vP-iBTJz9TtwzmNjp09OyhzMhglXjvsEoqp14i5YFC-Jq1EsbCQ3yEpXcgKLnzimLm2au-qCQ0Eucy_IEICmlb0_RbzrTEwVB693dpTHRVUYevk6pJ-6XTTpjswtZkIohFATHuS8yVCnET_4pkKSyWLVs6QRutAvjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAfoVNjNxP-MWO95EAXRuA74No1AcdWwLTy1IStmC-lUy4514lpuDEBbu8GzY5vSOvwIY-aAwRB6VQueCTwITqcJWpLxuCKC6WQIVzw5sd7tR3tEi3tposNQXcowkX9ceeSew9TkivSbBpF4kt9L1u8Oa4HJuZEOtcRL16xU4_sYHNtZxipLBg1BdfeAmWOPY7lseohkvYUnMycbsqkrS6PbNi44ivs415bMRVSNKu4JoQIgbKWuz6yNqAK7Rpxd9XIPsPD3yYDnjjymusEjLoPBE2iVvXxFvWXadrJPF8anHA8sHPTMAIRBSvK6nBFoWnFYYaNmq7Wf5wSiphvljw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ0mAM34qD0JIZjC9tOfeS20LwlV0qCRHiSmFbPNXIAs5AzZdrlNHoJADHEPKBZkeufEM3-bVPNokQLoUPu64R7jUFAdJmkqSd6b-jSKGOxqAQ8yIEQfEGcD6PsRwOsqIZZ2LjfmLmz_gowrx4ZooEl6tftSgQZVd9l2rZQZAiDFCfPtA0Py5yHDqsBcNAmuuXKc5NAyrAuz2hwzyFoHlj2K_3ZBA91mbvmBZVQtIq9pob81DpJPIFx0M2OFFz_TIJIouUkAPnKvaWRf1u9CKKPD35h6marc_Vx50GL8YOmCm1FV2ZliMxmXdt6r7eN0m8RNRypla4akPDStYcBr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtzEJjAiadBkpOk8hRdA6hZGwiwkarDFR8lkr-rD50Yo4rT7ZrJIOUp21mm2EmUGowpIw9-VcDXFHirBnen7-FVsyYsJzJH42qujPr93_TdsTd-XreZPaERKA9zM0SRM08hAtKasTD9SalHKkFoJkbbShs0t-zjopG0WzO9dChEXWVCKHqXopFeuuujPBXUNwPJV5JdwZZ6-5-Thas-5iwFjNmq_n9WsRDKh7jsVLyflNOnYOVTsKjmwpE6kHXQ7IGcSJgnxQxgALMsWAFwPFf6SRaXGAF78wRL0u-1jcV10if-yQTvSWG2T5hETjBfusPymsSpr7Ey4Wh8xU3KqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOXLtSgqp4ybD3AV_clKvbcObNgJav8X9Trof0v7_wDrRIdeBpQntfYHLyLkr6g3F-8OEua39YYtH-Pboa8QaT9RGscMJpcgSVhuz8QLB6qpmf8dOEwuP8RbUjPO-pu6hHSOJ4uUwvoiSrgMtnZOz-ZDhAM4aOJsN_cxw8B-aR9Wy6rVwRSxBVMW0wMSfkVkyz83MVMvds89M-nyTtQnwy9gBTI7WasW9t49YnfnwECNQTBhvfMJAipHi7tQaf8g9ibamqY6HJn-VNm3c1oOx45s-HOc6y6qkWO5krALbs6t6-k7mk5KRned-3UcQ9yN4JAuml0bliLaAZnVMHbR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGwPAMJrT6AIQHZgd_0WC4i435eeJGPLoQzkJfO4Nqh83xoKHAl-BdEaU6CTynd6lKbT6dIZtxCCiEss-NHAImhCmT50zBzNeZCvAQAI8kVnJNtXZQg3pJvaRfeUeGkwz0RnUq1z6Ii5YyP10U2HXcejYREuqur1yn510jQXjNrS7weToDODtabNoSxtXK_bEyyYxL1hlW7pV6xeXsvADWjnSNKCD8sdPlu8Sl9FXMx0yxT-ODL35NA1VB49VnghqH43mjOulBAfPQbago7f88F5L-UrbnuL8Ss60gAHukK0jEV3f-mLO231HAZWeqDfNYpKolyrgaoSqUcs3KzJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiKgjoCcaSAL79GhggbcV77N1eQND-fJN0cOGZFSUbzcMw2rxQzKdxebjtll-_ORw4P_0rq68aNy9s-mi6anXN6bTkFfUrKgyfK4U0uGxqseVLWOvcqBRoz_VKGP1WVhrwhn4cNySVF5ONcVRDBhFpFutXgjAf3hkKkFvC75kmyFAwBOFi3_9fYtaavl1aR8J3cxCNQGzK2tk7-bwfhG5tGSTBl5oS86MOvOJVRVxbNJLzJGwRkhfshpLbNq_-HWY6b8ufFcF8zhZbMNFwiCeY3Ha9bfJSKfyvxdWBp-t8ynY82egx7-mbXrzTauPmj5C1Saii_I4kpgxHVqGaMDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8ba8mGGeZmbKSp0L15i6ISy_7AlV3BeCHLoXH-qaHA_93EtkvZTd4YPRbbhBtF68ke0Rm_uOZ-plee_toY5O2vU4uLL8W_Wiit_991m2comVTgFoxzSOjcHc5y4kKSJOjyQKdyvMxC9sKPCGFxNFhNyYkPm-unmzLp8r6qHiv_5N-B0_E0ZbTTDnH_tKkW1yJv-H6HDEXDYtksxJdaXv6KN7O9F1Jj4aa_D426Ep_M4lh9Gx_vBGFEaj1TdNDTtNW5_Wf11HFPsaS_Bk3AaP6RV_6rCSHB_pu0MTs4tBiU1FGH8NSryMlfIfdsWg3qKVUrUqdz_BFEM45YeQG857w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=UQz4woyuydkQ7LQEpnxtRUJYBP0ly2vr4czMZrPkEK5Aw83dIvzmQDlNfi14VmJV76lHPuIAjJOtZCWjVCzIIcQYLCg9S_CdpE7kM5vTQ4SQaL5wojdhRIKwNQgOxY2-o_tIkx5wdEnq9CMZAcUQEWMyDBGtivQYchPG9z8qfvfVrS492R7iQGQ5EUMoQFPfH41wFunRGwidQfuJktDm4_RiXSDUU6ZN-Cx2RYwNA6VmtUfHSzecEepUQAbclw0KLqeZNj4c-O7j0wMpWKjj8VdtgkTv14VRiZ7-5ATByQUodXJtegteE29ckFK1ukTAecNix5zjmvW-FB27HX5DM43lNZmfU1gKjyLWIlLFqyr8y8tUduB7pTCxP85ND4BfhHrfK2hzZdGXNwMLiYz2YFx8bZ1AJTZNWglZdyUw-LxILHlM1Vceklq32RVCE8oh30EXLF-XdlN15cRr78836-aen7RbhciPs-sA3Iffc26kacF_xzQbzHkAzlUQCbbV6sbJwfqDEKHMJbrJ6-eWN30R5bDufl4nSZk-Us8la6OEPjQBdKNCXZR0XBck-jzv6A998ejfXm43ZK85VB1CRxFGPYaZtficT95nvmcK4K2gbQ1CYprAlGGVPOJtMxAb331ISxJSuqj1zWcO5K1WeG2jhTHCdmgYRk3gpsYq4nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=UQz4woyuydkQ7LQEpnxtRUJYBP0ly2vr4czMZrPkEK5Aw83dIvzmQDlNfi14VmJV76lHPuIAjJOtZCWjVCzIIcQYLCg9S_CdpE7kM5vTQ4SQaL5wojdhRIKwNQgOxY2-o_tIkx5wdEnq9CMZAcUQEWMyDBGtivQYchPG9z8qfvfVrS492R7iQGQ5EUMoQFPfH41wFunRGwidQfuJktDm4_RiXSDUU6ZN-Cx2RYwNA6VmtUfHSzecEepUQAbclw0KLqeZNj4c-O7j0wMpWKjj8VdtgkTv14VRiZ7-5ATByQUodXJtegteE29ckFK1ukTAecNix5zjmvW-FB27HX5DM43lNZmfU1gKjyLWIlLFqyr8y8tUduB7pTCxP85ND4BfhHrfK2hzZdGXNwMLiYz2YFx8bZ1AJTZNWglZdyUw-LxILHlM1Vceklq32RVCE8oh30EXLF-XdlN15cRr78836-aen7RbhciPs-sA3Iffc26kacF_xzQbzHkAzlUQCbbV6sbJwfqDEKHMJbrJ6-eWN30R5bDufl4nSZk-Us8la6OEPjQBdKNCXZR0XBck-jzv6A998ejfXm43ZK85VB1CRxFGPYaZtficT95nvmcK4K2gbQ1CYprAlGGVPOJtMxAb331ISxJSuqj1zWcO5K1WeG2jhTHCdmgYRk3gpsYq4nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyjoGW0BxUqaAUvUCCGb0kP_HwWtU4DZDPzVLUINX33jNDtQRuJwVWgEUp3_dpR4I3a09jqdEvnRnNmk6TFkm1pRiG9_-VTneQCF0vu2K3LSbrRKKuotH82aPjmtGZCjgK_sHitYlQBs3hNSZum793R2Vgawl4hd1S5iPikCzfF5mipcRbvCVzfPW1SV2LLbGOWZ_KWo1nWfLfIbEJbxMlegHZ-gJexfinvvMg7hjgCOBMYfU6xXAuJBTpBhcdJhHI-n2L1Mtmhw6Ngc-y-kmEO8R4E5hDHBVQO6P7sMu5wrF6ZkatCQNye3mKwERHwOAFYtAEOoAdw6OCPb8fV7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv0y-9ec-oxLOrt2nIKRlhe64O8lSFMq6eWdofGjfZy91Lp-bKCR4KVj6bOd0AHZn4N3vcuLAjz5W975BRXs9zGUanpPYGJxkipodAeZ5Fde7cqx_2jo6Pb_mjTfjiBM3wK1MIL1-8A4OHhfbT8iLGtV7Z2NpiDFbhXVjPimTSwGEA1iKvxbl0SzEkINjgAPAEzbwGpdq2KpGpJMdAu-GZHd5eq-m_1uZjv1LifagueR0K_Xi9pD69GNKT0a1lFEjWd2QbbqcByG67EFpvhLQR9WGtOtzp9kXafFAdkS3pxlC5JnpquWHgFPnMVoyZYMa1li73ocy2rDMyWNrWFvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaYMOfeoFBp9U2PK_N_7TuY5RJgtiKbN9yzMLVvPP7y8XPSDjtHqah_p0CagDKK8X6JnBCLo-YGxwxfOAsNch7x8M5WZBNt8h22LKTB9FdPdMGtv4c-gZ7-zaiuXRtKM4Dll1e6LKu7v3jgrtS2CzYixQXTBw58zE-mt1ybGQ9Zlx7dZQT5dRVTTdgGe_cCWjpzP5abKKo-saesqupE7Y2rtzYmLj8KOl8WAyaQw2221SAH_6gkK0r5lMT2-OmT0r4sIk2SglWggClFotpsMBb6HJnNOkZR_ndzPMtgOJ4DFsohZjo1IA-4ll8ZsEVfxae0ZGLE3MSbY2RdOKlqP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkXs2aBN094q8vQ-_KzE9VVdZlpEucf4WVXYwtoXN9mG5kP4tAozfNfPtyTOvg37T5l4CnDrwypw5Tdad1nCfe_GO_vMKY5KWKWSv-uy6Xjy41xc_2dkOK84DtERa0PCVi8Zda3DxQew7pQ4xZsQNdhelLosAfEr62Vb7zU4wF5dh1mNQmAJoNnESfvpZezl2N0uG_RG9rMrxk5uttGSFRbVsixs8oEHwfGiIv3MQOIlhfuIMI9d19L3fqJl3ULEHw53TwqyHe_eeO8Iv4eR7OMxDuzYqAuvLbzmy-jYTpBNqNs3onLNyob0tcVwIGfZEc99KgX1bsw5TzeWattOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7iN2RIDBpufRsHCiaN9Y8mpV87Yo_J3Xy-D4x1-y--dLUkEHELj2Jsq2fUYpjFJmhBRDps4evjnPmg74ykMwU6DHSoZOPL_-A0F_8jxyB3vUO47Njaef4uXf8pg69IszpZrFzWPnV3MJ0pw6esViEnRtfaGlFI7mC6Ue-CELauC3zgORmSTT14NmKkBSBZ73ydzuPJYChjAMkWRyPX_52fCQOuw1PjAQWzOO_zTQAc8N-cXMJ8GAJcb4WYq__zuahbgfb6nQYTkedNw1e5v0yzXLWNOhJNsGsjiwsOF_fielHkDfepyEMtQNwlIgNhRb0ZnDwUrrSWOUju3EXUcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1m_3-y1vc5BiWyYo6M6Y7IHjGBsN55wh0I64pNeUXbO3CVDPh0Rk2Xlevho6lLx-8toH6UB_EsNUN7xVt89cQ-yHBZBUReYbIx5lu05eVq5OEyaFKYxZwEEEVwGysBUpw0jefrQNMW49m-lgjxD2qLt5PcIYTTZWGXhcNDDHiSFYqf-HHtYC4um5fMS3KUxmHXTRjHPX6JYeuKUq67NcO9sH2l3VxPoEAdfTZfBGmDx3i1uLq6WOk4RWqot8Z3NICV22DMKBKuEfQj_zl4r7AhEzAfgJbxs0OR_Jfn1YVbuzJDdTs1LF0FE4M2NXPS75QbYMfdsbTIZtJSo62rh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=AWGixW7MsvE0Ke81Er6jlZtpoSPDXPH7YUHX7FmO_9jxFL69zXvk2FnlG56sv-TazLWHAjvOJegjfHBA3K-eakuG-Lj6zPhmn6aNqjQ_9fX5q5kmn2y1ImZHi1XPrSWtmysm6XGMam3N0eQ1w8iq3FOKmy_h0DnmqLommy7ubzMs3qxCITdS_Cg6n1XIQPF43BPtxpnhoOH9UDPoj-xV9vllED2iim-Z0xU2-i0jEPkMZLoToXHI1RgFCmdh7zz94dmN6bbC4NCzxh_JZKN2Vpq0UEEeSSnqiPN0EW02HBuCJ5EGF1vHthT0u0JLOUEIhPRPwad9Z1iw7iHtJw3Afg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=AWGixW7MsvE0Ke81Er6jlZtpoSPDXPH7YUHX7FmO_9jxFL69zXvk2FnlG56sv-TazLWHAjvOJegjfHBA3K-eakuG-Lj6zPhmn6aNqjQ_9fX5q5kmn2y1ImZHi1XPrSWtmysm6XGMam3N0eQ1w8iq3FOKmy_h0DnmqLommy7ubzMs3qxCITdS_Cg6n1XIQPF43BPtxpnhoOH9UDPoj-xV9vllED2iim-Z0xU2-i0jEPkMZLoToXHI1RgFCmdh7zz94dmN6bbC4NCzxh_JZKN2Vpq0UEEeSSnqiPN0EW02HBuCJ5EGF1vHthT0u0JLOUEIhPRPwad9Z1iw7iHtJw3Afg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvsG43rzDtOSEm1SbgW55Q1KbXIK-BFxP7SbeposFXQJC1cR8U_X3Rsz96b8ZbBMb86D5GUV-fe8LUpzCPa5Jbe6zbsSQueHiYZajvHqgRjLKMaIAQ4MOL6VVd3C7qSfuboDCf8vM48Oq9v6yW9ks1rBkeSJiIHh6kt5DDSButniEivWdvGqwitLOOXfhh6Z11y4CWicw4W7Tjnpjy8NVz_NniTk_qOtSNgDfCaHK9z1-C2W0D5bZNPdSpd2oQwoM-ne06-Z9wsEHMF22An5blVHuJtZBYf8aEPKc5EPbxLtO2ak7EZh7B8dtGFXBTO8DxZIOa5lek4g1EVm9BwSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwFqfGij_PEwy40q2V4ef7clOR-ed-h_NXXz-b0lJgOIXSXcjQA7Qa6xsf9SfvfnrUoilN1HU9lXuoqxck554mN_pW7_CYxZBqUAoLqfQL2-Lr8yDH2Kg5uQLyK0dtBqXdmhWbNzguKyXI1QS3wZatm99S0hmX-uMtNc2TrPT3nM38SoHJQiS0_Vu2DGjA3G46-0qh58qKVDs6hOMz2AZ8Z4cgWH_otWZ37vlM74r-yLNECadCxGNXWw2jwbS2uKjWRvGIllXTGRXkwmFZ9yPowE5BXyAPUVY0cPU512XsEpv9polMo_WYmNEGRbAXYlzdyLcQ1X2ASbq86fPlZERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvfMdeLXrbiYdz07GJih16WahEQJQCo-ZNbjmbyVfDHvXOJ3w69xpV16oXJOXbVcB1pONIVvKDIURiMVuYSw0-mZQvTxwMGkZgQcRnWX0jOGt-sOlZa6NyPxpODT1JRN-mCZQDhW4xSVrPf3ndD_HFpk1DtQzgQYyPhdt1phdDqAS1r8iapkCQxWTYeD_1Jkt5wnXszUlxQCjMEjT_UevgrHK2GNvz4WHXuWeGgfpbv_Av25o3flcyiJ9-d5ZWwwmgAvqK3lv1NUXo_mzy2xTkk-1V8kJcNpD407hdGEk7KmO5ZBSpYYYVQI7jreQs1m9i50lXHm59Di5kX5QyZwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhEK-pFuxSDY4YHJrTqhJ6DAXaKVSIEYHd-iCXu5VHrbqxHcvkOVSRQRNdsN8QgfS5HprWZN5ToCLg4zkcOqLIk4ORfaQZR0-CxcTuG2Xgw4yPey_G1rhapcJrps6vjZCWb2wZppVCtTWB3WnylWT8-NdXLJ8f2x_Ma7SQgg0x7UvRK0T0d7IzRZE5h8ylI0SjI6fmZj0t6QSgtDTZW_SJiOXwZ5EIoZxiATc1xIU4RmryY_4Dohya4ZQD24ftjYNXabYd_JGidJz2PVczIvaU1AuPD6IoNpf6Ax_8-fIXEd-XvKC5KfkcW-nM2_kjF1a3TP60wRAWiaIXzSQNDJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFxe-VaofDechBhSwvY7zVTTo2eBeLGYCDDAAMF9Ru9xQapxG18ncecK_cxtdxR_zW236Kd_mXz3an_fCG8mzb0Va8LeXmhEbkDi2mW0wlbcDXsDK0hNnf-eF7pPE_eRD313imsIdGujkSuOdoDo30HzN3LBfeGJA2WlFEHuqIiDUE9EIgaRc9EV2R2MKhQhosQ3USmHmXS6l6a7Tlri4KgtLwaL22mG6KBJYfUDzF-_sU3ZWSXdVB4Q4f5h7d5nfI2OYXFnVeFeemMnc5s6iL7z3T2tWGyDcYtUa5QvIVROO45VZlbJhzYU_0xxGPhtNA4KkAuEGMM_VUOV_A09Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3727MY37PqLlxGi3h9H1DS20Zs0dyk7P_suGscPif58RaXJ0F4z-DMne4eK_ltOAQo9qcMgyuHhsnr0rKfs91Xlgq92qSjfmKF9GZgbYeo5IKh7k05k8B9IRDg8JHH6B3lI7bEFWLSqG9PabIdlBdiZRLP2Ldylr9IEkvzmJxDsEHLjvYTWenPoPFkYagLEuyQkFCBodqFLjihW_FXdK9yrnoUMeDcovl8c4zhd7WpPtOxGBA-vfoVKLVPZH17OuUZJnkDLk4MuYxOlxGcg--cfXNxWHWOm0EfDGWpqOFEb48uE0EedKF_Vd3lhUPZVjgFYERzRUoTGnSPKEu3eeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI6qG9Lakk7DAUFbr_06zK68c46WIslyPXnKkn4x6GT0j4Uqi1BczotbULa32oraHhAiX_EqOhKFNjEcC1iGg6yYB2WH4G7qMldcegUuK0-engoziixfykL8RWOmvf89jb08D2uzANzt2GdIGIlpt-G6SbXgKenVLxmLdU3KDKCupPyJudSHkEI1tYUUOhwU7YJdStlpXLaSHH1L1fjh6rwgNQhQUTrMbVWHVM-qAHFKrOa-yMg06m7bDxukn6HgKEeSV9WDxypvpJ5ip1uA2lgpOyYmVFbxBTYCIYqn2gpk6nkT2MEmfMrQ1Ng35ysWZNU3BP5Llr_7PKFJxob5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNqibuh9h5NiHQSTnh35V8_5T7sBjrTUc6xetASifDhzhj9AyGcqQrlT5lhQvpJr9ALJRvXFVQw7dt86741d0hvEgb--qMxWPUtduaXYeKQbsiu78vDletZhwlAeRrvRUKGfQmhtOghtyk4-m6b9Z5rfhnWEpoBrG23OR_5r369JIqyFiekQzbj1vrO1K3RlE6brT3CWth9Rbvd3E00teFBZ_k-HxOJORy1I5TxcfMUyAW6tuF6RE1LZGuQKZ1V6wIiNrVoN7-Hw0MbUFqUaexfeBYEa0_mIKHchVkA1bxOe6aJkquo2LbeKlA0ddlthmF6q-HO2hoA7OyOO-ZeFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKZe6QDi5RD8gm9cjs4lSad59xGM9yELEatx-ocu0omJ09EZJGDvBWBZOkj0itU6M8V6Q9nph-Sn09wSd0EnYpqNSJodMoSsoIicBsodX4K5oHTdmCugTu8uY4bQKjPdLaIKiZK1SJRIL7RoQiSvrhIelRmwzKcNOR09F2LeXdEWAVFR_wmtNArJGeGf4sJhqq9Nu7K0g7RSCVBiKxrhp9dKj8E4O9I_jF0TrKFGULgohAWztwMTMT_DMcEPTzwuyiJZzFsQHPehzehLvAn_dwXgMp1K3w6rowOqbJA_xoFSUCFfXjOaDxATl_8nndcWnL5ntFYVta3AWroIQThxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krbMmP8K8xKnPLSfJ5Sy837yDUgedcNB4dk0EvWQDzh3DSvMz65w95VdJyRO-jQ4vZgc0T8gbW2I5o750AQWSFdIGmW2jZ7I3WzFzhRy5ZuAigpqM6Ezy4RJng0WtzGbLuSR15Pnt_EI325ymlXH1YIG--zYOc6xkXvb3PqYIV62SR45QZULiaimLfSOHNKTH1Rb1hC7F9I5IFr3QUdVhfmREQU2tPIooCWPpA5vm0juenB8cf8Q6j9wUiN_3n7dIR-NllL_yUxOuuRY--sG2I_-fi1z6PCum2KwBsbueW9CCsjiZuH7Pr8MbhLgiD73iHJH-avhaCjkf4EIhhwkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=sL__yzdriFFiCZGh4PfsezvnO7s2j9Hslvyvfsn1RlaEnEljchcbFKhjt3mQGZ1i7Th_oI_F6HnJ2E0tsYWYW03U_vN3zZJyTYHt2lCHGp8g1kRYWzEUauiq4IfoCv9AF2mr8fAFkaK1aWxfBcHW1ytK7R1OoqHZoIB-5fzhhBRlCvRVvHdcLKFA7UKXwvueEiDDue1ThLHpgOhB815cJGb--cjkMH4dHA2iCEK-y1WAOoEHaeqesDRK2sfOrICLlJC_SfoEyDNSyuTXDtagLHZC6HPuPy_JovIgDZYV-nvRIbWIwDqISfBVUJd3bJ2EFjuOTCelMKRD7pjKbPyJFWEIOMBu1z2DTqBT4PR05zoodr78kNyAUICh6_SAfkjk-qGzMX4KFtjxmA6WRV3ZY1wiiDE9-jUSImW7i8E1o49gYXKji6tlTLPwYgmYdYq1M6jF4i0VYHF4CgsnL-ZvmOwFNR4Kf3XKV7EavZVqtPwf4mkxCN4TtX5rpihWCAmnRpINNiru2ul82zdCs_QUm-ulSopmMrW6SpRWBLYOiAhKhacqojPTD-p7IsO111xdG8thjtf08_HxpyU8zZSw_mVfab98Nb1Dsh1wOv0SQlsRvBDbEF_A9Xg8f_C59k1D499J553aUYh0qZC2UK0wwF8K23kLNUboS1BoVluIF3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=sL__yzdriFFiCZGh4PfsezvnO7s2j9Hslvyvfsn1RlaEnEljchcbFKhjt3mQGZ1i7Th_oI_F6HnJ2E0tsYWYW03U_vN3zZJyTYHt2lCHGp8g1kRYWzEUauiq4IfoCv9AF2mr8fAFkaK1aWxfBcHW1ytK7R1OoqHZoIB-5fzhhBRlCvRVvHdcLKFA7UKXwvueEiDDue1ThLHpgOhB815cJGb--cjkMH4dHA2iCEK-y1WAOoEHaeqesDRK2sfOrICLlJC_SfoEyDNSyuTXDtagLHZC6HPuPy_JovIgDZYV-nvRIbWIwDqISfBVUJd3bJ2EFjuOTCelMKRD7pjKbPyJFWEIOMBu1z2DTqBT4PR05zoodr78kNyAUICh6_SAfkjk-qGzMX4KFtjxmA6WRV3ZY1wiiDE9-jUSImW7i8E1o49gYXKji6tlTLPwYgmYdYq1M6jF4i0VYHF4CgsnL-ZvmOwFNR4Kf3XKV7EavZVqtPwf4mkxCN4TtX5rpihWCAmnRpINNiru2ul82zdCs_QUm-ulSopmMrW6SpRWBLYOiAhKhacqojPTD-p7IsO111xdG8thjtf08_HxpyU8zZSw_mVfab98Nb1Dsh1wOv0SQlsRvBDbEF_A9Xg8f_C59k1D499J553aUYh0qZC2UK0wwF8K23kLNUboS1BoVluIF3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlYvDRrz_FsaIbF_JfkG1uKzikHZRBH_fFxHdBIwdQixRxkDNDWwIWjJ_6mxnxDpitRkwcfb4MIs9pRyiNwPTGePeQ9dmjZe-o-QcjUoUe-Oq_ESWyH4bzsuwJxC3aCig-EI8W87mc7YlMhOjxDTKS_0evbYPsD7ZVJ5APhBxmzmOBxeiSpvjW9shYDHM58KhpUTdTJJgz0JQYiTir4X6pJ0Ly-CrnEdfXVzdXlpC3_o2NRcFDJTmvYAqIr86f_64Vp_Lw-d5YnTcCUpDihquZsC9L8oWNj33UtfBNtdcq-5HEJ9Lq9wgrUsKYXgAmqCBlP0MTds-S_EI3KJIvbrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwT0O_wWk6K-5ZiH3pEt0_C6yBF2Pd1aIWNUJTktfeVf_PqOTBrJULVE6g7Y96iltfWyK828JI3eg12IBpK2ReMvKTtkIJYc-0ZsKU3-UszODVl7VWvjOkFQybPqmz8fUE_7k2lcg3wJAlbSPCP5RpkmcGnIYquPsxmTeoZvJJ1s5fQg7EZqWHcsMYQbHXOVyy2s7tGoaWltvkcH9vyhTxm4PjVo4OVPu8UEdpRaF78B2tka8_4rEKepgBqaskOvuz5H6DmKc4HfuOEipckCItQW_Qkm9bJWeJEYKvfsJ-ZoD2X5QHMjxvh5hTeK8FWzSsweVovgSLPERAPAHkjYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umD82K61pNQHRaW_zE4ALRl1bTzHk7p05jjWMpJafIXrUZh9-FRVmkv4nYqS0K0SCHOk0b3WyNYZIHelPUWvkw2lLP5E1aB3TlV1bDQep4RFPLxyB643ATWOt4HILzsjQX7DDEE5k1KOhij8UEBnGIEGNnvBXd-1cEOCLD_QOpqfemOwWI1O79WdDh5K85KF_pHLaESTiQFSvJjOf3B0zVjixLViqv2NOc-gwXRI1MinPlrYJi47ehfWuUnz4zX82mDSBv76P1zoRO8OdYD3eEJSTv7PHZD03OqvR9RSwS_UEfhRfeX1rV6CtuC90mnuDtnKx4X2kPOdV-zfYpfTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGFhz9X1Y83nVT1SatWnfwZADlJ8Ou5wmuoQvtpCnPVKJvIZ-xY9X72IN4MUV73x2iSwOgiJNVj4hYShrgjBgzI6RnNnuVx7gyc5y2p_C0qsEq-DZI4AVSZGTv9rbgriMbVu4q_fk_s7x-Yi9XPra5t3Jg06WfMGCf0pdUjMgAj6Y27xauclrdxTuhuPpIVwu9Uk6lvJDn2fPQqHpdnDhyfKAuC1Xiz3p4S5-aMZ-4gJjKjASRa3H3VmPiyEeO8V2FhQachNZKb7oa4rp5A7_cEDgdXhZa5KsvAsvs583hOoH4IAYMyLMowwfTl43Bo8bAGDxyl-2meMd7C4fLXblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfkafqjg4lqdaKH-A1oJNa7kXp635TXFtdtk9_fupsyquziP0ME-swAoDH1M0HFD4r9kOHS8FPNDjV3IS4E8OaP5j_YAH8aUUzQfsUvq0Scj5CI4vNnYZ0OXrRITXhf4_ulyMtJFi4fRHWQQV_-azy4c6qMKT2pjBPM2Ulq9s09hLVbOYc68fj3bk8SS64Oefg8RRFGgVFdMk4FRuZWcL3hpXOlciPG53qlK2p0q6eexf8bo7yuMsHBSARQNpSpBZvdxr7pJd47HaHCp07qh8V3Nq4YIWRgDOuvuncdFvImTGM_qcBC4xYuZqNPDceWrp1SmkD_3vYDAb6569UiavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfkRqobjS2WbiedD6A-gXI11MzNwr2cq3xTdtd8fZ0apse4d4ATDcWybF-zBHyWxCUaeehtY1HHG2XoWdhpCaLXgPPTYFtBOpzolE7SmwvyVJSizt9YXOl3Q0_gRgjRDr2657Itb4Q7D4jtLgvl8HNFIWAuXMjItrZY0TjpcNk9SyIfxtV4oYtLdIBihT0Gby-JCnr7O15iScNe4EdZ1nVh_FClCDE60v9eCsO236MjyITp1LSiBCk7eIRcFxJv9W9JqtruNSIjNpMi0qUSC_m_4ri_P2pa56vpmRdJzLonIW6qh3qePrJDGqRwSuJ26bRdCvjbhVA-riKyYN5TvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ9GQ53mrMbzAhvAcxhBMJqARURz1vkV6CIzpRzOW8aYBGog4KgmoBlZBO41JdAKjZX7_QIhKP5OOK8EwZ0a28Zw0Qc_kPEeWDI24KZS0eRp5bJsevOJn0rjVUNKBibIDDGegXreTHBAxnNsIRgbxgb2sUdcNBbGSTd5-7nC-UP7zVBL3JElmzifpwqQTqlxcw6YDBe9oCSKMc_iV06lGWT2_TGMRyf9bLkIQXLggswB-A4VGJVlANrJwpT8Cj0JSScY4TkJe3kSdqmhwmnz_pmq0W1ytjWvq53_A8Mye6Pi_5s-lYc1fnxIEGMBdcP2JNl5lzFBWrGw9zdisbjMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRrC-aDt9QQzIv61rT-_nPldg9RPv-q5-gLQM1cEE0m7EE83sO4uky3ontQEojZhoWsmkTD2b8dS5AKXfxuVsy8A0quqc8l9U7VKFK05v3eYP6Q1b5fSpW1A5iqy_1bvgRmOV23QAUfZUMWHl7R7NgAmktwHfuPnhwXP1Sr-aiH6kADyd0zCge78UI_178BhKD2Sv5DPEFQ1kZeyGPEX_cktlNS654IfwxxT4dw5PiN6eY_dZpH7yEAyqzlO9aKRbyB4hbODd75_LsVIEBHDiQnLJY8F0fg_Pj299BjrwH3lDHzpzfCgDbRCQwRja2lN2I7kLKwnFUnYpvJVmrABjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ0rcqcI4RodMpcweEwuXu7Lu4-RkMLSRWFs4Nux2TmI5RSKJdLaeBd71lFLUbDY3NtgVUfvBR1r7TmOEtwPljLUX4qvB8Rc9Nn4okTLN570w9tD10ns9J1zjgMQfTillNU-rPixULNViP81n4NkLqiynurwUE6pj1Ec3jL_sFEN2JV5723L6mubQp74JPHuel5m5rnIt9tnyuJyaLLRJuZNnnwtC_O1GfwH1-CfixCXJQWBKUmPzAjLqHs2XC057gVw_phZceqnHu7QsmGK3NHHip-Gw7tL-yNddYIummIgMfavSOdnrE-H2GqmebRCNUll-66RUH668VXVVApMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YccWLGWI3nw6nZXCfBprRSYKKhnhBbAo2UgR60emAVmr7QwkrLt9vjMFuBj-3LNoEB3qvJ3_kAIpjBA5xo5886avYsjf6EHeBHc0dyRv5WdVn3Dhx95sbfkdQdGHVIGdXVEP8x2BykG7E2uuUFANIB0FMz4t47Nox7GePPGAzh69DcaPs5Hk1LGOpJ6N239jQZj5htIAy8QbGwZqY30qjtGLMGUUfQjN_1_Zv2Cxfp3zZ710ApDxidVoZ45Reb_VGr64haaSRV4KtWQZj6wkIQPYauFzrjgXQmzqJb0udx0vG4UCO_PI7T8P9LohfvlEStd-kugF-R4M9rXBFsq93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6mLYtB6zxHKmgDp7-E0qDAJicWpacd6uyHu1930MV0iS4QycAI78RXg9VkksWfjAC7ODFZhUT21mUpb3CL9KXqpAzeJOA-Req5dqZXCtlFmaafTZGV5Ha1LcFT_85oBxKA21edrt7c0O9YDl2d-Vus2db_KxavP-15o1vdicZuHgt7G10egE7mFEAqhWnTes8mEFX3KhN78v293azHHoZWuHU_GE4CBB96vTQbgpveZHOKEkuPDvlQ8kSp165xXgMzhaURaLPQjPw3oaFlsA0-izGJS-DCnwbFTo0wNx2MokYIQN9mwH1MwtdVvdJPz7ti74IHwX9STcAexBm8kYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYN3Z5qcUPwfGuVjmHsivEX6bdY8JP5wzasJPfspcjL2f-esrebuS3by2K8dK2pn48OP1MI2qnFEjyByRRjZSu1lNUm_oxIX7A6M0pUwOIZ7KhXvh-bQOQN1r2HQ1a99g95eWgTxEfK_m3z_u84jSeIA7XzeWwPRU6Y46VbeudIN5eklfNgogydjrBlKq3uPNRnvhQai2qfk6c2WS17Z-woQQK5DoCrjZd4Cgx1AqBkBBUCZXtiZ-mgqmTpIixl7L1ygu_TJ_kL1tSeNSZzZUHNLujtx1AggQMGGaRiuZRdeIfhZsQKN2cAk201b3DfF9lREkdvKB7XMx_TpeZDC6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZZGewV_6PrFXQtB4ivNdT2dwMk8k4djZtO84pk9z-kPKHAlB90Adzu2KDlmdQKz4IrgDytkG_uAmBAS7cvRRWDuo8rcJ1rT2XSaaJUCDrtIth2xS2plL6ikI4_d0Q8kogm61hFgwzEreell-HcjjN86E22P_gStVSEX3fyVfpO20jbeGcWUEEnGdrLgPuzpRHrXkCoi7HDSkzg4aeXpJ3co5DyO4nfCga1FsbVfuFBMahcWtEXQTuO3zliIPBwVV8p_7BezD5QvyH6WE5I3E31pIKYY7p8RAwP1tTq51Ddlw0WDqxyS_msLeFkRnAcB5JfDvss4kUzhIb0EuFk6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA9cV9d50aarRXY0nQCYsMogHIpAgEZl--jpxNPwfh_v2QoAr88BoJj3kOQqZQRMxHa-WyEC74j2rYBAtiduArUQCQmT4-TIMyuUCMSiKEiCCevRMSmP8f1vYWXbGObuGlBoproWtAQUKFMFKWFO3uv9JxPkOIOtAfsCdk3rXFVyZi0PNTIxpiIFSOFU7FgWERWZVk8tQc7rC59_p_wFVh2qQGajGXQNxHg4B2FWE6YaDw6MbP-RXusYUZdvGp4BI2I2VIJxs-_fM_V1OMeIb7wUCiSJJV9MhcH3GrzU1vat2aGTZDGOMZTIUdXmxrZWYBkux7G9YzfdGB5tcWxPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFyvzUoZJnnOqSVYVIV-KwXgMLsf2Tlmhn_BWHMH1rAwuUhhnYuLGyXkGg3jr2tjL9ZgpnD5IQBSPDxFA-0Nr7UuhTdb_7JIahWA72TWVzaBSMPsNV0M4ZpBAIvmwKn4pOd4usKIBmYJgeOszVbkL0q1uKNxIs99yHjgeR7U1J482Iew9-wjekCB-wd1j4Cz3HCsL0_EZ5O7UtzRiE1KaBWYXZSAutez_IrInvRpq3SwQW6WvXkXuU-zBj3cqvr7AZBbb5gLA9NQFD_Z9CMzNoO2KvO-KZGjM7jajS4cY5b5qQ3CYcv_hsDTB61eKFy8wuP1EOpT0tbBeJu8CRX37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVVP0dAp4zZK_wRjro6dnXOmCYFX8shYs1wLJ1YJ_9gr0McRMdhOkp6zQX7i_G2ZjyxAgf2I47eK-56ArHgOMw0whb_V3oiBFcLZC7D7JRMmUFKy6Uo8YfTRumiG_rzaJp0iqwPmWo58mdB_1C5LCgGx-Xgy8IoC7LuGmtSQ3ifT2f1QeHSLnAyh8DShjmesyT6YDDXVaZX2K40oFLdlXiwY5sl19kRIhzFrlfrIVn_bwolKwrdxKQ7LqWfXq7TMfLnbN4lZpTY2IT9F0Q2d736BIe8oK9xWm7Q1o84HHBO2a8knpwtLnQAv-BouG-gh1Tl8IYrYrDIw8FdpUSOMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLn-zfRsUJ1kU53JJsDe_ctrb0B9k5cNGy8tpElzGXYy5Vd_fC6bqoeIzoBIVlZXOb3J8u4mFYQFG2pQmLpcJvFBU81uk5MsGymg5jVX_qXhtTqYIU96Z5CnEOS7zjhS2vCC4cJxh4iuj11KFemplhwz6bO0n4gf3w0okBLX80Pjddd2byOx6mw8YXLJ5zB29B260P0xlfWpq4NomDSUlm7wOCUASb3ThrFpTdM4ghPMeaCsDLD-Jh94VzooCDMJbf5Q5pTKrbeGNsgf5tnGokkPLx2dBRFEL2Bk4IkrlthLRtUxM7i9PygXZKVmcF5-qmX79eyrhZ2mgZdPFcowuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smKpAlwSBsnRmJ5eGC3jG5ctX1MhGE1Et_tIuu2ccuqb4jibljrQ39E2-mA-Zd7yTNrQoebX6EEyC7uJKeJcKTyK56cNtP3H5O0tubolmvFduoKiyeXtxFm3ryQp6Oj2FtqUqYOwblghgD5nUMlHftzu64wGTVvn8NIa3P1BkaVCmIWkoY9yjGyewVzfBIP_SkgNRoEZ5GuwAEvUhQF_9gfyHKRYssy1t4ODrWKmTH8aS4ro7Xw5V4C0StvBQYJT-Cu--OwIHYgXrSysSv-6ZOrjx6Zs62PTktAp-KX72XdvY9u_40zo60pTQb71nqihpnFCs-Om5bK6hShDq5WIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0zo8ojf0jToFmY1TQ-1gzk1hOfyyK_alXj0pEAZIjc7RXkc04BVIWvnQ9NzoGzOVFP2FUIZWvpyK90cGnVgfcdytUeF9F7ul7JtiNgSYxk6KKeMQvWM8zUH3lbSqda6dA8kwXXk1-5Z72SAeRpqe2o-iwZgderYStF7PWz0ZgIzDlCFtXgOxJh1tT268N6Cc-qfXcY9JZNenifCqx2_JyP9gt85sw_Vs5odBE0jMjLL4wszTAQBlJ4tMluwD0MEL9rrPRlRhtqRvo21XqhsKShRhCQ85_bedAZLfb76Kd-pLE2z7MJI88DwSPB8xs08RIKQUl8puCSCzgiJct8hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=XI_08VyVam4KqqHP1qmWps5jAy925oKxJgBOhWeu5j5Yst9CdhW03GCprbluaWXcijFqIpoDmuazdsVvF_7KEe8ilXQLkDAWcSoFAWEdNV6qsH7wHtoJVrmeamjevWa-w9s07YDacI9EH7MrZIh_4VYnWW1PJcvGDUimQ1V9YQNpkbFO4ojDxbF8nmFaTEZN6siahzFMY1um1W0y-hiVbspvFFjZmW0xcKLgV_x-xLm3WFmljc23TVYfR8M6-r_Tm65N0GnVBtX-te-RUo66SCW92E_D3yQ8rm7yMdfb3GY-M5QPlyeph0UFtQHS8KvqI7zsnKa8FHRsBvOSmdLr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=XI_08VyVam4KqqHP1qmWps5jAy925oKxJgBOhWeu5j5Yst9CdhW03GCprbluaWXcijFqIpoDmuazdsVvF_7KEe8ilXQLkDAWcSoFAWEdNV6qsH7wHtoJVrmeamjevWa-w9s07YDacI9EH7MrZIh_4VYnWW1PJcvGDUimQ1V9YQNpkbFO4ojDxbF8nmFaTEZN6siahzFMY1um1W0y-hiVbspvFFjZmW0xcKLgV_x-xLm3WFmljc23TVYfR8M6-r_Tm65N0GnVBtX-te-RUo66SCW92E_D3yQ8rm7yMdfb3GY-M5QPlyeph0UFtQHS8KvqI7zsnKa8FHRsBvOSmdLr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrnQ6fT0vtt5qqSdQFtxQ0qUnoZPxAsB6aLBdmhlx3MbHgP-PFzmTC0h2CAlJLiC5fkD9ht_tsPWPKwLsbHhnsuO-ZAo2sZFdkDsfH3niWZvaaqa8Gopv0STwKah1idz0Are2Byce9vSZ9jaBU4KArWa3kEF6GFgTZt2HxQZwvt-r5M0mBT395HZP98aPRz3H3NzZBsONzb-3fIblvA7kaJO887mgjKiK3SCFOypmSoe3XJnqUITgdKqwgV8X7NpUr5gwqqF-XaMGm6YaIxHsu0dnTUkRiSIsoAb9DLlTabNJLJEC3CeWjTS-E-H4Hm3ItzJwLpoBrEB4JJ8mZ_TUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb-qHBD-Ap8adnhmUYlF4oZPusSMOtbqWweOwXGst4mBxpdtDW9is5uIG2W_aAycNTqWaGjw-2uP1eYZpJUWHyYhVf2cI7ikekW2x9ivxlEePZx20rDVgrWE4ITzG9knFc0Rfh0J041sA3ztOvESeqS8OUDgSKGWhiTab2A816_-ncSMB-06u_2cR49FEzoY5z23a3Pae005dX3BCKGHz8UAKY9MDvYrsT2qB786MrvRVSykwHicWcI4l7Hfu9o9hwtMPLgdLp9Uhc-M7t3BGbsJnOFJeCwwsX2pDGISP6JvCkk3wKcKtBFz5MFrIf-D2pp5NgbgTL7FyOsupfLE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRQjSJsmHDxvi9dlJ0nmQUGZ9qd_0P4sOJwdvz3tvPkUSIAqlM6ibOKL-ZrS0OhhvY9hHr8smMAJZ-ESOhE7G0HPNInPNJEgtTtrvv2Ux11d_1aoFQfwlf76yGkMbEvvptbbUDDP2w0MYdxGxcbSedbR-E-CZs0WqL95g-juA42V9Dk5dHwCzLlzLi25xdRmU3I06jLIvBncl8-tp7p8OZtqsKkvUJABt1uZHFW4QuEYaGlpP81Dah5-xdCtK2XBCY4HTP-CI4z12wTgIkS4aiUbN0604gc6g2pXO9s3zo-1gC8rVRVaPrJJR1cEE8meQOATnAeRHSIQ_g7ML28ZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5lZM1pH3H1Nc0MElXAblBlrN7vOcHqA8MPLKZPxBqi2La_SEwJEKMQ-ocJhvjXuj2VQXuUO07JaKK7b4Q4P11iNgWmrr_CTsThvJmD4SalP7HhVx1TB7m9qOK8JkSQRQQGf_vYZUe7Hjrb89iYMhUMv3q72oBEMRCsIYFhz4JrjmO1f7k-sAC6HqpkG2Bd6-IkX7mjh-JSAFOssimQdWcvfTuxt-bLmsEYjo6c0_fslOBHTrH9De0HwIN68WtdmxVmPba2ywK_2f98S1yGPua5pf79G97qwNpQ8T21H4v7o1A3dD44aDzKRzP4fRLKe7hGty9cnK3nBfA6dZxdKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=WvFmkz9BCdYpQyqA0hC5ljBqBB0X1OwBHQ3dkNu2rrLVoUVAqARWCxfLl7W9broLitsMBixmYSeayUK6KeYSDJBGBelUxnAwf4rFofXoTQBWKwkYisRhRuHfmFOCNAda4mQfXi9fbEMIF3oGWHX4a2JTbZTFWkYsnDQL5kmjwidXZ1t3Tpn5T8jkanYT3O0UWolD_DiU5_TPVchgCTCyEdp4MS7vSat7WnakbtIO7CVB7u3cDZB99zu30iXxIViJFrt0waTDjGiERcLbJdK9AEywGJ550u3yGAsB8dejEE2E8z8cabSx9sW2x5ZNyE3s7hB9M_UdAvHOWTOHZoMY5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=WvFmkz9BCdYpQyqA0hC5ljBqBB0X1OwBHQ3dkNu2rrLVoUVAqARWCxfLl7W9broLitsMBixmYSeayUK6KeYSDJBGBelUxnAwf4rFofXoTQBWKwkYisRhRuHfmFOCNAda4mQfXi9fbEMIF3oGWHX4a2JTbZTFWkYsnDQL5kmjwidXZ1t3Tpn5T8jkanYT3O0UWolD_DiU5_TPVchgCTCyEdp4MS7vSat7WnakbtIO7CVB7u3cDZB99zu30iXxIViJFrt0waTDjGiERcLbJdK9AEywGJ550u3yGAsB8dejEE2E8z8cabSx9sW2x5ZNyE3s7hB9M_UdAvHOWTOHZoMY5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELthORZ8L3MXlATLdqZSRvxMDHopmaYre_fAwIoOXzzo05GqoFD1p7EYob09Cr3bGyQWuGFs5dxyK7ynijaV23YtpSktm-DlZ24BPWahwJQRqqLzForYaCmnLNYllgh8sDbUdXDlmYcEaUOnrFv3tO8U9xmx7Ji7PRMcCzZM0onNN-A-UjCnQ-xmpo9L6C0VISYUF8qEqlPzb1BzB-1ncN4aQwGbJlk1ERxwlbnRkgg5b1YNKKOJKnedRc2VDhNxwj5OQFoDoP7WYrcGamKy6OWsk0i0vO_LC-ZnhqWoS7ychHkKEGafEbzENP1IPHypKf_zVeO_gsXAQ8v-VqFF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_Ot9DC5VBV381wiN8PJKZVev7JTkDG-Zzud1WhxpitqPO0qMsuHpM-lCXnkiUJMpsLF3v_jiBFiOL66v145HCgRDU2rmQCwLG54rQG4wBnxQNjCoCm-2THH3vw_0Liq6LfR--_Xfc0FGv_YJchI2Tv-tL2WamiL3Jw-bWhBlUf2vpK1N3AZL0oiLxc63jUlYF6LYw3DjcrUc92LZO9M7dzeOEOAcE2thqys2VRlfTXtX6BUfIyRZJTWgiFi9eIBQNLam6ltoTLTOIYt7BOLLSG6xnYwYmLVv2wu-0SjODwJzJoxcKKGAOzIHOWizatWn-0J2u7n15YiBweqzRSkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKFunduWmvBXBFh9SyJUVeJtFgm0ojroWC3ljDr6enkHJZ4YGBEtf8DuKzIZyvc2UWD_x0bOkqEaUpfvSJbG6Qdyv4KEF7tQ5fRhTMYZhN6u0Y7iUIDWvIO0BoF2S_rzqtiP7oTOxzFTB2ifffAx2Ex9EL8cuf8P958Blfq4lzWe1hJ-gN030wDzg4r22xWN4TRcyxtQ7LG6T8plUM0bOKDUHDJyy3UDcc-ebSbbEve_706Fw3ZOXC9E_K0nM9G0D3dQbAE5Zxmi5zTN6ERdZWEo7XcNdl4G9scdGyZnHV57_s5ufoPwA98ZhWWbEnBfUyGIEbChLrBxQDCIoblUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlSUzJpxdNjkqPSEyEvk28ASA13MtlfgIje_8Vavu1fRsq7tjjn5b_c43wOmphqPiETvRIciIFmWI-c15YfvjQANJDJr4sM3sIH9Dzhogkz6ez51d_8k6bvl-7IyMYhhYL5aqPnaYXqTFyNsRlj8IRUKD9Ap10N7Pe32389qbP-1mqDaPtXQA4ZavUSWhlfLk8_xObcESLw6ZwPcr8VmwBNNA72OK129McFNnnF3vnD3jB-XXnGmG5JmsEcaaPwUF_He_OB2q1lOjLCaSK4NBUTW7-KEQEtXANDR4WAClyHv6pYEaXYnlTp8vVK5VBXFYnXd5BvvpzPvwZJDK_f-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5A-UlowQXZsk3nYYBrMQdMfjZBGFmWSFThKzvYSV4y9WSGRNcYa6FcKCJmzWRXB2cESXNLxNarOR8tOAd-DmmmijYVfMAfJkMdmQ_NGLwqLIBi1kzXpu2JU7W26m2VwYMqhsZ4fAARTv2zdEA3UwSqd926zYc1yecOiiQ4QICdADnOQW4tf5I2uGo2JCJ69uPxmq9Ak8zkyYkEZ5wnd2woMd0NgGQabRwqJbfjqWY4_jOuLL8y-ZxvjgogkyqIK4qoGNeERknUrkbbmCCNf23W1fuYxjcwlvShiJvkvnCMhJQLShYwEwbIJlXQT4oePw4N8GFnoZ--ysM9VxEVpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_j4cTQ6Ic-cYcAybNZE13AchE-4zT2UOnJncg2Dlku700u-sLXyfnbl2qabQ6AdSjdQK8wIe-ETdE9ETy5lIc-kfnuVq-bmpwEH5tpzxOYA9mt2-C08Y3uVNNyfMVxEbspF--STInDdnGKViNTskAd3lVYnWJJqf0DSik5wBSZFrmAnUP5iMzq-GlUbQvUjCxs_sWQr8t1r9JZoNVyKC-abDO8OYp0RxYsNFcv_2HpVtOUiurk5m37N3ALd5iJwjSXADTwrTaUtqtYRvGZEUDYLfG4J3bKbyHlPnZFhxbroXbDDlpWADJa9W5jRfZV5Dvoic42YhCJm3w5EBorG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWI3C_t9FTvILlFi_j8E-PbkgqQ_4K0UJvEO0MKU9XLZ3IHpCr5rrby8hRwCCweBLjHbFb4FtRhTD4CgcWdpLs_3rSyuzv55qbpyONr__Aji2YmaXm-J9h7rmOOzoEvYX2qWApSnTvzS_9bZmjQh86YX09RafKoEK0C_sHRWT0j5EfcmS3AP1VuKbjnrg3KgnpgSAlYkOY9VHaVchH9OeWLtfKLR040n39xYpYTkcAznPGwJlvxBeb6nbI8IoNdTJuOWRQ_2lfEd_jXK2vthrvKTs_S5EO_6L-HZnJJoOsEBo_bsNB9DhgN3ywYxtPCk7NvVCEXMCkaSWtElmdCRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUH5F8VTU48As0rbiximtXbBGKyx-IxVviXta-2Dhf0gFeOL0sOf3uRUM5YrtzrfCnycZAgX-xutTjrTErhPEFT3FoPYW1A65UhzrE1MecELvraMpT3zL_rnxcIBPxDGwdFnycWe_dkYb7wzvL2FO4eZHDCF_a1ELYvjE3Ho_9UD4hsqgvt6Oq50KDbclKqiOJO3Hfqq_Adc0ST0Vf7gaRXLEsJacIX49IAfIx836oRV3yJ1cfHdwHe8kcYunLrXRbIDRu7uzrpi_geFN3lNDpkvJO0okYJXn9C2YuNx9Do2v6uT-59faFH5QjaIeB1_ljnfwIop0OlF-7EhxoYjnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTFwYli2A7DNKP1kWomwTtVAOu-yV5f8KqPjprJdkhUkeHhzA2vBlM3LoKZtXK8ATO-5-oXC082brLHkMJuURKrfxj5-IHgReG94HzMyovxpKIHiKqypIa4-P1qyVKJWKL_ashurRjFcN8rr2GPI1WFAKTnbPNxzOCQ5vme5tPYBYu0-tp5Y2HB6i_i8TUvkO11c-t4jg9-F8RHEojx1IwBNhOJh6wpL6wj3avAfZFJ5vsKV_upSwp3Es2_U4s8qOmdYpBBHmUD_XrSmtSHWQCYWOXtrlZEMAbXAdl1HpEK-TXMzEszWuSZxQXtCgyr7iOXbT1DwnUrr8gf-ZTlPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9Tu8gavmo_JrdvXRC2ASrWvou8vIJhdpAEcS03hWV479FEfn9TDMDn5yY4TEFPiwxfnNft6A6LZfyWcmRp5mBoDyySUL7eNV8KGyduRYMg6HTkmkG3dCkl2bV5u6RDLAbvJFWSAwVboemwkFNGGBRNrj64XrtyBKcKMzncWRoDI0wbv37bzUDmavPyld-fDsUKY2m2loop-6CDzsHQrJRiQqUt80unXVtzgb53MC_NrpSlIKM6T7nbyCWsaVLViHh-73haYSF0ma59aXCn7030CzYrOFwmbBaNsBtoUHJDy1LKsI_55-PGKL_GHhhXaORbt9QKaTnoG16xvxHJV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=U59UD7SmX61cjq75uYZfsIygG5NTUKxVy-YVTu8DWAQFyGVDqhIDemIEf7DrsJOv9uaSl5fEioqrgFAlXLGdvSUYFaULj5FZaS1aAwOPkv95aqNKe7-sG-vXjWGIm2AM9h4KYOVol2BT0ZnmN3zchxPu2608sPy4sazm8AkTHVw4tm29rfrlAlnIKpSNWma4PvpPDMrQ0hUlvQKnLmKE8yzG385rJWR63cKt-kFRcZDjbmcy-pcKiAG6qxFJDvo-YFcqjT90r1Bd5USP-JzhIOQgrr-j5RVIIOHIgVgMxrnyA7P9jI-Yrfk507bNMrOlf4FyUw86TJ43LSds8PK_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=U59UD7SmX61cjq75uYZfsIygG5NTUKxVy-YVTu8DWAQFyGVDqhIDemIEf7DrsJOv9uaSl5fEioqrgFAlXLGdvSUYFaULj5FZaS1aAwOPkv95aqNKe7-sG-vXjWGIm2AM9h4KYOVol2BT0ZnmN3zchxPu2608sPy4sazm8AkTHVw4tm29rfrlAlnIKpSNWma4PvpPDMrQ0hUlvQKnLmKE8yzG385rJWR63cKt-kFRcZDjbmcy-pcKiAG6qxFJDvo-YFcqjT90r1Bd5USP-JzhIOQgrr-j5RVIIOHIgVgMxrnyA7P9jI-Yrfk507bNMrOlf4FyUw86TJ43LSds8PK_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8GhIdMbbiARgIKBDoYYsc687sUG4NZyeubyX9Qa9-o0JyHls9iAZ0oRjzxNV1xwvIncMS805CF-UM3Wj9m1sIDCQQN1GCNIQqJZMGSd2GtZwAp_xz-ym2-_CRPKGp_ILgydqN9NbIoFEnz2PF13zN_eIZyFSAe2C1TQYlI5_xQOPmvQl7n68zcFOjzRazAOfViVNNxE5WmO8lx24UXw5jsGPocuvjuCzsi5mWY6qLDvzq36LsOXVEKFEMk0Vs4PSmfgZ61QsgNCqEar5Ze-y-x4g7IB8CTQiGJPa-9wJx532vy1OUPUoiNOK5w_aT4yIF_42eiKnhCwXKviQqUxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTfcq0VT0Ib-YMbw99z-OnEqcHKjqVyHvJmQ7CRqjDfUfWyou3gajgWLzLxSX0TUSg_3toCifRrFznWC2_EUzjJheA4ECKRqlPSF6IADOTBQuXv2UIw215pNHvwWYRvqMtVC18dljj6gO5fyQM13llpX5VqwXjPbLRuPllFetPnKyGQ2Ug9EmJnvnN5VxpkrVyDOazreGe2npY9h3anoG2jnFsl8Qgg7cHU4whZM35Kn3t_uCPvcQI72M_UmnTWRFOZs0EUZ0M_21GAvVFsh-_otdk7Npvwb7n0V1q0eExFgV6YC8Td5MXa0xM8ohxvCpQlIMWBKh7Hyi_hLDIykUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBIoOjJN0p5upXS2GBCqxs2e5FFqiDMG0peT8SfCLaFUF9vAy9y1pthHROBv-wIaMsamw62GGGJ93H9mlpplg5tSduBcUKhbnuPtiVfsBQxRKvIM8N1au3Ogx7aEz0BkTUFzpuJ_kOiHKWvdfvVtcr2IbbOAIPg1kJ1Bjf58fPSyB4oV81JPZtXi9aIeCeVtEqI9UrGrbKNETYM_ipCGyYHYgHDMH7_hut8BPKvZ5rsOVX-0-I40MJBBLD70VUJc8I_wlPlHfJd0MRKj23jyc7GhkYF9TfDAH5256uwGd3WZHnBfiecz3LivAWxunzBMqxyfItRq6sAmDopsFOYQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd_AFd_R0QYpj5VWiDuVBR1zfOLPodY7M3OHcXbc8dIPONYfa7jcv2drjuqEeCdZoPRsM-UpqwqDHrb33orLuJ1VDMniLMR0J75Q46ZjlipddjFhwX57ZMKWuI8JHhUslyK7Nf-J_Z2ay4RSAHF9fhHtreJ_Zr4qaMF7tm_kEl7oFULDTN5D5WEj8d9iLw7BZKiYo_wYZ8yINE3Fz3QAnrkd_5p42OTFukgHvR9KeJcQSambNQFk7lMtnBnVZ85z-KlINJPJORUpds8Kc7WwceGqSG_WMyTagMTlopMqnuYwaKQ3q14Q0O5bQNR7EerQFJ9hgj7UpxmJoKdDJnDTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVG7bbZLVVcbw0PVkvxmpkyduAocRJsZb_6w1djDY3EgqkXfdTZepCOEAWuw8Cn_BnRIxGZoEIKN8G7W96PA5QwUcAiRzRP5PdM0T1zJx5XYKSX63_ksYh1jLNJz-VXXrCoucCCa9MH6Y7su-lRr_IuvDYYLRw2Alx3QEZdchPpx1LBhxthkgRquCoLnEQnooO0TxOXFUNiUg54qosC_IhyOO7tKr9rAog6awe9h0_zfEo4mgSqOyrnV1TmczzHmGNkRGqJPEZxXQVmy7NjrUlWaJezDfKA2QVOAa10CVuhGKrhqGfgZBj0azDjFPElbx9z4oQt6MliL2eD3PzMRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl5PK9PAi08HjOxtndX56IxdHFGJUGtaiJ1FXzLpffPM4aFsBdM4S_l72uicjr31tyBvjG0Iy7cwzaaS8L5jE9dtwdLgi11fy-6-zlSDmrWH9ffNGcUVHN8KRVrbTe84ShZ6bHkXJHyGeZ-fjaLZFB7zU2z3xlcqZbAcAZwda9kwSo8ek0Nfp2l5L6bmbW-qnyQHMgSweGSsQy7UzSX1er28jrAojT8aUgIMpS843h_fTcCQXswm2D84VmEt4cfQ8oW2pQbQMn7TVnYGaSMRJYP9GBal7boZ7amWcGkQZZNSnNChQbUwakuvAXxr50MyCs3jTYOvHFOiBu64kVgL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVuUrX7kRg1tolqutwDSSi1BqFe1-0zOU36hpJiUVUOsVQ761UHCbbOOx9dx2TWh_CIYPcTvSzzBauddN-4MRkhNsUcSC473bx8JoIDHrjezeQ9WLBjcfrCQseBX8ipOYdcvfmGvL92rHKvdsx718hLufQxYSw2OqtP1g5yhl5Ra-rRWi7w-ac2MdatgZXOXhXRffzTG8p9DqwecxQjhATT1zZXQU28yCc8QiBe-X70syogx2s-AqZLI3evdTWeTffnviIeUkt_EQQv-_KPK_zILl7OjfsyH1c1GoiBQnmwKxLmLZ7GIWxsNhTCRmCOIQID231XGQ9ncPdO4s7d95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a78x88nkTiUqc1F4f2-c-cgAIXsCij9Hc2czELcEde-IeI7fw-_K9YpxHuwAABEXXtlE7ZlNvf51UmOrUUcWeb_RUbwLeQKKeLFEEEJqn-jkn2TJnzgcA7Kt_NQy7_tuC8W_WeAMb7DCBZekZ2UYosnefTtIZqROPmm_FKSRpmTV8bTXqx-NZ-W0d659XYSwwinb7pNVMRvIH_tpSz1bjHhnI0dhnMvRQjbvykLrx4N7_ocdhO00pbv4yu7rP7sgtXIGLa8oL8uHXQaEStqX72GOIPUwhoUYQ-9xNOFn9oxAyfhACHd34QIN7qSIhcebd3TPyODSmkZiUShZwQMBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G58DrD1l3ts6d-GBisu4FSfGrDUOixLzDjnx10dvw4OOPQ0Hr36C7mgHdAl_iSql9QqqxQUreR9q5uWjppdIzMo4yBMrcd1qSu1O-BJOKCqxSpTi9FoDrzkY0mea7uaD4gYAjTCjvK7Zxd5VH-oYJAQNIkqtGANtX0a-4lMbLEHwwl2I7Mbs4smG-iOcvdjckanvuEUX39HFj0Dt7WnYmWNX31clbgEamnP04r7i96sY3q2gqXj9_-MlPGF-RSjz6qgPIjdxpQxvQvCd2NvADLe2S1EFkuKxdZ6YjBuLp1LDTQitShfqHGUJgtdfi4J29c1dTuHq5TBjWRE68F3bhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvT1PLnhCAS7cmaYQD1jYVNOo1LYOlAIIjEbWorpA0J2Jz_DU4K6YcyuChxFwPfwqYe7zTCTZyaFI6oHFCQ2liP5uoeAbvXD9uAPNvrDCjzFrirVI0UAy2LbeyRYmqwoEE1tnvRfL9ZD-Y4DbDsbr96mKJ8SMIoqA81UBMl5krh8OAPYUfX-_4EyUmiO_uw8hXqF6oxdj8w56d1w31a7Iy4qfcwYsy9lINubhLP0V0jYr_7snrgdRg7uslICBHUAHNt1kFBnb6ZC7x2VGTNf5oogYOUCAtsPcbK2Wh8dz2PAuMgKsVBTGkaX5wm1LKiudqLDwnjLRE5PpbZhWX-q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-Rf8v-FPqvolCJF16wL6EMi8flzawvLKUx1H4um6bZ9_aa51KYxal42pPNDZ-DvNvFqFxIAByTFIbnQle_oV8_XEP9y37maQvLhXgb-sxaj9tUK5oRSQImNG098BLHDp__-_L7iYAL_0emO76YTdFOvCSZCqD5hAJZLkX43hkVdG-Xx-OnnCk_3-Z4FsWs-i8pUm9DFJiEJ6JCDZn-UZhmAiFwV02irARffpfAtIiX_OKYA0mQUTRHKMHpT9O2TsxSTdCGhs9nbMg9zY8VJwjD5gr5Fq2ZYQt0ikgwfoufEfKUcTzrYlzEU3KzA2s9gDDNW2bGDe-lLBv_ZEbSEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8C2HdI5DYVnJom0CO_OOzm8z0tGqrhVEE_bmWS_eNGjO1pAjDBt6AUcOYQxMp-Tfo69CMG8GyFICKNza2-if_fXdiBny3CeH9L6WLd_NvVHe1E525U22zItePbsf8qupy3E6k6oGHZLwpiR8w3p9vKU4DGX3RlxUqmjSJRTwN5Wtr-a_uumgTVHcoU67JdX2IXqWX9SxF5_ZNza1FVYXOzW9BE6XgBCYqUVfreHthjh66GRiVhcFR0Td04wIV2-CO0bC6xPWQSyS0wAMKgWpEe3_-4yNtnT17TiydQh28bWa1MXaAoB5Iz40Hywstq_9m7fzHoiJCRP1oBIxdA7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m15zsxgGY6KuLa-v_1bM95xnGpgM0pJhgN4_CZD0aJyvwjF7d3H7cRAPr5O4K0MlDliE99qfIKeVpouwyIYNq-MgXda2A6XoL-sa3azeTkoK5dDYLt1ZqoPlX9-P7kHW1maRJSL-QFKbQMGdWWSL48CfCAOm7FPpiZF23HIIb4jWOaLoEB3qDu3U6KmF4lmWF0Lc3VNuuK-GCyevxmjZCUhs7SRrxgLxbPJWofKsEZqW4GeHb5u8gxg3mFnTiog24_4Ff9LcD3XHjvAY2Lp7uyOmprnCM-dny4pVQXNBmJOVXPf8Qqb8MjG2_kAUzoYH3nCYXlDyIspYV0irFimphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVLhAyQl5P4UEqIp1LDpCrTvQHf4xxWmkNZStef_L3g26dy1WFOukj-brxamOx8CjABu0SOzXsex88Sbfy0NAZUiWAPahAKy8liyllhk_6sUJEDeypby--JZZyAPAyTg7-dJEAAu_T73DNOWIOffflMwYSj44oF3Em9zp_svjKRq2GidDPYYJgDqI9s_xvmYy5OsDHuFcFltIfwogfDI3LENOpbj54Wgvjc1JTuzkNRwdyU3iZkZOJSPSBuuIs1XRha9W7vSRQI5Tbm-Zg2f4IJjHh3ILiCGRuGGCXpHn4vdL0AL8BV-BYfrjzOsoGjUMQdThBeDCLCNkEHnSOoKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6gop7JtUuQAMiRjkxVj2n8tfmYnIHMwRKK5PU792ctCP02xLx646_6oAEmhhe_LXtoHa2NGYKsI3xm9lulJzT0WKaQOMp_jYPLLhH5bRyjPjCwYrJEzMVil8iVgUwjLxzkdaZEjr8KwEmnobX-wvP9to1TcfgfdSo7gczW-i6WtVHIoRmrr4fCLTjroiICSk_1cX5cjBbFN_WBmqev_GYKK3wjjc4ea-GmX0rHQK9bX3VXuv227mIHn_I5VAKetE6074Q2cLZ3-7py121UidGxbpRyNatxlMSHRY9C-WWZrQWyAptx_ZJNZki4Fjrvqo4pgkpL6CSyTX0lhwIrYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=H47ZJuJWkZo4tlc9AZtuxQ7F1lsV7gj_G72qLHrA_kCXX60_rEAEU2d31cSM1unoVVKgBe8Gi6YOia9noJUeBN6SaqtGAx9eNEPDiwDHFf7hobQVlNVBCn3iNzEixx9m5i9aT4ZZY2nJQBnx9fP2Y87q9hRjCg7aQkXwuLEiq3-OV2KioWbcNv_QtabjCSHJF2hSYDZntj7m5kNcayakFHk7YyccdvBm6YaAPrXFalO0J0pmbT7_dLfNGEhIJdKONyvdmAWhmvbIooNWb5dcZqm-GHek55Z7snoQOuN3NI6uYtGe5YXjR2_0gbdl3agd1pKXJTjpEPIatEZ3JXezaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=H47ZJuJWkZo4tlc9AZtuxQ7F1lsV7gj_G72qLHrA_kCXX60_rEAEU2d31cSM1unoVVKgBe8Gi6YOia9noJUeBN6SaqtGAx9eNEPDiwDHFf7hobQVlNVBCn3iNzEixx9m5i9aT4ZZY2nJQBnx9fP2Y87q9hRjCg7aQkXwuLEiq3-OV2KioWbcNv_QtabjCSHJF2hSYDZntj7m5kNcayakFHk7YyccdvBm6YaAPrXFalO0J0pmbT7_dLfNGEhIJdKONyvdmAWhmvbIooNWb5dcZqm-GHek55Z7snoQOuN3NI6uYtGe5YXjR2_0gbdl3agd1pKXJTjpEPIatEZ3JXezaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyYrlLKYsdCI80A0ivLOXudtn4s8g2OGk-b7DntZc3LQwK9yE4_S_8B5uN3V51R3ln0-7843ViBcbvCVqtA8YkyIhZjiNyKJlqf6FCf-Don-zF7CaY6xO3P0svRXdQu77Vzj7W67y3f3Q2BF8egsgSay3f0Xk2niGP_sRrfIqcX_QjQ9sh6M2w7a8jO-DEwOZx0WkgjCd5SF4UmgX3Wce6GWUMWTBfT6ALTpmn5PH-5bxODLE8UweK4BDLeagb1PBoCDs6k7UKDMK8s8rz9XFi_1HLAJW8N6PvYSYK_kea-x0mHZEqb0dviF-GIC-EXJxS7WqVuDE1WX8GXG1t1YSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
