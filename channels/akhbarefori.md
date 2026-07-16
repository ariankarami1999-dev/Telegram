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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 02:56:07</div>
<hr>

<div class="tg-post" id="msg-671955">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است/ صداوسیما  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/671955" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671954">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/671954" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671953">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از یک مقام آمریکایی: حملات هوایی آمریکا روز پنجشنبه چندین پل در ایران را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/671953" target="_blank">📅 02:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671952">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع عربی از وقوع چندین انفجار در پایگاه‌های نظامی آمریکایی در کویت گزارش دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/671952" target="_blank">📅 02:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671951">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی: اگر جریان نفت و گاز از طریق تنگه هرمز ظرف چند هفته بهبود نیابد، باید نگران آن باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/671951" target="_blank">📅 02:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671950">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
دروغ سازی جدید آکسیوس و اسرائیل در مورد طرح ایران برای ترور ترامپ در ترکیه
رسانه آمریکایی - صهیونیستی آکسیوس مدعی شد:
🔹
در جریان سفر دونالد ترامپ به ترکیه، اسرائیل اطلاعاتی را در اختیار ایالات متحده قرار داد که بر اساس آن، یک مقام ارشد ایرانی به یکی از همکارانش گفته بود ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/671950" target="_blank">📅 02:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671949">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی دیگر از آتش‌سوزی گسترده در زیرساخت‌های شلیک موشک در خاک کویت
🔹
برخی منابع می‌گویند جاده‌ای که تروریست‌های آمریکایی از آن برای انتقال سامانه‌های موشکی خود به نزدیک مرز عراق و از آنجا شلیک به داخل کشورمان استفاده می‌کردند، به شدت مورد حمله ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/671949" target="_blank">📅 02:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671948">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله یازدهم عملیات صاعقه ارتش؛ مراکز و پایگاه آمریکا در بحرین آماج حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در پاسخ به اقدام خصمانه دشمن در هدف قرار دادن زیرساخت‌های شهری و مردم بی‌گناه، ساعاتی قبل، ارتش جمهوری اسلامی ایران در مرحله یازدهم عملیات صاعقه، محل استقرار بالگردها و هواپیماهای شناسایی P8 ارتش تروریستی آمریکا در پایگاه الصخیر بحرین را هدف حملات پهپادهای انهدامی آرش قرار داد.
🔹
امنیت و استقلال این میهن خدایی خط قرمز ماست و متناسب با شرارت‌های دشمن خبیث، سریع و قاطع پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/671948" target="_blank">📅 02:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671947">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فرماندار بوشهر:
حمله آمریکا به بوشهر یک مجروح بر
جا گذاشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/671947" target="_blank">📅 02:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671946">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور خودروهای اتش نشان و امدادی در مناطق نظامی پایگاه امریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/671946" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671945">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2p0Sm3KBKMaGKUfVBuat-o3GPgGkKWQWD4c0zMueAZ82rQXI3Fu-ndoz8prqsAD_i1nNPE8D6e7RVf93MmnNhPANPQjL-g5P4UbtDfdxKoqoTuli6JpZXjx5U2L-gtKliMlIyuJBKz434WaZt7AWH63tQmOYSNGGCCTzLwS2OHhFIl3XtbSLZmHAH1WzDCp1LudSj8OHYiH-o18wuRnPjMyApc9UZ83Qm8yacrrLf762e2wwrjj7NkfctjZjgdQFx3Ls6ihOzXTtMvTqytV2x93y0xiTASRhdi7_9FyyigK4Waw6FjaczdTcUgcJJjDuq2xRJ7mf8B7PyMJgu5EeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش سوزی گسترده و دود غلیظ در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/671945" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671944">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
یک نقطه در شهرستان دشتی بوشهر مورد حمله دشمن قرار گرفت
معاون سیاسی و امنیتی استاندار بوشهر
:
🔹
بامداد امروز یک نقطه در شهرستان دشتی مورد اصابت حملات دشمن قرار گرفت./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/671944" target="_blank">📅 02:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671943">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671943" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671942">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671942" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671941">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رادارهای آمریکایی در کویت، دوباره مورد حمله قرار گرفت./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671941" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فعال رسانه‌ای آمریکایی به تهدیدات ایلان ماسک: من در بزرگ‌ترین مراسم تشییع تاریخ شرکت کردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671940" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=Qgy1fXpAZIQ0B_w04JAsIz6v1vbpPRbdTdE7IKMeC7Qm9fSHvp7lMUDmrf3nQZa2NnNDbHUT9itLVUayRcTbtDZYgmRgBY3g6JaNwLBMt32HBdu5_3XJ2TNf-VxqsyuqZEeJsQHiAcHNdK5qfCOaq4EViJNklNt-6lRoVqqqf4oYATAD4yeW9Ls84pRhm6nz89wVNP_HgoqTVi8PO_g8l9UIQyjMJytNvrnIgyFG8C5ox6WH2TK38m-5tHufIhYclOp8b8T4bCTSywg9Wx_MM0Tu8OwZJVI8uWXTf1zy_nNFwAuNkfnLk5RYe_HlXErvQqDNFgyqBuT-4Hh45sC0imnb3auf_oDC5Rtb1I6cgoa89-N2SHszIRYh4lv7mrJktwcRgOY7PrgrbRHGw8m8hrWpmajRTvib598oKCETSH7f8m2fIjs4tPL9BSb7TQzpQDlw1rhXw3egI5IQVYsgCJuF7DGYwSPKRaCzcnaSWeocz_4SzQ22Hd4B4TkrrkbwRtqUy6GOWMf7ZjxT9_oOkgm_BXW4EJ-rnN7CJ6bAQnDBnPi4bjUIbvumqkgwe1a1Bl_qAcXyUiEcwYVbvZMDw2dds2LlVjrEj5O-rvT6OcGe8udg0UNrdhN93nprj8xhZmDr28YCuywOMVLasW4epMHBzkaZdq-G2DWTHqVxav4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=Qgy1fXpAZIQ0B_w04JAsIz6v1vbpPRbdTdE7IKMeC7Qm9fSHvp7lMUDmrf3nQZa2NnNDbHUT9itLVUayRcTbtDZYgmRgBY3g6JaNwLBMt32HBdu5_3XJ2TNf-VxqsyuqZEeJsQHiAcHNdK5qfCOaq4EViJNklNt-6lRoVqqqf4oYATAD4yeW9Ls84pRhm6nz89wVNP_HgoqTVi8PO_g8l9UIQyjMJytNvrnIgyFG8C5ox6WH2TK38m-5tHufIhYclOp8b8T4bCTSywg9Wx_MM0Tu8OwZJVI8uWXTf1zy_nNFwAuNkfnLk5RYe_HlXErvQqDNFgyqBuT-4Hh45sC0imnb3auf_oDC5Rtb1I6cgoa89-N2SHszIRYh4lv7mrJktwcRgOY7PrgrbRHGw8m8hrWpmajRTvib598oKCETSH7f8m2fIjs4tPL9BSb7TQzpQDlw1rhXw3egI5IQVYsgCJuF7DGYwSPKRaCzcnaSWeocz_4SzQ22Hd4B4TkrrkbwRtqUy6GOWMf7ZjxT9_oOkgm_BXW4EJ-rnN7CJ6bAQnDBnPi4bjUIbvumqkgwe1a1Bl_qAcXyUiEcwYVbvZMDw2dds2LlVjrEj5O-rvT6OcGe8udg0UNrdhN93nprj8xhZmDr28YCuywOMVLasW4epMHBzkaZdq-G2DWTHqVxav4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت شبکۀ برق شهرهای مورد حمله از زبان روابط‌عمومی وزارت نیرو
🔹
مردم با مدیریت مصرف برق، به برق‌رسانی پایدار به جنوب کشور کمک کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/671939" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671938">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای پی‌درپی در بندرلنگه
🔹
بامداد جمعه، صدای چندین انفجار در نقاطی از بندرلنگه شنیده شد که موجب نگرانی شهروندان این شهرستان شد.
🔹
تاکنون جزئیات رسمی درباره علت وقوع آن، محل دقیق حادثه و احتمال خسارات یا تلفات احتمالی منتشر نشده است./ مهر…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/671938" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671937">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
قطع برق نقاطی از کیش ناشی از مشکل پست برق است  استانداری هرمزگان:
🔹
در جزیرۀ کیش یک پست برق با مشکل مواجه شده است و باعث قطع برق یک منطقه کوچک شده که به‌زودی وصل می‌شود.
🔹
حمله‌ای به جزیرۀ کیش صورت نگرفته و برق دیگر مناطق کیش پایدار و مشکلی در این زمینه وجود…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/671937" target="_blank">📅 01:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671936">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
معاون استاندار: بوشهر مجدد مورد حمله دشمن قرار گرفت  استانداری بوشهر:
🔹
دقایقی پیش برای دومین بار متوالی در چند ساعت گذشته، شهر بوشهر مورد هجوم دشمن آمریکایی قرار گرفت.
🔹
ابعاد و جزئیات بیشتر این حادثه همچنان در دست بررسی بوده و در صورت نیاز به طور مجدد اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/671936" target="_blank">📅 01:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671935">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اربیل عراق در تاریکی فرو رفت
🔹
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/671935" target="_blank">📅 01:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671934">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وقوع چندین انفجار در کویت
🔹
منابع محلی از شنیده شدن صدای چندین انفجار در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/671934" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671933">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1VeUIk3GBuF1XTELcpZKMV-Qmae7AtjCJhR5uKIngSd0UXkItT3wnlJTnFz_8ecW3Wxg9HcOgWy_jbiu9vah8gStZsSaA_zeVWSqcG10XmV0bIIsjj7rMo-bVqEsK0yIOGBGK5cl-OeCXo7yp8Z9U-dv5UPa7Xe13qulMPn4pvqwVFwWnXt9yXZshsnJFB2mVAf6lDMvPaGBdpzQeY0f9PlYGvmwSUk25yJNgUPY2q0OlX0k8f3mbnWabL5sf1r_2Wrb6dsElXEGazxjVyzY27tAbjrL4PilgAn2eQIhHjApIDYNBsa0lBXhwFAe5xFiMY36C6PFPIrdFYrVs2IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اربیل عراق در تاریکی فرو رفت
🔹
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/671933" target="_blank">📅 01:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671932">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای پی‌درپی در بندرلنگه
🔹
بامداد جمعه، صدای چندین انفجار در نقاطی از بندرلنگه شنیده شد که موجب نگرانی شهروندان این شهرستان شد.
🔹
تاکنون جزئیات رسمی درباره علت وقوع آن، محل دقیق حادثه و احتمال خسارات یا تلفات احتمالی منتشر نشده است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/671932" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671931">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
گزارش زنده از فرودگاه ایرانشهر پس از حملۀ دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671931" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671930">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfbc72467.mp4?token=mIpR_x0fVNr001YTbd1rPkvb2Y9i71dRBQACWhUJaxhabjdFFH0n0WbTRsdkO978uZVusRUUwitnvMXTHkdEyJ7fs31R50LokpNeHb0uPSw-jlHFIzh1PsqugVfdX1Lq5U9fMTOVEMvzeu6dFrNb4ktyC1wxP8y4qeKDnE28eFAbA6GJPIzTCcCDY-2P3LsfXr4mgm56z9K1kqvlkxp99fVFoCqzq1aE1bWYyq4K68g7lP95_PA_IlirDu8pF-d2J4XFL8zBn0OENqWL5E6x0CNMUlIznGzf_HD2e9h214nXVOvI3du-O64CJl8aNtffM765EOw5t0k5LDJlzas8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfbc72467.mp4?token=mIpR_x0fVNr001YTbd1rPkvb2Y9i71dRBQACWhUJaxhabjdFFH0n0WbTRsdkO978uZVusRUUwitnvMXTHkdEyJ7fs31R50LokpNeHb0uPSw-jlHFIzh1PsqugVfdX1Lq5U9fMTOVEMvzeu6dFrNb4ktyC1wxP8y4qeKDnE28eFAbA6GJPIzTCcCDY-2P3LsfXr4mgm56z9K1kqvlkxp99fVFoCqzq1aE1bWYyq4K68g7lP95_PA_IlirDu8pF-d2J4XFL8zBn0OENqWL5E6x0CNMUlIznGzf_HD2e9h214nXVOvI3du-O64CJl8aNtffM765EOw5t0k5LDJlzas8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلی آخر را به دشمن بزنید
شهید حاج قاسم سلیمانی:
🔹
چه غیرتی می‌تواند کنار زن و بچه‌اش بنشیند و بگوید به من چه! اهواز را بمباران می‌کنند که بکنند؟ نه این مرام ما نیست. این دشمن سیلی می‌خواهد؛ امام(ره) فرمودند سیلی آخر را به دشمن بزنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671930" target="_blank">📅 01:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671929">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فارس: حملۀ هوایی دشمن آمریکایی به بوشهر
🔹
حوالی ساعت ۱ بامداد، بوشهر هدف حملات هوایی دشمن قرار گرفت. @AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671929" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671928">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تکذیب حمله امشب آمریکا به کیش  حسین احمدنژاد، مدیر روابط عمومی و امور بین‌الملل سازمان منطقه آزاد کیش:
🔹
امشب تا این لحظه هیچ‌گونه حمله‌ای از سوی آمریکا به جزیره کیش صورت نگرفته است.
🔹
وضعیت شبکه برق کیش کاملاً پایدار است و تمامی خدمات زیرساختی بدون اختلال…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/671928" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671927">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=egRhFF4FN_W-uJa8wH0zhhf98xha7J-paTTLS62HELP7AWGruIwdlI7KXQ7Tx5hf7TcPx5YlvPCiKtm2-KLkLfyAibsWpn0DpZu_kWzFRXzt8uA94e5YY5dtid6JEd1X583NQsjkp7ofCEO2II1em8e6L8m_xPOnzjdVA2zGMh6OS6mBs_S0C3TcPF58hyIb3TtrtdiitN1fdeVrTeZqNliGVADRuF8TFg_SxJPEOeTlkeHsC_9v0QeyAuxzFhO4eMQsEKWFm1R4Qkb5ySirOXUTYyJ06VXqm00beY_KafzBMoHEu9g1lJrDt-4Sq7JaKKR-InehJ5DrSNKBX-SHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=egRhFF4FN_W-uJa8wH0zhhf98xha7J-paTTLS62HELP7AWGruIwdlI7KXQ7Tx5hf7TcPx5YlvPCiKtm2-KLkLfyAibsWpn0DpZu_kWzFRXzt8uA94e5YY5dtid6JEd1X583NQsjkp7ofCEO2II1em8e6L8m_xPOnzjdVA2zGMh6OS6mBs_S0C3TcPF58hyIb3TtrtdiitN1fdeVrTeZqNliGVADRuF8TFg_SxJPEOeTlkeHsC_9v0QeyAuxzFhO4eMQsEKWFm1R4Qkb5ySirOXUTYyJ06VXqm00beY_KafzBMoHEu9g1lJrDt-4Sq7JaKKR-InehJ5DrSNKBX-SHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زنده از فرودگاه ایرانشهر پس از حملۀ دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671927" target="_blank">📅 01:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671926">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حملۀ دشمن آمریکایی به یکی از مناطق ویسیان در لرستان
معاون استانداری لرستان:
🔹
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی را مورد حمله قرار داد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671926" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671925">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxV58mFURiH4ETvVm9AqrzqhLPRjckZIxEzWnv3Ir6lnWJAZw5ayPsWqqFc_1Q546Nlrm_KmIL-nEEy8aS_3qUZ5n8NL4k-HH2Vxhmap7264VfSyJBivSgElNeYnEcjI9Re-R8YVWuat2WBDOLamrGImoAwfMiXRdaP4jXCGtk_9-HsA24Z-Az4PuBICGrCNAEBeHDXlipnPrcncIFh1A9otgb0ZAHWq4v5lFwEnNpEqraKkQKEOUGQYTDRGmFasvu2qiWWEgmsaYhpoe0VNs-9WnuGwauqija2GmbGalu5L2-6Ysoeoct55dfLCKNjm8w0Mwg6I7t5p8KqPIYGY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب_ماندگار از شهیدان حاج قاسم سلیمانی، سیدحسن نصرالله و رهبر شهید انقلاب اسلامی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/671925" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وقوع چند انفجار در بوشهر
🔹
صدای چند انفجار در نقاطی از بوشهر شنیده شد.
🔹
هنوز اظهار نظر رسمی در این زمینه صورت نگرفته است./مهر  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671924" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671923">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
برق مناطقی از کیش قطع شد  استانداری هرمزگان:
🔹
در پی حملات امشب آمریکا در جزیره کیش یک پست برق مشکل پیدا کرد و برق یک منطقه کوچک قطع شد که به زودی وارد مدار خواهد شد. اوضاع اکنون در کیش پایدار بوده و مشکلی وجود ندارد./ تسنیم  #اخبار_هرمزگان در فضای مجازی…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/671923" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671922">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80f301402.mp4?token=Zp6eKeyVxsMkhk9EIhuinS1Ae2a5N3UJGJ-05bYRvc6-K5i6L4pOO3yZP86QCQ3DGlFXPS2BofCVjfjLoNLbsS9SjKOMn_MVkaFrr2Xh6Ez15iuy3TiU50agHqQ96ps9kBRI2Pv8aisgjD7MIcwRQk8eejO8nD6IYCzUDWpn0GyPvCzyYg4kFrC8kt11mWG5-yZuhB0-tbRAPwj9LRGs7Ka-HE4X_3t5M93Lcm0In_jmDWHgYcPHeoAzsAPImGZJb0NmsudiJ2QrAf6kHS3LUru2gGlqacJFFzYJv9hq1Jl--IhasV5BaszLMLsvOObHGA4KM6iQDbzc-qzvPjP0cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80f301402.mp4?token=Zp6eKeyVxsMkhk9EIhuinS1Ae2a5N3UJGJ-05bYRvc6-K5i6L4pOO3yZP86QCQ3DGlFXPS2BofCVjfjLoNLbsS9SjKOMn_MVkaFrr2Xh6Ez15iuy3TiU50agHqQ96ps9kBRI2Pv8aisgjD7MIcwRQk8eejO8nD6IYCzUDWpn0GyPvCzyYg4kFrC8kt11mWG5-yZuhB0-tbRAPwj9LRGs7Ka-HE4X_3t5M93Lcm0In_jmDWHgYcPHeoAzsAPImGZJb0NmsudiJ2QrAf6kHS3LUru2gGlqacJFFzYJv9hq1Jl--IhasV5BaszLMLsvOObHGA4KM6iQDbzc-qzvPjP0cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا مدعی تصرف یک شناور ایرانی شد   فرماندهی مرکزی ایالات متحده در خاورمیانه ادعا کرد:
🔹
نیروهای ما برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران، سوار یک کشتی شدند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/671922" target="_blank">📅 01:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671921">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e6e08f27.mp4?token=WBEhLVeWbXz_VwiTfx3XoFBgOzwsvOAbfn78dEIVsnVnZNvFZ6lV0v5KYE-KkhP9QIM_PLlUwTr7coP26xPqK2_4atyEDayPEty8pRb2e3o-eZtJ9RCZZPNG7zttk_jkYwLJ2dgrhReC3I5nQMTsx4Q2RVsxYW0O9SWhJRaZVoyVF2klBr9X6nzy00mmk4zHwdFxl_ogbQc_2I1KgXjmgEBk-UlZOaOmTMtWN7B_HrEOLLTHtMJYotXZccjc5_2mH57s452hCQyFSVLQQQJ0HGbIAVMgvYJIP7p_v8spGfTvNnDHCjwlaSZuQ__uXtOOO6htQy7-d_P1tKQqbtA8HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e6e08f27.mp4?token=WBEhLVeWbXz_VwiTfx3XoFBgOzwsvOAbfn78dEIVsnVnZNvFZ6lV0v5KYE-KkhP9QIM_PLlUwTr7coP26xPqK2_4atyEDayPEty8pRb2e3o-eZtJ9RCZZPNG7zttk_jkYwLJ2dgrhReC3I5nQMTsx4Q2RVsxYW0O9SWhJRaZVoyVF2klBr9X6nzy00mmk4zHwdFxl_ogbQc_2I1KgXjmgEBk-UlZOaOmTMtWN7B_HrEOLLTHtMJYotXZccjc5_2mH57s452hCQyFSVLQQQJ0HGbIAVMgvYJIP7p_v8spGfTvNnDHCjwlaSZuQ__uXtOOO6htQy7-d_P1tKQqbtA8HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی بزرگی در یکی از پایگاه‌های آمریکایی در خاک کویت، نزدیک مرز عراق را فرا گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/671921" target="_blank">📅 01:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671920">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وقوع چند انفجار در بوشهر
🔹
صدای چند انفجار در نقاطی از بوشهر شنیده شد.
🔹
هنوز اظهار نظر رسمی در این زمینه صورت نگرفته است./مهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/671920" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671919">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا مدعی تصرف یک شناور ایرانی شد
فرماندهی مرکزی ایالات متحده در خاورمیانه ادعا کرد:
🔹
نیروهای ما برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران، سوار یک کشتی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671919" target="_blank">📅 01:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671918">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
منابع عراقی: یک پهپاد ایرانی، سکوی پرتاب موشک‌های آمریکایی را در اربیل هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/671918" target="_blank">📅 01:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671917">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b70A96d3umfztnhXcbMZf2A-ePUujg4fXs13H6BAto-aMihpsKHNhtA9-GM_ijgBjjYxOW7lbk30yNugUanHMvwv6Q9dUnhPfghZoFCvDzKqQtzRIenK7ZKcCh1_k1w5R9iEwmTbyszrfVziXHknMR_8yYbsYN6X5FCYi9-OHuYMc0VVEree33v-w-Bma6Oru-lAlrVwiVFqzZBr9VCDGHTY3SYF6ODGbBliXSkEBBe-zbPh2B2JMK6QObKnavJ4wvPZr7jTB3cF24658zVsS9wgH42F11n5__jVWyLqW-h3dIROunqdaZZj4Llv0gPJGUxeDoEOOXafJtwBybqOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز پس از حمله آمریکا/ چرا این پل مهم است؟ + وضعیت پل‌های هدف قرار گرفته شده در حملات امشب و مختصات آن‌ها
ببینید و بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230905</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671917" target="_blank">📅 01:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671916">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
برق مناطقی از کیش قطع شد
استانداری هرمزگان:
🔹
در پی حملات امشب آمریکا در جزیره کیش یک پست برق مشکل پیدا کرد و برق یک منطقه کوچک قطع شد که به زودی وارد مدار خواهد شد. اوضاع اکنون در کیش پایدار بوده و مشکلی وجود ندارد./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/671916" target="_blank">📅 01:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671914">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_a6mFnHNxpq3eRClzs9_waLtA3Kewg_vrywFD-KbQM2EdEQOEfOrQlEyqU2hkzg18Opv6AswWpNUmPtlG7v8Kkf62Fn46p6RwbJMzZfpuGG5MsbNuEKLs_PpFUQEV9eVYHkbEwpi2O-KvX05TD3uMg2M0w-nEvVnxN_msO3VkMpF7fbIsLa8hiCRcmYtA4SEmpFHTmtvePp0tRG84ySgDRQ-pasijxbkz5RkLUCkXEfLB534SRuSKkOgBBJ_eUUJh_IQU2zj8PqiBDwEkQXCXTE6Z8c1p258kQ0E4J9SHlOyiBUPO2tpsecmBfshRku0JymGmELtwhxiPLKel3iSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/671914" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671913">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671913" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671912">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4GjHCJzNsolHAUN7_DxvH0VuCf7T7U29iTzJzd9fS8oFdvbtS6QxgGo_nkUhPfRNFKMnw6boCQ_j8qYMhuvgPBiGtnaa55Y33t11F2OdxlxT8cWJPMq-hoc5o8OXo0XBC4jNhEkwgGl-LWIdPofJ1LBFu9ZDvBOAqpOldFnQ45TXjm82ZJe0nzctBo3h0da583qAWxhYOX_matAbDV6ZMmxCPByp1u3dUQHi5Z1Q07Md1k-zzDovHvQRaG5d3O4fdK4txzSCj4FAgBBM8enJyuKpfFuO_uqsTFAndASdBUnleJ7xM5r12dS085B2sqQaKqYjUBWGm_zsfW55QtlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین تصاویر منتشر شده توسط منابع محلی از حمله دشمن آمریکایی به محور بندرعباس–لار  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/671912" target="_blank">📅 00:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671911">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
حملات آمریکا به زیرساخت‌های جنوب ایران: پُل، راه‌آهن، تاسیسات برق بندرعباس و فرودگاه ایرانشهر هدف قرار داده شد
👇
khabarfoori.com/fa/tiny/news-3230849
🔹
ایران امروز به کدام کشورها حمله کرد؟
👇
khabarfoori.com/fa/tiny/news-3230734
🔹
ایران با این روش جنگی بزرگترین دشمنانش را شکست داد
👇
khabarfoori.com/fa/tiny/news-3230840
🔹
علیرضا فغانی؛ روایت صعود به قله داوری جهان | از قضاوت فینال المپیک تا سوت بزرگ‌ترین بازی فوتبال
👇
khabarfoori.com/fa/tiny/news-3230845
🔹
همه‌چیز درباره قطع بی‌برنامه برق و جدول خاموشی
👇
khabarfoori.com/fa/tiny/news-3230774
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671911" target="_blank">📅 00:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671910">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11af7931.mp4?token=M16C8wbbUt29vThvbGclPiJPUPqbdGhtRWqAISfDWPrlZxqSUQ5zjtZVrVQR2fVRTolI_AEagpj-098B3QVjApkeoNDzu3FY_Sn3MljfID29oLiJeTktIsWMd0uq2rIWTFbMbxYKOpuG1Vpm8mrLhrRfC5kNwKkj3IC6WE3MWAhcLCucFD1gPIsrCNqOjvpzYG62hzmRGu7C_I5AKVvnN8YvVn6IwxyNqZGrZXLuYVxhStmkZrgoTarcusrXmx51tj96LSyUBHVVO47VhTGel4PjHWiYOFdrls8oto0qu5ZmcsWQJYzzpQ66aL65kKJGeR8YscMw_B2cyU1WYy6ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11af7931.mp4?token=M16C8wbbUt29vThvbGclPiJPUPqbdGhtRWqAISfDWPrlZxqSUQ5zjtZVrVQR2fVRTolI_AEagpj-098B3QVjApkeoNDzu3FY_Sn3MljfID29oLiJeTktIsWMd0uq2rIWTFbMbxYKOpuG1Vpm8mrLhrRfC5kNwKkj3IC6WE3MWAhcLCucFD1gPIsrCNqOjvpzYG62hzmRGu7C_I5AKVvnN8YvVn6IwxyNqZGrZXLuYVxhStmkZrgoTarcusrXmx51tj96LSyUBHVVO47VhTGel4PjHWiYOFdrls8oto0qu5ZmcsWQJYzzpQ66aL65kKJGeR8YscMw_B2cyU1WYy6ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده شدن صدای انفجارهای بسیار قوی در کویت و شنیده شدن آن از بصره خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/671910" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671909">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند./  باشگاه خبرنگاران جوان   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/671909" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671908">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rth3pAvzy62x2fi5tV5Ff8ytRzA1JSR1IXPXlaZAzdsGU95MlIz46uqLc57czBgGofaCgkHnehd8ShBoeKqczEjAN1oaxLTz9oIrxde25mQ5o1E7tVdotKcutUmiuIC8K13dWInTvwq4RhKLSk7K0qD96yevK2OSyi1RSCV_2jfaprGZq-G2ZLIxmABnFgkup0IG2oSvTpRz8JhwvM9N8-Y-Le11Yvbb2JuKNVjxa2JK31cHL7jW-cxDD0rVnu2gaXHwdtIB8K0kMzC-6ELNgygGXwALdky9qkURpLGOMWPqgxLVL8VYG956FbvAtUN6a3oJoRTI3_Jjz_TFV5D44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام کد اضطراری اف-۳۵ بر فراز امارات
🔹
‏یک جت جنگنده اف-۳۵ متعلق به نیروی هوایی آمریکا چند دقیقه پیش، یک سیگنال اضطراری عمومی (۷۷۰۰) را در حریم هوایی امارات ارسال کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/671908" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671907">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شنیده شدن چند انفجار در حوالی حمیدیه
🔹
بر اساس گزارش‌های رسیده، دقایقی پیش صدای چند انفجار در اطراف شهرستان حمیدیه شنیده شده است./مهر  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/671907" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671905">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab33920f95.mp4?token=YFiu1GPQzUJKAjg21M5YNAp_G48nU9BsxOzIeiru2RWm4QU-rp5_Mncj67Z8_16n6wvK5FcFGDBcdhjGqwQPd61QocCz40DbeYN_DTTnKH5s400P3rQ5IT-yelpN6igcU70jzGroKZPpbjbGPi4kJwvuXlYYr27rU0YNXnWjqYmAWMywdfHPma8Gswvmi1HrGhvcsBYbv2M_hOxr1X53YCp6Zt3dwH9VxIqQaGcVXCBtNunI4jtrj_gIv40TiIKwL-rwlvSqHzsT2YoXHNRUkexRmz4XuRcXDvcRWtI2ChyDNyHGjUBl5JBmlLW261qkiGg-YmV22EYnfifBsCPKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab33920f95.mp4?token=YFiu1GPQzUJKAjg21M5YNAp_G48nU9BsxOzIeiru2RWm4QU-rp5_Mncj67Z8_16n6wvK5FcFGDBcdhjGqwQPd61QocCz40DbeYN_DTTnKH5s400P3rQ5IT-yelpN6igcU70jzGroKZPpbjbGPi4kJwvuXlYYr27rU0YNXnWjqYmAWMywdfHPma8Gswvmi1HrGhvcsBYbv2M_hOxr1X53YCp6Zt3dwH9VxIqQaGcVXCBtNunI4jtrj_gIv40TiIKwL-rwlvSqHzsT2YoXHNRUkexRmz4XuRcXDvcRWtI2ChyDNyHGjUBl5JBmlLW261qkiGg-YmV22EYnfifBsCPKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است/ صداوسیما  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/671905" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671904">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
./  باشگاه خبرنگاران جوان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/671904" target="_blank">📅 00:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671903">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اصابت موشک‌های دشمن آمریکایی در حوالی سیریک
استانداری هرمزگان:
🔹
ساعت ۲۳:۳۴ نقاطی در حوالی سیریک مورد اصابت موشک‌های آمریکایی قرار گرفت./ فارس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/671903" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671902">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پل محور کهورستان هدف حمله دشمن آمریکایی قرار گرفت محور رفت و برگشت بندرعباس به لار مسدود شد
🔹
برخی منابع اعلام کرده‌اند در هنگام اصابت موشک به پل، خودروهای عبوری نیز بر روی پل بوده‌اند، از میزان خسارت جانی هنوز اطلاعاتی در دست نیست.  #اخبار_هرمزگان در فضای…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/671902" target="_blank">📅 00:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671901">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
صدای ۴ انفجار در محدوده ساحل جنوبی قشم شنیده شد
./ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/671901" target="_blank">📅 00:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671900">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده شدن صدای انفجارهای بسیار قوی در کویت و شنیده شدن آن از بصره خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/671900" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671899">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
انفجار و حمله جنگنده‌های آمریکایی به زاهدان صحت ندارد
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/671899" target="_blank">📅 00:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671898">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW-VRV-iRf6Dn6Pq3kH-35o3FOsJGLpf05If5ih7y-Alh-MJKTzmYDL1Q5cACz2lImRA4fUb0XCS9tQwMz8-fBGFzgQoR1oyVqSpQ5Z_pPhmpGFHhY6lBArYVvfe8hGw3NJUQhSqPUA4EID9zzCA1y3xw2DdhSurt87yGJ-1hRsdW4d5_Zu1XlY9Foqq2xD02XXmJhfJM3htnb3kXJySSF5LNeGjwkJoY3yiuSxJfePij5nqebCsPTh8PsOn3-lFVxJYkRwaNXJmFYK1oS7MX8UhiKUQlLbxoqpRFkI8ZC4OR5dYRjDlXWKLA7mncmpXrVpHdsbCm1FnPhUzIgTErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/671898" target="_blank">📅 00:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671897">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تعیین جایزه ۱۰ میلیون دلاری مقاومت اسلامی عراق برای کشتن دونالد ترامپ
🔹
مقاومت اسلامی عراق در پاسخ به آنچه گستاخی و وقاحت دونالد ترامپ در ترور فرماندهان پیروزی شهیدان قاسم سلیمانی و ابومهدی المهندس خواند، جایزه ۱۰ میلیون دلاری (از محل کمک‌های مردمی) برای کشتن رئیس‌جمهور آمریکا تعیین کرده و پرداخت آن را به هر فرد یا گروهی که این کار را انجام دهد، وعده داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671897" target="_blank">📅 23:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671896">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVqFNVU24hNdTsZiZlTrUfroEk5Ui9OmcolnPskR6OegOooUGKU5KmPBeeNrmSu96h95zuA9AZ-vGkk6WfAGeSgzmp05zgNjsqOlNvBOGefUJ8kjMtGTs_tpBJ3xxhyoatzDMjmxq2OOiFYnq2K31UpeCwLTIdPvMJ-5b6hKmATEqC_dZGbjsFrpmowDCGz5n2URiBCAsP5bx3JaxQXcbi4sEI-FJX8LgI-7BgPwq88K-eOyUHG7bqRBm5VsbXKNA6yXPVewWqlC57mQFDn4JXouXRGyYcpk-y1VXOwuDJOHnN5aTbpQc5ouTmLq0Xb777ueoe0rAfe2t16EMeBgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از تهی سرشار
قرارگاه مرکزی خاتم‌الانبیا خطاب به آمریکا:
🔹
«زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده است را می‌زنیم.» در این هشدار، واکنش سخنگوی قرارگاه به تهدیدهای رئیس‌جمهور آمریکا نیز جلب توجه کرد و از تعبیر «رئیس‌جمهورِ از تهی سرشارِ آمریکا» برای ترامپ استفاده کرد. این موضع‌گیری، پیامی صریح به واشنگتن بود که هرگونه تعرض به زیرساخت‌های ایران، با پاسخی متقابل و فراتر از مرزهای ایران همراه خواهد شد.
🔹
هشتصدویازدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/671896" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671895">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
بحرین از محدودیت‌های جدید برای تردد شناورها در خلیج فارس خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/671895" target="_blank">📅 23:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671894">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
شنیده شدن چند انفجار در حوالی حمیدیه
🔹
بر اساس گزارش‌های رسیده، دقایقی پیش صدای چند انفجار در اطراف شهرستان حمیدیه شنیده شده است./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/671894" target="_blank">📅 23:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671893">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
حمله به زیرساخت‌ها توسط دشمن تروریست آمریکایی؛ حمله به پل بندرخمیر
🔹
گزارش‌ها حاکی از آن است که لحظاتی قبل دشمن آمریکایی به شهرستان بندرخمیر و بخش کهورستان حمله کرد و صدای چند انفجار شنیده شد.
🔹
اطلاعات رسیده و پیگیری ها حاکی از ان است که در این حملات پل…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/671893" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671892">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
حمله به زیرساخت‌ها توسط دشمن تروریست آمریکایی؛ حمله به پل بندرخمیر
🔹
گزارش‌ها حاکی از آن است که لحظاتی قبل دشمن آمریکایی به شهرستان بندرخمیر و بخش کهورستان حمله کرد و صدای چند انفجار شنیده شد.
🔹
اطلاعات رسیده و پیگیری ها حاکی از ان است که در این حملات پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
🔹
برق مناطقی از کهورستان نیز در حال حاضر قطع می باشد./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/671892" target="_blank">📅 23:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671891">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حمله موشکی جنگنده‌های آمریکایی به فرودگاه ایرانشهر
🔹
براساس این گزارش، مردم منطقه سه انفجار شدید را از حوالی فرودگاه ایرانشهر شنیدند و گزارش‌های اهالی نیز حکایت از حمله سنگین به این فرودگاه دارد.
🔹
هنوز از میزان خسارات این حملات اطلاعاتی در دست نیست اما مسئولان عملیاتی نیروهای مسلح مستقر در منطقه هم اکنون در محل فرودگاه حضور دارند./ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/671891" target="_blank">📅 23:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671889">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41c69856e.mp4?token=IMx5uZncwhwxm48E1dd_u2K7qxFbX3VtOM8TYLnzBKAh5J15LWe5GXdQrNoNrCzRtnV0BxXPC1EjuFA0327W6KBcaFYEHja0ti2J5EsAZNPHYPXLkueZF99fQMVZDF8FXLsqJco2LWsZIyxpSxXBN3L83g2w10omROxSg44dhqqReuvl-EA5zfW6Drkpd0R1BXTHEOOLm43sav04FwOb8mbAK_JKMhBD-pcRY3Yf58SAWuCncxxriP76KFh0DWXs2GM2CVgW3bv4T3zQa7YVUQdnA1vKDy7exMfPDWXcfHhfJbo1hud2tFyiVM_3ydkxfy4mtZv2hk97vS4i4o-1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41c69856e.mp4?token=IMx5uZncwhwxm48E1dd_u2K7qxFbX3VtOM8TYLnzBKAh5J15LWe5GXdQrNoNrCzRtnV0BxXPC1EjuFA0327W6KBcaFYEHja0ti2J5EsAZNPHYPXLkueZF99fQMVZDF8FXLsqJco2LWsZIyxpSxXBN3L83g2w10omROxSg44dhqqReuvl-EA5zfW6Drkpd0R1BXTHEOOLm43sav04FwOb8mbAK_JKMhBD-pcRY3Yf58SAWuCncxxriP76KFh0DWXs2GM2CVgW3bv4T3zQa7YVUQdnA1vKDy7exMfPDWXcfHhfJbo1hud2tFyiVM_3ydkxfy4mtZv2hk97vS4i4o-1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان ست پنجم| ایران در لیگ ملت‌ها ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/671889" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671887">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی در تپه الله اکبر بندرعباس/ ۷ نفر مجروح شدند
🔹
دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
🔹
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/671887" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671885" target="_blank">📅 23:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jywwzbYuXNsgvBFTGNyc74Y22KS3FVguDb1V3ZKxnXyJR2eR6y4yWRbehxp1ykU59WuEbRFtbcAMHrNgyqBEt4tyBwykr75h21JYqN2UFTypwN_uCqAbmVntwYHahlbXeu7AFF88uvxNXldqeLErlVcjWrHkux2sPGmyLI_8LGEaTE4jrEK8hGqDfs2GabcMhOfFXLcSgqh4GPJ866qgAl6MMCC586Cvgp585yOAtVWb9-_MjxhQ9pcQTX9WA2vIQZt_QcUufjvz3hzztViLKVnmnGAbERb7ZPteqMr38paYqbwLDxECc2i15CNP5UABU1fTWnIBTy1A6TT7l67VVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب جهانی و توجه رسانه‌های بین‌المللی به بنر تهدید‌آمیز دیوارنگاره میدان انقلاب درباره کشتن ترامپ
🔹
دیوارنگاره جدید میدان انقلاب تهران با تصویری از ترامپ در تابوت، طی چند ساعت گذشته به سوژه رسانه‌های بین‌المللی بخصوص رسانه های امریکایی تبدیل شد.
🔹
رسانه‌هایی از جمله نیویورک تایمز، نیویورک پست، الجزیره، فرانس۲۴، فوربس، یورونیوز، فارن پالیسی، دیلی تلگراف ، فاکس نیوز و ... در گزارش‌ها و خبرهای خود به این دیوارنگاره و محتوای آن پرداخته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/671883" target="_blank">📅 23:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/659ee464a9.mp4?token=qOfMEBbFtRiB_5ImbRo-sU1qGe3bY8KZQWY87zkuYyb9vz12IKsckTU3UNvaE5ECsKevDrRvlClGhHzAugOIcMHn8oqxfsprWXxBbHrWfTEoSYMLNNdzKLqBBaA5k5SXjkGfts1Q264ueGnodEoWOk06P68Zp4fUnFjNcKpzzQQADq_BFYNeIloHK5ODno-V-oSL0edekvZgpCg3jBeQngBXU6srJo3f5rfQE-NX_EhrSIFedhx9XybtqCUnEV2I2ivsHK4yHduHGC_JvprF55GiFbdypNEit3rU6sMjm9t_EocjfMwg1IhhPTDo82dLFaVmvuhEISdV7CcGSV5Hpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/659ee464a9.mp4?token=qOfMEBbFtRiB_5ImbRo-sU1qGe3bY8KZQWY87zkuYyb9vz12IKsckTU3UNvaE5ECsKevDrRvlClGhHzAugOIcMHn8oqxfsprWXxBbHrWfTEoSYMLNNdzKLqBBaA5k5SXjkGfts1Q264ueGnodEoWOk06P68Zp4fUnFjNcKpzzQQADq_BFYNeIloHK5ODno-V-oSL0edekvZgpCg3jBeQngBXU6srJo3f5rfQE-NX_EhrSIFedhx9XybtqCUnEV2I2ivsHK4yHduHGC_JvprF55GiFbdypNEit3rU6sMjm9t_EocjfMwg1IhhPTDo82dLFaVmvuhEISdV7CcGSV5Hpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/671880" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/671879" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671876">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس و قشم و اهواز
🔹
هنوز منشا این صدا مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/671876" target="_blank">📅 22:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671874">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0VshsvvdqnQmMmatQBKtamInDLP265wVJjOd0OcNzEfECHofjo8Bgiv_ozT1jfbX_-ZcQmBW5w75cxqQS7Zke9qHSqWKtNmfS76SAypFQd5TpF6fA4dYqhd2HBXu_N24kB8QluFPrATzlsHiAFnxjSnOUuZYUlzpNue6nL6kZ_BvZXixcQaHdB7_WZCY96IZ3v0Ht3RkImwpoApuoqUYevZuhmlk-7WZk6xjyw-UDLaH0xzKDk2dEyn4OYFkJlZjWajsBNZCgMjmhVc6X-HkhrXy9jiW5wP7J6zEe_QbstxNQRKzz1omKh9XEJ-8IhPSeUTzgUCJDnLkHHeeE6FEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلال ماه صفر
🌙
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/671874" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671873">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrXbwL4f-b2qtLdgHkyC5Sf6B8v6aOf33i_EaPdN32C7qIbXdhSRkvMepOblVASLPF1yaTT5OZzrvFKrZjiqCO0JlnFVz3LwxF0lo4kBgkibE4zZKT8K-nFBd1OiFqyD8tMjU-R0vEEeKxeZ-yoK64TYXqJiQfkr5E-t64Qf1OQoZV9aXrbuS9ADPYIrzKHkYC_PhboP-hwOFQ4HW1DcQKoozI3ykotl8xkwDBSqsaGCEvJYbdGFi5ZQUlQhypROIsC-BO_UzJ4MD21Taz8qWzVyEVhpKOEuVPgTh9d9WFyt6ptTPnp5kElh032lEEtlkqiCagfFCSISjpWjxnC25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/671873" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671872">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c56e6a741.mp4?token=HlkBVGUTdXaAy0oaUYkc85SFFsiriQG1nU1Il8QBCVSy5ErPwvWq9P1vdp_NHZ6clA5dcRfa2pJhlXPLaUU4YHUkJLOBN_UpjzcUZGi-K9fY0I1TBK4AbKsZSDVqZDTmDZx5Ci-CAdJpZjz2jmfkAbW-9Zu4cbqaNIARI8Az8uX15WvrQcarVQlpznabvnFZ-zWpBLzZCjqA7gjOB9my-I9V3v-BjmJRiUfmZPz4-5WQZUBf99SFcKcVBauMcBeNEdvCI9FMHrhRB6JgQnWt0XMy2pfptArI3KgLhPNI4k7p93H8YoJyhtYAXZ3OLUhc2QRPXnGt5qh7XRb_esLJpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c56e6a741.mp4?token=HlkBVGUTdXaAy0oaUYkc85SFFsiriQG1nU1Il8QBCVSy5ErPwvWq9P1vdp_NHZ6clA5dcRfa2pJhlXPLaUU4YHUkJLOBN_UpjzcUZGi-K9fY0I1TBK4AbKsZSDVqZDTmDZx5Ci-CAdJpZjz2jmfkAbW-9Zu4cbqaNIARI8Az8uX15WvrQcarVQlpznabvnFZ-zWpBLzZCjqA7gjOB9my-I9V3v-BjmJRiUfmZPz4-5WQZUBf99SFcKcVBauMcBeNEdvCI9FMHrhRB6JgQnWt0XMy2pfptArI3KgLhPNI4k7p93H8YoJyhtYAXZ3OLUhc2QRPXnGt5qh7XRb_esLJpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صفار هرندی: رهبر شهید در برابر گزارش‌ها علیه شمخانی، از شمخانی دفاع کردند
🔹
فرمودند چند تا مثل شمخانی داریم؟
🔹
رهبر شهید؛ لاریجانی را برای انتصاب در دبیری شعام وادار کردند
🔹
در دعوای لاریجانی و احمدی نژاد، اشتباه کردیم که سمت لاریجانی را نگرفتیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671872" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PozoqTFPjKQe0isL7KkZ74O-EJUghmNfi01kvYGMvuoiXBuM7uAIYknpMq_3ZpcxVIQRwgZvQiAnLkbqRZj29MFp7y2mMDj2swxcTkctmn3PYGoFzuNFnDPwrYqmR0L04ZnSKLEI0k8_ubaA0XDo7ZUeb6qhEsE_VIUGC_T1RkyURVUtLX-SluPye9QMpcPdw6eqMp6H_ad9YmmpTKEIbtRrPmgscS8M2NKhhEhSYpekrapvzT28BFHqepqcETY8jT5BynFuRTR0u6XYvnMKUExnKkEdst5GDh33TBiMxM9SiWlpIfzSTHHNM5rrJceu1UFmicUUzKMK9usGIkbAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر از منظر امام علی (ع) چگونه است؟
🔹
مى‌فرمايد: صبر  بر چهار شعبه استوار است؛ اشتياق، ترس، زهد وانتظار. «شوق» به معناى علاقه و اشتياق به چيزى و «شفق» در اصل به معناى آميخته شدن روشنايى روز به تاريكى شب است، سپس به ترس آميخته با علاقه به كسى يا چيزى به…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/671865" target="_blank">📅 22:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای خوک نجس در مورد آزادی شهروند آمریکایی توسط ایران
🔹
ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در زمان ریاست جمهوری جو بایدن به ناحق بازداشت شده بود، اجازه خروج از کشور را داد. او اکنون در خارج از ایران و در وضعیت خوبی به سر می‌برد.
🔹
ایالات متحده…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/671864" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9S0duzz-DKhyuDnc2f5MDtjhaXj_egDl6iVjoaveYPmuSqR8MqgAmAyd9kGfNQjB9vA8sbY6BqA91vAnro_QcfM202fz3CqPN9dgy_J29AO6ngg294jdSDYKzwp3Zrwy2U8Em5Nmoj7LhDWOwV_ZXrGKVjRgTDfaoH8JSQ1Ix7Fu9gHwWLJARHZt2SYwTyA9neiA65_t6ciifwFTlvvxiex_26g8fIJuwjTDCFPJmrHaK5f47orz9CrbxX6jCSAZs70vTtUp0GjWSSih5zeWSrk2gZBB3J7H5oyi-piaJhlGg3K7QWu8mNEmskzkj1FndUZOUxbjwoFc1dNS43SKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان ترویستی سنتکام دور تازه تجاوز به ایران را تایید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/671863" target="_blank">📅 21:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671860">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKMEabP--54Ojk43j6iwuHcoVj2rRQ-De0jab9odCSOMWDDTW226xKCZf05d4ehdSjNrWR7naNHIwRmPwjRyJ8wAqsyeD5BCYDViHzn6HHVFYV-lBD5JU4k55duBg1otlNK1Sw2-bym5hXFzCfy8ZDhCAkAZa7rdR-bQOJ3syyHV3fzvjLMtCBA6dFkEq-gCHaTMYOitPDzUrXb7pjQggME3OLK7t46TkgXyTngn3VxoQDQpDpsdZKk7necX3Ia8KVDGSpCicpbJuQnNznZFMZ8mPgexJR40qNc6u5ptKVkCynymureEo4FGMKePQBZv6NROoI0GUqQmaI58H-Ey6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست علیرضا دبیر از مسئولین کشور: جنوب یعنی همه ایران، پس به کل مواضع دشمن حمله کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/671860" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671859">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مقتدایی، نماینده مجلس: آژانس انرژی اتمی تا مرز جاسوسی برای متجاوزان به ایران پیش رفت
عباس مقتدایی، نائب رئیس کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
اقدامات اخیر آمریکا جنایت جنگی و نقض قوانین بین‌المللی و تمامی تفاهمات پیشین با ایران بوده و از این رو، ایران خود را محق به پاسخ و تنبیه متجاوز می‌داند.
🔹
با برنامه‌ریزی قرارگاه خاتم‌الانبیا و همکاری سایر نهادها، اقدامات برای عقب راندن نیروهای آمریکایی از منطقه در حال اجراست.
🔹
عملکرد نهادهای بین‌المللی، منفعلانه و در مواردی هم که مداخله‌ای انجام شده، به نفع متجاوز بوده؛ نمونه آن آژانس بین‌المللی انرژی اتمی که تا مرز جاسوسی برای متجاوزان به ایران پیش رفت.
@TV_Fori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671859" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671858">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewCsKrYFGlhUiIOJ-ACs9F4VpDr_Z7Ze4brbxG6925-DAZmWE7tq43BaM_9zpGH4LmtcIwXFUbupzYAg9V6ikiJNXdl87DF55OpcdEyaQKDlNyp8k_BTkzGVrmxVh8M8Za4obGB7jVJt2elxzPoPsBKsFCI74TDVWg1nYFp_wG_w7LTqgwiqGw5OUcT19KA-7PhyeFzGc1w133UmwERWjoxlgea7DjzoAAI1_otE5dOArOTGrOzguGXbjL5pbZNezQzY-uV320ZEePfAasaMMbXvhwQvVXRfTF19aZ7dJaghpNDXsysBLyQAHj9qDn6dtE59EAQJSHTvWCFB91_fkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با این روش جنگی بزرگترین دشمنانش را شکست داد
🔹
دکترین نظامی ایرانی ها را می توان در یک کلام «پویایی پدافندی» نامید. طبق این دکترین، نیروی نظامی با بهره گیری از سرعت فراوان و بر اساس راهبرد عکس العملی، شروع به برخورد با دشمن می کند. در این اصل و دکترین، اساس نیروهای نظامی «سواره نظام» است و مهم ترین سلاح نیز تیر و کمان به حساب می آید.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230840</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/671858" target="_blank">📅 21:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671856">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ادعای مضحک سخنگوی کاخ سفید: ارتش ما هرگز غیرنظامیان یا کودکان را هدف قرار نمی‌دهد! ایران به کشتن زنان، کودکان و افراد بی‌گناه معروف است. شما باید روی آن تمرکز کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/671856" target="_blank">📅 21:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
کاخ سفید مدعی ادامه مذاکرات ایران و آمریکا شد
سخنگوی کاخ سفید:
🔹
ایران به مذاکرات با ایالات متحده ادامه می‌دهد و خواهان دستیابی به توافق است. حملات اخیر به ایران به دلیل نقض یادداشت تفاهم بود.
🔹
ایران به مذاکرات با ایالات متحده ادامه می‌دهد و خواهان دستیابی به توافق است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/671853" target="_blank">📅 21:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22723d50a1.mp4?token=ody20qtGnSGBMbwr6DbgW7K_J5J5ShLNnDED0pMlauBx9CnOymu4aZwD_wyJnuYVT0o7m201k5sCceC8Wt1v0HkUgThdsXQp9LZG75mjSTVNqG9XyH1EiTyc71ChEiYZ-Yt4oCgaWgI4m7Isc3Cmyo-wV1_H2bB6Xo9uHK_qudwwGjGFP8uHHKY3MT3u7iFx3rMIC2GYOaKnFqa-yQVa2VH4kW7E4kMEnqISWX5b-JpDMkoQNNTMvIXUT_xrEuR5FGrKvtuxEaNHrXcAvu15CWbvCGN8ViBpGUNI-5ieqxvytaWoMBS5pb_kSw_f4bai5mig6jRyp1XsUbeAr-tRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22723d50a1.mp4?token=ody20qtGnSGBMbwr6DbgW7K_J5J5ShLNnDED0pMlauBx9CnOymu4aZwD_wyJnuYVT0o7m201k5sCceC8Wt1v0HkUgThdsXQp9LZG75mjSTVNqG9XyH1EiTyc71ChEiYZ-Yt4oCgaWgI4m7Isc3Cmyo-wV1_H2bB6Xo9uHK_qudwwGjGFP8uHHKY3MT3u7iFx3rMIC2GYOaKnFqa-yQVa2VH4kW7E4kMEnqISWX5b-JpDMkoQNNTMvIXUT_xrEuR5FGrKvtuxEaNHrXcAvu15CWbvCGN8ViBpGUNI-5ieqxvytaWoMBS5pb_kSw_f4bai5mig6jRyp1XsUbeAr-tRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دقم عمان حمله کرده است
🔹
این هتل به طور انحصاری محل اقامت نیروهای آمریکایی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/671852" target="_blank">📅 21:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU_yYlPPIKxbLiTFCBnBfrHRYuCoPZzo3BoOm1oP1LntamvnaaS8vCfvCFv3ILHy-gX_w_JGNwc-FTirWEgsTAjdYlYQan3qVAsD4GMEPjg_4u9nj3J0jPS3dvIfv_uzlQzotjJoyBy_6L6FDLdenvZ1g0Wq18Blfr0ppyEjwG1PSXlJzJjMrEHmUfTqvNZ2T3bhl4MXar4L7QW_wsg-D52ieXm9WXmtYN1k2JPeq3tOaLjuYkM8L3t_kzVOHrVzOQUCAhi_7qbDMdfXlXpDQ49KKCzXQ0_si2T0yOVFWHB9eIIkImtP0yRzNdCHRutL43WAyu7Vj8tEzI3X0lKKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: علفزار (۱۴۰۰)
🔹
ژانر: درام اجتماعی، جنایی، معمایی
🔹
خلاصه: اگر به فیلم‌های اجتماعیِ پرتعلیق علاقه دارید، «علفزار» را از دست ندهید. این فیلم به کارگردانی کاظم دانشی، داستان بازپرسی را روایت می‌کند که در جریان رسیدگی به پرونده‌ای پیچیده، میان…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/671851" target="_blank">📅 21:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671850">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حضور یک تروریست در فینال جام‌جهانی
🔹
کاخ سفید دقایقی پیش با انتشار اطلاعیه‌ای اعلام کرد ترامپ، رئیس دولت تروریستی آمریکا در فینال جام جهانی فوتبال شرکت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/671850" target="_blank">📅 21:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGkJOWD3zPOxNnzBHzG9YdxmV1nLEjO-nH7skel9ZPIt3_yXISl9L-n2HTadzay6VWbXekFUyda48OHT17Y6FaMMrjSVG5QdPi4ny7x_gyRL9wu2iFZZVRurPjovkGjDypb3L2K4lonC24OTgIvZmgZ8_xlmNp9SlndgEmvzkXNicXnEM1Q4LpWkyCxAxJgBP-U2clDsgC17rcxbO2htDTJ-kUwgceTxJRw58G-RTkDpiK506ajsW9YppegCUlY76ENU-5TKkviswuc4vyoYvXtM9YABmT3mMUaDuM0SJpu8s3wbVAqTu6Af6cAq-ztS_zGL9H-LMRGEMyXnAa55WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متن زیبایی که بالای سر یک کودک سرطانی در بیمارستان بقایی اهواز نصب شده
🔹
علی معرف
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/671849" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f0f88d2e.mp4?token=XXge4Jk6wzQBaTV2AUJ8PGYy-lh8CqokkvtxPlJFGLX0TrpiClDZg3OGSMvhbRtLop6oFH0bwPDdxajJ2qyE9DkISTCPeLBvAcziuQCiLUTxxz2nmdh3jt4UlVjaTTNgVgWG18Cx2eRqrzeUPFGsCB-JA1ZDlusCJRlpQbq79V7xZ--Gteg6r5YHn_3twnTVG6nS4j7uXIYaLCOXCAb56l7hTxH0VDDKkzRlCkHC7FfEf95B3cCA9k0eouq-C1MZX9YAy80dVi2tPRMWTQqKPXu18Lpm7S7Kjwag_nkRyTGVtaCbRa8EWE7g842SOfYGjRxjn7xjNUwFj6Te7TjmLZcxqU60HoDmBzNsoNA-fnGCE05yZKkkQ9YJG4Ggh9F4SSdTlkZUGmJtZbLaQckZ-MboWrJBGaiYYS3hr4J2hAIIN2G4vELUukYw8AQxk_gDRMfPA0ADjFw5zFsogdj-QSIfJq8gN0wEB5M-nin-oYpZR2V2Q4V42gmnDk9iN1Eg2vLXKlXOz44-t4Y8e9CC5g6CF73wnebJaQxLbkjWPvCtC_XPHCa6uzVK-iaULKtDwp-ytOOHPmT90Aq54SIV6b8JSB20k9UT2jR2YNkmxANoeEiIuAIh7ni6C4eyorSH9YF4ssM6eDQTL-ISjjj_ofrBER_GVMmypxtaa0qRUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f0f88d2e.mp4?token=XXge4Jk6wzQBaTV2AUJ8PGYy-lh8CqokkvtxPlJFGLX0TrpiClDZg3OGSMvhbRtLop6oFH0bwPDdxajJ2qyE9DkISTCPeLBvAcziuQCiLUTxxz2nmdh3jt4UlVjaTTNgVgWG18Cx2eRqrzeUPFGsCB-JA1ZDlusCJRlpQbq79V7xZ--Gteg6r5YHn_3twnTVG6nS4j7uXIYaLCOXCAb56l7hTxH0VDDKkzRlCkHC7FfEf95B3cCA9k0eouq-C1MZX9YAy80dVi2tPRMWTQqKPXu18Lpm7S7Kjwag_nkRyTGVtaCbRa8EWE7g842SOfYGjRxjn7xjNUwFj6Te7TjmLZcxqU60HoDmBzNsoNA-fnGCE05yZKkkQ9YJG4Ggh9F4SSdTlkZUGmJtZbLaQckZ-MboWrJBGaiYYS3hr4J2hAIIN2G4vELUukYw8AQxk_gDRMfPA0ADjFw5zFsogdj-QSIfJq8gN0wEB5M-nin-oYpZR2V2Q4V42gmnDk9iN1Eg2vLXKlXOz44-t4Y8e9CC5g6CF73wnebJaQxLbkjWPvCtC_XPHCa6uzVK-iaULKtDwp-ytOOHPmT90Aq54SIV6b8JSB20k9UT2jR2YNkmxANoeEiIuAIh7ni6C4eyorSH9YF4ssM6eDQTL-ISjjj_ofrBER_GVMmypxtaa0qRUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حاوی تصاویر تقریبا دلخراش
‼️
♦️
امروز ظهر در خیابان ولیعصر تهران، یک اتوبوس تندرو BRT بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت کرد
🔹
این اتوبوس در مسیر سرپایینی قرار میگیره و با ۶ موتور سیکلت و ۲ ماشین سواری تصادف میکنه که نهایتا ۶ نفر مصدوم میشن...
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/671847" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: اگر تهدیدی صورت گیرد، امتحانات نهایی آن استان یا کل کشور لغو می‌شود
وحید کنعانی‌کلور، عضو کمیسیون آموزش، تحقیقات و فناوری مجلس در
#گفتگو
با خبرفوری:
🔹
تا الان هیچ تصمیمی برای لغو امتحانات نهایی سایر استان‌ها گرفته نشده و امکان آن خیلی کم است، مگر اینکه تهدیدی صورت بگیرد که امتحانات آن استان یا کل کشور لغو شود. برای جایگزینی امتحانات لغو شده استان‌های جنوبی بعد از بحران حملات، تصمیم‌گیری می‌شود.
🔹
بخش زیادی از بحث مثبت شدن معدل یازدهم در کنکور ۱۴۰۶ حل شده و مورد خاصی وجود ندارد و اجرا می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/671845" target="_blank">📅 20:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGySAFH5IWc8xNfaHwbmJrqUzjhSunA-uiQYChwV_bDF4Zz09ltHpA2i1kzldk321bAGRJsxUZFnCnH5jWq2iWMP14oLkTzkvheCmRS21Y7k7q1ClWK7fJqxq4Xvrm5IbOWH1M22sDYnSqsHljHfF3JN4zvevxpaueyRiHJcCWfcoLJlJ_EzfLPsUM0zHIyZZYwbVYHPZS27KaPRv6Z9C8DhVtadfsRRl0VteJC596ndB1ipezF1MXxGI5oTViknEUIwndwRUIZaDtI7pUQoFWR4uWt_0up1x4Y3k6XSOJRjtSDmVURfaOskcsRkcV5LHH2pfJaZ3T2_aKdsZvZY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا محصولاتش را گران کرد!
🔹
شرکت سایپا امروز به صورت رسمی قیمت محصولاتش را ۲۱ درصد گران کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/671843" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96a114eacf.mp4?token=c-cre-P_msnD4V1MhYXrBT_jHICQGy0n2d2L7frRGi23Q-VTz_DymxTBLv7tvqi0FsppqEK2Qd2-b8uY1DRMxpI3Rrw1w9B1uSZi94yahzuc8WAYltECuRaXa2KN1Y91FFXJDzf6w-wVoS6JqATCoYAvUhel0SDu-clQdwdH64TBg_l1AfDvgSXDiu3BheRyia8XCktTNS6MGvyvUalAY_-eOG4usBJypxMSa-K8kySc4oj6fQZGhIN2XYsmzl7N3a0Kos9Yl6S4lTtbXhHWrSRN542hTZKGHioRkubA8HvyX8CyDHN4HSBP7S-qhoRL2wTOC0wvm3d-QvMMfiO8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96a114eacf.mp4?token=c-cre-P_msnD4V1MhYXrBT_jHICQGy0n2d2L7frRGi23Q-VTz_DymxTBLv7tvqi0FsppqEK2Qd2-b8uY1DRMxpI3Rrw1w9B1uSZi94yahzuc8WAYltECuRaXa2KN1Y91FFXJDzf6w-wVoS6JqATCoYAvUhel0SDu-clQdwdH64TBg_l1AfDvgSXDiu3BheRyia8XCktTNS6MGvyvUalAY_-eOG4usBJypxMSa-K8kySc4oj6fQZGhIN2XYsmzl7N3a0Kos9Yl6S4lTtbXhHWrSRN542hTZKGHioRkubA8HvyX8CyDHN4HSBP7S-qhoRL2wTOC0wvm3d-QvMMfiO8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شواهد جدید از کمک امارات و کویت در حملات به ایران
🔹
انتشار ویدئویی از یک حملهٔ پهپادی در بندرعباس، بار دیگر نقش امارات در تجاوز نظامی علیه ایران را آشکار کرد.
🔹
در این تصاویر، یک فروند پهپاد از خانوادهٔ Yabhon ساخت امارات در حال پرواز بر فراز منطقه دیده می‌شود که نیروهای مستقر در محل با سلاح‌های سبک به سمت آن تیراندازی می‌کنند.
🔹
این تصاویر در حالی منتشر شده که بررسی‌ها، هویت پهپاد را تأیید کرده و نشان می‌دهد ابوظبی، برخلاف ادعاهای بی‌طرفی، در حملات علیه ایران نقش عملیاتی داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/671842" target="_blank">📅 20:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DslhzoPQQw36zUGnNwFoP8S3DgsPO_iVMISuLL9xrUaC6sNResiNvr_UQNIOxwbrtRzWJXO3J65HawBSisDM1jOueMtzZquasQAeLngKrC1ciEmp-5z-GzAiobrFzJ8vDe4ohYQ3pbDRT4mtXm-gMPEeXLuWypIu98zsRvYsbdG9uzX7hI4O0DglKJevHuPKTcneL8R3k4FQzZckPQspiT4neRq0IDoJK7MtsDsUezvaeo9HFHITsHIdlPpoF2CmjEQ3f7Bnj5GntMKL9SSYQ-h2doJwHZIqoKpAKjfXkvme-fzsSDbBNwxWWlqwDcgaidUSuGgIEuMfFYhuGr92MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور محسن رضایی: تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/671840" target="_blank">📅 20:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671839">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
وال استریت ژورنال: آمریکا در پیامی رادیویی برای کشتی‌ها اعلام کرد «مسیر جنوبی تنگه باز است»؛ یک ملوان از طریق بی‌سیم گفت «گمشو»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/671839" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddQykGpyjBJoLiAo7lrGZHLpLg0qLfvIPzzCzPUWtFt8dzvjNw9ybbWmPh6q--flut0Usc7s01RSuGC2CR38HmVi5ooqNyB75ygLyICwZhPz9uEb42H6q4tv44byEhyNHlCPL4ha7xANEyKZLU7AU2ATBVnBNc4s3ZRHdGVSewvz9l0voDibvC50N2BXdJWSvsjEBRL6ea9SDXTuR4N9ycvaxvxGsQ6RxLaoIlEckoS3sv_3mLPApQnFF9w40eWhRA6OXHehBbN-n2ep9pMhI_r4kQh3hcqjJ6R1qWBfvB-e04telAf7yS28kWLOVdN4mxLZoeSKTq7IryZtMPU09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دقم عمان حمله کرده است
🔹
این هتل به طور انحصاری محل اقامت نیروهای آمریکایی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/671838" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO8dpAI9yHEDuLBCoXkYVqJr9IyfwacrKMfQJkYm4FB3rMugnhXpbn7TzH2YwwOKKN8cMFYlz6nMmdhn-j2JpWSuc_1r2d9kT4eOGMEs3gvb_lXE2ZkFAmtJRfQUmZWjgPtSIbZXPspRrQmS-UqdJrVJjzj5uGlOvUi071JbYqL_6IrIHMRT_fw3JDcAW6LWNihr2oha_30KuemzF-r-b0z7du7SprTHewUIA0SSgOCTJDgOOCORjtdl3muqJyEJa7WhT5XkWMgN2jVkwnggvxYiVBB84NCfvVcB2hczw7tStsozmfx5X1f63G_ePqndYW6IS42MAHaQhpNofYwvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ست پنجم| ایران در لیگ ملت‌ها ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/671837" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از مرگ، فرصت دوباره از خدا خواست
🔹
00:09:00 توانایی ادراک همه‌ جانبه افراد پیش رو و پشت سر در صف انتظار
🔹
00:15:50 سفر به سه فصل مهم از تاریخ بشریت
🔹
00:28:20 خواندن خداوند با چهار اسم اعظم، برای طلبِ نجات
🔹
00:37:35 بازگشت به دنیای زمینی با حالت سجده اجباری
🔹
00:50:30 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
00:56:20 علت تبدیل خیاط‌خانه‌ کوچک به قصری باشکوه و عبادتگاهی والا
🔹
00:59:20 به میزان دوری از نفسانیت به روحانیت نزدیک می‌شویم
🔹
01:05:10 کوچکی دنیا نسبت به عظمت آسمان اول
🔹
قسمت سوم (صبح غیرت)، فصل پنجم
🔹
#تجربه‌گر
: فرهاد یزدان‌ستا
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671836" target="_blank">📅 20:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae6595c4c.mp4?token=BGKCL5Xipg3bj5aXmBrpyZ70JuiTdrdYI1a43QuoL6B-1Mebbtbiy8L9XJPfVycDdWHy6ZOlhGmeLY1VB1zx6vxWzkPlGw-TrYZM8XXVHZ9EuYZhh8uFq0-y7AZOT9-XXunuU4_5AmO7KSHGgP3NxjbQr-wqCXRhb-KhwsFqQ3FCh4VxMRdaaefap6ZGNlnvEZBJEw2aK7LPx7QrMKe2Os5JtGrR-T6NCnM_3sNSOR7w-ciceNbRDkq0-d1b0ORr4ov4_xtfjlSF_HW1DbJ-GNnoxsoK8S2BKhEjnE3Oi1Y7AV5wEklWiscYgM09Np40Xf-eVs5kvNFW5V0PzGEing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae6595c4c.mp4?token=BGKCL5Xipg3bj5aXmBrpyZ70JuiTdrdYI1a43QuoL6B-1Mebbtbiy8L9XJPfVycDdWHy6ZOlhGmeLY1VB1zx6vxWzkPlGw-TrYZM8XXVHZ9EuYZhh8uFq0-y7AZOT9-XXunuU4_5AmO7KSHGgP3NxjbQr-wqCXRhb-KhwsFqQ3FCh4VxMRdaaefap6ZGNlnvEZBJEw2aK7LPx7QrMKe2Os5JtGrR-T6NCnM_3sNSOR7w-ciceNbRDkq0-d1b0ORr4ov4_xtfjlSF_HW1DbJ-GNnoxsoK8S2BKhEjnE3Oi1Y7AV5wEklWiscYgM09Np40Xf-eVs5kvNFW5V0PzGEing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام‌جهانی زیر چتری از دود
🔹
در فاصلهٔ چند روز تا فینال جام جهانی، آلودگی هوای ناشی از دود آتش‌سوزی‌های کانادا نگرانی‌هایی ایجاد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/671835" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx0gloHCQsrcIaCVoPIMxNsy0Bbdl2OZWKMkCYVtNzp5PEZ9XUkL5-bFq-Xt4aifEJVzcxiPQE51PnEu0dMoqQQSvn1Z82pPnlQXckFhCiKGUvPOEh9Y10oF1BP7x8cFy2sWza6E9QifhIPvZJUr5FfebbV9RFmzzAmlrm7j15UC6uEb3W150yfcy1xHFpYQSOW_4Qv2iD_ohLeZn2-Cb5zxzGpwLyZeTNI3cY5z1UlcNCI-5doDsd8d7uETgHGhSyCkmooLejtb8NQrRlIsFhSuurBrqNXInaH170s0id8HFWa0oDfzpAu4bDzkwGiwRt6VLJYe5-gjTlv-LNmMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای دولت دبی: گزارش رویترز درباره وقوع انفجار صحت ندارد  دفتر رسانه‌ای دولت دبی:
🔹
هیچ‌گونه انفجاری در مرکز این شهر رخ نداده و اوضاع کاملاً عادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671834" target="_blank">📅 20:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای دولت دبی: گزارش رویترز درباره وقوع انفجار صحت ندارد
دفتر رسانه‌ای دولت دبی:
🔹
هیچ‌گونه انفجاری در مرکز این شهر رخ نداده و اوضاع کاملاً عادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671833" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671831">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma8vsR_9Fv1LHjPNM5muTuwAqI8l4fXJqzjEJIVL81S6gWbeQC8pfMZlU66YMGFgDQFzMmT2lW-LVsXp9-KRsN0N2Iz2YKsx6fDWtCuc7IFw5tx0u1vW8mGxn_lZ0c5H1wNoBxHo3G1gd-T0D2zt7hCPvss2oBIGGPw0oBMapK_u0EuYsJRynxuJ8H51l7rJGMGxJ6mmXlaRQx6RjXQeUhf_DGlOLDXrAAyyUIivUHJ9xJqlESCRHk97IQuoOKndii4JTKjB9AfFziBoGXkSiCscrwy754YsShYQboJVaFeEIGhg5fgenQaMIZ9tvvor-LZ355oOysInyyM-QCHWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه‌های اجتماعی در حفاظت از کودکان و نوجوانان شکست خوردند
🔹
شبکه‌های اجتماعی برای محافظت از کودکان و نوجوانان، ابزارهایی مانند محدودیت پیام، کنترل محتوا و تنظیمات ایمنی ارائه کرده‌اند؛ اما بررسی‌ها نشان می‌دهد بیش از نیمی از این قابلیت‌ها در عمل مطابق وعده‌ها عمل نمی‌کنند.
🔹
از ۸۶ قابلیت ایمنی بررسی‌شده در تیک‌تاک، اینستاگرام، یوتیوب و اسنپ‌چت، فقط ۳۵ قابلیت موفق بوده‌اند.
🔹
اسنپ‌چت با نرخ شکست ۷۳٪ ضعیف‌ترین عملکرد را داشته و پس از آن اینستاگرام (۶۶٪)، یوتیوب (۵۵٪) و تیک‌تاک (۵۰٪) قرار گرفته‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/671831" target="_blank">📅 20:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671830">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام نظامی یمن: اسرائیل برای رهگیری حملات تلافی‌جویانه یمن به کمک عربستان آمد
🔹
نیروگاه تبریز هفته آینده به مدار بازمی‌گردد
🔹
آیت‌الله جوادی آملی: وظیفه همگان، حفظ وحدت، حمایت از رهبری و صیانت از نظام اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/671830" target="_blank">📅 20:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671829">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
برخی منابع رسانه‌ای از صدای انفجارهای شدید در پایگاه هوایی الظفره‌ در ابوظبی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/671829" target="_blank">📅 20:16 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
