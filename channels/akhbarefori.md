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
<img src="https://cdn4.telesco.pe/file/XPfkhj0kr-pFMsqxHFhiW86i4nohER_4qs0rNvfIfJ7Y4uODZc0h_JfhFCDWGWliVyohipV4gQT-srIpscBC3juU5lMpEVvgara4x0kxuaYMge6VZQduQ1afOjdL1H3EyoF-K3eqlDjv9QtNmLIQ37t1pl_AAyazE-63qQ-8NKMhpmoCKXKCFRPRI9EFRoF8R9KJb9o8PFTQavLRX9qDns0SP9P-tYA4-12hOo83P5rVQP-1ezg3ewjsKBMUKtpP-m-ATvg1vlRwvQOaNW7C5g7EjYy88upx5hu18ekpPfdE4wfXljXWjW6dFxEnHvrzQW8T3mZ2SS6TAalnmz2bqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 05:43:16</div>
<hr>

<div class="tg-post" id="msg-684120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM7A3AhkcKuxCANAlbDQJNn0EWdRPRxaTlIMY4n03stfQuqoMz6-BSuL1o18unEr-e-cirCbdppXo6tNbiPjau9pW9bzv4X_bdzh_PDqqYutDQbKaF94QuL0c22r9XMAU6ye5IgB1ukwyEQ6jm4Ol-IDP8Dmypws4I7tJfQM3y1lSazxiOuIoAAPeOr9LBzv3bjLHozoO4_RbWHjjvFtHgDFZSzigff0VMbEaThdJa2HinxEKLlmOUx52gspQIYc7L8O5YHb-22F6_ggULAYA6q48JukNU_xi6FRVyOCiMU9NEzReHzwlKUR3HmFSM_SZG67zhre0fAG7xEifaH-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
۵ آیـــفــون ۱۷ پــرومــکــس جــایــزه بـگــیــر
مجموعه
ســــرآوا
در بزرگ‌ترین جشنواره خود ۵ دستگاه آیفون ۱۷ به کاربران هدیه می‌دهد
📅
زمان مراسم قرعه‌کشی: ۲۷ شهریور ۱۴۰۵ هم‌زمان با روز شعر و ادب فارسی و بزرگداشت استاد شهریار
📍
مکان:
مرکز همایش‌های بین‌المللی جزیره کیش
کافیست وارد سرآوا شوی و شانس بردنت را بسازی
همین حالا شروع کن
👇
@Sarava_Finance</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/684120" target="_blank">📅 01:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwv7Q6k_13QhPJExip6CoQLztGYjEsI-iGb18WKw7YVC_gt68_PiKV8c0yVpoXpHs7YUkZyjvbbMcfISM2oyfOKlkq-SlEq3LDoEPKsR3ko9Dunn0_Uby-DpmwO6e1whjIIjOnmK_hX6N_mPrdP9sdhT35GeA5cHIv0appaGC55B9CRcgLDG2Rh8w23V8hSkgGIwJ26KZ6GMzCOX8tGx86CksY9yneZg6MH8joZGo0RqX1ZxGdtLnDVLOSk4bJSMwcJbiD0neDCjIKVnBTkxZtG9ZDby04k7_kXHx3IRl6f43ziR1WwlPM_dTCWbJDcWdbn4XiKmoSSrLJsWlPoI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و
عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/brief/41275/180124/</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/684119" target="_blank">📅 01:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تأکید اندیشکده آمریکایی به نمایشی‌بودن تحریم‌های جدید علیه ایران
🔹
عضو ارشد اندیشکده بروکینگز با اشاره به طرح ادعایی آمریکا برای تشدید فشارهای اقتصادی علیه ایران گفت: طبق انتظارات، این طرح چیزی جز یک کارزار تبلیغاتی و پُرهیاهو نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/akhbarefori/684118" target="_blank">📅 01:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6_LdznMtw4UQxNHrpdwaBrABHNHSXFXxikgXxx2j-DVApsCensHcFPeT35O8AhMIA5x47-Ar7R4iG8XGa5Z8JYAIxo_uGVJ_CyrDk2YdSz4L2OLOLbS5mMbFv2sPZpwGc7ir3YTVZIAeNeHVuy3hlDrpoWmDkRMBTnptDOuFQbyesQFOcGCt86GFR002cynB4FXtKdWcXi1P9Csq4wY5KTTz0XfQowhbPsj_MaddSX0oHSG1FiIPFBjRW3gVmvBRhHhh6ctFTh18s5Bk1houDtS9sxok3UqBHvlf9Jfr6pOqt2CCmbEbcPZRVZFiWV0mfUDtwB-4KBQmRWQTjdItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82af1dfb6c.mp4?token=DZhENg8Tai9mXjrL4IcnOcRFPz8bb-TIjHylIgPg4DDc-XsK2aztG2DfUMrzjlh6HsEaSagleWOtI_snK797TcuT-yWsbb_EG46LhJPPH-qe4kt7aO36dxxL53TvIY9wxjYNuazt1uM995OjxK2YE2b2f5_qkxCS8SQzySRY662bdMZ0v-t6_RASjSX_GKu1jEAJJKHVONyqn90hZwDyui2FuBqxdeExyNEdIWJ2iA9K3_ekSi-J0a9dL5pG2kG0ghh2LAvu-VXq8VeB7FvsNlN_fAvbr5vLKfxw2JPX2_hdMGMHsmQ_9MHxEb-X6A_UlmmqCT1zABWhSG5P3IQk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82af1dfb6c.mp4?token=DZhENg8Tai9mXjrL4IcnOcRFPz8bb-TIjHylIgPg4DDc-XsK2aztG2DfUMrzjlh6HsEaSagleWOtI_snK797TcuT-yWsbb_EG46LhJPPH-qe4kt7aO36dxxL53TvIY9wxjYNuazt1uM995OjxK2YE2b2f5_qkxCS8SQzySRY662bdMZ0v-t6_RASjSX_GKu1jEAJJKHVONyqn90hZwDyui2FuBqxdeExyNEdIWJ2iA9K3_ekSi-J0a9dL5pG2kG0ghh2LAvu-VXq8VeB7FvsNlN_fAvbr5vLKfxw2JPX2_hdMGMHsmQ_9MHxEb-X6A_UlmmqCT1zABWhSG5P3IQk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش طعنه‌آمیزسفارت ایران در آفریقای جنوبی به گزافه‌گویی‌های وزیر خزانه‌داری آمریکا درحالیکه بدهی آمریکا از ۴۰ تریلیون دلار عبور کرده: مهار کسری بودجه توسط وزیر خزانه‌داری نادان آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/684116" target="_blank">📅 01:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قشقاوی:
همان جوانی که پهپاد ساخت، می‌تواند اقتصاد را هم متحول کند
حسن قشقاوی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی در
#گفتگو
با خبرفوری:
🔹
همان‌طور که جوانان ما در حوزه آفندی و پدافندی نظامی توانمندی‌هایشان را به دنیا نشان دادند، در حوزه اقتصادی هم باید بتوانند این توانمندی را نشان دهند و آثار تحریم‌ها را خنثی کنیم.
🔹
همان جوانی که پهپاد ساخت، می‌تواند در اقتصاد هم خلاقیت و توانمندی خودش را نشان دهد، باید بستر حضور جوانان در اقتصاد فراهم شود.
🔹
اگر کسی ۱۰ کارخانه دارد باید تشویق کنیم تا ۲۰ کارخانه داشته باشد و اگر ۲۰ کارخانه دارد بتواند ۱۰۰ کارخانه ایجاد کند. نباید در تولید محدودیتی ایجاد کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/684115" target="_blank">📅 01:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9872e711e2.mp4?token=paBRwtuB69F503kpVPuQ93OXGbcPUk1Qhfvn_Wk414vlpAMlxuj61td6P4qk7PSFQjWKqxn9hykF_CH-3mtbQX2smamxABOUu3-Np2Q5q-E64qhRgnLrJZAniUCTX0PGH4XjNcGTzj8BkiD24y9TxOZXSHYvwkNiEgXVD5qwvfgxi5LRUmwoQ_i-N8MfOtY4ID6UXEFbqmkBYAReF17jSR8e_qQ2TAzLa_tjz8SzttkVtMkcyTljGUxQZTJK5a_Jo7n_0MFbDahi0lG5IgYNUyBinG3wbuwfuetKW9RZUqClyPvxQ4lEyujBica3rUI7ef6errdfsf7RRZXobwwxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9872e711e2.mp4?token=paBRwtuB69F503kpVPuQ93OXGbcPUk1Qhfvn_Wk414vlpAMlxuj61td6P4qk7PSFQjWKqxn9hykF_CH-3mtbQX2smamxABOUu3-Np2Q5q-E64qhRgnLrJZAniUCTX0PGH4XjNcGTzj8BkiD24y9TxOZXSHYvwkNiEgXVD5qwvfgxi5LRUmwoQ_i-N8MfOtY4ID6UXEFbqmkBYAReF17jSR8e_qQ2TAzLa_tjz8SzttkVtMkcyTljGUxQZTJK5a_Jo7n_0MFbDahi0lG5IgYNUyBinG3wbuwfuetKW9RZUqClyPvxQ4lEyujBica3rUI7ef6errdfsf7RRZXobwwxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس سی‌ان‌ان: ایران آماده مقابله با تهاجم اقتصادی آمریکاست
🔹
شبکه «سی‌ان‌ان» در ویژه برنامه خود در خصوص جنگ اقتصادی آمریکا علیه ایران با «جاستین وولفرز» استاد اقتصاد دانشگاه میشیگان و سرهنگ «سدریک لیتون» تحلیلگر نظامی گفت‌وگو کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/684114" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrUxArsxXAh0oMR9GFgMTBkLcJSdnhG-ugjTgg2AHokSPOIxnejqpr0q4WdhvCw827lBbhlK6_Cq8W2amt7by3yJrbTehOC5Co-6FkGHmlKif4ptDPnnNiHCqeMAUvxJQsihvuvXi-iG3InIlGbvMCnQyxoROMVoarkwwf52YT6Jh_vdQOMmbzC1JE3e1gpA_4d6losGpquSDMnnpmFnDkOtTTss3mj7YXG9Gc_k49pzFnGaDkeaB-0uQ64721giYWgqGvAE4PrRQ_he27GLX5-v2TT-d1v16kL7Nb32YDP2uDasQz8rcQyPfsbgSQiJVuLq-2ZHpq1Oeg-s-Rln1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی، تحلیلگر سیاسی: در جریان دیدار آقای عاصم منیر و دکتر قالیباف، پیش‌شرط‌های ایران برای بازگشایی تنگه مورد بحث قرار گرفت
🔹
میانجی پاکستانی، ضمن انتقال دیدگاه دولت ترامپ، موضع ایران درباره مسیر پیش‌رو را دریافت کرد؛ نخستین گام در این مسیر، اجرای این پیش‌شرط‌ها از سوی آمریکا است. به احتمال زیاد، عاصم منیر اکنون موضع تهران را به واشنگتن منتقل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/684113" target="_blank">📅 00:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEwAJ_etfMM8nR2dX8qOSSzd_kQtp3dT8g6NUeqir7P8sqr_jWrIwn5qx3Oku6MGX2B9YdRbTwyBsYsKrCT0kL07K-QpBpTaGfsRjTgYdJZFp0tzN4BdZ1KaE30WNSFTUKofPDEC5-f7P70QRqHL8XUprwWtfNThun5yi5l0U3w3nRR6UACOre1WUn-RnB7Sq9WK5I0fJoiYkDNMYTnt4kHpOK_7mOo0him4FNgDPQEFVk36hJ78dWrt2Mf8QAY546_vAkiJHtsppDtl9YrDsVdMY3FDG9CodUsPkGTJzdPtOjg9oedk9g3vRXGNm00AORdhRfL7nrU0MsMqXabSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه GBC:دونالد ترامپ در مسیر تبدیل شدن به احمق‌ترین رئیس‌جمهور در تاریخ ایالات متحده قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/684112" target="_blank">📅 00:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LALPFwJcS-Blpaz8mizV7SDurVc4u0XHfyaEGylED0BnnnoGwqXZWKT5F0RrmZzfVkdLEvQAGxtJnhzy6XLjqJXTEavGThONcYHkendu66l6XEr6o0rksozeD-90Qto3BMu6BoXNdVwQZFsTjFczpH781uIhRiVRVzfQPhgfLDlBv8spzMQ5wh3gkSGZ6WsnPi9FcuxqFFSgg13N_1L60Z1pCsTFsEA8tkavuCCCgQksGE2hCvffOGJUZ3CWgI4IZXKMjKL6VhR9p9oqkeN32SIMbPhZmjHRHEBHcgUiZgVsGuq13B262lg-37QLrsM50ugSCIdyyIrIt28jxDMRoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنسا: جنگ در ایران به ایتالیا ۱۲ میلیارد یورو هزینه ایجاد کرد
خبرگزاری آنسا:
🔹
ایتالیا اعلام کرد که با جنگ در ایران، ایتالیا با هزینه انرژی نزدیک به ۱۲ میلیارد یورو روبرو است.
🔹
افزایش هزینه بنزین و گازوئیل را در دوره شش ماهه تقریباً ۵.۸ میلیارد یورو تخمین می‌زند. هزینه سوخت ۵.۸ میلیارد یورو، هزینه برق ۳.۸ میلیارد یورو، مشاغل کوچک بیشترین آسیب را می‌بینند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/684111" target="_blank">📅 00:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: گزینه نظامی در تنگه هرمز محتمل است
🔹
وزیر جنگ آمریکا با اشاره به تنگه هرمز مدعی شد که واشنگتن استفاده از نیروی نظامی در این تنگه یا هر نقطه دیگری را منتفی نمی‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/684110" target="_blank">📅 00:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
اعتراف وزیر جنگ دولت تروریستی آمریکا: تردد در تنگه هرمز خطر پذیری بالا دارد  رویترز:
🔹
پیت هگست وزیر جنگ آمریکا، در جلسه توجیهی درباره جنگ علیه ایران گفت: تردد در تنگه هرمز بسیار محدودتر از آنچه همه می‌خواهند در حال انجام است.
🔹
او در ادامه گفت: این تردد…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/684109" target="_blank">📅 00:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmpbAsjfrCCN1dR7G8QBvPwVPWO8S270M6xV9E-hvs_QiiiB2tdXNe53YusnwB2WVveZ5upgayRTk6AUvcYfb1lCbHNnnnafZvvZsy5wds6h1lrC2NM9j8rrY14raj46W-Gr58GENI7lu_JbBBfNO2IztcvYOBYEPg2MTaDpa-Q_mOWZQiLofP7-0vIrofypesc-Kx4_xrYABMIgb7pXC9C8dSOtW4n3LtPI1BZHbFL5DV9hwLxXEqdoebYdw8knEa_rWZMOvYQG_i_D_4-U1RqlSYXo50Cr_4HzEXMYx7Ax1qYg72Khwga1txYmx_ZNyaRYdTU-fDV5RbWcuSbCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از ترک سیگار چه اتفاقی در بدن می‌افتد؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/684108" target="_blank">📅 00:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZo0wFzpbKnOptJuRc8KzS2Ohbot3_dzlp8HxMbs8qWyTPBKe0gcODkn1v5M56xeZLA6e_AHq1-Ej0K7SXLeMKCaEBIRVqMZ9BFpQF6xrDUhx0appm3ob5CgSetKTnSan5RD05BqE1kTtqB1AC5InkLYK7D52f3EPJScQhUuFBf0q1nC5fEQ7e0TNgpSfS8cueadMxczD5iKTNHUaQeluSGQBE_MuoSptUSXmBSSHvqQRTw1LhwlDXHehL7M0sSaYm5gzDRlepogaitlREyCknuiaHP1acvQfAsUiE3OlUjxzx3K6gvfZTmeCOh5GAK1p4HMer5Qkwc9CrbpcREz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/684107" target="_blank">📅 00:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وزیر اقتصاد: تفاهم‌نامۀ اسلام‌آباد روی کاغذ نکات مثبتی برای ما داشت اما اسرائیل و تندروهای آمریکا نتوانستند آن را تحمل کنند
🔹
امید داریم همان تفاهم‌نامه یا بهتر از آن احیا شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/684105" target="_blank">📅 00:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چین از جنگ ایران و آمریکا سود می‌برد؟
حسین قاهری، رئیس اندیشکده مطالعات راهبردی ایران و چین در
#گفتگو
با خبرفوری:
🔹
چین از جنگ ایران و آمریکا سودی نمی‌برد، شرایط فعلی باعث شده چین از ذخایر استراتژیک خود استفاده کند و برخی پالایشگاه‌های شمال این کشور فعالیت خود را متوقف کنند.
🔹
ایران ششمین صادرکننده نفت به چین است و چین ترجیح می‌دهد نفت را در شرایط عادی و با قیمت مناسب‌تر خریداری کند، بنابراین چین برنده این ماجرا نیست.
🔹
چین در کنترل قیمت نفت تعیین‌کننده است، استفاده چین و آمریکا و ژاپن از ذخایر استراتژیک نشان داد پیش‌بینی افزایش شدید قیمت نفت محقق نشد و این کشورها با این اقدام از نوسان بیشتر قیمت جلوگیری کردند.
🔹
اشتباه اصلی ایران در پنج دهه اخیر عدم تعریف روایت مشخص از مناسبات با چین بوده است، در حالی که کشورهای حوزه خلیج‌فارس امروز روابط قوی‌تری با چین دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/684104" target="_blank">📅 00:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تکرار
حملات توپخانه‌ای جدید رژيم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حملات توپخانه‌ای جدید ارتش رژيم صهیونیستی به منطقه «دوحه کفررمان» در جنوب لبنان خبر دادند.
🔹
منابع لبنانی همچنین از حمله توپخانه ای رژيم صهیونیستی به منطقه«علي الطاهر» در جنوب لبنان گزارش دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/684103" target="_blank">📅 00:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تغییر استراتژی سهامداران در بازار امروز بورس
🔹
در بازار سهام امروز  ۵۴ درصد نمادها در محدوده مثبت به کار خود پایان دادند. نکته جالب امروز این بود که سرمایه‌گذاران کوچک حدود ۱۰۰۰ میلیارد تومان از صندوق‌های درآمد ثابت پول خارج کردند.
در مجموع هم ۸۹ میلیارد تومان از کل بازار خارج شد.
🔹
با این حال، ارزش کل معاملات خرد به بیش از ۴۲ هزار میلیارد تومان رسید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/684102" target="_blank">📅 00:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اعتراف وزیر جنگ دولت تروریستی آمریکا: تردد در تنگه هرمز خطر پذیری بالا دارد
رویترز:
🔹
پیت هگست وزیر جنگ آمریکا، در جلسه توجیهی درباره جنگ علیه ایران گفت: تردد در تنگه هرمز بسیار محدودتر از آنچه همه می‌خواهند در حال انجام است.
🔹
او در ادامه گفت: این تردد  با خطر پذیری بالا  در جریان است.
🔹
هگست دلیل این خطر را  قایق‌های تندروی کوچک ایران عنوان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/684101" target="_blank">📅 00:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1F9KHhQ7xVBF5Yv31RvKkrRRH57hZ0LdrrOdT-mQ7WfvXiIjNS78LM2eZcSNkdzlufvcA-T89gqI5YoejyEUIJ5074owUXtlbldV8coJwrLKB-tvDrsmN0FnzVJA5eTj1eP4JEEn24uTqbtPpFpC1FVmAYgFCJJQR3LQwPtlN3-_GE7TJmp6N-_fUblN0ArZPUjTW7XFm9EIlihDx_kwt1Ebk7uRzmLqmIr2HIS4gr_g5i2KE7Vd-Z3dxx7r16-Xym_5AFyJx9tUX_y03O6eV2Dy-0h5pZIORqrS1zZ6fgwYer75Py6LN_Fyp_zgVy6_kXVpc1OMCleMEkytixolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/684100" target="_blank">📅 00:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crklh0DdEPn0giZeFLkFkY4x6IUIxOOGHXjq2fJzrmXH_0BLBdxx-KoJlyIRjjLUd4_LIesN9EDclcEp-Y455wIoy3H-5f3DltWgbO1dU_ojU4TBe9sXIolSZ4vR4UdgVIEGM0shU5JM5egyhPnFPBEo4b6CmltnJc6gFw-vpu641Lk1qr6CIImJmEm1bepGGf3ICt6RnSuXWNfGycVSTJrMUm0vcOZXnm8C0muhjDLiCsGs22rWw92AN_zItLebBcuJpOI4tlRopzA9mspwd7IWKhBnk53P4uNGtCrKBaYG186lTxrDv1jJJ0BwSvAeSd87R8wpOlr5IrXhM9qBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صمت: فولاد خوزستان یکی از قطب های اقتصادی کشور است/ سرعت بازسازی در این شرکت قابل تحسین بود
🔹
سیدمحمد اتابک روز دوشنبه در حاشیه بازدید از خطوط تولید و روند بازسازی خط تولید فولاد خوزستان پس از حمله دشمن آمریکایی-صهیونی، با گرامیداشت یاد و خاطره شهدای…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/684099" target="_blank">📅 00:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/472a78c05a.mp4?token=BfBX2YEK_tSsX6Eb6KCFp8RbZMFTWH2Q7pVxzVeVV77Q4sLDWaEVboa071fKCT9ao1EF7FuSKskzOtziUUpWLfcd4mL7u-iP3yVI4QmUK6aXZJd40t8W7SAcacrcVZNOaj3cBxXXTXFvoBnfCT47D4k40NDVPvTQxRXaMivvij5O_pAz7T1Z-x-uqcYUP6_ypE95g-J8H-eDiizAMLPqFypixGpZKgE3R1sOmsV5p22oSgy9w183r8ThSI9FQL0ePWk8qRGhLjhUdC1CumxzPLBWOZu6RcuFtEE-3ohPJkQJ0YggnhQKRIjn6Vj9zD9jODhxsa4BI53FYitEJ1qjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/472a78c05a.mp4?token=BfBX2YEK_tSsX6Eb6KCFp8RbZMFTWH2Q7pVxzVeVV77Q4sLDWaEVboa071fKCT9ao1EF7FuSKskzOtziUUpWLfcd4mL7u-iP3yVI4QmUK6aXZJd40t8W7SAcacrcVZNOaj3cBxXXTXFvoBnfCT47D4k40NDVPvTQxRXaMivvij5O_pAz7T1Z-x-uqcYUP6_ypE95g-J8H-eDiizAMLPqFypixGpZKgE3R1sOmsV5p22oSgy9w183r8ThSI9FQL0ePWk8qRGhLjhUdC1CumxzPLBWOZu6RcuFtEE-3ohPJkQJ0YggnhQKRIjn6Vj9zD9jODhxsa4BI53FYitEJ1qjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد احتراق خودرو از پمپ شدن بنزین تا خروج دود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/684097" target="_blank">📅 23:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
جنگ ایران روزانه ۶۰۰ میلیون دلار به گردشگری خلیج فارس ضرر زد
🔹
بر اساس گزارش شورای جهانی سفر و گردشگری، جنگ اخیر ایران باعث شده کشورهای عربی حاشیه خلیج فارس روزانه دست‌کم ۶۰۰ میلیون دلار از کاهش هزینه‌کرد گردشگران بین‌المللی ضرر کنند.
🔹
نکته عجیب‌تر اینکه حتی مقاصدی که مستقیماً درگیر جنگ نیستند هم با افت تقاضا مواجه شده‌اند. اگر این روند فقط ۳ ماه ادامه پیدا کند، بین ۵۰ تا ۶۵ میلیارد دلار از گردش مالی صنعت سفر منطقه ممکن است از اقتصاد این کشورها حذف شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/684096" target="_blank">📅 23:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4245e3c81f.mp4?token=M7fQXCU_ddZLXlfJ5dtjdsy5ND3Q0NFgUHaGb5uC-zfafNqubk8q11NS1bYR7lIn7Ldc-HlxIoTb4rJi62duAxRO_wsCx8q1hRgfkh82pzu6Wnh1NkkHeA-zgsRjkWNcdz-045kI6vbgQZb7v88_LN9oU22mJ7ZFri5WwlVakjesDhPUyS_eu4joFiukvdBqTrrtozyurpn9Lj3RexozK-iHyGlIbrqf_oAhQeqWaIgBSyeibW3zxfnUmrVVE-H59CciibVROClRNOPicrzSUdxnj0PB7BPb0xCYOqpLY_Yw5MzOcBuqgCXSGfjYNN5C4zX1vfN0wJy81wN0crjlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4245e3c81f.mp4?token=M7fQXCU_ddZLXlfJ5dtjdsy5ND3Q0NFgUHaGb5uC-zfafNqubk8q11NS1bYR7lIn7Ldc-HlxIoTb4rJi62duAxRO_wsCx8q1hRgfkh82pzu6Wnh1NkkHeA-zgsRjkWNcdz-045kI6vbgQZb7v88_LN9oU22mJ7ZFri5WwlVakjesDhPUyS_eu4joFiukvdBqTrrtozyurpn9Lj3RexozK-iHyGlIbrqf_oAhQeqWaIgBSyeibW3zxfnUmrVVE-H59CciibVROClRNOPicrzSUdxnj0PB7BPb0xCYOqpLY_Yw5MzOcBuqgCXSGfjYNN5C4zX1vfN0wJy81wN0crjlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایگاه زن در خانه جایگاه مدیری‌ است که از قضا ریحانه هم هست
🔹
این جایگاه اساسا با هیچ جایگاه دیگری برای زن قابل مقایسه نیست نه به لحاظ دنیوی نه به لحاظ اخروی... #چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/684095" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7d2ca1f69.mp4?token=pNR2IE8-KMSJzDUamUiR1xJfqy_CgTr0Y4dg6-RWPMsirUFhcmf0cM-fcL_RrAATkzSokXkce0hPwwB4xeNl1Zn8n-UTbAHVrGlhfrxPTW-BP0HDbjV8CJvV957nw6MsQgaO2V_-BvCefrNlzYYrsZ0pR1KnuYsU2gSOLPdHOdl1WfppUrUMRM7OvIzKnA473NKrNSnrSk35htc1nl3xY8UI3E3rvyzeyVGn_y34ZyzMVLpvhMaqMMZMXkCKLIq7qXbL7D4cp693rjq5CF6yw4BBPb-eiyZoQ3ycf22BEtdA6WRanGfqcuum3IlpOcR1eflQQ1Wvms1M5czLLvpJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7d2ca1f69.mp4?token=pNR2IE8-KMSJzDUamUiR1xJfqy_CgTr0Y4dg6-RWPMsirUFhcmf0cM-fcL_RrAATkzSokXkce0hPwwB4xeNl1Zn8n-UTbAHVrGlhfrxPTW-BP0HDbjV8CJvV957nw6MsQgaO2V_-BvCefrNlzYYrsZ0pR1KnuYsU2gSOLPdHOdl1WfppUrUMRM7OvIzKnA473NKrNSnrSk35htc1nl3xY8UI3E3rvyzeyVGn_y34ZyzMVLpvhMaqMMZMXkCKLIq7qXbL7D4cp693rjq5CF6yw4BBPb-eiyZoQ3ycf22BEtdA6WRanGfqcuum3IlpOcR1eflQQ1Wvms1M5czLLvpJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
صداهایی از جنس واقعیت؛ روایت بی‌واسطه شما از دغدغه‌های مالی، فرهنگی و اجتماعی در مسیر تشکیل خانواده.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/684094" target="_blank">📅 23:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ترامپ قمارباز: کانادا باید خود را با مقررات آمریکا وفق دهد
🔹
ترامپ در اظهاراتی درباره روابط اقتصادی آمریکا و کانادا گفت بخش قابل‌توجهی از برق، نفت و گاز مورد نیاز کانادا از طریق ایالات متحده منتقل می‌شود.
🔹
او با لحنی تند خطاب به مقام‌های کانادایی: یادتان…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/684093" target="_blank">📅 23:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ارتش اسرائیل: به دنبال رصد تحرکات افراد مشکوک، عملیات پاکسازی را در مرز با اردن همراه با مسدود کردن جاده‌ها و محورهای مواصلاتی آغاز کرده‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/684092" target="_blank">📅 23:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال گرانی قهوه؛ واردات به مشکل خورد
حسام ربیعی نایب رئیس انجمن قهوه کشور، در
#گفتگو
با خبرفوری:
🔹
واردات قهوه در شرایط جنگ با کاهش چشمگیر مواجه شده، مسیرهای جنوبی به‌طور مستمر دچار اختلال است در این مدت واردات قهوه از ترکیه، عمان و دبی و مقداری کمی از عراق صورت گرفت.
🔹
پیش‌بینی می‌شود با ادامه روند فعلی ارز و مشکلات واردات، قیمت قهوه در بازار داخلی افزایش یابد، هرچند کافه‌ها تاکنون سعی کرده‌اند با جذب هزینه‌ها، از افزایش شدید قیمت جلوگیری کنند و قیمت را زیاد افزایش ندهند.
🔹
پیش از جنگ حدود ۸۰ درصد واردات قهوه از امارات انجام می‌شد، بخشی از بارهایی که در امارات بودند به عمان منتقل و از آنجا به ایران ارسال شدند، همچنین حوادثی برای محموله‌های دریایی رخ داده که روند واردات را مختل کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/684091" target="_blank">📅 23:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c028896191.mp4?token=sC7mfXloN-vBYKHDnV52HNTevEm4wAKH-kXo_WJiJePkhWLAyAwv_HXawtz9iB8CvvesFUKoseisSwOtFE7kfbx-QVD1jqsHuvqeZR6kH3CrPmLVEPcAzTmiY3RTEJkSD39UY8hcmzcy6L7aximcVsHV35pzWWbnrkfAv7vq9Y5BsUf71O4kcCs7X1E2skLQeUt9WdiLt1UvF8t-ihTyV9GWG2fa_jLBRj81R_EQAIIofNrZ5hojLMoKtrpcill3O45wGsbXivhV23PipLooVReSPM47TaGq19F7kpQttLk-YLNj8SKovxhqnIZJOiYFZp9B4J0trJ4L2mj05zVPz3ynlRlM-9VIn68Ygi1NLTq0LW0VLRqK7qs6Tx4DPLZj7BZyDTpOTRcnA9tqcwlSbnicJKvRoajA7Ib82-9zEXaxFYHwehtXJ4oYrftrreKeEZHE2St_yIcizcOs9WPq50nd5gzGQLn0SxXmJK4juldfZfX960PGmtFJMgrEmqX83wh6ygyUpcT4CwQRPBuJ6aPMtqqulrGgP2mfvKg_15gJO_eUxgE0QZu5pz2id5u_by_7kOxXaAZcveTx-aG1E8AKb-Ti4mtbx-ZIZGhhmToEV1l_vZWG1efsmI-mWGxE1jfHKDKBr0L88VbBhoVYy1lJ88r5aLHi9uFtUZdrcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c028896191.mp4?token=sC7mfXloN-vBYKHDnV52HNTevEm4wAKH-kXo_WJiJePkhWLAyAwv_HXawtz9iB8CvvesFUKoseisSwOtFE7kfbx-QVD1jqsHuvqeZR6kH3CrPmLVEPcAzTmiY3RTEJkSD39UY8hcmzcy6L7aximcVsHV35pzWWbnrkfAv7vq9Y5BsUf71O4kcCs7X1E2skLQeUt9WdiLt1UvF8t-ihTyV9GWG2fa_jLBRj81R_EQAIIofNrZ5hojLMoKtrpcill3O45wGsbXivhV23PipLooVReSPM47TaGq19F7kpQttLk-YLNj8SKovxhqnIZJOiYFZp9B4J0trJ4L2mj05zVPz3ynlRlM-9VIn68Ygi1NLTq0LW0VLRqK7qs6Tx4DPLZj7BZyDTpOTRcnA9tqcwlSbnicJKvRoajA7Ib82-9zEXaxFYHwehtXJ4oYrftrreKeEZHE2St_yIcizcOs9WPq50nd5gzGQLn0SxXmJK4juldfZfX960PGmtFJMgrEmqX83wh6ygyUpcT4CwQRPBuJ6aPMtqqulrGgP2mfvKg_15gJO_eUxgE0QZu5pz2id5u_by_7kOxXaAZcveTx-aG1E8AKb-Ti4mtbx-ZIZGhhmToEV1l_vZWG1efsmI-mWGxE1jfHKDKBr0L88VbBhoVYy1lJ88r5aLHi9uFtUZdrcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: مردم صرفه‌جویی بزرگی را رقم زده‌اند
🔹
اتفاق بزرگی در حوزۀ صرفه‌جویی رخ داده که آمارهای آن به‌زودی منتشر می‌شود؛ باید در این زمینه واقعا قدردان مردم باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/684090" target="_blank">📅 23:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684087">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHHptb2w2WQ4HPyVOWMxd4-HJuGH13ftr-7m0bH9h1JU9Aml5hNUnRlJUmFtV53ZHf2wtP2zvwn2e5uYLhBjAjTNS4evSrJkcXVyvaD631WTayga3y_22zflXncOzM-Uld9x1QIJqyh_RgkjJpCyWWw8rA421t14iRJd3XiIXTnIoApN50vmFsvPoI-THpgfDwv73BJFSkalqcmzRn6YBK_K25yxCOSVvVa2RLT-ay3GkNgNHXztNdJB7Y25Nr8r_-G6bbjN-oaZcxVZUfUc7e1Ew9nilEYED1Uj0B6QkqSNpF-oXAMHFhZqnWdd2ptcc4wZc-yXZpNEKkmgeagOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxPSqHEPCEk3a9XJAbj6Bd7GSPSQKCmKexH5SOdLxZ9rwqh24XbZVgVXxMvenWJ5uYKNJDQ1Oermrd1WaKjyL2VBWdlrjmL6gk5JBEx9hzA6plrtn-b09-wmDPv1BWv65SW5a83x-AIq3XdFpBL_Oikypxbt6Hw2zqp-37DTwliaJX0UFyF3lf-FZnBglOgDUC_qN3sD714TPmybO1U3W4QSaZ9whibsHtc450f10YO4yI-drPKldoQno2bUfp0pH7N5xYL0no6hs0WX9XwiR5AeeZVjGoO10ChydRE_5o8PSFW0sRMUV-frrAitrVLgVKdT1mlVecrzbXyADGUi_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxLhPbTmRruL9NZ2um1Gu3K_60AYMEM-ZYJrI1jZdl0pBVEHxl2vmFUE6Um3npi6I_3Dly8uli1b7Z6bMKevrQl6PB2d4NH9I5m-5Z3y4TM9KZATtJkHycEawCDMa65yY0aVtWYr3B_862nRPfeOUiCe8FI5dXkyRt3TkpsfDLzXblUNoN8bftew0Gk9E2dn9iutPogNAFqzilHseIHudVf0nq9JIqxFJOj_WN0X1RD-YcdBAf95AidmwItVJE4P6e1KV2ZroWFNVIktSUdTvoqN8z-jPnRqcA_JTdVjfYl3FvD14unh55dAhWu-th7gRHeLdTbPVVSeV8QfoeloLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با بدرقه وزیر کشور فرمانده ارتش و وزیر کشور پاکستان تهران را ترک کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/684087" target="_blank">📅 23:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684086">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ollw1nCBWW2QF12SuitM5gr7ImEAJ0FrYcoqTjzZ0rWpJurS398MfD447k08JpsyyTyb_h6O5zqfgIhPDTRdSOOgXwbad2e6CNeqoFnIeAvgOBmer8OgcCvfDJ6fsKiuTaOk9G_AIItAQlfiBXYRo3XW5IinqiZtJWdys9I-vRlTplJIm0cjI4Hzp7z3cdQDlkKcjBfQG9T2FNaWPzq0PAxTm3t9ILnJt-te9qiB7ARHy0c8fWc6e-v4inVC22nD2WIxJi6YttRJCkXJZoiA3Rxr_mIyDvdyqsbXh4hFQlbur2Ct3KZyOQK__mqyCNddylXBEsZKrGQIOAwoPNq9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«راه تاز» برنامه‌ای متفاوت در شبکه سه با روایت دستاوردهای جمهوری اسلامی
🔹
فرهاد جم، سیروس میمنت، علی مسعودی، شهرام قائدی، پژمان بازغی، شهرزاد کمال‌زاده و آرام جعفری در این مسابقه با حضور در پروژه‌های بزرگ کشور، از نزدیک با بخشی از دستاوردها و پیشرفت‌های جدید ایران آشنا می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/684086" target="_blank">📅 23:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f814ea9e5.mp4?token=pyJqvzmO8QlU2X_38sFd_XQWBC45qGD2y8cvUmIkkMPy_eWLM_CHk9ij0rI6gRZLm9y9Eb8BO7TU6uQMUcKgS6mph0IolsThLqahFu4C9ZfMQ6pCdUXNYblUhIEzA3jsJXvfYDwB_D2opFrrW6h56_0v0c_VtmSA-wYoHVaoOtryb0wLo_Gok4TAf49WN0gb9F8TQ8s_YiFTs_BqFvgBZJDBFg17GTt36DBNb4OYoaKMdzxZ3puay1oWoEuIKq3sqMYtNzathPezNezuhuaWILFhC4vfzdjgUhuySr856EFH8TuOmProBz3U_tnCXgAmZAVHyCejRV0vEWCOmutE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f814ea9e5.mp4?token=pyJqvzmO8QlU2X_38sFd_XQWBC45qGD2y8cvUmIkkMPy_eWLM_CHk9ij0rI6gRZLm9y9Eb8BO7TU6uQMUcKgS6mph0IolsThLqahFu4C9ZfMQ6pCdUXNYblUhIEzA3jsJXvfYDwB_D2opFrrW6h56_0v0c_VtmSA-wYoHVaoOtryb0wLo_Gok4TAf49WN0gb9F8TQ8s_YiFTs_BqFvgBZJDBFg17GTt36DBNb4OYoaKMdzxZ3puay1oWoEuIKq3sqMYtNzathPezNezuhuaWILFhC4vfzdjgUhuySr856EFH8TuOmProBz3U_tnCXgAmZAVHyCejRV0vEWCOmutE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: مردم می‌توانند با استفاده از اوراق گواهی نفت سود ارزی از نفت آتی کسب کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684085" target="_blank">📅 23:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b83F10C0HIQsxLYia8OgQMR8vd7UWz6mwiqCVGAMfWucVh0Y0fIYQT57mn-wdED6LVdq1e4cfePrnIzJdOkE4RkyC4Dk47gVqz9xTQI8sNe5-oUBdcRByMmEqtEI9SWvZ96YjQeZzAf20Bc4AhW1q6_KLDrEZM4cQ67acMO9gz2TSk71kDpog0clRPQpy-LJVTNDypXlTC6ZxzJqhtQWiMhVy0ghhPYQLOuemVDKXerrqaDj_2B-ENu3ysLemJ3qL51o-ugFLTxLjXRsYmmzTY0MspP3IKtHr9j6A_WKQP_-owKo2fso0jkbgAQ4m3iFdGMtcR6xL2NFf8lwC652VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن چگونه می‌خواهد همه شریان‌های اقتصادی تهران را قطع کند؟ | دلار، نفت، کشتی و طلا؛ چهار جبهه جنگ اقتصادی آمریکا علیه ایران
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا، در نشست خبری خود مدعی شده مرحله تازه فشار علیه ایران بزرگترین عملیات اقتصادی در تاریخ است؛ عملیاتی که هدف آن دیگر صرفا تحریم چند بانک یا شرکت ایرانی نیست، بلکه تلاش برای قطع تمام مسیرهایی است که به تهران امکان کسب درآمد، انتقال پول، خرید کالا و حفظ ارتباط با اقتصاد جهانی را می‌دهد. اما واشنگتن چگونه می‌خواهد همه شریان‌های اقتصادی تهران را قطع کند؟
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3240198</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/684084" target="_blank">📅 23:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a63edf13.mp4?token=U3XihBM1WJpBVG8EtnG-xBGB22_k06ftOvwzXLWjnGA-nrPMg8G0ezMQqaLyl6pGfZmsGwf6xwgCp49LQBa85Bq04kGIKBItGuoucqpFpR1SXL55sCUhN81sP7uto2_lQPh-N4oZr5PTqxYL0khzWw1QkJeG8yuJqFZMgiHCPDLDLAOUg5K9kfWYapzCOqD7x21kyPb9jknzY-6W4_3th6aGXmwwWTQEJaBz_ojZ3HtEFVJwozSAaSGWk5ekIxVS7c7rZT1EQ42prftML5UNgC1yD3-Dq1IOVCXX3xkipmwrLg2GEpUr8SykDPWQrYv50TV3qyj11V2BNN93Zzmlxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a63edf13.mp4?token=U3XihBM1WJpBVG8EtnG-xBGB22_k06ftOvwzXLWjnGA-nrPMg8G0ezMQqaLyl6pGfZmsGwf6xwgCp49LQBa85Bq04kGIKBItGuoucqpFpR1SXL55sCUhN81sP7uto2_lQPh-N4oZr5PTqxYL0khzWw1QkJeG8yuJqFZMgiHCPDLDLAOUg5K9kfWYapzCOqD7x21kyPb9jknzY-6W4_3th6aGXmwwWTQEJaBz_ojZ3HtEFVJwozSAaSGWk5ekIxVS7c7rZT1EQ42prftML5UNgC1yD3-Dq1IOVCXX3xkipmwrLg2GEpUr8SykDPWQrYv50TV3qyj11V2BNN93Zzmlxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایگاه زن در خانه جایگاه مدیری‌ است که از قضا ریحانه هم هست
🔹
این جایگاه اساسا با هیچ جایگاه دیگری برای زن قابل مقایسه نیست نه به لحاظ دنیوی نه به لحاظ اخروی...
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/684083" target="_blank">📅 23:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای مضحک وزیر جنگ آمریکا: می‌دانیم که ایران نمی‌تواند فشارها را تحمل کند و اقتصادش در مارپیچ نزولی قرار دارد
🔹
ایران می‌داند که ما بر تنگه هرمز تسلط داریم، محاصره ما غیرقابل نفوذ است و نفت از این تنگه جریان دارد.
🔹
استفاده از نیروی نظامی در تنگه هرمز یا هر جای دیگری را بعید نمی‌دانیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684082" target="_blank">📅 23:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684081">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
نتانیاهو با استقبال از تحریم‌های جدید علیه ایران: به ترامپ و بسنت بابت تازه‌ترین تحریم‌ها علیه حکومت ایران تبریک می‌گویم
🔹
شما به‌درستی هزینه سنگینی بر این حکومت و کسانی که به ادامه اقدامات تهاجمی آن کمک می‌کنند، تحمیل می‌کنید.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/684081" target="_blank">📅 23:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وزیر اقتصاد: از نیمۀ دوم سال حداقل برای بخشی از دهک‌ها افزایش مبلغ کالابرگ  خواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684080" target="_blank">📅 23:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1a7200f9.mp4?token=B8eMQY7pP3NgUMaj7ZTHpkmAVzwnLX3VGUOoJnqICvHRJiHkFQrz1QslwET0dZQOWmyUmCFqpfw_9ijQP8DuCxpSOLJcNwR9AGj6lR3WhPTfkDtdU2pFKZWtT33qrNkFB-KVlEOIHdahv27UPqxmzACJYoZYjvAg-vgXH8PLkjCM_C6bf9S9DJzs-BRraQqMewYwMjFQL-wcbS9-BKGJ6cxCuGdncL3a3NO7-0h6LS25rQqh2k8RgKN-ycqH27oYQX1KTH4wp7c2GM_-cM64t-iQKWNk0JyQpw7hh__pO1E7I5tup7uclAYuquXyix-pd3-0U9PH1wq-xN5CykNbdK8-3x0WI5Yk2hKRWOSvFa4SHGyWV1CUEh859zBY4_XYGPxXQNN6swTcEnhuKr_dp7PD6LKB2zNWhyafCQxdktJHEOWebY0i5pW1G2MtNwzHnfF0HUCvMgSnV-OOyy3MQoif-FGDHvhWN13RPmJDqD4bm0j_qcIJ8u1wZcGr_nFU5-vovQUec84jOOOEc8Ous0ZhvOMFmCEFZw8hy9Y9qXx4GfH_yXvyk2yjv_toc2VTBQkBBOQbjYePwt3mRq_orHF29VYJVHwVJGBPYYVQty288psgTm8p5xy2hsif4F57be5VcbV2i9ofV_uxCqdw67g9UW3civz2WgVARnv2KvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1a7200f9.mp4?token=B8eMQY7pP3NgUMaj7ZTHpkmAVzwnLX3VGUOoJnqICvHRJiHkFQrz1QslwET0dZQOWmyUmCFqpfw_9ijQP8DuCxpSOLJcNwR9AGj6lR3WhPTfkDtdU2pFKZWtT33qrNkFB-KVlEOIHdahv27UPqxmzACJYoZYjvAg-vgXH8PLkjCM_C6bf9S9DJzs-BRraQqMewYwMjFQL-wcbS9-BKGJ6cxCuGdncL3a3NO7-0h6LS25rQqh2k8RgKN-ycqH27oYQX1KTH4wp7c2GM_-cM64t-iQKWNk0JyQpw7hh__pO1E7I5tup7uclAYuquXyix-pd3-0U9PH1wq-xN5CykNbdK8-3x0WI5Yk2hKRWOSvFa4SHGyWV1CUEh859zBY4_XYGPxXQNN6swTcEnhuKr_dp7PD6LKB2zNWhyafCQxdktJHEOWebY0i5pW1G2MtNwzHnfF0HUCvMgSnV-OOyy3MQoif-FGDHvhWN13RPmJDqD4bm0j_qcIJ8u1wZcGr_nFU5-vovQUec84jOOOEc8Ous0ZhvOMFmCEFZw8hy9Y9qXx4GfH_yXvyk2yjv_toc2VTBQkBBOQbjYePwt3mRq_orHF29VYJVHwVJGBPYYVQty288psgTm8p5xy2hsif4F57be5VcbV2i9ofV_uxCqdw67g9UW3civz2WgVARnv2KvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلن اکباتانی، فعال سیاسی مقیم آمریکا: ایران به ویتنامِ دوم و گورستان نیروهای آمریکایی تبدیل خواهد شد. ایران، باتلاق بسیار بزرگی برای آمریکایی‌ها است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/684079" target="_blank">📅 23:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🟢
داستان لگویی جدید منتشر شد...
ولی پایانش چیزی نیست که اولش فکر می‌کنی
🫨
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/684078" target="_blank">📅 23:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa13b21ef6.mp4?token=VkJIeXPFz7Izbw-J_qEDo6_3wxwJzbnCZywjbjxojIPj0KVsjAY3Ttv_AGKwJ9IY_M6mdjAhZWUw27Cur5Mf-DbEVegenWBxQBzyULUbdj2DznyrcRi0rl-P5149gQo_LHkJwjmUZk4Q1_76MC9qx0cd6quLhoHEjvruTfo-aLNM7AFoQJhdSG81UBp2xCCz-RzLET8r0dtUmiExXHtQuW85dPLq55hAOMxPNzkMVZibmh8p_WCica0SmH0Bz-z_fcxnagb2YlQb5kc9pi-p61nRfNGHKuVeqQ7Ll1oSJGotCxUL3VNHZew5vKfyVvTGf6yU6gaemXLCp6t3omvxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa13b21ef6.mp4?token=VkJIeXPFz7Izbw-J_qEDo6_3wxwJzbnCZywjbjxojIPj0KVsjAY3Ttv_AGKwJ9IY_M6mdjAhZWUw27Cur5Mf-DbEVegenWBxQBzyULUbdj2DznyrcRi0rl-P5149gQo_LHkJwjmUZk4Q1_76MC9qx0cd6quLhoHEjvruTfo-aLNM7AFoQJhdSG81UBp2xCCz-RzLET8r0dtUmiExXHtQuW85dPLq55hAOMxPNzkMVZibmh8p_WCica0SmH0Bz-z_fcxnagb2YlQb5kc9pi-p61nRfNGHKuVeqQ7Ll1oSJGotCxUL3VNHZew5vKfyVvTGf6yU6gaemXLCp6t3omvxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: افزایش فعلی قیمت ارز ناشی از التهاب در فضای رسانه‌ای است
🔹
تلاش می‌کنیم وضعیت بازار ارز را به حالت عادی بازگردانیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/684077" target="_blank">📅 22:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک پیشنهاد ساده برای صاحبخانه‌ها
🔹
گاهی یک تصمیم کوچک، برای یک نفر اصلاً کوچک نیست. شاید چند روز مهلت، کمی مدارا یا یک جمله ساده، بتواند فشار بزرگی را از دوش یک خانواده بردارد.
اما اینجا قرار نیست درباره بخشیدن پول حرف بزنیم؛ درباره چیزی مهم‌تر از پول است...
#چرخ_زندگی
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/684076" target="_blank">📅 22:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a6edfdc9.mp4?token=p7QGHxFDhxaAwODFOE_a0TzfIJZLvf8obpjdEu8qWIip7ZwOD3WvEgzcHbxe1EtB-Nt21-504iHFs8WcbAYIXHgqaruvMgVlYheM2CS3ip2AYSIoIPSHsmd4vgo_ZW4DUQEZ6wiau4fxWvqj-nyQh_2D7cmML9Ke_dAPg_Uzy6p3TyLGeS97Edn9qWAbBDFlUL0qVI7XMHjMxGfqKl4PqVuiW8FiC5HVhRvubakIQJohyqgaFv27k4rfhC60pJgHcR4qh0TRldjVO7-oCfHGGgJJp-jI-qPCS8H2zoi2mFUvCvqlVUVaH4StuL_oPbTBXO1vu2ECbwZkXVSX150_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a6edfdc9.mp4?token=p7QGHxFDhxaAwODFOE_a0TzfIJZLvf8obpjdEu8qWIip7ZwOD3WvEgzcHbxe1EtB-Nt21-504iHFs8WcbAYIXHgqaruvMgVlYheM2CS3ip2AYSIoIPSHsmd4vgo_ZW4DUQEZ6wiau4fxWvqj-nyQh_2D7cmML9Ke_dAPg_Uzy6p3TyLGeS97Edn9qWAbBDFlUL0qVI7XMHjMxGfqKl4PqVuiW8FiC5HVhRvubakIQJohyqgaFv27k4rfhC60pJgHcR4qh0TRldjVO7-oCfHGGgJJp-jI-qPCS8H2zoi2mFUvCvqlVUVaH4StuL_oPbTBXO1vu2ECbwZkXVSX150_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش وزیر اقتصاد ایران به اسکات بسنت: منتظر پاسخ ما باشید
🔹
آنها این صحبت‌ها را قبلا هم گفته‌اند، ما کاملا برای هر سناریویی آمادگی داریم.
🔹
شریان‌های مالی و اقتصادی دنیا به این سادگی نیست که بتوانند ادعا کنند ارتباطات مالی و تجاری ایران را به‌طور کامل قطع…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684075" target="_blank">📅 22:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZimj8pqMThedJF9ysQsPat4a3jDg0-n03-ePpx5Ts_dp-BNfGuRxBAIyt1R_cO5zR5mKdNFKjdyIiM8FOUvETiR6tjt9mX8n5iN6FEP2XKUvn2HALWB0GgBqGSQCyDmhB7sDaB_myu8Zib7MqAz7ra9u9vgdKRbLGdAhBFlutNK4djpIVoYj4t7EaDRv7ACTrIeQUBIYtrckrXPzsc_mGz02lqyPW9sQp1Kk3HGLubmrVPyUv5YGkwoK1SEjWtjweVN1y8yh88jOOZ3fAxz_FGFFgt617gxINXSNFADf_dZrrnfWcwywz4zGC9KK2eMqE4ic38Cg-4j180JIvp-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر در پایان هفته سوم با صدرنشینی استقلال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/684074" target="_blank">📅 22:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1kMnogj1eMeeGyQlvwUwLH59pRncoW76KR4DyvkzgOwi5vzmEEHIPA1o-mRBRSaq8aZVCPbeb_XCxhNx-DvOyS5cqVa_89rB_GYL4DTX9UT6dt_YOazCZIA0_Q1TirHUWaQ11Yo74iLo4acNOl8C1g6oSPJa1SlU3riIRZuPjUWeo55aADkabuoZwinUd5MO0A3qvvRsIet9EZQBnhtwhZCxXGdh5N2U5xTNbjuoSdzirNDqXodVK6LInp9aWpEfVYHzvRmYwgQF_3u6lOZD6gNshGFhuNyZM0slBkuXAZZlB-Hf5cWxl0etv9alYxPboDcB05EnB2_R1neKHBNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: از زمان شروع جنگ ایران بنزین در ۴۵ کشور گران شده است
الجزیره:
🔹
از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران، شش ماه پیش، قیمت بنزین در حداقل ۱۴۵ کشور افزایش یافته و بار سنگینی را بر دوش مصرف‌کنندگان در سراسر جهان گذاشته است.
🔹
این ارقام بر اساس داده‌های GlobalPetrolPrices است که قیمت سوخت را در ۱۷۰ کشور و منطقه ردیابی می‌کند. قیمت بنزین در میانمار بیشترین افزایش را داشته و پس از آن بوتان، کوبا، امارات و نیجریه قرار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/684073" target="_blank">📅 22:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پاسخ وزیر اقتصاد به اسکات بسنت: این‌بار هم شکست می‌خوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/684072" target="_blank">📅 22:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684070">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKqOC8UoynCUHd-52fbznI7g6Ow97ojrhdAt_M_jH7Ib81wn3xiC_N7O5_K9HyKdVAJCGcHIPQJBZD2z_1g0eA3DRfoh0CUsPOgBkNDLF_XfzdAg5CcVxk5iCU6rEEjESSh3oAWKa877xPw1WCyXzhqvLY2Ow7uQhI0wF3NUq8RH6PB2o0soQUhNvWhvcqBiqFn7Xw5BdpVOIQlud2U5PfG8vrXdMx4cFod0RQgudNd4ONXdxV5iZfJlgq-orU-XwUYkXBKTPcDOXyyam6QLAg-ONzcELSREM1nWpjkIA7k-mNI_15159kIYaEiSCfhE1blDqiD0yS_x-DsLraBoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAikv2BAEEMwXuPQtTvvjIp0Cty_6JjBgSw1r0YoBxO1w3AuC5sqoS-rO0SV0Bqz230Xfm4ickxJbaMquePmTMD3yaX1HEw2LzglnFRIkfit3cxbtAfd49U9-w16DUgb-vTmZU_ibLERfKzle9VGzFdQRx_97U6LW-k-I4KU8my1kWfndYK2BjexN8rUIpW-93TIpUhLB3xfbYerLHEIvFo3wtbGxa5bIFUEIajwjeY1_Ce9LO6fqXnk2Xdxk65w3LcqAzF-fdQNXFcab_XDDawI21TTUZ1RJMDTMRYH0ZLMntWWmY5vPEzxBlob2yfq0CvvHlyhQ6froZBWl3bcCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌طارمی زیرقیمت به امارات رفت
🔹
یک رسانۀ اماراتی مبلغ انتقال مهدی طارمی از المپیاکوس به الوصل را تنها ۴۰۰ هزار یورو اعلام کرد، تا او ارزان‌ترین لژیونر الوصل لقب بگیرد.
🔹
مبلغی که باشگاه الوصل برای خرید طارمی پرداخت کرده، حدود یک‌ششم پولی است که المپیاکوس برای…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/684070" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مدنی‌زاده: افزایش قیمت کالابرگ برای برخی اقشار از نیمه دوم سال اجرا می‌شود  وزیر امور اقتصادی و دارایی:
🔹
در ماه‌های ابتدایی سال، به دلیل کاهش درآمدهای نفتی و آسیب به زیرساخت‌های گازی، تأمین منابع کالابرگ با محدودیت‌هایی مواجه شد.
🔹
با استفاده از منابع دیگر،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/684069" target="_blank">📅 22:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پاسخ وزیر اقتصاد به اسکات بسنت: این‌بار هم شکست می‌خوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684068" target="_blank">📅 22:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
پزشکیان: زور و قلدری آمریکا راهگشا نیست؛ عاصم منیر: فرآیندها را با دقت دیپلماتیک پیش می‌بریم
رئیس‌جمهور در دیدار با فرمانده ارتش پاکستان:
🔹
آمریکا باید لحن و رویکرد خود در تعامل با ایران را اصلاح کند، چراکه تکیه بر زورگویی و قلدری، تنها فرآیندهای اجرایی را با پیچیدگی مواجه خواهد ساخت. ملت ما با اتکا به همبستگی، از هرگونه فشار و تهدیدی عبور خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684067" target="_blank">📅 22:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684066">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRJjz2akQ9zuebxzQcTepr04JRLflyonEGZ_xP1lw4zsQq0l2b--aFiTWK1aDA1odTGufqjY9DCQIgHD6o9uAIqh1L3s0LTZo854ar7Fbj0FPRlLJn9zrD2vke8R0CYM617-EsQGK0xO3YDsHOvZih8IynCSLPR7RAb4R_M-fURE8SYQmQUz7aEle7Sd7OWYCPgz8FDKnCxHzBBhPwivENwWFtyqbbk5SxSBkvyVOg0MS9mAdDUGDo9DTT5tLgn0KPf0bN48_ca0eSrvlwT3h3ywvQ-G9DGEulc4qJ1Gy9K3t23eFDILQID4ZZMdKvPDhmwgehyqibeTxfUTFd3ZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما زنده‌ایم به امید
🔹
تصویری از یک مسابقه فوتبال در غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/684066" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N512-4vSAzoT9l7P0FYVRyNGcynKkZj2JONlOSw_fqZ6D_Qjw61xnIFIZXAGY049mQI72alhYaYiYcxWmJN_arnw8NsR86MCXjx-5tuCmny89302hP12nRAGFEwlbuKABGNLqV7LefjTuTnXGck6YBgJ6X_havBO_eUGIFm0wR0kGkVmONu_CpDBOYZ_7SKNApnad9WRbs0Caa0wBgsR5rPOuHowJLgqiLTld3pTd7Etrs-1qdi6ypWXaTcTXshfes6G7LO5EEt1g-rdUJ1FlZr0QuJjwV-QGh2dep3uLEgH7XErEhRli_n0_LTawhRSYvPjwShDsMJ-UkXQ2OVcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدارهای غلط درباره رومینگ
فعال بودن سرویس یعنی مصرف اینترنت نیست
🔹
در روزهای اخیر ویدیوهایی در شبکه‌های اجتماعی منتشر شده که مدعی است فعال بودن خودکار «رومینگ» باعث کسر حجم اینترنت کاربران می‌شود. بررسی‌های عصر ایران نشان می‌دهد این ادعا مبنای فنی ندارد.
🔹
رومینگ زمانی کاربرد دارد که مشترک از کشور خارج شده و از شبکه اپراتور خارجی استفاده کند. بنابراین فعال بودن این سرویس در داخل کشور، به‌خودی‌خود باعث مصرف اینترنت یا کاهش حجم بسته نمی‌شود.
🔹
انتشار چنین اطلاعاتی می‌تواند باعث سردرگمی و بی‌اعتمادی کاربران شود./ عصرایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684065" target="_blank">📅 22:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
وزیر دفاع و رئیس ستاد کل نیروهای مسلح یمن: دوران نبردهای صرفاً تدافعی به پایان رسیده است
🔹
سرلشکر «محمد العاطفی»، وزیر دفاع و سرلشکر «یوسف المدانی»، رئیس ستاد کل نیروهای مسلح یمن اعلام کردند که ماهیت نبرد یمن از وضعیت «دفاعی» به وضعیت «تهاجمی و پیش‌دستانه» تغییر یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/684064" target="_blank">📅 22:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e560e021.mp4?token=PFgxzkBGeflpAMO3yDPJu6DdYwIIiEpcwoGrIEp3L_ryU13OdFt7NDVCy5JC-0gb-hgIjRaakdXfozeH9ckTv4nSzqiefWvKfV1ddiYRRvQ3qr9SgmZamxPRkrC9N2cDivfIZcMLWAwzhPml1U1vh56UB-fJu31vRDRcKVTxeC8UBA9gMBt26UKJsf8euB23Sa5fvacmuPz4NNQD81j5liE_MVWXBdCWFGKJh_pQyfygfWATsncgNbpcCcjwcL5kXs5TaygPoipcGDuREiaNVKsppKhMe0QsddPEuW6Wj0i6vKvCOj9RIZwGd8bsgAq6ptOoKnjTnrLYYO6t_0csBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e560e021.mp4?token=PFgxzkBGeflpAMO3yDPJu6DdYwIIiEpcwoGrIEp3L_ryU13OdFt7NDVCy5JC-0gb-hgIjRaakdXfozeH9ckTv4nSzqiefWvKfV1ddiYRRvQ3qr9SgmZamxPRkrC9N2cDivfIZcMLWAwzhPml1U1vh56UB-fJu31vRDRcKVTxeC8UBA9gMBt26UKJsf8euB23Sa5fvacmuPz4NNQD81j5liE_MVWXBdCWFGKJh_pQyfygfWATsncgNbpcCcjwcL5kXs5TaygPoipcGDuREiaNVKsppKhMe0QsddPEuW6Wj0i6vKvCOj9RIZwGd8bsgAq6ptOoKnjTnrLYYO6t_0csBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدنی زاده: زمان توقف کالا در گمرک از ۱۰ ماه به ۸ روز کاهش یافت  وزیر امور اقتصادی و دارایی:
🔹
طی ماه های آینده  زمان ترخیص کالا را به سه روز می رسانیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/684063" target="_blank">📅 22:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69aa0f9eb1.mp4?token=aTa8PhTGBj0XFewTurPVOJBhBOVXiUEXbAp5j08CPrVBPwwV5DSohinnsR2HLJgWDkoGViEnOnMUFX88PAiGTrzZWInTqvKjUSYQ1BAwt0xHW1tK-pSJXbvBe7BBZi3rXJQLvBp7N6grKCoUOt7_YeMebQaOHB9EeQdcve34Ii7N4vmPjYCRyQFi1_RYP_I-5ryMb45ki5HYY2D7i3ymez37iXJhqCrIRirgRO98L-1g4bpZaOuEybSn3m4G6ZYaOrMQJkCuAb-jqaDhnVAO_BuR2QcWuknRx7Bb5cmyN3AC9wVzBlV4qf6k4hxSSqj0iuX7DHF2xDAbiunkqsf73Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69aa0f9eb1.mp4?token=aTa8PhTGBj0XFewTurPVOJBhBOVXiUEXbAp5j08CPrVBPwwV5DSohinnsR2HLJgWDkoGViEnOnMUFX88PAiGTrzZWInTqvKjUSYQ1BAwt0xHW1tK-pSJXbvBe7BBZi3rXJQLvBp7N6grKCoUOt7_YeMebQaOHB9EeQdcve34Ii7N4vmPjYCRyQFi1_RYP_I-5ryMb45ki5HYY2D7i3ymez37iXJhqCrIRirgRO98L-1g4bpZaOuEybSn3m4G6ZYaOrMQJkCuAb-jqaDhnVAO_BuR2QcWuknRx7Bb5cmyN3AC9wVzBlV4qf6k4hxSSqj0iuX7DHF2xDAbiunkqsf73Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدنی زاده: زمان توقف کالا در گمرک از ۱۰ ماه به ۸ روز کاهش یافت
وزیر امور اقتصادی و دارایی:
🔹
طی ماه های آینده  زمان ترخیص کالا را به سه روز می رسانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/684062" target="_blank">📅 22:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSphtilliaeaEJI33GvNPkrnJqLvjM70zNpR6w9MgM5zFFzSuGRi8W-42Fhv4sBf4FIQ6sW9zIGuX51qkWbKZlZ8cOKaUhJNS9z02dcUXsrkG8Jkjj0YfmAJlNrZxwjfe8RdqjaLdVbsWvKrNqSpJnroLQFsZBaYEPvTNCJcY2j8u3stOJhy9cZ3uNvyADfG0utvQBFaOATLbyF0i77V-LAXGzJ5T-sB0x6Yli4ZV_vSoeN7k06oBIXAqRzXvSgU5k1BLeRwI5kneoUktnWfr9USS5aZyMBNuZhm8SF-9JtnpPyJo5qbfS_XtOv5geub99LebmSJLlEgsWzsWGec8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قمارباز: کانادا باید خود را با مقررات آمریکا وفق دهد
🔹
ترامپ در اظهاراتی درباره روابط اقتصادی آمریکا و کانادا گفت بخش قابل‌توجهی از برق، نفت و گاز مورد نیاز کانادا از طریق ایالات متحده منتقل می‌شود.
🔹
او با لحنی تند خطاب به مقام‌های کانادایی: یادتان باشد، بخش زیادی از برق، نفت و گازی که کانادا دریافت می‌کند از طریق ایالات متحده آمریکا منتقل می‌شود
🔹
یکی باید این دلقک‌ها را وادار کند که خودشان را با مقررات وفق دهند؛ وگرنه عواقب آن برای کانادا بسیار بدتر خواهد بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/684061" target="_blank">📅 22:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
آمریکا نام سوریه و «جبهه النصره» را از لیست‌ سیاه حذف کرد
🔹
وزارت خزانه‌داری و وزارت امور خارجه آمریکا رسماً اعلام کردند که نام سوریه و گروه تروریستی «جبهه النصره» را از فهرست‌های تروریستی خود خارج کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/684060" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2c709522.mp4?token=cc-7fRhlz4l58IpsRPnZf_nPXg1THFdG-VAxZLhA1aqi78io1uMHdiK-UHnMeCE7lLdJI6sKYidmUkH4bbZZte8FsDbPuysMXLe-bV8CPQ5tCtoJFREiFvzME5boFi0hFIWhuldEPnFGVUQ_7iyc3ImId-R7R2g69KD6SQCWWjCnZwPmYCf-uaeTc1BrYswT9GERI-q32GPSfITY_vYnyvX5tTO1o1G6J5PvXlLdFrtibx789sH6pZ0pvBK2eFIx-rE5NzxOLjhfFvv__v0_KLRn19m2lBAsDW_O1pJyUxw7B4TNfURc6PNVBMT1juWwtE6Eo-EIcxOsg62SxGaOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2c709522.mp4?token=cc-7fRhlz4l58IpsRPnZf_nPXg1THFdG-VAxZLhA1aqi78io1uMHdiK-UHnMeCE7lLdJI6sKYidmUkH4bbZZte8FsDbPuysMXLe-bV8CPQ5tCtoJFREiFvzME5boFi0hFIWhuldEPnFGVUQ_7iyc3ImId-R7R2g69KD6SQCWWjCnZwPmYCf-uaeTc1BrYswT9GERI-q32GPSfITY_vYnyvX5tTO1o1G6J5PvXlLdFrtibx789sH6pZ0pvBK2eFIx-rE5NzxOLjhfFvv__v0_KLRn19m2lBAsDW_O1pJyUxw7B4TNfURc6PNVBMT1juWwtE6Eo-EIcxOsg62SxGaOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کابوس مرگ ترامپ سر میز غذا
🔹
یک وعده غذای معمولی به صحنه‌ای مرگبار تبدیل می‌شود؛ اتفاقی شوکه‌کننده که همه‌چیز را در چند لحظه تغییر می‌دهد.... #کابوس_ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/684059" target="_blank">📅 22:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPvpuTpsmC8xIw5P_PPnzPpLgEyWC-iunlBCq1wU4-9xbbDsO6TNaR-1JyU941DKDC1qFhSmS164ZF8ypA0uRP_Kt9UguKTFp6MRtdvgSH6wM81wXDKMvpJFFR54x8-6dAMwERegdMBLWEyuYdxdv5Oi9NbfW0F7pjGZaL4t5nf8_FSlY6LsM9i6k7yKNAea5zgp7JvopXFCToWly9Q3-gV1PxxJsEndZsm9O2IEybv1yHlhJ-hhifv3UagmzTDk-cbo8yeJnMvYmcl0oAD0UKtV7adf9_LodxoCEpASedejbMWy-5nFHCo2DjKVw5IqspR9l4iYoXO8ZiKz12Ze1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رازدار بودن، فقط پنهان کردن یک راز نیست؛ راهی برای حفظ اختیار و آرامش انسان است
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید: «هر کس راز خود را پنهان دارد، اختیار کار در دست اوست.» گاهی نگفتن، قدرتی‌ست که به انسان اجازه می‌دهد سرنوشت تصمیم‌هایش را خودش در دست…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/684058" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16caf9a31.mp4?token=YCZDTrdXnoM0OuRkdteb0MHZSzyNZetPANCWb3-jpTpKBmt1mljGbm1z04ehdvrtn42KlPBgmOoO0vLuv6Ln7knZMpflQlvm95rcOLH9APkLdUXKxLswb_8H04KcBFYgO6wbeh4P7wkWf-73hBTcxhbCTgDRWmt7TreS5FkAiTsumLLd8gamC-kchF-QSkrEeMJKZAc_4oHn-auMufP80jvzjNR-INqc2upiA3H-awRkgmq2rSaObLoQqrYzyLxNiKlf6IxkoJ7IhogKejkmwyekAUZvRz63ZtyJKKmu7VHQiKt5C6qT0R7LWvkTwwCkzQ3bA3KC6YAumVLjhVwb1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16caf9a31.mp4?token=YCZDTrdXnoM0OuRkdteb0MHZSzyNZetPANCWb3-jpTpKBmt1mljGbm1z04ehdvrtn42KlPBgmOoO0vLuv6Ln7knZMpflQlvm95rcOLH9APkLdUXKxLswb_8H04KcBFYgO6wbeh4P7wkWf-73hBTcxhbCTgDRWmt7TreS5FkAiTsumLLd8gamC-kchF-QSkrEeMJKZAc_4oHn-auMufP80jvzjNR-INqc2upiA3H-awRkgmq2rSaObLoQqrYzyLxNiKlf6IxkoJ7IhogKejkmwyekAUZvRz63ZtyJKKmu7VHQiKt5C6qT0R7LWvkTwwCkzQ3bA3KC6YAumVLjhVwb1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال جالب خبرنگار از وزیر خزانه داری آمریکا درباره عملیات تحریمی ایران  خبرنگار:
🔹
شما این عملیات تحریمی علیه ایران را یک «روز D» اقتصادی توصیف می‌کنید، اما روز D یک تهدید به حمله نبود و آمریکا به آلمان یک بازهٔ زمانی نداد. چرا تحریم‌ها را امروز اعمال نمی‌کنید؟…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/684057" target="_blank">📅 22:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
منبع ارشد اطلاعاتی ایران: طرح فشار اقتصادی ترامپ، عملیات روانی است
🔹
یک منبع ارشد اطلاعاتی ایران، طرح فشار اقتصادی ترامپ را بخشی از جنگ روانی علیه مردم دانست و تأکید کرد آمریکا پیش‌تر همه ابزارهای فشار، از تحریم تا محاصره، را به کار گرفته است.
🔹
وی ادعاهای ترامپ درباره حمله به زیرساخت‌ها و تنگه هرمز را نیز عمدتاً عملیات رسانه‌ای برای کنترل قیمت انرژی و اثرگذاری بر بازارها توصیف کرد.
🔹
این منبع، طرح جدید فشار اقتصادی و حضور میانجی پاکستانی را تکرار همین الگو دانست و گفت اقدام میدانی جدیدی رخ نخواهد داد؛ ترامپ می‌کوشد مشکلات خود در میدان را با عملیات روانی جبران کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/684056" target="_blank">📅 21:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a62c30e2b.mp4?token=Z1D9F46B3WMElmh7GoD6G13gnJcD_lpfPWyLf-w9-wRe0DFmEv5ejLUL9Hnn0HAkKaRMGB_odHNkLzh33zR-P19ixEc7pDlDgklCgC8vB9VmsKiUXuGU1OUhj95-1P8sWXe6mlAvL-Jq-B3-n9gilH4Ci-yLCsDX3y4vC-bD1CkNX6iZwNFOcl2iRluzZJ1qqRMVu6yN4O27l8ew07EF068VPygfZQasnE-wfJ2BXkKFZobXmL-vlm3qT3HFQTGYOf32TDyEu31HaiGRfmZwQEI49UBiGOb2HW4zfIcHUBOnQpmA16MwEIkdqLLKdQE-cjT7_dP9UAtvzCdvU6CzSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a62c30e2b.mp4?token=Z1D9F46B3WMElmh7GoD6G13gnJcD_lpfPWyLf-w9-wRe0DFmEv5ejLUL9Hnn0HAkKaRMGB_odHNkLzh33zR-P19ixEc7pDlDgklCgC8vB9VmsKiUXuGU1OUhj95-1P8sWXe6mlAvL-Jq-B3-n9gilH4Ci-yLCsDX3y4vC-bD1CkNX6iZwNFOcl2iRluzZJ1qqRMVu6yN4O27l8ew07EF068VPygfZQasnE-wfJ2BXkKFZobXmL-vlm3qT3HFQTGYOf32TDyEu31HaiGRfmZwQEI49UBiGOb2HW4zfIcHUBOnQpmA16MwEIkdqLLKdQE-cjT7_dP9UAtvzCdvU6CzSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد  سرلشکر رضایی در دیدار با فرمانده ارتش پاکستان:
🔹
آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/684055" target="_blank">📅 21:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df291ff75c.mp4?token=a1YF8vejgEdGha-bVs6qhVay6nak8mGBPzy9-tdXJnPR15CG5AFE-lMu-nkFa5kkqyiOqG_7a4kjmTkFm6r0HDzjtBhaqo1OWic2ltTacGf6CtbrV-eZ12fEx-JmRTd0DKgwMbLcaS_-bcc-9BbAuGCxSCkVzO6-cxDhP9CHtw4cc0-bDMqEkYLPdEvM6gb39JXbF6Whg1fALfJOiE66cnANRKfqC0Tgr7oFDUypM3d4bs-4mNrU0nBnJn2WHuQ5nz50BG6h_Pn3Z-skJXp0z0w78ZF0-kTrHucTSG8f1KOb3HM92uS8yaLcqTsbnYwbPbZ2BAraQNtiTQY2P05m1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df291ff75c.mp4?token=a1YF8vejgEdGha-bVs6qhVay6nak8mGBPzy9-tdXJnPR15CG5AFE-lMu-nkFa5kkqyiOqG_7a4kjmTkFm6r0HDzjtBhaqo1OWic2ltTacGf6CtbrV-eZ12fEx-JmRTd0DKgwMbLcaS_-bcc-9BbAuGCxSCkVzO6-cxDhP9CHtw4cc0-bDMqEkYLPdEvM6gb39JXbF6Whg1fALfJOiE66cnANRKfqC0Tgr7oFDUypM3d4bs-4mNrU0nBnJn2WHuQ5nz50BG6h_Pn3Z-skJXp0z0w78ZF0-kTrHucTSG8f1KOb3HM92uS8yaLcqTsbnYwbPbZ2BAraQNtiTQY2P05m1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/684054" target="_blank">📅 21:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smAqgrbPAr3bBBeT7GYNT3UjxU-RB5zmLkD7CFg4zOXuPXQ9y72MR6FsO-NxW-rp216cuU_qW6hRJIzCSal2OS4obKVLzv8XeS1eS9cpq6eSnXFky7h4XS8qwhLmmVUbqOkE9HYz3ORZNuay5uLkKngvDUOdUrR8aOJdi3Co8SfX5QOI6wMNRUClGJckdL_uIEgTUoX4mFq_bWdSHqwSpRdcs9d22cPz0m2dC2jraQLK4wQmG3fBVnIT_HPBhWyC0FGU0dFpzYxvh6f_MMVByQgIvzIi1fkWDd7aQL8KvqHiEUzWykpvxeVt89dUBEiNjZVBHVUB55zMs4z2J-Ovsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiOTdWMNySo2VhfNfThI-ywIXi7I-JOuXXEYZCNi37QyfKTMrOo2YD_l50MRnCnrK_hSdIa2coGKoRt6q6Yo5u8EDe7JFyce0-b_pAL9zbI3f9IXEkUP02jMf1XU4InE7vKe5nwSw9Z0u3FhoZm3-ZP3diPtKprhrITVBbYaRVedbMDwjKR2Kytt2aN7zSyafqYtusk8IlXDUGOvguK3OzPQvXS2sFU8ilO5m0LwwHvQdV9o-TAl7BTXyNS0A_llw3i-iDw19YkY0GZ4tPl4RdqTlB1Rp8qdmPrsdTrp1sOcO1t_0jVE1LsvctAY209Vp9_Y1WY9mbVRoUZFGlgOGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامدهای بسته شدن تنگه هرمز
🔹
بر اساس گزارش آژانس بین‌المللی انرژی (IEA)، تنگه هرمز شاهراه حیاتی انرژی و تجارت در جهان است؛ به‌طوری‌که ۵۰ درصد گوگرد، ۳۰ درصد کود اوره و ۲۵ درصد تجارت دریایی نفت عالم از این گذرگاه عبور می‌کند.
🔹
پس از آغاز جنگ و بسته شدن تنگه هرمز، آژانس بین‌المللی انرژی گزارش می‌دهد که اختلال شدید در بازار انرژی ایجاد شده است که آزادسازی روزانه ۴۰۰ میلیون بشکه نفت استراتژیک یکی از مهم‌ترین پیامدهای آن است.
🔹
بر اساس گزارش این آژانس، افت ۳٫۳ میلیون بشکه‌ای صادرات محصولات پالایشی و کاهش بیش از ۲ میلیارد متر مکعبی عرضه هفتگی LNG از دیگر پیامدهای بسته بودن تنگه هرمز است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684052" target="_blank">📅 21:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684046">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1qT88LmZ2WDEC9LR88KgtTgDhkItybpUzXvcL0youJugjtp6q7tUbLmZmlyvnpx3axchaK3NxxZdyiWkQDagj3U8d8cmGHF1hbPcCicUxkdEzbuS7YxoERdgg-Ryz2CF9htzxWota_8j6JyVW-VHfomwDTBRjehAaXXN9MdbUBwW_5hkf-8hCaBnF76ZJo7S8kQDoKKqApJMJa1ZS8G59K10c_88LEXvtGc8WIs9lgnTRtqa50F8FFCuSBkDClGFJZMqiQ991X2TZkdE1_OXSxQwbhClHfsW80IWIBJ5sVDhAh5tixRVcTUH_CvdgXuSABOBL04ENb3xAl1c3LoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhK6RI24KRqoXOamnIK-87lVbK8b05wFe2wy5gUS-cLAG-3-NJt4sJCkdUoX191czJd0hFksVZTDSx5dhzYACeFbnUQnHudywKRBEwCaGAQWxHwtMiMrgCmspEE-3npu0_RTy2p9xGNeTrSe2hYxCHFO9qwDgvBafmXFflNCLpdFz6X5EYxwISQ7NQ7pLmxcWOm2RTZeXkbsMF6HFJZhwZfQXq9ScFlnae-a7rkWN3sKferEub5PsTMi9Udg9FjjlqDdtD2Hp4sA-mSEt_YxfLbBsVDjfz8x1xsl8jGt24jhASw0-2LdzatBe0YNz2V0TZPCet423GWoxyHKKJdMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVzSSh_eJVhuHQBSsC634DQtni89cv2MYup8FH8Hk-fyPWgS37TmgVA4q9zNiLIWLjEvjvxoHDTzFhSFyRhu-CrxLU0NlIzybMhjIv36XHiMrTkeegiLFj_O7Ykc7DcFYPepsEaJ7DwxoQFz7_SPBk3Q9P43Yqhj-o4ytc-GIydYY_vRp2TOsidZvglK78A3EQl15QQ0lPi-s7IcEcJwwcEhHmBGL7tRqrlGPNGha4eAH10Al13VEqFB2n3gF2n090jJglLCMRVXjJPRiYQBXqQcXq_K-DRFZWi1niTVJR1H9fwDaTIsZO4bkHxm1yRn4TL-ilPjBdzDGES4AJRuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyNmAgWGxSkOPGp-wbMt2YpD8PXSSZ1mviUqEBftuDdELPlweXCuL-P_KQ4xwkvJ7JRAjBEcbD-84U93wyckx6F0GfXEsh2B03Nint_oSjjN5vyVbzU2WNnMk2D_GcDct8NE8_aF9wS7bIU0ia0kERy7mI3lYpMgxikKnjsBilp_7V3fo9njHEBnnQ4BTnL-LJQ7o5mSZJSFciNNuXtVTu-CwfuVuyMj_gw9TjFYiH4XNSXHZ_Om_jOBHoIHFsxEP32i3zlLeE1GubOhUwm6DQ6GVfnnfBmfGVAF2QuUcIAlZK-9epnegVqz10TV-m30RqfI4yKHYKr-R-aTBHO1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNRaNsKP_xng1sw4LmW2x7teGa4m11UCJP0Z7Gp7JSSiArUV0g44BbhIe3nP-lSQxrkG_Tydmhiw3kmsixgSyf_lBjabcAL2fIB5wxtKEf1wrhfNT0BR0NXWuvIOcGXHDG509yA6lFca3xUsZZHejZSsFUsyUIsNcr10LPvm_XeR5bw6Z5Du1YalevdvVa-cIi2IdGvHdMLR9aR_TxwbFOLOP06CCbStkAOkFo4M3BGb-YkySsIfiht-scd77V-8_EhaDSOgdS8quvq45IDRPGVGaNZqjD9QZSy6UV-rmiFEEpjTp0C--PxVfzpB__ldUiEGC4VcsITKse9KcvUQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIOcoTUrhauYmn4bgs77h5HRN3_8xoAT_oUaK8QrLaGM-2kxCYZErf2oZfapU3B9zf8MBCKaQO-D57kFrMD4-2Hfe19WY2b-fKx-HnhUevxFrZls-702iWJrv0gjuy3aKw_-kMF2-EfO177-xei67iw74Veb1Mi9uAUJ9-5vbvtaPUShUQtF9ma6Gs3E1zZTP5HR5B4XeVO0LQGR4mYMjk8PDFku9g0JraydbrD4hDIXWfPlztaYfM1cj94P_QBFbTNRaFjEsCxRqXLqv4zm_45HR0F1-kFVUMgBqCiM5UqmD2A4ZMAkQ8wJ8J53yLcSUtfdoBVndkXZQX4XOjfDPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار فرمانده ارتش پاکستان با رئیس‌جمهور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/684046" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684041">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1cqRIHeeDdTtON9y5RxbyMH9wixtvL4SlH19BuRibiUVCaTRZ1k5M5EXakjNuGnOpu9ul13_6NBhGCDwy4SWsqAIOHBTh76iBJoQCPks8Jpr7oEHILCyKoDQqaeLaVNeA6J6dQNN8eQn9FhSUoI4DR5Z9xsZNh8yVGJ6uuziTLiiXXHJEwz9LBH_X_4dUaY6x2ffg-kmafLuawUJI7o1qi4tg7xGiKIRiAyH6fmGSwMXU8Y6V-aMsyq3n3ATsp7hSWabz2_bdCguqDLR22lxZpqF0BZwqzUxvRSiqsAf5A5-Ax4B_whjSAicREtfcf15xovNRkYVUArmVPk9kdOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkV2GRcrxgCEk93amZL_4DZcBEOyk8Zl8ujJxKx0NMCpRpHfYWovLAbFoaJewew1MzUUvNiDiXkSv-fio74EqNZBi9EGYKhytZs05zh9g9MnxY7aade7XlbXl3YBCGWhLjYln-bSm5Ag4isubOoOrHnl3E9TlcJ3AycfM8SYpM97N4p2sfq65FHuXFR6GiA3A6VaZbTHIJClqXPq0y_5wYp5eeLk57RllC2YpBzFfUAwFiXU-KILglCVAoluTwZUZ13e3Z4JbjT0tbUE-g79Cm3YwW35bMQEtsTdFi9DhacylMaS__bmq0oH580lxtsTiQQCkY5hYbuOuDT1qc2QYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-A8x3OXoAH28S1eWEXez1SHFp4FkSP0PFwyEiOu86mqRlISBRxPiuo41LyGEwKT1F81_-wLHgh9SnsQ_mAITIqDYqIV0wTOjHlFi_4AP2dfc16AAPDGWVgKfh5OaliZiO-bB_1OfK7gRuI3TnFRh63NJt0YaC2uBZDxKj6LpQePDiPglWKYLwv9C85m-MQYA1vx-zLlgTZDruht_U5sZG18iSY6RT4sfxqkzJH8PZHEqJkhfOPq7yen6DRoiLwGfIxF6B2v6SwhLqHObl3QZe63xakIO0hSLC363-haygm0U7ttxpHBwgIMhxPKX6C6whP7bitsOzceSRqyaNmzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU6mnI2nLR0Y_iY1Bk15D5pWivQeqto5SL0bOGhcnDlOs3ogWg63tU4ZwfWwyW29Pu2ZQSUhkeswXzVUY9GCwcgiOoWhtx2Gx3VOra4fZquIMn1ued6ubPNlAHRo1V5QPZXg6LIglK0puS2NXht4os_RhUCCSuqeEkPHcgNtYVxtR8OZgEVkecugxS5IZDOhdexS6eKqsx5IrMO14KMmgCo6pBxmQFxoUKLKZv5y8dBF3NU6ioAS1DF7AHUhCOxPrTaabS0UCxvzY4tsr701eGUqYhe5oCT9S0yxljKCvSVLcK3aykWKAEoTV8tmzZTxKwkLFQHAffV8FeDddZECPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvM57MKjulVHFI4LKaJWhArq628brh3CCmSQ_EAI1RrmkA1eTGXNX_R_6EWttEAlol7ujWatPm_1w97bCWkZUVNDGVDsNh0dWz1reLp5CSutGXXU8uc8_PcxjsSYRH5PPgfhPxXInBwyxkTGtXRGQ8-Z5N8-BUNFUtG0uzYVtlDUu_wfww4_zBIzZMwEv2FgZxSsM3BCaLcm2stIJgysrsvoMrYE4cRrH2tOgTFEnWLA8nJpzBoV3DRQoz5BrtDVhhA_HEv6haAo_VQNOxkK3SseAn0fEHXeVbKKn1I1Evu_gAurG24tqP6hZDL8vitFgkI_c4DcxdCAEwEd2nYaww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این سایت‌های هوش‌مصنوعی پاورپوینت‌های درسی و جاری‌تون رو‌ حرفه‌ای‌تر درست کنید
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/684041" target="_blank">📅 21:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684040">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h226wuznLNTlTEivsHTKcPxuSEzETYXsnZdAFL8tncQ71frLGZR4LwvQrCTzSbUNIxs-IT__vuVgUKBOc-_bIsbDLWF2a4hu8qdYZ7_rrPT-wkDh11zQWm3U1WHz3XMNuVgyD0TfVYGe4KTGHUW5SCW6TkaXz2iiTQ5gzjaktiTGpR3c_r2mF_fWDZlP12_-B_TGCCJOJps1a7kmSBqRLx96y713TwKpmosfQktOZqDrFYXr5EYHftJqQKXwha4H1zqvLjgXaAVwRRJudfUWBZUC4BxFtiBG87SLDS4rw8TJkZ5Up5DK2TXN4Hr-CdcnF7-F9TFv-F6HD_AEEI6iHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: پدر ملوان ناو هواپیمابر آمریکا در بازداشت دولت ترامپ
🔹
در حالی که جاشوا آویلس، ملوان ناو هواپیمابر آبراهام لینکلن، بیش از ۹ ماه در خاورمیانه برای ارتش آمریکا خدمت می‌کند، پدر نیکاراگوئه‌ای‌اش در فلوریدا توسط گشت مرزی بازداشت و روانه بازداشتگاه مهاجرتی شده است.
🔹
ملوان ناو می‌گوید مراحل دریافت اقامت دائم پدرش انجام شده و فقط منتظر تأیید نهایی بوده‌اند؛ اما دولت ترامپ با متهم‌کردن او به ورود غیرقانونی، حکم اخراجش را پیگیری می‌کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684040" target="_blank">📅 21:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684039">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guHK-hb6eM6iL1ULCjwe8Nmw9EUe2hH9c5LPYxgYBHg0T1IkZNCNhlBry6SuDzqbC9-rhGAYQC_le0aWTV1vpjRkiWQqACR9P7N4aGnkt2zouZGUiMHyy8ZHlO6gQCLIBvXDRcgbYomPM2pHq5nAL2EPsK2qsJQVkmte1M0oS_SfilKNF3170W_ddn0AY8eVHcGAN0D_ltlyde2-Au37A9hYX8PHbb12nEdcxlC2kgWF9kdd2a_HSFhMZdhMQM7-_LHXsdj7QyqH6aisVCJ0kVK2OfRVUAJMPd22AYRtCuggdcXOrjugJ0cMc5OGgKPByL-MPvCSQUoLaIeGRvKr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدای نسل Z تشریفات روی کاغذ نیست / دلیل ناامیدی جوانان «دیده نشدن» و «نداشتن نقش در تصمیم‌گیری» است
امیررضا احمدی، مشاور نسل Z رئیس شورای اطلاع‌رسانی دولت:
🔹
يك لحظه خودتان را جاي جوان امروز بگذاريد؛ تصور كنيد از صبح تا شب افرادي بنشينند و بدون حضور شما براي زندگي تان تصميم بگيرند، همه آيين نامه ها را ديكته كنند و درنهايت هم خروجي آن تصميمي باشد كه هيچ منفعت يا آورده اي براي آينده تان ندارد. اين دقيقا حكايت نسل Z و حتي فراتر از آن، كل جامعه است.
🔹
بزرگ‌ترين سوءتفاهم اين است كه گاهي در ساختار مديريت كشور فكر مي كنند نسل Z خواسته هاي عجيب وغريب، پرهزينه يا دنبال تنش دارد
🔹
تصور اشتباه اين است كه مديران فكر مي كنند با ارايه يك سري بسته هاي تشويقي فرمايشي، هداياي دستوري يا شعارهاي توخالي مي توانند دل جوان را به دست بياورند؛ در حالي كه جوان امروز فقط و فقط «حق زيستن، استقلال فردي، ديده شدن و حق انتخاب» را مي خواهد
🔹
ما دنبال لطف و نگاه از بالا به پايين نيستيم. ايران خانه همه ماست و فقط مي خواهيم حقوق شهروندي، اصالت و عامليت ما به رسميت شناخته شود.
🔹
نسل Z نه يك ابزار است و نه يك بحران، بلكه فرصت و سازنده آينده ايران است. صداي نسل Z يك تشريفات روي كاغذ نيست، بلكه يك جريان واقعي است./ روزنامه اعتماد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/684039" target="_blank">📅 21:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684038">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ایران رتبه دوم جهان در رشد جمعیت بالای ۶۰ سال!
🔹
شتاب روند سالخوردگی جمعیت در ایران بسیار تامل برانگیز شده است. داده‌های رسمی حکایت از این دارد که ایران تا سال ۲۰۵۰ در میان کشورهای جهان، دومین رشد جمعیت بالای ۶۰ سال را تجربه خواهد کرد. ایران در رشد جمعیت بالای ۶۵ سال نیز رتبه هفتم جهان را خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/684038" target="_blank">📅 21:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0iXwaF4tyidsU9L6dvloh3aKtcSrNMD9JenbV6ONjQmjWEJFHOTCq94gRlwhLbmP5Iol1CHEpWfyL9veEKdT8KSKK1C7bdHXRZ3FBaEXCbDe_fpsTnCWEak52uluLHUamPS9c_9qgpfGEclCKhM9KiBTP1YjHyKlrpfUKAGHRtKNn0MoaxRe7qH2ZP2XypBVGRK5saIQou5bd47ukrRLmV_0lInniUu1HSOHroOaE6eCUwT12b-URW7EyKC_aOMUXjVwuXJrJ_51hbiaGXiR3ZvarwU0l0GlJTBrw9mSJHGqfHQr5LS8Oa1y6mnnQqGEb7GVXkp4CrVqogyhOcSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf7cd6c43.mp4?token=FGZWhY05Ydfn5LyocCzh6OSwp_UaQeTETrgnTzDY8ce-hDll22rt5qnaKc5ic-42MO2ptolVXdGSQnYGHHRaj2uCl8CV6bAVx4KtA_2vYqLCZnQP0vevNq2BthBqkm985XSioJlVF3O2QiPImoxA5O3-j3g5ZioIAKt5zyi8cfb-BeHxrpDH68_UkTZQ74uVW0Jy3DnoAVqA1ubCQGwxKpezo-BnewUG_KzkP3HGv5V5TutuVyo0Ccs9prYwtFeUXDhNg8gRqmVFZsTPw3OuNobJLBNJrKGA0yVcXOFDMRH7_i7KXxF2M9-fhLFh76nw1XcuspE1tMt70jnjKU18wF4MGEiB5dryWlnoyDA2u7v2dvjhFztn9fo0aHIul36LchmM08FnUa6h2aj7yIaCqzHr84DUfgkkNQC-tsexKAqhACiz4rBJN3zwgCcS_HxbPl3TNZI7VLHkP0wiH6wIZ7F0_di55vwaBb5G5eFupWh5ZXk-U8AoOW0bM-l3u_MZ23jiBKTYGRGeXJLtIGHrey-a25UsA0nIac7KGrVDeY7Er9RTtHSysMyLT3VTwAmcF6iQk7phcJ3eWwLpVeIByC26afpPHgIFhV_2T6OSve8-BsQvGLgK3ANvRFTzqJKc-5fwNvoENlm4RPSqCJVNNjJLISDWy7YdXjKpkHMy7UY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf7cd6c43.mp4?token=FGZWhY05Ydfn5LyocCzh6OSwp_UaQeTETrgnTzDY8ce-hDll22rt5qnaKc5ic-42MO2ptolVXdGSQnYGHHRaj2uCl8CV6bAVx4KtA_2vYqLCZnQP0vevNq2BthBqkm985XSioJlVF3O2QiPImoxA5O3-j3g5ZioIAKt5zyi8cfb-BeHxrpDH68_UkTZQ74uVW0Jy3DnoAVqA1ubCQGwxKpezo-BnewUG_KzkP3HGv5V5TutuVyo0Ccs9prYwtFeUXDhNg8gRqmVFZsTPw3OuNobJLBNJrKGA0yVcXOFDMRH7_i7KXxF2M9-fhLFh76nw1XcuspE1tMt70jnjKU18wF4MGEiB5dryWlnoyDA2u7v2dvjhFztn9fo0aHIul36LchmM08FnUa6h2aj7yIaCqzHr84DUfgkkNQC-tsexKAqhACiz4rBJN3zwgCcS_HxbPl3TNZI7VLHkP0wiH6wIZ7F0_di55vwaBb5G5eFupWh5ZXk-U8AoOW0bM-l3u_MZ23jiBKTYGRGeXJLtIGHrey-a25UsA0nIac7KGrVDeY7Er9RTtHSysMyLT3VTwAmcF6iQk7phcJ3eWwLpVeIByC26afpPHgIFhV_2T6OSve8-BsQvGLgK3ANvRFTzqJKc-5fwNvoENlm4RPSqCJVNNjJLISDWy7YdXjKpkHMy7UY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از پودر دست‌ساز تا ظروف سنگ مصنوعی؛ ایده‌ای برای کسب درآمد خانگی
🔹
این بار در
#چرخ_زندگی
سراغ ساخت ظروف سنگ مصنوعی رفتیم؛ محصولاتی دکوراتیو که می‌توان با مواد اولیه نسبتاً ساده و کمی خلاقیت تولید کرد.
🔹
ساخت و فروش این ظروف می‌تواند برای علاقه‌مندان به کارهای هنری، راهی برای شروع یک کسب‌وکار خانگی و ایجاد درآمد باشد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/684036" target="_blank">📅 21:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684035">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4e204fdb.mp4?token=Jwq5-Vy5ZKra68TklFcFmnGbZpMgwXdzP-9FjsEV43urNqgh3aY_CQIiAiC1YszlS2RCZDAwEXWT-eqdJtsQbBLoOJs73eJ8Qmo31Gi34nu9lkbt-KnVuMGTCizGsgM1IxQQ6S3NsSRqEb3X4LXSxfe7ImgHOGknKF5eSf-egnTK-vZmvPU3U8ER512gdWN73tXIrzRS5xEcdf0Q16pQDiNu49nosoVa_P7fE4hnVeCySzY70I8oDpG-5QJHaGwFMzY6kAS4Tm7hwZ4vuCz45OxxUuRX7691eYVk5BsUuSUQH7Z5UlyERM21NwaICRViJ9AIj9NJfo8Mewh8SaFX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4e204fdb.mp4?token=Jwq5-Vy5ZKra68TklFcFmnGbZpMgwXdzP-9FjsEV43urNqgh3aY_CQIiAiC1YszlS2RCZDAwEXWT-eqdJtsQbBLoOJs73eJ8Qmo31Gi34nu9lkbt-KnVuMGTCizGsgM1IxQQ6S3NsSRqEb3X4LXSxfe7ImgHOGknKF5eSf-egnTK-vZmvPU3U8ER512gdWN73tXIrzRS5xEcdf0Q16pQDiNu49nosoVa_P7fE4hnVeCySzY70I8oDpG-5QJHaGwFMzY6kAS4Tm7hwZ4vuCz45OxxUuRX7691eYVk5BsUuSUQH7Z5UlyERM21NwaICRViJ9AIj9NJfo8Mewh8SaFX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملیات انفجار و تخریب بزرگ صهیونیست‌ها در شهرک میس‌الجبلِ لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/684035" target="_blank">📅 21:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684034">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دولت ثروت مازاد خود را بفروشد!
🔹
در روزهایی که اقتصاد زیر فشار تحریم‌های ناجوانمردانه آمریکاست، دولت بیش از همیشه به تصمیم‌های دشوار اما ضروری نیاز دارد.
🔹
یکی از همین تصمیم‌ها، فروش اموال و دارایی‌های مازاد دولتی است، نه به عنوان یک انتخاب فرعی، بلکه به عنوان اقدامی که باید با جدیت در دستور کار قرار گیرد.
🔹
دولت سال‌هاست مالک زمین‌ها، ساختمان‌ها و املاکی است که بسیاری از آنها نه برای مردم ارزش‌آفرینی می‌کنند و نه برای اقتصاد.
🔹
دارایی‌هایی که در سکوت، گوشه‌ای از ترازنامه دولت خاک می‌خورند در حالی که همان دولت برای تأمین هزینه‌هایش با کسری بودجه دست‌وپنجه نرم می‌کند.
🔹
در چنین شرایطی، فروش دارایی مازاد می‌تواند بسیار کم‌هزینه‌تر از خلق پول باشد.
🔹
چاپ پول، باری تازه بر دوش اقتصاد می‌گذارد اما فروش یک دارایی غیرمولد، می‌تواند آنچه را سال‌ها بی‌استفاده مانده، به منابع مالی تبدیل کند.
🔹
دولت هم‌زمان می‌تواند آن دارایی را به دست بخش خصوصی بسپارد تا شاید از دل زمین و ساختمان خاموش، سرمایه، تولید و اشتغال متولد شود.
🔹
اما این کار، مدیرانی شجاع و حرفه‌ای می‌خواهد، مدیرانی که بدانند نگه داشتن هر دارایی، لزوماً نشانه ثروتمند بودن نیست. گاهی ثروت واقعی در توانایی تبدیل دارایی راکد به فرصت است.
🔹
البته مسیر آسان نیست. بروکراسی، مقاومت دستگاه‌ها، قیمت‌گذاری، تغییر کاربری و مزایده می‌تواند این تصمیم را فرسوده کند.
🔹
اگر دولت دارایی مازادی دارد که برای اداره کشور ضروری نیست، باید آن را شفاف، حرفه‌ای و منصفانه به فروش برساند پیش از آنکه برای تأمین هزینه‌های امروز، از جیب فردای مردم خرج کند.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/684034" target="_blank">📅 21:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684033">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bedb53e8b.mp4?token=AXqvaUP8Q9vK3e3-gqudx5NJRK3NCt4nNkA5lQJvi3GUpJW55D-mhGlTjMJTvs6HhHaR6RRoRc_OvMOwNxuT-0Y7QjRYhNVeFdfJq9mcDP89wGGNObq8UatqxCuZI7jOWXLC1jKW9hhJbhxq__y7fw5kUJRYsF026L5r-tpaeB6K5j4IPaU1AIKdo88stzpsQIgUBumT-qjSkJhtZDpZvt3gnpXbC0sHGVxoZramnz-nK6jDa0qkGVU5x0bnUhzusf5IwVymrLRb_vXmEwhof4KlsKfk7soWgAh0Cq9lw7UJy-A4oICSUxvFI5Bru1_PLANywF9SL3fBXmAMKFCRzYviIjaYA6qTXyR9Wrak6694IZPL_JcG7zC-TbkzwcB1E69yw641MZQ4piku7NMYM8ndkZO2_nchjBJDXlUiIkZEYeq0QsKx8siF11tfFHQByZpvFXf-7BjC0zYZdSwb8qim_D7Sj1ofAabtg502B0TJpqUAau4sq506jMmaStE5e1u2IrD9GEYJaGKBspQSWT7xxO6_ftx_fw0Wf9ybKpXb5AyByHnC_V1p3WPf-Gb7wKMSfd-mi2Ua22Szz4T-48ApRTjUQw_HmPgwB1FI6RrnR0KGYsKvna8q0vr3czYqYUeFbvo4wM_XCB-5z8l2Zf25cA6nGEbqxFSu9GAwBP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bedb53e8b.mp4?token=AXqvaUP8Q9vK3e3-gqudx5NJRK3NCt4nNkA5lQJvi3GUpJW55D-mhGlTjMJTvs6HhHaR6RRoRc_OvMOwNxuT-0Y7QjRYhNVeFdfJq9mcDP89wGGNObq8UatqxCuZI7jOWXLC1jKW9hhJbhxq__y7fw5kUJRYsF026L5r-tpaeB6K5j4IPaU1AIKdo88stzpsQIgUBumT-qjSkJhtZDpZvt3gnpXbC0sHGVxoZramnz-nK6jDa0qkGVU5x0bnUhzusf5IwVymrLRb_vXmEwhof4KlsKfk7soWgAh0Cq9lw7UJy-A4oICSUxvFI5Bru1_PLANywF9SL3fBXmAMKFCRzYviIjaYA6qTXyR9Wrak6694IZPL_JcG7zC-TbkzwcB1E69yw641MZQ4piku7NMYM8ndkZO2_nchjBJDXlUiIkZEYeq0QsKx8siF11tfFHQByZpvFXf-7BjC0zYZdSwb8qim_D7Sj1ofAabtg502B0TJpqUAau4sq506jMmaStE5e1u2IrD9GEYJaGKBspQSWT7xxO6_ftx_fw0Wf9ybKpXb5AyByHnC_V1p3WPf-Gb7wKMSfd-mi2Ua22Szz4T-48ApRTjUQw_HmPgwB1FI6RrnR0KGYsKvna8q0vr3czYqYUeFbvo4wM_XCB-5z8l2Zf25cA6nGEbqxFSu9GAwBP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکات بسنت، وزیر خزانه‌داری آمریکا: هر نهادی که به نمایندگی از ایران پولشویی کند، از نظام مالی مبتنی بر دلار آمریکا حذف خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/684033" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684032">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5ae27fa7.mp4?token=FaWg41RJZckGgzD6PLM7cFToiJD0ud_OHHiwxhFeDBNUPf808XaoV5e8oPtl1QeZFvWI3LWDZaAo5HZSwZSHHNHJ4mTnMv6GwctUSIpq2sgnV8qKuC7R8AGPNNj_-J8f4i42aEDQlqVTSAUJBSubP_sT3dEuVokEu-i-AK1ajXCerVPmG3T4EY4aahaFgSf4GdodrSVhTLVUauvLp1Uko1ys0t80dSQePgj3CsiMdtnNsR08t3rdMknVmTM15tip7rJWwpYGLZ0rImOU069U_tpPgHkXT61t-iRJ9d9_NSLwAfTjOd0jxxhJHiX1pl3nZGCPGBYMulbCoEOZ4_Sicg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5ae27fa7.mp4?token=FaWg41RJZckGgzD6PLM7cFToiJD0ud_OHHiwxhFeDBNUPf808XaoV5e8oPtl1QeZFvWI3LWDZaAo5HZSwZSHHNHJ4mTnMv6GwctUSIpq2sgnV8qKuC7R8AGPNNj_-J8f4i42aEDQlqVTSAUJBSubP_sT3dEuVokEu-i-AK1ajXCerVPmG3T4EY4aahaFgSf4GdodrSVhTLVUauvLp1Uko1ys0t80dSQePgj3CsiMdtnNsR08t3rdMknVmTM15tip7rJWwpYGLZ0rImOU069U_tpPgHkXT61t-iRJ9d9_NSLwAfTjOd0jxxhJHiX1pl3nZGCPGBYMulbCoEOZ4_Sicg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: ترامپ با رهبران کشورهای مختلف جهان تماس می‌گیرد و از آنها می‌خواهد تعاملات خود با جمهوری اسلامی ایران را متوقف کنند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/684032" target="_blank">📅 21:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684031">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10b3915dd1.mp4?token=aeN60B7bcHQoyxtUG6mO2S61Og51qW0W_qzov_snD_Yq4fSk3lk2sh4HZOfp-bKy47EjdSCQ6KR9JKJ-sPRLXEv_uKMXBUEE2H-Mmr3WEridPkgcUzt5cAXQDEpI00MHt3TY6GV87ljIMorz5HHDDWfi7ccgrh_CT5SyOwVRGxbWtVJCMYnYmM1LoC2Vl_YddgvTVrNctiVaa7-UGnXf4kVPY96GsvATHvw5oIekz2VeifCDvxj9OTvmk8KqFJJhOVU2uzCl1NhXWfmdled8YXAh2nfxHlM1QqyP5GCjiZ0HSXr-iweW37EDkmNKYl5CitC-ymZni2ktT8IZcKhvPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10b3915dd1.mp4?token=aeN60B7bcHQoyxtUG6mO2S61Og51qW0W_qzov_snD_Yq4fSk3lk2sh4HZOfp-bKy47EjdSCQ6KR9JKJ-sPRLXEv_uKMXBUEE2H-Mmr3WEridPkgcUzt5cAXQDEpI00MHt3TY6GV87ljIMorz5HHDDWfi7ccgrh_CT5SyOwVRGxbWtVJCMYnYmM1LoC2Vl_YddgvTVrNctiVaa7-UGnXf4kVPY96GsvATHvw5oIekz2VeifCDvxj9OTvmk8KqFJJhOVU2uzCl1NhXWfmdled8YXAh2nfxHlM1QqyP5GCjiZ0HSXr-iweW37EDkmNKYl5CitC-ymZni2ktT8IZcKhvPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گنده‌گویی بسنت: آمریکا منابع درآمدی سپاه و حکومت ایران را مسدود می‌کند  اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
از امروز، حلقه فشار را تنگ‌تر خواهیم کرد و هر منبع درآمد احتمالی را که به تأمین مالی سپاه پاسداران و حکومت ایران کمک می‌کند، مسدود خواهیم کرد.
🔹
ما…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684031" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684030">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منبع عالی‌رتبه امنیتی به شبکه المیادین: واشنگتن تمامی ابزارهای فشار خود علیه ایران را سوزانده است؛ چیزی برای اجرا نمانده!
🔹
شبکه المیادین به نقل از یک منبع عالی‌رتبه امنیتی سیاسی در ایران، اظهارات دونالد ترامپ مبنی بر اعمال فشارهای اقتصادی جدید علیه تهران را پوچ و صرفاً تبلیغاتی دانست.
🔹
ایران معتقد است ادعاهای ترامپ در واقع پروپاگاندای رسانه‌ای و طرحی برای افزایش فشار روانی بر مردم ایران است که توسط تیم تبلیغاتی او تدوین شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/684030" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684029">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXivjl0jk_IZ1ocgHGESUNwpOUimAN-VLzL_UwSFq4HLWrhROV-GUYzN6mOD9oAEEW6SMv_CY7-FwCHApVm3qD7oCFyJH8gOHrIPMRrlxLxL7qxFiijgrAB7hHtVX-k6QtP1-QxkC02d4eINUkGikR-0bKwprs-xsDnVBaHLfct7pEBXF4kJqhF6Bhf7HGoinhFHFZXkoZVll7oflSU1s3NvvLknZ3NYlvAJiTzJk6SOKRDm2uOboMFIEn43TtRv_Dt67zqf9k5CtY-3skBWbMF82WYf3Fl09eoR9Yi7_D2QCCZDClPmLE7oe3w1-SBu5Bl-KXWKEKx_2JBoNLGHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا ۲ میلیون تومان تخفیف با کد PNTHRD
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/684029" target="_blank">📅 21:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684028">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد
سرلشکر رضایی در دیدار با فرمانده ارتش پاکستان:
🔹
آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/684028" target="_blank">📅 20:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684027">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9efd624f88.mp4?token=iHuJFkxDoImp7kiQurJR5CXnEiSTMUt5eRzEFppKD7aIbqEdWKsngAzxZotf6xR9Qaouxl3hVULOQ6M7moddFdjHBYFxsqYzbBTZg7gcVnEaP_MRWmu0EvJo4GRqroc36UXbtxwKYzCrGHKMbRLpEdhqumuZXtiKarEMKZcY5oDlhbxbALsVmebv39NTxKTtz_ZtvDaC8doWZHlp48IPSFNTLtswgIkm8gVt5zaVEz2DdPjdgAbCoupX7NxygfWUq5N5lz0rJDwEuOcT0LXLQBBHe0tPvF5IJ_o1xVUqd44rgqyc5ib1M83_Uue6IexVmK5ZtEA-l2KrOLDHtyvH7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9efd624f88.mp4?token=iHuJFkxDoImp7kiQurJR5CXnEiSTMUt5eRzEFppKD7aIbqEdWKsngAzxZotf6xR9Qaouxl3hVULOQ6M7moddFdjHBYFxsqYzbBTZg7gcVnEaP_MRWmu0EvJo4GRqroc36UXbtxwKYzCrGHKMbRLpEdhqumuZXtiKarEMKZcY5oDlhbxbALsVmebv39NTxKTtz_ZtvDaC8doWZHlp48IPSFNTLtswgIkm8gVt5zaVEz2DdPjdgAbCoupX7NxygfWUq5N5lz0rJDwEuOcT0LXLQBBHe0tPvF5IJ_o1xVUqd44rgqyc5ib1M83_Uue6IexVmK5ZtEA-l2KrOLDHtyvH7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده گویی بسنت: آمریکا حمله اقتصادی به شبکه‌های مالی ایران در سراسر جهان را آغاز می‌کند  اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
ما یک تهاجم اقتصادی علیه ارتباطات مالی ایران در سراسر جهان آغاز می‌کنیم. هدف ما قطع کردن تمام شریان‌های اقتصادی است که این رژیم…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684027" target="_blank">📅 20:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684026">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc411dd662.mp4?token=LsuPYOJym4vXhBwbb6B0iMFEWYwIMXTp6aBMlhyadQBCoR1NHKqaXGPkhK6N5lClgGK3TiszGG7UfRhI01g-jezKf4jQjydc67FqoBzHQbZDWZX31HGbVOaU51nyp6IfopCv0msAYXVfMwOxhdyhrdV-DHI_BlxiOaIIYGYN3k7GTVtMZlGSSNSv-XeoBfC587ANW7bE0210Y8j3QfDDXLEbjNG2ZJTPMrx2C3GFYcG09zhnQk399Ohry3Vf_L3wAOfHV8MbU-kgIsvMWvBOW5phFM7bqY-3WYh_G3ZMJ2LqO8-__HBXWdoPvC-T5gus2s4vw9ehj59ktKkdBauuJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc411dd662.mp4?token=LsuPYOJym4vXhBwbb6B0iMFEWYwIMXTp6aBMlhyadQBCoR1NHKqaXGPkhK6N5lClgGK3TiszGG7UfRhI01g-jezKf4jQjydc67FqoBzHQbZDWZX31HGbVOaU51nyp6IfopCv0msAYXVfMwOxhdyhrdV-DHI_BlxiOaIIYGYN3k7GTVtMZlGSSNSv-XeoBfC587ANW7bE0210Y8j3QfDDXLEbjNG2ZJTPMrx2C3GFYcG09zhnQk399Ohry3Vf_L3wAOfHV8MbU-kgIsvMWvBOW5phFM7bqY-3WYh_G3ZMJ2LqO8-__HBXWdoPvC-T5gus2s4vw9ehj59ktKkdBauuJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده گویی بسنت: آمریکا «عملیات طرد اقتصادی» علیه ایران را آغاز کرد  اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
امروز، وزارت خزانه‌داری آمریکا عملیات «طرد اقتصادی» را آغاز کرده است؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/684026" target="_blank">📅 20:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abecb4465f.mp4?token=nvQZ8Rjp5lVfQnw9yda149hjnNK3LNf5LTtOXO25yFGLtZHX3QT4iQ0vxxg01-Y-HJ2dTo4O4UPVPd_wkgjfYhqf7XFIBie6jMPQxDAJ3h5MK5eJLf5iYG9vHwz6q34P6pNmJ_XREsKSnZ3bnfPZFfRSuq2T4f2dGvAyOCymY9x8TpU2WeMhUhYLlWgh_7LAA0YSKwT2yfCLllU_nB1Zr24XH7csdOR9JeItfEq0P7oGB5ChTcH0XNTxc4ZXFaASD76vVK07LtCwI5ajas91PM-uL6TfkRFauNYV0YFtRfo75ua1I03WHgB3aNmhJ8LDWoGxzdhkGHRB82TnSDIaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abecb4465f.mp4?token=nvQZ8Rjp5lVfQnw9yda149hjnNK3LNf5LTtOXO25yFGLtZHX3QT4iQ0vxxg01-Y-HJ2dTo4O4UPVPd_wkgjfYhqf7XFIBie6jMPQxDAJ3h5MK5eJLf5iYG9vHwz6q34P6pNmJ_XREsKSnZ3bnfPZFfRSuq2T4f2dGvAyOCymY9x8TpU2WeMhUhYLlWgh_7LAA0YSKwT2yfCLllU_nB1Zr24XH7csdOR9JeItfEq0P7oGB5ChTcH0XNTxc4ZXFaASD76vVK07LtCwI5ajas91PM-uL6TfkRFauNYV0YFtRfo75ua1I03WHgB3aNmhJ8LDWoGxzdhkGHRB82TnSDIaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفته سوم لیگ برتر؛ تعویض طلایی نکونام و پیروزی لحظه آخری تی‌تی‌ها در دومین بازی بزرگ هفته
🔹
تراکتور بعد از ۷ سال در یادگار امام پرسپولیس را شکست داد
🔹
تراکتور ۱ - ۰ پرسپولیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/684025" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تجربه تلخ خرید طلای تقلبی در بازار!
🔹
«از ۴ تا سکه‌ای که میخواستم بفروشم ۳‌ تاش تقلبی بود.»، «با هر برند و هلوگرامی توی بازار سکه تقلبی ریختند.»
🔹
با افزایش قیمت طلا و علاقه مردم به سرمایه‌گذاری در این حوزه؛ شاهد موج جدیدی از طلای تقلبی در بازار هستیم
🔹
مسئولان اتحادیه می‌گویند مردم خودشان باید زمان خرید دقت کنند و امکان نظارت بر همه فروشندگان نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684024" target="_blank">📅 20:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684023">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b49fad62e.mp4?token=oLsLdKLARYtyYLLeTruNrMbvMjgIdH3fR8ioXeHT0gRHpNENi5PH_4nNXrdeH5ItblwQypFxnKqENkXUJmDn28RIdQMdid0tUrm6Nf-LgHT4HoVdECpGMzSdA2s6KUGh7BHMX9DFZoGWTN3BbRfrTXWIkJQuGDvOVJbfqkwCqtIQhNcrzJGa6RtvPncJTrIRbi3FCWl3VN9Q1xgkYh8I6kEAcPnMI0_DPp3c2oam6wwiKXj8N2fatkKF2Yu-J4HvXVEUjh-IO9w-lPkqwEx2u7-JhEG-6xkPmPEOB0JLsaqQxM3xmfmFtH5kDF3nO5V9xpHTBqISpwHRf7grbM16Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b49fad62e.mp4?token=oLsLdKLARYtyYLLeTruNrMbvMjgIdH3fR8ioXeHT0gRHpNENi5PH_4nNXrdeH5ItblwQypFxnKqENkXUJmDn28RIdQMdid0tUrm6Nf-LgHT4HoVdECpGMzSdA2s6KUGh7BHMX9DFZoGWTN3BbRfrTXWIkJQuGDvOVJbfqkwCqtIQhNcrzJGa6RtvPncJTrIRbi3FCWl3VN9Q1xgkYh8I6kEAcPnMI0_DPp3c2oam6wwiKXj8N2fatkKF2Yu-J4HvXVEUjh-IO9w-lPkqwEx2u7-JhEG-6xkPmPEOB0JLsaqQxM3xmfmFtH5kDF3nO5V9xpHTBqISpwHRf7grbM16Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده گویی بسنت: آمریکا «عملیات طرد اقتصادی» علیه ایران را آغاز کرد
اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
امروز، وزارت خزانه‌داری آمریکا عملیات «طرد اقتصادی» را آغاز کرده است؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/684023" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684022">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21936b253f.mp4?token=JR71aA4Hu6eD38r27giJ8TnyFXAn9_oHiX-5Pjqr1yu4H0sQcnmWNbQKUNM6yyRCpbWNLSMfeQ9lEyGniNkIQ9JpTLS7PjlLgKeiDiFVKhJJkB5OcCNFXyb3AyotYSaXhDzpkeiPd9ms0Zs2mh7DCSpRwB64G1oZfrtap1VDkrXqpb_uGso9S56sQ3eRxEy61Yy4jnOxwnAFd9gdnTe5JSNZncP0sh-LX0tYAM04KhzFvG1Ws-eeAtjkhaISFIa_cQ3BxkwLi9NZ1nAJTZIGQvmj43z-QySR8KaPSv3koNDcdAaA_La91tapIrgkQdg496S6hMtDjGzhtZI-6pYiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21936b253f.mp4?token=JR71aA4Hu6eD38r27giJ8TnyFXAn9_oHiX-5Pjqr1yu4H0sQcnmWNbQKUNM6yyRCpbWNLSMfeQ9lEyGniNkIQ9JpTLS7PjlLgKeiDiFVKhJJkB5OcCNFXyb3AyotYSaXhDzpkeiPd9ms0Zs2mh7DCSpRwB64G1oZfrtap1VDkrXqpb_uGso9S56sQ3eRxEy61Yy4jnOxwnAFd9gdnTe5JSNZncP0sh-LX0tYAM04KhzFvG1Ws-eeAtjkhaISFIa_cQ3BxkwLi9NZ1nAJTZIGQvmj43z-QySR8KaPSv3koNDcdAaA_La91tapIrgkQdg496S6hMtDjGzhtZI-6pYiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه ونس به شرکای آمریکا: کانادا و چین در سیاست‌های تجاری بدترین هستند
جی‌دی ونس، معاون ترامپ:
🔹
کانادا و چین بدترین کشورها در زمینه سیاست تجاری در جهان بوده‌اند.
🔹
چین بزرگ‌ترین رقیب اقتصادی ماست و چنین رفتاری از آن قابل انتظار است؛ اما من انتظار چنین رفتاری را از کانادا نداشتم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/684022" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684021">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
زیان انباشته بانک‌ها ۳ برابر شد
🔹
ترازنامه بانک‌ها یک هشدار جدی را نشان می‌دهد. زیان انباشته شبکه بانکی از حدود ۱٬۹۰۲ هزار میلیارد ریال در سال ۱۳۹۸ به ۵٬۸۸۵ هزار میلیارد ریال در نیمه نخست ۱۴۰۳ رسیده است.
🔹
یعنی در کمتر از ۵ سال، زیان انباشته بیش از ۳ برابر شده است. اما نکته نگران‌کننده‌تر، تمرکز این زیان‌هاست، بخش بزرگی از آن در چند بانک ناتراز متمرکز شده و بانک منحل شده آینده با فاصله در صدر قرار دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/684021" target="_blank">📅 20:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684020">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmszuJ1fZSLtEJAlZYuvuMftDk4hlSaVLtYwwPuaSqRrGNMFgEiDQveYuk8RX1MDiKVmufodoIO34nCF4xAfGr7lh2qlAhP8Ml6WK9fTjcCQ5h0QIjDc3PXeQM8uRcIAq3MbXy1vFEPRAA68IZCQKiNIyE7x2n8A9L9BES-CuxuJkPb2JYy1JBPpoYfWL4ll9ZUDarDRyGROSrpRgBxXiH80nAnssiBwnc98_XG7En4uIRfCQ7XmLj3XhZR4ctF1G21yZe9fmHTsesVcdXoOxGVrWIpd0-UgXP7YWh-qxgkaGnG7GOel-nJtrqR3lKW8VQ7ZG7_XuK9yxR7qNFotEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: کسی گُنده‌لافی‌های آمریکایی‌ها را باور نمی‌کند/ شرکای تجاری ایران به ما پیام داده‌اند که تهدیدهای آمریکا را به هیچ جا حساب نمی‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/684020" target="_blank">📅 20:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684019">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40949b4013.mp4?token=ZeEekAlqMZ6VwCjLctWzuDU5Bfh0K8ANvJTmNx0hmdmlAFanFQh1gCE2RQWz0IJsW9yohQfqUgnwox_cAl9yrD9iw35H_rW2v1ReWhJ4NJd2gNE6P5ppK-ya2LNfMje7q0wjmC6hAh2NZ0DKEgW8xqGIuA9t1TExdnUPXnyULMejuFX8FfB1b7JGoXqrwmbX5TinoiENu9coqsCUfab1rsCFJE8rSE4yAoFEByQd0MlbQO_b5-Nm_bp3z5xgPX9kV245oQV85llZbRNb0aJdD24C1SBNxwMvokC4AE1_tAp3gVRl0Q62Xd3d4vXhIwJwTWLG4GqB_OF4GTB8h6AKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40949b4013.mp4?token=ZeEekAlqMZ6VwCjLctWzuDU5Bfh0K8ANvJTmNx0hmdmlAFanFQh1gCE2RQWz0IJsW9yohQfqUgnwox_cAl9yrD9iw35H_rW2v1ReWhJ4NJd2gNE6P5ppK-ya2LNfMje7q0wjmC6hAh2NZ0DKEgW8xqGIuA9t1TExdnUPXnyULMejuFX8FfB1b7JGoXqrwmbX5TinoiENu9coqsCUfab1rsCFJE8rSE4yAoFEByQd0MlbQO_b5-Nm_bp3z5xgPX9kV245oQV85llZbRNb0aJdD24C1SBNxwMvokC4AE1_tAp3gVRl0Q62Xd3d4vXhIwJwTWLG4GqB_OF4GTB8h6AKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک ترفند ساده میتونی شارژت رو درست کنی #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/684019" target="_blank">📅 20:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb175d00c.mp4?token=i9Ws1SW6fFa4VdvgXMlJKYH4WBxlnXOIwlzgCUf0T-lzUBTriJK52BTdUcXWFm9up3zqHVK2bzjZCtMVrR9F8JChFjA6iupEJBwPe4R6w49e_Ih6RgHQbUlipIbhP5ytZWAWZeT5EGezHjZG9KJL1Saj_4Dp60ZZOt8YBmMSzxJgfQY9o42RpSVob93Sn8MCRQdasa-PnACiCBQJ7Tt6Hep-x_UsoE6I4ExDuJS1MhRuk7b72DVa_o_hrUrbCPuMO1HAOe1F3ZVS-blfGhNnafHGKS-qI4MPqmjJS4YKir3R1FmqomjYG2qMGWRB8rxL7L6IQfw8wxLhNFBgOVwdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb175d00c.mp4?token=i9Ws1SW6fFa4VdvgXMlJKYH4WBxlnXOIwlzgCUf0T-lzUBTriJK52BTdUcXWFm9up3zqHVK2bzjZCtMVrR9F8JChFjA6iupEJBwPe4R6w49e_Ih6RgHQbUlipIbhP5ytZWAWZeT5EGezHjZG9KJL1Saj_4Dp60ZZOt8YBmMSzxJgfQY9o42RpSVob93Sn8MCRQdasa-PnACiCBQJ7Tt6Hep-x_UsoE6I4ExDuJS1MhRuk7b72DVa_o_hrUrbCPuMO1HAOe1F3ZVS-blfGhNnafHGKS-qI4MPqmjJS4YKir3R1FmqomjYG2qMGWRB8rxL7L6IQfw8wxLhNFBgOVwdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادتی که باعث می‌شود شما پولدار نشوید!
🔹
یک دام ذهنی ممکن است شما را سال‌ها بدون اینکه متوجه شوید گرفتار کرده باشد.
🔹
بعضی‌ها فکر می‌کنند پولدار نشدن نتیجه درآمد کم است؛ اما گاهی مشکل جای دیگری پنهان شده.
🔹
این ویدئو را ببینید چون باور داریم که حتما کمک‌تان خواهد کرد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/684018" target="_blank">📅 20:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684016">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">03 Ane Manaee (1403-07-26) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684016" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه سوم
حجت‌الاسلام امینی‌خواه:
🔹
شهید ۲۱ ساله؛ پرواز عارفانه به سوی حق [2:22]
🔹
سیر و سلوک در عصر شتاب؛ شهادت، میانبر راه آسمان [3:59]
🔹
جهاد؛ عرفان عملی در میدان نبرد [5:33]
🔹
کافران؛ بازیگران نقشی شکست‌خورده [9:20]
🔹
چرا مؤمنان در دنیا و آخرت پیروزند؟ [12:41]
🔹
قرآن؛ چراغ راه مؤمنان در فتنه‌ها [15:16]
🔹
آزمون صبر: تا کجا باید منتظر ماند؟ [23:41]
🔹
حکمت‌های الهی در مسیر آزمون و اعطا [31:33]
🔹
فتح پس از مقاومت: مسیری روشن به سوی آینده‌ای بهتر [34:21]
🔹
خداوند انتقام گیرنده: وعده پیروزی بر ظالمان [38:28]
🔹
وقتی ملائک، سرباز شهید سیدحسن نصرالله می‌شوند [49:52]
🔹
صدای حق در برابر باطل: داستان شهید آرمان و ایستادگی او [50:26]
🔹
مکر الهی: فیلم‌هایی که پرده از جنایت‌ها برمی‌دارد [53:23]
🔹
از کوچه پس کوچه‌های محله تا کتابخانه‌های جهانی: سفر کتاب سلام‌ بر‌ ابراهیم [58:08]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/684016" target="_blank">📅 20:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqA6Y5Y0ZqamT2ihaXtpd6RecqfMqFAHlQmeqjBnFknksovDKx9ERDZj_7P76pYzD2YTy_cm6fI1Kjk7M3jdhcClnDSEx6iKJVzzxyI2YCGWWARMxscZrBkHsjCcS1NlAWqdkt6GMmjj7Jadh0q3R6EzAgG1kFwfkrLj4Gg_t5fZVuraaAIlmKVrldDjnzkTPCXT3zWqJkZrDxAUUXMJOLD4HrOjUmRVi04XRGfCC8X_1mI-45ajews3NPh4lGkZio8OrUDf_XhHIALVAOwIJ0KanjWh1lmF1nC0k0_jGSGGFSRdWPQUr3kkIhwR5-gH0oXFtPEHQ5wrS6MsDiq_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفن ابری فونیک، بدون دردسرهای راه اندازی
برای راه‌اندازی تلفن شرکت لازم نیست سرور و تجهیزات بخرید یا متخصص VoIP داشته باشید.
✓ بدون خرید تجهیزات
✓ ضبط و گزارش‌گیری تماس‌ها
✓ تلفن گویا (IVR) و صف تماس
✓ بدون نیاز به زیرساخت پیچیده
✓ مناسب تیم‌های دورکار و چندمکانه
✓ مدیریت ساده‌تر تماس‌های پرتعداد مشتریان
تلفن کسب و کارتان را هرجا که هستید همراه خودتان داشته باشید.
🎁
تست رایگان ۲۴ ساعته فونیک
https://isp.abrenik.com/fonik</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/684015" target="_blank">📅 20:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای جدید نتانیاهو: ایران قصد ترور یکی از اعضای خانواده‌ام را داشت
🔹
بنیامین نتانیاهو، نخست‌وزیر درمانده رژیم صهیونیستی، در چرخشی تازه برای فرار از بحران‌های داخلی و شکست‌های پی‌درپی میدانی، مدعی شد که ایران برای ترور یکی از فرزندان او برنامه‌ریزی کرده بود.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/684014" target="_blank">📅 20:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe1319de9.mp4?token=ARVlJ7tDLH2ZmZ-5t3aYzKNSN-o5_VMxdGUF3YBr8b2EdcTl1Hfy5yKVdE6Y8T-fv4FYfGRP_NylLllItFkjeaTqWZWLQ1lSdKsM6YKLh_twahIfXpRx7V8XDytIzrqsvaOqEkyZZY9bANHdMG_nLplqGemp_b1aFCKywhQgOMfczxg54qq8zeXxtQpt2SjbxG2DqHeaduLob5_SgsDjgoLCCWa3ZqYpPcWSPqQCCH1GptPTPuprJhpLqPcYuir_F8azvqdWoW89UzFlXMTBWfGtZqKTlaJOM3ScWJhoZJkMMoiDQT10F2WEvkUE-Zond6iu1e09F7gVXkHGD0i617RZcy4_U1HOLOsoufEkJ5fRPkDUPzGvpBv8abLqG75IAxW0Ej7nJacmFXAHaC1BxjYl4_WI6SID23TxnFWtfSNV5K5aaUNT6mS76YatjCs-zOx9VrnvacNRUW6SI7uUHCwFeOw4W0gZesAeaU4RBqOLIqLnYwSjZ6nXqY5BBkJnlMM9SSHZklAqJumGPTzm3PSYhw-UaVNh3Tww-9VhhTdcrIS_TpRx8BIwA5i77dtaNqVYRsC9Orx_GRqu5y2xMEaCUTsooTxzcVz_ptraGnvLgxLNCkcc_UlPMuSsN6I9QSYTZfxG8VI8AftWUDU8hU5dOqX_BS_xrpnRNoIctRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe1319de9.mp4?token=ARVlJ7tDLH2ZmZ-5t3aYzKNSN-o5_VMxdGUF3YBr8b2EdcTl1Hfy5yKVdE6Y8T-fv4FYfGRP_NylLllItFkjeaTqWZWLQ1lSdKsM6YKLh_twahIfXpRx7V8XDytIzrqsvaOqEkyZZY9bANHdMG_nLplqGemp_b1aFCKywhQgOMfczxg54qq8zeXxtQpt2SjbxG2DqHeaduLob5_SgsDjgoLCCWa3ZqYpPcWSPqQCCH1GptPTPuprJhpLqPcYuir_F8azvqdWoW89UzFlXMTBWfGtZqKTlaJOM3ScWJhoZJkMMoiDQT10F2WEvkUE-Zond6iu1e09F7gVXkHGD0i617RZcy4_U1HOLOsoufEkJ5fRPkDUPzGvpBv8abLqG75IAxW0Ej7nJacmFXAHaC1BxjYl4_WI6SID23TxnFWtfSNV5K5aaUNT6mS76YatjCs-zOx9VrnvacNRUW6SI7uUHCwFeOw4W0gZesAeaU4RBqOLIqLnYwSjZ6nXqY5BBkJnlMM9SSHZklAqJumGPTzm3PSYhw-UaVNh3Tww-9VhhTdcrIS_TpRx8BIwA5i77dtaNqVYRsC9Orx_GRqu5y2xMEaCUTsooTxzcVz_ptraGnvLgxLNCkcc_UlPMuSsN6I9QSYTZfxG8VI8AftWUDU8hU5dOqX_BS_xrpnRNoIctRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهانگیر الماسی: پول غذا ندارم؛ هفته ۴ بار غذا می‌خورم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684013" target="_blank">📅 19:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFu7VFiyLnMOJ6H3gdCOoBe52MOuezutlwS9aukLfMXBFUlz2dA7uTc5wB3vsFP87k1W8o-1PXoy7jkbzDFvUIT1ZGzMYb2XK_tbnXbM8H8akK8ngyzoI64UHpIjYJEWvPvcyySD_YH__bU5OiQ02Blom9Xw71ZDJgNZDR7ucE5u53TEFDFkbTvUpoBA94NDLNGVN8NHgrL3msaP8a10GJyARDB1-R487QR2vEkR_CQJ5aE_Z4ckuQAHdzJcldRR1sbricZUabPUI68bOohxoHSUMprP9iAwY2gbEbW7_F8Nyc1EIRhleokPIt3ObwDnTGHv8r8mgph15CY7x6gTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت کودک فلسطینی در حمله صهیونیست‌ها به غزه
🔹
در ادامه کارزار سیستماتیک نسل‌کشی و کودک‌کشی ارتش رژیم صهیونیستی در نوار غزه، حملات هوایی جدید به «دیرالبلح» جان یک کودک بی‌دفاع دیگر را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/684012" target="_blank">📅 19:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فرار رو به جلوی ترامپ: دموکرات‌های افراطی نظرسنجی‌های دروغ منتشر می‌کنند تا ما را قبل از انتخابات دلسرد کنند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/684011" target="_blank">📅 19:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGvgNpG1mrxjf_QEFz1qMBZJAqWLiDTOhmDQRHpcFeLJgbajTNLdkhTCkDapEUrenwJoNiwJ_qcr4B0tGS5lV-URGbQ7x3Q5QlUHYAGht2JMoNSDEKDUVezX9j3H6We_BDAkvgpnwmYjI4sCsAsK_Jpugcg_ykExGFxIIfqvVcyiCeANB4RawFgJzpGcQgls2zoQNLxQj9VPICBJHXoUGZY5af6WnPB6O1FrrzWF1y7DFV4v4MKQS6Mbw0VGOLzFJVN22yemzQmDANOex3ucxfPMDbKVQnripMGx-wUFjJqaj1tgllKrzW4Xv2qleaPVQpxXlNpKDHg1PrNaZu4QRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاهای خسته‌ای که جای چرخ موتور را می‌گیرند/ «پیک پیاده»؛ فرزند جدید فقر و فشار اقتصادی
🔹
در پیاده روهای کلانشهرها افرادی را می بینیم که کیسه هایی به دست دارند و می آیند و می روند. برخی از این افراد، خرید کرده اند اما بعضی دیگر پیک هستند. شاید تعجب کنید اما چند سالی است که «پیک های غیرموتوری» در بازار رواج یافته اند؛ افرادی که موتور و ماشین ندارند و بسته ها را با پای پیاده یا از طریق مترو و اتوبوس جابه جا می کنند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239896</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/684010" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
۱۳ درصد تورم ایران به خاطر مسکن است!
🔹
یک عدد در اقتصاد ایران به‌سادگی قابل چشم‌پوشی نیست، حدود ۱۳ درصد از تورم کل، مستقیماً به بخش مسکن مربوط می‌شود.
🔹
این سهم طی سه سال اخیر تقریباً ثابت مانده، چون قیمت مسکن به‌عنوان دارایی سریع‌تر از اجاره رشد کرده و همین موضوع باعث شده این بخش در برابر کاهش تورم مقاومت کند.
🔹
مسکن همچنان یکی از سرسخت‌ترین موانع کاهش تورم باقی می‌ماند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/684009" target="_blank">📅 19:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684007">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcuQVYl0RMcyOqTjFiQdUWEV0Gb1khDqPYLp6ZUwQbO7dZ5BzfbOCzhPak_3_inNI7JMl28GGS9-eZzbLX_Hv8pHsamgyLIKwnO1nmJ_o_jmh6rpl_1P_rlCwCUkjOuW25GldXUrA-LqaBw_SieWSXmolr6INCE1k6H5H2Wz1abe850Sr0XWAZ-KJ626mHgNzkCfjWcnbjYkxmBqzCcRtgpiTCXsMibUkzRmAEbVf1Xl1frWFwlSRSa0DeY3UwwwIdTQg4aPDuW0jFnGYnUNqqNyR4GQbFQPZcmMyy3_rmVRfqW4UUu8Ut1V59Lfj2sTgjsP_cuaeWHXLB-ul9aguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jbhiu3gmXNxU_LMRz8DrvVH3mw_Vrca3vu1Gi6BqCzA5pD8ZKNBX7ZowS9K6CKt0DYl_iWTYzgKQnJALXHGQyxh-BxEjtkrDnSnzrxG-tu_OLElEnHEPaxoZeW8QJENIs1v0cQWiNOresCk-Yxl4z7U_CXBnr-X5scC6qHV_pSKlm9l0DhinMOPTMaMTT9BWxg6633H1wAL58jMSeqapxht1Owo5ms5Pbq5DSGe8wf5xpn-NKzvOQfOTdIaxNhszJxDNfoyas50wFbLL5e4w_2xNCPUbfeD756KaGRVDhCJ8xQUH2zP_0MOGWgWiZuQGHlKK_Gc59eEUBPOKbUSpdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ورود فرمانده ارتش پاکستان به تهران
🔹
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/684007" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684006">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aScJzd2zBrnalLnyjxrqpZN2ljz0VMlIVcU9kqNOCk31UXbaL8MxhUYEQDbvHRORzU4DM_Zy05rOnr-EhB1wiVQ4zGdAeCxKtLvDaOpgLTSkDGRN3h2elTV__2jMZmkUK8OA5i0qkVE8q24UFF9xCxOG_LNI8YnkzZ9vQEYwf1EN1HZs1T_yCHeYuppU4HVpeqzaIU4sGVrRKSZJZZnY7sDuXmVLLXFhws7ROrq0dn6yFKOmwfd72hqQ9e_NFXRDAX15Atrrp3zL_keDPeywS_XHcwX4ygG-ymcxBLkDNKySzwzhAek5JS2gPgBrp3vt_TqGXJ1G0yE_Nh3EtefDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو دو بازار
🔹
بازار امروز در ادامه روند رو به رشد خود قیمت‌های جدیدی را ثبت کرد. دلار در بازار آزاد به ۲۰۲ هزار تومان رسید، طلای ۱۸ عیار از مرز ۲۲ میلیون تومان عبور کرد و سکه امامی هم فراتر از ۲۲۰ میلیون تومان رفت. با این حال همتی رئیس کل بانک مرکزی در واکنش به این گرانی‌ها گفت که بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست و در روزهای آینده قیمت پایین خواهد آمد.
🔹
هشتصدوچهل‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/684006" target="_blank">📅 19:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684005">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGLNvUTrJBl6HC80-YAUMqtFIQ8qXpbjgqrMaGrjVydi9RxOusubm-NiAY9rftfWXaubi7tXO_gCDn-o6LQlgCB8glKVSE9d4PfnmHlJUsN36lHs6THNwQ-54kp94t_jzI4ZXE0_8uXzJ85m6ZsEiw0vf4snymDCI19s7zWqq2szwEVgYM7LwUJCjvzABMQvyvvRBWa2fTEt2T9N2soa2WJYBLnAaLJW1OtsTALRsBb2X24lFtE3J_hLkNcIQVzfEW4gbeyjDGJ_BjzCJHVA2cmKmsoeyVi_48KG_XzF9rGR_fFIxJyJsbcK4Mm1Nhgdgv8w8FXVulKXyym1ohQslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: بگذارید ایران تنگه هرمز را کنترل کند
نیویورک تایمز:
🔹
جنگ با ایران دو چیز را آشکار کرده است، ایران نمی‌تواند تنگه هرمز را به طور کامل ببندد و آمریکا نمی‌تواند آن را به طور کامل باز کند.
🔹
ترامپ باید با واقعیت روبرو شود تنگه باید بازگشایی شود، حتی اگر این به معنای دریافت عوارض از سوی ایران برای عبور و مرور از آن باشد.
🔹
این نتیجه برای آمریکا یک شکست خواهد بود. اما در حال حاضر، این گزینه کم ضررترین گزینه است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/684005" target="_blank">📅 19:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b94af2eb.mp4?token=r1fdJxx8ES4ailODJgVIcNcpl6n7mJr2R7_WXcyk1nvQIpyKZjPAkw20HdhV_dEIR5Xri1vpHi1u5wZWuYnVD_YBcrfFJ7kO33ntgdFwVyA2B8bXPP05s7ByU4heE5VXVuH8QTQy_ai--tyK_Orr5GIGC595-D_Y0TUxk5jQOabBnQAoul6ejyKF19dx1G7nLdU0IUapKU6fqWGpxv7Vq-q3z0SyBZx0CM_sgSayp1DMJatOwNudx69QlfYRsczpx3k1IOvCq9_Tb0vgStbSLJN2a0xy9TZwF4HcnWSJXtlzVpzjycnNBrIivCjrBcnqFnzSvyF6foSen7ymV9V_fEnlejkLet5B_v8ZyASyaIbGHI1BQp5PGD_YaUdU4C6pBNxc2HuUC2QKSvTCTbghYh4B2yrVB-54kOkxjtGOHMyTLwuT325OFWgvBA2TEnlwCE5arC9LwdrB1rM7GrN79iBLWosSrPUPOmE7I_SsXWlgHYeJ2OBFFgqlWVais7RcNVjTrw28iDGY5plcylsYJe9DLLV-r7TaQW3I_Uq1r0EJyDUOkWCoLA1ZDIqMUHCF37K6FLKy0Ae5aKGcqUlyogDKwzIv34gl3yMcgAlhXdBoHU9EmVA-flQ4jHBUF1_H56EfrLBwOhkIq4PgBKxSWQYzHAqHG0XILWz4sL7wIVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b94af2eb.mp4?token=r1fdJxx8ES4ailODJgVIcNcpl6n7mJr2R7_WXcyk1nvQIpyKZjPAkw20HdhV_dEIR5Xri1vpHi1u5wZWuYnVD_YBcrfFJ7kO33ntgdFwVyA2B8bXPP05s7ByU4heE5VXVuH8QTQy_ai--tyK_Orr5GIGC595-D_Y0TUxk5jQOabBnQAoul6ejyKF19dx1G7nLdU0IUapKU6fqWGpxv7Vq-q3z0SyBZx0CM_sgSayp1DMJatOwNudx69QlfYRsczpx3k1IOvCq9_Tb0vgStbSLJN2a0xy9TZwF4HcnWSJXtlzVpzjycnNBrIivCjrBcnqFnzSvyF6foSen7ymV9V_fEnlejkLet5B_v8ZyASyaIbGHI1BQp5PGD_YaUdU4C6pBNxc2HuUC2QKSvTCTbghYh4B2yrVB-54kOkxjtGOHMyTLwuT325OFWgvBA2TEnlwCE5arC9LwdrB1rM7GrN79iBLWosSrPUPOmE7I_SsXWlgHYeJ2OBFFgqlWVais7RcNVjTrw28iDGY5plcylsYJe9DLLV-r7TaQW3I_Uq1r0EJyDUOkWCoLA1ZDIqMUHCF37K6FLKy0Ae5aKGcqUlyogDKwzIv34gl3yMcgAlhXdBoHU9EmVA-flQ4jHBUF1_H56EfrLBwOhkIq4PgBKxSWQYzHAqHG0XILWz4sL7wIVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متشکریم به وقت ایران!
🇮🇷
🔹
تشکر متفاوت لگویی‌ها از عوامل «به وقت ایران»</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/684003" target="_blank">📅 19:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFqlHKLUtKjb87ZiPgAsUkrzmZRLZ5tXSDzydoY7k6Ge0hX3VTNjZfcTa2IQjtHeQuG2Ind94wzbcR42DJTpBq-gk2enDAJ2KC_VBJisGL9Gk0n4V_3qVi451WbfCIBFvb_InfdkvE_ja2H_RfTO30b6VqwyKze8uw5yiFSHc_IvCK_ttui4BEeFJmzyzxjtONM8NN8L9dX8pbEdhFhuwFO6FRH4dUWrjizYw_SQsiya7v87Gic6QQkyMhVZQ5eYg0UTq06v_6NP7Jp3O6vRkSQiUsxq3zFgINdAoUFQoxLCjfMOo-ikb7CCkjfOxKkHacMep6GY9RwxYxjNvskseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطع برق در کمیسیون انرژی مجلس
🔹
کمیسیون انرژی مجلس تشکیل جلسه داده بودند تا علل قطع برق را بررسی کنند، که برق در همان زمان قطع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/684002" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684001">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367508c21f.mp4?token=S8Bau3DkRBZxWO6QczQgmMsQtkghBPPl7KrjK7f_zstYQl3R_CIdu0nf8yMo6MLKsUJlNxfMYebOZc10drOSHCNsbvyIDvXZLYozDpuTKHG6meaCdgqcUipiMOQT5b0qplbQQIBG6oOT3WVYFuh5j38slJ0x5u8AxyoT4oBngfTCLyNQYkr-kqweiQJAFrtT89xp6t_CRi3Mm0YYXuBOE2sTVJGlvTHWZ0RWEpy7FG8EoZxELZfdA6Kx3dpGRW19oLk73CyUKRWsijl1uQ8DKtg1Yc_fJ_Gm2D0uyptDROcDr94aItIe-lji6mygi8Z9aBdhckBbH7GP0oPhb7SzyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367508c21f.mp4?token=S8Bau3DkRBZxWO6QczQgmMsQtkghBPPl7KrjK7f_zstYQl3R_CIdu0nf8yMo6MLKsUJlNxfMYebOZc10drOSHCNsbvyIDvXZLYozDpuTKHG6meaCdgqcUipiMOQT5b0qplbQQIBG6oOT3WVYFuh5j38slJ0x5u8AxyoT4oBngfTCLyNQYkr-kqweiQJAFrtT89xp6t_CRi3Mm0YYXuBOE2sTVJGlvTHWZ0RWEpy7FG8EoZxELZfdA6Kx3dpGRW19oLk73CyUKRWsijl1uQ8DKtg1Yc_fJ_Gm2D0uyptDROcDr94aItIe-lji6mygi8Z9aBdhckBbH7GP0oPhb7SzyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام گلپایگانی: همسرم به معنای واقعی ام ابیهای پدر بود
همسر شهیده «بشری خامنه‌ای»:
🔹
بنده با همسر شهیدم ۲۶ سال زندگی کردم. به دلیل برخی مسایل ۱۱ سال آن را در جوار رهبر شهید انقلاب زندگی کردیم.
🔹
سیده بشری خامنه‌ای به دلیل رهبر شهید از بسیاری از وابستگی‌های خود عبور کرد.
🔹
او در کنار کارهای خانواده، کارهای رهبر شهید را پیگیری می‌کرد و مقید بود آقا هرگز تنها نباشند. به معنی واقعی ام ابیهای پدر بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/684001" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
