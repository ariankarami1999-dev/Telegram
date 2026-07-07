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
<img src="https://cdn4.telesco.pe/file/jv5RsXZJTwr-9OF_Sc2Swus_8lRIF-IoUdzF4bGTNCYz-u_wHC_F9u8OL5bjhwOiTWCRvGfgm-B7S-nmT1BbdFXuCfBnOg6zKwTE3zfGr3lAiEPIPl71TrPf7crJNoMozh01qUdA3kmu1fB-rkHaT9BUfwnDPgDyan6u5MOnMP7rogXpChHq9A90XohYWbkZOnAeqD_5Q20Yxxe0Rd0ubBz4_K8JVAO4U0frii41EKUmZ6COrUc8Vlckn7WVgeQEWrldttbjQBXQfjJL_XKL7VktX5wXjlUMpjFNRNzRkXyHLE2hgfxINVYQ7ntvmJoZ1eQEMu3kVvlrxwsE_OVK6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 421K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7lcxfPIzx3P69kKSXxUTg0Yvz9zfy1Jj5CdFuEWOzlr0xHD1GrekzQKl4K0R-6tR-n0uMut7v0N59pSEsF5FOAWkmHvBn-UrVgbkTw4KOOYtTUQ8xP3vrxnN73bkoDH2-1dcWYg4kH0Vc2LwHPdA6i5sCU_ZkOrM5NcWCEcIhO4SNR78u3ygQQXf_kr57UcLc9Ho7ANhADVBECNXuvguvf7V_C4swrTw1XjGdwoMfmezLTPF0JDkG5-ThpPBu3ZNsXTQYvUERpGJ1BTYNiT47QT8-jSG_BUkqmmNgt-LmU3yZ6ewxLIXCjPWTzjGWNfmO83GHEa_aBRM7R2J_4EyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoVMA5nPhCW1zUADkgxravRwOPJdRBp4KIe-2kOJj6U_r7gqeSf_SX1q5dmm2uop3Ng40iLl6ZhPNvL-co_gQPUDQooA5oAUfNcJHAROXF_BaFX-7IDjAUj-wfzWUIBvQDwQW7di__fSjcCI43PP_6a9UH4a5KvoGcd5tkREbesxYL7p19aHmK7wV4Cjhk98e1zruNzjfJLxS8VRZ2faf8t6JTg6ow05TAexxnrjPSUIpkeStCOafwSguYsxaQS56tmX6xHOc_Lh6FmTDecuPjG3PCzhxGXnMeSAI7DKBS2l-RQH89OO40lRpn75ki0o_K4398oC4Rn6-o27X87QqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=KiEZYTkd1sZH7VvNEhcdW1MseP0LQwk5a5d8JS3pN5T-JlD8XyikFV7vEOFjxWv0td6TR6I1PVN71C6b7b0Yggn5GVGXhK5H8-GLCHNp_bneJoi9A2u8Zd84lHJFEm9lgpxwOkvAGFXD9LLMQ4HSaH-zu1DCwfcRnHsUxhNYMGqzsiaFNKLR9dx75-qgfyl2k-zF4eOuC8v24V3wthTgUfLa2MtnJTRTU2IDCwfSSh8XdpR_0mxYdD2SiGi8A9YtlTebtcqSf6OPR7HtyW-jDOpMygZQ7ctgTyI1-PN0-dagPwPtJl2GLzc8b-9SQUT7oZGIvJ4gCfhB5KnFTi2jWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=KiEZYTkd1sZH7VvNEhcdW1MseP0LQwk5a5d8JS3pN5T-JlD8XyikFV7vEOFjxWv0td6TR6I1PVN71C6b7b0Yggn5GVGXhK5H8-GLCHNp_bneJoi9A2u8Zd84lHJFEm9lgpxwOkvAGFXD9LLMQ4HSaH-zu1DCwfcRnHsUxhNYMGqzsiaFNKLR9dx75-qgfyl2k-zF4eOuC8v24V3wthTgUfLa2MtnJTRTU2IDCwfSSh8XdpR_0mxYdD2SiGi8A9YtlTebtcqSf6OPR7HtyW-jDOpMygZQ7ctgTyI1-PN0-dagPwPtJl2GLzc8b-9SQUT7oZGIvJ4gCfhB5KnFTi2jWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIrJRu57y_sJeGEAysxom0UKVDo37LQjQnpYBjwwhLb0iUQd_JPMlRVv_hF6C88Z4I9eZxtt2_pKYvzu72TqgOtpxpJWUFUa9Xgg7ikTI_mG133Fzg_F6KL5t9HGBW5PFdizzhbPkuzGqU38anGVC-8WSTyTJAUnHyE32KNiS3DGKs4-8CA8NhTkrJ7jHhU0wEtD_PtlXPfgmYaSA_kOsIoWe419k5ncMEt-XJUjkbCYOtCGu9fV6mHpjCaO8Ki99kURLnYpy0EjA2GAeLFliUr9Bs0jMOihoUAoDGE_Q45S2SOjXrsjRslcx_mGdPKvXDVrpnvZwfJW8-aRXyO0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=C_ZIMSt3ml2xDlGeudfCHft1yHYeqgnEhJ2tOOr6H1DXOvXqoayKWFfMHrR72AXPxj8efbwNd-KNlNR_useLmE7Nk9ebLGWXSOGRefL_XhxXUuj3z43IxJ5miX3QxKD7FluLC4JfN9aKC2ZZdhGY16cqQKf3__A44DKWZWjlGw4nHRdL1YnjYQBqbY7QzW2dQfqMSqFk3EOD82fan1aGsF1QvWPZJpfUPMy84NCghFcCRKtx6mC60OkW3x6L0V1yWQIlNWaBsSDEhe5P1aexRddUAP5Wsi94xtLtnThnz7_UkD7UuxvEC7QK9JLnXIebhb_dcs2h3HbwiTCX7p0YEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=C_ZIMSt3ml2xDlGeudfCHft1yHYeqgnEhJ2tOOr6H1DXOvXqoayKWFfMHrR72AXPxj8efbwNd-KNlNR_useLmE7Nk9ebLGWXSOGRefL_XhxXUuj3z43IxJ5miX3QxKD7FluLC4JfN9aKC2ZZdhGY16cqQKf3__A44DKWZWjlGw4nHRdL1YnjYQBqbY7QzW2dQfqMSqFk3EOD82fan1aGsF1QvWPZJpfUPMy84NCghFcCRKtx6mC60OkW3x6L0V1yWQIlNWaBsSDEhe5P1aexRddUAP5Wsi94xtLtnThnz7_UkD7UuxvEC7QK9JLnXIebhb_dcs2h3HbwiTCX7p0YEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=AVBN8OWZuNhAH-JsFtmK2TlJSl-0PPa880-NVAid0HsgQpxb0s5tKe_rpDwRkOT32xMxwvgRG8Ukzrb-zBV5HvZJCZCeZ3HHqYex6cKVkY1LwYGK8_NamiVAcfTAQ-KhJpTGIxKBlBgk2UyJUgcIDd2LM9EjClB8gkObF0DwiplOK4FuCm-JFkyzOQ99fxmOXTUKM2tWn54pxzV_71WBiM4snzBjcxQ4ZQooCW6D0lCbPUCzs9Tnw0yqYsWnu20wB8QGpyZtrB11bhyGKO0yKDoGZB0hSQMZm2zEgYOJIV-1Fi5ekMOAkhiDfxmOb6tmIFzWWNJtDMF9l9nlcQX06Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=AVBN8OWZuNhAH-JsFtmK2TlJSl-0PPa880-NVAid0HsgQpxb0s5tKe_rpDwRkOT32xMxwvgRG8Ukzrb-zBV5HvZJCZCeZ3HHqYex6cKVkY1LwYGK8_NamiVAcfTAQ-KhJpTGIxKBlBgk2UyJUgcIDd2LM9EjClB8gkObF0DwiplOK4FuCm-JFkyzOQ99fxmOXTUKM2tWn54pxzV_71WBiM4snzBjcxQ4ZQooCW6D0lCbPUCzs9Tnw0yqYsWnu20wB8QGpyZtrB11bhyGKO0yKDoGZB0hSQMZm2zEgYOJIV-1Fi5ekMOAkhiDfxmOb6tmIFzWWNJtDMF9l9nlcQX06Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsF8wNcZPhZL2WiZFOSUBXkH_PyFuaVr8Aeu3mUPSaG59jgX8L2AQNarWoi34oDY_ggrVqzeVIwk0NuOF8oW_S-dH1jOs66vv0p0swv81dmiLS8sgeZWC2o9JEJpv-SwbVM6QKn4yggQUkPjVx3zoWcHG5D3qbckknWd6-E6fDnWbkOsfP2o2-fHG8n5OZK7otvwfH1kFiey9BZgOw8DUOkIkztV8oXslfHEkUqSNL5WtMkgaupIt6rmQHYST7VOOp0wauRXIAADATMXEnDtwssN3u3SU8T776kwVK5NbfbpnAqBiXN7MQ4YJZOOj0lupbw8roBy7N3ztHKYekceqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAXVs71CgHbeLkZEf6tPGtHd_6gg2wQ9yP_1GREkMj2EQ5m2nAMKlj-B5lGzCfnndkqBInFBll6EuV172dtGKqPj4ETzExbhXZb4GGIJ_SHdosEJtti8VdNhOKoZpg9MfV70wsXL4PTMtW-iRasfdbaCVOumoEgKSTVzYFqk128NQxlQuXnqJEfrRkb0ggGz3yoDIfyZT1oVpZtuv1FizbCisWSuYEWJe1jj-B8yRVGnvQAdDnTi7UbiM5LGA3i58DemRCnwp-WRe2rk7x96qvSCWdZQCi_OCBBTTVPTv82MLvdWaQ4lirM4DAAgDrsBRsSsYuHS78LXeqX_wfq9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psHrTiXJr1kvjGvEPpIR7jCPE8qjlaj1NaI_JHEVCg7fd-9D7TEBe2PZW8hZFAtrl4wKfS0_jB_6ytaVdfhZ0tnckkzlQ0Tr_fvJvTJeqpOnzZW_5wdoqcM5YJfAVh2qkfAX3eUqxUih4_Cs5gBKXhtxrP94iLZE_s1huqGjFJGti6TGfO9F2BdL-A22PD43KnZUhwL2tRs3KvUP70gQqXO5mN0XcpAERDyn-0tiBLjMuDW1TnGYeVDpZdTkPE6ZkVAXQadaVRMGMzafXPB2ZENSxyOFppw0vPK61dPal7JCS_ZQrw8QpcxLoKp2PNvg5-tyjVteXSRBFlPRmSyuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyNbj_Br7AD55aQOXyVYG-UnrRA4eXscyupVA0B90XkqiK8ZQqhP6q8DjCj_rWe-q_-WKc4ZK-mkb28K_eJNH-l-vsWTKiPKwYx2rtOp6H6DqaqhKhSmXR-P_sx_l4HkA8TXseptNIkzLlyqnFTPB5NStmpj89FJzMxyYcpZyeAtl4SO3AnWJEVYZDXUnnwjfQeJKf7oevj2yAX-kzVXX0wV5RCptoYIIKkhhaQkLWUQSPEZEJhJUSjXrrfrAZG87qMtfFE-nn97TlRWVybT7bRKm3aqu7UlErMGu7YUZfKKQg6Q3T3Zvske-03IZr7Sp9VndBBjUOCiQozOYEyUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1QYt4LbGiiwW7BUTDjdplohEJR_5Az0gYUrCAdgRLauxgsaHi2vXuHZSim9tKuVZrCvjjJQyjVsCd91dosI4iSItxi09_v3aJ2pbDkJDVo3E0H3W6nFPQTaubqWyjw2YliPUEvpSxOjdLcz4ZKe1J-QdQafZBoIqsrTp8Zt2TeXbSqcZO3ineUB9mEF5wZQM_PjG7mbah-4iCiMdXWQdHTyBIItTsGk6Dk1NEdunma0Of4jaku_eBtj4RawJJd6SQbAbpba6JLlg8glUidp4yZhxYGktFA8kE-LBiGXR_kDcrhJh0nSIJR18qm8S8iiOSHqTfC6Nco_TLjJbWK4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0KWt4HOdJs83CDuQfVJBj8NQeXG32Ku5JC-2xhC-smXBZay3B482dtRVs8Brlchofupi0JvVp4XcfMT3HbPcjm5rQ0qrzT4O0QNGCzEF9YMUV_yYknuwzEnPmnDjF5yjn5dUMzcSfx6Jw6vUsv0YzpmdyfJKH8h5taoaABFJaTXpsj01uavqfmk49KmPZwInhFFQjWsfjrFb5Ui1QPXc2MOVOk4_IGHi7ApRsB8zG92N0ttQgRqk4K_qnrCxkL0NqmZXC3sa0BKck1bv46jzbxLH8pfU2P2ftfjhj8Vhpt0s2Xln7ADZtPY9KkdVl7LGZq-XKbSw6N1fqvepvOQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5k9Jn677BX4k7b2w8zbWXUCyeJ3CKlNLzJyrpgjpLTUWsosA4TRcm1gk2UBZNOF-J4SEwylF6YXUZ2zhnJVM7srcBM5nCM98UjUl2GNQUza2i5Xo6lnIVdIMLZH8iZDa_OaPZS76XlCXyclZg-k4BEDWJiNhCnLrMEdA2L3XTRPnQ07ArAB3Oe_EYpx34BAxXulTDzHTbeUrkVAbVpR1WU7DRtYbljJ1QzfUrUH31QGLPTodGMftjWAoEudQHu50L83meVBFDWfnE11wTgCv13aSOtlDh4BB8QxlmyAclWI_3KhI8j6jbmavUulN4nlUtjLCCHU6HJCmGLEEiTRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb5QkBO2JSMRNspylkW15V9otVsYZeEJHE5yfo_sKhEZw7sqynMjw6RqPfPYenhhJKFPNNOpn4wOf-9gJi2UhvRoQCfCUO6I5g1aJesQxb8rb8iRiaJXN5UXoBcCkmoJpYC-IJVEd1SeZ4yAush8C9mSgaYBdWw0X86ZThGl05tra8IktaIq7BRjwLhzKxbXKf-WRcNzsmuhxLWQmfML8paWWzq8CAOFHmbAApc5sdejc7m0JlL454Rd1J4m9id31oY6F4NLlpb1-zB_zEE6hN4IZ2wfGmgmfHIRKpAufFNOG09vtA_gnRsTpMA0fUnJOZK-kDbAgBNQ1zrQYXda9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwn4wDTPr1GG3mhw7UKL-SDihYeZSte-nr5c2DbPh-Zjrs_ogHhnDqSsG5AId30gsUpKjcuPVefyJXb_dVJmWjAn38KoxAsAbmrEc5ClYw4GWEW3oVsEM-CYONjS35Nbb0W8KHmSX6ipBToXcMv_1tYb2IEX7bssG7_1GfqT5MviGUyFIhOyDBrqhKqevh2WEAZSfvD5xcr-5xQFP0Hvz5tEZH2SPL2oXnVHdEcqSmP2e63bLOLTOhCWfYeCUt7MllOE0mLipwQN2nO8b1_Y01lJcr5u0xh05ar3pU-z35F2669J70DHvVPxBg2LurExeAdeYreSXi2Vo0nVjHlh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru-QcQ0ODka4n6mAtW3DICWJ3BCQukgBb5kizb6nXzoz6QsLH90te5O-koG4ylTqumZBexIFBh0f193yWfrdVb-Px-U-TAOpXfIXvE8buHUpTZEjW1PQGMSaXYyCRP3kZvv_Q0Mz_gVA98Dnr642j88nlF53wSpXzPxJrRZnlfIEOTkshIGwFu0uRMw8jwCaI1NgOJblm5w_tFWFBOsq5v0aWLotKpNufrhDyn_SNpfKULcX3XvaF93bGiFZ-NMspZazj4ZlgMY1z7jjFlSQ0Z9bg0OyhCd_tuaIblIvRGq6ZQp-DZLfO9qBR-LWobuXerFPRxm24SFOXG6h_QXq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=US1OW27K1SUkm48wxbdqYDXLBwrSKVcAAcs029PsN_wLWdyNguOd8enqdjPBgelooQR0ubZs3jNuWZIt1jJ_UVs5WAIkjU80y-djNRaZJYe3-3NzcOoGZJObVPHKS1wu4sRJ4TT27GIndvmq8Ou25YcXgMu059xEj5tnA2uonwRtJtgtJt00EQ4E_y1TbH2bkSTKYpuozmpQKEZWWulekreZB9gUE_VFrt5lliP0O3S7KPUsdwOfF44B4dlK4WosCfJI9AnekK0h83m3wCMqXYuEWDSdeaxRfulDtLjgUaAK9huDttVGS_jf_Knzf3XE_bwMBpeb3WVHzpvmnFQnMSgSuM0rEbLAQHiE1TpyhqIx_DxaZf0IRVmlB45hCh4b_qIFdReRy7qM4UeN3aiw0CfyKa3ZtubyCbhAIhtk5CSTSJ2zOHNEWCTEpVcRIdfBmYzTzA9aEpc54bn5Nj6LEMYT5bhCLSb1p392t9U6yyPjwK-YzNMroUgVJuDoO-umE7tJHTrw4jgpiSyYEpobp5a6BZYCh0o4hWQ3eawKH3itI48nIxNGXUH7HhGLqCkVWJe1Z59s_grNfwZRdUta8jgGLM35x0plD2hux6Gw-QV_5H0rjABd40JhelMIUDIrkoZ8sSWtj8ckll0RkQhb1yQVwEVrcXWdTHEkoKKTHsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=US1OW27K1SUkm48wxbdqYDXLBwrSKVcAAcs029PsN_wLWdyNguOd8enqdjPBgelooQR0ubZs3jNuWZIt1jJ_UVs5WAIkjU80y-djNRaZJYe3-3NzcOoGZJObVPHKS1wu4sRJ4TT27GIndvmq8Ou25YcXgMu059xEj5tnA2uonwRtJtgtJt00EQ4E_y1TbH2bkSTKYpuozmpQKEZWWulekreZB9gUE_VFrt5lliP0O3S7KPUsdwOfF44B4dlK4WosCfJI9AnekK0h83m3wCMqXYuEWDSdeaxRfulDtLjgUaAK9huDttVGS_jf_Knzf3XE_bwMBpeb3WVHzpvmnFQnMSgSuM0rEbLAQHiE1TpyhqIx_DxaZf0IRVmlB45hCh4b_qIFdReRy7qM4UeN3aiw0CfyKa3ZtubyCbhAIhtk5CSTSJ2zOHNEWCTEpVcRIdfBmYzTzA9aEpc54bn5Nj6LEMYT5bhCLSb1p392t9U6yyPjwK-YzNMroUgVJuDoO-umE7tJHTrw4jgpiSyYEpobp5a6BZYCh0o4hWQ3eawKH3itI48nIxNGXUH7HhGLqCkVWJe1Z59s_grNfwZRdUta8jgGLM35x0plD2hux6Gw-QV_5H0rjABd40JhelMIUDIrkoZ8sSWtj8ckll0RkQhb1yQVwEVrcXWdTHEkoKKTHsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=pC_JBvSVc6Q5scUVJ9m1fPasXDmUZOD-2WxesskKJkyPwqBWQUzoCMurJcV55jy-FEFeRtKKwzwOZYOEkw9U663J_Fxi07cLq1WHceBQp9946-dpHSfK-AwTdoqP24b4PDuLXNz_zmpURzI3Q0akDC5Gb8BmWb0XRPWt8968MzCVyAZv_MzlkYCXcluP1WJbYFOB8i5-kKXmIQY4H8b4vrOSzMZ3oGSVj_8Jgg0YmoSbCNVcdASe7LSPFnAmwq2Na4F2_Sr0v8NmCdUWhCLY4viM_NJ_lyjw1SHdWa3oUBnbR8CNiFzKUeM9DwXeHmz1spW5Z77ktJWWeRTs7j4Fdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=pC_JBvSVc6Q5scUVJ9m1fPasXDmUZOD-2WxesskKJkyPwqBWQUzoCMurJcV55jy-FEFeRtKKwzwOZYOEkw9U663J_Fxi07cLq1WHceBQp9946-dpHSfK-AwTdoqP24b4PDuLXNz_zmpURzI3Q0akDC5Gb8BmWb0XRPWt8968MzCVyAZv_MzlkYCXcluP1WJbYFOB8i5-kKXmIQY4H8b4vrOSzMZ3oGSVj_8Jgg0YmoSbCNVcdASe7LSPFnAmwq2Na4F2_Sr0v8NmCdUWhCLY4viM_NJ_lyjw1SHdWa3oUBnbR8CNiFzKUeM9DwXeHmz1spW5Z77ktJWWeRTs7j4Fdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU0Vp0hZ60PeTAcYMF-w3EHElaU_YRMFha62l6dZUYlGDkt2kEBKr-aqy1mbBjpio6plyyMT48zSmjaBdBsCiZ7GpkyqYW6w4I8jdj515Un7ou2ZuwLkG852DNC1EkSXQ76q434JW6uRSnNNWHiLCC8xnZ3Nv_x7sqvsXMRqBNm59z2W9re_2gUTFFIAfCsaxROpeHZVrA-YYVZniIiw-wMdu7cLJ81UFLoaH-50Arv2BvuxCndZEHdlM3ERG2ZHwtdBIwWJcfxpyE4XOtKoIurahQxjrrBUl3VVaMk7F3T6PB2E5qBg8seICe3x9706Hwr5gtFHFljnG_nIb_DUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BThcbZ29ANqVovn3e3_AoeixZDIQRiy30_x0x3KB9L9Y_wGiT8TLtjFnJGTsjT-bEiTjwf24R5xJ9f8Sv7Hj7-jZj1WVmNKZL4hnuIZM8y8Tb8E4ySWIfggG1a-Zgz0fEi2W2ae6-vxEB2hw3oWU8_-CiBeVUt67RBlpt_8QAF6Gul70amW9pfDz0XOjE0rVhFX38Mb0PN-m5OIZKMiT2tqTmUv78ZOv4cDrRdE7Z1A19tSPyaKAyiJfGSbMJfIF_0AHrL9QN_pVGAjHDJZzEhJnCZ2oDVjfKUXLU0W-FA0cBF4OkyS-dAbbAjoATjkuJK5ZCXgiyfFY6nHikEHLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz0t554u7v5GOA-Lvsrmrk_TNbR4x7avf5LWHNNiDCY-Uqom4EcRfrl3iGiqOzSZ3c3N3UcUcs-93whN-RVbV5kXDi-ooefBifm3IQhhrQaTDH8pdkWBNihueT0rGHs4QllGQgnVz8ImJr4LWS3Yas-v61gv_9bCj842-XfGtbLBRXzArr2MIO7MmEUg9mSUgnHfYYMIllk_7EtSET4-6ghF8LFs7ZsGLio8nBPs1fD8-PmTzOmN4ga5WEaYrPrz8_HCDJDX_P23pJKDUR_35hUNa5uZY-4TaUEcxJbECz3Dxj8C4sCkgiSWD9Z1Df0dIvYUIiCozi93hIpjXHVYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqjzMmVCe6iFi-c_NEGgdMaJiMpcGStyFa-OgNyHFMNQkOMdQCxK60S3ICPGVGiclCLbIBw4i82PbRrkcTKIW9yb-1kh-oHzV1-l5wg5zMBeYX8M3XbQedF4hdPhqT-uZZayctYlJreUOJNLYMgOJVu7w4ARorI0ECrzxgSc48QIatPRXFvn8Jo8nqbxbaDbd5cRuCQP2_adxVbaKFqQBbhUnJ0MTqq3t5uLLm3Clc1B_OIg2ITTh1NW1Z0MHJID2vNmgJY08TpWgse5jc0sA0jKnnR16ff0knxW823trsy87Bqm00LUX4NUE5-rRv3sHLIiK99mc0UcYf_mCAlcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzUJ623KiYA_JbDRnmSNe1LIz6_nzgunlwuS_yJup1big9pOhsNWG546xUdHhYBarE9TadMwrBpEyacGLdLY5vznCqPgfqBhmMskBnTkqjoqhUwtUxaAuzke0IfL9mKrOZkg-pFYWQwUAoyP0q0Vrcj_b2yDhiMlQ9sQNNTx6Xlx5CevKzd4AOIS8BRXfr4GrmZdZTyu62IIIWBDhGF2AsI4fUeS_p-A1dRlTD9kxpV_BFZyGLY_eKlpk3TfHF93eGRiuBrlQSFJELRgiHqqfP90NqTZ97iwXtcv4HT_UPouOw0vtgyxYLrE1RZy52H7dOwxHD8BQXDAe0RM0R-99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apoU4lr7c2RI5b0WFyGgidEw9pGZnKXw_M-aW_y3gZBC6wQnVhwWb9sUV0BoFrwIhSdhWVvIp5SduG0nAr4tK8xlSnGp-PC88Vhw_9Lbuz34GRGZivvbADyVnAiIG_03Omn7vySw_zHPgEv3HqN137OEN-du7niVVcOHCMzZINjjxpW3fHrRKKQq8-3pc5Ig1P6HIunLPGviuXUdXEQOIimBajfHL7YVN_r6rvQOK-ehRG4FpdhrXGImigd9oEqr9ze4bazfTDwWD30jVkZHnL9FPJTf3JHicoR0wx6tCx22SLRSelghP3w9Iya-bXug6GNzR_zza2hCUqWENM4gUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-_Q_GL9S6N8cVb5M5jEF4I8szBleZXXfi9AnWeDlQU8FJzISx5swZBV8Me-4sqFWrdXnFlRKWbPpNJpt2pFMDmJGzGixHkWoSlyRPdfBKIgpQsydajdhp7Zdl_N6hGGqRM_KGeqMPH4uW3KzU2gscPAN7FctQu8_Ow4vKqdmofn2M9gmWqzDiRoVIs6n4Rlod65dfxKvEGer82oKd-1vHCBUltUsyMUMQ0bJFuDVkyPkgh8Hwc5XRLsdusXrbacMEtO8wOlcLtCZMncgDV0musWLekJHgl4b43F0_isBowEwvHw59FOnocL9TYnupHw7p4d0PB4-CkyaufGXQENUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL34ugje_g1o0i3gBiINFw_P04cL-YLeVeeiOC2uSIH3E8j6iFespdlLpkbagvjhPY2vKAkg0z361PUadXwGgTIAX1nHf0V1CHjU2_LFRxv8at6djA4N-ZXYYs5bT3eRflolYhoCwuf2B1CmprzVga-em31I7Jo-FxHaA6fx1iMfQvX_f559j28Bke9_iwk_ZuVBBDi1SWASG1OPfQQh9hHkq311NxGfQdJ2wLYQFpv4-zYW0NO1kkVTcnoCNgeb9KwSD3L1p6DwhA8ciOKNOZ-WnwuVKRCgIXqbUnkIlHlPjG6vuWhsySH8aoo-VzIlFzeSwka9GeHhg3f3A2vDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcDakIYAVDM7rElHAGtjwS6iDFPyrEaADAcEy6-O674aH8_QiRZHW8OKTqwHB6CitEg-fCFc6setbvELOYSPAP8MUcSNclw6dvyGDIQMtezeFNQgUDp11n0KGQYQ1-wu2GaQG677vM2W-OXCXMhAvYk1G6Sk0bIUlc1B-T9cT97pEUlLScCdao_b1PtbZzvySrbBZT3zOwprSzFokl_7loUPdDD2RjXYh2tBDKyLJJV_EAz0FrjCqYLDaJI6cNViqAynXRO-kMy6wTZnRMiMre2I0ygj4RoFkXkY-0cX4z8Cy4LqyplL369PNXeJXPDM6F1AN0mS6qRAbsnwkI2jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9_lzevNhXIr5tIhE-v97XOsaHmBbw-kshQgZaCS4dQ4yBEsyJgBMdMmyoujgAPyEYzInXU8wPYhEg_U_pu7fKrksQ6op4AZyKnavZ8XiethAdOLvWN5gzGf3fldYILbfRKk6SWAdVigvpuMbdTiXgOY3oWKC5EN5auyNsaF2cFtOnGVPNHBPI3JHncGx3XX9Vqeafyqx1fUiiUhDzORNBd65c7d2YPY0MRHuUhBiCx8ABsUHayW6Gu-AtDQjXHax6IkIpV_boKNaLQ_J2CP4kittFMkcB6moAToXkNcAdI5ex_zq98bZF4mhQN2Dx7DACA44XVp9ZxBa82DqPvC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA6aBSJEbh5SO1w5AOjGCpQ7YHCdq4WXyx4SRDylksPfF3q1Gh5_XVVCru3f9kHYrzs85LdwND6h-T2IquIyaotVpj7_uIvAGjTpzEUC7E-xd1Tw81j9K0IDQ5kuIpVR4JYULVX3BoGQjAWZJ5RTUfaYfkUZ8RNv0XDo2dQjZoCCzcP-_1oPW9i1Q_5GPENhZ8nhcSY9m-cIzb2H4F9R5rxEpvwXkRDQGF9NVhJQj4tN0k_IftIy-nNNP-cLc1UINP95MLFPQ2BtyZUaDD1nLPfKWrHyHmuRBTwP_1bX91jT5tfXSPpXu4JWCotP2uv7MGtzPfiXfcwU8oW4fxYBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd3VHxKAB_tl5u2dtiCVhqa03-1Lr3oTJA1tD4t1myc819aq4cxrD8Ji2ltJ1UM8uX_ULFcH2npYpbk4DKefpghz4kzqeDV5nqY7FRtYcOgBUKdVZtiyedsVBC7bgBEnAZvN-RxsNCSbWUkXVpsXeAtTtq0Kt1q0RmklqzXyghSUMZatdr9H3fZ5H8JDkgBNTOUioTxLRLayar7S7xOzCSUQxc9f9-1M7DD8Km8kUVbFrB6zEar3ik4bzbTamItgTA4t1CizZD0nUeyPvx9KAvCJ4rrNjFh5GDZxUibsaE8t1UT8qaqU9PVjWFKl4voWBMBEifW_PrT1NKxOKH5pHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfoQ1NTWbtWdkJLZY0RTtjTauxiy2gjnmQW14VUJbFgfcGBwUb1G59YUZ2m6AASj9fADbWmEmkCyggcUom3YJu0PdUS8oiZw0taveiGiWYFJYLDUJ5rtSSzqVIMQ6zaljMg-W4GFiitIsAmoMimoHR6ao7TYMq54UkJLXGXxqklBfPCoTkPEaIY7fu8JL-ja_8hQPPctq3wy3LapteI_k2gv19x44NnbWsXfUhQyoiOLEHxZ9LBbCljLUiJBSbCM1VliU1Ly8Sjg02b-huG6ckeHVn_U79DLavA8t-c0Zi6u7f8HVf7GFb3l31o3E0oIoRFrFX93aZocT-TaD4E9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNHx2AnpFVQBAUvkmEIJEmRT-Z-RBkcDKYOjL3XWsbRyV3OuLYQPne604qbgZ9u2JzayEY05eOOGk0HGAXRUOxahSWmxm7y9PjCVScMGl6ViZJ6Yk2prSgEYs9sw31VN76dOZeSrbLNqRpM_x6hwSy-Kubk_P0Yv3JQihta4Lbq6-i_vqZnmLLH1c6WUcvxathMvpEmp4Dc4pFntR1yPHDEygHjv1hcUhvO_NzRumlMDLjAneUJXObkN9Hu9c2MKWSz-WFaJWRnlU5cXAtYeDyZcYRg8PHbe83s9rH9ExX0GhvpxepMLvBbHstpLPZjxLxHM48o2W1Z2XBnq4cHcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCfqU02up3RMtyT7t5PjxY7c0UfRbb6iHQTlWlNWx9MRhO6uY1CLrdR1HspbxYDJBRVs9OMAmyrY3PfdOurleizqYdl3RrRGitf6QWW1UHSLVLRdkYsWALeFRAri3GVgz9cYbsCvl1-AileqFSBiEzFIiN3LBg9sBY4yUE8s5xMsutqnfCBcpSGRD6vubpNHmOP6DDV4b-t4nFxNVeMWOcWggO_sASA6JlTXjYuh1lv9ZheW3KgHNaTCgZIMObAAlCLbyT9I6lWQMmD08OVZcRLjTjMEFtx6piKb6qIDF1pH1uCF7YZBQESTPahHnxhfPYVxRjWtbbnM18FLE1u2Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alZKvSsKYOEmxgKXZJqUe9DfzpT52GBM2wfu8Z00-6GH2kMVoF72ysB0Lhd0hkP-1nOAaPb73mPC29dO7dQISX5o4f4CI5yR3nKuFPR551OWNMm7BTIG-ZtJdktwR-Tm1Tq-hwe0O4m_RTYbKQLwgNBUg_YbKmbkt3frHN7yMWHPComaaXwj_zQxbuvkZLmLtgDlgiYaIS6HzBZajbdunngnPI_tvo686jdVRuAGoUB79pRpDuCNtT1Jzr6pGjkuiwa1zA_LNQ5QtHGvtlA09NOetLKrbetOETMdd1mFsqgHe7YR373awLIHuvH0QKgRNGGyOYwaZOK2dRN8l5B75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf4iLmDp9zOKvNL6eWVjA9zWCv-K9_TlDzlj_h7u7EHdkRYB_gwKEM2NSJHeXyFwoVOtQED55GdgrNNBVpZXEsHhec0CvqJartMgZgr84bHQv0Pje1ajd5OZmvv-byS4QbZLccvX5Tb2TehA83-2lXtjZiaxrzxwZ2aXwR3B4eI58eN9dUIvK_JnOgdNF1mkvPj1Tn3q4WRl0yXm2Q_ZM2LBcod2fWp7PrRCJhnFDBAMSNb8hj3tcdIUKHunVQKLDrLrYRGfjkuiKE4ItOOr_VY8UVq0M7fCCYLvoDByscEIgZBKMT6rdP0VoKsJBHf0V7GAs6CrsgINRFR_bqH2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GoY4PnnZkcZ-GZVKJWVZED2r1Jx9ITdX4-t6Zhwmq_v4jPNP6m1ROKvfeQ90uaetJAyzNFkw2cvoibcxjUjqDEPZThr1CocmZwNOZoaP0ulU3JKpKXH-OsbFR6VurLcqP1NtKjo1NGbVGSj6du73GwSux9eVhSobkbbzcl895oROUBFMzd3_3boPVBNV69oflpzM7IViZ6kA0_5MKUQRd-Isy1uFolVwrq78ElAnNwKGWhMbNZ2fYMrHrKq3IgQqjL9AdxVF2sbuDJgmD1wGyF6ljWDXS7vygT1me3rYmfNG-K-SmoEZ0IJ2lvJ9SulXgPPxZ-66nTs9XFehgxBUGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GoY4PnnZkcZ-GZVKJWVZED2r1Jx9ITdX4-t6Zhwmq_v4jPNP6m1ROKvfeQ90uaetJAyzNFkw2cvoibcxjUjqDEPZThr1CocmZwNOZoaP0ulU3JKpKXH-OsbFR6VurLcqP1NtKjo1NGbVGSj6du73GwSux9eVhSobkbbzcl895oROUBFMzd3_3boPVBNV69oflpzM7IViZ6kA0_5MKUQRd-Isy1uFolVwrq78ElAnNwKGWhMbNZ2fYMrHrKq3IgQqjL9AdxVF2sbuDJgmD1wGyF6ljWDXS7vygT1me3rYmfNG-K-SmoEZ0IJ2lvJ9SulXgPPxZ-66nTs9XFehgxBUGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYOZId8la9J_OrJz-2oib_w_l1VNBzOjKdI06eljQQhyETKiRZ8TSeRxvtHlInlR91gCqMrGHg65zNSuJ_b2M5kg3mA2UoRu1AiXhteE9hiWUQjb-CXySXUEci7gaOvPNydVSpW86w9WysyrSBOH-LoF5eEdsnVfD5mvMjZuDeZmrRMhBE8qie8SFSvhQz2IrW-0wjbCSqVfGpqZB8N2Wg_m7eDCkbH19-vFngoa8cGrQMQ3J9rDrD5neHtEM5JOquyMMtMYZlDrqpl1aQL3rrnQ1Z0J0xzW84A_Y5m0th5vZAaw1bRWCgW5dIhUZ1VdkYmOMMddTfYZv9u3OEdLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_A9fbrn0L-igIHrhzL6cyxC-jkEVG6qIoNuQMZl-mF2arWobtNtsFHC6Ktvwua0eYbCfBnaafwCW05IKsIlgBGJ9Ry0NM15_9YLvinnlg1sRuKV5lsz9OUgqm84EIdQaYDJaUjFEzgcLLz09rGmzDmSGqqO9IV-lrzeBfFSxmuFQWaA6R-NR-XeZatGDELiuVBJhdiTFzeVX7xEy0_SNx54YBkqou81GisfpKDJa728jilProOFlkzEmvUjjHj9YAYqaLo_AsFvE6Of5G-bCsg3LaxpXlzcDTbMqq4KFdaTobXZriVuIBtsUQTLd5Rz2rPfQHl52Wqv4Mcm-YUXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huz19JsNzZmoSZ7AFSKJADiA6CBXZMJf0qXptbLbKiYhSpPh4dTVLwxuE7z0LdEyf5zHZMZ7NFWfnGOauSkvwVSWsQlZikd_-QItQ-X-aynBU_aF2C3fUEbxu9a8-tDgFrrJdbqNeFMPuasB6QLD-mI3a1_YOB2jDOVSxXuh6BD9w3LZ5O0WIPZTesDKDxV35daSYcqP3e51DKVlX5emptJJkZJapx68Eb4FUK3tj7wKHKAp_tYPCIy5wIf3Qui-qjOC69lYqm8DQTpJfKoB195Cis8Yr44AyViM9ExqEQamaqHjDZASu0wtyI2vnuVLitxgHUvKx0jM5fZvx7k7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIctb_9H-xI-UzRIaBncqi7SPdSJeqTgzjgud2VnUvKplnf37_8wkTNRyQvF4T_Ke2nTzRbiCpSjwo0C9PvLcySs3NiTCaXZ4NUZsqNp-iWBAuEtCHuuIT_W9xz8UYJ7fUUK_Dky3SoLqVJgCeepsgH2bbfWeQ2_EwFm5cGpx2x6ng5A9iUZAcXckm_Gn7uCv9y2ECvb91Q7neysb45Dvy9ZQJ55uZmgzoYP0e1p1RRU0vlmLKRnR4DAFg8UIyTNfg3D01N9szWK99FOknLmEFi6ECAQCV_x4QjZkWs_GXEz_C77pzLu6wUjntzRtd0H-SL9-vKmQo4vqofm3OJgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKSu_egjIpn6XdM6QEnpFBezL_SZUoBmyl00W69x4T_XX89OHnpEBW8IVG2EtWkA1OPue4l7-ZB3X9qavWw-nRLkfCdx-GT5dLKyr-TPL-1k0vuNbg85pXLpKmKhDUvGCzMYE2ltVqbHfkIdPGMEKy_y9HZrpeD9B3x8lbjOmStXK1b8NbGMledbNm0ZIHy0zFKy3ZBgq-SujniG5lDRRVxhEMHtVBjhjOmi7CQtwQ7s0yNWtmC0wQLmRyMv-VTkapxh62IRzIVdD7r1pDJNvQYkpF11TbSxqWNn_upIHd3enmHrkUw4upK_RVDulWMH-YzlEWV_sAoTASMPHh75uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBJSrx1SQ7CJPu7uDqs9Sxwo02oJF15sJCvsfrTSZm7qCBeKlCdYYTs8eTTf1Dzv7GsQ6GkEqPV0FWWkkS8T8K2jMGXFU9NDV8cJJHv-14PVAtVt5O0vK-VBfMhIfAvhkMxc6HL24w6yK5g3cpyph0Ft0Q6Cu0S1Wh9LWHfXVOEo7HRElM9zrVWN80huYTdhqATaLVVmNxutDH4rHyLDda52ZY4OHoEV55bLhcHiyD9GAsqNd0eulvCf6QppzK0GIGm2IyZ2i2xApvlaRu5-oLessCE0CUMWvMdnBxiIxuePHxzaQUbKGYAI00LPcRn97zeLQzsUpnPkvjdTV2I01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI6_bAPMo9UDYA31kbl9PJje8hKZRzBAQqV_KsOGI68Aq42Ky8SOBBMfZ0jiAx_zay0AtzK-22p_IrvpT823gpLZhXiktINIo1QAfnCScIj1sULiCrhrNi2bfeztCMY3uPc3sUl9P7dvFmKde6-YeGT-Fy9pAG8wPBhvKbTKr15eN1-SVji8-yP-bkfj2UryTzemKNsVWZzgPGfOv0tnxk-t8RYXGNwTTUGKxvZBVfe54PczfWxyZiYEjruNZa6U48Bzg5AwvfffI7lSN3jo1arZFO123ejhTDGpE0F0H9MmF-OdfiqBjzh9LcuXt5XyGcFQ8naolOVI8lmOlvOGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTWIWKv1F48YFkmaZuNbj9bTNlyg96tmJolNkFlHNGBPNUXQ59sNwBjf1YqwTK4JlF8WCSbl1iUwJcK33mYjSffcMAcKgIZ1xPy18LEXwzq7_SxPheFPBoKLkJnZqXS4k36nHurZ_eMayGAtkLijeoRPnRG5J9g7ANmaEHs7q2W8d-gBWTuex2NRZgUGxDRDmGsPfmUDiWeT3mLNCG-43_H1Nfg46p80k_rVJMoJu--lnchHOOt5tK9Lb6JEiBGunci2E5MacGHHdKaFHq3y2uiwB1cMRjwW1VBokiqqZNKZOwQjgnyfrE9VFs01_VrWPnBpirDfI2h7bGK3sO8bUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_LPF7L8w47tw1-VSz8xaoayHjZr91KwbyM6KbdEjqR73mDMeY8kABdiq_k91zKEPrAs3eK-LhIcWcAi_Sr5Y_5I1Ezs0FTKO_ELdYgypccPhfopTLCinxaimMpWWe55jQyXYXYSNsezfoyP82XwvbXrVbsnY3X4lc2Q2tl3yLyrapr5TN0_3uYw9MjIdDd6UHjDgFsAhW1Nklp6pyiYyICrjfijIFI5gcwg1JFRzrNNjQQ44JVqHfTbfguU6yYiZ37V3-i9oImu0X8-evKP41Rvav2__wPAD-M8_6zzYIP2th1nB-B-waawyKWgRzzgX5XUa9PDinvEEO50j6-vVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Niv19a_nzy5ppqgx9dkNs_ZtHAG6dL5k2ddgchEkcS7CahT8j0KlJqUGwoB5MXMSiFdpT9SLaZLjw9rMcvI2qR7gSrmJg03nOUA4ufncCd9fr9g8NG05qzn7e3DlWfjf16Ras4BE3Ri15vYUwPRPsq-Gq0rbZ7J1349weCFxkGFvYDXAdzsFYzpPOinTcOCOP7gpXnnoFltMRd7AdrjH8utpoTnP2YWtIvJ68h1p1c4p_qCwm3jgA2oUWltspcREqXmybay1_NfRTkvOqq45qRmZnq_ClrjnP0ixawOuZCUHoPo2ILPKXRpTWNB1Cjefa-6dkwoXU--w0rKj2IALuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4KVl68s9lyOpyciNuL8ExBJgyk96gAi2rT2C11T1Mi8aWezXHFDK-sp3Krc0GsBLSbmcTB_TmuUdWxrBRqSTCdl7C5wP2GeseANOO4V5MKcSj_SyaOYGQ6ZLHIcleMykG6LJ879LUQ1A8BuznKdAYoFDTQFERb8fPd5BJude81wrouyZLD0O_E8UDuVRPZWNvmsRbrPaa5Qrif9EOxhC-nwhk9abySdOYMcZv0JidSrUpquQFSqzwzyx6Yn8wr2Ww26bxoRMhnOAsbl3RGgsdqtYDzOWA9iOZjcSHMivc6mA2jdWxk-fLABArT7VRAc02h5SwfmIKguVCplho9JDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiybW76rVV7ayvE-tYPnT_NQ3y8QMtuZRsnCxHLH_DK5DW4R9-sSxO3EZiFm5X1R8x_7HiGIy-Yt6-caQJ-TSjg6r5I6uRzp-tqTedS_KGo6vUn1R7hoP3gLspTWzuT63RAbc5U_Cqwn-wglGRIIci78BZ3CT_9ab-sJmn3gX_2IcQiohHr3SB1udQY8nmJpaere8rslf_jC15uN3XXKHX2heQoUVaI_l3CWV9knqSeg0YrJRs8aN2CQUBtq5A5VYGdQ0yhJc8ghrFamannGRDAaeDM2ygayuJXolORXlqFz7l6k2GAMGajlpNV0UgrHUQhwf2NESQZJlIc7aixCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If0RvWOc5aXa4EBPbPZmZUCR_pMjnKvsAqwW0e3myqthUTU2nPoT2iviRJU9WUH7VfU1EfG3oVcsN5C74FdXhwwy2PzICKfMXlVisunfLGrKoZlmV4KawpFNF1ZZ4_i_-xmB0qOLuEA8JGmvrYXPitDuJH-sDxB-FS3k3GCAshrMpH5Mr-XBPb3l4g5aaZRT29vN7Yle5n8lFWQfVogJaKvZmAuXXFJ0daXrIUvY6SXpoMeohOYPFmhELW6fdNku33ZFPnRkZP6ZvhNm5wWZtdfukNqYLZLZejP3X87d3Zxgx1Xtm7ShtvC4TZLmcne8zw1BPslNSKd5VGBdC3xdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=N3Li-VaPtD9aEgQHkKDTd7o3m3Oe6QWeLi8r6tj8CESFw_RNc9E94qnvvPdX1p_8VyfEg45GZx5dooimhfs3QqJNW937FUVkVFmhTSQxGZFyHb2coCXcxv4jWq2UTph1PywK9C9xq6DOu68B2Ya7ZOUC_1eitmp9KczsFRGBRPNofwmsQ_71ik2GE0YeN2WgWIu0COLxEzTP99sX0atELCTgdZeWeOhbn-f6ya0fPo2Ttq3t0Wbp1etqovdlMDR5Dd_7WDdSnMbsEWqnNutlVHesXMKo4DFAeyOJ3vi62j7CDU1ljnSrHsw-DOsT1Miy6fJ7WXnSKDbnSQhajyzlPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=N3Li-VaPtD9aEgQHkKDTd7o3m3Oe6QWeLi8r6tj8CESFw_RNc9E94qnvvPdX1p_8VyfEg45GZx5dooimhfs3QqJNW937FUVkVFmhTSQxGZFyHb2coCXcxv4jWq2UTph1PywK9C9xq6DOu68B2Ya7ZOUC_1eitmp9KczsFRGBRPNofwmsQ_71ik2GE0YeN2WgWIu0COLxEzTP99sX0atELCTgdZeWeOhbn-f6ya0fPo2Ttq3t0Wbp1etqovdlMDR5Dd_7WDdSnMbsEWqnNutlVHesXMKo4DFAeyOJ3vi62j7CDU1ljnSrHsw-DOsT1Miy6fJ7WXnSKDbnSQhajyzlPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHSJHsVZcXmNYs9Vw-dUOe1nDh91qTNI4Q9z8xkL6Xz-iz4hAjKNW5WiTz_ILWgDEOmAfa8USL5Ym4KGi3K7zOr3vMcV3L6b5_PeQsoS3FwwH1kCjEvqrO0U1hq2tivSYP5Yx8QvXGG7V-KTXcavYQs6VNsMhKXJkrx7TzNo8KkVKQA1swoEe5iT1aXjXjAwMlEjv1yJLcZZgyzMy2vV6d1CEDpN8y4JLq5mkEucjhq28QiCmx5r_bhfqP_woEq-BkBX8AulaU8KkHv_Br4MC6_FLoKtK6LPaFwSeW95RHoD8yoBohIjikSiSON8_V_-X3UJZAhlQKw6glA59rIslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abyUIOHTWhSSeLgwoIdPzp4DOX3Qz3e39X8Nr5_Ksx-19X1PptVZxLdFjZwGXfgRP6ywcHyc3pDWTNVYAALvNNDgQLJ4OIiqqEVpqC5zhhgZsxRnJDjSFZxuoJ18wGtm-yimwG_zOEfv6fog9zuRWr53r_6wjlRGUH0NqrAPtV_DIOqnTwM5SQnXQ4Ys_4WFpesK4knM5I0Jze7qQVmQBLp76kzpwbaYHUrJSboC7i_R0h8raFlNMqc8-6Cwjm_n_xxFnSw6fT6ap6ydvG1LHKnzJ7uBTzrwsdUzfff8tf0FVunqd12J6Ml6q_gDRSI9u8xzZCPpq179whOqgxn9Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRVf_c8I-csxTP5KlrseXXqj5QDu4g1R4W9Xl-MbpsdSqF8f_SLX1eQoXrn2acr59E8hzzZ0PG0NIUBq705R3cWvYE1lf882y7amYwz9jURSFbi8B2G-Azj8GiW4HT1xvc99kbnmNrjGrJ_KcegirNw32O7OxorSqhyENmQBlhdzOF-otOExaq2dcuQd3JZFXRO-fAXpvdcXs0sjCJW-N5DslocTW217RBACObEX4FbjPBx8AH4ZfVBY3KjJj7ZdXoW4JPkPr0sTAxB6zg-r9E9YBRMaznIBk2g_Tj_4jNfAWd7wngpbwaWWBaBcPCOprAj67tTs5idvCEnbAjEBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWL1ZlMYQJsR1bXSV1pUjOHFN9FVXYj-yg4vJmOQryW7fEAKexFDdkbAujSUptdHVZfwUpembXEYdk7wYwY6Q15wPCtBCC0sq75iLDrxLJgoEYqDShrl6qzGr0ZuJBDTdGpl7C6OL_RNQ1nLod_6eD3D-zOMXYRAmG7HhfDPaowT8GDVkLFN5qVYquV2p0idf_OzpkWMiwXq8WIFTK57wZa01mC6h137iShLN8HQrg8DfwVXN4HT5QQ_Imww55UbwoVai-I23_vWygK7V7Jlc6CUQQYcwgQQDgncAc0APERIMTIIUjuoBojlHBGuSiulrAFmoPgTymYaxr2jdxj2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxm9KrJydn1sqtKU67CDvgpcZOGoJI2_zHpn7rrby9XFMAYvQ6DubR7xkqMz4Pcwj7agV_RRVi53Jb6FlpsdkWoz2ZAFh26NbrwkXadjeigOD_QeSjipzFjwMugmbGDmygSPC3hsrEjxnKwVmp2cDvBjcKJejUILcLS3KulVoc4fPL0A2BFZ9emcxn8Ti4Q3EyAtzIfGe0pOON7D9ze7Av3JJX-Z60HFQPRP6tViO_nmLsWXe1xQ2s8P6sg9SoRD-t871yrHmcH48yMw_jxk8P9GifsY9nSlw-rkpLeo5cWAXrEnZFHcU2rXA0ByLTmGNU5gu2f4C6moGIh8Yb3vfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFsky7NSx81dK44GWmQ_OQ3MIkPuc3DTOv5l9ubmu50iChXyk6dye5r5_g-NB4YsW458lr0mzVxh63zpViLUAXRCNRoV3e9hane9p4mXJJurfbInlZ49CQOKDoWUAPVFEtG8w3NoA74BCWLaANPk-D3PA5lRWOUEmyz60Q9yRix5-Q5BCaIIW1AeZi2lWndsiEhX89hGmVQKWQRJ9PfU-f5M0ZrPm0Z6MFTUO9WdA_GzzXSGvEQQbIBTJ7_nlvw3ognDg-BQ9tuAqxrslP4T7xrA46VqSdlPY9sgd0IDfd1OBRyjC_vWb0KbmZDoSBmTFDx5xvCIJoRS2HoKQElzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfpXaNNnyccC6d9PhkyAy_0Et3_QxsqpdVUJb5uG2BOs6ixI6z5cHLoK-PpXSVLms2zbvE_Y87DzHa5gWxt9U_l_U7dNg8bJcyXBufrtGc1ahpxwDwVxhc6Ct30J8mBjpJXe7BF9wh7Ho_dgIXsWUsKPJv8M7WkkO-8MA1mqn2FdZgjDzfV9zgtaNp07yioZ4u-dtGrOgrm-L3LduVJrCzBHI_v0gKkEIeBoj6bUwi_FN2rrwf5WQVyw_oLOrnXfpwWhuqkdQOeO_963ypxHSincnsB6TwAz1WsKHXo7gP7EXb1H9FrWofyURpW-VviPNhLrhfNSA7yKTytRRLReig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=PeQlL4KgRjtfoGqt210JbE3xEBqxG3O7KFAHKACb0L3UmRxxD1WUsajv6J0F-uhQH8lYVVyumsCZrXjUWsSOMIOVqfMbhh6eiNMWIyJBa4fUXpdvpm2x_yboYeHswo-aVZhosbwUkjpfcYjgCxdAWyhCYHQk9uyHmo4-NwyIxDzD-IdegOueteq8-kCUiLV5wcVq1eWH6-YnGAJM1uI2mT1C_3j_dh6N0g6XAAi3zwbda6L-98IJ7mTNzPtICL9NyU5nr20XINUnrNHxBfCeaIHwgq-_CMhBnHSWhzTKxe9bwAqEuZUdDTPuV7hZzK8apzel8KfBvlo16d1BdAclkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=PeQlL4KgRjtfoGqt210JbE3xEBqxG3O7KFAHKACb0L3UmRxxD1WUsajv6J0F-uhQH8lYVVyumsCZrXjUWsSOMIOVqfMbhh6eiNMWIyJBa4fUXpdvpm2x_yboYeHswo-aVZhosbwUkjpfcYjgCxdAWyhCYHQk9uyHmo4-NwyIxDzD-IdegOueteq8-kCUiLV5wcVq1eWH6-YnGAJM1uI2mT1C_3j_dh6N0g6XAAi3zwbda6L-98IJ7mTNzPtICL9NyU5nr20XINUnrNHxBfCeaIHwgq-_CMhBnHSWhzTKxe9bwAqEuZUdDTPuV7hZzK8apzel8KfBvlo16d1BdAclkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRPDRzTwT7cJF3qja5CPW57RY1MeMMfD0npMTPRBakCqs9HqEaYOVMuwVXm3E0p8vKoI_D6w-VJ60E3VgVPvW6WcfFOWZ2UGRz4qpEpa0KCn6kK-cVMwDjDZBMTL68LA4kGrJjmmm1Dza-jkcPt8P5FWoEHPeth0917q8yZ0kbIESYYZQU-xNr3vSNGHp6dwgPC0gUYqh_t7ES9aVLIR0IoXG31ygutA_lTNbLHR3_fZSj8p72aAEVGatXKxe13WqIcpXi8099Xf7YeRFH0m2xtO5MM9JlMFDxWJGVI71bDZWfAGN-5AuKSvQF16ldNNDoXGZphOJ5FastNg5RI-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rif3BBRRCdq398pOdCeBbasl08K0Q9OAyDKygqg-le5ZAvo1A8CO0jZ4TlU5Pe4MHD41DG4KHV97z3wnZOVC-cLK682dHDzgDiuuCOIxNUvnn6gIFPAukFTGMIMr5fDLrbVW9SVw-i7glpg6kw5ricmq_v7Mr4E8nd1LfniZd_m4Id5-RJaPEOBVpYKNz56pnIJ_E--K5ycw3zDgGS_-no3wavBrEmAqep6MQwjM10ZOniBd342oTKXLvvtd6klfqIKlJR1Ytk4qbiGG9vPdmSZg1KuTUbKJVDDnPBgvhCLvtunV-_f0sJWx4Zb-sYQHdux-65kyXJQWHU5N6wGFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=juQFe56Ekuk-cibnPdZAT9kvvQ8olhZvWvv45upquoS7P7k1jUC0xHjaPPnt_736xV4rsC5jschifU2WltWKWawrS8aOw0vu47FzJSt5kkzLto3oCzLSZAPf3BBxxZKU9rWbbYBBnkV1HDcrsjI9vVnlWHuxOpBgssHMqlDRH9vLKJ8CgLrJ_nAIxlCOuHMWwmHvBHGCxmdZzXCwyu_jHMJhF9w0L0ugRks9e-KsQS4ok9srZwiCgyyM9tHNnJunCVLPBGn68Q3NlMha7By8N8N8VN8SAvQSUQsBY0LGbXDcV3GOhSb863TuUv4Sa7SNQzM0zFtlk0hAW2cXmLkGWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=juQFe56Ekuk-cibnPdZAT9kvvQ8olhZvWvv45upquoS7P7k1jUC0xHjaPPnt_736xV4rsC5jschifU2WltWKWawrS8aOw0vu47FzJSt5kkzLto3oCzLSZAPf3BBxxZKU9rWbbYBBnkV1HDcrsjI9vVnlWHuxOpBgssHMqlDRH9vLKJ8CgLrJ_nAIxlCOuHMWwmHvBHGCxmdZzXCwyu_jHMJhF9w0L0ugRks9e-KsQS4ok9srZwiCgyyM9tHNnJunCVLPBGn68Q3NlMha7By8N8N8VN8SAvQSUQsBY0LGbXDcV3GOhSb863TuUv4Sa7SNQzM0zFtlk0hAW2cXmLkGWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=c4Bu1wlk3SpGa4EjboIRHwGajYrzr8Ozao12cqwEejQrMqVZk_Lgf_oa7R2zQn80dKATo7fsHrK1HC7IxcOFEEEw7AHaIQI1na6aT2CctZwbXPSQhrZK-dYpyNM23E_vOdIALsF6tra8hUMmTVIYxR6v66eNNuXZROW8ch873BFIHR-cUQpXT_46ofFFM3X1z5V5JDhLEsUEeUZErMIssXbjp0C1kMF70M_1fgDIEJGHW0E3ksRpY8lJTCNA9OR2sdJg6l4-KVRgd0UCmUXo_PVWdvscQX2Oty9Oxu2HAjOQzSkdwLPV_K-Hpo9llR6K05W-GGUcbBfMKQ967vNIdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=c4Bu1wlk3SpGa4EjboIRHwGajYrzr8Ozao12cqwEejQrMqVZk_Lgf_oa7R2zQn80dKATo7fsHrK1HC7IxcOFEEEw7AHaIQI1na6aT2CctZwbXPSQhrZK-dYpyNM23E_vOdIALsF6tra8hUMmTVIYxR6v66eNNuXZROW8ch873BFIHR-cUQpXT_46ofFFM3X1z5V5JDhLEsUEeUZErMIssXbjp0C1kMF70M_1fgDIEJGHW0E3ksRpY8lJTCNA9OR2sdJg6l4-KVRgd0UCmUXo_PVWdvscQX2Oty9Oxu2HAjOQzSkdwLPV_K-Hpo9llR6K05W-GGUcbBfMKQ967vNIdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=NMiaprkGc4RxSLzHn7OssMej7c7kX_6-a_-5GKVroACnnYbHllup_D2kkJPWqWtfAtIcQ7xWjdeA5_7Xkg-1GGCVLIzRlKZP2GiuSLNPsrYH1yjLQQzI-t7FyoGufMuhV4WuLl_YQQjiWY-RLuoseTGVxuJV-DhTP1yE5_TP0oEu0AgND6ZsWR-TKmdoSV8nULa7OJUX0FHMaSVjemFjFRiRGFFxFIWIPAvUKY--OqnGXywTekVclo_5stu7nCNCRNHGn-wAe5zyafFQbDlFth6l8pVsnjrfQfzQXP5oEi-BdrjjEeUdS2iYiB1iTCnvEuvxGYrNAiyVhVfSYkt2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=NMiaprkGc4RxSLzHn7OssMej7c7kX_6-a_-5GKVroACnnYbHllup_D2kkJPWqWtfAtIcQ7xWjdeA5_7Xkg-1GGCVLIzRlKZP2GiuSLNPsrYH1yjLQQzI-t7FyoGufMuhV4WuLl_YQQjiWY-RLuoseTGVxuJV-DhTP1yE5_TP0oEu0AgND6ZsWR-TKmdoSV8nULa7OJUX0FHMaSVjemFjFRiRGFFxFIWIPAvUKY--OqnGXywTekVclo_5stu7nCNCRNHGn-wAe5zyafFQbDlFth6l8pVsnjrfQfzQXP5oEi-BdrjjEeUdS2iYiB1iTCnvEuvxGYrNAiyVhVfSYkt2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=nT1FAVLiY_m0FdixZVObFtfUi9CmZwqjYRvG1_60BHiz9nXEtnn-qMqi-2hOmT1cxTjWGs8MMFf2qMyIe_3JblPA2wIwB-KI10_b_W_kz49EWch6m8nAwVtA_cni3EPDdsF5EBItKAj4NxVwd_0qfnQ80RMa4Nte9UrCDTvY8b4vKzZ7m_M_Fa7szTWgxqZocCrHRGzJwyW_oiiVsiM3GbjlQVTVSFFiIQ0_0Bg4TsdQ2MOAXf8sdx3Xz5kRYn0nsI7UpVS0lLxfArDR2YCVm80IJgnl37K7KyyQ_3YXuziSrTb-eDb-pWHsdegufra-vI7sRvxZZHIi8p6h4No4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=nT1FAVLiY_m0FdixZVObFtfUi9CmZwqjYRvG1_60BHiz9nXEtnn-qMqi-2hOmT1cxTjWGs8MMFf2qMyIe_3JblPA2wIwB-KI10_b_W_kz49EWch6m8nAwVtA_cni3EPDdsF5EBItKAj4NxVwd_0qfnQ80RMa4Nte9UrCDTvY8b4vKzZ7m_M_Fa7szTWgxqZocCrHRGzJwyW_oiiVsiM3GbjlQVTVSFFiIQ0_0Bg4TsdQ2MOAXf8sdx3Xz5kRYn0nsI7UpVS0lLxfArDR2YCVm80IJgnl37K7KyyQ_3YXuziSrTb-eDb-pWHsdegufra-vI7sRvxZZHIi8p6h4No4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=meNYaio37DiYoQpjPqrYRhKaucy0RVXh8-VvROO5PpTR0yhnaX-0lLCVoF52M_JJ-A5uSx6bkUwP3hq_BctaePz0lF220bjSywfgubDcydu5IOhyFqi-Vf96fosFVM_LEpNWVJmlPdX6W7Y8jwQTaAmnSjWGsJjr_aOxKqVSvzS8-bmxLvwOr0Hqbde9PhzAMVmkpFoBndoQy6j7NhpfM51uILZJjKu6NbFcNTDz6dn5PQ5bdij0iwc3mSaAhDvQX05_P_rv_XXEEajLSbNA7tr00Xq0CZAjSTYst_1UOvGyQ6kT-wfx7jTTFJKXpaUtyY_3g02OMcng56M0QbfMsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=meNYaio37DiYoQpjPqrYRhKaucy0RVXh8-VvROO5PpTR0yhnaX-0lLCVoF52M_JJ-A5uSx6bkUwP3hq_BctaePz0lF220bjSywfgubDcydu5IOhyFqi-Vf96fosFVM_LEpNWVJmlPdX6W7Y8jwQTaAmnSjWGsJjr_aOxKqVSvzS8-bmxLvwOr0Hqbde9PhzAMVmkpFoBndoQy6j7NhpfM51uILZJjKu6NbFcNTDz6dn5PQ5bdij0iwc3mSaAhDvQX05_P_rv_XXEEajLSbNA7tr00Xq0CZAjSTYst_1UOvGyQ6kT-wfx7jTTFJKXpaUtyY_3g02OMcng56M0QbfMsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6fYVQ7wQXnIuEfS47_AhOv_ICz5BfMVaUn2hlQKHWriHF0e1Iy0aYpRU2ziNyows1rF9pwo1n8CDekf8-FloWUrqVTqh-PbFkr6kuBk5ieSasnkkTzdpYFnevgk7Ya9EGsZcr-XzKyDjDey4s5Uum8mupl93Bw48i_0F4DLubZwjSJ14bH_2dfuT-JE4zvbyC7xoRmA1Ks2ZnyGRwIqeqPLb9BANnSon4-JsBNKO8pkpQggG20CmVBMEaAwSclfWfUu05ktTLxEvKZ0vuENQoi5eESheeQUbM0thCZQ8FADiF7JB0Uc4pdso5_XKV1bAOh6a7PCkFI8T7CegNvC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPk4c2IVNnbYhq3A8oF_NeT5Pf7cBXpl1DUAsDwHNLvoqyG0UC0eFPsWOWqGIMk_zYWkYD7oXzYGNH92kJ8zBPC3TbWlaS_fDGOCnRUtTrM4CLIR3x-or555GTULLDqqIZWDrIex_MeOp1vpJkZ1bgj6_pwKiGqDqoJwgk6_V-U-l53DVmBYrlp9Gj7qWKERgVAXKEdZBcN8DRAiVoA8oMxOQcMqHdamPDGXVYA97scdFjO-Y3b2XHFQzr67A84dZzK5QSn0ocsfOLP1wbEmiW0OqkctiDxO8YT0DxIauClM5M9kTtl4e7BQtUc9t1aHz-HnvcNG-KTijwy672B0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9pLi7hXVqobsWP3sDZXRo2cPUhr17jn9y6DYV5WW-lTyfosHJjiGTAnGoNupjZXvLi_MIQawRwVIDE7gaiqMcINw1CpPpfyNyOCuHaAZ2_OD94bSkrdUhCJNwF8yGw86fc9EfQWIXN93X4e3pleoj4Tvtz6z-w_pazXo5YgetiM2lLfZz_aMrUX4Ot9G-SLJrmd22helnYSZxdZdFn5GpFsdybDbZOlirX9GKzcM5uRGv2rlCZnXV3v4-DV3fRUDBNLoDMEBrYoLDFB-0SGIeMWrPCLr1C1fe9vIfMl2CfjbUUidcZVzMOz7wy-lVacU6q_KosiBw0H2xJt505mWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZC8uHx_6sABQkuELvDqJYg49U6NkqspRvjEb1azcN_Kl6dlnuodz_m6CzuOt_GiLHyjY-tlEe9PQPm0gtz2RG3ZgTVfCLmZwNiQOID507FfhwZrSijdlvwBPxduUndsbzfPu4vqSxnS1Kn-E-4IX5xb1LbSXMYVXt3oMt2az_xvcgMrggwyPMsrygjzGLEeJTpz7nOFBYGdBCHnO-j4mMTumZ6b-dIsDQMeqlmyNbkjbXknBPet6Ow6FJvUuMqYG69OpXYSJ469SagtcGgzJZ4FB4FDUoRE9CeOzULWJoci-hX9Scbg2TesbPEtlcl-dm87XtPP7SLehI6QdptNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZxeqGg-zggaO8-I8QlvX1rHR7X_RYo5yQS4twHcys_OC5AN-hm8nYysWy8OsUe1GHn_2KI_nWYZJD366bBnZVZebTnDXV28AKVpKKegOAjHy9z22AbrKh8-pCKRixbEY8r4idMPMOY8arZALXfzSFRs3CZRsuan-kEkOARsPFMTyiNxgmWgOcNZn9_lPwxSxsuxpsnM9nSw5GtFkArfJ_ENn8vwS5HiTmQkVVxYtnwTly74ka4NgcGiT9EkcuiSeBOrnslYdJ1PSCsv4eny0jq76vfAMZojOEfB2ouLEVjHTK7S_9lmHS-ouhMfZ8m47GxQHmIEMpCD6dvbjmZRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvxQO2fa_XPgmXIIqSKC4tF7OMuvNghM6vQ6-ngSwU8X1f3GlGbg1dJnGh_UDKEZvPuernNUBuU_k_qdBtHcEs-WhVQRzkGDCf6t3tzEehkD4EZfQbDXFVdBwMwmqLYuuIDfDqd8BPgsy-GdC5UXSE_tENZZfvtFxGTX7B3-GuQBUV0X7vY0kFaVVqU2gMwTp0r5hOP_6KQJJfb6o2wEPV_m9TYnc533cts37QQE-agf9wZsZgvDY3PPk4O0rok10z_RZEhH6D9UG8mRdKx4gjuE9lcB7Yg_kDwZnFYaGk1QhqfhOmjnls-IP6C5yqpE5_ngzMTI06gbcxDjHGXgWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni8sY-y6Jgw1_AtTQY-GhRtFN3Sw3KByAeis3pruEKtA-26XCfOtFXTdeW7ucXB4WD1IpiEJTqI2OB8HEEHUDodPO6WCOvUlZKV4LlKT2NEgb2n2QAPN5Jgsvjd_Q3qAdwx2M4nvlZyrGNlAw6puaPhKu0LiqBLshKwQNmFdWxn71AjnCD-2Yv1QPWqAWK65LzdhgMGn5HZnn-ZOjJeeUIjL-t9-q4WR0ZnX6v0XKQkYRUfprDev0RU7lGIdvVL2T6snLx2AKwn45iZ7RkQXKxAo_-h6iNqUoae3xY0-TmSuBGWC3018qdNDY36Zp6CXBvrzHJPk6z0UePufsGlMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpvY7dWuF32xK6xaCxVFUbPtG2f0b0KqXJZ_EmwcQEX2R-J2ziXhHIwXXGazYzYbQ11gJPM0m61KN1Y3F6UpESEsixqxaKd3o-MhaIsphEk7ljx0TfFhocZBYoTRU7BFRy78zYR_aNkVal2YtJMOtr4lKKADvRY6_6JGgfKQITxl1nUAUNlY4lvqsojFUNF2IgTExsUeTf6bhqKQkrxldjrtIxk9hGFEkUNuziy_bwHsellPGpDJyyfRmKoMwtqdGzhoL13ScwPCylOnlv3eYlCgW1v6-JN7L1WP4dfhGtNSr5IMQD9hEnaS4AGdr3ibbNq6tdna725XJhxXcFLfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABCfMI3nMvCqkJBtMk_tKERwTiFkqldYvZXq2ie5gcADvhwk7jZRW2KvXBisOigrsxHup70EKHRreHtb-kbl7i1Duay5ln7nU4o3H7G0diKSxSd2M4o-TV9yWlZz4ruwVpPVqKH4zIfwleI2my_JcT8sIcbH8ydCFrK4rhMr_u6XD2nHMmDAjOr7m23drbDOh6ZVBPPn9i6LlNPDFme0a-DafSqy88qEAwumhtnE6cx5qY_T_4qtGFPyp0ya18465bPPuvqzVVqd7kCUFru4mv9uTMdCAY1XQABvupem0d0QfASTCX58_3BUsBUMdlovXkb5XVMKK1MY_nY8D7NpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFSnWbHBIr4k9sgNrEnnbsoGdsnv3nAvDYrp-ZBlqdlHDotwXQOm-PEsALSfEivb__DJtnMA6n6hD8RIKbAaduvy5YU9A4JceyB8gnQIB9Z5OO4fuqamTkCEQ5I6_ZW2S2gGQf8rengQHEfqldXADAOuq7qlaxG9JeESyGvOYao8MIdRw9uqJI7_hZ3a1hohgpVfSRLAP6Nm2NRY2pnf-61erv6q9h5vSwZLGnTuvnnc9NT6XHsf3LVC82O1woXMOzKC68wvlDH50l8rrmeLOe-kAYUgOCwZjpBVdvCkTtkrTHUO_LbbI_pgakZZVvUKpAj9CXmD5kXhVzCKT6LmCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/locFMYTnzJHhuWT9ANXsOfSJmXPwdukqSwptERGNnIgIL1meh3MbSmYXhwFjyD6rCXl1PJT-v31msm3QOvTGVZ35WBeUHvYoh3zzcRnzx4BoB6jHaGPpxCGFcfjyC-NvBXOtB94BZJcJ7dWvHERRfLyUdLNxTM1UO6TLujfApvdJ9rucgsw3utF6D7aI2qd8EdPAygRvHSP_F2AA4txbk5QUZx_dg9RQIH-c5siYuuS9J9jKte_Frx7D06uh8YSidU7UkpuwJdTxIn5AH6OJjHwcsOMmbCYigTqRX-ENLsXJD_gK9Lr5iHm0zg6Jc2gjAJXGxDc2GFQbaUVMs5MNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5mSjHSGiLwzC2maAc0so5sgObu9OaarFDVz4DPLweGL5hk0PIfXzCLWX0ksd0e5g_5DxY3LR7GqjgIH8GFnLLvEI0KSaXx-WGfQcwgH98bPboNaQ2BlNdO5ghfS1G6OTrQtoKA77iYVpEIszdwelr7p2X8lh13e4F9r9-CD8nY8z-H9IACl6CVfDiQyjrdkNz1OaIqiaPHt0tXOcVE5uML4DfuF865tLcGQSPndBuLrVu4OgrTc3eCDpfBMTtQjbvFAbVctppnKRjxZTfcijAqFFJ82ZYryzDa36hVduDOzXHKIaA7b7j449z0t-ePu213FeztuMZLIXMuuCX2aSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=ZgrMUBLC9P40CVfMJvwKlWepqPzSb6C0UG2f6GYffBZn9yxdaCUerjPeykzWJaEBAg76S7Dsbam2dV5zkdI5D-Ce_sbeoNYRRHYS4KAzud9YNG5bghsAfRwesjn8ulMOSLX3vlDPSMMoOsNGGKkaNMoo-d2SQtWbxrZzw1ijNnmSNFBZJpsxCtMeIwRVGYWduwZbXtmaXYjfWXSTr5IuW46QDEAYsq7lYQ3D6VOCdaEui-2FO0QGay7LFfS7cjL4bthoqbXslM5ifD-F__4DmJFiwqzxEc3eC18JFZZ1JDOjwa3hzcoTcCO7d01L0bJCwuTUXi-LaS3d4S-YA3FGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=ZgrMUBLC9P40CVfMJvwKlWepqPzSb6C0UG2f6GYffBZn9yxdaCUerjPeykzWJaEBAg76S7Dsbam2dV5zkdI5D-Ce_sbeoNYRRHYS4KAzud9YNG5bghsAfRwesjn8ulMOSLX3vlDPSMMoOsNGGKkaNMoo-d2SQtWbxrZzw1ijNnmSNFBZJpsxCtMeIwRVGYWduwZbXtmaXYjfWXSTr5IuW46QDEAYsq7lYQ3D6VOCdaEui-2FO0QGay7LFfS7cjL4bthoqbXslM5ifD-F__4DmJFiwqzxEc3eC18JFZZ1JDOjwa3hzcoTcCO7d01L0bJCwuTUXi-LaS3d4S-YA3FGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=v4SywDdOXadjMm5l6oSokOdux3CKKBetCy1R2g-nemvSRh2G5ag4d3tyn1nYhU6uNjBVytnT3h2wW5fvPpNxslzeBgNeIQeckwzJazxcfObHfWYLjDiRvS85_TrqPGHMFAGOAuOzL8_JcydyQtKsvQQ8e7pjWxTJYhFvMut_pVP2P85dLWgy93nAMQ8oN309hOY-Ff9_53zKn8CcCvSGia80W8Nb953RqOlvKVRCbE8y21EY3z1_t7G7sCJZIyCDvQIV54YNpbUvcKGqBKQxUcAFHjI3D-sIo8-zTv_25lmMWTAgD2A_8FjnNRGa2Etx1ag6d6XPStJlkVwo2tfEzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=v4SywDdOXadjMm5l6oSokOdux3CKKBetCy1R2g-nemvSRh2G5ag4d3tyn1nYhU6uNjBVytnT3h2wW5fvPpNxslzeBgNeIQeckwzJazxcfObHfWYLjDiRvS85_TrqPGHMFAGOAuOzL8_JcydyQtKsvQQ8e7pjWxTJYhFvMut_pVP2P85dLWgy93nAMQ8oN309hOY-Ff9_53zKn8CcCvSGia80W8Nb953RqOlvKVRCbE8y21EY3z1_t7G7sCJZIyCDvQIV54YNpbUvcKGqBKQxUcAFHjI3D-sIo8-zTv_25lmMWTAgD2A_8FjnNRGa2Etx1ag6d6XPStJlkVwo2tfEzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=liF7ciWZNGNr1BstxM5YubICXYIoc23yo9hv--XO6x3VSJIxj0rEQwLG4mVAA2gJzTJq9TRcmhxQM7sgH7T-xLwrbm7isXBY1I13mGOGZs8GM3zBhwAVhHLl2DTBiwTRCGcFxfrbp9NnT0q0gJoIFSVok0_Bi4cfyA0isnVcpAPn7jyFrdEOqQ8_x7YA4dcHVc3CfmCAVtFzgZMFvU0c8rK8zciN-eiVM933H0o5QT5ZYsEzEjyZIstLJnfIX3rDj9ZPao-L0JEIv5MIMKxZG3TddLEiaTbquuPW_ar9LH5PrZmbyoC88XWRjtnplAqcU3GrcFVPf5Ce1VhQzWcvKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=liF7ciWZNGNr1BstxM5YubICXYIoc23yo9hv--XO6x3VSJIxj0rEQwLG4mVAA2gJzTJq9TRcmhxQM7sgH7T-xLwrbm7isXBY1I13mGOGZs8GM3zBhwAVhHLl2DTBiwTRCGcFxfrbp9NnT0q0gJoIFSVok0_Bi4cfyA0isnVcpAPn7jyFrdEOqQ8_x7YA4dcHVc3CfmCAVtFzgZMFvU0c8rK8zciN-eiVM933H0o5QT5ZYsEzEjyZIstLJnfIX3rDj9ZPao-L0JEIv5MIMKxZG3TddLEiaTbquuPW_ar9LH5PrZmbyoC88XWRjtnplAqcU3GrcFVPf5Ce1VhQzWcvKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VldAEA5QXhxxt7AoC76aKWYuy9DuYb30vrg7DvySlTyTAC378s3axZrq7vU3HUVRaysTRfcM1fYxMp2AHvE8K5vHPgsqIbMqSX9-0ZSR-qGdI0U783_xadif_dwcURQ7IdgnakdlJ-sPI3wjU89Rcleah47He7ILiy4mAP8Qny_Hk6zReVbwzKQ4ARAJt11m7jW25xPXuwn0QTUV3v_mHiFDILIrb8QJEoVwaEcRqaT-UjxluJFcRJoAmC43BPzaQqoqDUlF24RLyY0gSJ-bOeEQ0mLI07psE-RbIx9cxAhRFbLml0MCQVDL1MzIokmk7mhdQ7pzKhmAmD4022BDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx_yrQ3lKg_tSSLHpGR_n-LwX0yXqEK7_YcG9ZtFWN0scjbu7W2Fvo6k665oyMnDOmfeUwzWwPeUmjtibuWd_pl340cKnl9-2y4DhJmbditrhbA3yCWTGMWKDy_gmd6DTC_y35_mN4O_7DCVtkajjTqAdtOzeTFM0ia2-OUX0z_vkOU6sh6Z4jrxeYlWdGMoyzXHUjcMCI_KypZyXZq1jlDURfFUctMoRLuxFKpECbVSPzHli9QDtWJ2xoG_a1DZE6pwpxc-6Jh8fqMbW_Vlz_nbRP7owUUEb9LPOx7sss163KEhiNB8GVZi5bUbIjxeDxZSGCrvOrzF9bWKLTLtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6GOFfENB0TShNb0nrQ6gpuCv9qB3CC7_wi3bUKSfVI_uxMBYcJ8IgOGu76PmIHSSmG-9HTw1UMURBSI024zLyTpdnbwxAHrsKCmytz7XWytpyDW3jU4wxtxmAJDWbbZUHjVvGh05QH1eRDTmMN7idIjBOds9JGlY3LeevXGXH1PrBhxZTBC6Q0KtIqek5Vti6IlrAPDce8Aa8CMnvT8OJSITxzn8jgff4NHuswmY_e3HBzYSXBQLwXZbFmy-PsSwVqfOuFlwX7xsh0JsaaVZp5fCs_uiM6dlXKAzxmmXZ4MFVW8S41Kvxo8ysBtz69ZFd9vbI-C0rERbLBPPi_IzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=mlSsOLVABTvmIgcdYA9t6Ar8XByqKQ_bZzv3E-bHS8pm1YeXSUm6AI6GT75Q9NnAzDcH5rXec2H4Q13wrRrS737bwbfnASMNJw4jMTxhhEXNm1SyDcIAZAyZLrtbPvDOTQDgBbKD4fgt1eWv5rJfWjh_On70iLr61dIdZ6iOVdOqvHNz9oWdcvwe21aUbLK8ys6XSuqSzzZSLw5IuIJueZmENMS761OqhEgWE4mJs_Pdnnxw8bWXDwCiKxibqZ7V_LPRiJE5ouq2DKcWIm47e_PcwLLZCM05yPf3vgHcafDeRyTrDxAPTdngfYUJl6J82jWdb7jgI7aUGdH7bfRlaRRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=mlSsOLVABTvmIgcdYA9t6Ar8XByqKQ_bZzv3E-bHS8pm1YeXSUm6AI6GT75Q9NnAzDcH5rXec2H4Q13wrRrS737bwbfnASMNJw4jMTxhhEXNm1SyDcIAZAyZLrtbPvDOTQDgBbKD4fgt1eWv5rJfWjh_On70iLr61dIdZ6iOVdOqvHNz9oWdcvwe21aUbLK8ys6XSuqSzzZSLw5IuIJueZmENMS761OqhEgWE4mJs_Pdnnxw8bWXDwCiKxibqZ7V_LPRiJE5ouq2DKcWIm47e_PcwLLZCM05yPf3vgHcafDeRyTrDxAPTdngfYUJl6J82jWdb7jgI7aUGdH7bfRlaRRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5g_t5dH7JxXFl2-gSR_vAW1UR0qAvu1Bj4FnYeeK7Kvcv16ANZPEiZ12duBlU-7X2IH8339HlBTa-IXXuQhcGp7K48j4nx3qTeH2moA7MzBVee1W4uK9yADvhvTZB0uAAbEjRQGezF-1DPc3BOwrx0k7f5s9xW5wsT3maH8JToB2nkAF6xASyWM2ZAw408kBjOXCIey9J3vpC1G6aa48dLOeqJbLgF7ygy6FZIsybDvNCeoWvvN3Cn4RvU1INabh6SbLqfVCMZRgCumOgMoQ2mEKvSytCGlAv2cQ9iz-yUoTbEceB0ks-Fv7j8wstwDcEj6xzUwlX5W4N8z_AUmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeH6Q65yr235kWKEfm-VMRJ3J_Gru7tFLOEZ7urFg8jX_HmNcf3_aXVAjvG6xd9A6BW8n1_m6gh3ldp4Nwdbs_Gi0QIfqCn-GVBV4UuWd2GMtvCPEkM7P0qQCMaNUMMCLgJfW4KUSIzxFDNgTdcSe5KIRizl33N5pQa7MHVXUg6XJ1q_ys1o1pylaUNuKKUFRykLiYhKlWskvS_GYv1iEvyN-brulNl2UX9uuDmu1DVlc88BQaPiAkp_DasMAw-Llr0_oNI36bMoBcRATLtyMVj9IMuQ51dgriTb7tKgE2rFVhPOXhtPPrR6hXAfS10hm7EByucxR70kAUToBlu4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4usR6GdkJSYinh-8CHBDv98Ad6zuyZoRpkF19JIsIz0govRrxfV11_wENgzk8KbL09QwTS-aQVn-NcwtASX7QHVCpeySUPJkwdZw9Eta8H-86vzcb3367VIK7dDVYw68pq91AI5h7GLRXZg_GhMdWUt4yqsr9iA-JT_Kqe64wzKrxh-6MMI-iygiLcH8Va-gg55o6URzvxexQK4KqFMeuxdAPTsliJ8l0vTgdfngKpPZ1nG5Wc_LAmxjIBcUZEwY1qC60PIHQueVwn-PRkK32PKy_34miw3M9IAKjEcEybNOWEpxraOL8Y9o6IG5FsNZNAMCBGGerAfhLrA3giCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFUuVlQZjS9eSC6voU6wzoVc-7rsBfQj97zPGyT0OWVqvlR2_vvISWNf-WNI6ypgkytbmdJT_JYv6nGXfmBweRr6nQhIEDOC4FBzFqzn3aFCZs2Tf5OyrFdTMxWh4ESKqDUzBhCQnZeEocN__rLNidG7NjSmtUoA_vUZMG0K9xmAqeUJBztdkhw3_x1KN0uU-elEUa0DczJdRbeCcMjobtU4F4JG3oYt-ixO2OD_Q_UIECqLvZC2qVb62OijILV5s4Q6WCWM2LV2IHigJc6c1cBRN70oCkpH7bipyH9uHhP1ksVU03NbnPYb_yz4DPYr_Yry-Xg3u-u0FTwMijajKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLdMmANx_wJw2Ah_pOql1sIZkUtK5Z0-O1QE979H2xpw3yrAJzxyCLjerckhQfvIS_7lJpOHfhXxIOJBSM2JDnfEXc8srQU5uki9VKcbnKaxp9O1klwbB_1fuAoF9HoIiPMLIkEP-YXfou2Wpuu1CsiH28mUN7qe89mV427eSZwKXf6z_-cRY5jacdCAT83Lrdl244DA9iRDrjzUFx0tWWuPl-N7qGf9w0pnT4yzhbWG1LNCJepP_cIiP3nbTCidGXc-kc02X5_RGIQNH5LV6kkbT7_qmHF5PIxSiSnl_b_SdpvQVnazWOIJD2HBC66gACFzfJHWigxDZENEJo0cUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8cSC1sepfb4a18b1YzdBrPYLswTYgm30fy3a2kn450uOr3psq6v7PLXceKK_iehLDJfzZPpDCDwr_9GgB867bHnPIjW6naUk7LK4onsob8k4gpDnBWf_GRg0jtQ2yKZ4y3ty3f1QcmnfQO04PBwwUEH6T5JhNH97fN8fc_WaWKtJvudrsin23zm8vcXdg1uMN5BTQy_mmk5vOjgi1j9QRcd-CLrcB5iFzXqinvOu5VX3W74sLB6UxVHB7M5qOFNvUcVW8j_cCChcHq_htC14LpWLrL2r4Hjbi16REGgxeKvEr6hgp_9NfmhpMBBEBIsNeH-ztTwlrXyDsmYu3roEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtpaPwhyoQzOnIH7sISEKrmO0Wkgqmvr4mNaGaYXIUmD11PlRXxDYTxquL7VQGqVCh9_ZoEdMfPOd7vUUNVejZNW-x5Els73dUTlQv5j_NdkVP1y7tpVSy1y3pAj8Cz6I1Y41V340WC1MBdGKo3FVFKcMQ60fC14TeMeZRKuOzPj-P4hI6WSP34NkDgEw_dw176cfiurSgFSBS8o1pXPgVZ8DmdjjOhBy5D9ettI73z654iRcOVzVh4zgo5zIpptKy_LLPTgbHkt_WQmM7C0NpNVvi8mtI93K9N3EjHHETny1Ws3tIDBNLr6RGSIwU2b6_6TU5bB_9gPt7et6xkj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cvlf80hVJ7SKN_6k3fhMZR4cH2lq3QQZ41j3tM4_0x_BjNmduh3JR13eyPqMBpki7mhodtIKvCsJnyvzAtT0_EFt_mjgiMj6qBrMAOzFu7igmSEZL80oV9WrcvcFULmEPjKP9fGCbR6NfSqYAYJ8EB8VhbEJBvWfqF3o1fRJGZsTRQhU9uNQb_hz9EkiiKsHzD8QjXiF_F7MX3k1O_kw-I1Bz0HJUVI3MqLf2WgP-cIm-BI35Ni00Sakcx8iodRpynb1GrU4ryAigprJAgec1ybvFICB8f0ue5S5MrH2m6bWdeMlhsjRmtm8_09ustZ5R_nb_mrj9QBfA4i_4fDn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geX2Evbvw1xL7uECTySJu6uWu1fD1sFxLIQodfluZcsTV0ZTHj0oa__UIZyt0yKBYQf_fb2CPWnVkTd9pcMXXvwGV7uZso11vvycjP1am1CxoS8Z5KEEVu4lPx_lXMOv-wdtXR4lGPFNT78-1_qtlGi950XPUgFyX36j0Ssz_PWUnqZzz7Oj52ZU2IlFcc9cvAyOvIIkY5iSqlpJs3QYJCZpOmPAaDr-bKDmCRJbgszUKpEmlgmLeEX_auaPeGKLwH_VQkX9WZRW2psts-padxa2QlHbC4IGfeCeCqysQOtpiWmi6uQFqtlxWvow_9uJeOmuQYIBpq0PAsVTzaMEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6Qrx9wrBwgldVHJQuDqAPLzZ0In3Tm7W2b1X2_WkPpYA2T5RTLTJMrKuUkOShNYXixOQFA4RRHiNr68ab7ietIlQxadc1MIk8RJrEQOB5HH8cDLhk9DuRWhEdL2Eb-pXdWJyxcpRBj3LJUXTd8SAmJFMaLnlULTj30pcHtE1BizJ2v73ITNo4oQZtlZl_DZKVO8x8fQtUkC__JxrkzUHv_yyqtdeAUHdVjDQylC3NGRAhgGRUeMWPSEY19jqmRknksT4VV3kCaklgXUo28vqy-mMzA6SSv3g-LdSVBkyDSHyfyKWEQjVwOJqVc2JGvU1Uhc9p85fR_n11_DM2FmXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sirmvF7QmVtbphi1LviFbMi1nYMdlwB2oovyyESi-8GFWlG9vDJ0LMt1zXTlxoig1wvOaNqR3l7UG_LUexNofbSAEsp7nsZgpHEUKgiXx72SWCt44E3CgQjp1KBqx-Konu9TZg9UjVlQzOvXJcqLcoe4XeC2lSeleShPFhvIUksu7-aV8th2GZIRyVKQ168IJ7PvOuSKe5NOmxjULSSRJ82q4qWusa1O916xWHCAuNBCjsuiA7RA6B56T_wF6BvIu8x1EZonSaNAdWaGhAFKfSWPTPVAwHJFim-grScL7eiDXnp4Nvi3NadKq7dd-gqMW8mfdlcu2aG9obV9LTKovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=h4OArDOk5Y_3szmKg4WGYSLoV-ELWArtykx7qhoRGxCfv49S1NaT6hdo5Njny5zzosK3kyE9M04G1bbFtGX3uSB-sLBoUxCszGx1SifJ0PoU9XwIBBiC3t-Diy-WcyTgLPMu71i_pyeYQy7SRO1tahOzXcWs57IKdtTmcRGAF6xnRACO-QDj2eU6GqKWGiKuDovjt0l1_z4yIWhvtWJb6IEdpW_muvjYzPYY4nkwKxm82FNIL74Z0z81p4YOkD0L-BkdcWg4AxmoeVtgVFdkwE3suOkhANwpQQw4eF5Jo1V0_HNSipjZqV_-HoPnciDjb5xfS5FVG5JNSn0Ip8SI7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=h4OArDOk5Y_3szmKg4WGYSLoV-ELWArtykx7qhoRGxCfv49S1NaT6hdo5Njny5zzosK3kyE9M04G1bbFtGX3uSB-sLBoUxCszGx1SifJ0PoU9XwIBBiC3t-Diy-WcyTgLPMu71i_pyeYQy7SRO1tahOzXcWs57IKdtTmcRGAF6xnRACO-QDj2eU6GqKWGiKuDovjt0l1_z4yIWhvtWJb6IEdpW_muvjYzPYY4nkwKxm82FNIL74Z0z81p4YOkD0L-BkdcWg4AxmoeVtgVFdkwE3suOkhANwpQQw4eF5Jo1V0_HNSipjZqV_-HoPnciDjb5xfS5FVG5JNSn0Ip8SI7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=X9C2slqXfyW-GLWJ5-ObqW4_YjzR0EATL6doVSd2WMclJ-ziMc-e2FGLP0R7NA0zfaceAmd9BtpGIT_x00_yvceiIvbb3WM31fLbDviY4UBMejX4vzbdbvzX3XBCbomz5pbbTYPyCfuj8aU0Oq77s4GDKwq-kd49H3iPICdsypJ4RrF57UpC3fcoaEaATR6pzb-KKaoM1ZwS90oietYNupVhdgfVdK0HHMhMIbvsogzpEmqy-y6hqPTnezPR1iM8FbY4Na5BEZWPdjrChpCl5pZ6CMY4-1Knduw35QmHLaMIOXDlQWYPn0xWIKxC1wI4RvXh39bJZ5IJR7LeEDXV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=X9C2slqXfyW-GLWJ5-ObqW4_YjzR0EATL6doVSd2WMclJ-ziMc-e2FGLP0R7NA0zfaceAmd9BtpGIT_x00_yvceiIvbb3WM31fLbDviY4UBMejX4vzbdbvzX3XBCbomz5pbbTYPyCfuj8aU0Oq77s4GDKwq-kd49H3iPICdsypJ4RrF57UpC3fcoaEaATR6pzb-KKaoM1ZwS90oietYNupVhdgfVdK0HHMhMIbvsogzpEmqy-y6hqPTnezPR1iM8FbY4Na5BEZWPdjrChpCl5pZ6CMY4-1Knduw35QmHLaMIOXDlQWYPn0xWIKxC1wI4RvXh39bJZ5IJR7LeEDXV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tre9UKjFJ5klkoZby1bLTAPMpmE9SfaHcm-GStSIc7-3SkJFy4O8cmUtb33ffQAwSAYbZ7-yRQabLnZp3-kPia0KIWzc6D73y4g34E-F2hLPhNQeilYpLsK9Be0J9UVueFs-CyNssfRzwmxwdEAih-1TYu9G45lVSOetbIHhGp9bvOfL9HyDImxqqUn2r2i-fWFp0GdfO452dc2JKtlK64yf0uXr_UdGlOWUmpPm2yjJSszKNIcD78n9SiCCsMBkxd3Axhwt6gk-DZ56VgIe223zz5VzuhdMuVAmkhRCzWQRMcDZCqchcgoKBGVKVbtkhoPgyej592WxyR42PC9O1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3VuIEB0ruBOiY0QWKMaQ-QQkcy9iXcf6kY01bNRp1x1x1A5eqZDzwLORHze1u8ODBmu54k6GP0ENnFcAkqezC4Ejjv0Jn_3kjYF-dheWLPcc13AzuWR_PVXZMwr7iS4j5oECjcIbj6fSkySKjLj9B1nKgRtGo_xWNU6Viy2Qv8AJRDJCSescenfMj6zT5h4I4634IyZkZaNOxgywUCO1KkWnPdovlHvGRYBCGuaJiEKNVy3mNYnQaKMTPT4gKp4GSg64mvR9alBYZ09vBiWIo_zA6yOpHfKoZr0PbID9OG-ggknog3aXGwXkQbV0F63hKYhlkHYaEHIxXdFvGIURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5itV_SUzKJgXii1Axumsa4IzMU65VeABnpbrEgdcXf2V15NRthqU5asSjWwRL4vmoa5XtIM5t2_og6eBu1FCPqDrvmkecGUElEUEu-uss53YItje5_n7Rz0DBLvpMBC4VMrFRq8A6rjfkwLQE78pyAiS7NqjEHFH6grpcJy-2ROIT8Bhqa7faiaLu8WQKszP9Wxj-F6sFJGnr9A7Skp-ZiUzQtZy28M_aEfflE6-xurkiaGhjtGSlsCTYpewI_RyI9nhcxjlpf0d8dlLwwLLFLYxf6OAZxq45iLjev_E20T3L-hiG7ME147x-ABXgzgNWgk32S974rnSYuJK2TLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q13f71YFszlZjVp9niIgbOF_yrn9_Wf1p_2vFUVuWGodb1Gtt-fopUvfmIsmHE6srAa8fEPcANnf77KNhdNyJaGDZFpFJ9IjkSZvLDMOvPyx3po3z7ZXplvNZ1h9Vtxajv7TQxL0x178GdAk9ZT0U6gLrsE_j2a3-iWsqLkm3owJ1dF_9r1733MzgC7HjbSJOl_0Bcss-FWo9wuiuXcyQyjV-h1ndcJhr2oup5zqvAzb0Fewsgsw35GIL1tSEEEw-LoMyNgSvQ5lFeX5qw_WtjDe8qvUWGewoaEeDDKQ4DkmNsl214c2UzAO0NkGZRB37-EHzVeyVN-CBkhycQ4D_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
