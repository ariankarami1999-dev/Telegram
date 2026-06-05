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
<img src="https://cdn4.telesco.pe/file/vW5qaF4FzAEC_Fw2rxqskDyfH-buzcl70EUuCnBuT31Y5g4wPr46P2kRUMfiIqEvJGukFbkLjxrsLUygZFMgAhHKZvm84_LHg5dlHhWFdcfOcIDInkx_DYaHyCo2aFRnnfasowyps7HWjUt-IqroB2N8an1ugv9x7DDgs18O-L6jEOVrbsnJjbOyhkv0BGKwdkLMl_oVFS-xPj8-uPWoWt7ZntDSwttrz8JfTyDnqyABfUyDEnT43cxQnY9KxRi9y2wXZPdfoT3oskot3Ls1Lx8LF8L9qYgDiDBX182zLUwp7XXJSgFOkoVVXZXSk1F-7EQtKH4sPS_vf23a6thl1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 289K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-13560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند.
خط قرمز اردوغان: هیچ نیروی نظامی کردی در نزدیکی مرزهای ترکیه نباشد.
@withyashar</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/withyashar/13560" target="_blank">📅 20:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بلومبرگ: طبق داده‌های ناوبری، رفت‌وآمد کشتی‌ها از تنگه هرمز تو ۲۴ ساعت گذشته به‌شدت کم شده
@withyashar</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/withyashar/13559" target="_blank">📅 20:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">️حمام خون در بازار کریپتو!  بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است. @withyashar</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/withyashar/13558" target="_blank">📅 19:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آلمان با صدور هشدار امنیتی برای شهروندانش، نسبت به سفر به خاورمیانه هشدار داد و دلیل اون رو احتمال تشدید دوباره تنش‌ها و اختلال در پروازها عنوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/13557" target="_blank">📅 18:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سنتکام:
ادعای نادرست: ایران ادعا میکنه که به سمت کشتی‌های جنگی ایالات متحده در خلیج عمان تیر هشدار شلیک کرده و کشتی‌های آمریکایی رو مجبور به «عقب‌نشینی» به سمت اقیانوس هند کرده.
حقیقت: نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی ایالات متحده حمله نکرده یا به سمت آنها شلیک نکردن. انجام این کار نقض فاحش آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره مداوم علیه ایران رو به طور کامل اجرا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/13556" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gloria2018Remaster(IG @yashar)</div>
  <div class="tg-doc-extra">Umberto Tozzi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13555" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/13555" target="_blank">📅 17:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=iIiY1AUOy_ooaGFaW1i1t43kGrVo57rJdwaoHxhi5-sAzZ8CvdldFHhYiy0HAv0zGm8NABzYiLrkxYiIOOOv8numebuYghlXj36L1b_S3Zs4VP3gkI8m_vq3bISqiXv1sxjSIUpBnlm0gkLe4Z1PEBDXnvWSXy__8_xgoSeA8jXXC6FWBiosoYcRGGXSW7AaPg7MWISnlaHRTZL6p8hHtXTOkL5kn2P67VkWFPeqy-vgWXUYwcpVzn7IbBVvaFQ4zodOye7BzZPphvC2Y_WYIN0_-ss03oUHOT5GWYdk4v1RCwL1JotB7XkMPcM2AkXMvURdFVyP1WjorZywA2RQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=iIiY1AUOy_ooaGFaW1i1t43kGrVo57rJdwaoHxhi5-sAzZ8CvdldFHhYiy0HAv0zGm8NABzYiLrkxYiIOOOv8numebuYghlXj36L1b_S3Zs4VP3gkI8m_vq3bISqiXv1sxjSIUpBnlm0gkLe4Z1PEBDXnvWSXy__8_xgoSeA8jXXC6FWBiosoYcRGGXSW7AaPg7MWISnlaHRTZL6p8hHtXTOkL5kn2P67VkWFPeqy-vgWXUYwcpVzn7IbBVvaFQ4zodOye7BzZPphvC2Y_WYIN0_-ss03oUHOT5GWYdk4v1RCwL1JotB7XkMPcM2AkXMvURdFVyP1WjorZywA2RQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ویدئویی جدیدی در شبکه تروث منتشر کرد که در حال بازی گلف است و یک ضربه فوق‌العاده میزند. همچنین از آهنگ معروف گلوريا لذت میبرد.
یاشار: آخرین باری که این آهنگ ویرال شد در فیلم گرگ وال استریت بود. مضمون این آهنگ این است که
کنترل نکردن زندگی احساسی می‌تواند خطرناک باشد
توجه زیاد دیگران همیشه خوشبختی نمی‌آورد
باید قبل از اینکه دیر شود، آرام‌تر شد و به خود رسید
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/13554" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رئیس‌جمهور لبنان، ژوزف عون، در مصاحبه‌ای با سی‌ان‌ان ایران را متهم کرد که در رویارویی با آمریکا و اسرائیل از کشور او به‌عنوان یک برگ چانه‌زنی استفاده می‌کند و گفت: «این کشور، کشور شما نیست.»
عون همچنین افزود که مردم لبنان از جنگ میان اسرائیل و حزب‌الله خسته شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/13553" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است و جای نگرانی برای شهروندان وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/13552" target="_blank">📅 16:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130435eef7.mp4?token=ktU8NiTK6-qwCYQV1_gLyEig4ziFy5Dj7FFnyOGTCu-Pm1hxYhaEnaLDxaeVEeTKbKsA_jT7kqMF7rePjpjBemIhhrlkL9OEJQQ2tznMX-MA7zgU-0qiHEQFk56TxIDE4NR-5MGtSnNZu6AF13IwxwN9V83wEXMYytqXkF5Qtkgry76PVqPGbJTPBqlXVVbDngMIyK8fX9D1FxL4h3x8QMpyWZXEqtsTcd_A-fcnIyElAg7QA9DEVeuUT6BCokXr9BUn3Qpy2LL8idGDPB3XNYCme3O35c9sNMFON2aR6gymmo-beR92ObObSFt444FfAz-rg7TR6MCwcIcfoxTIgIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130435eef7.mp4?token=ktU8NiTK6-qwCYQV1_gLyEig4ziFy5Dj7FFnyOGTCu-Pm1hxYhaEnaLDxaeVEeTKbKsA_jT7kqMF7rePjpjBemIhhrlkL9OEJQQ2tznMX-MA7zgU-0qiHEQFk56TxIDE4NR-5MGtSnNZu6AF13IwxwN9V83wEXMYytqXkF5Qtkgry76PVqPGbJTPBqlXVVbDngMIyK8fX9D1FxL4h3x8QMpyWZXEqtsTcd_A-fcnIyElAg7QA9DEVeuUT6BCokXr9BUn3Qpy2LL8idGDPB3XNYCme3O35c9sNMFON2aR6gymmo-beR92ObObSFt444FfAz-rg7TR6MCwcIcfoxTIgIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13551" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c96db917.mp4?token=gI3N8MG9ADkpb06uN1b4yhIazdO79M4dpQ_E41Xnserx5-MgHVcuUMrdaFWM1zJxfKlsR46MnT2O3g9DGkUGpu9KeBlHO_FUxaWwRLPRnCzciOmgh2yrgcYUNnwTVD3QXdVrwLEgu54I7flYPOSPseV2nH5Sfv2VlYNE-RqhH7EWRsFGMB_uHHAj6DcM21NwNyJIP6j3CHxDi--i-QQnso4H2TO7qU9ZaSnKSjLnFRazaKL60SAHYHmEW_Q0pvOHpkWO_mtJKbHoewEvJ9J6qtE7Bl5_C8bSzePo9XFRE25Z1uyX-C8M6ls02aUZvQyDD_LuOIEHKv8WiVhvrqjHtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c96db917.mp4?token=gI3N8MG9ADkpb06uN1b4yhIazdO79M4dpQ_E41Xnserx5-MgHVcuUMrdaFWM1zJxfKlsR46MnT2O3g9DGkUGpu9KeBlHO_FUxaWwRLPRnCzciOmgh2yrgcYUNnwTVD3QXdVrwLEgu54I7flYPOSPseV2nH5Sfv2VlYNE-RqhH7EWRsFGMB_uHHAj6DcM21NwNyJIP6j3CHxDi--i-QQnso4H2TO7qU9ZaSnKSjLnFRazaKL60SAHYHmEW_Q0pvOHpkWO_mtJKbHoewEvJ9J6qtE7Bl5_C8bSzePo9XFRE25Z1uyX-C8M6ls02aUZvQyDD_LuOIEHKv8WiVhvrqjHtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ایران اعلام کرد که به دو ناوشکن آمریکایی (DDG-103 و DDG-87) در دریای عمان شلیک هشدار انجام داده است  موشک‌های قادر و پهپادهای شهید دانایی.
هر دو ناوشکن به سمت اقیانوس هند عقب‌نشینی کردند.
ایران همچنین ادعا می‌کند که ناو حمله آبی-خاکی یو‌اس‌اس تریپولی مجبور به ترک منطقه شده است.
هشدار نیروی دریایی ایران: اگر کشتی‌های آمریکایی بازگردند، از موشک‌های برد بلندتری استفاده خواهد شد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13550" target="_blank">📅 15:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmWHIvxBSbvOQH0dP6QIEFtdN0WgMaOY1cZUsDSggvhO9NJ4GMivu5En4sqNG9lPPbWA7uLTEEZWUg2iSYB6YK1eyzf61M9VGkrKlQ-piZN97_wbq65AbvyttEKQF5TIT2diOIaxvNYOXLrFccXoj0GYgtK4noehRPjGFcLb6rB1IDElW6vqbYmn7R5sUXs46ndxLdQijU5tT982ROmX68tQsRgu55UAKjHchrlvLzvUCrHIJG04TJuY3fgHTeoO-QYIX4FGPo3wolq5-n2KvLLLTwFTvBXRvqvLPYVqexLvnwUHVw6HIHnDSHNb6_H1wse1yvq9ixBeeZAx94icsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️حمام خون در بازار کریپتو!
بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/13549" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=uonIwMOzWIj4XFvvlNmkp8KflBTUW22HeJi4KsSs2bH2DwFQ8iIFGmAxg-9S6E1Vi-q0ECVLlnhnJ5s8UhVNYg58GGRqinPIx44ndgUBQjRoerAPej2qaS1qE3XpnCbriSg6uw7ESrNPW_IaHOgO-eqkkZZ9ZshmnLzdNgDzjrFwUFdzBF9-9tfVHxR1pTihHdpGT6Q8vh6ykEkVs_XBxfDYwwXjrwzwxwEiOVJpJ2z1mxMClFUfo09mukWzmrwshBuhP7JTrgNmqjUEKWkj16AtegnC6_ScgG9WLI3B8sHtxi7_9HjDInla5TB3laM-yrK2dYeLeYWFCa1XI8WmlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=uonIwMOzWIj4XFvvlNmkp8KflBTUW22HeJi4KsSs2bH2DwFQ8iIFGmAxg-9S6E1Vi-q0ECVLlnhnJ5s8UhVNYg58GGRqinPIx44ndgUBQjRoerAPej2qaS1qE3XpnCbriSg6uw7ESrNPW_IaHOgO-eqkkZZ9ZshmnLzdNgDzjrFwUFdzBF9-9tfVHxR1pTihHdpGT6Q8vh6ykEkVs_XBxfDYwwXjrwzwxwEiOVJpJ2z1mxMClFUfo09mukWzmrwshBuhP7JTrgNmqjUEKWkj16AtegnC6_ScgG9WLI3B8sHtxi7_9HjDInla5TB3laM-yrK2dYeLeYWFCa1XI8WmlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود حجیم جنوب مركزي تهرانه  همين الان
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/13548" target="_blank">📅 15:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بر اساس نظرسنجی‌های معتبر آمریکایی حمایت افکار عمومی آمریکا از پایان جنگ و حرکت به‌سوی توافق، از ۴۹٪ پیش از جنگ به ۶۸٪ در آستانه توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/13547" target="_blank">📅 15:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه. @withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13546" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فیفا: نقص سایت باعث صدور بلیت‌های رایگان شد
‏فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13545" target="_blank">📅 14:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13544" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13543" target="_blank">📅 12:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد و از اسرائیل نیز متقابلاً خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت این کشور احترام بگذارد.
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/13542" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اصابت یک پهپاد به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13541" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل شب گذشته به قطعنامه آتش بس در لبنان رای نداد
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/13540" target="_blank">📅 09:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">طبق روال هر روز صبح حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13539" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL00r_x6xF_ubztutT7lNj5gMEknldpN9ykUQzd0dFmpAOJ7haN-FZqcXY-uFBJLrhJXwC59CLxGNrxu3At6R4qmXoh_tsfPbxKC01pFEOdW2uYwLdVJlTNRhEGVSiuYVb9xi6Qvd_aBXic7GBTtMmFd85PtLk0kkZDUruS3QODRMcmT47Gi7nVWiWMu8RhWwTNXiI2dOA3BTzz_AvQE56GfSF1fmy7un58bltKrb0vNpinHF2lXk01mWBT-I2Az0gK_y1_8H6Y-CeEvxcXjbcowNxTydVzx4uEBpbYq45L7IAqT5zguZ7r8QzZRvpaVS-_-sOps7KAolj7TPbcJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای زیادی برایم فرستادید که از پدافند سنگین ۳-۴ صبح و چندین انفجار در تهران ولی مدرکی نیست… فقط چندین عکس از اینجا برایم آمده.
آزاد راه پردیس به تهران
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/13538" target="_blank">📅 09:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امشب بیداریم ، ردبولم میزنیم
🤣
💥</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13537" target="_blank">📅 09:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رویترز: بامداد جمعه انفجاری پهپادی در بندر الفحل عمان رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13536" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نورالدین الدغیر خبرنگار الجزیره در تهران:یادداشت تفاهم در مرحله نهایی خود قرار دارد
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/13535" target="_blank">📅 08:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=Ode9Qj1oCrfcDMfwoePAk2sJClCrQw_Tg-TEXMWNiRAdTip_3IyN27I6K6XUJWD0_uYgZjcoKzfjzpw-bzlJN6e_KRUVtOdGqNVjl-AxAV-Bn8-IwGi0GeYURmFyYJ-IMDGnRATE9CiNN7KZkr8QOZ1zazQuHfr0ASMNHO38Ib4l8INb6rVrVW5OOOs4yHKNK-G_N8dRvUJWPl33pnEg-2_cyxDc9D8I1wUgbp5QCaD9ZQ0KniXAzq8JXGqlvk7KSgh5w6Za9mPvAs7KEbyQ7DIg9qzmObMao4BtbXSrZbP-tR9UbYGsglytY8A0-3MLaelFGHZoaM0a6lBr1bMNAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=Ode9Qj1oCrfcDMfwoePAk2sJClCrQw_Tg-TEXMWNiRAdTip_3IyN27I6K6XUJWD0_uYgZjcoKzfjzpw-bzlJN6e_KRUVtOdGqNVjl-AxAV-Bn8-IwGi0GeYURmFyYJ-IMDGnRATE9CiNN7KZkr8QOZ1zazQuHfr0ASMNHO38Ib4l8INb6rVrVW5OOOs4yHKNK-G_N8dRvUJWPl33pnEg-2_cyxDc9D8I1wUgbp5QCaD9ZQ0KniXAzq8JXGqlvk7KSgh5w6Za9mPvAs7KEbyQ7DIg9qzmObMao4BtbXSrZbP-tR9UbYGsglytY8A0-3MLaelFGHZoaM0a6lBr1bMNAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر اختصاصی جدید CNN خسارت ناشی از آتش‌سوزی در ناو هواپیمابر USS Gerald R. Ford (CVN-78) را نشان می‌دهد؛ آتش‌سوزی‌ای که در بخش لباسشویی کشتی رخ داده و در زمان استقرار آن در دریای سرخ و در چارچوب عملیات آمریکا علیه ایران گزارش شده است.
این حادثه در ماه مارس حین جنگ با ایران  رخ داد و نیروی دریایی آمریکا فوری اعلام کردن آتش «مهار شده»، دو ملوان با جراحات غیرمرگبار درمان شده‌اند و ناو همچنان «کاملاً عملیاتی» است.
اما ویدیوی جدید CNN نشان می‌دهد خسارت بسیار شدیدتر از گزارش اولیه بوده است و منابع به CNN گفته‌اند سامانه اطفای حریق ناو از کار افتاده بود.
یکی از ملوانان گفته است خدمه حدود ۳۰ ساعت به‌صورت دستی با آتش مقابله کرده‌اند و حتی نگرانی درباره احتمال از دست رفتن ناو وجود داشته است.
مقامات تأیید کرده‌اند این آتش‌سوزی به‌طور موقت عملیات را مختل کرده، پرواز جنگنده‌ها را دو روز به تأخیر انداخته و باعث شده ناو برای تعمیرات اضطراری در یونان پهلو بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/13534" target="_blank">📅 01:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ می‌گوید دولتش بررسی کرده بود که نیروهایی را برای تصرف اورانیوم ایران بفرستد، اما در نهایت این ایده را رد کرد چون خیلی پرخطر بود و می‌توانست به تلفات آمریکایی‌ها منجر شود، و این موضوع را با مأموریت ناموفق نجات گروگان‌های کارتر مقایسه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/13533" target="_blank">📅 01:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13532">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ ۲۵ بهمن ۱۴۰۴: میخوام با آیت الله علی خامنه ای دیدار کنم.
۹ اسفند بخارش‌ کرد.
ترامپ ۱۴ خرداد ۱۴۰۵: میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
چه تاریخی بخار میشه؟!
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/13532" target="_blank">📅 00:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: ما به ایران رسیدگی خواهیم کرد، و به‌محض اینکه کارمان با آن تمام شد، در مسیر بازگشت، برای مدت کوتاهی توقف می‌کنیم و به کوبا رسیدگی خواهیم کرد… باید از شر این نظام خلاص شویم
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/13531" target="_blank">📅 00:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ: برنده این جنگ ما هستیم حالا چه روی کاغذ چه با قدرت نظامی
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/13530" target="_blank">📅 00:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/13529" target="_blank">📅 00:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ : من دنبال عملیات مخفی برای گرفتن اورانیوم ایران نیستم اون اورانیوم عملاً دفن شده و از بین رفته
اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران؟ نه من نمی‌خوام جیمی کارتر باشم
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/13528" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
راستش نمی‌خوام با آیت‌الله دیدار کنم، ولی اگه ببینمش، برام افتخاره. با احترام هم باهاش رفتار می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/13527" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak</strong></div>
<div class="tg-text">عمو یاشار اتاق جنگ نمیری امشب؟</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/13526" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:
من در امور امنیت ملی خیلی تجربه زیادی نداشتم، اما فکر می‌کنم واقعاً کار خیلی خوبی در این زمینه انجام داده‌ام.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/13525" target="_blank">📅 23:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">منابع عربی:ظاهرا چراغ سبز برای بمباران حومه شهر بیروت گرفته شده است
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/13524" target="_blank">📅 23:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح هم اینا برن، طول می‌کشه. این زندگی واقعی هست و رؤیا و خیال‌بافی و وعده‌وعید نیست! حتی مانوک هم گفت بعد از مذاکرات تازه بازی شروع میشه، پس ما اولش هم نیستیم.
ولی با من این مسیر رو راحت‌تر از تمام حالات طی می‌کنید
❤️‍🩹
🙌🏾
ما بقی بازی سیاست و خبرگزاری‌ها و مارکت هست که ما هم به ناچار توشیم و انتشار می‌دیم! ولی این اخبار به هیچ وجه نه حرفه منه، نه کلاً تأیید می‌کنم؛ چاره‌ای هم نیست، این مسیر باید طی بشه!
از توجه شما به این مطلب ممنونم.
دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/13523" target="_blank">📅 23:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فقط‌منننن خیلی‌رک میگم عمو ترامپ ۴۰ تا ملغ میزنه اخرم نمیگه
😁</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/13522" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد @withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13521" target="_blank">📅 23:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13520" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13519" target="_blank">📅 23:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13518" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">پدافند سمت وزارت کشور فعال شد الان</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13517" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13516" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAMIR</strong></div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13515" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال 12 اسرائیل:
مذاکرات به نتیجه نرسید، آمریکا تا آخر هفته پاسخ میخواهد و با ایران اعلام کرده یا توافق می‌کند و یا درگیری از سر گرفته می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/13514" target="_blank">📅 22:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neYeBBheiTXQ9Dgr3z2YZKrSOgrxgwXsJq8n8yuhKybFeZp7X_kI8puYss0svUE5hPoBqkePJOyxb85v1-pYlE4Tpc-UcBApdozEMmHlJ629PVasQa4n9sIy41rAL685_hJIakKnknvsBjWFqoi9YN8M6PABhBbymCky-BkRFTUGqhDZtlx2IZh7llxTAHeJwNoDJt1TyhL0AvKbq8eYrLCphvKmeIB02WNSCrfW52trW0VjU2Sa1hc_QxBfkQmX8B5B5xvB4QaSp4y0sQsJy4zNp7UP3bZZaEgSrJo7bMm9WtWK2J91fWRtfYZAdzTdmoNeaUMQZ9s6wlqEdxf6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده هشدار امنیتی برای تمام کشورهای خاورمیانه صادر کرد
دلیل این هشدار محتمل بودن درگیری اعلام شده و از همه شهروندان آمریکایی خواسته شده که نزدیک‌ترین پناهگاه را پیدا کنند
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13513" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAniyOMQIxsvjQkmpFEMQEd-RQf92q20fv742nbBfZvbfyMlx9YJkypz6M-BP1OUP-_ZG-9Y70sipUZGPHsnSYthKNbh33-QgHrJYEVCZrsyIiThGkJUAn8pduWUx03Y44Any_W3_ZmAOvSwte5BEjkNQbOtrFg0wZmu9WEyZINvYKj_wR626wXEk4-4pkDkjNvMRZpZ7SMwr3Fgyu6mS0-CFF5ILIg4seuziR3qKV2aXNDJt8xn3es3UFhwV-QgH3Y0wH7m-UsUQb5te1K_2FMgc8-qotdrkqytpxK10avFtndcppiGQzp-uonKCxdemPzo2zUNO7gTGdpCh5iRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان و دخترش کشمش
🥴
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13512" target="_blank">📅 22:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13511" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سفارت ایالات متحده در اورشلیم هشدار عدم سفر جدیدی برای اسرائیل منتشر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13510" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13509" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ادعای رویترز بر اساس داده‌های حمل و نقل: صادرات نفت ایران به پایین‌ترین سطح خود در حداقل ۶ سال گذشته رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13508" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۲ اسرائیل: واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13507" target="_blank">📅 21:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIU_Vc7D_ZT_ACW1ol388DVnflzNSPmAxjrqR7x2GiFQ50qH_6E6vxCmVn5hNsocP5-0Gi7S_QnJi0R3Blxzhu7Vvzcfq38F_lE6xQYx3d2xcfiLK7xAmcjonzcopDSiixRLrg6pcXxtvRHRw6tobP-P7thE9Q6e1MYqG1yb_-HV4Fntqw0g0ERQGYmxu8dLK0aWd-mK_Sb_8IPyqOuDbpdEh4Lgc8rSSncWdVvovOSfZ8oo5Xm1rq2sELK_YE70BXPqTC0ueG83I6HX5tGq3Y8hcQ-Hz-hBkDEe2uImXlGGF0l8uarmgOqIQEWUMH00OLP6naiSjGrb0mymRL7Qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل :
اعضای ارشد امنیت حماس را ب درک واصل کردیم
این اعضا وظیفه شون حفظ امنیت سران حماس بود ولی خودشون حتی نتونستن امنیت خودشونو تامین کنن
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13506" target="_blank">📅 21:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خوانندگی قیصر برای کودکان میناب در میدان امام حسین
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13505" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OitI5PHwr5Oj9PJbcAN3PH4IDrs8pOWxkWsljmM2G-qL2jXe9pLZhORghLZ04ZHToxCYFJvAVRJFTDqTxhyk4KPrLToz8qxEPscaMVH8gQ0ylo3xViC9VrqwuwCkx5grO9_iBMZEBKR7TbOTlU9s8j-ib0ZiO3orj4hVb7yCsja_KlrCYGVulqz8kT3HaiVl4DT-iusGPRsK8SQmiwG_ecEKxplcR7n77-eFjv4JrUz5DAdItIsDXqhK9dAtP3z_uG7fRjLFDim-5opNHeUZffs_GP4_9wjHMy1Or1iHtdjyuKiGzLJ0aROWJ-m6GUDEznGmsHdoNAslG6kID_O3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها سردار سپاهی که امروز تو مراسم سالمرگ خمینی حضور داشته:
محسن رضایی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/13504" target="_blank">📅 20:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">@withyashar
قیصر</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13503" target="_blank">📅 20:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=r87wvWIlPxMhr2A_ouROl0Vz64zmhgRSLdliQiYGmTQbp7OKcUyvU0uu6BRrs3MPyrL8kUN2Zt2bMbZLb1lBchwaKASqhyGns01VRXlD6ngOeB5VhmzVobl8IezivJyFD7ORADyJk709NIuoOnGBoWxk1YlxYc86zpfU1PNbI1rx_mO1tLn6xTue85MJ8HlwwYAa_b5RvTeOdhjT3dmo9nbyD4lDr5NWW0wo8PCSvMS1HTKtfTobWTogtx8G52skM2I970P8fKJB1p5wl6ziQZ1nZBybCuRzrGqXfowYbFDZxn5U_HLix4Vqt0PyJf7j9jtJi2YQ51SC1iV_pW1dCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=r87wvWIlPxMhr2A_ouROl0Vz64zmhgRSLdliQiYGmTQbp7OKcUyvU0uu6BRrs3MPyrL8kUN2Zt2bMbZLb1lBchwaKASqhyGns01VRXlD6ngOeB5VhmzVobl8IezivJyFD7ORADyJk709NIuoOnGBoWxk1YlxYc86zpfU1PNbI1rx_mO1tLn6xTue85MJ8HlwwYAa_b5RvTeOdhjT3dmo9nbyD4lDr5NWW0wo8PCSvMS1HTKtfTobWTogtx8G52skM2I970P8fKJB1p5wl6ziQZ1nZBybCuRzrGqXfowYbFDZxn5U_HLix4Vqt0PyJf7j9jtJi2YQ51SC1iV_pW1dCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حظور قیصر خواننده
لس آنجلسی در جشن غدیر
🥴
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13502" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/13501" target="_blank">📅 19:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">داداش این خاننده دوزاری لس انجلسی که اوردن ایران پشت پردشو تو باید بدونی دستت تو موزیکه
پتشو بریز بیرون این عرزشیا عر عر نکنن</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13500" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد،
زودتر از آنچه فکر می‌کنیم،
سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13499" target="_blank">📅 19:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس با اسرائیل را رد کرد
شبکه المنار حزب‌الله ،گزارش داد که دبیرکل حزب‌الله لبنان گفته است که این گروه از جنوب لبنان عقب‌نشینی نخواهد کرد.
نعیم قاسم در این بیانیه گفته است درخواست این توافق مبنی بر خروج نیروهای حزب‌الله از جنوب لبنان، در شرایطی که این منطقه زیر آتش قرار دارد، به معنای "تسلیم شدن، شکست و تحقق اهداف دشمن" خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13498" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وای‌نت: موساد در اقدامی با هدف سرنگونی جمهوری اسلامی، سلاح‌های ضبط شده از حماس و حزب‌الله رو به کردهای مخالف جمهوری اسلامی داده بود.
سازمان اطلاعات مرکزی آمریکا، سیا هم در طرح استفاده از نیروهای کرد به‌عنوان بخشی از تلاش گسترده‌تر علیه حکومت ایران مشارکت داشته. این طرح در نهایت پس از فشار رجب طیب اردوغان، رییس‌جمهوری ترکیه، و در پی هشدارها درباره خطر گسترش درگیری منطقه‌ای، از سوی دونالد ترامپ لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13497" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj2-YX2JNuxJnqbvwNLdG_vSbiTa_xizwl-TAF3oBmKT9XG6qrpXmXhCJhlJXNTghHcEn8wOLGE_S2BYYxuLsTTBS-GEO3waUmrz4qmVRgErRbK824TI2tRcPghbXHRs3BiFFZPyRmfk0f2vXFPtOw5MQookAT_2oJ_OFAUL-_KzmyF0Mamy81KlifV6El7I3_5wEDRxDdNJB9GSgL-wgHZ7vI-kq2jgu_uhyzYBSCcZ6Ta18gYtbvubjlqOA57W2ca_u3Up2rmu8uHdummT2fY8AsH05RM3AJcjZ2tcrm6gdIJKufej3YH7k4PPiqz_EzmkHMeTaxtOxHXDgB_ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای کاتولیک یک جن‌گیر را پس از ارتباط دادن مشاهده‌های یوفو با فعالیت‌های شیطانی برکنار کرد،.
جن‌گیر مشهور و قدیمی کاتولیک، استیون روزتی، گفت به باور شخصی او بسیاری از مشاهده‌های یوفو ممکن است ماهیتی شیطانی داشته باشند ! وی علاوه بر آن روان‌شناس نیز هست. به همین دلیل وقتی او درباره یوفوها صحبت می‌کند، سخنانش بیشتر از یک فرد عادی مورد توجه قرار می‌گیرد
اسقف‌نشین کاتولیک واشینگتن این اظهارات را مغایر با رویکرد رسمی کلیسا دانست و روزتی از سمت جن‌گیر رسمی برکنار شد و همکاری کلیسا با مرکز معنوی او نیز قطع گردید.
روزتی بعداً عذرخواهی کرد و بر تبعیت از آموزه‌های رسمی کلیسا تأکید نمود.
این ماجرا بحث قدیمی درباره ارتباط احتمالی یوفوها، موجودات فرازمینی و پدیده‌های ماورایی را دوباره مطرح کرده است
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13496" target="_blank">📅 18:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRi_ntv6GrroL5tB7rUqXdqSkfMReewk4h5dgDzDuQpkOyIt8BgS2-_gOUCJ6zx2cYwC8EriTt-1Ud59prtWQnTCDitUnZsMTksG1UDYqB3EFESoXnSeoxl9kxelYkWOr9Zp32cSL69jc4umB2NZTCJEzPtPpoJx4mEwUuH3IwKaZq1etRhx352vQyc0Iooobkd4_0pZWr-7kAGgzEfEUCcotNuW-ZY9cjmyJVvEbp3wijH_dx889KlzvpsGSh_61TnDykqAHs4p3aX48amgENZ-AOUoDv7iEVX5aAeBaunXWpu5tZKM7ZRpR8XL7HBSYL7t36t40j4pf928H73IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم رو بردن تحویل بدن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13495" target="_blank">📅 17:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سپاه: اسرائیل فورا حملات خود را متوقف و از مرزهای اشغال‌شده لبنان عقب‌نشینی کند
هیچ آرامشی در منطقه بدون عقب‌نشینی از مناطق اشغالی لبنان برقرار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13494" target="_blank">📅 17:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اصلا جان بر کف و جان فدا برای ما بود اونا گرفتن
😃
🤣
اون عرزشی ها کپی‌کارن زبان فارسی‌هم میراث ما هست نه اونا ، شاهنشاهی هم میراث ما هست لغت شاه هم کل دنیابگین میگن شاه ایران !</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13493" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مردم به ایلان ماسکم دیسلاک دادن موشک هوا کرد
😁
شما توجه نکنید پیشنهادم به بعضی ها اینه که یک جعبه شیرنی‌بگیرن و با خودشون آشتی کنند</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13492" target="_blank">📅 17:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGICfYKUNb40kPliSqzjl-nxsJ8v_ElkCpncZp9iYInrGIxM9ONkWWFAAHPvnfLAKh5fUr_qHAVX5RSklqzUqfQHqQUbRNhZg2IH2-PtApR5H3Pr8ONZArmOi9PILVaAVCLmMHlzFnQU_fyucARTvVqYEp_rXghz2np73OMkZdaVoCSRFoXevj4ifpB2684foVuCsKL2NfmVEQQyz_t2vLGT2yLpVo3Jj5C3xEigQfnDPUB7YRQfwEf1-5ETSF7Mm-6QqL64KMoAlLe2jbDEVVXE3IU0Z6Jdm0mjd_Pp01t44wwIC408usrS-bybC0hk0d9boSoIiNtBE6tae1TYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13491" target="_blank">📅 17:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌹</strong></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13490" target="_blank">📅 17:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=Sn9Ojw7S44a2bRC7Gc81cefo2axwgBkZoJO0ekj4kOuXX6Jp3p_Y8juFK0f36v5rMhjbaf5fk787we2DVdERYSHJ7scHor6DT_HIwq3GGhq0i1-9UXilmj4nfJBmvXQZJ8C2q50OEM-Xt2UdS0Agg2rU8rz3Dj_XDx4BykK5byS_Fn8lIS4j7Zb5XrbITLV-P2bE4aM7NLzaaOI-0V6Bb4n5d5XGahNOztse60ThL1HB1izkD7k217rBnd0gDOP-OpvlFtMtZQdMLVBIW6d3KHeX2Ipy4_WyT4u6Y2hPokSA52bY2eumdxEygIsgzPZxj9G0tu6VxNQcjYAY3X2nGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=Sn9Ojw7S44a2bRC7Gc81cefo2axwgBkZoJO0ekj4kOuXX6Jp3p_Y8juFK0f36v5rMhjbaf5fk787we2DVdERYSHJ7scHor6DT_HIwq3GGhq0i1-9UXilmj4nfJBmvXQZJ8C2q50OEM-Xt2UdS0Agg2rU8rz3Dj_XDx4BykK5byS_Fn8lIS4j7Zb5XrbITLV-P2bE4aM7NLzaaOI-0V6Bb4n5d5XGahNOztse60ThL1HB1izkD7k217rBnd0gDOP-OpvlFtMtZQdMLVBIW6d3KHeX2Ipy4_WyT4u6Y2hPokSA52bY2eumdxEygIsgzPZxj9G0tu6VxNQcjYAY3X2nGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایت شهبازی از کار
😂
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/13489" target="_blank">📅 17:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad Jalilzadeh</strong></div>
<div class="tg-text">اقا ری اکشن کوچکترین تمرین هست برای پذیرش دموکراسی
وقتی یه عده همه ش دنبال کم و زیاد کردن ری اکشن هستن و دنبال اینن که کی چه ری اکشنی زده در آینده ی ایران چطور میخوایم همدیگه رو تحمل بکنیم و باهمدیگه حرف بزنیم؟
همه ری اکشنا باید باز باشه و کاملا مخفی</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/13488" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی…</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13487" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چند گزارش ساعت ۱۵:۵۴ دقیقه محدوده شمال شرق تهران همچنین نیاوران صدا پدافند شنیده شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/13486" target="_blank">📅 16:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی را در برابر چشم جهانیان قرار دهیم.
@withyashar
وی به این موضوع که ورود پرچم ما به ورزشگاه ممنوع است و چه راهکاری باید داشته باشیم اشاره نکرد.</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/13485" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezANfN31Z4bPzq6vl_KHtlDz0qfWgXjzX996mLFOglwIXxIR38CB3wrYJ6TageV1dGg1nlS_k2p6Isv26BDeV_UCA2Nfz4oN09cEmIzeNxQVllbFqyF1NFC_gn7NyfEDbjlIBFUCkFjAZEVtC9nHFR1iSRVYv5zxJsy7ArIJ8t8p8uLBOsME8V2GruMnwdcBNkBSOU07zB4Mx2Nhb8DF5qZjNSmYUiw8wBSJWBhMJsB4WssKX3G7EAoe6YhjSQzjf7GkLgsY4LRkwOdZTAezP5cOXGKuxivgd9VEsboKNxujpGZEF3iCOyrzS9C3eKv2rFRpSaBtpyp-8baY-WwSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : سازمان تروریستی حزب‌الله گلوله‌های خمپاره‌ای شلیک کرده که به یک موقعیت نیروهای سازمان ملل اصابت کرده و در نتیجه یک نفر از کارکنان سازمان ملل در جنوب لبنان کشته شده است
شلیک‌های حزب‌الله نیروهای بین‌المللی را در معرض خطر قرار می‌دهد و به کارکنان سازمان ملل که در منطقه فعالیت می‌کنند آسیب می‌زند
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/13484" target="_blank">📅 16:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نعیم قاسم، رهبر حزب الله: نتیجه مذاکرات دولت لبنان با اسرائیل شرم آور و پوچ است و اونو بطور کامل مردود اعلام میکنم.
تا زمانی که تجاوز ادامه داره به هر جایی که تصمیم بگیریم و بتونیم حمله می‌کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13483" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: در وسط مذاکرات پایانی برای پایان دادن به جنگ هستیم
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13482" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej8Bw7S3-aIiOhdt-bM20YmTtk9gxniVyaywFjejPN5AoqBBL2J9WsfdJZJBRnl6riigjErakFVchF63tH6iW8-LyJzHeOwbQ7pymW80OBUckV-uHuBUznecwe0ZHvZgQIOGAk1X-QDhQvrTleTO4uOQaqdhFlN-nZXgcCG1RDc7qzZaDibZDzYZrHqkGdWB62y-4xO6rbwzEvzVShXy1ze-Q0jv-yn9yoWL4T2LhFGm5Mc7I06q7R_4v2NiTqgPQH_mAm7zF7tAQsimgQRBCeHXWjDWV8AoRQ9KyZbsG-CFxCCa_bzHQyzJvssQ_d18ccwG84QGt77ZzDUD5LBmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عکسی از نشان‌هایی با نماد جمجمه به سبک ترامپ منتشر کرد
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13481" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrnEeOzJLwh7WsyXwhzFSI4UUlhU1mYCL2bgRjb7zx-KO1LHa4Xs_bMxaZtK87nYFf0Tmw-feFIoRjlYsWw5bzLpxUw6IQJ1il4YR1oYAXTUJyX2jo5IuGL2zlYlQnO5KNCWWzyI4kC8_Q3E_c1wy3TOfNpB-pxV08AuzHBDb2l2UEFr36OuRuh3RtAxP0ksUPF000o-GBZlljBMQ1yb60h6iYMu1Q_6Oc1zloNvrQK4G8owfevNKadfDtz8Hen0818-VAIqV3aGfVOKLLX5XCAWY9AB1LFvx7oLMVK24rtdutPaKYYpbTAP3-XoniLCRdNQHFpWy0jX_PwnegCnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیروز، در یک رأی‌گیری بی‌اهمیت، مجلس نمایندگان با رأی ۴ جمهوری‌خواه بد و همه دموکرات‌ها، تلاش کرد اختیارات جنگی من را محدود کند؛ درست در میانه آخرین مذاکرات من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آن‌ها می‌دانند وضعیت مذاکرات در چه مرحله‌ای است. دموکرات‌ها با چیزی به نام «سندروم جنون ترامپ» هدایت می‌شوند. آن‌ها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یک پیروزی دیگر از میان پیروزی‌های بسیارم به دست بیاورم. آن چهار جمهوری‌خواه، ماجرای دیگری دارند آن‌ها اهل خودنمایی هستند! باید از کار خود شرمنده باشند.
MAGA!!!
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/13480" target="_blank">📅 14:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد. @withyashar
😟</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13479" target="_blank">📅 14:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اکسیوس :  یک شکاف رو به رشد بین ترامپ و نتانیاهو در مورد آینده منطقه در حال شکل‌گیری است.
بر اساس گفته مقامات آمریکایی، ترامپ می‌خواهد تنش‌ها را کاهش دهد، درگیری‌های جاری را پایان دهد و به دنبال یک توافق دیپلماتیک با ایران باشد.
در مقابل، نتانیاهو به نظر می‌رسد تمایل بیشتری به حفظ فشار نظامی بر ایران و متحدانش، از جمله حزب‌الله، دارد.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13478" target="_blank">📅 14:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فیلم جدیدی که حمله هوایی آمریکا به پل B1 در کرج، ایران، را در طول جنگ نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13477" target="_blank">📅 13:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال ۱۳ اسرائیل: «کابینه امنیتی اسرائیل امشب ساعت ۱۷:۰۰ تشکیل جلسه خواهد داد»
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13476" target="_blank">📅 13:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وال‌استریت ژورنال : آخرین پیشنهاد ارائه‌شده از سوی ایران نتوانسته رضایت کامل دولت ترامپ را جلب کند و هنوز اختلافات اساسی بر سر برنامه هسته‌ای، سرنوشت اورانیوم غنی‌شده، رفع تحریم‌ها و آزادسازی دارایی‌های ایران باقی مانده است.
وال‌استریت ژورنال تأکید می‌کند که تماس‌ها و تلاش‌های دیپلماتیک همچنان ادامه دارد ، ترامپ همچنان به دنبال توافقی است که از دید او برنامه هسته‌ای ایران را به‌طور مؤثر محدود یا برچیده کند. در مقابل، ایران خواهان امتیازهایی مانند آزاد شدن بخشی از دارایی‌های مسدودشده و کاهش فشارهای اقتصادی پیش از پذیرش محدودیت‌های گسترده‌تر است.
اما مذاکرات هنوز زنده است و کانال‌های ارتباطی بسته نشده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13475" target="_blank">📅 12:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وال استریت ژورنال:
«ترامپ به مشاورانش گفته است که جنگ تمام‌عیار با ایران را از سر نخواهد گرفت، مگر اینکه نیروهای نظامی آمریکا کشته شوند.»
مقام‌ها می‌گویند حملات مکرر ایران فشار بر رئیس‌جمهور را افزایش داده و تردیدهایی درباره دوام بلندمدت آتش‌بس ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/13474" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انتقاد مارک لوین از تصمیمات جدید ترامپ:
جمهوری اسلامی شاید نیروی دریایی و نیروی هوایی قابل ‌اعتنایی نداشته باشد، اما همچنان سپاه پاسداران و یک رژیم ایدئولوژیک دارد که شکست نخورده است؛ ما ملت ایران را برای سرنگونی رژیم مسلح نکرده‌ایم. رژیم کماکان در حال شلیک موشک های بالستیک و پهپاد ها است و هنوز مشخص نیست این تبادل آتش بخشی از مذاکرات است یا نه؛ هرچند در نهایت، چنین مواردی قابل راستی‌آزمایی نخواهد بود.
به نظر میرسد ما از نابود شدن سازمان حزب‌الله لبنان ممانعت می‌کنیم؛ حزب‌الله، قدرتمندترین نیروی نیابتی رژیم ایران میباشد که در 40 سال گذشته آمریکایی‌ها را کشته است؛ همچنین حماس به جای خلع سلاح، در حال تجدید قوا است.
این وضعیت برای آینده و پس از پایان دولت ترامپ، نشانه خوبی نیست. من فکر نمی‌کنم چین کمونیست که بزرگترین تهدید برای ما است، تحت تأثیر قرار گرفته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13473" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9960590f00.mp4?token=gru_IJ4QJU7UrUhtYkyP0-4At0ugC5tCk7TeMjCXw4KHy2cSzji6z5T4PwrrvjH9T6BsQJfy7MO4XQvpxhccDUGGj0u3KZ_zcDGJDuUz6aU0ltHfOppyqwdGtiKU9j0WYw06tJjgxKphuir-z5opBaDMSS77KtJqdYarOkOu439Aww96pw3BlE1oFHjAgPwFtou9uxlQ_3RuH3OA6zrniPAXpi8y3buIG74QaB2dtruuUJS3iYdeevICquVkDuU3ETXjLvE4aypmKSgIoW5J3NVdLI5fc-s5cPqPEpdDciWDvFvdc-Gte0Hc-ETSG_HNQTe_TorMRXUJOqeV449zjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9960590f00.mp4?token=gru_IJ4QJU7UrUhtYkyP0-4At0ugC5tCk7TeMjCXw4KHy2cSzji6z5T4PwrrvjH9T6BsQJfy7MO4XQvpxhccDUGGj0u3KZ_zcDGJDuUz6aU0ltHfOppyqwdGtiKU9j0WYw06tJjgxKphuir-z5opBaDMSS77KtJqdYarOkOu439Aww96pw3BlE1oFHjAgPwFtou9uxlQ_3RuH3OA6zrniPAXpi8y3buIG74QaB2dtruuUJS3iYdeevICquVkDuU3ETXjLvE4aypmKSgIoW5J3NVdLI5fc-s5cPqPEpdDciWDvFvdc-Gte0Hc-ETSG_HNQTe_TorMRXUJOqeV449zjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری نیویورک پست
: آیا آیت‌الله (مجتبی خامنه‌ای) همجنسگرا است
ترامپ: بله.
مجری
: واقعا
دونالد ترامپ: بله، و فکر میکنم خیلی احترام براش قائل هستند.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13472" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در مراسم سی‌وهفتمین سال به درک رفتن روح‌الله خمینی، پیام کتبی منتسب به مجتبی خامنه‌ای خوانده شد. در این پیام آمده است «نظام سلطه پادگانی به نام اسرائیل از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13471" target="_blank">📅 11:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13470" target="_blank">📅 11:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
@withyashar
🥴</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/13469" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :  شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.  برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود @withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13468" target="_blank">📅 11:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsdejBu4gDEOcdwANngNB_iBGR1qmHquGFWlEmlZH8P9n2pn3zwjOd17yJnELphBw8JFDhMJnpv9M-UW1dUL6FYvcmA4e6L2MWXSoCnhXqUD5r2D3nDOTshz6KIRvU_jIk3INVe-elIpmyWY5U_egfN5x5KTpv_Fi7ECvMxECajs47CqrDaRRgKbY8pBIoELPKLBiEA6X8HMRtLPUVYbUF9ep8ja_HoY1E9cvLy3ceqlUFOqzBAMyX1JDRL3MzOS-WBgthkAy-So66kGTvMmpSR-D8N4KMIWnLSms97PQpYvT1js6-WZL_OEW9uztX2KAlMevMuMhZYt5bK_IBiKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد پیدا شد
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/13467" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13466" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prROXeWv0JC-vSSI_tvQPIgcLTczBM7wqBK7mqLVdzy2ZucIAJWijVdo0V52poYGrV7ubGmmDp3ZBfRFsrLofB4lr7F54bYou2Wiru5vl-88iKL22wnxzjrpltmxxHad6AYThJ7qg0fdKYf7NAZIi39F2dnDiWMvL-m-e2_gLkAO-68iNEcvbZpuBGA7lEQk0orn_hk880vYI8LeT1IV3DDjX7Y-vq_-Y2B1FgsTd-zVRIEq3ef74_Ce6txwoeCRnV3fPiUUUgtU3UZxuj_QU7VS5TePOZUBHxgxuE0CQz_uj1DRlHEofT9M3bnpljkAiPCE3BdDRHNBJXXA3WO4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/13465" target="_blank">📅 11:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مقام اسرائیلی: ایران تصمیم گرفته در صورت آزادسازی اموال بلوکه‌شده‌‌اش، بخشی از آن را به حزب‌الله اختصاص دهد.
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/13464" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جنگ ترامپ با ایران و اختلال در حمل و نقل نفت از طریق تنگه هرمز، ذخایر نفتی آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۴ رسانده است.
برای کمک به مهار افزایش قیمت سوخت، آمریکا میلیون‌ها بشکه از ذخیره استراتژیک خود را آزاد کرده و همچنین صادرات به اروپا و آسیا را افزایش داده است تا جایگزین عرضه از دست رفته خاورمیانه شود.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/13463" target="_blank">📅 09:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=RRF8vtWaeUcACokbXzybdDypEzgTc7R5iALmJeHTdOKgiI4BjCpKj_-aqsQvOimyeYpMtULDf-UbZiDHJRV7CAbTF1271IBppiqINnWaMkL8Y875jFrzgqMpAmBV74UTGo9fItX2hcEZ4RLKyJdOL3bqZkQejn6uixgS1FRHh84A8Mb53xmmnZPbL3PAihsWtAipl52GmAZ6vUWTD76GQHQThBHOGwBqQ_STP1CxzGE8fVnAXfNAVAR-Hk14Vx8ykWTcPHWMg2H76gi3vihc3NabQ5CUoFnKip_8DFphclSkgu718Ofwi8D8Sr8GmvimV9Eyi113Klu2qD7knaQif53QLFGu0_Ihiy3n8blOiW3R7N3XAaIPwm6x3l6yeTJO6XaORKdasnAPZFJU7jYQFh5OLCGcA43wM_3ql6lbdVx6cOjSDovq-R732x5XIHDF_4u4FTBRlI3URGB26hcUITKorTaq4Jg5UKjdxfp6FHhHHvDxbgtYA21S1b0P62nRuQv-DNylJHvVABNUUa-WL9PKMUDUp-Xzn518ot9PrdJmtrucIvh40kmUqqp35D60UkiKhdzvuHBfnezUNIUYSY58_AzBlS6I2fpZJ2AwdKxKqOREZ8tl28IwoHmpB7cE3LDip8qn0inTDlHNvhjhTlfecqVvazfqDGnWknczltY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=RRF8vtWaeUcACokbXzybdDypEzgTc7R5iALmJeHTdOKgiI4BjCpKj_-aqsQvOimyeYpMtULDf-UbZiDHJRV7CAbTF1271IBppiqINnWaMkL8Y875jFrzgqMpAmBV74UTGo9fItX2hcEZ4RLKyJdOL3bqZkQejn6uixgS1FRHh84A8Mb53xmmnZPbL3PAihsWtAipl52GmAZ6vUWTD76GQHQThBHOGwBqQ_STP1CxzGE8fVnAXfNAVAR-Hk14Vx8ykWTcPHWMg2H76gi3vihc3NabQ5CUoFnKip_8DFphclSkgu718Ofwi8D8Sr8GmvimV9Eyi113Klu2qD7knaQif53QLFGu0_Ihiy3n8blOiW3R7N3XAaIPwm6x3l6yeTJO6XaORKdasnAPZFJU7jYQFh5OLCGcA43wM_3ql6lbdVx6cOjSDovq-R732x5XIHDF_4u4FTBRlI3URGB26hcUITKorTaq4Jg5UKjdxfp6FHhHHvDxbgtYA21S1b0P62nRuQv-DNylJHvVABNUUa-WL9PKMUDUp-Xzn518ot9PrdJmtrucIvh40kmUqqp35D60UkiKhdzvuHBfnezUNIUYSY58_AzBlS6I2fpZJ2AwdKxKqOREZ8tl28IwoHmpB7cE3LDip8qn0inTDlHNvhjhTlfecqVvazfqDGnWknczltY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد.
@withyashar
😟</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/13462" target="_blank">📅 01:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=j8YAAMmXszMioYeV1hZgjmf9MUmSqO1S9pL35P91kKj-spnwSnDxS239y-GraUQSvcBIMfugl8kY-2kESABK5WLEMQE290mqJ4w4Ve_n2FFzAO7peDfPXzaZhaKoadLEOtl8ZJsm6VWDWwt0kVJ_MyQFm1hrdbEePmNrY7fWnp7-yxpCLiq24isA60Gb3r1y4FodJsXH9QjXfdP2-zZVPtS-w7xYyny0cvPOOcJ2S7uD-sfEJTiKsZkv2eaKZr_29qfpsm0fvqfufrMI6IdhdZDwXl4ceZZqqvoPkO2gjUCnAruswfarvvf3GUscuv4JPOOmb2WEsvcC7gz_wV4ZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=j8YAAMmXszMioYeV1hZgjmf9MUmSqO1S9pL35P91kKj-spnwSnDxS239y-GraUQSvcBIMfugl8kY-2kESABK5WLEMQE290mqJ4w4Ve_n2FFzAO7peDfPXzaZhaKoadLEOtl8ZJsm6VWDWwt0kVJ_MyQFm1hrdbEePmNrY7fWnp7-yxpCLiq24isA60Gb3r1y4FodJsXH9QjXfdP2-zZVPtS-w7xYyny0cvPOOcJ2S7uD-sfEJTiKsZkv2eaKZr_29qfpsm0fvqfufrMI6IdhdZDwXl4ceZZqqvoPkO2gjUCnAruswfarvvf3GUscuv4JPOOmb2WEsvcC7gz_wV4ZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
چهار جمهوری‌خواه به نفع آن رای دادند.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/13461" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
