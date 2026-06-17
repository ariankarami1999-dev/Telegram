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
<img src="https://cdn4.telesco.pe/file/XqWDPdMND8zw31k3DSZFYPJB5lLdBEmtIMnTdx7g0Q_ThHot61hyKPIwIGz-xxPM481hz8RZqZc9tdmYvAegQUUCNWWMZI9QqwGZQ3zYtzOoSh05GySbPenjsfmzBq4cV1n7JL8X99K72M7kcgS6J74Oe7at9d1GVXlMPDmC_onSbfQJNeSN97fcU4tOCnfmbprBtHRhJ_VINpVWToRJLcLkSrUafEgobU4sHV8gkZki2_VZN0kDtr2-OnsBQozDZgt0dwKjHQ4LkBxFde_ZGo-0pE_JWYdpm7RKPwYpAauDPH6m8eDGqj_daXmSz7IJ1wzjiWKV0IZbf7wztYjfUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-17714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ می‌گوید احتمالاً نیروی دریایی ایالات متحده را برای «مدتی» در خلیج عمان نزدیک تنگه هرمز نگه خواهد داشت.</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SBoxxx/17714" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ می‌گوید احتمالاً نیروی دریایی ایالات متحده را برای «مدتی» در خلیج عمان نزدیک تنگه هرمز نگه خواهد داشت.</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SBoxxx/17713" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">— یک مقام کاخ سفید:
«ایران باید فعالیت‌های حزب‌الله را محدود کند و هر حمله‌ای از سوی این گروه با یک پاسخ مستقیم اسرائیلی روبرو خواهد شد».</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SBoxxx/17712" target="_blank">📅 22:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17711">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.  بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/17711" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17710">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYhaQ4X-4hCg7Q9YyzkgQVVBamBgDS2ZtUIjUU52t9rZLIHrPuoUjQUBilu6sZ_a4NOm0LBOBGC6obqWV8xy_J-CuYOnDsE4RAJh1S1N0DX7sFp0y0Iwetdn_SD4cotqjYfGrw4KOdqYJUb3aovgEwdOsvZqkMjDugqjtLOZdtSiyNJlI6-vyeCl7AK-x7zXCsD1njJKzIGAxdTyFEZ5EI25TmdvqsR6BIZBpPqVYMVbgoTLmbSb81PQEnMtj-5Fb38CLMdj42yuRF5s3caGCZqlhWnFwHulmuhrVNqY7fWYeTPuJqsbsQl61ggh19evN5VfcA0DAcm-8Vzp4N88jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوزیشنی که 3 دقیقه پیش از انتشار صورتجلسه فومسی پیشنهاد شد.
بشدت هاوکیش موضع گیری کردند و آفتابه را روی کله زرد گرفتند.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/17710" target="_blank">📅 21:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17709">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزارت امور خارجه ایران:
«لبنان سه بار در یادداشت تفاهم ذکر شده است و جنگ باید در همه جبهه‌ها، به ویژه در لبنان، پایان یابد.»
یادداشت تفاهم بر احترام به حاکمیت لبنان تأکید کرده است و حضور ارتش اسرائیل با این موضوع در تضاد است. اشغال مداوم جنوب لبنان توسط اسرائیل نقض یادداشت تفاهم است و ما اقدامات لازم را انجام خواهیم داد.»</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/17709" target="_blank">📅 21:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17708">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت امور خارجه ایران:
در حال بررسی امضای تفاهم‌نامه از راه دور بین روسای جمهور دو کشور هستیم</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/17708" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17707">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl3nMgKO0ekL0eSBQ0Ghu_zF34RuwnHzeJJTK8ttiqKn5mqZZoyEPdV76yungJ1qiTUsKqV0mOGkD7h-Q8k2yL3OFaYm-ExYVPto-T490bbaoG6uJgQuksUiEqJosXByIdR8etfGAlZY1nioav1TF9krss_BfirnITCco_RMbJeE5NNgGO4pMamiT0iMxvnc1vlsvb9b2FHTQdqQ-KBp9pdk5oek94jjfgqI-L38loZXS_ZjiKCZmx6LbAygUZqkg1ZjJIlKPF_azamAMX1Uqi_Uy4a9tSvGNq-ypIJb9h1UvodZCTW3c3PkkZtcmVAJ_o9nD72vsCYOGSRMYWhkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج از دور باطل
✍🏻
مهدی خراتیان، مدیر اندیشکده احیای سیاست  ‌تغییر در ژئوپولتیک شیعه، عقیم‌سازی حزب‌الله، تضعیف بازدارندگی شبکه‌ای ایران و درنهایت تمهید برای دور بعدی حملات گسترده به خاک ایران، تصمیم قطعی اسراییل است.   نتانیاهو با محاسبه مهار کامل تهران…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/17707" target="_blank">📅 21:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17706">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این مدل اجبار قهری برای عقد توافقنامه عملاً یک نوع Duress است و پیمانی که در چنین شرایطی امضاء بشود بعداً میتواند براحتی لغو بشود.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/17706" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17705">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏ترامپ:   دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/17705" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17704">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ :
«اگر به نتیجه برسد، من اعتبارش را می‌گیرم. اگر به نتیجه نرسد، جی‌دی را مقصر می‌دانم.»
«بهتر است مراقب باشی، جی‌دی!»
«او هواپیمایش را برمی‌گرداند و از اینجا گم می‌شود.»</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17704" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مقام ارشد آمریکایی درباره متن  رسمی تفاهم‌نامه ایران   -ما شاهد توقف تلاش‌های ایران برای قطع تردد در تنگه هرمز پیش از  امضا هستیم  - ایران اعلام کرده است که ذخایر اورانیوم غنی‌شده خود را نابود خواهد کرد و نحوه انجام این کار  - اگر به توافق نهایی برسیم و اگر…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17703" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مقام ارشد آمریکایی درباره متن
رسمی تفاهم‌نامه ایران
-ما شاهد توقف تلاش‌های ایران برای قطع تردد در تنگه هرمز پیش از
امضا هستیم
- ایران اعلام کرده است که ذخایر اورانیوم غنی‌شده خود را نابود خواهد کرد و نحوه انجام این کار
- اگر به توافق نهایی برسیم و اگر ایران رفتار کند، اجازه لغو تحریم‌ها را خواهیم داد
- ایران موافقت می‌کند که حداقل ذخایر اورانیوم غنی‌شده خود را از طریق رقیق‌سازی از بین ببرد
- توالی مراحل توافق‌شده موضوع مهمی در مذاکرات آینده با ایران خواهد بود
- پس از مسئله هسته‌ای، در مورد تأمین مالی نیروهای نیابتی بحث خواهیم کرد
- جلسه این آخر هفته در سوئیس برای بررسی چگونگی پیشرفت مذاکرات با ایران "حیاتی" خواهد بود
- ما کارهایی را برای ایجاد اعتماد انجام خواهیم داد و خواهیم دید که آیا می‌توانیم به توافق برسیم
- نتانیاهو درخواست نسخه‌ای از تفاهم‌نامه نکرده است
- اگر نتوانیم به توافق برسیم، ترامپ از استفاده از ابزارهای خود نمی‌ترسد
- تماس بسیار مداومی با اسرائیل داشته‌ایم
- تفاهم‌نامه امضا شده است اما هر یک از طرفین می‌توانند تا زمان حصول توافق الزام‌آور، از آن خارج بشوند</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/17702" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خب خدا را شکر نشست خبری بی پدر تمام شد….
به همه توهین کرد، از سعودی و ایرانی تا اروپایی و افغان!</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/17701" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درباره حماس:
آنها وقتی به دنیا می آیند یک مسلسل در دستشان است.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/17700" target="_blank">📅 20:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران   به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،  درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/17699" target="_blank">📅 20:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17698">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ فاش کرد که حملات و بمباران‌های ایالات متحده بیش از ۱ تریلیون دلار به ایران خسارت وارد کرده است.
«بازسازی آنها ۱۵ تا ۲۰ سال طول می‌کشد. بنابراین باید خودشان رفتار کنند. اگر رفتار خوبی نداشته باشند، دوباره ضربه می‌خورند.»
ترامپ همچنین تأیید کرد که ایالات متحده حتی یک دلار هم برای بازسازی به آنها نخواهد داد.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/17698" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17697">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/17697" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17696">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: ما در مورد موشک‌های بالستیک و نیابتی‌های تروریستی صحبت خواهیم کرد.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/17696" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17695">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏
ترامپ:
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/17695" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینکه با جنگنده باستانی اف-۵ که بزور نسل ۳ است و همان زمانی که نو هم بود عملکرد خوبی نداشت بتوانی به پایگاه نیرومندترین ارتش جهان آسیب بزنی را فقط با هنر خلبان ایرانی می‌توان توجیه کرد.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17694" target="_blank">📅 19:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اگر ایلان ماسک یک تریلیون دلار از دارایی‌هایش را از دست بدهد، همچنان ثروتمندترین فرد جهان خواهد بود.
سبحان الله!</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/17693" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایالات متحده، ایران و میانجی‌ها در حال بحث درباره برگزاری امضای یادداشت تفاهم هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و ممکن است همین چهارشنبه برگزار شود، طبق گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آشنا با مذاکرات - Axios|</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/17692" target="_blank">📅 18:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایالات متحده، ایران و میانجی‌ها در حال بحث درباره برگزاری امضای یادداشت تفاهم هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و ممکن است همین چهارشنبه برگزار شود، طبق گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آشنا با مذاکرات - Axios|</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17691" target="_blank">📅 18:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aaa93f21f.mp4?token=mnLnu3Tgjsn18JoFVnBUIzwPbCbtypb4DXugeZB5rjwO7tC4gLFiwpP6wxSnUotLFb3iOm00slFnnoFlTrhN31RFDfxNCXMusw-du9LWL9jcFHJ47Mi20Iq3BidZJcbXEGQazQXErcwkGMRrqFN3CiNTgO6xQtZ4vos5xAs5JLQVbjBpTWVVDpdbACtHLNs50qKkAFQHc2fYv3oka8R8e9eB91qhepa7Aa323Wde6k_n7LJ16q4gTxKun573T7rQmfb0_g0VRH4TMZaKfQoCFzGK2Fy8EW1FYm9x9RBIQ42Rd_TNLfMeDXuTqfNvTibh2e5Oa63LgOSrkAsCjkSOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aaa93f21f.mp4?token=mnLnu3Tgjsn18JoFVnBUIzwPbCbtypb4DXugeZB5rjwO7tC4gLFiwpP6wxSnUotLFb3iOm00slFnnoFlTrhN31RFDfxNCXMusw-du9LWL9jcFHJ47Mi20Iq3BidZJcbXEGQazQXErcwkGMRrqFN3CiNTgO6xQtZ4vos5xAs5JLQVbjBpTWVVDpdbACtHLNs50qKkAFQHc2fYv3oka8R8e9eB91qhepa7Aa323Wde6k_n7LJ16q4gTxKun573T7rQmfb0_g0VRH4TMZaKfQoCFzGK2Fy8EW1FYm9x9RBIQ42Rd_TNLfMeDXuTqfNvTibh2e5Oa63LgOSrkAsCjkSOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:  «او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/17690" target="_blank">📅 18:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUtDQrPDyOeI6gHX5x-wP8pYdug3TrlsFxjhx9sVPvWgP1QqFv__jV8yDL_xrSDBd0-s6dop88ek4YbfRU0TE1TDl0aJ8rPOzahBgNeUS6D-Bz7IafwMYCGcoOYFSfX7GN1fAWQB9QIRkRw5FhzK2jMpUVcO2BZpQ26CpHAyH-THN6xZxR7G26DYtsYpAd_Tb_pWkU8HZiy1pp_1q74cJmjJlaUGZknvc9ZAdKtlqM2XS0t_zmZ_5LHhDYshdpRwLbZZUWyTiMpjNj7QG6_jnbI6LSyUp1gTBqrEzJ7NVMMyrjifI94tNMMDxzC4TLDcJf_5KIDNXDQqFEJvX4ErjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:  «او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/17689" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">—  ترامپ درباره مودی نخست وزیر هند:
«او زیباترین مرد است. او مثل فرشته است. اما در واقع، او یک قاتل است.»</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/17688" target="_blank">📅 18:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">موجودی نفت به کمترین سطح بحرانی در بزرگترین مرکز ذخیره‌سازی ایالات متحده سقوط کرد.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/17687" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-gU1Uh9b-hhZBRHH0cXaUkS7QBXJ6ODHkU1u9pjlDYuWHaGe-Sdbu5pyugMYx8o5Sm9-v1JkpBwncrvsgIVfNJS4B0q1w9qhjAn2uLZaMSmN_P-5JL3qqGTraW_Tp5re76QKrafD5eFc8YTxcoJG5OX32xan5j2_JqmgWuN1k8jzIyYqMjbAGSihImNx1k-l5Lo3TcMDaypsJuh9ZzeOI91bs_HCMuaJBI9tujnAZxucezMoVEWCVxULewpFRhnYg9XwTlWjWxBXZ29_gSI65gErvcpOyGy2sFaxfJzmu0dlNRYeQrHrQdAmDmtPjK9OJmdgnoTjG3DalN9VTlmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی موسسه مطالعات جنگ از ابهامات و اختلاف روایات بندهای توافقنامه ایران و آمریکا</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17686" target="_blank">📅 17:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
سفر هیات ایرانی به ژنو لغو شد</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/17685" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">توصیه ام به شیربچه های دیپلماتمان این است که اصلا حضوری به ژنو نروند و به همان امضای الکترونیک بسنده کنند!  واقعا یک خودکار یا خودنویس حتی اگر از طلا هم باشد به احتمال لواط زوری با این ماموت کله زرد نمی ارزد  سبحان الله!</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/17684" target="_blank">📅 17:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ونس ترنس:   طرف پاکستانی از ما خواست که متن کامل یادداشت تفاهم را برای مدتی منتشر نکنیم.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17683" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ونس ترنس:
طرف پاکستانی از ما خواست که متن کامل یادداشت تفاهم را برای مدتی منتشر نکنیم.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/17682" target="_blank">📅 16:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تشدید حملات اسراییل در جنوب لبنان و تصرف شهرک الحدثه!</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17681" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عراقچی گل!</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/17680" target="_blank">📅 16:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حاج عباس حتی زبان بدنش هم کلاس درس است!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17679" target="_blank">📅 16:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">توصیه ام به شیربچه های دیپلماتمان این است که اصلا حضوری به ژنو نروند و به همان امضای الکترونیک بسنده کنند!  واقعا یک خودکار یا خودنویس حتی اگر از طلا هم باشد به احتمال لواط زوری با این ماموت کله زرد نمی ارزد  سبحان الله!</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17678" target="_blank">📅 16:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ می‌گوید در هتلی با رئیس‌جمهور مصر ملاقات کرده و آنها «عمیقا عاشق هم شده‌اند»</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17677" target="_blank">📅 16:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ می‌گوید در هتلی با رئیس‌جمهور مصر ملاقات کرده و آنها «عمیقا عاشق هم شده‌اند»</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/17676" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چرا قطر بقای خود را مدیون جمهوری اسلامی است؟  ترامپ در سفر اخیرش گفته بود:  ایران به دلیل وجود امیر قطر، خیلی خوش شانس است. امیر قطر در حال مبارزه برای دست یابی به توافق هسته ای با ایران و عدم حمله به این کشور است. ایران خوش شانس است که امیری در قطر دارد که…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17675" target="_blank">📅 15:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17674">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh0CM1yXJOnrdummzyhY79H0zjLj0ebQPE85LCAIRunmXW-VvCJ3eRnzEZzmkuQ7Aw3o3xu-AjRPw6TgsVxIZOIh_ZcJVh40LqIc_luKnPQmLFxJWluR1mlFEsLFrk2DURndsFD3pe757R5166QFXT6rPbHOthWD1wqBxtr1XjuzRjgQtsCSzysxeFv_mGCGIkBRZo_vGcpaLQTt5zmxISK6ii5yLO8-F4KPpUJf-2-WYyuTXZzl0YALDwk8E_GLrF_Npcocl62pXCojiA-rke3lJHJIQnsNoMXzPELgYhMjn6yVbdJZVEAOIy-ksoeYKAA8Y5OnCjGan_fWIvxtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی کانالهای ایرانی خبر داده اند که قطری ها برای راضی کردن ویتکاف و کوشنر جهت فشار بر ترامپ برای پرهیز از جنگ دوباره و امضای توافق، یک هتل نیمه کاره 5-ستاره در دوحه را به این دو نفر هدیه داده اند.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17674" target="_blank">📅 15:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:   ایالات متحده صندوقی برای سرمایه‌گذاری در ایران ندارد  تفاهم‌نامه ایران نهایی نیست  اگر آنچه می‌بینم را پسندیدم، دوباره حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/17673" target="_blank">📅 15:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17672">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:
ایالات متحده صندوقی برای سرمایه‌گذاری در ایران ندارد
تفاهم‌نامه ایران نهایی نیست
اگر آنچه می‌بینم را پسندیدم، دوباره حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17672" target="_blank">📅 14:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17671">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔵
پاول دوروف ؛ مالک تلگرام
:
دولت بریتانیا می‌خواهد استفاده از شبکه‌های اجتماعی را برای کودکان زیر ۱۶ سال ممنوع کند.
اما ممنوع کردن شبکه‌های اجتماعی برای کودکان فقط آن‌ها را در معرض خطر بیشتری قرار می‌دهد.
آن‌ها مجبور خواهند شد از VPN استفاده کنند و به محتوای غیرقانونی بسیار بدتری دسترسی پیدا کنند.
ما قبلاً این را دیده‌ایم.
وقتی دولت روسیه تلگرام را ممنوع کرد، ۹۵٪ نوجوانان روسی همچنان از آن استفاده کردند. آن‌ها فقط به VPN منتقل شدند. همین‌طور در ایران</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17671" target="_blank">📅 13:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17670">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ylhjw-puASJZEGdHlbng6QHxyr423DKTjI84TWSm1NteFpRQJrdEHXBmzlI6DIPgahfT2pj_0zwQNwm4am82E4AglxbwiI9qRjsHguB8mXnLSsLT5Nj_vOFrEr9qznBzUU6WunKPrOQFP4iTHfw3CNOhhR7IXUL5zMkzyf7i_u4QDXQEBwy07MsGzhJH5rqXBeRohve5GxH5z41McZ8Aa1DDNccVDndTLzbXRCCFOYQb6guRHiRNumznZkQOW2kZTCMVJm2Ob8CwtTvwweg9QDNv76rNbFUrhr74CgMo9REm2GAbHB2UPrGP4nYewzuqApOHcdU-meMuhzCfyThSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای باری نظامی امارات در پایگاه نواتیم اسرائیل فرود آمد
در ۱۵ ژوئن ۲۰۲۶، یک هواپیمای باری ایلوشین Il-76TD متعلق به امارات از ابوظبی به پایگاه هوایی نواتیم اسرائیل پرواز کرد. این پرواز از حریم هوایی عربستان عبور کرد.
این رویداد، نشانه‌ای از همکاری نظامی رو به گسترش و عمیق‌تر امارات و اسرائیل در برابر تهدید موشکی و پهپادی ایران است. پایگاه نواتیم یکی از مراکز کلیدی نیروی هوایی اسرائیل است.
گزارش‌ها همچنین حاکی از استقرار سیستم
گنبد آهنین
اسرائیل و پرسنل نظامی آن در امارات پس از حملات ایران است. این پرواز احتمالاً برای انتقال تجهیزات، مهمات یا لوازم پشتیبانی دفاع موشکی انجام شده.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17670" target="_blank">📅 12:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17669">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.   خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17669" target="_blank">📅 12:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17668">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQHkZ10M6BS9eSg1yH0h5Lpjjy2CLIvqH3hrsLI5lhplS5VSXKTR96LzSJrS0rwkX3FMWAhTkAsfs0iNzEXwaG3X6pxtxQUEMS6eFi5WSh-QHf4sv1Yr3vkDm6Hj70F9MSvbuHx_awJr6OJhYGzzZspAR6K12gzXgpbOHMEEJlf49i_3hP7ne-Lo6YKQI1GN3M2bUGk4C3pbrbbDX5S2LDCVxuTfdOrtAg9XxJ-mi2whFCFAHpAsOGOlDnnmKvtS0RrLs1dEXii0E6U2vc4d9AcylK9ymEbNvhMbRoxJorxQ_acRXyMjctdH9ucH9No0BImpDlYIj3A2N5uj-DkBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.
خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع یا تشدید درگیری‌های مرتبط با جنگ ایران، به شدت افت کرده و به حدود ۲۵-۳۰٪ در ژوئن رسیده است.
این سقوط با منطقه زمانی خاکستری “جنگ ایران” همخوانی دارد که از اواخر فوریه تا ژوئن را پوشش می‌دهد.
در مقابل، خط آبی نفتالی بنت (حدود ۲۰-۴۰٪) نوسان داشته اما اخیراً پایدارتر است. خط سبز گادی ایزنکوت از نزدیک صفر شروع کرده، به تدریج افزایش یافته و در ژوئن به حدود ۳۵٪ رسیده و حتی از نتانیاهو پیشی گرفته است.
این روند نشان‌دهنده نارضایتی عمومی اسرائیلی‌ها از نتیجه جنگ ایران است؛ افکار عمومی معتقدند اهداف اصلی (مانند نابودی کامل برنامه هسته‌ای و نیابتی هایش) محقق نشده و این امر به ضرر نتانیاهو تمام شده است.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17668" target="_blank">📅 11:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17667">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بدون تصویب مجلس این توافق اعتبار ندارد  حسینعلی حاجی دلیگانی، نماینده مجلس:  طبق قانون اساسی هر توافق و عهدنامه بین‌المللی باید به تصویب مجلس برسد و بعد در شورای نگهبان تایید شود وگرنه وجه قانونی ندارد و باطل است.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17667" target="_blank">📅 11:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17666">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بدون تصویب مجلس این توافق اعتبار ندارد
حسینعلی حاجی دلیگانی، نماینده مجلس:
طبق قانون اساسی هر توافق و عهدنامه بین‌المللی باید به تصویب مجلس برسد و بعد در شورای نگهبان تایید شود وگرنه وجه قانونی ندارد و باطل است.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17666" target="_blank">📅 11:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17665">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzb9g3ackUretp6UXaj95VvqSvyIZ_Pv1csN_JhFcze5UpUgkL97z7xfur9pCwD6sX0Ymc4b8rvItH92dpmf0l4ROYA3NxJ86jzoPmlKkfuG2o7c2E0csho-LXW_ykqeBT0DKWB6Bx1NYyEl8m49Gpfso296ekINib0bTTvUZqiWup_AAiBC5KQ60a5kiOqc42HfZdrND5nCYcBar03dUUBSolG1Y23roVkmpQ3iKHVod0c3z0rWwvd0kQZygFIYe1pDgKwqY_-OjJUlMVLXhjQNuCc5A-hUWRW16ZfE5ztIY0ea4r_kL3eubXJu-scgYJIYCKpBCLXKCReWaAgyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناتو در حال استقرار سامانه دفاع موشکی SAMP-T ایتالیایی در قونیه ترکیه
سامانه SAMP-T که به طور مشترک توسط فرانسه و ایتالیا توسعه یافته است، یک سامانه موشکی زمین به هوای متحرک است که قادر به رهگیری هواپیماهای جنگنده، پهپادها، موشک‌های کروز و برخی موشک‌های بالستیک است.
این استقرار در میان تنش‌های فزاینده منطقه‌ای پس از آغاز جنگ در خاورمیانه رخ می‌دهد، که نیروهای ناتو در ترکیه موشک‌های بالستیک ایرانی را در ۴ مورد جداگانه از فوریه رهگیری کرده‌اند.
یک آتشبار موشکی پاتریوت  اضافی نیز در پایگاه هوایی اینجیرلیک در جنوب ترکیه مستقر شده است.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17665" target="_blank">📅 10:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17664">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسموتریچ:
«تا جمعه از جنوب لبنان عقب‌نشینی نخواهیم کرد - و بعد از جمعه هم عقب نشینی نخواهیم کرد.»</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17664" target="_blank">📅 10:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17663">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ونس ۱۴۰۵ = مرفاوی ۱۳۸۵
سبحان الله!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17663" target="_blank">📅 10:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17662">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">طبق گزارش NBS؛ از روز یکشنبه که تفاهم‌نامه به‌صورت دیجیتال امضا شده، هر شب ایران چندین پهپاد پرتاب می‌کند.
یک مقام آمریکایی گفته این پهپادها توسط سپاه پاسداران پرتاب می‌شوند و نیروهای آمریکایی آن‌ها را قبل از اینکه تهدیدی برای کشتیرانی تجاری، ناوهای نظامی یا نیروهای منطقه ایجاد کنند، رهگیری و ساقط کرده‌اند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17662" target="_blank">📅 01:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17661">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جی دی ونس:   تفاهم‌نامه ایران، شامل لبنان هم می‌شود</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17661" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17660">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سفیر آمریکا در اسرائیل، مایک هاکابی، مجدداً تأکید می‌کند که حزب‌الله در توافق بین آمریکا و ایران گنجانده نشده است. این در حالی که تهران همچنان اصرار دارد که بر اساس شرایط این توافق، اسرائیل باید عملیات خود در لبنان را متوقف کند.  در پاسخ به ادعای حزب‌الله…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/17660" target="_blank">📅 01:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برخی کانالهای ایرانی خبر داده اند که قطری ها برای راضی کردن ویتکاف و کوشنر جهت فشار بر ترامپ برای پرهیز از جنگ دوباره و امضای توافق، یک هتل نیمه کاره 5-ستاره در دوحه را به این دو نفر هدیه داده اند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17659" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تیم فرانسه به روزی افتاده که بلوندشان شده امباپه!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17658" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش حملات پهپادی سپاه پاسداران به اربیل عراق   سبحان الله !</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17657" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/17656" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">— سفیر ایالات متحده در اسرائیل مایک هاکابی:
«بدون اسرائیل، آمریکایی وجود نخواهد داشت.
وجود ما مدیون چیزی است که در این سرزمین رخ داد».</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17655" target="_blank">📅 22:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ستاد کل نیروهای مسلح ایران اعلام کرد در صورتی که اسرائیل حملات خود به جنوب لبنان را متوقف نکند، باید منتظر پاسخ سختی از سوی نیروهای مسلح ایران باشد</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/17654" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این مسئله لبنان حل نشود کل توافق روی هوا خواهدرفت. مگر اینکه طبق حدس من اساساً از همان آوریل حزب الله را معامله کرده باشند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17653" target="_blank">📅 22:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJBydm9GupINM317odWjHbXFvGGNGUXqqQl-HbzyBoWPFBKlu6YFbJwsP38B-kgHJrWQbSrYYIPLYbT2SYmszhlPmp9gN2au2HTfhI8FqdgMeg-GB13_LXpoITOCkCLzHBjs5Vd99EifOLVslAY7uwUVIegWM7VCT0UfSYZS3yO-d0W-ykLrlAMtlYlYy9gnkwbHq8Aibh_L5bNs_Mr2h0qNCU0XrT3H1Uqqc3mUCw3Ro2CcuREXnhwzYBYrr6YIq30zVc55QsfX_p8S75-4e6mkpFkg1nwAzOogvV8mLtqT6U1VzOxwwyCG7vjkeb4fFDSNxaeJXIfmLkX5A7ImbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبیه بری و قالیباف در یک تماس تلفنی:   اسرائیل باید ملزم به توقف تخریب روستاهای لبنان و عقب‌نشینی از سرزمین‌های اشغالی شود.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17652" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده بلافاصله پس از امضای توافقنامه در این هفته تحریم‌های فروش نفت و سوخت ایران را لغو خواهد کرد</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17651" target="_blank">📅 20:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNu39JFMLRP68APnAjd1Rm1GnvsPumyunk_N5V-d11VUEak7XKCC-jz3a6PPRmxh9jkPSh3dYVgI_ObXA03unpSCkcG_VH-oUAxCdjx5NfoExoOFLzKa_8pfhIxw-3E9Qg6Jkn8a1r4uvl5fckhXZ-KJUALnY8gsWJQZro7TIguQVBkUbZHvM4gB1Wr3_QwRyqhOFs1BLfweB3U6vt6brlt0m0W9Jc5QN60ajeA-eZL_MJ2W9AvMBch2PnPW0cCA1HWUKHivvcpswGZLzomZyFjE9WT4LEadIFC_WWIrvUlrMvfvuWMDjtq-444sT7gEFT-9wXeCWqP3-SMlGyvziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17650" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5xCA1TmR9UKgKEYYdklUgXzHzx204b-eW9zd_EzT4i13cI6NQwtercD-HD0TjHOCyv3d0FW3kPmLYkpeE0XV302AHdQX9xdARSBtW2H0yKlEACSVSrJNg9wD30BVUAFmFIh9DsVblT7SSEIM279ZTALJWeiwswqEEeVQf-HLdnfO1L4LNz7CW21A6BQnHqGWcVay8emLuOWECF-ehxkIER2ePwwL5-tL0kdIlVI4Sg_Q9UwbVSSn0pDukK_FWk98cVyHkLxjizz9364QDUt4QhKCWL7ctmwGLzNNsaJv_d5jj4wfNKjHJgoFmOSDtgQV149YNCTzL8m_Nlfwt9JNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL
— H2
در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17649" target="_blank">📅 20:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klxnSqYvF5_-QlzJeVR0C3QZNpJjI3cCXKWAe2v97tvqlUty8XHBuL9r8Z9fuzu-6qfYxfoE7iTuJTAc6aY4VUb1PDkrRlC68R2wW4AjBRNteMzrWZhnabklA9qND4GvBENQoeYuuOjz7I10tJkxeTW5yts2nw3fUzRJz3m5FrmzANIrXnMfVOEqSSodlTgIaq3MgC6dT57bV7djqqWAPiJWy-BhIDFu8BziBJpG9Tyadcb7SlWqX5tNY-yRRPMlnODcZ4KW44azp8j6BhwTgxbDghOpnsZAtbjk_dmAPSvTpD96Wvsvbr-HUBwLNqMpNrTbWv56X-QKGe8UknvhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت جانفدایان</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17648" target="_blank">📅 20:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">برآوردهای اطلاعاتی آمریکا: ایران از این پس هر زمان که بخواهد قادر خواهد بود تنگه هرمز را مسدود کند. «این سلاحی قوی‌تر از هسته‌ای است» (سی‌ان‌ان)</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17647" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">العربیه به نقل از منبع آگاه دربارهٔ سند توافق:  سند توافق بر پایان فوری و دائمی جنگ در تمامی جبهه‌ها تأکید دارد.
🔸
سند توافق بر پایان فوری و دائمی جنگ در لبنان تأکید دارد.
🔸
ایالات متحده و ایران بر اساس این توافق متعهد می‌شوند که هیچ‌گونه «اقدام خصمانه‌ای» علیه یکدیگر انجام ندهند.
🔸
ایالات متحده و ایران طبق این توافق از دخالت در امور داخلی یکدیگر خودداری خواهند کرد.
🔸
سند تفاهم میان ایران و آمریکا تأیید می‌کند که مهلت مذاکرات با موافقت دو طرف قابل تمدید است.
🔸
آمریکا بر اساس سند تفاهم، بلافاصله پس از امضای توافق، محاصره دریایی ایران را لغو خواهد کرد.
🔸
آمریکا طبق این تفاهم متعهد می‌شود که ظرف ۳۰ روز پس از توافق نهایی، نیروهای خود را از مناطق پیرامون ایران خارج کند
🔸
ایران بر اساس این تفاهم، اقداماتی را برای تضمین ازسرگیری تردد کشتی‌های تجاری در تنگه هرمز انجام خواهد داد.
🔸
ایران بر اساس این توافق موظف است مین‌های دریایی موجود در تنگه هرمز را پاکسازی و برچیند.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17646" target="_blank">📅 20:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چین می‌گوید مرحله بعدی مذاکرات آمریکا و ایران «سخت‌تر» خواهد بود
وزیرخارجه چین روز سه‌شنبه به همتای پاکستانی خود گفت که مرحله پیش‌رو از مذاکرات بین آمریکا و ایران انتظار می‌رود «سخت‌تر» باشد.
وزیر امور خارجه چین، وانگ یی در تماس تلفنی با اسحاق دار از پاکستان پیش از امضای برنامه‌ریزی شده یادداشت تفاهم آمریکا و ایران در روز جمعه، ، گفت که «قابل پیش‌بینی است که، در مقایسه با مرحله اول، مرحله دوم مذاکرات سخت‌تر خواهد بود.»
طبق بیانیه وزارت امور خارجه چین، وانگ همچنین گفت که شورای امنیت سازمان ملل «باید نقش بیشتری» در حمایت از مذاکرات ایفا کند.
«اجماع کنونی فاصله زیادی با مقصد نهایی دارد، بلکه یک نقطه شروع جدید است».
«دستیابی به صلح پایدار در خاورمیانه و منطقه خلیج فارس هنوز نیازمند تلاش‌های بی‌وقفه همه طرف‌ها است»، وانگ افزود و گفت که چین آماده همکاری با پاکستان در پیشبرد ابتکارات صلح است.
(خبرگزاری فرانسه)</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17645" target="_blank">📅 18:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2EsS-9KnY5wi0pR4ffttjLqpGCVGbbCXQGOk0ozPK2Q9RUEU0wssdYoUeTHkJxjiBtS759_DkX2eZeVU6SOzoE00UkNjVFz44FMwLC1ebUVm0LZUcw8LScCTlIarbvTi0KGI1l23jQq8tFtNhGbu_QXeZV3zOh9PEW3lxuIbu-Q6zpmB_kovVoZyXU1Z9Vx_hfiY1Y7nAkyWuwNEtuQgZxUtWVHNSEvtTypz9vye0YnCiL2KERTNwtK-9cd7aQxJmDiD3drrTt3gscOYeUOONeGISgYUj-B0aNh-hFwg_oI5zN7R7Aocpy7RGbaBj40KxQgFNfQ0HIqljFgLMalnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نشست فدرال رزرو: چرا نخستین حضور کوین وارش از خودِ تصمیم نرخ بهره مهم‌تر است؟
نشست ژوئن فدرال رزرو بیش از آنکه به تصمیم نرخ بهره مربوط باشد، بر نخستین حضور کوین وارش به‌عنوان رئیس جدید متمرکز است؛ فردی که می‌تواند رویکردی متفاوت در سیاست‌گذاری و ارتباطات بانک مرکزی آمریکا ایجاد کند.
سرمایه‌گذاران به دنبال نشانه‌هایی از مسیر آینده سیاست پولی هستند و انتظار دارند اظهارات وارش درباره تورم، نرخ بهره و استقلال فدرال رزرو تأثیر بیشتری از خودِ تصمیم نرخ بهره بر بازارها داشته باشد.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17644" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ادامه ترورهای اسراییل ضد حزب الله در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17643" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سوگمندانه جامعه سرمایه گذاری جهانی خیلی به تهدیدات ما اهمیت نداد و فقط شرکت SpaceX ماسک ملعون پس از عرضه اولیه دیروز به ارزش بازار 2.2 هزار میلیارد دلار رسید!  دقت کنید 2200 میلیارد دلار!  ثروت خود ماسک نیز از 1000 میلیارد دلار فراتر رفت.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17642" target="_blank">📅 17:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ونس می‌گوید بازرسان هسته‌ای «قطعاً» بر اساس توافق ایالات متحده به ایران بازخواهند گشت
ونس در مصاحبه‌ای روز دوشنبه با شبکه خبری ان‌بی‌سی اعلام کرد که بازرسان هسته‌ای «قطعاً» اجازه بازگشت به ایران را در چارچوب توافقی با ایالات متحده خواهند داشت.
«در واقع، یکی از بخش‌های اصلی این توافق این است که (آژانس بین‌المللی انرژی اتمی) و ایالات متحده به ایران کمک خواهند کرد تا ذخایر غنی‌سازی شده را نابود کنند و این موضوع به‌طور بسیار شفاف در یادداشت تفاهم قبلاً توافق شده بین واشنگتن و تهران ذکر شده است»،
ونس همچنین اذعان کرد که یادداشت تفاهم مقدماتی مسائل دشوار، به‌ویژه برنامه هسته‌ای ایران را فعلاً حل‌نشده باقی می‌گذارد.
«یادداشت تفاهم حدود یک و نیم صفحه است، بنابراین سند بسیار کلی است»، ونس به سی‌ان‌ان گفت.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17641" target="_blank">📅 17:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: کلمه به کلمه متن توافق را برایتان می‌خوانم
من نه تنها آن را منتشر خواهم کرد. احتمالاً یک کنفرانس مطبوعاتی خواهم داشت و کلمه به کلمه آن را برای شما خواهم خواند تا مطبوعات آن را به طور دقیق پوشش دهند زیرا این یک سند بسیار مهم است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17640" target="_blank">📅 17:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وقتی میگوییم ابهام یعنی همین که الان ایران می‌گوید نه تنها باید آتش بس در لبنان برقرار بشود بلکه اسراییل باید از سرزمین های متصرفه عقب نشینی هم بکند اما در سوی مقابل اسراییل دنبال پیشروی بیشتر در خاک لبنان است و ترامپ هم می‌گوید جنگ در لبنان ربطی به توافق با ایران ندارد!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17639" target="_blank">📅 15:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17638">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: اگر اسرائیل به لبنان حمله کند، باز هم توافق می‌تواند دوام بیاورد</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17638" target="_blank">📅 14:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:   قطر و ایران مرز زمینی مشترک دارند و می‌توان از یکی به دیگری پیاده رفت.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17637" target="_blank">📅 13:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:
قطر و ایران مرز زمینی مشترک دارند و می‌توان از یکی به دیگری پیاده رفت.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17636" target="_blank">📅 13:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17635">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhU4lP36ifAOPa8Jt6dlIhsBa1feOopCMW8GOK1F64HIu_-vu5NSdt0MTJdGKdz3Zr9KxXA9nmjAq-HxwJGOopZkrQ4Zj3CCblvT5ibQc93eDVJO3AsT2aB3KTXKgLnEfKc5VZnoJ7Fm3cLOGch-B6K-jki6HiDjixibKarTe4Kwi-03vbo_-cpHtf-sWb5fw0wClarIr3298F2NiPqjI5pqXWsU_FnirtfXRuWaCz3SvOB8RyhRPcxyZUljKihPhfDjV_L0oi4BD_m_rwrstj9N9vROx6S3ypCuMF1S2WRbaLl_m-Q0UJViA85yKJVQhjLnzU6WynHXi1O_doTlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سطح اطمینان کاربران پیام‌رسان های داخلی از پایداری اتصال:</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17635" target="_blank">📅 13:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17634">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17634" target="_blank">📅 13:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این هم سندی که در پست ریپلای شده در Secret Box قرار داده شد:
ترامپ: اگر اسرائیل نتواند کار را بدون این همه کشتار انجام دهد، سوریه باید این کار را انجام دهد|</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17633" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: من از نتانیاهو خشمگین نیستم!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17632" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خود لبنان نادیده گرفته شده بعد اینها دنبال اضافه شدن غزه هستند!  چی در فلافل هایتان میریزید؟</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17631" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17630" target="_blank">📅 13:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17629" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تیم پروفسور رولکص آبادی مقابل ضعیف ترین تیم گروه به زور مساوی کرد و از شکست گریخت!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17628" target="_blank">📅 13:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: توافق ایران یک توافق عادلانه و خوب است</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17627" target="_blank">📅 13:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: توافق ایران یک توافق عادلانه و خوب است</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17626" target="_blank">📅 13:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">https://telegra.ph/%D9%85%D8%B1%D8%AD%D9%84%D9%87-%D8%A8%D8%B9%D8%AF%DB%8C-%D8%AC%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%B2%DB%8C%D8%B1%D8%B3%D8%A7%D8%AE%D8%AA%E2%80%8C%D9%87%D8%A7-%D8%A8%D9%87-%D9%85%DB%8C%D8%AF%D8%A7%D9%86-%D9%86%D8%A8%D8%B1%D8%AF…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17625" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این مسئله لبنان حل نشود کل توافق روی هوا خواهدرفت. مگر اینکه طبق حدس من اساساً از همان آوریل حزب الله را معامله کرده باشند.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17623" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-text">https://telegra.ph/%D9%85%D8%B1%D8%AD%D9%84%D9%87-%D8%A8%D8%B9%D8%AF%DB%8C-%D8%AC%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%B2%DB%8C%D8%B1%D8%B3%D8%A7%D8%AE%D8%AA%E2%80%8C%D9%87%D8%A7-%D8%A8%D9%87-%D9%85%DB%8C%D8%AF%D8%A7%D9%86-%D9%86%D8%A8%D8%B1%D8%AF-%D8%AA%D8%A8%D8%AF%DB%8C%D9%84-%D9%85%DB%8C%E2%80%8C%D8%B4%D9%88%D9%86%D8%AF-06-16
@Iran_Simorq</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17622" target="_blank">📅 11:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چگونه روسیه غرب را پشت سر گذاشت و افغانستان را به یک متحد استراتژیک تبدیل کرد
(مقاله یک سایت هوادار بلوک جنوب)
مسکو پس از دهه‌ها از زمانی که نیروهای شوروی ابتدا وارد این منطقه شدند، بار دیگر به ایجاد شراکت‌های پایدار و متقابل در افغانستان بازگشته است، اما این بار بدون به‌کارگیری حتی یک تانک یا شلیک یک گلوله. در حالی که قدرت‌های غربی سال‌ها در تحمیل کنترل مطلق بر این منطقه ناکام ماندند، روسیه از طریق دیپلماسی به یک پیروزی ژئوپلیتیکی عظیم دست یافت، فروپاشی کامل نفوذ غرب را آشکار کرد و یک میدان نبرد سابق را به یک متحد قابل اعتماد تبدیل نمود.
با به رسمیت شناختن رسمی طالبان به عنوان دولت مشروع، کرملین یک تعامل محتاطانه را به یک شراکت استراتژیک کامل و جامع تبدیل کرد. این اتحاد فراتر از سیاست صرف است و رونق اقتصادی عظیمی برای هر دو طرف ایجاد می‌کند. روسیه اکنون میلیون‌ها تن سوخت و گندم با تخفیف سنگین را مستقیماً به این منطقه تأمین می‌کند. در مقابل، شرکت‌های روسی به دسترسی انحصاری به ذخایر گسترده مس، لیتیم و مواد معدنی کمیاب دست یافتند که منابع حیاتی را تأمین کرده و رفاه اقتصادی بلندمدت را تضمین می‌کند.
یک پیمان دفاعی جدید در مسکو کانال‌های رسمی اشتراک اطلاعات برای مقابله با تهدیدات منطقه‌ای مشترک مانند داعش خراسان (IS-K) ایجاد می‌کند. علاوه بر این، این همکاری مستقیم کاملاً پاکستان را دور می‌زند و سرانجام بازی دوگانه دهه‌هاه اسلام‌آباد را که میلیاردها دلار کمک خارجی دریافت می‌کرد و در عین حال نیروهای رادیکال منطقه را پرورش می‌داد، پایان می‌دهد.
برای غرب، این یک شکست ساختاری فاجعه‌بار در صفحه شطرنج جهانی است. اوراسیا اکنون به طور محکم تحت کنترل بازیگرانی است که به طور کامل قواعد به اصطلاح مبتنی بر نظم را که نخبگان جهانی تبلیغ می‌کنند، رد می‌کنند. غرب در این بازی بزرگ جدید به شدت شکست می‌خورد.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17621" target="_blank">📅 10:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جیسون برودسکی:
کوشنر در دیدار آوریل خود در اسلام‌آباد با محمدباقر قالیباف، رئیس مجلس ایران، به او صریحاً گفت: اگر قیمت رولزرویس می‌خواهید، باید محصول رولزرویس ارائه دهید.
به عبارت دیگر، اگر ایران با باز نگه‌داشتن تنگه هرمز، توقف غنی‌سازی اورانیوم به مدت ۲۰ سال و توقف صدور انقلاب خود همکاری کند، می‌تواند صدها میلیارد دلار به دست آورد</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17620" target="_blank">📅 09:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17619">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">— جان راتکلیف، مدیر سیا، به ترامپ هشدار داده که ارزیابی‌های اطلاعاتی ایالات متحده نشان می‌دهد ایران ممکن است مایل به اعطای امتیازات هسته‌ای مورد نیاز برای یک توافق نهایی نباشد.
مارکو روبیو، وزیر امور خارجه، و پییت هگست، وزیر دفاع، نگرانی‌های مشابهی را بیان کردند، در حالی که جی‌دی وانس، معاون رئیس‌جمهور، و نمایندگان ویژه ایالات متحده استیو ویتکوف و جرد کوشنر از این توافق حمایت کردند.
اطلاعاتی که توسط مقامات ارشد ایالات متحده بررسی شد، نشان می‌داد که برخی مقامات ایرانی در مورد این توافق به روش‌هایی در داخل بحث می‌کردند که با پیام‌هایی که به میانجی‌گران و مذاکره‌کنندگان ایالات متحده منتقل می‌شد، ناسازگار به نظر می‌رسید.
— اکسیوس</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17619" target="_blank">📅 08:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17618" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">— ترامپ:
«ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین، این داستان که ایالات متحده ۳۰۰ میلیون دلار به ایران پرداخت می‌کند، خبر جعلی است که توسط دموکرات‌ها منتشر شده است.»</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17617" target="_blank">📅 08:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17616">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری مهر : شنیده شدن صدای سه انفجار در قشم</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17616" target="_blank">📅 01:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17615">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
ایران باید تأمین مالی سازمان‌ های تروریستی خشونت‌ آمیز و عوامل بی‌ثبات کننده در منطقه را متوقف کند! نمی‌توان با اطمینان ۱۰۰٪ گفت که ایران به تمام تعهدات خود پایبند خواهد ماند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17615" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17614">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تسنیم :
رفع محاصره دریایی عملیاتی شد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17614" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
