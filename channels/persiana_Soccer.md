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
<img src="https://cdn4.telesco.pe/file/hpFo2wrsVScXtoLNBn4KgqatEA8M7NqeZ3xD9aaDmuo5kRVjzTjZ3u2Bg0i1aN9pxpQFX0w_3cLK_Fz2mO8xB4kncKvmG_JajoJ4ZRzVLoFbdr_KTR5dLLgu7kB_wpCdBKwgdtB342-rqcijAR_0NFfPB7Zi_cxfTYB2BnQkpk3-Knnn0Z6mmbcUN73u-Mi35dJaLbzpmy3HZtMsRreqwPQwHTaJGiBIL9MYVpm8qs2EP18mAQTPd4nbS0sO3W8h-14PberAHR3Ja3rj7zVTel388fxbDpficzBVu7JwYCH108nYLAB6MHThSCNpCHR59FvHy6orjsgpqFB_JWXCjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 295K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r77AD4hT-Kr-P6RfRG4i1jEUHncgWm7UXSuGsXNMU2O8gzwN_lEe-_2eE_kg2MZxtv04y8dDdwBBpcwqzgB-sOakhtB01fUlc10qYMhNaLN0vxSaJGGo36-65nNE88dJjMSBndHUQBZc2VuegxjnpHCA4mjKv41usibg4oO38l4Xr8uqSU5cBY7rTKYodmm2sR8OaROL2qBeHIuYuhAl58OcTaf5MxIZMaEO2FVGGzWn5fMf5Sh5HxyfUzRelVosCktctvYYMx3Kdue_pfiy2IGi7mocvHYWQzZ6-Ld-y__WrQqXAv_CYpXW0rm0qUmVzNq8zlYZZ_UukLW7-pwM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/persiana_Soccer/23545" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAX8K-N88EKee8bUJDptTjx26kLXNQ1F4OMD2U8c19lUuvef-kydmQRQOOPUfyoZHZ6gHZiTI5AWLJ2J_Khdb_29ijMbI0mePuuKsgtmjlzfis3BY8PnH6zaujYgNJYlaxLurkKKl3aF8wiOzGbGJ1_eXrWdva418gQFAY33NLirh3baefixDqgcEsU3z9NDTN9v8hDNFhmWoCIAK6seEaOGaVKQBzgCl9h_wysaMHbT6N_GOOJyXBCj_49PNONOJv86T2tl43DmmSyDY4XOzPOm-aIqfL825UI7LTVVj7Y6WQ3ZGwMjZthjQOVlwYQdba7ReI_GnU54SwvR2JN-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
جلسه‌نماینده کسری طاهری با دوعضو هیات مدیره باشگاه پرسپولیس دقایقی‌قبل به پایان رسید؛ ایجنت طاهری به باشگاه پرسپولیس رقم مدنظر این بازیکن روبرای عقدقراردادی ‌چهار ساله اعلام کرده و منتظر پاسخ‌نهایی مدیران این تیمه. جلسه با تاجرنیا حدود دو ساعت دیگه درسعادت‌اباد…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/23544" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSWOPGWbqjirD9fQTq3_BgTiNKzCR7lKrx079rNyVDMtbaZiN1kOYnPfUwlXGR-WMWYwcl6CVXPorY3IAhRmMEbfSEke8WacOeQRGSBQ-uSpru3SMAHc6rLQnMu0i-jn_BVuwzxOGkMhckaSQviBfev_hjzDUYP4sth38SvZuortZqjyw5mXycwsJZzB_ptFfpICo9cl07p1t5KXCpjRchkGE4hm9wiUGxdyrh5sid-alEs8yybxUJVaNVn76JQ068Cd9CjpCkXevt2zZAL2VdyiClVpkiMEWK4PIgmRoBPOAJgj0VgaPoSya4vqBQw6GpmTG6HZILmROD81U7ELxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23543" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5WHDCeybKb-d2ORaw2UKyKNAwDamk58VjWD6PfsV1tCsv-VzwggTm4UeaHT0pOJ2aeHr7E3nr0653Ui224HUXBLvJV8mu7eLzSrvXZ6OszFghYnXjniLcORGuSxeQq6OheAmkQIh2MVsTQX-i4cb4xtOaXXTMGQsLqO_Ft11z9ApO5tn0C0sQNzSLhJqQGfOPr_SEGN5NI1lS9ztjZERqa6aru2r-1o6ttFQpyWse5Lc_25MO4Z-gGpp2Ii6dhPOlGscxyjQdOKKwLRD_Q_eIVNcR8IN4sQEk4DVcPZPR5Rrrpjj_dDupTHlxwbL61N_ax3saG0H0s9muavi9UQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/23542" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGdVmIE6k6nZM3cHrKZnLwvGTE2iF8OIpo5bNNHu9BSidoEwzKVktBNl1S6BHoDEi832ieJOTO3rOIH-5ySehW_LKbBDsnqrjnlGCrxivQ2FkjpY-8ON2mTUgprsIecG9soYPbDnNIqctvRZxoRdNhVC5bXFshjPKgDCGYXdjxdzJkpBRMqZnkbyeilJP-VcLQYo98UyJ9jPvY7G46ZT0alT2xWuUby7VwbpNwIV0iby8dfVpMpu_HszX965TCGQ0sVaqkQn5I-l2yLytnbeV2irOVLYkhfEpGMKNdOonOzQFb3CQS_xlbAZRgNNicS3acWBL2EdYIVQMf5J_kB8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درو‌ازه‌بان کیپ ورد در نیمه‌اول دیدار با اسپانیا 7 سیو موفق داشت و مانع باز شدن دروازه‌ اش شد 40 سالشه و ارزشش تو مارکت تنها 50 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/23541" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYlR7UKMB_0ITmaUslJ_uVdc700ZBFDvqLpyE-EhttkOHp1u_KdtIxAsPYm4u571wa3EOIFxJvyWGb7LsfKcBo3AtpsHQSwvIcwY7sXvI1EN9U_Tbunv_DKejMexZML0RYYLS185414voyp6DU-CQuWT6swBhGnybJHzfPhOUvSO7JZ9k_WUpHH59GtrC6SvblzWcU2qtamhLvnqhKvmEhSZM0tHF7L0tm2MoaCBHAHrnMWvrYkYhtxN12uMRuEkZ1Y9ysbLWaAD7cpxVMrqVESqOUGIHqNPf77ZXxKOlJRsMzHFkb3qlC2q4aApWNMAcNiTXJL6Y-TWbdYdFEwjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/23540" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEilwdkjl51lsPP-uzFDbry3otMBWD5CwD7LpBjSBxtEgzOA_VG3AZP5Roy4ks2QWSdwSHjCyuHdStqgOTu0cF-L7NrceAozFN8w8qdINzK3RJQBJOmZKJT5Nlm68RaXVTIFpQX5gpmaGfIGfkYQFEMcP03zmkTcTQngXnZsOlw-OTCE8AkslMUQGliLjiiBtyol1Vb5weEA-J43ZYeB4fqsJIUb7ebrG-vHyqk6_-UmiZl5FFBTYeUqAETaV0GlS2Za0hj-oA70VZOv1x3Xfi5Bzz3aaImxFVOwaNWI2baK3oXlkB1hu_T4Kezy_rxwqShdgDfkQMX9nxmdkxYqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/23539" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2w9s3TWBrh7HJKzm5uf5g6dN2wT8nr082DaQK6QwCt02thB8VYRViMm5YnYgnjqWpKgVyBXlOxAaL4cVr_2CAjKXxRwj9oMjik16WNTsK-OmzVswrb-34Gcl8yGvvDV8GEEn6aZp9NBwk1gewfdQ8yXUU1j96QyGVsnqqT_TVfZp9QPHkkBPZxo6XOxRNKp_LIHmZYmBGmU9NwwtcHahLG2g_g_kyQQT_jckf2HSxQKBZuLWo9Mu6XNEJbcUr03gxWsp50QYWLRKIEQCmC6E4gUjxm2RR1GkgkbcRZoN-STYCbB7NOasNmxWPgHiw_gUK3q2N--M43p6AVrb-yuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - نیوزلند
نمونده.
🇮🇷
⚽️
🇳🇿
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
Apple Watch 11
می‌شی.
⌚️
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی
«
لینک
»
بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/23538" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaA3VK3-h81mDlIMTzMR4Qmm_52o9sWRppq2H3SIKb9jq-V4noueUinMGwz3VF4VBKzVth0CHm7_bHdzM0GrANY1_dNtH7LAogOHcWwB8ooLSX09YmpwW9KPhMsIPP4NYJdQfzWh5BxS2SZhkfSYZJiJy4k7E60qQ8r5_PNvnu76Ap4BPCv9qENPG9XZK5OlTeiodUGMDCcj9Ve4b1leI64AJskCYOU829CZLZW2pJQSkpDRNTopSSFmEPspFqxtjrDAFiKqUEAutazf8fJdEDGDNrt5Acu6--AyRlfsPFK1BVJ3xgWZMNlksjx_hbVAm22vgTF2nCyAtioH28WILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛
فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23537" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBpxpjp1lPVcrgs9ag1uTl9bQxkQSQpvUrZUWq_7eTSzkdVXixV6u0VjRL8SBRxiQZqTGtlujxpS6-Pywngf1xSnLCJThxSTpLBfh-g5u84LoGd7sBookAyuVWv7aFaCvklraW-doWpW0oixlkCUkdpUuiDzBkP8oSpM-VWTIPzL2UplcHUhe2eGDZSp3Pv5wa8NjBDConIRcvI-M14opPXeLUpp-q94UUplanRmVHtAjwzpyIxEHxMia6YFYEqJDn_-qPqvTygqgHNsfeKMeznA40-SwExVUt97PTOtaEpeT6VyNQijV8kZlxksFz79VHiWuck0aI05nv_YDbdoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/23536" target="_blank">📅 20:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JalBprcOBHgKKR90JAhPVUZ8NFh7hm_a5OLp5HoxtSoixTmSBj9erXx-te1Kf3nC3g2uSdWgp2bN_ZaRyN_BxA9B3WwOJVnXL9_BT9hX-dlUL59n1nCkn0eI6x1BXfacofL6yZe3S2LYLoWkfp207PUGWInKOAdUAeLTdFJCPKMrKI-aNJq5bYooRePJTZIYaEoiyglQ2XTpHYUQK3pGQYihrPJZ6ToKxpJd1OBUjBDnIRdEcRvty_TrgW3BOUzzwh-hyj8oLqXrZoCytRP8yCbT52DeO1dVgf_FxvBcT31KEvWVd9jdbgZUkKmu046_JEw8Qoz0VCFO2hVvDwXPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتایج‌اولین‌دیدارهای ایران در ادوار مختلف جام جهانی به‌بهانه‌دیدار بامداد فردا با تیم ملی نیوزیلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/23535" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=MzdmYdoDjb4QBNCTeoqD0GkYTfrWd5rBdkEYt7AT7I-VPFZSw9ZNu5dYYwpcLoatR-HnS3a01Z9FZEOw_1fnwSi4VMrJutYX6ubSKeUr1CJFCTDpsbDDcn8yv_KvieeLDYkBjDuTuY1L9IzMNY0zRPeKPVdIZRoETplXDlqif3UYCJoAmGnf4_9CNEeM2MB9-SSqL6Wvybd29LhqEmV539Ul1KL-cY7MgDNo_CVPvS54Gtc2LGOFbjliNz0JIixSTk_Myd_RF7csd8SgmeNFCVds8N_SOxjsz35HRf7y6yNX9fCI1J-X952zHSprCTQ62nIuBq54FMlDfn19TXx81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=MzdmYdoDjb4QBNCTeoqD0GkYTfrWd5rBdkEYt7AT7I-VPFZSw9ZNu5dYYwpcLoatR-HnS3a01Z9FZEOw_1fnwSi4VMrJutYX6ubSKeUr1CJFCTDpsbDDcn8yv_KvieeLDYkBjDuTuY1L9IzMNY0zRPeKPVdIZRoETplXDlqif3UYCJoAmGnf4_9CNEeM2MB9-SSqL6Wvybd29LhqEmV539Ul1KL-cY7MgDNo_CVPvS54Gtc2LGOFbjliNz0JIixSTk_Myd_RF7csd8SgmeNFCVds8N_SOxjsz35HRf7y6yNX9fCI1J-X952zHSprCTQ62nIuBq54FMlDfn19TXx81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/23534" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poLikZygiVCX6Wnh0Zbcn5M8AyrZStHytmZYiFYX_Pc_y84YSuul9Yd_aFXPm7zB5zSKGqC3Cbrw_N1qtmlBuwm7VMlIAsHX_LFOzz8is1Li4KTzTwAtWeBqND-Ajxw89aKk-0tmzLURMZ8jVCE_vW0EX2uQDDXYLYLMfAsHL3WOaWYf0_8lx6fN9XOWRqzgsKhu8KASSvlsrjtben7bdOEars3-UzElWrcJ4WQdb-4apITMk0UzLDJmzfXfLc5slO3GC0Nm-KydFYQwRTB7bPhslDmaC2JxYu8fay82SXTEdIZC6vY-i4W9XMbidYhZLWX7YX4PHG4YqMflPY8rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عادل فردوسی‌پور: مشکل‌پرداخت مطالبات یاسر آسانی توسط مدیریت باشگاه استقلال برطرف شده و طبق اطلاعات دریافتی ما این بازیکن فصل اینده‌نیز با پیراهن استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/23533" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEkvueTGZYa0guDtlW4Hu0oXvojMPkskcLXmmzWV5rDhjyfWhnQ14b67_SM1AQw_Ls0Lr7LiczPLuwUwOSPsWyMcic-FXvVNLi2OkbGSJAJAMMMmqC8wU6csjAT8C0QUoYgpfHaQdMZ3ofW1oT1pwDQq-ccmLIUmpB3R7VpaAmNHbvPIc4JXtvUIXVV4IrURxUElRE0MvGgeFhkNhg_g10e7AdbOaDL0S0ecWgC3i9OpBvxaZAN4zfty0xVV9KQqD_Y6BLSrDWCPlvsP7EN_nRnFkzUvvumKl2hStgQjk3fVX6JCNoAzRF10w7u4cpll3zYQusF5kC65wzGuPX-8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این نظرسنجی که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/23532" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnQAi1bPegS6jWNykF0JgLO_eyz84V5wj8l8uKC1tXnO7KnOfUbtNQ-5e0ya85shKdztBQI3VUYHoAPIMogiyWLXKmxjjjKHVtV0uupg_Pz-mrPi_A8sv72oOwEZkX-crz9p4HakLhj1tT2GFHcwkf9ErVboy5rvypLJEj2PoEQo7xlVWlpxEKORVoO4_Ch6e852fR_B5G38wU3kPfidlDVRy-2gg71anPDd-ccULhGR5ZVgEYX3lvFCzoi6-oYvenB9nLonSmOWUoFtrXqWxWGURfXrD4LR_ID5k4IlTRjMp_c5aPXs8oJN_WGK1bdOrUqyYPvlSosAnecGLMOYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23531" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=sRSDQLdQS_TKT7K2-snJ-fT079ysor1Ik3eZOB79fuuMbkGESAyNdUevjYpVUNdQQtPgMKQG-hiIJpJtlufVmUBE1yVDrf8SnlXjP5Dh2XA7WbnbmtljutHLrVS8aX89PJCEHlOuF9zNV-PLsHiG05PMNgdWHitFHvzt0djP1fL7KCbW94lDdoDO34NsE24tG0U1I2d5OPv1oeylyChLYbuBVeTZLOcjFmYncpLHY9mEoepjVOS5hT2UOsK63hrkPpRWMW8_Zv4umpjZPmTv09WMaNKnnckYb16mhpXaQ1vVR4fajoP9P9uysxO-EBEgPiZXSZkQJsa5q_dO65HhuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=sRSDQLdQS_TKT7K2-snJ-fT079ysor1Ik3eZOB79fuuMbkGESAyNdUevjYpVUNdQQtPgMKQG-hiIJpJtlufVmUBE1yVDrf8SnlXjP5Dh2XA7WbnbmtljutHLrVS8aX89PJCEHlOuF9zNV-PLsHiG05PMNgdWHitFHvzt0djP1fL7KCbW94lDdoDO34NsE24tG0U1I2d5OPv1oeylyChLYbuBVeTZLOcjFmYncpLHY9mEoepjVOS5hT2UOsK63hrkPpRWMW8_Zv4umpjZPmTv09WMaNKnnckYb16mhpXaQ1vVR4fajoP9P9uysxO-EBEgPiZXSZkQJsa5q_dO65HhuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/23530" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxfD6HlSOiVkpGzkANnlOFD5X5eWe9RzWh9Fptt1nGeh8D8dZcsgRSpwaM1tiOUHwNto6paYu6BnET1xB2oBvOeb2ersQz5njs02Fayx26fdnNPLkimzx308ZI64y1HPKnlR8sEPLmrclViVr1ZNDoFoGcgWOkrQtx8bUYL_k86TGfI55lGJbTY8QrbmYJblmg62ta0WRlcXtSB-6EH11SNvim_49hOvaocAztOKxRsd5iqhQyLclnOrnxet6GUs4yqJbQhdxkcvf63JUiNJOxuTdJPrpM61oQM6tGLfaF8ymk4M0V5A-gkequyC3KBmBzUsJPfoXIS5kQXUv8n_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد...باتاخیر چندروزه باشگاه استقلال امروز صبح مطالبات معوقه یاسر آسانی رو پرداخت کرد تا مشکلی برای ادامه فعالیت ستاره آلبانیایی ها آبی پوشان پایتخت برای فصل آینده بوجود نیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23529" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIr-zISJJhGRNBWRq6j7z-Kum9mwY34Raki-s0GPyWfsKIgfvnGCXuzS0TlKsviKLWWKepLp9F2gGi2PZ4hOgh8Ual0u4BDdjterscB6eh30BoHKPofcrBC6gegOeGCFX7z7emsMGKfdHY06A3nMfe1-dR2izjYXwajHeWwn-8V2xiB2mPHDwbLiL3auX4ERJfKkifxdeEtXzX8u5aItnRkYrvdaP3cWLW1kcIjmVNa--iRDHuBB1rFCaUCTotT16xhGIps_3iYPN2RS52s67oKCT0owEJTHMYuFP9c05Nfx95LsblfIxZ3BI_x6UCrDDwBN-aZLFiKr--kMfgBQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
بدن فوق العاده کریس رونالدو در سن 41 سالگی و آماده برای رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23528" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKDgGZBiRd8cvfGxl7CHf4zX4mbX3Q9LC9KF2rRqWmP2xkptgfU5yDLKn60kiDcTDg3gISvxP-ph6YOO91E0J5Lo_XidHn8e1KU-LTlwFwhELr1ksHh9LsmztQjkx7oLX7-YFOyd-y5DONqirQy_LK3PUFGl7MdxBb4aWHqTxmnRE9JUjcSh7K-2NolCqFyB9HpAS3wXhLX9WYO2hxbr9hoHePc2egLCTb54j-Wmy3KpKCMTinhjPZtTXtEmPMo2yENjF6UBZTvRi9kYUcbfKEaIRNy7wC94IVxhaUXpp4Xw6Cr30WPGzQRJPU7AGVjFOjC91ofJocQNR5daugI54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#تکمیلی؛ال‌ناسیونال: یوشکو گواردیول مدافع کروات 24 ساله منچستر سیتی با رئال مادرید به‌توافق شخصی دست یافته و حالا توافق نهایی بین دو باشگاه رئال مادرید و سیتی باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23527" target="_blank">📅 18:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=mQu__s4jT7T0qaOzuu3_h5FL4dfx1RPXP8i1kEKfHs-zzDUqr4-G0tiP12uTc0oIytprYiAluUpj-Lel2IzLuZL-iOmFKggadd0sELB9-dSbqisSFbXGeCkzXFyXn9AklL9GA2ojmmoYmC1KBpgRbMIBCn0XFKPenDmCX79oogrKbhBA2CUfjUnM3tqnZ9OUaLQcNzJ58etPOcdUPXcmu6Hi5NGWv-149ev8XpLK7uORk6l2PKvl9IYh-V2XdQBerl--J8Wv3NOnb-PQeOWJ6FyZhhX4i27j3KrDe-kraJC8xIr8bhX6czRebZNEQuXmmtg__7M54IlBOnWv_CCXAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=mQu__s4jT7T0qaOzuu3_h5FL4dfx1RPXP8i1kEKfHs-zzDUqr4-G0tiP12uTc0oIytprYiAluUpj-Lel2IzLuZL-iOmFKggadd0sELB9-dSbqisSFbXGeCkzXFyXn9AklL9GA2ojmmoYmC1KBpgRbMIBCn0XFKPenDmCX79oogrKbhBA2CUfjUnM3tqnZ9OUaLQcNzJ58etPOcdUPXcmu6Hi5NGWv-149ev8XpLK7uORk6l2PKvl9IYh-V2XdQBerl--J8Wv3NOnb-PQeOWJ6FyZhhX4i27j3KrDe-kraJC8xIr8bhX6czRebZNEQuXmmtg__7M54IlBOnWv_CCXAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
برادر از 4 سال‌پیش‌تاالان‌داره مینویسه؛ سرمربی تیم‌ملی‌ژاپن با همون‌استایل خاصش همچنان میتازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23526" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-nbenO_QxqIskf2QKi85qx5Eb506rPKunWpbq8WavMPwocmPboqFfndMO6keb1rjLZ2c4yVEwxfb-5wG2f1tb_IA2Ph05An1uKS8wS37exozMF-JfrDR7_ScnCVXtOfIMmMokaiblKzeslyWr2JqkpgNMsNX3oos0bX1LQKSvr1VCQSM4czfzxQcB_i-fClRCXQLA6VFVf0uP3qk7cXjYw0aAQEHdjE07HkYgh7CucfYL9dbzG21GT909QHYSe7pcfr9SwUP6TGvKKOX9hTOzbpqAwjehMkODAihEWRq7fIdlquuPvShK6_M7tlqHoGfeeFuO3tLW8sjSjF-wKbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23525" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=YBeePY5JOP8G0ZTD1vLs25nLqX1tEJ_6zoxFMGK52mqf9gLVS1Q3oxLbJ_hgPqAkTGbLKzCBVSu2gyhXQ4JTeuM2fSgxIgJSPD3Ws3ToYq3vgadhYPON5HUvEaey4yeDBw4IiDDGwMsm6LKBCqQrasghtYdaHFCRQydw5oj7lQpDS3hS9XBNrpDMlQTvtJn5UqCT1FViWyA2U-e4X4ALJv_dRNSbMas7MvvEgUJxHhsitpC2UbNx9W-vhBBpnOxUcFF88_Yp8aUdD-P37zJr7qrvN1vMxcWM1c2Pi75NkC_1uTeJQ1OWgqGbKpqhdkWITRm87AMVfzfliWviXrZ2wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=YBeePY5JOP8G0ZTD1vLs25nLqX1tEJ_6zoxFMGK52mqf9gLVS1Q3oxLbJ_hgPqAkTGbLKzCBVSu2gyhXQ4JTeuM2fSgxIgJSPD3Ws3ToYq3vgadhYPON5HUvEaey4yeDBw4IiDDGwMsm6LKBCqQrasghtYdaHFCRQydw5oj7lQpDS3hS9XBNrpDMlQTvtJn5UqCT1FViWyA2U-e4X4ALJv_dRNSbMas7MvvEgUJxHhsitpC2UbNx9W-vhBBpnOxUcFF88_Yp8aUdD-P37zJr7qrvN1vMxcWM1c2Pi75NkC_1uTeJQ1OWgqGbKpqhdkWITRm87AMVfzfliWviXrZ2wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
آردا گولر ستاره تیم ملی ترکیه پیش از آغاز بازی با استرالیا خطاب‌به‌هم‌تیمی‌هاش: یالا ما ازشون قویتریم؛ بیاید این رو از دقیقه 1 بهشون ثابت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23524" target="_blank">📅 17:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe_ZzfzUswSNNeD4H0NZdwwC14vjTAiVB1xo6JWbjJ7k36041t5OIaJPfOjZFyyXfJ56eA-Aljdr08NIC8AGqJTEYdArjVhBIIZwp26SgtfwRELSmmkTaHBbSvlgqru2xqn9RsMQpynz2thBk2k97M6f1WDLACHBT4Pzbh5ipV45r2wbNJ13byIXEUYut2qUNsfH5Ull0_wo0AD3DyPwr4uQo1zw7Ed8ngq9yyAcvAu6wvcya8Vky6QGHfmcnZwIx3Vjrfd6U6oszAclg3nuAeVxUnIMhy3ksOqWTwDfAAX-H86e_HUnnrXkmrjcS_EIHmU2RASCIKWnvp1uhpHFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23523" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk-BuEWiqlqvUpEekMzKL_a2t_kDXylWXIfU1i95FKElbVU7UaCbKtiD24GcYRaghpNITnc5r6ngDLQfY9CH-B19uzRyg0lbiA5OvbDcQ7_LdJ1ZpMuRgWI3ARiZY5vNDwlRmlROPSPgdYSHNyMClA7Hx2yDKjBhLAIXWL1mfX-dgpRP-UfzPTQvJn3K6lyNnD4fc1VYzZxj9nIvnk9J2uh0pktfDiljHxnsHL-2W_RRTRovLwp4jkBjPl19gAaYhtsn-1XtEmiFBZr7RGsGCjtZpAg6-gpT5T3SmunpM7Q1zuCmMgFKdMroTcqlqyub7Pjt68uQqkDJFpai-FNd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23522" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiuljDd4_36nRimsfwQb55t2W_kxwIvW70LHX6cxr-2eCK2F1zVNDDl4KM19DWRzbivoTFR4unViJ62BvaIZTr0pOcta8hd0uonFfyOTX1o3uF-8Y9yJ9Is7LJKqEL-rIyOBj6b-9Z9rUfUrIL-_ggxxlvmPnOlECt0M68vr8c2bFRrFNBXTA8jHM1PM-jDgBzay9-7iwGTsaT9hQdkVZmHjBltr1O9VxFHuzn_f2drXZtYK9AsovBwmXL5tgzJqgBJJhBTP3uQP4iSNjqjbJEeTL7gLK0m4YB0jvqSuqxozk9Qye_iU5vN3QCoGPb3hClxAnDrzWbiHpS9KZgG15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار جذاب امشب دو تیم ملی آلمان
🆚
کوراسائو در هفته نخست رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23521" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=EsmmYgGe1VBUwZ4QZenRwz41KUuYPPcRBkmVkFYp5ZFpVKbAThne2lkhMyUmMqdpqMxL10KPUoeqjF5U_4EsKE54BwENuqnUgyxUR_2-UrmNCgY2VoMk3wpaHGagMN1jRG4J8Cyy5Mik_Ol_A0ioNTKliBaBRGJfvRLRulq3FQWlEiQCsiSz2DtE2BBObgf0RhMEIerIc-b9sG1s2LJd9zUleruWzLQCs3P_hUXaw7D5RaARGaiyL0WqpsXOHWjFDHmDzFVR_YJQNOK9EkHhmHC5OSceZOGN5Zue2bv74Fh-3pMUomuOAGnEe4cT2qmw1jP8zAbwWVwJL_SNwOLKer5WhA-d18awO0QHeLRFG3xld_exRSTcJIQQVfGd_kw_7IYgDGCSSQ4Q3gMNmuRBLkWN0ogbcaAfeW9UG0FhpIW32jBAHZbBzi_F3nU-AFZdBJy55oEbMGpYfr9iqdY-IblLw_hkM_axlcUTMEQadcJlAk4oaWsvtlrfe6KaICPxe0T-54t-bwAnPtU1iGgLiVqZIYCJGsvz3haVCfrnThWG0aw21Go3Sd50In0HT6KAFJbc8BbX12GDlNGSkZEY4o4l89LZtpCl4_60R-aDCeTfncZtVTWXHWeV0m2vyQuKkTg2Cw9daMRHR_AEv_et0EngF5MJfUpar0BugVI_Ucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=EsmmYgGe1VBUwZ4QZenRwz41KUuYPPcRBkmVkFYp5ZFpVKbAThne2lkhMyUmMqdpqMxL10KPUoeqjF5U_4EsKE54BwENuqnUgyxUR_2-UrmNCgY2VoMk3wpaHGagMN1jRG4J8Cyy5Mik_Ol_A0ioNTKliBaBRGJfvRLRulq3FQWlEiQCsiSz2DtE2BBObgf0RhMEIerIc-b9sG1s2LJd9zUleruWzLQCs3P_hUXaw7D5RaARGaiyL0WqpsXOHWjFDHmDzFVR_YJQNOK9EkHhmHC5OSceZOGN5Zue2bv74Fh-3pMUomuOAGnEe4cT2qmw1jP8zAbwWVwJL_SNwOLKer5WhA-d18awO0QHeLRFG3xld_exRSTcJIQQVfGd_kw_7IYgDGCSSQ4Q3gMNmuRBLkWN0ogbcaAfeW9UG0FhpIW32jBAHZbBzi_F3nU-AFZdBJy55oEbMGpYfr9iqdY-IblLw_hkM_axlcUTMEQadcJlAk4oaWsvtlrfe6KaICPxe0T-54t-bwAnPtU1iGgLiVqZIYCJGsvz3haVCfrnThWG0aw21Go3Sd50In0HT6KAFJbc8BbX12GDlNGSkZEY4o4l89LZtpCl4_60R-aDCeTfncZtVTWXHWeV0m2vyQuKkTg2Cw9daMRHR_AEv_et0EngF5MJfUpar0BugVI_Ucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پیش بینی 4 بازی امروز و بامداد فردا رقابت‌های جام جهانی؛ ببینیم چند تاش درست از آب درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/23520" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=pvrBmC039VtfaLUmu0kL3idh9lG-OUU9HQtJr2CbtMtTeZoBT4pVoBirGQlnzx_lTV-JksQSFj8Kk7oRDGinMRzZ_UZXb1NCcQT1Qkr-XrwCoX4LGiSiAzsL8kXpJvW2UI-AThGjy0kD7nKCBrJNGDDcPy3wazMNdq8STTE_Ds24pblV7aNU5SqIYNgwmRWiY5urJtWKztBPZHLPGhxCw1j00RRSt-duxHbVFX785Rv17YIMpOTWsUNRvsHbvrWl9Wg4nnj2-n3C41MKNb6fbqcQDmoktNDbYZcYfMIjyTBwLFErWQj8dR2ZhWoaK7_hKpSciym2LtsZEConyvQYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=pvrBmC039VtfaLUmu0kL3idh9lG-OUU9HQtJr2CbtMtTeZoBT4pVoBirGQlnzx_lTV-JksQSFj8Kk7oRDGinMRzZ_UZXb1NCcQT1Qkr-XrwCoX4LGiSiAzsL8kXpJvW2UI-AThGjy0kD7nKCBrJNGDDcPy3wazMNdq8STTE_Ds24pblV7aNU5SqIYNgwmRWiY5urJtWKztBPZHLPGhxCw1j00RRSt-duxHbVFX785Rv17YIMpOTWsUNRvsHbvrWl9Wg4nnj2-n3C41MKNb6fbqcQDmoktNDbYZcYfMIjyTBwLFErWQj8dR2ZhWoaK7_hKpSciym2LtsZEConyvQYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23519" target="_blank">📅 16:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=QpAw4of-SDgAPWlpg_I-s7FN6fx9f3z9RkhTFzADEm4CWVtf6ndZ7V0Ij9b5wc4C6_GTVgUIAtAu0FIZt0oFI93z6wGIehR8xZCzMtp8ZEdrOtfeCBgbHJXEk7F3lAgb2xDFy9Zf6ZNTgP4762Buo8isr5yRQvjusJHJ0_eFpo22AvrRTSE_mZ_Uo-2oZwmb0iPMxCsq0Cv6vi-XiSdpsUjHdFBSLbMl4-xQpx-heZz-4p75eGM7Z_bRYwLkom7Ss8ndHrQ7ZE8m78rZ8LMHbIO09wmk6ptAejIqs0OleLpDoNfrqwSD5DT0GnsKzVDgtYMIHAmwCDKB2NGR6hokBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=QpAw4of-SDgAPWlpg_I-s7FN6fx9f3z9RkhTFzADEm4CWVtf6ndZ7V0Ij9b5wc4C6_GTVgUIAtAu0FIZt0oFI93z6wGIehR8xZCzMtp8ZEdrOtfeCBgbHJXEk7F3lAgb2xDFy9Zf6ZNTgP4762Buo8isr5yRQvjusJHJ0_eFpo22AvrRTSE_mZ_Uo-2oZwmb0iPMxCsq0Cv6vi-XiSdpsUjHdFBSLbMl4-xQpx-heZz-4p75eGM7Z_bRYwLkom7Ss8ndHrQ7ZE8m78rZ8LMHbIO09wmk6ptAejIqs0OleLpDoNfrqwSD5DT0GnsKzVDgtYMIHAmwCDKB2NGR6hokBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت ژائو کانسلو ستاره32ساله تیم‌ملی پرتعال وباشگاه‌بارسلونا از تراژدی تلخ و سنگین زندگیش که در سال 2013 مادرش جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23518" target="_blank">📅 16:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1W6_zUXMSHrqpxndpl04QlPOeW-NYwmlmm7jT7VFH4I-XY1ddgA9_UodBM9NaZPCOtUfTqcobfdpEM-MRnxOfyb7mWhR6cMWyz3cMXcMhkcxI8BbjpENsdzvv-Vplq9yIBhg8U502epya5SSezfkXxlr51adz6xP0tDy00YQpx9Ae26ulXcBc3xs5_uRWcS1cOATgXHUNUBjuggiwIh1LmtAxi1uLr4D12KXr27NGhV3FFczFJgwsXBGz3U6DBL6RVMo4Xa4o9wKvvhupsD1S3EbIwmnT-jEYr2o1eYhHBikyjyP-vhJ8pvdHwVuNaMp5l2QdjFPgLTSYx3WU1DsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک‌کوکوریابازیکن‌سابق‌چلسی‌ومحصول اکادمی بارسلونا به رئال پیوست؛ وضعیت باشگاه بارسلونا:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23517" target="_blank">📅 16:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOKaGLNnBvA4XwAOkXaZDSMIiN7mHFkLUyDelAqioJIy4g1vRHix3i8HCtCCbzS6JkPkDiBJFMRbfD5pEE5eBBmMlINmB2N_s0LJcHPztDhzoY1euqULlz85xPmnzVY7piG4h41F6fMKQ8EwWmn8aMYqLwCI2VvmQMG9bsog4lRRe4mNzituPtFuuHtyduTvocJ-Gplei0031sAg3xDJLr37JUOJccllcGLS_gbVbFPzoBHjZn9KqQBcQq2ya6dS3-b5lbM-e1f5jtVzzyJesyCvmA0p7QYKzPsAkePQU5F7AZNsa837nbDugY4VYCVTEJzEki61LXZy1eU2og02Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23516" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1jHAk6aUPfL3Boed0WQbA3CVMCUStgBIwkeBh7Rk02miUg78wVbRNuFeR5BhbpyWcERsmlVPM-HFskQklHmFQUNlriT23TOaUqIsigd1HlxO8ksEIgZ0ASycLeR6kaMw-nuMpa8iE--XhiYhGCRgUA7QYPPFlXj6dD8udWbmQDJJvt-czbYgWL1J8_47xRMt0HPbhBnPqczWjle2avsrtws93hU4KBsDAP4LH1ZIpoAALoDAZeBt9XhcHmPXYQC54XndF-9jT498UNlQJL2eAN3E74YUlb7mMO3P19CWOCVHVGypGe0mvvSty1SUhnWLaM21xBX1TrDRjmxy9jiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23515" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvRzW44_d5YsJWaztBNwtZvbo1GXVpvmmTpicb9A4uMJxDAp3vpazn1Lhk9j7xr13pRauIFxVXGQewKZr6Ky5cdh3hTb_rTjXhPOIXIJZVqKFbmKCoO5xIxa8-KMLsZkAa6gE7fBmdQ6wrsbKiNXwNW8FW6NAQoEbGkwBqrmM4TeujAxIuuhpGarRadlIjidjjW1_i3FDw8EL0fTESoxH9m966lB509lxXOyXXT_YgN5k3GMft6PJ1k1OXr9KQ7IyyoMAyd40L3LNtz4A187P5UnUb7gFrNh1RUWjTe0DmHlvgK1se7VjFdX7TKbz89SqHmIZUvTtUPPzLySso-W3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوسمار ویرا سرمربی پرسپولیس: بارها به مدیریت باشگاه گفتم‌که‌به‌قراردادم به این تیم پایبند هستم و به محض آروم شدن شرایط کشور به تهران برمیگردم. لیست بازیکنان‌مدنظرم‌رو‌به‌مدیریت‌دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23514" target="_blank">📅 16:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZSn6aF9BQfhIstdqx_RAdR_oW0MvKuYlcmv_oW3ccZSnd3vTmswU4p2fW8CwbZG-nRZPGho0zQYEO0n38YRaC1s7EnJE968HHYbI9DB1eDSDBuHhx3mn8AshCXzm9QMyu4lbV3cTdoG3sewZQ41TTwWrAIFtbIKVfir-R7HUFsd47bFND28pmILBzrEk9ItDA8plNFpD-XmtLDDT7G6GBF4AequJzzVnmLpn2dcaPflHQWbsSMQxYIhfgbesuXtegwOi0mF2y7IPPc3QrlPAfcdjiwRY65CVrJOw8kfWfYLM1jOBHSuNtMMdBnNuBX0VnXbUe8lykGV6Uyq28ei4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دایانه تومازونی‌اعلام‌کرده به ازای هر گلی که برزیل توی جام جهانی بزنه، یه عکس کاملا برهنه از خودش میده بیرون و اگه برزیل قهرمان بشه، با همه بازیکنان تیم برزیل یه دور می‌خوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23513" target="_blank">📅 15:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=IL1dOez4Fz4o7PKl-vGJJqd9D5AEADBaa6WfZVglNC467uUeb74l4rFI1Fo5hZKwfHI1Yv3RyCuIHf0F9rJOfefCXcycG3cmOhSkWLPaQnmz3Hvahmx3x5Aa6ulBFlE2LhErLrj8Jg-25eO8mY6fY0Aag9GrIC7w3gJ8RxypohM1Ly2L0ZhcRh7uRmQpIQ7mdRGT5mIWACkdHoXIlP4reGTfg7noMR9m_MGcLda2S7D9V1-qwd1fL2lX_bVeagsmq21EbtECyfX6GOdJ4PMaPB1DceJ1cU07IV_SI87MGEWihtuwRpSHmXgqyEWa5B4x4v1_2Km61wwUb4MvGTixOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=IL1dOez4Fz4o7PKl-vGJJqd9D5AEADBaa6WfZVglNC467uUeb74l4rFI1Fo5hZKwfHI1Yv3RyCuIHf0F9rJOfefCXcycG3cmOhSkWLPaQnmz3Hvahmx3x5Aa6ulBFlE2LhErLrj8Jg-25eO8mY6fY0Aag9GrIC7w3gJ8RxypohM1Ly2L0ZhcRh7uRmQpIQ7mdRGT5mIWACkdHoXIlP4reGTfg7noMR9m_MGcLda2S7D9V1-qwd1fL2lX_bVeagsmq21EbtECyfX6GOdJ4PMaPB1DceJ1cU07IV_SI87MGEWihtuwRpSHmXgqyEWa5B4x4v1_2Km61wwUb4MvGTixOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش صحبت‌های ابوطالب در برنامه‌ دیشب درباره اظهارنظر رهبر کره شمالی که گفته بود عاشق لئو مسیه و دوست داره آرژانتین قهرمان شه عالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23512" target="_blank">📅 15:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=DFw6TJb6luF--kC_MwwXxMFhiI3AZwxPXlS1yRRXq-TRSLbGMpDT4To3HTaDT2k3b_5IYhOoz115XaYzS0YGLLTDD5G-g_PaqnTXcNK_EJyLpeuH-dFQ2BfKQHnTkt3RehYLbkfs9QZoofOcSaHuXISlo88GKco0CBwGoNzL_IuOAknfF3KwrZ5gzcLqhfnqaDAJ0LR3-BAhdc5LIuZM7FEf_vbGeB7rZ13vkICOqtuHtIUdBWtSVphBZMj3EXc9mI2NfT2WHj732rEqCNxgouu3xZCnmfxMTv4ihmh1a5YkbzvX9zLNm5ip5mqvcRAvuk3y2GQX6uW1kxpT79gdng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=DFw6TJb6luF--kC_MwwXxMFhiI3AZwxPXlS1yRRXq-TRSLbGMpDT4To3HTaDT2k3b_5IYhOoz115XaYzS0YGLLTDD5G-g_PaqnTXcNK_EJyLpeuH-dFQ2BfKQHnTkt3RehYLbkfs9QZoofOcSaHuXISlo88GKco0CBwGoNzL_IuOAknfF3KwrZ5gzcLqhfnqaDAJ0LR3-BAhdc5LIuZM7FEf_vbGeB7rZ13vkICOqtuHtIUdBWtSVphBZMj3EXc9mI2NfT2WHj732rEqCNxgouu3xZCnmfxMTv4ihmh1a5YkbzvX9zLNm5ip5mqvcRAvuk3y2GQX6uW1kxpT79gdng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همسر کوکوریا مدافع‌چپ جدید تیم رئال مادرید هستن که در مصاحبه ای گفته سال‌ها رویای پیوستن شوهرش به رئال‌مادرید رو درسر داشته و حالا بسیار خوشحاله که این‌اتفاق مبارک براشون رخ داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23511" target="_blank">📅 15:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv5SkxPD2BX-TynVtFSbZCzqsT4I-k8uA2VfXyc78pNDcnc1loEuJeSowCVDoQPoF5QNWdurF0zGTE3DW-XNTsKAA6Ad4dyMLvLtVz-c5FvkEcBd0hhySfoE-_LUVYrNAPrWhIDdGabHo4zEslmlXdmYmTNkS5InIv32uCZhlbo3ZOJHqWOEyvFlc7pDfzXLvuNuEdUgvV5pO7Dk-gQAT7JL6WGNGC8GyP0aXOza5IevRcHMNJNrieqploqByRGWHv5pfSt-ucKFbMcUG2dCSg15D98swrpTuDV75ONy4wlxFFZp1HU8B75JZQZ1XY_BSDMAUKwWF7sdbi3jI-dAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه‌بندی‌شادترین‌کشورهای حاضر در جام جهانی ۲۰۲۶؛ مطابق معمول ایران اون پایین های لیسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23510" target="_blank">📅 15:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSFsY46WE7K9DtHMJsccXhE108lfDJN8qIg0gg-SIQ6Bi9X7B2HHx4LNSujJnct3URNiMdEPKAbtsY3xq1yLOh3XB0-2AEDyVC7xb_qKtsJHnqW4F4AG5XLwowMJheHND64UyYnEwhqyFl_osC16CQPZE9jKRnvmscqmx6rde09tqogNIlBv_GWLg-nkgjj_aDqCGo_MfhnGOpYG2eixEM9qT0K6CG6-cs0sw9WyQzxVpOWdE3m2zRRRLp1Vo-rKdw6yYtQbsEvS13KzPaSKR95D_MZUJzFAEgNn6OE2aIWoLDMXFxujlT12szhSYtWREuRlvzodXragNq98qTDCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نیکو اشلوتربک مدافع ملی پوش 25 ساله بورسیا دورتموند آمادگی خود را برای عقد قرارداد پنج ساله باباشگاه رئال‌مادرید اعلام کرده و درصورت توافق دوباشگاه احتمال این انتقال زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23509" target="_blank">📅 15:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=vL3JEG7bjEZW1-urP8ttHpHCiXUeYPZ43-eUhE751hy8VxovOiW2jIfcr4fOE-6CBU4bvuEWvcbm6doNhQHrzMSvY8gWEgIePbXktK9ZcH0uOC5lBtBx2MIDgKH25GcRrbkVw5Fq4aee2HxV8rYGbQ33fvj--lLTgFWDw5IfgYZ_M8tlcfFhEeCJ2LmOu-QAMhDxuuopp0TeKmyis53f-yJCNW95agCKOOn4yOpypzv98C3-PkUiUBvVrMl0xH7oOONrAfa1JiNfKperrCHnEfmlJ5MjZrfX53F15AgfHe0b3L-9JOdzpvgRJL789VRFw7iMyrLHPP40f57Z_vuiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=vL3JEG7bjEZW1-urP8ttHpHCiXUeYPZ43-eUhE751hy8VxovOiW2jIfcr4fOE-6CBU4bvuEWvcbm6doNhQHrzMSvY8gWEgIePbXktK9ZcH0uOC5lBtBx2MIDgKH25GcRrbkVw5Fq4aee2HxV8rYGbQ33fvj--lLTgFWDw5IfgYZ_M8tlcfFhEeCJ2LmOu-QAMhDxuuopp0TeKmyis53f-yJCNW95agCKOOn4yOpypzv98C3-PkUiUBvVrMl0xH7oOONrAfa1JiNfKperrCHnEfmlJ5MjZrfX53F15AgfHe0b3L-9JOdzpvgRJL789VRFw7iMyrLHPP40f57Z_vuiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شیث‌رضایی درمصاحبه باابوطالب حسینی: همه روابطم باخانم‌هااسلامی بوده! دروغ تو کارم نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23508" target="_blank">📅 15:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=bai5EtY1lJ26PAcpWMCf3eddth33xmhzR16GZh4Q_RfVSxHNPbLVnkxqCQTtvdtYcElGFxbn4SZ8YqB2Htvb_ekHgYxvMgijNhmDO-0nLctYuCAuxKiQTD8IIXWjwxDfd90dfA1nSzcuN5PABJeqweBZ1EHQSYPDGwct9lRlF4avNvqLjKfekYKo8wFQNAIR-xvMDEz6pGU26Ke9ekzKV3AMEpOmIkk4x7zAh9FYr-Sz1mqBkE7EasTJ9VBMTeRZ4p4qocPzZhE3_CdePrjk2dUoFSLWWYfSnGI17N6zIiDjH-Q_9h-kzElwM6_B8QFNrzH7M-BL7BVNB_FbO4xnXKOn7nOeP16BldOQ3GGDDkNe07WgOflzcIAavK0jw0r9w6ab7taIxEOm3mXHA4cjinNd5lGnVRphlaFA_zXjYmRPRoj4zVBE7Ttaeji9UiXcwohxASuQTK95Qu1FOKISmV6to4BQ02nR1Zfh0O31mEfX14oGWx5na1XpPDMnUWdzfXiezwwiaPN1MGzKM1zCiopci6JpwubR651WzrAS-PLJXypov3MR4yEng-jmi-MiG3db7WIKPC_IMdNHqkEX5oFYHq3C6KAvvfXJRSpREfqz1gXp9HyCy4PUYn1ExjWs1RjaB3g6kObXziIhJnVL8WRtcxV2_Nz6sGZQpitKFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=bai5EtY1lJ26PAcpWMCf3eddth33xmhzR16GZh4Q_RfVSxHNPbLVnkxqCQTtvdtYcElGFxbn4SZ8YqB2Htvb_ekHgYxvMgijNhmDO-0nLctYuCAuxKiQTD8IIXWjwxDfd90dfA1nSzcuN5PABJeqweBZ1EHQSYPDGwct9lRlF4avNvqLjKfekYKo8wFQNAIR-xvMDEz6pGU26Ke9ekzKV3AMEpOmIkk4x7zAh9FYr-Sz1mqBkE7EasTJ9VBMTeRZ4p4qocPzZhE3_CdePrjk2dUoFSLWWYfSnGI17N6zIiDjH-Q_9h-kzElwM6_B8QFNrzH7M-BL7BVNB_FbO4xnXKOn7nOeP16BldOQ3GGDDkNe07WgOflzcIAavK0jw0r9w6ab7taIxEOm3mXHA4cjinNd5lGnVRphlaFA_zXjYmRPRoj4zVBE7Ttaeji9UiXcwohxASuQTK95Qu1FOKISmV6to4BQ02nR1Zfh0O31mEfX14oGWx5na1XpPDMnUWdzfXiezwwiaPN1MGzKM1zCiopci6JpwubR651WzrAS-PLJXypov3MR4yEng-jmi-MiG3db7WIKPC_IMdNHqkEX5oFYHq3C6KAvvfXJRSpREfqz1gXp9HyCy4PUYn1ExjWs1RjaB3g6kObXziIhJnVL8WRtcxV2_Nz6sGZQpitKFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی زلاتان و هانری، اسپید رو دست میندازند؛ این دلقک نمیدونه ایبرا خودش ختم این کاراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23507" target="_blank">📅 14:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_8FWKM2Z5cekxPVXCHvpRZUj_T2gc2dvFrwXKwkaVq5r1gWQRdSYYV5alEsoUWgKoxlfRjQNVYU6WEaEcWjvXiqSyPoOTBaaleF4z-2pRrGB6OgJKs6Ai1V_pG1KnF6iTUbaM7SvG9EOjPDy5yrzeytoarlo6uRO1-Gc8g635FZED7CBcGME9F6ileYWDdOk7LHJjnyNz8cMsF5bJLhK9CKGF2q1aXwDD-LHWLM7EDK-0YGFeyrvoY5ZEZsZbI3lCtXGA7hL73VBGyfjZBTu90Pa9R1TAubxK-IfYcoPDRlbBfzskeZ18Qoass7AKaQZw1SBvxP_vxZlw0PyqJ-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23506" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvZozs8hJt9TsNuWmrwWJ4fk6TP53EerF8l0_XegAUlj-Igbu70T7oRrHPW65ONK-_0jH9aOor6vGwgHu0Vi_Z5yg13Zkg-E6-t0EWpQnXGRk4VnWzBoM9lznxdMD2_wbGZaNJd4bmoMSx61pK-0HH55NUTZV1OVLFN9aQau8bDScloBAXi_KHqq7h-Hao--U4rmUK6TraAPr-LASAAHIglldTP1yKXzTTSCtFCE6NvnF71SceOZLGDTWnlATFxQCYFryMGniNzTb3ZruUP5q7BY-TI6AiHTBRBRkEDJ13j-Hr7cCFLRppPX2gY_3nTfetazS-P_BQFYJcDpy86M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23505" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358a407b96.mp4?token=d9sUX9txbKxU_aIIVWpl5gVo_zzbKt5U8ZnZG0lGHaQO1mNDbWk-vCz-0c2vHjIH9r6oS1D_029N4acTeCJJkyrn7TLOieaAWAXmgRBeK7L6_IGfMOS_j0mW8Gijllfow21x33CTDV7xzak82MkbseAZdcfNkd6ibSv9Zja-HEJN1d2ph78sR0cqynbAicR0r5FUPN9W4sKatxBuv795Gnpd-Biwfz-vyZhBKX2EUSk4y2KokmiIG6cpLVV-XVBGICM5vrYDHm7IwW5ESzDmoTX7e25f6TtMIVrnXpO9ruNBQD3gxKFvbnYfj08kYVH1u7LRWAKUFpWEAxb7i8EWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358a407b96.mp4?token=d9sUX9txbKxU_aIIVWpl5gVo_zzbKt5U8ZnZG0lGHaQO1mNDbWk-vCz-0c2vHjIH9r6oS1D_029N4acTeCJJkyrn7TLOieaAWAXmgRBeK7L6_IGfMOS_j0mW8Gijllfow21x33CTDV7xzak82MkbseAZdcfNkd6ibSv9Zja-HEJN1d2ph78sR0cqynbAicR0r5FUPN9W4sKatxBuv795Gnpd-Biwfz-vyZhBKX2EUSk4y2KokmiIG6cpLVV-XVBGICM5vrYDHm7IwW5ESzDmoTX7e25f6TtMIVrnXpO9ruNBQD3gxKFvbnYfj08kYVH1u7LRWAKUFpWEAxb7i8EWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احسان‌محمدی‌مدیرکمیته‌مسئولیت‌های اجتماعی می‌گوید بخاطر اتفاقات سال 1388؛ تیم ملی فوتبال ایران دیگر در هیچ مسابقه‌ای سبز نمی‌پوشد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23504" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PTf4j7M-kHv3oIrJ6wb0ZCKT-YMy-zukXXfDOFWzRY8GsTsSnZWK3eYl8KdH8jGj25yZOkpmyOrWvAIO5RNOQG9A7zyPy_h1DorT5hWIsoGCAYZwQLN0875eQ3asPlvxh8Odw5Cvsmq81H5H_AhlNuU5LspGoPhRqBwHytSjmR33i6f0GjC9Vxrt1OD_PXEfcwg-SlnpG33TpszFVPdo1pzG2hn56i-QPO2lMquRP6iIhWhbCSep7KKTCaTeAcIUk6Y7KjEv0qLxzWeUofg0GG0SR0n7sIapKabtVKmWH0msjh4FlH5z1eAXdBAbGTP-7vI_e4G0tr-3I5kFMoU3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای،مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23503" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=fc_ZXJLvS5al-GZHUwniYXYltltdplMOLaSsWyQTGhLTVnEUIglVik_0luj8QFiU1nDdLRNpHnrRitqiY703wTW3lRo4ht_-4GseqQibpTwHtUbhKmSrNWifdGHPzZ0B5Io60N3KiHiUhr5s3FrJqaOMwsmn1xWIpf6GFD7cFdQIJJHvetK9dJWdHvmTxEhGSUR6nvS4SGDCrJGGiom0FEsqJ9xKs3aR1T_atBgToelfw6R95VWQBJTcTeBGOJ6V3uQyR6pW_x3hbwgATBfv0THUbsJSzGBLz_285-ZLZN9Mt9CdkAo3Empw2YjXUUAT_Hk15Ms1IBxmdmPl1kLXUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=fc_ZXJLvS5al-GZHUwniYXYltltdplMOLaSsWyQTGhLTVnEUIglVik_0luj8QFiU1nDdLRNpHnrRitqiY703wTW3lRo4ht_-4GseqQibpTwHtUbhKmSrNWifdGHPzZ0B5Io60N3KiHiUhr5s3FrJqaOMwsmn1xWIpf6GFD7cFdQIJJHvetK9dJWdHvmTxEhGSUR6nvS4SGDCrJGGiom0FEsqJ9xKs3aR1T_atBgToelfw6R95VWQBJTcTeBGOJ6V3uQyR6pW_x3hbwgATBfv0THUbsJSzGBLz_285-ZLZN9Mt9CdkAo3Empw2YjXUUAT_Hk15Ms1IBxmdmPl1kLXUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فوتبال‌فراتر از یک‌ورزش؛
بازیکنان‌آلمان برای دل گرمی دادن به‌حریف‌به‌سمت آنهارفتند و از تلاششان قدردانی کردند. کوراسائو باوجود شکست، اولین گل تاریخ خود درجام‌جهانی را به ثمر رساند و حضورش دراین‌رقابت‌ها را به یک دستاورد تاریخی تبدیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23502" target="_blank">📅 13:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YviEv75x1XmuZOJwl3Z-GDLqqji1RkI0Q0QlWa-21PlzJ8LOsnW0F5iaPTZxuKNUIR-2b8S2WHAQmvVEzmtn9LOPxCLUspc7syx4-O-eXav6fARvxO6snwNaPkwBnqUGm1rDDXF5z4nBKUwpzGkpkXtO5ZCYB3VCvGFhc-knaPsqHAGUvU44UY73zN7c6cO9xV_86yXM2XCRtc76mVVSs2J7MHxzfvWXOFAjcnlgBVERsGYS_MjonkcespmYhzGryD7YDZqdL7kITY9ZwFmexIo8fVxKeokJQErqJK_xaoluWAncDY94YsFH7eP9ZHhuPpUevbLE-x02D6PfJh4bKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌بهانه‌عقدقرارداداحتمالی آموریم بامیلان یادی کنیم از این‌توییتر‌که نوشته:زنان باقاعدگی،بارداری و یائسگی دست و پنجه نرم می‌کنن، مردا چی؟ یکی از فن‌های یونایتد هم گفته: ترکیب 343 روبن آموریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23501" target="_blank">📅 13:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxCQoIQEoiwzsIf7C_rEJ_snRLjAhE4YhO6Mf8qj4f3j3_mAk9_dujZ0GkI-p1FYvfvlrntV45Y8HK2ThspA32gZrCBcpXWfsHGR01aK9vfvLtwKTDf5vSG4EvazJT8TEXPe028Rt8-tb8dwUzB2QkAGqWGCMhccgdTOPMCTLL7K_IDXKjsjjsvkO_SqavgHt4jZN_qBUtbjERGVOlFAExG2efzMMwZV61BxbfiisTlmYeN7D8n4BOOYsqAfU4Jq8MPRHRXW9FtezwekCX-zFGNBUxjaQFxiY1mJWaFUeQo-p58U9209hV-pnxOLwglaX_u_EaoXBsdLNGVfl3K86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا درسایت‌خود رسما اعلام‌کرده که تا به امروز 19 هزار نفر از زنان سه کشور میزبان باردار شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23500" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165e001c95.mp4?token=U0qJCBuErdag_mnxVDUmppuMvMcE0BzayrX4ARh92ABe7mte8MLXIz9zAktOKJd6I21iqEbX3g3qSFTZOw16HPFeLjAfK_lta2jv5O2za7puyqHP82WyEl8ujypFqiyBKdafNRTMHRxMCFmjT657NXr1l3U43syINTXdoOCUZPanwzPiCtiZK_3hlcJ_QmTcDv_NF3NhqNx700G6nkVvqmLORE3IBRNFNbcC1oNGg1lHM3Vw5w4HQcnbCW8N56SWTGk57NipsBiB3FYqFKf8cgaCkpSZku7ctchlrUfW9pCqquizk6N9icoPnyXJXQtkFK2z-7MbjscXVHLEK9uQJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165e001c95.mp4?token=U0qJCBuErdag_mnxVDUmppuMvMcE0BzayrX4ARh92ABe7mte8MLXIz9zAktOKJd6I21iqEbX3g3qSFTZOw16HPFeLjAfK_lta2jv5O2za7puyqHP82WyEl8ujypFqiyBKdafNRTMHRxMCFmjT657NXr1l3U43syINTXdoOCUZPanwzPiCtiZK_3hlcJ_QmTcDv_NF3NhqNx700G6nkVvqmLORE3IBRNFNbcC1oNGg1lHM3Vw5w4HQcnbCW8N56SWTGk57NipsBiB3FYqFKf8cgaCkpSZku7ctchlrUfW9pCqquizk6N9icoPnyXJXQtkFK2z-7MbjscXVHLEK9uQJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد سیانکی گزارشگر:
امیرمحمد رزاقی نیا هافبک ملی پوش تیم استقلال که الان مسافر جام جهانی شده رو من کشف کردم و به فوتبال اوردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23499" target="_blank">📅 13:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzea4fTO8zNsPaZoGDhVAayHrNpsGoi_ufERbTy2B-exO_cBH54ySVXRX7dGF8nXNElfxzg-ipsoKPZHgxQu4c1kr3iuBWck4FL9oAhgHfdak8-PAwS6BtxZMlFB_GfAccmr-yjtc12klDR1nRN_8LY_Qe8paXsMhdtcFitISBlqZMkLWRLgSCyPQrqQtlM0FRKMWQa8qEqf7FkPfqLB8jL9EeQ6EOJQ9DP4ZbrMnv8nWc0Gn-3U1JrR11SXCC9unlqU5RTj07It4KW7U7q47r7KJ--PZY3Rt-MY4QWlnwNiHANoqatKWxDioNQ8AsMOetwoe-1zLMJZ3d5woESjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات
|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23498" target="_blank">📅 12:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXUTzxLjzGSQG2Mhprma1FSBN4zqRgBUg58wlAD8hajXBZyjx8k66tnPz3uVleCeYbdJhbj-bS1Rss-3qgCHALmlXF3g36w_hJMSRMutTCNlVAQ-FJHPMqXBktYz2yDYuzULYfEcdd1zadf8tuUuzXqBC95KUBJUf-DUXGCkGW9lXLY8uYMyAqEeU7iPzuyOlTvY2PVC5QpDb8PscnqP3zmEAdSkehZYIRtnJCBSGeJWUpO8DRUzdvjYrp_Qw71fLdkju2_GMk6bmIJTMDjAiQWaJfv7ilwW35XEG0Br9RA6_F60Vh3oAin2-4xje2stzbu7E0Orjz7bW2IzuHjAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این
نظرسنجی
که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23497" target="_blank">📅 12:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvfbZ5KamhdAbVeoIhZ7wdUrNDEycknzNJ9mVc4smI-AlHucZoe-26v_OyWf8nUO7_qTOx6xq1AbL4f-x4kID8vRzX54ITCnF2mrUtp3doowfZyj5OfiiPZpW29FOn1U_29okowIVcQ_RJ83n9SmbQMYlPlb41RHTCjtvrEYTlPJ-1hrMmH7R5svcu-0eYFCteXlXqQRO-QM3Lr5kbgFhgJyETKxleum43IlNFsXC3Wdyb6i14cMKQI0n_IpXDiY9ufL6qvD6K71RfedQliBjVXidEEZ0oZ6FyeHawdyHntwInS9p6ZCrtt4TNH-ihc4XFHLFcBdiF2bYRCQwopJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23496" target="_blank">📅 12:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=YpbRBoR-hVvxSdKg3EaWUwM2I1bGt0QO0I5wI1YtnPWg-mkL7Wm2Y3tdniO64ZhlVO8jjGwRFBMrweqFQGkXC4qb9hKBmlc8tF42FFqhVsQw_zx4mklLq0a6gMWZ1IDGWQk_OyhZEcvUD7VnK4BmAg0zbQ1EGrktd1Hd-HJxcxcklQUIuyfu3RlTx7h977M3ip75IwnZvrwHHlzhhVuJ31xoeHmYCN4x89cCAKJTkGxmBtF3z5R220Tl5j-hryNuAKMM_IaGCnink3qGtTz-VPQEpxBPqd1_K4k2jGkldFrkQ3ixI88o8ahIbVV1NLeh_Xa0537u2a8V88k8vw65pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=YpbRBoR-hVvxSdKg3EaWUwM2I1bGt0QO0I5wI1YtnPWg-mkL7Wm2Y3tdniO64ZhlVO8jjGwRFBMrweqFQGkXC4qb9hKBmlc8tF42FFqhVsQw_zx4mklLq0a6gMWZ1IDGWQk_OyhZEcvUD7VnK4BmAg0zbQ1EGrktd1Hd-HJxcxcklQUIuyfu3RlTx7h977M3ip75IwnZvrwHHlzhhVuJ31xoeHmYCN4x89cCAKJTkGxmBtF3z5R220Tl5j-hryNuAKMM_IaGCnink3qGtTz-VPQEpxBPqd1_K4k2jGkldFrkQ3ixI88o8ahIbVV1NLeh_Xa0537u2a8V88k8vw65pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23495" target="_blank">📅 12:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0tifTL1GAWrptx4rTYy5nmX4KE9gM-n1a5jlIpw1sbJCKpvM9rJE_v4JnNPPVHybM5iEUm-qa-ZY3OlBtOqzjKoXL9S5E65bR5KWPTKEs8IEIw3KIQqZZoFn0foNDH91kX8uoPo7_g-uc58rraMDo_31zsh7XSXOdNBLTuukkjVCv4gTtUcgj1RiJjcTZeRPUh9kIHYxFhlTOsPj05VB5VthZdfW3L04Ch4NMEPQyG5Pki_B8gqO0nJaW7IwvpEEwRPOGpsLznXe6fCW04dV5NovEo0hB5suV35zJCiO61XL_WwtKxjN1wqknxS4xYghpZok_4OW0WeiAq3XxIglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اروپا هنوز راه شکست دادن ژاپن را پیدا نکرده! سامورایی‌های آبی ازسال ۲۰۱۹ تاکنون مقابل تیم‌های اروپایی شکست‌نخورده‌اند؛ از آلمان و اسپانیا گرفته تاانگلیس و هلند. بزودی تماس سرمربیان بزرگ تیم‌ های اروپایی با ژنرال برای آموزش راه شکست ژاپن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23494" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiniNwBK9FtsapmJh4CkYo8dubFlircn5e5JiWLe19YSyHD-U-1043jR-fN5NP4rF2gYJUF2-4Nc-mgxWRCCU6k0YuGTgjL9CRF7gTAUItygkxj8qF6F1xsRJq-1XUtOvoUPWi0o_NrPiYv2ieed5l-H-bXqMU0EXvINERbS_qRHk1CMftb6WxuHWchSWs32BsuuDOoOpirf4Yg4B1pa7l10BEP4S4fCc7DC9BPzsfQqTkL2lFU5I0SD8VYukUd2DzazRg9sJWKWJjMe3gNwelal1n48LhDeC8Npp1HYqpqdnrLROClp6CqGI8R8kDK9I6N7mOgI39BpmKQoOVBWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23493" target="_blank">📅 11:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akNY_KYfjomTMin58aQo0IE82Z7Bh_01N79VEyVvV_y9SZ9J72S4ts6BKp4vzyd8NgyqfGc9Qh4uX2opi1wwGbhLlyCxIH2F3gB7to6_BAapZDbz-abeYmzqL5quVaJJolrdAbxTVmJvtpvF-a3tBjY5AdgueTBaeZ_6AMULXaIxQT5NjQ9jmhG66PKlN8o10xAaL9qe55xKBGgEF-FcVWXq-sfDkt6ItZy-2G-DzYKnfj2NNU_wo7XkybqN2zPbQFt05aYEcIIRIu1U6c8tgBZQaUA0CVY370LQMiINOLAjsIscRJxMSJhkaFR1Tk8yfmFCXsqZWAoxfyTBY5CiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23492" target="_blank">📅 10:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0qdCZoD1pYvx4Eg7XAVi5TclRTcokF4TgCA8FjBEzyQmYi9W6Kozx-V2m6xIW7NCTqxnngBN3VrlBvHzOuX8FJWtg8SH3PolVm-6-YiNb7LXY9iC0wq31JSJMTazpW8U_FuSFkbosWrDi16w7gHm1lZgdjtdeRxPbTP4Ws2_RsFOxe8zo8aOoMIfILJpQNHmZ1fhclAo2pGM_LCE8RLp2xIP5mp03_7Xpjm6G5RjxwMs1XrtY2Zihoz5BAeT5ksxv7USzdX8Jjdfefk8I8erAoHDxX0Qkr2iuphs6rq7Qz01gUyJAJhWEgYE3dip0ZdPq92UQr16AJ-Gm1ENAAteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23491" target="_blank">📅 09:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuJmtFhEHENqAgeuB581sY-iFJt8l9vZcCL8ClGOOsLulyCX1x1dcCozEQArgaqkwKyjabsZePzoBuA4lfumR_5XL_pF6cnALez0-wkLYFFmOlxLu-WGgn3A8GbY-5l4ilD0JA9G0ZJ_tvXquzYV4S0XNnEejMN4lrg6OQlX8cyU2OKuXqxoVlGDut4ukslLQBZrorKpKqovkS_mz5Tv_iNoHji5DXLRWA9PpE1tzM9a_nkxC8sP7yDMKjjyAsIidv-Cnznl3ATiZhyhDmmGNrICOtgNKgUvhu55UqHIp0u_VnVr0hX-NSK5npNd9xgQimIwWG6ZJlY30huQtgctxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های پرشیانا؛ مدیر برنامه کسری طاهری فرداصبح‌و‌عصر بامدیریت دو تیم استقلال و پرسپولیس جلسه‌ای مهم برگزار خواهد کرد تا مقصد نهایی کسریِ 19 ساله برای فصل بعد مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23490" target="_blank">📅 09:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=C6ARaFmvlvDdjv2IqMg0ucKAbA9yH_3w1xOmFxLuTuaQoq0V5dioMnoQNn_lvndK4r6-te_z_QzFCfIYybk9ywV4IP-s12KK8eCMYLa7xQjv4b9-xEb1I5grtCbqN57f6HFbosz8WkpdZuVj1IxZPU_6H4t3q8uYesBrivkyPxV1clRF0YH2ak7mcRo6V-39fmPdd83_ufGOOEsLzIQwpnrU74XF0vfJWws5vbcNVERXE-dtDNAR-Ojo89gpeanw5LdghOo4doGZP5klG_1CrxI-LtcrIQ1IGvWJRh-LOlgD-a94S6hmxhBIYaQu6IJAUslVRPleEJKvaO43JS8e7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=C6ARaFmvlvDdjv2IqMg0ucKAbA9yH_3w1xOmFxLuTuaQoq0V5dioMnoQNn_lvndK4r6-te_z_QzFCfIYybk9ywV4IP-s12KK8eCMYLa7xQjv4b9-xEb1I5grtCbqN57f6HFbosz8WkpdZuVj1IxZPU_6H4t3q8uYesBrivkyPxV1clRF0YH2ak7mcRo6V-39fmPdd83_ufGOOEsLzIQwpnrU74XF0vfJWws5vbcNVERXE-dtDNAR-Ojo89gpeanw5LdghOo4doGZP5klG_1CrxI-LtcrIQ1IGvWJRh-LOlgD-a94S6hmxhBIYaQu6IJAUslVRPleEJKvaO43JS8e7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مهمون‌های ویژه بازی هفته نخست آمریکا مقابل پاراگوئه در رقابت‌های جام جهانی 2026 رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23489" target="_blank">📅 09:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=o-IuyIDcrye555iIgK1IWJpMl9lxWplono-eoFjh-q93LfToOYsqi4xRp6iswenuYgNbSGad42bCO1Ce9ME8zc4B_slD33FFxl1njL2NibfeXrwa-usVrKqyNJFvLDWIvLRQtLi6muBt-3f-cx2MenRs4A7ojkfexPfXBuOnNZbqZmSD6ET9QusauI0cq7TG5HcP9-vU4e8pkDNLpVJjgpSdCrIg7PAQYeihHEVpwsv8DPK3cLMk_I9x2ga2opOn00KJ2DXPAB_PEVACN631VV4PhDA7xmKDfuhg_Ad1fpAlp4s2faC5rnPBuUYCBHxjQX8YfEtU62iI_x16As-vsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=o-IuyIDcrye555iIgK1IWJpMl9lxWplono-eoFjh-q93LfToOYsqi4xRp6iswenuYgNbSGad42bCO1Ce9ME8zc4B_slD33FFxl1njL2NibfeXrwa-usVrKqyNJFvLDWIvLRQtLi6muBt-3f-cx2MenRs4A7ojkfexPfXBuOnNZbqZmSD6ET9QusauI0cq7TG5HcP9-vU4e8pkDNLpVJjgpSdCrIg7PAQYeihHEVpwsv8DPK3cLMk_I9x2ga2opOn00KJ2DXPAB_PEVACN631VV4PhDA7xmKDfuhg_Ad1fpAlp4s2faC5rnPBuUYCBHxjQX8YfEtU62iI_x16As-vsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛ سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23488" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMcK3aobBuf9lPFaDnmWeK8hCCZU4QFgL_4AJ_wlsKm432QfCYB0WZqtHc5b_djSMP7Za-nRt4gC3COhYsK4rbirjdVlde-jqyzpBRrdh8apahNScHJZkCbobHKBcHdGG0eTEvTRdiJDSdr-jGGeyqCr703HYVREn5bdYaXYzVQKbdhZq2YJTIngoU5R2NTzVQd_GAadmisI5pLE0IAyRZQJaa3EwS_ZboxpvNz3Y9WrKLrzctezlGqOhopayiPCYodNsB7I5MqStPG5ldYcFGHmvusi9eiGH0N87mcUX_duiyUnT-_ywwO8_IIlPfuNXq1XLUI8b2yl8hYBk04q_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFN6k3_9qq1A5zYgz0d67RLJ_e1B6GK4Ks_PGFk-ZHSkb5aKhxDaN34C-cUSssepaw09Ahje9owv6l-P-MX-8h93oL6OdTIzKhgHy9WM0JWgb_MmEudfeHsopAao2la1DJzAliBjqE--bPgr6iH_3cUtx-bXekvRnKFDVq380DESNqxpFweDPcWzZ-ha6RTTPVKCLY3kIKjxvJ7xX5BEKVHDHZxFXSHqAgSyHWG-7q43MMs2HT2Hlyl649UNKpE3VUs1_bcP4_YLKOaEvXmFRNop1TuqZmn6Va3LQGlzPMaqVx-3V4hCOIfZP62sfc-7X9XJtqImhEqr2-7x-_RAbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23486" target="_blank">📅 09:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjtwW5l_5-lYRxLU0PEh_gYbSbLjaXMylKasWH5MDkmwnF7WPW13ShSjyJ-ieLOSwpb_p_zqXXeieI2oHZbzpF3854go5Xu-nJ4CrO2uW24DQgmNewUnaRA1rOuP1UOLuVRZgD1_V6Tp6LCytL2RJeq0YmgpF-kpIw_2Nb9TfFTSFLfjVmSrea0DzvWWmdsoHBYWFGaRqY0VPFPoa11bHp9khiDUz7nKPQFC9AAP1rg5ksp7zuspA00z3rG2T_Gbl_IWfNeC0kl8nhf9tpnbPDMcNf6qWqAh67pEVrap-xDD4RH00R7Nmke5Yvi28HKJ-k9bSw-jE0wWa90Qlhr16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌چهارم‌لیگ‌ملت‌های‌والیبال؛ کامل شاگردان روبرتو پیاتزا کامل نشد؛ سومین شکست ایرانی‌ها در لیگ ملت‌های والیبال در چهارمین بازی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23484" target="_blank">📅 03:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVk1IaTDReqDmxgR8Kximw015kAInpcvB59xRIyQ8eZc0TWqOowsdrheqNuC0XxJtwML3JvG7VDoohSbkg78w2G2AAvbkRPBqC5bXjm2V0GkEKQJWwIf2xA6OiQpAQE3wskbHjXbFmP0hJJagvCyDdLzmnI-sViT5hfwZEGs6-n5XRWTsrGyq7HiCjitoFKGAhoCm68NCgl0RvGTGNHbNRHbzrG9HEjBT7LcpPTzR3stQThKT2Alguavgisj6d2nzIUWiCJ3GFD5islRZuG9Qcy86M5PicLAXKRdiPgPaMOfw0iMG-gDVFjb0W5BEkCcPAM-5AOdpbIUxLchSOgYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نماینده انزو فرناندز به سران رئال اعلام کرده که این ستاره آرژانتینی بسیار علاقمند به پیوستن به‌این‌تیمه و حتی‌حاضره دستمزدش کاهش دهد تا بعد جام جهانی شاگرد مورینیو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23483" target="_blank">📅 02:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH8mr3DVSMtjdBpayPKyS7S4zx-rsMYUiqkLXiacGSyFGax1ma1unl437ADuIh57h31hqWKA6qQuAxI-6BGGTtlks7vKQ5YtTBRXCm7HcZunhZl4n5A3hoBsnI7EYlDShTFSrmrx1EMiGeMHEQ1oF2Cai9PjOmTLDC64WiQ52mokZsypKQwufJneJw7HCyY3sEHEfsLVRFk7FdODAo13VL1xL5qR4VUeV2245-6dPwnQWAr2H2wlA36RYwP_GyDW1xjI-HlJCgejbAHpOiIhSN0q3WxUf86fgjNeiViRG_vTIekdxVtSPJzSRgiI5ppptiaFmYmQ684rLg4LXeB3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23482" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STG2zhmSzv1B6rI8SxR-nS8woNzC6jjqNQnaPaoGT8qMlxfIAlcg0-FOwoK5hYtCC4Ss2EyesonOli-IYAbPAYj4Zf4cbJA20D0kJ5S8uI3dkFQHxSmBwU4SQEAFFYPjkz6bQc-k0GXzeDdtEU4lokSq6rvsV3SST8Yze4iJbVTfIG0bb__j9rrbtSV-NUF-en5Ydz2fEZg5oYS6YtxtihoD9UW0XN2nlIKP3m9pMtlfaR-WtlGTbsl054z9qYg4XBWs_qMHJ4JmhQ1RhXzfxlya33w7deW0WRONXF4RBXa3yNDGkUpUaSGnIxp1oXAUBSSFIrhSg5-iXm306MSR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23481" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdRcEuZT78aoqfTFZ8h73Ebrv3MVNY_Ef-GBks0i8mB2v9rBB5m-aV5vSK1kEVQyMn271I4DSEMmPDAVwfXwf_-QES7wrvI-_Gzjs9KaZDro3ZAoT21_gSnd8j87gmcAKtsTkDz11HdT-P7JvQZMwYp-sikr4mlcaxa2L8JVjBzAKIqgZKJta30omUMmGL8eKfKkXiWUyQmWUWh-pqhSVVoK8kWRbSDvBdLzr64eS1trYIWYu8QodGsc-AU4GNN5uuJpnMZD7zJZs5XJIwM42Cuxh55tZXuUgoAGUMTZyQMY52ZNqBTW9vZSGx1gTKRgmRQXhwBI6AGFFHC_ae2vZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌جشنواره‌گل‌ژرمن‌ها درشب دبل هاورتز و تقسیم‌امتیازات درجدال هلند
🆚
ژاپن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23480" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=Dk0muhJIu9cWOFxv_Ke_aaQC6FEr3o1IvPx26YNj9R9_WjvlahLjl49bI7QE9SxZZXrzs1qrsAnuNZ5-t-ryRGV7A-cSgBQrPVmHbqf--fP-mKfIMWmr0H5m-Mpvo6f7vinaS65-XwOxmcm0w6A2L4HV-WFQPm20ZhSuhP7XBQ1FuNIV4gbS_mm03Fcu61Ydmn8izQ3bAFYKJA3PszgV8uwQ3i0wWH2ab76jwn163YqwevDbp4WEoSruxQQfYVbxL6Rp1Fi74h_7yjYTLVhviqnuuhGQnzdupL5MtxIM9d1IKnqEPVqjR4d-YC6zokPC-VIOigdUzkDG36ZVRRx5Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=Dk0muhJIu9cWOFxv_Ke_aaQC6FEr3o1IvPx26YNj9R9_WjvlahLjl49bI7QE9SxZZXrzs1qrsAnuNZ5-t-ryRGV7A-cSgBQrPVmHbqf--fP-mKfIMWmr0H5m-Mpvo6f7vinaS65-XwOxmcm0w6A2L4HV-WFQPm20ZhSuhP7XBQ1FuNIV4gbS_mm03Fcu61Ydmn8izQ3bAFYKJA3PszgV8uwQ3i0wWH2ab76jwn163YqwevDbp4WEoSruxQQfYVbxL6Rp1Fi74h_7yjYTLVhviqnuuhGQnzdupL5MtxIM9d1IKnqEPVqjR4d-YC6zokPC-VIOigdUzkDG36ZVRRx5Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛
سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23479" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23478" target="_blank">📅 01:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXjEXmbju3VbKNy7FEoeule6j6VejgmdxIPa_2_xVgMJ3FV-IH2Gz1vG8QnQn2YF8TJXYQbiWEGXClMSoHaTXPaOwH9beeiAXDYXkJ2zvDT6HACKOBV_5ekvGDqnlZMSPWjYwDfe8TkT3ZYaFOcAzMUCCujq-SQKOjijhN4gSPUjntzAujqEHaR7yioBCgs5gEq3l80JSE6tsaozJkGsoaBwoC1AeHYq3JvNxtWcxOEpfmYuhljmznSdm1QywYP5U2SEX5WNCrqBnXPyBLCtu9v10UNjWff8Z3BnEtesm_A-QJDE-mHdqDS0e-mlncjN9kbp3L9KXnFy1zah3kitbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23477" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=kgCTTWkzJJidqaixlZhVeqIgmicFdGyzuRwJu9BV8tD6kWPlCBVu4qW6bMfN8VQoq5Gk2cmDxTKpRbtzWZzbWCAf5OAkDiyZFFb0Mbs86N_3YU0AjuZeYLH0gVx1gxMciUKSEkKIvdTOOku9Mr_St6Ite2PYstzijqRijg7dhlG3ZAUmBX5eVBeaonrzcmUZPmR7yPGzqRosU3Sdcjmb_jMbnEtK4SxgdolFQsQaoeAajSQz9p8AtDLerNoi_c06OqHj5xqBwfAXEPRrgDco9ZeQCKRfVArJeZuC6K00ivbHQlXTo-ToDRCX34iXK9zCfsZYnuLLs2tsnaqQOC80Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=kgCTTWkzJJidqaixlZhVeqIgmicFdGyzuRwJu9BV8tD6kWPlCBVu4qW6bMfN8VQoq5Gk2cmDxTKpRbtzWZzbWCAf5OAkDiyZFFb0Mbs86N_3YU0AjuZeYLH0gVx1gxMciUKSEkKIvdTOOku9Mr_St6Ite2PYstzijqRijg7dhlG3ZAUmBX5eVBeaonrzcmUZPmR7yPGzqRosU3Sdcjmb_jMbnEtK4SxgdolFQsQaoeAajSQz9p8AtDLerNoi_c06OqHj5xqBwfAXEPRrgDco9ZeQCKRfVArJeZuC6K00ivbHQlXTo-ToDRCX34iXK9zCfsZYnuLLs2tsnaqQOC80Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
عادل‌فردوسی‌پور در ویژه‌برنامه امشب جام جهانی به این‌شکل‌جواب صحبت‌های میثاقی رو داد: اصلا حرفات ذره‌ای برای هیچ کسی اهمیت نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23476" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=gmNDEvVL0iJ5k4EYdWutnHhsBXj2OQhx0Lj5Y7cfvvteuu572dF0fhLoZQCAoRs0knIKVb3xrV3W4pecHXbvOnsVkSB3wiucSf_lBFzlEdReELyg8sX0LculEfHG8Ja9QiOaxb7hyllkI3reH2OyVDH3ExMsgQOfN6ZWV42ImnDqMyJPCM57vlAXZPxv6tlfH1N373Rlk7M7ssDmj7qexX5GLEzY44chRydJdPD-4f5vjKYIIBe4SSIj8MGDe-3PeNntcOcMhdjL-iYmvFqBcE17KK348GxiO8-hLWVAwcufMNH0-__39eeQVxHv3vaEduqfS1EertP965AeYI4qzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=gmNDEvVL0iJ5k4EYdWutnHhsBXj2OQhx0Lj5Y7cfvvteuu572dF0fhLoZQCAoRs0knIKVb3xrV3W4pecHXbvOnsVkSB3wiucSf_lBFzlEdReELyg8sX0LculEfHG8Ja9QiOaxb7hyllkI3reH2OyVDH3ExMsgQOfN6ZWV42ImnDqMyJPCM57vlAXZPxv6tlfH1N373Rlk7M7ssDmj7qexX5GLEzY44chRydJdPD-4f5vjKYIIBe4SSIj8MGDe-3PeNntcOcMhdjL-iYmvFqBcE17KK348GxiO8-hLWVAwcufMNH0-__39eeQVxHv3vaEduqfS1EertP965AeYI4qzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسپویل‌ازصحبت‌های‌امیرقلعه‌نویی سرمربی تیم ایران بعداز دیدارفردامقابل نیوزیلند در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23475" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4L6erl8_qfOeXdOR9sI2xzcsfnwwk6_b8aIZEO2yTN3vNopqarAUxcjjdL3aQZUKs8qIuUKbWQgopMNpQTs_3iwdbTo3ItByTiy2VCbWs_4B7GWgC4b1DJJJZsM9LB6QSG3z-1LvGvHxdhueSCq88g6CYdHr1Hd2Vg0qWL_SLydEEApGsy934Ea7WNKnI4A-fYE50cYo8wiM6ncVr-p9YNvNA4qcD2LLjYoVukuj0W-eqzwLvno5_Epvwx2MdndaO_h-rANmuWPFgft1amIfdWEbinwTLozp71RVYjGXEyFgR8KnSDM_KxBF9xs_uxsZ8jSImQgHSHAQzQxUmfjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ نخست‌وزیر پاکستان رسما اعلام کرد:
🔴
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد؛ جنگ در تمام جبه‌ها پایان یافت، مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23473" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8n8AZ_VuxDGsGpzgsCjaykZDfRtOsTC2KQbtnk9DW6GbMfBY4Ra9BTSy8Mu7stQeLAoRwQ_Ej4wgDYiEoOyLyE91bYfmIPlDkjeuIk46BDA6v6SYR8QSsDganZOlYS6Al3uXsSqyFCPWU66sadw-0l6a69x9cci7SYtzubnbiuL3IdFGzIivfS8BMrELi26-pk7E5t21gKKi-_NkCB9GI-g5sDgHdoh0EKuopk22OgM2IRylP4NPPbM0AyKhi5rVvPT4T-Kl_3RJtxEHsUvkbZygz0wEBKV8US4WDZuUCzwvvC_cz8YUrumB0CAeJPwLWBtVeZVNPs0MLqdPZK6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
#فوری؛ گویا دقایقی‌قبل توافق میان ایران و آمریکا رسما امضا شد. ترامپ درگفتگو با وال‌استریت ژورنال: بزودی بیانیه‌ای صادر خواهم کرد تا موافقت ایالات متحده با توافق با کشور ایران را تأیید کنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23472" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIBwNqzCn6iO2ynluQIdhLa1GXWYTDQJxlbeN7Z-I4pnZU5VZALVDbWCK9-b9Bz91euhwi3We26LqOrb1xJH0hTcDzPF23qCh3lD3g-nfDmWjNk9b2GmjDfCZrbDvQujfYkGkPDuj41dgEfHljqzW3u_ICTUjskIH4auOaLnrOKnM06gOSFsim-0IRKUkDREMnKQEnIOLVyd1XUTXzpwxOI1SF4m8dQfRBSnwzFKudx9P_JevabzVJOzw8KntmbV8MAZqd6bI8rpNZpBpygAqfS8VJzRuPcfYJz8JuPac6RFHULlEgoPhx--tnce3xztx3wnJhEoUbzUG4APgrComw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انزو فرناندز در گفتگو با ESP: به سران چلسی اعلام کرده‌ام که برنامه‌ای برای موندن در این باشگاه ندارم و قصد دارم راهی باشگاه رئال مادرید شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23471" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psWGpE0HeZQw8HyFxTHilrVta8N_tgEMwouSVkxgbsDuvRAfX37Zv3Ig4AczlDHOOcfQ65DTaxHqub8VIrR8cq5BDERkytBbd1f82w26uMIYMQEtiW7DXAJ2lkB79f0cZzhaZe0QNYCd0VeGFmtUlYVdy7xDKb9TpnqEWfcvXW5sGS-IRlq2au8XC9LVPB_7iFp-ZWUx6KY4Vj5UIiujhn5pS_xK9elTXzQ_iNwyy0IMoxWKIhX8HaR7rYpFqrUIMhMTccBuK4tYune5FWoqHdIZxIPkmiT2cdhkGOSFr1mwSBwQPm8Km5f_jl72-ebsi9eZGfP2PR8LeGcxnlRVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#تکمیلی؛ رومانو: روبن آموریم تموم شروط باشگاه میلان رو برای سرمربیگری پذیرفته و گفته با هر شرایطی حاضره به این تیم بیاد. سران میلان هم گفته خب باشه بزار حالا ما بریم دورامون رو بزنیم اگه گزینه بهتری پیدا نشد با تو قرارداد میبیندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23470" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmlAHhwr2BUzZpT6_DGl0y3vqStCARrbOMHo_eysgqzh0858Vf6UBGa6xQRIO5esDgAz5J706Y7gPqcNwsrGRMjfz_ONX5Ii0v50hs3Y4wb3XhfOlm1Js8mOnP4gqW6A3O4iqtF48pBOuEY8Ccodniy3cSMh7vXD5g72WX2CtExLuzfiPZGeUJPTovGOQq3YffT1AvaMDeW7cTSD-CX88bt4E-YNxxdkXQz9qrti04jL3pjRKCwrZ-rn-HQjJFHaaBmaT5Oe3zSQ42qbo6FYruMGvNpBTsMDYl_X6vlL0OGYJR_MlnzOlc3p_ohbc9CcRQVF7QuPl4arfnqTZ-8Dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23469" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf-OKcTVmUG59viNQDpjP6d6yK6r6mbSEKm9MJALBHi8GoACaatUwF6VnO_WI1Lwjk8xOlS9GsTxJDzU1C7jof4tkiu_I_QFP_-CMGy1LyMqUoMehjzpI5k65tVqCSQ4auNqd4OaEHPiDMfnWi-fW4pYP8nEujVKNTNJAxU2BqEdT3gSoqXJYk_ZpmHuzcAuU9D1vOh64gqePyiqVVfVXWLWnRB3Hse4Bwhg35tGvgp2NIbts_0-IE4VhBpno7um_u3esCNmKzlElYgpc63KTg4pc1wlVlkoQaAs5LfLlZDGJNyKr-6giuqPh9XcwRLLPK3NBJ9UXWo8LdsI75qI6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاریخ‌فراموش‌نمیکنه بچه جون؛ یه زمانی برای یه صندلی اینجوری داشتی خواهش و التماس میکردی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23468" target="_blank">📅 23:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_04-F1MEcqzkHzXYal43PnVtWEyTvsYxiUL_HvVVGlgsFhyNoRw5MwnuXGA0j5V2JW4J__nxuQzLQjxE3kBOL7j1XaqDZzEFXblVcgoiHld8Ch1JQz7yPcqaam8h7SCnR-2mAyETfd7_a4tKUKy4fwEaA-L5t5203w4XllAW0kX5DX23QVRFqxWDLw7dQ1NSsVuLD6K-oPkGdl3RYhDtLcpLx6xK_lYXu4mfQ_Vji6Cf7QtY7QQPsW__jQ65sBcW3TC43QO0hiN6JMX0IFT80uMc083PRJZ5a7YNZzMMNWDVfWDcxpk2E5D49F36sThcwm3CBKLiKxOuwD-ZGu3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23467" target="_blank">📅 23:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=MJJdG8jU-_GKA-qu1J58F-_O3nr-IbTi-gI3DT1l9JLdTdKDkJoydbPPfgyexmpLk6sbcQdC5yQ13i3T8ni-WFk_mqf0NfwXvtZsfq-rWFL_vEHszqLc4G3By57oO5Ro_2IMBET4JOUqH9XHClhKj2SalyyoDQMDT5Foz8I3HFFU5JP2zpHkiDHABPjWbwebydkknO8e-oYSpheWy2BkgTGq0CipObqYnw1bRK9YWKbCI9pM1Fe6aN_HMeHtwFZvHagtOEzSZwZc6BfkBbzvkVHcGj1jfS4bJxdd-vOHOoAvehEYm6j4xakH9KVJjRjdno2Jn_wEpNb_2dbxL27PcAamKk_tn-FeO1To_Wktzs52B9LRzjFpomj16UD9924z_W38NRcAFR97kZnrzx-WtqGYrO7l6zIbeHpLgSeTGlHatyNg6JclIIk2wHp3kVrW8ucGxAkHQ4sdsWuK8iLeJ-E_wBcA0a1mP56F9Bzeb30isAUrDeZu8BTyYo6aNnYpDuPJWgjAi5siqWdrNq6MFyWvOf1OqLKw2uKd4cq1tJU9GUeX9c8yCtnOPMO7dxTF_fYf2dSfoqwhozabsv5ApMZ_97lJ4ZIl1KwaxSx2nckT_M0zEFtr-uz16yyIac2CzgRs1XJ_0AHi1sxepEA9ASYS-NK1mqLOEyVZEMwRzAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=MJJdG8jU-_GKA-qu1J58F-_O3nr-IbTi-gI3DT1l9JLdTdKDkJoydbPPfgyexmpLk6sbcQdC5yQ13i3T8ni-WFk_mqf0NfwXvtZsfq-rWFL_vEHszqLc4G3By57oO5Ro_2IMBET4JOUqH9XHClhKj2SalyyoDQMDT5Foz8I3HFFU5JP2zpHkiDHABPjWbwebydkknO8e-oYSpheWy2BkgTGq0CipObqYnw1bRK9YWKbCI9pM1Fe6aN_HMeHtwFZvHagtOEzSZwZc6BfkBbzvkVHcGj1jfS4bJxdd-vOHOoAvehEYm6j4xakH9KVJjRjdno2Jn_wEpNb_2dbxL27PcAamKk_tn-FeO1To_Wktzs52B9LRzjFpomj16UD9924z_W38NRcAFR97kZnrzx-WtqGYrO7l6zIbeHpLgSeTGlHatyNg6JclIIk2wHp3kVrW8ucGxAkHQ4sdsWuK8iLeJ-E_wBcA0a1mP56F9Bzeb30isAUrDeZu8BTyYo6aNnYpDuPJWgjAi5siqWdrNq6MFyWvOf1OqLKw2uKd4cq1tJU9GUeX9c8yCtnOPMO7dxTF_fYf2dSfoqwhozabsv5ApMZ_97lJ4ZIl1KwaxSx2nckT_M0zEFtr-uz16yyIac2CzgRs1XJ_0AHi1sxepEA9ASYS-NK1mqLOEyVZEMwRzAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی وسط‌پخش‌زنده سرودملی آلمان رو خوند خداداد از خنده کم مونده که پخش رو زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23466" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی2026|جشنواره‌گل ژرمن‌ ها مقابل تیم کم نام و نشان کوراسائو؛ شاگردان ناگلزمن در ایستگاه نخست رقابتا حریفش رو هفتایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23465" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctfs7oUtthUeorRNcP0M6CcUxsBeL9l1OFD85cY9rEK_HRiY-xPtv2XlDicqld4T2K_rDXZq_U43Z6XGba0RO85AakjpZ1JEcNG9F54nlzl8FQt1qzv53b4jDpP_A0Ar25SaJP3-Tcf2gYu38qJVgL2sC_sXPiH_sm81rk2j-bPnZbBiZDYPdedO15yCUDNw2UFK4Qb4PAvkNsveRltbYyN24PVdNl_y9EfZ3RVyaqlji06QJAymtprv1b0KUFS0DICXeqkgDEiFcqKWS0184sZcb28jkxp8S4Z5jc-nbjKaC2C2uaV03UnBs1U5WBikGBNCc4MYO0BIGdE8oegBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz0rkMvF8Zrme0hVtAPT06_hFFxERmXOKuqr5mw0dpNp8VUqhoY-jDOyB_-5TBfJJwVcb8ALXpFy0jTVgozn262k_TGHXkN5li2pK33-pI6v32jrR685Pw2pwQ-Ve_hGlaau1ixu5qG-Gwz-uU82CKa1g1VpMvVy1WZ1w3EabJkCZiDZ_FwtEVCLPqSYsSaV4RiEZp1MI27DjaiJfLaKcocg2tjwua-dT2KzhNBEwmyuuZfbMtPyWh4-bMOWXHb0-7x1zz1Uuc7UoxEzzmyiWMnAZlXLBfIn-ElvGfNoPD4RcuFuhxkeMx1opVpOOMjkK9WqX9bK7MChSrH2UD5tJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cg6peM3lkfaZScQ5buJyZcuEDM1KIjaqAxg_fZsmA1Yfr4BpS9yhx-u_Kfcc9flpuSBQxTeoIAPboPmjtyllscjSNZFW20Js1x7xHPm1JQs3CiVw6bBev--0fdhuKNWuhzX8B-ZbnnaeKgiGJ-U8uY-vOHp_jVAxbmXUhiSE5-CUrQmgmxcazHRDgMbWwh1E-oAQ44rQ0lk4TDoEmZWUhHlHaNWX9GJgoapEXTlD64VvZyK2k5z5zsqqhoarsXITkdCTeZm7Rk3emrtE7pQwVIQ-LDtrGRz0xXoY0arZYNw8egEAa_1xIOVnXOiIFcI5x6f-2ONNdRtFRVOItLUbDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی
؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1l5bAVpd1FDrJO9FWDxzpNeezGG02sKos8Bhn8shGWdytXSLfhjOjjL975Lu4yC-J5ULr89BRqR2XwSgxv6KtvDtk8YCjg7M2fItQLvV4-HDCHz1Dl1KWbqKoO8AkJIlFwTXwaPVGVpbkxf2qU39mS3YvXgyfqr1ZP1DQZ_37fK6ItdObCEXnB2gkr5HaCFIHegSG0-ZFHR6-_1uP7zg7z91tjFSAiMEOcSPryqhUuKpTyMA5-b4GkH0kVj4pgwsX8xN4IDSAp1GZCrG95kXt2gGxNsMLKFG8XHBiUaTqaxMg7YJkNCshp4Hk41WD5snq-MtIDZtKJJEkoU9XA2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=jvrKMtiC12Ugc0kSv2PQ2xUg3Vo7YF8k97mlfyYb9fvnEdXh8EA4rttdA3boO14h7b7wrT0R7eFVmxs3L7iuvWJoV9WOM-ar8hCSbFvD4TusPZ7PR7NE9Wu4CGQglsIgr0GWn0sjpxzuTeZr8X7SCoIbJIqbCAEaV0UJ-P4rdMet_OjrYY3PZ58udnO9jbdKUPLwojZlZPMzq7WJWorKYDYxV7qeiW-RaGhysH-ZLmykJ7xrulgCJ6e0IMETj8116idH21OWi3e368vHrVzE-g0RWh-_r_93HjYtPVQgMa0XhrFQIgAkl2-fCyvaCFUbXO18r9NXN4ixTaQapDP2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=jvrKMtiC12Ugc0kSv2PQ2xUg3Vo7YF8k97mlfyYb9fvnEdXh8EA4rttdA3boO14h7b7wrT0R7eFVmxs3L7iuvWJoV9WOM-ar8hCSbFvD4TusPZ7PR7NE9Wu4CGQglsIgr0GWn0sjpxzuTeZr8X7SCoIbJIqbCAEaV0UJ-P4rdMet_OjrYY3PZ58udnO9jbdKUPLwojZlZPMzq7WJWorKYDYxV7qeiW-RaGhysH-ZLmykJ7xrulgCJ6e0IMETj8116idH21OWi3e368vHrVzE-g0RWh-_r_93HjYtPVQgMa0XhrFQIgAkl2-fCyvaCFUbXO18r9NXN4ixTaQapDP2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های ابوطالب‌حسینی به بعضی از مجری‌های بیهوده،دلقک و بی‌خاصیت صداوسیما فعلی مملکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyyj7zINx9sIkoimAsrPFSNGFeHdVrVfMPml_SLcwL_I_NBKobCC1v3hqwO5bg6-tGYOlJLerKV8eEkwoGCaxcGO00d8dWjgMyFQ-Dc09RxDdE7puiq176oKfDuTIRp-G0aVowm7lRlj_-q-VafM3lTvO4z6ugiJrRPFCbdbS2pEAygd-dqm6DQnGoiejNjiah2jGqbpHEjyFbAqzTbd8TrCl2M5vPSWF_SIJ5ROWRCKYhOf1LpCVDipHWEQ32_6UNheUCxh-q6BJEm5AzJCj4GKv-QTP-8Dg2UZZA7JkEkXvRRy6fsHnbgYTiwIKfumOjCyR561Fmtjk63SjpbpLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX2_gxKHsmcEuiAAqbRma8sSjZs3z-JGaqNW_WGE8_TX_1OZDi7XK46f2Th2NOXGYVFUbaRki2s1uc3Alc6UCqD4wEMIFf3UbqZlVvo7_CZlk1xOhH1VqST1wT9fMSsDtACxKdEicP6cIbChAJ6Ox0fbcCdA4gD8dEowcBOoQgackwfIvy2uYXX2o3s4_QxafH-iqIf3NkB4oZIBzwnEwJiaBU9OHBGA5KyPrFH4S7gwncvlXGySLcnE4Cds1uXl8hgY1NdUJ0gLjl-KM-n7JI_9zQeLu29zn630TA5fPP3AmBNCzdJWU7-rqKp6XYctjsPTtrFCiLLD-WOB3hH2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkslIlkuxejxm3eNHDWP8yULmmKI8_vSi-kV3wKYcjKFm6R4oZrHMoCN4fFZQUtV4jwGFKAVRdfOtJdRBJ2YAvcQIIl2ppWRQHR2SJmXjgVkowQzdldJbbfUZNTUlXYkBhnlqfGa1WPCbWh0sfcurJpgi2x25YEnkAuZLH6V2IjQxQzKvW8eYRCLRtr_Gg8QisFNM7yTT9or0TRlF-p8-D0cC0IJ3Q92X0fb4mOcesBfF1Z558Yz9I3cxXSC4GTK7chtYZC8QynresmCcBwPJ1kamBaz7Xm3Es7YDiUHC8-XdHsNszxW4l0v-ucUCZ0bnJL7jOB2vYC18Bt6wG6tug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWbOnVADTjWpvvSLkjX_Iyoje6Lk6ZtkElm9SBiTJ4Ms6l3ru502F7fUF0l9yiIddV2IygvOPBzrUn9PX2wpKOFCKapN_YKB1fw14Fb-qR-Wl57ZtADDf9qDFCTfG0Ik32pU4RMuFWpyrRXprPwn_oIePi0jTEjEYkhUTaByBX1mglXkv0KEEm0L8vWRH-cES9fNci-ONHrrdE0-VzzfJcnOxVbGsmJVZt4VdYOAOAUOi-3t6qc3_g7FnPrcaNiRc1doybl3hBSlpQ6oOabJpivAHiR-4tqGktK_B_svKADP65BxOdFrPRrvyBvKO752cpz2Wf39MoJQsASGYJpyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=tmdwxch5IIkmZWPwSzd09U3zqZlAh_x8txwprBOACjEXZHmnKOeeQL4LaMvd3o-tdfxSCAPmYaox2kACTvyG1nMhWP6vLcZrKU2SGcJwF-EL1rT6r8kUg3Zg7HmIncKuGhFNecHcwV_kRYC9J-psaSjVfBiBlV5mewsz1Wka3fSK2SdFaIKwhJpatNeQCecinDEgps2ktCj31aBTDhOXsonSwYATL8H0voyaeqziIgALWKS5Y2oJiEiGI5QZ366IIE-PAWmpma38VL7zgOTCbOO_Czj87mjdEUAuricp79irFi61axk8RNcAsQLmlt-5L7G0Lt4gBOs4G9_x2RT3vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=tmdwxch5IIkmZWPwSzd09U3zqZlAh_x8txwprBOACjEXZHmnKOeeQL4LaMvd3o-tdfxSCAPmYaox2kACTvyG1nMhWP6vLcZrKU2SGcJwF-EL1rT6r8kUg3Zg7HmIncKuGhFNecHcwV_kRYC9J-psaSjVfBiBlV5mewsz1Wka3fSK2SdFaIKwhJpatNeQCecinDEgps2ktCj31aBTDhOXsonSwYATL8H0voyaeqziIgALWKS5Y2oJiEiGI5QZ366IIE-PAWmpma38VL7zgOTCbOO_Czj87mjdEUAuricp79irFi61axk8RNcAsQLmlt-5L7G0Lt4gBOs4G9_x2RT3vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr8g3z2Ak5aksXLVSnR4DhUxVbnIukAdswKOPrMahHyDUUE6-npOfhymsvdm3nbcSeRMW-QsAuhM9h2M9q275VAPOSBKAq9YPtuD5lRhiasuTYjjbYtDJo0x97IdxFje2j1MZsyrY0ZPfRFJLQIAG-1gtII3nwhpRt8wv8AEO5FNRB7bKNPbVmho_jjjveEZuKKXjhffjcCEhMUxrmhc8zCDaTRWe3Ahlau3R9LgEXvHXtEl7iDeBRRQBE7gSyyBU5XeqdR1y8zeV4fNsNoaNIHXQmz6oLBufWX7-c-JtAdMNk4h4Q7diQ7s4xAYbmS77Wv1VWkPNThxGM3CmXvGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkMar5naoJFL7oEW17Mxr22l1FZH_A6wryzzAEIW1ZJP9smApuFtq0ubgVDXGNUohl5sQPF2HkBdGpB_8HB2pm2gnV5CkwF98DAS7ZB4Gn1rXbsjTKu-TL8ilEqahvRvkXba1JjFDjL5r326R72pr8o_oryjGHzct-ykFDsMZvBFv8eqVZDUad0fNFTRv0-9wXPrGTZmN0cy0LzWZUaKeg6eVWX1omo_9OBie53-YTKjOhLL9voM81ezn2Nzv6Vw29mp8l_4uXh5c-0Z2B9xa49Lh0osOugVN_f9dIU45KOnTHWPG0uVcavwOETBx3RBivp8TWIQX6mY3-NF5es4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Dd50RzjZYNRBRRQEnZUDgi3ZIT5hNJY1rdPSXVXE0dLwNnFIUPkM8RlLHYDcXv3ZwdpI-PHeUROc_sC-c2wGqk8ZP62ivSJnvmYGephh0xMVU8itmR72ecQkrgJG71o80ZuynDkxL_8Y-6xRo61HtQAe6BG__37IofiYMZ604qk7MZ8567T2zHZSQfLuAjhBa28IUVH_VgdcG0IBoZoToodvdwgqlyFkzYcVhIPTP7WUr3eOhkcwxuB0Z665agY7JTrHyNr_ReOrCWu0OVfppK0kxoOkkvbIDNdN3r85GHnirkMAm1q91gV1IQw8TZc7JClfyA-7gG8j9etP0HAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTGK2bSSb5aSTYWWebDb6hU5DYK8nr57iZLfMInIk9n1UUOi-xUzjTIN5WdEOWiGf1XTMDg6OUMQbOIDhpInJVqJ4J19aNpJ8L1i4RhwdbdVGSDld5kolKU0tgEGtm8rxojIDp10lCRgHKemRAB69v_G6GqI9yGoAK8INgAZrnI4aYS66Jpzai1DzhTzEGm6F13BYNlx901YILB6p8a184ZXJZJgoKJff8jhw1zcNubDNfdeI4lamHuzWPz0mpCaNGD3Q5xTLcrjMbsY73aTJQ2e_xnEZaCWCtKL6UiLNMHdCU7LXF26nBfyxdG30vjASo8gKiOg_iVOt7aNDWqYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=rGfq1FTZa_GMd0FIJpGxs7AuAW7ic8QdS_hxeDpu2On0fctajqIZLMFpOiThyKooWNlKDUB10rcVtOIrXQyjT-OhsAOD24iQBpbb3QFjeFDDqiwXOaxTsW4Z2HSngp0gQgDyfBrFs060LWbP-uWOV97mKSp-AKRGiEAtGn1kHHrStkIWQzg1aiIbctDLFOH2d0RKQwHXSvb6sJfmSao6PZkeTnwyBVMJR7z1EK-0BRZ0ukxg5iW7du9wBGn0xUMyEE3XBd_Zc74FUGGgjpkydBKKr5HaRrBCNe75zKecKVsKNovOWhrOEqK0tR-qofDedj8kPH_pVZgsYBJFsZys8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=rGfq1FTZa_GMd0FIJpGxs7AuAW7ic8QdS_hxeDpu2On0fctajqIZLMFpOiThyKooWNlKDUB10rcVtOIrXQyjT-OhsAOD24iQBpbb3QFjeFDDqiwXOaxTsW4Z2HSngp0gQgDyfBrFs060LWbP-uWOV97mKSp-AKRGiEAtGn1kHHrStkIWQzg1aiIbctDLFOH2d0RKQwHXSvb6sJfmSao6PZkeTnwyBVMJR7z1EK-0BRZ0ukxg5iW7du9wBGn0xUMyEE3XBd_Zc74FUGGgjpkydBKKr5HaRrBCNe75zKecKVsKNovOWhrOEqK0tR-qofDedj8kPH_pVZgsYBJFsZys8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbCuOrp6HglF3i4_HyH3tkz4G7RP6LwRDYzeO9eZosvz2N1WTsJDR7jDiCecoLn74NkELvSvkxfbGFDFmkhWJh64ijXRFohMW9w3RPMIG8FK7nkxtYJVH7P8y2y4LTitzxyaXqwck0fcboxUpqHKoAZQZzO_oly6p1yY4KoCgwqKrU0aMAUgA4fKYjFz9k1teccOV37Vp9OLDPlE7kqtkcXMNBTuqEVjTPvcunNFBoNVLMdbmwkFsH-TPvS8EEdHiX8VigzbVLvNvmabut_FYVf8BbosTqGpKhdt-tB5MX_4VShomRgMBs_7LUQRYzNI_B_E6WeI3d7xqDCJpY512g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlCZ_pjK-8SOATLqj44O-yUikEMkPsK4LpbwJIYh85Qv1lOH0551dqadwW9wsK2j2yRRIELQl_5nNkE8yBlp-4V6q4qCgA-z8tfKP-mLQEndpavHIW7x43sxp-iruJ_53V9P9fOQ3X9k_A5SWONMZvWLAIoJQkcAqGKgsCouDIJdkEY0-qohfhBb363IXgkq_v-54WThQCt7dNnXYYWs967Zk44VdXr6MnGluN9YwPs8t9EIDxN-mK3Ux1spV2_SMhBgTSJnyZmg7srJmX2UegZV5Pc1XlfEjfhcTQHQJzYyIUdy3qJD1e_fM_uFGKnjY8NKdg5Bz_O3McAwnjWfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLSBxDM-uaeJaQ0NoqpLTr4X6T6Wwdnn9yFGbPC28NEz8Oeg5IGH-ML0NgYvNaF-OiJ6tt7kOZXBSIXGRIASymwFPdgJFzBbEwCG3UkMn06IesfclGMU6TnyApUMX419Zc-i4Atk5ylNF1xhxtYZPwm8ktZIlDrN1JF4-8Y9U4Yom9_Au4Kxznpt9BIhbIG48tbclQDqnBnuDV7SxgjYUVbhEYWLbn6Huvoa7HaH19hpC2oD9Zw98dgYhYD6H6HTUVL0QTZOrwVE_sEUZFAl9ZBC2hWraa9ZjNXV0LQ0eFqPPLvbphoyrWWmlbrGL84-Ile0XC2XXnC-boAOXOmbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=VaZs9meJW7LuessBW17WzDCw_NJ5-lHUnS1WJJ3-p2Pn_ZvtXwPS4zwDGCIcSmqbwTolndcfB8QgcyrebRQmpDfJMoWV3nSNtOp-vo8rXKntJU4-IP5IGsD0OP6Fsu31KmcLVf2jMYPPbZONZpETurCypHTOOLgCsIti5H1eNSHtAXlHnpy_YPe9G2m6ZjO6zHJCTeEHGMFXLy_vOXb30BlMEqMNBFZOBk-ad1KTAtP0kiDkKfYNDlHpr9_BdRtmtixkyqAmMH2QZ7IL8yvKkv9zgCe-2SqhLtrlhlbbZ3aMap9uwhLf5DZFmHcRVwAvCcSdzzgi6tB8f7GPeL4bUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=VaZs9meJW7LuessBW17WzDCw_NJ5-lHUnS1WJJ3-p2Pn_ZvtXwPS4zwDGCIcSmqbwTolndcfB8QgcyrebRQmpDfJMoWV3nSNtOp-vo8rXKntJU4-IP5IGsD0OP6Fsu31KmcLVf2jMYPPbZONZpETurCypHTOOLgCsIti5H1eNSHtAXlHnpy_YPe9G2m6ZjO6zHJCTeEHGMFXLy_vOXb30BlMEqMNBFZOBk-ad1KTAtP0kiDkKfYNDlHpr9_BdRtmtixkyqAmMH2QZ7IL8yvKkv9zgCe-2SqhLtrlhlbbZ3aMap9uwhLf5DZFmHcRVwAvCcSdzzgi6tB8f7GPeL4bUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-m4SxBYGOe5cjFEpmcfCMXbJTaWnUa7ZDIFJisJl4UUTSb4rL80ZJ4pSir9GNns82QEpzLlguyX3fckE1fqpaIDml99Wl2U7b1617AWj239td7Yjx-eICzI0Rr7yBeW7vVkWRLOZLYwAlD54HkfAQfpfCbCuxQ0PpovugQK1mIhDxIXEwvh6w4o9uiqZsQ10MfkFg-1A66NjE7EGlv2swp_0tAVi6cbA9GJd9EGmLyWQ4CIXt20iZ2Q8fnLeUOTf2-uCm0B2wrwgCW8ikU3yqWkzw3NcD2vgkQ0bJ2tSmqvi7AON7hPLdK_HjjdYtsexvyoe36SpbHVN1ZrRu9Kkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOHvrftEGlBsb31Z1D-h3DTmVWQMQS2a6QueoqU1S8JZTKJiVxf-vWLUNBfh-RQDxx3-o74dRgnIqkNLY-TMpIe489OJVqDilSqXt6WlTzPvXzf8hTke7Pq5487aPHjsuctfJk2xND-Av676SMaOvc1wEWw2f4VRGF16mtvyQX20vMagLL0i3s1VtUqx9v15AWlhiesoUNksZyDSy3q0vN5Hk3QEWdr_TWaIbz89yXlT80Vxys65ctGJweghL89NwXHGMjQ8rdnE2mD5DrLMfzq2_pDE6wQQ65FLQhYL3pHF8BelX1bnuOWnG5ELV-S1vC3QY6ZXKoQznJsQSr1Z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVuTiRiO907W7tNvEEDGn2ds39dmdaNXBwMlbdaQdHZ3u2A7JRqAJq4z_eilDDWkuZnymY82DZ_lni11lD7VYCZDdmnXgMESHmx-U3PbauEJdwwfy2zX2Fqieme01uu2gq-_IEx7789XxcYfGYtWQOjK35guv5iaqgtt-p-AJVRSqVEvDcEs9mGAuMBk2vAFnsGUGe7aohbCdXctepbCGZTYiVf9L0eGwy9wBlVGg5jgkl12BYyQ9EfM0uP1hUk_dtFTHoXpWV_1beuI_ZcFyC2aZ02tkV6S8T6SWLGIG8Zia5Adcw-vExMuFwsTjMlECJiagk9FB0cWAlHYxXCefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
