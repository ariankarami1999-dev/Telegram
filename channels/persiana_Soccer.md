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
<img src="https://cdn4.telesco.pe/file/GBIFt5_l3E5RvyyurTKJXJqGSAxjUXZ4GtnuSkx76JLzPmlA7xjEdc551rw_WB5mWZSBIliwPzZuql9725tHLiqDL1dMvC0W4d8VeOVZ3vtqym1J35OId01CDRp9odD1MZcqGe8GXK249aiEHnVIjcH8hbHgXxkP6ga1A05gxv2usVDQcsmJzuVmuGGHbJIRAe9dq3-bjscYe5KewdUkuelfl2NqiuwmJzV-JuJQ4WmYHTtUctm1mv9VulBt2R4GPAOosvH1SaSD3IPbFkUVbaR2UNOraSHeOyyfq1GzRHU1x0u4nFqYU3gw8Z8LTYlc2eDAWIUVkf4fVjw2-QjY4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 635K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 15:56:08</div>
<hr>

<div class="tg-post" id="msg-27203">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcW98M2s8GHK1-VMTAu0AzZuDnQt0BfD7s97UrrFxpGwOxXNXvCUjck-EYdtVzZaGIivhqwFcxdtCG4JRC_BNXqFC6WUS30LIAC3wBPpDAipwp64dLudYuV26w3l1jgLcV_lUFG0EzIvgBHFfEuA0Is6yy46HvQtyEnZecTURckmXAVwBr_w0vvYRUbCjH60IpYm_bu46_p2yybileDc_qqsPml9puWFsjkAW5PNPRuMuskegfSBXJxvNG3o6tw20ImHVMnvoH-rm22sqZzkxYRJMKfLr7t8zQQnySfr0R7wabOwyX9bQdBYwEpcXMHTszAkI5QY1EdOeVKcDp2OdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی پرشیانا؛ باشگاه استقلال برای‌دیدیه اندونگ هافبک گابنی این‌تیم بلیط تهیه کرده و این‌بازیکن‌ظرف 72 ساعت آینده به تهران خواهد آمد تا بعد از تمدید قراردادش با آبی پوشان در تمدید شاگردان بختیاری زاده حضور پیدا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/27203" target="_blank">📅 15:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27202">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsD5gE_RNIl-hLUik63z368lsJoDOEurCtIreCukbnCSXUXLHdhmtt_7A4T0Pjlh1lcscmPJrQBa2pGapwCGkMbjW4ioESynwYy9Fcqo27z-2jLyJAMKwIqJzHuKagVEprT3ukiLa2qfiNqrxFvrJ2ijj0pH-boEIToaGRXv5mTJPmvpxm89YpAAJvC51tEwXrIfHfNZ4pKj7Tqbl-wMCfLy02WBRzTAwO4pLvtjJUiEwwyPSV0XOCWtwyePiQs7hyx0FsAQckJeVULji3rmu6nfJl0XjdbY-XQxg0gZZ7yuJmmaffkKmmRWbdJcHHbLLhw20DB2da-4ITdBYMtHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از بسته ماندن پنجره نقل و انتقالاتی باشگاه استقلال؛ علی تاجرنیا شب گذشته بامدیربرنامه‌های ایرانی آنتونیو آدان گلر فصل‌قبل آبی‌ها تماس گرفته و ازاو خواسته آدان رو برای‌بازگشت‌به استقلال راضی کنه. به احتمال بسیار زیاد آدان بزودی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/27202" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27201">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/27201" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27200">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27200" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27199">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aueVIhvA1IobEEs2f4KMcSdLZVrAMZbDECEEJZnJm_2h_cuM_sso6k0V-VUGmCjDO34FUK-WCyHertzuYSbyb9qJQXuj1mAzpgCYY5t0Iqv_VkW4zi52wOd-OoiLBLmG5uywSCJKvP82LvA8wblgrkRKhegWoTD29JiOvFYZEx2RzeBVI9cPaVRgNoRwgliCVzs4p8PtUIu9dXzGZozrQKntFYRwrIwNeQbRrMimkIRwfgUQzrZ2LNo0P4I-ueePMx2_rB4dBMsUGau8V-43ste8Rec8in9I4ztxQ4P37dZ5arj1oCNpoDLsbZ9y1RU5bBuGO29iTq-vsjyu6aVfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aueVIhvA1IobEEs2f4KMcSdLZVrAMZbDECEEJZnJm_2h_cuM_sso6k0V-VUGmCjDO34FUK-WCyHertzuYSbyb9qJQXuj1mAzpgCYY5t0Iqv_VkW4zi52wOd-OoiLBLmG5uywSCJKvP82LvA8wblgrkRKhegWoTD29JiOvFYZEx2RzeBVI9cPaVRgNoRwgliCVzs4p8PtUIu9dXzGZozrQKntFYRwrIwNeQbRrMimkIRwfgUQzrZ2LNo0P4I-ueePMx2_rB4dBMsUGau8V-43ste8Rec8in9I4ztxQ4P37dZ5arj1oCNpoDLsbZ9y1RU5bBuGO29iTq-vsjyu6aVfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌ تامل‌ برانگیز زنده‌یاد علی انصاریان ستاره فقید استقلال و پرسپولیس درباره حسادت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/27199" target="_blank">📅 13:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27198">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvNjLfRyeImK5bzcYjtwxIxfqUsEV7rQZmN_t7Zhrz1pQ9ggw0ZDi6Oa9lDyhLy5SCXxR-LrEBA754g0C-ttfPh9cfRKoal0PeJtksidMtgpVnFZKIKqGPK-F-e8sN9QVJQwKZTwqe9mGpX2gGN_-s4AHgdIMBxJRynKaI3n8ASQqFzdy8vEASbaesw_DsbtJ6dkic6kyJs7Fja-f1aVNCuCqu7RLcayL3xqTNu8NdGUaNXXK1lAMfWU_YNSBKOHUc22mQH2O1NOOQVKWwhYpgivlcE6MR5yas9Ugz1R0X9Rz-Akm7um2pRMVv4PVWTIWbYCbFXDqy9oRpWTj-HLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/27198" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27197">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bor17LPbqOR7edqSB4pHlFSty9vzknusLq-lRBVYZuQ2sWaZxDkGqmhutg3W2JZd8wJzHsWhMFBbdyLJWv3cK66JCjE9ehTdHMQnH2ab8F4iAFcGKYO82PPI7EhfVcOco_Ac7uxFHPJbuLyi44dj9Q4SNAP3foAuwzaOJjAxS0hx0bPvHu9Ngr7H5PUuY-iXXNft5qrmdFJ5JX-enP_UgxH-wmHf-WrDXvYZ2pyHnGUwMljdpCTjph-W0YNom2ix_dCkXEL8itscFXfdan_5j1y9tVscsR07d5pCTq-74djWp9RIqNHlcdM2D7sPdxXI-MvYbcZi9K8H2KKbrj5Uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فابریزیو رومانو: بعد از رئال مادرید، بارسلونا هم برای جذب رودری دست بکار شده و با مدیران باشگاه منچسترسیتی تماس‌گرفته و آمادگی خود را برای فعال‌کردن بند فسخ قرارداد این ستاره اعلام کرده‌اند. حالا همه چی به خودِ رودری بستگی داره که رئال مادرید رو…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/27197" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27196">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHgJo16EW8CibtxmNos93kkeU2TTG4rjnqepXUBhJX15TLYy-X9rbZli1IVBSSFSZQTcGkgWjwlmX9R2BgMuj1WugYkz78kgiKJpVm0nr-AvGAj_ZzWm9pjgiF6fPMgj8V4-kYT7lkkgvsKEYBy2A_cMh-YLb7HYlBPRbjoU3QYmRZt-ScQhDbmuOfIs5YXhxMJuBHBhIPy8jssEs3OjWRGfZ3tQx-eqMbhDd6FbyDdQ51SVIjswtJj8VIf-kk-_jhhbZkXfVz69UTqaUGeSu75LqoYW0J-LeGbkTO7PXKQQl02Nv-gkxyAM44tlBOOc7NSgCPpjTNnK69NX_Ro-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/27196" target="_blank">📅 11:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/27195" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fi0TfOsQGekcSfHk94eDYkg_jGNCloHsEtLOnSwcG4hqZL0EDzJxWUu3owAD7yMA_yiRP-FIWrzGkvtXvOadQvYnHbqzTWfjEDbJc6MIPwElby43KiuYO8DTeM_fTg6lJajNsUtAqIGy_8uFCfEQFDWZ0-OXfBhSvLqiWRXPCDmrmJCCVzEtXIYdXLjjZ-IjsABqqUifYxtU1v7mG1pkZ-l-zo_7q-aMJUFcDhUqnOEc4JiDELEQMaBgmDfwCUFud26nDDi7pr1jsK872g8WWpFgALZhYM4kps5SVl-s5HcagJsvi_qPtGimqq-nWs_WLNNcFaNJYroUtADMtI_1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxq8u3bCHbZEvvNdo2XZ4Nty1h_f1KJtItVp56i84vuqk_IpZ7VMl-Z9Hg_h01-dbDq22iZeRMLwgqZxN21lS6WM9d7qwqwQOQsPWJWaLmi-NKKq0XBNKWur9HP4sqCLxSD3xAml82Qz2MLyMtph5C3eq3kquxTWMq-VArq6pUgn19uGsc5H5VnwIxaxTi4c_LL1Lj2qd3rDlv41f6iCMSJ4PBzNRy2xW-fsf_Ffj1yrM3OSScGIK2LEYUavpvRo790DwJMp9RxBcRTaAm0BJ5d2aAExd1IE_n0L4Mxt-o12K2kOje0jeE9UnxfjFHWwREbXbLl3uTLY4LGQbhdNbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به جورجینا هم اومدن احساس بد بدن راجع به بدنش، در جوابشون گفته: واسه من موفقیت واقعی هیچوقت این نبوده که خودم رو توی یه قالبی جا بدم که معلوم نیست اصلاً کی و چرا ساخته‌تش. موفقیت واقعی یعنی با خیال راحت زندگی کنم. کنار آدم‌هایی باشم که دوستشون دارم. حواسم به خودم و سلامتیم باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/27193" target="_blank">📅 11:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27191">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ محمد صلاح فوق ستاره مصری تبدیل به سومین بازیکن‌بزرگی‌شدکه‌به‌ترابزون اسپور پیوسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/27191" target="_blank">📅 10:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27190">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYhb2jmQ6INLVbaXKEJrYf9NZ_YHpfWEJyHkNALJ1mu8V2Tex5XCMUW9EXIJMhcRFgA-YNcYFdaeyKtn7_-yKjp1BW1ezkhJYs7iS-7URtjkQBLuIA-lM3zz9o7-I4P6czWjeeaeTPn4sq5Smugo-QM4VMNDRJWhRFVvxcfT8NoTlBF3lG13QyB-W6MmsPVu9gTjS3oJdfukNq8ePCWNgS1AYppuIuWucDmKNygPx6Gp0FbBYE23ELLiS2__uCLDcEeS6RC4hozPYZC9c9KGYKi2sbgTuYhOAx4vr6ws1FdEQ2uuhM7vvGDwYd0Uof2_OhwioxdxhAqYoQqtNJHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/27190" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27189">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بغل کردن جواد عزتی توسط یک دختر در اگران عمومی و تذکر حراست سالن به این هوادار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/27189" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27188">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛
بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/27188" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید.
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/27187" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX7dUGvM5uErBXi84-fq8uVoJyh7166VCmhHrXFaSrwWuuezpEU4EqPk4ZgoOqHvjJfeKy3XwStUxvDPSBh76AzN-bzL3R1F9E2l7NM1vGU-tQo_Bf_K1xJYvR37-2gGGKn0-iXoYFiXa-f5oi1mXO17qSSTPpNQn9IlJQnVAW-rgDruXLjBxhAtjORYHm89pdDTxYQjVzMIqNxPrf2nHepxIwnlS-7Z-z66mikSUmZnlT68_vbrYI_l72iHhvUReDwVCDeMtE-rfcWYB-zmjsj4I2P-aDjLsGJybkdtmbYeOVQs5eWNoV8reJGyQ15Y9heuaKCO0Bfeu7p8Hoz2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
نزدیکان دانیال ایری از توافق‌شخصی دانیال ایری باباشگاه‌پرسپولیس خبرمیدهند و بانک شهر این باربه‌مدیریت‌نساجی قول‌داده که بزودی رقم رضایت نامه این بازیکن رو به مازندرانی‌ها پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/27186" target="_blank">📅 09:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeR5mv4BHqSPZQ97stYlcrb9Y1Nq4lqkFUP8QQmV28ZucPPqY0HHDIgbb8Cf_hsoGFPOb_TlLD4O-SWT-5qk6KJZ2Cgg5FCul58eivrGK0eZjM7IfYG5DCkg5ur7vXRyJRlYIwXO-F5Wp-VKB1k1MCa0gbO6TvQytICyZS7vpuvseIyRoNJ2nSv5zS3nEbIgrqnOGnARcseS8qyUDQWCieRjeuPzVeKk5ADgyxv1B2nAqsmbHIsGtGG4jgm13AIPXaoDFt9aVm5kqX4k_wGBMGwwdWvjUzqLWy7xp4d9yuFLrbvTORg0eFVb7FrH1WpEHj77_F94Uy0iDvMSmlfoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو آدان گلر سابق استقلال: هیییچ صحبتی با باشگاه برای بازگشت به استقلال نداشته ام. باشگاه استقلال به‌من‌بی‌احترامی کرد. دوبارنوتیس فرستادم اما مدیران‌باشگاه به من‌پاسخی ندادند. بر خلاف میل باطنی‌ام مجبورم از باشگاه استقلال شکایت کنم. اگر جنگ نمیشد استقلال…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/27185" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT5VCI-SrcZGqpIy_yinBUHBztA79P0FbGuFGM2Gd1oOggfOv6tflbKaWZJZhFAxDUjlDRKIijYayYQgQw_SgfKxKRzRIqWnJzHFqE3wWRL5mmiEzHwrTSPiRee5afhgKuPQUrC_xOXpg1rbJGzi49uM79qFgPpcN_GFyNyC7cgNQwmdlejOYsbNdjUhjQTE5_C4zNWe15h31JwcUgmjcQmD99eRmAt5p6A4oYu4kId7hWfr1L9imHSZ_CRiHrMy-dwfa5q3H0ZdiMV9Gn3gT7yWKtTimE55wSQReqD7fEbo6vh9DBpmzK36XYLSbhFikzEg0s1KyiLAycvm1fdABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل لیونل مسی در اولین بازی‌ بعد از جام‌جهانی که از ابتدا در ترکیب اصلی قرار گرفته؛ همچنین لئو یه پاس گل هم از روی نقطه کرنر به ثبت رسوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27184" target="_blank">📅 09:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kN54es1U3C8dGcHeiUoxVMAa_5MhOi3mhGX9lAzX4ZVW6jgPjZhzaHk1HtuJX0JAC6tLmDymLnm3CCloe6A3aSaJpU1gKdri1YJ21Ddv2C45A53qJzZq0P63mPPr7ildObfb0Vth1gQcZb9DBBa1jywyzCkWfUt89FLUVQ1_PYt48hg9AGSweO4oh3qdQ9LJX6bsSWMrrgv8IoI0zgCx7ceMaEPw5cc3cNYrAj1On8yI8LQXlcO-v8DxJDuatDA9LakyCnfXrc7CWPEisD-IQY9OrQtlPP3q9MfC96RdurMi7D8cne5CRaO704dR5uWAUM64smD7YBlB-y90F6BZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آفر مالی رئال‌مادرید پایین‌تر از ارسنال بود اما وینیسیوس بعد از مشورت با نزدیکان خود از جمله نیمار تصمیم به موندن در رئال مادرید گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27183" target="_blank">📅 09:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27181">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBzcqlvXJuNnhvFb3QNAyTAnuXZ9uUqWFZEJLLiJi8Ei4TAaC1Y87XKyCRDSDCaxZhm0U7mzuSba_mFPHxUBQqz3MhUxCei7QnHIyOat-oToHqPYBu9erL7OWygrzgaXKLtOM0UrugaG0PnC_s976Wej0Zt2rdyoLhwXN_2ehoWyhEgUH8p0eRdEDVJfYvH3BpCzLqtN-VrJV7vvYSofA6AocpuDRf0JGVXmfyohysWvAQU_yRRf0l9iaJz8OiqSKsvHlzfnI9LK9JbCM94b43Z4ulCnVxTtYaB1LjkvWWpGpBLayn7vzoQwzv0gJFgI7b4pv5-eeK71pCkJAJMYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27181" target="_blank">📅 02:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27179">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhEheoWubFcQAnkzUCH0O6iKO-dwRBi1UUZFJtK0BTK-5ZM2eOd6E_Y1wonQdCvMPgBkqvxTEpgDllq0yZtsRuFATEh47A8KgRhTSYhMzTwFmfHXAIuYq-JxBkicznn_4YAMO4eAu81nL15PWGyXVoLgu5EpFT36sgVHiU3R0c88GeNzvA6iqiY7PLFZRbANr7RuPPxQxPkZDnovsaFv-ESvqvQPza3d3fjBziVMEQw-KKZvHC_rTSxh47d4EAA-XKIsAhMbolSofFFdf-vX_V0Kdq5wTWd1QMx_NeHNe0SVSoRcgbGMdVOPWbzHnrEL-cUeJR09poCLVuY1GGUSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/27179" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27178">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از گل‌ های دیدنی در مستطیل سبز روی شوت‌های فوق‌سنگین‌بازیکنان؛ عالی‌بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27178" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=s1WuGs4KSjM71S89nKYycsycmEn3LV20oVcx_PX2IJqb5NGrEbYxa5UleWacF6ifiX5MhrXrf5N8bkJ4tIj30KpqhTEd23mnpDz_MayLvjmuDwqgMwqIUb3GzclnaAq-ap9R5XbAsH0GZcqGZDvr1tGmwxtNbkMV35qXROLMsOU7JP0Tkwr36f7lUQ2Pm9vz7ef6NdfC4rw-FZ-RldybFbS91v6GpDEsczI1-K6qWRsMKPLAkX9dHQn6Y5sRxta-GMS60Gm0QSzRk4qGkJ0bUm8vMP6N1yrwdOwig7rZ_kdOHMEk7DebCD2gPOIrh3MmmCH3B4wFauQxzlPIJF9AoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=s1WuGs4KSjM71S89nKYycsycmEn3LV20oVcx_PX2IJqb5NGrEbYxa5UleWacF6ifiX5MhrXrf5N8bkJ4tIj30KpqhTEd23mnpDz_MayLvjmuDwqgMwqIUb3GzclnaAq-ap9R5XbAsH0GZcqGZDvr1tGmwxtNbkMV35qXROLMsOU7JP0Tkwr36f7lUQ2Pm9vz7ef6NdfC4rw-FZ-RldybFbS91v6GpDEsczI1-K6qWRsMKPLAkX9dHQn6Y5sRxta-GMS60Gm0QSzRk4qGkJ0bUm8vMP6N1yrwdOwig7rZ_kdOHMEk7DebCD2gPOIrh3MmmCH3B4wFauQxzlPIJF9AoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27176" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mkK8TGGTTgMDa2ngVskWUmw2ND8k9j28PI-pkiomUpV2BzgYFw0-kJ4OopuNvCzIL5wWF63bslLufhV2MnYmTf43Scm3i6qHSJvePOZXVV-KLKkV5BzxYyVoehrzgaHX0-a301wzxZGAAa0xlCYIGLPCUWqZwCyQaQAXEu6dThdsdEM48AR10L3QML-m9F-QBfHtkZfllsfEA3tL-G2n-YdoDbjlqxTSWRXieav9ATf_OkFinzVyOq3-rUDt2g8Jd2pxXsXGhmpen1jv2cbGOFTFtxxnIzvZfJWWkuL97r5JU0jbom6oetAv4FL0SkPqbn4TEKyZCoBCUB3y0bow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌‌دیدار ها‌ی ‌‌‌امروز؛
بازی یاران اللهیار صیاد منش در دور سوم پلی‌اف فصل آینده لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27175" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27174">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp44nDugGDQN7WGqw1eCesFdZwcPf26-d5ZOoofuF7CUyNLmSZ4Qdb5ue_4_RYTd7t7Od9IPugKxJWTZslrXZeN8fMNNlb9rnpjtfEKBUmqNv_xsTq9tV4FcPLq-QV3_LsFGtrtK6ty-2nFMkMGTqJri9SXf9mzeTRNqQA3ukXfMbyMBPABHoZUYA__cn99_LyS8OoMTbhhP_VnhnNdV4wcquKGA_VmcK91tUDXoSw_UrOXf1sJbYxGZ1hZPMrlOZR50ZM-I908dqh2JwBnPFNfIzRT1xP4AlTATwGH9EWf3Sjmw91rXzYkqOPT54uHPCmP1CR2VBHTsBrlGWz7S9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
تساوی در دربی میلان و برتری شاگردان اسپالتی در جدال دوستانه با چلسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27174" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27173">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd26SkgujW-vnz6cab2PZGloAXjQC-87oozRL31oJwQ9LLOPn8Q7y2N6nG-Eo0QwYpa4f_sAdFianBeV2tSGpLxX4jAmOoxxUFEKgsgWV7P1-82ZHnG_PTlJ9wU5Q5H0NFyg2IBy8-4KNDcleRcHrG-4xpatlPEn-SPcFVOHTgoTQ6nXGlyp77ewVyt_NCdisP22yMyIDpXq3LaF1kQa4ufGtSp_te4uHpWw42QoJBBzbvPxhPpO5fDj7RTa0NdtED5nzh2-bsHW_qyMXB_Vd825x7N9mB57WA-9wJewOhCNSp15kQkSJDOBJdn9x_KhunHV9E-uTrQriE3RORC0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛بیانیه‌جدید باشگاه استقلال: تموم کارهای‌اداری‌مربوط‌به‌بازگشت داکنز نازون انجام داده ایم و منتظر بازگشت این بازیکن به ایران هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/27173" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27172">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeJHsvkdfHZtnWZ5F4eBzLxtk8DdKa4eG5a-yhB26NW1jr8ltRkkPPOJzoHban9zFc8WV81FdNE6fzoK2fngSqyFE9T2LVsKS4jqO9QGAOtHpa5JleSATLMdnonM8wSIK5NWe9phxHvSu_ijiXTVOoAIg7ZfcLdE_Uwa4rllC37RamHlDlgL6QQc2cRMKJ_keeurUoELNDb5QRPKvIlKwM3Kgjz-lz2_vBuLQjera9HJX6FYmpT4T8A8YjR4todUqltBucl0rlqNkij3WIgCtE_xs-c2XtVoYjI5sRTkdFzJqRzrUwNt6t2fn9CWnmLFbPKL5KanV20SWnQmz7rRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/persiana_Soccer/27172" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4oXaCtkdQ9_f6towDPJTJBiopjDybnplYAd1tmKTTOkuM9ZGo8EdoG0kUNnnKCBGM5Lao40RVe1-U9qaaqely8UjQ0cy0G3DVwPfNwouhMnlK4y-nuDRBnYgRhDLtS46Tjk8_H0Q-SrgrbySeDG3yWQNwr563OApB_GkYQcZVRJit1khbEKF0UDb559u1ESoFJ82pQcWW2H4ywbhs8G-A7AHZ3E_8mp4qXzMriwrBoP3FZf1TgLAVNmYgueMDhxORSshEV5eP19MBfpo1y_syJ3g6f2tg--qB6EiXH9R8a-rhADKTLS6T3w-LCKGk4_b4maVHduJDYXxsgKVeSBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرو خبرچند روزپیشی‌که دادیم؛ باشگاه نساجی به احتمال زیاد به‌وعده‌اش عمل خواهد کرد و دانیال ایری رو پیش از شروع فصل خواهد فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/persiana_Soccer/27171" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPJEHP84WYf4xSs3RKYyI6DZ-mNkq6k_71yiOnM05yFpEdtBLsG81NxkrdkNCjf-GhCqfXD7MkPHBMIsfOuWvwKTeY5pwMiOsmyp--dIKzthSpk6FVYA6e77_BvW4w6zxD78x3LBN_3OfHP3ofOqBUjPHYmfTiC8VzDbEIx4T_At8gqUIVMPk5J5P781bwWNx1IUQihDJGZHkVTQuL3Ddzkl1Bvv7B6yqKwc3IM9w6h6bZonAqVIpvpEG8A2DpDsEd-CEH5X4yjUltKa7IHgOanqatepludIj3hVF881wiTPffQCYcHUH5vrEqPIKpFnDiatuZ67D1WSr8haF5ynNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/persiana_Soccer/27170" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2pO6GPux1Hf9Wc9nIgR6LItBJrQ166HxsmPb7e9g91hx5sMH4xFLc_DX-eXeLah5EqVHjqIgRZqrUD9_H8LuO17r_LvDKgg1LykDt3W_ePpNslJK50XcdNlZw3Lg9eM5n5TMHRvjn1SEJkzwAGZ8zLxt5FbVRvIttANGesaQaOvkDfJmL5adCYriVmV5hKoFYgZoo9vNOisyr7UWX10AzeWx3QyrasocYRg0iGE6ph3OBVoI2Bt1QgJVLzKzorkX9ZI4Fkyn9VzOytPogcwIZXwlirymOzkPDZhXoMrRepRoGteNtwUhdhVmnfoc8sqBW1fIlB37ZdFCbhiZq7FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
توییت‌جدید علی تاجرنیا رئیس هیات مدیره استقلال که غیرمستقیم‌اعلام‌کرد که رای دادگاه عالی ورزش اعلام شد و پنجره تا نیم فصل باز نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/27169" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqaqFZb5FULcpD_WcQkzkAQaksXERYmh7tzVNuBVPfIdMr3kJ3KzWyvvNl6AfLjzS7hFWMMYKWHKpG_emVE3sZTvVdwzZOSaynf7mW52tbUibnzSRV3HDQIOs6xSg6ei83nkigUEVxdPTTukI2p_Q-R7v_ofF7UzFN-wK66Nk8LbyIEhXL-vRICqetNQYUYROhfg47kdUlh3iRvgGlpaH76g4l5xVBRMGFc09QDBpxqkOtDnQ317deFyH30D0MBm_19PX3JUMnHg9yksx-6EhW16EhZHXAh0RtvUoxP6QAfWGW2Hfbqny94e57NkwxdBMSGHAbZBImv3sy71Pe3sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=E4BLUzDAAhmbCeLdDDXScEnGqtfEem6mjOtuZMyTvMfrV_fFXKnFY8m-wiD4zdqv2TBFTlqdUcm6gTFPoAceO5ItQzyoG9UPxOolbc08az9O3IalITddv9j_Lu-oO8QD_hgicqpXREwVbZvwGD1erEBTS29kHAlUKlW0kc5flh9e3sJvlczLmQri36Hx85VwwrSGHLTSN9JAwxoj3bSOVE7m6eldjxamVpJ67BfzXt8lEyj_PIWlMJ0O7Z8jwLp58xfGjSbWU_2ZhA1hhxtqqfwGPPDrC6VaDIDrAyS48RUWrnGxBrOHn4ZMowbRP7a8AWUxv_Vk3C6qt3Rm0rxb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=E4BLUzDAAhmbCeLdDDXScEnGqtfEem6mjOtuZMyTvMfrV_fFXKnFY8m-wiD4zdqv2TBFTlqdUcm6gTFPoAceO5ItQzyoG9UPxOolbc08az9O3IalITddv9j_Lu-oO8QD_hgicqpXREwVbZvwGD1erEBTS29kHAlUKlW0kc5flh9e3sJvlczLmQri36Hx85VwwrSGHLTSN9JAwxoj3bSOVE7m6eldjxamVpJ67BfzXt8lEyj_PIWlMJ0O7Z8jwLp58xfGjSbWU_2ZhA1hhxtqqfwGPPDrC6VaDIDrAyS48RUWrnGxBrOHn4ZMowbRP7a8AWUxv_Vk3C6qt3Rm0rxb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAAK_qC1tKOj0092CNCwlbkhnMKNtmeWDubr-n_Z90gQn-WwsNwkDFEqauEuFRRTXV5gnhqn5KLTtD-eyx8vGWqqJu59i-N8Yg1J4sh2-s_RD1Y9znV_G8OgdWBf15p5bFxqG2-UqHZTm4wBvSrjyWF10bBMYYirRDXOxVRLdGkQ3A2QD9nEmegIzkgT5VRsK_zRMgCILBDsWlVNNSrZLGzqIv8w776fwS78PPGmus4vdPNVlT21gZDvoy1hWSiHlLUFTk3TkXWnEwdAX2J02D0LKW6hz7Ladk8_fYbrgGhy6qMYqhfGIlVnlhK0D3ycmFTocw4kj8Mc-kf5d3n_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neDrS1C3c18Kjly-0oRjQ29fP16IvJSSgxq3HSfY3BcCPtWPv79qCcsyicB8KFVQ_jiJvljW6n0dgbjhKItaTflWvwqJKePqlD7sMyHkpRFK1537IZU91wlQjhsVL6RkDUGv8IE2wo0-CoWrKISZU9JfgmjrT1zdftOAC8vSDGVEM2j8OFEXqPNUGi_BwQEqo1M4yQ7t83rVGHCtvJPNXi27ZqSWFSRi9fesoJf_-1Kw2Pdv1mvgcWI2ubySCOmynRFMVhgn9OhJh_V4BM-ihhf5w3Jt1DhJXvx3132RE7GLxTehg4PHj7J2amUpDK_jnsOViusZ6m7XrsB7y9uAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR8SaDeMmnWeGgR9o41eqZ1DorBPgo07-YhSs8nYgScDH-CAMkd-5g_DucUGVbsMnW_jXV410vKG5-DzO5shgAODX3xfK4qp5eqxAQbrTI-I-AIuXWaE-d0H4Udg70ZG4szWSpBuQjIM1p4RyqJmeD_l6MUaniVAxq2dxRmhpIul7e9nGdcQq5tbzgozBCkPHoDIpsoXw7nAHHiJy__XQwY1uVeJwUiho8aNWVdplU_wWCs6VMNuJPXEj3bUMSJz6sndOp1hm7TwxEJ014UfXeZ8LGL9zoC8j-3PN6u_dQJ76BfO8pQnbDPZGxlXpi0FZFaAlE3WDtktfntBO8-PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_BgRkJfEGcYG9Ax3MVXEihMWBShcZMW3mr_B0X-kdlKOxKf5KOUZ8-7jp9fF5pkgP9ScBhC2LZcv7oel9CIxGIdDYuuML11fSDKh7K4j8RWSJFObkksPngEhr0S1_5P_05NzejLK5fUg3xJz2NUoi2TczqF9sKwbprINwArcpG59swfsGObGcQJPqC6pnGqKtG3LSjpG0WBehxKyr7vuA6-sSKwkIFpFWgXM1F_OkMkAPhus2Yzle2rattXsuEZ6waJFkQMOidJQRierACEz4JaYFFxMvDtiXrNInqLPesfFEHPlEvQjHpqsYEbiJ1krqS2UuitBUDQXwjIqSr7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6oczZGMoCoJWFxDllh_OYCT2SdARov587rHs10SLSb_HbYODfUvxEC5olJcptqNz5x2PWTDeCW1WZOwlMZbkjlt61Ps9zIRs_DoIk6tGU61pQ1iLxQ7W0IoKZcTzCMn8bj37q8Wb5tEF2-Gi-FLSvQIg-la665D0KwXxlFpOV2Pf6Czg4TFmH9mM2Hw5t9oQwVbW0p7uZpdb5pWzUHt0yAIR3fmQXGBHI9eEhuR4JghkHxpsVisu7z1mqrwnYevpXlsa6EnMv08kUMowk3PvsUDLDxRrUj1SrZaJkOsPjAl9OWOFmMB9euyRiA8RcUa9Nm2eDKpWzbRy4Ha_gi2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKWWZQBx_y6BRWSPH-tErMseZvVH4UOSIGSubEjCnf-K1NB3o0T7FAXWMiQB9pwxgrU2bnGCyyYpkINvNog_Dp_pdW0_1HU1_TNHH81tLNS_-e1C8yBiiWpG9Ql5TZG6f7EwMw6qw8y-BIdhtts4iuY8r40h0HQrBJnbQ5xYL_bzwSyu66vB108CcknYrjQkF1qERF6h_eAZ0if18m-DO0QtQKgCLld7SnNzJDdfOKSvgQD1jlk7XnbsGGNXiNMJ_VYT0Qo9GJJVyejo4YkYoSwm6rWwecSNhu5y6GEcaoZZqs_MlGV0YlPxtKQAURYywDHgL24uA1SKRc5prwe89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALR-zXRd-jImnhoRyur_-cfzyl-E3E1HPSKbLsSwrIl-lZVTLucqR3lR_JcpUrKfKRnvhrDQz9LgvlPloezpL2vXG8so2eZarga8sv3rj4wr-u_cfm1JzCWrICVoR9UivHJuYZgFxX8RwDAJNQP0Z8bRiTq-NNZ2B2wSGn1tOjIJQy1SO1IZrMLERav-A3FSiuwg2CrZMrApBDSQGNgUoGtFwXYmmavBtCMB1YDNqIHy_Lcp_kOyKed9CTiEBIwZdf00WfOd-JXYEpGTQXRbLId1DNFQC65CDvCSqhIOMOIdcuD_8KzDjdCCPdKJW4V9om-ZqSpVxYBJwnfle-9hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Susa_3Nf049P2Z--1p9qrqoTRmuM9eVFEx_k3FDn9rzUSDbPguoseHVdhklI0ZJJlfoJX7xttme1Gg3TtqCrKEnh8t74coLZ5f5RxuME7IsayCeOsef4Rxaawl3BqgwAJQ8A9T7AVJCKmClZD11v_aCNxggGYDqQiKcNBc6aD14Gge9cKv2vdQXKWu-_MSiHy42tfo3I6ug1Tbto5XzpgYDIQytSKVEeYVOO1YiurDILbMGSNq7h_jRiacSbPg4jTMlJXNoLClKVqbD0ht9vT2CTyrEX6UndjTaQa5EW7ycbbmhfVYH7pHLmYtFlIGZMHoTSxSCGJP8VgUnHXoLuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXaLGJVZy5EVivF_QkkE0y6g9kDYzm2c10ubPqJVTmeb-4L9Txy2JxX1adrHwPO0IZIwrmNIwxQEK--N-4PMG6aZrdc_FfRLbGCu0o98u6oNO8H6YzEoeMczZAsKg8fMgXK5jk0tbGs1yJaZ0OTHqFJuFr3TLHdyY95twJuk9eTXHFr-_BG7qxJ4xj1MP7D5_cLXdCWWK-EDs-j5i_xR_y7YMgIQp3CahY-LPOVJk8zWVhXukYD2232ulExIUeH2NvUNEQdGk6hNjdGHlu62atb34qUpxc_FaYktAYB4cXdXxizqW6KcneeevH-NZ32FNQwpJ8OYwk1vTxt70sb0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNZrVi1myiUW54a8OuETFASXNl8qU51UaH6OxK-bIiE8CykA4HuxvN3DHv0cp_yJPrJMCwfNgsdE7qeJfnicYPg9nJ_5qL71ax-hlyhBsuD5vUhX0TUnOcQFXSOxWRHbmHP-nSGI4y33pFEl_B3Tc-4DV7iZGxp4PSEdpJPhFOeOPlWYsCS6I0teZWgHV-aqGefwuHW7Ub4N28R4e5jf7Jm3_kLioqrYuhZH2RxchDHKQ4bgNUhKu4LiD1aB_dXk2wV-CdBAm95iwWoMnqqr0Z33IhYEG2l5he1JWyvxqUkyQ1dsOh7gr7CV6P07U_qkXOSgML_3IZoqda89NBE0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO7XeY5uWlSfuih-MQ3fsSzQilo-RR4iC3H_PahSXcezeO9fujIy71H4dJ_Tz5VAp3TzZ0OJm5hnhajVDXl1QcusNtnINSu1HGrRDVCTSi9kLoTWcqXrAfxU52kJyKQxGR15zQuYgcwIkenHBGceSQKRwJwoXc6fHRnODndgn8yPg_9ErIxGPNcFnnOrt1KKE8p2CWYPrv0B6wyMd98TFXPdmo9wbz1kgrkXp5oDEQUPRNbJJbSJ82CvjkvsJyMCgWuH4sQAt3KO5nfaFivzUbHjvoyjp7ghikURoY4XI8Zzu10yRPPJcYddt8kvGYxXh2hNfV9QNcQiNVTiUHqgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTY__C7YOlAITXWdx_8XUDKa5-kbjWc3U-1KQE96tn-BpD94VEYwOx7hEQr1meldzWdV4c8K0N2LLrd_rAO64U0XE8AsrMikeBLWsdB7qpMzpFD5ZiGAEi8ONO0AG78uhT4Mdlfob4xjrup3Kb-Zd2LwP92O28Rr6eFqMliJ3XnEepVObrCLAw93YREC_VWn7FL6uUfpTF1M8qk-sFmYZeop6IMKOnvGMg9K2lwj5Ft-FT_55EDe6Z_Z3BPhxpzZmG5f3-G3HWPz6Idf3SyIDVNz4Z2KWGPPmo9fQDk69UkTrxjYC1W9mBrSm5Ky3_po4yO_Q1jcitpO9eO6ebJmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=YNpCs-ZZpYvlpUTNWu6w8-6QnsHEHFANmQUFVACbErlcBHXPgc2I5bNHCxiERRUiTIdQnpeDQau_vgrrJ4779wWzPP5o6n4Akvq7pADJ9mtdGdkeKRNJrRdlgbU-SlW4wtKW_g_yBvRzjMNV9bJhxuq5J0_HO1pMzDQH_guokk7xuMiwFgAnEEIFT81m4--yUEcDlizR1e7zjoaPfrpNThKR4OcfjkbVC7IRRqIo3un6gCu3XUJ3UyUtA-Zl6D4Lqo8GkYvM7lBoOBlFtFVAjcYJs7zcdhGg_g1b9fMsQUh8jH75nMFt-6I9Av9SRZbYGSQF0vzTCnWqL3bbOjOdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=YNpCs-ZZpYvlpUTNWu6w8-6QnsHEHFANmQUFVACbErlcBHXPgc2I5bNHCxiERRUiTIdQnpeDQau_vgrrJ4779wWzPP5o6n4Akvq7pADJ9mtdGdkeKRNJrRdlgbU-SlW4wtKW_g_yBvRzjMNV9bJhxuq5J0_HO1pMzDQH_guokk7xuMiwFgAnEEIFT81m4--yUEcDlizR1e7zjoaPfrpNThKR4OcfjkbVC7IRRqIo3un6gCu3XUJ3UyUtA-Zl6D4Lqo8GkYvM7lBoOBlFtFVAjcYJs7zcdhGg_g1b9fMsQUh8jH75nMFt-6I9Av9SRZbYGSQF0vzTCnWqL3bbOjOdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHZI6axGQGC-E_x3AbbDeocsowNEL5bTngxdiXiT52eUtH6bg-dOmcaOEwzRnOUVXdfsRjRSzv9FyPIa2UB9f8vqIVd4bGZwgZQDLNnWzFj_5cQtsq7-zBHzYnd2HzksOjupvvDgtMVOGzYtNXKVMO6qtEnB8hSkFzycKzvreiSE0Rjv_p0B35wKux5f4yRQ3SxNL-SdXSsvBQONNxB8ipekbnXu-UxoAb8w94elgUm76iZjPGDlEcXImMWqwfq7WbWVFrEAKD1259RB0yua_1bd69sGD2wIC1o_do2GanywtaF4TEBuGxfa6JF7ac0XtdrNi5ieq255MhsETGmkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVrYJXlyYJi9SyQqaExfFu7BUPu_3ojR9Cuuw4MQr2apHTtiuy6vm5SghHg0OlOeFt7rZzff0g26POlzVpe_3SLf49oKuRrroElH2yWYZwTJDjzFon7xxvrWAY27Xx4KqQfErA4cCgTJ_y0THeXf9BsJ7EPO6rQ09QH8V0Deol5KrwYZCqN-ly5Eu7k3JLG0l0hjkdoCK142nNWm-A4jSXyAH2f00IHUMGCpfFz76N_-j2iHcebTtxlDAmRWgpVHCu9PlljJKJ4rkEsQqG2aIeji3HiHbBnLpEe5WRz0JkCOOE4qRCBsKjJVqmBvakqvfTfO9X2nNDWD2Kqz0EkK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=hWRi8dMPT_3_4le7lZdN5D8KH_46eq5dO5qtPQapoDj3xYzkOM2cE7qkgb9vyn0ycqDSvGAdH1QLB-Qt1oZ_QKVZsDqTmnVkmAKxi-PAPsl6oAA1ISGTJ9Zx3HQG6sqB94SsNRo2GzRVL13DSQoPxOiSIJiqMyZOFcJbqkK_VpaRV6M7ajC9RvNsQ5wxfO87FocX2pUZKJYMKmt98TCEubiwgPaEyITkbbJWIV3z1JCnJpH1qwfGbj4hNujjlfqE0rpoaiP6M_SHnMuqa5J4lQxOAbG4Orkqy-1LPfXg71pzwkXF1tjHNzjmOaThdCYDowMHqRp4-rudPQM0P28Y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=hWRi8dMPT_3_4le7lZdN5D8KH_46eq5dO5qtPQapoDj3xYzkOM2cE7qkgb9vyn0ycqDSvGAdH1QLB-Qt1oZ_QKVZsDqTmnVkmAKxi-PAPsl6oAA1ISGTJ9Zx3HQG6sqB94SsNRo2GzRVL13DSQoPxOiSIJiqMyZOFcJbqkK_VpaRV6M7ajC9RvNsQ5wxfO87FocX2pUZKJYMKmt98TCEubiwgPaEyITkbbJWIV3z1JCnJpH1qwfGbj4hNujjlfqE0rpoaiP6M_SHnMuqa5J4lQxOAbG4Orkqy-1LPfXg71pzwkXF1tjHNzjmOaThdCYDowMHqRp4-rudPQM0P28Y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHVvw0Q9NN-n10VYfCgBUh8RhLtLOVSvFuI1llEPESTu9bRWrw3XWUqaJk_dbdLW0i3xj-h8ucOfPsGLd90F1uYS7x4N3YOl__GbLcqpZMM_wvtPM2eCr_tUwpfAtxJ1khGXhpol_jr4Xxl3_BvKDvuumYy5ikKBcVUPlM30c10js4o1I2hEPuTjyScoNmM4TLwBuu0VpGtcLMn8NVSfWc1XODag7LKrCGC_GEkfOpc0-SLikruc7TCPS6y-iGBWH-Ej0Sy-VRQrt5iT95IwSyGNXrQ7wKtXMJTdUu1UBT8VhhZcTElBnc7exKjW1L-kNM-cxISVaEdsM3kONE8dQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=ALhOk8xOp11M90orz8ggTMkgQijlsS683g3Lntu5cNSuiNxI4f6P4lVRuGtrO9itd4PklFlfhP4Ro2XlBpBiQ6Ci1l0uYHyEVI18HtoCGOQi09tR1KZjocXVJbYYcEgHbnJxeLPXQM6dUjR71RKKUFK7VXTjRCjhQ0T4mzh3RbLekYF3pajiFFJx0J6HW-wQPEKrRhHcuBPs5SPNlAVAzOlJZmyQmkQhCkHI2iS7jsGWP7fVoopS1F95pWxoCD_fsVy1VPGYnMzZXnMv--D7tghDujfs3ZitInab-ALqc3bDqbzGbdztYUKo062iqnIAzmUlggjyG4KUebO4QusclA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=ALhOk8xOp11M90orz8ggTMkgQijlsS683g3Lntu5cNSuiNxI4f6P4lVRuGtrO9itd4PklFlfhP4Ro2XlBpBiQ6Ci1l0uYHyEVI18HtoCGOQi09tR1KZjocXVJbYYcEgHbnJxeLPXQM6dUjR71RKKUFK7VXTjRCjhQ0T4mzh3RbLekYF3pajiFFJx0J6HW-wQPEKrRhHcuBPs5SPNlAVAzOlJZmyQmkQhCkHI2iS7jsGWP7fVoopS1F95pWxoCD_fsVy1VPGYnMzZXnMv--D7tghDujfs3ZitInab-ALqc3bDqbzGbdztYUKo062iqnIAzmUlggjyG4KUebO4QusclA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=cALNREfXdDL0qzS5Z2mRcGyap768z-jlM9IOWnuzqQF8ghSl9ZDm6p7CeyINgNoWk21tap7kj4d8_k8cgnzr15oHXBIKPDb-5NjxS5MQcL3pky1tLbnIlebQk9slmURbs-UM-AJDz-wdpWxVIABjGMUwqDqOxKKTjdlmBZBJUnKXAUzJrcsx90m9rh3fDI931SKO8sbxLmWCUpltiDgEbl44VYaLwRmPWnjOnOrLFQNviKJJEG-5yFnj6jnZ4ryVIuabhJeGhgWcbKr3fZkYFo6Q3zXAQmjJVeBDn1L3k0mhxsqiYlFw4ug6HMHkflYzIxilwqljar7DYy9VZ0TfNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=cALNREfXdDL0qzS5Z2mRcGyap768z-jlM9IOWnuzqQF8ghSl9ZDm6p7CeyINgNoWk21tap7kj4d8_k8cgnzr15oHXBIKPDb-5NjxS5MQcL3pky1tLbnIlebQk9slmURbs-UM-AJDz-wdpWxVIABjGMUwqDqOxKKTjdlmBZBJUnKXAUzJrcsx90m9rh3fDI931SKO8sbxLmWCUpltiDgEbl44VYaLwRmPWnjOnOrLFQNviKJJEG-5yFnj6jnZ4ryVIuabhJeGhgWcbKr3fZkYFo6Q3zXAQmjJVeBDn1L3k0mhxsqiYlFw4ug6HMHkflYzIxilwqljar7DYy9VZ0TfNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6fDdzP56pH8yGmR_Z72MbDoamPvup0GGjrAuPMz6fC6dvIaynj_nNaOfa_a9FKjCI381mS9pn_ky9VrRfKYb_ovkTtkyF5NEYTXwcU1ScewnbSUd14MtkaIIuER8zQz2izV3M1A8dX6Hwbnfdo0yFQh0qgWnkWwVYzbEbJlY8VcInhVjY_cX_Tvr0FyDnQtsJpb2ro-eGUIrfOyNF6DahU8dBkmR8JjDffFHVxrJ12gcU0q-14h00TOlAsiJ9kyIaqCMYayvD2xYlWAsytJ2jOYUx8LBisWGFr8kw2FuiXedTmc2CyICqblYjTf-taUMB22t3XM7bp7KiTdidHomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neC9fDdseCD80Kucw40B4p8thUNDWNGoWYwwvhY5-mXs9wQTG6KzS2jBsZM-FC9cs4QNpGIc6-zq_0662H97-qRJbHXy6RIygFPemnml5Q-OaK7PO94oqpGIAiHq0U2hzrkPX6f4U6V9FKjtts2Q7liIC8vqrM82sFZLX97afS8AQVKL8u00qziMIqGYS6_V0ewFgR369Z9mXMw2j3IHmiULSO4Z3h4mM0_O7EFSkb4Ez8CTP8Ve8awznTvQPY6twf4xJcx1TzWYuwRm5CTcBIfr5YbMEUYnWNO9Xt60jYL-1l3KNL-xu3poaDgWzJY6Mk7K64kHsd8n_ZZgEAfw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=Snsr9w9hMdlMEsjBH-WvjMUm6FsJMHQfI7LtCRTtFMc829DZtx7AiYK_ygqJfJR-yErJRALRoED8yRe4Gk-vL6H9wWMls4xwV12JKTeemW5OpEIrzCNwv33Dp_Es6Jwoh4IsFu69iQ3ByJ1yydXCOwawfqIzfvJf2fffa4HTZx9-IsblqDDIQQi1wE-lWhwGWXFLW3Rn-QJanbrrmLxpxUX2AkC4Ss0zn0qGPOU8VgcdfFaE1z5JOOwURKUhgpcZOnFbl0hZBlHoyHwhVz5PxRPq8YyDsN1Mhqwbe-b8R3I5FycVzNw0rr_6W4cEx4EXERIz3cez9q6pqBKOTxBBOhDY7Y2Lmarhx1ZhK_s1kNdchl0CJKLY3VXlUP8vGZB0qJRALT1r1jZ499Hhhbtg5y-B_pPjAAkuSTCFdvoceP9OAdn_y4q_3Marg3udh8pGoX3rs7ScGyXqmMtfwzBXhyktoxUMG7yMlFdBDSAJIrHE98eFM6Rc9UAtJ0zIb2KyfK00oJStYWd_ABlTMS7slZUr9ClE1mbMjIlWz1dpd7ZfipmDaJNg4cKldXbI3KvjGtqArNsBQF6AVI-M8Qo-wSCOj_8jeXnUMuv2D63BTa1_2g6ARflVSIq0DHKBbdufkL9PjZ3C91yJzaA2833jAH7Ah6FeGWFjdN5HuIXVYbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=Snsr9w9hMdlMEsjBH-WvjMUm6FsJMHQfI7LtCRTtFMc829DZtx7AiYK_ygqJfJR-yErJRALRoED8yRe4Gk-vL6H9wWMls4xwV12JKTeemW5OpEIrzCNwv33Dp_Es6Jwoh4IsFu69iQ3ByJ1yydXCOwawfqIzfvJf2fffa4HTZx9-IsblqDDIQQi1wE-lWhwGWXFLW3Rn-QJanbrrmLxpxUX2AkC4Ss0zn0qGPOU8VgcdfFaE1z5JOOwURKUhgpcZOnFbl0hZBlHoyHwhVz5PxRPq8YyDsN1Mhqwbe-b8R3I5FycVzNw0rr_6W4cEx4EXERIz3cez9q6pqBKOTxBBOhDY7Y2Lmarhx1ZhK_s1kNdchl0CJKLY3VXlUP8vGZB0qJRALT1r1jZ499Hhhbtg5y-B_pPjAAkuSTCFdvoceP9OAdn_y4q_3Marg3udh8pGoX3rs7ScGyXqmMtfwzBXhyktoxUMG7yMlFdBDSAJIrHE98eFM6Rc9UAtJ0zIb2KyfK00oJStYWd_ABlTMS7slZUr9ClE1mbMjIlWz1dpd7ZfipmDaJNg4cKldXbI3KvjGtqArNsBQF6AVI-M8Qo-wSCOj_8jeXnUMuv2D63BTa1_2g6ARflVSIq0DHKBbdufkL9PjZ3C91yJzaA2833jAH7Ah6FeGWFjdN5HuIXVYbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fww8xK1XPK2i35JBJmos48lA8BpCbP9BrJQqoZfpfQk6ZNh3iVprrKII_q3jjM5HlHmFW_3eS821Gep0iBnlG_AP0r3na_zQvSy6NxIHoaE-oaWt3HJF20a0SqbCTGLJ-pYrSjbvUfhJB23SDWktdheRjtSBqCCOZJaDlOSp9sJ_fIdihT0audBuM_7d2xo7lLKpLdgDSik7_H-rR_hDB4K7_Q9zIYZsiQ8iYsGO9PGHOnq0ojshuvbjAi4obb3d19C87P1k4NkEPd7n-JFkANa5USt0Hg7y1t9wZD98pCy7lSXJ8F68J1k470Bva_C4yMXULkqQXYj9Ts3IvsHA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=ioKpq1sHhZeUIKWa-kMJ1wclOfmLUXxNEp5Zs7oL-0wKkSyNHu1rv65Cx2Mn-StINkzj3sbiudYpb-_H-sBlh1X3HWZkARTfFrH3J0T025LVxYSu5_EW5VSSodVGmheuuNnIX9SXErWgofpHR_HQp3q_JVLmcJ52K2Ld1Eh9YOJPvC_pA0d8dnPkAq-PAs7I82a9YmoDcrMgLeITLJb0t3EUCLVrQFK0zB4bCwH-GcUuIRQsH_NSDVYtTkkfux8diUMOoR_zyx2rVnvDO5E6Ld4tnygp-QCp2T0z8oedMlRUUPRI2df4w2iUx7U3Jm17IGRvtY2qDMDFSjgx0Mb_zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=ioKpq1sHhZeUIKWa-kMJ1wclOfmLUXxNEp5Zs7oL-0wKkSyNHu1rv65Cx2Mn-StINkzj3sbiudYpb-_H-sBlh1X3HWZkARTfFrH3J0T025LVxYSu5_EW5VSSodVGmheuuNnIX9SXErWgofpHR_HQp3q_JVLmcJ52K2Ld1Eh9YOJPvC_pA0d8dnPkAq-PAs7I82a9YmoDcrMgLeITLJb0t3EUCLVrQFK0zB4bCwH-GcUuIRQsH_NSDVYtTkkfux8diUMOoR_zyx2rVnvDO5E6Ld4tnygp-QCp2T0z8oedMlRUUPRI2df4w2iUx7U3Jm17IGRvtY2qDMDFSjgx0Mb_zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSInmR4lyfcEYX7XuXDEwk8t00wY_gMk_E4MGCNAi1jCGYsbLdqoMS_C0Fa2ILwg0DjVquXEs_Lh8_A7WU25JfPG7sZ_yH7OJWDAr0jJJiO1MTNI6ISrNcBfJKBFBT20E7TloWM46KxV4zcxw5wsMPxq_r-oS06Jz9k5KVceLimuL2EyOWVKrxocS_06n_aLtcEqfGwYrXj_7ps-RWM5UElEdc4QSY9ZyHZKYCYknqZHNACVWPdzXmCRDXqA04SQOFObTy1Mk4fSOK1RbkLJzwpq-OxgusYF2IrkIkS2Fo2ur0Hfl_e5QF6-zkb2a-RKCPdxkrhSoo2FazWpUXXYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5W-s0Zn0pJ8m6yJ02wKLroPBFSxZlWMk5apBb9goGiVFQcZSOWj6PSQqCiwCxicQaWpo_iwmVg_3e8DlRK6JRgdLTj3QmURHFMpA3VySFWe2yOc1XsSIM1ASMYnBf9E2qX7jaC_DlhC2Ot4Q51_vQs9EP5UPogdyzaceTDpj4E1mC3vlBJpHe7r0KqsQ11h5gyyPiFALifNDIhM9KDMwcLc6N3kWNZnfQMHp8Bk6jbTvC5uzaQ09_1LqPkrI4o-C58UtEvAx13HdE1daSHHmdKqX1e0DMm6mSs4iOVCfhehy6za3AYoZG4P0lecNQkqdovN54_uA1OPXp0HcZlrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La1atJcMyuuCozYCnEOyvE7OuC461xP342L9Ks-kn0S8LSTHPL6Jl1Nj6q08LAddiNZ6Mjrg29aMd41OzjsDGbQlQM54qMyn0IN7AZ4Vty5hLWoS-gzPvIHhUgpQltHdRO512SNbwNw2e29fwf4cYICUMeqnGcnyWb3FeW6NSRCDr7ESHPkVVdkp3SDfYLPuTrdF5Vte5ulY1i598hGj6c1cJm9ueGVmARXNuo-qQjaNJDi9zy6Kygn-XhgYGPiz9FPrTfeZKa9gvypJ8cZ3ChOTy4ywcpxYO5iWO_Fb_SgoFTN0EwtueP_Hvul_XqN1A9zq9UJNo8EO9Mz4PMDX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xi5G17W-ljVN9zFBSW6i4SlBkwiTIBlTXQwM56T3qqFL-ZL_VX5keyKAbiF5mrwtU3wyC0YSYV-nIoKUV56Aun_im8hfBwUBqZ9S2g7do6EP-mVQzrpaz0Qo_d_zKEnU5X7U0LoRzEfp8L0JpOFpbNk2zL_3J3xO4fR48Yn848vgWYd1MdjI0thhF_oxkjx9uLaj18_eGj1iBRQK56vH4_Pmi9sO0Ksk5BsCMbaXzYkc25K55yjbZl3ByQ2BMn3EFiIgnZirdIGc4cV2ibjiolJ1_Uurm5b_Q2GAoMAwsDrOXG-DLb0ylSupl6UkzwyWFXraPHjbbqKWepU-ky1CLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xi5G17W-ljVN9zFBSW6i4SlBkwiTIBlTXQwM56T3qqFL-ZL_VX5keyKAbiF5mrwtU3wyC0YSYV-nIoKUV56Aun_im8hfBwUBqZ9S2g7do6EP-mVQzrpaz0Qo_d_zKEnU5X7U0LoRzEfp8L0JpOFpbNk2zL_3J3xO4fR48Yn848vgWYd1MdjI0thhF_oxkjx9uLaj18_eGj1iBRQK56vH4_Pmi9sO0Ksk5BsCMbaXzYkc25K55yjbZl3ByQ2BMn3EFiIgnZirdIGc4cV2ibjiolJ1_Uurm5b_Q2GAoMAwsDrOXG-DLb0ylSupl6UkzwyWFXraPHjbbqKWepU-ky1CLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=kWJyblXQ8vy2FzbQJsh9hqVb--TGZfflTN7ONa2MT7oHPX64EbpQjJnsQZZjYkO8yJsb0eVe9m6nY-wJ-gvBgQa13Rlp0iTamqp5QA3O72xSxORBc6LYzdrIg6xXUDLM1ZXzbjgQ7-quBIcMae1QIXOZJu_zQ0H88eL2oKWKEv4Wsa-9ClnHOn6EjldXK_gxE-wsjeOByZB5WXxZT0tXGpX_sAGYogwyWe9BVGDEjFByle9eaBg-aHywN0IbfXEA5yo-rO8szfG80YL4xgeMmtJ9P3rWNThbo3Trm3VB-LZ_TxhZu7-sMKMVVrhq7Na543zDS7j8jB5cesMr8NzQ9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=kWJyblXQ8vy2FzbQJsh9hqVb--TGZfflTN7ONa2MT7oHPX64EbpQjJnsQZZjYkO8yJsb0eVe9m6nY-wJ-gvBgQa13Rlp0iTamqp5QA3O72xSxORBc6LYzdrIg6xXUDLM1ZXzbjgQ7-quBIcMae1QIXOZJu_zQ0H88eL2oKWKEv4Wsa-9ClnHOn6EjldXK_gxE-wsjeOByZB5WXxZT0tXGpX_sAGYogwyWe9BVGDEjFByle9eaBg-aHywN0IbfXEA5yo-rO8szfG80YL4xgeMmtJ9P3rWNThbo3Trm3VB-LZ_TxhZu7-sMKMVVrhq7Na543zDS7j8jB5cesMr8NzQ9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHlRmljTGBg0mmaOb6l7o7-u_QXspzfI7eGBlZ4M-dxS6INYQ_alTUJs4eWt_gz3BlwI4QtPu78s0ouqUpPMCG9IcaG5-Dd752GDM2sv9nMq_oK61fg2a7qS_bmcvbQSky8Q2cIvWf7H9Sx8vrCuTlF0ShU3GqYXHCyrf3tYXKaprROf25h45DXd-ix5NxYxBIcUdn_jzZijidPRoKhfTpL2J4-7TYKrWcS9IIk6-EyxJIqi6-JY0KcwMXXBzA-DMzP9t9MQYYRxf6fYvqjRqcatnp2l6yIrCfetmOfl8I_KLq4TYw7VLdHOcBLfcHX3g8U_ZrCEpOgnCr-nF6_ynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=BTljpWVBVd48CizmrRrWtpB-4SERYrg7kVHRxOio0N1KQggtJwhVglP-zWhV1baCe8rB7xkkbNGF0lXQ5b0RCXPWizXzkqFkiDiZxgjAmbbj188pynj4NeSe5dv2TGt7m3pLvpwS84ro8C-bjdzIL9R-uZiZoVswmKCyVuIE3j-NSwkWJuQnMJ4kE66WXAcieeLHcdtwNbzcHrhIINTqKCfDSFUkCPtEa6PLUoMexKDCJyCuZLN41R5yC1mMkZ3Nxj9ptzYrgehDitgX2ibbbZv_KPGBuewR7JCWQJw73Iuzlb7obpPEF6WTxkxF7I8UZcleE3bnwd-b10Bsrv758A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=BTljpWVBVd48CizmrRrWtpB-4SERYrg7kVHRxOio0N1KQggtJwhVglP-zWhV1baCe8rB7xkkbNGF0lXQ5b0RCXPWizXzkqFkiDiZxgjAmbbj188pynj4NeSe5dv2TGt7m3pLvpwS84ro8C-bjdzIL9R-uZiZoVswmKCyVuIE3j-NSwkWJuQnMJ4kE66WXAcieeLHcdtwNbzcHrhIINTqKCfDSFUkCPtEa6PLUoMexKDCJyCuZLN41R5yC1mMkZ3Nxj9ptzYrgehDitgX2ibbbZv_KPGBuewR7JCWQJw73Iuzlb7obpPEF6WTxkxF7I8UZcleE3bnwd-b10Bsrv758A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HByVXQdXFkDsyMKrjXj_1QHV1x0ChnMWXncyn_NEbRi_3qFIM7WbXnXMxAWTwA38ZNl5iKmLn0lBGcXX8dAhD-S1PQ_pHEWyRG529-I5uqrdtsJqdc7rfC7qc6OtUB28QDv9YW_Fs3sXu1huYVpXaZ408Jlssl5VVOBL57aCLwArtn47ZgScBciHfaVIwRCmvw4aC6bSjSQHozRtMNBgATQXiTPxL06kCfUJtrtCfMSweB1mhhJyXyLnULahar9D5GCuM-PaEP090U4I5Ad19oEuaI96NrZHZFkiMQTfyBYxH8ORhW51HvtTxZkMVuH8sYkE-RGffuvBVr1CCQfVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQNx08Bq06n2ZBtDbPZMEPUszupRIQ_kLqJDGgzRyuRMR0eaNml8Txzvk5jH0D-QkPbwLnPDRFZnvC9ML7MF8gOp5HpVPjcr8dW28JIoW6B-dA0Qc0z0p552b86DT-1VKAGMIdF35ZH4iDXZlWUV7wRSZhw6eXXpfFvzJ00JI0ztgyqxpXCS8jQCmhW__4KGGM3By1C9NU2F3kSiU1GzGlKiImmpWGtCBVQk64CnJsfIvZq9FTKnYNnERUx200RbKKLR_vSXwnAgYnQWE6yxL6D1gHoIylyEdpyiquJvj17dUhncZK0sa5uKAK_25qG3KHlOm9AlQZh191y90AyRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7WsB2rAonFMJd1Ab3wtVEb5KuSLncLSRxxZ9V9qt_AsXa7dGhLjKKQxxbIboWKfQ_-s3LOqGHVCbK1eXBwdpP4CnXsRw1hmzklbdpjkTjlkOUYrfSYc5RO_xLqzq3H6FSqa6XxJnnXP7kR4dnvRxvK3rNJcnqnXSB0M8rxVAb1jncZm_lF4ir2y_7sXV085QWmSLXmkCNeBRhFmRf3CubfqVG1u5JsCG1zn5ClCMM3OJDYd_Rre8tFr9HSUFDupJTc4vJWyEZrUe00BYP2I4B1xXmGfgyNTBTkImo9AAquBrgNqbFsXdusDQyG8CM0tbPWCc7sYPw8UNda7gOinGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt3SdJcxHxsW9NDU6hbFppIDPHXncVdxVV26A-5HcRW0BdAEOJYlvPFEHLQ5kih2Xt3Nt_2oX-NQotLrxYba1y8uc3dWU_ar5Bc791mLo_nizAaEFDIz8YiUWyNIIdfV26_IaxlbH5WP19V7vGocYtv35sNEB57V3W6NTV0jjNxB5zGy_TZHNWcR81rYVCswGE3MftRO_cHVfnsGbWmaUXdryD9mbKEy6tSKv_IPTcvlaVI2oDE4eyEqvoHn6OFUqEGPLIq0-kF-u4PbEHoBUeYkNW9rAAi0WSjXw3Mh-jk1rCrIEajkKA4DkTI0tlFeS-o7j7uDoTI9xN459JlXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYTKnh7C_Fo4P4O_NJP1McysrMKYFIlODFiT4xxQL4ghkDwkEy6nNaWWr7x4CesQC2wW0D3fEhxNvfWCBVTV2NAzlAlAIvCuGuKNltGSskOAOHq-C07aI2O-czNoXewC90Lis53qodGRw_aYTTTvOyofqW2BNr5GEsEiiaxvPsblhzQ6PqWXQiM7NyYJABRwkvixDZxHz3SQ_XwN_sj1tdOa4KfowHyrBW4n1c78dOm5dIzN7Xd3DmPWMxriPwwsCnzGWcl-ZU_LdTayj8TIQ_56gF-XM9MV-t-sVu56u0ORw0rTbDua_YfwRs2dojI8cAn1cBlv6dzAL1bf194F7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpMhLF3Fisx-S1jiel5sJU74-R0F8kfpDzAlj_Y7IPFssm5o6nuKRS45VODiyekd97pRFBMMhl94Ih5k3Dear4V-4xx3qQ5zJtmBlaGDksg2-C3se-kTUh_9z2qw_TIfYjKeLQT8WcxtrjkpLT-SxOFw3WnrQmcK78JygOb-xGoWyjbR2kodpi1h10SeqZQxrUImNJyDTG7Yhgn8ZJIdHbW1jzYa3FMGQt9_h8CUwmQBJRy55MrphmK93uj98k9050uqDp6yjH1Ft_KgdvpQl7WjlzjZ7j63TV6haU9LyiIrNLauhuMs6BovodTIQNV7QzZ6oAYi9FAovfqXEQWloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZ6K4Lt40OC7oK56R7sjJdqcVXhl_Nl0Afqj05MAynb51xAe_exztWWLYWF-tBnqnLtm97V_5h-lSiRXs8hfkqwil0oieAPpm1CcBys0iVsGn7D1_1BaqoDd9lf4I_tsLaCNr16fdEx72iTuUc5jPcSurWgdi-KVbBOaUUI9v_8ZFTckGeXEPJ6qesO4auM79SQ4r5fdJonjdN4YbPS0rSgccdZKmf_gF9PgwLgMCXfnvQWiPXey01qj5ZHt6aIug6iv2nJkAPMwGn-JCggm3DsLQYcwbZ8dhud6XcQYazERz8mu_bTHRYRlbx0vcbtSeE90NBZfxMNMBkU5Q_79QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRekYflzd4k7f8ZsvxukL5_cMKB4thSFcy0Fz0GBKHh6C6lurm6nYhAEtaoajvQ8n0JHku84B9DDCjHbl33ZcJ9t7thj-Tg_QtxWsrmd5SkHivQF-4Cs5okMmVbUKR9bMP_H1jz4w_jUTHdqq7Gy3lOXVwGu6xq2MFqF35Fn6X_GoDjfz5K8LsivrNWotcI3Rwa6jJwjiAatkFsyaLjslaxTT3_D5Kzl0ARvUT4f9sdK6JDpVMQHS_B6v0U1cU5p3-Hw-5_lL9iS2AjTC3MHdokOunQttUnUA9vgb0hwPNtkjDdXhP4DSC7bY5CBjraEyKYJi0REkaaFeVdhUxnX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4JTtqlTPFEg1kWnjBdyrdPRhr1IszaHN26cMfCAYNHPmd7KLULL2oJtrZFqVcw8GKz1ZmxPT1ARolibWkWUlmIBC8yT6gZjFmJzqRFTQLcxqHAMXyuXHfx5jrNOJGPQoa_m13knEBNOuP4MSpgehmin3rqBWLGDdBkwrQFRV9rsujZkFJxbOTuWVTh58bwKlkhlbpzPc7hmFNg97hLioTfsNqOogE_EK4xmCEtTdfyLGQx36CzLRU_XEMBUhmk00wcqIB_jFnMG35YTLj2OQWt6NZqEBRlTksQY2Xy06oB_2cCoHpNd3NPXT5_5kFhv29ercg6yEYNkFgN30UVYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiIIDdSziGleeTDSvs94GAuP68CwjqlirxtSSsp68bIilnfTlcsx2IiIOIcMP0mXNJleZLfjpmdAnoLrEeBbt4c60_LDspTZJ7EHXBifGl6GHu2qBBFhbllhZ2jqcVoA9kC7k2pqrSuj35kNAZSFEC0z1IIASkrXB1XhQ1zGaFDWyOe5N7O5eJQTuERx1Gna9jjpAGuS2KJ5CvXWhSeAnXhiLsDQ-rrvyE5g-D25Ace4OOvnvubg1751AdvY8arjs40ttvGE6jVTc_JKfDzlQawXdz2pXKkdpwqJN4vTpuFCGhhzhnCcm6YAEWFjGEHIiYAV4ugtps8_8G_QEJio9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAXIzwVFF8TM0dXfQwNROxajU0f8i7Igb5qNu4ds6QIZTThiIrmrRiE9fauTUVeqskjEjHcQeCsgD6MPWzZF9XwPk8vrENDtt2aSxdegwoK88fbXfF1ymivus-10D1dkdQ84XZbzuGgC5bLGektzVdvHqxl_1XmUD9NT0YteXa090Sn28C2mEs1yowlB4zmvWrcEICrIt2IMULUeIoJ_thCe7NBErRdK4QT_FEP_vl_ULJSAXFqBRKBM4eMhncJqrzvu7QOw3fKfl_QVs2JQCnCFFrBUZ5Actg7tAhS5O4808ekNULcVNuslLu1xLP1Rewdz_YGrIU_p7rHCl4gxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=F_Afh9UE5z66axmcnzBuUNTxntBQ0DgaQvjcuc2wNhfLdy-P-BSH6hiiiMxcVS1kRZiNx5RQFykY7-7Q022OfdxYHKZxDNLiisnI_SZnp9c7uR1B1il_ghQKO4qbifE0YJ62jifSWWxRNyF_0ij7Mwd8xq0cNrnYPwAGcXwOaSLVruZ-WU9A_YgLfRTmSW98uLPui0h7NI8rcR-HJK8IF3BgRPcq1jEd6teFcSMA1R6HrQknKxJiYxLK1vV1bZvHQURVZhEm-7JOYjbXPyAlw__5RzIvBx5eRMbrbcR8Vs_5gTttj4J8LlyKlGlRBk0rtVdJhTH9ZytseqH3JvQtE1NbLWAfG8PNivvs1vQkEWPdo_BsyT1SFTFBYef5cszlCpdfQQKGdlG1CdJ_oFRumf1sxKH0nmFrwQMW2m-LjvsWoB4ROPoEZv6W6iIe2tUiN3EwtA_Fvb2bxdGtCWk6dmc0QHgNsjgmUcJLZlaweG0Z1albetTJ2d-8LeOdpoTcih81MhUUkiVsZj0OYfQxfElbz_QJ7DDXm9wVA0bCltUbZu08cDe0U6la6sQch_An8R8v47Eg1kQ-UJUp4eM_NuQ3QDCJ2kEM2hzYOFjlkr6AZAVXhYAHdLmJnm1181gzE_agZdBXyPgcly6FcTDVJyFW0XxeUeIFRMFpJ54FFUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=F_Afh9UE5z66axmcnzBuUNTxntBQ0DgaQvjcuc2wNhfLdy-P-BSH6hiiiMxcVS1kRZiNx5RQFykY7-7Q022OfdxYHKZxDNLiisnI_SZnp9c7uR1B1il_ghQKO4qbifE0YJ62jifSWWxRNyF_0ij7Mwd8xq0cNrnYPwAGcXwOaSLVruZ-WU9A_YgLfRTmSW98uLPui0h7NI8rcR-HJK8IF3BgRPcq1jEd6teFcSMA1R6HrQknKxJiYxLK1vV1bZvHQURVZhEm-7JOYjbXPyAlw__5RzIvBx5eRMbrbcR8Vs_5gTttj4J8LlyKlGlRBk0rtVdJhTH9ZytseqH3JvQtE1NbLWAfG8PNivvs1vQkEWPdo_BsyT1SFTFBYef5cszlCpdfQQKGdlG1CdJ_oFRumf1sxKH0nmFrwQMW2m-LjvsWoB4ROPoEZv6W6iIe2tUiN3EwtA_Fvb2bxdGtCWk6dmc0QHgNsjgmUcJLZlaweG0Z1albetTJ2d-8LeOdpoTcih81MhUUkiVsZj0OYfQxfElbz_QJ7DDXm9wVA0bCltUbZu08cDe0U6la6sQch_An8R8v47Eg1kQ-UJUp4eM_NuQ3QDCJ2kEM2hzYOFjlkr6AZAVXhYAHdLmJnm1181gzE_agZdBXyPgcly6FcTDVJyFW0XxeUeIFRMFpJ54FFUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbY4EDgD7yMCoGoOs05wYQtE4L7yPuJ2EEpftJddmvn1f-DeVisYKgT6GmaTRlDZ4mYAlb10RldwLu5BExLELPxUqzvpDbPSHbA4PoDoQB9cyWqn-WvhIJ_i95chlQo3BleR7oShBJYZf36RGw6-HB61sdmcNXmActn2tvEBr7HHVlkLmE-YKLBiBNAoBrsPH--R4DhphOKvD-K99Tsbq270w_5Bu9OIGOsUQsfTqf44ffwFWzMSagHERMlBLZ2-2CwY4FPKJHkbuEF9e1iq1Ip5NsiniTZ2ueW-fmlb2McU6uMP4K2iIhJKbmnw2tvH79EeJOxI1zb4LgQ0bSxwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q62otksz9P_50fq9_WtyceiB_yBhGF1zTvWZjt1y10L5MI_NlNWDOAYG3jD8tVc608wxa0k16j1zaazXb3bSG1OtYS-d0iKhUrRbaGNYNx7JFZbP-h6I1fMoXVQ_L0Qhb7s2aAmcRa5k9aERSEMNdCSD3TaK6GbSSzIgOFeNrZVlPFH8pNNfgHu0qVmtn83vwlUfFwKeWhJqI6wfvEcexRtVxlwQ5Fi_RZQs-nAlRVO_gDjO58QpS5EariPVATn1X9M4mWrkQVSU3Q0wGfUD8S8tXzfkfIGk-xTqxXG-WDFpcQ2l73e5uTKZhgaLhKIW-wTGH-GoirELI4xWbf0xjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=KAQ0wthuMjUSOMqed0pM3LydIdGDDoiFlCkV58oZZHX3VoAxEeSbnVIpBi50CjEpezXyWZelUzaWsoCx5OSHJOkySeaKtjcelA8UJBzUpZC7GIT8XcYd5MabJI0_YKw7nn1ZsMgqSOKFtyhv9-gxIRw3cYZiSq0Sac7bPyhLMgKnQ_Jm1MLoJ4SFh_u0xhOoVkYkH4q6jzpM2yi5VQHnynh5UDySCeJTC1MFQSUFHzEjumw61fDiWyfNDl1v7G3ThSGW6z7rnWUSrbv-8gA6ExVqXuZ2grgRSQlvx74-g7F8RM5o5zRi89z1ZzC-l5YLOcaoerl1d3iKtNH42WStiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=KAQ0wthuMjUSOMqed0pM3LydIdGDDoiFlCkV58oZZHX3VoAxEeSbnVIpBi50CjEpezXyWZelUzaWsoCx5OSHJOkySeaKtjcelA8UJBzUpZC7GIT8XcYd5MabJI0_YKw7nn1ZsMgqSOKFtyhv9-gxIRw3cYZiSq0Sac7bPyhLMgKnQ_Jm1MLoJ4SFh_u0xhOoVkYkH4q6jzpM2yi5VQHnynh5UDySCeJTC1MFQSUFHzEjumw61fDiWyfNDl1v7G3ThSGW6z7rnWUSrbv-8gA6ExVqXuZ2grgRSQlvx74-g7F8RM5o5zRi89z1ZzC-l5YLOcaoerl1d3iKtNH42WStiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE0odP4J7DrAR_abRvxD1DSZlAvMDK3ujDT8RVBOWyigvIs93bbJtMNDHNOR2GPvjR4C5DbReDbzjy9XbXOYQF1c1kNTtSSuUdFlno7duJeBJGevrXq15ZRGOrk_EB0AlHz02kFTsq1EUxAZcKEeKd4bSucKDt6MO1FNjqqDw-geKaquDrbQ6gxJwkP4fL-nU4hqXLNLhfLrSm6gMtflm6frnbBkDcl9paO1lIBcGglEp8DfUGMX4P_aM1pTt2RtRIYHztT-YNMimGuw7d4FXwRSdkw-Y9Wy_DShyac3jvL52GBSTJW0I0u_6BHvO2mQ9q8hdU8tdBGe6BxOa8KmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0BOqitLlO9ZpyFiZUWxvdRNqpWFeiKp1u4cgzvoP3StWnJZyFJqsklDES4IWizBFfzAF6FOjxFVzlYcYws_Hs76VW8QCJ0_yHMUhtXmy-EWo2wEISY3ibQXu1dGu_vAOa1xEk9_05X0qgrFtjzwBNa5XlDOUcukPXClz1puUZk8tQA7l2ot2MT9Mp63gd95QsYxfRmXr8NBTZekae-Eu4PkBXflcLKyrtNX02LhPqamBXna4mEyr_14nFmr5MlqQr47jIkBolUNOqnxVPke9_LCDTaYa1yKoAVhizrdGTrU7T9d6QT_HhaIE_a0j0pKQsns_H1dTfT4Jmv0tmH0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfNeY17vCApYEAgCUYMYiKXGv8PjTFpe9TgClgHEJ6LuFEnAfJyA9OS5D3WFF0AG8Nq_NrNlVELelbuPsNDWmP4sjDQr58YwweElcqJfphaDh4KmGPBjzxPCItuMie-yzFXKwl76p64IkQnWW2c3dmAFee5Gred5D9demo76SjWIAqcVOD4BxmlpTmYvkwAQbDqOh2XPdtdy3GJBYRxtuAnCqgNqNcxagitM3V1P7FfWMirdXf1vo18ZtFN2g_AmYsfZ9uMYKzDeQm1Vzw_554SwMrehhAX9W_q9kfwofPOAJWcSWt9A7E4l_lvbgsZJrEKl81enSrCbDvUT02DfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utmx3fNS-GH3fBva4SOXeEiYAxHjHxYNyXnXGo3HtzKf_yV-8Fxo9iSqmzX3RK4ZQPp9-SkIbBoBoBt2ecZJfMZd-5qyXhi5XSah_HdyjHOtzNmcZmbpRJHT6yfPlMWc5iNN72H6h1bamPqTBGT_ZKbhqXZvvt1Swz5C4O1bJFLW6sdTJyeDA5RpAdbtH7sIagjZJAy9ngztEbljxzMdyZjClbrpRwBT1pC3RdWhY1WPCqo3lF9u5ZsAGi99xx8BkXfuP20jIm4QQ8gOJJ5qvC8GcW-0IiraGX4Y5Ds9Xv90_XS_RyBKdnOe1UBxTQZakTgfhnt4XGqviuJ814u2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBBpHSZjBBMIQsHkdCLDNMV3L-81YK-dJ6S81YpuqiRwI7MDkwABVliS2wD5jAPdqQZhIWwN9HE13IGORJqfwQZHRCv0TUTUBICWarvT01qxoZC49dpIpECuZQ6_1O4EzRxbBiCsxx60E8yLat3U11YB0-UTF-sIRce5jBk34hQ_x8faUwTk05T4jq3kOjAs17cx8aGY_tZ4z4yJ1_--dDatLX0kWE55OjqV0k9pB2f67VV8kzKXsZuQoa-6BbCV2azik0ntdQNQHENKP_6WrvLPLr32DGNPxK41qU_ZPXvX0AfvKwrARvr68OP924-N5oTakiHTtAxGn5zJbjSCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1Uwqvpw39J0gtCRF2r0SWS2TqXa7jjXgQU6eIN5m0nx2W24k9y8NzkotjzTBP1ZsHntVo6zznL1qOfzHTrpkh5ADVAkkPbAs29fycfT_O6ENVazh2_AOSq3HYWO7l903uV9ZaNyEFsDYBl7DT5_IQd81Iz2x_PLfWCaA8MDku4ZV7NRKi0GLmsLN5BsgL39mIMEopA-6uRvkRVB4CHYSN3x76yPkC_WR4TkFxSZJMAUGRAoReNErmEfYubrr8TpLh4K9wHByS9rdPg_xC_gJgDO3u-myuk2bSkWAKwJPv_Ibc2ZACTqs4sT5RAny7OPC9AGZ5bhQ5xIT-fXmdkuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlvmtI-O2PtxrTx7rmHLTl0qseWMJiY23oojwKkL1B9WJUt43rD9_UH8cvmw2GOqyPJgbLepeizSi09tsubMHxmEwLHM3OwOZ-IIHZbiYG9bo2QsFe-M4Z_HSz-6P4oyc2O8jUrVkFq6LetN-N5dSPDFzHO1lpaQVb6YJy65alKGloDr3SvKsgsBICLIpvsPU-ZBVd-RuRdRDAgBQrtNPTc0YsLIUIS3t8b2hLa80qZfJQagPXDRHa7jg6Z1AXmkFZKt6XNi3VM3g23wfX4DeSGqErLmS88Cv8nnyPGeTuH2kiP5Rn7RmF2h9ga_FJIvD_gxPu15Q8JluOBRRhjiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxfC8APYdHO6fjiOQNRgFRH6Dg-JF5xqc3uHguHcN5gMoDvs6J-IhNTzCH3gVxA6BjPKkYA7UFREs9P49VX64GwL49GdDCkVPPn4CBrzNUJRwoa0MneAji_w6-BSEgcMUtBarmOmCnTZnPwfCJ-Zxd19_DjaPitEOwmRwjVYRsJQcROjJHjLNWj7K0TInkBSCZGX-k35wNDqeMQwsBEGE1jKutyg6AVPfUA9GyyOJy8enA9S9b1uLAbvhda-0hl_Eid7iWbTng9LchOj_vy7ga1Rxz1ZEhycrlzwfrI0LOM4zNsOiFWDJLWVMHIaJLQNNIKl9Ar7s9_k1xsEesijKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=Db-FT-btQOVBrmTAhRg3VlXaoLM7A96wEjmxKSlGgTMXwwIMgVDIWbog8gnrgVLQ36GurmfQ6O-r4tRNjCaap2Syhz3fuguWNfBdNXyQs8Lm3nQsalcYiPdliUy9INgQ5R0i2N9r95Fkhgpe41xXOq9BaHGZ85Vkxqfg8AxNzxrzRvnwI_NGqGCPnkX_2z_9aWChU_3nEYuIrpmwfG5Ti5mUpBlqB49r8kJCRA-TrasoVhIPuhpaRfdj7_G0Zbasvqw5F81lkC_7opt8bwxP2EIJsaIQXc1ujb_KTtL1cez1uwgEhB9y4uQ2Y0eQ_uZU9GFU9R4mYT8jv4rjnJccSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=Db-FT-btQOVBrmTAhRg3VlXaoLM7A96wEjmxKSlGgTMXwwIMgVDIWbog8gnrgVLQ36GurmfQ6O-r4tRNjCaap2Syhz3fuguWNfBdNXyQs8Lm3nQsalcYiPdliUy9INgQ5R0i2N9r95Fkhgpe41xXOq9BaHGZ85Vkxqfg8AxNzxrzRvnwI_NGqGCPnkX_2z_9aWChU_3nEYuIrpmwfG5Ti5mUpBlqB49r8kJCRA-TrasoVhIPuhpaRfdj7_G0Zbasvqw5F81lkC_7opt8bwxP2EIJsaIQXc1ujb_KTtL1cez1uwgEhB9y4uQ2Y0eQ_uZU9GFU9R4mYT8jv4rjnJccSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itZZox4u2D3OFexUwCxrih1txTIZTQqHEC8E4iLb8b1BMUV_4_eECidvI377NETr0j9F5fKCMFNpeYT8GMM2nH__f4-yEy1Vlx1N5EhEy5U1pA81LolawKETMyqatwyGi0bw9Tm03JBDFegubcf-rB7L6QUW62dn34AF6zdaylFAxQCaC2XRAaMboKZVZL9QUNSlKia0bdQk2Tmy424xBWTwvknm8NH_R00OkuJcpGixeuZAe1SvcEQHcmM23Ol9IWs87_UlHZAn033cjrh4BggfIsjhfnPZ0skmsmzxJ9LbdlLbltqYmSEQ4RyRkv1CDJd78qRqP7A6F3iCwkQkcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=vNEu5JtaK4WLgsbJjAbZ1eu1b8a7tat5UPxydgDbJ2VgdURCECwMs0WNIBnhg7hRJR1jcjqELEZ_PgLMwGh17U1n_4ZPUpfxZwEJJ2XYivo49wFZc8L2N6v0B_TQehR27XcxS6X6zxP3RiZKE5k7rNoNQAku4ZaX3DMNwSluYlz5tMxukZkVEi3vB-fm4zDO6GyuMb3o8riC7qOi9a8K-aYuN_ibDnpP11sVOFzcakQiKvyE9QkfunQ6mhQx1XTBfUnGvRY0j2XM6w8rB4WXwgBPtbWlfGqLDLEinfDtZcj8CIyWkdfIg0t4j6ZWdmAGcihnghznlvjpAu4x9HC09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=vNEu5JtaK4WLgsbJjAbZ1eu1b8a7tat5UPxydgDbJ2VgdURCECwMs0WNIBnhg7hRJR1jcjqELEZ_PgLMwGh17U1n_4ZPUpfxZwEJJ2XYivo49wFZc8L2N6v0B_TQehR27XcxS6X6zxP3RiZKE5k7rNoNQAku4ZaX3DMNwSluYlz5tMxukZkVEi3vB-fm4zDO6GyuMb3o8riC7qOi9a8K-aYuN_ibDnpP11sVOFzcakQiKvyE9QkfunQ6mhQx1XTBfUnGvRY0j2XM6w8rB4WXwgBPtbWlfGqLDLEinfDtZcj8CIyWkdfIg0t4j6ZWdmAGcihnghznlvjpAu4x9HC09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=YSdv6W8K_TJEGZoLT3Gju_0KkeH4Q_sgMIurYww_r6LZ26i5y3BlkhHGPUX0_eWxlBKdiYRZR8FrFTlvj6dTlghwu0PwaCP2nrR5PoaAHJN8X-3lttONWO1n1Ga6kI5URZbdpLYCsqHqYfjAHrxB4qb5_dkcN0-jIRXWKIiXBABX5qKyR8NZrJEs9PBOC_9Mh2ER4FK0WS0qDgL3S3J9SbwCHvoYo5oKIFNUnahELYDUHTKuM-RKDmG3Jnjs2jlLpsefD6F-yDDLtZQyuH7WazE9ZPtmoKw60GXy2a_bqltQQP570xbEHCzXLFOhfqJPbnG9Oy4F8JHVuzXQhzJTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=YSdv6W8K_TJEGZoLT3Gju_0KkeH4Q_sgMIurYww_r6LZ26i5y3BlkhHGPUX0_eWxlBKdiYRZR8FrFTlvj6dTlghwu0PwaCP2nrR5PoaAHJN8X-3lttONWO1n1Ga6kI5URZbdpLYCsqHqYfjAHrxB4qb5_dkcN0-jIRXWKIiXBABX5qKyR8NZrJEs9PBOC_9Mh2ER4FK0WS0qDgL3S3J9SbwCHvoYo5oKIFNUnahELYDUHTKuM-RKDmG3Jnjs2jlLpsefD6F-yDDLtZQyuH7WazE9ZPtmoKw60GXy2a_bqltQQP570xbEHCzXLFOhfqJPbnG9Oy4F8JHVuzXQhzJTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpFkrocizlRx8iLnb0gJlyxcRjXTstmLEXJVJr-t2ivAE_O3UnzySECWpMvG9OURVgZLwMm6ANdrQmp9beVIDtMziAiY50INuZk4wF-n5tCvfCQLSutL2YvPx9vWfZfBs5ni8dkcB1wWnUE0cRen-Tu_ld4XT9sdOVjkf1nECk0seTNqh-7EXbsZSy3n3LCEFJD_B8_fOLyklqd31O7LXEF_Y8vL8IyVrZQAR8pw54OFv3IkN1TohL_4TcpHQLvNLKa8e9pH6TrilwKxSBCo-RmHpwBi1D3Mw-ub67Z6m4jWAub-nNMnYTdXg1_-0Vg52tKytsifSF6JsoKU1a7VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=iGS-Z0GV6WvQZsQaDLwXLJkAONP_VtU7ZhkdHs31wCPoNbaLf-sEjxExoy_uCwU--NzJhB2LlhnEK4nuT96IORl9QoYXdAxOusOxx5iwOsOf3zqAD2X_K6T6pTDl9FEBmyttwy6a2rBQD8-t7i-_3a-ztYIdGXxvvBM3aFbBarzog82NQpLLz8he3ke3sl2uKirhmUSghYdNKy4BKKYr0ObBFE4wFqTAFcfRmIfYwmULATlhe-jCaaFUEmiOyJ6ZX2zJrV2UgrnMhnMuIuXK1j6VEzJrmygqr-b5icXkDPteoymusLjzD-j4rKMJU62A6i6B__nJi9ucOZJdqgLGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=iGS-Z0GV6WvQZsQaDLwXLJkAONP_VtU7ZhkdHs31wCPoNbaLf-sEjxExoy_uCwU--NzJhB2LlhnEK4nuT96IORl9QoYXdAxOusOxx5iwOsOf3zqAD2X_K6T6pTDl9FEBmyttwy6a2rBQD8-t7i-_3a-ztYIdGXxvvBM3aFbBarzog82NQpLLz8he3ke3sl2uKirhmUSghYdNKy4BKKYr0ObBFE4wFqTAFcfRmIfYwmULATlhe-jCaaFUEmiOyJ6ZX2zJrV2UgrnMhnMuIuXK1j6VEzJrmygqr-b5icXkDPteoymusLjzD-j4rKMJU62A6i6B__nJi9ucOZJdqgLGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1IZKZWWyXVb8xw_Z-WC6R8iBqHkako7kXaTDGh9BHM_UR1Tq-a-ICM47ExLViPKQfJbt0AzOC0yf_VSOeXCtciz3hn6B7OUTJc9UN2G8UUrlZewJBDDFgqDfEkq1bqpeQACm09biDuFF_mh27rgecZqrz7TBLIxeF8CRpOSLgFKfWhcQfkujpUZzJyMJOVTXJvGyOETwijtppDA5jx65p9LsGtL_z2F-v8zM85zaiXxEMLRouMVedwSnUmDneSBS1w3NnzOMh11zvfNrtpW00bva5HfI3ogDUVsNQ7rI35Av6niQr9gQyzcCSOwX5-Mgcunq8pflkCTTbZnvQ463A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGHYX8yzS4l4IOXjx6CwivqzV8dB4-m9ZZ60sB_V-sdYNf8DECdheANMQI5NkLYlUBxZNPfugaZV7vJL1O0AyA_1A2Wa12T8OhRdqT3sc0VDn9m1UD3wALdxBI93qaV2K-bQDmmjTXPQKPOomZ2cCAOq_DAE07N2iVBNlo0MfhOFKMJ_KuiHQAk941Yt3YhPeAqvH-R4oLYXE28W1wliVwSx8tTWhhme1c4coocca614q8FRe7DOgcTSey5WC8-3sXrDcjzLTZUzUNRSAsb2gbMv4zYQnFmzn9pCi0VS-rVHriW3gZW6vHpu0OOg_8cNDHXRWvFcLRjqGjnJBQtOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGf-aVgLMc3XJGc2xT1HD8xw3ryPf1sS6L848Zy1mgZ-ZK0SzQPoMdiOW_-nU03tafxFDmL1XqyrRhhnLGZcL6Z8-LxoOjFidizmXjnBqi_2l6T86T_WysBs6962pmPfk0eMpYyfriAGZrThWY66yLXKD3a6NwUDiq36KeCSRHEab0Tyu-TqWo6n-JmpKJ16rsAAoTM26R_G7wRckTkr_ltzOgRQ3HofSnh1kKrcd5PO4DuYbb-S5Q6aYnN0IC_bc3ZWjDYt5wIN8l2VksdD6o8nCHTqDLdUjoZv3J_dp4sL8YboT2bjpMcqZRUW0SFYvnl1SHZ9yFAampavRNMF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWMvGRv1MYlPoVAeYOUbAVtZgF-9B9PD6B7J86a72kfGettQ0-ahyJBcYg3UUhcnROh0Tndk5ROfnmClOZbG4_nJgsahYj-vD8SoMNAfJffCTxj7JkT73ybcgGNG6TCkKTcINmSLKZ_S7sAcXmam0mJf3vZj5zjSWZK-7Gn72sOqjhfGeKp5FD2FfKHAGKb4kOpTQShha0bRuP0kOcELTs1drNRjjVUyw67vIP5eYfx3jqXinZn8BgSNr2J5iW5MW6PLjAEIpcKHvazHIp39eCCSX8awWvFEskXs9jshKSH88f8WH4dFw0UY3TEcShUV67D9cjIccNqSRTf5fKQbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
