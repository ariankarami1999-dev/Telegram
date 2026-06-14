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
<img src="https://cdn4.telesco.pe/file/Cxwcb5h3xAUcTM3S3ZxSOXY_zDksSkslmAMShTJn8_MoJi6LrACJ5KgesmVPd1tZXy7MxtRrlcTtuLs0CZb5WTCr7G2-LUx87UnJk6lG7csZ_8ft9pR24cAcbEWPpAbwSMT82nGRFfBNzgnc33YJ2oFveBUKV8IXJOLQ-Re6DLgvy0yFFBgORy-L910On3sYG5oOLYdFzM2KkBQRu0aYwLqsgAJ1rgS65z43V5NVdKyJJbLeBTi6bfstVvsj476rJ-PBMUQhTuY6h2aVETq0lsAUV5ivXV98L4ySOikw8yUveEtZT8fCi08gHBK-x4Jh9-KE6lZrxY2dsFU_SoUFIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 03:12:55</div>
<hr>

<div class="tg-post" id="msg-17568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJfb2ISsVLVbwf5CbmK0JUXLiPjao8wpPC1kWzpwdv-WWmXv9Aqp3UeoApV-IiFwugTIXntGyMtRzWKoESweGqtLaI3nd3U65NT-QSIhjFhWTph23oQX4rMlWxrTXyr2SHl-Tm9abq0vwxhFegTC_0dca2QdsmY8XtCKa0QjGw5XAnZAw39Ropu4a0KSzV8lnOmm23EibmL-SgTNlElbPN5AzZ5egCxCVzH_K3fVJd5e4ihMNLhhF3C-Ip9sN8m1VFH9-I7Gsnw0nacWUk7MQlhxj8kdAiuwwXCinfaNslwguhO8YqeutLAZHBwz3GnjQRe7Swoi9AwVHP_jj5-P1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه:
لغو تمام تحریم های ایالات متحده و قطعنامه های سازمان ملل جزو دستورکار مذاکرات ۶۰ روزه خواهد بود</div>
<div class="tg-footer">👁️ 993 · <a href="https://t.me/SBoxxx/17568" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نایب رئیس وزارت خارجه ایران: پایان فوری و دائمی جنگ و اقدامات نظامی در جبهه‌های متعدد، از جمله لبنان، باید از امشب اعلام شود|</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SBoxxx/17567" target="_blank">📅 01:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آخرش هم گفته بچرخ تا بچرخیم!</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/17566" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فعلا که خبری نیست. فکر کنم آقای دکتر لانچر خودشان را فقط آماده کرده اند.  سبحان الله!</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SBoxxx/17565" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ
:
معامله با جمهوری اسلامی ایران اکنون تکمیل شد. تبریک به همه! من در اینجا به طور کامل افتتاح بدون عوارض تنگه هرمز را مجاز می‌کنم و همزمان، لغو بلافاصله محاصره دریایی ایالات متحده را مجاز می‌کنم. کشتی‌های جهان، موتورهای خود را روشن کنید. اجازه دهید جریان نفت آغاز شود! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/17564" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alKG3NdNGIhJ2AB9KdgvT4vpN_39DgYHPj5Vf_O_5fdC17ak8p2DkkYL20ZnHXniZckjdhvyGe5d7Zcfq99R4ct5ffrhbVCfVtJuJPwEGPqbpTNYbSRQWJ7EKTBslc-y2bJJOHpkMo9uLQCSMVtQru5dEjo79RWS19vWiNOTaVDFnExyoks1zZ_qPgJmNm0TfwNot__b96T3rxZ-c-dg0bPZeDkjpDszRk4uIKZ1XVVdMdyU0fLYSRNP5LZC4gSDLXYrJDXBpswFYb71ChgVgz6SGeKgiQiDgAVJZ65RawylNv-EeiBvzBdcDldd8Mcy_ovacx1x3rwgVUSfr0rrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام نخست وزیر پاکستان، توافقنامه پایان جنگ جمعه ۱۹ ژوئن در ژنو امضا می شود</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/17563" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ
:
بعد از ترور رهبران رده اول و دوم در ایران، رهبران رده سوم فعلی منطقی‌ترین افراد در برخورد با ما هستند.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/17562" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/17561" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: ایران در توافق پولی دریافت نخواهد کرد، اما ممکن است تحریم‌ها تسهیل شوند - WS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/17560" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/17559" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش روزنامه‌نگار اسرائیلی رونن برگمن از ی‌نت:
پس از حمله ارتش اسرائیل به ضاحیه و تهدیدهای ایران مبنی بر پاسخ موشکی، به نظر می‌رسد تهران در حال بررسی به تعویق انداختن پرتاب موشک است تا به ترامپ فرصت دهد که توافق‌نامه چارچوب را امشب نهایی کند.
به عنوان بخشی از مشوق‌های این توافق، به نظر می‌رسد ترامپ در حال بررسی لغو فوری — نه تدریجی — محاصره دریایی ایران و تنگه هرمز است.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/17558" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کله زرد :
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/17557" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/17556" target="_blank">📅 00:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز معلوم نیست این فاکستانی ها چه غلطی کرده اند !
احتمالا دوباره نسخه ای که به ایرانی ها داده اند با نسخه ای که به آمریکایی ها داده اند متفاوت است</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/17555" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این فاکستانی ها چه موجوداتی هستند که نه آمریکایی ها به آنها اعتماد دارند نه ایرانی ها!  سبحان الله!</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/17554" target="_blank">📅 00:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFRhaQn3ZYu499C0eJU4091bkGb3XiiPDdO1K7OTkvUQ3-H5vfpvD8h5AcQ8xba1FsdPxSCnrIZlCdgDd13bsZpvXq29MFZb2tgrzd0Ne_6egSofB2D5EK2ZCp4H2sTLH6ah1J8rnls8b6A1OK_4Aa_5NciJ_mZWDgU0amtuauyuIx_0vmPq85BDFWVAWUOq1U8BMpNPzvx5Eg1ShnVQKY01gdZuf4GsdckNYM0d0i7Aa-b3tzENWtYNkOpBhsloLihoS62oj65pV3U7L1LfkKonc6neOUAjwa7u8bXHDuIH54HzzlSGDUfHJgeNleppEMk4dxjzC9icd0C1JlkVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.
دو مورد که مدنظر من است:
— همون همیشگی (حمله به اربیل)
و|یا
— سپردن کار به بچه های نقطه زن یمن
در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه باشید.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/17553" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">علی اکبر ولایتی:  یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/17552" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">علی اکبر ولایتی:
یک اشتباه محاسباتی در بیروت، صبر را به پایان رساند و دستور حمله صادر شد، ساعت صفر فرا رسیده و پرتابگرهای موشک بالستیک در حال آماده‌سازی هستند.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/17551" target="_blank">📅 23:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ونسِ ترنس در بحبوحه تنش‌های فزاینده با ایران به کاخ سفید شتافت!</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/17550" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:   هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.  نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/17549" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی سازمان هواپیمایی کشوری:
هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است. / مهر</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/17548" target="_blank">📅 22:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ینت اسرائیل:
دونالد ترامپ از نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌ نشینی نیروهای ارتش اسرائیل نماید تا ایران پاسخ ندهد، اما نتانیاهو هر دو درخواست را رد کرده است.</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/17547" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قالیباف:   آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/17546" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">قالیباف:
آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/17545" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/17544" target="_blank">📅 22:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نمیدانم که میزنیم یا نه اما میدانم اگر بزنیم آنها هم میزنند و بد هم میزنند</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/17543" target="_blank">📅 22:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خداوکیلی از دیوار هم صدا درمیاید از رییس جمهور مملکت نه!
بلند شو یک چیزی بگو مرد!</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/17542" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فوری | محمد مخبر، مشاور رهبر ایران: به متجاوزان درسی خواهیم داد که پشیمان شوند.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/17541" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-poll">
<h4>📊 امشب:</h4>
<ul>
<li>✓ میزنیم!</li>
<li>✓ نمیزنیم!</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17540" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17539" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17538" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این مقر موساد در اربیل مثل درهای بهشت است
هیچ وقت تمام نمی شود</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17537" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مقر موساد در اربیل؟!</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17536" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محمدباقر ذوالقدر: لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد
پاسخ رزمندگان اسلام در پیش است. وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17535" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMHAiPn-LoGWpIz-juYbSOI-7kc3DUF6NvNUeZlTEn-sDqRehnIoWa3apfgUoVwkhtBi_jl1JiOM2cAWRVBfpBYyaVnpjcuxiuVEaSUFqa7RJx7YrjkZC05uFXizDzkSsxAnkQT0u99Tmv5sdpU-kw1S7sb7usaf4SHimjDpG2zZnOjKNgRxapsxGPg_iqdGsVeL3k5zRyzzf-N3PaBsNGv9Ll5vCZ3QL0JNqJX-oHydCoh8L9OjiQa4gG4uZVaXjGEXgi68BFNOCwiw6jPzKCW_XAdGCsa-i-4rggQyjepOSmVrSNVKu_VM5lYUNj9M49F0K9g4-wJ2-1W7sePf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17534" target="_blank">📅 21:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">«کانال ۱۳»: ترامپ با کلمات تند از جمله برخی ناسزاها به نتانیاهو حمله کرد</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17533" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17532" target="_blank">📅 20:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):
«انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.
ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17531" target="_blank">📅 20:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اصابت موشک حزب‌الله به شهرک کریات شمونه
منابع خبری متعلق به شهرک‌نشینان اسراییلی از اصابت حداقل یک فروند موشک به شهرک کریات شمونه در شمال اسراییل خبر دادند.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17530" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17529" target="_blank">📅 20:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17528" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.  ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.  — شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17527" target="_blank">📅 19:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.
ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.
— شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17526" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آماده‌سازی حمله گسترده ایران به اسرائیل
اینتل واچ: یگان‌های هوافضا و دریایی جمهوری اسلامی ایران در حال آماده‌سازی یک حمله گسترده به اسرائیل هستند. بر اساس این اطلاعات، فرماندهان ایرانی از یک عملیات پنج‌مرحله‌ای با روندی تشدیدشونده سخن می‌گویند.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17525" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:  «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود،…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17524" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ:
«حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود، مجروح یا کشته نشده بود، و نباید این روند مهم را مختل کند.
ما بسیار به توافقی نزدیک هستیم که صلح را به منطقه از جمله لبنان خواهد آورد و همه طرف‌ها باید از اقدام خودداری کنند.
نباید حملات بیشتری از سوی اسرائیل در هیچ‌کجای لبنان انجام شود، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری از جمله حزب‌الله علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد، بیایید آن را خراب نکنیم</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17523" target="_blank">📅 18:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17522">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طبق گزارش خبرگزاری فارس، منبعی نزدیک به
تیم مذاکره‌کننده ایرانی، تنها چند ساعت پیش از حمله اسرائیل به ضاحیه، فاش کرد که تیم میانجی‌گری قطر در حال حاضر در تهران حضور دارد و بندهای مورد نظر ایران و جزئیات مشخص را به طرف مقابل منتقل می‌کند.
این منبع تأکید کرد که هیچ چیز نهایی نشده است و فرآیند مذاکره را دارای فراز و نشیب‌های قابل توجه توصیف کرد و بر این نکته تأکید ورزید که شرط بنیادین ایران این است که تمام ملاحظات آن در هر توافق نهایی به طور کامل منعکس شود.
این منبع افزود که حتی اگر تمام دیدگاه‌های ایران گنجانده شود، در زمانی که دونالد ترامپ اعلام کرده است، هیچ توافقی امضا نخواهد شد. این اظهارات پیش از حملات اسرائیل به ضاحیه بیان شد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17522" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ارتش اسرائیل برای احتمال آتش‌باری به سمت اسرائیل در ساعات آینده آماده می‌شود</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17521" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مرندی :
فعلاً مذاکره دیگری در کار نخواهد بود.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17520" target="_blank">📅 17:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">معاون قرارگاه خاتم الانبیاء گفته ایران به حمله اسراییل به ضاحیه پاسخ خواهدداد</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17519" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17518">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برخی منابع نظامی نویس ایرانی:
به نظر می رسد فرماندهی موشکی هوافضا در حال آماده سازی یک حمله گسترده تر از عملیات "اخطار" و "نصر" می باشد.
- اگر در سایر موارد مسئله ای دخیل لغو عملیات نشود، شاهد شلیک از مرکز و غرب کشور خواهیم بود.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17518" target="_blank">📅 16:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17517" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17516" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قالیباف :
تجاوز صهیونیستها به ضاحیه بار دیگر نشان داد که آمریکا یا اراده عمل به تعهدات خود را یا توانایی آن را ندارد
با چراغ سبز نشان دادن به رژیم، نمیتوانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب، دیگر کهنه شده است.
اگر اراده و توانایی عمل به تعهدات خود را ندارید، صحبت از ادامه این مسیر به سادگی ممکن نیست.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17515" target="_blank">📅 16:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تلویزیون ایران به نقل از مسئول سازمان مدیریت تنگه هرمز در خلیج فارس: تنگه هرمز تا اطلاع ثانوی بسته است و اجازه ورود یا خروج به هیچ کشتی خارجی داده نمی‌شود</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17514" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیم ساعت پس از حمله در بیروت، گزارش شده که یک عملیات هدفمند دیگر انجام شده و این بار در شهر صور</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17513" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17512" target="_blank">📅 14:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17511" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=rZ_2TN20TNzwylndhTYFhpsm3Lza75RFUfeMu6LYzXAwRzc2XiLZSCNcZeRU9KIgQeWatxWi0Vm3B3Cr8fIJE4MuRAr6bouW6PoGLGiRVDcUah1euLddTiTe5wbmqsOXjWZ1AuE_fpQTyydHATMOLV1SjdQPWeC-AKdpsizaA-tsaX7fQKXuyVN30CVgjvBaOdYA0M6w_3OaQ6youS4BNYPlL7-8kgqYMPVFoWhIJ-W1K1_opk5SLTpTE7maTHkQEF0MzW-NFbvIZnK_Ir37hy7QbvF-AA807HH0pwgATffNeKur-hV678Dt4tC-gEc-heVf-oMrsyLrwvu1KPgQgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=rZ_2TN20TNzwylndhTYFhpsm3Lza75RFUfeMu6LYzXAwRzc2XiLZSCNcZeRU9KIgQeWatxWi0Vm3B3Cr8fIJE4MuRAr6bouW6PoGLGiRVDcUah1euLddTiTe5wbmqsOXjWZ1AuE_fpQTyydHATMOLV1SjdQPWeC-AKdpsizaA-tsaX7fQKXuyVN30CVgjvBaOdYA0M6w_3OaQ6youS4BNYPlL7-8kgqYMPVFoWhIJ-W1K1_opk5SLTpTE7maTHkQEF0MzW-NFbvIZnK_Ir37hy7QbvF-AA807HH0pwgATffNeKur-hV678Dt4tC-gEc-heVf-oMrsyLrwvu1KPgQgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17510" target="_blank">📅 14:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864badacb8.mp4?token=ggvMF1rOsismGIYIxRylJm79GHP8pEOMWmePb-onBmSgMyexwS9qT1aS33NVv7DiNkVn0xRUzZHd4BZInE7jNvHtIgLJRnXJ08UX9YWqLiWTjPnXQKeobIu9Au1U7jAtbELvPg8qLq-tSQcHH0gEaSH_UazKEgvZ45YN60vS_tGi3d4UceGcWz-6_5QhDVMEEggw8Ir9bsw6k5BrqBeI4wsLiHK86iorK6cULMJjVtWkH9JZiJQNYjJGIq1mfd14vr3XTg1P3DCG7xcy_nCu0UZB3q3WZ746wbuuKQxjlRFkp9PB3y2vKYaa2ItWJEn8KLJx3whaSEiR_kcMvT2P5rEZY7EkVKzDmgzhDYdGMFx-7W641-WQ3U7RkhFzM7mGuREzaccpL-m3DbIPgTdyP1SNmCujS8J1grRld69dWNktCXLEV1VfsXIqqHjZogQkBeB8JirL2_K1noLS8iHkaywDplDO88uiCqyLdbpu1HxSy9DieobjzXBcSrBFF1xzjLBWJHUVHOJLlpI5RKOq4fGNSxlTHJv_hIm19wuVV_DvJ8jCB4aqg-wdPfmCx_r-NbO0fQmDyBOTJSDqbexD0b22ot1EFFTIGsLLFhXipYRVJK55BfR4mLuTpmyb9j08WfJ9j4ta-MQy3o9Q-zQrMcXGI6BwtJBqc386cSIuotc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864badacb8.mp4?token=ggvMF1rOsismGIYIxRylJm79GHP8pEOMWmePb-onBmSgMyexwS9qT1aS33NVv7DiNkVn0xRUzZHd4BZInE7jNvHtIgLJRnXJ08UX9YWqLiWTjPnXQKeobIu9Au1U7jAtbELvPg8qLq-tSQcHH0gEaSH_UazKEgvZ45YN60vS_tGi3d4UceGcWz-6_5QhDVMEEggw8Ir9bsw6k5BrqBeI4wsLiHK86iorK6cULMJjVtWkH9JZiJQNYjJGIq1mfd14vr3XTg1P3DCG7xcy_nCu0UZB3q3WZ746wbuuKQxjlRFkp9PB3y2vKYaa2ItWJEn8KLJx3whaSEiR_kcMvT2P5rEZY7EkVKzDmgzhDYdGMFx-7W641-WQ3U7RkhFzM7mGuREzaccpL-m3DbIPgTdyP1SNmCujS8J1grRld69dWNktCXLEV1VfsXIqqHjZogQkBeB8JirL2_K1noLS8iHkaywDplDO88uiCqyLdbpu1HxSy9DieobjzXBcSrBFF1xzjLBWJHUVHOJLlpI5RKOq4fGNSxlTHJv_hIm19wuVV_DvJ8jCB4aqg-wdPfmCx_r-NbO0fQmDyBOTJSDqbexD0b22ot1EFFTIGsLLFhXipYRVJK55BfR4mLuTpmyb9j08WfJ9j4ta-MQy3o9Q-zQrMcXGI6BwtJBqc386cSIuotc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی اسرائیلی ها از لحظه حمله به ساختمانی که ادعا می کنند ستاد برنامه ریزی عملیاتی حزب الله بوده است</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17509" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17508" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :
ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17507" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17506" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">العربی الجدید: تهران توافق را تأیید نکرده!
در پی سفر امروز هیئتی قطری به تهران برای گفت‌وگو در مورد یادداشت تفاهم، رسانه قطری العربی الجدید ادعا کرده که
ایران همچنان ملاحظاتی در مورد این متن یادداشت تفاهم دارد و هنوز تأیید نهایی خود را برای این توافق اعلام نکرده است.
العربی الجدید به نقل از یک منبع آگاه ایرانی نوشت که این منبع ا
حتمال امضای توافق در روز یکشنبه را منتفی دانسته
و تصریح کرده که همچنان گفت‌وگوها در مورد توافق در داخل ایران ادامه دارد و
موضوع به صورت کامل حل و فصل نشده است.
این منبع در عین حال تأکید کرده که ممکن است امروز توافق نهایی شود و تهران امروز تأیید نهایی خود را اعلام کند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17505" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگر نتانیاهو بخواهد تسلیم این توافق بشود (با این فرض که اساساً چنین توافقی وجود داشته باشد و امضا بشود یکشنبه)، عملاً سند مرگ سیاسی خود را امضاء کرد و سپس باید ریسک دادگاهی شدن و زندان را هم بپذیرد.  اما میدانید که نتانیاهو سرسخت و سمج است و بعید است به چنین…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17504" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbrY8Ese5N6bXt8cqn1T3ULpsdxR3NuveMLO0ht7_sFl55XLhya4YAlD3DbSKvKx5yrKCYxH52CYXZ_EXw6ZxQESF8JsvwO6xyi9Qd3bebUH9sD6Clt4kNI6Q-pJqYQzlcRynMvX3CPl7hPm-yq4VCsz0IgH-DlC0fV4YlmQF4UBogJDdMbD7wxi12h8ZKmYhhOAfdmRP1c-4k0aAj2FLCAc0A-SzBzfnR6y2VeJ73nYmjNzc6mzvnezwyMUrortH5H85avAUdbedQ_sn9ypFCWlaXiq-QJyYwjgpS_9riFwNYrjLB_y-6Oi31JSXsacDeR6dKW4p6pg0AsztqEMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17503" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17502" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668556cde.mp4?token=tSJl6r5UN57Y9xr_yZ4Bwcp1X1N07w9isx3whm9MADd7fS_nrGOCWZMmNAo7hqXbVGkPMzOcBGunzXbM0tmo_VIf7cvr68z3_x7w9-ADiME4R89RIDGWaq2wQOOxMXXocfTZC8M7JUSgB2pEdKt-JcB8zejPWk1kEhpSxt4EB0lRYCz7ab6ZFYNhIlVkHKXC_hgW21ttitx_dSoGohaVPCJeCeWq85-SxMwzsZB62Kvv2akwIlZisE505PAxZnTfrzvkhhVac4OAL3CbwEhZmyGVI3G9JswIhxN8osHOux1a6x2121i6T5yFVMLufnqIxJk1lz0OZfocmeB8oxLyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668556cde.mp4?token=tSJl6r5UN57Y9xr_yZ4Bwcp1X1N07w9isx3whm9MADd7fS_nrGOCWZMmNAo7hqXbVGkPMzOcBGunzXbM0tmo_VIf7cvr68z3_x7w9-ADiME4R89RIDGWaq2wQOOxMXXocfTZC8M7JUSgB2pEdKt-JcB8zejPWk1kEhpSxt4EB0lRYCz7ab6ZFYNhIlVkHKXC_hgW21ttitx_dSoGohaVPCJeCeWq85-SxMwzsZB62Kvv2akwIlZisE505PAxZnTfrzvkhhVac4OAL3CbwEhZmyGVI3G9JswIhxN8osHOux1a6x2121i6T5yFVMLufnqIxJk1lz0OZfocmeB8oxLyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوبی است.  باید تدریجاً هرات از هر جهت در بوم ایران ادغام بشود.  چرا وقتی نظم مسلط فروپاشیده و همه دنبال گسترش مرزهای خود هستند ما بنشینیم و به مرزهای جعلی استعمارساخته احترام بگذاریم؟!  هرات؛ نگینی بود که توسط ناصرالدین شاه حمال از دست رفت و هیچ قرابتی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17501" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUtZdrfZsrH7RFdmfw4M71_qK7V9mllaoyKfVaBLohwTs6LLQXZb7URupm4eu_FQeVVAUudk8HrfGhsRHdNNT7VIuEtEIihvfubXUSBNZVb-hmvLcrmvCkvxbCS_G-jxk-Aljg4gEniu1XeenVZbsRVI5dWA88lccNHeaivWy1LeSrz_IBq_lqzQhwgRoCUsYKGw7z3AOcif7hUzXpEf3Ss6vPA15YP_-KjCn2EoTFPIOSMZLe0FJgC6u4jLlijDM3xyvHi_fhxYc8eXvgMQPteBbyaPBUzKsTA52gy97uNDYCG5iOe_bLMjUsUX5t0XRUx0TOeCvP2HcYVsOe67uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هشتادمین زادروز این نکبت است.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17500" target="_blank">📅 11:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P09LO9JzlqbSYSWGnsbP75NTgghv3KrlmGSjBSnkJOLTKZsCmOUMWaXszu7O64A-ZYqASVdeIe9z-U4PhsslTSv68tdw4YfrQhi2ByBSTgxe4XMLtom0LUg9hO4MWqNKyE4qlvgT5sXqO7b_cIWxavu7qS2rvMMot96P-hwaKDoyJN5DIQSY_P5IkDgoniY-m2l6mLODakHU1DttHoTt4uwxvq8_UvlFBhCGnMk-eLo-tgzqzX3PicB2flAh01XYZrf7gC3QnNtLLbTeBCGp3066UbfbbA0UvyAIJrA8wAR3cWXMcvxvw7LygnmB4yey9JhvnrSHttcqI1E7odfQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنا به گفته دو منبع آگاه که با شبکه CNN گفت‌وگو کرده‌اند، عالی‌ترین فرمانده نظامی ایالات متحده اواخر ماه گذشته سفری محرمانه و فوری به مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا انجام داد تا به‌صورت حضوری در جریان طرح‌های ارتش آمریکا برای اعزام نیروهای زمینی به ایران و تصرف اورانیوم با غنای بالای این کشور قرار گیرد؛ ماده‌ای که مؤلفه اصلی و ضروری برای تولید یک سلاح هسته‌ای محسوب می‌شود.
این منابع گفتند جلسات توجیهی آن‌قدر فوری و حساس بودند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، ناچار شد در ۱۹ مه نشست مقام‌های ارشد ناتو در بروکسل را ترک کرده و به سرعت از آن سوی اقیانوس اطلس به تامپا در ایالت فلوریدا بازگردد. به گفته منابع، سطح بالای این جلسات و فوریت آن‌ها نشان می‌دهد که دولت آمریکا تا چه اندازه به صدور مجوز برای این عملیات زمینی پرخطر نزدیک شده بود.
سخنگوی ستاد مشترک ارتش از اظهار نظر درباره تدارکات مربوط به یک عملیات احتمالی خودداری کرد.
یکی از منابع نیز گفت که ژنرال کین پس از آن، رئیس‌جمهور دونالد ترامپ را در جریان گزینه‌های موجود برای انجام چنین عملیاتی قرار داد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17499" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تحلیل من همین است که ۳ هفته پیش ارائه شد و امشب یا فردا یک صوتی هم در این کانال قرار داده می شود.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/17498" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLMNNGojVaLb3sk7kjFDnlJ2pvnGpWvoCwFE5OhjW7K9rklJ1cIscLJrFnj6syuex05FVZn-2xuwBwf-ZaHxjmAPwIkzqsjUpAQZhhL5yRLbDtRB5I2bXvhO4JmYbAXTQBBLbBZcMGjr1N6yuMI_1-ySSUqlzcpAtqKxw-8p6K4VuxIzkWR7wfuI_VP6LMXgc9e0fQtCriOFEEa9CJcHJAIk4ac2V1bpDxeSJhdJl9ibbvJwWH6iUvmWhS9pMtgPZBA9oxjhIknAhGeaSiV2252oTbphbcqPqadjVZv4iaras9ly_NUA0Lnho_IJ1m3pEy4iUl-NiYuIc5ghVkprew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک رادار آمریکایی در بحرین بعد از حمله موشکی-پهپادی سپاه چند روز پیش</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/17497" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خدایا درگیری جانفدایان کف خیابان با جان برکفان ناجا را هم دیدیدم اما قهرمانی .... را نه!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17496" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/17495" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5fZnemm7akUbu0eUykYFG4VbGamk2I-szk9Vs1Qw3sGHohHfYGsilsSwGVi_vpF1xSEtk-5qQh0MLZwvnuQ5S15MUB_3ok-aZUBiCpav9djoSwzVbkf8E9VWk8DdouVBFhNv0-GFt2kO879gCmtP0nyGtKh9LV9Ivfqx-tg6z-P4AC92SBW9qjG-8NRvoHBKjeNLPN2B65aCQfz6yfoGNArdCa9gqQSvgNQwjjs8ftztEuSV76AXMjh2I9TZh_jDXHa8j161A01Tw3JB6ZvB5pxi3z1H78ffPcYB_LKunfxRzWOG2Way0K7G6bMHErJtUjKtVkPlQB-VIPmqZKowg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا همه دارند به تنظیمات کارخانه برمیگردند!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17494" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKVInahSFJBYjYZY1IPg6aBAzr156xgxdPc2VXNGbg6Fg3oypyJ4yoh-brA5HB9TyD11m0wV8aATwbwYul5s-4mzZrRskBlB43Iw57dO7XstV9a7-Kf7BJX13ZRhjBhRScc-a01TjK2xrBG2OpFC3vaPucZaKkH5wvQsmwuZTHwULzSjkfFrEqPQ_GbMLMH6nNBclD9UwTQViRm8-lMG2iMLO6j7Igi1OJjcIyFGH4pVIvNS-ePN3MQxgig-bHz8FvjteVEMfxPBGz4js00RIz0k7UQ-IRe5LgF-PGBOQK0N31HNumaaHs-iXtVftskbwqIl1DDDCuA2Pc4zh439DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!  فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/17493" target="_blank">📅 23:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/17491" target="_blank">📅 23:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!
فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/17490" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/17489" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17488" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:  "هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/17487" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:
"هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/17486" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شرایط جدیدتر اینطوری است که ما کشتی های هندی را که از ابتدای تنگه هرمز  می خواهند عبور می کنند میزنیم. در پاسخ، آمریکایی ها هم کشتی های هندی را می زنند که از انتهای تنگه هرمز به سمت دریای عمان می خواهند عبور کنند. ِ  این وسط، گاهی کشتی های غیرهندی هم هدف قرار…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17485" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خیلی جالب است؛
ترامپ می‌گوید نه پولی می‌دهند نه عوارضی از تنگه هرمز اجازه می‌دهند و بعدا اورانیوم غنی شده را هم خواهندبرد یا نابود خواهندکرد
مقامات  ما میگویند هم پول میگیریم هم مدیریت تنگه هرمز با ماست و هم بحث هسته ای الان مطرح نیست!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17484" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17483" target="_blank">📅 21:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منطقی هم هست؛ امضای الکترونیکی که دیگر حضور فیزیکی لازم ندارد.   بوگندوهای فاکستانی فقط دارند می روند شام مجانی بخورند لابد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17482" target="_blank">📅 21:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فوری | ترامپ:
ما امیدواریم که عملیات به راحتی و به سرعت پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مجبور به استفاده از آن نشویم.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17481" target="_blank">📅 21:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!
کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17480" target="_blank">📅 20:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17479" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:
«توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.
امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد شد».</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17478" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17477" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17476" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17475" target="_blank">📅 19:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این طرح واقعاً بامزه است.  کشتی ها باید هزینه «امنیتی» برای دریانوردی در تنگه هرمز پرداخت کنند تا نیروی دریایی سپاه پاسداران از آنها در برابر حملات نیروی دریایی سپاه پاسداران مراقبت کند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17474" target="_blank">📅 18:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت امور خارجه ایران:  «تیم مذاکره‌کننده ما برنامه‌ای برای سفر به ژنو یا هر مکان دیگری در دو روز آینده ندارد».</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17473" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17472" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17471" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17470" target="_blank">📅 18:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTAqT7i2f678ipiM51pWcvm52jdte-ICBUojAkxDfPecPMOvV4BKkylstQ34s-wVI-7Rk7ISEXpapJyVdNZBOI3C-zQw4ZYQwuWtmPFtydIjcO9MPYXFh-6xnNvbx4DyKkOpv-HHSxiSfKAk_oLDvkXZ9isz_52hxfak8ArBnsYtCQtxC2kIp0dqI_srsoFU4WzYlr8Vx5dw59A0oIGQMLYmfuNbBEX45YNqq_kUhrPHxCJqyBj75OFbbCEz7ubwkvl9ee1t1gC8eDguZ2mTPHKXI8e54w12ulDf8Rf_zlVghjwcHfaO_B-GLPq_zlFh70lZJSN4D0qbZLTF5x6Irw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله! جانفدایان یک پویش توییتری راه انداخته اند با هشتگ نمیپذیرم!
که اشاره دارد به برائت از ائتلاف قالیباف-ویتکاف!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17469" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گویا یک ستون از ارتش اسراییل نیز به سمت صور در حرکت است.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17468" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
