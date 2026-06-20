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
<img src="https://cdn4.telesco.pe/file/VKu9A8sneObxPkHUzJ-kWjwrk8uFxltL1gYWfVlv8Hvfat8EetXMgHu6rq_d30OMSeNsDFjDKeHcREfoh0Oo6xmw2_SA1-tpNauuoN_QwbZRGWiuzA4524T8fbMgNGA2IPk8w7i8Jr2M4vuzSnVooLR519ErL1hc6AJamMqL5Bk6ZP1ArED64DotO2v1KY5FcmBx6XXRzNbhp_t-tPs1CbwGs8-M6lxPY7N8XYK-5-aUTnO71njNNqangil5CNRdupWDles2wBRuCN7f5M1p_kqkYSK15unpYqYse01P5iHd8MfHDleXSChci2VT7UAe4S_Ng9W5HG02EtDeMxwSTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 11:47:27</div>
<hr>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=TmUHU5Ufy0a0PS4DW4YZUe30DHMKxL_WC6phW0sbKx_393eY5kfWGGUUBicfXPIrAmkOD9QQNkxIJZfd2sh4YdGiv7YITr2IZ0uJ9E1kzaorbZOvX5v6mXBgxBObujDEoNRZi7I11jU5f3UqFjkJh_1ybJSA_fQ5mg2qu79GcioGH9yTKDJ69GJx1Kb0CYy6T7JIEVzBdL34dm6U-ipILPtV-o3xg9wzO-9eE6WUCMPqU2uQYNVvcaHy35W6i3Li9KK3NxeXJE7L-KtzV2bKjoL05kciJ7RDzlM4CAfr9OuH_-4m3bMHKGJvv3FlspT5LN3lI4G3qqlQt53LCmhJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=TmUHU5Ufy0a0PS4DW4YZUe30DHMKxL_WC6phW0sbKx_393eY5kfWGGUUBicfXPIrAmkOD9QQNkxIJZfd2sh4YdGiv7YITr2IZ0uJ9E1kzaorbZOvX5v6mXBgxBObujDEoNRZi7I11jU5f3UqFjkJh_1ybJSA_fQ5mg2qu79GcioGH9yTKDJ69GJx1Kb0CYy6T7JIEVzBdL34dm6U-ipILPtV-o3xg9wzO-9eE6WUCMPqU2uQYNVvcaHy35W6i3Li9KK3NxeXJE7L-KtzV2bKjoL05kciJ7RDzlM4CAfr9OuH_-4m3bMHKGJvv3FlspT5LN3lI4G3qqlQt53LCmhJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCezbkVznLfF59wNkpVbjttrUaJpUYgn31fcwYnOLHMRLWQGY490cr7JWSpgymenxM6fIQoT7Pq_qvhHf6KSHpz-OEF4AIUiRPjnWGgfQFwNknc2G5EX9OF32dE6qq8jWBh58s_OlulWdrrhj7Z--RDfkkEGs0MqZAeuolfLMAxXFZtGCJ5vJO3ZLMnbvDNCg2SMh-UlDe6-WZG4nHdwnyw-0eNNHiZ9f1drABNVVEQlgFVsLUu9gGvLY9tzsM4JElKvaWb4CAfpe8QQVnddZoyPxPCJ0usRmH3UBUlrYbAfsKGnrT4N6LGHr9qNBhCzJQOa3Gdd8JTwsLov7wmfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGraSaI-9Fcst90tlBJaTvqEfl5EUyvhzphcvR1QKQCDH6Xqg-FYM68BnMbEK-zhY93x2Qg4xFJFmNNzsY7vahoOzKZryibyY2XLTmMnNAiyPuRVTZEx9Z0_Ij7BSd61f_seH4IOXneExisd0G7ub4F3P4Po3tzNSquZflsGwT0qv9mZ9zxgHUkR18rbLWwmQJvbaNVA3KJ6MSbsoFgc63jnSSUPoqWCpQwt1Aphj8L_BuDur_TFND6k-ADSQktoO2zxPWbY7lZ1kugckFdKMZZrewlXrgFvgP8oNJTm9XTdwHa13DJV6dqpCh_gpN9Git5yhQanyAoK1LX1BA47jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=suTqBHsNFIm3cOXVb6uIVGQh2kMcoWnen2b0xtYMeoNVV5FGutgbu0ftEzLbsJM25dtrZfS6hJQX5g_IJsegil-4qzU2oWvePcPUKmVZZ8Hx2-PlxIdq1L4PveVYzbgSJMa7tIz1w2dz_bFwerPssh-0IZ7ODzzKiAsb5G6sI_iNarWy8KtWnRnCssDuUyfJ4EWfl5fJ5A7VMKZoHAv5KZJ3LyaizNSNJxnEqriuIh-l04hAbitkp-OA-m-hZV__FXAaKZ4EhhyU07zgnv16p3NUtCf3gYENbyGIq5_Z30Xd6EgB2LDt6MGi6VovE5SzJ1Zn2JABA_UrTUzKHtYvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=suTqBHsNFIm3cOXVb6uIVGQh2kMcoWnen2b0xtYMeoNVV5FGutgbu0ftEzLbsJM25dtrZfS6hJQX5g_IJsegil-4qzU2oWvePcPUKmVZZ8Hx2-PlxIdq1L4PveVYzbgSJMa7tIz1w2dz_bFwerPssh-0IZ7ODzzKiAsb5G6sI_iNarWy8KtWnRnCssDuUyfJ4EWfl5fJ5A7VMKZoHAv5KZJ3LyaizNSNJxnEqriuIh-l04hAbitkp-OA-m-hZV__FXAaKZ4EhhyU07zgnv16p3NUtCf3gYENbyGIq5_Z30Xd6EgB2LDt6MGi6VovE5SzJ1Zn2JABA_UrTUzKHtYvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSKKfWxy_MGxmrhZc1i0og8IJE3SjVh51ogHpCk7rQlcOHdzQUt7Yh7LdVK7eSfQo3gKKqssEWfaqKHnfb4xY6JriIWCIb3h6jOQ5e_ODPuCC-4oceWg3UWCRFKt2mIwotFfRHKLDQ1UrEZG47buF_Z3kuC8sYbRQMbg4-SDUgvIa-JuMQ_tOQRb8QyGC1ZEHR_Z2TF-w4gStDWafWbv9V2rurYWPZxmxMqyZu3s6ZATDG9uHhzxTtVjwHjAA8H46iywoKIV8iK1v9yPnHPH8kdJ6xBZSp0wfLo2aYbkHdb8_xw6d2A914pA16ZU_Mpq2PXCGCBukIGuZmCBUhczWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
بدلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🌐
MelBet1.net
🌐
MelBet1.net</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23886" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klcQ5F3F5cGkevjPwvvi3pO0X4DR0gHY2wqf7Lpz9cxq18OK6bsiKamS66YCPA2qDqyOdlDza4HkEvi5jPRfQ3-ow_Qs1f-ykTPhmgUvkGnCnpTwo2ToiL543F3OHnyx0FxiX7kLoRbgrA2XpD00EAea9TiVwplUUV9aWEQHiCszBpByRmU4zDZD0pE7ywJUnOYU1y3_tR-Gg8Oh1DRA46Dibto9awX3BV1vFbbxjZGB5vf8Y8yXZN9jbAguqrbH3K8sA1MiBPr3JpdGN1wgVqByNvt6-H961s87udqHgPcRJM-MIKkYGqKkA5ROwGKgt0qwLKF7hiStchpfK05q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=fIkPLATm9jfSJ6oQLbPjx6PGkEcbDugM-KUOK8w95liIkkNSswNVrWrCum3b-eDORShWQkZMOE5jnVNBnyJb-5mmv6BPl92-CJaWfIt0FeaaFWacx_Qrwd4G3LjYuEH1trVxBwr3mmdVTCjXrntDGHqP6z_IKibaRts_pj6Kq_pwiRelTy6lIGm5daijjtkYs3ChxcUkp9GsOTILwVjuKI5FURoFmfluN30KTHDpIsr4KcJ5MrwY5Naw6OKHy9aFkdJ0OHFAJa6-AyTwDJ7C_I0L-bFlYw10oNXJrgmPMluQAvPSXmFvz25QAbUfQ946Ab7KE_5Od-QcHbqp-wyIog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=fIkPLATm9jfSJ6oQLbPjx6PGkEcbDugM-KUOK8w95liIkkNSswNVrWrCum3b-eDORShWQkZMOE5jnVNBnyJb-5mmv6BPl92-CJaWfIt0FeaaFWacx_Qrwd4G3LjYuEH1trVxBwr3mmdVTCjXrntDGHqP6z_IKibaRts_pj6Kq_pwiRelTy6lIGm5daijjtkYs3ChxcUkp9GsOTILwVjuKI5FURoFmfluN30KTHDpIsr4KcJ5MrwY5Naw6OKHy9aFkdJ0OHFAJa6-AyTwDJ7C_I0L-bFlYw10oNXJrgmPMluQAvPSXmFvz25QAbUfQ946Ab7KE_5Od-QcHbqp-wyIog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJMvNvQEnrW7y-YxFKQQrdWuPZbNABX7LAntgRtCC08XtqF2g3dWPs2ZSTgCcHkz-j9abkRgisCxslzVt2d0vuIyVXRun9NgfIcjbMuAhklRbKpLQa3sadc96Y0_w3Em5St7DBaRDVAywK5Oxj4E8gkt8MuCXMa4As9E7z1ti_T3UaDVkomSS0VL4LPpOSHcBZf_wIFK3GxlGHw9Q-n-DhtmjMyBkSvGhI6gukkDZuwB1Oj899o3MCFwN_wx_GjdoWxwPiYFL6TSb38yOPGabT-32qN2_iHCRwwlNNFbDSxp6uzST_bG8z4ozVci5Mkv6CJY0c3RE0dbv_TsGMgI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUPW_mXivaDO6d6sYkZ8lo4e8F8xh2gMP7S78q5biB-WqFZ_984j9iEPaW2Xss8ZJlBtxHhcKQ-jPPsVMVF9Fj38uXihI0sGffRiVq_lkZmN7QrP6h-ABwY7y0iV1ggkLG8YbH2mpJdbQeJahKx84S8TcB4XVZi47b252e62_gf6uXTEfLh-s664y310MXJBxNRFv6F2EYmP1PAISJDBiaG95pYaahfnxnuCF1yjCBNZ2PqfElaEQBT9jYgUl3Z2q6NgjQSU9yNv87SSJeIS9otSYaamp_A_Bb6JUvp_Slpc6J2EXdRzAnj839qKlssAIE94tcnJAQXnPUIMyl3xsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEld8PsZ7XH70pDzxFQs1r8lLbkMyjERnw5j6_c8CmKfjpHWUdk8SubajD91oyxGXd2aUmIB3dJlD_69B3IwRDOieoQIctRNFM7EsN0WuP_2sRiHJIP26KVZF4xyCNa-CvaD43kKTi5U1N-obfWUmTCff9wWLVjl06LpFXiW8mPsr9miEHqo-MP_3npP14V3jMX_iZ1grCEJVx6aPqNgsFTNcwDyzKVnk6IQ5iI_RRhpUP30GtmRg5FXqc5Dtk7Er1S2ClPNinTg7uXdaJB_c0N2UcdioaGdt0hQ0DnDxHnjPO-F5ld64WiVJ6RZzUnHAipDd0oLX7_C_cc76NQ4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db7oJ11n8LBK61KEjiTuv7GgczkCk0LgX11MBSow88JIlT2xEnLWn3MomrbdA5J4Sd9yq8Hg-YOxsI7Mu74Ovxpm3OyY2g_IclTBeXt4IC5fEpClldd5SW_fg_Rc2S_cFhsD2-Xh2vt65YdJMQMvQcU0m6fLVxg_tD1Oii8PgqC8ESxw3EeFkdG3AS99uR-uCMPHFHlgaKNuTkgPX6ZRyWAp261ABHhwPRdiVPbN3FtEBIvgC-yvaqZqsPdeM4J_ToB31E-aAsJennqH6bgRsWUvK4Hx_mgdvY3b0M3jYhyedA0fvPr4YlJG2xrc5M8SGTNfl192FmhEYvvwpdUR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUzyouT4b_PHW5d4Jnse61EE4t8REvWBbdahrXdcph-z-PXNNI2-Vm768Fy28OkoXwt_xpx1H9j3n30yvWP2GAcqi7crpUwUbpVlaKSnNu7KyCVCebuTZIx3RL0pe-_wuaxDzx-cDXv_hF7lBW2XChm7nXeGMoa4wNdoAABY7cBr2LpbVkr7IkFzKJ5msoqxxB8dU8N8wDCQzp8hpYO3UoYnknsqUfaRfjs4Tkju6Djrm8r3SIrv_leU-W8alBxC03HQCQpXJrRnFYCS9hr3Ojtd74iFOncoDKnhMvZKvPat-s1FNVSSL75gll0zBgk7jny-P-Mrt6eIPZSzZjzkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfRLsTOEaRo_TuB0fwUoKgp7KOcy1awslM_azZhg_xYSH2fVgtH3kabKJoJBHjtHr5xuAqyEiTOwt3XbsOM2Wf6gNT5bjUT_N6WTwQNPCXz-HDN1kpPuN204v-CAzbPt8tkwaykk92MSpBPiOqrvhJA4i9FpTg9OuydYK1LwVeCU6WMmuJ7w-9LATokHjlL-AkDLJz_o9IW2S-UXLQo9lViIzYYdLN_RxhOS-IbGoALDzvOajHt3wo4ZJbBJBKGakE4glL5FLZLM5gMSmsPZ2GmDBVvEJuhBWwEka1Ag18iwms8RulPj7jr9dkSPvX5fA-BhkyRbfWFx7IEOleNsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMf4M6E-oJBX1h_xKkqW5yUZV8ZovCqP0fNtmCh4-AHLh8M7hlN3515V8zYZmiwgpQrLsbFawr80lPp_lvQ939qHj25xH7J53m-l4lVcyfB2OiYT_go_FvfE68gm31I9uckJolzoE3bJsWjIIqhBAoup40jIjKvnYXg7DiccItKJDh6kdSpc6bkV1DISq6dPcW9o1KwNYsLDNW0z4r5gDCjDDUpn3gagoru0Hq4aC8nDkVMBHEnaesIl6MVaxGPXL7EFaof5xFVJOrMEeIODv7-AeiN9hI1yjEQF78a2A-SCc7vluCoM32s5A7MZhwlgQi2e2zlBxaTTFQX2SonAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2_cfzb2pVB4TR-cZgIU5dcAAljwcgdmQ_rx5CYsnIIeCkeRG8UD3rb2Q-iq_LZG2XJNhd45r5TxWUu6wkDoYHQ3VrAmUJ9rasDDDwyokwbUL1BucbLZTAo9DUjeNgDsvzjk9dUqg05jjODAOTLSWjmMJSqPjOoKUTVgb69qax_QXq2n0YCImtFTeeAi-jSSvew3Ej05mzq0UThX1it9cD036Ig8Js8NnYbDtpunbp-oB-E1D-q-jA3blM4nGi1zIPQpzfrRTrCvRppmEA09BpP4Bc_OI7VicR2pAyh1m2AsEaJAqSnc3GKu2H-mnyq6sMnNz1I1IWcf874qOBAWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-tMnIceBFvANqcPpAXM7KNx8huIISqTCE_id1Zn7nGY1NdtMvEDqhaRzsHxTJYcv2HR9ewHOX5Eh_Lez_A-wxEoaNfiiO6xXfUtlPbZ6KLRODgWIOKDMUFoh_FIiq8WevybDpRmKdow2kMj2Mugx-GOV37s3LgMK188TjLWXJ6Y5U6ZqNdqx5pOPwTk3fBa6X0XP2USthCZAlxO6qtkQKWKxJYxspIUBMSqQmmqYcccgqx3w73MtVY6KXo4RXYq-89Fdrc_mSfhdkvZOB85m3Hd0msQ_yfIVnCdHKGWYKzkj4dmVSjJhjN0lO5yRwmXx7b5zJQjzxfFTnkbvJpNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23869">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwkmeHGLSEgN3XKBA1IZ4DdM54NqacbSgxsIQUpyzcPyGnRuhAmvPOp4ZaMTMJuS12MIV9N1e_3NDr44vPnXk7jrYfE6nZmljJ-FVj71n7zfpwB6s08IJUQI_pUU5zqeJnJ7muRE_qakgu9N-VEtEf1i62dLN9feSk4P8zA6hisZCGhGqNK5vmNqyKGaiDtMdaJsm4sNTQTqRRfqJDz_NClP0yoOCWEZRZACqMVP4qVsY3ltRoldk0xoHCLqxxQXfacp43R1I6dkHBPr65WjTH1o3_Naod0XGazGGWZxlfMHyg-gOydIKBVcx47YwlrbRoL8cNkZpOuaVv5wj9zZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
آیسان اسلامی به تلگرام پیوست
⭐
اگر توم از طرفدارا ایسان اسلامی هستی بیا توی کانال تلگرامش فعالیتش شرو کرده کنارش باش
🙂
ادرس عضویت کانالش
👇
e29
👇
https://t.me/+QMjHLL65ocsxYzRk
https://t.me/+QMjHLL65ocsxYzRk</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23869" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omZsKjrenN5Q9eoE0DqGQvye91hdVHp4qqLwdfpTN1-gnenwr3werF6DjOg1bK1TW5R02_cwlwppIgm3UfZjR0DOfqS1-vK9BGPerHSGdIU7wAQoX7zEOOsEZSrrV5FmAWmI44uomPamktjB4AQvmtgrITfKCecYNPzfejT9gXBSEA1fNjtwlwJ3X3OiB6eppHVE9xFH_nFb57WzLzGmv4UokLnxqRaRE5stkHKx3Pszy0leXoUu9H_9YhkmAo1mQjMdKUcxaBUMCqYP-hXLQ928CY-U6dcFmWMHgj8OBnbleu8lCGB5wUuHua9o-8ChiXQvvDO3FeTvEyBYi7-uKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g85Khn0c_L8aL2yjZT99IkbBcD4NltSlCTsQPybkAfBQeFzfs9OyYKjSAn6HJbDypMIbj7lp9hOEBcfIUQGh1wlLQ7exORlcQBD3Lkvy4xPcOog0wz-M7qFpIh-rXSJ5-yO92WCLkH0NL7caXj9fMmxgsP3t0DLt_U6LlsEwtrMnqCnNkp7DKmZ8VZsQWMUVLl_8n5FHEINnMLHzTEAIBX5gIv-oqkUv9ARweXQJOqKSkfc55cgD5DvIVTCc0LrmNumFgZ4JxegKh58KZSxzsnO0Uvi3UCCSbUKs6KkuY2jMj9ETd_jnxnTJWqoN4nESeimqfFemlm0wBbDFKAO-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVN9TfCywV2XLnPCIymacnTE_aD0sdvrmgs7kZuTDpdJHQey4p5jleeo1WVidf1Hbgo90SAXwgzj1gLjjPasJNZSostv8ogNyQuKNGHcE5o3HbzbqFbkjyFDPxC6JXISmmEmY9hduZA5rzlYllD62BWlLLdzStwwYI7RvU2ibhD94ZhFPvQUwUw0hjutfuLMjKoedXvHpOm10QsC-nxKMpUuqfB8OFO8lBL5MkWP3x6dC70AxGXpV6PT6g99faJijRdzYI9suNRq4wtaLQjxA8zjFslCLMbWdt0CuUtmC6gXTJttqn2rrTpX-ykcZKjXHYClPiZSY-LG3EXqzoa_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSy8HTlaDYK1i-0rRz4pnA1btaG7YGwvpensnytDf4LVaUfcXFAgoRbY7PMOdM9qzPAOWJUWVIe_VRESgYkQoc1dsvrGda0j3H1ZxNi4UA7u-LinrsUTEndDOtbSOp5VC7Y8AeMUyk4fiHjWtXykUsOfJG8t1xhu-epNJdjG5i63GNgwcW8yOMtSk7LkNM8ZLQm6RkLl2lffTkWy_mDkCNkdaniOZhP9p6W_6uyg_VPAC_OgcgOaTq0skKH_Dku6mbKhAjPlJWpVYbuyQTByzvXbXkqGTii7F46sgJeNRWHxJLIx92NxlpfT0pgsCEj3glGC2govdyAT784zMuANGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqq75EZ_ClwdhACrcRZ-UNd-d6DtwWCsTkRe94nyBW-pePv6SGbm-CpswlstDsyPP0RoBRPWC6LHguIZMSyKbqnn1yy70SZs9meT0ce-nc674qPQgK7U9Z8k6gKTq_AU-r2fux6UrzFLLpUj2_VQwXJXJOX0o-XMHx9ssrlcGUKk3HMwVNQ2x2wnPLJP-qz28vODx5JvmuOHOa7dTBSjA7ZAdY97ZBHfhiw66QCCzUzpGcLk26GqGwOZ9hkM5sG2VW2Tq--XDYbfPGVr8J8eBGBUBAUrS-hOqs0FTZfP7zWE9Vo-3Nide-Urm6P1kMDSA2kFpGoMs7ErkLNt3kBAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD7KLBIt_PzxFKyOYizoVfBUNDu_HVjRMwJS8txnkXIkqI_LkjWDV_QF3yOUMH-O82My2UZj6KobQ71b78uK7J1ZRzPN6VaBs56SPMmsu-s8LVzvGA2ia_lpgaXvGwAoWoEYuLqjSUct7HAiPL6Oaoocwf5seEWnfKmZoUhdtFMajf_D3jsyS-60UQHA-Xax7m-gVcovtXT5rTBk8PFOaYZ9jDA5nZ3xhy1URIWb-5gpcY79CniigL4K5FcL9xCzkPGZ0emYhKyth4ZTruGhPsbyFBEbxHvatB1SdKko-YaCJDkHxtphLtoxd4F6dIyoUJ07dZXHBpa3Q80QSTOBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erTBKBixWPLZIzOLecVYG30cS8r8GUk5JqDgKXjPkK9m2ZF3DFom3S9apAGybBdR-knOMUrWjaU31dQvnsmro1o5XHSucOG_Pxlby64oKzP5PXUWRYh-1-dbz_vPKF74zQ4P7dyCjDlM-P32gPihvgPz6ljMcQLRiC1iVTeX_rm0NKN6sNlhc61YeNL5YEWGGUiG5iZvFm5foZ_HVxgyihKJgbdC0nYQOa8PWZwfMK2r0AwUuTJWOP2aWoWdNEorSNFoN68eIEhl5sol4_Kxvr5W42W-feouhlCb4RHpxVr6_thYH4T1kGwYM_0y8CyqjIqRpbcZbWwKmZFNReVobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23860" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWhIwQG6BMEHwQGUFdWebHjT8xVPNrpirpzYUc9IVuum3k0EFAqNOeaynj2iVRpYAYp7j3Hw-0P93-KipxtsH3bAQ9kdbyhgDVJ7lBKXWEe3Xz7261BA3bW2s-RpJnv4dmAUJ-COGt5jJwWqkZB24J792WiF7He3O6x4AQtnPq0yp67bNFnojXf801rARbK4VBglWVakFh0-phYNaBtndFT3tFGQQqyGnIictjSm2ijbIQcrh8naNa1sxapLVryH9NMQZAfuXZFkwwTbv6Go6_64Hy4A0Ow70KRX4geq_GbcgmbEICrXrMHiMItuKFCtP6Bk9W5mNBSkNiAQP4_WnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7Iyg3F232kEkycerc9A1b4diBeIrtllMUvUIY1N2iVWeX8ALeQAXQ-1kLwghSEV_GO3EB9B9eV-3oMtECFrNoLnG7RY-qn_uudV-UrXESir1Y2X7hoOD2uDw5yhYcHPW6KFIyy6Vh0JAYO1YGDQMvWSEEhu0Tqgtg2lCc8-YqOrh_d3J21QUAm34i9q-bwlmKKlbIgFaGIWozQYVWweOgabEDYBr297vHV7TKC4TjvI9kU_3JjewkIq6WcxOam0WvZuX_odI9pHac9LtoYPS9KV2haCXdD1fwnUFYZodMPUKYKgoQP-IOb5m0NXTUD7zv4EWWYa7moT8XVBxihu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdX9ZWymePNNHBamec50M0tlRCNGAkLm8_XdBxVlZDoDLt47W2dqXkE5sfhPFYO9KKaxzj_1Jp0p5mflIj4tsJS5fcj1hvrKgKczkbrbvyzqiMGCgLqWK8zrhedQb2npR9UzO-6qi71Ny3ion0w6UWJzVW7tL-wwkATUAPtgmb0t8WbnImcmmvi5j0Ggm4k-DajUnyn-v3P-zRWnhEI9lveVBghZAGv2TV_Au8p2_dFaQmCubxd9gSE5e-JFM3FSjQyn624cvVS9ON9z9oMrgSVJ0rHfSnmM6esx-sMGYawbXZoelIKo7jPCt2RnhpWSvxgSW91nXREpBVp4adINAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmNetkQq-fsCATYjixgP0xr0rxPnCZdI9KUIObu1pPWlYQk-dIQUFyivRCvrIgVPSKsDqrIy7vHN9MxiCfe2v52VHxqZRDaJ1G4tx4Fh_LeBJUqFm496ISllsiSduGYXJz5PAnCFhIbC_4y4a53PPgY7ghMjrv3OvP5_qnTjEPwpHMZuKwwBCNBeL4HcOWwfBU5u7z5UtShtYV6_WfLb_tE1fyIRM5bENdM8BkG3kec_Mhe51NuAsuAmTpBGj4hWi-hKAFveVrkmZUZntuK4Q9a8rXjRhJ0PzmfQ1yh6uzI1DOXmCBztzxTvt4aNVJwdpq9rH_YcG96kvT2w_oTylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mui1kahPgwY3GVvLXcYIvrZ-fXifyDICtkmw0pB7WKbVT9gpVif9AJWKyj2VSEumN9fVEj1jIdWccCJqhh2kTOhI2zPS9vRvSnnGRZiqcV70YzUL5FkMyljoH1jB0X2cDS1-VBDJPd0Bh9RA-bmez80dYSbbuVEnXbVRZ6XovhS7mxSvWp1MMkxe1bnwzhm0dJJlO7d8VyVZ7hk8ADVO17ID2RGbxmc4vBK0jc8sAfkPB_MZTnFPamtkaIPzVIR5YH6iuxkMyj9ktshEF-ax3vweL7D0cH1iptgQqw3lTkofRSYyFyKnTl6RU7uWGMtpWgyZZQSqiBm_-nfDHy-mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxx4BJjzT7cUNlANntvcHs-PSZTsFI7SlzjhevXFMj-jKspW-Ico8jAa0rAGoMSoTuIu2xO_M7MJX4GZagKxZ5LvOtdcV3R8I1Y9A0ag5QZv-feyILSQvl0C36_5xOeU88uv_YK8qQ5iuG9ogQ117646EUihjbt4Cx79snjZ269DNX3wMYeS6G5Fdg7YWyQqClEgxndsa6Dv-lW-QEa76tcw9IUQ2hHtaikM0C5ssD4bYkR-Lj5RaYS64DkdJT2qMMYjsosKnbDJuGGbu-7vYmrOymKpYhmNYbJc3uWzPhQ46zGPXcPmzyfevKNzA_kroBvkcdJv-EcgOwV_TelnxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-DqgBXJpolvsYQx7ZccW2dvSJebC10ZI0uyVLVTlA2Ci3BEnpmyI9qnBDSQh9jKSQs5B9ypWlW-Dhd2rPI7hGqWKmVBYIyEvIBInqT8X7Ao-TWu8Kw3xDsE_nrXvkH3hNNbiC5n-_sidGt5r0PK14iPI27DoTF9pyoyuSikm5KFwbHO_3XahrfOIh_3t8UO6P6ooKZYWQeyEtp68Ws9-YD-uRojT8xuPwU28D7ZujZ97ublYibq77ZZTwxxuw_roBYCUs3FenRwQoGHBvf3ENXugFx13IkuMOuFfzhWIEWs4MeWOdZ8j1H7vIxYDnZqgIDu3eMAyUQqq0PBuFaKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaHe6dEhd9XP43ZqaA-_FQh-ij281L_J2MJIGMYIJqMR00DXU9hy2PTk5U-BdhSeSoh_Vcbz896Y4Pl57BsuDCHz8X9mRmEy42rjtY57_SimV7gOskfJ1nR-PlFo0CQWH14P3bu2S3oIHjZGE1eFFy9b_HGr9sXfTyBlRi5qMOddp63yTe0yAZgdyRCb1rGFjDch7WYf75_gLdcddN8doPoNx_AlMG3KNPDeJjizxoQeJPsVgvqInUJbgzFS5PVxvSA5p-9MlokLYLgRsIqlJkQk90kjHhL08z8Yb1py1pExTnYWDR4C6FglI_cXaxLssEQrLGQ-sPM5R2K0JxdqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=tvBceG2UkZ4HwOVVCtNETOMfrEVpWIz2o7ICAir2IP59X6tP_XQr9DK_-EFfbICBDUbVtMcGe6bLUtWqzXAzhZgsx6_VnV0Nu11F3DfUL4hJAPklYT9KlTH-LFZe23lMPqIi4-TbECW3zfz3DHO0tweln7uu5LACbhRlw-06Spq49iKzVp4Cfqbv5eoA37fN1zYy2q7hv4HkP8GlgfGEYemRr2n5f66t18skLY9DK5NuvEhjejiRUDk56fV4KAJs5P2XXO3FeWjIGUAE1yrLeqNptec312xUoExnJ7nVyQJ_XDzKuRXddS4Sadun9ctR8ollaJmrAsn-Oosdld53Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=tvBceG2UkZ4HwOVVCtNETOMfrEVpWIz2o7ICAir2IP59X6tP_XQr9DK_-EFfbICBDUbVtMcGe6bLUtWqzXAzhZgsx6_VnV0Nu11F3DfUL4hJAPklYT9KlTH-LFZe23lMPqIi4-TbECW3zfz3DHO0tweln7uu5LACbhRlw-06Spq49iKzVp4Cfqbv5eoA37fN1zYy2q7hv4HkP8GlgfGEYemRr2n5f66t18skLY9DK5NuvEhjejiRUDk56fV4KAJs5P2XXO3FeWjIGUAE1yrLeqNptec312xUoExnJ7nVyQJ_XDzKuRXddS4Sadun9ctR8ollaJmrAsn-Oosdld53Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK1PGFvjB7zxQTukSX7YYs98tO30Zjruvpk8nAodE3IRD8GU2TWe9KYMCm9viSTRIX8HIXfO_9cUu-bjbbCg9Z_CE3qAyqsIM6y55QZ5AUmsv2sqmUIUiYJZ_6N61LyBbr8-pOyhU6b1IKHuh1mIdPaZenPLO_gFGmGSLbaToZwCDoE53Jrnw-Wrmn7k5lGIKqwlDErwkhiAoW9TmbR3Q8TBM1Bgx7zWUYG0v8cDHlCmzrhRfl8UMJfHsKzTBRdOdNwroYrfTnq-YzEqrOULJzxPCpQOOjGObFImqUBHcKfLK3txyrunkwd3bvcZGj7AFes3USplbWQHi8jitSdGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MciWV93_Xyh9TVnzp3b5UFC5FpjtGSzfmuzE_RrQ2558dQ3zKY9_d795hvO_hDMe2Ysdvkqb1QToT9fJ1_xllOu0cr2LDEm9lEdkuy1iK1c0J9MQoZt4oabccmLc321ZXc5FziK9jl_nqFaR2g3PxKMJ6nc2WWVGCM0XVfKH5Lv_bShIDsFz7czU0trqnpFbA3Z72FFh3dQKpKZzsPxiTUSFbncqd74R5FqDeFAx1XM4--Mgg-Y7TLBZHBlmF1-2fB9mizsoRpUqBbwpUHXCkUuHtumMjblpoEmO92BgO5orzwuV6URbY4UFAncD-iQ1kk3YwgMKKx3bnpC34_SM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9XSkhRRRUUhda3yunVtVHrjBK2jeeGTz2lwu9XOEHcpu98qL6WASCEyI5u_XBUWEFx4bZ8tPrWjOpDp4Q2lJfe7KL3zpg__cgpfeJEfSiMJDZD766B8DkEruWao2I50D45QfBOqqDOvVNZzax3v-gS9Nmz9O4iE2WgLL8j5ZSybHI8VdySprF-osUJ8rHjVJg6u1DfdhMmg_8rcaTBnY1464h_AzqWGhLkCuU7XR7YECLIfJM8ZZbtYsLi408bqvEBttcO64zc-mJBQeBuGlj52MQgffFVzDEp67EbiT_hmkB-c31rCHMoPFc0jBSbnbaJXu1eCFyumExD2O1Ef-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvi9H6iEEPgl14X2kKtd_8EKcQGKkdCx9niQf2Vl-xCWCFNolhr0BkB088n5mfAGvZgdeXHuOBt10u9hGWDCyqYH_v63_f8QRRoGYeW2AnHtLtKLOymIimcBmzeKE-L4Flo0hXPRcnfKb1bBCgbsCnYv7dZOcnsXnnGARJkRzBHaz3EyT8qka-BJkq2te9zPuxHbY8xojpsTOr69RlnCpFkSQhe82G7oySiezqO_NkbVXIjKUAQlpz3vFiBmOX7r3vT0_VqCnkTE9NzdBPyZiP368W3qI1_oGfoklcar-ySD_u1ChxS9bhdBpTln0pnZOVxtRrpYXktBEnoVBo8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0PAFHpnngm7NME1YMMOI59LHVFpPFX9tGJXs6FTwyToil0xXyeKMplUwjTFTRaQpMYOslI5lgpI68cRhK88JNhlEje6piV3QvJ689cheKoi7v6uR7nFVPgZaSjfK6KOzj3Doj0P7wolK-lkRwzIe4A-RBcKsBX8n9EEq0Zvobgfo_SEr1814lzTkiZ106c-VcsMsvntiZMcg7coqCStbUcpRS2niWv2qFv3PkSFX5pB915M458COjX1HyAo0rZpYW90h9gS10Ua8hNK4YTAfhY8dbAKne3_m_08c2UbfQfPdo87GvDzhwp4xhruLxr_SNSPuA3fCbEnEX4bXYCPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgpLEaPqnhPdyUbYgV-LRfACNFUYdNKgcPpq8uAHc49vflCV7U3TykD5JVEZjpSoUxsZ4iPgf4jRASLFGviNSR8hCfUkMPsZ6EXd5EUVYWG0RN8RBFFhLfxKbjMr5VOdwnRRt5yytJLuSlpEF0yOzkQ64S4vSUPSVqgVpkMmL27_YO8kGVnU9Jflsi09XrRA8RQ4pnXoerJOINcx3klk5J1-GTBLMKoYP17KRnjz3o3cSj_mfeITyuDUxkoDxnfL8Ci9iBJOOO9sIa38BqZLYbmdmwZBc5CSh50PdLG3ISM_pbS75sgZ-08ZWYdsUUmuzHpaeyRVZT0gCZZulohBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4MKvVeYTgOxkhAjMSJTyrFTn55WqRmOKN6f8YVVSQ_YMWDVGpj_kzwr1gNoRkUKKL9meK3kSjYWWnQpbH5Tj_LhOE7mWMegP7Wr03ROc805I-QnbQGK8C_xoRZHUc2RVfmz3lfBWpH9LXX_juXodSx1G_hiMGlgn2JyBaUBDK1j6Wrd5H9EccDVnCUR0qZTpMV53XjoX8_bYaamBRDHisOoeqHWX_kPjxbomwDhQF5zl0Sy66yfRhLAJLfTpE9gFhUWxCggAZsq2A4v-XiW9QjmOIkDjPGOPYWwky4Hds2huZJfiM3isGMFB4KHHoym0R6L8MjkqgyOwwM5AJNOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPnQojm9_6fWOP_GwAHzzIX7ia1sCoy2He6MX-Q77x9EZH02fMWSJhDJFp6jgL7LOKgAKFSNDofb9d9ImgW1_b9cKPRI9r5jSi8G1j4EAoSRxv24nz_eE1Rpyb92uSPM98UXAxt99nteSYv6mu3mmw_1Heo8MbHo7ttqtwL1segDAO4cOULQdmjdG5UrcYtfA-pG_2-9jin7WtjT9rNOxHsPIDPfd8j3lsU_VmU2EqUFxTtLt_sbpfYt2BKkPXFbdMk6YZ4Ijjwcl-RusX1YfcJBOZSWUPwvsk4HXBcVDfvNalsktZ_u8-VH2dCwA1ftkwjWK8YaafmqfNgYYLhz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5xv0CxKSkOJfsGrbcWiDgyXU6AosCU_PSEwLSW8P0CaN9iq4qs10n7HDda9G3yquOAimISsKl2HXHVA5prciM9s85hG7ad4jBuzVDuXYK9A77HH-nGPOB5IXpCMMcE2nMOwstmz3s2oNS4tjdkmpH7vw3ForM9Y2cpNp9KU8fU7OMmvbdINYSmQP9ire_tw9y0oxxX4T0ssy8r6blSPssJYAZdUdPbleARgOvnASN1MgwM3_yW5EBml6A6pLFMlAPVUkBVLa9mSiBlV4b_MWzozT3ofHbpFzHYqv2XDby6RQwNhepPn-WtUz0gajGVXshxhr0rNVbezbVwZmOBOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVieDFn0EUNE59BqcwB3iZlksJAlaJdf5fRopTe5-MLo5VbmWWQP6hv3QdBIUMznX0hLOVaannbDp2a7HPGh-kC6zuBpw35-ZGPCt0uYNcMrTLpiCenHr2LYHnSWCtTOEJYeFo-Lv3C-U8eHVtSSs5hwUD9NX5wr5H5to92ote3dznH6SfM8-S46Le0cs-59yoNOJEklm82yygYOhq73TfR1jM39uX-k2czq0Ls7-lHh08craqfu4z4ueBktcfJ36FUJ_5gcqBZ0y71XedLN8VROtT5NWOxyLeFSbYAIcy4K4_btUtJ8vejkT7ZCw5RAkh1u2USYU5ZVU3ksz027uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=eS89JoTcmDzCuU1Ak79gRJgS3bHbUpgTIF2Z-74AjhUfaxHfCunZX5LJUCLWCJT6Xj3HZ8dhN9cpgxQ8IcjfQuWGGxYkQLGAbp8NhMaWaqng1Veov33XO56QrF37gGITZTluXQ3mcYKPb9hBhIYURQTakwJjj1Uy6j42hqzpSPETPKpCIN-KtVctNjs7BrVbGpdve_1qOUts9oSgYmpvo9zXHFijCUE3hR_8uP4aHIRSVS5I-MCF26xE08reDD1OPUn4b7aFscmBV0LFdFc8cuLaTvH7OPrPboOHe_IbakYSCGjPCqD5gcGuG-lcldPEIVpXYP-2DlyAkYFLT1aCMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=eS89JoTcmDzCuU1Ak79gRJgS3bHbUpgTIF2Z-74AjhUfaxHfCunZX5LJUCLWCJT6Xj3HZ8dhN9cpgxQ8IcjfQuWGGxYkQLGAbp8NhMaWaqng1Veov33XO56QrF37gGITZTluXQ3mcYKPb9hBhIYURQTakwJjj1Uy6j42hqzpSPETPKpCIN-KtVctNjs7BrVbGpdve_1qOUts9oSgYmpvo9zXHFijCUE3hR_8uP4aHIRSVS5I-MCF26xE08reDD1OPUn4b7aFscmBV0LFdFc8cuLaTvH7OPrPboOHe_IbakYSCGjPCqD5gcGuG-lcldPEIVpXYP-2DlyAkYFLT1aCMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HESumL2kJd6zSXy0R3LfJrwK2mR0Q6H392yJtNLjCti3f42Veuknw9LYDE7iFc57wr6pZacT4qkWe2FWkjLio4DFuBeQdERuU22UoyLNxEpOAl6wXwb9Yuf12KwZrW4_N8W4oTW8Q-HjSCJPJ3QyfMZW9Cxj0zBTcutBdrVrYBKcI5hKBXOJMeuBK3i0Guf3XCB73nHKoHMI7FWKxOnUuoXXk8zg87wSt_sYiqVYWK2LALaeSd_NTBGNqPjQNa9eKifdsZ7C3MWVENM5TwvHtnAzF_Ha2ru1d154psqGIQLAox1-iimcpF3i4xA8q42XQ7kY2Kwsv1NrIdpMFy8ztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glkgIVX3D3z2zg_75pgpXqJQ389nglks9hWb1mWTbc4gXDDXPs0Q-0QiQ9SYuvh-peqyfC9oMFp5Kzsu5ZZ9q6KAshtQqGG_ifCjoD2ji1f3OV9hX96JKg4PFXNexB14TUssg2d1gv9pXTSs4v8FQfU6c-YWRVUlPU-tmaCOuriqxbMSe37GS_44oNIlgpe8NVazCkF6f09eCh4z-AogDiBP5XwtjowX5DGLkJkdGqS2rOC6XKT2gqDtUnzMGODbyiOEBWrmnxq1M6NaQ7HCDq_KQddMWUjup-O2kGB-lFwV1Mg7_J3DJxCl2q3TOEI-iZGe2gv2XFk7sEqKK3BAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=oo5yrE-WUaoiwNkHyJ2QKSGLHcRZINkrEwVGu1d8vg-u66iQjOLI4X-Ec62578XSsPv2-qG9DmlGRSuvWJgrnQcL1qWqKLgfjNp-jp9lGbIyrNRz6y2M8e1DnJ8DUItVRt6h_McYrSEfl9bWIH8MIR1A6dbLSrz4A8J7XChLF8RdRjiOR93xMeORMBfnorfc2GI4hVp7bRlBsydBLVzz-qqDDx0Wk43BlCw-d6A7e_51TlnH87TPue18BAdAE3QeZhz6DNuvIB7ldk_ZF36Hj2cWrITB8PwehbTb5WeTVpJQj0lodvXMZyostu1AP_LvfgG4hZhtC7eP70iZCnmu3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=oo5yrE-WUaoiwNkHyJ2QKSGLHcRZINkrEwVGu1d8vg-u66iQjOLI4X-Ec62578XSsPv2-qG9DmlGRSuvWJgrnQcL1qWqKLgfjNp-jp9lGbIyrNRz6y2M8e1DnJ8DUItVRt6h_McYrSEfl9bWIH8MIR1A6dbLSrz4A8J7XChLF8RdRjiOR93xMeORMBfnorfc2GI4hVp7bRlBsydBLVzz-qqDDx0Wk43BlCw-d6A7e_51TlnH87TPue18BAdAE3QeZhz6DNuvIB7ldk_ZF36Hj2cWrITB8PwehbTb5WeTVpJQj0lodvXMZyostu1AP_LvfgG4hZhtC7eP70iZCnmu3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah8979hdTBpnZWp-zdIVFhY9Lo4Gw4pfzJjl48saVeNzEEwVycBK9WOl4u3QQLtYohB1WZFJLGdiOzHewP30orNqlehKhHgGzntelcBdEUwAPg5F12EHz9VoDIYdyZc43Kr873aPuIJ2HKx1dke8BTL8ctrmHc0nG-YrSKgqD09JTTJE1fLPr4ivSKVAAedkxu3zH4DnhgSpGsM-9igUSpsuV0LXijk5agzomJTKrE2EHuZJ9VZ6jLlbtwTO4BDQ14FKNNVi90M5bPbpEhHEG-6w3q2w3iKB4-O6I-3oCqTfuu_hONAkwdUJ4EsIZ9fVo4WggdJanRYUwmBN5AZY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYgXkEpQswO6vbQX_kPYQH7G9XErRFNd-jjZLisSMSr6Gqs0kPssepr_szZyWmYY9NJocpj9f77tnj7tatPRmUZkWfspSlmuRDZD9rFOJtx_5kuFsSn22pbBf4--Kji08BWvp5IEOZh0v2CBEL7v4G3oaKACAyQWcuU8yweneBRbMLzTh3Y01R1S1liP0AxCKw-Gshfk8on1H4w9cuQXeRTZtmlPQinT5CRQaM5_uByadqYp7kJKfsYWe3ZGQaufGZD9TD8GlaNQmvJmwWClREuhTNpiNYKFrhvjSnebc8W1lS0obE0IjG36B33ZP4rByAqAg_XdiU-1OlZv0yAqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=jRgV8VT4e7L94iN-JSLXE_Qa5W5vXtpgJXBNgHV9UoK00fxY0M4qRA1e0MLUbBdZAZNp7MAHinVc6xBQMNrqB2ftAd-0V7vdLbCOQBPDMf_299AOZaWGWRXQmqNmdMYqbjnvjoeIcKclvTdckDBZ7ctnz4jc0azjx0lOFbIIP7BUZ-2prlLJwYPAZ8_sD63PdkFbpZ7wH9U4N2j1m3nVK4_PUEpbjunJARr7hnQnWM3exzEcukzpUUKoQk4JwZcMCu_T8xnugE5wA9UTOrGKyOkf5murWQ5a74B9jNPUydaSFpNcUNtUTR8lDOGic00fegD9DNtgC9VmvgjvvzWmSJQd-4rpWvyca60x1SRbPrXD5x-Kgn87AwTeosWNE_SPN1LuZ71vkN87XFpdyzFHzjVX7j-tZOUNA0SOzL1gTd7ck_hlFBQEMgRsduf4LRehiBPDPF9L1rsCafZoWYzR9ZtkQ3c4jrTzKnhIQG9aRKW1Iyy4BZ2fcuyKvVGT4iufI6K8zkmcUI6YI788zE1g4x_LZ6cRZk2IpNgDq76Roir8kkHeOKiTJw1sb7u6Y1dFHmTK_dYcO8xkrvcGJMExJqvBvcNBnDPoYvB19ms1Z1kQ6UD1j6t89XC9EQAdLOl2jZj0oypohsoawnc8ymmeaHWpP8W3zaa78YbvwSacHPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=jRgV8VT4e7L94iN-JSLXE_Qa5W5vXtpgJXBNgHV9UoK00fxY0M4qRA1e0MLUbBdZAZNp7MAHinVc6xBQMNrqB2ftAd-0V7vdLbCOQBPDMf_299AOZaWGWRXQmqNmdMYqbjnvjoeIcKclvTdckDBZ7ctnz4jc0azjx0lOFbIIP7BUZ-2prlLJwYPAZ8_sD63PdkFbpZ7wH9U4N2j1m3nVK4_PUEpbjunJARr7hnQnWM3exzEcukzpUUKoQk4JwZcMCu_T8xnugE5wA9UTOrGKyOkf5murWQ5a74B9jNPUydaSFpNcUNtUTR8lDOGic00fegD9DNtgC9VmvgjvvzWmSJQd-4rpWvyca60x1SRbPrXD5x-Kgn87AwTeosWNE_SPN1LuZ71vkN87XFpdyzFHzjVX7j-tZOUNA0SOzL1gTd7ck_hlFBQEMgRsduf4LRehiBPDPF9L1rsCafZoWYzR9ZtkQ3c4jrTzKnhIQG9aRKW1Iyy4BZ2fcuyKvVGT4iufI6K8zkmcUI6YI788zE1g4x_LZ6cRZk2IpNgDq76Roir8kkHeOKiTJw1sb7u6Y1dFHmTK_dYcO8xkrvcGJMExJqvBvcNBnDPoYvB19ms1Z1kQ6UD1j6t89XC9EQAdLOl2jZj0oypohsoawnc8ymmeaHWpP8W3zaa78YbvwSacHPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxiASbrw1gObwmAQyc32nIMc0UEnAxr_6_ZX8EP6hPpLEfbrt6ABHxdF4O_SJwwJBFs71D80te1Vo5Qm7RtmQXv4td-w1ND_OE4STa3IdLXLf5NXKqSj_8UhPip3HXsYCSbbw8TqnKfYILtGCr-zm4bOBgLvjQqxYTORdSGUhK0NpKhMruCS8dq31Ej2TEQiyrXSGkJ-uwhu3zB8rGIylpiuBElb7sG-JxrPK043GLi6mdCveoJflJaDji83FFoxl4apZvNhxYQTDesrowmZ0acxd26q9BaJVoOCjrjH2UnziOq2RMLdUgDMB_NB7OveUtoimTOiT5UiomatTL_fWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYoOeVf04Y6MzLC8IE58klv9aS0Q1bEEIszMVzfbn_ao2I-2-KTFWPKpz8A17_UZnFtK9pyl9HcRZt-2ZESzzTEcN7fkn1BLsCAs1iPfds84v1H_aNl1ly8VdAMAfgP0JHydhKhRVPw80pwePVLr9bLHrzUDFbFrVpvaPwClYKgREYxkN1w59UVDELOGbKdsbIgXLJkEjD45stg69BCuMur3cO-mHlCAh-cosQ41dSMW_OWmy5DAbC1maXmTZrXmGXtqkhuFKpyy0BD6xTcml4tB_YV99D7cRY0mY9VwZPKDuxHmC6Mj7vbQT3P8n5H4ymQZJ2yqifw1IOI3WBMmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMdnYXnB7W3A502l898nMLPlpipXzQFrNxDJcs3oZZ11ntvqifTkr_7xZ1fx2HHOtK4-qZ0oJiGuwFMgD1mESc9NLp4tvtrb-U0LFTPByW-AcyRZCTPVMQA1TzU08zyy0YVQ7V3y3JU16CVDWXjqfsLjryXZGFBr_SUylQQjCNMPR71KYkgVJJiQKZzH8oU5j5O3xMaYgL-yeNY4cDVMQKocsX-PeK_NxBBomReR8nQETBQClIxAzk_arAXVVWLxq12crVSziO5oqG8ydpA9geJf4jHSp9VYOv1tbzTCYpnocuHKuEg6SsXceBiXuXWEGC1VR4joy09NydGVCCiY-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzaHEfqH9VQzG2JZbC-HBmYrL06ZPDY7Zk-Nd3QyeKrzSaGC5Nm3txKH_TUvkQG-HyKjwsyNJGHUmKmn2VIe0nHTaLUMg9pkZUwWLJ6YwO-B7Dw3IDgc14m02VyRy-Z0Fh14Fkr9XpDNu_U24-kVT8eQpHDkAKtT1vgvdScYtXf7ZByH0A0Kv5AQrMz5k8wNxuEXdER8AXdebeXeKHXnRwJRY09bAa52Jzh3gmVln63I6EgjhEsLYmMkIrW2F2iDnV2lh1Fy5_RmZdTeUK3jDDOcpXMWkzSxSwfb-9d7vu9N4wRKGmOFty3J2-voQJ3rfLqpT0Co6y6rF056pyV8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=j6iW-meh-2sb3fsM8Be17ohlI3aCL2Yzc7zv5Jv6BX8mBCRIv1joUfp8tBmuYJWcFPnwwGkUC4uRZKPLGkmQAEu_DZdQfVL4a7O8ScmpeANDDy22BJt2wTXjQbw7QwJQDBXIMK7mwBUYoH_4QGPPxRFL3jUAoX7Rf5_iVGxX1mYdKAUOh5ZWhv4pXIBovM47v5hoJKCdK3TyN_fDhLHBkfhexLb8phXg0ymg6_sEMDCfBMlmlTcIpFFNJ6F1-E4Clw6QkISt3_etP7sGkmk1tfQbneasb491y3pmAP4M6di_hz7qNKAqoVs1RlShEJ4jy6d8xRZmGBfk8TKP19ACCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=j6iW-meh-2sb3fsM8Be17ohlI3aCL2Yzc7zv5Jv6BX8mBCRIv1joUfp8tBmuYJWcFPnwwGkUC4uRZKPLGkmQAEu_DZdQfVL4a7O8ScmpeANDDy22BJt2wTXjQbw7QwJQDBXIMK7mwBUYoH_4QGPPxRFL3jUAoX7Rf5_iVGxX1mYdKAUOh5ZWhv4pXIBovM47v5hoJKCdK3TyN_fDhLHBkfhexLb8phXg0ymg6_sEMDCfBMlmlTcIpFFNJ6F1-E4Clw6QkISt3_etP7sGkmk1tfQbneasb491y3pmAP4M6di_hz7qNKAqoVs1RlShEJ4jy6d8xRZmGBfk8TKP19ACCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwgH_v48wo-JZ6hJrov7uJDJai2EAd_7knLKIoWloXJsOEQL_kGRpKPiV4pjRuyr4qkEXuu2oOrGnQTwhFTvtRaGveHnLTDvYLH2YjRb4-qLkZg6Myo67kVNa948-z8AOdz03pk5A-JuahFwtoK9hYhipDJ0cOYihAdyIEVONj9mgZlHbUCO8JDHOgZXQwRVwVz9pK8xsL-Cdwnz6QEclOIZO43j4DSh4gF5s4rI7G0RBFmChhP8KEEUW4Tc0fdx7J59Zxwi5HyHvOkeZ559tUxZiLAoJS7oiRsyIGt5ahRYq85JA9VdGKU09s8NM1qxg_Pm1AE6K6W0NhU2-GV3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=YlRlPg0tm1M50kfnaZTpEZdhM7NIYMCsD_jcaK-M8NUL1jRTb0xgMs-PwVx37TEg-AK4pS_ucLIsirN-Xw4J_pTSkYa3wAUySQLMJrl4PJ-1CB24zVaLBNJih5q4jXdZq1MG4eDn-N2o1ZjSQ4nuPc8aayJo1GRnj98-EbbrwhqKMQ1doWkHvfyyA9Z_oH3UVGDngwFRfm_gb-oX5ULedHvNVuKJA1Dlr1jDMJWaR8qjJ-kB5BYh9bleSKxULP4h-y9X2R7xs0fElCoModmbQvHuRvr2ezKlZbOH0SCLSDJnlXjkbEKYz49PPt2IBVdy25ZvqMUa4GxD74IKRSYrEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=YlRlPg0tm1M50kfnaZTpEZdhM7NIYMCsD_jcaK-M8NUL1jRTb0xgMs-PwVx37TEg-AK4pS_ucLIsirN-Xw4J_pTSkYa3wAUySQLMJrl4PJ-1CB24zVaLBNJih5q4jXdZq1MG4eDn-N2o1ZjSQ4nuPc8aayJo1GRnj98-EbbrwhqKMQ1doWkHvfyyA9Z_oH3UVGDngwFRfm_gb-oX5ULedHvNVuKJA1Dlr1jDMJWaR8qjJ-kB5BYh9bleSKxULP4h-y9X2R7xs0fElCoModmbQvHuRvr2ezKlZbOH0SCLSDJnlXjkbEKYz49PPt2IBVdy25ZvqMUa4GxD74IKRSYrEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0pGTuGdJaka58jefY85yZpQbnchQj251wlTtfeQ8L1sDQ7Jgw0Kjh_kII0j6IKwG01AwbjkMsf0I9S_wI-WLQ5l1CMPQLiduWLxRka8GQ0gNwOIO7fDwAT5i5tJ-cgrUSWqbcBrBRYnDimM4BrNIuDM6CzM87iui7apnvUkfjTgX2cC_uh8GjEnZan6ekc6zPz3nO_DvarB6vkfUvVVOiJHRUfElKaKRbav-xXEMjwZu8KwtEkzd6yhwUaZDyk8Sffd8d-5B33uiWoETDFXYlSJuBt4Nsv1i4kNKIIaze5hoZZsCIthEwKSuaEVgPrGVt0H5fPKL0HbvuEtv17ogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viPAM9GEB1I0nNPuPN-sAUejZbf3Uf-EBiDdreqPOpwVL25lle2HjjRPQPDVfb5aeAsD8nBzm-3uM-0A9yzLw2FlHnwP6YoxD7DbuV106Ey_vBVs_lErm0aVVEScZXJsRwHXDU4XsMeoCjsEwlHKEPsWFPfj2LtGvokJEVH7g10f8EwL75s0W9Bu3Pl0PXcpaYVyp7sYKzh_6fhtGVVLgvjV395o6KgPhKqCVsmKL-MzbZJZDmKlQWUgMGu1J9TKE85qgOQCkq9uQigG_jadZlSufB4Az_wugM4acjOm2Gm60xlrU9uEzx4jTXAhTzXVGzv0m6U_8IcZmp68QX29cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=hg3ZBEuD4SdIhvuhXbpeCWMSnHsyokQ3IKFndc5UxIcLWxX7KKrMbk8a0NDE2Aw5wGv9Yo8COD_NNdhXYsONsWslsLT-2ka56WfWWYjWU6ri0wMXgAxj7NW-RdoV8Wo5SZU-d28mc9sdP01ygQZVKCLKr4JttEzrMszm48ndp_YRJTPcgaUxRvdAUG8fno4X5IiOQ7nqBE-m3IrrcJQ6sgdRxq2GLd9ooSLdDHf1UMTqHFj70ZppmX-Al3xJ7J7LdDtewIBAiD4uwmyokJqbTCWU2TM7yAslAEVIvZpTr8bYXLBs4CnXD-ltXsCBIetuTbk6YuolN8YoGilB-wTk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=hg3ZBEuD4SdIhvuhXbpeCWMSnHsyokQ3IKFndc5UxIcLWxX7KKrMbk8a0NDE2Aw5wGv9Yo8COD_NNdhXYsONsWslsLT-2ka56WfWWYjWU6ri0wMXgAxj7NW-RdoV8Wo5SZU-d28mc9sdP01ygQZVKCLKr4JttEzrMszm48ndp_YRJTPcgaUxRvdAUG8fno4X5IiOQ7nqBE-m3IrrcJQ6sgdRxq2GLd9ooSLdDHf1UMTqHFj70ZppmX-Al3xJ7J7LdDtewIBAiD4uwmyokJqbTCWU2TM7yAslAEVIvZpTr8bYXLBs4CnXD-ltXsCBIetuTbk6YuolN8YoGilB-wTk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=MmHbJsp8ZZ9h46s60wfrRyRuS4fzMAq1ofddnOIBPeZDfW86LDWhAzqCafSYeteVuEpz5o6ypex4LPf_qTc9Q_moOh313F0_k9K0cmwRCzfcq1unYAVHRVzv7lUFPRF8IHovbQUg9tArv2YKth_Zg6aYZwLGGqLZ2HBuSFHxUIGs3cQx5eDYAWwqu5AKsuCgYEVzpXzXZeZSnkPBdD31DVz7cEZYux2AnWOvGDMTU89MLY-VCd0lxkKtheI6N5TWHT6y0H9UdNJp3Wg5LP7ktU96JuWfSw89EvgdX3gMAO3-d-npujdEw8OB_MkmYxEr1ujXGRe749uTh_GY5JbTNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=MmHbJsp8ZZ9h46s60wfrRyRuS4fzMAq1ofddnOIBPeZDfW86LDWhAzqCafSYeteVuEpz5o6ypex4LPf_qTc9Q_moOh313F0_k9K0cmwRCzfcq1unYAVHRVzv7lUFPRF8IHovbQUg9tArv2YKth_Zg6aYZwLGGqLZ2HBuSFHxUIGs3cQx5eDYAWwqu5AKsuCgYEVzpXzXZeZSnkPBdD31DVz7cEZYux2AnWOvGDMTU89MLY-VCd0lxkKtheI6N5TWHT6y0H9UdNJp3Wg5LP7ktU96JuWfSw89EvgdX3gMAO3-d-npujdEw8OB_MkmYxEr1ujXGRe749uTh_GY5JbTNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srhoB-r6JYSEzn4eImHCaJXott7SbSkZMYt3WOmqnQdn5csnNCu-wAowp0HWciqTtXAxqGV91R1TTI15e0iUdDgm93z_3axROIem6xpt6FzTOhgiFj-HlNML7PotVG5eE-ey5FMqd6fQlorGtvFrNTXFdJfr9MaCIJVlb12aXm7EJAXmMJe-b3pjuAh9thMlHewKZcV8C4c8ts-zlrm5GxH5RmOqnKZopdhlyEoB1DOwkk43jm8vGtaTVv4MQu-R_JsHMAbJqLmH2GDN1qUXAad75XcMP5Upde8RAoWY3PbFkuoZtgF-uU1igSxExZMe211MPTbNuF002loFW-0cOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=PCttwPYX6aYXDNhiExUiV0K3-Z9XXYi2k_a7-KkYBU27mTXMEh0areEpvsgv7FXk1GzNDWDWJUGNUpgvhU39bD_WRoSQqZvi9qDzb2ZEAapfZecpfk4K9YMfvYKk-fkxdrlqhA_ezqspblNio30AoplZxTu3Cegs6tCB7YEN4dHl-sa45rp6YB5if_5PELoXRuDqHI0Yro1_8u2IISEJFtpuIQNh5El3RWRXgq6Pez01iKprBgTKfAKUUfcvtpEvRlLesuTaKYLu8OyVEgotRZ6cIj6nbf4mjhRDkJK9H0Vq9c6GTe5K2sYefEsb5pltiuwjfk_C_QOB_53koSrNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=PCttwPYX6aYXDNhiExUiV0K3-Z9XXYi2k_a7-KkYBU27mTXMEh0areEpvsgv7FXk1GzNDWDWJUGNUpgvhU39bD_WRoSQqZvi9qDzb2ZEAapfZecpfk4K9YMfvYKk-fkxdrlqhA_ezqspblNio30AoplZxTu3Cegs6tCB7YEN4dHl-sa45rp6YB5if_5PELoXRuDqHI0Yro1_8u2IISEJFtpuIQNh5El3RWRXgq6Pez01iKprBgTKfAKUUfcvtpEvRlLesuTaKYLu8OyVEgotRZ6cIj6nbf4mjhRDkJK9H0Vq9c6GTe5K2sYefEsb5pltiuwjfk_C_QOB_53koSrNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=Hj_j_gpoDB7VCFI5rxM_pvChMAq3-PtHap9C6lBGEN_bCAxq-s0pwtMmdxcvkLZY6laTdQ8oSms301IrruMaMEEMiHTM9YVrkkYJdEpHcScRdq3BmhQURoucke7eTSm-zIpO5wnpOQ2LKiKrqWPKk1qUmsteEHUPg-TX0X0kIt-GNN4O8MEMsc_UYZMHe3U6BjdqSwdfZoniBbiIh87_vPlgHYl3YKYVwe2-4PfcCzzWlZHsRswkJsFbhYGcExCU7rGUQpJg5uvYQeK87xee5IDgqX5xPkaCkTVM1gJfdAfLuB2f798wKSZaSj78pI5m0FoF6vZ6wMr8hxS7AAd_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=Hj_j_gpoDB7VCFI5rxM_pvChMAq3-PtHap9C6lBGEN_bCAxq-s0pwtMmdxcvkLZY6laTdQ8oSms301IrruMaMEEMiHTM9YVrkkYJdEpHcScRdq3BmhQURoucke7eTSm-zIpO5wnpOQ2LKiKrqWPKk1qUmsteEHUPg-TX0X0kIt-GNN4O8MEMsc_UYZMHe3U6BjdqSwdfZoniBbiIh87_vPlgHYl3YKYVwe2-4PfcCzzWlZHsRswkJsFbhYGcExCU7rGUQpJg5uvYQeK87xee5IDgqX5xPkaCkTVM1gJfdAfLuB2f798wKSZaSj78pI5m0FoF6vZ6wMr8hxS7AAd_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntPZX5fTfcbMFW-_EsdFapYxLM7hrQSr4krJRXcHyc-Rvn04MDc0cJ5xZekoIO3nSf70xApzgpzUloJ7S7BEHyrk1mIEJH71Tvzq6VaOFjjU8vVmrml4hoEGLFea4MPlmXRJIq2jehwVMCnlhHW5tde3P__6U65Jjw438cKMg6qfsVKm-l8DJrz0HyZO3uci08rbH2OZJ4RSxm4BrUb-ty0jsI0PGzCrqNnsCY6hJRIpDhzUXODL5RwMc4XDcKPx3NHxySyTVPfctO4aAveh_zLtXWzp2STSo7QxFNxllX9lKblaTYoLUXvMwsPTYOharqBHrW4NrtYGWNYsZ9zKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK5vqPlrarV8RBI7Iv-oXBLFPyLKboDWRwuPGDqsSblFxW43rj6oaOAE0i4csE61bzgmRiezM0KKQ_-zxUzxnOyJvhYXBek7Fv-JYudFVxUbQQlO_3QbVfofqDXdpQpD2-SjIaMQScI0rrSRSyz3A1q5F-KFvwt4g0f5r676g9L3ToyHgmGFACcvH3583YrU_354FIrf2bcWEiWAPVsQK88Exb0OUzYuv3pRhc42n6bykoGMH_SmIbILGsz7UuXnklQBYYz2mQH-N7qpfbGUoEo5MAngocjt44bSiHqx4WMRLDhn5ZrjXOgpD5QTmnFb1-VPdidkafTnnfKMaGQdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=JwfYS2iPX8N9JNS2x001xqcA3X9RLNHWFHly55unUGvlNj2io4e7dr9bBTn_8AdAn-qo-SDBj16dG--42_tBBEjw2w7BVLFaGrygCo2txxUtAu5ivEsIZnqHc9JWERSUHicFQgJvkfIH-AViQeFG7ciF2ubONL2pL9B6QuFYlMD0pqamEv9uVOdis3X74ubH81cOk7IsBg5fP1tnoxai-qIN33xpJKCdlJWn-_rLNOXVk9sSICoAJF6skEh1o2lXOghLHE2se3mp1mZ4wEybRvsl53duhUCMfJ_UvDF894AvOaNPoln0q1vlLK9ppp5q3Y2FJru3EE3rq5uZfIbNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=JwfYS2iPX8N9JNS2x001xqcA3X9RLNHWFHly55unUGvlNj2io4e7dr9bBTn_8AdAn-qo-SDBj16dG--42_tBBEjw2w7BVLFaGrygCo2txxUtAu5ivEsIZnqHc9JWERSUHicFQgJvkfIH-AViQeFG7ciF2ubONL2pL9B6QuFYlMD0pqamEv9uVOdis3X74ubH81cOk7IsBg5fP1tnoxai-qIN33xpJKCdlJWn-_rLNOXVk9sSICoAJF6skEh1o2lXOghLHE2se3mp1mZ4wEybRvsl53duhUCMfJ_UvDF894AvOaNPoln0q1vlLK9ppp5q3Y2FJru3EE3rq5uZfIbNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMuQLh1EfRT1ZZMK1E89cbUwEfVnxQCKPCwWf40tXyIWHnlb15BE9TZc94hG_J4UU6TRwdlX6efNtr8I1JMWJQ93MTT3kUOk1Y_PLCT_kuDf5KcWnnHOp5jLryjlQVss6FeDGRSpn3Sfog6EsDD-3aynA0cgKCX4b45XQBol0aEIoiOW9j4EOCxFlB0RAi4OV6inUqwIwPTQoL_3RzWpOjPY_l1Tj-bj0mcdgkcMPun0r4cHJAXE2gPN4e0ku1KDvgL1gzS-UxbgJ1_EfFxm-lq1AgmuOr_BrU26Cqay51upSJbWM7YbfmZ21IrQhJhhPBb4GZQjpavF_N8deswMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqa0A1n5CJtIYYYa-rF8FwkyZIMPUwpyj7DK8uvBO6FxhpG36Hahzu8cfF8XZ8KEGL7W12Ole3ZnUnQghYkGmaARfuFKaQ4H919ssXam8d4yjxedkkdbe6I3SG87EFVU20GCmV49b_0JtM69RfUl4RbyKuyiHEbzU4ItvCP7z0oIh_2zZaDC61TMNvrisVt4kJUIjdtKPbi-M66Ipfb8LT-deLwZOhTXACAFRp6N_GFfEhoVSRYiPvo7uzBamEdBr16Awly8M1YdEtsf6W00d1t5asWXP1mjlpsteQFoCPYjiiZYS7MTsYWael2eV-1H_zKdMBKS5XcWkjOJ28qf_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFmCp-JjbNB8HBoyB0e56r9CyY93621g4rc6szJacgxI00kCrlZwcz090144xtZsayKwEvvDCS9dzJwjqzAdFxa3iSOwm5xXt0BCTVgUbRezmZTRHDAbqPitS9ugoSqTbx23xY3KlN4ohKQVnYKfHedw_cEix9A-g1xTKMyIcxQiR2vt1EcXE4WS018gbPYApXXllqWnL7tUpQmDOKIwFyoM_bOeEEOstDAgmOWwNi0c80mrhAnFNkxGqpcHhngmHM-ZJeHnx1Uq7BxKBimFy6aj7ncuDH3NhqzIiT8dsu7VE27FlZPYaw_zvsqr_FJN6mI27r3rzID2Y4DjvKsLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=oLcbbPG7R9_3WZPSSlHx1Lf8cm94Ki_3T7lhLdEfFokfBcHp525n3GHtjQlx_1VDXVQMFZ4O5tq6x5l7gcrUrDC3MCCeeDRXkBgx-lwqAxnsZH-MvaClbnk1o-tanqiYhy-Bk0oiSCbL25rC6oglajLQH-ZxWkQl--mlTUC4ivssBrNRTe8YctEogPrY8D-VmCq1e30Co2Y6eIj_wtYa3DMDJhjxwreOPODQb3NytWLYN9daR1m9Nk2ROZj4Z6h0zLK97SERYtlH9WHzfV3M6P1D4zGbqiv7pslfP5Qq3T9ldJMYWylcihwKCSXBun28P3GvcZLgJZvfctx3l_LBC2WeF2FXqiXJk1CG4OKsV_3_JZb2z47lVeFw4sorVg-6xGw_P4ecB7KgC1l3zua1_4bDiUwxzNVMM75n5ia7E9REiOH9wTTyjlCV6w4B1-SdUe9bb-Yo8NkoEqmy4yQKGRvAMthYZOvOr_A1gt7XYFe8UbYKHvtyr3_W4qXeox5GtNQop1ogtAX3v8q6evDaG8ZQg2_L-HWd-vf0mW9QM6e0EdLe8T9XxOfoh6_r3GQurchuEBsYK6xn-pM8YAHEexh7sQ5lCLn_eRDbB3EgiGGAmZZuIpDlf30_sF_n0_cBoxHPVf1wX5LAx9bBBLbKGvwNFkEiFwU1EENwYf5AoRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=oLcbbPG7R9_3WZPSSlHx1Lf8cm94Ki_3T7lhLdEfFokfBcHp525n3GHtjQlx_1VDXVQMFZ4O5tq6x5l7gcrUrDC3MCCeeDRXkBgx-lwqAxnsZH-MvaClbnk1o-tanqiYhy-Bk0oiSCbL25rC6oglajLQH-ZxWkQl--mlTUC4ivssBrNRTe8YctEogPrY8D-VmCq1e30Co2Y6eIj_wtYa3DMDJhjxwreOPODQb3NytWLYN9daR1m9Nk2ROZj4Z6h0zLK97SERYtlH9WHzfV3M6P1D4zGbqiv7pslfP5Qq3T9ldJMYWylcihwKCSXBun28P3GvcZLgJZvfctx3l_LBC2WeF2FXqiXJk1CG4OKsV_3_JZb2z47lVeFw4sorVg-6xGw_P4ecB7KgC1l3zua1_4bDiUwxzNVMM75n5ia7E9REiOH9wTTyjlCV6w4B1-SdUe9bb-Yo8NkoEqmy4yQKGRvAMthYZOvOr_A1gt7XYFe8UbYKHvtyr3_W4qXeox5GtNQop1ogtAX3v8q6evDaG8ZQg2_L-HWd-vf0mW9QM6e0EdLe8T9XxOfoh6_r3GQurchuEBsYK6xn-pM8YAHEexh7sQ5lCLn_eRDbB3EgiGGAmZZuIpDlf30_sF_n0_cBoxHPVf1wX5LAx9bBBLbKGvwNFkEiFwU1EENwYf5AoRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHNbTH0iV9Lbvgf7E_kQ-1bkaWgl2iCSf_bCSHINcPZNKKQnBt4l1jBhhNRqAuyXsFXE_WXqQch8nIRzA6U0edO4VMKBjVobVYCQ5bJkX_3IeOZNr4hHaLx2v7fWUgQ-3YShKlDn2mRM7s6my77byjAc9z7uQmBoD3LMWKhsZj0cstC53ZmdzIcpYTB8BgSzvafXznhSj_lMTgsseqLxSM7DFrUlDJ9qOLvPAIxssMRHcmgX2UJrXPP9qp4HzDCTuXZDJfgreFLplYZuP67LjFS9wY_adtRlCodHnNEQlq22Vf8WsLyieFmeuIFFrfmvdsPNUOcPLEjSSSIxU6u_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LED8HIHVuod_3JNuQ9rruipBYZXJ9NSPZEPu63xFhRxOZgtGbegCDP6APwLFz-wJaZA9hQ7pnAgB2lhqfsIomE9W5aTkU8mStECIk5gvlKp2p3ur1YH2EqjzjPCiRwaajV20hVBfGfGn-jxuRCHJ_ZE-4OuJhOENxJFYxRBGM-L0wd4T9xA91ec-0fNA8eMrxLj9hf7gmc7a38HqTzu76r3XOGuK0CHWme9sLS4RB6Qr-l9q972KRNZzE4A21xpjykjL8V-07MukslzP3QV6HPmaWAYfO2iVWaGttNB40P_Mbf3ZtDpwDgAKcaN-xzuaksVSYzvvCo618x1kFQBq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=svcCY7Qd6UbUnb2t1QX3rE4FWgfQFQdzNaseHPED31xatsEshOet0_pFyWmiVg0mn8YLF1qC1u3klUoMkNEMdtnjraCdfh0wD2xdcR0gbdtW-ljEmT534xaCMcboYEvRnRZlAP9CdMy9S5c_BlyoPkhuJ3fW5K-D8hMPiKwjY7149VsfVvIxId5fgZNHIAgL97aRDFRV2ytIL_uYWLft8hdUbEolt1lGOWEzfnQOygkA23IfBtgLwqZqDHlnNDf16VTfl0Jska3XWaNaPyvHiY4rwEx_WjRg4oKvR3iE32NQc2zYyqyxoi2QdM86QKIn6qL1LZJe4Jy1sb5KDix_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=svcCY7Qd6UbUnb2t1QX3rE4FWgfQFQdzNaseHPED31xatsEshOet0_pFyWmiVg0mn8YLF1qC1u3klUoMkNEMdtnjraCdfh0wD2xdcR0gbdtW-ljEmT534xaCMcboYEvRnRZlAP9CdMy9S5c_BlyoPkhuJ3fW5K-D8hMPiKwjY7149VsfVvIxId5fgZNHIAgL97aRDFRV2ytIL_uYWLft8hdUbEolt1lGOWEzfnQOygkA23IfBtgLwqZqDHlnNDf16VTfl0Jska3XWaNaPyvHiY4rwEx_WjRg4oKvR3iE32NQc2zYyqyxoi2QdM86QKIn6qL1LZJe4Jy1sb5KDix_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mChMOkICa42JKwY-Viunus2FiyAnVqr6L2BgZ5jeJgDdu45DDmI_HdHaCVmtrsCHRDGwW7agQpRUvdqZa0Mf4Oc-26_HpbCMMX4q1LDIMlSoQVNCK7tBpRVbklGZ5z0C2eZRZWMb7jUxeIkELiXIakpcFrkuKz9h9yLBEdZF-GgE9CR12a5lS77Rhxt2DTAh92rx4h4gCeExuNMsVP7p_5CAQfWvkgbaEPehmpDG1dQ5vAhfDjqEY2m9_tEyYW-gq1eCUOq1U9VD0eSlJAQynrN7dU9kWlAcFey2ydMdE8uTUeV5VADstIDKPbepVdo8Hw_V5P2ZyDpc3Zt6y3KBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyw9NUbB5ohixyRdlHjw1Q6JelqIdtSEIkXizoREeqZt0USkmawtsN4pl6_Z4PxID-Tn7qahT8PpKnc6-LjDzhgA9oSvvTnxLTgS6nu4wDpSjKrgJ6L9QO-spX1yqh0QIgXY0bEhaqv5bDwhuThz3ttaB_nS_OdMh8O1o4hhsU7SWbOaQ1D9g6F8ztBOyvEhEaCrTlPInIakiaUyAFj6ATbTtbZAqx6judNy2N6nwr5xaELrCfeOxkFdYItbmAFW6iu4InPWtfLvXX7yOIsJqV8Mdf9Kjrk1U9n1T_j_OVeBwdVJ_MC01j_tbFsXHNX7oFrUQ8L283kOGrsGYUWP3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8g7llkN2Y3LOCgutPLyr0QhK9fe_NVYhOzDSd8rERjQiw8iOsTL52My3WE6M6xh4nwC2e2apaDzZiPQUCOqnTCo0PlIJ8j5n4iSlgSlcmC1M-e5zTQiyM7_z00BFlnkzoH0GNhPvA0hpKoS4GGNufXGXh0LzNz5qG5dxzxQQZKA6i7lKITNtBK9BCDvLA6waCpOENYKxm4cTE0K7uUdED9kdmnllUqFKEmppdtT1LCUGFlfoNyq2N81ZqOvkIjeNEjo8tx3kuelngtzuTiLIpZhzhyLnlr5r3FTDnAWNOw-0O2p_etPEdj2hdKXI--J-ElrodXiGLVAA6gAUxnu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kos1yKOCc3K_En8quvAP4BLlLGGISPTOw0VNik9l97i4TYrVFCSeC5-2ub24-FD9ZYvii9ozAzofmDR7dmmDDjH8znzPjeT1d5UPf2UZP-ve3nVB_TBMDeK4P1Zo1Wb5YNs35s9IBAYBRxreiN_GzN2PRHP0Fp5Hw8cN84f5TXubcVTUi1BSW1XxcZGJkVO6P20N7w93BBUkQNV7Lrd7AEGIDA0cXKK9g2QTSo_oXf7CnJbuOXvXIntl2p7n9eIZf2qVAth18e_DXr7CMOFSkmtreGEUy11vK8juwePLG8wJ8BEr5CRdsPhOInY6c8QykAkbrxxBw5tLfv2E9whqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gdb25j0VAtiC9OMxz9hiDAPWOzbfKwaLbmUExH_RikQYYnh90ASy9qnEsntl4JMnET8gQ0BnBkMIdNSYgIMlMVfDcPMuDZIzjq6sfyG1ILFLW5p5qmIKixqxDllnbYA8669hD1-MoYGVizBL0OPZrLNRoXAeowTcLdO495d-3RBBAdO6yShJTIPqli6giqwUgLxTkV1t0mWkYDB6UJnQjWjUgQumfpLxgtdQUUjHOM3W1vmthzqcX5k0kUwfzzxpNzMtagPxT0LZBuTYTp_YpH4lLkF7b76DZh3plqNQbaek7sn-Vs9uKMPOFBkkTM_NUjCywOZ3KflVe4OSjooiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4GcC3H-JnsTrn3JGRDzACRgSXg7q61GFjgg4wNQuz8TdvxpT7B1CjalMIWQsAV7eUvvIVwRd3Kyh1D6SfUmHX6bRn-Fl3alKkYltkZ5_YS4tdro4R0oVHX3GbYU1QZ25i1PoYlI2PMPUVd8Pk4-sq5tBxpLZjKWlSfajrvBWkC5FI5A9r4COQQ4-JvvjmoFiiFZFQQk6OMSBw0IB1RPAoeqZ4aDu8dXg0wYmHUXYhWovvTi_o9n6N8kd2OABeDGZRFT1e1PqY6kBMIC4HC0WkbIPrVPLMDAF2z8uiTAlPil_snA1CHN4mpFoLXYg-H6-GnfD3Bl8BZBiXYD-lzFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ej6DoM7lHgd_jcMR4VbC5IO_18xFEy1eyiCwLByTxzbpD42RNq1o2ZUkAXu5rwQdJ_WQrvo_x_OIY9fOJyzQJDRCWtOOrAKYMa2qlyxh0fQAlnjAjjWVbHvBOlUZXthLYqBZWHm-AsQDnJFT_wvzPnEe33wg3-KLl-uz80J0h_W-v_XANwbmsSmLDWcgRfGFLy3Gj4iQ5kYbi4qZya7i7BD4Vj60epAD1AqTZwgcXtJXryLNLhEVZpSYtBc2zbvVMo6Qw5gvSxfyA9A_wn6XtMsFK6PA10BnKcSM9Bq3_aMZdHRIMO6IxMdEdtWMu2nqF87rPoiQvnbNyFucZGIt6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyjZRHc2kR6RpKOVxc9tFRMBHGJa8eXuVsk38Gjxyo5z69xyyOKzXHwPFMh6uJzSj02dI-VACEo18_NUEGXKRynUiWA71qOGQsXj6gaUVUTAjad2-VUHkRHcjD_RT-jAh-QeccRnAKC27jcDHcNKTv3AngpbpEBV33HgHQc2j8ue_znz6r67ZWQI2I8fztXxZtK3YWl3jUkPiEUUOsFexKW0D3FL_GLazqxfYknn-3csMu6C3kBZ6aGmteuS7XPZLfPwIVhRrGiRlQvy9Hy9Kz19NGZGPRR3EK8frwX0sJqkjvGn2dC5CvS9g8WdtfKXIqyDVp4qfjfOcYXq8BK2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKuiH6Su9uGhvqdn8kQbxC3_XAVkz2C9IaJ4JlN4Bezclisygclni6YKZ3wft_-D4lA38kDMmuAJ2cOHcRhKAOK7RhnqH2G1urc13w4_ZwtkKp1xrcXq17ozqt_L6L5mkPCpHQojMLZAkJP-PKuAs0a_8cyiWiYv-mak9MMFvuxpwdOT23VqNSp75UsxEwcLXbAnQBZmWVnI5Hnp-HQaBvUZthJ-zuXMumFbPZzguPDIaSHXn9nCozTp4mP7bsf1zkKNNXZpXjUrxUwTkURhH1EM8cSh7Fwy1mD4v0oY44U9136KIbJnSfV3GugPZ-XMLvk9_LyBQb1kadZlaXhl4EVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKuiH6Su9uGhvqdn8kQbxC3_XAVkz2C9IaJ4JlN4Bezclisygclni6YKZ3wft_-D4lA38kDMmuAJ2cOHcRhKAOK7RhnqH2G1urc13w4_ZwtkKp1xrcXq17ozqt_L6L5mkPCpHQojMLZAkJP-PKuAs0a_8cyiWiYv-mak9MMFvuxpwdOT23VqNSp75UsxEwcLXbAnQBZmWVnI5Hnp-HQaBvUZthJ-zuXMumFbPZzguPDIaSHXn9nCozTp4mP7bsf1zkKNNXZpXjUrxUwTkURhH1EM8cSh7Fwy1mD4v0oY44U9136KIbJnSfV3GugPZ-XMLvk9_LyBQb1kadZlaXhl4EVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RncEHRSgGhu7OZ468J9pnSdHQOr-WKdTT-aT5Cf-rq7G3pPwoB9JeseyYRD31a0e8mG-3zNdem5quiya_cmmxhBC5-HeVIxUskGR_0bnNsuUhSuLviVk171VoPl6Tp0CFv2lSImrW9TtiFtDb9ilw2_f7Wi7sRyBoVJoW32nO4Pwh3s8YZquIsR_Lc-I0Aj7byj-dDINNbQVs_HteV2uQgI31zjX6-i2IhC2GTwbN6qoQiAiQ6VWABvEsi1Pq3ql8SqhkJsEh2XReFp0nsv4aTYBBOnGCVdUOmsRMwcmLNpYfyhCyEveeYH7rG0y6UleO3cV6f0bXF6DDGB9_WTjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H36kYv1A0FP5reFb4uZl1w3B1WtmgumGVjI1iRDZnkhGN9VPubQ8pj1tXOoHbwVGMID_8DuIkD6Obn-qvJqxkeRHQi4LVZK5BY2eoaOAOhZPm9V76j_bO0qOvumS425EP3_jQv9H986sZxDSI8ilbk9xWvT8nF9REOGGXbZiwxCL14bUJFFarFYBuoc4AuWhAJUw-NG7-cp68OnsBCICMS9W8O5A6s4J3GgZ-q6RFRj-1VDLmAavzrmRt-NBlwcWAEO7tFcjwHGI6lF95h67wdkJ__3hbut-9n_0-wJLO4DV087Zdnrp6rgMsOjsypUUmytdOVg2XocPdn8LvI6IIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM24mUnLkFT1PHUDMSWQ8KemeNE0LxlCESGIq6ZsKdSqR3P_S1E_7PZiV6os7H7lWiHAtI_xemH9FjCpFGX1AS--wI4SnAPy0pBiWHmbyhjXlZNiAA9k7o2H7O6sxcUYwk2Xt0s1bFmBi8fES-AWOjWwsIWIxm09Zp01syepxs3DTlWzSz778izAZl0Fc0FZKMRyr24nfEFHsDrh8N8jRxwG9pY_xHIwKqIhEOP49uCrFsKjB4RfT_9sijq69Hm4PGf3_BFgS6bgq7ITc9KJXIEf7AyJmHQ8Q-FB4cqBwmsIcCdkI_DyzgPTo3y7lUXUNyaFw9IjY9Xfk5cfIXJi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUbrM2KXa5b4E-eU3EZUUpJOb1fDwJnGcNHEQpf5xi9HEK5bkgh_rCbOc-tvWidio80fe1aauD4XXJKyd1FA6XrJOpEeQiBi8hU4qGt3QQ1d1M0-4j9YeijS4kr8QILgz6AL32Jo07_x6oeDOLjoq5xATXbZ18R_9YLXeLkYAQjJ_D3w4hQ2rnIUDX1ou3VKHSD76Er-EZc9ebdcZzMshqvieauQMA6Hnb7igNPD8LEJU9TFTc724j7dslzP8Gp8Q6n1ZgUr9m3U-qkynUAhUFaImXf7msOqrGcsxo_uzxA5IQlGcp_LEQWY71Edfix6jl8RxHkZ3wvwlGJY0HtXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=Eewl8trabUSCH9UKtm13KpvB5TpYTC8L4-WDLNl2i5MIycvGySQcuomCPJ0YGC9CxuWTeQ1OFYYp6U4SIztjg5Tvhd10-yMTE1E0Tg62hz8Ejf5FfMuCjbs82DhoxXNsdXPSoBd0UdNc4XnO2RElfYOR_0NKyzKGt66kLsxE6180I59NVi12GGRxS2R7ll8hO-AdPZWNpbypnr_Qfg8R1U3-achlumdpkavrvlLQ7nuzXEcDCsDameP5lz4mN9M1GVrn60gdSXkzWSma0sVn06Vyus4kEi6sq84oamzQmz9Ae6AoJNcJ5ellm5G-Ed67Qak1tYLGgS3OzlW4U7f-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=Eewl8trabUSCH9UKtm13KpvB5TpYTC8L4-WDLNl2i5MIycvGySQcuomCPJ0YGC9CxuWTeQ1OFYYp6U4SIztjg5Tvhd10-yMTE1E0Tg62hz8Ejf5FfMuCjbs82DhoxXNsdXPSoBd0UdNc4XnO2RElfYOR_0NKyzKGt66kLsxE6180I59NVi12GGRxS2R7ll8hO-AdPZWNpbypnr_Qfg8R1U3-achlumdpkavrvlLQ7nuzXEcDCsDameP5lz4mN9M1GVrn60gdSXkzWSma0sVn06Vyus4kEi6sq84oamzQmz9Ae6AoJNcJ5ellm5G-Ed67Qak1tYLGgS3OzlW4U7f-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0qNTIE5VFqb4-gxfSjuk4_rMPuMFOecVWpU_36XLkqXdU2QQr0WyTXebUFNNrxeCzN-NXx1NeTTJfdmojWq1-XKkDgO1ob_af6y9mbwLB18HSCfEVvtgLwpJnP7FPTJRP83qwGDIzJi3BLFKEoC9FKJhHLvDX4kD4UsoFzyPgnu7J-cBW1iNrpFFnm3xTr1hvx9l613mUfScsR5CIZa_6l4do6cK7F77n5Mh-qSWsJyChQGI3-SRkXyQTnmThqlphy43KehlE0NoXWEgZ6Vw432stJZpEWgWcv2YQ5Gd7FXhRc-fz1ME5JA_A3KU7kDxiy998WLQdeFu1KTvd1H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOnbZltcSEbyTPphe8gPK7cwsGMFjVUE-cOq2FEMztRStQbb8O692P-k5B3ltE7bqSy41cEoODWYz8kO8DSORvJ4eAvQAX7S35TrJ1Ug7h6GOyKCxEfFe-5kC-9Lkf8eUZfsLPhltrVYg9h0EbxDIBc6mDgCWEg4mVKJ8_pnlSgWOI4Jyg0vQlBSxY8xTkokMkDrld2iTpd4GALu5A5cKjhmqMUIx86gYdB2gVWvgpw6buZ_Xi0obKv5kPAAyRVJ6neDSCF8zLM37-YhQijE5xvFh1_DEM5FfvCDxrSvHP1njrYKUveaC4fZoPbrdGx3W5OI9rqyEl3avSTrUauLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4llOPbWJKz7teA8Yge1uMgNfUNGDOIMNDOtsveQ_iYfbxPb2Rd7rA-eKXxb8UEngxRdMskcxJA9qB3YVfCE79RRd0KbjRFQzH-FF-w-puz_VD2XdANcIhhst_0qWGA5CjSJenRLMddacbF4MAjOrZ_9U6KQlrjLeBgfE1JsgQ0ENcz_gzyyAxfFovuVtoWJgJAGTqbTqICbrMF4YTV2bkujw1Kx9NN4E9btMV8kYExH_fGmQpEx4lNaxvoCdJdkoDYY7dCPiOkZ5Clui2PhUgjU3VB1dLIXR4dtwZ80k3vcm1-_XP474chpMEm_oqc5w2vk9iKfYZDRRdgjD0AQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPBGhip5OoUus8a2hg1OeY0cyqLKvl7Fnbu4BZ6YQckhlzeaxzf4A4h4kqhv9sMo5Cpsi-eAjImJYMny3yFd8nF4UNvt0C9ecPBfAw1OikUvdIjrTZ0pgp7ue2EBW0IyeI3-b-5nRIqNp53mqQWj2iLncAkNn7niFlsD1mqa1NWQs1fM7Mj_Nsnp4MG2pK7yb3F21VS9570ojTPgdjesQgb76a-BiMZcyJt19NukVutDKR3415-dhunhIUNLAj7EiqMhTd7iPGZNUcdYjaO_CM_3TrCgLJ5J_Esx86-iMbWBTMg2h_w956ktNJJTMsrkR5nP79Ru2J0BfkQ637VAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COYfj8yDTUZdrGlx2D-4h99_03jOMzy9GZiCgUiIyJKi4Uz4d_A1raEi6IZLq6WAWRZW0Mbt4rg0FOlwU-S-4mx3VEVw_l9jmQddVSnC_I0RlsH8fW6_Qq9FWt5iPfhja0r47l4nCKq5p3Mp8Ii3_RuH6L6xoQ2dhqiTXGrU4wcB4mZlGglSZszWMjlq-Wl86sFgrFOStjrA2UsQPRGqANP2OXBAzpe6JfvIS2uZBIvgKFJOaXrTAEGF_z_B0fQT_k1cEshf7Y5s-syvex9xTwf6OJoMw8kv7DyIlM8dT12Hgz_R4-Cg89F1JCJQ2tKn__voEZY1xq8XfXkxk_Tl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocHFN_kR-NVoBneZO6maYU9B7XXUJRkMIBD4SWJbj3DVTyWLC9V3pIVxEpZiaDL301xk4vl8_355vmc56MrPactSfwKK7h1cXjuJFbZU7yq1l-Amjjqk0ZBsbDvNF8TUvz2IxzO-CDuGcJFPMrkXu87fGCIZR0xmc1vEPH7dN3eJi88UwLRLl3MH2bWDuBlTLcMua-5QjxvHTm9jYOGjidTeT5_kmxu93VsHuJyuz-V2kw6ed6wMfo-69GVvc8zSIVJWChG6cvIPek2Zm-Eug9VAzMKRIIiJpXsgADb2eQ62_vUXOkTKoKYdlLVW0vsCLAHpYzweG7lxXfvc4CvVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUy3b98t6_18wSzuqgvkS9MK6V4PUUK0WGH96aVNUA3kko0dcPYpNlTtrqLWuA1V4M1AQBgGOD_bkF5vcj0GRkH_O-aUoINUcp5AWHkoeFbrBExVEa0rDC5EGjYeS89oaqCWWPW8KfCu1dIRqWCPBg4EC0dNUbYWGR0CaDN4kbFWh720XvZSX1nxD6SWYCylQ4rllTGokUNrR-PLybKINP-vsAXIiZU7Z5sVoNI7i36wESADhxwaFNr_jDcp-TAMEnm9DP7eXptzSXAKunzBPfuqRDRy28P6X6pRERxLYPmxmguwS4m3kufzy1_vJaHiP4FABIz6y1xbD1-spSeT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
