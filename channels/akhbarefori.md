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
<img src="https://cdn4.telesco.pe/file/EIbChDLiprBGLeWi_AjEm5HQ_VSD-ntUMeY0GIrJl5tsx6PBtSc168y4XQYn6zN4IbEpNCd84QiUKhAuvmipc-6ce3gUzizyleju6c4Z4XU_Pc6HxhWTQ5kaP9euYhPYG8nbCKYwOyesP2K6yeE8UOUuNvlls7t_xoRgj6zk-kWYzzMDuEyEK0vhTvuB5fEM7Ccc8Lds0sGloNUvOAMfEa1D5lHb3xn5qWbLkw0webzTlYVz5WpI1yUHbw4eidn4N3kumT48J6JBs2nVW21WKZ01qrf-ziG2DMvGFxVDrMlD7paPML3d5DpYMX2QZO6Xgiqhvj01EPHPxn4zBkazFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.99M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 08:36:54</div>
<hr>

<div class="tg-post" id="msg-652357">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=WSmGaz2AYQJRzyIxFIm8v4SGKI7kPPMJ6HjVcGnwpz27lQmzQ3zyeUxYpEpvpXjPyTf8I5YiAXtN5t2noAC-Pda-Q3VUsW1nwDS-ECtgMUE737LcfQpEkMugajuyRcSaIRrA1_-SKQS_bufm7K3FfXw1yP0NDiqmMYJssPg3R2omoiT0jl81Tz2Gy5xUAGhMyJ7UMcLNe4lEWgbJ17o-PDBAkixFm5xkAeq7f5RWCWWAkO_qQxnT4XgAOExXA2zyaT4JgTVyfk9RMJCxYc_N2C6lzVT0wPFhsbJTTlcTHYPBEZA9_93vW6L6P63hhfo5GDa4pvqAbinMn60NAjfEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=WSmGaz2AYQJRzyIxFIm8v4SGKI7kPPMJ6HjVcGnwpz27lQmzQ3zyeUxYpEpvpXjPyTf8I5YiAXtN5t2noAC-Pda-Q3VUsW1nwDS-ECtgMUE737LcfQpEkMugajuyRcSaIRrA1_-SKQS_bufm7K3FfXw1yP0NDiqmMYJssPg3R2omoiT0jl81Tz2Gy5xUAGhMyJ7UMcLNe4lEWgbJ17o-PDBAkixFm5xkAeq7f5RWCWWAkO_qQxnT4XgAOExXA2zyaT4JgTVyfk9RMJCxYc_N2C6lzVT0wPFhsbJTTlcTHYPBEZA9_93vW6L6P63hhfo5GDa4pvqAbinMn60NAjfEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجۀ آمریکا: در مورد ایران، درخواستی از چین نداشتیم
🔹
ترامپ هیچ درخواستی از رئیس‌جمهور چین نکرد. منظورم این است که ما در مورد ایران به‌دنبال کمک چین نیستیم؛ ما نیازی به کمک آن‌ها نداریم.
🔹
ما مسئله را بازگو می‌کنیم تا موضع خود را به‌روشنی تبیین و آن را شفاف کنیم تا آن‌ها درک کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 241 · <a href="https://t.me/akhbarefori/652357" target="_blank">📅 08:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652356">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت بیستم</div>
  <div class="tg-doc-extra">سردار عیوض‌خان جلالی</div>
</div>
<a href="https://t.me/akhbarefori/652356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
«سردار عیوض‌خان جلالی؛ مردی از دل قدرت و توطئه»
🗓
این قسمت روایتی‌ست از یکی از چهره‌های کمتر شنیده‌شدهٔ تاریخ؛ مردی که در میانهٔ بازی‌های قدرت، جنگ‌ها و توطئه‌های درباری، نام خود را در تاریخ ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/akhbarefori/652356" target="_blank">📅 07:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652355">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edecf976c1.mp4?token=UUpaRWCbrzc8JJfv5y-g_li1xbFgigZ00APhdPGUHbVOlTZ4dnTA19HWy2C3JGF_kJFL_CE9jbNFuBLtbkDiVJcKJy51gDKTPsYm3eH5U4knw0ESP6Sm-_qCQvcX0I2JaIx1lC7mXEPWHSw48LCXSFBm83X4TqF7c-H6-R8kMSBGy4RFAY-eyiWEhTr5p05sXY0YmbcfGmKn3NTk_byF-E8dOPzjddnrB0lZ1u-mrWX39KiDUEO7bfxCz96QwEzJAPrxipNPVK4lP7db8LnG-Xxz4JU-6X2tHYtmAY10Li9suiVxk9Skj6vpDN65wFpmAXCh7Ll2_W2CQRT1-9jCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edecf976c1.mp4?token=UUpaRWCbrzc8JJfv5y-g_li1xbFgigZ00APhdPGUHbVOlTZ4dnTA19HWy2C3JGF_kJFL_CE9jbNFuBLtbkDiVJcKJy51gDKTPsYm3eH5U4knw0ESP6Sm-_qCQvcX0I2JaIx1lC7mXEPWHSw48LCXSFBm83X4TqF7c-H6-R8kMSBGy4RFAY-eyiWEhTr5p05sXY0YmbcfGmKn3NTk_byF-E8dOPzjddnrB0lZ1u-mrWX39KiDUEO7bfxCz96QwEzJAPrxipNPVK4lP7db8LnG-Xxz4JU-6X2tHYtmAY10Li9suiVxk9Skj6vpDN65wFpmAXCh7Ll2_W2CQRT1-9jCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای دینی به کرمانج‌های ایران‌زمین؛
به آنان که در مرزها زیستند،
جنگیدند و در تاریخ ماندگار شدند
قسمت بیستم پادکست کافئین منتشر شد
☕️
📜
روایتی از زندگی عیوض‌خان جلالی
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
🎧
https://youtu.be/IpMt8R6uBX4?si=5ppbO4oz91FFpq6i
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/akhbarefori/652355" target="_blank">📅 07:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652354">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
کالابرگ سرپرست‌های خانوار با ارقام پایانی کد ملی ۷، ۸ و ۹ شارژ، و امکان خرید فراهم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/akhbarefori/652354" target="_blank">📅 07:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652353">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4NPeuD7Kp2uG1SsYvu3HO9lsYkAkOhPfzvqXZl5dJeayPpya8we0pCgapCNFJyeFr8EJSwcPRumKSS-FnP6W-GJzhVt6QuxAkXqxf7fS1u3XgIvmOaMYGFl3LEArNja5cmjgi88S3iuyoLrYMRFmYZTP45B5GStLgD-fXyedNG0fzc2rBkRN8aP_q5oiF8IcL0Re1TyTWpxKaVUOjngkChHAroGkG9cTnJz10FNVuBnWfwidLnS7Xo28sKFivngH6VXPogigszi3tH1O_Nnk98Ez5BnvMBsQXNJ7ofXjiGukx9aXHZ2VxGCvAi9QfnmR7vA8reaO77fErv-GWl5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۵ اردیبهشت ماه
۲۷ ذی‌القعدة ۱۴۴۷
۱۵ می ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/652353" target="_blank">📅 06:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652352">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
یونیسف: ۲۰۰ کودک لبنانی از ۲ مارس تاکنون شهید شده‌اند
🔹
طبق اعلام صندوق کودکان سازمان ملل متحد، از ۲ مارس گذشته تاکنون، در پی حملات رژیم اسرائیل به لبنان، ۲۰۰ کودک شهید و ۸۰۶ کودک دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/akhbarefori/652352" target="_blank">📅 06:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652351">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ترامپ: ایران از نظر نظامی نابود شده است
🔹
رئیس‌جمهور آمریکا در ادامه ادعاهای ضد و نقیض خود بار دیگر در مصاحبه با فاکس‌نیوز مدعی شد که ایران از نظر نظامی نابود شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/652351" target="_blank">📅 04:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652350">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2e84f307.mp4?token=fXXw-oUlIUATVIMSIubXCAb9MjDit2ATJKH1subVYximDmOZD5uRJG52jYEO_HdN4vJbzSIM8EegXqLuTzH2AAmEaUjxOthVjDsBj36vbSAlkgfm2cM3y7bGkuaCpYyyep-D_wqk0gqRbXPUt1CcjtXcyY5A6AVAs1EwuTSL5BF0G4LtxKWIX4okc5yESAx6m7tgjbviMjKKJLqbmEqTqYMkPpGzQ7QaCNWOaxiUs51cbm8RBnTy_apRf-BXmx5GmyKrKTWxPCVFC_Deb6znYJkFdU-owlAUuu7cvrTHoSOtDBaxGmZyeojtmWPYW3acRYQzXCrhc_4tVteTt6uUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2e84f307.mp4?token=fXXw-oUlIUATVIMSIubXCAb9MjDit2ATJKH1subVYximDmOZD5uRJG52jYEO_HdN4vJbzSIM8EegXqLuTzH2AAmEaUjxOthVjDsBj36vbSAlkgfm2cM3y7bGkuaCpYyyep-D_wqk0gqRbXPUt1CcjtXcyY5A6AVAs1EwuTSL5BF0G4LtxKWIX4okc5yESAx6m7tgjbviMjKKJLqbmEqTqYMkPpGzQ7QaCNWOaxiUs51cbm8RBnTy_apRf-BXmx5GmyKrKTWxPCVFC_Deb6znYJkFdU-owlAUuu7cvrTHoSOtDBaxGmZyeojtmWPYW3acRYQzXCrhc_4tVteTt6uUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجلس نمایندگان آمریکا با ۲۱۲ رأی موافق در مقابل ۲۱۲ رأی مخالف به قطعنامه اختیارات جنگی برای محدود کردن اقدام نظامی علیه ایران رأی داد. این طرح با توجه به اینکه برای تصویب به اکثریت آرا نیاز داشت، شکست خورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/652350" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652349">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423faf9ee6.mp4?token=IfogXBV1bUF8suxoGCSnn-zsr1eJvejc0n3y04hJ25QFpTKaJIxGZImJnYlSEU9ffUp1V--EjKH5ePLjJhv51qWkNlmdtDlfJfGkkhhHhGB56RNdllnnbTHAWnQdiaxcJAxxij4WwNbravWPH4vE27u3kpleTLl-3omOn-smxsd7Mzk5r0bikiX92p7XVJskYOTvH-H8v7_DHUC6ptwVRwZqUOGzVY0wV2T6bah1sY5sKmWENc_okF8Q_HfTKX__-QC9k17lVM-E0A5nxYCCHULHdf7pDi8V2jshyqyH71mZxf8K2GyUeHD3JcUmfKGa0TuqDIdGpOa4AERsS53OCiKR50eESBjeZTjrSMhD2orMNC8V07LFTDoYlguz6IURB-bNHPFvT6ChdcNtaiwQFl8pVcHXCZSyepip8M5VS9UcvsmPBpQGukl3h0ocf5veJNeScDP91eJjPb7j1G_nAMdw3imuJ7LvBXyGif-1DTAaQaxLCxMySn0EqsoQpKDvS0ETWZoODEQK0_QFj2-zyzLX2BMDuD0n5t3ezhbuzBcv18oLTCJXccvBPV6n6vV2bQcMuskvSCMuEtJWtZP8ZbTXcYr1OJo2ExcS1PQd4piaBD3V5Zuj2_FRLWSg7GAAXQnzV6ajoitotgQ99bPGPAcXhfH036ewG18CcYAKv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423faf9ee6.mp4?token=IfogXBV1bUF8suxoGCSnn-zsr1eJvejc0n3y04hJ25QFpTKaJIxGZImJnYlSEU9ffUp1V--EjKH5ePLjJhv51qWkNlmdtDlfJfGkkhhHhGB56RNdllnnbTHAWnQdiaxcJAxxij4WwNbravWPH4vE27u3kpleTLl-3omOn-smxsd7Mzk5r0bikiX92p7XVJskYOTvH-H8v7_DHUC6ptwVRwZqUOGzVY0wV2T6bah1sY5sKmWENc_okF8Q_HfTKX__-QC9k17lVM-E0A5nxYCCHULHdf7pDi8V2jshyqyH71mZxf8K2GyUeHD3JcUmfKGa0TuqDIdGpOa4AERsS53OCiKR50eESBjeZTjrSMhD2orMNC8V07LFTDoYlguz6IURB-bNHPFvT6ChdcNtaiwQFl8pVcHXCZSyepip8M5VS9UcvsmPBpQGukl3h0ocf5veJNeScDP91eJjPb7j1G_nAMdw3imuJ7LvBXyGif-1DTAaQaxLCxMySn0EqsoQpKDvS0ETWZoODEQK0_QFj2-zyzLX2BMDuD0n5t3ezhbuzBcv18oLTCJXccvBPV6n6vV2bQcMuskvSCMuEtJWtZP8ZbTXcYr1OJo2ExcS1PQd4piaBD3V5Zuj2_FRLWSg7GAAXQnzV6ajoitotgQ99bPGPAcXhfH036ewG18CcYAKv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد منان رئیسی، نماینده مجلس: خسارت مستقیم جنگ به ایران فقط ۳۰ میلیارد دلار برآورد می‌شود در حالی که درآمد هر سال عوارض تنگه هرمز ۵۰ میلیارد دلار خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652349" target="_blank">📅 00:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9Zk6rST7UQB7gnFonX8VWuIWTOlZyholRD5WEoR6m6SovOOvLlDwGx8lnZJb80MK19acwzL4vogacPsJWmKDslC5Gv0m7RqT5pZw_ZmzEW0wntXmcimkLTO7DHSAP2l_Xo1ZFHcHaagtkVA9vkcbcD7Iik87NtT7OP3BKRDaHCcOdUScYooGbnNegi0OyWmalDvhbarWXZ3uiKMzKAVoV54zdANkBm9HJVyGf5vRZMiF0-mVSii779vjNQO-xcINx1LRK2YbYWIFEyhHvtkZT8Lhmav4OP3DUfyaGib0ol99gT9RnqpexUEDEui-nX4JYT99S0HP6e_BjdAVAAvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMaRjkbm4QEkYap3vo0EFhS2c-JjNnC_j_j_LZrRdKCPu9aBcKDIZOm8zCR0Q4_-6vyJK4cXIBLd7OY6wmAMs_XX40MIiu389ry1DD9XpGZtjrpWub65q596wWTCOWO9PBwSprdL8_mHDQjZhFmwqzJ8X57H_cY9mJke9awUafCWj_L35bf5P0M-kWxPuaBNYz_NSd8cLjbr_ZLkTef4qgiVn_dB6XoVmdnumKWXQY6qubXBuN-akaQ-pxsLXmsrlWteH1jp6xpunPMKUbsnu_wjUplklA5RKpeSrAf8iShMZgqi6i59RTNehZrctchPBrRAjWKOjm2ELGQfIeBpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-d67MEeZwdhLCxWK8KfCx0mqmeSREsulBv4ml67Pi-AjW-JEzg1N_26zVfjfBfOZec7hbONNeYfMYZ5Sjp10JQb30ZGJ16vUsfb6Yd7G-nvPAbfAEEaB4TS9HvkGagymMf_9BGSlQNB-66dIUga56glaZmy-8tOjtjs3OYrPuEbmN58IIm-JTeOtHwLjck9fQ71Bl1QsAfM8B1iupEF_eI0EmtrXnuhy0Yy20wJS-zvm0CvolSQCyb0leSp8dt8g8rpwa8jcpQ1B0TNuVSESJrXQ5CPnIe-5DRyYoeIub3UJBhMRi61bLbCPF-RZY9k0DWea8WD3tQsGk___WBTZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حنظله: مغز متفکر سفر نتانیاهو به امارات و معمار اصلی توافقات ابراهیم هک شد
🔹
گروه هکری حنظله اعلام کرد که با هک «ساموئل شای» طراح سفر نتانیاهو به امارات و معمار پیمان‌های ابراهیم، شبکۀ مخفی او را افشا کرده است.
🔹
به گفتۀ این گروه هکری، شای نه‌تنها هماهنگ‌کنندۀ اصلی تمام توافقات پشت‌پرده میان رژیم صهیونیستی و کشورهای حاشیه خلیج فارس است، بلکه تسهیل‌گر کلیدی روابط پنهان اقتصادی، سیاسی و امنیتی میان تل‌آویو و ابوظبی محسوب می‌شود.
🔹
براساس اسناد منتشر شده، شای، اپستاین را به «سلطان احمد بن سلیم» معرفی کرده و از این طریق بسیاری از حاکمان فاسد امارات در شبکۀ اپستاین گرفتار شده‌اند. موساد نیز از همین مسیر برای وادار کردن آن‌ها به پذیرش خواسته‌های خود استفاده کرده است.
🔹
گروه حنظله اعلام کرد امروز ۲۶۵ صفحه از تماس‌ها، شرکای مالی و ارتباطات محرمانۀ شای را به طور کامل در وب‌سایت خود منتشر کرده و تمام اطلاعات مرتبط با شبکۀ مالی او در کشورهای مقاومت را در اختیار سرویس‌های اطلاعاتی کشورهای دوست قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/652346" target="_blank">📅 00:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVSBzQOCZ3xwMTMbbYoVDKp4QPJeENEMKI2kpYaKkg_7OgtLBo5_ZuhHT6jgvqs0JSimE9qhOZUHff7S8n4gNrwGmxlm3M8KSnS3j7wUdUnzH125z8kPt65KRqujCyyjA9gJsUPqvQ8E8BYG-e3ry660dxLOUcsillzLDcCcXYVcQjQCQ9AU0pAHT5wp83IfWfJ_34gBZbEwwy2sBpXLbH3uGVdQhglhvZBY0oYnJ1AlH4MwPcXhtqMF5eWKe_sxzraT2R7h3LsgTpXoKRfC6nNwA7d1imBj4df1U7tokbSRQDKIiCRe3aJonRwoBzu0XQW_kU5IGHkmt87UrIH3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منوی شام چینی | دیپلماسی خوشمزه | شی جینگ پینگ چه غذایی به ترامپ داد؟
🔹
در ضیافت رسمی که روز پنجشنبه در پکن برگزار شد، رؤسای‌جمهور آمریکا و چین، پشت یک میز نشستند؛ مراسمی که فراتر از یک شام تشریفاتی، نشانه‌ای از تلاش دو کشور برای بازتنظیم روابط سیاسی و اقتصادی خود تلقی شد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214964</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/652345" target="_blank">📅 00:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf56a8776d.mp4?token=lj-c2PxXfTiMGsIjlDuE6jm8Tyv37pcTxxC3EpTSW4dc-q2IvfRQ5gCPDePSqw1iwFn_M676OYVpGFE3KrOarxgNCXtCAk5NEQKQujwJlK6kOMbCjLQxiM4Akf8Wr6OSmPpjr-py_QMzmXOjPGugckUSe5Ho_PvGtbmxyTsaQbRwm-LHs-LAGYMpBgTI-KSZ6gl3Mfclmo3hE_KWYX-ZDFAulmzenuAlsCYsA4eec5q-dJdivje86plsE_IOrPSPPyBULGMxz_TKDxKRkIbpg5L6PPXulLCjxnxp7MIZf675bBE-ql1GZe_Hdt-RMZwfZIwfPzuW0UykAmCahsBZxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf56a8776d.mp4?token=lj-c2PxXfTiMGsIjlDuE6jm8Tyv37pcTxxC3EpTSW4dc-q2IvfRQ5gCPDePSqw1iwFn_M676OYVpGFE3KrOarxgNCXtCAk5NEQKQujwJlK6kOMbCjLQxiM4Akf8Wr6OSmPpjr-py_QMzmXOjPGugckUSe5Ho_PvGtbmxyTsaQbRwm-LHs-LAGYMpBgTI-KSZ6gl3Mfclmo3hE_KWYX-ZDFAulmzenuAlsCYsA4eec5q-dJdivje86plsE_IOrPSPPyBULGMxz_TKDxKRkIbpg5L6PPXulLCjxnxp7MIZf675bBE-ql1GZe_Hdt-RMZwfZIwfPzuW0UykAmCahsBZxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طفرهٔ فرمانده سنتکام از پاسخ‌گویی دربارهٔ پیش‌بینی بسته‌شدن تنگهٔ هرمز
🔹
هیرونو، سناتور آمریکایی: پیش از اینکه به ایران حمله کنیم، آیا این فکر به ذهن شما خطور کرد که ممکن است ایران تنگهٔ هرمز را ببندد؟
🔹
فرمانده سنتکام: فکر می‌کنم صحبت کردن درباره اینکه آن گزینه‌ها دقیقاً چه بودند، نامناسب باشد.
🔹
هیرونو: بسته‌شدن تنگهٔ هرمز توسط ایران به ذهن شما خطور کرد؟ بله یا خیر؟
🔹
فرمانده سنتکام: تقریباً ۱۰۰ بار از تنگه عبور کرده‌ام. من تقریباً هر روز به تنگهٔ هرمز فکر می‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/akhbarefori/652344" target="_blank">📅 00:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: به دشمنان هشدار می‌دهیم اگر دچار خطای محاسباتی شده و به امنیت ملت ایران خدشه‌ای وارد کنند، امنیت آن‌ها را در هر کجای جهان که باشد، سلب خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/652343" target="_blank">📅 23:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اگر فرصت مرور هنه خبرهای امروز را نداشته‌اید، داغ‌ترین‌ها را اینجا کلیک کنید
🔹
ترامپ پس از سفر به چین چه خواهد کرد؟ | بازگشت به پروژه آزادی یا حمله به زیرساخت‌ها؟
👇
khabarfoori.com/fa/tiny/news-3214896
🔹
وزیر جنگ اسرائیل دوباره تهدید کرد: هنوز کارمان با ایران تمام نشده!
👇
khabarfoori.com/fa/tiny/news-3214942
🔹
بلاتکلیفی درباره ترانه تیم‌ملی | معین پاسخ تاج را داد
👇
khabarfoori.com/fa/tiny/news-3214908
🔹
بحث داغ مخاطبان خبرفوری درباره حمایت از تیم‌ملی | نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3214858
🔹
ماجرای رابطه ایمانوئل مکرون و گلشیفته فراهانی چقدر جدی است؟ | سکوت بازیگر ایرانی و تلاش طرفداران رئیس جمهور فرانسه برای انکار یک افشاگری
👇
khabarfoori.com/fa/tiny/news-3214881
🔻
ویدئوهای جذاب هر روز را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/akhbarefori/652342" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKMDiMa0Gw51tR8RREesTMB0sHA3scl4LC-Vjywx-P4hPxKoH5gxkpzQkf26OnHQK2xNsTOvUA3d5VcVAoZcEepT7P2wV5hHKt4r2bUbOTQ4vQHfao1dI7Kbc431y9tNLh1frjpVs0t4BFxDotvaDsrNEjLASi46OAK-2Ys6E69l0P6cYY96rprE4-xRq_55wwFe8xJ6XwRrWfsee2G8vhSw5PnyY2jBep42YpZUzcSollKu7WpIyVahEAhwY1MMjjJlxWl76sAJ1tuTHDYgJ3XpKfYX10rGR8xO4Vv6II3bB_ALXFb4wQxIcYyiBIlxPMXfAgT0kfKu5ktfY3rSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مورد عجیب یک فرد متهم به جاسوسی برای ایران در اسرائیل
تایمز اسرائیل:
🔹
یک راننده کامیون ۲۷ ساله عرب-اسرائیلی به جاسوسی برای ایران متهم شد.
🔹
ادعا شده که او به دلیل خصومت عمیق با اسرائیل، با میل و رغبت اطلاعاتی در مورد مکان‌های حساس ارائه داده و حتی خواستار حمله موشکی به زادگاهش شده است.
🔹
دادستان‌ها ادعا می‌کنند که به احمد داعاس برای فعالیت‌هایش پیشنهاد پرداخت پول داده شده بود، اما او از دریافت پول از تعهد ایدئولوژیک خود برای کمک به ایران در طول جنگ با اسرائیل خودداری کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/652341" target="_blank">📅 23:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKIsGzJv7QXd2Adi8QvCZCOu26GPQ8sizDnI-KtYqCXD8tmLeLLfhq5lC0m0ZH__8NxFrPyl13SsCdRVbHFEbM1re9JQZtuGQQnou03kmLL0fdoIGz4T_lU2W-jHXupmWPhZxlB_1Wppipr6sOwrFNhqeBWjkzyPrT_swtBMwiBm6VOoARUM0JAMCZILzPKcYE9esqLDo3-UoHmFx9o_GBU5_Kuo6IJ7F5FodDEqUfb_vGvVsE8xgNajBarWt1vxVGzLkPUCYjVQNHgP5lAaus1C52thtsCDJWS1ZcZuWiwFuoXJzsyM5Vx5aRBUi00nPG8TxfXfbRkNEbmWE_cdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای رابطه ایمانوئل مکرون و گلشیفته فراهانی چقدر جدی است؟/ سکوت بازیگر ایرانی و تلاش طرفداران رئیس جمهور فرانسه برای انکار یک افشاگری
🔹
ماجرای پیامک‌های ایمانوئل مکرون به رهاورد(گلشیفته) فراهانی همچنان فیصله نیافته است. با وجود عدله‌ای مبنی بر ارتباط بین این دو شخصیت، هنوز بازیگر ایرانی عکس‌العملی نسبت به شایعات مطرح نکرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214881</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/652340" target="_blank">📅 23:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حملات موشکی حزب‌الله به شمال فلسطین اشغالی
🔹
در پی شلیک ۶ موشک حزب الله، آژیرهای خطر در شهرک «کریات شمونه» فعال شده است.
🔹
شبکه ۱۲ اسرائیل اذعان کرد که سه موشک در اطراف کریات شمونه اصابت کرده است.
🔹
منابع صهیونیستی مطابق معمول ادعا کرده‌اند این موشکها به «مناطق باز» اصابت کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/akhbarefori/652339" target="_blank">📅 23:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uih4MmyjezqaRnFKCi1k5Jkd6hxYk7LSYEoemBwaLAEs0nJZENuloHoHZdZVk0w8ocMjgJcMww9PGHzYlKhk9OEJ0k4xTxokIGgP-x1B2rUrgqpNJxL241pGvBvWeZ-2dDyh2SKgvxUaGnvcAtf7xhtwe2NASPPYwhl7r1r35XIZvcNDXjLEg5JCVtDQGyHMroWwpoEfD5AGcZnDVvJ-58pMeHIM0Uhkucqv5TTq6bNPJ3RLIbYv6z_Orq7q-3QHRq0IRKxxHww1fN5ARjr_5Rt6JJoUQaOS5ZA_KLSmL5-u1uhOyyY0JrFSzj89RBZZ5G8cQquI5mYE1bv9mQ3N7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک روز معمولی… اما با انتخاب‌هایی متفاوت
🔹
از صبح که چشم‌هامون رو باز می‌کنیم تا آخر شب، بارها و بارها انتخاب می‌کنیم؛ کیسه پارچه‌ای یا پلاستیکی؟ قمقمه فلزی یا بطری یکبارمصرف؟ ظرف شیشه‌ای یا پلاستیک؟ این کمپین داستان یک روز ساده است؛ روزی که با عادت‌های…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/652338" target="_blank">📅 22:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652334">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6yJw-qBziafyphSNX8CJ9Z29zSIHCFVlDFvQKA-5pCGUdcEFUsP1dfzr2XAj95WlLMZx22OK_wE4dww_nfQfxSHrXbNw4DOYVBrgufI63_FXpLBGLh1tqh_lBogDJV5yZ11vtmoN0zXsogBN_bwiscK1dzDNdDdlIwgQlApgSKOn8jSyQVuYvVPPE-2zcQJVLVetoTdQWun7PGzSZw8HlBUP61arrZruTusbLSNV0eEB-JKnAc8-X9SVQ6u2GjG3mMXx_QlzBOaykPixp5rhwzKaXFXuIDnkqfkt-YdWvuwwpcyvrZSo3bYe_eBm6E66VDR7xr0tZMYOFRHLqzCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/culsHchWLyXDpTfnAtJPs8olU2uUrcdg5mCo7EAhSzgruWxe0PLIl4aQQlqla4O-2Tr4oP7UX1Fo6nWZ5DD4FKAxecboEf9CJPFFeZZOJ6g3gcz4BAxLhhJDqsMv11sHSZIhiVsg-mHsHvbw6j7WBU4gi8zoxS6mxprqESXXh2X5G8Y2Lbk2bJ9FE_j6GFjgBCqUX7pE1YIfWyf-hC-NUuf3Ye-J64U2rou_OXYS71NKwedd1hSc2loxv7TggVcLXDSCMqz3ib_9I_vg_IJurWcn6BwfKKJFPtH51EL2VIFlN-l2VJ0Xk_JLCs8qN802KAXqWthYSOva4k_BjdTMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNom6YfB7HKUP8gEgIwZa697t7lmp3VGy3M9UdVb7RWhJUTwrfdFqqlEaq2h1C75XwxD7fJzEo0Ay04ePydbqTr1hLGlNjUXnJIR9Z3yPbpj8emVV6kVHtDE86ZeTg2dEh3SMWsa1EkQeDGyGzTg6VF8XNi6F4px-GJBbDwJini3f1YNGSqWixiaua8rrMzh1LEOm43A8qlbNzlu_DRfKw4m1LsnBGqvfoYu-VmhzZnnMds_QItLRhB1TivnK4Evqdn4JMZ7i1dxPovfb4Ns5t99aa9A3fBXas0uAolUndgVLhSsTuBDQ4YKVPrW2JyZbYxWvDVkMgxC5Xvt0FNhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elzFMKMc3WlqdaH2rHbKKAFDJQwcuVJPNyA13T0fbi4x--YmfhGYC2_qcB_Faltbm2MuTcHNGFSWXVyTGAyOqui7PuMC4jvMgWx_s-TnnfiyBWdGOHo3xBvs0Lj_XjCK_7nsm5FPd-JG5gapryCATNR6g8KEYxde5mj7M9XfhykgljOrE6wBseyqMDaWoHY4J6mur0DtGHaQkIhP17Xl58pVQFdJ3218deF7YPQo1KKOmsuZAMA95ZXn4Go9uhxEXnSDOa6UGnaS8O5WyGvZZIcPs7zqPIoTQM2nww5BJjpFYnW3i5PShggQudpMa4tnw8XLYw8QVVO-HaldV5msrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس | صهیونیست ها تأسیسات کشاورزی فلسطینیان را در شهر الخلیل به آتش کشیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/652334" target="_blank">📅 22:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652333">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82aaf1c68.mp4?token=UfkDL-0k5FVTpI65J7QruyXp1sFv6TMUEApfLYVLsHVxMbUh3mb4tXvuWJKcmwiSEHe9zKwwoecJl0IQYHjkRvdyvutFx3YWzBQgvE99iHSivLT6qAIPUZSx553WchGQ50rBo7UkXMxuTTyM_SAj11CFNngojoaWZ5xLfX3WbM-uzF7lowqe6iya8Ue-e9C7yyRdGSqlvOZ57vU11pRj2Otphoi6SgY5dpcFE9jaKt60MvhOPX5m3xbuBGQ360jCz-4ygOWCA-XTywjNTsG2UMSp3i7jzJp6bkJTZmH7hWf7ueT-8XK8xLIw1S6pKraS6NOQdBFKJs8hy3ETYBmLYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82aaf1c68.mp4?token=UfkDL-0k5FVTpI65J7QruyXp1sFv6TMUEApfLYVLsHVxMbUh3mb4tXvuWJKcmwiSEHe9zKwwoecJl0IQYHjkRvdyvutFx3YWzBQgvE99iHSivLT6qAIPUZSx553WchGQ50rBo7UkXMxuTTyM_SAj11CFNngojoaWZ5xLfX3WbM-uzF7lowqe6iya8Ue-e9C7yyRdGSqlvOZ57vU11pRj2Otphoi6SgY5dpcFE9jaKt60MvhOPX5m3xbuBGQ360jCz-4ygOWCA-XTywjNTsG2UMSp3i7jzJp6bkJTZmH7hWf7ueT-8XK8xLIw1S6pKraS6NOQdBFKJs8hy3ETYBmLYYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقب‌های سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/akhbarefori/652333" target="_blank">📅 22:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b008f364.mp4?token=svIGOabiQoi453jZlv9EkzoOpISW5fP6yhcqSY04llarIw-DONYBowB0_F_POLJJJYkdpo7yHD2HtOKT1JmAV3BUNHdVW1b8Fo0n8_smzJx-_dCdiHhemqpI8ePAyj0sjCUxBVYCvb6vvolc7GbpI0mVVOGX7Ykv9id5nl9csdU6JAnPG4lkloh0kDJckirDynngb0aoLcexifTyy9DbYMyGjGEIERU4OTgx9uVsdqSbRgCdnD5ngsWZ_yEzgadKKPvMHLc4coweeVte1meBvxeAVI1Xa-wXd3pOVzh8hNR3d5bstPqbNHBhxKaJ220EngxE8dRSuGP-LFyubaC72oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b008f364.mp4?token=svIGOabiQoi453jZlv9EkzoOpISW5fP6yhcqSY04llarIw-DONYBowB0_F_POLJJJYkdpo7yHD2HtOKT1JmAV3BUNHdVW1b8Fo0n8_smzJx-_dCdiHhemqpI8ePAyj0sjCUxBVYCvb6vvolc7GbpI0mVVOGX7Ykv9id5nl9csdU6JAnPG4lkloh0kDJckirDynngb0aoLcexifTyy9DbYMyGjGEIERU4OTgx9uVsdqSbRgCdnD5ngsWZ_yEzgadKKPvMHLc4coweeVte1meBvxeAVI1Xa-wXd3pOVzh8hNR3d5bstPqbNHBhxKaJ220EngxE8dRSuGP-LFyubaC72oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهدید سخت کویت توسط عضو کمیسیون امنیت ملی مجلس
خضریان:
🔹
کویت فراموش نکند که تنها در ۹۰ دقیقه توسط صدام تسخیر شد و امروز هم حد و حدود خود را بداند که جمهوری اسلامی بسیار قدرتمند است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/akhbarefori/652332" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3f2d6c8e.mp4?token=QZoGnEWQBPyfnjqt61KlJMvb5PI7PkOCHmtwmQT2YFAdxNrl5urOkEx-lcHRMifiEK1k1Leh1ds2KunVTeaSW_fp5ivhuOTvTGDKn_Qwx1EdaLv06TgGkdFKc5zhDe6aoXP8QVy3zOeZ6Ae2XjW5glh-J0d9Kza7q1qviP19E3IM5VwB8SfLvQCKlLRpRYkKMhZOBFKBPAUXipElTb_s8Nxa9Xvqs1-XxCora1mJDc5jfgnJVF885Eg3M2QjTKYZh6W5oe-_cbZ5OxdYM5woZFLzgnTWa60k8M6HSQnk09rvCkWSHvNccGSABju6cbUXQFv7_8aicGDJqYe8-RyavjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3f2d6c8e.mp4?token=QZoGnEWQBPyfnjqt61KlJMvb5PI7PkOCHmtwmQT2YFAdxNrl5urOkEx-lcHRMifiEK1k1Leh1ds2KunVTeaSW_fp5ivhuOTvTGDKn_Qwx1EdaLv06TgGkdFKc5zhDe6aoXP8QVy3zOeZ6Ae2XjW5glh-J0d9Kza7q1qviP19E3IM5VwB8SfLvQCKlLRpRYkKMhZOBFKBPAUXipElTb_s8Nxa9Xvqs1-XxCora1mJDc5jfgnJVF885Eg3M2QjTKYZh6W5oe-_cbZ5OxdYM5woZFLzgnTWa60k8M6HSQnk09rvCkWSHvNccGSABju6cbUXQFv7_8aicGDJqYe8-RyavjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طبق صحبت برخی افراد نزدیک به مسئولین و مقامات، در صورت شروع جنگ مجدد نقشه اسرائیل چه خواهد بود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/652331" target="_blank">📅 22:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652330">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKk4OjTdi-qSYj59YkXjRH1tmVo4QLf225Zz2SmZ5_qMNOx_23VlsCoErpPxJAWLPJwF4WMihliDhl6XhQDMt_bvdY3Hy8G7d-Tu0ibJntGOLA9zrovk7vugDj9u76_Dsj-cG8X-c7MbWByFv8cQCeqrrGxHpgx0cg3BHIQwU-c93JU-Yl7h7iD28Vf7sSeYcPmeajU3YfcZ-AAJBAYTpgRKbt7epOQs7ot2d4DXW-cUbLVacFCiBcCNS9Y0-iRtr77Qj5PjZJar54Exv92HLZg19Y_V9U5nOZbNz8KpcCWVrtQfqiSRWQFgWbIdjjJQqrxi0yMn0Y-u2YPjDQLsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر مدیرمسئول خبرفوری از رسانه‌شناسی قالیباف در میانه نبرد در میدان و دیپلماسی
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/652330" target="_blank">📅 21:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652329">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آمار ناراضیان از جنگ با ایران در آمریکا بالا رفت!
🔹
طبق نظرسنجی جدید مرکز تحقیقاتی پیو، سهم آمریکایی‌هایی که معتقدند برخورد نظامی با ایران «چندان خوب» یا «اصلاً خوب» پیش نمی‌رود، افزایش یافته است.
🔹
امروزه ۵۱ درصد می‌گویند اوضاع خوب پیش نمی‌رود، در حالی‌که این رقم یک ماه پیش ۴۵ درصد بود. تقریباً از هر ده نفر، تنها دو نفر (۲۲ درصد) معتقدند که اقدام نظامی «بسیار عالی» یا «خیلی خوب» در حال پیشرفت است.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/652329" target="_blank">📅 21:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652328">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8421f0494.mp4?token=Le6ISYTb3zKkxa5utaklst5t_usRVdkn4b8STtTDnERZs9HQVCYCSKVdQ5a0Lx_B6T0nHzcGst1TEftU0qOYLQWC_BIBy4Eoa7JeoVWwXbhA1LQ1xP8QlriEKoJG90VDOyzfKXhzjYVAI1y1GXEbYRHeCYfA55CYUWDvZHln-cphf2zIujo2Yzd4OkhcJ3izxN4jD9Ht0UIL-dgxQcWYEpjJ2KwTDSWEnkpUhfVwtH3H-7VRDObKLf7y5s0x3ujgmmx9PZkRJix0G2K8yQygxj89gYa8fj1hYF18R4_b9eVHwEpBu6aVlkCB5_0VAkqEKAzfzXn11MsIxLqQ9UmZdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8421f0494.mp4?token=Le6ISYTb3zKkxa5utaklst5t_usRVdkn4b8STtTDnERZs9HQVCYCSKVdQ5a0Lx_B6T0nHzcGst1TEftU0qOYLQWC_BIBy4Eoa7JeoVWwXbhA1LQ1xP8QlriEKoJG90VDOyzfKXhzjYVAI1y1GXEbYRHeCYfA55CYUWDvZHln-cphf2zIujo2Yzd4OkhcJ3izxN4jD9Ht0UIL-dgxQcWYEpjJ2KwTDSWEnkpUhfVwtH3H-7VRDObKLf7y5s0x3ujgmmx9PZkRJix0G2K8yQygxj89gYa8fj1hYF18R4_b9eVHwEpBu6aVlkCB5_0VAkqEKAzfzXn11MsIxLqQ9UmZdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت کارکنان بیمارستان میناب از مواجهه با انبوه دانش‌آموزان مجروح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/akhbarefori/652328" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652327">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQp_hy6GvezYXo_npN23uydFb2kiEVLOuoO5YfejbVByhAYM0wF3NnUAMrbBt0V21IVgnw0IUHleKQFsD9DUuK9YKQqNNf8IhYRj2EAQV2S4VKf23FUjBMRhWM7yDmA5vncBk7_aeg_rVw4LZMNpM__fOsNg9lOIKNmmZNza6aQ3EfjLme7OUc6tN9P8MrYFM5kkD2CmzaDaGl8xli1Sfwr06sVCF9WHYmEqcIDn2c6eHhfDhvD86iIU-y-GYEA64y6dV5F9DtBe48EwIoSVq70Fno9RSRAwFv1J3MB3EcWOnmq61C5Xa_3XfKKKt6FFXiGLnXcLCTdLVNqm5KndJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان سناتور آمریکایی به مشارکت اعراب در تجاوز نظامی علیه ایران
🔹
عضو کنگره آمریکا جونی ارنست روز پنجشنبه از همکاری گسترده کشورهای عربی با آمریکا در طول تجاوز نظامی علیه ایران قدردانی کرد.
🔹
ارنست در اظهاراتی در کنگره آمریکا گفت که کشورهای متعدد در منطقه به تجاوز نظامی علیه ایران کمک کرده‌اند.
🔹
وی در این باره اظهار داشت: «عملیات‌هایی که علیه ایران و متحدانش اجرا شده، بدون وجود شرکای فوق‌العاده در آن منطقه ممکن نبود.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/652327" target="_blank">📅 21:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652318">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhQZ-BmL5ZQhZBVrBjXXRC3L6icsvqz_nbcgwPjTeRorCk0l5JGCg5YwxY02T_8YgQGnuX9_qKwv49WUk54Ex4f44iqy97T78HmyHVpaS-g1Z7bvzkWoZ0RLwoJIJRojGq8lBY_ygZVznF3GrQkF9Rbnuzedttq_d93nc9cdRl6YDv9yuF4sY-T09gkj3gDSrVyVn2BftRopfbSb89Rq1JVoQWO4XpbemQiWNQB1tkfWhkXU-ImktLUEuqspGbu3wj-qn6EOx83PPEp0ZZBourvBQ6ONm-SzV4D_uL7Oa6HiIP8CCXTaP0qqfGa_I8sijjTIg-qFw1FuJOROzJ7kaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOCpnq5esvUoadXQ8Iw1wfslUH04p5wkfOIqXfW9itqA2KGdSYgCYELUgWW0F7coYTlLlO0SiiP8QHQRoT8JgWsOps9FP_pYQb3kbASLsUmHpfb5MhCnOAIpAsmrLFNSXs8EwoFbfMQUnIjJQ1t8e7vNK4iEqRQd4S4uDVixC30BTKCT_86iufijKXw9zulTdJE6FTPa-_qy2ZoN0wUKXogCq67T8GqhNWW7pVQ7nkT6Hxowz2vi3yNVzru7aeWv0DuXFsW9FYeuxL1Iia8CDrhzGN9rMXnOe0DnvKE0lAZpVwvuZjqhz_-q7Eji0KCKsYWtrFWlactP5E2e2bHDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJ9oXLp0NCcaMzWYpy3Ubd_fLz02iKv1XuHB77XBdrO8cC73NX2hhnK3E7uj5HOdiqJJVBBe8Zldgzc0GsGkH8ABL0-H5EMn6k_thhnvDYNexadSibsWX6e430h3r8juf7qOTb3Ql0rca7pTnFwjPG_64L44Si1cUV4ytDT1yhJBsmcdUVuiigUTsBKxPzzrb4CQd5NHiH8Nour_FIoJkXE5CxCoEuHlh3GIxD4mdiQF7txqbpbIrMUXCGjfPE1VM3nU-CuR8KIlnPLmm2oE9NH36C55sgH2thnIJ0PDJ-o9ux2j9qT56FOPrVJc8u6xPbfj9tdNRo14ZfnIXZ4sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUN3HgZ2Lle7Q_RgSz0PTNRImfSv0kt8j0EZjGv2TUD9saDIkeZMGW8J7VqJ-ZNB8IyeWhTtoEkwMR6vlCgCI9oA8WJjg_SXlP2lCHTKUJ-MrednpD9kH-L38RQKJaQT5DxlzZcuSdFIk0gYw_TPRWuh7_jnIqGlJcYrqmx3WJ5kvTROJzwXM7zNAkwe8A5cl6qHJEqoFITk4dCbo9J_FlevfUgDebmcmop3cuEn5wjTO6AeC-zDtlsyPuL4sItpYljnlfm3HUVEs5tpo-bSBHNsF3h4fOGu_tJof8Ste3nVa8qOAOkKgKejhdyV4EgFzzyPznijKWTUpPFd0Gwjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAfAc9u6Jzh1CJrlcaAWtCM0ljaGPOu13js_7Z_Q8GVrf7kFBi63GvgKpIqhdWTY8nlOFP0F3ykd688ygSm9qu03mJWQPcaBUIw1UVx09rCxww0UCIc8akojcwxOMez2rX6_Cp0torX8gbjvaTK71ex9xSlVx8pb7W_7i45wsZpL00v0ksu8kuNEkbTH8u4Zai7ZvuoTUko_9Lo2TX4wtjFYHzeWzLZfzQc1Pa1ICO-3TuhIDQhR0jUtjPxSaINVgCtRgiHVAYdL5pvD9NP-G_lgoVoFvoPqVqaoJOi_dhtt86r41kT6bEK8ruXTCrLhEFzIAryENKtsw4bQNbd2FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AF0GR8H9tbo0xoEXQrmlu2yxcXcxcEKlVtryR71inLy9twHSVYRzIGxIwNo12VCYzlRBHYG0Ybv7oQqz_lBzSCi-EPqvEPi-vUsaHEn69h-XLpSEm1V7jehEsQzUPMFjVd8ujjJGdbFrRfIVswrqHePeQEDWoDqEisWxwAsBX7zd10q_AzNa0pqP6kAadoPpLjRmUc2DCtlC_Z9g-1ajH7zxFBDymbeXAGQ4KOVGVgm9QBHSMOot1bBHYfl_mPxibrleylXWU3BYnR4MSdja2PI2Mg3acGV30UVUaUw4xPASiHAhLcwyLvUscwiQhw3zq_BRby7yX0W3VyrsxpWSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfMcEA9QE7U-8HDaCUupShj6STymw-Z4cj-KMPd6y2NaUc-gpIimoN5YhAp0sN9tekQVn-vG0ATJ95XqABt17te0aJ33XfXKQURMmgth0_DlB_A34BRAfsdeo7LBleAJEs1YgyXnQBphmFw2ozMY3fwhSqLX7Ju0NKGxgDxqoPk1NUidhnZWFmWiJIr2c5V5tDoVvOuAi54jzhUt-hFuZwZuh2jP-pvWLx3N2o5jiNKM__MoHmThENoeaBs3dfSnQoee7UPO3nCkI95_o80YbQk_2g-r0LNp-8QkDIKzFo2D2ZgG0OXCurqgFQtGGCoD5ENxX26SLZtF6DXsWotY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jB-BCqzeW4vqDZeMHqSi9RSvS5dAWO06dpQwMIkpbTiCG7-ekyWsibAwKjdRPgog8BN2CZ2vOksGpAjkAaFsq40urf-HOQnJBIgozIQSURP-hT-MAn-lS4t5hljlEZechTdsDGID3SMl3SxWi67WQ0P-zTHaHkW8ncY1J1eAQ1MUK7otkluUNNFf22NX_glE4q8yTG9o8z-JS1Qt-QZcupKUd6hUwZYcs1V2Wqtk-4ZrDCkAgTu9yFaLwI6KP9PKV3VY_4rEUMxRUjJW6vw2a8mfEK5VjKgbmtdFlLLmgaD4ylmuxr-iDxpM_nzGZ3fMi40nP5aXjuksHh6TZ0IuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DowIZQQdRomJeC1Lt8mnP6kZMmHFAsBd5yyft2fBbtsqkolnU0rCh-yQpp1L5LVO6EkrCkLVzF2yJqxBf9sKgP6h7VKhUAWFJFibHFHFagxaRdsbPSM5PIJlQfJRk3Qfq9sflyHdw18qf-FbfdyayGr4jbgyaS0-nihPOm_FIdnyfdMiwxnEW5pqy3jR6Ku_S_EmIk9IFH4xhs9H3QJNU50V9z8ai8jf-htPgBMyoZCnlwNVs9_I6AiLhUu5H6YpkaFEhssGH5IWt2B2xPf-mJgkJfW8rJAnm1sfsEHmhLuRGUL7ncdA8N0oCjqkzBn7lN3EfJBmDER-D9PWZH6TQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازیگران موفق در دو تجربه همزمان
🔹
فیلم‌های شبکه نمایش خانگی این روزها بازیگرانی مشترک دارند. بازیگرانی که همزمان در دو فیلم ایفای نقش کرده اند.
🔹
در این اسلایدها بازی آنها را در دو فیلم ارزیابی کرده‌ایم.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/akhbarefori/652318" target="_blank">📅 21:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5004c897f.mp4?token=aASBQye5GuUaTfAtk_-MoT3uokvUlc4bYtqpByZGAJ2CeaECYIBPs2_PCy0WaEudivKMjoW5IRw-n0zYdxjRq5Kk65prAYNX3omJvdifILqprd9jZhVm9MTEy1S2eWdGOYaKY0dTAtBYzJgkiBQxvWv-waW7eprXGeLffcLaC65q8oPM5-PZ6Y8ANgw5ZFauDa9DhLu4vSEeUbL9FiWiqAbPbEtDl-RsgFFCPp7_C_Up_SUlFvyefjmxuj3hSTuZTz33X6EvEVJArZ_5I2cTMPu6QFSuZLiHWbxsfRDlipdKHaD0rjubRJtabGlW7-91qB2hF3su8xvNiu5xiLh7rUccrrdHuds_14VaeWt68U_i4IXCHZ7up6iN2Ksb-I1h28wCMYq5VqGppqYbAdl4OJKFNaf-kK3WJpk7EafugAlO8-PTAqoK9gw29vTBEv3rUqvknMGkawsIS8WdvuxCxvkVZz1TB06J3cZFGy07tmPr7Tzei54lQEo3tZHeG7lTaZDIKO093HiVexw4eLn5vcDgukfhJcxW3vqKo9s73lcFta26ohTK9OistYMHnM2Npax3kbRkuqe1mrFJtuqbW8jv35xb95ZiUcxBPHfL2lH8nhzCdsFQki-lVakniQyP293annS91hnHRKtB-NKMWSj0y0ERHzfghqqkbz1kb7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5004c897f.mp4?token=aASBQye5GuUaTfAtk_-MoT3uokvUlc4bYtqpByZGAJ2CeaECYIBPs2_PCy0WaEudivKMjoW5IRw-n0zYdxjRq5Kk65prAYNX3omJvdifILqprd9jZhVm9MTEy1S2eWdGOYaKY0dTAtBYzJgkiBQxvWv-waW7eprXGeLffcLaC65q8oPM5-PZ6Y8ANgw5ZFauDa9DhLu4vSEeUbL9FiWiqAbPbEtDl-RsgFFCPp7_C_Up_SUlFvyefjmxuj3hSTuZTz33X6EvEVJArZ_5I2cTMPu6QFSuZLiHWbxsfRDlipdKHaD0rjubRJtabGlW7-91qB2hF3su8xvNiu5xiLh7rUccrrdHuds_14VaeWt68U_i4IXCHZ7up6iN2Ksb-I1h28wCMYq5VqGppqYbAdl4OJKFNaf-kK3WJpk7EafugAlO8-PTAqoK9gw29vTBEv3rUqvknMGkawsIS8WdvuxCxvkVZz1TB06J3cZFGy07tmPr7Tzei54lQEo3tZHeG7lTaZDIKO093HiVexw4eLn5vcDgukfhJcxW3vqKo9s73lcFta26ohTK9OistYMHnM2Npax3kbRkuqe1mrFJtuqbW8jv35xb95ZiUcxBPHfL2lH8nhzCdsFQki-lVakniQyP293annS91hnHRKtB-NKMWSj0y0ERHzfghqqkbz1kb7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ چین به ترامپ: خرید نفت از ایران را ادامه می‌دهیم/ آمریکا می‌داند که اوضاع دیگر مثل قبل نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/652317" target="_blank">📅 21:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652316">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3669d8d576.mp4?token=Ic0WogCEO56ECnJBTf_OXx40a9vKRGCbJ9pUqlumNGEnGyxC1lO8udB6g_q6jP6BlXVniaREyqMX24o0Yvt32G4HAeTYUqQMK14JT_8nPsfxVIRYI_hGfb2fQ_7NfYzcFOC1ZTM3l0f51-PA5r5G3QMlbBUltLvk_en8xslx8o3c53XZsw4QUTR1RwMJSJxl3Eqltxkk3a436duxu91z4MwzplQBwrkaOuqsGRbMcngeRZ0dkWAV5a6E9VVV84U3ODO1xv4kUJBzSL5R5j8SzJQ835zG5FhhXUsoOLyKKjic5hUtBzMAhNsUwQQbk3anQEY5VB9DFifRiOOpRifjm4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3669d8d576.mp4?token=Ic0WogCEO56ECnJBTf_OXx40a9vKRGCbJ9pUqlumNGEnGyxC1lO8udB6g_q6jP6BlXVniaREyqMX24o0Yvt32G4HAeTYUqQMK14JT_8nPsfxVIRYI_hGfb2fQ_7NfYzcFOC1ZTM3l0f51-PA5r5G3QMlbBUltLvk_en8xslx8o3c53XZsw4QUTR1RwMJSJxl3Eqltxkk3a436duxu91z4MwzplQBwrkaOuqsGRbMcngeRZ0dkWAV5a6E9VVV84U3ODO1xv4kUJBzSL5R5j8SzJQ835zG5FhhXUsoOLyKKjic5hUtBzMAhNsUwQQbk3anQEY5VB9DFifRiOOpRifjm4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناتوانی فرمانده سنتکام از پاسخ به چرایی بمباران مدارس و بیمارستان‌‌های ایران
🔹
گیلیبراند: ما داده‌ها و اطلاعاتی داریم که نشان می‌دهد که ۲۲ مدرسه و ده‌ها بیمارستان در ایران هدف قرار گرفته‌اند. شما قوانین حقوق بشری جنگ را رعایت کردید؟
🔹
فرمانده سنتکام: بله. جلوگیری از تلفات غیرنظامی یکی از دغدغه‌های شخصی و جدی من است.
🔹
گیلیبراند: پس چطور ما ۲۲ مدرسه را بمباران کردیم؟
🔹
فرمانده سنتکام: راهی وجود ندارد که ما بتوانیم آن را تأیید کنیم. نشانه‌ای وجود ندارد.
🔹
گیلیبراند: راهی برای تأیید ندارید یا هیچ نشانه‌ای وجود ندارد؟ کدام‌یک؟
🔹
فرمانده سنتکام: نشانه‌ای وجود ندارد.
🔹
گیلیبراند: خب، این نشانه‌ها همان مطالبی است که در منابع عمومی در دسترس است. آیا شما درباره این ادعاها تحقیق کرده‌اید؟
🔹
فرمانده سنتکام: خیر، تحقیق نکرده‌ایم.
🔹
گیلیبراند: چرا تحقیق نکرده‌اید؟ این با ادعایتان در مورد اینکه دغدغه‌تان جلوگیری از تلفات غیرنظامیان است، هم‌خوانی ندارد. من در این مورد یک گزارش می‌خواهم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/652316" target="_blank">📅 20:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
به دلار چقدر دستمزد می‌گیریم؟
🔹
حداقل دستمزد در ایران طی ۱۵ سال گذشته روی کاغذ رشد چشمگیری داشته است. این دستمزد از ۳۳۰ هزار تومان در سال ۱۳۹۰ به بیش از ۱۶ میلیون و ۶۰۰ هزار تومان در سال ۱۴۰۵ رسیده است.
🔹
اما وقتی حقوق‌ها با دلار سنجیده می‌شوند، تصویر کاملاً متفاوت است. حداقل دستمزد دلاری از حدود ۳۰۰ دلار در سال ۱۳۹۰ به تنها ۱۰۵ دلار در سال ۱۴۰۵ سقوط کرده؛ یعنی افتی بیش از ۶۵ درصد.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/akhbarefori/652315" target="_blank">📅 20:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5e2d40117.mp4?token=JiKtwAniDzUJ5vGN_D8M9Ih3XXThcADlF50Ox0dgZQUccz8PhHMYe3qFxlzxeZ2a1qLU3NXBVYoHXKdXmPt0ROG0Sw1BDY8TueaLvQbZl-Mnvexm-OK_H6Uog6oZ4-URt4JErx12xAU8-7R6oEphQMcwmY_xaCcoBmPCxetqhHRsYUdzzkPUOccLB_GEOPsAkAkTW9S3t5t8L-kNe9HDGBWR1IJVHfGweHRKtW7Cuefp4bwxR68QQQIE2eA7EtCqLFi0pMNpe4ZL0chtRQKE7Dcu4afX3BWUQBVye4IT5x3tks2PG6KrrnUUzEl6StQkje_T0L6R9F0MSuMgTZvXag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5e2d40117.mp4?token=JiKtwAniDzUJ5vGN_D8M9Ih3XXThcADlF50Ox0dgZQUccz8PhHMYe3qFxlzxeZ2a1qLU3NXBVYoHXKdXmPt0ROG0Sw1BDY8TueaLvQbZl-Mnvexm-OK_H6Uog6oZ4-URt4JErx12xAU8-7R6oEphQMcwmY_xaCcoBmPCxetqhHRsYUdzzkPUOccLB_GEOPsAkAkTW9S3t5t8L-kNe9HDGBWR1IJVHfGweHRKtW7Cuefp4bwxR68QQQIE2eA7EtCqLFi0pMNpe4ZL0chtRQKE7Dcu4afX3BWUQBVye4IT5x3tks2PG6KrrnUUzEl6StQkje_T0L6R9F0MSuMgTZvXag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی باقری: سازمان شانگهای تروریستی نامیدن سپاه را غیرقابل قبول دانست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/652314" target="_blank">📅 20:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65f2ab3c19.mp4?token=twdhHvnuo1HxEWmCnT_95tr3VjEu9Cfce6jafDSXe5b6V80iCN2KpTyt-OxoVfFLpWrkJq7Qk8RWYw8Fe-35HVzZz8IJpy9PaDEtPppL2h_kqvf4nf1N3U6OW6WUSiL-gSC0Orb93MPsL01K0E_1ZfvwRSwgYGYyZsCY6gRjBq886Qx6jOTkNnUC8c0_kFoORQyvIHm63LPVRrSI1NhaHr0hRr4LpOb_XRUep4P5l0l3dl6xldbgK5MQHTCK9n36jTjYnsZWdGCn4awBYUB624YlBgQYDhWDHbydlByrNI1i1gMIOHUXiqE-XNVEEwR_IE8PfFvH8Ad27LM8Tf3vsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65f2ab3c19.mp4?token=twdhHvnuo1HxEWmCnT_95tr3VjEu9Cfce6jafDSXe5b6V80iCN2KpTyt-OxoVfFLpWrkJq7Qk8RWYw8Fe-35HVzZz8IJpy9PaDEtPppL2h_kqvf4nf1N3U6OW6WUSiL-gSC0Orb93MPsL01K0E_1ZfvwRSwgYGYyZsCY6gRjBq886Qx6jOTkNnUC8c0_kFoORQyvIHm63LPVRrSI1NhaHr0hRr4LpOb_XRUep4P5l0l3dl6xldbgK5MQHTCK9n36jTjYnsZWdGCn4awBYUB624YlBgQYDhWDHbydlByrNI1i1gMIOHUXiqE-XNVEEwR_IE8PfFvH8Ad27LM8Tf3vsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض سناتور آمریکایی به هزینه‌تراشی ترامپ برای مردم آمریکا: هنوز هم روزانه یک میلیارد دلار صرف جنگ با ایران می‌شود
🔹
سناتور گیلیبراند: قرار است چند روز، هفته، ماه یا سال دیگر با ایران در جنگ باشیم؟
🔹
فرمانده سنتکام: ما در وضعیت آتش‌بس هستیم و مسیر پیش‌رو توسط سیاست‌گذاران تعیین خواهد شد.
🔹
سناتور گیلیبراند: در حال حاضر، ما همچنان روزانه یک میلیارد دلار هزینه صرف جنگ با ایران می‌کنیم. مردم از این موضوع خشمگین هستند.
🔹
این رقم می‌تواند صرف کاهش هزینه‌های مسکن، کاهش هزینه‌های غذا، کاهش هزینه‌های درمانی و پایین آوردن مخارج روزمره‌ای شود که به‌دلیل جنگ در ایران مدام درحال افزایش است.
🔹
معنی قیمت بالای بنزین و گازوئیل این است که هر چیزی که آمریکایی‌ها باید برای خانواده‌هایشان بخرند گران‌تر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/akhbarefori/652313" target="_blank">📅 20:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFYBmGoOnHsgn_ubjw5fm65iJK-uo7cS9t04VRS4Erd--blLMt73bR6_CFE1XbtXZh5btpQyzkgCx-dqYs0ThfaIq4m_TolyUMrs2QwxbDiyWrXbs9yBBqaSVywlHLpPOaWLSkM_RN44CEd4S_DW6yZWjN5Bszr8JoqE998kVvAKbVC28IX0heS-0Ld69aLkPPRamOqH-ju0_9ueludLCpj3ggHZ6UGpomoM1ryXzuMRKFx6TqNw5Yp2Q9XsJPu2pb047mSLXpPp5UzD3rQtG-1H6CC51ROx4eznP_ZKGGWAftY2PkVOK0g6g9rjNkBR_UvwfD-ttbnWwJmA0M1Gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منوی شام چینی | دیپلماسی خوشمزه | شی جینگ پینگ چه غذایی به ترامپ داد؟
🔹
در ضیافت رسمی که روز پنجشنبه در پکن برگزار شد، رؤسای‌جمهور آمریکا و چین، پشت یک میز نشستند؛ مراسمی که فراتر از یک شام تشریفاتی، نشانه‌ای از تلاش دو کشور برای بازتنظیم روابط سیاسی و اقتصادی خود تلقی شد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214964</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/652312" target="_blank">📅 20:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b68453adda.mp4?token=LMUO3d0WFgrZRcACYBiv9iwq4xH5NmDU7U4QWYi4wfMY-a6nEu-5P39UvboMCffHdAJo1QwsHiayUZkVLCGODv9sO0KvwnAsQwpeYAQ2d38IjxPLUNdfbJED5WoGC7R_6p2CyH04QTVpRzc0qIcY4j_-vWJhTWXykuyPb0vcc0pxKjFvgb0IQraHUd0Tvl7Axvn8QZKg1sIvtjm56NBIlCnjdA_2OqP3gT3jKiTVSzqL3Z2ZAz4cWP5lb_S08aGK6O5LQfstrPKPZd6TYg6p04JgaR6E4qHCSYzvSYnt7zQG90kyUEQAw084a3R5LxbsHfT8ieudCVlyTxVGdCjYyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b68453adda.mp4?token=LMUO3d0WFgrZRcACYBiv9iwq4xH5NmDU7U4QWYi4wfMY-a6nEu-5P39UvboMCffHdAJo1QwsHiayUZkVLCGODv9sO0KvwnAsQwpeYAQ2d38IjxPLUNdfbJED5WoGC7R_6p2CyH04QTVpRzc0qIcY4j_-vWJhTWXykuyPb0vcc0pxKjFvgb0IQraHUd0Tvl7Axvn8QZKg1sIvtjm56NBIlCnjdA_2OqP3gT3jKiTVSzqL3Z2ZAz4cWP5lb_S08aGK6O5LQfstrPKPZd6TYg6p04JgaR6E4qHCSYzvSYnt7zQG90kyUEQAw084a3R5LxbsHfT8ieudCVlyTxVGdCjYyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف مهم فرمانده سنتکام به مشارکت حکام عربی در جنگ علیه ایران: ۶ کشور عربی در جنگ با ایران کنار ما هستند
🔹
۵ کشور خاص هستند که به معنای واقعی کلمه در کنار آمریکا درحال دفاع هستند: امارات، بحرین، کویت، قطر و عربستان.
🔹
هر آنچه انجام دادیم بدون اردن و همکاری نزدیک با اسرائیل غیرممکن بود. آن‌ها فقط مأموریت اجرا نکردند، بلکه در کنار آمریکایی‌ها خدمت کردند و از آمریکایی‌ها محافظت کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/652311" target="_blank">📅 20:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaGPB6i9IFmkqhVQcL6S1UAenyG5i8stfHK8BIgNquFIzzyXYuu8LwCJS0dyYUrIAlAxmICaIzf67gMpJFaQz1s8DBg1IUJfwZTICUoo1pfPKDLT9lyeCa9qWtbTcskBaPWZUO5yxGaNmH8ZxICMFUd4DXh0i5Xm6weIJPeYw8EvEUIBuwDYg5dYCRj0L97CSYTrik4NHUhLVFhuVJgzSZJQUhws17TVZ-36blhZYMUtiH8vIYi4RKUVGDSX-lXXRyUzLV87CYCZjcPhhQtqmEvBJ-MHqlW0AZDmhXOSL-9f48cQ5pzzngJP5C6avPAjYClLlRoRoD0Kk3feBqJbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرایش جنگی اقتصاد
🔹
اقتصاد ایران در سخت‌ترین روزهای خود پس از جنگ به سر می‌برد. عبور از این شرایط دشوار، تنها با همکاری هوشمندانه مردم و مسئولان ممکن است. وظیفه مسئولان در این میان شفاف‌سازی کامل منابع و ذخایر، توزیع عادلانه کالاهای اساسی، حمایت واقعی از تولید داخلی، کنترل پایه پولی برای مهار تورم، و ارائه گزارش دوره‌ای عملکرد به مردم است. مردم نیز باید مصرف بهینه را در اولویت قرار دهند، اسراف را کنار بگذارند، از کالای ایرانی حمایت کنند، از احتکار و هجوم به فروشگاه‌ها بپرهیزند، مالیات خود را به‌موقع بپردازند و با نقد سازنده، نه دامن زدن به ناامیدی، در مسیر اصلاح گام بردارند.
🔹
هفتصدوچهل‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori
,</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/652310" target="_blank">📅 20:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhENO2JXH0axl0Q3xXNIa0A4asUSH_6dG5PUi0-J3p2DRecJJCZwPo4zjCZkgh7DW4_16ZRnUcySiTYXlXaO8p6WEfjKpFKRdv3Co30yuXKAt_bQ94JQdG6_6wG7Tji5BBFo1-MPSI-SjwBxJDIfZPM6rvk0qOrR2P25Mg-bb7eLrbw8U8r7HwONU1w4K-QQEB0tBPv-v-jICWnoxWCB3LRT_PFCyZsKwpc_717tP5MMVJDcVej14MZhsttMHdhT6t0LDK1SFf3jm73dHcD6JeQviSvB1nzqzYoGs6XNhwto8BnXb9HWAIGBQNlauhxe8AlqNuQoA2IicrtYUfk-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین، انتخاب تو را به یاد می‌سپارد
🔹
هر بار که کیسه پارچه‌ای را انتخاب می‌کنیم، یک قدم به زمین سالم‌تر نزدیک می‌شویم  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/652309" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219c992f35.mp4?token=PbiqegGsTvwx7KwA-NtDlVMW9ArWot_U3KfhC2a262CNdfA4VK_MBz9nMjef3M-Bx7yq1hnoBHNLanwZANpXHBbCe1VYz161VwG9EAC9mz6YH2hYb_HHTE02xje995BqKjvEmbNj_dTCvnskWWwKbyyTh0Q9hjR4tFOxt7qmtJlW4H08D2dxMbqr4JrEzrHT6M9W16sX32lMp8S7mVyXNeF_crh0PYBxXQlh-yNR8AdvY_7EaibbcJTH4oxyW3T-MAJpIhTw4qoJ59Vwupe3I-rfDhfdNSnjjBHNKsly5EHN47DUKroWDe_77mWNppQTQKfoNVjvFvxqHX0gjN0Kho1cLfUWnKQ0HNiY590RgVt08RHkuEmw6f-GrZmBmoJ0nvOXPPswFNJaXKebX2CiWH8dQN-LLxnbbWi9kKjndqLW-ca31tAZZeW7R0n43prIE-IZiZrtUjoZembDDGLY49FC26Zwf0HnBiyD_PpFyLQYfLIpDZIkkNAPohPugD4dDchxFRnkbCD1tpDXPfCBROOpCthlJesxjAboP-eiF1IjRLd3mqGGZK9GSLmncoqTaYd4HYghmG-OTGd9cB4KFQUJ6y9EUVWM8CKdA-m7HSfIEoj7CqnfIba02y3XD2T7igihkr-5Bt9jSfSlaVPnP1PU6CrjFSaxPsKK_PLFu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219c992f35.mp4?token=PbiqegGsTvwx7KwA-NtDlVMW9ArWot_U3KfhC2a262CNdfA4VK_MBz9nMjef3M-Bx7yq1hnoBHNLanwZANpXHBbCe1VYz161VwG9EAC9mz6YH2hYb_HHTE02xje995BqKjvEmbNj_dTCvnskWWwKbyyTh0Q9hjR4tFOxt7qmtJlW4H08D2dxMbqr4JrEzrHT6M9W16sX32lMp8S7mVyXNeF_crh0PYBxXQlh-yNR8AdvY_7EaibbcJTH4oxyW3T-MAJpIhTw4qoJ59Vwupe3I-rfDhfdNSnjjBHNKsly5EHN47DUKroWDe_77mWNppQTQKfoNVjvFvxqHX0gjN0Kho1cLfUWnKQ0HNiY590RgVt08RHkuEmw6f-GrZmBmoJ0nvOXPPswFNJaXKebX2CiWH8dQN-LLxnbbWi9kKjndqLW-ca31tAZZeW7R0n43prIE-IZiZrtUjoZembDDGLY49FC26Zwf0HnBiyD_PpFyLQYfLIpDZIkkNAPohPugD4dDchxFRnkbCD1tpDXPfCBROOpCthlJesxjAboP-eiF1IjRLd3mqGGZK9GSLmncoqTaYd4HYghmG-OTGd9cB4KFQUJ6y9EUVWM8CKdA-m7HSfIEoj7CqnfIba02y3XD2T7igihkr-5Bt9jSfSlaVPnP1PU6CrjFSaxPsKK_PLFu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شی‌جین‌پینگ؛ مردی که جهان از او می‌ترسد!
🔹
تعریف و تمجیدهای ترامپ از رئیس‌جمهور چین در جریان سفر به پکن، توجهات به او را بیشتر از همیشه کرده است. شی‌جین‌پینگ کیست و چرا حتی ترامپ هم از او می ترسد؟
🔹
این ویدئو ناگفته‌های جذابی از او دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/652308" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPb1H5IQ8PkTbXFlpcOyNwmdprUXMGbFPXRQ6QmSH3wTebcZiWZIqs99rnPO9Ahv9l-ncdxVL2bI0Ex2U9RadP5sfZGkXGMPv7lnrUNmUndzxWgX82pptWTzlUZpXWtxE0S_x71ydvE5kK5-M7cwea4sbew0k4u9hjEJYM5XbqkqDguKAW8ToQLTzvA8juZ-4mqMqXHptpp-6YDzMRUM7oDXf9zt92cMshmun_CWeVmKXMfe8JshE3f9_zn0_GCR5Q5sdEp3MZ25gf3qmobT8Tvb2x20AJqT33_WAQ10knwRd0__4kDLxJZQM0pf3QBZvSM9BnP6A6svdqLpiZFzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد صنعت هسته‌ای ایران پس از خروج آمریکا از برجام
🔹
رابرت مالی نماینده سابق آمریکا در امور ایران: تصمیم ترامپ در سال ۲۰۱۸ برای خروج از برجام و اعمال تحریم‌های فشار حداکثری، باعث رشد چشمگیر تخصص و دانش هسته‌ای ایران شد.
🔹
این تصمیم کاملاً یک ضربه هسته‌ای به آمریکا بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/652307" target="_blank">📅 20:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ak310g_qpHuLLtdzea8RxMqtlxzqIYcj7MXEuyPXvkl6UzxaMyf9CEuScBueG5gfbAa_W1kxNAK2HVeS4cBJbE__8IU9oLfUiZscvU-PdRMOg1PJeKFGN7p6NSK_0_x2IgBgZemQKYpNRmAqF-K-Gb9MYmZk64MK2CL06E4on7AtXrEU3MIWF0UyrCwWOODIRzwtGqP4FFwtWSPIMPAKNPMuldalaW9pFBIuKsYvbMp9t4KUPJwyZKsXlu4RieNq2DxRuVbJpSJUbf7F3qB1hYpJLFh8G9buZTBkvE--Otr0Ma6HMoBzg1-PgUYqQggyjXGmZ8vr3IZDo6beEQSuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امضای بزرگ‌ترین توافق تبادل اسرا در یمن با میانجیگری اردن
🔹
منابع یمنی از دستیابی به بزرگ‌ترین توافق تبادل اسرا و بازداشت‌شدگان میان دولت جنبش انصارالله و دولت مستعفی یمن خبر دادند؛ توافقی که شامل آزادی مجموعاً ۱۷۲۸ نفر از دو طرف می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/652306" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652305">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6ab2a709.mp4?token=QBBHy3kLPzVgZzWByatOimYFr_UVEZIi8N0HgHVPTxkbwJJC2oZMTf5PWtSWysfDoRJ4RJVHQnmMYA4IiItnT9RrBimpY3D94wAJq3gu9s_-UNhgHIQcPMkKb3ylNsfGBpETU1RmjjqN-Fim7J-hOOwF54cQWdQXIAXfdTJCtzYA6JxpUtZufGoHMhRX7D7PijInlc9z6pmR_WBJXQUq4OT5aqxPDjeoLWAjBf7h7NA4LCkNGapph-8DURO8eDxLCJ3tDug-RXIgVgW-6Tq96EezVPsbDCQ7Zxymu0ZAjaoZm28vP3JJuB7fM3XLGKMviGw3w7aouxaU55CAV65I5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6ab2a709.mp4?token=QBBHy3kLPzVgZzWByatOimYFr_UVEZIi8N0HgHVPTxkbwJJC2oZMTf5PWtSWysfDoRJ4RJVHQnmMYA4IiItnT9RrBimpY3D94wAJq3gu9s_-UNhgHIQcPMkKb3ylNsfGBpETU1RmjjqN-Fim7J-hOOwF54cQWdQXIAXfdTJCtzYA6JxpUtZufGoHMhRX7D7PijInlc9z6pmR_WBJXQUq4OT5aqxPDjeoLWAjBf7h7NA4LCkNGapph-8DURO8eDxLCJ3tDug-RXIgVgW-6Tq96EezVPsbDCQ7Zxymu0ZAjaoZm28vP3JJuB7fM3XLGKMviGw3w7aouxaU55CAV65I5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده ولی‌فقیه در سپاه: رزمندگان سپاه هم دستشان پر است، هم ذهن‌شان آماده
🔹
حجت‌الاسلام حاجی صادقی پس از بازدید میدانی از نقطه صفر مرزی در شهرستان بانه: دشمن توان ایستادن مقابل ایران را ندارد
🔹
رزمندگان سپاه اسلام از آمادگی خوبی برای مقابله با هرگونه تهدید دشمن برخوردارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/akhbarefori/652305" target="_blank">📅 19:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652304">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
اوباما درباره برجام: بدون شلیک یک گلوله برنامه هسته‌ای ایران را متوقف کردیم
🔹
رئیس‌جمهور اسبق آمریکا: ما بدون شلیک یک گلوله آن را متوقف کردیم. ۹۷ درصد اورانیوم آنها را خارج کردیم.
🔹
هیچ بحثی وجود ندارد که آن توافق را کار کرد و لازم نبود ما عده زیادی آدم بکشیم یا تنگه هرمز را ببندیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/652304" target="_blank">📅 19:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652303">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owh6SGB-OXLoTQSNQD_9fuf2WnM2fMVsw3_xtBTAqDMemS3aXcmeAYdLuu2w85aMGV3FcpgR6mzgaguEo75BMLhlksGrL8XsaWNOTBPNGI-Br-B-YeSjlVmg_vo-uhAfBCpmEBmj9e8gcjQdaI1wTGNA5tPcGRFxuYng-caXh9kqmOT2Mbx0aeTlFgZlqJ8QSrmQkL1ngxFoGzRHRYdlFNMYHuNEx-KWpIfhcQyUvJjCm0_dLbqhVhnxCoRZCYtRglv17SLcI7uQtuVc1Rc2hqKCQNplD_4G89IZz9bwyNy1YxS571Ng9MfZ9hEkJEj5dEjNoPKpFuhj59Hg93VU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمود عباس: با خطرات وجودی مواجه هستیم
🔹
رئیس تشکیلات خودگردان فلسطین: ملت فلسطین با خطرات وجودی، جنگ، نسل‌کُشی و تحمیل گرسنگی مواجه است.
🔹
تداوم بلوکه کردن دارایی‌های ملت فلسطین و محاصره اقتصاد ملی دزدی مالی است. اسرائیل بیش از ۵ میلیارد دلار اموال ملت فلسطین را بلوکه کرده است، بیش از ۲۵۰۰ خانواده فلسطینی به دست رژیم اشغالگر از ثبت احوال حذف شده‌اند و ۲۷۲ هزار نفر در اراضی فلسطینی شهید و زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/akhbarefori/652303" target="_blank">📅 19:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652302">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برنامه‌های پیشنهادی برای حل مشکل بنزین
اسماعیل حسینی، سخنگوی کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
دولت باید به‌ جای افزایش قیمت، سیاست‌های غیرقیمتی مثل توسعه CNG و LPG، انتقال سهمیه به کارت بانکی، واردات خودروهای برقی و تخصیص سهمیه به کد ملی را اجرا کند تا شفافیت بیشتر و قاچاق کمتر شود.
🔹
روزانه ۱۲۴ میلیون لیتر بنزین مصرف می‌شود. با مدیریت مصرف، نیازی به واردات نیست. حدود ۵۰ درصد خانوارهای ایرانی، خودرو ندارند و تخصیص سهمیه به کدملی، یارانه سوخت را عادلانه‌تر می‌کند
@TV_Fori</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/652302" target="_blank">📅 19:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652301">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyLu7sQpiIq5PVBIQ4IyT5ZLU5QpxPum1ohIRTrSpDGAzxRG9zdDC0sHI8PwJFjvEHLgek9W1nhdfUmgtJGvauq-X-_NfchFk7KrE3NQ-J0OiK6w0ytC3NMtI3sjBHtKsATYHOvvwrlhiW8JuTHxdZbBO4jWRAUnD7ifXcyVhgsOc7CpsrTFzUzJD1dmLLNN1xsnRzaTLWzc3h2p6CQxjIkTyNSbOUkIhnQHR9OsXkQj5n2ngZHHZD5NqphM8Hd1UnEVqGuwJq4M8B5VqkxpicEEhdxLvezIfRyS8m-bCjGQo11UNzzWRWcoHlyaem_EI7PxAlVZqCY7FLi-hdBSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سجاد عابدی فعال رسانه: کانفیگ ها تلفن همراه مردم را ابزار جاسوسی دستگاه امنیتی خارجی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/652301" target="_blank">📅 19:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652300">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca819d09a.mp4?token=clTkAbGA2xaeSY2w4ygsO6OQmoPgTRITbOV_YhV6IsU8FmFLPAdWBxL27eLPZ6g74dl5KanZJ3lRtZxD-7sTluiTSMIjVvFvxlC2_3Cq4biZpv2N4-Mjgbj8bL-vqV8x3n0Dqd1OJ5h9qYWus8YS1dl4-C430DTWwYxJQwOHYYx1yVMX5jroP7BnK1vLno4V__oUaw1k9TfNawnswVlArvErQ-CvFURstIZAHM7MD8hZ8csgbSgNmzk52jjxeXphPUYYVHbsEPBcZ_o4xBrbkGPRC8yqZxVtW4pkU48uBiDGXXxBCE74N4nZCwRXylPMnPtSLGUWHP2PBfGi147GvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca819d09a.mp4?token=clTkAbGA2xaeSY2w4ygsO6OQmoPgTRITbOV_YhV6IsU8FmFLPAdWBxL27eLPZ6g74dl5KanZJ3lRtZxD-7sTluiTSMIjVvFvxlC2_3Cq4biZpv2N4-Mjgbj8bL-vqV8x3n0Dqd1OJ5h9qYWus8YS1dl4-C430DTWwYxJQwOHYYx1yVMX5jroP7BnK1vLno4V__oUaw1k9TfNawnswVlArvErQ-CvFURstIZAHM7MD8hZ8csgbSgNmzk52jjxeXphPUYYVHbsEPBcZ_o4xBrbkGPRC8yqZxVtW4pkU48uBiDGXXxBCE74N4nZCwRXylPMnPtSLGUWHP2PBfGi147GvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده سنتکام: ۶ کشور عربی در جنگ با ایران کنار ما هستند
🔹
۵ کشور خاص هستند که به معنای واقعی کلمه در کنار آمریکا درحال دفاع هستند: امارات، بحرین، کویت، قطر و عربستان.
🔹
هر آنچه انجام دادیم بدون اردن و همکاری نزدیک با اسرائیل غیرممکن بود. آن‌ها فقط مأموریت اجرا نکردند، بلکه در کنار آمریکایی‌ها خدمت کردند و از آمریکایی‌ها محافظت کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/akhbarefori/652300" target="_blank">📅 19:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652299">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای جنجالی؛ ثبت‌نام ماشین الکی است!
کرمی، رئیس اتحادیه خودرو در
#گفتگو
با خبرفوری:
🔹
ثبت‌نام ماشین از طریق سایت معمولا الکی و بیخودی است و هیچ اثری در بازار نداشته. حتی یک ثبت‌نام هم نشده، سایت را الکی باز می‌کنند و می‌گویند ثبت‌نام کنید و مردم را سرکار می‌گذارند.
🔹
مردم هم آن‌ها را شناختند و می‌دانند به تعهداتشان را انجام نمی‌دهند. معمولا کسی هم ثبت‌نام نمی‌کند مگر پول اضافه‌ای داشته باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/652299" target="_blank">📅 19:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652298">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33a946c25.mp4?token=irf8RfMLP1NP6tRfdFJ-0FULTEgkg3YzHxUpFPJZ9805xwDWidql4sOszJvCFnnSzr-vTQ9b1fM2vsXuLdnU1xcAxDLCdxoEhrVZ6hoggdRrm1770o2W7weMOX4mF78jwi0ANJD1itLOt37OdBuP4DtyDuTYu5W4NkjeIerZoPeBy0rcbTfmxpxVkXM9i_oV8vkI0lif0WX0AjW-3GlNAJbWGG-ory6r5P-HQfKAen_n36KfHbFX-b9-bAJni7BVcpvnrBxZ3kl5ctSy92W11fCwP_t2bmFOJzPOUNj5rRPtAv2sFrt9JtQfqQ3qT31AAEmDAv9zllTX1sK51tJYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33a946c25.mp4?token=irf8RfMLP1NP6tRfdFJ-0FULTEgkg3YzHxUpFPJZ9805xwDWidql4sOszJvCFnnSzr-vTQ9b1fM2vsXuLdnU1xcAxDLCdxoEhrVZ6hoggdRrm1770o2W7weMOX4mF78jwi0ANJD1itLOt37OdBuP4DtyDuTYu5W4NkjeIerZoPeBy0rcbTfmxpxVkXM9i_oV8vkI0lif0WX0AjW-3GlNAJbWGG-ory6r5P-HQfKAen_n36KfHbFX-b9-bAJni7BVcpvnrBxZ3kl5ctSy92W11fCwP_t2bmFOJzPOUNj5rRPtAv2sFrt9JtQfqQ3qT31AAEmDAv9zllTX1sK51tJYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر گردشگری: رژیم صهیونیستی از جامعه کلیمیان ایران انتقام گرفت
🔹
رضا صالحی امیری، وزیر میراث فرهنگی، گردشگری و صنایع دستی در حاشیه بازدید از کنیسه رفیع‌نیا تهران که به خاطر حملات رژیم صهیونیستی تخریب شده است گفت:
🔹
میناب پس از هیروشیما و ویتنام سومین جنایت بزرگ آمریکاست اما ما هیچ وقت در این باور نبودیم که رژیم صهیونیستی از جامعه نجیب کلیمیان ایران هم انتقام بگیرد
🔹
این بنا امروز دیگر یک سازه عادی نیست بلکه نمادی از جنایت رژیم صهیونیستی است در حق کلیمیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/652298" target="_blank">📅 19:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652297">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce82230059.mp4?token=ull1V1Yq0XcQ6wu6PDg91cZLWS01f4pu1ig53WC8yLmdKFAf0AsD-FCWD5MGoqMMauXuU2tpIT90odpZZ4h7_SAaK2-cBHK_D0TjFbr60wOSJkmuq5-4koW4yL8zwv3R1H-x8iiJkR-7wpsQQXckF87uNbLg7N-b79x4w-qbYG4iB3lsHhO-sMTPSCu5L6EnQoOi649xiJqBLw1GYzbUkp2cB6BeemwFdayAwAkeCpGZwLMC0CJzBbuLQrioDHgYAuZbD6oFLricRQAV2Px7hhENjWhlFCpL1VTsSTswNhBBWi1Td9Af-hb40PokRlNmDS8-vDV2d3KRYK6yYwMmNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce82230059.mp4?token=ull1V1Yq0XcQ6wu6PDg91cZLWS01f4pu1ig53WC8yLmdKFAf0AsD-FCWD5MGoqMMauXuU2tpIT90odpZZ4h7_SAaK2-cBHK_D0TjFbr60wOSJkmuq5-4koW4yL8zwv3R1H-x8iiJkR-7wpsQQXckF87uNbLg7N-b79x4w-qbYG4iB3lsHhO-sMTPSCu5L6EnQoOi649xiJqBLw1GYzbUkp2cB6BeemwFdayAwAkeCpGZwLMC0CJzBbuLQrioDHgYAuZbD6oFLricRQAV2Px7hhENjWhlFCpL1VTsSTswNhBBWi1Td9Af-hb40PokRlNmDS8-vDV2d3KRYK6yYwMmNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاهش قیمت خودروهای خارجی
🔹
جذاب‌ترین عدد امروز مربوط به خبر کاهش ۱۰ تا ۱۵ درصدی قیمت خودروهای خارجیست.
خبرسازترین عددهای روز را ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/akhbarefori/652297" target="_blank">📅 18:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652296">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
علی باقری، معاون دبیر شورای عالی امنیت ملی: زمانی که مردم و کشور ما با تجاوز آمریکا و رژیم صهیونیستی روبرو هستند، موضع قاطع دوستان ما – کشور همسایه روسیه - چه در سطح دوجانبه و چه در سطح بین‌المللی، شایسته تقدیر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/akhbarefori/652296" target="_blank">📅 18:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652295">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
روایت تلخ یک تولیدکننده از خسارت جنگ؛
🔹
«همه زندگی‌ام را می‌فروشم تا کارخانه بماند!»
🔹
یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان با بیان اینکه ۹۰ درصد واحد تولیدی‌اش در جریان جنگ آسیب دیده، گفت: «تمام زندگی‌ام را برای حفظ کارخانه و کارگرانم می‌فروشم.»
🔹
وی با اشاره به خسارت ۷۰ تا ۸۰ میلیارد تومانی، از ناکافی بودن تسهیلات پیشنهادی، سختگیری بانک‌ها و ادامه فشار دستگاه‌های خدمات‌رسان گلایه کرد و افزود: با وجود توقف فعالیت کارخانه، هیچ نیرویی تعدیل نشده و حقوق و بیمه کارکنان همچنان پرداخت می‌شود، اما حمایت‌های عملی متناسب با حجم خسارت‌ها وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/652295" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652294">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e397d0e5.mp4?token=SRK0sDhnz8jLIOhHmvvuDYyqkjo-6VqyuekH59hqQaD-khMpE59_wuQOinYXomccBezU67FudSV3fQrWTs-aKWdwkoY8rLfNanhH0lBxwIrWN6MnfXo1dAwEBa6zsxdqoupYrRt5n7mRTHBL-fStq9v3ul57HqOelVHurs7gf9DqZVYwMtvh9NgPUlDIS2cfCMPNYidJcKY0wuNlzEXAU5rENIWmmiFf13n5G5c92GQUMY_NBCgLaMY0U8KDMlGqb5IK7Acm3c0IGq2eB7F7bQeA4zmh_YxBwJe4ECQFBrgdl77cK-keCqiGcKnDJsB0lj6XBNFOws5safHoxijLxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e397d0e5.mp4?token=SRK0sDhnz8jLIOhHmvvuDYyqkjo-6VqyuekH59hqQaD-khMpE59_wuQOinYXomccBezU67FudSV3fQrWTs-aKWdwkoY8rLfNanhH0lBxwIrWN6MnfXo1dAwEBa6zsxdqoupYrRt5n7mRTHBL-fStq9v3ul57HqOelVHurs7gf9DqZVYwMtvh9NgPUlDIS2cfCMPNYidJcKY0wuNlzEXAU5rENIWmmiFf13n5G5c92GQUMY_NBCgLaMY0U8KDMlGqb5IK7Acm3c0IGq2eB7F7bQeA4zmh_YxBwJe4ECQFBrgdl77cK-keCqiGcKnDJsB0lj6XBNFOws5safHoxijLxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: آیا درباره حمایت چین از ایران با شی گفتگو کردید؟
🔹
ترامپ: او گفت که تجهیزات نظامی نخواهد داد. این اظهارنظر مهمی است.
🔹
اما در عین حال، او گفت که آنها مقدار زیادی نفت از آنجا می‌خرند و مایلند این کار را ادامه دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/652294" target="_blank">📅 18:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652293">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea360c9ff.mp4?token=BHEQfSH2jpJ9C8tVHzWLutenEpMZ6C6fasOz8nWXhDAdW7BnzVO-03BUGvL4uF4Dj5bm0gbDSx8DUfvcKMJoj7LDsI_UbO6FnsGBGqW3U883tTaLr29ZacdvzZUBsYITZR51-kVsFBp7rGViK_TW6M3AzMl9S7JUGIXJPs9tY7MAEOZWWv0Kr7ddAiCFiyqzFz-_wnPNl-QNGW4zW5V7Ejo_fmQxzreCS_G5Hk8jlCwZOVhPFf8eG68tPBjXhsdnCcZlajt2Lwram-G_uoNdC44KHD8syGerszURAwfsXLq2mdrG2X8HGezwzWqHO2kugVVnacRXwb88Uyt_bCyGJ08NlIqHyNM5_3K4G7hhzTLjPCNSrRScIsAEpmTXKnFgMKr-GcfrWi7naD9n_6xXKq-8gxj6Ygst9FA1n8mlBKnX4UaTTl957yc5HnSVsdu9jZswchtkgZ_POy3wrwRI-3nztq6tUDhPi4R9-3NjU0-J1wxmCMEMblKgzBucDDHSoUaA6DgbkWYtbld4sYVXNkmC7yNEJsXY25F1-ZCv5bvwovSpSlKLdrWUmN7Sdoky8l3tq94myLlo_73NR5Llp06B5dFvSSM75v8b2swEtcrdHhKACwVBXhyuJ6O6nILFLJfSHQ4P3P3_coUMgp0joTLJtC6bsptHEUZH2Do5w44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea360c9ff.mp4?token=BHEQfSH2jpJ9C8tVHzWLutenEpMZ6C6fasOz8nWXhDAdW7BnzVO-03BUGvL4uF4Dj5bm0gbDSx8DUfvcKMJoj7LDsI_UbO6FnsGBGqW3U883tTaLr29ZacdvzZUBsYITZR51-kVsFBp7rGViK_TW6M3AzMl9S7JUGIXJPs9tY7MAEOZWWv0Kr7ddAiCFiyqzFz-_wnPNl-QNGW4zW5V7Ejo_fmQxzreCS_G5Hk8jlCwZOVhPFf8eG68tPBjXhsdnCcZlajt2Lwram-G_uoNdC44KHD8syGerszURAwfsXLq2mdrG2X8HGezwzWqHO2kugVVnacRXwb88Uyt_bCyGJ08NlIqHyNM5_3K4G7hhzTLjPCNSrRScIsAEpmTXKnFgMKr-GcfrWi7naD9n_6xXKq-8gxj6Ygst9FA1n8mlBKnX4UaTTl957yc5HnSVsdu9jZswchtkgZ_POy3wrwRI-3nztq6tUDhPi4R9-3NjU0-J1wxmCMEMblKgzBucDDHSoUaA6DgbkWYtbld4sYVXNkmC7yNEJsXY25F1-ZCv5bvwovSpSlKLdrWUmN7Sdoky8l3tq94myLlo_73NR5Llp06B5dFvSSM75v8b2swEtcrdHhKACwVBXhyuJ6O6nILFLJfSHQ4P3P3_coUMgp0joTLJtC6bsptHEUZH2Do5w44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ظهوریان: بخش انرژی کشور ۱۴ میلیارد دلار خسارت دیده است
🔹
۸ میلیارد دلار بخش گاز آسیب دیده است؛
🔹
ظرفیت تولید گاز کاهش پیدا کرده
🔹
پخش پتروشیمی ۶ میلیارد دلار آسیب دیده است؛
🔹
بخش فولاد ۲.۷ میلیارد دلار آسیب دیده است؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/akhbarefori/652293" target="_blank">📅 18:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652292">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
مقام نظامی آمریکا: سنتکام برای مقابله با تهدید ایران تشکیل شده است
🔹
رئیس فرماندهی مرکزی ایالات متحده آمریکا (سنتکام) براد کوپر امروز پنجشنبه گفت که هدف از تشکیل این سازمان در سال ۱۹۸۳ مقابله با «تهدید ایران» بوده است.
🔹
کوپر در جلسه کمیته نیروهای مسلح سنا با بیان این ادعا که تشکیل سنتکام پاسخی مستقیم به تهدیدهای ناشی از ایران بوده گفته که مسئولیت او در کسوت شانزدهمین فرمانده این سازمان  در وهله اول رسیدگی به «مسئله ایران» است.
🔹
سنتکام یکی از یازده واحد فرماندهی وزارت جنگ آمریکا است که در سال ۱۹۸۳ تشکیل شد. این سازمان مسئولیت هدایت نیروهای آمریکایی در منطقه غرب آسیا و شمال آفریقا، آسیای مرکزی و بخش‌هایی از جنوب آسیا را بر عهده دارد.
🔹
شورای عالی امنیت ملی ایران فروردین‌ماه سال ۱۳۹۸ سنتکام و تمامی نیروهای وابسته به آن را تروریستی اعلام کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/652292" target="_blank">📅 18:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652291">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqh5s3BzNcv7zOS3MGh0xI3dFK7aew4xbvGzjxebTfb8fkhglez1xLOmI9933Zohg_6orTKaCi8qgjD69pznFIuWi9l8jOw4gXlMr3hJLYdYabubYwy2Ki6iFUNzRj4wtSpt6k7D72pYNMDB6amxpNDl7khxf2qGNLKW24w8eZyx68mla4yArBhTbSziqre557t5Na62AlXX9QnjQfsO4g4lmQgx-0hF9vDVBT24Iwqqs3UzcWPEkhZpts4eQpYPEU8ujlX9lEW7JP-Buk9flepOwGufqVIo-hDAIaH-U0bb_LCM3wu2SNfaqM5b_Bubai3MfbZcYemNAGBFkblSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلاح جدید ایران؛ ترامپ زیر حمله رفت!
🔹
در ادامه جنگ رسانه‌ای ایران و آمریکا، ویدیوهایی با شخصیت‌های لگویی و موسیقی رپ و ترپ برای تمسخر دونالد ترامپ منتشر شده است.
🔹
به گفته منتقدان، این کلیپ‌ها نوعی «تبلیغات در قالب سرگرمی» هستند که با استفاده از فرهنگ هیپ‌هاپ و رپ ـ به‌ عنوان زبان جهانی اعتراض ـ پیام‌های سیاسی و ضدآمریکایی را منتقل می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/652291" target="_blank">📅 18:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652290">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU6xFL_YP2-HRw6UqBTxvl7AA3LA3SO5S2cpqBQBpapIjuqBMN7q7yKLawfR5PaJ52-4URaimOQdgJ_swk4aTEkDb1LOMVnOvp9ol-4AyVVZgxq5KgI-4qn49vSW3Tc4RSBxwcHi06-mc4aLkScjoB5GfaHmnXn4gjMy-yKZCWx-ESih7-J8mr-7TFtipjNDhUXo9NNAhjcVLA_w7rH-617IUsU5tPuZIch-grr-MHa4XycYMu58vEORv1t_vUnNxsRlR31n7UkPSUmleOxyW3l6tQbbTB1hPEh-BF15VjTpp6RrJD9x594n-enqAa7K9YYDpYEq5LA_GLF8zs9MAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان تعویض قطعات خودرو
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/akhbarefori/652290" target="_blank">📅 18:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652289">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آمریکا تحقق اهدافش در ایران را به ۴۰ روز دیگر حواله داد
🔹
رئیس فرماندهی مرکزی ایالات متحده آمریکا، سنتکام در یک جلسه در مجلس سنا تحقق اهداف جنگی این کشور در ایران را به ۴۰ روز دیگر حواله داده است.
🔹
این مقام نظامی آمریکا در جلسه استماع سنا گفت که ارتش آمریکا می‌تواند ظرف کمتر از ۴۰ روز اهدافش در ایران را محقق کند.
🔹
ادعای فرمانده سنتکام در حالی مطرح شده که رئیس‌جمهور آمریکا دونالد ترامپ هنگام آغاز جنگ در ایران گفته بود که این عملیات بین ۴ تا ۶ هفته به طول خواهد انجامید.
🔹
شماری از نماینده‌های کنگره بعد از اتمام ضرب‌الاجل ۶۰ روزه در نامه‌ای به دونالد ترامپ تصریح کرده بودند که هیچ‌یک از سه هدف تعیین‌شده برای جنگ علیه ایران محقق نشده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/652289" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652288">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMtstFWo0GdJvQ37vMPfEh4lw05Pp3wU9dkwqtq8FpNbd2Pxaq7pQpEILAzdsJnTNbYakPxQkAaeIzK5iKKXPzmgjjLoM2Bda8cjwf_rPfCOGZ_bObSTReJgFiQKfhIBULn5W9aWiGrt5e-BSw9qytKFCl7gZcctMY6_2HFhufkRkv4exj2CvLW1alW15pDZzmLZPLLQoKOeyXYerdKUvOj8DtFo0CRI8uAa5DjoIlu5m7u1kLPvy4nzDffKyMhyXc9UJhquqTfK2p9mjTVwyXM9V2IRaCdgKawFw4uNmoh8NGgW2pETnW29I_6unNjUTWcoxf7_Vq1U4ODRdAyCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۴ سال تغییر در نظم تجارت جهانی؛ از افول هژمونی آمریکا تا پیشتازی چین
داده‌های رسمی نشان می‌دهد که نقشه صادرات جهانی بین سال‌های ۱۹۹۰ تا ۲۰۲۴ دستخوش تغییراتی بنیادین شده است:
🔹
۱۹۹۰: آمریکا صادرکننده اصلی به ۱۷۵ کشور (۹۰٪ جهان) – چین فقط ۸ کشور
🔹
۲۰۰۰: آغاز افول نسبی آمریکا (۱۵۵ کشور) – رشد آرام چین (۱۵ کشور)
🔹
۲۰۱۰: نقطه عطف – آمریکا صادرکننده اصلی به ۸۵ کشور و چین صادرکننده اصلی به ۵۵ کشور
🔹
۲۰۲۴: معکوس شدن کامل وضعیت صادراتی دنیا – چین با  ۱۲۵ کشور پیشتاز است در حالی که آمریکا به ۳۵ کشور تنزل یافته است
🔹
نکته کلیدی: این آمار بی‌تردید بیانگر کاهش شدید نفوذ تجاری آمریکا و افزایش چشمگیر تسلط چین بر بازارهای صادراتی جهان در سه دهه اخیر است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/652288" target="_blank">📅 17:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652287">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
منابع خبری می‌گویند کشتی باری هندی که روز گذشته به مقصد شارجه در حرکت بوده در تنگه هرمز هدف قرار گرفته و غرق شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/652287" target="_blank">📅 17:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652286">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
معاون وزیر صمت: بسته حمایتی برای واحدهای تولیدی آسیب‌دیده از جنگ شامل تمدید مهلت بازپرداخت بدهی‌ها و معافیت گمرکی ماشین‌آلات است
🔹
بر اساس این طرح، واحدهای خسارت‌دیده ۲ تا ۶ ماه تنفس در پرداخت‌ها و اقساط دریافت می‌کنند و دوره بازپرداخت از ۲۴ به ۴۸ ماه افزایش می‌یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/652286" target="_blank">📅 17:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652285">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs7tte5hhtU3YRosjjRF5vNL-InCxs81lql95Nf5GD5NdCes3JY47zVLgb8Brv6fbCitHh9SnqHmuALyjHCGHXOXHZNYQRVGaaQqDojz-cuiCt_r3BGCs7TrbDT2HzsG5wsSoBkjCZ5a14o4tq7tVUYLSfuZKVJu7QAXvrvUQUIrRLEpHQr9k8saiUz9TDlwcEtCJimLkUxia27TLyytJEI53-WjqvnzPbm91JarS_Ux7oet-RIHNvIIlFgG6Fmt6COcGNgM2_o0ShtUclIponh8oz9hqmLc-VBfumr0XGHPpn9zup5AfT1z2DDXX_0VwC9zH_n9HM0KQsh7c9w5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: در جنگ ایران و آمریکا چین برنده شد!
واشنگتن‌پست:
🔹
چین از جنگ ایران و آمریکا برای تقویت جایگاه ژئوپلیتیک خود استفاده کرده و برتری‌اش را در حوزه‌های نظامی، اقتصادی، دیپلماتیک و اطلاعاتی افزایش داده است.
🔹
طبق این ارزیابی، پکن پس از آغاز عملیات آمریکا و اسرائیل علیه ایران، نفوذ خود را گسترش داده و در بحران ناشی از بسته شدن تنگه هرمز، با کمک به کشورهای دچار کمبود انرژی، خود را به‌عنوان بخشی از راه‌حل معرفی کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/652285" target="_blank">📅 17:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652284">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ee701724.mp4?token=FBkY8WRYdQdCzng_U8D8oqZdlg7aEvkqrlB_bUgY7SVb7iHjfDXaps6jllxNxApctLw2_flzN77fG3yFL0eOqMvOtzQceKuq-xEsK55grSpr3fuzkjNHY7pRG829nOhjJw1B26IzAX52LfS4fmtOfEE8Rla07p12rKZ_of1LHZGoZyhDL-o4bJ2DP4O9-9K8n_-iGjUHXUh4Egm2FT1sJSwYsQRMpb84A2JLpLAk2agwgUBZJFd7AV2wwcT1g3xAZgiQhiYB6v7xV6w31g9eezdJhxopPEiPrhQfajueOxBAjrKvvkILMPLLvJMNdyrIZdI6-VpNSI6klYnXTH4oBCoWBE1vnVBwaAhLWf2oI-cKR8j3D_J1GeOdBa6ttPGblaD5yyqdamQpdd5cOWOczXAiJgXjMChgoexF711MPM-cH3IyXGAnZ4_4QUVA-NfuUjSfuY6etAbgn_gLxmbT-TFOKwvkiKopikoGFjm0vcchN7ntFpNNhqIshGdgCxeu1QUvvVFQc3iJq_uSDXBJLie4EMXBEel-rdJSdgwnWHQvfo5BrmWXFCa4rqjsVVz0p0l5hxoM8-I46gI7A_dMRFa4bO0Vj2k3T277Z9BIGq10teqlHqPJ1O04VuGGskLwTmWM-rM2CJgh_GlcH2pahmp_bjU7VAl9FVnDmJocjTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ee701724.mp4?token=FBkY8WRYdQdCzng_U8D8oqZdlg7aEvkqrlB_bUgY7SVb7iHjfDXaps6jllxNxApctLw2_flzN77fG3yFL0eOqMvOtzQceKuq-xEsK55grSpr3fuzkjNHY7pRG829nOhjJw1B26IzAX52LfS4fmtOfEE8Rla07p12rKZ_of1LHZGoZyhDL-o4bJ2DP4O9-9K8n_-iGjUHXUh4Egm2FT1sJSwYsQRMpb84A2JLpLAk2agwgUBZJFd7AV2wwcT1g3xAZgiQhiYB6v7xV6w31g9eezdJhxopPEiPrhQfajueOxBAjrKvvkILMPLLvJMNdyrIZdI6-VpNSI6klYnXTH4oBCoWBE1vnVBwaAhLWf2oI-cKR8j3D_J1GeOdBa6ttPGblaD5yyqdamQpdd5cOWOczXAiJgXjMChgoexF711MPM-cH3IyXGAnZ4_4QUVA-NfuUjSfuY6etAbgn_gLxmbT-TFOKwvkiKopikoGFjm0vcchN7ntFpNNhqIshGdgCxeu1QUvvVFQc3iJq_uSDXBJLie4EMXBEel-rdJSdgwnWHQvfo5BrmWXFCa4rqjsVVz0p0l5hxoM8-I46gI7A_dMRFa4bO0Vj2k3T277Z9BIGq10teqlHqPJ1O04VuGGskLwTmWM-rM2CJgh_GlcH2pahmp_bjU7VAl9FVnDmJocjTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ضرب‌ شست رئیس‌جمهور چین به آمریکا
🔹
چین مراسم استقبال عجیبی از ترامپ داشت؛ حضور همزمان کودکان کنار یگان نظامی تشریفات!
🔹
چرا پکن به این جمع‌بندی رسید که چنین استقبالی از ترامپ انجام شود؟
🔹
این کار چه پیامی برای آمریکا داشت؟
🔹
این ویدئو پشت‌پرده این تصمیم چین را افشا می‌کند؛ آمریکا هنوز حیرت‌زده این تصمیم است.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/akhbarefori/652284" target="_blank">📅 17:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652283">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoBEUqJymBJrRvJC11xQ1vgMpCfTdh1WgFTKm72casjRns3n2NuPXTpx7QaeTmqSZ6s-efrIOXXStpSKIbPekpi17jhxP56yyUqGB4LHVMK66WOYBm0it7VCVFPMEYqcNYcEUkjaNroQA5Tui_RAvUKXKEmiHrX_rtKco4Tk03j1BjXPxhHZnVf5hdRBvYJViyjCM7H1-lE3MrZsbRylXF-Iu6cKkd294Hg3Hwkdz7xx29Paw9EEp0xiW8jETAPZwQuigjerM3FoW4Fm9L-M2tLb-ydOJTz541STJ3l7XTnRRjwTL8unI9tgvG9m0VcIA_wGMybJPZFuO0s4IHMvYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی در راه آمریکا / افکار عمومی چه نظری درباره جام جهانی دارد؟
🔹
نتایج یک نظرسنجی در وبسایت خبرفوری نشان می دهد که بخش بزرگی از افکارعمومی موضوع اعزام یا عدم اعزام تیم ملی فوتبال کشورمان به جام جهانی فوتبال آمریکا را در شرایط کنونی چندان موضوع مهمی نمی داند.
نظر شما چیست؟ بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3214858</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/652283" target="_blank">📅 17:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652282">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6422e614c6.mp4?token=d_8V39Gz0ZK_sfe6bpqlQvjqEySEa56e2UoVp0SkITioQvhPw75ujKw93Umz6gBI-fROGMNgWQUjnR4uR7udDJFcBCuf02tNgmKG9kPIb-Appn6zbOtGqHLHcZkOFQ-0mHlKrB5n47OA6LogrfNtaCmRMp7dWEQTPyrYtdxQFCdiBTxE6-NGB0gupomxJGipFwiu48m7EqoJlGDAx5hd-aj6ADwSh-79CuXqkCyYwbj5fuX2h83JfiKr2cTTpRUzU2YVtyUWY4gLTpKLlq59-wNo28c406eZpmbTNtif0KKr_bEYlIx_N5am2IE95Nm_0YoA_h5AUfjl0n7QtXEJ-5m2pRcvN7oBbI5NBMGQxfhH09H-Keai2RCNtsq7d06ef3Mjqjz90YsIQeFw9pNqRhLgFe5sUxnYIE4-mAjOGgvSYfNAfFdYvxOo2wmFmlWpCheT1uxjtfqLWb5lK5ynPAIqMN1AjlvRg1Ahr8h0rlOIX55mn78dC_tKebN85ALIYnAUYNX0-IchQgSUCRORA7N7ynp8sAA2ew-OsLDc5xSobkH2Wq033JBagRCzh2FwYjBAcjDXHmK8V7dZ8X016Hs12WsO0rINOJQBIUIrSwBLNRTSxpUe6VqlJkaHcYTo4fLvdQVS7T40jAL-w1nYcUt0miDC0sV64OEHabOYJkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6422e614c6.mp4?token=d_8V39Gz0ZK_sfe6bpqlQvjqEySEa56e2UoVp0SkITioQvhPw75ujKw93Umz6gBI-fROGMNgWQUjnR4uR7udDJFcBCuf02tNgmKG9kPIb-Appn6zbOtGqHLHcZkOFQ-0mHlKrB5n47OA6LogrfNtaCmRMp7dWEQTPyrYtdxQFCdiBTxE6-NGB0gupomxJGipFwiu48m7EqoJlGDAx5hd-aj6ADwSh-79CuXqkCyYwbj5fuX2h83JfiKr2cTTpRUzU2YVtyUWY4gLTpKLlq59-wNo28c406eZpmbTNtif0KKr_bEYlIx_N5am2IE95Nm_0YoA_h5AUfjl0n7QtXEJ-5m2pRcvN7oBbI5NBMGQxfhH09H-Keai2RCNtsq7d06ef3Mjqjz90YsIQeFw9pNqRhLgFe5sUxnYIE4-mAjOGgvSYfNAfFdYvxOo2wmFmlWpCheT1uxjtfqLWb5lK5ynPAIqMN1AjlvRg1Ahr8h0rlOIX55mn78dC_tKebN85ALIYnAUYNX0-IchQgSUCRORA7N7ynp8sAA2ew-OsLDc5xSobkH2Wq033JBagRCzh2FwYjBAcjDXHmK8V7dZ8X016Hs12WsO0rINOJQBIUIrSwBLNRTSxpUe6VqlJkaHcYTo4fLvdQVS7T40jAL-w1nYcUt0miDC0sV64OEHabOYJkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم ایران این‌چنین‌اند؛ ما با هم از این سختی گذر میکنیم
🔹
روایتی از مراعات حال مستاجرین توسط مالک‌ها در شرایط سخت این روزهای جنگ.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/652282" target="_blank">📅 16:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652281">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcO_JjFYfluVSKnEree4OgUIYjWHKwwA98y-auuVcDCdNOhLXgN6AA6k2Pn50eQIB8pknK7vpSmnoaEkNb8IhspxRrOf2TgidXJFTw4eoX-rzyCpv_KwGUZ71O_gmC7codryrjInBqk9kolN1GJyI6-5wuFoVcHDib8azNY86_YFyhHGI_Kdm2aGtMD6ap1aj3Shql9KVy606RqzKFNd1ZZ2DEo2CsgnuQ0Ve6RdDtGhr6t4VrPWFiGl85atamIPEASB0tknOhVe5KHAd20kFJI8jEuhe_ltZgP-insZ6xjLFmyW64F6PxKOtkEO6gBpJnr5mL5s9pjH-4SRBRav_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقوق گمرکی دارو و شیرخشک یک درصد شد
🔹
رئیس کمیسیون گمرک اتاق ایران: بر اساس مصوبه هیأت وزیران، حقوق گمرکی واردات دارو، ملزومات مصرفی پزشکی، شیرخشک اطفال و مواد اولیه آن‌ها در سال ۱۴۰۵ به یک درصد کاهش یافت.
🔹
مبنای محاسبه حقوق ورودی این اقلام نرخ ارز درج‌شده در ثبت سفارش است و در صورت استفاده از ارز ترجیحی، نرخ ۲۸۵ هزار ریال برای هر دلار ملاک محاسبه قرار می‌گیرد.
🔹
این مصوبه از ابتدای فروردین امسال اجرایی شده و می‌تواند به کاهش هزینه واردات و تسهیل تأمین دارو و اقلام پزشکی کمک کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/652281" target="_blank">📅 16:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652280">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6IHSLr6mGecTfXsxJ1R0d8FuFbckXkfGpsPzKS2mD6qZItWZQUL6RAh_VP33W7GpyPtjmN6lYcutZRpQ8QcrVjIVK-CVjPM_EOErJAzUYS5uSwUob4NwBzJURCmAAyXyki4uOcvIDlW5p8A31KF250BjUbWNbKq57o7whgWyqkt8KkQfAWOhHP00QWFT9c0ZNVbjwPc7I0L9kmZRNjmIhbm4d65JJziACFO32SYJvvCqG1UyIwr3mW9JMhgMuXn_17Jh8BEN1MA5Yx6C0r-ZdZoCAihhIJ9PXdOMpkp7JVoq159Hqib0MdREmqR0_bE6g83NxzugEiLE7_1O5Cf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهدید تازه وزیر جنگ اسرائیل علیه ایران
🔹
وزیر جنگ رژیم صهیونیستی به رغم تمام ناکامی‌های ارتش اشغالگر در مقابل محور مقاومت در تمامی جبهه‌ها، ادعا کرد: «مأموریت ما در ایران هنوز به پایان نرسیده و باید اهدافمان را در این کشور کامل کنیم».
🔹
اسرائیل کاتز مدعی شد: «ممکن است به‌زودی عملیات نظامی در ایران را از سر بگیریم تا به اهداف خود دست یابیم. ما برای هرگونه اقدام قریب‌الوقوع در ایران آماده‌ایم».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/652280" target="_blank">📅 16:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652279">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b95Gw0IvsR-wvIdDXw3SOZmgC7fweHNwwYM_u-q1Hm8MYtEbcRIo30MlUN4ypNaOSlt6TcuASMXXPGBgmMn1T01USvb0zqaF4h38nwKygNx80spxU7hlpirBsI6ElZ97rHdouwLKlNJbBL-3gmAbfh7Feynr2JB53nioIZHcOcCYcqqMFYU_zO1fkAK-fRnFFdgGkEw-W4y_HVBKUWxyx0bKHi8EZmTQ8U3rKql8lTCF1MtCdCKSXjEKcmCqBFSZYYZikjvw-v0XrcnrBKXiBhmtcOWBFzXMJS3qSrllHOueeDcN6Y5slplzUdK_iaI95gJ87nALd-StGfazPmEYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تریتا پارسی: امارات با پیوستن به توافقنامه ابراهیم مرتکب اشتباهی بزرگ شد؛ توافقی که هدف اصلی آن ایجاد ائتلافی عربی-اسرائیلی علیه ایران بود. حالا به واسطه جنگ اسرائیل و آمریکا علیه ایران، آن هدف اصلی به وضوح قابل تشخیص شده است
🔹
این اشتباه از سوی امارات بود چون به این معنا بود که امارات خود را به دشمنی اسرائیل با ایران گره زد؛ دشمنی که بسیار عمیق‌تر از تنش‌های خود امارات با تهران است، با این که امارات در همسایگی ایران قرار دارد در حالی که اسرائیل حدود هزار کیلومتر با ایران فاصله دارد.
🔹
اما ابوظبی حالا در تله افتاده، و تا حدی به نظر می‌رسد جنگ ایران با هدف وادار کردن کشورهای شورای همکاری خلیج فارس به نزدیک شدن به اسرائیل برای جستجوی حفاظت در برابر ایران طراحی شده است.
🔹
به همین دلیل در میانه جنگ، نتانیاهو مخفیانه به ابوظبی سفر کرد و حفاظت گنبد آهنین را به امارات پیشنهاد داد. اسرائیل این را یک پیشرفت بزرگ در روابطشان می‌داند.
🔹
در واقعیت، این تجسم همان تله‌ای است که توافقنامه ابراهیم برای امارات تبدیل به آن شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/akhbarefori/652279" target="_blank">📅 16:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652278">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV5CUn04TCaEC0lbMybJbEyTiYdD1RzOUSVbnHJHMCkVW054bSs4rrhgSCo-Y6AlGtHnXAm3QtY9zGgTfqzgELYuE3ViCvvqZWrOl4osNE14tHiB4oTOhjn_WhnAcL6Ty_ewGVdjoP2kIyJT5ply7Jus35a9WkwRZ-aSan3Q3mTMjNbIl5JRe9Nzo-IJGlll5Kiq2_nZ0P_HpOXdohSSlIVS8KGTCutQ-KaujxhEq2I3LCIQ9h27-u96dRPvB2ZingbpsfDl8UQmO-ATl2n4ylt_LQnf98G3M0dvEfMsZASbO5Zn7uW8s4tEemnC7YdhWJ70MrlZqPPdJnhOTPDS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک ترامپِ بدون موبایل | قرنطینه دیجیتال تیم ترامپ در سفر به چین
🔹
همزمان با ورود دونالد ترامپ به پکن مقام‌های آمریکایی تحت تدابیر امنیتی کم‌سابقه‌ای قرار گرفته‌اند؛ وضعیتی که برخی آن را «قرنطینه دیجیتال» توصیف می‌کنند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214792</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/652278" target="_blank">📅 16:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652277">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a27ad55f.mp4?token=MmzOxrpX9_iB-QAdBCLhvsDqIjuSO8_2LtRTH_1EuPP2Kq8PPLh-3kaPWidx1OeT8aSpIAVUd3wtQvb_leXL4rAf15a2cim9YCmu9OHld2Wfj6qRMal-wYNUxhtxdGIMlkYZBOAHqz3FzANhkVyhrLdg7E-YUDhYd9jf2DkKwejQu_4axmOMchdaoxWBA6OcOVMziWoPPCM1g32jIeO_PEhVC_o_lZAFRjZ-s8Kuo1XiqjXaUDFz7DAhaA_3jMatUvq9-Cv_AZKmnwoRu8EezVCVGZSblyQQFV5jYFrg8lMOlwdvytGs83hYQh8fLdBnxJxhMOaifNKEZBrvs11xB3Dm8Kzq9ndqEKFhgHkbpGGxEki9lue9KtuSuUrldVGPR32k6lruDP45ZGmighkQHWPf31XyaNb4BVxCpgS5bg3xFFXBXU17yI9DIpf3GbjEx1-DnPKXEHKnaXyJNcDPxHQ-oR9GwCPgVpQdzHM5Y-f02OVKSGW7_35qDs93TFiR-hD0fkhWV-yQYf_a7bE9BG2ti7xiaoeMB-gDBDS-wUpEWutIaQ_8EPcmgRtL3tUfzR7jGqC7AvRaBES7cFSFKEGzGbxZrN085EP4mmsRr1DxRbxwHs5b-Ns7qiPkduEtn3Z7UwfJ0e4UF6O2Gs1_QbjCHmBMaMwqt4bpD44raSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a27ad55f.mp4?token=MmzOxrpX9_iB-QAdBCLhvsDqIjuSO8_2LtRTH_1EuPP2Kq8PPLh-3kaPWidx1OeT8aSpIAVUd3wtQvb_leXL4rAf15a2cim9YCmu9OHld2Wfj6qRMal-wYNUxhtxdGIMlkYZBOAHqz3FzANhkVyhrLdg7E-YUDhYd9jf2DkKwejQu_4axmOMchdaoxWBA6OcOVMziWoPPCM1g32jIeO_PEhVC_o_lZAFRjZ-s8Kuo1XiqjXaUDFz7DAhaA_3jMatUvq9-Cv_AZKmnwoRu8EezVCVGZSblyQQFV5jYFrg8lMOlwdvytGs83hYQh8fLdBnxJxhMOaifNKEZBrvs11xB3Dm8Kzq9ndqEKFhgHkbpGGxEki9lue9KtuSuUrldVGPR32k6lruDP45ZGmighkQHWPf31XyaNb4BVxCpgS5bg3xFFXBXU17yI9DIpf3GbjEx1-DnPKXEHKnaXyJNcDPxHQ-oR9GwCPgVpQdzHM5Y-f02OVKSGW7_35qDs93TFiR-hD0fkhWV-yQYf_a7bE9BG2ti7xiaoeMB-gDBDS-wUpEWutIaQ_8EPcmgRtL3tUfzR7jGqC7AvRaBES7cFSFKEGzGbxZrN085EP4mmsRr1DxRbxwHs5b-Ns7qiPkduEtn3Z7UwfJ0e4UF6O2Gs1_QbjCHmBMaMwqt4bpD44raSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام ایرانیان وطن دوست مقیم نروژ به مردم داخل کشور
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/652277" target="_blank">📅 16:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652276">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وزیر امور خارجه آمریکا، در گفتگویی با ان‌بی‌سی نیوز ادعا کرد که ترامپ در جریان نشست با شی جین پینگ، رئیس‌جمهور چین، مسئله جنگ با ایران و محاصره تنگه هرمز را مطرح کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/akhbarefori/652276" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رسانه‌های رژیم صهیونیستی از وقوع حادثه امنیتی سخت در مرز لبنان و زخمی شدن دست‌کم سه نفر خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/652275" target="_blank">📅 15:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2xkwAKwG6WbAFXgDlwkQ7hcXTY6K64UCvJx_Vyz70WEdmM8JNwaFXsG-2MVxkA8q0Qgy3fa-jKwvzVxtRreSKGyMXsBEQMAm5tzV9CgrN2-AqxCL5QF1WfX-nWdTjGWq7db46qKgqdtGqeh9XeM3vO3ebgoZ3jlJuMJeu20jR2x0tt__NNTAF85tqeg-U_8qgJMkjLEgv1Dt0wMUZEHL2FE_MC40C9Jk8DIQOLwNOTFCiRjlTTDTDLXq1iJy9ETGsjJLcMVE-lrPXuWDBT8e8epHqMXLrBneC2AL7zk-c_0h3O-XHbduhFTgP7au1FwD4V0fXbrLLo7izDbMvkTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتلانتیک: ترامپ برای یافتن راهی جهت خروج از جنگ ایران به تقلا افتاده است
🔹
ترامپ در حالی که با فشار فزاینده‌ای برای پایان دادن به درگیری‌ها مواجه شده، اکنون به دنبال مسیری برای خروج از جنگ با ایران است؛ جنگی که منتقدان می‌گویند از اول هم بدون استراتژیِ خروج آغاز شده بود.
🔹
به گفته مقامات ارشد آمریکا، ترامپ به‌طور خصوصی از هزینه‌های فزاینده و پتانسیل یک درگیری گسترده‌تر ابراز ناامیدی کرده است. با این حال، هرگونه عقب‌نشینی نیز در این مقطع، به عنوان ضعف آمریکا تلقی خواهد شد.
🔹
کاخ سفید همچنان برای تعریف «پیروزی» در این جنگ پیچیده، با چالش جدی رو‌به‌روست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/652274" target="_blank">📅 15:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fee3b23f.mp4?token=ZAwuvWm_yq3RT0B_-ncU21tRcwbEV0Xyq7E9d2Vclad9j47DtKPE3k-i-31nqu3k1IQs4I3IFzYriynMqzFoRgMfa1R0bTUMtRuDnk_EQmjjpvogntbVjg2WK2f2R6GoJyPyQxfwT3SEytxf6GJBLdqxp4oVPcI-wMNRSR9ELDeyhcVnuvCFDu-BPnnCRYEajG1iXiYzVWhy2dqRle6CKdHvxnz2FCHTc0gFCEsVcxP3ySiOsqHVPKLqb4C6FuFi7Mh0uAMPrGagQscyuHFNzV_U0947i1iHEGCTnIy93yiL0kC75bIaQ9JZpLjLey03pWoKs-GxamH_NrJTejsK1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fee3b23f.mp4?token=ZAwuvWm_yq3RT0B_-ncU21tRcwbEV0Xyq7E9d2Vclad9j47DtKPE3k-i-31nqu3k1IQs4I3IFzYriynMqzFoRgMfa1R0bTUMtRuDnk_EQmjjpvogntbVjg2WK2f2R6GoJyPyQxfwT3SEytxf6GJBLdqxp4oVPcI-wMNRSR9ELDeyhcVnuvCFDu-BPnnCRYEajG1iXiYzVWhy2dqRle6CKdHvxnz2FCHTc0gFCEsVcxP3ySiOsqHVPKLqb4C6FuFi7Mh0uAMPrGagQscyuHFNzV_U0947i1iHEGCTnIy93yiL0kC75bIaQ9JZpLjLey03pWoKs-GxamH_NrJTejsK1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: به هیچ قیمتی تنگۀ هرمز را از دست نخواهیم داد
🔹
اصلا تنگۀ هرمز مال ماست؛ ملک ما بوده حالا مدتی از ملکمان خوب استفاده نمی‌کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/652273" target="_blank">📅 14:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دو راه‌حل پیش‌رو برای موضوع بنزین
مصطفی نخعی، عضو کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
هنوز تصمیم نهایی درباره تغییر سهمیه‌بندی بنزین گرفته نشده و سناریوهای مختلف در دولت در حال بررسی است. ایران پیش از جنگ نیز روزانه حدود ۲۰ میلیون لیتر کسری بنزین داشته که از طریق واردات جبران می‌شد.
🔹
درحال حاضر یا سهمیه باید کاهش یابد یا از ابزار قیمتی استفاده شود که حداقل مجلس چندان موافق این موضوع نیست. ذخایر بنزین ما نگران کننده نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/akhbarefori/652272" target="_blank">📅 14:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652270">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxIbhS4VlCNa5ZTRVkL8RIUd0tYOK4PHcdz21e1U3gLazgissmc_fQkYwAbKg0585E03feTj4HfSMVG1rWjPXeSW44rllA164yLVZPzIgdZoRHh3W1wCRX7aP86VognjJE6bmucMdC3lsw9YGweuoUJXwh_2NwDbd66sGiODumGDvlPmr73uTWC68qWqP2-XCKKtQu5mEiho0EGcKJ1TjbF26x1J7EVdZ1WmKxNFVIo5cMYpkojaSsPYMNq6no5ZTWpALrVVlnEwksapUSbJg3lLlsLtEFZgQmVH5cGz5Hx2qR85JfpldHPCNPf_A68RBsku6szuOru6dWX0m1zRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سانسور تصویر زن ایرانی در رسانه‌های بین‌المللی؛ تصویری که شاید به نفع آن‌ها نیست!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/652270" target="_blank">📅 14:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652269">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38ac5d731.mp4?token=Nb9EhxYbuE5Blzbi4xWsPdKfPY9xQ0trIe7BlgQt8uUzkz_pb9FkYf8tAtXn2po637dYsPADnjy15nqcFDytobn7QI0BZrm4ak1lFgrdrcFARBpBtg9qY_RYpKovDY-GM-3Bfc-o_BTvw7ECW4jTI1HEr4MPwTpcNzc-UnWdOxBtXazrWjhI-msBz-iF2E2BFeH_XZq8WQlC8GgzrpFl22a9sM7EdVzYk6zPL_VPe5raC0wmW2juHkuq6zANN_79WGahuHiUP3m_i6uUXPv7uXwuqUvopP9lqpSqOp4eCw8q7dqHfmYNbvc7Fu9iX5GB_GmZn3XlaYpPmLzRTvE0Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38ac5d731.mp4?token=Nb9EhxYbuE5Blzbi4xWsPdKfPY9xQ0trIe7BlgQt8uUzkz_pb9FkYf8tAtXn2po637dYsPADnjy15nqcFDytobn7QI0BZrm4ak1lFgrdrcFARBpBtg9qY_RYpKovDY-GM-3Bfc-o_BTvw7ECW4jTI1HEr4MPwTpcNzc-UnWdOxBtXazrWjhI-msBz-iF2E2BFeH_XZq8WQlC8GgzrpFl22a9sM7EdVzYk6zPL_VPe5raC0wmW2juHkuq6zANN_79WGahuHiUP3m_i6uUXPv7uXwuqUvopP9lqpSqOp4eCw8q7dqHfmYNbvc7Fu9iX5GB_GmZn3XlaYpPmLzRTvE0Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسوف اقتصادی برای دنیا با بسته شدن تنگۀ هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/652269" target="_blank">📅 14:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652268">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bcc3a2430.mp4?token=CHHgLC6fUoIp1kXPexrUmnitPyemk1V0w9uhZ31GySvNJU7ng6ZmZmEZzJwYZdOpLDjvnthjd7sRS7si8vWd9hO0tR-F-p8UzLd6CJSyTVhtaJwCFkrHzbWdphJ7b26EZYg6rswsgmM6H0W-tF7GADBECYbDrdxZgkIiHSX3bo29jD6yuv8iQ64-RRsCA3CXz8De4m923Hm4whOjdjcXlv-73-Ml1AmltAw5jqYBStxUtPvu-5YjSJ8gCAtaK9xZcAgpZ9V_OQvOxZ-xyXQA2-iyAnvqB2CMZC57gkqy5HU3gCY8cHOJrb6mJb41iYOe-3k0wJvAJR9FHVi04uNmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bcc3a2430.mp4?token=CHHgLC6fUoIp1kXPexrUmnitPyemk1V0w9uhZ31GySvNJU7ng6ZmZmEZzJwYZdOpLDjvnthjd7sRS7si8vWd9hO0tR-F-p8UzLd6CJSyTVhtaJwCFkrHzbWdphJ7b26EZYg6rswsgmM6H0W-tF7GADBECYbDrdxZgkIiHSX3bo29jD6yuv8iQ64-RRsCA3CXz8De4m923Hm4whOjdjcXlv-73-Ml1AmltAw5jqYBStxUtPvu-5YjSJ8gCAtaK9xZcAgpZ9V_OQvOxZ-xyXQA2-iyAnvqB2CMZC57gkqy5HU3gCY8cHOJrb6mJb41iYOe-3k0wJvAJR9FHVi04uNmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون جوانی جمعیت مجلس: وام ازدواج بعد از قانون جوانی جمعیت ۱۰ برابر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/652268" target="_blank">📅 14:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652267">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k58fAw1UR5FbTf3Yijj-NVHk3GRJajwrw15KSrW7tyhx73cHwn7CePNVwXj5hUITjnHigy8bdvPaToepjp0qz1dsTBohIUfqJwXdD5yeEveywZR8M26HWC7a2OU8bJCGZ5B-Vbs8WY5pQykxicWmcDVZM-1NZR80E0xoRExHcLW6TuU64k2854h262RcPzFKMSpgGDVW9NsIIh5RT6IZNz_J6mAtpPJwvW1qSbhfMoI9AALJfQDCki7EvmsTYI3QopUlW1FtzP-kq2jsrTO8hXPKgYhcvF9UM5kbJmaMzltEsbXzvXeskIqy0Ag6Bm4248n1ZWG79pVWhxYFKwxJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره‌جنوبی: به ایران حمله دیپلماتیک می‌کنیم!
کره‌تایمز:
🔹
یک مقام ارشد دولت کره مدعی شد که ایران به طور قطع پشت حمله به کشتی باری کره‌ای HMM Namu در تنگه هرمز است.
🔹
او تاکید کرد تحقیقات هنوز در حال انجام است و قول داد که پس از تأیید، «حمله دیپلماتیک» علیه مسئولان انجام شود. در آن زمان هیچ دزد دریایی در منطقه فعالیت نمی‌کرد، اگرچه تحقیقات هنوز قطعی نیست، اما بر اساس عقل سلیم، بعید است که هیچ بازیگری غیر از ایران مسئول این حمله باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/652267" target="_blank">📅 13:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652266">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b74446bc.mp4?token=jcUhzEwhKtNLQn384a77DjcRyIciqlv_ccI1ETosfB1eDojyTOPan_2PeJbMH6Rkh76mQfoAuLtWCIhGYBw07MUWXN0rvSWIyV8kOgt51crjdFxojvChVCuWsRTXno_e2EoLT6ppIUE5RZpQ3h1w7fZGWjtnk0p91MdMg9WTNaB_xgcCJLcoAwPcdcakN1ZIWJj60G6Q1JutZ8QZh6N3KZ3w5xr7dFgusG0HXsg673U3lt31g3LeHDdm0_nZYJ9z4KP3bjBx29iu0R2Bal2uTpo0LS4kGJNCp0aXS6WfMv_hhXJhxCNdUtcTsI6eWnSnyK3Qrvkdh6km4YJ2lVfq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b74446bc.mp4?token=jcUhzEwhKtNLQn384a77DjcRyIciqlv_ccI1ETosfB1eDojyTOPan_2PeJbMH6Rkh76mQfoAuLtWCIhGYBw07MUWXN0rvSWIyV8kOgt51crjdFxojvChVCuWsRTXno_e2EoLT6ppIUE5RZpQ3h1w7fZGWjtnk0p91MdMg9WTNaB_xgcCJLcoAwPcdcakN1ZIWJj60G6Q1JutZ8QZh6N3KZ3w5xr7dFgusG0HXsg673U3lt31g3LeHDdm0_nZYJ9z4KP3bjBx29iu0R2Bal2uTpo0LS4kGJNCp0aXS6WfMv_hhXJhxCNdUtcTsI6eWnSnyK3Qrvkdh6km4YJ2lVfq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قصه پیرمردی که از دیرباز در کارهای جهادی بوده
@TV_Fori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/652266" target="_blank">📅 13:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAfaRzb9Ko8Wju1tJT2WPImeQbQ5LVM3I88xb2jHFV21YE_JS0Je4CJWkI7J7ljInJBKRO5MMiSGZIaSjE9sXO4CXUv5n6U6OiFsRM3sOq2J9YQUl6bEBENGhtXqm_SMk44ktuNrouai8wLyRLYws00hEjg6_HpnjFpsG9FA9qZ4xnosIicD_-455b0CjMcn4SmgtcXecQUUEdyWApxy_JPZx9cscVk4e9bDDDz-oxLWYo6PdyWKlbd7c9py2QonKRLRTrFidnOqE2pwsaZEAsJ-BTVxuZPj9jN4Sxubatt_tabKWHgBmr_fvawU-iSEqj9yFU_TW3oxB0Lgv_KZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باقری: هدف آمریکا از حمله به ایران، ضربه به هم‌گرایی آسیا بود
🔹
معاون دبیر شورای‌عالی امنیت ملی در نشست دبیران شورای امنیت ملی کشورهای عضو شانگهای: شخصیتی که امروز می‌بایست در چنین جایگاهی از طرف ایران قرار می‌گرفت و به گفت‌وگو می‌پرداخت برادرم آقای علی لاریجانی بود که ترور شدند.
🔹
در طول چهل روز تجاوز بی‌وقفه، شاهد ارتکاب جنایات وحشیانه‌ای از جمله ترور مقامات نظامی و کشوری، حمله به تاسیسات هسته‌ای صلح‌آمیز، زیرساخت‌های صنعتی، آموزشی و بهداشتی بودیم.
🔹
دقیقا هدف آن جنگ ضربه به همین هم‌گرایی آسیایی بود. جنگ با ایران آغاز حمله به جنوب جهانی است. این جنگ برای توسعه‌طلبی و اصالتا امپریالیستی است تا با ایجاد حوزه نفوذ و تسلط مطلق بر منابع انرژی خلیج فارس مانع از رشد آسیا و ظهور قدرت‌های میانی شود.
🔹
لذا این جنگ اگرچه با ایران شروع شد اما محدود به ایران نیست و در صورت انفعال و بی‌عملی در برابر آن، تسری و گسترش می‌یابد. هرگونه پاسخ ضعیف، دعوت به جنگ بیشتر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/652265" target="_blank">📅 13:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652264">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPAB7mhXNIfuSLpX3TIjIMnM5pmE31W3WHlEijXoedYeMswTRn_quP4Q2jxuYH97tVYFgsgLrEJ-tNJ9x4FCXAGESVZ3C9zvGUVCbScDuxcNpsKYGfbvyCs3AkUg0XvTwAGRHZoe4HkQRYWkxvQIcw71ydKGODcAxiAvdaAL6EFHTs3iCsPiAOTdH7YLtoUWORf9uNANcjeJhvDq8pt5K9sQzjVmrS9SaBHCDadfk-Doj48chIs7KeZzVWiIOWwGKgmjFRROwTTyLXyGswdjVfbqd4Fl3TnuOm3GuuyBiTpcBx7DI7rsoTO5Mzrv8Jyrmyr12XVnBvMebTpgIVvNPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل هیوم: در حالی که توجه‌ها به سمت ایران معطوف شده، حماس بی سر و صدا در حال تسلیح مجدد خود است
🔹
گزارش‌های میدانی حاکی از آن است که این سازمان با سرعتی نگران‌کننده در حال ترمیم تونل‌های تهاجمی و خطوط تولید راکت‌های خود است که در درگیری‌های پیشین آسیب دیده بودند.
🔹
منابع اطلاعاتی هشدار می‌دهند که مسیرهای واردات از طریق مرزهای جنوبی دوباره فعال شده و قطعات الکترونیکی پیشرفته برای بهبود دقت موشک‌ها به دست حماس می‌رسد.
🔹
علاوه بر تقویت سخت‌افزاری، این گروه در حال آموزش نیروهای ویژه جدید برای انجام عملیات‌های نفوذی پیچیده است.
🔹
تمرکز بر توسعه یگان‌های پهپادی و دریایی نیز بخشی از استراتژی جدید حماس برای ایجاد تنوع در جبهه‌های نبرد علیه اسرائیل و منافع آمریکا در منطقه است که به شکلی مخفیانه در حال پیشرفت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/akhbarefori/652264" target="_blank">📅 13:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7LqBHqR4vh47S4q97IJzYqAoorP8aIJu8Q3HWk0j3KMau0zDlFLRDMcQZOnapEDGRYxso1geWf-TalloDuDDuszMpn3H0UHzE_t3APJuLrJz0xIku6TMkuScux9gP3lJPt3LBnOrLIBYiAcoyYOiNxlY3dBRtvjYNABTOGhGjBA3vUgBTjmfuFP_K0pVPqFIrywg7syyII3aj93Q60OzQWidizn0ecOifKAGBnp5MUGH_WJV07NZ42fmmaQyIXxs7wKYqgonIwK3TOKf5ZXGLF_78CvjpXXJHIb_khuwz_EQQibLZcCki0RSttHCQtNP5dx1inYY04GPGnvxTtxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان بارندگی در نقاط مختلف کشور
🔹
طبق داده‌های رسمی، از مهر ۱۴۰۴ تا پایان فروردین ۱۴۰۵ نشان می‌دهد که در سال آبی جاری بارش‌ها نسبت به بلند مدت ۲ درصد و نسبت به سال گذشته ۵۸ درصد رشد داشته است.
🔹
نکته جالب اینجاست که بخش‌های جنوب و جنوبی غربی با میانگین بارش ۳۱۶.۵ میلیمتر بیشترین بارندگی را داشتند. نواحی شرق و بخش‌های از جنوب شرق هم با ۹۴.۹ میلیمتر کمترین بارندگی را تجربه کردند.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/652263" target="_blank">📅 13:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652262">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDnuQw4wHAFzDXbxrzqXfNYVOu9eVviG0fGwRYbMT3z12ejhWoHHyFo40Du8Qa20cO5j_Ec2-Fu15R2tqSqUndJRu1KP8KsRQveWJiI6BpjHX2GQAPeftJ8tynpv60vlX8YGU4XYVSo9owEyEgHDCbqPiVeb4irgu76V5nvcvJRACH-TKqymgdltIBEmFkH0qM8am91cjMsCwiQknwRR3_jbBaGqReQH53okaTSmpcJbcPjm2pdYX2VFmO9CE7V1Skipxh3i0ZPU5ii4ZrCFJU1jyEHQ4B05E5UHtAAG7Kdj42eEBl9a7-L6d8ty1gjDZr3Th9ts9L5zWYSY359SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین نفس کم آورده...
🔹
پلاستیک و آلودگی همان لوله‌هایی هستند که راه تنفسش را بسته‌اند. وقت درمان همین حالاست، نه فردا.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/652262" target="_blank">📅 13:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652261">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
واشینگتن پست: ارزیابی اطلاعاتی محرمانه آمریکا نشان می‌دهد که جنگ ایران برای چین در جبهه‌های دیپلماتیک، نظامی، اقتصادی و اطلاعاتی مزیت‌های استراتژیکی برابر آمریکا ایجاد کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/akhbarefori/652261" target="_blank">📅 13:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
عراقچی: امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود
🔹
سیدعباس عراقچی وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات در این نشست طی اظهاراتی بیان کرد: من در سخنرانی‌ خود نام امارات متحده عربی را ذکر نکردم، به خاطر حفظ وحدت و ترجیح دادم به آن اشاره نکنم.
🔹
اما در واقع باید بگویم که امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود. زمانی که این تجاوز آغاز شد، آنها حتی از محکوم کردن آن خودداری کردند.
🔹
آن ها حتی حمله وحشیانه به مدرسه را در همان روز نخست تجاوز محکوم نکردند.
🔹
نماینده امارات درباره حقوق بین‌الملل صحبت می‌کند، اما لطفاً به من بگویید کدام بخش از حقوق بین‌الملل اجازه می‌دهد از یک اقدام تجاوزکارانه بی‌دلیل و بدون تحریک قبلی حمایت کنید؟ همه می‌دانند که ما در میانه مذاکرات بودیم که آمریکایی‌ها و اسرائیلی‌ها تصمیم گرفتند به ما حمله کنند و ما شگفت‌زده شدیم که برادران ما در امارات تصمیم گرفتند فعالانه به متجاوزان بپیوندند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/akhbarefori/652260" target="_blank">📅 13:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhT4RMRwN8Flr55opFdUk3cmZt6TmIJpXJyIp63LAjIvKxztAT8mHGTC4MVS8nsqdwdrdVH1nu1I7eUxcf9TJyPGX6XfJ5Bb1gWh4hnY6wd5U28ZSWjYnGY7h7byQeYG4Y16VmlVZJ5dEtw6s-61mOna3uamuxK-b30wbLKRW6E237AI3210rq0BIJlc-50IGfzzl4CD29Dba9EJof1ZNCbDVfcbWaFyKz7QZSCXvaauMlzL0hgjp8pFpS0WB2JkUu-VIt-_BpZKznF4Y7ECI0iqHDKfWfYWazX1XtCHumTukYgVBKvz1jMsR9Ocw-ELO-YsKJjU91nqeZv_EbpPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی خطاب به امارات: ائتلاف با اسرائیل هم از شما محافظت نکرد
🔹
وزیر امور خارجه امروز در نشست وزرای خارجه بریکس در دهلی‌نو در پاسخ به ادعاهای بی‌اساس نماینده امارات گفت: ائتلاف شما با اسرائیلی‌ها نیز از شما محافظت نکرد و در سیاست خود در قبال ایران بازنگری کنید.
🔹
سیدعباس عراقچی افزود: من در سخنرانی‌ خود نام امارات متحده عربی را ذکر نکردم، به خاطر حفظ وحدت و ترجیح دادم به آن اشاره نکنم. اما در واقع باید بگویم که امارات مستقیماً در اقدام تجاوزکارانه علیه کشور من دخیل بود. زمانی که این تجاوز آغاز شد، آنها حتی از محکوم کردن آن خودداری کردند.
🔹
وی ادامه داد: آنها اجازه دادند از سرزمین‌شان برای شلیک توپخانه و تجهیزات علیه ما استفاده شود. همین دیروز فاش شد که نتانیاهو در زمان جنگ به امارات و ابوظبی سفر کرده بود. همچنین آشکار شد که آنها در این حملات مشارکت داشته‌اند و شاید حتی مستقیماً علیه ما اقدام کرده باشند. بنابراین امارات شریک فعال این تجاوز است و هیچ تردیدی در این باره وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/652259" target="_blank">📅 12:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پزشکیان: هدف قرار دادن اماکن ورزشی نشان‌دهنده دشمنی با عزت و سربلندی ملت ایران است
🔹
رئیس جمهور در بازدید از آثار حملات و خسارات به مجموعه ورزشی آزادی: دشمنان از هر نماد امید، انسجام و افتخار ملت ایران هراس دارند. تسریع در روند بازسازی، احیای کامل زیرساخت‌های آسیب‌دیده و حمایت همه‌جانبه از فضاهای ورزشی کشور ضروری است. چنین مجموعه های ورزشی بخشی از حافظه تاریخی، هویت ملی و نماد تلاش، امید و افتخار جوانان این سرزمین هستند. دشمنان ملت ایران، نه‌تنها با توان دفاعی و پیشرفت علمی کشور، بلکه با هر نماد عزت، نشاط، همبستگی و سربلندی ملت ایران دشمنی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/652258" target="_blank">📅 12:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvbKji7KUt8Jvs6J1-4oOrrHqCbgdF6GG0yx7htRE5y4p5ifjVM___WYoYGxDHEPWtPsN-KImC_MIQmd9G0aYc-Vk5vAzFg_fyT-5wRCp00PXr0oWRYya3QljPQB7SkFg4C5IYmAyYnFIoDPkahPwZitJTWiXZDRxiUxLbZ5HvZDPBwxa-_0tBzTzyvTvfI3hAHuBOgW9MLXP4A0z0hITbA7V-Td5rVpDAIobnvM3sALwQxbRL33gEUXAmEo5QagNsnhZHoDDl4nMLcOkIXWybCop6N9cbCYP8wrDlAP8FqeTjB2RXvapDwOfpbgH88Zy4Q3cG9NT1mYurLEw_n5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: بستن هرمز باعث افزایش هزینه‌ مصالح شده و پروژه‌های ساختمانی را در جهان متوقف کرده است
🔹
طرح‌های عمرانی در جهان به دلیل کمبود مشتقات نفتی با تأخیرهای جدی روبرو شده‌اند. قیمت موادی چون قیر، عایق‌ها، لوله‌های PVC، رنگ و تجهیزات گرمایشی هم رو به افزایش است.
🔹
در ژاپن، شرکت‌های ساختمانی از تأخیر در ۲۵ درصد پروژه‌های خود خبر می‌دهند، نبود حتی یک قطعه یا چسب خاص کافی‌ است تا کل یک پروژه عمرانی متوقف شود.
🔹
در هند، بزرگترین سازندگان املاک از افزایش ۵ درصدی هزینه‌های ساخت از ابتدای جنگ علیه ایران خبر داده‌اند.
🔹
در استرالیا، افزایش هزینه‌ها تا ۵۰ هزار دلارِ استرالیا به قیمت ساخت هر خانه جدید افزوده و تعهد دولت برای ساخت ۱.۲ میلیون مسکن تا سال ۲۰۲۹ را با خطر جدی روبرو کرده است.
🔹
در انگلیس، پیمانکاران با افزایش قیمت ۱۰ تا ۳۰ درصدی طی سه ماه آینده روبه‌رو هستند و کارشناسان نسبت به موج ورشکستگی شرکت‌های ساختمانی در سال آینده هشدار می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/652257" target="_blank">📅 12:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Eshghe Bi Karan</div>
  <div class="tg-doc-extra">Parvaz Homay</div>
</div>
<a href="https://t.me/akhbarefori/652256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرود رسمی تیم ملی فوتبال ایران برای جام جهانی با صدای پرواز همای منتشر شد.
در مراسم بدرقه تیم فوتبال ایران برای جام جهانی از قطعه موسیقی "عشق بی کران" با صدای پرواز همای  تولید مرکز هنری رسانه ای نهضت با مشارکت فدراسیون فوتبال برای نخستین بار در میدان انقلاب و حضور گسترده مردم رونمایی شد.
@Akhbarefori</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/akhbarefori/652256" target="_blank">📅 12:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
قوه قضاییه: توقیف کشتی‌های متخلف آمریکا طبق قوانین بین‌المللی است
🔹
سخنگوی قوه قضائیه با انتشار متنی در فضای مجازی به روند توقیف حقوقی و قضایی نفت کش های متخلف آمریکایی در آب های ساحلی متعلق به کشورمان پرداخت و در همین رابطه به راهزنی های دریایی ارتش تروریستی آمریکا و زیر پا نهادن همه قواعد حقوقی بین المللی در این دزدی ها اشاره کرد و نوشت: رئیس‌جمهور آمریکا صریحاً به دزدی دریایی اعتراف و حتی مباهات کرده است.
🔹
جهانگیر: توقیف کشتی های متخلف آمریکایی با حکم دادگاه صالحه و مستند به قوانین داخلی و بین المللی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/652255" target="_blank">📅 12:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652254">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
یارانه اردیبهشت دهک‌های یک تا ۳ واریز شد
🔹
سازمان هدفمندسازی یارانه‌ها: یارانه مرحله ۱۸۳ مربوط به اردیبهشت ماه سال جاری به مبلغ ۱۱۱ هزار و ۶۶۸ میلیارد ريال به‌حساب ۱۰ میلیون ۲۳۰ هزار و ۶۸۱ سرپرست خانوار دهک‌های اول تا سوم در سراسر کشور واریز شد و قابل برداشت است.
🔹
بر اساس دهک‌بندی اعلام شده از سوی وزارت تعاون، کار و رفاه اجتماعی ۲۷ میلیون و ۹۱۷ هزار و ۲۶۹ نفر در دهک‌های اول تا سوم قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/652254" target="_blank">📅 12:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOqu-vU2I0rht-dSUPVwKtoFriajVVEpnYsjdkhpeFTQOAvInd1dHfIP6fLYwnZsgQ6RbFJxTXAloQPq7lCsBEPiKhZdoPiVWrQeXRrDsky81IoFBJ3dis8pFZbuo5gsXrawyMN4BG317aFLJzty9cdwXD3DwzsIYnxrTTdQKfVDzoHfKKHLPHwFJ6idMoks577FF-QdKZE_ZGQSNUMVZ8DecnhGZVDGrFGlJPOtb2J67FjhyhUelDlSEvI2C91JT_ErYm4RlKSr_ivHegeyM1SXfiD7-iJfreLWkRvaIlzihgedsyB_-zgEQsy-C_XtAN_awOcP0q2w3F_1GkYP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF_KhMWCfBNkDIl2Y9FeuzS908Ddv5Flg5JPoymBT1YPPIxZzVbTnoLB654k20fs-fdzqb1LDo_nG7Y1Wt2IX04m-LzsOJMrWo_AayusfKAmP0U3V0urW58H9MRZeUDPll9BxPp48wHqwTh5JHEPKOPwWSuEcbmImWo2iVS0FIgG7phMqMfWvHe7QxtN5HcXjiRWmy1CD3X7eCrfoF_xkhU65GMISrKZ1Vdw0voyVdTVe8kbfu7149CIJMI6AgmH5Dhlu47Bd0opY9tcX_hAorAjtu89ojqkIytwb_ARc4RHny-2AcDbP9CcNxIZ_GX-XsWrOZv5ygFDZMt6utecyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6Ju-QBF9WOdnDQvDuTdc9bs46B-yrn-Qd454ni_va1GFV8uAxV1jB1HDpnHsmic520Eu4qoM5B-RSwCVT_bMNtPbJiIqPE2tfz-l7kc9pMkNQJ7ryJvHC_aeVK0nsKj0OoWnWFHt_zRDXgI0ylfyyqfKo2QZqvwz4hDX2CyGFJA3Vk0gef6YW0mHYoCUFxeIL4tU2s3SvPUyKZn6LIY5mFt_Rx7U1tHyWS73vxO302azF7XxcdaRAXVl4f_t98eVePgAWbe2pFZnwMJJDswDuu59h97uF8aHz0-4sm9N4hFXhbOkJqPM-f3EX2fBqvS8fKqMzrdi0XTtVkLhjNwsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید رئیس‌جمهور از آثار حملات و خسارات وارده به مجموعۀ ۱۲ هزار نفری آزادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/652251" target="_blank">📅 12:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTWz8GWcOkMKaD9lkyEDfXWcocTJE3ubIUVnHYuLcR2lbKb4PJQt8PcDXCxTuc7InFbTDlonlyduDe3xZy0zlKsLrnWaymqQgU9gJGhe6eyuQ7VLI0tvQGPuL-gbzKqyVrelAy5idVpg4kp3t2KOGuuc87pYZBiNe0PPJ3TzbLSPX4XGQNfpL2HrmiTmW4Y90YHfc20tIwIxcZqo-rh3RcDlIXbziScJMZN2KGY8hsAc0EEk545hKMji_HIy-6JcHsiro8iFI7mWbZD4L5gSv1CHk-i1kq4OhqPFaVtOn9RBy9m3pf4HHdt1-ugRI2e4flbqDjSTX_eTNsNotom74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله آمریکایی نیشن: بحران هرمز با تمام بحران‌های نفتی دیگر متفاوت است
🔹
اسرائیل و آمریکا با حمله به ایران، ثبات خلیج‌فارس و عرضه جهانی نفت و گاز طبیعی را برای آینده‌ای غیر قابل پیش‌بینی‌ برهم زده‌اند.
🔹
این جنگ غیرقانونی بحرانی بی‌سابقه را رقم زده است. در حال حاضر، بسته شدن تنگه هرمز، روزانه ۱۱ تا ۱۳ درصد از نفت بازار جهانی را حذف کرده و باعث جهش قیمت سوخت شده است.
🔹
کشورهایی نظیر فیلیپین و بنگلادش به خاطر اتمام ذخایر سوخت، وضعیت اضطراری ملی اعلام کرده و با تعطیلی نیروگاه‌ها و فلج شدن سیستم حمل‌ونقل روبرو شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/652250" target="_blank">📅 12:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
۱۵ شهید و زخمی در حمله اشغالگران به غزه؛ هشدار درباره بحران‌های آوارگان
🔹
منابع بهداشتی غزه اعلام کردند که روز چهارشنبه در نقض‌ مداوم توافق آتش‌بس در نوار غزه یک فلسطینی شهید و ۱۴ نفر دیگر زخمی شدند.
🔹
مقام سازمان جهانی بهداشت نیز تاکید کرد که آوارگان در چادرها در میان آوارها زندگی می‌کنند و برای تأمین ابتدایی‌ترین نیازهای اساسی خود به کمک‌های بشردوستانه وابسته هستند.
🔹
با وجود برقراری آتش‌بس، «حملات هوایی، توپخانه‌ای و تیراندازی همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/652249" target="_blank">📅 11:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b7048ea.mp4?token=UpDx-rOElOilR2QmTeowIa9OPIXADq7Aj00SGpYXTLzN5n9eb6RZyAaQzH4p5Oid33VoJcV8VOzplRw6oLh2uO-eaiP80iQAYryvhRplXJZzcFq-igB5253--QyYmLA_oE0FHslmHbfMl0U-fMxt0bDBBKL31-6wzPW_5XIbVwXAWQc1N7mQjDFFFdUxJsnPWTjukqpQcRF5ePFtgaGg18xhP6fDul9hYaDE2G0PhN7Mb-EHX92KmBhMt1JJT01KiBci4T1x4TMsaNBZ7kebfc3WwZepUbRnW1rfpYN3Q8lPXlUuQ4HsWBAYgdnKek6W7qJRxh2er9CK-GHxzmC-vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b7048ea.mp4?token=UpDx-rOElOilR2QmTeowIa9OPIXADq7Aj00SGpYXTLzN5n9eb6RZyAaQzH4p5Oid33VoJcV8VOzplRw6oLh2uO-eaiP80iQAYryvhRplXJZzcFq-igB5253--QyYmLA_oE0FHslmHbfMl0U-fMxt0bDBBKL31-6wzPW_5XIbVwXAWQc1N7mQjDFFFdUxJsnPWTjukqpQcRF5ePFtgaGg18xhP6fDul9hYaDE2G0PhN7Mb-EHX92KmBhMt1JJT01KiBci4T1x4TMsaNBZ7kebfc3WwZepUbRnW1rfpYN3Q8lPXlUuQ4HsWBAYgdnKek6W7qJRxh2er9CK-GHxzmC-vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: تاریخ نشان داده است که امپراتوری‌های رو به افول به هر چیزی چنگ می‌زنند
🔹
وزیر امور خارجه در نشست بریکس: کشورهای دنیا باید این تجاوز آشکار را محکوم کنند. کشور‌ من در یک سال، دو بار مورد تجاوز آمریکا و رژیم صهیونسیتی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/652248" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrpqvOn73WWlSZwU_mdVarzKKJkymb9tm_RYy1VpJhC83XE3apJjrEc8B1nY838UW498L5lJN_Bdfqz5YHNicrzvMsGrnGiG-Yzq0dTBfp7dJY3vRKyP6vGobOywJ1xMnnPtupJGWDpiVUNFT8TR8LgPLima8k5NXQs43VYkOvsdISM3v6wKF8_YWE4LDd6iPmlZVtjs9YcO-obG_yc9rOfQ3acUzJ0BCPMM_AC0Wws68VZMoDZo5mk_IG6y9Wph0LveX9NuskxMeWMRlTEeFsDB5BeCu6rJ8QMWzQgGDWL5o6PgP7Va9xGA9d3DknyOOCL010pZdzgEqpw7gQ4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جروزالم پست: حوثی‌ها [انصارالله] همچنان با استفاده از قطعات ایرانی جدید در موشک‌ها زرادخانه خود را توسعه می‌دهند
🔹
براساس گزارش مرکز تحقیقات تسلیحات درگیری (CAR) قطعات الکترونیکی به‌کار رفته در حملات اخیر در دو سال گذشته تولید شده‌ بودند؛ امری که نشان می‌دهد شبکه‌های تدارکاتی انتقال تجهیزات قوی و مداوم هستند و حوثی‌ها با سیستم‌های جدید تأمین می‌شوند.
🔹
موشک‌های ضدکشتی، زمین به هوا و بالستیک از جمله این سلاح‌ها هستند که نشان می‌دهد حوثی‌ها اکنون دارای طیف وسیعی از توانمندی‌های هجومی پیشرفته هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/652247" target="_blank">📅 11:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5cba69a2.mp4?token=g99VaY6HhlgwSZ5ZTXNuo-BwhCsVJdWN248Gw40hvARC9CZZYy4Rzvm_TGvZCTV6YfjyJEo_Fj-kJNMLENkJ5fHZoPONzWFrcaE-AA35UCcjNOZ24wy0FDxySoHYgNZN-7c8wrfhbH-1s-Rh4jWnwNs_tPpx7JMjYV6YIQGGJVMS-63GzH3JN3M5gjQTlAitLlWe9MWx73s_RS8Kwh71cVy2bK0q_CWSezbiW5TW7aApzEOcrCvsGEnTP6fUIL70tpAE504IJdPWT5gWbMwJwVPSj5yXlqMtEdX9mbpmfJ-fVapo7OLNs-INvf4inLkEfmUtAQeC8Cbd8VcKy2zMo4KXzCyqfx3INnRlLA6t0DoVcJdaOm7VUowEj8Hxiqm2Bl9gtbQMc74Eb8V60n--QX_9PqRalbYob5VEmLH6W2I_G0SxAEW58MvEpFO0fOO2JiXcdByx1C7hprqZeqzo3ovgSrMjXcjuiSjr0sOI8D800N8ayIM8i3G7R9-hJh72tTxOHPoog4tC7vdCh9aWovlQcBIgaKQivlasUlbk1C_1-aAaNlM85IxDcrdzfXJv8m8k0BHbL1cH0UhU4kNi2_RA2eOP91EhMyYUbXx9Q2FZAcF6ZRsvKc7IkdUhDwC6xuWHSRzNO7QcYCy2rA_xeZ96kFZY6NrvMbQAVWvVBHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5cba69a2.mp4?token=g99VaY6HhlgwSZ5ZTXNuo-BwhCsVJdWN248Gw40hvARC9CZZYy4Rzvm_TGvZCTV6YfjyJEo_Fj-kJNMLENkJ5fHZoPONzWFrcaE-AA35UCcjNOZ24wy0FDxySoHYgNZN-7c8wrfhbH-1s-Rh4jWnwNs_tPpx7JMjYV6YIQGGJVMS-63GzH3JN3M5gjQTlAitLlWe9MWx73s_RS8Kwh71cVy2bK0q_CWSezbiW5TW7aApzEOcrCvsGEnTP6fUIL70tpAE504IJdPWT5gWbMwJwVPSj5yXlqMtEdX9mbpmfJ-fVapo7OLNs-INvf4inLkEfmUtAQeC8Cbd8VcKy2zMo4KXzCyqfx3INnRlLA6t0DoVcJdaOm7VUowEj8Hxiqm2Bl9gtbQMc74Eb8V60n--QX_9PqRalbYob5VEmLH6W2I_G0SxAEW58MvEpFO0fOO2JiXcdByx1C7hprqZeqzo3ovgSrMjXcjuiSjr0sOI8D800N8ayIM8i3G7R9-hJh72tTxOHPoog4tC7vdCh9aWovlQcBIgaKQivlasUlbk1C_1-aAaNlM85IxDcrdzfXJv8m8k0BHbL1cH0UhU4kNi2_RA2eOP91EhMyYUbXx9Q2FZAcF6ZRsvKc7IkdUhDwC6xuWHSRzNO7QcYCy2rA_xeZ96kFZY6NrvMbQAVWvVBHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منوچهر متکی: آمریکا دو جنگ را باخت و سومی را هم قطعا می‌بازد/ گزینه ای جز مذاکره برای خاتمه جنگ ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/652246" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXh5hyqE4GZfcFbvf_RWyeif8yIplm-TLR8UqvP26yxGEFyFk6hy-pzvzD2jyTQBJJZ5qI3--m0PxLOxAdZ0l3N0Jp9Z9TnjmELOx3v4P7rhQr-DcfchC83xUiPt2KM2mJ8DhkblhILtrta-ZeBluArv9aYxzDNtaNd0UGIh9PRO6gkxERKrz2NXsYRnjzWABI6DMO1WsJUoJqI3EmStqW0hMbQQs4cPeZzAo-sEnSEKw6cUC6obsO0nxLJK32MfY68jPGOCcR7tOQQpInSGyCFE-NMZvnA4mGmQzQmLkZccS0v7RxUUhzzmGYMIDrspHGhao0qY2qrNMB1JxAVJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دریادار سیاری: آمریکا در جنگ با ایران شکست خواهد خورد
🔹
آمریکا در جنگ با ایران به خاطر رشادت و ایستادگی غیورمردان نیروهای مسلح و پشتیبانی ملت همیشه در صحنه، با تمام تجهیزات و توانمندی پوشالی دفاعی‌اش شکست خواهد خورد و این در تاریخ ماندگار خواهد شد.
🔹
حضور مردم در تشییع جنازه شهدای ناو دنا، بسیار حماسی بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/652245" target="_blank">📅 11:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQzC-iszURC1BkCHPka4q553NqdI8D-1S8AlCT3Uhof5ThPJaAmDua3pYlJwACwljWrkCxUvNTvQNdttaIF4ySCJpyedA5Pt8qUMShemqF9mqc5Uaa4RKZA7ZiSlUVhm8juzHT4O56jKRJm2XFvPpKRRM222XnFeOEby5GlqVk_1J_zBjy8xptbh3zxbPApFbzkS11G0qaQeUKO0DrDB-WZoGRmOyG9q0LIDgeWRU4ZO1oioqvHtu-rRjW-M88SnEn9DES7vXRno-m95FFqtZS3VfiuUHY9G3U_vpLJxYrzqAi2x-iJMn6UGG4S5SD7ylK4hHSqWTmLzbLmAHcfgSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع یک حادثه دریایی در نزدیکی فجیره امارات
🔹
منابع رسانه‌ی از وقوع یک حادثه دریایی و وقوع انفجار در پی حمله پهپادی به یک کشتی در سواحل فجیره امارات خبر دادند اما چیزی نگذشت که مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی درباره یک حادثه در ۳۸ مایل دریایی شمال‌شرقی فجیره دریافت کرده است.
🔹
این سازمان ادعا کرد که این کشتی هنگامی که در حال پهلو گرفتن در الفجیره بود، مورد تصرف قرار گرفت و هم اکنون در حال حرکت به سمت آب‌های منطقه‌ای ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/652244" target="_blank">📅 11:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baacdf786a.mp4?token=pvXHj8WSPaWW5dvy9edyqeij3gVEBVmaJVKGh9BqKxR7tER4ZKXsMuDFVeYMUwrWve7TothoQuiSxfvN17cI0gIgPqPtaSFVHobVzHr3FAD0ZkwO5pub2ijSZ17ipyB9xKvHtADmbvhNWKCfj7EIvQaYJR6iRk8p3OflTlgfr-3JYlf0qPblUV0vJZkqpdyTqfvXwnDAYs1iXeO2j7NPDSY3PaZfuby-em7YoJoGps_cRR7VamCKu75gI6nNDUM3H2pRec0JSBVvZAsuEr5ByTv5rc-teA5BmG1nAKl2nSy4rx9pCoJnpWZc9Ky63JPd27Rlw3AjJVn6pgiy6HHxlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baacdf786a.mp4?token=pvXHj8WSPaWW5dvy9edyqeij3gVEBVmaJVKGh9BqKxR7tER4ZKXsMuDFVeYMUwrWve7TothoQuiSxfvN17cI0gIgPqPtaSFVHobVzHr3FAD0ZkwO5pub2ijSZ17ipyB9xKvHtADmbvhNWKCfj7EIvQaYJR6iRk8p3OflTlgfr-3JYlf0qPblUV0vJZkqpdyTqfvXwnDAYs1iXeO2j7NPDSY3PaZfuby-em7YoJoGps_cRR7VamCKu75gI6nNDUM3H2pRec0JSBVvZAsuEr5ByTv5rc-teA5BmG1nAKl2nSy4rx9pCoJnpWZc9Ky63JPd27Rlw3AjJVn6pgiy6HHxlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جعفر دهقان: بمباران مدرسۀ میناب توسط آمریکا قطعا عمدی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/akhbarefori/652243" target="_blank">📅 11:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy8OOefFItz3wtQcesVn--6Ij34Y7r-H7ktZrS5Eg1dbvlLZDSmmnYx2CClYMDCOJc9rj8QzVDyWlrLkvVfs7Jhz-wNmaLdWGEJyAs0dZmw0IJN1ZnqP6wW070zCad5apP9x419URni7RLAbr3qnKPOeteWtQR6hS5RAgXRvBITXbEnY-OC-YWWErjrKVr30WCXUES0oJDDVBobdpfNqte5fTKQf5AvHwWjRIBLhlsrC9a7jeHvFRIBSShX_E2i43Dnw5dYNH9Z1h8oMoftjZ20qQYLmdFVXasS9efe95dUlnz55Mn-Gv2UZptfN7X3mkCtMWwhgRabCoh7wtlvLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شتاب عجیب اسرائیل برای بلعیدن جنوب سوریه
🔹
بیش از ۴۰ حمله در کمتر از یک ماه و افزایش پایگاه‌های نظامی اسرائیل به عدد ۱۰ در جنوب سوریه، در کنار نفوذ نرم میان دروزی‌ها، حاکی از شتاب عجیب اسرائیل برای بلعیدن جنوب سوریه و ریشه دوانیدن در آن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/652242" target="_blank">📅 10:58 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
