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
<img src="https://cdn4.telesco.pe/file/lcuoRpvJo5mKTRofjHpg0O1ANyO9x1jwjt2QNNd7ZYAZgWnzcB9ESsMVcmBDp3djykeeNqW-aC4jV-8HSgya8lSGbEtSUa07PExQL1kRyNXKOVkHRyQvb7kWVEXeCT1sajFxAjC-mMkaN8sthlVypjI72GDvCBHwB-UpKRf6bP_eYOYBwk0grFpP1tOywwnTz3M16JU0bo5_y50hL7FKrxToU7e4PGw2HJrkdMOl-IUSj5nR74P2kQtSnl-TYGI2BBRiJ1xOZCgN1K5CMLAyWnRALmoZKDiXMIviYoC0eNMLKVqLnjHqXhW7en6qZzQBdNxL60dCAcgj0TOymAdceQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 417K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 11:14:42</div>
<hr>

<div class="tg-post" id="msg-19173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه وابسته به سپاه اعلام کرد:
زیرساخت مرکزی داده شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز هدف قرار گرفته است. طبق این گزارش، حمله متوجه بخشی از زیرساخت ابری و دیتاسنترهای منطقه‌ای آمازون (AWS) بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/19173" target="_blank">📅 11:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">BTC : 66,000$
TETHER : 189,500 T
@WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/19172" target="_blank">📅 11:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه‌های آمریکایی به گزارش‌های اطلاعاتی آمریکا اشاره کردند: تنش بین تهران و واشنگتن یک درگیری طولانی‌مدت است و بعید است که ایران به دلیل اقدامات نظامی آمریکا، مواضع خود را در مذاکرات تعدیل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/19171" target="_blank">📅 11:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک حادثه دریایی در کریدور عبور جنوبی تنگه هرمز  تحت کنترل امریکا رخ داد.
@WarRoom</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/19170" target="_blank">📅 10:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارتش جمهوری اسلامی: ما عملیات‌های خود را ادامه خواهیم داد تا آمریکا را از ادامه حملات خود به کشور منصرف کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/19169" target="_blank">📅 10:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رحیم زاهدی، مشاور وزیر علوم : يكي ان روياهاي كودكيم رقم خورد!
مادر تماس گرفت كه در فروشكاه اتكاي ازگل هست وبه دليل عدم استفاده روسري بهش تذكر دادن وگفتن از ارائه خدمات معذوريم بلا فاصله تماس گرفتم معاون وزير دفاع و رئيس سازمان اتكا، جوري شستمش كه كفت اين هفته با مادر برم پيشش و عذرخواهي بکنن
كلا ما چنين ابلاغ يا دستوري در دولت نداريم وجز سياست هاي أقاي پرشكيان علي الخصوص در زمان فعلي نيست هر نهادي به دليل بي حجابي بهتون خدمات ارائه نميده بيخود ميكنه وبايد باهاش برخورد شه
@WarRoom</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/withyashar/19168" target="_blank">📅 10:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هم اکنون
نیروگاه برق الزور کویت هدف حمله پهپادی قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/19167" target="_blank">📅 10:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ادعای آکسیوس: قطر، مصر، پاکستان و سایر میانجی‌های منطقه‌ای، طرحی را برای
آتش‌بس ۱۰ روزه به آمریکا و ایران
ارائه کرده‌اند.
در طول آتش‌بس ۱۰ روزه، تهران و واشنگتن در مورد یک
ترتیب بلند مدت برای عبور و مرور از تنگه
، مذاکره خواهند کرد.
یکی از گزینه‌ها به ایران اجازه می‌دهد تا
«هزینه‌های خدمات معقول»
را برای امنیت دریایی، حفاظت از محیط زیست و سایر خدمات دریافت کند .
@WarRoom</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/19166" target="_blank">📅 10:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKv-eb3lYdNexl6vQpurZcPjR3_L8Jd_vxcOjxo-I4bTpsbT5QtBiaiEoAAwC4-0QMc0PoJXC2yP5hRBkARd7vsHeHp29jIY9PhG8vnBROCAeVQCtKFDzFzafEZob7JMmOABvmFcyFfOriKbLmsryCAFD527UlFJRzZ_zDRB39XV9BGnq-OrS8JZ5uc5eMNX5NddoyYc3mE1cnnDFDG0OD_ooPm1ph42vrzl5YINg7EAN4WH8KUKiv0lSaFOzxxv8lQAJofSSqqjySwwY2SWdyGPZSDMfsUVMLOkNhzjzf7d-SjsN4ELCB5PsWMiYFIhgIXazemlyOzSWxSI0uJhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دفاعی اسرائیل (ارتش) و شاباک، رئیس بخش عملیات تیپ "شهر غزه" را به هلاکت رساندند.
@WarRoom</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/19165" target="_blank">📅 09:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار در اصفهان مهمات عمل نکرده است و اعلام شده از قبل
⚠️
⚠️
⚠️
@WarRoom</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/19164" target="_blank">📅 09:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک مقام اسرائیلی:
لازم است عملیات نظامی در منطقه "کوه کلنگ" در ایران انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/19163" target="_blank">📅 09:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کامران غضنفری، نماینده سابق مجلس که حسن روحانی رو به جاسوسی برایMI۶، ارتباط با سرویس‌های خارجی، داشتن تابعیت انگلیسی و فساد فی‌الارض متهم کرده بود به ۱۳.۵ سال حبس محکوم شد
@WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/19162" target="_blank">📅 09:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آکسیوس: تلاش میانجی‌گران برای آتش‌بس ادامه دارد؛ اما ترامپ و اسرائیل به دنبال یک جنگ تمام عیار علیه ایران هستند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/19161" target="_blank">📅 09:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a46db237.mp4?token=NVm7A2P-0bJG_XUbitFSnk7iYVIMZvQSpxmAFWCzdXMAZaVQpZ4MDhZHprbznmLWsQLDQsjTIO5zcTcBIckUnSeqmffdm8NPg-_pAeMp5bQBWCbGtLzVcqDEmBTQ_G7mLCrAy6DQlL9Onr9yhwWu-bKwup-QPxvljMYWh55eMp-V5eGpo5VQyoj-0ilKgfworNg_UAoVP91prQWp70Nzym3QA11IfxTEym5bcfuveU6qWfuyArX-T9W2U6wysgoSaekgLluGupxeL4BOPDRSZLOobvTijRz4n62Rx0nYxHOpRDYqwA4rpCZsT5_R_4C-lQ4fuOlycnSyfJ1Y8C0DRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a46db237.mp4?token=NVm7A2P-0bJG_XUbitFSnk7iYVIMZvQSpxmAFWCzdXMAZaVQpZ4MDhZHprbznmLWsQLDQsjTIO5zcTcBIckUnSeqmffdm8NPg-_pAeMp5bQBWCbGtLzVcqDEmBTQ_G7mLCrAy6DQlL9Onr9yhwWu-bKwup-QPxvljMYWh55eMp-V5eGpo5VQyoj-0ilKgfworNg_UAoVP91prQWp70Nzym3QA11IfxTEym5bcfuveU6qWfuyArX-T9W2U6wysgoSaekgLluGupxeL4BOPDRSZLOobvTijRz4n62Rx0nYxHOpRDYqwA4rpCZsT5_R_4C-lQ4fuOlycnSyfJ1Y8C0DRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: با باقی ماندن کمی بیش از ۱۰۰ روز تا انتخابات میان‌دوره‌ای، زمان برای رئیس‌جمهور ترامپ رو به پایان است تا پیش از حضور رأی‌دهندگان در پای صندوق‌های رأی، از این جنگ خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/19160" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شاهزاده رضا پهلوی در گفتگو با «دات ریپابلیک مدیا نیوز»، گفت:
«می‌خواهم کاملا صادقانه بگویم، سه گروه متمایز وجود دارند که ما نمی‌توانیم با آن‌ها کار کنیم: عناصر طرفدار رژیم، مجاهدین خلق و تجزیه‌طلبان».
وی خاطرنشان کرد:‌
بگذارید در این مورد خیلی واضح بگویم. در مورد هر یک از اظهارات تیم من، ما اکنون قطعا سازوکارهای بسیار سخت‌گیرانه‌تری وضع خواهیم کرد. به این معنا که افرادی که ارتباط نزدیکی با من دارند، باید بیش از گذشته مراقب آنچه می‌گویند باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/19159" target="_blank">📅 08:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پرتاب موشک از شیراز
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19158" target="_blank">📅 08:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وال‌‌استریت ژورنال: اسرائیل مدعی انتقال هزاران سانتریفیوژ ایران به «کوه کلنگ» شد
. این سایت در عمق حدود ۱۰۰ تا ۱۴۰ متری کوه ساخته شده و به گفته کارشناسان، هدف قرار دادن آن بسیار دشوار است. اسرائیل معتقد است این انتقال می‌تواند تلاشی برای بازسازی ظرفیت غنی‌سازی ایران و محافظت از تجهیزات هسته‌ای در برابر حملات آینده باشد. آژانس بین‌المللی انرژی اتمی تاکنون اجازه بازرسی از این محل را نداشته است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19157" target="_blank">📅 07:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19156" target="_blank">📅 07:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اکسیوس:به گفته منابع آمریکایی و اسرائیلی، رئیس جمهور ترامپ به یک نقطه سرنوشت‌ساز در جنگ با ایران نزدیک شده است و دو گزینه اصلی پیش رو قرار دارد:
1.  آتش‌بس 10 روزه برای بازگشایی تنگه هرمز.
2.  یک عملیات نظامی گسترده با اسرائیل برای وادار کردن ایران به تسلیم.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19155" target="_blank">📅 07:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c0991007.mp4?token=MWr3mSEYycrFgn8-qNjYZxszrXtMxNlqhbf-JzUqNPNt-FoTVhMRpla3OW0xSHB0UK8OeEYN3sfs3hoeeLNfF5T_R3Kb_NKtj0fI9-cT-VFmX8mQ_F-KtsxoMRGIRUmPIjhlxNEKh0ei5KM8ZFKw2xDBu_U1xa47UEsXV7MG8TMfYqC3uGZTJ76e96JArJEa7WlO_H5EdMUOT61e4AfPLXAaukI35y4PE3Wgt-v6Tj8aabp0ojW313EM0b90AlivZPd_mh2jhcGo1AYahU7aRyuj7x668a35kvQb0GuMoBOcY8gVQ-fFyTgif2SUki6uJ7g4ezkrZcxOXS3iUQreLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c0991007.mp4?token=MWr3mSEYycrFgn8-qNjYZxszrXtMxNlqhbf-JzUqNPNt-FoTVhMRpla3OW0xSHB0UK8OeEYN3sfs3hoeeLNfF5T_R3Kb_NKtj0fI9-cT-VFmX8mQ_F-KtsxoMRGIRUmPIjhlxNEKh0ei5KM8ZFKw2xDBu_U1xa47UEsXV7MG8TMfYqC3uGZTJ76e96JArJEa7WlO_H5EdMUOT61e4AfPLXAaukI35y4PE3Wgt-v6Tj8aabp0ojW313EM0b90AlivZPd_mh2jhcGo1AYahU7aRyuj7x668a35kvQb0GuMoBOcY8gVQ-fFyTgif2SUki6uJ7g4ezkrZcxOXS3iUQreLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : گوشه ای از تصاویر شب دهم حمله به ایران
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19154" target="_blank">📅 07:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سنتکام : پایان شب دهم
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد
دور دیگری از حملات علیه ایران
در
۲۰ ژوئیه، ساعت ۹:۰۰ شب به وقت شرق آمریکا (ET) (۰۴:۳۰ بامداد ۳۰ تیر به وقت تهران)
به پایان رسید.
نیروهای آمریکایی
مراکز فرماندهی نظامی، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد، و سامانه‌های پدافند هوایی ایران
را هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های تجاری که از
تنگه هرمز
عبور می‌کنند، کاهش یابد.
عبور کشتی‌های تجاری از این
گذرگاه حیاتی بین‌المللی دریایی
همچنان ادامه دارد. از
اوایل ماه مه
تاکنون، نیروهای سنتکام به تسهیل عبور
حدود ۹۰۰ کشتی تجاری
و
۴۵۰ میلیون بشکه نفت خام
کمک کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19153" target="_blank">📅 06:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نقاطی که در شب دهم مورد حمله ارتش آمریکا قرار گرفته‌اند:
💥
شیراز
💥
چابهار
💥
بندرعباس
💥
جزیره قشم
💥
سیریک
💥
بندر لنگه
💥
بوشهر
💥
کنارک
💥
کرمان
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19152" target="_blank">📅 06:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:مکالمه خیلی خوبی با نخست‌وزیر جدید بریتانیا، اندی برنهام داشتم. موضوعات زیادی را بررسی کردیم، از جمله رابطه ویژه‌ای که با بریتانیا داشتیم. به زودی برای موضوعات مورد علاقه مشترک ملاقات خواهیم کرد.
نخست‌وزیر وظیفه بزرگی پیش رو دارد، اما قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا. من آنجا خواهم بود تا کمک کنم! درباره نفت دریای شمال، تجارت، اتحاد نظامی و پاکسازی مین‌ها از تنگه هرمز و موضوعات دیگر صحبت کردیم. مکالمه جالب بود و خوب پیش رفت. برای نخست‌وزیر برنهام آرزوی موفقیت و انتظار خوب کردم!
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19151" target="_blank">📅 01:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همین الان پایگاه هوایی بندر عباس رو سنگین زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19150" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">داداش الان سیریک طی ۱۰دقیقه ۵ انفجار قشنگ و محکم زد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19149" target="_blank">📅 01:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8dHHuY83OcHh0i1L1slSkltGqwoPsaNcxxqbnjTjO2V4ALNVHzzOrnVvbvjYpjJaARtrHTVKJIXl8T42FfoiGrazkWcNZoc-jby9F6_Mp6YSAmPzmnUOYTVQ9Ib6pLm3V8FnojIo_f03o285s49nX7Picy8DKbU_eokrRDmARjPKKkLzG_hQDpWwrPzJl6OV2MREqMw-yruMJdYBIEolR6Bagis-j0-v97mi8VSZOBh3QuLmMJ0SbbgEFXiZ7mrrjJJCRjaUM0ecXx8aIHO7UGiKgoYlJtrHxq_v5z-EDLSBS05l8SS_Na7mxkoMkbIba58ASVDWTOxvqbh82RwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان UKMTO گزارشی از حادثه‌ای در ۸ مایلی شمال شرقی لیما، عمان دریافت کرده است. مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ VHF گزارش می‌دهد که توسط یک پرتابه ناشناخته در تنگه هرمز مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19148" target="_blank">📅 01:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19147" target="_blank">📅 01:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش تایید نشده از حمله به نیروگاه بوشهر ، ممکنه مثل قبل‌ پدافندش رو زده باشن
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19146" target="_blank">📅 01:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19145">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش صداری ‌انفجار‌ جدید شیراز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19145" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19144">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan</strong></div>
<div class="tg-text">درود رئیس اتاق جنگ
خوشحال شدم رسیدن به جیرفت (کرمان)
بزنن هرچی مقر سپاه توی این استان هست با خاک یکی کنن. هرچی میکشیم زیر سر قاسم و لشکر ۴۱ ثارالله و این سپاهه. جیرفت و بافت معدن سپاهیاست. البته توی این استان کم نیستن. به امید اینکه اعلام کنی تک تکشون پودر شدن.</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19144" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19143">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسرائیل اینش خوبه که قبلش میگه ! پل ها رو هم باید اعلام میکردن ! پل‌که در نمیرفت ! فرمون باید دست بی بی باشه  تا این راه بیفته پیر میشیم</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19143" target="_blank">📅 01:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19142">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خداروشکر حمله ها کاملا فقط پایگاه های نظامی هست و امروز تا الان مردم عادی آسیبی ندیدند
😍</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19142" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19141">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چابهار همینجور میزنند
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19141" target="_blank">📅 01:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19140">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a96706789.mp4?token=N2xZZwf2MDJHJun5amOfb5_LntszPAca9yX8DCkpc2LGcb2H7cUy9TXmmlgLOhCFjzdWP-8u7BJ7tvhgWtqagOovkaQhZKRNNPlZ1Xp7WAXNvqkwF9p7wEhqrdPdEJ-84UGKyQ-XoV3j3KNkFmX2huwsCim_SLIcFkmswhC2E6gu_jlCuBawrxO-O61zoPXNr85GYLde84tvwcIlzS5YZfy2yWLKDnS3lmh1rugAcO_zBhZJYi3OndRKuusUd6lnxhkeDcIHfK-3UJ_pnWqBGQJ1NzOTdSQCQAaYVAAdigokLt1P-BpNFwSfpkS62_ZY0r3h8Mkf_aUcUaEbFhQOLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a96706789.mp4?token=N2xZZwf2MDJHJun5amOfb5_LntszPAca9yX8DCkpc2LGcb2H7cUy9TXmmlgLOhCFjzdWP-8u7BJ7tvhgWtqagOovkaQhZKRNNPlZ1Xp7WAXNvqkwF9p7wEhqrdPdEJ-84UGKyQ-XoV3j3KNkFmX2huwsCim_SLIcFkmswhC2E6gu_jlCuBawrxO-O61zoPXNr85GYLde84tvwcIlzS5YZfy2yWLKDnS3lmh1rugAcO_zBhZJYi3OndRKuusUd6lnxhkeDcIHfK-3UJ_pnWqBGQJ1NzOTdSQCQAaYVAAdigokLt1P-BpNFwSfpkS62_ZY0r3h8Mkf_aUcUaEbFhQOLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوش این نیز بگذرد…
❤️‍🩹
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19140" target="_blank">📅 01:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19139">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">استاندار اصفهان: صدای انفجار در اصفهان تایید میشه ولی بخاطر حملات نبوده و دلیلش درحال بررسیه @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19139" target="_blank">📅 01:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19138">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ffff35e3.mp4?token=Mlk-olYsf6FtXdjNliYpy6hJIVXKb2z-fEj3yIlkbhimmeBEp0ivxu60in1OYLkPT2dxwF7ZZzbKDPsV-eTBcAy5tEIQe2Eualseub4FP-xRtYcCGV3VsPNM4m2rWdoYZYOE5IbYEyEBFtTSLHYXaRT35LcTWSNCVNUo4DY9GHuNLB8IKaQpknS8fsNxENvFuFHq2K91j4bWmDyKj9VdMRhbLOoqZghWbNHbAOxrjfBGkgaKRWpLt4tUiLMiE5BBHuF-o5RwXlVMP7M3jfUd9KHacenRh0xPru3zy2huvS43NOOBg-bl3AY2xvYmPpEO_n6vMshVeFrQSW-vFzG0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ffff35e3.mp4?token=Mlk-olYsf6FtXdjNliYpy6hJIVXKb2z-fEj3yIlkbhimmeBEp0ivxu60in1OYLkPT2dxwF7ZZzbKDPsV-eTBcAy5tEIQe2Eualseub4FP-xRtYcCGV3VsPNM4m2rWdoYZYOE5IbYEyEBFtTSLHYXaRT35LcTWSNCVNUo4DY9GHuNLB8IKaQpknS8fsNxENvFuFHq2K91j4bWmDyKj9VdMRhbLOoqZghWbNHbAOxrjfBGkgaKRWpLt4tUiLMiE5BBHuF-o5RwXlVMP7M3jfUd9KHacenRh0xPru3zy2huvS43NOOBg-bl3AY2xvYmPpEO_n6vMshVeFrQSW-vFzG0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار پادگان امام علی
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19138" target="_blank">📅 01:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استاندار اصفهان: صدای انفجار در اصفهان تایید میشه ولی بخاطر حملات نبوده و دلیلش درحال بررسیه
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19136" target="_blank">📅 01:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش انفجار شیراز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19135" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">تحلیلگر ارشد</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19134" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کره جنوبی:
از شهروندانمون میخوایم فورا از کل خاورمیانه خارج بشن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19131" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_IifnEAeXw-smT4GIFfFHTro2JDvs2znTIoKUGKTzPAZ5sfJYr2CXKui4m4sHFu30ilefbb-y-PfYTDNR_NnNvoiEcT-htMB9GdfGGo06H5tC9X33wltAyXdpZlZ8SZwjzs3fXcrS7AEe0O0u-AaHg7WycepasAa61nkSfjoHOArXjDqW-0Zb-yxDIYiNRu7MYaOzouh0UOak-rJnsBnu4U4RDRhfxdDSDtvNAGHSqu_9ZTKVMajbDbiKva6uGNdZihf5XSmijBTg1Goy9FFrvb9Vm1gt7sJ8riVVxPh2PWpY31i28OnDBqNBIVP29Obkq8aJRW9ATIAY7ySwoBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیراز کوه دراک‌ رو قفلی زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19130" target="_blank">📅 00:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش‌۲ انفجار بندر کنگ
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19129" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شیراز صنایع رو بدددد زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19128" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش انفجار شیراز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19127" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش انفجار اصفهان
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19126" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه حالی بدین اینستاگرام رو هم بابااااا اگه ندارین فالو کنین دیگه instagram.com/Yashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19125" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز
: حملات به جمهوری اسلامی ایران در مقیاس بزرگ نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19124" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">استاندار بوشهر: تاکنون هیچ گزارشی مبنی بر وقوع جراحت گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19123" target="_blank">📅 00:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❤🦁💚</strong></div>
<div class="tg-text">اصفهان یچی زدن یاشار شاید باور نکنی شبیح ویبره</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19122" target="_blank">📅 00:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سلام من اصفهانم
ی چیزی زدن صدا نداشت اما شیشه ها لرزیدن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19121" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19120" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7Xr_FAnNfYfC301IVE6CUpr439SxdvCieqpC5Sc3nJR3AL3rpjWg2tESdDo1KpKpmgcpWONBH7pgWi8_ZQM2RdNUHTne3a5jH3_0J8Xho5f8rpT6jB8UcxixwidayPcV7l5zAUXa7q7OBv1GjxlZrNRWLIUSBt88M87Gfub85iMAs2ZwGlMObeBjzdwO8REnmc9xnVdiZIu34tZ_gV7rIhcgcGJKMIapQQXhWXzN8p0Lz-trMu-POKWzTpoLZGiaRv_rwlCp0wKjFvaTND9eMrxPg4wgFxyEuvWF3lEc9FdUgE-fTyWDgzhq8PoW1RNgfwQN7De02TtL77wsq9mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی از پادگان امام علی چابهار که نورانی شده
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19119" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19118" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پایگاه امام علی چابهار رو داره میکوبه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19117" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدای انفجار در بوشهر
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19116" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چابهار رگباری‌ داره میزنه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19115" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فاکس نیوز: دور جدیدی از تنش با ایران در راه است
به گفته فاکس نیوز احتمال بازگشت آمریکا به جنگ تمام‌عیار در خاورمیانه بسیار بالاست.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19114" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کنارک رگباری میزنند
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19113" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چابهار ۲ تا دیگه
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19112" target="_blank">📅 00:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوباره کنارک رو زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19111" target="_blank">📅 00:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه حالی بدین اینستاگرام رو هم بابااااا اگه ندارین فالو کنین دیگه
instagram.com/Yashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19110" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستانی که نمیتون عضو بشن فیلترشکن دیگری امتحان کنند ، اونی که دارن لیمیت خورده
❤️</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19109" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش صدای انفجار کنارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19108" target="_blank">📅 00:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صداوسیما: صدای انفجار در بخش بمانی شهرستان سیریک شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19107" target="_blank">📅 00:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش انفجار چابهار
🚨
🚨
🚨
@WarRo</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19106" target="_blank">📅 23:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش انفجار دزفول
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19105" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19104" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبر گزاری داخلی : دقایقی پیش، صدای فعالیت سامانه‌های پدافندی در اطراف نیروگاه اتمی بوشهر به گوش رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19103" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بوشهرررررر
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19102" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19101">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شب دهم شروع شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19101" target="_blank">📅 23:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19100">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش صدای انفجار جیرفت
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19100" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19099">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">موج سنگینی انفجار بندر از شهر های اطراف احساس شده
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19099" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19098">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بندر عباس بیش از ۸ انفجار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19098" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19097">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۵ انفجار سنگین بندر عباس
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19097" target="_blank">📅 23:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19096">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شب دهم شروع شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19096" target="_blank">📅 23:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19095">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوباره بندر رو زدن
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19095" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19094">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدای انفجار بندر قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19094" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19093">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدای انفجار بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19093" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19092">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاهزاده رضا پهلوی در گفت‌وگو با رویترز:
داوری بی‌طرف, و پلی برای رسیدن به مقصد هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19092" target="_blank">📅 23:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19091">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
ترامپ دستوری به ارتش آمریکا صادر کرده است که به دلیل کشته شدن سربازان آمریکایی در اردن به زودی از ایران انتقام خواهد گرفت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19091" target="_blank">📅 23:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19090">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19090" target="_blank">📅 23:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19088">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19088" target="_blank">📅 23:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19087">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شد ۲ انفجار سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19087" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19086">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش صدای انفجار سیریک
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19086" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19085">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری سی بی اس :
یک توافق موقت درحال شکل گیری است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19085" target="_blank">📅 23:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19084">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وال استریت ژورنال:مقامات آمریکایی جزئیات سه حمله موشکی جداگانه به پایگاه هوایی موفق السلطی را شرح دادند:
حمله اول به باشگاه ورزشی پایگاه که منجر به زخمی شدن تعدادی از سربازان در مسیر رفتن به پناهگاه‌ها شد
حمله دوم به یک آشیانه خالی هواپیما
حمله سوم به یک خانه کانتینری که سربازان در آن خوابیده بودند
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19084" target="_blank">📅 22:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19083">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">@WarRoom
وسط راه</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19083" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19082">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5XAtERDoJdDl3u5kZ-v558UHY2wmcE2K2Cw2RqoxqA2z2p6qZ-lMXaGJMAnTSlKRzhJVjvURWsntGObkxIX3Yokrr9AERUILC2--o8l1TIThZyTMhHPNmACHyjDboi3LNHeVOGnWqC3kbg9_i5x06vmREkhylSAA1sq_uwbTt3l9wFhZc3gEnpMsI3KBI7sInO7MiCZON0buyq90_B8X6SAkicwYr_A-mqijDGXkhXFIJApXz96kQvogD9Blj0pl1fOPJ5324s7V8f31CjlJlTA32wsGyxVOQW5NfIJpoSVWuFXQVFDNAEj_n6lT7Zf4aQ7qP4f7ndDDNp7NgqtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه کرمان: یک موشک کروز آمریکایی در آسمان رودبار جنوب رهگیری و منهدم شد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19082" target="_blank">📅 22:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19081">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فایننشنال تایمز: بدلیل فشار های داخلی ایالات متحده آمریکا کاخ سفید در حال بررسی گزینه الیت (تغییر رژیم کامل) در ایران است کاخ سفید قصد دارد سریعتر پرونده ایران را تعیین تکلیف کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19081" target="_blank">📅 22:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19080">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شرکت هواپیمایی ایرفرانس، تمامی پروازها به کشور های خلیج فارس را به مدت هفت روز متوقف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19080" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۲ اسرائیل: شنیده شدن صدای انفجار در بندر ایلات
احتمالاً این صداها به دلیل شلیک موشک به سمت اردن بود.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19079" target="_blank">📅 21:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyGJnMmkbM6Eopfz98Dtoj59_5W8kTIqeL0WOplmNcH-CaSTy-_KxaOY96VCDLTLomGIfMYSbHpyYMbUOIVs5mxGaZugZEwjI9ZV0MTCMahdSg0FHVxcG0ETNvxYQa_cN2hCXy1YHLZsRB_Dn5p-lueMF0ZPyOhKe_bb1rUsv7lUhf2cMjyiRIRHN6uzrdR1DtZGg0auBRlFzQCn_5fI1Qqk9qhMnQ_YXRIpX_8bKb9Q4ha-hiigiw18kWh6Yp3EcrGFfLZjVxIfda2r3bAuOsTq-cZQVlb-IsTb2RPCs9NU1AbwkQKUC2QMHZ8GMQxifqRRg8p1ZbnC8f87tiVVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار همین الان سه تا موشک از غرب تبریز فرستادن خیلی صدای بدی داد
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19078" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شلیک موشک از تبریزززز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19077" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به شبکه i24NEWS: ایالات متحده در روزهای آینده، مرحله بعدی عملیات نظامی خود علیه ایران را آغاز خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19076" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کاخ سفید:رئیس جمهور دونالد ترامپ، فردا شب در مراسم استقبال از تابوت‌های سربازانی که در حمله جان باختند، شرکت خواهد کرد. این مراسم در پایگاه هوایی دوور (Dover Air Force Base) برگزار می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19075" target="_blank">📅 21:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19074">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPSYNB0p-X2QayUiWWehV44ImM3WVlzLVXUUClUu8ktFytOfizM_fhdO067tXnrLDhQ7xbKpV3aunCplvFBvIAQPhMXXXRMgS8gLNLHsiUqcCkwt_mEnK0w6D9FC0bQFwuP-PJNehjzA-w4CyZHImW851X5BgvDIfuogngV8m-CJGm_pIldUkyfVlb5Nn4wCuJEi2688RI4hgwtSDV5qYELDQoBeuYneUlyXtPbz8sxi8ffE7BbI7ilzYXpb8asKwsbeFPirLnv8IO7bMmehA8MMP9_mlcSMMc_Imu74SUAmx2AL2CJ1C0nlDxJ72ZsoaXdyTbPk5CgOYPw0RPgQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از وقوع یک حادثه در فاصله
۸ مایل دریایی شمال‌غربی کومزار، عمان
دریافت کرده است.
افسر امنیتی شرکت کشتیرانی (CSO) تأیید کرده است که کشتی توسط
یک پرتابه ناشناس
مورد اصابت قرار گرفته است. خدمه کشتی با ایمنی کامل آن را ترک کرده و توسط یک
یدک‌کش
نجات داده شده‌اند.
آتش‌سوزی همچنان مهار نشده و کشتی در حال حاضر
بدون کنترل و در حال حرکت سرگردان
است. همچنین تاکنون هیچ گزارشی از
آسیب زیست‌محیطی
منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19074" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19073">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منبعی در سپاه پاسداران به نایا که از افشای نام خودداری کرد: تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده و نیروهای ویژه هم در آنجا حضور دارند. این عملیات احتمالاً در جزیره بوبيان انجام می‌شود که محل پرتاب موشک‌های آتش غیرمستقیم آمریکایی ATCAM به سمت جمهوری اسلامی ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19073" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H29omMgabSuz4vNvphdZ5xDreDNPbsaPD-goTtgNg085E9Z6KMAslJjaxXpJ45a816iCi2FKCfOxa8y9StLsJgijTEvgTKcuwOR9iI2h649ly1eVAk95eXYzVgD6Ff9Dz1ZtAfbrNiaS0gT9e_oY4IGfJBf3FqMw3eLgsf7Yui3XSKjffhU4WIhtwEzD0OZyqZSqC--RdZN43SnnLCF87y0bnK3DqlRo1IxM0o1ymXcreZCxNl3d7GOYY9IZyXAsTatKJ5LdPgydS5p3O4nw90ftAlbaNfDB15CIOtCiZJVCCrNREbp7U15QKobnOC9wFHWnqzzWJ_XFVQr3G5l-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز تجارت دریایی بریتانیاUKMTO: یک کشتی در 17 مایل دریایی شرق دیبا، مورد اصابت یک پرتابه قرار گرفت و باعث آسیب به چرخ دنده فرمان شد. تلفات جانی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19071" target="_blank">📅 20:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19070">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانال ۱۲ اسرائیل: جلسه کابینه امنیتی و سیاسی اسرائیل درباره ایران با حضور تمامی فرماندهان و رؤسای نهادهای امنیتی آغاز شد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19070" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19069">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReESBOCDqpsHY1YKuSWJPfZn-Zy8R5ST5ArWum7_v3abphytjSmEVSYJokLDgzYpyZ59e2slKlxh1QU0rgUX921x2CeMWIfgMXyoy0oe_fr7SvJ_KMEYH6WlqPUKunjD5uty9fwBu0wtwDL9158lm2yxss39ILUdJEWWCo0pm1BxUs-ozUAx5wWxkXeJ3yOeb5Fp8vcNyrlxsqbENJYtJndkr7z76Ef72ZD9wz2BlCDzqlsw1Q3bo-Uy0bIkjKrFpN2TY9q7CQEy5FU-b9w2WxUr9X1DU9UZarX8g_sAWwQiMIk-zctiPCUszEIn1psdqN4N1HEHjLGhA6GQlOQcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
بنیامین نتانیاهو در مدت حضورش در ایالات متحده آمریکا،
به هیچ شکل و تحت هیچ شرایطی بازداشت نخواهد شد.
او در حال مبارزه با
جمهوری اسلامی ایران
است؛ حکومتی که به گفته ترامپ،
به‌تازگی ۵۲ هزار معترض بی‌گناه را کشته
و طی
۴۷ سال گذشته
نیز مسئول کشته شدن سربازان آمریکایی و افراد دیگری بوده است.
تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این
چرخه بی‌سابقه مرگ و ویرانی
کشاندند؛ موضوعی که
باید سال‌ها پیش و در دوران رؤسای جمهور پیشین آمریکا با آن برخورد می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19069" target="_blank">📅 20:27 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
