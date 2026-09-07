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
<img src="https://cdn4.telesco.pe/file/vg7qumNc66eMXZ2cO3boI9fJs26fA5yoaQ9E4uW0p-HU-0vaYw0jIGAhQOMCAYYMtwfhWOtl7Hs1_kbnorsaUsBMRQXoJxJnX3_sV3xnqF0Y3x3D5nHpnxjnqfy72Q49yoMy8EXbNGkY0uKlYuZSQ9x-Lum57PCzLtJXc_4vK06KDuuQ4qNoImlVTwStVOKIWm1o-Y6hqxW_BnHCQsPZUdQgkWitkiS937NgSMgEK-aQ5yIlGboHIyBBaNO6mq6JpFgJ_A2gLVqXAYW4SfQtbHTKs-wo_v0avBrTDCQFMydKOWGYQvMfz8K6pj-q9Qjzlx5etFAUE3XI0yGlbw2HjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-71236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603211e44.mp4?token=XEX2PU3dDdyqenO9jn2AClVltmD8OjLGc9EA1vPduK__Nl1PBC7512WbVLPPWOWUflJ5GxeboOyluHbteLYPDG_4yD6dCe891-M-f_jMoNxIv2hphEs53508yYoyTRvoUIXCeu1Ag5djCWsYE8VQzMwS2WQj0J8llSy459CpENmI4xa6dIWhorB2_Z-7hz3bzaP-_-uhHeb2xBKoRxSoTFame-sHP_UTjG_nG3MMxjD_qkiPB4QOWnjVX0vaz9r6TaA1AxalCTUgECGfO6xocwkQ3q6yTZ327-x-iFEX5usBRpgshB7DyKwzqLCvq8Cua7f4PqxzLfjrLvVIo-OFvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603211e44.mp4?token=XEX2PU3dDdyqenO9jn2AClVltmD8OjLGc9EA1vPduK__Nl1PBC7512WbVLPPWOWUflJ5GxeboOyluHbteLYPDG_4yD6dCe891-M-f_jMoNxIv2hphEs53508yYoyTRvoUIXCeu1Ag5djCWsYE8VQzMwS2WQj0J8llSy459CpENmI4xa6dIWhorB2_Z-7hz3bzaP-_-uhHeb2xBKoRxSoTFame-sHP_UTjG_nG3MMxjD_qkiPB4QOWnjVX0vaz9r6TaA1AxalCTUgECGfO6xocwkQ3q6yTZ327-x-iFEX5usBRpgshB7DyKwzqLCvq8Cua7f4PqxzLfjrLvVIo-OFvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی
:
چهل‌هشت ساعت پیش اولین موشک ناوشکن خودمون رو بالای سر یه ناو آمریکا تست کردیم
واقعاً یک جهنمی به وجود اومد.
🎙
مجری:
موشک بالستیک؟
🇮🇷
محسن رضایی:
موشک خاص حالاااا. موشک خاص
😟
ناوها فرار کردن.
حادثه آنقدر بزرگی هست که سنتکام هم نتونسته نفی بکنه. اعتراف کرده به این
@News_Hut</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/news_hut/71236" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJyodev9TSJbtqRTnbqYvVmfkNaneD70bSld43KH2OdEdt8d3YO0UgbqZ-p4gjw-NjgTg_yceNiQwtKpXOgB5olDjuTJnaIizjxnl7IHH5UYeMES0XDDxjGp7xCLZT7xW2oaLd0EmmO6CFW5ZQRLLgoc5FHe7qGTWAxnxFETHy4gSqz_ykDgLlBSz63SlIqBMHkIRacRPP1LKX0ToQVgreatfEp8HnsmpZiCjlpoCjALoVNPM2BP9H_ntdkfujWirjMdTWUnu_ikk8wXyy3W69ryEGYNB05fpc6axwC49cDbmGaLyWFs2PRTE_5Z_i9u81PjAuIIKvFFxC2WqAdipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
⭕️
🇺🇸
👀
افزایش شمار هواپیماهای سوخت‌رسان آمریکا در شبکه مرتبط با عملیات ایران
بر اساس نقشه OSINT منتشرشده توسط DefenceGeek در ۷ سپتامبر ۲۰۲۶، مجموعاً ۱۹۵ فروند هواپیمای سوخت‌رسان KC-135 و KC-46 در شبکه مورد بررسی این نقشه ثبت شده‌اند.
⭕️
جزئیات این آمار:
۱۶۶ فروند KC-135
۲۹ فروند KC-46
مجموع: ۱۹۵ فروند
این نقشه پایگاه‌ها و نقاط مورد استفاده برای مأموریت‌های تانکر در مناطق تحت پوشش CENTCOM و EUCOM را نشان می‌دهد و علاوه بر پایگاه‌های فعلی، برخی پایگاه‌های مورد استفاده قبلی و مسیرهای ترانزیتی را نیز دربر می‌گیرد.
در نسخه فعلی، تعداد KC-135 نسبت به آپدیت قبلی(3 اوت۲۰۲۶ منتشر شده) ۷ فروند و تعداد KC-46 ۲ فروند افزایش نشان داده شده است؛ بنابراین مجموع ثبت‌شده ۹ فروند افزایش داشته است.
منابع مستقل نیز در سال ۲۰۲۶ از به‌کارگیری گسترده تانکرهای KC-135 و KC-46 برای عملیات مرتبط با ایران گزارش داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/news_hut/71235" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjnQmBBEp_55Q2TdX4Q5aeRiaVgBMQMDakOA8C-_MaxFMFA5o76i329RT4d6eLdR0ZxshXY1gMhkWr1hdVf6D_btpgbC6EsvtnNkTytL_N-ogIte6wWe_OqBV_R-LIoS9sJPr2XljfLLaXLaAYvLpahbYtivWeJnCGpgmGv0U9_qsRHnlvXhJV0cWmmd7yjy2klMRbW3BpGRDDzn0xcNyRNcDlnIH5WvXIKBnBKmgodDHfMApJX-W0iLpYQ_Sk3FBkuvT71oxzCL8lng91BxRSQP4ROiDkV2-jGPrmRVjGMYEA8H-JShtGVd9u1ivoqE_LTMLfFcqDfX9zNwAw6QtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
موضوع ساده است: زنجیره تولید نفت و گاز در اینجا گسترده، در دسترس و آسیب‌پذیر است.
شرکت‌های نفت و گاز آمریکایی که در این آب‌ها و تأسیسات حضور دارند نیز در معرض همین آسیب‌پذیری قرار دارند.
به دارایی‌های ما حمله کنید، ضربه خواهید خورد. ما پیش‌تر این را ثابت کرده‌ایم؛ از پایگاه‌هایی بپرسید که دیگر کارایی ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/news_hut/71234" target="_blank">📅 12:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=C5-M5xZfIvisoXI4NAiE3-lrFjUDoiSYBk0IOzEfkv_8_e3sziRIsObaGBkSqFDFCtI9GRt26qdaDGT3GYZqlRQAhlO2U9UFBd7LLs5_7DXm_0yt2yvvaWKWDjf5IAV2m-UH1HhR6gpQRSNWmUXrvq-Zl0KqrUEfyC4yiieEVJ1NF_iCyhzVII3dmwjGEYxlje7GSMUCGCIikcLi4n-VAFo0pOliVva0j5mnhHyv4feXEJiXqlUu7wqHEGG529HDw0isXxWfDUpYWhJrTPsLVAfGCwp1Qe7SQo2GLnj8RgG-YNkLEsg2Uo2kuTXaQv1_j5QkdCOQw5ru3_5Lv72ghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=C5-M5xZfIvisoXI4NAiE3-lrFjUDoiSYBk0IOzEfkv_8_e3sziRIsObaGBkSqFDFCtI9GRt26qdaDGT3GYZqlRQAhlO2U9UFBd7LLs5_7DXm_0yt2yvvaWKWDjf5IAV2m-UH1HhR6gpQRSNWmUXrvq-Zl0KqrUEfyC4yiieEVJ1NF_iCyhzVII3dmwjGEYxlje7GSMUCGCIikcLi4n-VAFo0pOliVva0j5mnhHyv4feXEJiXqlUu7wqHEGG529HDw0isXxWfDUpYWhJrTPsLVAfGCwp1Qe7SQo2GLnj8RgG-YNkLEsg2Uo2kuTXaQv1_j5QkdCOQw5ru3_5Lv72ghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بمباران آخرالزمانی پادگان فتح خوش‌نام کرج توسط جنگنده های اسرائیلی در جنگ ۴۰روزه
@News_Hut</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/news_hut/71233" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/news_hut/71232" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p94bvqQKm_pOqXURIopkPXLDV85Jx2hv7UAwEYWzr_Vzm-4iHMs4Rm8ZD8CnN_4KtRbsflVCDLnwGAsfw1rEC7z7gwRF3lGu8nIlJby3I_7e3EAoZnRNL8rX-DEVfxwXAI0ccu9mxFGoZeAtjkn3XeK3WXnp7m7C05F5MVEB2_vQyxcoiMxFrXvDg0YR4zuwPDBIEIGUSb776ZytYVvDa9Drv2ckrmC0qFWz3WF2gCOjfLWyAPcvEiPOpyXHzyutJLuoYBaOTAC_5zO8Ijq2TjzFuc3o4rLUNXGvg9VixCHKWDX7CXO--ogbzFXLk3pfPlgWhnqh8gs0Goc0eOWLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/news_hut/71231" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71228">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=kUb-8VXwaBRDoD5SYvNrRyxHtR8r8vymk0Qdk-fLaMr9V8V7OGiLVEfMYYkFm0fEc8QUnHdzJ4C4-3Otxf_sPozTmz1SjqbjFYLdVepVsfSAkhuP1dwEwrsnl-sWbgaiHDh61idtfjqUqucqWQeRkepqoM2Xalyxo9-U_cm1wOr0abkgtdSksgVYrE1b9-GP8KlkefhmRTCgeY6qbm3c-YPhOGpXG8Ofs_zKKn4YGsWjCX1qFWRFD0k5fwOULoZyET03Rk3own8P11ufl272ih1Rmall6uqR0LhpHk7xRNtAZU9zHQHgVK6nDdeyf4zHXcD2LHqkKmytlAFaA8PPog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=kUb-8VXwaBRDoD5SYvNrRyxHtR8r8vymk0Qdk-fLaMr9V8V7OGiLVEfMYYkFm0fEc8QUnHdzJ4C4-3Otxf_sPozTmz1SjqbjFYLdVepVsfSAkhuP1dwEwrsnl-sWbgaiHDh61idtfjqUqucqWQeRkepqoM2Xalyxo9-U_cm1wOr0abkgtdSksgVYrE1b9-GP8KlkefhmRTCgeY6qbm3c-YPhOGpXG8Ofs_zKKn4YGsWjCX1qFWRFD0k5fwOULoZyET03Rk3own8P11ufl272ih1Rmall6uqR0LhpHk7xRNtAZU9zHQHgVK6nDdeyf4zHXcD2LHqkKmytlAFaA8PPog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇶
#فوری
؛ بیش از ۱۵۰ ایرانی به دانشجویان عراقی در سمنان حمله کردند.
🎙
به نوشته خبرنگار بغداد الیوم در سمنان:
گروهی که این رسانه تعدادشان را بیش از ۱۵۰ نفر اعلام کرده، به محل اسکان دانشجویان عراقی در دانشگاه سمنان حمله کرده‌اند.
گزارش ادعا می‌کند پلیس پس از اطلاع از حادثه به دانشگاه رسیده، اما هیچ‌یک از مهاجمان را بازداشت نکرده و صرفاً تلاش کرده درگیری را متوقف کند.
طبق این گزارش، مهاجمان وارد محوطه محل اقامت دانشجویان شده و تعدادی از دانشجویان را به‌شدت مورد ضرب‌وشتم قرار داده‌اند و در نتیجه، شماری از آنها زخمی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71228" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=lx-CWXgzRkNJKGXaeHqI-6s78EAbOjZQlvD0anoD54Oic4K2JMYlBbUUVv_DHh-oACJ8K9_wNQ_L9yc6XPHJocPsyeg9CrRWsBk_zzKMmVhxZx4ZlMhOV9VUj_85JCBLrDk0N3tHZugb_GWoJNW1CbrBLXafllkdjP4FxKD6gimdoUMSTsAb0zojHDL1zhstiSKChMVw72BSbVwZQELrR87_hb05d2ZAOmEajHSN8qcVsMoejUwbJFvAMu9DpQ1aGhI6vEA0Oo_trJFDE4t4dYbIp5Ujt3r_vQP2_URKuvEqzyBimykY-ql3DqbeKtxHXonElAaGPlfc2Nm93T08Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=lx-CWXgzRkNJKGXaeHqI-6s78EAbOjZQlvD0anoD54Oic4K2JMYlBbUUVv_DHh-oACJ8K9_wNQ_L9yc6XPHJocPsyeg9CrRWsBk_zzKMmVhxZx4ZlMhOV9VUj_85JCBLrDk0N3tHZugb_GWoJNW1CbrBLXafllkdjP4FxKD6gimdoUMSTsAb0zojHDL1zhstiSKChMVw72BSbVwZQELrR87_hb05d2ZAOmEajHSN8qcVsMoejUwbJFvAMu9DpQ1aGhI6vEA0Oo_trJFDE4t4dYbIp5Ujt3r_vQP2_URKuvEqzyBimykY-ql3DqbeKtxHXonElAaGPlfc2Nm93T08Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از روز انتخابات دانش‌آموزان پایه هفتم آمریکا که این پسره ادای ترامپ درمیاره و مثل ترامپ وعده میده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/71227" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc7xOlfY3YqTvPdydwii0dsipJOdwcfE0nO5xdQnm53Zl0oekTCgQioAGbK4Toup70ccF3ygrIf8tuFCnEeJaMqAGic6D0nqlbBQLlzHJ08J3-bWm_sCKWcmXkokc-vNuix0Ky-35opzmIGMvD6uV7BqgReM8sbXPetcZlNQGGU9kdAbixmbInnHk-QyF1BJ97f5IAQKdGYE1UchuXBojwsDVYI_86E7z9JfWZqMuCZ70NaRqCVJlUbExBBFReqSclRIhuNFvPa7RUfrG0XZ4SgxM3kyDS4KOm81iCLuwJhqRHsXqw8p1k5qTfFGTl9gZqgQbRx9lkzDlFIdCDrVLX99E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc7xOlfY3YqTvPdydwii0dsipJOdwcfE0nO5xdQnm53Zl0oekTCgQioAGbK4Toup70ccF3ygrIf8tuFCnEeJaMqAGic6D0nqlbBQLlzHJ08J3-bWm_sCKWcmXkokc-vNuix0Ky-35opzmIGMvD6uV7BqgReM8sbXPetcZlNQGGU9kdAbixmbInnHk-QyF1BJ97f5IAQKdGYE1UchuXBojwsDVYI_86E7z9JfWZqMuCZ70NaRqCVJlUbExBBFReqSclRIhuNFvPa7RUfrG0XZ4SgxM3kyDS4KOm81iCLuwJhqRHsXqw8p1k5qTfFGTl9gZqgQbRx9lkzDlFIdCDrVLX99E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرفداران حکومت یه بازی ساختن که برگرفته از بازی مافیاست و فقط نام نقش ها فرق میکنه.
در این دور از بازیا ترامپ برنده میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/71226" target="_blank">📅 11:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=IiATQjNxL22OdKVjCDqxcoxy7bG66vheSXU7J6X5AI1CYTm6m9SmZ9jYXhTPlc_yPsNCOchMDh1flO3-hJyy_bvipUs3bAWrPZAYk0ZjLo8FpWCwXoWSNDe_PmTKbd2aoj9Zk2h5PK-BgPr1wkgBWAELBVj20hud3jg7CccQVM18BzWf3fHobbSuY2B0g5K8fjPXlwjnO1av76tBlOoNLSbnZXrI56mt03UPR-YAyeLZvXRuku8ETWI89hfHqvMs9qQYKsYOVHUQabf79G5T4GJCAWD99Vl6xz2D_plSKFbdB-FD5tRvHoyPA_DcG3txj0UVEfK7Qx2djgkDa-XYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=IiATQjNxL22OdKVjCDqxcoxy7bG66vheSXU7J6X5AI1CYTm6m9SmZ9jYXhTPlc_yPsNCOchMDh1flO3-hJyy_bvipUs3bAWrPZAYk0ZjLo8FpWCwXoWSNDe_PmTKbd2aoj9Zk2h5PK-BgPr1wkgBWAELBVj20hud3jg7CccQVM18BzWf3fHobbSuY2B0g5K8fjPXlwjnO1av76tBlOoNLSbnZXrI56mt03UPR-YAyeLZvXRuku8ETWI89hfHqvMs9qQYKsYOVHUQabf79G5T4GJCAWD99Vl6xz2D_plSKFbdB-FD5tRvHoyPA_DcG3txj0UVEfK7Qx2djgkDa-XYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای عجیب یه آفریقاییِ سیاه‌پوستِ ساکن ایران:
خیلی از کاکولدها به پیجم دایرکت میدن و اصرار میکنن که بیا وارد رابطه‌مون بشو و با زنم بخواب!
حتی یکی‌شون می‌گفت هرچقدر پول بخوای بهت میدیم تو فقط بیا..
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71225" target="_blank">📅 10:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-D3vaiopHeDL6i71Us6X9JGOLM3xXvFFML91idN0RPTP7wj1DQdbLYAJZwTpw9YDggwx4nvaKpSD2Gisgjntrk0uQoy0J8HyAkiTzu2rNrkti6HORrRxcGqNYhHcaO_yH5yChxj4GXYHZ2wIdjfDsROPmyYPNQYre5T7VFq6c03CrryVA5FFbbDhKmrqjuytAXkfUHQQHppJQJv5r6UU1aZQusOLBwqA8zcn2uVOYW0qwBJDaGYcQwaaTPDfBxlDZx0zU7oHjPiAxJJRGzw-rDGfOIKroW9zoNfE9AivDM9XJV-dSRXxY1D2wOdC7HATRKh_jkqCLossiF59us0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
شاهزاده رضا پهلوی:
هم‌میهنان،
جمهوری اسلامی بار دیگر با افزایش قیمت بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خود را بر دوش مردم ایران گذاشت.
همان‌گونه که در پیام ۳۱ مرداد گفتم، گران کردن سوخت در شرایطی که مردم زیر فشار سنگین اقتصادی قرار دارند، اقدامی ظالمانه و خیانت به ملت ایران است.
به رژیم ضحاکی و رهبر مفقودش می‌گویم: فقر و فشار اقتصادی که بر مردم ایران تحمیل کرده‌اید، نتیجه مستقیم سیاست‌های ویرانگر شماست. منابع کشور متعلق به مردم ایران است؛ نه برای پر کردن جیب مافیاها و نه برای تأمین مالی تروریسم و جنگ‌افروزی. اموال غارت‌شده ملت را بازگردانید و حمایت از تروریست‌ها را قطع کنید.
گمان نکنید با کشتار ده‌ها هزار میهن‌پرست توانسته‌اید اراده ملت را درهم بشکنید. آتش خشم و اعتراض مردم خاموش نشده است. ملتی که برای آزادی، رفاه و آینده‌ای بهتر ایستاده است، در برابر سرکوب، فساد، بی‌کفایتی و تحمیل فقر سکوت نخواهد کرد.
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71224" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSmqNrObdN7aS56l-NSEl--SurarUuVJJTYayUghUfZOEne5s_4EoiRZ8_UPnIHxLnhY1hUlCHTkwXOVePDiZiojVXuAGQRhqpi-kW56GEASWQBy4YSaLxaiRyJYS8xg2q-OZT6Vwa1OnAB22s2k6R5jYTqYOwgLqjB1i9LtVjA2Jp2E6nwjkWVpI9SxM5GLTdlmbT12LxYznsjmp5OKWJ2-cb_qUM7z4U9Tp0G_JjK6cWi4x4NI_m_CAHN2gvfhJkhURHxXf7iaH1z46clwUWkUNBfv40j67UuhBiof4amnh2zwUAJusYVJOveJtkMkZstf51PbE0jxJk2fDCffZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71223" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=K0Koly-oS4LP4CcErPiod32F0Q79ONxegOv2rTLAgDpPA1df3-4oRElvtcSksF2ZoTj1m7fijaqlq2JM3mAcYMP-wbVBGqh7tWCwOWxa5aJuEjOs8KgFqU7Bsla4XDjZE-On2UrmznPEhtZHsp7Vhp16gGhrJDanWvQNMExZprMa6ChYw5Tjh_MHQp-_W42xQjm0NJLHYwrpsjiB97CvJx87rg-HCWPRHlFsfkM6VayTzPx3UQ6Q31gib0hrafnTzgBORoo2A05q7dJrRyVoaajj1z2bH7z3F4pn8J_7YcVZtTjNviUQKgXqaectp13gyCoLKhCMSAeCm2oKN_zf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=K0Koly-oS4LP4CcErPiod32F0Q79ONxegOv2rTLAgDpPA1df3-4oRElvtcSksF2ZoTj1m7fijaqlq2JM3mAcYMP-wbVBGqh7tWCwOWxa5aJuEjOs8KgFqU7Bsla4XDjZE-On2UrmznPEhtZHsp7Vhp16gGhrJDanWvQNMExZprMa6ChYw5Tjh_MHQp-_W42xQjm0NJLHYwrpsjiB97CvJx87rg-HCWPRHlFsfkM6VayTzPx3UQ6Q31gib0hrafnTzgBORoo2A05q7dJrRyVoaajj1z2bH7z3F4pn8J_7YcVZtTjNviUQKgXqaectp13gyCoLKhCMSAeCm2oKN_zf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک سرهنگ ارتش :
از فرمانده‌ی کل ارتش ایران تقاضا دارم، یه قایق پر از بمب با جلیقه انتحاری در اختیار من قرار دهد تا خودم را به ناو آمریکایی بزنم و منفجرشان کنم
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71222" target="_blank">📅 09:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=QLri2094H8ix9krd3slAxk-sZsso1fprXhNq7AAlCBaiGxn3sCrVnDqIGwIOylIRrDVJ30DxIUzPNCQ90msJGxuo2HZegs92HkWYivr9YhXI4P_xDyZfW1THgA6VIz9it0MbrUGwHiJg1W5XJWScgEARC9HqTucHvgsOUyFO2BSaGmzA0fZWr5sAObWE0RRlZ9m1u3QP_F2DHpPWAMBtIPCn7yHjsOfTLuMAdX30pJzRHcEicEcI0aMzugYmKKwflt3Vu9h1oHZ9WI1Ms-XevWN1MwlEnCDaa7Kk22cjKLYIbQye4wM23fa5mJRKzZtmXT7lq6_MqlqnJZqY1cuTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=QLri2094H8ix9krd3slAxk-sZsso1fprXhNq7AAlCBaiGxn3sCrVnDqIGwIOylIRrDVJ30DxIUzPNCQ90msJGxuo2HZegs92HkWYivr9YhXI4P_xDyZfW1THgA6VIz9it0MbrUGwHiJg1W5XJWScgEARC9HqTucHvgsOUyFO2BSaGmzA0fZWr5sAObWE0RRlZ9m1u3QP_F2DHpPWAMBtIPCn7yHjsOfTLuMAdX30pJzRHcEicEcI0aMzugYmKKwflt3Vu9h1oHZ9WI1Ms-XevWN1MwlEnCDaa7Kk22cjKLYIbQye4wM23fa5mJRKzZtmXT7lq6_MqlqnJZqY1cuTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان زمان انتخابات:
خیلی‌ها میگن من اگه رئیس‌جمهور بشم میخوام بنزین رو گرون کنم، ولی من بارها گفتم بنزین رو گرون نخواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71221" target="_blank">📅 09:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71220" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71220" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_dX66uuWYUSmLfbvOrsPm-bsW1QvFAfKGCqu7_nBdLDK9aMJrYauLiiioCCD80mvD4WNG5uJ0NYSyw2WdWwgd8cTP4TWmh2q7rca66QXoptbLRgWcybuhAQi1gh6OvQzzWZrg67tGFfqZmjE6Cg2bGgSEKKoMYg28YB8xGddViDO-wM9H8jBKP8qvH5bKrwPxnJmrDemh1oeQD-Nm_GShvdSd8BuhgxvDNsgrjqEEbFi0cNLv6fuDEo1dhRd62U0q7Lt-ll97_lYk5SJuJlmMm3SdvtuyduK0kwDl2tAr_9ixw_abOJmu1WBR_vWJO4HqSxBAz-a_OU5D2eD2fw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71219" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKnuvqtAN5pl67Li7FFAmn6_xoNmotiwmxg-DIno9MZSVQ1tBa5At9p52LFlAmCbQTiD6rTD3TYudWBJfMHLVfnsKwoAZBVw_g_8okQahVcePrO8C9fh-ZkeKlA09Ui7SLVvvk8AF9j0zWnu9x4BTF0Pd4D2hDGgwiYiqpKV6m0cXyZb0qn8F5GTtQvH4tZ24NOh38fTh1wsS-qvoK8Bt-b8H1qCYnD53EyYsHAFHpJf1rKoWzszbCfNzuBDxDT3UM3m3aIfkVNwkOf-Y-LJolHQ3_ZoVxQYZYxrtIi8pyUmu7nndiZ2SEAFZMO9mzsqfEl4xnhVroLCp69v2t_jzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohUa1UStQbOEl4Ro8-q6FAPo0g5Wbm6N9kDYCRB9QGmnCg7SzSYM-JZgxuR9UuLorRa62HRWZEhni_N7SglgaZlYX3VaVwISqJaAKfi8HysFhtCgJps6oVR9WrH8fCZfCTrJXve5XjR_bwVyW-DtltD1z5LxYJBwmQ8KKLsN_F9EaZAH8PVGhkFYe7PucabOUAYH07HKTptEMAt5yxsy-_lqr1yonXPd2gjnJ_IwCTe2LdK-3m-V5YuyfnWncUfxjHfN8D7FNaGn92gLRwGabRYMmDqkx-lNiP597iotuig3G7xVcxXftULNZc541n5NAjtYKV9KbNDoZimEkiqkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2TtLjdllkED_i0NlqGAp1v_t2kwZp8hahZ727HGxrTXEqcKyTPCr_XMRqYGCpN1WfdonjyY3FhcrJ3OmViq5Nv2nI1iH4TURL02IqGdFPtC3F3acriBFcrjOqyPl5XjftNL5rBBXbg_y1f3uGq5c7y4E2vU9mnc2CandtR2ipXdcCPjNUC7OZyAKOpi2At8_l4C01UbZJDNeDtHN4SpNmv7k5hwvPqbE0VuFAA5wjHdkoI168efqynYa4Uik-naEFXD5YCKievtc7aPEQOsHZzpk8z2CgP6Mdq1UB7V8JIvlIYwnNtnQHWpEPm430qEsi42IjfYJs-43tce8OuBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGWS3Y67BrLnbh_WFijd1p23o2o1TF6oAD-PMEeXzZYBbpb1G23zu4Lel-bCxm5XRk6JuS8gdBosNxUsPJRJtcqtXVzC5dWh6VWuq32Neowb-Ah20NiE87V5WkRx2T9LlNkGC2SDQW34zQsZn3lBmSZBKlyEEkYN3ojxiaaiohlsxrIAlSoGF5pHEpTaq7A3Vvl33ERaATCUPx93u4HxcOANpjFMkXnr7-1a6QgOU298rnwWMz77CBBhlZ4qSiH2DBapJCC7OayOg8ImsF6Lbv8ms0ZMs64hugzfyCSGwDkg4IPUGWLom7eCQb5A9xHOhYLocxhvyWj_E6kMauNmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPCKOJTdLND3wPmtZHWpEzQiPqJ8JPsGX16uhURstXoE2qVPzGYtAikdhnofXE0dGyza0LaDsb9AOsgcsbOWW2-SvF0UhrorsnXXKFZZTdDXKptKmGeHm6dmGBfVpnYCiDRRUGGaso48qVcLyUiarlQ7_JO9p6oShx2m8SSwLxbPVs1vUB30a0rRtcrdYjVYu8T6fwxIMoy8XSTVR2z-2tZBSx-X1lhSp5-noBZIszr6tkcpVWJIzjRxGsWbnPnIns21dLCwap4BP9toNMZkZLn5rQnckih5-_S7cfp8jcRjU9V7IKHw1NKtaQqpIgClNdAi0L9-PgCMCr0I6nkbMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ:
۱_ایران کشوری در حال فروپاشی‌ست.
۲_خداحافظ جزیره خارک.
۳_ارزش پول ایران از بین رفته است.
۴_صادرات نفت ایران به شدت در حال سقوط است.
۵_ حجم‌های نفت هرمز به سطح قبلی بازگشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71214" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71210">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWXjQ6Bl6OFQmGv1lt67WzMgjKiscDkHLfw2U_Tt76xwYisPHztLsgPL5eExf_LfWs1XuOT-N4NT4w33kMR79w7jpKq-7myqFfT5S2gN3PwfKKKcggiNCSWwfzMNGpU13aLbDxUUnZBPY-atUlQ2dYA6qZINt8dBASrepIHE9fDh3qQc-SOevvmtuNWN8qEK5BHnUdS4XWM51Pc3ToHosbJKvNqPkDuuSOkz2DxoZKhvpPci3pvb7sckmU_fEkRFbAg59gosfJk86A9rt4Eb97HPsYy1KLd5hSlJV_yXhFf-pBBgEw_95N24qbTbaHZjBpAhLEwBA1FxdR0ihpFWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eK-WUBAL-agDyyVeKy22WIlfaQzDbY2AJuhS_Uhs8f4VPdGTEKSI-q01_eOyCdD3olXUusebXvbj_4KxzK11JhVmvoGyGhKbakwigRXSpKo4l58NN0Xv_B1k9np58NR8xDhL8saNItwGzWeXv81y0m_55KLv9NiqE0VarsQdc76UQ9JZr5szECQ-b3kZhyTYxfZl8H397Q53Dzrnxw73W9VLhVMYkAdh8as0Bnj6GVPnZGThYhK-93pV_aLVLk-hIjjAitniwmWURB3IvOMMViGjg_G3O7TyERMv1om-7CCtGg27HLg4ado5vvuWCfW1Rn-xn02PhchnHmMsZyahKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ در تروث سوشال منتشر کرده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71210" target="_blank">📅 00:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71209">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=EHFUEtfZduXDWPSMApuL0aBEPEHrX4pZ8i2dnSY9FpoH5kBiJ4pkEjxPmJJfS9t9IIS5gdWpjJnkYjjocXO9DHtgPMgiNplQlJ8EKgmxCKRJ7TByXUHni5Tszj7b6YXi7DRgaD1pitCpMpgLGtXZjo_kyJrahEIesQYw2bXF77pzmhUyWGkGwh3FmXNrVfU55rb6r1mU26vQQtNU1Xe5Y0xobbioci1L1ACo9ukurhz71BjIW1WR7BFOPW2C-_HtX0Pp9A_qBtCxCdHkUhM42w20hLksXcHcoxsqwFzJ33V8VQ5ZYZa6BbtamLveEt3dXtbl8TpAM3QnaYTDeQ1eQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=EHFUEtfZduXDWPSMApuL0aBEPEHrX4pZ8i2dnSY9FpoH5kBiJ4pkEjxPmJJfS9t9IIS5gdWpjJnkYjjocXO9DHtgPMgiNplQlJ8EKgmxCKRJ7TByXUHni5Tszj7b6YXi7DRgaD1pitCpMpgLGtXZjo_kyJrahEIesQYw2bXF77pzmhUyWGkGwh3FmXNrVfU55rb6r1mU26vQQtNU1Xe5Y0xobbioci1L1ACo9ukurhz71BjIW1WR7BFOPW2C-_HtX0Pp9A_qBtCxCdHkUhM42w20hLksXcHcoxsqwFzJ33V8VQ5ZYZa6BbtamLveEt3dXtbl8TpAM3QnaYTDeQ1eQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دو عدد سیب زمینی 100 هزار تومان؛ اینکه قیمت یه دونه سیب زمینی بزرگ‌ به ۵۰ هزار تومن رسیده‌؛ یعنی فاجعه اقتصادی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71209" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71208">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=pHzcDFK7vb6XBTWYxnWoZBHr-7h8ncBZsjSaPHeoTa9N2b5lz53MTesj6TE3L9PxiOj15YbGjsmwun2DMOsIhCA-U9-cl9mR1GhHGWrUnWcqD_rURjMGfIHKbXKParYIN332S1ZRrSOSgUy2u62x1AZfAgRbBiz2WdE88MlYWOLHAfVM65nQ7ACFl7aEC5qtz7GLTFEzAV41Whq942pZhP4fCdMwPsmpBxBN0GhCo-XTK_VQ6-XxdJpDRaol2iCJf55p4jnlVsiVH8Aor7sz95Qvs3AbjDjClpuZIyMnyfBogAi0XFY9w0uLodnGJBSYXiZ-KNNCz9UvJ7-R0qD2aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=pHzcDFK7vb6XBTWYxnWoZBHr-7h8ncBZsjSaPHeoTa9N2b5lz53MTesj6TE3L9PxiOj15YbGjsmwun2DMOsIhCA-U9-cl9mR1GhHGWrUnWcqD_rURjMGfIHKbXKParYIN332S1ZRrSOSgUy2u62x1AZfAgRbBiz2WdE88MlYWOLHAfVM65nQ7ACFl7aEC5qtz7GLTFEzAV41Whq942pZhP4fCdMwPsmpBxBN0GhCo-XTK_VQ6-XxdJpDRaol2iCJf55p4jnlVsiVH8Aor7sz95Qvs3AbjDjClpuZIyMnyfBogAi0XFY9w0uLodnGJBSYXiZ-KNNCz9UvJ7-R0qD2aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سعید لیلاز، اقتصاددان و کارشناس اقتصادی:
«کشور با تذبذب و دودلی، مس‌مس کردن و فس‌فس کردن  اداره نمی‌شود و حکومت باید تصمیم‌های قاطع بگیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71208" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71207">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEBXEUvRmlw86s5Vw-GxC14JmXlPtzkCHFmQv4kAMfVkCFo-s-krO6H0a15uRCxeZ6R_DE1-D9lxNF68UDO2MFdcN4ZtG3hmQExhngqF9Dm-R5OQyIJwE4urk6UoW443aeU5PAQE22eX2pI1mHeZ4zBqKkVlKkoty33WAP75JcmbqYOVe7K5ZGAngglLoG2W4cb1Odhe5brYj7JvwFEqZ_FONMez4lEYQpleeCYGZz_6OEpOd2g8lixdAeFl9N3Vg1ABl0AUPkaJH6Wbi34Rd0lSZWMwFgjKM5f_r2LsfZ8iLyaTY7OMGdKAr5WmGumXkwWV0qE27YdmSsP1F4Izaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث که اومده کلشو جای نقشه ایران گذاشته
😟
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71207" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=DGVfqA9P-2l6Ft0TS6-hx9ZUs1MvB2KfAQuCuNF81DfssG-ycGa9J84tGHuxH0Qd1FjdVPUANdOYzP_eGipHjTyAh-2SpooYUkFzHwflvY9JAQiUzMP0Wkshqtw3pggX7IBXd_JhSkvtDKb9oS9aQ18GwTin5FwhImVXowCIMbiFdj3vJf_UaQRpTsxGhB0vC1k2CWEgpqbcvU-ucYmuYLXlEwUsP_-67BJs9BaKhZfgE3IBEgvBcKkdJQBD3MveW4zgjOlGMnPSdO_ztiZyvYLLRzblOqg7LPZ3-ZDv6yQAlYN8stKOCQZbTb1kHTtz7fxsuOudmR9TMbXLNxSXGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=DGVfqA9P-2l6Ft0TS6-hx9ZUs1MvB2KfAQuCuNF81DfssG-ycGa9J84tGHuxH0Qd1FjdVPUANdOYzP_eGipHjTyAh-2SpooYUkFzHwflvY9JAQiUzMP0Wkshqtw3pggX7IBXd_JhSkvtDKb9oS9aQ18GwTin5FwhImVXowCIMbiFdj3vJf_UaQRpTsxGhB0vC1k2CWEgpqbcvU-ucYmuYLXlEwUsP_-67BJs9BaKhZfgE3IBEgvBcKkdJQBD3MveW4zgjOlGMnPSdO_ztiZyvYLLRzblOqg7LPZ3-ZDv6yQAlYN8stKOCQZbTb1kHTtz7fxsuOudmR9TMbXLNxSXGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2YseL0kAXk99M1o8Q1fEwWA2Xc8nwLzVsnBqsveJoqjbcXdo1N_FtzepdsYiGfumcrho2R1WvLyVdx_fL9K0vC_ljznLnTV1ANDvMFao7TcUM3J04Hwo1uaaHPJcfXJP27RwY2VZK5ztRz38VmUNL2ICUgGTd-cqmvDkInBR-WqOn8gQnj9oJDprGRy80nRgLKNA-Ec8ROoU9_x62LTfHFLhFbQ0rL5s8Oo1DvbcRMyvw7YieRz2KOvJGiR7Ak8W4TxslQZW9v4QOHD3rkit6vozZwW__TTA2p5uQCV30WQJO-RjLnlJ9_CPrMlg9MHnKOJqPLByy2Njjayuq3NJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzjJAxlueh9m-oIY44YGDioqrRjhtco0Tfb8qSJKIiafryf_RbwLGVBvYx_M_CJ3CotMJSP_iCPXzjQzerrY7mJl82RfFn7J7sYnQlsXo8F5sj0hBy5vxHjcPFk9MPErGOwjQF6aD7vlAQ6dnc0SsFW5BKIcPU5MBI10pE95UVoalZm2SVPYl3uUzBGwXZX5H6GCx0iCE22L0o6je-vRQzIQM8VsLXserz8sBQ-G4Z55mDEjCYj4Y4TECrDqymqcw-eTfKfVLfGBv6QJ2SbsLjlrVLUHIKEZlG8b-2GhxOQ3EkqXhtLfoBZtJ5Ek0dkGtVumW0cFTn9hhNd1KcG8GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=cY36qWDIkcS3UIl-PyA-j91I7H_HKAE8u_TOz3iQL1mUs0lhCdC1GQlL84QmKCMIr1rJvHPgayKtt4mB9nkhSmK6vOF-UBXWPscxLus9uiwV2EGejicoSZrauEuQr_k8LXYKa4fG4u-GElw7kwaL77eyoy_AV0boJ3GDt9jQWTNg6FpnXNdpLkSrJBvWjnOMENjoUDte_rPm84L27aLtW-I6IOt-5VTPKywgPn6qXDjvQBN1BasmQ_pG1Wz3HLVOSN3b_yq2QVe41nHP-y-JHrvrdMU0XfntanvqcfOvstm0QnortDpHekDb-TfjHq7p-_d6YwJMGxWRTTgFLo1qTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=cY36qWDIkcS3UIl-PyA-j91I7H_HKAE8u_TOz3iQL1mUs0lhCdC1GQlL84QmKCMIr1rJvHPgayKtt4mB9nkhSmK6vOF-UBXWPscxLus9uiwV2EGejicoSZrauEuQr_k8LXYKa4fG4u-GElw7kwaL77eyoy_AV0boJ3GDt9jQWTNg6FpnXNdpLkSrJBvWjnOMENjoUDte_rPm84L27aLtW-I6IOt-5VTPKywgPn6qXDjvQBN1BasmQ_pG1Wz3HLVOSN3b_yq2QVe41nHP-y-JHrvrdMU0XfntanvqcfOvstm0QnortDpHekDb-TfjHq7p-_d6YwJMGxWRTTgFLo1qTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=VvhekB5CYjsJHaIzsInK7WoTiGtIRTnNlNoH3f9L-A2WTAzlq8bblpodTd2iq4tb_UZssGoaH0WxYNYcVY29uBQKIz3wvlfmVBRc1RIepXBagrq_xsFOjRn-bmokZdmkX9-ZuWTpGcL-46bODnvWJI4BNz2jT6vY8bbzMOzUT6r8msaqc-bL62ahcX-Aswf6Y9hEB55IjOpECXDmAB4_5opSTll0RDmCY5nzmaRPxtJ0ljamw-SW8M4hBz2LzfKrfi9sCTxaW31xp-ciRW_bk91U1z6-lr8f3vftT5LNGRJZeUE7DstS8NfF2yUlnVotw4ZoaAWNpy0JwTscNQuakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=VvhekB5CYjsJHaIzsInK7WoTiGtIRTnNlNoH3f9L-A2WTAzlq8bblpodTd2iq4tb_UZssGoaH0WxYNYcVY29uBQKIz3wvlfmVBRc1RIepXBagrq_xsFOjRn-bmokZdmkX9-ZuWTpGcL-46bODnvWJI4BNz2jT6vY8bbzMOzUT6r8msaqc-bL62ahcX-Aswf6Y9hEB55IjOpECXDmAB4_5opSTll0RDmCY5nzmaRPxtJ0ljamw-SW8M4hBz2LzfKrfi9sCTxaW31xp-ciRW_bk91U1z6-lr8f3vftT5LNGRJZeUE7DstS8NfF2yUlnVotw4ZoaAWNpy0JwTscNQuakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=FUzlLnKc86Yn730gVui_s_g3clg_jiW_35ML7UH7nqvgYDQ--ta-uKIFUvHV1dB8UJplGrak82iOEpCFZRsLib7mvLm6IBI6gy6b_s6eX0M39EawizpUZPKEYiXpBwfroie9tIbkdBayqKuGHkrZbHbJeiL0OzzsE-i2ELiotAwrganey2qokIyvbPE3CRM5Zrat55kqAvEqSt0Xh3jyHrkdrc_UJa9XNNubMyMBNirVKkjBQFJBeKTpf3Oi2WQxqoNLA1Sa5SLyjfWWEhxZ2oMdGrWYumJ4T5NZNX50sxl3cMQdOj1OgS6r7MeP6o6LAKTqPNKuMaL6YdoYVdomtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=FUzlLnKc86Yn730gVui_s_g3clg_jiW_35ML7UH7nqvgYDQ--ta-uKIFUvHV1dB8UJplGrak82iOEpCFZRsLib7mvLm6IBI6gy6b_s6eX0M39EawizpUZPKEYiXpBwfroie9tIbkdBayqKuGHkrZbHbJeiL0OzzsE-i2ELiotAwrganey2qokIyvbPE3CRM5Zrat55kqAvEqSt0Xh3jyHrkdrc_UJa9XNNubMyMBNirVKkjBQFJBeKTpf3Oi2WQxqoNLA1Sa5SLyjfWWEhxZ2oMdGrWYumJ4T5NZNX50sxl3cMQdOj1OgS6r7MeP6o6LAKTqPNKuMaL6YdoYVdomtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djTvA5MEvOW-qWoGwfTs9MZHjV4Fch2b9wnA1X3kRPUaxUvLkBiFqF-95hUpBrqsWPg_LO4onSbZ7RWi6xNLHvMNPJBE3ia63DzWYn7-xR-dxTolLRysrLFbaHmrv8b4d_4POlqtbLDURexDrxTa-HNMuwWh3zbnqJ5LIpjGFDZsMsvdWTCSL3Wfjm7xCnRzdh3FGpB2s4xpDRN5ZJydpHDYqABAyQTMCetWHhKhZ-VYpgqq9TRQGHqPkVs3RO2jAGZGt9CpRdMUGjEMwKUclL3FLX3egzo566mlQSgPJ1VJOcTkEmkJWXQPQY3ZxPYRGIX3PWCK9P1KV1FuiSE04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hensaTYEqShBYACGNK9bo5CVRgCUIwQBY5dOcwoMvh3WIQat91XJh9xH_-POnkM95R-CyuJMs8sdQDFQLRt54dHvSbkxmgQb9K9Rzwl8kvOlMc3UR3o0SBc1reGTSHd9Hh4v0uitpwm0fk6KDrhZe-weS86vV24zhusbU23OJq-Ab8CbqXwq-Jf7LIcQf80Y2MY06gZ4pP3E_VEcczcry40QH8nohVYigQ-1hCOyZiBeDT3WpN2VKaXZ23BFLcZ2gSLxpdAbt1S6ChRv_2wAvNfYj0EzMYeuWCyrYp0_FG_QGnesy7uiWTuwjFuyiPkCr4DdGJSkqcu5OJkLgXRCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbDx5bgKnUZ3ub3MqzE7Py9q2pRAKpkJu5usPjHdqz8jrcsylTfB_zMvuOnZ6pxeuExtz9ZyZ9CdNluW8Z4YeCZ_MlUXYXKET7vs_M-JJ_MGV8YHQXZ2TN2XjUKSpxdjbi_dVkPLbu7bB-LMlv5yHsGVZSCsNAzdHHlXnbrNRVIwH5tzCtdwwUs9pxcBIQKZvWGvuTGa0jtOp4oQJsM118cOlPI_UtKYwuf_6r81GCwzzi5L_1qSM7xgvSISERiOdoMwPgva4VnoD2zHutw-1f1THtNuc4Q7kuklh8Hn8bfih2sF_QNc9FgpQX6HbaAiCYvtrR_uWxlPRmK_PguG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=KJSkWwcJX-dLigCvCeCSsnKMtOrjPlNp-aN_jJrh8hFffBtF5D4mHYugxcoPmS8k6q2HAzLKrX28rYNPGum4u2swq9C2nhSKW1UqEzDyyBGFpV1I5HyxCStevlqaedaCUwuYEyRQK8Uh1aUQGj3OQ1pKldNDdlHQLA_xn-Ws5DWQ5bFnhK42fn_za2_h45VVz95V9Pzf1m37xbDNo3oI6zfR-hyx9nFj5y6Uth6_7DTRg2vaUjN2_HDHND89xoyUlUtjajDJKrABRZGd1SC1Wt0sEHJdssXqLaPzpSdhiHl-oRmAkURNUIoOEEEAemEApuZKbOHnRkddyUUFQ9kqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=KJSkWwcJX-dLigCvCeCSsnKMtOrjPlNp-aN_jJrh8hFffBtF5D4mHYugxcoPmS8k6q2HAzLKrX28rYNPGum4u2swq9C2nhSKW1UqEzDyyBGFpV1I5HyxCStevlqaedaCUwuYEyRQK8Uh1aUQGj3OQ1pKldNDdlHQLA_xn-Ws5DWQ5bFnhK42fn_za2_h45VVz95V9Pzf1m37xbDNo3oI6zfR-hyx9nFj5y6Uth6_7DTRg2vaUjN2_HDHND89xoyUlUtjajDJKrABRZGd1SC1Wt0sEHJdssXqLaPzpSdhiHl-oRmAkURNUIoOEEEAemEApuZKbOHnRkddyUUFQ9kqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPpaHh-lGkKx_zEWCUxr_Ieyl5hdSICpZbmw0Ok5VGSClkGo5FZVfnV5wOWLot09gkn1cX2jkN2lgZcW7w59nx89DyYawunnrTvhx17mw1mHNQQRmj134Ngg2itG_TI6vqMfM6fwrz6PWFWWfn2tWyDv8NY2KDtATuPvqrwqTg-6ARccp32U7-XXcaWnkj-KhRI-06i1P7HA4_Tgz0Ec_FdoSkdnscOIUSOiiDBokSA-3Ogh0ueIy3pIP3zFeESKvZgwVzO8Gc9pYXcLZJylzUxCWkyCT3QZgvXR7Z0hlVW2R3dYmAEnPjC6kqDMTeIo2oJupQ0V0flzjuzSle-ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU27KpZqhBXcA3sYj5wOJR7M2d39C5vA-lQfPmUc3zOiTuOC9huC9uLx5Pujnb68aTMiuyCDkMBbWbgigtm6j9KQ0S592UiY8gkf1M_3V8JQLGn21to4rSfTNneUovGz_8vs4D7hJgEFevAikO4aDDCVp0pBqSoX_g9YecqxRXhZOmeah4nYvpP1bQKbtyUax2jLRDdW9KapSTMGYS15PUhyGZjZUF_q4fiYUTIw1yHKwWzGUCeQWGCYfiEtWP60HbDDzLnVemxGjnTnN62PfQBkxQ_NT7sFhY9KBJdC9uEpG4uloCTlpMnIe7Azo2hJ71wWhKjhZiHG95PzkAcMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWt1__7W_WkU62DTYn28DTMFhp6qCrU4_HG_aS4YpI87FriX7_VQq3UAF4OtjsngdbuRcIYusvsSViPuQ-wPSjC43KBCbel2pqyyzUFpp61lruQ2MX1vlfikpONkvvF2K4rVI10ApXnXwcdZgrrUlthNCZCxD9sAW6WP790uDXcErUi-Djco6hDlywkMeuRk2WltyBqSawdc-sVGlDrerl2FHrVRyXqQ6JqBv21Q5p_PgnWBYGJsmxrZHj0Cbdj0mBauusxJxVULVIRTUoqD_Azh_I202Wrd4GkLhy-15dsVRbrJa1vo-NKHgmKW0WnvfnhiXQ7IfvNxuyxzRqisSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=HGAUK3LKt60jgRqwW199bt0bN4n8GiGqAX0XBCbn1rzpSY-XhZRfHhXyzGhwScgJYcuaz9vVvbd3KPjONMtsx2yUvKENaFq9WunoVih7JkpmtLFGMk9zhCg5R_plIWKXL2sPTqxxNiqbwTdaXr_xsp5LMRarf1T4Yu60peTR6uxebTUsGPygn7qJOm0vfKIC-2fnh5kJvX27TA3OyYnLey4E2u0WlkY3Hw_S2xsd_nGs8R5J4iRLk67jq6FRaeYFW93lkpkdaEEDx-pEQCTNyXhmHBuIbt030MiMdJpKn12OUnRe9b_R-4kzZdJo-iSH1Z9AG4Z4-SXpj8T9N9z1PIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=HGAUK3LKt60jgRqwW199bt0bN4n8GiGqAX0XBCbn1rzpSY-XhZRfHhXyzGhwScgJYcuaz9vVvbd3KPjONMtsx2yUvKENaFq9WunoVih7JkpmtLFGMk9zhCg5R_plIWKXL2sPTqxxNiqbwTdaXr_xsp5LMRarf1T4Yu60peTR6uxebTUsGPygn7qJOm0vfKIC-2fnh5kJvX27TA3OyYnLey4E2u0WlkY3Hw_S2xsd_nGs8R5J4iRLk67jq6FRaeYFW93lkpkdaEEDx-pEQCTNyXhmHBuIbt030MiMdJpKn12OUnRe9b_R-4kzZdJo-iSH1Z9AG4Z4-SXpj8T9N9z1PIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=A85KxOo6R-xC4QJZJxkWQgIMBtFpCy7Bhd9VdBLlaERcBcDCzUpwIdO05_K20LxJmR42Po9juNKMkS4A6EYf5wu_AbnhLLXCq7wUgiPopi4rfnINl6QMQtRJvu3Xocimiq-NJhnBxOKVgBMP4x74aUM37r0C9bA8Za1gjOFVU9sOXg9U8kxwZE2t14UzhhaPkJudzTnXrKzdl-FBx4IlOgKhBUA8XAoZnPBKeqE2Jl4oKpUwGFrEj4-Xoff-BiIbRcQw9NuvwQlDw0hClT9CvgPJbgcC11w3vUOJpk8CqdN-Lbp04AePM_4km-hnyGuyN5fXUjblgiovO67htug8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=A85KxOo6R-xC4QJZJxkWQgIMBtFpCy7Bhd9VdBLlaERcBcDCzUpwIdO05_K20LxJmR42Po9juNKMkS4A6EYf5wu_AbnhLLXCq7wUgiPopi4rfnINl6QMQtRJvu3Xocimiq-NJhnBxOKVgBMP4x74aUM37r0C9bA8Za1gjOFVU9sOXg9U8kxwZE2t14UzhhaPkJudzTnXrKzdl-FBx4IlOgKhBUA8XAoZnPBKeqE2Jl4oKpUwGFrEj4-Xoff-BiIbRcQw9NuvwQlDw0hClT9CvgPJbgcC11w3vUOJpk8CqdN-Lbp04AePM_4km-hnyGuyN5fXUjblgiovO67htug8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=ooCAVwne7Qd5Km6TmeSO7BF8cD0Kp3f_hNAvFmAXSi4pou-xPHkPK7k2sj2HzhX3iiXdNlsfRgvLWAyDc0-qPlDbz5Wy_9WIkzKhrvargjLjJWO2htjV4sjKn8LdMm6SSBeyOidEFjAvRdaNzLn4v4lhBF-_SHms966rV5SyijpQhDG4cvusqy3Dv2jszbUjvMNz_t_8HSS6evcUUPyOayKWe7un8_ESTQTNqeH27VgBlTLXfeAi3PEzDUHXZJ-RbHMRAvtjMz98W3ibcCKbG_Q2g2GyBJbDvIg0K1rrpFicFtWu1WsL4-8bKchr4rDBIXYy5AGkF8TyRXWX1ak24Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=ooCAVwne7Qd5Km6TmeSO7BF8cD0Kp3f_hNAvFmAXSi4pou-xPHkPK7k2sj2HzhX3iiXdNlsfRgvLWAyDc0-qPlDbz5Wy_9WIkzKhrvargjLjJWO2htjV4sjKn8LdMm6SSBeyOidEFjAvRdaNzLn4v4lhBF-_SHms966rV5SyijpQhDG4cvusqy3Dv2jszbUjvMNz_t_8HSS6evcUUPyOayKWe7un8_ESTQTNqeH27VgBlTLXfeAi3PEzDUHXZJ-RbHMRAvtjMz98W3ibcCKbG_Q2g2GyBJbDvIg0K1rrpFicFtWu1WsL4-8bKchr4rDBIXYy5AGkF8TyRXWX1ak24Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAqV7O73hxiwA6uETAiAHSEdTZ74FNtKjaJIWVYNbh-H-fWc7yAKbT1m2WnTS4IRw83F4h-GVbYnnkzSm_u7z_qzrpuOwQlKqGFsbtCnuokSVWA2c4IysNyRPE91VXKMxZvdIywd4gpfgofQYp7dnWlRgmxb15NJ_croS2TwpOabKgr6ouXLWtbWiu66cLsfYVAvqmq6Mxdte-Me3IyDwpqryGXWQ4KaWYSFK8aGIYbSxch4KxHQ8CETrxeKfAjKnOgde6Mn5pS0Nif4i4TRb8pJ03Ou2HhlSUGxxOAjmaUR0ZXzGjKGGjdSN6GxFkvmpRK3p_bwJix4XIbGpun86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=sXyiLkwBqBmvsW6rJgjkC0gKLcz4k1TDprXoUEyTeh3O5TubNyU-11kmjoy4ITvTsLMwoBDlrfSRAZCezADYYSqjuYGrgRgAePdQJpfUvX8J8CXEHau2aMtrNKoWB4jIJAULfpRcpRhoJv9w4By50BBd_KEO3yTkwAa3AtLl9kMcdSC8AtPkUOoZOLiQvPNv9q2_ygwzbRyAZvRWs0s6SiupXsxi7fJG3TpTIvk4sEw25lAVfsFsD9-BkgyMBCtF7oDQu6hhKoOkM589VgnIeu7_Ty9nJIvdLbZ6pW8waqtB93gMbv_dXP40o3OmaWFwtQ-hDVofWB_pv5LWXQBy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=sXyiLkwBqBmvsW6rJgjkC0gKLcz4k1TDprXoUEyTeh3O5TubNyU-11kmjoy4ITvTsLMwoBDlrfSRAZCezADYYSqjuYGrgRgAePdQJpfUvX8J8CXEHau2aMtrNKoWB4jIJAULfpRcpRhoJv9w4By50BBd_KEO3yTkwAa3AtLl9kMcdSC8AtPkUOoZOLiQvPNv9q2_ygwzbRyAZvRWs0s6SiupXsxi7fJG3TpTIvk4sEw25lAVfsFsD9-BkgyMBCtF7oDQu6hhKoOkM589VgnIeu7_Ty9nJIvdLbZ6pW8waqtB93gMbv_dXP40o3OmaWFwtQ-hDVofWB_pv5LWXQBy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=eT6yE4cJ5VlK7nZ2EykSbgum-cplWZzQ_74IrD52rNAxVp2EYfOy9X-GcLh83k1rz0Eiktg7OAQ7PixXBL_SbjM7F0MfZnM_qZ1xqK_LluFDDhlMXnV6N0tlZrI2qwJh91KBG5y2JIHCJz7VxW8THI5zVTkts5NjYkHvYIMpbQ8Re5Fe5iNg4AKVpctKiFptxreOuv4VpzZUT5k-zPZx9FC2-qYEUT52cHNkckz7SPIUJE48Fo7i2Da4YRdAIXdazH2jXa-skbSxGAcm4wpp_VUGN2ykvhzX-fsu3ctPtoA-0FfM3jPxq4cYhULeHBPHkALjgVGda2e5FBJn7kvkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=eT6yE4cJ5VlK7nZ2EykSbgum-cplWZzQ_74IrD52rNAxVp2EYfOy9X-GcLh83k1rz0Eiktg7OAQ7PixXBL_SbjM7F0MfZnM_qZ1xqK_LluFDDhlMXnV6N0tlZrI2qwJh91KBG5y2JIHCJz7VxW8THI5zVTkts5NjYkHvYIMpbQ8Re5Fe5iNg4AKVpctKiFptxreOuv4VpzZUT5k-zPZx9FC2-qYEUT52cHNkckz7SPIUJE48Fo7i2Da4YRdAIXdazH2jXa-skbSxGAcm4wpp_VUGN2ykvhzX-fsu3ctPtoA-0FfM3jPxq4cYhULeHBPHkALjgVGda2e5FBJn7kvkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=D2stdFqt5EY9jjv2pdf6YSpCG5cQntnKkz894o1Q3A6wGyzRf1zsOVxDwvkGAAxo8mrpDxmJLOnE94Qe2-TQkdS-iq30IBAKsWWTQZk3JKbhH7p_YKzLTCR49gQaWSLFQfYcpFGRzx6t3KiMAr1NbzMuwGfftpCHBd26wv8GBD2wqc84jm_xwVmhmMkxYFZx6AJLnpMeq02EugVBT4bAV3KwX1tml79AQzPv6oYktGvbu6V4sgwEgslxacs1WQGj0FV6yOHnb9tm_B-RewIR4cYz-Qd7TkDiSXihmZk0jFdvoMd_w9yFNSPVDfmeshIazHDc779JsXTjT3mw5URJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=D2stdFqt5EY9jjv2pdf6YSpCG5cQntnKkz894o1Q3A6wGyzRf1zsOVxDwvkGAAxo8mrpDxmJLOnE94Qe2-TQkdS-iq30IBAKsWWTQZk3JKbhH7p_YKzLTCR49gQaWSLFQfYcpFGRzx6t3KiMAr1NbzMuwGfftpCHBd26wv8GBD2wqc84jm_xwVmhmMkxYFZx6AJLnpMeq02EugVBT4bAV3KwX1tml79AQzPv6oYktGvbu6V4sgwEgslxacs1WQGj0FV6yOHnb9tm_B-RewIR4cYz-Qd7TkDiSXihmZk0jFdvoMd_w9yFNSPVDfmeshIazHDc779JsXTjT3mw5URJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RhTIA-A14TnlaCzcRSmSXrxY52Zfut7uVz7Q3cjDheU_G6x7EpOp2H23wk0bvyvtRiipmHnOp__NFd_HVBTjue7nkZRxc5Rvco1TPEp5Avgk1Mia9JcdQnsp6TGrPPXU0zOKRqyR3vfnB7TcWgp8ykv17NTkl5XFqfZYLkRDy6pYhpvvEca-zBLxeUtQz1oxgRI6sPlgy3QhXIyxM8Fw1M4wBHDqGF7-pQFLfBzF0tBdoolinPESbTRoM6nZY8gXIDaloNC_dVWoKxiVqxZwdt35VY2PkgoHe0zkUvJGjnlgTZ7TOOhdRf2VMoCb1SBumwys-swvPWHYA11iG9MA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RhTIA-A14TnlaCzcRSmSXrxY52Zfut7uVz7Q3cjDheU_G6x7EpOp2H23wk0bvyvtRiipmHnOp__NFd_HVBTjue7nkZRxc5Rvco1TPEp5Avgk1Mia9JcdQnsp6TGrPPXU0zOKRqyR3vfnB7TcWgp8ykv17NTkl5XFqfZYLkRDy6pYhpvvEca-zBLxeUtQz1oxgRI6sPlgy3QhXIyxM8Fw1M4wBHDqGF7-pQFLfBzF0tBdoolinPESbTRoM6nZY8gXIDaloNC_dVWoKxiVqxZwdt35VY2PkgoHe0zkUvJGjnlgTZ7TOOhdRf2VMoCb1SBumwys-swvPWHYA11iG9MA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=lYL7NmekmMv3egqBvxMNmjNkXQueyHGnk-YhVMgCneT7DDeVWiC6CELP5BavZXXMepOWEwKlOGvkjyc8R_-yfnn_kXHTcWjZs942cP3B-DcU6h8-LPkTTOPS0CkrFhQMsMuAnEbHuuWaVETo9n6qPsTAdoudUWcmfafj4zllfYpBb7cUlQ0u-dOl0cNfy5Hq84lfb0dpLQd3iWJY_IsTdw2Cy9M42VQIm8LWjhuNip7YSIy73f5CD3fNWxHEw8MLF9So61ipXG9wiwP71EMEOeHCQ3MAGexloFOY82w5yTSnQCD6cNlU_3hwI7AxZW4QypnGOhMEjUW4hfRAr3__dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=lYL7NmekmMv3egqBvxMNmjNkXQueyHGnk-YhVMgCneT7DDeVWiC6CELP5BavZXXMepOWEwKlOGvkjyc8R_-yfnn_kXHTcWjZs942cP3B-DcU6h8-LPkTTOPS0CkrFhQMsMuAnEbHuuWaVETo9n6qPsTAdoudUWcmfafj4zllfYpBb7cUlQ0u-dOl0cNfy5Hq84lfb0dpLQd3iWJY_IsTdw2Cy9M42VQIm8LWjhuNip7YSIy73f5CD3fNWxHEw8MLF9So61ipXG9wiwP71EMEOeHCQ3MAGexloFOY82w5yTSnQCD6cNlU_3hwI7AxZW4QypnGOhMEjUW4hfRAr3__dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=W7XMBJaLaTZJEKZKAYD6LZNPNVYBbbZT80-19KM6_ZHN-Gsh6z7Ij7brd5JORFFr_vr8WNuZ3kvmgxs9T-yNeRjOXHavyxi0qPSTncsNCAHiiYNqIThNUyInAkPcStQSzXk7SVTbKg5Rl6G5lFa3xdKsQVxOxaR6Ru-ZqbJLDdgZz2kjryi7ECwdCKGgB6ke8DjDM_p4yFPLkl5BfwLYftvh5FNYGsOk5ho40ItbfjqdYXjqxTIBb_HQhrirUcQPo3m99kf-UV_qsBV7wvDX8EEaQFctR4EUX9vu_BN6D1eXwgI8XqSgAH3fpSIvR35_pE43qwtpeVQuXBX9jUuLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=W7XMBJaLaTZJEKZKAYD6LZNPNVYBbbZT80-19KM6_ZHN-Gsh6z7Ij7brd5JORFFr_vr8WNuZ3kvmgxs9T-yNeRjOXHavyxi0qPSTncsNCAHiiYNqIThNUyInAkPcStQSzXk7SVTbKg5Rl6G5lFa3xdKsQVxOxaR6Ru-ZqbJLDdgZz2kjryi7ECwdCKGgB6ke8DjDM_p4yFPLkl5BfwLYftvh5FNYGsOk5ho40ItbfjqdYXjqxTIBb_HQhrirUcQPo3m99kf-UV_qsBV7wvDX8EEaQFctR4EUX9vu_BN6D1eXwgI8XqSgAH3fpSIvR35_pE43qwtpeVQuXBX9jUuLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=u_SEuAqj2bv_p1PnKNGtfhfTQEkViy0Qdzf-rX_HaMNEwdpfsH58c6bCkijab7ZNn8wFRLsu3-iIcx3Ji7S_R7PLyDkSpuJ4EfDN3qs1qF-QgmCQFiRmhK8mkzBawHyDfqpMqB-4tVMDZMtrI6keXGdz-yrJhAnNbL8p7WUyANBCpwXAKAJb9Qx9_vIh9OCCWoSjBjrxQdXFpsdIZESKaimJCbV0xT8maSgdmwltaNT3gEtLWxHpGuugIjBWjR21YNe4JoO1MoOVzmbnh1jP-yLcvhqQQ1cBA0ckd9CQz1IUo9MZAgTYsYbVjvb8jPEGNdfmtfkDD7uAWLLAG2lBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=u_SEuAqj2bv_p1PnKNGtfhfTQEkViy0Qdzf-rX_HaMNEwdpfsH58c6bCkijab7ZNn8wFRLsu3-iIcx3Ji7S_R7PLyDkSpuJ4EfDN3qs1qF-QgmCQFiRmhK8mkzBawHyDfqpMqB-4tVMDZMtrI6keXGdz-yrJhAnNbL8p7WUyANBCpwXAKAJb9Qx9_vIh9OCCWoSjBjrxQdXFpsdIZESKaimJCbV0xT8maSgdmwltaNT3gEtLWxHpGuugIjBWjR21YNe4JoO1MoOVzmbnh1jP-yLcvhqQQ1cBA0ckd9CQz1IUo9MZAgTYsYbVjvb8jPEGNdfmtfkDD7uAWLLAG2lBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=fxVr0Hbvj-8kV7NBzmnnNc3TnFi0-bM91kVbMf6UX3GfxSMg53zRTV9OBW4EUcSOSq_QQ4UBXuPeYUzY9Uip8kDiJaT6glMCSREcg8PGTQfWFSeyDqEQYD_Vb5iWsoeS9RI-UHwrW9uj5KVKQJmtI4b92VT_yky4KkYPjRzZxHes7uQ_bLZj8jBsuDAPRJwmlh7WB9JPI-u_NYYksOpZiAYRIZoI3mdcnoRVF58DMWDybqqFd94OFTh8flDSfA78Zg-vBwn_7Koa-543kmSb_dY2syiRmH4lknQTQiTwUGCGIYv_wMnM3ZUG4ICcCYmr_dr6D2sbYXWz52wmVFBRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=fxVr0Hbvj-8kV7NBzmnnNc3TnFi0-bM91kVbMf6UX3GfxSMg53zRTV9OBW4EUcSOSq_QQ4UBXuPeYUzY9Uip8kDiJaT6glMCSREcg8PGTQfWFSeyDqEQYD_Vb5iWsoeS9RI-UHwrW9uj5KVKQJmtI4b92VT_yky4KkYPjRzZxHes7uQ_bLZj8jBsuDAPRJwmlh7WB9JPI-u_NYYksOpZiAYRIZoI3mdcnoRVF58DMWDybqqFd94OFTh8flDSfA78Zg-vBwn_7Koa-543kmSb_dY2syiRmH4lknQTQiTwUGCGIYv_wMnM3ZUG4ICcCYmr_dr6D2sbYXWz52wmVFBRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqdaeb1_MW9lYrk1GsrbmNznUOJSGlSMqGL1Skmwa8p7uFPfl_haG3pcC-a_wd6IE4L3TVPC5NItADk8OYgFQkPs_NaIoM1bPsnT-njziQYBq1TWgDBV73ZOCEKg2kEuuYZFiVEXrdMETmbKY02WkjQ1FWES40nx9spfOUmXkTII3of8EnWrHOsSoCaW120eeD4BRZT1MJ5rgVat4qXE03iQbAutxT-lHraEsFQUWsWS_rKCclx4HWrE9CQ0q94qs_i0PZZYt8iJPutygGIN96tfESZ-cTjYrGGC1hJrph1Zxje9Zz7h-oeK02Pas_zC63DP7Vp9RNwiHuSeBqzqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=aREqeagqCg2y8lRZsNSLFtOOOFiQMJWNJffro1s28fTG4hZUZlC47wWV4jlXFp-gX5SRUBpl6VWEvbWZf4RVbEPmI47fCX2Ra_Gs83btr_RSYtAm0M4i8fVHP9cegzSwGjGd4oa-nWcjYYhU6NrYEmieeRWzLTuxjgfo_Vls6nX3cneBGvarroFwlu3iO8kxhI5blVWjgFSgGXUlBKdUmXRDIKz8PpTsVjEZnrIFoBVgFfs24E58xy8kp_mkEr-JyS7XKyuUcEF6H6FhOYlUOuuxHcQZEfCb0FWvZ3k0QZw90uyaaUjiW12yWp5LVOd03JRgvDycpEuXcEWo__500Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=aREqeagqCg2y8lRZsNSLFtOOOFiQMJWNJffro1s28fTG4hZUZlC47wWV4jlXFp-gX5SRUBpl6VWEvbWZf4RVbEPmI47fCX2Ra_Gs83btr_RSYtAm0M4i8fVHP9cegzSwGjGd4oa-nWcjYYhU6NrYEmieeRWzLTuxjgfo_Vls6nX3cneBGvarroFwlu3iO8kxhI5blVWjgFSgGXUlBKdUmXRDIKz8PpTsVjEZnrIFoBVgFfs24E58xy8kp_mkEr-JyS7XKyuUcEF6H6FhOYlUOuuxHcQZEfCb0FWvZ3k0QZw90uyaaUjiW12yWp5LVOd03JRgvDycpEuXcEWo__500Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=uzDQmsYqcoSXzE-jqGoYEEuF_RMoIgxQked9VDCvOSsV-6fteA3UYX17VZuoir__gGz09BbeXS5YqIAQK9Dv1HM_q5U0qpMKFZ7QQv8a8sR2MJgH1dpkLpbLqpmQrHX0sr3n5XkJIcZ6TsujZjoj4Y96PUnqZrBZ8fZshodgEyxxotPlgMudwH0aozPlBdhmc4Gp7GcKjQskFXXCPCSmKVIQPoZGg-Jn4qTbP-txk2D0j0KelnRy1XVjKS6U8_AvSeXfCpzoIaFghIOdJqsGlq_YtuvgvRQJxInnjwGtk2vQAPgOjUIXXMCV0u6HHRskGZw0JNejVn5YQvY8VNbqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=uzDQmsYqcoSXzE-jqGoYEEuF_RMoIgxQked9VDCvOSsV-6fteA3UYX17VZuoir__gGz09BbeXS5YqIAQK9Dv1HM_q5U0qpMKFZ7QQv8a8sR2MJgH1dpkLpbLqpmQrHX0sr3n5XkJIcZ6TsujZjoj4Y96PUnqZrBZ8fZshodgEyxxotPlgMudwH0aozPlBdhmc4Gp7GcKjQskFXXCPCSmKVIQPoZGg-Jn4qTbP-txk2D0j0KelnRy1XVjKS6U8_AvSeXfCpzoIaFghIOdJqsGlq_YtuvgvRQJxInnjwGtk2vQAPgOjUIXXMCV0u6HHRskGZw0JNejVn5YQvY8VNbqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=rzySHiLVFOzhBOVotvagucwYDyJJEF_fVyYDLM9DFW-pxGoUapf69JOWF4vqRXLOVYksp9HZWimOyB7zdqBrcbi1v4Y31iUOIuR642a3qxG2r5tDtAWhJSudqBMBPPKUEW-Zh3RCLTJnrjjMkmXy-Tm0FOo19anqfLnYvEMYLUYkTa7aSJ4v7tBYGg9pQTJWo__ncpa2QSxgGDc7DwC5LFf8DRr9G5hdiN-0uyE24l0WdFeFTEf0XWatI8UNulzMw3YXmZVySIh4XiTHQi2MmBx47aQL3e15wfgE2KgIqLatPdX6zEYuj0zTvkAN7UzHy6EPIhWTO4-ZGS2skcClOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=rzySHiLVFOzhBOVotvagucwYDyJJEF_fVyYDLM9DFW-pxGoUapf69JOWF4vqRXLOVYksp9HZWimOyB7zdqBrcbi1v4Y31iUOIuR642a3qxG2r5tDtAWhJSudqBMBPPKUEW-Zh3RCLTJnrjjMkmXy-Tm0FOo19anqfLnYvEMYLUYkTa7aSJ4v7tBYGg9pQTJWo__ncpa2QSxgGDc7DwC5LFf8DRr9G5hdiN-0uyE24l0WdFeFTEf0XWatI8UNulzMw3YXmZVySIh4XiTHQi2MmBx47aQL3e15wfgE2KgIqLatPdX6zEYuj0zTvkAN7UzHy6EPIhWTO4-ZGS2skcClOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=NbvBgr-RfoDm_sGBxYTCCmzkJ-AY9YDP936lxTopI-6UuRJmW6Pn48qRogrpys_wDtkS2YKuVt-cWkKwKBEvKJAr-wrrxCmNepU5Lm_4WwM28z_NgCb5Nn-p8HcNf8Rb3KXH_MQZKeFawu9XUIfEISV-x-4odKvmu2bx0oEs0Dzddp4sfvKzC2VihehlNeBdKoIUb7AAXbPqXIqs3hQApjJvJwWxSdstlBzf8vJ-8HFraaInK5QBpX7oStAJW2hsCVxgMmQwzvvJ-ta_gDZOEykhieQvsfrEPt_u_tv585ffp9l-JP0bavklKGJH0T4jmb6qdkkPlOADe2hGcVer0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=NbvBgr-RfoDm_sGBxYTCCmzkJ-AY9YDP936lxTopI-6UuRJmW6Pn48qRogrpys_wDtkS2YKuVt-cWkKwKBEvKJAr-wrrxCmNepU5Lm_4WwM28z_NgCb5Nn-p8HcNf8Rb3KXH_MQZKeFawu9XUIfEISV-x-4odKvmu2bx0oEs0Dzddp4sfvKzC2VihehlNeBdKoIUb7AAXbPqXIqs3hQApjJvJwWxSdstlBzf8vJ-8HFraaInK5QBpX7oStAJW2hsCVxgMmQwzvvJ-ta_gDZOEykhieQvsfrEPt_u_tv585ffp9l-JP0bavklKGJH0T4jmb6qdkkPlOADe2hGcVer0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=pOIXKKWd8-CqbEjTLm65jBzRCRDlblF8ZjQKc5-i_e2c8vInWpoK4UwNACrnWCmFvWo4wCxVguHl_v3i3IqC63X79vGoE3fak8vBUAGDiZrSV1vfcgmX8c4dR2Bn7beNnr5uNIn7cIDpcIvQtJ8nbPXAp7yIOy_ucRkcBOjV5vsiqbVkD5jPTMF5GvyrONjLJxrB6M8w8-MbHUZdljyPeuzqftM5JrWpf-bubv6xwc0eVGex1okJrvJvPIaqgc9_8IRgbNDJTNUZermpzg-rpmr2okNGYVYl0tOtS6KnQUHZJttmhR5W7WUp3rNaJHunlFq0-vpjeHr8T0L-4TvjnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=pOIXKKWd8-CqbEjTLm65jBzRCRDlblF8ZjQKc5-i_e2c8vInWpoK4UwNACrnWCmFvWo4wCxVguHl_v3i3IqC63X79vGoE3fak8vBUAGDiZrSV1vfcgmX8c4dR2Bn7beNnr5uNIn7cIDpcIvQtJ8nbPXAp7yIOy_ucRkcBOjV5vsiqbVkD5jPTMF5GvyrONjLJxrB6M8w8-MbHUZdljyPeuzqftM5JrWpf-bubv6xwc0eVGex1okJrvJvPIaqgc9_8IRgbNDJTNUZermpzg-rpmr2okNGYVYl0tOtS6KnQUHZJttmhR5W7WUp3rNaJHunlFq0-vpjeHr8T0L-4TvjnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=m5YqA6g14CrPObNJUXWwrnS9mU1CxfvTb_V9StTcVHO4RPnPCByCXsZI8_Wm1OkQaiTR29a8tA8jo8XlRI-XlQ36gz3MefOwG3X7HmiMdv6aO2HUTPqNhofOwbz4kxIcXUfJj29hAm1uba93Bu3OqmySQmvLkhkFvD6afWK3jSHZxiUZrShYg8G0stwcn13Mutsqk9E_MVNOS9hIu33JWMvuDyx7jnn6vD5Id6Ie0x0IrU3tWMvUjSW6P6qJeZpWsyjMJaMlcTKCv0leOfLaUXInRC00OlL8xDcJd-yJV71QY_XgXyxZ0AXcxP3axIQIvZNVIMHfsxiIU5r-vfmc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=m5YqA6g14CrPObNJUXWwrnS9mU1CxfvTb_V9StTcVHO4RPnPCByCXsZI8_Wm1OkQaiTR29a8tA8jo8XlRI-XlQ36gz3MefOwG3X7HmiMdv6aO2HUTPqNhofOwbz4kxIcXUfJj29hAm1uba93Bu3OqmySQmvLkhkFvD6afWK3jSHZxiUZrShYg8G0stwcn13Mutsqk9E_MVNOS9hIu33JWMvuDyx7jnn6vD5Id6Ie0x0IrU3tWMvUjSW6P6qJeZpWsyjMJaMlcTKCv0leOfLaUXInRC00OlL8xDcJd-yJV71QY_XgXyxZ0AXcxP3axIQIvZNVIMHfsxiIU5r-vfmc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=ntvQanvYgHLKRhi6O0wNMzVinstxknZC4lXNj-8Ezoyhr1Dy2sYU8bvXIO_-FBTLoDzu51Virm14IbGayQMqM5qv26R_vNEsiDDZRn3WGDwcqxxFxF9XnZMMLaleHcOGzOexZjCw03ZhCq4C-vpfB6UR8b8jCJF1MrcxoHZYXWr3EnNojqisLeTjrBtYNhm1paz6xJhayn22pdPQfvuWsRnvdNjRHZkM8mYB4qgoyn4-EEFm7KtnXlvThrk4zj_bPAcXwWmBJCJD6C-jit4NtZaDJ_-jVoFmXBcMygmrPcDvUFzzgUeitd-WzR7gGPXM-1C1pvinngYANzDYOr5kDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=ntvQanvYgHLKRhi6O0wNMzVinstxknZC4lXNj-8Ezoyhr1Dy2sYU8bvXIO_-FBTLoDzu51Virm14IbGayQMqM5qv26R_vNEsiDDZRn3WGDwcqxxFxF9XnZMMLaleHcOGzOexZjCw03ZhCq4C-vpfB6UR8b8jCJF1MrcxoHZYXWr3EnNojqisLeTjrBtYNhm1paz6xJhayn22pdPQfvuWsRnvdNjRHZkM8mYB4qgoyn4-EEFm7KtnXlvThrk4zj_bPAcXwWmBJCJD6C-jit4NtZaDJ_-jVoFmXBcMygmrPcDvUFzzgUeitd-WzR7gGPXM-1C1pvinngYANzDYOr5kDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=aIvxFHKNrR79LAyWGATcz9CFuEt8D89FTsmeqNWWGWWE4yQae4Xj87Vg33Olz4MWrNk4zq1oGiggZg6ib3GknVaBW3Czmu9FXtoP7HSTaxJLPsdEQyDKMc6t0CFiQNmHM4noujvWHuVxKNPVgqx0pyOeCTf_TElAsGy6mwuHY7vsVIt2IDB-XNayKT51Ruvzt0KFfU-ajoL3OH0WG1LXMMMWqF2yXSaRt67tM5RbXOfveiRtsGXJcG5TBtEJtRBuzBacCs9XvQ8H8LL7ijrmNApv7yyzAlgvJI2nOXFGMW4GiiiD94aZmw2dwfooNnptwGWfRR_bA8RrhOOZFQzPqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=aIvxFHKNrR79LAyWGATcz9CFuEt8D89FTsmeqNWWGWWE4yQae4Xj87Vg33Olz4MWrNk4zq1oGiggZg6ib3GknVaBW3Czmu9FXtoP7HSTaxJLPsdEQyDKMc6t0CFiQNmHM4noujvWHuVxKNPVgqx0pyOeCTf_TElAsGy6mwuHY7vsVIt2IDB-XNayKT51Ruvzt0KFfU-ajoL3OH0WG1LXMMMWqF2yXSaRt67tM5RbXOfveiRtsGXJcG5TBtEJtRBuzBacCs9XvQ8H8LL7ijrmNApv7yyzAlgvJI2nOXFGMW4GiiiD94aZmw2dwfooNnptwGWfRR_bA8RrhOOZFQzPqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=klLms4N-i6NXyhVT3T0oxPE26jMJBhL330MYH6uIinkzEeKYEc5N7_dJqhGGcIBGhQtMdHmlKs2FcuPv8HRIRb0KFAjtRxMimYxZFeSKjLtFYXyJpaTMKHvGcF7VYXW0iMk5yADvsfyORBfg9oQi3RVHENxdrFx7yVqLy0ws44w9doB76xyVQqOSrv2gGMJ-e6s0aVLIEabuv2l4nx0IVxQorXxh3U1zHT18o0m0U7MxB2vDA3UH0v8ysrwcW5QeD_bRyGpp4v-MocYri_DlfPD020ANoSlXvHICIg-6GpgDkJ7gbeEtUMJjSikoRhR2LAAMhfsyCTQoZS1VgUb6rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=klLms4N-i6NXyhVT3T0oxPE26jMJBhL330MYH6uIinkzEeKYEc5N7_dJqhGGcIBGhQtMdHmlKs2FcuPv8HRIRb0KFAjtRxMimYxZFeSKjLtFYXyJpaTMKHvGcF7VYXW0iMk5yADvsfyORBfg9oQi3RVHENxdrFx7yVqLy0ws44w9doB76xyVQqOSrv2gGMJ-e6s0aVLIEabuv2l4nx0IVxQorXxh3U1zHT18o0m0U7MxB2vDA3UH0v8ysrwcW5QeD_bRyGpp4v-MocYri_DlfPD020ANoSlXvHICIg-6GpgDkJ7gbeEtUMJjSikoRhR2LAAMhfsyCTQoZS1VgUb6rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIgqRNjwpvI53xTGI7brlyy_xzl1fq--HV7C8bMybWPUvMfNpIZqJ-vH7lPGiJDa4hHPrMNT81zHPePXHvx5RIxFdED3yqDYmQMm2YUO9ZZmkYmb-JHUkDpqtfKVg1sypmiHVPBzEAq4HjQ5Dbv2rwVfvoQA-aKoq5DQ6YXo6cbm_Owb7sDsTGuncycr42qsyUscspV89iLeTeBklYs4PGMsUc7KnLoNWR1Zh88J7t6xqh0KB-SB-btUTyWHChAFgmr-PAOMAoevHoBp9rPCadoF9T-cOuklCLiYLRQPmjmnXp5kaLYAd84zu_RQBDGV-84YNPHoPibHQOA2IbJrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=jxOPi6PRAcocluWwmvt-cXkuajdWE3Js2arvm32hFbzNr6y3zu-TL2ZBhivv2FhzbrVnth4E_hX7339ZV1xi7xKNsPleDyMEo-sd0phJ6IwwEeHXGxldPhR5J0AwrnNah2m1LK5yRMCF11VQmG_9wEDXUHDjPU_rgDL9JvYOaHQK8r7SpL0DdQlF7jk7ti4e944qnv-oWMzQKX4MjtJRTbi_VHLUEWOIzqsmKYLackjJqjSXs93_4xbJxS_GOzGQojLERWTJY3d6N_WxGjxWsYYq2U-j_UEfscxx2xSYxx9ACrgm1z-5gHXl1FjZ6t7RiD2gb1K3iWPwJmQiH_C9G2zfLCio7ih15HGaH8FJu8yTgWSm3QVhIj2f6KuNBHni1TM4eXlr7Dk-II8PQls8pHbUpLsxG9JhO4L2Rfx6FjBQx3FJqcgAF87EsO7WGqeqqdDr7JR6NUW_mOz3zQz2l4lpqYT1rInzF0gEO8skkzUCJTmGfiMMEKTQkLKmYzeSXD8PTA3mrjg61dsms_IODv0c4QEpfAnLKoZQ4j-dgJmpOtIzWa20uAFahre9rs1BB3XyuPg6z2tWqtclba2hus13P_lebQkqQLilYqSCBhc8czHdtFRyVD6f48FNUH8ZDtdEybw_a0EieD6XLlNbhDvHDtaEoIIn9pELMNNbz60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=jxOPi6PRAcocluWwmvt-cXkuajdWE3Js2arvm32hFbzNr6y3zu-TL2ZBhivv2FhzbrVnth4E_hX7339ZV1xi7xKNsPleDyMEo-sd0phJ6IwwEeHXGxldPhR5J0AwrnNah2m1LK5yRMCF11VQmG_9wEDXUHDjPU_rgDL9JvYOaHQK8r7SpL0DdQlF7jk7ti4e944qnv-oWMzQKX4MjtJRTbi_VHLUEWOIzqsmKYLackjJqjSXs93_4xbJxS_GOzGQojLERWTJY3d6N_WxGjxWsYYq2U-j_UEfscxx2xSYxx9ACrgm1z-5gHXl1FjZ6t7RiD2gb1K3iWPwJmQiH_C9G2zfLCio7ih15HGaH8FJu8yTgWSm3QVhIj2f6KuNBHni1TM4eXlr7Dk-II8PQls8pHbUpLsxG9JhO4L2Rfx6FjBQx3FJqcgAF87EsO7WGqeqqdDr7JR6NUW_mOz3zQz2l4lpqYT1rInzF0gEO8skkzUCJTmGfiMMEKTQkLKmYzeSXD8PTA3mrjg61dsms_IODv0c4QEpfAnLKoZQ4j-dgJmpOtIzWa20uAFahre9rs1BB3XyuPg6z2tWqtclba2hus13P_lebQkqQLilYqSCBhc8czHdtFRyVD6f48FNUH8ZDtdEybw_a0EieD6XLlNbhDvHDtaEoIIn9pELMNNbz60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaXQ1nQoYn34vfhUEf3J1R67OYnmq9qqpZwjikrzmoFcHQgz3f2H9gMRP8qh8mVWrYVmc1qB4pdjQzTP1g8A8DPHLtBvijySiVdtgCK8RW_cUjiTjZhDXo1brqlo7pI04Fr86mnPGIYvJHK4jDIc0VFLVd8GMOGtBwrwSpGPU4oBsMHrjtIpI0Yzhd0snxp2820d-wzCRNhC9EaWoa-hualZhf0dmh8Have6M2Hp5Kr4EZgHABbtv1V6d9pOE2tRiaSCv24aAyNn1yym3oLyJ2j1Ma6YTBVPGVx016fOLlmTA3s2Emevl5PhmaKf5aDKnBlJFg6urt9YI89R7W7RBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=Jzt9Rl4H571wUuHvHsMjujbQ3VrbnXr_TLNokDkoMYJG3JXJWo7qOQaFR52dpNCW0XZe0n5GVkgpvk2OPjnrx5pr4FCfaLVcFVXDTwIrUiZ9o91v3PoCOcbflkuHWAyloDmM9L-o6JNxjqw1GpEIFuQzIq98qsL5j5_cFK7r6DFNzUmvDRgA7co8uIl4npGePsf0pKqtBn7o38PAQc93gVFRhbIKsjN1kog40CTCgxdvZ8x1A9wHS4wB6s-iEEWvMRbFIFODHwIjLgWOxK8cEICc6Bbhd-jJZ9r4HBJnUlTt7H6CTWo9j3A-mhRy1J-yZOVHO_2mHleTw1Ji9hOrEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=Jzt9Rl4H571wUuHvHsMjujbQ3VrbnXr_TLNokDkoMYJG3JXJWo7qOQaFR52dpNCW0XZe0n5GVkgpvk2OPjnrx5pr4FCfaLVcFVXDTwIrUiZ9o91v3PoCOcbflkuHWAyloDmM9L-o6JNxjqw1GpEIFuQzIq98qsL5j5_cFK7r6DFNzUmvDRgA7co8uIl4npGePsf0pKqtBn7o38PAQc93gVFRhbIKsjN1kog40CTCgxdvZ8x1A9wHS4wB6s-iEEWvMRbFIFODHwIjLgWOxK8cEICc6Bbhd-jJZ9r4HBJnUlTt7H6CTWo9j3A-mhRy1J-yZOVHO_2mHleTw1Ji9hOrEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=oBhpNlY4Co5McQ0QPHR_iRKE1u9u82SZIytWNyjwglHtS3_F1t1gWgC80OUnC7oySEFu8MQUMVRbD5Aq5IAzJFP_x2hUjX2nOQ5EF7w1tu6niY9tgIt6G6i0A4g2QoeR6zgkxYQPjngaNmRRuGP0Pzsn39YGJJqRuJQeZu68rYi_cTWY-PwBlkuRqZKllBiYeAnAkQyExVimSRZJqKaEALWHzBPAyuY3sWnkjh4kZMXNkUaMfI7dh23LMIVLXbORtb6SRdfjccut4hBItCoNP8-TRgLOWdoxFnlISsT3NVKrPjGpW95sJgODAe05tJI-_TCBnlOgLgM0sn8sKTJhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=oBhpNlY4Co5McQ0QPHR_iRKE1u9u82SZIytWNyjwglHtS3_F1t1gWgC80OUnC7oySEFu8MQUMVRbD5Aq5IAzJFP_x2hUjX2nOQ5EF7w1tu6niY9tgIt6G6i0A4g2QoeR6zgkxYQPjngaNmRRuGP0Pzsn39YGJJqRuJQeZu68rYi_cTWY-PwBlkuRqZKllBiYeAnAkQyExVimSRZJqKaEALWHzBPAyuY3sWnkjh4kZMXNkUaMfI7dh23LMIVLXbORtb6SRdfjccut4hBItCoNP8-TRgLOWdoxFnlISsT3NVKrPjGpW95sJgODAe05tJI-_TCBnlOgLgM0sn8sKTJhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=Av6CfLH9WxOrOmYrRxhMPnq7sYIr3-6yNyElO5kfxJ5jv4Z5HsyR8orz7pe0Sj1EGZiA5sMga_AXqCm_w6E-ezvengYzC0QIjhYCq8TKpTeh8MR_udb7nfSLxwLcoh1anCd3tISEl3xbnl_sfdsxXjaUkl9ALNRebtFaT_1CcYHE38F4W3GtZUdJxrckDIPw112-cpqHl-KqCajZfJTmOHSqwuFO2Y9e1c3NvPm75CVxIYbSOhjcAm5eE6Nwfr379iw59O_7CuY7Y4k2PBjyXJeFO4cBCekNZXwu6_yScZwlxC2pvJr1LcnIN_pq4MlilOXKPeaAcKdBxhvG3iBOHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=Av6CfLH9WxOrOmYrRxhMPnq7sYIr3-6yNyElO5kfxJ5jv4Z5HsyR8orz7pe0Sj1EGZiA5sMga_AXqCm_w6E-ezvengYzC0QIjhYCq8TKpTeh8MR_udb7nfSLxwLcoh1anCd3tISEl3xbnl_sfdsxXjaUkl9ALNRebtFaT_1CcYHE38F4W3GtZUdJxrckDIPw112-cpqHl-KqCajZfJTmOHSqwuFO2Y9e1c3NvPm75CVxIYbSOhjcAm5eE6Nwfr379iw59O_7CuY7Y4k2PBjyXJeFO4cBCekNZXwu6_yScZwlxC2pvJr1LcnIN_pq4MlilOXKPeaAcKdBxhvG3iBOHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=jn3J6_B4gtptevLJN3-hETl03CwLH2UrJTexZan9AB9mo2PxNmoqf67LwVO10VHtnfrjl9KcKIEFBVDNb3K6UiCceOhh-Z7JV2svU3DFE7lbFOPuOM15eKm15yNCuO_xE6GPChTOMUdV2yHMyaEFL16Ggxspi1LZZqUncZifgGxINYJ1D0wOpZ6UiJl421FVyZggbqq_fGkAuR_G6WOvHDEYCTQfSH0FMHyXFAMTueB58xo0zQhV_yPA3ygH_HEbp3y4rYx3yoklgewI2JLJvncpCMrXTvYcksrvUgqHZ7Z4wZLVDnLLRVNpOdkJhULW9S8d9abu9nL-lWkgDFhsBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=jn3J6_B4gtptevLJN3-hETl03CwLH2UrJTexZan9AB9mo2PxNmoqf67LwVO10VHtnfrjl9KcKIEFBVDNb3K6UiCceOhh-Z7JV2svU3DFE7lbFOPuOM15eKm15yNCuO_xE6GPChTOMUdV2yHMyaEFL16Ggxspi1LZZqUncZifgGxINYJ1D0wOpZ6UiJl421FVyZggbqq_fGkAuR_G6WOvHDEYCTQfSH0FMHyXFAMTueB58xo0zQhV_yPA3ygH_HEbp3y4rYx3yoklgewI2JLJvncpCMrXTvYcksrvUgqHZ7Z4wZLVDnLLRVNpOdkJhULW9S8d9abu9nL-lWkgDFhsBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=EMOlj2-c73EqzVQuRaikXx2S7PxkNRMkrzUb2UCsmjrWkkja70WOYiTuY2zYBG0TtRfd-WnkOqq8bFZ21KbrkaW9_SvFnV9xT5dvqXNxJ_Sjp_nT2RxEpgSgRuOa-AEOQRbeDvvkZaELOCB9lyhbFE89UJEnjQsLSQivIaoFQ-e1SKUZTAbYJIYFiqa8-r1iKg8y3sg4grvh_1TGUooY7CXomfgEd4u4MDAfDD1S0AEt8k0ouEPxl-aT1xSNIpyv85bVxindDxIyEqb4p6WXPwizL0D0W0nOr72hO10Ci1-ZVsBRc9wFokP_xcr41Y67PBY9Dg2NaBkRrR_diTVf0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=EMOlj2-c73EqzVQuRaikXx2S7PxkNRMkrzUb2UCsmjrWkkja70WOYiTuY2zYBG0TtRfd-WnkOqq8bFZ21KbrkaW9_SvFnV9xT5dvqXNxJ_Sjp_nT2RxEpgSgRuOa-AEOQRbeDvvkZaELOCB9lyhbFE89UJEnjQsLSQivIaoFQ-e1SKUZTAbYJIYFiqa8-r1iKg8y3sg4grvh_1TGUooY7CXomfgEd4u4MDAfDD1S0AEt8k0ouEPxl-aT1xSNIpyv85bVxindDxIyEqb4p6WXPwizL0D0W0nOr72hO10Ci1-ZVsBRc9wFokP_xcr41Y67PBY9Dg2NaBkRrR_diTVf0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=v33lKOevw_LE2Ao4c2nJinz2wsxZVTEYHlvOE1xm3CLWyI_mJsPU5uo2DWgwEiFJUfGXKa3x21mmy7SNCm4irE9CW0_P7woVC6X-nhxKCnNpA3-P03QyRXM4krmi8qGVOikecAxcv4bVzV4DwE2R2a0H75JLUZEw2MbomM7JSP_UUsjOnJkrZiCguEZL4JnE-zMRqPphcdJkh6D9gxXYsBVgRa0qJq2KWvvpu-nnipNXSZCVvZ4fmTymGLt9VDtsowTbKIGv-9wUSqcpTmok_YE2mw7k8KwYjZXb-3n3I1KmmdcmpMgwnCUrysEqElJ3SL0R7mJXZzpkljq78XFGiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=v33lKOevw_LE2Ao4c2nJinz2wsxZVTEYHlvOE1xm3CLWyI_mJsPU5uo2DWgwEiFJUfGXKa3x21mmy7SNCm4irE9CW0_P7woVC6X-nhxKCnNpA3-P03QyRXM4krmi8qGVOikecAxcv4bVzV4DwE2R2a0H75JLUZEw2MbomM7JSP_UUsjOnJkrZiCguEZL4JnE-zMRqPphcdJkh6D9gxXYsBVgRa0qJq2KWvvpu-nnipNXSZCVvZ4fmTymGLt9VDtsowTbKIGv-9wUSqcpTmok_YE2mw7k8KwYjZXb-3n3I1KmmdcmpMgwnCUrysEqElJ3SL0R7mJXZzpkljq78XFGiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=f416aKV1TzQghQHI7C8pbf6EGci-rLC-JmL6bAZcxJU-kN4G2pHgMRPbwZkIGDbnROSth-HE_oRpzKYOaeNZy5EXJVVI0AZhBxzoJ27aZQHrvb7rNFSGw_29rD1q8bio40Bvj7FI_FeJpgD0df7hsIbnKVFsMRFhByU7a4FSw1f6Q3fZhWVLO3ktgs8spSkko6NABNRj3dTtT2Ht5RgeqmU-99nAk1whp_Xx5MnTb2uLc_M7pJhTRo41LzvkmoKIraGoFeQlYk3qqS9eI0_9BZkHJmejv6fWVkcqkg7E5XxiEmTyE0l6RQQoWeu5N-lCWplW_VZiX-Hh7aMZmgqyBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=f416aKV1TzQghQHI7C8pbf6EGci-rLC-JmL6bAZcxJU-kN4G2pHgMRPbwZkIGDbnROSth-HE_oRpzKYOaeNZy5EXJVVI0AZhBxzoJ27aZQHrvb7rNFSGw_29rD1q8bio40Bvj7FI_FeJpgD0df7hsIbnKVFsMRFhByU7a4FSw1f6Q3fZhWVLO3ktgs8spSkko6NABNRj3dTtT2Ht5RgeqmU-99nAk1whp_Xx5MnTb2uLc_M7pJhTRo41LzvkmoKIraGoFeQlYk3qqS9eI0_9BZkHJmejv6fWVkcqkg7E5XxiEmTyE0l6RQQoWeu5N-lCWplW_VZiX-Hh7aMZmgqyBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=AxNrVIV7wLrZQ_RFSLfmPgyW3eZxnR44IxBOZYNCkMcT_I4Mdz-1HwKq75dBi4bzuT2oPdi9JZ0ygbMmKP0gYlI8SfgLLtN4GNsJ3m69ZbGtL8e984Z5n5SIOwCIqq2ZJZeK0pinQgwEzsVCStNRJ3vGtZN1SOdqmoBtl_BsmwcjgL5KnqA1cFyVpvQ1qiFpmlWPmRyZf_LCiO8Ka_NH6dbJf5SuPIc8tRvs4RvbRieXHqJW7UiLRum-yWZhlrrCdosdE8rvqYhFOj0eKRn219QAo1G1r4VBrutr0dyxfmNobEo3-jj161mwSOkxBrYk2gHMcxqLyPlLgixVYvDxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=AxNrVIV7wLrZQ_RFSLfmPgyW3eZxnR44IxBOZYNCkMcT_I4Mdz-1HwKq75dBi4bzuT2oPdi9JZ0ygbMmKP0gYlI8SfgLLtN4GNsJ3m69ZbGtL8e984Z5n5SIOwCIqq2ZJZeK0pinQgwEzsVCStNRJ3vGtZN1SOdqmoBtl_BsmwcjgL5KnqA1cFyVpvQ1qiFpmlWPmRyZf_LCiO8Ka_NH6dbJf5SuPIc8tRvs4RvbRieXHqJW7UiLRum-yWZhlrrCdosdE8rvqYhFOj0eKRn219QAo1G1r4VBrutr0dyxfmNobEo3-jj161mwSOkxBrYk2gHMcxqLyPlLgixVYvDxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=iyzzwwwEv2MHm5LecojW2PeZAzdk5ckUM7Zwv12cOVOE3BVPPfr1uEYzYuJjjHnsg_4J3mydQ4op2LO8IEXpWYwpf8IfkHbM0OZ8dzqCa3cej3jgSX5DHHbyz-CctPsQpnhSGc9fMP3PYpKuX1uK_1YlQmDPeOiHtmi40T62J09auqzDP1PcN5buVqE8R6hdk5-vRGRSfMZvPRkJ3u6W-E8bzYoZdfOjnUXWLAseHCYnfL8_hFihKgISm4KZ0wHYNaIeY1zg7qciljR_B68Yo1A5pTyxRERrPHuaBa58waD0IqfMlD2sSUSeXaRj0BzhkJB5KSbDi1srN6KOhKP3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=iyzzwwwEv2MHm5LecojW2PeZAzdk5ckUM7Zwv12cOVOE3BVPPfr1uEYzYuJjjHnsg_4J3mydQ4op2LO8IEXpWYwpf8IfkHbM0OZ8dzqCa3cej3jgSX5DHHbyz-CctPsQpnhSGc9fMP3PYpKuX1uK_1YlQmDPeOiHtmi40T62J09auqzDP1PcN5buVqE8R6hdk5-vRGRSfMZvPRkJ3u6W-E8bzYoZdfOjnUXWLAseHCYnfL8_hFihKgISm4KZ0wHYNaIeY1zg7qciljR_B68Yo1A5pTyxRERrPHuaBa58waD0IqfMlD2sSUSeXaRj0BzhkJB5KSbDi1srN6KOhKP3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=QB9e7n0Pvqr_hZZsoRc6Q50d54Q6q9gBhcMiQOW3o7gM25yyo1iBT9R1-dI46HfR5PK0WBD9v_dfUA8u3YhJup_vLzcgefrcuUsPz0FzhPj5kZatltB8wUjv6AivXdKJ2r3VesJXR74TDVlcyLv3fSl-7FKE_Nt2kB89stv9ImX3rlarQsQ7-VmR4EtvadhUrU4TBfoeBZceR_BjNulZlHpQSfUzzumZETrZcwF31ACHP-6ZG6HBk-9GZbM6AtyySzDPpYXn7v3o6qokLn0GJPzapyUaRJEF_FRPBzTIbLKxmcYaVgHaGKeHTQcYSgDwd4DtEApnOlCfjDukNsfx5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=QB9e7n0Pvqr_hZZsoRc6Q50d54Q6q9gBhcMiQOW3o7gM25yyo1iBT9R1-dI46HfR5PK0WBD9v_dfUA8u3YhJup_vLzcgefrcuUsPz0FzhPj5kZatltB8wUjv6AivXdKJ2r3VesJXR74TDVlcyLv3fSl-7FKE_Nt2kB89stv9ImX3rlarQsQ7-VmR4EtvadhUrU4TBfoeBZceR_BjNulZlHpQSfUzzumZETrZcwF31ACHP-6ZG6HBk-9GZbM6AtyySzDPpYXn7v3o6qokLn0GJPzapyUaRJEF_FRPBzTIbLKxmcYaVgHaGKeHTQcYSgDwd4DtEApnOlCfjDukNsfx5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=QNMbsMoIplzUpcUVDe_tgR2R5rk3VZ6EbmBlUI8m4H4_jnBDB86Iy0PJ04JO-BrEtPNh7ozI2rBIPj7DRj22YlbN1-s8FCYKWQfdYwoOJA3AIoRMGuQ_Y7FQN_f-erSYTE0AFYync21RWVNyzT3MbY_UJ8w5MREtIzQWDkBUZcE45XwsXcVqG6Zw-il59Co4cJLk7QapTm_3lq5cOQCYjwtyG5t-8pLnedUYI2F3oiKep7DoH5wPLv1mA-u8LGqZTqmW-PBxzx5QUj8c5sR5F_R1WfIAnjCabsl0biCeuRcVvPfwDKej0N4HG6efrQl0TuIsPpVP7jrlsAUrVGjJAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=QNMbsMoIplzUpcUVDe_tgR2R5rk3VZ6EbmBlUI8m4H4_jnBDB86Iy0PJ04JO-BrEtPNh7ozI2rBIPj7DRj22YlbN1-s8FCYKWQfdYwoOJA3AIoRMGuQ_Y7FQN_f-erSYTE0AFYync21RWVNyzT3MbY_UJ8w5MREtIzQWDkBUZcE45XwsXcVqG6Zw-il59Co4cJLk7QapTm_3lq5cOQCYjwtyG5t-8pLnedUYI2F3oiKep7DoH5wPLv1mA-u8LGqZTqmW-PBxzx5QUj8c5sR5F_R1WfIAnjCabsl0biCeuRcVvPfwDKej0N4HG6efrQl0TuIsPpVP7jrlsAUrVGjJAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JMWCcJNCsztpo-uOYuZiLrTr2RQu2BzlEnjQU6-AXKiFJavEIqUurAuFGmvcMDO6TtVo8VImQmY0CVT9Mvx7XIpBEaVE1U2HkxxpfqXhwKBtCIf3pXDhyB9P5o56bcaLScCEPL0LubvTdaGXUi4rtlta8dQmHqOcjhZZi6FFDUKbM3EJhOIGAEThSdxhExjCz7KLTB4Y0YwS0a5CYK1kYVOAeJwjCG6NvJqyIkPqK0bf2WJBLUjQwcO5f4Sd3qwgVuAJ5IRePzxj4eg7i0lwoKbaasPL6QGMs2vdC5xm-baTFVNRads3qV3W_CqHYyBJyolUa0YmtZzZl1x2Un_ZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=sdvfQOwI7u6aelNEqrIQ6Y-62aMEX3qsIbSVlyRCwEHzmtRqPFq394yABmF6YSrt2cwFiPUQO6YnszaljuqwTIqBFFkHqzBsENaxZ6cmiCQ5clrVQ6vaiqeeEXa_M25LHCXjbgORa-rLOq8UVwsAqt18bGvvmTaK5iSPXv1xpP-Bo1a887EjiX60598wBbIOntNphT_Yr_ZDvWrewqlUx0Ac-SIRnuw04VIxUIyZk_xHUxh0AjqCNyYoSfmehWttRE3ziaJ9gvgiLTpKDIvElqkvD_IUz-RJpML4YPeO29mPO4yRqDY1oGCziZQGOluQClW0Dox66B5nZDekbzXdDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=sdvfQOwI7u6aelNEqrIQ6Y-62aMEX3qsIbSVlyRCwEHzmtRqPFq394yABmF6YSrt2cwFiPUQO6YnszaljuqwTIqBFFkHqzBsENaxZ6cmiCQ5clrVQ6vaiqeeEXa_M25LHCXjbgORa-rLOq8UVwsAqt18bGvvmTaK5iSPXv1xpP-Bo1a887EjiX60598wBbIOntNphT_Yr_ZDvWrewqlUx0Ac-SIRnuw04VIxUIyZk_xHUxh0AjqCNyYoSfmehWttRE3ziaJ9gvgiLTpKDIvElqkvD_IUz-RJpML4YPeO29mPO4yRqDY1oGCziZQGOluQClW0Dox66B5nZDekbzXdDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf_nUE5CSmliZxdqEXRzRbyAYnoq859CDXLb5UovD0sNREgFkYzahyfl08DwW7z0zM-cjxC2y28lRisWn71Qg-g78Wa9HcVVB_K0RAH7lwQ2DIuNRN3lEQMuAVo068v9aaokXXtQiestbEYZJAN9euZCbp08JCb9EVmWWMlOq6ehaV5vLczJXzMG3iz9p0ojdNcbhcIgFu9y854RF3T1_z6tTKIh04mm-Bzn7uO31l3lwS3kuGDQU8rrmqWRHd03HrDflQAuql0qzuJe5RmRHAiR7yNtqh1Z4dzeC_WtJ5MzzNmcybDsCBH2Jzjs3bDyG1f-LT0eVMk35XVBR5mtgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=Od_4m9yBNP94mlvamMBSxO2SRWY7O9WngK10ir2n473yQpaFqPQ4xRG8nHb9BcZ45dkHVwXJcUN21ttNo-0vOSkg4MCkO9WuBl4wd4-sf0DglpsyMuuCwsEauEjmpaiaIIvAv1M7_hMUL51WMkivjqgRvqHGDrmjbDp_vmaWRc2fJCSYTu412EOSVfjB7nR-nDL5UsYd46jNLopDaYItApgGqZBz-tPs-AFJ4w4d6JzkGcdjhCB48CxRWbBfd0fuH7Hnz3iA3mfI51QcvTJlmWjBjmekH5mPKaPdrRGEA0w0VSUwO0pvs3OIvSluHXYaWil9aNmrEamyk3m_kHpDpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=Od_4m9yBNP94mlvamMBSxO2SRWY7O9WngK10ir2n473yQpaFqPQ4xRG8nHb9BcZ45dkHVwXJcUN21ttNo-0vOSkg4MCkO9WuBl4wd4-sf0DglpsyMuuCwsEauEjmpaiaIIvAv1M7_hMUL51WMkivjqgRvqHGDrmjbDp_vmaWRc2fJCSYTu412EOSVfjB7nR-nDL5UsYd46jNLopDaYItApgGqZBz-tPs-AFJ4w4d6JzkGcdjhCB48CxRWbBfd0fuH7Hnz3iA3mfI51QcvTJlmWjBjmekH5mPKaPdrRGEA0w0VSUwO0pvs3OIvSluHXYaWil9aNmrEamyk3m_kHpDpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=OGMg7-qr7t0oe2i7MslXEfQ8SE598BvdUeqIoXnBZucZzGMIwUMMgas3l2kkXaIexBZi1mHtt0q6gh8vFhGGRaOFvqBqiKhAUzpMpOvulhn0SI9m93oQbQMsgoRRE2T30Ro0KOLTFBF_1o1znaQl0A_arzaKPS2M-Msoumjro-fZlTHv7J3wv4P-CL1tOZgUidGhLsHvFgkF7YnnDaH3Y10tlZlWOrx6hwAiSozZ6bVjK6PFNiCnxqU2cJGKDNmFCJNTqMcPxCFaxEVKyj83xWCEFRXnGxZck1V1L7f9WTU09t63LS-qlYS7rXo3cV8MJ8JDo37vzYhx0PMJXPprrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=OGMg7-qr7t0oe2i7MslXEfQ8SE598BvdUeqIoXnBZucZzGMIwUMMgas3l2kkXaIexBZi1mHtt0q6gh8vFhGGRaOFvqBqiKhAUzpMpOvulhn0SI9m93oQbQMsgoRRE2T30Ro0KOLTFBF_1o1znaQl0A_arzaKPS2M-Msoumjro-fZlTHv7J3wv4P-CL1tOZgUidGhLsHvFgkF7YnnDaH3Y10tlZlWOrx6hwAiSozZ6bVjK6PFNiCnxqU2cJGKDNmFCJNTqMcPxCFaxEVKyj83xWCEFRXnGxZck1V1L7f9WTU09t63LS-qlYS7rXo3cV8MJ8JDo37vzYhx0PMJXPprrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=ZlPSCC5HKDnpylP43mhLLeuXmJzQs9DynmiZrcrOKnrk1UrjlUhiwkw9W6QpHp9vgI4dNUAJg6UIOYuIpc-6Q7wRDZC8_Lpfhi-9moOG4-EIS-B1ieQ-qJ4tnvyx7JGtbS1sTVChpudacdnGNDX_l3SkIGjvvNZxeAy1Yaxqrt6grTyx9Q8C36-Vv9ykZiRm3qaXBLplhn5vKY1djDQbe2N8amEMikj5bxmQxE7L_UJZNSkRayewA0OcSrcHTk_3kDwg5ylu0t5Fa0ryzdV6oVJH5r5b0On7SD3HbYqcTXCP-LaSsvoWFmFil1a8BVeqPsnBCJgLeIYbXiEcKLMvPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=ZlPSCC5HKDnpylP43mhLLeuXmJzQs9DynmiZrcrOKnrk1UrjlUhiwkw9W6QpHp9vgI4dNUAJg6UIOYuIpc-6Q7wRDZC8_Lpfhi-9moOG4-EIS-B1ieQ-qJ4tnvyx7JGtbS1sTVChpudacdnGNDX_l3SkIGjvvNZxeAy1Yaxqrt6grTyx9Q8C36-Vv9ykZiRm3qaXBLplhn5vKY1djDQbe2N8amEMikj5bxmQxE7L_UJZNSkRayewA0OcSrcHTk_3kDwg5ylu0t5Fa0ryzdV6oVJH5r5b0On7SD3HbYqcTXCP-LaSsvoWFmFil1a8BVeqPsnBCJgLeIYbXiEcKLMvPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=SGmyWgQUvsdWFXFFzqizZBvY3-aHVec1OnSzH8JwYlfCWTnLkpBgf5Mt30qFInS1kuXfSj3k0BGk9gLmMMk6kh9hwbVvoIiQicfvuqWvELbAvbNqXVHAAe8hz7Xm74Cf-sgFMsrt7TsW3DJyCNij8VM9PfSYEbw0QJERSesy_Is6fEKo-DC3RrsCURAgC_Fno5beQUwaBAhcQLgGF3cM5_6U9fMEUoFboZTjESvOVAzKQXVtAhTgXV8nzEEWb-jsHV2Jwg0qQta8mNtPdSFJLfaZQ52tvysGliPzQ-h9IgvpOF8EmldwDPk5mGN_o3UJ4aPaTNkDIpmGO5hxvWYnRhCOMqhlLWCBoeeBbaZvTTeVHv2CBxXly45xUetBgt7ERhhjMI4PWIlCE95MaHoWBZdshpbjTUWKsDRcDZmswsMkhKKPZHnZOBxLB5W-o8gWITMlFo_eg5xnrUp6lkfuJPjEf8O7NDNOnk4DqrbDqR3ijc7jTKtN6c-FTQwJwhyhjJOSCVqn410kS75cRfUaxh4pPymJx65MruzdttjypB9xiUUIJ8iljuPxkg5qD8fXzGZCT6e8IV-aU5YkigLp_3xqhPUOn2jsYtqJt6pdveRfPUOXEcl_vLHQJeVTiqQcbFdeDgoQGaWeh7R3W_oUGndOJsHwUrGfv8-IGNhow2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=SGmyWgQUvsdWFXFFzqizZBvY3-aHVec1OnSzH8JwYlfCWTnLkpBgf5Mt30qFInS1kuXfSj3k0BGk9gLmMMk6kh9hwbVvoIiQicfvuqWvELbAvbNqXVHAAe8hz7Xm74Cf-sgFMsrt7TsW3DJyCNij8VM9PfSYEbw0QJERSesy_Is6fEKo-DC3RrsCURAgC_Fno5beQUwaBAhcQLgGF3cM5_6U9fMEUoFboZTjESvOVAzKQXVtAhTgXV8nzEEWb-jsHV2Jwg0qQta8mNtPdSFJLfaZQ52tvysGliPzQ-h9IgvpOF8EmldwDPk5mGN_o3UJ4aPaTNkDIpmGO5hxvWYnRhCOMqhlLWCBoeeBbaZvTTeVHv2CBxXly45xUetBgt7ERhhjMI4PWIlCE95MaHoWBZdshpbjTUWKsDRcDZmswsMkhKKPZHnZOBxLB5W-o8gWITMlFo_eg5xnrUp6lkfuJPjEf8O7NDNOnk4DqrbDqR3ijc7jTKtN6c-FTQwJwhyhjJOSCVqn410kS75cRfUaxh4pPymJx65MruzdttjypB9xiUUIJ8iljuPxkg5qD8fXzGZCT6e8IV-aU5YkigLp_3xqhPUOn2jsYtqJt6pdveRfPUOXEcl_vLHQJeVTiqQcbFdeDgoQGaWeh7R3W_oUGndOJsHwUrGfv8-IGNhow2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8EDO8YjoHzgkEgwSozXJUBruUWIi5b9XX49zEnpUNsxkaxIX2Mq87yhFuNwNTjnUp8zpF0Lu7rk5PcMH8myYejoxxBQXE7MJVWIoRf4Zclh-PUmkKhUwU_DdkGUspcPZOl5SoMT7e0BDd1WzJARXwa3pdsjqWVBzERs5OEJusQknzbPRfJoiLktv_b55aKUcEyqjOixs_olPVNZ_ffyCJpO_JIV1iW7_gs-meQfM9sJmWleDbMT5BCqJ4d_wRvIWFgzxA6n9G50jdOVDI5xlvhRssThnw_Gw_svkt8fXljgJfm9LhcUT1uattRhlA3CDoGpx37xtrdCj0kjOiYC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIaLwQlCHjPZPr0cWCJAn2tWlI1Bz5QSF5FUz98QgjNYQP25R7UX33W54ZcX42oOLVFPfoL-uYtsY-pFBPwDo2bqtMpZEEUVjcf_iaPAqJ_0_TzzNk-EJDOeoaNZ2TwcgdxaxAp0E-kW0uhnGrhzqI5QOx-sqLUTRbMb8f3pCh5WLav36fyldC_0gvrn1CGy7co3nVWncEhFf-XVkkWpSTeBNub23WIctfQXC36M1uKAtRRvgAd5dTnPggNel0VeckBT6hHASIx-bxQRbJ1_qiy9vAcoBr9HjXYINI9QV4TtxCJIhxm1aPk0rDjZxe9CswKT3MLUhxFbWGl4Ginkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=OnSJQHAjc9evTsN0RPfw1yYkE4xvZA5jKqxtSOpAOiN-a0TS81akJbchgx2MuZhWUAglEklSU3nfkMou9VDUdBgvSZtyZZIdnTH8zWr3IDU9FZfsg6nNagtZtgZTe2mbMaM1ew_GXAwZ-KghD0s8nyQva23Oa3P_RzwhKTlxFkpJFqUY_XSaF8yV7w7qWJWrujWFyqYz949DFMN-TojdIV9AnNXX-__4H8-OAEh2COzoj_2SaGpo9WxmFiRQIlH1PAKTpa_OinCeblQMnU5lYqx6--Gh-r_-AZ40LdbQP2a0ANerm4ITw3EPTCEPcnHGAteoj6oTwlDmuOCPswzOfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=OnSJQHAjc9evTsN0RPfw1yYkE4xvZA5jKqxtSOpAOiN-a0TS81akJbchgx2MuZhWUAglEklSU3nfkMou9VDUdBgvSZtyZZIdnTH8zWr3IDU9FZfsg6nNagtZtgZTe2mbMaM1ew_GXAwZ-KghD0s8nyQva23Oa3P_RzwhKTlxFkpJFqUY_XSaF8yV7w7qWJWrujWFyqYz949DFMN-TojdIV9AnNXX-__4H8-OAEh2COzoj_2SaGpo9WxmFiRQIlH1PAKTpa_OinCeblQMnU5lYqx6--Gh-r_-AZ40LdbQP2a0ANerm4ITw3EPTCEPcnHGAteoj6oTwlDmuOCPswzOfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=E3oljeRPqPjhF_Ad_oAjhkG4lZF4bp3Mq3wzlZOLvmcsgTy9gZ7Owryz5PHbGifeybqShFvpIvavrKsxfyB5sOJo7u8C5b0N3yHbAQP6tjMORTH8etn-N-Arv9M9CzO63qmfKrf-xgJRvewlvTulnHDI61TyBEz-i8SsLJiTtwesL-cRV6EcE6xyAoHq3SDPuJxzKbF895iC5CboCmoHHvSoy9Pn36o9QueZOzK0AkeWdOwQc9cPDposixUKUyWfvoijyJc3fNOtfVSfDX7G2cDEchYlPXgZPgCU3qLfVlAPost7bl0N-pz-uHjj9ufJPpQjEo2vOPvv3mHC4vq0HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=E3oljeRPqPjhF_Ad_oAjhkG4lZF4bp3Mq3wzlZOLvmcsgTy9gZ7Owryz5PHbGifeybqShFvpIvavrKsxfyB5sOJo7u8C5b0N3yHbAQP6tjMORTH8etn-N-Arv9M9CzO63qmfKrf-xgJRvewlvTulnHDI61TyBEz-i8SsLJiTtwesL-cRV6EcE6xyAoHq3SDPuJxzKbF895iC5CboCmoHHvSoy9Pn36o9QueZOzK0AkeWdOwQc9cPDposixUKUyWfvoijyJc3fNOtfVSfDX7G2cDEchYlPXgZPgCU3qLfVlAPost7bl0N-pz-uHjj9ufJPpQjEo2vOPvv3mHC4vq0HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
