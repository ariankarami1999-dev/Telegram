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
<img src="https://cdn4.telesco.pe/file/k7yAyFMoAUslVIAkE70Ugk_OvvPFooBQdwQNAIW9tbtJ_-w8yvozrltYel85Mo9wdOadDcetMyQRdmVlXv-YI6YYl7TW3saYME2fVNU_kXbFHtVwDrtxAfOZHI6hoRSqQj_p9rE-qbnHHTr2KyCsKH8l6_8n-hdACFATvEfubY7t6b7vCwwipWar_sK8OYZ07I03Y86l_w2vpw2h5SmCxlPMnNkpLhtWDGuDNhwqPlexKUO2j6sH7oF9J_EBlKyD11_SrhYtBnCxxHVe4QmWooOwozlMyXFl0huPOqxNgOPZS3Q8DZSppvS11p7qjK0sZOEf80ZSegwQaLCe6mIBAA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سقوط بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده در دریای عرب
ناوگان پنجم ایالات متحده اعلام کرد که یک بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده که به ناو هواپیمابر USS George H.W. Bush اختصاص داده شده بود، اوایل روز چهارشنبه در دریای عرب فرود اضطراری انجام داد.
سه نفر از چهار خدمه در وضعیت پایداری پیدا شده‌اند. جستجو برای یافتن نفر چهارم در حال انجام است.
ناوگان پنجم اعلام کرد که هیچ نشانه‌ای مبنی بر اینکه این وضعیت اضطراری ناشی از اقدام خصمانه بوده باشد، وجود ندارد و علت آن در دست بررسی است.
این دومین سقوط بالگرد نظامی ایالات متحده در منطقه در هفته‌های اخیر است.
یک بالگرد AH-64 آپاچی ارتش در 9 ژوئن در خلیج عمان سقوط کرده بود که ترامپ گفت که نیروهای ایرانی آن را سرنگون کردند و خدمه توسط یک قایق بدون سرنشین Corsair نجات یافتند.</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SBoxxx/18158" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:  چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.  چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/18157" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:
چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.
چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/18156" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">موجودی نفت خام آمریکا در ذخایر استراتژیک نفت (SPR) در هفته گذشته به پایین‌ترین حد از ماه مه ۱۹۸۳ رسید - EIA|</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/18155" target="_blank">📅 18:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/18154" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz8BLBZAuUp22AX6M72SzYmx_0RUyDzmKAfVp3eZeEo_icygXfcGtSeNNecm_TOagWh1SDGBtHz9yNw3v9D5l2dbUR4d5suUpkoImHACh8Y7anIJ5DQguBlSU7AN8mggkJpG3fDtbou-kqzwUS1r3mfL8xes-Extkl6HSf09osj-snWybzSJbn29E_2oGhR1mp3MkTYgv228v0LbZvwkQurrndXNpxGBV2DrLWWFhM3xT5I85Sxt15QTymkiFLa4qTjhBsxH1T7IFPM7rfTalCYC9YJZH1Hz3n3DP65165EaANic_5Dm8i4wxI1tPi5ZXESm3dbk4v_xUkyfL7hi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سومین روز متوالی ، امانوئل مکرون با عینک آفتابی دیده شده است.
به نظرتان کار آن عفریته زنش است یا صبیه وجیهه رفیق بهزاد؟!</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/18153" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گفته می‌شود با اجرایی شدن این توافق، قیمت چص فیل در سرزمینمان بزودی ۹۰ درصد سقوط می کند</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/18152" target="_blank">📅 15:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18151">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به گزارش العربیه، آمریکا و ایران به توافق اولیه برای آزادسازی ۳ میلیارد دلار از دارایی‌های مسدود شده ایران دست یافتند.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/18151" target="_blank">📅 15:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/18150" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTSQCwX0-jhCkUt2ePYgmNnkHdCQ-sPEqcMGqIgXHI5gRL96C62HzGCQHHfhsSvWZ2C5nIwsID91wVRhcbi_y0XWT5im1SW_w_ekQo1u-Y7BdebdFDvv-pUtbywS-SoII7vhN1R8qdABdFoJpVc0YgQWGnHDbb7csjtdNYxL0aqD6rlE-CPV4opOBJLJcTw-9Cf9ozv2T3Z7A-5328GyiKRHFI8-CuFkRo3kLP8IOOSU9fpObV4U_FAVBCQNX2zCaYepnFMB5rjkx1CV0xB-gInL9Dammg9cdxR0jyxy2cPnhVDGpEP4WVFRzVhB4f6rFO6iw0vKZNtqBtpSERn2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد دارایی های ریسکی و افت بهای نفت!</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/18149" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18148">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQPjnn3cGV37BqaZZOip9uf5sUcQzWarDEY1PplAbjlPLwsIM6FOQ9tmq8c-jM45PqIF3GcbNhBcm6bDDMjNmQRVJR-g2CGKeRbxS5tQwZwyZc3-r3wwn_V5s905-I66h5xgUHN0w2urHaR5XC-mGEFjQQ1UyV4IHIl1WQmdyLRPGT56ULEVjp5fxwLKdlFjy5ib8axeBHYGcUbhIJCRTBz3ZEAmxW8XC3Se9e3Xm8pJivTrYtIQetNXfs9wF6DJoACDePDIibDwE3GQsJluKd57lJHZnPYm7E0C4qMI9Q8KHxWPl6--c7MmAiKkFZgL-2jztTkf9tallvF6MSK7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/18148" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی در پاسخ به تهدید کاتز برای ترور رهبر جدید ایران:
شرایط تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است.
رئیس‌جمهور آمریکا متعهد شده است که حیوانات خانگی خود را در تل‌آویو ساکت نگه دارد. اگر آنها به ارباب خود توجه نکنند، ایران به آنها درس خواهد داد.
هر تهدیدی علیه مردم و رهبری ما پاسخ فوری و قدرتمندی دریافت خواهد کرد.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18147" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=Rwh2_IP2Gd-wsEebNRzayAgRVGTYEV1I3CVnc1jZOd7VjGpateB_te1YW0C3gCJ6FTYwLbrt3FCSZZs2KVKw0XaX4-ItxADepp8VOzAW893qxRSMx6LrBpRn7_n889msphCco0z5PPAQiJPotRC4-S3b-5LT6VLkhfy1Gip1C9pFEqkqosjf2WpYcGcrCD57FXMZiBgyeNr87IO6mQTb27JFc5iM6KbkceQzZ58oJpTZvhVz3AZRpDF9-EaDuf68bBgSkreHuRFSnTZkluqlnp9Ax4qhEDJ2kC7dg4PoqxOdTSL2YoCVmrW8uBNG0aGehHEkqUAdH7TKfak4Ws-UKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=Rwh2_IP2Gd-wsEebNRzayAgRVGTYEV1I3CVnc1jZOd7VjGpateB_te1YW0C3gCJ6FTYwLbrt3FCSZZs2KVKw0XaX4-ItxADepp8VOzAW893qxRSMx6LrBpRn7_n889msphCco0z5PPAQiJPotRC4-S3b-5LT6VLkhfy1Gip1C9pFEqkqosjf2WpYcGcrCD57FXMZiBgyeNr87IO6mQTb27JFc5iM6KbkceQzZ58oJpTZvhVz3AZRpDF9-EaDuf68bBgSkreHuRFSnTZkluqlnp9Ax4qhEDJ2kC7dg4PoqxOdTSL2YoCVmrW8uBNG0aGehHEkqUAdH7TKfak4Ws-UKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/18146" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محبوبیت فردریش مرز  به پایین‌ترین میزان خود رسیده است!  بنا بر گزارش بیلد و با استناد به داده‌های مؤسسه تحقیقاتی INSA، حدود دو سوم آلمانی‌ها از عملکرد صدر اعظم فریدریش مرز ناراضی هستند.  این رسانه اضافه می‌کند که حدود ۷۰٪ از شهروندان آلمان از عملکرد دولت ناراضی‌اند.…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/18145" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💳
اعتراض عضو فقهای شورای نگهبان به بازشدن اینترنت بین‌الملل
🔹
مدرسی یزدی
:
باز گذاشتن شبکهٔ جهانی اینترنت بدون ملاحظات کارشناسی دقیق از جانب متخصّصان متعهّد، به انواع بهانه‌هایی که نمی‌تواند جبران‌کنندهٔ آسیب‌های همراه آن باشد ـ از قبیل آنکه کسب مردم آسیب می‌بیند یا حقّ مردم است یا خلاف وعدهٔ انتخاباتی رئیس‌جمهور محترم است ـ کاری بسیار خطرناک است. این کار، اقتصاد کشور، امنیّت شغلی مردم، امنیّت داد‌و‌ستد‌های تجاری، امنیّت نهاد‌های مهمّ کشوری و امنیّت شخصیّت‌های مؤثّر نظام و سلامت روانی اقشار مختلف مردم به‌ویژه نوجوانان و جوانان را در تیررس دشمن آمریکایی صهیونی قرار می‌دهد</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/18144" target="_blank">📅 13:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfCpHhrObhxLQZRlmuqP4fafziArzoEfbR7B0T2KKdS4mCkhTFJAEqufkqSP9KMB7clS07O4ylzGzMX5ZprSTMqx1ACCgGaJ4HEDUktbeCbKE4IZpKyggdTFIaJt6-PJkILIblCykwQfS2-QgP5flWHbu24vRBfPLXPrspzfAOYiVFFPJXqr5RQlIwVBRMgCPJqNColTNC1lhe1GRXqgzVbZF6NIDklRIDtcrUDJXzym2uPuU55pWg_XJvAimSe8D-ghruExm3C3mjlEHhtIjRWYeeWGrUQwF1zUB8DNCarKNhApotpZJ0nmxtlk2ub7ll4iFUff0jGjPg_KnSepUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/18142" target="_blank">📅 12:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/18141" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Secret Box
pinned «
🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/18140" target="_blank">📅 11:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه
ژئوپولیتیک و بازارهای مالی
ارائه خواهدشد.
یک
شاخص ریسک ژئوپولیتیکی
هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18139" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go5Kwic6JkHrb6lQ0nsEherc9mJrpCzKFBRA7W1_RKnuW51U4UZMLLPsFGcV0FxE3-kjd89jF8RgXtxNmusqcF7jiJ8TNJHSntNMZw-WL3DXIhjqogvmv4SsuDFMrgeTPYoP5CEM534D2MyPr7RgSco3UFrhy4fYdpwLBGO7TdU4rnbMk28vSG3os46V2SCcLB_yE3bECneohOVi1v91_A4ps6eT2Ts1dtwXrLzTbSxzGzYs-CJ3a07CbZB0ZR8kU3RBV6zDF92U5TQIw86EwvzJ0ZgnS-I8V2kwqG1Sp4HmU2uIMyCpfYCKQFKlY8nJx5VLPOrAOFtwn8sQs6E0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اظهارات جدید قاسمیان:   واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/18138" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اظهارات جدید قاسمیان:
واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18137" target="_blank">📅 10:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmvrdFHVSM5iRplklu1lDPO4Em1wisw6kbeZdjj0wRqbs-WNoJsM5cskuFzGnJKtMfasiGeT1hoelmgVYz-98Grg8H6lqvUpq04uysFoFqkFLbfd7kLrfThmW2uL3NYUIyoRRkBGbSl2c6SMmUKr677XpJirkZSMyzGaYvOjSZeR-9vUlwxD9NeaUOMcLLSJgd3W-NM5UbUnFUqmrlh-bOnfUOfGqz3TJ93K36lhSRMW1bCmOJ6vj1Be07bp0O1JVzw0UdLqcDL29uFj598N1k-lc5Xh6zMF1-hcwpSkdHm4YdnOcxF7hIwTwTB67EjfmnIKB9PRcuCb0wIcP_9BxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/18136" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brb-YRYYRV6JOlJ4sx2F1jh8rYvT3Ai6t3Jy7s_0SJGEhrDN3dE83QhAzYvQLHqeZzDb2UNN0grKewjeEOwXt7S8cE_XP_Wzur_Xa45kUQc-I7OTLoTYLwRgLdefNiteYa6m_0CsBiTPqH-yE80XfBD3Foi2Cm4gMSDSfk4eMoqqbhV3Wx4cXBvtsnaaq9zRTXW5olApbqXHpGlNOzada9DVsRrXUGbGHxb7h4qZHf00n3CnMpF55qEa6XaUdCECbJvefnlTrkz0oNXuKpnfi9Ai5qYzd6VhVPUyY9pPqZKbo6tjgijHSpr-UeXnO79H0800ayOvKA6hfpFf8Gzc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد دو ناو آبی‌ـ‌خاکی آمریکا، باکسر و پورتلند، در حال حرکت به سمت خاورمیانه هستند.
این دو ناو معمولا برای انتقال نیرو و عملیات آبی خاکی و ... مورد استفاده قرار می‌گیرند.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18135" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فراخوان‌هایی برای اسکان مجدد در غزه پس از مصاحبه نتانیاهو
بنیامین نتانیاهو در مصاحبه‌ای با «پاتریوت‌ها»، بازگشت به اسکان یهودیان در غزه را رد نکرد، که این موضوع باعث شد قانون‌گذاران برای تبدیل این چشم‌انداز به واقعیت و اصلاح «ظلم تاریخی» جدایی سال ۲۰۰۵ فراخوان دهند.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18134" target="_blank">📅 09:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18133" target="_blank">📅 09:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=J0ZxgxHDGyy8k_BE18ukskG9gS0JXZY1l01kX_89-jtsiRtRAYa2qCCIuhehl8XMS651AvRuIVKRNLHG8TSWARs9xaa71dYw2wOp2OTg_JmyC65Uq-FYDxm9jHhv_Vhc4qfv4AnOAZgfIOJazRSxWfHeHOzTm_Ul1hejjUpW6uMUedm7LxAfOEN4CTQYwotu0Fclakm7soMf7CzAfT4r4fm1pfla4r3RKjXnPxab5ojvMn79vUbZqNIscnl2T9HKct32z9oaqEGcPxZ-5gDtlrPYX85oMc2qTbF6n-XJg8gB7CYLVgJ1066zqxkvrDqIFAXxZ92ZBwCgDBo7t9W1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=J0ZxgxHDGyy8k_BE18ukskG9gS0JXZY1l01kX_89-jtsiRtRAYa2qCCIuhehl8XMS651AvRuIVKRNLHG8TSWARs9xaa71dYw2wOp2OTg_JmyC65Uq-FYDxm9jHhv_Vhc4qfv4AnOAZgfIOJazRSxWfHeHOzTm_Ul1hejjUpW6uMUedm7LxAfOEN4CTQYwotu0Fclakm7soMf7CzAfT4r4fm1pfla4r3RKjXnPxab5ojvMn79vUbZqNIscnl2T9HKct32z9oaqEGcPxZ-5gDtlrPYX85oMc2qTbF6n-XJg8gB7CYLVgJ1066zqxkvrDqIFAXxZ92ZBwCgDBo7t9W1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد خوش چشم:
«یک چیزی از آقای حاجی زاده بگویم که احدالناسی نمیداند جز خانواده اش
که آنها هم به من نگفتند!»</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18132" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جِی‌دی ونس درباره ایران:  یکی از چیزهایی که درباره ایرانی‌ها برایم هم جذاب است و هم ناامیدکننده، این است که آن‌ها می‌گویند «نه، نه، نه، هیچ گفت‌وگوی صلحی در جریان نیست»، اما گفت‌وگوهای فنی بین ایالات متحده و ایران درباره توافق صلح در حال انجام است.  این یک…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18131" target="_blank">📅 23:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18130" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قالیباف رئیس مجلس ایران:
تحریم‌های نفتی برداشته شده و ما نفت را ۲۰ درصد گران‌تر می‌فروشیم</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18129" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=EzrWdRYKajBMz58HhRvKPK_2qRiRlnLp-E00_p3JfLiqD1qw332wFLArnetFtdy2nDInswDt8R3QF-gW5-VVnL1a78oyeHhv8Srm4LitvcY5Qz_JkkUhp2qCVkDgqGTQZLXKyFSC2KDStX5dheWWjgLxn1Llm_yhFMcWU9ZXocBrAxs44kot7Nf6HwGo9rkyO82wqQx0HEbZegnEd-EvTd6QJtCQM7aeCQ8RJdWA7AexR0J5b7wdsov8tUZs93skc8Y51oOf1M1jyqnKsWqJm79hAkri6h_xAy8iyfgfPWmNXBELI4GSQC4OkPYodxrGT3hIfrIyHureBI5x1lcyHJcbRXVCUPl9zSAhLsjMt1OFC4NY0uYkjBVFQY6nRoQ5XecS0PQ2Ji3lufV-5MMImT2cSIXAuWPrumJN5ATWhNQQXOSl9O-Luk_gPJCIFHgZzaeUDLQDMeKFmE42T-C3XeEl5UPMslTkoDGXbgVdZnoICkUsqymBJ9TNEjR_gsV3AMZ8qBp2W03WwMU6AIOQuY59ipb1Bgt1SWtUuVE7NjVORNu3DHwwEUUlsCYuCLdffB6ltdUmFcqVnRKY0DZj-uEl29ZnGo_bHUa3yJih8YEGQue9ZgvZsuHcu48Thht9pKFh_yjOPt7DssY2czWq8NKum8MhuVaqFmz2umlGnAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=EzrWdRYKajBMz58HhRvKPK_2qRiRlnLp-E00_p3JfLiqD1qw332wFLArnetFtdy2nDInswDt8R3QF-gW5-VVnL1a78oyeHhv8Srm4LitvcY5Qz_JkkUhp2qCVkDgqGTQZLXKyFSC2KDStX5dheWWjgLxn1Llm_yhFMcWU9ZXocBrAxs44kot7Nf6HwGo9rkyO82wqQx0HEbZegnEd-EvTd6QJtCQM7aeCQ8RJdWA7AexR0J5b7wdsov8tUZs93skc8Y51oOf1M1jyqnKsWqJm79hAkri6h_xAy8iyfgfPWmNXBELI4GSQC4OkPYodxrGT3hIfrIyHureBI5x1lcyHJcbRXVCUPl9zSAhLsjMt1OFC4NY0uYkjBVFQY6nRoQ5XecS0PQ2Ji3lufV-5MMImT2cSIXAuWPrumJN5ATWhNQQXOSl9O-Luk_gPJCIFHgZzaeUDLQDMeKFmE42T-C3XeEl5UPMslTkoDGXbgVdZnoICkUsqymBJ9TNEjR_gsV3AMZ8qBp2W03WwMU6AIOQuY59ipb1Bgt1SWtUuVE7NjVORNu3DHwwEUUlsCYuCLdffB6ltdUmFcqVnRKY0DZj-uEl29ZnGo_bHUa3yJih8YEGQue9ZgvZsuHcu48Thht9pKFh_yjOPt7DssY2czWq8NKum8MhuVaqFmz2umlGnAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیریت Secret Box حدود ۲ سال پیش این ایده را مطرح کرد که این روانی عوضی را در قالب یک معامله بکشند که هم برای ایران خوب بود و هم برای اسراییل و اتفاقا ۴ ماه بعد این فراخوان لبیک گفته شد اما سوگمندانه ناموفق بود!  مردک حمال یک دیوانه کامل است و می‌توان او را…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18128" target="_blank">📅 20:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وال استریت ژورنال:
اولویت‌های متضاد ایران مذاکرات صلح آمریکا را به خطر می‌اندازد</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18127" target="_blank">📅 20:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18126">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!
از این جهت خیلی شبیه احمدی نژاد است؛
منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18126" target="_blank">📅 18:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18125">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسپوتینک:  اختلاف با عربستان، جنگ ایران و تله هرمز عواملی که ممکن است امارات متحده عربی را به سمت خروج از اوپک سوق داده باشد  دکتر ممدوح جی. سلامه، اقتصاددان پیشکسوت نفت، به اسپوتنیک گفت: «مدت‌ها قبل از جنگ ایران، امارات متحده عربی به دلیل اختلاف با عربستان…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18125" target="_blank">📅 18:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18124">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بقائی:  ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.  آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18124" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18123">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بقائی:
ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.
آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های مسدودشده ایران با طرف‌های قطری است.
بنابراین تأکید می‌کنم که هیچ دیداری با طرف آمریکایی در هیچ سطحی برای روزهای آینده برنامه‌ریزی نشده است
تمامی مقدمات لازم فراهم شده و امیدواریم این روند به‌درستی پیش برود و به نتیجه‌ای رضایت‌بخش برسد
رقص و ابراز شادی مقام‌های آمریکایی از صعود نکردن ایران به مرحله بعد جام جهانی، با همه معیارها و اصول پذیرفته‌شده میزبانی مغایرت دارد
هیچ درخواست رسمی درباره بازگشایی سفارت کانادا دریافت نکرده‌ایم در صورت دریافت درخواست، آن را بررسی خواهیم کرد، اما تاکنون هیچ درخواستی به دست ما نرسیده است.
﻿</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18123" target="_blank">📅 16:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18122">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM-0hwFdSXEyGb62z3jvEIe8aOJyzDFhSRe_Eq-ZB3JdDP-wmkF2VomE9sffZZQ3VDNYx7tdNFAE95dVJk6f_iEfoE1pTkXusZBjcRvCWOkyJ3fGUOz2HjcPWfokU3pDmp0rL4AxKaAsaLAGZRh0AI0u_9atHGopw_d6mIqVsrBI8nWQsRH6faQlI81plp5p49ZQB-zCTS6Dczcj82gpfpWw-Rq6VmpOGu7xLFQXT9m5m35jQONkMwobANdQt-oTN6UHkDfwBeAyCmkO0uQM1NGo0-KWYsXvCZniY2dzv-8gAJkoSFbiHFHQyK77AUXQO37ZdXAvtrgbIStI6XfKsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.  سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18122" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18121">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.
سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های مسدود شده ایران هنوز منتقل نشده است و آزادسازی آن‌ها به پیشرفت در مذاکرات بستگی دارد.
او همچنین گفت یک خط تماس کاهش تنش به کنترل تبادل‌های هفته گذشته بین آمریکا و ایران کمک کرده و قطر با عمان هماهنگ می‌کند تا عبور ایمن از تنگه هرمز را تضمین کند، که آن را به عنوان اولویت اصلی توصیف کرد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18121" target="_blank">📅 14:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.  در این بیانیه، او از اصطلاح "دموکراسی اجتماعی" به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18120" target="_blank">📅 14:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT3v-tgZ3ZbVbMv_fbYEDGgAxfUXreC6VCn1Bc4u5FNaPtkrw1NKqx9mlwk8wjcKGh5p4wDDuLbNiDqQJpipiuvyQweHnvHq4MlEaB8E3WFlCl9eUVw-CU165MlcfsulyL7udBR_jB8W7D5CjBcWnFAmNwhgPNSOsJTyi6uIa7qJua_pLnblauXK8wLAr4sCFSWPH2M5vR3N9ohvF1cKz3gA59jusA3PT68jodUBFW8zEK_MUSCNRSRgRh9zfXrsmamlWgDaYvjijgqzsc9wpmAJhvRa72ZEShAJAToqSIdLv5VTJREvRS6yWUaa9g4VoZH8df4dKUD7hOMEumc1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.
در این بیانیه، او از اصطلاح
"دموکراسی اجتماعی"
به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد این اظهار نظر علیه جریان‌های سیاسی داخل ایالات متحده هدایت شده است.
طبقه‌بندی کمونیسم به عنوان یک تهدید وجودی، حتی از خطرات کلاسیک امنیت ملی در فرهنگ حافظه آمریکایی نیز فراتر می‌رود.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18119" target="_blank">📅 14:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18118" target="_blank">📅 13:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejhy-K2rtTee6Kq4MtHo-wfMblwfhFpW3UBIRUPzaPfzAueh51vMT7BvME1_8090P5DNOisgN_sDhcDg84ASzfi9ZdcxTCzU4Y5xgxZfZN4FTtG1K5GIUYpqTztI94hdvJwqsYEkNfPJuja0uUPeMzq29MGqsX3jRW3XMMZIhi5ogWLVkEpubdBng-Q5nCd9iBy7_viQB3ct2fQW42KvJH_ToydDucdm0Q1tN7C6G3HtKW8eWMr2RNkpEvArSsqwmWbOWh3aLKfScL6Z7qN_nqyPOc4F-9YlMJACa7slmTCGhtBgkN4HaWAgCua-nNneDyte1tzBRk2wnLM0Iv3G2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18117" target="_blank">📅 13:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
قنبری ؛ سخنران صداوسیما : ترامپ جنایتکار باید ترور شود تا رهبران ما بتوانند از مخفیگاه خارج شوند که اگر چنین نشود آنها باید تا ابد در مخفیگاه بمانند</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18116" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است  یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.  یوسی کارادی،…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18115" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است
یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.
یوسی کارادی، مدیرکل اداره ملی سایبری اسرائیل، به روزنامه آلمانی
دی ولت
گفت که مقامات اسرائیلی در ژوئن ۲۰۲۵ حدود ۱۶۰۰ حادثه سایبری خصمانه را در جریان جنگ علیه ایران ثبت کرده‌اند.
به گفته کارادی، این رقم به طور چشمگیری به حدود ۴۸۰۰ حادثه در ژوئن ۲۰۲۶ افزایش یافته است.
کارادی گفت: «برخی گروه‌ها بسیار ماهر هستند.ما می‌توانیم با آنها مقابله کنیم، اما باید آنها را جدی بگیریم. برخلاف حوزه فیزیکی، در فضای سایبری آتش‌بس وجود ندارد.»
کارادی اظهار داشت که حملات طیف گسترده‌ای از نهادها را هدف قرار داده است، از جمله سیستم‌های زیرساخت حیاتی، سازمان‌های بزرگ، کسب‌وکارهای کوچک و متوسط و شهروندان خصوصی. در میان اهداف کوچک‌تر، شرکت‌های حقوقی و دفاتر حسابداری نیز بودند.
او گفت: «تا کنون — و امیدواریم که اینگونه باقی بماند — ما موفق شده‌ایم حملات به زیرساخت‌های حیاتی را دفع کنیم.»</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18114" target="_blank">📅 12:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سردار محمد اکبرزاده، معاون سیاسی در دفتر نماینده رهبر ایران در نیروی دریایی سپاه، در یک تصادف رانندگی در استان کرمان کشته شد.
اکبرزاده یکی از معماران کلیدی استراتژی ایران در تنگه هرمز محسوب می‌شد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18113" target="_blank">📅 09:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18112" target="_blank">📅 08:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">غریب‌آبادی :   اگر عمان به هر طریقی تمایلی به ایجاد یک رژیم مشترک برای آینده تنگه هرمز نداشته باشد، جمهوری اسلامی ایران این امر را به تنهایی پیش خواهد برد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18111" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:   ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18110" target="_blank">📅 23:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دکتر محمود سریع‌القلم:  دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.  مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.  اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18109" target="_blank">📅 23:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دکتر محمود سریع‌القلم:
دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18108" target="_blank">📅 23:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtPMA2lLA_V0eByUUXsZMBohMsm_3URN3uhmWnvXE4zdSlkVDKhHfQ72o1aGIxUG1sl09MvV_ioZQ_q4MRqR7XZozLJ1ePLTQjZTpeGhppwdtOojMy6wfzkmdKYTlDer3kbeLs4yUYgRTn5aCq6VBNz7wxWHM47cwD1navXPsR-VUZVzr_oBVy7FFipTYsI54A4LvT0TkF_UC2nXIkAM9ZhVupFL1lcNAUwwmiTWz9MhOXsqzIzkuXSwZpi9u9JYoWS8Jlzp1ud2V2xqUuL_sdUqCm-drYmbwN_VmjQD6Ci8lBcnb90ji6I0Gc0dzODFd7N85zSgc_8mAPWaNPogYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18107" target="_blank">📅 21:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18106">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:
ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18106" target="_blank">📅 21:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18105">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مکارم شیرازی در دیدار با پزشکیان:
اگر بدخواهان مانع‌تراشی نکنند، توافقات اخیر می‌تواند آثار مثبتی برای کشور داشته باشد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18105" target="_blank">📅 20:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18104">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVq21yLpTzO6kAs6dQYBR6QwKHoiLpIH9jO8zakKDh_3d5ulrUl8YUFxwANz156L3pcTqOm-w5v4NlFASGMyYUBatKMSFhSngwn2j__CA7iuvbE1Ch5xPT6yIziMwvBk8BtQKqXC6ZQren4uk7StqGikaHQQ2K0kO_Ff3k96yoEZL4dKDD0W8-PCEvlS3MEc7E0fTxtH8Sp4wu-kyeXo4hksJ55JavDaYtxrtHYLWBwj2Rw07jqWdRcAU-duanX0bNKvEB-b4Ei136urEgAo1ordPHwu-v7ibx545nzJXpzeVzYUib5JliyJNWHVyOD21_OGaXK4v0G8OpefHf1Tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18104" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایران می‌گوید برنامه‌ای برای گفت‌وگوهای مستقیم با ایالات متحده در این هفته وجود ندارد، با وجود ادعاهای مقامات آمریکایی.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18103" target="_blank">📅 19:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18102" target="_blank">📅 19:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18101" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
«من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18100" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18099" target="_blank">📅 19:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:
— حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران
— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی
— توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله
— آماده شدن نیروهای مخالف حوثی ها در یمن برای حمله به انصارالله</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18098" target="_blank">📅 19:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18097" target="_blank">📅 18:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18096" target="_blank">📅 18:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18095" target="_blank">📅 18:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18094" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رستم را به زابلستان بازگردانید!  ترامپ گفت ایران درخواست دیدار حضوری در دوحه داده است!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18093" target="_blank">📅 17:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0yNaxkMRIUCWsJrcJ9PmMJNmZicZ1Pl6kyZlTm2qnoSIsYEHZBRx5Ph7ryfsUhMxSoYUFaoU3XbO-XSuIovIVoCB12YUd9ZdzZLI8K-zRctr9nWMztz8Rh23-YZn8CtyeS1YCstF-ZdEZ5Pto9SF85sW5TppWxiFGwJp1cZ5Tn79lPEjxTaT7YrCJjNY2Jmx_i1gRhjL4i2RcLS9bHPZstBpP2UInGSEGVU8AfGu4roi-J1z-W4zULTyC6U5BfvVMmIJZiqYuzQ1nY2zcJCEBydRL4g6T9lOoNDvKKSs70yUGaoEFD3FQc1dE6wRlpnqAWNAOH9MOhleqyJ67gdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طنز بانکداری ایران  به دلیل حملات سایبری به دیتابیس بانک مرکزی شما به پولتان دسترسی ندارید ،اما بانک بابت اقساط به پول شما دسترسی دارد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18092" target="_blank">📅 15:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQqOQPIrtXxtQm2bgGXrOjpjSwo8VSKxQQtqviXBH54-OcU4-K79qqgoSbIVzU-4XZpzoiWUNHksBkfaQCLPWe1SBoWy99TlHT2bvEBP17TMBAt7o56VFahmDULCLZATVW0R-rqTt5JdmkFZpyf5_Sw0DEbwggg6vDvt5DwBeIDc4XxvPRzyhwmFIq9a4hLqkwjoBJiLciJ-gBbyqU0ML2sBFVoTAwtvelw5_060vBelMIf8JIUE7DR7mImh6LkgyA7OPyduNzcxGMCWWJx2NFm2lzUrW9Tg9auxnRtaZLFIxtgKq_O2DgHuUkk3yojru-pnPX6PN_BkbnYUN1bbbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینطور که بویش می آید بایستی بزودی رستم تهمتن را دوباره فراخوان کنیم.  فقط فکر کنم عینکی شده باشد که ولی خب.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18091" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18090" target="_blank">📅 14:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5MzT9yOQ6Wzx4tAMiu28ETBWWuZsU26HxdjusI9vadAngJ3yscMzXtkoRn3gdYLtFNULR8I2OJ-pfW2xN1cdPnTYPLLQUTe2JkE5STyhWDP7zpB31uojMA2h49d3gTm0kQmtUZsdjk0LwxMTztkybBaVnvW7hbna2aSa3NgyoANPSiYbWPbfT-aCK2tuEQWtGSBZ5vff8GIjIXNQ7r4jr3lYC1fVgkxxTea-PD9bWr3WizFPUWqg5FIyze5iw7RrHoiOWmmsZtjjaeNdJPNKpqO4H3M9f19XLiMhJ3bsbN3deVC3CAafzTI_HbYofETiVnCFsFD47SxylbsVJoGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت اسرائیل پهپاد به شهرک نشینان در کرانه باختری اشغالی ارائه می‌دهد!
منابع محلی می‌گویند که پهپادها برای پرواز در ارتفاع پایین بر روی چوپانان و کشاورزان فلسطینی استفاده می‌شوند تا دام‌ها را پراکنده کنند، فلسطینی ها را بترسانند و اطلاعات جمع‌آوری کنند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18089" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18088" target="_blank">📅 13:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18087" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18086" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIa_B0PLU0gkHVCbEbUVdFFuxKO-EQF6l_zeAOyt_f5T1n2XkO7r4wqA0B2R3saTVBFAYkBuhZ8RpVTb-QDP5g47YXxfD9yBVeoHbUa9_qF3KFUQHDAU-lRJ_P1e50zcpyOsP5A93_pWFH1kpl5JRYX4enD9D5lkjWiPuZnwfdpxs3fHsyFpoONcce3iei6jvgC7DaDtNqjb4SmogzItmPNz6txYZe2bB7IoN3ckqPhq8hq8j7tEvh3ZXbd07laPX7qxngUZ-HI1Bh8vOUhbto4JM83_Tb4giXvFJtRDlzkK8xplaZbqvuLNvopWJn6uh19PwdrMLmuv1UXzfibboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا رقابت هوش مصنوعی میان آمریکا و چین این‌قدر سروصدا کرده است؟
رقابت هوش مصنوعی آمریکا و چین فقط رقابت فناوری نیست؛ هم‌زمان رقابت بر سر ارزش بازار، سودآوری، امنیت ملی و برتری ژئوپولیتیکی است و هر جهش جدید می‌تواند انتظارات سرمایه‌گذاران و موازنه قدرت جهانی را تغییر دهد.
مدل‌های ارزان و باز چینی در کنار جنگ تراشه و محدودیت‌های صادراتی آمریکا، معادله اقتصادی هوش مصنوعی را تغییر داده‌اند و ابهام درباره فاصله واقعی دو طرف، به مهم‌ترین سوخت این هیاهوی جهانی تبدیل شده است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18085" target="_blank">📅 11:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRo7gy-mux4ee5ZzYIUDozQsBz9gJI3jlDA7qH1dynQckzey_qRfe-4-euAUPK0FTNn5NCNGbHN_nh_iLWwaPHVi5l78Uyj6RG0iS5BQpG_Cb9e43cZ348c0cdz_TViLV_viCdmasPdd6uU_BUK1FYcN-iDjwtt7utSCEjqQDhNKmU5uUEIkmtfFtZEwPYbP0TQetPNysbh_Uk9aQK8HjInJouQZg4-c1W6bh6HRc0YHG-USxfJfZDlMZxVm5ypdnx2g0mfTrEBnAPrW25CT9mCCBwhoKT8I4VHqlFM3HOC1h5-xlOCYKz2fFpI2SWfiY85tj9St9WfUvhu6X8ft5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عبور کشتی‌ها از تنگه هرمز به طور قابل توجهی با ترافیک سال گذشته متفاوت است.
پورت‌واچ آمار جدیدی درباره ترافیک کشتی‌رانی در تنگه هرمز منتشر کرده است. در ژوئن ۲۰۲۶، ۵۰ نفتکش و ۴۰ کانتینر عبور کردند در حالی که در دسامبر ۲۰۲۵، ۱۱۵۰ نفتکش و ۴۰۰ کانتینر ثبت شده بود.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18084" target="_blank">📅 01:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حمله سنگین اسرائیل به منطقه "مجدل زون" تو جنوب لبنان</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18083" target="_blank">📅 01:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی  ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18082" target="_blank">📅 00:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه  بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.  برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18081" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه
بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.
برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام این ترور را بر عهده نگرفته‌است
چندی پیش یک عنصر چچن با نام مصطفی الروسی از اعضای نیروی ویژه تحریر الشام موسوم به العصائب الحمراء نیز ترور شده‌بود.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18080" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18079" target="_blank">📅 00:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی
ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18078" target="_blank">📅 00:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر علوم و فناوری  اسراییل، گیلا گملیئل:   وقتی که از رژیم ایران عبور کنیم، نوبت به جاه‌طلبی‌های امپراتوری عثمانی می‌رسد که به دنبال گسترش و نفوذ خود است. شکی نیست که ترکیه با آرزوهای گسترش فراتر از مرزهای خود و رهبری منطقه بر اساس دیدگاه خود، تهدید واقعی…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18077" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFIXPpjR9mEuaEJeWzzSkcTwdGR4mKoe5WOdEOJTvizYztO6HUiA56XAKD8rz8ez5LOEhutLNgCjT6aeQDxyCgpkbocR9hYYD4eAAoVy53szDPVjRsDcC6OwNN0kbQmSXNduC89FE-tjIpFxZuiMTJNLNsk5o9fGdTL_a0bZ8KcYrPjshBCK0f7nn3XBcd0pHg71R9twC1nag7DftoZ17ddjBL5Kmb_bBN6XzAjN20v_1kd2ZQkEMdAt2CAbFnFBR-_Al6ld1mBMYKwf7fpz_1-xpLQR5QHe3_IntowBw2hF_yZ_tRnEFgqO-mbVXpDMQs9F3Bm1YWeDiSc20Ia6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا شاخص سهام کره جنوبی در روزهای اخیر ریخت؟
ریزش اخیر کاسپی بیشتر از اینکه نشانه ضعف اقتصاد کره باشد، نتیجه هم‌زمان فشار روی سهام نیمه‌رسانا، نگرانی از تداوم نرخ‌های بالای آمریکا و خروج سرمایه از بازار بود؛ بازاری که وابستگی زیادی به سامسونگ و SK Hynix دارد.
با وجود شدت افت، کاسپی هنوز فاصله زیادی با سناریوی «ترکیدن حباب» دارد و سؤال اصلی بازار این است: آیا چرخه رشد نیمه‌رساناها ادامه پیدا می‌کند یا قیمت‌گذاری این صنعت زودتر از انتظار به سقف رسیده است؟
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18076" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هندی ها جوری هستند که یکی شان میخواسته از بانک پولی بگیرد به او گفته اند برو گواهی فوت خانمت بیاور و نداشته؛ رفته جنازه زنش را از قبر کشیده بیرون کول کرده برده بانک که پولش را بگیرد!  حالا شما فکر کنید بین شمال تنگه که پولی است با جنوب تنگه که صلواتی است کدام…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18075" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن، می‌گوید دولت جدید اسلوونی به رسمیت شناختن فلسطین را لغو کرده و سفارت خود را به اورشلیم منتقل خواهد کرد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18074" target="_blank">📅 14:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بحرین می‌گوید حمله ایران به ساختمان مسکونی آسیب زده است، تلفات جانی نداشته است</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18073" target="_blank">📅 14:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=qgmL-KfqyWuJy7xKNIC5f8NOE2j4aQBrLSqE9uErVmfWFPS99g2166UHaPJ77U-TR3-1P15Ec_L1HN4wT7o_dyXdoaWGEeseQIOF6fZejJBRizvbDYCO6H7Tj_Ed8z2KmUd6v3mT70o2C_aYhyozIesLJBYRkCDmI8P3mMisfxL1_KaEZkAiTul16nRK0SwfgwYwpb2XkPwiouS2I-OvCWW2V7XbWl3YtXnzTvyPpNrFWMa6dfiRK_0L0HIdKHWtMbrArAjABwK2Kt0KEuCqt4O7JvnZSUU4b4O-mqyJFf6I3qHAD17AcQ8PVxHYV5xTXlFsR20tNrFUHL-aDeX7ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=qgmL-KfqyWuJy7xKNIC5f8NOE2j4aQBrLSqE9uErVmfWFPS99g2166UHaPJ77U-TR3-1P15Ec_L1HN4wT7o_dyXdoaWGEeseQIOF6fZejJBRizvbDYCO6H7Tj_Ed8z2KmUd6v3mT70o2C_aYhyozIesLJBYRkCDmI8P3mMisfxL1_KaEZkAiTul16nRK0SwfgwYwpb2XkPwiouS2I-OvCWW2V7XbWl3YtXnzTvyPpNrFWMa6dfiRK_0L0HIdKHWtMbrArAjABwK2Kt0KEuCqt4O7JvnZSUU4b4O-mqyJFf6I3qHAD17AcQ8PVxHYV5xTXlFsR20tNrFUHL-aDeX7ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی نجاسات الجزایری پس از خوردن گل تساوی تیمشان از اتریش که باعث شد تا در مرحله حذفی به اسپانیا نخورند!
بعد پروفسور جمشید خیابانی به عربی از این نکبتها درخواست بازی شرافتمندانه داشت!
حق شما همان گیوتین فرانسوی بود و بس!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18072" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18071" target="_blank">📅 10:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18070" target="_blank">📅 08:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=fyZhpZkmRlB-M8tKKeChtBsbVG-jFi6QQHddnVnsp6DFOxPsb5HFzJVeOVGfZhlNWcivYg_lUgJEnai2yFYcfbTDKC6QU3mTL1WDjDUbWSvgh4LLRKswrdowkVoWNmkPagISSwORsaoreMKUZ8iZBIKBu3jZ5oL_Hdb5XW9iQ0BBPJ4JPFHHPMhcSgqgsUs5uBad6D_2J7Rx4xqyQCtRRmu4egkbV1llNVad4jTFq01PlsAaXUftNmX1oFKCePUwi0xROVQFXLgr2FwlUnl7lXNT4YmfVKqi1L6P3IvU29qd0vVToxfectBVOGVxAfRHWvmp-Ql0syORP2B4K3Vn4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=fyZhpZkmRlB-M8tKKeChtBsbVG-jFi6QQHddnVnsp6DFOxPsb5HFzJVeOVGfZhlNWcivYg_lUgJEnai2yFYcfbTDKC6QU3mTL1WDjDUbWSvgh4LLRKswrdowkVoWNmkPagISSwORsaoreMKUZ8iZBIKBu3jZ5oL_Hdb5XW9iQ0BBPJ4JPFHHPMhcSgqgsUs5uBad6D_2J7Rx4xqyQCtRRmu4egkbV1llNVad4jTFq01PlsAaXUftNmX1oFKCePUwi0xROVQFXLgr2FwlUnl7lXNT4YmfVKqi1L6P3IvU29qd0vVToxfectBVOGVxAfRHWvmp-Ql0syORP2B4K3Vn4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18069" target="_blank">📅 08:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارشگر صداوسیما یک دقیقه قبل از حذف ایران از جام جهانی:
یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18068" target="_blank">📅 08:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شبکه ۳ بعد فوتبال یک روحانی  را آورده او هم آفتابه را گرفته روی همتی که چرا گفتی از دشمن گندم وارد کنیم مگر گندم تراریخته نشنیدی!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18067" target="_blank">📅 07:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وقوع انفجارهای جدید در کویت و بحرین
هم‌زمان با انتشار گزارش‌هایی از وقوع انفجار در بحرین و کویت، وزارت کشور بحرین از فعال شدن آژیرهای هشدار و درخواست از شهروندان و ساکنان برای مراجعه به نزدیک‌ترین مکان امن خبر داد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18066" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عراق عملیات گسترده ای را علیه سیاستمداران عراقی وفادار به ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18065" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18064" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ
:
هواپیما های ایالات متحده بار دیگر ایران را بمباران کردند چرا که بازهم آتش‌بس را نقض کرده بود.
احتمال دارد زمانی برسد که دیگر نتوانیم منطقی باشیم و مجبور باشیم آنچه به صورت بسیار موفق شروع کردیم به صورت نظامی به پایان برسانیم. در این صورت دیگر جمهوری اسلامی ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18063" target="_blank">📅 06:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
فرماندهی نیروی دریایی سپاه:
شلیک‌های کور آمریکا به سیریک معمای اشراف ما بر تنگه را حل نمی‌کند. اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناورها یادآوری می‌کند.
حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.
‎</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18062" target="_blank">📅 06:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18061">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گویا صدای انفجارهایی در بندر لنگه و قشم نیز شنیده شده</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18061" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18060">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بیانیه سنتکام:
«پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی M/V Ever Lovely، به ایران فرصتی داده شد تا توافق آتش‌بس را رعایت کند، اما وقتی نیروهای آن در ساعت ۴:۳۰ صبح به وقت شرقی امروز با پرتاب یک پهپاد یک‌طرفه به کشتی M/T Kiku حمله کردند، این فرصت از میان رفت. این نفتکش پرچم پاناما در حال عبور از نزدیکی تنگه هرمز بود و بیش از ۲ میلیون بشکه نفت خام حمل می‌کرد.
نیروهای فرماندهی مرکزی امروز در پاسخ مستقیم به تداوم تهاجم ایران علیه کشتیرانی تجاری، حملاتی را آغاز کردند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپادها و قابلیت‌های مین‌گذاری را هدف قرار دادند».</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18060" target="_blank">📅 01:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18059">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک منبع نظامی ایرانی به صداوسیما گفت:
«صداهای انفجار شنیده شده مربوط به برخورد چندین پرتابه به برج مخابراتی در سیرک است».</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18059" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18058">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18058" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
