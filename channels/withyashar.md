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
<img src="https://cdn4.telesco.pe/file/k6f-ERWH2kmJPX1BwWAfD9yYG7nbP_Wx2KhikuYyNLxTHbCic52kbnwWoPSECjl3WBMjJZCtb5jMzCsydQv0ERqcnIsKM6TkJGcQgO1x4CF2qLUDvPr8KAXhTFAVjqCSdmUHIaghuIzv2CO9WvryewyJBU9T6ZB-NuvezxwUwMIkoumweZFKeIRR2CnZ9Iai3LhY0HcZo7krFfX0bP3-sUejV4dlxmm4jEFSCIQ4NYsQfOASIk0VYtua5sB70d0l2PaG7-FAplUpeS2cpiMHE-WL_7zg5QSVmA_7oxNPjEthgUo5FszORijO8QSsFArmaykc8jCVzra0euV5yPUB8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش ۲ انفجار در جاسک و چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/withyashar/23113" target="_blank">📅 18:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6bvN4J4EJvDZS2AN-hQ_7xSs5_0KIU7kQs4KSBHyHuhKNDand6YNeYbhZCLSWvZJj9bBWAMLMAAFxx7wwSdEuAFj5WUyJvb1Dxas9zFCSbFeMK4H8JF8eaWnFwFq592emi6LoFtujvC6b1RRYqexNG7P_fbUFxh5pD94Yioin-g613OZiqyQXD4GBS2zqzLarIILHrFlms7chl2m1B-MW1tSenLF5CiCMr_4Dsytqu9qMfAVmli09YJI--PR2D5odGv-3O4y6talspoIM7SVyPS0LshDS9UOEeYFae1XrrwOIiGufpAFxgX-yvMBTwp-e8jaU8gEISBuYJa6xg8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: تنها چیزی که هوش مصنوعی به آن برای کنترل یا ایجاد «چارچوب‌های نظارتی» نیاز دارد، یک رئیس‌جمهور
قدرتمند و باهوش (با ضریب هوشی بالا!)
است، و ایالات متحده آمریکا چنین رئیس‌جمهوری را آن هم به وفور دارد! دولت ترامپ جلوی افراد فعال در حوزه هوش مصنوعی را که کارهای بد یا بالقوه بد انجام می‌دادند گرفته است؛ افرادی مانند داریو (آمودی، مدیرعامل آنتروپیک) که حالا وانمود می‌کند یک «فرشته کوچک و بی‌عیب‌ونقص» است؛ و ما به این کار ادامه خواهیم داد! ما همین حالا هم
قدرت‌های گسترده کیفری و نظارتی
بر این شرکت‌ها داریم! یک توطئه
بیمارگونه
علیه هوش مصنوعی و مراکز داده در جریان است و تنها کسی که از آن خوشحال است، چین است.
هرکس هوش مصنوعی را ببرد، برنده خواهد شد!
ما از چین و همه دیگران جلوتر هستیم و به این روند ادامه خواهیم داد. نظریه‌پردازان توطئه، خیانت‌پیشگان، خائنان و افشاگران،
مراقب باشید!
از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/23112" target="_blank">📅 18:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPdfvuFa6YpQIg8QBAK71fEEsyxPJOW1HdLm-3L8OGwj_yu3FPQd_ZZ3WbcN5nW4HnNkS9-DO_1np8C2JRRYoq8LijJ1K8O9ms65qnM0Ktrs_uDOIXpwcd_fnSV8p57nc0ke2MevGwrTc-mXprNSEVvPIb3KwG91hAw6rfVgfySzPH-5S0cUZqsv3XueroJkmiXkNDkmVEwNl9L-iERrPgQ7pB5IF5WcMFWcJyqcxJXElO034bZnJL9SUHRiGz6lUzdqobYb1q01zcVKbK8EaoniFikjTTTesK3N416JMotVK0Q_ISLHL_J9eyGARtpKVTsRP6QdZ5NpgJB8LbcbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت رسیده ۱۰۹.۲۰$ با نمودار هفته های اوج جنگ برابرشده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/23111" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تنگه دعوا شد ، ۵ صدای شلیک/انفجار
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/23110" target="_blank">📅 17:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت خارجه چین روز دوشنبه ۲۳ شهریور گزارش‌ها درباره ارائه تصاویر ماهواره‌ای به جمهوری اسلامی پیش از حمله موشکی ۱۷ شهریور به پایگاه موفق‌السلطی در اردن را «بی‌اساس» خواند و رد کرد. مقام‌های آمریکایی گزارش داده بودند که جمهوری اسلامی پیش از این حمله، تصاویر…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/23109" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">لحظاتی پیش دفتر نتانیاهو اعلام کرد: نتانیاهو هفته آینده به آمریکا سفر خواهد کرد @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/23108" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آبان ماه پادشاهان
۱ آبان — منسوب به زادروز نادرشاه افشار
۴ آبان — زادروز محمدرضا شاه پهلوی
۵ آبان — انتخابات سراسری اسرائیل
۷ آبان — روز بزرگداشت کوروش بزرگ
۹ آبان — زادروز شاهزاده رضا پهلوی
۱۲ آبان — انتخابات میان‌دوره‌ای کنگره آمریکا
۱۳ آبان — سالروز انتخاب نام «رضا» برای ولیعهد ایران
۱۴ آبان — سالروز فرمان شاهنشاه محمدرضا شاه و اعلام ولایتعهدی رضا پهلوی
@WarRoom
یاشار : ۲ آبان تولد پدرم هم هست
خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/23107" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زارتان زورتان</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/23106" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96df3d233.mp4?token=kK4yB3LfrCXdvkS6ZJNyp1Y_P6JKMfWxnfR3bPdguiCR9QHDGOfrcZ2Mo9uFNWiDg6ufUUsle7dpapx-mEQiuo4Ya2z6HvEAv2hqcP3PMbUfw_aVEbaB3vLcOxS7j6CNHRQmwmYYNXie9tFIlo2ig_ekdX1ZyQemJAOJ0OYa1yylEJzXO-bvPJEiSh0GLglCru8n3Rb-qUO7PgCrEdtrma0v5rk0YnmtDqiEwvm2Q7DiEaKRbleNAiD7PJpyq7GnCAaqWHZgGC7w6qPE67cM4UJEauw51oRlX_wpgqNg5H6sQD6Bmd4eCLDmPEuVDTjUfx94p_RwebOrpkLAYKW-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96df3d233.mp4?token=kK4yB3LfrCXdvkS6ZJNyp1Y_P6JKMfWxnfR3bPdguiCR9QHDGOfrcZ2Mo9uFNWiDg6ufUUsle7dpapx-mEQiuo4Ya2z6HvEAv2hqcP3PMbUfw_aVEbaB3vLcOxS7j6CNHRQmwmYYNXie9tFIlo2ig_ekdX1ZyQemJAOJ0OYa1yylEJzXO-bvPJEiSh0GLglCru8n3Rb-qUO7PgCrEdtrma0v5rk0YnmtDqiEwvm2Q7DiEaKRbleNAiD7PJpyq7GnCAaqWHZgGC7w6qPE67cM4UJEauw51oRlX_wpgqNg5H6sQD6Bmd4eCLDmPEuVDTjUfx94p_RwebOrpkLAYKW-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/23105" target="_blank">📅 16:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لحظاتی پیش دفتر نتانیاهو اعلام کرد:
نتانیاهو هفته آینده به آمریکا سفر خواهد کرد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/23104" target="_blank">📅 16:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">باراک راوید ، آکسیوس :
ساده‌لوحانه است اگر فکر کنیم ایران اجازه می‌دهد انتخابات میان‌دوره‌ای آمریکا بدون ایجاد آشوب برگزار شود. برنامه ایران این است که هر دو تنگه را مختل کند، به خطوط لوله حمله کند و [با این اقدامات فشار ایجاد کند]…
@WarRoom</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/23103" target="_blank">📅 15:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer"><a href="https://t.me/withyashar/23102" target="_blank">📅 15:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارشات مردمی از ورود جنگنده اف ۱۸ آمریکایی به جنوب کشور - دقایقی پیش
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/23101" target="_blank">📅 15:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر انرژی آمریکا در پاسخ به سوال الجزیره: عبور نفتکش‌ها از تنگه هرمز در شب و با اسکورت نیروی دریایی آمریکا انجام می‌شود.
ما کارت فشاری را از ایران گرفتیم، کشوری که تلاش می‌کرد تا کشتیرانی جهانی را به خطر بیندازد.
اطلاعات ما در مورد عبور کشتی‌ها از تنگه هرمز، تخمین نیست، بلکه حقایق دقیق هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/23100" target="_blank">📅 14:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5acf092a81.mp4?token=VatXy-dYB3U6F2ruEdyY6rCYEPJ0Qgi9dvxe-jm0easpnNkm7vYr9WBG8ffSuf10AX5jx9CArUEc52uQp32MYRb5W4xMF9O9wwnxNppQm5zvyRLzuGXjEzGbeeieMYKXpjH6Vw0jE2o-xCRj66j2AH-SQxLvYPEM453_vsQMAdP_USe2_QlzvaPq1ThI4tauGZZMi9oPfrjfZXYJ4vFdKNwN_57zhLeT3FbOtJx0c7N8PM9rx5YsCzChn9u-UxANV9Tm2uMg02kq9ATSv3fe-iXQaC65MFVb1IhRqhFTvGMAleQCIVn2bqggFIX0yWaw2QezSvj31Kn38XtfHO-IsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5acf092a81.mp4?token=VatXy-dYB3U6F2ruEdyY6rCYEPJ0Qgi9dvxe-jm0easpnNkm7vYr9WBG8ffSuf10AX5jx9CArUEc52uQp32MYRb5W4xMF9O9wwnxNppQm5zvyRLzuGXjEzGbeeieMYKXpjH6Vw0jE2o-xCRj66j2AH-SQxLvYPEM453_vsQMAdP_USe2_QlzvaPq1ThI4tauGZZMi9oPfrjfZXYJ4vFdKNwN_57zhLeT3FbOtJx0c7N8PM9rx5YsCzChn9u-UxANV9Tm2uMg02kq9ATSv3fe-iXQaC65MFVb1IhRqhFTvGMAleQCIVn2bqggFIX0yWaw2QezSvj31Kn38XtfHO-IsoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه هند در جریان سخنرانی بی محتوای پزشکیان در اجلاس بریکس در دهلی نو، به خاطر خوردن یک جعبه آجیل خبرساز شد؛ او مشغول خوردن و لیسیدن انگشتانش بود و مدام از ظرف آجیل برمی‌داشت تا اینکه سرانجام کارکنان تشریفات، ظرف آجیل را از مقابل او برداشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/23099" target="_blank">📅 14:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رسانه های رژیم
:
با پیگیری‌های انجام شده مرزهای شلمچه و چذابه برای تردد مسافران بازگشایی شد
@WarRoom</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/23098" target="_blank">📅 14:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز:
محمد بن سلمان امروز در جده با دریاسالار برد کوپر، فرمانده سنتکام، دیدار کرد
؛ محور گفت‌وگو تشدید حملات حوثی‌ها و تهدید علیه عربستان و مسیرهای انرژی بود. این دیدار پس از درخواست‌های ریاض از ترامپ برای اقدام نظامی مستقیم علیه حوثی‌ها انجام شد؛ واشنگتن فعلاً حمله مستقیم را نپذیرفته اما حمایت اطلاعاتی و کمک هدف‌گیری به عربستان را در دستور کار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/23097" target="_blank">📅 14:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رویترز: پیشروی حوثی‌ها در امتداد ساحل دریای سرخ، موج تازه‌ای از آوارگی در یمن ایجاد کرده و از ابتدای سپتامبر بیش از ۸۲ هزار نفر مجبور به ترک خانه‌های خود شده‌اند؛ سازمان بین‌المللی مهاجرت درباره تشدید بحران انسانی هشدار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/23096" target="_blank">📅 14:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1ad975d0.mp4?token=Biu9f6OjtgCqC7xqOzZAxdJUK-RIMdApQN6Aw5qLtym25TTB_KKXzv19BNuYsP-jpGCanh3VtPkKc1AKA5xdmjtailfPoLAMZ6NrrcWDvAVy3bFI44pQem_PjX5vYDvcpQ_msgHSLl5T9wqHMsDcCJvF2hvZbj9eMN4BL7Y3_DUu9imOeUb0OwCVwzILJJnT-kl-faic8snel8yWgT0wONRAfWRviHW3UWNQlz5IMlmjGjrpKGLaAHwyPyABFzYCFq-gnsiZikcuP7zHHWM7gxYztFOpwmT4z3nZJFkNOjDQM6zEEL3xbBlykgKmL4j0KNS4j8w4KJAhZih8xbxTgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1ad975d0.mp4?token=Biu9f6OjtgCqC7xqOzZAxdJUK-RIMdApQN6Aw5qLtym25TTB_KKXzv19BNuYsP-jpGCanh3VtPkKc1AKA5xdmjtailfPoLAMZ6NrrcWDvAVy3bFI44pQem_PjX5vYDvcpQ_msgHSLl5T9wqHMsDcCJvF2hvZbj9eMN4BL7Y3_DUu9imOeUb0OwCVwzILJJnT-kl-faic8snel8yWgT0wONRAfWRviHW3UWNQlz5IMlmjGjrpKGLaAHwyPyABFzYCFq-gnsiZikcuP7zHHWM7gxYztFOpwmT4z3nZJFkNOjDQM6zEEL3xbBlykgKmL4j0KNS4j8w4KJAhZih8xbxTgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت ماهواره‌ای اسرائیلی ISI از پرتاب ماهواره جدید
EROS NOVA
برای مأموریت‌های اطلاعاتی، شناسایی و نظارت با دقت بسیار بالا (VVHR) خبر داد. این ماهواره به سامانه تصویربرداری پیشرفته‌ای مجهز است که امکان ثبت تصاویر با وضوح بسیار بالا و شناسایی اجسام کوچک تا حدود
۲۵ سانتی‌متر
را فراهم می‌کند. یکی از قابلیت‌های مهم EROS NOVA،
پردازش داده‌های خام در خودِ فضا پیش از ارسال آنها به ایستگاه‌های زمینی
است؛ قابلیتی که می‌تواند حجم داده‌های ارسالی را کاهش داده و سرعت دریافت و تحلیل اطلاعات را افزایش دهد. به گفته ISI، این ویژگی‌ها EROS NOVA را به ابزاری پیشرفته برای مأموریت‌های اطلاعاتی و نظارتی تبدیل می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/23095" target="_blank">📅 14:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاملترین نسخه و با بهترین ترجمه و خواناترین زیرنویس فارسی از گزارش ویژه «۶۰ دقیقه» شبکه CBS درباره عملیات نجات افسر تسلیحات یک فروند F-15E آمریکایی که پس از سقوط جنگنده در ایران، حدود ۵۰ ساعت در خاک ایران مخفی ماند و در نهایت طی یک عملیات ویژه نجات پیدا کرد. این افسر برای نخستین‌بار درباره لحظه اصابت موشک، خروج اضطراری از جنگنده، جراحات، مخفی‌شدن در مناطق کوهستانی ایران و عملیات نجات خود صحبت می‌کند. این گزارش همچنین تصاویر تازه‌ای از عملیات نجات و جزئیات این مأموریت را منتشر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/23094" target="_blank">📅 13:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e4f0e7504.mp4?token=g87nQ4eVcla33in9ZRibGjcKnM1SUI9AT4MR1xMeJ_ep-KcY7O7PHjCj14UOW8AHPAKLT-Ir3jnMu-VJuITVpw4wLlMhkTNRlRt7ScHcHi4Z5y9Y6d2naEQUyr5vk7p9GQ0b4sxehc9l-ZNlwZNu3BxGQLf_567BWrXb4tKIg2_gcnyO7w3mioX_KLPVjv7VHbOS1gV5ER7uaAHRN5IeRtHKbzLXjAiO-aUmjSEOhVfrp7RYSC9FymMIeuWVa-TTkIwYvitw1uzf76IrCw3O_sXT3uDqf0XvIxGjkGhNzV5RLn3R03MJzBIh3jEOk2yOLG4vs2ivT127eQ7LLI9TBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e4f0e7504.mp4?token=g87nQ4eVcla33in9ZRibGjcKnM1SUI9AT4MR1xMeJ_ep-KcY7O7PHjCj14UOW8AHPAKLT-Ir3jnMu-VJuITVpw4wLlMhkTNRlRt7ScHcHi4Z5y9Y6d2naEQUyr5vk7p9GQ0b4sxehc9l-ZNlwZNu3BxGQLf_567BWrXb4tKIg2_gcnyO7w3mioX_KLPVjv7VHbOS1gV5ER7uaAHRN5IeRtHKbzLXjAiO-aUmjSEOhVfrp7RYSC9FymMIeuWVa-TTkIwYvitw1uzf76IrCw3O_sXT3uDqf0XvIxGjkGhNzV5RLn3R03MJzBIh3jEOk2yOLG4vs2ivT127eQ7LLI9TBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏نیروی هوایی عربستان سعودی تصاویری از حملات هوایی علیه اهداف حوثی‌ها در یمن منتشر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/23093" target="_blank">📅 13:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf59f98ca.mp4?token=p4Q_2yiXQ90NpZ4jF4HIO7u5t39hYD4lVcnjzLBk4cPxLbn41fe0MxET5hjFwW1ZXHT0VCezLADoeTHUEe1OEkUMwpHXmOUgMT_77fqB_TaJlX8sLBJn3BhZbHnXyXjNG1ZEhfwahWPLD0zxLUY0eAJe3pfkAD31T7U6xtLX7PSv357eMueHqg0OP4eFnCWuZkjKPNUHRHHvdnzpiiU77uXvOXR4tJ-xf1OHUHd5GHg5VDh84viK3QdUp_02qMRpmfjg7Zhwi__fLG88Yw9SXXNxNCJGDlW5EQWxIyz9bcsudVqkg3Ivh8mS-uyBKH9M1_AfkK73AAm20YSVxydyDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf59f98ca.mp4?token=p4Q_2yiXQ90NpZ4jF4HIO7u5t39hYD4lVcnjzLBk4cPxLbn41fe0MxET5hjFwW1ZXHT0VCezLADoeTHUEe1OEkUMwpHXmOUgMT_77fqB_TaJlX8sLBJn3BhZbHnXyXjNG1ZEhfwahWPLD0zxLUY0eAJe3pfkAD31T7U6xtLX7PSv357eMueHqg0OP4eFnCWuZkjKPNUHRHHvdnzpiiU77uXvOXR4tJ-xf1OHUHd5GHg5VDh84viK3QdUp_02qMRpmfjg7Zhwi__fLG88Yw9SXXNxNCJGDlW5EQWxIyz9bcsudVqkg3Ivh8mS-uyBKH9M1_AfkK73AAm20YSVxydyDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در گوشه ای از مستند جنجالی نجات خلبان اف‌۱۵ نیرو های سپاه در نزدیکی او در خاک ایران هدف قرار گرفته میشوند ؛ حتی یک نفر از ۷ سپاهی سوت موشک که به سمتشان می میرود رو می احساس میکند و سعی می کنه به افراد خبر بده اما نمی داند به کدام سمت بروند. در نهایت انفجار…</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/23092" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سازمان بنادر و دریانوردی ایران اعلام کرد
۷۷ کشتی
در فهرست عدم انطباق (NCL) قرار گرفته‌اند و به بیمه‌گران، باشگاه‌های P&I و مؤسسات رده‌بندی هشدار داد از ارائه خدمات به این کشتی‌ها خودداری کنند. بر اساس این اطلاعیه، کشتی‌های متخلف در عبورهای بعدی ممکن است با
جریمه، توقیف یا مصادره
مواجه شوند. همچنین هر کشتی که از طریق انتقال کشتی‌به‌کشتی (STS)، ترانشیپمنت یا همکاری مشابه با کشتی‌های فهرست‌شده همکاری کند، به این فهرست اضافه خواهد شد. ایران اعلام کرده کشتی‌های قرارگرفته در این فهرست می‌توانند برای
حذف نام خود، درخواست فرم رسمی همراه با دلایل و توضیحات
ایمیل کنند؛ با این حال، در اطلاعیه منتشرشده
هیچ هزینه یا مبلغ مشخصی احتمالی برای خروج از فهرست اعلام نشده است
.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/23091" target="_blank">📅 12:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حمله بامدادی ایران به استان سلیمانیه با شلیک ۵ موشک:
آژانس امنیت اقلیم کردستان اعلام کرد حدود ساعت ۳:۱۰ بامداد دوشنبه ۲۳ شهریور، پنج موشک به سه منطقه در استان سلیمانیه اصابت کرده است؛ سه موشک در زرگویزله، یک موشک در نزدیکی روستای گرگه‌چیا در سیروان و موشک پنجم در حدفاصل داری زاین و میراسی سفلی در قره‌داغ فرود آمده‌اند. این حملات
تلفات جانی نداشته
و آژانس اقلیم از مردم خواسته از محل اصابت‌ها و بقایای موشک‌ها و پهپادها فاصله بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/23090" target="_blank">📅 12:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزارت خارجه چین روز دوشنبه ۲۳ شهریور گزارش‌ها درباره ارائه تصاویر ماهواره‌ای به جمهوری اسلامی پیش از حمله موشکی ۱۷ شهریور به پایگاه موفق‌السلطی در اردن را «بی‌اساس» خواند و رد کرد. مقام‌های آمریکایی گزارش داده بودند که جمهوری اسلامی پیش از این حمله، تصاویر ماهواره‌ای این پایگاه را از نهادهایی چینی دریافت کرده بود؛ حمله‌ای که به کشته شدن ۳ نظامی آمریکایی انجامید ولی نام این نهادها را اعلام نکرده و دولت چین را نیز مستقیماً به مشارکت در حمله متهم نکرده‌اند. پیش‌تر نیز در حادثه‌ای مشکوک ماهواره شناسایی چینی Yaogan-50 (02) در یک رویداد نادر در مدار زمین از هم پاشیده و دست‌کم ۴۳ قطعه از آن شناسایی شده است. علت این حادثه همچنان در دست بررسی است و تاکنون مشخص نشده که این ازهم‌پاشیدگی ناشی از نقص فنی، برخورد یا عامل دیگری بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/23089" target="_blank">📅 12:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eda4cc06e.mp4?token=odtlmWCjAQrV2zbPzcTlcRhkB44Zq_Od6RFiehYsVr9puzFjHEgOwannvsoRiugEx5z6Ucqmy8iZ31NmPLetjjM5EcEvLAY-skuhg84Lx0WTY-OY3YEI7DA79SrzZqEFyBSV9AOXJnMDmqX8g4yBDBhgl7wvmBtrnRRqw3KoPJQTP6mi0J3EaHLIMpq9fSg5pxijpqxrtrBv5T-Wz1fYutqyHH1MgZ3B39E04Bmqn6bPBWCA5Ra9LiUBfxP7Ax6gkPPK_QLbUIFNgBvkktkmTxTIFQb9A-LBuS2kv2PtdCSpSvOg93k05G6lruwBFxbh7zngrWVony5YM4U-VwzYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eda4cc06e.mp4?token=odtlmWCjAQrV2zbPzcTlcRhkB44Zq_Od6RFiehYsVr9puzFjHEgOwannvsoRiugEx5z6Ucqmy8iZ31NmPLetjjM5EcEvLAY-skuhg84Lx0WTY-OY3YEI7DA79SrzZqEFyBSV9AOXJnMDmqX8g4yBDBhgl7wvmBtrnRRqw3KoPJQTP6mi0J3EaHLIMpq9fSg5pxijpqxrtrBv5T-Wz1fYutqyHH1MgZ3B39E04Bmqn6bPBWCA5Ra9LiUBfxP7Ax6gkPPK_QLbUIFNgBvkktkmTxTIFQb9A-LBuS2kv2PtdCSpSvOg93k05G6lruwBFxbh7zngrWVony5YM4U-VwzYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در گوشه ای از مستند جنجالی نجات خلبان اف‌۱۵ نیرو های سپاه در نزدیکی او در خاک ایران هدف قرار گرفته میشوند ؛ حتی یک نفر از ۷ سپاهی سوت موشک که به سمتشان می میرود رو می احساس میکند و سعی می کنه به افراد خبر بده اما نمی داند به کدام سمت بروند. در نهایت انفجار هر ۷ سپاهی را متلاشی میکند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/23088" target="_blank">📅 11:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی : هنوز ویزای آمریکای ما برای سفر به ‌نیویورک صادر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/23087" target="_blank">📅 11:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/23086" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیویورک‌تایمز :
ایران تشدید تنش را مسیری مؤثر برای افزایش نفوذ و قدرت چانه‌زنی خود در برابر آمریکا می‌داند.
تهران و متحدانش اکنون بر دو مورد از مهم‌ترین مسیرهای انتقال نفت جهان،
تنگه هرمز و باب‌المندب
، نفوذ و اهرم فشار دارند؛ هرمز تحت تأثیر اقدامات مستقیم ایران و باب‌المندب تحت تأثیر پیشروی حوثی‌های مورد حمایت تهران قرار گرفته است. به نوشته این روزنامه، ایران تلاش می‌کند از شرایط ایجادشده در جنگ و اختلال در مسیرهای انرژی،
دستاوردی راهبردی به دست آورد که بتواند جایگاه تهران را در منطقه و در هرگونه مذاکره با واشنگتن تقویت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/23085" target="_blank">📅 11:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی‌ان‌ان: آمریکا خواهان تمرکز مذاکرات با ایران بر پرونده هسته‌ای است، نه تنگه هرمز:
به گفته سه منبع آگاه، دولت ترامپ به‌طور خصوصی به کشورهای منطقه اعلام کرده که ترجیح می‌دهد مذاکرات آینده با ایران بر
پرونده هسته‌ای
متمرکز باشد، نه بازگشایی هرمز. سی‌ان‌ان همچنین گزارش داد تعویق نشست عمان در شرایطی رخ داده که برخی کشورهای منطقه نگرانند توافق پیشنهادی درباره هرمز به ایجاد
وضعیت موجود جدید و دائمی
در این آبراه منجر شود؛ وضعیتی که برای عربستان و دیگر کشورهای شورای همکاری خلیج فارس قابل قبول نباشد
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/23084" target="_blank">📅 11:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اکسیوس ـ باراک راوید: عربستان سعودی در پیشنهاد ایران و عمان درباره تنگه هرمز اصلاحاتی ارائه کرده است.
یک مقام ارشد از کشورهای خلیج فارس به باراک راوید گفته است که ریاض نگران بوده متن فعلی پیشنهاد، عملاً به ایجاد
وضعیت موجود جدیدی در تنگه هرمز
منجر شود که برای عربستان و سایر کشورهای شورای همکاری خلیج فارس قابل قبول نباشد. این اصلاحات در حالی مطرح شده که
نشست منطقه‌ای کشورهای خلیج فارس و ایران در صلاله عمان به تعویق افتاده است
؛ وزیر خارجه عمان گفته این تعویق با هدف فراهم‌کردن زمینه برای دستیابی به اجماع انجام شده است
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/23083" target="_blank">📅 11:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_iAwEGQPGKtoCG-oi2c5uZWAbrLaL6WLISlkahJnA-ikZS_ASF-j0f8PRPWYXTXasD7_aByqURsgKoKkjrjLYilioetYjWs1SftaMwBTuHfFgngFoL02JlpKndIQmodRHqloE_JogxyIzY7JNWnMElsEqiZNTL2V44C6cKDvDYK1Rcgkq-ycHsDR4CfV9LripT_dRGPKzr08a2qK3rWWSsvWDdeS8qvxHqST3OEAak_f2tlsRoRdQC6hdCGbjurA1Q8-oWUZ-dXuMCC3BtNqo7yDzSjQEZ6lNqnmMQw__i0H9OiS2FvtVn0QI0N2VQQpheuvkxvFYXICsb3ApOOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت به سبک کامیک بوک
دوستون دارم
🙌🏾
❤️‍🩹
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23082" target="_blank">📅 05:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">روایتی_نفس_گیر_از_نجات_افسر_تسلیحات_آمریکایی.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/withyashar/23081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">متن کامل روایت افسر تسلیحات اف ۱۵
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23081" target="_blank">📅 05:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پارت ۲: افشای جزئیات فرار و نجات افسر آمریکایی پس از سرنگونی جنگنده بر فراز ایران و گذراندن ۲ روز با استخانهای شکسته(فارسی)
برای نخستین‌بار، افسر نیروی هوایی آمریکا با نام رمز
«براوو»
که پس از سرنگونی جنگنده‌اش بر فراز ایران، به مدت
دو روز پشت خطوط دشمن
گرفتار شده بود، در برنامه «۶۰ دقیقه» جزئیات این حادثه را روایت کرد. او پس از اجکت، به دلیل آسیب‌دیدگی و باز نشدن کامل چتر نجات، با سرعت حدود
۱۱۰ تا ۱۶۰ کیلومتر بر ساعت
به زمین برخورد کرد و در این حادثه
کمر، دست و شانه‌اش شکست
. براوو که در یک دره گرفتار شده بود، برای فرار از نیروهای ایرانی خود را به ارتفاع حدود
۲۱۳۰ متری
رساند. طبق منابع نظامی آمریکا، نیروهای ایرانی در مقطعی تا فاصله
چندصد متری
او پیش رفتند. ارتش آمریکا برای عملیات نجات این خلبان/افسر، یک مأموریت پرخطر روزانه با مشارکت
۲۱ فروند هواپیما
انجام داد. براوو می‌گوید نخستین پیامی که پس از برقراری ارتباط توانست برای آمریکا ارسال کند این بود:
«خدا خوب است.»
او پس از دو روز سرانجام نجات یافت و توانست با همسرش در آمریکا تماس بگیرد. براوو همچنین تأکید کرد:
«بدون ایمان، این داستان را نداشتم»
و گفت اگرچه ایمان جایگزین آموزش نظامی نیست، اما «پشتوانه تمام اقدامات» او بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23080" target="_blank">📅 04:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23079" target="_blank">📅 04:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انتشار نخستین تصاویر نجات خلبان F-15 سرنگون‌شده آمریکا در ایران شبکه آمریکایی سی‌بی‌اس تصاویری از عملیات نجات خلبان آمریکایی منتشر کرده که جنگنده F-15 او در جریان جنگ رمضان در آسمان ایران هدف قرار گرفته و سرنگون شده بود. این تصاویر برای نخستین‌بار لحظات عملیات…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23078" target="_blank">📅 04:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انتشار نخستین تصاویر نجات خلبان F-15 سرنگون‌شده آمریکا در ایران شبکه آمریکایی سی‌بی‌اس تصاویری از عملیات نجات خلبان آمریکایی منتشر کرده که جنگنده F-15 او در جریان جنگ رمضان در آسمان ایران هدف قرار گرفته و سرنگون شده بود. این تصاویر برای نخستین‌بار لحظات عملیات…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23077" target="_blank">📅 04:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انتشار نخستین تصاویر نجات خلبان F-15 سرنگون‌شده آمریکا در ایران
شبکه آمریکایی سی‌بی‌اس تصاویری از عملیات نجات خلبان آمریکایی منتشر کرده که جنگنده F-15 او در جریان جنگ رمضان در آسمان ایران هدف قرار گرفته و سرنگون شده بود.
این تصاویر برای نخستین‌بار لحظات عملیات نجات خلبان پس از سقوط جنگنده آمریکایی در خاک ایران را نشان می‌دهد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23076" target="_blank">📅 03:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer"><a href="https://t.me/withyashar/23074" target="_blank">📅 03:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:
ما به سرعت ذخایر سلاح‌های خود را بازسازی می‌کنیم و در حال حاضر موشک‌های پاتریوت را با تعداد بیشتری نسبت به هر زمان دیگری تولید می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23072" target="_blank">📅 02:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بلومبرگ: محمد اسلامی، رئیس سازمان انرژی اتمی ایران، پس از آنکه اتریش تحت فشار دولت ترامپ از ورود او جلوگیری کرد، از حضور در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین بازماند.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند، اما ممکن است یک نماینده رده‌پایین‌تر ایران در ادامه هفته به نمایندگی از تهران سخنرانی کند. انتظار می‌رود
کریس رایت، وزیر انرژی آمریکا،
در این کنفرانس هشدار دهد که «ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند یا آن را تولید کند» و هم‌زمان خواستار
همکاری کامل ایران با آژانس و دسترسی بازرسان آژانس به تأسیسات هسته‌ای ایران
شود.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23071" target="_blank">📅 02:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ درباره هوش مصنوعی:
مزایای آن بسیار بیشتر از معایبش خواهد بود.
ما با اختلاف زیادی پیشتاز هستیم. هر کس در حوزه هوش مصنوعی پیروز شود، برنده نهایی خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23070" target="_blank">📅 02:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار: ممکن است نهادهای چینی تصاویر ماهواره‌ای در اختیار ایرانی‌ها گذاشته باشند.
ترامپ: آن‌ها در واقع همان کاری را می‌کنند که ما انجام می‌دهیم. به نظرم او معقول عمل کرد و ما هم معقول رفتار کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23069" target="_blank">📅 02:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbLeyxDK1ds9Cw4-YChJPD6VwZn17YBqxq2DJNXPMdqiJPCcZt0PuEskz_KaWN31sNICWLSv-saqU6opUV3lgkMA2Vct-kbcB8RJHb59JS0qIJpj8UcVmQa05FbxCsnuNqey-rkI0Nt6Lz0bvo4FHgaiKtG0aMEgLEX7DH4ifd9QRIqgukzKZpMQBPMIcIbqeW4JYs7KAy04xbUzlVdlf_yhqc8ypP0_o1WK1KapNqlgGKEWetlnoz3E1pZl1LSSHc6i649v35GlLW1XMBudaT3NuiX4XcANoXqt1in8zJ6z3MZfV0mhd_rd994F0G2VTu37HSiQbqdtoJ6LkjNRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بحران اقتصادی و جنگ، ایران را با کمبود شدید سوخت روبه‌رو کرده است
وال‌استریت ژورنال گزارش می‌دهد کمبود بنزین باعث
صف‌های طولانی در جایگاه‌ها، اعتصاب رانندگان کامیون و تاکسی و افزایش نارضایتی عمومی
شده است. دولت ایران برای مصرف خارج از سهمیه، قیمت بنزین را دو برابر کرده و این افزایش برای بسیاری از مردم که درآمد ماهانه‌شان حدود ۱۰۰ دلار است، فشار سنگینی ایجاد کرده است. اختلال در پالایشگاه‌های آسیب‌دیده از جنگ و محدودیت واردات سوخت در نتیجه محاصره آمریکا نیز بحران را تشدید کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23068" target="_blank">📅 02:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:فناوری لیزر اهمیت زیادی دارد، چرا که هزینه آن بسیار کمتر از شلیک موشک‌های پاتریوت است.
فعلاً برد آن محدود است، اما به‌زودی برد آن افزایش خواهد یافت.
وقتی تجهیزات را در اختیار داشته باشید، هزینه خودِ پرتو لیزر بسیار ناچیز و تقریباً صفر است. لیزرها همین حالا هم برای مقابله با انواع خاصی از موشک‌ها به‌ویژه موشک‌های کندتر بسیار کارآمد هستند.
به اعتقاد من، آینده از آنِ لیزرهاست.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/23067" target="_blank">📅 02:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: ویتکاف و کوشنر دارند کارشان را عالی انجام می‌دهند.
به غزه به عنوان یک نمونه نگاه کنید؛ درگیری زیادی در غزه وجود ندارد.
حماس اکنون حاضر است سلاح‌هایش را کنار بگذارد. هیچ‌کس دیگری نمی‌توانست کاری را که آن‌ها انجام دادند، به سرانجام برساند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/23066" target="_blank">📅 02:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHTH1HX4sFua6gv1GpVG-dG5m4MmKW__T6cY2F-xQenDWIRWCLlo9G64cp2rqnJppjQOHrkEKoT2Qmsmsq_-uqls4rU9BRtAnx0mCxHpoM1zkgFwZa0W5uyW0wcgHWvX9oZhcB9J4TwxN1L1OiAPfEor75W7TU_OBNnqykdl5MUTKXEXvV5MUPolAXwmlNAIh8fcGJzYmO9mqR0KZQIZkQfHUWscAuHu7Gnsn_KtmsF4v4mgRr0MZt2H-TNA1wbAHYmJVLxwdpIuHdZh2rcAcxL8yG0EQ-RnperzkcgDo7lsqvHdW61NB9d6fn6BDBkhnzNWBfrlS82Y8aNWyOaHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با باز شدن بازار نفت به ۱۰۸ دلار رسید !
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23065" target="_blank">📅 01:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23064" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23063">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV0byndj_OpdG3zdBn0nDl54T13d1wAc2iGKSvdxM-0jlUTxLS3kuaIaStTvdJ7YpS2aNlXa4iUQ1y3_22imlQa6vdnTBLC0mlScafSdPW9C5jNnyM8hFNPYZn4LfFvMyyyqYuB6a69IvgmxovhfOIemhwMlElwIomqRbXgyI60ywmU1IlPvBMCLbtLarfLOwnPSEd9zcxMwl8OMwACf5T8lafv8MdK1T4CpnFtYNYzHdQZuuK0WCdIVZxLQxx2MmpCcLacP0ABLUulfFReESn9ZFQTiOD4JP3pmyQQikslqGaRuSHcdpkA37_gg7pJRUnyXL4t9oKIxrkDPqy5yJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، نیروهای ارتش اسرائیل (IDF) ۳۸ حمله را در مناطق جنوبی لبنان انجام دادند
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23063" target="_blank">📅 01:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23062" target="_blank">📅 01:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23061" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23060" target="_blank">📅 00:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23059" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73711a45e9.mp4?token=YesxWXpjIrs4VtWbMa80xxEN5DHZNepXyRIHbBl5dPs2f_Qmzhuj9EEOeuewXV5vNbwyWlVWgwCGWOqbvS4NUsuUdKgEHhcdUOxVRZlmPoGYQnAKzWiF3sljaB9XAdhS6w_yi2FfBsqfr3eVXdu0cFbTfDokpNsmhoJF5uDAkYQxxO7J4iIYzfqBHOuatSsK_w1EfOSpW8l8z1l-fz8BHV47LVgcaHMNRSiFd1nbXQonVJW0vtzc3Xm0Buc82n24lYPHshle-PnxfSAbRdrHRKahLG_uUBSN-eqeyxGoyofo3U9iqtyY7QIDaBgJUtkIuASMsPUs_8IU5MZGgXGXPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73711a45e9.mp4?token=YesxWXpjIrs4VtWbMa80xxEN5DHZNepXyRIHbBl5dPs2f_Qmzhuj9EEOeuewXV5vNbwyWlVWgwCGWOqbvS4NUsuUdKgEHhcdUOxVRZlmPoGYQnAKzWiF3sljaB9XAdhS6w_yi2FfBsqfr3eVXdu0cFbTfDokpNsmhoJF5uDAkYQxxO7J4iIYzfqBHOuatSsK_w1EfOSpW8l8z1l-fz8BHV47LVgcaHMNRSiFd1nbXQonVJW0vtzc3Xm0Buc82n24lYPHshle-PnxfSAbRdrHRKahLG_uUBSN-eqeyxGoyofo3U9iqtyY7QIDaBgJUtkIuASMsPUs_8IU5MZGgXGXPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : امروز تهه یک کشتی دیگر هم چرخوندیم، سیکش رو زدیم، تعداد کل شد 101
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23058" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">@WarRoom
Level Up</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23057" target="_blank">📅 00:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23056" target="_blank">📅 00:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">@WarRoom
extrime car</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23055" target="_blank">📅 00:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23054">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23054" target="_blank">📅 23:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from➤ 𝗞𝗮𝗶𝘇𝗲𝗻</strong></div>
<div class="tg-text">یاشار چرا نمیری اینترنشنال تحلیلگر بشی</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23053" target="_blank">📅 23:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر جنگ اسرائیل : اگه میتونید تپه علی الطاهرو بیاین بگیرید، هرکی بیاد پسی‌خور میشه
@WarRoom
😂</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23052" target="_blank">📅 23:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">@WarRoom
Package movaghaiat
😁</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23051" target="_blank">📅 23:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان ایران برای ۲۵ شهریور فراخوان اعتصاب سراسری داد: این ائتلاف همزمان با چهارمین سالگرد کشته‌شدن مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی» از مردم در سراسر ایران خواست روز چهارشنبه ۲۵ شهریور با بستن مغازه‌ها و بازارها و خودداری…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23050" target="_blank">📅 23:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیدبان اتاق جنگ : انفجار مهیب نزدیک ساحل سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23047" target="_blank">📅 23:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بدر البوسعیدی، وزیر خارجه عمان: در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاده است. ما همچنان متعهد به تقویت گفت‌وگویی هستیم که از ثبات و همکاری پایدار در منطقه حمایت کند @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23046" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b044a4166f.mp4?token=bGrv8TiAAJ8-EDE6qThMDDfrtsXyVev6Qcm9xkF3Pwvi2WMtv3v_oWxMVMGb0sonoc8mVbqKTPffhG6FFndmc_-qrcLf5ryuCIE7F01vI4z1xJu-3pjRzfViTbIwtoiLXWP2eCgkmpykZUuAS_5tGQBlz3zuc29mE1FWeAiOWVvX2mmCSMU86-hnHUG1ShGSGSB-mH0s2q9Hj9YeKlD_VpqmGzIgrTFYgygnj9uueRh_dX5i0C8sEKA6cN6AogbIbWhG91HbjuiBxu7wj7VaLBl7q3MOCcH_FhdCyXCazPqIByj1E-pPXDicMPpTiDLiwVXcsxWsLoLwZqMnWO6tFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b044a4166f.mp4?token=bGrv8TiAAJ8-EDE6qThMDDfrtsXyVev6Qcm9xkF3Pwvi2WMtv3v_oWxMVMGb0sonoc8mVbqKTPffhG6FFndmc_-qrcLf5ryuCIE7F01vI4z1xJu-3pjRzfViTbIwtoiLXWP2eCgkmpykZUuAS_5tGQBlz3zuc29mE1FWeAiOWVvX2mmCSMU86-hnHUG1ShGSGSB-mH0s2q9Hj9YeKlD_VpqmGzIgrTFYgygnj9uueRh_dX5i0C8sEKA6cN6AogbIbWhG91HbjuiBxu7wj7VaLBl7q3MOCcH_FhdCyXCazPqIByj1E-pPXDicMPpTiDLiwVXcsxWsLoLwZqMnWO6tFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک جانسون، رئیس مجلس نمایندگان ایالات متحده، درباره جمهوري اسلامي:
این جنگ ترامپ در ایران نیست. رژیم ایران بزرگ‌ترین حامی دولتی تروریسم است و آن‌ها در فاصله چند هفته از داشتن قابلیت هسته‌ای l یک بمب هسته‌ای قرار داشتند.پیشگیری از این امر، هدفی بوده است که برای ۵۰ سال، توسط هر دولت دنبال شده است.آن‌ها تا این حد به آن نزدیک شدند و رئیس‌جمهور مجبور به اقدام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23045" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بدر البوسعیدی، وزیر خارجه عمان:
در راستای دستیابی به اجماع،
نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاده است.
ما همچنان متعهد به تقویت گفت‌وگویی هستیم که از
ثبات و همکاری پایدار در منطقه
حمایت کند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23044" target="_blank">📅 22:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان ایران برای ۲۵ شهریور فراخوان اعتصاب سراسری داد:
این ائتلاف همزمان با
چهارمین سالگرد کشته‌شدن مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»
از مردم در سراسر ایران خواست روز چهارشنبه ۲۵ شهریور با
بستن مغازه‌ها و بازارها و خودداری از حضور در محل کار
دست به اعتصاب بزنند. این ائتلاف، اعتصاب را «مبارزه‌ای مدنی و پاسخی جمعی» به وضعیت امنیتی و اقتصادی کشور خوانده و با اشاره به ادامه بازداشت فعالان سیاسی و مدنی، افزایش احکام سنگین و اعدام‌ها، از احزاب، تشکل‌های مدنی و اقشار مختلف مردم خواسته است از این فراخوان حمایت کنند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23043" target="_blank">📅 22:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ از لغو تعرفه‌های ویسکی ایرلندی خبر داد و گفت «همه مدام پیگیر این موضوع بودند»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23042" target="_blank">📅 22:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23041" target="_blank">📅 22:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from... ...</strong></div>
<div class="tg-text">درود آقا یاشار. السیسی وجود دارد در داخل رژیم؟ و بنظرتون اگه وجود دارد چه زمانی رو میشود؟</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23039" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سی‌ان‌ان: عمان پیشنهاد ایران برای دریافت اجباری عوارض را رد کرد و پرداخت‌های داوطلبانه برای ایمنی ناوبری و زیست‌محیطی را پیشنهاد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23038" target="_blank">📅 21:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMqjvqnjJyM4mTZyDqZtVuWsBc4h1AQUV5Gx3pqvf0ggYwSq8Rgucvnvm52Wuev0tyh8vP3AxjmEZKj-6EyhhHbqa6daZEHuAZdVA7ajB_vzJNerlkY29GtzewK4HNxcWH_SHNg8PRpQdzAc2DEuo1IsYxKieRkyyZOK_1RJ8A5fxwNjDKI1c5_Z7nEHNpzJoWpGTCWRPJnqRO0RyRFqYAOFKGeWjLqisOKVxPCiq-8xEBP9Zp2UEb7ciUwmDH9hsy6JsG833mmxUtiHX_h1GHOUKxnL3gPRlVInQOcSFzOkLV5o1EOu7uoLNtjxFWJDDipghz-Bx4KF89rWR40LWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون پرتاب سه موشک از یک نخلستان نزدیک سیریک به سمت تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23037" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f697ad6f42.mp4?token=k0pyR5cEt8B9fRtChPzTsHa1D0yEhjopNUNOktRXGWwH-ntCEnp4jrfLcCPNEPyQrQ5Rz5n70Hyqg_vkFDd_xetp6pIQmuqKijBpC2nzWByezr6wtZA7db5OPl4sAlozHfwa6OjNYyge-Q1pAjYQrWx7br-l_P4PKJwPLUXCvHEzVBgHK-R2fkZhGXGYaZBkBHWKQsfulFWFRjTaahAH4o-nAXamLzLjv7CQxYQjN2PUy_H38zBmAi4hlYwric_B9xfmN9SOeo7tcrVYmiMgyiZBCK8J4qobvERLayk9gjJOfct0kq0cPi8mHJzjRydYrQ2Wf-P_3IsVlG4HAu2zsxlITykatjS7HDD8mKLlZHIr8PdhH8Urubg2wE8SQgVHtdXaGr0jhmwPDtlwJc5k_ycmAGKfRUBoDWEqREisekhVxw70p66sdpsA_deGxTyQIStKVxFqMLwSU9b1fUYVnVbdhiAi2EVY1IlIFMR0Q9DNWh3kAMGRUR2gyrZ9sM5hKkw-vTI0Gtaw7KLArbxsQKgvzFVyHj0be3ZFSjrvNzUD-h3bX3ZgP48hC_yxZbF3KNxxH7notSH9HKsTZTkst-j1eQxRfPWZMG9Jd864I7nNWsjnO3dfYbPS60mggSzgSGBqwFoml_Jtv9MdjrICL0iGSeyC_xbzzLxqEqQlzLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f697ad6f42.mp4?token=k0pyR5cEt8B9fRtChPzTsHa1D0yEhjopNUNOktRXGWwH-ntCEnp4jrfLcCPNEPyQrQ5Rz5n70Hyqg_vkFDd_xetp6pIQmuqKijBpC2nzWByezr6wtZA7db5OPl4sAlozHfwa6OjNYyge-Q1pAjYQrWx7br-l_P4PKJwPLUXCvHEzVBgHK-R2fkZhGXGYaZBkBHWKQsfulFWFRjTaahAH4o-nAXamLzLjv7CQxYQjN2PUy_H38zBmAi4hlYwric_B9xfmN9SOeo7tcrVYmiMgyiZBCK8J4qobvERLayk9gjJOfct0kq0cPi8mHJzjRydYrQ2Wf-P_3IsVlG4HAu2zsxlITykatjS7HDD8mKLlZHIr8PdhH8Urubg2wE8SQgVHtdXaGr0jhmwPDtlwJc5k_ycmAGKfRUBoDWEqREisekhVxw70p66sdpsA_deGxTyQIStKVxFqMLwSU9b1fUYVnVbdhiAi2EVY1IlIFMR0Q9DNWh3kAMGRUR2gyrZ9sM5hKkw-vTI0Gtaw7KLArbxsQKgvzFVyHj0be3ZFSjrvNzUD-h3bX3ZgP48hC_yxZbF3KNxxH7notSH9HKsTZTkst-j1eQxRfPWZMG9Jd864I7nNWsjnO3dfYbPS60mggSzgSGBqwFoml_Jtv9MdjrICL0iGSeyC_xbzzLxqEqQlzLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23036" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e431617c.mp4?token=X9E-uiWXJtPIJJ3sWytKc1BS-bqCRw2XQt9bUpgu4L8atch-oyuIsO5WOXKe7oSHO39KboQOUUn6IkQdI75konl9dKCx-pvJVqMkbcxqG89TE7NZ4_3pI0i30cp-Kk6DyPn5IfQwXMbfZDa9YevUTOqvu7QuxHPB1GQoR92-a7DRsnCYkcJZz-phMj0hSYYjznC_q1eTDRjpdhoRcjlTUREuJW3-Qp5Irx2evXREHO7u54cAmHjFbDDLQyAi3QqNPdjjwf83p8v-QBbgvhWNDMkHTdPldOiTl9X6LrgYuh-y3cZdRvKvbaIbAXkgdO7bHfsoqNGq9EubVsTBuj0hPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e431617c.mp4?token=X9E-uiWXJtPIJJ3sWytKc1BS-bqCRw2XQt9bUpgu4L8atch-oyuIsO5WOXKe7oSHO39KboQOUUn6IkQdI75konl9dKCx-pvJVqMkbcxqG89TE7NZ4_3pI0i30cp-Kk6DyPn5IfQwXMbfZDa9YevUTOqvu7QuxHPB1GQoR92-a7DRsnCYkcJZz-phMj0hSYYjznC_q1eTDRjpdhoRcjlTUREuJW3-Qp5Irx2evXREHO7u54cAmHjFbDDLQyAi3QqNPdjjwf83p8v-QBbgvhWNDMkHTdPldOiTl9X6LrgYuh-y3cZdRvKvbaIbAXkgdO7bHfsoqNGq9EubVsTBuj0hPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام، می‌گوید هیچ‌گونه نگرانی‌ای بابت کمبود مهمات آمریکا ندارد.
«ما به‌خوبی مسلح و برای هرگونه وضعیت احتمالی آماده هستیم.»
کوپر در پاسخ به این پرسش که آیا نگران تهدیدهای آینده است، گفت: «خیر، نگران نیستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23035" target="_blank">📅 20:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23034" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا تنها</strong></div>
<div class="tg-text">سلام .
میشه دلیل اینکه بنده رو از گروه بیرون کردید رو بدونم</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23033" target="_blank">📅 20:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23032" target="_blank">📅 20:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قصه قورباغه و دیگ آب جوش
@WarRoom
🐸</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23031" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اطلاعیه رسمی قرارگاه جانفدای کشور:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قرار است به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فوری اعزام شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23030" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23029" target="_blank">📅 20:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMalekshahirad</strong></div>
<div class="tg-text">رویا چرا الکی می‌فروشی ب مردم مرد نامومن</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23027" target="_blank">📅 19:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23026">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فایننشال‌تایمز :
حمله پهپادی روسیه به قطار نزدیک مرز لهستان:
یک پهپاد روسی امروز به
قطار تخلیه‌شده کی‌یف–ورشو
در نزدیکی مرز لهستان اصابت کرد؛ این قطار تنها حدود یک ساعت پس از قطاری حرکت می‌کرد که
بوریس جانسون، نخست‌وزیر پیشین بریتانیا، کارل بیلت، نخست‌وزیر پیشین سوئد و شماری از دیپلمات‌ها و مقام‌های اروپایی
در آن حضور داشتند. قطار حامل مقام‌ها لحظاتی پیش‌تر از منطقه عبور کرده و وارد خاک لهستان شده بود. قطار هدف‌قرارگرفته ۲۰۶ مسافر داشت و پیش از حمله به دلیل هشدار پهپادی تخلیه شده بود؛
در این حمله کسی زخمی نشد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23026" target="_blank">📅 19:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba17bf936a.mp4?token=i37R5oYz1SP_kMmB_dopeMyzfrg5-md0CvyixZtrYblE3m7z9d-o9SDj8NvVStoRNpyUblDEvi33yYxbY8e5kcqEMOn9sj74VjfgMy5olaT_fTx2fYKZ1_REq-8WY_PbzNX0rWmHnAI1GEDjTls7nRetnpxdNNvX21zOFt7F6CdcbSPj8l6RKtc3G8lWcR6zXmkyhF7EZtwk5_BR5pMXjztSo0Q7ZFYvEaJhMoig7ryFDvZe4jepgqZJbO8TVlWkWLhcMSM_AHkID5iJO6qAWLCgE3JaXVppdjJD2x2buXj_DuE5tdGznrBjTDNukuVpgRMDxlxQA-T5lb3Wvg4zuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba17bf936a.mp4?token=i37R5oYz1SP_kMmB_dopeMyzfrg5-md0CvyixZtrYblE3m7z9d-o9SDj8NvVStoRNpyUblDEvi33yYxbY8e5kcqEMOn9sj74VjfgMy5olaT_fTx2fYKZ1_REq-8WY_PbzNX0rWmHnAI1GEDjTls7nRetnpxdNNvX21zOFt7F6CdcbSPj8l6RKtc3G8lWcR6zXmkyhF7EZtwk5_BR5pMXjztSo0Q7ZFYvEaJhMoig7ryFDvZe4jepgqZJbO8TVlWkWLhcMSM_AHkID5iJO6qAWLCgE3JaXVppdjJD2x2buXj_DuE5tdGznrBjTDNukuVpgRMDxlxQA-T5lb3Wvg4zuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23025" target="_blank">📅 19:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">درصد ٪
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23024" target="_blank">📅 19:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=CJfwqr-DdEwJ3WrcryRLVhaoY0ijEP543YisT3HkYOKJ_j_J8grex4DiYz42YZNdFX416JGxpqEfPYpzeY0AfPMCbRGyItY_eQrnY-sABDE2CQVWddb2EaSGkAfnxK4YJVVYFwCpcjmSVqeGR_osekp3MJ_hKM5mhGJPsAIRcMy6f1LLjl2LHzTypSnnwSvYq49_6NLr_e7Q38y4Ww72TCnvusaqTyYa-4_ItWy_QWKeOTBEvuJ_npyf65_epn8ljKL94WhQ7-B4BMeTkgrItHP_nEoUCC7Th6jJvxZQVNCRi36yv0Kz9ZYVqcgKHugPPUlQAuq2FkjHQIO-YxOHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=CJfwqr-DdEwJ3WrcryRLVhaoY0ijEP543YisT3HkYOKJ_j_J8grex4DiYz42YZNdFX416JGxpqEfPYpzeY0AfPMCbRGyItY_eQrnY-sABDE2CQVWddb2EaSGkAfnxK4YJVVYFwCpcjmSVqeGR_osekp3MJ_hKM5mhGJPsAIRcMy6f1LLjl2LHzTypSnnwSvYq49_6NLr_e7Q38y4Ww72TCnvusaqTyYa-4_ItWy_QWKeOTBEvuJ_npyf65_epn8ljKL94WhQ7-B4BMeTkgrItHP_nEoUCC7Th6jJvxZQVNCRi36yv0Kz9ZYVqcgKHugPPUlQAuq2FkjHQIO-YxOHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23023" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPo</strong></div>
<div class="tg-text">ما نخواهیم پول نفت مون نره لبنان و فلسطین و نفت مون رو آمریکا بر نداره چیکار کنیم ؟</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23022" target="_blank">📅 18:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک‌تایمز: تندروهای جمهوری اسلامی در اوایل ژوئیه مخفیانه توافق با آمریکا را با دستور حمله به سه کشتی تجاری در تنگه هرمز در ۷ ژوئیه به شکست کشاندند:
مقام‌های ایرانی به نیویورک‌تایمز گفته‌اند
مسعود پزشکیان، احمد وحیدی و بخش بزرگی از رهبری ایران از این عملیات بی‌اطلاع بودند.
تحقیقات، تصمیم حمله را به جناح تندروی مرتبط با
حسین طائب، روحانی بانفوذ و رئیس سابق اطلاعات سپاه
نسبت داده است؛ این جناح از ابتدا مخالف توافق بود و به فرماندهان میدانی اختیار داده بود بدون تأیید مرکز به کشتی‌هایی که ناقض کنترل ایران بر تنگه می‌دانستند حمله کنند. پس از حملات، پزشکیان با وحیدی تماس گرفت و با لحنی تند خواستار توضیح شد. این اقدام مذاکرات را از مسیر خارج کرد و
حملات مجدد آمریکا در روز بعد
را به دنبال داشت و در ایران نیز کشمکش قدرت، اتهام خیانت و تهدید به استعفای برخی فرماندهان ارشد را رقم زد.
عباس عراقچی
برای کاهش تنش به عمان اعزام شد، اما موفق نشد. هم‌زمان،
نبود
مجتبی خامنه‌ای
بر بحران افزود و مقام‌هایی گفتند حتی پزشکیان درباره اصالت برخی دستورها و پیام‌های منتسب به او تردید کرده است.
طبق گزارش، هم اکنون
جناح تندرو دست بالا را پیدا کرده و به‌جای بازگشت به مذاکرات، خواهان تشدید حملات علیه نیروهای آمریکایی، شناورها و زیرساخت‌های انرژی منطقه شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23021" target="_blank">📅 18:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23020" target="_blank">📅 18:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: با ایران به توافق رسیدیم، توافق خیلی خوبی بود، دیگه هیچ سلاح هسته‌ای در کار نخواهد بود. تقریباً همه‌چیز نهایی شده و ما به هر چیزی که می‌خواستیم رسیدیم. مهم‌ترین بخش ماجرا اینه که ایران هیچ سلاح هسته‌ای نه خودش می‌سازه و نه از جایی می‌خره.  ما امروز…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23019" target="_blank">📅 17:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23018" target="_blank">📅 17:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
instagram.com/YasharMotors
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23017" target="_blank">📅 17:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFatemeh</strong></div>
<div class="tg-text">ی تحلیل کن اقا یاشار</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23016" target="_blank">📅 17:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMَ reza</strong></div>
<div class="tg-text">چرا موج مکزیکی تموم نمیشه</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23015" target="_blank">📅 17:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976afe9552.mp4?token=ZRPZmWo-4T0Hu605ZGJlcWtoCNuZX05v5dkj00ZaEVRJYDPIZgKDGKbJG3Avdhyy_r9X9WSXBafTm3NcVL6F9PQb9Xh_wkC9DObMa9ebUFuhH45003UKnpzC0cTGoP_qpHmZCJjptL9VRZOkvnPBpMePSbMyMMIcrN2szfiNa6kdEV6b0wF5P4Rr8WO8zr7M9tNyq_cl48m-DZBLZrQg-QuCyh5_GUGtrcHeXeTUl5nUAIH3kEn9lXOHj_d6CdE6WdENzPGnLrnrrmo5VOzG9EiL2lTjaPKry6ZZEPvF4p9Iwd3o4mrrlRXYc1Q2IRRx5Rdmyhf8ZJgD_ws-_L_9Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976afe9552.mp4?token=ZRPZmWo-4T0Hu605ZGJlcWtoCNuZX05v5dkj00ZaEVRJYDPIZgKDGKbJG3Avdhyy_r9X9WSXBafTm3NcVL6F9PQb9Xh_wkC9DObMa9ebUFuhH45003UKnpzC0cTGoP_qpHmZCJjptL9VRZOkvnPBpMePSbMyMMIcrN2szfiNa6kdEV6b0wF5P4Rr8WO8zr7M9tNyq_cl48m-DZBLZrQg-QuCyh5_GUGtrcHeXeTUl5nUAIH3kEn9lXOHj_d6CdE6WdENzPGnLrnrrmo5VOzG9EiL2lTjaPKry6ZZEPvF4p9Iwd3o4mrrlRXYc1Q2IRRx5Rdmyhf8ZJgD_ws-_L_9Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ماجرای ایران درست پس از انتخابات میان‌دوره‌ای و شاید حتی پیش از آن به پایان خواهد رسید.
قیمت بنزین به‌شدت سقوط خواهد کرد. من می‌دانستم چه کار می‌کنم؛ چاره‌ای جز انجام آن نداشتم. ایران نباید سلاح هسته‌ای داشته باشد و هرگز هم به آن دست نخواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23013" target="_blank">📅 17:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5a025761.mp4?token=WP2D3yLPo5dQ9QNnFFE8Agg0ijXepur72R9F16H9r9WqtfIl4qvpDBt0CTUWAZVrLoD5eLwm-y3EMiMjfsj4Z3Hc1jPYU1b5dgUFlfLdLt7aeaEcqIfPR1ufhXI2SG--SMW4zlszxbdNCbMx826PnOeZkFuU7-zB_uK_m9mye9_TbIBMQ80UTFLiSssBpE6bycQIKFCNTxmPZbn6GrDx2-YESC5Ran2tOi14ULbCcbVyERqLepbUzC9Ake1XaKnGS6tXywsRPEm2r8dZFLKhnszM7b29-tcrGq8XT4gACm-EkFv6VRFwMaGGylStd-gnz6tCc7oBxpuhBA-b9wG64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5a025761.mp4?token=WP2D3yLPo5dQ9QNnFFE8Agg0ijXepur72R9F16H9r9WqtfIl4qvpDBt0CTUWAZVrLoD5eLwm-y3EMiMjfsj4Z3Hc1jPYU1b5dgUFlfLdLt7aeaEcqIfPR1ufhXI2SG--SMW4zlszxbdNCbMx826PnOeZkFuU7-zB_uK_m9mye9_TbIBMQ80UTFLiSssBpE6bycQIKFCNTxmPZbn6GrDx2-YESC5Ran2tOi14ULbCcbVyERqLepbUzC9Ake1XaKnGS6tXywsRPEm2r8dZFLKhnszM7b29-tcrGq8XT4gACm-EkFv6VRFwMaGGylStd-gnz6tCc7oBxpuhBA-b9wG64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران به‌شدت خواهان دستیابی به توافق است. آن‌ها مدام تماس می‌گیرند.
ما باید توافق درستی انجام دهیم. من تن به توافقی که خوب نباشد، نخواهم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23012" target="_blank">📅 17:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2125e8e92b.mp4?token=p-ikbkJUVW34SrygffR5YTS9ne7rc5ON2Jte_Luldi4TCUaLKs6-H0jfNaNRDcvhZszC2HNop4QbAxU8po6xvlThDREvwYnSmtbaAzHXAgGuz5HVSpL0mRdy_Rtps2qxQPqIT7mJx8l30KGMG9mX5AOrdwwH8Mu_zZBOt5c6YgaqV7O_3RYWPFH0pOmDDlWq9rSSwPRjg_FT1YIxcBjYsTKb6dojZTJvtwOfuOfR0kj5WAiDTWW1Xm1kWYpRAiluhcUWnJtb8OdoyjlGXoiA0pOnqv-BzZFVbfC7sArTX0nQsH8T1tc1rQiQ_qBjPKsMaRNDlFr_Msvh5Ts2BfTUjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2125e8e92b.mp4?token=p-ikbkJUVW34SrygffR5YTS9ne7rc5ON2Jte_Luldi4TCUaLKs6-H0jfNaNRDcvhZszC2HNop4QbAxU8po6xvlThDREvwYnSmtbaAzHXAgGuz5HVSpL0mRdy_Rtps2qxQPqIT7mJx8l30KGMG9mX5AOrdwwH8Mu_zZBOt5c6YgaqV7O_3RYWPFH0pOmDDlWq9rSSwPRjg_FT1YIxcBjYsTKb6dojZTJvtwOfuOfR0kj5WAiDTWW1Xm1kWYpRAiluhcUWnJtb8OdoyjlGXoiA0pOnqv-BzZFVbfC7sArTX0nQsH8T1tc1rQiQ_qBjPKsMaRNDlFr_Msvh5Ts2BfTUjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ترامپ به نشست دوشنبه ایران و کشورهای خلیج فارس: برایم اهمیتی ندارد
خبرنگار: نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
ترامپ: برایم اهمیتی ندارد. این به خودشان مربوط است. ما در نهایت از آنجا خارج خواهیم شد. مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23011" target="_blank">📅 17:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab990d240.mp4?token=eAtEBMqUxCt4dI5WQCUQsfWmeHOyR4Y2n7d6bya4N4C110Sy8g8ynRCmKAa4OsbrmTCoth-FpqFNBmkLppMGOZ6FJtay_PH_4THVc4zV7llE9rQD7OIuzpu6ZohUEhjXf9KGBUMERv1eYE3sfst27f4PYUabkroJLSEv0AwwWfG6z2H8_gSHuUWHn_tqwiQj-aqgQReGfu1haeapmY_uxhu6FzD_4PEXqo15-8eMVwSwH30fGiY-B4jnAMFp9RUAEvscnWh1k-fdAXzUpaGJNhWo9Cc-_hE8xXqPIUqhrWUWh1H-Ye_Vfl3TRsRvvn7AWLwe-fSS-A6rSllbaeyC7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab990d240.mp4?token=eAtEBMqUxCt4dI5WQCUQsfWmeHOyR4Y2n7d6bya4N4C110Sy8g8ynRCmKAa4OsbrmTCoth-FpqFNBmkLppMGOZ6FJtay_PH_4THVc4zV7llE9rQD7OIuzpu6ZohUEhjXf9KGBUMERv1eYE3sfst27f4PYUabkroJLSEv0AwwWfG6z2H8_gSHuUWHn_tqwiQj-aqgQReGfu1haeapmY_uxhu6FzD_4PEXqo15-8eMVwSwH30fGiY-B4jnAMFp9RUAEvscnWh1k-fdAXzUpaGJNhWo9Cc-_hE8xXqPIUqhrWUWh1H-Ye_Vfl3TRsRvvn7AWLwe-fSS-A6rSllbaeyC7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات رئیس‌جمهور ترامپ درباره ایران:
ما در نهایت خارج خواهیم شد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23010" target="_blank">📅 17:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش ۲ انفجار مهیب از تنگه هرمز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23009" target="_blank">📅 17:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: جنگ با ايران قبل از انتخابات میان‌دوره‌ای یا بلافاصله بعد از آن به پایان خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23008" target="_blank">📅 16:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: ایران می‌خواهد به هر قیمتی توافق کند، اما من توافقی را که بی‌نقص نباشد امضا نمی‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23007" target="_blank">📅 16:47 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
