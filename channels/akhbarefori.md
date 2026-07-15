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
<img src="https://cdn4.telesco.pe/file/PDgrB4vGEfeYGq1eUfOS8P1nw22r5D6RAEDR2s8FAEq9ltpQtIvnFbdb4gZ3wDVVpmMn8WUjo503Z9TxtGJPd8YIJmZbN6X66I9LydBfwHSupY1KPXsx6ElPCyvndMtseNlgAga4hxgVjxMOfY3XDrR-X4mxM0PHbTvvb-0kjq_mKalwX9OTIcOo3TSmN55d4mqdtNyEbo0ZCEVbRb_e2nchR2ojI6_Kz1bn3SlXSdnENHL7j3k8F1r40Vqu6wYKbF8b0H9CTvw_pkdNwsBSRyKj0A9p0XCiv4pFq1hgb1P1lZ2QT8f0ZOV2qI1FhVE-8pHZaL0gRsq-25VBscbgbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-671495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
قالیباف: حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند
🔹
مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/671495" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671494">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قالیباف: برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/671494" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
قالیباف: همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/671493" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
♦️
قالیباف: مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قواست
🔹
همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند،…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/671492" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قالیباف: باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم
🔹
جنگ و مذاکره دو روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ، بخشی از راهبرد…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/671491" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
♦️
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔹
اگر قرار باشد ایران از تفاهم‌نمامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/671490" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
قالیباف: نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/671489" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/671488" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHOLv9iYoXVLcOzAcAm5wM1bfCw4MyjaSM9blB4uaCGmFcGS0VzyPWwWKBc_wDxX5AUtGscN2TkrlWNBMl_ewmf8NdAcMFZ-D80cHuDqFl-4d9Jpvv16z8_qPfilvRuvsoheVs2BeyhgKSDcxCCq9djTS3eVHckkjbmw4WmNFVhL_LKV5ZZcFtPgue7hFA1GFyHIq6cfMJjDOXJr-18zognCTn-g64P52JRHNAWotZeN5Oxyx4Ngu34NBArC4f-NNyf4P2sGMsPxTUpAG-XvsoB2IxE0Rxhqm_RUW2S5qlaq5GEAviOY0pwlhCH8WZCFhUZi_vqQrRzI3HxJDY9qYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، سلامتی شما بیمه است
رسیدگی به سلامت دندان‌ها مهمه و داشتن
بیمه تکمیلی مناسب
خیالتون رو راحت می‌کنه.
✅
در بیمه‌بازار
می‌تونید پلن‌های مختلف را یکجا ببینید و پوشش‌ها و سقف تعهدات را با هم مقایسه کنید تا انتخاب مناسب‌تری داشته باشید.
🦷
پوشش دندان‌پزشکی تا سقف ۴۰ میلیون تومان
👈🏻
دریافت مشاوره رایگان و استعلام قیمت
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/671487" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
قاليباف: ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/671486" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم/ ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم / باید از ابزار دیپلماسی و مذاکره…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/671485" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم/ ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم / باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
🔹
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/671484" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2aac84bd.mp4?token=XFiKYnjRZ4h7W97i9AlrI48mKnRYeGtXD-EExpgWCFmI7p9ZiC70nlMGixg5GmcivoWD5Q-JRQtuZaFcBi0PJYFFJ1dM-UIFLE8RCBlB1H8x5T-K8FvWBRnDfQD_BcpWxcBoLsVMpusfKbunpJUKbFwnReHo_jWqwyuq5ppSXLIvrHKY0mN0GkgsNb3YJAeJuNdfuZ2-3m_-d5goTPTWIF42p1b77GB5j1ay3ZA3yCOA1WCwGBebbIHxTonoIZigB3nJU5DkbgFAu91FUanjsR5MnNMY66jauFdCTuH4O-MxAKFEiXevVyEnIbrU1E_5riJzdpreFr-a8g7Ce3oy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2aac84bd.mp4?token=XFiKYnjRZ4h7W97i9AlrI48mKnRYeGtXD-EExpgWCFmI7p9ZiC70nlMGixg5GmcivoWD5Q-JRQtuZaFcBi0PJYFFJ1dM-UIFLE8RCBlB1H8x5T-K8FvWBRnDfQD_BcpWxcBoLsVMpusfKbunpJUKbFwnReHo_jWqwyuq5ppSXLIvrHKY0mN0GkgsNb3YJAeJuNdfuZ2-3m_-d5goTPTWIF42p1b77GB5j1ay3ZA3yCOA1WCwGBebbIHxTonoIZigB3nJU5DkbgFAu91FUanjsR5MnNMY66jauFdCTuH4O-MxAKFEiXevVyEnIbrU1E_5riJzdpreFr-a8g7Ce3oy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ رعدآسای ایران
🔹
ساعاتی پیش در کویت، صدای انفجارهایی از نزدیکی پایگاه نظامی آمریکا شنیده شد. برآوردهای اولیه از آسیب شدید به تجهیزات و نظامیان آمریکایی حکایت دارد. با وجود سانسور گسترده رسانه‌ای، جزئیات کامل عملیات به زودی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/671483" target="_blank">📅 20:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ae1e724d7.mp4?token=QpQ7KQI7smkoVUn_wNujNKbsJ7tn0RNBS5U4TnL3CYot1d09alJZTelPs5RuUq4ClC2L1y9okrXdBcTsMgUYMh3MDa1vJFi1369gTZ2uyTXh96e470bQXf1cmxvS7hJiE0K03P7jvQN6IAOMmX0cy0Df-gMxOW_s2-5hrBclod1jSRVqzgO4HVvI4QEBZWe3O0F-3ZLrq6k94gV91zjA0kjaQ6fSkUBqUVgkwlRsTTnzu6Ak0Ulrj263uzxjGOlNJ7auUASUAgviEuzbImbvzj1BkZ7nwBgotKObTmlDDmr8b9T0oZiH39g5KhCeireURgZ4U_snwmLJA_jeWwNLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ae1e724d7.mp4?token=QpQ7KQI7smkoVUn_wNujNKbsJ7tn0RNBS5U4TnL3CYot1d09alJZTelPs5RuUq4ClC2L1y9okrXdBcTsMgUYMh3MDa1vJFi1369gTZ2uyTXh96e470bQXf1cmxvS7hJiE0K03P7jvQN6IAOMmX0cy0Df-gMxOW_s2-5hrBclod1jSRVqzgO4HVvI4QEBZWe3O0F-3ZLrq6k94gV91zjA0kjaQ6fSkUBqUVgkwlRsTTnzu6Ak0Ulrj263uzxjGOlNJ7auUASUAgviEuzbImbvzj1BkZ7nwBgotKObTmlDDmr8b9T0oZiH39g5KhCeireURgZ4U_snwmLJA_jeWwNLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط تیرهای برق در نیویورک، چندین خودرو را به آتش کشید
🔹
سقوط دو تیر برق در منطقه «کانی آیلند» در بروکلین نیویورک، منجر به بروز حادثه‌ای گسترده و آسیب به اموال عمومی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/671482" target="_blank">📅 20:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اکسیوس: دیدار با نتانیاهو در دستور کار ترامپ در هفته آینده قرار ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/671481" target="_blank">📅 20:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
صدای انفجار مهیب در هرتزلیا در شمال تل‌آویو
🔹
رسانه های عبری گزارش دادند صدای انفجار در نزدیکی یک واحد تجاری در منطقه هرتزلیا شنیده شده و پلیس رژیم صهیونیستی تحقیق درباره احتمال پرتاب یک شیء انفجاری را آغاز کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/671480" target="_blank">📅 20:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
دبیر ستاد مرکزی اربعین حسینی کشور: همه مرزهای اربعینی کشور، از جمله چذابه، مهران، خسروی، تمرچین و باشماق، آمادگی لازم را دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/671479" target="_blank">📅 20:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix0GF255cVZjj69Qlsi1-MYlt_i6sTHpbeFk9Uh1NWq5TiAuQ_vI8nWnnla96ViMcwUKPmxszZvO19n9pmd2YEnjjdPKGRUdCmjxG57XYcpbQ6aF72gVBNsz7z4Jx1TgQgfq5rCo7W7iN07PmnRvb2mTLVlCdrCkSE453i6Wi6n7WBw8LN_bvpoRyvr_8tGFOyDnL542xR9xFfsTuTbnNuXwRr5VdJGCNroKB4aMR0aT5vjcJKzJnRa8lLAvCNBiynW618EQa4qdfVK8EEV_LRpH8rWsniNOhwXiOMOPg-aF66sq3hJZc_GjzslHeqjaTv8-Tgw88AT3LIRdeWxXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در منطقه کویا در اربیل عراق به‌گوش می‌رسد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/671478" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671474">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c5efec0e.mp4?token=ksKrSGnKB4IL7BqG280j2FEdCBtlkkTiMHk391AG3_8PJk4kNdP_mPRl1K1Zitd_aJpxmw33r-1cpauNh6P5ivQwL6exX1LQAgYWlvA7qdAHIMBpJupj3dcGdh0IDSJyVw_xoq86NTnOQoTY8LKFQRUVGnvTOAEmYsFSdGAMGbMbvQ5wHoJO0v_10qpPRA4YxEeozUtnXqNwqCC-coKhidKDtH2_n6Se-N94byDTCJoF3qccZ29zEKlh6FORoCPPmdrMx7t73mfLWff4rfSlB2ryC03-6vXhhaVIntkIbxLFGjMMNp33dyw9Cwd-HIca8ZB8Xm_hhlpt0lgxCefF8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c5efec0e.mp4?token=ksKrSGnKB4IL7BqG280j2FEdCBtlkkTiMHk391AG3_8PJk4kNdP_mPRl1K1Zitd_aJpxmw33r-1cpauNh6P5ivQwL6exX1LQAgYWlvA7qdAHIMBpJupj3dcGdh0IDSJyVw_xoq86NTnOQoTY8LKFQRUVGnvTOAEmYsFSdGAMGbMbvQ5wHoJO0v_10qpPRA4YxEeozUtnXqNwqCC-coKhidKDtH2_n6Se-N94byDTCJoF3qccZ29zEKlh6FORoCPPmdrMx7t73mfLWff4rfSlB2ryC03-6vXhhaVIntkIbxLFGjMMNp33dyw9Cwd-HIca8ZB8Xm_hhlpt0lgxCefF8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاقانه‌ترین وسیله‌ای که امروز می‌بینید؛ «تلاک» به خانه‌ها آمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/671474" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671473">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
خبرگزاری یمنی «سبأ»: فرودگاه‌های أبها، نجران و جیزان عربستان همچنان تعطیل و از چرخه پروازها خارج هستند؛ این فرودگاه‌ها در پی حملات موشکی یمن تعطیل شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/671473" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671472">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تجربه‌ای شگفت از مرز مرگ؛ ۲ ماه کما، ازدواج در برزخ و بازگشت به زندگی
🔹
00:06:30 دو تکه شدن موتور در اثر شدت تصادف
🔹
00:09:20 نوید بازگشت به دنیا در اولین دقایق تصادف توسط خانمی با چادر خاکی
🔹
00:20:30 ندا و فرمان به انجام سجده شکر
🔹
00:35:40 نظاره کردن امام حسین(ع) هنگام تعویضِ سنگ مرقد مطهرشان
🔹
00:47:20 تناول انار با پوست از شدت خوشمزگی
🔹
00:56:50 ازدواج در برزخ و تشکیل خانواده
🔹
01:04:00 شفا یافتن و خارج شدن از کما توسط انگشتر امام رضا(ع)
🔹
قسمت دوم (رهگذر خواب‌ها)، فصل پنجم
🔹
#تجربه‌گر
: داوود سلیمانی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/671472" target="_blank">📅 20:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671471">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پروازهای شیراز – دبی پس از پنج ماه از سر گرفته شد
🔹
این پروازها که پس از پنج ماه وقفه اجرایی می‌شوند، از امروز (چهارشنبه ۲۴ تیر) آغاز شده و هر هفته در ۲ نوبت، مسافران را جابه‌جا خواهند کرد./ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/671471" target="_blank">📅 20:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671470">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWpQLdWmRX5As3LSI9hR1DY7K3ylC27kdrraWsVX5WdhXEXgH1mYpBaBZ8Q9-VIuR7lUb9DyRShJzNctk0Yv0SNAeAVk1jY3q9vGV8GTMb9dKTh9ObyuBnckX4bKFrDONlmdDKq6ZGs4T_uNll6A9ah7hY-cEpJGPW33fLtgB0HMCTfgtFxLVgUBMUueco-V5aTAOERUqjmqeB3-JfHuuzEAjV1-CppEIsx0XC9vBG34InaGxib45B6_HTve52H-jJmG-yKssznzRmvEthGFyw-gUTN6PTTEen17c-rNvSM1SBfv8Nm8MzI1D2lT_NCEV1LQk9lDRc0Gi7rQYrOSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست سوم   ایران ۱  اوکراین ۲
🇮🇷
۲۲|۲۱|۳۰
🇺🇦
۲۵|۲۵|۲۸ #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671470" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671469">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آمریکا جنایت خود در حمله به انبار گندم در هویزه ایران را انکار کرد
🔹
سنتکام گزارش‌ها درباره حمله نیروهای آمریکایی به یک انبار گندم در هویزه واقع در استان خوزستان ایران در ۲۳ تیرماه (۱۴جولای) را رد و انکار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671469" target="_blank">📅 20:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671468">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXNyvNkhoREMd1UJhNqd8taLeTDz4kqNDBsrFYqk0mU5RaRelhJ6VSb7s34IEv7_Rpl2hAPgoRbaVlIj4xWmI2d_8qKqCqCqqQfhiTaKlF4JoNHuZypKt8S8L-EosrK77AzOGr3ZlgsX2xeR9XwKKmlFUzhR1yYN1Uqovyc3oGrOtrgctp5cfHItvXkh2PyYXua6ZuPWnig63m96Kx5cE8XGe-SQ15_gAq2ur0YEiX3yyLf2ACNP48DOKQAgzqk0V-0ldrvjn6uSWZyKQGk_RKI-sxSuh6KYRRGYjZqOXp6tGu_5dQHcIQ6OqeWXCo3HErptvxjMFmN1VxnTwbcQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت یوسف پزشکیان درباره موضوع انتقام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671468" target="_blank">📅 20:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpH-MI0tMitkw8EHVpB8JyiubFfeI6bjg3EsnhcgclRLh358G_1_vIDowbEmSxyKCcpgY0sXDoAwSkZwcvxqsB6t2qx6ntXcV4-8pSTFeZakSpSGk-1mBPEDVIL7VDahJz-GELbw_nooTaYgTZzagmiTU9TASCAafExU9tNGciUyDdi7F0agVaVcqBujB_v_hNMAfGOYfTKGSyzF9bgWn8n_YLNC8Vp5FLuhMHlOJO5TCmK1d3y93xaU1wORhpUJoOSNGgCN7SnwvqBIJa99KTkqYQsLIaQZe1leDOEV9jGwU1_tCEGFZDmlCFbkGOvQFe6AfMrbCEcrmIx7DYeLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kl3O7JO_Wiv-TS_iVo8CuCOUC3mVzHU8mWDNq9-p-10SDmXyb-wEWq74H2Cy_9Mwl4AF895ILIHnawfW5O9ieTHe23Pwgzso_0uriIRNjhFhDqMxobEI36QqfvaZRExr5rlRxiz_zMI8vNQqeaXypyfT_o0M7Pk_Vxe98wFqSeIRObKrDBbZD-p_-SeTye6pxFuh2SD1c_WbaD-pBCIEM03g0I57ELmPPN6CXabOJukwpzkerUP_Ozcs_aOxJ7TWFGYCiNZh0XLQ-bAmEkGFdmHLP0uFs7Wh2X-imYsycf0vSSa0oD5l0WhbY2Jmjo5RNHtNn0wouEw6oGcYJTxCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkFlN_9x6HXGLS8Vm9qQE0PykMtN26G3o6bxBH-gno4bvuinhFrVfmvjZe_owXKXKrseiNIYlQ8QhZ-r_zrx5NQBd2l0pZcx6CcB9sQXbsyeQ3cMzjXzqSabqXGbTbl2jj6kY4udU8c9sN57lvicUxdDAcqt7DeT6dTX70HIyXJ0y-89ehoN29VEJ6o3ic8ekB__JIDsLiTYeFC1P3ioq7lv4n6gCqRMw9SVW86HBv-2PMVWW_Gn3sDDv3sCzIKGlkA4XgqUhatOvnPxY-ldoxi27r7N-Uqdz8zXsm4cWN17fynnQgxH7gqxQiDndTFlGmLo9iXjKjPc6PQVkoTohA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/671465" target="_blank">📅 20:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عون: تلاش برای توقف جنگ علیه لبنان و عقب‌نشینی نیروهای اسرائیلی ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/671464" target="_blank">📅 20:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
یکی از مسئولان باشگاه پرسپولیس: اخبار مربوط به مذاکره با یاسر آسانی صحت ندارد و این بازیکن در فهرست نقل‌وانتقالاتی سرخ‌پوشان نیست
/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/671463" target="_blank">📅 20:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW282-1Xc-iLjlW8IU-fpaJrDZLt2XSJ8MaGGz4iYs2ES_b4fZYny_LnEWwT7_cbY1ezCe1Tk2IaoFx7LNoTqC70xLAvFYuY7fsiMeNXC60XaDD1p1Dod1i62LBDkJhmUZj9snOcnXhYvTo7WQPKdgGTlJjMPMfZUCuBrNpdZxXvLhEJQDTdIHvDr9P6Kbw6fV5_gT2WMrU04SDlGbJGETU72Iyy7NtUGtaVW3fHilc0vE5bsEeR-iX6EfYUpvmGBXHR5UFptUiK7Ajh3l8gDr0PagjJEiJ8CMHLSOCNrXWnFiDN4wapBpy8ZbYnwe_8jLSbdYywRZGrJoShTSAvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه امروز قیمت‌ها رو دیدن...
تو شرایط خریدت رو هم ببین
💎
اجرت از ۳٪
🏦
خرید طلا با هر بودجه، از ۵ میلیون تومان
🔄
تعویض طلای سالم با عیار۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
📲
داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/671462" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: فعلا برنامه‌ای برای مذاکره نداریم و روی دفاع متمرکز هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/671461" target="_blank">📅 20:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1_1693951181.pdf</div>
  <div class="tg-doc-extra">7.8 MB</div>
</div>
<a href="https://t.me/akhbarefori/671460" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل کتاب به نوجوان گفتن از نوجوان شنیدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/671460" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/El-IIwbRX2GqEf5YnLWHnF5dXh0z4bqGPPK0rKNmvZWVQPTnjNkewWtATRdQNm_euGfXUTCpzO1hie3yLDfbWNvTte3nuPLjSEuN9g-k9BzQQz8loyjfrvntUePzhXCH2SJJ8NtcJi9cgPwAsfdqToBO5NZ28R8XmvDc4L0xoVVgI_ZncAcXiILN33QILTzyActB-ICA9Lf-gEgvy8oAi2iJFFqQyLR1kEhB-yJfzw2dmWUgMBn13tBj_W8sdpELZNx7QpDBA1wMPKUf1INv0_kZTXyqsOswo763zvhrVxNNCrr_ZAuqbihhWiMpcTiPHWsvSBUYrTwcEo9gxhIFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P422JLmDhyqKFMxGOdZ91lITVEE-Y4c78bTz_AJcZEy__kOud1xUe11jLUT_nAoYt7kxQxnAIKb6caPBvUswGfOBmqDz1JeIsoEUZ_a3ReZ1Fp5vKNeytl_7Ls7nfxJkxEWrFOt_asqg2-PzT4Ws6mdDHHGCIJdudV6S3Hb68Eb1GOwrGIbyQPLT0boQLnWgwHbzgGgYseXdBcUZRbYbg-As78pitpbM2vguGFkoS11sMhhSrIpCUSW6WW0cLI2m-glmkVatztZ2UUX4QjWIFRKesKudNAJ_zN8h2FfXVRFPVnqSYOdgd9SFjlcEBrqBjLVolJCaeEbeAghC-trfvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر نوجوانت به جرفت گوش نمی‌ده، این کتاب رو بخون!
🔹
«به نوجوانان گفتن، از نوجوانان شنیدن » اثر آدل فابر، حاصل سال‌ها تجربه کارگاه‌های آموزشی است؛ کتابی کاربردی که با زبانی ساده به دغدغه‌های نوجوانی، احساسات، انضباط، گفت‌وگو، مواد مخدر و... می‌پردازد و راهکارهایی عملی برای حل چالش‌های والدین و مربیان ارائه می‌کند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/671458" target="_blank">📅 20:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtvwuK2U5YJGaoXfNp1k0KrnJfATLBn-L2jTj0qFNe08VTUzyIR9H_k0fT_VyhJlms-a6Kek5hc8YNs5eV0oWvtsTauLJtSf5RTZvLVe_r0H9fL0rEBolyNbDlPuTJO_SeL7GlIK-3T2nFuAo4rAmuLPWqOFAFLLm9Cb5pqB-kRhFyQuNHClqkJFB-73q4HFoLGhoRyQdJVLwZz4OJp4JpuJKjTT7AnrlGp05yVgvwhylSciSSgSbIB8S_GKCMuhaTZc5ZguRmLhIpFgaZ_NEOckqazeJEbwifwTGpjPismiWz_AjbQRX0hLK9FWji2AQ1yFWq1tVg88twREhVYnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلاهای بورس کجاست؟
🔹
در ماه‌های اخیر طلافروشی‌های آنلاین با این نقد مواجه شده‌اند که به اندازه‌ای که طلا معامله می‌کنند، ذخیره طلای فیزیکی ندارند.
🔹
حالا یک فعال حوزه طلا این سوال را مطرح کرده است که مگر صندوق‌های طلا در بورس، به اندازه معاملات خود طلای فیزیکی دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/671457" target="_blank">📅 20:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWvb0kdtJJ9vfMTrNwGRfHBpr2Fyu78VajPJqUTDUVceCURTjrPBOrEeF-8SH0noCKMuXgKbG4sxyFl_EsYkGFeMD7w3YW44npcSCDGydI5m7esUWdUAdnqSbjMdAc0rnDJ-NyZf8FZg4HKYGdLrYL9UgZnk9kJl4L7zVi0V7EqtMFFVE-A8UCnmgZ4VacDUYXzkWqZJZ7_yqy44-kfDmZkqsK74ostPJO4eDNXbzJzlVD14WlPTc-xvi_OQxJHeHogyDEch_9aRUUA7lvIXCVw1vTS7pgxg2HImPdSYtz433asiNijmu2yv59xn4OLfRQiwHtXAGhczMF76qWU1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/671456" target="_blank">📅 20:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
حملات فسفری صهیونیست‌ها به جنوب لبنان
شبکه المیادین:
🔹
توپخانه ارتش رژیم صهیونیستی منطقه واقع در بین دو شهرک برعشیت‌ و بیت‌یاحون را با گلوله‌های فسفری مورد حمله قرار داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/671455" target="_blank">📅 20:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست دوم   ایران ۰ اوکراین ۲
🇮🇷
۲۲|۲۱
🇺🇦
۲۵|۲۵ #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/671454" target="_blank">📅 19:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در منطقه کویا در اربیل عراق به‌گوش می‌رسد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/671453" target="_blank">📅 19:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
منابع عربی: دقایقی پیش ۲ انفجار، پایگاه آمریکا در کویت را به لرزه درآورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/671452" target="_blank">📅 19:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxBP8byHvY7gumD2CgdnFqwbWNged4j0jRfvPG8qD82oh_Sjsp7MtC6V2nhAbH88HeHZhlx54qLrbVIAG_2mYNVMI-AcZX4zdRinNb2drYWycn91kX-jGNci5SUVfraEHRBwaOPAZfMcKfcSsGndCZG1FMSI2vC7lu3qV8IWj9rRw40sDsvPeqtPzn-z88qWk6Fe-jnl5D_c7VR8irreEDB89azmB0dLYkOtBm_LxSU_gFyS388vig371PXFjAn9tqw6asWw7baZaMVrOc4RFEO4lE7Ga6bjgzxb39s9iNsCIXlIozaRLZ2haB7ti7fsO_34STnwQm3Ba8fWiIkopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر عضوی از ملت؛ یک پرونده انتقام!
🔹
این اطمینان را به همگان میدهم که ما از انتقام خون شهدای شما صرف‌نظر نخواهیم کرد.
🔹
انتقامی که در نظر داریم، فقط مربوط به شهادت رهبر عظیم‌الشّأن انقلاب نیست؛ بلکه هر عضوی از ملّت که توسّط دشمن شهید میشود، خود موضوع مستقلّی برای پرونده‌ی انتقام است... و بخصوص نسبت به خون اطفال و کودکانمان حسّاسیّت‌ بیشتری خواهیم داشت.
رهبر انقلاب
۲۱ اسفند ۱۴۰۴
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/671451" target="_blank">📅 19:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در کویت گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/671450" target="_blank">📅 19:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671449">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVN5Lah88ZxRQ0Ujv0kzf09wjxF1S1XYbAt5dguZ_JjQRBVjaSqxsnRZKbvx9z5X3-6jrV8VdCSqPdiYvtRPCrgl7aD-ZuDMDDkW2RfY0Ox6_prtjDSdlD5RBqPLNnC7e9wYstGiDZhmZxPuYGAVH1edOIjZgqfTqbRTnBuMULjDUHyGFQmmrPh-OKgAxWdm_OiO9l2ccAOtc8Zccb66SgDdDD_wsBF_pEK2JvAikJ24PDAWt09Rh4vrYT1rCMQIjhWlm6rI84PJTMc-UatFnC_fnRcTvU69Lh_2G0Wslqotiq-5w7VfAV3xFc1WFR29bYDnZpdPIm9AUcXT00yU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای حمله شب گذشته آمریکا به پادگان ارتش در شهرستان بمپور
🔹
روابط عمومی ارتش اسامی شهدا در حمله شب گذشته آمریکا به پادگان ارتش در شهرستان بمپور را به شرح زیر اعلام کرد: ۱_رضا شفیعی ۲_فرهادعلوی ۳_ابوالفضل ملایی ۴_حسین جعفری ۵_علیرضا قاسمی ۶_حسام‌الدین…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/671449" target="_blank">📅 19:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در کویت گزارش می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/671448" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671447" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxj3rNycE49l0K7zO-AwFuIpJw7bw3VD71lBNn2ziGXUBJ4_reiByICVff03UudT5YRtwYJfGsegvc4XYIjh-iirCMxzO6JDQJ9xgwolmQb3Zz9m3HfXKCCoU6U3lqULm5B0JvyFUkgYW0a_6fpfST4zE3Vn8OlSO9x1HU6Ec6bKFzmezlSzv8hPL75dfBWur3HER7PUbsf4_cCPUmhhv_oSKpKzof8_sbE6J33CZU9LMa4XaaPub4vruW9iRcE-nslg25rBZpVz7FtkE_3DM0-eNur312xfX6PTJeSLhZh_z4C6SfakZ7Gapn2WvjsGCDSQxfUiJbtC66RKsDV72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه اقدامات رژیم صهیونسیتی را در فلسطین اشغالی محکوم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/671446" target="_blank">📅 19:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست اول  ایران ۰ - ۱ اوکراین
🇮🇷
۲۲|
🇺🇦
۲۵ |  #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/671445" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b474fc302.mp4?token=Gyk9ayJ6WrCxZutoTA6e_oN7Xsd9SKLaDV2qD-cwJsxCZPb8Ad-89IrpMfzcQCqt8h82h3hr38StTPGfhuyYJAR9LyH32NHVV7EMJ56H6V7cuDLyTT0o5plVsx-uRRc29GwY8SVsiCDHSu4qbRgagtkDaTr2T3_Mrz3ebwnyZah2PLeJpSmK5CtEXTd2ReeKFxqq1MQ0-rrYV3PwNliDCDm-NETArWhN1jfu5pyE2bQmSycipgdW225DFa__sQL4-r7rFFTTQarbxt_3T_BxFLxZTk-YdZiBXSmFckWvugkyRgStsU0zQbvpI6CCKIwO-y42IiWyFsAlL6btg3Su8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b474fc302.mp4?token=Gyk9ayJ6WrCxZutoTA6e_oN7Xsd9SKLaDV2qD-cwJsxCZPb8Ad-89IrpMfzcQCqt8h82h3hr38StTPGfhuyYJAR9LyH32NHVV7EMJ56H6V7cuDLyTT0o5plVsx-uRRc29GwY8SVsiCDHSu4qbRgagtkDaTr2T3_Mrz3ebwnyZah2PLeJpSmK5CtEXTd2ReeKFxqq1MQ0-rrYV3PwNliDCDm-NETArWhN1jfu5pyE2bQmSycipgdW225DFa__sQL4-r7rFFTTQarbxt_3T_BxFLxZTk-YdZiBXSmFckWvugkyRgStsU0zQbvpI6CCKIwO-y42IiWyFsAlL6btg3Su8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرویس عجیب والیبالیست جوان تیم ملی در دیدار با اوکراین
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671444" target="_blank">📅 19:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7d-CX2PV341PU77rUw3lUpPu2bugXUb7cs0S7Ewg6wmeugC6MKumTbJ_gPJwbl1YkQTZ0j31tlXSepgiDSyQgbuf5RWNBHGgw6YuK8Ec4nA8KiB6yMZb3cFwYpffvY-cesz7kc3Sk304xjV4lGn2PZ5j2dDfx-JR8ga8RgQ2RyPzMhxDbGulF4poY94O72eAlBe-Mtscm0Y7DMqWPeP0nqGlWSlvo9EjBi1HkWc3JJfkd3L9uKBXMUZRtXpa2wUT7U5jVV5P_azWsS9OLByyPuWJtSzOxfx1QdI7rokeOxenuert7VyJyXnpbvMLx9GFK5FZiebQ3MK73hb95_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/671443" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تصاویر دیگری از لحظه حمله وحشیانه مزدوران سعودی به فرودگاه بین‌المللی صنعا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/671442" target="_blank">📅 18:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
آمریکا با ادعای اشاعه هسته‌ای و تروریسم، تحریم‌های جدیدی علیه ایران و روسیه اعمال کرد
🔹
وزارت خزانه‌داری آمریکا در دور تازه‌ای از اقدامات محدودکننده، شماری از اشخاص و نهادها در ایران و روسیه را به بهانه مقابله با تروریسم و فعالیت‌های هسته‌ای هدف تحریم قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/671441" target="_blank">📅 18:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671440">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
اصابت پرتابه به جزیره هنگام؛ استانداری هرمزگان در حال ارزیابی است
🔹
دقایقی پیش نقطه‌ای در جزیره هنگام مورد اصابت پرتابه‌ای منتسب به نیروهای آمریکایی قرار گرفت؛ استانداری هرمزگان اعلام کرد گزارش تکمیلی پس از ارزیابی‌های اولیه منتشر خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/671440" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_y5vU-XTSMntD_rUFULBz6u3HskJ1LY7fHPsHtphePB5a3Y_UL5P4fB4nwAQwF_KcjtDUZp_T3Im9bq9HxTL2WuLSfeSPvWHWvaXhJIgMR-b_dHKiF5HHfKGtioht2sRJPWRl2slDh7qW2fYcgEvIzInkf7YcOkrRQBuZ_nYJYSuAlJFNkgInDFRLWcHQS72qunW4s5pEfr-ppvMJGXWmOdAysa0Uz5g1t4yjcO1t7tjczPhsLYtpwQoXRCaCnIMEPHhP8xsr4Ec6dzhd_IOR1GYn1ykUU7UT48ybboCiaeSfRVVOnWhhsGyAIvAr1szh01LD6KjNCDI6n3c5XEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد کشتی‌ها در تنگه هرمز ۹۰ درصد کاهش یافت
🔸
در ۲۴ ساعت گذشته، تنها ۱۱ شناور تجاری شامل ۸ نفتکش و ۳ کشتی باری از تنگه هرمز عبور کرده‌اند.
🔸
تعداد شناورهای عبوری نسبت به اوج بازگشت ترددها در ۴ تیر (۵۷ فروند) کاهش چشمگیری داشته است.
🔸
تردد کشتی‌ها اکنون به حدود ۱۰ درصد میانگین تردد در ماه‌های دی و بهمن سال گذشته رسیده است.
@amarfact</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671439" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671438">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5Wb7jjbKvZgk_TRuSTxUPrI6W4rFL-Re7h9sdW2eQEGx6kugRMEJYC24y-kc-OtSWbbQZqaLtLqEkmrboz3Ogyiz92cBK0OoW5Ly04Ld5N4YZOAc3LxeQNJ3vbgx55pYGmncectCrrbafehYL8Wxw0z9WP7bsqpfpBhM7N40y96xflFwV4b7lNXTfHA0RPMRCGUv6_pOVPBgtMyz9soaQi5TWFzf5fWgVTUZQslDJNC-dQyfUGH1Q2qb8SCOPd467JKXM-pql7VbV27tDCE4_4WNhNzWvvlAd5Z8nFqFaYpzg2ccX487_deRplex3YXa70NumhdITYkp9tGgAOXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: نقض تعهدات و تعرض به خاک ایران بی‌پاسخ نمی‌ماند
🔹
سخنگوی وزارت خارجه با تأکید بر اصل «تعهد در برابر تعهد» و حق ایران برای توقف تعهدات در صورت نقض طرف مقابل، هشدار داد هرگونه تعرض به خاک کشور، فارغ از موقعیت جغرافیایی، با پاسخ قاطع نیروهای مسلح مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671438" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671437">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال | پایان ست اول
ایران ۰ - ۱ اوکراین
🇮🇷
۲۲|
🇺🇦
۲۵ |
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671437" target="_blank">📅 18:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671436">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
جلیلی: خون‌خواهی امروز ملت ایران یک مطالبه جهانی است
🔹
خون‌خواهی‌ که امروز ملت ایران آن را فریاد می‌زند، صرفاً یک مطالبه ملی نیست، بلکه مسئله‌ای جهانی است.
🔹
این مطالبه، دفاع از حق همه ملت‌ها در برابر کسانی است که به خود اجازه می‌دهند با نهایت گستاخی، حاکمیت ملت‌ها و عزیزان آن‌ها را هدف قرار دهند و به آن‌ها جسارت کنند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/671436" target="_blank">📅 18:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671435">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c1785fe7f.mp4?token=aRXya8LC6PhPJOSAvIC5WtJChbaOMfgECbXkzVQxIwc9p0cADp9r6ncUl_riEOL8nXLoO_gdbSh5ehyXWPzpX7Q7n099wr50w-gVE4g6kKO1MnhadxYAiX1BlQKBgnbzAp6gnoAEi8bXwAfS0m93jHThnZm6s-qWcNAoXc4iJarHSHGQnIsqiuZpZpbBIBRjBQdB4HwYIpw8uZhGQE6_IoySQLdMAcW9-Qk6TJ_B96RRl3FJWDL1e8ReAa6wnFfpc7xQdTJThDl4i_GIBGvEHqA-sZOKZq2Urw83892xgRZbWmOgxVWAjeZ1G15IOvwXhZKo9zY0HkZW0F_bXl9dQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c1785fe7f.mp4?token=aRXya8LC6PhPJOSAvIC5WtJChbaOMfgECbXkzVQxIwc9p0cADp9r6ncUl_riEOL8nXLoO_gdbSh5ehyXWPzpX7Q7n099wr50w-gVE4g6kKO1MnhadxYAiX1BlQKBgnbzAp6gnoAEi8bXwAfS0m93jHThnZm6s-qWcNAoXc4iJarHSHGQnIsqiuZpZpbBIBRjBQdB4HwYIpw8uZhGQE6_IoySQLdMAcW9-Qk6TJ_B96RRl3FJWDL1e8ReAa6wnFfpc7xQdTJThDl4i_GIBGvEHqA-sZOKZq2Urw83892xgRZbWmOgxVWAjeZ1G15IOvwXhZKo9zY0HkZW0F_bXl9dQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از طوفان آخرالزمانی در نزدیکی سان آنتونیو، تگزاس
🇺🇸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671435" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Di05xbGqTG8Wfj4mioVaC-oslvaLG2crpmXeHkJf-yAZFu9Z5IA08dHJWJwp3erdek7BuhAoBPbhX0PyCbBdiQLZ05N3Osn4SjA1khQYGlYjwBhBEWFuXX7eWvtM4dYGffhVFFlmoAbTOldM4m3Kg-mcCl-XG9tHKCUodgPGZ01KhGD-YIvcsm4P5A4o7mrEsVL-Xdxb-GXTAe5ZlgkQp20VZ4yiyeGT2Omu7zI7pMGYAXNgUR_11X7NadOAQT75weqEndW9vLr7EwvDn24UXR6VtNJMIo77ExImHXJX0gTA7DXq_Ozj_UE0-HrjkdU6EYmlgCALpBdGBOE1wnz9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlwSOBf5E781CX21LOwrgCC7pF68kGL1lKTqgPluX1JI1mrj5eQcnOl4J3Plf5AjkhxTVwQzIWCYwKZTvB0YGHY40lqLShrDvmDsgThNGc9WF1VFQLnu6-WQkstBuSRhjcddmhGNsQ5s2uJgk4d4tJeFiEluXndBdcadNldi1MJtoCZpGv1ZrmmL_YEM4Fdf96efNhpXk8pjwWJbJxTzDRqtywmDc0vT9MKtLl7_pEOCwzhRCCFLvq6i4kU7cjOQLnSJw7KErY8apEMy4PfsdeD54s19Sks9hZW_AG_A7jMZeo-mYzRTZQQUiRe2KJhstEQ6go-fXNVgow4whXPKCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
ایران، وطنم ، جنوب
🔹
استوری رامین رضاییان درباره اتفاقات روز های اخیر در جنوب.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/671433" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkF3sx9Ewah4t7xyyQ2gjm9ezjAu2t6xaNjgih2W3lSKZgd3Pg5nPEn96JYuft2yqgv2LWv0P8rqaWmy0tppET9OtzFH_2Cvod8RDoxA1KPgwHG4o2sZUHnmOHWnVlHOUTrg-BzWwyahlzN1t8MKPRVHeqAZLtHE5J7r7RSs4jdyYUSVjdvKRKJCc0-MQQRpOIhL-n5Mlgq4iv-YjdEAq2Ll0LIyNirvZbhL2HPu11JcGFtiBb5tZJCI6XjrmwNuRuUpYLOnpS1TPPmHB4ek2bSXP9ewK6WpoT-VU8E6bNPfU9iZWkH-hl93X_OLAvpP4LsYuwuUbaJzjm7XL4XJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه‌طور یه انتخاب کوچیک می‌تونه به کاهش مصرف برق و کمتر شدن قطعی‌ها کمک کنه؟
🔹
انتخاب لامپ LED با کاهش ۸۸٪ مصرف برق می‌تواند سهم شما برای همکاری با هموطنانمان در کاهش مصرف برق باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/671432" target="_blank">📅 18:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUNWEwm_jO0DVWXxzhnMJlnpdljg3MDc8AtNnGE-WrvrWJ739RcVQsqjhQq015oOnRd5s52z5douA3qAFWuFG4x069Qhp5i3oBj4xLf7natbx_hxn7TykgEdlPJScoXIu7hZo-2nbbkgUtV00udcmw1d_ZP1bGp1Ljw6S3QnEVWBo9Qj-3c0e0ZxpNhdV0u9P7bVuia8pM9657i0Rf51RYqYvj-fN61mi17pXQ6ip7IRK3nxYXhBCHwAS2aCmIMNdOq0OsL0L9uEUjgLp6wFo-BUpdpWpmWOSBQq_0FRAZY8fQiROPiEA1k_TMA1PWEEM1SNbX49pF6yKj3HR0eoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران درودی؛ بانوی نقاشی ایران
🔹
ایران درودی، بانوی نور و رنگ، نقاشی بود که از دل رنج، زیبایی می‌آفرید. بوم‌هایش میان رؤیا، کویر، آسمان و امید سفر می‌کنند. او با تلفیق شکوه ایرانی و نگاه مدرن، جهانی شخصی ساخت؛ جهانی درخشان، شاعرانه و رازآلود که هنوز مخاطب…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/671431" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7151964478.mp4?token=tU7JuYsrI8XpM_GD-lJlJZ10-ixJZ4xf-5TPUuPRhwrbDkyFAMQwDKD7tWv2MEU3UCdktI7HUnGz6KAiWA_KqByyiOgFHwTJxs9ZIqk-RSnAefml1dpEmeTit9JoZf6zNVcVmnxzAmiEEL54HyncKj1Lo3z7RZ1Xl014ECBuRTfr2FAHe4w5-LJEphgp1uASM1LFYLLHLVoMplqbU_VnlDTdsU4FG6CX5yjgCwL9H7-ykgL1mVbs5-088aw0iCLXOKzVdul3Zqp_-BE1O-wK2adsA6A9xLL_kd11EEj7s9okU5AQhF-zxBOENh1iOYwvqUtyQkGS_xFopRF9dwOdOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7151964478.mp4?token=tU7JuYsrI8XpM_GD-lJlJZ10-ixJZ4xf-5TPUuPRhwrbDkyFAMQwDKD7tWv2MEU3UCdktI7HUnGz6KAiWA_KqByyiOgFHwTJxs9ZIqk-RSnAefml1dpEmeTit9JoZf6zNVcVmnxzAmiEEL54HyncKj1Lo3z7RZ1Xl014ECBuRTfr2FAHe4w5-LJEphgp1uASM1LFYLLHLVoMplqbU_VnlDTdsU4FG6CX5yjgCwL9H7-ykgL1mVbs5-088aw0iCLXOKzVdul3Zqp_-BE1O-wK2adsA6A9xLL_kd11EEj7s9okU5AQhF-zxBOENh1iOYwvqUtyQkGS_xFopRF9dwOdOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کابوسی که هیچ سلاح آمریکایی قادر به حل آن نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/671430" target="_blank">📅 18:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فایننشال‌تایمز: ذخایر بازار نفت در حال اتمام است.
🔹
ادعای تازه ترامپ: روسیه آماده است به‌زودی توافقی با اوکراین انجام دهد.
🔹
یمن اقدام انگلیس علیه سپاه پاسداران را و گذاشتنش در لیست گروه‌های تروریستی محکوم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/671429" target="_blank">📅 18:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تجاوز جدید رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حمله توپخانه‌ای ارتش اسرائیل به شهرک عیتا الجبل در جنوب لبنان خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/671428" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72b47b139.mp4?token=V-MJAmgjQXZhz9fUoE44nKc8TcVAeio7Kbf3duVVb9a3B9bC3HIGwvE53_tpd2RsA3itXP1hKY3HUuITqTd4zMoskMUILIzzEFZfa_1ah8DzSOQLKKwr5oKhSApHLBN1CZFIayVVYtaVvcUhHGvqmV26qNkb5K-1-G-b7kBO3rLsT72MvbfO_ncG9461ET3lij69JGvUJqHi8Yn565X7T2Eh2BrtxTv9fTSilvZsf3NL9Lx8orCQzK2KQiRWV5xkdynhva3QD137LrXtXE4IWoKSeiQ4pd_2u-Mv-U3ik47bQ4tQ_Vka7tn4boSH2y1fyWiUdHGjSnPPRKucWSNk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72b47b139.mp4?token=V-MJAmgjQXZhz9fUoE44nKc8TcVAeio7Kbf3duVVb9a3B9bC3HIGwvE53_tpd2RsA3itXP1hKY3HUuITqTd4zMoskMUILIzzEFZfa_1ah8DzSOQLKKwr5oKhSApHLBN1CZFIayVVYtaVvcUhHGvqmV26qNkb5K-1-G-b7kBO3rLsT72MvbfO_ncG9461ET3lij69JGvUJqHi8Yn565X7T2Eh2BrtxTv9fTSilvZsf3NL9Lx8orCQzK2KQiRWV5xkdynhva3QD137LrXtXE4IWoKSeiQ4pd_2u-Mv-U3ik47bQ4tQ_Vka7tn4boSH2y1fyWiUdHGjSnPPRKucWSNk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: خوب خواهد بود اگر اسرائیل از بخش‌هایی از لبنان و جنوب سوریه خارج شود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671426" target="_blank">📅 17:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e88234b22.mp4?token=HouTw8_JetQN36GJxo1g4LFtzhdFPAXi3HM7QncJAogr1lhqHTnd9Z78VGDECv9nbPL_bISlIUzWZvgWnhh1OFm4Il2Zz4KqfbZ4jjUYVZdzF8MOq6_cN4wNtsK2WHNvU3oZEWJFR0qF5UejKVE1MIVfaiu4jF8gJs7bA9jiE8D7f85q10Jrr58KWfmT0q6p3Rs4TnREK2p0vnXB-F1GuhZYDQ3a4bFRkdI1YbbFco79C6ViEjjQjPmt-TkECFTQY_IDo-Gwcdi7QRtyqzFjqGCIIES0L9FHCnEC6MktI8LojyewMu-phr6OfdvVjHFc1eAuBXb_WmmnNGis8zaBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e88234b22.mp4?token=HouTw8_JetQN36GJxo1g4LFtzhdFPAXi3HM7QncJAogr1lhqHTnd9Z78VGDECv9nbPL_bISlIUzWZvgWnhh1OFm4Il2Zz4KqfbZ4jjUYVZdzF8MOq6_cN4wNtsK2WHNvU3oZEWJFR0qF5UejKVE1MIVfaiu4jF8gJs7bA9jiE8D7f85q10Jrr58KWfmT0q6p3Rs4TnREK2p0vnXB-F1GuhZYDQ3a4bFRkdI1YbbFco79C6ViEjjQjPmt-TkECFTQY_IDo-Gwcdi7QRtyqzFjqGCIIES0L9FHCnEC6MktI8LojyewMu-phr6OfdvVjHFc1eAuBXb_WmmnNGis8zaBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدر همسر شهیده رهبرانقلاب: اینکه ملت و رهبری خواهان انتقام باشند منافاتی با مذاکره ندارد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/671425" target="_blank">📅 17:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOAZgS2DZTAEMVw4UNYaQLHs8NnHgQmrgSM0qfFWNUmyH7oPEm_zOmqAQjiX5XgvZnL4TYaZ-OXHA8Nq9o9eepzje-d3HH5O87BIFihx56tSeu8r2d0jxiCEkvspM2Y5ZnCXV3hV_0iaHtPaGF5JAEk_qqWalbm92vEl6Ch5lkvAp9UtrTO4Qa3ECpzABLYqIFTv9Q0cqwZG5D7BsAq0UAQa6Sq1DCADTio7AE54FbyTji3rqPhX1DdLo3vERi4cmZFzFqr0GyF9woDHnSR5xst6tBTCaEPuZFLTpBMIC4klUrc6CSzjDlOa22JoHxb9du4uI2xQBd-9ikP-8cYjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvuPRoscqm-XKgGvyywq3m0gd-DgsVmR0FVax7BjJqLYc7EsArthyqDQHSGpXUB1Fix0CwxkNjT82RG3eCoqDg2dpb2iizqdrcA6bf_Z5K4K9_l5XfrYcoA_J0VMA8fHr3jntUyNUVieL3j9mHhejXJUtOYf6-cTxsqVdmuwTlPEbNoisnCVgxnHDTN0yJWkL_5whOkkArsowPwNVz6yoTz4mVzJPtFYVTfKuoVFaK_H4Dpovb5khwkwZ8Oqi0oHMZIX8kVDM9Zbd5vO5qU8bFPTuX8ykFk-yYr2uTM2tUAPQ5s-VMQOfH-7bcHM4fnttHwR7P1Fpxs-8I9qiszchg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران در رتبه ۸۶ جهان از نظر چاقی مفرط قرار دارد
🔹
مصر، آمریکا و عربستان از جمله کشورهایی هستند که بالاترین نرخ چاقی مفرط (BMI بالای ۳۰) را دارند و ایران با ۲۵.۱ درصد، در رتبه ۸۶ جهان قرار گرفته است.
🔹
در ایران، ۳۲ درصد زنان، ۱۶.۳ درصد مردان و ۱۲.۴ درصد کودکان به چاقی مفرط مبتلا هستند؛ موضوعی که نشان می‌دهد زنان بیش از دو برابر مردان درگیر این مشکل‌اند.
🔹
تغذیه متعادل، فعالیت بدنی منظم و اصلاح سبک زندگی، مؤثرترین راه برای پیشگیری از چاقی و کاهش خطر بیماری‌هایی مانند دیابت، فشار خون و بیماری‌های قلبی است.
@amarfact</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/671423" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671419">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hC7zQzfxVL1trCq58hRwncO02v9g821th-v6g8iqIb4r4v2YSIA9xgERSiSyI5w43dw3XSEqSXySJb7fZIQP1H6xPPJ2w4YvTBTh_fwGAiNepnUzQz7IJChYKxCHoqjWUFdo9vzu3FBtHxynLAE4KPoMHmRnQkRhdJ0hBHd4KwxrdNSRtE7s0KzD-wmhBM9i6tDvviS9FdowsYnVLjx5CadE6smWFAKNxxWiSaHeB8JUYtkaLXQQBEzViD3OVlBLy_MvcMHd-01yGbCGIXt_8vmv2EWjfrsLoF9PU2JT0BQQpFgvPKyAXlrYQbtgagI_yC96W8fiFx-fvVzNQmd0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u502A8Z88HgGFqJ-Wnb99jc0glJ305tVF6D0FJ3uEulmQdRuMu2JoBxorvY8k4LAEnQFu25xGfrFq1tyXKZD4JxzshxkIWxiBzaYe-k_osrKOTos9h2f--NdM8VknD3hgliQ58Q-OFcbTkv0awSaaJP7KiFo4UdGm7pirsbIfvhm3CWhtelONMcVqhWAt1jEYauIEFoiENwj4ipU1YXHNoloWCmhsRITUErgWlxwZcKpV3Mzjmo1Rd-3Go3lRSD4sIVh0UM4K5qQwwYhHCLCQrlSsMSaXg6AlDKTK76PZErs5mTBBw_n4ZyhUbH9pk_oBwNgAr1wyhi-mIoufLFaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKhynGwLEuBieDUW0dgBX2Tf5dyyK_5dMiF2P63kUiatxHcfi-iUlE3abQRLsuYl65s9p1RdsW3qUp0NxcQ0yso1r8q82NpwOiPvLWAWGpiB-MI7pgzqicy9Cog24lWfM2OvflBNWQdtwYQkkas727HAd57LI_QCB_7t2aPdqpp0eRvR7__1GB4NrzdAB1aCz10qkoI-Wda4RrXVwevK0XwRv5c1NHT75tzsZf_SSCQh7h6rhOXe5ACSkSQAQB4IS3npbyuG5-PjRATIqaDxZdAwn4_kFYMVenJzTmuwwl6dquw2Bn5Nbi6nV9xk1OXciUCUb3Om-kHc4TaT4riAcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5fb84a8b.mp4?token=JTj1wsDvWEvdaE8d1u60HIgXCj9t6GJQ4jRKL87plCdhJqbNIorsF0ZkanOfyxFcFGaDoT4L5QzQm_-VPeGSh3nc2DnfIMtEf2c1ujLFgFYN49dJNzs1e12G9TEGEqpq-2uwG3lhcZPSCbfhATcb7QxGd3jmzNUyQL9vc2pg3zdB1u1Y0pkYX6uhPVYTYr8Hwq61yBvVOLS5iIoLwO4nGos3ZIXtw9G1q1xRAssXTRTo4_Lisj3-jGhtiIpAviXul8s_cZMZR66xgZ2VlW4VWo798peskQw7aJtfa67cNy2aAcELanGzB_6O_b9njHCr8GWh5L8h7R_lvbJOoOLTNY8Pj4i22twswahsdp7kro6l_HXSParK-uNfTKmGtCxVOE_XRvIGL0xP6IPxKiJb7MCaeIilpZ37xuFFqEX0oj9SNHKSqUVWTEqoKkq6ynBiHdyak6KWY5RN9ucPUIu1xnF4FbE8xcsilywFAiRLsz0voc4W7wTOroFuws55ZfWyr6Q6cwOw8ykePETN4a3TTq8IKcGpRCEUQF8ojQ0p0l9leZZJqK4u077_jACShLPIBNmPI5csNL47d4LF9Epj8m1E2u_gtZcsgOnf9ireJgNNWU1H-uACf7Ldy88dmYD4AzmfN-cG3vjjsHtYW_pir0UUJyLy1vqcb38Y2mJrNh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5fb84a8b.mp4?token=JTj1wsDvWEvdaE8d1u60HIgXCj9t6GJQ4jRKL87plCdhJqbNIorsF0ZkanOfyxFcFGaDoT4L5QzQm_-VPeGSh3nc2DnfIMtEf2c1ujLFgFYN49dJNzs1e12G9TEGEqpq-2uwG3lhcZPSCbfhATcb7QxGd3jmzNUyQL9vc2pg3zdB1u1Y0pkYX6uhPVYTYr8Hwq61yBvVOLS5iIoLwO4nGos3ZIXtw9G1q1xRAssXTRTo4_Lisj3-jGhtiIpAviXul8s_cZMZR66xgZ2VlW4VWo798peskQw7aJtfa67cNy2aAcELanGzB_6O_b9njHCr8GWh5L8h7R_lvbJOoOLTNY8Pj4i22twswahsdp7kro6l_HXSParK-uNfTKmGtCxVOE_XRvIGL0xP6IPxKiJb7MCaeIilpZ37xuFFqEX0oj9SNHKSqUVWTEqoKkq6ynBiHdyak6KWY5RN9ucPUIu1xnF4FbE8xcsilywFAiRLsz0voc4W7wTOroFuws55ZfWyr6Q6cwOw8ykePETN4a3TTq8IKcGpRCEUQF8ojQ0p0l9leZZJqK4u077_jACShLPIBNmPI5csNL47d4LF9Epj8m1E2u_gtZcsgOnf9ireJgNNWU1H-uACf7Ldy88dmYD4AzmfN-cG3vjjsHtYW_pir0UUJyLy1vqcb38Y2mJrNh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویری از پذیرایی یک سرآشپز ایرانی از بازیکنان تیم ملی اسپانیا در جام‌جهانی موجی از واکنش‌ها را در پی داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/671419" target="_blank">📅 17:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671417">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
فوری|نشست علنی مجلس شامگاه دوشنبه ۲۲ تیر ماه با حضور ۲۵۹ نفر از نمایندگان در بهارستان برگزار شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/671417" target="_blank">📅 17:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671416">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlEf-ilwJWH35cGvObChzJDwyQ8I49ov2g7iARMedDehZA4R6P-hmyitkJmZkNTTC4aZhJGNeFly5RajeZOSRggcB_j2JCV0-Y8FPTcwlafmFlu_-1np6iIpHXnLH3-qbW5r8NnTiMv9JOcAfsM7KbtZjzDJW5KF0wWsaacz_gJxtuto1ezu8yyfhFtmcUd-dMmUsmbriEVuLjt0Th7rEEykrxBo3ryN_OAMFKVrR9q4Yo9mitAC5LPSVE0hPi9jRjwn5lZJYLEHllOro36OuJUOnNisxAzft4fTWw0FPbQrNWl58W0bgm1W9c4GxaGdblVSB1oO4bu-8bpL2n2mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/671416" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671415">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تداوم حملات یمن به فرودگاه ابها عربستان تا خروج کامل از چرخه عملیاتی  منابع آگاه در صنعا به روزنامه الاخبار لبنان:
🔹
حملات به فرودگاه ابها با استفاده از سامانه‌های موشکی جدید و با شدت بیشتر، تا خروج کامل این فرودگاه از چرخه عملیاتی ادامه می‌یابد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671415" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671414">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJJ1J2aRJ88SSszTyRjO7XKUgKrFtrMwYpnfvKscDk1mGuD2CiRoZmGrGlqCtxruoyOYDn1MC9uXyp8X_43foSGCbsxlb2urZpWs4jXI9dHvv2aXNcGxGibk2vPz3-BWVh_BeXuokvE9zzEcvX38XHGxNitEc6gHaPEXedy0bxRajAZu-p_u2FfgRJP8pLEhatkLqjnnJM7A3K50I7ZAnSHJrvcLj5_IfKLfBPjgtYRDF9CjFV4y2YmwPX8siAQ1tGkd31x32RLzI8q9Jg0haCDHmBUXlS2b1o0M68CvHoodCXVhsjspdpwOFa6GZrQ8GGamWeQmL5_I0c5xvxiVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
۱۷ سرمربی از ۴۸ سرمربی آغازکننده مسیر جام جهانی ۲۰۲۶ کنار رفته‌اند؛ آماری عجیب که از موج بی‌سابقه تغییرات روی نیمکت‌ها خبر می‌دهد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671414" target="_blank">📅 17:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np_SystHEl7mqf19CmvOrWtif7yrkNxghqApi1zROhGWy8U8a3Khq6h8R6l4NjYrphFJMMLkCYkL7UXxwshHu2Rsko3pBj8nh7uZ3dkIlgcr_HRDnaK9xjgVC-tEdJ7d4yTvMu-DtceyWrI1x1JLoRgFxhqjsnKiaokCKA2lZ2KDFw2zPB4semWSjPGcSiyKXdy9O2vtA-uXFvW625bFHp2qP6Qtvq3OhHKsvpmM2dzABz3zzL21_zCysNaYNmlHoZf_dOlk3gHqxakEpA15MycYasUiRuE7CPsRJu_MgNRQa2JOH_N1laXURkw4mLjYEQuOOBY4I5HSVRksEEU6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش اینستاگرامی محسن چاوشی به جنایت وحشیانه آمریکا در جنوب ایران  محسن چاوشی:
🔹
جنوب خون من است که می‌ریزد. به یاد جای خالی مردانی که دیگر  باز نمی‌گردند⁩.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/671413" target="_blank">📅 16:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
کامران یوسف خبرنگار پاکستانی: پاکستان به نظر می‌رسد یک گام به عقب برداشته و پس از آغاز دوباره درگیری‌ها میان ایران و آمریکا، رویکردی «صبر و نظاره» را در پیش گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671412" target="_blank">📅 16:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671411">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
شاهکاری به نام Lindt؛ کارخانه شکلات‌سازی در سوییس :)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671411" target="_blank">📅 16:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671410">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699d8b25a3.mp4?token=grfo1Uh4lkBaUSCWQf1rDB5g7AldbfQBfOZhxBy7eq8cDapAGLSY9o-2HUrgVz1xIR7fvXlYgbk0XBbgzTkbUSb9S2R9NVxiyE6yJ81by_ZksxDc971lVbdzbcXFEsGYynOpqd8L9Qdk08-5fxG_nCDYyIsmtYizW2YgkFJNx-OgGOVLd4FwA5XOTR0JX8by0HXTPvZuanto2qpKAZiNnNLSvjLBQs6ZsCX1sULJwUMbP_7xtCWX7YkyGKGBqPFDyfnuxfRPLZLS8Dbb7r6dus7ly4lT2sRAjq2C_A-6IMmvarcM3KhEItZqHi307V-dmzWK4lIZJ5soVyH2U3r86wr5BrH1ySk7dsS2j5l8PzXTtPYiBtO8S7kJ6sLhmsYTUzNuSKzeoiymB4_gV_JN-Z83ZZaTHs3oD9_2KEeYwnMgnyptezKZFNGjG6ypJy_dvADFBflm_rdJzIBSPRO9y2f4kPtJ6e_x1jcMv3F8ZlkEzqa_suBhFzk6WMmB5tdDXNkMlBWetR1hqZRJjMx_krQimV6mqzJ1VYc6PKGwUy3c3pu37tKVVaj1p2P7UOrIMZWnWQffO9dvMtYCtYfYNNQE9axM208ObzR6tx-NVz3DCvhvBZPdO5vXrFErE1YqGnMfdXEubF9L_BuE2P-f_P0ffkTT5M7XBA8Q58HEQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699d8b25a3.mp4?token=grfo1Uh4lkBaUSCWQf1rDB5g7AldbfQBfOZhxBy7eq8cDapAGLSY9o-2HUrgVz1xIR7fvXlYgbk0XBbgzTkbUSb9S2R9NVxiyE6yJ81by_ZksxDc971lVbdzbcXFEsGYynOpqd8L9Qdk08-5fxG_nCDYyIsmtYizW2YgkFJNx-OgGOVLd4FwA5XOTR0JX8by0HXTPvZuanto2qpKAZiNnNLSvjLBQs6ZsCX1sULJwUMbP_7xtCWX7YkyGKGBqPFDyfnuxfRPLZLS8Dbb7r6dus7ly4lT2sRAjq2C_A-6IMmvarcM3KhEItZqHi307V-dmzWK4lIZJ5soVyH2U3r86wr5BrH1ySk7dsS2j5l8PzXTtPYiBtO8S7kJ6sLhmsYTUzNuSKzeoiymB4_gV_JN-Z83ZZaTHs3oD9_2KEeYwnMgnyptezKZFNGjG6ypJy_dvADFBflm_rdJzIBSPRO9y2f4kPtJ6e_x1jcMv3F8ZlkEzqa_suBhFzk6WMmB5tdDXNkMlBWetR1hqZRJjMx_krQimV6mqzJ1VYc6PKGwUy3c3pu37tKVVaj1p2P7UOrIMZWnWQffO9dvMtYCtYfYNNQE9axM208ObzR6tx-NVz3DCvhvBZPdO5vXrFErE1YqGnMfdXEubF9L_BuE2P-f_P0ffkTT5M7XBA8Q58HEQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه قصاص انجام نشود حیات جامعه بشری در معرض خطر قرار می‌گیرد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/671410" target="_blank">📅 16:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nz_7_yGXmXJzMF7ykt5Vo-EtOe9y3UeUOMlosEGrWmxBO6Td5Rw0ePmESl_MI4GM7Cxb_PvG_hiDImCQOxieO5YmMHqfmCKxbkT-ffFa16cS14Ou8MvkZdIYXH0EjSVRIGprhmMqORGcGh1ida7dHr_CZADqmPAtjIMAsQGZY3uWycHJCC8rp76kuC-U--3hvlnSD83hN2pm9zVqnmpVNCc8SZ93jlkVS7xRsW4oMEyB475v1Y4phVavihuU-e-OB8P0YHCo2zzKfVfmVOA-FzmTINrhrBHliHRvbIjOyim7kh3GflemugzU1-Q8kJ510-xzGM_kCP7phFv09rpZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyihS84tHjmfRl9lNpyr4TBCfgE7XAbXwiJ-lrGtRLbvFctTLSwEK9k3iJMOsfvRl3kNImClJ_MULfl0x6NfC630JIW9xgM8hEQpOf0mL4YhtwhTg5JNcMcDNMTtCvwoQ__58AMeyyBjuiMu1G8SCtnLrg8rlUZx7oUi28UfZq3QEn0SDQaZ6M4x7hbk9fYJofk0NQiWx3sHOrvlUcijazKibw7-mnJeeFsHnLhX7RVTUVz4idVtR57f-bS5QOZcwhkS24zjBe0FjBgUMPLiem9S_vpF5HTiM6o-jXWWo2NBPc3ZgjFuyW0vWUik3219sB2U8PB-djZ6N2Y-5yh-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwaK32-sb7ZL--sqOODVN82BQbld_GKop3ZvD2lk_pOqC5a5O-fH70p4r0m-zgVQDJfPCHHrJ8iSPj-DR9BDPj5P1lWz6UMxAjQZ1SVvstg5sfnEMFWEy17WJYm_voVQP_kTuerMqfvII5L8zlmIX1jBEXych9kLUIH3kpP2oC9wO61xIRW8JkUWEMF4-Agyzl7jKZ6YQbc6EP-fveJRImkFJ0lntwFqihBS0gzzuPziOw4ME2xgwQtK4Jj80cjEj8Zi-U4mJEWOxYNx-BHr2SJ4gSwwiuFRqLi5n5cu6dmaH57W675AfvMKan24y_2Mr1q5RVlU12m9xs-h8nNtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oklv56r7UJ3GVSpO-6sjXc-HUgvMyIAWaF30a9ylXYDskiBhFGeBR9zHiv9Ak8ZeLGiRtkThnTimFjY4HWSrvjnMTtqKDuGlKMWuOgM-Z9w3PXoY4dxZorF4MdkafyOidUsjseXwW3KRgp03TbQ0-8Qp8zwoAHWwID4-tB9pHfh144-PE3tKUt-r8HISRnLPIpzOKmd7QMO9izZ-JG-whvlkc3-CH6ck_kEgysW9vf4ETBA92HCtbie3lYftmct5R3a4fp8GW-XoQe_iHJFnKVdeCbA-ceL4Wyo4MHwEWwVWNx-X40ItfLC_aRncMqlDoXESG82-IehgqvIqgZl0Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از موکب تک نفره اربعین برای خدمت به زائران پیاده
🔹
یک بانوی سالخورده عراقی، موکبی کوچک را با هدف خدمت به زائران پیاده روی اربعین برپا کرده و در گرمای شدید هوای جنوب عراق خدمت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/671405" target="_blank">📅 16:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671403">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9b25a297.mp4?token=GjsnL77MhFRR5Iz9HGg8VfsuCzDhprT1KTtPPCa2H1UTPBNgNNePhiwH4Raklc8-dJ7YqqEMn3eC-DHXBf_tyoCY6mtpdqmKSYXD2ZKWVuViD0QcjzmGVRSBPPPxrO9ZsxQmCjxRtufk687wI5sThSRm1_H8ISWWPkyWr4K8li1PcU78KDeUbTfU627XQXabXF6BRoJnbAieqw6js7QvM5i4zOc4NmPn0HwwGCB7Nnl8fRDvSf3Ux5mBtfZVF5_yQJHWdtLgD3cTGuN9MMzrmDWcqG7ZSH7guS7RR_1iPDjFHruceQERO0eVA09TmAS7zu7KRzcjbED1SMMH8NZ9cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9b25a297.mp4?token=GjsnL77MhFRR5Iz9HGg8VfsuCzDhprT1KTtPPCa2H1UTPBNgNNePhiwH4Raklc8-dJ7YqqEMn3eC-DHXBf_tyoCY6mtpdqmKSYXD2ZKWVuViD0QcjzmGVRSBPPPxrO9ZsxQmCjxRtufk687wI5sThSRm1_H8ISWWPkyWr4K8li1PcU78KDeUbTfU627XQXabXF6BRoJnbAieqw6js7QvM5i4zOc4NmPn0HwwGCB7Nnl8fRDvSf3Ux5mBtfZVF5_yQJHWdtLgD3cTGuN9MMzrmDWcqG7ZSH7guS7RR_1iPDjFHruceQERO0eVA09TmAS7zu7KRzcjbED1SMMH8NZ9cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام تاسیسات آمریکا در مینا عبدالله کویت
🔹
صبح امروز سپاه پاسداران طی اطلاعیه‌ای اعلام کرد سوله‌های شرکت KGL متعلق به ارتش آمریکا را منهدم کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/671403" target="_blank">📅 16:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671402">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دیدار ترامپ و نتانیاهو، دوشنبه در واشنگتن
رسانه اسرائیلی i24:
🔹
انتظار میرود دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه در واشنگتن دیدار کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/671402" target="_blank">📅 16:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671401">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HegyA1Ea1aeV-BvMfRgAxPVgGLepJBOeoeXaTe1t8tlJWjbimRV-xiE8cDDFM3-MSlZ8xx1teqCDIOOyYRpU578wwxEY4WI5NK4A1JwevUasJbqSbKftXl9xbz4Up9LkH81eFwQrAXmDtkGPmC8HCKJvCyGl8EGYHEwrKHI33hbYjck4j0IK2Kwp-QeveFOEePP524oaZWwORDg0VTe_UG_8QTGlit3Vf0ImO8MiCSueeuwpGfJcXmcxrUPF6JaWOOCcdzKU5lIuvk-IZQpp0mstxg3eZy0uu4-_d0R8aa4DzoQ73A1IaXASBKytrP_A4U0Efb5bcMKZ9xpfbSMC4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنی که از سایه برادر به مرکز قدرت رسید | دارلین، خواهر لیندسی گراهام کیست؟
🔹
دارلین گراهام نوردون، خواهر کوچک‌تر لیندزی گراهام، در مراسمی رسمی در ساختمان کنگره آمریکا سوگند یاد کرد تا باقی‌مانده دوره سناتوری برادرش از ایالت کارولینای جنوبی را بر عهده بگیرد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230598</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/671401" target="_blank">📅 16:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671400">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b6047653.mp4?token=XrSNZXiSYM6zDNWx7Re_f5Kw72mYz0ZBOOek2wj9ALlymLGRQjIJBBtwrTvMBPPM_6zZGOok1X-ixmfEDD1tWts2aTonmbQhr0hHuXXTiNsq3gPuxnkrOkQ02MjARFddvtrEe7DoQS1-Uy298GLsd3cPqj_Ccnw00MXv_o6qSlqF8QRA34E4gdPt-wAsKDkR5KIijYgem_uvCrYue9NNKM5ojoA_vwKR0iFm2-4kqnQ5h7e5HWQiINmQ0EU76LqNs7NiKLbTxbPzDGlqrF0CVXvVD6gnvPKTNQ0aAinwc_lpeRd8x8kisAWMXf-85C3G3oS2m-gQhH1SbplLkK--bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b6047653.mp4?token=XrSNZXiSYM6zDNWx7Re_f5Kw72mYz0ZBOOek2wj9ALlymLGRQjIJBBtwrTvMBPPM_6zZGOok1X-ixmfEDD1tWts2aTonmbQhr0hHuXXTiNsq3gPuxnkrOkQ02MjARFddvtrEe7DoQS1-Uy298GLsd3cPqj_Ccnw00MXv_o6qSlqF8QRA34E4gdPt-wAsKDkR5KIijYgem_uvCrYue9NNKM5ojoA_vwKR0iFm2-4kqnQ5h7e5HWQiINmQ0EU76LqNs7NiKLbTxbPzDGlqrF0CVXvVD6gnvPKTNQ0aAinwc_lpeRd8x8kisAWMXf-85C3G3oS2m-gQhH1SbplLkK--bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هلیودون؛ ابزار تخصصی معماران برای شبیه‌سازی دقیق مسیر حرکت خورشید و تحلیل نحوه نورگیری ساختمان در طول سال
🌞
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/671400" target="_blank">📅 16:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671399">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP-hK1dR_AVswq5vzpC1i78um-zqsTuO4o-ToSpT4QL7P1IglSrOJvGK1E-7l6yKr9tObfnXR25zdno2iAo8lYOVNmdApngFlz1Nkg-Fo82mL3jGbdpkW6tRx8ebn124Nd3_awvopZQIaJpmlwQo9lKRm6oh8PipwDnqPfZ_YQsPTkCksNBTulXfzJuXHUIzPhkr5QVkurRe4UeGFL5F4tz_bh_pa8s2xQnkkDYdhK1NPnYshmlr72iQvKd3UdwyBaZ-paEPTaRCtt24S2Rm90LvzvHIQajfADavWte5Ks18jlOokjdqCwbLD7L6ldfXvjUNra0VsbrgWrXD-nHAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور احمدی نژاد رئیس جمهوری سابق در سفارت قطر در تهران و امضای دفتر تسلیت درگذشت امیر سابق این کشور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/671399" target="_blank">📅 16:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671398">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7485d4f748.mp4?token=sr1rA22-_uHgKqLb_2Il5hpO3OXzT0qRmAOALv-V0HawT6NvAfqxXIbkfjum07KiSoYXBU4OZj3vfcS0l3yluv2XNJ0OPibchZJs_ZPZq8ANRIcG6ugH7jgj4y3lSIkxYjb1CMinCtGOXmSjamh4AKO_umVmKS8LNwcvSIwFUVgL1vd-M3Y4RAbrobAnCJ9wbuHZ9EX2hoE6e2wYH01DlFNk6ZEVD3IyjBYFJdcdPAiJyFClPRcIzgsK8VcIKclNgpntKv_BEcMj6_tdOksu-dKWUnoXLK_6RW-vkJGmIZBdLCnmaEcHmE6eNWx5qfoMUNey26prz5dLNHByVlu6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7485d4f748.mp4?token=sr1rA22-_uHgKqLb_2Il5hpO3OXzT0qRmAOALv-V0HawT6NvAfqxXIbkfjum07KiSoYXBU4OZj3vfcS0l3yluv2XNJ0OPibchZJs_ZPZq8ANRIcG6ugH7jgj4y3lSIkxYjb1CMinCtGOXmSjamh4AKO_umVmKS8LNwcvSIwFUVgL1vd-M3Y4RAbrobAnCJ9wbuHZ9EX2hoE6e2wYH01DlFNk6ZEVD3IyjBYFJdcdPAiJyFClPRcIzgsK8VcIKclNgpntKv_BEcMj6_tdOksu-dKWUnoXLK_6RW-vkJGmIZBdLCnmaEcHmE6eNWx5qfoMUNey26prz5dLNHByVlu6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با خرج‌های روزمره و کوچیک سرمایه طلایی بسازیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/671398" target="_blank">📅 16:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671397">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c810eb0d.mp4?token=GM-rTnB9CxSwddMUYjn3eVbwWxCTNRRtVTVtlubso9u_VsRvdPgz-sOaWjRqzMnpNjJ6ArirYJl48V7IBZ7GGgnkAnWr7SKSd-GGH8e__WRSqt8l85InmR7nZLObxhUHamg0bYTRkmGe454hP25zexX2h2LHVVPX0XpX48MBQfi9cgo90w2qwDb9b9mOalRQwvFYxsHFMn7oqDZ6-3Q7vj2JWd_XDXWCFsoDPNxhwDhlTkIfOOhyKw0ujETphKtAefP4-A2RL0t4lnQ3qwzW3jNuAi68oBVRzg0E0gKsJXDnlP3VtzX3q0GVzP1mW4FgrtBHvBC_2RxoEwCRDYOl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c810eb0d.mp4?token=GM-rTnB9CxSwddMUYjn3eVbwWxCTNRRtVTVtlubso9u_VsRvdPgz-sOaWjRqzMnpNjJ6ArirYJl48V7IBZ7GGgnkAnWr7SKSd-GGH8e__WRSqt8l85InmR7nZLObxhUHamg0bYTRkmGe454hP25zexX2h2LHVVPX0XpX48MBQfi9cgo90w2qwDb9b9mOalRQwvFYxsHFMn7oqDZ6-3Q7vj2JWd_XDXWCFsoDPNxhwDhlTkIfOOhyKw0ujETphKtAefP4-A2RL0t4lnQ3qwzW3jNuAi68oBVRzg0E0gKsJXDnlP3VtzX3q0GVzP1mW4FgrtBHvBC_2RxoEwCRDYOl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف استفاده از کریدور تحت حمایت آمریکا در تنگه هرمز
🔹
داده‌های پایش ماهواره‌ای «کپلر» نشان می‌دهد با وجود ادعای ترامپ مبنی بر «باز بودن تنگه هرمز»، روز گذشته هیچ کشتی تجاری از «کریدور عمانی» (مسیر مورد حمایت آمریکا) عبور نکرده است.
🔹
در همین حال، آمار حوادث دریایی در منطقه به ۵۶ مورد و شمار قربانیان دریانورد به ۱۷ نفر رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/671397" target="_blank">📅 15:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671396">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رسانه آمریکایی: پنتاگون، هزینه‌های واقعی جنگ با ایران را پنهان می‌کند
کلش ریپورت:
🔹
برآورد‌های داخلی دولت ایالات متحده نشان می‌دهند که درگیری جاری با ایران می‌تواند تا ۱۰۰ میلیارد دلار برای مالیات‌دهندگان هزینه داشته باشد، که این رقم بیش از سه برابر آمارهای رسمی اعلام‌شده توسط پنتاگون است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/671396" target="_blank">📅 15:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671395">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سنتکام: دور حملات علیه ایران امروز به پایان رسید
🔹
فرماندهی مرکزی آمریکا در پیامی در شبکه اجتماعی ایکس اعلام کرد «در جریان این عملیات ۹۰ دقیقه‌ای، مهمات هدایت‌شونده دقیق علیه سامانه‌های دفاع ساحلی و همچنین محل‌های نگهداری و پرتاب موشک‌های کروز در جزیره تنب بزرگ به کار گرفته شد».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/671395" target="_blank">📅 15:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYeObpy_2WIjDIjUFhMvbY5hUTJdirlcv2bNgfnXsGrjVeUacrM2yIi5w60s4_bJy_Gr_NCZY5NALbgGTBTOyraH5xUlRNqXxNY7E7C7HHx2rA-IeAr7gonlc7phngdy5CD20Cw-HO-xGcYJ9AxTMSE0dNCBXNKowHb7OmKfhn601c5yi3yIrDSNzJEa2sdwK71pUaiVhWUQ0i61wzU2uesbON93L9YWkjn1vbmIdQppEsRvL1npUz_LKzAVLpZy26tD0Rzh-h6UysuXiptrVKOa7ECXeGnBD8rj5Tap-rqyS8EjhP_cBlA65YppG7qtJyVTHClNPUdWsyLok8NgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عراقی: دولت عراق در راستای همسویی با خواسته‌های ایالات متحده، نام حزب‌الله لبنان و سازمان‌های مرتبط با آن را مجدداً در فهرست تحریم‌های خود قرار داده است
🔹
این اقدام پس‌از سفر نخست ‌وزیر عراق به آمریکا صورت گرفته‌است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/671394" target="_blank">📅 15:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b03649594.mp4?token=UcSaIxspC54T93Mb549i1vSl4CxrffWsObaK7Ej4VE2hkQ3nl2kH1l3CM7fjrgtgWSgBuRehpGeAwlqDnpoFisuSEmlytZkritQTTFvAd12h_5jRHj_V6dvIdkb3ebkSRkwDRVOg4owvqxbYB-onR-2xuARZEXTGB2g1MJ6SpMT4f5nVRI5iJSEO-LhMUbTF5X4yLpxmWSG1ABCx3aYfpt1YjcKtIzsi16vHonnpolq74a0SRcRlHJmwgZeaJPI3h9t4E-D2A2x2w3PHaOe6sNrvRWdzeU2b3rtvw0DnmZAX-LYA33ZhLp2haBOQ26Vfym8NgzsMJNeSeejXJaLeLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b03649594.mp4?token=UcSaIxspC54T93Mb549i1vSl4CxrffWsObaK7Ej4VE2hkQ3nl2kH1l3CM7fjrgtgWSgBuRehpGeAwlqDnpoFisuSEmlytZkritQTTFvAd12h_5jRHj_V6dvIdkb3ebkSRkwDRVOg4owvqxbYB-onR-2xuARZEXTGB2g1MJ6SpMT4f5nVRI5iJSEO-LhMUbTF5X4yLpxmWSG1ABCx3aYfpt1YjcKtIzsi16vHonnpolq74a0SRcRlHJmwgZeaJPI3h9t4E-D2A2x2w3PHaOe6sNrvRWdzeU2b3rtvw0DnmZAX-LYA33ZhLp2haBOQ26Vfym8NgzsMJNeSeejXJaLeLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار آمریکایی: جنگ ایران باعث سقوط ترامپ و حزبش خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/671393" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cae589567.mp4?token=vzuqBRMOzrMMczHhajEd8TFVJvF9djrwtMmbyi4AH96twEkMIt0hemGKxpuSaM4mBtjRIX1VFGn6gb-CCLzEfT3oYiNSTNKa69wPGrnmL10m4zey_b2lMg1JgLYnUCtJI3pC96d7PknEuHn9obZloi8J9sbe_7Fw4k9wMCY_wnbJJ1kOjMfiml3gzE6QHlDUMTnc5RJY1leklFbOpdd1nKyYehhKsTa62A4-t1FO64W8TQ43PCy-nxbn4SpRM92fyfqY4VtsTDPbFNPxgV6tLAiXlIKrSEVo8R4DtrHNPRHrbOSbjK0YuZJG3QIX9Sn4xthbN-FY5m4rqBDjwaCXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cae589567.mp4?token=vzuqBRMOzrMMczHhajEd8TFVJvF9djrwtMmbyi4AH96twEkMIt0hemGKxpuSaM4mBtjRIX1VFGn6gb-CCLzEfT3oYiNSTNKa69wPGrnmL10m4zey_b2lMg1JgLYnUCtJI3pC96d7PknEuHn9obZloi8J9sbe_7Fw4k9wMCY_wnbJJ1kOjMfiml3gzE6QHlDUMTnc5RJY1leklFbOpdd1nKyYehhKsTa62A4-t1FO64W8TQ43PCy-nxbn4SpRM92fyfqY4VtsTDPbFNPxgV6tLAiXlIKrSEVo8R4DtrHNPRHrbOSbjK0YuZJG3QIX9Sn4xthbN-FY5m4rqBDjwaCXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌ ناشی از گرمای شدید ایتالیا را فرا گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/671390" target="_blank">📅 15:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4872d05318.mp4?token=caGLdfmJrDlvBOh4pqVQs5_HdkJNuqhqN2rpt7TxDrqCTNrqyEu9vIHg7AZLeDIQ9Rd8ve67VqtdBhJkEHZLwV7rR-prHoO4zi-WvhGTsBZURZ0iuRh1smB9M_17fwsJzLbxZygJSRjc2pXt9TDFgtRGg4Z17G7gT7G1WNPFlXKhMUwIum7jiXFBmLw1p5W-RGpIPbGOQbKCKrJdnW7KaSiBNQNq9wZs2NRPLev2VNFtkphqXQMs20GOtavVtr3BYuzQlyOWlFu2DKZHYibjrtfPuZah-vzeHTHUbWQ0VXxFDRYAlFlosBuVo8DAuYZIs4F124Hm2DD3iTPm4audOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4872d05318.mp4?token=caGLdfmJrDlvBOh4pqVQs5_HdkJNuqhqN2rpt7TxDrqCTNrqyEu9vIHg7AZLeDIQ9Rd8ve67VqtdBhJkEHZLwV7rR-prHoO4zi-WvhGTsBZURZ0iuRh1smB9M_17fwsJzLbxZygJSRjc2pXt9TDFgtRGg4Z17G7gT7G1WNPFlXKhMUwIum7jiXFBmLw1p5W-RGpIPbGOQbKCKrJdnW7KaSiBNQNq9wZs2NRPLev2VNFtkphqXQMs20GOtavVtr3BYuzQlyOWlFu2DKZHYibjrtfPuZah-vzeHTHUbWQ0VXxFDRYAlFlosBuVo8DAuYZIs4F124Hm2DD3iTPm4audOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلدان لاکچری با هزینه ناچیز؛ ایده‌ای خلاقانه که این روزها وایرال شده است
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/671389" target="_blank">📅 15:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRq640HP-2PpV_4m-f1UnhWybsRH1rz8YRYLFqIkLrUM40a2954VNQVVoErbHA7ts1Z8DGrPTsvodoo-nrxAhFoRIz0ZGudbDeNYhFIpecRfsI9S1qgYqGujq5uJkgXrDxLMskNb2QZcYHrx89RSybcYUU8beV6V4VJhpnzImyVxwszewWZzTwIWpxYneCWPNYyWyVsQfgkw0KItWbZ-KeFxTgFy5jz3Z8UqtYX53-Q1oPmT_Zf2yzBt3eFnzojXNk23yNZFJeNcYfNRWhMsyR3kCpZHzQQvAwD9PzTxZFsBIg15Co7khiMiaHYIhWImy0E2waCXTLKoFi4B7OxVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
تنها ۱ روز تا پایان مهلت ارسال آثار به سوگواره رسانه‌ای «بدرقه یار» باقی مانده است.
▪️
سوگواره «بدرقه یار» فرصتی برای ثبت و ماندگار کردن روایت‌های مردمی و آثار رسانه‌ای مرتبط با تشییع رهبر شهید انقلاب است. از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوا دعوت می‌شود آثار خود را به دبیرخانه این سوگواره ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (پوستر و انیمیشن)
📌
هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش به دبیرخانه سوگواره ارسال کند.
🏆
به برگزیدگان هر بخش، جوایز ارزنده و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت نهایی ارسال آثار: ۲۵ تیرماه ۱۴۰۵
📩
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
📨
همچنین می‌توانید آثار خود را از طریق شناسه زیر در تمامی پیام‌رسان‌ها ارسال کنید:
@Badraghe_yar
برای اطلاع از آخرین اخبار و جزئیات سوگواره، کانال رسمی «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/671388" target="_blank">📅 15:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
عراقچی به قطر سفر کرد
🔹
وزیر امور خارجه جمهوری اسلامی ایران به منظور شرکت در مراسم ادای احترام به حمد بن خلیفه آل ثانی امیر سابق قطر به دوحه سفر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/671387" target="_blank">📅 15:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
امتحانات نهایی رشته‌های تحصیلی پایه دوازدهم در ۴ استان لغو شد  وزارت آموزش و پرورش:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های این وزارتخانه و با توجه به شرایط خاص کشور در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته‌های تحصیلی…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/671386" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_uzVww1ZThEHZ-K_39ifdH_JasFpM9u4McT2nEVBq1h0nCK621jpOkIJnGqJwg2LkGfkg2mioiQTbZg7xev7elghqWFV21tIm4QwlX-DiuzCR1SVPFUTZXCNXOqPV_XyQvnSg89u2QZwQXn3WZytErGvwcyimMpYpMi54RrbDrpDPGQQbIjVjdBw3SC5Kf0V5_5YMo6yGSF5OdwXAVf2owO7Fb0uhqfOMD-ZqM46rwPjoQQNTqh3l4FtwkDEFq0lRsmz10YRJRiZNIH2Lh8v8BuTSfK3IW1YnleAPP_S2xMhRp6DGCQIJB0UFtdI5tty_MyPweGeSM3pOFpXYH7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا از ضرب سکه طلای جدید یک دلاری با تصویر ترامپ خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/671385" target="_blank">📅 14:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4fb22104.mp4?token=QrfxkDjj83waNsX-eDmHo1hckhR53qGxeFQsVYsCR0DnluNC2mPRKe572I7is7sdFwUmcxu6kmPNB9s8hL8G2DYQlatZLPsWML5xymuuprWcxoIX0DhZVMfV1Wsq4ecX48740MroFSZBdTT6AnxkijqBMEzZcVqscHcurNDcg9oW98f_H27OOVLgbjoVMqFlhXEMAMCWuTDvSbgdeYADLqD-SB5cdkqqjb_gFOJmpNiN36m7Ji-8NWBk3pBrnvUxHrrCLwqDhMOE6pv3HrQG8uVVgbWYwntBIxgNWN5IJ0-SlYONoBaeR8tGsH8CId9Uf6VmGKzRz8dxWKMiDkKvcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4fb22104.mp4?token=QrfxkDjj83waNsX-eDmHo1hckhR53qGxeFQsVYsCR0DnluNC2mPRKe572I7is7sdFwUmcxu6kmPNB9s8hL8G2DYQlatZLPsWML5xymuuprWcxoIX0DhZVMfV1Wsq4ecX48740MroFSZBdTT6AnxkijqBMEzZcVqscHcurNDcg9oW98f_H27OOVLgbjoVMqFlhXEMAMCWuTDvSbgdeYADLqD-SB5cdkqqjb_gFOJmpNiN36m7Ji-8NWBk3pBrnvUxHrrCLwqDhMOE6pv3HrQG8uVVgbWYwntBIxgNWN5IJ0-SlYONoBaeR8tGsH8CId9Uf6VmGKzRz8dxWKMiDkKvcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز همچنان بسته است
🔹
تنگه هرمز همچنان بسته است و در ۲۴ ساعت گذشته دستکم ۲ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/671384" target="_blank">📅 14:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سازمان امور مالیاتی:
مالیات خروج از کشور
در سال ۱۴۰۵ برای سفرهای خارجی عادی از
۹۰۰ هزار تومان
در نوبت اول آغاز می‌شود و پرداخت آن به‌صورت الکترونیکی از طریق سامانه‌های تعیین‌شده امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/671383" target="_blank">📅 14:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
زمان اعلام قیمت بلیت پروازهای اربعین مشخص شد
🔹
سازمان هواپیمایی اعلام کرد قیمت نهایی بلیت پروازهای اربعین اوایل هفته آینده اعلام خواهد شد.
🔹
درحالی‌که برخی گمانه‌زنی‌ها از تعیین نرخ ۲۳ تا ۲۵ میلیون تومانی برای بلیت رفت‌وبرگشت پروازهای اربعین امسال حکایت دارد، دبیر ستاد مرکزی اربعین تأکید کرد قیمت‌ها هنوز نهایی نشده و جلسات تعیین نرخ همچنان درحال برگزاری است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/671382" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/614c0b0bbd.mp4?token=CU0fIXs8kjgpt30QHIj8ghnyxMnfwCBaSbEiQC0f2udZaM4r5Fs3bbNz6mS4aj3QzPWZwLytjD1ViIvx7rgx3s2__f5sBK8olmllvLEKeGDu8Ejjiq73QnRIxIigAJhnTNv7eUnC65BS28UZD2Aimnf1ZRzdqGo0f908uuizf9JWwtpBPZUAoU-hJXN9Dh4f7umVAiziiAkRYBNzy6ku3RuEeUxosWXhMygBGWN7A5JAXyThX_xOkY4UZ3OjnHaBR0ml5FLPfDaIgzTeHVpO3UoYO9oNZa-oV5Vjk-4wlWq24bzsgAcGpTsdRBlfUNPlTNflcfh9V6LidqviJ9g0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/614c0b0bbd.mp4?token=CU0fIXs8kjgpt30QHIj8ghnyxMnfwCBaSbEiQC0f2udZaM4r5Fs3bbNz6mS4aj3QzPWZwLytjD1ViIvx7rgx3s2__f5sBK8olmllvLEKeGDu8Ejjiq73QnRIxIigAJhnTNv7eUnC65BS28UZD2Aimnf1ZRzdqGo0f908uuizf9JWwtpBPZUAoU-hJXN9Dh4f7umVAiziiAkRYBNzy6ku3RuEeUxosWXhMygBGWN7A5JAXyThX_xOkY4UZ3OjnHaBR0ml5FLPfDaIgzTeHVpO3UoYO9oNZa-oV5Vjk-4wlWq24bzsgAcGpTsdRBlfUNPlTNflcfh9V6LidqviJ9g0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید در آلمان؛ خسارات گسترده و اختلال در پروازها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/671381" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37729ca78.mp4?token=rNWH9jaJNcwpRlVcvUNxyqx5V-E0SJMNvCXSWju3yLi__Wh0HbNpOZyTo8xx6Rh6tPniFfaEJOVnBLx_633lcVbnkplfimtZjLIj5Y5EoxNjxyuigvTS0uF7OGuylrvdtviLa1xF3MyzrVTuSpLw6DNYQnAO3cJa3Dnu6j9eeoejU4vn1X9HBhd9vPzMyAGN9sJLantlkh_UNBkzZ4oaym8RD2XmBqkMSTiWglOOnQRAeug6P-ixk7JGiY8cxXZfGn1JH90xtjVuPx1_h66jr6neYKh8soWUjU-0kU6sGBa9BKyMd9pTq6t0jcNMGxracxaiq4uclTq68k7OPedzznskaeLIudHQdAeqCPlrGYJIWBJEPmHqLxpsqrtO_gyQWsbWZQqjvrRh6XGf4_XjYiMMcLBAHMR1klVBhutpEIjiyIBtDQZMMCpThfufNdmA13WWydeFyH2qxIDVlqMxyjAfMgHsEbD_waLlOcUDw2JkMC59qJ8rM5T_KLtfFN6MNarPxf6hd2-oKHi1PwRXffNCVyCr9EugRWuidpjA0dhF-Ud5x_dl7heStPmZ3oVtD49Bf8yZBUgeq-FQbrdjxarM9oPWHtV4-ZEb3Uj73n9oK_QxjE5exf23YfOCKtJXJf6Aa0gtZlxAjagzhOV43sloHWAnlRwBqpSpONL4AhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37729ca78.mp4?token=rNWH9jaJNcwpRlVcvUNxyqx5V-E0SJMNvCXSWju3yLi__Wh0HbNpOZyTo8xx6Rh6tPniFfaEJOVnBLx_633lcVbnkplfimtZjLIj5Y5EoxNjxyuigvTS0uF7OGuylrvdtviLa1xF3MyzrVTuSpLw6DNYQnAO3cJa3Dnu6j9eeoejU4vn1X9HBhd9vPzMyAGN9sJLantlkh_UNBkzZ4oaym8RD2XmBqkMSTiWglOOnQRAeug6P-ixk7JGiY8cxXZfGn1JH90xtjVuPx1_h66jr6neYKh8soWUjU-0kU6sGBa9BKyMd9pTq6t0jcNMGxracxaiq4uclTq68k7OPedzznskaeLIudHQdAeqCPlrGYJIWBJEPmHqLxpsqrtO_gyQWsbWZQqjvrRh6XGf4_XjYiMMcLBAHMR1klVBhutpEIjiyIBtDQZMMCpThfufNdmA13WWydeFyH2qxIDVlqMxyjAfMgHsEbD_waLlOcUDw2JkMC59qJ8rM5T_KLtfFN6MNarPxf6hd2-oKHi1PwRXffNCVyCr9EugRWuidpjA0dhF-Ud5x_dl7heStPmZ3oVtD49Bf8yZBUgeq-FQbrdjxarM9oPWHtV4-ZEb3Uj73n9oK_QxjE5exf23YfOCKtJXJf6Aa0gtZlxAjagzhOV43sloHWAnlRwBqpSpONL4AhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجاب استایل‌ها دین‌فروشی می‌کنند/ با هزار قلم آرایش و عشوه و ناز ضربه بزرگی به بدنهٔ مذهبی ما می‌زنند!/
تلویزیون اینترنتی مدار
این گفت‌وگو را در آپارات ببینید
👇
▫️
https://aparat.com/v/qypc186
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/671380" target="_blank">📅 14:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCinjjNgG1CTbsjah3Akvvo51P5kAe0cbllI-_SWySDPWWOToNguGyKeT7uJwGMz34Bv7bTJBCEw8ScekI7vUQD44y8W2SDKfY7fMgP3LWtO7OIf5QhPq-17sC4fXyOn16sRnQtjGCx4KPuM4H-QTBOewvTKGbqp9afgDmJQoUVCFqs3zlz-WL3GipIdybwlhM3i4G3UCNLfyfsOrqB6yjYASbvKn5ZaFMjUT53PAGLD6lDHBrVk3zalGJkj4bYITw_gqkNx37FBA6md8IVJDFANuHbwlgFHF_rWq5pjof1rz1-nOz5ijobMemPx-U8oQrN8u3ttJ9A3qNhj-yr3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شال مناسب هر رنگ لباس؛ این ترکیب‌ها استایل‌تان را چند برابر جذاب می‌کند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/671379" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای اکسیوس: خوک هار جلسه‌ای در روز سه‌شنبه در «اتاق وضعیت» کاخ سفید برگزار کرد تا درباره یک تهاجم گسترده در ایران بحث کند
🔹
منابع می‌گوید که این حملات، دامنه‌ای فراتر از تهاجم‌های کنونی در اطراف تنگه هرمز خواهند داشت/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/671377" target="_blank">📅 14:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
دامنه
t.me
تلگرام به وضعیت عادی بازگشت/ علت تعلیق و واکنش پاول دورف
🔹
دامنه کوتاه و پرکاربرد تلگرام با آدرس
t.me
که برای هدایت مستقیم کاربران به گروه‌ها و کانال‌های عمومی استفاده می‌شود، پس از یک روز تعلیق و قطع دسترسی در سراسر جهان، بار دیگر به وضعیت عادی بازگشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/671376" target="_blank">📅 14:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0-_4Y7VDfGZaO3aHhHJ3xmA2fww3XxT5mUl9Mch0Umgi_SOV6o1B-pjgOnpIQDeqZV2cA6na5RYSg_c5XdwgGHCCJPGt3En-GkK0pysLV7X7H6Mc8zhD1KUwNxPe7ASYs5plUQHSTriT_ZU4i-tAzFR_rbpFg4Bwdi1lggwInUzi-5kjtkYfJuuXEMP3_TD7depmBn8nCZkFOB8-MLJoenmBhniRnftIgSiNNU_MoT02zzSll-j0_Yp3fELy1XklPXy1RJET1xr9BPU5l5dmZVAD64LfsagWLk5eM5KCB9x14evx0W4JrN7hSdENKa53uD9bzjchsYhGQWCsL0hRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3Jgp4NHT6jR7SPlADT90iwXvllwpZxcEdyasRPctbVsE_Rbx-sK2F0tN8yDLScOlHm6ymCyT3lcWRH4VeTA2EjblnCbJHZYmhOroyTMfSNfxMGlNmd80Geq0NmLoZg1mKoztwRNMEsbXmNrO_YwX2ZikH3cWyvTiBwMcy3JWOmpqkSx_XKGnHGTTkJEowOI25SymBnVyEEMjJcs86TrhsQTIFi78FjfrsmYCGmwLp7y9MLLXWejslwNcVTcLQbxLQC3XcU5j0Xb8RnxrasIJotBzSAEmkvP4wwPVQYBA1fMwoYXQlLVJph0NBVNAhR00qLxTJAB6G9_vFzEC1_x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcNMNx1a4pw3T09mCbAtm305DIHOkTkcT7kIm0m6qMYRo8s492vyCNda3be_bxsFBwOzuH2f7UIFbPuyhuLQjGt_7mhgnsqexiE2O6cRPiRZAz6MLvtc4sn6bnf1yc_J9kzjZSgU2xbbHoQmU0ZdRIlu0BPtEqnwpAJu3IJm6tF3-ptACIqJXXJr60zWzxojfSTd3PXuHJ_e_0bvqsLseeLYE7upY_rEGKLw4vdNS_0oBHgh0VNRNx7-qKWcby5N9klej4IVZD7gPBCH31pgr-IVpoRRkqyGGkJ98ncXmV2gbt5HTy5FNyzhMzdK8XZJygrch61KtuJlEtIwhVj-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای جدید از حملات ایران به پایگاه آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/671373" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
