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
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 18:02:38</div>
<hr>

<div class="tg-post" id="msg-683988">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
♦️
حملۀ موشکی یمن به تجمع نیروهای سعودی  نیروهای مسلح یمن:
🔹
در حمله به تجمع نیروهای سعودی و یک کاروان حامل تجهیزات نظامی، بیش از ۱۰ کامیون حامل سلاح که از خاک عربستان وارد یمن شده بود، هدف قرار گرفته و منهدم شده است.
🔹
همچنین چند تجمع نیروهای سعودی در منطقه…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/683988" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683987">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مخبر، دستیار رهبر انقلاب: مسئولان نظام برای احقاق منافع کشور هیچ اختلافی ندارند
.
🔹
رئیس شورای عالی قضایی عراق فردا به تهران سفر می‌کند.
🔹
رئیس‌جمهور چین خواستار تشکیل کشور مستقل فلسطین شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/683987" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683986">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
💰
📣
✨
نسیم سرمایه
۳۰۰ میلیون تومان وام قرض‌الحسنه
با کارمزد ۴ درصد
‼️
📅
حداقل مدت میانگین حساب یک ماه و بازپرداخت ۳ تا ۶۰ ماه
🤩
🧮
لینک محاسبه مبلغ وام و اقساط
📱
لینک افتتاح حساب از طریق اپلیکیشن سرمایه
🔷
اطلاعات بیشتر
‼️
وفق ضوابط چنانچه حائز شرایط ­باشید
تا یک میلیارد ریال بدون ضامن،
تسهیلات دریافت نمایید.
#تسهیلات
#تسهیلات_بانکی
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/683986" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد   سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/683985" target="_blank">📅 17:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683984">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
عراق به ایران و عربستان پیشنهاد تشکیل یک شورای امنیتی مشترک را داد
عراقی‌نیوز:
🔹
عراق رسماً پیشنهاد تشکیل یک شورای هماهنگی امنیتی مشترک با ایران و عربستان برای رسیدگی به آنچه بحران شدید اعتماد بین دو قدرت منطقه‌ای می‌نامد، ارائه کرد.
🔹
قاسم الاعرجی، مشاور امور امنیتی نخست‌وزیر عراق، این ابتکار دیپلماتیک را از طرف دولت علی الزیدی، نخست‌وزیر برای آشتی دادن تنش‌های جدی بین ریاض و تهران طرح‌ریزی کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/683984" target="_blank">📅 17:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683983">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24152d0a7.mp4?token=P7oRsmZGdQiEAU9Iaj975wwR6kzu406VsLcUMai67zvOYnMxFpe0JIovKhMrjPywzPmIhP-Oox_KKUicSfwkJ3-oB6evi6QCgqdqkszSILcnLv-hxM7u8q2WdKbi4BuNDu1sq6HTTU0X4ZiMgNB-x2Vn2PTX-Ku868EnbgnUu6Ip_iBXZzKTziqmyqhKhKKG43I4QdkiCOaoaLtQbWZSUcdr_PbQfuxpATTbBdkb_MlVG7fp_bsUrjJezN9z63qXNf087XglKTx1BiU4YNJk9DHFpkUTdNv3e4wrv1xovHE-T6VJc89CCURfkZyn4RrHLmM8kllRDS3y-2CSwy0WcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24152d0a7.mp4?token=P7oRsmZGdQiEAU9Iaj975wwR6kzu406VsLcUMai67zvOYnMxFpe0JIovKhMrjPywzPmIhP-Oox_KKUicSfwkJ3-oB6evi6QCgqdqkszSILcnLv-hxM7u8q2WdKbi4BuNDu1sq6HTTU0X4ZiMgNB-x2Vn2PTX-Ku868EnbgnUu6Ip_iBXZzKTziqmyqhKhKKG43I4QdkiCOaoaLtQbWZSUcdr_PbQfuxpATTbBdkb_MlVG7fp_bsUrjJezN9z63qXNf087XglKTx1BiU4YNJk9DHFpkUTdNv3e4wrv1xovHE-T6VJc89CCURfkZyn4RrHLmM8kllRDS3y-2CSwy0WcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقابل جنگنده‌های J-16 چین و رافال‌های مصر در رزمایش ۲۰۲۶
🔹
جنگنده‌های چینی J-16 برای نخستین‌بار در رزمایش «عقاب‌های تمدن ۲۰۲۶» در مصر، در تمرین‌های شبیه‌سازی‌شده با جنگنده‌های رافال مصری روبه‌رو شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/683983" target="_blank">📅 17:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683982">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KapISF7rPQtYAfhrS-2oYXr1H6ks5zlQMoagY76icheEgTJ1POqpLJajKPfNJK05d0QJfD2tFZK6JJePkpUVZIC6d9n3jwFZMUbYgPW6p2Q0pLk2yJuVFUfUKSBB8_psXp6EWpkDRPibWPRgTFzrRRkONovgsTi34R9vNWCcinQZ7YoCS1WJtgrEuU5DElWzRpEoow_j-D_KyWvexBSTbql0bDRcegFm7hWcIKHh4CEIAA4LcA9npiSBBJ4aAHW8rrz5Fy8M5BnF2qxV8lBRYkcYyT7150rqD2miK7_1SyCFZBaCIlO80EMruMO07q3-MWNjOrb_4G0GPqovPztTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/683982" target="_blank">📅 17:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683981">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFSOctC-5_-vhZrjctbrkwLgOsBaDxUiw7I_ripHGBkFwJUrb-dIHcpIDndAwwyofRIG6tzKJHIMaP2vHmg8fCpGmUOlWRhQ86Wd9lUXVahtYTDU273KtfTfxOZm0WmgWv3B_l3LifXqEg5RDSHVERftdnMDwKT3qpsO9v5APMYWusAG9MpnS2Lj3g8LH7C9gJtep1q0hN8xjDHG9KFWRB9UYw4tBnb-tUceELlXU2SbcoKRwECF1i25wruu4wC_d9GiWJmx--Dde38hAGfKlFC2d-iT_SWFwr4p3NKU1n1sPOy_Ycii_67eJuPNALA9UlavPfecMz7YKsE53dFG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی جدید فولاد خوزستان؛ بازگشت به تولید تنها در ۳۵ روز پس از حمله دشمن
🔹
امین ابراهیمی، مدیرعامل گروه بزرگ فولاد خوزستان، روز دوشنبه در جریان بازدید وزیر صنعت، معدن و تجارت از این شرکت با اشاره به روند بازسازی خطوط تولید پس از حمله به این مجموعه گفت:…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/683981" target="_blank">📅 17:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683979">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد
سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع آتش‌سوزی گسترده در این شناور شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/683979" target="_blank">📅 17:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683978">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3d5fbbed.mp4?token=etQ5FwsBUq0YZ0WZRMIDL7wLTJSdV_-14QypEJbPtmM0-rxAirGNQ-QO3RwVTFwzaccO8LA78-fiqmtkfxjJqyogF1hCGklmuc1q5VFB3LveUtrccvYqhAwk7v6XCaELlLMUOYG8_L1Feye28fufS1gN2OF7fbJRxPy1ZcrTDKX-u36O49g1OY70_pQ0HVcONzhCg2Z5DjO1VUbM-3znI01aDJ5h5jIPXPbnn6_w15S8TYj_NnjRF16O1JCh9U3G_aYIX-brRTaMNZLZ2pFQk9rjtBnaf2Yec-xI8L1gf6LxCtnjewbkimG9pMk2ynq8kx5Bymq-QbPioI2BXKgn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3d5fbbed.mp4?token=etQ5FwsBUq0YZ0WZRMIDL7wLTJSdV_-14QypEJbPtmM0-rxAirGNQ-QO3RwVTFwzaccO8LA78-fiqmtkfxjJqyogF1hCGklmuc1q5VFB3LveUtrccvYqhAwk7v6XCaELlLMUOYG8_L1Feye28fufS1gN2OF7fbJRxPy1ZcrTDKX-u36O49g1OY70_pQ0HVcONzhCg2Z5DjO1VUbM-3znI01aDJ5h5jIPXPbnn6_w15S8TYj_NnjRF16O1JCh9U3G_aYIX-brRTaMNZLZ2pFQk9rjtBnaf2Yec-xI8L1gf6LxCtnjewbkimG9pMk2ynq8kx5Bymq-QbPioI2BXKgn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اخبار تائید نشده از حمله سنگین یمن به مواضع حساس و انبارهای سلاح مزدوران سعودی
🔹
بنابر گزارش منابع خبری، نیروهای مسلح یمن با اجرای حملاتی دقیق، مواضع حساس، انبارهای مهمات و تجمعات نظامی مزدواران سعودی را درهم کوبیدند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/683978" target="_blank">📅 17:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683976">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBECFX10twttYNhdHiUXwQwxEms3_YdjTnBR0Il4vtqp2ecRMXZxxvR-FgXI1c_Z7F962jTM2dhuLTYjJkc4c-obRnVvaM8fO6VEG14n0pbz96_KC_SVFdg77JNjVg0-ExrjjVUAsreIqdwcHFAjjhMJNphop7GLefCN5jDguGVGUUc6xwm3y3vhEBaorwHWJzDuFRVn5JXeWdem7gaFyqkvHa-kNmX-cx7rhocOE9jKLSL-wgujF-7m_iXdVdoSu-AX16GDmxhysODzLMfU87_GRA0aiL4hXhWcdui0BZqBuCLe5oVoIYyyUyuhjDXBpP4JMsjDYPZSezmFCj1Mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXg7VL20pdbS7VARPyWW7yhRkjopbW6RsY9r3WxJ9qFp2BMsMLXUTlHIZooLYsKTApuyG68Rm72PgkzsyECpx6ppVj_Nsv8NYq7COYghM66EB1sqDYXaLKBRrNCqErjgbaZkS1-5gLwY582Kq1O2sxDnq8DS_Fg7rSrpkM2qH5bCD6D7BZoiIt2XuRwdLXDhQnYTUu74LYgzqqgHWAHNiGhtsFwLibD2fmYJPKeBi9ES-3XL96W2GofyNHWhQWLcBveA6JeHNFeK--EV5wzGgSOIY_dsr0N0AU9Aoy4pFW9jnwNoQxlkknCVyAIXT-zta8HjClbBm1zlX2Y4NfXGUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری که گفته می‌شود مربوط به سلف امروز یکی از دانشگاه‌های علوم پزشکی کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683976" target="_blank">📅 17:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683975">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvWYBjz39FTcxywlFkUP1yoAL4VM8GsYzD5pIWIU3eF10wQGRGKzaG3ZtrvH9E1-6baS2-gja1lTk4Y5VSpNDLYBrTMh98-GQ85TRx9ZVQYiZ6YWDo0nqSXICezRd01agoKslKxLs7GBuM05CE7nOkzTAP4TQPO9wiHOJSvGgnuTr7I5A_HIy8UxKczgUbLypH02z7FiPE-n-0ZuQDvA0zc_LC5zR1Jve0B8phYsG7TvEucnqrmx09E7VGHJLY1z58I0E-cNNN_MYABt_MpD3KiKyKHX3kUJHvrcIW8SWujapdv5aPHHPtJhZIEvistyryIeVunaKjmjWpPH4mmOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۶
🔹
کاهش۷درصدی ریسک اعتباری بانک کشاورزی در سه سال اخیر
🔻
بانک کشاورزی در ادامه روند رو به رشد شاخص‌های عملکردی خود در سه سال اخیر، موفق شده است همزمان با افزایش حجم تأمین مالی بخش کشاورزی، ریسک اعتباری را نیز به شکل محسوسی کاهش دهد؛ دستاوردی که از افزایش اثربخشی سیاست‌های اعتباری این بانک و ریل گذاری موفق در مسیر حمایت از امنیت غذایی کشور حکایت دارد.
🔻
شاخص ریسک اعتباری این بانک طی سه سال اخیر وارد مسیر کاهشی شده و از ۱۴.۹ درصد درتیرماه ۱۴۰۲ به ۸.۷ درصد در تیرماه ۱۴۰۳، ۸.۲ درصد در تیرماه ۱۴۰۴ و ۷.۹ درصد در چهار ماهه نخست سال ۱۴۰۵ کاهش یافته است؛ دستاوردی که با وجود شرایط بحرانی جنگ و چالش های پسا جنگ در سال های اخیر، بیانگر ارتقای کیفیت نظام اعتبارسنجی و بهبود مدیریت اعتبارات و مطالبات است و روزهای روشن تری برای پشتیبانی پایدار از تولید و امنیت غذایی کشور را نوید می دهد.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683975" target="_blank">📅 17:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683974">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بیانیه نیروهای مسلح یمن دقایقی دیگر منتشر می‌شود
🔹
بیانیه نیروهای مسلح یمن، ساعت ۴:۵۰ بعد از ظهر به وقت یمن، منتشر خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/683974" target="_blank">📅 16:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683972">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: کشورهایی که سرنوشت خود را به تهران گره می‌زنند، با مسدود شدن تمامی مسیرهای دستیابی به رفاه پایدار روبرو خواهند شد ‎ ‏
🔹
هر کشوری که به عنوان شریان مالی برای نظامی در آستانه فروپاشی عمل کند، باید انتظار داشته باشد که در انزوای آن نظام…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/683972" target="_blank">📅 16:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683971">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVeUocX9C1k1aiv_XQhMyWKH9jEarP3PWxmERpyhqrn5SHB6vbw1QA_fbR6_CR0FNxZunw1Vqtl8O3TSIrZgLAtvyXSPjpz-yVYr4kb7e3EUaa44gvO1_fq7WFek2Progz6UxuMFjjatc6qHQfT-wV0CqDGA7xUXuESErt3Hd1YDg-t7_6gctu0n5TEEZIZN_Z0rJSzzbglsYJLcR1RWoM11i-o0dHnYVUNo7rSVkz1v3MCvhvtYcLnW-fJHStyIHZ8mVCWBwZGioWMpEUm5wl0fEVPm6_7Tdi_5_S6ZmCXVJ0nTijYgYs2nPPLx8pjr3Tgs_a0COXvuXbD2YKTJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آموزش آنلاین ۸۰ برابر شد
🔹
در رویداد «تخته سیاه» درباره آینده آموزش آنلاین، یک آمار قابل‌ توجه مطرح شد: استفاده مدارس از اسکای‌روم در بهار ۱۴۰۵ نسبت به دوره قبل ۸۰ برابر افزایش داشته است. آماری که نشان می‌دهد آموزش آنلاین دیگر صرفاً یک راه‌حل موقت برای تعطیلی مدارس نیست و به بخشی جدی از آینده آموزش تبدیل شده است.
🔹
اما بخش جنجالی ماجرا جایی بود که کارشناسان درباره کیفیت این آموزش هشدار دادند. فاطمه مقدس، مشاور وزیر رفاه، اعلام کرد باید درباره تکمیل آموزش آنلاین و حضوری هم حساسیت به خرج داد.
🔹
از سوی دیگر، کمبود ۱۲۰ هزار معلم، ۳۰ هزار مشاور و بیش از ۱۰۲ هزار کلاس درس نشان می‌دهد آموزش آنلاین می‌تواند در کنار مدرسه، بخشی از پاسخ به بحران‌های ساختاری آموزش کشور باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/683971" target="_blank">📅 16:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683970">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp0jzG7hugztrBPv4fWI2IBtteEgNXbMK8m37XW9Z3CMfv2nf9_yXt_PYulwMcm-FvR_-I3uDM7MdnIeD617aH6J0G0FAYGY55gAIc10isGoKAk2f5W5VwmnltWsq68G0_APlJfKxgSsZq1FkarDRI1KQ0gEVJ6Jvh0ry9xDIlvJvqOD6Nkal9eKjNFdTXtMrH1YaC_wYNZwzJHi0L9MO1Bb_6ql-qoriSGzx9XWpO_meMkpiTSGl6ljr-AC3GEI_coDWeTIbzJVCW3w7rxEJ-4cwvIB5fiqBrtyfjxoBLyl6WveU9eHfIa8BwiQ9lM4294tnXrRr-ZZqMwuWTR6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لفاظی‌های جدید رئیس‌جمهور مستاصل آمریکا علیه ایران
🔹
دونالد ترامپی که با وجود روزها درگیری و عملیات نظامی علیه ایران، حتی نتوانست آبراه حیاتی تنگهٔ هرمز را باز کند و همچنان هیچ دستاوردی از جنگ ایران به دست نیاورده است، بار دیگر در یاوه‌گویی تازه‌اش مدعی شده که «ایران به‌طور کامل در حال فروپاشی است.»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/683970" target="_blank">📅 16:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683969">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7VxZhQN9Ej9qLZ0plf0FlXiM6YZ3qnJHnPfpl-621RlTSc8aLWEok0-GWwJc2DFCM6cQ32Qe5ebu3eVdTrnTwJEiUYo9NrhSKt9w1AsqMaIlpF0nlio9O0KpOkWf7tFobtjGBL1KYpV__HmfZfeqjY3GuR6Ib9VcbSuTLka4Kdcr2BXMBdFLrpsn7GrOUXWG6hRiuCDakSuQZg945TsgKjXy74d85nm2xTh1QKoo7n9dIW_ifuo3ioGlKjO6sE2tS-XHPHajQameeaRzpwq5J28wNNy2Cp08HGB7bnszUL50C27pl2bzAIs0mauWcE7T948ZryguFh25MTXU7WxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاجیکستان تصویر ابن‌سینا را روی اسکناس۲۰ سامانی چاپ می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/683969" target="_blank">📅 16:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683968">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8vny2C4aUXYx45Bk9uMsX1UKQPcVLaE1tsD2kY-2PYYeZRpbfqOiZw8o39JsY79dOM0mEG-nLBwGx8Vbtpjn4MuGadejvp8U2ND6B0d7bch-PzK_DffhIpDBHVEz03eJQWKlKcZc75yAhz2G_Oayi8xMNkNjGxV9Qa-kEig66eCoocCIUUX4A6tjcKHr88aoq6cEAePH4EwuQAz1RdugrwCVLhDFcXDzdFD5T8otreDcmyvLFzFfrbCSQB5v1dSQsb2cfbLzE3y31PUYptPQkiiag-_3y_jMVxRz-5xGjhc9DnaRhVuxx8xuPA_ApJbn6MCe3Xiry6ZLsRiIz86IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایش توان فناورانه کردستان در حضور معاون رئیس‌جمهور
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کردستان و همزمان با هفته دولت، از دستاوردها و توانمندی‌های شرکت‌های دانش‌بنیان، فناور و خلاق استان بازدید کرد.
🔸
در این نمایشگاه، محصولات و دستاوردهایی در حوزه‌های
کشاورزی، تجهیزات آزمایشگاهی، سلامت، خودرو و ماشین‌سازی، فناوری اطلاعات، نفت، نیرو، صنعت و معدن
عرضه شد.
🔹
از جمله محصولات ارائه‌شده می‌توان به
پودر ثعلب، فیکسچر دندانی، دستگاه کشت خون اتوماتیک، سامانه هوشمندسازی گلخانه، کربن فعال، بذر هیبرید توت‌فرنگی، تجهیزات هیدرولیک و آفت‌کش زیستی
اشاره کرد.
🔸
همچنین چند شرکت فناور استان، نیازهای فناورانه خود را در این نمایشگاه مطرح کردند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/683968" target="_blank">📅 16:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683967">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e197e215a3.mp4?token=aFuj0UVTaKxSV8OyJ7ligNncmvQNqmpXw-M96l1eEDeLcNOvarx3vWt2-xtbDPAWlrXiPJmYZMm-L6QGC4U0pl4HBsA70dMRsgf24vk4YZJu1A7B7VlwNLHpCrbbbVcZSez95-U8UPoa0caqDRXyXxfBqhPOtaV4jY6N7r0TIyYLldpWHdg-1jrbr-64XqqjlnIFKojyx76v9twfPQAqty86zw3DqgIlsCH1WWBsY9O1BPD-C9uoXMGYA_YBCniwZBWjxLmOsxCaRp6cfsYX7KDtS3NyPdPXlu-4mVUVMZ8ijLyblKAl9UbD6QMlPdcs6IFNyghd_hSm8iw2i-eAWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e197e215a3.mp4?token=aFuj0UVTaKxSV8OyJ7ligNncmvQNqmpXw-M96l1eEDeLcNOvarx3vWt2-xtbDPAWlrXiPJmYZMm-L6QGC4U0pl4HBsA70dMRsgf24vk4YZJu1A7B7VlwNLHpCrbbbVcZSez95-U8UPoa0caqDRXyXxfBqhPOtaV4jY6N7r0TIyYLldpWHdg-1jrbr-64XqqjlnIFKojyx76v9twfPQAqty86zw3DqgIlsCH1WWBsY9O1BPD-C9uoXMGYA_YBCniwZBWjxLmOsxCaRp6cfsYX7KDtS3NyPdPXlu-4mVUVMZ8ijLyblKAl9UbD6QMlPdcs6IFNyghd_hSm8iw2i-eAWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفت‌وگوی جالب کریس رونالدو و اینفانتینو در حاشیه مسابقات جهانی بازی‌های الکترونیک
🔹
اینفانتینو: «۲۳ گل دیگر تا رسیدن به ۱۰۰۰ گل مانده؟»
🔹
رونالدو: «آره.»
🔹
اینفانتینو: «۲۳ عدد مورد علاقه من است، چون روز تولدم است. موفق باشی.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/683967" target="_blank">📅 16:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683966">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtgkhvvvIGKd7i5xvMOwKdrvt6bFl7MV1Cm8o9gcWEpYnBFNg30VYfm_EnTFprS4jLs0nHvjk2aEOm113pzIna_Hbxk_8wdrGsydCEpXLvWK3PKbKQZXlpwxyhaNO6COplLWhvdn4fERXcYZwp7NG5EKPu1m8b1PxR44159dgmtooRyswU8WM5taCWMnAM42CY3keaZqQNfwnAPiK23Z_anRAcfFktO8wUdg84UKdIw8jbax4IWKoP2D5r9MzGPFXH3yF7Sg-4UY6MM7VeQ0Gh_Mh27mnWL-rL3Vlh31RV1S-gNFmuta7usOsHKZq34-QKiwmfLymqv-A9UWTcrOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی جدید فولاد خوزستان؛ بازگشت به تولید تنها در ۳۵ روز پس از حمله دشمن
🔹
امین ابراهیمی، مدیرعامل گروه بزرگ فولاد خوزستان، روز دوشنبه در جریان بازدید وزیر صنعت، معدن و تجارت از این شرکت با اشاره به روند بازسازی خطوط تولید پس از حمله به این مجموعه گفت: فولاد خوزستان با وجود روزهای دشوار، با تکیه بر توان و تلاش کارکنان خود توانست در مدت کوتاهی بخش قابل توجهی از ظرفیت تولید را احیا کند.
🔹
وی با اشاره به حمله فروردین‌ماه امسال به کوره‌های فولادسازی اظهار کرد: هدف این حمله ایجاد اختلال در روند تولید بود که در پی آن، ۱۱ میلیون تن از ظرفیت تولید تحت تأثیر قرار گرفت. با این حال، فولاد خوزستان تنها ۳۵ روز پس از حادثه توانست به ۶۶ درصد ظرفیت تولید خود بازگردد؛ رکوردی که حاصل تلاش شبانه‌روزی کارکنان و سرعت در عملیات بازسازی بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/683966" target="_blank">📅 16:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683965">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuWpajRnxnwaM33xZ2-uQogwnS79iubIjWmonVZBWm-cqRGfvGHoKlhPpQxYDKy_tGm7PzaDcMsQ5WDPGKxfmU5nNumpmb2_WwhdG2QO79wX5pDd1vfndDKBObQBhpoeJKVaCnBPjpX1jh2HEQA68xyLC3YVSIRhUdBDEsCYFaiEAF6l4GTRMZ5nVITHaoiIdVSrk_BuyprKMrOT4juxKdCcqwSQtzkpWhLJfKl-Jeg0rPO8oXLl3tafsI3KS1goOZqaKryUAVR7OPdLxARmhcRx8EBJcxS9kMFwR8KyAPjVtdy1AJgds_a0O2leifeL-L_XeKCiWYIIV5Wv-6YWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: ایران ۴۵ نفتکش را در تنگه هرمز در فهرست سیاه قرار داد
🔹
ایران ۴۵ نفتکش را به‌دلیل نقض مقررات عبور از تنگه هرمز در فهرست غیرمجاز قرار داده و این شناورها ممکن است با جریمه، توقیف یا ضبط محموله مواجه شوند.
🔹
کشتی‌های مرتبط با شرکت‌هایی از امارات، عربستان و کره‌جنوبی نیز در این فهرست هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/683965" target="_blank">📅 16:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683964">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDWyozfCh4Vqt51Jl-Bd2umRRryKjBdMPV7maCbvHSxZfgP9whUqIRNXyKhXIu9m2jEWsH_7H6dbujWbrnbxK11hKSbFKI-3rvbfOSidgkXxl2vBUTzAIkVojf2ECye80N534kYCvHSnhuny540wdfO7BhWfI49Zb9J_VoZi1mh1OO65hgmRTm8XcdtekkUfOZu4RhQcyPb2pf6Zt1NQ67tF1SfFrD2BsHz8ZE_sZSvg8Hhcrc9MbHjxxDzCkmvfT2dCv73MZPrCll_PtaJN2fJKdMjav-lAdQNLGc3GjcL3IEAy8b_v08N9nr7z_AmcpUt59id6LMECfhou8rzYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کویت اوضاع خوبی ندارد؛ درخواست از مردم برای نهایت صرفه‌جویی
🔹
وزارت نیروی حکومت کویت از مردم خواست که در مصرف آب و برق نهایت صرفه‌جویی را به عمل آورند
.
🔹
رژیم حاکم بر کویت در جریان جنگ تروریستی آمریکایی صهیونیستی، بیشترین همدستی و همکاری و همراهی را با متجاوزان به ایران از خود نشان داد و اکنون در حال چشیدن طعم تلخ این حمایت‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683964" target="_blank">📅 16:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683958">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEwWHauN_Bi2r9v6WMOBGCx_dNBk3FKfSfm_IUNoEs7LX5aWEJkIREpzCFfPx_KJmJr8Ji2Ls7B6JDzhS_0oSBfhJiEhZDzPCqXsm_9DewRCC2bMwUPStLh8ClQk0YhEUmHtniTxhyT6sHzzggkd5io6GTf9YMurbIv5ngIwK_JV8xPBiOGwzbCq9tjW1X1AfANG2NPkuWVuHcX1IO9m02Z7naVZtw_I7IBcw9QUwBtdHwRSs8kJQFLO9SjAWgzISat0lRqnuTaqq6nYKSpcVKG9-ID66wr0vAgs8827tuUhdIj5dNotMq6bSjK0ojZZQuZtt9n9tt99jZMIvWZoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qe2Quf2p-Xr361ENBixx-RDUixn9G1Nlb3nnmfgQBWpcihPNqo6jXiKLC2ju1T55-owIrUSJM-W4JZAjCXbwvDoPpG5BnVq-IL6xIf5rhsSTC_fOHfqo9Qy9IhGrlSAoUjPTGd6mX2ULuRL7X2Om2B9uJLCA7OPPjmh_JvZSQe__-D9kTqGhYvZ4fwLGqMRTB7ZMds957nizAQGoAk4iVYA0Sufbhzg9rt03mJt-SxZqPQBG4ooa809niqLnFAnyKekou_34LSwpumSZCToReTES9YoT329bE2PvyehUwSU-JPwRdf5T7sKMEfqWqf2I17G_B2A9EL-84AxhebLjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMkK_iROHp9_ymyHg0yrcCZfZU3XLDY4atsgmENRBD5nOI-nS4rUfg82yH1ikS238j_K6uTMhYPiK7xEie2WBv_Ffin5fx8UYsUfhMUe5o7CVGWweRzdLqndIjO7NvAAMr5DPyyS0On6ANAGSQ4Z3mwkAIjym7W2TAWnbq3_y_d2DoTG7lIYlrF12KdIvdZHEqHzz9f88lhumGc_GCtY5RmN8roACXd9_NlggdZpWPqquewWtzqE79G3wVtbGPlMdCgtt9P4SCRsmEoaifAbN2vlbXMLhxoPnOMpHCcAEZsi9ZhjMEPuo_i6E8fp_8cnBUaRh_ylrgaVTky8oxR0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3_rveQOt4ELU417tz2jPQMAB0ku4nzYx8oVJBPmNC5XxiePL91iwzDoIgzkoU39eEJrM3f5AWXQj6PtawDuxsay1UdXdyEfmWLBpw8Uns6YkB8Ljzy7F3dyxzZKX8nd62RAQMemyvHfTdEz7TiylKWJMFtpUZi6jTNFbNQe13ADMKlt7XLBfucTeDf3JpgvM-PpNv6o-ZTvJ_O2Ie_pTu6JbKcRjjGGV3LbxcVsLFLsGF0JCCXFImINNlTWAQLe210BsWwMH4xpmSXhvG07iNnl7wALiGSzvBzX2_0fG1w4yNtPRj9cOuZgOjRRHfOmco2W01jHg4eDIMkt3c3Dxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wplpz4mqarsUYFZSuYT4m9VK4Bxzmb8bWnyZr15cPH6tht4Uk14QH_yhTraIZaruBEQmWCYqtBQsAEbJeledUlQIxt3sHeIdiZLBU2Fy6gensU4vf0UcdJvN8CtEk-Nt1Y9lGRXhDmLdU4oWZvbYvvemYLlZuiFrs9cwPQOXYrD0CB5xyqEqtXYlYF_lsmw1uY-snb6x5XTpOlo5R6aLlzJdXfvpk0qUFhuXVTQwYcm00YxatV8N6WOC0RISWVxuBXy6eBhDrRxAhzd1ldjEQfQmbieU1vHyPCCnG9KMyfQ1Om6kHIh7N5V1f9AIPWu_afadK9JxcRYAkzAL3Un_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdXuLRzQ8Rrezd0liMTYnR-CvWiodxfP2CedbUshNiQMVQYKicX48o-IBtBg8L7SHzOO0jFt4Rm2O01OMpZb_Xb32lrh5hmBdq6vl4GiSNXnsfWYT8QoCg-GIzIAR6NPH7iFoQ4jiUMGdeX1kIOXHpRpjGmO2R8B7acj4TQkB7ZPaScIPsR75sXgvS2AF-hm-emfHAbZ4OPKNFv3YiRSlPKKH1cQ9M2aeOMibzy-xezpl2PkKeJvPidn5w91wllWNRvZ5LiKb4Ni9rR5bep2Ou2-OMeIVpCnDTJlfxx8mHEks_E8uGMo8TVjdu_QMDt6-hMUvL7GiNdJBkb8-hVioQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سکه که حباب داره، بخریم یا نه؟؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683958" target="_blank">📅 16:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683957">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
چین و اردن در بیانیه‌ای مشترک: باید کشتیرانی در تنگه هرمز به‌طور عادی از سر گرفته شود.
🔹
نیویورک‌تایمز: کنترل ایران بر هرمز با عوارض کم‌هزینه‌تر است.
🔹
دادستان شهریار: یک نفر از اعضای شورای‌شهر فردوسیه به‌اتهام دریافت رشوه دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683957" target="_blank">📅 15:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683956">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس صداوسیما: جای یک نفر مانند محسن رضایی خالی بود تا حریف ترامپ در جنگ نرم و عملیات روانی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683956" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683955">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
روزنامه صهیونیستی «معاریو»: ارتش رژیم صهیونیستی در طول سه سال به اندازه ۳۰ سال مهمات مصرف کرده و در سطح نیرو و ادوات نظامی فرسوده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683955" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d432a1bcd1.mp4?token=GK_iB2A5e2DIsvhBLK84lfznPc2HWZ1cjUsBp0Ab0btscDgEorXsSk2frqE6tg1zQdyAKXXe9Cut24tEmPr6YR-UiAVzmCLJwW24JsfqwjYst_X46f2JCabFdJCRhtriOAmgau_gJPVuqB3ov3PCQWicz_6-7flVKRmydD2dnrcvHx65yzFlPdbXsrx1z0g6uFQrQllyl1PK6CzybBo2a8AMzthCHm5E-k2PLBYM2Tb_zT5GONnF8d-OxpjqEMoXsu6jqpsgnKP6RgonI_6tmqxJgs48ZN0LjJi5Qy79d7L1QNQak54Duq10SJ2qc9iI5zI32Cy32ce83YFi-Z9XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d432a1bcd1.mp4?token=GK_iB2A5e2DIsvhBLK84lfznPc2HWZ1cjUsBp0Ab0btscDgEorXsSk2frqE6tg1zQdyAKXXe9Cut24tEmPr6YR-UiAVzmCLJwW24JsfqwjYst_X46f2JCabFdJCRhtriOAmgau_gJPVuqB3ov3PCQWicz_6-7flVKRmydD2dnrcvHx65yzFlPdbXsrx1z0g6uFQrQllyl1PK6CzybBo2a8AMzthCHm5E-k2PLBYM2Tb_zT5GONnF8d-OxpjqEMoXsu6jqpsgnKP6RgonI_6tmqxJgs48ZN0LjJi5Qy79d7L1QNQak54Duq10SJ2qc9iI5zI32Cy32ce83YFi-Z9XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس اوقاف اهل سنت عراق در حین سخنرانی از حال رفت
🔹
عامر الجنابی، رئیس اداره اوقاف اهل سنت، در مراسم جشن میلاد پیامبر دچار افت قند خون شد و از سکو به زمین افتاد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683953" target="_blank">📅 15:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ارتش یمن به زودی بیانیه می‌دهد
🔹
شبکه المسیره از صدور قریب‌الوقوع اطلاعیه نیروهای مسلح یمن درباره انجام چند عملیات نظامی خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683952" target="_blank">📅 15:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
یک‌دهم ناوگان آپاچی آمریکا زمین‌گیر شد
🔹
بررسی «سی‌ان‌ان» از داده‌های سوانح نظامی نشان می‌دهد بالگردهای آپاچی ارتش آمریکا امسال بیش از هر زمان دیگری سقوط کرده‌اند و عامل اصلی این روند را «مشکلی گسترده در سامانهٔ انتقال قدرت» یا همان گیربکس این بالگردها معرفی کرده است.
🔹
در کمتر از یک سال گذشته ۵ سانحهٔ بزرگ برای بالگرد آپاچی ثبت شده که آخرین مورد حادثه‌ای مرگبار در تگزاس بود که در آن ۲ نظامی آمریکایی کشته شدند و آتش‌سوزی گسترده‌ای به‌راه افتاد و ارتش آمریکا را مجبور کرد خلبانان آپاچی را به‌طور موقت از پروازهای آموزشی عادی منع کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683951" target="_blank">📅 15:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84e839840.mp4?token=qQZhBdg2NY_DcaKnN-A50q8LnpyFQqxZYbHjdqSitNfXdLqzjxwxdU9IHZB-s9hqvYHxa-CxnV_6ae7RIlVVnerDCIuz3aEBywtXKw9vdD5U-3L1g28_qhrTtFkT60yeCKsJWds7_4Zuw18L8sIItkPD1Era6GOV6qnueQf4i4DnymyaDpiRfN_0CI4YqDaOmisGCKx4Js00JHsUViyr9zlQ9BZnsQeyhwtRIEzEeFzfluei4htsiVE36tLtbaaei67-myJE30rdksVW9VswuSnyfASBNg11nBl0yhHbGC914o6adEVkZ2_TVk1p7Ru12PYgbD8QMPL-gI2LILMZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84e839840.mp4?token=qQZhBdg2NY_DcaKnN-A50q8LnpyFQqxZYbHjdqSitNfXdLqzjxwxdU9IHZB-s9hqvYHxa-CxnV_6ae7RIlVVnerDCIuz3aEBywtXKw9vdD5U-3L1g28_qhrTtFkT60yeCKsJWds7_4Zuw18L8sIItkPD1Era6GOV6qnueQf4i4DnymyaDpiRfN_0CI4YqDaOmisGCKx4Js00JHsUViyr9zlQ9BZnsQeyhwtRIEzEeFzfluei4htsiVE36tLtbaaei67-myJE30rdksVW9VswuSnyfASBNg11nBl0yhHbGC914o6adEVkZ2_TVk1p7Ru12PYgbD8QMPL-gI2LILMZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس بانک مرکزی: کشور در شرایط سختی است اما تلاش‌ها برای ثبات اقتصادی ادامه دارد
🔹
مردم باید بدانند که مسئولان سختی‌های آن‌ها را درک می‌کنند. معتقدم با مردم باید صادقانه صحبت کنیم.
🔹
فشار آمریکایی‌ها نمی‌تواند ادامه پیدا کند و با اطلاع می‌گویم آن‌ها بیشتر از ما نیاز دارند که این شرایط تمام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683949" target="_blank">📅 15:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683947">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b4be905f.mp4?token=Wh9DSKzdqKAByYOeuTXzhFhJ3z__inQL0-Ozahl-8f-h0fzVgKr2r4jmt6rhfqgW76K8H8TogvsKXvuBoFHPLqDIvuOgDQty9TZPZPetEbZ7F2eFslihz6LwtCbs7JT1aywA_IFdeD0bY-kcDsDV09iHs4lyquhIH0E744DEETRQl2LmezXAaX-OGmLFh90DnU7JK4H_WTr5NGyk9_xRnjxY8ObS5M_bImwAJMQ5-7tgpaoqPV7oLNpwweoPvqS3PQw_PQFNqGoZuJT0o_4EpKEO0kAG_Edn8Z7uyY9TLbmBmlon0xIe6LoRo9qoVH_gtAxXRzgDjrrRX5tcqGEjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b4be905f.mp4?token=Wh9DSKzdqKAByYOeuTXzhFhJ3z__inQL0-Ozahl-8f-h0fzVgKr2r4jmt6rhfqgW76K8H8TogvsKXvuBoFHPLqDIvuOgDQty9TZPZPetEbZ7F2eFslihz6LwtCbs7JT1aywA_IFdeD0bY-kcDsDV09iHs4lyquhIH0E744DEETRQl2LmezXAaX-OGmLFh90DnU7JK4H_WTr5NGyk9_xRnjxY8ObS5M_bImwAJMQ5-7tgpaoqPV7oLNpwweoPvqS3PQw_PQFNqGoZuJT0o_4EpKEO0kAG_Edn8Z7uyY9TLbmBmlon0xIe6LoRo9qoVH_gtAxXRzgDjrrRX5tcqGEjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
روایتی از همت و نوآوری در محیط خانه؛ انگیزه‌هایی ماندگار که ایده‌های ساده را به درآمدی پایدار تبدیل کردند.
🔸
اگر با تلاش و سرمایه کم کسب‌وکاری راه انداخته‌اید، داستان کوتاه خود را در یک صوت ۳۰ ثانیه‌ای بگویید و عکس کسب‌وکارتان را ارسال کنید. بهترین روایت‌ها در خبرفوری معرفی خواهند شد
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683947" target="_blank">📅 15:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683946">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeXkiLaWEHdNMYsl3VN074zM3NXGn91o3Jm2XxybNhprI81DBLaugmfEAG7cX7jIW0q6djVenD6DghUR3UAZr4C0gNoWivIAUiuwq3wxxfKwQ4s0n2c8tTkvzmA9DU77BEezjtObrrEsF8r-b9XUyjqBP6RGHvS1kSx5lYQOz9v4KWL4FstdGiHY7vxdn8oZgCGwcAamlOI6ayZZi-fAjtNINRMRkJRs7PeZT5j258iRscxrDzdahyxk5vegkHHXPEiMcALtZhpwVXvbsyLPlfZlgReDMNNFFqZuD5aoI3973Cn7TquWVYLxFSMifjBlsDFsm9SNuwsszAWsCZPtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشروعیت‌بخشی به تروریسم در پارلمان استرالیا!
🔹
مریم رجوی، سرکرده گروهک تروریستی منافقین، اخیراً به‌صورت ویدئو کنفرانسی در پارلمان استرالیا علیه ایران به اتهام‌پراکنی و سیاه‌نمایی پرداخته است؛ حال آنکه این گروهک در کارنامه سیاه خود، سوابقی چون ترور و کشتار مردم بی‌گناه ایران، همکاری نظامی و اطلاعاتی با صدام در جنگ تحمیلی و اقدامات تروریستی و خشونت‌بار علیه کشورمان را دارد.
🔹
با چنین کارنامه‌ای، سؤال روشن این است که پارلمان استرالیا چرا تریبون خود را در اختیار سرکرده یک گروهک تروریستی قرار داده و برای ادعاهای کذب او اعتبار سیاسی می‌خرد؟ چگونه گروهکی با این سابقه که همچنان در رسانه‌های خود بر فعالیت‌های مسلحانه تأکید می‌کند، در محافل غربی «دموکراسی‌خواه» معرفی می‌شود؟
🔹
این اقدام استرالیا عملاً به تطهیر و مشروعیت‌بخشی سیاسی به منافقین کمک می‌کند. انتظار می‌رود وزارت امور خارجه ضمن محکومیت این اقدام، دولت استرالیا را پاسخگو کند؛ چراکه سکوت در برابر چنین رفتارهایی، راه را برای تحریف تاریخ و تطهیر تروریسم هموار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683946" target="_blank">📅 15:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683945">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mXkxNt0Hk5qpHIOls3cfp1PaY43nu4_NsVs5EGHDfd8n0wIZYblEbC7ke3HsFTdDUiei6V_7v9KrCCKyvciSsN51A0gsu8i2WvCxuNS6TPsKhhloLchp8sv06bNVNguCzcRQz5giXisNXf7vtU0HxJhatTmj5hbU8YoZ4DePyF1ju6UNXewmfNGQSCe8NXbUaARLIh6yqx6tR0KF4rbo99sK_kj327XMX9GiGt4uC1RD6iOk8FMmt0Hz9r7E3NYyKPPCkc0adPIFIEtkvrewS5PW2MyGRZSDI3HW0O4GUPk3WB41ePa6uETRQgGiJA9_U5KbbeBH9D2bugnfM07Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فدراسیون فوتبال ازبکستان: تیم‌های ملی فوتبال ایران و ازبکستان در تاریخ ۲ مهر ۱۴۰۵ در شهر فرغانه ازبکستان یک دیدار تدارکاتی برگزار می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683945" target="_blank">📅 15:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683944">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4E6YSzsntUkhuyJGgWPXQgPFJGZZBKYymHdbYkuUkc3xu3kPru7uLaOiBZYf0Qcrsv4rGOqzwA8HJuvcRrZvJh6NPm7id5X8hhreJD5_Cm03iYRbvy3bhCO98WAiEQeeMAGon58bzbMH7SSR_MB23KxjHsqYZ1Hv30ja7XmuB7PFjGJDLT8R5H3HAiSdV77hmxA1d3YC9HsZM4J2XXuDONzWHpcHeDwipI2yz4FvWQhH0iJIF1YUH7p0R3nwgXnCnMtwB4LlVr7dwQdljNqFDm3jomuQ8mrfcFa6JEwFdNpX-xnSEH06qzjevYHhUO8cgYy00F4b7ByqzzILk_uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار صریح سردار رادان نسبت به نقشه دشمن برای آشوب/ مراقب بهانه‌های بنزین، معیشت و اقتصاد باشیم
سردار رادان، فرمانده انتظامی کل کشور:
🔹
جنگ سوم تمام نشده؛ دشمن به‌دنبال آشوب با بهانه‌های بنزین، معیشت، اقتصاد و بیکاری است. غافلگیر نشویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683944" target="_blank">📅 15:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683943">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1ACv1Fm1mM7585eWpLHI98v5yawb4i76tr2I7hNRqcRDa35FoQCp-lCTXv4WnJD-wNYZ6mmwV6WS1GckCiFfPSN3MPalPUJ5mF546qT2py-l__lQl0_DLZXkgUqG_k31tMcuqI4C3pUYanWqSApftULs39ze-RBe_v_L05gyjtVRFwztVVPCc3gjPj-qRAgzmzSzwmrNTLpTkJQXZG-cJSpgi2waP_I4lkaTN_QEzDjGTJyiaLN8YHraNEsAj0L7jcG3-DXCuRvXilF3wS_H_vNuQQiPHYGekXST0kHKHGlztx4hutWzXZETbXRtlj8MuIFX5gfI3P9PZZTmef_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌وگوی ویژۀ دبیر شورای‌عالی امنیت ملی امروز از شبکۀ سه بازپخش می‌شود
🔹
گفت‌وگوی ویژۀ سرلشکر رضایی با شبکه خبر، امروز ساعت ۱۷ از شبکۀ سه سیما بازپخش خواهد شد؛ گفت‌وگویی که به مهم‌ترین مسائل و تحولات روز پرداخته است.
🔹
در این گفتگوی ویژه، دبیر شورای‌عالی امنیت ملی به بیان دیدگاه‌ها و تحلیل‌های خود درباره موضوعات مهم روز پرداخته و به پرسش‌های مطرح‌شده پاسخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/683943" target="_blank">📅 15:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683942">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d986e8cec8.mp4?token=cHThCLA3jSjef-PDA3Vh1t4bPobCglhqh9v9EzcOqtM5CKwnQIwsHeA9v6KfXGhDJBD0Zn5S9TOGdZtLETIlE4RUg0_UtyqGhwAL6y8dvejQ0c7b8MatYQa733ZJ4GV031Avz6X395qRQ5nV_hIY6DO2y0k5QgWMEEprcjabpBokEbWxL_HM93SpR2YsxMYupsa5IKY0jadV-7f269xoMLw3B6FrRRcoLtjuLjpllhHlDJR9X5lAMX6YQmSaZySuAmcod7xzFU215h-Ivy9sprYN5FHiUL_SEGFRretb12DuBH8lgNdvNODG56L9SjcIMggTN7qKuuFqdCm_q1828w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d986e8cec8.mp4?token=cHThCLA3jSjef-PDA3Vh1t4bPobCglhqh9v9EzcOqtM5CKwnQIwsHeA9v6KfXGhDJBD0Zn5S9TOGdZtLETIlE4RUg0_UtyqGhwAL6y8dvejQ0c7b8MatYQa733ZJ4GV031Avz6X395qRQ5nV_hIY6DO2y0k5QgWMEEprcjabpBokEbWxL_HM93SpR2YsxMYupsa5IKY0jadV-7f269xoMLw3B6FrRRcoLtjuLjpllhHlDJR9X5lAMX6YQmSaZySuAmcod7xzFU215h-Ivy9sprYN5FHiUL_SEGFRretb12DuBH8lgNdvNODG56L9SjcIMggTN7qKuuFqdCm_q1828w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقاب اصفهانی: بخشی از مصرف بالای بنزین به خاطر کیفیت خودرو است  رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🔹
با اینکه کیفیت برخی تجهیزات پایین است اما تغییر رفتار، زودتر از اصلاح تجهیزات و اقدامات دیگر قابل انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683942" target="_blank">📅 15:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683941">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
چطور با تیشرت استایل شیک مردونه بزنیم؟ #استایل_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683941" target="_blank">📅 15:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683940">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUl8BhbR7IVbzAorzM1wOvs8ps-XnHbqWJBjFein0dMxO8X0F9EoRnWHeE0N3Ny73tUl4J-IhQK4Xak6F5SUmdZGPBG3wb4GBUSc4GTcs0NpzCPCBhmF-nBi1AJ5akNv_nkwlhm8aDaxN5lcaHL6674pfZcG3c1_o9vVtdVsviHPeuguIXqvjuJB9DKbbDih8Bv9uC6r5q0nOtJRc7WXh9idZi1hxoHl7xklbi7F8ts_njAUVX9jAEFuEBSxoQvUMB4T8_EmvuSgQ56Q8PSANae3fVVx9sfGlAAaQqVfW1_Jg3U9WtItVMbZ-7C7wTY1-oKoqvcEoilRFp3oaz4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افغانستان ۱۳۹ تن کالای ایرانی را با ادعای بی‌کیفیت بودن برگرداند!
ادعای کابل‌تایمز:
🔹
اداره ملی استاندارد اعلام کرد که ۱۳۹ تن مصالح ساختمانی و سایر کالاهایی که پایین‌تر از استانداردهای ملی تشخیص داده شده را به ایران برگرداند.
🔹
ادعا شده که پس از ارزیابی‌های فنی، مشخص شد که این محموله‌ها با استانداردهای کیفیت داخلی افغانستان مطابقت ندارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/683940" target="_blank">📅 14:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683939">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2mPI78yv1vzdYvPTiUDoJUS7871m0v6mlg8_-okwubHMOwORKbMsSoldodHBKNtWF_6RYHp6qnVdqPTmCUVJcsl0xf5ZzpMuVT_z33Su4t_dizaXUUqG7LiBDDjWE0aIxpVhSAP5fh3lEh1nMW09LqufXK406uPexN5APVzVjFk4LGC0fllAQBsKnvBa01ED3vBa2D48T32a5xU545895iVIrSUsSISqOKl27j9BZaPj83pK8DiQe4lXv7-KGPRaOfY0-86_LL3mMOKTCe6EcYP4OFTGGE2er8BFUwR47s-KCvyyKmysALaulqvRr6LYzmzL_X2R6jNaMKtWA9kxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توپ دست خدا دلار باران شد
نشریه تلگراف:
🔹
توپ گل «دست خدا» مارادونا در جام‌جهانی ۱۹۸۶، در حراجی به‌قیمت ۲.۵ میلیون پوند (بیش از ۳ میلیون دلار) فروخته شد، در حالی که پیش‌بینی قیمت ۱۰ میلیون دلاری محقق نشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/683939" target="_blank">📅 14:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTWvoyfI93yjuNs9Od3QqKwI_TyxYXo1M3bJYBthBU2rnMutoW7o_7tU2mfP0Q-J0k8Dn5u0ZzWVRJtJtqbEUt-BQU-B4SxxGUtFosGr7V1iSr9Kanq3WPVk88adGKDNcDiQZiC-SBpoX-mltmGDrYdm24_JFN2Ty-1G1lJg-y4Du8X2S94wqBsegYRW9NZ29uaZj9bbyX3-m4STC6op5SP8IHrwRwxet-5xGWtmmVfE5gWeI7t4FdxSIMSi5YqK38_DLVVNg5uz2sy6S5DlqBNts8drOVmdz0TkUyWUU1LKO3t0aESLB96nT4l-YO4r7-9UtsCV9uMDElLr9crO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بخشی تقطیع شده از سخنان قالیباف را با هدف اختلاف افکنی در تروث منتشر کرد! #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/683938" target="_blank">📅 14:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c29214271.mp4?token=MT0mYQiomESlEMYwIO-64ggfKqqFfR3J8_SpYYCxL3BtdcmnSHBU7viqHVK1I0vBnbvaInC0CTFLiZZ9t-PJu3RTcBJ6ThCl6r05gQvNc5O1YXEZ-q63YviH9IP4JDMeebVMKcbgFtHPCootPP7piatmqQSznwyPEvV8sy1RYak1xAIj9Xpu7UOvzU-E7dcDhjc7n0667iCCCtTUVJLGtw4UnNkoM8bqq5ChOXYS7Wgegokn77OZ0Q9uDwC9WVAT2Z67-uM_XnsQL5GZc-3WeB6AdjkOn-XIhuG6yoKZFMNJmY97IXSw6t9AnSvFwoBbWwZqiVyYAAmBS9Jldq99Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c29214271.mp4?token=MT0mYQiomESlEMYwIO-64ggfKqqFfR3J8_SpYYCxL3BtdcmnSHBU7viqHVK1I0vBnbvaInC0CTFLiZZ9t-PJu3RTcBJ6ThCl6r05gQvNc5O1YXEZ-q63YviH9IP4JDMeebVMKcbgFtHPCootPP7piatmqQSznwyPEvV8sy1RYak1xAIj9Xpu7UOvzU-E7dcDhjc7n0667iCCCtTUVJLGtw4UnNkoM8bqq5ChOXYS7Wgegokn77OZ0Q9uDwC9WVAT2Z67-uM_XnsQL5GZc-3WeB6AdjkOn-XIhuG6yoKZFMNJmY97IXSw6t9AnSvFwoBbWwZqiVyYAAmBS9Jldq99Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید یخچال چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683937" target="_blank">📅 14:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d204318c92.mp4?token=kZ-Qx-i3cFcgnR361s6BLW8_b_3UsUVzHKER4Se-Z_kqwp844oe14x0Xz6yj8UQdPakSKGOnfeFuvVfnjP3aKTcnCPJ2zHmZKhMJPzlqAOvJO-9j6aQ1cwU37P15u-wzcTtAQrRPcsLkHq-V-7h45duEEyeJGMW-Y73pg-7aRU6HBXr2_N1E9PHrWULk-XM5FNM81bZ8XH9cEkhdESxobTWW3y9docSxWQw9-6_ZP6j_immV5RjcLjXjqEUIhH1QLWZL2PjmnqGqXnyQ_8xPfH2jiQgd1WH6yAn6h7NGpMOMeqO490eyWkZr41un46NP73dchRdZi5zdK09GhPuwCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d204318c92.mp4?token=kZ-Qx-i3cFcgnR361s6BLW8_b_3UsUVzHKER4Se-Z_kqwp844oe14x0Xz6yj8UQdPakSKGOnfeFuvVfnjP3aKTcnCPJ2zHmZKhMJPzlqAOvJO-9j6aQ1cwU37P15u-wzcTtAQrRPcsLkHq-V-7h45duEEyeJGMW-Y73pg-7aRU6HBXr2_N1E9PHrWULk-XM5FNM81bZ8XH9cEkhdESxobTWW3y9docSxWQw9-6_ZP6j_immV5RjcLjXjqEUIhH1QLWZL2PjmnqGqXnyQ_8xPfH2jiQgd1WH6yAn6h7NGpMOMeqO490eyWkZr41un46NP73dchRdZi5zdK09GhPuwCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: از رفتار تفرقه افکنانه پرهیز می‌کنیم  پزشکیان:
🔹
از آب و خاکمان در برابر دشمن دفاع خواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/683936" target="_blank">📅 14:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73c0a03d80.mp4?token=POoFlDd-grFkutPIu0S_9_kmLdqH-ygTHnwrwgluDw2IrU_gwBnkFw4EiR5Zkd4g6ECMStg-m4HJsPB66yKWehKmKYxsde7Kh0RGHufSm9Mk_zBedLRNznGme5U8Er12WOdSe9od9mffqUVdBi3WYYFq716gwqcoFtI0F8Aw-DC7QoEZuNQXlpTiLj7NJEhb-V2oHmAogaTJYtfff3Q95vxxNbjbqVAXkyIJUJ9C20cFF19dtSDHnn7YY8FXMd-rRFOIo94HyjF7BBDgrtspeLv5nl1s--p5eW8ArhleYtWubH1f_Ku6yzOXISQ9Ob8kcYet-oaYCs0DJIAZz32Y8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73c0a03d80.mp4?token=POoFlDd-grFkutPIu0S_9_kmLdqH-ygTHnwrwgluDw2IrU_gwBnkFw4EiR5Zkd4g6ECMStg-m4HJsPB66yKWehKmKYxsde7Kh0RGHufSm9Mk_zBedLRNznGme5U8Er12WOdSe9od9mffqUVdBi3WYYFq716gwqcoFtI0F8Aw-DC7QoEZuNQXlpTiLj7NJEhb-V2oHmAogaTJYtfff3Q95vxxNbjbqVAXkyIJUJ9C20cFF19dtSDHnn7YY8FXMd-rRFOIo94HyjF7BBDgrtspeLv5nl1s--p5eW8ArhleYtWubH1f_Ku6yzOXISQ9Ob8kcYet-oaYCs0DJIAZz32Y8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود تماشایی غول آسمان در لندن!
🔹
لحظه فرود A380 هواپیمای غول‌پیکر امارات در فرودگاه هیترو لندن، واقعاً دیدنی است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/683935" target="_blank">📅 14:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683934">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edf0a1588.mp4?token=R7R63AgxBCS8GJ8ZJlWJ9HFFgQV3F524giuP3lPHHg_A8lm7uG2vEiUZScklEWf490O1qfcaJzNcOARyBp0YjpytFnUk555Ac7Y-uq-1fAkAUpcHcmVEOoKUBHaPegXuNa0Nztp9ysZbkzMlSn0-8a66nBiQWmXpcnpotTsYxwYJVz2GU7C25yXHHsejBDLxD81X7ZD3ZU7RzAY0-eirj1-QzoBU-vONWgczPMlhPxoyh3NSJ_kZT38m77BY_kN5-plLukc7IGclgGQhm9LpcO5TYwV2PHqYACZL3w8Y-mFX2qWO_t6VlaDQQsZ2wcvzTWAyII6hS4CEGk3TKWEJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edf0a1588.mp4?token=R7R63AgxBCS8GJ8ZJlWJ9HFFgQV3F524giuP3lPHHg_A8lm7uG2vEiUZScklEWf490O1qfcaJzNcOARyBp0YjpytFnUk555Ac7Y-uq-1fAkAUpcHcmVEOoKUBHaPegXuNa0Nztp9ysZbkzMlSn0-8a66nBiQWmXpcnpotTsYxwYJVz2GU7C25yXHHsejBDLxD81X7ZD3ZU7RzAY0-eirj1-QzoBU-vONWgczPMlhPxoyh3NSJ_kZT38m77BY_kN5-plLukc7IGclgGQhm9LpcO5TYwV2PHqYACZL3w8Y-mFX2qWO_t6VlaDQQsZ2wcvzTWAyII6hS4CEGk3TKWEJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فکر می‌کنین کاربرد فلش کوچک کنار آمپر بنزین چیه؟
🤔
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/683934" target="_blank">📅 14:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683933">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فرمانده کل ارتش: باید آن‌قدر تلخی در کام دشمن بریزیم که از آن سوی دنیا نگوید نقشه ایران را عوض می‌کنم
🔹
ما باید دشمن را ناکام بگذاریم و آن‌قدر تلخی ناکامی را در کام دشمن بریزیم که بداند ایران جای این نیست که از آن سوی دنیا بیاید و بگوید نقشه کشور را عوض می‌کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/683933" target="_blank">📅 14:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683932">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fd2d7782.mp4?token=DGqjDwYxT6n0cxrH_3PPYmKU7AhAXB8sUYMypWU_7P2Pr7QYkaf2BVv2y9EUi1BnX4EX6oEYCTXs6uL1TkoN1G1rGb1uSynvUZX_fA_-yVvU-qgHYUPN__BhHOrTaI-jddr_ul-XIBSWjad2o_k4tJC-QbNYXf83kZ2g9I-EkIwXMd-xXkZ76NnN1qkOUFh7NOCKmQmxsbE6Td_KARzTO_lqT-WWghECTDX9ly9XlNgsY1hrou5TLf1ckrnfY8XrwhZ1-l5NoexoZwcluvgfzXGXHa6LxpCIxPErvKzcuHW2cKGdhd8LmpWDBCmZRbFUBY5Ux6G9PWoZpreZYlf-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fd2d7782.mp4?token=DGqjDwYxT6n0cxrH_3PPYmKU7AhAXB8sUYMypWU_7P2Pr7QYkaf2BVv2y9EUi1BnX4EX6oEYCTXs6uL1TkoN1G1rGb1uSynvUZX_fA_-yVvU-qgHYUPN__BhHOrTaI-jddr_ul-XIBSWjad2o_k4tJC-QbNYXf83kZ2g9I-EkIwXMd-xXkZ76NnN1qkOUFh7NOCKmQmxsbE6Td_KARzTO_lqT-WWghECTDX9ly9XlNgsY1hrou5TLf1ckrnfY8XrwhZ1-l5NoexoZwcluvgfzXGXHa6LxpCIxPErvKzcuHW2cKGdhd8LmpWDBCmZRbFUBY5Ux6G9PWoZpreZYlf-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: از رفتار تفرقه افکنانه پرهیز می‌کنیم
پزشکیان:
🔹
از آب و خاکمان در برابر دشمن دفاع خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/683932" target="_blank">📅 14:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7ft-lgiOlUmTja6JtNZ6xXmFv3TA_IkKxbr9cf2MTr12RE31Q5ofUhQGpv8RbVWJU4sFD5jK7MCUxIewDapHY_z86XdlbX0c1znrpeuC4dr6Rmb-W1HE6Xxq_20bT0Duy8Ud6ksZ-q7zIRI0G6FfY6EFxo2x6OvT5HtC5Ulrc5meb_5xO_W6XsTbHHSE7sX5nyPBxecKRN9ARm1a6CgtUsxccevUmjJqnVrGv-nXnQ30AjsM72VJ7n8q6P-g2HRqnaKNI30d31rtevTSa602UaJmZxc4G4Zc075HDG5gfbvbIfCRtLb3BDyzxHrPzrUt7hB-iq0LiVaiFLGf5uO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlV1nip8fQ1JDR1abrNwiG90FAuelcD2Azwvlo06IqYjp3Ul5c4jogvANSLmjFvyNEow4267HbTKcM12BVquzdk9N1TTsXcISzL_8wnjdxJBt3t938VkF2NoMHgeMUAwE6BysRtXCkVnbFx8EViIuc8MRLjUGhAsdwQjCOFXc96BZakNeLnrNJRvKFsVATtOweLse8R_0kkCTn1AfWOf9bujSUu9GckgkD2jJmTF-qUONLZjRLGIFDu69ai0BHFZtCNfdDsqMwt3csdM55eeJvtR5bCfPAUwN84Jx4LGAM_sSHng39mYdYc7cKGoZ36JcCgnKyJvBwvqeaMg3keczw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان بلوتوث درواقع امضای یک پادشاه وایکینگ است!
🔹
نام بلوتوث از
هارالد بلاتند
، پادشاه دانمارک، گرفته شده که دانمارک و نروژ را متحد کرد، لوگوی بلوتوث هم از ترکیب دو حرف رونی
H و B
، حروف اول نام هارالد بلاتند، ساخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/683930" target="_blank">📅 14:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اژه‌ای: درباره اصلاح قیمت بنزین اختلاف‌نظر وجود دارد
🔹
سخنگوی سپاه: دکترین نظامی آمریکا بر این اساس است که این کشور بتواند به صورت همزمان در چند جبهه وارد جنگ شود
🔹
رئیس‌جمهور: وظیفۀ ما خدمت به مردم با هر گرایشی است.
🔹
تمدید قرارداد قلعه‌نویی به چهارشنبه موکول شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683929" target="_blank">📅 14:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683925">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fracDNEQSutoRCbQydHwN3czIV9tVTX-nj2EYybxfIRXkMJH8MYbF2X4IDNF8cUI5qsaFm6xkFCqfDbCXjBiqan1o3doIqphY2lrbgCI4TKc52C2ACD8IicaGDM6UgxaBnJ6QtPRfPRYwgdgHDNug-TuZplXwpd_895g9u2zlRIiRfJPLFDzTWDzYtwlL6le0sJ-6dTXRN3p0A0inuLFAHlknV1T0Kvf3NzhogfpmAnFe4DaYBoQrOqCNYSYPXOEV9PmBeWzY8dVKp_ufBqAOjW7RnAit6Qpcf0nL2Q0hx4hyN0sDhZcIOohawCT0gEnJxTyS30dRfHETGiaKdGyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuWvuWW_uB7-UqBytQBKQJPLucml5zrr6-VKYMD70sMzQZ6DDiwvE5XycT0kXSfO7nRqbeXqQM6g5zTcOq1lPGzFs_M6227J1Y3svK-tJMUn56OZfVHy0x__hNAE2lRPVvijEMOfuT9QBHsBOfzGSOkKiauGTCguJvB4fTjDooFvSUBlThVPrKU9hWZRwEq3lFkDi7SPP1u76k6Obw7j2qJi55320RzadqLZ1CAZ3PxiiZ6pYqWjYoM_rjt8SaBc6a49UvEDV1mlQPITibHnplqU2qHjHm2whvZiqkpB_SybZdj1TErXre_7x5vZsOqQvTFZFeecJA1t5oURwpYNtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3f0b88.mp4?token=eM3jp2MWuQo9VAxEY4aAstzFRis1c8-LYEvJvyNpj4U_LUUeqGBkY9acA8nWoqQ1dq2Az3PRvtZEVnFg8vDIciXdfOwP8SzlwdS-uop5EAleFF3vO65vyVF7VoV0uGMirN9Y41DslUzT2Bp41k3NXhBmAJRpoxybjTO7C_FNoEpMzOdo_YobDOw0mEd58uF7Vqy6vw1E-Bl43g0Qzgai_99PSSDKTvofUW0QlcfmCOPLuzrA0VuZdjHxwJmmG3tA4wEKxOZAEpPH6QSdbpHP20jHXSoCH_3fASrcWzPD1UWuZBJDPcauj5nlhlil0F2NOupdgTLFQbOmjL6hrhaN6mY23U3ImrYxmxpedmOjamYpcsf9VGDc62Z56gCHGYAw5VCU3-hFgjsLKg55NuX-QscyvokzRsRS1T74hkchDT-Nx415IOxVZ6X-MD0SyEDG7FhTs8p-HryRqW9rZor7sMqyGunuIbOpVNR5w1-nZrA3bxr3dk09lHKs0wEnJ2MhOBC6aOXjynq3yMknqK8NLGiPxQ4WHFuBhOkgHBKtDMBhKb_OC1OCXIvNcN3uUGWbeem35rCVKaIV_KLjL_cQOgDcCExmFa1Os7_1wZc4fo9-xrQM_Pse8T0kEznNwmQieBC72ns-ywYnMC9y7iDweAMQEr-0qy_bTJ6svwHm8gc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3f0b88.mp4?token=eM3jp2MWuQo9VAxEY4aAstzFRis1c8-LYEvJvyNpj4U_LUUeqGBkY9acA8nWoqQ1dq2Az3PRvtZEVnFg8vDIciXdfOwP8SzlwdS-uop5EAleFF3vO65vyVF7VoV0uGMirN9Y41DslUzT2Bp41k3NXhBmAJRpoxybjTO7C_FNoEpMzOdo_YobDOw0mEd58uF7Vqy6vw1E-Bl43g0Qzgai_99PSSDKTvofUW0QlcfmCOPLuzrA0VuZdjHxwJmmG3tA4wEKxOZAEpPH6QSdbpHP20jHXSoCH_3fASrcWzPD1UWuZBJDPcauj5nlhlil0F2NOupdgTLFQbOmjL6hrhaN6mY23U3ImrYxmxpedmOjamYpcsf9VGDc62Z56gCHGYAw5VCU3-hFgjsLKg55NuX-QscyvokzRsRS1T74hkchDT-Nx415IOxVZ6X-MD0SyEDG7FhTs8p-HryRqW9rZor7sMqyGunuIbOpVNR5w1-nZrA3bxr3dk09lHKs0wEnJ2MhOBC6aOXjynq3yMknqK8NLGiPxQ4WHFuBhOkgHBKtDMBhKb_OC1OCXIvNcN3uUGWbeem35rCVKaIV_KLjL_cQOgDcCExmFa1Os7_1wZc4fo9-xrQM_Pse8T0kEznNwmQieBC72ns-ywYnMC9y7iDweAMQEr-0qy_bTJ6svwHm8gc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاکلیدی رزینی؛ یک ایده کوچک برای شروع کسب‌وکار خانگی
🔹
این بار در #چرخ_زندگی سراغ یک ایده ساده و خلاقانه رفتیم؛ ساخت جاکلیدی‌های رزینی دست‌ساز.
🔹
با کمی رزین، قالب و چاشنی خلاقیت می‌شود جاکلیدی‌های متنوع و شخصی‌سازی‌ شده ساخت و با فروش آن‌ها، یک کسب‌وکار…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/683925" target="_blank">📅 14:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683924">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RE5uNoNyZjU8-exRzzPoGfq5NROg193hCdWQaYPHHtYVfO87fq51DyJhgnvKuEB9W4PoZQvJHIND17lFoV5lnwkaEjJqQZH4Qa1cRvNDHrzr39tg0H8R3VBOD1xohZ3M7y9B5WDMSah41VqRyNmAEnCDLTc1wqFeGln7s2qdFRjiCAuz9HHdsbZ2-3JZ79YVRKtVeR3vJFLvrc4oZ0SyHRcSUasiWjkdJ9iJVxZ4UZXFask_792YxR2QamSjoxq8bjLOEFDPZiTkaJ37qPWj7AEkz4EMCZ3faaqxHGf286hzVVgrfXA4wZynD6e_lb1E-hlv-Lf8GQ3JzKR8QZRDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلعیدن موبایل توسط دختر ۱۹ ساله برزیلی برای جلوگیری از افشای پیام‌ها
🔹
دختر ۱۹ ساله برزیلی برای جلوگیری از دسترسی نامزدش به پیام‌های گوشی خود، تلفن همراه را بلعید و پس از جراحی اورژانسی، جانش نجات یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/683924" target="_blank">📅 14:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683923">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
انفجار در شهر تدمر سوریه
🔹
منابع خبری از وقوع انفجار در شهر تدمر سوریه خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/683923" target="_blank">📅 13:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683922">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/683922" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683921">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23d45155.mp4?token=e1Arp30tMNkZTeleJUWPJNs0OjdR1PnIk_EreGogz6SdZx4BfTfJZVbsW15RTJe4WrswZy_nQAhk0_8ZL0sfDEEfF_N-8d6RlzdtqHpfpQYI2DuTcm_izGLwZ_LZ-h3MqVhTAseL_qLZgu6u3EI8JtxtCOsTacZTQcMXRom4B41zk6AUDBqimCLobxtPCGj-2AIq2HsFUFom8V0ZoSJNZQXai1z6h3TfquorNeN9YVLQEpK_nHHPWeo7km_bkhf3bw1Jv30C2k2mRllvFeFu9N8NfL-maLEPC_RVbNoDmmlHGDxFuu1-SiHqNUFXiBeDFMybvFH7Lmo-3GaFXoKX3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23d45155.mp4?token=e1Arp30tMNkZTeleJUWPJNs0OjdR1PnIk_EreGogz6SdZx4BfTfJZVbsW15RTJe4WrswZy_nQAhk0_8ZL0sfDEEfF_N-8d6RlzdtqHpfpQYI2DuTcm_izGLwZ_LZ-h3MqVhTAseL_qLZgu6u3EI8JtxtCOsTacZTQcMXRom4B41zk6AUDBqimCLobxtPCGj-2AIq2HsFUFom8V0ZoSJNZQXai1z6h3TfquorNeN9YVLQEpK_nHHPWeo7km_bkhf3bw1Jv30C2k2mRllvFeFu9N8NfL-maLEPC_RVbNoDmmlHGDxFuu1-SiHqNUFXiBeDFMybvFH7Lmo-3GaFXoKX3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: تهدید به تحریم می‌کنند؛ مگر تا الان تحریم نکرده بودند؟!
🔹
رژیم و آمریکا دنبال ایجاد شکاف بین مردم هستند، آن‌ها دنبال به میدان کشیدن برخی افراد در جهت خواسته‌های خود هستند اما کور خوانده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/683921" target="_blank">📅 13:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683920">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تقسیم اموال و دارایی‌های متوفی میان وراث مشمول مالیات نیست
🔹
بر اساس بخشنامه سازمان امور مالیاتی کشور، هرگونه تقسیم اموال متوفی میان وراث اعم از توافقی یا قضایی مشمول مالیات نیست، اما انتقال اموال و دارایی‌ها از متوفی به وراث و یا اشخاص ثالث مشمول مالیات بر ارث است./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/683920" target="_blank">📅 13:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683919">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651a0e2e99.mp4?token=VMaiqlYdBdZlQm-SgwNqnr4jODEMZZpne0gpUosL4ojcZ5xpR6gEEJeulH1imNKhjkvU4O9I2lQwou1t5rni4f4wWVpV5ApXEUs4tk-92eWWUXitupIiXSkry3QrI3eBwTIHhe24I1MR_3SWatX0T5CxQ39xMJkjQpjPJSnUR3MJy_2v9oWZhT6VgJPOPnu53ioF-v0ksov2NIlKf4Iz07vCVXxHyHOwHZKtriH7mWOK6MBSYPH4fJSvqPnSE1_f3_80fIcuoMAEXoCd3DdLtOwS8bpNmNoAJp1_CnYy9rvQVUd1L77TLs6PCEEfipRFTNBqnGo86FdLZR2NwO1FQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651a0e2e99.mp4?token=VMaiqlYdBdZlQm-SgwNqnr4jODEMZZpne0gpUosL4ojcZ5xpR6gEEJeulH1imNKhjkvU4O9I2lQwou1t5rni4f4wWVpV5ApXEUs4tk-92eWWUXitupIiXSkry3QrI3eBwTIHhe24I1MR_3SWatX0T5CxQ39xMJkjQpjPJSnUR3MJy_2v9oWZhT6VgJPOPnu53ioF-v0ksov2NIlKf4Iz07vCVXxHyHOwHZKtriH7mWOK6MBSYPH4fJSvqPnSE1_f3_80fIcuoMAEXoCd3DdLtOwS8bpNmNoAJp1_CnYy9rvQVUd1L77TLs6PCEEfipRFTNBqnGo86FdLZR2NwO1FQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: پیروزی را تبدیل به شکست نکنیم
🔹
آمریکا که تا دیروز به فکر سرنگونی ایران بود اکنون تمام بحثش تبدیل به باز شدن تنگه هرمز شده است.
🔹
بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/683919" target="_blank">📅 13:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683918">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ورود فرمانده ارتش پاکستان به تهران
🔹
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683918" target="_blank">📅 13:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683917">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9a4d424e.mp4?token=In0NN2OYX52Afq0mkalWd2LFYCl7QmcuLo71etVHT1hg6e8LQruxu3wmXgD5G4Hu_bQ7JmGJR9kpp0q3Dzt4_ccW0EeqifNezF8udR30BW_0BWeTkzZNH3LHMpwyIu8lpGEKiI08M9C20yUiS6pOFOKABE7w-aWEUaPLy1KMrlaUzCoPEtgd4Dh3E7uzNcF_ptI-I4nddPaunwVwvTzbw1aQBLKRouWJMPI3mK1EN1_wOC9_eOpeHbysJJYLk7PL564JXY6RuAKtpi34lRIjcxqcRzdWiwxgl4mbj41XYq8wYCk0J2aqWhy_rdUDlZNT4pOcD7VEzP3xYvPQiqaUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9a4d424e.mp4?token=In0NN2OYX52Afq0mkalWd2LFYCl7QmcuLo71etVHT1hg6e8LQruxu3wmXgD5G4Hu_bQ7JmGJR9kpp0q3Dzt4_ccW0EeqifNezF8udR30BW_0BWeTkzZNH3LHMpwyIu8lpGEKiI08M9C20yUiS6pOFOKABE7w-aWEUaPLy1KMrlaUzCoPEtgd4Dh3E7uzNcF_ptI-I4nddPaunwVwvTzbw1aQBLKRouWJMPI3mK1EN1_wOC9_eOpeHbysJJYLk7PL564JXY6RuAKtpi34lRIjcxqcRzdWiwxgl4mbj41XYq8wYCk0J2aqWhy_rdUDlZNT4pOcD7VEzP3xYvPQiqaUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از تخت جمشید از بالا، پایتخت امپراتوری ایران ۲۵۰۰ سال پیش #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683917" target="_blank">📅 13:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqmxkS7xrYy6qwgpfG19El3-1uctEkoxrG42jwNMDW9PJAxDvejNOateL_FUAMaQ9NxEBB7qRXqJIdPi58fHoA6BaO0g-33BpcMzL5shFKPPEcLpHZ4TIc9KnwbqTjm1imATvo7v4R5mkoCK1GO3555jYmqA2V3Fz_JjaS18R7ppke0ElZuZC0f1ZGC5RSFkRuYVgTZTiNmY6T7HKej4g58tMdseTv5wW90ZmH0OWH2o75OkPw9NWavmWeK6RBN3jkhziwnwX1gwJpAbibnE0yaO2dG4PbtU69tHMwaZZ2U5oEjiWezaeCuJvQ5vNXBxVztqFA0QkD_qyY2o0W08BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFn0aQxmOPOat0xsOfl3F846ckYCObPNwsVs4smsvXcgVPdxYRV7OKxsrvaQPxZnnbztTBpHCsnuhJMlQKqCkDRMcdXMmqF-4QnDCns8I67TYOVZxkMF1kSfuhCY9j-o0MCD51tMmY5m2NxDH8grr6YnBc0313NbeG9oiqnPUJolruh2fuHf7o4DXv65nkEgx1WrKH5mamyJqOqcuuFX-C6NYKD9ff3khQ1TCiiX4KE0fEKKDhFOSEFgojvb5lCYlvqgay089-4b6kaz5gkxcroyQpB6FQVRgm8p-LIJveswP9fQb8WvcXrl5NKkI58Cy53DWpa3Mr2TottmcWrKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzTnUyerxgXrCAW1Gd2YaJ5bROwmHlLqUf455Z26d_tDWa4WuMWwM0Lc-MczW1H-mKaHaRVM5WxUtNNGguUhTDpNQ9VNIOjEbxgDxfJZCDwHABsZnXUxMPPpc8np37Gpe6bDkIF1rbxRZ_zEGWxu7XQrSvnAmIMSDmuNsUn1ZUe6MWgyIguxV7-kjWNMXYkyMx_Z1eBqAFHeeJLVCB2lZAdlBfFuWW8Ps8hboc3xw-7fpWpOlgQCSHCmOFka6VJOzoWv9j1xl2plBjgfDwYs7g4cBsIPCIVrJPt7SzCdRLBvLoLU5WSSuwSkFGwp0PG1cm9EweBFSF6MKhCONAO1pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طراحی منتسب به گلکسی S27 اولترا؛ شباهت به آیفون ۱۷ پرو
🔹
تصاویر فاش‌شده از طراحی اولیه Galaxy S27 Ultra نشان می‌دهد سامسونگ احتمالاً نوار دوربین مستطیلی و حلقه مغناطیسی سازگار با Qi2 را به گوشی اضافه می‌کند.
🔹
این گوشی به دوربین اصلی ۲۰۰ مگاپیکسلی، فوق‌عریض ۵۰ مگاپیکسلی و تله‌فوتوی ۵۰ مگاپیکسلی با زوم اپتیکال ۵ برابری مجهز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/683914" target="_blank">📅 13:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCpJGg2vH-QRZxro-pg6WBJL92bbrLvCiftyDk6HDz1-xGrV3CL3cO5yHMQl6AqimlUvHnQoBpcsEsAwPQt61974lWTLxGuxz8-YbNuLPU-ELpCvHC8RdJqXA_OmSugAxdwYTk1-uk2FXpkptcu6beNjENSeIWtWfWkt-PAptu3nCI6EuEDG8nSOyPvvAMZlgPeHPD5WCk9BuLBw83F7bET7bfO1dK_f7J_qHyy4BZeZdmWUtrt393NWVniuDJPDxbJLmrkJTFzi38KgMSkMG0ECJmpmsybpRfd3JGahjVVgaK6mQSEoqlVvh1fWWCSJYZmvi01x9yyxoh9CF-fAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲ شهریور ۱۴۰۵
🔹
بازار خودرو امروز ۲ شهریور شدیدترین موج افزایشی روزهای اخیر را تجربه کرد.
🔹
برخلاف نوسانات پراکنده روزهای گذشته، امروز رشد قیمت‌ها کاملاً سراسری بود و از محصولات اقتصادی تا مدل‌های مونتاژی و رده‌بالا، همگی یکپارچه گران شدند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683912" target="_blank">📅 13:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: کشورهایی که سرنوشت خود را به تهران گره می‌زنند، با مسدود شدن تمامی مسیرهای دستیابی به رفاه پایدار روبرو خواهند شد ‎ ‏
🔹
هر کشوری که به عنوان شریان مالی برای نظامی در آستانه فروپاشی عمل کند، باید انتظار داشته باشد که در انزوای آن نظام…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/683911" target="_blank">📅 13:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c7177ed3.mp4?token=FUEnUAzV-QAxNjRGTzAe177O_dVSl0So7VF3RXuI2e1D8PmuGoU8h4zzX1BXHJRavaZkOh9xP147qbIe_3wKylxGyBZH1rpejBEA2-1-fUokLketczdGGky0pcgX14CPL047tIHzfk9bljbtodEJsqq2t8IV5iOQdQmnzrwd1mDKvjWCo_IVO2T1fIpfs3fhOOo9OpM558w-P7mEU55z6cL7K71Lo4n4DHZcM2Oy4w_92QsuH7PpSa9Dk9NLtY9Miw3wX7k4_uPjKhyd036UUmFsa9xfXcr_aZ-74Hn_vVq0P-ax9WuU3kBRIpVXO1sXO5e5Kq7xe-tm5WMFlc9rIV7oYhFurjtHYbSDBHE-jGEE3Ud8lUedJzxtbDbJvD3vrbhz9D7z4PlaQT4psHRrApFiEss9wu0L6UZKgsXRWyc-UXn1cxJk_HpZ324X5Hb7v2YCReO4OxqB6uEf7cIptm1MQkumohUIMG0llqgj-LKorlHBxa0V8JGrDwmOMe9f5TTic_qJwMayPkFKzuf9lR-jMzDoGtZOaB6l9lH6uQ8ZlvMoESJoxnxhggOTq5xGWDWYsclJX6Nbeuwf5wwTtNc4ioh1URI3s6eNfNlQOStUCUrKDBCiVrHb8mkGl6hT_E6xqNyiq0Tb6WQ-rJVTbCnCA6P3RUcEm9EOkngj7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c7177ed3.mp4?token=FUEnUAzV-QAxNjRGTzAe177O_dVSl0So7VF3RXuI2e1D8PmuGoU8h4zzX1BXHJRavaZkOh9xP147qbIe_3wKylxGyBZH1rpejBEA2-1-fUokLketczdGGky0pcgX14CPL047tIHzfk9bljbtodEJsqq2t8IV5iOQdQmnzrwd1mDKvjWCo_IVO2T1fIpfs3fhOOo9OpM558w-P7mEU55z6cL7K71Lo4n4DHZcM2Oy4w_92QsuH7PpSa9Dk9NLtY9Miw3wX7k4_uPjKhyd036UUmFsa9xfXcr_aZ-74Hn_vVq0P-ax9WuU3kBRIpVXO1sXO5e5Kq7xe-tm5WMFlc9rIV7oYhFurjtHYbSDBHE-jGEE3Ud8lUedJzxtbDbJvD3vrbhz9D7z4PlaQT4psHRrApFiEss9wu0L6UZKgsXRWyc-UXn1cxJk_HpZ324X5Hb7v2YCReO4OxqB6uEf7cIptm1MQkumohUIMG0llqgj-LKorlHBxa0V8JGrDwmOMe9f5TTic_qJwMayPkFKzuf9lR-jMzDoGtZOaB6l9lH6uQ8ZlvMoESJoxnxhggOTq5xGWDWYsclJX6Nbeuwf5wwTtNc4ioh1URI3s6eNfNlQOStUCUrKDBCiVrHb8mkGl6hT_E6xqNyiq0Tb6WQ-rJVTbCnCA6P3RUcEm9EOkngj7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مامان اولین سکوی حیات‌روان هر آدمیه، برای همین نقش مادرها در سلامت روان انسان خیلی مهمه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683910" target="_blank">📅 12:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
آموزش ۵۰ دوخت گلدوزی با دست
🔹
آموزش ۵۰ مدل دوخت گلدوزی را اینجا ببینید. با فروش این هنر دستی، کم کم می‌توانید #چرخ_زندگی را بچرخانید
👇
khabarfoori.com/fa/tiny/news-3239788</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683909" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5pqtqXpf_bynltjQFE9xAiYGFtHpxXVIjebyHahPv_dfeIg8stQCjp6TOX0HBt8sHjsInIAj5YJ31xsBBhLrH7o5Pe81B5cvJXcyDevcsOThN3i_FGm10R9UyF_QfVTjpOL3RySCANr2spj5dvV7O68-l07wwk4F4gP4U4fSBTggove_VZ88PeFk7e4waWi8hWRX5sX0lz9VFIWH_zKJ-NpcgFmrxSD87NBOMbp8nfvh64gFS08lf1wEsTN4tiVijEv524gIviDqw13dws3BcJbo6nnLzQv_fGtNF792rszR_d_xHufZvhdx6iDHYgft-PXwvwpMG7bUSvcyMQwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بخشی تقطیع شده از سخنان قالیباف را با هدف اختلاف افکنی در تروث منتشر کرد!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683908" target="_blank">📅 12:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده کل ارتش: ایرانی تا ۲۰ نسل هم شده می‌جنگد و اجازه خدشه به ایران را نمی‌دهد.
🔹
سخنگوی سپاه: ایران در نبرد با آمریکا پیروز میدان شد.
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۰ هزار واحدی رکورد تاریخی ۶ میلیون و ۱۰۰ هزار واحد را ثبت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683907" target="_blank">📅 12:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEA8nFY2oMsE2Ecexb29TDTCi1jhTkAp82Q1Po_WNXQc44lQ7KnzQtCaJRslUc2klycDh0eBrOz7tBoT_yBUHTyPqmxRMplUgc_bL4omDQNIgfEcLrtv2YueNN2K800cV-w3uuOLqW5WGLDaXvKfJb4IT-RE94lTlhUUb05Dj0YvMrexUfnaHl6oRGLf5hlC6fBcurhQ2ElCbQjo8WBxdXzNM3Un1sFR0Jvv0U0mAloe9PNaaewyn4v8f8Os-O5eXty0R6JlEJfD1T3CrPY-o21j0I_9NlBXoYCb8uHbybvVFnDNZQ73U9FhyXPhsxH1Mqf5FGtRjh5x3nhT5PKtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت بسیجی اهل سنت در زاهدان
🔹
یک بسیجی اهل سنت به نام «نادر سارانی سخی» توسط اشرار مسلح در شهر زاهدان ترور و به شهادت رسید.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/683906" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683904">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyep0sf4hVSgOxywXcuLMiPgaBNM5XwgAmNG3j2vV56M61HWF6_k8TG7vDC7YEzXzmdjw54Vsk4rxPc1aPnuNIq3k567nIOGaQX0Iq-tdfwQn6rtyCiS053dXCUd2dU_pt16VXTCxPFbUMAVLWW1Om7pvJ2H5KqGBvT70QOKf8OCpW_to3CiJPJ-pIlmXMI03ZTfAdrHa5ffUeb7JdsRYQ7sLHBRgLc7Uhb6EX9jxgHTWGEOQePwGHJdUMo3CbNewQUSyhQ3ck4KcPUcLdPQZ4VYsPJBZzbb7ciX8yb4ln4J1_7G1ZCbYTgonGbVO9SABmVLga8OfEhuSli5zKZQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان سابق فدرال و ایالتی آمریکا: پس حالا دوستان ما کره شمالی و روسیه هستند و دشمنان ما کانادا و دانمارک؛ منطقیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683904" target="_blank">📅 12:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683903">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آغاز ثبت‌نام مسکن استیجاری تهران و مشهد از فردا
وزارت راه و شهرسازی:
🔹
ثبت‌نام مسکن استیجاری زوج‌های جوان در تهران و مشهد از فردا آغاز می‌شود.
🔹
از ساعت ۱۲ روز سه‌شنبه ۳ شهریور تا پایان روز چهارشنبه ۴ شهریور متقاضیان مسکن استیجاری زوج‌های جوان در استان‌های تهران و خراسان رضوی انجام می‌شود.
🔹
در این مرحله ۳ هزار واحد مسکن استیجاری برای اجاره به زوج‌های جوان فاقد مسکن با اجاره‌بهای حمایتی عرضه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683903" target="_blank">📅 12:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683902">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3325bfbe5f.mp4?token=kv-4OdchXN5YRX_tPZhRakCe5rRrKvsxaK33c4pGLURSsn6BDXMg6f5CkmkouVTOG84Hbrb4QB57E6Ze9Jc862czc5nAcZ5Tr5JwJfGnMehs_B6N6p33e_wjIkE2ZD3cVxHISqxCOTkOJAmCgVyAx3_rDP2CKGf0SEhei_2bhd9Rgq-xajhUk8pz67wxJu30RX38CvBK3RDpboNnSB7b6sbUJA8E9fz_ZtRADklNB7qsBNSh-mGLzDz4DKzokYVlIvBOjn30zgH72i872cwHvGBl5QxzLLG6VVVeRFHffVRNO2drnBDgmpT67Y2_j0QY7F4oUQ5pjE_XcjNLaLOIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3325bfbe5f.mp4?token=kv-4OdchXN5YRX_tPZhRakCe5rRrKvsxaK33c4pGLURSsn6BDXMg6f5CkmkouVTOG84Hbrb4QB57E6Ze9Jc862czc5nAcZ5Tr5JwJfGnMehs_B6N6p33e_wjIkE2ZD3cVxHISqxCOTkOJAmCgVyAx3_rDP2CKGf0SEhei_2bhd9Rgq-xajhUk8pz67wxJu30RX38CvBK3RDpboNnSB7b6sbUJA8E9fz_ZtRADklNB7qsBNSh-mGLzDz4DKzokYVlIvBOjn30zgH72i872cwHvGBl5QxzLLG6VVVeRFHffVRNO2drnBDgmpT67Y2_j0QY7F4oUQ5pjE_XcjNLaLOIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خارج کردن کیست هیداتید از مغز
🔹
کیست هیداتید یک بیماری انگلی است که خارج کردن آن از مغز نیازمند جراحی بسیار دقیق برای جلوگیری از نشت مایع و گسترش عفونت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683902" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ورود فرمانده ارتش پاکستان به تهران
🔹
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/683900" target="_blank">📅 12:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کلید اولیه سؤالات کنکور ۱۴۰۵ در هر پنج گروه آزمایشی منتشر شد.
🔹
رئیس بانک مرکزی: مشکل تامین ارز نداریم.
🔹
فرماندار جاسک: احتمال شنیده شدن صدای انفجار کنترل‌شدهٔ مهمات در جاسک وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/683899" target="_blank">📅 12:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683896">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران در حوزه حمل‌ونقل و لجستیک بین‌المللی
🔺
اتاق تهران با ارائه مشاوره تخصصی حمل‌ونقل بین‌المللی، فعالان اقتصادی را در انتخاب مسیر و شیوه مناسب حمل، کاهش ریسک‌های تجاری و حل چالش‌های گمرکی، ترانزیتی و بیمه‌ای همراهی کرده و مسیر تجارت خارجی را کم‌هزینه‌تر می‌کند.
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683896" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683895">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
الجزیره به نقل از رویترز: فرمانده ارتش پاکستان پیش از سفرش به تهران، با ترامپ تماس تلفنی برقرار کرده بود
/ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/683895" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683894">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Opr-gKStKtyhIQ8LKHC46lDUlmQ-2kSaLZMjUpPWhUpW1eUhyk64ERjwiWhw6KfyaaOgSXRLCf2AkkdL-bTb4WV3pBrhRyLP9PEKEl9ZVLdmt_CExNsAkDvaZZF3K-XovHvi3OYzEaTrAYInCJrozSWvf82LR-Th0JS4S1R7ShRTgSNEFOyunFuqPAIIyqICfDmxPYcsaLXF1AHwLSNXjdpmRW-LDAgJdu1960ZyNhd4X5XuU68kJZ38PYa-GjJZhp4j1AHYRfoA_m8-U9jQKtLij1vbEmKSSJfm8AgathI4L28TkXQy4zfQ09gP1b1ww35U61isD2GtW_DSRxkoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرش پازیریک؛ یکی از قدیمی‌ترین فرش‌های جهان
🔹
فرش پازیریک با حدود ۲۵۰۰ سال قدمت، نشان‌دهنده پیشرفت هنر فرشبافی در ایران باستان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/683894" target="_blank">📅 11:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683891">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2803d6a33.mp4?token=NR-Kx4WDGnejljMU7VI54iXdZRlwIyfuv7lnsuGHG7ydCXZv_fDxDKGnQFEMYOcXZVyNwNEHRRnvIWyb0rzWF3PJP-EAysIetZkRbSEQheh88oJAG5TF-SkSRkRCo5t_nfYx1u3I0qofV2d6aZLjItcjtkr-ahUpzEUxaxfHZGoWTAHINw7ALn4CAvBOAQk5FyJKGEW0OVZudoPPjPxMFXVeDzNNa42TTfqKV_pn9y5uKytod2T9KSuyqigbM3UChza4-MyLf_54XuiUJOA41mAQyET4FTSuwqZy-XbJJzwL3sg34auHHD_rjNCMHeMm3H5w36j3SpAt5YilRZS4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2803d6a33.mp4?token=NR-Kx4WDGnejljMU7VI54iXdZRlwIyfuv7lnsuGHG7ydCXZv_fDxDKGnQFEMYOcXZVyNwNEHRRnvIWyb0rzWF3PJP-EAysIetZkRbSEQheh88oJAG5TF-SkSRkRCo5t_nfYx1u3I0qofV2d6aZLjItcjtkr-ahUpzEUxaxfHZGoWTAHINw7ALn4CAvBOAQk5FyJKGEW0OVZudoPPjPxMFXVeDzNNa42TTfqKV_pn9y5uKytod2T9KSuyqigbM3UChza4-MyLf_54XuiUJOA41mAQyET4FTSuwqZy-XbJJzwL3sg34auHHD_rjNCMHeMm3H5w36j3SpAt5YilRZS4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: از «تحریم‌های فلج‌کننده» تا «فشار حداکثری» و جنگ اقتصادی، آمریکا به‌دنبال تسلیم‌کردن ملتی است که تصمیم گرفته از حقوقش کوتاه نیاید
🔹
تفاوتی نمی‌کند چه کسی سکاندار سازمان ملل متحد شود؛ عملا کارکرد شورای امنیت و خود سازمان زیر سؤال رفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/683891" target="_blank">📅 11:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3BHuX-75eTl7Pvytg2iELDNCipXw85DnRWrtxlKXRHOJbOBHiJujZpxdXM-cTy9_wjAw0higoAJvITuWFmV1BQrjwOZ7IxTxmRbX6i9b1sZJqHavQFr-HXOyd3ajEKMnle_zbpryMDkUlUI3K-05Quv16deMdjZAS0r5wKGz6Gb_ag-zCDF20Dgy2Fmn2qE94zi1T-Bemff8bLttP8jL0q5vIPaJyHxwYk564mg9_Z34WBeITMYaCA1vbxdRMtb2sw4XLxWo7nSQxXCI9bEi2Bjvn_aLBK1KOo_OFkpTOgxFa8-K2iJRgKuAD4idU2gfm2GUcaku3DoPyLn69snwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: شناورهایی که با شناورهای متخلف همکاری کنند به فهرست متخلفین اضافه می‌شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/683889" target="_blank">📅 11:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdf70a392.mp4?token=sMLRqRrVdyBgGX4lXZP5NqE-QCZYbKAmxrAwva5467G7oFVwKARJnbz_yCvQKyhZeZ5PzW-kXgPjqB1VJGhEoUPALgxBq_H_pSnlZsTH0Iqy-kGWYGqOM0fRajr1azxeNpOKdk5JhelLq8WzQmgnctvzhSmBKYKVOvmFs8NHnvSGmxaBnutXR6-R6BSEkbavK7ZE4r3URvLoz0HD7grU002mx1DXB3RxN8n7E0CNcm7MKdgBsYv_f6ndOS1xjgkhvbaKpD80Kk-_Mpu4eb-ajB4Rz37-Llzo4RZSPxMMlKq-55AP7J9occpr2wqAJ4way8K3GuLM804VuQ1MtZPnlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdf70a392.mp4?token=sMLRqRrVdyBgGX4lXZP5NqE-QCZYbKAmxrAwva5467G7oFVwKARJnbz_yCvQKyhZeZ5PzW-kXgPjqB1VJGhEoUPALgxBq_H_pSnlZsTH0Iqy-kGWYGqOM0fRajr1azxeNpOKdk5JhelLq8WzQmgnctvzhSmBKYKVOvmFs8NHnvSGmxaBnutXR6-R6BSEkbavK7ZE4r3URvLoz0HD7grU002mx1DXB3RxN8n7E0CNcm7MKdgBsYv_f6ndOS1xjgkhvbaKpD80Kk-_Mpu4eb-ajB4Rz37-Llzo4RZSPxMMlKq-55AP7J9occpr2wqAJ4way8K3GuLM804VuQ1MtZPnlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: رایزنی‌های آقای قالیباف با مقامات عراقی روند همکاری‌ها را شتاب می‌بخشد
بقایی درباره تعطیلی سفارت شیلی در تهران:
🔹
تصمیم گرفتند به خاطر صرفه جویی مالی سفارت را تعطیل کنند و در برخی کشورها این کار را انجام دادند؛ این به معنای قطع روابط نیست
🔹
دو هفته قبل سفیر و کارکنان سفارت انگلیس به تهران بازگشتند؛ ظاهرا به تعطیلات رفته بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/683886" target="_blank">📅 11:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c317278ea.mp4?token=qTCJzgSAMneMWoELhbaDKWrSPPCI1iwVH3jsb_2RfKD-7E882DcLRHJRO0udigvOlD85I51SqFS4FoRsCTJLG-4w6Gsy7TZB0marqlF_C1qYA4l86TSMC_FOzHPADIEn68xw5IvbF0jwsqza3T33tAXZ_vt6QnLjT-Jwa5MjTqRSg7-ydKgU4Hi-7iIOKhZu7uz_FygJi6-souh3U855jPjmYTUsY7lUiDPQ4Yot-YkLOhKMEjYvX-8nVD4mB7rzKKrCxnz4KTo-9hhVW2w5RSPkMYRtGAdO4jsIB8gPL-6iiTmEVt2wKUMBBDY8xQcsF4rnCpj9bDRYqW99Zd8gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c317278ea.mp4?token=qTCJzgSAMneMWoELhbaDKWrSPPCI1iwVH3jsb_2RfKD-7E882DcLRHJRO0udigvOlD85I51SqFS4FoRsCTJLG-4w6Gsy7TZB0marqlF_C1qYA4l86TSMC_FOzHPADIEn68xw5IvbF0jwsqza3T33tAXZ_vt6QnLjT-Jwa5MjTqRSg7-ydKgU4Hi-7iIOKhZu7uz_FygJi6-souh3U855jPjmYTUsY7lUiDPQ4Yot-YkLOhKMEjYvX-8nVD4mB7rzKKrCxnz4KTo-9hhVW2w5RSPkMYRtGAdO4jsIB8gPL-6iiTmEVt2wKUMBBDY8xQcsF4rnCpj9bDRYqW99Zd8gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مگر ما جنگ را شروع کرده‌ایم که خودمان را به‌خاطر ادامهٔ آن شماتت کنیم؟!
🔹
حتی کانادایی‌ها به‌عنوان همسایهٔ آمریکا هم دربارهٔ آن‌ها گفتند «امضایشان را با مداد می‌نویسند».
🔹
تکرار تحریم‌های ناکام علیه ایران حاصلی برای آمریکا ندارد؛ جنگ اقتصادی آمریکا نظام تجارت بین‌الملل را تهدید می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/683883" target="_blank">📅 11:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtyxZi9eSWb6nedU3-1LN_elhA9ZIq7nSedeuS3XbIC9aNOxJ-EOV6xqME0x432VgQIcTCUPzeuXwbQIsb5bFvrgkIX7Wr0IIlFEEYjuEoYm3Xg8TfncOdc-eqINI9pMfclTkhjRFMSXLPc-I_rAFN2CqOeoHHrWZkkyD0Mp6xSXVsf9xUIhvbby1yXJJhkPtDS2nFZuhLrsm1Lo72CGnfT3J6FMJksrvYsSziTG6QxryScmXPQihTAJpTB0vHhw53e7x078LMy2tTjb3aivKSuNLZy_cGgKLsE2yejko3BRm0tUSfmeEfVIAP62saWzWRfEGFdEihu8IkKyue9CYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا همچنان قله فتح می‌کند
🔹
قیمت بر اساس سایت رسمی اتحادیه طلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/683882" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cdc830a2.mp4?token=IDS0BLP_yecVTd-WWCCY_WyJX8zTIaaEatJW03iYQawymo0zlCmL4GCCZ1U34Hj0Cmi9q3fUv231ND-O4FhYgnej2ksAlHBK24Qpen3P-Ihe35UxGfL-5GLU1r7Nl3sFAZ9y7gttf5faLBt4uiEWxvCJvxArpsRQcKloo_6u1RuoKZK5fos5BlMQ1qWxqe_tzFYiQHjWMhyny6nQPbYkO5ohxzv4Y5fhPyBI-nc-qWBiRd3PwmOrH4teJR3VdCduGdJoUCawBC-Ipd2q0wl4UMXZxpHWhIP1vC4gFlxADIEDrbttQ5AYPhzmCVAiO8_jXvkKZ4xKhIdricl-HvZtwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cdc830a2.mp4?token=IDS0BLP_yecVTd-WWCCY_WyJX8zTIaaEatJW03iYQawymo0zlCmL4GCCZ1U34Hj0Cmi9q3fUv231ND-O4FhYgnej2ksAlHBK24Qpen3P-Ihe35UxGfL-5GLU1r7Nl3sFAZ9y7gttf5faLBt4uiEWxvCJvxArpsRQcKloo_6u1RuoKZK5fos5BlMQ1qWxqe_tzFYiQHjWMhyny6nQPbYkO5ohxzv4Y5fhPyBI-nc-qWBiRd3PwmOrH4teJR3VdCduGdJoUCawBC-Ipd2q0wl4UMXZxpHWhIP1vC4gFlxADIEDrbttQ5AYPhzmCVAiO8_jXvkKZ4xKhIdricl-HvZtwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران در حال حاضر ترکیبی بازی می‌کند
سخنگوی وزارت امور خارجه:
🔹
ما از قدیم شطرنج‌باز بوده‌ایم؛ در سال‌های اخیر پوکرباز هم شده‌ایم و حالا مدتی است که ترکیبی بازی می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/683878" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683876">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86534c54a.mp4?token=KXbn7yEi08GcpSwfyYBvpOx7Kxhc4tVHIUFF7QOx4DBwrm01JnFEmg7nehNzXXYCvuVjlq018LXUqBzxRqv-egDXe6D7OvmnTG5I_3rizTS7Txi2Vq6qZIbVUXp8LwtlIMc5aFoQJi-aKnIgwmSGyfS2UUkiDq4cNNzZm3D9vFM5wixXfm3UMOkrZ2rQQUEW3bsjlSjfQYBvlrYpcJqlHGEOC0vXxhRWJtl1LSj37NK0roSKmZX02DtRIo9kFHWarzh2_Cz2ivs54KVjIW4ufAT5Z82MZ5UV-zXQSID8RKqEWFxYkEOOjoE9Mnshu-jyv5b98DP2MMMWAkt4MbZlDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86534c54a.mp4?token=KXbn7yEi08GcpSwfyYBvpOx7Kxhc4tVHIUFF7QOx4DBwrm01JnFEmg7nehNzXXYCvuVjlq018LXUqBzxRqv-egDXe6D7OvmnTG5I_3rizTS7Txi2Vq6qZIbVUXp8LwtlIMc5aFoQJi-aKnIgwmSGyfS2UUkiDq4cNNzZm3D9vFM5wixXfm3UMOkrZ2rQQUEW3bsjlSjfQYBvlrYpcJqlHGEOC0vXxhRWJtl1LSj37NK0roSKmZX02DtRIo9kFHWarzh2_Cz2ivs54KVjIW4ufAT5Z82MZ5UV-zXQSID8RKqEWFxYkEOOjoE9Mnshu-jyv5b98DP2MMMWAkt4MbZlDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: برای عضویت در پیمان مکه دعوتنامه‌ای دریافت نکرده‌ایم اما برای گفت‌وگو با این کشورها دربارهٔ امنیت منطقه پیشنهادهایی مطرح شده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/683876" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683875">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940e004647.mp4?token=gG34oKx9z8d-YeibADuWrMvVUcW_v-mCb1cY73rQxsgxe1b-aqXivr0AMAfGpkGFdKKAxvxrXF5-P8v-o2NlZEB3DI56HZ6CNI7Mk9bnKtVZoZBJuhyh_IyPMZcl8eLzqiL6qOrZMhxQfk1tH6_G2MgpTQP_s2JCvZvzkoEkKyLpA8dQIEzcdGCJubRKFaeIqL4CpnJN0_Rwq3YuzdJzeMwOWcs--CsPRKrzAnj4uAtfu06s_ArJ49CLlOu1vFr5FffApu4JLw58ntlaV8aY1KiMGassygZd0alzPwxG2gslTpcKfERx-H89tlc8Mka0T7fCmHVI0kz2t7Lat1uvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940e004647.mp4?token=gG34oKx9z8d-YeibADuWrMvVUcW_v-mCb1cY73rQxsgxe1b-aqXivr0AMAfGpkGFdKKAxvxrXF5-P8v-o2NlZEB3DI56HZ6CNI7Mk9bnKtVZoZBJuhyh_IyPMZcl8eLzqiL6qOrZMhxQfk1tH6_G2MgpTQP_s2JCvZvzkoEkKyLpA8dQIEzcdGCJubRKFaeIqL4CpnJN0_Rwq3YuzdJzeMwOWcs--CsPRKrzAnj4uAtfu06s_ArJ49CLlOu1vFr5FffApu4JLw58ntlaV8aY1KiMGassygZd0alzPwxG2gslTpcKfERx-H89tlc8Mka0T7fCmHVI0kz2t7Lat1uvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای المیادین به نقل از یک منبع ایرانی: ایران دعوتنامه‌ای برای پیوستن به «توافق مکه» دریافت کرده و این موضوع در حال بررسی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/683875" target="_blank">📅 11:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683872">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c354ca7c68.mp4?token=MWgBZniz-YeZ14UJRfEC8N4Qo7eDjcZ4JFoBgAOVzs4ZPDjB1qCTGTvJaYaArDBN6rOX8pAkB0EhRZ8jBh5vllsIrTkyP6f0T8T0hngiljZzO9hLxQFN1QT4OwiROoIhEEskjz2TvyjIvgytY7Nc8LeUrcd0IZOIPoCvNkw0T4dWwbfFS3mE7DJYMMIQvcEM6yi51EbqK_7cvAfMRb9tv8DgC1jQ6kZ0HW0ofCfgjvoxeHGPls_3xPAqflCVLsey5ikBtwN7T7RMesciM0yWVMNMSMee8GwKfdD8qpkDySk8haB0NIbLIPnNWK0pd5k2zTNpAVlOwycHgLhjCr08I6e3TyXCTB9IOYIThsVcRp1jPInpX1x9Y4S_ScOuawng4DRb7w81whKQ8V-AQESMWo8Qsg2CWrLL0S96yB465A14jB9FJ7Y8I0E79DhrB-fKYGS0JTeM7dZ6cQGcuMevSuHXDnXfQ1prg8k5GnUnr0yDX7SZoe2HGxwiYVrxIm74cZxNsxucRkGFgIAyWXT9Ci3xasOoGnAJRFKp5u8TtHxNS27L5Ahe80d0L-OAw8zFjJQhCoYTpdb5J9-k6kIIrBoO3dyLeCXXhrcIORqRLJgcdyYCcN1IJS3FdsdnDfG79wp8HgSbMNiQ6smtzmLkVAaPZhq4Ozj45QOb5KRidQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c354ca7c68.mp4?token=MWgBZniz-YeZ14UJRfEC8N4Qo7eDjcZ4JFoBgAOVzs4ZPDjB1qCTGTvJaYaArDBN6rOX8pAkB0EhRZ8jBh5vllsIrTkyP6f0T8T0hngiljZzO9hLxQFN1QT4OwiROoIhEEskjz2TvyjIvgytY7Nc8LeUrcd0IZOIPoCvNkw0T4dWwbfFS3mE7DJYMMIQvcEM6yi51EbqK_7cvAfMRb9tv8DgC1jQ6kZ0HW0ofCfgjvoxeHGPls_3xPAqflCVLsey5ikBtwN7T7RMesciM0yWVMNMSMee8GwKfdD8qpkDySk8haB0NIbLIPnNWK0pd5k2zTNpAVlOwycHgLhjCr08I6e3TyXCTB9IOYIThsVcRp1jPInpX1x9Y4S_ScOuawng4DRb7w81whKQ8V-AQESMWo8Qsg2CWrLL0S96yB465A14jB9FJ7Y8I0E79DhrB-fKYGS0JTeM7dZ6cQGcuMevSuHXDnXfQ1prg8k5GnUnr0yDX7SZoe2HGxwiYVrxIm74cZxNsxucRkGFgIAyWXT9Ci3xasOoGnAJRFKp5u8TtHxNS27L5Ahe80d0L-OAw8zFjJQhCoYTpdb5J9-k6kIIrBoO3dyLeCXXhrcIORqRLJgcdyYCcN1IJS3FdsdnDfG79wp8HgSbMNiQ6smtzmLkVAaPZhq4Ozj45QOb5KRidQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلسه‌ای که رهبر انقلاب استاد راهنما بودند
🔹
این فیلم مربوط به دوران پیش از زعامت رهبری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/683872" target="_blank">📅 10:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683871">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXTECrbQfzbmfDV5Azv7q8PIfiw-064SwR3Bu8Jk-XhlRW2-R76QE99oazjxuA2t14xV4UEe_Eo02XLyaRcdNTyN8IlFjcmkI521uhCTsh78crd6EVvD5hKXGC_OLO9QN-HFiV3oz6F7kEqfGTTqodXGEih4ZMmY5wa8tC0yh9C0pAu6q7zakx1rbq5CvGW-hdhDNXmPTu_K8QcciT6kEUiuJ_kfXLslhCsJ3fB0DjfHF6x7_B980tk28N4mbW8FQAQrUAJJdil7v7olOcCryHHt84zFUlRO-j8brgKEqy1vHKw15hbRZhbmNQsVvM5kr4eAJEOJznJm473bAwlOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/683871" target="_blank">📅 10:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683869">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81555e7b8.mp4?token=s0dDgS6ISfHphHNnyd4BsyVm1SUBLQngWqZvgGuO9ayaD_PlSyO_53R1-qFqwxdLexWdCDIcnK-l-H02jlr5vrUy8l0iZbUOVBgsADYm9x4jF-fjJQPnCGH6Coko0f5uejYRZzIBuG0p-AQG2P1QjV59qCa_7F07ugXBN80m8ZxVOK6UAJtFM23CexcuApd4cauCn1tUBGtn9rfSim2zEpgkREGVIOWRFMyAOPjJ8ktimAAYJuQkA1cTdIAm9MON8DylOAIj8-kkTs6EZKkq5YDI4ZQv9ACU01n65FXRJQnhjZo0qzUg-TGM_R4AQ-fBh0E-30ZhzPZj3C2jCIZxpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81555e7b8.mp4?token=s0dDgS6ISfHphHNnyd4BsyVm1SUBLQngWqZvgGuO9ayaD_PlSyO_53R1-qFqwxdLexWdCDIcnK-l-H02jlr5vrUy8l0iZbUOVBgsADYm9x4jF-fjJQPnCGH6Coko0f5uejYRZzIBuG0p-AQG2P1QjV59qCa_7F07ugXBN80m8ZxVOK6UAJtFM23CexcuApd4cauCn1tUBGtn9rfSim2zEpgkREGVIOWRFMyAOPjJ8ktimAAYJuQkA1cTdIAm9MON8DylOAIj8-kkTs6EZKkq5YDI4ZQv9ACU01n65FXRJQnhjZo0qzUg-TGM_R4AQ-fBh0E-30ZhzPZj3C2jCIZxpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از وضعیت عجیب ترافیک تهران و موتورسوارهایش!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/683869" target="_blank">📅 10:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683868">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImvIZ0LpeQNG66FrmLEXfHyZeVtuQZlk2c_O5E-f4impzRR__NDvkDvuWpt5qcRcvd25iTekY9Stq0oHMIwICwmxPmvRipfw0tdXxnxL-xjRbSA8zIYKFYmoROcthv4CNXAZ012HASm2sECvadSHldpMEFah_trb6ni0VVNlrq1hPplLrwnv-aaGhhhESUfT05_WzfSVna3vZbgUO5XoRDbdNQ3YDi_kQMDtweoye50ODV2J1Dc4vKdkdBxWI1J3Nd8mzE0LmWI8JvhhyfyTIFg-NX7oRyWX-dxqC3k-feO61ntIqpST2HJFu7IVb2aaffT7NQnZk5DpvZ9qWt2AQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌ روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌ صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/683868" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683864">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a634c77154.mp4?token=NTBBjhbezU9wS2CuPD9HKcvvSfrdCAFHv8nv03xkZFfwisrQXkZskNczpym0E9YaD0CSdHoUI30P3FF9WtmhRxAEKxaLtFElzfjx3h2SNLy4arGOe5jfEJQdh88URrrvqhvG9uVLG_Eon4Wr9uSuHRH1k_ljHZsOD2FmIgGWdzHYPWaKov6KIdq8XNIwfT7p_bGgAxNBdQTHNu4f01iw6PMotZERnJMkFdUv3ynGP9rhljEhbP3Xmznz3j5urIctiu1Xw97khzdaltJ2-z74ux1z7LxGhyKFvFLEkGKAIJNq4IAYeRVOlgHmyb41UNFMicQTa2Zi2yQwVPxlD0ryhGrrr-Om26HkMUmHUg4anCOXfSmN7UMTdR4eWjb42ebViAiTFWVDiDazKfsn5UusKJEsg4mfAxGAJ9aeT07CQSOGEE4uo2DmuTPZMomYF0XUIXwXPm74Q8Dc0QakNSJajOvdz_ts2G9mfhBVXX5tsm6ufvfgRBJjLlN6KPVNX4cGPNL8WpNlRoiIg5MKy4A7C-2bME4q-CfJMNKFBU8-D-Xgse6K_cyc28mQeZeHT9IbdGnaLC0D-CTLLSurLPKvBW2BMF8iw7GzrWeYxwjQJaQxX7agivS-C2ipNxSR5l8xDmgj5zOoD5kJ_PLPBvGmhCYOy19uIHp2CTGSY2D5jFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a634c77154.mp4?token=NTBBjhbezU9wS2CuPD9HKcvvSfrdCAFHv8nv03xkZFfwisrQXkZskNczpym0E9YaD0CSdHoUI30P3FF9WtmhRxAEKxaLtFElzfjx3h2SNLy4arGOe5jfEJQdh88URrrvqhvG9uVLG_Eon4Wr9uSuHRH1k_ljHZsOD2FmIgGWdzHYPWaKov6KIdq8XNIwfT7p_bGgAxNBdQTHNu4f01iw6PMotZERnJMkFdUv3ynGP9rhljEhbP3Xmznz3j5urIctiu1Xw97khzdaltJ2-z74ux1z7LxGhyKFvFLEkGKAIJNq4IAYeRVOlgHmyb41UNFMicQTa2Zi2yQwVPxlD0ryhGrrr-Om26HkMUmHUg4anCOXfSmN7UMTdR4eWjb42ebViAiTFWVDiDazKfsn5UusKJEsg4mfAxGAJ9aeT07CQSOGEE4uo2DmuTPZMomYF0XUIXwXPm74Q8Dc0QakNSJajOvdz_ts2G9mfhBVXX5tsm6ufvfgRBJjLlN6KPVNX4cGPNL8WpNlRoiIg5MKy4A7C-2bME4q-CfJMNKFBU8-D-Xgse6K_cyc28mQeZeHT9IbdGnaLC0D-CTLLSurLPKvBW2BMF8iw7GzrWeYxwjQJaQxX7agivS-C2ipNxSR5l8xDmgj5zOoD5kJ_PLPBvGmhCYOy19uIHp2CTGSY2D5jFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوکی شکلاتی بروانی رو در  کمترین زمان ممکن درستش کن
🍪
مواد لازم :
🔹
کره ذوب شده ۱۰۰ گرم
🔹
تخم مرغ ۱ عدد
🔹
پودر قند ۲/۳ پیمانه
🔹
وانیل ۱ قاشق چای‌خوری
🔹
آرد ۲ پیمانه
🔹
بکینگ پودر ۱قاشق مربا خوری
🔹
پودر کاکائو ۳ قاشق غذاخوری
🔹
لایه شکلاتی ۵۰ گرم شکلات سکه ای شیری…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/683864" target="_blank">📅 10:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CminvTVBWkWpCv9Eo3_jOw_cp-uNtqIchEVjkLiCpyMD353OYwrn0jlbSm-C22mDcEC1LEnODHlTMA2-3wNe-wUodZoU22FW6v04me3cClUhO2_QXkc96ZYIYBzc1DZeBKmGTTVt2tzbONFt4A28jHG1152VA_-PCBvolpbSHFHaFVy706zf9edmmxhzrM-naD9eeFOgfKIvZWJjWedxYNGUeOWAp2CrKkQfQbzXX9V_-M7tpJFaoeW2iGX6RZZwVNZ9uPe6pZcc2psbMEoA3XVuITnlb7rVxlQjZawyS1RJG6X6wLsI9SqtN9HvXzcIT7XhpJTEgMGeTRBJxCFLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت معاملات آتی طلا برای اولین بار از تاریخ ۱۴ مه، از مرز ۴۷۰۰ دلار به ازای هر اونس عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683863" target="_blank">📅 10:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quosBDr7ZP83oTwVpXX7lL4V36TZjXkp_5yp7ck4QQkD0IZQN4eBgqtLVIuLdY4v4O4mXjwGVQK5BUV_0jz7sOdBLDp_vxokMXpjSKMYA7lCX8nviRnJGfxwlP6MZYdgVSWMyDvG9cioBvUZUstT-5Rap73PywSRXWKvVRVkrmWIHJK6NftYRUVdA7vSN7dz0J4iYut5w9s-ZRa_--cuPdvcLpOccB1a9kxbSmkcTKpxAQGAIByAZe4zlJ5Qj_yee--VFa2bqx0JYnV4indR-ghOTnivGSQMtN3ixCm13y0ehZKqttnkdB6zjA9hoNUsMEnfyF6bevyTesGYt8jVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محاصره‌شکنی کشتی ایرانی در «روز دی»
🔹
طبق گزارش پایگاه سوپربرو، یک کشتی کانتینری منتسب به ایران توانست با عبور از خط محاصرهٔ آمریکا در تنگهٔ هرمز وارد آب‌های ایران شود.
🔹
این درحالی‌ست که ساعاتی پیش وزیر خزانه‌داری آمریکا در یادداشتی از آغاز فشار اقتصادی جدید علیه ایران موسوم به روز دی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/683862" target="_blank">📅 10:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سود ۴.۵ میلیارد تومانی وام جدید مسکن/ قسط ماهانه ۵۱.۵ میلیون
🔹
با افزایش سقف جدید وام مسکن، سود این وام به همراه تسهیلات جعاله در تهران حدود ۴.۵ میلیارد تومان است.
🔹
مبلغ قسط وام ۲ میلیارد تومانی در بازپرداخت ۱۲ ساله حدود ۴۰ میلیون و ۲۷۵ هزار تومان است. کل سود این تسهیلات حدود ۳.۸ میلیارد تومان و کل بازپرداخت وام‌گیرنده در ماه ۱۲ سال دوازدهم حدود ۵.۸ میلیارد تومان خواهد بود.
🔹
در بازپرداخت وام تعمیر ۴۰۰ میلیون تومانی قسط ماهانه حدود ۱۱ میلیون و ۱۶۰ هزار تومان و سود آن حدود ۲۷۰ میلیون تومان است. کل بازپرداخت وام تعمیر با احتساب سود آن حدود ۶۷۰ میلیون تومان خواهد بود.
🔹
به این ترتیب سود وام ۲ میلیارد و ۴۰۰ میلیون تومانی خرید یا ساخت مسکن حدود ۴ میلیارد و ۴۷۰ میلیون تومان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683861" target="_blank">📅 10:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683858">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13db53a616.mp4?token=MIKa1OAT3KRhrpZrYVfrn9x7qJkXNbTnLCHK5ur5tq3JIpMYL4ZWYPbSCuCTphTapnsxE6xyzcvw3V6Ws9SGeRJaUzXdegYfqZNZ2b9qjX69VS78U2BwREvWf7rYGI6HlN-GUGMbh3T4PiQCezCoIKqMqcyQctTOolD2Y-n9_EQEkLjwkj1TjHJAo4dTpo_CIEwHy7LBsQyiai3crop2A5hlUwZ9cobvZUYpb4D27KkJaCwZBJYaEJtBwPv5mGU7m1EGYItbdoXhZJ7paUD7X4ngJ_mGuwtjhsbJNHizLsGZxTB8wiNXaQPGZC9B5KoFOm5j71J-jLEqUtE_jG3Fkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13db53a616.mp4?token=MIKa1OAT3KRhrpZrYVfrn9x7qJkXNbTnLCHK5ur5tq3JIpMYL4ZWYPbSCuCTphTapnsxE6xyzcvw3V6Ws9SGeRJaUzXdegYfqZNZ2b9qjX69VS78U2BwREvWf7rYGI6HlN-GUGMbh3T4PiQCezCoIKqMqcyQctTOolD2Y-n9_EQEkLjwkj1TjHJAo4dTpo_CIEwHy7LBsQyiai3crop2A5hlUwZ9cobvZUYpb4D27KkJaCwZBJYaEJtBwPv5mGU7m1EGYItbdoXhZJ7paUD7X4ngJ_mGuwtjhsbJNHizLsGZxTB8wiNXaQPGZC9B5KoFOm5j71J-jLEqUtE_jG3Fkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین در حال آزمایش «ربات‌های پلیس» برای گشت‌زنی و کنترل خیابان‌هاست
🔹
در شنژن و هانگژو، این ربات‌ها با دوربین، رادار و هوش مصنوعی می‌توانند با لباس عملیات ویژه برای شناسایی موارد مشکوک در خیابان ها تردد کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/683858" target="_blank">📅 09:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683857">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29000cf9f.mp4?token=hev_VG-cd-eSFaQH3w5uqx5t15gQXjAGt9oNbVvfrFAUsDGyI9zQaZUyL2RuMLFOJq2vuCq5V67n436kX_2HWaQ0ltMhpH27x9jMXGfeaTkwDryoHtINXnT2WyP3TvyAPZoPaT8xiVsX7QS0G4qrKUZy14YscwONaVCTGIDZD-te3nsoGqvPkvyl_a17f6S6hEjuEfzwKKF-kbYsrlHEkRIp4KlDEWTwkzGVE36KJ0KWFfyo2pD8Fu5PQ8NAlUtY6DPVSGjr3_IvM0_bN3GpHnMYgnqnZSNmhY1t2sni4Xg0gnQyocvGi6NCPy34jjURrusgEW4MNZD6yn83nrgMe3bkWcMJRaM4JKkDSlenw9Yad7c-mfIWlxSTBoltguu-QN6qNF0d1dWX5RAeOPrpXvdzsyrv94I4dtJknEPwoE_PxKha6GW45Fz325tkcQoKWhPPePecw5-hbtatWd0qP5mhRlr-kQRTV3Ls4-ErWYDbj7S5R4C3e5cvn7L_Z5Wsr2akYc037CpmdR-cEqCz_SGPFYG7V69k3pkCCAS4av4PnL2pVXqqaDh0PYXNpQuNcZHmGvczwsbWlgDpy8O1jU277ZX3A7DYDQcTa1HSzPUgEwEZFpP7JqBl_Kv4y2YWYG1ClgP_Ug59etMkETpxQAHTNYCh4ilPBWVZx5KSs28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29000cf9f.mp4?token=hev_VG-cd-eSFaQH3w5uqx5t15gQXjAGt9oNbVvfrFAUsDGyI9zQaZUyL2RuMLFOJq2vuCq5V67n436kX_2HWaQ0ltMhpH27x9jMXGfeaTkwDryoHtINXnT2WyP3TvyAPZoPaT8xiVsX7QS0G4qrKUZy14YscwONaVCTGIDZD-te3nsoGqvPkvyl_a17f6S6hEjuEfzwKKF-kbYsrlHEkRIp4KlDEWTwkzGVE36KJ0KWFfyo2pD8Fu5PQ8NAlUtY6DPVSGjr3_IvM0_bN3GpHnMYgnqnZSNmhY1t2sni4Xg0gnQyocvGi6NCPy34jjURrusgEW4MNZD6yn83nrgMe3bkWcMJRaM4JKkDSlenw9Yad7c-mfIWlxSTBoltguu-QN6qNF0d1dWX5RAeOPrpXvdzsyrv94I4dtJknEPwoE_PxKha6GW45Fz325tkcQoKWhPPePecw5-hbtatWd0qP5mhRlr-kQRTV3Ls4-ErWYDbj7S5R4C3e5cvn7L_Z5Wsr2akYc037CpmdR-cEqCz_SGPFYG7V69k3pkCCAS4av4PnL2pVXqqaDh0PYXNpQuNcZHmGvczwsbWlgDpy8O1jU277ZX3A7DYDQcTa1HSzPUgEwEZFpP7JqBl_Kv4y2YWYG1ClgP_Ug59etMkETpxQAHTNYCh4ilPBWVZx5KSs28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: کاهش سهمیه‌های بنزین قطعی است/ کسی بیش از سهمیه بخواهد بنزین خریداری کند قیمت بالاتری خواهد داشت اما هنوز این قیمت تعیین نشده
🔹
تفاوت قیمت بنزین با کشورهای اطراف زیاد شده است. تردیدی نیست که باید در وضعیت بنزین مداخله کنیم.
🔹
وقتی تولید در نتیجه جنگ کاهش پیدا کرده باید مصرف کاهش پیدا کند. در مورد سیاست‌های قیمتی تردیدهایی وجود دارد و هنوز گزینه واحدی را نمی‌توانم اعلام کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/683857" target="_blank">📅 09:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbZJZ5O1XgCBYxa_ar6AHxqfgNwPyrcOyQ3hJkb3daIgrtv1CcwlPPUehe4Z7F3RZCZlWPeqbMjPkwymGrCSj5bhUm6_YgZQ2TvYsm22xmYgoRYldVLczO7a3zGPBNkM5EpYj_uM1ZQSszGC0w7TBCbNV_pzrnP_MHJcuqVkFFlZFgHg6oQDD-jdaIv6K_9cHDF96KP2dTdQtj0iK8d33yxvreipUXl8Jq7XmQRCUVEpcOrdSOvSXsIcV6q_ONOXEW9laPoWE-XgQGcP5CWl6HtcAiOcd9iNC18hQwqHL6XFTfvd-XO0GayC1DVevCDJQAXk8lsV5yb_nw5fV_JtMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقتصاددان آمریکایی:
تحریم‌های اقتصادی بی‌سابقه ترامپ علیه ایران نه‌تنها نتیجه‌ای نخواهد داشت، بلکه نتیجه معکوس خواهد داد
پیتر شیف، اقتصاددان و مفسر مالی آمریکایی:
🔹
کشورهای دیگر این محدودیت‌ها را نادیده خواهند گرفت و از آن‌ها تبعیت نخواهند کرد. ترامپ هم نخواهد توانست تحریم‌های تلافی‌جویانه‌ای را که تهدید کرده، عملی کند. علاوه‌بر این، ارزش دلار کاهش پیدا خواهد کرد و قیمت مواد غذایی و انرژی افزایش خواهد یافت.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/683854" target="_blank">📅 09:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051fc127c8.mp4?token=AkVzqjXJownO07uD08EPQQhIHAl2atcztnVWrl0vV8jt5dLRyFfyL2xisTAT7SAw9WQsFWaqKYqy4MOu0na9sxjxgwOw_3XTpcj1jwg9jbuTibVDVGRmu51aMrHBTM-1FtF8iI29XxJROTAcB9CKdfhSWwxbnfox5awZm6NeJV63yCaPbqr-EnSf7wyZfGs_JvfBTGlqWh679ANdJbG-KZ_8DlrsfsiSrKE3d4-Wtlsolz7OVNl8fa4IS6KpB03arTw9rFhKjztRFHd_0__7Vvz060G7TSUJ5Tg4cnrPpaQMLAi0lusRrTlG3mVRRgIKzTN8XGgYHWxZ30N0_R1OIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051fc127c8.mp4?token=AkVzqjXJownO07uD08EPQQhIHAl2atcztnVWrl0vV8jt5dLRyFfyL2xisTAT7SAw9WQsFWaqKYqy4MOu0na9sxjxgwOw_3XTpcj1jwg9jbuTibVDVGRmu51aMrHBTM-1FtF8iI29XxJROTAcB9CKdfhSWwxbnfox5awZm6NeJV63yCaPbqr-EnSf7wyZfGs_JvfBTGlqWh679ANdJbG-KZ_8DlrsfsiSrKE3d4-Wtlsolz7OVNl8fa4IS6KpB03arTw9rFhKjztRFHd_0__7Vvz060G7TSUJ5Tg4cnrPpaQMLAi0lusRrTlG3mVRRgIKzTN8XGgYHWxZ30N0_R1OIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزوهای دشمنان به گور خواهد رفت
سیداحمد خمینی:
🔹
ما را با موشک نمی‌توان از بین برد چون ما فرد نیستیم، تفکریم.
🔹
امروز همگی پشت سر رهبر معظم انقلاب حرکت می‌کنیم و آرزوهای دشمنان نیز به گور خواهد رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/683853" target="_blank">📅 09:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683851">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRasa_factory</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f718582c3b.mp4?token=E_s8YcTyA-xjUGbMgcebDw1EhaonWB7iwe7U_pEjQZZEmfxSUrB5APYB8Hyk5JQIVAmhCq5SnKiBy3MzpIfI-3kT9qgxrcDvr2OT6pLj9UnjAZnx3n4ujMpst678hSeNZY7D1Yq1RWJfVbU8IrhQb7K40MB9KKtW7agwfptFAXHXZmuOb5pDGrj1J7arctejHrD4nO6xkPGF8hbsDJ9U8PtS-A_UWZGN7lPdO-YgXFtfuOla_H8F2FKcJdlvD9JBqwFtIpi12pvsxIq4h4AZa5uw6YqtL64N6ESVQC_Ur9K5tr49jkhgkNEXcT_krm8tZ2022vZIcMaVaGv0xj8fVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f718582c3b.mp4?token=E_s8YcTyA-xjUGbMgcebDw1EhaonWB7iwe7U_pEjQZZEmfxSUrB5APYB8Hyk5JQIVAmhCq5SnKiBy3MzpIfI-3kT9qgxrcDvr2OT6pLj9UnjAZnx3n4ujMpst678hSeNZY7D1Yq1RWJfVbU8IrhQb7K40MB9KKtW7agwfptFAXHXZmuOb5pDGrj1J7arctejHrD4nO6xkPGF8hbsDJ9U8PtS-A_UWZGN7lPdO-YgXFtfuOla_H8F2FKcJdlvD9JBqwFtIpi12pvsxIq4h4AZa5uw6YqtL64N6ESVQC_Ur9K5tr49jkhgkNEXcT_krm8tZ2022vZIcMaVaGv0xj8fVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فـروش ویـژه درب‌های داخلی
(ضد آب
💧
ضد بخار
🌫️
خود اطفا
🔥
)
💰
فـقط بـا 4 مــیلیون تـومان
💰
راسا‌دُر با ۲۵ سال گارانتی تعویض
✅
منازل،هتل‌ها،سازمان‌ها،بیمارستان‌ها و...
🔻
برای اطلاعات بیشتر تماس بگیرید
05136666789
📞
09153068010
🔻
لینک شبکه‌های اجتماعی راسا دُر:
لینک اینستاگرام
▿ ▾ ▿
لینک تلگرام
راسا‌دُر تنها تولیدکننده درب‌های پلی‌وود
در شرق کشور و مشهد مقدس
@rasa_factory
|
گروه کارخانجات راسا</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/683851" target="_blank">📅 09:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683850">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVPe7ALiwCFENh_PhBOMmoSlFth861rMki-gYKsqlMtr56eGpDMFGebioWkT9739eNhtYkrJ-fJDx_ZhWT4PqaAgW-0CLqy2-To6FAhMjtMZgU2UTlu88aDmPkmGVeRay62ZdiCsN67fBsX8dM0DJgyUk-DnEAdaU-_8_JXzMRxoPPbNEJQIUp8A-qGcSN5k3yD3b2JbG_8t2e1VXxKLapbveVifHOQSu4ws_xqUKiraCA1HN1al8LXbOzGQ1waxyY6PZBsYVNzoWpmWDfxnLKHO5AddkSv5yV3PV8MHUMx8lN76kH1vyEMSMQnFLxVxZsnCeGdWYrRqttN-38Mm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت خام آمریکا تنها برای ۴۱ روز دیگر باقی مانده است که پایین‌ترین سطح در نیم قرن اخیر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/683850" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تورهای گردشگری لاکچری و گران قیمت در طبیعت، خیانت به محیط زیست است/ مسئله اصلی «لاکچری بودن» تورها نیست
همشهری:
🔹
تصاویر و ویدئوهای منتشرشده در فضای مجازی از برخی تورهای فوق‌ لاکچری طبیعت‌گردی، از انتقال چنین تجهیزاتی به دل طبیعت حکایت دارد؛ تورهایی که گاه با عنوان «اکوتوریسم» یا «گردشگری سبز» تبلیغ می‌شوند اما حضورشان می‌تواند با تخریب پوشش گیاهی و خاک، ایجاد مزاحمت برای حیات‌وحش، افزایش خطر آتش‌سوزی و تولید پسماند همراه باشد.
🔹
رحیم یعقوب‌پور، استاد دانشگاه و کارشناس گردشگری در این رابطه می‌گوید ممکن است تعداد افرادی که توانایی یا تمایل به تجربه این نوع گردشگری را دارند بسیار کم باشد اما آثار مخرب فعالیت یک نفر می‌تواند به اندازه آثار منفی تعداد بسیار بیشتری از گردشگران باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/683848" target="_blank">📅 08:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/289ce816c9.mp4?token=r4cPe8rhIotxmfq2hpoF2RN1E6jsN052fT6tW7Aw1HbKnB16OVfqFDI0oK80FGptAdAMizRo0f3I91_WAmSZKe-r-vMGVD-EVhTGJTX8w3YEmq9XZaZmYn290FoWj0Io6xLLV1KF9GwqOmjBcoxrb29TD026StDYx4JrPDLm5VQG0Z6iaz0jbWW512iO0JISj8OHruCU5euUUYjW1zo4f3lX2iD8mtBdZLJ9oCdRrGuGcK6Ebx7L0snjZoINV6iz9LGHacVHA8fPzk9Eatsn1M3By8NaxfGr4Tm1vX8OXJYg4WHwZVyCa_C_S2Tl9esh8rcmJBZ6EqfULp-LLFUxxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/289ce816c9.mp4?token=r4cPe8rhIotxmfq2hpoF2RN1E6jsN052fT6tW7Aw1HbKnB16OVfqFDI0oK80FGptAdAMizRo0f3I91_WAmSZKe-r-vMGVD-EVhTGJTX8w3YEmq9XZaZmYn290FoWj0Io6xLLV1KF9GwqOmjBcoxrb29TD026StDYx4JrPDLm5VQG0Z6iaz0jbWW512iO0JISj8OHruCU5euUUYjW1zo4f3lX2iD8mtBdZLJ9oCdRrGuGcK6Ebx7L0snjZoINV6iz9LGHacVHA8fPzk9Eatsn1M3By8NaxfGr4Tm1vX8OXJYg4WHwZVyCa_C_S2Tl9esh8rcmJBZ6EqfULp-LLFUxxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بگومگو ترامپ و ملانیا در حاشیه مسابقات رالی
🔹
ویدیویی از گفتگوی ترامپ و ملانیا منتشر شده که ابتدا معمولی به نظر می‌رسد، اما رفته‌رفته تبدیل به بگومگو می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/683847" target="_blank">📅 08:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
رئیس پلیس امنیت اقتصاد فراجا: مردم برای خرید طلا با سکوهای دارای مجوز رسمی و قانونی معامله کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/683846" target="_blank">📅 08:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd6e28b26.mp4?token=QWd59hh0BCgxjaKk8ODGp8BD1WaKKTx6-MPpLp0DpVHi2kOMu1BjQlhpkrji3KInEKvckwCHNU3JdzcKaecRlQqZJIk_vrvW97KRjHXfhtXgQEm_m7pyrJwGDZd5YNRAkZ4UqWNcoYU0Zc7lSIhnLeDhgjE7B4Q_vYETkhP7m3iXw_OaDLxtVskiZPxIML5THq0LjIZH0-1lZKxmxXySP02GSczQtpOKq0KxmjoEaBRZRA_GDEBVCS8p_9X1btOPr9P9bGdI9yzgMIqx8epTyHrQqSpZUcedIIRGZnkdo7MO12LLITJfLGydYgN05T8EZAXCT5ccnAA3hEueCyERgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd6e28b26.mp4?token=QWd59hh0BCgxjaKk8ODGp8BD1WaKKTx6-MPpLp0DpVHi2kOMu1BjQlhpkrji3KInEKvckwCHNU3JdzcKaecRlQqZJIk_vrvW97KRjHXfhtXgQEm_m7pyrJwGDZd5YNRAkZ4UqWNcoYU0Zc7lSIhnLeDhgjE7B4Q_vYETkhP7m3iXw_OaDLxtVskiZPxIML5THq0LjIZH0-1lZKxmxXySP02GSczQtpOKq0KxmjoEaBRZRA_GDEBVCS8p_9X1btOPr9P9bGdI9yzgMIqx8epTyHrQqSpZUcedIIRGZnkdo7MO12LLITJfLGydYgN05T8EZAXCT5ccnAA3hEueCyERgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه از غزه مانده است...
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/683843" target="_blank">📅 08:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b43863683.mp4?token=sWKK7_QvK3XJGlhh7tOHwxBXGlUJ-ax2n4EaTB710lokZgcOSbdX39eOWVm1vhvT1ICwc4-JFsTaRsO4ddwzoJeIzZqsNdmTgRw3FgEzwLVGCQ4FkMW_6dm3VugWMEAupEJqTUfdLidp2UvPy3gzLx3hglNRjg-4tZrwnM5nc50HmK38aLj7QfPNG0Ed3K7yVzCe8kQIFee5vNuZjjlJCKsECwv5sOGQuXEgoNQ7pIC_gljAl4JfT6GePWUkmNvsvFCmsyBCR_C0YJ1MEoVstG7S2LA8HKrFzVmnHU5GFyQPumilyLPmTLxvdR_rLEfxjAhcGTSxk8pAyLAPcllFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b43863683.mp4?token=sWKK7_QvK3XJGlhh7tOHwxBXGlUJ-ax2n4EaTB710lokZgcOSbdX39eOWVm1vhvT1ICwc4-JFsTaRsO4ddwzoJeIzZqsNdmTgRw3FgEzwLVGCQ4FkMW_6dm3VugWMEAupEJqTUfdLidp2UvPy3gzLx3hglNRjg-4tZrwnM5nc50HmK38aLj7QfPNG0Ed3K7yVzCe8kQIFee5vNuZjjlJCKsECwv5sOGQuXEgoNQ7pIC_gljAl4JfT6GePWUkmNvsvFCmsyBCR_C0YJ1MEoVstG7S2LA8HKrFzVmnHU5GFyQPumilyLPmTLxvdR_rLEfxjAhcGTSxk8pAyLAPcllFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ نوشیدنی در ۴ زمان طلایی؛ قبل از صبحانه تا قبل از خواب چه بخوریم؟
🥛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/683842" target="_blank">📅 08:03 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
