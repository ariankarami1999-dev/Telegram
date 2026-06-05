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
<img src="https://cdn4.telesco.pe/file/p3vWM1xK7feOaqLbHVAzHegouR5ECJzbnjlpbFbuaYsOusk_oRrLiYUxXju_4Picg_KzHbUtLaLztJ3f4ecdwsxYzVHhVXdwj2w9RSYIGvZc0Gj_l-JJppKWHOvlWzTatzchZZ03Twi4uGikmqj8Go-zkRFr09F4FyljjX-D2h881hjlOgjOOZ6lExzoq04pghcGu6EaWifYXR1fAbU-iTJmsk15KKksncSYMUSFq2WYpsBVrI-2vq905xrN14ZziKZypvosKvC8f6MpETHZYO59JzDjeADgXAiWfCYzQ3uehdPXCE8mzzvYJG3rEYGyNJd2rzi01ofxZRXpTbkxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 289K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 17:57:44</div>
<hr>

<div class="tg-post" id="msg-13556">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سنتکام:
ادعای نادرست: ایران ادعا میکنه که به سمت کشتی‌های جنگی ایالات متحده در خلیج عمان تیر هشدار شلیک کرده و کشتی‌های آمریکایی رو مجبور به «عقب‌نشینی» به سمت اقیانوس هند کرده.
حقیقت: نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی ایالات متحده حمله نکرده یا به سمت آنها شلیک نکردن. انجام این کار نقض فاحش آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره مداوم علیه ایران رو به طور کامل اجرا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/13556" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13555">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/13555" target="_blank">📅 17:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13554">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/13554" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13553">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس‌جمهور لبنان، ژوزف عون، در مصاحبه‌ای با سی‌ان‌ان ایران را متهم کرد که در رویارویی با آمریکا و اسرائیل از کشور او به‌عنوان یک برگ چانه‌زنی استفاده می‌کند و گفت: «این کشور، کشور شما نیست.»
عون همچنین افزود که مردم لبنان از جنگ میان اسرائیل و حزب‌الله خسته شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/13553" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13552">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است و جای نگرانی برای شهروندان وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/13552" target="_blank">📅 16:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13551">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/13551" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13550">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/13550" target="_blank">📅 15:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13549">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmWHIvxBSbvOQH0dP6QIEFtdN0WgMaOY1cZUsDSggvhO9NJ4GMivu5En4sqNG9lPPbWA7uLTEEZWUg2iSYB6YK1eyzf61M9VGkrKlQ-piZN97_wbq65AbvyttEKQF5TIT2diOIaxvNYOXLrFccXoj0GYgtK4noehRPjGFcLb6rB1IDElW6vqbYmn7R5sUXs46ndxLdQijU5tT982ROmX68tQsRgu55UAKjHchrlvLzvUCrHIJG04TJuY3fgHTeoO-QYIX4FGPo3wolq5-n2KvLLLTwFTvBXRvqvLPYVqexLvnwUHVw6HIHnDSHNb6_H1wse1yvq9ixBeeZAx94icsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️حمام خون در بازار کریپتو!
بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است.
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/13549" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13548">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=uonIwMOzWIj4XFvvlNmkp8KflBTUW22HeJi4KsSs2bH2DwFQ8iIFGmAxg-9S6E1Vi-q0ECVLlnhnJ5s8UhVNYg58GGRqinPIx44ndgUBQjRoerAPej2qaS1qE3XpnCbriSg6uw7ESrNPW_IaHOgO-eqkkZZ9ZshmnLzdNgDzjrFwUFdzBF9-9tfVHxR1pTihHdpGT6Q8vh6ykEkVs_XBxfDYwwXjrwzwxwEiOVJpJ2z1mxMClFUfo09mukWzmrwshBuhP7JTrgNmqjUEKWkj16AtegnC6_ScgG9WLI3B8sHtxi7_9HjDInla5TB3laM-yrK2dYeLeYWFCa1XI8WmlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=uonIwMOzWIj4XFvvlNmkp8KflBTUW22HeJi4KsSs2bH2DwFQ8iIFGmAxg-9S6E1Vi-q0ECVLlnhnJ5s8UhVNYg58GGRqinPIx44ndgUBQjRoerAPej2qaS1qE3XpnCbriSg6uw7ESrNPW_IaHOgO-eqkkZZ9ZshmnLzdNgDzjrFwUFdzBF9-9tfVHxR1pTihHdpGT6Q8vh6ykEkVs_XBxfDYwwXjrwzwxwEiOVJpJ2z1mxMClFUfo09mukWzmrwshBuhP7JTrgNmqjUEKWkj16AtegnC6_ScgG9WLI3B8sHtxi7_9HjDInla5TB3laM-yrK2dYeLeYWFCa1XI8WmlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود حجیم جنوب مركزي تهرانه  همين الان
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/13548" target="_blank">📅 15:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13547">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بر اساس نظرسنجی‌های معتبر آمریکایی حمایت افکار عمومی آمریکا از پایان جنگ و حرکت به‌سوی توافق، از ۴۹٪ پیش از جنگ به ۶۸٪ در آستانه توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/13547" target="_blank">📅 15:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13546">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه. @withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/13546" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13545">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فیفا: نقص سایت باعث صدور بلیت‌های رایگان شد
‏فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/13545" target="_blank">📅 14:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13544">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/13544" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/13543" target="_blank">📅 12:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13542">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد و از اسرائیل نیز متقابلاً خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت این کشور احترام بگذارد.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13542" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13541">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اصابت یک پهپاد به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13541" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13540">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل شب گذشته به قطعنامه آتش بس در لبنان رای نداد
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13540" target="_blank">📅 09:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13539">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">طبق روال هر روز صبح حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13539" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13538">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL00r_x6xF_ubztutT7lNj5gMEknldpN9ykUQzd0dFmpAOJ7haN-FZqcXY-uFBJLrhJXwC59CLxGNrxu3At6R4qmXoh_tsfPbxKC01pFEOdW2uYwLdVJlTNRhEGVSiuYVb9xi6Qvd_aBXic7GBTtMmFd85PtLk0kkZDUruS3QODRMcmT47Gi7nVWiWMu8RhWwTNXiI2dOA3BTzz_AvQE56GfSF1fmy7un58bltKrb0vNpinHF2lXk01mWBT-I2Az0gK_y1_8H6Y-CeEvxcXjbcowNxTydVzx4uEBpbYq45L7IAqT5zguZ7r8QzZRvpaVS-_-sOps7KAolj7TPbcJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای زیادی برایم فرستادید که از پدافند سنگین ۳-۴ صبح و چندین انفجار در تهران ولی مدرکی نیست… فقط چندین عکس از اینجا برایم آمده.
آزاد راه پردیس به تهران
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13538" target="_blank">📅 09:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13537">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امشب بیداریم ، ردبولم میزنیم
🤣
💥</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13537" target="_blank">📅 09:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز: بامداد جمعه انفجاری پهپادی در بندر الفحل عمان رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13536" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نورالدین الدغیر خبرنگار الجزیره در تهران:یادداشت تفاهم در مرحله نهایی خود قرار دارد
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13535" target="_blank">📅 08:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13534">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/13534" target="_blank">📅 01:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ می‌گوید دولتش بررسی کرده بود که نیروهایی را برای تصرف اورانیوم ایران بفرستد، اما در نهایت این ایده را رد کرد چون خیلی پرخطر بود و می‌توانست به تلفات آمریکایی‌ها منجر شود، و این موضوع را با مأموریت ناموفق نجات گروگان‌های کارتر مقایسه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/13533" target="_blank">📅 01:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ ۲۵ بهمن ۱۴۰۴: میخوام با آیت الله علی خامنه ای دیدار کنم.
۹ اسفند بخارش‌ کرد.
ترامپ ۱۴ خرداد ۱۴۰۵: میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
چه تاریخی بخار میشه؟!
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/13532" target="_blank">📅 00:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: ما به ایران رسیدگی خواهیم کرد، و به‌محض اینکه کارمان با آن تمام شد، در مسیر بازگشت، برای مدت کوتاهی توقف می‌کنیم و به کوبا رسیدگی خواهیم کرد… باید از شر این نظام خلاص شویم
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/13531" target="_blank">📅 00:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: برنده این جنگ ما هستیم حالا چه روی کاغذ چه با قدرت نظامی
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/13530" target="_blank">📅 00:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/13529" target="_blank">📅 00:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ : من دنبال عملیات مخفی برای گرفتن اورانیوم ایران نیستم اون اورانیوم عملاً دفن شده و از بین رفته
اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران؟ نه من نمی‌خوام جیمی کارتر باشم
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/13528" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:
راستش نمی‌خوام با آیت‌الله دیدار کنم، ولی اگه ببینمش، برام افتخاره. با احترام هم باهاش رفتار می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/13527" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13526">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak</strong></div>
<div class="tg-text">عمو یاشار اتاق جنگ نمیری امشب؟</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13526" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13525">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:
من در امور امنیت ملی خیلی تجربه زیادی نداشتم، اما فکر می‌کنم واقعاً کار خیلی خوبی در این زمینه انجام داده‌ام.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/13525" target="_blank">📅 23:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">منابع عربی:ظاهرا چراغ سبز برای بمباران حومه شهر بیروت گرفته شده است
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/13524" target="_blank">📅 23:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح هم اینا برن، طول می‌کشه. این زندگی واقعی هست و رؤیا و خیال‌بافی و وعده‌وعید نیست! حتی مانوک هم گفت بعد از مذاکرات تازه بازی شروع میشه، پس ما اولش هم نیستیم.
ولی با من این مسیر رو راحت‌تر از تمام حالات طی می‌کنید
❤️‍🩹
🙌🏾
ما بقی بازی سیاست و خبرگزاری‌ها و مارکت هست که ما هم به ناچار توشیم و انتشار می‌دیم! ولی این اخبار به هیچ وجه نه حرفه منه، نه کلاً تأیید می‌کنم؛ چاره‌ای هم نیست، این مسیر باید طی بشه!
از توجه شما به این مطلب ممنونم.
دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13523" target="_blank">📅 23:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فقط‌منننن خیلی‌رک میگم عمو ترامپ ۴۰ تا ملغ میزنه اخرم نمیگه
😁</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13522" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد @withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13521" target="_blank">📅 23:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13520" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13519" target="_blank">📅 23:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13518" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">پدافند سمت وزارت کشور فعال شد الان</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/13517" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13516">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13516" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13515">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAMIR</strong></div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13515" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال 12 اسرائیل:
مذاکرات به نتیجه نرسید، آمریکا تا آخر هفته پاسخ میخواهد و با ایران اعلام کرده یا توافق می‌کند و یا درگیری از سر گرفته می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13514" target="_blank">📅 22:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13513">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EduYLCsBu_3hkZ8oOpWGkaYP_dPYitRDVIr2udQyRymAwimDn5ftT8qF7STHtnWy4_1X37_l2XZuJpnbbaUYOI8TFrUv0B8fI7Nv26tw6mvrc4kKZNVrCoNHnrUOJlpR6jZBUDRn1aA3WXzFiu7rsfNGK6GTNIlfqCtNWYX0hYQEvc3SK8g-SuGpU-2XJgTN8SG9mYvQw302VhEUzi7BUbnYn1xvNhT5HiSXdHG0Rb4KXsMG6HgveFin-7OCCDapq9poCWJqRkvdyBjSJb3dJ9kggE2uB8o_vZyhdhDZCsS3cqUJl4G3UIplndn8WynKG0dMGDr652rHx2aBempgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده هشدار امنیتی برای تمام کشورهای خاورمیانه صادر کرد
دلیل این هشدار محتمل بودن درگیری اعلام شده و از همه شهروندان آمریکایی خواسته شده که نزدیک‌ترین پناهگاه را پیدا کنند
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13513" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBYCDYzUqszgmFF9qw0WiIZeq0QSwMgDCViq5m53ntyoiR2OXZBw81jg6Cl5392NZDYVzU8vt2Dg6_uENbr7UjB2ipyPyvbQ4m2QNSHq3dG8Lrdqx09Lpw9M7ZeRncFo84dYHrzCLD2tj6TfpVBPCg1Tnax3Qjir9MOka9AG7O3bl3SErnXHdyIp0iV67RVe7tAKL4YvBdWtugA-dsZ9LlWNYp38Hu6LS9udKUKBU-y6ehc_7-3SPfdMCxyhXULR9mjhHul6Shl5sdLYFgh4y658KnZaR-fzZYt1HU5s-yErcwfzlfGy96cA-iHcPdN8fZrdgpYB-bmnZWTCpucVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان و دخترش کشمش
🥴
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13512" target="_blank">📅 22:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13511">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13511" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13510">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سفارت ایالات متحده در اورشلیم هشدار عدم سفر جدیدی برای اسرائیل منتشر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13510" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13509" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13508">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای رویترز بر اساس داده‌های حمل و نقل: صادرات نفت ایران به پایین‌ترین سطح خود در حداقل ۶ سال گذشته رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13508" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13507">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کانال ۱۲ اسرائیل: واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13507" target="_blank">📅 21:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13506">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQzGecdJbhMC-BwdwqrUay42iamrM0YzRIV7O7anEKBR85s-_QyKt--Uhe5c-qm-KVNSx6_xmQqUEDfCIJrg_w5ukWsinnm9GabQuLDWkq06JOpZIqU0gXF4MR75DeaboIr5Qf_1MkgIFTFpazl_jNiBQ-dgEG8C9165UZ65B2fRvYuymSje4ISP1DrQw0AMk61Wos22ds8wJ7gPiVTnGpojkdo-9iHkZfPUDJgmE2D4EH8qgab_926TChLcCvh41od9tHLHkEjw3Gw7M7wGy_aOhDQzf91CmlCe3z7u9Fc4Pfe33OLZtbV74BoQT_IAcl3aKC9T-7RiOowFS2zoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل :
اعضای ارشد امنیت حماس را ب درک واصل کردیم
این اعضا وظیفه شون حفظ امنیت سران حماس بود ولی خودشون حتی نتونستن امنیت خودشونو تامین کنن
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13506" target="_blank">📅 21:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13505">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خوانندگی قیصر برای کودکان میناب در میدان امام حسین
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13505" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13504">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twUhrCpnoFrSjceIt2YVxmve4wWMIeuTIbFoVKbD5s5qSAnOXjLyULeRjH0Ri7fPGQJ2Dhq5PF9mZZFVn-XbOFu61VVmun4rGYxxVE_AltEiUlO3z3onelTo8TJRAkUlSj84AunDuFAY66njvAY0McPMTSPU8qJMdNyj8hH41GF0pJIVUH9cJ2n_v__HJlXY_ZvpoHYe_vMikt0x4eGvfhLlNZ7u5Ti8mbbsfCy0ugK-RWiqpjXmiPjjOQUBoPHA6HCK5GG4FNexUbhqD3fHSpGYe0rQlOmr4gYNucjPm-fAEx7ZpOilcwswAt-S1JjWstBSGdTBLy9_e6gqE2aPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها سردار سپاهی که امروز تو مراسم سالمرگ خمینی حضور داشته:
محسن رضایی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/13504" target="_blank">📅 20:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13503">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">@withyashar
قیصر</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13503" target="_blank">📅 20:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13502">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=NG23OhSB-0I_GWw1Qi2-NCHtwJytI8HM2kTW8uEEHbQWpOBFZlvXdTA7saclq9-vlHvLRdWUC8bXmjJ_3DqSxqhSPbgL8bJ8pQkE1BNGjfR592xVvggUMPAd-mukgKbSLO2DSXPEAHmhXnTg8hh9vjDmwSa7jVUP8cSujHUTGwwt44juiH5tAF7r82Ii7eIwqon3T-sQlDi6Hq2m4vnvoJKr1KaRrtg4DDzqMfGiwehCihafz27AyVYRZpFLKk4HxbdwJ0gASJmor5XIDiWhQ2d2Yyc4yGyoaZZmc3HwGNAD6wW0rHjM9HuN8AnJZh7wDFNn_q7LTScNR126KfwUKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=NG23OhSB-0I_GWw1Qi2-NCHtwJytI8HM2kTW8uEEHbQWpOBFZlvXdTA7saclq9-vlHvLRdWUC8bXmjJ_3DqSxqhSPbgL8bJ8pQkE1BNGjfR592xVvggUMPAd-mukgKbSLO2DSXPEAHmhXnTg8hh9vjDmwSa7jVUP8cSujHUTGwwt44juiH5tAF7r82Ii7eIwqon3T-sQlDi6Hq2m4vnvoJKr1KaRrtg4DDzqMfGiwehCihafz27AyVYRZpFLKk4HxbdwJ0gASJmor5XIDiWhQ2d2Yyc4yGyoaZZmc3HwGNAD6wW0rHjM9HuN8AnJZh7wDFNn_q7LTScNR126KfwUKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حظور قیصر خواننده
لس آنجلسی در جشن غدیر
🥴
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13502" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13501">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/13501" target="_blank">📅 19:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13500">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">داداش این خاننده دوزاری لس انجلسی که اوردن ایران پشت پردشو تو باید بدونی دستت تو موزیکه
پتشو بریز بیرون این عرزشیا عر عر نکنن</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13500" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13499">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد،
زودتر از آنچه فکر می‌کنیم،
سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13499" target="_blank">📅 19:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13498">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس با اسرائیل را رد کرد
شبکه المنار حزب‌الله ،گزارش داد که دبیرکل حزب‌الله لبنان گفته است که این گروه از جنوب لبنان عقب‌نشینی نخواهد کرد.
نعیم قاسم در این بیانیه گفته است درخواست این توافق مبنی بر خروج نیروهای حزب‌الله از جنوب لبنان، در شرایطی که این منطقه زیر آتش قرار دارد، به معنای "تسلیم شدن، شکست و تحقق اهداف دشمن" خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13498" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وای‌نت: موساد در اقدامی با هدف سرنگونی جمهوری اسلامی، سلاح‌های ضبط شده از حماس و حزب‌الله رو به کردهای مخالف جمهوری اسلامی داده بود.
سازمان اطلاعات مرکزی آمریکا، سیا هم در طرح استفاده از نیروهای کرد به‌عنوان بخشی از تلاش گسترده‌تر علیه حکومت ایران مشارکت داشته. این طرح در نهایت پس از فشار رجب طیب اردوغان، رییس‌جمهوری ترکیه، و در پی هشدارها درباره خطر گسترش درگیری منطقه‌ای، از سوی دونالد ترامپ لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13497" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOac7SHQQC2HG1rGGYFseQpbNTYrxu6Riq852KB3GsKdSn_zWyuGeshGRvOWyZWn9yBnjC9yGW4OsbtTpivAjwxIhd6CjMrLbXZjwPuF9yuY_x3JlDZRTFHTQZh6vBdgHyekZc0SOKJuo5xTBPFOjzHtgwyvHRomYWghGyi_1NSY1w0LOkMYov3kAtDQ2S7Fk_WLngGI5zWyR111JbRsz2Fhy0OGEI2hSdvCYBKctpGvwgA50eGoVvksmi1q4mLFP_CQxuG0k6d2I76d64jZZr4qqQYAU00YIwSHuqii8r-oGQqjPJBWI6TAVibLpk_kP6kAhZoUo-Kbfec80lx0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای کاتولیک یک جن‌گیر را پس از ارتباط دادن مشاهده‌های یوفو با فعالیت‌های شیطانی برکنار کرد،.
جن‌گیر مشهور و قدیمی کاتولیک، استیون روزتی، گفت به باور شخصی او بسیاری از مشاهده‌های یوفو ممکن است ماهیتی شیطانی داشته باشند ! وی علاوه بر آن روان‌شناس نیز هست. به همین دلیل وقتی او درباره یوفوها صحبت می‌کند، سخنانش بیشتر از یک فرد عادی مورد توجه قرار می‌گیرد
اسقف‌نشین کاتولیک واشینگتن این اظهارات را مغایر با رویکرد رسمی کلیسا دانست و روزتی از سمت جن‌گیر رسمی برکنار شد و همکاری کلیسا با مرکز معنوی او نیز قطع گردید.
روزتی بعداً عذرخواهی کرد و بر تبعیت از آموزه‌های رسمی کلیسا تأکید نمود.
این ماجرا بحث قدیمی درباره ارتباط احتمالی یوفوها، موجودات فرازمینی و پدیده‌های ماورایی را دوباره مطرح کرده است
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/13496" target="_blank">📅 18:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13495">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMniL6302UO9qFA-ChVjTqsN_KBoBtayyIgo4OVnZOorrwf5fO99x2bhWU-eyJyMmyPDSshMpHhPI-st0GDD5kDw9bWEiRHxjmYJg5yOCn1xxLFEQ9MB0c-9lFBD1g14c-opEuxTPz-w7Z96-wFx1Bg_zzsyShQ9SVc3qE5EZAMWp8P7tTDtJzahlu-QfEWg5L4t5gRFW0IruuovUhdweDY2MdO3V0uj9GFCR9KDDSWvcokxULlJpxkMJhi-DZ9M5t6MAT22J89oWoOBfoIGEQXsuknMl5EyTFAbrRONaGpaHOP88QoumvgMPx4zKMaoK_Ou7rvoDEfMDVttSQz42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم رو بردن تحویل بدن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13495" target="_blank">📅 17:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13494">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپاه: اسرائیل فورا حملات خود را متوقف و از مرزهای اشغال‌شده لبنان عقب‌نشینی کند
هیچ آرامشی در منطقه بدون عقب‌نشینی از مناطق اشغالی لبنان برقرار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13494" target="_blank">📅 17:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اصلا جان بر کف و جان فدا برای ما بود اونا گرفتن
😃
🤣
اون عرزشی ها کپی‌کارن زبان فارسی‌هم میراث ما هست نه اونا ، شاهنشاهی هم میراث ما هست لغت شاه هم کل دنیابگین میگن شاه ایران !</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13493" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مردم به ایلان ماسکم دیسلاک دادن موشک هوا کرد
😁
شما توجه نکنید پیشنهادم به بعضی ها اینه که یک جعبه شیرنی‌بگیرن و با خودشون آشتی کنند</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13492" target="_blank">📅 17:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0dBIzGh4cBWynnGJ48Q8BMUJRstjtUCoZwPHO-RobMYB8qIBRxdL7WZCHDCquRiX90GttYLD4svuGGyNgPqMQLnHwR93rONxA-OdEqiRvvQxFj-P8M7qrqUyWGRZ92rVTomtiSHwZxnv4tJ6uw-oYHWuS5zLge4zyX_-aCaAsVTAhqUc6Tfq6re5n33AZTcztE6MnsNAytJy2xXX7DDeyeF-HvKwZXNpPBkS-kQKfGhQa5RD3K9yerZh-sYNfor8nzok7VO3t5XV3PqaHuZKKYwFIbBE7iAhpnjL7iTMvzQAIrJ0vlCLBOxiVA9xcEYNRJDFYoRBkzR3ooijJlAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13491" target="_blank">📅 17:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13490">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌹</strong></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13490" target="_blank">📅 17:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13489">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=hJbSCZygkd5ST2jjMDWQSDlfR7l1S12VlJjRm05GbtvCJVcUtCR5VIOZ_mPVGa-Hbah11OSxmsb09LCy81E86FCqtEKtbu9nCxUkkMt6XeMFBYAt5GsY8FoyEeQ7xuEJH5DLQBvxJ5cT_xljt6dj8FkA31qk38wQhVg4xt7LNIbeXiBq3Dx0Kp_ouFps-PmO9d4OWmAmh8gJpkKhgeN9NVxGfdlOna_VX1mqpg8Po4zOYt_x2kPleE3uva4SfhBjRxxNXutAbHzetNjUdHSeyZxQFGshXh71YbW2VMmdfNI9Wrw6i8huZEb_d-FFFRrMf-bU17urPxli1frkEnthww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=hJbSCZygkd5ST2jjMDWQSDlfR7l1S12VlJjRm05GbtvCJVcUtCR5VIOZ_mPVGa-Hbah11OSxmsb09LCy81E86FCqtEKtbu9nCxUkkMt6XeMFBYAt5GsY8FoyEeQ7xuEJH5DLQBvxJ5cT_xljt6dj8FkA31qk38wQhVg4xt7LNIbeXiBq3Dx0Kp_ouFps-PmO9d4OWmAmh8gJpkKhgeN9NVxGfdlOna_VX1mqpg8Po4zOYt_x2kPleE3uva4SfhBjRxxNXutAbHzetNjUdHSeyZxQFGshXh71YbW2VMmdfNI9Wrw6i8huZEb_d-FFFRrMf-bU17urPxli1frkEnthww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایت شهبازی از کار
😂
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/13489" target="_blank">📅 17:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13488">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad Jalilzadeh</strong></div>
<div class="tg-text">اقا ری اکشن کوچکترین تمرین هست برای پذیرش دموکراسی
وقتی یه عده همه ش دنبال کم و زیاد کردن ری اکشن هستن و دنبال اینن که کی چه ری اکشنی زده در آینده ی ایران چطور میخوایم همدیگه رو تحمل بکنیم و باهمدیگه حرف بزنیم؟
همه ری اکشنا باید باز باشه و کاملا مخفی</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/13488" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13487">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی…</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/13487" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13486">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چند گزارش ساعت ۱۵:۵۴ دقیقه محدوده شمال شرق تهران همچنین نیاوران صدا پدافند شنیده شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13486" target="_blank">📅 16:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13485">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی را در برابر چشم جهانیان قرار دهیم.
@withyashar
وی به این موضوع که ورود پرچم ما به ورزشگاه ممنوع است و چه راهکاری باید داشته باشیم اشاره نکرد.</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13485" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13484">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIppLyq98t-Lw942jpMnXJI7Fu6-26c8wz0OYa8WKG4bPfh28p0oQC62-p9xmXB5ms4dYccQAhk0IgNXFOP_RAw7LnL3evi3XK0QgI4OGOAaNetd3e0Qht5mxo5U1Xibwznb8msMz1uwiTBN4QfBqpC4D-uUGIFQp9y3BDpSyaWEWYGat7Jq0-1FTPFbIOw94nd_N6V_BKl-nbd2pkWD-qW95gpwRhg2DI5px3GXl1IohMoK9WfumnKUWlzrucSDEfm9Brnbcs1YJ0R_A9CUbkgPm-UiyEPq-whsGem4Lsjpx1ODLcL6Ui78MUheMKRY3Ougk4kGr2tdOSrTSFE2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : سازمان تروریستی حزب‌الله گلوله‌های خمپاره‌ای شلیک کرده که به یک موقعیت نیروهای سازمان ملل اصابت کرده و در نتیجه یک نفر از کارکنان سازمان ملل در جنوب لبنان کشته شده است
شلیک‌های حزب‌الله نیروهای بین‌المللی را در معرض خطر قرار می‌دهد و به کارکنان سازمان ملل که در منطقه فعالیت می‌کنند آسیب می‌زند
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13484" target="_blank">📅 16:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13483">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نعیم قاسم، رهبر حزب الله: نتیجه مذاکرات دولت لبنان با اسرائیل شرم آور و پوچ است و اونو بطور کامل مردود اعلام میکنم.
تا زمانی که تجاوز ادامه داره به هر جایی که تصمیم بگیریم و بتونیم حمله می‌کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/13483" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13482">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: در وسط مذاکرات پایانی برای پایان دادن به جنگ هستیم
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13482" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13481">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK7NvrCDVWRZnW5UHYLn4Kqj2GekfMk9132ayZgX__lPPuclo5MZ1A1GxL-H0mXAXkzZy7G-gSKsSjrbJppixzuUcHBG8_-VU0zI-qFniyw2g2paX-fbyA5PpAQvQdZDV8HLEfz-H6WVlYSkWHDzZN9JpSRswjDvxzqNAQNZMAIS4YfVpF4ym2lMbsO5Crgmg4hIV8EyrPU8fqfLebQRpvfAaUSHKWANQH2dnie72uFh_5V3_NvZPV2_-vhlLk5e1W0OVCnMPePrIiAjtMAtN23EJzOXR6AAHXjhf3cEeB1qenJIaePDwW0WtqLfk8BuwxUDCEpKBbM9JNzzUJXLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عکسی از نشان‌هایی با نماد جمجمه به سبک ترامپ منتشر کرد
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/13481" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13480">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIBK5T3kAMkBrlslYQLx63YggaBRFirf0JrEiowtCliGJzcLr2wojQa9gdpdVJQUJBYuDoLLpVFKxdFUjuo6CrfWTujNo_HvCMGRtylHZaEKXOqFu-9sW4GeLw7VCgaJv0yAb4iF2oJc6Xgwl6oKFZpNlX0HCCLlWYTfrFFeZJYGrAt8aghaSlbtrBjxKfjb0bWBl7ER6N4Vt_JORKrOlPm32BYbh83wM_hBSGd6jCmG8PHMcJ7Xpcb7K79LBoG7S-ih4vFEwEmDJHYmL0qFmhrf43A3GiUfXDR1VqMTH9jH1CG16ZPo9-XtEgU8cNEdbZvhpTqB6jYOgtbQLD_mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیروز، در یک رأی‌گیری بی‌اهمیت، مجلس نمایندگان با رأی ۴ جمهوری‌خواه بد و همه دموکرات‌ها، تلاش کرد اختیارات جنگی من را محدود کند؛ درست در میانه آخرین مذاکرات من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آن‌ها می‌دانند وضعیت مذاکرات در چه مرحله‌ای است. دموکرات‌ها با چیزی به نام «سندروم جنون ترامپ» هدایت می‌شوند. آن‌ها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یک پیروزی دیگر از میان پیروزی‌های بسیارم به دست بیاورم. آن چهار جمهوری‌خواه، ماجرای دیگری دارند آن‌ها اهل خودنمایی هستند! باید از کار خود شرمنده باشند.
MAGA!!!
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13480" target="_blank">📅 14:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد. @withyashar
😟</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13479" target="_blank">📅 14:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13478">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اکسیوس :  یک شکاف رو به رشد بین ترامپ و نتانیاهو در مورد آینده منطقه در حال شکل‌گیری است.
بر اساس گفته مقامات آمریکایی، ترامپ می‌خواهد تنش‌ها را کاهش دهد، درگیری‌های جاری را پایان دهد و به دنبال یک توافق دیپلماتیک با ایران باشد.
در مقابل، نتانیاهو به نظر می‌رسد تمایل بیشتری به حفظ فشار نظامی بر ایران و متحدانش، از جمله حزب‌الله، دارد.
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/13478" target="_blank">📅 14:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13477">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فیلم جدیدی که حمله هوایی آمریکا به پل B1 در کرج، ایران، را در طول جنگ نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/13477" target="_blank">📅 13:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13476">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۳ اسرائیل: «کابینه امنیتی اسرائیل امشب ساعت ۱۷:۰۰ تشکیل جلسه خواهد داد»
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13476" target="_blank">📅 13:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13475">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وال‌استریت ژورنال : آخرین پیشنهاد ارائه‌شده از سوی ایران نتوانسته رضایت کامل دولت ترامپ را جلب کند و هنوز اختلافات اساسی بر سر برنامه هسته‌ای، سرنوشت اورانیوم غنی‌شده، رفع تحریم‌ها و آزادسازی دارایی‌های ایران باقی مانده است.
وال‌استریت ژورنال تأکید می‌کند که تماس‌ها و تلاش‌های دیپلماتیک همچنان ادامه دارد ، ترامپ همچنان به دنبال توافقی است که از دید او برنامه هسته‌ای ایران را به‌طور مؤثر محدود یا برچیده کند. در مقابل، ایران خواهان امتیازهایی مانند آزاد شدن بخشی از دارایی‌های مسدودشده و کاهش فشارهای اقتصادی پیش از پذیرش محدودیت‌های گسترده‌تر است.
اما مذاکرات هنوز زنده است و کانال‌های ارتباطی بسته نشده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13475" target="_blank">📅 12:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13474">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وال استریت ژورنال:
«ترامپ به مشاورانش گفته است که جنگ تمام‌عیار با ایران را از سر نخواهد گرفت، مگر اینکه نیروهای نظامی آمریکا کشته شوند.»
مقام‌ها می‌گویند حملات مکرر ایران فشار بر رئیس‌جمهور را افزایش داده و تردیدهایی درباره دوام بلندمدت آتش‌بس ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13474" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13473">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انتقاد مارک لوین از تصمیمات جدید ترامپ:
جمهوری اسلامی شاید نیروی دریایی و نیروی هوایی قابل ‌اعتنایی نداشته باشد، اما همچنان سپاه پاسداران و یک رژیم ایدئولوژیک دارد که شکست نخورده است؛ ما ملت ایران را برای سرنگونی رژیم مسلح نکرده‌ایم. رژیم کماکان در حال شلیک موشک های بالستیک و پهپاد ها است و هنوز مشخص نیست این تبادل آتش بخشی از مذاکرات است یا نه؛ هرچند در نهایت، چنین مواردی قابل راستی‌آزمایی نخواهد بود.
به نظر میرسد ما از نابود شدن سازمان حزب‌الله لبنان ممانعت می‌کنیم؛ حزب‌الله، قدرتمندترین نیروی نیابتی رژیم ایران میباشد که در 40 سال گذشته آمریکایی‌ها را کشته است؛ همچنین حماس به جای خلع سلاح، در حال تجدید قوا است.
این وضعیت برای آینده و پس از پایان دولت ترامپ، نشانه خوبی نیست. من فکر نمی‌کنم چین کمونیست که بزرگترین تهدید برای ما است، تحت تأثیر قرار گرفته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13473" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13472">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9960590f00.mp4?token=MrITK0UIuPmOsVRIkhKmQQnpuRGoDIBu3Mlu80GiqyZaVosrMHpsaTzXNTPAhW_q7HDfBSxpEoagHq-BGGd4SH2mwN6XRB8Lj6m4vybvUm7yw9P_amyErTYf93-c1LKdPL5UbUdVaCigiyp8q0CnUc5Mu0C_2XNGHFXbdSw51PYr9_jxZRyhLBH3hOELnJ7ybfo3DeUgQpa7o--xju-kh5uyupfupxIdYSZKDCcvbUWUtGgoj7fAVmpQWz-yhfPOtkW3JBLNMhyyk_DD1IPiDiP8LZEOZHsxgKgs7BG2msMsBRmPrVSky70wEHJF9BYi8Eys2Sth0DfXGrUt4wlr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9960590f00.mp4?token=MrITK0UIuPmOsVRIkhKmQQnpuRGoDIBu3Mlu80GiqyZaVosrMHpsaTzXNTPAhW_q7HDfBSxpEoagHq-BGGd4SH2mwN6XRB8Lj6m4vybvUm7yw9P_amyErTYf93-c1LKdPL5UbUdVaCigiyp8q0CnUc5Mu0C_2XNGHFXbdSw51PYr9_jxZRyhLBH3hOELnJ7ybfo3DeUgQpa7o--xju-kh5uyupfupxIdYSZKDCcvbUWUtGgoj7fAVmpQWz-yhfPOtkW3JBLNMhyyk_DD1IPiDiP8LZEOZHsxgKgs7BG2msMsBRmPrVSky70wEHJF9BYi8Eys2Sth0DfXGrUt4wlr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری نیویورک پست
: آیا آیت‌الله (مجتبی خامنه‌ای) همجنسگرا است
ترامپ: بله.
مجری
: واقعا
دونالد ترامپ: بله، و فکر میکنم خیلی احترام براش قائل هستند.
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/13472" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13471">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در مراسم سی‌وهفتمین سال به درک رفتن روح‌الله خمینی، پیام کتبی منتسب به مجتبی خامنه‌ای خوانده شد. در این پیام آمده است «نظام سلطه پادگانی به نام اسرائیل از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13471" target="_blank">📅 11:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13470">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13470" target="_blank">📅 11:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13469">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
@withyashar
🥴</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/13469" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13468">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :  شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.  برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود @withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13468" target="_blank">📅 11:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13467">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C70TR6v5iX3QeyClYdUqUHGPX0sBen1eM0r17tVkeqyolrnhZymNU7CFAN3kFFpJqKCXzsSKny1hOmfWVAOsrmdaA9o4FY-DhpBnuzGXryAMqSNkNZl54u_wx1glxIaujPn3dgDXimFVcirIjD1-VKxnJ_MT87vGXzGRM92BQFW89oMFhK-eECPCN-Madq3XjOQSCDy6r9F04PejnloS2KuY1X2AzMmq-7CsIlqUI7k5ZVHUEWPZWnXzvYXOQIy-Me7i84mzUn4E2C5LA2j-ASlmqRG9usDeLZn-3aZJYpvW3w4RJr052fk8mMGnajq0U2yGLOsTxf07651opfNGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد پیدا شد
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13467" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13466">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13466" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13465">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p24HEGc2uwQDGBARvCA06NIK2nsP_vwf-plXcH3RxkYeKJ4HLOUG58Q8WhZVMGm76zNBu1QEUKx0jyC8Al3pcdXqw6b9kdOQCUDLXX8OrOm4aZjoVacuw1sSHqYyUCHbw-A3q3EAh5in10dSLxwS-y7T2-qCO762nIL0xWi9mef8kRZWFqyfITzNZRHcxJ9NJUlq3I-GJprtOCBZUO60xCfCd9PaTjMrpbxRT4qjxnhyMUJltxJVR66L88-GvbKxLWyzJcM48baE38DBDFHN5cCixLJTDgryb-y6VwsIKbwgiaBNM8nQ8dZay7ECPtnRPafb3qI_MxxlF8q31wRYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/13465" target="_blank">📅 11:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13464">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مقام اسرائیلی: ایران تصمیم گرفته در صورت آزادسازی اموال بلوکه‌شده‌‌اش، بخشی از آن را به حزب‌الله اختصاص دهد.
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/13464" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13463">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جنگ ترامپ با ایران و اختلال در حمل و نقل نفت از طریق تنگه هرمز، ذخایر نفتی آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۴ رسانده است.
برای کمک به مهار افزایش قیمت سوخت، آمریکا میلیون‌ها بشکه از ذخیره استراتژیک خود را آزاد کرده و همچنین صادرات به اروپا و آسیا را افزایش داده است تا جایگزین عرضه از دست رفته خاورمیانه شود.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/13463" target="_blank">📅 09:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13462">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=LXvn5Jqi1TLj4T4fNfy8ivaXLuiz3-0t4C2GAA_zNToZYF0WHRJEpjUWd99n9YWfasZiy_-eGJJ-UHp5Bh4ijZlgweeOmKp_tkSMuyKqZP8iWwLJE04xrH9vb4QIxIZjeuHMAD7kAsEx1EpHGyBj-n6kRkSa4tHQaqKDl9mPCK2UZmThJh9AG-9SGzWzXizlxVK7Jz4kaZ6eTzbqz-4OMmJbhZVBnZKX0N9HBTyzahq4_BFrKmfkVUtZedFx8SobMZzrpldg2HHNd2dUudoksJsylglG8sTJ-t_JTca5NPnm5kKTeGnwYxT9lY_bORI2KU0kkTxEajhM_EKDkbQ_nLab72jZqRteK8Zs-r0UniYebk4qmmDImOa5k98s7qgf0kkPcVj2V2KqLCsdzClC8dXeRdj5qme8COd2Pj1NRW7kaAvXwc2CVwF7XbHKgkKrnkJe8SVTmiUHj3aGhSOx1FjCjTSBxO1pBtO1WBBC7wu5VCD7Uuxbd8za5FescD8x8_dzdGA32VxhKq1Wlk_-ihPeTGjm3IVb--GuOdnTqhfqFx54-wpbnQ9NqEx0KUNFwcXfNvg5h3s7B-7aHEPCmmJGBhIJrUwLYgysji8gPCvdx0VZdM9XOMdFda8uz_CJfkMKSdFL0jlLlaSJaT6s3MPSqBwvLhWkWCYTTzUGiNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=LXvn5Jqi1TLj4T4fNfy8ivaXLuiz3-0t4C2GAA_zNToZYF0WHRJEpjUWd99n9YWfasZiy_-eGJJ-UHp5Bh4ijZlgweeOmKp_tkSMuyKqZP8iWwLJE04xrH9vb4QIxIZjeuHMAD7kAsEx1EpHGyBj-n6kRkSa4tHQaqKDl9mPCK2UZmThJh9AG-9SGzWzXizlxVK7Jz4kaZ6eTzbqz-4OMmJbhZVBnZKX0N9HBTyzahq4_BFrKmfkVUtZedFx8SobMZzrpldg2HHNd2dUudoksJsylglG8sTJ-t_JTca5NPnm5kKTeGnwYxT9lY_bORI2KU0kkTxEajhM_EKDkbQ_nLab72jZqRteK8Zs-r0UniYebk4qmmDImOa5k98s7qgf0kkPcVj2V2KqLCsdzClC8dXeRdj5qme8COd2Pj1NRW7kaAvXwc2CVwF7XbHKgkKrnkJe8SVTmiUHj3aGhSOx1FjCjTSBxO1pBtO1WBBC7wu5VCD7Uuxbd8za5FescD8x8_dzdGA32VxhKq1Wlk_-ihPeTGjm3IVb--GuOdnTqhfqFx54-wpbnQ9NqEx0KUNFwcXfNvg5h3s7B-7aHEPCmmJGBhIJrUwLYgysji8gPCvdx0VZdM9XOMdFda8uz_CJfkMKSdFL0jlLlaSJaT6s3MPSqBwvLhWkWCYTTzUGiNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد.
@withyashar
😟</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/13462" target="_blank">📅 01:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13461">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=OXyEm_jSjqm54vZbwPm821mEK82Y9U2vMg-7GGv_qNtU4KVVImljuAJ2bkShB2rzprLDee47x1nT2lk4SEnpsJ0GawpmlVUCD3zHW48w_XStmCRyYAdSOqtSwe0KWdOKGYH2t9e6RgALo__lrHBtGI3nOnsh4madkCivgKGkpoiFB9vM748RUxq7oRMdx45i1beorTjvWPrMnJyapoi57jR1svQlivagGXug2CBdOa0PCtJeBnMvyQA_kW5DfhEX27Zn90XtL-UrOEr_kD4_-Y-irkciTlwlz5aMtWXXr3JZKNDC-udMjmvwOXyyv__o82THDcd9Xa5r1LGwaZ95PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=OXyEm_jSjqm54vZbwPm821mEK82Y9U2vMg-7GGv_qNtU4KVVImljuAJ2bkShB2rzprLDee47x1nT2lk4SEnpsJ0GawpmlVUCD3zHW48w_XStmCRyYAdSOqtSwe0KWdOKGYH2t9e6RgALo__lrHBtGI3nOnsh4madkCivgKGkpoiFB9vM748RUxq7oRMdx45i1beorTjvWPrMnJyapoi57jR1svQlivagGXug2CBdOa0PCtJeBnMvyQA_kW5DfhEX27Zn90XtL-UrOEr_kD4_-Y-irkciTlwlz5aMtWXXr3JZKNDC-udMjmvwOXyyv__o82THDcd9Xa5r1LGwaZ95PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
چهار جمهوری‌خواه به نفع آن رای دادند.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/13461" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13460">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">داداش اون بحث خیلی طولانیه اون میشه زمان ریست فکتوری طوفان بزرگ ( که با داستان خیالی نوح میشناسید ) تا اینجا بدون که قبلش تمدنهای بسیار پیشرفته بود روی زمین ، باشه برای بعد از آزادی
😂</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/13460" target="_blank">📅 01:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from00:30</strong></div>
<div class="tg-text">درود ولی من‌میرملاس لرستان رفتم اونجا دیوار نوشته هست‌مربوط به 12000 سال پیش</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/13459" target="_blank">📅 01:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یاشار : دمت  آقا دایی ، مردی ، خواستم تکمیل کنم که عدد
۲۵۰۰ سال
به طور مشخص به
سابقه پادشاهی شاهنشاهی ایران
اشاره دارد، نه به کل تمدن ایران ،
تمدن در فلات ایران ۵۰۰۰ الی ۷۰۰۰ سال حتی بیشتر سابقه دارد
@withyashar
😁
🙌🏾</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/13458" target="_blank">📅 01:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/13457" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
