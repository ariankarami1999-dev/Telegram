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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 11:07:53</div>
<hr>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaR9NCTrwfD3vNOBPEV_S02tSUAQxGTHYsaGqTZe8cxl3XZbk6-NYz9zE-j6TFbqoxXv4HH2e7VCHv88NCoIaAFhhf6afjvkUnMhtaos6_FaGu0E9qYBfZdAxwBL0Q_ffvrCzzWZmpOokMqfNNk1QArR4ja7PYyqgsghhU14YdlLRay263UIv85n1mSM-JY2k8eUKV1DEH3gpxS6vfrU1ljhrO1c7lHjmoqzCWRnc6AkVi5Vud_EiBR5HYC0_54Y9Go8yRMPJJ2swZ8500mFr45cUI7Zgu-7YnoG9dvg4MW0nscGvycALwwT_929FBdwfUGUPLOs4kHg6VnpQ7rdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZiXrTQ7SbWFTYGt-ISF50z8dQUcWY13qDeYiPD2ddmdAS-WAnfIqxtm_f8K_z0BXWF0jU1K7dQU-_35j37WAlPoIBqn-I7xhBv2A2uFes3oWutiTahuNH7M-ou9bkSb-xbubaCy3faxnVzMsdMnXk7mVB_0AuEeM2C1IP_rvXKqaqSGZo__TIVSBFSH8dj9eUIomA37Xfm8TlS4wnjPzQWqp0Yvvy2jcEyXfIUZal3Qu5vklyVFOnGqDx22Q6V1D4xdtTVNWW4jZSGwqtxunPoP83AlHCSTxp85GpuM_P1VDnRJtXBUYfDMyHfE0HdsaNOFQ8yJSUx1_iwtmJotrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Z7H6AxPLkyH08Qs4N309MhQcJ-cfZczl-6AnA7GxAz2qm_AGmdBIHTqAucXON4WqK4aACb3gabC9cmvlX2PnzjO2550JDIkKGrb3OlPNXyRkD2tqBdU5eXp9ON-jv8w3bM7ALNaGiJ3KIUK8X0vodjwcT1JCl7fPkG23hQBA2k0lATISQGAIhXLRQzNQVYnTF99k4uwg7Wt98RiHwGO6GMHydnNfgcKnWnYEuSVBuBQFKL7T1gkWxRWL2lkBaI0Ny9FwFJOynrWsSfiMK1tuWxODNhMK_0ajpYZu02CE32yiVS_Ftg4EVi3SCoUcI0cajLTH8rNRikZU6CJRL4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTKEs0y4J_GsjRjOZY7AbzmvKlAy6uPOMFYRmW1lPTvJlgCJ3Jvtw9pqngLfwOXScTksFiSJPZc6imgv0vrD0BuM1beog2zL3YNHkDB9qpUPddpfqOB_R8fKKZWNb4YyCmWBufZdhWpS6-LmD90ypwcVjm-3X46AIMW8a043GLONKStysH-AnNhshpxb9rWSxafzpE3JhxBQqmvnf0-M4gKETMpweTmdnAi0TSRAROtLoHU7rCQMDKLE3mEZMnOUxoLABN2Qetls8jyBjaCim8G7CuYvJjBOX8HhQLjYkFVJhnWXqKBGpcEZg5MWFPUXBySPpB5dtQER_cz_Jdq7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9LuuOXkJJJ11GtRZ9pNp1zF4kdbQHHlGLDop6TDMS7y97g8_HSOOhVpyy1MsmJKocbNFTnDDXn7f5imiuMb4MoFiCm9Ei2UBSB_mkQLJNhf_f1d6eaA9K54shcZwqCCGjhyzl-4PASTS43QNJ1sUFZWe5GOKi3k1j2pDkJdRzzpgogM6eXbhla0b7rBsovEBbA0qS-FVF3rQw4Hjlb8iB075ez5448hzCZwDLqdYPFL3ubjs4UfA3PhOqxQCK8ImOjwEaraC3a7d-CXgRZU35UWxotshIt3xFvFatUgDx3U9nl8iwFMmkFvMem_3GJGR3Toetms_y7fB_m113PvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpsNwdaI1wtVtUZ57QVA3lvZGIz6WHe65DguMKLAMGxqeS82_D9buHOkGNlt4pvj43PlboyszGk22FZLkKqPgrLR8p9ya5gWNG1d-sbmLG48o5mo29HjI3xm6-2N1YsSD2T57oqdn6KCGE7SwgIPjdcbXJO8lfLKhFHiGlZeYvEFgbTKVEN29Z1T1YxWJP6syFAnpkNR8M7GLMliasW5GIUnQ8FYYzvW_P8M3qQVmeHrLTenp3hp2N37OI7QY9hSrXOHvzxpiyVM8S6efo6p1Ve7QvivUewcRt4Ac7RT8yZrEDWtpVysogL5reEg577qDeYHGtHEq-w4b1sGUOAXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdZFwWb0_DYylwXTgEoNvxZxA2UBR4tCzY-ona2uH3Gpzju4H7wok6wk0Nm168A4_xLcI6MtYyEo5HtKBhXtQbzUkhQg4XMJmTSP1Xlu8c7HEASFWGo-IWECXYguEU2Z3-NemN4u988r8Oz4Btj79jvRww-t0ML9tRc_kVHoKPCy2xfTg8rDequEU692I5syDRTOsKqxAZg94zxj34k1jWiZgs6v4DEQ-t1fUCkyDOAV0npwTNyKflx8KYhnJjgjcaBFpeb0fu_wzHPKRjmAeyqmzMfl-fkFqFSsQb_INgeedvdrZXHuyBWUjogUrEg0pCKDAUWdD1DUttH_YyiSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxhfmUAnaO0w4IhtIMoa8VB9v4Vg2dHjDW-AN0i89jd29JLXmlOJB11YaEDffhn08wl_P_YpFtRLNXZUoXTmdn0umQV_k2za7OFOe25yWKinO5p_uRd2J2vbsv7Mz81Gw-q7WnSSZngH22Vk0Sw-4zzWdywhxHYxdFe6ByUERe62RGda6rjraDEBvS0Jj5uJxii04VyORDN2_rASITp_WzilC23wRJTLaK-pV8qK02V_7nG0yBb4aNzUYxEXRzLkLBkudfd6L_O1iM_KrVv74PjwnlXfjrD1yNAf2ef3eB7LnGKv2u67xbzvLWtHHieHyfxUJg0aex-nZkt7uB4kmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=JOONkTLUGF77dcu4YNkM7JAmF6cdgTKWc8B0HXYoIH4Z6s4UgpIcjajyXbNsEB011MYt1OSuTSajidMsmlrO7gShVXqYH7HAye-6U53niSuUDKBYntI_tK99OG6CgHeyleySWPJHmwDwkkuKLoGfOs15Rzhr_COqs7zN8MC8raFcH5_ySzKkGouhrWXWHZGWCjt_7FmzZo84XnAX8tNbhPc269Mniie7_NFyrGCYeWx3pH299w3BNXQ9hM65MMzphdf_pwu9GPmiqrrsDAA21K4ZpVGOQgFMSThlOmJhv_KOhK135F1-12dFyM2e9uIAKy1N1i1DQORCQY25IMLbhjUGkyxvSdlL3meI3yc2Bm8NwHyVJur0p7iROYPA0qa7a0eiaD5k4jO47JiroPEw3AxonAC0vf_AUbb3rtwwLD42uYo99HwzqLHxOTBIgdPr1_fj2SYdcZasdMs24RB8XC1heayoizhgNa26zvQ_ke7STsBkNU2WjoK04Cvn3828Qj7mDGEioTclOgI6k3MVfb3NgfNp7VZxz2qtjGguVLq4_KgaUuEOlNDMbtpo-Joq7Ap-cRXMsK0Nc1WEzBYQqqFuJHHBjvhHYziOlT4SLF1kPbT4xaZVTPRoGzkpiEFVx1-0s01POyqOLzFQ4wHq_EeWjhBSl_vb09dP9AmZDvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=JOONkTLUGF77dcu4YNkM7JAmF6cdgTKWc8B0HXYoIH4Z6s4UgpIcjajyXbNsEB011MYt1OSuTSajidMsmlrO7gShVXqYH7HAye-6U53niSuUDKBYntI_tK99OG6CgHeyleySWPJHmwDwkkuKLoGfOs15Rzhr_COqs7zN8MC8raFcH5_ySzKkGouhrWXWHZGWCjt_7FmzZo84XnAX8tNbhPc269Mniie7_NFyrGCYeWx3pH299w3BNXQ9hM65MMzphdf_pwu9GPmiqrrsDAA21K4ZpVGOQgFMSThlOmJhv_KOhK135F1-12dFyM2e9uIAKy1N1i1DQORCQY25IMLbhjUGkyxvSdlL3meI3yc2Bm8NwHyVJur0p7iROYPA0qa7a0eiaD5k4jO47JiroPEw3AxonAC0vf_AUbb3rtwwLD42uYo99HwzqLHxOTBIgdPr1_fj2SYdcZasdMs24RB8XC1heayoizhgNa26zvQ_ke7STsBkNU2WjoK04Cvn3828Qj7mDGEioTclOgI6k3MVfb3NgfNp7VZxz2qtjGguVLq4_KgaUuEOlNDMbtpo-Joq7Ap-cRXMsK0Nc1WEzBYQqqFuJHHBjvhHYziOlT4SLF1kPbT4xaZVTPRoGzkpiEFVx1-0s01POyqOLzFQ4wHq_EeWjhBSl_vb09dP9AmZDvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvMEpgujlO-VxsFw4JWZ_D--iGwBj31kzO-kcri93bIwPEH7qDhG2KqRm37HfbOsG7yp1LNLIIpOMisSjMQWqHRgjgZnDSU-sEkzbc4kQ5T79YbFGuLXB2O1uYz-WPHUL0aK6I_DbXVvyoJTsP8YGLrBB8uoHN5NLEe66hf5ZRC40FZRsOiu7SZh0-07m_XUGxpj7V3lKOC1sxwTIHtKhgaW_zWTdiiQuuKZ4LR--olx5ciqNmZ4IMXz4yj6VrXtSaXeF-Dk0ZXX2qlGfADgyn28X5nshBqMATZdTX4c0wx88EoXJSV_abOV7gyAEqTfeq-LUwBYtChi-JM0OIZnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=WQsmJI-4Gq6qh3G1pwBirIeMzmvVQvx8JjkoBYoLJIKa4jVHWVP4wO_7xuUnKCIaXw_rYLNUEipS-PHvqOr4ZkVkqnke4_DHxhm7wI-2PbklyRIhKsROJRzyNUKH6ej_WSc-safdD4iLgMCzqgmyxN2Qv0FF-xDE890yfO0qCQSlkQzbXJSjLE9MDJAwiKxgxvXZCt_qLMlUNA2gSUR7Ogl36zntOn2-7Onw_lW3cxLlKB7UspuumMly6lZqIn-WaDuG5ZKhUTJLicuYZvIfU-7TVUz76STq_NY64yNrHStQk_pc49NNw2XSmH8Ac2PDgiYHJgJHrhd7jqKjujDdHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=WQsmJI-4Gq6qh3G1pwBirIeMzmvVQvx8JjkoBYoLJIKa4jVHWVP4wO_7xuUnKCIaXw_rYLNUEipS-PHvqOr4ZkVkqnke4_DHxhm7wI-2PbklyRIhKsROJRzyNUKH6ej_WSc-safdD4iLgMCzqgmyxN2Qv0FF-xDE890yfO0qCQSlkQzbXJSjLE9MDJAwiKxgxvXZCt_qLMlUNA2gSUR7Ogl36zntOn2-7Onw_lW3cxLlKB7UspuumMly6lZqIn-WaDuG5ZKhUTJLicuYZvIfU-7TVUz76STq_NY64yNrHStQk_pc49NNw2XSmH8Ac2PDgiYHJgJHrhd7jqKjujDdHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=RVf8xGtJ7RD-FzbHxMF7tGZUFJ6eSkLzutL4i4O2lRcQL79_KaXnKZ4-KACfIFawQ14Pt9a1anSVHf82ktt58r8qub_zrr_h8iiUIIpbCyCCaSTWHckIsRHMDgdlmyuIs21qYFabqcxxjISNbp3iRUiLys6u43nbfmk-UIBuyiZU5-x7Tkvt5vhzBrpZVMxGs5oJ69VaeRJ3bGrerBGjHfhaVobjbySU0UXAIIzaktBmsL_JvqeesOPbd-zJjFP09c91T0t-B7ZOH2QRt5V0slINg1DAWDjEuaLsnWgyQWbFv4AZlzNPfJ8fj_OhcswSivpNTep6iz7Y6XQjbQhgfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=RVf8xGtJ7RD-FzbHxMF7tGZUFJ6eSkLzutL4i4O2lRcQL79_KaXnKZ4-KACfIFawQ14Pt9a1anSVHf82ktt58r8qub_zrr_h8iiUIIpbCyCCaSTWHckIsRHMDgdlmyuIs21qYFabqcxxjISNbp3iRUiLys6u43nbfmk-UIBuyiZU5-x7Tkvt5vhzBrpZVMxGs5oJ69VaeRJ3bGrerBGjHfhaVobjbySU0UXAIIzaktBmsL_JvqeesOPbd-zJjFP09c91T0t-B7ZOH2QRt5V0slINg1DAWDjEuaLsnWgyQWbFv4AZlzNPfJ8fj_OhcswSivpNTep6iz7Y6XQjbQhgfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDM-cgVF2ECFuYTSCnt8TxCC-Xsg8EbGgZpGvzV0NrDBpOEjTx7lqFQ4p7SiaF0VWgtN_gAEF5ffeT7Gwl7s5YUdsAtpK9Ovqy9KAaB7H1CNCKFFDNb46j80aarYMez1N8iziAp57rGzbZP-C4JdjkbFu27Xi4evriB1m6cKS5AVb5cLi1DhZcGicFhYFo_q5cVEyBKvt-KGlQNsXq12B3xIGtHA9_WSZpD9DyoMB14ds8i8VjfHZUDCvkcBcrOO3IICOEcdIrNtOu9fhCz4ovXpfHVKoTj8X5VTlAGIU7pkFvvkEKe7hPZ9tSidnCkJKBYjiu0fTuzh325zuZvlVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_Risg-qqpBt5Pu90Edj7Il2YGV3BxjBog3Grl4G5LZu6vegMFTgYAkJMythEpuTlTPBnbb9hlJn1_3gA2lcCkS2wJ3jbNwlwKUkqMTCJgyKGM_RZaaM3PXhp_CdjpID_EzSri2K7_i1drUp3gfjv8RYtYInQdRrZ5g2zcPRaolqLMuM1LgCNX1errh3fCp5HO6sNbl4kqYznhQg15jDwk4R3_UP_p-B8S3jrPsPjGIpbPOawIf_YoMi2dOaj5wF_MlXmykfn2yj42NQRih3gHacnm4kBuaihTuFfP37buU6j4OkVpn13aBKx6GqePY33-vt1zxNr1DdS7YPe4dZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=upuwivTssVmzp1TRcAbRYCNkVv_dMegv23yYhdN4haVkSsxlf7zLP86jlMlObVMleccSIdBn9iNiJp3CfilYaTRCbJsfeGz9SR9wMFfwds0ii-_7WBTZGvFCYLgztqvKrRBjti7Ou5rn9jcnrIF0469bU3FyUbbqEORcYpYieu_5YaLkj8J-xliciK9_5-dUjp0xpqYhvy0-9jgPam8CDOJkyvGFzqLTm2t_golalsEDIknRfEdCvwTjDdP_hdpgfSzyoueXA26nMgxho-Uz1yEn4zNY2KuNqP4T-_APtkMQrh7lbFJ_HrUgKstOKNjQ843kQuEWoLvVoVsntrMDirXAkNgHwe9V7xxDrQPGpcRc_zwYUTir99ms4p38bkhP3MfQJuj9GIBv6vji7pzORYxpbDEUbUn-0EwmMmXzThI7TAs7T_SbliewpqTetCezCaztDpGz4abD3x-EIoAiU0plMUleJ127OMi6xjiDFY2jPijpf8amoGhZhIMPQujlb8xQGicJvQo62x6mNngVn7ryxb6_1XePUgBdV6p8L-gqTLeuiGD7s8doQlyZyL7AyzyWHYWkEvS00Kmxl9ZY8doJ_qxHsNA4wJ02NrOxt5rDSyuN_TV5V7uYKfDQoaDqcI0ymQANccXD1Oe0J8LWQ4SVHq1gyiev26zdBnwWX4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=upuwivTssVmzp1TRcAbRYCNkVv_dMegv23yYhdN4haVkSsxlf7zLP86jlMlObVMleccSIdBn9iNiJp3CfilYaTRCbJsfeGz9SR9wMFfwds0ii-_7WBTZGvFCYLgztqvKrRBjti7Ou5rn9jcnrIF0469bU3FyUbbqEORcYpYieu_5YaLkj8J-xliciK9_5-dUjp0xpqYhvy0-9jgPam8CDOJkyvGFzqLTm2t_golalsEDIknRfEdCvwTjDdP_hdpgfSzyoueXA26nMgxho-Uz1yEn4zNY2KuNqP4T-_APtkMQrh7lbFJ_HrUgKstOKNjQ843kQuEWoLvVoVsntrMDirXAkNgHwe9V7xxDrQPGpcRc_zwYUTir99ms4p38bkhP3MfQJuj9GIBv6vji7pzORYxpbDEUbUn-0EwmMmXzThI7TAs7T_SbliewpqTetCezCaztDpGz4abD3x-EIoAiU0plMUleJ127OMi6xjiDFY2jPijpf8amoGhZhIMPQujlb8xQGicJvQo62x6mNngVn7ryxb6_1XePUgBdV6p8L-gqTLeuiGD7s8doQlyZyL7AyzyWHYWkEvS00Kmxl9ZY8doJ_qxHsNA4wJ02NrOxt5rDSyuN_TV5V7uYKfDQoaDqcI0ymQANccXD1Oe0J8LWQ4SVHq1gyiev26zdBnwWX4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=Tkbo9-7nfZj9v4kqY6I4QOF1ByiPaUp2ijyL9K8aaJUKG8ZJM7ydzDrRUwbEeyKF6gvPBlzFAGJXUNXGGYnSavKnHBKTqBxLthMb6pvwJhHbFmIr5Ohgk3e0TL6cgw0DnmJh-sQGArKcnhDjjjy2Dysy9cNOV-Y0xN3ep5boQXAXeF2-yTbpZxOHdxGO6qVd9GR7fXV0-b12MR36Old8nKJTo94zV5a0hy4HN5Fp2owqFzR_K_cygPpEmtD-Bb43uDeegf_dQZmurVHMLozhQ9AX5_vmfLd5THyKKQC3VTrF7SSWEyuAugFA4mqUMJnaFke6SrmTsaHvIdbL9YPshh0NypbYW0ZJha4eDnKTq63JtPhELO1cwqDsuoNPjT2AamsXEYiG2ViLUl_1NsFei387lUNN-GoDG8MX3AGwR80rZzUoJ6e19KBr2suQkc9QM5RWnPYmsKC2l0ARPJxw05KzvH0UjxvQ-kB_xUrHuQd8s6BLbwnjyLe03LYKcqgoUHd_srU2bNXonc12HRwnMpeNIoatyUCHN_A_hw96dAMvz66FLQXR2l5rSxTbI230P9JVGUfU6EdSe8J5lJ9On-D9lZ2IPCa5X6tz7RIro4oiMfXOyQHBbUy_6VMSUnpyZ3j8lSW54jslItfHMjqDQf2jdiMN8kxBJUSbqzdpBfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=Tkbo9-7nfZj9v4kqY6I4QOF1ByiPaUp2ijyL9K8aaJUKG8ZJM7ydzDrRUwbEeyKF6gvPBlzFAGJXUNXGGYnSavKnHBKTqBxLthMb6pvwJhHbFmIr5Ohgk3e0TL6cgw0DnmJh-sQGArKcnhDjjjy2Dysy9cNOV-Y0xN3ep5boQXAXeF2-yTbpZxOHdxGO6qVd9GR7fXV0-b12MR36Old8nKJTo94zV5a0hy4HN5Fp2owqFzR_K_cygPpEmtD-Bb43uDeegf_dQZmurVHMLozhQ9AX5_vmfLd5THyKKQC3VTrF7SSWEyuAugFA4mqUMJnaFke6SrmTsaHvIdbL9YPshh0NypbYW0ZJha4eDnKTq63JtPhELO1cwqDsuoNPjT2AamsXEYiG2ViLUl_1NsFei387lUNN-GoDG8MX3AGwR80rZzUoJ6e19KBr2suQkc9QM5RWnPYmsKC2l0ARPJxw05KzvH0UjxvQ-kB_xUrHuQd8s6BLbwnjyLe03LYKcqgoUHd_srU2bNXonc12HRwnMpeNIoatyUCHN_A_hw96dAMvz66FLQXR2l5rSxTbI230P9JVGUfU6EdSe8J5lJ9On-D9lZ2IPCa5X6tz7RIro4oiMfXOyQHBbUy_6VMSUnpyZ3j8lSW54jslItfHMjqDQf2jdiMN8kxBJUSbqzdpBfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=b2JpoPjC2B-5EZ3Nq3LFdpIAW8Xvz14WMvUC4yMOAfV7xJqIC8k-0dLqEoJndEY2KeKyy5Fc9Nozstjv53RjAvnoZhCihN9cQv4CaoNkun27KrZ4fygF4tJJlPB5pMpCIfBGVsYN5dfVR1oDElYZ_D_ohLINaFgZJI2Htp2frRwPIbT3D57NNfVYw2QzVAQuAHs6CkM1bv9HbyZFbFRG8M2uPc6H52ZT-REUHKC9GskippZ_gu6PWs1g1R5ChVZo97_mMH8yr7GuA1PqMDXh2UX26vu1Z_ij55nPt1CD6vL24EmYtrWdt7hig6LcNcTmrQx8OnmZIBuNFJ1Mye4sog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=b2JpoPjC2B-5EZ3Nq3LFdpIAW8Xvz14WMvUC4yMOAfV7xJqIC8k-0dLqEoJndEY2KeKyy5Fc9Nozstjv53RjAvnoZhCihN9cQv4CaoNkun27KrZ4fygF4tJJlPB5pMpCIfBGVsYN5dfVR1oDElYZ_D_ohLINaFgZJI2Htp2frRwPIbT3D57NNfVYw2QzVAQuAHs6CkM1bv9HbyZFbFRG8M2uPc6H52ZT-REUHKC9GskippZ_gu6PWs1g1R5ChVZo97_mMH8yr7GuA1PqMDXh2UX26vu1Z_ij55nPt1CD6vL24EmYtrWdt7hig6LcNcTmrQx8OnmZIBuNFJ1Mye4sog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukeswOcM0siIVcs0NrnQaZsE_svPsqcU57nYgYn1QQdl8SCF2LcHZ6vyhnzUyHAtS550K3YNkiB6L9ceiJ_ech3B7d0V_4bBpe8KH7oVM4LKrrXIkqibhj5qEqOrJjDQnTx0tZSNPBcj2V61LPGhbiN8GI8PE1n4BS5tjECOF1uTpPJkYSfMzicXS38MCfiL_kMOArK47xbnUeosR2i7JoEvMmV76iw0XiKwv8xpvKFldL-iijMFFMEA49kXIYfXcg27wuLwQzrM-LTOa9SEkxuP6KrEr2FzTeMHXtfiqjMae3eUAf73ZSuNi4l1S8U8xrPf-VH9g4iCMkfQEe_FAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=k3RJgohfBGqNC5ZxVNrzdi1D8mh99L41mkFvjY1vPjT1AlmLr204TAs7mVb2qlGNeLzAEx4eXOiBTqHswoVbJ-Tc0eUhcex3qNfv-a3kaxkHdfZvx-8go4UzjdywDUye0WnowdSiYfyGj0TzR6Ho3jNAnR04w_DUaiVi4_tVRyTPF-dW9Kp-B465CnvP8alahAHYjDopTI6ofmZAMfnZ2R44M_P0hQVKutfjIBsfKkhT2P25dwvkkIJcF82tnCEZfuPSh5SSx6QpX-39B3n9x-69mYusIe5YomEikbthtbkKBtGT5wzVIxWHECfj7_H5Rtuph6v4woLfPen4RVzy2KIyxSQCrA0n1i7OaEXmREgXag0ogn3aIDFaGwc8cJILEtANRYk4e5JdXb-V-A9wN49hBq741CyRD8hkn2bGCfZ5d-URRG9w-MzUn0hOohkDLkmGKQGWV5Cs6urKBDHqsxPdbfO8YJnqRm7AnTqhXMkqODmAyW93My7KYSsW1ZzZzVBWhgmftRfJMLDPOoDcTO4YrTO2CRR38q597Fjm2HOjNYf6v3hGf2puOzVlxy0O7AKa8awDJAPwy10QYDO55PcI5_c4dOuBBssPllTQFWEYF1g4f8cBm8rc1A_PxbHmtJUgYlHxes5H0wkSO02lpTH6Zq7HZ0HX2DZKZKpxP_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=k3RJgohfBGqNC5ZxVNrzdi1D8mh99L41mkFvjY1vPjT1AlmLr204TAs7mVb2qlGNeLzAEx4eXOiBTqHswoVbJ-Tc0eUhcex3qNfv-a3kaxkHdfZvx-8go4UzjdywDUye0WnowdSiYfyGj0TzR6Ho3jNAnR04w_DUaiVi4_tVRyTPF-dW9Kp-B465CnvP8alahAHYjDopTI6ofmZAMfnZ2R44M_P0hQVKutfjIBsfKkhT2P25dwvkkIJcF82tnCEZfuPSh5SSx6QpX-39B3n9x-69mYusIe5YomEikbthtbkKBtGT5wzVIxWHECfj7_H5Rtuph6v4woLfPen4RVzy2KIyxSQCrA0n1i7OaEXmREgXag0ogn3aIDFaGwc8cJILEtANRYk4e5JdXb-V-A9wN49hBq741CyRD8hkn2bGCfZ5d-URRG9w-MzUn0hOohkDLkmGKQGWV5Cs6urKBDHqsxPdbfO8YJnqRm7AnTqhXMkqODmAyW93My7KYSsW1ZzZzVBWhgmftRfJMLDPOoDcTO4YrTO2CRR38q597Fjm2HOjNYf6v3hGf2puOzVlxy0O7AKa8awDJAPwy10QYDO55PcI5_c4dOuBBssPllTQFWEYF1g4f8cBm8rc1A_PxbHmtJUgYlHxes5H0wkSO02lpTH6Zq7HZ0HX2DZKZKpxP_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=AaJtPaAhOS2VKxq-GEeiHPkmOtCUSvn4-TSRqFKfw6VX1yLYQItUXcMMgg1oEvPkETPVpPLkcgNBAn5gqlSX82EwJC0jxQKF1sDmT14rJ8SFoXqknzXCR4Qp2_bBlpOZADaAX9974qZxldfVJrWyh-AGikplqDKYL1KDK7Kkho9Gh56sNWyHc5uhhc4e6ZLnNUxkGdIcV8VcvnCGwu5vvOo4ZvQfBDR1NCcVraF8_v_gDJVEyBgqIlehHtfwWoYAZA5kI-ptXfsLUi3QuXFewy2ejQm36aRNfGR0V-84adt-xuMXk0dmJbkMGFx-9sFGosrgZnUT6bH5q7cuS_0HCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=AaJtPaAhOS2VKxq-GEeiHPkmOtCUSvn4-TSRqFKfw6VX1yLYQItUXcMMgg1oEvPkETPVpPLkcgNBAn5gqlSX82EwJC0jxQKF1sDmT14rJ8SFoXqknzXCR4Qp2_bBlpOZADaAX9974qZxldfVJrWyh-AGikplqDKYL1KDK7Kkho9Gh56sNWyHc5uhhc4e6ZLnNUxkGdIcV8VcvnCGwu5vvOo4ZvQfBDR1NCcVraF8_v_gDJVEyBgqIlehHtfwWoYAZA5kI-ptXfsLUi3QuXFewy2ejQm36aRNfGR0V-84adt-xuMXk0dmJbkMGFx-9sFGosrgZnUT6bH5q7cuS_0HCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlvftqudze1cyHNuJjJRukjqrwOGNT0BzWbAfIl90xue8utF9ZXOZ5NwQeS3ZIY7JWmxKumejjOJ52eXmj3cG_p-FzEigX06XnYXKCHgx6qH7Hlt8B1-nJpMI8kPCBwWScFG89m9r3-7SMgV-bGFVLeOilNkgswLK7YEzlOZmgaDxWiVfri-EhNr6s4A0SptdSJOvbmDPPrWXj9W-t_PYoC5iAOl3NtdXpkYVkZ68Rry623sYTf5-xtuEw2ur9SvoOQ0n-rMSq4IUNH2Z82my4pZfzsIjBwWQjYOLNTvx6miMDMATXTcmgJw24HW64BVE9ecJ5D2H6P7TcHeklbYdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4wBCpHVelGSscPhMK4hmYlLOlAHNaMjl5G5vGsSyxbebmFu7L5LA-iN4b2oFC0h4hquyh1eUzAK7IVqR8z7N6tnLT1nby1x25c2iqvSs-Sq_EaLJsOpKOygDnt_m-3prDeMNPm4tX5VM73z3c8O0okAFh1WcWFAIq9DPcEf7DF7xVcqW5vqR8s80ymmHQvwDfEEDHDRTCGWFedo6m764HQFi0lprLV9TAzzuCtPyYZNGa86A3fTehyZPpNWzbPtBKm5jX3PvXji-79ePfcjm-fmvIuTNf8sGvzmgNwJDBmy1YKm6SvrEHMaKd3o2OESk7BtRdLEkFzqh5TVYZ0l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouYBJ4AGEQpmQiC4g1qzaO2SwWZN2PlaAUzHkQytNjHw0yp1ZMYBDdlFTEnUGxTFdJYMOXjYDk-zkIdcactS5tTzpwAHMOg132dbhZ_entiSdCj2aSDkwTwDRKYM2r5AbyP_LkemgIG9T5PIss-gF31tyQhP0HlM6UYkzItQRgy5p9w1vheus9rzuh7fcGoQsFPBHFm9tSIPsOqo4tNATbg81wwOB5uNiilvd_vK5WB3EB7K9HF5p8AV390wZubrOEfrXjdgHUk19t3miUIRHIDwXiH46NpdfmFYXWYrbnDEoGVGOSkNHAfUhwqvNgturK-yZntbE540_6A3O0s4YQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JlxgjXoCzrNu-bIrRbmxVEKH0w2uKoHcShXsAdqdRp2Jpt3wi1befmL6B4rnFJK8NLImi_MTQylP8bY9Iq2ZAUPwSnGXFkMw0YSVYpS1Fnz_O2jzhDmECixwSpuo8GXxeWmh_y5ULzxPQVsBDyUpvJaIwtl2Gj2eFBjAf1w36HotTcSMCiQfWe_7EbzKNT1-HnTy6JpYDd4CxHS4Le2bAFSudmwRn6eScmDpTC_qlFflIKXzP0w7x2uGyhuTwFOZOoHeIJp0GEdc66Wgnu_TjRfpjRXZDu0RFUVhJjOBbGZmvFP78S_g2TcUPPAKhRJ9fLWAR08fbI1jDTmj1gd3Jo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JlxgjXoCzrNu-bIrRbmxVEKH0w2uKoHcShXsAdqdRp2Jpt3wi1befmL6B4rnFJK8NLImi_MTQylP8bY9Iq2ZAUPwSnGXFkMw0YSVYpS1Fnz_O2jzhDmECixwSpuo8GXxeWmh_y5ULzxPQVsBDyUpvJaIwtl2Gj2eFBjAf1w36HotTcSMCiQfWe_7EbzKNT1-HnTy6JpYDd4CxHS4Le2bAFSudmwRn6eScmDpTC_qlFflIKXzP0w7x2uGyhuTwFOZOoHeIJp0GEdc66Wgnu_TjRfpjRXZDu0RFUVhJjOBbGZmvFP78S_g2TcUPPAKhRJ9fLWAR08fbI1jDTmj1gd3Jo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quCM6xEYhwDXLWcBd3tpRVfnFfruVyul31RxIU1lvBJrUlegRKE2Gm1XAYYeqLRQYzzfIX4Gjb-CbnsQnT-oYmYVxAZFausQZKL-o3g2U2h6-qT2R2ewEHzKIyfVQFR2Cs6c6q4Ad0BP0_W84KwL0cglWV20FuTBCmNjkTVKOW5Kv02XTQoBds6Y5QETU5EehWJoWlEykGtsMlZuK3hgmC_JZhk4xtCq-kT_vujgZhlA9ovNnH9lAy_i944pmGqdPlJZfgFf52oHKx_bdlga8xK13M6tXt26rtOwCXVSSs8Rdp2d8txQf9agxFPrFb19rq6JFdi-0a6Ch0M0cGfhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=mlreo2XDrL37aZkuCGsv9BUPv5-VNKtLK7wQrInD0x5bEtCvuntBaC0z5Xe_b3GpLTdSshopaeZxFaIEAonJCVe58kSvBiL-csBtvdF-4amRC2m5GJ_ZyjL7-0k6XnF_34geo92ZD1rXDlMtlQmd9-x3_JrIT8WqgAxBQLY0M3Nd-Lq3AO-87mupo0La9wP1103g9FbUlbazt2pBd5-y05y9yubxCMkhHBd7fPq-HPXnXeJqyy1UIOOHiy83myZcwY3_YiGIuage8jYFrNLYvEr_YB2gLdtS85Vueu_jheyMc6c_6ghS6hTS6sj2yClytyclaJYqor88vT5Nme7PiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=mlreo2XDrL37aZkuCGsv9BUPv5-VNKtLK7wQrInD0x5bEtCvuntBaC0z5Xe_b3GpLTdSshopaeZxFaIEAonJCVe58kSvBiL-csBtvdF-4amRC2m5GJ_ZyjL7-0k6XnF_34geo92ZD1rXDlMtlQmd9-x3_JrIT8WqgAxBQLY0M3Nd-Lq3AO-87mupo0La9wP1103g9FbUlbazt2pBd5-y05y9yubxCMkhHBd7fPq-HPXnXeJqyy1UIOOHiy83myZcwY3_YiGIuage8jYFrNLYvEr_YB2gLdtS85Vueu_jheyMc6c_6ghS6hTS6sj2yClytyclaJYqor88vT5Nme7PiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=Fow5nqUtZw0VQXXHnnkzLZeilHHsMdBAjwHmpumcnZMiRC7FDxtr5mmoxOVWEAB7LSMT_sq62Jg-swn56WdL_Fiy5Bph987hFBGP-kGME7xnRyUzHGbS314xHJKLqVt1RMiLxwLp1gZByfkr_M0QRmunfh3T2R6JhjmmC6ttox-DCb0b6b5jlGApozNqpV6_qjNlZCvFWemfkNpNbx6_hsNLRyn53xZUp65CAH5dha9nApZA23NbcE4nE09lXMEHP0OK0K4dZHyj5RC6W_gLGuCmqJRLDBuH3UQde7nnJPxrApkPpF45WB2JsL7ATTwPZlNval-yfgfhDRfXqxVh8XPEbgqYTMNhNkKloJ__BRbdfPpEnup2X5E6vTZ8_MZvdGxX-lPuZeuZRZJ43jJ1MOPwKsXMywSAMhD_wfNFLEj_JVQKVm16pfhkFPmflOkH8AVQ5qfD__xIPeFznp4_2ULbSdqgH0KukUlT7kOByp6VX0zwX7xvz7KHE7HQdg4OTRdr5JIUBynIYa1gNsQ0K-GxGReBcgH_G2uJOHcuxp7XOdAxyZRA18HYAxIciTSW8_HoWZPLuKr62WTP4w-2viODWn3x5TsDrJdjrnCg8NZTDmCou0lClsnJT66DaeaQ4O9F3cqgRUisoCAONw2UDUT_xVStSO_-t4L-jODnOBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=Fow5nqUtZw0VQXXHnnkzLZeilHHsMdBAjwHmpumcnZMiRC7FDxtr5mmoxOVWEAB7LSMT_sq62Jg-swn56WdL_Fiy5Bph987hFBGP-kGME7xnRyUzHGbS314xHJKLqVt1RMiLxwLp1gZByfkr_M0QRmunfh3T2R6JhjmmC6ttox-DCb0b6b5jlGApozNqpV6_qjNlZCvFWemfkNpNbx6_hsNLRyn53xZUp65CAH5dha9nApZA23NbcE4nE09lXMEHP0OK0K4dZHyj5RC6W_gLGuCmqJRLDBuH3UQde7nnJPxrApkPpF45WB2JsL7ATTwPZlNval-yfgfhDRfXqxVh8XPEbgqYTMNhNkKloJ__BRbdfPpEnup2X5E6vTZ8_MZvdGxX-lPuZeuZRZJ43jJ1MOPwKsXMywSAMhD_wfNFLEj_JVQKVm16pfhkFPmflOkH8AVQ5qfD__xIPeFznp4_2ULbSdqgH0KukUlT7kOByp6VX0zwX7xvz7KHE7HQdg4OTRdr5JIUBynIYa1gNsQ0K-GxGReBcgH_G2uJOHcuxp7XOdAxyZRA18HYAxIciTSW8_HoWZPLuKr62WTP4w-2viODWn3x5TsDrJdjrnCg8NZTDmCou0lClsnJT66DaeaQ4O9F3cqgRUisoCAONw2UDUT_xVStSO_-t4L-jODnOBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=l9NtdO0d57cVTKQqlikzcyTfQwFoGtJm2HBgE8T0LQtG1CWrTYOucd6NZWlWOL2TX8R9hhTVsfrL4qcc5rGaOukAklC1OMo-innTWqnOXdZkjzc8fht0aGFezzYuOa3uYlQsrlp8RvjS-7jl2siFa_Dk7n9bQ9TWF075AXxx11YLV3U66aDqfCGPYoIQMtSInCAy0XT8npM2iTo4xitQaMYfIpdHDrG0TJ6jM9xf7p9ft-2RJ3A6jTZ0wBVJemG8orVhGE6EalR2CIWAQZvT3umJfVv8QfCDCIkU_pEiHxu-bf1qRnOJHNveEkuE2QF_sCKk-n_9QtK_skAA2RoZ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=l9NtdO0d57cVTKQqlikzcyTfQwFoGtJm2HBgE8T0LQtG1CWrTYOucd6NZWlWOL2TX8R9hhTVsfrL4qcc5rGaOukAklC1OMo-innTWqnOXdZkjzc8fht0aGFezzYuOa3uYlQsrlp8RvjS-7jl2siFa_Dk7n9bQ9TWF075AXxx11YLV3U66aDqfCGPYoIQMtSInCAy0XT8npM2iTo4xitQaMYfIpdHDrG0TJ6jM9xf7p9ft-2RJ3A6jTZ0wBVJemG8orVhGE6EalR2CIWAQZvT3umJfVv8QfCDCIkU_pEiHxu-bf1qRnOJHNveEkuE2QF_sCKk-n_9QtK_skAA2RoZ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1NLytKRoW2EED3Mm8peB0dOX_HxF_tAQCpZB4aDfDsC-mTaaiAYSJEWuEcB9-LSltP6pDMMSTZ89mgPNOeGvuypAc7mND0DX-1FsvxadyczD6YazluJvG7fzCVUxWKLfOFQETu6RQvwklRQnUYzzjXEF4TztZcv36jDx9QYli6zPQC2nWcSCYHiebz48r_MHNsTWDTP4YtIgKOYRYuvnX-MFZq7J1GOl60x9dD5oCPxbg1iCInGvRmpxKDeh-X3vdpyjiRInMnskqJWDchyyAtNO9dtumixjEMom_RvcrKU40s2Y6DKvc_QKTB9qaG6gVf--gOVCsXOTtNtpZWx0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=s2vtQG7rJBcmpvpD4s27PFr2HbPRnHj8yR9fcc153cY8UYqGoVHr5es0IzKB1VIqTYez1_ekvvnhPXCKNAzufeyn4NGRGYaGWQBSR_GIVJvDlOMb6Y092zMFbsqiLwAfOvpRwIH1tR-bQFm1CSt2-6ok0299YeY-l_SgwoH287DzkrEe2368Jb8SizQ5UV2LhLQRivanFMc5AjMU-Cc6enV0neF_Ii5IkI7ZUwuwxRUj1K_vIB5TQnyyL0MhQEoxJUKgMU4hwLQ2WFPOA2ghq5cbyeJJAX3eCegtDq0FF_EUq8KsYMPDnklBCnO2y0_wSXAwrDyoU0BTO0YYlIHdDGtljRi2N5G3qbxRS78CIzijhB_VEtZ4S_ZuAuUOT4nXMM0nZqHyZyn_gYivTCr9oTU2CoTmgtF-2HGihX8nmOVzm7kxWk2XsGiA9vH1nXAdfJY8FyWObjHSrfhOdA56q5J0xFlc82KhzVJtcrcKlmTbwuX8rOWSCCJub5cxt-stcbxZ6LEH3YCkakZPR86EKP6DalhAIKOcViLQL8MOiykU8DhtIXUtc6iXJmQSMFi8yCzegGLijZ6R5C0xvloetkXNSk-7dzVARJAXGXpiqhpw-3iQYglbeIt1RGtyfVbdIm328nmbs2FrKGFwn3vtX8yiI6nXRKldSp96ke5N2P8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=s2vtQG7rJBcmpvpD4s27PFr2HbPRnHj8yR9fcc153cY8UYqGoVHr5es0IzKB1VIqTYez1_ekvvnhPXCKNAzufeyn4NGRGYaGWQBSR_GIVJvDlOMb6Y092zMFbsqiLwAfOvpRwIH1tR-bQFm1CSt2-6ok0299YeY-l_SgwoH287DzkrEe2368Jb8SizQ5UV2LhLQRivanFMc5AjMU-Cc6enV0neF_Ii5IkI7ZUwuwxRUj1K_vIB5TQnyyL0MhQEoxJUKgMU4hwLQ2WFPOA2ghq5cbyeJJAX3eCegtDq0FF_EUq8KsYMPDnklBCnO2y0_wSXAwrDyoU0BTO0YYlIHdDGtljRi2N5G3qbxRS78CIzijhB_VEtZ4S_ZuAuUOT4nXMM0nZqHyZyn_gYivTCr9oTU2CoTmgtF-2HGihX8nmOVzm7kxWk2XsGiA9vH1nXAdfJY8FyWObjHSrfhOdA56q5J0xFlc82KhzVJtcrcKlmTbwuX8rOWSCCJub5cxt-stcbxZ6LEH3YCkakZPR86EKP6DalhAIKOcViLQL8MOiykU8DhtIXUtc6iXJmQSMFi8yCzegGLijZ6R5C0xvloetkXNSk-7dzVARJAXGXpiqhpw-3iQYglbeIt1RGtyfVbdIm328nmbs2FrKGFwn3vtX8yiI6nXRKldSp96ke5N2P8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=VoPKxY-5plufqdnYdzop3suM8FjAaHTkbR3-VQkK7sXBRGxXMQSH3aW9yH5cHrrZMlnsybMfrA5-C6_1aoAoAZ5vB0p9i4qquj8meUHXt-IOF2TNBRWM8C18TylTouzbKUbsfxPcuLKyejZVAO1EISNNb5LW5wHxZyR3QEQhVAD-NTq-S4CEurv2CMa_bW0F-niXS_v8CFlS7TUdXPn7fkFlmIXzUEkl2pIM6Mmmy4x-JSedt7NtA5ODtW1UsqsjLOdvxqQcJhsOHJ7uM87xTMZLFWgI8T0pFlBp_EpIwtcWyL83cXe42gvz_fRgRpPZrXPBA8CoW6XRyc7IxZB_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=VoPKxY-5plufqdnYdzop3suM8FjAaHTkbR3-VQkK7sXBRGxXMQSH3aW9yH5cHrrZMlnsybMfrA5-C6_1aoAoAZ5vB0p9i4qquj8meUHXt-IOF2TNBRWM8C18TylTouzbKUbsfxPcuLKyejZVAO1EISNNb5LW5wHxZyR3QEQhVAD-NTq-S4CEurv2CMa_bW0F-niXS_v8CFlS7TUdXPn7fkFlmIXzUEkl2pIM6Mmmy4x-JSedt7NtA5ODtW1UsqsjLOdvxqQcJhsOHJ7uM87xTMZLFWgI8T0pFlBp_EpIwtcWyL83cXe42gvz_fRgRpPZrXPBA8CoW6XRyc7IxZB_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=gxvSSqbHvhGnEt882weaT-tADgVInwkhDKKHtItnmmjluiQrRK5Ba24Pa7HOpz00OVQAxs6dRccaBcfpFVh6hj9DCtdKOoSa4L5itfph1cD33rmvggGVOLNc6HezA3mDcNi7dS1PUWyWw4qafzybI-e_Zef8-Vy6hqvnLwEC6shGtK2l4vc38Ji9bBKr3rO1TgbFNKSK9Be34x2boMGeim2zbjx85frYCgFvUDVmrb8d8QUjf1gU7zHrbXnjzJhXP04O5gFimGFtJG43p4rjcPzd1jvsqYfgD6KRBU6hu5aBBc_9J8efTjAym-HlEjt0B_Wks-7dS_rhES1W7ZOlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=gxvSSqbHvhGnEt882weaT-tADgVInwkhDKKHtItnmmjluiQrRK5Ba24Pa7HOpz00OVQAxs6dRccaBcfpFVh6hj9DCtdKOoSa4L5itfph1cD33rmvggGVOLNc6HezA3mDcNi7dS1PUWyWw4qafzybI-e_Zef8-Vy6hqvnLwEC6shGtK2l4vc38Ji9bBKr3rO1TgbFNKSK9Be34x2boMGeim2zbjx85frYCgFvUDVmrb8d8QUjf1gU7zHrbXnjzJhXP04O5gFimGFtJG43p4rjcPzd1jvsqYfgD6KRBU6hu5aBBc_9J8efTjAym-HlEjt0B_Wks-7dS_rhES1W7ZOlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSbRSnRZo_1MdApOGf8TlqqzRm2bOkp_kyW0PUmz_NNV7pp55DxdV0d8GLMRhYZpUoykLnYeVgBP9OoSRuaIXhXsybPfZURAhiGhCvZXS_aBWUWobPeGmgP8-qp9wXBytCQ436nUoDpaLGv2Ds049ZR-Yd1sl63VBJQ1RplLzTj6ohMfJa-CZM9MVS07D7N5cALphV6Fz2k86RU33eTHHieeTPOxAJbbYV91XBfNlwNLqPSxpa2XBdTceF8bXgdq_zciKDNEBz9o5Pv5Jpgb5SKpxh0fnNmJmtGr96tzctA89wcXc6hIA1jkz_Ll9mLdNWX4yqcNja6-KullO3CV8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=YrZ8kAzuP2itVt3dv1__cDYfXxh9u-kt9smuhjZq_s7j41dv_JDUMJ1UOJlSW0s-gWpq4pjw4T9V_g1Admg9l6IYOx7qsz5xTrGxLmOhoOxZGVBmQGQBeQs8H-k7lUvRNJ7AkDZi6L5Bp9DpPsNPFAzjkdTBaLV8iuN7wXZS3lY9ivmU0fPEN68wf_bwUDCTs30qKyGfpnOPRGOzg6P6Sz0IdHl8Hibe1fRwb53nvTjjNkwsILpO_g0V6LDWzYYyk-6M6R4NXNvaokYQqZUy_vzYdLI2yKxPkLZ3tW04AlTxnv8h6jtjr0EfZklvKNQY5koeWrOMekQQirfXiUWPlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=YrZ8kAzuP2itVt3dv1__cDYfXxh9u-kt9smuhjZq_s7j41dv_JDUMJ1UOJlSW0s-gWpq4pjw4T9V_g1Admg9l6IYOx7qsz5xTrGxLmOhoOxZGVBmQGQBeQs8H-k7lUvRNJ7AkDZi6L5Bp9DpPsNPFAzjkdTBaLV8iuN7wXZS3lY9ivmU0fPEN68wf_bwUDCTs30qKyGfpnOPRGOzg6P6Sz0IdHl8Hibe1fRwb53nvTjjNkwsILpO_g0V6LDWzYYyk-6M6R4NXNvaokYQqZUy_vzYdLI2yKxPkLZ3tW04AlTxnv8h6jtjr0EfZklvKNQY5koeWrOMekQQirfXiUWPlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl_BWmIust05XnQhh34U7ZKpoefm-Dxzs7BSCseq_6r39EAQoqVpHCQpqXQeXf-urZnS6NldkJKSLbPYPJ2mKgHaeMlMjPRH9u7Y_lMdwKX9rQezoRFdwgHLl6oME1ruk1799ZCSyLP96iVZbmZzk-EDwdfUC-k1LSGhjWktROYmSN9GDUMTZwwvJRjaSnIdC_aEvKkCPcdsVvn-u5udVQ331u6QGGhiWsFo3HTMFR8pqI67We9p7j79mZ9AZljMtWAHV4OvXmT3Tsm47AvY5-92jM50XLbJyKtTk9C-NpZaSAetIX8w9YyJbiTRSR_FTWoH3PDlIVOJNA2Lp9JkyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=onrvEYaSgixlhmGPBVXWGmK0sRPzDHG5g-VRbg0ZorIjRVDif3MZZVJyN1dQ41PzCoCqptvRE7xh41-V04km3kKEisKxhJbROBbnzInBJCMjvjzxV25OEYqFQqxTZcj3umCiJVFQH2wQbh2XNbUm82iwF_oWowdtiphyh7KyLjU0A-Eqc8u8KMGp4B1QGbvy-dEqUU_FV5mufSw28DvHc9BwcxenjSH5trY_nx_ft0XF4jHk4feedxw0E5P8mR_XqYvWPPtvDR1PGcybfBxNteMFdLMjImCq3OEXEh4U7Vn0Zj8XOAzoARo5rQWCEHO6QhMUGQRKVYd3Izz7E3t7kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=onrvEYaSgixlhmGPBVXWGmK0sRPzDHG5g-VRbg0ZorIjRVDif3MZZVJyN1dQ41PzCoCqptvRE7xh41-V04km3kKEisKxhJbROBbnzInBJCMjvjzxV25OEYqFQqxTZcj3umCiJVFQH2wQbh2XNbUm82iwF_oWowdtiphyh7KyLjU0A-Eqc8u8KMGp4B1QGbvy-dEqUU_FV5mufSw28DvHc9BwcxenjSH5trY_nx_ft0XF4jHk4feedxw0E5P8mR_XqYvWPPtvDR1PGcybfBxNteMFdLMjImCq3OEXEh4U7Vn0Zj8XOAzoARo5rQWCEHO6QhMUGQRKVYd3Izz7E3t7kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA9g0Zop8UsgsCuNrBwuzcQIzyZvLqVqrAIIaIPaDndkFZW3C7XjmKgI8wjHM0MB3azhsrO4UZaVPuWdVOkM7x5AMGZzvHad3-4zyooZhXCgcYQRRsfXXA9bggWYHhkKyJMtqmfz9XYFPaBumaOEJ8JsyB62ZKZ1DNMrYG2JV6F-kH7WKoXXgu6yR_WhfqV-jnhTU-wCD72lctRq-arTKmZ6bhRfcgimden5CVkcx4t5UPvg6TC7TbJEg7OhwSEKjypZkYvOWZtEhZKf2FZ3Uf2FCC9xn_pb2xXVLoy8D7VNKTjbAXfF2x-kCHUDorw5TeamosWXv96nAUS5cUVwOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=Rr6EQdk900eSbWZUaQnd0MHLUwReNWClxlwzUeAC8RmaHqobwVK66HIDf2em2qecxvUEt_iG_cWRkPfvN1jHcpyo4_TiYcsFSFdoIs5-hep_0ZQhUL7PhSnFGDT0bGQ3x1GaXwTAB7pI7sNHxcZ5Fsmhf8_6ZsG9_dB21HZbPdou1lgltkb6LsVziBMbDLLQbWw-6AzA6588jv7bVrK1L76Zue7OhlXaMrMir7KZ0P8qebfQEkt9zUE9UjLOc3kovzwbp90H_o4moywKvrJyRASK5HEWu--VwfqRagkrMJO_fvvjtd76yO5yAEc2tTDjVjZ0gtFlj6pe60Qjc7iHAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=Rr6EQdk900eSbWZUaQnd0MHLUwReNWClxlwzUeAC8RmaHqobwVK66HIDf2em2qecxvUEt_iG_cWRkPfvN1jHcpyo4_TiYcsFSFdoIs5-hep_0ZQhUL7PhSnFGDT0bGQ3x1GaXwTAB7pI7sNHxcZ5Fsmhf8_6ZsG9_dB21HZbPdou1lgltkb6LsVziBMbDLLQbWw-6AzA6588jv7bVrK1L76Zue7OhlXaMrMir7KZ0P8qebfQEkt9zUE9UjLOc3kovzwbp90H_o4moywKvrJyRASK5HEWu--VwfqRagkrMJO_fvvjtd76yO5yAEc2tTDjVjZ0gtFlj6pe60Qjc7iHAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=TJxZIl5QG0Jaq48nyukgLYQ4ariBoLyxlgk4mHaygX8_HjABo0zN710_va0xt9C8LWkBkvW67bPNwLdugzc66k45KA0xdG6ejBpAG7FyaB4y9ZdN85QbcW8POHp8GAkWy2s75xivLOXnoDaHqIKsUjYtLRQ0ipwDuWCcq7dPFQFtonXhWzL0HmkqFcf-KmNqfu0szdTi5ZqQwcP8UaPNSNFbPhb5VJ4GffKyLSVGIJEYFXh9QYCx_rv5APgH6dehhL8ZlVvpW-b_wpg6DyQUGWFBs5jD7X79G7PA_kX8rLGHhqcxUXdmDxrtC2-NVGlo569Od47f1axL0F-NncWwJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=TJxZIl5QG0Jaq48nyukgLYQ4ariBoLyxlgk4mHaygX8_HjABo0zN710_va0xt9C8LWkBkvW67bPNwLdugzc66k45KA0xdG6ejBpAG7FyaB4y9ZdN85QbcW8POHp8GAkWy2s75xivLOXnoDaHqIKsUjYtLRQ0ipwDuWCcq7dPFQFtonXhWzL0HmkqFcf-KmNqfu0szdTi5ZqQwcP8UaPNSNFbPhb5VJ4GffKyLSVGIJEYFXh9QYCx_rv5APgH6dehhL8ZlVvpW-b_wpg6DyQUGWFBs5jD7X79G7PA_kX8rLGHhqcxUXdmDxrtC2-NVGlo569Od47f1axL0F-NncWwJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giRzdki4E9OaCjyOi-Nd1wvkvCx7lpHpzTVI6zf4hgsD3tIqT_duqcZ4a5JP56kfRdETizb7xaLu-RII27f3H335S9k8eZCzkOu-yaSQ3fG0hUmeoEUeJFBKd1ylvqy_XvZqWIZR1GcPmTscei5gjq0akHxg4GVyiM7iz8nU_xGSrsY5d3H-kNHntWrpCNneo-BZW_nTNsgjlwa14KK0c-2QR7EH0o6_4B3dyXUo3HN-NfCcv9gpNbyUHiOrYCEnqY3SERN5FDAr6cLCcSvmR5cUu1OnJEsuND0PStR65fi6m7-SuehNciGSsrwJrBErsFLDGGMSbebB5uPnJMGisQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OazYMwbdfek0DSDDvPdq9OIQYHjEfcYrnPUQb-A1phvZAK_MI1WFJDau9FXRtBmsHbEFtWhT0Oc-ncUD3kD1GTWs3WXWmJ7Cz0BQiMweBcusabphaKj9MLCs_vBgJn2_c9I7gamevPlxkKvS8NGik5HN3VVNBGCAh8MDCzq4jXNBV4Cs5dPFYAIpyp7HYaXZxa88gTVs6llHN6ewL3uVvZGB_gJBKtlFPrlT4xO5YG0GMw_oicRM6-I-7LOofjzEtb18Bh7NtMjWmLNVYSZnfXC0t-S9UaV4RsG0KeX0kOAmBhMbJaSi2IOJAUE3YJtJro51yPYwJ_nU3kWhcOozYoMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820OazYMwbdfek0DSDDvPdq9OIQYHjEfcYrnPUQb-A1phvZAK_MI1WFJDau9FXRtBmsHbEFtWhT0Oc-ncUD3kD1GTWs3WXWmJ7Cz0BQiMweBcusabphaKj9MLCs_vBgJn2_c9I7gamevPlxkKvS8NGik5HN3VVNBGCAh8MDCzq4jXNBV4Cs5dPFYAIpyp7HYaXZxa88gTVs6llHN6ewL3uVvZGB_gJBKtlFPrlT4xO5YG0GMw_oicRM6-I-7LOofjzEtb18Bh7NtMjWmLNVYSZnfXC0t-S9UaV4RsG0KeX0kOAmBhMbJaSi2IOJAUE3YJtJro51yPYwJ_nU3kWhcOozYoMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=cFl4iTlb12EVs-4N4l_VunqkJTObGS-qQ5ZPisHlVfwG3jdm5ct67B9VslR_iYPh6y_vNgH-tR4_6UHS9HMUwF4Ke321pzQFLA7KuKLEQeGtrgN9Ja0Ev_lFwNpCr8OHkINK8TnJuKc3U80xYIsj9eXXQdvMEyDUw4tzRa-geSq1J2BQMN1DdJemJQ_m1-DJ0MIsM6nTqIQaaPeT4414D8tr4zqbGHW-f2V7nxmDLDgS9o9xhDrMLMC2BQJ9eT8k-ylzTDMX3dAC1NB2lABTFdfIz6peqNflB4l2mueQaIks4x-Wwu-4NnB7DHuu3dvIobNaE4ytuguGty9ImxSULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=cFl4iTlb12EVs-4N4l_VunqkJTObGS-qQ5ZPisHlVfwG3jdm5ct67B9VslR_iYPh6y_vNgH-tR4_6UHS9HMUwF4Ke321pzQFLA7KuKLEQeGtrgN9Ja0Ev_lFwNpCr8OHkINK8TnJuKc3U80xYIsj9eXXQdvMEyDUw4tzRa-geSq1J2BQMN1DdJemJQ_m1-DJ0MIsM6nTqIQaaPeT4414D8tr4zqbGHW-f2V7nxmDLDgS9o9xhDrMLMC2BQJ9eT8k-ylzTDMX3dAC1NB2lABTFdfIz6peqNflB4l2mueQaIks4x-Wwu-4NnB7DHuu3dvIobNaE4ytuguGty9ImxSULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=GNhUnY86s4n1H_72fWYTz_DD10Gixqh71NsVVZqD0B-v412-tyJzUhtEG1ZY4Ds7EcbedRfXI_OZ_reo5FzsMwFJ6PwDaICM1_YlVfrd43xzW2RYVQZ20G39cDRXXsRJtq6UHajbLZgjRkS0NxrLKTyxfBwXO8gUmthg3YXA06kbsBWF-Yt-gyzmVmR78i9YLQCb5ELWViPCx0Zyv4QbtB--8Th4c0TS8LhuDfkfVIWxoPuBeB4tMgLmwQu51ZZBEImjMATlEYvGSufRgdxAkK7ip5wai--BEktLR9ZUxdIX8fW5ZZ7-kk22wx_QGUqq0uYDE2cJGrnUUzvqvNNy6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=GNhUnY86s4n1H_72fWYTz_DD10Gixqh71NsVVZqD0B-v412-tyJzUhtEG1ZY4Ds7EcbedRfXI_OZ_reo5FzsMwFJ6PwDaICM1_YlVfrd43xzW2RYVQZ20G39cDRXXsRJtq6UHajbLZgjRkS0NxrLKTyxfBwXO8gUmthg3YXA06kbsBWF-Yt-gyzmVmR78i9YLQCb5ELWViPCx0Zyv4QbtB--8Th4c0TS8LhuDfkfVIWxoPuBeB4tMgLmwQu51ZZBEImjMATlEYvGSufRgdxAkK7ip5wai--BEktLR9ZUxdIX8fW5ZZ7-kk22wx_QGUqq0uYDE2cJGrnUUzvqvNNy6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPkktBuE7kypXKAUXyo06v94C5y32eBco23gb3-VYJQYjgfNfLReV6lFqpsiNDoqAu1qaO2WpdTbXJBCja3Jlt8kAq0L9bvbp6FAocmlILqN7qOrcWobx_Oo9bX4Y89WVzAARHgipmiEoOC4U0sGs6sOL3CjX7G8ukJg5p6Y8E-EC2bQeZzvRtd-3_UVBIZRa8rDFk-TrHGOLhssr-At4Ua4irltrWrB0YE6uuoCotrtHXw3gg_-eA-hKE2spCp3dMdrIn48YjifS94Nsxo4f5Q5b66HRnOGjSjcjR4BPyc81fzjnAcGUEYjX2TUgT5czlmDs3fTYRIzH8ivytZ49Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=UsmP04QrxueUAqShiwnTHxBa_dQpjcLSIZRdOaAkXOWCHoTYx9-pstxlT2_k4pudjhy2MkWFMQPvmOa3k67KJbJ-fPeMFIxI_DT49qBLKbW9cebbtTloSx-MpuN4ZdOMJsSckU-De1vx2eD_Bztv7kDcoNvCkPEuuHBB_Sx7Vm-Yb13D4_RFtJoZ41d-tQec0UMWfO9-s7zXhsMkjK5YHfle29DhlqKtOAc_kFRUb6cdx7h6-OOxappLKTViB5Yxa8dzsZyvYU2MqnrlKS1667cZF4R2qcu058O3oE7M1FruS0EHf9nO3uAz36B6FecmQQqdGa5egjhJalESg_hZrjP4mwxfhH_sT2dms115w6iGG3OC29lHqsuUNgQM3SHDzbT2vRLtOOp8hp6G4QFXlUSlzJ1vMa5-6ppih0Rn6A3UJG6_OhBNddUGZ4h0tuqdyRVh2WurfQ3_8pUxKA3k1y1Pk2mo6lkH-v6W0QOHMdNfXlYVeg9a9kAaA0CrDUZWLLsINRVTutOkdAwjMGBITJy45giIYcSV7tozj9J5esgDE-ibXqkkUyxdIBgRh-EfrU2O-ecVfO4rDdNZw1s1iLyAgRzDvDuykvSGCtwNx-9fc92HIUy81DWOO_mhcUxeZde4SJMySf_gskZB5imjhk_m8ab601PmDNcmf05L-cY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=UsmP04QrxueUAqShiwnTHxBa_dQpjcLSIZRdOaAkXOWCHoTYx9-pstxlT2_k4pudjhy2MkWFMQPvmOa3k67KJbJ-fPeMFIxI_DT49qBLKbW9cebbtTloSx-MpuN4ZdOMJsSckU-De1vx2eD_Bztv7kDcoNvCkPEuuHBB_Sx7Vm-Yb13D4_RFtJoZ41d-tQec0UMWfO9-s7zXhsMkjK5YHfle29DhlqKtOAc_kFRUb6cdx7h6-OOxappLKTViB5Yxa8dzsZyvYU2MqnrlKS1667cZF4R2qcu058O3oE7M1FruS0EHf9nO3uAz36B6FecmQQqdGa5egjhJalESg_hZrjP4mwxfhH_sT2dms115w6iGG3OC29lHqsuUNgQM3SHDzbT2vRLtOOp8hp6G4QFXlUSlzJ1vMa5-6ppih0Rn6A3UJG6_OhBNddUGZ4h0tuqdyRVh2WurfQ3_8pUxKA3k1y1Pk2mo6lkH-v6W0QOHMdNfXlYVeg9a9kAaA0CrDUZWLLsINRVTutOkdAwjMGBITJy45giIYcSV7tozj9J5esgDE-ibXqkkUyxdIBgRh-EfrU2O-ecVfO4rDdNZw1s1iLyAgRzDvDuykvSGCtwNx-9fc92HIUy81DWOO_mhcUxeZde4SJMySf_gskZB5imjhk_m8ab601PmDNcmf05L-cY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuDCGKN51LzPgiJ2gs4Jsvyv-RneFGw-LBrq4eSLmvoQec_JmKuGcFejz5_O61fj4D4NMkwW_W4utM999zasMxRa3PPKTOpBjZPZ06wkiZ3_YmUUrAXML2prKez8Qo15q0HgSUfVO4Osn31w4BShuiwcD7QsOtJ9qv_fWGChv1XGxW3D0lJbSXoX4AfybN_kUPISDsKtuMdH6TJ_C8JiMyFdHhqaONwD8qnqttCEcMerZS8c6V5VDPjUPlE0FmlhoNVP9wx0hFcj7rTmtBHHijH-yaZ5gnhMq1q1JhPhH9OVLmrE874qVYfMM_xc8ytKoHrYlBLx6H6WtOXUL443dQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=NxRJZrGfAKs-kb_UoJNTDUZLxowMw07MIFnzOe2Vt6aNSIfqzGnsNOslwfvU4PwLu7ThNwgO565sgdgd0RZODsdTFbxTrcgogTjuLNz-GfzunrJnnhXw_W0zQ1OnY-uVg5kkRL2jOefGafRqUAa1enPjzn-3pOlIieK093zfz7voJxq75xPFYlxA-p6BS6MbMiG6tPlmBzzwl1EC7BRc1zSzOelSJoKNA6l_YT7VzSDYM845V5gLrBwrwB6svaRP3AIf0KIRYFsiGClPB3zLNUE9KGvONU6xboQfB1aTCYsWDfqs6WJhIJXR4_RWiKaAdGOarva-hGlIKihkx43Lhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=NxRJZrGfAKs-kb_UoJNTDUZLxowMw07MIFnzOe2Vt6aNSIfqzGnsNOslwfvU4PwLu7ThNwgO565sgdgd0RZODsdTFbxTrcgogTjuLNz-GfzunrJnnhXw_W0zQ1OnY-uVg5kkRL2jOefGafRqUAa1enPjzn-3pOlIieK093zfz7voJxq75xPFYlxA-p6BS6MbMiG6tPlmBzzwl1EC7BRc1zSzOelSJoKNA6l_YT7VzSDYM845V5gLrBwrwB6svaRP3AIf0KIRYFsiGClPB3zLNUE9KGvONU6xboQfB1aTCYsWDfqs6WJhIJXR4_RWiKaAdGOarva-hGlIKihkx43Lhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp2hSwinrdcyxcyx3zobDcarMJ0tkCg7AJmSKiHmKn4F6xAJR3Q2QV5SAXWmUQe_SgO32MxGrlRl7m6B2NoEigLw61xMVOB-2N_1UBSBpmoFpGMsdbFDMwBVtTBKJDP3uiCBoxx6j49dVNibsh2hpfRxglFJSS6WMjXSm67cGXtUywpyHHvV6iLtQxvWCtvhex0NomwghZ5JkKYOnoJXWCUIo4OK9O1Cj7LztAIvHmAFhqECo-qMtnGMywZkspOwZgtuObJN3cT-DLq6-ADGxWJowVFYAUmyyefwu_0qN7JAqFssSd5OeIKy7PHxJvHCPO2ACe0UWQceRHCg7K6vfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
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
