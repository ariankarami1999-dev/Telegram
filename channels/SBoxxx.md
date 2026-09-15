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
<img src="https://cdn4.telesco.pe/file/sQXWNW3nJ6D59bA4gwQGurU_hnWMiYBbbXl41ALaPLY8pnvjeLR4F0EPSll-8hp0uPM-TqDFEUOrnd98DHEm5vfS_KrnQCVT7wy7mbtAvc65YtSTKrJ4igM9JMmANoM-W2C_XsShEIocX0sqQ6JhlyAD8O3Nne2cs87s3QwcJunmd28Ao3l_PmSw8oiyqzICh8N9zHLKP_Mc80XGgF9Bt211NW5pwiqWbcSX2yRBOq4j3ryw0zaQ-gMW1g89GUewOOQxCuwYknFdpq14u618wmraUmI9zPKC-Qfv8DOoRyCEIwaDOsxnBoJwyImEiTN45QK4872J4quQaHI5294HGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 04:34:56</div>
<hr>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXR3z13PTmMJPkVEFpkWLx62P7X0ILsFyb5Hu8DaVEv30yJeMj3AiQ5c6Sceu4p6S2DEl-wuFMf3DwTq9M7y0c9PjCe6r5Zz-Ypj3uvm2iQwtySMeeZdVYm4YZpf29viMeVtQqjiUPBOnnjtz_YoOdmqRpv9JHHIr3BSXJ8n7aWKCRlYXLhmPwTaiNU9hdyWXijC_apAqx9YQeaSKP7ui6s92QblAyqsdnLURXWv477un8tHJi1egOJcltefJ-d4dpv9mYDIeI9QaqwOGutb9PGlsvTdkcsW0zGb2Nq9Al_jxdkRxj99uhjkgnBlsorJDIZY35crzQ7PxR6lplD9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt_2VM9FFzGH4QVBoZeUCvaaB7ZhnrMuJPBfW30v-idzI6FG0Cfv_gU0jX5_fZgcT_YFWCWCRTa_CtKnQyVsEangdA7WspT27QBpvI64JErZR7WfneclpU0KZ0BLhuhBZzeMXIk-TJGrWrfs4qzbEJ974FoAFhEfVMAV0V1mMs2uY3n2uWpdOVqtz5Emt6EooFCiKbaNfCfmJDnbyidpDPRcTelvmvwlkz0zgBLthLDPfsGsFavHP3ZIfCe0SRl_WbRTR3z9kyEN1Fw6ePzWAWtc2PSoYLMF_LmapTVofr_OQOBIKU2m_IC6FvPor9NUED0KNnUpexi9YaWi62p0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAgJSPDZ5T4CRSWM36U1BSovCXkDeRKzsRc60C2XQbkhYpTo0yLu9HQbR_3Tdmht5vOzHBTsKOh-tkhu7-ZqpoTOsRonm0ZlMGHAcFKc3iW_wu2ZIU9mbht2TtFhMFNGQBJDYFobsSwHp1z-dvkiZg88DrhTp7R1pzRgohgNelXT-uK6z4MwUfeFf5kwNArNkXD8mBQ2T4amCa38gqU7mu7OpEJB6xbebolVmFyCkV4aTRktD74Od3svu0UlhuwQ0FVOm7SpxdnTJ9aAxE-22otealIcArmDvMHHe5o6CiF-SSBIn06DXWdq93_O1HFa0WBWlQlgNRDfZIP0xqW7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGZr_Ox3c9Qwjc_lZ1GU4iTULJBXTQyQPZbp3l8C_b6j_HhDc6ONOwps1L8hUVW2xoKcjFLUyBHzz5Bux8YXbbDter9-CPtKyysPm3sy7Ad_jESTmb7YGTFsEfwUaWm8FagzSw_QcfyBQKguCg9aHnsnk20SKCTfCnzSlHA__waPni6eThpGA3o1GiGGzvdcV3nCQinRwzTr-bIeLG1V1Z7aSR7W14EGSo2KUlyp9CydSRIRoBUc5ur8vcHyK-YifR-5p9lTWMWAcHdWmmE4hiFKQfYpO4_LlcnlJveNt67ML3FyJDEfhha_JgEPMV2TkAOuiXG8WzjyByc53xIjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obYROlD7369evnuRFvV0rx3m-Hs5OFpKj39goVF6fSLMP6VhrbpWQQ2_aEY0v8EZY779yzpe-vyuwEGeTb15fKx3AxnA6G1hDXzIaF8Vj7H8nDZiYMD-v2cDdAqG4cljAuygap9zhP772wKSW-AOhJsw-5jWnPJtJ-JGLDWdseaXECxIv_0ximy-VWxEhRcL8Z59NVIaHaw-G3AuH6mo-f7IJUeRMqJOwTTR3s4Qn6a34CH-JjK1TPqhVNeuk9u-YaCk-3XW8e-s_IJiQWnrG3eqARf_3d00GJzziWT9Bn6pzGjYJM4xbomf3NXGv3swXZLVxKsEgd82asrTq-QuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mksphmOiQ30RPoQcZi4kZx5fWXJaz_uu-DMiduCG3I0CKEXmQvUJR54KpGKVJOJUN5g2G3JW8TrzziycwNxEB5MwPyRIn8tfOg8pxJH4QxHy6_pU-joZCb1dA0-NpAWFtypPV5RdQ_pnfz6ylqod77Yu7wJY_xirHL5EnxaBIu93VoFuwnRoxRlWO5PmT5QUtEm2ShrgVFF8nfPTlKPDp8EU2RVdQM447eKimDVCBWtyWR_c2z0t8JgbN5UKckeQc29WV1yukIyV3kNskbKKOXGIWl3zDteeZVgZtJVu7GyISNAmH0VqmumgwmHgwKGCsdcFulxErPfj2RisRq9v5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzBgO9RH62pSDCwu_jxFJc7BhrdHZEbvfz5zegKE1vRnCw2731QTZmHhbn2go6sm7FHpGu7Sg_hSXNPkqGT89gI7LzWIWdO-m6lCaiemcWB-4-xqBY3pyKTrziIz8duNkOuBkRyHPbJhhpgeEpdoClcwa2dUOooFfhLxL9uxW3rpvX04mo-7XzCYxPeRR8PvNzLQ13xPKdhjeLHKDGn0mo5HNOZSgJj08ykVO8aFQfb_zWgBDR7Wj7p8BzXvMR0jAPv_CMDvQNCZs6Qyaymvpka1wh-SkcnyvQJaliv39dT98GTnxhUy9FWYakKMQyCNaAU04GnAnRRmaSAFNIv5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت تحلیلی | سناریوی اختلال کامل در مسیرهای صادرات نفت عربستان
یک سناریوی حداکثری برای بازار نفت، تخریب خط لوله شرق–غرب عربستان، بسته‌شدن تنگه هرمز و هم‌زمان بسته‌شدن باب‌المندب را در نظر می‌گیرد. اگر هر سه اتفاق به‌طور هم‌زمان و برای مدت معناداری رخ دهد، بازار جهانی نفت با یکی از شدیدترین شوک‌های عرضه در دهه‌های اخیر مواجه خواهد شد.
اهمیت خط لوله شرق–غرب در این است که به عربستان اجازه می‌دهد بخشی از نفت تولیدشده در شرق کشور را بدون عبور از هرمز به بندر ینبع در دریای سرخ منتقل کند. ظرفیت این خط حدود ۷ میلیون بشکه در روز است. در شرایط عادی، صادرات نفت عربستان حدود ۶ تا ۷ میلیون بشکه در روز است؛ بنابراین از کار افتادن این مسیر، وابستگی عربستان به مسیرهای دریایی خلیج فارس را به‌شدت افزایش می‌دهد.
اما اگر هرمز نیز بسته شود و خروجی دریای سرخ از طریق باب‌المندب هم امکان‌پذیر نباشد، تقریباً تمام مسیرهای اصلی صادرات نفت عربستان مسدود خواهند شد. در چنین شرایطی، ظرفیت قابل استفاده برای صادرات نفت خام جدید می‌تواند به حدود صفر تا ۱۰ درصد ظرفیت عادی سقوط کند. البته این رقم یک برآورد سناریویی است، نه پیش‌بینی قطعی.
اثر اولیه چنین اتفاقی احتمالاً در بازار نفت بسیار شدید خواهد بود. بازار نه‌تنها کاهش فیزیکی عرضه را قیمت‌گذاری می‌کند، بلکه «ریسک عرضه» و احتمال تداوم اختلال را نیز در قیمت لحاظ خواهد کرد. بنابراین افزایش قیمت می‌تواند بسیار سریع‌تر از کاهش واقعی تولید رخ دهد. ساختار بازار نیز احتمالاً به سمت backwardation شدید حرکت می‌کند و پریمیوم نفت فیزیکی افزایش می‌یابد.
برندگان مستقیم این سناریو، تولیدکنندگان خارج از منطقه خلیج فارس هستند؛ به‌خصوص تولیدکنندگان آمریکای شمالی، کانادا و برخی تولیدکنندگان آمریکای لاتین. شرکت‌هایی مانند ExxonMobil، Chevron، ConocoPhillips، Canadian Natural Resources، Suncor، Cenovus، Petrobras و Occidental می‌توانند از افزایش قیمت جهانی نفت و کاهش وابستگی بازار به نفت خلیج فارس منتفع شوند.
در طرف مقابل، خود عربستان با یک تناقض استراتژیک مواجه می‌شود. افزایش شدید قیمت نفت از یک سو ارزش هر بشکه صادراتی را بالا می‌برد، اما اگر نفت فیزیکی امکان خروج از کشور نداشته باشد، افزایش قیمت نمی‌تواند به‌طور کامل زیان ناشی از کاهش حجم صادرات را جبران کند. فشار بر درآمدهای دولت، پروژه‌های Vision 2030، پیمانکاران و بانک‌های داخلی نیز در چنین شرایطی افزایش خواهد یافت.
اهمیت ناوگان نفتکش‌ها و مسیر SUMED نیز در چنین وضعیتی افزایش می‌یابد. در صورت بسته‌شدن مسیرهای سنتی، دسترسی به مسیرهای جایگزین و ظرفیت حمل‌ونقل دریایی می‌تواند به یک عامل استراتژیک تبدیل شود و نرخ حمل نفتکش‌های بزرگ، به‌ویژه VLCC و Suezmax، را به‌شدت تحت تأثیر قرار دهد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20867" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رقابت عظیمی میان ترکیه با اسرائیل برای ایجاد هژمونی در غرب آسیا شکل گرفته که بجز جنگ با ابزار دیگری حل نخواهدشد.  بزودی در قفقاز هم شاهد تحولاتی خواهیم بود که نقش و جایگاه کشورها را عوض خواهدکرد.   اسرائیل به شکل هوشمندانه ای از دهه ها سرکوب اقلیت های قومی…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20866" target="_blank">📅 10:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR91grhosArsAYAQS3mntcMeJ7DcvqYKy4VVXh3kXgmGo0mbi65vVLeWHR39txQn-Q7nfnr8fa4N4aFqa9RMN7URl0IOF0YH3m_mfgTuS3_Cmi8Uyefb9mie2zHJC4HOj2Jc50xs8sBSR1Qi7V9HeldXMYjutandZawEszBv8JSEaTLQzMhkRpZMkuPGJ9ZbTbSmzp4aLbuFuqpDJYvffki2Sy2RuyofhB-86c6EF8sYetD3O0qiSs5n4vqo-qJdBuQmxrdshHWT-3LB7yow5Ts8Sb2gzpNC2JTL2TsmgIYkoXNd5_A0mUDemxoHQkih8IJRwRpS0Sjv-yIILU3HFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ نفتکش‌های VLCC به شدت افزایش یافته و در تمام مسیرهای اصلی به بالاترین حد خود رسیده است، زیرا جنگ ایران ترافیک تنگه هرمز را مسدود کرده و جریان جهانی نفت خام را مختل کرده است.
هزینه انتقال از خاورمیانه و خلیج فارس به چین به حدود ۱ میلیون دلار در روز رسیده است، در حالی که نرخ خلیج عمان و چین در یک ماه ۳۰۰ درصد افزایش یافته و به ۵۷۱۰۰۰ دلار در روز رسیده است.
این محدودیت فراتر از خلیج فارس در حال گسترش است. نرخ نفتکش‌های غرب آفریقا به ۴۱۱۰۰۰ دلار در روز رسیده است که در یک ماه ۲۸۰ درصد افزایش یافته است، زیرا سفرهای طولانی‌تر اقیانوس اطلس به آسیا کشتی‌ها را متوقف می‌کند.
موسسه لویدز می‌گوید که خرید مجدد نفت خام چین، ترانزیت‌های خطرناک تنگه هرمز و راهکارهای ناکارآمد فزاینده - که اکنون با تعطیلی خط لوله شرق-غرب عربستان سعودی بدتر شده است - عرضه نفتکش‌های موجود را بیشتر محدود می‌کند.
با توجه به اینکه حاشیه سود پالایش هنوز به طور غیرمعمولی بالاست، اجاره‌کنندگان تاکنون می‌توانند شوک حمل و نقل را تحمل کنند. دلالان می‌گویند هنوز "سقف مشخصی" وجود ندارد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20865" target="_blank">📅 09:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_QZQhAKHtd8YwghrJ6psBMIgdiuvgw2quihMIneI0rRitNSHtZ9qeWF_p0aGmzNArA3ROqNKNleASG18lLLIFHh_pKo2E90BW5crqvCAVlvJeCV5oCIgmavHXyR0aAYfi3xA293q3iriGFrFtxo4f3uao3rkDDAZifOYjY-7yuXADJdbBv5Hr0KEneeDw1T3zDwRlprdKJtJrFwBxWNIxdrCAkoCvcG9NR79L3tjIe-Q7C4ZYIgEjYZQwQUWoAoZWr4XeA9jdpu-oOr40FH2gazV2R9eK4LRomZ6M5_UMhxkZrdqQPSDdhrF15UIJKLLHKQkgJxAAH12dir87tQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی ممکن است تا ۴ درصد از عرضه جهانی نفت را از دست بدهد اگر خط لوله شرق-غرب آن به سمت دریای سرخ در عرض چند روز
راه اندازی نشود
این خط لوله پیش از حمله پهپادها که منجر به توقف آن شد، حدود ۴ میلیون بشکه در روز به ینبع منتقل می‌کرد.
منابع صنعتی می‌گویند ینبع در حال حاضر فقط مقدار کافی نفت در انبار برای حفظ صادرات به مدت پنج تا هفت روز دارد.
این منبع زمان مورد نیاز برای تعمیرات را فاش نکرده است؛ برآوردهایی که رویترز به آن‌ها استناد کرده، از راه‌اندازی مجدد جزئی در زمان زودتر تا ۵ یا ۶ هفته طول می‌کشد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20864" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6j4bdCURy9hlZArXJgvhZqtPuOks6LiQNTG0u0s8tKMnsaDKwpByviLhqKf4r2Jel3G00B8XX2SM1tW6p7DtX4Lm4ynQ9rJlXkM9OV1p2vqsePcMpMrwkBZ3vGeGoqKIRTqKmCymyexhC_S6YQa3DnKsrKrHEMzU_FImhQ232-M5OLyGqBFsjYjD6nZ9TilJDl11xRxVJqkYLRCOPDQ8_TCIa4YW1jJrhb3BHaYbhxOQ_y3RkwC7nAYboQKZe9154BgAqoUVWoyRJFgBGFg6OhEbzR1rZwxjV-iTZJgW4jH9Juggwiza7uBWHng0oHjY5tiLKGj-Jw61Tjf3DosGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20863" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نشست فردای ایران، عمان و کشورهای عربی سر تنگه هرمز فعلا لغو شد</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20862" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20861" target="_blank">📅 23:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20860">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vc7KcRCvKpbJCxMh7RZTm3amavbGc_6KS76RPgR3xb46Kos-ZC2X0p9dwFwbDOSsuIPxTKLPjqZIgkQ3_0pWvLCL-5Kd_Uezv5lxVYeKxPW5y-sTHa0-CVC2wxd0chl_HOTFys3RicI5uaG-ZzOFELa95niVNLy0vrWe3PplW3kIYxL4Dj8xULwmkcIsnGrPiP-9KNkNbiH12n15QjcG23_nsoHwYEd-JZXhuHP1rMz4thHJNcI_Kp9j-z-1Y4IS06CJ2S2MWuTiOygAM0x0HHQulAJvSwqtSUr6_OFm9nbdMis5NJTj7XBCq-nsKyjmUVJ8XXQ8QjLVHc7iy4ngPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان
پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20860" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20859" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aitjIdk01YI179O1RWtt28XlxbGUWJJSX81zaVeFdVnuVEvfQjzHryzxHUqGu3POaPYmrvyRT6A18egOPkPuMc1O2WQNYqSjKc-xoKqlIr7YIs54e-NUe4fCL1VkcB6oLwJ2fzNCKR8jWDWsfJrjkR4UaHIFCAWpZ2FVab6Dc0YIWX2xIOGEbuBURv5rQGLAsoraDtfudifHPPy7Xf0TL06j1Ev9uTuqlSi433k0tLZFxGc9Tbk02DSyoySC2G3-jEM5PeYaFgwAKpRRAVeiGXjJV9gKKgw05hOeGxwi-Xk2qMjrtPC4CKb6fdGgRYW1F6Sb386Zdvo-zKO9eedKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده J-10C چین: نیرویی جدید در آسمان جنوب آسیا  جنگنده J-10C چین اولین پرواز رزمی خود را انجام داده و نقطه عطفی بزرگ برای صنعت هوافضای چین محسوب می‌شود. پروژه J-10 که در ابتدا در اوایل دهه ۱۹۸۰ تحت رهبری دنگ شیائوپینگ آغاز شد، با هدف توسعه یک جنگنده بومی…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20858" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فیدان: سوریه می‌تواند جایگزین مسیر هرمز شود
وزیر خارجه ترکیه گفت:
سوریه می‌تواند با اتصال به اردن، عربستان، عراق و ترکیه، نقش مهمی در ایجاد مسیرهای جایگزین تنگه هرمز ایفا کند؛ مسیری که قرار است از طریق راه‌آهن، بزرگراه و خطوط لوله عملیاتی شود.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20857" target="_blank">📅 20:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfQ_uDM5Go2tkD-Jh0pUXusqJWUufBj_jsbZ6ruB93Ez5oIpdHLVo21kFSxo_D9GhQla-HJkSOC2BAh789UMAud_sjf2QGMzVkLYENQBfcAe6dn9ncUD3bY7ZP-tJ4oydaXmIRspwumBElRfdI5r0POqDv0yfIlVJXYlp9NZUewM2XBb5BirZGRHcSp6c3y9dA-qwM_6bb6Us0DRVx-0akgFhv8hge-OQDVJZrZmfWwZrlNpQLPvf1XohjYSO5tAyJ29nodwkwdXDB8qQdch-4AHWVfsHCJ_zyGo5vy3IvfJVv9lp_9IpDYyi823kr1TtQNO_JExd0q9OHrlKEq5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
ایران از روسیه درخواست پهپادهای اصلاح‌شده «گران» را کرده است
بر اساس گزارش FT با استناد به منابع امنیتی غربی و یک فرد نزدیک به کرملین، تهران به مسکو برای پهپادهای مدرن‌شده خانواده «گران» روی آورده است.
باور بر این است که ایران قصد دارد از آن‌ها در درگیری جاری با اسرائیل و ایالات متحده استفاده کند.
این نشریه علاقه تهران را به توسعه سریع اصلاحات جت‌ساز روسی و افزایش قابلیت‌های این پهپادها از نظر برد، سرعت و هدایت مرتبط می‌داند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20856" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_IsKKn90tsPO3AYatcMshKKseQZmgoAZEJxi5FDKkVbAgQmkCGquYl-NBdkBzg6-qyWMM7SBupnMlEeSZdsCHUARq3mhTtmmvDPlxSc2kNHw6MaNQt8dHQO_taB6rf_1k1bnXNJVTZhMgaZybBTXNs0oNNTGeJm7UillChFZs8VNY4f3clc4LYFPt1q_ooaOY532aOxha6yg--gImBqqMXoJhyMZVBZQ7VK_FJ5zrfDyx0prOF15Nh6Rl8oseKaJcV1jUFgZSINW-YNrHO8jS3RKOGeoieRPLvBkjDA3p5QlXLyBfbHxrwSCFuLReuuFlEcxLs6L9yC8mOEUH93pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
نشریه شماره چهاردهم منتشر شد
📌
در این شماره می‌خوانیم:
✔️
طلا؛ دارایی‌ با بازدهی پایدار بالاتر از تورم
✔️
واگرایی میان فدرال رزرو با خزانه داری
✔️
وضعیت رشد تورمی در اقتصاد آمریکا
✔️
چرا طلا یک دارایی راهبردی محسوب می‌شود؟
✔️
و...
🔗
نسخه PDF ویژه دسکتاپ
🔗
نسخه PDF ویژه موبایل</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20855" target="_blank">📅 18:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجار در بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20854" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هم میهن:  ترکیه به جای دلار گاز، غذا و دارو می‌دهد همتی به استانبول رفت  منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد  دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20853" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هم میهن:
ترکیه به جای دلار گاز، غذا و دارو می‌دهد
همتی به استانبول رفت
منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد
دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر اساس سازوکار توافق‌شده با آمریکا عمل می‌کند ، عبدالناصر همتی ، رییس کل بانک مرکزی ایران وارد استانبول شد
به گفته شیمشک، مبالغ مربوط به خرید گاز ایران در یک حساب به‌شدت تحت نظارت و تنظیم‌شده نگهداری می‌شود و ایران فقط می‌تواند از این منابع برای خرید اقلام مجاز در چارچوب رژیم تحریم‌ها، از جمله مواد غذایی، دارو و کالاهای مشابه استفاده کند.
سخنان شیمشک فقط درباره پول گاز نیست. این اظهارات نشان می‌دهد که ترکیه در دوره فشار حداکثری جدید آمریکا فعلا حاضر نیست برای حفظ تجارت با ایران، ریسک قرار گرفتن نظام بانکی خود در معرض تحریم‌های ثانویه را بپذیرد</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20852" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5_WFAdHHRq5EFE6RGEGzkc8Cawfy1oc6NmqFd2eMMk7qzrqWwmT8hYkwOWQaQ15XGq4Mx26tXLpZKQas0_TFISRtDyI1JiDAEXdpiclpljGBjxEdwnREf6gl1e0z7A_fpk04qYPD_F45_iFDEyxBiRHQQ9uJdZCA5tmnqqsLhJtQCC2qDtWBK8xMsiVF3HzsxPUJN1uMwBCKflqnIkYH98vnwUSUjC-v1H-gfGxImbfTd4BnJxBpt-ybC3yDnQebbtUd0y43npmzg9TlOqewCxPl0sYVWGqNtqQLR4p4Z7VJRiu4SoeZPyTGQm1BFGDoFhq8vIez3keNrQvtRTHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
حوثی ها با هوش مصنوعی آنتروپیک موشک بالستیک ساخته اند!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20851" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پزشکیان:   نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20850" target="_blank">📅 12:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پزشکیان:
نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20849" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20848" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">— یک کشتی تجاری ایرانی در نزدیکی جزایر هنگام و قشم مورد حمله قرار گرفت که در نتیجه یک نفر کشته و سه نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20847" target="_blank">📅 10:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">احمد اروزان کارشناس ترک:
خلبانان اسراییل برای حمله به ایران در قونیه ترکیه تمرین میکردند!</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/20846" target="_blank">📅 02:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">معاون وزیر خارجه یونان:
ترکیه و همه در منطقه می‌دانند که یونان کشوری بسیار قوی است که جایگاه بسیار بزرگی ژئوپلیتیکی، دیپلماتیک و نظامی کسب کرده است.
و من مطمئنم که هیچ‌کس هرگز این قدرت‌های یونان را آزمایش نخواهد کرد.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20845" target="_blank">📅 00:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW6sOJ1WmbXkex4QNu2FLimAgqn2TiUm_7WCbH5448eYbeha9gTi-oSZCE_lc-vWWAIccNE6xaND50I45SnyC_4o3mpJaS3EF2VE0OID27WkHwE38fmCkieDgontn-K5Ex3z-f3IQhVzN_amKJVEU7pZbyIGni8PcZbI558evGF8mJkCe_al4YKVd5lgnCHFuCU4oaiaxX5vSjVu7Hez7Pc3ocvfMQCyVtcdK6DCvkKtJkATNGfERBcrRqa8lnDGemnQeXU84B4u1uQd4-3xgVPNuED4nHhtDu-wjrFbBkbmD85B9HKI_LkcYXyCRZpnimUi8T0IkU3UQYdU9HM9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پیمان مکه!</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20844" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پرتاب موشک از ایران به سمت هرمز</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20843" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
ایران در حال آماده سازی برای تست سلاح هسته‌ای است</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20842" target="_blank">📅 23:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKTHQlLQknMU2biPXaguPYsHh_bOp7WDne5u2-fei5oi73iZnf_Ckr6MDGyM08xMbfbO1lYD9cgN8_7TjtjkpBv7Wv1MpthBrMTBhwRYMEktHK0qApDkAiHQ5RHw7H2XvjljZceUDhoB9kxeqj2PJs9nUTJiz7yP6UoaIgfG5B3KpGYbhvW9shsiWqUk7gRrWWkvEqYEbkvdRDp3xLl937U5KwZuWuigZEY65IZb5rcHyJ5sjVJbjHl4ZnClt59O7U_rqqh56awf5Hh4LuMEOHl6mHCMBG577B3HBS1Zj17jEvoxV5ivcmKVeH2wdAa_zcZJ7ts4I_tUO9mg5e7NBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20841" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20840" target="_blank">📅 23:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد  رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.  مسعود پزشکیان گفت: «کشورهایی که…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20839" target="_blank">📅 23:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترور یکی از بسیجیان عشایر منگور
سپاه پاسداران انقلاب اسلامی شهرستان پیرانشهر با انتشار بیانیه‌ای، شهادت حاج اسلام کاک درویشی را تسلیت گفت.  پاسدار پیشکسوت و دلاور عشایر منگور، حاج اسلام کاک درویشی توسط عوامل پلید ضدانقلاب در مقابل منزل خود در روستای کوپر به شهادت رسید.
شهید اسلام کاک‌درویشی از جانبازان سرآمد و از نیروهای مخلص و وفادار به ارزش‌های انقلاب اسلامی بود که سال‌ها در مناطق کردستان و آذربایجان‌غربی مجاهدت کرد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20838" target="_blank">📅 23:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">معاون رسانه‌ای انصارالله یمن: با هدف‌گیری خطوط‌لوله و پالایشگاه‌های عربستان کار به نفتکش‌های سعودی نمی‌رسد
درصورت تشدید تنش میتوانیم زیرساخت‌های نفتی را هدف قرار دهیم تا اندک صادرات نفت عربستان از کانال سوئز هم قطع شود.
همه چیز ممکن است؛ مگر این‌که محاصره علیه یمن برداشته شود؛ عربستان فعلا درحال لجبازی است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20837" target="_blank">📅 23:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20836" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد
رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.
مسعود پزشکیان گفت: «کشورهایی که خاکشان از سوی آمریکا برای حمله به ما استفاده شد نیز در این نشست حاضر خواهند بود.»</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20835" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvQ_Oj-2Qa6u88MkkjDkO8AgzzMvZQ8aYjQTJXDbcwEasbe4untdRCvUP8SsK7ssZbnFOBqTkoND67giiOqJ373UiQ4vEvvFODMRqVWr66HVmmLJ8M0LVwXbObMkuW8dW0rkWCb0adVxnRUg_EE_kUouyjWLA2XLYhQ2_oC2VS8DH81jL-PR6K3yCY4kJF56EQ2IsjfGnorlUZAFK2JIkOwIbz0CH7UzYjjdmS_rDoxFURoK9Ymi_cFGC6nu7Vdn4Y_cFuOQa_JdOUdjaXnXpBqrj9Pgr0niNeL7vtN1EirPWMUC1bN9uKifNzunUOMvoO8Dpfh8DmNcxf4Os-atug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی ان ان:
اوکراین در نبرد با روسیه، فراتر از اروپا، تیم‌های کوچک متخصص پهپاد را به آفریقا و خاورمیانه اعزام می‌کند تا نیروهای محلی را آموزش دهند، از گروه‌های ضد روس حمایت کنند و به منافع روسیه حمله کنند
حدود ۱۵ متخصص اوکراینی در شمال مالی در کنار جبهه آزادی‌بخش آزاواد (FLA) که توسط توآرگ‌ها رهبری می‌شود، فعالیت می‌کنند و به جای درگیری مستقیم در خط مقدم، آموزش پهپاد، اطلاعات و پشتیبانی عملیاتی از راه دور ارائه می‌دهند.
نیروهای اوکراینی همچنین نیروهای چاد، نیجر و بورکینافاسو را آموزش داده‌اند، در حالی که چندین متخصص در سودان نیز عملیات کرده‌اند.
سازمان اطلاعات اوکراین می‌گوید این اعزام‌ها با هدف فشار آوردن به روسیه در خارج از کشور و تبدیل تخصص اوکراین در پهپادها به یک «ابزار سیاست خارجی» انجام شده است.
نیروهای اوکراینی در سال جاری میلادی، هنگام تصرف کیدال توسط شورشیان توآرگ، به آن‌ها کمک کردند؛ جایی که نیروهای شورشی و وابسته به القاعده، نیروهای سپاه آفریقای روسیه را به عقب‌نشینی واداشتند.
نیروهای اوکراینی همکاری خود با توآرگ‌ها را عملیاتی و نه ایدئولوژیک توصیف کردند و یک منبع اطلاعاتی گفت: «وقتی توسط همان احمق‌ها مورد حمله قرار می‌گیرید، تفاوت‌های ایدئولوژیک در پس‌زمینه محو می‌شوند.»
اوکراین همچنین از اواخر سال ۲۰۲۵، اپراتورهای پهپادهای دریایی را در شمال غربی لیبی مستقر نگه داشته است. یک اپراتور گفت که یگان او از پایگاه نظامی بین‌المللی در مصراته برای انجام حملات علیه «ناوگان سایه» روسیه که از تحریم‌ها فرار می‌کند استفاده می‌کند و در عین حال نیروهای محلی را آموزش می‌دهد. یک پهپاد دریایی انفجاری اوکراینی از دست اپراتورهایش خارج شد و در سال جاری میلادی به سمت یونان هدایت شد که باعث اعتراض آتن و عذرخواهی کییف شد.
اوکراین همچنین تیم‌هایی را به حداقل ۵ کشور خاورمیانه اعزام کرد تا در طول جنگ، آموزش سرنگون کردن پهپادهای شاهد ایرانی را ارائه دهند.
مسئولان اوکراین مأموریت‌های خارجی را هم به عنوان راهی برای تضعیف روسیه در هر جایی که فعالیت می‌کند و هم به عنوان فرصتی برای آزمایش فناوری پهپاد اوکراین در شرایط میدان نبرد مختلف، از گرمای شدید و گرد و غبار ساحل در آفریقا تا عملیات دریایی در مدیترانه، معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20834" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plYhhJPUHPo8Bs5X3_bL3N4-9t-woVz3f_tHYbB-k8nCLpDuYi8KQboZsASrr4aKlwR7AUapDndfqzzP2rYjsnhhp4xYezdzO-pZSXQS5JxOPZg5Vq3dxcBlVqatcwqQp6eWaoJfWt4PBhlxynKvjt3LQrRQZNiqYP5JXwo19Awz1uEXI2iCxqgFVsqO7rHGrzQQXmYGgRod3zA0LDQzB5wHqQBwOg2ff73bM1QJ4FLONaYb9_nvIA-GSglnCVP4u5LPdxSINwwcwMQDvYfugOJnBL_Yy0BAUANbHq3bgsmznX_c1lOUxxRWWbYFmZ1dygy6fkKxI3SDhIltR1YK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20833" target="_blank">📅 19:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20832" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مدتی است به صورت آشکار و بی پرده، صحبت از لزوم ساخت سلاح هسته ای ایران از سوی مقامات کلان جمهوری اسلامی مطرح می‌شود</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/20831" target="_blank">📅 15:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ:   حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.   ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20830" target="_blank">📅 13:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:
حوثی ها با ما تماس گرفتند و به ما اطمینان دادند که به دنبال درگیری با ما نیستند.
ما با حوثی ها صحبت داشتیم، آن ها تماس گرفتند و به ما گفتند که دنبال درگیری با ما نیستند و نمی خواهند ما به سراغشان برویم. آن ها اجازه می دهند اکثر کشتی ها عبور بکنند و فقط با یک کشور (عربستان سعودی) مشکل دارند.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20829" target="_blank">📅 13:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20828">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20828" target="_blank">📅 13:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=dNYrTq6jtFKM77K471QYOdTNsEzLHpOiosNidJy8VUGfinBRygrM07hKLH_bAu5IpKeXByrB7D0c1A6xvioabSZRbiYNMf1Kn90uK9qpawtHuyuDr3aDbBWSA_npsQBaJCsbfMTbkS5-G0KP-m57jnkVdM4QMxMex6QUiuCQRAIudcQvmC6AczWqB8VrKrX6wpN914rqwI9IsOxWNZJ4UqD9Mwt-8wCHMzghd16dCtp72DcNYIMkm533GMshMXkykwo945_PoaJnP2VgQbTXHqLEps1W1ihbd9RND1DHl0hNC04CjKRJf5we6K9uG3eCKRWLr8t_kl0loJPS5xHxTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a939b42fc.mp4?token=dNYrTq6jtFKM77K471QYOdTNsEzLHpOiosNidJy8VUGfinBRygrM07hKLH_bAu5IpKeXByrB7D0c1A6xvioabSZRbiYNMf1Kn90uK9qpawtHuyuDr3aDbBWSA_npsQBaJCsbfMTbkS5-G0KP-m57jnkVdM4QMxMex6QUiuCQRAIudcQvmC6AczWqB8VrKrX6wpN914rqwI9IsOxWNZJ4UqD9Mwt-8wCHMzghd16dCtp72DcNYIMkm533GMshMXkykwo945_PoaJnP2VgQbTXHqLEps1W1ihbd9RND1DHl0hNC04CjKRJf5we6K9uG3eCKRWLr8t_kl0loJPS5xHxTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلی دیدنی از پتانسیل صعودی شدید ریال</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20827" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ درباره ایران:   قیمت‌های نفت پس از پایان درگیری سقوط خواهند کرد</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20826" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ درباره ایران:   همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20825" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ درباره ایران:
همه چیز به‌خوبی حل خواهد شد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20824" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده در آستانه گسترش تحریم‌های ثانویه علیه ایران
بر اساس اطلاعاتی که یک منبع آگاه از برنامه‌ها به
رویترز
گفت، انتظار می‌رود وزارت خزانه‌داری ایالات متحده دامنه تحریم‌های ثانویه‌ای که می‌تواند بر شرکت‌ها و کشورهایی که همچنان با ایران تجارت می‌کنند، اعمال کند را گسترش دهد
این منبع گفت که این اقدام به عنوان یک هشدار نهایی به کشورها برای قطع روابط تجاری با ایران انجام می‌شود
انتظار می‌رود اسکات بسنت، وزیر خزانه‌داری ایالات متحده، جزئیات بیشتری از این تدابیر را در یک نشست خبری در ساعت ۱۳:۰۰ به وقت شرقی ایالات متحده (۱۷:۰۰ به وقت گرینویچ) روز دوشنبه اعلام کند.
طبق گفته منبع، بسنت همچنین یک کمپین فشار اقتصادی گسترده‌تر علیه ایران را ترسیم خواهد کرد که او و دونالد ترامپ، رئیس‌جمهور ایالات متحده، آن را «روز D اقتصادی» نامیده‌اند.
این منبع گفت که انتظار می‌رود بسنت روشن کند که کشورها باید بین همسویی با ایالات متحده یا ریسک قطع دسترسی شرکت‌ها و نهادهای بزرگ از سیستم مالی مبتنی بر دلار، انتخاب کنند.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20823" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20822" target="_blank">📅 11:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مرزهای بازرگان و بصره بسته شدند.
مرز بصره جوری بسته شده که تیم تاج برای سفر به بصره جهت میزبانی بازی های آسیایی (سبحان الله چرا بازی پرافتخارترین تیم ابرقدرت چهارم جهان باید در بصره باشد اصلا؟!) به مشکل خورده!</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20821" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5jY7Yqm0LkogCA0eV9AXC6RsJRpKrNE_EaH38Z_aaiZV4McQQ3LiYn5A95fDyUJvRVyC-eSfqGPvPtug4k1Js274PKYxL14L7WvRGDXyjqCIhq9zkHQbwE_x8IIRIt88E-tEGMAJ4sygGkCumr_VD3gwqNdYsxs0I4I-lGqZnIBbo46MXRFQeb2pquLGmxno3djhBxibLdnEgPzs2LTcCztYOT79h1RzoV2CRessbD2uj4mz4c7VbOK5cPiRvlAdpREJ-_Rw-8p7OfsDzwrr0lEKDKf9VlpVHG0Vbvn_WTq4iQAO3qLfZqJLtm-cqH_EZY4xDVnEOvwedl-aW13SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…
توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20820" target="_blank">📅 08:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">— یک مقام اسرائیلی به کانال ۱۲ گفت که کنترل حوثی‌ها بر تنگه باب‌المندب «خطرناک‌تر» از وضعیت فعلی در تنگه هرمز است و به جغرافیای این آبراه اشاره کرد.
کانال شرقی حمل‌ونقل دریایی در نزدیکی جزیره پریم تنها حدود ۳ کیلومتر عرض دارد، به این معنی که کشتی‌ها در محدوده دید مستقیم از مواضع حوثی‌ها عبور خواهند کرد.
«آن‌ها قادر خواهند بود با موشک‌های ضدتانک به هر چیزی که بخواهند شلیک کنند. آن‌ها می‌توانند کشتی‌ها را با چشم خود ببینند. این همان تفاوت است.
در هرمز، ایران به رادار، سیستم‌های نظارتی و موشک‌های ضدکشتی نیاز دارد تا ترافیک دریایی را تهدید کند. اما در باب‌المندب، یک جنگجو با یک موشک ضدتانک ساده در جزیره میون می‌تواند به یک کشتی تانکر شلیک کند که می‌تواند آن را به صورت فیزیکی ببیند،»</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20819" target="_blank">📅 07:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">— دادستان‌های فدرال آلمان هفت مظنون عضو حماس را متهم کرده‌اند.
به گزارش‌ها، اینها در حال برنامه‌ریزی برای انجام یک حمله مرگبار علیه اهداف اسرائیلی یا یهودی در آلمان یا اتریش بودند.
این توطئه تا ژوئیه ۲۰۲۵ به مرحله عملی رسید و قرار بود در دومین سالگرد حملات حماس به اسرائیل در ۷ اکتبر ۲۰۲۳ انجام شود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20818" target="_blank">📅 07:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران
به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.
در این حمله ۳ نظامی آمریکایی کشته و چند نفر زخمی شدند.
آمریکا نام شرکت‌های چینی را اعلام نکرده و چین را مستقیماً به مشارکت در حمله متهم نکرده است. پکن نیز این ادعاها را رد کرده و خواستار ارائه مدارک شده است.
نگرانی اصلی واشنگتن این است که ایران از تصاویر ماهواره‌ای چین برای شناسایی و ردیابی نیروها و شناورهای آمریکایی نیز استفاده کند.
اگر این ادعا درست باشد، همکاری ایران و چین وارد مرحله مهم‌تری شده است: انتقال اطلاعات ماهواره‌ای می‌تواند دقت هدف‌گیری موشک‌ها و پهپادهای ایران را افزایش دهد.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20817" target="_blank">📅 06:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار در استان خمیس مشیط عربستان سعودی</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20816" target="_blank">📅 00:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SBoxxx/20815" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1ti8755wMsuLacuNXf30sHaQq56NJld0xyQ-uSi7GcvxA7Sue0UnaApm0WcGkXRvROwInhg4NR7Av74G32sSUx6Kkg7dbrvfi5HYLeSzyAamJRBVMn7sCSs1QxV3mn8fisut8j5Ib-LU1T4DfTU7bK3o5ENwznUiII4gxPETGgr1rd-lFmfjYW3o3C-nEXB_SRN25-GDUHkqrJRkiGdbXfmFPozdc66Qvw4-ZAlt72sQWScN9Xzij3RUWiVO6EErIPMg0QwfEvfEBhqjf2JNXmmunNCouF-VMti9ALc_T_KR2YKUMX2M0ajl5oOQBhsRIWOEBf1ZjeLvhKATpZpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/20814" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">— ۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران ایران یک موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20813" target="_blank">📅 20:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=U7hNh8fA7Iv-VcpBORQAJL-1hLPtoanV4_nXCwhWRzpLgF8sm52-goxdPykfhJhLTSWoKTNzdEKL_ozK4lP3TSjYMnNKg_IDVgp_tPHDMlglhdnWNE1SHrXG75DUFNYk9qlhegxAOcUJ7u85jg1iM_nzYJAyfp-DXFN_KWrc1D3Xp9d459BJ5VYicDJyv9x93HkjPRao7fGjfgDXx7W9Ia-tv9U213sPInwOr3UFuGRJ_DHocxhQ3XGEXpT2Ff9OQmaB5_wipihHP1lb0s2sd9gdCPi-selTPw0Y4cc37thFi55d9E686IDmnaYKOEEP275wDjFWY1CxmTM1jaIfhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=U7hNh8fA7Iv-VcpBORQAJL-1hLPtoanV4_nXCwhWRzpLgF8sm52-goxdPykfhJhLTSWoKTNzdEKL_ozK4lP3TSjYMnNKg_IDVgp_tPHDMlglhdnWNE1SHrXG75DUFNYk9qlhegxAOcUJ7u85jg1iM_nzYJAyfp-DXFN_KWrc1D3Xp9d459BJ5VYicDJyv9x93HkjPRao7fGjfgDXx7W9Ia-tv9U213sPInwOr3UFuGRJ_DHocxhQ3XGEXpT2Ff9OQmaB5_wipihHP1lb0s2sd9gdCPi-selTPw0Y4cc37thFi55d9E686IDmnaYKOEEP275wDjFWY1CxmTM1jaIfhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین توزیع قند و شکر کوپنی در دهه ۶۰:
عبدالناصر همتی
، خبرنگار صداوسیما در میانه گفتگو با مردم به مصاحبه شونده می‌گوید:
«اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره!»
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20812" target="_blank">📅 20:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjGHnxa3sD6PDiDA9I-nAuxDyyVD59ZmLP7hdoWeDDG8ujmrvstXymyVJmPT4LIRWSeHE3hm5vF8bd8IwlLVgnNkYAVWIkK5mhV6qzvrw5ednz033Jtfl2mpgGOMkVJl0kandjy8EyfdobUy21BEV_1Cqm9huYp69C3wIgDDrMq3vI0tdKm41jlGurGwDjOhC3PMROgl4ijKaP9qbVNWJPoYBcreiM9wqzVvXjX-Fl-oBMZlqXPg9XiSJRa4oaSXbUciCmh35LVG0qVSZkI9zu2k99KISIUkO-t-oK96NTKFDdBi71okslnQWLfhv1NF-DEBbYRyosJpkuWlb4satg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20811" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مرتضی محمودی نماینده مجلس:
اکنون که قیمت نفت بار دیگر به 110 دلار رسیده از نیروهای امنیتی التماس میکنیم یک مدت کـوتاه هرگـونه وسایل ارتباطی و متصل به اینترنت را از دسترس عـراقچی و همتی و مشاوران و دستیاران پزشکیان و قالیباف‌دور نگهدارند تا قیمت ‌را در این جنگ اقتصادی کاهش ندهند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20810" target="_blank">📅 18:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ:
ایران بزرگ‌ترین حامی تروریسم در جهان است</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20809" target="_blank">📅 18:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6eQ0Zcj_gWwCJQMLizm10V74Dx7A3wGw_fWnb5jWox4QJyPeXDhCZrusytyDfJFrmQXcwjX1FbFkpua6thZ3_mOtdyepOEp5TcHPK104UmkGGsYeFzloooEe0JGvpkTcfTMq_La-277jFDisVlM_KLEs1qT9gMIUPEPkTaPJpCPtX-mgkWOh7FjOQAl0ULDOXcLAS88No1p7V4SaWTL51WwTWMY2vv9qRntDmQJ9Jp4dSKKC5vwZ7V2X24tN5Yn_FqKpx96ntyo-r3LoJnKC2us0OcOdP-8sLpl_lCZaF1w7Svdco2lGohxtF4HKNzLlFd4CbmuetCDzLK9cAkO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟
اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از یک درگیری نظامی به یک فشار اقتصادی و مالی گسترده‌تر تبدیل می‌شود.
در این چارچوب، ایران می‌تواند از ناامنی مسیرهای انرژی و افزایش قیمت نفت به‌عنوان اهرم مذاکره استفاده کند؛ هرچند این راهبرد دو لبه است و در صورت تداوم، ممکن است هزینه‌های اقتصادی و سیاسی قابل‌توجهی برای خود ایران نیز ایجاد کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20808" target="_blank">📅 18:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv-H6ZmOvn0AjJybSO62sR7MBYlWte082UioNyn3SapHZIoV0AsiINAoOzNNQXAX_KHiPt_MwmCNEjJzPAFhlc7A4-1XdGAKH1FsW8hyIJfygHgbOahUJHzV5tOCgzGM6VmR3FjOx2sK0PWElZ8nVJa7PQH3y6qTsyXSxh5cb1yWtN88hJliKWm8X7j92u67hObfKMhAombIgagVDxPhYgPc1TofVm83tE7gnWfB6ybbaOHaTFF2HSNj6JsW2yxBWkZfateRvfWCOjhj3M-eC6aGhVeGHD4xQrla6DXlezEJeatk8MB_GNOZhT0iyayRvsdYwjRWkH52hY58sXDtEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس یادگاری روسای کشورهای بریکص</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20807" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.  نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20806" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20805" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 26
جمعه 11 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20804" target="_blank">📅 13:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIdrLkiQIsY2Vx_MGwup8M39UvSJkNfJN-494Uzz2D1CVNx07twhOdLiYVbZIKQhmejTp6LGgkItagdl5vjRo3dTnGqX6DEuR9fxQV7QyaK74mB9y7P0PYefUAKZCEPdehnfy2XvRIpfxEJaXq--MWVhmMouG1N9I7PjcUKHjNqMqLoeNbpA9FFscqKLGZCCb24_Wb_at2-shsbVqsiJZgqVDXTZ-OjCq2daP52GMJhocMcVTSl8mjxwhWEhM0g8CcgF1fDuXs5vj7E4RdM3QD6eIlUFTTgaKbKibo_eL5DMl_7MYxUUHiVu-rVWDzc6qx2OmSlZKpRXbsprVGrcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20803" target="_blank">📅 12:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20802" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20801" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20800" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9kcLAdHuDPsKJfoyCVgBfJOpIZl2Wq18sVVQueqb76ZTRhMliHgX6Lr6eZZ7-ti7_jBqdrqvZDKrgOxQjGSaGu3lAibBX14e6KOBtGrj8zmTZOUEQI_8is-FhY_tpic5Ocm1V8-tqdTjMSf2Ac-nfDOaJ8yuWb-TFJMX_r2_NhgWm3ydSvacwENnPcA_5_xbnI_L-7upo-KFV2LwadaMYs-2I91_UYb4L4KJQqvNx9R2vmOAgAUy9XaAi3r2Hjt_-PDobuSUha__k4yNeriz6hpCDtSCmCCEX8PGq_iQzx1sr-JKBj_Q509KFONVUEH5YvTBKN1bVaWFtFPfeBgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.
نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20799" target="_blank">📅 11:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPJ9lnxB9z8mvjz8dB1vO1RL45btzE5a2z0PG29P_693B3Zt6MmVbG7CKhIQhaGwzanEzxQiSevuk7iHICBEopELnw8qLUC3Ny0zJVuJhsVeWboxdcQSkWiyLgDnvOSRr4jNQPgLOdk2UB0DFqxmyd2D06Wv2hcrfRDnDfXO5T66E5WFJBc_ufIqWqI132cpi61MGSiQrHNXmHpbDu_ZoT8QVoZwh5sMrJi7f1l5w84C4vhjlJXtC-5dQdWIR2noZSMdGd6wfiCsDiPfEH5Kx2RDHshtAB3JPLn3WiLdJbq98Z4zJG0-6jaVcOYQtpGEySWCZPhNYO0E6WMy0c5tow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جهش بهای نفت و تاثیر آن روی تورم تولیدکننده در آمریکا
جهش قیمت انرژی، به‌ویژه نفت، تورم تولیدکننده آمریکا را در اوت بالا برد و
فشارهای قیمتی را دوباره پررنگ کرد.
حالا بازار منتظر CPI است تا مشخص شود این شوک انرژی موقتی است یا می‌تواند مسیر سیاست پولی و قیمت طلا را تغییر دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20798" target="_blank">📅 11:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گویا امروز حوثی ها این خط لوله را هم در 6 نقطه هدف قرار داده اند!  با ادامه این وضعیت یعنی عربستان حتی از مسیرهای جایگزینی که طراحی کرده بود نیز نمی تواند نفت صادر کند!  به نظرم تشدید تنشی بسیار با اهمیت است و از دلایل جهش بی سابقه نفت در روز گذشته</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20797" target="_blank">📅 10:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFahtN1c5iQ4GxXH2SugBdCny-vPJP3_OskpwblrcmDJ3OngnqVO6e3LW7r1IRlPKxz68pESHOM0rs4WDCuK-4VdttOC0iCVngizZB6guODhVtkGV4wG2o9tWDWsyuoW1gYaNLsCGBG4QSC1LEZhmnZA1h-g94zPpwqD40o3xRrAoPLRYMAlO3fBU6Mzf2hgrgDX7BNY1vVQKqULcNWFuWeigBm0odtj7r4YgUqva4DWXlqMaAlQ4Q58pxHFED8fsOQtoRcYW-3voLmS2iNlBnpuxo0EcygkmA1v9aqPfV6KYoKkaQZg82n8V0nekK7p1ORARkZfKi9R03xhYv971g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای درک حجم و‌ عمق بی لیاقتی و بی عرضگی ارتش پفکی سعودی کافی است به این عکس یادگاری جنگجویان حوثی که پس از تصرف بندر راهبردی مخا گرفته شده نگاه کنید!</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/20796" target="_blank">📅 10:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حقوق ثابت نماینده‌های مجلس ۵۰درصد افزایش یافت و مزایای جانبی نیز افزایش پیدا کرد</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SBoxxx/20795" target="_blank">📅 01:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی ها هم می خواهند یک خط لوله از بصره به این خط متصل کنند</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20794" target="_blank">📅 00:56 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
