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
<img src="https://cdn4.telesco.pe/file/NIgsX-F5S3PyaVtJ5VpKA1y4Td7aSbKgBI7qU3BexUaft4OXLPUSb8OSUMA9OzBE_cXMXh05rpch477uvZrKwsxmWtOh9rEbVNUbLBGl4oLeJ9Fql-oMebx_mG0ax3d9U5fpkI96kXyLajXIuZPBifCmcO6BggSysfk2vDCeWgPgdD4NtJ1RqTPSVAHCPhPCj_EP9BNAMtp9uuFxvekaDZE9JnMstazSfxX5R3KGsKT4fSWyFy6uGVQYyAzlColwuSCfetaVWLY5PGuQ0aw5-sI2PM5djfcTJNekfFZEsYtxoHbwQjFnElMdH2JvtNBR5ZG3BqnvMlGfJyK55zbK1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 00:56:25</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 287 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrWGa0v6VUuXO-4rtaP9ygD2iLUVN9BD_4vfaCdDEDyDnZfLao7yQ0rcTP--ROZ0yptZIL3NiwgeK0ZX0UpZPQB-jSrg5ccwF4i_Yw6WC8ViK4RjN2DkpuaK7hhHqIjt0ri5M1CFN_58lXwIE5lIxcfKk8kn1L1WwEdfB0vDuTTG7u3rBwqqUxfOJK2AZfxuv3cLoZhB4rX_URawPu20YDvPJWZ7YZyGmq-N0SFO35n-6LMEP1DadQ7fyugobVW4atlZoBrfVVzmPX58Ln7vIAfM6AW7-xKWRaBapq_I4B8Y09DkS0jxF5VCGc72tq8_Uf5lvyGDZdq9hQ7dNlH5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 513 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=j2PLq1MBE2zEbh1omKXknQuKj61KVaNc1SmxSQrVQZJ4IfJJ0_P9dftfRZjuFfq-8puVL-vcyjeMYjAWUa7u_3KQH88UOMxLxdDCns91vDlF_6QzGh0z9FgjJWVt6cm2CwMEMF_8lL7RDAhCNcnRtXt1C_vMOJTPVV9l-moRhbineTUAkLxGfLTN5dLmD6mTLaOtuPWoy3Gz7mPxpMBOkCxZ3eijQrcus3mtrfSbZsedE7QytKUBsSbqvB3FKxq6ulWzbN1MmXpMYQIMVoKzzLgoGJRBiIA0UWK1-1Bvn572OBLt4UWeC48MoMR_fMDeCYCrspf3jYdAFZXUy4kJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=j2PLq1MBE2zEbh1omKXknQuKj61KVaNc1SmxSQrVQZJ4IfJJ0_P9dftfRZjuFfq-8puVL-vcyjeMYjAWUa7u_3KQH88UOMxLxdDCns91vDlF_6QzGh0z9FgjJWVt6cm2CwMEMF_8lL7RDAhCNcnRtXt1C_vMOJTPVV9l-moRhbineTUAkLxGfLTN5dLmD6mTLaOtuPWoy3Gz7mPxpMBOkCxZ3eijQrcus3mtrfSbZsedE7QytKUBsSbqvB3FKxq6ulWzbN1MmXpMYQIMVoKzzLgoGJRBiIA0UWK1-1Bvn572OBLt4UWeC48MoMR_fMDeCYCrspf3jYdAFZXUy4kJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7eolAnpojKjboA9G7xmB47NmqLbkv9EkB7yHOJ3xeAxsSnQRd1pKxMgq48eXz0Isea8_9nys33EJCTDAccrfcTC8mMezML0kEkUk6A5o3FvjGn3sgY2srljcskCmjlXdHEGHNTtQQ-K9fY6AzlPMxn2jXUNVGK6TvytAHY6JqyNbesLDrKsp2FkAZsA4WVOWm3zBKJRguJ2NOi121jspMcJ8TR5niXw_gEisonuOAMNnLWBl0p9in2AkuIBm8byzPWBd9v6daxA51itvJKtLnnjXgijSKlR7e00OzyQ_kzN7-t1TBslHZNURt6DNGfAoIv5XHCmrUMUI0BQL8ICpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 633 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSi_KvGt-1c8YsgZkv9NfhC4LZEAT6Zo7ed2gPREm_cmngjM8EgOu7ERWb8thlLwykmxas44jvv5t2kbAl_fw5kBnGqm77y-5rJO1mzfZHE8ZYb9fZIKwd-oNxze5jCfxENBbCSZ-eV9TSZ-oVeFohSY0iHMtS40r5oDXJXFaHy6-hVcZl2-ZQWP0b_YgRuYFI3k4m7K8T91UWe9z00eCFoyBe8hAvzS2YWV5hqngN75jH1LZFy_nqajR0N4IEQHFYAZK6iN2e_qtEj0Z6yqcG6MI-BjXvJp_GHbfcThTU7AcoQFbHyGDpC3BpbKX9DzCTVxqGAPzgOSGWBdV3AKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1VT9tSKyWnYvX6dYZ07m0uiAqKpy8Bsn4ei60O-4UuKXK5xrhNzO6MfV-x0fWOlix8blc0aNLuY3S9eez6yz0woydS3eRtQFmtMhvv1VcBgdMNWOgy2twpzFj1okKd26OqEWVRSuTU2p0XVgx4RoiNxmNctJoL_Ool2AhLtNRrfsYT_c1zpVCruvEKkr0yswsLwCFaLzMs1dH4zo2WDhguq2T7Zv4fTy7phEXequ9eXBC8RJXams-uzJZO1Ak_qkzAb2A5VXjJzTwHuXM5L_NpGi4t1KdC25Hl30ORIXPOJlXmnnp06pi5A9JbjCCFq89lebepLhTS55h0sJSVDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg0czVheKPdyU18dI6_w9-TOeSfkhfyrXj6jZ9zLGQQ9DqmSC8TvD5vr07n4xGoAKIbR1njdT_8MiS24lWoGFZg_rrueVoKMZHuU88sQpfXxZlDmSD7XVy0uqYPq2CIf9zHzHFsVDnnjRH-0rVKhVNXwrA6p6w8rebGGQ-Q9cWK4IjP0atL-BOD30vSRSt-BgC5rlQvoYMmq3zYrYmO4y7Ma2QbJXhGbfP65HEhPI9J_yBxf6g0cHDJWtL5G1I-ZQUqDuQ2jTv7nAQoTEBSA_PzVN4gXEx7DeO7wca0fIK00DEdaGujVV1tV8Ea-OqcfJnfBvzSk0jGfNgmV__PkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKagFrykCvSVnJantoOPMhBI4ErK3DLAPq5LvNlEtEr7yHVvkMG8wPPdwVI9bFxRrb7Rz_wd6Vk7Jskibr6kq3g18V412BOkgvma6OCTzSuhOQT-kuz2HS_51aAYfDSn9XTJv1OCCxLJzrU_thl4UVSnImNsg1hVLmFJzyTEE2v0zv-YFFyOv1uOcn24XR85hWOIZ5YmmUdlYp2-k1QyMcYYxxrgu1orIQqHTgufQfxGmF2ZKd3ZxPS90P0C_oLUWsAeyMAoNR4CsozqSAwZCCHmL4Xsq3CF19WsOarVC9fOjp8pYSLPsPLgVLx6uDDece-Vq0rqd_90P6xo-83ejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APDLAxMhLuDOmhC917XgiPKmK4W8pVFb4yXc2XOLR7lpX3a1kggVsqyC5sf3XTeVxNPfFpJIkK2LxpaZib-CMF53T1Ok2L3Tt2_mu-B5D3zopNxtL7NElsLa2c_7hsTGT8gH8kYCcB6Q6S-Xfv37WcJkE6q5xSG6Cc-UlAwqHCRjgQAiZQ_pQD1HQEb_bgFSIgAPLjTt0dAAntAYaVdwxWgNxnAQ2liXsz8AzPFbxe7AxO14Ep52pCL8nDDDfDUvN5K-Rww81Quvu2fIwVvLn03aeY-kra0STtndzK-xZNmhkQUNOmWqC30_1Dl73r-CTnPyzY0Yxpdguv_meFsTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD2bCtCE9PriiCG1JbFiTYpvTWYVYbZdXZFbcUjcyX4xTUs7ZuxRtzIfFAjzejZu8oum8jRcBO4MlL_D2-EE_KG5Wvd1d-XOu7SgMF5RJfqUI4paGVHVzQ0mcbnQQBnCurHKWMIJZmFipmR1jqRUMR-ihjFnPEaXGIm7b_yB2fOM3ualpZfTskRpWNZ5yhiLYdWBXWikCOUg53_keBW8-ZDg1GCFi0a7JqPa2jHzxc_2Axov_taI4rf3A_md00dVrFP3c5Y7QV34RzH7lIeK8Zu4AHa-pJ9BKFBycx_5_AGP7-UlX6AJnnpwyPVmuEimA4Ez6SLGuwkLbBBNqNfkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXsn-OivGhSnrFMpv_74WFoK-ddTorkEpeEnQzGGtI-n9pmugDWA4w0s_Z4_ycz_CGgBn4AZQczGu2W_clNBBL58OZ2oztDujXfmt0W4O9hCrAPd6XNSiKF-OmDxSf69VX0Zs6t-26IIYo93znT5wZ-6BmNhAAMrNXWftRgIA1mtDfGqadIbhBAGsxbbsZZDakLM1MsY_yoSgtFO1ahkNcbQg0Gh2_WLdjw7lMCtevK4uGy8APFRT2MhM71O1_Z0kssJAt3Jq_z2M1omDZr3PCUkI2HTYMhMWP0pjFrr2ObAruPUjsaSOBsBEkglblhgZ1oQ83SOe9X_1vLtaENBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1SbghODtJERiXXGKuKVZhOPhX4ndkgiKqsIlvlB_tR7hE3Fdfp9xc9YEwpRbi0mYh59l6ZPs7tpt_Z8GDyApbYbRICEqPQp2axYZHKNtWIdwgJ6z9VJIfcGgbej_grl0byTK3uJaGGm_7jeqWXloWrCfZJk0PkPtJg6MJI3NTIO2aHL6KPu_YnZs1CrcJ5Lq9yAL5_oZj4zGKYcsAFwWwEa637_S2fOWcjYA9elq4adfzJhpTb7dKef0JBqexnAUs47PBGb2zpyc6RMvACBgJd_QwMo28x1iDE2DlAFjcwaPxh-Nr0uWoMpLacH5i9bdginSoloxMKgWwregGUZJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOPLLLmsyUiDLHgeFsTfTnzeK7vo4Wpob4i-RFdPWEKrQKUIlMSHa2ysCsqXfAzmYLkGjcrueQiHvtGpRLGYm0OJP9HVexaRQ1dcW7VKXoG6e-1BGdg4lNiKpHoe64XUpFyspYLHCzSpf7WSM2fTENoBvRPDGCJfOxpk5HVR5KmMuCjTH-ra-fWoC8JBXiyy_ba7L5OfGMkUNYMfXPA4iPreyufWN6qs7WScedEpW3WFhBampdytjoCThdt8EnpDcqOMItj8XNyhIqWQMDwZTaVOJkVru9TMxMPk6LmhqS_KQpmGMyT9muDN3aIWpCZ_vhnvpg1YY7aeJ8fA0vHMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltnjKXo_09Qa-x7xlaQdDKmPu1lFfWV2PvCzP4Hbygx2Pi6nR5zP9T8HlJT49Cf1AQcGS3EtEx2DhBU_3xd4J9A8EkZ4q1xej5Zpaj22s7Eh7BEwiMJvB0IHSui_bRhLfEJ2zfMs7209fbTAFw6Hn50Xct5qWHZL2ZNR9ub-SVVF2f-nRiggMU3W9rss5Z47JIZ5fVP8i85ftBGSC0aapHGzfbmcWqzcpQER8ae4Hg8YCLjmawQFydFUv-Xt2VxabzVD9ey9KGIX6Y0TM2a21lTUTkTCub0xJCnvd8V2y1hDAbE-CEAePebf9PejKfxFjA1zMY-oY5355VBVf2wFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JusF7oW9pD3BeJJI-FtnNKYYbiKlvxnS1FrR4SUwazmjhFokLUznSfKNEAvc4a0kftDeIAkPmUfUj1BtgfFUgd39S27wrNGyCqvOyfegFb1VNMBE5PtOkzy1sjtloyluPG5dBhJli4YeCo152pgn5EGC7jYiLm1XgMmS3QOn5Ic1vA-856IYgIN_xJq_DdfqinexQHjcmSzKNHrheUq3GKck4f0eNIq4Iln9gQ2jPEHuGT_Q8A0GSc306JIUJoW2Ryy5JGyHO9uCrLZ9jao8FRHIQR217WF3TLzqznOi7EGIfFIY2kS6irnq1K5etA-OAqD1D36W3kPW0EiA3G92tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF0Es9K3YL9jlA_za9hCEanJdIN74uvUVLNRV8tEopuP3orYZPZVPpC4NK9RyX-z9ZaBxhKWPdN5xUOOMyDmpqdbT0a8SLAo49NgwOn03w6Wjto_8pgsrcqG0lQ5hut-qULk-Cf7bT63rL9HsnC3T2801h_hTjvfW4-ddaPuZxF5KAhJIKN2vUR7QEzk3AgBvpETqFWJWEyysPy3sKkqbZm1s_20sGMdIgIev_v2rioFy0B9VbFsCS0p23YLhIXJFzkvZEVlQd6qtzlR-HOrbukKc5tootcAhr2hEItLP8UvaVYjcX6uUjkjQ__90JrhoTSF0tdu1D5UI1D6qI6jNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knKYBX47GPZnMl5jmD0WinFT2OSbaCC7AfwFSQpUnLTg9BY-nbx6Qe6btQxS1Pbrfl7KiG38tZh0MusPjkeEmssHZKd4lBrRnK9Ju7VJfFumkmCAqV9WBYyXdnsyRldoNDHS63b07tXTx0Dg4NoMcBCz03SK1w1vsw5xP5Qn0VuIWBEyyXzEqYS17Ovpxp8ekve039UWFdOgOlm-4cP9TrJVcAvQ28ZlANqJiB4n1M4rJpbloaxbSVy98i3DKbIBgU1neMFBS7zlZzGoR96aACiBavKvhhf5fnSg7rx5yhdNp8qMN1AEm-OOpUWVvLzoTJqvWaea1HD08nibs9AH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SupqP8c2zxpt5RV0OwTemB5kQ31iLgCUcvLyAphDh01H_aL_JlAzFP0d-vsppEoYaE4yK89xdSrS-djXWJkrUxJeQV0fXVYSFy2nesmmIx8ibss3KGRzoNzApT_0vu4IkTD_A7C5LQLtyD0lSNteO7H4Gj6jtO7I2lY2pKi73trQWNGuYTeuCYK5L1mDHbIvwCL3yO4IlLhCJLk7VUl6cXrJLhG9w82rXj4xygpM2P_U2li9aUIXdw3LOgvI8xweufwqsvRf1bg3ldLa_1ZxU2iKiqP_hho7AlLDfz57MBIx_bfvFk_2yd_45-I_RV7y20h2oLsPM1PXvsJENcVnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0dWRjT8gI-Xhd834vMSsLPi2cI9CDv1U1X_I67vLHx7qTMws1IfPJWGuqGetb1dt0s73vlTntj1ri7piUFAJwJEsNvSq-_wp12eK3pOmtEESfwYLH2rNsotXuQrw-iWkPZ4tA3tiLovA-XfIG90K1NHFHbTdOqZHjye186H8heRLXXNAD4d8gjwWcgA_c8C_jBEdn9OiF4V79sSKKBDIr8LVR2tORVWzA_86xk_jBJ1xXrT379vT_3tMaWTGZKMOL5pZa0G5C5fvFjQK2hMp_QAnKsEJ47Gd2gao4rI32ra-gC5zHIp8LPvGSseQaNHlyqTaqQo1IQEhBb4YKrtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iy4NkOA-1hFek0Y8ahRRxOdHt3FQUfJyVF4ue9de8IZlpkI6DDwRr8SXNfafyuZnmSyHgzATu7CO5bvnhXwLWfaD23KwuK8tTZ3AAvig7rWjEQQ8vkXyHvF33NC6FwwXgtx08BeqgydDzcoTnXPvBZKtPDXmD2tSYbTMilIZkpMsA5dkaGuPASCYap3px9nP0KJkzIJNHyzGGC6cYTp3YFALom39E8tyO-cohcvtMmiVUnHsQRJaGEOZSD6_z_7z8nRHNNkbn7q7I1p25AbeMpVw_ATzbrBIDyqj6ar9yEWqC2Z0_eXCpcTPoUlXdiLUEy5DDaDaiBSpo3pl1JlbIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KprnXD0g6JVK4qfYfgRdmlMbBPeMKo2a6Qcjx8G7gSumaMCZyoE0-7Kx1DZAZXTR63JcMYylC9lmPTgqWWym3DD2g6-0vj3JaPylxsrO9a1ANkiTn18oNJN62tn_sp7PrYziq2Mk_8Cfg0ayDrDPxhM4mpoH_t5bWxqLfJUwqei2kb5709oVjmIacHc0y0pfryGO-6dnKBVEAyfV8ftBPu2M5LjxPXLem9UXFsE2C6vwAaOP4d2Xj3BMxuFkfV6FZjaMk-kVigP1DVGGN347d5rfAaES-ivI6cjFOKhuO9fv5Ie2MIFOW3vc3pHhJna3t8Jvd8iC55BLZbiU6pdHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=cZMteF2eVNiTo8TjIUhg9JYyKq8Nw4jFO-uzNw2VWe-6C_J_lZXVYwqnik5uyZURgLHpyozwCMG_xz3XDQUo4I_1iKrB2Pzaresd7DVjNcyrxVTAISFqPlqKTbtPajQEnhnk8BcrXBkT37waK5__xyhJ7zRr-KMH0bR8K8A9P661MrYVBWuZVfTnft0-xbfQ1udTH-a2PlbU2AhcZiKxmE30HgyjbP6-Pbr1x5P1L03pZcQbw2TX9ISLTRC0OB54Cwnm3O3obsMFoGlupmFddu_dMsRuoI4D-oRZSUBqdp9jZuwd9xZeISPAZ1LG3odHTgTdQt4mYdMuwwFWIntPBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=cZMteF2eVNiTo8TjIUhg9JYyKq8Nw4jFO-uzNw2VWe-6C_J_lZXVYwqnik5uyZURgLHpyozwCMG_xz3XDQUo4I_1iKrB2Pzaresd7DVjNcyrxVTAISFqPlqKTbtPajQEnhnk8BcrXBkT37waK5__xyhJ7zRr-KMH0bR8K8A9P661MrYVBWuZVfTnft0-xbfQ1udTH-a2PlbU2AhcZiKxmE30HgyjbP6-Pbr1x5P1L03pZcQbw2TX9ISLTRC0OB54Cwnm3O3obsMFoGlupmFddu_dMsRuoI4D-oRZSUBqdp9jZuwd9xZeISPAZ1LG3odHTgTdQt4mYdMuwwFWIntPBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj421wHVnrLNsz09jlCCck8p-TtCA0aOvRxE9dn7z0LNJwPHt9OcQHj1FL_MbYs_R27Zmtq_VpzlfAtRmx7uphigVbFEQwxJ80_0lK3-UrjkhgD5AgBbzYEXOPihrItSQYBGfCLJQLTby4H-Dz7uWlaSoQScqh0IOgDLuU-gn0n0bNHIJylRNMovIcLgOalaAaZ1L3T9Uo6hc8cbRywOeGMciwKb2v_-V3Mmqzp-KlCWs3QoLjwHAQQ5jfk7C791kGGwJ-6ZS5izKvbgR_p9k8VEO8rF2ZzpiUAAk4yvIIgAjNwz75U2MefwYfktVoB82OIPJBkZq7Lrqhi4VnLbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR4wMQN2Z2rQ7_mzKFuV1CXHvz4mJNIJB4u11PHx1f66tUMVxu6992vFnBiRpWnx7aGTc1t0VTJ6JXMIkwTcNT4wcdzV_308nSvCqwU4JhyP7ODCTSrBD63rok6shoxbDprU0VsL6d9DRgZizeB-0RtJXqYW0-yvaQes9AkKF6FBQQksNE7uecpfbzeuyOc0_heerjsFpWh_erbuXPxdXU94Y_UfSdQR0uetAaVpD2hMfAyKJRzg7iAlt_uL2eFWfWXDByws2welsEAacgSOTCrJOiWQbhJzWrcqZnbS62OcrzV3__DIALWPxApAd7ojUwi7Wr5eYuR5JV3o1NN2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJsGaTDtPlMTULQxH_NkGz2LQTkilGogNeQHf3u3MxLIfAMEj0VCP46i56BdqlD1uQaM93djtcMjF48oE0bwJeVe9H0aiOhwaVuZOrVfZY0a8V8XqtTrgE0eh23p2w3l0OZZo1NuKEqCOgsRyq0bpuI2EUYTorwyeJap5Efje0-5H9a1l8nTK58o0538aT6cW5xp8vooYNhrtz8k4Md278cjvhi4HS5FK_16inE-HpL4UuWu4fPaaR9u_mLEEd0zFFCGvUQIHtuQojzDsanNDXY3XfxdMz2Z16EMFwRCq5_B8cdyAibaINbSQjlRr5AGu1VdawKDSCHlrYWW_8y9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGRXvJgaC4PCpsc0vnJlLDTcS2wheTmZJfkSWENcUBBHkMS2Y1q9F2nlt23YQUwtLzFK4Gno86LLbNesgEd-1ssqftGHjbuojFm-WWTfGKXOem_vKKcz-Id513gRl0ZE1xYR-vInsBiMgw4PVrdsctsWhYeZeDSRUuRpS5I7G7VXPxohvn4PoJwLoWyRS3H4X4TaFnPSb0qzijUqp4dTmtgFTNsjAGfNMbfdMVmUUpzKtCprHkLt_aWykFNAzaipgApx5nDZw2yWOIikURKLRabwmEkjHmQQzlW4xxMOBvQY9v9BDhszyAvow-YKSPpBhqYzWNbyyAHeofEGeuhY_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHlTrxeP4sb4bfgloaJqgeLmT5ciW_9Kt3uJsHWCT3UD6d9zjBDr4t4GFVxyXUn-ofrBkum-Bd12AL4VQb21KouBQxHAhF7PW2Dyt9Ut3TyIeQrTB2Fy1K-EzPPLGD5c7yRHsCm2X-ued92-EnLQV33IsrViDNY7lIIHYXRSl3QuEuufC2Wip6PVa2Ad2nahIPwhCdjLD8E4nqYZOJH2RZmv2I_3COwiDwtJ61Gjc8E-dml5wPOi52DxMClm-j1uiPcVZPSxCQoq6V3iNiVZCFBIBhdeCeC5nck4O8uWNPfQq_TO2n9jc_5jjY7ge6uI4UF_aEh8_tmn4nMOYjeBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuHg8u5XiCV3srqBoAi-SsKn_cb_EoraJ9qnXgScP0Jt0G5qGeggpZ8jw1cTQWvxbWeAaQhwSrjb3wKwjE1f22-VowU335oyelVXiOOPkdkzaZcJbO6byr6pevTniEp_A5CcJERCLzj-rHhe8nClCcBx4n8MJd20y0iABs4H-1GHyKN7EUxxeuvn7Jh2O9xoQDKxYRlQ-b0creXWMDzk6Qrx7Ymtd10lZV30XPdtdEJPcZvDQHVx3BX7lkRboA9bQBOLVArFEDYBGF41Ba0u_xYxyVVcf8gtxrrAjUBGcbfPyRqHCefHnY8iNULRFE8QXQkztM0PYORypBzbbsC4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_vt1zYmqMQCaiz6BNZWso3IxSCkh6l8SSsEQeJHrKbDRY102dsYn91ylpKrdRQnKOa_p1DWCxtXRnNAX1dV9ioKKMrYvZXcfjvjb8ZyIyrVJCYjMFNjkn-HtU6GO3uJuosRQvurHPbc5Ul7zv7P9JYU0U5hlJ30VPgtLdYjHVF1v2t2lJQFNRcqtY-_KXw8XG5HDVC2NcphBveJxOfOriKOCm3y0pZN1Mp_6vmjf2jSVlpK3xT-w9XYdnjbBLOFRWh3v_-I1FcNj4fLOg9yo9ITY_OFH0z-S2PSUQDuI4I4ToVEuy5NPTJ2gyLkDPTTZY_NxF4H6K4saHmYtpbXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjTeWqaXWjPgcanyZKjuo0H-hO6pOt0o1r7pwXsIkLJfs9WaVkSnDcZDd7SzrTB3xvgFpNgjAU7Txa5V1gRiNrM1xVRIFZFzgDM6Ma4m2GiNvp6DFQl9MVpbUv9DEJri-K45EfML23tiV0vmfNt02rW8dSYNRxndjUbX1-RX3BaVaW01ET1Q8btuUax0aisqoPBGcEUwUx30hqa8rILZW9HRpGuFPggzCzRC22NytR0YrWRVXvs486oUxdBGmVeSRPUWlAtbh4IrnaH9sWU8bfOd799oHaki2nmxUetv6Nqr77iskvqMA1GwsvcF3E61JQQ_K9X5eVmGlUmWJrPdZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd4R0Zu87x5aoN2VKZ1oNVlMDAVRmWfIPH2G0H84uEsGIX-lGEvbJLxj1sMOh_O0Hbh0csTHyLaKUG54KGzoZz4j2WiaxVPk1Rm7ayeql-ihge63v7Fnr29gSRjY0O-iVLS4BSzXt0QPPnHlTvG7Yj8kjlBtR9N9NBaAqCZlwVUNMLxwWXhG6TF2DoD3uxLW-2qhjG6njlcCJg0Gc6RHW6yZlhKqQBH57-3_NW1ZRspVWU2dpdFBQJpWfjNn6OHXFtWe_v86pQ1nZCsH8ohAlP0wEdVP9c7OQGYGlDyb2t1jQCM40YgK7171wy880zeC4iB3T0gNw7nG326tJsFQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vokv2BR4J1g3FfswAxShwUQTN5k_GJJD-w9NZTzyAZyYRtVUf0ZezpKBASE8Tfc1Oqsz_1NP6Bz-E3kWhCdjKgbFu9HHAFk9wv3nSBDZGc5fiSnQKCRChstpZBZvKDpopHsyI9dEDL2KPYzrZ_QDkLBRar9r4GFb5Z1JKHMufgVXoiSFnvQPGoqZH7qITl3yfSS6LlH5W46BY1vEPSgTIgh9Yjsqokmd2F1k1Ll88tJdKxIJHKg5kQI0IrguZW1vGjXajB4iULH1nJNo7rLpe-9-5gDQ9ux-ljFoS3qhl5gEE3kNNTyll04fWoy1QtVFRIsn6N95MbCmVd03Y1L4fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O79K_LWZL3iOrYEIV29p05SkzqR-hTl3bc_t4-ZxMPKzfwWS1sSYFzGnvSVK6XQkTRIZADqwt4CCdI2ECBUM_qsXzmJcnjc7OOBAvwwLabv0DQyLF4fO3UeU3JACmjFRqwiMIBNpPHXe4vJrFyFO9gIfRJn1VFFdrvU1Ut587Q3z1_Tx_FQXYIhkHnolpuebEfeM2g4bSrJLBT69FPK4JQO53GRHm3Qz8BQczUD7-hJNVUUGLhEoVBgmtSZUoKsXJINm0D0ILGxbG3axfhg7CsJ43juswnBz5lmvjMG_kMYBzvoqy2mZzWJxNMkBmxtOmDHBvHXlza-42P3qeZq78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bONfD2noeyK9XLAOf8R5iBWkW1lphHb8mKHpCHfPEOCDz6Lw2YtSJN8_x0gTZzuSaw60Uo2-fP59Ba1zDJlmf51-jQeeSF5x6kHQB93QxRxF1CE6S1pVaBCTVes2w_4zTB6Od0mft7-bwjSSj4oHB73fVP4NOx4_kfPfK1rKCQG7BG8vt6yjrKyrIOQINWxSIQmCNQ-EbE4jIAbMS2CTWzSdYRwt4cY0DZyR9UVce65g38L76Aja3h4K0R0uwBwHxoMtWbai7UvY48VFK2GVRe52jAoAIb6FZHlZM68965IOYrABQg5N41lyOu9DtkPERH5mrtkYkWguKLfRjsBe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7LJZFJlW5g6kwAQ86sNQFNF4BdnDYJKkw4m3GWkRJF3EppSh0rStw1ZEJyE0xsnL7cTCC19p3pZ1--vy1kazw-aJon5WtbFkD2RnHqG6hOfpsmjd7w7ZshVqqVgAr5e5rx-7nOlVICbjDHrTiai-3VTr-cOiyyFijHxfbrEjrjpmMoOyHiLkaaZk_L8AGCgXvPpJppbpRHzZqv8uhexPi1FCFW_zH8gw3GgQ14E3VrXmma8X3hQ2IC9dOZMEjcCDxtRKDzXyDpgWBIIHbGOisPdVTNMOuIe_b0oUL16kTiXxlq6nGI-bvidlMoh6R4vGN9cTwh87MCpewf2caubQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4RTUrhw24NN1Ojy0YqfQ4NJVVHusndBvRhbdBXVNwFhmbsai5bzEz5hBUe3YxnbVWec6V1pxvqW6X7Oarmwc7dsXycDF7LKhAZh-dozeXcUPY19Lr8oaFBBUWq4wD0ZVUVkJc9wvbpWS2yufvSCyYsOiuinFt2HzRFe06UYL5EGzxJDKmsWIyMuA8uGSH9j4VKYQfMIsMM41voyYD5BOakQnjyjSMBTSKANackHo00RdiLneaFTjZGjAugfKJ42i1u3ZMLiu-NYFiexIpLaImENu4PsKqEnJNv3RI14eyTRZjQRjh2QGEHxNHAPOrHnZ_XiJDrTc4q6RwZa3OK_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPuZGqc0TfsoH5yu6XpmrncR5TM6yuaW8e0UNUvz-Dap-RkG9M74aVSOaXB_pH8JRiiZIXSpP4tXeNfsPHgphD-B1y1aas8FLWMTNqnS8dObsvBGM8S1bHlQgDan5RWOHvnQgj5rezFrCAB7Eke45qcAhM1u1SnrtgXoDQWlMVmcGvpm78_NotNW59uVm_Z058ujAZmcQ1SM1sGu16osnwjdY8YYug5ggl2uHfbZANs6xgLlhd9541MCE1v0CzPcIJbpL_5SgFaCcujaP70E6oaqy2OsTRb0LvrumSR9YfLY2-MiOus-cnNDYRaVav6LK_zLvzPNyXLEi01svtHGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n21mkFkiFHWfkvTY95aQ7yjgXGA-cEZzTmrz5iaCeZTlFnsZh1sIYwEGE4iC4a8YtoSjbK7us-hR3VEHfrC9SUBNKiIvcAMWBkkHT0dHzu24TSD5j4Jky0DmP1_d9ghCT4cMPZ2lePWOCE9DMhEX2AsZpSvNE_8rQ05mOv9pJ6T9873JMKrXGz0A5gIHN5ES8u15JczbpOk7lOPRwo7Ovtbys3DD0R_eyg7xmbuk1-fNKYYtwINbb8XkwcNhcjpceILlhqgDieP-KSe0IKOH7Dy2YWgh9ci7GvTpt5XhYwEy2O9HkH2_81_OlvMWmtRnQEUEV1t7UVd1TBBpU4eRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcYegDHiKoxrBuPy8XbpbTaDUTEVeFe9TlUX3fFxQJHT5W5g-9d97OcRaFA_PrWDEzljPt0sklkC6ZYy3I7QelVJc2EMoy2Ni_jICl5E6-YdI10EUpAUJJzvXS1rqyu2GlfHZhe0ZZNpPxbnti9KKxlQC6PNSMzxJB7xkxVNHspaZKV5kOhUeZzLLkc30aTS5AqbAqVvzfIF7tXHQ6xkRWoMEDZdNpc7-WuoRquM-IFAYEW3WuE0ZbzGqTjFW4cGZdFbMKCxpQkEvZObE92hKjycpr8j61Qw5wLPtcL0E_kqntoFv2vxNLJ0aGPv-GAqzhruwXnXK3uJCOfUhWTyPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f72jBdKVUykhDjMyF3hiOomAuUzAwV0kMUlk1q_u-arUNpdYBPfVguJirdhBMVbAES55e2ubJiN4Wbw8rOFh5sGy3c2WFbbs5zUr2wxB-P9Gu69u9nILekGhtHhd8k13OIeTIOZVtJd4HpAWSb35eiL20Ehl4iHNDcH7VvnYj5S7OTClZ7WJk19j_tyAWfaNSD-cXpCYvVvrO7VERHKCTXaKC0Qnyru4EGfyRa8ID_OtL4K0d98F09OS51e0gE4EHdpdAqyU9OOlgH0ZmE62fB2fGfJQ85wNJPdO5alKwf-wFd7hZaxD4f0wIHp_MCQzrNAmvWPUznawV-whj1QArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 582 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9Z9GoLhfknIbv8d_GD0leW16EzudXrn51udYG3uwJ-yFAY845iX-iw9IexhqF-dbRRsaml28zA2ss_eGLn_MKaN145WMP72XONAfCnsw28ZPBmyj9Naf_wbAWQwq5BfYcmhWzcghsDkmQPSmxOHspYtK2dVoH9nw9l9J0rxqia_mb9dGR8SacOJ0iC23jXjZFaJERdYnAhx05JrKfqfOcvdxFKbZb2ed3_tS-kOk5uooElO8X_9xlkYx4d5WlspQGXFEcJOlpQjIkkBYkkiH0nxbXGO-5iRQm2iA-bFLXAIAAn6D2u3YlSiIMNhzoEjSlcOotMKUBznJOrr5J-A5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 594 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLdc3ciCc5XMy0Rf4QKKz58yTbN4w6SUPyr-w6DL_1z8chMTF748RbvDlei_66cCb2sJvIFaFUFU8Qz90YLFoISf9Mm24OjTeB8jGkzvDV_W3eLFHSpIDjI4l_3LvO8V67mmuBeFsb-7GXNuK_lWeEAB4pZYIuIHl7pCdqeU8melWwnsfYXiklhmBG3_QHkBi_lB7o7u0otQ0_AZ4KxTfmVLD_hGqXft6qFGJvNkA17B0HupDAY3XJwoqyUpC-IwJZ6_5AUjlkHHIXUGyP1is-zocG_1CSjz_iS_sN22V-PWYnsI4bDd2tpqvkC66sJigxdzHL-dzt0LaLHpev-qDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qec0XhW5N8fwxNpb5HktPzp70A8gN0jwOsnNH8f9Id1XCaBwfN5Ek0l_Y5G2G4j-XloX_OvphM4JqBfZszvptd4fxo6BBQqEIriihmESfRbhv7HWLTiDDCh3mVdu740RXd_26vCnd_re5GwHf9H_idTfJLF_2lLvpZNwPIsS-J_oZoNVOsoQ8b7QFEUVHiNgNi45ODm_PasoFIYP1qYkD_RsRJi0ViLOaW34-SbLGwBkM9D0A-SSlZRbnYolSiLDq8CNlU8CeCHtmqmy-gp46lwT_vBHb4pYVpWkBQ-kDHRV9pSrh0r1dZ7yaki5TVtoUK8j64f2rcX8p0mauwauRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSNbqwImzsrWcDcFuokuFczLfqSWUJDxQvnxyF0SmP9eykgH6vUbEksr62iR-BsAkhM6l7hOGkrarz7uVMSv1coe0rKa-dd6aO9S-V8ghEaDPC-c3UXIUAybSxyBh1NFa7L0N2c8H39kuc35Fe34mPgFEFAIxjU6GmLa8LeLYvDEAtaGVO9TbuOqf6RH5E2f2fepFe1vnN7vsUFapR5v8GP7l5lXKvbC47YvbGXcUwZtj6WRfY5CzItUuRCC7JrPpINP2-4WEjbQRHQ3j27rf_qqDwVwbmUu7jJLST3PEHV8BeZW8KGn11ydcYuA5dtSXJKDi7E4GZ8b0neKBJxtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWIIP6PjlKIn_k8K05BBNaJJHme6_Si20ZrTwz9dQddCWHdPWXl58rHIpRV9ABqyMaS67DVcKWVm5mxopg2luf9XpKe4D9BZEAXDbRra-9Cw7koG1VSt7w-B06Y3il8VwZkZ7T3i0v1Z1a2K724CM1f8iTrpcjR18Or5azHCfIhIYPpU-5obSb5NNgMzbHsNNuxcVRatqrj5_yXxEFWO2oSkOgIGuzDAz4UirMnjrzGmvC-KlrXaZArPOiGJ6QjZ0ta6BaDzsX2yKA46DfwdxKdUPZf26J1HeHBGIhsFncrLiq_jf30Q4wGCjjIZMV8hTkSguHRnAiIJrrJRNeb8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDNA8dZhA2VX4VcsGV3fjdlY441XGQ9QOsh6Fy4PJK1PhpDb810rmj54w2ICJjkd8jNo35dilW_SsPAiBZqCqqONTCcS8Koh9dqKtPwMj1L6hxEaCavZ1mfyetamPvc0C70KucAZTb_CesUee0x_DuBG4eioOZhtGlZA8XwYkBO8CN9f8c8AvEGGN-RyetJC_NE9QXWHtYUkWa_5rSTLFRYLWI6fTT0Vm9vAD6rBUzuW590wAshPRmFpDAeRiDLSg_DDLJIrDQRvHB7ZOBC8rMtA3IeN8TVrPtwr_Zkb5bINzHt1ErHuKOfHM0DYbfUssDMO6CYAYaBtukZzQPqpLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPblXI86CEXrKXhaxbzL_783ocO2qV_O5tdOOstAdk6jaFBgvKJs82H9hUsehVWBxzIt0DzkkJPt-a8SHVm6boS5ix29XQ5Sd_I4PXLGxHYrW4y2J5HNaHAqBVgbQQ5erfzVeWQSCaQdbMQMeSfk5A9e5CSAOzyzvqolHd61kwc5x7R13Zfoh-T_sO5PYvq67ClmlryfE34Qlxi4b_pHDAP2LliW_kB3cAofGUf7NOz_Qk6iuY42mGIcs5ktTy6YivtNIMv8RgXLSXHA8Kf3PM6ATkExY6oxdDfLJm1LzQPLs6gDlTImc1K1Nq4I1KDCDyHokzCzGElhN9Eaas0c_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o79SNy6O4pluAFtEuNL5ZZgu4SifDpOKh5xRbLG0zC1D4V15ygAiEnXb07GixcUWHfd1vFipNZMm24mqi87N7t8ZjBtV3TUqDwkwJ7I-TArG4Y456cKAHLvbyg-CZFsvXIeTXL0CzAL3HF6DohJxJPA5m_0fl66fa3zGzQmvzyM-6VuMHGGDQyzWJObqplLNDUNa5qjcsm31eanTU0Lh0MQy4xGsvp9Qkk4RDbFP2OpeCp8Pe2u8rXLo5AzxAD23ISGDWhfqO-LjZnfEpRy1ivJXYpwstPjqpUBYoaA8-ews_giIckkCeq2Aj4KyWZ5hIKSqicSLFs0-l7F6ceBDiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhzBa4yKZfn4C0kpdbekAjuOxwIYwsOwRoVG4Ifg-F2lsfDiVv8BX2mkNN8o2xMl5YFDRTd5VfwBPE5jBvLl_I929flAUuj0JBuLIPyX4Ayq0P-DOmxqYuQvICFyB0imO6F7zHllyVfuiDT3e6i99bk56A9FQjoLMcTXBpWdFUC__j4a77gV2UhbKa701sCE3C6A5b1Wayrb8YdGisGUVkdaamahQ8rs3sj2MmzTGqTUIfl0hDBLrPue0GsKgXO72IyXINEiKzbF_ReBrx_u5ECWk60NnCvgsLMvpT8jiS4TRLFiqQI-SxL5ZH4XL3N0WxIDirQ-rbalM_TIdhpXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUF6EGpXEDxrzSwjuiaT31p52JfqwdWk1-E8rDc2TiO9mzvcv0agn6pLO2j3RC5zFpPNJP8RBlIShVLzRGwl_Fo15d8BwSbFNo4yXvnVDYY39kFbY48Yb1qSR_oY5JZfsLsIBzaERQrOvhRxqlzGtsrpMa3jCGut0gGcwDYEgV69RJV0A_gP6mAt6fxRs0io0TLg2WlYt0Oio9o4ZofLV-OO2aAErz9uq6YW-P04gg_9ppj2vDcMmTALL-6BMtnKri0Iv_W_rVTzqk9ClOVZqUhp8CP8t1NfBkFt5G_5oYixSyaIp9RRV4hKNip5kM-wb-WRGw6ujsTW4FkroFeEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acFBci8cuT2oP02Xq6oDyvKignZJ19fHO1KvBX8hHm7WU0Xaoa8OXTzTFBPZ32VZ7tEyC9qER10ZoJYT9XVW28W9TYPwKANe9szcgIDlkKDy-GyXuGx88JUGoYADUhMlF-6O0vYjegPkheiRVVw3xyZNY5R5RSn-cru9fu43l36Ycy0B_uamx3YRW-nqyMN4-63TQnx5eWAH5Vvg2V8ANFCFxGb-CtHI9FXXd8dmYWoQbof-MqFvMyi3k8JYYWmSZLGdRj7SwDVkEK_Xa0R2hFfLf10Tj0_QUNymbam9RqlBLgVVH32ZCF926frPoB6O8vgNzPgIzNTdCkwvINpdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqwL0TfBr0zdVw4NWvlIES-Zu7sDAzk7MtdluLNxVa2p9_cT9GPyTxLa6uGM80cx9AErX40b4RnlxCUdlS-wSZivLF_0a0hkyKN5ZQClrU-eW5eWOrn-FK9tSJKvZxsdvGtQYOQLyALVeoI9E2XEjcf69kA1Jdw_g9So-e0-xPLh4wewbMn6yIxj6Wgou0hH3TaB_dQIGFHi8Lr-JKT9nR8iocVvy1aOApfxJHHswZOpXejemMGwEV2wTztk8S32WXD8TeQgOM6sf20ztpbUNe6gHFcWL0_ja3acX5OODEW4AIGo8wJVQc2nCN8unZCKYJQdfmrjQ335eadzFb37uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/js74uNAV0qdrJC0SWtxCoINjZH_ykuvYvWCO9phv7IjMiqmhetEgXAJHmmL94niTtomQuQEAHoKfUs02k58QVBanKAqv4jfS6Y7--Gs6Ohqo1Jk5vaq9Towsa0g-vkje5VDtekHT9EfgO4iUj1ze7UjntxaNiOFN8xxr1RK2MBOTqmo_QZfapx--qG8K40faD0F-gUMJaMy6SXZPjltOuUugmJx_Uy5ns0mdil701U0Z8gdEdsk1Do5iKd5dh52pVY8N-9OlpggJhW9a3x8-s3kwkNQpq_466VNViMhBZdY9ZYN3etIXs0IeHDVQ8OSz5cOXnsc2U2eod9lh1cwexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRWIK12cvXOeIOvM5l8-1tfToMFrPWGJVle13UMlTWqZuCkwk9BsDIoSieHoMT11ZD-VhcY9nc6NPfeZkKCccH4PSjbkPpGh3WI_Mg8wsCPND5qI0koxp-M3F5xg6xeH8s5UI0NuKCqZKR8d_IzG27W0FYwElrI-qak_08mlj9f-Ks5fGUL3IW33tq4S9gb4xfCI5HGAofF7kJl3MEclxqmg2v8hoVh0KkNymrNjCFuKhBEjJe7f95IkWDswggAbjBhsxmkMrXa5Zo67gHURC9GtpzaHiaGhnT2HnKAzAk85V6OTZpsqUKPCW94ba_k6H9Hsxn4c_7TLHDLEE-PU0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK27emnR24l0iF0tJyFSIuRNM-B7DPkgvASRkXHbZtJ0FgBK4Z19OXxb4pGcqf73Cv-soPLQOzp1KUzPqRdUiC3gwqswDpYpYcFkKanA1TrpVhqEXL_xZ8FH0en_rC6btbLrVK33wp845_Y0I1uTn_Gvk41skf9brDligFoYs3hQOA_6Mk_dIFetJpfL4V3j7Veky0N864359qH4lp73MMyqsWJO4We3cS5F2bJH2d6um6umiakAVcKqzHij-N1dJjJMArxnI3opEFMsC_R8A36u7m5BKy4Z6WxO2ZCtiEwiblMztqHDgS0q_eaYsu0iBRaZZ0r5OxYjaAyfbtP3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_F3wzjYgeV9FiMU50bE99XjM2iQOH2nyJvgto5vSrJAdgVf6ZPsmU6Ts6LzRlnFEDdvW2Q264xgBlGpzoxQII7bvk48AP94sTMmW6gkFYHhQOdjkikL_rJTgYEb9iJXw4oawSUcHj7Xx8KajbBhSShPmm9-TH49lJIVrAPe1dTYHxPvBsKopIsWN8WybQX_z1XERde_HsyfSK0IY4YZnU-0VwYYeEl-0ixl455b0A-hV0-aG_jg50F2mWko9W9HGwWSxNF-REd78d6LJ_mo2pkHSUZP6jj3Bw9UnRnmP0x08Trw55fgOXVcy-AvhVtqV8ywMV6lFAxAqZjGqbwQlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv7bya8Hp5Z2OzNNoPWCicHjTO8NZ9RqLAFtbwc_48hXBYQTre6l4S0l0GxmOCN3ZKUBcIDZ1tlNVhofPYo1WdDhURIuvhoJHwZZ4WEPQj4PgKRlfkPePIYU0j1nX0IvHD0EpeBTiuwictytp23WXU-u9w6Ixq4bC-gt2uGPb_ItSQKM1IsHarOrT3B9JAzMhA1uijbiFhB0lpOLlKxLP5ejAFYFhZTPcfMh5F9cmCKAXmT3Jhxv9X6BKk-ePkxI-Hb9mgpUAcIJkLRDUaFw6PW4XUjcd-fip7avJnxwt5X0hfhtRFcLO8I3H_76l7yseRu1zcSKibzyKsXrgC3ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDkpZbVybzOoswwkiH3HmtOr9IK1sz5g6ufhFWM0-pyzjcU8sZzJ4YrnPnFlbPYleRCFT21_E-v27RsbJAqunv8TVcuJtlBfq2P673bO2A9IncRPyaksx5FMAqrE3WbNTKUwjS3W29kjuy5bnlnUu1JKgsB14tH3DkvlMykdkdBUPV-nCigSguEUAA5v4k3WKXHVqKgNNK465bKYHmPD_6-blj60i9N3NNruPrgiKFL9ljAV998QJhwNqqtEGNooHTOKUbxcxbW6vMndnLqGwCNwNQ3LVHjH6sQns4Cild5eSDfjnUT9lJ26bBL1k2P8foQjzu3z9DzpjUEoys0muA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVi18bSLvoe0xRFVCkS-6X54CJjn4iD66XXkMs7smeYu3DYXEpf_V49DiaNLskqx3IN-C8l3JwAV5U_X8Mb6ReF5fF1pKOF7iDQgKlCDJ7gNXoLwVvwcoBLXCG9uc6j-xvm5UZFTjeQxyNWohqA2f3_crwSm-GnN0pnUJsxPKmGY10N7jR-_D1Az0xP8Oj-MIrUCVBRioon_Dfjjnfb3TsLNKB0kXXTorhdI2DNbbrN7oC3BiYViR2RMJlILA5LsBgkRaIinU35tofdz6EWpHNK4TrGMu9nQkPEYensSusgELsIEziHt9F7CkNHnKXCdu-CgCMIsf-HZYMvyklgTyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apP9YLuEN5vLhQ58LffKqaDkN8UuUoRgMl3-yNlC7ZzuusO83t2W71P_K8WzRTlxManOIDYUOGIf19I0UowF3XH6rtQNjX6yAO_Y34geykIf1LBvcMkMjvPx8qvENLIV8z_nLgCb64Q1fmny6M1KUOXx0Id5yDmovIwfv9T4Pf_kH4klj-DImxP4L0tXKm067XvgxIxhjt1p8YF0tY_Szu-iRSpCGghApXTJzcm5Osd5O_qGbuER6GAmvbrkHEX7IRPymLnU3u7SRGs5ZIfWht6PsP9aQhky3eEhqnQfTMdY8wDqP0AxfQVRu6TT7PhV2yqpd3q1Si5aQmBy5mVn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MESOwe5ZPicRdQAhFithAjhkolGrBOWF3fyDaIqbLa6Wm8Uwe_ki1sz6NQlAhXOm1t180wsQmKyaZddu0jz_7-AY4B-5JkcoTQcNG2V6S-8QKQfU6GWC9D2Oaab80Y_3Nz3-kWFjIB0qMWZ1OrZsAxFF04jdFbjNhczZgoOLJGyNLLmEU_rfTKTCgsMGwiZ3lxIjPq4JKpzLptwQkRkIUDZDVHfM5_MfvUMFxqNPzi9I-X97VKbSor8LobE333j5pPIuTOVXbCNpNYUGKHTZ1-YEY8VCw8cDvCvzdriYBMOi9LfXM-CNeKfWqVrd5Llp2pJ9YkI2rJh2GTGDHAVJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSe8VEcMKwcqsV888XAvjLHxDI_fr7r9WrbikkLhZww-7hBpxFRwKIMRY_VbwEWE1EZi7CUjqW7MfgqktzoU9xUN3VeFpUjXhtFvgDJYH-s9HkGJs02M1o0VnlvzZfckvnZmNvd5qrBI5CSZj5rhvaxIn6o8JjLmwocweFkVlblPyX84W3xBlNm9zD4Sgevd5RuZTne6SYVL5_HM0okc-uAxVMqonoQT_exZFNgxBqSXLAbqYMM8H4p_QFxvMbDqwhRY1CTCaH5ntJfZ9eXxXI-wKVgSWC57oYRr0fyIJMF_DI017DE9SSyRzYgWIVr8lx6qgqB_wZhc6XOIqWG5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZyf8uh4BaV5fvUwTnXIiKHMK0O014hrqbfpaOCQSTkSANcvNIUPmE4NSDtp2ovhB47ckC9rG2QJmnxIpj29nfMmkdvyPo-lgMi8rs2t2Ti_isLyDH6z85KmxBQ5T68xvpyL1QytnrE9hqQod43y-68zX_pjvNPb4Ydf-1TmasZM5eX0LwTxebhqOKG2OtBHE-0RMyUgjtRlMuQiy94rKXNRdqPNFSsUPnlxEpcYn7UI6xZc8jiA9R8L7fVc56hnciKD6Vh-1EUvpu_-PcFR6KtWHexxE23y2SXqpS3DHuZbLKJA0uzi6P8cGpjF-RV5mxUK9jMn7vMZRDc9SzHX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8gn_Lr5vLcJac_6rZX8UXljzgDFwgVfbVv6MEtmMdAeKsCUhK5_U0sAAb3Nkw2375e-nXmuIWncguUgfSADCJgpficypb_DTF_6Gv37RLcqIBNBZ6yYe8_hUDzzBSXN0keeBHmsn0LP1nDSHiWSB4Xl6nf1OOM5joYqwWTnXhCAZlUKHJfAoSwKqSaJS3LvgT4276oql_bG5zshQlG8NH1w2WlfWVMS1Ljq4yJkbKe3iUL18rZQ9KQWncXfJHm2QCPVo2gyQztrRc6oXg4YPO1zTvMJwJQr3QI-QXHJF6poQ1Ov4FnonzYBG3140x0k7ZqwJFjNrDGrk2Amf8xj_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjQ-nnSvQf2wYN6ZJcRkeE_3w6uSKhNWItmO9e30IwItQItBxTBHJykLag3SJfiyA_KzEbOsdLhA9ZynhV_aonh5mk6E8zBL0_17q2VYuq3RiNqxC4xh_m1twWd7nSUXXQU9lhq6yyQ9kqwcfSnptfYGO5K4fd9HWgcaqMvwtcj9Fgbs5HCgXzVp3B5Jn20H8CdnbvTG7N4-wSji8QeJky9QTa0opOuXNONhJtYCaWGwZk0e9yB_B3SR6hpJglj4lrQFE2Rt8-oogOkSiq3OGoYT8V0AZbpKtcUOhva21ms6sHh-X7VfZUrDEvWUtLXt9vYAr0F8Bmn8Ryob3Cgdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEI5hnhcDHs6JekNV3BG8_wedLnZGNKiEd6KdfvwdUv3glimaxWqsHwEDLVG2ANgVsNxYTJUkRik7l-JqEbSrjuq_wafZ8jyj-zEfvgj9C_f10rbwgH0vapitpqJ-GtmFBdkqPgdhzmmXhsDGIBVQWaab13Rg1xows_LrbdAunRq1ptssrNgBVIsvvoclwiEIhHXzMaw92s-s08mIFsI5IJm1xml0ZixLigj7IjMtoK_Itiv8EsdY1Lqf2sInLxH7BczbtLiYcU2KS8R-UrtXy1UZfQVUhWtrYxJvACvMWtwfr7CStgUt67oX1ayNI8S66z33seTRvNDgFgVwvUUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPHBhNmjyUvGGyAdibtK3Nf74VQa1mPotIZcW5hRmIP02n9uZMktt-4nC-b3p1HXGdUn-9aew3wgFYGuEVxvxKXcIlquYSA25SuQuJEGuj-eZCgr1Xm0h2ZbMc59piUcfHEdtS9Sp1Fhfdkoa5B7--GzDcgPMr_FcL84BwVtlo_hU2nU6I7vZRyP-E6gHg8Rtv6-shPFSUQD9NiWk-uwWHsoClWEL7Dm_17TaURM01TGtK9xV-XZBrMl4y9CdtI3lh9Fmpfq3XYe6FE0pE6vNrpQln_AUQAKjpZGk_Cwp0Gy9hM4_72nJVYWK3HaM5uqFQESxX-F2mdQA_jQMgSzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXBIZg6uEcApJVfhLONrmP5rM_YZXvPb6d8n2JGrcZ9s5LdhVvzcG7d5LvU5yvYmg4cWDU64_jGYinpdC_lAvNiQ4IQcmtN2tDu2Mmr4fZQ3tBExx_f1b3vo59OKYZJECkTl9JuU_D0lBTIh2KilA-8xZXlixYafZw1Wa-2kmC6W2d5MvAtnX1xRITF3edmJxeKceLA3GQr6DLSyKm8sPnNorpSogycStsgNRHnbud_hrxNMrG0ktbGZnBLJnG8dJN0KG2Xk-WgRWrfiB6PPFSEkzULzjhbFSPsdnyzYE7xjsgtCXuw-Js0R8gHPX_ZiDcj3i8j5Dpw_R_PzRk9mDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Lve8ZazF9-r5L4-cet0j6gRwekzys1LwK3cXYiDM1bCMxe3gLq0t1ybVfz593lxhgtqXnJEQ5MX_Mp6l2JYDHHyZPltOYOSK_FyEF7VrPC_SAJfKXybDO9ev3THfT119KTgW0I-pXK1d5xbiof5OGNgQmj4rooAiACt4tOFr-SdS5La8Yo6P__l6O_QPCy8KC3Xd8wzyUxuR98VHkNcIndfa-Q4QNKtoxPd37DY_D-OtwB26CJBuw9uTD5X0AVmma5W4M6xwMNcfVRJkfVxI5mZyl_6LIZ1D0Fn1sGBXEqV_HQcjJ5RXkCkcEKKatx8mBUtyMaH67pSqV5rCXXVN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Lve8ZazF9-r5L4-cet0j6gRwekzys1LwK3cXYiDM1bCMxe3gLq0t1ybVfz593lxhgtqXnJEQ5MX_Mp6l2JYDHHyZPltOYOSK_FyEF7VrPC_SAJfKXybDO9ev3THfT119KTgW0I-pXK1d5xbiof5OGNgQmj4rooAiACt4tOFr-SdS5La8Yo6P__l6O_QPCy8KC3Xd8wzyUxuR98VHkNcIndfa-Q4QNKtoxPd37DY_D-OtwB26CJBuw9uTD5X0AVmma5W4M6xwMNcfVRJkfVxI5mZyl_6LIZ1D0Fn1sGBXEqV_HQcjJ5RXkCkcEKKatx8mBUtyMaH67pSqV5rCXXVN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBszyZNl6eFksvLfHjFIrIPvOMN01bs0OccaSwwnYTVLnVyF5RgB-wTrV7xi8hzZZYx5-alec3aK1Wzp3lhp5k4GrscuvA6lbgdpZQXzCdQoHIreG2Gq60ao7eaoCKcS5GBquYjvPD7A65K6Cl9nDmmfL6AEYFEKVHT8TsNjWHvqEVYRSHtqLvE5zjIzAZPqxytLnK6oceJo84aqIhHuBvdwTYVR_KnZDGVVOkssDRJ0ZwaIMxj-MuPq34zV6r5ZoUaqTzsTpxshgU2asDBGwbBNYWxTBcyQPjOLZLjjkZK3RP_OVFUrbetHB4nG16kbnS8ssVZi2Xe4abHYTw8RjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm1GsjeJnDUajyALCVU_GTGyY3olWwMgHidrPeFGmVvUqx8cNHawcMhzvc4oOa6JaL0LB0WrRyiQzPP_9k_nAJD5zfJVw3vnrBxC7iS-bqjOK5T9vble-Lje5dJBgm67563e0pXDsG4aRRJBlwbipXX1JrYDQKBbSGDwZkm3nlHqT50PVUPXGfoHz82Hiu5fgMa0PHuox_dArGngHgze7Xa8AiZNQcbnd847WxfXOqlYFFZCbfsBR7FWxd3Q__nyS2csyg3RVT0f9DbbpXnXNSkPFK-EIPE9P61gDF8IymPxlPVZRJMZ9w4YzvTX2RC0LCFECjt9kykppSM3Gly7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3rvlNrWsZ4TBaSSvEnd7SBCilmaibhZxy-cT4YN6AcM4fPijYPnFNfmQFGN3SYC4qTzEIgeDO2dnRcryQ5zdxi8JAy0_aBXJu06v--4Ikn8pr2vS6SYYTF-YA2NTHK70a9aps-Kcn83EY8JgJ5B0cJ8q4ADAylp62-01hZkvj9IG4-wcJG7YuXhxEpjsFS267LOOVji1sPIDfI8SQe_zBqzBFse5ahFN3UxFwJ8EG7pDuy_JBLNNwv3GnHJBbyGIja3liv6nxGdgexCDOCGa_5BCzSlIiYd3Hxi0EMzODIaMgpPD2iGzCg_rYbr-IrgJ5ti9R-4vhAl9LDx5FIPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSf7SFqoffoNKqcRXEP9ZQth2gIts-DfX3EMI5j8nTE0JKO4f1-hoKAkr5tLw4YuScDXXnsWD_i2djuF_iYw1kirIacfd61u6p7KSkLGStqAf0hDiUnOODdFBHYReGSw9eiTuPqt8HoqXP7kPaFZo2roCb-d2n9kWxr3Robc7GQOvz4daFScftIB5F7gwvqhb2n23BKei9dvLR1GY1CoYJ1WMduiagWC321s5D2ur2hU5TBKUBWlhpf9mVVmg9Gl-v0ZW_BEox9vxlbWa9hLYJ0G6rIv-moyQ0gGh_E1nIdmN5OF8lfFg4MQawlfLhbzQFi3oAUoQZjQ-FuaSxae7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXwZiSPheW1W6TvEtNyPc9zHhK9DInmV6dAulKOpXjLUoFCBqx8rqPMjImjiY5bG2S7WZS7nlm9xN-oK4dwqQ-WtXP7iyO2YlKCBFiZNVe6cMEMAxzxCTh-oZrMBDIox_8XLMGSJFR_B-PtHXpGNtxikGnPSIXuPK6Eu1xFordMQucWdejLNYhmcPgD3nTHjBtrwZs3ybPg3rBpGbkMK2p7C0APFvjb5YvcfHuZVcfolizXXiNHS-eCOR1RempdXj0xAgS4_JK3hX7bDnWtv1BUibifPwlxzN0S8-XbS7YS_VYzFmxRGy5UGb4jDXHfM3O2eYovBxdAe8ull4Pb0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-WlXPsLYEzIVi5XFKmQl0Lo6GS8MrbP0s0dGuZ4wseIzq0qZBoXwjzkkfawOMoghWZgkH95eL7efQBiYEq7vsZV9ZX3CEfCL9_0ACDYSgHjSxHz0GEn8Pt-3IBYQ6nClOAJdkgpeIGxLsxdIpLcDulEoPa0Q-8zQVMkvP5b7w0LI5oeiC1Oxrlxz6i8v17xQllgz4o8kLdUsAqxx0ZOJU07yUNeVmhoIOOoDLuuUXMdHtFpjXBZIVIntV9Umhda-Q_VwZ-bMwNh76bK-Jb_dYld8rP29ngJEsAR6M41O4urKjUGhUQ3VOLQvk3pNUKP1slohUEyU2aLaGdu7CVbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaU3F_EFmXLoUkE1EqbUKfRg9thnygicnUPMPwL2y4GXGPIwRooTR5KFpTqvI_nWFP4VFmwxaOO3MKqFwNoqvrQ6fd-yWJgrsaEY0Gpvi7RW3iNDtDOKCatA0aWCL471bHtuPZIs6Q2FJUvw9Ml-RikiJmgRGW1HXRM5BkCMLPScyPUvI2BKyZ0e_imAmlm22L8ntjKqSwwN439pgeYQ0BVPUKJmxHy2a7E2OMzrLRJSquAL-enfHRzfFV7Ijq6xP98ftR0qlLimvMPEKmAhPfTe6IJj-CLwm5NBPSe8LysskUrP0znVYy_6md2ddmTbjdzS2y5c2CwT-SGDpFN5mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Uyvn-psA5AzCR3bsf1QvQkaW1juI0njZgrZyKdLOQxXEEHTCwNcrfF4yEwMtrhbaj7rz8aHCYyRYKSqUCnF4rOFbHk5QQQJ8OO2Dm7WBHhvDz7zCfdsliHUvV_3Jy8svRNctQYju6dTjSoGnDcpYMqYGZX3g9CQtamifNwZvOraJpDzj7coxHDzSKNUIhSFoxNJtsBllBalB8qMgHTQVVnkQIymyrR2Y7hfjLhmLbRfSTAUYTlixgpbF9Kptg7e6NggwZDCWz1VMgIMErZi_Bv429V_46T6F2hZ-ZBsWztBhBe8nafsheXv2405925Ejqx6YudJJCHxS6GxrthasBC1tKP2R9pf7GZpgE1Zg-TxR0nwmkTgp6ZDtgQfbiMeCdG_K7AevWihzn19VS8-xE4HoXGSiwirA4gNhhKv9Cy4WRdKzEmzCsfF7vkxh7ri1wtchUf4CpUwZIPJd2zm5qlp1OcfsKnF6AlyyTvYStFb5pKLSsFfYu4CHY8fUUJuWGFg5oq_ilylZ8m8P_IvDIc7nK6xglsigkY9u8RCF86dr_9CX6U4WKRe--1A6LUhBa9wy2IHaNzAluyUZGyMRzAx34MPs82-Y2gVpRwtijjBthnFy72Lbdt_k0o3atwQvwWoNIkQEIWgpvXaTev6gzUjICyoma4yRFp963hmqSEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Uyvn-psA5AzCR3bsf1QvQkaW1juI0njZgrZyKdLOQxXEEHTCwNcrfF4yEwMtrhbaj7rz8aHCYyRYKSqUCnF4rOFbHk5QQQJ8OO2Dm7WBHhvDz7zCfdsliHUvV_3Jy8svRNctQYju6dTjSoGnDcpYMqYGZX3g9CQtamifNwZvOraJpDzj7coxHDzSKNUIhSFoxNJtsBllBalB8qMgHTQVVnkQIymyrR2Y7hfjLhmLbRfSTAUYTlixgpbF9Kptg7e6NggwZDCWz1VMgIMErZi_Bv429V_46T6F2hZ-ZBsWztBhBe8nafsheXv2405925Ejqx6YudJJCHxS6GxrthasBC1tKP2R9pf7GZpgE1Zg-TxR0nwmkTgp6ZDtgQfbiMeCdG_K7AevWihzn19VS8-xE4HoXGSiwirA4gNhhKv9Cy4WRdKzEmzCsfF7vkxh7ri1wtchUf4CpUwZIPJd2zm5qlp1OcfsKnF6AlyyTvYStFb5pKLSsFfYu4CHY8fUUJuWGFg5oq_ilylZ8m8P_IvDIc7nK6xglsigkY9u8RCF86dr_9CX6U4WKRe--1A6LUhBa9wy2IHaNzAluyUZGyMRzAx34MPs82-Y2gVpRwtijjBthnFy72Lbdt_k0o3atwQvwWoNIkQEIWgpvXaTev6gzUjICyoma4yRFp963hmqSEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN9Ll-U-7w7wKB6f3Cn0jkFTvefu09mipCf9zvU1HRMr4Ka-UMccCx6qCfUVqhUydQLhM81tsGYW23kZOxF_UyXKGdE-cxUcTfiylS9Q26m7J_1KVnD_72AgTv_JTkPAUq3rFFtlum1xJL-BcYcRoP6sALQhApceQXp_OZvtNXKM-SZ2N4tmVZvGa_UCrOtec7fBwGI7-AZudhCJOO72AlfIdh6QT08Euf2y3GcNmnogrBjRmPCBLcPfUE5OOpeqs0jNulxnTzZpF6p7Y0Gm5l18UtVtZHzXIyr9XKZ5PRntBhw2GFiqTiMMCgvtCIyYoYwcCkdzEPkqfjBOQsgt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWQLBzVyR1g5RsDnfnA6-NeD-0Z9MWucjA7X45EREtpskNDg2-_CudMYohf2XAwt6uHHMo169LaQ9mDx28ErEEcSUnkbETkuIgkrdxu-FHBOsHWPc-IWfQhSEfENWypqPdH_gjbDebLY8IgiR4apFelDYo12x1-woH8lHPENgm6ZU41TZ4n141yV7GvVYC3hMmlgapr4xfi9upV2bUzcZfl9YvdY-6Foyi80fxLomfgCKVh6noxBrCikSl-kgh0JxgH2WMopwS_-K0s2tcD28zQLnpjodKtJ_JdquAFyTx5yDgvvcaQFRC7qXKVsTJC1gLl4HZFOUSQP6BOWpKHdpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmCPaPgZq84ZlxYTq44PLSIoJPm3Hf35RzPWZ_Hj7aQFiwyulHnlwwD-Lfeeih-9DwX0Q6VdmEzIaqbQQTnj-srg4OQhPlQdlGvVT208qX8sYwkRbn3gGYhw2F4ym99p6Mw84U4Yr6Rzwx55DsT6sgnm6mfMCVFmxFXLroYRDo5JMNGj_0Bl-cKQPUSdl0r0z1YQoLwBW-KVfGHZpWIW9hkniPcL12an61uXXtAMYmcZdFVuH4Ne87sD0hkq-3zVljoPCvvImf8vsdf1QRMLS6V_MmJhDSVgftKBNL_4woIrc1k1RjBkXhjVfsS11lg6sqJEjyHJK4ot68fUq40GSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/In__hfmxjjjNFxtRlH-2hx3jAK7TCogQ0RRysuuFAxE8teTVJHbs16UOeXfAw24DAulyEoMbDd5z0Apc4SU-uW8dCGCOqXZKu8NSvPr90PZ7cWLXhVDDlsJ8P2lDm4BCUAxb78HaWE7-iUlcz37Y0hetR_kC9ScKn3FCj9_9vd4RQ7guzoblrk8o6tSNduHpd0uQizAI4K2wb8yTUbtJMAmlJqRbzqjGhLdfwAckBu22GqVBZHjvShQyhmSd9xRcC5Pf1rsc7FyPboLlJs6qtHMndmJSkj9_QERXT3IS4TXH1liDYM7nRlQXW55JD_dAytco5Beg8eg-xm8NUWHpSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNhoNaEOwgoswNZRRxhrcEwmqkHYOf4JN_hDWOU-1iDms0_jggzzjYg5iOSdoQeVJ8jPAM6gmIuoVswHLmHa3Q5h5SSEVAYHfUVq_Gi03WNDjyRw88y2lrHR0owDfwQTqhkaV-fm22zxqOdDpOdZWS95Kjk4h1MJKE64qFbCiJFRxdpMwNzHsYr9-PxMJfxjJAL9lA0LKrM54vTqv40sqDqnWypsMW4jSgNg6Nh80JKYBspTpw3BdpHFaJGEc_0SGoCMJYJ6WnkTXqERsoJPOMaOlApJkv3cBoKOtcTaC27U4q1yoyPQHDNg_cEmWjwufg_uoJhTvqBHBNLIiesqQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bsy1qcBSWoGke_3L6WWOIU2k78h7tpA-Sl-hedkNVIwft_lyValuwDBoAFlwtNJsZVyyEXfXd_0Un4kfYLr2ZTN1_kqRQkl-Xqb2VDMqR4Tbx3Qn2TKzOk3vicw4d4vMEWCFgYN1LhYpp288Zpyq43z0ZVxZIHxRnzb-IJOdGrO__97m051_nnzXLTnBLsnD42WJZ27QGDdsaOYO8i1xZpsHAf5WC4gVXfgnBgBrioZc1-yHZ4NybHgpEmuoGctFF9LS2asrRSC9c2yBCS4MS-zC3rkv3IBQo8Sf-TTpDRpY3DVcfgjOwSJU1kIhg54dQ0eQbi5LBOD-v3IeU4o43A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bsy1qcBSWoGke_3L6WWOIU2k78h7tpA-Sl-hedkNVIwft_lyValuwDBoAFlwtNJsZVyyEXfXd_0Un4kfYLr2ZTN1_kqRQkl-Xqb2VDMqR4Tbx3Qn2TKzOk3vicw4d4vMEWCFgYN1LhYpp288Zpyq43z0ZVxZIHxRnzb-IJOdGrO__97m051_nnzXLTnBLsnD42WJZ27QGDdsaOYO8i1xZpsHAf5WC4gVXfgnBgBrioZc1-yHZ4NybHgpEmuoGctFF9LS2asrRSC9c2yBCS4MS-zC3rkv3IBQo8Sf-TTpDRpY3DVcfgjOwSJU1kIhg54dQ0eQbi5LBOD-v3IeU4o43A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEInBR8iFnjgjDOl8wHP80_ziO-jNl1hnqOIKrAiau8dw7fMlzEGUATfUWCJHNMobRUwsJvy1vqlsb-HgXLtjCqWlPee2OnxX-Vnv1e_erk8nB58pKyHMzlSK96LIe2TCA3a736Ya44fQH5JKlitOD-eLLvEXT_MioJnskkOoSp0th_f71fDh5j0UnURWWokF1i6Ttl--BCeILv8zRoFw5S43SikQBhDpgdSw-8-rofVFsN3qqClW0R0-oJCfreREOfGehLwEhWhRK8XqP3iGheXpjoc0xqTCAsvZvZmDOqQhd-R51pZK7-TDV5EwXi8ao7V4I4tLlDrOhldOl-jVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
