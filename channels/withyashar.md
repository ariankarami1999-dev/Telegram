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
<img src="https://cdn4.telesco.pe/file/Odo-CiZDYxRAz0GKWVkNbjiIPewYhLmKRuEy46bBk7POrniTiCvGy1ep0wuBCGdUIJua9iXlWxQMWmtzF1jpBWiEfht2xtYVD6zWZddSCbwSBaRdf5E7LIPqe-rBzWCx_hNIVjw1xPJiym98nM45u9qKfr5YuzirqgkoE4gM0dxFaf8lJEs0tkcgd8CdhjJfCMhDuE0wwHHcHp7wRZqqBzLtTjasSdTq7T-wtNr-FTXuRAdUULwlpR12lrEmAqtqY_NphxB6SxN04r6nfUcEb-Ta8PXDKosL18AZ1rOwzBiZ7oh0aKr9WehSQXtkMLOXeH5OWGUIxYpYkRTUjcE3YA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 327K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-14722">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الحدث به نقل از منابع آگاه:
منابع حاکی از آن است که یک هیئت ایرانی، شامل وزیر امور خارجه عراقچی، فردا وارد پاکستان خواهد شد.
هیئت ایرانی بر مذاکرات فنی مربوط به این توافق نظارت خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/withyashar/14722" target="_blank">📅 17:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14721">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS441IIjH-gTxhKD07LJjB-GRQzhw9pGjIPV2VqAgfUaiGvPrY6iFhKhdqeoS71zpgmBh_nu7XCPsRIhQaFqtsjSc2m8RceQYNfln6CRNOewosfbub8OzQzlBrfLRa-wQlLUplJ1jj0Xnt0hQt_QjBLZS9SJeM0bEpUbl1FWSKEFzXvD4PtBE_u84MaUlU0zlCewHJ1JsYwuqp0eINYYS4vHp94rwqbjmlEXBz-Up_E_wQjnwH7slLRtHWy01mx2QCdaQ203cOBqz9CkZFn-hmS_dmzKBTQiyFX04ahpXx7eNfQbAieS315bfvpzkXHzikDHvi8-zaRCBvyVqbwmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ توییت شهباز شریف نخست وزیر پاکستان را در‌تروث منتشر کرد :
شهباز شریف: «ما اکنون بیش از هر زمان دیگری به دستیابی به یک توافق صلح نزدیک شده‌ایم. با توجه به اینکه
انتظار می‌رود این توافق طی ۲۴ ساعت آینده نهایی شود
، پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق صلح بلافاصله پس از نهایی شدن آن است و پس از آن نیز گفت‌وگوهای فنی و کارشناسی در هفته آینده برگزار خواهد شد. مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به دلیل تعهد و همکاری مستمرشان در طول مذاکرات قدردانی کنیم و همچنین از برادران خود در منطقه بابت حمایت‌هایشان صمیمانه سپاسگزاری نماییم. ما اطمینان داریم که این توافق صلح تاریخی، بنیانی محکم برای صلحی پایدار و ماندگار فراهم خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/14721" target="_blank">📅 17:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14720">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال های خبرگزاری فارس، بابک زنجانی، صرافی نوبیتکس، والکس، رمزینکس و بیت‌پین که تو یوتیوب فعالیت میکردن، به علت تحریمای آمریکا همگی مسدود شدن
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/14720" target="_blank">📅 17:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزارت خارجه آمریکا بار دیگر درخواست ویزای مهدی محمدنبی سرپرست تیم جمهوری اسلامی و مهدی تاج رییس فدراسیون فوتبال رو رد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/14719" target="_blank">📅 16:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egccOcIlsd6QwU6o7I_75DwWOavwJ5l4lFEC-0-f1KpgGryC_W0ik2QqI7Y6eUenWC5xXrdD1z_CfPRqu4ypize-HB5dQsOft8flyugzjI29Wy-9yHrTV71uE-Ki43tymMUINSSXjFNJbjKMbIQWfWndP_8TKViWr2vxVAL3JUX8zd3P61cj7_iTypvPepMLbelVLQKTNpKd2G_tJ-MxSk4tQXyPmp8U2KAMJhSGZU9oQUFhZ8Oagw6YbPo7jZUNLoxfgThgWRj5eFlVBdA_ezD3AHVN3fnAFKNCVS_icvf_pKUYLOLvExrxuH8oEC5OcYyBlYngtSvvncWf4EemQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">16 تا نماینده مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌.
@withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/14718" target="_blank">📅 16:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بقائی، سخنگوی وزارت خارجه:
درباره زمان دقیق امضای تفاهم‌نامه باید منتظر بمونیم؛ اگرچه فردا نیست اما احتمال اینکه در روزهای آتی این اتفاق رقم بخوره منتفی نیست.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/14717" target="_blank">📅 16:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نماینده مجلس خطاب به  عراقچی وزیر امور خارجه:
مذاکره بعد از حمله نظامی، دیپلماسی نیست، مستعمره شدن است
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/14716" target="_blank">📅 15:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14715">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر آموزش و پرورش: به خاطر اهمیت حضور دانش آموزان در مراسم تشییع، تقویم امتحانات نهایی بازنگری میشه و احتمالا تاریخ امتحانات عقب میوفته
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/14715" target="_blank">📅 15:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بعد از پخش آهنگ امیر تتلو از زندان که پشت تلفن اجرا شده بود، زندان تهران بزرگ تلفن او را مسدود کرد و تنها دلخوشی او هم گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14714" target="_blank">📅 15:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14713">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی به‌احتمال زیاد در جریان آتش‌بس، سلاح‌های پیشرفته روسی رو به ذخایر تسلیحاتی خودش اضافه کرده.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/14713" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14712">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/14712" target="_blank">📅 14:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14711">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نخست‌وزیر پاکستان: متن نهایی توافقنامه صلح بین ایران و آمریکا به دست آمد
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/14711" target="_blank">📅 14:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14710">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جزئیات مراسم تشییع و تدفین علی خامنه ای رسما اعلام شد
شنبه و یکشنبه
13 و 14 تیر (19 و 20 محرم): مراسم وداع با پیکر در مصلای خمینی تهران
دوشنبه
15 تیر (21 محرم): مراسم تشییع در تهران
سه شنبه
16 تیر (22 محرم): مراسم تشییع در شهر قم
پنجشنبه
18 تیر (24 محرم، شب شهادت امام سجاد ): تشییع در مشهد مقدس و سپس
خاکسپاری در حرم امام رضا
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/14710" target="_blank">📅 14:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14709">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بلومبرگ به نقل از یک مقام آمریکایی:
در صورت تحقق شرایط، واشنگتن تحریم‌های ایران را کاهش داده و اجازه ادغام این کشور در اقتصاد جهانی را خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14709" target="_blank">📅 14:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14708">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فارس از احتمال حملات سایبری به ۴ بانک خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/14708" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14707">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تا دقایقی دیگر نحوه و زمان خاکسپاری خامنه ای را قرار رسانه های رژیم اعلام کنند.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/14707" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14706">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">واشنگتن پست به نقل از یک مقام دولت ترامپ: تعیین میزان پولی که ایران می‌تواند به طور بالقوه دریافت کند دشوار است زیرا بستگی به آنچه آنها ارائه می‌دهند دارد.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/14706" target="_blank">📅 13:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14705">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دولت عراق خواستار تحویل سلاح نیابتی های سپاه وخروج هرچه سریعتر نیروهای سپاه از خاک عراق شد
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14705" target="_blank">📅 13:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14704">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">از صبح امروز شنبه ۲۳ خردادماه، سیستم بانکی سه بانک ملی، صادرات و تجارت دچار اختلال و قطعی شده و تا زمان ارسال این خبر همچنان مشکل ادامه دارد @withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14704" target="_blank">📅 13:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/filrLy8nZ7hMqolNyHjoiKaBzOJuhtE8Tp33Hz7ejNDT7WvHgk-I8ms8xjZs3wV3ZEhDzbg5VmwrayN6ow8pt-npb1p3Uww82nz7rKOFFWbrvHT9xvij5YjzisAwJpOX9kXR9KAi6wPOCxUU5g0sBe2ZXSutOzSyDYZBfJLyBW7RociewAF5BtLICdPf9Cu90v6F8nmK3OMC2UVDVY9IdUcsegErRjgNGl7ct-Ydhl81tN4fMgMJpXKaAllQ3ETIaQ6mFgfqI-KmbvpaCmvuDTk7aPUVc_PxJdKoG2mUk85XLDWWtO6ZdOrvxCnQ82h8TZZMefI81chb916Wt6zekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنوب لبنان؛ ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه «یا حسین» نصب کرده
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14703" target="_blank">📅 12:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">از صبح امروز شنبه ۲۳ خردادماه، سیستم بانکی سه بانک ملی، صادرات و تجارت دچار اختلال و قطعی شده و تا زمان ارسال این خبر همچنان مشکل ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14702" target="_blank">📅 12:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هوش مصنوعی رقیب جدید مدرک شد
نتایج نظرسنجی موسسه پژوهش‌های اقتصادی «ایفو» نشان می‌دهد :
۲۰ درصد از شرکت‌های آلمانی استفاده‌کننده از هوش مصنوعی معتقدند که می‌توانند کارکنان دارای مدرک دانشگاهی را با نیروهای مجهز به ابزارهای هوش مصنوعی و بدون تحصیلات دانشگاهی جایگزین کنند.
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14701" target="_blank">📅 12:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">️اسکات بسنت، وزیر خزانه داری آمریکا اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته (میلادی) یا اوایل هفته آینده نهایی شود.»
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14700" target="_blank">📅 12:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">روزنامه خراسان (نزدیک به قالیباف):
تفاهم ایران و امریکا قرار نیست اختلافات را حل کند؛ فقط یک فرصت است که طرفین خود را برای جنگی دیگر آماده کنند
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14699" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14698">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWT0KndEen4FLZ4zCePeemgeIq2ZahVKfk4MVbETSqbFcz8C66HBjVQ-NYq5gwqIbNZLSiOY9GHmZ7BMBnW6iT_JmWNkWM2xCAxwM8KL0C1vo4uP94vf49quiz0AS2qxplhaURNutyyI4o_8VBlMvhxTjJ-QdRrpAjluPcdGXvoP8pT4dMUFRbojlysX4RDe9M1hQXSxmRsbrSeygexdYeMBmJ5iWWiLdx-a6usWgqbuzQ8WnA3Z3GpiT1b1ldhQw3Qrw-r0Xa7tMgSiQoc1J3kncLIUvOf1FcOmqUSZsCcNjkUy3MmU4LCPoIDQDLufq_qj5XQyV5D9y9pmFfgmfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود الان کرج
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14698" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14697">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به ادعای CNN: ایران بخش‌هایی از ذخیره اورانیوم بسیار غنی‌شده خود را با ریزش تونل‌ها و مین‌های انفجاری در اطراف ورودی‌ها مسدود کرده است. این اقدامات در پی نگرانی‌ها از احتمال عملیات آمریکا برای تصرف این مواد، دسترسی به اورانیوم را به‌طور قابل‌توجهی دشوارتر و خطرناک‌تر کرده و تلاش‌ها برای حذف یا نابودی ذخیره تحت هر توافق آینده را پیچیده می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14697" target="_blank">📅 10:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14696">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرنگار آکسیوس باراک راوید: نتانیاهو امیدوار بود که جنگ منجر به تغییر رژیم در ایران شود، اما رقبایش اکنون او را متهم می‌کنند که با پذیرفتن شرایط آمریکا، اسرائیل را به (دولت دست‌نشانده) تبدیل کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14696" target="_blank">📅 10:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14695">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارتش اسرائیل، هشدار فوری تخلیه برای ساکنان ۲۰ روستا در جنوب لبنان صادر کرد! پیشروی در لبنان به سرعت ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14695" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14694">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYVRYRMCCT2JUIttUVUoSzegGht-NI_JRoHK68BuUg3H8xGLaqVmrzuZS6RPPH74tEjEGnzeE-02JuTPY6WEozzUbJYX_DopuwtpsKhsGiWc9WwGatz0y41xvMJ9fTHQeaONTNHyABVin-AREeVfeFAzAAYFdVJhsVoxci0Xfxyh0x7mRtI0QB_0r5Pranc6uftpL8IOV9RNKOI1zkwBiecqvMlpyLIcganfpizMmg_NWJM6yiAElp0nfJ8_Sh_fjCnAXx-cA8EstkC940UJUzKOAnfrw2_bQBpzEHBbs6xQgb5HFarPUvABpZ1kG6I--EK4mbqbStcUgRq2Yw7Kyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام (فرماندهی مرکزی ایالات متحده):
«ایران چندین پهپاد انتحاری (یک‌بار مصرف) را با هدف حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد.
نیروهای ایالات متحده در ساعات اخیر همه آن‌ها را سرنگون کرده‌اند و جریان تردد دریایی از طریق تنگه هرمز بدون هیچ‌گونه اختلالی همچنان ادامه دارد.
این گذرگاه بین‌المللی تجارت همچنان برای عبور و مرور کشتی‌ها باز است.»
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14694" target="_blank">📅 10:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14693">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">صدای انفجار دزفول ناشی از امحای مهمات است
از ساعت ۱۰ تا ۱۳ امروز شنبه ۲۳ خرداد، انفجارهای کنترل‌شده در برخی نقاط شهرستان دزفول و خارج از محدوده شهری انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14693" target="_blank">📅 10:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14692">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اکسیوس
:
برخی در واشنگتن معتقدند حتی اگر توافق اجرایی شود، نتانیاهو ممکن است بازهم بتواند نقش یک اخلالگر را ایفا کند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14692" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14691">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مقام اسرائیلی به یدیعوت آحارونوت: ایران هربار تصمیم بگیره در حمایت از حزب‌الله به ما حمله کنه، فوراً بهش پاسخ نظامی می‌دیم.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14691" target="_blank">📅 09:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محسن رضایی:
ترامپ با آزادسازی 24 میلیارد دلار از دارایی‌های بلوکه‌شدۀ ایران موافقت کرده اما با صراحت این موضوع رو اعلام نمیکنه.
@withyashar
🥴</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14690" target="_blank">📅 02:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeHMgVq98Xv53vjSlWjvNT4F5vgBXKiB9GcaOVTwmJhWwS_dVwja1ysfgybLyueV5DZwRw5xmXtJh4NM920Od17U1Hm2R7RcDL7e744v6Q4xdlvtvsncQj9NlyoZKgZc4StRly4gLUvbvRS7JOY58npyg3GXSFjpVsI2AVdpMmbOu4AWkreYssznE7gb3AZ9Ee49Sx3JVo2Gzssqd9mFlMgCA-__1a9fAsdpqeqRlF0Y51IsxX0jtRA74DX7gKYr8syCDt7O0m1AvVIv1vWBX34rZwMU3bWiDWhxeSy7tTEA6v4SN5ix9FxjG-75WXCSZ-k5UouJ-NVmEeYLofL74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشروی ارتش اسرائیل در جنوب لبنان؛ ۶.۷ کیلومتر تا نبطیه
ارتش اسرائیل به شهر ارنون رسیده و هم اکنون در حال حملات توپخانه ای سنگین به تپه علی الطاهر هستند.  l بالگرد های آپاچی ۶۴ اسرائیلی نیز به تپه علی الطاهر حمله کردند.  با تصرف این تپه مهم رسما تصرف شهر نبطیه برای اسرائیلی ها آسان خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14689" target="_blank">📅 02:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14688">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Bombardier E-11A در منطقه توضیح در ویس @withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14688" target="_blank">📅 01:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14686">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRmKOUgtUlJj4oAjptE9KOok3obJ1WV7Bvge_oeY2-7hhAXgELTDeLnhBm4PRvBAuiKJbI2SPXcKmnNelShfp3f1mBl71WylyVIeMoPsAjTo1NCGXMLP5PWPhsmfvhb5VBg0syl-8bsYyOYm5loIYPri-pG7judFlSr9mcAqS4mX3xYGvcdpWCGMdoWtBbBPHe9ORB7WIsxKriZ9yFLm8kGkOEU0Iz1LbpuCOagkB9_wJcZGyo0WWgLDfrbVhDJqJ98Aupil81Z7rkV5kFcA9pndNtdvluS0KgVio3OwawUSh_UsdErPTMtqPhgfr0jrFq3YlxnldBQk4U1XdctxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Bombardier E-11A در منطقه توضیح در ویس
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14686" target="_blank">📅 01:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14685">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14685" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14684">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyX3utef_YyE3DLPyBIMMHQ6hMe8vMwfAcaf4kkX9E22KNeIujg26CoTle7PDGHOvH8TAt7VxEWb_J4q7bM6nM2tSGhZfDj0s-NlJG_q27S-VgPj6-o-D4jCpMdUi75dT9rXi4W_eS0rRRXVynDgmzmiommsKFnInTn6Jtb-zDcUqHZ4INyjJVpdsvutkxQiBWcdQqBjOLoyJeRzlYBgrHKADaI44jbplvFvq9iwrNXIMx3ip69KUrHQ3MpOgjbW5am3IoYe1x61DIkDr6mL6_BPEXtz0Qa7tu734Y8BzC69Tbn74ZtUWMjQHYnv3M_haNd582u8Zn1f3-CVSYI-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ادعای رویترز بابت آزادسازی دارایی های ایرانو تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14684" target="_blank">📅 01:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14683">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Khabam Nemibare Live(IG @yashar)</div>
  <div class="tg-doc-extra">Amir tataloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/14683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14683" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14682">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14682" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14681">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14681" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار :  باز‌ تنگه دعوا شد ، گزارش عجیب از حضور هواپیماهای جاسوسی آمریکا همه با هم. !!!⁩
https://www.instagram.com/reel/DZgA2cQxrjS/?igsh=cnM5b3ViejIxcm5t
کلیک کنید و کارهای اداری پست را انجام دهید.</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14680" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کاور  @withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14679" target="_blank">📅 00:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">۳پا : کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14678" target="_blank">📅 00:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1ff8xU_nN4vE7VqEqWljwp2w5X1B5dWF1dnxfmwf2_zGYVkxSU40EZr3PQochLeAMrDh_ETEpISK5yzV3XnXBYQM99zECG4xP4faihidC5YMu6tSyfQ4QEbAgYHen014nHEvOQqD9GBuPA_KQqa5D2eqmhoHkd4jrDWKrJpqIL-MesHXAJpvbD98JzTos99HJmXlWgVyopDFvV72Q4xdE9kn9IYtaPrOYeh81AFdXqn1J1IEOO0U_YGdtH6V96uOMusmuRXRxxpPL-xh4d8TIH3K_kPsSSsR0TvsL05KVXlbEa33EyV6ZDDWmwzazqR15g7oTOv6eWMiDGI10MrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14677" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14676">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تو تنگه دعوا شد
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14676" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مهر : شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
بررسی‌های اولیه نشان می‌دهد، در پهنه شهرستان سیریک انفجاری رخ نداده است و احتمالا صدای شنیده شده تلاشی برای کنترل تنگه هرمز و از سوی دریا بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14675" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14674">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14674" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صدای انفجار سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14673" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14672">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عراقچی: در مذاکرات ۶۰ روزه چند حالت رخ می‌دهد
۱. تمدید مهلت مذاکرات در صورت خوب‌پیش‌رفتن مذاکرات.
۲. نرسیدن به توافق، به‌علت بی‌فایده‌بودن مذاکره‌.
بستگی به شرایط آن موقع تصمیم می‌گیریم که اگر نتیجه نگیریم چه خواهد شد.
تنها کاری که می‌توانیم برای اورانیوم غنی‌شده انجام دهیم "رقیق‌سازی در داخل" است!
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14672" target="_blank">📅 23:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14671">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عراقچی:به‌زودی ایران و عمان بیانیه مشترکی در مورد اداره تنگه هرمز منتشر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14671" target="_blank">📅 23:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14670">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عراقچی: عوارض نخواهیم گرفت اما هزینه خدمات میگیریم
ممکن است در دوره ۶۰ روزه این مورد کمی متفاوت باشد
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14670" target="_blank">📅 23:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14669">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عراقچی:  این توافق دشمنایی داره که اسرائیل اصلی ترینشونه
امیدواریم تفاهم‌نامه امضا بشه ولی اگر نشه وارد دور بعدی مذاکرات نمیشیم
اگر قرار بود به تهدیدهای حمله به زیرساخت‌های خود تن دهیم، قبلاً این کار را انجام داده بودیم.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14669" target="_blank">📅 23:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14668">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عراقچی: به صراحت میگم که این توافق دشمنانی داره که در راس آنها اسرائیله.
سکوت کنن رسانه ها که برسیم به توافق خوب
وقتی ما به توافق میرسیم که دو طرف راضی باشن
حالا توافق 50/50 هم نیست و درصدش مهم نیست
مهم اینه که توافق کنیم
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14668" target="_blank">📅 23:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14667">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عراقچی: نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم
بهترین زمان برای پایان دادن به جنگ زمانی است که دست بالا را داریم؛ ما واقعاً در میدان نبرد پیروزیم.
ما به مدت ۴۰ روز در برابر ابرقدرت ظاهری جهان ایستادیم.
توافق و پایان جنگ، پیروزی را تثبیت خواهد کرد.
توافق نهایی هنوز حاصل نشده است؛ اگر نهایی شود، قول می‌دهم هر بند را به طور کامل توضیح دهم.
توافق شامل دو مرحله است و ما مسئله هسته‌ای را به مرحله دوم منتقل کرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14667" target="_blank">📅 22:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14666">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15f030f45.mp4?token=XGWIM2nfXVIHO-9arNufyBomV0d2tKAMgyF3W4V_I3KcLpLIo7voNEpMR3X4Re8sigSx7ZrtNPs-1unizuMA58Jmg4cXyFpjEkmnUMYZMhrbU2LT1eqv5djUWVu5L_g4fmpZGcNwsfQXMsgmZ8-T4pvCS2gGjdQd34o90tEImHzoR9wmot92-GwuRtQRb316t3ndLcpExofIR4g1n2ygXuKoDEWfM8lpXLczZ1-i6iEzrVHRXN2D6ZjSIK5Jrt-_38sb_muiWBYL8swpDFD0mUbMErBWAKijEmFQJO31gQDltkgvlVxg5fMNFZucRCZ_pwPGVtcT-i80qfrq87pk5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15f030f45.mp4?token=XGWIM2nfXVIHO-9arNufyBomV0d2tKAMgyF3W4V_I3KcLpLIo7voNEpMR3X4Re8sigSx7ZrtNPs-1unizuMA58Jmg4cXyFpjEkmnUMYZMhrbU2LT1eqv5djUWVu5L_g4fmpZGcNwsfQXMsgmZ8-T4pvCS2gGjdQd34o90tEImHzoR9wmot92-GwuRtQRb316t3ndLcpExofIR4g1n2ygXuKoDEWfM8lpXLczZ1-i6iEzrVHRXN2D6ZjSIK5Jrt-_38sb_muiWBYL8swpDFD0mUbMErBWAKijEmFQJO31gQDltkgvlVxg5fMNFZucRCZ_pwPGVtcT-i80qfrq87pk5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند مشهد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14666" target="_blank">📅 22:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14665">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14435d52ae.mp4?token=sFU-XArnXFGp5aiZRq8RyfHEkcwxzob872c5HZiJshc2lM97taVegHFQCpCMhlYUrhsZLE8c4xJYTL5bi-P1xgsBPsvSirthwi_f8CazWzoUzthxPAixHpJpjzG38yUdoEZsmFWVNCJSmjNoEYGHAPcOjmPk8bnZYtPM0gWYfoGfI1PUyIxcFgGUOCniDUy34fLi1IVo-T0zLBGXaKFISbV2Y-drQLIR0EChHz79TA0i_n2up9ZYQkQE-JqmWsIdIUCA5Q1CCU1xW4_VM3ZES6UgGZx9zYMy1sKsUOQKa4PuhlzbSH1hp34XyCDCJuvtwQkRFKWsuVAvDhRD6Cs52g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14435d52ae.mp4?token=sFU-XArnXFGp5aiZRq8RyfHEkcwxzob872c5HZiJshc2lM97taVegHFQCpCMhlYUrhsZLE8c4xJYTL5bi-P1xgsBPsvSirthwi_f8CazWzoUzthxPAixHpJpjzG38yUdoEZsmFWVNCJSmjNoEYGHAPcOjmPk8bnZYtPM0gWYfoGfI1PUyIxcFgGUOCniDUy34fLi1IVo-T0zLBGXaKFISbV2Y-drQLIR0EChHz79TA0i_n2up9ZYQkQE-JqmWsIdIUCA5Q1CCU1xW4_VM3ZES6UgGZx9zYMy1sKsUOQKa4PuhlzbSH1hp34XyCDCJuvtwQkRFKWsuVAvDhRD6Cs52g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشهای زیاد شما از مشاهده چندین پهپاد شناسایی هم اکنون در آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14665" target="_blank">📅 22:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14664">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea29ba51ad.mp4?token=mim3eXLTitZ-TGWmQvIB0HdESeHI5L0Zfp3I8r_4buYpAjMlVnMf285mBqEkctPSK-5_WHaE6cN2Elr3pkFUaCG4880XSM5B4151i8GQDsLiAnAYK1BWzFyzDBxw4j1tKoSBokqQnk6p05EUzpcrjLdeZkqn6AXCfFt1bcL_Qe1Za7RhZjyFqN1YR-3ZIas_pC-BsG4Uc4b8ije15ODBVKsOWNAouXT5WmK9srq4u1L1fee5eh-_y4iRB7Hnl-s3kOxrQnUfunpXg4ojuFktz9Eb8UcER5vHkR9YRiuKEtofznOhFaCFStADK--POJHM61bXgmCESCCIagvh6_-vfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea29ba51ad.mp4?token=mim3eXLTitZ-TGWmQvIB0HdESeHI5L0Zfp3I8r_4buYpAjMlVnMf285mBqEkctPSK-5_WHaE6cN2Elr3pkFUaCG4880XSM5B4151i8GQDsLiAnAYK1BWzFyzDBxw4j1tKoSBokqQnk6p05EUzpcrjLdeZkqn6AXCfFt1bcL_Qe1Za7RhZjyFqN1YR-3ZIas_pC-BsG4Uc4b8ije15ODBVKsOWNAouXT5WmK9srq4u1L1fee5eh-_y4iRB7Hnl-s3kOxrQnUfunpXg4ojuFktz9Eb8UcER5vHkR9YRiuKEtofznOhFaCFStADK--POJHM61bXgmCESCCIagvh6_-vfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهام شرکت فضایی و موشک‌سازی SpaceX که تحت مالکیت ایلان ماسک قرار دارد، امروز برای نخستین بار در بازار بورس آمریکا عرضه شد و معاملات آن با قیمت ۱۳۵ دلار به ازای هر سهم آغاز شد.
عرضه اولیه این شرکت توانست بیش‌ از ۷۵ میلیارد دلار سرمایه جدید جذب کند و ارزش کلی اسپیس‌ایکس را به حدود ۱.۷۸ تریلیون دلار برساند.
در پی این جهش تاریخی، ثروت ایلان ماسک از مرز یک تریلیون دلار عبور کرد و او رسماً عنوان نخستین تریلیونر تاریخ را به خود اختصاص داد.
در لحظه نگارش این متن هر سهم حدود ۱۷۰$ است
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14664" target="_blank">📅 22:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14663">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حزب‌الله:
بر اساس آنچه مقامات ایرانی به ما گفته‌اند، اسرائیل بر اساس این توافق از خاک لبنان عقب‌نشینی خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14663" target="_blank">📅 22:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14662">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">طبق گزارش ها،فرمانده کل سپاه، احمد وحیدی با شرایط متن تفاهم نامه ایران و آمریکا موافق نبوده متن تفاهم نامه با همکاری عراقچی و قالیباف تنظیم شده است و پس از مخالفت فرمانده سپاه به رهبری در ایران ارسال شده،
رهبری در ایران نیز تاکنون مانند دفعات قبلی متن تفاهم نامه را تایید نکرده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14662" target="_blank">📅 21:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14661">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سازمان ملل: از روند مذاکرات دلگرم شدیم!
@withyashar
😁</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14661" target="_blank">📅 21:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14660">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار فاکس‌نیوز نزدیک به ترامپ از نقل یک مقام کاخ سفید درباره توافق :
۱. مواد هسته‌ای نابود و منتقل خواهند شد.
۲. برنامه هسته‌ای برچیده خواهد شد.
۳. هیچ‌یک از پول‌هایشان تا زمانی که تعهداتشان را انجام ندهند آزاد نخواهد شد.
۴. تنگه هرمز باز خواهد بود.
۵. هیچ تأمین مالی از سوی ایران برای گروه‌های تروریستی وجود نخواهد داشت.
این مقام افزود: «این همان چیزی است که آنها با آن موافقت کرده‌اند. این یک توافق مبتنی بر عملکرد است.»
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14660" target="_blank">📅 21:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14659">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الحدث: وزیر خارجه پاکستان امشب عازم ژنو می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14659" target="_blank">📅 21:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز:
توافق با ایران اهداف اصلی ایالات متحده را محقق می کند
این توافق تنگه هرمز را بازگشایی خواهد کرد، ایالات متحده مواد هسته ای غنی شده دریافت خواهد کرد.
توافق ایران همچنین شامل یک رژیم بازرسی است. اگر ایران رعایت کند، پاداش اقتصادی خواهد داشت.
منافع برای ایران تنها در صورتی حاصل می شود که آنها واقعاً به تعهدات خود عمل کنند.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14658" target="_blank">📅 21:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال 12 اسرائیل : سرانجام توافق شد ؛ این توافق قطعیه و به نتانیاهو اعلام شد!
ترامپ از ایران خواسته به‌صورت علنی درباره توافق شفاف‌سازی کنه و هشدار داده در صورت انجام ندادن این کار، با پیامدهایی روبه‌رو خواهد شد.
ترامپ در تماس تلفنی با نتانیاهو گفته:
«این همون توافقیه که دنبالش بودیم؛ یک توافق عالیه و وقتشه این جنگ تموم بشه.»
طبق این گزارش، نتانیاهو در این گفت‌وگو زیاد حرفی نزده و ظاهراً متوجه شده که توافق در آستانه نهایی شدنه و توانایی متوقف کردنش رو نداره.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14657" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آکسیوس: ترامپ به بنیامین نتانیاهو نخست وزیر اسرائیل خبر داد زمان پایان دادن به جنگ ایران فرا رسیده
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14656" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بقایی، سخنگوی هیأت مذاکره:
همین الان جلسهٔ نهادهای ذی‌ربط درحال برگزاری است؛ در مورد متن تفاهم ما در مراحل جمع‌بندی در داخل هستیم
اینکه گفته می‌شود ما خیلی به تفاهم نزدیک هستیم، حرف جدیدی نیست
مشکلی که ما در این مدت داشتیم اظهارات ضدونقیض طرف مقابل است.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14655" target="_blank">📅 21:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14654">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: جمهوری اسلامی به‌طور محرمانه بابت ارائه اطلاعات نادرست در مورد توافق عذرخواهی کرد.
@withyashar
😁</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14654" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14653">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ثابتی:متن توافق احتمالی از برجام هم ضعیف‌تره و نه گشایش اقتصادی ایجاد می‌کنه و نه جلوی جنگ رو می‌گیره
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14653" target="_blank">📅 20:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14652">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ : پست اخیر عباس عراقچی، وزیر خارجه ایران، درباره توافق را بسیار مثبت ارزیابی می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14652" target="_blank">📅 20:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14651">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ : هنوز هم معتقدم که توافق ممکنه تا پایان این هفته یا نهایتاً روز دوشنبه امضا بشه.
ایران به‌صورت محرمانه بابت ارائه اطلاعات نادرست درباره توافق عذرخواهی کرده
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14651" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14650">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر جنگ اسرائیل: رئیس‌جمهور ترامپ در حال حاضر به سمت توافقی با ایران پیش می‌رود که از دیدگاه منافع آمریکا، از جمله منافع مشترک با اسرائیل—برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای است و ما انتظار داریم او این اصل و اصول اضافی در حوزه موشک‌ها و نمایندگان نیابتی را حفظ کند.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14650" target="_blank">📅 19:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14649">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سناتور لیندسی گراهام:
بسیار خوشحالم که ترامپ گزارش رسانه‌های ایران را جعلی خواند، چرا که آن توافق افتضاح بود
آنها در ضعیف‌ترین وضعیت خود در ۴۷ سال اخیر قرار دارند.
ما نباید فراموش کنیم که نظام ایران ۴۲ هزار نفر را تنها به دلیل خواست زندگی بهتر کشت.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14649" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به گفته‌ی CNBC معاملات سهام  اسپیس اکس $SPCX تا پنج دقیقه‌ی دیگر آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14648" target="_blank">📅 19:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14647">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No99aF5cELc-JGZdmZNBmM-LJDfxMRACbHhXaqQdlaZqhWfjsSExPOup3PeFBOZS0d5foc0fB5RMwLrmOpds_udsmn75GSY2xes-3niNx0TnIN9jwFwuDMmI1xD_JVkYJ1Pvl2yEEidj--egSoWQYRCvGwKdd6TkfUhIS1EbD58JgD0boR3O4_ZzyWs9dGE2OrCYsyB7P6gT7i6JWVPzvFOaneMoMfVmiZujFyv9LB0PUCiCptKlBjamUGbf5rRA-sELK8Kb8PFN49QFcNHXO6g_kZIIJeNx3m9QtLGLqY1ggb91_18xaxwTUreldQqIDWEbGGwR02-ZZj_V6b2-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چپقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.  در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14647" target="_blank">📅 19:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اوهو‌ووووو‌‌
🤣</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14646" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14645">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جی‌ دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود
این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد. این توافق پتانسیل بازسازی منطقه و منجر شدن به صلح پایدار را دارد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14645" target="_blank">📅 19:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14644">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سناتور لیندزی گراهام: ایدهٔ یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی در ایران مسئول است، به نظر بی‌توجه می‌آید.
این مانند طرح مارشال برای آلمان است در حالی که نازی‌ها هنوز در قدرت هستند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14644" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بعدن میگم
🥶</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14643" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه چیز بگم مغزتون سوت بکشه
🤯</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14642" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14641">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جی دی ونس، معاون ترامپ:
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14641" target="_blank">📅 18:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14640">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چپقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.
در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک گذاشته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14640" target="_blank">📅 18:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14639">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14639" target="_blank">📅 18:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14638">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnHzQLsFgfA-zeEnNHrv7Ne12APJI6O0EBYxyizHKyQ04h4r87qV8p2vU2oFP2uCLTskne9hU-FEjnMdZYjF5y4iiCsNjFh9aK69b3MK5utBK-0CSUupXP3r-DNxid-QsDhM-hHBbyZ9fAWHdfCiu3FIFW0RWBApdq0xp0Ml_8GApDJhnkNW-sKFZnP3dXP8SpdxEiNWP7r7W43V-qEvh328OCYZ0GKaYFF42jw1Xyj-_ETdYT8G-wQUTeMdoc4p3DjggigJiPI_GuU4pd0fY6QdJoueoFyxINCHZeBCaCsiUbj3J9tZKK-ZyCGCi4tm7QafzPGgL3cz5sTnSSapSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : مفادی که ایران به رسانه‌های جعلی (Fake News) درز داده است، هیچ ارتباطی با مفادی که به‌صورت مکتوب بر سر آن‌ها توافق شده بود، ندارد.
آنچه آن‌ها گفته‌اند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود یک توافق، هیچ نسبتی با حقیقت ندارد.
آن‌ها افرادی بسیار بی‌شرافت برای مذاکره و معامله هستند. در مورد آن‌ها، چیزی به نام مذاکره و رفتار با حسن نیت وجود ندارد. شگفت‌انگیز است!
همچنین، حمله پهپادی کاملاً ناکام‌مانده آن‌ها دیشب علیه کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، کاملاً غیرقابل قبول است.
بهتر است هرچه سریع‌تر اوضاع خود را سر و سامان دهند؛ وگرنه با عواقب آن روبه‌رو خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14638" target="_blank">📅 17:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار وال‌استریت ژورنال: برای اینکه توافقی شکل بگیره، مهمتر از تایید مجتبی خامنه‌ای، تایید فرمانده‌های ارشد سپاهه.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14637" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منبع ارشد در تیم مذاکره کننده ایران:
یادداشت تفاهم نامه برای ورود به مذاکرات میان ایران و آمریکا نهایی نشده است و در حال بررسی است و
هرگونه امضای یادداشت تفاهم در روز های آینده کذب است
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14636" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏شاهزاده رضا پهلوی: در ایران نوین با مافیایی شدن ورزش مقابله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14635" target="_blank">📅 16:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14634">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رویترز: توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14634" target="_blank">📅 16:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14633">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نبویان: ما آمریکا رو زدیم زمین، رو سینه‌اش نشستیم که کار رو تموم کنیم یهو رفتیم پای میز مذاکره، میخوایم توافقی بکنیم که اون بیاد بشینه رو سینه ما اخه.
@withyashar
😂
🍋
🍋</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14633" target="_blank">📅 15:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14632">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی:
اسرائیل به آمریکا فشار میاره تا دارایی‌های مسدود شده ایران رو به عنوان بخشی از یادداشت تفاهم آزاد نکنه.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14632" target="_blank">📅 15:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14631">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwKVSrcBOrVqGEy442UMVpMixzvJLQctir6Vi3WtjXB-SNbUCOBI0gLvQSm24HnYw57GuVjvVV094XmRbKfBSyu6pLWO8UT_9uUeUHM7PkiBl6aBATOVNKTRkWulO935WVDgnPPiiNyqMwz7hJGnbjITucSS5GEaIf7Pq4QaIDtEGj0ntkzCUwbm-a0ebW9uUzmxVxOCPxGQ2g2JYIUdyw4W_N6Oa4gRk27S82Tn_dDVXyo_jbp6hMuXLGw1LN-4X2YprVKc4gFO7iUIbh1EJM2Wc9BYrKCXTcpU3l3zSSCY6XKG2iX0s0hNjaXe6qQjOjPU1cGbm3dj-V0OhRq8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ناوهای جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان در آب‌های منطقه‌ای به گشت‌زنی ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.
تا امروز، نیروهای آمریکا ۱۳۶ شناور را تغییر مسیر داده‌اند و ۹ شناور را از کار انداخته‌اند تا از رعایت این محاصره اطمینان حاصل شود.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14631" target="_blank">📅 15:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14630">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرگزاری ایرنا درباره جزئیات توافق احتمالی میان جمهوری اسلامی و آمریکا:
متن یک توافق برای پایان جنگ با دقت بسیار بالا و وسواس زیاد تدوین شده و هیچ مجالی برای تفسیر خودسرانه یا فرار از تعهدات از سمت هیچ‌یک از طرفین در این توافق وجود نداره.
در این یادداشت تفاهم هیچ توافقی درباره پرونده هسته‌ای حاصل نخواهد شد و جمهوری اسلامی هیچ تعهد جدیدی ارائه نخواهد کرد!
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14630" target="_blank">📅 15:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14629">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتانیاهو:
تا وقتی من نخست‌وزیر اسرائیل باشم، ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
من و ترامپ در این موضوع کاملاً هم‌نظر هستیم.
بیش از ۳۰ ساله که در خط مقدم مقابله با برنامه هسته‌ای ایران حضور دارم.
اگر این تلاش‌ها نبود، ایران سال‌ها پیش به بمب اتمی دست پیدا کرده بود؛ بمب‌هایی که به گفته او برای نابودی اسرائیل استفاده می‌شدند.
ایران به‌دنبال نابودی اسرائیله و من زندگی‌ام رو وقف جلوگیری از این موضوع کردم. تا وقتی نخست‌وزیر اسرائیل باشم، اجازه نمی‌دم چنین اتفاقی بیفته
.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14629" target="_blank">📅 15:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14628">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فارس: هر گمانه‌زنی دربارۀ امضا در سوئیس یا دیدار حضوری، چیزی جز فهم اشتباه از پیشنهادها و آرزوهای آمریکایی نیست!
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14628" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14627">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ایرنا؛ تفاهم‌نامه پایان جنگ چه مسائل و موضوعاتی را در بر می‌گیرد؟
۱.
موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲.
تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳.
پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴.
آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵.
غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛ موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14627" target="_blank">📅 14:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14626">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سخنگوی وزارت خارجه : متن نهایی تفاهم‌نامه تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14626" target="_blank">📅 14:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14625">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مهر : توی توافق با آمریکا، واشنگتن متعهد شده بخشی از تحریم‌ها رو برداره و نیروهاش رو هم از اطراف ایران عقب بکشه
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14625" target="_blank">📅 14:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14624">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری فارس : آمریکا ترسیده و عقب نشینی کرده ولی ما هنوز داریم پیشنهادات رو بررسی میکنیم و جواب خاصی هنوز بهشون ندادیم !
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14624" target="_blank">📅 14:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14623">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری دولت: هدف اصلی امضای تفاهم‌نامه، پایان جنگ در تمامی جبهه‌ها در منطقه است. در این تفاهم‌نامه پایان جنگ علیه ایران به اضافه تمامی جبهه‌های دیگر منطقه به در برگرفتن لبنان هم مورد اشاره قرار گرفته‌است.
عبارت تمدید آتش‌بس در متن فعلی ذکر نشده‌است و اشاره به چنین عبارتی در برخی گزارش‌های رسانه‌ای نادرست است؛ متن تفاهم‌نامه خواهان پایان قاطع جنگ در تمام جبهه‌ها می‌شود.
تهران تضمین‌های روشنی برای آزادی دارایی‌های مسدود شده بر اساس ساز و کارهای مشخص و مورد نظر تهران دریافت کرده‌ است و در صورت تصمیم تهران به امضای تفاهم‌نامه پایان جنگ، بخشی از دارایی‌های مسدود شده بلافاصله و بقیه به تدریج در طول مذاکرات، آزاد خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14623" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gztvzm8HDe5AU-euTz2Cj50SMlWOHlYWoyHP0f0-xcAaZyl2xOisylFLzOiGYengN0aN54Znzc6RYyFu-znvcJMaRgGOsNQP0cm3h5xs9PPc43ldPeKooB9x5ICho1zWzyYmOeGzJdPa_VxsQdaIaaXy_wY7v2ESJSQL-0yqDWPcwo-ADdhx02HczPORZx0OIKwJEi5ncjFPd_8lrPcnILbb9RUiDH5d72cjzS9g3lHHxBcYktDQ1A-a-NBW1KU_bMh_e73I2ORdwr3HjPrNWGTc-2L4TepRLLbK-fzjKpHLAYpBdEs26UfVMe8-Mhh6KMIMhIm0BEO_kuN9ktlGYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام دونالد ترامپ مبنی بر  احتمال امضای قریب‌الوقوع توافق با ایران، قیمت جهانی نفت 5 درصد کاهش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14622" target="_blank">📅 14:00 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
