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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXMPSZGepz6F3Ekm8ZfJq9pKDX0UJsCHl8f3b8MfI_dFoPH53w8QQfYZMSpOsyJWGdExUKlr_HmWsy3i4rs5i52CcXax9fqAzYMOQncoBm03n-EajHpQwyhaLPwEWWMyeOUv7uKEH1t4nyMp01QDhncgieV3tYlFElVXDyWfqrbT-PGqtxOUNqMd9BoLeR1-3KUhFweds0SIJZ_UGBFcBxMFKUm6qxrqT0W3nrfL6FTwY7LUPRV-tdcTVl9j5vB1zXJfyJ_VseX_k7ZlKGWs7c-DNavqH8-W5Z6dY-YcGBjwZaTTzro5EsNDQkqFnkLCcNcW_S7_kF_c08WWaOK47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKgs3fwLHnKcVoT7wszhdqQhJnsMHeGyCabVtDVnRE-h_wcG_Sl6LPlg2uquu23a7-GxeHqQnmBj-FJs6h1hUQmgwq1vHEdoPGqGA7Zp-h2ftCvS5d9ZF8zNBYW_0U1P9zt2vjECPIeAOyFD0w-tevQ9DDWNgCDld7QuHAHGENdxnsSdMNOiPg0aZ-WnfGfQJhxG_fqzU3o4TuV57OoeLepvQxODl9m3KwMaUx4dy-cNp7qE7DqrK64zwePtEvBwzj2zKsnZmTJN3oTUfedzIpX17Cka7KN9KJMRiC72rwB0yreNngZrQ0xhXK64DfFzNuE8YTEAGJeYphyNY6VYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7o_I_NToE66jFLsZdaUKkEL2_I5cARe6WGWab3X6J9ssLH7d1Wax8tvjJzjFtQYdgOzafr2P96_idSYZbe80iawaBl5RmvHsTWaq4JVMbyylBAPn7nDNHDQOjsCQ_-MqDrkmPWVdsZNuN2xxLigQsQzzj3LEuEV1sSpO2Fc6lFeDnzbGmQsxQSlMhmz1sq8KWGSjU8y8w7RtUYkfDo01f-5PsZrGfiOhLTIrw5_uNQESR3U1yiCUoWFGvE-5nPYT-S1TxsSO1j2NXShHxTWBsnpDehgm3km4P4iLfWfj_ywfBi0O_YpvmfLrzKMr6WhpyOiULPIgkZ5zV6QcH5x8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYhJDZzm4dIkOAYQXhW8fSKKOdC-YIT86JDE_WtbGju8GOa2z-mA-Le1Sf4xxXGVWRTo0pISicZFb3ux9bjSvtP9lp_fnzA7dHK9Y6ovY3C7esgaSJDRov-Zh3NchE1Io6T9UkcC3rLbXm4CMFfPaeqTD4qqKGT3kAZO7pyiWcmRup7G469BrjpsPiXRsYUOd6GL6njFRzDo9BJAnI7BZaFtyn-LyfifRYC7W4N5XRCVZ375ROnElBQY0p2631i7SVqNXfBtZ2scU7g2_g12SivVtX_O0jSLqYUzMAHUUjEC8XViJYhKr5Gpfx_4tNP0dwPwaFnIW3Vgj_MBRdDRRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwCgJBV0Oy8w0cfZBE-ltxJI5UekttWhcumAIb4QHEZ6pxGGZUgmYmIoDToSkUICBi2Brt10lxaWSfRUSNkid2EHHAT1SSVzzZB1rgUdNl_b2sWsVs9AXttCDogJU6L2guD8ReKH4IBlhG0KKXeXSUYuZ3qnING8Ab8aBrrxvcvKa873ObUidrFT-eU84MqV0cyuMJkf_TOoxxT2Y2P4Z9pLkPAPxPRwWc67BAlIkxGSvwVLMRZentLPh74x_IW6r0ie8kJS3Y4Dmhqtx20k7-OXUgslowX3vq7QvMjmAM-XIFhpCa2asoZt9D_YFET5PkTg9xJJiO_Ah43Y260QGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQojFrGNmPpdaSRF_bV9gZ2e7MZHIz_9IcW8VUVcOzSuhKGMNmVXSa0-VDYeA0wtoGhfXLXZa4azfBZZ65wCkqvBurCAZzcWQMf3hlrSg2NOXRpXYgsqb6OqRhB9oqCPOy1k3QXh-hed98B5kUx5uXL0F8j5LOHmJU5xreJ0JBnRR0JY6RyJrFVf_VC7IHF8Ih_CJ10UwYU-nGnRNV29ECFNBNkoW-jxNzgNX8-Hr1fhLGAHmUxWJvJkSsU8JNTmkCzndQoY_S6PSRJqScWd9w1lYcXCnRJiccVCU6xpjXendz2bXg-ZU905wcGAdVwp32Dz3ZuQQnOBH-Vlkqsw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXjcdHG-rzEZFJRSUgp7nBxXZtHheq7ZoCN9GZ-ICQosUcqIXhum98QUGavHp6nTO9sVE_o4SzE6FZhx5zloFIcN2KEhRHGTDru4WAyy7mP2OVOXOfGzQY4xdAmkYeNg08ipmJkYqJxc0z04kEmKZOMMEh3KLP_u7qBP_s5kNAAtdA_z5tNArgRBM2DupBSn5BCKVk34wvDJWjCUfebAjXbYjY5ry-jKokZGrOKMfcOeLLgn259XmTTlN3Hu2V1HwXYfTvxyQIxgQxuT585LUyH-xzAKDFF08pi6w3saeEkKC-WQa-qfSurPWiwqNzklzhK_CDdd26GvNjcOHDAxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrCq52IQg4_2KJFkoT35Bqh7t4i_aFlNBPIv0S-lglyBWr8cQ8DENdrZVdj4_Pa-jIanGECXWCS5Dcmaqf2xdnMV8WPFLfufq5fvHu4wr13yXOqQN02T7xkKJR8mCvoGVoV3QGAVnN95eo1ZGYfddK6WaXN1nVE_tGYQho938eub3QsSqNLKZmWKSY490adltBdamnlP-Ntm2r23EA5JKXZhnaGiIxDhUbdTRUH3nEywLNNTi_BxBLSFlNQXeuUmPSEQUjE8jdlZBAIKy9gy4S61k1fIP7E_v0J1ZlYU6Dp9J_4tM5hLo7HeA_079cAtjkI30Epwd-Wb6vJeXoOyHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-3Rp9qr1ggwRtSwoXlDLD6PFd4TXXICxaDSvsgQTmXZeEBymxlvldOp6wARspx0Lla0r69ZfmJ86qyLp5Vq-3EGgFpV35Kyl2JW3WiQiXAh7D-3n3XgWzKOqvhXDv7bZZcxYR9N5qTPHxMKiami9soVcNgImNxAkjYVkdLNJ2YQVrfJMIgeZbr7Njr7V5sJI2f1P6kCqQ3R60rwCeRbHKay6pwjxXyyZYG0DMJnlkG29VdrzlPwCRdVH2GEZ44AQ9ZWD5kD0QF6BYv1sopP0QOEVFWdnRm-TXGo0Bp7iebuvk7S3ltNcxzuDrt0_q-wG5vS8ToSMAc9BOnEBRRytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqwfld8DddmdBk9o7aXdJeDUDRLFXs7T8bgLYSCz1oSItlxWcvZicccj4s4cXbJQviz2XKa6epHjM59u14mqG4Fyc7VD4EXonSeywkw51z5kn9CugNEIA46Te4ln3vIzmgIkemJVVIBOihjM6rXsUxxOcObMCqeuXEUGHr_3wbWibjfHfremH7DgTJdZrWrvngv7XQhjkvq1tsZoUVAwVpNkdxkFuAOAI_lkCu28adsEsqWDZipKTBs5o1ha2-K2Ayi0uOuN8EZy4ESsjZyMbuE-UiLBgqsH0sQbuVpYc8tgV9D5YdUYMcm9dvN7dPp7byKVUjBES_G9IuBdst2aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yxwjy4Cce0L214uSqtcDLa0nZ1KFUQYHNxh7_4GweVAanE-9a3zvoNS2ZaHcaJbSwUrJBtaMYmhFy5zcyCK6fPBFnsg-Ka_ShFLk_6gZFH4O_uLkyMuBzAf4j3M65ugiZgTvxo-4EGjVwjmN-564GARR5m-rKHhX06JJx-bgzmcTv6TjGOO6XHbBLNRTO8k7VVng4vmCeCWF5ilhmbMsG3rago0vS68bRRm8GAzBWPYFIlCB5Qkaj6vn08dWiyKgw-ashHXcIJw88seQVgoYjgdRLdeedlDW6RhRMMf3GZAkc4Tq_yh36qn00TGmgeGcpq2jNEKRb7Ekdyo4X-lJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUJPlP3P42-3r8kFfI0x1goB4yYXlNxFWvRjYgpxkOmBwlGIQUXXnxB0lC-pT_QXK9kK1ax0NhCY_41Tt8RgJRqGUzOvSegp2EM7QLCpPW5MftofCu3Yt3xrsV9qTnOHtJ0kCsIu7DtGxD1JFwOtmlk5f4d7N4_Dw0UVjF39CX5fZszeYiy4oUO6Z-Ydiflm5l_0s1_x8WjPAjNm6IlkKKbPQg3EeH4pU4GiMjcVlcfcsyiXjSPJnh0O9xuFX8CwqhTkpH9RCnXaiUw15Hr3oPdXdleAEvjgOlzXFaGfLZgHeb-1ZpfMDCTIPwjEftrbgaOkTDIUdUrsud5W-wG9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYzZt9OQSiwK2vkZOKnu4lvjtmY53-T4beIOcGMkKBbAXDItEnUSZKNLNsMyirFBtMYXzKf6Lp8rIkmyOezf96EuQFBAyiY7_j4T2i43ZiuyxL3RkNqjPyIzWw-hrgCrHTDC8cTkqCUKcf8Gs_c6QYkN2gN0-OXdO9Waf9Nn0zm5Rm_WJIBz_Z5pPp93f5byScanFicsPs3AQJtssuoslilMIf_T3xEWHTw2QhvFMEBYJZK_K6PEGgOClHKe_H0R8mc5E4BX_dr7vcclprE7EJouiY-99EAIBJo-hV1nZccDD93-rv3h-xEBCBXpQ5ivWRtogfBMG3pFSK1QRAKvgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0iKeknBa4xd52QlBNy0PKUBk4Ek-kX8_fD7hZEWP9iJQGNI4aR6CN4U2FlN-ZLiTF_xS5VV8RaRC3yvRZeM6pd6q0i3yB9Mo0JAMXtf_ZBVx4SiMApE4gu_6vlyQfDdkBrQSpNQQi9lMuM1PzcBDc6FoJW5IiRfGtOSDuLIwnLVscWDdMszb9DhkdmIym9yg9pbfouagKd7GwQsEvkucnHu2bCHtFRtD6KPxTAskV26MO5OoPng1uNHgjZ0AmTgNbv03kC_-2njQU9q8ijdRe1tgP7JAjZNEfMnKoZGE1uRL0YbOR85RCL4dq2-cnf9AB0-syehkR1BisSsV-jldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_laEC-6hs-Vd5zdVmfx6Z5NvlDLq3yMnhcVgJBMeRokEWz2iX9oLKtiy-jTrXmPLuDI5UZ7aeECDfd-jY9c1TjzVtAxz-R09HQZ-zPuOBvDHelZGOhON_1YUvnz1jP-u0GAjUjt6dmPaWz6SqkOLelWjxKPuWUOESGnq1CtbEPl-WcjsQCTHiF4qCmx7K9fervymSOVwWI5GdTq9Ak3o2Cpfl5FMDp8XSmsFCcebX87zPJYwJa7L3GHMHOoaRXSce5fUeqpWJRqHwUSqys80ptrabLP_V3d_CwrimIGfWDgmajYNkVK_XBe_ssXyhERZS17ABM_ehlNJDbLupNa-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqmyatvoXKSvuZn78fZLG_uUR4OfmknOx4uXFuRTuiBFRL-ajiI6r8J51f6pMppdEoVyam5f3WIXttxhD__JMqXYLlf7_RaEixIuBo1g5Z6R2vvIwy4Wzyvaekp8XXfR9E8Oa8nEAdk3Q9PEP4YR35i-dHF2MzP0JQw8nfkbhep7DJKPL06zmiutN18muiC6A9Uvsos13x73hoLWtGdjQPGH7cidNctNeCYBcgYbYjHEgue4oeGOA0mWDxddgIYT3vMi7XvrmyNPpP2HevPTZqVaF7EMNtB7z1qC88FFR33UZj5EXHI32Ue_mNZv5-Fyi1YQhGWLecZNyXyEisnVdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8kdspXKy58VGeDTt17r0lcriY-BFad_voqZtrylwu5sOoDAVKClRnqzGv7l40wzTDvC_CYuks8n5koB9fYOn0FmQKNA0-5ukrBNb2TMPbDZdvZb8s70Pqe7Il6C3MPcwd3pYSlKEuTXr9bFCMA6_ScB8AYLKu3EpUyqEaQDjrDmi5QLGmR9uDA66Xb0A7oRg1gNARc6cGr3aUQ--v8agG195p7eImO43vTwe-4681PJJSL52bbTBl0TRa_QGuBHbm4U7kZTFK7QpkTiyvJfZu3bFxx4xsz7ZaJM1DBoQDjvhGbsiYLqbaNuxeRlrj736xkPDbEb6gXEE1QJkR8NLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEdddwi4YP0-aYrsnQlYZtgYkLHmFQEz1i9t3B5ATCX6yrRn0xt8ANvOsz7nZoaMauBd02wL9fzg2r8_GoO2P75x8ZfnEt56jgBsGfl9sJPA60rGulVtHCpfmkp91ZkDIWEJUEhrKY_2y1Lya0hmMSdzOg6MO4mjv1Gevi3lDwxV7w2ULD_ceSg_ZWUKsjr9WsyURoBxSJCM-eyON63ww-yr77PQshxm3Sc65Ca_NupvtLnrKfmMH1vw_qRdVi1f1hP8mD_2uBgCZPWeW3CUH2Wu3jWVaw-Vv3GuPuz9Xf_l-dIjUthYL7sYCsZk6WUhjJ2izPg91ndnOIBVmL-eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZlwnjsCFb_sLc_8DPhWxr_x2fL8PjUISn8UDdTSoJy76wvegmO1w8f1pJHru3qRMvpjjdUMit7nHcK5C6wBZSlS5Hyvgo94tdr69PF-_8KJofdM1vRO5gPC8Gml8CwhkSv7JtYoJ92TL2zTPHZn4qR_1NVKS502Qh5LoflxoGX39e3ZVcrire754ds2tmgTPozy1MsP6ncQMtgo5HCry_w3XmTWzfBOafkojgI5gXepCiW1m7Xey3xeeMaDuAddkxprxDyKUaPOU4MmizksBsRbtXSJl9hBLYooXPXJd5Q4ak4TylK78F0ter3FNUNhjaxja6v3LhU_IcDXpNiw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mkbw2ocxql6HrXkVOKjc1iToUvN1RbbIVBlfoWlKWJJSrpQTLQBeRUPrT-AHk9Tt31eN--X7KM3cbiNOvLAgPz-rZuRYcBpQ7rvLvaOZPcvkgATWH7R4FTw2btQ8imuX4Tdmri-Rq9Zw9xJ80GNQrCFb427wZNIshKNMWOGSYuAM0VIkkdoymSBvQVvn3Mo9jkR5LNXRhbVBJXqEPXe6u_KJwrZMj3Y0eRhXePRKafiYI7Z5tR0Y15eiBvbQ96uCJ6cVjtJQUPu8Fhijnp3X3fb6hIswSA2GykwGuLapqGZHPi2-P1QZQ5aTtj5Eqwl1u2Ln-P54wcbwmQEsbZM_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxaoKOuX50jvuIUWP2aO0fl2LXRUlesS2Y1k9--QPcf9z2uhZTFowIl0EfMpmkjQfv1mteTfCP4V9BPwGza8C6K2SvqvBtqCW63MI2aoqgdsQk-1Y2TvfFZ8crCWQ35jqRevf76V5zGKls9xYVlpfFcH82qp5d3iDVXLpDFPaBZAbM337EddevXb01qaGWebzgUdt8FXrTezc-oulZuFe5uuefTgRa6-JmY0RUbI6uZGSrSHE4urWXrLYMEbgbZE9MgrU6HczA9ggV-I4sfEDZlZI71V4d7MYnJfby_eKZBZgeJOI2G59mUmFvDM2HtIMEx-cVJycw3Fyy9HoTEeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bs_nPNB0RBa2DcXqVGqmGDmCPTe92Uz2lqrQrnzxPouP6AxeDhdwhQQe-h1f39XN53R1dI9v0GbZ35nput-Fc5doCk9osPq0v4nIZ-KX-wEpicwQiPl04FtxXQLhTtQKUOVPhETq8d5CKjdefsw0iljEi8oQcBEsj4B7dJNlnxrQ99ao638fxA40Z80fGbagR2IKqDXMlExob334WvNU2iw5fBrT33Bh5xsf0kbJkHTsmX53zOL2LQGnLKa5X40EUqjYhLMMgzTpiYyIPRMaRWxeheaPTmDRm3aKeRsNFrYXnfmnZZRWl-FrnokHeValwjNnoUvtjJGoVhWxuS-3KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiZu7Phaj1C1ZjZTEg7JZFTdbjAzWYq6ScpMEQB28MdASHmhVFpGSpttscYRltcSz6hdWa4GA6_3rhs-CZum3fsAF1Mgm2EfR8bde2ZIC8yBidz11Q2cmfnurB9-28LiCKeJ2j3DBndYH5kWEXJio36gTjbGqbv_QoVTnuTgJhBHDSqmwmFOZb0DtNEs7c-QRrkiqHwsvlL8sbOCl_Jp5NzC0F2X2RjobYgkVygxLYIBtRQTk5_bJEs7YIVrg1Ky3mbEDtGRP3JK7mciHLmHROZBydJaGXd0fmDBAVlVBY-huneTo0M9p19jIrQUEveqpMoPf6YsYK9h1-ikmsmg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCzOVnX4KUMBtREIa2GFHgezqf0Dm0zeCFXLWUhWhM5BBtOoujLtVVx9et5tr00clhMcoYFnyb6tI2nIyxKT1Pc7qNvkrSVQiQdIqXsVUCN0RowTjnVoOA4lKjApP5Vj5_lkugtUHd-MRrvGfTVesk0e5Jg4scsO7C9fnwt8tcp6SOySSIHfLK1hhkaRi1O0Q4h7D4l6YmBIQEQhXHHKQ_FlIWv8ZivK-a0pOKeDP8g_jw9cn4JdM3LrDTRys1a0ooYtQUtagFVtiU-fQ9ML0qv1F9EC0wDM0xOiT8EzH1eHqXfUCTm2tOK3kNd9nxZ0A_lmBmQYOHlGknnyfIInYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd8X977fC81Il9NQn8Olw7q09xf6dlFUZB67nYU4cf4ElmNyWpmPHDGwP1yll-TYM11tC3QNhMhi0YQ_ruXJIA2oISihhsoSL-T9C1bF5Y2DMhqw73U829iRv5Mjja_6sISISCViowjYTDtXBceTAyJt0oKdYpa6tcOdyiLW2amq3ZWWLepoWPEwFdHVaSoVbcIJPuJO2jqeTDvh5_cDjoHtESjqeE5VsowpDkoa2u2vnXWzCsFvv3Dp-ScNVMaML6qLCgvV0qvJZkgpgmLqDxIHpcN6uQGttMFOHXDkDpGOl_RDTHoOeFku-8Zm8feAAl4pLEEFI0D-8uNPtOLAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inieGy_GCZsQ_2t9sbvAQCMIoJMLGXOyhd84UbDo80xnpm2nMgq4-HuE8-ItNzCp7Q8GF_edfeI9QwHxSibep4Mf5ai_YRxeBHPPMMwIhxYVIG1E3_bTonrlS6N7V62AWMZ60Dm4Cxzst5Ki9l1LC8xWdK8c1PC7L8AzY2Vmdc-fMe4f874uuIIBBs9V3YJnwP7yHr35h0JfGuhsmfpqgdKdBaCkfyUvpY2V24Os_DFrpWE165qx1wKMHG9OkC3wRgQzKjRD8_v4l4eO2w3jh27V7AUNyPAqkF6p1Qnd2zKWxVS9ORhLw3Unxwh3glBcg5cf10p_jZrVPZAv0bhQkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDlWGfcyN4MQvmyHECJrJ4GVnJ-N_LlYnbnD9CDDGeNFDDCQmfsIY121A85sDIpneQ-pbYpeX5BL_Gb3jdClGism1pHaRFvapaLqyoKqlXNdYQkiFchKvuFTkYLPU8kaqgx2SMkM19GPepEKpsaI-Z4W2Kr0fnSJPXE9JLgwmiA26SVbefDrlMNfCSqLspeWkRx_nOoxY7VoC46rw3lPpp0Chg_bsemFxpz9SO_iqk6c6da8p1rFsZPNhVqerIaGpZtSWbqltS4qya58ZRgSOqC_XWRusmJlZxV274hyYzJVS4ZWRwSVAGNYELeGM2dWHawNCyCH4B3gUuKCEdME1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4-5yPCdgMhUYA2cm7Pw_-KiVei3clYQncPKuOsOfqnNcwP2d83Tl5dmD-TEeG-Mhe_f65XIUPNBijcaEhDzE3KmqLkssrc5rK4muf0VnJ8Bhmv0qEimVYx7nPDF5BRhKgruJFzKFQ_d9m-AEPWWR0lcyWK2M9ONzoPp7xHyP-es8JDgWyWNqpLqlwVXUeffPdUZZBS5vSDTc3UfqZ128wcs4sCf9HDMVwdaCD4Ox2Tob-gjHMjaDE7_imZZ6jzYUIfilWEGTyY8xx0jTyx30lXxwhFhM_zmUP0TMbNDWRA3ng8uRQ2fPmSZ6Dw__RLXBA4-ygJ9RyP4i52J5ZWVFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=V9iOwYlT7soM70r6h2Fj_h_ivKALiy6EU2BdZiCWeLz25rfwCCD4Z2TTFZUKe7V2HE-sxJdL6dQTdMTkbjIMpQbNBiJWUPDfOYQ8NOX1ULaccCNtcfDiTe24qp3Q6bpDeh2U5flJ1mAasAxoryd-clLwPwGuGUzzKV8N3RJb6ZINUN667Dt9SU99Xg9Kw6CaHgNeG8X8gi435gIbMcpumtH04ORN94iqUpFMV_X7Fsp9jMrBYPkFLXyunljcXuvea22Rte6ycvAo0iw_paT33MTnSoaqftfviaeSkvcZ2I7atsJ2llm4JmzAadP07UW2u4vJwOwh30PwKRQYUrUEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=V9iOwYlT7soM70r6h2Fj_h_ivKALiy6EU2BdZiCWeLz25rfwCCD4Z2TTFZUKe7V2HE-sxJdL6dQTdMTkbjIMpQbNBiJWUPDfOYQ8NOX1ULaccCNtcfDiTe24qp3Q6bpDeh2U5flJ1mAasAxoryd-clLwPwGuGUzzKV8N3RJb6ZINUN667Dt9SU99Xg9Kw6CaHgNeG8X8gi435gIbMcpumtH04ORN94iqUpFMV_X7Fsp9jMrBYPkFLXyunljcXuvea22Rte6ycvAo0iw_paT33MTnSoaqftfviaeSkvcZ2I7atsJ2llm4JmzAadP07UW2u4vJwOwh30PwKRQYUrUEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd7Z8zeM5t8_yiBoHMH7hN9oHPOE55P4GiVyCk7G3Lo1yPhFv5Yuo1RyE3fdg5pFpohC4qfoou5GinS-PvGWRvx1tL8MzXZMKfXMiU_Pe6dooz3DnyrEhyyrjceLJimCWJbqveYiWVrDKEbZMDQ9s-B6XbUFCUI58jgLWYodODRg60eSfCpGiXx9FkcfoptON0gpWB4UE-BlSFHxSP8Y-n8-Ttoc0cG1FMMbMpFSODEDInZHUqUFET4I-QOk0839bKaog8aW-sda7sXGAfnDd3v6E9q40ubY6kzTtI3PZhREkFbUNdddTu_JJDFNxC6uLkmNEnSVRoJehowso9GbcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7JV7x5wu3Q7DW72U6_qCrIXWSara0pFj5tqnECvF-qiGdHf6-3j6wI1WM2wp6iK0-obHICmOYd72O9dmyH4nmfmSkjVB4aTA9QoXFUyuA6hi_UWPo3A75koXIV3g3xIXBlKkvd1NfXr5TuY3UfMvuPpKVU3yd0zhw7t_uWKA1UIZeIVjYvjIuSDGdOqbuC84RurftTMDOljJWJQMJ1YDoac3_xfnwpOUK_iewRNoTvt6J6bqFdYYGlK4bboi7hHzANvpDogshyhAsC0dgovB9hPMTewHn9g3LSY9HjOnA2zZFsRO4Ol_InYRvjqjLxpxyu3qFPSPB8Hdgx42nMMdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-77rViHOSzNEJiISoCyQuOUO36YLLsGqGiyU20MWZrNsGxjlegxQA3LKChGK2RXEJbGdM3XgHqNS4TiXWv2qPM9oYL6LH_dIt-k-IdUVcaddzyTo2PzEEQ-t0cy05a-ofvrD4RD2hdRt3KyD3-lr6aUc-OtwBIJjccP_PiviOQNZULktvHN7nUNyGC-cuo3bZzUshY7kzxPjnrk0tQ5HPyq19986SfGj1W11_Yz1mQYchFkGNf4mX1Syr93ZMCy8Uufs8yDpmLs84c1AhdnP6eTHOsyBq-0JP69m32zfvHNPwuiD9fojrUyA_nThyIcBn3l56EXx5DuMOQ3viEQyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKSDyhgILC8jezr5RoJgLAh-KamFqQmW5-ESaIug4lI59YFf-s59w1wxrLT534DnVSz7nX9ZNde-nLKH2wYgqLZ_6IdmepXCg5-xSDh7FG6Lpf1WlYsfkxMw4bUoZwbl7s9P8kNBgAnI7vf13CkvmVLPxcb24_qQ3IfiYWXQE1p5DfXDvAT7kejKApuq0s-vj2JcSEDUZmbKt1sIbx1p_tK7s3ctanCJpLcKI0Zdr3qAeXVLZtUwflRVA6OBr-GTLRbzXfyTYlYuc6xVJRKLtcbzDHTeuod-dTf8dELCWPiO3pep16cm7OxCpM4yWEIHl9y09KOX2NNGU960uPIXhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOlTdu44DrxZxAEjr9RsS9OChTFKAQmG7BvQHRJOA2NZDSQr7r5AqQvkz0mbdKVZ-o_j89ITjwvRYu7-4_huObdLPI7sviaKtR_WITHRLExDsCyAOemFZMfJeCUifz4ShrT_GXICzj8pviBIMpgHdnlup53FMMyX7tQo1IgcfT_wmUpyZVi0aYPpoqtv-UQMzg8C5r4IHa-MSizFJSXFPjySw6g4gQYDk3_VCtDtyjS441niFn8nk6A9s9MeH4gUIJd2f3QKmAQSPb1F_Ur4cCL5Cfz4pbGWrUnjvVL5lgE163wEfawjwsTDurnzJ2hEnYPvE8TeG6u-BNsWyA9Gnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghkVO14aWi4oxN3rSH9TcrrZlcVR7NGgWHJdLWRfTf6mxF96ScGFhZ0vUr6O8Lv3qgxOuChQ873aafzOOxCoUc8Iym1m0k0nhbXsCB_BW0_-WeGuJ6Y7LiIbzUStlapdseyrmcVNEEBtlkknHHOgUFcTSVjHF4sxyhZAfx4UabuPdnWjctLopl1NwSemlV_ff5QtE6s8twmJJdxKK0UlhOvncmDY3TDsTReWy6zyornrWBEeKhBq7rssfLw54ui39sGYSy5LOcJ7Y8w5QEMEB6ooNJvlA5CE6ImnyCwOcBZBjAMJe1R00L9wq-dz_R-EltlYU8xBE7L4oIlTJRq8PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOyihSsJopJD0R2GwWf0Qw2yFECbC7EEA3jBqm-ymhMNwnkfKzBO63QSlLbS1fohWpw6Dans4ER5tVlYYn5uGPuUJokZXHEBo0MVpO-9CBVAJsLywOI4sbvSFWkWg8XrGYI6GzOooq1dwpKj7DgRCCiA8yXDU3WEZOC5HNpykSbUl_do86YUmOUEicND22t44q9eiMltgyjJwaPOQNVFF-3SGB77va2QTUG56uoIl2bIIKF8XgqzPEM3ClqdlDlGqXMF8l2zVTkfAKzLtIDdxK7puLyuJWyNaPOhNodwl19UFECFhtmLgMM7f8My90YkwaILO8cgjiM9fBuxgjMcuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syr-XQwq2oHptdZO9Ady8ahlKQs2ebRpsKGYTrrUmaD4jvvhVWh9Ou3sBTSndjMC9DG4BxNGW2NzaNmqZyAXJn4zABormjSPoY8tMnhJ3mj2GYzI2aHpzSkz1EVXzbcF_hyNOKUEmGup7brEcWl_zD_eYOfjh0cDlJ5fcOw-0YiBf0Szvtdqrl2PITbXgig0nxfFJY5_nzeo9b5VYFnQfcyXa85PcgcFfA7XjFxSq1KcCxfT_M-ydCZTxAZxkhzfG_phWx-ngC0uVzhzWuQ5CyNRAzZmTAzjOdVQrq1_o_W7S_eIALUzNVoIzu0FrfiQg21QMG_aevc1GamG6k1Dew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9p_iNlUKcMvftvAx2aMFkStAXIXIexoWyMbjkXXr0i6SuxEbtpKHbpu83YmYDlnB-Qx-AWJ6vkEVHKMeQ_c6GHVE5e9bmw63YH5nO1FkXvVDBO0mJtjzCc3L4TDp0yJUepgsAGogPMO2dAjF4iyuRHDJu-Z4zWvvhrosiQtN7PEAu4KHfnESelOLfBkvIlSEveP_1nUumXM3izTBsPPyyckUC5ftX5s6KFyfpudj4bgraB2O21yJmsH03QN_FyeLJMJvBur7cSERRp2NoHjPTwF7YC8IWbool5gNcBwkfT8VGT_PFaMvZG9WnsO9O6fDkYEv1yYA5Xgnz9Wxe5SBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyTSw3uT82t_kslMDEotzbNlloqGtT0SNCgHs_glkeRLKs38BdjdzTYzP9eyWgPHdDg3K0aMpEFNzgXirqSVDIvM4XwSa9ftHFlCSJu8xSG_KLs7_Sozt_ObPxOoVbozve7gPzV0ZelJZobeSE_wkHaWyMA3_H-tWg_knjB7cXrwTanhfb2rBIyW9X0WBeqTbxU6wBGKUuMZ6sA4C78qCa7GK02WYTJLEtrlXfl-7uXxjW1enqbE3rPNQI1Ko9XJk1OW9mI3XjZTZoxsOTiSZOHZQ8rcs21oatGTJKmGJUBjM2Pv10oDaFdJBRe-Z4EZFzOGDdMKHg2TW2ms4M3EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JErVE7JZgTKxXFxyUi0wrPdRlGJxoXdNu9LbODj3ma5rhbE5MSqWPk1NHJfpJh5CJjfjgyb5WyGANyVFbfaSiOHiL0o2B6AJLt5V10mDkVa0zjGkwzPkpPIUCt9Vnm60s_rhXR9BSYg_wpvdA-EwScL-3IfclJpbBxoARRQF3DxQYC2elJ_FGXgFkIzLGFhYTTxPkwLfprwB-QwH4a_XNBnda30KsXM4VZSShnnemJJHcDl4L31EDR7UGpALOV2P0YsvrqIKyAGD4r05UjNlU1MvSbWdL3XcDxzGYLjjBQmTIf4MBdgyPKgZ1BhvJUiHW3T_Ug2DvdEEUGGPn2p_5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmeY4vhZ0cPBk42YGmO0tg04qF1UCROFbTNVe0Ovs4ToSXcd_HAb_WLpR18op3mIPAq-slT0ggvlwGhkGsFZtG8ZyHVqA3k2T4-RuZ2RSiAmPSulY-4z_ZxlugjmCmZC7JsX8Nzbr57l9H5zWDM6JEcICi6rm9-3zwdwqN3cUU9Vy3L0Y26FIPgUJTumiTyAiG-IT-GlvBrVxSELsiduSVo4AsAMj1LJ1C0q9BPhSCdCkg0HObEreHh_M9fHgGwgo8lppprUWUYIH9oCFPq9OV4PtkSlJJ6jkRC8AWUKkVMy6L7RqNSJw8JpvjjGTusNRM7c1pSctrxHYwsAx1khsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe1c1xeR6wuN8w0wQ7OLOP-8ovchXdhtn3x7PeLmtEKMQsw0-YLeh4MM-PuHik8RTC2YfLS9JboBtfzvVWX5E0qkASxxdUtK46IrZ0HVkUd3TKgPqX-k-X3hUg_mJJLTJ9A760-3BiYofyxZj8EQ0WGO4TL3-oKy8b-HT_izLcdJuqn6u3J_DmWsMOvWvaVvm7NViWpBMUCr1Fqa2PAB7MfcGMCHmQKoaDo_p127y7BDy-MxqHiO__Edo90j3av2W_R66TKeMKoBN0Qmk_MBHa7eP1ftLtmFUCUoKeQTGoU1LEOCKmvyJheUKHnJxkLrxLfYpDvtbAhLsMnKUKS-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQPmN13fkBFlTORNT0bicBSJR5T6fzvrGgJy4kUKnmfHsDv2pH_BP1dyqMmqgIgKmM2LIwd-g6A6l1fSzvumLA46IxY1H6xVU2-qknvRN5MfGnl6No84JPEiruMcIx_qTVlvUu7Gqnwbkl9qWnqbgurYysqhaCxoiJ7E3BI1WGWhDeLlL3TqhR9C_h5GWAFdNfCv-27iIVwZme3uwadoYXfS30FDovUzhOVxv-Q9D8nCYZBjssSkwEZ7Lzig1TMwMsBHdYg3ic6lxBoOlTvFRjWPBPSp-i8lOv6wCKwd431UQbwXgv1yFzsQCVZfJtxOMW_I4pkxMQLnhlShWo9fiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unjjl6yRnQ-VgYI9ZjfQI_ZEVaIKTGMT1K_rVTNIgjzgEKsP4dAy0yVWttY1J6gsPoZTvTRRnd2tl-UHcqm9x56qmOTPlEG7lGfnWz5DK8H79WhABvMzO11J6kkj7ipYKnit0FkrJVDeAgsPWwiIsE_9i3NoRXJP7zM7qdKJPXwQ5nrpBrnLoEtdk5qCy5FvVkY7ALi43py5epNXjTjXtAGVy73oiVWcC7eQOp7qedSjP0lahsh7zbDWReH_siTP6G0us583_EaH_0o6HlnSPhNTXGCsECv7ctYAUpBUDonII4MlKXYjW-bKBV7Xz5vD3r1D7CVuJwGMoR2F5CezDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK7oaydM1tuZb6tpB_5NL5AKp1fjZFOmy-EHQbBq3JuWBNXKWmBUB8bvfJAv_LjDURk8eiKtWN8694hMB0PNNXJMYB9dGUuo5OX9s1iMCNUOBaWs-RBtzZ67iZhdSaEXkugzwLLijyIEcd4kl9glRm3atV7Om6fjP2z5gBw9ebfWK82OtOAQMEQRDRu0_JBIY_2OeXQWZktZTLYcxGtzj8ub4dYoT1rDr2HN7cgbTG5tNW_JkLxEQk_i1G3NPfnEoh4zQZWwUyNDoyTtVA0-UBEB9CWXzo7SExgtJtF9RouK-TtbuYc_Iju8_Kws0mw7rOZfQhn5-ulN8bflMHSC0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kax5OYb13k8YBqNAZaySyVmU4wj5NNG0EpF27Qs5OW-7tT1ejiaFAqaj62IG1H18VQgS_uU2basX91eAtXfWPRHjzKPOTO6vMg-3q5Bk_Y2NU1bF-CRgeMPien5QHG6aXuvVq9UVUqx4W75EZmSohaJY1ZMCid2JF0RIyZenFOyS0BsjCqmJKNJITm6FoFYYSswwJUQvkz7Jc57ippjv5P17N0WwxM32eyq1-in4m4-uzbbA21-KqMifzKHb9FGefyelSclJYVmlWWoIF3o2d0D_3QnX4tbHlJIP7jPRoH30wDxskH1x2XvkBoNQl9um1vMTz3SSkd203u72ucpJGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw23gFjCUlJ4euTyb5twPqoWeso0cdkQ7VCGLC29hCujmnqKeB74u5WW8b8WIQgp7Swi6hfGwAUWzmMGfrmtGlLYM7hwGa-JDI-HPxMata3w62Hmmemtxm0FbFyiNQLZc8nSNLFeG6elOtFJsGGkl8uI_Vf-CH4kxJH_BaRIRTo0-IPzcuq6Tj8T9qubKolXjsjPrR8arznjg9LgpMYOP6PBElGso1ERb4RKhTOoCSNf8MRrTtb_QzQG44oJsAs8yUyRvQFtVYG35-RVAfDF2tynvI0_EecPHTiDlA6nLNWoHRAuBKwAPcj_CZOQ1i68ZcXzW92EHV13u5xxVby-VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVixGyrP593KeVkHLw2fJsFrsrsEfRMrpYT16ZEc4OefND-VgZ53fgUNTTTglTf0Q1RbPbJnZQE7raD4e5oihx1yMoB__8geRyMxSu075X3OB9EgPOTSjb6EBNSC6Ot6H9vA5MNxW1e4c-XwgUe4VgPQHs0Ky3GucVTYBDJU33RRd-bc8oGGjC-qHRd20M9sxYvhEBuDmEky4lI0W76tfHSheDFuGnUDesaD_c85HHX2VSh5EP8vdF8st4Z84ixEuWTwoFI2VBYMJIYlbbkiOUqtCayhFJ7isWivzwJZuuwV61beDHK3kaBGIJ4RvTMJxlWY9t_8pPuMYsw_vBXBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMErnOLCvoYkc0duydA75uaPtLhUu2AS1DEk1FvqEfXTLFUHtai8FXQbRt1Sg2GB63gEweeZGxrKCaK8MKLGUk7VCiviiYgx3p6CT-025SqjwRmX0IWzQnRNTIgdkv153TjyFfUGC5k0UxescyShgFswUbG8l1594K0-rhQmiwHcQVn0JNCpyt3MvoUbVfE1hBCRW6gtNWnoNrkq569HNmLylnKLc20lL1FAzBklGAActeOAqtUIGKGyuyLPLlo--UqS99vK_zuWaVPcYlBDdfMm-R2x5p7nGzntOhBuCf0XM9umsrV4yXOD61BW8xs6tKFmzdBhOsGQmlqjM2tt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bzj6aZneBKb-T7Skcd62ZvmrZoffULbmrvw9SIgddxiMwJFZap7cmF8-B0YU6qyKr6xbWOmI-SrcVVPb4NtT2DRc2RgldKrcrvNgpWhoP95eZHoe7uLliYOcZamhjbNpZ9cqFW-07YK3S_BnRDx33AmOIVfjC5VzGbJhQFjpnxSNYUlf3GP4hdWR4FY3-aLFy2lZPT-sCfaIDUzTvEMzzyHsXFHWguyEpAvxLjDciWVMfys_4M78wWrYg_CdYFArrCJUO5KeFQw4h8OZqVcVnjy4RWuyakf3zMdjdlcURYAKA-NOzDt8FhsE_KZMnNi1hewPnOyp4f5Gn0dlv_ydpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=oHp2PbhnwQBKtIDP3L4F22-fSsx1M2cWfO9PFh6NjiG9slAUBsCMPJSlV7cMzaNLw0VkesyVKT2u7amydpS0oss6Z4JjDb9gG8Pcojny13sFGCOvaHzBr_kyX93IJ5LlH_-fUGm_gTLXAtc5Pwn78AHFywEBIQgiiNmMXpGj7LC5OS6Tiyp3Hfy-760rfhASnmKAkMzlRfK8j5LMvfPuRMGiKXJxRHjgamkiz2vsRKd8BoAOWx7OMYF9iMNqAXsmc5BMYUIQZjXMWzpgr_Vzhcdc6DiPu1k73KXKucghoWgNsJdKmw6jcN8mfn1J7fV8GyKIeNCchpJ-Yr-aJDhynQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=oHp2PbhnwQBKtIDP3L4F22-fSsx1M2cWfO9PFh6NjiG9slAUBsCMPJSlV7cMzaNLw0VkesyVKT2u7amydpS0oss6Z4JjDb9gG8Pcojny13sFGCOvaHzBr_kyX93IJ5LlH_-fUGm_gTLXAtc5Pwn78AHFywEBIQgiiNmMXpGj7LC5OS6Tiyp3Hfy-760rfhASnmKAkMzlRfK8j5LMvfPuRMGiKXJxRHjgamkiz2vsRKd8BoAOWx7OMYF9iMNqAXsmc5BMYUIQZjXMWzpgr_Vzhcdc6DiPu1k73KXKucghoWgNsJdKmw6jcN8mfn1J7fV8GyKIeNCchpJ-Yr-aJDhynQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRTVk_5rhs3ocepJjaZUfqpTkxTFpB8Vm1dvIeDVmFSNMStdbcb9siL4K5EFzSM0GSrgtnEgztX4-tSP7LEzKtniXP32WlhtUAP4mApNuAGbszzyI7BEsc8Xp0eEBpY78847RwTbKzy2mUuSZeM6P7FQr9V8wAKGu1qgIZ_mappSR4pQHLNKp4rzMZzs7on6zOXY2SlsOHBqwljU91Wcxdw_L4t8UsMcDwx89PZdmUMmF7TGeeU1jZ7zIepjQLLV4N-yFCgAXI8IL-NAfOElepu7EiKX0dRz8mVxSg8eOY8OBB2CM9QLFcGECHXYC46Q1MNdCibeGznn2buv7LxgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4hijtkHVf_IWl66RmySx97Pz16mzib7aRIxf_ItvMndGWu9Rqj6wyvUzENoMoLEuEdgdgR_OnUgpaFNkLj7QfUZsqOXrqweMgrk_PF8I_PgmCRoQ-q8UL-08wMah0hu6LL3xpcPmdO7BTnzPISVETWpD81yKFeokA3FQvccW0unF1Gr9-5iKtHh695OAB1-AODqO6EI1M2PyTJg7IKYKN4RssnoGyrw-1uLFRNlIMZ1zZCsFgkh-siddp4FNUKhiOc8Ebmqi2CGTcRkYe32zac_Ah6efVtWmqGPkIlGFYBQarwGptLg5qn8wDp7k0COwvXNgsEE2P8MCq-WUPMYSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnZYuMzS5Tl6vZIDhqb9TXMNnpuNnmqW4b6XZO5wmhZ30d6Rh6H8_XD4Fh1CWHQNqIrUhtXQ4i-sRcaZm2ifJEdfbr6OEIeLS7_-B2X5jExansm-5T5brFAok9bfU3Od5kuswreh-VAAqWXjFYnIWsh-XLVhHob3yicLtYuhUwNLc94vu730zQFsoZWe5eOm1knFcqeSgj4b06-BHbbheliPNIG-bMehSMsQGpi2F4xLupvoN4TF4487gxInH6RsST8DaA3_Fdiqqj7dj3mqEvroq3WSaY6W411cT_KkdOStFJs7kXRzQuUN36uCnGEtX_CzTVbk6rwbeKVK0D-efQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=szhNwdltghhgtKGdhdY4KB-8XKiBKxO1ViPKyTHnBVGflJHSU4-ZjMB07kC30NySgpp_sr8b9HcqF-DhqZ2LaUvGsqehJIzbnohYTAYNMOtMNZ8-LR8CX866btPc_DkdtaWYCziCTfI9ISCOKjpW1xfdBNvqhbzTjOePd_TnllJdZzxAzACTcab3eCsT8olC0Kj9iT5hpbMgaSYiUCNsFJQgBJyrdkn8Rjub0YKTQejgt7DkiJ-G1nEQo_vK1ks_C4T2LMxtX0YajatcMFxuAMmjo9kHqP7P5CfrCzIRebfCStgY9CSDQa7xvUaUCqOMahLLkBLy6wJPxG6WdzfVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=szhNwdltghhgtKGdhdY4KB-8XKiBKxO1ViPKyTHnBVGflJHSU4-ZjMB07kC30NySgpp_sr8b9HcqF-DhqZ2LaUvGsqehJIzbnohYTAYNMOtMNZ8-LR8CX866btPc_DkdtaWYCziCTfI9ISCOKjpW1xfdBNvqhbzTjOePd_TnllJdZzxAzACTcab3eCsT8olC0Kj9iT5hpbMgaSYiUCNsFJQgBJyrdkn8Rjub0YKTQejgt7DkiJ-G1nEQo_vK1ks_C4T2LMxtX0YajatcMFxuAMmjo9kHqP7P5CfrCzIRebfCStgY9CSDQa7xvUaUCqOMahLLkBLy6wJPxG6WdzfVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azttwamg30IqSF6IEzakI7sZbX988uyzjP8Jj6Fexc5PbL2pOdt6Qk6MveexeSMhKM2AvnfH3NeVi-o4eubOv24BV5DxKuyJYdcbPEXqJEtaAIFOistVDyCxJbylSBD7O6MSVfQ1T0LNNcC_ucltfvFXcyhbGt6rJgozNXpDbxQNLo6C7em1KSCtXhov2gX_eWoxDVPAcyyflgeIEIT85aKG6trFmUj5rmQvtETrpIzCkD5D86KuHsPPwsO_oykioA3yYE-PoWLHMNbjivsKRsvkLdmwK9ETtK4JOd8Fpk51ttLRXqIP8N6CclkNDadL10r7mCwvUBy6B-VSIEVueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fw4Bl3iolI7QtcKHfH6F_qHE5LR5m7_5mKQZX14B9iT0gmO5LKX5QBuxFrg_dJVSwH9IBn2fbAfRRaJufPLvLvKG39cU1aZnvARI9ILBFN5aV5ATcZT-4IZVzzX_uAkEujmDtW1t9lGQreBVq4har7MlHIHwA-2jTGQzs6cuG2h-btSvF6nhtXJF784QIadzkqDLYbr8H1qYqt4dFtouc5BfCSKLcViItTOcODm5pg0WBVuv5Y7g-Z_r8PT4cajSHIej21KWLU4rVWU6cZpGUiyQ_bBkf9QSysD-9xgC9lQFUyRfPLsXUaz-qOVDCrzW7mNlv8rD8nOtWHWLdaaqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtTMwl-CgqhisQpuCFPpE5FfgTaCocge2pHoP1fVOToYfgnpDRcf9I51ea7E2wHR2dGnooYeG4XemEuLeWMIQe9tIBUk8Rh4zzeGS7-E7hEb3i9O0ctoz652q_zi5Lu9Pw3SbQ1ZNcIup-5dpDaHpDuCVb-uFtlSP8qTbQNzuUury7g7Ym8YcArnlVi6To1EZTkNscwBPJQHhOVVbaWjhwjBgNPZzEzaekgJey9kimtb5eqdPTiJMyIXg4Aj692XVf9G8gO_B4yebSlxPAltFWByppGS9saEEitcjjKTR1sQBFnLCiDAbeZbzP75CfxDFmVAwUm8ZuLZyrfXYkV1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0nzdGZuyBiSeNgbDUZ5LyTCKWvTJX7Stf7Ojga6RxkUIhX6xC5TUChYDRplIdnO3xHB_8-hLb6MwMNAjvW4Ii8My-kq8IX169L_WybPvmgwzuOQmELPF23-r-FnouwzDBlNFqw_YkPWn9CbD55qcfuwPl-GiCvm3QeS_bG-L1nwPK7gDYRDfEbTfvh3WCbKkh7bGXHGDOpHP_KWy7_v-ginrH74pJIg3J2nHxVIg8jKuBjqJHiIlHeWtrH5R1OS9KYROpcWX6yZg-WhT1GXLFnykWk_wWA_ZflEiSxOgRXiuLGT_FKX8ivZ7r7r-Gr1WJk4PePMVUnYcj_Z3wA_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgCdbcyDzZX90mvuBwlAVFZ6x2Ny5OoF1VtOmV9KRFrV-g68rpDNktK8YaFg08_n-lfAXpr0Z5B0FWvJ03vgkn3VXCRG3ug0Qd2lRSLUdKDgP1AGbAySTufQu6FB08ic-PEMWoZqyDog5meBR309GvZap70ev80nMg1yIP4KOHhEhnef6zX-p_CwI6MKHuYe2BXc4oebZOolq0VfcNbeS1k85KCQL_4WHC5jjQ-gd75gQSxbH9snas7S_HhDoQmPshGInhxFhrlmSUbRK0Dc9xJxJrQfpUkhdLviml9-hZzLjJaJgOMEk0I-zHDv0FNIqZDWbFQ25ntqWknUCQBmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DV0CHIDYJV4vRyVh2iz75EhUozIgp2Eo6DwSnDQNVQtC19jBV9aPq1vaFtCUfzVdfpVUCFGFRQYXSZe4XLz7-cGVUY953WSJACEIkuMmQXRJLBDVJCOs7PVC-egi9RrOFwDX-G1yA2DN1XzWyV8NvQGgBD6t7ymY2xqzLDHFwIvZaJ0MKhyQyWiIAQQVn3qiOjAFjA8FPvmJfhsVVdtU2r0zRFnryMKD5JiNEvqzeFHHlZlw8kLDupW2wfhTidghLDlbluyZhVXbhnA5dDcgt-e1k5-wZgp26jirsPIPPhN4vlTVCLFhEGcsQf2ijQ3WO_LTopZgHtUlFEpMZWgqQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzZ0VKvacOjQcCSXNt7gW2u5iXEqzVkLixl7ac98yi4YLD75s5R7EzqYBQimhn2Ao6dO27TYuWzj_FfFhyd-F1EWdfveWcS0hBorc_N6qKZkogQJ-_YuMeZbNRI-g-GPkcHa8ubEewt_wB18-ydJkORYAjrRQ7QGo-8ytWwUyp7eugFIlfcPdb4BGtlcVTP2dWhKqsYYx0Uv95tWFC8GIfQL98hHj3Z_1Tkv06PUOTOMg9U_pK40ZQ1GcAOqkVNmXw9pN1LAwjCKwwu_EpLzjFt2ajK5UZvoWIQoCSyWCnJTDLgTWZJnKb6v7ycN0lpkUqC5B2ezB_7KeRXUzRWxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=NAdxNVsyHNZhH49RueqU3Quo_51alTeMgA6gAMFn3cYvONU3tW0WZolT2ZHIFG6ryC4ZCQlCnCViQdfH7Sr-XeK3miytFShAUrWaju5u8b9TaZdDvesnYIVK_xr_o6o82Bjg8BZ9UYcGV-pwecBCBRu5DA_QSrnRN-gx3vHYD7rlsY-iZ85Mm_pvifaLvRSRWLIW_emmX46heKOh1JvkJQaNZaJSEzo0LaLXdKXjGtU9DaTE3-bmWYzCFEwf2tPnNZtU-jWNx5DLijoykeKfT9rdtw2RoOsSalZe54PoWGcfONDcjpK1W32hvAoni5joV9n1PlKyKdRezs4fTbrJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=NAdxNVsyHNZhH49RueqU3Quo_51alTeMgA6gAMFn3cYvONU3tW0WZolT2ZHIFG6ryC4ZCQlCnCViQdfH7Sr-XeK3miytFShAUrWaju5u8b9TaZdDvesnYIVK_xr_o6o82Bjg8BZ9UYcGV-pwecBCBRu5DA_QSrnRN-gx3vHYD7rlsY-iZ85Mm_pvifaLvRSRWLIW_emmX46heKOh1JvkJQaNZaJSEzo0LaLXdKXjGtU9DaTE3-bmWYzCFEwf2tPnNZtU-jWNx5DLijoykeKfT9rdtw2RoOsSalZe54PoWGcfONDcjpK1W32hvAoni5joV9n1PlKyKdRezs4fTbrJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3cI0clpe7I-HsVfZO8YXxSeO9r5Rn1jz9xSfTBeyBWFkIn-nb0lIxG-vgtYNBdF8TQbGq6F8nlgE06jWmh1gLHNSBCdu5pGUKByUBzL6ZamzvCWzfuIaOW0RqZ3suxm_UDLdsgQGgQGQyaW5zZfVL_v5vkHeAZfaNff2kZnLflfLXrf4fK56NfgmTy9174zVYPkpyPkSDrLOguLpd-Cw4RUIvLLGKyY8CEKoYrpn9UW7X_PSYDXax_kqkOAQpulk1uvV-7fXXnJBM4OkPfjB9Pkt4CaadfjlGiFZMbsqDNHe5KC_XzxMz9M334_ufmitmWIAjd3o9KjlSHQjmVIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPx5wI7re5oZXq8w4-NPuXEIo81g11Y9RtwLaJuHCKfPrENg19aamCyzBGe0V0gapwyFV3x2OTBH4jg7OxTALUDVkBjWKkoO8TbegUUwPdJpPuVZKZ88dgJ4hEGLvfTq-rJwrPLGBsVTmp0DgjhpFmf3idfYmGvLIqS804V4OTzj46g5PpJT92hvGPlzwnPCXTeeOS7Elia6VdtImeyGjp07R5SzVxPHyfYDDXA_50xlgGxJ2tw5-TGZI-UQrudNBgHXb1wSQW0qylmsUjDS2YwXweh-wpGTZJTuNfFUcOnu2FNwVLGKJZCXAUNG8wllmDAMRn_KL--IP4ALC02Sgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7fRbkwVey2ij6EsKNGahC2COEz3hEGqMImRApPDdbzKyANkWuFq6k_0-DR6beHI6mN8pe0lnam6qcOFZ9ivedmr9orEtfae3y175U4j7YfXaHjIhgGZWUVKjupOnYL-urSJGw6wBCycV2VJJZ9rtL7sfmqr27KNCFzuKUHXNKrGfHKJEVW0qyLFCYxslBY8yleKuFYW1UDf7T3uqtEcJijJ2nrdapDp-sG4PYp3MGXa5839h6LDv-V1Yvcljm5Y2z8Y5_aQzOvMhTa-dg7chhZ6Vtu_jFkI-ozDVYs1eExsgb7NFWRX6RC1eE3fflB1uV2XHrhpZ9UQAIgmwI9z4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkBC5cwDv-RBEfjD_-pbNqQUK6g51ApUTeJLMBq12Fd0fAPkTeGIGFQUi9WScBOewNm7pYb4vYLHleQxIlxom6-VETpUfBgaqRoNnDFxB7XYk0o_w-JABAtQfBmdFu6p6Z_bA5c4YMDG6aOQMP6uyRWBaHYD7EVICGTMT6u27Yfot85Le0qJFUYrUfNMGu8xo1N96h-ClJmAc4ozKP5jDs9HeMXBnlfYGWwAn5Y0FcNOltt6DGObwjrCRkOZCQBRinHeVPBzwtxaohFmr_ydK0DrivdtcQpiZA6NCDoIzP5_5qHvceTR9Tbsg4xPZRtMPCc1-7iv9ouJUCtO0I1_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlRC3fqAP2fqnExV7FbFgafmG1udpOEBlFBlSp9GEV006e5eCmS-jil57TXMUJBC5GmBnBW7FWn9asVG7qig4pJb2XwQywnzV-juIfynkPCVV42Oo1xvYrT-31EimrEjsY94uBoLlkNlcSM4CeP3UMCwdsjYvBGitDAcj2zKoN08YJi-dTC-VI-NZ95LaSuUy7rav10va2_0BhD_YWWLoz71GhNYg7wrbEGB05Qd_u5yy8Qwgp2TYPyM6k4dpkAyxlQo9iy81iuteYhbA0Jtfg-0i18jcr_ELnrjyxR47TASaV7MkgrTTbDDwQbWBy7xJTP7SOcYLgHRLYF0zZezIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEE-0XED43xHCF9hFlGokrPmTEnF2XVWXhresdT5VHRgvINlE0xmQi4Bc1f4hYujmOo3YFTljZX5eEPUxU3Yr4QvKx0Bzr_WH8Rk3a3h4Xh9P1xSYVBWd7UKHrD009ds3KrvnotPwUOWwoZaM6rAciv2-sp40rw4pwcHIyx6F0briHxsa_KBPgfKsGaUWOdtt_cixTbRynjoPuOUXCs6CSVS_0t0MNk3a9GUlpdUQoG-R04sx1H2gNnmnYe9OhMPKPkvW8SF54_Dh3gf-LPY9Mdz4NjwlaaCimLjSCjenu6vAnIz4juKm8WMF_VlrZlBbD__LATwGSAYcsEAjDKI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a19pEciebKRznSEGNiyKn8K0nW4m1an4NPb6NNwGUUnbL9vQNIRzMQAksm6Ftlkaab-LRRpE3Ej0TK1wFaYQMa5WBY6XhHqJgutK-SIRrjmzWvqAEDlvNh9RlMDwwulvmqZfdRFpUK2z8fpp7LIuqsQMoURk5lQcBm0JXX0IcmeiantwanyS2NWD2MOJVL5KGhQvCFuQNQ3oS8vZ3V3UW71vsznONnr7BTvtwj8Xk3nGpge3581qzJ41t5Hzx-QslxBmID8u5wlTrQaw_CHhwa3QVVKlkHNZGntrZBNpOOvIY49szaOa8GXEcfjvLmzBP8lN8_sB6fPXS7jjkJOqeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpaGzpx_7FIzWivcMT0vQ4a7CAgaW7cyM8VO-zqWA6RjtSmAQBy15ww3K8acSzcg1ShvIFa0fOTp11TL8jrTw-vr-DoX1ZJAPSqwzIv8s85dGZr5aJKDnMBYLBfqKYycVHl2l92jds8BriMzN6vBnLH5PhbBhkUCxUbGqf-mu7yoMpi904YEK5DU_zgGAYbS2KLSaGSHMpmIqbMj_7zizTY4j6_875jlZmSceSoIGhD1dkZ_0tfDwZT6EO16DI6B99fzhB5wjBSSMC9cEZu7wxEd6-uQxkGz5X1qUcGpc_8o3J21oZkF23FtszFNLmOSKIqaU_pCy22Hj14UCe396g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-EXE9wVtySUnxv3iFtemB-2lBKnB7QfT7dMoMkLajurpgrmELFr-udD3taq-xUaSjCYwbhoZyhEZQn4Lm_gWMkNeIFYSqLmIR93f5nictx6gViZnK7s54cHqBFArUwnbrmbdEOxzM7wEeisaBfJkhM7gDv5ecvT1UwJLRydyEt2s4bNnw8THP1KTBxoT2MgLa567PLlSlCfsoHPw5wFcYR7LcJOSL-o6yGj_ATCSmvTEevyV7LHk19JHXCLcQqeIZ3ZjRuFmP02BZPBQfU845LGn6PqoocYH_81qSwU9NoxRS5ydY5ozAoUWkyrJKJBN530b8_E0pG4jPr2kQAoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=n2b2KRKSw5FShPnkfWPvn_x4FkGKIgH8uimO8EnJgngaJROBRVA2xdCxobIyCbCJ8p73PfEKS8V-kaLuHSAsjEzKdnYC1y30rjzsthIJudIpk1MFRY0ypLlX2YOx9i_eDiZ7IuQ5-Vn6kR90QGFKKppgsQ4G3l4nV1fH9Af9ClQq1TgSbIwUsNHZVNbsGZij9mtv78_uILFXUtLLZwNTioKrwzmqk0NrsPO4cusol0BTjpLHXpU5R5382n4wMJRbLlmuk8st9VwlPLw_3it27g-aq8nqT2nT2MQcD3r4oLRP6K0EqJ1bYy1NhOFZeDEhMgIzG8L3ql_8WzQO0-NCog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=n2b2KRKSw5FShPnkfWPvn_x4FkGKIgH8uimO8EnJgngaJROBRVA2xdCxobIyCbCJ8p73PfEKS8V-kaLuHSAsjEzKdnYC1y30rjzsthIJudIpk1MFRY0ypLlX2YOx9i_eDiZ7IuQ5-Vn6kR90QGFKKppgsQ4G3l4nV1fH9Af9ClQq1TgSbIwUsNHZVNbsGZij9mtv78_uILFXUtLLZwNTioKrwzmqk0NrsPO4cusol0BTjpLHXpU5R5382n4wMJRbLlmuk8st9VwlPLw_3it27g-aq8nqT2nT2MQcD3r4oLRP6K0EqJ1bYy1NhOFZeDEhMgIzG8L3ql_8WzQO0-NCog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9En-Hg62vA2rLc6tGoir_O6fhlWn6Ud2be_U1Lq_cW2LutF6k17xoYDRuI6s27LwUYqlIAm_hsFDMKUA7kxT2WGKr511Sl-WZk_tRb4LcrGbJpGIEObHrdF4ZPS8lb9CFl_aE4RaMkARto214T5BLTh14M9muEvorhQkZsFDIkigbxan2aARWoBAPiqpgioV6YCkn2gg15KrQ9I8Uq6HNgnH98Ncp05KxMJ_hekaFH2vI37IsQdEOlK1UzWlZct34Q8zEWmhL6kDwvbhOh1e8F-nQhJVQbTtA7EiUk5Zt8Pk-ALOf2USxtN-_KmhsMUpe7UABkhGUKNPIDhHftLTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFTrISqbxAEeubooCtYTqNuZ8TfSbCDZ837gZGr3r-v7vqUVGFMAtMaX7ITrHdjZ4SRfq392w9kdvMI0xU-XQ0hxmrO1k33A0PJ_KdER64XV37tkAnu0FAZYSiuhjIuRDSegkFqY4Rp84NAC7dj292Gt5gzq_AQ5xb21v0VhttWztX8_R0XheJMulqYrCrdkSCMcEtTA6Y6IqRrTRMrX_K2ZldXSODK7LektITWkuJDV3MCWE4POSgLUcYlw0sHPXUo_nOFFugDBkRyEWbf2ouUpuMDmUbsdNLVNmfR3qjxn7KyR8F9ddgMvhoCaKrbTN2XwnzpbX5GLHcup7se8Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlEzumpcyY_kCSvfkc98LF3PnCYNWZizuedDG4tjd84yfe4_SWo9NJOcN2QpckmWpIThUyKQDdP0f5z4klkdI35f9nehJD5DAP5Lw5fD2LMwMAo8BMvubjqiN5MIypUXwQXBiYsycDBGjADIGUsm385yfGvSabAUK7r4agAqPdBtxy6gPyObaMVXZzC51uYaE9mKwnyV5m8vxaNxQPACmd7K1vUYxqQP_Drll5DWkgo1FoKqqS12fcG8epLKElQXFZUAYXPxZeGnTtW0nbSoehkN6fafxjePJpz7E87db-vK7KLVIVrSBJ5LQfLo51JZmE84Daax8qxDc4yKEeIDTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKi9F0wqkJQCxA3aTcB07c43QSv5DEjLqsT5iyket_S5Yf0K2VIHzrfaerypOkNsnJBmjpJ3jqnc1s7N3XCT22lEQPH1eHAGBXB2N-Sd92V_GgseJ4Y1ArZVXovXF8myfuAvgEp5Vlo7vH8Z1KX3dFqU27osJFoKKiSVf4dilXit82QQBnQDQnPvrrnT_iRmCLoDTd3yT3jEAPqSKGN1LybQufAMlvx9ct2OT2cvP71-ZmUouaQy3j6NkUaHx4-aGOqQl_wnpHVdQQnGAu423CWuwxmQG3BVena9lXZHghRjLxVpPyGK3AcaAgU9c6K7P5EDXZZ6Bp_TIjM7VG3dcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq6XTOGI5uIdAbCExeVKYN_RDhvY4IN0h-WjrEjkkgKfq-IHbToks7VozFqS6F87leuGAZNMHbn6XyDn8l3dX7s1y3aJSXSxe_BS9yLFOf8t-UbnbcE9Z6wMeIJ_07gDYTfevPETAHXlgecNakIo9X6Z8Rq-WL3iyAYucXgusMTln6Yropx0AUCiawtbSJwFX-_2nj5HFygMOQc4DbYwasUK_sxjBl3mH_tj9y0CtBhdtFVDGbgoSWkczmKAoMQ60XUtzuNHF3_2xgeW_7W8qynt7oxTMxRRDj1wwvph1CcFOzMbrRDwBukAHUmZdzVskUzLsuFoI_CYxLM41BIfBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEaLeiLIbvX2vMYRsC3ExEh0qG3tF9M3csOgcpQEqCSnT-HiOG0YudLR_boJfkXG0mGH54nk_9eEk2ioSKnxDWLk7stOgw99wPnyxAcoBCfVi41VUroJ_WI0atKXtftg-t1Id1RDMEUb6R5QrfyM68CfFrCeeh9QPdd7u1VT-l7BOWviyeqhhcCF2HKXJJiFCkHtprRVmo95kxrJ9GHtnlGO3DiwuWP20IaGvwSrZ2OFXwiVu7R-hbEmgOqIOQcRtXpA-Q10u6P8kE-7pK35REB4Qfb-NG7UlBbFajbWwFGzsWUI2TPatYITdFVpJNZkooaCM7dB3S4EBqL2me3ivw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbAUIyrccJpD9kXWGwMfb0I9r1jsukN1yiwSzYA-asJC0yYlfdbz9Mxhvsk99mfXUoE3G1gmu684VREPXnxfQCM9TEkB0okuNDI9DPg08mpxSIo8l4YPSKUg2A8amROG73BW6thp0fvoZrQKfPYPoduy2nthEzbe4Hs2O428hbvXcpZa_21KAfkf4XbAYAYF2jOvfVpjvFICJoC7Wt6FJagN5Sc1yrFeqt8-IVfmGjhL8Rxk1xQnMbYVNdjzZ-gqMRdT4JtIDLJSz-jwkIbE1OqpjjA2M6niegCWx7R6Dab7SjirQhRlzqV_qahe2o_8Xyiy3-FUMxogGeSksQj1-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IynRiJ71zLBVm0-0lhGZMCKWgGChkSEu3QQFeIKbXa1aQjuW57X2UNCAaVNX4k3gCTketDh8MDYeFCvB4IQ84XX8Ho53V_xKRmwdpLYYEiJJkuvoKeBOiJLv9fimDhd38w9br2rnC9pgZ_ipCnJic-JfPHeJJ9d-WKlmnILsTV8Mn5zHlmEl3yG1gvnq12r_AuhKBzQRQuVeVP9uqmfKKr_kvrXKijTRta8VpmOlZUKhgLedI-8rDn1FbLeMLgo0KdJqQ9QtbvPazhH26nSDgdK3WmrnDpJXLwFDXhmWPx9_-eHrXgfMC28kEyM2XJPDLFoBFS8y_JwYHEtZMSTo4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWEUKCzYuhaUS7Lm0NJDrgBnP9HXnNh4bXgcm7eCwEnyrO3F8oBgiiSmJ3txKBW0YUkVZtCtC363enXRWZoLfj8OfL__VCKnLCy_Nj98Va6wbMDq5Nfu3vZye3IMLemVEzBX-xz_vbn1DwSdiSh1luyRJGPi00RMBw0SS-vdtQJ1l-7n70FVJkcjY2yEGzmK74q7zd5M8lR8_IcrTlolscmyEmr2zBdcQkGMg_Q2egIQ8XUCJ4a3u-HnqiDuRzUrIiqz7C07P1XS3O7wj83idBPT9zo1Mdv5UoIsuEi_Re2YMTSqwbQX83Hi_teOX_XdMKppOpyYA0TPjaDvaKqXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHMDYa1sGUSP9AK_zjvmg7tcpcM53E-YgZeDXVsAqmQ0xCXpRQLtNWwzkwjIbn03ZFmgLqjhIve5rKTWXXC6AAykkS3u3BpWq809UWyBxKROkmmXu6ZxX4eEGy1f_Mr4VYrN7Bx1Rmb8zZh6txT06ty-B4ubdphSjGEBbf8fIY6IM_Ya3A1XWpn8z2IUZaCnqf2RczmHkTZvvX-o8p-GBovzRlhVwHmef9fpe47j7nuiOaGnW7IkTrt5YZ98k9HBqH4GoZo80WCpoPQ8mR-2qbzs8F7XoLns-Mle3U0AKr4lMFdv5aFAn8eURgU2Tia3H5Ftl7AnnRLpgKBEZAG5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh5nCOf9k9Brk1WZz61simxi2V9SuW1GWLfq8KP3nwrD5HrQI_QBa_HbJMbIYdh3RBRPLD0uLYwwsbCWbfrPvspHmeo1iv5xb2vS3nZT7JeD-URDGgRCBaPPSFTI-elFDV6nuVGSIvT8J2YqaFVXL2LVCaNluHjymumWFbiDwF7wcryI341zqYhWX_JZRkqsjR4sj2yUOqNr2-LsgvsLhZNuJxAuyq9TvS_b7CdMXli_8nuMERWqwminAjreiKn2pzXAIJe2f1xLGYYK2xz_YftL-pvjcGXefRPuL5WhkbDZrXL_iFd6IecFpu5H0zOnwWc3e0pFEBdwpVPS_4fx3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
