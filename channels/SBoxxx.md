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
<img src="https://cdn4.telesco.pe/file/iGBXucioGQkl2NQvKe2TW0AiJ9vXgnDpyEccmAsoUduMInk5H2LgJ30XEqDJQLgnZEKrGJ3C4brEep9HfAfvzwgDqcA6RrbjnQjU2iPLnGhhH4bfconmeOvMJvlOXbBnz7fTrqv0astaZ4Cezyi5UM82AM93XDMazt1RPwzDafpsFhxO6HLeEH-PB3IpdLN3XcK7de23ZHGrGJQeEsqoxpaatbsG7RKj0vHpF2w5dJ0rC9-cF5j6KvPkfGISvoM-e0TtQRHtejOoyXDBPMQzniuSfzjWN1L8ztu8WzrvPykQHwcfDcLOaMhLGOlAFAWtQtUpPmYN3sxa6YT7OYvRoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrGK8RuLDjZlsittil98QWpmeaiFkvxrVhVSnaYVFWREqb1tIsVm7-MzkdFNeLdik1mza4VZHJwmDDvJRweGOaXWD1bLnLT0WU47XuwSn8JxcVtbRWymGukphuxJOYlR8OJEFMqLbngMrZZS2hGdPuaWu1i_r4ucA1D8MVKSikSnuzJVacJ2p5tdtXa4Q64SYgukGdo_AG1K4UHQp-ZxXC3Kj4O-Rask3vgwK54A5g18dzsCCNZnWP9dfQW6W3k-FrrQ3LllGXx7sj-htPRT3TU9RLW7uPH593bIlMb0xRZjs17eudLgVfzZ2uw16lS_GhHKzV7X3DPsunnVz984zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#طلا
بر اساس نمودار، احتمال ثبت یک کف دیگر پیش از پرواز دوباره قیمت بالا است.
بهترین محدوده خرید میان مدت 14.2 میلیون تا 14.9 میلیون است و تارگت حداقلی 29 میلیون تومانی فعال خواهدشد.</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SBoxxx/17953" target="_blank">📅 12:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:  ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/17952" target="_blank">📅 12:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">برخلاف تصور رایج، «لابی کشاورزی آمریکا» یکی از قدرتمندترین ائتلاف‌های ذی‌نفع در واشنگتن است. اما این لابی یک سازمان واحد نیست، بلکه شبکه‌ای از انجمن‌های کشاورزان، اتحادیه‌های تولیدکنندگان غلات و شرکت‌های بزرگ کشاورزی است.  نکته جالب اینجاست که این لابی، برخلاف…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/17951" target="_blank">📅 10:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/17950" target="_blank">📅 10:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:
ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/17949" target="_blank">📅 09:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتحلیل و رصد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=VArKmKX8hWnB2WZ6ip8t3qOtr_q-0CrfJNicsrGw5iaPKNt3g8TtOf6ylc4ejJhu-pXNoduBESLA5NtVNR_k2nghEXaYt8xV1ZsDsFtabJ1dbX4lJ1e_bjn0cdtuoairX3sG47wv8T7vyG9IUPnIzEB5iCoPPk-KCi0y-lSYj63OdRLgyA-T3KtHgH7kWlcnQnazzDrzLa7N4_OyvKQlGwdNaQvJsE-w7wYAXUHMxAOwN64DUQ-J6aGK73UHSMxUCWYdsElLrQalpYKmFPC9GhR-nfAufJLwmIia-SyEOf-Mv8bHDy6EHQ3mgdpOTk0inXmxZQwljCEwWSNJ15WzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=VArKmKX8hWnB2WZ6ip8t3qOtr_q-0CrfJNicsrGw5iaPKNt3g8TtOf6ylc4ejJhu-pXNoduBESLA5NtVNR_k2nghEXaYt8xV1ZsDsFtabJ1dbX4lJ1e_bjn0cdtuoairX3sG47wv8T7vyG9IUPnIzEB5iCoPPk-KCi0y-lSYj63OdRLgyA-T3KtHgH7kWlcnQnazzDrzLa7N4_OyvKQlGwdNaQvJsE-w7wYAXUHMxAOwN64DUQ-J6aGK73UHSMxUCWYdsElLrQalpYKmFPC9GhR-nfAufJLwmIia-SyEOf-Mv8bHDy6EHQ3mgdpOTk0inXmxZQwljCEwWSNJ15WzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!
پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.
ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه ولش کن. ولی مسعود هیچ رَقمه گوشش بدهکار نیست و فقط بیل میزنه.
@tahlilvarasad</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/17948" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است  یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.  ایتان لاسری بر این باور است که اسراییل…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17946" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نخست‌وزیر پاکستان، شهباز شریف:
«کشورهایی هستند که می‌خواهند توافق را مختل کنند، و من می‌گویم که بدون ایران نمی‌توانند موشک‌های بالستیک داشته باشند. استانداردهای دوگانه قابل قبول نیست و منطقی نیست که برخی موشک‌های بالستیک داشته باشند در حالی که ایران از آن منع شده است.
یادداشت تفاهم (MoU) به مسئله موشک‌های بالستیک ایرانی اشاره نکرده است».
«این یادداشت تفاهم به موشک‌های بالستیک اشاره نمی‌کند. هرگز روی میز نبود؛ هرگز در دستور کار نبود.
طرف ایرانی هرگز نخواست حتی درباره آن بحث کند».</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17945" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17944" target="_blank">📅 15:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر سابق اسرائیل درباره ایران:
هر بار که اعتراضاتی رخ می‌دهد چه اتفاقی می‌افتد؟ اینترنت را قطع می‌کنند و سپس هیچ ارتباطی وجود ندارد.
پس کاری که من شروع کرده بودم، فرایند تهیه و قاچاق ده‌ها هزار گیرنده استارلینک به ایران بود که اجازه می‌داد اینترنت و شبکه‌های اجتماعی وقتی قطع می‌شوند، ادامه داشته باشند و به اعتراضات امکان هماهنگی و در نهایت سرنگونی بدهند.
متأسفانه، دولت ناکارآمد فعلی اسرائیل این کار را متوقف کرد، همانطور که تقریباً هر برنامه خوبی که ما شروع کردیم را متوقف کردند.
و وقتی اعتراضات رخ داد، آن زیرساخت وجود نداشت.
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17943" target="_blank">📅 15:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17942">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17942" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTTORljklYbS9GXO9Ui24ola2ihkxf8FeZMsrvHGOp-rqQyMU7YPhwPR_3JhGJFqM6WeUB0qXyYRHad99eli8J-c03T5UwEY_AcMtQ2s-J053sHWln9cpEoXzW154tiTsQWGBb8kY65kG5nQ6BxYNlZ_KF45uYwzuEWxllQm4QZdJEmxphV_EdBn1_av2PmR3dsKGkp3c48pGen3sPAJPm2MBsiEyAt22wLPW3HHYA6E4vyGStqGX_-jLFsyZkO0zB6dOQXLKPeu26TM7CPvqSXysrbmlFPjTK0EviGp_NaLCNVTPEmh0B4iEOGV0oHzpEMqIFjqdWh01TShRoLJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8j_zlwPWv3pmcEA9LV_U7V-Ez7_-C3omCTidCQF_BGX1VVSr5kEkeeGQiN4v7L7i6OPBcHT6hCUmnxYohvo49uRaElgFqPyljUduWL5tQsNtI8G1xA-b-pbHHV9mc66KIOIfxo70S3nXraryovjeJ8nYA49WocE4gLspNk6blKInUCxV9uIUZVKwzbaueaLAKx-zLtu-vOiUo-XSKs6i1gH2upBVNY2ShTAIGwk_hcvmB_UWhPLPRmLAJKAfLGObs_Qm_qTALDGRLZgWochrRL4Kp3MfnBqURfE8HQ9et_UWKL_gCmiTfKx6uT6mC3-mL-RG_V0oXdhLP7V0H5UDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه جلو میرویم داستان رابطه مسعود با شهباز
دارک و دارک تر
می‌شود
پناه بر خدا!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17940" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
امیر پوردستان: آمادهٔ عملیات پیش‌دستانه هستیم
رئیس مرکز تحقیقات راهبردی ارتش:
🔹
در دکترین تهاجمی، عملیات پیش‌دستانه نیز تعریف شده است و چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم.
🔹
نیروهای مسلح هنوز بخش مهمی از توانمندی‌های خود را عملیاتی نکرده‌اند و دشمن می‌داند که در صورت ارتکاب هرگونه خطایی، با پاسخی فراتر از مرزها و تنگهٔ هرمز مواجه خواهد شد.
🔹
در یک ‌ماه اخیر، ما چند نوبت تا پای جنگ با رژیم صهیونیستی رفتیم؛ لانچرها آماده و دست‌ها روی ماشه بود تا در صورت عدم عقب‌نشینی اسرائیل، جنگ آغاز شود.
🔹
تهدیدات قاطع ایران سبب شد تا آمریکا برای جلوگیری از گسترش جنگ، به رژیم صهیونیستی برای توقف تجاوزات به جنوب لبنان فشار بیاورد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17939" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توییت ترامپ در مورد ایران:
با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17938" target="_blank">📅 14:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🟢
طبق اعلام معاون اول مسعود پزشکیان ، در راستای برگزاری مراسم بزرگداشت رهبر فقید جمهوری اسلامی ایران ،  13 و  14 تیرماه استان تهران و 15 تیرماه کل کشور تعطیل خواهد بود</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17937" target="_blank">📅 14:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17936" target="_blank">📅 12:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارادوکس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6w4h_u4q1HoMiZpVp_juOijxpvBWv2Eem35isMa-aEWKvAyw5G23jl9qg6TrB1Qjba6Xbw8UcoxGQHfd1bv6VnaAtqifZ7NS-yArYCPGhDefmgUm5U-9iE28BkU1mEnvWivarYYwAWV4iROOxeyprX6Bl6BvDRxg08l_lElqFxPzJikLHcFYJblQcVqrR-eNiTQrMa8s4EV4gIq7U5-jNXSWST5EsPXjPV7kFVZ8f3dVBszZnjB0Vp5AfaENyCwe6TuFaSFZOtl2U-Kc4gzNHv8BNGir3JrDU1diFruzrfdoy5oiJ1UgWVwpXSBHBcdMsMjRsBsqqzgJsG3RFgXubsF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6w4h_u4q1HoMiZpVp_juOijxpvBWv2Eem35isMa-aEWKvAyw5G23jl9qg6TrB1Qjba6Xbw8UcoxGQHfd1bv6VnaAtqifZ7NS-yArYCPGhDefmgUm5U-9iE28BkU1mEnvWivarYYwAWV4iROOxeyprX6Bl6BvDRxg08l_lElqFxPzJikLHcFYJblQcVqrR-eNiTQrMa8s4EV4gIq7U5-jNXSWST5EsPXjPV7kFVZ8f3dVBszZnjB0Vp5AfaENyCwe6TuFaSFZOtl2U-Kc4gzNHv8BNGir3JrDU1diFruzrfdoy5oiJ1UgWVwpXSBHBcdMsMjRsBsqqzgJsG3RFgXubsF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
⭕️
چگونه نام تاریخی و ریشه‌دار دریای کاسپی (Caspian Sea) با یک ندانم‌کاری آقایان پر مدعا خدشه‌دار شد؟!
یکی از تلخ‌ترین لحظات تاریخ معاصر، روزی که حیدر علی‌اُف، رئیس‌جمهور وقت جمهوری باکو، به ایران آمد و در دفاع از نام «خزر» سخن گفت، حال آنکه سید محمد خاتمی، رئیس‌جمهور وقت ایران، نتوانست با تکیه بر اسناد و مستندات تاریخی، از نام‌های اصیل و ریشه‌دار این پهنهٔ آبی همچون «دریای مازندران»، «دریای طبرستان»، «دریای قزوین»، «دریای گرگان» و یا نام بین‌المللی «Caspian Sea» پاسداری کند.
او در برابر آن ادعا سکوت پیشه ساخت و حتی با صدور بخشنامه‌ای شرم‌آور، این دریای کهن و ایرانی را به نام قومی وحشی و بیگانه، «خزر» نامید؛ نامی که هیچ پیوندی با هویتِ تاریخی و فرهنگی ایران‌زمین ندارد.
⚜️
@paradox_p
⚜️
پارادوکس
⚜️</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17935" target="_blank">📅 11:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrng6JrwgU-EVN_4rhRblVBLVBvSBh27CEeO9tusgc8r62FQsVcaOmnvH_rbGgcxkys8a_sh9R-P5NoCv0RGHG-bZR4O1-LUfPDMsbHGEGs2LqApzFl2-oEtflAnvNNi8QN56_Oh8_i2xs4mKNLvMzwNu6OXfi83qrUL5gHd80h02VGI9DfwT21DUwrhSeUsBTXnIQ3gkCiO2JWTRSUBqH8rNgFIPmD7ZWVheyQlr5o5gbwfCrKR7nGdcXkL5z2xYJBXTWA2ScxEgEZCntz90b91DsTYgi0ThQV-YmHzdFRvJrQ9lvoUMhpnsQjHD1pMgvsFTTj0V8F5d2IlX5iE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت استاد!
از تبیین کوانتومی آفرینش و پایان هژمونی دلار با ظهور بریکص رسیده اند به رفع نیاز جنسی با دوغ!</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17934" target="_blank">📅 09:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17933" target="_blank">📅 07:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17932" target="_blank">📅 07:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر خارجه عمان:    به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز پایبندیم.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17931" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:   آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.  اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.  ما می‌خواهیم شاهد همکاری ایران با کشورهای…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17930" target="_blank">📅 07:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoVab-TfRlDk3E2AyzwXX6eykLd05wvD_rbgeGgtywctICzy43634dZzk9m3TnB3aX-IXoYwZZjcl3W60OGnBgoK2JyBfD84s3CKZd2EEncF3PZxPuYhqBZ31iy5i4qWrppIborfpWXqjKHhOJlcLjQb3ni4IpdXz24brRm7312smLy0TnI4WLCRRLGQXaDIb7tTTkNzaarNmLoEbt7HWDcrz5MieE6Nz5L3JIBK3DRgxudlVsXwtWsaaYUgk589MYq7HIFw8YPDwUXxJKrc8cNLE_ixa9P-NTPCERkHBjrha3j-inO9FyqzN3kUJKVYjiIoIYQjwQa_pkvur1--gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی رئیس بانک مرکزی:  ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17929" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17928" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17927" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل :  بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17926" target="_blank">📅 23:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل
:
بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17925" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oymjnjtOEreP8NF-hwcsG6f6U2b8t9jBFZypIE0hdXOpyTTiAleWvOgIvxoJprk65brgCLu_vwm01SBX2sgE6YzvCfLIcwiuR-SvxAFj60Tga-vbwp35inQCMo-dMDvAfCLwetiPcPtqlssdSxBh6ZMV21sX7se12rrIQTb2N9ez6Ut4ORxAfx5NLJ8w0trMTKS58K5_okPK0qER7WTHYEx-fQC92c_M5GwDUVMiR5gt5fj-m-q6KE091GDMtdsLuEmMuvo3tBYBNOfej02TgqBHMXIB69AFy_uRS9SX3b8_qh7ob63TEkfaECRbRzxTlGE1qQTIZX2Ga6_uTz5jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوستالژی هر ساله ما آغاز شد…
جای کیان رویگری خالی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17924" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی نکند، به مذاکرات باز نمی گردد!   ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17923" target="_blank">📅 22:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هند قصد دارد موشک های کروز سوپرسونیک BRAHMOS را به ارمنستان ارسال کند</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17922" target="_blank">📅 22:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ:
همه کاملاً آگاه هستند که ایران موافقت خواهد کرد تا بازرسی‌های نظامی انجام شود تا «صداقت هسته‌ای» را برای مدت طولانی در آینده تضمین کند.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17921" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خوش‌چشم، کارشناس صداوسیما:
آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17920" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مرندی:
🔻
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی‌به ایران صورت نگرفت</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17919" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17918" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPV1fNBD10NVFBYYr3R2mKatZbMYJwKBLzyHX0kU0IlLO5XiGF48TQNnByhyJl9Z51xir5lEFVZpDgAiYm1qAf9_rwCK9m686hNtdSYdC5Q_qR7Q6ij4N6ijEYbk4jcj313yKbbxDKIDIRfv8qfaqLVa9iXRVoTTGTBN1VEcO7d-9Wtcvo7Wvn3vGy5oCfqpABjXmrEEsFTUUVtyv9gtgfE8alORMmF6XSRBK5O0d3ztDmQpLmJd2Bz-H97ejm7Q7PDUu_Q-iVOK7Q_I0OcsaxJBK4PRoJHb1NiWXlKCbabV-hdI4IvOgNwiCz4YgqRC3L_3VPuzbn4ZNZ3duual_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17917" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خردمند کسی نیست که بتواند میان خوب و بد، خوب را برگزیند، بل کسی است که توان تمییز خوب از خوب تر و بد از بدتر داشته باشد.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17916" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7DyW-_wBEKLw7uMfOhTlYaWUomPUzUTlQOky6zwykVm4JpLW4G8lAeBwYMSsAaySh6uJA9QHyWTPwEpEohgeAnLgEBaH3w_5X7TCuRgLt3FcO9tjLhPz4fXkQb5qewaGll066lYXmkVW1TN4sf3ZT1UTT_BPFybtvZ3ukPBMr9cToAaMuOQdxNa51Nh8O15k9qbyfxLgl70bVfJ37DMtz_nNkI5_cuLahzdHdBH3mZiMg6__5WdKnHFTV3LLaeluOaAS3vSJ3l7Or1RMHcuJxpXriFPAwbrkgxiqYJ9QvHx8zRBVaIpLSsmCp3qooVUqqHCg-5VsxtpHKPZS2gSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxvTYpmbEI0x024lDsjO-XWhs90wCBQBsxRroVwuCsHGH6IFLx9N12kTNVsMNntF1Uih3yaQ-gC7dB5SZxwkx_7nsQemuvPobc-nQBf7ne8pocT5TKFTidCE-PbDRC4vfV6ggxMsoqxJOeJC6U1OziGWh3Vv_X7EAZWUMWgItxO55IKMn6Jc1Ijx4PvZjSxi0zCMB5tdo_vDplyDiikawrGZhwwlWUe7NHewupvoF-2x2p5z55TMWJGetovFIbOoj-r_f-u9GxSKBb4ZnX4hoGJWJZZffD2HiC7S9hjC8r5sxn3X0PvmtOlqje6hTs6gxjPIfLkn8eGpuvB-aGzVNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمیگذاریم اسراییل بزرگ تشکیل بشود اما خودمان دنبال توران بزرگ هستیم و این نشان می‌دهد چقدر مادرقحبه هستیم.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17914" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA_eiR_TQLw77RCRdDtCNJeljZ8akczOYyZoj6BO-yLTnRszlc9tc6ne1qyEtKuOMfm4zwXlCCgW5EqqN8r001cpQv1P_Qzy-dt2-3a3wOJ4p22ohDQt3vYP3-UkAhnewif5QSJ57Tszo9707LLj6oCn1o4BCYwtRGOMHpbSqjiaBKoD8VUFnhsnwdvXj0v-x0jhmGZF5PcsPuos2jngLZWni_FLfh2iMS1tbvCzwaxK3p0Itgu4cMQuGs7XZCvG6bxdQ9WJE7li2aql-sTCpYHvQF265STMfzhLZ9il6ewLjF9T9iWsnAa7ae0I6H0ZN-usgKEaBGmKK-EoJbeR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو دشمن اصلی ایران
این‌نقشه، راهنما و توضیحاتش امروز یکم‌ تیرماه(۲۲ ژوئن)‌ از یک کانال تلگرامی نظامی اخذ شده است. بر نقشه و راهنما متمرکز شوید:
"کوریدور خیانت؛ تمام حملات هوایی به تهران و حومه، از این مسیر و به طور روزانه انجام میشه... آذربایجان، ترکیه"
کاملا درست ترسیم کرده و نوشته است. باور کنید در جنگ‌های ۱۲ روزه و ۳۹ روزه، تقریبا هر شب و روز‌جنگنده ها از بالای سر من میان البرز می گذشتند.
ولی این کمترین سزای حکومتی است که حاضر به گوش دل دادن به پژوهش های بیطرفانه نیست.
بیش از ۲۵ سال پیش، پژوهش های طولانی مدت و استراتژیکم طی دو جلد کتاب با عناوین: مقدمه ای بر ایران و همسایگان (منابع تنش و تهدید) و کتاب: مقدمه ای بر تقسیمات کشوری(ج یکم)‌ منتش شد . کتاب هایی که نه تنها سرداران آن را خواندند، بلکه مقدمه ای شدند برای اجرای پروژه اطلس استراتژیک ایران. پروژه ای که بارها برای سرداران فیروزابادی‌، شمخانی، باقری، سلامی و ...سرلشگران زنده گزارش شد.
میدانید چکیده کتاب ایران و همسایگان چیست:
دو دشمن پابرجا و اصلی ایران ترکیه و جمهوری آدربایجان هستند.
ولی کو گوش،شنوا.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17913" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9qXoWs1fDGaQlOQHUgWrYUWYCBlbY9nJfc92bvXosq8kOfTvhfASTcZ8Wo8gdW5sLBw7sGl1LkN0kUlqbt6ZOBIVS_Eb7d4X6offl6mwf001HxNWvl3yakqZjqE_BM7rko15vdnl6PJCNQNpf4k85_6tyD6GUCPdA10teTQfUb-Q_qJd1c0t55lNkBV8cEjG1Pgo25LNI1l9KlKey-_V4gx2AmEHWL9Au9G7uyo06Nbcp3-h8ZtKmJQi5M__xwl3hpeY0iQMTxveZHK8DRkDpHeFwiZfTpZK2E9PR0fmbMGutnIuf0Qmqov6SW9_ZG4bREKGW2v-GC7IVBNUIiftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/17912" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17911" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17910" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17909" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3LcS9R1WW5xVD5JxTe9g2KPqw4F1X05BN4ageMz-rbtLvkOR2G7JclH2I5x4pSPeOzZAmOpyi7AsuUUQT-iIz-vOeBsb3tjFcfZm1RXeYj1pIkEGTEIXEkfKGy_qvqyQj8_V0K3vS4CZ7MzoPSWCWZFB-INm-i6O1YOBqpvcOWOIFlNzEBN0N9jkfkC9y1XadUTgwJovSso3kxuZIUl1MveQm_MbgQZlXcb7TAfQV5lDG7nkIygpOAadwvLUQ4ZYL3i2iLPar8cz4u3Jnwl_ygKa22rcYI01zcmX3bHHonAANVo1X592AFCyDDG-D9lbI5qxsOCh7lWL5GOvKMYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
یادداشت تحلیلی: آینده بازار نفت در شرایط جدید ژئوپلیتیکی
بازگشایی تنگه هرمز و توافق آمریکا و ایران می‌تواند فشار عرضه نفت را کاهش دهد، اما بازگشت تولید به سطح عادی زمان‌بر خواهد بود و رقابت تولیدکنندگان دیگر را تشدید می‌کند.
در سمت تقاضا، رشد اقتصادی جهانی در برابر ریسک‌هایی مثل دلار قوی، نرخ بهره بالا و تنش‌های ژئوپلیتیکی قرار دارد و همین باعث می‌شود بازار نفت وارد یک دوره نوسانی و چندعاملی شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/17908" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:
آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.
اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.
ما می‌خواهیم شاهد همکاری ایران با کشورهای خلیج فارس در سطح بالایی از اعتماد باشیم.
مقدمات برگزاری نشست‌های خلیج فارس در دوره آینده برای بحث در مورد امنیت منطقه‌ای در حال انجام است.
موضع اصولی قطر رد هرگونه تغییر در وضع موجود تنگه هرمز نسبت به آنچه قبل از جنگ بود، است.
چشم‌انداز ما برای تنگه هرمز، باز بودن آن و آزادی عبور و مرور از آن است.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/17907" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJnfJ2ldAOrBxBHIhx8pJ0PJYgXZ89A05ZlMTIHmzko1-02cAAkmJdviQQFr1eLzWgvM_3TpNdMwDi9cGjm7cFYkv9aMNC9iZ-SyeAq7AkA7SA5AjmphiWPMAaMsgh4PbLQiz-27Yxt0FHQa55gn6SGzSxGAbF8HZpi0ROSKJedMzoD79lSITEo0d3Y3nGlT_fu9U1ycKWv_10LynM3Y_ktQqYQqp4mVVpIz0-rhkrHkWUEx_QrAwnGcf5wPsgo-rG-cZpfEfmL6rQj2JsouYbaCHcWqyq3T2kLKW2kxK_H8vpkl_X1eBoHqi-SPWoQfRiWZobu4u7zw2X5pHH5q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش احتمال وقوع رکود اقتصادی در آمریکا به ۱۵ درصد پس از توافق با ایران طبق تحلیل موسسه گلدمن ساکس !</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17906" target="_blank">📅 15:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17905" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17904" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جی دی ونس:  آنچه جرد کوشنر و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپی است. اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17903" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17902" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جی‌دی ونس: ایران مذاکرات را ترک نکرد؛ ترامپ به اظهارات تهران پاسخ می‌دهد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره گزارش‌های مربوط به خروج هیئت ایرانی از مذاکرات گفت:
«ایرانی‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم چنین تهدیدهایی در شبکه‌های اجتماعی مطرح شد، اما آنها مذاکرات را ترک نکردند.»
او همچنین درباره واکنش‌های دونالد ترامپ به اظهارات مقام‌های ایرانی افزود:
«دیروز به ایرانی‌ها گفتیم وقتی وارد چیزی می‌شوید که نسل ما آن را "کری‌خوانی" می‌نامد، نباید انتظار داشته باشید ترامپ پاسخی ندهد.»
ونس ادامه داد:
«وقتی آنها حرف‌هایی می‌زنند که درست نیست، ترامپ هم به آن پاسخ خواهد داد.»</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17901" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17900" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17899">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17899" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را بازگردانند</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17898" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17897" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17896" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17895" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">— یک منبع اسرائیلی به سی‌ان‌ان گفت:
«اسرائیل در حال بررسی اعلام عقب‌نشینی‌های نمادین از مناطق جنوب لبنان است.
عقب‌نشینی‌های نمادین شامل عقب‌نشینی برخی نیروها از مناطق اطراف خط زرد خواهد بود».</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17894" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">استارمر نخست وزیر چپگرای انگلیس استعفای خود را اعلام کرد.
دو ضربه بزرگ به چپ جهانی در کلمبیا و بریتانیا در یک روز!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17893" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17892" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17891">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجار قطر بحدی شدید بوده که در بحرین دیده و شنیده شده</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17891" target="_blank">📅 08:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیانیه قطر و پاکستان در مورد آتش‌بس در لبنان چه می‌گوید؟
طرفین (ایران و ایالات متحده) توافق کردند که یک «واحد کنترل درگیری» را بین خود و جمهوری لبنان با میانجی‌گری تسهیل‌گران تأسیس کنند تا از پایبندی به توقف عملیات نظامی در لبنان طبق مفاد تفاهم‌نامه اطمینان حاصل شود.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17890" target="_blank">📅 07:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
بیانیه مشترک قطر و پاکستان:
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17889" target="_blank">📅 06:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
عراقچی
:
🔸
میانجی‌گری خستگی‌ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔸
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصره دریایی برداشته شد، برخی از دارایی‌های مسدودشده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17888" target="_blank">📅 06:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17887" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رییس جمهور چپگرا و معتاد کلمبیا امشب شکست خورد و جایش را به یک راست گرا داد.  قاره آمریکا در حال یک دست شدن است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17886" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دونالد ترامپ، پس از ونزوئلا، اکنون کلمبیا را تهدید می‌کند و گوستاوو پترو، رئیس‌جمهور کلمبیا، را «قاچاقچی غیرقانونی مواد مخدر» خواند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17885" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17884">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=Z70a1-KJtZtVEDxI0wZ7iBL36b-NX_ikT2GejSgohhl9U566dUXhHGDWCo-PbDLtS37m45YtMfXkR3v6oRMxssakBxREkur0E4Vc1XRV147wIa7lDS85SDroVH5eiUlpFJx-3B8_3ZnqUAlxUJnbDzvl87CfqbF2177L9tZ2wTfBi7csxnm0yRxPqj-qFs0iIcBdRiOD1T0ErZDXWbrpOyL5hHdAKCnyrR3fGf8KVxYHp9TYDD31VCX8CaFkl9em-S6GEYhD4hD2vZPDzxjtuPUDsX-aCpDoqDKU4xn8KWIdJlT41SiCYjF6Oqs-zQJdtsL8LA0PQtV4cKGsnlyBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=Z70a1-KJtZtVEDxI0wZ7iBL36b-NX_ikT2GejSgohhl9U566dUXhHGDWCo-PbDLtS37m45YtMfXkR3v6oRMxssakBxREkur0E4Vc1XRV147wIa7lDS85SDroVH5eiUlpFJx-3B8_3ZnqUAlxUJnbDzvl87CfqbF2177L9tZ2wTfBi7csxnm0yRxPqj-qFs0iIcBdRiOD1T0ErZDXWbrpOyL5hHdAKCnyrR3fGf8KVxYHp9TYDD31VCX8CaFkl9em-S6GEYhD4hD2vZPDzxjtuPUDsX-aCpDoqDKU4xn8KWIdJlT41SiCYjF6Oqs-zQJdtsL8LA0PQtV4cKGsnlyBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهراب سپهری به جای طارمی؛
😂
راه حل خیابانی برای گل مردود ایران به بلژیک
🏆
در قسمت دوازدهم برجام رونمایی شد
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17884" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17883">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظرم تنگه هرمز را بدهیم بیرو ببندد و خودمان برویم تنگه مالاکا را ببندیم!  آبش را هم بدهیم آقای میثاقی بخورد!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17883" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17882">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17882" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17881">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlqI0u7jpgiHg9gHC7SCP5_eTz1x41ESHWF3rZh1f5UfR_kyUOi_iFWIh2QyjhAkscTXGYrtp7G1f4m_cCYxinY-n9pP2fnm78SfHJcjRwA9Q4sZE_QbhcMmZUJPB8iaDYxFRu_JAhhdNdEMBwIoQnzTDSxSvEwb7KwtIv1Ro9hBMd74qHam1-Rda_saEDwSPixAyTTXndo8AKhcb8k9kptXjbSDNGGo9QcEwvFouOLKpGKB-bs1WjYqilUsUuHJKaGnCvjpvg-twl-8vDnmlz3IhSEAmaWHmTuPPLxLneHig2MsX1guef_pDzBkd7RSsBHj17O8sZwlp_uEFbwVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!  انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17881" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKC9VEzL5mqNnhul8TZ4ALreejut1VLURxUkb19slo8mhWKAGAJk04rY7gQ1c1P5S1qR8mGApG5voaB4qBIZLmvleM1D-PBAHvGeEAvLxsFmRuII6Q0x1vT_9EOQVTCbe2_byQW5W1vn7sNq8PZK1ZEAhVPbXRn3lBnADeYDQtCJsMThq5TjoxCSysiyUvDEj0Fm57OJOQ9K7wOvjr_VirSpFxK1J8bNeQQeu8Yfqh51zE6YrwlxpD7_VkE3ay8fLNMo0Dn4SEwLUqx1m5dM7f_gx8LDIeAizcYGT5zIvb9WXPsq1vKOOMWR39rK5KMsq34NNp-5t58YfOCEDmJqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!
انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17880" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=QM5IaI3V2RgJYbhlwv8_xAPHOZfYNDzX4da8_9I26pmH3qsnFfawnzZhgC4dmYXz6j-PbHyx_bF8GLt5gdLRTHUc5_1skRDbJ8xLg3XLXuqtocprIeEEVwsNqVhA3xlTh-G8AKoy2bkPSPyaxAXkuHxvxnmkMea0nSAMqNNDpIXcXTJ3rlLFVT5BSghuu2_Pb2hftpWsSmNHNd2FajKrkpVgOhTV2iLYH87TVKc6WDvkWMDT-EHMuuFB-fYkisbhZZ17bEFRS5YiYUI9GUZVWfJImVfnRKBQNj7w9JbYaGDWD7aXf4ES2yUA1WCHgXlDGtMO5zHoFeKl8pXv6GQUTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=QM5IaI3V2RgJYbhlwv8_xAPHOZfYNDzX4da8_9I26pmH3qsnFfawnzZhgC4dmYXz6j-PbHyx_bF8GLt5gdLRTHUc5_1skRDbJ8xLg3XLXuqtocprIeEEVwsNqVhA3xlTh-G8AKoy2bkPSPyaxAXkuHxvxnmkMea0nSAMqNNDpIXcXTJ3rlLFVT5BSghuu2_Pb2hftpWsSmNHNd2FajKrkpVgOhTV2iLYH87TVKc6WDvkWMDT-EHMuuFB-fYkisbhZZ17bEFRS5YiYUI9GUZVWfJImVfnRKBQNj7w9JbYaGDWD7aXf4ES2yUA1WCHgXlDGtMO5zHoFeKl8pXv6GQUTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دلال های محبت فاکستانی را ببینید!
شهباز شریف از عراقچی التماس می‌کند تا با ونس ترنس دست بدهد اما عراقچی پشت کرده و می‌رود و بعد شهباز شریف و عاصم منیر شروع به ماله کشی برای آمریکایی‌ها می‌کنند!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17879" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17878">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">راس الفان همان منطقه ای است که ایران تاسیسات گازی قطری ها را در مارس به آتش کشیده بود</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17878" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17877">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرنگار صداوسیما:
هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17877" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17876">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزارت کشور قطر:   انفجار داخلی در یکی از کارخانه‌ های منطقه صنعتی راس لفان رخ داد و تیم‌های دفاع مدنی به محل حادثه اعزام شدند و هیچ گونه آسیب جانی یا نشتی ثبت نشده است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17876" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17875">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17875" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17874">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17874" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17873">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORlOrg6fBgvid3sL3x-p_r5D6yqSaC0WZkD9DNWe5uU2Xlo3OGx-VvMWXg-Sd-fknvvZbdEplfsjLYzSrY1gw4YWaGdUn-YqhZ7eS-dBO-T5P9fuH5qPqCrsV2XB_-w3EyKXjiXSaepdEQdDSlVCOPbYeVAskYRBxcPqRHqHBB342A5bRlePvTz1tUR9VZ3m_gNPlkhucpkjoWlE7RXNvSm_Xz3_bKxZFK64JkYRL8jE2NDDcX_w7SRq6P62F_m66C4myF5awGFRhgL_FyO4S3zjpxrWJt6BUO1HJCwqbXL6L2PfyWGKIcNmFbHMCgRKBsxUfQmSkDX00ICrtcmjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به جای طارمی، سهراب سپهری رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم  》Keyvan《  @OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17873" target="_blank">📅 23:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">اگه به جای طارمی،
سهراب سپهری
رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم
》Keyvan《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17872" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به اندازه قهرمانی پرسپولیس در آسیا از بلژیک جلو بودیم…
لعنت بر پرچم کمک داور !</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17871" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تیکی تاکای عالی از بچه ها !
منتهی در محوطه جریمه خودمان</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17870" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">از نادر محمدخانی به اینور هر چی مدافع تیم ملی داشته امشب فیکسه.
》Footfun《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17869" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">با نتایج درخشانی که همسایگان بیابانگردمان در عراق و عربستان و قطر گرفتند، فشار روحی از روی بچه ها اندکی برداشته شده و امشب با خیالی آسوده تر می توانند برینند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17868" target="_blank">📅 22:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17867" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خواننده Secret Box مدتهاست که از این طرح آگاه است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17866" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسرائیل در حال بررسی عقب‌نشینی محدود نیروها در جنوب لبنان است.
— کانال ۱۲ اسراییل</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17865" target="_blank">📅 21:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17864">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17864" target="_blank">📅 21:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17863">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17863" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.   @StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17862" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17861">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استراتژیک</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=t9QDI_STKpzxgvHuaSfQD2fFBlEci0Zm3-_oFHiLSuNSBgBwXvA_k1hDkze-Ue79YmBJyYjhYT9j0zNqekopb6qGOA9eJn-CBPYABZO8xNLnpII3RSazvJf69h1nqNrrnpg93X3bTFzLQ6n73IZjIs5V9SXsWCvdXWAHaebV_7w5pnx1Mck1vaI2QZbK0_tgpxu9TVwq38r_KzCsU-R54qhnnK3z2cHAO07ACtWas5APkCI-v2DpFWG1CmjF_IcEfkT5vhNH7Elaahyv-CswNWuOkfeLnZHQLJe8hslOQNlO2jfmgOrSzVJS2Z3ByEKMvjZDxmLwmC437jdO7n7yhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=t9QDI_STKpzxgvHuaSfQD2fFBlEci0Zm3-_oFHiLSuNSBgBwXvA_k1hDkze-Ue79YmBJyYjhYT9j0zNqekopb6qGOA9eJn-CBPYABZO8xNLnpII3RSazvJf69h1nqNrrnpg93X3bTFzLQ6n73IZjIs5V9SXsWCvdXWAHaebV_7w5pnx1Mck1vaI2QZbK0_tgpxu9TVwq38r_KzCsU-R54qhnnK3z2cHAO07ACtWas5APkCI-v2DpFWG1CmjF_IcEfkT5vhNH7Elaahyv-CswNWuOkfeLnZHQLJe8hslOQNlO2jfmgOrSzVJS2Z3ByEKMvjZDxmLwmC437jdO7n7yhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17861" target="_blank">📅 19:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17859">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ درباره لبنان:  من ناامیدم که اسرائیل نمی‌تواند حزب‌الله را از بین ببرد. آنها بدون خراب کردن ساختمان‌ها نمی‌توانند کاری انجام دهند.  من نزدیکم که این کار را به سوریه بسپارم چون او کار دقیق‌تری انجام می‌دهد</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17859" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17858">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به گزارش الاخبار، جولانی در جلسه‌ای محرمانه وعده داده که از حزب الله انتقام خواهد گرفت. وی گفته :  «حالا نوبت حزب‌الله است و ما انتقام خود را فراموش نخواهیم کرد»  به نظر می‌رسد  که در صورت حملات آمریکا به ایران، جولانی از وضعیت برای باز کردن جبهه‌ای علیه لبنان…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17858" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">من دقیقا نمیفهمم روی چه چیزی به جز پایان موقت ۶۰ روزه جنگ توافق شده؟!  لبنان؟! تنگه هرمز؟! موشکی؟! نیابتی؟!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17857" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17856" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17855">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قراردادهای میان کشورها تحت فشار (Under Duress)  در حقوق بین‌الملل، قراردادها و معاهدات میان کشورها باید بر پایه رضایت آزادانه (free consent) منعقد شوند. مفهوم Under Duress یا تحت اکراه زمانی اعمال میشود که یک طرف با تهدید غیرقانونی، نیروی نظامی، فشار اقتصادی…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17855" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مدیر Secret Box از اعضای تیم دیپلماتیک کشورمان ممنون است و به شرافتشان درود میفرستد!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17854" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxMzBpQ7cDIDdZOVX4SIsFDen5I8kLv92AqdrMPJk83M9oQ9LBO2hBiUM2H8is0TpZSD-ADHEC6k_uu3K2dka9TnW53xq5igtPyBQ1UfcnWxRfpa4pYjb1ijU3zSUqzZ_8m3H8iWclQeneekJ6Bqxh_yOhv59Suk-xRUmbRkT24fB9jR2OMy9nO5ODJ3B5V1rUiezXqqrwdxfuscNbpJC-TW73d7xRL4YKr3sRwt3cI5mGnVtUvfZllcm-Sag5ExoodksSS6bDOpVm9kD0FDvAKOTJfMvZq06MOH2dem8HnHjT3kHY5FvDacY0raaiZcSNAltgDETZpUNH4QH-T2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17853" target="_blank">📅 17:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17852" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:
اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17851" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">— وزیر دفاع اسرائیل، کاتز:
"هیچ محدودیتی برای سربازان ارتش اسرائیل در لبنان برای اقدام به حذف تهدیدها وجود نداشته و وجود ندارد.
آتش‌بس دیروز اعلام شده، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که جوامع شمال اسرائیل را محافظت می‌کند، باقی می‌گذارد.
همانطور که نتانیاهو و من روشن کرده‌ایم: اسرائیل از منطقه امنیتی در لبنان عقب‌نشینی نخواهد کرد".</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17850" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
