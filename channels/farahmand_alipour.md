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
<img src="https://cdn4.telesco.pe/file/dki_9AGfKzqq05ffQ6hyBlKPwjQnZdnmOaaR6AHJt_Pb7kqUw4IALCfZVpLGbMqpdn1vTMJnDajQ7vnIbGbP9kP01RobGblvHC1jfR_pEk2xGsW0b_jC6btOLTZniT37jljGizM5L1dqRl6jUyinBSorGqTKhM5liv7fYdfpAReNq-6L5Tj81Aizyg-HGv6eVrUqlkxGRtpqpRdmagI2FU2ddA3oeF8gFNbfYcZNrhel8QaqhK0xQisb6D9Jf59G_ZG09Oz6aO1UWC7i-cGKrw0DA-iIOjAkQWCpebMGlJ_o5gjdteVgCHWpWNwWzTcbuI_jn6p2M86mpBWuMZJIaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 14:34:53</div>
<hr>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaR9NCTrwfD3vNOBPEV_S02tSUAQxGTHYsaGqTZe8cxl3XZbk6-NYz9zE-j6TFbqoxXv4HH2e7VCHv88NCoIaAFhhf6afjvkUnMhtaos6_FaGu0E9qYBfZdAxwBL0Q_ffvrCzzWZmpOokMqfNNk1QArR4ja7PYyqgsghhU14YdlLRay263UIv85n1mSM-JY2k8eUKV1DEH3gpxS6vfrU1ljhrO1c7lHjmoqzCWRnc6AkVi5Vud_EiBR5HYC0_54Y9Go8yRMPJJ2swZ8500mFr45cUI7Zgu-7YnoG9dvg4MW0nscGvycALwwT_929FBdwfUGUPLOs4kHg6VnpQ7rdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZiXrTQ7SbWFTYGt-ISF50z8dQUcWY13qDeYiPD2ddmdAS-WAnfIqxtm_f8K_z0BXWF0jU1K7dQU-_35j37WAlPoIBqn-I7xhBv2A2uFes3oWutiTahuNH7M-ou9bkSb-xbubaCy3faxnVzMsdMnXk7mVB_0AuEeM2C1IP_rvXKqaqSGZo__TIVSBFSH8dj9eUIomA37Xfm8TlS4wnjPzQWqp0Yvvy2jcEyXfIUZal3Qu5vklyVFOnGqDx22Q6V1D4xdtTVNWW4jZSGwqtxunPoP83AlHCSTxp85GpuM_P1VDnRJtXBUYfDMyHfE0HdsaNOFQ8yJSUx1_iwtmJotrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKJ4HzQmGUukaK2SOoS0nZMqIXq1oLpO7eY3wwGSmb-Cxtwukf22u7q0kMUzk5jzt-RAuWt_n8WZAILkqFSdSJMptQIsofkk1VV2t0b__g9shXjxrx502QVekeO2uMrEx62SR15iuXlEW4IiwL0Q7ZWkKc9Jq5Es_fvmTpmJpOzouQUOWfTsp03nImNmMdEjB6O09NSUa8uYYcJLUhtuzu_D8uDEF3XBqZNRHcf70OH7xLM_USA_Rr1KLirlNRSHX8if7bnad9Z3l_T7Gwom45j79DuTfCSTTwq_Iib6lW7kG4oIErYy6nuPgopZ8vWJqTrAyGSAWeRLkNTvmSQ8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Z7H6AxPLkyH08Qs4N309MhQcJ-cfZczl-6AnA7GxAz2qm_AGmdBIHTqAucXON4WqK4aACb3gabC9cmvlX2PnzjO2550JDIkKGrb3OlPNXyRkD2tqBdU5eXp9ON-jv8w3bM7ALNaGiJ3KIUK8X0vodjwcT1JCl7fPkG23hQBA2k0lATISQGAIhXLRQzNQVYnTF99k4uwg7Wt98RiHwGO6GMHydnNfgcKnWnYEuSVBuBQFKL7T1gkWxRWL2lkBaI0Ny9FwFJOynrWsSfiMK1tuWxODNhMK_0ajpYZu02CE32yiVS_Ftg4EVi3SCoUcI0cajLTH8rNRikZU6CJRL4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTKEs0y4J_GsjRjOZY7AbzmvKlAy6uPOMFYRmW1lPTvJlgCJ3Jvtw9pqngLfwOXScTksFiSJPZc6imgv0vrD0BuM1beog2zL3YNHkDB9qpUPddpfqOB_R8fKKZWNb4YyCmWBufZdhWpS6-LmD90ypwcVjm-3X46AIMW8a043GLONKStysH-AnNhshpxb9rWSxafzpE3JhxBQqmvnf0-M4gKETMpweTmdnAi0TSRAROtLoHU7rCQMDKLE3mEZMnOUxoLABN2Qetls8jyBjaCim8G7CuYvJjBOX8HhQLjYkFVJhnWXqKBGpcEZg5MWFPUXBySPpB5dtQER_cz_Jdq7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9LuuOXkJJJ11GtRZ9pNp1zF4kdbQHHlGLDop6TDMS7y97g8_HSOOhVpyy1MsmJKocbNFTnDDXn7f5imiuMb4MoFiCm9Ei2UBSB_mkQLJNhf_f1d6eaA9K54shcZwqCCGjhyzl-4PASTS43QNJ1sUFZWe5GOKi3k1j2pDkJdRzzpgogM6eXbhla0b7rBsovEBbA0qS-FVF3rQw4Hjlb8iB075ez5448hzCZwDLqdYPFL3ubjs4UfA3PhOqxQCK8ImOjwEaraC3a7d-CXgRZU35UWxotshIt3xFvFatUgDx3U9nl8iwFMmkFvMem_3GJGR3Toetms_y7fB_m113PvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY3Q2AHJn5uDtLFColFfCMpe3qaje_eKXc-uoay-xKRgSlvSPnLo3DzewH-Qi0uNscdQCjItqVXI-684BCOb4I-e24tBKcdReWDUq80BHwGZg0aPvccBWw3CeCgxgWNxOzj3mdfQpkiSw3hqc3H6neo8X0ndmmXh-eBpUaDoj_LikZK-K4sX__WYPrAaZn-V5Z4-WE1wnDDuUsM9wZxu_0_ggPxb85S1sdYb9WqrS3n_pzr1MzZvD-ZEgX3QFHXWRXoIIJ82sHmlaVxDvnycXvlsUm2TxuGni_2g80uDbUL5aw0sxX-ZWkhIoM4TooJUdT5yBJXm4koYE7gXp6KlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohLf0y_BQ-E9Z0CUnfVlZuQC4JUmV4KIhGXjP1Oxg6RI9aQ53RyI2-GpX4vwhDrYHagxe0QW-Vob5Sa5xK_WshUlqyajKtdDb_4fdfnvTGEBI0Af9FI-uN-gWaVjeQv4ERmME2W9V3U5DSWbvUkhQ6FYZQD9AuRJMOmQj-GD83c3DdBRPNV5TsAJS7NWFA2llDOn9VnanRliRe8VSr-xoaj2DztZZuE9iFZf8D0iU5XjssULXVkS2s2npyV2WFJi-ie8bFB_6jniC9-bu1bzBkK9NQBv3kmzcanVCrE7mH7wfsoWqWFWLPWfxq9ygpgluPlvKZERgq3mvnOTiOvzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCDoxY4M4iPw8TKuyDVd2meoxHBIfd7rKs6PlWQ-5QQyjSJn1sykxlDZGyq9PeLvYQoEpBqE4-TNrYM1o7E8IYiV9roeS_GAVM3udHftrbW3ogLdO0cw8MHSYIW6kSKaCHCuNfb2jNaMW1F_ORPZypbdogt1IKfq9mHkzwkSUvsw42Z_I9nOIOJ92anr1t7jutlyBNRJJbbmLHpSHBF_OcO1wAy3wBXvGu_bFK83GMStX49fu6dU5Ar1-A68oRLJK_UjmnHMvKGs8MNc5vb92FA278lqTyDJ8V8DblZUiLPkHJsMeTNAT_0sy0q2CQdu54YzWw21L07-SadJ7zr9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxhfmUAnaO0w4IhtIMoa8VB9v4Vg2dHjDW-AN0i89jd29JLXmlOJB11YaEDffhn08wl_P_YpFtRLNXZUoXTmdn0umQV_k2za7OFOe25yWKinO5p_uRd2J2vbsv7Mz81Gw-q7WnSSZngH22Vk0Sw-4zzWdywhxHYxdFe6ByUERe62RGda6rjraDEBvS0Jj5uJxii04VyORDN2_rASITp_WzilC23wRJTLaK-pV8qK02V_7nG0yBb4aNzUYxEXRzLkLBkudfd6L_O1iM_KrVv74PjwnlXfjrD1yNAf2ef3eB7LnGKv2u67xbzvLWtHHieHyfxUJg0aex-nZkt7uB4kmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMEkULeRPDWC1tt9pCOmlciNNdEFzMT2cr-ps7pfTnvRw8mWcLEplJ0oJ674cPEsZ63N2sQOsHW43y6tlu5Bw8M6GCNWsweqd7azOa187B_y0RhKSmUBra1BPGjm6Bf9TIYFSuO4dgZ8PkQW-rx3pYutK3sXfjumsVzPoFzxPwj4Ev6v5xPv0tMG2LFMK-wqBBlpm_st2B1AKZL9cs5ve7ENuS6FTSSaDulS1RR0bfTTqwMyL_iS4qirsxiB7OH73fApL89T9uQaPsClvZPu7Fg7eBrl-p_XxgWXwTF9MPvEHZ110zPjT0RiEv1AKfSoS4YaLKCTPjsb9qP6Nd6myIH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMEkULeRPDWC1tt9pCOmlciNNdEFzMT2cr-ps7pfTnvRw8mWcLEplJ0oJ674cPEsZ63N2sQOsHW43y6tlu5Bw8M6GCNWsweqd7azOa187B_y0RhKSmUBra1BPGjm6Bf9TIYFSuO4dgZ8PkQW-rx3pYutK3sXfjumsVzPoFzxPwj4Ev6v5xPv0tMG2LFMK-wqBBlpm_st2B1AKZL9cs5ve7ENuS6FTSSaDulS1RR0bfTTqwMyL_iS4qirsxiB7OH73fApL89T9uQaPsClvZPu7Fg7eBrl-p_XxgWXwTF9MPvEHZ110zPjT0RiEv1AKfSoS4YaLKCTPjsb9qP6Nd6myIH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=B6na9xL9Q0XpDXhjhh-xhMLpvw9HReikI0YWVn_C0NZQ_opOmmoT5riVRfwmo0D6WT_cFug-VKJN56Vzz0cPJL-R7I5xesPQlenqEGKv0BaJX4XWDOTPZxw0ECRndhK6IVCmbCJjt1Saz4sU89sD9V1GmEur1GmbksRh8RiZCoSaEKRiC7l7sWxcyJqXRp7avfw8eI1gelOpFAv0ReLDZ5qFdse9lUOZdRR8GvIlGRYCpdKjPO8uHHzKKk3eLXOEp372EV0V_dL4BwpP9f-onhNkf8Fa0kFwp5W2l60FBCvQ2QZ7v2p_cIcaG6-eUjbpbboRqN6VkmrdezE98m5z4XAOktpLg7yoF1NvYJv8Q76-UiMkfSbm5R7nNRIRdLatz23o-Pi70R2vAvD6BISSn8smbwrVZcAvB9rQE1SGFNoSh2NAtcwuj1Vwz6Fge75OuUb1w2YfMhSquX_KvzK6g46ZnAODCcGYoF1ZMdPfRI4DDc7ZHRHt_x2FpKV8kJ5Zparsy1B1-29Nc1r5GcvL0OxnIEtBVIdJL81NUbFmgi-hBnhOv3X_wY_MukPtXUhSdZiSx20ylBIHJIU7jb-3oZF07m5sNBBO4hZGCyq9Kzlb3VgMLYUkHqMANfFptUecIvBfQIzmEYYHxBsdq96Ko2cOTOCprTgG_QWZBU01c8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=B6na9xL9Q0XpDXhjhh-xhMLpvw9HReikI0YWVn_C0NZQ_opOmmoT5riVRfwmo0D6WT_cFug-VKJN56Vzz0cPJL-R7I5xesPQlenqEGKv0BaJX4XWDOTPZxw0ECRndhK6IVCmbCJjt1Saz4sU89sD9V1GmEur1GmbksRh8RiZCoSaEKRiC7l7sWxcyJqXRp7avfw8eI1gelOpFAv0ReLDZ5qFdse9lUOZdRR8GvIlGRYCpdKjPO8uHHzKKk3eLXOEp372EV0V_dL4BwpP9f-onhNkf8Fa0kFwp5W2l60FBCvQ2QZ7v2p_cIcaG6-eUjbpbboRqN6VkmrdezE98m5z4XAOktpLg7yoF1NvYJv8Q76-UiMkfSbm5R7nNRIRdLatz23o-Pi70R2vAvD6BISSn8smbwrVZcAvB9rQE1SGFNoSh2NAtcwuj1Vwz6Fge75OuUb1w2YfMhSquX_KvzK6g46ZnAODCcGYoF1ZMdPfRI4DDc7ZHRHt_x2FpKV8kJ5Zparsy1B1-29Nc1r5GcvL0OxnIEtBVIdJL81NUbFmgi-hBnhOv3X_wY_MukPtXUhSdZiSx20ylBIHJIU7jb-3oZF07m5sNBBO4hZGCyq9Kzlb3VgMLYUkHqMANfFptUecIvBfQIzmEYYHxBsdq96Ko2cOTOCprTgG_QWZBU01c8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsDCx4FqAtJ_vctJ-YwD61GErXnVpSft77a3sxSJBaZnsn2z6eTWnQ0lROx8WEEpP1Pyd9w-nWrpNQfFMAb3WVCRpRokLsauUJHXuSymRrkRksFVWCveDQwgkE4k-zNb3Jem2scrKw-sSD7HskAlRSkQw2GNMVRXN7sFGOXp7r0KYio7cavdVxrry3S8I5aBLSBXK8xSYOC5zdC1af1n7BLRG8z-nGyDl6DZiY43iyVOxkGFUM_AbbiSx7ffLTRgZh3EQLVaO7KUJ3RuxJpxncbiG73lKeNaoXDWmn_D3Q3wnH_LF4qoJFt_EHQw2uKaWa4sSj_VOuEzqgYCfcVkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=UJtEbbCMVV4pnLJHWcxAtpHBtZrm1ULySgtCNuCCDPyxW6eSQlZBw2SWvLmbfJgXh5OiO8rcblGz3Qahd1LagCzfMNGV-mnb-W57xEd1YbCkIypdNyL3bUStU3P8TiXppsrrXII57kPAjknLA_W270xs_8IKh6JcMi2Y2K18GrGBvPt8TsI0rPpMId5nPZVckEOQYE0aFagFl9sC4woUGRtp5aIvroMRkdVb4wB4AIQSQGv-w2di7m6lajoUZRP8qYfVa6GanOtWFyEuUBVGS0x69d6fuzp_0bfEX3A5A2LrCfYH52I-1ASVGTBoXq7izznlgknyLAtyxd4zoYxSMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=UJtEbbCMVV4pnLJHWcxAtpHBtZrm1ULySgtCNuCCDPyxW6eSQlZBw2SWvLmbfJgXh5OiO8rcblGz3Qahd1LagCzfMNGV-mnb-W57xEd1YbCkIypdNyL3bUStU3P8TiXppsrrXII57kPAjknLA_W270xs_8IKh6JcMi2Y2K18GrGBvPt8TsI0rPpMId5nPZVckEOQYE0aFagFl9sC4woUGRtp5aIvroMRkdVb4wB4AIQSQGv-w2di7m6lajoUZRP8qYfVa6GanOtWFyEuUBVGS0x69d6fuzp_0bfEX3A5A2LrCfYH52I-1ASVGTBoXq7izznlgknyLAtyxd4zoYxSMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoCQoHrl4OAQFqbYotlNBtW5uil4LG_XebzanUr1TSfMDZbbLJ1ynRFfwByh1mYgAjW8TEC6-E6KVlfAj-9vgC9WJg0xW1zXvBpTY7YEhGGqsGNQEm4D1zDFbS694KvkD7W7TKQ3i8Jg27KJTpIyXrj_sBNKV0QY7FH8XzzlVWukedZhTsmwPKwQ3wc116SDM38Gk7bSRONQSxbHdRs4hn0lMPHDUuE8mAPFrY-hZMp-IS0b0Kyd_Mjrdy-OnIslbEF8wRv017idqpQ6fXiTvZE5rIObj9wKW37YGJ6ET9_CZy2tlmd7oSqDaAGO4a8BjU2b2bKEyyvaM8fXqNR_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH4_DArWWSU0TtDntSmv9iQDKy33c0XGSAqdT6G5ii2QAE9iOGfksORqAdLwNmiALhyDo5kK64QgVBaHDqBAyMCvLpxalSk875BlERcQ6bhy4x9vyE1xHVMbyf9t0aILbj65pMhHVuv9AFwDlR9eb0bFZx97mxlAPEwy8yAyWHu1bMah7mz5Tj-Akb1SvFW9mUyBLO6DKdmeo2895Uf9cwK5_e2UduowpDzr8LdMZsdWXOEXMAgvZinItU1BS9f-jq6olmDmiwvrabdLel7hu-cKAZ9mskbPE5DMDinRBArLCckq5tu1YdAtfrSd7MKqQtcNDKqsUMz4H1T0DyNa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=bV3renZUiyhm2H9ojKQn_N1geQ9WKqq2v3L8wA1D5nLx9D0ej9__TVL8j95ocmh0qQckU5WvTmzO0OCXvkhkHY0mN0K53K7D-9eE1hQ1m1G2Qj0tQC2Y8qrmSlxG5MgQqXQPNj10BKDB9WS4Z5E2UAZpYZdPJhd5zMChrtaDHoks2LhTM3UCQr5sqsbKuJm7ME07Mscb31mYHsm5XlnMiD8P-QlvcTN3nC67m47abV62bCtRRoFQNj5WrPzp21ig1Tq02MhCgWodQHOLHlGImBjvMXwmNYDGr5xKnNleDBV9WHX7F6kip1r_buJZBYniuW1t7btczCPNpnKRzoEhd5tdjwoF6lJpS1KtvIqThFyNu4HaIo9lm4DOLnEKtIT2adn8LwChvoes4jk8qwCxfuekyhL79utrFs0QEHkNRB38xsLBr-m6pxu7upwxV0VYFvSFHWgeZavzRVXtiWIOnfArINaKtR1MM_R8RIGsXqMIrv4JQ5GpetHVpB2NBUH9fI_H0VSKINCWZh5SUzug6tKvO4ImbfIU6R-RPK4Pd-UgAr8GXXt4NqHXHGMeDSifrrobcVo95cI50x1tcq-yUhLrqHDBifos4cI_x5JXyaNvCeUTrAu80iC9M1_ONqh27lIuHCXK_m-FzI5gmAspBDBKDm6BeR6aIHC9430dQ7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=bV3renZUiyhm2H9ojKQn_N1geQ9WKqq2v3L8wA1D5nLx9D0ej9__TVL8j95ocmh0qQckU5WvTmzO0OCXvkhkHY0mN0K53K7D-9eE1hQ1m1G2Qj0tQC2Y8qrmSlxG5MgQqXQPNj10BKDB9WS4Z5E2UAZpYZdPJhd5zMChrtaDHoks2LhTM3UCQr5sqsbKuJm7ME07Mscb31mYHsm5XlnMiD8P-QlvcTN3nC67m47abV62bCtRRoFQNj5WrPzp21ig1Tq02MhCgWodQHOLHlGImBjvMXwmNYDGr5xKnNleDBV9WHX7F6kip1r_buJZBYniuW1t7btczCPNpnKRzoEhd5tdjwoF6lJpS1KtvIqThFyNu4HaIo9lm4DOLnEKtIT2adn8LwChvoes4jk8qwCxfuekyhL79utrFs0QEHkNRB38xsLBr-m6pxu7upwxV0VYFvSFHWgeZavzRVXtiWIOnfArINaKtR1MM_R8RIGsXqMIrv4JQ5GpetHVpB2NBUH9fI_H0VSKINCWZh5SUzug6tKvO4ImbfIU6R-RPK4Pd-UgAr8GXXt4NqHXHGMeDSifrrobcVo95cI50x1tcq-yUhLrqHDBifos4cI_x5JXyaNvCeUTrAu80iC9M1_ONqh27lIuHCXK_m-FzI5gmAspBDBKDm6BeR6aIHC9430dQ7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=eVl_RtJW7hdBXWyqdINmBq9_gPBPGwRt22P_meIGlVywPvIYioPyXSPgJusIRtLINbQYjWfKvoGUbNQPonfEBEw_nq6zFYjNd_RZgORFHWpfHIqwn-HUHuRdEdqwVkwYpd4StDdeVNQPzFOQS_s10uygr4f-wtcG5kzfzvp82k5pJUzYZtNc5jMKkQ_WAfy5G_0W292joB5TZAS0JpaY31W7eJHGEuYKXaJPk_ueIllVORH_eWRfQmOphYsdsw4gaf-4g3PH7BXw2YUwZ5qVlQipxhjjn1dMnm_IjxiItMrvAKSHvLnRoc6QZd31k5KquhC1XZrqoLR4F9Tz5GqAojIHp0KWUn1cImx45pCd62Zp5X21605MdUbapORyX6UgS9NrqTolnbiNEGfpEfCvxDfZ6Iz7lIas6Z81ECtqRxsdDndp5MlgUgifdwAXXeEBmrTuxlwhU1ODolj3aEc-YHBlPPlBjquiX4QYoVUZygah1WG_34XdcdJQKYw_ekN8iurscNH7RaxUAHPIweF_Kd4-sbsfIx3fqCg095wE3ti9_9gIh2nocqgNj_EWOGexeJgrzKPyPbTtMvcKSBGdbRviXF1yykJ_3JuHhZ3nk7JKzngP5eU4viQ1RKjnHi6Onh1ZJogEz7fShSsWhZdhmhYVaKl_wXjKFMBk4EQRDyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=eVl_RtJW7hdBXWyqdINmBq9_gPBPGwRt22P_meIGlVywPvIYioPyXSPgJusIRtLINbQYjWfKvoGUbNQPonfEBEw_nq6zFYjNd_RZgORFHWpfHIqwn-HUHuRdEdqwVkwYpd4StDdeVNQPzFOQS_s10uygr4f-wtcG5kzfzvp82k5pJUzYZtNc5jMKkQ_WAfy5G_0W292joB5TZAS0JpaY31W7eJHGEuYKXaJPk_ueIllVORH_eWRfQmOphYsdsw4gaf-4g3PH7BXw2YUwZ5qVlQipxhjjn1dMnm_IjxiItMrvAKSHvLnRoc6QZd31k5KquhC1XZrqoLR4F9Tz5GqAojIHp0KWUn1cImx45pCd62Zp5X21605MdUbapORyX6UgS9NrqTolnbiNEGfpEfCvxDfZ6Iz7lIas6Z81ECtqRxsdDndp5MlgUgifdwAXXeEBmrTuxlwhU1ODolj3aEc-YHBlPPlBjquiX4QYoVUZygah1WG_34XdcdJQKYw_ekN8iurscNH7RaxUAHPIweF_Kd4-sbsfIx3fqCg095wE3ti9_9gIh2nocqgNj_EWOGexeJgrzKPyPbTtMvcKSBGdbRviXF1yykJ_3JuHhZ3nk7JKzngP5eU4viQ1RKjnHi6Onh1ZJogEz7fShSsWhZdhmhYVaKl_wXjKFMBk4EQRDyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=moLw-coatruyXaXnXbwc0vKQ0I7aN3cV3ag0dbduxh4y0h0fRYD0radWtaFXIWM66gHUYEF7xhhF-IywdpOx0tozkfftdnhKjHvo73lnJs3gOACUNBZr91dIt_SgJvZLUjPIH-GwP7TS2RF9pAi3ZTJG9xBTKDyLPyOkoCQs_7ZC4jqaQzi80JWfijMrD4b-Qm35TI9FSPZ9mU9TTj1mh__-Tt93gnpchpaxUbGWT2UnAmf6K0dVMvwxCtY2vdF8Fcdsu_2aRxVXPuqDo6lfaN7GBbi6OE7f3S1ea63Fn-cqoiSSGC_oybo__2wKfmWzH9eDlWgGto-yHvfKoy6orw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=moLw-coatruyXaXnXbwc0vKQ0I7aN3cV3ag0dbduxh4y0h0fRYD0radWtaFXIWM66gHUYEF7xhhF-IywdpOx0tozkfftdnhKjHvo73lnJs3gOACUNBZr91dIt_SgJvZLUjPIH-GwP7TS2RF9pAi3ZTJG9xBTKDyLPyOkoCQs_7ZC4jqaQzi80JWfijMrD4b-Qm35TI9FSPZ9mU9TTj1mh__-Tt93gnpchpaxUbGWT2UnAmf6K0dVMvwxCtY2vdF8Fcdsu_2aRxVXPuqDo6lfaN7GBbi6OE7f3S1ea63Fn-cqoiSSGC_oybo__2wKfmWzH9eDlWgGto-yHvfKoy6orw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw2379K3ogCe-ErBsL-KWoEcNJAitwwhDKyCYeOUUZ6ZAG8vA5gMsrd4Ggxohq1F8CUFGGUA-uhX85W2fBzkzrJ4MIZ3g7tQHhWyxaBIvzlBuIr8eOrehIfPnE-0MRKSMsvag7mCn50oB2NKwAbIjEkRVc0QI4zLHLNhv2zAijKd1ukQ4dBzZaB6gl7JYvXT3WeiVsPX-xmn7DeAlfuIdc2fuNtzhjwJrzoeZnYwM0BZL17FJyWKARc1OegDEaTucuVC6Wp-i-IOpZ59vqaO32R2VAsuYMfedpHlQpFrZokiN7QTylEuAKc_nSK2bkrnKUhiDS2K9SD4kZgYpBx25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=G86speHTXDuUtYHKyCNipkcSiFknAc-I1uW0_bmWTvMq5rXUHBeG--lRv239nDaxv1KR9Rw3y-2G3yghVS512aSxX8MFn4Bn0aXAqvfnHGgJuU9innrg45x7vKpa6BnmVkl6DTOagOFQvQYZYNp-boT3xtsv_mhFuR7AozSusM3VyPfiNj-CgiCfVX-slKQy1aW2p8KRwzSqb5UTbrfepeqPjfYo76wCIvESD36gA7m-fNQrYKvAYxpyYEvD1XSwVLQvyrty7SLvl0iLr4UgCgxKGU6kMBHZdznqbBgZmkQMd7LPpZZEZ6B8UHzl4UuYJkVvkcQLomQMAMDladtDvDc8ySy45qm8JD1wjW2OCd1OUUNct0gTn3AKbsIL21LDsZteISlbup-QltkgUSNo7DjgothbPKXeWqPvqcgmBiS4vVmPOVRbk5R5srYdmxHE7LIG_c8V5jvpkFugjo-Cp5Y_19Ujsia55hmAbBQ_PnVPZ_Q4QlZyNHwZJPvG7FmKzQJmssLd8vWCVzF-IUYIWhj0lvPckEzHdkHbD9ljipxlk5CumbNPhupCzbGq6JvBKsOEj8UUieToOyNUd6dbHsIDK2FoEi-KgkKD7qv1kGzw1wrytbDRYXOhpBgWmzai5AlNc4RPUCU80bH6knRY4Tn4bGlhrrw6-scSw7MBMkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=G86speHTXDuUtYHKyCNipkcSiFknAc-I1uW0_bmWTvMq5rXUHBeG--lRv239nDaxv1KR9Rw3y-2G3yghVS512aSxX8MFn4Bn0aXAqvfnHGgJuU9innrg45x7vKpa6BnmVkl6DTOagOFQvQYZYNp-boT3xtsv_mhFuR7AozSusM3VyPfiNj-CgiCfVX-slKQy1aW2p8KRwzSqb5UTbrfepeqPjfYo76wCIvESD36gA7m-fNQrYKvAYxpyYEvD1XSwVLQvyrty7SLvl0iLr4UgCgxKGU6kMBHZdznqbBgZmkQMd7LPpZZEZ6B8UHzl4UuYJkVvkcQLomQMAMDladtDvDc8ySy45qm8JD1wjW2OCd1OUUNct0gTn3AKbsIL21LDsZteISlbup-QltkgUSNo7DjgothbPKXeWqPvqcgmBiS4vVmPOVRbk5R5srYdmxHE7LIG_c8V5jvpkFugjo-Cp5Y_19Ujsia55hmAbBQ_PnVPZ_Q4QlZyNHwZJPvG7FmKzQJmssLd8vWCVzF-IUYIWhj0lvPckEzHdkHbD9ljipxlk5CumbNPhupCzbGq6JvBKsOEj8UUieToOyNUd6dbHsIDK2FoEi-KgkKD7qv1kGzw1wrytbDRYXOhpBgWmzai5AlNc4RPUCU80bH6knRY4Tn4bGlhrrw6-scSw7MBMkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Ai2DjXcWbkkNMiUIA7rrL07TlmbdapsGJbmTH02O6Nbz_sbqrLQ-CNBJbMQup0n7ij9Yx9JqEwgcG-3Loe8ztSjRO8GafL7QFkBRr3a6IR5A-9T86j_I07EU56apVEkyna0sjAoqznnz836GWeHbLTQbwOV5LfjJi2EJEzLPpBR6XM3IzFSPQmOece2xyGqVU_BFHb1-PAGBSGH69kuaQPwVqZCw-pL1B0fEsvUeYHvI-bDT6q39JkpdxJtLPEqNfdJ2ZJLYLu38YWK8p7Fn61dsZIxONhF5D5DySdrXPbh9JiOMuS1-aOmDDVU1aP7g6vI5T-7Le2H6RgcnbFo1yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Ai2DjXcWbkkNMiUIA7rrL07TlmbdapsGJbmTH02O6Nbz_sbqrLQ-CNBJbMQup0n7ij9Yx9JqEwgcG-3Loe8ztSjRO8GafL7QFkBRr3a6IR5A-9T86j_I07EU56apVEkyna0sjAoqznnz836GWeHbLTQbwOV5LfjJi2EJEzLPpBR6XM3IzFSPQmOece2xyGqVU_BFHb1-PAGBSGH69kuaQPwVqZCw-pL1B0fEsvUeYHvI-bDT6q39JkpdxJtLPEqNfdJ2ZJLYLu38YWK8p7Fn61dsZIxONhF5D5DySdrXPbh9JiOMuS1-aOmDDVU1aP7g6vI5T-7Le2H6RgcnbFo1yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKWNfLPZc-b63dOsISNMzfqjFIIRqOBdxvzjcJY8-UqpeABIU0Cj60xez1A5WYCWhbas50BZVTW4HUP5MlAunQxgwWbiUQwK7nNwvtQIxFtuNJvp3XPp7_eJhzqYSuZNQeT-yBjjd7WZVEEHhMevO7bzb2LSiTS2-kERrU2ISqdYeKKw0NpivATGp97DjuS0QoWPeks84YcUMRLoFy9WeLZgpqVySK3uay-f2XfrCIx1sNCvEiObdPQP93vcHhDUhCcvM1vKuAYg5ojMLDQY0_Xz5GogwUZj16ajnNIvnYVbQCLPk7A8N-QcIm8Jk7XrL07SMpg2Dh1_a3YqVNUNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfh7Q4MmB54DY53RxCAhkgbBnjOTbWrsM792UTQqsjHH96xP8NlzmDkc-8WcSjYGT3jqdfMJax41SNHuEcaRv7_LdGS1SeCCaEhuT3P69qE-nMZpSYJSroeCdr5Mpip46Bmllni6GS3GXCcTpLu-wtGN1MoJFadsbTmFx1Fil5PgsTDcgtBvzKT4-dv1vQawrhV0PQ1GZZlnufVaIYe4oOmt3nT4biguy2Pec4k2u4XuPWxC4vLKm9p-amYkDvq5Nntp5JvjkT6_9PETdxmNosfMirmFLWDGoXzsZBvzcqUU_aemaD6JZt9ULs7yUEW8DbFHIKDWZCiAPd3-JO20QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFmc9rWAX8Vej479O-YlmRct9fT-AghtLdmyeTMslPspocK892TxYsjGo3P66UqhN1R_mUNgZLymQDqUCJaqyeueGgpej_7lwtoiMgegzQnm3yP6p0kfU6met0bY4vUjLlgRtXO5-okMc-afQfhIwpOy9ZMci7cxa6RDXzrBNXNONXb_QxMkdpAFq6HP_NYf_4bVLGDI0dVRBLU4obps_-RigC8fqmUYNBYs9umCCVPNvprfdZJ0W69BWBeO07txUonxYbh-za4VKc-gKU30394mv4l5d18qo4TacQbkCnb7heeH0RXWHcR0bHsIllR8B-5RGzaxVNbaok0BQVltTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jrw6XRRcHTpTObQYgzRU9SzuDAuOLUjJXcr523l-SncNt9pCbwBonoEEbFAvcuGeoGv8UekJPw8uuYPlnKxD6aa0KIFUxh27QQbJ2-zyWOfqU9ukG_oy8HYaiCfXIQ22OIVnaD9blIndX9BrheeEO74RI8Eh7u-mFHgSXbvDBS-1uH9qmPI3ZIWO_ob05dYsmvQ7O4-7hz9HPbzj_yH6ESMTrEaIr4V3ycpw6tua7X5baQ0DMyOH-5HOKxD8MMYBJlSN7EWG_jQkhFU2X_Hz5Z6WmWov2GwqWUppTWjKuTsSSEkh3cYG-QTzJWwxjA7KBsk3s3aXlJX_E2zYKJ73tKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7Jrw6XRRcHTpTObQYgzRU9SzuDAuOLUjJXcr523l-SncNt9pCbwBonoEEbFAvcuGeoGv8UekJPw8uuYPlnKxD6aa0KIFUxh27QQbJ2-zyWOfqU9ukG_oy8HYaiCfXIQ22OIVnaD9blIndX9BrheeEO74RI8Eh7u-mFHgSXbvDBS-1uH9qmPI3ZIWO_ob05dYsmvQ7O4-7hz9HPbzj_yH6ESMTrEaIr4V3ycpw6tua7X5baQ0DMyOH-5HOKxD8MMYBJlSN7EWG_jQkhFU2X_Hz5Z6WmWov2GwqWUppTWjKuTsSSEkh3cYG-QTzJWwxjA7KBsk3s3aXlJX_E2zYKJ73tKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR_R6nhU829tQtY7ehhe1rkhlaB42-2ryg-PrS3OemMaVLwBvWKg_XSVO1IpZ5_qQVKdJAxKwpV6fwTASVtI2cFrLnURcb45rGPsPsk95R_YyKD2VZExXltw5qAba0BwFAewTnec0CMhaAri3O3NqBcXY3jB6Ucuu8Oe6vRDDGKkwjdkDntukplG_jtu8B2VqbvZEjNUgLSt3dDE8lNltHgxD4BSZsRytYN51UVIZnxZl-eg_1UNETUYIp-ZzNHiPl1dAXHJMvUlxZ_b3Q-WeJThUoKYXIM3EX3k3qN_sBpxN8MXCLfZCE_0xQchCQfV6YTuOY4-DrZ6BIhJwgeBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=J1eIyjvNIZYY5ufmU7mlvnWesfIx7mMAsXp_eYjXN4byUZ9J8wvc1W-5qQxPtkwvyyQu_nO0OL6DKOVZRZrEbnQ-bbHzpHg-m7J-at5NRfDEJMkUFWCp22d-hKqxV5krauLbG8KTtchb5azIgOtAGFI6i1_VR-A4ML75Qeu2-XLkGF6rIN5L2_bmIFzJTLK1FCw7mPMbiCp0U3ERPiNyed6tDYDJv-6zQFzH6A-ksQ3E3GL17kRvrBYtTEQ43leIMrJzvoLyY_IVnevXsPH_JgBZExOIfMlEXnsCphxfti6BCL5BGZfKPQsSE2xw6EgjDPVh3VA-aY5f9PXUBb9zOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=J1eIyjvNIZYY5ufmU7mlvnWesfIx7mMAsXp_eYjXN4byUZ9J8wvc1W-5qQxPtkwvyyQu_nO0OL6DKOVZRZrEbnQ-bbHzpHg-m7J-at5NRfDEJMkUFWCp22d-hKqxV5krauLbG8KTtchb5azIgOtAGFI6i1_VR-A4ML75Qeu2-XLkGF6rIN5L2_bmIFzJTLK1FCw7mPMbiCp0U3ERPiNyed6tDYDJv-6zQFzH6A-ksQ3E3GL17kRvrBYtTEQ43leIMrJzvoLyY_IVnevXsPH_JgBZExOIfMlEXnsCphxfti6BCL5BGZfKPQsSE2xw6EgjDPVh3VA-aY5f9PXUBb9zOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=DkuN_RDRLwE-tU3kdANi5wmw1APlZWveXxrJnapznYXM1UCga4AFSnEGYUSICgZQvgmWJnNCm3eAFSAEGI01lw9jAylcpbl6VvCfzXhlQMmVhLq9QkqOCMXYExDMygP76OEyvfjytERhRcbrljNKPQ-BlhkylGobXcPlLyZ73goYBOt3TooAcVpwh91g3uDVw38OJZuIFMDtfqTxpGcQorETgOKdqyWSUAc50vN-CalPyZpvYk-kRIPXaF_aUhypgYTJ1c7yVro9KcfSFeygO958n7rdKB2Fi5lnIQKoD5ythfZNoPA2jzkKMau5thXH_qvSYOwgSOYrzqBckLja5SKBf99Ac_MiXc6PZt_ebHo7NLLkUhMslwuT4mrW4ohWvf3V_vYoY-RXEXQt_tHrFCli19lSpddrJDk6bCbPE31i7S7WkFdd4Ws1TVqZMHi6vL8yMtiyUf3YhjaepIgErw6dXsbkE65mA8rEHp3FKuBIbpJG3BoqvpozQKgJV-dKqzPsEtEJZYmF0j5Z-dXnFnBBQgfftUTMzBI9dVSoAiCE1ylfQrnQAjFuy7Cxb6PGteMDfbMY8j-FIm8RdfXtCQAMMZI8OGPRZ2HOD_hDCpZ6ve8SLGfOMxEqF4U7tOb6TwCzL9cCratqBnF3xQ5BEmKXq9z_jZXtqyuUt5fe_yU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=DkuN_RDRLwE-tU3kdANi5wmw1APlZWveXxrJnapznYXM1UCga4AFSnEGYUSICgZQvgmWJnNCm3eAFSAEGI01lw9jAylcpbl6VvCfzXhlQMmVhLq9QkqOCMXYExDMygP76OEyvfjytERhRcbrljNKPQ-BlhkylGobXcPlLyZ73goYBOt3TooAcVpwh91g3uDVw38OJZuIFMDtfqTxpGcQorETgOKdqyWSUAc50vN-CalPyZpvYk-kRIPXaF_aUhypgYTJ1c7yVro9KcfSFeygO958n7rdKB2Fi5lnIQKoD5ythfZNoPA2jzkKMau5thXH_qvSYOwgSOYrzqBckLja5SKBf99Ac_MiXc6PZt_ebHo7NLLkUhMslwuT4mrW4ohWvf3V_vYoY-RXEXQt_tHrFCli19lSpddrJDk6bCbPE31i7S7WkFdd4Ws1TVqZMHi6vL8yMtiyUf3YhjaepIgErw6dXsbkE65mA8rEHp3FKuBIbpJG3BoqvpozQKgJV-dKqzPsEtEJZYmF0j5Z-dXnFnBBQgfftUTMzBI9dVSoAiCE1ylfQrnQAjFuy7Cxb6PGteMDfbMY8j-FIm8RdfXtCQAMMZI8OGPRZ2HOD_hDCpZ6ve8SLGfOMxEqF4U7tOb6TwCzL9cCratqBnF3xQ5BEmKXq9z_jZXtqyuUt5fe_yU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=etylGLAtMPLbqx369Yni7AascHPRgj9fA7mjJyad1ySD0Y-D-pMqHvfC4lz2t5lIG1Nu3PaHiKnpcc_mVChsb-bQ0OQFzTaU8WpvxyKWUGk3W0rucMh8wk3Mhc6MCHMnvcNfAcQr9KBQ_s7I5ri-hwVDuf_oC160g8lHKtj0G8N0576ZxjC5uXGBMWEVHnYHg93DMLczaoZn9nmcwOsfGCw8YGRrp-CFFMDOhKgufBbR9YZal_7SU8s-f3N1rS-76Y7cxBdzg6gxNwWD_eIgrMWqRmzrAD2YqozT-xKp17fdHZVK4Q8GgajpEvAgqCNRfRnmfXedX0va5IH7HzoA3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=etylGLAtMPLbqx369Yni7AascHPRgj9fA7mjJyad1ySD0Y-D-pMqHvfC4lz2t5lIG1Nu3PaHiKnpcc_mVChsb-bQ0OQFzTaU8WpvxyKWUGk3W0rucMh8wk3Mhc6MCHMnvcNfAcQr9KBQ_s7I5ri-hwVDuf_oC160g8lHKtj0G8N0576ZxjC5uXGBMWEVHnYHg93DMLczaoZn9nmcwOsfGCw8YGRrp-CFFMDOhKgufBbR9YZal_7SU8s-f3N1rS-76Y7cxBdzg6gxNwWD_eIgrMWqRmzrAD2YqozT-xKp17fdHZVK4Q8GgajpEvAgqCNRfRnmfXedX0va5IH7HzoA3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hs5FUJqg4Q2jzHPaEuoCnkbwCe_2S8RqtYB5z79XBf2eS_wnEM2CWYDz2jvIe_buXVwdn9U-qbOSXGEPBbMR0helkidJNYa1wj1M2m49MqBoWFPkUeOuSdUBZlRDl3D73ldma_Ac0858tSGBYzVKH1PkY2QBPFsTjuWZMFAoBwjcEPqBWBdz2uhWQ5kSYWUike1iSm25YIlHKug_9czW5uiwMlpz5S-2SH8LZOf4ij9o0TViWufYi5yNX0LUAIGKpcKDZDGEc6Ji49-rws4S6oSpXTdEHoqyv5ewiQB7EeZ8AIPSgLUZUKhUd2sw1gvv3D7hKlXY_UB1w1l0GaUOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=uf4erAA5vtZRtzJMh5GImPiv21j0tPxil1WzBmVjxONk4Fjd1WrptEUG2d17SgNgJxDzIuB9C2yzlop930oOLJ6ZgyPFvvR0wZvT1EhzWI_vE1y_g8U9XfxtgxZkHVZIcDWloGQ25S7V7bSzHU7OYZdjegODw450hkAJBhEncuKxt4yh5lQrgEGKBvfQLwhQkIS7EomayuVjN9XEFt0RuvgRwAhNzFnJfCu4qZM9Breo2C3mjcFUb1I21gRQXGGEO74egn0vLOzA9TxKOK5uyLYHjpsNqxvjRdh3xpdV8iVmHsRZOS1-ATXaJhKZ6UZ6CyDEPua3Fhm0wCFys3DIqhzn_eAADD9vneW7hFHS9f9tYZoUjVdxDKkwyhr9jj9Iwf6qTVCmNoKEff4fNqV2GxMDpzm5gDj04q1kvWKU4M1tm0Zqtesh2eci22JumoMWYsxQ-Ss2Dpbr1qG-B2Yyelrkz6vFdt3_uLvi9LfbQO4tMzv7LetbtaRPHtIBoQmBIS8RX9hO97d1Ifm75STKNBwP6kWh5Z1tbxE-u7GKA-mN_V-dwmlkJYlRhRgOOUK1UZTzjzKU6fGn_sZq6PK-N-L5SlPnC1nJ3WApAqLiuf3vpbUR7t6Npdqr-fbZwd27sWQ-hVolwj8rH1pJL8yftriQrJjWHZKCo4sopjh7pv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=uf4erAA5vtZRtzJMh5GImPiv21j0tPxil1WzBmVjxONk4Fjd1WrptEUG2d17SgNgJxDzIuB9C2yzlop930oOLJ6ZgyPFvvR0wZvT1EhzWI_vE1y_g8U9XfxtgxZkHVZIcDWloGQ25S7V7bSzHU7OYZdjegODw450hkAJBhEncuKxt4yh5lQrgEGKBvfQLwhQkIS7EomayuVjN9XEFt0RuvgRwAhNzFnJfCu4qZM9Breo2C3mjcFUb1I21gRQXGGEO74egn0vLOzA9TxKOK5uyLYHjpsNqxvjRdh3xpdV8iVmHsRZOS1-ATXaJhKZ6UZ6CyDEPua3Fhm0wCFys3DIqhzn_eAADD9vneW7hFHS9f9tYZoUjVdxDKkwyhr9jj9Iwf6qTVCmNoKEff4fNqV2GxMDpzm5gDj04q1kvWKU4M1tm0Zqtesh2eci22JumoMWYsxQ-Ss2Dpbr1qG-B2Yyelrkz6vFdt3_uLvi9LfbQO4tMzv7LetbtaRPHtIBoQmBIS8RX9hO97d1Ifm75STKNBwP6kWh5Z1tbxE-u7GKA-mN_V-dwmlkJYlRhRgOOUK1UZTzjzKU6fGn_sZq6PK-N-L5SlPnC1nJ3WApAqLiuf3vpbUR7t6Npdqr-fbZwd27sWQ-hVolwj8rH1pJL8yftriQrJjWHZKCo4sopjh7pv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=izr1HVXHJQvsP29VXGbxyvDQhjVlL1XD4Q8gAPLKZQqKnsxNVrfDYMgxlhSiRS_lS_Pb7zBwD-FQTLdc9K1BcYdyJ4V9IRRlQSw-ZpCXM9eqzMoqjZUNzem-r9drZAJvaRKDsjyn-ztn9_TkBF_3Zy16-lVv9lSZGlg4nf6E95XR3f-uyIeZ9Ic0ETU2WJkhSgSyROogYojsoNIf9qgL1kFtqJ2NbYXwm2i-2kcGLmLOlclMoIkQ7RO_-ttTsa8MbFYs8PuYmFKY9RXVXowHHrLTkUXpWKugLs12htqiPGLj2mo4IOJhrRm1u0vo0_EYYr5Cw3ZY6upEuhfMxWfqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=izr1HVXHJQvsP29VXGbxyvDQhjVlL1XD4Q8gAPLKZQqKnsxNVrfDYMgxlhSiRS_lS_Pb7zBwD-FQTLdc9K1BcYdyJ4V9IRRlQSw-ZpCXM9eqzMoqjZUNzem-r9drZAJvaRKDsjyn-ztn9_TkBF_3Zy16-lVv9lSZGlg4nf6E95XR3f-uyIeZ9Ic0ETU2WJkhSgSyROogYojsoNIf9qgL1kFtqJ2NbYXwm2i-2kcGLmLOlclMoIkQ7RO_-ttTsa8MbFYs8PuYmFKY9RXVXowHHrLTkUXpWKugLs12htqiPGLj2mo4IOJhrRm1u0vo0_EYYr5Cw3ZY6upEuhfMxWfqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=Nohm0NPzgAWkrdtN0XfPg2S1jJ2v4XAIoPuJhPnetHOxJFI85RDh1ETe_aRYSaTcQtwx4HbnW14LMmY7LLAFqfKeuOqPgOu4jbwn-R4opHGxEQDcguFj78QQ4PgFodE9ugvk1Yl6pxyN2q-_1dJIs20grf7bUMjMyhAWUcxaHsmyskuHfliXuWncbcFkTjA92CMtk6vrQDexiM4SXZsWiWH3SBwcUyp3ygKpDkEWQG89tat3VDDeOpRg3o7YQqm3MeLsRbPHEV8NCkzzgAuWvXr1dyJJAcGj_IhOkhZiCyu9dTTTyaPiQwU57gw7kDP597mqyex9GD6hnjGGNIC0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=Nohm0NPzgAWkrdtN0XfPg2S1jJ2v4XAIoPuJhPnetHOxJFI85RDh1ETe_aRYSaTcQtwx4HbnW14LMmY7LLAFqfKeuOqPgOu4jbwn-R4opHGxEQDcguFj78QQ4PgFodE9ugvk1Yl6pxyN2q-_1dJIs20grf7bUMjMyhAWUcxaHsmyskuHfliXuWncbcFkTjA92CMtk6vrQDexiM4SXZsWiWH3SBwcUyp3ygKpDkEWQG89tat3VDDeOpRg3o7YQqm3MeLsRbPHEV8NCkzzgAuWvXr1dyJJAcGj_IhOkhZiCyu9dTTTyaPiQwU57gw7kDP597mqyex9GD6hnjGGNIC0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGuvLhtMdkk2AqXPWSeI0RDMtKuey0UY8Butug6cXDmzM989BJIspsbWbVUi0XueoRECgLgHRO-a0g40TMpthelCVaUGhUU4W4h40nGAm4aN8GDlobzP913X9FMGm9gIHvusy5XnCGqJGyAIOvxtM8KjycMm5SaC-RluCzKCGfbLcY2IztzgNY7gmuaBzU1SHE-AtZiMo3PZTyrIYZheBz_PqlyRKZKq3sdvV50DgjoUI2xOwpZ0_a-sTUylcNq38XpFZaZVNrSbWpJcshUlXH71bieeU6VuDnLxJTMcu5b_2p6xLfgjZIUQ6dKf8977yBOIMh85XvDCoTWvqtZywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=uwdiCvYNUrQxQcxOgcRpFN0-vZg6GrJefSYKcfrSjKcBmEOSRysqOqG_co2iVXkVrCAdywMmcB4VrM_DTSAgFxIS2QcM46OH05x_rwAxkdDi8XmuYAPt79LAoOvR1XHlxU7f5ZmJOMuDFZEXSLtUpcciWHnlAFpaH2vdAimdUvIoOLM9MWk6pQHShf4YO5oj6XfORv4P52mJsmUsm1t7Pu_Z1qCDpUgQcer37Kpgit31BLQ4ByzuWnsr7JhamMo13cqj9mIdK9fQBUjiPu4Yp9NQjktTwfIdQcCGoq6lGwwj4Qk9VyNi0YqqWIuiXA9O4mzlFAosHuiDdASbqT1jCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=uwdiCvYNUrQxQcxOgcRpFN0-vZg6GrJefSYKcfrSjKcBmEOSRysqOqG_co2iVXkVrCAdywMmcB4VrM_DTSAgFxIS2QcM46OH05x_rwAxkdDi8XmuYAPt79LAoOvR1XHlxU7f5ZmJOMuDFZEXSLtUpcciWHnlAFpaH2vdAimdUvIoOLM9MWk6pQHShf4YO5oj6XfORv4P52mJsmUsm1t7Pu_Z1qCDpUgQcer37Kpgit31BLQ4ByzuWnsr7JhamMo13cqj9mIdK9fQBUjiPu4Yp9NQjktTwfIdQcCGoq6lGwwj4Qk9VyNi0YqqWIuiXA9O4mzlFAosHuiDdASbqT1jCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvGCcrb-wI4ZP3s3LyToHcZRSfPu9q-8N_F6LP1lMxfCreGs23X_4hgWNY-6sRHR0Fno9DZXKVBoGl-dgtO7B46wWUBCsAPEcre2oFZHi-ZBoWF2C2VgCvqIo1J5QcKuHGtZYqPnJQ-6RbXih5UU7FUXUPkncmDbZmf6aNrt8qghBij5k9JlV7G5wkpNibKoO4MBMLPASyBrNEnOuxH8DpesJhrnIXjqMVS-UzMTY0jzJZZ08alM_qL0RG8DBY0XnsznRvPXfVcoCUYIbLJHYRglLwnUcIVWZjayIiH7j7wmIIrw7vL8xkGLdCLWaOPbllAihxtk5mnH7HlwBJA-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=OKr9ZY2KRcdcLSuf9LCDqg0j0EYPvvC4ahvreSUZIJWOV4_9RZj8j75sBLb_OigYzOfnXsKmHGydEHyqC6yI2jIwWGmZpfkmPxGf732qNLwz1GUhl9SQEHGx9mD2jttTPENIuIoR2JDLaOQWSLPTYrCXx_fBqUpRYHFguzg7Ad5BD8m6WFi1acq_hZhiIWTdLKCCOgPd-qKTdXd84Vr-2HkpAvIw0UYZHz3KGrbQIsOYjs2NHgvl0eMTiWR4oIO6Jw-NPd5yzank4ra7Qy335PZY7dsdrltoBqSNu4xycXVEOs5ll0Vq-kgN4fLSWbPg1WpNMA1bVtYS5RuQRemV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=OKr9ZY2KRcdcLSuf9LCDqg0j0EYPvvC4ahvreSUZIJWOV4_9RZj8j75sBLb_OigYzOfnXsKmHGydEHyqC6yI2jIwWGmZpfkmPxGf732qNLwz1GUhl9SQEHGx9mD2jttTPENIuIoR2JDLaOQWSLPTYrCXx_fBqUpRYHFguzg7Ad5BD8m6WFi1acq_hZhiIWTdLKCCOgPd-qKTdXd84Vr-2HkpAvIw0UYZHz3KGrbQIsOYjs2NHgvl0eMTiWR4oIO6Jw-NPd5yzank4ra7Qy335PZY7dsdrltoBqSNu4xycXVEOs5ll0Vq-kgN4fLSWbPg1WpNMA1bVtYS5RuQRemV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuhbUPl-XOZWTYwOtXLpopDn27QO4VBw0DAFvKGVRdfOTbqaguqs2q9RYGD4BnmmK1hMvvbKVwxlDA3VgQRYRkxGkcV81qMTUwvVY0a6xT27LMUSmtTU-jUdvxc3iQQuoaoM7UdofUbqUMXNZ_9l7Ztjgyrm3tp11LuH3yDZ1Gv5ZlJU7rLJEXC64SP0dT1fNK2eKxFtUUOHVu0NgU-JmcYvxWeXyDN178BnUChoiR0h7XvuIlavaymzJXKaDYZkimVu-1aGDh6bqgMXBc1fGxY5Sb-IlTUb__5PYdrTCfw3lVoD_LqA5r9Ab-MSYft_HGldRfRE33ernxTFBpd_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=dKCOsktYMt6rN4nSv1qU5Zu__t4D6CzIvTZz07MjJYDhVg6qrucOb3vuwShEgS9musDliDRjZvDOrs3ckngNYEMmMAwqsbl0kZdOhAK9wMTAiizpasa0_Vn46ZN13mLu_htmABFrE62XUc7Yyxrv8ymI3EdLQemQzS_dHwV0wTRZzGXmT3WL0VZl9aWOjoCQWnMx3PqKTRq7JavzSWR_eF2UxOdP_U2pYjKBmrytDheC-a_pLzIBzNtq3lKP5IzwMrrRPNXP__0XS0IeFJ75FWaAY7aQOTs-pNXlwRbSIaG5m5hOf7YMzZaXm3FUPIynWojkVDqpOrFSY6oyuV3dxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=dKCOsktYMt6rN4nSv1qU5Zu__t4D6CzIvTZz07MjJYDhVg6qrucOb3vuwShEgS9musDliDRjZvDOrs3ckngNYEMmMAwqsbl0kZdOhAK9wMTAiizpasa0_Vn46ZN13mLu_htmABFrE62XUc7Yyxrv8ymI3EdLQemQzS_dHwV0wTRZzGXmT3WL0VZl9aWOjoCQWnMx3PqKTRq7JavzSWR_eF2UxOdP_U2pYjKBmrytDheC-a_pLzIBzNtq3lKP5IzwMrrRPNXP__0XS0IeFJ75FWaAY7aQOTs-pNXlwRbSIaG5m5hOf7YMzZaXm3FUPIynWojkVDqpOrFSY6oyuV3dxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=rYam4AIy8JH-5VHNK3uvXPyDvdMIU3Q64Sanns2Rbpx4GWFveAU1E8SKGgG0OxAS-m1CHx7WgCm_K9bafaZ2PqYudmToHS8Er7VcmwEMzN00-NunRwvTdllWzXop-fCA_4z_iL2fwdi8Jjz3wWsfRI3C_mqZlKnoYoVfFDIqspAlK9R-EffWTmx4dQ7mookGBn2O5clSA0ZmsoUPPZTDHRwR1wX6RlWWmtEDWAmkL0cQuR3hN7IWIGEoIu39X4k5ccjjHBdbiIib7lJPu0-Iqz2TAmXWylzxVtotxk0peIdYo0cszA5MNGxTM3tDHe6OAW4C_C3bjxCpIFl7A6rvrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=rYam4AIy8JH-5VHNK3uvXPyDvdMIU3Q64Sanns2Rbpx4GWFveAU1E8SKGgG0OxAS-m1CHx7WgCm_K9bafaZ2PqYudmToHS8Er7VcmwEMzN00-NunRwvTdllWzXop-fCA_4z_iL2fwdi8Jjz3wWsfRI3C_mqZlKnoYoVfFDIqspAlK9R-EffWTmx4dQ7mookGBn2O5clSA0ZmsoUPPZTDHRwR1wX6RlWWmtEDWAmkL0cQuR3hN7IWIGEoIu39X4k5ccjjHBdbiIib7lJPu0-Iqz2TAmXWylzxVtotxk0peIdYo0cszA5MNGxTM3tDHe6OAW4C_C3bjxCpIFl7A6rvrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJHVr7aaTjLYZ1bY2FZbBnjfnftuYMksupMl3oKDim4X4wdXceUhPWCYto2lbHJwPxrcP3vc5Cdec6t-VQwcvhHmIpIZiSqWysyVgGpaiSuOdSuw9GStOuXumJSliyxaiLfbWGUwFooG2kcqTYk9rC_VUEW9DWZToweQPuylltMFKmEMG9C6O8kVz0M-4pKrGneDuUIz2qqGRf9yQh8Nv7qsllocJIFvcWOaCFcDeJLs-e79K8edauuWJH5wiq_g6sYo1VZVghvHFpQW7C2s7CSTibEiqZYSIrtIqVCxDcr01kSrDMA1zY1W4Xa3zAuBmtSlKV-K5ZDyXcIZSbuQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-ydC2aQZAfneUFHVQhI1PIaCpD9nwyaRwV8zn0VD_HVftkBvuLbfnGW4OhbO2nOVakSlHGbjpYCs2W_5Un6Bp9Hkm8_KYuJE9zAj4oioJEPCSaYwiAoCOr3T9MPDh7FMRrHs_P7OD6kS-VErNejNxpFanc_uf9X6vmJ7ZB9fqZPZCKacarrqqjt7S-hOBwUdKQZL3vEw1VACUsJ9Kgj8JZya6i950f5aAs_0FKdn8ySRZi5k_BMcgxC-_JcX8e7wul7bFEe_pAOt0dpwlNtoHmaWHeMOsf7s2oj5gx8Ze4H1PLejwiBvjEksLvGasZCAFJUl1dULKnVgPcQ5PW4zmnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-ydC2aQZAfneUFHVQhI1PIaCpD9nwyaRwV8zn0VD_HVftkBvuLbfnGW4OhbO2nOVakSlHGbjpYCs2W_5Un6Bp9Hkm8_KYuJE9zAj4oioJEPCSaYwiAoCOr3T9MPDh7FMRrHs_P7OD6kS-VErNejNxpFanc_uf9X6vmJ7ZB9fqZPZCKacarrqqjt7S-hOBwUdKQZL3vEw1VACUsJ9Kgj8JZya6i950f5aAs_0FKdn8ySRZi5k_BMcgxC-_JcX8e7wul7bFEe_pAOt0dpwlNtoHmaWHeMOsf7s2oj5gx8Ze4H1PLejwiBvjEksLvGasZCAFJUl1dULKnVgPcQ5PW4zmnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=FbQDSv4dJ3_xOWBoT4Gp3J8wpBThT2MFgC_qMFa_JWLaKK3Lnxbge4I5GT3FzYXg_rCWTUhLrKmwXY2H5c7w-frwjVstXck9oY4ZpP_SBecs8vHYQGzJHWJ1lUIoOsMgLe8OTG5exLK4efdj2TSeO7hXHDXvrOkEcNlKx6nkOBNoQ0HOijnJcngmIhFQWf4xHTgyZTx5t9HsceGnukEA4deZzAmnlpmCO8vpHEfWZ8D2aCCLOWaUzyJlOVXEWAmAnXvSaiXVXnqiay0V1w3vTTprwhTbCCcLk9XQSILWKEuCglWjLgYrFmEshX5vxHADe85STQuh3GSD8cc2aPs2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=FbQDSv4dJ3_xOWBoT4Gp3J8wpBThT2MFgC_qMFa_JWLaKK3Lnxbge4I5GT3FzYXg_rCWTUhLrKmwXY2H5c7w-frwjVstXck9oY4ZpP_SBecs8vHYQGzJHWJ1lUIoOsMgLe8OTG5exLK4efdj2TSeO7hXHDXvrOkEcNlKx6nkOBNoQ0HOijnJcngmIhFQWf4xHTgyZTx5t9HsceGnukEA4deZzAmnlpmCO8vpHEfWZ8D2aCCLOWaUzyJlOVXEWAmAnXvSaiXVXnqiay0V1w3vTTprwhTbCCcLk9XQSILWKEuCglWjLgYrFmEshX5vxHADe85STQuh3GSD8cc2aPs2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=aCBOdXGNYtKWqBn2u7zfMGvMRUoyd0HHkJLAZNz3oHrBSBQiTxIvuIHwrc0E9DQjGTXHGXZXB_SNG4dgN1xQtecvKmPY276q5gXDxa87vHENGJ0kPWrBi3gDzxYb6RD3BSe8uM0P0Aauefhjrbasrl9pvv2MQQ1Bfm5ITYwlPVU4t4s1PnMN03UqxlGji5uDc2xgT-FmNJrJI_6euKyi2WJYUIlHCORDonqtOHxl0zM8d2rpYhE9RjtxY8BdoXHcMSw9BvVTV5m7ywMsNCvkvL4f0BV8XD_wjtOUrZa3NmekBJStDC1cv_VvP6-3N9yHar2wwLlQV2WzMBfe9AJapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=aCBOdXGNYtKWqBn2u7zfMGvMRUoyd0HHkJLAZNz3oHrBSBQiTxIvuIHwrc0E9DQjGTXHGXZXB_SNG4dgN1xQtecvKmPY276q5gXDxa87vHENGJ0kPWrBi3gDzxYb6RD3BSe8uM0P0Aauefhjrbasrl9pvv2MQQ1Bfm5ITYwlPVU4t4s1PnMN03UqxlGji5uDc2xgT-FmNJrJI_6euKyi2WJYUIlHCORDonqtOHxl0zM8d2rpYhE9RjtxY8BdoXHcMSw9BvVTV5m7ywMsNCvkvL4f0BV8XD_wjtOUrZa3NmekBJStDC1cv_VvP6-3N9yHar2wwLlQV2WzMBfe9AJapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-Zunf7zYlkGBacMqUtmewBTeM69AH26rJQqaBt2puG4EKm9cKnZhnup-g9AWnv-z8mNjZUUuckaURnSX8zVkFFucqc0yxsg8n2MIb864bFdoYxVVVoseU0uMwh_uVpTKjpjmE_ldsf-EtTVD_LBz3gp3y6LnGPNh-gT4tFpmCwq2Yz42fzoAQhBzw4wYwOZZKAnsRYLZ4rvGIIMtJlAtJqQsYNw696YX4Z5JjEn7vn-SiqtuFuSMwCoExYK_I-nnTBHqEk9OMRDR3UpWRbW0Oq8JCnaiLe93e5MduE3DN7pbBQHq9k14knAyGHzHDS3q0x-izAUQODIpixqm55xqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=VaJciIzfu4F5RJpcrvUsiL6F-bWyrYArCTl8_oj44j1GOfuvg-sapie48MiLgLCvEriatJhcQ8r8zUedFQKQtpLxGfxSmC6QGD0AEH1ueR5rlDpZ2lDpM2JLrgao3iRoEeA0IX-53aMM6k9g1Bhs4TQEFmX1hOGLyT4d4WDH0c-hbkrRnr64EIDt0kcmDjN92AWlrZb3ruV4kfX69YXzUnNgeJkdyp96yuQXJGUAarQZL2wlRL2lnqKwGSXzoppqyKFrUI2tkMiKBj2nPCTw5WgAc8Z87aVfjcZwEBlBZNyhI4Gf3JXEvuXwt4xVJMAUJoj73PX6R_1Z06dlhCYrLx2uX2EXYXw73ZszuiPMscGoTu4QRAZJduGa2zjKcirqr6Xb2FPJ5F2V7aqOXxLgJQfLJbQ3NBBAtF5BPZ7auVjyOs4HbordqLGilLJaoN4jzK_Z2GMerkZcflTIebmWPfeeaYYFHfkIgH4Q-fHTbR90eqRvjo78b5dTRUSDUmVSZVqoObwRamMBCiYtizfalhWnJ396_ZRSV4cyjR7o4C_j-3I5v-LS6fKhBEY_YO10OYYP_oLoS-iodX_oBdsuAhGkUicCzcRUr-xLcbIqKGkhfsrmHJMkCe5OIldTc31rR0WcXssg_KSM5_IMP3HhXmdMVqsZkUciTUSzp4E1Tns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=VaJciIzfu4F5RJpcrvUsiL6F-bWyrYArCTl8_oj44j1GOfuvg-sapie48MiLgLCvEriatJhcQ8r8zUedFQKQtpLxGfxSmC6QGD0AEH1ueR5rlDpZ2lDpM2JLrgao3iRoEeA0IX-53aMM6k9g1Bhs4TQEFmX1hOGLyT4d4WDH0c-hbkrRnr64EIDt0kcmDjN92AWlrZb3ruV4kfX69YXzUnNgeJkdyp96yuQXJGUAarQZL2wlRL2lnqKwGSXzoppqyKFrUI2tkMiKBj2nPCTw5WgAc8Z87aVfjcZwEBlBZNyhI4Gf3JXEvuXwt4xVJMAUJoj73PX6R_1Z06dlhCYrLx2uX2EXYXw73ZszuiPMscGoTu4QRAZJduGa2zjKcirqr6Xb2FPJ5F2V7aqOXxLgJQfLJbQ3NBBAtF5BPZ7auVjyOs4HbordqLGilLJaoN4jzK_Z2GMerkZcflTIebmWPfeeaYYFHfkIgH4Q-fHTbR90eqRvjo78b5dTRUSDUmVSZVqoObwRamMBCiYtizfalhWnJ396_ZRSV4cyjR7o4C_j-3I5v-LS6fKhBEY_YO10OYYP_oLoS-iodX_oBdsuAhGkUicCzcRUr-xLcbIqKGkhfsrmHJMkCe5OIldTc31rR0WcXssg_KSM5_IMP3HhXmdMVqsZkUciTUSzp4E1Tns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6FI3msXQt5Gqi1WOgzKferS1S1maRwOj9xnhwI9fiF0P3orWmtRCZ-rPHd9cNjVdCDjwRecfoYA0FsWki50uumKGqAuRe-coYofuRGqmxAnpQcS8lAWPOhbeO5rQOGoIvgPTYs2zOWRNhdvXWw6fM83fSZkdlH4foiyQr53JbR4G0FrV02c3oU8cLWmuRCX5omCWKHurZ01OJJ-7nrosln_hS0Etn9FK0mUsUEAMIhdUfHXXcvsfLGd9NJjBlQ9ZSTnyv1srOuGQwGmPYx7EXZJw4ZDCLk7tU5SUWvnLvAbD7wfxmAuKLGIPr2_HQSTsVIgSyYS_SsO67d4Bct2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=JGLNqcWg_A9EuGpN5Db6o31PeQtGftGFWRQ8PvyJ6cpUiLy-egGXJ6zkVbRx25u9aqWKsDCpq0knZOfocKQxNsLsaGk3x-FW1SQEm87ISPMfjFCdS6OCJrLmqZbn5eUvaBGunENTR6hMHwyzX6f64ILBk3kB03jEg7_G59P_7vf3BuYgzvcAJgz0GX3bv6UCR4PvNJoBawf-UELGYMp3sqKEQoyGxjn0rfFnc1_g8nMGqW74EdiPyEtJhvqhu6Rp7n89vQ6YxCK28jV5PIsOvbWCWRFbr17V3mVU6CStLGlkzC_7tpXdD0ep5SP0YKKKhAl7BFRPjRfRuVnIZVzbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=JGLNqcWg_A9EuGpN5Db6o31PeQtGftGFWRQ8PvyJ6cpUiLy-egGXJ6zkVbRx25u9aqWKsDCpq0knZOfocKQxNsLsaGk3x-FW1SQEm87ISPMfjFCdS6OCJrLmqZbn5eUvaBGunENTR6hMHwyzX6f64ILBk3kB03jEg7_G59P_7vf3BuYgzvcAJgz0GX3bv6UCR4PvNJoBawf-UELGYMp3sqKEQoyGxjn0rfFnc1_g8nMGqW74EdiPyEtJhvqhu6Rp7n89vQ6YxCK28jV5PIsOvbWCWRFbr17V3mVU6CStLGlkzC_7tpXdD0ep5SP0YKKKhAl7BFRPjRfRuVnIZVzbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0aQRH7m9Y7UEfoYjdqYgRvJh_OIp-UWP-tW5Xvpdtll9WktDO5HTS-NHpro-urGhzzW0YeiFIjsnuCQ7kf9Wt8k4lLjnuqH-ZOveKPOpbIihm10Y7mBdtZnHxOE6NRzG5PdIYy7RUXxRN7zJgB8JmFYSqz6sfAHqUA5slo_F0vlwgqo3CxmPZPo7FQ1JtolWIEHIeFC7nIn1dZBZ6lsxav6OQ_vqdWXQXgOKfVgsBX7urF3PBM1fx_ObuLQh-x5mV-ImlqXBUJrn-F-7x75G3cUZR6zsv8eOZMge9-c1rrXpAmf2KZeolyrco6OfSSacJ7wX_2S4Me35ghH2dQV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
