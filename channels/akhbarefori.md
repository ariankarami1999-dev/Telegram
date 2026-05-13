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
<img src="https://cdn4.telesco.pe/file/ei9NaVnKPmeXN0n2nZKXXwmOnxMxfDo3DM976HcReRA3IYQBaccEQi_YsqcSwO_Guec-UEkb8Ydp6bFbpKfHD-qz7olP0bMai7aXGiGMX2dwSeLm4Xhf384OXB4cjRo6Mbsm5fYMdakqIPJo84fLctKrhftAaO7Exp21nZSdohzQ1Mt9mwMytmfmetrx7_-kBoaywBlg0pqIxM2t1r8Lt2Qkv1wjHkNsJW9s6tIRBY6BeiLSbJP3VU9nzbO05Ump7MHs0kSQnY_XNGI5MQZKtD8dYFeVfGZm7qnAphmISZxl6m29IdvYgqRxurLcRs7UTvV1LdkyrV05HdTovpYJCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.92M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 01:21:45</div>
<hr>

<div class="tg-post" id="msg-652209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رئیس ائتلاف حاکم در اراضی اشغالی، با مشارکت تمام رؤسای فراکسیون‌های ائتلاف، رسماً لایحه انحلال پارلمان این رژیم (کنست) را ارائه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/akhbarefori/652209" target="_blank">📅 01:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf6sWzwHurecJNQJSWpzhPQIRMzBHOb4M7PqoVZ5RCi9ZE84l4lD1qX8K39sLhre6XGNLPGZvImdu6SexY0zzV_dy__xn5q3aFEQ2uBNg1A58i7jnHgOODQmJ72v2WOY2UC2AzOPn-fYaDY8kq0zdKwEvCJAsJBTKWQ4WNwdKEThYshSWrpiBW81BF_28-CIhMem7jboFdIiiaaNR9UeWQEcrCVgC0ZVAEOGzjr7NRP7je466NKe3tRagdT1uAldcbv5BwQt-DiuRr9aoiOPEd_mskwo7MWrMy7pki-PClAOtIMo1fZm8EpLeKvA5GIOU60tn1FXMRNTIR7O2PLneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بجنگ برو جلو
🔹
تیم ملی فوتبال کشورمان بیش از اعزام به مسابقات جام جهانی امشب بدرقه ای خاص و متفاوت داشت و در میدان انقلاب توسط مردمی که بیش از ۷۰ روز میدان دار خیابان بودند بدرقه شدند. ملی پوشان ایران میثاق نامه ای قرائت کردند و گفتند که قول میدهیم تا پای جان برای موفقیت و سربلندی ایران در جام جهانی تلاش کنیم
🔹
هفتصدوچهل‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori
,</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/652208" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
توافق محرمانه آمریکا و چین بر سر ایران
👇
khabarfoori.com/fa/tiny/news-3214648
🔹
سخنی که گور بی بی را می کند | نتانیاهو به زودی ترور می شود؟
👇
khabarfoori.com/fa/tiny/news-3214727
🔹
حرف‌های منشوری پشت سر امانوئل مکرون و گلشیفته | سیلی برژیت به‌خاطر بازیگر ایرانی بود؟
👇
khabarfoori.com/fa/tiny/news-3214825
🔹
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | آتش‌بس هنری است که ترامپ ندارد
👇
khabarfoori.com/fa/tiny/news-3214576
🔹
تمام قاره‌‌ها درگیر انواع‌‌ هانتاویروس | بیماری که با آنفولانزا اشتباه گرفته می‌شود اما کشنده است
👇
khabarfoori.com/fa/tiny/news-3214245
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/akhbarefori/652207" target="_blank">📅 00:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652206">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حال دریاچه ارومیه خوب است اما تو باور نکن!
محمد کوهانی، دبیر شبکه ملی محیط زیست سازمان‌های مردم نهاد جوانان کشور در
#گفتگو
با خبرفوری:
🔹
بیش از ۸۰ درصد بستر دریاچه ارومیه زیر آب رفته، اما کارشناسان می‌گویند هنوز تا احیای کامل فاصله زیادی وجود دارد.
🔹
با وجود بهبود وضعیت، تراز دریاچه به رکورد سال ۹۸ نرسیده است. سال ۹۸ تراز دریاچه نزدیک به ۵ونیم میلیارد مترمکعب پیش‌بینی می‌شد اما در سال ۱۴۰۰ بدترین ترازها را ثبت کرد و برای رسیدن به تراز اکولوژیک باید حدود ۱۶ میلیارد مترمکعب آب در دریاچه وجود داشته باشد.
🔹
کارشناسان هشدار می‌دهند کاهش بارش و مدیریت نشدن آب در تابستان می‌تواند دوباره تراز دریاچه را کاهش دهد.
@TV_Fori</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/akhbarefori/652206" target="_blank">📅 00:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652204">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYm3wHn6dq2R5zklL6mTEixvv72C8RIW2Z_nfh8kR_c6p6aIrv4CDJK8JSb9qpzIcAzCN7AFQAbbiEyNNp-9gB3uU_T6jSiylEn91t5OTWWh7PYGYMf4gdJa1IKQJyS0yHsMgwewz3cmp4AL_Bfa0moZ5wVK55XbNg9KUh4wb5MZ1ez7X3Z7bbRC0eK_r6GqRtN1MpN6nuDd7iJHcBgqwDImimslP787sQBeciSeUd8IeJbUd5RjIqeVt96uNHSi1JHgUWutujFMCAXp_O_P1_DBIIvxkx1dK9bG-yrphr35p3bg8YIBjy7HlyJGQ0PE_mgHOGsq98zUPz4ZYIEmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی: حملات حزب‌الله شمال اسرائیل را فلج کرده است
🔹
مقامات محلی اسرائیلی به رسانه‌ها گفتند که حملات حزب‌الله باعث شده هیچ فعالیت اقتصادی و اجتماعی متمرکز و ثابتی انجام نشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/akhbarefori/652204" target="_blank">📅 00:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652203">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش تقاضا قیمت کاغذ را کاهش داد!
نیکدل، رئیس اتحادیه صنف فروشندگان کاغذ و مقوای تهران، در
#گفتگو
با خبرفوری:
🔹
قیمت کاغذ تحریر و کاغذ A4 کاهش یافته است. کاغذ تحریر از ۶ میلیون و ۲۰۰ هزار تومان به ۵ میلیون و ۷۰۰ هزار تومان رسیده و قیمت یک بسته کاغذ A4 نیز به‌طور میانگین ۸۵۰ هزار تومان است.
🔹
این در حالی است که کاغذ A4 در هفته‌های گذشته با افزایش ۵۰ تا ۷۰ درصدی قیمت مواجه شده بود.
🔹
جنگ بر روی افزایش قیمت کاغذ موثر بود، اما دلیل کاهش اخیر قیمت کاغذ، افزایش عرضه، کاهش مصرف، کاهش تقاضا، نظارت سازمان بازرسی و کم‌کار شدن چاپخانه‌دار‌‌ها بوده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/652203" target="_blank">📅 00:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652202">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
توافق محرمانه آمریکا و چین بر سر ایران
👇
khabarfoori.com/fa/tiny/news-3214648
🔹
سخنی که گور بی بی را می کند | نتانیاهو به زودی ترور می شود؟
👇
khabarfoori.com/fa/tiny/news-3214727
🔹
حرف‌های منشوری پشت سر امانوئل مکرون و گلشیفته | سیلی برژیت به‌خاطر بازیگر ایرانی بود؟
👇
khabarfoori.com/fa/tiny/news-3214825
🔹
روند مورد علاقه ترامپ: وقفه‌ای کوتاه پیش از دور بعدی خشونت | آتش‌بس هنری است که ترامپ ندارد
👇
khabarfoori.com/fa/tiny/news-3214576
🔹
تمام قاره‌‌ها درگیر انواع‌‌ هانتاویروس | بیماری که با آنفولانزا اشتباه گرفته می‌شود اما کشنده است
👇
khabarfoori.com/fa/tiny/news-3214245
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/652202" target="_blank">📅 00:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652201">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfHqeolspBs83CbWTvzIKxx7RKTd5z_PCLQlhzchWmydlfE7OFCrSC_lNGNVEPuLsNjC-19z1_U3J_pZBd5650ll4qr9rpSZU9kx8GlLOocLocnTOZXK8QV7R1UVguOzDZl_lGl99aifzuVbFxENrp-25t5bcfW6KSVmBuK5t3FpvuMrgxFO4YxCCUefdscM54Spx5QurYzjpOT8xHF6p93-i5hVvHeHftcVYvnYm4KCeTXLtyq5AKyriux0tVUdS1gAg7cFNX-gtQ1aczwITKJiERInppMM8Cdzuskf9r4i5_X5l00Cj4o4km_X5TXU3Ri2-gcR5ulkF4CuMop3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به اظهارات اخیر نتانیاهو؛ همدستی با رژیم اسرائیل غیرقابل بخشش است
🔹
نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔹
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔹
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/akhbarefori/652201" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652200">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtvmL3zNdsef4ep7CMhLHTBlmY6SG0c1fpYCTJfb_B5rvAFRmIE-IavWDqshBHeJB6t4FJPO3Ylq_o0QjxLTONWgQhvQC4XrJenOBaJ0K1F9dWjTBoo1S8b67Z3CEzCVutLysidQv_hcaawHaYc5kgMBUG7JXntQ2DyINgHJu9gPrA_3L6oVCgEFFRgiCRKlxa4lGfN-k3DA4KGKw1gKuPkbjjDcrlLOT6ghMJrkGg5rgYZjOT_xuZCVguPqXmfg4TKLHX1dJq1p1sZMI5WSMfSZ5v23Om76iroRcj78MZwxe5GHNjBKL9hSrBexfBVsHh2lIcJcdmz3eKzIXdt1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روبیو در اقدامی معنادار با لباس مادورو راهی چین شد؛ او چه پیامی به شی داد؟!
🔹
برخی رسانه‌ها و کاربران این اقدام را غیرحرفه‌ای و کودکانه و دون شأن یک وزیر خارجه دانستند؛ رسانه‌های چینی هم این اقدام را تحریک‌آمیز توصیف کردند، به‌ویژه با توجه به اینکه روبیو قبلا به دلیل مواضعش، هدف تحریم چین قرار گرفته بود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214685</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/akhbarefori/652200" target="_blank">📅 23:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652199">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/611faee3e5.mp4?token=FOrm-NE4ZKUdYLsVFtN4FcR0ZylQU-LeA6xdGZsLryx60WiPhbqeI0j28Ct7NjICam7zX72KBGOhi_mQ_S4tOPPULtw6wXpOb-znP9-QTZRWemyIkJtscxjo_DT7-bHmcrJaT3M07mV_afls4dvRX_Z3H70qPWmTRuUMJpxX_DU_KVZ4MUzMdOAP06g9HNZTbVkQiRkrRN7-PAMCfRZRcOCWZVHV_3bdiRrk5SAeX_2m728RIpQVZzCT9ovOQ1Mu6v1iz_cW9kE1h29JyZYnhVPGUNG-mlHaq7MxetUPkIw04U4uPrQu_X6QJckjeQLK2zj9oiYtnUw1aKhtNUGPDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/611faee3e5.mp4?token=FOrm-NE4ZKUdYLsVFtN4FcR0ZylQU-LeA6xdGZsLryx60WiPhbqeI0j28Ct7NjICam7zX72KBGOhi_mQ_S4tOPPULtw6wXpOb-znP9-QTZRWemyIkJtscxjo_DT7-bHmcrJaT3M07mV_afls4dvRX_Z3H70qPWmTRuUMJpxX_DU_KVZ4MUzMdOAP06g9HNZTbVkQiRkrRN7-PAMCfRZRcOCWZVHV_3bdiRrk5SAeX_2m728RIpQVZzCT9ovOQ1Mu6v1iz_cW9kE1h29JyZYnhVPGUNG-mlHaq7MxetUPkIw04U4uPrQu_X6QJckjeQLK2zj9oiYtnUw1aKhtNUGPDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری سی‌ان‌‌ان‌: براساس آن‌چه به ما گفته شده بود تا الان ایرانی باید تسلیم می‌شدند و محاصره آن‌ها را پای میز مذاکره می‌آورد اما نه‌تنها این اتفاق نیفتاده بلکه آن‌ها توانمندی‌های موشکی خود را بازسازی کردند و مواد هسته‌ای نیز در اختیارشان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/akhbarefori/652199" target="_blank">📅 23:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652198">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvGNy3dillNJM8e31Hzb1be1Q0gVbrkmQkdyrHZSTVqVf1W-gA1udbYuBauOXsKwGy0hZW_UhAee20xDjkqn6Agsb_I9NpDo0602YtOCWV02JtSCK4pylUeiC9En2VQ5zQY5bslirG9PgwEke6gAEVejupaPmEggDYunU5MN4K3She1qRrETaIksJHDtioUnrZvaqd8yQobeblmCQwGtp6LlOa258HCnu1hJM0ySeLQpYahTNIqQGA96mUlimyab06ml191kwAHTx9CTi4DgT5G7K34HoJwfpTVn8JMVSck9BkBEteLKGMQV8AI1IGTjCbGF_7obBqfZafuf0gKQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر روسیه در پاکستان: مسکو آمادگی خود را برای حمایت از تلاش‌های دیپلماتیک اسلام‌آباد با هدف اتمام جنگ آمریکا علیه ایران ابراز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/akhbarefori/652198" target="_blank">📅 23:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652197">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bb06e773.mp4?token=ea1s5ItNb1kKruk1CLqpOWdDnMypRS5SokcsiEvYYWyxkhOACTJjWKb6KqICeSm1BDYyceuyEMUnWMetMhbgkYi3VDp_Mf62A-LbpNyDiCHlW969ldrYA-iJljPASxWMaLW0fPPujx5ZxgmBcylhVX60zjmwUf65xTfJZSlrQEEhzOWM6gotXMPm_4irVSiTS9HX0CRqWS86ImkiMUY3wjFotguR0pubSosFTwUx-yGJHlJEjS9WDeG3mytEx22DszxltWeHl6c0GhDOEcTyh0U3Gfwz6_RclNL8VhvaGNbtJ6tsJp5jQokI4kUb8HO2_hGWEXylzQfhWNDF4kl1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bb06e773.mp4?token=ea1s5ItNb1kKruk1CLqpOWdDnMypRS5SokcsiEvYYWyxkhOACTJjWKb6KqICeSm1BDYyceuyEMUnWMetMhbgkYi3VDp_Mf62A-LbpNyDiCHlW969ldrYA-iJljPASxWMaLW0fPPujx5ZxgmBcylhVX60zjmwUf65xTfJZSlrQEEhzOWM6gotXMPm_4irVSiTS9HX0CRqWS86ImkiMUY3wjFotguR0pubSosFTwUx-yGJHlJEjS9WDeG3mytEx22DszxltWeHl6c0GhDOEcTyh0U3Gfwz6_RclNL8VhvaGNbtJ6tsJp5jQokI4kUb8HO2_hGWEXylzQfhWNDF4kl1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی پربازخورد در فضای مجازی از تشبیه فروشندگان vpn به خوک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/akhbarefori/652197" target="_blank">📅 23:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652196">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نسخه نجات بورس در بحران؛ چرا بستن بورس خطرناک است؟
🔹
بورس بیش از ۷۰ روز است که تعطیل شده، اما راهکار واقعا تعطیلی بود.
🔹
در این ویدئو چند پیشنهاد جهانی برای عبور بورس از بحران‌هایی چون جنگ پیشنهاد شده که می‌تواند به بورس ایران نیز در صورت بازگشایی کمک کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/akhbarefori/652196" target="_blank">📅 23:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652195">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dde9b497.mp4?token=gP-yAHa9tDgb9LCgWcbz9gx8uIlpZG5YxFtnAQbKdkf4A5_W1minVl_Ajwd6eZ4Le6itberPX3PrsNaAaGZEXQSMxRJ05wmMH8FcqFpxhFlqHhCdK2tIoBbMWJtc55FKyzhFdEToDAfnkUAn-WTiM1NV-8_I5u6OfnzcvwQqx0Gu6nwLhoOBWadb2sMj4tT8DcPBukHnom2rFqnAc83rsmwwmIM3oxfvrceQpJjjBn1UXiqz8-nC9yHuPzzvJWJwZRUM9mYRf2MLiu0SN4dYrch8lCE8EOHkgEoWCRVkTTdMWk9gQiZVV4DrkoFpnAKG-0j0uhquQzLPErj4jKYVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dde9b497.mp4?token=gP-yAHa9tDgb9LCgWcbz9gx8uIlpZG5YxFtnAQbKdkf4A5_W1minVl_Ajwd6eZ4Le6itberPX3PrsNaAaGZEXQSMxRJ05wmMH8FcqFpxhFlqHhCdK2tIoBbMWJtc55FKyzhFdEToDAfnkUAn-WTiM1NV-8_I5u6OfnzcvwQqx0Gu6nwLhoOBWadb2sMj4tT8DcPBukHnom2rFqnAc83rsmwwmIM3oxfvrceQpJjjBn1UXiqz8-nC9yHuPzzvJWJwZRUM9mYRf2MLiu0SN4dYrch8lCE8EOHkgEoWCRVkTTdMWk9gQiZVV4DrkoFpnAKG-0j0uhquQzLPErj4jKYVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب آبادی، معاون وزیر خارجه: موضوع تجاوز نظامی رژیم آمریکا و رژیم صهیونیستی علیه ایران، در گفتگوهای وزیر خارجه در هند مورد توجه خواهد بود
🔹
البته با پیچیدگی‌هایی نیز مواجه هستیم. یکی از کشورهای همسایه که عضو بریکس است، در طول تجاوز نظامی علیه ایران سابقه خوبی از خود نشان نداد و قلمرو خود را در اختیار متجاوزان قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/akhbarefori/652195" target="_blank">📅 23:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652194">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
چینی‌ها از افزایش قیمت نفت ناراضی هستند/ تاکید برای بازگشایی تنگه‌‌هرمز در این دیدار
عرفان حمزه، کارشناس مسائل چین:
🔹
با توجه به تنش‌هایی که بعد از روی کار آمدن ترامپ پیش آمد، یک نبرد مخفی میان آمریکا و چین رخ داد.
🔹
ترامپ می‌خواهد چین نفت را با قیمت بالاتری بخرد و از ابتدای جنگ نفت ۷۰ دلاری به۱۱۰دلار رسیده است که افزایش قیمت نفت سرعت توسعه چین را کاهش می‌دهد و چینی‌ها به شدت ناراضی‌اند.
🔹
ممکن است این تنش‌ها جدی تر شود مگر اینکه آمریکا و چین با هم به یک توافق جامعی برسند.
🔹
پرونده ایران به عنوان یک مسئله اقتصادی و سیاسی برای هردو طرف مهم است.
🔹
احتمالا در این دیدار هردو کشور به بازگشایی تنگه هرمز تاکید داشته باشند.
🔹
توصیه می‌کنم سیاستمداران ایرانی لحظه به لحظه این رویداد اقتصادی و سیاسی را رصد کنند تا در صورت نیاز بتوانند در پاسخ به آن اقداماتی انجام دهند./جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/akhbarefori/652194" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652193">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/856039f6ff.mp4?token=FNo9CYcsv-HbnRwSJ9Fl-b85uthyqnhlTeVxS2ZTwYKvxJntB82g5Ypt6q2S_QIfiyF5kjfTPlE1PG7qv68icm1GaoGJXvSS0PxfihwT0J-uiYPFo8J4_Gh7URQLMt-Jva2yOhpVHVRPU72Z0ljBlffDo6zqALzcQ462nHvnGZGYsYy7niYWaKafeThnSwFO3PhPLZ0R8ZUdt1w7qrh7du9pDlzvA7OLXcvrkQHXaPKfv5okiuIvdwkfyyTkXtHu9RIjpcamBx00Xt1EvsHG-DyG6YhcMAwK_vzzA7jMAHWzM2_Khca6g6tN5yWVyqje2F7nkbx7vKz72bEcaKyfzzUACJ1G2aJUyiML7opbrbCYXBwcC0eGP0-U59SG0KF6rBiEAbBP3h0NxGErmsd6y8423mm9JvdZBiy4De-WWw_wMYszMm2vX58vJMQxBd2I9lnPFlO-CB7OP82nVJMGJU066biib6h8U_CfkAJWRosqWFZu68tSJBAFQE0lQkJ-ETLwBX0jnzJqmGS9zhnQSHeXCVRVeOMPrAmiiJmtafurOoArx19bj3ECglTrs0jU8v4e_XsBGYKdjSwuwz9xCxyfZcQwcwE3E9V3DojjcRQRVzAgx7F_TiT3OTJtJqPj_ghK_DZ8bZ7QyLHvwtmH1jmdqVAfPx7cgqAeJ4hiIG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/856039f6ff.mp4?token=FNo9CYcsv-HbnRwSJ9Fl-b85uthyqnhlTeVxS2ZTwYKvxJntB82g5Ypt6q2S_QIfiyF5kjfTPlE1PG7qv68icm1GaoGJXvSS0PxfihwT0J-uiYPFo8J4_Gh7URQLMt-Jva2yOhpVHVRPU72Z0ljBlffDo6zqALzcQ462nHvnGZGYsYy7niYWaKafeThnSwFO3PhPLZ0R8ZUdt1w7qrh7du9pDlzvA7OLXcvrkQHXaPKfv5okiuIvdwkfyyTkXtHu9RIjpcamBx00Xt1EvsHG-DyG6YhcMAwK_vzzA7jMAHWzM2_Khca6g6tN5yWVyqje2F7nkbx7vKz72bEcaKyfzzUACJ1G2aJUyiML7opbrbCYXBwcC0eGP0-U59SG0KF6rBiEAbBP3h0NxGErmsd6y8423mm9JvdZBiy4De-WWw_wMYszMm2vX58vJMQxBd2I9lnPFlO-CB7OP82nVJMGJU066biib6h8U_CfkAJWRosqWFZu68tSJBAFQE0lQkJ-ETLwBX0jnzJqmGS9zhnQSHeXCVRVeOMPrAmiiJmtafurOoArx19bj3ECglTrs0jU8v4e_XsBGYKdjSwuwz9xCxyfZcQwcwE3E9V3DojjcRQRVzAgx7F_TiT3OTJtJqPj_ghK_DZ8bZ7QyLHvwtmH1jmdqVAfPx7cgqAeJ4hiIG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا جلسه اخیر هگست برای افزایش بودجه نظامی آمریکا اهمیت دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/akhbarefori/652193" target="_blank">📅 23:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652192">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده‌شدن صدای چندین انفجار در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/akhbarefori/652192" target="_blank">📅 23:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652191">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سخنگوی جنبش حماس: آماده واگذاری اداره غزه هستیم اما سلاح مقاومت در مرحله دوم بررسی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/akhbarefori/652191" target="_blank">📅 23:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652190">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آخرین تغییرات قیمتی روغن، برنج و حبوبات
کنگری، رئیس اتحادیه بنکداران مواد غذایی تهران در
#گفتگو
با خبرفوری:
🔹
روغن در فروردین ماه، ۱۶ درصد و الان ۱۵ درصد افزایش قیمت داشته است. قیمت روغن ۸۱۰ گرمی در بورس کالا ۳۲۷ هزارتومان می‌باشد اما در شبکه‌ تنظیم بازار این محصول ۲۸۱،۹۵۰ تومان به دست مصرف‌کننده می‌رسد.
🔹
سایر کالاها مانند حبوبات و برنج روند کاهشی در بازار داشته‌ است.
🔹
روند عرضه و تقاضا به طوری هست که انگار در شرایط جنگی نیستیم. زنجیره تامین در کنار زنجیره توزیع قرار گرفته و روند عادی را طی می‌کند. تا این لحظه مشکلی در راستای مواد غذایی به خصوص کالاهای اساسی نداشتیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/akhbarefori/652190" target="_blank">📅 23:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652189">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
نخست‌وزیر انگلیس در نخستین جلسه مجلس عوام پس از بازگشایی پارلمان، بار دیگر ورود شتاب‌زده به جنگ علیه ایران را خلاف منافع کشورش دانست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/652189" target="_blank">📅 22:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652188">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Muq37frzlYQHtSFbjFA-u2dG8iPIu8KiHD6wTY6xplPZdlC64CdOjJgCopPU9GLuuoOkjaEAK9rxPZBLWMKHcrHQKsWEaWtU05CjDCJfBGyBhY_F5weoNOM66U3_CHuBCY9I0NIuZashMZFWkeAbBD6K-k9YIjQijStuPtsU7b7mXo4AGLx-C0SmuIsn3mwzNCiHC-90w2lnFJCnxdYFWQ2XvEPUSHr4zyW0Uf8Pj3rxhWcHTUAm8V4if_UmJi0kb1wBoLNwQz-Ywe7jcofjUPrTWlf7kxQ28sQ4jEj4eh6lgvJj_h2Xz9K2IlepdkQlp1gwM8XUtsifDon28J6gEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رأی ۵۰ در برابر ۴۹؛ سه سناتور جمهوری‌خواه مخالف جنگ با ایران شدند!
هیل:
🔹
سه سناتور جمهوری‌خواه از رهبری خود جدا شدند و به پیشبرد قطعنامه‌ای برای توقف درگیری با ایران رأی دادند.
🔹
سناتور لیزا مورکوفسکی، سوزان کالینز و رند پال و تقریباً تمام دموکرات‌های سنا در رأی‌گیری برای پیشبرد قطعنامه‌ای که به ترامپ دستور می‌دهد نیروهای مسلح را از خصومت‌ها علیه ایران خارج کند، پیوستند.
🔹
پیشنهاد لغو قطعنامه از کمیته روابط خارجی سنا همچنان با رأی ۴۹ در برابر ۵۰ شکست خورد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/652188" target="_blank">📅 22:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652187">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نیویورک تایمز به نقل از مقامات آمریکایی: شرکت‌های چینی در حال مذاکره با ایران در خصوص فروش تسلیحات هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/akhbarefori/652187" target="_blank">📅 22:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652186">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
«ناوگان جهانی صمود» فردا (پنجشنبه) از شهر مرمریس ترکیه در ساحل مدیترانه، در تلاشی دوباره برای شکستن محاصره تحمیلی رژیم اسرائیل بر نوار غزه با مشارکت ۵۴ کشتی، حرکت خود را آغاز می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/652186" target="_blank">📅 22:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652185">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fc80f2a9d.mp4?token=uk61O8B_lRNT323cNJt0WdEtYDDg3WqSsxyxdz09oALKYY3L-mH9saNkTkh4Brtt9rrvWivk-9XvCV2_YjwtwzNX-My6rDE08ywfC-E0Ehw-ydQ-xkG9CzOY_hF_LJSLOyB4DO7oFfVt3prkACCRNjT7evIze0M76Ub99dNHqeVQIr59vbC1x0t2wIOa5q5Kl6keT-l7YBODGrEOnE0pgWcQmFMRJDMMx16RjbIHFaPX58XATMTPn16NK7B7WBmZWsIkyCPN-TLgmKrbkigd1V-qDDhNtDoRbLjQWxD7hN63S_zHwZkGArBvUTpxoD3oq3ow2TzGnT2IAs5E3q6DbEgh2upbf1l57GRu0bPTX6OqRpfN5WKy-VK18-5C45m-jmOXkxY4wJTYamOXjPHmnsTFl6YA1WoV2a1iS5TIB9HSlRvx1LpstM8A7ZrgBPC__y2OcPN1Fd9I1ut8Z1ru3-9lvyuPN3bTOZvHfTg6TPKXINqq5H_IcYF92iEqudHe-yjvFGzJu2QGmRFQqnUaRhspfA2N5ZQ7-rmRLArVqaeSST6fZxcz-Nw52hYr5wTSrikD9sQPCAdjclfxS1IEXEN2jJ5eYKKg26DfcVO40h6kP8JR7njVPV84y992owqg6GeeUmRpS75pDtG2tWo6-BiJE1oGrnqFRQ-fBS_EnwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fc80f2a9d.mp4?token=uk61O8B_lRNT323cNJt0WdEtYDDg3WqSsxyxdz09oALKYY3L-mH9saNkTkh4Brtt9rrvWivk-9XvCV2_YjwtwzNX-My6rDE08ywfC-E0Ehw-ydQ-xkG9CzOY_hF_LJSLOyB4DO7oFfVt3prkACCRNjT7evIze0M76Ub99dNHqeVQIr59vbC1x0t2wIOa5q5Kl6keT-l7YBODGrEOnE0pgWcQmFMRJDMMx16RjbIHFaPX58XATMTPn16NK7B7WBmZWsIkyCPN-TLgmKrbkigd1V-qDDhNtDoRbLjQWxD7hN63S_zHwZkGArBvUTpxoD3oq3ow2TzGnT2IAs5E3q6DbEgh2upbf1l57GRu0bPTX6OqRpfN5WKy-VK18-5C45m-jmOXkxY4wJTYamOXjPHmnsTFl6YA1WoV2a1iS5TIB9HSlRvx1LpstM8A7ZrgBPC__y2OcPN1Fd9I1ut8Z1ru3-9lvyuPN3bTOZvHfTg6TPKXINqq5H_IcYF92iEqudHe-yjvFGzJu2QGmRFQqnUaRhspfA2N5ZQ7-rmRLArVqaeSST6fZxcz-Nw52hYr5wTSrikD9sQPCAdjclfxS1IEXEN2jJ5eYKKg26DfcVO40h6kP8JR7njVPV84y992owqg6GeeUmRpS75pDtG2tWo6-BiJE1oGrnqFRQ-fBS_EnwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین پاک، کارشناس جبهه مقاومت: امکان ندارد ایران به خاطر واسطه شدن چینی‌ها از شروطش کوتاه بیاید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/652185" target="_blank">📅 22:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652184">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وزیر خارجه کوبا: حمله آمریکا منجر به حمام خون خواهد شد
🔹
شهروندان کوبایی و آمریکایی کشته خواهند شد و تنها سیاستمدارانی که فرزندان و خانواده‌های خود را به جنگ نمی‌فرستند، جرات اجرای چنین سناریویی را دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/akhbarefori/652184" target="_blank">📅 22:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652183">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حکم قصاص قاتل شهید دهقانی اجرا شد
🔹
سرهنگ دوم شاهین دهقانی دی‌ماه به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/akhbarefori/652183" target="_blank">📅 22:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652182">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FApJDKowJpH9q0Tmco8nlq1qKYfVTU9iN2PzN7UnwgU3gX6gHRtuRE6CjAbQiGuHrfLJHEkCvKgBX6_y8-HqPNVKDjwEQv2F_4zetRmQBVj-4kL-KSfKMaE5cGLCBWOA2IDuwu-febYGEZ8rKtL2oIptV1xtBrhpJDeaSt2HghxEiqUlS8cjOIIFWTHch-o2pnRcJWy413_-fAlgE-jD5WwaZd4ZsJ9pBmNJy6LkVOA7Zpp1nbt2BM3vJdgxA8ByFHgIoF9dp9WoBUObuK6P7V0Se3V8_8aRl0jyetVjXMcd13jja0Zch4zotzth4ioPPcBw23IDZFtisJiCaMLqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یمن: عواقب جنگ علیه ایران دامن تمام دنیا را خواهد گرفت
🔹
معاون وزیر خارجه یمن تصریح کرد حمله خصمانه علیه ایران، امنیت و ثبات منطقه و جهان را تحت الشعاع قرار داده و تداوم آن، منطقه و جهان را به جنگی خواهد کشاند که پیامدهای آن گریبانگیر همه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/akhbarefori/652182" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652181">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6670d6dcb3.mp4?token=NHhhe0mi3P_zckoq2OqhyRBr7lmpzyfPffgQJdhx4lqX8Zdz7yNFHVemsjCCefa3Trt-GBEX3ReEGHMbQMDKlyXV9Qh53LQwt3lGliOenHOz611kIrsGK7fnAYx27Wek5QhSu6PfBdE8Y9k94NW4HkYmRaNUZ98HetVOkG_D6DmbvsGYJ2aLzCT03QaEOwwOMip0IaRwxBjQV82mbbXXWpSN8TgtGkCZDczi7ruXgSUchkq7KYkC8ZgGauK8pBew4ATqBAqBqr56NdCBnBIt5B5KWgVasMpLH4yqNT5Ifqfs4r3TH68eBQynppcu9lXUGgOCLcfQw0SGXyW3uCZqcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6670d6dcb3.mp4?token=NHhhe0mi3P_zckoq2OqhyRBr7lmpzyfPffgQJdhx4lqX8Zdz7yNFHVemsjCCefa3Trt-GBEX3ReEGHMbQMDKlyXV9Qh53LQwt3lGliOenHOz611kIrsGK7fnAYx27Wek5QhSu6PfBdE8Y9k94NW4HkYmRaNUZ98HetVOkG_D6DmbvsGYJ2aLzCT03QaEOwwOMip0IaRwxBjQV82mbbXXWpSN8TgtGkCZDczi7ruXgSUchkq7KYkC8ZgGauK8pBew4ATqBAqBqr56NdCBnBIt5B5KWgVasMpLH4yqNT5Ifqfs4r3TH68eBQynppcu9lXUGgOCLcfQw0SGXyW3uCZqcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های طوفانی مردم به توهم ترامپ!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/652181" target="_blank">📅 22:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652180">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084593e8e6.mp4?token=gy46WyZer1gwu8zbvj7wklzJJscFBZlZwPSiPVg7FH18IqP9Bu7o6uwT8Ew0c3B3Muxd-RjbjiYBzHLmKzTA0aVgV8vnv2M9w-KG_l6w9Tla8I9HdnOgi2Lha-xOwb_Hpa_x16E3V-fQQiuCTUFRKDf6g91b6Y31PBGMMwnoKX3-1Ezx6sIMiAkEbUuHShlEPSKDyg8jMzbFNumGuHE94h4og07A3kt84GG0O9w9VjR3hb2wUwD6KwZANc7Gwrod5lw3cUsKYvE6ggCRqPtPYs2Aaq0ChNnlRblK3wWKcCrwd7uLWcyw1QhvvyI2Xr_6qzfWoUinI72dUYVi2iftVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084593e8e6.mp4?token=gy46WyZer1gwu8zbvj7wklzJJscFBZlZwPSiPVg7FH18IqP9Bu7o6uwT8Ew0c3B3Muxd-RjbjiYBzHLmKzTA0aVgV8vnv2M9w-KG_l6w9Tla8I9HdnOgi2Lha-xOwb_Hpa_x16E3V-fQQiuCTUFRKDf6g91b6Y31PBGMMwnoKX3-1Ezx6sIMiAkEbUuHShlEPSKDyg8jMzbFNumGuHE94h4og07A3kt84GG0O9w9VjR3hb2wUwD6KwZANc7Gwrod5lw3cUsKYvE6ggCRqPtPYs2Aaq0ChNnlRblK3wWKcCrwd7uLWcyw1QhvvyI2Xr_6qzfWoUinI72dUYVi2iftVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
زیباترین پادشاه ایران در مقابل هیولایی مانند محمد خان قاجار ...
نسخه کامل را اینجا ببینید
👇
https://youtu.be/IpMt8R6uBX4?si=-7JMsyhn60BXSofd
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/652180" target="_blank">📅 22:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652179">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72a4aeebd.mp4?token=in8Iie36dp1BN0n3PY6oOlvbos5ubxFox4R_qPUCs7BaOuS0sWqtlPWdmQ3RRqNtXzCDijDqgmEfZtlN6NrL8ytNcxjoMAu4uxGAn8vwPnluM_xHXfkKxCOL4-Iz-TsAueYFrqDP-nkXfn5MxRlxjTgCpWlbBcmkTA1UkRT2KCjE997o2HI9bnUI54D0T4pw3hzle8D-jWqoMx4-MsF04d7vcuWIwXZhZWOI2uJYoMdCL_-NUCYnVhG_BdqeY0RbkaVuv8Y6PUYsbf2rcSZ1OOC4RV4XYWnqTY8Dms8OJ3Fc0La6lT72A3qXYZak7NoaheTAKlWExHmdGsZAlfvr84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72a4aeebd.mp4?token=in8Iie36dp1BN0n3PY6oOlvbos5ubxFox4R_qPUCs7BaOuS0sWqtlPWdmQ3RRqNtXzCDijDqgmEfZtlN6NrL8ytNcxjoMAu4uxGAn8vwPnluM_xHXfkKxCOL4-Iz-TsAueYFrqDP-nkXfn5MxRlxjTgCpWlbBcmkTA1UkRT2KCjE997o2HI9bnUI54D0T4pw3hzle8D-jWqoMx4-MsF04d7vcuWIwXZhZWOI2uJYoMdCL_-NUCYnVhG_BdqeY0RbkaVuv8Y6PUYsbf2rcSZ1OOC4RV4XYWnqTY8Dms8OJ3Fc0La6lT72A3qXYZak7NoaheTAKlWExHmdGsZAlfvr84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چی این چمدون رو سنگین کرده؟!
@TV_Fori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/652179" target="_blank">📅 22:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652178">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2AoVpbWvi60N0_O6NZ-f9r4bGF9zIDKOXOrFv0UUvUXr_zT1nFD9ph9SYLRu5AiAQWVsdyCbrW38MMGtOKVLqCQZChxarmWIbAACdSSPXMspB4VAjHhq_uXOlO40yFOUVUbHJ6h1Thg4A2V9r3qhMloirSABU3fhy1rpbV0jZv9xSNCZ-3b497lrgRyHRiDqz589LpyftJJ6mTLEyvL5DtBjQVAoIXskQAfqlWY5SDpqokqW9DnDX0nf4L7G1d1yIydHx-v7ZcEWO9EGJD-WqNPA7srK4Oj6E8vvVjl8dtWN5WwP6dr34ycgbf1Sy_GT2oleo_ab1Brg6CeUGrtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد عباسی، قاتل شهید سرهنگ دهقانی که در اغتشاشات ۱۷ دی ماه با ضربات متعدد سلاح سرد به شهادت رسید، قصاص شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/652178" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652177">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
رسانه هندی: آمریکا جنگید، چین برد
تایمز آو ایندیا:
🔹
در حالی که آمریکا موشک‌های خود را شلیک می‌کرد و اسرائیل زیرساخت‌های ایران را هدف گرفته بود، چین بی‌سروصدا درحال برنده شدن بود.
🔹
پکن بدون کوچکترین مداخله نظامی، با محکوم کردن حملات آمریکا و اسرائیل، دفاع از دیپلماسی و تثبیت روابط انرژی با کشورهای مردد در قبال واشنگتن، جایگاه خود را به عنوان یک جایگزین آرام و قابل اعتماد تثبیت کرد.
🔹
آمریکا سرمایه دیپلماتیک خود را سوزاند، چین بدون هیچ هزینه‌ای نفوذ خود را از خلیج فارس تا اقیانوس آرام گسترش داد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/652177" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652176">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D--FPf4f4baA4p7vVlFLo5A72Wg76-g2PxUJFnzIa14MIeuqbDrUaUMKPutESjjVuwYvtkloIkx5T1qyE5TyW6RUU9babKr3NmNafv5SK-e3aLvQ4NUANZnwEh9dcEFK4TfPBSXyoqXSR0m7gje_8NcHEQAIz4wNLILDTwnAsFlv53zLyRpviGGfQD2SFEwratJS8wJglZXosn965tan92gtWmwYef8rXoti0EOVhirqWxkhGN_IGsqmFNid8dt7lgF9y27xg-FORVteeXuc1-hOAMPS-0nA0f484ViR9MtyKwXCcXFnyMvgBrlbwZi8sf8iZ-Qx-QBcUzKYq4F9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ارتش: کنترل بر تنگه هرمز، دو برابر درآمدهای نفتی برای ما آورده اقتصادی خواهد داشت
🔹
امیر سرتیپ محمد اکرمی‌نیا: نظارت ما بر تنگه هرمز، هم درآمدهای سرشار اقتصادی به میزان حتی دو برابر درآمدهای نفتی برای کشورمان به همراه خواهد داشت و هم قدرت ما را در بعد سیاست خارجی تقویت می‌کند.
🔹
پس از پایان این جنگ، دیگر جایی برای عقب‌نشینی وجود نخواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/652176" target="_blank">📅 22:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652175">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مراسم دعای ندبه_جلسه 48</div>
  <div class="tg-doc-extra">سخنرانی استاد رائفی پور</div>
</div>
<a href="https://t.me/akhbarefori/652175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌وهشتم
رائفی‌پور:
🔹
0:15:30 عاملی که آدمیت را از حیوان مجزا می کند
🔹
0:22:00 دنیا برای مؤمن مانند قفس است
🔹
0:26:15 عاقبت جامعه‌ای که در آن امربه‌معروف و نهی‌ازمنکر نباشد
🔹
0:41:00 معنای اصلی کشتی نجات بودن امام حسین(ع) چیست
🔹
0:46:50 ارزشمندی اشک بر امام حسین(ع)
🔹
0:58:50 مخفی بودن قبر مطهر حضرت علی(ع) تا زمان امام صادق(ع)
🔹
01:13:00 حضور امام زمان(عج) در روضه حضرت عباس
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/akhbarefori/652175" target="_blank">📅 22:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652174">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
نشست مشترک مجمع نمایندگان استان تهران در مجلس شورای اسلامی با جانشین فرمانده سپاه پاسداران انقلاب اسلامی برگزار شد
🔹
در این نشست مسائل مربوط به استان تهران اعم از نحوه تامین انرژی، آسیب‌های ناشی از جنگ، نحوه خدمات رسانی به شهروندان، وضعیت امنیتی و سیاسی مورد بحث و بررسی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/akhbarefori/652174" target="_blank">📅 22:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWrbnscwo-FXBI1b-Zl1TDiZ7bKSUYP6ElTyofQoVR7Vc4n5oiJ4-odC_l6-xkZ1Jg9_HdMAvRwPd-wJJG4GQa5n94PlUzbMP94-pAaCePGUL_PPQdrZmFDjg137l9aAR9lbq4NZVURdfWDppTcsAhID0M4ULaDTOd6tmaq_HNilvNQqOpt4NCrhWSBku9JopbhzpxtmuKmScK1l4me2e857MUtb39cudTTgGQkL7360NQ7xvnYf_sUywoEdp7cTCHQdPsOICafuhfYRQtHLWhiArdEEEXYLeXoKBWcZ3PbeTYggIHkeRybYOT-OEoJ3GjtbG-z582jKiS83OJ2Y4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن افرز: آیا ترامپ می‌تواند به توافق هسته‌ای جدیدی با ایران دست یابد؟ آن هم وقتی واشینگتن مطالبات بیشتری دارد و تهران اهرم فشار بیشتری
🔹
دستیابی به توافقی بهتر از برجام به مراتب دشوارتر است؛ چرا که توانمندی‌های هسته‌ای ایران از زمان خروج آمریکا از توافق سال ۲۰۱۵ به‌شدت پیشرفت کرده است.
🔹
ایران در سال‌های اخیر دانش فنی در تولید سانتریفیوژهایی کسب کرده که شش برابر کارآمدتر از مدل‌های سال ۲۰۱۵ هستند و سرعت نصب آنها نیز سه برابر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/652173" target="_blank">📅 22:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652172">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آرایش جنگی در کشور و کلیت جامعه در قبال جنگ جدید دشمن ایجاد نشده است
🔹
مهمترین گزاره های تحلیلی اقتصاددان فرهیخته دکتر خوش چهره در دومین نشست «مقابله با جنگ اقتصادی» در ستاد رسانه کشور:
🔹
درک درستی از تهدیدات وجود ندارد و بعضا شاهد ساده انگاری هستیم.
🔹
نابرابری میان تهدیدات و مدیریت تهدیدات در کشور وجود دارد.
🔹
قرارگاه جنگ اقتصادی با افراد امین، علیم و دلسوز می بایست تشکیل شود.
🔹
در درجه نخست نیازمند اقدامات آنی و کوتاه مدت برای کم اثرسازی برنامه تورمی دشمن هستیم.
🔹
مقابله با لیدرهای تورم، ضرورتی اجتناب ناپذیر است.
🔹
در تاریخ جنگهای جهان، دولتهای موفق در شرایط جنگی بیشترین سطح  مداخلات را در بازارها داشته اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/akhbarefori/652172" target="_blank">📅 21:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652171">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03968759d.mp4?token=pczm-X7zgr6qlXeLWuD7v5CEpqpwEQKcy4_9L2w-gf6ZWtDT2W-P2DPASgBBoqIjXzkPZ8uj4uZM-VKQt1idoIuJbbkDt50u692ESD_njQO7EZWlL--yB2KELJlGMzRClNp5phdwjv9q-k0SgWvKPo2lUVijmg1AIpu2QXsbgV3IPk8DzjfJFlGpQvh3PfEM4t3yPlWXnFA_yRCXe4pLB0Hmmf6_3CjHU5MxRQodxCyMW9-sfxzpRkTxwESJFALSEqFMTs_FaFDuuoI0T0bV5jZ40lekkdJakCqAZs3yLH7CjOgH80BzIcDn-bm5WnbinOXRT4nnFONJCnP1M0Sstg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03968759d.mp4?token=pczm-X7zgr6qlXeLWuD7v5CEpqpwEQKcy4_9L2w-gf6ZWtDT2W-P2DPASgBBoqIjXzkPZ8uj4uZM-VKQt1idoIuJbbkDt50u692ESD_njQO7EZWlL--yB2KELJlGMzRClNp5phdwjv9q-k0SgWvKPo2lUVijmg1AIpu2QXsbgV3IPk8DzjfJFlGpQvh3PfEM4t3yPlWXnFA_yRCXe4pLB0Hmmf6_3CjHU5MxRQodxCyMW9-sfxzpRkTxwESJFALSEqFMTs_FaFDuuoI0T0bV5jZ40lekkdJakCqAZs3yLH7CjOgH80BzIcDn-bm5WnbinOXRT4nnFONJCnP1M0Sstg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام رسمی خسارت‌های آمریکا در جنگ
🔹
اعدادی که امروز در رسانه‌ها خبرساز شدند.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/652171" target="_blank">📅 21:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652170">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a758a0344c.mp4?token=hpO06GTrlX3wQ4Cfqgwo9dxfJTuIVjz0q3UOheksumJ3gS7dNnmOqZij5j2TEDgkNNShpB0--zhaPRlRneBbeofILUvG9LY1SZVV64nEYPAHq60-NwEBXBX4zZ90nhSXjpcUg42vNZ7vahcixolMjg-qeLhBmpwYmWwuf8WZ0nbwo4-uNm0TCE4C2zP7-B4j3R-t8lxZIXcWTkjhMUjAlrkLn_FuZs8TY-vcTtLvt7k0IBPC3Uv62WcKMuW0RwQoxoVMHhqv5Th1WzM6lUgd_-fDgBsuHQ7OBVLH44tzY_uRsna95hRMKyf5QSuTk5G-zVOjxi-2DvsVXIP7m0VCG3uyb6FduByUeVIcur0T7NDheCMQ9NiBoUi1PIn_CKTgdQCc7GauXnCWqGmY12k_jbBQYQ6qM95Luj7m0SuCplRwUR_Xo4NZVSyo0iZCWvz1DDTOePiJWnVUPLSzZcnDlkvzgdOjoVZwtiJqVEjTVDzY5i_XztDrkA1qy8-QYjEyttn2FBCeOxsCqnoVPe-oh2NzDKWTY1PDYnBlOWrZwAnaolMsC_eU2cFqsK872Vn5UGVliUrACzlsrlKOC2tCdBnkpoFizcEcUZr9ULv09kZV4fnwBEzOM7pDW2JiAbiJjtQCp1J2Uk4iLiLyavCi7fxS8rmBQqhgsVdrQzYIZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a758a0344c.mp4?token=hpO06GTrlX3wQ4Cfqgwo9dxfJTuIVjz0q3UOheksumJ3gS7dNnmOqZij5j2TEDgkNNShpB0--zhaPRlRneBbeofILUvG9LY1SZVV64nEYPAHq60-NwEBXBX4zZ90nhSXjpcUg42vNZ7vahcixolMjg-qeLhBmpwYmWwuf8WZ0nbwo4-uNm0TCE4C2zP7-B4j3R-t8lxZIXcWTkjhMUjAlrkLn_FuZs8TY-vcTtLvt7k0IBPC3Uv62WcKMuW0RwQoxoVMHhqv5Th1WzM6lUgd_-fDgBsuHQ7OBVLH44tzY_uRsna95hRMKyf5QSuTk5G-zVOjxi-2DvsVXIP7m0VCG3uyb6FduByUeVIcur0T7NDheCMQ9NiBoUi1PIn_CKTgdQCc7GauXnCWqGmY12k_jbBQYQ6qM95Luj7m0SuCplRwUR_Xo4NZVSyo0iZCWvz1DDTOePiJWnVUPLSzZcnDlkvzgdOjoVZwtiJqVEjTVDzY5i_XztDrkA1qy8-QYjEyttn2FBCeOxsCqnoVPe-oh2NzDKWTY1PDYnBlOWrZwAnaolMsC_eU2cFqsK872Vn5UGVliUrACzlsrlKOC2tCdBnkpoFizcEcUZr9ULv09kZV4fnwBEzOM7pDW2JiAbiJjtQCp1J2Uk4iLiLyavCi7fxS8rmBQqhgsVdrQzYIZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مثلث مرگ!
🔹
داستان واقعی نبرد ۴۸ ساعته سه سرباز ایرانی در مقابل ارتش دشمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/akhbarefori/652170" target="_blank">📅 21:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652169">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل به نقل از یک منبع نظامی گزارش داد: حزب‌الله از ابتدای جنگ ۴۵۰ پهپاد پرتاب کرده است که شامل ۱۲۰ پهپادی است که با استفاده از فیبر نوری عمل می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/652169" target="_blank">📅 21:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652168">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رویترز: عربستان و کویت در میانه جنگ ایران، حملاتی به عراق انجام دادند و پایگاه برخی گروه‌های عراقی را بمباران کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/652168" target="_blank">📅 21:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652167">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA9d6xL-9RryguqokAX5s1FKwo5P-zRUjoarhei4MlwmHboq57lT0_K5ViXnTNdQT07W_JzQk3zOiPlK1YgT5b0El9eV_TaVlIt16aSWvCbVNd35fMqhR3St7LnMH1feftjXkBX2ynEj5PXwIsTZk6sTqg-2Wo9PSsIOhB-cD6u1Ht8DVF0cFrgFekgTXECVrlfpuHKGJpQQ97RWkBB5c2f7ZUV2FmnmPXfVuBPF2OuxrADH10Oh9KDVJFvOlsproqHAO3n7lbLNPOoqJZ1fFrAz3rL8ZbGzKiXG94K4a4ctnBdx7ztypRfze6eGKc3Q-TCgHYp-coKuSLETKRGf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: اطلاعات آمریکا نشان می‌دهد که ایران توانمندی‌های موشکی خود را به‌شکل قابل توجهی حفظ کرده است
🔹
تصویر ارائه‌شده دولت ترامپ از یک ارتش درهم‌شکسته، با آنچه آژانس‌های اطلاعاتی آمریکا در پشت درهای بسته به سیاست‌گذاران می‌گویند، تفاوت فاحشی دارد.
🔹
ارزیابی‌های جدید و محرمانه حاکی از آن است که ایران به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز دسترسی عملیاتی دارد.
🔹
نگران‌کننده‌ترین بخش برای مقامات ارشد، شواهدی است که نشان می‌دهد ایران دسترسی عملیاتی به ۹۰ درصد از ۳۰ سایت موشکی در تنگه هرمز را بازگردانده؛ امری که ناوهای جنگی و نفتکش‌های آمریکایی را در این آبراه باریک تهدید می‌کند.
🔹
به‌علاوه، ایران همچنان حدود ۷۰ درصد از لانچرهای متحرک و ذخایر موشکیِ پیش از جنگ خود را در اختیار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/652167" target="_blank">📅 21:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652166">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdVI-BnZpWjsRVd86PqXcoIeC8YlYwz8ekFDv_8D8GcfbuDHL9RVaLWK2jYufzm2QlAEpKLjl7qHwRCJggtevVhxCHa4-w3frG3zpjdIQ4KilwAFx_7vgYYin0YhfB7JyAuyzu7iUAg6nvI5U3qkRhmWSD5GZ9677035hyKv9mVICGCf4yGj-74yJIHE6jwaivPl3O3cu0tAWvwTPx3SMHj_7SBzKojiW_drI_tVkQrM0h18Q4adN_ImsHiFsx7AQu2pGjWIIvzPwcRgpJczdqklXx-zHTdLmdx9p_IPERhRQS8XUH0QMdWZlY7XQuZasy9B6iHc1JoTlL_IhRvh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: ایران ۶۰ درصد از توانایی موشکی خود را دارد
ایندیپندنت:
🔹
دو ماه پس از بمباران مشترک آمریکا و اسرائیل، زرادخانه موشکی ایران عمدتاً دست نخورده است و هنوز قادر به حمله به متحدان آمریکا فراتر از کشورهای خلیج فارس است.
🔹
کاخ سفید بارها ادعا کرده است که ظرفیت نظامی ایران «تخریب» و از بین رفته است، اما منابع ناتو به ایندیپندنت گفته‌اند که این درست نیست.
🔹
یک منبع ارشد ناتو در اروپا: «هرچه که دیگران در ملاءعام می‌گویند، ما تخمین می‌زنیم که ایرانی‌ها حداقل ۶۰ درصد از توانایی موشکی خود را دارند. ورودی‌های آنها بسته شده است، اما آنها هنوز در زیرزمین هستند.»/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/akhbarefori/652166" target="_blank">📅 21:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652165">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac658f9344.mp4?token=h94_dGmyKRSXXuW3CpkkUnNwHNu0viY0eCKIPLyE6oAQHnFuCvueM8wB2-47DAh6imlibYpyYWZESoo-dIyYMfTAxeiDVFhZYSkCWyTrjt4bKkMLDZVq-wxk-9QaW9Ht9ToMYyK2OiAsW9Hu92TSrsRKoBO2DN2plgeMaTvVLHVLEi442omOgh6rzuq84BUnePiyy25yvGAMsIxOqcS3rNRvigYMcIfJby6G2XCwkj4I63wO2LsnB9T4YlUJGxgS2cEBXpFQaiWi6nXR-KAEaXlE7AwSIpMMKi01KWxiMWj9Q0op2mU-nOe3HuXqy7M662u5oMaC9fzhXqsgGbWexw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac658f9344.mp4?token=h94_dGmyKRSXXuW3CpkkUnNwHNu0viY0eCKIPLyE6oAQHnFuCvueM8wB2-47DAh6imlibYpyYWZESoo-dIyYMfTAxeiDVFhZYSkCWyTrjt4bKkMLDZVq-wxk-9QaW9Ht9ToMYyK2OiAsW9Hu92TSrsRKoBO2DN2plgeMaTvVLHVLEi442omOgh6rzuq84BUnePiyy25yvGAMsIxOqcS3rNRvigYMcIfJby6G2XCwkj4I63wO2LsnB9T4YlUJGxgS2cEBXpFQaiWi6nXR-KAEaXlE7AwSIpMMKi01KWxiMWj9Q0op2mU-nOe3HuXqy7M662u5oMaC9fzhXqsgGbWexw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه روغن میخوای، تن ماهی بخر!
🔹
فروش اجباری کالاها از کجا آب می‌خورد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/652165" target="_blank">📅 21:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652164">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfCeAPXHdNfMiCq_pHmeroG6nbR6BXphjucwdG_MapnmPIwhQRnmIzGdr5fEKopZSHmsXEbVKqKMgwp-qXCjtKkaVjWUwNE4B-h18WYGUAvmq22KNKBZmbreQMv1yy0nMqTQ6Q3tbW-LjGPOdWFyBs6fSPTdX-NO8_gNc6qTbZ50aM1AZSNHogORbyFINPz6b6dtL-eU27VXtBedNYXfvh021hVFxvJHrZf1XT28o7mBnl2NwRvnnuXluLePmRsb2cyGMLtPN6b8i4wPBYP1SlTARp9h6OvJ7SERH_rtN0NPXUVnR7QcLdveXIG9FFVKyHyYKE8ICxnUJccl8E1_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حداقل دستمزد در کشورهای اطراف ایران
🔹
مقایسه حداقل دستمزد ساعتی کشورهای همسایه در سال ۲۰۲۶ نشان می‌دهد ایران با حدود ۰.۴۸ دلار، تنها بالاتر از تاجیکستان قرار دارد.
🔹
در مقابل، حداقل دستمزد ساعتی در عربستان بیش از ۶ دلار ثبت شده؛ یعنی حدود ۱۲ برابر ایران. عمان با نزدیک ۵ دلار و ترکیه با بیش از ۳ دلار، در رتبه‌های بعدی قرار دارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/akhbarefori/652164" target="_blank">📅 21:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652163">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3FUh9XrFILx8WDJ_4XFr2GtssUG2TzKi_EOy6SxGF05zDpWs2Ysmc6HcFg99a0uxekc-WseyMRNsT5YkXdM6TVNmS-iJ8HkyYiFdZeqzJHyW0UZ9IH1B-PVkHnm3xM6CjGALtdQALVY5Qm3j_X6D190cDutDX-Qmch09kTTQVPfoCzwKRDc-Vw3FE7HwBwDEApTUVklQY-VEOi7Eo0Hzfruu45YIY655YRYhmYuUjzk4RJ5XV--5Ht7oEgd_YY7MdEKQDmKJwzm4L9ZbsgUHFIpxPJxwskWMl79uAJFMQP6XAj1iUp1kOcddhCT9U3Asc7Tu6rILt4Lsf2fDyo_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تابستان امسال، خانه‌ها بدون خاموشی/ کاهش ۵۰ درصدی قطعی برق کشاورزی و صنعت
🔹
رضایی کوچی، رئیس کمیسیون عمران مجلس در تشریح جزئیات نشست این کمیسیون با حضور نیکزاد نایب رئیس مجلس، وزیر نیرو و معاونان این وزارتخانه گفت: تاکید نمایندگان در این نشست اتخاذ سیاست‌های دقیق برای جلوگیری از قطعی آب و برق است.
🔹
بر اساس برنامه‌ریزی‌ها و توسعه نیروگاه‌های خورشیدی، مقرر شد در تابستان امسال قطعی برق خانگی نداشته باشیم.
🔹
همچنین قطعی برق چاه‌های کشاورزی و صنایع کشور حداکثر معادل پنجاه درصد سال گذشته خواهد بود؛ هرچند هدف‌گذاری ما رسیدن به قطعی صفر است تا امرار معاش کشاورزان و تولید صنایع دچار اختلال نشود.
🔹
در جریان جنگ، برخی از پست‌ها و شبکه‌های برق آسیب دیدند که با تلاش شبانه‌روزی کارشناسان در کوتاه‌ترین زمان ممکن بازسازی شدند، به گونه‌ای که مردم کمبود برق را احساس نکردند. اکنون نیز با رعایت اصول پدافند غیرعامل، شرایطی فراهم شده است که در صورت بروز آسیب مجدد، ترمیم‌ها بلافاصله انجام شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/akhbarefori/652163" target="_blank">📅 20:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652162">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سفر مخفیانه نتانیاهو به امارات در میانه جنگ ایران
🔹
شبکه ۱۳ تلویزیون رژیم صهیونیستی فاش کرد که بنیامین نتانیاهو نخست‌ وزیر این رژیم اخیراً با محمد بن زاید رئیس امارات دیدار کرده است.
🔹
این شبکه افزود که این دیدار در سایه احتمال ازسرگیری حملات علیه ایران و همچنین در پی حملات صورت‌ گرفته علیه امارات انجام شده و سه مقام ارشد اسرائیلی این خبر را تأیید کرده‌اند.
🔹
دفتر نتانیاهو نیز اعلام کرد که نخست ‌وزیر رژیم صهیونیستی در جریان جنگ علیه ایران، سفری محرمانه به امارات داشته و با محمد بن زاید دیدار کرده است.
🔹
در بیانیه دفتر نتانیاهو آمده است که این سفر به گشایش تاریخی در روابط میان رژیم صهیونیستی و امارات منجر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/652162" target="_blank">📅 20:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652161">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5GMLfDW5coi9lVn7si-uIKpiNwaMcTzDf0j6Wk23tYclnVTokK0U0bB159egIq13uwHdg-77wAU9_P-zHzXH3ocCO7UwqT7FNuWx04NhQKGTPZGmfeAPL232rhhmNJUhlqibHh7_IQpdh6xdMABuad41pw4AluCkchGdBPmMpm8ry6xX5MYhpuqcN8zB_GPcYIXJyYHgU96qRFzuR8K36j3xKy__wxHzePNrzFCKS0WDVInB1DQzqepl4AKyp8pC-2SlHUrAkvRohRmlvteT5CTHQzcguZj_e15YXdnW_mS5vBSohYVa7ewwr4Qmzoac6vgwTkLNom7cNw-Xb4J5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسقاط خودروهای فرسوده به ۱۱۵ هزار دستگاهی سقوط کرد
🔹
آمار شش ماهه نخست ۱۴۰۴ نشان می‌دهد تنها ۱۱۵ هزار دستگاه خودروی فرسوده اسقاط شده‌اند. این در حالیست که این رقم در مدت مشابه سال قبل ۱۲۱ هزار دستگاه بود.
🔹
طبق قانون برنامه هفتم، ایران باید تا پایان برنامه سالانه ۵۰۰ هزار خودروی فرسوده را از رده خارج کند، یعنی در نیمه اول سال، فقط ۲۳ درصد مسیر سالانه طی شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/akhbarefori/652161" target="_blank">📅 20:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652160">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjtgDxAy7c69aa6RNzWUYgq7iF-fiLASQPjTtIUvAL6iPF3I_O1YGcSVO4yv67NSx8jAwM00bBQ6VyBkhR0dNV4gG_ZX8Aw57-iT5iGBPRxwN3C9oAQwSDo-jyTRGfJPOLFiO3jWA8qOWQCjVJ9eRMiyTWL1nW99gVUTsGLPzMVqV0Pebu5cD7vo1ORmXQGIE3qacXaN5vlDhJa8H99hQ1UFn6of1RY57lS_mMoQFYwUVfKNLq0ojyYC2IjaAvbJ_lZG_eEGeusHeOPD1bFmdxcpDrFPItYS8vhbNQPI9uqamWb6JY-qfD_5hzO64jE-nshikxe3QzfFa1eLrUOufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم بدرقه ملی‌پوشان رونمایی شد؛
سرود رسمی تیم ملی فوتبال ایران با صدای پرواز همای
سرود رسمی تیم ملی فوتبال ایران  در جام جهانی ۲۰۲۶ با صدای پرواز همای، که به سفارش فدراسیون فوتبال جمهوری اسلامی ایران توسط مرکز هنری رسانه‌ای نهضت تولید شده است، امشب همزمان با مراسم بدرقه ملی‌پوشان فوتبال به رقابت‌های جام جهانی ۲۰۲۶، با حضور گسترده مردم، هواداران فوتبال، هنرمندان و چهره‌های ورزشی در میدان انقلاب تهران رونمایی شد.
این سرود با صدای پرواز همای برای نخستین‌بار در جمع مردم و ملی‌پوشان رونمایی و اجرا شد. همچنین لازم به ذکر است، شعر، آهنگسازی و تنظیم این اثر نیز توسط خواننده کشورمان پرواز همای انجام شده است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/652160" target="_blank">📅 20:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652159">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
مجلس سنا روز چهارشنبه برای هفتمین بار قطعنامه پیشنهادی برای توقف جنگ با ایران را مسدود کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/652159" target="_blank">📅 20:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652158">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a35ca03f.mp4?token=Gyj8BE7UOUJS91hfcra1VNTUNDyQ2ysiAQLQL7y-cssoLIoi3EBqmveDvjweiRUNsWmh3-du2Fjz-ljQoVsAH7H_I4ATmLg03XEKEexLw1KswhTgelK6GUBJY7MalomifRRmWn8od77nB7fEMyrDRep6syQmwAKEstcD-xwoVLPIdEvNd6Ls20Vz_r--6_IMULwGi8X4sm_Oc1oB35yzznWBzPjHTX4Q00VzI9Zkq_Hm51jbKQGaZ7AlLnjMlSdCpeC-12iuTixEHFiV_hpMt6N5oGCAXwh5ACyileSa6WqHT1snqGRNi6XnevM-kpgYA2flhWxBd47GEfDMgxMIBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a35ca03f.mp4?token=Gyj8BE7UOUJS91hfcra1VNTUNDyQ2ysiAQLQL7y-cssoLIoi3EBqmveDvjweiRUNsWmh3-du2Fjz-ljQoVsAH7H_I4ATmLg03XEKEexLw1KswhTgelK6GUBJY7MalomifRRmWn8od77nB7fEMyrDRep6syQmwAKEstcD-xwoVLPIdEvNd6Ls20Vz_r--6_IMULwGi8X4sm_Oc1oB35yzznWBzPjHTX4Q00VzI9Zkq_Hm51jbKQGaZ7AlLnjMlSdCpeC-12iuTixEHFiV_hpMt6N5oGCAXwh5ACyileSa6WqHT1snqGRNi6XnevM-kpgYA2flhWxBd47GEfDMgxMIBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش متفاوت یک کودک به سوال خبرنگار در محفل یادبود شهدای دانش آموز میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/652158" target="_blank">📅 20:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652157">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dea98ae1.mp4?token=MoAk0907aNZAy21wn8gxX0jRyF2eDfL_yQQ1RFG2N5o6BzDnd2c852-UVyc4DN6tjyF9dpQdFHfN5Lv5gDXj5Bm3PgVUC-tgl7yHKkvj78dXhq5iLdX4bmkKNjqCzodsoUlgq_Z3PYc3FWcVQRjedECrKm835TwfuLvPMYuEECEt14hvFVHkevdsO0HURQLyzdnCYAFkmYnP6PadLQX27KzROPqLHoE3gNK3-ts2BsILNClCTesRbGwAqBXEfcW2BuWLcmW4gHHKa8P6B_Rtati0HS7wUUT7nqso33efQQbq9rIEp4G-ggoLd9LPgQGftXDBU_c0vTcFB5ciniq1q7spxbntvDyN1sxz8SvPjxDA9XBX4ByvgmpNONr2M_lY4Y7Vfr0IuTQwh6pKtQiLswFg0rv5Ff6kmrySBYJEYkdNBeG0iCDpoMVFpbII8yy8eQf9Xb0jP0qllbHyxqp4RheciZnwTH5ynC4vKEod6m9q9UIK_74zr93Bh9NqD8CA3juywBSBYW0ULg1nydWru850aBvPvFut1QeF7aWvka2TGICoCHfaeYCM1IUhqyd8_x9zsgfvldYEuBCqiRaccTfWHaHZ_OHqNN-RVlWDCFwnSKGTZ9_fR5ljfyjVOTySXK1W-sWaTumkVJBt9ZgSIIH9Qojb3B1e2GK_J81FZa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dea98ae1.mp4?token=MoAk0907aNZAy21wn8gxX0jRyF2eDfL_yQQ1RFG2N5o6BzDnd2c852-UVyc4DN6tjyF9dpQdFHfN5Lv5gDXj5Bm3PgVUC-tgl7yHKkvj78dXhq5iLdX4bmkKNjqCzodsoUlgq_Z3PYc3FWcVQRjedECrKm835TwfuLvPMYuEECEt14hvFVHkevdsO0HURQLyzdnCYAFkmYnP6PadLQX27KzROPqLHoE3gNK3-ts2BsILNClCTesRbGwAqBXEfcW2BuWLcmW4gHHKa8P6B_Rtati0HS7wUUT7nqso33efQQbq9rIEp4G-ggoLd9LPgQGftXDBU_c0vTcFB5ciniq1q7spxbntvDyN1sxz8SvPjxDA9XBX4ByvgmpNONr2M_lY4Y7Vfr0IuTQwh6pKtQiLswFg0rv5Ff6kmrySBYJEYkdNBeG0iCDpoMVFpbII8yy8eQf9Xb0jP0qllbHyxqp4RheciZnwTH5ynC4vKEod6m9q9UIK_74zr93Bh9NqD8CA3juywBSBYW0ULg1nydWru850aBvPvFut1QeF7aWvka2TGICoCHfaeYCM1IUhqyd8_x9zsgfvldYEuBCqiRaccTfWHaHZ_OHqNN-RVlWDCFwnSKGTZ9_fR5ljfyjVOTySXK1W-sWaTumkVJBt9ZgSIIH9Qojb3B1e2GK_J81FZa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم نوشت| ریزپرنده‌های دشمن در این جنگ چگونه از کار انداخته شدند؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/akhbarefori/652157" target="_blank">📅 20:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652156">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123da29c75.mp4?token=RcHhgcdIeeYuvfGOj5OdMLW9rXoFQxDHEqxWCAaBcM7K0k-iL4LIHXGRu3gkHmOt1NYSGrNhPE4TEcQWyGaygVbLLngS2uRcvg0YUmryHGDQI04nyDPZbLh3U4n4bcO8A9_OplhzucTi54eboBUXgWs4NfdgJJyDK1c3kjqn9Wf-YsizZ-NULzdO5oBIj25zQjCDKOdOTjJxTcKNVfjpno0prKMa3R93K530_hzZb6flRXNz3A-eohTjax6dYwLbK7js4PdkYOcdeAGjtpzCxhJlVIny9oajsNj5efX35VbsVXCQ6tWpjw6qAvVwbPRLoM9g-0aAu5EzIXBVGgVysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123da29c75.mp4?token=RcHhgcdIeeYuvfGOj5OdMLW9rXoFQxDHEqxWCAaBcM7K0k-iL4LIHXGRu3gkHmOt1NYSGrNhPE4TEcQWyGaygVbLLngS2uRcvg0YUmryHGDQI04nyDPZbLh3U4n4bcO8A9_OplhzucTi54eboBUXgWs4NfdgJJyDK1c3kjqn9Wf-YsizZ-NULzdO5oBIj25zQjCDKOdOTjJxTcKNVfjpno0prKMa3R93K530_hzZb6flRXNz3A-eohTjax6dYwLbK7js4PdkYOcdeAGjtpzCxhJlVIny9oajsNj5efX35VbsVXCQ6tWpjw6qAvVwbPRLoM9g-0aAu5EzIXBVGgVysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهای خوش هفته‌ای که گذشت
🔹
در لابه‌لای خبرهای مهم و پر استرس این روزها، این چند خبر حالمان را خوب کرد!
@TV_Fori</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/akhbarefori/652156" target="_blank">📅 20:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652155">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxiZjqsScw1YmDPAP_cT3q_yWzI3k6L3tHzUyA883ycZH5U4yrpMkbFlgy9_nkdSnY8Iq4wPMP6cVQ_RQIZQQz2Bmj8yuIyjSzs9HjG7h6zB8zEh_aOMEmp64J_QSeqgI6L9EoBHaDy8no0Oe7ypAxxxdo3i5ld3314ERN3PC_pT8DeJONAlHKNv1VTcfrLbAr6FBSfW7V5JlN-BpRgrO4tBB_3x19Jf8odhC2jEJF0-h8Qxj7spWJTbjG1fehC_inAICOMHW3uqRLL8PfcjrOXrdRq3SMXDKrv11jCoyH4bvppG6F_XDDiUgfFbmIp1Jnc6S37MoQfKuDruHsa0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسیجی جهادگر «محمدامین صابرکار» در بندر دیّر به شهادت رسید
🔹
بسیجی جهادگر محمدامین صابرکار در جریان آموزش‌های دفاعی در بخش بردخون شهرستان دیّر به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/652155" target="_blank">📅 20:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652153">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2eQNHBJBaPUbw5vYO8x4b-j32QG0_u0RxxVpOlODo9e7Kk6jlHg4V67BjWjaIALsyG3M08H7V90bpv-Yx0YCFNCXRpZPPGrl5uAS65C7suHnbGbWtx0B3XX0VGuMa0-C90bK7PWu93fpJd8yZatIDERZJqubmV7NXi_p-LQnJVAVirJP3syrOvUWCwgUKVQgnEnSlk0Ytr3Pw5K3Aantm2jbhC9JM09LTbLzTg1UInW0vJTMw-lx-ZbB02HaCqv26sleQlLxwt5pHfGmfJdTUiqHAB1McogDl70zj5bk8VT3oTTPLOOnn3-n-M2-rxZQh_4S2qYFJk9vQXrbifW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراض وزیر خارجه ایران به دستگیری غیرقانونی اتباع ایران در کویت؛ حق پاسخ‌گویی را برای خود محفوظ می‌دانیم
🔹
در تلاشی آشکار برای ایجاد تفرقه و تنش، کویت به‌صورت غیرقانونی به یک شناور ایرانی در خلیج فارس حمله کرده و ۴ تن از اتباع ما را بازداشت کرده است. این اقدام غیرقانونی در نزدیکی جزیره‌ای رخ داده که ایالات متحده از آن برای حمله به ایران استفاده می‌کرد.
🔹
ما خواستار آزادی فوری اتباع خود هستیم و حق پاسخ‌گویی را برای خود محفوظ می‌دانیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/652153" target="_blank">📅 20:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652152">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggMObWheAnKJdYquAv8K_8oBixmBmgZlfMdBpUvgsDlW7OyhqbcYZGKcDxRUtYOcPnrjqKKnNnOIGbDD1SDbH3O1FxIWqlHWY4dESdwTABFzEscXbtnGTtG2s6gcLeuaA6uCkGG3HWvvwJi5RofRDYF7mU8GmtMQygkVjPwHvqmehQm47-BGkOS0chcp4ZT0qkYOuWIVPWD4INP3xzlVeFNFA6Vjj-0TkM3Rdh2N3S4sutTfDoBHsKqcomQpCVY53q3yPGnN7mUEauLu_NPaauVN_HFOYZ-ZXC0_t9utURJdSrQC8Iyd9gHjD0Q-jN-7MRNnpLP3Wne_WLrXiABEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان استخدام فعالین رسانه‌ای، اقتصادی، سیاسی و فعالین صنفی دانشجویی در ۴ استان
مجموعه خبرفوری بدینوسیله از تمامی فعالین رسانه‌ای استان‌های گلستان، گیلان، خوزستان و اصفهان جهت همکاری دعوت به عمل می‌آورد.
اطلاعات علاقه‌مندانی که سابقه فعالیت رسانه‌ای، سیاسی، اقتصادی یا فعالیت صنفی دانشجویی داشته باشند و در فرم ذیل اطلاعات خود را بارگذاری کنند، توسط واحد نیروی انسانی خبرفوری بررسی می‌شود و برگزیدگان به مصاحبه دعوت خواهند شد.
برای پر کردن فرم کلیک کنید</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/akhbarefori/652152" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652151">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ed274467.mp4?token=M7JWCswnfi6n0NMTVgl0gMUGIx7_JFIcZ7T_z2Ryehk8Hbf69oNHVFFOMqWNKTCSud_STs0n1voBW5SEfwIrboQyf5scpsTr955PzAbTtlyI1EIza5UWM_pSxpQnsNDUzmQyc7sEUDZ483Aa0Wnt0sZLoQu9SA9hR1GB96vYgJvl5wysYYGe8WSRGxOBhjInDUuN225ZWYA7YWxvBuk3vTk72aYqVgvbdj4eKCj0S-tG14UWxiJli7mn81hfKc9xE01tb_JwkonYGNR-WAlNXpVA9CAEABZT3huYgn8EQBdUm6Niq2UDdWWyGEEc71JVW-9h_2TPz2r5GU1gWjZDyklw_Q77mcGkIsxINRVbo7TV3Hlnj1yl7WDR1EjO12kSDaifJe5UfkJVVsAd5Hzpsn6d7ZRUY7swVayjXeaPEJkhVyEdwVCocL-_Zjf4Ha8Kag8nrjWP2-L_DCLVmghGaXlwB8kGEs0KoYCI7FNNo-r1yAvGbWgZduRdMOjpiYJMk5XUG1AmLsc2gsBXGEiMHhr2Orp9kVSGvxgO0VDYE9mFMHS2LwPqkol1f8Kw49mURvUo3X4y1fQNgyE0Ff-HHU-f6sRSLFx3PfSdMxjRdzutW49Ls76j9XZNwzSRuAk1d7VDvtdHtLHHyOj53CrXAlrniPwEtUN0CrtvCzLY8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ed274467.mp4?token=M7JWCswnfi6n0NMTVgl0gMUGIx7_JFIcZ7T_z2Ryehk8Hbf69oNHVFFOMqWNKTCSud_STs0n1voBW5SEfwIrboQyf5scpsTr955PzAbTtlyI1EIza5UWM_pSxpQnsNDUzmQyc7sEUDZ483Aa0Wnt0sZLoQu9SA9hR1GB96vYgJvl5wysYYGe8WSRGxOBhjInDUuN225ZWYA7YWxvBuk3vTk72aYqVgvbdj4eKCj0S-tG14UWxiJli7mn81hfKc9xE01tb_JwkonYGNR-WAlNXpVA9CAEABZT3huYgn8EQBdUm6Niq2UDdWWyGEEc71JVW-9h_2TPz2r5GU1gWjZDyklw_Q77mcGkIsxINRVbo7TV3Hlnj1yl7WDR1EjO12kSDaifJe5UfkJVVsAd5Hzpsn6d7ZRUY7swVayjXeaPEJkhVyEdwVCocL-_Zjf4Ha8Kag8nrjWP2-L_DCLVmghGaXlwB8kGEs0KoYCI7FNNo-r1yAvGbWgZduRdMOjpiYJMk5XUG1AmLsc2gsBXGEiMHhr2Orp9kVSGvxgO0VDYE9mFMHS2LwPqkol1f8Kw49mURvUo3X4y1fQNgyE0Ff-HHU-f6sRSLFx3PfSdMxjRdzutW49Ls76j9XZNwzSRuAk1d7VDvtdHtLHHyOj53CrXAlrniPwEtUN0CrtvCzLY8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده آمریکا و اسرائیل از یک موشک جدید با ۱۸۰ هزار ترکش برای حمله به یک سالن ورزشی دخترانه در لامرد فارس در ۹ اسفند ماه ۱۴۰۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/akhbarefori/652151" target="_blank">📅 19:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652150">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آشنا: تنگۀ هرمز دیگر رهاشدنی نیست و یک وضع واقع پیداکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/652150" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652149">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فروش فوری ویلا ساحلی در شمال ( مازندران )
💰
قیمت ۲۰میلیارد اقساطی
🏕️
ویلا مدرن لاکچری
🔥
فول هوشمند ، داخل شهرک
🔥
✅
متراژ زمین ۵۵۰متر
✅
متراژ بنا ۴۰۰ متر تریبلکس
✅
۵ خوابه (مستر)
✅
شهرک با گیت نگهبانی
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
💰
قیمت ۲۰ ميليارد اقساطی
⭐
اقساط بدون بهره
⭐
- تماس جهت بازدید :
برای قیمت و اطلاعات بیشتر و ارتباط با ما
وارد لینک زیر شوید
👇
👇
🆔
شناسه:
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/akhbarefori/652149" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652148">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSrEDOAjIMI8pb0LAxJdmF1vhOrwcF96YOSCmfx-No14c4KKZ_hh0FDUSNIBa158nRW_nGTd_hgcLcQfHc2MBwcC1IziX0kYoQWBSl5HzE-2H3RxQyB6fmksWKgP-BRqFhqTahCETfDB9k2bR8jwI9e_yakK-Ezhim7lcpOVooSNz_guXvtpaKnKe7YnKbZebvP-AkkjTJuFfRpwGso_UJtiGlrBIy5UtZayv2fdrmjk_Bn32b4e2ADv_Ez8-PG8OUgwD0o91dZu17z9ZARBEh1uDSxJQBAy1hjnvi9H4AYnQdPVi7ZTOgUwU7H9QYUcyzXYLTtweJ_Qo5nR17dWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتن لوینز، تحلیلگر و روزنامه‌نگار آمریکایی: امارات متحده عربی شروع به نصب تورهای فلزی مخصوص پهپاد در اطراف انبارهای نفت کرده است تا از حملات ایران محافظت کند
🔹
من نمی‌دانستم که پدافند هوایی آمریکا چقدر ضعیف (رقت انگیز) است...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/652148" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652147">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBu4nc-fovNhUd11FlRo444mxRyxR5saAwcOsjB9tauUpTKmHsQWMCSY6Kqe38bB-7kyptwxqMiMEtELQBGsgOpWuqRxTEUFpeB-V_ONejwLEPKMyjzAkakWw9YqA57SXCn9EbGz3973W0HAWTNHusZFWMNAPJLZp44S-vAwbNnuzImlF4pSD8wmmMxRwstldGiMnNd-ZodNnxrBHgsLZVu714WVk88D7XopZUiVCSSD-kxJzA9tZPv_zCF49LMiw5hso9VczmXn2vlDwFzl7OQ72oMkZ06iNa8b-p7aqPvCBifSox19LsRdHJ6gxPq1G6ewBEPYWtkjzvZJE23VCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو: تابستان خاموشی نخواهیم داشت
🔹
عباس علی‌آبادی وزیر نیرو: با همکاری مردم و افزایش ظرفیت تولید، وضعیت امسال از سال گذشته به مراتب بهتر خواهد بود و امید است تابستان بدون خاموشی سپری شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/652147" target="_blank">📅 19:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652146">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-kzTU_WIVwlDeKbqAAFuNSe5K8SRceGp8AXhLWLUkAAhNcXXfS6-pCMCNcL187iF7_v6ZCtkHXqpE5xlB6bRe2tiHu7dIIU_xB3DpR1tL9dkR2TPsknDz2vlX8McKkOrOADQYMjhthNxdhIUAV6ICxNUAQB_7R1jc3TFxRrfwxMckqdDjRfwNuhe1qpk57hFkOTHDnH-ZzxDqUVYUmfWF_T0NSLjnuaK7Oe61BUSvJaHj3fxn5uMaIuEequhZlZOeU3QVAbaZDl6Cb59KoaGqN_7sFeltYDax36X77g5NE-yCBcXH4trSWmSIdN895z1sv4ipO1sMxSCWUnlcDldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احسان تقدسی، روزنامه نگار: ایران همیشه بهشت صورت مسئله پاک کن ها بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/akhbarefori/652146" target="_blank">📅 18:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 در زمان انتشار اخبار مهم نظامی و درگیری‌ها، کدام شیوه اطلاع‌رسانی برای شما جذاب‌تر و قابل‌اعتمادتر است؟</h4>
<ul>
<li>✓ ترجیح می‌دهم اخبار را به صورت فوری و کوتاه (بدون تایید نهایی) دریافت کنم</li>
<li>✓ ترجیح می‌دهم کمی صبر کنم اما گزارش‌های جامع و تاییدشده را بخوانم</li>
<li>✓ بیشتر به دنبال تحلیل‌ها و چرایی اتفاقات هستم تا خود خبر خام</li>
<li>✓ فقط تیترهای اصلی را می‌خوانم و وارد جزئیات نمی‌شوم</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/652145" target="_blank">📅 18:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نزدیک ۴ هزار نفر به خاطر مهریه در زندان هستند
سید اسدالله جولایی، رییس هیئت امنای ستاد دیه کشور در
#گفتگو
با خبرفوری:
🔹
سال گذشته ۱۲ هزار و ۶۹۷ نفر زندانی را که رقم کل بدهی آنها ۴۷ همت بوده است از زندان آزاد کردیم که ۱۲ هزار و ۴۸ نفر از آنها آقا بودند.
🔹
هم اکنون در کل کشور ۲۰ هزار و ۳۶۵ زندانی غیرعمد داریم که از این زندانیان ۱۵۶ نفر بدهکار دیه، ۱۷ هزار و ۳۵۸ نفر محکومان مالی و ۳ هزار و ۸۵۱ نفر زندانیان ناشی از تعهدات مهریه و نفقه هستند.
🔹
مجموعه بدهی همه زندانیان غیرعمد موجود در کل کشور ۲۰۰ همت است.
@TV_Fori</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/akhbarefori/652144" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuQ35caBqywSC2K-mO-hWPJ4wK-gkZqAerqgYbP6y8hiLhBVK-UomxmaalvhE6AB6v1H0sx-z-bwK6O29MAr-nCjaxJxJwS_aBPDmFnJ4U-RgOAy2a0tW6Px-xZdFfP5TDPPKnihzS8DFRb6sbcOh6t6Dfaq_TzWDmPEk8vXMFqbSGMEDHbRcEZLDylqarQDuwX3zNgBjNcdWr_EGvOVIV2kvcqnYKZ4ZCsavxP-1RQMIxjWtE6lurBJ6pr6977KTf3mWPDvx2omMmvBjXz55CFcGreeheFNGwJsCs6Yr1BJFMsWg2lNr8E3MXm6_xHeJpLBr9XmN7BpTZTPsmOVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موجی از زباله، دریایی از درد
🔹
پلاستیک‌ها تجزیه نمی‌شوند، فقط خرد می‌شوند و وارد زنجیره غذایی ما می‌شوند. برای حفظ سلامت دریاها و خودمان، وقت آن است که جدی‌تر با پلاستیک خداحافظی کنیم.
شما هم به کمپین
#نه_به_پلاستیک
بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic
#نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/652143" target="_blank">📅 18:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652141">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
معاون ارتباطات دفتر رئیس‌جمهور: اینترنت بین‌الملل حتما وصل می‌شود
🔹
محدودیت‌ها ناشی از ملاحظات امنیتی دوران جنگ است.
🔹
دولت قصدی برای دائمی شدن محدودیت‌های اینترنت بین‌الملل ندارد.
🔹
محدودیت‌های ایجادشده ناشی از ملاحظات فنی، امنیتی و نظامی بوده است.
🔹
دسترسی به اینترنت همانند بسیاری از خدمات عمومی، حق طبیعی شهروندان است و دولت نیز قصد سلب این حق را ندارد، اما در شرایط خاص و اضطراری، مسئله امنیت کشور بر بسیاری از حوزه‌های دیگر تقدم پیدا می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/652141" target="_blank">📅 18:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652140">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZf-Y0Dbl5L-vPwhyrKuqlmenZjoOphdJ8fEl6uW8E0BoOOjLWFiBEQbCsRBHw5DvtOxLQfsDx1BbhZdRBVxJFSXPwJja5GBvet_BZ6UDxqV1FavDlzKXhJhT1YkcyrZOU9JlhhWInLB8HGK3l8RIK1DpPD4xU_c3bpjQhglvRqp2QvaD5FqIKe3oeHPmGUyKyxTb0UKpzdZLBKpAcvkiGmG5OWsHlZFSfAUHaSBLFAqpNwflZBiAxPklFNDziSzg92ravgvxGqUWfIPLc21580xP7vdYR85p68lixiFA3ukuWJ0fiC8lHKzGS8DMzsk5KSeb5LdyO7kFrrYCbE3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم خودروسازان از ارزش ریالی بازار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/652140" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2a897a4f.mp4?token=VKLSJmqidGqfxdGYBWQV6Shz8zm-iFwbZGqRoSzYvrtr06jnjNQ8LcKqc8C-5R08XbehTByKZuUoqXK56Yvo3vIj-b2y0NOL3kX3EHg240kb4axn-RpqW4QZlu0788y74jmjRp1ZhiON6SsSB7R5YX15Kk-nDnngmCS6a-DfArBvHkkEzYcNNmZjqiHv2ek0HR5DS29wLLlwcgHzJwtqzB6s2LXO0MNwDVAzSauLl5QBBhLBmSfrmHLwMRzvQTIPCLI4T4UzpXBQn_P2WnELb7NEfkAlB3YEXi06kqkaZGxCQqszldma6tpGsnyCC77NMNWPLAeJPAkEzXhqWjEufLp9eJqUL-o_dPNuLiBoNulyDXjz3aS6pfTRCmQHd3JTLlQSzI9WP7_1Ilj1xO95bgshaFStwogphm89zxz8MBNaw8WwH7lSmCSwhiqGoI9ENbaUkrLlAlD5x1QJ4I4_s-b6sSR0uYJxLAoYL0mgp90WsVKlzSV6c2b_9imyO8zMwZcPxP7eQI2fjOqMxqrUB73eLVC9C2FYQqcyd9EOkBNHxiugXaZFFzjRPnC4bp8BBOQeFbpxV4N39Zizrd-8_auJtIAkg6oUtQFIFK4Dwiq6dp3DjCzpDdnRMXe8zRn0y0cHUo_F93cX89P3GKVOaVBzq3DkZ5V7E90lI71i5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2a897a4f.mp4?token=VKLSJmqidGqfxdGYBWQV6Shz8zm-iFwbZGqRoSzYvrtr06jnjNQ8LcKqc8C-5R08XbehTByKZuUoqXK56Yvo3vIj-b2y0NOL3kX3EHg240kb4axn-RpqW4QZlu0788y74jmjRp1ZhiON6SsSB7R5YX15Kk-nDnngmCS6a-DfArBvHkkEzYcNNmZjqiHv2ek0HR5DS29wLLlwcgHzJwtqzB6s2LXO0MNwDVAzSauLl5QBBhLBmSfrmHLwMRzvQTIPCLI4T4UzpXBQn_P2WnELb7NEfkAlB3YEXi06kqkaZGxCQqszldma6tpGsnyCC77NMNWPLAeJPAkEzXhqWjEufLp9eJqUL-o_dPNuLiBoNulyDXjz3aS6pfTRCmQHd3JTLlQSzI9WP7_1Ilj1xO95bgshaFStwogphm89zxz8MBNaw8WwH7lSmCSwhiqGoI9ENbaUkrLlAlD5x1QJ4I4_s-b6sSR0uYJxLAoYL0mgp90WsVKlzSV6c2b_9imyO8zMwZcPxP7eQI2fjOqMxqrUB73eLVC9C2FYQqcyd9EOkBNHxiugXaZFFzjRPnC4bp8BBOQeFbpxV4N39Zizrd-8_auJtIAkg6oUtQFIFK4Dwiq6dp3DjCzpDdnRMXe8zRn0y0cHUo_F93cX89P3GKVOaVBzq3DkZ5V7E90lI71i5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: بانک مرکزی منابع مالی بازسازی واحدهای آسیب دیده در جنگ تحمیلی سوم را تامین می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/akhbarefori/652139" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ec3b0e04.mp4?token=EwPWvuh_eJNkQ8fgOBh3Gdr_zXV2pZcpAkPuAQEPbdE5HDAAqK0iRM_P6w8sy5oeXmohIp0MRhUvLnvDhR-5kmYYDwUxkZsq89F-hlVHzOANq_igM28KdIcWF4PxFwbwM3a21uf4FAyN7ibpGxkRzyOj-qA8O6GPoEKhocG-d2jczw51gbJYRcrdN6emgIW2sZNFR0ejy257hw_zEmIiy5D9_fa80hNW6Jopc2FdMHW5TWPo7u1NDEWmGg3itD9GS_wsoFR8pQA857sT1nvwNwPe_Jt_6kdsZL0sLaeXiP_tjBmjPspbsanrmmVGIJ3h-U4qhtwVQq0hWVY1tey3iDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ec3b0e04.mp4?token=EwPWvuh_eJNkQ8fgOBh3Gdr_zXV2pZcpAkPuAQEPbdE5HDAAqK0iRM_P6w8sy5oeXmohIp0MRhUvLnvDhR-5kmYYDwUxkZsq89F-hlVHzOANq_igM28KdIcWF4PxFwbwM3a21uf4FAyN7ibpGxkRzyOj-qA8O6GPoEKhocG-d2jczw51gbJYRcrdN6emgIW2sZNFR0ejy257hw_zEmIiy5D9_fa80hNW6Jopc2FdMHW5TWPo7u1NDEWmGg3itD9GS_wsoFR8pQA857sT1nvwNwPe_Jt_6kdsZL0sLaeXiP_tjBmjPspbsanrmmVGIJ3h-U4qhtwVQq0hWVY1tey3iDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین  انهدام بالگردهای دشمن توسط رزمندگان سپاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/akhbarefori/652138" target="_blank">📅 17:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652134">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o76XmQOPALwX11_fOooySlG0sT15jSfmm7J7hrukZtPo0QyYVJelFrn4Rvvmh62ez-QH5HFjNrcnY4LZV_Trxr6Y4M5oXbSCHndMDRtSSmt399Echg86vSJprU0Go7chHdkfEBQQu8kmzRcNubbU9qPW-cQpFYuEkzBhxDVjnuK0YcW02yI3tEhJYWk_YyEDSFGsMK0NuOlH1wP3BmQylZ6a2KBO-lac2t6enlzLa6bOtYRo2RnZ614m_Ez9pvvAbK8RCqUkAj1Cqxo2JpwQrz3WE2a5U8CmsRwvlNhlxISzm5d4j0r7JJAC3KvDzK0wpXGYs3C1722fj-be5N-jVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعوت از اعراب برای حضور در نشست ناتو با محوریت جنگ ایران
🔹
به گفته منابع آگاه، سازمان پیمان آتلانتیک شمالی (ناتو) قصد دارد از نمایندگان چهار کشور حوزه خلیج فارس برای حضور در نشست آنکارا دعوت کند، نشستی که احتمالاً جنگ ایران و شکاف فراآتلانتیک بر گفتگوهای آن سایه خواهد انداخت.
🔹
بر این اساس،‌ انتظار می‌رود وزرای خارجه کشورهای بحرین، کویت، قطر و امارات متحده عربی به نشست ۷ تا ۸ جولای (دو ماه دیگر) در پایتخت ترکیه دعوت شوند، اگرچه دفتر مطبوعاتی ناتو از اظهارنظر در این باره خودداری کرد.
🔹
این نشست در پی افزایش تنش‌های فراآتلانتیک بر سر جنگ ایران برگزار می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، متحدان ناتو را به دلیل عدم کمک برای بازگشایی تنگه هرمز مورد انتقاد قرار داده و متعاقباً از خروج حدود ۵۰۰۰ سرباز از آلمان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/akhbarefori/652134" target="_blank">📅 17:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652132">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e1a3ee0e.mp4?token=mzuUcFhplo7kRaodv_MmsY_OAQnJXKXGwDfF-GiUZ0R5hrTGyF6SZ380kDzVS6AOwy59FVITJurvWVp9LmVL8cOm670w7_VxOb8qaJ8yvt51SzuR3OWtc6nrOoeQ8zWHBL9ZXb9r5xJIcrp-n4MGQwrNJrjHRNSN_nyE1RWjqNvrvqM-2GwzGdkzi0JF7lZ-79Ai0wa-itSbrMxhc-0vNRhArX0qBmEP3Qr6FE2SsTIWffILl5RhasAUyjeqA1u4rwimucjyf23FQt5OGJlxfWK96jqDlt4Gd6yWBvocqEjosVbCQljb0vivjw-hO0pIoPLRpBJYCMi3EGlhL8nX0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e1a3ee0e.mp4?token=mzuUcFhplo7kRaodv_MmsY_OAQnJXKXGwDfF-GiUZ0R5hrTGyF6SZ380kDzVS6AOwy59FVITJurvWVp9LmVL8cOm670w7_VxOb8qaJ8yvt51SzuR3OWtc6nrOoeQ8zWHBL9ZXb9r5xJIcrp-n4MGQwrNJrjHRNSN_nyE1RWjqNvrvqM-2GwzGdkzi0JF7lZ-79Ai0wa-itSbrMxhc-0vNRhArX0qBmEP3Qr6FE2SsTIWffILl5RhasAUyjeqA1u4rwimucjyf23FQt5OGJlxfWK96jqDlt4Gd6yWBvocqEjosVbCQljb0vivjw-hO0pIoPLRpBJYCMi3EGlhL8nX0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کولر پوشیدنی رونمایی شد!
🔹
جذاب‌ترین خبرهای حوزه فناوری و تکنولوژی را که با هوش مصنوعی تولید شده را ببینید و بشنوید.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/652132" target="_blank">📅 17:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652131">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
۷۷ واحد صنعتی اصفهان در جنگ رمضان به صورت کامل تخریب شد
🔹
مدیرکل امور اقتصادی استانداری اصفهان: بر اساس آمارهای دقیق، یک‌هزار و ۴۴۸ واحد صنعتی، صنفی، تولیدی و توزیعی در سطح استان دچار خسارت شده‌اند که از این تعداد، ۷۷ واحد به‌صورت صددرصدی تخریب شده‌اند.
🔹
تاکنون چهار هزار و ۲۷۵ نفر شغل خود را از دست داده‌اند.
🔹
میزان خسارت خوداظهاری‌شده این واحدها نیز بالغ بر ۳۷ همت، معادل ۳۷۰ هزار میلیارد ریال برآورد شده که این رقم، ضرورت مداخله فوری شبکه بانکی را بیش از پیش آشکار می‌کند.
🔹
از این تعداد، ۱۰۶ واحد نیازمند تسهیلات خرد زیر ۱۰۰ میلیارد ریال هستند که با تأمین آن، ۹۲۹ فرصت شغلی احیا خواهد شد.
🔹
همچنین ۲۸ واحد دیگر به نقدینگی بین ۱۰۰ تا ۵۰۰ میلیارد ریال نیاز دارند که بازگشت ۵۰۶ نفر به بازار کار را تضمین می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/652131" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652130">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی ارتش: تنگه هرمز تحت کنترل راهبردی نیروهای مسلح ایران است
🔹
دیگر اجازه نخواهیم داد تسلیحات آمریکایی از تنگه هرمز عبور کرده و وارد پایگاه‌های منطقه شود، هر کشوری بخواهد از این آبراه عبور کند، باید تحت نظارت نیروهای مسلح ایران باشد و عبوری بدون ضرر انجام گیرد.
🔹
غرب تنگه در اختیار نیروی دریایی سپاه و شرق آن در کنترل نیروی دریایی ارتش قرار دارد.
🔹
دشمن با وجود برنامه‌ریزی ۲۰ ساله برای حمله به ایران، هرگز پیش‌بینی نمی‌کرد نیروهای مسلح نه تنها توان رزم خود را حفظ کنند، بلکه با شلیک موشک و عملیات زمینی، مانع تحقق اهداف دشمن شوند و این مقاومت، عامل بزرگ پیروزی امروز ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/652130" target="_blank">📅 16:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652129">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL5hpXIjBxGcOjVpHi-iOWwzL9dacDsnIfSb8McsXD7HARKjuEXclhgN7-Jou6Or7jtDq370c5Z91iwWqbJul1dvcbbBLGRgylyJP-_Hl9zjESyaNPJja_8xn3qwKcdIsflTVpN5D-anwget0lwWxe-5G1bhKqNY71jAViqthK-PeWzLxxo3iws0OONMReRHqGl5K5eKRgNWK5qbZyMuBbBowtB_W5SndCg4mw0iI0-7r0dhITcnlGXFbzjFagHY-hYjtHaURxdW9HtiaswtyMBfulnIuiYNAWwiG56J5QiVutWCX2X7cdA_OferLQ_e5HRbGs4BMfa0BWEIq5GxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف ارز ترجیحی بیشتر از جنگ قیمت‌ها را بالا برد
🔹
درحالی‌که بعضاً ادعا می‌شود قیمت مواد خوراکی و اقلام سفره خانوار عمدتاً از زمان شروع جنگ تحمیلی وارد شوک افزایشی شده، اما بررسی آمارها نشان می‌دهد درصد قابل‌توجهی از این افزایش قیمت مربوط به بازه زمانی آذر تا بهمن‌ماه ۱۴۰۴ یعنی دوماهه اول سیاست یکسان‌سازی نرخ ارز و حذف ارز ترجیحی ۲۸۵۰۰ تومان می‌شود.
🔹
بنابراین مرتبط دانستن کل افزایش قیمت‌ها با تغییر سیاست ارزی یعنی یکسان‌سازی نرخ ارز و حذف ارز ترجیحی، نمی‌تواند گویای تمام واقعیت‌ها باشد، همچنین ادعای اینکه کل افزایش قیمت‌ها در این مدت به دلیل شوک ناشی از جنگ بوده نادرست است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/652129" target="_blank">📅 16:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652128">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وال استریت ژورنال: حمله به پالایشگاه ایران در جزیره لاوان، کار امارات بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/652128" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652127">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران یک آژانس جدید به نام اداره تنگه خلیج‌فارس تأسیس کرد
نیویورک تایمز:
🔹
طبق گزارش لویدز لیست اینتلیجنس، که کشتیرانی جهانی را رصد می‌کند، تهران در حال حاضر یک آژانس جدید به نام اداره تنگه خلیج فارس تأسیس کرده است.
🔹
لویدز اعلام کرده، با این کار، ایران «خود را به عنوان تنها مرجع معتبر برای اعطای مجوز به کشتی‌هایی که از تنگه عبور می‌کنند، تثبیت می‌کند».
🔹
این مرجع جدید ایرانی فرم درخواست کشتی‌هایی که به دنبال عبور هستند را برای آن ایمیل کرده است تا ترانزیت را تأیید کرده و از هر کشتی که از تنگه عبور می‌کند، عوارض دریافت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/652127" target="_blank">📅 16:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652126">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تب گرانی بی ‌حد و حصر خودرو خوابید؛ افت ۷ درصدی خودروهای داخلی
کرمی، رئیس اتحادیه خودرو در
#گفتگو
با خبرفوری:
🔹
وضعیت بازار خودرو حباب داشت که مجدد مقداری از آن برگشت. فعلا بازار خودرو رکود است و خرید‌وفروش نمی‌شود. اگر همین روال باشد، شاید تا چند روز دیگر قیمت‌‌ها ریزش بیشتری داشته باشد.
🔹
حدودا قیمت خودروهای داخلی ۷ الی ۸ درصد و خودروهای خارجی ۱۰ الی ۱۵ درصد افت‌ قیمت داشته است. درحال حاضر نه خودروهای خارجی و نه داخلی خرید و فروش نمی‌شود.
🔹
ثبت‌نام ماشین از طریق سایت معمولا الکی و بیخودی است و حتی یک ثبت‌نام هم نشده، سایت را الکی باز می‌کنند و می‌گویند ثبت‌نام کنید و مردم را سرکار می‌گذارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/652126" target="_blank">📅 16:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652125">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: طرح مدیریت هوشمند تنگه هرمز در کمیسیون به جمع بندی نهایی رسیده و برای بررسی و تصویب  در سامانه مجلس بارگذاری شده است
🔹
عزیزی:
🔹
سه گانه موشکی، مردم و تنگه هرمز محصول پنجاه سال تلاش آمریکا را بر باد داد.
🔹
پیام حضور و ایستادگی مردم در خیابان ها و میادین ، بخشی از رسالت مبعوث شدن است.
🔹
جمهوری اسلامی ایران با مدیریت هوشمند تنگه هرمز می خواهد از این ظرفیت جغرافیایی به عنوان اهرم قدرت‌ساز استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/652125" target="_blank">📅 15:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVKh-Pq3aLMX0FBEhRkYQyKuIiIiFgDXpSDqEb4Vmr2rwdzTXkZdo_7n0rTq5WcSWNFo6jRgo7yxzyWvFlwq8uwloN3zl1ZjDjb4R46gMLyjm8uSMS4LYTbOJNApUz6aDP3AlLKOF_Wsy6LMimgDDtk8MCvKi14XVbFZPh8qujneUe7gFmWXk71UXOIMf0RW-ToFU0tVYSpMs1PYTx7DgME-7JNr9V4D6XTySHoTPzEeSkt5rFW3V1QQJwtailfHl-yfY21GyHsK1_AlVinQoB5_uDtJ6pr8iJ5uoPE0ScYJuwpq_0yF98OGNsqqm0kczfUUGP78U1utBgencImK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: پاکستان و عراق از ایران مجوز ویژه دریافت کردند!
رویترز:
🔹
به گفته پنج منبع آگاه، عراق و پاکستان هر دو با ایران برای حمل نفت و گاز طبیعی مایع از خلیج‌فارس قرارداد بسته‌اند که نشان‌دهنده توانایی تهران در کنترل جریان انرژی از طریق تنگه هرمز است.
🔹
دو منبع آگاه صنعتی که نخواستند نامشان فاش شود، به رویترز گفتند که به طور مشابه، دو تانکر حامل LNG قطر، پس از توافق دو جانبه جداگانه‌ای بین اسلام‌آباد و تهران، به سمت پاکستان در حرکت هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/652124" target="_blank">📅 15:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
جدال داغ در الجزیره؛کارشناس ایرانی با سندی از جنایت میناب، کارشناس آمریکایی را به سکوت کشاند
🔹
مختار حداد کارشناس ایرانی و سردبیر روزنامه الوفاق در پاسخ به ادعاهای واهی کارشناس آمریکایی در شبکه الجزیره درباره جنگ تحمیلی آمریکایی-صهیونیستی علیه کشورمان،با نشان دادن بخش هایی به جامانده از مدرسه شجره طیبه میناب گفت: این‌ها بخش‌هایی از مدرسه میناب است.
🔹
این مربوط به اولین ساعات جنگ است، زمانی که آمریکا با چهار موشک به آن مدرسه حمله کرد و کلاس‌های درس به این شکل و به این قطعات تبدیل شدند،و۱۶۸ کودک به دست این دولت آمریکا شهید شدند.
🔹
حداد افزود: کسی که غیرنظامیان را هدف قرار می‌دهد و آن‌ها را به شهادت می‌رساند، آمریکا و رژیم صهیونیستی هستند،وکسی که از قاتلِ غیرنظامیان حمایت می‌کند همین دولت آمریکاست؛ همانی که از این رژیم صهیونیستی حمایت کرد، رژیمی که ۷۰ هزار فلسطینی را در نوار غزه به قتل رسانده و همچنان به این عملیات‌ها ادامه می‌دهد و هر روز فرزندان ملت فلسطین، لبنان و ایران را به شهادت می رساند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/akhbarefori/652123" target="_blank">📅 15:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652121">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-OYKHr9lM1sCR1AIZkfvnsSYbqNMZkaoDbT1v0JOID1nc41kPuouX37V2jbsso54DfeQBqYfreifLBMzbhgVfS8YeOwCZ7TKWvUZ26ABMzzqJ4qQ5Rl6D6jV9dfjasKCYQxhgu94O1BgMWJ_9wLvuZ5UQ7-ZPXvYBslQ_eDMG7yuUOUxT02QKQmAHMfs-A28Er_6VRZYivJZ2oV2f1rurrK4Jbc2gNxDR6asTUbDB_UM6FNZT2ULF0ug2maqN53-yvYVPZfSYNGHmQQp2z4mrysN9ZKumEz6qFjllreZBKq_0VyJq_QtDGEirPvsnMkP48avNRHolXU6TA_R_43Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4MUJE1bsSbpbOepy0cpRxutPZ7snbo-tgvGya99k1wd5dk1s9pdmbxM3fWkYg1F4LUd6vYFndNUYMrbeFXh4B3ra5H72tbK73YuK8czsRsiBZPY6IcJPi_NrCjnXxBVKa6ZQ8HmWmMlJg5lJYVCCGjmg_bo6mJP9ikS6hSX3kh_vXAFZpMPTpsZU8BHC8nAvnqCRR29gL_BL6Ng9NCbROW0fGSyYAOl28OIxBk-y_I-OqyQOgvcOVQcuN3SniJzwj0d8o7MFttnqM6mv9qv3xT-xyhMt0vQERhKtW2YFWQ-dpx6LNM59xUK2_ZsBP08YvI80d6HycuT2H8zCc6_xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زمین را خفه نکنیم
🔹
هر بطری پلاستیکی که استفاده می‌کنیم، سال‌ها بعد از ما باقی می‌ماند. پلاستیک‌ها مهمانان ناخوانده‌ای هستند که هرگز نمی‌روند...
🔹
امروز نه بگوییم، تا فردا دیر نشده.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/akhbarefori/652121" target="_blank">📅 15:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652120">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ba53bbb1.mp4?token=UNs74Rndbpz6JAMT0Qr6z0QpIWnBh_yh1TelCnhnfDT38yXNBBr8RZ7zaavIX7n8IGiSUoop6jIojjd-RUVh5WlLIchJ25_t8TNqyUFVywap572iUl4EvEM3a5xSZ5MEqM-taMpww9gvY-az5huEXyVRnAe6J1fwri0_-2lpqwwy1wGhrAiUqd6sXee7OwY-g84PW-UWQlwL4T9jR_lt9DtVTUJG95sc7s0FyiuKHaoRKTXXz_O4M97n5uzow62RM_vVbT5pBHnfXZ5CfdKjRRgaS0383_JGeE_Y6BkyuWQybGvOjrzRINY59ogy266pjpbjc3Nhk48xwyr7ppEPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ba53bbb1.mp4?token=UNs74Rndbpz6JAMT0Qr6z0QpIWnBh_yh1TelCnhnfDT38yXNBBr8RZ7zaavIX7n8IGiSUoop6jIojjd-RUVh5WlLIchJ25_t8TNqyUFVywap572iUl4EvEM3a5xSZ5MEqM-taMpww9gvY-az5huEXyVRnAe6J1fwri0_-2lpqwwy1wGhrAiUqd6sXee7OwY-g84PW-UWQlwL4T9jR_lt9DtVTUJG95sc7s0FyiuKHaoRKTXXz_O4M97n5uzow62RM_vVbT5pBHnfXZ5CfdKjRRgaS0383_JGeE_Y6BkyuWQybGvOjrzRINY59ogy266pjpbjc3Nhk48xwyr7ppEPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما هنوز برای هم هستیم ...
🔹
توی روزایی که همه خسته‌اند، هنوز آدم‌هایی هستن که حاضرند بی چشم‌داشت کنار بقیه بایستن…
🔹
یکی زخم می‌بنده، یکی سقف می‌سازه، یکی جون دوباره به زندگی میده.
🔹
این ویدئو رو ببین؛ شاید دوباره به آدم‌های اطرافت امیدوار شدی.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/akhbarefori/652120" target="_blank">📅 15:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652119">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbxuRO7F5i7SzintC2f_NYC-vK7-HTtdcCNYiCHxsZawwX4-XDH8VrpzKHskDtHv6sqkMPw2zi7FWkquq2OZT2_vbvrzWir5MkCtG2u95_kgWTX6BK2_wwxxevLTK7r3-9Kjz6WmEO0fUYLynabmXNpAYqpWXc2cfmARvJoHuPEBEPMJASM-4_CqcqsVG0AQZjPKTKwzKMwaRTbf7PkJj1JhV5jUEeI6F5dAn-tQorOVbW6e68GNtr84lx_pwHUgKpeDoBNdDWOo5UMk7vcGIYSkKsS1FyoPwLPlyhOaoMtquYf2BWcMqiELvGWRgmqz7FAyidYZXqY1H_BGdFy2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود نظامیان اسرائیلی به منازل سوری‌ها در القنیطره
🔹
منابع سوری از تداوم تحرکات نظامیان رژیم صهیونیستی در مناطق جنوبی سوریه در سایه انفعال دمشق و ورود آنها به منازل سوری ها خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/652119" target="_blank">📅 14:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652118">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ سومین حمله امروز اسرائیل به جاده بیروت-صیدون؛ افزایش کشته‌ها به ۸ نفر از جمله یک مادر و دو کودک
🔹
یک فروند پهپاد اسرائیلی خودرویی را در شهر سعدیات، در نزدیکی مسجد جامع این شهر، هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/652118" target="_blank">📅 14:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652117">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
آتش نشانی تبریز: در پی ریزش ساختمان نیمه کاره در تبریز  ۲ نفر جانباخته و ۶ نفر مصدوم شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/akhbarefori/652117" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652116">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giIlsT3Zs21TupR7sRckA6T9Y-7Anv8UfZT3c-2TQVTZI1YvHSTRT4NAiB0rICIO_vf4x624pPGSA3f3R-8y7N4y6smR2pK49eRS5EttyjTnctSrjPeDnkM4FZkZtNpa7m7lpW_DPcPVd1FXCwSW7wjYf18Uq-a3qqkuVqaVT91jCtYx1djBIMoPtqn4htLJrhnsA45jpXRR1dzrPSIefJYECthSvLmEYCfIILItReaM4vRMws7VEKiFOI9BDbUQ1c8vo4vXCWIPJ1qB9QKDSF0NtEEeFCi8DV5wyjR8Hzx1nzPBDmjFsuczOKY6J-6mrZDB5LBCYX3RTFxFhlNN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کانون وکلای قوه قضاییه: حمله به فرودگاه بدون کاربری نظامی جنایت جنگی است
🔹
حسن عبدلیان‌پور رئیس مرکزوکلا، کارشناسان رسمی و مشاوران خانواده قوه قضاییه در فرودگاه شهید دستغیب شیراز: فرودگاه شیراز به لحاظ موقعیت جغرافیایی به هیچ وجه گزینه و هدف نظامی تلقی نمی‌شود و دشمن بدون رعایت تمامی موازین و قوانین بین‌المللی در جنگ، این منطقه را هدف قرار داده و منافع ملی و سلامت جان شهروندان را به خطر انداخته است.
🔹
هدف قرار دادن مستقیم هواپیما‌های مسافری و رادار فرودگاهی مصداق جنایت جنگی علیه امنیت شهروندان تلقی می‌شود و به همین منظور وکلای ما در کنار کارشناسان رسمی حضور پیدا کرده‌اند تا در مورد پیگیری حقوقی این جنایات اقدامات لازم را در خود میدان انجام دهند.
🔹
براساس نظر کارشناسان ما دشمن در حملات خود با استفاده از سلاح و مهمات نامتعارف و غیرمجاز درحالی که فرودگاه در ساعت خدمت رسانی بوده امنیت و سلامت جانی مردم را به خطر انداخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/652116" target="_blank">📅 14:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652115">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSr9tLtTU0usJAtr_sgjYLJeFMoEJHhWOCMxYWbwzFhCJq3XlI88F5PwyvOMvj9yElsgPgW17SYqm1nvyrvP6IrcCG6Z4FO8BCavHpaoYGu2Mra8K7WiqdLQq032yc96RJt2gY8zlFrDn3tDbA3nSSyQkAFgyPy34MLoiZNwvIIszXJHo0OSELN54KSr4kjbqvroCUJoxSAVzNUubQu-1G4DgVQZpW7rflVGJRk1Logk1mAgRCGh7vQK7Y5c2ahMWoBxwxuL027ZYcnfci7ikV809jRqTJ0A0GvFelePEnCZMCsJKK922JNq7JHcuJZAKcKl4O7d9Nl2Tlje5j5aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف ۷۰۰ تُن روغن احتکاری در بروجن
🔹
فرمانده انتظامی چهارمحال‌وبختیاری: درپی بازرسی از یک انبار، ۷۰۰ تُن روغن خوراکی احتکاری به ارزش تقریبی ۹۹۳ میلیارد تومان کشف و یک متهم دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/akhbarefori/652115" target="_blank">📅 14:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652114">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زلزله شب گذشته را ۷ میلیون نفر حس کردند؛ احتمالا وقوع دوباره زلزله
مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله در
#گفتگو
با خبرفوری:
🔹
اینکه در زمان کوتاه زلزله‌ای به عنوان زلزله بزرگتر اتفاق بیفتد، با اطلاعات موجود چنین پیش‌بینی‌ای نداریم، اما با توجه به اینکه منطقه مستعد رخداد زلزله‌های بزرگتر است، زلزله‌های کوچک را همیشه به صورت نشانه‌های احتمال رخداد شدید تلقی می‌کنیم.
🔹
منطقه تهران در این ماه‌های اخیر لرزه‌خیزی قابل توجهی را در بخش شرقی خود نشان داده است. منطقه فیروزکوه تا پردیس اتفاقات لرزه‌ای را در ماه‌های بعد حداقل در حد همین زلزله ۲۲ اردیبهشت ماه نیز تجربه خواهد کرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/652114" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652113">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O36dDzH0LqP3rHRizNNvpIBIapGp587ztVKiJmUAWR6x7n5OqqNLYHCAd5MxJS4ZeXwn2F4Wz72hmFbnJdtucodac5FrADw4ML892L3dXA-wDHF8W6ZJausfcLkDUKSX77EtiY_KmbbEOiNT7nWB7x5RdgSP_2EzDs1-J_oEWBDhjV07DcI9f9bq3V_9oaqnekuWhgBWVGkBwLFaAIJ-8OSvpKGBY8NwjVKzoyXL13jGkcw7pK0tFPgNw52DZY-Twc_otyxCjIaiXVQzA-IelhxQV5p4zK_20QRrm47qVOO08TmV70hC1akqD3SD6SslogeOB4vCm1hXy0zplfPAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست رئیس‌جمهور از کارکنان وزارت جهاد کشاورزی: می‌خواهم تمام توان‌تان را برای کنترل قیمت‌ها به‌کار ببندید
🔹
مسعود پزشکیان: با قدردانی از نیروهای جان‌فدای وزارت جهادکشاورزی از دورترین روستاهای مرزی تا پایتخت و وزیر محترم که از ابتدای جنگ رمضان پای کار معیشت مردم عزیز ایران بوده‌اند، می‌خواهم تمام توانشان را برای کنترل قیمت‌ها به‌کار ببندند.
🔹
وظیفه ما این است که با همه وجود در کنار مردم باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/652113" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652112">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
قیمت آب در ایران واقعی نیست
🔹
سخنگوی صنعت آب با انتقاد از پایین بودن تعرفه‌های آب در ایران: وزارت نیرو خواهان اصلاح قیمت آب، به‌ویژه در بخش کشاورزی بوده اما قوانین و تصمیم‌های بودجه‌ای مانع اجرای این سیاست شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652112" target="_blank">📅 14:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652110">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3_6MAbW6oRNGuKshqMDyUKbwP2rHAwdwlU29U94VwlWk6vVJjTFSQ3LOgLP_oB56bOGQrM67z-eqa0OkZpSUibOXSlHxKCc9du93o4yK7v0fMdYEkOy0Fi_n6r-vy7vq2Y_cWg2Sxohv1WTOlb5nCr1guffXNYk3D2Oi3N9dG5APiAdhXMf23bhztYiMB4GIh27u3uMQ0eJUq6vsQy1eSGc4lw49i9GLcDEIEl_J8CtWLqyDTh85m8iTyNDmw0CXq_BZ9LRiyjCKFxjX-zoXMGvcU_L1_0n7BwDVk_rFpzmYvv3InWmvstC-caZtD2NTHZQyaVGprG1KvjX5Mn5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر مخفیانه رئیس موساد به امارات در طول جنگ علیه ایران
🔹
روزنامه وال استریت ژورنال گزارش داد که دیوید بارنیا رئیس سازمان جاسوسی موساد در خلال جنگ آمریکا و اسرائیل علیه ایران دست کم دوبار به امارات متحده عربی سفر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/akhbarefori/652110" target="_blank">📅 13:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cei6DvVJy09YwS8sfVImgD_0iZMShBOHlWYJ3-OfpfheQlsKoRztlcA2veGTzQfJtjaCTU3z0dCvaOyoSP3OdVwaM5Af7fnv0wOWK3xHS9wIxibS-BwArUAElJ0glbBniMy2DyFF_PRcnd1HBiy_3L6tv7bfbZYWI1hh8sYhbnzUYJ9QsjrLFFdf15142fIAW0-tOzD81DiL6QzRwFsuZ_3pdKXWLOsn_-ifcFYuYlxIqMKp8bO4OMeFFZIMAYYY2MiEsHucBbsUpEiJ4yCxFOd4ER4eWJVFVhZGALMueryG-qAyxrKZBNbhBizOwdVX_TthhlWAeyvoN-U3rb7-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8VFkVu4mdiQpcEQoj0Os4N5Z51pZJvRyZYlHPNHBmK5SGhwkQUzh4CGqIAWdydGuUztT0nqqMA80LcwI9gz8Y5zZecAH8vzXXbeo_bxWEkhYyStM2Sg-ggVOL7yOfHhysTKqR18QXlWav7SDiu00kMW6zotgMQVAp18vLNp2vo15t44irR5ofwNYuZOde4Nyl685LIRugnRtIxLznMFWrcmjyEoFV6-uRVenSnb7czW7iiKDglz-w2vi1RNMNBL8wgJWyntZpVIcjMOXJn5Cs4Yi8l0R2B0fBPp8EhQy7-nIsb0PWL9TR18dO0Y-BerSy-jDBCUukGG3lvN5Vi71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAJnQSq1eqevu_SayewdE7QZBvNChVccFh-Q8lFOtOCvXoyRe8A_b6HA1xbIxXO5DYG1l2E8KpTH8SO6SqCtUfRPbxUuMPXduKWqvc9YZKoT1OMA5Rf2HXdCWK1lxlr1hvqRpL5pxKk9Guxly9aT6Cig4ryWY28BkYYBriZiUC8k2kItYVZ8o_1pqN2U2kg7v8oiLeDtEFZgN_WwFYjdbmBqoIm7yANKexqsJl0NPRg6WmCuvULbl88o7ScxVzKs5aAz8FkV-blg9Bzz4GVX8V_Te04AzC1T6fHY3ZnFsKLhProREP2SHO1lxdlLRmmgX6s7XyL53lvEXoYp7-h3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2OvBIXmBpZHUZwcrNOh-5WLk4U9ckBsK0JdIwZAwIxpNib0i5S3XwZUbx7c5pay6FHCQ1VwqmVGCeKZEVhPk_M5kB0na7vil7TV91AmOre8WlmEfVE6Q29AGr6pQFfhowVfcKekE3YXBktGIC-gm0_Yqkyt-mbfwDAhEGZPbpAIQiPAosPDRbPlEWKDIHKOL5Nyas2EI3FjNtXtTbNlSRBVLUOXoNqC8AO1uHpO_I10fJuLxI9ie6ia4WdaeavDu1y5bnCzxvJPzAwdI3xWFm0QY9Gk78FwrSVY0pQ7C9fW47vdoX75D2S8sJAeQ0PZ7r57he3kCHl5aU3XzoTtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoXk8Kcu9cABWUoPC0fDBSzsazXlx_Gs_35rUwTmb3Yq3zr4-hAFkP8Si1bbx89XYL2MDZXzoTRPKLSBwIjzzjDGzSuLnHZgSqZZyKiK_HGa1iiZaAMHGATDGPCgMDRg3JQzhA5DFoHkekMbwg-sVfAdscETHGZ3jGUDMmnwY3WQEwrr6NNk52NnqpPx5xR9d-foQicNBwdK0YarXAFq9EmxVU39dtSmc77Np5vMjsp4kBjPrAuPDbVdENz_-ER_kPbeYgrQlCsUky3gribIRU6PmEmEdScNrYm1H64zNL87g065G436B_T8JRGFoMdjOtD2YUZj1YI7VglC-SAh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBIyzMIn0z-SBSiGtALK0p3qRLszJLuaDLIIJJhvx4j8w6gCwnM1OpCORyDeHlxfwsJihNqRj6WnamoA67FM09WDQN-4TqIbuUubzjtiHcy1RdUcei4b1_8FQHuHXFWUqKBOlNtBQeAecmiTyv8249nbgGhPIYlpF4ZB5Aai_zma3xi1Uds9D-opzb7Ove43XvYTqAJm0jhF0fndD9gBZFL1dN2qRVTjd76fUz1FV_3AgwGZZpE6KtMqTuOxe8AqDDKhnnRjofpqkFdnzM8hqSkmPPEAkISEb4RG_itITD0b_aKF-vc4lcRyQVGMTkDel8El5cX_wi5QZ0VU0oQ2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KePhJ5vh4Zz_4ysKGvBI6QFnKBO7Mr1UJJqRrdVigsajUxsIGqoVIcbugFGiDc5mL1aBaVIG094tfxMg1tx5I3zjUW3ozUZCXq-I7NHm-6Vuf9NWPstGC3Jcg4cxGCpPFHv-8kDFKHmvAToGXKTP1Ug2ncRcjdOAHbqJi_R9GKT1gdYFRLF8fIEOSUe8IzzVk4qywR27wJCHzDvULfJWNEMxJ0VOldEMZmLUsjXTOIYcACkVE8ytzVANPJt_FJ9XQP1LKwqny6PH5kJqEnhSD_3IZxheGSVhBuL9nPWnUNsZFRHHf8zuG2cFR7mKc8p0fmje0h5NKLlv8Zi2vK3KVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8C4gL0HVZfmLJRBsAwDkNedbvZ5QImeHOpCeRS-nK7DOH9hEKkHXb-tPpUh1-UFoHyPfgB15n0f7MCQzoQmN5920melu73ue3OFfR4ENia-gFhUWSDMbiYA1t2f8tz0KSeXl139ZO1A6P9wE9g_4CUEjUHm9w2H-Xp9ZOexOKBPRlC4gysWhEyx29sJPPSFMLtDe10XtAmbs_SL5KwTKVy5f91fhi-Xrc-GfsXPDv2A72Bt1oKTvjiT5BaLyw_jjbMDGU97W2CyFBbWXMTKBPPxP0Qb-9T3-AxlE82iyrgIegcgCTd0D0bacb67xYq4cnbYJfRclUZ4bS3yYEv2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAhoW_LwGO-yu4e4LuPS-dI889Z0rNO7z5O85z8oQpMS5yhLfjn3GPGtH_pNGdULOZF0rJIfgspYuL-0evLxOHzeVfIV9-Ot4l8oDeuP4ZJtjF_KgIiZrvCXwadu8hVYX0K_krxYz8pWvRiOK-XkQ2iS36qJMh1f4TZnZAAODddal6XjfrN27-XMwa4Hz5lB6bNNWtIHYAqglFYxCq-mUaAtzXc5WmrQTCAgyrr56D-zRPzqv8SnYqzdSJZjSNtw7wnsPh3qiw5YiO2LuKunboB2pHBEPJOmUaIYjbm2KNXsc9wKmsviFLuj28Hg3R7GBnCqIPdYLVI6kY_6hrUBig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قاب‌هایی از تنگهٔ همیشه هرمز
🔹
بیش از ۱۵۰۰ کشتی خارجی در دو سوی تنگهٔ هرمز منتظر دریافت مجوز از سوی جمهوری اسلامی ایران برای عبور هستند.
🔹
عکس: معصومه کمالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/652101" target="_blank">📅 13:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9d2fea12.mp4?token=dGed6nhiL0t6x88kLvMnyuegT06kG3f2zA0bSLmSJt4otxH-CwxOOFFYDz-xoobSqIQx9EI3pr5At3ZkyEL3M8mGcV7OfGAfPVcWOTdbNUuZZKTmimJkiTsIxopLDNeUvASwyoc1IP1HHUV5JO1QqMDDc5au-pu0CvAtFlhuOASovcGMa2niQacL4nBmMFvBJy2G6Xl1P1QWP4R9t0OX7CHv3HH1hekFHFFF86Rbj24uOtSQsJGt3TYSR9akiSqf397konYPC9Vok29btjJtQ8r8TH3IMV4EFw9k5p32i9yluQ2SOVeG5yP2g-P0kFztXRMoquSrtETZjQr_QLxtg2fDiKPmpVNnpFHojq7a4O0soI7dIoKawmY1WYLw-4aP6blUgUa1RDlRC1D7d1PJN1V9d_3-tMpJBrEpiAccP66xG8wO-3JNtdFYAnMhwiD2cJFmu1B9csmEINpbfIJ6nZuvPGGti0GtkbVFKVxAhHyX9QyjNfeWHc9zR42qtxvxnLP8d-OqfYgwwBqPY11_tTo0gA1Hl33Nwp5-Y9w3TZftue6eOZCOpLhjDG4FzGHCUGNIsXxmN95UCoT2Phjn0qqswUU-QSidLtSsoX6-v0METE8G96bgFx5D07FMic0bhVIbfb5ue6b6EfLmUVmqyQ-C3kPhDNdKN4o4hlLdKMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9d2fea12.mp4?token=dGed6nhiL0t6x88kLvMnyuegT06kG3f2zA0bSLmSJt4otxH-CwxOOFFYDz-xoobSqIQx9EI3pr5At3ZkyEL3M8mGcV7OfGAfPVcWOTdbNUuZZKTmimJkiTsIxopLDNeUvASwyoc1IP1HHUV5JO1QqMDDc5au-pu0CvAtFlhuOASovcGMa2niQacL4nBmMFvBJy2G6Xl1P1QWP4R9t0OX7CHv3HH1hekFHFFF86Rbj24uOtSQsJGt3TYSR9akiSqf397konYPC9Vok29btjJtQ8r8TH3IMV4EFw9k5p32i9yluQ2SOVeG5yP2g-P0kFztXRMoquSrtETZjQr_QLxtg2fDiKPmpVNnpFHojq7a4O0soI7dIoKawmY1WYLw-4aP6blUgUa1RDlRC1D7d1PJN1V9d_3-tMpJBrEpiAccP66xG8wO-3JNtdFYAnMhwiD2cJFmu1B9csmEINpbfIJ6nZuvPGGti0GtkbVFKVxAhHyX9QyjNfeWHc9zR42qtxvxnLP8d-OqfYgwwBqPY11_tTo0gA1Hl33Nwp5-Y9w3TZftue6eOZCOpLhjDG4FzGHCUGNIsXxmN95UCoT2Phjn0qqswUU-QSidLtSsoX6-v0METE8G96bgFx5D07FMic0bhVIbfb5ue6b6EfLmUVmqyQ-C3kPhDNdKN4o4hlLdKMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته شدن پرچم ایران بر روی کشتی‌های متخلف آمریکایی-صهیونیستی
🔹
ماجرای توقفی کشتی‌های غول پیکر با ارتفاع ۶۰ متر توسط نیروی دریایی سپاه پاسداران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/652100" target="_blank">📅 13:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ3I9z93ClK_bHlXpdOKT_icDrYGNSxcEyhiT5XrrmNm88qfYqL7mIVLHWUd-NqwZQuR9ecbhJl2cHOLhUvINp5a-mFd-vfSQKufFRLIMJKlINpWWrlyBCrFHcgYdI6qg4n7sBWPla8YaxaMrQF9EfUGbOlJpkWHGrOgurk7hVuf-Zlsa5H3s8MV16c4CYHhsEbebwS5oprZtGKh50KJz6lKwes0jNOYa0lMqyNCQAJFgpYi3uoK7d7HKV9TQHF9vwJNN4NIM39e-E1icD8cbpzCbxjBUBFVYJEr63QxXzLUkE-kuVuX9g2FOSkaTXiRWmtd2jx3TEr4VbLaonMQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: هرکس جرأت کند پا به خاک ایران بگذارد، به‌شدت پشیمان خواهد شد
🔹
سخنگوی وزارت خارجه به شبکه هندی ایندیا تودی گفت که متجاوزان به دلیل اشتباهات محاسباتی‌شان درباره ایران، این باتلاق و وضعیت فاجعه‌بار را ایجاد کردند و درباره تکرار چنین اشتباهاتی در آینده هشدار داد و گفت ایران، غافلگیری‌ها و ظرفیت‌های زیادی دارد که هر زمان لازم باشد از آن‌ها استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/652099" target="_blank">📅 13:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj9EdDoeTBWRMvi2JWPzwtXmdAYx4HmfvT_3vv39H4RmlDS253Q3LIrbaM5QJWwfpSNauNS6U9BDxWY73__pRBG-XcvcX6dXTX8XwHy3sUOA4wM07e7mx9ZD1yytdxZxFrcInC9SwqasAELL3RMXyON8vNcPZVwLDBvfMuPYqr5sgKxOlZ6dKIBdfv7Be6TVyMZ5Y5bQI6Wh35tZyWX_lry5YfX0bP-Bw0Kl7ZJe4dM2iOGPd43XNVdRKv47N80xTssE0SGmr75Cp7doMLAk27OAH3z2lgtu5RGAVbYodduuNP1vq9D-3dh9N2XtXcgPnnUf_X_Yq9ximVQ2pWwuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرزبانان در ۴۸ ساعت گذشته  توانستند ۶۶۷ کیلوگرم مواد مخدر و۴ قبضه سلاح را در برخی از مرز های کشور کشف و ضبط کردند
🔹
فرمانده مرزبانی فراجا: مرزبانان هنگ مرزی میرجاوه توانستند یک تیم تروریستی را متلاشی و تعداد ۳ بمب انفجاری را قبل از ورود به کشور کشف و ضبط کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/akhbarefori/652098" target="_blank">📅 13:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
انجام آزمون، مصاحبه و دریافت شهریه در مدارس هیئت امنایی ممنوع شد
🔹
محمودزاده رئیس سازمان مدارس و مراکز غیردولتی: تا زمان تصویب نهایی، مدارس هیئت امنایی موجود موظف به ثبت‌نام دانش‌آموزان صرفاً بر اساس محدوده جغرافیایی هستند و دریافت شهریه برگزاری آزمون و مصاحبه در زمان ثبت نام ممنوع خواهد بود.
🔹
فعالیت این مدارس بر اساس آیین‌نامه مصوب سال‌های گذشته شورای عالی آموزش‌وپرورش انجام می‌شود، اما مقرر شده است فعلاً این مدارس موظف باشند تمامی دانش‌آموزان محدوده جغرافیایی خود را ثبت‌نام کنند.
🔹
ثبت‌نام در این مدارس باید صرفاً بر اساس محدوده و جغرافیایی تعیین‌شده از سوی منطقه و استان انجام شود و هیچ آزمون یا مصاحبه‌ای برای پذیرش دانش‌آموزان برگزار نشود.
🔹
اکنون حدود ۳۵۰۰ مدرسه هیئت امنایی در کشور فعال هستند و نزدیک به یک میلیون و ۲۰۰ هزار دانش‌آموز در این مدارس تحصیل می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/652097" target="_blank">📅 13:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgpvEgBUWPnSjm1PlxWQnBRfnx05Hg45w4RohaXKx0uqgFdq8fOomXxiOOeWTZo9v4Z6YiVxBz6FICHBnjqYkxTV_zjEfR3gPnSTcOScGNzFw3k2o8S5142cMktZncryF8rUOWCmPJkar4whF9XPsiu1WLLOiDGTRrMyV9CDkVQBVpIN9uoitOkjVZKVvnw3pe0dxHyq7wQhN4Oy1LVYWSPodadNb1kSeqprB3umr_jYWcTRSI9Um-6scWtN3c7d-F0m5CuO93LQpYWZwIFVAPORGberZTiHVvy-4TrBypQmQo35GKNGwP-2aaWZOa4QbNBAISIvoPFGmVtpwd6Bqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبعات اختلال در هرمز؛ ذخایر نفتی جهان به سرعت در حال مصرف است
🔹
آژانس بین‌المللی انرژی اعلام کرد: از ماه فوریه تاکنون، به دلیل بسته شدن تنگه هرمز کاهش عرضه نفت به ۱۲ میلیون و ۸۰۰ هزار بشکه در روز رسیده است.
🔹
به دلیل جنگ علیه ایران عرضه نفت در سال ۲۰۲۶ کمتر از تقاضا خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/652096" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: ایران با وجود ۱۵ همسایه عملاً محاصره ناپذیر است
🔹
تنها ابزار آفندی آمریکا در جنگ اقتصادی با ایران محاصره دریایی است.
🔹
خلیج فارس با حدود ۶۰ درصد از ذخائر نفت دنیا و بیش از ۴۰ درصد ذخائر گاز دنیا مهم‌ترین منبع انرژی جهان است.
🔹
در جنگ اقتصادی بایستی دستگاه‌های متولی اقتصاد آرایش جنگی بگیرند.
🔹
ایران با وجود ۱۵ همسایه عملاً محاصره ناپذیر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/652095" target="_blank">📅 13:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8E0XguDzTHq8-5lQSpiIJ_dcLu0BgkkgHebWlF2I9CHJk0CegD5Q98X28w1Cz2cUJySk_XbmuN4-xdr2b5WsekP6fAFnoBcfUxa91b_309gRsNKPEEgEAcAppl6IuLTDEfDy0E6q8pY9c7hNfLHKo704aV9MVEsY1mgi7GbsEErtHN-PjuL8DWT4TUtkyJkaWEDYTf0YhxfImVtoKFCr1wgYgp0GnR-cyp80Je_GQTV7p9ax3y_MoLWXfv_Bd3fsKPwpBgVjf6DdGS_n_NppaY5ldOxlSZ0UpFH0WLnxZhWATs83JzQvNtLlhcpb13996Otm5Y4HmerIjs82BczqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کاربر فضای مجازی: بعد از اینمه فشارها آیا برای بعد از قطعی اینترنت پرو، راهکاری هم برای کسب و کارها دارید؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/652094" target="_blank">📅 12:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
۲۸ نقطه شمال تهران مورد اصابت موشکی قرار گرفت/ ۴۵۷واحد مسکونی آسیب دید
🔹
شهردار منطقه یک تهران: در این منطقه ۲۸ نقطه اصابت موشک ثبت شده که در نتیجه آن، ۴۵۷ واحد مسکونی با آسیب‌های جزئی تا تخریب کامل مواجه شده‌اند.
🔹
۱۱۵۳ دستگاه خودرو و ۸۷ دستگاه موتورسیکلت مردم عادی آسیب دیده‌اند.
🔹
در یکی از نقاط اصابت هشت بار انفجار رخ داده و همچنین انبار نفت نیز هدف قرار گرفته است.
🔹
در اصابت محله زعفرانیه ۲۸۳ واحد مسکونی پیرامونی نیز آسیب دیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/652093" target="_blank">📅 12:42 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
