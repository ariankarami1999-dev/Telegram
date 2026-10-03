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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 06:32:46</div>
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
<div class="tg-footer">👁️ 720 · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtL5bvKN5w2BlfV--VFl3QndWJJ66hfzdyoLXiXpjSMzn-LOdJol6-V5RsyZV-i0XSNmfiLdn2R5wCt_4TTwmzQw10HyHpXkN8-6zKWdKHOF9ZKpuHlQUFSAWjm2c1LhUHyAPx02oIyWVSA8VvzNIx939bav8FCcO4czr_uFM8vJAI_a2-3UX0DeOir1Cxdf446OyQp85vQi59LN3p8rWAe7grN9lUi4CHfo2-rc1SZtEnRPNGBcmV7pHRCV5KhqBlmwEqtINy1G1_-ftT5a4GSW6wmlPCp8hIH1NHTgFy52DUOKiuhNVHQCZChdG5IFYUrQhHZmFqMBKsJAohFhBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXMPSZGepz6F3Ekm8ZfJq9pKDX0UJsCHl8f3b8MfI_dFoPH53w8QQfYZMSpOsyJWGdExUKlr_HmWsy3i4rs5i52CcXax9fqAzYMOQncoBm03n-EajHpQwyhaLPwEWWMyeOUv7uKEH1t4nyMp01QDhncgieV3tYlFElVXDyWfqrbT-PGqtxOUNqMd9BoLeR1-3KUhFweds0SIJZ_UGBFcBxMFKUm6qxrqT0W3nrfL6FTwY7LUPRV-tdcTVl9j5vB1zXJfyJ_VseX_k7ZlKGWs7c-DNavqH8-W5Z6dY-YcGBjwZaTTzro5EsNDQkqFnkLCcNcW_S7_kF_c08WWaOK47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmgJxmcHKmO9JPew-v6Jvx66YBrW6yVzjByIDy_gqkEgWu-Usp7CNsp6DBgwaI50IjnGB1ny7k1hOoP8J8Y_HFBg0MyG-uAOXu1jri1YWt-FW4Npb-OdsRvyQfHrZ8N8uCAso7D7Sy0jDCaAei94RiZuPLLwA2eAsMU1aJsGybyv75qMnKFcNQc-xZub2e2lVS66d-hRCHPaY5SyCD0JQVY7kNoO-0z7RyRFnC5zXbfLOUcpX6YQEV_-frvV58RDkXbsE33_V8bm-P6ij3o7DXqBAL_Q0nsdqtui_Ow0Q7YFnC8q21X46WZTl7CjQU5XjIjr6KD5C2ifZ_n2sXBXSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6mPQZacLhdR8mRTCiQsiQpC5qrzTmQcpzSWeFGmwDl2K8MrroCTvXXnQTKgPJYXXDHjwvq8X9nG0N_tzFg4PLtV8_oNH2KX5k7ILNPgl4Wn3E8PkSjCSuQijMI2agO1wUOTaScd0W1tLEhb6GdjJUwBVRWOvzXIEPeRLGVf8p1mcOTu_cQrkks4D3UwJ-HTfz1FkY1Zu7hoFpRjPVwajJT55Lcp-73LOwt8P1Bo8UmqTOgxu8rfsCJ0gAmBwuOGbJIn-ic-yKFFWLXgUwyhIRlmV1vmyMlf0RwR4W_zoxdIjITOBFGap3Cc26ITBS9bZg5waZpZ8nbNTzqldiiePw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOc5wI09gBF2309NB1g3OQ0y3ZR9qf-PwiISwzVtlOVUTR_VgXv7vKXVqhNWXRriQ0dINMldkIFaZr6qTx1WzW5Vq0PqJ4bOzepN5iILI2IsZjK_rglkTTi0yN_b7WxhGHpwhycUoun8mqJ5UxOqrcYfD1KDtszeuU83VJoRRup9jDFxVT178Pq7WpqCEyCTVWCT5w_wJ6c-raELOzEN7Ua5VakFa_VgdCDpFZSBYhIWWoHOd5kndm_ObnfYcWUL1iS3Y_cE_DWC2JAaugi5svZI1es6yeBdkdQsbh5YaWY8BP520rjzpAmZGNJ9JSxkikUIpz83A9oy3nckyIHUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCHpw1esN9NyTbcsWq63vnuh0RhVeQGFTFOsF8Wgb_r1zCKGO-eFRXA6ZUIIxYF7KFHRLHJMmCC7VguUh_vu4oYsLPu_WErs6eLZQdOKumYRXZqyF88iwSMfo-7xYJd1pq1t1ZI4kyry7eDeNXfebz-_2P4SgHKy7mLwTABVkBaRgLqGQxkHhyP01afeSZfYaeXb8lmikgk5b5pWFpC9ZbOVbM65888YT0KL3bJDvwOIpAkkAxHMQva3NS__zAx71ghoKjCWpB2ouS-9J3h1uI0uAxqKxbKxVX4RBuZz6KTi47Nv6cheZgfhp5OHIBU016SGqNa-w8wGP0FTpEL49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2avPMb21Tx_9c55zHs2cjnbDqKKCp3DXBHSRx-CaTndCKXG67cBNAR1Q6yNkp5jD6-_xFTGwFqv-ARFdC8RzvBdFcVXDaslkk7nldNogOaKizsfS8ToTJU6DxGKT-mv_v2SuE_0N_ugBTdbfaDfurU8-RIrpQmeIrYI7iHEX66chRC3lmKXEFNe91o_JwJqSAoxapcLQ_FpSNJTtZwLY87vS80uM1ybI75wWxQBMBXsfDEZ00B63LVMfTrWQtJDv9RPrUwDBhtPSjscJIn_LXFx9skGpO49hZUCEpfyR3z1dj2wzRlzj4upUW-XdgN1M7impCXItLi48kpMYIoB1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIVaYpAnRpWADoFQ8DcdIjcID0Z64OJtrYuu7luH0eTMUKUAlNwYGwPLD4QB4xPjqo2qzUG7vnyZR9B-3Lcx6nnH7iHYdEVMKmP6irSObG0QWs1Ov-Owa9_cO8zYGbNXCKfDlgIJtYicm5ipNKTzotylJIDxAieRrszEC0pBHnyxgEeJekmg5_FP4Y5SHQNY2QS9k3ISMPMBWxUb8EJMZeQaaGBB_ylUXjUQ9Bz1wTpcSiVFGleD2wkDIDKb0e62NC46Zf26szW4uve4Ir64rWh56387nMxqvLKjY0L7ziWMXRoPRTfP7bZnHE9Q_DWZ2at0z_Aa5Q1dTpTe5roNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6mJmOvYnixfHrlGaqWWyrgsgnErJ2Tiv_WTroB5Z76VYuNND7irlDpqEDKx13NKOS9n4lepseU5G17J6T10RG6Sc8yOw9es0LuHw6Y9KPkW5TcEJREkMF4Y6pDegGEUyWAEP44R-P9G6BbW97vgDQosTsIStJWi-tquX3kG0-XyIB-XEEmZ1bEZ646uvUH29vn8xYvP-G0geO8g1JhHr34atx42nrLCtzXhjsNKffTfQosP4xtgmlQ5c0tH1akTOjiFkX4h33h1eW2bI3YoeA3Y4AYiaPwcA78KGiD2JKmoQjuxBtzX9RRuU1xI6b_8AUk663Fw2jPskUHGNpdGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUtI-Xgh0nP4F4UJsBirDhmDDtdFcFm2yqOYx3e2LCI9LgC_lNm2lL6YpXuJdxRG8IqJkGOji5Zyp4oOQEc8L4jUYI4Lq1WGX6foEWHYT0NQOlLWa-Fckyny3zrjjUHod9Gt-A4Ii2xIqwBeGBJ-UKcU-lC_i3GWTjnC-Qzmi-YD4bDinD1ljqO4vC3N5JCVTNSjh8Eyf2ml48EpZjR94qqEeIKZsJI6endUMNR5uYfQytPPpiuE-QGSnkngrx8-Ug5EOoUUBGtAjB-1igd-QQFEmTbdg5VMjRNuBBz5_u9YMMueSOwTAjBQtslxgQzNwT0ujGy8qk7NXzKnJbfiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM-ZBtfuWGLmfV_YGYnecS3zlCg41HiyjhF-oi_LOghodVv9jDhAk-UprwLU9YpmXE0bdjo5b7HCUW55oHC0Ne-LcrlflQxwGfWZaOPcLm3HxCcLLyYoWgo3Pb_Yr5BFp62dTgMoH_4NT83kuYhKnkiCufiJxVBB22UyfG2O5MRJ-iTG7spa1rr_AXkESw46n6lAmubtpyAdqRXuLm_mufInb09vJKJLRLIkZFJkALyyRJQg9duFOvhct7ArxE-6-bQOnVB9kBF_DF1-ujuxv4Dp95Z9XfPrQMt9uOy856dZmPX-wxnQhgh8fXH-Mat45FMJT0bAhhUqerSppl5PtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmIJNJiQZAkJTMFskPJzoNz96DfgIeLIN9jz8qk0Xorid9tVy4QGqR-fIhViuQbCMXblYdESshzMUQ89pJHCMdvQ0XUFOb5oV7sxGoQYljWxO9Vg_kEYgVaZ1rzo8llO-8-NPLlzm3kT4VFYCauPYK0sYG8wyBLsX40J2N-39r8Mmukh9L-26wLXVkoWJ304bqiPP9k5spvWqzR8RLksbrD8SSHT7WftKGHyIN6lN-QyenVUSnI-HPKTsn5cJJcZnS22zNkzRRR5EjUZYOaGend9fKZsdo1hqIdC1sXtDGVVJFRW3BiQSjS_oCrNaya817MpnvDg_mG5C58o-Uh9_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cW5269eIeyp39dzsMMSO92oFn6Qlc1DpFkSJg-EGpVEsca9NYQbm_T6krDFh805IwmdtbRc_b9M8ylo4sIpL0NdLcWKv8PZTITZ_DbzL0GhVIROfsDb9JM4B9NpBXGcosXk4RopO_U0kM6Y-Grc3VupLu15jzYYMXtxwPUHL6dmw3gLr3CzQCwE5hluSzdeiaGXLBJQVPPNSEbHUZelWdl-Rn69K1QKmkt_SUi6a97AfSbPHE7OsxBSCjEGWOdmTOSPnv-lwyGsal0oyMLJWIgJgP0qVloAfSZTHtbsSUS4zQoKoytPUnqpUjRg0euSTzf7HPPMefTIj4LupcgefqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R72NPOEMtnkra19MOR4geOSFBFLD_HRQ3MSP7PivWtUf-ffxn6N2aLmc4IXuSiFnkbgbcrGNV1QFv6jwPhIHy_5obpVEmSMtgUqoxjn6IKAVrRbmwEg4LcyqXYKCDvHs_WaBI3HFr5l3fus4Y8CcaOmf4Z91MdmG5KcoArMjeC1QEcHtPer4qyL3eUsdPhIDC5cyEDYHpqsfLGYsfFJmPXP1Ker8AUXpb6h3Vx94Rj7rmDYVLskUdAap8Bh_0ZTtZyerRJTqkqPyQpFFYYx92F52CLPWgiBEFPpGrCx-VKFaM3w3euC_xY00ybq0QTeDD48TqDmu6BH27v78t3CXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMguWQF2QmnPWmpxwkGzIhtiMUxb8i_8xzPjQEgp3VpdteW938h_ijAGzvJZmtFsGJSZjhIT39rbdWwYS8z8-Am3-sn0NTPOqY_n8a8FH3-Rc8f0DUfN0BzjH7EyFQysVSY4pW0QQ33luIoYyogyNuEMLBor8RJyGnd0OmCBPueIg-S3EQtGi7vRI9h3soLuvZ4zXFu1V_FJQXHMW_OohcyMNtomMJTywMd6ZdDy2m2FQsm3VgGFcdt-3bSEdZx_V49l8FAF41clxBi8YBNrdQbIGY6q7olnF8ktnZZR8AHDapOsTpOQv3O7lNVP36EBCENcuJ2la9tkhdUjrCBeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zd1qYEYVBCQLi6KtkHUUuGj-cC-W0yeU23dgD8vQV5xj56FMVmZy4Nry0e81FXFYzcBlS2AHyf2oe859kzf_2tVYosgbfa4gz4ZSwpcl4fsXc--PY7axOglUVkVTiAnbQ2Rto1lwvIO8YcXuZ9_t_2QlGMUveYsa0KGQFiBCv77Uu9t8LJ23EvyjrqIR_JbUJQmYvWgGfYB5sIDT9usQQD_nwkO23UFxKMVSUe3bnMAblNqGwWDoQdftbDxW7yawf4FfeonOYx-gNju5DxmV7W-DGDIasuTbaZ1fNW3TcPxLB-X80OTJl86jtNJ3Ct0WKgI4zIamypwVGYOAxu-aKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjRWCu2ocAQc8FMjSFgpnc6WDfb2hgPPCsG4h3cfeI9DDeT1x93ZOBwHdThxHcLMc63mC_qZWPaqx_F7nOhIgQmXGCz_Agrsaj0p4oTFvfRReb_3WaVrTSbLWmpACGy1UixffFbuG0esRk61A-q2sY2hjf_4hEbYxcSQiE58eZh4vQ8O3OOhApuZ2bqmnhhT6IKO_UB0FGA5rq7cBUcYXWXPv_0r1OrULsKGsF6WjATcAV-wZ2oe06c3h8wN5kMSqIy5tS5xpOQ118_TiBtkaV-qLq7wtIE9xWRTABG-EQLQg9vGXWXNux24BJMx4l7OyT4NxvkIZxya_VoV9ykeHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urf8MkcnlT797h8q0u4W0J5ety7UavIXUKjvi1Vos9cEXWefdW_NYoEiSYgnwBGy2M6FTRciAaAc79rGtakWZ_ulubg2QI1_0CBIsUBZJSDEM-dximN08Q-gUE-gAdBhnGnnep-AzyoQ-V9MjB9ZIbykug5xBhhSEn8IOhZjq3z4yVB30Zfz91uLfSVLLnSbeljOvsZ_YUMacBmKENuMtFg6vRPmLOIBqQkcUVE5uALmg-kXwOa-j3BtBdMLA2EdxtN9OnNWSKIOPWw-DIKYJV0_xEK3oxh2M0qaeEbKRKf-RyIW-t-spxqieh9Y39So4ZsaKc6UZnQ3IVnT3_mg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7OmHavTsOP5XqD3vcAN7Za7n07Y7mONn3i12PkBXYX1ITaJ-iloRsYivgCRjUCXd6zGKrEM1snqu13Sr2Wj0m67SF-rrR0mBhC77yziNwv6jNE7MpCYAuQPuurSMqDU4tRbqQY6OxwXgWTqRUhmShRcN2WD0ofPJg4qe9YArjnelrQ2nFSuQ_aRD4g-1kmA6BGK9cbH4PZNKP_G2DmE60_lNWcGzZ_V8jVtg3PtygFghuNiPzZF5KOF_x6QwS2dzi0O7iNVStte6m-1VgiXarqPQv2PH5ZUq-9MuIjl5Xm7-HXvDLJcP-PtagpFfQbDMNdAn3dLpe0nb8Rg42D-_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG0R58aokbx7fWmDIs5w2ZnGy1y_0zx6uUAzvqdW3t04BjTt-iWs6BvM525hELLlK6U70gDr2F_bo7ncjnm4189HlMmo7gjgEnl5kD1qH2SR1If4mWkig81P1V6qtl1I5a9ZN8SEIrnp9X4zWs0T3WD46Jt1MhxQy3hO5m4UZV6DQBboba6JCYtod2YfmUs8zkOrBNKzcnPToAwUwioWKXLNvbTysfGmW43dQ29jZH4rC8wcARgelZY9EdRKMKogVeHAzo9GL13ksS0PZzCQZD7v1wSV5VcbGEodUH_2r8vEoBHplyekIhxz727lzjDLw2_fttATzYPcOm0dfRZovA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PigtX1-VDlqotJSe5KkPrPSXBPlQMC2x87WXuxzKBCshaKoNK-Ra-6V-nXBz2NFLu5oob6ZyYflcncFnyydgMbZqB0ywbO2uxL8IVT9hjtZF6QO3Cw0DBf7uTIX7B2VF09SYXJiDflbX_jtJOGMMZHL4z8_ZMzBPRkCBYvnxYpVUSHtB9p8t7pomqR7D1lsGtI3jQ5o8Y6ITc7wUeMFIdgtWTmywEEBQ9gwKSrqgtorvP83sbs854bnX-jiIajrH6FdhjVBF76LJ7orN0iVRx2N43nsA7Qw-3lPQQJRl_nc84PNQXWer_2e-d9JqjVhyr43gEk-lP-R58KK2BAtRqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4dz1YnztJUWoV9QniE8jEOccmbctHvbTeYQAnf6M1gIxyjo2YuDqvgfRp3IVAzq22ogtS-6Y-5PQsiyiYUVkd59rbQ4MpUESroNo8AYbsKlpPizxYrqeDdOiUDKpmr8Ay8tSKIPgq7WseuPjm4i2uW-keLDnWxRPQO5fH7gBpKk6fLjq1_Iv-XI77TLIuSln0lJQgfbbxbPXrmN0cU6PX71OKJlWXZ7RU0euzEhMOGRhlnRxVfN4GMxBY0fnxi235HrfYdCdZSdFEoPLUcffLQTaGlHbMYLlcXrJFLx1PjmYM_5MBLywsDwGF5wteND2gVMGupZIfQ0SGjFBgQvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGR_1LricPpUrtYSPsktGpdUwCi8MpMjhmoayK2XAg16phKnN7s_JrYYbKZ3ACmtVaPIVUVv6EuTtVQCr0_EG_v2l4NHhU9P9SI5hR5cWoraiy9iKmAXxqFOxenDq0Oz6LvL_AEbrDjb8fGONJkJtMt6WsvFiU3JVzwkLJniAhnI8uqf0_m6uIf-hkZEE3YPKYyhV4qnTlvBn-i_HqVhmoW_HP9T4hcjPRyx-anevkc_-8GjtqWzOmSGNMuJ4j1Y_1BQW6BGvqECgnlSg8GZHSXrvZAxmXsfs8X8NGSIg8UbBqOcZTZIFMJ5d_HcPHflJA7x5nAhjnyDeVStTLuOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjCjDy5FGo4D91bL_sPl7VRh95a0TbSdCNMS6Hiv0Jq2Q06tJbBJIXfVLEpM1mxSBGzsgHGp4g3zRVzrES7-yfi2Q8swVqVX-lztLplMR1ZjCbq0JxVKyrfhGPMiM3O5f9NKBI_aa9gs58TynSecfCOgBC7RwU4lA56aI1oPoqlwBgv8NZJJBlEEicONi54oK65aWARMhMqq7vB_eVjXS1cDNXgU-Fms1UjQkTlrrUUvb2LRdo_ehTZRa-2V7MLmNTfhVnQLbyfhAZWtGTtrvssuRL6moEZeRDqGk1W3AQNSN5knMUth--0Ly0fbdI0eMrbmHzKaWSkCM_qFInM-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9dMMSvmosZHnxZotMEjFE836kT3x-pFRhYmD0vgjE_y1uytItO83ZHTlFe5UHF5xmcmJTjYrzQI8kYXW_0eZCUnuDk-PG753JPcue_VGdW_m48winZEgsAjaLusDrypIrBHGtkF3UlpA_jminbuUaIgpjn8GZqJwFttcpYxkiH19Gkk8Emx1So1FlFrodfxefkIP63g2m93zNjWLCfkr-aOYKsD8fgkmxvQ37MEHsrWOhw-K8aw01JeCyZ5YYWoLgICjYGN-Hf0cmEGqhrKPNCJVD4UcFZSY7fIm7Le33YmhySY1GJgG0Xmn7BDFCeSFAukPJ7aGCw2qG74QBZhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szVSAhyFC1_O_Zl-gcqNIuKEj97bo_eiKBExa1o5ZurmZDRWDuP1WO2T1HxNSeAMKrWgIZglVTHuWGjgQkXmTvwKGcQ2LbeKWcxlUSQiB7Ax0V2KADwmOqYzi2TAqXc2NqaZGVgrGVYEQp0_wUyGAoX0TZmIQ4iUQWBffj1W9ItSezpvrtcV48Ke7hht7wIedsHrIVoReG5qopOzw0FrGJfFzD3V_fDr1nL5mLdHujXYDkN1HkkAPxz_meK--sthdHAjtgkVhxIDdSGLfQTdk5sKZvJSpk9uISd-11PKknXxUqUYHa1_9OBOy7bqhfgfIs0x4mJdDTXV-zoGJdeaBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3zVkid-WmlVm2J7a58uTbPDbpn1Cj1nn9s3fHAtLJ6eJAQrZRfEgxbWHo1ljY66EcIF1jh6zbGVpgV3Pb-Dtryot6GFK9O1S_YkOUSvLaDIowu5fYcIrJX7eceu_z22E0FKywLts5YmpKrKUB-wUzarWq-g3SkUpecS3AumQ-Q7vJolTEYNyzlokUA7OL_M8wuyNqIKTlx6x7nW55hfqJTfynF1y5lWs9M6pzCz7APBoREn-m4Bn8bL6gfpDy-rypLgeWlaWHpfzABYb6V7KEdhD1T7ZS0GZUwSOt_FmRlt-V0Ofx5vRFGuhAhW4EUiUfZxmcf-hAV8KQbXgOLT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao-tJO0WDbzXLaSc6Z_NBrsy93tiqH8eKZwnGkjOfg2_bAume1S7x7iMf8TK9U7GnPLsDBw__MHNk2XvydAYW7RIK4iqIFdV8SLDNc7pi9weci9V9jdPKFaAezEqGODlBBiOE_MwpZ50JyEDZfanAqhAOXXzLiKe2OKkXEMvj4nicscGhromRUnl14NVubVl0LWNMr4-6lGqCGMqPj2a58NutJO3cFu2LNJ8JD_b1mgyEDJ2d5LxtZAofLYFEyFng0P4Wiy9sTRPrqbXKT5syMen8XOPzthHpr1PLO-zWI1T1Ww5Lw5TahNBJVTCKqrfS3gy9_vDBOZo0YHqJK7SSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLY4cvBt95YY_U4FsOdFplFxfhhoWIjTv7qqFxhucrhPTgq9jETqIZ4-t286KJpZ239wQhwl484B4FtMghbaG4yEIQWO3q-hAfNMMGXVgNRg-ZgRAxcoC_GiW89sopNfipEwLcbJPSW5qegCswYT7nQ3aXgEVTyL7YkJCD0cfJFRhVNoX5AHvo0lnyBfBJdAtyaDIRRBxVCYqZAsLWFWmUXqw5PFTTr86xDeJZOu-0GwgowswNm3MhF98FvltLK71qW0g2S66SllidvSAZocdL2TAxmToaoEdV0On2njK3DPgMjgiWcUCwMzVuL4snD6nDebV8toYYV-IEozSr3jXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzR-g6H5nLVMF4aV37QB3iZNNiLPMZDn-V9kTogvIfxuE4hL_Yf9EdVsgNY2Bb1-AmYESJWKmf2PHsNMCKE5cgjbo75CwycjGjuZepq3dZjVTA-LqGqWV92b0wpPd6E9SvbUUroMpxmYUdiwakgQ5yT3ixScpUpoC9TPYfLaqbiWPzTBIAHYDhPfwfQNTvanM1ZpxIQdflbG8Q0zixtJvZTiYm-olALjNYtP5CbQiA00-FhES-yc0k8lFe2kUhUproFD3U6MAc8EP0AnnJi65hMdkHxGBG5Kcef2qxrrLnnszVlmUncpvgjXE2NwVMuTdc2-h-6QL2KO_Jdoq_S7Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjjcB-VYaLb8f8EldWuSQkAlFr6lQFkB1-L291TVFG47Xm2BZXbX9Wh3GTdjBDvi_keZuwBcfcenx8rvOnv1oOaiYQyrzMjtWXTvvPSd2lCLRfeRe6_mYqdNflXZWzG7rsdEpRNTSwiYA-Ns-56U4SfVt0P4aNUVG9xcvU51Pd7D7PZSb579vbhzqDmggviJ-T8zQ7QFaKVfRcN2m1B1WmNqKNTc0oW_v8qB9AjzWel6WiN6wVvqlT6YPF-IW1MW0kmC2aS9V1pjCADIaywkYxL-YOR2g_IAHotvR2jJjEyJ7vhvLxkNeO-2xBaXQPKllH8LmpyFvvp8hMGCwiUGJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=ceRCrt5ULuQaENByXu7g2OfVUTloveCU43CIGd3kE4A5ICP76l2bfcO086bduhc-gV-Q-WZqRnbvPOUOp2QJ9XDbYJnel-sBinyiw5zSYEuX6RpgjEFyCPBAuwbR_Lhea4_VIzDKLMzM0VERZV6uqMkgAnnBgzaHXcTT81TmL7jovkTw5RDjm0FavLO7qz9rOho9-CEiLctGfedcNib7WUCrlbyJEH0gOGmR-cpvzTQzFUJCrutJ2oJdfkX0_jS5r3AHSaHGBYrWU3jVkD4sn2gr2jXnCYe0UXN72vZ9RasBvfgrAkjvYBSS64YWuf5dhSHTOB7d0Ni-FzWd1YOvqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=ceRCrt5ULuQaENByXu7g2OfVUTloveCU43CIGd3kE4A5ICP76l2bfcO086bduhc-gV-Q-WZqRnbvPOUOp2QJ9XDbYJnel-sBinyiw5zSYEuX6RpgjEFyCPBAuwbR_Lhea4_VIzDKLMzM0VERZV6uqMkgAnnBgzaHXcTT81TmL7jovkTw5RDjm0FavLO7qz9rOho9-CEiLctGfedcNib7WUCrlbyJEH0gOGmR-cpvzTQzFUJCrutJ2oJdfkX0_jS5r3AHSaHGBYrWU3jVkD4sn2gr2jXnCYe0UXN72vZ9RasBvfgrAkjvYBSS64YWuf5dhSHTOB7d0Ni-FzWd1YOvqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAsKJXP4nTh0i8sHy90p3gI5tayBXYvS4K2A3E4bjb-NfIrcuaCOJ99qUcuIpqYHBtbkCAY7MfavKf0Q5xM-5oKcsW5_RgEI9texMm_3TOwfhvKtmFBnUBxB9hO2mcVFF9UBhbGQlDBdzTWYxFiLmLq1pyBAjwT0IgllJQYtCw38CjRVvGBqg4mQZUuFGeUqZjkSwhW3xjrVmIanzADgOd_3igcpOjzCtdFI3NrZ0hkqV8kg5jAZ4W96ribsOpY1XsXvgrJbBoqIZEuIeyaMnJls-b4sNNhYh4SgkDRNJ4PWuONSpAbLb14FWN8kWVeheBNhzMsLYNqybGkfKn9BUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPHb7sphsBuEU9sguJx14vTJQ3gmQxY8mR0TO-Sc-xxSP7Z4AYeqm079R13qF2elTnygA5E8F5tEo8PCR8tSNEPDBsCBIR1uT00Rga37-MOpPPYTtAkSzG6SyI57j-omH_s2i8bzSxc7rXzYcIg3AvlYhj_2Pfc6GV0SAo43Hjiy_PHSDUjQAWVpAF9bfB323AN6_M0t4Lr7PB7yAH6UNEikpZ4XL9Q_E9AJCtlU732PdI3mY_iBbO5QcJax38D4kjEG9VGDzgFTtNYQvf4PX793_pj3QrU_N7_KoyYKJZN-zRIZZHPfPuckOVPW1FRzHruI78GwQjaE7PIpEvtpcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7-Hx_dL60-1ZbsWn8iW7GaZvDE8fNSL28CqDS2lm-NEVYyUbNgZrzaxFT9g0djf20R8VBJj6FpAWRhCwvb867NgkfiN8jphQ85XJl4btMMU7RqqvpPpRMWi-kJqaB9KB-DIE1eC3npK_wyP8BYfq0OveO75ovG4JYQgbHJVDp5LORhbuyFtidCSNtS_Ol7NxAarVKz5ZwNkoPveFd-2CmlI3uPPji0mvzX9xy_vCrClS44vvvwylW2WrTINoa-hTAqh51UCa274axsemlwzTygMuyLbqAHR0YyXiDfO2_9HUKKFy24vwkBmjRNhq8JSie4bsGHZA77Yq_pSUKTOUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLuEE4-OlA1zzvVaADmysG248NjW2pS_ClM4nmIw2TpMRAPsplloHSPbUWwTg4RfuVUGrSTJhE2LmJMI20oxg7lgB-z8rKm4ZpXpK-YeBN6oXpvtsD3e18At053J5TtmzeVCayuHdtLbe2DA3ptpaLjGpAni9NOsKaM6H4NDuN4GT6IJ3vj6LFQygc8Q0evxKc3kDfRwC9oawDBnpt5jt4WMyUhXz6_CoKbA9dPYKsH2NbefFyA_sId8t2jIINc4w5CofZ9E2WDDCAHgTU8GM4NInFrJ9oGXESjNMfAsCobi1d-JS7A2vTy1gmEXSFMNiWdmNQ07V_T4L7-gj8Kr8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnaAEWyt7eUYLmO2O5f2xq2E5eshaaEInj7DxmKbL3lAXBaX7_y8uhMKlipYG8bUqTNycJ2f1VtGwq8MyByHj3k5XWdokjD29aGmAs587sfUgN0Zq7UOZ1geskVaIuFe5pkpISBVuavvd51S_d1-X2OSfUFGVGvnqBeQ1iqt9vAQzeIB7DbS6kyQsRE-QK_OuRSGG0KzPEyASNCAlSOx9DdDjGHDMdB6_rCxvrenpZGDdbdbWfDa6b3R0ueUZzyEuL95zDMM-olrLxh9JVptP-LnJKEx8-3bcoqIYyiC3EYs-5d-Gao5wKqa3ooFpMBflZC_nqAZDcSrKrZTmqnQbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju-kMiiesKlDEBIM19tm6fw15XJ-tNnoLicSEgzBmkWephOCCfAIvX1kkdLwbRH3Nij9XYzsRvhjNWi6jatdgW9sVaZ3SvBXOEvhx8AN8boqGrg0P_aCv0tii2GDqXvBCwZFvlQBy0j4ING5c-k7CahDpK1BV0KY0kCHRdB4Tt9TWo0SM3kL6jonEcTTKg6olBvG4NbYHUU6_sfClgJZSe5w3r_V8Z7I9UrNZ3pyNfsIEAiFww3j88rbtz5OoY6A14Zpsn40E_WquIWqBL2qeAjGvrRItFDtur-6t47xD2NNHHPBVf_n87SBCfLunq0RqRCtA5ebxaMcKlocqZE3BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL1vAuGuUR4PsxPlHzxKs-74wWpX_iGV2kHrmi4mZqOi3V7zNeqgvtyZDkhhnmn01dmvXB0pBUmnUbmGkEh3kJRR59MOKfcBO09Gb_6DGU-JBlt9qsKhZEMvVCd--xZPZnlf9SCJNm6uDzF1zunQtQncJKphey8ilyGBhuRoRqpsDPNMJfv8DYWrFYdbx9SOvBlkAVHCRTRxl6mimj9V56KNicEr1aQb_wVrq7DJUd1EIejpHRDltdkHXC3cW6bs-WioOoV0-1iF3Ze_8G9wNgtSuhZx4jHiRaiUOWy8lsqHuravUO4L5UN94BiwbbCOVNWOHbMiDq3wyHv05olgVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO7Tq12GbuiS4TB7iVoxZXsAPSIomSmsstv5FO_SzAXPt38Z7HHnRc-dKWlEs7BtznkvGuvn8N9nJffDVpIOeQe5mAgvx3pGcFr-ujEyhexwp2oFgEEq1u1ITMx7_It7CRdVhgcQJRBrzbC9nM3wWOvVCt48KIY1lV7M8SgdeBNS3knw0SMZvNEGyOTWBsp6TwHMH7Kw5WxFCbpnypTTyUskaLPsyBjW2QhiZsvV7IIp2Mapp5Nw7Wgae5p28Ez4I3tbkACWYbZjTfD0YsfmO9x-hBy_xrzuOEMu7_yJSEtPesRtDinkF77DN7LdvltgiXmbqPlHv3kBuVT5pQ6XoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM_1na5OoCkebGHvmQ_-QRaZfkJahTWZq3yB0rwBFCubRrbBCfHxOlvB7TLVRSOywN6CW3NcbqhVyWycki4So0rPfQO9M7GQ7KMf7_tCTgSJkfbeRSF0kJYi7NeMQ8Z_rrKlmGeIkJKTuFDMC3MIoV4wyVfxbQqeY4Ibj9hq73FzwlOK88MKkPLyr1l8RCyqk4juxaCAQUpR0z4tXzaD3KV8n3eXvlRZMaaOMbkq7PR7r1Zanl8AXpkhFdpqYqGvEnwJRuvpjyamygXIZoz1VcNUEPaEeBDPvGdroDaL_4R-qY6KcCQ_mG0IOX5XGpnO3awnXbDJV6x8xJp1bQMFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdgDLCHZW-7BIo3NVNKDItkUS9WLcRvKx91UkE5wHbTWGbwzoGyzKnPasWjutqG_GnHJOtRbd9nFg_pYBhKMoIJSoDJ-5dXJp0p9Xc0nnr304DJEulgcoH3O6u_qV8OSm7ULxMlyvOeF4cWRTU_NO77RJk6hCmnGaeUYPKMpRcOGKrSRwXFndhsHyQdX10FCEe9lavQTM5UfF2v_rT3a0GlphTiS-pBiVVfEXRo5TfFk7yukrudeMjEQlL0_0J9-0AtkcbCkVYtyKi0HtVZrfmv_SmjJjpvBxq2SDrmZ0UHAmIQPZhR3Xw6HK3ZbJGc_qslyB3mN8wPJkeGduMkaMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK6KxjkboqDjAl50-8mpZoPeKBLaGC5MUrXaGfMwvmF8TsfgsgENc64BafGt34xGOrOcR-DlZwyn4lmuDlLHy61iRHF736sS7e55NpbY3MIIgGb5bni_1zneXo2IOYWXkPJrQ-3wxFI_q76mlMAWlwI0W2xk8zdTdfJBfHUNr0OYTjeExiAon9GFNHgTFOQnEuHDoA1WA_-bdHyaSzWP9O0X3yKQ-fOlP7nZs_0v4a5cF9tU9-yMY6tf_1wloLTNXYuFMECfYwahmXGFIkHOfx-LSo4qGdmCjaKH2Pg1Bkeusoh7CMUokOJo_i36B6UbqEDkwqKE9O4pdepHOYlSgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAVip9iASn11erGeu5CKeJ6LJza1ZMrx41UAYq6GffMRBJf5YlN-EVMRs0NzWluBEeyZ8SNsCoTHy6OtEf-O1390jNnZGmV7B2KBoCqlxyAn6pGML7mfQRZEIbknmlApH0N08Lwz79N-qvz8oHNRQXAyFQj0h_2YFYtJfU07ID0ggBqBsWfUAJoyI_TVlJzqUZZhZKpLVpY6piMl0Qd0JqmWzJ_WMpGAoFMtinrEA3ZNnAUUIvpfe96dBia65p7XUjTMnagev5EaM_Z2uWbcxay32QE8vjznqiBCUhcAisgJjUy72Ik6tgXsxuWzYVZrz8Raap3diQB_CzmhOta-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_JWJpbkIbA4lfCJx7saJ7_0notVC5bDKFYNeIDDqIos6K4YXW5g82TA63GcS0km5r2HmfaK6iaYkzGPNJM1jntLDft6eD97BOEtDn9TItwAqvrsPGkZai8V6AFG_2kN5TJXKbX_kQ_11iSnbd-GJGfgkysOET2lZe6vZGwvBj_3LlMw1uMVDxDe0CzMzgMmDtLshsvUAbyteAQl5pNL5IJcP_hh1_ix1jyg4jpqWn0DE1bRJ7piCI4_P6gY4jmZkHcnw9BV2iVoLCuejtvvacJYYt5xIto_30ft9LIFdJMHlTFBpCgnl5HXwq-09qtjcAR2K-Z0FjMGg7Z03mYjaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuDJqD8kK8LxBFNKuXh-__A0wsy8zUeAmZ9MYjRNGrcIHnUDrb6gONgW_Yz1LFhK1AnH7c982_bl49ku0dLOAKwZEbFyXKnUDdtM8oH5P0bGt9t6QpRHtBKDqI7vmxEoBidfaAEJwqo9w9QrDhW2XptadzCbwZBJu1u_gkIz4dk-xWXO12WUo1gRQactM4rDEx2mN-14wbDnJNrDmKhcVCLWjOG-lBFQMzVBQ4ZxqJys2mweYYTGNpmwrs-XxTmWE5vqWiEcmMt9TMvAZ9frgD1BXWo6maC6-W1WveGVCsogY6h6miof8zul_G9XfcJKz-XsSOANYX1ghuY6Q0Z0aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU3kGkX9xJjvqdfVZxjasHkAIew6jXpTXypFtldlw3gHdTZAMnohXPWmFzJluzaZiF7s9mCrUMKlXEqRjDVY06uh4_R0Ij0xyexODGTik5aKvmKLvXFc3zfCLxZfNMi0ZULsaaU8eGakN-bgsNzm1KMtDhgn3mkYnV-2Sn7ldIzZz9lKucMSmbyG5TkwLabDJRXCIqRvv3QZziUNY83TdBdfiahaNnhkp_cl9GwMh3n-DRG262uTTuX8Ruau_EAHj_Kdtr5OibV6B4MA5Tvt4KgBonWlN_xP07fCVIgCObwhMMXJHqfOQagFk8Efoir8RufO3qBtvTyfaPOr_N4jLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIKC5N1rFuWl36O7Y7V2iT-KDuaBTJ2SJ2Ze4sZgFg4TOVP8zTWK7i5rPagh7LEFeV_goTXKYoGiEhEpiwHo83DF7fStcZMJSxT1ugQMHarUvHo6-u3s1bTMjZR46iET0fImoqtNfI5NTyeh32VcicfhBxYGmpfRYbHV6hofohrAkRckbN5acQ5bsWKxe1PBsxow31I7tD0VMYRWTx9Ts8cA9-dcwpRA4syDhOA7gUNwnfU0RLy1WJ9Ubv_xzysUyMXG51f2G11pXEhPdd5cfwKD-22FIIiZjI2XV6Ep7wzz3lh4DRPiULu9YwcfKjapJnxq209vDe2qYqKAO9Y25w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APU-2kytywhAJA1moi76p_l8M7f38so9IDIiexYZSPujKKrMp9S6uuQ9zuwtBAq2QKyaCZ3gIr6Pc4H9YRXtomskSe4AGv3dIQihlazDAos3Uq1CyzNdD3R4pmai8HPiA320vfzUbAzv_zZuc2IFT-6XGd2uQMPmEpkIGoICzxo3jnsSwCH_6s_YNwH0vmarG3C8gR_BIKNuZGHG67IpnFm1LZTg8QDbX2fUDiQT2YFIdYt84b50jm6dUe9RN8O8ByjA4tJtbBG6yKqfTQy4CjTZhxUSYNfi4IUevbtVI4jj9d1LWOWUgB9KLoIs1Qa4klGuic-irp6QHMzFMn3n1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjowuA1IsF1e2XUfdRbiEkO5vZniPBk0NwsHUaDhdwtVtt-Ms9q2pcNtG4exeBUsHEZiy0sCkbqV0Zh7ddCOgc-UFBJbh_ebEmBtUm3MvP3bXZ6EcpHXHDmr5mtlRlmHay1YMb3I0lBe3Kilq7uixtN5M1EBJq4ndMsTzjUzQMx0Rsa5gc3ikLNDpepYSxQngzULg4YUCznC5aF3zro-4lO-qo_Le4zQXWBRj0sXos-lZ6gjgnzohV6G4poA4tap1ChXIrVAGK3gHBg-GO_7CFK304Fl0aX936uM3d7p8OSsbFBm7c14MB5ay4GO1V7ZED3X8qPH9G4H88v0tfirsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdyhrQpVqT0E3PtVZlAL2v1meBJG_LvU-tg3nFECc1dM7cI1p2H_vwqZcqfnfR-vgdc-h8mg6yBc2ZbqbpmQqA0Hrved9hnhXNYJ7sk4ZL2tpSlb_cBLA5VcE1CkIzOMrI1a9CH1Mw62WbO3I7kiOa861VJII1vapytZyR2ke2n7coVASt5ib4biRpX4DAhF2Ls02G6jqoJjKo7RKwvRyUAcfdfkgixSb4D00AA7klL5_9eyFYQNyYDdumHefotpob2fqvAYfqi7_XbxdvnpHSbSFhQxFAe0s4AQ0x6knO6mvz8_SnTiqas69ulZanUxI7Fk2z3UTsziLyyu2jZGJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=qmp62cbeDY4arSKoOXJZNaU61BfrpsldKVIx-g9sSIpG3rSCTPSQxr93wHeB034zkHiyhlGy2iFTEP_t4ijajODzeLKshnUxNFC2hqfkoHJUskWByrfPyij0HFfj3ZMPt9uWjIuJ7mATUF2SLPvpn1f74hkDh0B1AssOHw2-9DBnVDOx_RDroXhsPGMAcbOfRckPS5ynj_E_Z2DMb0kn76FtvbnyI6f4rvNfg2ubyqHu7YWjK-5c9l9eVL4U_GACBdttLoyyF2yWjcADN_ofhKrPc-75d7aQH9GZgMtpTpiL-VQM9kBM1Rj32TYaSR3sjKCMBHOxaCUy9y9TiTvzxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=qmp62cbeDY4arSKoOXJZNaU61BfrpsldKVIx-g9sSIpG3rSCTPSQxr93wHeB034zkHiyhlGy2iFTEP_t4ijajODzeLKshnUxNFC2hqfkoHJUskWByrfPyij0HFfj3ZMPt9uWjIuJ7mATUF2SLPvpn1f74hkDh0B1AssOHw2-9DBnVDOx_RDroXhsPGMAcbOfRckPS5ynj_E_Z2DMb0kn76FtvbnyI6f4rvNfg2ubyqHu7YWjK-5c9l9eVL4U_GACBdttLoyyF2yWjcADN_ofhKrPc-75d7aQH9GZgMtpTpiL-VQM9kBM1Rj32TYaSR3sjKCMBHOxaCUy9y9TiTvzxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBOkUU1k7Z4v1IeoxI5ZtJMBJy1KylUG2y2Orj4ExGuK0qBCeJDxwxsYH_bYnoCZ4qey5p4HTBdGcHx0BETvmQ3ag7-kwd_qYJYE0asFc2l-r3vjOcS0uX5cHehBhfGEK9Tv_L356KQz5tT_ymLLMLOXPKIT2Hl7-q7cYeB9p6uyEQt9mqlqfpvFZGgMR1VXlx6xYgxh63mSYNE7WKlX7cEmr8yxsPtQjzfhZv7tnT5OT5TO2b9B-CW3nrkJIi_5MWYSgJ1mYAVHA1qafO6RoHqDRHh1woSKgZH516ABma-ShsEzfVKZH5qJEphUBnqQnMnHdUo7NJGE1idYeu8PNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9Crlx2chLVCaZkNcRNjE-46EpATBaeQYcaDoY6fHH8_RwEJS_mLmu9eWQLx_BL8xZtLsqPTyJpiJVRK0umXkx-SZpG0u5dbpyVe5wvocncwQjznwMwyIdEcnXCO4N3WveW3KwwSwTdLRq5C9Gp2B37dYPsiXzj7I-bEZuCNVGkoNGliU-eilqXmUMNPCqED6nm9-O7EMskadz3FoPd489yeeNW9S2Rt2Khig17siOugRcflXjk0PeeJGS23dhjUJl-4OqL29GAL9ylV01VIlvCmubCDaccGA-g3gq10Xn6vVSAOL_04yBpq-P3xfrW7h5ibRWIdzBcJKYrJeJRRpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBeOF9XTK4uvLJdIE4L6f4mce_tWYuxUNHMEfipjgIWlnUfpj02OPnKZYQiIr3hAkWwuaPw5OnVDgwQYtoy50KR1Z7AC7kimHrCPBeTqk0QCcRxPZa7WIf9cy8c7ePq2JP5VpkwJEIZqZcjb2-kNpbPqR-RByhjkQ1u0OzWb6j8LDaIDFdbvzEylkIj8BJS7-7seInAg4VKlbfocc4lSzRkM3ujvfkJ_tTT9yphTAV2Xp-YoPGx4yRZR2sjzWXvcktp4sX-fJuQ6dkBjaxhNoQAYAxNaq9oGTbMUotiwvepnxDvmDCSxg13C5wAm9jYbRirXfRJgotN1U3XDhpQxuQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=lJfTWvXUs3Jv1H8qWD8h2i2FvUQc-gOuvPP9oUBg5yj8wIpAiFci6Neo-d86ZslyKOBVyEc-89nlnHWhrr4ro72BgdVT9xZxsjKQ9CXM4ydSZeUZF0YLuTNAHPOu7xI_oD3bs-V-MK0me_UFrfx0fnirfBIpSXOfLpm1-K2cFkNlfQv8LJ8QNb5nzIy2YcM86YJYvK0rxMJ02QI1ffkZIiM48qfaV4Scn6bJ9QykWPxfOTJkE-fN0GuQloMBJYVJ_GQd4Xvt0v5TDj15IB9KMV-ajY1pqITDAvstA3-dkKJfC5Pt3p3RIzGd8hJIrmv64-vy480UtrRKazbdV1OrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=lJfTWvXUs3Jv1H8qWD8h2i2FvUQc-gOuvPP9oUBg5yj8wIpAiFci6Neo-d86ZslyKOBVyEc-89nlnHWhrr4ro72BgdVT9xZxsjKQ9CXM4ydSZeUZF0YLuTNAHPOu7xI_oD3bs-V-MK0me_UFrfx0fnirfBIpSXOfLpm1-K2cFkNlfQv8LJ8QNb5nzIy2YcM86YJYvK0rxMJ02QI1ffkZIiM48qfaV4Scn6bJ9QykWPxfOTJkE-fN0GuQloMBJYVJ_GQd4Xvt0v5TDj15IB9KMV-ajY1pqITDAvstA3-dkKJfC5Pt3p3RIzGd8hJIrmv64-vy480UtrRKazbdV1OrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz_l8BI_zr7qixbW4YpSZX5Fid2uSDGVfiTgPuuRWptDXn7E2w12VDBLcCcp1eBzQnEWMQ8v_JJEHomNCAtkhFJmTjzPVY24ZW8_Nr_0p0HOQR0xt3HdJwwqUnWmxsEnQdPhovO2yqbQdo099IGwzYjVawNQYaK2-Iq_w5bqzVlra6ZgHoSRca7s_HusNux3yKGVSs5fp36dzYnoY8-8095XhPD2mf235YOupZe8a-sBI2-7Akna7Bh99BEaf2gyzQ9j1B8-m8teGiJIMt-0MVJEKBZ8yO5KKObfAzCyx_Hfm_0Hi2_GsXVuLLrwQXCT-mUIGzkYWrj1fUdije1zAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uq02wPZxVQFMNoYCykmUYmf0amv1JTfwMHxm5Mh4gKUXw_woCs6R2fw3ypHYvZGQ9PuMhORN5_TFaVv622pObjfAtMaGWpIx3ittZxO9XvMPL9vSs6oOiJHSyS8rsrmPk1BfLxn1ZW2sVnpNrSH_K04FDqhpm14uNvLMYxIzKTjeUzTnj5mDNA-q412hzFzvH1hfU2oL1GKQF95SxvMLyTymlhKvJwiAJ9tzejR3H1Nrs8lK-WRnVZP3MEVUPV_4fIbVCzOw3JAIy5Lh7wFdwAtecEpnfZmkMW9KI8UOeZpxdKRP_vt14i3jVNwFnt0Y7RNXvISbwMx3nj5UQZA7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScVdi8kjKfYsAxqKpVF-i1_83M2NSgyB_dvKKR93PhFjnpVZUXXclLmStwY0Tlii9GqZ7Od9v1C55kWjtbZ2lHmV2oNRfwGiGgCnmRPmaRhGgZ60C2NA7i-tWFHwkC4jUbD56bP1q-oavdblp8-zRX-urF1H-iBFthZEyeLhyKlvDMMiYwV2lcGL2wzIK-9QXqJX8vkCSHXo-a03Z7iyxj3vt9bjQJDNEP7iGc2DxsZIWoUc89nhb6jX5GZ1SUuLPvn2fVp4DiiDi088xIOeunXYgrTZpPJKEp3dim8lK9GsV8V_Fc-H9OTXCOxcd92YxTshyM1gjI-XjpFz0PjzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F36xrkom8uoG1npzsHZz1kD3UUAOlty9HoOtX0OBOPZDSlzMcCb-f3XflYQObr1YXYxcZ7mTsORPtacHuWNS1sK2hocGoAzxKKXAiVITYVVYYArx3ce1qJdC_tzgfAdbnsshrm5lMwC_brQVgqUQUQb_2mJaDKk7gldxYpEhaSes_33PgLCCfF3CRbel0hRygedQgSJyMIjleP_NjMoL6vrCEQ0a8aXds-7TOHDSOiMNFAMfZNW0pp88ozCGE5dE8SdoHQveqQtfMZajP9iLPIGv9XTfR4hK5g1Q0aptKG6YAwxnVpD3Dr-Ognhp02bVm03ZsKzXZEL94zn3CWih7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpT_uHR5pCgfca_c7uigBqPpMNs94JiKL01Aeb8-td0JN1H0qOu1s2igYtz6FE57ypL6n9tHyBLmv_y5w9Ow4lHDxEqLU1oPhWuKn6epx8XZzZdVVfhIP_Y6eRjCsJXYAarz86jQ7v43guz9sT8vqsWrRyNJeujyHeiQH8f6MltoMuPFGm2FJgu3vlpIb1tM3bjUeDvKiNtlmtYQdBvowN-Af8BnnW5dPw3Vf91oP22J2AWXxnsyc5xk_CqbLv4PdQYTc902lyfhp2B5_hXN7iOHVNL-h9Zb0jfMjw1-cj-flKUI9_zsHleJTl4IYMEfTz-wVuN5aNGRJ9qhp7LPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMxCj2jewidYa_LJdquUS8R9Fe6igVY-GkrkArO27akcE1wHYTOVSGncDM8U-qk7tqiNOxeFYR7XoDeL-PlvfngRTrgDImlMTlNowfqpQ2ZiW8pRn-9wrtDQa0gAbrURZu-V4HGgbmKsTt1tuE_Ypt6kfoNu6r3HIXcb_x7fIEYTwgrNpTmsZZYoh8nxWspUYkZACtrQNnCbdMszq8BQtFKFfsiVd5yqFWhq5jFvEjGno5Fr7_pauUSUBDKgSatuBSgs5f6RHuN8cg_DCp9Z8nULw3D83U5eV45B6y7oXkdHQZrdkNqW0hWe5J-20tuoC8-PTOHvrtq6g9S70aS4bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlgNEq1t86ETFBG4iwh2Mk1fLYK-lwIbg3ZzEgYy25JaoZoei1JLduMVK3rxlv6ISZbyciTelJoodedQV0Fj_C5uhWYMrGgvmBS6CeI4uVs8zCeeOWXozS2wLALQraZ4HImh7eTPoDZavRgGdmlz8pSZMiRW_XxflqctDc3QNh72tYvS0yP8J0Z1IdMiYGq_NyBZggP30TYqfaqviVIzCTB5D2gke71lFCY3g_KOCzlS-T_OdQnj8dpXL59piCuVYaNrbAvZhl5y0-nTCgpzT_4zIWwxwpTe7FNhOq0nzx2C8OZFx5dTCEGSBrWLPAejfgU3wXTUr22ORFI1YjQimA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=EHx2Bs2Xt0qs-Z4ReftRJrYSS3DlQJwTRbPSehWbmrOwEKag7AwuUZhDlwn-V1zmVjz08-4OI0n66ln7twh6i1ekVuqFhuD-ikHnVTTnX-x7uKtbBvGecImzwikRXcS_H0oFvFxFDhA4FxIwe71zpFshFvWYppwiw9dY5lVuHuaW4LMCOntAy5W04jftPjMLys6kCIOxUSKB_5b11rKGg_yvfY9jIr5D1BdhJlfmqJbkRGl387uTsmpydjhty8OPNlXdFxsierLuBNOXUF78_eMiYV7YM2_fszRb7SW5KSoD289mnbjcS2yev5m8DHbAxo9T02ert1Y2-didBWaNgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=EHx2Bs2Xt0qs-Z4ReftRJrYSS3DlQJwTRbPSehWbmrOwEKag7AwuUZhDlwn-V1zmVjz08-4OI0n66ln7twh6i1ekVuqFhuD-ikHnVTTnX-x7uKtbBvGecImzwikRXcS_H0oFvFxFDhA4FxIwe71zpFshFvWYppwiw9dY5lVuHuaW4LMCOntAy5W04jftPjMLys6kCIOxUSKB_5b11rKGg_yvfY9jIr5D1BdhJlfmqJbkRGl387uTsmpydjhty8OPNlXdFxsierLuBNOXUF78_eMiYV7YM2_fszRb7SW5KSoD289mnbjcS2yev5m8DHbAxo9T02ert1Y2-didBWaNgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrjefoW9RFu4LrBqsp77Z-WMpgVWJmyaIJkiPKBtLtQbCKMPqnEw407pw5c_ViSK0TriZ91dKrLWnhZsFeV87y3FhCdgutx-p6b0FGSoZhdLJaBp0nCZ8mt2uVrmJEwSNdOZazJRBmg6hX03xIiwxRJK_5OGn0AaeHi5YKe0mtjvqhtIX6lLskhIGNVeYouBhva-Q-nHzNBcXwVUWb0_aI8RjbPq1hqAmpLh3liAUCQ2wtHeUZDQC7i8caR-SLtjREHez8xfw8SxQfjg4dsq5spFqI-icB_TPkpfget97_tkEzHH3X2n4ZbDRwKejnsjjHkqwbV_mZu0ClK0saOnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHKaG51XkgSuUJ0zyeMngXaYhycRn97dcGcUQPnUVKfh_YM6X7R-KoRh8uyJQoJ65Q7TLnBIcL_BUwBK_LC8ej5LHqbfucpS0X1C09vZY4lj6z2F7OgTTU_22_Xvre8EJiopXgu6RrrLYPjsXM9gn8uKoPhwG_sHNGYctMBtc-SUgKdKo0Dk4m-CRUVbuI1H_5aDqFQNWJh9LO7HfwrNcG3wtRQKehQ7xy3e4grMKIZep07mWcMh2CV4DY4QzjipJpINGp-5Lep-3SRxP1mOIngyUWVwndpdTF3UhNz6rN7KnLTqf7ZV_rM8vCu7H7TvosjvBd0nGGZxYhvsMsN8DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpLl1bTLKFTjd9bK45PsQH7coYzgomNV_M4HPSMXI1qZCR2L5k-EnRz2t-IbKmR8lhfFxv-1qvAXk3yRdh1pVJfP-CQb_GSyN1rCtalhRmLu_aPfi8yf1DkFIyFTqWGY6CDb72mEEiC-3C6iy8XvevQfwOTFR9zZKqCWAy-oC5dDPQG18qZjuf3NsPUtoyoc9kPMZ2viJy2-vif7NcFaALDFHB6ntkG_4kiTlx8sp83huDkkcJ7GrltlCHN3Po9ZI7l48SSwTNxqYJPwTVv1KXAe07dRSFJ_ra0avy0Yd2Xes_JRO1u2MPv3KJKIm_d5nsNu81HaDLdenwgAQPebXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLdwzZYadqDvfikGEys-uEWaSDWOHciagoYPZmnfQfLTkyD4mGclqZRzKufHa0YFhm2OlcYNKU0hz1u2U2UJlyMwRd7p6I9PLeH9hmKdBJVOdDjukE-QaUJ9yJxnq_1-aAum4OBURp-9WJeOYt0T7jLwo8qAhT7SlecUoGfX5F0wiItc0C8gtbzokxhKlsdOCWA964nWZhQncV3t8VPD-PrY9tcSYquOilkcfzVOxZ1QL_3wGlNdeRwiVW0USC57_78CckS3BOv-6Mz6jNUUeAFWRWbN5eW5hksy88EGTpHVYtNWjhyqX_yIl2pxu2l7M_iowfBRrUtYrGnXViBurQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EggBhDPw30nQgWer5xBfhUvaJp_EBwYilO9lszp3RMYwZ1A4_EUPCQeSTYUFKPECIrmWuhIynm4TSZBc9DcFhP8q-WfUQ962gqv_XxkR4STxyk8zPRb1bL4c0zWUGxSGKFsOLlr4XBoOE4lrpGSCyLilq900y8IWV1dqF8tEeSkMTBTL8Pzjw054DTr00u0Z4u14CQSgqH2IqquDN7yNhlwr56pQagBUseEucX8WPZVzJ5wRSKz2voo_Foa5TFKwmrwibsbsuB1KTUt-pBBN_9WiXSrdIL3u4teZITqDQQaBLocc_A2lFuDq5ZuY3FtB10GUBWN-C48FEfibIV8lLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyUXLnARM2LxgxXH1qxfQ1zead739AkxyAYyjdytFTXual218X7aQdUR_024viSot_ZaC5XGJWZMbJCHr6tFTH3DUeOc2JSnEpZ89dNX3p2JynSuvzbkvyDVcOSIhEm1QBxW7SwwtRumOLwpOHlIj2l6srwo91LceeCohQoziJGIZ6jbXXlARuVg6ufeufkilb8KxzstlDOyTHCm_bRDr2-_RBWDIGzmPqHmzRp7l4CZgNL8AqxO7zJxWYrgni-5hWHHEwPk0S6lZWk7122_wJ02kIU3BOgKCpHLYIrQknyL2hOyXSJxL_pxA9jDxD-tqrqhEUK4yRkJmVatroa5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e80ZgQowKCqwrLciMn_nEN0VKfYYLeYDUMKoAenHozsbE0U3WZclecxPsgu8nEg5mcCJLYoeuc_yqYw7FWA-Al0DpXgTPXmqrZkLOe3d2NXqsnWEwR6lJrBSYhDkfUyXVT7JRocgCwv3ejC_AIOwpEoxVlUJMPpKEu6Tdz0WGKCwxPi_ofYZ8XaH0nnyn1IwuJqIECvq2JyN8AXiBN_En8wIf4jvZD1UBqOCB4ubiOyN2kYAuW2RwuPbuMieTLDRXJWGRzxsp8iV2nE6TiDqIXi6veOPlg_evB8bMuyIc0ZrNDTuNtbgBPwmBBmsOHCZT4txXqD87U5atJp2Q62IhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EucgXMbqwMIrLIRe0OvgU8Ag9x4BAIxAuxgh-FrdocDSAYiXNF7ndz43nSeEWQHVqodxTRMKEfo5I1gqo6LJkmJwpujK1Tt8fQ-tr25xHPr0kR7oda-hgJOh_EMn90oTQUWLH1nOlGD4UWKWQOPGYKuAf36TJ6Wa5ml49LV1LKQGFc3wBie9yMtRiEREIhNmG-EjMuIa-7KACYMBRgoIV0NCBOrgqBls_00Nf9mrnGyvf7sUa_aOQrSngAvpd-m3zka8Zbl2siEbIoEOSIWkDl4lzKL6ez8STk2K-LSRbbxWqZCrfQsvsl3kFdF811C8B-do__cDtIH2L1UCQWLzeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4jT-tDmMm-4k4thy7L1yqJMOlG-Vlnatj6vCYFMsP3Sj3YMQnf-03462yzNGzgpG42OqqI_WEZJAVGF1FADF0NQqUm7OsxdMlWcgJX-SyAjFdr6I87eHmYGwGr8izWEZ5W13nZrGUk5QsP0UdqyAV8wKEJSTZE9InldjZ47C04h0_vOmTItUo42olnWT2S4U9FZCG7pEJdwTA3oZZTIpk7jOQZ9zx5V_CAnpAsZQsaH5qhnfoRoMoQVc3Ai6dkgAnRH71WXeIZ6BdgjccEaxfUh7mmfomvOS19cc9ffe_J8izV-0azP5mm0Lz6M43sblRuSHdrnF1GkiprV3QNBJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=b29UeRoFX0LGeMh_N-u0sxxtjXDe_-SKDe48nUkYvP0yvtkSfqe1Nmb9udr9qTEowl7Lu3b0Bg830gr9NInouYisT01PfM2p3CL3GaJ7Fpd1H_vj39obL-ZKXNqmRHkn42znEFRp7idVwUeDNkakncK3W6Tvia0WnJr3I_u25g8iCC7on4c3vVyVKh-WZKnZc2aYvFmUPnsRleolcoz3rJUJ9oUjJuadp_VSOw5rc309_3Fsj_35Kk84d3_HgdYQcnSUSzbRI3EBAECGj83I2_xNERRSB4FgfRSZfnPag-rpf-uP1QEFhPixYyRMIRVdA9M7qhxz7RFKlKBKCrnzhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=b29UeRoFX0LGeMh_N-u0sxxtjXDe_-SKDe48nUkYvP0yvtkSfqe1Nmb9udr9qTEowl7Lu3b0Bg830gr9NInouYisT01PfM2p3CL3GaJ7Fpd1H_vj39obL-ZKXNqmRHkn42znEFRp7idVwUeDNkakncK3W6Tvia0WnJr3I_u25g8iCC7on4c3vVyVKh-WZKnZc2aYvFmUPnsRleolcoz3rJUJ9oUjJuadp_VSOw5rc309_3Fsj_35Kk84d3_HgdYQcnSUSzbRI3EBAECGj83I2_xNERRSB4FgfRSZfnPag-rpf-uP1QEFhPixYyRMIRVdA9M7qhxz7RFKlKBKCrnzhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMmH5XZ3A0YfzY_V0oz4NPhfzd2MMoI1X7wRIGGRBEN-2vMz9GCKBmiHHr8p6Cqjkqh67DhQpsCOwSdBnPTqz6M57uzoEc6eGEB8WKzvK3VN-Hwf-4dXsmz_-U479w1KDS7XoYLyeDDF-PAbBldpubcXlnoUEgNifYkH37ufUU-sgRN-XwVxMM7rAIDd9QlwEHIqEDDn7AQL2r6DMfDbf96MYXWqL0hWa6BauFwBNAP2XsSVnWHW4KKYQjk8zk3BnGbJ2penOy51ofJ-htCwjxhIjdtZwtQ1Mtd0MY0v72OxNOCYwUlIadBtaGvcay9RH3VfMlj4j3mMADHl8YIwDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGAtZ9FxlYNjrL1EMOzfMSlhG5CsvD6Z3-COD7dUdLgD_uDAgDnbITV2YFismTbsb2w0gy0WoLKlNRT4Ymzl-YdSTm_uz3ovYW6sFJEa_LnVhTGzzVljE38qhzIykYz7khDffQz2bgdStDfW5Bpxk20vsOIU7Bkt4CNtexB7o_UxeUcoKAzZb30UWMBW2SbPNVw9Y2rGR7OcjQxJs8v82hwC3lxEZE5NG8ySODXt-uao1EcfO2-GRkXX1FjiWJ8wKYS7FAu0sJ2CdUky1UtK1CY7bfDSuyP3425ipa3dVqxMbg42EHOY_VdEg5NtFAmbyE7x-Vegntluyhyg_AjJ3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irQ0pT26NRHojt1umcEU8batYwLOtRVhjSyxCKsgQnKIBA4G7jNna-31nKS792OsWUPVnoOJroUkxF_d8Pb-3vDLDeKL9L7tZqCWEp7zYX-LykKqUBpsn8D8hepIBxP9Iv3bRhyTeL9IN1wv7eROe-49wEZcf_AQlVyBt8wIqAimUWYgkP4eFt7LDfhjopkM-kAdjQvbzAVrmgWMzXM9lbO7lJFJG124oo_cmDmxuF7dLsKdOYs2XMSuzmVgwOgNsnkoiB6JQQL-sYDDvijgoq-IrB2DZeXnF5FMY_ZI7XJmTp_0xq5GbSJMYJ278ugLU8JFVCzC8Eio0zHgGlYNwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Xno4oEQA5bA6Ut-iYU2AroxLXiwW80gwYuNfhNGt7NvBwmVXtDttnjhpl7HQFwGSRcN1H0VQIKASCTHDqm5VAevNXPjrbqIaOul2AowHGuJN731Tr6ALYivVMFoDHCP0eAkFSNFBHJr7FVK-VMMdUmH8w6SfVc_xPjAVhiv4wlRY0GbbcITg9dT2GHLk0NrAFcdl-PddIgMA1BJ_RQDBZoTSHogz56-UJ1HJiGOFSnkMlRS5IgBkShkSfqtImk56aFMlAnDTTsHcnsuYKV0MB2CBRGIjptcxvHr3c9MfF9W0QmAjqAQHK9mkUgnBiH_JlWfuRajJzUpM8aim8YlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4_FfayGSZRJElWD6ftDhojvQjBIveWaky4ZdIf3EHLdLa-oTCn8zK58NV0FlJnoNb8b50XMwoz7DhBL9N52Kg0SO8MnYtqM-lHtTbSXeVaK6vLt2D5zYQN_NIHvPjYG44VBWjaR6Ng2QVcBOBRx7t21mCXvOrFFy2SH_8IRh7hFK7g0mTXZLDbbQ0pHQDLf23suxiaW-lgAr-yEcbeWb5D0Lc26kLcd4ues5x0goAQB0rm7CLtGurVHeTjZYDFoa9K3jpX6yA-xmT0b6AKUTL2WOs8le9c4nN6rSWFc6luV2pF67eYk-N1D40qRIl83x5zu7WovsQDCUsR1Q0yaNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fjgi9yAtSEnXzFQyobK40np6tuuRX9FpnIEc9XR1WwfmlT7XdRM6oBHjqR12lM-FYPe4vVt8WaGoWdVFCVy6qifO8HGauCC_aWyY0VdBhwpCF4I_eQQ7LScSi2ttow7vZNTP8_8ydubM4GYZUK5C5vSlmOOpPVBrJxPQ-0n_Yrsoih5utOiJbSpfWuyTiLkG7wzsIp13jSI_gnGpY10j4tC8xDcw3Ggj-VwAsGH4HxMMkhIXE9SuaYBkTKfrS6Ga-Vbg1SGXl7NEn5irvJHERBj1aXpQkYnueUUBS-nTp0hI-ldDpzYBNjRhCb2A14KSl-tRiwKHNJWVsgvOIcHUeg.jpg" alt="photo" loading="lazy"/></div>
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
