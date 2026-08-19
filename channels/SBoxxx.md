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
<img src="https://cdn4.telesco.pe/file/bJrjwe4iW7IqbqEGiL1sC-s5oCqWOla2Y-3jzXutTxaRXVH9e1ls1aFwY9z5x3XYHWNUdcLuUcjDOIoGDLQW_REIoOUJ11XRJGEbxFvp--oeMDUF1-hVlE4egJPfY271EkI_BouxXKFpP6X7v8Xkpejwz1HPrqCh2MJSL_n7FF-eKIzTfBeLmRMA0e5OiMbHVhUlzAqVk53LozxIr2EieA0Xt-VVvc0nZR9_hJt5PgqBHyTAzAg1XnEtg0y1_Kx7rJ8WLPw2DGxvF72kl2xRoOfDP8e9TBfEV5ij9yon1nOlkoVQ8RJWX9CseJPrlUlxQ0OLgvcSbI34DX6mfQJERA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 17:33:48</div>
<hr>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایینی است و برای طلا این موضوع به صورت نسبی مثبت است.</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/20022" target="_blank">📅 16:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ارتش اسرائیل در جنگ شدیدی با حزب الله برای تسلط بر تپه های علی الطاهر است که به شهر راهبردی نبطیه اشراف کامل دارند.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/20021" target="_blank">📅 15:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/20020" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/20019" target="_blank">📅 15:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.  هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/20018" target="_blank">📅 15:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک جوری میگویند خویشتن داری کند انگار می‌تواند خویشتن نداری هم بکند  چیزی نمانده برای این وامانده های غارنشین حرامزاده تروریست</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/20017" target="_blank">📅 15:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:
اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.
هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال خواهند شد.
در دولت بعدی، ما این سیاست "مجازات" را به طور کامل اجرا خواهیم کرد.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/20016" target="_blank">📅 15:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/20015" target="_blank">📅 14:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5NSAhxjfdWCk7Dueb8V5tD7hwc0O0yqdnkzPoclMEXt3GGc--x6HKH6UUW3GQRe2kqLBMlcaGW-H1WoRuk6K8xcaQsUX03jRhVtHEUTLbisSQfyKGDcEs-Y-KIwfUjDdy4uqs1vvqwYA5Ht6DbxVntjgo4K-Lt6txov0gp7aCgPDCmnXgQaMkF14P3pk9D4dxfwaKccXa0GCntQi4ZXy8M9lHZ8tWjaygxUY5ZCiVe-CTwhfeQbmY3AAvBiyBkPxHScTkwTGMZ7NWSI23nLPI8VeVuNxrGjQOSUzI106vP5MZpdV2G1CV5tPrNbVJGE_COkCALOjVYKvLSePRIPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایینی است و برای طلا این موضوع به صورت نسبی مثبت است.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/20014" target="_blank">📅 13:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwhaA7qu2OwsoyCYyuyZJ9IJocYLmPt68NKsBeRZCDuL9kGGRC4e0iU2wIg_eWN8SohuAo1kf94-jpNquPEWtHIvu95GPV5WBcvLhrTDlCbWWB4AncR22M9LvKPliko24axIRLq5aGNfjp1oaR8Y5UH1gMmVSUNBEIvL7ml5OYzxalOoGb0C7jxOMex8AtgTyrZahwBRm2sF_Mntg6F58Lozvs6K27dYS_DkcngGmkVpozrr5L8fKY065D7zHxU0ItlzVObxDBwRYcI9njioitnVXQoKyib63ndRO4fHcf90xUyDn5WAE8FKBR1S8uLXaXuzbUsUvBrNuVk1lDYIdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/20013" target="_blank">📅 13:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ایران در حال بررسی حملات به  خارج از خاورمیانه  است
اهداف بالقوه شامل پایگاه‌های نظامی در بلغارستان و قبرس، به‌علاوه کابل‌های زیردریایی در تنگه هرمز است.
مسئولان ایرانی به‌طور فزاینده‌ای تعارض مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حملات به زیرساخت‌های حیاتی ایران می‌تواند جنگ را فراتر از خاورمیانه ببرد.
منبع: FT</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/20012" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2YrS-DB8weU57-EvWA1ur3Uhd-D0SUZaZGI0NgCWzUBuMvRqClfpmNh5qYaMtOdohnGRo8mUylm82G2V0nEFFENIugkncsUuWNiQ0IFskDNY9UrMj8GNty8b1DsPPVIH6utmN6bEpZ8LvNoIpaZ-kHpZ6Jfc7nZQeuflONr1Y9ZMXpLO2N9lsz-USiXE1vfB8S1Uv876DqQYbWmsTPxUFme2zTyBPAVBFO_jaTGJdrB6eDr2hPxlOWoEzYFBpg_ey3IxWWYt_a6p1_AoWL_DYbjQ8B0aTwm0vr8pJO_lGKET0DPoWmdcY5UPk8QeRdl4X0344BEkwHvVgpVrsC4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج انتخابات داخلی حزب لیکود و چالش‌های پیش رو
در انتخابات داخلی حزب لیکود که روز دوشنبه برگزار شد،
الی کوهن
(وزیر انرژی) در رتبه اول قرار گرفت و پس از او
امیر اوحانا
(رئیس کنست)،
یاریو لوین
(وزیر دادگستری) و
میری رگف
(وزیر حمل‌ونقل) به عنوان برندگان اصلی شناخته شدند.
بنیامین نتانیاهو
از این نتایج ابراز رضایت کرد و اعلام کرد که حزب لیکود در انتخابات
۲۷ اکتبر ۲۰۲۶
به «پیروزی بزرگی» دست خواهد یافت.
گادی آیزنکوت
， رهبر حزب یاشار و رقیب اصلی نتانیاهو، لیست کنونی لیکود را
«لیست ۷ اکتبر»
نامید و آن را مسئول «بدترین فاجعه اسرائیل از زمان تاسیس» دانست. او در پستی در شبکه X، کاندیداهای لیکود را به تقسیم جامعه اسرائیل، عدم پذیرش مسئولیت و ترویج فرار از خدمت سربازی متهم کرد.
لیست تقریبا نهایی حزب لیکود شامل
۲۵ نفر
است که
۸ جایگاه رزرو شده
برای انتخاب‌های شخصی نتانیاهو در نظر گرفته شده است.
گیدئون ساعر
(وزیر خارجه)،
حایم کاتس
(رئیس کمیته مرکزی لیکود) و
اورن دبرونسکی
از جمله افرادی هستند که نتانیاهو آن‌ها را برای این جایگاه‌ها انتخاب کرده است. همچنین،
نیر بارکات
(وزیر اقتصاد) که در رتبه ۲۴ قرار دارد، ممکن است به جایگاهی پایین‌تر منتقل شود.
بر اساس نتایج،
زئو الکین
،
مای گلان
،
یدیت سیلمان
و
اوی دیختر
احتمالاً در انتخابات آینده کرسی خود را در کنست از دست خواهند داد. نظرسنجی‌ها نشان می‌دهد که حزب لیکود در انتخابات آینده بین
۲۲ تا ۲۴ کرسی
به دست خواهد آورد، در حالی که در حال حاضر
۳۲ کرسی
دارد.
مشارکت در انتخابات داخلی لیکود
۵۳.۵٪
بود که نسبت به انتخابات داخلی سال ۲۰۲۲ (۵۸٪) کاهش یافته است. این کاهش مشارکت و همچنین تغییرات در سیستم انتخابات داخلی، که به نتانیاهو اجازه می‌دهد
۸ کاندید
را در بین ۳۰ نفر اول لیست به صورت دستی انتخاب کند، باعث شده است که رقابت برای کرسی‌ها شدیدتر شود.
انتخابات داخلی لیکود نه تنها لیست کاندیداهای حزب را برای انتخابات سراسری تعیین می‌کند، بلکه نشان‌دهنده چالش‌های داخلی و رقابت‌های سیاسی در داخل حزب است. با نزدیک شدن به انتخابات، این لیست می‌تواند تأثیر زیادی بر سرنوشت سیاسی نتانیاهو و حزب لیکود داشته باشد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/20011" target="_blank">📅 08:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نشریه "اکسیوس" به نقل از مقامات آمریکایی:   دولت ترامپ از دولت سوریه خواسته بود که خویشتن‌داری کند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20010" target="_blank">📅 02:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نشریه "اکسیوس" به نقل از مقامات آمریکایی:
دولت ترامپ از دولت سوریه خواسته بود که خویشتن‌داری کند.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20009" target="_blank">📅 02:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK02ouRo3pdTPHRcL_nYT-lSFINme_2dElhs-TnFIWZkKJV7M0BpPBm8u06lXDMo6nMIfw1TR0KlUfozjSpogSAOIrT7DeFVyK2hBKJplwAAQ9wwUwB3SKP85J9b7FS3osvhfrDNkK1h-E-sVIbUWV4gkke-IdsGaZwWJy-J-4KvVCYj71BA3X57-BLBucFdTRsSvi8fEmiVBzdThNqfnvbbQHaLmtooBNhgto-iCU_1yAV0LhQ91suC0SzRyvmIsVEwp-UimklmCRGTVYzPheKhEU_TePBzy2eDM9ZqM2kRqQJJKy3MZNDSNAM_xd36j29ycFTt9FE_Vy-i1c5hHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید فکر کنید ایشان امام جمعه خارطوم در سودان باشد اما نه این مرد همان روبرتو کارلوس است که به دین حنیف اسلام مشرف شده و با یک دختر مسلمان به نام سهیلا ازدواج کرده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20007" target="_blank">📅 00:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ به مشاورین ارشد خود دستور داده است تا مذاکرات با ایران را متوقف کنند!
دولت ترامپ در حال فاصله گرفتن از تلاش برای "فشار حداکثری فوری بر ایران" و حرکت به سمت یک تلاش بلندمدت برای "تحمیل فشار" بر تهران از طریق فشار اقتصادی و نظامی مداوم است.
به نظر می‌رسد هدف، افزایش تدریجی فشار بر ایران است تا زمانی که این کشور تمایل بیشتری برای پذیرش شرایط ترامپ پیدا کند.
منبع: CNN</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20006" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h51aG1TbgTLg1CsOpvcNVosA7d5Wa6lUzeoo2CovkKXpP8wC93YigMlVENW7uMNOvBQTfn26TUcegQZeTlItrkDkTnAOk_wxfM-yF_XDGrqf4O6K5LGsjGcx2ANij80Sd9Y7S4252zmvoX-gIsYJtEq6d8bo24HD2n5PhLcZ29MLDa8VsUeN44BnmCq00SZ6z-I2cB_w_61KPQSW-NX9vf8pcS71l9kV49ngLgloSDzcEzGrF3uVg_riPuzADPhWWxBBsHjdNscprTMbvh620qcYEu_2AHoVp4lJUcQF_j4IzRpvJ0GS2qrjagu5HkP_t1xhzXaoMXHKtwO_DwY65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نتانیاهو:  اسرائیل و سوریه بر سر حفظ وضعیت موجود در مسائل امنیتی به توافق رسیدند، توافقی که سوریه در آستانه نقض آن بود، با اجازه دادن به نیروهای ترکیه ای برای استقرار در یک پایگاه هوایی نزدیک به حلب.  اسرائیل بارها به سوریه هشدار داد که چنین استقراری…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20005" target="_blank">📅 00:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دفتر نتانیاهو:
اسرائیل و سوریه بر سر حفظ وضعیت موجود در مسائل امنیتی به توافق رسیدند، توافقی که سوریه در آستانه نقض آن بود، با اجازه دادن به نیروهای ترکیه ای برای استقرار در یک پایگاه هوایی نزدیک به حلب.
اسرائیل بارها به سوریه هشدار داد که چنین استقراری تهدیدی برای امنیت اسرائیل خواهد بود. سوریه این هشدارها را نادیده گرفت.
اسرائیل تهدیدهایی را که امنیت خود را به خطر می‌اندازند، نمی‌پذیرد و از بازگشت به وضعیت موجود استقبال خواهد کرد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20004" target="_blank">📅 23:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امارات متحده عربی، تمامی مبادلات تجاری با ایران را به حالت تعلیق درآورد.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20003" target="_blank">📅 23:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پروفسور خوش چشم:  باید برویم آب های فلوریدا را مین گذاری کنیم ...</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20002" target="_blank">📅 23:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=SZ2PDftWp2HxRM4r-70eVGkWVaKuX_u_ivL2B7B6kEyGJDbV6OJN2aCncoyg5B-GxQuzeM4EOwgJpdv1umseOPV4CSR7UecI-3fPkW-OLcPeio6UKHym38DBiFanVWnq7HlJUhGKS3pBp8e33PRqS9HDlaY_xJ_mlru4wqOaz1yFnnHLrJclfbPV3ovvuVawRlmgtaCClkijDlcDdfntYzf9uE_j8mA2OemFCtbSMTsLvTHDVg-WJQV0biaCK8mAcME_5G29uZt7eeOQE2EfqSVcuBA9LB_vJTI8JDeatan7kyk3Cpy_00EzM9xsLPhDzQiPUA1XSVFAsa7z5u2qcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=SZ2PDftWp2HxRM4r-70eVGkWVaKuX_u_ivL2B7B6kEyGJDbV6OJN2aCncoyg5B-GxQuzeM4EOwgJpdv1umseOPV4CSR7UecI-3fPkW-OLcPeio6UKHym38DBiFanVWnq7HlJUhGKS3pBp8e33PRqS9HDlaY_xJ_mlru4wqOaz1yFnnHLrJclfbPV3ovvuVawRlmgtaCClkijDlcDdfntYzf9uE_j8mA2OemFCtbSMTsLvTHDVg-WJQV0biaCK8mAcME_5G29uZt7eeOQE2EfqSVcuBA9LB_vJTI8JDeatan7kyk3Cpy_00EzM9xsLPhDzQiPUA1XSVFAsa7z5u2qcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پروفسور خوش چشم:
باید برویم آب های فلوریدا را مین گذاری کنیم ...</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20001" target="_blank">📅 22:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20000" target="_blank">📅 21:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19999" target="_blank">📅 21:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujspRTDpdLJ7GAxBkGXuaXlWWUXFAJTqFAA_hsQapAfJr1X0Hdb8h_f-eFTk4FblleJyVoAdrV-OuIB4cgiC92fyjNS7m-YIXRpTBWSnLhcQDIq_7zoQrGNYpj4WOZLH-wFSl0Vhgu4GiKBV25cwtKOUiTYAJrrqcNgkHlY8A-kxLx-OQ13gr2aVy-Pl4MXkw4-afB-JtqBnPoU_vrDobVzbVszvJjKldBr8VHExS7zdkDv_BetYMB3V4yhJSmfaS9naPgehYgZoDrXikx_qc-k6MPDSKCfWhcoii7LBgrMIjdQGJQbRRxjIWAawY8rPIthsOd59Jth584JPh9bZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دردناک!
تادالافیل ۷۰۶ درصد افزایش نرخ گرفت
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19998" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یکی رهگیری شده و دیگری در آب افتاده!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19997" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد  : وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19996" target="_blank">📅 20:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد
: وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19995" target="_blank">📅 20:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19994" target="_blank">📅 18:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گویا حمله به امارات کار انصارالله (حوثی ها) است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19993" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19992" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات در بندر جبل علی امارات</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19991" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53cb17e6f7.mp4?token=JLJm8YnC_pL8ieq8Vgj4Uccft_ZdlKMMJZRvsKRzrYpetBq6VmjpRhlre9gnaWg9ztIkt0joo9-zv635Z6FqO6yL1RjN6eIM1DSvMEv-t7d5lEkgofOnQ36DCzoVeQS1Q3EoRcYwYEFkVv9sWL-W68hMq0zGlWq4u9p-NugLeH5EUG3UImIn8Nxs8hwb61zwX7wyIEi_sQcapOtcX-CYfOlFtuFQJwRxKfOi24_zNRF-h6i1bm3IDaCLMfyRVpfDRV9BBkWSpWmCeKADBAEz76LPvm6bBqNCqGSY84QfFt0UxeUKXHJQiFPUcbSJBOWVVoRjZmAsC8Lm8QIIl1Q1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53cb17e6f7.mp4?token=JLJm8YnC_pL8ieq8Vgj4Uccft_ZdlKMMJZRvsKRzrYpetBq6VmjpRhlre9gnaWg9ztIkt0joo9-zv635Z6FqO6yL1RjN6eIM1DSvMEv-t7d5lEkgofOnQ36DCzoVeQS1Q3EoRcYwYEFkVv9sWL-W68hMq0zGlWq4u9p-NugLeH5EUG3UImIn8Nxs8hwb61zwX7wyIEi_sQcapOtcX-CYfOlFtuFQJwRxKfOi24_zNRF-h6i1bm3IDaCLMfyRVpfDRV9BBkWSpWmCeKADBAEz76LPvm6bBqNCqGSY84QfFt0UxeUKXHJQiFPUcbSJBOWVVoRjZmAsC8Lm8QIIl1Q1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:   هیچ مذاکره ای با جمهوری اسلامی ایران در جریان نیست و برنامه ریزی نشده.   محاصره دریایی با تمام شدت و اثر باقی هست.   تنگه هرمز باز و در حال عمل است. تمام مین های دریایی هم حذف و یا خنثی شده اند.   از توجه شما به این موضوع سپاسگزارم، دانلد جی. ترامپ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19990" target="_blank">📅 18:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طنز تاریخ در این است که پیمان دفاع مشترکی که عربها با ترک‌ها بسته اند دقیقا ۱۱۰ سال پس از جنگی روی داده که میان خودشان در قالب شورش «شریف حسین» ضد عثمانی ها درگرفت و اتفاقا نخستین شهری که عربها آزاد کردند همین «مکه» بود که نامش اکنون شده لقب پیمان دفاعی اخیر!…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19989" target="_blank">📅 18:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19988" target="_blank">📅 18:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">— عربستان حملات اسرائیل به فرودگاه ابوظهور در ادلب سوریه را محکوم کرد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19987" target="_blank">📅 18:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسرائیل فرودگاه ابوالظهور در ادلب را با ۴ حمله بمباران کرد.   طبق گزارش‌ها، نیروهای ترکیه در این فرودگاه مستقر هستند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19986" target="_blank">📅 18:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
هیچ مذاکره ای با جمهوری اسلامی ایران در جریان نیست و برنامه ریزی نشده.
محاصره دریایی با تمام شدت و اثر باقی هست.
تنگه هرمز باز و در حال عمل است. تمام مین های دریایی هم حذف و یا خنثی شده اند.
از توجه شما به این موضوع سپاسگزارم، دانلد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19985" target="_blank">📅 18:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دولت تایوان به هر شهروند این کشور مبلغ ۳۱۴ دلار به عنوان «سود تقسیمی هوش مصنوعی» پرداخت می کند که ناشی از جهش اقتصادی این کشور به دلیل رشد تقاضا برای محصولات مرتبط با صنعت هوش مصنوعی است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19984" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کشتی یونانی در هرمز هدف قرار گرفت
کشتی فله‌بر «Minoan Dignity» متعلق به یونان، هنگام عبور از تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و موتورخانه آن آسیب دید.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19983" target="_blank">📅 13:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مادرقحبه ها این چه وضع اینترنت است؟!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19982" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">با پایان مدت تعیین شده برای نهایی سازی توافقنامه اسلام آباد، اسراییل حملات سنگین خود به جنوب لبنان را از سر گرفت</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19981" target="_blank">📅 13:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل فرودگاه ابوالظهور در ادلب را با ۴ حمله بمباران کرد.
طبق گزارش‌ها، نیروهای ترکیه در این فرودگاه مستقر هستند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19980" target="_blank">📅 07:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگر تن ندارید لااقل آماده باشید!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19979" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب رفتیم برای موج C از ۲ و چند صباحی دیگر فرصتی برای خرید تن و دلار و نفت</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19978" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPGbeS91tJdMTxF5eoSNSJutT8TWweaSxBd5Y8BzB5ggAjzDgNxuJulRQRbk2TmQiZ6MRZWtuYEKtmvjrKqHKsRrt7FKRsN9TsQPmBjl2ps6Hl8zlAo_PbCbFBZQ92XikERehU1w9kGm0m6nxSjV0Gv-IbVdG8pmL05V2bCCVFqmwGJC0na8DCXQi8WLVscdk3r7h9TNGVm6xwreMZmJsA-IFGBIPmxptIeGNrXIBXfOZ-L245ImaT8l355j22PHS98XvnZwzxxsnHwV2AHJiWD7cnlLmNi79qkwFY-wmgfZtsiWeOUQHuuKMcts77HkpZupzurrliHSVCgGakNLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19977" target="_blank">📅 00:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">محسن رضایی :
تا حالا زیادی صبر کرده ایم ، لازم شود از NPT خارج میشویم و خودتان میدانید این یعنی چه!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19976" target="_blank">📅 00:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfmoh3uZXMml0Mq6SfQthBS9msWHg27rAtbQ1a7DFjQOfPZwl0wYSCI2IdFv-dsANp8yYokCh6Tc7FhVFroBOEDNlKdbcIQ48LRDEZ1e7GkS98GsSAUGtCGPigNuuppDC7pj36SngXbd7ju0EVj2cY0XRSzUsGhHXrFEVC30p6D-7x8nwa4PfIUlJ8RXHT5jvqVhEVUMZHjQXi079Mtofriy2G2dJHS7z25u9wwmBOPCpltfDgo_yDYN6HQTr9vAngocIfp1V5a2swRihGaX_IYBWNUWG0FfQRfXkIH7xvAJjBGUH05dadYiipeyuPLqok5BzWTpAs8dy-AjtG8Cyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19975" target="_blank">📅 00:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جرد کوشنر درباره ایران:
در حال حاضر،  ترامپ بر فشار اقتصادی متمرکز شده است.
اگر ایران مایل به پایان دادن به توافقی است که آنها با ما در مورد آن صحبت می کردند تا از توانایی خود در ساخت سلاح هسته ای چشم پوشی کند، واضح است که او مایل است توافقی را انجام دهد که می تواند برای مردم ایران عالی باشد، اما در حال حاضر آنها هیچ علاقه ای به انجام کاری که برای ما منطقی است نشان نمی دهند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19974" target="_blank">📅 23:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxcp5n9_nTh_a_A3668nrYJTtCX5iwKGC37HXMzZ7CndBKhFWN-txgDqoC0tSigYS1lMmMNQRCIGCG_SDvKga7YMCLv6qnzZENhpZKD8-jiIkwH_TQxycGVSmyQYmmV-9Id6N1jAEfP8_d0xL9XY_IIXbxn-wLu83o_z_d-Hw_RVTqkaGfzD45YDd_TXLRjgFz88xAua4au7q2iIvdZqOFpDPiQtJeBbt2cWo9lrpmqwSnUAGEi2rWu9vXwFYw3HPqjP_6o_loE6v_XdH4Snfc4SQdT3qWyA1PnngNt6bVMhqgM1bByHnhxqGmkoByEFOyZfrflHuDPoGI4epFjJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19973" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ:   توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19972" target="_blank">📅 22:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ در مورد ایران:
آن‌ها می‌خواهند توافقی انجام دهند، اما قصد ندارند آن نوع از توافقی را انجام دهند که من احساس می‌کنم ضروری است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19971" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19970" target="_blank">📅 21:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:
توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19969" target="_blank">📅 21:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19968">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گویا سپاه رفته کشتی اماراتی را از دهن آمریکایی ها کشیده بیرون و آورده قشم!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19968" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19967">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ می‌گوید ایالات متحده تنها از «بادام زمینی» (استعاره از بخش کوچکی) از انبار سلاح‌های خود استفاده کرده است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19967" target="_blank">📅 20:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19966">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQv0iJu6AKkHEUUIP1Ru5MGZ9WvePO_VXeIkBKjEbGbVSLP_Js_vcOi0yRFFZHbvCRjVFtMXp-0JeOQhMe1ra1sA6YYWkvJJMye9sIyyW_5dG8LDO5R8Cn9jlVUw9_QmJ1NCaOpoVwRl1nUHpflh6kuEhlE6pfhDaycfN70M3yCEIWz_vR_Ug-jJzlUZ1EOOB4C5QiMTU9KLTNGnFB9kz0il18lMb9myWng6jhyQMuFAE1jZ4yovkxO_yrbQuT9qa8RpUlQRpPUtZlHL__vNH0N6-GhsW-yK5Ak90PNQ92onAfov2-AYLonj7H7lYAd7BLplhTkF0qurpYZjB1nRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم:  داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.  نفتکش امارات در نزدیکی قشم متوقف شده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19966" target="_blank">📅 20:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19965">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تسنیم:
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
نفتکش امارات در نزدیکی قشم متوقف شده است.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19965" target="_blank">📅 20:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19964">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک مقام ارشد ایرانی به خبرگزاری رویترز گفت که تهران از یک سیاست دفاعی به یک سیاست «کاملاً تهاجمی» روی می‌آورد و به ایالات متحده «چند هفته» فرصت می‌دهد تا توافق صلح را اجرا کند.
«تمام نهادهای ایرانی آماده‌اند تا در صورت شکست دیپلماسی، تنش‌ها را در تنگه هرمز و در سراسر منطقه افزایش دهند. ایران به طور نامحدود منتظر نخواهد ماند تا ایالات متحده به محاصره دریایی ادامه دهد.»</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19964" target="_blank">📅 18:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19963">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.   به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19963" target="_blank">📅 15:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19962">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.
به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات منجر به سوختن کامل کشتی و غرق شدن تعدادی از شناورها و سوختن بقیه شد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19962" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19961">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19961" target="_blank">📅 15:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcIJ-_XBC-OczDoRdE7Flrcz1bYpZqE6MjgzGtpwnDb0KIP9Se48fYvEzqHV5sBrQHi5tzHiOEQ44Pf6v__fro6wHOaFHygP79F7omySec0TlV9g0gNtrAEUA03E8fMFTNLlqGTM21llOazBrIBdD7JYaDtIl-pR9DezOAoB-1twc6OqBYXmcR2ZbvVKz0E3SYBASlLwSWpOPHMf2J2M9HJ9tpqOvrtwYqgZ8haS-u4ElwFGhZvZngDzsnoRLLx8H8aWaqDcJfE3IFDrWwVfU580grTy8jWOQnzMCxeqf54xMLGtMGpJHxvRSNLLVOgeRzJhXFZzIwBI3YrGaTniNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.  او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19960" target="_blank">📅 15:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.
او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19959" target="_blank">📅 15:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ به فاکس نیوز:  ایران باید پرچم سفید تسلیم را بالا ببرد. آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19958" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره ایران:
ما یک کانال پشت پرده با سپاه پاسداران  ایران داریم. ما مستقیماً با مقامات سپاه صحبت می‌کنیم.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19957" target="_blank">📅 14:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ایران باید پرچم سفید تسلیم را بالا ببرد.
آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19956" target="_blank">📅 14:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ایالات متحده و ایران بر تمدید آتش‌بس ۶۰ روزه توافق کردند
— العربیه</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19955" target="_blank">📅 14:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">درباره اینکه چرا ایران مداوماً مواضع تجزیه طلبان را در کردستان عراق می زند، یک دلیلش این است که توان ترابری نیروی هوایی ارتش و سپاه در جریان جنگ 40-روزه بشدت آسیب دیده و در صورت ورود زمینی نیروهای شبه نظامی تجزیه طلب، کار پشتیبانی هوایی و لجستیکی بسیار دشوار خواهدبود.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19954" target="_blank">📅 14:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه
وقتی روی مواد هست
گوشی دست نگیره
مرسی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19953" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTqZwOnCx50ZnCOITQakImZaMVjek119wewb9APEPCAAVNGQDNoSVW4Tupa0hCePsklcoOsL9XkKhzLSYlhEYkf-qiFMwKZdaLunmPFjNpFHFdXuYMCsjzFYAnPBzGi9oPHWAjZx7_F6hXoOUNaq5zFsMuD5AHJpilSH4fKleL8iPhtft8GZd7eZmC1Vfax5Oe9PS5bntCP0AS-TAwJvi8ECOs7OQjqFfh9YTY3E4iXTpJsABwxDdrGZ7KY6TLVvEpbs4m48PRuViX6mwujrw0YQ3XwBVPVZ3qCD5ClhsuQB7f4OF8y4K7E-hsv72XGS7e7mZMxDxBuKbu989g2TxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19952" target="_blank">📅 12:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnxqq74ARgDo238pEMdZw8QrOavfsQ3wz_s-H1AUm9rZxkIyDQbITgF9oxxjTG6pWEnVKw2EgIVLsCheKr1pjYCtjchylUi9b5HXz-Nj-FCRWcYj3AFJxCNJWyh6xlSXvH4XJQb7CfCYf5VOaLksKhjnOdxb47b7gAjvABqB2KdqwTPQocD1whe1GbbHY23Vb0I1ohzH-Jl_hBw8BChAvT6g7wGXdlPQsEkPkfY1il7B0KfK0pMm_E-Tut-vEQkcLCxJpK5XgokjBZqK7ezhMheW0--e10Dc-Z32UevmWmdWM0mg3QvxovXCrJji6A42nleK01vdHz9Pg1sEXLpWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/19951" target="_blank">📅 01:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHIogKXcDGVmi9ocnNajekfKY4Kho2HhxKlq0fPhzwBVytvNSLpgKHwU10EcGlhukYbERoUeXgV5nhkjHriseWR_5rpQ4kZY4NBFMMGT84Td9eQBVgrc4IEQvsBPBqjz_9jBU5ltGaCdcsfYPvcfmsOs9RpQGTTSJl6seXxDEkZEOKek-EpO0oygT3tRrE27HeriRyMvOHMjy9VxZUVzP0aIw59rVEk1tY6bNk1_Y7qJujbxXbRjbNc6wYz9j60zpkKmVqXE4B-Ih-akT2_bzETe_-6ItYXLB63VAQqIiuo_6BTqmbcAwHt4J1dWu4ThyjXLVUqExUxyU34oAsa7Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/19950" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19949" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/19949" target="_blank">📅 20:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا به پایان رسیدن مهلت 60-روزه در فردا، لزوماً جنگ از سر گرفته می شود؟!</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/19948" target="_blank">📅 18:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/19947" target="_blank">📅 15:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/19946" target="_blank">📅 15:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از فردا با حجم کاری کمتر فعالیت کانال از سر گرفته می شود.
سعی میکنم شاخص GRI دستکم بروزرسانی و ارائه بشود.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/19945" target="_blank">📅 02:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مدتی نخواهم بود...</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/SBoxxx/19944" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgrjVKSbOIoQzxvXYNGFGO2TRh0CojHiBBtAKo3qwt6qRTECtP3-PvofDqM8hUEd-IOL7IUN4Cl5PLHGs51MImMLdqyG7F6WXkp9h6R6pUp_1jEPJDvDPd9bvcKaomrvOoVnTUEnS_TguIUERcQizHKlCzX5vsdA7-XJYg-ie0aAIoJAtaMHMBNnhiG-HZuV8ZjUZmZ05CXaNqK31pR2cySCwq16wxn_up1_6LDKfHJ6IJMs3gXaXK2qkgCHmj6j54P-8t_SL7hRhkiY090tts2HVxNsO_BVPeodu6q74VQ-UkRFudANpt11NHUj2Tq2m-I1_BpaE8wWryKuAB7VNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه به دنبال تایید ایالات متحده برای ارسال ذخیره‌ای بزرگ از سلاح‌های ساخت آمریکا به اوکراین است!
این بسته شامل موشک های اتکمز و ۴۷,۰۰۰ گلوله توپ خوشه ای است که به گفته منابع، ارزشی حدود ۲۵۶ میلیون دلار دارند.
واشنگتن آماده تایید این انتقال است، اما سازمان دیده‌بان حقوق بشر از کنگره می‌خواهد که جلوی آن را بگیرد و به خطراتی که سلاح‌های حاوی بمب‌های خوشه‌ای برای غیرنظامیان ایجاد می‌کنند، اشاره کرده است.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/SBoxxx/19943" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چقدر خوشحالم جای پاکستانی ها نیستم؛
فردای امضای پیمان دفاعی با عربستان، یمنی ها یک کشتی سعودی را زدند که در اثر آن چند پاکستانی کشته شدند!
الان هم سه روز است میگویند ایران و آمریکا دارند سازش می‌کنند اما ولی خب</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/SBoxxx/19942" target="_blank">📅 14:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:   فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.   ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/SBoxxx/19941" target="_blank">📅 14:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آذربایجان در پی دریافت کمک‌های ایالات متحده در زمینه فناوری‌های پیشرفته برای پاکسازی مین‌های زمینی است.
دهه‌ها درگیری این کشور را به شدت با مین‌ها و مهمات منفجر نشده آلوده کرده است.
باکو امیدوار است که روابط نزدیک‌تر با ایالات متحده بتواند تلاش‌های نقشه‌برداری و خنثی‌سازی مین‌ها را تسریع کرده و بازسازی پس از جنگ را پشتیبانی کند.
منبع: آکسیوس</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/SBoxxx/19940" target="_blank">📅 14:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.
ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/SBoxxx/19939" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/SBoxxx/19938" target="_blank">📅 10:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/SBoxxx/19937" target="_blank">📅 10:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SBoxxx/19936" target="_blank">📅 08:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:  به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.  وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19935" target="_blank">📅 07:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2XE9I9P_FK7osQO_UUPMw0weJhxpnIjAPmskmXmupj086VS4PiNnDQzw7t_4cMKh8KPOw0e_70T4s-dQcm0VoLDnqgctVky88QdpH8qnrg3xJfar3mCfSYvkF-UGBulCHhaOlOU1k1j0St9VHC_IWI7RUHStETZn7j2-r_bSzDnkNcR_w-Zv9M54DNyM6uNSrFT_RaA3WmgtjwE1ew_UCU6A2cmx3lPLTivz29AXg_LHHuw5M9XX-akL94yZj65Ox0-n-_qYHbf1xCHcRqOHIRqcosAF_wQNF5En4cgZ6QG9PJFAm-2EqFzxDIB9ENOv5nicb5bVqtNj3hFSaVuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:
به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.
وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق خطوط لوله و تأسیسات صادراتی تازه ارتقا یافته از منطقه خارج می‌شود، ترکیب شود، مجموع جریان‌های نفتی در حال حاضر به طور میانگین حدود ۱۵ میلیون بشکه در روز است.
فقط در روز یکشنبه، بیش از ۲۰ میلیون بشکه از منطقه خلیج عربی خارج شد که این رقم بالاتر از میانگین پیش از درگیری است.</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SBoxxx/19934" target="_blank">📅 07:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SBoxxx/19933" target="_blank">📅 06:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SBoxxx/19932" target="_blank">📅 02:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19931" target="_blank">📅 02:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.  @PressTV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/19930" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=gUltliJHUEZKf0Mwg94Jo8aYnPe8olAM04sJg1vfaevxSiv1NY76F3pJBMrLip8SCN0s6VnBdocY58Mw5NBLRp3Y-2LB4cKpAp7ZP4um4UAHw-InVQ2KALwHx9GUDu3OKQyMAgBNCwByWEPvPqH90UFns-Gzyp7KdjoFuCZQGkc5hmt8hdw0u2WSQFW1i4_0ItziyM0L1dBQY_a6ompQ3NSwiZ5B8Pp3abJWepR9GJ1azmAeC4v8fH8HVGqHX_bNEo_-Al8p_er1TWGEh46LD59CRAGY7ntETLsQ3hKvPqtl9V3Edp2mnV9YVkeUDtJX5Vkl776h4zgg3vKtRl3OVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=gUltliJHUEZKf0Mwg94Jo8aYnPe8olAM04sJg1vfaevxSiv1NY76F3pJBMrLip8SCN0s6VnBdocY58Mw5NBLRp3Y-2LB4cKpAp7ZP4um4UAHw-InVQ2KALwHx9GUDu3OKQyMAgBNCwByWEPvPqH90UFns-Gzyp7KdjoFuCZQGkc5hmt8hdw0u2WSQFW1i4_0ItziyM0L1dBQY_a6ompQ3NSwiZ5B8Pp3abJWepR9GJ1azmAeC4v8fH8HVGqHX_bNEo_-Al8p_er1TWGEh46LD59CRAGY7ntETLsQ3hKvPqtl9V3Edp2mnV9YVkeUDtJX5Vkl776h4zgg3vKtRl3OVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.
@PressTV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/19929" target="_blank">📅 02:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDKSmVpSm8W3F9XUx5S2X1gUqvGPn3FJpAuvKLj9ClSPwMDbctDgyqoV6PyOUzq0WCeHKLLH9UH0-jVfpon_Ej934hpdrA57mGPE2x5e_YMgQ7Zys1N6gqoZ_wTo_vfEzwezrHT8_Uawk5pw075-ZtzpJysEpQsVYGsn1LH7DXEH6oZt-e1p-sIuq-Y8PFwAVxiUhD8nNb4nByOxBlhrguf35bECisNIdOs3yGpn-qNuNs8pNst0x67jEnxBF3GhMFFM4S1_cM_d9U45AjYdZm5DDmYFilpCfcy5U7PSBGXjxUWeJXdr0ij1YhNr0kOSInBSXx2MheJbdJdWp7ICxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19928" target="_blank">📅 02:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/19927" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این ترکیب و چینش سیاسی و نظامی خبر از جنگی شدید می دهد.  تًن ماهی یادتان نرود.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19926" target="_blank">📅 23:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اساساً به حمایت خاصی نرسید که برای خرید اقدام بشود.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19925" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGBxKdvFWA6XEZbexYLRUPsEtaCKXIOiQ0I6XroHFR1iguoFSBKAqBXjMoqofcUJ-SFyfkE3QnsFrNosDUWrO9L20C-ZvwxEWMxmsWDKxorAFY67BmV9os4BO18reRoAZ1G50ERXI2t-Oev2ZyKkh2-zodBLYifs_qi3OKUlNd2TzgDqlI1GN6OFCz_9x77-n3l7N9fBzoLDiCV5DRDiYL6n4w9RtDSl4TCKvxLH1rsFjzXrFvraZmA7EDFPRFde-QYScDQc6EeAx3WjkOFmm08kDsVzZH-4Nub63gxmRuY0ls59Rd34jpb3ZK_GK4DM5Q7BNhaDPoKB68P-n2iwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19924" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19923">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر   ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/19923" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19922">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گریدم به اسلام آباد و توافق ش. نفت را دریابید.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19922" target="_blank">📅 20:51 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
