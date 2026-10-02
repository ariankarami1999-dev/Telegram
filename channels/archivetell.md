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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 355 · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By_mwIKZaErkyMbaLhDbfIUboxJa1JABxg65vS3m25bRyz6ahKF4PpcA73mvLTGEJ7fI1W2Wls6n-5UfjUCHQjZWOmdYnYMcmi_Xahm3xUXaJdQPyAbkQtdAc4CPt53cz4xvAo00YtdY3Kb8eFYNJ-hRgfLnCD-_ZOYewMcr3J8sLBjsi3nCuzx2bx-7NxRlhgiheWkDxni_BhsfYGfi6p8s_zf8jqK46wzSxVDe7LzjUYJYG02_iRaJ4UDZ96DfmfgXpbxSyIRmbTCYmHFzCKD_K1a438_kXqvAqJEa8dE7L82QsvzOBiXxDAFSCw2jYj_sWoqyLe7WH6f1OrlrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXMPSZGepz6F3Ekm8ZfJq9pKDX0UJsCHl8f3b8MfI_dFoPH53w8QQfYZMSpOsyJWGdExUKlr_HmWsy3i4rs5i52CcXax9fqAzYMOQncoBm03n-EajHpQwyhaLPwEWWMyeOUv7uKEH1t4nyMp01QDhncgieV3tYlFElVXDyWfqrbT-PGqtxOUNqMd9BoLeR1-3KUhFweds0SIJZ_UGBFcBxMFKUm6qxrqT0W3nrfL6FTwY7LUPRV-tdcTVl9j5vB1zXJfyJ_VseX_k7ZlKGWs7c-DNavqH8-W5Z6dY-YcGBjwZaTTzro5EsNDQkqFnkLCcNcW_S7_kF_c08WWaOK47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKgs3fwLHnKcVoT7wszhdqQhJnsMHeGyCabVtDVnRE-h_wcG_Sl6LPlg2uquu23a7-GxeHqQnmBj-FJs6h1hUQmgwq1vHEdoPGqGA7Zp-h2ftCvS5d9ZF8zNBYW_0U1P9zt2vjECPIeAOyFD0w-tevQ9DDWNgCDld7QuHAHGENdxnsSdMNOiPg0aZ-WnfGfQJhxG_fqzU3o4TuV57OoeLepvQxODl9m3KwMaUx4dy-cNp7qE7DqrK64zwePtEvBwzj2zKsnZmTJN3oTUfedzIpX17Cka7KN9KJMRiC72rwB0yreNngZrQ0xhXK64DfFzNuE8YTEAGJeYphyNY6VYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7o_I_NToE66jFLsZdaUKkEL2_I5cARe6WGWab3X6J9ssLH7d1Wax8tvjJzjFtQYdgOzafr2P96_idSYZbe80iawaBl5RmvHsTWaq4JVMbyylBAPn7nDNHDQOjsCQ_-MqDrkmPWVdsZNuN2xxLigQsQzzj3LEuEV1sSpO2Fc6lFeDnzbGmQsxQSlMhmz1sq8KWGSjU8y8w7RtUYkfDo01f-5PsZrGfiOhLTIrw5_uNQESR3U1yiCUoWFGvE-5nPYT-S1TxsSO1j2NXShHxTWBsnpDehgm3km4P4iLfWfj_ywfBi0O_YpvmfLrzKMr6WhpyOiULPIgkZ5zV6QcH5x8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYhJDZzm4dIkOAYQXhW8fSKKOdC-YIT86JDE_WtbGju8GOa2z-mA-Le1Sf4xxXGVWRTo0pISicZFb3ux9bjSvtP9lp_fnzA7dHK9Y6ovY3C7esgaSJDRov-Zh3NchE1Io6T9UkcC3rLbXm4CMFfPaeqTD4qqKGT3kAZO7pyiWcmRup7G469BrjpsPiXRsYUOd6GL6njFRzDo9BJAnI7BZaFtyn-LyfifRYC7W4N5XRCVZ375ROnElBQY0p2631i7SVqNXfBtZ2scU7g2_g12SivVtX_O0jSLqYUzMAHUUjEC8XViJYhKr5Gpfx_4tNP0dwPwaFnIW3Vgj_MBRdDRRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIVaYpAnRpWADoFQ8DcdIjcID0Z64OJtrYuu7luH0eTMUKUAlNwYGwPLD4QB4xPjqo2qzUG7vnyZR9B-3Lcx6nnH7iHYdEVMKmP6irSObG0QWs1Ov-Owa9_cO8zYGbNXCKfDlgIJtYicm5ipNKTzotylJIDxAieRrszEC0pBHnyxgEeJekmg5_FP4Y5SHQNY2QS9k3ISMPMBWxUb8EJMZeQaaGBB_ylUXjUQ9Bz1wTpcSiVFGleD2wkDIDKb0e62NC46Zf26szW4uve4Ir64rWh56387nMxqvLKjY0L7ziWMXRoPRTfP7bZnHE9Q_DWZ2at0z_Aa5Q1dTpTe5roNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6mJmOvYnixfHrlGaqWWyrgsgnErJ2Tiv_WTroB5Z76VYuNND7irlDpqEDKx13NKOS9n4lepseU5G17J6T10RG6Sc8yOw9es0LuHw6Y9KPkW5TcEJREkMF4Y6pDegGEUyWAEP44R-P9G6BbW97vgDQosTsIStJWi-tquX3kG0-XyIB-XEEmZ1bEZ646uvUH29vn8xYvP-G0geO8g1JhHr34atx42nrLCtzXhjsNKffTfQosP4xtgmlQ5c0tH1akTOjiFkX4h33h1eW2bI3YoeA3Y4AYiaPwcA78KGiD2JKmoQjuxBtzX9RRuU1xI6b_8AUk663Fw2jPskUHGNpdGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUtI-Xgh0nP4F4UJsBirDhmDDtdFcFm2yqOYx3e2LCI9LgC_lNm2lL6YpXuJdxRG8IqJkGOji5Zyp4oOQEc8L4jUYI4Lq1WGX6foEWHYT0NQOlLWa-Fckyny3zrjjUHod9Gt-A4Ii2xIqwBeGBJ-UKcU-lC_i3GWTjnC-Qzmi-YD4bDinD1ljqO4vC3N5JCVTNSjh8Eyf2ml48EpZjR94qqEeIKZsJI6endUMNR5uYfQytPPpiuE-QGSnkngrx8-Ug5EOoUUBGtAjB-1igd-QQFEmTbdg5VMjRNuBBz5_u9YMMueSOwTAjBQtslxgQzNwT0ujGy8qk7NXzKnJbfiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj5vZgOQMDk8S8BlCcQ3R1pihMn-tMT8sDX2Lz1ft2yAPItKKnq89I21yFAQXzf2PJN5SFbvYcpv-N1mhfQXNJA05CxX3-QfYNFW4CDReohvWX-qS2MfHvk7WIgawSbnGvubRqfrRxGSCTxATzbK16WrC4CWGsv_rnlia4n_Pv8VdqjTD4hs91bR5Tc-cYowbwwRyfUVKKcq6CW3eiUTcpJUR7V1ff9NPVQ1_20rrC_TwcOmQNhOr7-snQvAPcqjd9cNaj76y9cslv0uY7bi0sEnibk4puw2puTxTw1j2sTzahvKq2bMrVv1Wti6QCdWThaHJcreAnVmyRt5dzV_ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urf8MkcnlT797h8q0u4W0J5ety7UavIXUKjvi1Vos9cEXWefdW_NYoEiSYgnwBGy2M6FTRciAaAc79rGtakWZ_ulubg2QI1_0CBIsUBZJSDEM-dximN08Q-gUE-gAdBhnGnnep-AzyoQ-V9MjB9ZIbykug5xBhhSEn8IOhZjq3z4yVB30Zfz91uLfSVLLnSbeljOvsZ_YUMacBmKENuMtFg6vRPmLOIBqQkcUVE5uALmg-kXwOa-j3BtBdMLA2EdxtN9OnNWSKIOPWw-DIKYJV0_xEK3oxh2M0qaeEbKRKf-RyIW-t-spxqieh9Y39So4ZsaKc6UZnQ3IVnT3_mg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3zVkid-WmlVm2J7a58uTbPDbpn1Cj1nn9s3fHAtLJ6eJAQrZRfEgxbWHo1ljY66EcIF1jh6zbGVpgV3Pb-Dtryot6GFK9O1S_YkOUSvLaDIowu5fYcIrJX7eceu_z22E0FKywLts5YmpKrKUB-wUzarWq-g3SkUpecS3AumQ-Q7vJolTEYNyzlokUA7OL_M8wuyNqIKTlx6x7nW55hfqJTfynF1y5lWs9M6pzCz7APBoREn-m4Bn8bL6gfpDy-rypLgeWlaWHpfzABYb6V7KEdhD1T7ZS0GZUwSOt_FmRlt-V0Ofx5vRFGuhAhW4EUiUfZxmcf-hAV8KQbXgOLT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao-tJO0WDbzXLaSc6Z_NBrsy93tiqH8eKZwnGkjOfg2_bAume1S7x7iMf8TK9U7GnPLsDBw__MHNk2XvydAYW7RIK4iqIFdV8SLDNc7pi9weci9V9jdPKFaAezEqGODlBBiOE_MwpZ50JyEDZfanAqhAOXXzLiKe2OKkXEMvj4nicscGhromRUnl14NVubVl0LWNMr4-6lGqCGMqPj2a58NutJO3cFu2LNJ8JD_b1mgyEDJ2d5LxtZAofLYFEyFng0P4Wiy9sTRPrqbXKT5syMen8XOPzthHpr1PLO-zWI1T1Ww5Lw5TahNBJVTCKqrfS3gy9_vDBOZo0YHqJK7SSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLY4cvBt95YY_U4FsOdFplFxfhhoWIjTv7qqFxhucrhPTgq9jETqIZ4-t286KJpZ239wQhwl484B4FtMghbaG4yEIQWO3q-hAfNMMGXVgNRg-ZgRAxcoC_GiW89sopNfipEwLcbJPSW5qegCswYT7nQ3aXgEVTyL7YkJCD0cfJFRhVNoX5AHvo0lnyBfBJdAtyaDIRRBxVCYqZAsLWFWmUXqw5PFTTr86xDeJZOu-0GwgowswNm3MhF98FvltLK71qW0g2S66SllidvSAZocdL2TAxmToaoEdV0On2njK3DPgMjgiWcUCwMzVuL4snD6nDebV8toYYV-IEozSr3jXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZat6Ylx9yCTh9VlcLgW5tHfERqYd0ElzbNjOPMS6WhOabVCrpCbrwJIr2VVpLlojz90jrRHxzpGOYk1tvoWlrwcvXTaze5BNlZpjCpopfwyXzvIMh7PuJ19rPK9wlCSExlgsER0PrpOGkd0_GDn6s_YIjzDz3h0-jz_rcDVg8p9OUsvJGfMJLp27uBwXWjzoSwWZHcsWan-OdaMxcHFxPC1cxdPwvUEvoXBpFkCG8fplWOd4be_ebjg-i8waKc3ZMBCnWO-pplsUSVxNQJgv8IPsIMXkV4D05Chy8ykeyY_Y6uhESNRm5zQofG6MGQHoJiSvUD-RRuwsDhlysyErA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbl_a8A7j1zIAOF2ZR1eaFWt1iElaYKFDc-LHEtq9yVphaL-bkAZQ15pUVhy5n9T_95p4zkRHCQ31e-kVuIySKDdH_yPp4yvYHwXCrKMeIOcWktvztr2zFmGWT2dSShRjtgqJsOj93kQDuPNbUDBhgiH2ncXF_VbHsOVY4MX4tXtSxslDGIf31Vb8-qa-D9PS1inF4AjvQNZ4lxER5M27rDvDOI2yalbFIgtz9YNBvJgGay7ZwKFXWTleDdk4zTzP9HEg3Gz8C0uyNcG4gK0Hsx4SV0by5uSNJpHsXJ66m-kJ3rEBDDPdsuBGRSEAL5uMaOok3EpeHq5oQKZktSnww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOvGeow6eUHjsMfhgxuojLwVXMESWbEr8tzkBVj6dPyvLw7NTwkwLCieu9k6yUPPAajiYlv1VB708gEwbQPO6aByro5fK94uTVAgHCJ9fZmWzDrhCJFdfs96odFwgZ_pGpRg5OsfiZem_xpEezjNGSooVhanpkzNPdAmtQVIHb7ekMlnPW360k5YtIvd89XBG6wZe4abcoaM9uL1lvFaZqV8c4XGd3cz6KQdqY8T8n2M3hUyOp6I9HMKGVhzJI0Jikya5CRTqQhPeivcGT0d971RWeKGDd46AqlG1NfbSJPcJsaXX0JZRscSfA0krqlS9rqtA4nR-vXIst_GR8NXsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQR6bDiTPoU5yCAlXUy4aZFB4EF_lYB2TujCwgK_07HFMSZQb8Ov9KpviykNpE1-T7Hy64Mj4YffnywvMDaA2jRMXNHjlbnQSfInt8esi8VoYG7gITPNomoD30x7I2Up1qEU1skxypZ-Fqc7c6iR2Zmyx52Q4XfYEt6fYHSIgL3nD72Rxg4VHzg3rMBvF6vRhBZqmPul2AS7qj8xcPqj9Ny3TZPiDhQh-m3qo5GNMgjdOAlJvn2d6JDEMdCmCSf1COZMRfxtzq_s4tNBdSUWTuMkmhnBibxF5U48qDAg4s2W9SAiL4oS1YxwDaU-9rh27_0HoQWZPz8JsMM9PN2qOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCQRAm6z0ktszuYM0FAsT9Dl1iffghuibPc8WRImiJiLBD_91V163NSDtNXOQRKubwJdBAh9hHCt-T1tzD51AqJhKBkz1pYygx4Mge7IFn82__RemPaITlA-3vR1Do74rWz3HRrIRhxtM0lcYKWeCSqC4qcVunZSywp1PANd4ZuMdV-KItejjhe8TseCyF3aZbwKKNrzp5xqrrVfYiRwKbuiKtIRnBg6FuDF62F-gP4RPVa-9pFEGzHJGZDinf3tnnTKR1hz-ao3TXRxe9t6F0T4agdxWB6eDDKDxD8DwjGv5SY35VuDHFCb09l6v51k7vGj1cO4y40-X9mtgDHCgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpkoFMXKt-y2bUiciimVfket35JG9vJ2ooFOgYEPswxGr4V9cxVQjTXFprLZxz59o2hWIxxkqkZlje7ekZIeVbqKg8R3SMvF3CGR01_W19uLTXDxNgPkTUaLZmgXcMJFfyIyA59zQJlMvscJp3e0ziABVPWgDuo5tGDc7MaIPX6R1YxtjePBI0EyKBpsGOBLgaWXtdG3jjYy9xjb9ToI62j5UJSj6Rdv8m8uLxQWszz1J8FXqzuV8UixNCdClxJEFZg1XmPQ6DwCYZvWWmCVx3KulDe58eS6j2voMAEr2ZZyEgdoMAvfzPekqIrj1isHMzG8kDDxdwqSIYQMfSfIEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-cqtctmk4FYM1rJm0V9MtrWXJMQ0JOLR8hSvZ2pbACnO6jpXeY75dmzuW_JtfgxGvsR_cQ4MIYcs0U9Ib6RTiSdTp8uCBYHmVMjFx00r9oOpK2HNINgj-BAIqjQbeDfOuHlXWIQjwzrZ5VSD-IpjcSk5WkRDodrwKtqEJVPhbBKC-FO3XwswoWvfeyXknQzMr8VwBW6_9iprxKkBxLmCi_liIZkf1PMCDzgNgg3ovgRtA1eqaZ8hnu-cS-Benuu2Opeh-6Qu6ys4Cpx2qLpFga259QtpDFItWdkJzpp_miCVi9gHqX3txEN2es-Sj6_Xv0yIJrW12U3CGQJg1CRWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQrolRvjFbeb1n3473uYiVGOx_vmg4IT0aE4uv54qAXJH8Sv0B6ZcR7DMr2fm1nZsWRSR7YvYeHjrj93KvJv2qU19b56bLua0Fxk2MrCae3S1Eypg1wTMlWXJwbrk0ExAcxI_JN7_rpuBh73lCs8WeLKigx--VrcT-Tjoy4lcbA2XWhinv_0t2MvEpqIIxjgbCh4FOw4tY_XMd27Ip1wBG-xpqrVilDwtKOlIyjhyiuBGLluLh2So4G963XQQ5pGMgpXa2QBjDJSSSWan4L128_hORj3CO9ZndKa0OCzNbtUrRDLsaB37-IT8CxuIWvfToLrLN_NpRoxRxHyBQP4lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjuk7bWBNhz9cyZqmJHuUzdFbw8hd1YeZwu17Iz6rEp-Xd0jSdSyQkRGFW3TVUfnaeBo5pA_Riv0qx1q57EDyTY6JDDGCIgf7vHaVIqSKK5Bz1-HKTKnv9AYaZVGuNe_oCMufVJKCYuut5vhjYm1yBTsi1woso-Ady6KCN6P9znyWkoh4CewmnG5_mERt83fkHFAdYagIewibI3KFgxJblhFKuA_M3C_aFebDRlbotzwTb4z0lcCq6PJ66b5hjH8dNWmt9ew9HFdnLjdqUSMog-dH-sUDsMrb632KgOkC0Phy-LJhhluh2hD5OYRW2uKvp7MtG0ILFq-1Kxr5f9fOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlgKIpsshHv86ngPm25fONuycQDmdYW-JJiSHuEEy4OzWF-jLCANlGpD1lu_StY7q7U80dVTuoII2ZRz3JtsVpt42RIxvGVcrljtcxZgp17j45iYvOrZj_sgcreA9-sgkLhEchMO2aYoFDkUB6RIxKHfHhYcWMJ0OgbLyuooHjGVc5wsOaQ1IGmrWKWOsj8eynCSrIrkWkgIHh9EizaxjXGoXSMNQJ-Z2jEriyEp7I5E_c7jRF0quk2DKis9o1DYQNml7_5n0_8rfiroo26ontIu86gI4XvoIQDlmoSYpe1mxY7nmjfv73lYaDsis29VHJyP5DrcBVPOmwDoJteV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anZNbQ2nD4LzyLv3XggmyJ_b96nVTrL6yotQRfBvk7GbrQxWsL8DCqUlBs5cJ2TOn7DuXceYBateLoPvR_LCcunQ-ZpSc4JkK1fJ05rdACJKZSrQ7bWURvOY9PJzpplGfZVlaqY6tTNc7iTRsPnnZdGFDG9_wk4jhYW8i2WniZa8jN2nJzYIgi58xIL-279AUMszj3E8OyJBl9y0jpITEQ3_wuZIgaAp4_dzSJwnJwriifvx_ybMunvSMNRvmzo-FQB3XkIDUC4EMGdb43DfJYpnrdeZVQ4JQQjpGIZCRV4RjJnkfEbf7r9G0_2t6qOo2n3UlMvO7PrmYqdouZoPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdyhrQpVqT0E3PtVZlAL2v1meBJG_LvU-tg3nFECc1dM7cI1p2H_vwqZcqfnfR-vgdc-h8mg6yBc2ZbqbpmQqA0Hrved9hnhXNYJ7sk4ZL2tpSlb_cBLA5VcE1CkIzOMrI1a9CH1Mw62WbO3I7kiOa861VJII1vapytZyR2ke2n7coVASt5ib4biRpX4DAhF2Ls02G6jqoJjKo7RKwvRyUAcfdfkgixSb4D00AA7klL5_9eyFYQNyYDdumHefotpob2fqvAYfqi7_XbxdvnpHSbSFhQxFAe0s4AQ0x6knO6mvz8_SnTiqas69ulZanUxI7Fk2z3UTsziLyyu2jZGJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=cIj7JddV9FYXhNCPb3vOJD5GZ60YhBqWWv-nj2a1Uwd6jE5bGpPrz6Ojrar6OjqANgpKXkGdXwgko3xWngkYAqylp4TonB2yNaY2DdCW0IoXH9D5r2JOE2c77SqPVA3s5WP8vKZ1RlypP9nFTe7DEYyA3xSaa6_5hGYaUe2h8Gk56jtcXahe4-kR11RZUtkpyBEoGfc7z2EkcEEpmCdDvNaOjUDmCe7HzukcNXVQvOa4UalA6VEZMec9wfILPjK9mUanrcl1f5aZns4v5lec3qWFuVF33SwCOtf5q0MY07g0LEI1C93ZE2dMt1gmNgydsY2HMCyUusaubJiTpHWmjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=cIj7JddV9FYXhNCPb3vOJD5GZ60YhBqWWv-nj2a1Uwd6jE5bGpPrz6Ojrar6OjqANgpKXkGdXwgko3xWngkYAqylp4TonB2yNaY2DdCW0IoXH9D5r2JOE2c77SqPVA3s5WP8vKZ1RlypP9nFTe7DEYyA3xSaa6_5hGYaUe2h8Gk56jtcXahe4-kR11RZUtkpyBEoGfc7z2EkcEEpmCdDvNaOjUDmCe7HzukcNXVQvOa4UalA6VEZMec9wfILPjK9mUanrcl1f5aZns4v5lec3qWFuVF33SwCOtf5q0MY07g0LEI1C93ZE2dMt1gmNgydsY2HMCyUusaubJiTpHWmjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqpnaGnSOslFay1QBMtgiXWOOXpMzKdOrNOgcsLUb-YXOJebB_1qPR1fiqZrL9CkxG0_AdMg1AqnNgKHtnBcMtKI7ZdiD8873rdm8NYVMCmdEEUkxZ6JVW3YQL9C9Dw4UOzCdiR9Ip2SaL2vD_vgMhUdIZHK2S8IM_yrSE39KR4KfmfohoGTeL6rxJl1_zrgapX6kmD6vqJsa8xzw1uftwbAAb_hDYGqJ0RL5Pw8gQSp0S_V5N0eF3N_M5ymr5xas5qu1Gd4bpGWF0CPKAxwouQCFOk044aEpEyVaogRrDz8iRekdlmLxa8YRtfttxVAHs81xH-z9UW1xqmsKp5ZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJwpnvc0ch7Vu1BuAFMoaB7Uzx-gkXp3UGVhrSgG5ktWGnJKivs_Te5UwCviaEY2TJ5ADVcwspmN24dARSWJGAPFwgGmWWqD6ovCufQ_mE4FewTMkMHaEXp4oRkqddeRwg4Z_fCYI_OH97ydTg7vjCJRDZJIrVG0RHkJY-Uax4wncTu0b07928IRRTCtEoWhMwtCxDcSbkpKn1iWn5CfjJbVLrd3ibrrqP4NawkFNOvlRcfNXx6u05wuVXtLcVnLiX5l3QrMZT0CbPuR34RhzS-G8fLR-eyN5KMkEetQcghrPeC9GpAUOifOhLDwctyx3EBA3Ec4yfIjXQZrPc6tAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve8OBKrWvwbT73QhbUla8OIe7sBxipttIDIUS2ooqZSJ27k-V-xmqgAoxm_wIzBbks1xSrqF1H_mVzJo7nskB8aPfAhRfouAC8dcICFFXuhRagCJexe_0gF-C1voRoylJWE-7ac6nJVV5h10XywgPF0gL99Aq7wg4LDBrTbPiLplAfF17mwFUN4JKfgTP9KPXOx6_tPTVGG-VtvVxVnRUu8SgZnxLmx9sJhi1ojQ_JJWnNoWY2bcUxGUBAW2iE690veSkJJcOjw3bCUzy76IjDtvV9OSuT-IjGwffg4cjvLA5nBxoioCk6i-FV2UY_bEDT9Pbv6n_puHW3hP09PlxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=H3FWi9B4MUDRQwCbxx5Rwo6k2XAlLrOzG4KTt41Pd2S8zvKiI0D22P55Kl_9k0oqRTqAujIk3pmbZDCA3YcmX267ntB-9L6h1bSlodwW2ynJkwxgcwv4R-gC-8X4oLptd0O2fjheH_x4aSE7MYHcmSOgYxQxnUUStgq_cW0X4BPJq_S4obHlvnYk5p_UiMKmiSKzwpZsvjImAm6sv24_k9lSwy-RWKuPj2s-7AqrukSiEzGmhgIwM_AApNw3vzY-B0QKN48mzA0Yz1t6ooAO_iZIPO5-TxsbBZwJFfaL47uin0hveSVVYTOKoX1qxZM7dwgktIDySD_9hRc8Nve0TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=H3FWi9B4MUDRQwCbxx5Rwo6k2XAlLrOzG4KTt41Pd2S8zvKiI0D22P55Kl_9k0oqRTqAujIk3pmbZDCA3YcmX267ntB-9L6h1bSlodwW2ynJkwxgcwv4R-gC-8X4oLptd0O2fjheH_x4aSE7MYHcmSOgYxQxnUUStgq_cW0X4BPJq_S4obHlvnYk5p_UiMKmiSKzwpZsvjImAm6sv24_k9lSwy-RWKuPj2s-7AqrukSiEzGmhgIwM_AApNw3vzY-B0QKN48mzA0Yz1t6ooAO_iZIPO5-TxsbBZwJFfaL47uin0hveSVVYTOKoX1qxZM7dwgktIDySD_9hRc8Nve0TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8oOW6LlKlKt8KYimv8VotpSQE5IWyaNkYV98UObZ9M76jyq0gjTWfQnaXoM6bY8PFOkQK7x-wlEeFSt1aFJVA0BOD3BqWobUgVs5NKDVIDj-wqaky-uUQbBQjBe27_0l3AZ_pL3bt88zUov1oA4og3qLg2jA993pg3ovvAIgl-h9mvJASVoUs1ojYXG5VExs6P4nlh-ysqcTh8aSZIggpfDpo6oii2ObIW_eLvHT9UbmYWpdA32hZBPP14KKPu3791xelzsbFn0ubjy01S3lQ8yO-E6Y7xP6am4nb_UfaRgsFGyswTisPe2r06xfG0LdkjMlrYYUll17wt3_xnAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKmrVM1pctvh1aetO959o9J9FF3-gJj-IRKdT1H57nzlgxFEBgxwBtY0UNZVi42yqx_bFX-Lth98-perbsevdmsocSdpEcvxMY3SiNKqmvFzPxnKF6yUbJMuppiuzeEw1rwiWTNkydFG1YXSBJgfIyqEcl5bmx354KqeO-8GP2T82O60s09DHUNzNcgZTOPsEruxh3E3AQMvFVl1hodT_oX-aPB-AFl723bwSSKKGR5sfP13uiJP3IMBMFCqwuAa6hOgXdQwY0tjefWBW4NMudkZnZs91iaVSHhH__xeT66iBg-uh92G4CvJx5OHqA3Jt2mJFerNnjroJ2IbEEyEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIJKF0f4w4R8xJtxfx7XvX2S85hrftgXkVS9SaMh2S_PXC2Iz6kfrra4MODnbqE2V681DNIIppU357ucvh0SpBVew_ZzAXh0rOvKU8_HxFSN5MyhlGIx8XEEMMQPG6HtD1m2XRb6rharL0jOsGhvEQ_OU7yjR-jW46_1nlTQpsg6W2WYkbVEjgXQ3CxyqfRLK5eETW-HiGCtEvumjOtz9e8M1noE8CJXZWiKhWUHzPKeOuuPcid10bolltIMbX27aEuBTC5twGc02gz-YkGVn9ejsgAzGgPDOsp9CfnX5zmk5cRq68YvPcMhzaUd64zrIRB_R5o2aVXjsLTuk4Rk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewGvga1VHc27emfmlFvfZrdRcBSyJ9kcFAGns3isKOvVZgSb1flGgTrsa5VOpmg24cL-gW8XeY1ZbxNChFrP8V2REdOPl9Az82Jf9lxv_7XK-NMZflY9UoFNH-oXJPJXGfR1WP6i4qpxVuhmCK1USN7Z_72Sj5M6JL9m1R-4nbwmHIvzb21chHtkerOV1jox7gRK8EIpUmbgZ6mYiAkx3Urv3hhQl1QE8dIvM-3pMbcIi3zMPhiyaoCxiEGGKrnHHhmqr7GKy3t0LTxM0bsmfsUgFUiGx0e6v5mXXflZGHWaGMPAJn03n7gXpWh6rh8VZbZny_-xdwKNEVFOd-dFrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpT_uHR5pCgfca_c7uigBqPpMNs94JiKL01Aeb8-td0JN1H0qOu1s2igYtz6FE57ypL6n9tHyBLmv_y5w9Ow4lHDxEqLU1oPhWuKn6epx8XZzZdVVfhIP_Y6eRjCsJXYAarz86jQ7v43guz9sT8vqsWrRyNJeujyHeiQH8f6MltoMuPFGm2FJgu3vlpIb1tM3bjUeDvKiNtlmtYQdBvowN-Af8BnnW5dPw3Vf91oP22J2AWXxnsyc5xk_CqbLv4PdQYTc902lyfhp2B5_hXN7iOHVNL-h9Zb0jfMjw1-cj-flKUI9_zsHleJTl4IYMEfTz-wVuN5aNGRJ9qhp7LPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA4a1_8bbhhl3A22nw2DJnOStort-HMO1mlR3qUnJ1iHN3oytGyuuypQsGTF3ySlp1SXOogttZ9pcigu-FCAcVyqzpgjRtRDr1LzGIO4LfJZOpWlxMIQ0Ycp1DzyN3c4TbpWYhhl_Gb2NfAnScU1B0GpFJhbgQGjpCQQFgblswmYwjBPGg_-cEmomb978RSbbQD4YEB3_Ha6TQc_u8xr--RA1JHxR-PG-hR3CMdAy2zZPIcSyUHolLCe0RpTMYAaZ_7OxQWOSact8WmSuOcl8eFcxbkhVT5o_uhgLZCgEZXFRUUtku07QG4NzvVRssG27yWzYswAXxjCogZomVmzRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXAEyiqVwapFcRkLrwI0cjAgZnMp3F4ASHcdAa6GA91H3--gZgNcKdwXZHRBLMdfMsUNZtLfVxowQ1oJt4pFfLGjfrQXjHtIACLEzKJtbG52OZXCublwz8spilNgsy4_33_Kltl_gb7fhRTY9pOCJg7G_99kVlV05Rh5ztVZJCVQuZGpjWCjFWTPQqzaW3fGpGfJOcGI7dvw_5bVcJwxs-VvdcMIndBpQ8LPhu_QDGw6Kvrmuv2z-k9_i2-FDB-b_brAPg5cgVzkRBY7uDxXld1iJNSNffESkDHnhBtClSTggKXZrkfqxuUMNxDXX1-OtgsXN2g_9Sdzk1SpKq1QEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=kV1BCI6WgME04ThflVhRS2DyCBIhRB-gqyM3kzWtFZUyRSZymlgC5cgqknteLpBEzdaviAGe6kU9QB99uN5yHA9LLfcZFKO837cAUm-xErnXnXNMHwd9EcDTZz7H5i_HnPUGhKtZcBW4JYeBnH_Kf7h5z3rJw1VnOOQhLpI2xF_4YhFoDVcrUEvTqN-12f2W0q7-rWbLQoGib2xz1xVjEzvrKrswuwek9Ip9IwLwrpf1RWKrZnF6sPd3o0eUtssMIYQb42erMZ392RbdIlwMgpNSx0Wc1knLNDmTjcuoBH6H5r_fwPRkhTHDqQcSIeqyeIxdQxMX21fkc1lAwdPuKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=kV1BCI6WgME04ThflVhRS2DyCBIhRB-gqyM3kzWtFZUyRSZymlgC5cgqknteLpBEzdaviAGe6kU9QB99uN5yHA9LLfcZFKO837cAUm-xErnXnXNMHwd9EcDTZz7H5i_HnPUGhKtZcBW4JYeBnH_Kf7h5z3rJw1VnOOQhLpI2xF_4YhFoDVcrUEvTqN-12f2W0q7-rWbLQoGib2xz1xVjEzvrKrswuwek9Ip9IwLwrpf1RWKrZnF6sPd3o0eUtssMIYQb42erMZ392RbdIlwMgpNSx0Wc1knLNDmTjcuoBH6H5r_fwPRkhTHDqQcSIeqyeIxdQxMX21fkc1lAwdPuKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVZpXZQgXQCM3vwsUv5Wmcv75ZaMvURde2OTvpMo8SPS7hFmxdZ4_6l8Wh9_1Z0SwJtPGQZzvWwuFBorfd81Z9tObD2rwqqfZtL80wXTr1jb3iKL17JPi_XKEFh6bGgcH2vXD5-5Bsvpyw2hhDz3IC99rjNiQTse6Gz0QNsOnL0iQHUilcga42gwyMVr4Fc0sjWiG1yGeeT26COaOONkfSCJI63Y1lbH-kHZwKY6eNS0sAn6t0DOjvyIhpEaC-qbnm1Y9oAonC8GL4cOaJ9bL1o5WPz_S7RTuYjy_Xppn9snwV6trSPukU2soj4jnwcmW132uhU_w--w4yf_14w1bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNsZZoRH8KvXaQlHJjXLFbc1xGsiPXOWT05s4bBpI5G-Es_0LTmI5Tp1uNAMJ3nUvGcx3ErdMDJFVNzeGsGbvRBUUN6WOLdBG6Q_0eQmmSseCiVz89wJGbabxJj_Z0QMALw6q0t_D-4ynuggJTCZslmPszI9seImQWmfuJCs5C5LV5e07q4hV6KfM0rZKUVcj0yNKoKRToFZZWJKT1a8Frdm4BSTYKWcD9KwzZseVp9XsmxR3ITEazY1ojIRwQlbrhRSNSraL8A1ppXlxAlcUz7Tkx-FQY6vsWe2BG0eLfItJ2b-4YVOpDgAVp1qwY3cR6scWoIqxZobEW1HrXAcpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnTIMIn8gb1n7W6ZlERFpOTnRmepquew61OkeNSSQgOqz1rq3v5qGxHs0TONih8dlqi4TURiFGRrdOb3fEtCNq6wlwRgrev0lbYgqZAdN6jbhq3iHC5VA9WaiyERXXnXeLDRCs341MUIMLat3bX4akTtMUI8x2A_sSwyNYlpZlz3Je5DawRFzdA7KqT_0q8JOWpQyDA6B9vCAkKDik2p-vrPQ2p88bf52-Mp1H_gSy3JcmJW8-P-WuJ3jL0mxy7F4crzTXbDuT_TMGbHl_dO78ryQeCRGKvam6lsdeZYJnyYzv36NYJdeJj3eGkZJgfbr74M5JFOd3vxXS-ovb-l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWVrG5oeAkyb72_EvbxtAzkrHOx0pBiQAGU8tO3yuHXiL2zhJ4bYjrFOrjjK1qy2u41niP90uy3zpAaaEeztaWnP4iOBWAg6uhRs8RvoHcodoagWSDfDfYBJLM6cMm1UfLLs3bEGz2Tdkvy49nODqCGDTgDSU50_1-K-DGzxZDt2ZMlF8sk4CTRBNDxSYoGOJNbjzwhmBJ9__AlCcgr5frGg_AVWabAlisr9niu_A4VylNfLVRHDAh9ywUsMpm5lzkwtwlb5ugSF7GQ9gu-nrar1Xm-SPFnITSElJ6wue_Jb2lWVV_-fCG_nufoyHO_pUxTd23YL7pHySALr9o7zog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXJbdH3gww55HNpNZcbhE7kYlUkcE9YntdwC-9VEHe0_jQLsq2kKrk3iBZANZDKpa6OurVMhE-pM92tUTTl2BrZS9liH9ZLna7nQ1eg8ahYonqKI8Cx-YUo0UKexNsql4h9UIPOg1sWB8E1L2IgNAYvqh95sjbWA3t12JOlAy-46Ba6oha68SOCJG0AcdyLobXxHjgoBJvtTfC1y5nypChqsnoJCZjotUaOqsIhLcaCtwlH940bdyLmHXQPG0zbtZ83HZx7EDrRg_Z82p9XubnOHv4EEgVXtr89Aig0dqsxxZsIoVkO67g4H5dr5O3Eu9Pka_-64FkBZXfaAADQRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shNLRjHJ7snj6sA9m7JrK2QP5nrED3hnXcARiOtJMYku__REWd6Voy2kcj1cVfBrk25bvdhinQpWPZPh7UL-YOn50WUZw5ihMIATERkCvbDVAEiSSENzlmFCCLTfkkHFNnlAltpI1p43mp2O3WgZobsOQ0Q_pmFYmnPPWZhmBEDjiLSpMHjWHBEXSNMWvFLNEBKhBo-JkQdV2ouZMD7d8SAXoghGcwRiNfSvAoH8vCAdOH_O5KKCv-7ornHX_4QhI4edBZ6SIOLa93Mlp_diqyuvKWzbNwvR6OLhJ1cp6BJs-zSb7IPLdTRTMwR7uvg_VQ7bYiz04UQ9nfZzv7518w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Uh0nl1DG1jA4Q-1Kl2veRU9GjWCUn7qWnQZyPccrs9CiFcxfvHSguPPmcGdV230kV0n0hYJ918Q30JTAT-X5-JQmTuPZOkKBtltwwKFsDAUMH-9ykk89casrjrsX5ilAZeWpQyqZNL5USWLQK3HvDaLTbSD3yxTm_KXfsQ1uJC6VH7xg1jPSdtk8YdFFR3taVhNCaRhIFiFxRt23c28wkne-c9sJUFGLJtAMd8WOxdAediIkvRreLGbVEo693xQEkjuqKE2HbOk_Vx-D5-0Q1tGMO6pUoz8OfZhTRSPY-PJpnquYqQZpiknlE0HEAi4NMjLDtPgPXwTt3CbyK8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4jT-tDmMm-4k4thy7L1yqJMOlG-Vlnatj6vCYFMsP3Sj3YMQnf-03462yzNGzgpG42OqqI_WEZJAVGF1FADF0NQqUm7OsxdMlWcgJX-SyAjFdr6I87eHmYGwGr8izWEZ5W13nZrGUk5QsP0UdqyAV8wKEJSTZE9InldjZ47C04h0_vOmTItUo42olnWT2S4U9FZCG7pEJdwTA3oZZTIpk7jOQZ9zx5V_CAnpAsZQsaH5qhnfoRoMoQVc3Ai6dkgAnRH71WXeIZ6BdgjccEaxfUh7mmfomvOS19cc9ffe_J8izV-0azP5mm0Lz6M43sblRuSHdrnF1GkiprV3QNBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=mxfl14hUg-jW8GhZbBcW7ybMM9SyUtLaekAG8Jaiy31vDBpLixDY1YjJvMrk69vYGHsL3l3m8ykzgNb5vhgBqnA7NmEJstUoJGMOxXQoVN4B4566giqMNdP7nfc2u_OX3-M-71zIvVcIg30yV4hGWUpvTaVkAQ0GAL5VsxLr59-ZxJE4ywH4C9d1CbeCZqaz2qMJZcILG06XXyv9tcdWLQnl1bVXvVI5zzz41YgHKlylshmKOJXcKmkBn3egFV5chCGXsDc2tQPYZYEo1-tqgyfEOi8gx016FfFQJEyCDmU3_VfyZ1UVJb3GXuDfOJtLK2WrgzJr3PVxV0Q2kn443Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=mxfl14hUg-jW8GhZbBcW7ybMM9SyUtLaekAG8Jaiy31vDBpLixDY1YjJvMrk69vYGHsL3l3m8ykzgNb5vhgBqnA7NmEJstUoJGMOxXQoVN4B4566giqMNdP7nfc2u_OX3-M-71zIvVcIg30yV4hGWUpvTaVkAQ0GAL5VsxLr59-ZxJE4ywH4C9d1CbeCZqaz2qMJZcILG06XXyv9tcdWLQnl1bVXvVI5zzz41YgHKlylshmKOJXcKmkBn3egFV5chCGXsDc2tQPYZYEo1-tqgyfEOi8gx016FfFQJEyCDmU3_VfyZ1UVJb3GXuDfOJtLK2WrgzJr3PVxV0Q2kn443Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6UhBPzggYD7-6KzSnYiDTSgEK-zf2NjBHRYD1X3m4wSPNE0IrzTNb8576V3tEccnnHVC2Mqdn0WereG940jGWwev5S-eZwMFJP8V7PpbA7U7yZfRN_zMWYUcBFKuALI1NIACKxAua4hm5R4pWJuuzD0Vswdb4jSXmWPQ3Nv9-FvMEB-rDtDn5cPN1QONOMrJgN7Z5KxEv5rEc43bkbiHQQpfYBERDJBMsrMuCkKfMVniamLfNsmFsUMH_jyCoJA7hI5SEkyXyiuGKfoXPmvuQMthhs4lF1K2XlHhpVYec72kH7LaBHNBH0sH9Vn5HVTs-CiKPSc-WH3zXOXsSAnXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD0W2fnaHnFbxOw3rW4UdgYvLKh-57Z8QfdJU1GfaNSoFcSWHVX388mvx8qmXFu512q006KaxMoozzXIf3tociYnD_ZCDGgIf0AlByUaN9k1evGuJyKmS4rglPPIcG8XMkzF3xMCQvJl5d6VtoIGrp52QShlEG3VS9_hSTMlXMfWIo7CbqnTb8O2NOjuzZ5iiNx2-YfvYw0KwXKgxKORKRASKgJ3BaBFdingPqOIgQtqMsMau9BzJf8ixwTlqJ9sWHOJYOlcTwaoDlWexU_wh8LLUV1xUerlTo-wWBvIMm_xb8lWJ6ST1LXsP-0atfSKKoE_mc5qwyjMgsJvyHQgAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQsJeRVYyz6z7-pm-E4kWRJDU_hVKLEBNw5tkm5_HsX2QzJ8fA_aBmgGLRMw1DZJMHCmbWsElxZvs-0upLACkPAuMueErvRa0D4NiQ-c-pGHjLumB_QFcHRbIBRV3PTM6y4XCqqVC7kPFSwemd0t9ObtrtvIZtYQZxs7cHxTFusX314nMGfki47ijtltpsGNRStmeQJNSp25vPn_7MA7p2F39sHdvSznygV_HWdwJFvaFpmtxDGYss6A6btIXWl5ke4jXHAsFexiBFmBCtukRQBuxUsUJ-V7y15wepuYaPdNvRgRCEY-Rqo5jG0dRf88qmBmkWRAH7lAqrvyDwau8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpIfEvJi2wFoHRT8CaT1ZVkuvi5exMV-I1L8ALd04DhLQ0rCJvpZyJPQdFuvjzyWzyenZo6yn3wQ2TSYkbSULRmVVkMII3yOa5zVS4Em2p8CocoOdN_z9ZYrTShHXh8gXIxx1lidy-28WEvWch_RRbH2SfTkpoMyBecbrs4art7L_EJscXhH7z6Xk-wlsT5yUN9kXr_Rp0bw6WexRpHip4pln3dv2CuHwDPLyAm-he3_6Ffom9wD62Qp9lLKLTy5mS8rVU0bRKzFyRzxeMtw4TWznn10y3bdQKWUtaPyV5SMBz0ycT5J1RFIFp7yFhzMWrysfGI-EVh3u5CKE8L8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKSvEMvTh7EP1p95BOstFLq0m05dTAuYtxh9QB4oVbxvMfYSX8__m6qFs0pYDH_e2xLfNTH9NKei280rA9ne511QLF6532k2nmSlgj4LaVJtxDh8qQ7BrQJHwyBkQASdN3ECaJHkQ9TnWIH6QNqMmv19bhYdjvIM9ksdmopTMepdjmHBdz14NOlPAGcn-Qc-9opz2d0lJZmHWcO_YAkiOVqZKPc-vVVsmJUSYtDoHVUlVvtbMF3SeaoDidMEYhI7F1_4ayO3C-5rYszdN9vILsNOJzZSVEa_jGjLfVFdZIqftMCsS6iIMf8BB5mlPgBPoSQbEjE_-Ws0fXOGW75flw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6ghjntKmgb9SQNdgDbV_237apSBbti_wqSvYAMbTgBDA4ZWwFcDmJ60NsqDvId2eGlrsDq15BSrqDuWd-9g5PClUS98GCSJtxaXWt0dMBVhXJeNfaiARlsOCAHfmdY08cfcAU1rzLtj9Htfvi3WdE9ciwXwAfl2XM9NNaQbF9ll66l4wy3_Le-jhRc8mDWw_dWORJhUmZlf7LYB7aqKZlXNIgll0XHEhghOYUX1KN05UQH4a_TMVaMXp1WFE0EXflqDm4Jf0ZcUNKXYoaADtZ_2DM1Nu_7vbeajelzm6hxjvgnsJB0TIZ9ZBFTNlwqe_TsvUj-SuyCrfjhxxjRykw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o29DyvRFODQXoO_5B12089ecgA1Xfdd1VZZDKSWpjfJvF5U025OUzH738CCKPOUxzq9EDzvU3TSiKenu_lpJ_roRMtFwBQDuvPwzhHFgUiT-z1n0cBUqIbjNJgu53pADCBMSroWY5Je0QSpWncXQ7CAPYQxZiFzCx3KY5RW4e_3zT_8xYj6kHvOQf7VOFgBiSwSKnjfsUg-EyBmB6isouuJixhhpbsEuq1JtNumq6os1bR3YjVxrTk0dC9nqnOjBaD5Gm0IGGXCAdRzE3qaab4R0R3PyzyUSSPDzzdaIP5pL3phgHFPmlQPqhFphe4W0Cs3MonyllZzBdOkKLNV1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دانلود هر فایل پولی، کاملاً رایگان!
🔥
اصلن به این فک کردین چنلا و سایتای ایرانی(فیلیمو، فارسروید، سافت ۹۸و ...) اینهمه فیلم خارجی و برنامه های کرک شده و کتاب و اینها رو از کجا پیدا میکنن؟
بعله منبع ۹۰ درصد این فایل ها چیزی هس که قراره بگم و کاملا رایگانه!
از جدیدترین فیلم‌های روی پرده با کیفیت اصلی و دوره‌های آموزشی چند صد دلاری کورسرا گرفته، تا برنامه‌های کرک‌شده ویندوز، اندروید و هر محتوای پریمیوم، نایاب و بدون سانسوری که فکرش رو بکنی
🔞
💎
( آره حتی اونام اینجا کاملش هس
🤣
🙈
)
اصلاً داستان از چه قراره؟
اینترنت یه شبکه بی‌نظیر داره به اسم
تورنت (Torrent)
. اینجا خبری از سرورهای مرکزی و محدودیت نیست! همه کاربران دنیا سیستم‌هاشون رو به هم وصل کردن. وقتی تو فایلی رو دانلود می‌کنی، در واقع داری تکه‌های اون رو از هزاران سیستم دیگه در سراسر جهان می‌گیری و همزمان بخش‌های دانلود شده رو به بقیه هم میدی. نتیجه؟ سرعت بالا، بدون قطعی و کاملاً آزاد و غیر قابل فیلتر شدن
🌎
🔗
🛠
قدم اول:
نصب کلاینت
برای وصل شدن به این شبکه، به یک برنامه نیاز داری که کار جمع کردن فایل‌ها رو برات انجام بده. کار باهاش به شدت سادس؛ لینک رو بهش میدی، خودش بقیه کارها رو میکنه.
📱
دانلود نسخه اندروید
💻
دانلود نسخه ویندوز
🌐
قدم دوم: لینکای دانلودش کجاس؟
لینکا اینجاس
🤣
آقا یکی میگف من با تورنت حال نمیکنم. میشه مستقیم تو تلگرام دانلودش کرد؟ بعله اینم تو پست بعدی میگم. نحوه انتقال فایل تورنت به تلگرام
😜
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
