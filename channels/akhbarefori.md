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
<img src="https://cdn4.telesco.pe/file/ifTA3EiV27UZq8zQLvkvwN_B6JfnNmcpm9BqRhbCQk263Kg817kKbsaVE_zuGZxLTxPz5W9e9xQVG9xNn3_bYYk_kItSCjYsuYcMdEc0g2Q5n6jS78zjsLW0Fv7IXaaXCEXcrYre5qyWPrGcWxQkYJQ5Qjoi8xAJs_Ony4DE_CPiNtmq0pb6RR9j1ceQxG-5m5-CS1KHcUt-MDWIHQ7pOsfWgHyM7nEWl3UwmYV290nQuREmorGJTUxMT2sIGbDHIPzZKooqRvVw-s6XCOBnhUm5brmVZtc7ZoOXr7QSd3Wk8W4BOEJ8wQH6ZKPTjDj33hvEih3Q_DvRagMA_ll5fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 08:52:16</div>
<hr>

<div class="tg-post" id="msg-683235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معوقات بازنشستگان تأمین اجتماعی این هفته واریز می‌شود.
🔹
اراذل و اوباشی که به یک سالن ورزشی در نسیم‌شهر حمله کردند دستگیر شدند.
🔹
وزارت بهداشت لبنان: شهادت و زخمی‌شدن بیش از ۱۶ هزار لبنانی از اسفند پارسال تاکنون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/683235" target="_blank">📅 08:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef507mFtBtPbXCh6q5FjtVLMkweWnfzgB51H2yaG-MnYc1KnMk3vEXWxJI_Gc_8PlwochUkl-7vIh3r3GmZGcTy2jBUz4OpkWoaTLyQp4cuLiWtlL98zcHgYijD9JTp5VVUOWNfsL_lVZBhHOwhIup4OQE8TuEf-el4_fsYcWveuCPyxyK_Row-evOmp62Bc8Q_SRZD0S_QzYPHJmoolcNeh99dLvprCReo4KFegRjouY4D3prwdJz4Vu2EAL5MjIohEssEGNYLWXO-bdbJOhPtq_Ecnuh4x74ZXEZoW3SpdRGe67DahK_IJ9WGxHY1Tc_AV_19e3JjLWcCa38zKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۸ نظامی کشته و ۷۵۶ زخمی آمار تلفات ارتش تروریستی آمریکا در جنگ علیه ایران
🔹
بر اساس تازه‌ترین آمار پنتاگون، شمار نظامیان آمریکایی کشته و زخمی‌شده در جنگ با ایران به ۷۷۴ نفر رسیده است؛ ۱۸ نفر کشته و ۷۵۶ نفر زخمی شده‌اند.
🔹
پنتاگون طی روزهای اخیر ده‌ها مورد جدید را به فهرست مجروحان اضافه کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/akhbarefori/683234" target="_blank">📅 08:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unkZ5Ptb-qJ3StgU8wONbTeVR-6Uw45bj52vWcHypN7kR1mb8itNYI0niRkMYp83hRy-i1-aXXV7ahmEnSmn7zkcWC50Sgl5VI03mNlqMfa8V69yOL6c8JfAOHXVOr1yjmxfvdQgTceoD4BDF3QyUd8lci7GlULfWn0IoXYlDmpxJzf3H3XrfK0mJTBGRmStspuoMU0vdoMftKtw0avY-Q6XUFQ5rqK29tVwDpOc8TWJDNnqRvZxV4D9Nqc2h8WSZYxUOYTE-D81Kam6Gf2T4JgoOUVQXOg64BsiqPhE9Mb1x0tBK2UE8riVMticjh2DaXl4hp3MeBGWJPMKqmMcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itepqndtiP5EsIQBKudzHI6xAZQJsDdk0W9EAFbFPk-g6WBVnxaSkb5Ex54qgUZrhNMhqi_BlNosP-1xm-TQzXWh7ey6a3_z0qUGg_jf5PxhmI1RhMVrM0Aa1WjzuHEPRH1218YFe_-fYlaknRTEtNRmiYNpfKuen4IJq4JNHmYyS5JorzQcK6xM-zzPZRSTmSOEL1buUZ9VmcxuhCfxQaGUqk8UJSdc_H__b2qYN_JG81IrMzPfmEJ-eBsLd30K18H_LLUK68SJnMdSVW1SJDV-Q7McLxvxDAtD6SlrOBVmIjhoDg__cGlQ0LREwFdLS78xvl6D4fsJ5wy4lB7cuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nT6_NKFQy8u_dx51F7uUI9eYEHcXtOhlghDciVwmosYD9vV0q2fb029YdlJ6GHR9Rd6kAaVFSgMyTlY6uJXsO2xcdKsm03vctsvaxOkb_flrwj_8buL0CsEqDcYHz_Mebm5es6FIf0cPeg5y1hiwL98q1GuGh-kH_ldhHHO5oQ-ri9RuBd4JTQpLyc6zCKFP4U-fFVT6UTA5R2xT3oxqe2xBPL47eHO7bGWXQpUK6TT8wKEmxr4dFUtKEAA74akt1Tc8eBN_6gyz3Y7ZYQOj2827B7Lp4Jsiv5d-A9Zm3n7aIgZDhhO2oPTpB5qoLdS_bOl3vSlA1Vmw0INYXF1RJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEIX54Gavj9rcI23OG_dagHg10l4xk5uj3T3Ljz1lspna4yDA4am4OKcgg8KSwWQ-WkAQj3LlDIJjUgcEfN_sJ3gHXCxdtz6m9FWPeySn9azKOmFzyXW1JpdXkquKLgKod6NS50A2gLS-296mtzvnz4XR_37soOUnYQVpom6dPPTbzQ2e4VDW8UyQC9rnQawTWNrI5sFZit3D9OIg9Qg4TzJZZE1cZcr8zG1JAWZFbX36VOgSKaGjIZtqYGKXAWHjlzMdZVU6IfdPYelH_9ndCslytLSfF8rQBUNqoDs33gKpHFpKteai5uxaiJxLvngO7-18b6Hshe7vEyOa6Hbrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اگر لباس بنفش بپوشید، رایگان وارد این جزیره عجیب می‌شوید!
🔹
جزیره «بان‌وول» در کره جنوبی با خانه‌ها و معابر بنفش‌رنگ، به مقصدی متفاوت برای گردشگران تبدیل شده و بازدیدکنندگانی که لباس یا اکسسوری بنفش داشته باشند، می‌توانند رایگان وارد جزیره شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/akhbarefori/683230" target="_blank">📅 08:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تنگه هرمز قابل دور زدن نیست
فرهیختگان:
🔹
دورزدن تنگه هرمز به‌آسانی ادعایش نیست. اگر قابل دورزدن بود، دشمن مدت‌ها قبل اجرایی می‌کرد.
🔹
ایران می‌داند خطوط لوله جایگزین در میان‌مدت اثرات نسبی دارند و از مشکلاتی رنج می‌برند.
🔹
اگر میادین تولیدی منهدم شوند، آمریکا با بحرانی طولانی‌مدت روبه‌رو خواهد شد.
🔹
خطوط جایگزین تحت اشراف محور مقاومت هستند. الفجیره و ینبع بارها ضربه خورده‌اند.
🔹
عبور از هرمز به ۴ درصد پیش از جنگ رسیده؛ میانگین روزانه ۵ تا ۸ فروند کشتی.
🔹
قطر بزرگ‌ترین صادرکننده ال‌ان‌جی جهان است و راه جایگزین غیردریایی ندارد.
🔹
خط لوله ینبع و فجیره مجموعاً ۶ میلیون بشکه صادرات دارند؛ در حالی که صادرات پیش از جنگ ۲۰ میلیون بشکه بود.
🔹
هزینه بیمه هر بشکه از ۱-۲ دلار به ۱۰-۱۵ دلار رسیده و اسکورت هر کاروان صدها هزار دلار هزینه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/683229" target="_blank">📅 08:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c72a6e41.mp4?token=fMXDJgSsE5o4DoliRXZPQb6BL7eieBAEJF_Rv7iJClqtrk4jMJaSFDbEzuAo3ImMBP_ycbKaYVwaKGcpRML5ieMFuFLxr-lwk-7ysjDjcWW_hwmLDmjOSYtE2FOGvft6AM3djFs-qT8MssJ_SwEgi-TkF5a5pKLVIF1npZ9DfaCbmxhdpmCy9s0sNREEkrf_BV5Jokm7EgG1nWHUD4nzjGXGAbkIB9Vf_f7M4iYyB3a22G7M0Zq6bHlytXWaAeZFQYNRXI34xRylyPYv0NRn3SodGinP0Ex1DPVE-VfwukXTvAmVZqujpf1ErA51BrDCW0Sea3oTf4AWsuSQbM8F2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c72a6e41.mp4?token=fMXDJgSsE5o4DoliRXZPQb6BL7eieBAEJF_Rv7iJClqtrk4jMJaSFDbEzuAo3ImMBP_ycbKaYVwaKGcpRML5ieMFuFLxr-lwk-7ysjDjcWW_hwmLDmjOSYtE2FOGvft6AM3djFs-qT8MssJ_SwEgi-TkF5a5pKLVIF1npZ9DfaCbmxhdpmCy9s0sNREEkrf_BV5Jokm7EgG1nWHUD4nzjGXGAbkIB9Vf_f7M4iYyB3a22G7M0Zq6bHlytXWaAeZFQYNRXI34xRylyPYv0NRn3SodGinP0Ex1DPVE-VfwukXTvAmVZqujpf1ErA51BrDCW0Sea3oTf4AWsuSQbM8F2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرونشست متروی پرند بازهم به مرحلۀ هشدار رسید
🔹
تصاویر جدید از محدودۀ ایستگاه متروی پرند نشان می‌دهد که علی‌رغم گزارش‌های مکرر از اسفندماه ۱۴۰۳، فرونشست زمین در این منطقه شدت یافته و ایمنی زیرساختی شهر بار دیگر به مخاطره افتاده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/683228" target="_blank">📅 08:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
هر آمریکایی متجاوز به ایران را بکشید یا تحویل دهید، ۵ میلیارد تومان پاداش می‌گیرید  طرح جدید ارتش که توسط سرلشکر حاتمی فرمانده کل ارتش اعلام شد:
🔹
پنج میلیارد تومان پاداش برای کسی که هر آمریکایی متجاوز به خاک و آب ایران عزیز را بکشد یا به واحدهای ارتش تسلیم…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/akhbarefori/683227" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrnJrg58tKOMphus9WK93MHPJNj5iuBzklAlfbpsBtTVOMFqySg58kHuVKQksSMG09wFas7JGc0HndKjsI58Is6o5VtXNZA4eQ5hiNSV-awnHdKIy_tU5cbPaKpFeMJFUEctBmrVRneNy820cV5jMCOJOkCgTjsAL1FuVappFK8w9RutCssnxX1BjVE78psJTnZQK0F-udOkzPAZqDYltK01vgxvVLSBlPMkQ5ygL4hyUjxRFR6D6dC6jEAkgFRen0j_XjPusIpv6cLN1Sh89xjpigleHmkWp1JBLWPhD8T8a81Pw5c8Lfp4_h7V-aiyQnEkq3nqI95lfZI2uXHMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از شش ماه جنگ، ترامپ در حال شکست خوردن است
مجله نیویورکر:
🔹
دونالد ترامپ با اعتماد به نفسی کاذب و در اوج غرور وارد مناقشه با ایران شد. اکنون او خود را ناتوان از پایان دادن به جنگی می‌بیند که هیچ‌یک از همسایگان عرب ایران خواهان آغاز آن نبودند.
🔹
ایالات متحده اکنون در تکاپوی یافتن راهی است تا ایران را از ابزار تنگه هرمز محروم کند که اهمیت و نقش‌آفرینی آن تنها به دلیل مداخلات خود ترامپ تشدید شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/683226" target="_blank">📅 08:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647bfc14dd.mp4?token=vw9xe3ZONp3Nx_oirudeqFzeSOOMgJoDDCD3mrFvxkCEhxUVkEDRvfo8uCo2zwRoJ3rZoR7AW8CdbFQKNpj-JI99cmktNVe-5zjNd1dAWjMxLrI3c91MHRzaxnUcjN9ISnDkEZG2wMnKd0Vd2LjwAvWrQ5SXhEfsQtl505xc7J0iLO6fBMPI7gQ3ED7TviRWETND2cqrSO_wCXRSWtiVnQlxUHdeadW6i5hyh8Swxm5iepmko12l4M1aFRRlT95fyhEpEa-fQ5kCVkC-pc-R2giQEocQfmsA6LrzlkstBdR96ATwARTHYgUJidpVBDaR3sPajzGIDqIG5oWaFbbqqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647bfc14dd.mp4?token=vw9xe3ZONp3Nx_oirudeqFzeSOOMgJoDDCD3mrFvxkCEhxUVkEDRvfo8uCo2zwRoJ3rZoR7AW8CdbFQKNpj-JI99cmktNVe-5zjNd1dAWjMxLrI3c91MHRzaxnUcjN9ISnDkEZG2wMnKd0Vd2LjwAvWrQ5SXhEfsQtl505xc7J0iLO6fBMPI7gQ3ED7TviRWETND2cqrSO_wCXRSWtiVnQlxUHdeadW6i5hyh8Swxm5iepmko12l4M1aFRRlT95fyhEpEa-fQ5kCVkC-pc-R2giQEocQfmsA6LrzlkstBdR96ATwARTHYgUJidpVBDaR3sPajzGIDqIG5oWaFbbqqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت هیپ‌هینج کلید تقویت و کنترل کمر #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/683225" target="_blank">📅 08:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eum9eVN1xeKw-cnH6kxkcrTKK53_AujsvOxl9Ti0OY3CjUTey_pxMBTzU95rR-HugA0xrakvnUTkjFH-n_CdfsyhTHHi4DTsfti99jEsiNvEGxo7KQ4XDD7BWl5d7erdb_AXG9EyBBIovWs-NldjbzPaWhlbgaJ7pENEjUzXpKUmBBjj4QuqpCz6L3p_XNnCaMPwF5v34oq3QzpmEzJLREyknfJ9ptLOH3KEexM0IuWTieNYY-OoqbaLS8NMAXHBzcCQKWECBKaY05oZqYkzxnkGuPBam4N15TTJRLOzVSA0ZqbNdPJkuSP9BhYnstQgMsOP1numqKOvuMcnnaKsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰۲۷ می‌تواند گرم‌ترین سال تاریخ زمین باشد
🔹
براساس پیش‌بینی‌های اقلیمی، بازگشت پدیده «ال‌نینو» می‌تواند روند افزایش دمای جهانی را تا سال ۲۰۳۰ تشدید کند و سال آینده میلادی را به یکی از گرم‌ترین سال‌های ثبت‌شده یا حتی گرم‌ترین سال تاریخ تبدیل کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/683224" target="_blank">📅 07:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شکست مذاکرات تجاری کانادا-آمریکا/اجرای تعرفه ۵۰ درصدی ترامپ از امشب
🔹
دولت عراق: ۳۰ سپتامبر آخرین مهلت خلع سلاح گروه‌های مسلح است.
🔹
فاجعه مهاجرتی در تونس؛ ۱۳ نفر در دریا ناپدید شدند.
🔹
کی‌یف به‌‌دنبال دریافت مجوز برای استفاده از استارلینک در حملات به روسیه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/683223" target="_blank">📅 07:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
امروز؛ پایان زمان مشاهده و تأیید سوابق تحصیلی داوطلبان آزمون سراسری
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش:
🔹
داوطلبان آزمون‌های سراسری و پذیرش دانشجو-معلم برای مشاهده و تأیید سوابق تحصیلی تا پایان امروز فرصت دارند، به سامانه جامع آزمون سراسری مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/683222" target="_blank">📅 07:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین|فصل‌دو،قسمت‌آخر</div>
  <div class="tg-doc-extra">روزبهان بقلی شیرازی</div>
</div>
<a href="https://t.me/akhbarefori/683221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
روزبهان بقلی شیرازی (شطحیات و شکستنِ نقاب‌ها)
🗓
در قسمت آخر از فصل دوم، بزرگترین کلاس درس تاریخ را برای «مبارزه با ریاکاری و ظاهرسازی در سیستم‌ها»، «پایبندی به حقیقتِ وجودی» و «شجاعت در شکستنِ تعصباتِ منجمد» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/683221" target="_blank">📅 07:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f964f5414.mp4?token=GMI10ifLy21GHefO3ABBHHO4QgJQ2iB3IWmzDhYziEkoTR1GpcygT_12d-DqrCREurKnu94ahEb8e9AWHnq95e6-1qhC0-TtvqnzJM3IIdTXzsiXyjRr2uePPIzQKkWdvQ-m1MbtH0-XQW2icN5Az1SJuQogUF0jJ_w-128w9ehooMbEl2OZS2QrvsX-nB6U-9CRf3qTS_lsnjFNP8e72kpOEcAB4I2hmKbqFfY_SWSQba827Ght5vGkUUWccMYR_TTTVJBITFRnFYOAdJ4DrL1ncnzo6fKgVNQw64QkgKDVEOcdRfr_7BlYf_rFM4VmaWeC5Z48HRINLpwNRG33I6LlsN2aiqYGQQoyEMHeqkMQuDZZ7g4tieI4fa49PMDGVZWnp1hbu5iFiMPscAGptSWbxL7LJFLY3H4VgrfQZBPUdbtix2ilZh-T2CvL3Dp_nkxB0qAMd5leSpjVXeHTZA5WPsIOOxaAsQa_zaAZ_zSgemSmD3N0ez5bNEMm7IAe64Ad_Om0VQLYCjzpQ6qaa2WlBd5g9IRCiPd2KBR2pfZ8XSeB5sJj3ez8ggGmNn1fEJgBuzSxcLnbvWtyrqbI4NK2s-D4oTz5yeEj_y0rFqw46fuab8gYIS2IvNSb7R6nLPCYIjEmhpUkJO1G7plDcudn5rFmcesBBU11s7x4Lm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f964f5414.mp4?token=GMI10ifLy21GHefO3ABBHHO4QgJQ2iB3IWmzDhYziEkoTR1GpcygT_12d-DqrCREurKnu94ahEb8e9AWHnq95e6-1qhC0-TtvqnzJM3IIdTXzsiXyjRr2uePPIzQKkWdvQ-m1MbtH0-XQW2icN5Az1SJuQogUF0jJ_w-128w9ehooMbEl2OZS2QrvsX-nB6U-9CRf3qTS_lsnjFNP8e72kpOEcAB4I2hmKbqFfY_SWSQba827Ght5vGkUUWccMYR_TTTVJBITFRnFYOAdJ4DrL1ncnzo6fKgVNQw64QkgKDVEOcdRfr_7BlYf_rFM4VmaWeC5Z48HRINLpwNRG33I6LlsN2aiqYGQQoyEMHeqkMQuDZZ7g4tieI4fa49PMDGVZWnp1hbu5iFiMPscAGptSWbxL7LJFLY3H4VgrfQZBPUdbtix2ilZh-T2CvL3Dp_nkxB0qAMd5leSpjVXeHTZA5WPsIOOxaAsQa_zaAZ_zSgemSmD3N0ez5bNEMm7IAe64Ad_Om0VQLYCjzpQ6qaa2WlBd5g9IRCiPd2KBR2pfZ8XSeB5sJj3ez8ggGmNn1fEJgBuzSxcLnbvWtyrqbI4NK2s-D4oTz5yeEj_y0rFqw46fuab8gYIS2IvNSb7R6nLPCYIjEmhpUkJO1G7plDcudn5rFmcesBBU11s7x4Lm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزبهان بقلی شیرازی، عشق علیه دکانِ زهدفروشی
#پادکست_کافئین
| فصل‌دو،قسمت‌آخر
☕️
🔹
عارفِ سبزی‌فروشی که نشان داد چطور می‌توان در برابر انجمادِ فکری و ظاهرسازیِ مسموم ایستاد و با بیانِ شطحیات و حقایقِ بدونِ نقاب، تعصبات زمانه را متلاشی کرد. پایانی باشکوه بر فصل دوم کافئین.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/55g94bwW9F8?si=URz67u7w_S1WBO8N
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/683220" target="_blank">📅 07:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6zDjUkBI2FDqrf0nVaHQtXTLc7FtawTkBMAsaBJmFdkRlaLq3UZ1nxQXMM4-uA4l1Ad7S1DyAZcmc-zvQNo9ppFqJj4GyPgpVxXDQSqZC2GIx1uGmIVnPEDRPccRu8ZNE0ww-mYvZbODLqTGo8G5F8XE3rwyhGkhnIWK4sbfgsbcc72rgOt6_Ns6wvxLhlhWoYJcSHPHQY28QCrFhTqWDbsk8_tVV9x1D8bWnzgLBGLLDtXtmVMA7cr9jqCJDHcrEamF1KPqo5mQQc1yQ26ktCWM1mPL7BAB5yCDpDgnyB4ha_7EAzVnE3s60Ti_W5LKl2GwLeE-Cnq1w7Jj81Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۳۱ مرداد ماه
۹ ربیع‌الأول ‌۱۴۴۸
۲۲ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/683219" target="_blank">📅 07:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f9b48103.mp4?token=K0MrY2pOYamhEBHopgE123fDJvKyAWhKagRxog-Db1D24E-cKybThd9qk5KsVdPQjqU8FQaXZOAn1emCvkTtdD8GI7KziMcqJMUmqr2YWNNeSc-dLtpKa5hj9ZLUkROMak_V1K9zwrrUGYUZBDGEfsUds1Yx0KrgBvUtQ8fKl2RGKswQuHvsroEINZj6WN-Jk4h8jNti1inMOoKqStw1C8nkBUWzpugbFsDvHejNL7zuSxq6f-VGt51NzJ_BuvEggOW2pzfFY633UJ4GOgJaIUnalG5cjhCalUTo71VeSx4Gu-RfN0HBnlobJRR-ochhQYVExzj_3m1edWZ7i46l4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f9b48103.mp4?token=K0MrY2pOYamhEBHopgE123fDJvKyAWhKagRxog-Db1D24E-cKybThd9qk5KsVdPQjqU8FQaXZOAn1emCvkTtdD8GI7KziMcqJMUmqr2YWNNeSc-dLtpKa5hj9ZLUkROMak_V1K9zwrrUGYUZBDGEfsUds1Yx0KrgBvUtQ8fKl2RGKswQuHvsroEINZj6WN-Jk4h8jNti1inMOoKqStw1C8nkBUWzpugbFsDvHejNL7zuSxq6f-VGt51NzJ_BuvEggOW2pzfFY633UJ4GOgJaIUnalG5cjhCalUTo71VeSx4Gu-RfN0HBnlobJRR-ochhQYVExzj_3m1edWZ7i46l4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلال در سخنرانی ترامپ
🔹
سخنرانی دونالد ترامپ، رئیس دولت تروریستی آمریکا با حواشی تازه‌ای همراه شد؛ ورود یک معترض به میان جمعیت و فریادهای انتقادی او، روند این سخنرانی را برای لحظاتی دچار اختلال کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683218" target="_blank">📅 04:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAOHbBcmpGsGqro2ym4IVh12T51NOkxXGMndIj6H4T5aRmygSYbggJN9pvY99Yk3yOv7qJeC50mIMbQkSB3kOdxykJWARjGb4hJKgtBD6L0kVbsbNA7PKcNc4kMGXVrxOJFJuGTe3TJG7BrbnIiz3t5S_GJkoiYi7DSNo2-4Vp0ThLCl3qY3RkDv41YYbXX5_Vaeq_GI1T87GbUN-JM6qR0aaDkfxIwpPyWuZhirUwYrFQJsFw93MKJZXR2fQ-_vEyd0PW-sv4oNhCgMUL1cVv_XVlGATFr3CCk7aKORALIG-LJUQt_z_lGAQMucdWSnUaiZeurXR-fPU_oBkrTXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزارت خارجه به تحریم‌های جدید آمریکا
سخنگوی وزارت امور خارجه:
🔹
تحریم‌های جدید آمریکا بسیار فراتر از یک «جنگ اقتصادی» علیه ایران است؛ این اقدام تلاشی برای تحمیل حاکمیت فراسرزمینی واشنگتن بر تمامی کشورهای عضو سازمان ملل محسوب می‌شود.
🔹
هیچ دولتی حق ندارد بانک‌ها و بنگاه‌های اقتصادی کشورهای دیگر را وادار به قطع همکاری‌های مشروع با کشورهای ثالث کند؛ این تحریم‌های ثانویه هیچ مبنایی در حقوق بین‌الملل ندارند.
🔹
ارعاب اقتصادی برای وادار کردن یک دولت مستقل به تغییر سیاست‌ها، یک عمل متخلفانه بین‌المللی است و همراهی آن با محاصره دریایی، مصداق بارز عمل تجاوزکارانه است.
🔹
تمکین در برابر این سیاست‌ها، مقدمه‌ای برای بازگشت به دوران استعمار عریان و فرسایش کامل مفهوم حاکمیت ملی در نظام بین‌الملل خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/683217" target="_blank">📅 03:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aab003f1d.mp4?token=cCeuHNdzeHtkw1IyzY3SUifYLLOmTeTiVlAiSO8emst7HvnluR_XtryfKqwscZyt3RAof49UwWJ760I-xJZZWkvdvUrYdIsR5-B0Ee_fNPkL4-DTZ5uYgLz8XdAcB_0DKdhGuUBpZtp7uASezzrWrC_rKv9MzWQOX6CLHeEMsUK68WG7FedHBm3xvi2NXPFNP8VXbyQcm9vdClu6CUcCv_YDKihz1NXZBgiLJqVHJ2u2S2K7YgeDDtmg73_IFY0Zr0Pyze4QCLkLoNdS5lsuFc8NIG_S_9pyC7Q64w0SGkg398QhqwqWJ4RNGHokqi4DT4Znpx3WJmYLRoxXoRTcCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aab003f1d.mp4?token=cCeuHNdzeHtkw1IyzY3SUifYLLOmTeTiVlAiSO8emst7HvnluR_XtryfKqwscZyt3RAof49UwWJ760I-xJZZWkvdvUrYdIsR5-B0Ee_fNPkL4-DTZ5uYgLz8XdAcB_0DKdhGuUBpZtp7uASezzrWrC_rKv9MzWQOX6CLHeEMsUK68WG7FedHBm3xvi2NXPFNP8VXbyQcm9vdClu6CUcCv_YDKihz1NXZBgiLJqVHJ2u2S2K7YgeDDtmg73_IFY0Zr0Pyze4QCLkLoNdS5lsuFc8NIG_S_9pyC7Q64w0SGkg398QhqwqWJ4RNGHokqi4DT4Znpx3WJmYLRoxXoRTcCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: اگر در انتخابات میان‌دوره‌ای شکست بخوریم، من استیضاح خواهم شد
🔹
آنها من را استیضاح خواهند کرد. اصلاً نمی‌دانند چرا #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/683216" target="_blank">📅 03:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683215">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سخنان احمقانه ترامپ متوهم: در ایران هیچ کس نمی‌خواهد رئیس جمهور بشود  رئیس جمهور جنایتکار آمریکا:
🔹
در واقع یکی از بزرگترین مشکلات من این است که نمی‌دانم با چه کسی در ایران باید معامله کنم.
🔹
این تنها کشور در جهان است که هیچ کس نمی‌خواهد رئیس جمهور شود.
🔹
آنها…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/683215" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683214">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: به محض اینکه کارمان با ایران تمام شود، قیمت نفت به پایین‌تر از سطح فعلی‌اش خواهد رسید #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/683214" target="_blank">📅 03:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683213">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
گزافه‌گویی مکرر ترامپ متوهم درباره ایران: من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم؛ این یک قلمرو آمریکایی است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/683213" target="_blank">📅 02:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683212">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
گزافه‌گویی مکرر ترامپ متوهم درباره ایران: من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم؛ این یک قلمرو آمریکایی است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/683212" target="_blank">📅 02:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683211">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDOAwAXlIBalv0PKTjOOSytwEFzkGl-Rqb4JLWDHpKGQGMQy5HnvrrzrIwnvgNHEGFNm51bvmUTv_IZ1CUdVPzb511fqUhBwJR0sg06y6tW0qclnrFmBsO-sz2Zal86ZJZLqMLxupUbOjwqYuUsrKuDofOHaCobP7SUBXqkprMhs-GAe2tsfqtvWJKc_Xt8nK6Wdtkaao4Fl9LObI1j9JfXW_O_QA3rUoG9gM_CVErWSrVHPpLRxhT9vS3BN4mG3ICaL_RkUrRj15cNolxLEFiVM7ByDqU5T9_1-ed6jzr3hx-v30_wruWpJL1RsZ9iQgZat3W1JOvino5Suz9QrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر جنگ آمریکا کناره‌گیری می‌کند
🔹
منابع آگاه از تصمیم معاون وزیر جنگ آمریکا برای کناره‌گیری از سمت خود تا پایان سال جاری میلادی خبر می‌دهند.
🔹
اقدامی که در پی ماه‌ها تنش و اختلاف با «پیت هگست» صورت می‌گیرد و خلأ رهبری در ارتش آمریکا را عمیق‌تر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/683211" target="_blank">📅 01:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683210">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed38c6c628.mp4?token=VK9-qkEX2LWst9AViR31x-sKinhtgEJ8umkG9hdQpZ3VScG2410SHuyWLuG5HuQErv9xvYsoo-UOEb4cUWo3jUbWSuGPNENIzvW0Vos5s1xVlum0X4AAv3K_kvz_pNWqeVzcQCIn3nywzUUYj_J7PxcLTc8-0DKvBVckyGwknOdRBsimxvDVllSZoMpK6xe__R-zbLqRm5TzZwfPHO9ywgcl8sNSKDuYkq5ht2-xqVKG2H9JU1WVB0xdr6jJLnFGw1Dvw7mTPTigZOci5NuW1uoVTWXK-ihrNlpMXuIX0P120JSsPpyXaMqjIxeWaTN1NpvJYkTY-qoNba7_O9CMfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed38c6c628.mp4?token=VK9-qkEX2LWst9AViR31x-sKinhtgEJ8umkG9hdQpZ3VScG2410SHuyWLuG5HuQErv9xvYsoo-UOEb4cUWo3jUbWSuGPNENIzvW0Vos5s1xVlum0X4AAv3K_kvz_pNWqeVzcQCIn3nywzUUYj_J7PxcLTc8-0DKvBVckyGwknOdRBsimxvDVllSZoMpK6xe__R-zbLqRm5TzZwfPHO9ywgcl8sNSKDuYkq5ht2-xqVKG2H9JU1WVB0xdr6jJLnFGw1Dvw7mTPTigZOci5NuW1uoVTWXK-ihrNlpMXuIX0P120JSsPpyXaMqjIxeWaTN1NpvJYkTY-qoNba7_O9CMfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای مهیب انبار مهمات در لیبی
🔹
گزارش‌های دریافتی از لیبی حاکی از وقوع سلسله انفجارهای شدید در یک انبار مهمات در منطقه «الغیران» واقع در جنوب شهر مصراته است که موجب وحشت ساکنان منطقه شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/683210" target="_blank">📅 00:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683209">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
صداهای شدید در مرکز تهران برای جشن است
🔹
امشب همزمان با آغاز امامت امام زمان(عج) استفاده از برخی ترقه‌ها که صدای شدید شبیه بمب داشت، باعث ترس گروهی از مردم و تصور وقوع درگیری نظامی شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/683209" target="_blank">📅 00:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وضعیت اضطراری جنگنده فوق‌پیشرفته F-35 بر فراز آسمان امارات
🔹
منابع هوانوردی و سامانه‌های ردیابی پرواز گزارش دادند که یک فروند جنگنده رادارگریز F-35 در حین پرواز در حریم هوایی امارات متحده عربی، اقدام به ارسال سیگنال وضعیت اضطراری کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/683208" target="_blank">📅 00:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fcce2754.mp4?token=K5FZUdS14_KqR-WXnHSZeslu5hxT6II0dJyIsVL5LfVHLkcf86OzSao-HJQu2fXvdw7jeItggHuLcpBVQ4eIpAITLp-bGMvGqWsaQR5RHIUZAaCZuHxp1GATtTYsRJ_4Xq-QAliEblK-thl00biz2KTtsVB35_rSpNgKKjHjx7jfpsg6LN9RQAFee1MGs8lRZFsdf8ytDE-ksTKusFW_P-miqfLuxPhTwPv77y45jQurQ_kKfnh3HhUfKOSlVtHcf41pOkPiv5tqmTPQDPdfK2SuZnHG_Pd77UZ-CrkW8sTVVrX7NThe6W3ot0Ve4diYtRGiF-cBdcJeU0MvlDgLWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fcce2754.mp4?token=K5FZUdS14_KqR-WXnHSZeslu5hxT6II0dJyIsVL5LfVHLkcf86OzSao-HJQu2fXvdw7jeItggHuLcpBVQ4eIpAITLp-bGMvGqWsaQR5RHIUZAaCZuHxp1GATtTYsRJ_4Xq-QAliEblK-thl00biz2KTtsVB35_rSpNgKKjHjx7jfpsg6LN9RQAFee1MGs8lRZFsdf8ytDE-ksTKusFW_P-miqfLuxPhTwPv77y45jQurQ_kKfnh3HhUfKOSlVtHcf41pOkPiv5tqmTPQDPdfK2SuZnHG_Pd77UZ-CrkW8sTVVrX7NThe6W3ot0Ve4diYtRGiF-cBdcJeU0MvlDgLWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: درباره تغییر رویکرد ایران به سمت جنگ اقتصادی؛ آیا این نشان می‌دهد گزینه‌های نظامی برای آمریکا محدودیت دارند؟
🔹
ترامپ: نه، اصلاً. این فقط به این معناست که داریم می‌بینیم چه اتفاقی می‌افتد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/683207" target="_blank">📅 00:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ایرانی‌ها به شدت دنبال توافق هستند اما توافق درست نمی‌خواهند
🔹
ادعای ترامپ: من فقط توافق‌های خوب انجام می‌دهم
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/683206" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
دستاوردسازی ترامپ جنایتکار با ارائه به آمار جعلی درباره ایران
🔹
ترامپ مدعی شد که ایرانی‌ها دیگر پول ندارند و به پلیس و ارتش حقوق نمی‌دهند. همچنین تورم در ایران به ۳۰۰ درصد رسیده است و آمریکا کنترل تنگه هرمز را در دست دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/683205" target="_blank">📅 00:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENvadn7ZPh_ViYEik13FsWaN1cvo1BQTj3GKLLxo7DcYNsqyoNSWMqJVgdOUpa6e-NsZoixGzJ2gwNgPo8KiCeT_nLwh38eIYJL5NgbOgM_J4FIsxZQhb78l79hoEg8XriGtScQiu6fudxxrJcj4yCeR_4LokGCC6Z5DEgJaYuL5cuHN9aJ7BdD8gOS02d0c2jTBjLB3MND7dwWCA35xgkDDRL-jkTjSgDwVsBOEf-d61JHvQ-TSIzU4D8Sl7ZW1CmciqifO3M4UThExT9-TogjVuNkVVLYzTa4r3G6Jx_JB0cP8b8v5nnH-eMFm511j-zDoMLF8QqVjmO-Hja630g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار اطلاعات جعلی از سوی اسرائیلی‌ها علیه ترکیه
🔹
وزیر امور دیاسپورای اسرائیل، آمیکای شیکلی، ویدئویی را بازنشر کرد که مدعی بود ترکیه به‌طور مخفیانه در حال انتقال سلاح به سوریه است.
🔹
شبکه ۱۴ اسرائیل، که از حامیان نتانیاهو است، نیز همین ویدئو را با همین ادعا منتشر کرد. اما این تصاویر در واقع مربوط به سال ۲۰۲۲ هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/683204" target="_blank">📅 00:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683203">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
یورش نظامیان رژیم صهیونیستی به حومه قنیطره سوریه
🔹
منابع محلی از یورش نظامیان رژیم اشغالگر قدس به منطقه قنیطره در جنوب سوریه و تفتیش خانه‌های مردم خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/683203" target="_blank">📅 00:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683202">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcB_90slyn734zRDCEsP-5UBnrt7cdZJIof_UiMZORoO42t2AFTTU7ce_Lm3HDpIwm0axbxeoxr9ee4vKotyMIPNgwIsBkAxYvD3GnAw6v0FAKfBQIuBBz5M7guGMtvKZQVlfeDuLgmgnoStU64R3k43iUNLFLLenFtHKsQa8s8EoqnHOuxrU1rDmbTVamzoMFPDBZ9i9F2ijXc3Jfz_0AIBp8w237Ls_lB-qmg-ZF328Ig3vyukAtV6mKei1dIYX0caDUrWL99lJUKr2YeSU7ZYVZXSWTi-6rx43sEKxXc9Z12oISbna9nBL7bSLzMOgYLNjcUm5QaiVGfGEN1rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/683202" target="_blank">📅 00:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683201">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ترس ناتو از حمله ایران به بلغارستان
👇
khabarfoori.com/fa/tiny/news-3239213
🔹
ماجرای جمع آوری کمک مالی برای پسر و عروس معصومه ابتکار برای ماندن در آمریکا چیست؟
👇
khabarfoori.com/fa/tiny/news-3239408
🔹
کار به پیک پیاده در ایران رسید / درآمد ۲۲ میلیونی بدون موتور و بنزین!
👇
khabarfoori.com/fa/tiny/news-3239303
🔹
حرف‌های جنجالی شاکی پژمان جمشیدی در حضور ترانه علیدوستی
👇
khabarfoori.com/fa/tiny/news-3239280
🔹
اظهارنظر جالب یک روحانی: در هیچ روایتی نیامده که صدای داریوش حرام است
👇
khabarfoori.com/fa/tiny/news-3239216
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/683201" target="_blank">📅 23:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683200">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d311a6232.mp4?token=vYtSI6mJXnuFvtr38SMLXql0ZQ-FGhGr1Xq_L-hIsrXSi3qc7N-VgeEAh5SUmQlLX1xtNoMEYDNyGgTXihaBdEOZOqdNyil9y0i8Se-P-W0agBKmY5l_pD_jFmn0DkgNbT_TJlQpR6KX7V7c4XC-9dz8DCJF0nZjNcQeB2FXMtMV7SAxFgrUaLpSFVcjb4rej7iRGC69TkqhiCVerP6vBD46WMgsZx-acgNrAsi7O05v-SNPyJBXl4k2jf9Yh0MjLFyniglNjclvAkefSCpkdqiG3u6nFNF6DShpQIhApVxGMPZOzSbFjq22APDIl_rYHmOTFb6x1cg3sV5dyI2qbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d311a6232.mp4?token=vYtSI6mJXnuFvtr38SMLXql0ZQ-FGhGr1Xq_L-hIsrXSi3qc7N-VgeEAh5SUmQlLX1xtNoMEYDNyGgTXihaBdEOZOqdNyil9y0i8Se-P-W0agBKmY5l_pD_jFmn0DkgNbT_TJlQpR6KX7V7c4XC-9dz8DCJF0nZjNcQeB2FXMtMV7SAxFgrUaLpSFVcjb4rej7iRGC69TkqhiCVerP6vBD46WMgsZx-acgNrAsi7O05v-SNPyJBXl4k2jf9Yh0MjLFyniglNjclvAkefSCpkdqiG3u6nFNF6DShpQIhApVxGMPZOzSbFjq22APDIl_rYHmOTFb6x1cg3sV5dyI2qbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض مادران آمریکایی به کوتاهی لباس دختران؛ ترند تازه پوشش کودکان در آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/683200" target="_blank">📅 23:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683199">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpMbngukxT8JBuEN39xhBRrkljzv8g8Km-ISDcKg2dURYFBGe-Y2YI0gcwBkerWvt0nqqzxofrbBNHSakpOJ2vv1u46BubV1wdMdUJbqGXWSbcmIjN8nFep8bztbqNgBAvGwIJot0lAMwXz_GBflsurdN70lBXSElUqsAN8D8ZjEbaDP2Ists-MzhDbK7soet6wueq2fmI1DPhDMsobDlQhmHYmOeVBiwiMvx0Jo75Idj4EfJUDNARvplCik6mK67Js38GDlmmCw2CBOr74LWNu6O1JqsbyNHvsBhpqwwdNUgucB-bDZKwfYs6Xk_Vb-9J-nWFbwxl0WtAyftQdwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام، صفحهٔ «رواق دارالذکر» مزار نورانی رهبر شهید انقلاب را مسدود کرد
🔹
صفحه اینستاگرام «رواق دارالذکر» که به پوشش حال و هوای مزار نورانی رهبر شهید انقلاب و شهدای خانواده ایشان در رواق دارالذکر حرم مطهر رضوی می‌پرداخت، ساعتی پیش از سوی این پلتفرم، از دسترس خارج شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/683199" target="_blank">📅 23:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683198">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
پزشکیان: راهکار مؤثر، ایجاد ساختار مردمی است نه صرفاً ساختار دولتی
رییس‌جمهور:
🔹
در حوزه بهداشت باید آموزش‌ها را از مراکز درمانی و مدارس آغاز کنیم؛ آموزش به زنان و کودکان می‌تواند در این مسیر مؤثر باشد.
🔹
این آموزش‌ها نباید فقط گفتاری باشد، بلکه باید به شکل رفتاری و تیمی ارائه شود. باید به جای دعوا و تقابل، فرهنگ همکاری و هم‌افزایی را در جامعه تقویت کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/683198" target="_blank">📅 23:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683197">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
پزشکیان: وقتی دانشگاه بودم بحث‌ها بر سر اندیشه و راه نجات کشور بود، نه دعوای جناحی
پزشکیان:
🔹
وقتی در دانشگاه بودم، اصلاً بحث چپ و راست، مذهبی و غیرمذهبی مطرح نبود؛ بحث این بود که کدام اندیشه و ایدئولوژی می‌تواند کشور را نجات دهد.
🔹
چالش‌ها بیشتر در حوزه فکر و اندیشه بود، نه اختلافات سطحی و جناحی. شرم‌آور است که انسان برای رسیدن به جایگاه یا شغلی، دیگران را زیر پای خود له کند.
🔹
در مقابل، گروهی با علم، اعتقاد و تلاش خود، برای فراهم کردن آسایش و خدمت به دیگران تلاش می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/683197" target="_blank">📅 23:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaYle84aFLteA2usjQViIWnJUtCFWmdP9yLve0W4Yufp7BqTVmAQmkJ0sdKuTUZxzbVvlOtiBHRd1MB1oe2f4Sl4aSAibEmQiAxLiU9PgeeVCFpuqtJAK4cI6GcG5i_q6YPlMPJOOI0xhbBsOOihyqkW40QVMSu4mQ_fQHW0G5ZWeHTXjJnpy7ALdWTC4lwGUoeuD7K1KnQZS1sM6JnEk34pRRpg-P1mYVXNAxS_i0zlDhx8en1CO1aBMtY5DAptdX5CKgQbz4Y7UueQAzuNzlsj1PdhSn3d5cRVQNVYd_P6Lvw91GGCCVl-9pwg1P7VgxyqIY9Y5DPT9z5CRnf42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qh3xQ99GbxYYxTjKzNLgitFWmCpuAXq8cTrZm3SA4xeSof5X-ij9DaA6vQSXE6LgcAX_ZkkeYNMyfALjMWd9S5iiLdEQ26nsJOcYCglvfqF0GaTmAy9iVUozM2_R3vKGI4PUDu4rc48uyKfiIl2khx541ze5JMicARq7CEY90y-xSy2j5o5ikNEnY2AcuyuFd3qabuJcRbelrm41175tReIuBa6UzprzdH0Z8KgbKjYBUXluJPiTt1oRKVy2j6tmbnc7b-d8JjcbLzLxGuOsF7-NavnZHRmyWQxPnqHkeZhyCrXrXkhRdidkm7h1Cd6EUfTviRbMX0l8Zc-LwwI4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXkpEzat18cLGLGX_Hb8RsqJqKB89v4PQyP7LOyPanj9zlZs3GCuSrTPLLX-XZQW3wgFCnIpjaaH-y_4UD5i3rlNTuwErjtR7ALGYiAXpGF10X1mSoqcd7lyZSxK0nC-_GWJku-7AbMh2eM1gVSq1aYgHBZRfqnJ-v7P_qim_VaoaEO4FMb2MhwPVwxGuTCLaDDNb8de3GnVDqZLOGiicG7zGepscUrcTnTgYqjjSLVY-GAnYgbpB-qDkjz0aAy-9UZ-_UszjebBmZ3_j--UgE9it98OjmrIGTt_KdE6wm8pfNCEGGJDxvMbLp8ntwM00ZyoAw3alaKGJBMkLrU7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAkhmw8tcpfpgCqvHH6PrqNpfnGTAyOTD6Mi4c4wvNCaHTf3Vh6Uy3mpBC9lAUQfFk3KsafpLz8K0ozs8_-CHTETNqlsjliFqxZA6rNCEQ6sBhE7aJKR0asuHQhL6vu_Dm1NKbcP4S7sQf8_wUJGtdYlQBFArbG7Bb9h-aCWbFUXcMEHOTKfXsQTvTsjxSkHxAJYQ7o-8Q4_5idBuELmddZNqHinW2M4AVhkWx9nFP1IOOffw6i9nyEF9llju09nYC58tsmVVL4_t_KbBPm_AwQ87B3FWSx_e7b_RPWXrWPHI11iOsXIFEzFF104tUmsw-GctlgOWcMETrgkEA76fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T749nsDttiBYV15VIz1HCXfSuLrT60onVQbOLeLCpL1kPoUyy-PUkiuOkG6DPFF8gNGxuAp3-6A2lfWGojO5NTkvIGYoeTyCLqi7i5oKr010AgI52FmP4ERKc7HHtmLogfzOFj__1wNV31uj_IaLTD6oCMPKNJdHON9p6Ycwr4exqmpjM09tPPM0eJNAFtqY5uKfAWT2JOzfGBYgj1Na2T3X3-TT2r_yw6Hl5CQOGp4cfDp19T41s5RZXoLplujWK4HYBgDgbvFdeKOl0Yk7Al3VDJW46Pon6eAD9NB8JqYqbiF7L15fm7jrI731qd9TjMxw9pkYohVF_xVIZHCd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQvPdMwTXttcM6AH5xYd2DeGLf8_0wpXYq3gx74E1ywV9ZX_MtKOBA4Vs7Rvi2oIK4iU9aOK5phA5cNJOsyoisGh5Yxuxt-lacflcOFd--deT1bHriWL2w0LIIwj4v3tySkvfNqDyj-pe8wd3oSPlYfy6K2QCdJlR1CqZr7QwfUan2iWcMItjoTLAjPX6yOSxHW0EcspQ6y-dmH0AquLz41cYsAKF51KpyDJzyz--3QgrGsuCzduUIljge4R1ivUqE6rSub0xVNOkcZhmXoWBlYAznx1ZayyeSxO6EWJGacDJ_s6BuVrBfdqBAexDNfp9f77GGn_1nt1EYZvZJZ2kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند ترفند خانه‌داری که زندگی روزمره‌تان را راحت‌تر می‌کند
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/683191" target="_blank">📅 23:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrZzWG_LhPH25DlUy9w1pXGeS7y2Nl4Gt3VPQdKl9HXBzgPtjXTBfErD4qg05-fdONM0bWKsCj1emCJLUhaPuujtFD2uOLNijM3K9oOkjwo6WgFBIFla2uI1UIT6ixjR8VUAqAXsG4MPKiWNDANC_7kzNsCiNa7EFcXujADJIwXR24nYgCKc_3zIp5k59_wUj5i-NxOLFCDzoZFfDUMux4YVLuH10-XmyP8XYFmu2XliXJokOdE0J1Fi7H23FP97Ed2g234mRDzEZ3yUtdScLwQllDkQsyQQgI3dwESTMl9Ld74MJaBCx3dHgWz55GeLMsB33b67tToQXpt6V2MJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/683190" target="_blank">📅 23:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر جهاد کشاورزی: دیگر قیمت‌های دستوری تعیین نخواهد شد
🔹
مقام ارشد ناتو: هرگونه راه حل درباره بازگشایی تنگه هرمز به توافق با ایران نیاز دارد
🔹
اکونومیست: نتانیاهو برای بقای سیاسی، خطر انتفاضه تازه را می‌پذیرد
🔹
رویترز: کمبود ظرفیت پایانه‌های نفتی ونزوئلا باعث تشکیل صف طولانی نفتکش‌ها شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/683189" target="_blank">📅 23:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683188">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36536d542.mp4?token=CIOFKi6VouQKnfrvFLanpHA1H2DGdtwnSQMnsjyKtP3hsKOrl5lD1uh-kwFDnHBXnr8o1VJxRgYDR3nlMXLzADXJ3jPvAPWxFNOqt7OxEWCvPn_yGNTELUEoterx0RSVk5sPawQsqDY8AfebWw9fUFL_-1PN48biTLGeQCzuV_vnfz4XIqS8mYoG6dkTm3YlB32EBHLANvMUhjDDA0_XeKMwnX5t44P0PDI1OawCZU-JkQGhkc1T5mOl8kggYMNDnXfwkuYoKq8CoW5tfWZfP8v51bM0TjoT6bWvNxh1W4upJoTEZSJnbWWoREM_nJJ6O5v8kmPo3PftjaAKonlYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36536d542.mp4?token=CIOFKi6VouQKnfrvFLanpHA1H2DGdtwnSQMnsjyKtP3hsKOrl5lD1uh-kwFDnHBXnr8o1VJxRgYDR3nlMXLzADXJ3jPvAPWxFNOqt7OxEWCvPn_yGNTELUEoterx0RSVk5sPawQsqDY8AfebWw9fUFL_-1PN48biTLGeQCzuV_vnfz4XIqS8mYoG6dkTm3YlB32EBHLANvMUhjDDA0_XeKMwnX5t44P0PDI1OawCZU-JkQGhkc1T5mOl8kggYMNDnXfwkuYoKq8CoW5tfWZfP8v51bM0TjoT6bWvNxh1W4upJoTEZSJnbWWoREM_nJJ6O5v8kmPo3PftjaAKonlYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک، سخنگوی وزارت دفاع: یکی از عللی که سال گذشته و امسال نمایشگاه نظامی برگزار نکردیم و رونمایی‌ها را متوقف کردیم، برای غافلگیری دشمن و برای صیانت از اطلاعات و اسرار صنایع دفاعی کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/683188" target="_blank">📅 23:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683187">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRr0Do97Aow6mBrRn00ZxtQRLj8JyYiruR4VbeSsBVaJDhaRUiGPQpheuURmKMS5Ej4wwD0sCubSqp7f_vjJDvbS4YWWRINjSZzorhamxStoeVWRdhj33z-xJGeOn3k3raUDInPybIM3A1TWaxNccWMIiXA0oWGh34sniOxMNPqIkcnVDZTE6MnJDVox9weAazHnxYX2-YbbC2R57mBASTE5ifD4bvocGp4jM2iOcLLyqAGnWpT--71ZdLgTnO7ZUZsC_NJOUolyTreJTzQTxL3nJWcKF1zY5pqM2EER7hR7HGKCnJPLqxpbrMNS5Wu4UPKeB_lZDU3kj09iyX33Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه وسیع انصارالله برای تنگه باب‌المندب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/683187" target="_blank">📅 23:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ea7675b3.mp4?token=cbcwh0rqAa1V0Sx41wMXgUQn9z0Z3THZflNrn0wHZ-j3TfeoLZy0A_63F0VisLMDsib2nrm1Lx-doPjJjTdXa_JbQQVVHLny0RvUS_nQvSoC8OasW1Len5hdWREUiBk3XZbZaLHi9McUnKLeRg9BViQGSdQSA-hMpqg0JcGpMGVlmeO2K9553ZJLWTE_jCh-XfoWBZAmaA7We6ahVClmMg5IfcyiCk9xCbyqlSrIUo_PSOUtNTAyMh3wsw8HseSlmY_NsNXUHahhMQVQwyAxwRwlF7yJXcGbhEp8HWEHsP5WNvturx-NGdeieWWCL-c_5omszMPXNcbxe0n6dS3wFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ea7675b3.mp4?token=cbcwh0rqAa1V0Sx41wMXgUQn9z0Z3THZflNrn0wHZ-j3TfeoLZy0A_63F0VisLMDsib2nrm1Lx-doPjJjTdXa_JbQQVVHLny0RvUS_nQvSoC8OasW1Len5hdWREUiBk3XZbZaLHi9McUnKLeRg9BViQGSdQSA-hMpqg0JcGpMGVlmeO2K9553ZJLWTE_jCh-XfoWBZAmaA7We6ahVClmMg5IfcyiCk9xCbyqlSrIUo_PSOUtNTAyMh3wsw8HseSlmY_NsNXUHahhMQVQwyAxwRwlF7yJXcGbhEp8HWEHsP5WNvturx-NGdeieWWCL-c_5omszMPXNcbxe0n6dS3wFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر ونیز چگونه ساخته شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/683186" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFM1X4KtUjz1wh2sYjMuYlcTH__oG0tattUgXjQ9eAQ05CnVFnzzo0VC-04quS9kRPGoop5cgRrwb7fDlhY8yuKoMxn0WJcIGINZUg81udIjoD-xhb1x5VNLZtvHniWDXdtD-Sz21OZjLaE7LVXoNcLYwSQwMxbfW510UaIGsZOXOwtDld7D4z6kr8A6I3UsWwvrn2afvWtzvv3plRzf4coAdbAPMysnHiAtV7SMcJceIG2i61_NV8_i4xmdrbgX2UUCDNdmCEXBMw2Iqcl6_FywyEOn2-vuDvdWvY2mSETIIjTkQa3nz0wp2ifoStKF_aj3duTPMnldnLetMUrzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت وزیر خزانه‌داری آمریکا در حالی از اعمال «سخت‌ترین تحریم‌های تاریخ» علیه ایران خبر داده که تصاویر او در کنار همسر هم‌جنسش، جان فریمن که در این عکس پشت او قرار دارد، بار دیگر مورد توجه کاربران قرار گرفته است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/683185" target="_blank">📅 22:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683184">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تهدید فدراسیون فوتبال توسط تاجرنیا با چاشنی کنایه به پرسپولیس: اگر تصمیم بگیرند جام قهرمانی را به استقلال ندهند، از طریق فیفا و AFC اقدام می‌کنیم ولی لابی سیاسی نمی‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/683184" target="_blank">📅 22:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UryGa-bXNJkGsbihavRz0ZLNUD10zDtScItn05hozEu7TK_WcJhZSL-sodm5CjdbgEik9m75cWCptYBDqexxq4nfX1l4uH-A52HEle2rjz873h9-VMrHslmZ3AR6qqK8jfo8KwV_typBbQ-aBOg6-6j1aSlfl1bXIcV_jGIwLqDkpQ35uasHxbsvxUr6D7jGVZlGbQaaAjVaiGtmqASJrVUWhBam60SqKAwBs6UXL8oe5l7eFU9-Cexhk3qDwY9Sc67U3v7RPe4EWm3W2ZfzAPMZvLzimtLiynBm1eWRU4jBmIvhlA5DvRk93nWRoLdjQoDm8--UJxdwkiEhAMOt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرستی از با ارزش‌ترین شرکت‌های هوش‌ مصنوعی دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/683183" target="_blank">📅 22:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683182">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29cbf6bd8e.mp4?token=R8B_SMxsFg26fNZ3Z2yTNF_rEWpZ5mFWIS_eG6zgmJztYJXMjCbqMq7jNyW-UAd51VZyVVMMoEN1nJN7oYsy3_tP6Hvy79oNL3W-Xay96r8q7W0pApJUanFFKCbfSfSyIPyOHzELdy0F0j7ahJDAbjvN_-JoYaox8ee4PDuVUZloifiCUukcKik60iHP-ZtYVKSTvi4QH1qPwLACnwOY4Pzv7vR3Ldy_7K03QBWhcpiT_JwGAmowoIPbrESDD2p4b_Q7xa3m_9cfmSdjRBSi-deimm09pIq5Yl8JacJ2ACKa40Ja9EPuxR2i6JJ9m7p37QQe9cwHalDNj0qltfOPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29cbf6bd8e.mp4?token=R8B_SMxsFg26fNZ3Z2yTNF_rEWpZ5mFWIS_eG6zgmJztYJXMjCbqMq7jNyW-UAd51VZyVVMMoEN1nJN7oYsy3_tP6Hvy79oNL3W-Xay96r8q7W0pApJUanFFKCbfSfSyIPyOHzELdy0F0j7ahJDAbjvN_-JoYaox8ee4PDuVUZloifiCUukcKik60iHP-ZtYVKSTvi4QH1qPwLACnwOY4Pzv7vR3Ldy_7K03QBWhcpiT_JwGAmowoIPbrESDD2p4b_Q7xa3m_9cfmSdjRBSi-deimm09pIq5Yl8JacJ2ACKa40Ja9EPuxR2i6JJ9m7p37QQe9cwHalDNj0qltfOPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر سابق فرهنگ ترکیه: ایران برادر ماست
تامیک کمال زیبک:
🔹
ایران فقط از آب و خاک خود دفاع نمی‌کند، بلکه به باور او، در خط مقدم مبارزه برای آینده بشریت قرار گرفته است.
🔹
ایران دوست نیست، برادر ماست و شرط انسان بودن در این روزها، حمایت از ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/683182" target="_blank">📅 22:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748c9bb82.mp4?token=IOc85Ybl19m2hTXvO6UXJfuFJgDdRcRR8WIj_97678kXhp24Vvl39-rF631hRrisrbXK0WLtt43SZHcGC0gQmfoRKcxpjtlvzf-PTeAGNlh0kR1PBKpM9KfrUrONfL2fgvl9KPKGHsUNNYBFaAIH9hnsP1rCCT8g7QM0ch1mSS_Rpfzg9hO2CzbJzLA0rs4K-wnDEmQUxCzCw-BhlgsENT-tkjqJuVv0CPa9MxP3hIyZPzoplVoyqXb9ZMfPsyH25-9_0RDH_VORUvFwzKURyPt7WjrgxKStmt44-ZQovyoC47_cmdmu74fdnsbtFPqwZmQl3YyAJ5_CGbr1SbfOWyd0Jt0KRs-TyU0_4mCYhBoI9zYKGuWfUHeCL9Jl4aidIBzqSk5BlF45WfPIvGNeSzoE2Ep7cq6qy1BfP_DajS4MqwF3GDht3q83nuDvnEXnxzrc9WEPPvvKdoesL-ONG5KxwZCXMBh1UHo_FUHU0q9mjhSY31FuCW0avJqSARmyLFXtVL0bukW07IgekxXbcrIiP6puNlcW_jXQizLDmIjQshosKo2bjSRDsRzLDZiaH28Z6r9PKplLvFF7OvzPCXf1YcTcsCMqMzBiCeUVCqgmfiRvXcC9ynrbtYJObweVu9rcYHECDOWoBQBBu63dprWmcE-ABmXNgOibDDcA-ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748c9bb82.mp4?token=IOc85Ybl19m2hTXvO6UXJfuFJgDdRcRR8WIj_97678kXhp24Vvl39-rF631hRrisrbXK0WLtt43SZHcGC0gQmfoRKcxpjtlvzf-PTeAGNlh0kR1PBKpM9KfrUrONfL2fgvl9KPKGHsUNNYBFaAIH9hnsP1rCCT8g7QM0ch1mSS_Rpfzg9hO2CzbJzLA0rs4K-wnDEmQUxCzCw-BhlgsENT-tkjqJuVv0CPa9MxP3hIyZPzoplVoyqXb9ZMfPsyH25-9_0RDH_VORUvFwzKURyPt7WjrgxKStmt44-ZQovyoC47_cmdmu74fdnsbtFPqwZmQl3YyAJ5_CGbr1SbfOWyd0Jt0KRs-TyU0_4mCYhBoI9zYKGuWfUHeCL9Jl4aidIBzqSk5BlF45WfPIvGNeSzoE2Ep7cq6qy1BfP_DajS4MqwF3GDht3q83nuDvnEXnxzrc9WEPPvvKdoesL-ONG5KxwZCXMBh1UHo_FUHU0q9mjhSY31FuCW0avJqSARmyLFXtVL0bukW07IgekxXbcrIiP6puNlcW_jXQizLDmIjQshosKo2bjSRDsRzLDZiaH28Z6r9PKplLvFF7OvzPCXf1YcTcsCMqMzBiCeUVCqgmfiRvXcC9ynrbtYJObweVu9rcYHECDOWoBQBBu63dprWmcE-ABmXNgOibDDcA-ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سهم وزارت دفاع در قدرت‌ ملی و قدرت‌ دفاعی کشور چقدر است؟
🔹
راهکارهایی که شهید نصیرزاده برای وزارت دفاع داشت، استمرار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/683181" target="_blank">📅 22:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7984717235.mp4?token=Gs64vgOs7HZgOVSimbVdg4JR_OhTVvXkrDBfrD7LpbroaqGALS7zJGCHng2MjG321bnEL2Q34it2F8ySrhUa9CORvuqSvQH3xycdXtjqAk0sXfj7wSp2Lqr5gBr74pGIQL92IXAqQrL8wu3nZQMTF95D_jFXP_tvjUC4CRddt2Xo9uxJvxM4kMVYKSWvtT1q29NJjHhTR11APRDYFJ4Ya--qPwmjjhslYvqfx6E3aISEGp9xAppw7OVTOQ0SeARSwkH3YNKxernIMDAz5ff8n_UrpHYet2jmZBlG4XPy1dtDvukJwOPqh70Rfdulk4UaCqaip0sUkTh4Zs6hvzjYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7984717235.mp4?token=Gs64vgOs7HZgOVSimbVdg4JR_OhTVvXkrDBfrD7LpbroaqGALS7zJGCHng2MjG321bnEL2Q34it2F8ySrhUa9CORvuqSvQH3xycdXtjqAk0sXfj7wSp2Lqr5gBr74pGIQL92IXAqQrL8wu3nZQMTF95D_jFXP_tvjUC4CRddt2Xo9uxJvxM4kMVYKSWvtT1q29NJjHhTR11APRDYFJ4Ya--qPwmjjhslYvqfx6E3aISEGp9xAppw7OVTOQ0SeARSwkH3YNKxernIMDAz5ff8n_UrpHYet2jmZBlG4XPy1dtDvukJwOPqh70Rfdulk4UaCqaip0sUkTh4Zs6hvzjYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از اصابت پهپاد به تجمعات سعودی توسط انصارلله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/683180" target="_blank">📅 22:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5FcTu9j8_6Gt6z3EbMzMqn_dY3hQqv7eCQNN83OkIRH0P9P4Lj4RfiHqvLb026S7sDUISTIXOC2W_ar7fsBweD_OibJquBFviL9YuMNKLnaiGDNjHvwsidex2I5IXwUl5AsX_khuYhPWhOO76krf508L5aIObR3mzPkANbhonOxV8QQGXS3BtpCLbXefiFT8j03HaXCHhlWay_QN9H_B1z268-UOwxpV-7MK8cLexYRyUR49UGDyT_YlUfvOe6oZFmNAoMYBEFiYDk-i1n5hm07o19P4rC1v_bXJJObLCrn5w3ewCbwn3jcp72JIjS6VyRaSzV4aUDAv1NLRb1wYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
ایلان ماسک: رسیدن بدهی آمریکا به ۵۰ تریلیون دلار برای کشور بحران ایجاد خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/683179" target="_blank">📅 22:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683178">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227375ee24.mp4?token=N7M5fkI3YW2ymY85ap2eCyhldKhmfkIkpwAX8DfKe1EkpEN-FkQ01_yTwHspxC5lwPXde3i6HXqRKHObzVjZjxaK7GNjFuNBeDNLETatkMA3KFqksssjBL2loJk8uE2BaxNXPC940hgyU3qt5ec8FyDuitOawCAAJY3XxULbWLLuKifuaLiZPZnFFloyDa-uV1cdYxZ-0Es1rPI0yMi_3XjnKwrfaWEZMJXiBU0RwvL6IpVB4OTT6cunUCOww9A5R_h6NE9XPqZmT27KbY6PFu9ym-EtsSMpmac62-8yxSFe3bAqKkuJIo860ghsvftgLBGNPUZzirgdXW3izTWGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227375ee24.mp4?token=N7M5fkI3YW2ymY85ap2eCyhldKhmfkIkpwAX8DfKe1EkpEN-FkQ01_yTwHspxC5lwPXde3i6HXqRKHObzVjZjxaK7GNjFuNBeDNLETatkMA3KFqksssjBL2loJk8uE2BaxNXPC940hgyU3qt5ec8FyDuitOawCAAJY3XxULbWLLuKifuaLiZPZnFFloyDa-uV1cdYxZ-0Es1rPI0yMi_3XjnKwrfaWEZMJXiBU0RwvL6IpVB4OTT6cunUCOww9A5R_h6NE9XPqZmT27KbY6PFu9ym-EtsSMpmac62-8yxSFe3bAqKkuJIo860ghsvftgLBGNPUZzirgdXW3izTWGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع:
در یک سال گذشته، میزان تولید تسلیحات و تجهیزات دفاعی در کشور ۲ برابر شده است
🔹
در جریان دفاع مقدس ۴۰ روزه، برخی محصولات راهبردی و اقلام مورد نیاز جنگ، بیش از سه برابر افزایش تولید داشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/683178" target="_blank">📅 22:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683177">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972614d705.mp4?token=TIBCBqFeW31xedMzmAiD_pdoYbGzRpJYRKpAQGw5twW8WN-EV8nDKNxom94JgJvPQek9EZYwbRVdTsxUR_hZICnkps6H86kdwtyIUSW2iU0VOlTBHlmwXSb6boBaPkYkNIig3AXDLp540OUfwRAwwVGODL265yHlur7OKr3xI5U4aNo1CU6HpU1QOKY7qpCl2oGwUFIjBDra2C59cwFfdwM8BspatRpJvYYhH0IaXsIqlnUSmAh3gqZYVsqoT-0edb8r6Ssq7LZLyDBawafMmtRAhO_JqrQ6wuwM5W3bjdS-ySUqclTnOH7FDpiIrjBoTL1vSvwCQor6AhEpzgLOmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972614d705.mp4?token=TIBCBqFeW31xedMzmAiD_pdoYbGzRpJYRKpAQGw5twW8WN-EV8nDKNxom94JgJvPQek9EZYwbRVdTsxUR_hZICnkps6H86kdwtyIUSW2iU0VOlTBHlmwXSb6boBaPkYkNIig3AXDLp540OUfwRAwwVGODL265yHlur7OKr3xI5U4aNo1CU6HpU1QOKY7qpCl2oGwUFIjBDra2C59cwFfdwM8BspatRpJvYYhH0IaXsIqlnUSmAh3gqZYVsqoT-0edb8r6Ssq7LZLyDBawafMmtRAhO_JqrQ6wuwM5W3bjdS-ySUqclTnOH7FDpiIrjBoTL1vSvwCQor6AhEpzgLOmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید فدراسیون فوتبال توسط تاجرنیا با چاشنی کنایه به پرسپولیس: اگر تصمیم بگیرند جام قهرمانی را به استقلال ندهند، از طریق فیفا و AFC اقدام می‌کنیم ولی لابی سیاسی نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/683177" target="_blank">📅 22:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683176">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113caef9ab.mp4?token=mXrlYSdpYHPiq5IXZpXQceaiM-0LYCxGvxjzQ3WiQ5GbtoCmYVVgcP4U328nQR9rzDWt06HAQcdSAPSiZyK2ivNRU1Nc_Y0qa_1Kp5O4NM_sfNbpUzH4s-U9csR5MCcjdn9j3gAMFt_auBjXI3CotixpvS4Q7B_F9plDASItJ3U19Smldh8XkJsHTmnZwY_bl0MPqwB4EmQDk34sSMY9vRAu_NgkhTMSvWbIPIvTD233aDU1DwSTbMdH_sn4RWxwVC9Aqh6lHDjct9ueXuMte2SbY2cbIGiU-2v8lqFZ_hP-9c8M51cOFqxjXOU_BZ64Q_6LTDe5-jCa3De1KqNXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113caef9ab.mp4?token=mXrlYSdpYHPiq5IXZpXQceaiM-0LYCxGvxjzQ3WiQ5GbtoCmYVVgcP4U328nQR9rzDWt06HAQcdSAPSiZyK2ivNRU1Nc_Y0qa_1Kp5O4NM_sfNbpUzH4s-U9csR5MCcjdn9j3gAMFt_auBjXI3CotixpvS4Q7B_F9plDASItJ3U19Smldh8XkJsHTmnZwY_bl0MPqwB4EmQDk34sSMY9vRAu_NgkhTMSvWbIPIvTD233aDU1DwSTbMdH_sn4RWxwVC9Aqh6lHDjct9ueXuMte2SbY2cbIGiU-2v8lqFZ_hP-9c8M51cOFqxjXOU_BZ64Q_6LTDe5-jCa3De1KqNXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: یکی از ویژگی‌های برجستهٔ صنعت دفاعی ما، سرعت و قابلیت تولید محصولات دفاعی است
🔹
به میزانی که در میدان رزم سلاح و مهمات استفاده می‌شود، با سرعت جایگزین می‌شود
🔹
تنها راه سلطه‌ستیزی و مقابله با قدرت‌های بیگانه که می‌خواهند استقلال، موجودیت و هویت ما را مورد آسیب قرار بدهند، فقط قوی شدن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/683176" target="_blank">📅 22:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683175">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6313bb63.mp4?token=qy5x2JnUZJL_fAF0gWjRQr6OWeMoZ1kMwpl1eOn53O3qfXE-MMfX5T50HPensxsWm8d621PPtK3azJnkbG9jKkdtUNdhvoLoVSQxiSnSJb_qxpePbX4n85xRELXOpuO1p5DtNT8D-_2kTndMNAMyQtJbxK5PlQ0lMTXbmU-khnspIcu0d54sop7xI-i0HcseDd-B5mU0qpmGri8rXBiidIr3jQh9InPPpPNGrRYnmImlyLIg409o5_QXZA-uivFUfnrLudK3oiJ4YJRUt-c2IKO9rA_x-p21iKlQgZaHcF7xTmWgBfPvxvNODYpw7bKS7ntHZQaVSJdTqiRG5x8WDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6313bb63.mp4?token=qy5x2JnUZJL_fAF0gWjRQr6OWeMoZ1kMwpl1eOn53O3qfXE-MMfX5T50HPensxsWm8d621PPtK3azJnkbG9jKkdtUNdhvoLoVSQxiSnSJb_qxpePbX4n85xRELXOpuO1p5DtNT8D-_2kTndMNAMyQtJbxK5PlQ0lMTXbmU-khnspIcu0d54sop7xI-i0HcseDd-B5mU0qpmGri8rXBiidIr3jQh9InPPpPNGrRYnmImlyLIg409o5_QXZA-uivFUfnrLudK3oiJ4YJRUt-c2IKO9rA_x-p21iKlQgZaHcF7xTmWgBfPvxvNODYpw7bKS7ntHZQaVSJdTqiRG5x8WDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع جنجالی برای دفاع از مادری که به قتل سه فرزندش متهم است
🔹
تجمع گروهی از فعالان فمینیست در حمایت از زنی که به قتل سه فرزندش متهم شده، واکنش‌های گسترده‌ای به همراه داشته است. حامیان او بر ادعای تأثیر داروها تأکید دارند، در حالی که دادگاه درباره عمدی و آگاهانه بودن اقدامات او بررسی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/683175" target="_blank">📅 22:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
میکروب‌های زمینی در ماه زنده می‌مانند!
🔹
یک مطالعه جدید نشان می‌دهد که میکروب‌های زمینی می‌توانند در سطح خشن ماه زنده بمانند، البته در حالت تعلیق این اتفاق برای آنها رخ می‌دهد.
🔹
تحقیقات قبلی نشان داده بود که سطح ماه برای زنده ماندن میکروب‌ها بسیار خشن است. به طور خاص، یک مطالعه در سال ۲۰۱۹ نشان داد که اشعه فرابنفش و گرمای خورشید بزرگترین موانع برای حیات میکروبی در سطح ماه هستند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/683174" target="_blank">📅 22:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683173">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نخست وزیر عراق: هیچ قصدی برای رویارویی نظامی با گروه‌های مسلح وجود ندارد
فالح الزیدی:
🔹
برخی گروه‌ها سلاح خود را تحویل داده، ارتباطات سازمانی خود را قطع کرده و به حشد الشعبی پیوسته‌اند؛ با گروه‌های دیگری نیز در حال گفت‌وگو هستیم.
🔹
اجازه نخواهیم داد این کشور به عرصه تسویه‌حساب‌ها تبدیل شود. دولت قصد رویارویی نظامی با گروه‌های مسلح را ندارد./جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/683173" target="_blank">📅 22:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683172">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGLqn9NQ36-cvRTgmpdZ39AV4hwT2n2m6nvJKUhbtN-3AafxAKwq3IIeq3dlTo_XHQ43XrQphWt3_4NSesmXxTDu8epMeJaCvlsfkT6lgxrqGvoupFVfWZ5c97LkevieppZz5uYMZ8pcaUGDlVhWGxikIZ2ATbl__YcfA53hhcaFwIzcxGv4Zbtorcl97ylQfCixkUORJH7micnTip13wI9mMsqIWzuqrf1NsMMLZQSIakMk6PCHt7rKn2Zg8KBdmQSsnJg8S51H9rQXUqonrpiQzQJ8gI_kKic3SaCzbPjn_xa3GGVzccosEnxSWbI1w7crbyW7_y2HHILZChhM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چجوری بوی بد پا رو از بین ببریم
؟
🔹
ترکیبی از آب گرم + جوش شیرین درست کنید و پاهایتان را ۱۵ دقیقه در آن قرار دهید باکتری‌ها را نابود می‌کند.
🔹
قبل از پوشیدن کفش کمی جوش شیرین در آن بریزید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/683172" target="_blank">📅 22:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683171">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUNiWrll5kD-W8UkfTGb8sLkp39Y6BHaoMU2a9AN3S6b1jkty1Tv-dhtXInN3x47oKah8qaVNShbGs_RnRl0eQxXAyahfXvntL8bUNd9ZmxDNAWrJLxNS8vdM-YL_xZpATH1gdsOtDlOE18odJUpROz9rJigUnsskDSmF_GMttZ5hAdLFEfGOUEhI6zcIJ9NcaTWs1h320r9yQ86fO-K7vuD8NyCqgYY0CWH-djnoLoZ3fBn5gTI3dtiXG1BJs1YkAxuTS8rTUvuOHg96GCWddzW35csFIBQsms1vyo13Qb1lPywe2YGL6zcd3ib7qQuy1dXtxIK7SsoR6vmL_ULBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: نگرانی مردم اروپا از وقوع جنگ و حملات سایبری، آنها را به نگهداری بیشتر پول نقد متمایل کرده است
🔹
برآوردها نشان می‌دهد هم‌اکنون ساکنان این اتحادیه یک تریلیون و ۶۰۰ میلیارد یورو پول نقد در خانه نگهداری می‌کنند؛ این رقم در مقایسه با ده سال پیش ۶۰۰ میلیارد یورو افزایش یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/683171" target="_blank">📅 22:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683170">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: اجازه نمی‌دهیم اردوغانِ دیکتاتور سوریه را اشغال کند
🔹
نتانیاهو با متهم کردن اردوغان به دیکتاتوری، یهودستیزی، کشتار کردها، پناه دادن به حماس، اشغال نیمی از قبرس و زندانی کردن مخالفان، تأکید کرد که اجازه نمی‌دهد او دامنهٔ تجاوزاتش را به سوریه…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/683170" target="_blank">📅 22:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683169">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B43oz-Jvwq78uXGiZYbBgeK_H5D6H5YVBSHh4ufIySUZhKsAjf1qwYGeAz4aCMovvpYul5w7nuDWiOTBrIVFxgwbdgYQqYl6TzUQM8zrCGdVNEYh8sgmxB3xbkmsM4XcXo5hVGgrv2Pv-RL1MVRujk3Hn1wx4RJ-217qvkVmihIHl7j6P44g3lA6pye4-S6uFwveM-1SnP-_Cm5VTtRyjwzu7rN2WgyBw06o4sNZuYb7ALxJCh16WNomvOCZ0ibWrTUcddrX3oviclF-10SdGCDxkpFGfmrpM4c9QyLS-a5E7h6rf1TKI9tVChFkoh4hMQTmcNG31LIe1OEFaKP6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
اگر دانشجو هستید یا در ۶ سال گذشته از دانشگاه فارغ‌التحصیل شده‌اید، از شما دعوت می‌کنیم در این نظرسنجی علمی درباره کنکور و قبولی دانشگاه شرکت کنید.
⏱️
زمان پاسخ‌گویی: حدود ۱۰ دقیقه
🔒
پاسخ‌ها کاملاً ناشناس و محرمانه است.
پاسخ‌های شما به شناخت بهتر تجربه‌ها و دیدگاه‌های افراد درباره آموزش عالی کشور کمک می‌کند.
برای مشارکت در نظرسنجی، لطفاً وی پی ان خود را روشن کنید.
🔗
لینک نظرسنجی:
https://harvard.az1.qualtrics.com/jfe/form/SV_6MsiAUIGfXgJZQy</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/683169" target="_blank">📅 22:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBA68UWtDho0wptMKglYEGNamGNu1700QRIwa29AcpqT1HqpCmNf1A9X-BGxJZXx3m8_8YLKbno6K59cwM8D-EtqsF2gjEKKZnI-WrkA-RoyHnV3EFUcBn9khLJkfKx6at6QvtxMjsMyBkXTH6al7gJTuvxeSeWFc0l_84Y3qcf3p5r9JnI9T_lBhjWi0Hf8VdeLJwEelVvtOdge53z-PUMjCQrsBmA6VK7jhG384CvQ6CREb5G8sly6EOtH7yL0JyTCOtSxwgfUb2MbsckCn8lJH9tPw68D3DnH6gj9wQGw9n2lQums6kuzIROrJm7zhrRyjDf5L6yfSTDB-0ZMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgpaUiDvfpqECTN74aQhPynoB3kAesPmOq7WWn7jP3V54oy5v9Y2pWXsKkK-kcCxKwEtVP9EDooKpOwiDL0WirSihRiykJPuCl1K_le_J4XlvkPKU1AK_8-_Z7C27WWMxa_eWhaczHZdQ9sHP6N4N6ZclODSQLIYiMdK_57rR6ITcEAVwyQ_0MzbqnUE_uNiWYAku4NgoKX2uLhSPQvy76pNPYggNHkhp4AmdO_XmmpLDug3lM7bq9Jj3ZiU2AJnFrW2EosP8WizdYlyOjINM8Pj2Yhz9HNEVOaBON7Xu0MuYVYRsD_50Tb4MrZR1tBRlp_pnM6sXtgUHxu4T3EGeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5da8055a.mp4?token=ZmzuQeXjndOa-AEWOt1SF83UrlgW477iI0VEEwSHPZ2jqo7AvB2QIJPXSFpKCyY2TwNv0rSg1QveU2O787Aq2vhVS0MtCuRITVqEErOK5FdGWI4PAM3HZ0yk4iXI_QYlnrYRTt8ACv-Q1_B9ZgfOyC992Qu_grOrXujbhekw01FWuxBK-1vVHoD5tx8weHksq-t6nb-Tvds9RUBX8kg0ma38r-I8DNXOdaY4P1e0f77Z_zbIM_yUnKUUWiQllSZfup5nz49Hz6cPshImRN7if9rVLLGVXoNMBOjJVOxp60djvCfDlgrL_Wb8y8o328otRNhBNApndiv8GAWnGXVvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5da8055a.mp4?token=ZmzuQeXjndOa-AEWOt1SF83UrlgW477iI0VEEwSHPZ2jqo7AvB2QIJPXSFpKCyY2TwNv0rSg1QveU2O787Aq2vhVS0MtCuRITVqEErOK5FdGWI4PAM3HZ0yk4iXI_QYlnrYRTt8ACv-Q1_B9ZgfOyC992Qu_grOrXujbhekw01FWuxBK-1vVHoD5tx8weHksq-t6nb-Tvds9RUBX8kg0ma38r-I8DNXOdaY4P1e0f77Z_zbIM_yUnKUUWiQllSZfup5nz49Hz6cPshImRN7if9rVLLGVXoNMBOjJVOxp60djvCfDlgrL_Wb8y8o328otRNhBNApndiv8GAWnGXVvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
#پک_استوری
امامت امام زمان عجل‌الله
آقا مبارک است ردای امامتت
ای غایب از نظر به فدای امامتت
#امام_زمان
(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/683163" target="_blank">📅 22:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683156">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda5519a1b.mp4?token=hsgiWuGKI4ZHcZ53c5Ub7ZdA0YIUniI9tklnLbCWXugd0EwrMykDjOPI-B1FZufB3vaPhx3WbHO-mj7hd8mS88vSPLZ9d7bNX11xwdfq4apDNv9FWKrxzvHdJctsPghHRlx0_s1jisXxQdAdPfdFQ1J3Zo7MN64z7PN2ElCFuYpRQZel_u2XsIbT75mf7oJaXT0Vng0Hs_Wz4_8lXnfReL1i-e3E6CtobBcSHoa9pIHU0pKdTjRwthvJeuxsihzqNSJmer9mzD9io6nhnfkYLUxZ1JFE_U9mt0d3lpBJAij61zxvULEXhK3KNKWd0fhuFmmijL1hV2Td96SdCKkKSx2hQik_mSdrDW23WzOdgXzfUBgFx2GzwhJEVVwrKBPc6nLYy51nTCj42t9971UwnEMFJa4Dg_FwnOdUwfBjtKOv5dYjY96haRO83CAv7c0-KmAOdR3Yu4z1xqqY81mSv-EZrSsN8346VPsdotyZjsXlIiwFyBxzAP504d3txQS8pPYgyrHsMfSEkBetm7gOzB05Tgg4I-bmSQHxB3SW3BFnOTQwkvmu8vWE821Q4nj_knbrR0IeQNK_-AUMqsf75zFGa_J4kEG0A6PImroD9Q78lgHvLyUepmv97ZKMUAFrC8XcbHrphw8hsb0NJGG4yr9CC78_gjjJoJt0CB19KqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda5519a1b.mp4?token=hsgiWuGKI4ZHcZ53c5Ub7ZdA0YIUniI9tklnLbCWXugd0EwrMykDjOPI-B1FZufB3vaPhx3WbHO-mj7hd8mS88vSPLZ9d7bNX11xwdfq4apDNv9FWKrxzvHdJctsPghHRlx0_s1jisXxQdAdPfdFQ1J3Zo7MN64z7PN2ElCFuYpRQZel_u2XsIbT75mf7oJaXT0Vng0Hs_Wz4_8lXnfReL1i-e3E6CtobBcSHoa9pIHU0pKdTjRwthvJeuxsihzqNSJmer9mzD9io6nhnfkYLUxZ1JFE_U9mt0d3lpBJAij61zxvULEXhK3KNKWd0fhuFmmijL1hV2Td96SdCKkKSx2hQik_mSdrDW23WzOdgXzfUBgFx2GzwhJEVVwrKBPc6nLYy51nTCj42t9971UwnEMFJa4Dg_FwnOdUwfBjtKOv5dYjY96haRO83CAv7c0-KmAOdR3Yu4z1xqqY81mSv-EZrSsN8346VPsdotyZjsXlIiwFyBxzAP504d3txQS8pPYgyrHsMfSEkBetm7gOzB05Tgg4I-bmSQHxB3SW3BFnOTQwkvmu8vWE821Q4nj_knbrR0IeQNK_-AUMqsf75zFGa_J4kEG0A6PImroD9Q78lgHvLyUepmv97ZKMUAFrC8XcbHrphw8hsb0NJGG4yr9CC78_gjjJoJt0CB19KqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پایان سربازی هم تبدیل به یک «مُد» اینستاگرامی می‌شود؛ از یک اتفاق شخصی تا نمایشی برای لایک و دیده‌شدن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/683156" target="_blank">📅 21:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683155">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45944f0cdf.mp4?token=HJMF7t4AMfbdIxdv4aQv3gh8LulSNPVHIIeRY8zyY6Y0SB4PLKr2iL0Gw80vR8DX5y3Tc2vuFNZNr6uJEGFkDcenkmO8sSsQ_VD37BWMlijPN_X-bxlus13i4pS1fFMCtqZzJw8ZqqMOJWQtPiFM3yX39NUuCdugDpNCAlaB7dBEJBLapbHkjvNdiX7MiKo8F5i4aCQfCJsal5BKTxMPTqngHtVniT-HVguhRT7uzpExeX5RaZDUxRT3AcD6IcFSB3iQYfkWl9wvn2eONK3hyqv125k3fIRdl7_IMZBwf7IuFQkp72lSApvKxsJeVLWTiHstVK21ih4vNsn3ak4Gfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45944f0cdf.mp4?token=HJMF7t4AMfbdIxdv4aQv3gh8LulSNPVHIIeRY8zyY6Y0SB4PLKr2iL0Gw80vR8DX5y3Tc2vuFNZNr6uJEGFkDcenkmO8sSsQ_VD37BWMlijPN_X-bxlus13i4pS1fFMCtqZzJw8ZqqMOJWQtPiFM3yX39NUuCdugDpNCAlaB7dBEJBLapbHkjvNdiX7MiKo8F5i4aCQfCJsal5BKTxMPTqngHtVniT-HVguhRT7uzpExeX5RaZDUxRT3AcD6IcFSB3iQYfkWl9wvn2eONK3hyqv125k3fIRdl7_IMZBwf7IuFQkp72lSApvKxsJeVLWTiHstVK21ih4vNsn3ak4Gfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانیان در تاریخ بارها ثابت کردند که خلیج فارس و جزایر آن، از جمله خارک، با هیچ سلاحی تسخیر شدنی نیست‌‌...
ادامه ویدئو
👇🏻
https://youtu.be/PkNQz2D9nTY?si=MZvjgT4CBM9FkUZQ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/683155" target="_blank">📅 21:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683154">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حکم نهایی نظام وظیفه؛ بیرانوند از مهرماه سرباز است
سردار زاهدی، معاون نظام وظیفه عمومی:
🔹
علیرضا بیرانوند از مهرماه ۱۴۰۵ سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت./فرارو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/683154" target="_blank">📅 21:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683153">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-poll">
<h4>📊 به نیت سلامتی و فرج امام زمان (عج ) نابودی شر و کفر چند صلوات میفرستید ؟</h4>
<ul>
<li>✓ ۵ صلوات</li>
<li>✓ ۱۴ صلوات</li>
<li>✓ ۱۱۴ صلوات</li>
<li>✓ ۱۰۱۴ صلوات</li>
<li>✓ ۱۴ هزار صلوات</li>
</ul>
</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/683153" target="_blank">📅 21:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683152">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادامه گزافه گویی معاون ترامپ علیه ایران
شبکه اسکای  نیوز:
🔹
جی‌دی‌ ونس، معاون رئیس جمهور دولت تروریسنی آمریکا مدعی شد که واشنگتن ابزارهای فشار لازم برای مقابله با ایران را دارد
🔹
او از ادامه حضور آمریکا در منطقه با بهانه‌ موضوع هسته‌ای ایران اشاره کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/683152" target="_blank">📅 21:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683151">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هند خواستار حل‌وفصل تنش‌های خاورمیانه از طریق دیپلماسی شد.
🔹
سی‌بی‌اس: تحلیل‌های اقتصادی نشان می‌دهد ۲۵ درصد از نیروی کارگر آمریکا «عملا بیکار» هستند.
🔹
رئیس مجلس و هیئت پارلمانی همراه وارد تهران شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/683151" target="_blank">📅 21:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683150">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkgHx1fgekMR8xnn4FVui2aGCDpxhRg-hrxmZBZDOE8fRUlJu5H9wWFmXz6YkKMq-wEqGOB33yfC0jACx7NGtv05TDBY-5DDUtHtpD6FWzP7vxQyxn5Zhi50QfzioiJ7YkvPyGMPNxRC_IDgBRYF90plHDvNf0-eiIxbNIz43nWXeD2say6oDTaUQAa3L9S7nJQSvIH7LbxDj0_Vvb2LVkYasgQUraLvDyNooT053yml8N2QrDS6VwWS45XcO7Dt7I2UyKOiwQdHcRnmmvwxeri4a5S_IFrYccTrWQKao3qMjy5FeMbDHCg13ujda27BdJgikfYcDPmTElFfuxgHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی انس طلا بیش از  ۲۰۰ دلار گران شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/683150" target="_blank">📅 21:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683149">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198312ec77.mp4?token=hugbt3TOSmbofsiwNFBZsVw73dJaXs76zFGZQmwEod7I-Z67atcBlfOfL9yG64BGn1xOUbMeUGWFFdXsq0Lusb1OUAh4dxnmDh6a2j4KuWn-KADysx-LXFexB7c1hU21C3qgIBrbOIa03JUAOVB9p4RJRn2hMe8nyqELqC8GQ4CMGHgFm4b3nlk6yS5WVRf_KN4X9I1qydB643lqxTkfWm3irH7xpQCfbbuLZqG2JY496pjLa4Fdyj8Bf2GnnqMpJXDCvNKdx-qddV4XZy14dMn0BtGSZgDb_jfMHibG1xePqkSoRvsywwDIhc82ojOmiUETE-EouSiu7CQlxGQPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198312ec77.mp4?token=hugbt3TOSmbofsiwNFBZsVw73dJaXs76zFGZQmwEod7I-Z67atcBlfOfL9yG64BGn1xOUbMeUGWFFdXsq0Lusb1OUAh4dxnmDh6a2j4KuWn-KADysx-LXFexB7c1hU21C3qgIBrbOIa03JUAOVB9p4RJRn2hMe8nyqELqC8GQ4CMGHgFm4b3nlk6yS5WVRf_KN4X9I1qydB643lqxTkfWm3irH7xpQCfbbuLZqG2JY496pjLa4Fdyj8Bf2GnnqMpJXDCvNKdx-qddV4XZy14dMn0BtGSZgDb_jfMHibG1xePqkSoRvsywwDIhc82ojOmiUETE-EouSiu7CQlxGQPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شقایق جای خشخاش را می‌گیرد
دبیر ستاد مبارزه با مواد مخدر:
🔹
کشفیات مواد مخدر خلوص کافی ندارد، واردات مورفین هم گران در می‌آید برای همین مجوز کشت شقایق برای تولید دارو صادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/683149" target="_blank">📅 21:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683148">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ایران قصد دارد بزرگترین نیروگاه خورشیدی جهان را با ظرفیت ۵ گیگاوات در اصفهان احداث کند
🔹
در حال حاضر، رکورد بزرگترین نیروگاه خورشیدی جهان در اختیار نیروگاه خورشیدی می دونگ در چین است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/683148" target="_blank">📅 21:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683147">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp7yBP28-kZMPAnIy6rf0y3x6ZiC6_CpMBUXgXqr8CsnMyOnva4kgzpykD-WhXz2d1RZpsWlp1f6dp7QvvdmI2pJjqrwN9_LQBH0UzO1ZqU5kG83-LTVRUuW5csWzzAWOpnjWaqa9IUgW-RFYIlqj1LLqCWsmPX0Q5HNrcPKMYZ5YEV5PiTjhp3jsBaYYXvkEYVB_j-zR0Pz7qfAf23_Rsm_r92tglthEteaRuZtzrkPp9gyj81BktN9AVpXLTJkjw62i1Z8ISAzqAnSUP1U5PM4hTqqk748ASZyW-xJBCI5ha6jPMRUvpw6nqxLW383PnMpMC7EMB8BT4z62mj78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از جنجال کریدور مرموز در جنوب تنگه تا شایعه اختلاف لحظه آخری تهران و مسقط در مذاکرات/ عمان؛ کلید جنگ یا صلح ایران و آمریکا
🔹
همانطور که عمان می تواند حل‌کننده مشکل و درگیری ایران و آمریکا باشد، به همان شکل، قادر است این اختلاف و درگیری را تبدیل به گرهی کور کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239391</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/683147" target="_blank">📅 21:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683146">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxXokfVnw5tUTnnnPX6QAngT61RWXFjdEFmR_tGc8jQG1liZTNMC6O0vHT-hnpTAEIel2B6VjTh6Hko_fIaItKuRZf26_jEzdfo2xU5e1QSxABazLOnRRSy5g1nNYSXyzUyElYTAOn4-mXdwunyzKqMd-qrYUN5Hb8YuwRHwUnXCqqIZHdsI1CUEVjFPIBY_FNtuK-0X44e1jPJj9wqRXe8mH1hg4PXPXWOv5xQ84KVOo-VBB7ZbtKvmo7L_IfVBhgYPiFWxfDJSfcipFop0sBztZS4f8B7bPOAptgN26GKu1QJyNpF5fDUIpDCGTgtpd66C31OCItRIwFxIP1XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی : احمد بابایی
▫️
با حضور:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای : امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/683146" target="_blank">📅 21:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683145">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
خیابان‌های نیویورک پس از طوفان شدید به رودخانه تبدیل شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/683145" target="_blank">📅 21:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683144">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e4525ee9.mp4?token=JXwqExefPzGM9mSZ4zRux416d5ZLwuOx7ikd_l-cG3rNrRo73COpgX2CtPSIwuzGEgZU-uzTFQpE9HlPsLF5gOs2HeFqhlUAx7UCTxS1tvVHckoNCh9Icws_0vHDghsq5G1bsGrYtl6liRpj0KNRpnpj0LKcUlG174y43NDKaUWpJfDnWblDE50qyIYREKtDO4gCSPfwrt8Ui6-K6y4-uZz12TSEVpyVLeGRkYDflV2ULt1zRLVLrjIL3NuRC0N8WtqbxWdM_QSuJus2MEx1B5sa8mHdgLm9QRUDJytzY2Eh7iKJfyqnT2h8m8cX5H6vTpJGDWR_sjtnNNTu80bl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e4525ee9.mp4?token=JXwqExefPzGM9mSZ4zRux416d5ZLwuOx7ikd_l-cG3rNrRo73COpgX2CtPSIwuzGEgZU-uzTFQpE9HlPsLF5gOs2HeFqhlUAx7UCTxS1tvVHckoNCh9Icws_0vHDghsq5G1bsGrYtl6liRpj0KNRpnpj0LKcUlG174y43NDKaUWpJfDnWblDE50qyIYREKtDO4gCSPfwrt8Ui6-K6y4-uZz12TSEVpyVLeGRkYDflV2ULt1zRLVLrjIL3NuRC0N8WtqbxWdM_QSuJus2MEx1B5sa8mHdgLm9QRUDJytzY2Eh7iKJfyqnT2h8m8cX5H6vTpJGDWR_sjtnNNTu80bl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطوری با حقوق ۳۰ میلیون پس‌انداز کنیم؟
#جیب_من
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/683144" target="_blank">📅 20:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683143">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd4c75b53.mp4?token=aq607iI53-xxdbnHnRolyHV6Pznwwv2UwNogwPgORyAlVSsvYDi8ZfJXTuzskw-50pcJl_SYy0o0ZUOagZBMItjLDf0_Cv9is9eULUVkdbGLfv1IBuINOj77tG6wVdcOWbcb7wDbMl-Wd0zsn7MBMpL9LdwqA-ni103LdYaVpT6ZEk7UYzMiiUl_6MmfttdYWh4zIxS-MI9tgVfYVmtElcZaG7GLASXh9HGz3L4Ov9BDEBK0hCkSSm63GbRV3Dflo8UZeIiaJcAyLkzszgPFTRKv_LgrGAhtfhkzkOfNFTSfNcktk28A5t1wuAKQBgIZ-6olX2VpBeeZHrYZQHgxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd4c75b53.mp4?token=aq607iI53-xxdbnHnRolyHV6Pznwwv2UwNogwPgORyAlVSsvYDi8ZfJXTuzskw-50pcJl_SYy0o0ZUOagZBMItjLDf0_Cv9is9eULUVkdbGLfv1IBuINOj77tG6wVdcOWbcb7wDbMl-Wd0zsn7MBMpL9LdwqA-ni103LdYaVpT6ZEk7UYzMiiUl_6MmfttdYWh4zIxS-MI9tgVfYVmtElcZaG7GLASXh9HGz3L4Ov9BDEBK0hCkSSm63GbRV3Dflo8UZeIiaJcAyLkzszgPFTRKv_LgrGAhtfhkzkOfNFTSfNcktk28A5t1wuAKQBgIZ-6olX2VpBeeZHrYZQHgxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابلاغ پیام رهبر انقلاب به مردم عراق در سفر هیئت پارلمانی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/683143" target="_blank">📅 20:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683142">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf5d544c.mp4?token=ACA6OqMZxlLf5awfy7zPhUCSuZDxDa4fVkHQmvaMHvQj1Yj_moBK6Js9GqxKfTolVCsCvy7QF73liWGQMt-EMjrAb_kzArN6c3csPy-fGV-DS8k8-B6xcgLWsAhPJVgnQ-t5i1iZBQQNnThc7SMiv9Qds6RoWdSnjVuEZ-KNUaQJCvnjQbTbLFGch62DolNgZrVEVzp26fn4KooRbWmIsHa4RebPw8p4yxlgZ97mtpHZddagXCXVJPtRN1AqaRQoyLaWzYDMS0OL4I22v8bL83fyZe0CD1ouA8ihnpDMEPjTz3AYI9t7eFYqWPkl-0He-PKajZQbFDJdjhMYhDM3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf5d544c.mp4?token=ACA6OqMZxlLf5awfy7zPhUCSuZDxDa4fVkHQmvaMHvQj1Yj_moBK6Js9GqxKfTolVCsCvy7QF73liWGQMt-EMjrAb_kzArN6c3csPy-fGV-DS8k8-B6xcgLWsAhPJVgnQ-t5i1iZBQQNnThc7SMiv9Qds6RoWdSnjVuEZ-KNUaQJCvnjQbTbLFGch62DolNgZrVEVzp26fn4KooRbWmIsHa4RebPw8p4yxlgZ97mtpHZddagXCXVJPtRN1AqaRQoyLaWzYDMS0OL4I22v8bL83fyZe0CD1ouA8ihnpDMEPjTz3AYI9t7eFYqWPkl-0He-PKajZQbFDJdjhMYhDM3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنباکسینگ ربات انسان نما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/683142" target="_blank">📅 20:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683141">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymFLpl9-tp_gARPOm6v7iEizVnPEyT3_-NRD38IfjrF7WoSMpNN1eqrV4ypqghVqJrHAVcxrjORqwI0y90ThCs_P4Ay1S0FP18Fttz72k679_MctsqVtPnc6osc2l9aaP2TuklNW5vkRXUH9j0C6r23W1Vrksjckv3f_-IM2DElGcS4YZb1qW2ttCk2gXo6FEp6NxLiyoWYR2XOKPzqbTOmEIVSFCICcrjXtXoGNW--V0FMvCTOISow-Mql6tzxwnZWbUT-H7zTRIqHbaEww-qlzjEG7VJstrcDPL8baQuI-7qIaCKR3RZZvRT0VHBhWYgqM9wxf__eq8XTJgIz9MXeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymFLpl9-tp_gARPOm6v7iEizVnPEyT3_-NRD38IfjrF7WoSMpNN1eqrV4ypqghVqJrHAVcxrjORqwI0y90ThCs_P4Ay1S0FP18Fttz72k679_MctsqVtPnc6osc2l9aaP2TuklNW5vkRXUH9j0C6r23W1Vrksjckv3f_-IM2DElGcS4YZb1qW2ttCk2gXo6FEp6NxLiyoWYR2XOKPzqbTOmEIVSFCICcrjXtXoGNW--V0FMvCTOISow-Mql6tzxwnZWbUT-H7zTRIqHbaEww-qlzjEG7VJstrcDPL8baQuI-7qIaCKR3RZZvRT0VHBhWYgqM9wxf__eq8XTJgIz9MXeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بانک ملی ایران: ۹۸ سال اعتماد، فراتر از اعداد و ارقام
🔹
بانک ملی ایران در پیامی خطاب به مشتریان خود، از رابطه‌ای سخن گفته که به گفته این بانک، طی ۹۸ سال گذشته بر پایه اعتماد و حفاظت از سرمایه مردم شکل گرفته است.
🔹
در این پیام آمده است که سرمایه سپرده‌ شده نزد بانک، صرفاً یک عدد نیست؛ بلکه حاصل سال‌ها تلاش، امید و زندگی مردم است و بانک ملی خود را امانتدار این سرمایه می‌داند.
🔹
بانک ملی ایران تأکید کرده است که این پیوند طی نزدیک به یک قرن، همچنان پابرجا مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/683141" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683140">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VberFzRMDQSx-zOVu32wc46aDpdvTF3xAbOAtjw4tiGw_ZE2Yw4qpSOe65lf4UAeos-tZOgEzjnA423inos8VtHdmqI9Jt0t7hzZZCHTNLWc6OO8x2P8q-HxB8ZKzJrLma8Rl3TTcc_DYZYR22OhEvCm6ZrlzGylhik62nDsrvS0LPJYbghfk3mAERzQtTSmF5KwQqL2rlnPN9W0gpS2vE0IqeQ5Dh7YpfpgIG5ZiLA9a4o75Wjlrb1MNbjd8aQ7VltoyKHij8xrcHGJ1Uk2O28Xu7djlU9BRcVl8AMT-fADlyHxNs8PdQ2jrgIyfH_rXSFw02-Bb6FElloIot5abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوراکی‌های ضد بوی بد دهان
🫢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/683140" target="_blank">📅 20:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683139">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9fc42fbc.mp4?token=cWECzKNIo8WAA3P7EzIihvGNaVS3q10uV5A73ZBkHoCcjfWNOv1mx_uxY9SKdDH9w8OTpUBInXUFwVygdMeE_5-NVQ8F0ujdjmR-AfjrOjQwpJtHlROwIwQEdFI2MOiMAdzZen7bDET0DTKOAkZFuJYj-NXIsiSnVA4kyfzyp2DknlitKX6z8ozOGzuT6_CmCijTdy2nzpj9_9KNjH360juI-QaevJW8GsczfiFy2IC5r52Vhed1joV85qZ1yCmxLUpgfbiVXb8NIo4VPJLnFHHEoqO6C4EFRCg3Z9xmjAuvFw6mRkaiTKo5r7cVdYCkiXIEpWdN9Snz5lm9P2awoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9fc42fbc.mp4?token=cWECzKNIo8WAA3P7EzIihvGNaVS3q10uV5A73ZBkHoCcjfWNOv1mx_uxY9SKdDH9w8OTpUBInXUFwVygdMeE_5-NVQ8F0ujdjmR-AfjrOjQwpJtHlROwIwQEdFI2MOiMAdzZen7bDET0DTKOAkZFuJYj-NXIsiSnVA4kyfzyp2DknlitKX6z8ozOGzuT6_CmCijTdy2nzpj9_9KNjH360juI-QaevJW8GsczfiFy2IC5r52Vhed1joV85qZ1yCmxLUpgfbiVXb8NIo4VPJLnFHHEoqO6C4EFRCg3Z9xmjAuvFw6mRkaiTKo5r7cVdYCkiXIEpWdN9Snz5lm9P2awoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قصد فرار ترامپ جنایتکار به پنج طبقه زیر زمین به بهانه ساخت سالن رقص
ترامپ:
🔹
در این سالن رقص تا حد زیادی یک بخش نظامی هم محسوب می‌شود؛ با پهپادها، پناهگاه‌های بمب و همه چیز دیگری که در آنجا داریم.
🔹
این سازه تا پنج طبقه زیر زمین امتداد دارد. می‌دانید، تقریباً ۶۵ فوت، یعنی حدود ۲۰ متر، به عمق زمین می‌رود."
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/683139" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683138">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826d7da14f.mp4?token=hGDJ7RKHGjdq7RVBXNddnPb-0F-k0DayavDWruvQB75-7KwzKStouwOhL-Q-MCo8qhD-NuQG2hJI0xDizjgHE7SznK5DZSRT-DAMYhQD69sL3p2Hu7-z6snVydjpsYpTFF6mGDbSnXdlG8QC9pA86iykI8KjnZmcb3KjifZGBGW_BLQNDAxAjifZ8k28yYujAiZkyc731DU2Gaz6gtcDnpnUYbrtB6ib9VxXX6eb0QaakwCchWwNVY4NaXrgcS8i_7swH3__vO7N6LLmpG3jsJAiuua9xqrAFuASl6JrRe8fkq1oNZDniR7Ryx-fwAUyUeiAydhQlcX2nr9tj3kFbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826d7da14f.mp4?token=hGDJ7RKHGjdq7RVBXNddnPb-0F-k0DayavDWruvQB75-7KwzKStouwOhL-Q-MCo8qhD-NuQG2hJI0xDizjgHE7SznK5DZSRT-DAMYhQD69sL3p2Hu7-z6snVydjpsYpTFF6mGDbSnXdlG8QC9pA86iykI8KjnZmcb3KjifZGBGW_BLQNDAxAjifZ8k28yYujAiZkyc731DU2Gaz6gtcDnpnUYbrtB6ib9VxXX6eb0QaakwCchWwNVY4NaXrgcS8i_7swH3__vO7N6LLmpG3jsJAiuua9xqrAFuASl6JrRe8fkq1oNZDniR7Ryx-fwAUyUeiAydhQlcX2nr9tj3kFbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاینده‌رود زیبا؛ جایی که هیجان و آرامش کنار هم جریان دارند
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/683138" target="_blank">📅 20:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683137">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
آب سرد سازمان بین‌المللی دریانوردی بر پیکر ادعاهای ترامپ درباره تنگه هرمز
🔹
دبیرکل سازمان بین‌المللی دریانوردی، آرسنیو دومینگوئز در مصاحبه‌ای با شبکه خبری بلومبرگ ادعاهای دونالد ترامپ و مقام‌های دولت او درباره باز بودن تنگه هرمز را رد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/683137" target="_blank">📅 20:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683136">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K42WGrWJfl-50KYay7ZVblYdjAv62ovzbZF47kRTS3YZy5affJByOq6L8aKdilzRm2TrR4Q324P7AzSomZ-CLYrWEvMJklSiHasDKFIsX7HDPgZFE24Mp95zZNx7Bhc8ycJ00v6jBaZA_QihBE5-cS_2u6I-BijDB7iQgDvui9lTQX_sYYfpAP5LXgKMlhJhY14GOT-JRvqkWVYbLFt-o5StIfUTF2ibg9LLDcZ06RZaPa9vSlJxboNNqE-6WFSx1B3wDIZjwGc_idovzB9pwALxkvox2nsKNq_fcspBwkzzMYjJ9iINM7U4ePy0g7AJ-rUupSjzMqVxd3YxO1uqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا اعلام کرد پرتره ترامپ روی سکه جدید یک دلاری چاپ خواهد شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/683136" target="_blank">📅 20:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683135">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcu_pVJRYPNDGe4AnE5Z8ZKBRH3T2MKXBLa1GG1389x74MW4IMO8KjpfWKbDd8-RuvZ2sbLRPzu9WBEsi_A4kJBRoIWsK0YnDCez55t-uf3p1WTZDknYvuU2ZWsoj3slmprAgrWghKNP-B9tX5-Zz0RwlfH-fzFB1QAy-wfY9JhIYNtYYz_4SckqnzNd5XQAgmWQv9DRhjZ-AWDQA-JOcCBqtDBPKAirxvr9cnDjzc5MaKpDUrh0o7eY47IwAM6MAHPMLM_6RITF_SVqEKG1BpVlAFqG8DIVcoQHA-jE13iZXw0n3disGRR_-Ns-csqMAL7gIMxDGQ3m7z8kRq_aIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا با عذرخواهی از مردم ایران، منطقه را ترک خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/683135" target="_blank">📅 20:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683134">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EylqiMj-yS5E6wxCNZUe3Dj7wPKi4oZk4-q8yQfHjsWCtxLhqMqED4Fh8csdpyiUzcEYvY5U2KB2c0Ap8szDdkNC92G6z1T1QJhBYv64cAAfKYmRs6eHdKsFkOZ32TeVlD5gsqHgcyNhHOg7rLKclIMB134YwNQee09PZu7INkWcnYEZNAkguQ7pGaf4Xq1U-Gd1vIGQ-M-lOFAF5T4XNTUcJ58GBYc8N_PocOr0Lo28SZDE3LqLUAt-W275uzBxjFvPXxk9_7Hmi1wlxqIyU5ZTTx9BAVSk7cjLtNj6uDT95VpltSpLpvakxJe1SS8rYWU6AfLjqL11BxW_HdO18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص‌های سنجش بیماری چاقی
🔹
چاقی از بیماری‌های مزمن و شایع است که علاوه بر تاثیرات فراوان بر زندگی روزمره افراد، باعث افزایش ریسک ابتلا به بیماری‌های قلبی-عروقی، دیابت، کلیوی، کبد چرب و آپنه انسدادی خواب می‌شود. تشخیص و بررسی علل بیماری‌ها، اولین مرحله رفع مشکلات مختلف هستند و بیماری چاقی نیز از این قاعده مستثنی نیست.
🔹
اکنون که با دردسترس قرارگرفتن درمان‌های نوین و موثر مدیریت کاهش وزن و بیماری‌های متابولیک مانند داروی تیرزپاتاید (Tirzepatide) داروسازی دکتر عبیدی با نام تجاری زیکورپا (
®
ZCorpa) و داروی سماگلوتاید (Semaglutide) کوبل دارو با نام تجاری ولوریتا(
®
Velorita) ، مسیر درمان چاقی در ایران هموار و آسان شده است.
برای مطالعه متن کامل این مطلب روی لینک زیر کلیک کنید:
https://abidipharma.com/health-items/obesity-assessment/?utm_source=telegram&utm_medium=post&utm_campaign=pr</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/683134" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683133">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تماس تلفنی وزیران خارجه ایران و عمان درباره اوضاع منطقه و هرمز
خبرگزاری رسمی عمان:
🔹
وزیر خارجه سلطان نشین عمان و همتای ایرانی وی در یک تماس تلفنی آخرین تحولات و شرایط ازسرگیری گفتگو و مذاکرات را بررسی کردند.
🔹
وزیران خارجه دو کشور، اوضاع تنگه هرمز را بررسی و بر ادامه بحث و بررسی‌ها برای رسیدن به تفاهم تاکید کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/683133" target="_blank">📅 20:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683132">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRzdhRhhfNIVYpAsExon_lJyOL7g_sew0z0RD5npoym1rfZJkzBddwzQPAa9i4s8Sr59g6Wr7Qt83vdo2cTirS3kguzhuJxXJu563DoHsAsCP19UYfRch2IGxFOEEp5FCGviBqm-MCEYDgfBLSFrB4YkJUhwSGC5MrznkrrHaP-3Q--fISHUwasI-90K1DJg_Gx4_ZOMMRg7mXNrUVSOP4RJuV_vkWkB_ZgWBgvE-AtO5O921WXaYBED_JmwwbzneiVINjfVZnIKlX5D95PlQTabwqA0XLfBycKTmGYOWCKnwedzDmxNkHL1zjot2_tGrdY043kPSw6OY3pPwruKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگه از شر لکه‌های کفش راحت شو
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/683132" target="_blank">📅 20:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpF6doZg2MHT8f3_lEMtehdPssJ6PoyQQg-vqpbMc8npVH5xxzbpNeCPe2V7opQ6lHYHG9gcYqlDxZb_ijWY5u5uBnbsS_d5D71Upwn5WNEtf0AqvKzIl1tbYwEu5hZkuOVFbh9LNrFF7vUwpFlDyPbLiTgspN-pxqz29Vg8kQLuHgAHNXE0Vd-rDqInURstM9tHw6_GQll3EOzwaEQ0qjq9E-ylD2gCw61-FfN7bqeBioeSxesKLbWZZi2jdPlypKeTIA3yD-AipeERnCw41sAx_LWyXSl_rJTfXj8pvijkLvLgVXWuuh04zwBfTtKf5YM4YNscL9j_a5BQEtPX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا ترامپ واقعاً می‌تواند مانع تجارت کشورهای دیگر با ایران شود؟
الجزیره:
🔹
کارشناسان حقوق بین‌الملل معتقدند که هیچ کشوری نمی‌تواند بدون مجوز شورای امنیت سازمان ملل متحد، یک تحریم همه‌جانبه و کامل را علیه کشور دیگری اعمال و سایرین را به رعایت آن ملزم کند.
🔹
به علاوه تحریم‌های پیشین نتوانسته‌اند جریان تجارت ایران را به طور کامل متوقف کنند.
🔹
کشورهایی نظیر چین، ترکیه، پاکستان و عراق همچنان به مبادلات تجاری و انرژی خود با ایران ادامه می‌دهند و منافع ملی خود را به فشارهای واشنگتن ترجیح می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/683131" target="_blank">📅 19:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1a148fb2.mp4?token=BQS9Qd9bStbZ5JULO5dilvwkck7uOEzgV3SIP5JCwuAiyTGqxdHpKsoH3ylkdW8trT4DaIX36lz-JSoGIhE6o1kzBqgkaA-0PQIbJZ62xSyyiG6v1nQyXNA0U764jkLsaz__WWWxZ8B_ICuXl3qevew-xrIJ0GjuC9nV9yDxxsSz7MEax10VOD0Jjm3Mue84z2rlp4hD1qYD0jvUIe17rbOa0ZmG6F440XnU4FDXo_pwojrMpzNbvWuwt3c5UWyGYZi6Az7WDiNQJZDHs3Ki-Ltn70v-SgvQ-qKtiNh1AHAB6vsDfT4huY6NYcZfkf7jho8XwMyv4g3fxoGn_hQC3RkG_ZUutw4WdHUOK9YHT1MCn9Fzg0pN-mXgaEEau6yeucXcqC5mtlq9pr4kkZP_grn3CsSvCmn3OC39bAc_mGfeuQ2t01lVfgybBhhGDxB_aKsormj_8wM2K36oonjmZSfHm3Cx022w-0WaJKcPAJ5rvYgHG5b_hK_Rk72imug6Q5zhf8x4ZAu3qyXb-iHwZ6x6U9R03ATJJZt6fJHgWEl6MrNYmMw_Jhp_3Ieqx9lrHD4PS10AvG7tarUaDejmBnKhziTli6Km5-iIM7znEnTwSFbJc9R5Fhzw9SCD7GxSL8F1dDCjDFl2U06MeFUJZLMn2Mr6W90Q6m6xiUOS5m4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1a148fb2.mp4?token=BQS9Qd9bStbZ5JULO5dilvwkck7uOEzgV3SIP5JCwuAiyTGqxdHpKsoH3ylkdW8trT4DaIX36lz-JSoGIhE6o1kzBqgkaA-0PQIbJZ62xSyyiG6v1nQyXNA0U764jkLsaz__WWWxZ8B_ICuXl3qevew-xrIJ0GjuC9nV9yDxxsSz7MEax10VOD0Jjm3Mue84z2rlp4hD1qYD0jvUIe17rbOa0ZmG6F440XnU4FDXo_pwojrMpzNbvWuwt3c5UWyGYZi6Az7WDiNQJZDHs3Ki-Ltn70v-SgvQ-qKtiNh1AHAB6vsDfT4huY6NYcZfkf7jho8XwMyv4g3fxoGn_hQC3RkG_ZUutw4WdHUOK9YHT1MCn9Fzg0pN-mXgaEEau6yeucXcqC5mtlq9pr4kkZP_grn3CsSvCmn3OC39bAc_mGfeuQ2t01lVfgybBhhGDxB_aKsormj_8wM2K36oonjmZSfHm3Cx022w-0WaJKcPAJ5rvYgHG5b_hK_Rk72imug6Q5zhf8x4ZAu3qyXb-iHwZ6x6U9R03ATJJZt6fJHgWEl6MrNYmMw_Jhp_3Ieqx9lrHD4PS10AvG7tarUaDejmBnKhziTli6Km5-iIM7znEnTwSFbJc9R5Fhzw9SCD7GxSL8F1dDCjDFl2U06MeFUJZLMn2Mr6W90Q6m6xiUOS5m4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اگه توی رابطه‌ات با امام زمانت شکست بخوری، کل زندگی‌ات رو باختی!</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/683130" target="_blank">📅 19:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683129">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1e9a0c02.mp4?token=CUvaVl9tXo-fnYUEF7UYPHLMTPkEoYgQyJF90JEuCb9SAtmvPAAQnSvERUvyeL05btotRoY1mr8xbi3QpTWcf8IgSchsM16D27S7Syvp_3CV400cALAuJ0yKrwuIlwd9XTFUYSgM4sUe4GPBFfrunFvZhsYtUHbIyWKBmmh7BouXkNv4jwhedRjdgSD72jhDd5MEzyyQVFNzzkSgiMXH8tunxeLYEGHYHfttTrBS3H62RtikVyVrp71DQoH707dSeZjxRC1clDoSlh2Zs-pdTKIPoeHe9IxL7x7053vT8AZYrU30xBrDictkXrUJQPeK-SxdPEwBkAt8h-Ps1MTFRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1e9a0c02.mp4?token=CUvaVl9tXo-fnYUEF7UYPHLMTPkEoYgQyJF90JEuCb9SAtmvPAAQnSvERUvyeL05btotRoY1mr8xbi3QpTWcf8IgSchsM16D27S7Syvp_3CV400cALAuJ0yKrwuIlwd9XTFUYSgM4sUe4GPBFfrunFvZhsYtUHbIyWKBmmh7BouXkNv4jwhedRjdgSD72jhDd5MEzyyQVFNzzkSgiMXH8tunxeLYEGHYHfttTrBS3H62RtikVyVrp71DQoH707dSeZjxRC1clDoSlh2Zs-pdTKIPoeHe9IxL7x7053vT8AZYrU30xBrDictkXrUJQPeK-SxdPEwBkAt8h-Ps1MTFRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت سد لتیان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/683129" target="_blank">📅 19:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683128">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvgaeeiLY25YXrFEPuNKjmz6eiHSfqEOgRCgVJ7JVtJ6s9XHwtq9jv2ejFRrl3NaEndRdoAzFFL9FHNO0Ww7i65oI9yt-ZLKi_mf7ZRMKp5j3yxh3iNsDadRnhyx-Sc_a4jsPbzEqOhn_Fp8_kf2sRrROAwQBbqyYPStY0Jowf9pXn9R9013H1TzmYSfve7iTB4IlnSlYdhdbA4C27A-NNIQpXrqsngvOG44B6lM9LrzsNW8LmxQLoLQ01lOMhEbmej3WhItM4E6WgebqiIacDJqkPyCkLTmgEvBb3yStyCQ4nns_xge2L-sGkyrSNHvwCJesvzjcsNnyPDEtBNXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسن‌ترین زن جهان ۱۱۷ ساله شد
🔹
اتل کاترهام، زن ۱۱۷ ساله بریتانیایی، بهعنوان مسن‌ترین فرد زنده جهان تولد خود را جشن گرفت. او متولد ۱۹۰۹ است و راز عمر طولانی خود را نگرش مثبت و میانه‌روی می‌داند.
🔹
رکورد مطلق طول عمر با ۱۲۲ سال در اختیار ژان کالمان فرانسوی است که در سال ۱۹۹۷ درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/683128" target="_blank">📅 19:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683127">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL51HCTBHiisEVn52W95syawoQCcX8D9DbO5F5TIzY2qBI5yhLTCUd1kErZOIfsv_cN8Ms_h6tF3qpD_5Gye3c0N1kZezbbq-VgpMsxo55Jtlua7iUCW4Bc0KimUfBQVTbFNg3IRfbn6HVHAk537HTKbCxFjCMwsCIxRTNfk1XJyv4CxU3uIu98YUyBJyPlWIkLh7ra2bzzs4Rv3no_1vbfJYk28NWFDGMt9DsSqCaYRUGsOpIAWkDDb05GSJ3abMH9M7QmpaB8g5m_-QVNu2rMWK1Wp7HRGpzZz_DrmGTxaJ4qBtgbARk8mCtqHs6F_hGfl8hix2b63PzB0TTeAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/683127" target="_blank">📅 19:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683124">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bbc1c9f3b.mp4?token=EVA1mV0_Qhx0lIOGM043itdKMqMkPDuWHOwty5NSRvTp9uTD-Zc7LA_uZIJmCWrzvXeW2sg-z0_RC5_OwJ7pk1EK1jsbzF56pXgZBsddhbl1DYiR6KCHb7urlsUjoKn6SEqY9hnsNXiJdMaFbx_M3vR0ENqIZXJTRYyFM_by8WsrSti727mRXTloDmmQDaJVV3dfL-dlII8vFSZPMWTQtfbY1QOeaFFNB1R-o4d2nXwdOKX8wcxlISWYOwBN-ZoD-qxP8htcaR_S1k8Ka9xkr7ZHo6s4ZirDkLu5t4MNYiZSgbeE6onQZifHrULmmqmp4j4Gy5cORqMKNz_AbrQvQ2PaQ552kZ9GFsL4jOZmVuKkDaJK_pRIOr3DkFmcgD-6il-MU85VKSY9_8UxQCwMIKMsiOTgiPuLUL8FotwC0J3-BNBXT8q0oJ93SrIJwRwHpjyXg5KNxN3lJEKRxzJQgnKcxKUrk8O3I0v-FWjDjLCAaXrjXl_FW6x4DpvWBXM0yS07as-NWLN51DIDvLOVSY3g7eAos8okyrEm71bgWkuH_-wPO7D4ffOcWd5czE661m_RNS2dixS4pZFSnYznTX9Vr8-fag_5cQqs-05BIjN5n2vB5-7wRQGkiIjdSkD0n9c0MisTWbnn8Zi-rwUB7GVml3KQkQEYhNHAKB_zrIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bbc1c9f3b.mp4?token=EVA1mV0_Qhx0lIOGM043itdKMqMkPDuWHOwty5NSRvTp9uTD-Zc7LA_uZIJmCWrzvXeW2sg-z0_RC5_OwJ7pk1EK1jsbzF56pXgZBsddhbl1DYiR6KCHb7urlsUjoKn6SEqY9hnsNXiJdMaFbx_M3vR0ENqIZXJTRYyFM_by8WsrSti727mRXTloDmmQDaJVV3dfL-dlII8vFSZPMWTQtfbY1QOeaFFNB1R-o4d2nXwdOKX8wcxlISWYOwBN-ZoD-qxP8htcaR_S1k8Ka9xkr7ZHo6s4ZirDkLu5t4MNYiZSgbeE6onQZifHrULmmqmp4j4Gy5cORqMKNz_AbrQvQ2PaQ552kZ9GFsL4jOZmVuKkDaJK_pRIOr3DkFmcgD-6il-MU85VKSY9_8UxQCwMIKMsiOTgiPuLUL8FotwC0J3-BNBXT8q0oJ93SrIJwRwHpjyXg5KNxN3lJEKRxzJQgnKcxKUrk8O3I0v-FWjDjLCAaXrjXl_FW6x4DpvWBXM0yS07as-NWLN51DIDvLOVSY3g7eAos8okyrEm71bgWkuH_-wPO7D4ffOcWd5czE661m_RNS2dixS4pZFSnYznTX9Vr8-fag_5cQqs-05BIjN5n2vB5-7wRQGkiIjdSkD0n9c0MisTWbnn8Zi-rwUB7GVml3KQkQEYhNHAKB_zrIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تصادف رانندگی سنگین در نیویورک
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/683124" target="_blank">📅 19:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
آکسیوس: بازار نفت دیگر مثل گذشته به اظهارات ترامپ درباره ایران واکنش نشان نمی‌دهد و معامله‌گران اکنون بیشتر از مواضع سیاسی، به واقعیت‌های میدانی در تنگه هرمز توجه دارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/683122" target="_blank">📅 19:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDeu7S3vynwssCVieU3ledmOdYxbtN0ZCBXhoF6ObVExFml71OfAtoJgwOlFytNc0RFcXXToOBtMnTWm5iCWiGJYSNK1Fg9lcGcndFxQiOSEjf3fkT2qGpJF69_YI_fbaKMAhtX3zc1Varsv3yw4LQA0jft082rnaI8Z2VpRotB2A77dEXem4vXHHVy0TKMf3clh42EnRp08C6_z0kMqLoEa-b8VBHaX1gt4s07j0_Zau-EUPdxTwjjmPePmxVLctpjBGgd5LyyZO5VAA3nadMCmNYv27lcE6JI7ByNhcCtbN8LT4mD3WP5Cwn84H2Jn4j5l8CGxiwu3jEijOG5ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینترسپت: برکناری‌ها در موساد نشانه شکست از ایران است
🔹
این رسانه آمریکایی با اشاره به برکناری روسای اداره اطلاعات و بخشِ ایرانِ موساد آن را اقدامی بی‌سابقه خواند: آخرین مورد از این نوع برکناری‌ها به دلیل بی‌کفایتی، حدود ۳۰ سال پیش و پس از شکست طرح ترور خالد مشعل رخ داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/683121" target="_blank">📅 19:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0140942b56.mp4?token=JBCk8ueXMrk5z8m_MwdaSIjCBZw4eVQfOmV9Gg4o5zzKq7oTLnaje8efjBPsa86HbMmZcbGiJB9hs_cv9om_pK640t4GGu7KCSowu30_ADvW-AbEYPYUozbTCwWIVl62GsUx7dwBOJdGCLjM9yMM2MJ5JHnn6PScN1snGTxYJVqPn6bP2TXKyLL5HQHIoNio7m1aooOZaJs-m6WP0PG-NhIxo-flyw2aJLN3R_jikfOrRD57Kp3XQLQ0BinfPHPky_i73N8H9HW7fVt1GL1fIt3qfJ911niAvZvP5oJA34T97U8vPYslgx2SnrpwWI29Z4R-Ty79qiG58Z4aT73B7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0140942b56.mp4?token=JBCk8ueXMrk5z8m_MwdaSIjCBZw4eVQfOmV9Gg4o5zzKq7oTLnaje8efjBPsa86HbMmZcbGiJB9hs_cv9om_pK640t4GGu7KCSowu30_ADvW-AbEYPYUozbTCwWIVl62GsUx7dwBOJdGCLjM9yMM2MJ5JHnn6PScN1snGTxYJVqPn6bP2TXKyLL5HQHIoNio7m1aooOZaJs-m6WP0PG-NhIxo-flyw2aJLN3R_jikfOrRD57Kp3XQLQ0BinfPHPky_i73N8H9HW7fVt1GL1fIt3qfJ911niAvZvP5oJA34T97U8vPYslgx2SnrpwWI29Z4R-Ty79qiG58Z4aT73B7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاری شدن سیل در جادهٔ روستای گیفان خراسان‌شمالی
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/683120" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683118">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRL4TmyXrKpMzqLcIHgNbzDX72AiWiPN2QCcDtrvt4cHIlC6YYrqAQbdQYD_X9zylmnFsGRfzCRooJI72LnsA4ejTH2bOYnu193etgXEc23ssrZnx1ppoMGVlPGnJN03ubTtt-MwaFepAlEGLWPlxs93aq21UVzMbga3NMoWZwy8WwRjVGP0dKDnnjs7r0mHz1VLwVfgxR72CKpxmxOY0RN5h2THyBS6Fjnz6x8L6bHN8za-XdkbIay6wfrMwD88YO96B_gSHeOZAxRkDiOZyy5EouH9BjyzLLmJpGFWD2069RjKFekKed2zj9yZDIBAdz4pDbm_lEMQAxEnmLaOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: اجازه نمی‌دهیم اردوغانِ دیکتاتور سوریه را اشغال کند
🔹
نتانیاهو با متهم کردن اردوغان به دیکتاتوری، یهودستیزی، کشتار کردها، پناه دادن به حماس، اشغال نیمی از قبرس و زندانی کردن مخالفان، تأکید کرد که اجازه نمی‌دهد او دامنهٔ تجاوزاتش را به سوریه گسترش دهد و اسرائیل چنین کاری را برنمی‌تابد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/683118" target="_blank">📅 19:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683117">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466763a826.mp4?token=WlI8tisPOiEwy5k1xnKXvX_7x-UaflrzqRR0Ea5LHsSmzwSergH5A3LnToX-vrQnBzH9r6e7rq_NsbUxcnRgijYGUCctIITVb-QtErFuuDjWx_ej8iwts574AuS9F6pe57NjvFSfyCE0kyCn-A5FfEI80shrT4zHQ6oRDZ4qVtDoCpPXfycdook2xpayLG0-YgP0XW5RlumW_PCuo6mlymXPJyIB_E8dNHj3ZK0iiFPctOvY5YituXdD8fw5HXyTZ2yrvbae7_x2tEWZqppHvgYuyXMyMmLEURjyp5OfGde_xaXtjrVFZ6RcmanZMSgqh4aawVYPww9LmLVEL_ytuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466763a826.mp4?token=WlI8tisPOiEwy5k1xnKXvX_7x-UaflrzqRR0Ea5LHsSmzwSergH5A3LnToX-vrQnBzH9r6e7rq_NsbUxcnRgijYGUCctIITVb-QtErFuuDjWx_ej8iwts574AuS9F6pe57NjvFSfyCE0kyCn-A5FfEI80shrT4zHQ6oRDZ4qVtDoCpPXfycdook2xpayLG0-YgP0XW5RlumW_PCuo6mlymXPJyIB_E8dNHj3ZK0iiFPctOvY5YituXdD8fw5HXyTZ2yrvbae7_x2tEWZqppHvgYuyXMyMmLEURjyp5OfGde_xaXtjrVFZ6RcmanZMSgqh4aawVYPww9LmLVEL_ytuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
صداهایی از جنس حقیقت ؛ بازتاب پیام‌های صوتی شما پیرامون موانع اقتصادی، فرهنگی و اجتماعی تشکیل خانواده.
🔸
پیام های صوتی  خود را  به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/683117" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683116">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En8B6rwhXf8up_gsuVjomEE3DDLKAWPiO_61ZE1RtRLF04faMQh7hfsSvhJ0a5TIdIKlQOZSvn_SGgRuUDyxbUMbtruzT3qMI6NoApiw-uN_tKZY5PIETzFs2eVqTyjXNRSxnpMIeUjfduKG27igHPx8-FRRAm478b3ZqF4ujAs7sLmc_7XepCGxuTpiLsYtUG_iAM9HL7U0GJCQT2pBS8wa7Iy9AnpbHkKmQkAsTQtjpP9DkhYlmslNwFyFKhXklHgh6mLUhAQdHkd5nvR4PpdZjNmfAAWT3vpVy_ayd-TA-T1DEdCcserKQHix7d1ZT6sQ0zFbQl-dZXBCORFpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سید عباس عراقچی وزیر امور خارجه به ادعای کمرشکن‌ترین عملیات اقتصادی تاریخ ؛ این فیلم تکراری نیز محکوم به شکست است
🔹
۱۴سال پیش:
«فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
🔹
۸ سال پیش:
«فشار حداکثری.» شکست خورد.
🔹
۵ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
🔹
امروز:
«کمرشکن‌ترین عملیات اقتصادی تاریخ.» این هم محکوم به شکست است.
🔹
این فیلم را قبلاً دیده‌ایم؛ همان داستان همیشگی، فقط با قلدرهای متفاوت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/683116" target="_blank">📅 18:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683115">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
فرمانده کل ارتش: صنعت دفاعی ایران با خودکفایی و تجهیزات پیشرفته، بازدارندگی را افزایش داد و دشمنان را به تغییر محاسبات و پذیرش تفاهم سیاسی وادار کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/683115" target="_blank">📅 18:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683114">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce969d3d3.mp4?token=c2-ob2svoDN_NvMzoJAzdA7c3BchLYYIHC-srFJHkFO_9a7t16vq-sYqVWIx9m4bP88N5eZj5oyNzaIzaOBbIvitdxEfyovNpkOxPU9W6lzX0BygHA3t1LQmPeYl2-1gbWDppL7fNCN6RPo4EUJ4O7MSLXCuhhbDdi5MzU0PsPJZ7dgU7rHSripaF4Cal_xnq6SnkvWtejo9P9QzAV6f0jIRPZ7NLP80FgW9FshbLECD9eF2cH2J73HISjC-xDizycdH3qnycqvaVUHpqAGtFzDTNPHghds1Uz6FCrDRnnzXZR2HFHl2DAyNntAkuLpCIbMIi7Ce7B87e7dZ3aII3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce969d3d3.mp4?token=c2-ob2svoDN_NvMzoJAzdA7c3BchLYYIHC-srFJHkFO_9a7t16vq-sYqVWIx9m4bP88N5eZj5oyNzaIzaOBbIvitdxEfyovNpkOxPU9W6lzX0BygHA3t1LQmPeYl2-1gbWDppL7fNCN6RPo4EUJ4O7MSLXCuhhbDdi5MzU0PsPJZ7dgU7rHSripaF4Cal_xnq6SnkvWtejo9P9QzAV6f0jIRPZ7NLP80FgW9FshbLECD9eF2cH2J73HISjC-xDizycdH3qnycqvaVUHpqAGtFzDTNPHghds1Uz6FCrDRnnzXZR2HFHl2DAyNntAkuLpCIbMIi7Ce7B87e7dZ3aII3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تفاهم‌نامه مفصلی در حوزه امنیتی میان ایران و عراق امضا شد/  ایران هرگز در امور داخلی عراق دخالت نمی‌کند
رئیس مجلس شورای اسلامی:
♦️
عراق در آستانه خروج نهایی نیروهای خارجی و تثبیت حاکمیت مستقل خود است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/683114" target="_blank">📅 18:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683113">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKvTHhfq_hEZbSQXaypUOUGcIKjq7bhBnB_FaPIU0t3NxmS8Cv3Cd7SGyGxPPmgLBALTJZHPKYQAU4xmwHhLH-fnBnVF3Y5hyc2qgzCsdDHE1Gm_O5UO4HNtiu-dV7Mjfwj8I20qAblcna4JuE68l2GaGUJeHXozzU90NEoDv6G8ooqzzQ7DORv81DCmd3zYJ_s0TrvB37FsnNWcmaH9QYOmLlahGo8oyHaDoQAeTqPZaHnAl3LQqalXI9QpFR931qgSjwEQ8LJHywShJOtRMnRcgSFyuZ62sL75YR1IxHzFjroEgkFnMKMVmP6iDZig3InKV7woq0E1riFbfPSQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده نیروی دریایی ارتش: به‌زودی در پهنه دریا درس تاریخی به دشمن می‌دهیم
دریادار ایرانی:
🔹
شرق تنگه هرمز و دریای عمان تحت کنترل کامل جمهوری اسلامی ایران است و تحرکات دشمنان فرامنطقه‌ای به‌صورت شبانه‌روزی رصد می‌شود.
🔹
نیروهای مسلح تحت فرماندهی کل قوا محکم ایستاده‌اند و به‌زودی درس بزرگ، تاریخی و فراموش‌نشدنی به دشمنان خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/683113" target="_blank">📅 18:43 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
