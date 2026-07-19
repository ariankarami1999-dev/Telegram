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
<img src="https://cdn4.telesco.pe/file/RcNWJov13IRwYWKvNLtkRKXmHoK2PuJsOyDHUXwV5gJejWWv8cEh3hw-UE5p36v6HCnSH7Ozv7imNkbGJWIfvnMa-3Q2gmZI4eKURg42ZCzKTTKBaYa67edaOxHbZpI9IrrIYLDEsvd-kQ9Fa-f0CrpVtC-X2kxBYR10anlhBftsW3H1UweAdv8XumWhg3-1KaytA4llOoz2L3P_MG4bPMBR0g0fn_un0hoAjRa14T_xIziJ0EDvFzOLgdoifsGvRhG-4JyN88-YlFYXslv20CI5mcB2cHSxHqFUIEJpra9977P7wvazA0n82IKR0ePuLlNByLFR_nNsIrGSyNH4aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 412K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 22:23:10</div>
<hr>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: من دوست دارم تقریباً یک ماه را مثل مسی و رونالدو زندگی کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/18911" target="_blank">📅 22:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx30befmObJdreesUqdX4LKvDcGwqgKEVDkAfbSpsT6NsrWHxB-1lM9xt8Th1TLav6NcsWoxwFJkUJrCkINRBoTOtlzU46p0Kx-qWTrM7CCiI3L5appSJiEX_PtFbo9opzGy2C9plgVi2WuiQSnS4nXGcwz1Je4E-RpzplB1JgXBRaZu9QCtLMqGoBKOlTDMgHXW7HTWM2KKLH5cHoxzyHcQRTrSrSoE2_VtLgboafZZBJfXirdxaGr402cPGgoFZcss0v-nkP0IAvCQVX3UE7kBhRJuM2m2eAmf5HPrKiBa0yoKe7cNLUEstzwQR-fuwsxwx_CQ2q-x0FmqCFLf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ضرب الاجل هفتاد و دو ساعته محسن کج بند تمام میشود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/18910" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در مصاحبه‌ای با روزنامه نیویورک‌پست در دفاع از کشته شدگان جنگ با ایران گفت : آیا تا به حال از خود پرسیده‌اید که چند نفر در ویتنام جان خود را از دست دادند؟ آیا تا به حال از خود پرسیده‌اید که چند نفر در یک روز در افغانستان جان خود را از دست دادند؟ در یک روز، تحت رهبری جو بایدن.
ما در مورد دو جنگ صحبت می‌کنیم: ونزوئلا و این جنگ با ایران. این موضوع شرم‌آور است، اما در این مورد، آن‌ها جان خود را از دست دادند زیرا نمی‌خواهند ایران سلاح هسته‌ای داشته باشد و نمی‌خواهند شاهد نابودی خاورمیانه باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/18909" target="_blank">📅 22:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرگزاری CBS: جمهوری اسلامی ایران به حملات در روز دوشنبه ادامه میدهد تا قیمت نفت بیشتر بالا برود و ترامپ تحت فشار قرار گیرد
@WarRoom</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/18908" target="_blank">📅 22:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیویورک‌تایمز
:
دسته جدیدی از جنگنده‌های f-16 و f-35 از پایگاه‌های اروپا در راه خاورمیانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/18907" target="_blank">📅 21:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">منابع به فاکس نیوز گفتند ، امریکا میخواهد در نبرد زمینی بزرگ ترین جزیره خاورمیانه که «قشم» است را تصرف کند و سپس لارک و هرمز و خارگو ابوموسی را تصرف کند
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/18906" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ادعای شبکه کان اسرائیل:  در حال حاضر، ایالات متحده می‌خواهد اسرائیل را از دور جدید تشدید تنش‌ها دور نگه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/18905" target="_blank">📅 21:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بر اساس گزارش ها ترامپ به رهبران کشور های عربی اعلام کرده است برای جنگ با ایران در هفته جاری آماده شوند. @WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/18904" target="_blank">📅 21:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بر اساس گزارش ها ترامپ به رهبران کشور های عربی اعلام کرده است برای جنگ با ایران در هفته جاری آماده شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/18903" target="_blank">📅 21:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شبکه کان به نقل از مقامات ارشد اسرائیلی: ترکیه تهدید کرده بود که در صورت حمله نیروهای کرد به خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/18902" target="_blank">📅 21:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ارتش کویت: حملات جدید رژیم ایران تأسیسات متعلق به وزارت برق و آب را هدف قرار داد و باعث آتش‌سوزی و خسارات قابل توجهی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/18901" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجار در کویت
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/18900" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری i24 : اسرائیل تنها در صورتی به چرخه کنونی حملات آمریکا و ایران خواهد پیوست که باور داشته باشد ایران قصد حمله دارد، یا اینکه رئیس‌جمهور ترامپ به‌طور رسمی از تل‌آویو درخواست مشارکت کند
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/18899" target="_blank">📅 21:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18898">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شبکه 13 اسرائیل به نقل از یک مقام آمریکایی گزارش داد :  احتمال موافقت ما با این پیشنهاد بسیار کم است. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/18898" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شبکه 13 اسرائیل به نقل از یک مقام آمریکایی گزارش داد :
احتمال موافقت ما با این پیشنهاد بسیار کم است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/18897" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جزئیات اولیه از پیشنهاد قطر برای برقراری آتش بس۱۰ روزه :
1
- پایان جنگ و برقراری آتش بس
2
- تنگه هرمز تحت کنترل ایران به مدت ۱۰ روز باز شود
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/18896" target="_blank">📅 20:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18895">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18895" target="_blank">📅 20:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18894">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ایالات متحده به مقامات رسمی کشورهای حاشیه خلیج فارس گفته :صبر کنید. این ماه، ایران دیگر تهدیدی برای کشورهای خلیج فارس و جهان نخواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18894" target="_blank">📅 20:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18893">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال 14 عبری: ایران در تلاش است تا با یک عملیات زمینی، پایگاه‌های آمریکایی در کویت را مورد حمله قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18893" target="_blank">📅 20:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18892">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارتش اسرائیل (IDF): کمی پیش، نیروی هوایی اسرائیل یک پهپاد را در منطقه مرز اسرائیل/سوریه رهگیری کرد. منشأ پرتاب در حال بررسی است. سیگنال‌های هشدار طبق پروتکل صادر شد. @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18892" target="_blank">📅 20:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارتش اسرائیل (IDF): کمی پیش، نیروی هوایی اسرائیل یک پهپاد را در منطقه مرز اسرائیل/سوریه رهگیری کرد.
منشأ پرتاب در حال بررسی است.
سیگنال‌های هشدار طبق پروتکل صادر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18891" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927e9308c6.mp4?token=O53bkJ6rGIbnqxpeVtU1G8tRWCP839y7_-aOQHmVTg8sBOGOSOTl1dswAxbeKYJLNeYIZykvAUKwVwWWqr6qMam6RAVRcJwWdD_3C1-Nq9uP9B1QY_cIe6-ucmkmHJpFOof07XI1sSPNyEQhClPi3IwTTgAUV2Snqyk-QRzlt6_P-fE92Ki9WrcwUrlWCyLTdkCI6TwU5q5TPKSdrf85L-N30YxywaHCTRhnMgKuza9Ul1GsO_c8ip4W0wKgBtSPOofZF38CnwaYhIsNheM12TyQvcUEiYO6byqJqNhCykgAoQgrzomd0OzUMsjsBjJFQoN9aPMjzxXWB6gmY5VgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927e9308c6.mp4?token=O53bkJ6rGIbnqxpeVtU1G8tRWCP839y7_-aOQHmVTg8sBOGOSOTl1dswAxbeKYJLNeYIZykvAUKwVwWWqr6qMam6RAVRcJwWdD_3C1-Nq9uP9B1QY_cIe6-ucmkmHJpFOof07XI1sSPNyEQhClPi3IwTTgAUV2Snqyk-QRzlt6_P-fE92Ki9WrcwUrlWCyLTdkCI6TwU5q5TPKSdrf85L-N30YxywaHCTRhnMgKuza9Ul1GsO_c8ip4W0wKgBtSPOofZF38CnwaYhIsNheM12TyQvcUEiYO6byqJqNhCykgAoQgrzomd0OzUMsjsBjJFQoN9aPMjzxXWB6gmY5VgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانوک : مدرنیته شوک و اخلاق سگ میخواهد !
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18890" target="_blank">📅 19:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18888">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار جان از بالا سرمون پهباد شاهد رد شد به سمت کردستان میرفت احتمالن
صدای موتور گازی میده
ما زنجانیم
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18888" target="_blank">📅 19:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18887">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک نیروگاه برق در کویت هدف قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18887" target="_blank">📅 18:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18886">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
در ادامه شلیک‌هایی که به سمت اردن انجام شد، تعدادی موشک رهگیر به سمت تکه‌های موشک شلیک شدند تا احتمال سقوط ترکش‌ها در خاک اسرائیل منتفی شود.
در نتیجه،
تکه‌های موشک رهگیر در یک منطقه باز نزدیک شهر ایلات سقوط کردند، اما هیچ خسارتی وارد نشد و هیچ مجروحی وجود نداشت.
طبق سیاست‌های جاری، هیچ هشداری صادر نشد و این حادثه به پایان رسید.
هیچ تغییری در دستورالعمل‌های ستاد دفاع غیرنظامی اعمال نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18886" target="_blank">📅 18:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18885">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرمانده پلیس آبادان، ایران: صدای انفجار شنیده شده در آبادان مربوط به عملیات نیروهای مسلح ایران است و هیچ گزارشی مبنی بر حمله یا اصابت موشک آمریکایی در این منطقه وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18885" target="_blank">📅 18:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18884">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18884" target="_blank">📅 18:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18883">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb62a2aa1d.mp4?token=f_jOJs-WrKrX9kPG_WnzRLHQtzXFJiaJVVcXRtqkA25FJwLKI1GcQ04rrfl8xnhgNOHzsWzmAkxbPW0z8FLUEXmQ4k4kfihN8anhHB75GKIUz8YPAWQXRxWKp1Io12lp13GoSi5ugTvl6DbAheHxjzondZyfoUWU1qq0u1GN2sVNhVypBNCS1c6wuipP0vNOPVDVewahEIrBgF9t83oJiYPLsvHfYJmxsiT2TsruM4zFc79MxdA9homdm_JVICfYGZoY3x97I3gjQzoWLwRCyQzJP2NAFSGVnsvdC72vLkRGARZsRJGEz0wRi_oQ58_bWS4K8e-mlnBStAEQP5lxTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb62a2aa1d.mp4?token=f_jOJs-WrKrX9kPG_WnzRLHQtzXFJiaJVVcXRtqkA25FJwLKI1GcQ04rrfl8xnhgNOHzsWzmAkxbPW0z8FLUEXmQ4k4kfihN8anhHB75GKIUz8YPAWQXRxWKp1Io12lp13GoSi5ugTvl6DbAheHxjzondZyfoUWU1qq0u1GN2sVNhVypBNCS1c6wuipP0vNOPVDVewahEIrBgF9t83oJiYPLsvHfYJmxsiT2TsruM4zFc79MxdA9homdm_JVICfYGZoY3x97I3gjQzoWLwRCyQzJP2NAFSGVnsvdC72vLkRGARZsRJGEz0wRi_oQ58_bWS4K8e-mlnBStAEQP5lxTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه I24NEWS: چند هفته پس از ترور رهبر سابق جمهوری اسلامی ایران، یک گروه تحت فرمان سپاه پاسداران در امریکا، قصد ترور پسر بنیامین نتانیاهو، به نام یایر نتانیاهو را در خانه‌اش در میامی، فلوریدا، داشت.
با این حال شین بت این توطئه را در آخرین لحظه طی درگیری در پارکینگ اپارتمان وی خنثی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18883" target="_blank">📅 18:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18882">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو مصاحبه‌ای که قرار بود امروز با شبکه فاکس نیوز داشته باشه رو به دلیل شرایط اضطراری لغو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18882" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18881">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb30b2010.mp4?token=ivPg2czr1nAZtUjCwyVT6hIR76sh9UQCvQ9P_GH2Mr265KvlLS-3Te-7GfwSmBVbF7lWz4zb9ri_WjUWtUdfScKiztCpXSok4Rx611robH1N5QBcHClYSDLEqQ0a2gyklz3Awx8YM8zLImgl6nlSBBQ1206OWJb9qx_154LTokujh2f-NT5ZOm7W-gZUvhbA6GSFWBlGT-jlJ1V_XMCF-LpWxhpbC4ioQMRlMyXK2-cf0dzDz_1ahlE11IC0WmesjesFcwtmGBT5lnPOlbdW9eERrWp9yTBNOF4mLuX3yNt8cMj5SMX2h-iUBK1AZiEzEKRMKzhoH0p8Old-rA-LMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb30b2010.mp4?token=ivPg2czr1nAZtUjCwyVT6hIR76sh9UQCvQ9P_GH2Mr265KvlLS-3Te-7GfwSmBVbF7lWz4zb9ri_WjUWtUdfScKiztCpXSok4Rx611robH1N5QBcHClYSDLEqQ0a2gyklz3Awx8YM8zLImgl6nlSBBQ1206OWJb9qx_154LTokujh2f-NT5ZOm7W-gZUvhbA6GSFWBlGT-jlJ1V_XMCF-LpWxhpbC4ioQMRlMyXK2-cf0dzDz_1ahlE11IC0WmesjesFcwtmGBT5lnPOlbdW9eERrWp9yTBNOF4mLuX3yNt8cMj5SMX2h-iUBK1AZiEzEKRMKzhoH0p8Old-rA-LMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام
:
ملوانان در حال آماده‌سازی جنگنده‌های پنهان‌کار F-35B نیروی تفنگداران دریایی امریکا برای برخاستن (تیک‌آف) از عرشه کشتی جنگی "یو‌اس‌اس باکسر" (USS Boxer - LHD 4) در حین عبور از دریای عرب هستند.
ناو باکسر، کشتی فرماندهیِ گروه آماده خاکی‌خاکی باکسر  یازدهمین واحد اعزامی تفنگداران دریایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18881" target="_blank">📅 18:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18880">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee9644417.mp4?token=OgamqHUA7XTAwfu0SV5BwJwfLT5tYkV3bK-_1jtRu9bwvAKZF_sLSmmfDUJbkLupEYhQrBHzzRUrsMgbGt0QM-zMqh-uziJeFRb0jYlcZa71JVCghnacVp4IMeEtoVs_xFHqW-lMlflAsFQb80netEOpIJ596dkaeTGApHdoaTreIB4b5WLiQn2ZibzMJa3iM1hMSFBkIVuHOtw8t0K7kAnnDQCeIOq2Uj9GggkyJScDLeDhUaDqlNIilEYqHnyAoF3hKPAJ4Va2JQ0Bo2pUkRCZXtkH8NVqpbuNPKIstqr0iRAPQIFmCbml9WDsrMNA21DnRdkPr0ygLmbzcdHtfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee9644417.mp4?token=OgamqHUA7XTAwfu0SV5BwJwfLT5tYkV3bK-_1jtRu9bwvAKZF_sLSmmfDUJbkLupEYhQrBHzzRUrsMgbGt0QM-zMqh-uziJeFRb0jYlcZa71JVCghnacVp4IMeEtoVs_xFHqW-lMlflAsFQb80netEOpIJ596dkaeTGApHdoaTreIB4b5WLiQn2ZibzMJa3iM1hMSFBkIVuHOtw8t0K7kAnnDQCeIOq2Uj9GggkyJScDLeDhUaDqlNIilEYqHnyAoF3hKPAJ4Va2JQ0Bo2pUkRCZXtkH8NVqpbuNPKIstqr0iRAPQIFmCbml9WDsrMNA21DnRdkPr0ygLmbzcdHtfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از سخنگوی قرارگاه کلش آف کلنز منتشر شد:
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18880" target="_blank">📅 18:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مهر:
معاون امنیتی استاندار خوزستان گفت که مکانی نزدیک به شهر آبادان لحظاتی پیش توسط حمله موشکی متعلق به آمریکا هدف قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18879" target="_blank">📅 17:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18877">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18877" target="_blank">📅 17:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18876">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز: حملات حوثی‌ها و ایران به عربستان پاکستان را به شدت از تهران خشمگین کرده و ممکن است پاکستان به درگیری عربستان و یمن کشیده شود
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18876" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18875">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سقوط بقایای موشک در اسرائیل  @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18875" target="_blank">📅 17:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18874">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حمله جدید اسرائیل به جنوب لبنان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18874" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18873">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دو انفجار سنگین بندر عباس
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18873" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18872">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9kTc_kR68FLVIX9Id5c4xH-OJV_moKeznyRpc5OBPl9N4upSFiMp-sfAnwRREKJKNh7DV9xm8Q9RPAj7zmaaQuWGDEXDRwOBy04c76DtPmijBb1t1w7hTAe9Lpx-5HrpamgsZhvlLgKTjREYsnQxMKlRyQe-NatSX1RmZfyBkEst6oQ_E6JUEMEljlk_WNLNsepHiv7bnFjC9-eXMwTYismqcR0lwjIsNGxCkVKkx6ffwMilCxLV4SgdTm6rsaQaur-BsgANwKVZPyi57IWBFHnRrDQXwdL8iDj9eXDcpIs1NpdhmaSwL3ErBVMu3MTiS8Rf4xmxFjCX8H-mT-jaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : وصله‌کاری موشکی؛ نشانه‌های فرسودگی و کمبود در زرادخانه جمهوری اسلامی؛ کفگیر سدمجید به ته دیگ خورده است؟
‏تصاویر منتشرشده از یک موشک و پرتابگر غیرمتعارف، نشانه‌هایی از فشار بر زنجیره تولید موشکی جمهوری اسلامی را آشکار می‌کند. بوستری بدون رنگ‌آمیزی و با ظاهری متفاوت دیده می‌شود که به نظر می‌رسد با کلاهک یا بخش فوقانی موشکی از نمونه‌ای دیگر مونتاژ شده باشد. پرتابگر نیز ساختاری ساده، کارگاهی و به‌مراتب ابتدایی‌تر از لانچرهای استاندارد دارد.
‏
این ترکیب نامتعارف می‌تواند نشانه استفاده اضطراری از قطعات موجود، کمبود بوستر و لانچر، یا مونتاژ ترکیبی برای حفظ توان پرتاب باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18872" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18871">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPete Hegseth🇺🇲</strong></div>
<div class="tg-text">آبادان صدای یدونه انفجار اومد
خونه ها لرزید</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18871" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش صدای انفجار آبادان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18870" target="_blank">📅 16:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bql1IpMLlK0iVp7fWHmbs-1HBPkOtQEbGWzuxao9wWK3W0I0rpBZPivYoF-n5_SWZzREiaCDqKG2x-lMQUCN6-g85o1KUZBCvlgso2r4EY9m-A1zWbMvGpzWTGHDUL6oBpTVbaKKIHUueEn3n11qqZQXt8LTXWwGFob92eTN_GbahAoiK-0vouVHpgqJSQW2zskN4SfeVH5C3iTJuXOlAbibp4t0_M0HzlHB4UFhTZJ2tFyy4AZNHFZPzCRHXLEmIiDjoEmTXBpxX91CcqHfxa_jjYNXFDd-AL6V-JNsyL_pPvvoN0ZbQQTazYfV_lWGrDlCXeZOxEW4ptt70FYoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشات میگن ، فرندلی فایر شده ، پدافند خودشون  موشک خودشون رو زده یا موشک خودش ترکیده
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18869" target="_blank">📅 16:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چند فروند بمب‌افکن رادارگریز B-2 آمریکا تو روزهای اخیر در حال جابه‌جایی دیده شدن و به نظر میرسه دارن برای مأموریت‌های احتمالی علیه ایران آماده میشن.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18868" target="_blank">📅 16:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18867">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚠️
کرمانشاه صدای‌ انفجار نیست پرتاب موشکه
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18867" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پرتاب موشک از کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18866" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">طبق گزارش ها،اسرائیل ممکن است در 24 تا 48 ساعت آینده،ارتباطات رادیویی خود را به دلیل تنش قریب‌الوقوع با ایران قطع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18865" target="_blank">📅 16:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18864">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شبکه ۱۳ اسرائیل: تخلیه هواپیماهای سوخت‌رسان آمریکایی از فرودگاه رامون پس از هدف قرار گرفتن عقبه اردن
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18864" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18863">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هم اکنون 14 هواپیمای سوخت رسان آمریکایی از اروپا به سمت اسرائیل اعزام شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18863" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18862">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رادیو ارتش اسرائیل:
سیستم‌های دفاعی آمریکایی دو موشک ایرانی را در منطقه العقبه رهگیری کردند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18862" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18861">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlwTnEzZqxA2HmpSK4A5Q19AaCP5yIk-NaQez3cWg1fd8iJvSWgHYaXekai5fVFDWOAJiXgE2MmxEo8lrcKBuboeKRfyyufsyA6L95OjG7cedmE1uLKoGcCJuD0wMZ4bPjPP5nRftvy08pumO6PGkG4jDL8mR3Lmq4REtnawrBiDiwOCkW3BBPEanXkIBpyrMzPmT1uzMWpARl4DvYBkUxmV27Q1FP9yZppFY26Kwm8dChOMIFaylgw3nAhLT4b0FOrn4PSYmP6hvexq9jKQvHu4BelaVzrbe1m7ZbQRAhub4AXRoJR8lUovh6NCFIfE5TBYHaeSn0c9-dABfId0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی در انبار گرانول مراغه… @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18861" target="_blank">📅 16:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18860">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIXqywgwM0VrISncvwWWVFI0jkNPABoCNhh_6T4doqwEJr0jFxLaMuD29jPnXXXr4yRyEUdHuC24RTBNzGdpg0IBgVRLjE7MvlMLrGM6E4vakF2gVARMbNasmyVvOxaaJU__IR3ErJuCCYerQehWZd61toGKyuwklYrmK1B9zjkktg4Wx-g0ahuwUXNBqvDoVDQki6FAxZD5-rPSUi_H1Tc3Crk-oeqX6dTGfF2BpKNLR1BkEsIuNUVbpGWTuRLdwMZWYOajcJbb4VvEF16w1pnx_ng26xEhwoIv9WhQKhKdJ9YV0i7z_IHMAELuL_I-uPzPTfObDbZJCGRONs7GhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از کوهدشت ، لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18860" target="_blank">📅 16:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18859">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e80cb396.mp4?token=Sru_V9I4OgecwZRC5zlDyS0FGIfvOmEySjpPQGb_ZHJLXJUE7rr84U92acGjQIX6k53ilZH1Wnh1UjmoM4TQaDZrZg094dt5obkTkmH41nMd9jeh65nYc4qqhIqmdN9UYvMBf7pO6MLilS2ouB2FXDqLuDddH5oGkLarawW3yn4T-DKOofVOKqpFxNQOz14Mw-b_B21VWlIOJbUSDenM_njuV-ysI-CGltnAf3Hby7nn5iSlah41r-Nc4zToJx044hupCgIn70lbHDEWLVRLXvB2-ejpkIKrWrL7VYwkTBKf2mexqOlwlB3bNqcCbJNqIpm4plTYaeAMSdNQ9KP5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e80cb396.mp4?token=Sru_V9I4OgecwZRC5zlDyS0FGIfvOmEySjpPQGb_ZHJLXJUE7rr84U92acGjQIX6k53ilZH1Wnh1UjmoM4TQaDZrZg094dt5obkTkmH41nMd9jeh65nYc4qqhIqmdN9UYvMBf7pO6MLilS2ouB2FXDqLuDddH5oGkLarawW3yn4T-DKOofVOKqpFxNQOz14Mw-b_B21VWlIOJbUSDenM_njuV-ysI-CGltnAf3Hby7nn5iSlah41r-Nc4zToJx044hupCgIn70lbHDEWLVRLXvB2-ejpkIKrWrL7VYwkTBKf2mexqOlwlB3bNqcCbJNqIpm4plTYaeAMSdNQ9KP5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط بقایای موشک در اسرائیل
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18859" target="_blank">📅 16:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18858">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqjMPHWaVem3NZXL3Mn2h0WY_jkxM0HYobZjJcgasg653QvZFLuxIqOvzP0lQaIln5VS_Ilr1pQFHr12WDuJ38T5qTV8ytcJwt2HrsXg1xoa0r-Mgw-V37G44U1yjfNl9k5HWilUydc-GZ7R5imaj5v3a6YIFNvOVuaIK0i6GHzEdtvBMYUq2LiKzSZcl4wVAkINIo7JKa2XuITxb6_r-Jp0UmKqtfpYgjozqb1x12nbvb2SjSV2JcpMhsu1o1crYaMU-WgPILbBRsdbruq2qF4isAk1E7iRuued3FG4BYEtmpWEhgHroTzVoqwdO7jipsS7poSguajRSmoAvbfF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از ایلام ، لرستان
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18858" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18857">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش اسرائیل: چند لحظه پیش، ارتش اسرائیل پرتاب موشک‌هایی را از ایران به سمت شهر عقبه در اردن، که مجاور اسرائیل است، شناسایی کرد.
احتمال وجود دارد که در نتیجه این حملات، خساراتی به اراضی اسرائیل نیز وارد شود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18857" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آکسیوس: آماده‌باش هوایی آمریکا برای تشدید جنگ با ایران آغاز شده است
آمریکا تعداد سوخت‌رسان‌های خود را به سطح مشابه آغاز جنگ خواهد رساند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18856" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj_8nQ1X9Zgjw2IYHDdJwD3tXaPglg-ETafPlRqphp7wH4gX7IIMvKqbcYNNbyVQ7Ib8khwsI91uX3zMaAQkmrNDZN6OjqHAzdX131i_IKpVsA03Vri3JYrL9OrBabrc6gmRHx4hcteYBFfrDNu199GFrCSEKSTWU9iSVusjX1UGWYU01jv11JVTp2sAY7BHT6zSgxiNL7pgl35BA_-qPsj0cNqWqPBQrRRsbiZwYdi1oYYqZ7DvOYz7NhROPysWd1FCJ4zGiVqK4wgbVbBXVsnaWOxG-E18Ce_5bAcUBQu8jvshS9RzR3e2-ubdzJ7enlvpYkk61Ubeo21sw8C95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این کاری بود که لیندسی می‌خواست انجام دهد و قرار بود اتفاق بیفتد. مهم!!!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18855" target="_blank">📅 15:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770115730a.mp4?token=lBMui_ajFdPNGjrRZt4WNFt7rsLfNQH_gBpgZf6wKPeHD4hSREoXKcD6DS48p5oeF-2iXKgMNAAiXb2eJRoFZehODj3xbwfoTbA5_xk1v8fa0N3Qb7xiHAaYJs-0pEt6a4FYg0coQOOZlE17cVY1AYKJDIqgIuKzOVem_IFnaMjS1CdL7QVUA3nIsZ8ZETtCtbupKK1VKaoW6aDv2-tve3D4ZyyYSWGR8uz7Wws7yKQXBXw8hyZTgT9DHbAsJKeyVO9vUUbLAPA6OjPOURz0RSimtwP7932YLrLFLkU0HGij89hsEYYEBpkvH8_giv300V0V0LKarEOSZNdkY1zJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770115730a.mp4?token=lBMui_ajFdPNGjrRZt4WNFt7rsLfNQH_gBpgZf6wKPeHD4hSREoXKcD6DS48p5oeF-2iXKgMNAAiXb2eJRoFZehODj3xbwfoTbA5_xk1v8fa0N3Qb7xiHAaYJs-0pEt6a4FYg0coQOOZlE17cVY1AYKJDIqgIuKzOVem_IFnaMjS1CdL7QVUA3nIsZ8ZETtCtbupKK1VKaoW6aDv2-tve3D4ZyyYSWGR8uz7Wws7yKQXBXw8hyZTgT9DHbAsJKeyVO9vUUbLAPA6OjPOURz0RSimtwP7932YLrLFLkU0HGij89hsEYYEBpkvH8_giv300V0V0LKarEOSZNdkY1zJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی
در
انبار گرانول مراغه
…
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18854" target="_blank">📅 15:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USjGU0PQVAxZyXuNWAsKG0_7drT21x19hMFyPg5QJAPqwvUL6-0-PZ9BilCzHw1LrNjjdXpURNfTpb_p-bnyLytRTfz5rCMcXdqpjIAL3D0SIqnnZe0qnQ9mxJpjBbxsgTNIs7wYxH2_-6F_ajVv2LQZd81tZiJvFX3fOkR4qwiIa_Ay97FXWKIfv2kioGzmZ6_fC0QHDA5fsRWV2Szf8neRFGbmwnl0DO6yuVi-IljJ3TQSHjFxx_cHFJazbBKk9aNyWHxh6bIUGk267a9yYPzhhfdHUlklNBrvFM7-v5gNnoFIAOusQu3CPbI6sgFOOcQS1XxjvIL7YSDkrET_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهروند ایرانی/آمریکایی ممنوع خروج شده که ترامپ اداعی آزادی و رژیم تکذیب کرد با نام دنا کراری بعد از 566 روز به آمریکا رسید
کراری، ۵۳ ساله ساکن کالیفرنیا، برای دیدار با خانواده به شیراز سفر کرده بود که گذرنامه‌اش توسط مقامات جمهوری اسلامی ضبط و از امکان خروج از کشور محروم شد. به گفته وکیلش، او هرگز رسماً زندانی نشد، اما تحت بازجویی‌های شدید و مکرر توسط سازمان‌های امنیتی قرار گرفت و در چند ماه گذشته تحت شرایط بسیار محدودکننده‌ای قرار گرفت.مقامات امنیتی کراری را به «همکاری با یک کشور متخاصم» و «جاسوسی» متهم کرده‌بودند
وی به عنوان کارمند در شرکت امنیت سایبری پالو آلتو نتورکز کار می‌کرد. او در کنار حرفه فنی خود، بنیانگذار یک سازمان خیریه حمایت از کودکان محروم بنام فرزندان مهر را نیز مدیریت می‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18853" target="_blank">📅 15:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYDLsaCecx3G6eh70xzeUR5NKUY-foj8hdKsvY8hgzW985bpkUQAzmV5nFkMXsJyUGgxO2B7NivcJL5i5VDmUo_iC88FRyDMk7jsv9UxMttSvS7VGWIumLIfEuAsICJPr1yHMtFd9BErMiAGsUwh92fhZzUCuk70gceVHPwRBZxviWihd5igtcpKcTKMDmBBousMWrX9ShKmk9ABP8-C8nXNBbM6MJ-G2yUU24yEeWO53HtvLJrtpLamdWLRCnB8DOSxE9sl9fW5QB32phCY4L3Z1QOYQ88Z-ckOI3ieCgsIk7yLPovNuRv5Eb74AG5OulvApLEX7Z-ErfBZOVUO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه هسته‌ای شهر دارخوین با نام های(کارون یا استقلال) در استان خوزستان، در ساحل رود کارون و حدود ۷۰ کیلومتری جنوب اهواز، در زمینی حدود
۵۰ هکتار
در حال ساخت است. این نیروگاه یک راکتور آب سبک تحت فشار (PWR) با ظرفیت حدود
۳۰۰ مگاوات
دارد که طراحی آن توسط متخصصان ایرانی انجام شده و ساخت آن توسط
شرکت
انرژی اتمی ایران
با مشارکت
گروه مپنا
و شرکت‌های داخلی دنبال می‌شود. عملیات اجرایی آن از
آذر ۱۴۰۱
آغاز شده، هزینه پروژه حدود
۲ میلیارد دلار
برآورد می‌شود و طبق برنامه قرار بود طی
۸ سال
حدود
سال ۲۰۳۰
تکمیل شود. این سایت زمان شاه نیز قرار بود میزبان دو راکتور ساخت شرکت فرانسوی
Framatome
باشد، اما آن طرح متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18852" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سازمان انرژی اتمی ایران: ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18851" target="_blank">📅 14:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سازمان انرژی اتمی ایران: ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18850" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مجری : دست فرمون شما ما رو رسوند به جنگ  خلاصه گفتگو با سید عباس عراقچی  @WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18849" target="_blank">📅 13:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نیروی دریایی سپاه: ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه، قصد ایجاد اختلال در تردد و خروج از تنگه هرمز از طریق یک مسیر ناامن را داشتند. دو فروند از این کشتی‌ها دچار حادثه شده و متوقف شدند، در حالی که دو فروند دیگر از ادامه مسیر منصرف شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18848" target="_blank">📅 13:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اختلال در اینستاگرام / واتس آپ ، به گیرنده های خود دست نزنید مشکل از مرکز است
@WarRoom
⚠️
⚠️</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18847" target="_blank">📅 12:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش‌ تایید نشده ، 4 کشتی در بندر شهید رجایی، هدف حمله قرار گرفتن @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18846" target="_blank">📅 12:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش انفجار در اربیل عراق ، مقر کردها
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18845" target="_blank">📅 11:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش‌ تایید نشده ، 4 کشتی در بندر شهید رجایی، هدف حمله قرار گرفتن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18844" target="_blank">📅 11:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آلارم حمله موشکی در ‌بحرین فعال شد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18843" target="_blank">📅 11:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ادعای اسرائیل هیوم:مجتبی خامنه‌ای از ایران متواری شده  @WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18842" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ادعای اسرائیل هیوم:مجتبی خامنه‌ای از ایران متواری شده
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18841" target="_blank">📅 11:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نیویورک‌تایمز:دولت ترامپ نگران است که افراط در استفاده از تحریم‌ها علیه روسیه، کشورهای بیشتری را به روی گرداندن از دلار آمریکا ترغیب کند؛ در نتیجه اقدام به کاهش برخی از تحریم‌ها علیه مسکو کرده
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18840" target="_blank">📅 11:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0163277b0.mp4?token=SHae6Xqx6E2XvmH15koBzptrcfM0g8OVKPF_nZYu0UQUurhGvrbl-j-JhZ4sBY1pPKfYQFwSHOPmXG2sekd2PkgD2u-uJYESjLykDfsnJfnJk-QMMQQ_L60mlsGA3x0dwfxtYB2GEySSWi4SjvtMUWaxy0nSdDGYhtnPPyG2n9XmZeCErUCZkWW60hUUzhzUGbAU1GIp2aR7Sx4yzvh6oD8RnTFmRBrT7pdZpEVi4-TRNZOwOb_S_Ps7ZzoRIxxvNOoE6X2RHnP6Ha9StyetriDkewBPb8arhzVcPNIY-uuemzMJ3HosGTGwErl3rU6nYlsqXx-XHP58EHLAonho0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0163277b0.mp4?token=SHae6Xqx6E2XvmH15koBzptrcfM0g8OVKPF_nZYu0UQUurhGvrbl-j-JhZ4sBY1pPKfYQFwSHOPmXG2sekd2PkgD2u-uJYESjLykDfsnJfnJk-QMMQQ_L60mlsGA3x0dwfxtYB2GEySSWi4SjvtMUWaxy0nSdDGYhtnPPyG2n9XmZeCErUCZkWW60hUUzhzUGbAU1GIp2aR7Sx4yzvh6oD8RnTFmRBrT7pdZpEVi4-TRNZOwOb_S_Ps7ZzoRIxxvNOoE6X2RHnP6Ha9StyetriDkewBPb8arhzVcPNIY-uuemzMJ3HosGTGwErl3rU6nYlsqXx-XHP58EHLAonho0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رسانه‌ی فرانسوی با انتشار این ویدیو نوشت:
‏زنان ایرانی در نزدیکی بندرعباس در جنوب ایران گرد هم آمده‌اند تا خبر حملات هوایی جدید علیه رژیم اسلامی را جشن بگیرند.
‏آن‌ها پیام زیر را خطاب به آمریکا فریاد می‌زنند:
‏«ادامه بده. کارِت عالیه»
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18839" target="_blank">📅 11:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903Uro5PedrWTj6in_H1z4DNpsDpwZNoISpUOpXmpQMBYbysKQZPUb451MfoeJa978ZOyOW2Mx-f9WAh2o6X3cH1Wx2yVuvlxmuucHTMJX7JpXE4e9Wc6gi7c6umc03Y9kySQ_sskaBeCFB86iDZ15VZhGX_sveJbvAXJxOlZ62c_dyXbhAKIUxrRJyvZrcPbHaXjq3eerC3QNI8dwNmbRRwrzUHz8gCJCKKe3s_8pJZdLU1o_xD8creTc7XNOadU_tGA4DkJsiUYKVJmaHobdN8D_jGr7ifogjU63wPjROUGOAO6lmvlydVWg8MlxHDrhEP-o4qxEaK6xYgwUkmo_cFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903Uro5PedrWTj6in_H1z4DNpsDpwZNoISpUOpXmpQMBYbysKQZPUb451MfoeJa978ZOyOW2Mx-f9WAh2o6X3cH1Wx2yVuvlxmuucHTMJX7JpXE4e9Wc6gi7c6umc03Y9kySQ_sskaBeCFB86iDZ15VZhGX_sveJbvAXJxOlZ62c_dyXbhAKIUxrRJyvZrcPbHaXjq3eerC3QNI8dwNmbRRwrzUHz8gCJCKKe3s_8pJZdLU1o_xD8creTc7XNOadU_tGA4DkJsiUYKVJmaHobdN8D_jGr7ifogjU63wPjROUGOAO6lmvlydVWg8MlxHDrhEP-o4qxEaK6xYgwUkmo_cFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : دست فرمون شما ما رو رسوند به جنگ
خلاصه گفتگو با سید عباس عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18838" target="_blank">📅 11:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرماندار چابهار گفت: صدای انفجار شنیده‌شده امروز، ۲۸ تیرماه، در حوالی این شهر مربوط به عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده و هیچ خطری شهروندان را تهدید نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18837" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏ارتش جمهوری اسلامی با صدور بیانیه‌ای، مدعی حملات تازه به دو پایگاه نیروهای آمریکایی در کویت شد.
‏در این بیانیه آمده که ارتش جمهوری اسلامی در پی «حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی»، انبار مهمات ارتش آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش در پایگاه علی‌السالم کویت را، آماج حملات پهپاد‌های خود قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18836" target="_blank">📅 10:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیویورک پست از قول دونالد ترامپ: کشته شدن دو سرباز آمریکایی مایه تاسف است، اما ماموریت نظامی همچنان ضروری است
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18835" target="_blank">📅 10:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: اگر تهران متوقف نشود، منطقه ممکن است وارد یک درگیری گسترده‌تر شود
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18834" target="_blank">📅 09:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وال استریت ژورنال: بر اساس اظهارات افراد مطلع، در حمله ۱۷ ژوئیه ایران به پایگاه هوایی موفق السلطی، علاوه بر موارد دیگر، هواپیماها و پهپادها نیز آسیب دیدند
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18833" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRGxpY8a0e8xtwCP3AjuEUXzuQetNO3AciC5T1uA4R7azPLK3RmXECRZqUpLxDikp1fryupCZa3zLR4kHXqjLnqiRqHqQqTjGvoEbYFrbWSWZaNAbIammfB_1qUxVVfAo9DrPzkxIbe9yUvjKxmXuAd6xOXRcDQVH60oguJ2PBJXwHcpJxbinV7kZ39xAuX-QsPjbUli_lXlL9kpGjA3Y8Mi6YSB7X5DU7RlBHLDceWLbrds5_OaDP_Fsh8zh-9U5HkCbpRE9Wtm6JmqfQRE0TcqJy-Uv1-e4vU5f0JjTzW2JDtVTZe7LmUNSbELV19flRdE_Sksw2FYaUxwuXtQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله در دزفول و اهواز @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18832" target="_blank">📅 08:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">معاون امنیتی ‌استانداری خوزستان:
جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه نقاطی در اطراف شادگان را مورد اصابت موشک قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18831" target="_blank">📅 08:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سایت موشکی خمین ,کوه انگشت لیس , بین خمین و گلپایگان @WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18830" target="_blank">📅 08:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">زلزله در دزفول و اهواز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18829" target="_blank">📅 08:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95514648b.mp4?token=DtutvrTONkNtv5TP1TC-H_fg89SMpGTChuaQZup6vbfq2MzhG5p5rFUcvDNUBOp4BRsbbkSNfyhJxUf6l37gEbatatWB18UYCCmeuFoH5A3DqiQIwH19kE2r1ogFASF8F_eB0Ok3L9u7XgFwyU27AUBPtZi6Kr4l6vJygYQOqDtrKDXTU5PIDW8VEgCHczsSaS5xhP89pGXk4scIL82LUofNQVBFcvqMnJZEQJB3vwX7TgA_UIwGiseJMp1YEWh1rXrX9Vo7iLLkOucV-jC5gc1SkQU5kBoZ7e69ZBJuOIPXoX0wQKqezw6E5xC7MWamiVDrc7_X0SJkC1YjkOeUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95514648b.mp4?token=DtutvrTONkNtv5TP1TC-H_fg89SMpGTChuaQZup6vbfq2MzhG5p5rFUcvDNUBOp4BRsbbkSNfyhJxUf6l37gEbatatWB18UYCCmeuFoH5A3DqiQIwH19kE2r1ogFASF8F_eB0Ok3L9u7XgFwyU27AUBPtZi6Kr4l6vJygYQOqDtrKDXTU5PIDW8VEgCHczsSaS5xhP89pGXk4scIL82LUofNQVBFcvqMnJZEQJB3vwX7TgA_UIwGiseJMp1YEWh1rXrX9Vo7iLLkOucV-jC5gc1SkQU5kBoZ7e69ZBJuOIPXoX0wQKqezw6E5xC7MWamiVDrc7_X0SJkC1YjkOeUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :شب هشتم تمام شد
ما
دور تازه حملات علیه ایران
در
۱۸ ژوئیه، ساعت ۱۱:۳۰ شب به وقت شرق آمریکا (ET) (۰۷:۰۰ صبح ۱۹ ژوئیه به وقت تهران)
و
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)
به پایان رساندیم.
به گفته سنتکام، در
هشتمین شب متوالی
حملات آمریکا، نیروهای این فرماندهی
تأسیسات دیده‌بانی ساحلی و پدافند هوایی، توانمندی‌های دریایی، و انبارهای موشک و پهپاد ایران
را با موفقیت هدف قرار دادند تا توانمندی‌های نظامی ایران بیش از پیش تضعیف شود. همچنین نیروهای آمریکایی،
عناصر سپاه پاسداران
را که به گفته آمریکا در
۱۷ ژوئیه (۲۶ تیر)
در حملات علیه نیروهای آمریکایی در اردن مشارکت داشتند، هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/18828" target="_blank">📅 08:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=f73EZ3RZHjewHN9XGeiHuMIFYaUy-ODnEqaYreGx8UF3ZBeZV5SWw9OT68CnpRlW8M65bJp7Hfpx5wA2tcypt5lyEEMpA8HkXcRXUY5WtBtuSjJZpMe_ql6GwCx9VjP6zQymzk2Z4KsosstebaJ2X7gCvbSlpri6ik2n8I_N6w3GDr54LAsimp50BpMwlsKZzQdiLV00xKBVPnfGExiq53o0ExuKLQ6EXU7GknPoE-WSyw4RZWWtTGNjad3hE9HUdLuCQ4-KUn-rG-EkJjhZPbj8cp9cGOehudomXii4RXcKKKbR86-PH_9rS9-ufrPno6D22kU2HUac1ZyobNpOUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=f73EZ3RZHjewHN9XGeiHuMIFYaUy-ODnEqaYreGx8UF3ZBeZV5SWw9OT68CnpRlW8M65bJp7Hfpx5wA2tcypt5lyEEMpA8HkXcRXUY5WtBtuSjJZpMe_ql6GwCx9VjP6zQymzk2Z4KsosstebaJ2X7gCvbSlpri6ik2n8I_N6w3GDr54LAsimp50BpMwlsKZzQdiLV00xKBVPnfGExiq53o0ExuKLQ6EXU7GknPoE-WSyw4RZWWtTGNjad3hE9HUdLuCQ4-KUn-rG-EkJjhZPbj8cp9cGOehudomXii4RXcKKKbR86-PH_9rS9-ufrPno6D22kU2HUac1ZyobNpOUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش انفجار  در قشم
@WarRoo
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/18827" target="_blank">📅 05:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سکوت عجیبیه</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18826" target="_blank">📅 03:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سنتکام: امروز ساعت 6 عصر به وقت شرق آمریکا، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی رو علیه ایران آغاز کردن. هدف این حملات، تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب…</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/18825" target="_blank">📅 03:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جزیره لارک سایت سپاه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/18824" target="_blank">📅 03:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/18823" target="_blank">📅 02:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahrmECpqWhyZklpx_H4KgQL2xl3Y0_6P8zLHPWQoB-oJwobum-UxLB9LSF2iBMMn91cVsJ2-79-oz9navhbehrkzzQo4A_zaAAt2_Iv7ExwOch11C0jMFPKLT9VEC3852oxyvs24PArhKhff97v2PgO2ieiKT1nwaR1OKzflrnZ2SUbteqjgdjqjEnT9qwtLoaHoV9Cxf7-Ib2PUNAJgyMCTPNvkjpyBKcAwoETmpGdr7dOI2I69RC51StiKmfzrh2XVO1zPotxwrPW34N6lVE-B4cL0YCuuxHkwW4_DqVtf5OgW5p5o2VJdiSu5Bzv0CzEF4rw6w30sw7b7Ihnn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار جان الان امدم بالا پشت بوم جنوب تهران ستون دود بلند شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/withyashar/18822" target="_blank">📅 02:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از مدتها نمیتونم ببینیم چیزی
🤒
همه رفتن زیر پتو رررپتپتوووو  @WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/18821" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک صدایی شبیه به انفجار در کوه دراک شیراز که شهر موشکی هست شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18820" target="_blank">📅 02:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/18819" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش انفجار خرم آباد لرستان
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/18818" target="_blank">📅 02:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18817" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هیچ گزارشی از‌ بندر عباس نیست !
🚨
🚨</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18816" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش انفجار در بوشهر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18815" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش‌ انفجار در اراک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/18814" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18812">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18812" target="_blank">📅 02:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18811" target="_blank">📅 02:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18810">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/18810" target="_blank">📅 02:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18809" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
