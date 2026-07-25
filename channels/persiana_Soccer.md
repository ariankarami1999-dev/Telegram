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
<p>@persiana_Soccer • 👥 580K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 21:22:00</div>
<hr>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EukDkGr7tbfK1-VCL6vxYOGJOoeJBEGHsJVRiDkLW5bklVblWkH8owbtXQ6cp0_ccxmbBET78bxJhYi40JJysi_r4cJWSwsis86xNS7T2S8BwbQktAKf3d-deZav-FA6WARjAWSLNuex99RXHNnpuCfMPdyxZrkrFP9ExT-WjXmQL5N-YjEzayDJQcghDfUo5xEF4hg5jNgp5moNUkzzGtRP3GGxDHWgFEDogjYhk_8Ybb4KXWSQOK7kBj3DPUhF7lfrA25bho0pyk0SI3w6PsKu0OZO2TDrgD9ebkRxu35zphQfQjt3e_zmCfxlVnh0hQ3HwLJ5kdnbZmgrwTj9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFwcKwFGTQCp2LSjhQt0D3JWW5pWEvyCUjhKSIuOltZ3mIiSH1Ftx-o8rdrXX2Y4DMQo92JHpEwsWsDEdUiAuIS3nPwHXGw5hpx6VugBJ7ERMZnEnJI84uqXH5aLaOOgaEfTZ0e0YNTfWxcr9s4ZZ9TbbhTkWVj0LGgfd9Hdp_NDrkGnUBF2A4QDpyT8b3r2hs3bqoMoPPAfglSNx3z8ijiz1eMT3GXGiGplRURPfRMe-dQTDhlw0NoHxoV8SGDpPYwfUW6HWwyCHC1EiN96O_q5UhNqKMzYRxNIFEyAvksNfCFniYSO3PukojGf9OKpwhoNJMru168dg8OhWprP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-T_0vNK86TO3_2rLIVELHIeYzvtK-EY4ZLSOrKAehD6nxbgsZIXR8SoLMNZnpLS1PIKei1H1whbYje61PTCZr47jQANcsBhhrqV49OpeEUiQE42wH9hZ3T6yKi3m_p4J44exeIImRw5FiThr34Inq45E996bToZOYGfo6r2q6hyZ-CLc_O0QSmFUrO1DAyx6MPSwD_CL8zUAJ2__TosS0y6xWEo94WMV3LCtK3EjdUtmVyUHG9zAosM6vunzNPMD92zzTdGPaiq621SgTScK6GACJJFoeEV0QfD6kxPv93Y29phXx87dbzaj_nhvBEFnb4nkACtziJC5d5zyFcc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc_QEPZ_nx1o7Hf008jIpkPjscTlixOqrCFWVVVtNXhDdE27RtRucj7NX89Wtjx0s7iGj37o18hpWTCffSqpyHyrro0-jlTJO90ow85sHQxvlQM7Lm-h7gx_TvG4Sc8NDIkDqqaM5yuTpXj5D-b0HYxkL4T0fiyRvW4rmAo-cb3WwrsLnnTQr-35E1ofzyRFJ5oSRAB_CZ_PO0An2_8PnGIeO3e5pJHh-4PvnhXonVJnSwQf_9XS-Ao1cJnEwN6mMNHUFJQGnElnMVv3f9ewZ0J4DaRHOEYm9Do2r0gkfc0cEbOQINYyfEJdQ73eqZADXqbBwwqO2VsA37LcyczabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0zQaFziDrxD_YNg6l8Hg4cb7-vXMvH2OW0CRhm6k9zHmjm3VHbRQKeF6GSrWBT6PpcLydfMDEOz17A7ynF8juo80DHb7RUTE65oyaBDJbuYqmbFNK1ctSqORDTXUnwfeoqcEGIgrOK8a3r0dFWJztdE4Tt705P25nCfDPSs9bP3yufAnAfsKOgS5vuTAJhQhGvT7G0KmjTSU1Zn48-fzHmoxovETbPCuv1u4XZGVQexJPNzCBrbw0a9U-qXW3OlmEL7hRETdgWFnPj8LdOWnjqzgQlF6VTdBJ3VHE9lv6YtPHhLiCg_XZ2-1VnciWZlszPZ8rDdw8XrI2SI5tLbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAeVOC9i_zHrjFowWhnMy4CtJWOI_HEahnqzACMoRJOlobryrWpQY1UPdiEWUMYT4RnuD8HJZ5Wm_5ibt9EhXTZJ7gRZgU3H-sP5T_NIrloky5LB-N_qgBWjm78vOwJWd8KPqiGDAzqHfzZzOyTIyVe_bIpacX-ezI-6SbfhfYF0gRRCr3h73eYYMQxuS7KdIbn_64p-Qlgwm8A-kqcGwNKJXbkWKqjowmMsoJRDq7VE2LgdIsY008Jzy-QM75NE8Ya4vTBja1VvUZhluIIYMiPdANw050eD6Q05X-Z5lE6k2nGuF2AdP4fOXjKiXb2mCO1CzAO3Kjy1ob0ZTRRnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SulGdjBtJZGT-dbk2TpKEfARxiY5n_5edD5baP_0KdXpPpkrPy0C7xTyGlbSCB1OfqUjZbedeNXHS6w1LwZe9kWzzII5skV4q4gYukPGjCn6YjsYMP1qC_-n3Zmo6J2Ow6LEVIbNv2BFi__jANBU2LPzNWBD6_SSl1dkpUOLe2PWueXoRwT33Kv2Asgdf8e80e3dpE29MEZJ5b5WecjXECjLiKj3k7VVpvEKdaXMPhbwdxjoQOkWpzAtzgjUHN3cLzfdr15cOF9cKblysws-KJF_oXHL4P_q0gb3NXukt0_M2isyhROdCoQ8CVTEja_QVAg56ApsTNcBBgOqdwpuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO9Zxj2k3c-u9A3MD5o8CW1a_I89bVFDRe0LO3kmO_T2UHbcYCJ14dculspSOtdEpvZuuyrIaiTKpqzNvF9MF5MpXTWyzw0aPpwcBNRrp49uA3HTUwOwiuRFJLdkeBxSAWNNv92QBLZD15hBQFkFyDg7zfPKhtA2mBuLNcT6N1D8W9VZoRxm1V0G7LcbxMSQXzsP26EqVKbthvKW1c8y8bkUzQJGXmYnyifbEwrJ1vIn5QNv7jbDNUZkB8tLoDsimYMTPcfZ5hgbG0KdPz61zXs50u9MFNlAwhTaa0ivrJKEGNyKOixj6jM2QfBtzBBtN6AAUJ8jwhDBKeGRsIXP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1erqe78W6G_ORauvCB4ZcA05hxQCB-MxGvTlXu7ddHa1FnjdoWHkv6MrI0AZMrYJQPqjxRO7kRbwX_7Zr3g6YivNDyoG1mUnUS_Gj2tBvG2V1p48kJ4IWqqj8NjCZSuIrS-8dfHtIPvGjS4WMVT_MeY0snwlcORTXYYGdzA0bDwWSBSoPH6UBLT68fCjkJc6PxTFCfM5rxQI11mMK9GHgfMbiNQrSSLm3oLKjwPulVNuqVZKjVtTaYqEcUiqYCfL8FivSullOegaQDKzSAvQc0ExvT8IIi21vNllo3UfQ8UD0_SE4EppzCa9hfTg3OKV9nJUjUQKNRWho87m39gIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Od7TfafBQCPLRPITJaJVJ7u9S1iTRXUYJFnVP4FNd7HvCC9bGksI-kXEsEdZpqafwe4hrSt22OTwdvFaPoP46xdIGlqanrGmgIYa9wU1f73G4JtTW3o4VNyTvdWj8YI6g3RjzBKpxT_-DQ0I_dffb21PJf0oD0cTwwMzmrgI4iwgpNJoOnqjbCA5bsYoh77j_vzQdzs8tWq2a-nsFLmJJOZKwe5eGNndrRNzFtEms0MxHonZZ177CvWK_RcBV01Ti11HmaZn3O6-QG8J-qaMh6-bc1TPJBjg56oQqInuk8tPmeeL2oo06GzLkcfHP3DOzTf1whswEYeGuxAIBGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFVeChk_tbt1rW1DMKy8DA8-ROGHsfLvfLd1UoKpEoFIuyo8pCJgT5Alg1TPjmp0x48AYMoiRkoMMuWiQ1AUQKchk9p06P1U-jF56FJn63t5j9xug5733vxEF1aAHHttVWcMMPVfKd3fdBmn4_cJzddKW-muzHooCHAVFh5utHhnZmob5A9vP-iBTJz9TtwzmNjp09OyhzMhglXjvsEoqp14i5YFC-Jq1EsbCQ3yEpXcgKLnzimLm2au-qCQ0Eucy_IEICmlb0_RbzrTEwVB693dpTHRVUYevk6pJ-6XTTpjswtZkIohFATHuS8yVCnET_4pkKSyWLVs6QRutAvjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAfoVNjNxP-MWO95EAXRuA74No1AcdWwLTy1IStmC-lUy4514lpuDEBbu8GzY5vSOvwIY-aAwRB6VQueCTwITqcJWpLxuCKC6WQIVzw5sd7tR3tEi3tposNQXcowkX9ceeSew9TkivSbBpF4kt9L1u8Oa4HJuZEOtcRL16xU4_sYHNtZxipLBg1BdfeAmWOPY7lseohkvYUnMycbsqkrS6PbNi44ivs415bMRVSNKu4JoQIgbKWuz6yNqAK7Rpxd9XIPsPD3yYDnjjymusEjLoPBE2iVvXxFvWXadrJPF8anHA8sHPTMAIRBSvK6nBFoWnFYYaNmq7Wf5wSiphvljw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ0mAM34qD0JIZjC9tOfeS20LwlV0qCRHiSmFbPNXIAs5AzZdrlNHoJADHEPKBZkeufEM3-bVPNokQLoUPu64R7jUFAdJmkqSd6b-jSKGOxqAQ8yIEQfEGcD6PsRwOsqIZZ2LjfmLmz_gowrx4ZooEl6tftSgQZVd9l2rZQZAiDFCfPtA0Py5yHDqsBcNAmuuXKc5NAyrAuz2hwzyFoHlj2K_3ZBA91mbvmBZVQtIq9pob81DpJPIFx0M2OFFz_TIJIouUkAPnKvaWRf1u9CKKPD35h6marc_Vx50GL8YOmCm1FV2ZliMxmXdt6r7eN0m8RNRypla4akPDStYcBr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOXLtSgqp4ybD3AV_clKvbcObNgJav8X9Trof0v7_wDrRIdeBpQntfYHLyLkr6g3F-8OEua39YYtH-Pboa8QaT9RGscMJpcgSVhuz8QLB6qpmf8dOEwuP8RbUjPO-pu6hHSOJ4uUwvoiSrgMtnZOz-ZDhAM4aOJsN_cxw8B-aR9Wy6rVwRSxBVMW0wMSfkVkyz83MVMvds89M-nyTtQnwy9gBTI7WasW9t49YnfnwECNQTBhvfMJAipHi7tQaf8g9ibamqY6HJn-VNm3c1oOx45s-HOc6y6qkWO5krALbs6t6-k7mk5KRned-3UcQ9yN4JAuml0bliLaAZnVMHbR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGwPAMJrT6AIQHZgd_0WC4i435eeJGPLoQzkJfO4Nqh83xoKHAl-BdEaU6CTynd6lKbT6dIZtxCCiEss-NHAImhCmT50zBzNeZCvAQAI8kVnJNtXZQg3pJvaRfeUeGkwz0RnUq1z6Ii5YyP10U2HXcejYREuqur1yn510jQXjNrS7weToDODtabNoSxtXK_bEyyYxL1hlW7pV6xeXsvADWjnSNKCD8sdPlu8Sl9FXMx0yxT-ODL35NA1VB49VnghqH43mjOulBAfPQbago7f88F5L-UrbnuL8Ss60gAHukK0jEV3f-mLO231HAZWeqDfNYpKolyrgaoSqUcs3KzJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O73KE9PPDl3Xx3AKvf1oISzfhWL8H-yVAcM_QdH1UDE1WdZ1mPfWl0OGfs6rtoUpBlkIdKq1CrDFzVMdgzArZJoOnPo1BBOU-BC4E77Wvw6FFy02ur58HrREEMkyT-2oF0iN8yLhM1He51xMO0xhbdcS-QCAY97LF_5FBCHMJDyrtKeSG-HgIvDasfO1XqH_UNy_bVV4Oq-e3d-jyp5t6Js6BD3K6gMvsMgb2Pw7VsNhQvIBxUrgDjK-o0qmT9E3VUb25A4Q9KsSW6fGrsNeBrQmYnyN-YjwF9nHWwJzLuM22m4n-XcTnGAaa6y2X0DN3uYVDjcAltJfVLJtP8vymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDLPVC98ZNwTtNXzH75lgVpMy5yX0TwIOaaci856vj5RxxIDVnYiICmsPW_s_NAKOW79YSVCKMHXywYljyKlrzuQCPtUQ96yzVXymwue6zFAIRRHZ-er7VBZU4u1z3gtCVp4sj6IsdJVFtzFdYwJplmc0dQ2kfPDctPqtcb9I6GdK99FYauJp_tQf9vPQ1Vr_8MmsBBmbsyoJBnDBrSvul2dN7PQQk13OOPECmAk1okhB1emFzIgCBydrn-sWTZswolXXKn9lBSHk2cXxOODsUzCmrRBKmrQb7f83HRpHaWtSI9YiY3TVBto3fSXr5kb2D2LlJ-M0XT4-_5JNVwURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=t5GeoDEKaWEZqC6WApn6FQFvLJQRfp0TnfbiSPqZGHcVKE-m00OOtmLiKZFBV4i6H4AwEqoXV4I6-6QQA6hc6723Zunk-ad6CFvn4R0NZkwzkYBydzFCq78GPkEnMg9ApVkuayyoymPJNuqKwvqLEPJyaqzaa3gPD0ogXnvqt9K06U_cwIR5pj0LWjjqplVUFyb-31AurEVzTn-AXQ3JgML3B1qMu9iURtrzpXRXoWo0_m8jtF5WnBhatU-6qKby__zGwMuWLYKEZSFSd0Z5lM_xeLs_IRFQJpd_sKM2Opg1hStDY8SV1loaKMkkFh7r52Bfaip_pUTD7bd2mmvWbCsQh4JGm4FUICoRznMLdj2HsDAC34Ep-AWeF54geb7XvGcA_PSBvzoeYPLu-b23ahg2ZyNuJr3GYpHL6SFXyzjGIzOXVlSNnIsRqAjJa5dwHhkCIPDrfE7MMi-GXbtJLi_LefoIfVU9UmFkkHlyw9O5IVzO3v6xDZhP6oIpvt3ELrD3LOROugih-Fu8ia0ji8kqJooB1B6VdUkQYJAWz90_6z_PtFddtMf407gsigs9br7uRJIuGFgWwlMOckht1-rfw-htdO-oZJ-7pRFcU9GFDRk1ID-RMvCUAPXC-CLcs4dvXbhtWi0v3td3gGGc27yPABCl-qsUNHclkT0NJ_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=t5GeoDEKaWEZqC6WApn6FQFvLJQRfp0TnfbiSPqZGHcVKE-m00OOtmLiKZFBV4i6H4AwEqoXV4I6-6QQA6hc6723Zunk-ad6CFvn4R0NZkwzkYBydzFCq78GPkEnMg9ApVkuayyoymPJNuqKwvqLEPJyaqzaa3gPD0ogXnvqt9K06U_cwIR5pj0LWjjqplVUFyb-31AurEVzTn-AXQ3JgML3B1qMu9iURtrzpXRXoWo0_m8jtF5WnBhatU-6qKby__zGwMuWLYKEZSFSd0Z5lM_xeLs_IRFQJpd_sKM2Opg1hStDY8SV1loaKMkkFh7r52Bfaip_pUTD7bd2mmvWbCsQh4JGm4FUICoRznMLdj2HsDAC34Ep-AWeF54geb7XvGcA_PSBvzoeYPLu-b23ahg2ZyNuJr3GYpHL6SFXyzjGIzOXVlSNnIsRqAjJa5dwHhkCIPDrfE7MMi-GXbtJLi_LefoIfVU9UmFkkHlyw9O5IVzO3v6xDZhP6oIpvt3ELrD3LOROugih-Fu8ia0ji8kqJooB1B6VdUkQYJAWz90_6z_PtFddtMf407gsigs9br7uRJIuGFgWwlMOckht1-rfw-htdO-oZJ-7pRFcU9GFDRk1ID-RMvCUAPXC-CLcs4dvXbhtWi0v3td3gGGc27yPABCl-qsUNHclkT0NJ_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCaudgXtynWKcDVwQO_cIO5I1hjYsD484YXmKZDRpg4OSOARDa306XLo1eW2DHEtiI6TNGfp7ojUbCRDlp788aFNt0OMK-AkLW4ylAkBNraUmPaAcNiF8zPa5qJd2MRFc5QqZwUi-aK2JjuRZUBNDupPVFeloQWskIq_UZMlnVQm4_5nT2O1-3M0xhqxKwdsMZk_Hom8ddtNewPJknLE1ri9tfpddb3jlDEhGWxZ-aRz_Q18L18nWKRzJhpu9PA3_UfkxCEJhTFD7BzXMJDbJIdxEeUrfKwatvqUr7W56w4RdQP66aHH1EmhVNHSzo18Hnti1T9PEJ5CxZ8v-vYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ0FY3qixbHuIk8zG7qDIX7hpuGePGDtLhOlDxfg-WmMkUDQ2TQwH9POWY1A2_N6JEYKN70UU1YhFqWyA-0K2LbBS_XXy52_6m1qJkLFCOnw4kwlKJQLjZVlEtwFalKUL567U6iwqDjcx2NFh5jiSfeCj9_R8672AU5RwNZFKiHPiVL_4D-7wEXkPu92SRJTnUxhTFnAGdEehxtwQysSM9xge54X76bHEp--YdbvBRA_xkU8jcCA_N1OOQW0mpgOJRMdiXqSIvsITAQqTZi4IMRwBHYBpF_BDo5wO3qy1HUutwSmjMJ-5R5Kf9xauPtdj3MJ-rb8wDz_1UAAgnMk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgU1_G0tEKtS-DShsYwQ93UC_MJ7U_B5G5MYpXWH6UaIBhLhCuOqaMNQToswPVVQfajsjLrGsryZRXYNliJ5UBgfe2x7L9N8GtEOlXuXDFyv4tRtlauI44VLhkM4MxT1fNVQwlaXDD0S4fDdclbYFnBfSOZ-Sz4Sdjsndcvp-gjMOcbFDKbDErUbRUyLt9Zz87Oh43ocgHRXmgL6KOGkAd_iOwcgw4zLu5CMdaAJHzL2gL1zUMzzQAy4CsnujAusD37X4nqSwpkfHmzXCIuqC06L2Y6ZFIwu-mRePUxk6Tt8432a2AN6OWM4blwq_eJ5YmD8QZhNtI75F6f5tt_Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE5lyiLGaw9JkLT23ujA5RxNFplBPsPv8khi58Z3rQvWu4sfvejA0ySzIKs7Fe5v--IboWzdF3FKCYAa4Gvywyhn8MtMrg74qJKV12xyLmkpKvD2a3TNNSB4o48rj0Zxyoxk7T_EZIs_nM1oTu0r_6aGEFFXgAFHJgfjbkF48hh1vQiKkH9LrABy9jGkt_1qxI9M_Vsm4snyXV-OiQR6NehfSx4Xgjw0l7VhAXXhLlXYYu2aZqIq--mtO4rzPJf7a6pgHUzlndKzHwBCo4vtkif9hDA8lBCqmHQ3X1-BFNehIaq1lf2UrfM4w67Kf0iJhkHEJviGTCwfaqfAEKGVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8J3A1YhBWUkfbiozQfIawn0eKDUmuwL63vL81jQo_hMQl8_tLPha6mQfq0kp25RBi1synJJw4rjibLzOBjSWLCE6Zp-jUgvRx7i-kmkU8SrsoL-7N4jmSwiWQnY_ydyjT2jVY1z52vIxaltoIyKt76HeUxiPvQbRkbW5ppo5rONKIyUIfAPPKmf11l7h4G0ZHp2fLBO5Vxes-8st5WTEVVhdJrOWeQnQZwYHff83jrOkOJcWSYZ8Qs2Ug3udTfFitsUQq9owkqjBYZAg9l017R1sMFCqnb3Mp1kB_vEl2uJktYGqfePDdEyVk6lOk3uysI7SVGkZz0E7prVMXR_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY61XZuposLo2jNUMaKUuL3tSWFIOs28M-FfInLoUM51tyWo9lT9hPGUFTZwLG_ugnab7mvLotyN5cax6bxusgjrwiR3Ohn-8XMD16tLEeRuETdIddLRHCtSGGhM_A-xu5TtiF3rTMUDlPb0TwVi5gQ14Y5CMarQjmlKSBJ87eHd1SAI_yujMIcy6w-neS8edVi3QGbCm-QncO7BBG-qItmAmy9J0eMY8Wth3WaiJ1QozjcYCkqgVnqWKEuqxbcLJ1Bf7MDXcHcy2qhhL5KTfgJwBLU3-WIMEqPdghlIggUWiJOGrOzL7__-15uFOTqZVrhSUuEMP1iUr_ELEsvwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=qPH3no-3Yo_AWBd0-pihjcgaZEgHrOJ2Nvp7eZa3DJWI_whcfMUZehenIeRv36jaefuIHr4ezQ0u3Wh_CEAgLygilwdjOemQ3HbIPNraVdK_6DTK2Jw5dqT1vR8eX-8w-Gd6OLVDyCCeTO6XFnHZMfe4WsDuQzwETZINURGKqTX2qhQ-DAmT6jL0dupfr1E65qLbdsX8yKzf486WdNbX31P2F-Sy845JLVD5F7LkNPDuUj470tn_bNQfDOkoFLVso1OCRUdxafvP2aJO_NYKxhv8-m5_TqL91Nxo5B66WRsVtSWSobtEFmZi5kGuV2103lmWYdXIcDbt84ePBVSEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=qPH3no-3Yo_AWBd0-pihjcgaZEgHrOJ2Nvp7eZa3DJWI_whcfMUZehenIeRv36jaefuIHr4ezQ0u3Wh_CEAgLygilwdjOemQ3HbIPNraVdK_6DTK2Jw5dqT1vR8eX-8w-Gd6OLVDyCCeTO6XFnHZMfe4WsDuQzwETZINURGKqTX2qhQ-DAmT6jL0dupfr1E65qLbdsX8yKzf486WdNbX31P2F-Sy845JLVD5F7LkNPDuUj470tn_bNQfDOkoFLVso1OCRUdxafvP2aJO_NYKxhv8-m5_TqL91Nxo5B66WRsVtSWSobtEFmZi5kGuV2103lmWYdXIcDbt84ePBVSEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFEm3ryYqKFVU7li25L9z6Ft0QPWAqNcFITOV9J2LwlcuR7t2YQI4OP0Rgyvn0FYY3rTpbbm1O6p-fTlQzABCNzIhdqCqwWQCpGpWLDRTqVmtG6EoUsosYebR0wnswkzxfirva42dpOlGQTxLDivp2eUKN10hiYP311JD16ssvjxZ9cJq-g7ctkhgg3ZEFa7XP4YVV0c_k6cZIjTve3pjVxk1DAUKTYiWVv661ji4_d9TEJfJdKs3CCmB6ThOrbXf9ird-MPJU7vJ0vqMQ_j8U-FNy1QsGkY5ZUTCoPcoIGhfeIH-14rDcpeLKatkJAlg5cMEJaRl0PCMmdZNH8KPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSTchlJUxWdAFL1ntCy-G2Uv0VYGw6XVwnM6q9_4KwaNpzCRTySrBz_F8QixGKwqmfAhXq72N31KD3hoCkGgBvKUl9uIpnfjK4NhB-RJgBXm0S8vh7izxqfs8qQyEQvwhXI_k-5WwICn5wsaMA7_n8qFVFCFsenOCT58rW4wT1seaakG_wPcGg1_I43FJ3QAEvbK-kf79WJ1MoE6jEFlXUqoBjajzauGOeowSeWcoKdNt7qGyCVGREfNWZhMlM6--YEjCtlvyr0uYEslI9Ka0VLyAd3wwIPE5zhBtxbL2VIw2oWisD1BSWFuC8SEqoMu6cLiJ3yMhk21j9kUN86G4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO5lx6uZydpqabzEXAyJ0ou3CWl4DnNQGmQjEVtksHa7RVyBPuRQuu9-tlAKgsIx57BwMb-WvRWMy43dbvzP3aVFQbk4MRLVXB38mN45-kKZ-IHU1K5YvtpUsw8IdWb5MEdsfnTx_o7Kz4lmf7muBDFhAhgRr_cYgF6ZBaQ31JEQ8kcxKnHqdIrtPeQ34kYqbKhznlK5NgRq9jS9GkHS0HLb06rUPSNpy0Fq2Yx-ni1S904MRV1jl4pfy66RFOs3lNgAnngDPPEjZDfTD8WyLL84fYeBPUb3zRKbcG4kapA20ol1gjGYlmCzXxZzKBTu4brODoxH6FQ8YvBsNiaw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxSozE-q21GIgNmTz5gTZZBrkposGEQwSwQ41BE9U1c_1rWtXMiR_Oz0STlUFMFSy7w_F9WwcV2gHIBoVWxGQqR9ce2lNHQg7Xeiygb5aE1Pyqm79zKMGZENh7FBpH0swssZ5aAXEaYSB3Chjbn1U4lUb5liPtqzzscv24Ddfuc2Pf-R4hNRpV91_p47UsjBJPhhbDrIRnNf-df_sn5CfSCNrkuU9FBk_15SNvmjsQ_TlDh288l2bZMNuIsC8YzzNk9pwpOWvyKaKqNFNU-Lfa66h01trAp5n-cO7UL6o_gByScWjVhLgCdmYzdqz6_Lf2isjXQ4QxObBhONvO_xrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvi5al896GloKgLDlyir4QpY7KICJHgM92DumLDFqXoNsF4FywdfyKGYBK8zcuBvhx2c-0ZIvdBKgFtXjQ67dvxSSiq3VH2m8oivyK3GwJaF2DxpzzOAwhxkOKVx_8xVCADryY51Dupl3SL6-bA91Xs5yh59BoQ0PJj9NQ6Tfbbx0nMEsZN9v8bbf_Y-gXK0O1AG4f5c8nrWegvECzAnfnaZfDgZgwNgNvfrIUxC7LWuBQO5fB2cRBDp1DR8R3vUnEDsiyW871ieQpz8pf3gf7t9VMMHHjDhTdBiMYrvTyQfdjNpZZUn_yd1R-CeIO01EEumimLEEduFFl5fw_xNgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDioyJYuPV7iqcDexiEswkEfDGxME3df0_lEf4iYvpBSw1wsdc2B-Xw_9n5P7yEa5D5PHXjJWnhXLqYE55uUdOXpCr2lefmkVkc1ph53zfZJeWON0ugq7xd6reXl4BfGszCKz0CHA8E3DB1asjwknZt1HSFIjXqDIozSjl91dOxbtpNrjtbqvuduAbzK5HtXHhScG2KDjaMEVW6G292Dyw8PJmsg-y9tvRe8nh3_GsaiNyXPzIClMMcuqZeQrIoUgtbQ4af_7PLdMbAYkZjYmbgLOtHeZSx0cRKgeF3t5Zm4SV8xWW1un7SyPCejTW1CcLSjKoEepaCawhg54J7khA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgDjnGUG_l2qk8uRwuuXSpDSZI1n2SpLPoYUeVAnFPR4kYra5Qwm2EuALcZfajdH3sMSlUfdInYu09uCCry0e5EvdxUaW8fywMwNeme1Q6McB4cmTCdEVhIj5M9GcjTewnQzjmsPXEk72pDH6rr6tNPeoet7caeVeyKMw3haWjjZKSMuCCbPLatyyVCL8s7OH_epiyBJoyuO48VtNS9NUzF5IQZcHK98_PvYn-fgqffaqiNqcS-7K7w8umvL7x6BJTUuFbYXEC2Oa2lPeCBmA1Rfplxindt-P6_tr8KeOCatRbpHAF4yp8cGDrrY30lixLx2H3FM7Qtqt0QqXG312Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWZGsBJS-S8iqQk9DnV35YpXVH4eQIB9zD60zC1WiTwy1-QYYk8aqK6E98Z_Z0dDJI3UQqEFaYKpRTKVmBsG2oj91Ie1_Eshoq6xh3u69rg8dn0ZMYEXao32j6X4K4fX64EuVuknPn1QDaW6EvsdhLkIkSSl8SszZtAPx9fc91N_hM0Ol2cKGXlXXbnYTY-c01pWYeVCqFyzmMezJ7e9-ue5pnwUOy0t9nZG4BCeso8GB7E7DLNhQFjjj38vdpu_ofY6LL8p39DryDypj3cAtuSca2Do_iFdp7lG3AZeMpDnZ_qRGl6GSbCZjq2HfrCpxnJcGsxmbYnf3Gl4WN3v_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo1bR8GB_Sz96BE-kKla8wn2FQhJurGDl7ZRlfG90hX7SqpJSrP6Iw26fTKxfzOWnEBoO7LbNlxc4aAQuY3AqYpd5V_DLKG2G20D211TliuEyvb-u_H52fNxXK8WsTrwuaMni007UNmCR8-wPBo--or8OdJOMF869_5nJ2c-7A5MDnbpwen5erBsDf0vfxBln9Jwi9CmGXHAsrwHIcpYkYsUolKdcHnokQrgzHSbxTBN6A6VkAW_X356oq-w1ckTMdQ-LUGjFSpwEkuXoDKcT9ot8_l9FSIwHk4xYSV2t4q7Zo4OSba6uq6XUsqqq_CO_tknfo1wSDnDIL4m0Ivyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVhZHYsZfTVzoJZaSBR4VEc4lNaBvXdW02UP6C20uHAMweCF5bWYGFt_p_Ah2oQkln4TgITWdoECSeJlhT3wPocuKWkrWhdRdoodJ6uP5T1EomaayW7zTuTz-_yuFOte2QWctYP28cN64RqDp0me4F1fc3G_XTGM7uVHisP-dFiJaY0qw6EfI_9XldDdS2JoqwLbtrO6hggS93XFvdfdThSf0xQ6GziDI7hxnYfGiKX5FxWLq66HFoXcdYMJcYJU5Yw8rHxCAFCjlLGsi_MTpW3UKejMnzfj1Y33l8mI_Ti6Wk2ouazoNSUqNBqh5l32jD4dp01TSWb45chnbdBcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=CDtlRmFUZU8UXBe9xxYw05td7G4DakRGQIK-e97c9ZUlkqP5V6VVzA2e1rVZh3J_ZSr-8rGrys7Lx5d5-w5eIsF2D22JELLRSoc6xtGY0gGaY7b5occ92Gw0L663plxAo3PWmi35RpYK2ETbaUjMyuTRdfuaFhalBenfwqkc9EK7eRr2ahtOx_B1wApjnM-O6DuE7MSxFl_Jmm5lrnwRsaFNML14o_hZcNwa-7id9Gu_PkALWMZKmd6i5keHAjI1-NSN8vkQFSJeOHu_HJOdpiHUp5svDudrZYkIGqooGC2eOU3RvufBLXoez_7MzdLzeWXQAklKZ97glzBCmdHKMKB3dtOY8C2nNOLAdjK5FYCCXUDJKbM52FRHPa7QyFlicWcENt7vfSBlKL2cjPR7htE5Y9e_nNGrLgfrGtZ_WdiRRXGxBxMTABxQ1KRlJYJ5PiMNT8A61IFwZmFdi917r0pZAukoNxc7bn9vf2AuRlOj9BtaCs190gcR5336Metfjv90gJSxkwI3dlsj9UNHbyxta2bg1OiHpTjWnISMaX1x1PYYW5DGHMoFNFv_iwAKQxv-Ycp_seqS394zcDK3gxRbMCg8G-nIqVi3ijQcBQA653rtDxPXTQkeoX2ec4dAGmzBIYV7BOag0wErPYJ7MKU7Ho1qFOqSI3N8oIyM6QE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=CDtlRmFUZU8UXBe9xxYw05td7G4DakRGQIK-e97c9ZUlkqP5V6VVzA2e1rVZh3J_ZSr-8rGrys7Lx5d5-w5eIsF2D22JELLRSoc6xtGY0gGaY7b5occ92Gw0L663plxAo3PWmi35RpYK2ETbaUjMyuTRdfuaFhalBenfwqkc9EK7eRr2ahtOx_B1wApjnM-O6DuE7MSxFl_Jmm5lrnwRsaFNML14o_hZcNwa-7id9Gu_PkALWMZKmd6i5keHAjI1-NSN8vkQFSJeOHu_HJOdpiHUp5svDudrZYkIGqooGC2eOU3RvufBLXoez_7MzdLzeWXQAklKZ97glzBCmdHKMKB3dtOY8C2nNOLAdjK5FYCCXUDJKbM52FRHPa7QyFlicWcENt7vfSBlKL2cjPR7htE5Y9e_nNGrLgfrGtZ_WdiRRXGxBxMTABxQ1KRlJYJ5PiMNT8A61IFwZmFdi917r0pZAukoNxc7bn9vf2AuRlOj9BtaCs190gcR5336Metfjv90gJSxkwI3dlsj9UNHbyxta2bg1OiHpTjWnISMaX1x1PYYW5DGHMoFNFv_iwAKQxv-Ycp_seqS394zcDK3gxRbMCg8G-nIqVi3ijQcBQA653rtDxPXTQkeoX2ec4dAGmzBIYV7BOag0wErPYJ7MKU7Ho1qFOqSI3N8oIyM6QE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sok2Q4EZLs3NUSLAJR_YI2XeecprNZjlIP6gyV4FAfEumzXqDCkbbLxQbkow_0mHtKYi39ELsxbJb-chvhLHdGxzji9NpgBCcSRBlMqS_jxb4B1dIDJizFQSgHFZMXE0o1Rujm38fpPVfuXkVcHQ9P47fcKdR7jrN3ONFPayz2fXXMzZhMCrlvxw5pJFHpxxiXLhqEIgaAir56XS0a9KQLLQn4lKVn1WdAsjluyNiI21qIYzZNBz26pjjQWpjnXeRrl62-ZWAb0yqOKSgFQgpKiIOUsZoXxi3YHaLOCbsHxrmlzP5DqQN25_rQTtL5HNKPEvNgaeyRuEYzfCIol9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSWtI-vXB3bYRmjMR6nkIvjV67qftmtgfQnWhBPSl6tBpEiXgFy3WtPChlULdMyzb3U8u3uMjFE8J0D4w9jzbjI_tZL3uzDT8fydtbjdIAo9V4K1D9kieBV8n9ECG863cWRpZ8CHXD1pLv2-glJBnDYuXsr_HuYiVp02HOHviNJVzekYVaAwr9ptfbewVd_PtS4iFY_WEqQ8jQ1rLzY0uIgUNULbaUpQQ34Oigxcz6ieHxULYXSWujEtT91W0lbRVX5NrY7vL00cJ66f3W4lMTWhQRfZTRzCHzuqsNM3RShEejCw2m5TCwdM0X8RYqnHUMo99mBUSTJI7vJ69jeA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyYgUg3kz31QAaFXOTbdX2qql82QJhdXZjHpWxbbJRb_T_woKnmPeWDqoOtUpkgSUiWW9dj6Fc-jlnPW25uHSRb69stAKiI1dhMQFhWxA5CzfImQm_DNIqi0U_QgmPM5wGiCBf2cZ_McqwUAr0l--uaBURIniq3AId5mczhaUYhbHc6ZA5Ug0Yt1QWbX-CmFcaUfZTlHdXyKGdYpLu5iMSUKCw2OtasG1qBfNkRc9nqjZJuN2MwasgTBfhEdXeAx05HIeyArvhEMMDX5LiJHYrRrWFyGWMbm3I4R3uw-45iwNQRgVD_9q3q1iGnrCSMd0TSGXUdpMOOt4nlbkbDLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQbVj6Xh4VCBvPGdHesheqRm73Ik3Hj0Bs2xTJqJgazvhoNt6Kf_tBvqRt9dAe3n6GX9cW-GC5gR_YkEPDurFPCxkWaE-GjQouTLsT80vPmA7ai1e8FB8w1dNAHnDFtF0OGXXRyJSjVc_arMVFxixV_rToDan2lDGEgb53Cz8QneCvzutBnZMCpEdfnj3GEZ5r3S6_ct2Qshghs-PBXpAelYgmWolDwe3anHQ73kbj4HakOHkv_XXJKLyye7ylXtBgkCQOopF2WgYo23xx-skcG52zFQy56X8Z_MiQ1CKXwFDpZU82RiCZD4DZZPU1zDOD-wCeHHB-X492YCe7L1JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv7dNcLW0gFSIyeqYBLVb18GvqP2Yuak5ZXUZMpaVj0qrmvytraO-KW_jwqPb8sX3mXW-A6I8IrWxLsLJnx0aAVELdmaJk0GI0WdguORyKyQrs5Nwc3DM72X7p7fGib-G0sbZcnzxjIkzgXPD-_-pUXvvKS-98kfU-1tvrRvHghaWAlsI3XwfQWhDvXU8vYDvi-E0i6SH4TPJlo-mwdBSWf4v_VNlex2NnSvcgVDH1xNNFh9lbY8OKwtfD3G6FCpCyYvsyT3B6T66ceKcUQRyARrJDkbxGlEQSdyYGnC1cQ75TrfUQIzSWd23YfXM-qhHKLVxFZqPbWh-BGb6gmYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqblARr2ZDkdgcpxwnFo-Jx2ayEyenVaKhVVPOZoPtaojy848fFxCLAcQ23Jh0xax9itzM_iQHx3ixpqgac3K7ZwyS8mtFcprCvHftuFBOILz79vKHz2CIsaRCVaDi7MzT_pjXDa0SRUhX64_0v6nYTK5Ls8dxCujKgkIy_N98Y8blV3OAE3Ag180CaGpNIadmPljqIStt1JerOC1l9VVjg_KHmlvma11oAd6wKLU_ga63uyqekeINMocQ2g4kZevpQsyLesESlUjz_wV3azU7AkqpMM50SSfxjsW0GrHD0xyHQROzqlWi3YxidujvE3OPjBM8iMzT3pntX1s3v2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHDDu9rT7vOyKk0w2ID1AyBz1QY5kGmueysA1o_eD86kE05UvXEYwzrxkoLZCwoBuW_stPvJ2B6zsfnW-BH1zXEMkCGB_7KWY4b-it2_lAIU9IUInHQqcSfWpOLFGj33PxyFjiL0jqxjxPsHMF53Z6s5ec0mhpesqO2b-DqWHlr2vh6Ikh1aPbpG_s_oQ6mvjrpvZQHbkyDNlPlUBdJyXmDFZnd3UYOEWra6d8oH_rOT5r5TmiarclK_K3zRMGeJzp0oXfuzM0iYg7iOZEOxcJvR9RT5wlL5d7kIdah_8TSUv7mqYY5CDrZI1EnBLPPfTZWBSuHH1w3LJwIL84EeVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_K-AQuaD2hNbvJZ-qCIba0_Cmj5i8uNzwn1jo4vmNOuoJ-8cNFTNWg_lesgpjaqTkhv6oreepLS4lMKNjT1xILvGxzwETF22ccETlojDSeYABnVE4y4zAyyXw-HyPS6uKIuaLf2YbptfXItqF_vCdDQxnxjq6r9HriVWhvlWCk91F2oTV0TAk3PNvlVtwCJZ0MZbW0RwfMFFxQcx99CKJhOcCUa_dcFJWxlwkXXltmdMM5-JNWoHW804QMeqaEwzHm_1plmdPeJogb9vnuVgejjvdGaF1vSwKM6tpbr5stdbIfpB9qyq54WwMuVP1DNGKjNa3mq1whgT34PmMxB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLFoXhDMTE9iILpv5yFjzjR_fPbBfVzYLDTUfB2F8fw7I2ahXr7eX4ij4qjSuqt4tV4VuB5c-a6XigDSYC4yj8t7UyWqdL900dMXZ-DP9h5qPgAyMy-jPi43wDLPf1b_R-2h9WDNRCems_g_Cnemw25B5wy3bsDZ8VIMc2-Y4SpA91xPcIZZwfLS0a9De78BRpmGJJeFpTzGmAS7JMCZfRUokuXdWbhfVWxmYH7DPLYmI_Mo_hEUagwnNT1qzA7-O_cUxiLx13iDGLlk9et5b82RnAt1WipoKHXxRwoyDZjAUeC8Tl4ePtI2BuBm7EiRbrq127GIbE-BajzNJYgWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsny3bAzvtCtvBqDRvZDXUTk9NzNnhU7eVv5s5wJidqV9ph5Q14ofKl30N5w3ptBi2zAkn8rpiNfylq4M-l-NyfgCGa6QZwBdiMOJpDn0BjdXCAUXhlljdc092bH3br43_DKc4gQi9ZRRJvi1YdQsnOr2DdWWGj3xsN-l3wtQ30xc3jMwd9Dsrf5SyZGJdc4NN8KZ5lIicnkp0LiWDjVhc_U0zQdrgTtCGVW1QK14IZyH36PAaZgwwNOrc4-vabQU8RUcSib2T0QrZMRd-VsMXggKTwEtxAHyDPaldGaN-3OdZ5KPNVmM8Kjx-wfLW_FYnGJfrJuhHq6fvYGGFiMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrDnfi9dez-UAm9Y7J2JSTT9aN5oiG-jHFUndddX4JQoVw36fQwiknBIpfKx0D3pyNgxM800tN83uCoCZtZpGafckEvuPRMZqYJ6jYRrhSAlD7lOyfCOt0hHhgARgcSif6HBFdhHpMhCCCgGbjWieSrR86ydKdg9GHertVKJV5WxmhG2eJDk5tiq92Ti_i08CXWZYjSdZd8q-l6GxxgcVBaRZoNkpEgTOLrGUhfBHsayXBb4nmAAJHPwIJR_TWM_J3fKaUOSf4sAXPPGN-JbulmJ8TsqjG34HqLmeN79pudTNC1waT86LL9FqkFlfgCkIk9xMDqpUujqwpwSIIrQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPPg9hHpAWuX_RhkG9T-xd7a1-R0rbIzIbnwEgaESKDOgrrZXvLW2NVmEXYy7-k595Ju_c1q-_INSr0ThOU2Zgnp6HBm212P6Z4X4NGLJj-AdcuInr954SbjE19hi5QDHJcfcx_IW9IXUqNRkD_lyhlBI6Glqnav_sLNc9X1AqeNVQJkIUgIDoSQCuEJE1CH3R1MPuCAeCqQ8GmxfWIXxavcZYRD_w9C9V6PqzY8G5KBVXELx-SWcC8KQHdnKiarllIh9V3yQEY564wd55tCcCT7zIM2FEsgUuIK35xKNyAVvbCHoEmwGHn2K-Qu2l56jRj1k-vSazIY7A2CE42yDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2WTf2pE31YAGQKO9NT2DtimGxMbJ9ZE3aMLXzySuwAYpvDh36HfvnRmWeXKbLVJ_31T_1WZH1LH0Bm--K8gMFqKsn9BZzyDrhM5r-pcSbtPC2cccAVrjde72ONTuUkwi2uyMWlVSu89o-SgiNFllvciKHV4zySVI-6i8bpB1lMwPVo8N4GM-qQfqhFtnTstMz333uMoelEUcSi9IIZdVMXI4zWGcCKQf9v2ehJGrZWrSJIRiOzV5aQJAlZrUfJHGGfyLzUNtZL53v0FBAUvuLgcsUsmshZ_ysKMGsu9SFmq-GvrLy3J8jv5w3tDT7UBu1Kbwbuwb9PDsZUw6SDiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ftaa48V1OR6hGrGCacPIL2I4g_XMxc2DcorRb-Vb4jIjZe-_SCMZQUCHqzWmRpchJaQLQoyxAT7Dxm66iDrVvgBHhoQQZrb2z914HF8ncsUduoem99BXB8nhYjnHriPtLDSa8aSWurOxSDaUwytZAxVsr9yLMs4rkUumpW2UUI0tGGUvcjXPSeZby1On66wa4bs_MnXAZ2ifDX5sry1kqhu0Dl4dhMf4GePcEg_Bf7O4mVvayqqcuLwAVmRBFM8_dm_Z6FF8xxHV_tpmJBAX9L7U1eEMPZPdFaTv4wC2yWAIC0zs5HZYdOet2Y8Op-eJ4EmnIalxB743c8c-h5YPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-D93VmkjmcIP1jG9XKxNIZhbDQIGjc7CGTzcPgtYas1akV7qU5snjzycnLoCCAnB5f-IHd6jc9IYxTEFswRARjbNcPFWMZRdbyP7QsAmIvdcAs5udk6CPDmfaMKf_J2hrHXEH-c4qKwCo5_AAQAfSisLT9hsXLDWeWQvvbsyJZcLXk4J9Hs50OW7tdXK-FkrYouBO_P4b-43gI0ac1hRaLqXxGb5NrrXoyp8g86vCZel5GtKF5QUwHMxuXM98WEwufjWUXvsf1FbV1PDuV0tscpuwPLNxX2mmY0JpZEIQMenwY1LL_aIdpol2xwvHJcK092RlMvqZPIeXiBhVn84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4dCyQsCAH-u5GC3EBNv0UB9T2HlJd8Cxl0HII-oEzdwBGKKSJPlOsL00ra9nLLFSxvifBH5xZ9h8JZ_ukZNpQovrLOTphV0fD10WFolqHzIXC5GtlMAiHOkVOvPpQLartcUzeki-QnRG6zeUIspY6hbxRG_BBhGgg6vlLw0_pG3popvpXcllMwR8YK984SxE3Cu8BkeiH4IM9_QkL2JJ5hvKkXbzc2XHUd3FrVXWDKCebP4oVeqXxeYKQwr90vZTTrU8SnJ0WBpviSf3xijTi8vz1USfOXG7ZP1kHnozET32bq6Y4IjxqzQHCruIijZ5V9KcbGRBD_52yVeyQVFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4d96XNdsEZIxB7DmP_rsUMS_1Qv6OIgi-6DGlzMaYGkA0i98ZFC_2Eu2tUQnapoEYI4KjR9-xSlsHDcoPOPRXO_hmI-UoMXXVZ6Vv5v6U2qljA_JmMrxiZTr6b64Z3a_uP-vW0wbDtNmCuzOJxEnnu87EXni0Cmjscky3MCykkaIsgxizUAQRKp_6dpcOctSfGGiaRweDta6YzveyrQjykPo6dIAl3AuFGERSlhPrH1kFAbAkbQ6BM9FQtV7Pq6yhxzWEvUSs7ofEVBDplPncLDuYxbeFfAx0s-ODcexzsbq9s2i5fzvmWjcfervatRn-QF6sXLR5g8NJWXhWeB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GByN2qWH3tNbUUjEBt4HVnRYW-AsXjg4k2kJdaU_fKWWxTPIXMh00rxIfKNGh2l-qfR0QVXTD7_chvRiW_mzapjCzRGyQHH_9qeGyz3wZJ2u-MMnpBoOtqdLz5EYlm47YsqnT1GuWZ3WOMgTw_dahxTDUk71SLdCgtzvgS_Z0dJYtapOotuhDwpN7spTqQW5WX7JcxugXSSNbG9e4ZwQJZSeF3Q2VlpvtCTBnT1N26vom3RjvVpzxFjwbFr_Khi4fwcMLAJB0sLEswN2mir8Op_6mqOeSpyOmpVQki1TZa9EcPmduBIKuElqC03geaQ4lyDlNbtGtEZQ4IGGK5Iacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4qlEmvrwceovYpt5kBL-wCpNGMeN_htbFXojFDhDmAIN3VMLAkQqWjxJbn7IdRrCcfZyVexZCXLw4UUXSuvuuEX4X5Vj1JUaROvBPkuajtBmbi1Q-HnUzcnHytKTShHq2I0nt-Lxbp1jmoM9dujNN1DSOmK4oGVv6Tn_2QFjPtEfP7kjlu0kr9YPhwDnaLCDFm7z93RSLnKctLMEmYefumEaC1524xBEXOi4IjGOxkNo1_Tr0bXiYgYPmyVHz0LMeUTlSAEajWzLNaODWSGIKc0vIE15581_xmNy2XDRK6EC9Whps7SG_T5MAH83nBQVdo_8T0IdLhklzXrQQhEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=Qw9Miu-yp0dR8KIq1U-VmnoWwwZob5ljwoo8UirRxtvuJYFBbKTzHHawhDPr-jSYLKbay1BLjb8-YEfceXQMmRRUWOnbcCSHiJM8JgIIVwZXVbsJbYUOTHnrfNLP8kYDIoBd3QHBh7PbXhUvzlbh5Y3xXcleK0OzpkjyZa-4yEbSfI5zJHNUOB1sWlj1gQIbn0too5cqp7OX1HIKvnwpwRf_4xgTJbYF-k0P03ZT0muBn88o7Hbk9DjVxzAGiVKy8AbEvrsdxAqlvYJopuqjBc7RxOFqjuWGkfySsbXEeotMcBGbE9ZJXu2njNtlu-NZ3NCmBr1-zFSsjlS1uwlRbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=Qw9Miu-yp0dR8KIq1U-VmnoWwwZob5ljwoo8UirRxtvuJYFBbKTzHHawhDPr-jSYLKbay1BLjb8-YEfceXQMmRRUWOnbcCSHiJM8JgIIVwZXVbsJbYUOTHnrfNLP8kYDIoBd3QHBh7PbXhUvzlbh5Y3xXcleK0OzpkjyZa-4yEbSfI5zJHNUOB1sWlj1gQIbn0too5cqp7OX1HIKvnwpwRf_4xgTJbYF-k0P03ZT0muBn88o7Hbk9DjVxzAGiVKy8AbEvrsdxAqlvYJopuqjBc7RxOFqjuWGkfySsbXEeotMcBGbE9ZJXu2njNtlu-NZ3NCmBr1-zFSsjlS1uwlRbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VruS1j9rjGcaRnlyVsOcZshsqmMwGTfN6-QN9Kewy1YfnDitU3R0nNSlbNs7Rgq0n35RZcCMUrrKN-PKNPddjq406h-aqNnLPZOElqwhSv9HSJqFkAa8-6JZVlZhW_mAyA8HeextnuzlPVZv6NRl90XysflYZGA2fll5jAKEsFHWjFUdvu-nwpzQH3uza8sefwoKvqA31a78L1Jt_sYwTbb96FBVvaDkV91gABehypIpbWi0xwjNJq8gWAz0fUsC6bKMDjuRyl1P_BAlQo9ou14RbZhcgUiudU0jOs3R6ApzNtRnAgDMtfI8ay6wC_4GDuKpA_b_KQLcwQd1jSQrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPqSBvZthKYq7xbhAKrjtPgIQUp90TCCC3ESFRnqZXMEFDJO46hkVqTRArvX0rhZVgTbkAhUotsTNfY-K2LUVYyRBsxdc2pxSrMUlIj-mf3fRMZM0BFbxvvGHjmq2q7o1wEGo_9KfnavauUfKm0UkCVwSxd1o4_yA_QreQGXTcmApDdkhitHDtn8onVqS1Tuko8g6XTkJ59I5iR3Hc4CZaH5JhnyDCxExGN5uCQJbJj4ueLRWpMTxErrsc9ZeWyVQSIQ8osyVVZFRQBrAUMY2VidoXVKchDbzXDI3Vw1RpbQIGkQBYvX2N8lKBWe0ningplJt-Xs5kZzYbUERNZshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0kk7SPqo6DGgTg6QZJsLDj0anHT_gck3nGqDn4qotkLZq1YI9_R-2OHDbkis1dYi-z_NOgk4XIL0Ja_heltkhTq8CfGAJhLSBSDx59Pt3vvlmulTcUeYCm9YU21fhXOPtxPS7TBaNs6MaOvIG7j312fv9mn8B6do6VLTDyDvdn9wDHXueXeWRXmwrzT6eTNh9sY3b22WoFtRT2FxugvCv5EySfvT_PwHkLLk97sDz4B8XIwyCynwFBye2SggoW8yuD5ixba_i03dyNqyvbizNMUd5DH_7MXwC6_xSN-_XT8x2zqFGJh-3Y_QFm6GrPMMjJo5tjmos0w5GLHhO8IZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7Tj4FKyne3l3c0rAnSz8iycMe2U3A1mfDhq1pH8i58QUKKUbyIX-34I7ed86wqYoE7Z8ktg_FFonImajXDurBcVmY0rRQ7fAqD7k7L9V8yb9ne6vw8IC-I4sgJpXQpmz55rZL3XEZFIOTWv8kqDT8gAl3HTUyEjGU75ajV6Pbi_5eT9-6MNmppXG2kaQ6jywRYPIGl-LU7YyulsOyWpurSpOT_TMXk9Ow3TAViXMIxqJoz1q1fQI3nXZxRRWjDTqxlClpcG0PNYbs_1LKlOTSySN04JkJu3syrTgTz-kA0mu9s6YOWKGH40GKzyg8nhxhOewnWsVOSaRVj5iv_jZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=flzxl7VqCNU84D3e667bnbVPQ_oNgkF5rw3OcMb-DaV77MwosmV2aD9h7u2DZ00WDU5TvCTa3q1kP9A5qyqrJQykz9toA_dxCe9oF9MgTxJYzff8fAV4elHyyT24AJf560vXmj8nKqZdjcS4-wfbzsVmdP_NMeZNYr25R423qPxK4q-5O8C6eq5sqnHuDwBFvfiKkLdEG1wHCJMGun5aiP6sPPcbsfHlJGEhWtZnR2bBmf3_c1VK-2NRFUTARmxuJThEanbqOmrBx6VV1L1rejJj88aYk1703vLeSkjBAn6AxrdR2sITzGUok0_dA3qRiy8jJ9ZiTcp_jlI6GCdbODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=flzxl7VqCNU84D3e667bnbVPQ_oNgkF5rw3OcMb-DaV77MwosmV2aD9h7u2DZ00WDU5TvCTa3q1kP9A5qyqrJQykz9toA_dxCe9oF9MgTxJYzff8fAV4elHyyT24AJf560vXmj8nKqZdjcS4-wfbzsVmdP_NMeZNYr25R423qPxK4q-5O8C6eq5sqnHuDwBFvfiKkLdEG1wHCJMGun5aiP6sPPcbsfHlJGEhWtZnR2bBmf3_c1VK-2NRFUTARmxuJThEanbqOmrBx6VV1L1rejJj88aYk1703vLeSkjBAn6AxrdR2sITzGUok0_dA3qRiy8jJ9ZiTcp_jlI6GCdbODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3govbgGy_a__f2ZSWSTf6Qgmz_jNlrIWCh6sViT1ThDZ2367Fm11joaPtmWs9tKQ3FQwVDmrHehymT9hFnpiE9fAf7dp-z8Mrsprk8qJ0lODAVftHylDvFEzxivvcmml-yeLqYwJiNiowiAug6w_4DFWDMyV6e17t3O9p57aIXIhnKDcXNooE8-kV-4IMG2yiT_NOw8Flyzd6oYLRzVvnA1Tiy0wat4Go0vJWMbTUr7w6cQnoETKexBhtMpFWE6-1QqyWXjPRtIJ20zUF8MY-c7yRL9rKh7rJ_QCBmUCpzTwDJ_Zz4mB6bBSdbvpifNRexOWZOAh3ZpuZYQqVGk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r31PtAQ8nAs_eSm0GYdXdeaGtYpQpZzGRJlXadZsLJIU7oV3hdrsqjkFTYDUsaS5oux6HoJGfE8IDp_nuMQfIekn2hh0Yk6BqTnnAVEvzeXRiYt0YKD7EQMgFgSiwxKARkb7yuV7n78ronBxIgf0rhfhJyQRxPHpg3GGdnhowc86AJ9E0fVqcFtHYnKtfapJ-8vESYbYzg_cLlVXqdgnkq6WI7Jr1KYyGKMTA_j6FiXloiCOasgsdqspLczH06u9HkGiyF2lfDfff6U5SjfKBn2k3eq5-Ng7qOQJ901nFoLmQUsaryfv8CNa9mZkASSDTWL5Yh2gY_0mDBsNza25RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw2rayoEh3yTOPAlVidjIJS2TQeL7QIjusbuhoutkuPp2s6b9RKbc60EwqHwB6uSkL5TaP4h1acMA_asEuoHR9nRaNKjt8sa9TIcA5k36daqBRgEfZ6cCOLgC-5bApQvQ_vnx7lPyA2dFHCpTlyfKNmM-zS_rOg1A0kxzt3tySe6D26ORBqVQV0YNHBDGylDlzg4aO0h7kZthdhvhNAuZVKlFnHp6KCk0SL2iO7pOAeU5pddlYzkpcrpZss21GdqW4xVPbUHQPYh6qwjSYXbZgdNw8WKZDaBRikmF9TRFkoJ9ixMQwTuhQKj6HvzV_g6eWVNO_VIUFKcSc99l2_XqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXbjNTwYK18bragruleFLtZlfyPCyeeAxANCSu8R4aytI2RknEg53or9d8MsjmScNQ7o2y7Uh62veRZoUm8Eiy8Qe0HmsbkM9jFdfr0Zhivhi_M1nTkrx_Xl3LJ2rSi8CvFhYXAK405d6HatxRbG6sn3clYCfQsYl3ptoDqXf4mf3AmG5qvK3rmjM0sZsgj9o_5CFb9YHbEN-dX829fQZxQSdoAwG-Ed6vE0zGV37sYgLj5Aql882GFJN4nYgMgkiulZzQDZ7JGTBWULDRrLne9BoLrMbyXNnXiAtlY-q75VunkWAjyfpcvAyI9H5W_MpNqP0AtYIPZNP0hSJMG01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6CmAPEZpl0c0iBzm1aNBCYdMahkrYJg2cUty-bsUTDPQhYavV_I96z7ckqL_bl3756gxDc95zyuksLFyw8vCKQqmLSB3-ekHjU2yjXvi8fJtK8etNIV7UD82bx0Qfc7Ac6NUP5BWlpIavx91PJ0tnUAFAKyOXC5BphMoUETlHilcmnmBCnfruNqEwB8lSygwg8W1e8Or2nK1uvqy1_DcgEscCXzyZLyWqs0VXuE-JHwT1LtdB8E4n4ftavJYylB_G0dLNoVbagVmV9osr96whOWgXGA-CGzpSdAgX_jMi-s6FZd4fNMM8ml1MULVxPjVF7u1JZRUTv8xwJQVKOcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhGMpTeMvm16gZ_UmSR4o--3ix8VlV-aKhdaQ5uP6kYUXy2kG0dix6Az56cqZY7jv2o_aU0_jVzJN8QA7CQ4QinI4yiQIKmZB5BdMN-Sg1cy-3CeYBvE0cGPduGLULlxkHV060c5Y4eVJygW6LM9M8orDUpYczOKppnhnTKPblGXC7z1H-sOgyqc5GxWUltMHDRFM5alAubZZJa6hAwf_CH19u81F2awn73AIMAivA7FS6Y9KfS_FLZOBHDvdYnkKNkOJPF9TD8YrpSZS939LSMKwA1EnpmVk0bymPy0jE51WS5QprP5r9Vo-ZeZe6mtWq_O-S7IGx5P_khHJqXXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJl5LJzRuhWboiFlvXTabguE5KTnn5qPazQnx0gwzbOVOe1pEdvv7Mhj5qPjsWtL6bdSDTerSv4adM6XFR3XCvRJoXbuB1ilBh78zcdy5IIdf90R5k0uQXsO3XfanNSUz4HLcmLnh2hwfocHrab7Z0TAYazWfdRK9r-vArZsRCQ31oZtqbeRG_ADsRbauHL1prU7oJuz8AT3R6WqM77e3a_yvI6D5sYrySmnwxFtgxn3BNaZzGABzXrKy5uN6734K2fSb481IeqdAW1bXB_h2eIJ7UEwL2bTQSY9pbNKjk7mz1UGGfbUm_xebaQSs8aP-uQBDbIoNJuQPTaQjum5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2r47OIpjhNxTv0ArkuLDdZkbXQitAGM1Tptzr0TgSTRI03MschN1bB8VZjP2jyajVULS77ricwNsOSF_YKIciYGgiRfskLOtlsbFPRp502j-PIRIUY5vYQoEmdUOC0HNl9MRxo2aQaGcaR8wsAOX-tfbolTv8fvdefkpOvMh13Ckjr4C3sPeLLYHYbBZAmBcw0mKUFwo7hDdbQrztuSGRBt3dXKDTWlWeLyKVqQ4avw7i9odP74JNJOStl_0sW9AzaO5BzdjO2PRsjYAi7MCdjrsGf-60roVfII-AddCK7d1kzS7n-kUXDQRIk5pXQNTWVWl26J52_AblsSzpi1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUP1EMvkrpWuGFrnvzzU5xtxjuEmm-3MWEF75qFJ-V6BzNJHLkCWXbDfUdkZFGZZwjGWGjAvfceSq1r6Cam9u3dvbLrdUZbSC5ZKdTzcA82qfrRcU81jhqoEiu_MS7d8XgZ06yy2bMTCA_RgmGqeHKkI08zAH3uQ7_AyDmw8z-E-qJcGKQEtKv0CituDS5-oZ_WF8IOPNk8MC5Or8nAQd0KS8Cxa_Lk056YnMtbbVb1toPq9e-HEKLYBRu9QeHYdVU_-NEMTlBRp6MLUPQiSl7nK7PbkKKx14nAJfloULq6GQs3c0WakF0ubLBlJWdAz4EjL-i_PAeToFmhuaFDPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMtPI3j51u9Q5d-EpNPsXIwqp_kFg8RWLRxJJwHzzqZp9vqftzuGK4kTp-9hpaTFpCcy7IuJWa7EWW741V8J2OA4zp8FngIQnCodtf5sanq1NPw_k5EM24jnXD3kI3dR4r7pStRTn375e3tXcPchLe4PhE8Tt9U6uFR_cLv6WaBKVEjunzWih2Ux7qoCkxp2eKtTHbZNHX9oFqp0kZSYHXwYKkaZ32d_mF1tLO2N8-T4k5epLgnMOSI-zIQHijlQ1fz9LM4YQ3wktLv6bJjlG3iAN_ofIswGJsNkwsYOBpTOEuVjeXvR-N3KgbL9WDerDt0oitmPbKsA_VaDY0WiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=HczljHiHcPKIUrX9ndPXnSCyaUBYU-NQ1LZv_4ngZZ9_F4AyCPlLX_yEz9UCNGo8BK1RSec8DU9uGIrkMCELLKVI2MAfJ-o3Min4OnHlQvkCSBBpZJzCbdRJU9OGXbkJqO1ptGP-Kkuu-uqGU0ZzBYHJl1hb6yNHoYuOMygVnhk7pgM8-xMeKydBHlsCKrwucrMWmmN3NmsFr5_rpVoZNG4rKmzeNjll8vorPrbrcskIgrY1xuJSCrRgrnG-sRV4W_2pr8xhUEqBPAbubwBe-cyuByENhdQCXJSFMQFMKIKshwMg2v5Vt_aMSM8bnvBNPjTmXPrJzwRtXAbs9zIkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=HczljHiHcPKIUrX9ndPXnSCyaUBYU-NQ1LZv_4ngZZ9_F4AyCPlLX_yEz9UCNGo8BK1RSec8DU9uGIrkMCELLKVI2MAfJ-o3Min4OnHlQvkCSBBpZJzCbdRJU9OGXbkJqO1ptGP-Kkuu-uqGU0ZzBYHJl1hb6yNHoYuOMygVnhk7pgM8-xMeKydBHlsCKrwucrMWmmN3NmsFr5_rpVoZNG4rKmzeNjll8vorPrbrcskIgrY1xuJSCrRgrnG-sRV4W_2pr8xhUEqBPAbubwBe-cyuByENhdQCXJSFMQFMKIKshwMg2v5Vt_aMSM8bnvBNPjTmXPrJzwRtXAbs9zIkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlgJg-yPZC9PT_-LgysEH1C4MRaO9gnfb-hdCxOae9nmdVUKw-6WqoN80tU5rPXblczr2wkXeII1aLb00GNqkMLQbblYX5Okf4RndCE6KZnlAexNS9Ecnxd0ViSN_x96IBjHdN2cFmsmuxirHYLdwhgKlwEhxaYrBZzcv7zQFuk0iNI1FwqHKKlgkJZvjRd5mQto07740q-HCxV7YZXhcV8GQpLX-sXkrIXUHtZggF80a4l0GMA1vTPXflWBZdz4Wt5wdBJiW644HZ6wuJ-ZQ_tDmjK2h-gqLAJQojVVlk-Zy9us2t-OvwBhUnegyo5D_UrwfAe7xHhUFUMLtkjXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA3QK3aO2ASzqilY4NcTdCihi176mPkkEC0ahfZXnEymAlrtdGpgnH2xzMeXMEO5aOfTWBoJSNJ48gNg0Vfs12D5k0UluW-18k0k4HqfyvVIRO6EJLOEIDOjROpqzsjAZW5ady_MDP2nOcR52QVbPmGimD8uhGf5BGSxrWOQXYQpo7MeNhAgXdZWvQtxvRxxbsPqrr93iaiLJDzdexi0dFAbVCBR6KeG-ukutSEjQqZLVGmhzjXyfSjaMH1ICWbWr3BtFTRnlYsIG2mLlreZoty93WPnMS51nufg1RTfXAuxVJE_v0jkkm3AeEKE1YFaMaQZuzIvnJyCivs-nbKiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unokWyH-5J95Vs1rAP2stevUOyqNAfl7g-AWLwZnl3eZyl0uH9MFJ6Z4mlH8F-jUOi5zETfWLA5XvLUL69Di5LPraKeWGvJOeQN58ipmLRRN3l82QlgImNehbYNntNPURpjYBJG4QgaUfAh5NQH6KqCMr3tqT1_mF93GllizX9mZ97TOrSVsHd8-RXngQgf34xvvpub4JwOasCNO2ddVl8pf-2-1GmXfePgobCF5mOc0ggvVAe56dq9Fo4IIGLWgiqM4w183aGG8dgFU7ONKB6nZill08rLRrdeDLBWzfgLZj9GmCk0Ep1vRBbwlGDVDR9wo_krPrTqemfDZ4Lzs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVWQjBzNwCP-cCXa9zA7ic4U9B0nuWv6J2pAzn0BHApy6J641aVdJr7vrHHnM8hFrvmVqDlfiYJenrY1L0h6ajl4v3F_YMSdGpzvKhnPF6g1YNub4xfFUH815XMLidxvwmCc2crP18YfIKMP3FJjsrIiUaoj4dIdIoSWxSRv2z6zr9Yg9hHI7hPnnV9kev2UmliKUNa9MgjDEzDuKVBqewMljM4BagWQb8H2l8oDUiV_jV93nMsMdTSQ1tfh2w24Rx57sTQxxojxWSwANyY_xrksrYYeZ-8GSpn6FjMx59bMGlLpJptFJ-QUlaQyv6rZiwMwGpADIKGXRt777eTO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVG7bbZLVVcbw0PVkvxmpkyduAocRJsZb_6w1djDY3EgqkXfdTZepCOEAWuw8Cn_BnRIxGZoEIKN8G7W96PA5QwUcAiRzRP5PdM0T1zJx5XYKSX63_ksYh1jLNJz-VXXrCoucCCa9MH6Y7su-lRr_IuvDYYLRw2Alx3QEZdchPpx1LBhxthkgRquCoLnEQnooO0TxOXFUNiUg54qosC_IhyOO7tKr9rAog6awe9h0_zfEo4mgSqOyrnV1TmczzHmGNkRGqJPEZxXQVmy7NjrUlWaJezDfKA2QVOAa10CVuhGKrhqGfgZBj0azDjFPElbx9z4oQt6MliL2eD3PzMRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou3Rx1bgL-4Anm8iA8N6uoULAlGIv9pwILkmgIsr3nppHJMFjEYaXarO9BJ_UyFSU_HmaqiOYRTPjZba1iJk8WBsXTmZ-QwXYkzyy3g9g4fXN35-KenkVXPSCBBv8PBN7rXRdeSLjVe2jDGUMQffF2HzZZSsLqAhOGDeNmiCc8RyLxVyKufUsAvT2EmdIyHdbt_0MCsfH3RhX3gAdoc1rYbcLfbT2khY9VxFoyuEx9HnlRb8BxRLqqsrDqJmJM0PYyB4wrBv3Fy0A93co_46DuDsMOK7QgLuR_eYs1sCWbn42vrPaF-aDNyHBTOFAdNRrvxXqzHkHmIoWT3ptCLdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG_-zyqoai6_mj-3vaQCDOreePsYMfOkuT7vanP9vedW8AEnpMQCYmwKw8U7EEXOtH_JwJ8PZoDQlOuf_yEE4X03ew0-7OhveFoAa_KD97-qi5mZJpjyXLvVxW6YaVOGVDJrdQrofD7WZtjqJGKo62AGt-txA6U6WNb_V2kFKZZkd9J1Yyeiut64qzIwbwC9VOS4mWKjP2p3mU40z9V7BNx6XvJjXevpnbZQmEdW3o7ikA0obu5tXKd68DP4zOcG1nWb6QXV587gVSgZegPTStzqJlnvuvHL3YQ6HFtX0sxmJiWEnoB3B4sV0Rjsk6GieVRUW0YIca66PM2DNcUa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxeayxXb0eWE7ymkBGQCd-3r9_SSnQShYxtk4zosGQfbE92BTTYZVHxhcdkIsBnhwyXlhkSXriFtmCw04OZFVQloj96A8sYp9Z_XOqQ7nCRmQm3FowXxgaxdja5Uw1qY0dk-RSu7_eVfnBry-OM2kJztgxc61Lx_odwXqP4cyMWw40M4ezXA3yPYak9zhwHBsNs0fqPmZzSQl3qjck1dfCAH8U0jA2otbXQxxEzKg_R05JWJq18SCjs7aWh7zpx3742RlDpbIHHq99wWFcDKh9YrLvzORPtW-tdayURKYX7HofNu9W2oml556OoccutfzRZTc484qlm9IcFZXSmBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS3_jyK_HJV-PepsLh11olslDImVDKuHMki2Lr-aENUVfhDiQhJyJy_dF86iU55PIjNV-EBdJC9TLjHMJpdrDwmzIOnpPhbpyp9k6K-uYyJCgoseAKbbr6nVQp07X1bU1pnapmbNxMGn68eLt7ly0snkrIGcxFi1VSnbaD6rvfG-aeP7HuTTcGRQyDUfnOwr6Cs8BWL0gC9nvy0plPaU1tIercYGYRqmYsHTQC0duDqhqCAd8Gyt2ZCbJj6r46Q46nBLZpF5beWSXxdCcjG-qpMndpef_beE4bTtiMk2eCFDwf3AEzLduy-hbc7LCK4ou0DXSXvYwhouK_8OUyukNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXQuDDufds8JJgmZp9P2QplZLNLZLf7c2cd_MBXVnBqgASFr__SBLrD49K6FfGUz4bc6mTxsphnsqLCHW43XVA7O0yzKlI3gW9qlGxH2c1qzD-j3bXzjHypMVpcpHNbkuxxqYUlXhZTI3y4vY3TqigE49KS3spfflNPQRC3Nb41Nn0a1n39tdvum98na3SSwX1u4nNIHQCw5LkD_gwDoXSC_X_kCmVWSAnQUZUFjfPTjuve2XHA7kiBFiAcTE01KBjvE7FrsdJlFH3deXm_VtUmHRGW0n6EtXHQ1J4I_Y4VJlZujVeaQjy2nTO2bIhTkufihIkG7k7Vo75Y2N1vWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD9wzmqE9kZRYTsg4XanbP5VwJfnlD4K3Rv0_D_yF3rUIFZALPYr1HVTY4_3rAuImvjadILPL4zKFtWjt8WYlYSgiwNY3elcvJB3TXiBYYJbHetjcAC0ctBm4HWy4gpStJq5drEaVldT-cdZOKX9IEmUbN1fz81ixmWBC1Sa1O1OCXLheZcFKgso_-I574mn6k5wMj5pRibSEzdwtdbR9MHQ6oRsr8ePMdgUQ5qjbYvDPjYNwMY8qH14r6y0NjJ-QxP-_8wTQS7myO9EI0O_EmWC2IitL-OapQgS5bd5mja8-XuFSCkcerXhxD_EVyEWioStOEBi47SUbqjmVxEkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihEH-rSznH0rFeh49RAU4cPUjkKuYynvftxP5FMbDZwQtIQg69TEee2GRw_xKf_CB7-48RHlSVGcNBWAynlyGFWWPe00IKx5hXgfIBq3tZRxFdmymRIPL7eaywyBwdx7KCOTn1y4JwHRS9VXst6enJhQOJ73pLXzDgdwZF4yFuh-esXqUJwrXUEFwM2aJknr81zGI1GfUR_6WBEaSr5u6xex61g8OF_1dUQ_qHpXYsN8usnFPM43gKriHVoyFLaWNWNcyByD2ZS1x00E1BiKx4QXQ-sfcMpXqKPcUjStyabff-6JnOZHevShtbxj8S7p1EJCGFRovPESttZc0vzX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkljRUzb1WaLnge7tvJx6R0V4w5fahmmPpz-y4-5bhPnXbdDVoT0sse6taTYzMhAodMDz-l5x6ONJsVv3_6cMlugv2CzisjjO-aQ8S63aNKHna5VDD0Tc-Q0xuDwfqXSFpzjOw7PafOxoTry2cuPy_xYuX--2ovvEBnztgqJUeTAmAB6CjEXoFUuJbwrySrJo0wRzWu8zgS4iTDbYQ5LW0U3cal1QplGNmxPUGqdBod6cLy50ckXg1qiR6d5gCWUCt4YyWR-I5V8wDXXEdt8bRsYX2t5yoEsKjsBCPFXzn-m4NOU-nnt20QM0L-A_t-Ivr72tZL48Q6O5jG_J1s5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0Dpl0Zw9TrD2tgSDFq6kiG3syrcpqJlZiniNHX98qseS5JdDoqVAtFrHBOVBtjvg3LD8bOU5XwRurbqM0Nfx2LzoJoS_VTxoioqCb8QUjZGPYsUgYWdkEuqzZViqW50I46SITRe1ISLzs6THQrRXhrTino-jd2Uzkd-1XJFmC8I-tSn0MOvenx68KS5lV2GRhho6HFDm_cbNeyfguSOy2j-daiZOZsJXQvSLxuzwqNK3cdyu0gDjtFLIfTk6H0JbBjh6yrg9XKt5xLNouzYWwIfEliP5uOyDC8GHj5RZdEX_DunWLbReehCIztbJf7XQsu8fT5jJ2VyhNxGm5h67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi6MjkVPJUkVOj07bdhEnG2_ShC2tOFvlfnZG2Rjo18q76taQUaolJ9GbTsrGnVUKIM3NKBAsqzOo6LqZycP5kbzQeQlKeWKSVYe-7mYP452AXDfMgz82fpYiS89ru00GKT-fF6zTZ3xSmdwyzHwNOY4C9deMnun7f91bIpyOSdAga6gjWkRvjvLgxiGuDRdK1J1pWiEiR3emWtq1i1dvDH4en0NpP9PgjnCzL1o7i5B7N1FTNQtOVvHGplqTFsRnOYibxEvKhuLgmVe6u9biefBDAxeQEQDWT-LnZNVSfQrHQSRLOJkzFab6oRuUb4kTMVz06NStVreyEZmS89wUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ES6zpREwfkn1isKFtfdKSHTcpPN832_o5HTiPasPPjGldrHzzgWZhfNugbWo4qWOYXzB_yRaqqLszCbhwr34kFTgb6mbPxBwWHVt5oSMclCAr4Ycd6Dw6DhmvwmI-rfnQNPHKHBCWKMReX95fOpZD2-gdDlxFxE6T9jdjHusv1MNWJFzpBj8FikSaCpAbsiZozAbWl0wf4Og0C6sOCbOMNkPj-OsrZVncApqQEeD7WnDVvhesF3tb1yaKDSHt6bgu7ycZa0lODgQlAMh7PaoJsSSlY8xSRzGQHLYOvdNmPZhdJMKoMQXELrqxZmP5TWn5SSJWa75esdy3Ak-QGTtgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ES6zpREwfkn1isKFtfdKSHTcpPN832_o5HTiPasPPjGldrHzzgWZhfNugbWo4qWOYXzB_yRaqqLszCbhwr34kFTgb6mbPxBwWHVt5oSMclCAr4Ycd6Dw6DhmvwmI-rfnQNPHKHBCWKMReX95fOpZD2-gdDlxFxE6T9jdjHusv1MNWJFzpBj8FikSaCpAbsiZozAbWl0wf4Og0C6sOCbOMNkPj-OsrZVncApqQEeD7WnDVvhesF3tb1yaKDSHt6bgu7ycZa0lODgQlAMh7PaoJsSSlY8xSRzGQHLYOvdNmPZhdJMKoMQXELrqxZmP5TWn5SSJWa75esdy3Ak-QGTtgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TijHa7O4AMSf31ZMj66j4fvq_ek9ER-wMDwdcTzk2gKot1Mvc6SzhJPgAlZaUj8ReE6Ww-RQ9zUDYzO5dBAZ0R02xO3tJ89rPxDjRpXQzrg1Ygj4g844rbUgUhlWIiP2uAOwnP0yPScdxlqlXwFoZUqSHntzTs_Gxo9fLVhfcWOYhTRqdqjnXwle4d1r7njNOv4rO67Gd_7wvS9TAp162BWq_A_0irIJ4ol95g9I_ETh8WjK2MjcUG5IdjJGfUPCNUUY5UQBu4npLsUxjQDbC6X7irgueWTla-g8toXpkFBS6KzZ0PuR2PYCLHLW0CdJnV3IX0CHrLHgc9cvAI1jCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNCil89wI1e1FajIw_-LnIzFdFnLmuS5CRDwalqdn5hNlYGpshVh3umQkW1xK6eEGmXafSzMOfJyJ6DvGd-XNEqJ1Yd0fgyn1SY7MIjJiJw3oi4UbEBCab9Djrrkd6gbBxuIJLl8ImO_Ma3pDeDUgVfOkfk7Mx250-0P2caPeTl9GQbfmgMCfQonls2vLTf0j-ndOBcTarIghofbzDw_WSMNwexdHlizvp47nzT6aTiIIXk59PzfasRZrZCXhp8BkldUhnoNGSr2NiidfKNodSCxomdX2A7IHuWRTVNMSFMe5eL-IU7VP-8C-AxNMyFt4BLdHTQYCIFQuG7O-hU-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQUf9YtQTHtn-vQozEptpDVex_BnKSZJKy-HuU8k8cC7D9lBapX9anCH6u08COjW6uxYTVOY0X7uN6axtJQKrl3n6pm6zId_A73zZywWsniqdwdFGrCwSTV2fjoknRxuqXHFv4Vpgb_giGbdQB7uiuXcLQpJdYF3MLYXA-W_OCXbZguJUpFhuGT0eBQKSHpoUzkGODZBJTr_OtVYjE6tmqF-bmqMp3mGT7vuGvOcH5S8oc939hMTUxJzvNnsC_jYMzyZlk8dQUGBjdkwHvKZ8EVIqUaGVMmAXg5zq0RDZTSv-rRoSRAh-WkdujYebj8Wtx11IrvdhCgbYKGqkccsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=ghQm-PcBw65w7sbbxo-wNgqDLJ0FxPuKVn_twSV0vTksat9ItFTxVZwqx8-qxcrMEHWxvFSYcYwAOpRbQLaVnCrD_as5NerlMIhdvUQTM4KBkpsPHgfFM6nhJKJwhPKFrTTceE3kH8uvZVleZXR9giWsuFy8cDDKYT0obgRRRwkYo33QpFNjCCsAiHTpdnQNnMAnVI-Welgk_AzA95F-n1dPo9rR4Z_e3Vk8GxsbizJjNKKrXH7LIJvY-DjMks5h1pKBYMm79ipZVw7Z7cROxlOWWsl7IvErtyghOJxr-mcWYxa2hAUlSKRn6vwmIOSBNevfsW3M4Yk78IXqsYb-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=ghQm-PcBw65w7sbbxo-wNgqDLJ0FxPuKVn_twSV0vTksat9ItFTxVZwqx8-qxcrMEHWxvFSYcYwAOpRbQLaVnCrD_as5NerlMIhdvUQTM4KBkpsPHgfFM6nhJKJwhPKFrTTceE3kH8uvZVleZXR9giWsuFy8cDDKYT0obgRRRwkYo33QpFNjCCsAiHTpdnQNnMAnVI-Welgk_AzA95F-n1dPo9rR4Z_e3Vk8GxsbizJjNKKrXH7LIJvY-DjMks5h1pKBYMm79ipZVw7Z7cROxlOWWsl7IvErtyghOJxr-mcWYxa2hAUlSKRn6vwmIOSBNevfsW3M4Yk78IXqsYb-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
