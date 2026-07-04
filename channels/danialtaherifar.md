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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 285 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrWGa0v6VUuXO-4rtaP9ygD2iLUVN9BD_4vfaCdDEDyDnZfLao7yQ0rcTP--ROZ0yptZIL3NiwgeK0ZX0UpZPQB-jSrg5ccwF4i_Yw6WC8ViK4RjN2DkpuaK7hhHqIjt0ri5M1CFN_58lXwIE5lIxcfKk8kn1L1WwEdfB0vDuTTG7u3rBwqqUxfOJK2AZfxuv3cLoZhB4rX_URawPu20YDvPJWZ7YZyGmq-N0SFO35n-6LMEP1DadQ7fyugobVW4atlZoBrfVVzmPX58Ln7vIAfM6AW7-xKWRaBapq_I4B8Y09DkS0jxF5VCGc72tq8_Uf5lvyGDZdq9hQ7dNlH5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 512 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb4x1_KvMeeTp0hh_LuocQ0ddbgtMr-igQsWBA2g9EP3y01fjtRAW6YlqUsslXk2fyQEG1_zowltTw5cZlGZBmpSYRRYuaKaYpzOX8HE-iEDVRrth24ipzztXFauxvbyOV_rs0hyn9sDCJVBL4hvp-R3G7jwEWjKwzLp5hJq2iOhW6FjLcmBrPfHV9l0zzGTqP2yv7Z_wqQTaz4_nDRY2-GyqZiJe4MrNNQVsTlVwglTZTVHsk2MvEG2C8VGxx7kBVdlhQLPYbuH23muBjKPZEDxgH3nbP_SuYD2tzYYCHMvjlfkjN_obH7RzCGR2DPNW6RaeeN38szDFnE_C5IgCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOFQw1_HYoBNmap1MbkYi-j_spG80iuZy7XviFxHNI8axf3cSJlk68FCMCVxcJQBgd9au_JolgcRvbqcaPOGd5cXFE3QbHO0rUqGhn1C6ejiq1u_t_VX5527nZGV5BifUqcJKa4TrMlcwQVGpEMFFuflRw1wsOMLtMHqP34BOfBtCYxRs-Fc2p8EZFKNjBikdG-uW-fPykAw_BTuC7Mb9J28vkHn3CmDnOKjVUIFPycNr60PMK6JhHBguXe8_P4gYrz9oCD130QNnFRpig7bo0b8ysWy4BY7XnbvuN2fOGLRqJn1b_IX-qbXzJNjZbWXTfwoISSjmmU20IW-T0SfhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2LrWOi7rI-sLsdbE9d6RWQDGjDTg4Datby1GYIw2GzyujH-eZi5CL3kuwYW-qHQuEn1CdxoW92slG3h6O9Ez29iJH0NPNuvU6GvPT-yFM9bYdurGg8eRbDhyl-0FGIJ8E_D4n8sjWHa6WCqqN-26gRVazSZxKxrGog3eOJJ4N2WId1OyOSOuceo77G2QE_tHSRDroi8R9w4kFKFlrnZPKMB_hTkZe7u5Lmuox8wpLXh8ND6AbJuET-kBmi2oj_d0z-D652rg9bCGQLbBTXH8K7G-BHDyOY1sw7-fl1uuWwhdxbb1thAG4JISJXb1gQ1QroF7PKi0VV1MVUdEH-ReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTzMySs3Hmm4H-hFnNHqSbWmqLxvQrK44No3cuChHg6lnXZapCXWRxlMZ0YAZ5kpsdHa5LR6sdUtfG0vaWTpbFfqhd19cWdbJurF7N0ro2CUscceSALWvUKeeKhs10qC3-Km9ZzNj7eGRcL_R5SwuK97a5D0bar5APU3fQbF4C2hl6ghPqq3lP5P6kz_LjTRkjdzPaFgbdBJ1wxKCmrmKdMo9cj1Q6n9R3vE3rxAUmkhrZow1DDS0Temlb5Aa8xiMa3HOuRlkAtpGcvPFyMuhhh77ipFGVDVW7IqWScrMTXo5dtYyZNWjIB3wHAixUgOIs_pK6HBpR6I_2aL4rqL9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST1Fsvo6b_5t0_XdkQ36bXd6Wi1_sVmrK4384caKZQoJq-uFQkn39TV3Ovs4pqhJPhVHBodxyjxL46o4CWYIQuccfvmG97-MY9F5xQzeST33WPM_ptPcLONP-snHzE8So0cuq-QaMnkwBVfTnNGHB4YEBsXtSWnjW2dWwkYX070ULzZBBla5UVOkMfbFhhWJGfaP-EHpfGjWeeq-i8kl8gR1-_Q9011Za2ssF8B9_Wvktx2vl3u3OoTtUG4HjSX3KJWpsHJXcgdq6HQvM7FPlZ-wmoFHEsdGBMTXBqpx-7FRqaKkRNNEPtrfoePKwFEvqtlzLb4GLCh-NmJynUGEGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D543qoDOmcjqDt5irv_9dBiGqYqYHeac_wMB4ItZGlFOIPSG0w9kTFiCWiiDaxTDdozRgp9t5KHQubKYL2OHMK6vykcEoFiS9TCLYDNnLO5VfO8ybQS7KSQ8kzqFYAoM-brx26IwD9ndghREidcVQTnf5JGd-isOggcvkAIEipM6TpYA7PzRVBlZzZ9TndFjz0HhudmJpgpxHNDml3XskxGRMOjrG9-F0s6KM4Fk3ktSoEE_vAEkDGY2rdeQsAEqSA0LMQSJR8T5UGfAs5Nhy69fcNR_cHyR2O2SLALd7ClIqMxIO27tpqY4BqTxToJXViBG2ybz_FnE_s5i2ILMuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvL5yRKPc91AFwgavVTjGq5MAZEQgn6i7aslo_i_xmQiSolTezESkZiujKT7CEuw_hguTgubKuD8z2-mxqECmXPM-PGuCyxYDv6qKD4YuguaG8HbdgG257DaVIPi_WwT4wNtAv-3IzoTsf1Ic-BIyWCyRKEr93Usdw2fVf5Qj8jPYCvbnh1bd7IY-2bewKyRQJ5Ebr1C7Z_eIndNZSLf2ivZWI75JeFZCWfYsWB_krjpC_OIEbA4V3GHgAQ5DFRrK1BlXxzfggPCEdQgU1wEUOSsM5hTVFfwNVqwrTN9e-HvgQ6GIUfVKblKklWqTcBJUjmIimCr88eJHb1-fgdD9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNl8RDvG-DR4CH_jS_eebAj6I8OL8ahg7QjRyA89SFcAAk4vMzBB06UByLeROwrZ1hC3E36gY3Y09SHA5sPtdSlp6BDR21dLuhdWOGLFAcGn9Ccp7uzmEW1g1LM5xYj6tS7rVcga9-N9TY-krddu3N18hW22Sw8luG4RgqpBNB-eNP_V9DUHQLVLA0iiux-ZqFfeNlFdHeiuz8uSGqox1kXE8ysGhMTcLioJKDvMsauh80nppmAr2oC6l5I-yISyUyHmaWnZekg6oOw-Hok7amDgNLtv4DeuzzBmf3h9At_zz-CGsJbwv0vLlPs-Ep8oHv2hIYUQ8kCn8UHgmE5UZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRuvMSOg3o2hJGxvfNfK1OZG8gQBpzzCMDfdt1ky8LqG0iSAqSRVlX8uE3SfN7W_7NWW8mN6uFr2-t24dhVwoVlC0VsBMQWafvHoUbOTqG2vmRAjNahcoRa1eXnxM7NJHVwziOQ2bSuRwpb4J0n3PScGUjyrUPxQ_UQRrCVvrV5siFRzvE0FpW30nBEJM9u-tqyQkZEAfSCHqe5x8zcLLzpXst7SXOQq7Ao-A-7Dh1OV76Tv84saeTtudke98kDnRu9R0G1GfFUnjqxFQq_BwKskoFm18bLwijmkyf2_E9y-FFw3-rajNPhdq0x2QEqsAmHA3satzyQwxt6xDy7Zeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfI-rHIQH2-TUtnv5tCy7uFw_1KA0FS7gDozZWSEPeUT1ni10xdfgXpnaRLbrHlfS0FeBaub7APNmuOnXMRJ-AuLpw9NFy4fFDsOwPVXG-F0Posc0tTZOB7n9iSPl9cpxgZoicMMgLH7hDkujc_RwPxlbaD37I4SdKRNqTlsMNuLgKz0bqduJwJI-D6lACdi_kIiQA4lkR3Oia3CYCMmk4OsfRHw5zswJCslQ4BghjSsIQnCoZhRg9RoFMwz_OuVYm2mBP7fR-yNd88aNFuyFaKxPbEdVr7HNjDzYdt4Khx7hb8R_vfo0w3MTRD1O5dvw5sfGc5MxRmIwqkL9hLEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6I6D72XRCW_vrjQpKHtrs87oJ7C5SJwQ1e2Cf1GhE94zjW8JDe_jDeJCwLXud_vlxBSPPxh3QGQYGQ8ugeiHM_ImLUCGtW7Wh-0DOERw9FsligTzCNvYurUg8NkUKsmhsTsRgeR5bdf5PpXVXDlz3TLQOAUUKHSzBFxkI76NZOyt0NP4b3W7tvxep8arLuQo-s7sVQ3vp3YnhQXjHJJuXzPkcywVSY1e6PpbJ0Ag2US6AAg6RXbyyiaP7v55RpcFyXv6dD7kBQe3DXV4ZHSjKXbo3MAqU3amXJYJGzm3051JvB7wRPjbNMvt8WyL4m1aG-suZWUnR3tpMZ3TvIxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGVocE_EJugDDyD-wa0aqyujbf7IaiXdHADCClREpDwjJiux1ls1MKVF1PD3w7UpURlF7ORty5ktpAAz80hQgXcQ5QX4bYWasxOnfEWr-sJrPoZJiB0QOT7axoNlZ3dvXO8lMpnVGeNmCUkBaq-3mLS1860D2JQyF840QJbPoXX20Mv2XFYnYC5eQolaTpMEDoi97qGvPdkybSBpE2o_pAYejCAz2SZMrNuI4-yFNCkhli3hWBpjmsDjz3-7ywSQdfF_qfrvpgCiX0Z3m8C33yXgs5FzFEtCaddcW73wm0qIZm3kFlNzcGXwssQDpTl_XACwKbCXznd_jS7OZsFyhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LADA-lmZvNooE8Jbuz4MZIt4cmHcbPvE1lxlIUxLCPsJM-qPhZh3EDAUcKHNhI9EPkuxDDbvpvRMs6AskD8WTzk-WAEg6eoCbBxXlB9cJpqh0M3Y67ZwnZoHwdQNR93gPfiiZTc2aq94KYIvmGaHjHotEb3L0vw-uIZUJyzPdpb41LftCVDGBP9iMen8g-aE1gdsOAl8J9lML9I3Iu8jVNgzwiyfpE14hebHfkQtVHx5cZNqD2kNmKvUGPxXIymb3e8NCzvjSuIj_QBlXBbAZ3snd1sE_yxPRU2stHv1Fg5VyXB_u1XAvpMiz_BECF_QgdnIYP4_WpaeRJceHIuDnQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=XgK9cvfKVLUU8BNcPJRT5c4DIEwltMzUpoMymwD_5nmDNGT4nZSbvRXIyd3RqpA7aHargDzWelSYy3VlelswyBJyDJzonMX-1hmcitOiPnzWGl5NJBSOlZdBjgswnXoXYGlZck4DieJswWJ93gK_oUtrZFJmtHj_jZh608HZrOKZRBNHNmCzQLcQCTDRNE_faBb0HErkb_h6w6BZEj84xikEUt3kw-bgCBUempHtnNeVGZDSBqZPhobWEcnHl4xr53rTvWMYEtLdZiNa81lJpY9HoVWfJY7zJ0lGEvmXMQzuX4luo1fmuEKdbrj_VCGXQO5-05gKCzvIWPgnrSCNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=XgK9cvfKVLUU8BNcPJRT5c4DIEwltMzUpoMymwD_5nmDNGT4nZSbvRXIyd3RqpA7aHargDzWelSYy3VlelswyBJyDJzonMX-1hmcitOiPnzWGl5NJBSOlZdBjgswnXoXYGlZck4DieJswWJ93gK_oUtrZFJmtHj_jZh608HZrOKZRBNHNmCzQLcQCTDRNE_faBb0HErkb_h6w6BZEj84xikEUt3kw-bgCBUempHtnNeVGZDSBqZPhobWEcnHl4xr53rTvWMYEtLdZiNa81lJpY9HoVWfJY7zJ0lGEvmXMQzuX4luo1fmuEKdbrj_VCGXQO5-05gKCzvIWPgnrSCNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBTf264Q1BEzUGy4N5uego0LOCQLE-_NFvV48AVVssIX1To-yeE_PHZ62Ni4xA3JYlfhLqap_9mwerR34yKAG8C6G_PfAlhlpqfB85mzsnDeILpNENN8n90vfcsyrNkxuwceCxmdNG_E29C8L37mPWFly-nxAAPZbZ4oh296B5u19k514IJHPPeMc6K4dPxXEjBfvQe2lMZEC3yu8s4f5bdjMN3M79gCncdH9KjEyu25Imn4I5LM6vLJdnncQHUK349dYeI9041CWk9q4e-oRilPGyZYB9Dh73i29j35TwIyoYtv9PgcW_FAG94uBS4rufAqCCLtefjDf6_6iGw2nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrKPZv6bOmRbzl6lNFPXygsiZulju-S1QCpUDV6EYzDApz969K4DxJnSf422UF_0rqPUNg7oWfNMx1ri4id2G5DKHx60RhQAkVeA-7Uni0W2vqGC07TOWghUK2nAB5UCUgkX5jBy22Cr2zpoB8_dfMjsl0JQleXaQVD2WEpiWLclFRdQnTkiCGddclhclIvMxcvQWy2POEzlrl4xXuTEztVble1Auq_opBv_qEgVXAfrcX8oJWKTW4YLw6andVVXMNTFvN6i50M0YYgB3FrWtJvX_PWKtNOc8uMSRCqHpQn8zooVq79HfPwpqr4VP0JrI9Khy2pvDdew77gg7vPHZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZUcW0NyIp7CnEG40PMiczocFURHiEtKqqDMoPe6wj0ymMKP5ImkL9dpYd7BsZ-AkPkDOOzF7ci3NissmJ8byJFPxOid1KgyZkNyJPP95clmnBaWettBBlKAo9GuBaa_pJiTm2RO1ZJRdhz-joWvA3nbPWdF51Pb_Mp46ykhdzdD0T9MO8fHtBF3Ontfmq6jF86J6gk2KGGER_1HRcbusthMO3246O-fascp3wppx-GZZmAtPebi0Rq16JyiJlyvYmFTOsSoxxxtIPlULOLqCuuUZz7IIGcw498y-3Q5JBvxF7s_FfP2T69oP1cvQ_Jq0SOMdlnanusrU26UP8AqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kb-tI_vxHxWaZB22PoHFXnvPO9EcatO2_URgdFMM3GnwPwgnM07u4EXJP9B_7mLeLrZUhP8CFXCbUm6NObowSe6xu2VZXg-KLkpaFaRI1cOhglkKefY6TRa5Y-aPaMYvAvzQcsQX4RZwICMVuJBLrUpnob5bgS-PeOLbxIciNhhayliHb-Hmvz5EvPho3juYd44bVCpOz_4TuS2YKUFBEqhZe_DpjUvUaPkIBUi0JeNdtqidNRK6-5DhcLYzS8pFzMZZDrXx1zSn9vEOv2yfci8JQVo_2c789od58sN_Y1PeZQObi4A3DGJ3L5roxe7_1dfGpKhZYhLoxFhKwZb3hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5i6k-QAYe51i4A-1w3mVoA1qJ7OjnvdOTwOlZZWZmV3xeiadlufUFJxt3sak-_f9hHTODVQTNYSiUuGiDy0fCLREY2hXaEnk_Ikl5alCb88iu1S7YTK3Emolx6H6I5Hwp7fFiEJMeoLON4gOXqQ-JKWjeN_OQBvGjrA8NwQW46Pcdo_uvD4UefaB5XydKRMLXzpmwqQa7YTOFg4nkr6iNuOOYzl337GemeaBU1q8-BU4FeGuipkFgB3Vvc8tfW2ITyaT_5s2tOJHfkoIHBdcaxXvadHEpZZ0xWA6BMWJaq8ryEFF0ciNEh-8bkLvD1BGf255bK5gz_1JJeoxrmUew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJh1d-B5FHfsjVBvhiHkP_dwT8efqhrMf1mN-iftbBmJ1hSHWQPje9B8nvaF805jZw1QDhmdSQLsw1L1zbiMeumnI4K7wpQzQR3Fq82GAtEJZ-8lBipwt_T1WkwCrr8TVo_OySRrXj5OHFPKsPqb1uWV9wBMJiIO9qYa4ecbGL2q68CEA3fWsN6nimVNSC50yfSry3dtzHfDWytn5MRApTcrMhWksQPUIWJaiXMSp1ChD_esS-rwYUx2ji7LwSYPll0zfEl_U3V2cQUSjKbU6e2P2xHlUBaIkiIfUgpUC0qkyn6mlezydQPlIYpFXyigbolxLUTcnYmp6fKV2IUmZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sybgXCu_sR7-lA67smJdhkI6o-mkz9qlRR9LcsiawWLAdmWuzEQvslzlc8Syn1dSfI5AYqSCo2ZBNtdzAEEnVrxv9u6SDP4N4ojjKVMWhLT6aD8poc991BgMfzZlYLcMxIMVTmS4691t29-1SvS8kHPo5CHjqHSl76OAC6U6G66EF1LdDQ-fDwj27Aap_k7Vd06rMfH7kVwrVS5x32Er163u-TrQcn66nzooVb1eK00u1kUO83iMaHVpgyoHx_ra_FiI9OqiDPKNNwQW63kRaVze9WNwfx4eNQETDbTlTI81H-RxnC5nQ_BygAQltzAzw0m07gDZ4QXDfkCk05hPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjhxdJz7wHnbJ0VNEIYcQ_khLtRRMAYqWZY3ExVvnOCLuUtwSLZti1XDzaeeNEN1D6wjBVsIkoZcpvS3qMQHO93u0X8K3pXRE1DKNycot7ENS9XYRVhpdPJxk-cuqOEFrP2eB5EqVc5xWFu0X8Qijeo-w9YOB7-CvbymUs15Q6e6uPkSDEmkVqsGGT4ufPkO5wqniFEKhQ2cE2UoT_aboE4yCkweaqcOiIyr-5OR1s6KcuyU0GzSnu6W6TxGyDL0xA61Znlv4GAZslwKn-BWZd7Xzm1uUdT8hgY6unBF-D7XIMRpetLWlZ3hmVol5uXSztP2HoUTaPPENtrPVmG9nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmKWGxaxoMzTA0QKvls52XeMTImHG0NsF8HSY_U-qtjlXPScuEqLksqMGb2vjXXqj3CNsii0t2iXbQoXS9kSz_zxvXVIU1Jite5jWkbh527L4c4SP0lvRS_1Ub8XiXgGje9--HcNVIpDt9PDWnGfgW3Xqs5ayNWm8WUKODfXa-YrqsPtCcmMhrReJDeU2dE_AvCBjdjTiNdRnNN3WHm3G_Om-thDOXp9DYEy9VKFlRbrhwuIWL1vevqEkUteETyegeZIV7GrzbCqYZ0kCMCbmT4h0tLFQziavuD-JQFtDM_1uqfzAT0K_hHc-guIX2WJlNHeOr25_ABRlS6lV182TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wzVx3EUPEo8Oe67JDYVoyGaLk2XDteLnMJRMaKfXJkK4o68oZj4mXeaN1bjZnGKTeGVYXIBGO4uZ_HE0YDk6_MpEG4WZqGuiXbvicMw_ji3iKHivOfXMKTGjXoa548asQg1t1zHpJtXXbDru3NBBM4rPFZXHiTpdNQBQ7Vje8QUx9pJJqbTb6lbcOkwWVj_k9VrZxtEoZ8fUyyBP6OxuUmVhmTaQTQPyryJEnsdY9S7i5ZLZlLWxW51snr8kl_ES2KXlqETbNM09w4zmz31AnWOJ7BRtTynW68zKGC6D5TQqVjbB7xWnwkO0Q5EumJpv5I58xtyztfVs_N_d525g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsRbmRxvyFkQsMlsLYBx7QC9J70Sbdr-gk2Ws8FVfta3FyP3rAtOCHYgsLE1g8f_9bzSgwW6pOgDdGTGh3u19jZD9hICH_U1QY9T9_hrYqzz6aQjMwsVRkgxnuQUUeQt-rA9p8hdDAjbeIeXxI1215FDK5Fj5lsthQ-bM5cg3iJnonq3QKUnLm0fiw1h3Mc36owyh1MCJQOskgu8E2fYOx3qdtKFnRbfEmuIWoBVx-yXWV_DDqk9pjbhmVqNFD6ONQLLbzC1QUX2WSJNhMLsd7FPYshGRqZWy9CnAUVvjD-zo14a97lTRf9flegkS6oLPkS4yI_5PmwuLCurXP1RAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdTI4DJdngzhOHBWLqEyG8RaoZ3iJ1gGap2d1x6L3uISfsVUtCc5sxv3RHbXP4nD0Wz3_Kw9vEj8-qVh6uwwP7N5gyT-0oh1JMgGSCB3TR7iJBenD-FwGXO5DwU8uNzD5OMDgu8q1FEbp_5r9PQtmUxc9KYWoGwcRyuLga7YbSGQEI6B3gw4GcQHRM1ZrylU7VycC1h1fION-vyl6B7uHIk3gksWqh7bF6MeY0SIuZ1A_Wi9EFaYE2hdclTSzSNmbn1UDIZgtGe9Z-_XG5Uj-yi1SPcc3w2RTt8HlvsrzmrzXYHzO2tW0wrKaps7jt0z9OolZrmV5GmVhhm4ANPR0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Axdf_bZauMP5-Ljh1kpvqkF10XpP4RxznymYt4gbos8WIY1XhF_c5keJ-V7Ee9DHE3TFVZbmYv65wK5UxZkJ6sQleN855CM8dN5apjOlik8YPGacUORUIAM5Vf0r50tKGMn9eiG9IFMylQnmk4Es8mDfTLG6VGFKSfUVsVKGxIT2CuxwTpN2LiMc0fZ5qULejPJ3_-wCE6uxbbTw3SzUVdGsBn1qsx25czB7DRncKlHg7CmQOJMQLjiDhRzAznvk_xaY_kxpdsZVoepkbaQ3e0SUA0an0xT3fiM28Cn2XoC2Eoz7ypbUdLkxVStZ1K8-BxivmdAmiX_ZM5cYIJ_cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRYRqYDVGauYnBXQaJSxaUH1BteKkFRIyj6xN_MnydJWyHusJOdMXP76KHWrvhoaHInjj1R-tNxwON3UWvGreu-MTP_9r_lrVzknDTshVKwhIUvlCsiFtWsnlFisGt7CzJehcwMEBdba0BXDKgyWdpNFF1XJLBw4OGJT4gTy9MKmdA0RF2mE_GTsozKy-9BAsx1dxkdPaqEQ9ZSHcsSj2JJ64M3CSs6TtxvIYTEsGiki0R81DAH8-tmrBWxxD207sJ1I3iCkdSR6iJPCPN34bxFZfigPDtnOakM4Peu0Tl6V_-vP5BwwSfJQaCnhFCQjV0mTDAVhW4Br378CSoFcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mszy6d7n-7uWPD8rO0i8vmsKXcuikejyA1FXPiXSh__0gTQueaEsFmaH6LZSzEZlZZrUVbTHl2jUW4IBtPLSyRT7f0QLaej8UbyHbo4bE54mcmt3KGXJ91XKFigZYeCns_9zT2GmIsqyD6l4Xuxt4ya7WEZNQkP5H1wpmzZUUl8Xgel1I3vjAbcd7sYJtJAaeoGEdfFibpXIFRWBbkiN5okuT592VdFuMqNhMmpWalHUVb8l_b2irtDGXwQ2hC1fQAr9bzShYf5msR8tXsE1do30hZvpVg6B5Z4w4-y_aIITY69OqaR5Y3oHLZeNOBmVC6rM7ujTXaKHtvxUayzGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkSkKhm1AyZn4h89r4PqycQ7WZze15Wnr-gzGNnOYByJ29xWa61xauddnwVdDTXo3g7J-M_Q0SJIu0nBedCe3I7iLXHrfl6nJgcT97VduLfx85MQSw2KSkHd2lYs4g79_CTKIvAjjZeT9wuZXqMp0tpsiavEL7EamomlTu8tguSqgXwZtolqDDAzWKNrriZ6fEYzUEpqyuUakiETBZfesmrOJgmUDYf4rHsk0tYP_dRZxT-3CuiaUfhpb4FUQJa6qD9zm9dktHfBZIZ3CmAaub0eUOOioKFYdUhtiXq_GMzswSdcv6DgA9PVK35CpU_5tjPL4bVg6VnSWeEvlv5EiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cE5wyRzuf3qhzSGYrVH7PNLK8PCWN8lFor2q5TzgPnjbYmVERsZH4CibJ6xWgRpNIroAX0vjGmkAwcn517bHMQCeh6htAVrVY_ZgKxXBkdagFZNTTh0tFQuMN5Jbeh9m88uRdBh2Q8hSEmPaVL8osscgUXz57gqcubHsUWesgnCcw289KMwoEyzg3TRrKk_uoDLcRKuJbUfq7A_E2MLORw-qoWdNZZTM900TgNV2UlBHcC0kq15h4SdWy6N1qW-XWw7ZuKAdHtK9P00lS5rBKL2V-VFDA3DoQcFVOzYHq8JJ3DJIqxvkMwZCn5EOePVeCkYZ7Ja3Gyshkwypd8ocJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orgz3yeyAPf4nOYygGwSUnrvcBKUfB86j50UKBZvkkoQU18H6b4iukgD7gmp8jFaBBV5tJhH8M4lbTgDFnPQ7SrUDooBcbakKcndTy-YWLAeqVnTiqNWgGfB9ZH8UqeYj9faffJ_droizFk9k7m-G5TbvDBAh0hs5KtBkYhAOSxKd4hFQ_fZTwtoqAifxNR_R449NoP-digr76LcVtqkshNKkaqfUOCUOOxY4CKi6QJAAN6zGXCMkCe_-NVtFxJOJIisjHczjUPvFFV-uiUTdUPWtWZfQjIhEKBVxMK0G-CjE-QGfkV0CFCVY9BvKN7mKdq3JN4LoOWl5NWmC9395A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koKUoYAfYWQu0GQRAmGb3Xh_y5dytUbwS2R1QFLSvBsM7BYMv3-dKepZ851qpaWppJMhltTNorm9s28d2h5jzXWUlXFJfEurJi-_1UqfQ4mqXM9HHsMmbe_EuRyahK4hpeKUR7Gyfi5FqQMaL5YM0nBLpXi01Jfi-7EqIMspZjp34eeoP-vvoN_DGbqbmb5Sfv6iPyhx1Qv9HEMrgrgm_sDn9gYins5BIgkO6rw1Or0eTHf_KueHhRnopTm4Er5YZWZMeI1C71fZchCZ5SDU2m6qCc0kR9LC7Ji63p4iO0bew90gl6SAO6JmZOUUzEaUV7zfkIRE2MJxhZOETyI0vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTfUyyImzV_0gQBUhj5yrmOZV23jVcDNaQbNYRcKCavO6GrAdgXV9ueRvPa5_2S0fr1ixF3M2AEUaRurJj7hsZZEVlblmj4vyMYC0RslStMd6oVm5KASeh07RVRdMocSZgXevvyDn4RxjTclvWlIi2UoXKTgUZK9KDZE99IGqY9uDhSECRvSp0VBfq1MCIAIHf0h-QFv_oeF-SV454CbBcsMVSmAfuO_ZWvLguctR1UG3CBAQSLQLldo7fpQ6touCA4kb_SrISUzFNxsv3xIJtBg9WEQmMnsTmyVSk-zCiaheLMK4tI40cnWfaDx2aRTi82TyxUkPKsk6OG6Pe3OYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3E1IkghXibHsK6oa5ODLrksFiQ6f6zQEaYveK_5M2tWcepSdaMV8HgHuqFOcECvPAFbLGd9L4onJd-U_WaBWuzUxVNaJ99tqMSY9GPIBRhxw-BqDAXy4lt7LBYFNI9SoPjjAM4VIrsUpXJWLhIPeJegzBv_S-ziQfXaGOfKa6uNLOS2rEhaliIwBHJkwMX5-_V7ZRerjFSHjl0L0p8BjP_7fLAhpjAb7Z4AAoFAm0tj0YGKnaeZsyUWmr16MWhHko9bgy4Yero4ua-wBQ4x6ljLNdl8xGcor5gL4vJ-dDQfFrhmn_H0IEBXj3KKmeSUGQHHan4EMLuNQS_K5f8V2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEsranOUy4koVkIb-EwkXmSabHaQXJ_5iu4UgfY8QL96NwdJZ5-CYbsFr50lAd8zJzLOhsQ83JlprivEhifh6PKf5UhESArvOBwqpejR1F8IUNH_ghdfbyl5kn3FYwwQ-193rRmORL1OPv1rzsnQte0-20D1fqFFnyNjhTExwZQOWdTAPE0NEwJIP07U4jtiuf39dDdMKnnOJO4nl3EG3RZ_E9FY2ASkg55VGIMK6COmq2toQsSL1A6T6fodD76SVN1qRH1LFjinHaPiIzqS7Td97J_AC4XN1P0njk1cRiyScWwr0aVHiY3q8-wB1DbKpsoQWOFVgNjT5WoIXch7HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uiw4uklmRhdvcns7SUmz6AXwfTIyL-T3fQDmt71_mZ-8L8WFF2jKQQV9mh80fa8ezFMIJ29tbdLtPGpqtj2nBN5NryETXCKmPe8V-JzDyNH0xgYXRq5lHZdVfX5glunQB3Rwqq8R6oPfnGRtRyZn6_ezBesdd69ZGXdp6bULru82sz1prfegMdzCR5IRMVHLDr4MXqTGOTslTuFBeyd7K_rLXuMZm-3yRvwDMIc0f8vEUua4EMj8bQMLdTBsUY91JQYXTqe3npbp4_SkNHv8PnrMWw41URKJwCNJrFG-HDAFglG9nkpm4r0J5GArANso-ZviC2kdyG-ewckyEZ8bqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQv25N23nM3joAdnuLtnxDjy4XfUL2WHld8_C2J4NSNzh6GUmCNz_Q-28DUuFhjxOsaT8cYRd54U9c5YKs8uO1vbJdwKsZFi29-bIf6HNCS29OYD6aRgrkhjhjqImRrtjPJqb3rEWCxHeUTc89OiGTpmYxuLZb8iJ0S1h_0JKLaWSegMpIw47VYG5n9O4WFv__shufOylJCmHAvbo2cN60K_w_TUxZ03NqdEm74Sd5_XvCSd96IiiuVeHwsUPR18JdKdYE9hUf1wlb7KgDQWtaOeOnCLazweHYiQVNGAGxFO0__YhyEupWFCDM4p1__cGDMQZMjPUoKrbv07UPUhfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVmn50XsDhmTzPESNvT6o_Ltr_qUWlQFITMKcYPXqgus1cub7krb6QDwJh4p-DeMiEVtRERwjXAbuBlgsTvbVStMF0WHmQg9P4OX23FouHoQnnoZ2kHyDiBhWr3SynAthBmQ_UhS4ONs400uyqQnxtIO5fKv7Rg-URFFh27St_8dUgBDXMiNy7JQptQLFXMzJrTQgpLD1fRuVEN0tZbV0Os1jDBDiWzfOHU7m-TqFTltxi4ACtyCoPDAP_lT-ZAYzgSHrjkgLcRPXcRwWvtWTgHsXIglkgWv9VtJSBydeZWFEzXCY3Nm-Sg7ivP2QjZgSWJ-4wrldsTnzl2gi7u1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0N5pGmWJ8rYnXeB3WXmL8frDxaktrQjUbB-HYLmjp0dDdObJpmN9dlOJOc-wnh_M1gydqxE3FfzDfYy4q9SE1wbBUKjGCM8HeF9rnei2DOCRfMKzhnsCZUiV4Clz82CIEoFS8Ya9HCkseCRCsZcZNRgVjXINOnpkKIF4VqoVXu0wlv8d5ePhwvx9gIUuQpy9MPlSCnwvP27radqWrKfFq-z9U8BN1UQSSbfAKJ2eBgrSn2KsF0bqNYFyiqGiMmPjtq4dAQFVJpbGchadlXUcIFL6QGGYfxGqO-hsvw8gsIs9z7aWs6p8PVqMuA_wNLH7YMH5bfS2QpenoxaV4ZOrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4ukCiK7L8CQHOglpfB6tVRzVhBeyXqzx0fsWQc_Y3sfy8G6Eq_tBAVG--1X-hcfb6GjaIPOod90hIZ2I_fll3B3v6wmoOlB4-pswVD_4LHOmi-GaXTzRDd41BJCXp0-Wdh5JX-NYVM6OuHyzYRL6CC3QBLatyMKk1uLkcoefdAS8Wo5r2UyoVPz3KUnM3O7E_I8U0Ewdn5iFDYXGVDegUornQETop9BfaTGtZqZOy35fDvft9LLDE0ok4LOWbw7ZQtrOaAJLjfuvnnrVrZbGU13ESPIzw6cMiwdmtGRraJh5U87W3VBBGhH93sn2JB0Wh3STWNAhQ6NEjBqUZ-okw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szxSi_ZiwQia5oRowGrw80RpegsgDrN744MWX3whOFmKgfL6Mr36KTn1OcNxHlJWekPe3Bjkfy4Vzc-ZN5HjqON-CejK1FIqPvApc_oWR2aGjd0zNgqEsUWz2w1siLOfE-e6wi1L1tCzbGT2cdHnBt-Bxemki2TzFPPtyWO9TNVxgXIOaB2q7ZVeHnVDy2_M-1bux63a2VzAWKd9XcH2AmhBg6l81YsjdPRS59xnkSREjBAv1jrN0C6xjUX2IQq_3uq0RpnHdJgrB1nTJzQwitAtOHDtqKRp7essQZGVFgW8hRFR-u7f_MirzPQvScPtg9ERPzE0ejirROR8awcw2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyfjyr4AcCn6bbxZNIVpRK6zTopQwkD9aOWaCF5umhBdY2wVy2eV6B9y3t7RJ409gdV7clx7mxzJw78iuk3AzblZVdxzSE6_8MjSG0DTpn2KOoE_BiWCeErJfbjzl8ItZvHbY75MJOB5m1Qg0L6mrEsRKDalGD-HNMi6JBy9L9zoE_UqkPI_KEDbKGahTyNcMylcJi2UbKjPe6WT3p66VBeF_gHTL5ikJN6x30tMAepUPGmZrpRkemEPWzChXhTp1lD7hQqOtNELgU1qeG_qWaQVH-KC0tyrpc4QS8xsjZczB5dz9PuPYI68mpJslEZEy8YUyuB-QNfMGfGyXiyidg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKCr9C2GiqaFF0rwmtKcWY_qRHQMN-gWxXjAv6W7YBW-YFSk7iM1_p-kUTaVcopDuIq0UhMYVdgP8I-hR-_g6hlmOKGyJP5ZMNF0jp5ClfwQkJnBseLItuQ6NcQ9LmjS7NSvg0RsIzC4sk_1wvy9vaEzRB16xtcbIrYDfhQxTWYZZjt5BFA71dvazshogUuQwj64gjVWn688eoEG2VqMoerxkch4X1ckgc433l6uQtGnewwNQQicwHcbFVtUFkt4lObOmOAfJWyr_QmBU9WoLW3HANf6ThBqpZ7JfzYY3jUYQqVXU3OA3aHPJL7P4UmFY9L9I6EUcuQ3qKIeu2tLrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KT6S6upe-I277a-UAYKOY-N8fhKyBEESBRh72j_l1eturhDjufrXgkPJKD3lIlIziNL2V1IAIWaYeX-EUMQNqXdL1-r2Vrf71ZJljV9KpefpcoBSIbZocol2oSPA5mVyk5nc9QEwuswfv7-vUkhg11RnmFe1xodc21i29faCv1rC_GGcsNhJG7p4gm8E_Bana2dk4w9_CVakHO89OI6c2qctkTLhlmL0IAwJJpTcdcATKeqzf3SM27bRB_Nka6jWIHtyhYuwmL99JeeYfV-5R_6vNXGHRD-E-Gedeb-3RKYvNmXqL7-wawVD5roq8f62hrSaOpJGqfUyjNP42GXJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRhSQQ5MBXA0ssyJUiSil2nnXgmOt-t6rcn71AEMHNGftEoc0lLHL2urzfz2je0zMImi5vWoB3ilMDFvU_THIK6kDGBE2cFtdCH4MkIa3_0NINpHuu76LmXZwUn8fGY4w2HXsk63fnT0z2xHGrTlAIW_y2EuT41Tgy1GaI8UrLg6CElQu7LXla5porLbEyhX_6hYU1sYrmSCY8qmWTwr4Bmxdx64AN43n1iBCMpjudZdPfWAI9qYdpj5Y1o3RyDYa2H2J0az-FY6E8DbNvI3tLzTeo0Vf8V9kkpGXoFR3s_CKkKDxq7pU4ddvMJDTl1FFZzJa63t-FLIq4PS97g-Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udO290dE8i3f3xwNT9pKcJuqn_8LVhDq3rmAX4Iai23YpV24h0p2rknb7XuF2V-1EEjRZoajr_gPR_r3iK68pRvxG9FRgiMDlgqkdAMY81fcPUktUwQzq5grjZOYBp_IvOKLnhaURSZnrZP_HE7QuoflBdhIXOYalc_7Dz5V6CzRwpD-GjU1McfF_guWwqnD_eKJmQZK3h7o-k4qkmtupzxtd1rkUrxuIA8bFwpfJaRxrRcN8jdzZG4ciSCtjsdgjbmKz27RZ9RFo3_KBOpHv8wxSR_sH_umdc51NKoblvW14YwzoYOyi8OciL95zpwWmv1FJnHh1jh5hErMWfsTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOIq2VKZDw0OzWw_mT1SpfbV22I5Sgcn493ln3sop2I9b8POYFgTPYgCeHTIrxeVo5nadGzcBOOgYL4JGPmAm1-nWJ7RG-QHgUvB6VssAOp6ftPQ1qFYOSzMPaegYmkb51QngQ9D2t4DEQRdmJNleCmijBG2BKJK2_jGInjL8YlLPYJcJhvC88LD9Ncyaz5CWvv-J_zM7YOW4X6-XdoHY-7juF8k8yQKHDJJvsed5TworoiwVaEMCZwMXQIm2R3WV-JYd6f4Pgz5NlrUqNmhIWRnX3AcQINHj96EIguuTsXpmSLuCMDWwrlItuHarklBmJGezkP2rE7L8WpRrCAK1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyacluHDLGRqNHzrM80WlvcIjkwn-_ctcbWNwFRshDqHbqdhfrDfnL3s97cd4DeOPv6w91EwWR77XQu0dFQiyNpCLp-_GL0GdQhrubFqwIxDbjj8_hDCFa7LzSLaLKs-EFSd5TIGQmSK8HE2QK93qr7slNPGF_bxYot_VlmhlFDNEGs83nPC7r-XpXqsvFODCBrTAeSOIOVQsEvgYzPr7RjDjZ6p5wpxJpg0TIOVgJIS1q2i8ozw81xweAyJ1ThmXjafQiG8zi1fqR8S33mxgugjGeUSKa-zAVn8u0RxZOp-gsF9JJR0w-u9uAf7m2KvjanhEQNsRPDx9blBTQYp6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIEYY7W3T02awTuRe5-zUFar0BF9N1DTAGbZA0CI2rho33rQUqn84_YD2M3fgGKSHD_efDqrEsK3lxZu2bynsP5PTOG8v8JCXipuca2VNy3I5Jlzujip-7qpmo5hpFBX9RuajrhV7I4PMnqgWI6NXWCCwmZTxbmWxCn2pXAq_EjN6gdU5ezLvmQA9cG1veLEF4T1LOYR5VrQmZpE-yp-2jKe78Q62cAPWWwBY1g2YJPDsT5XjGZK5q-ABF3bb8XX-C1yBDIOcUIiMXuY9SupUXfnBKhvmwrbVZx9DnzHHetLJVmKkfBR4JUxsIuXRk08za8aLfTukjgdyJsVH118Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McAZq6xUORVHlXAsTErY5pzbCsTgaAXaPvvC5Q0aBwGMw9dCLxlVc4kesWpynuVZncYigtI2NdqTMJNGUtFtrdJGl3FRKzzhmIji9veCjsh4X2fOMSS9Nar2snH12-HAy_haNVlcBwPbOXiAGBxaotaMheszFkZOrU0CxNSN6zDJkNUhfKE-oGAt5A3bxFlQDnsTzBRzNPCkAeGmBIbZIa8GLUHlAUSIAmI39pQrOq5DO67wbJBsrqKAIMX6A85iLb5yJWXfcXVt4sPETRvt-gJpAnV6hSqFpj4IG78IBhEq0iaY0m-JbsH90LC1EntG9LWNYD5_ZaVHUoyYAJO_gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXsopHwEqC7Kf_eViTy3MPes3_tYtcUplnH2IMrmBFhJRGSCkyVakdWlrDKMMRPvw3WvxTDE-12reP7J3vhHQ1UN27kTjEeiLQiaje68TR7T57XDVKBe_5O1CEWoPQchqOmX8vCtbHBT05w-xgs2CJkJpg92tW0ZCf9lhXL-tnzufH99fxRBzvAjDEndLEBOdGCwt3WIorU_SgP2t0P1wLoDnXxgty4ML_5walHD_3BUbur-Dmakps-H5GUwSUIRJ4jFFcca0pzfH7BM8knyM1RsbOOg9u_EBuMdj-5Wxub7E-sAvu3rF52NR05-98ZYLdnPQJtEEpLHuzEoqCdVHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7fx6wEvWfHnBgPIxmNM2QXhGHrFkyOu8ewdhGEWIxnCGK0KlgIux2wwlBEsq9KCAbtzvEYf7TSh5RkFarcW3NhRkFAz6xKSRNZBBbz-y2NV2euuFmjvd04eH6p0Eb8bvCr68W-wZyCan8ZfbSyiYHdOaVckL7dSVfvrw1YyxFpCScVKtRnIgVKUGEA9nL6cGDnArJwurMP_tl0XmzU08p7H_X29Qn9pKp21IOxrcvUY8lr3hT43-xyLenPoTsVfTuSdhE5bNJVU1Pmz-AHhoXCrevL3ueaOJcc2kMW91mEIJDPfnA96M2_4tHhbjYCmJ2LPZCO0d8q7mx8r7S90AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9xeyU28pU_G7ulaAJCao8fQI4gauOxESm1tNF-WFGBi-nRxa4jBQms6Unp_7PAHb_xkqsWST9-MfTUhT7PU1tMzNPWLof7mz-5byYHnwZTw62zgvrpD-eBvctH25oq5MI6sg4gjqdi1BOcXTPG2zfhU7xDPTzQLfYI-JnazUVljqroG--9ZjbyDIq2ijmIHSY9UvE7V-Dvl916unc0LQjhtCRJ-JThddcq0BRYQqhXri_zv_nblinBgGE8GMi7mmDsXfxY3WVxtBwu6vAkllZDpizZF1Aboe_JC1PjZ1f6uZ_G1lK5s_3ahBwS47xxHPOsxF384-4hDNDyeoVaqQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaLuFgGqoqp1Dk5AcLzhJTdIRk_fpgTjNXSM7ZMCmx-qHojwAaE2z9eWX3TZy35-PanBp31KDYUTQeSfgiN01R4QDnl-URnYMBI8CHrMxcIFN6S2NoBsxmhr_EZd1bRvyD_kVinkVKL4x8yGxkf4KNecletdBw1rG0pUHDRpO9QqqZofHhIciM-QDMKJAx09X_juLuVRUQLaeIByXNUaMS4sjyAoVg7cCmyYxnBGg9AC5qcKb-uM6HVvUEhTc_BwNrKl0zPHdqKIFgs7IukPkpUrq807TZCIm5U3FN8kf579pLeYB5IcDnABVLJY5m6IpXK772AdA0Yfj78cFG6zQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1gA1eYK1BUdq2L34oB5hwZxbOHp9zYYrnyTFGwlBJkZvVD0R13ScWtf7zH0uvgioMRVjkvo0NA8j5foCduQNF0zq9S8hczxfN82JZsCRvZL6KaaEM5fUVf37cbzfFT6h3r-hWhhQaQ1zxl0iQGCtN3m-nsEl1cOoM6_bBIytY0-IA4xlNXvRWzW2voXV-ANxQX1ful6z8UFJm8fDiRD1Zf8B_GblN_y9z9KjSyJej4mC1eLXdXwvJa5L7dNuvbhTrMfACrDJ4bnn0L4X4lYpdJ5aJOtj0gVzZjMPf7P5YlkH9L7ycAmvOjoWMY22K7HFWcZ5EYYqb4PrpBY3JVY5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns50ylE98LxVJslZE6QLyysptDErxLgG-UIpJKgoQqJ1nQEvepKsYblpgKoM4ACIf6ZDlUO67AIbMsBwdL1BXnaH2K--ocdmVUPiYrnuakmAjwtrRytJw6PUCNPDz-egS9EZPnd4k1LoD7y4yPJWjb_1yRurnIBy-b1a1hittE57pmBak5JMC6r5TGYVghQ0SDAXGp0jB56IkRtkSNUhsWcIOgYRyvPBtAjmCSK_bsnUhGwKVniymQn-Tbgr4pfjzqmFFbjkVrLav9bTrZ5tRe1lxuvC8bTj6NacbDi0cMPbwcnBF6QSnDcY9Wsd0tOUAZGkRUF946Xaimbiqh5cJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7U02WIuihcs3nKwHy8EjlU24875pdWk_csJg0U7xq5Q6ZsdoODZExaxHvsH_LPACk3svnVO9l_BwmMg_H1utyGG7MTp7OTFwziXB5b-vXhnivSkyWyrLo7gC1a7G-pw8XceSoJa9-l1RLB8jakrUToxuyO4hgMUJHYN7RGUNbSfDLeKJou88QwYwiEamthiuaKMHgw_PtWElywbcOtgoDtOSFJmWM0zpj3CRx1da-wurH-Im67G4_5m34HlYZ3e1SGGhSE2T6WueRxaNsQykte0BADonFACqm7OBI3MPL4I2LAJx5ThKK6S1po8Rx2MSjHeK-JSezxLjWUIYebgIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT_Qk8DtTAx_wj3NfSbvuTVIYKhoXExml-qofpw4SG2FzzUrWQI7bO1G_URR9uLPptCWkzHzMfe6UPbVKB5AJ-yjBDhqG9ZedPlB7q_pgYR6_80OQNdAM6IuuwvgeAFcBQwGGOT64cP8RKattwaWvO5QvxIqfBHkyMLvxz917d4E6WVGodSPtf_r95EemoAehTWK_s8YO1dwWRJIldL5ATvgmghVKI-prngzs0ucbSVMp3oWWcXt-NsMiyddEMWI9mVn44Bwp6iDcBJ_vJhWVcspGtlvxFTl7yKXYrzhuYbk-bcTGszhp7kxlGeoy6aarLCZAYRKhbtGRdL5XAFfaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYV_QslK-VwV5RvFkdy71ZT2IJvauXCkqSG8BSXtNQIgRpwmMEd_U6cG7jzhwexFf6ZTs-vsfZuJNuzbreYCtEhQsvcbvnU2hltY4TBOaW532g012-jOzXTld9RQ56zQ545mdEeyvHZ2zHh-m7HFvutLVcO_l27ZhkQ9996ZnGoyw2jjc_sRFK1a7te8iQYmGOYSafifYQbrhVB6COX7hNqVfPsXfiWQoBu5xFs44-lBVNl3ZrW-J55MSoegqg87uLRO-0IyBb48uBPiU63OW_fKE--z-aa00hhjY4KeJJRdZ1H5OrqCTKdcN-cMzCvA9tS74XD3E_m1b-7mUltwDA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hYcv87SG-8Uin2er_SlP7B6osFj5J-vr1TzwUHX0kPvq-UmsZd-jdeli0g4BNVCkSE8CwJEGcTWalHW7oNDD8RrSXHTiuCtrMYypZHIA3_43Tp0HcAdgiUcN5XNF2kE_s_VEG1faVox0I_HGqeT9A0tbTITBSjeV-eiBlt1Q1Q0rIIjj9NfImtqDm-G6ewA3OZjXvz8R91lXvHK5ZD-84kcWmbo2MFpUnFe4q3GX0WFIF0IdzX9qiJQkssLCtKrtJA6wUXp7n98AGHdAW2EktVEB4TQ1VHfrfauiX12Ft0e3XWex6pClbVOr6WC3RjVQHOabJ51t40WGkl6brBoSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hYcv87SG-8Uin2er_SlP7B6osFj5J-vr1TzwUHX0kPvq-UmsZd-jdeli0g4BNVCkSE8CwJEGcTWalHW7oNDD8RrSXHTiuCtrMYypZHIA3_43Tp0HcAdgiUcN5XNF2kE_s_VEG1faVox0I_HGqeT9A0tbTITBSjeV-eiBlt1Q1Q0rIIjj9NfImtqDm-G6ewA3OZjXvz8R91lXvHK5ZD-84kcWmbo2MFpUnFe4q3GX0WFIF0IdzX9qiJQkssLCtKrtJA6wUXp7n98AGHdAW2EktVEB4TQ1VHfrfauiX12Ft0e3XWex6pClbVOr6WC3RjVQHOabJ51t40WGkl6brBoSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyZglFA0sQCGFhDE63OEiRh_FsStDfF3kwUvb9yxW9yDoO92BVtofTNpXVRtJXTp0-SOhm3Wbj-siULK233YWxCDyzZHsx6AVMtWRzJE-Ndwz_9-29-MORWa_BH-vXGZiRDkS12OA0sik2Nc_w7ls6SZ6nZwUS5kt9c-Gtp4j0fLVl3r3-ocbKPugtBNolOHMi6mGAn64S7KqF-IHox4GGIX3s3QtCu4R04oIEk8LJOvKhGgXYJXRFwwUfDpUVG12_jimVMwntWObe7RxG9LzuX1diTL-9J6T6w_KErnNDZMen_BBD7TUujDItuml9rNcYnVt1T0stllPm69vAfGcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ2dSaI_aHWglLLAdydvWHPhav0aHOpBMUA0k7Swq0MO8y3hnKjMWoqD8RCjvhVwX15p57boY1ONSx-vNjWwK1SM-7_-7Ib5fNk00jtBvdR56ZzBo081nPFEv59zZj501BjumdgGKNChIhFN1wTyZJ0MsPE5W0XJcUl_VttAluZi6B-l322w115h-v73mos9hm7kO79EdULcWHN4BnzcyzNNaO2zFRllAA1RfgiP__5-UwVP5uHYf4gexW5MCf74fo5nqTxOvEVMzvKGaPxdSuDF2qq47YucNurLoMYLCkJrHnoXU3qrAzShNz3avJFTiEX64QDSW0zTdKmALT94cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWwZWrw0yX7v6NMthoWKEufgK-OpKPTHedKHcRSZOmC1QrMm1E9qoYNvyycXJ6KblbruLUsiiAM-6ek1a3YF5Ld67BzzD8TfC_q1tTI1OEKQ9k8dXS4J1txXOhEUzlabqaCxoOhZeWXvrm5Ja2JSG8SfDoPRNH1AcaRMOpgBCMG04eUajNJir51mURu4RyEDTsXOSYXZIx3HpL5-c2foTL410tCvkBQA_23sfCnsCfJcvwcSFI62FhsUgrKsGvhJ5szOOwoCOCdqR6LS9ygd0HqdTyoLGTyFZ3oNREkaMqP567aglVDlfzLV05WcHyvwK_rAIkt3MeK53H-DVCosUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3QmGYGg0nnqf-zvgzcD7iFqT_qgglfChT9CLsNim73p8Ec6grKTGmdRPVSIpb4amV0t6jd7XzIrEjDqg-gjfu7Rsaj2Bk9OEne_CY39lx0pABcy7IZMtyM3LZdDKaOfIOtoMA3ac-t9swEq48ZD4osyyJHVo_2_taeEiG6rhCKP4i8pyoD3_-5OftDF_sj-6jh6jYFWzbFrP22Z-LcOAYq4Koxuq3oZHpnUCOM7PjPGBBVb5CLmQlwIT-CSENj-Jwfqr-_R3acCc0xOBsOfopO2_DhQPgUMkODjP08jfO6ayx6gzwBCpLOd53SP-pqrTkITKHVbmLhbt0aQAamSGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTsC30UROSKxRDaL9mQ695niyR_PNQRTz1lcfKHw393195pfEjAlalPTpiGFfTx1aEwa8nUhTn-3wkECEpFKEWgg9OhwfrHsiPBnIBaDSTsjYA4tMGdM74pzRrudgUwiD-VyA9h6se79wApaGtKqG1g3L9OzKbaGiAKjQ4XDXOhx0WH3uNWbAQMSgimN2cYku0cdP7-rbw7Sz6GLlVvZ2du9w6dCyYNIzG3L7DCY1vCHXPcCSIa4rmaXgtHS67P2cFVcx4tivKusPTdcGaSRj5w5N0kleILiDX9Z085YQjDqJDXL-ImUKnf-eo_Fs2IYhs8fMAi9u5laENImotidhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4Jk5b0bBkZprqC79rgLr5KCpFZ3qlLyyP0xH5GN_oYNn6q8aDK1D0BanEPeX1sdpvsibNi92Pwu7_jlAaXy-gZQdzoRSsxN7uR9vqiH1D0s-q4dFlv4zxhhNDXTtS5MHvsIUdL4cpNRaELdt7RXnvLAlQkGGmu0E-Qox6Gfc09rs1SR24UHhAt20JSWQ3HyOkFrWZGLYi6q8NdnrCQjhQ1rIB-7hW5ne7FyEK3OgqfQJemOfR6YfNYdgA_-PyKK40aQQtJajefOYikCfVAC8ViOld8ZUHnEefVd2A7lo1PFdoIZ0EkF7wkl7DJaGJ8IPj6-DSaFskPXE-bLHCoz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csKcPg9WBvGtocnA343XPwHTb23ooq0f8gei41TD2N6rnvLJkBHVOkj0sn-60jsKFJvz8D8zkpD6cmdffznfk97-35iEZLYhfV2bbt5oQT2TZ8LnEv4R-R6STG4p9gv88_uaExe6kVA5MdJoFzZuGjDkUfJHcIa2NvCY4hsS2CIaqBkT46q66Qt8ng7jgndfikuWGVY8utFzHzgJHIvd2m4H0IsVmZhX0BovrK8dDFi8LmpOza2KI64ks5dds7etcWMoLW8FW9-aD1eVVhaCQEUr-hetGaKnWgm4rQxScLAOLZGsb3iJw695YaX49jCSaMdRfQJiiv1Kz84uasZfiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=YccMhUSgMpaCQaPUSWJfJCOUngypPtFzPbIzXG4ElqqjWmqIehXZ_Vh2ny4wyJ_qv6-lQCoKnFG7EL8uxRrHgtB6Q6Kta5Ay91tVNmoNEfJprvmg7iHXAt6f3Wo33qaoF_yhPnEs2emW2oX58pE62qR3LuvUfwHTc9TZ3Zq665Sqt-TfcU_zqf5fX8lGznnL8CnkXfz2Rk7YZ_1LEqJwXsye7bLrmEu0eDgSqM8vjq0qO7VxNnb3DfaVTUOM7E0j8SlkD-9J0CvCWIuJzdlPpEfLydgYuzuVew_fS87brXTTFvU38OJXHjuh8sfF-488WqfSMuDVwNb2-Hm8Ldz27RuaFV1dlmhEUekWhUMHioppRCAEWVjWawJvFyx4nroBuG7wJ2mrin2fUCZZiBOZb8ztouHJkzb0u4DyjNhM4IlD3TseZfZ6ypj9TZKwsTQ64IO1BQn2VhjEH6dNnpgHjny1n-ZGBYxSFjPcIeSc2kOEOW9y3F7CU-9fQlFC_PsO13KBOPUhPSwuDMZ1TtJCZNN_tBSlNFQe3TixZY6lSoswbDng92jwN3usKqggJ2-erbPdV--oAFlCS8i_fK2vy85W0sbYjNpdgJMsCzqX4WUYnXwvgUoH1yOCB22lYbrhLMwfj6L0GYe1dXk37_nRlHPnghOs4C7V5wzBGBjxJAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=YccMhUSgMpaCQaPUSWJfJCOUngypPtFzPbIzXG4ElqqjWmqIehXZ_Vh2ny4wyJ_qv6-lQCoKnFG7EL8uxRrHgtB6Q6Kta5Ay91tVNmoNEfJprvmg7iHXAt6f3Wo33qaoF_yhPnEs2emW2oX58pE62qR3LuvUfwHTc9TZ3Zq665Sqt-TfcU_zqf5fX8lGznnL8CnkXfz2Rk7YZ_1LEqJwXsye7bLrmEu0eDgSqM8vjq0qO7VxNnb3DfaVTUOM7E0j8SlkD-9J0CvCWIuJzdlPpEfLydgYuzuVew_fS87brXTTFvU38OJXHjuh8sfF-488WqfSMuDVwNb2-Hm8Ldz27RuaFV1dlmhEUekWhUMHioppRCAEWVjWawJvFyx4nroBuG7wJ2mrin2fUCZZiBOZb8ztouHJkzb0u4DyjNhM4IlD3TseZfZ6ypj9TZKwsTQ64IO1BQn2VhjEH6dNnpgHjny1n-ZGBYxSFjPcIeSc2kOEOW9y3F7CU-9fQlFC_PsO13KBOPUhPSwuDMZ1TtJCZNN_tBSlNFQe3TixZY6lSoswbDng92jwN3usKqggJ2-erbPdV--oAFlCS8i_fK2vy85W0sbYjNpdgJMsCzqX4WUYnXwvgUoH1yOCB22lYbrhLMwfj6L0GYe1dXk37_nRlHPnghOs4C7V5wzBGBjxJAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKX_9swO_yuWfbCxeFbSsO9NqJ3bd4BHdrFDGhT74i5Nj-O_EL2W4Bf7gQAZDmS-gaBV_WDkvEFNaPGgV3-T8FHQJXM2pi_pfegzKaidG1PQ2ryYZw77nxiUMjf_PrKvzW0V839iifmQphVyGeFO6NTIaHmjK6DNL5IKgbWdJpdOHXhbbx1zBKD3neM6r8EgTb2BhBCBU_0H0SjLubnRIKb6YUGJUux4I_cDV9-6AOqy_GX7MvrboZJuBfXKYsqI2cZHLjGI5ZLF9pIsBYL2PsaRd-YLwK4l6laaR8KTI40Uf5aZx93tpzDDZokERlPeprLZ0FuHCxZw0QDIAaw2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9WNXzmgYYOvgKu0c-IMH0xL_XIyOlKWhWZup_P0f5Y-bjipBAvky0Pb6NNcXgIe0ytd8MuwYDQ0H9wn7YfAGIE82YUiA10JiU8G-HduEsaj6URk2GBF8b0wH7VEuxcWWkjVa1qzADrFdpfXHRXDB9Yaf6QwlbvH-b7DeCPeX6Xu75sJ0XX4Gas0yUb2qc43ajg3a8TJ0gvZZL6dUpifDYiZ86EqM19gjcoesH6ICzhWogYMdhCj43Hv6Xjyu6o1sDlR8vYzVeU8qeBmskgK0WzYZfMEer3pyjwraXyhCrDaBZ7PrNE0zamzk7X5FDwc-Djp3wU-g-tm5rViPSObCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3RSC6__77Z6tdNE7MsTCARkU-ykhvW_WFQ0nNNRsUk7GEblBnpzkBxYdPGhPa4d8N9feo-hUcrGF5GxiGPOK08l5kAPhLYP4KNbAw1WfdLhxjUnH9xGyqh2V7MfC5ouB6rCZlCYI7--v3fe7JIUuZOEgUxaeg0--gvPrAKqx0TILbQue9-E4DLee5QOt7buFVnP5TrPHZsgeuIDK3g7MuJjKwYyaf3Iru9gs4YYJ_N1bZtHzsJzZcs_aJWJLAOZYm_RE9ETEvn8rAcyba9jDQOscYJVOmCz1iIiEYNxr-CjDldpr7FzumlTXlZcbaZzG97F2JvV0jVVoSSpZwFzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jz27qO3bXVS88fd62ehMQq1nzZretR-1-SU3-Mu747WZeta4DkCBj8Zjjv12rjHXcDQu_XzLwMOJfveKctFXofYZWZr173N_BU0V7PAzYmHQsnWMxpO_YIJ0ayoXq6WiOgI1wZ5r24ipBbA1Djm1vG-9kDZQkJfoIccV90h_mX7N5s4Zyx2im8hMAEG7bantFkEjtSyWPKI_T3XWDOSK1t9XclTMwMpibaiV9Z2KUJ8bH2GUG4uE1E9mYuEgkC8DrXuhpwU1dikAflVhddfGa30YyUooAKhR9Weod7uTE7tKjz2SuXZamMXvgJThKB8I44ylEMqzl1L7UKk-OZmJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ord0oGYcze3euvQ5_kHeQvdjkEPMLViJ6BEyP9DnC4vxdWLsoYVjs4oC8bRiuPZRkfSEq7rm1Ql-QfQg15hW6oHBsC1Br12Wm5BfD92aExKK7pfN5jY42fcIIVuQH4CmGVri77rr_2ombOUh1U4CcP9pTtgJQ7gzpZrcqIXnTRQD3Q-8t1jFofYwH7VLzvKhgbjN2ar3Zu6XSfhPP9PqSU9QWx361eoh3A7mbsHxgilmq05Wqic4tQ8yatpIBNIEZ6SEMRlGEMT52ScWk1bnT42j6mbMlsrtKvDc0Vphg1xSf3Xd5rIRXvegwUdueQNSf7m8-GpMzd5GdEnr6kbARg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m6sltU3G_TuC4V3XBCJTujYN398AQVnsn-5wnU0VvGB7m10D8tawfoZiZhC40JtznRWGfHMA-AtQ0RfOrThKI2c9_w8_hvn2b_uDHiaH2LTa7xEkQZgUgYMkdgKFbUgyLfk2Dpu5cw1X83ykTNgN80em2Yh7s5dizpAfFIkTel3aGVYxY0AjUvC8ymjGWP1CeWtXKKNqsswEbYaIWeDaNJB1qrw2-Z51pwfDK62woUtgv4qlPFVcLM5Ol9rmMad6IkBkU38c4ds0sub66NJ0Ds1ChCYNMLrvpwAFzDD_-qJJQ3iu-4F6KfMfoKB62jYw0QY9hCizG2rX4wTmIRWGV8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m6sltU3G_TuC4V3XBCJTujYN398AQVnsn-5wnU0VvGB7m10D8tawfoZiZhC40JtznRWGfHMA-AtQ0RfOrThKI2c9_w8_hvn2b_uDHiaH2LTa7xEkQZgUgYMkdgKFbUgyLfk2Dpu5cw1X83ykTNgN80em2Yh7s5dizpAfFIkTel3aGVYxY0AjUvC8ymjGWP1CeWtXKKNqsswEbYaIWeDaNJB1qrw2-Z51pwfDK62woUtgv4qlPFVcLM5Ol9rmMad6IkBkU38c4ds0sub66NJ0Ds1ChCYNMLrvpwAFzDD_-qJJQ3iu-4F6KfMfoKB62jYw0QY9hCizG2rX4wTmIRWGV8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqVjXZPDL0-GoE7p9JDacboOPpJCRjIzBsC5UEPTTUym6fNx_lPLSrbPkZGJzDRi2M9_lJEQ3CqwzNnKGa7eBPiNqB_yWGmHl-UjMr83PTfgoCunL8b148HZUDO_eZYU8hKSf218d1imHUj4IyFUYrxTYwFUbkAjjxxbNTREi5rdEE8_zmJtuq1u89soUjbt1lWI3qQOPYhQ1I1Fz1FdBVxu_Q48fpXhStFndZqojvUT6dE9QSITk0HIcb0b-M4BFV0BIvrMSRaNXwOaWkxiQMHev_vSRCy34Uh7xE905Jym-0vfIvDOmqb6IswpnUhjONXQXrL4suQNGSdFX7vhgg.jpg" alt="photo" loading="lazy"/></div>
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
