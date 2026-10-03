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
<img src="https://cdn4.telesco.pe/file/fDcIIlcOab5g3512_KLNS0qchWs8SSE5xGuTnmYY6mvtVilMJp7xklCm7i_NZ1gDE1djy_na9LWf1x3VQg-yz8ZEzWBalTIOM5J8dDxHwQ004OePXvaGfvj0hOf_F_-JA9vQhO5xWkB3JdW_7u7F4QZRHIzD-b9aZZjZsZdV_LqZ9GyAcDbxGK3xFoTgete6Ekayl_n1a49hvY8mGEJSpsCmjFpdxWOyxPpYQfIyvuS2tfjcRxvZipAl4p-OpOjF7aDVvuKRLaNbvJRNXbCUWf72m5AXbFrCyfCeidbPu4O4sXHo1_tONTRk_BIal7RVk5nrjA0VtXVG6RIEIiA_cA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOagb_vLCD5vpB4SSRC_OiX4I8w4iTtrOBGQiGkByFRt0PFvbT-m-FzLdiJVh2xGSJM6SOorhWG5oW2roF59GNf7p4XYO05bhNn_up_kadv9jKu4unMttJICdF0Jwn_xyFT5rSY_EkD77CLKOHrOSb5bJctKe_txZ2q1bwpWG8ZTJDZFe7EwYlcjPnFOvAH30lYdsdE1O0RG30Pdj6d899i0HRdeL9_xWrKaQqzCbi3yLNtFdqRoqeYqvtRke3o77cWr5sbtvF4mvqVPR8_0d0ANUWGtmX3PDMS-1QlT1FpHq5ILPTpVJMCnsT-LoNiSRPka0e0YHbDWWH-RlXUSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By_mwIKZaErkyMbaLhDbfIUboxJa1JABxg65vS3m25bRyz6ahKF4PpcA73mvLTGEJ7fI1W2Wls6n-5UfjUCHQjZWOmdYnYMcmi_Xahm3xUXaJdQPyAbkQtdAc4CPt53cz4xvAo00YtdY3Kb8eFYNJ-hRgfLnCD-_ZOYewMcr3J8sLBjsi3nCuzx2bx-7NxRlhgiheWkDxni_BhsfYGfi6p8s_zf8jqK46wzSxVDe7LzjUYJYG02_iRaJ4UDZ96DfmfgXpbxSyIRmbTCYmHFzCKD_K1a438_kXqvAqJEa8dE7L82QsvzOBiXxDAFSCw2jYj_sWoqyLe7WH6f1OrlrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raZv00khQQ8-Icw1KDxvCo2vTva60AwnI9WB5Ar9mN8DzwpmPo_p0wxf8MvR4pH9Eo5sz1hmqCngM47udaSDXN1fLnUyb7A_4RZR0w6Vbst2caMS3LCQyMpSAObDJbE0-evVPkhiBb331-hczgoqe7s0iRzOjVjXDeibq61h5w4KdtVGnp65lwOrtLTCNuriUg-8C93uijHA9pJw8l1S3iUATCI5cCEuF5HQn7I_C4MU_dKJVO9nLC6yHqKQCLp6C_qhfxoeYDD9bEvRV1xh57IUvU1KvHy45QQzSUFUr6YGmEW3MKiEC9gnzQkAlNqzcHJIUmSSQNm6eOR9z1pjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB2QqxVFB7RMLmVskE5jhQ5FEF4ZVeQ-E-U0RXSlEyD7QG2AliE6Fs94Mx-HcoD52oBQrIrDK6J90KPlQPDqhDE1gB2sXTSSIJm0FjQRiDc1v3NpcRflj6s3xq8HcWhJP2k-bZXvSfw-pXo8T269JWxKYw9ZvTq0VutQnBiSTnqwE0Kda8DrA2qNGUNB3lKuCIiJr_GzCAikdx2CNoEeDhML2ZMkq2XoV1dNA-6upxxZu_nsRRtpQzP4Gy5y8TXpjxE6eOdynWlD0lCCa4j2mIm09RBNf3qGLw2EobHawTajpcbchxR45PI9hf90L67w27wuOYfwdYIkogjX75PWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXMPSZGepz6F3Ekm8ZfJq9pKDX0UJsCHl8f3b8MfI_dFoPH53w8QQfYZMSpOsyJWGdExUKlr_HmWsy3i4rs5i52CcXax9fqAzYMOQncoBm03n-EajHpQwyhaLPwEWWMyeOUv7uKEH1t4nyMp01QDhncgieV3tYlFElVXDyWfqrbT-PGqtxOUNqMd9BoLeR1-3KUhFweds0SIJZ_UGBFcBxMFKUm6qxrqT0W3nrfL6FTwY7LUPRV-tdcTVl9j5vB1zXJfyJ_VseX_k7ZlKGWs7c-DNavqH8-W5Z6dY-YcGBjwZaTTzro5EsNDQkqFnkLCcNcW_S7_kF_c08WWaOK47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0VnIvpoWs_cIKD6ZXexvK7gkGCD0pmVYnL5p9Cqww8RSxob79E3LCdPdWXXDW177jZCBakymM3CLbyeX25dXbn8foMUrBG74gppeq4ox-GiG4_2ZFY_1Ko9keoMqOmy7v-xIsN3lkW2iscILnfS11NE-mCZOCoAH7BWMzO73ODyH8u7lhXZq-s4EaovgBOctXmeE-YdOrlbM3_hYGxXI92giYn4zUJ62Yp_lmF3eZAutE5905U3h0ORjdXCeDmHQ3FlZkL3Kya0vQQKaTHyqlMZ0H7L19JjkRju1c1dOBatmDh9w_0o_set8n43S00HrcdHUl2EuGDCdRYFRLyIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2DDCa3BFHiLJp7i1iLc-sYgfwrB1F2jlreAD8z4mtThafjfpBXMFFnk-5JZJpkjV16cEPRh1a-O9bD123yE_tne7auOxty7Q2HfyeLAfFLN0xkcvglG5ns8A1gK0JfP_GNhq_kyIAng_6eBCTPT7_PnrKTYicyIteUhUjbvihUbzNXzAHOC-qkr5Qm8_eRIpR-Rf8Rw8sDsqudyLoGQ2wb1zFcONHkCqq2J4QmjkSbYWMu_qu6mDkf1TA9yHvKyzmFcJdHVx_y_74gZgZfVEu-PuYg0rS_dnHQv1Nwegp-tN1lfqCgSEKyNsHTJogrAAwZWwy1GWJKxBWLm9sbO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwLJxcm71aHILOg6B6GkhUJ4MnphiNq2i3M6tYv53eXBP4JPp0DCZDEspaNOr5vVCMlw6Y9uVpaHrsN4FrEsaadBZ1fRKWfDt-sCUdgViKxNduiqsGF2rU8Zwe5oZJxncQRd00C-PK1p7QLohCUeXNwqqdH2Ss25kuMQQBBEoVSbWmAkG35d2i45-hYdxlXSU_nv2ru1kbVt8JUr7rzGJC4EmEp9878eLmyS9sStDxCzQQXUUizbYMeUR4Todw1jFiu-5nxEGJMdJpWO7PF4vElZx3Owi0NKeLyJysuiYrK-IfJ3kcOjEz2c4nExXmt2blfDqg3yMeAaLcqQ69d86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOc5wI09gBF2309NB1g3OQ0y3ZR9qf-PwiISwzVtlOVUTR_VgXv7vKXVqhNWXRriQ0dINMldkIFaZr6qTx1WzW5Vq0PqJ4bOzepN5iILI2IsZjK_rglkTTi0yN_b7WxhGHpwhycUoun8mqJ5UxOqrcYfD1KDtszeuU83VJoRRup9jDFxVT178Pq7WpqCEyCTVWCT5w_wJ6c-raELOzEN7Ua5VakFa_VgdCDpFZSBYhIWWoHOd5kndm_ObnfYcWUL1iS3Y_cE_DWC2JAaugi5svZI1es6yeBdkdQsbh5YaWY8BP520rjzpAmZGNJ9JSxkikUIpz83A9oy3nckyIHUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCHpw1esN9NyTbcsWq63vnuh0RhVeQGFTFOsF8Wgb_r1zCKGO-eFRXA6ZUIIxYF7KFHRLHJMmCC7VguUh_vu4oYsLPu_WErs6eLZQdOKumYRXZqyF88iwSMfo-7xYJd1pq1t1ZI4kyry7eDeNXfebz-_2P4SgHKy7mLwTABVkBaRgLqGQxkHhyP01afeSZfYaeXb8lmikgk5b5pWFpC9ZbOVbM65888YT0KL3bJDvwOIpAkkAxHMQva3NS__zAx71ghoKjCWpB2ouS-9J3h1uI0uAxqKxbKxVX4RBuZz6KTi47Nv6cheZgfhp5OHIBU016SGqNa-w8wGP0FTpEL49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2avPMb21Tx_9c55zHs2cjnbDqKKCp3DXBHSRx-CaTndCKXG67cBNAR1Q6yNkp5jD6-_xFTGwFqv-ARFdC8RzvBdFcVXDaslkk7nldNogOaKizsfS8ToTJU6DxGKT-mv_v2SuE_0N_ugBTdbfaDfurU8-RIrpQmeIrYI7iHEX66chRC3lmKXEFNe91o_JwJqSAoxapcLQ_FpSNJTtZwLY87vS80uM1ybI75wWxQBMBXsfDEZ00B63LVMfTrWQtJDv9RPrUwDBhtPSjscJIn_LXFx9skGpO49hZUCEpfyR3z1dj2wzRlzj4upUW-XdgN1M7impCXItLi48kpMYIoB1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIVaYpAnRpWADoFQ8DcdIjcID0Z64OJtrYuu7luH0eTMUKUAlNwYGwPLD4QB4xPjqo2qzUG7vnyZR9B-3Lcx6nnH7iHYdEVMKmP6irSObG0QWs1Ov-Owa9_cO8zYGbNXCKfDlgIJtYicm5ipNKTzotylJIDxAieRrszEC0pBHnyxgEeJekmg5_FP4Y5SHQNY2QS9k3ISMPMBWxUb8EJMZeQaaGBB_ylUXjUQ9Bz1wTpcSiVFGleD2wkDIDKb0e62NC46Zf26szW4uve4Ir64rWh56387nMxqvLKjY0L7ziWMXRoPRTfP7bZnHE9Q_DWZ2at0z_Aa5Q1dTpTe5roNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6mJmOvYnixfHrlGaqWWyrgsgnErJ2Tiv_WTroB5Z76VYuNND7irlDpqEDKx13NKOS9n4lepseU5G17J6T10RG6Sc8yOw9es0LuHw6Y9KPkW5TcEJREkMF4Y6pDegGEUyWAEP44R-P9G6BbW97vgDQosTsIStJWi-tquX3kG0-XyIB-XEEmZ1bEZ646uvUH29vn8xYvP-G0geO8g1JhHr34atx42nrLCtzXhjsNKffTfQosP4xtgmlQ5c0tH1akTOjiFkX4h33h1eW2bI3YoeA3Y4AYiaPwcA78KGiD2JKmoQjuxBtzX9RRuU1xI6b_8AUk663Fw2jPskUHGNpdGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUtI-Xgh0nP4F4UJsBirDhmDDtdFcFm2yqOYx3e2LCI9LgC_lNm2lL6YpXuJdxRG8IqJkGOji5Zyp4oOQEc8L4jUYI4Lq1WGX6foEWHYT0NQOlLWa-Fckyny3zrjjUHod9Gt-A4Ii2xIqwBeGBJ-UKcU-lC_i3GWTjnC-Qzmi-YD4bDinD1ljqO4vC3N5JCVTNSjh8Eyf2ml48EpZjR94qqEeIKZsJI6endUMNR5uYfQytPPpiuE-QGSnkngrx8-Ug5EOoUUBGtAjB-1igd-QQFEmTbdg5VMjRNuBBz5_u9YMMueSOwTAjBQtslxgQzNwT0ujGy8qk7NXzKnJbfiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG7xYeI3wU0cYU_qfa9O7Qrzr-LD62sK8UIYW-qly_hrXbaCBjsxSZHJZhGLiEmyj-ksUmrkEe8uV78kpK5f6HUbW3asLbZkCgKzFl9jEFs6CPEuRBbwp44xmIJqys7ycQc4T6HHxDOljR4zeR2a40VrUiGldQxBZQGHmCxl5o6LoCq8XS4vckIY5OxC0fSX2y-MuR6pXFRzjoIcyBCjDDNbDJbC13j5pBMl_QsyUcJZoVzMAVc_twpZ2B1tXH8gycl95FLvFpdMOmaXKkiq78B-_dsuBF416xenud98APJ9N31fde6W6ALlfRCaTgcWSM6PGil48_t49Z5SlsNdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy8HfUaak22zOKDZhlLYQNYyhXIWFoAUunDhc61UUu3QoTNi-Swu5z_C_rocO9h_UwFyyiHfJToxl8IX944WxQ_04zrbhQgS0BfcezJ6i46Evf8fpnIE-bUadTOP5GbC-NeF8FSR7lBgZi4c-n5h0CNFcVxuuqSMNqoQBYb_dXDdJOA2yLUzsRjNVkiZ8ug81ZucvBcsRGsVHflmzN888x9UjuoxwmG1YjEAnZ3IqPQDOyk9ctoex8mfrZP8jU7Y2tJiQsC_SkQvhglMLuXYsEJApUYxeNpUSf0YvNZTA3LMqVIzxlIH2hcFMeW5oSI365vlWBoi0ZA-7H0xICRO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cW5269eIeyp39dzsMMSO92oFn6Qlc1DpFkSJg-EGpVEsca9NYQbm_T6krDFh805IwmdtbRc_b9M8ylo4sIpL0NdLcWKv8PZTITZ_DbzL0GhVIROfsDb9JM4B9NpBXGcosXk4RopO_U0kM6Y-Grc3VupLu15jzYYMXtxwPUHL6dmw3gLr3CzQCwE5hluSzdeiaGXLBJQVPPNSEbHUZelWdl-Rn69K1QKmkt_SUi6a97AfSbPHE7OsxBSCjEGWOdmTOSPnv-lwyGsal0oyMLJWIgJgP0qVloAfSZTHtbsSUS4zQoKoytPUnqpUjRg0euSTzf7HPPMefTIj4LupcgefqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEoFwhNzRSqvBCutpPzazAK9nR9kvyCJ2Ba4JzhH7bpPOiTmfOQnmj6ihg1aXeJQaEQZh6xRqHenIn241K48avmuWXuxZkOAuQNOl-Boff3lIxgEz7JdLmXWfEAGmXqIWIc160dTlhZcNdGXbuWYgnQGd9lcwIZqaFLGxMb9zGdGP1FVBktYBoS2NTm_HTw-hzNo7zGiGTiDtZhEyuAu0JCWeqCJRGzAZabJfX-hV7oxPmJkR7GNZSMU0XfpRjIZVUYoWNc-p272Bsyu6wQHNZPwesamL2K9fs1GF2-YB7_B8pw0GUxY0CvsM4jBGLOx1A-fTokeRTURjo9K1oP3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1nQDmmNzL4_4rI4uKNu4SFEzk11CbczZAAK0ah7IrvN60E4pFyFomtYlymVx-ER8azvKwXorIs5BAHCuiJ6YKh8lseDfmXPieaGBn-MvQbXEiOUqbLIpX77JO5MUKBwQBdQSZmcwU4p3_hAnXMGrSArJA_syLl1UevGnNsC9h7sdm4JmCwntFtt7MTHiX9i2CCfVH02aq1hwUwophJoMd8Bvs_los6QBw2WjuhiYqBBVm6I2xfZzJBeBl60iXBhFDi8pr8rBU3skF_cCJkFTwHimwoffGQOmTnFPsBsu-63tglZvkvW6jgt6AoOuxYBO6c4WQzhLFZyeJXsJu9sMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmLCXq5dAZRaih6Z7djP9OZv6EHeqvqrhnE6RuBT-Nq_cbXYaMYYhB7ChxJKzzIXHgbhiBnGcA9_Pw7MqoHk4ny7X_-aOinjd2pWcZzgIpECpA6TIoN18wk2xztnQRH4cVo5NVmwk-hlswUf6-Gjve4oP7uRxi_LNb4YB0ahXba-G46zGb7Zv2dxb1BdReRuv1W__tX0I_VqD5T_rl7YE7rki51BLc9UXiX13DG_xeiFF6JWlqXPJjFscV7ZLfD6Z5Z2N3ywvSug4gAwPEE74336CPMC5B5U_D_VSrbiq3864oaFNOlNE1XKKU9xBOVFr9tvmVviB_FELb9rGVZRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKzNfShrXVqlXe5ZhoX9pdrwyExrgZFAuL9YKFeLnFf3w5nvmP25ejheLAnp6oq8LIGSp83TCzo_tMnQ5JAVLRf18VKpHvmiineoEw__iUg5xT3Q1i9Fn4xnMsDTw5wy6AAUFDPq2qNMmZJ_A3QN9V59O8Zy71-9vnAUfzZp9LBSNUaeudRyGAHkrDMLWQD_aMOWCr5WAhUyQnid3JX99gpnOmFzj_91hjggDmCFWTDbBGmoNDRthRScfE3HwXYF8rl4cwuaavzTWptAl7IK1f_asousJzZFv-8kOI4SumW19aCJvdiO4lq2cbO_k6vmHz3QZdU4I2ibiKC7eiS0nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JggMcnr0OdRp3rdq36ZsFrxtIYQQsgcVnl3SsuXl2HMDS6rchWA17AyLeQ4SFh-kUzaA1hYqCqxM2iblMuQGq6M5eadMJp7t-Dt0iCGGqQa_uELu7ml1WFX_EhYGCst7U2oMCFTMQIh3pBwe9_err09jmf2Q6ON2EC3t4iCZohbNdFYSjxH6qahjOYmzbw1gtUGj7TFxMSA3ODz59BWwBxy-AW9TsY-aNIlHNIP1p56cuwE_dWHItyDKt_sXIB0cGSdcX3E2ma43FQ3UBm4UOl6-Puw6bgbaoNTi4-sUvj64Jer1Q3ur5svQxeeY15k9vUMRUxCRTbmSlvS7lujzzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjCFroEmuqbnIlumUPwvX71jUXaLJkBnU0fH3kViBx84dWS5O06RqrNoBdozsw22IzRPZ4KZpXv9cilQj_wJbRqc1D0yRuzwOsw8zf7g_EP2mEae6Nq6lnP9rZe73Mv9SSexM1k3ejN5ITFLUTGuVp7SEhJhbHnve_TYPhXve25fmVaVw9LaGyl-CEkL5X5u5fwSCynaiy7_gS2_wT5gFEyXi9vkYiZ3s2y_8mlIj34CpoWmzW0Bn2IcHRbs_v0_6h2Ndci6X-SonFrkv6un7epIysmGbZ8fprAGBYVuVBFtdcl0qi1ehzGPcoXIwTze2Kraf58WO0O1512J11DXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgPgLeYC7ZTg0-lD2FQrwYrIfuqrJtqdznHcuwaDUQdIeVe4QsPVbL_Yc4bTd4bR0MsBdCI-tgkw4jrGB9bP0JvOAJdhPDtLx8Pam--J3GYvxBZzyg0Kz4oi-hIp3fMJT2V02sGD3KIlNHb_PqRPRebhIgQRpC2WMBAQt6s70pJDHRUV-J62pddUSDFfTSXfc-qLXeqnlMU7p9cq4EtPbjLgADVNd4BPAVKh6ZaPQfUO0PvdJC7bTICJyIaogZ7FM5KWJSro8eTGRum6UTf6QSKqtePRGg_Q_wL13oxB01OeZ-KK77AHLRIyXf4UrboHKpSdFngkGsz5aiAPj8-1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wrx1qiiRDJh73Vmj58s2eySvgTJO1sB-R939zmxH6eUW3AwRGa129adf47Av0vKPEG3w6D8YK3jaVpKaW5hiu7e6KCkgVg2OgziPMPs5PYb6MKZsjFC7egg4rzMZ88KP0XjNm_1nC7kGeIEqKUo8u8cQOYtcJHAstF6E0JTAnaw1hDJjnXZG_VsJMfTccuJ64daeJ9cwhxroFaOF3n8wMeufHqfc8k-TE897kDLkJ3JHGc1c8TDa37VXmg0kSwV3PxIq97VxPdpHiMdQvjAExr_4ht514Z4kijOiKe2iP6xdEmif4OksNX6WvQqpYh5GiZH8Zi26A4md4YslVtEnrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmpQs5r3QUkc8X8ZuxHp1f-OWkUlz8ZtZ35UpbJCFzbZwrNgD51DfIychB5VKlNeDel7xPPpP8vkqnSm-D2OAsOrTpqzu-101USbYd0SiYkt1eKLdhIIddt23q_xhWZ4uQKpOu00LzxJLxCjIVI95UvNLFGF6d-MfUrIHhkc3C54RlbBQ2av51M9eL2DtNUMPitLoS0SC_A0qH3G6QywR2pR2ipQZBQITWGK5HO6iAgw35ThobeYpHOs7Uj0EaWaXB3G8dOK1LLRBmtWUiit3FE9Zr1sM4s3vl1JWvi6KwdNS6BtOPZQHh4nLoa5Meq88OQ914htMKU8LKfrrYNOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufpOt0d8LVcuYFNp9lTWSa9cQAzuV0SwSDggeo0UpjsIT_qEVNKRQj-0-MG48gyx4-HDzG87WKJcaGO4nrH5z3k0IIvg6XxbIuftBL-fKOJdazaomvNTO6jdSX4vSNfNna25ElyTJvkwjU5bH5HicCu7p18bbFAJku5tDTofjVY7SOn3sOKdaIN147wFS5UNPXgXwn12bFntRmCajjEM7rxO4lj1lwGKv7N9zC6xj4lcqn5HxEQ5IP4kpy5813cqSKpqJixKztPlYJQOYqi_swn1Tv-_8S_SOSnEm9ZHxhU7kHKgSRpYWttPKYFNWg6GDzdRjlY1io37gm5sCQA4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjCjDy5FGo4D91bL_sPl7VRh95a0TbSdCNMS6Hiv0Jq2Q06tJbBJIXfVLEpM1mxSBGzsgHGp4g3zRVzrES7-yfi2Q8swVqVX-lztLplMR1ZjCbq0JxVKyrfhGPMiM3O5f9NKBI_aa9gs58TynSecfCOgBC7RwU4lA56aI1oPoqlwBgv8NZJJBlEEicONi54oK65aWARMhMqq7vB_eVjXS1cDNXgU-Fms1UjQkTlrrUUvb2LRdo_ehTZRa-2V7MLmNTfhVnQLbyfhAZWtGTtrvssuRL6moEZeRDqGk1W3AQNSN5knMUth--0Ly0fbdI0eMrbmHzKaWSkCM_qFInM-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-7RRTGR0hn8oeCeFtmu6i0Mm1NArdmpVq2SfUpL3eQ_vDIy5zU3CE81zWf2xcLBw6lSWyxZtjCgTzoiKe1tjJMWEgC9LTMXWoB4LLTx1knbmtF8CUmVWDxhXNV7ZCKt8Mkjb6fmBxHmhkIWaD-3Asmzy939kZ3m0GCOwxv0KYBkyTuNYcHpUUxzvoEUi9gniUH6spDJBUr5QYRwuUq8emMfip7dsmyF1umw8QVTfwmiytCaxCmWTjAlgp8JPFNVrxXMsgMWkvPm9at0uA4G9yfi73h7wJ7B9cl1uI5b6iD7EslFz-LJTH0Ipp9Km89NV2rxqgMtvbmVSr4HuSlTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oym90AcDyKmX00T9ViO2XKYaOm22P2t2RytsZpzV4O6CZY2J64Uh-8cesxLN4rb7Zg_jzNxU-N-Afsu1uMS26eALReNZy4hWAyutyyYRrUfbK6bOG4JejaCyP_WhBVqU4ByjamvKWuxqAgKkou7BJnMXsDKta3O70fQAU2L8DjpZdr_WYCWJPkPNZHJXTTxnd7-45O-WdE2ZEtlcxA7BGLBPEHlW56dFdSCdvxxW-NSCVzquogQu0RAKO3Csrb1T1g6jGzYJWr0p0DoMvvqEYZOQTtQeCFmQu3ADzTqejMiX0Hy2irjcUvltfgC6hceFOmB9D4kC7FZMNMTxGOD4bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7Z-FdkLfqoOpafmKLycHcX4P9L8DffQNOR0dIlkLkjGSqz5gQM0FnYtJOykIsltJRYcMQfJpWY9cV4tV_9g2WIdDxM0mRbxhLIDAjJKU7Yi_FYCA5aeYaLeJK1jtBUzM9ryMP5JGsE43ve-0GBr08ifoeXt3U4qYtTXNmOwz3jkqt0d3TajsvNjjbGBR4npA-C_9pe9Mpkw0altuEtPExe09FCbCW1hz00AiuUHgkL1ZsSD8GjmaIQg2VjMC3QB2nxSARjzytE_S70kJgFTXcmf1G_aiE61QiShkCN4gjwH4QRrxiEpb8uPs4Jq9lsjolTbbjBgakm1g1qdrn79hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMWdGRzrZ2rpoaP5m6r86TuZp5OqRZWuz7Md9hWkv23RHl9YLWQ_xP3_bukdncf9sHYBSvDk2fx5pSBSmqNeUyqwVC8dls4bha43SDlbR6nvloLTAvrzk1FmoK3Puklx-2sPPVh1-RjkBKeU8zjKJW6pIaPuYpO5vHizg5egD962YY2QXQNvCVaXYt7mo9nbn_Pu6dIRLqkSgzG03HgVBPMBnJnu5U5R14iCAw7dTDFRDAVpA2aRPr7_cz8B5x7LwUunY-GL98iqicOA-EmOx-h1lTgBzLAdo3rGxamimlABiXVI1hFg8tWCNAeAjla-eQCoAyj_kLBz1DLaeC1PGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBX83h2HqlnTf48baZK51FNutZJBp_NXwZrA8OlZAYGERDEeV-ClNuTKZw_7JvPARRluqsKPIrgbAPC1Mp8NiD1z4O8pLP9iL2qMU29-M9s09pWxiwuJx28g5kII9A0vBnpIcoaD9HaNNGiFtas3HeNx1BbLvl4njsu2d7YNOj2Cj3EAdZnbx6-Ue4YpHoV3_EOpTdeZJIhhBF5CXaG6eUro4eILGRfY8idMC_TvjDoazxRsQ1UpHZsAppmCG8np4vEAWhTj9vqxH6JqZhgupnVIzW_sdhblFcXlvNEVZUHcnPm3oDKWa_NrCFhdjwI6H2WF7yetRqsuq74BspNbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhcyv6__WpqkQHKHLTZGDaTQXwtB5M7QJ3bYG0MZlau38tta77TaOPbTCskHhRSUV6GJxvag31Q6uyGkqtn8Hny7oJPofS3zuvGJQm-SxF52o5Am3xKzyWroO6Z1vlvbBeT4PTtuzExP3LDjBLlKCziQVpaJVEtJgI-2GXuUQkLKt6ELNxdDQnG7pZxkFKAHz3V21PX7DL6c8hIOky7qKpBf2jH7vpc8cuN-FKT9Clxv-5897NtzKkHF_q_oBTM9vRjelav-m1T0ub0w7TrxEOSYuPgr8-vU4ZPSzMbRJTv5lNSYqhukAYOD6ILzk-3fC-ChV_g0WxIFTflulp7psg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM9R37zZXnV2OUcS9ZBV_KJqqTcKn3kQQmrjoc6lYG3Ygiq9TVbA_Gw6uoei6WppYfDA-NHej0SrZ81UWq2GvTXfXPzH0UEuyI1p00u-2zUOoOadw0kcMvLYyf9ERO6tpjYpm-piqJ18K78bMQqiVwCzLUzMSBr8uLrlMNExt47TVRZk1RIr6oNAyCmpC8xofwx5LcVX_q6d6tHDY5otQvBJAIo9_Yu3so-AB-vGxDM7Y9O5Rgk23ff-xPLY2NGTC_36R2U1fDFwimH9Sm47L0zpoC7WFURuq_ZfFkz2tc1kv7eHBPXN9ele1QfhKZsSTqsQY-55Ti1cvNSvV4p5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4niew2Nt7G9wPnAZNnEmwN7_UKu0uwPnITF5moRLYVEv0GZ4aCrWJUWKJ8hUfVZ7Wol6xp5ukk_3XiR1XSA28A4gG2g0oE3E1HpBvNc1Y-71F4elgcPRku1a6NQ2K46xj8OQHCaZq9bu3noLLzfWYR0ywq58H8kAVlsxQLOk2dswSBMyCp2U-XJ0rt9MY8ssLUYGP4F-uaOLkw7gB-dBHdZPc0Pcy0IU_4VoewSnYQXpfKkF62GH0jvo7wooNoUnAJL7jc_KCd9g3do7Vew-VJf-LkWRtKq0L5a4TddFjMt71TRH8lVwK64B8BXPSK1ptdveiHYvns9U5YUm3lNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=DkQfg2nOva6MZ37Gp9sepWyshgC6xI190dDoKZzYjEkEceD6erUECKf58_Hv3Kab6W-8b-TnkJNbE-CsRn8eY9R2fj4rBEOcWJOKQmyvKf5NFrONDk7ZOZb3LIAL3pEBdEqE4hQLRK5_8Vni_K8uuXSmraVl4Ho9tNDR255QjD2bOBFbRxEAdIlLsgvIo4wjXcGWn4lRCbSCYXptV4pA1tucJ9fuUIzbjXxzFrCt9iofLp_UZpQ0uA8Mgd6kw2lT1CtDDOmcw7rivQyUYvoD-WZDBp1-hniU0rfgU0viBY84D-BRxeCmLdGsMhMKdPV3Qo9rugghKg8ILYNPfcv_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=DkQfg2nOva6MZ37Gp9sepWyshgC6xI190dDoKZzYjEkEceD6erUECKf58_Hv3Kab6W-8b-TnkJNbE-CsRn8eY9R2fj4rBEOcWJOKQmyvKf5NFrONDk7ZOZb3LIAL3pEBdEqE4hQLRK5_8Vni_K8uuXSmraVl4Ho9tNDR255QjD2bOBFbRxEAdIlLsgvIo4wjXcGWn4lRCbSCYXptV4pA1tucJ9fuUIzbjXxzFrCt9iofLp_UZpQ0uA8Mgd6kw2lT1CtDDOmcw7rivQyUYvoD-WZDBp1-hniU0rfgU0viBY84D-BRxeCmLdGsMhMKdPV3Qo9rugghKg8ILYNPfcv_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay7ICpD-v076eE3ycR_4Za8qyLnGNgtC6eAA0eyNtFn_TpTa5HY0FkvhOK5UUJojXchU7M276q1ABwwdcZpxFkzEE43XVm3d3T0t5Q8KWAUp2j6Or-d29RD8TjbMz5XIGQzV3psx1DZYnSc4aMutNZlVEgbb94Ul0lE9xPYhqpSpEW7SzEwR-binye74Ul4S8d3774oOYRa2Zb5WGed4YGsmpSJSxxyACIV2ZcPtzI-9Aeoz5C__eqRYLD8EKeo5hdg9Ev4rmND7PozBqXopG276r8VLGcWdXVWulWJTLo7E7uAWzK5O-ioyNihSTuXoPeZPHatarZDWlo16F8zrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4BS5wQx-C-VocrP0xGe5kpeuByct6VMATNUHcEhtyon5JzqIBaGlY1b5iY_sPevM3DxoRohDHUeoqDVy9vbSP6Vm3jlvw_5hu1K8P1118GAT0XpPXksi3DQZVp9c5NHxOgm_LGhGpOFsLd-6MgJALQ2szrMA1NesF5NfdjygQ7gZ8eiIkMNg5QKfzfIR161C_0H8Y4OAUQ4qm7GZ-jt63D9aYAnHReiSLW-Su62e4INgEgdD_MUdFWSTH7aJNsYwnxXp5F4ESiQf7H68bc4G96Ql5mWzYtwiNf3_nX7XsnS38SqTW0DxA5kPxWjzgqjoNNyoTpsRantoTKv-ZMYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1_TqCRaDw0riPS7RbYTkkQWrZ6eniBN8J81mUPSrhPs0fTelDbzbyQDPF7wiz3ZvY-FZUENPhhmBxd1zKTpXRCIv355Idk6dZcpid0xG4J_gUsrkahdh8j3rMD1YpG-75qcH9QtPqSdzKE9HqEZGAyKNfLJeh3wFIzvnHM7C8-2hMdHg8Eobo5ayVOGongODhJx7xfZQQZnSlZpXXghvCApPFz_QWl5zFeiqSxrUe0M0K-xbIIBiZzqicGjiuR1bz1wCCbYzVD6kBt2Fs9gp0STM-1IXNPWK2mPXUZFTKCoBUFQB6dz_VT4PRGPRimcqy5NjBAOcKFvly12ymDcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXLSc12aoOHT8BFdjEpvnKMfhlfJhraxxHEsXpB0XRWuaCm8RBtmXcVnLgy6Jwz6o6C9JPfxUpZPpJzRypMNZuQ99zT3sKmyPkO1hwYBNj8S0LRBfCXbKiX_SQN5ZX1LqqDQ0EtfRKWIAB9gc8rHIyt8pFP9f_wT4HJ4ZL5X9gyuVLLrqUmxttOc59DOu8-wHW6rxmVqgPS--8AgA2JWwUWuMZfvyagXR_04xn7n2TQ6Y0Pabkb9QECJm2_aOXZdGPnYEFVvjxGF8UmAXU7HUJnzUDehZKwF_5LTfoTButQn3XyNpHO4sKZyiQ92L8wem5nKV2zC5JvkcaB4iyE-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmVWolW2T0fsTdlW2QKYOIX8H4rMwzzMOnT_WbfGRUnry1hvCWHlNyX8pHYxiEgPw90Uam8DPU3OaFjKS_HsTl-vYGSqEnGEri8PtipwmehhiSWiPpPoGq0SM-oDevRqrwF6l5ii4wIxbs8mHttVru15XY8nMbjcAjUENwUOBvFdNC11kjQNgI24J9Av8VN3S4F_oFWGn812_CNm6NJFGMTqKp0gWYHF-rTCKrhmiB9gFEBEJft9WrIUK9mWAk_5nd-xP6B9IkeBtTYCv6iOVfdM3jRmk1GnCOfZ7udKsg65ivZQB65_QeW5KB8EJ5f7DWj49sAUDFmadUs5iTDrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz8lFg6S_uEPbT1t5R6UsolFBAhKsh9lpwVmmprh_92WHpLj443W8kR1KkzgRQPKSpfKB5PKaVtxm7mGLtNTRlk3P9LjIR9Fx1tSoW1UUtYfcCLtmr74KVCJ1ILAphi8iELq1h7vC3WoSguxEiQr5z95mSBstpolbgGnXe-KS54g2vBaq63DzatU3HGrnuLnfKtT-onVQLLJBdKo-3ns9_OPyhQNS15uBN0oOLV49iALWKBE7IU_McuTpcEGlQEP6xJI6ZgoezirwqiLLRpLZTNaY9CKwn64cTMSczIwH2N8Qk52V-utl-Icj__ixys5jtwRzW8lJubhn7qo0-lFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omh4IG2PNzsnmrSkQPkKC0XjHwMkomqocs0vIkZ8GJiEBUYGdtkYceQRYFhx7GK1H5SEf8J2GTlQCF_kk86q_OHetNTMOStgDGeJhhBhb0BWDbxSVsaUNxW8IZ3qz5JoOkDvU4eMNbK6Tbx430JI4Ko1roKwC1pSoLFEl7m_mkdzAlJSzsfvrAjD_3kn-ykhH3WhXJj8A5BT1ejqZChNGAM_IXvqdAxRSZUtdjFq_AYfP2NqVZP87QdLMFORCuUE4c4R6LU0VqV00DKQwrohDXkqvx7HZ1mM5d9GNBy3OMoUHhXzlBi0D41LH-284bobV7KQutkMWurJZ_e4F3JorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCD6YASkS2IB1tMN9ZACnjAU9a54pcw9wriqcTPtd4RWVIwJVpUD-EH3y73LvYCwBG5vj3ytwoI7c4BJWos_QbjirQz_cNQIAHqUA6637mzCdlIdNtUhEcPNbMn1QWomQ27NKvICpdPJwezV5NYVGIT0oVroi7LESZQ4KjZCyscEhnVQQ6i37YwGXfpdPJnPn-qiqEEYvv0hFbV3GCmiTPK6-1HfrCQt0BysyKc11zegrW-W17vMRB6qSEZkQkUedsAz662apFydzNfbzTleryuLCrxg44vK1BU8OgwZPfhH2MqID_F-P2ZUufsesidsp-xAOzDpcbX86gLcnkbXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrmFncAO-iAvTYGNkSfWIcdwNQn1i5SNcPNSHVKx15LArURXdFdv33R1yYLKhNKr2CIOFzOvlyhKZbbJeWDtvj7ez33VHLgOzfONaVB1yR0z6HPMxCcRlau1uvCRkAarlYGmW1PIspKZ7NmYZ2OxrZ-bwIiKiSJc2YmIK8h9FKEOY3kykO0wETbliT6aXn7Cck7AaAlpwMPdyaxrBpsDq-QV8dAaGC8shUY2PmCNRSZ7-1WJGIlVzKZWjcXXyMhjgeI7AyUSFz_R3R3QMy4tKgdiIUelbELlheyGHB2Q223g0Wzp3hyjPf_-jQaGSPkgVhjzy7v0QtBp6zGNPLcA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTr570VYR0GqGI1Li_c7hB6SQ9Pkd7Yj-DS3TxoB_ZPN_xW6txFkdgrdMOAdwlpg1GZKHzhoEMD4kuPvbR05wTMiJpSTE-YOzMKzL80WdI_j49epOpsLeMsxlPTj2YpgtNb2oQAJEW0sntg74_lCIpGjNROsvU8NKbJxpYPAs-3uRQtEk9-kg1BNyS7ggQgOn5NzaCG1p9_Lf7m6vqGbQuW89mSaIuZ6Mo7uIvzHIVAQvQko2Tq6oA9L3jWwq-ppdyt-OweaT0ZP2stdiqnQoFhl91yKiM0hl_FaEuqWA0FGvkHjar4fgNLp898QY-Yu6dMhuS1MJvmRDq8spIjw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwIBpcue6_BhIxd-6eP899SP4X9xh6QEkE3z9jSQWKJK8SFd9rPTrNgLqdyuw28tMYbYIhyoHMeV-7OV92imYwv9WDbMa2rRkGFeS9dF3WOQfjC9zHRMvD2hJ8Fn4p_CSosZcU72dRpdDyaDkFRpblG9ErqAJT4T_5rdvYwWoM6Yn2PWg30Qw7c0FSLzFBFw6zrpvpDdsPThm5sOeHkq6fa5t7d7vajL8XPDoUzAoSDyMc1h0c62rxyIKO5mWT4zITbeUMTEFR7q2bJ6vlDF0LfAhZnYmi98VrbqrlfFOU_-luyRNmEr5I58djmL8PoiFlphlwL79pC_G1XTbTkt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg6cTAGsd6FPnAE2nNA3AiI1Y4c_kArWkB6ZhUg0_L5ADHBlOQxIiieINkJl2GnNiwiSUuVCYzFllXaDL13Llt1jtXGnj5pm1pwEH793hEm-NtRqjwdehtABl_piZskWS4I9KUbiWNkn9u4Dp0_W81QZ31TS5rDaSMCo7IIr-7rle8Y6mfupfAeGPvWXHkR9EHJv8QqYrlOqMj3sHyN0OR5apZ4EPNF6BHdLiV1J5-CMQeotPfHGQx10LLyNO64-lKXiB9V4DQJwpW3kla9rA1k_iGL92_PCPdHXRHOvHCldaELSaDk4NTdTcjrYuyioZV20ZeWz3A_M33Q9MKe8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-D5HX9RAZ9QWtIkbGrpb0hmLLsaHV16L-p50cI61nwHcrbZT7y2TsTuKsC7BKBKGGd8V4cMqG-6wxZ8IWJTuv065R9Twyy6T_U4andU6-MybySXAnd3DGJmWPEcih5OjSRfK_Ae662WxjJOioxYH9xklAE52hesf98wf-ENqXJz3iOTTl4M1KVXkGzT3gjv6lMadHKnT1GABzmo-t_Ok6iDfAzvDwuxOQNkQoh5w_hfykrkbBuqPsPEW0-Eti3rxHyxT3-52s-htUw60xV_P14OxZXWfp8u5KHZdGr-zVGz7TByJDujM4tRYyP1xUZE0IwRcSA5Q2n-9zsyHZIPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sis4DFqOPHfghBoMJEggAjy2_m1zcXAjATYmq3XsnahiqsCKyz-TtkmlYG2hRIRerJS_0pkc4_oN5kbfnh5NkE9qwewOsq8G8x5VxMNVP8yXvLh9o2RCQ3sEBEvdC1AAS3fOINFNcp_6VmaBXkUAc5-BmDD5DJLyo1zgLdG3mZQxa0P8Jjr5VIfrr5XvW4INlVQXMFyu40kbUgz-CVjriiQ64ffwnhvWrxYVpKJq-TcqHC1a3TtXNp4BSxKP_LxzSQ8iPaP1Z_PhMS5eKrpZlda8va3JYPmojhESc_W1D3LC-PlvE-nXSb5oWvyWEZR_n5TdyTLp3-w0NrEa8OZrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDk_7DhhF4BJZv0k6U1S4U1gGbt_Ak1Dg0QehAEtt4p5C79MeNASOdD_y9PBo7mBM74s9gwrfXlV0GcWv1Fx_cigVXZ4RX7eWEreG3S4VZYTLVadPtaO8owt2EiuduPQtEmav2HL4IY7KXGCPzfZv3A-JsOVizDMfDsxue7fm_CQ8R-PuDmCWQKPRvJyrdskXPYJ6nLNZe4_PwfqmvYVokmhLCEG_RXU4wx-rivyDCoqJm-TB1gx_ytB68GUW0ZHDfHo5EepeXTDOa2zI7ogaKy0PJdVQCbsmeNNKMhso06-P8TUOuGiJK9iUnhZz-RGw1sO00wiCbpUooNI0WBeOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi0BErC6aRO38MmAur_k2tKC29__BrDA7kWMD0ixzBBXos8XnQE2qJnHpWVI8N0ZZ4ATJsyY7JqIe7Eu5lRvMUn8M0JR4quMyBpw2XaHAknw5fLLzuII6N3pMIQLKu9dEJYb1G3ZUSa5GJu10sHQuKD-FqkpbKCrXQr6jS3SXonyqRkJaLw62iTbTYr0z4XL__TF_TZA46N2Vkm8zNia7DZ8IAzUys6apsKZpW_BOAkVRJK5FAMKug_AtUg50Iqqo1TarHJATctCYeY4NYz6TK-BLLtch4y4-PC92SHArWOqKJo7Sh38I01-dC6GfeZM3OXzucUyYSacobwKtoSFqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwQyn5frrT5h-i83-YyD2UFaSZrio6RO_kdZ62XUdQKsM9uOJkDQ_r6mlNkg65BOXi0Ngu40RsxxrH-HNp9AzNEoCP3LPIIqSDrme_5wc5CTDjbWcSgmsF86gVnI_-oet7X81waA2n-5bC368LJd6KCMw3Jf7WI5t2ZN3XDjulR9GdAAVvqGTMtgLLetjwQEGA7GzCwfe8Q52G8QuVNfdyxtUcNK_40FhfKWv1JVXpdFrGglvYhMpqRBQ2Ou2DK-uODTiRJ_GQPFAOkHID5r5K8Btom5GNNaF3sATdhgDSjpCKOXjgk9NcXQqPFTxhEWD9GvLbY-xAqXmUSDr0PvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_mAEnKQjmD1_xEVY30IlLqsaAvaoxTyrguGLKKaArUIKhFOnLniOYQ9GJVecU791pdU8d-SYOz-gqFG4RDDxirFAbN3Thm3h7R0XgTATiEr5n10ij2fQmIiKCFLpZws-FAeeaAY4x6OfAFaLgBS9SWcK5myzWp9oO4S9BB3tFxJd-yloyn5IKDAWL4sfx41_1dXYY7jAk1SHTgOyL17e5AOspgOC8MXjBhSXBKRpDJJEBlCe01UtSqfPgmO4etLmd_WGTLmqwqDeoFCBlykRsY5EG8sJ5AlLcZsnQeYxv_qUizdezjZFOqRkyr4SZ_Hyri6yA7JjUpI3ZLfw8O1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJui2CHV4Ttgie_ob6kGy8aNtpFQuYaMLXsEdcosZyItSk3nx_FxYDwEhmQ28ezOh1Lu_-bJ6CwrBoak8GS3JXszq1TKQ318qtYWVkZi2yctpWP1gVpnl2H4u_qxuOT_QouiVEz291lZZ7S9d221-TOLTnMuuP8Iz0GHJB_UKtt-2Eq9a6thEhBoMnLCoeqiG4F20kC-n5CRKuVdGbe05fd1rYOUVcJreFgfV4AZR-87z_ANTPvn4kHROzUcnlYd0o0gQzxI9IJHyXKw9gKU0t5ZireWLR7zcSUrfDVq1MMZpJa2D_ybuPHM_OG68n_7NXP0fLmrXNDIeDNeRG0v-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dKaAzGJGlxkgW5w5V5ItukF71qKYWH9Ukj47L0rXpPnde8KetmP9BLgKJ0VhnbWhyTncNuUS-__vV3z6kEPQWd8gPjJBukiAa_DV-ED2af5indPZXvVbYQDtRGvRi4q1FdgT0HcMr8hyfy1_5SpuR9b07eDXXLUsZS1agRKDzYzshhcyU9iIhL4B41Lx95ByS7-ZD3WVvlb8Hi8SURyJiXevHvj_hEM9gGKe4WGN2uwUS2iLotK1ZyUzFrEINuvdzH7EFXKqvUqOaq_j953bbWkmdMrmcpoXfxE3zKl0qz16MlhMYt9CsI060VuACpTiT7Gn2RrHo_nSrpgKqSm_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdyhrQpVqT0E3PtVZlAL2v1meBJG_LvU-tg3nFECc1dM7cI1p2H_vwqZcqfnfR-vgdc-h8mg6yBc2ZbqbpmQqA0Hrved9hnhXNYJ7sk4ZL2tpSlb_cBLA5VcE1CkIzOMrI1a9CH1Mw62WbO3I7kiOa861VJII1vapytZyR2ke2n7coVASt5ib4biRpX4DAhF2Ls02G6jqoJjKo7RKwvRyUAcfdfkgixSb4D00AA7klL5_9eyFYQNyYDdumHefotpob2fqvAYfqi7_XbxdvnpHSbSFhQxFAe0s4AQ0x6knO6mvz8_SnTiqas69ulZanUxI7Fk2z3UTsziLyyu2jZGJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=LRgS3VTNeIfTUMZ3uBfS0noTj7L6N1Wf3h593F1V67-Bx9nKykltFQhyngjgA5enlOWWLiOqYsIIoH-nfP9HH79N_ln1YwsqzNQn9kv9tikh52qJHI0RGomBFrK2X4OiMhFwF7qCQp7ozr9OCGOvE_XM4h69jd-Dd9sHWPjlJb6Jv_fX--kOcXCUHMkjIt-1PCn2hjGUBjhExdfzWIC_q7ZvK0TXgsu3w_oUlSU7SLIUD1vX6JKr6CsitaRojDj3I8jRE2xYWvUfG05T-V5fZVFQdm0uS1ombMBnXtrmaeSZBIttnpKo9oaNWnKs4C1vjfLBIBSVOOJ-IxO7jygxpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=LRgS3VTNeIfTUMZ3uBfS0noTj7L6N1Wf3h593F1V67-Bx9nKykltFQhyngjgA5enlOWWLiOqYsIIoH-nfP9HH79N_ln1YwsqzNQn9kv9tikh52qJHI0RGomBFrK2X4OiMhFwF7qCQp7ozr9OCGOvE_XM4h69jd-Dd9sHWPjlJb6Jv_fX--kOcXCUHMkjIt-1PCn2hjGUBjhExdfzWIC_q7ZvK0TXgsu3w_oUlSU7SLIUD1vX6JKr6CsitaRojDj3I8jRE2xYWvUfG05T-V5fZVFQdm0uS1ombMBnXtrmaeSZBIttnpKo9oaNWnKs4C1vjfLBIBSVOOJ-IxO7jygxpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0xijuGNlxMbrsS1WLKfLLnCoLHp2wbil121tMnvznWelOmWiiT1_XSacm3JeNRTj1PItq5A9szTZmX2_ZhbqfOyn1e429sXdXcKKUEKyExsYiyFYo5YxtzNgT3SxoaWzJOk_Ll60L71Z1NQI7_NZYPYSqM-WCSMHZKRkNB8KFDi2ZTpOsLgeHuw4eMWGwSxngSJm3jHFakAvuiwYVQeElz9-ot54k5x4RVuBbPjzuHe0xysEcEiHIGd6z31whvqKfZFoSkun2lR4UZI1IRPvDzYK2uaXGhlR4an9cix--xzJ0KTtpzVxgt9Tw1STOxu5sw1cdk5NlXG1ZKOUmGKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d92sleZrJZr-MptDoA7ZaRv3hSgwopyNgxFPbtdTaq7Pv7YbNEWWjBoCYZf-1J-tT91RgkuUq-a31BSRa-BZfhQ4_-1DWfHgeDQ3eOlPcrK4zmE-_9Jbs3g_GNM6hdVNG0c_3Xe94yJ1KQ0b_o0vcAWUPLMw7eeRLSi5OJxDvImiLS0zwW_aQHJjtr1yEMSto6V94m7rrYBMcOCg1-rr_zuJRU163dNet14sumoDo7XCi63q_1M1GK_NjOJ1qtgoNfZHW6bQghBqeyRq9XSjQ_9_rYh0OJmgWnr2L2pKlEJ1EXHD42UbYmifcNy_CWDGGXbAPclvNErgo_RQnSEs7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH4CCJojeAXmkwaAJczZwDtu86EH4C1u3kyq0SUO8FvDs_CMln707UidpyqbY5ABZDV-hxdAfqer_CKneg03luEs-5ESprPXzvdSDdirgymWScDJ0wopgLwQx4wd_udDiQGWmq58WmV4tTlm6qo3hnfu-YuuF3vgI2V-IKWl8ZonWriw005gfICzBA7mDJHtzXhm-_mkA9puxJe9d7QJGrz5Vcj_xuP2aJshxF4iJiv-F8vi5Cr007lxKaTSCc_QigZLMpMZMfijRcuscw3GAL1PHqg_i4Cj8lQJp01aCPbZZiLCm-g12pBsEBs7PifG9CPQD7yiUvy2okUIUWAB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=gKEeczKcDayyKvau6tdoSGTs3OFnfMb1cScMrsnN3Q_QttmMuX0AXVch0YX6pikGvFGQ0v95Sr9kWzBOWLnPJxXMyMFerml9ueTIUWS5qrGU2_GC2KOrA6fP1X7EoyW0Hvu9YEen5Z2DArxbEy-DcI0b7h89OCND13DRt9qjbTW22YCngtRLD20tW0m9ZIymJ3tWktX10AcdcFLJy9pUoSSZ-SQux6NIqEt6LRA-81frhwdmab49FejWMLKIzVr9Mkm0fPN6kogQBgyH-wQF__mPDnyXkg4bYdrLop7eEvyNo08B6Ssi7o8KiUHJ0D2x5FqLMhlv-AJxvzJ1x4XG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=gKEeczKcDayyKvau6tdoSGTs3OFnfMb1cScMrsnN3Q_QttmMuX0AXVch0YX6pikGvFGQ0v95Sr9kWzBOWLnPJxXMyMFerml9ueTIUWS5qrGU2_GC2KOrA6fP1X7EoyW0Hvu9YEen5Z2DArxbEy-DcI0b7h89OCND13DRt9qjbTW22YCngtRLD20tW0m9ZIymJ3tWktX10AcdcFLJy9pUoSSZ-SQux6NIqEt6LRA-81frhwdmab49FejWMLKIzVr9Mkm0fPN6kogQBgyH-wQF__mPDnyXkg4bYdrLop7eEvyNo08B6Ssi7o8KiUHJ0D2x5FqLMhlv-AJxvzJ1x4XG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goJ3qRnLFDimG0F7NHddkcwXq8MdxN_CvBd7lZTfRlKmM28FBxNybgebw-4oayLwBTD4ngZv5pVKEcbUmy6v45PR-11ymLhXIiTeujXCHbKFT9EUDNzDWPP3coFoo-wR457yw6CmXfntMC94GIiZcTJ5E5sCnQxmF4yhIvxvMf5WtZF_jRqz3-xjh6tje86ygcYsF3td8XW3D2SCnhwIuDlKLco59P8bvNVyWLavQzzy0fo_fKaPsHbpEYtNP-RS3sJiKH0OUf_zvmZau6MmGIF5JVj4N7tDigyf1rWVtSTjNIZq0P2XHZnNM3PvklDIxHQg4WRcNTXKPWzAJT0UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE29vCvbbpEMbcUGWskaJP1w6xDtmci55fhy_DSgoHzdb1mAZAgb0qTRQ47ubZieVdlErc6xeGAjyHfx5L5zjMv-qz9QdQ6j7vtkU2AmOd8QgxtI_RK4MuegJV6jns6cwiCoOdoiT6TMdwcVQicgAVryOXAlRZLpI7nDJOZlU5BaW04TflBvj45WJu12J27wWGyrngRaQvb7SFDwPlhBGkf2yZ_pz5naGnzExgYV_PVEKSC-C8KvaE4rG3qmpwu-BSUlCkDjSv4qEZgxCh-ip-TeuJNGj_BYqOGKANmi3R6ZqbDt_eKlIXjldp6rMWjsor9Qhvp_OfpHy4VvKBK2iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFisPf2WjiMfUI_KfjBlDppo7YWJzhem-enUuJZzdjymDiApMpeXWNV79eb3lRldbSnMtLF2zYb6m2QbQZ-OQ1C2A3qKAowDYMYfFGTPku6rGNsnUJbmILfxGmo9HrJPyJ-gfOE3dq4BDR829W-nkYvDvLlXo5LMt5nyg2PGDM8EsWZ-eXRPhPv2ZCx94DuRPMiz0YNWg0dIRI7jb3hRtAdCnWFazT9QuGlGQAI6utEa3TjZVksZkQBJUugFgoY3mQZGVqrGsjlP0ST8wpz1j---8C10h-B2p3aE8PapMoabmYG5vJEcG3dCE8U7wyPCXN2cuJGPcC0wVtPNluRNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvcF6HIhMXGI3k1_aRRfTaVyxAnGrpZIvQDoIj0zOz4tQvLjXROsMiEmaKv7RH9_E7-hCrGjtbmulN4IfIeupJGGLX1PkKw1RuKU37_48_FeGNuGAozPHaNtGoZuChN0gl44Ongqf39idSOxidbxnLDOdp-EJYT5plkYLruFMndhFD-KRDzeLwXGCc4OQPhFfiSKqYBM5Y-fPIjoinQNnEAMpI8oLO0Sz_KzfG2ijsj5c7P99Bi1tWt7v7iuwKaJp3cPdYPt9a_3A8dyalgLIQRkqg-Ba21FI-3tvrkWr02KpZwMkgfZNx0Blz7pdpIT29hHLqHtgd69VlCNBdRLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpT_uHR5pCgfca_c7uigBqPpMNs94JiKL01Aeb8-td0JN1H0qOu1s2igYtz6FE57ypL6n9tHyBLmv_y5w9Ow4lHDxEqLU1oPhWuKn6epx8XZzZdVVfhIP_Y6eRjCsJXYAarz86jQ7v43guz9sT8vqsWrRyNJeujyHeiQH8f6MltoMuPFGm2FJgu3vlpIb1tM3bjUeDvKiNtlmtYQdBvowN-Af8BnnW5dPw3Vf91oP22J2AWXxnsyc5xk_CqbLv4PdQYTc902lyfhp2B5_hXN7iOHVNL-h9Zb0jfMjw1-cj-flKUI9_zsHleJTl4IYMEfTz-wVuN5aNGRJ9qhp7LPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBM8F37tn5m8UBhCPNMb0K5Pe35Bpn4iXfOLKf6EeybVSmpQnXRK0QOEt2jqg1T6I958ulLxwzVXDVzjxEDDWjLrUQfLne8nVuFb9eRL8e5gZo3DFOubFot6AbWayjGRIiV0bCZ58izxedOt2UJSi45i_roPjh5gbcPUBbRwFSnAqdkHZEVTNuPdDU2lU72QSVvgSXsVgPJYr6a3Q75n1njmOGFtPf9ryelYYHs_zEzZZZkpGCYwcgOXjNoCHuXp3nJ3JKo9g7HbkzJeNC82HKce0IcwyU-4Ngz-AIefyO-ebtzjg-CF3wvw-tJA9wvFUEroloRC4Cs5dYdaNHr7tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYQmbs3DKe7Jeh4YMc5S-MnWUU_dzWNQlKRLOCe0Mni9XHPegXe_8jSTPHc5ekBCu_Z5hgSxglejVj7V3yvwtIf5hQF61hm-PJBEiZOCh3Uqalv_o-RlafVNDgX3UZeKaTEeQ_2mNUSvmDscN8CIhqo0U9wnrM1CiiMSb9OnfNeZ05R3CcfQPScQK3G-n54BKJU_jp8YtrvxAmTZax5VwmD_1R3me6azA6WvwkxEn-OIjYw1tRVf9HM0N372jXTZvSWMuELABesENcXMOwLifg2owN9j_oT_AKvydA2PzynCjwVqPj2kzhIF-pJ-5M1tJwUEPi0ZZnHe6E4zA8srXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=RpZih1ZYAsswoS2yr5MlILCNQ6ltinYy1DcBs7Ys4kRLuNdlRnAucvp2lz1BnMNUc-VTLoUW1lyOYtm0g9Vh0mzT_Y-xvkLvnFeqCO7TUg7X_R6avAYPHDT7UtHZGBYWWIrrpAbq8Jps_Ga3Bb0Ilw_4uAnCF5tSAJAA6ojcXTRqW3kkYaBJOFLYupQwHbjdIsYfwRfnoEJ6XOLGck-O4BUIumhuWdpFfOaPTIcp8GQRDMqJsNQxCgw-4m9OltXjXOJM9xca4QT1eY5hb390zIAZ-MxLD6cgvrZw05o_9ax-UyEixDYa3oD7bKiedAXfAY-_jK6X5l4-Pu6YlLZoKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=RpZih1ZYAsswoS2yr5MlILCNQ6ltinYy1DcBs7Ys4kRLuNdlRnAucvp2lz1BnMNUc-VTLoUW1lyOYtm0g9Vh0mzT_Y-xvkLvnFeqCO7TUg7X_R6avAYPHDT7UtHZGBYWWIrrpAbq8Jps_Ga3Bb0Ilw_4uAnCF5tSAJAA6ojcXTRqW3kkYaBJOFLYupQwHbjdIsYfwRfnoEJ6XOLGck-O4BUIumhuWdpFfOaPTIcp8GQRDMqJsNQxCgw-4m9OltXjXOJM9xca4QT1eY5hb390zIAZ-MxLD6cgvrZw05o_9ax-UyEixDYa3oD7bKiedAXfAY-_jK6X5l4-Pu6YlLZoKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZErgaTT_rVHk2qPyifx42l66546Zf5lRPUUpli0iAnmehCBxuGw97MLAnHsoMquBFAIpElmYZKBHYoXCJa5UnjTbtTGp3vlgyUf0D2cqEs72i23DX2JsQ6ZMlYEO7FFhhHpbVHskxdMhVNpJLIu_A2vNMT4FxDo0ftEBvmNIHry7CXUy4ceRwHhafnD2FsyMqMAAVYYHQJotPbMdcucx6-gwambgaV3NmkEte2ucDdi87nrLcAhjjlRjEEltkld5kn0E6h3fdzqcXQbeBFTIm7Prd7oZqPb8hJMqGocDj4LopFqZT4EqTceJzRUURa5FdRRV18OIoe5u_L61p_4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLr3gFPn2tKHiYAlSrjyM25aaOUSAZ-qLB7qBBO8yPwJVRddfsP03du-_cw5mBK0q-m7DsNGGX40dEwoVdL1YfEkb-I-eTXdfsqtrdiE-xIWU_Q4aQbFzB_8ClM1cB7vcDF0hWlWK1nmH6udlQI7HzWSZnMKIFIAzA2bQkWU0ppfK48R0l4js2UjEYNFep-5SljJC3CF1aPtD2keM7NozpPhjf6BLXeoNz3NZhob_vv77NiBBHT1mhxFjPHKF2VC8bbtvGmFEUwzCocqc8OLxzQCJ31sY4bBUk2na8_UVwYjO8DBvThik9ekhMmPIw1C8tMtp7z-h6QE1dIduVpxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNBiM6yJzMvvxJ7V75DuGsso4EhWyTHG89_YOizQQxE-cS7VVfDC7x36wrMNg21rqZB-hXCM67Wo_0C1mmxOpeN8qOm7UHsp8WxvGB3-1U1Q2MVckoUD2C64yomirOZgiS3uJj9BomW5JYYGtb8XaxkIWc4VIGSsealMYxLJ6WfA6rVaSDR9uT37i2eE3oh-wG6MJJkmcU1adD9nBP43pBxksleLmnrsuSV6H06PMdS-TzxlFVfZTaMsehwLGvhGa4zeY7mMTHmuUd0ZOxsXk-7sHxPlKcd2FUPLOjXhtN2BdXVCGZmL0LnVG6Osx8R3ZfmtK23lEGwY2BdUKnFb8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYwV7gScXNxAvszMbkrePzf7upB8dbarTG9f6mFGyh-1m1x9G9w-4QI7efwdomAmoK5w214un3ld9IuubQNg2RwE82ORIL6lRSdiN36dWQeSmpERz2Hvk8JZK-pqwkfKjOz7t9776FPLx0X1_lvs1Zai1QPDPn-jRK6qVc1N3hwUp1l-WLH1FK0HXuTtHimJ8XbgPc6TDBqqraHxbypUswste5Bql0XFQ7C34NiKPavwyk9oLJK9kAOXfHVXav0ST9AVE9CRFItHNFqD-3_ryojAZrQHaYITSRQLtvz4Z0lJ2CFMwb_jxOb8VQmSaN2YnO2ppE0_awjpJm3OnKLJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cShckGlsfsceTWFEQJla-5wH4XtN-RAyyhrFnf3DXIqvy8-GZXpf0I-pgPnhecDpQ5n_sh29R3-ro-EYzrcRRj8pRKitX6C9CAAJ72EptPf2TQs_EWe7Dye63BI9CvUQy_CwMPA0lAkKAKyB_k_XxLWJNoY-8aBfPKx9NG3DG1G_S993r_8AiNWlek0xsUCYQfdXw0dYXEGX9GK4gEcp7-9oYyjg9qmsdqwSW3hsrp9GL-IcJu9lTKwrkQZJOW65ftXl-y4VvHc809wIbrhYycqWuzoRDXvVAryde8PLvQucjWE6nEbf6VJ7GvCJ5gRvxWR-O6XJZmeMp0LDTE3KLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6feE7N4DE4Dw7AakUeYBOGM2ns3NsXSgxlcMgiRtK1MAL4C0WxitQkiGO6KaZPUAG17emoInoBpVop3gV_4J-OhG-Ps8fKuN8Znik4qLSMLW9YLC2UVaFfnw-jFFkDETSpdjHjo4dHCndOLH7mL-wHY-bNMYjdEfI0iK07YP0nUkdE_YIrAQUMwLtITPaM52zBzoMJO36YGk3DFHUQavVaZfAAFDHkEI533QqBqv_ri8B5WvmajJjHauDiZaQdBCaCPKxYgMoEVv99vlOcEDoHDcL4nvLdHVIo7zRQD6DiT-G0R3Uwv3B6deZ-0S68-IBjHxJUU4DMdwKwCeZYV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7ZJJ9TvldakVFDaIPDdo-IxsRk6pC5A7cQ7Sfja7KCgFKbTh53gKD7KBgxGPvmoszO0QT95L87TG-sG0uy6Es-4yT3jOcZ4-hRXBab8sTTpOsOMqhCeazHs1772BRpo7I--DORyBPrBglUiYTGM7SLIO6sZnr-lb8_hHsisDd4J8xWWY-KTL25NcTLJAoPcLMwGn8grGGQ61LGlqlbIOaTsxJtNtzJOr9Ebbi1KOSWt-ygdI_TInBuomkZ4lff_hJuFZPHWoZyD5kkivChCRCYMPQ5ZbZTan2nfEGRm6NPDFyE5NuR_vmTY96L8sC7jsNBEkHlwJneFv9WnIUqZ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3Myu8XGXGcq2UWmd8QulrwjLUg8jDcLkpgpvZt2uc33cyFpVCKLDNNF2jxp0-XBumx7razXCIoOyJwfcTkAroDKx4wPrLPqU3yw-Xwj3sWW9KnJdYNotXgOw_y_P5hhcf6SiOQVcqhXfPpry_VRx3-pWdhNfRHcbcUoZNt0cOW3KnmehRE5ttDtBIGMJPNZnCiQ1u_DI6hIMP6XBej9iYXbOryn07f7m6JxIBRbArN7IpRJD4mpSvS37ZkjT4iAwiDZPn5T54sOZrfp5mCYDMISLOlZgDS34YZwxPtofOUqofAf0mYLf1N_kR44N5B-tq5kDWETYoJXoDj7Moie8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDZomAnhvZR9Oq2yVMCPL9ZepGML5SLYpzagfmCyHkAYhhCp_z6oo3L5ivIELJujKnSPY1Yd8WxER6sj8ObMMToMDqXc2zMsIcTgHqx-qSVDARGgwR-tyR-uxfAEg-lJ2PZah353HdN7T3Comv-tO6PqR2Y2qkoHJRYU_aDXrz6yk7X84UNHp6IyZbZre0fHSOp52W21l564HwgCmUiAbSLxDAPp1Nj3ecdR1lbS78p7vQsmEfE-N0uxbpkVZo2xxNCtPdNYM9ODrZYTgIZ4rmeo4N5ZsFbPfpMAiCwF7NxvUgZzo1rrKQl_58d2i4PZs9yZJWuHzHQ3wfTmI7YXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=HAZ1U37QuWQJGbe1b_a5cmGujkPE0EtR55jPuEiTirklN7HSQPcBpnpLrXWFQxybAA3R7nKREOzmGEAmJcLjmS-ZEraDNpmDWdrR13IS_GKOOqiv4vDOKXpIr_Our9sEzHtrAl_Wbw2lyaH8cOw2QgpqboPUscPbsxZ2kFk2ceJVTcoh1YbtQPaqyUjG1a4dV4zJsMFEf1IdmaHRqc9ocB31KjAlZkZ0wxJr01p5sj_-J06mk0JuvSZHNOf_JUeRfqx75nTzWL4IJfSWjBIh63EyTVcDPFlUx_o2_92S-Zrk7gn_8-uiaF6Ob-ZSve8Ais_YJZWvnqv_kK-ZS2xwFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=HAZ1U37QuWQJGbe1b_a5cmGujkPE0EtR55jPuEiTirklN7HSQPcBpnpLrXWFQxybAA3R7nKREOzmGEAmJcLjmS-ZEraDNpmDWdrR13IS_GKOOqiv4vDOKXpIr_Our9sEzHtrAl_Wbw2lyaH8cOw2QgpqboPUscPbsxZ2kFk2ceJVTcoh1YbtQPaqyUjG1a4dV4zJsMFEf1IdmaHRqc9ocB31KjAlZkZ0wxJr01p5sj_-J06mk0JuvSZHNOf_JUeRfqx75nTzWL4IJfSWjBIh63EyTVcDPFlUx_o2_92S-Zrk7gn_8-uiaF6Ob-ZSve8Ais_YJZWvnqv_kK-ZS2xwFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚡️
یک خبر خوب برای طرفداران VS Code و GitHub Copilot!
اکستنشن
🔀
Router Models منتشر شد!
با این اکستنشن می‌تونید مدل‌های مختلف AI و Providerهای
OpenAI-compatible
رو مستقیماً داخل
Copilot Chat
استفاده کنید؛ از OpenRouter و Ollama گرفته تا APIهای شخصی و مدل‌های Local.
🤯
🔥
قابلیت‌هایی مثل:
🤔
مدیریت چند API Key و Failover
🤔
تشخیص و فیلتر مدل‌های رایگان
🤔
پشتیبانی از VS Code Settings Sync
🤔
؛Import تنظیمات 9router / OmniRouter
🤔
ذخیره امن API Keyها در Secure Storage
با دادن
🌟
دلگرمی بدید.
🔗
GitHub:
https://github.com/web-elite/router-models
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSc-FyBLhPsWs9gUXD2fVXbTeQ5LnYJ6b14vCvk4C9hjY_-Gx9z8Y_zbLsxMCl8OyhAZngQMRwdHdUq9XKam_geQ3blV9E7QsW2tmJF9aNkmHhqcUp6hQ8C0qU-A0Vx_VWJmc11j8C0DUNafZNvkm90pTuXZGFdMwD41EweHGuVsjvSvlkGmoF12MfT5tu3LjdCbCqJEh1JzAr4H7M0T3QkcDjKgdwHyS8iLty-n77Vmr7ld8Znwt-RqR3fYOH-K6hdlEp9Db_Z6lhuoeVOrCQrHBamA9Fw3uVKWthLBTb4LC_2nJjMEsMxqxqaK2nhBCInOyHoZxLuIIt9MEA-sSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
نسخه 4.7 از Grok منتشر شد — قدرتمندترین نسخه Grok
🤔
پیشرفت چشمگیری نسبت به نسخه 4.6 در تمام جنبه‌ها
🤔
عملکرد عالی در حفظ متن‌های طولانی، کار با کد و اسناد
🤔
مهم‌ترین نکته: قیمت بسیار مناسب — قیمت همان نسخه 4.6 است.
🤔
با توجه به پیشرفت‌های چشمگیر، نسخه 4.8 از Grok به زودی منتشر خواهد شد.
🤔
برای
تست
اینجا کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDe5uF70pRS-VSUkTHo1zZP5v51yCkHhxw1QqOOkkiZogq_2AEQRAoV6UcsOSqt3rYauGdNa1cuUwzuZeyCJVy4G2khMnWyNF5toB9wYZRKL8W961mJojkws2ehZO1JDJOLo3CvuXeR8quKe07SJnY_uOtWh06AQ9UZGzRwuBdE35MQnSe6O4I2sv6Ildl_8kf_3O7YkrmbbanKJu8ktmy17lo9ytgjDY_RHb_s5ykoXTWg68kseqXiLYQptM7qBPm_PVeL_p3ntmMZA8ZPNXsB4QePhwKuluA3Hjjl0vOZEgMh9pndtqX54cPwnblY8lyEzbamG71brmRAl7eWZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
500 میلیون توکن GLM 5.3 Flash
؛AutoClaw دوباره توکن توزیع می‌کند، این بار به طور همزمان 500 میلیون توکن در دو روز
21 سپتامبر: 200 میلیون
22 سپتامبر: 300 میلیون دیگر
درون آن، GLM 5.3 Flash، Deepseek V4.1-Flash و V4-Pro وجود دارد.
🤔
دانلود
AutoClaw
و ورود به سیستم را انجام دهید.
🤔
بخش Credits را باز کنید و روی Redeem کلیک کنید.
🤔
روی Claim کلیک کنید.
⌨️
انجام شد! حالا ما نیم میلیارد توکن داریم! مهم این است که آن‌ها را در طول روز خرج کنید، زیرا در پایان کمپین (23 سپتامبر) از بین می‌روند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQRvv6k7jowRM66sVm-jjyjoZNFkskYrKt31zGG41zcnAnEpu7DA7rSIPaY5Npa5VEg2Ao-xCVX_6wG4EwxESRbajEvs0uxRp7PQ4wLZ192JMAipYiFgjB-Cz8MQLUc190L0oPINhPP_Ou3wAhHa2juNsg0bdOdz_YVUYLsfDvm7DQynhqVMxoT2tlwaoGxeiCVY23-Jb41-LUNHNFeOVpju-AfqSsX4PvdroumTCr_LR5LrohsK2mNv_xC9S2CJmb8SYeIXiXbRdorw1N61h0RstalErpbOZHzgUjq--IMDVivykB2IJ4awoxseEYBmyvpItF4diM61Cm1yLAWKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مرورگر Sigma؛ ایجنت هوش مصنوعی داخل خود مرورگر
مرورگر Sigma روی Chromium ساخته شده و ایجنتی داره که به‌جای شما توی صفحه کلیک می‌کنه، فرم پر می‌کنه و کار رو تا آخر می‌بره. هدف رو توصیف می‌کنی، خودش مرحله‌ها رو جلو می‌بره.
🔒
مدل محلی Eclipse داخل مرورگر اجرا می‌شه؛ طبق ادعای سایت، پرامپت‌ها روی همون دستگاه پردازش می‌شن و آفلاین هم کار می‌کنه
🧪
حالت Deep Research برای جمع‌کردن منابع و خروجی ساختاریافته، به‌علاوهٔ چت با هر صفحه و ترجمهٔ سریع متن انتخابی
🗂
ادبلاک داخلی، تشخیص فیشینگ، رمزنگاری سرتاسری و پشتیبانی از افزونه‌های معمول
⚡
در بنچمارک Speedometer 3.0 روی مک‌بوک پرو M4، سازنده مدعیه ۱٫۱۳ برابر سریع‌تر از کروم و ۱٫۳۰ برابر سریع‌تر از سافاری بوده
💡
نکته:
نسخهٔ فعلی برای مک و ویندوز (149.0.7827.117) و همچنین iOS و اندروید موجوده؛ نسخهٔ لینوکس هنوز منتشر نشده. بنچمارک‌ها هم تست خود شرکته، نه مستقل.
📌
دانلود
🌐
سایت رسمی
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in4P3CvbE2eE9idTz9ieM9kkOdiS6Ik3q5bV6yi-giBYwQ2aXsrx_Ifm7meF-cd9vD-I8OO7WobnSwYN2mH-0c8umvSB4luYcg-Uulxel9jdvrVUTAP21AO1GLKvxAEJZZTVnodl-FDScuKP3jMUCMC_UESc9v1iWjQROJk7gCbnyQ5fodDPSZdPfd_GtEKQmwyGJ8cgI50gNtTGEbiUKHTu3blUERdZIk56TpXZb2GOOftYuV3_IPObh16lO20RAqqtRxL2y4zIvuDvVt21mHi1g_oeCb2ks9Vdn9tIAOakHk0PCGDxbNELhdLmLP0kTczkWqeKalaUdkgvBAIKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNBtTTrtijt7uo2JuT6E3MduVkFJOYknv2kji3AZyGNNN2PZ7r_IAis5UF6SRPEgTP9DgR1OVQEQjtS_uTpZQUxNzg60P76dAoi2x45SLfppdvOTTftV6EZV6TRctpStLP0-Nx_Bd6fZuVjScXdsqwk43DTbbMQiHrmdjZmv7DXWaBtukGOgl2dwgWSfkpjh7FqPtwHPqIRwV7-KPsIUSMVeeG3uzoZkZReX0UYGkA9OZf_wIo2fNWMSVxb-XfZTAqg4ewkJK2LC89yM_MaXpg4QJ4MbCNGNoHVfGdu1Y0hY7gjtbLxPSGqqG8TTkxNxURLdAddINzCR8lwzDzGcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWO-aK2erM0EVdkk1q_Z6y7Z7_Kev7vJlw3Xrc6DvS3SkjmjaIzPIV4U-gYMyS94FdYLdGTQl4j_hp0DgzzkmgVlY6n6AnSfSRRadoTECV8_nrqjECfLK6pDuqmO0jaUvZjWZMKnkTcFvlj63qHmrGaaRaRlDDaOKdrYCwX4M10mRJhipFJkqQjKJLxAXS97Wm9Vxf8V4hnjz1ES7agYR1tBhdobsvrGzeINyQcafMlM7gDDl4GlpUovdw8CDACeXjIvd9WaluasjVElIhuHGco0gh1xt_GKbJOl-Kuz2FuK79k7MOO12f4alECfS-Yft1ds_nbI5LlA0L1yWRzxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cloudflare Quick Tunnel
☁️
یک قابلیت کاربردی از
Cloudflare
برای ایجاد یک تونل موقت بین سرویس لوکال و اینترنت، بدون نیاز به باز کردن پورت یا تنظیم
DNS
✅
با استفاده از
cloudflared
می‌تونی سرویس لوکالت رو با یک آدرس
trycloudflare
در اینترنت در دسترس قرار بدی
🌐
🔺
بدون نیاز به دامنه
🔺
بدون Port Forwarding
🔺
مناسب برای تست API، Webhook و سرویس‌های لوکال
🔺
راه‌اندازی سریع و ساده
📌
این قابلیت بیشتر برای تست و توسعه طراحی شده و برای سرویس‌های دائمی مناسب نیست
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgVErynxMDitaXWeoy_DafjM2EFOrJ3PRukDVQuodMJyNkM21-mhpIf21IW1qqS-EarPxN0MOtCquKLFLzzXdh7ON1bQ3d_PIPX5zaupDWLZ0SNVQc9BdXUDIx-3L05-h9lJQrB789H0NI7uQPv9jp-yL-QB_Ym_cw0rB8IcSMhRLpmEtxPOeceJeaJMGJMkKYpNkXjb6WqxZCFRoszJkvmApT4kIgmDwKzEjQ-BbvJF6lNpAspRQc5I4MS7mYf1D9-Wm3N1FnkoPZ-YoL7ZneZ2IWmYQwzVeHb7tgUKjlujDoww6LIeAJmTiuZ0LdcWkOG5iA1uFUMROAKcRyjVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی API هوش مصنوعی | قسمت اول
🤖
سایت‌هایی که برای ثبت‌نام اعتبار هدیه می‌دن!
بچه‌ها یه لیست پر و پیمون از سرویس‌های ارائه‌دهنده API آماده کردم که بهتون اعتبار تستی می‌دن؛ خوراک استفاده توی کلاینت‌های مختلف برای دسترسی بی‌دردسر به مدل‌های پولی!
🔥
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
سایت Modeloc
👑
└ خفن‌ترین گزینه لیست؛ همون اول
۱۰ دلار
اعتبار تستی می‌ده!
2️⃣
سایت AAAwinn
└
۱ دلار
اعتبار هدیه ثبت‌نام
🤒
اکانت گیت‌هابتون باید بالای ۹۰ روز عمر داشته باشه.
3️⃣
سایت Jucodex
└
۱ دلار
اعتبار هدیه ثبت‌نام
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
👀
قسمت دوم به‌زودی...
سایت‌هایی که مدل‌های
کاملاً رایگان
دارن و
هر روز
بهتون اعتبار می‌دن
🔜
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔥
دانلود فایل های پولی، کاملا رایگان
- بخش دوم
خوب سری قبل گفتم تورنت چطوری کنیم لینکاشم گذاشتم، حالا یکی میگه من حال نمیکنم تورنت کنم چی کنم؟
یه سایتایی هستن که سرور های قوی دارن مخصوص تورنت، شما لینک تورنت رو میدی به اونا، اونا خودشون  فایل رو دان میکنن، بهت لینک مستقیم میدن!! و شما به راحتی با لینک مستقیم دانلود میکنین!
سایت سیدر یکی از از این سایت هاس برید توش ثبت نام کنین:
✅
www.seedr.cc
✅
با این لینک برید ۲.۵ گیگ بهتون فضا میده، ولی برین تو بخش Get space میتونین تا ۷ گیگ افزایشش بدین با انجام کار هایی که میگه
🏃‍♂️
خب حالا من لینک تورنت رو پیست میکنم تو این وبسایت و فایل ها رو بم نمایش میده، روش میزنم copy link و لینکش رو کپی میکنم، و میام تو تلگرام وارد هر ربات url to file بشین جوابه مثل ربات زیر:
@uploadbot
لینک رو بش میدم! و به همین راحتی فایل تورنت اومد تلگرام.
برای تست فیلم سریع و خشن رو از تورنت میارم تل که ببینین تو کامنتا شمام تورنتاتونو بفرستین
❤️
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
