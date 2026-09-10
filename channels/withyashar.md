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
<img src="https://cdn4.telesco.pe/file/tPVn1E0soenCJ3URMz9I4P3xk9ENxS2_WwisrRXleQ6OGEpRhOCP8nwuGFsXkkRyXXdRDwMvJN7brd7sp8aTZLxvPpzZJSlnD_zefN98_3n5frcE2zUHVXgHxTJvZ4zD8RTtuyZM3-p_z2xX9Jvr3sZ_9uBFZy0KA_yAKW-pehZIgv1ede9VO2aAj-S-rIAloE6v6Z3eMPtHuzDOYfwd0IKZzBXp8sYtEF8U_dukQzAabuKhrxrLcPvkiONx0ADXPE8MZxT9151anlbh07rMlmjkorxJ7CTPhp-6ILsAR-XZDy60lmZHrELn5qCqChVSEO_VtflIki4d4uLtGvm7YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILA8ORtPrgXiMxvjym3fc3TLaacL9F6V9N7n4PhxDfO7ufikddCaXZJnSu-_S-W0M168z7-HzCqsJHVzfj9n06DrvrfsBYw6ZQSFmnT31uDmaoKVNGPDVk5kC0OiZUlXWndLhHqpKJz8zdsywFJEepkIgMg6wJWUc0WarIAFsDyKQaBZKKJ4dRVeeJRrPkIs-enoBL8CLyDl6DZ4zbtkvY_cYqybSrjISiTzsJ_t9bUZWrIERqwqqU7X54FiDbFcm3uWGgzbyyv3fYpb8ECMCSoTZ84XBO4kqbZvXUs7X2V8coYu2PwKQzUVuQLP9RNiSbZxVxQajA526hBz3V3J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود جزیره قشم
@WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/22781" target="_blank">📅 14:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2AEn5KYMuKKgfqwbfoPIWn8xhJiItZ1R4g9fxGoIUroLNeiNvJWIMvGp8s_r4BmXXI62XJ5On2c6Krt0OZGOJAAvBQ7crq1I9dXZs-PLahFGhRlA0M4tQLsL8MzhK1V-tqoUhHKGY_3cnZ8guXRsRWijX7eIJ9TV-iMAYY7vno6qG9Py1WzzC17QehbSf_-KPS_6Ap8BgoOmMsn0AlyP8MG8vrPfL5cauLa_jnPeiA2NiHUEhcxrNViOfjTMil6KLDdDkTkjprPn1wtJhfacadiDokR3dxubbmnJJ5Wrgt7ZWilv_uGvdR17RuzZmJOPHwlHZuAVRzHoV3SFHTVgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : اسلامو علیکم یا کوه کلنگ
😂
دقت کنید جاده رو از وسط کوه اول میبینید که میره سمت  کوه دومی
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/22780" target="_blank">📅 14:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بر اساس گزارش‌ها، ایران از فشار محاصره فعلاً دریافت
۱۰ درصد هزینه حمل‌ونقل
از کشتی‌های خارجی که محصولات انرژی را
به ایران می‌آورند یا از ایران خارج می‌کنند
، متوقف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/22779" target="_blank">📅 14:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک شناور گزارش داده است یک قایق تندرو ناشناس به آن نزدیک شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/22778" target="_blank">📅 14:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b971e734.mp4?token=pBTciBP7ZYtgHbOPSXo4XoGht4Rc4VQUk9O6TYgrqWEgFAWTaE8gLUgdqDSnhwLbzU3DeeP1-TLDbuKfYcoGd6CUD4a2B6oDcR-tiLPB_dN-Fe60JSHz-XIe5TJIabGlkDd3SGtg8K1skMPA-7HN_a8mHRviYoMTFM169ZC1Z7OM_Q80RGHlu2-YuI-4n9BoQt6TqxeMbJlL6v9r9aKKZSsF_TMFa4RBuZrOcekxcDjWV49oGHmCwicF-yDmqdi2TFn1fpFrZKY16pEGwiypiqxgKOw2r7f2Sid8TIBlpwyRSF-TLH5n9QuyrBfOofCg4QSN_BSsk-HFJmTpInLpWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b971e734.mp4?token=pBTciBP7ZYtgHbOPSXo4XoGht4Rc4VQUk9O6TYgrqWEgFAWTaE8gLUgdqDSnhwLbzU3DeeP1-TLDbuKfYcoGd6CUD4a2B6oDcR-tiLPB_dN-Fe60JSHz-XIe5TJIabGlkDd3SGtg8K1skMPA-7HN_a8mHRviYoMTFM169ZC1Z7OM_Q80RGHlu2-YuI-4n9BoQt6TqxeMbJlL6v9r9aKKZSsF_TMFa4RBuZrOcekxcDjWV49oGHmCwicF-yDmqdi2TFn1fpFrZKY16pEGwiypiqxgKOw2r7f2Sid8TIBlpwyRSF-TLH5n9QuyrBfOofCg4QSN_BSsk-HFJmTpInLpWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر عراقی ها در مورد مجتبی خامنه‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/22777" target="_blank">📅 14:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7f0cc7fa.mp4?token=T75uEQjC3LWhCBfA9fqUR-mpT4llIdGVFvDnkx9hsut-G4YnjXrGhR2bUu3T27yKmhS2mkF1-m_pLF6YCJ-Luy_ZxSD_JU_DuP9zxF5c-HpyoaPdiWXSZi2SHN2H_hxQHcBNcx_hICrxfUKhCwlSkvgfgmUpgySJM4RE6R2nfsYzqJ_snFvSZqkZf7k3qaLj99LbXkfce3L_ZTqe-R7Ur4AoDSNoZ0RMTEKMLfzqVeGPW3V4nnh6oAsLn63u1x-AkVrhTIGntfZhKlS6V5Db4av2ek570h1_7ME-V3J5LWovtxuz96Af9P3QX9DjcSH1TKFlNVh3CGC9dqwH3r3FcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7f0cc7fa.mp4?token=T75uEQjC3LWhCBfA9fqUR-mpT4llIdGVFvDnkx9hsut-G4YnjXrGhR2bUu3T27yKmhS2mkF1-m_pLF6YCJ-Luy_ZxSD_JU_DuP9zxF5c-HpyoaPdiWXSZi2SHN2H_hxQHcBNcx_hICrxfUKhCwlSkvgfgmUpgySJM4RE6R2nfsYzqJ_snFvSZqkZf7k3qaLj99LbXkfce3L_ZTqe-R7Ur4AoDSNoZ0RMTEKMLfzqVeGPW3V4nnh6oAsLn63u1x-AkVrhTIGntfZhKlS6V5Db4av2ek570h1_7ME-V3J5LWovtxuz96Af9P3QX9DjcSH1TKFlNVh3CGC9dqwH3r3FcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک آمریکایی که نقش سیاهی لشگر را بازی میکند از فصل چهارم در دست ساخت سریال «Special Ops: Lioness» ویدیویی از پشت‌صحنه منتشر کرده که در آن بازیگران با
یونیفرم نیروهای ایرانی
دیده می‌شوند.این یک سریال جاسوسی و نظامی آمریکایی به نویسندگی تیلور شریدان است که داستان عملیات‌های مخفی سازمان سیا و نیروهای ویژه آمریکا را دنبال می‌کند.
فصل دوم
بخش مهمی از داستان را به ایران و تلاش آمریکا برای متوقف‌کردن انتقال دانشمندان هسته‌ای به ایران اختصاص می‌دهد.
فصل سوم
نیز دوباره ایران را وارد خط اصلی داستان کرده و یک مأمور ایرانی در ربوده‌شدن جو، شخصیت اصلی سریال، نقش دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/22776" target="_blank">📅 14:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش ها از وضعیت محمد ناصر العاطفی
وزیر دفاع دولت حوثی‌ها:
«إرم نیوز امارات» و «أحداث العالم
»
گزارش کشته‌شدن محمد ناصر العاطفی را منتشر کردند، و آن را در قالب «گزارش‌ها از کشته‌شدن» آورده ولی تأیید رسمی ارائه نکرده اند.
«یمن شباب»، «المیثاق نیوز» و «أحداث العالم» حمله به جلسه فرماندهان حوثی در البرح و حضور العاطفی را گزارش کرده‌اند، اما مرگ او را با تأیید رسمی یا مستقل قطعی نکرده‌اند. همچنین یک گزارش جدید از
i24NEWS
حتی می‌گوید ارزیابی‌های اسرائیلی احتمال می‌دهند العاطفی
زخمی شده ولی کشته نشده باشد
.
@WarRoom</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/22775" target="_blank">📅 13:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFBqxAVgOXmn3L6fsnxMvXoWW-njfZmKRKX0SIOuRG23H4xnA23KufTZx60TbNuL7cm61cDBeRJNsGxI7pvpsQTWzzEnq4vM4dL5zA8N5l0moIj5hI4gmV4Eo6jbNnvflytwncKgkV5hGmoB3jI5SVOKIuWEIwArClFubfvwoYKUbM3Mz-lF0mdM_hub-EVwJ7gB9uS_Q4dkB6VJtuiGFCQJ0gsnwOTQazH_HsRWN9Z2Fe9kvlbXWhI-k4Yb-duJb5XGnZEs6DXTGJjkS5uLLolZ5zLlciW9VFOD3ZAIn-5X3JU8xEDN8KFJD5KIyFflf6CFGla-hhv3lpkGs8hgLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با بیشتر شدن فقر  در جامعه گوشت گاومیش هندی به سفره ایرانی‌ها وارد شد
@WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/22774" target="_blank">📅 13:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وقتی شما مشغول ساختن عکس‌های دهه هشتاد میلادی و هویت جعلی با هوش مصنوعی بودید، رژیم آخوندی ضد ایرانی با بی‌رحمی به جان
رباط تاریخی سبزوار
افتادند و بخشی از هویت شما را نابود کرد
این کاروانسرای دوره صفوی که در دوران پهلوی محل استقرار اداره امنیه سبزوار بود، و ثبت ملی هم شده بود !
تخریب میراث فرهنگی یعنی تخریب هنر، معماری، تاریخ و بخشی از هویت ایران.
لطفاً به اشتراک بگذارید
@WarRoom
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/22773" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وال‌استریت ژورنال: دولت آمریکا خود را برای یک درگیری طولانی‌تر با ایران آماده می‌کند؛ از جمله با ادامه استقرار نیروها در منطقه و چرخش یگان‌های نظامی و دفاعی. هم‌زمان، طرح‌هایی برای تشدید فشار اقتصادی و منزوی کردن ایران نیز در دولت ترامپ مطرح شده است. بر اساس…</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/22772" target="_blank">📅 11:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وال‌استریت ژورنال: دولت آمریکا خود را برای یک درگیری طولانی‌تر با ایران آماده می‌کند؛ از جمله با ادامه استقرار نیروها در منطقه و چرخش یگان‌های نظامی و دفاعی. هم‌زمان، طرح‌هایی برای تشدید فشار اقتصادی و منزوی کردن ایران نیز در دولت ترامپ مطرح شده است. بر اساس این گزارش، جی‌دی ونس، معاون رئیس‌جمهور، و مارکو روبیو، وزیر خارجه آمریکا، در جلسات خصوصی درباره احتمال طولانی شدن جنگ با ترامپ گفت‌وگو کرده‌اند. نگرانی اصلی آنها این است که ایران بتواند در برابر فشار نظامی، اقتصادی و محاصره دریایی آمریکا مقاومت کند و در نتیجه، پایان سریع جنگ ممکن نباشد؛ به‌طوری‌که در بدترین سناریو، درگیری حتی تا پایان دوره ریاست‌جمهوری ترامپ و در ابتدا ۲۰۲۹ ادامه پیدا کند
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/22770" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ : این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.  گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/22769" target="_blank">📅 11:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جنیفر جیکوبز، خبرنگار CBS: چندین هواپیمای نظامی آمریکا در حملات شبانه به پایگاه هوایی موفق‌السلطی در اردن آسیب دیدند
؛ منابع این موضوع را به من و جیم لاپورتا اعلام کردند. یک فروند A-10 تاندربولت، معروف به وارثاگ، مورد اصابت قرار گرفت و با یک بال مفقود بر جای ماند. حدود هشت فروند F-15 آسیب جزئی دیدند و دوباره وارد خدمت شدند. نیروهای آمریکایی در اردن برای دفاع در برابر حملات ایران، بیش از ۳۰ موشک پاتریوت شلیک کردند. این آسیب‌های شبانه پس از آن رخ داد که آمریکا در واکنش به هدف قرار گرفتن یک ناو نیروی دریایی آمریکا توسط ایران، به پنج نفتکش ایرانی حمله کرد. در پاسخ، سپاه پاسداران انقلاب اسلامی مدعی شد که به هشت نفتکش و دو ناو جنگی، از جمله پایگاه آمریکا در اردن، حمله کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/22768" target="_blank">📅 11:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102d5064ec.mp4?token=HpvBlLCG7eYrDgnBeSgdSve6k2Wk4RcBW3ORznqxe1ZeUOxcp5DKId1RUJq8Z4WphWocLtvuNzn_DdARI-Q1iFZH6vD8pW_bpMWEd3qyqHH4a64w53d4k-KRMXZi1s6y6PWCDN5nM9w1KzUJ5M8zz-9wjnzfrpJUxMFBfvxC0GBf-kopdfqOLTUmjr3ydqaTOUANR87fkpJBOeSfb_o7NvBPdz2jqBzR7lgw1jxV8QLZm8sNh43srLP4sxRdRAa7Ozxz3p4s2oIQniVLCrEoPhIUNTV3YwnUJcpCiUO8-xhUHs5UeOIpE1wi-G7Dbs-LLKyahj8an1IGovilha77-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102d5064ec.mp4?token=HpvBlLCG7eYrDgnBeSgdSve6k2Wk4RcBW3ORznqxe1ZeUOxcp5DKId1RUJq8Z4WphWocLtvuNzn_DdARI-Q1iFZH6vD8pW_bpMWEd3qyqHH4a64w53d4k-KRMXZi1s6y6PWCDN5nM9w1KzUJ5M8zz-9wjnzfrpJUxMFBfvxC0GBf-kopdfqOLTUmjr3ydqaTOUANR87fkpJBOeSfb_o7NvBPdz2jqBzR7lgw1jxV8QLZm8sNh43srLP4sxRdRAa7Ozxz3p4s2oIQniVLCrEoPhIUNTV3YwnUJcpCiUO8-xhUHs5UeOIpE1wi-G7Dbs-LLKyahj8an1IGovilha77-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «فکر می‌کنم باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم.
خانم‌ها و آقایان، اعلامیه‌ای در این‌باره خواهم داشت. آن را تنگه ترامپ خواهیم نامید و مطمئنم رهبری ایران از این موضوع بسیار خوشحال خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/22767" target="_blank">📅 10:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167df781a6.mp4?token=E4NqR3t6uDpx6vLU7kDEpVlaovcAZHhq0Cz8EPx3dc6mZxYtrl6ePmPcR5R98wRi5tOzoCGLlqchxrw-ccvI2BkjLGf-MtGcjbCqsF8Dc8rOAOM7q91NX7vLYQcSgKeFre-a4ZvIi9_v7bfMNU5naF9Z1ezAv8BUtaOjSwEKf6SlIWpk020OiBgJetb7KKLYp1PAWWZZGOY2S62vPdIopiyIsOhAx5Ia4d_07MAZZt5E7AZiEzzz1z74PRaL-yeWlVX0DN3GAzW-4wWsP-OEcaNxKpiQkYBx-_vjcVuKQ34kV-T6_2va5SCvlPpQSqmQ7MozMvcm1r4i0eqsbFX1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167df781a6.mp4?token=E4NqR3t6uDpx6vLU7kDEpVlaovcAZHhq0Cz8EPx3dc6mZxYtrl6ePmPcR5R98wRi5tOzoCGLlqchxrw-ccvI2BkjLGf-MtGcjbCqsF8Dc8rOAOM7q91NX7vLYQcSgKeFre-a4ZvIi9_v7bfMNU5naF9Z1ezAv8BUtaOjSwEKf6SlIWpk020OiBgJetb7KKLYp1PAWWZZGOY2S62vPdIopiyIsOhAx5Ia4d_07MAZZt5E7AZiEzzz1z74PRaL-yeWlVX0DN3GAzW-4wWsP-OEcaNxKpiQkYBx-_vjcVuKQ34kV-T6_2va5SCvlPpQSqmQ7MozMvcm1r4i0eqsbFX1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: «دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای B-2 خود به تأسیسات هسته‌ای آنها حمله نکرده بودیم، آنها همین حالا سلاح هسته‌ای داشتند. اگر آنها سلاح هسته‌ای داشتند، من با رهبر عالی ایران تماس می‌گرفتم و می‌گفتم: «آقای رهبر، حال شما چطور است؟ کاری هست که بتوانیم برای شما انجام دهیم؟» نه اینکه مثل الان، حسابی آنها را بمباران کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/22766" target="_blank">📅 10:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ درباره کوه کلنگ
:
«به لطف
نیروی فضایی آمریکا
، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، محمد العزوری.
می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟ از هزاران مایل دورتر.»
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/22765" target="_blank">📅 10:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اورشلیم پست: گزارش‌هایی از انفجار در جزیره قشم و مناطق جنوبی ایران
اورشلیم پست بامداد امروز گزارش داد صدای انفجار در جزیره قشم شنیده شده و همچنین گزارش‌هایی از اصابت پرتابه‌ها به مناطقی در شهرستان سیریک در جنوب ایران منتشر شده است؛ جزئیات خسارت یا تلفات هنوز مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/22764" target="_blank">📅 10:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یورونیوز: آمریکا عملیات اقتصادی علیه ایران را تشدید کرده است
همزمان با حملات نظامی، واشنگتن فشار اقتصادی علیه تهران را افزایش داده و تحریم‌های جدیدی علیه شرکت‌ها، افراد و شبکه‌های مرتبط با تجارت و حمل‌ونقل ایران اعمال کرده است. یورونیوز این اقدامات را بخشی از تلاش واشنگتن برای منزوی کردن اقتصادی ایران عنوان کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/22763" target="_blank">📅 10:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آسوشیتدپرس: نفت بالای ۱۰۰ دلار باقی ماند
افزایش قیمت نفت ناشی از تشدید جنگ ایران و آمریکا باعث کاهش ارزش بازارهای سهام آسیا شده است. برنت روز گذشته برای نخستین‌بار از ژوئیه از ۱۰۰ دلار عبور کرد و نگرانی درباره تورم و هزینه انرژی در اقتصادهای جهان افزایش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/22762" target="_blank">📅 10:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فاکس‌نیوز: حمله موشکی ایران به پایگاه‌های آمریکا در اردن ناکام ماند
یک مقام آمریکایی به فاکس‌نیوز گفت حمله موشکی ایران به مواضع آمریکا در اردن «بی‌اثر» بوده و تمامی نیروهای آمریکایی مستقر در این کشور سالم هستند. اردن نیز اعلام کرده بود ۱۸ موشک از ۲۰ موشک شلیک‌شده را رهگیری کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/22761" target="_blank">📅 09:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز: تردد کشتی‌ها از تنگه هرمز به ۷ فروند کاهش یافت
دیروز چهارشنبه تنها ۷ کشتی حامل کالا از تنگه هرمز عبور کردند؛ در حالی که میانگین ۱۰روزه ۱۴ کشتی بوده است. از میان این کشتی‌ها، تنها یک نفتکش بسیار بزرگ حامل نزدیک به دو میلیون بشکه نفت خام از تنگه خارج شد و هیچ نفتکش ال‌ان‌جی از تنگه عبور نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/22760" target="_blank">📅 09:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd7646c71.mp4?token=ujDh8gGR2YqZy3EzVgTi54_uz1ZXRoQM-v5dB50xjBxQjYb6hQGi_6v_i9gi1-ocTnSPOSvhDIZxFNYwgDQAosAO9v3OFf4T4auMp3yurfRg4ZC2aUaIOzYVQfUDeFQR8BjXc_b82YrU2kcwxVKjNbUUMmWGtOqCwVC2tszkVgeX9qRTIEWo60veu6rAbrGmZqv27Cd7ZGeE1sFez14z5JexcyIyFOedNTe1RnFnadMVpTn-fAHRAyf64062iInABc1HwWqcZo-WhX7iqSiXiBSDVbq4zbjODxwia-i6XsP1EtK99uyhtmD4HXWXBmtPZOcn2ZLxR0mWTxFsBldhP7-hhYMfMfYtValwxXNFTwAucFJQOVvK7ySCQc10u92e0QPqw3Yb8p_l2QHpq_LSXFCTyCfun8j0Bm0fETKp_2ldkziMfrXahRwEVBxh5y0b15q8N6fpVP1LZclIFso7RZ4uYL-asRnlUV88krqYwcwIPK3wZ_jf6qikykn-A4Wlib6dRcfwmi6GP4qag0TI4_OHY1z2tZ2lnArNW31N9iQKMkBKMDwmhv9WzSntRgzsdZCZAZf-oM0V5Pt70w5qCwj5iRkuJy2mzMTjrQtkJIK-Qs3FV6u-3nSenBPtJia04jmEWHPSD2Tg_Tean3JJG3G3Z4_bPPVZQlgCoZd2SPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd7646c71.mp4?token=ujDh8gGR2YqZy3EzVgTi54_uz1ZXRoQM-v5dB50xjBxQjYb6hQGi_6v_i9gi1-ocTnSPOSvhDIZxFNYwgDQAosAO9v3OFf4T4auMp3yurfRg4ZC2aUaIOzYVQfUDeFQR8BjXc_b82YrU2kcwxVKjNbUUMmWGtOqCwVC2tszkVgeX9qRTIEWo60veu6rAbrGmZqv27Cd7ZGeE1sFez14z5JexcyIyFOedNTe1RnFnadMVpTn-fAHRAyf64062iInABc1HwWqcZo-WhX7iqSiXiBSDVbq4zbjODxwia-i6XsP1EtK99uyhtmD4HXWXBmtPZOcn2ZLxR0mWTxFsBldhP7-hhYMfMfYtValwxXNFTwAucFJQOVvK7ySCQc10u92e0QPqw3Yb8p_l2QHpq_LSXFCTyCfun8j0Bm0fETKp_2ldkziMfrXahRwEVBxh5y0b15q8N6fpVP1LZclIFso7RZ4uYL-asRnlUV88krqYwcwIPK3wZ_jf6qikykn-A4Wlib6dRcfwmi6GP4qag0TI4_OHY1z2tZ2lnArNW31N9iQKMkBKMDwmhv9WzSntRgzsdZCZAZf-oM0V5Pt70w5qCwj5iRkuJy2mzMTjrQtkJIK-Qs3FV6u-3nSenBPtJia04jmEWHPSD2Tg_Tean3JJG3G3Z4_bPPVZQlgCoZd2SPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیوز : ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. منتقدان می‌گویند رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند
جی دی ونس: رئیس جمهور ترامپ می‌خواهد شهروندان را در این ثروت عظیم ناشی از تعرفه ها سهیم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/22759" target="_blank">📅 09:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4bcfd6f9.mp4?token=Q0MXhhjJUZJUliENE-isI2aH5PqZWMzZUVc5OzaX5D2Tk8Jri701C3jVdc8Teu2f4PF3EvJOwkoCFR8cOFsoZ5WfJo5_OSW7ZY-IsJ8O1Vvb3Ufdyc2TmBaeVvGhj6GpDLCdUpUm5A8-O4rZaiKpn4R7rFQ9o0DnF9iESSSvWybIXBNc69Y5PUzpB_3GfDyeRwZzcB2LMUlNX53RGiD5cJNWejpZ38_kfCoCvSjWGA0tOOYIO6d2OKLtpCgaAJLZaBDUAdhY3RgISem9gFuVftdLrr7Q4xZorNXit5EnyQKn-HBeH1aDNVDW4rHoB_tCyDwUzLogxXBWGypFhz3L-GWBZaEQcsVEcPFjd1-z5ONgd4JgJ_fbc2tz-ox4QbgfJdgPdIxgWy-DW8nx1EWkJuDJs1WbyW5uKVInKLK5f58JD4mzZB9HZ_kjJBEHb5dLFihxL_9QM3XVAr16u7LyYR9X1LBpzraJSLZp0dUFpMVJwoP-U6jU7Co4dnHbk-WnTGwTln5L2GbX14Vz5Ems8axqvc7TML4VHnX8PW70I6hAAK05MW68hUU-IsjvxF4hA2-IC01NvH36IACO-wFD-Sjhn_3d9Q7FSnqvCTNGJ6XBiVG64Qi-fGFNOYN9v4k1_VIyXB8OKXmhrShm8GQdymP1My1P4wi14d18sn0Mp1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4bcfd6f9.mp4?token=Q0MXhhjJUZJUliENE-isI2aH5PqZWMzZUVc5OzaX5D2Tk8Jri701C3jVdc8Teu2f4PF3EvJOwkoCFR8cOFsoZ5WfJo5_OSW7ZY-IsJ8O1Vvb3Ufdyc2TmBaeVvGhj6GpDLCdUpUm5A8-O4rZaiKpn4R7rFQ9o0DnF9iESSSvWybIXBNc69Y5PUzpB_3GfDyeRwZzcB2LMUlNX53RGiD5cJNWejpZ38_kfCoCvSjWGA0tOOYIO6d2OKLtpCgaAJLZaBDUAdhY3RgISem9gFuVftdLrr7Q4xZorNXit5EnyQKn-HBeH1aDNVDW4rHoB_tCyDwUzLogxXBWGypFhz3L-GWBZaEQcsVEcPFjd1-z5ONgd4JgJ_fbc2tz-ox4QbgfJdgPdIxgWy-DW8nx1EWkJuDJs1WbyW5uKVInKLK5f58JD4mzZB9HZ_kjJBEHb5dLFihxL_9QM3XVAr16u7LyYR9X1LBpzraJSLZp0dUFpMVJwoP-U6jU7Co4dnHbk-WnTGwTln5L2GbX14Vz5Ems8axqvc7TML4VHnX8PW70I6hAAK05MW68hUU-IsjvxF4hA2-IC01NvH36IACO-wFD-Sjhn_3d9Q7FSnqvCTNGJ6XBiVG64Qi-fGFNOYN9v4k1_VIyXB8OKXmhrShm8GQdymP1My1P4wi14d18sn0Mp1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر جمهوری‌خواهان هم مجلس نمایندگان و هم سنا را پیروز شوند، به‌دلیل موفقیت اقتصادی عظیم ما، به هر شهروند بزرگسال در ایالات متحده
۵۰۰۰ دلار
پرداخت خواهم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/22758" target="_blank">📅 09:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تتر ۲۳۷،۰۰۰تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/22757" target="_blank">📅 09:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22756" target="_blank">📅 04:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSINA</strong></div>
<div class="tg-text">این حروم زاده ها کی میرن رفتم ۵ لیتر بنزین زدم شد ۵۰ تومن
😐
💔</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22755" target="_blank">📅 04:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4a9d76473.mp4?token=MTBAPsDTR-6n_q_aCClY-o6OJEb3MG79U6sQ41x3kStivJy77-qaAaTOOh-b_E1BzWOmjy1WHxCwZAQLVD3VD3Unu0c73POuAWkbQvuY-XYlGpeTnGIbooOo4SLs1YhsboODJo26n6pYrvKlPp9NESomS2kn_WObZ4_0poW1-UH-wBVkgkhSxOaSgg60aZ0js-a2GS3xaxbzvPJ6p4PgjBahm48BTI0fKq5MMZgK2K4kiPAD2EMWwk4gPiUqom0lQnXr_eBYplmcAmmScT9Ow6IsyqP8WKQddeWQWGYjrPiLkQXwLbgk1HsGdvz9RCb-5TWu6Czh6_uRDnn1PD_Ehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4a9d76473.mp4?token=MTBAPsDTR-6n_q_aCClY-o6OJEb3MG79U6sQ41x3kStivJy77-qaAaTOOh-b_E1BzWOmjy1WHxCwZAQLVD3VD3Unu0c73POuAWkbQvuY-XYlGpeTnGIbooOo4SLs1YhsboODJo26n6pYrvKlPp9NESomS2kn_WObZ4_0poW1-UH-wBVkgkhSxOaSgg60aZ0js-a2GS3xaxbzvPJ6p4PgjBahm48BTI0fKq5MMZgK2K4kiPAD2EMWwk4gPiUqom0lQnXr_eBYplmcAmmScT9Ow6IsyqP8WKQddeWQWGYjrPiLkQXwLbgk1HsGdvz9RCb-5TWu6Czh6_uRDnn1PD_Ehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22754" target="_blank">📅 03:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromabas</strong></div>
<div class="tg-text">سلام
یاشار من عصری از خستگی و بی بازاری و کلافگی خوابم برد بازارم نرفتم خداگواه خواب دیدم. مانوک اومد تو خوابم. اصلا بهش فکر نکرده بودم ها. گفت فقط ۱۲روز دیگه صبر کنین</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22753" target="_blank">📅 03:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22752" target="_blank">📅 03:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22751" target="_blank">📅 03:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22750" target="_blank">📅 03:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22749" target="_blank">📅 03:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22748" target="_blank">📅 03:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فنر رو بکشید !</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22747" target="_blank">📅 03:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دارم یه کارای میکنم از قلب واشنگتن دی سی ! تا کی‌تماشا ؟! خودم دست به کار میشم ! در چند روز آینده متوجه میشوید !</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22746" target="_blank">📅 03:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f949e07910.mp4?token=oBjlC2d4vJydIwQxBK5n9g-Zmw5HDywfxyIETqcR3KsapSqPl0zuu-zjlAXyxf9fbMBoPsoy_tTtlyzXK6VrS5C2bEfTIotHTV4Q3dWhsjvArkqd5Cc55xPoFZy1RhBNL6mm5FHYE46EsTT_3jInpr_i2Qc449FVYmLMVDZaK7iXw-3X0lV1HL1CBVtvAADn-X-C2D1pa1jtAK8HmSREzo6Gz7K7BFoCP3Ef37asm9UP1cqlUjCjt-UG5XLZarZdu1JVnEU4_v2XYgiu4DUB5ygZGkwIMqXQqGwqX9p-zRDAEX9hVhC7q7EXO2JsOyT7HXWDfLYO-ZKwdyHzCj3Srw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f949e07910.mp4?token=oBjlC2d4vJydIwQxBK5n9g-Zmw5HDywfxyIETqcR3KsapSqPl0zuu-zjlAXyxf9fbMBoPsoy_tTtlyzXK6VrS5C2bEfTIotHTV4Q3dWhsjvArkqd5Cc55xPoFZy1RhBNL6mm5FHYE46EsTT_3jInpr_i2Qc449FVYmLMVDZaK7iXw-3X0lV1HL1CBVtvAADn-X-C2D1pa1jtAK8HmSREzo6Gz7K7BFoCP3Ef37asm9UP1cqlUjCjt-UG5XLZarZdu1JVnEU4_v2XYgiu4DUB5ygZGkwIMqXQqGwqX9p-zRDAEX9hVhC7q7EXO2JsOyT7HXWDfLYO-ZKwdyHzCj3Srw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه فریدون فروخزاد و مانوک خدابخشیان را ادامه می‌دهم، نه کسی خرج من را می‌دهد، نه از کسی می‌ترسم.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22745" target="_blank">📅 02:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHECFApheHrkHumeQa3lJ-omRl5otfQp4CApIHPJ5WU455GRWz2zb41TNyHbrbkcNeq7OvzRLiDUjr5EVZCB8fGa619CWvxjcVzZgGftrkT7nsHiGG8digcmZYCtpehANlpfdLFoswunwjWYMx8Q7EKlF0Ni4YoaozFVUea-LEnEbo0HCDvzw7qu_JmvOpToEZZWq-wpkEIVgaYvEJe6HhD_4WYPy8vHhKsH-JYTB2JgHxDhpSPiD-ipj4fV1zKe2mOjaccePjcz3RS_vxESE9Wo2I1K3CIy3ZBln4_e0KpDytV0lMHRY7hyKNljVuzGPh6_OqSx8-zvJ6j3IB0p0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت محدودی خلیج فارس حاکی از ، همچنان در جریان بودن عملیات دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22744" target="_blank">📅 02:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22743">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آیت الله بی بی سی دقایقی پیش گزارش انفجار از میناب و سیریک گزارش‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22743" target="_blank">📅 02:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لازم می‌دونم یه چیزی رو کاملاً کلیر و واضح بگم. من، اگر امثالی مثل نادان لینو کس ، بهشت هم برن، من می‌رم جهنم مستقیم. خیالتون راحت باشه.
شما اگه جهنم رو هم انتخاب کنید من با مردمم و میام و بت نمیسازم از چیزی ، لطفاً به من دایرکت ندید که، امیدواریم که تو... تو زرد از آب در نیای. این اعصابم رو به هم می‌ریزه.</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22742" target="_blank">📅 02:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">علت اینکه سنتکام امشب حمله را اعلام نکرده فقط می‌تواند قیمت نفت باشد چون جامپ میزنه
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22741" target="_blank">📅 02:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امشب بخوام نخوام بیدارم
🤣
😌</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22740" target="_blank">📅 02:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مهم اینه که بتونی ولی با مردم باشی وگرنه که عمه جان منم میتونه</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22739" target="_blank">📅 02:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22738">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3484ab8c.mp4?token=dP0ryf7Hv3a_9wKwUhXAfLWRcaAB9BD07S5lwiDSYLWH1kqNZ8udD21oo_0z6cGJJzmN-6TJTt3H3zT9IiIQage83HkZYem1yDWZsY7BS6FxUUOcFRXpq03trl26oWPDmhx89azsmLjpdXU67s492bpl5XdM2ycmtKMAhZk2TYdjVPTWqD7gLi5OqGxqleTt_gDDNsv4xirH5TPJizuYSsj-siZpAxKC-kiBRYxxit2IaqggX-fgK58nnXDrSmu8JeAhVj12YUBiCqHiQ2oV4HBxb-MKZarB1PBIOqs3G4-3_onajV_CP7OofDMRveaCEoOwJm5rvxyEqI16sd_BoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3484ab8c.mp4?token=dP0ryf7Hv3a_9wKwUhXAfLWRcaAB9BD07S5lwiDSYLWH1kqNZ8udD21oo_0z6cGJJzmN-6TJTt3H3zT9IiIQage83HkZYem1yDWZsY7BS6FxUUOcFRXpq03trl26oWPDmhx89azsmLjpdXU67s492bpl5XdM2ycmtKMAhZk2TYdjVPTWqD7gLi5OqGxqleTt_gDDNsv4xirH5TPJizuYSsj-siZpAxKC-kiBRYxxit2IaqggX-fgK58nnXDrSmu8JeAhVj12YUBiCqHiQ2oV4HBxb-MKZarB1PBIOqs3G4-3_onajV_CP7OofDMRveaCEoOwJm5rvxyEqI16sd_BoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22738" target="_blank">📅 01:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">https://www.instagram.com/reel/DdFPOr5xRMu/?comment_id=18007178039969398
کامنت برای ترامپ</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22737" target="_blank">📅 01:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شاید فیلم‌هاش بعدم بذارم. تاریخ ثبت بشه. ولی اگه بگم توی پنت که گم می‌شی دعوتم ، بیست نفر دارن می‌رقصن. من دارم برای خودم یه Grey Goose می‌زنم و اخبار جنگ می‌زنم ، فکر کنم با دمپایی بزنن تو سرم. حتماً مستندش رو بعد از آزادی می‌سازم.</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22736" target="_blank">📅 01:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">منور زدن ، فک کنم آمریکا زده قایق های تند رو رو درو کنن  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22735" target="_blank">📅 01:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZO4ahjTenez1KZiDuU-Xl_TCC-gwTNxhfQhrTsn9ywrHfNAC_flQV9xp6k8ZrOuZ97rYtzfwr9jRxovzGj8wKt2i61KSlV5l4jByi8kB-D3HztHjjcPc3lEwDcCmTB8DwrQwNy2vzS1y6CLxxujHF5HTyLNc-m9eFfbvY-MAn63r4UYh8c5kDXqSaouCBfU62-YKbX0tN8hSwYpAvB5Th6yg9mFla41hOHcBmiVw82Gf8tArNqQGCWe9eJn5iWhVxZPGBDPFa-MUcmhxqXSAQXP0bt8ESxeo13Z__26TmdCQ9wmHUi60uGPcmy9YuHErcw2YVNBoN4hqFGGDRr1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منور زدن ، فک کنم آمریکا زده قایق های تند رو رو درو کنن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22734" target="_blank">📅 01:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نفت یا ریال ؟ پیروز کیست ؟ کی تاب بیشتری داره ؟ نفت ۱۰۱،۲۱ $ و دلار ۲۳۵،۸۸۶ تومان !
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22733" target="_blank">📅 01:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آمریکایی قایق تندرو جمهوری اسلامی را در نزدیکی سلامه هدف قرار داد و در آتش میسوزد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22732" target="_blank">📅 01:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چیزی نیست کابل فلت گوشیت خرابه ( بچه ها بهش نکین که EA-18G Growler بالا سرشه )</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22731" target="_blank">📅 01:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSepehr</strong></div>
<div class="tg-text">یاشار سلام خوبی برادر
نمی دونم چی شد یهو گوشی تو قشم حالت پارازیتی مثل فیلما شد که صفحه بالا پایین میشه
😂
😂</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22730" target="_blank">📅 01:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هواپیما های جنگ الکترونیک آمریکا برای کور کردن رادار های احتمالی پرتیبل وارد عمل شدن درقشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22729" target="_blank">📅 01:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سردار آزمون امروز در استوری صفحه اینستاگرام خود تصویری با پرچم جمهوری اسلامی و یکی کشته‌شدگان مدرسه میناب منتشر کرد.
پس از این روزنامه فرهیختگان نوشت: «مشکلات حضور سردار در تیم ملی برطرف شده و او قرار است در فیفادی پیش‌رو و در ادامه فرایند آماده‌سازی تیم ملی برای رقابت‌های جام ملت‌های آسیا قرار بگیرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22728" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دکل سیریک حتما سر پا شده بوده
😌</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22727" target="_blank">📅 01:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری رژیم ایسنا : چند مکان در سیریک و زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22726" target="_blank">📅 01:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش پرتاب موشک از اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22725" target="_blank">📅 01:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">درگیری‌امشب فک میکنم همه جانبه بشه حزب الله هم پهپاد زدن شمال اسرائیل
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22724" target="_blank">📅 01:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارسالی : یاشار داداش میناب در و پنجره خونه کاملا لرزید و احتمالا کرگان رو زده باشن
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22723" target="_blank">📅 01:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiTbO1ofB6BDtmMWyu-eaNxjPHwH3VRkOmdu-4l1BLlpyXxGm4FkKPqiATyUQGuTmOs2Df7WZE-7n3Zqote628ATVQYOiIq4QezKMNoNplor-cl_SQ6T1sqUrI4cO0FaS4V8y-apjtYaNTtFK9635qRYpFL4lj_nveHezJC7Ax8OKeP1WgkWs34wbNu55H06vwiY6Hvv1847NUfB7h2VJUFuFuJ5I0GfUf8b8js0TGNjy-1a7k_CZwArdNydQz_uU3A3RXQwMOpXBLv-KRKUF09Mi5cRyvairOV9y_2VYJRx_Sa42yLGYT722hjsABhB0agx2Yhh4_rMUgZxX4d9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: یک فروند هواپیمای هشدار زودهنگام و کنترل هوابرد E-3 سنتری نیروی هوایی آمریکا بر فراز خاورمیانه توسط یک فروند سوخت‌رسان KC-135 استراتوتانکر سوخت‌گیری می‌شود. هواپیمای E-3 می‌تواند در منطقه‌ای وسیع، عملیات نیروهای هوایی و زمینی را هماهنگ کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22722" target="_blank">📅 00:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قشم گزارش شده به شرکت کشتی سازی‌هم زدند
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22721" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بچه‌های بندرعباس لطفاً بیشتر گزارش بدین. عکس و فیلم اگه دارین، چیزی هست بفرستین.</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22720" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گویا قرارگاه طولا در قشم هدف حملات سنگینی قرار گرفته.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22719" target="_blank">📅 00:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صدا و سیما قشم رو تایید کرد صدای انفجار از قشم رو تایید کرد مال اونا نبوده
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22718" target="_blank">📅 00:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدای انفجار بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22717" target="_blank">📅 00:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22716">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صدای دو انفجار مهیب گزارش شده که درو پنجره به شدت لرزیده…
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22716" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مردم تاکید دارن که حمله شروع شده و پرتاب نیست !در انتظار تایید میمونم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22715" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صدای پرتاب موشک از قشم
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22714" target="_blank">📅 00:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a5956945.mp4?token=M_u0DSpZeiYllQosJ9PKQrQC3oggGJgXGc8yrwr0nz1zH64VjmgwHakDQqddHrdeb7YJhudf-8W4u02UUiY66Vokz2R7wOBUp4XB87sKwRdus4z8UqDlN6-SBe6MwnwwijR5laaWd3SRP-b9zIXlrk-AQyfm0f8vOYfv2bDf56I0l5OIe76n-eH_WGODRtligpY1rQ4zMS5_4ZxbybanLsGWrLKf6XlPESnQGGEUEagpsQArezwGOq6vHytBGNQv1UAvCbXqOc13wv8Qg3MHmGTlOoRPaZ4rk47IIuK8Ok9i2WYorcrooQwPbjp0OO2X5AovT4_HezrL0aA9AZ9m24WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a5956945.mp4?token=M_u0DSpZeiYllQosJ9PKQrQC3oggGJgXGc8yrwr0nz1zH64VjmgwHakDQqddHrdeb7YJhudf-8W4u02UUiY66Vokz2R7wOBUp4XB87sKwRdus4z8UqDlN6-SBe6MwnwwijR5laaWd3SRP-b9zIXlrk-AQyfm0f8vOYfv2bDf56I0l5OIe76n-eH_WGODRtligpY1rQ4zMS5_4ZxbybanLsGWrLKf6XlPESnQGGEUEagpsQArezwGOq6vHytBGNQv1UAvCbXqOc13wv8Qg3MHmGTlOoRPaZ4rk47IIuK8Ok9i2WYorcrooQwPbjp0OO2X5AovT4_HezrL0aA9AZ9m24WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا: ما معتقد نیستیم که هیچ کشوری بتواند چیزی به ایران بدهد که معادلات یا شرایطی را که شاهد آن هستیم تغییر دهد. در نهایت، آنها همچنان به کشتی‌های دریایی شلیک می‌کنند و وقتی به کشتی‌های ما شلیک می‌کنند، هزینه آن را با از دست دادن نفتکش‌هایشان می‌پردازند. آنها به کشتی‌های ما اصابت نمی‌کنند، اما پنج نفتکش خود را از دست می‌دهند. دیشب هم پنج نفتکش دیگر را از دست دادند؛ چهار نفتکش آسیب دیدند و یکی غرق شد. آنها به دلیل این کار همچنان
هزینه‌اش را پرداخت خواهند کرد
و ما نیز به اعمال فشار اقتصادی و خفه کردن اقتصاد آنها ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22713" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نخست‌وزیر نروژ: به هواپیمای زلنسکی حملۀ پهپادی شد
هواپیمای زلنسکی هنگام برخاستن از مولداوی به ‌سمت نروژ، هدف حملۀ پهپادی قرار گرفت و تا آستانۀ برخورد با یک پهپاد پیش رفت.
مقامات اوکراینی هنوز دراین‌باره اظهارنظر نکرده‌اند.
@WarRoom
یاشار : برخوردی صورت نگرفته</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22712" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@WarRoom
???!!</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22711" target="_blank">📅 23:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش صدای انفجار/پرتاب در‌ سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22710" target="_blank">📅 23:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فایننشال تایمز: ایران برای دور زدن تحریم‌ها به رمزارز روی آورده است؛ نزدیک به ۱۰ میلیارد دلار رمزارز در سال ۲۰۲۵ از مسیر ایران جابه‌جا شده است. همچنین ایران طی سال‌های گذشته از طریق استخراج بیت‌کوین نیز به درآمد رمزارزی دست یافته و برآوردها نشان می‌دهد حدود ۴.۵ درصد از کل استخراج بیت‌کوین جهان در ایران انجام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22709" target="_blank">📅 23:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ :
این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.
گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها را بکشید، اگر در هر نقطه‌ای از زمین آمریکایی‌ها را تهدید کنید،
ما بدون عذرخواهی و بدون تردید به سراغتان خواهیم آمد و شما را خواهیم کشت.
ما این جنگ را آغاز نکردیم، اما تحت ریاست‌جمهوری ترامپ،
آن را به پایان خواهیم رساند.
جنگ آنها علیه آمریکایی‌ها، به انتقام ما تبدیل شده است.
ترامپ :
ای مردم سربلند ایران، ساعت آزادی شما فرا رسیده است.
زیرا ما آماده‌ایم دولت شما را به دست بگیریم.
این حکومت متعلق به شما خواهد بود که آن را به دست بگیرید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22708" target="_blank">📅 23:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نوش…
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22707" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: [ایرانی‌ها] تمام تلاششان را می‌کنند تا روی نتیجه انتخابات ما اثر بگذارند، به این امید که یک گروه ضعیف روی کار بیاید تا کاری به کار آن‌ها نداشته باشد و بگذارد به سلاح هسته‌ای برسند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22706" target="_blank">📅 22:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjn6k5ZfjLBf0KwZUpd4_whwgdHQpH8A5ZTHjHjrqRTN56u1xZzZDFVWLQhcufHb12vtp3jAj01EyKYF4B2wcLV5lZvEc9TMnzYvEj9R5G2TjolG84SFztHlhFQ2_hApt5rfqxL-YsNtdvL5-CDUxYrw4GG6hG_anP9rlOxPr71E8kZbIi-a7l6Dl8FVukLsertN7HedM4servfV19P8ZFwYhlCH6QswcDtJCheFfQ2ujIDPx3lWEsNIihnzDKvOgR4HCBIHtelos5HlzOXgwsZUZfnHDdmaotZZzolFsnXS15gVgyUCf6m4YwOgOoD28qJJUbNaVAXsUR0rzjWnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید سفارت ایران :
سرآشپز رضا در حال پخت و پز است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22705" target="_blank">📅 22:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b54a836c4.mp4?token=CdtUsafjDV_elrrFYfmSpaT4QoVDVeFg8nHyTXFjyqpcWu2bNipDGAIzCQNnx4S14m8gyejGoA-F-ZYvpWjhbZhnm8xLrekS_9SySPQmSD221QYCHguMTJsm2NqfKsxB9T36WQJZ7Pn6Zz5nfJ-RVjGPOhHkYObk7aHUqSWxsREzjXPl6xyYUydabZe_5GRKQSWRCh5lUkKccKjoN7UmRRG32amu38DHfKV5yRPlx-Rb9cGbeDb1jvtYG_3f9FE0hsC8X8IYl9oJ2USI4aZc1P8vg0xKSUAQaYz1YcqSuCR_K-ARZ9lX_1xK5B2gk8vMXKwtgaYo12jJ-UP6gmNgiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b54a836c4.mp4?token=CdtUsafjDV_elrrFYfmSpaT4QoVDVeFg8nHyTXFjyqpcWu2bNipDGAIzCQNnx4S14m8gyejGoA-F-ZYvpWjhbZhnm8xLrekS_9SySPQmSD221QYCHguMTJsm2NqfKsxB9T36WQJZ7Pn6Zz5nfJ-RVjGPOhHkYObk7aHUqSWxsREzjXPl6xyYUydabZe_5GRKQSWRCh5lUkKccKjoN7UmRRG32amu38DHfKV5yRPlx-Rb9cGbeDb1jvtYG_3f9FE0hsC8X8IYl9oJ2USI4aZc1P8vg0xKSUAQaYz1YcqSuCR_K-ARZ9lX_1xK5B2gk8vMXKwtgaYo12jJ-UP6gmNgiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: ما شاهد حملات زیادی در تنگه هرمز بوده‌ایم.
ترامپ: ۹ نفتکش ایران را نابود کردیم
این حملات توسط ما انجام می‌شوند. شما شاهد حملات بسیار بیشتری خواهید بود
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22704" target="_blank">📅 22:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: چیز زیادی از کشور آن‌ها [ایران]باقی نمانده است. احتمال مذاکره وجود دارد، اما ما به دنبال آن نیستیم. جنگ پس از انتخابات میان‌دوره‌ای ایالات متحده پایان خواهد یافت.
وضعیت ایران بسیار وخیم است. کشورشان در حال حاضر درهم‌شکسته و نابسامان است؛ تورم ۳۰۰ درصدی دارند، ارزش پولشان از بین رفته و حتی حقوق سربازانشان را هم نمی‌پردازند. ما کنترل تنگه [هرمز] و بسیاری موارد دیگر را در دست داریم.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22703" target="_blank">📅 22:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ درباره ایران: «ما به دنبال توافق نیستیم. من در حال انجام کاری بسیار فراتر از یک توافق هسته‌ای هستم؛ مسائل زیادی روی میز قرار دارد.» ترامپ همچنین گفت جنگ با ایران «بلافاصله پس از انتخابات» پایان خواهد یافت @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22702" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره ایران: «ما به دنبال توافق نیستیم. من در حال انجام کاری بسیار فراتر از یک توافق هسته‌ای هستم؛ مسائل زیادی روی میز قرار دارد.»
ترامپ همچنین گفت
جنگ با ایران «بلافاصله پس از انتخابات» پایان خواهد یافت
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22701" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ درباره اوکراین: ما گفت‌وگوی بسیار خوبی با پوتین داشتیم. او می‌خواهد به توافق برسد. اگر زلنسکی هم بخواهد به توافق برسد، خیلی خوب خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22700" target="_blank">📅 22:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22699">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرنگار: شما گفته بودید قیمت نفت و گاز کاهش پیدا خواهد کرد. اما قیمت نفت دوباره به بالای ۱۰۰ دلار رسیده است. این موضوع را چگونه برای مردم آمریکا توضیح می‌دهید؟ ترامپ: توضیحش برای مردم آمریکا خیلی ساده است؛ فقط کافی است بگویید: آیا اجازه می‌دهید ایران به سلاح…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22699" target="_blank">📅 22:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e04575e679.mp4?token=v9pNNqZyxRJrz2vizjiUiJS0_D0kychylOH6epbzRefC2w7mJnD5t4rkskjOngspanoKmYy1TUGKgCwuBzd7GxIkq3nZ76OfSf72Os3pT6eogQQWfrtV3IU-a4vUMwFwZS_0OCJWFs4HEAH62NFic1n7pWXlFDFVPuJmGNXXsQstTc9vrIRRnhXrbwF4AvzZ4HZdVmtICnzEvtLFWeVWcIK2Emual6UmfjBdzKHg5EpfbaPrw_VD_TvJjaNlf9hOmWhKnMifnJyTxz5pN_ecOwt-tVWXc6HwXfwh9r3vOfx_eyfEqPXaq_RTy-hReiZjdRMzrtgD251eN8L4vWp2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e04575e679.mp4?token=v9pNNqZyxRJrz2vizjiUiJS0_D0kychylOH6epbzRefC2w7mJnD5t4rkskjOngspanoKmYy1TUGKgCwuBzd7GxIkq3nZ76OfSf72Os3pT6eogQQWfrtV3IU-a4vUMwFwZS_0OCJWFs4HEAH62NFic1n7pWXlFDFVPuJmGNXXsQstTc9vrIRRnhXrbwF4AvzZ4HZdVmtICnzEvtLFWeVWcIK2Emual6UmfjBdzKHg5EpfbaPrw_VD_TvJjaNlf9hOmWhKnMifnJyTxz5pN_ecOwt-tVWXc6HwXfwh9r3vOfx_eyfEqPXaq_RTy-hReiZjdRMzrtgD251eN8L4vWp2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید قیمت نفت و گاز کاهش پیدا خواهد کرد. اما قیمت نفت دوباره به بالای ۱۰۰ دلار رسیده است. این موضوع را چگونه برای مردم آمریکا توضیح می‌دهید؟
ترامپ: توضیحش برای مردم آمریکا خیلی ساده است؛ فقط کافی است بگویید: آیا اجازه می‌دهید ایران به سلاح هسته‌ای دست پیدا کند؟ پاسخ «نه» است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22698" target="_blank">📅 22:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8e57fc1.mp4?token=WW_Zvr5c3ScWZwTSRUnmDGgkPiGunPYxE6CqMx2mgGG2u9PuHBDSQn4ywafcOy3R12jlXDMLcaJ96yJLOCZC7Spqbq1XOB1meZRwDaTczY7anAKsuZMwNGwQAILe9yKGemePHaYrJTCZk1D8ebAHyA6qWCWxFefNYJbR_2gevI-siPs1wWjSpb7YLFt13qgBHHxPU0PRpul5mNXjhC1UrdaaulyZ4covk87zkNzz1dWt9LhI9rrIBgOUoP4tRHAuz3RZgZ-EceBolkse3Ipy0o_0uyRmD1tCRDdAyTpfwDOQd6YQhIxMVuHHi7z0toNE4a7rcA8oH2cq-cv1gSp2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8e57fc1.mp4?token=WW_Zvr5c3ScWZwTSRUnmDGgkPiGunPYxE6CqMx2mgGG2u9PuHBDSQn4ywafcOy3R12jlXDMLcaJ96yJLOCZC7Spqbq1XOB1meZRwDaTczY7anAKsuZMwNGwQAILe9yKGemePHaYrJTCZk1D8ebAHyA6qWCWxFefNYJbR_2gevI-siPs1wWjSpb7YLFt13qgBHHxPU0PRpul5mNXjhC1UrdaaulyZ4covk87zkNzz1dWt9LhI9rrIBgOUoP4tRHAuz3RZgZ-EceBolkse3Ipy0o_0uyRmD1tCRDdAyTpfwDOQd6YQhIxMVuHHi7z0toNE4a7rcA8oH2cq-cv1gSp2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیفون تاشو و سنت‌شکن اپل با نام دوو «Duo» رونمایی شد. شروع قیمت از دو هزار دلار تا سه هزار دلار بسته به گیگ ، امکاناتی همانند استفاده از دو آیفون به شما میدهد. میتوانید چند اپلیکیشن را همزمان باز کنید و … تاریخ عرضه یکم آبان.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22697" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال۱۲ اسرائیل : اسرائیل تصمیم گرفته است که به هر حمله موشکی جمهوری اسلامی حتی اگر به اشتباه از مرزهای اردن عبور کند، پاسخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22696" target="_blank">📅 21:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22695">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دلار ۲۳۵،۲۰۰ (سقف تاریخی)
تتر ۲۳۴،۴۰۰(سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22695" target="_blank">📅 21:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هم اکنون برگزاری جلسه اضطراری در کاخ سفید درباره ایران
به گفته خبرنگار ارشد کاخ سفید:
ترامپ در اتاق جنگ کاخ سفید حضور دارد و دیرتر از موعد مقرر به سمت دالاس، ایالت تگزاس، حرکت خواهد کرد، به گزارش‌ها، ترامپ در حال حاضر در حال دریافت گزارش‌های اطلاعاتی درباره ایران است و وزیر جنگ و رئیس ستاد کل ارتش آمریکا نیز وارد جلسه اضطراری با ترامپ شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22694" target="_blank">📅 21:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بنیاد دفاع از دموکراسی‌ها FDD
:
ایران پریشب با سه پهپاد یکی از اردوگاه‌های حزب «کومله زحمتکشان کردستان» در منطقه سورداش، استان سلیمانیه عراق، حمله کرد. در این حمله کسی کشته یا زخمی نشد، اما به یکی از ساختمان‌ها آسیب وارد شد. کومله اعلام کرده از آغاز درگیری ایران و آمریکا، مقرها و اردوگاه‌هایش بیش از
۱۰۸ بار
هدف موشک و پهپاد قرار گرفته‌اند؛ حزب دموکرات کردستان ایران نیز از
۱۵۵ حمله
و بیش از
۳۰ کشته
خبر داده است. این حملات در حالی ادامه دارد که آمریکا در حال خروج نیروهای خود از عراق است و بغداد اعلام کرده تا
۳۰ سپتامبر
نیروهای ائتلاف و سامانه‌های پدافندی آمریکا از عراق خارج خواهند شد. هم‌زمان عراق برای خلع سلاح گروه‌های مسلح مورد حمایت ایران مذاکره می‌کند، اما برخی از این گروه‌ها با خلع سلاح کامل مخالفت کرده‌اند. در صورت خروج آمریکا و ادامه حملات ایران می‌تواند
شکاف امنیتی گسترده‌تری در اقلیم کردستان و منطقه ایجاد کند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22693" target="_blank">📅 20:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش صدای انفجار جاسک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22692" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بلومبرگ به نقل از یک مقام ارشد ایرانی گزارش داد تهران در صورت ادامه حملات آمریکا به خاک و زیرساخت‌های ایران،
پاسخ خود را تشدید خواهد کرد
و برای یک درگیری طولانی‌تر آماده است.
این مقام گفت ایران با وجود فشارهای اقتصادی فزاینده، محاصره دریایی آمریکا و حملات به نفتکش‌های ایرانی،
قصد عقب‌نشینی ندارد
و درگیری کنونی را تهدیدی موجودیتی برای جمهوری اسلامی می‌داند. به گفته او، ایران از زمان پایان شدیدترین مرحله جنگ در ماه آوریل، در حال
بازسازی توان نظامی خود
بوده و خود را برای ادامه یک جنگ فرسایشی آماده کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22691" target="_blank">📅 20:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به شورای امنیت ارجاع داد
شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22690" target="_blank">📅 20:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بیانیه مشترک ایران، روسیه و چین:  از اعضای شورای حکام آژانس اتمی می‌خواهیم به پیش‌نویس قطعنامه آمریکایی-اروپایی رأی ندهند @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22689" target="_blank">📅 20:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بیانیه مشترک ایران، روسیه و چین:
از اعضای شورای حکام آژانس اتمی می‌خواهیم به پیش‌نویس قطعنامه آمریکایی-اروپایی رأی ندهند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22688" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گویا جاسک دوبار نفتکش زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22687" target="_blank">📅 19:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش صدای انفجار جاسک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22686" target="_blank">📅 19:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaYQTGo8vpmKUOCd02GiHyCOHaVfrcU6fx9B2jKZb_4GAonAO7VpgjY5tNJnU-1UFDkszqrsnDPozqU0UYugThInBcW8XdwvgNwzUbz_fQMEBdRojoGRjiXGOni81wHrXfMxD73iReWFF_y2pq8BpiMZstJZTApI9kby_7o3vBvxk_bTTxtVTovLBujKhMpZaL67BjrhOOblic6hQD6cFqpCpaf7YR2M-pqY7HWxERZDlcSJ2W2QwR_3VB4mmtlR4UkxETTgMosWBw4dl4ChZ8o1CnqAD3fUud38BkkGeQIrg2rXAfvFTIJqo8_rqEsaINfiKC5A0qNdAY9ZxCINuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : شهپادی که سپاه چندین سال به دنبالش بود و یک بار ۴ سال پیش اقدام به سرقت کرد ولی ناموفق ماند، توسط دیدبان اتاق جنگ شکار شد.
این یک شناور سطحیِ بدون‌سرنشین از نوع «Saildrone Explorer» است که شرکت آمریکایی سیل‌درون آن را طراحی و تولید کرده است. این شناور حدود ۷ متر طول دارد و با استفاده از یک بالِ سختِ بادبانی حرکت می‌کند؛ انرژی دوربین‌ها، حسگرها، سامانه ناوبری و ارتباطات ماهواره‌ای آن نیز از پنل‌های خورشیدی روی عرشه تأمین می‌شود. سیلدرون اکسپلورر برای مأموریت‌های طولانی‌مدت طراحی شده و می‌تواند ماه‌ها بدون خدمه در دریا باقی بماند. این شناور به دوربین، رادار، حسگرهای هواشناسی و اقیانوس‌شناسی، تجهیزات پایش سطح و زیر سطح آب و سامانه کنترل از راه دور مجهز است و داده‌ها و تصاویر را از طریق ارتباطات ماهواره‌ای به مرکز فرماندهی ارسال می‌کند. ناوگان پنجم آمریکا از سال ۲۰۲۲ استفاده از این شناورها را در خلیج فارس آغاز کرد؛ مأموریت اعلامی آن‌ها افزایش آگاهی دریایی، پایش تردد شناورها، جمع‌آوری اطلاعات محیطی و شناسایی فعالیت‌های دریایی در منطقه است. این شناور پیش‌تر نیز در خلیج فارس خبرساز شده بود؛ آمریکا اعلام کرد در
۲۹ اوت ۲۰۲۲، شناور پشتیبانی «شهید بازیار» متعلق به نیروی دریایی سپاه به یک فروند Saildrone Explorer متصل شد و آن را یدک کشید. طبق روایت آمریکا، پس از نزدیک‌شدن شناور و بالگردهای آمریکایی و چند ساعت پیگیری، طناب یدک‌کشی جدا شد و شناور بدون‌سرنشین رها شد؛ حادثه بدون درگیری نظامی پایان یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22684" target="_blank">📅 19:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیدبان اتاق جنگ وسط تنگه هرمز شکار کرده
🤣
خبر تا دقایقی دیگر ….
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22683" target="_blank">📅 18:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آکسیوس گزارش داده بسیاری از جمهوری‌خواهان و دستیاران کاخ سفید، با وجود تردید فزاینده درباره تصمیم‌های سیاسی ترامپ، عملاً از تلاش برای تغییر نظر او دست کشیده‌اند و ترجیح می‌دهند از خواسته‌هایش پیروی کنند. یک مشاور قدیمی گفته است: «چرا زحمت بکشیم؟ رئیس اوست.» با نزدیک شدن به انتخابات میان‌دوره‌ای، نگرانی جمهوری‌خواهان از رویارویی با ترامپ بیشتر شده است؛ یک اهداکننده جمهوری‌خواه این وضعیت را چنین خلاصه کرده: «هرچه بخواهد، به دست می‌آورد.» در همین حال، نزدیکان ترامپ معتقدند نباید منتظر کاهش نفوذ او بود و هشدار داده‌اند که
حتی پس از پایان دوره ریاست‌جمهوری‌اش، ترامپ همچنان یک شخصیت سیاسی غالب باقی خواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22682" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو: در آستانه سال نو یهودی «روش هشانا» در ارتفاعات جبل‌الشیخ هستیم. پایینِ سرِ ما دمشق قرار دارد، اینجا لبنان است و آنجا بلندی‌های جولان. ما بر تمام این منطقه، از جبل‌الشیخ تا رود یرموک و از اینجا تا دریای مدیترانه، کنترل داریم؛ این سطح از کنترل کامل، بی‌سابقه است. این یکی از دستاوردهای بزرگ ماست. هنوز کارهایی باقی مانده است؛
مأموریت اصلی، شکست دادن جمهوری اسلامی در ایران است و ما به آن بسیار نزدیک شده‌ایم
. ما می‌دانیم که در نهایت تمام محور سقوط خواهد کرد. ما برای انجام این کار متعهد هستیم و آن را انجام خواهیم داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22681" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز گزارش داد نفتکش سوخت‌رسان «Hercules Star» با پرچم جبل‌الطارق، در فاصله حدود ۱۷ مایل دریایی شمال‌غربی بندر میناء صقر در رأس‌الخیمه هدف یک پرتابه قرار گرفت و دچار آتش‌سوزی شد. آتش‌سوزی مهار شد و نفتکش سپس به لنگرگاه دبی بازگشت؛ خدمه این کشتی سالم گزارش شدند.
همچنین گزارش شده است که نفتکش «MKD Vyom» در آب‌های نزدیک عمان هدف قرار گرفت و
یک خدمه آن کشته شد
.
@WarRoom
یاشار : در خبر رویترز «یک کشته» مربوط به MKD Vyom است و نه هرکولس استار،  در تمام رسانه ها به اشتباه منعکس شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22680" target="_blank">📅 16:54 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
