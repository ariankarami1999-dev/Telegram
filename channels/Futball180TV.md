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
<img src="https://cdn5.telesco.pe/file/QcDJAgCY8Hj73dMOAKhWYEG4ikGZHtW7sI6SI-zwEbnYlLk3-8p-8RK-SEWM5bU4ZjAJfMiWaQmVB6EMHiGwFgL3w6_KjIalXkXvxE0q66tdAWvO4cjZw7cdAUu-y4wcPvtUYcLBiJKfxcmAquJmaYzRzGoxZkgeGr67P-V3lbckc5HmYmsTQt6YB6mJMPj6OXnumkpFfwOfpYOEJRyvbxZf80cU7AeQa6VRvu_LQjrzpVhDRiZNYYjmmctHAeUUxzZA7hEgMD_vXEjsTwopjgjmq9OV8KLv45Pb3X0ptc3w8RrifMNRe1CtE2RG-748uZMdZVdz7OcpydqtjOYLYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 427K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 05:39:11</div>
<hr>

<div class="tg-post" id="msg-105562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/105562" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN30SfnMt9z9wd-Xf16D5qP5FIsdcbB7m-cAWZbXfTZsTcnTIxEsTX-eneiJHvN4UMM_OX1Yo0sYkaipdQlrFmvZ5zNxRS2-OLzB--e3sChd19aiqFvDkqLTkD9-1M1OKOFFW1dxoVnRfKs8Y_s2jDVhIQ3f4K2IbLn11qPN8R2TU9BPXEz-LlcVtJB8GPll69v_QIaAt4OIoP1xdtvnDVUlu9V0DZClGjtdzfbeOlZQRVbAfuRBjheq-fbOekA0h5_pRKwxKhfiMP9P3Am4umV5-Dz8cgFKPksF4a9KpjGWDCBDEjHG493ZiYHMc1dyUigJTHfbVlVVRnVeJZcpCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/105561" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/105560" target="_blank">📅 01:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=u0WLylGMoTwaU6kCHeRWkENMMEU9f90TZOEkbdLPyfXPy21xPOYWW9DQbVp0wpZXWzhbu3Of3ktA2Z--xiGpO7jJAMYh4Meg7cH5WH8sDZ_DR4QUXq0Ks4UN28_CIVCAonLYMwAJ5Xee9S3ju4NxFQELUbgiyIVRvUmqi35hcdjy2R_px23QIGhE40fgvXhwrrUYQxF3YXs9rVE0V6zdLib5xuJPQOaY8wgVy6os57WeN4gIu5fuToXxvFnxpcnOyOfZ3ZDyqaJ0PMpOqbcO7fQMZWsekPZ2ul3TcvXoW61AsnTaQbUh1liT5rMWh87lWK3RjsRLYU30LuTJFdP1LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=u0WLylGMoTwaU6kCHeRWkENMMEU9f90TZOEkbdLPyfXPy21xPOYWW9DQbVp0wpZXWzhbu3Of3ktA2Z--xiGpO7jJAMYh4Meg7cH5WH8sDZ_DR4QUXq0Ks4UN28_CIVCAonLYMwAJ5Xee9S3ju4NxFQELUbgiyIVRvUmqi35hcdjy2R_px23QIGhE40fgvXhwrrUYQxF3YXs9rVE0V6zdLib5xuJPQOaY8wgVy6os57WeN4gIu5fuToXxvFnxpcnOyOfZ3ZDyqaJ0PMpOqbcO7fQMZWsekPZ2ul3TcvXoW61AsnTaQbUh1liT5rMWh87lWK3RjsRLYU30LuTJFdP1LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رفتار سرد مورینیو و وینیسیوس بعد بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/105559" target="_blank">📅 01:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPS3tsNPuZMk4KWG_RFpOqaFEL-74eV95b39-zKJXfnHekbd0NPkLDsljYfZ5ElRYkEYd2zWTD8xR6k36ZswSnO1JnZ6uAh_Yty3y691P0ztLlsCOOMeHCkQP8rxrIkRHyI1Ikqlyi--aMnHzhYJRaJaOGjV1XQ3bshiP9vJPnR4S0YqkvdTgY0K-LY5palqvPnoSzienqluffrfeInkTcsxhzLmcHlOeuep7mjyCb8vMU4JAe-9_DjJp-Uq7Qtf1axtFdMGNdiSTnwUczZn0-vcUaky5hk99Z84f1gsPy3VJhzDNpSq0ac2gpmZ3BUx1EMWsauJhXkX2_LLAGnj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
#فکت
؛ در آخرین‌فصلی که رئال‌مادرید مورینیو مقابل بتیس در خارج از خانه باخت، آخر فصل بارسلونا با کسب ۱۰۰ امتیاز قهرمان لالیگا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/105558" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmm-oQGdycOXrIYqG0_BpIRNVR6KgiZr4VXdxQeKt1GbdtihnYVxEGdt0AhHLGF_B4n6yMBterpzs_K76Q7YlK0XxassLYpsSQA8_KWHfgZ3aP6m0NWHvWdW2mp6sxr8FizP7EqpLlZiz1maGnKrfP01bim2shROXuQecbp32C8sMDkIbWugnkTZGFyrmNMzNjKlHMtOlCP0hzynf9wmoM2pBmctTiEMkBUhLZcMgseTlBmVl6UqrwhBZN0mO0IOuqXPmkidr_HMihgPgqKRq03Sax8OJtIkKAUXhH3xJLaTjcvQD0igPZ-MT-tGsCt-NcQ6U3DdXvmPc6sd3KS8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/Futball180TV/105557" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d903ez6eTC5DYuyDCI8NwotSOJepmJHH88cF4PqffM00OnyPqg8JUDEGEgtrnjPOOl4BHGzsmry-aQYEik4jnrOGEZj3YaGZMmh1uE3PBbtJRlbf7KEBFM7F85ZLmN0l24PvI73bvnvXvrZA-YaNq-v0DmzBhZ-qwo_GrM-gGcQk9_-pDDOciMfSCvGlT-5nVB42K_PX9_XAkDuToemc8QLcEn3e6kyv1qkViPxr3KS0xKlP3qVncs3DZnIOkwcug2WokFuD8VAG2WKKVUTdwLSLXc83um8zH0G2-OTYKNIKMSRHB6Ts9uyg_GRe3j-RdnlOH7SwXW7C-gR24fxHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وسط ریدمان رئال‌مادرید گویا باید از اونور یه فکری به حال پاری‌سن‌ژرمن فلک زده بشه. سه تا بازی کردن دوتاشو مساوی گرفتن امشبم باختن! گویا اثرات جذب فران تورس داره خودش نشون میده
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/105556" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK4qCPo0fEDiDojnXbe6W6CjRQWMM_zMFov66Pu-k19TV2juFPv2bWkzfXgyjXGYaLR0Je3AZdHgIVPqfPlV2pusuTuI0zE9C285Ly_vjB35HSP68ctcAkg0EJ5u07EU2LHnDjJf-ViZwR5K8uVv6ueqxEuHRroC5bUumB3op2VeTGh5j_Nvy11vNfSQoP2YvRdCW0ASgCEK3tzplgRY0wQuKYv0GH5Af9NxU6q5aYFp19X0IBFsfX6ePo8R9Canbn94M3GOVCJHjiQniTczqKr_I-yUww0cMlEl-dmUx9Vd_g9Wx_d3Bgo8FFeaqVxslBRyMTSVDRjFN0alS_J7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/105555" target="_blank">📅 01:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🧕
البته گویا این صحنه هم آفساید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/105554" target="_blank">📅 00:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoUbWy_2lcFInXNkCM_LOuKq6xp8F-z8ADnGaFmc7ak0tTJGoHIyWaK8uj87XraP4aaMJmXQwOBwDTO7Agz5b6puosyUhpykvAOcXk-h-Z68ifkvtBlg0xr4liuiOb74DFwhUCnQQtYvIEubrwpulvwm6B0u7gyP1YGZU3i-8ms8fRU5e7jAIjQWcHRiN-0Fp-s3TUhVO9PQz82h2YAdYjdMzlQw1mNHoQOJdFNIuinhYbByhr_u9o0lRceGjj7BbkcnHMdaBl25YACBcLGxaUMBr4V1-dnjDU4_QneA5i4cofr5Dj4Y-_AbcSoABTsuVJnm7w1UHLLQcQ7kD9piBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🇪🇸
رئال مادرید در پنج فصل متوالی در لیگ، نتوانسته مقابل بتیس به پیروزی برسد [سه تساوی و دو باخت].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/105553" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWnk3ZaFMNxm79v8m55qI0_cvvj_zVJSrnW3J0x7MHPxQSRhN67rUIWBDqm4VYZSdetN9amGkkWD-RIdRWPCFBPcuLmrpNNu0Q_psuupLu993ZyNcypXwBh0U1-84-uX2IQCk_ESTXyHCQiAeZ4FWd0t3oGntVZmB8r7nHNmoIORi1Toz7tYy-dTSPx5IN-52T1U0anSh7Lv5s1iaQ_EDGHPIloCSZNJ93_ExrdeOQh72bFULRxlej02z95V4sdP2ieX2dLONk8ePSQc9fGh_8Pv6anmNTGD_XMh5aILQB5rfLTPrWUPSzu-VNUjBqL__Zi3OpZ1RcGM1euSQhCBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105552" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdSSoMXBj1HAmK0d_KGXdKtizDqAHXsdwcnoGlhLdny1G4VQeH3_zbpFXrxA4EEDFr0wCjn2zllWug8QC-v7dm6XyvzFflvdekda23cnkwe0hInMRq0Tsk8MvHqV4h2uixba2SPkh2Y48CbewtXkIxe7OXmZRcMD1mXRwQ9I1cKoGQcM1CxOsGKqWhkvPj7Sd5ENPfRQx_Cp5fymwnREgYdzmBLQrCuK3qcTsDAfVs5z0xqqGzU-wF722M0LDtldLTiBq4nNgzox85rljAR9RLQSYbLjVCT-SJD4UDhY1s90NYAChcgi6TKA4QL5YBoLWm0aMad62rMOpPIyd2fHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105551" target="_blank">📅 00:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105550" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE6jfLixIJt-yaneNJOWSXNSiZgDjKiOTCkrN80xcavxW7RjBjdRR8wEVz7YWLatU9DC-nldIFcbMx7ovJzENK153dzNq9ihWgjPsdOFkZC5yJwNshgGnbDwPVXvbegT46DJljEjmWga1vJ_-_fV0IkkRPEmTQxzDDLiaEKoHLP1eN-EEVOCh5s09gVTSa0v3OPkzmkN-EjDuvzmjHC5li5B7FNPjzFP-tNZsdaQCN_Z_m9Llf8hvAy0bUf2FjIGls1spB4DBChlgm8gvEhFWeRpJq7VK9fHUpy8e0s3qpxgi0MxLuR44lyJYwYG2K1gp671RMVUGzwkmKLcskTc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105549" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رئال‌مادرید بدشانسسسسسسس
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105548" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105547">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وای خداااااااا چه شبی شده
😂
😂
😂
😭
🔥</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105547" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105546">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
امباپه ریددددددددد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105546" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105545">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بدلیل خطا روی وینیسیوس
😐
😐
😐
😳
😳
😳</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105545" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105544">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برای رئال
😐
😐
😐
😐
😂
😂
😐
😂
😐
😂
😐
😂
😐</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105544" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105543">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پنالتییییییی</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105543" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105542">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV-nDXJnkToX0LF1sP99Tqo7VutR6U-Z0CTDyVPsJpn2yaDgl2s9J1PMWWPcyBgCTeXjIOaxJHJSsTfoe3ng8fxyam5NNf699jxmkNFXn2SHx1AXHAVvMhytB8J3WRJwl4zQSCt26C0jq7CN1bqJFXcoLb7X01u_pfg1t9XD_1xB3piu_1kSkL9V_JYLebhf-PH4Gp155a4USFjTmVoQmjfOn-haJ7p3EnmiFKzvFbai99Duqg246saCHckISl-supO-4TWGUSUXjg0HUrPAxjY2lKackuXJqyZy20Jh5iYhVS3GiBRI7yYm9PumSOqrKo6Vc_et9bSe4OtbS7oMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آفساید ببینید و برینید
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105542" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105541" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IFkEytNs1wvGrW_mzSPxlfZyhI5B6zJ1Sut1lk8p1Csemy8d9Qg5r-cub85pOkM__Ue7nVl6MkB31OFiBpLfX8qzZ0ZSvuVYsc92CXTeqKG_YbUxjelLQ7JQkxDxUMxJRywbnHE6nDgYAZC583oxGL4jI4KskQSH0rgfoSBGowi6zylOoBIIT1bHpE5Dxl9rb2Kvg3rcFyCFI-E2_RTupq8H5YcGWnO4haKe-Uj0nxlvyLxSZAQWH-bRq3bbXBMxT5vb4ETVQ_H5ScZL-Ud-7IF2qVlkpth-lab9kZarJ6fELkbk7LhW2CAvhYUM0VsmaSSX1MAeD3aju1xb4FfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید اسپییییییییی گرفته شددددد ریدم حاجی چه صحنه‌ای
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105540" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105539" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105538" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اوه صحنه رفته وار</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105537" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسپی نگو سوپر بگوووو
😐
😐
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105536" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رئال کامبک میزنههههههه ببینیم یا نهههههههه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105535" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">چه گلییییییی زدددددددد</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105534" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پشماممممممممممممم</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105533" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سووووووپرگل اسپییبییبببببب</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105532" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگاگا</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105531" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئال تیرررررر زددددد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105530" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105529">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105529" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105528">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسپی برای رئال‌مادرید اومد که گل بزنه
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105528" target="_blank">📅 00:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105527">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رئااااااال ریددددددددددددد
😂
😂
😂</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105527" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105526">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بتییییییس زددددددددددددد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105526" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105525">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگگلگلگلگلگلگگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105525" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105524">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92b13a9911.mp4?token=OU_AOacAp92zEqmdFbx0_co8ydmlv05Om4PJVllLZOswtE8CQlxmS03pe7_DlGeFEBDr5n7CLHA0rzhnj7mMIJTWRlM7UNP_CbEodKyO5efOVcDBzydb-56BiNKHBTbzZ-sWEtmXxoA5OjPqlNAQBPcYeigBDMt9uNTW5aIlvrNEw9HA3xhzqK-CzHJ_ilf5kP87bE2e1vO8ywljHHy6Izb4-g-37_w9WtET-OCo_xaLd8_o9-ehspXpTlxlTo590PaeTvVPK5L_co8GYThpyQd2VpI5BVSTb0XBVcSXZpIYZJHsdKMEsQ_XG7GEtevn0BrP_UPP7fhofipnkhLkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92b13a9911.mp4?token=OU_AOacAp92zEqmdFbx0_co8ydmlv05Om4PJVllLZOswtE8CQlxmS03pe7_DlGeFEBDr5n7CLHA0rzhnj7mMIJTWRlM7UNP_CbEodKyO5efOVcDBzydb-56BiNKHBTbzZ-sWEtmXxoA5OjPqlNAQBPcYeigBDMt9uNTW5aIlvrNEw9HA3xhzqK-CzHJ_ilf5kP87bE2e1vO8ywljHHy6Izb4-g-37_w9WtET-OCo_xaLd8_o9-ehspXpTlxlTo590PaeTvVPK5L_co8GYThpyQd2VpI5BVSTb0XBVcSXZpIYZJHsdKMEsQ_XG7GEtevn0BrP_UPP7fhofipnkhLkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇫🇷
گل‌دوم موناکو به پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105524" target="_blank">📅 00:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105523">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=tPnUDMcO9eNYilTtpt-FH35gF8ZQ2355GHJqwoPHnEqZRjrB4whPtkLBrMqv2juShO95kKKuA2L-tEN1Ulc2ZiP2lyYlu3T2BAMyNInQaxxNGe86bYexSLiQNvLKksN4SDPjuxcSMJ9Y2v1zORwvpwCjKgzD5AEV5yaCfyONbD3rmFhqwruhaFIs1Y-HPJS8WZPBfhKpXpfrJZfv12ZXza4XznyzhaoT0_YhsohF7s82XKOMb0kE29HwdMPHFb_md66NXX2hfGqKYAMVmyAqkXSMJAbDFfXX5uLXYaXO3_r7ekab4cA_XpJhHF94eRMzEzWN9o_xG0MAY4qUfUrYEj5ME20v6Ws2223z-NtBYtH0CU4u4MltCZ5iLUPMfe4uBxw7pQ7D_p6DmQTAhNXLs4pSh5LiWMoacrdlKmgzFMR-C7kid03P0YXuX9shnLji7vZTEE-Pctz9lLc0NVxa03xHW83ymOjecTLXfghYnjcHfZWMhi6JLuGcnYJmuBVn1UpW8z-So17YLaWhY2J0EtWx8uToaGquic4SkorgNUCNpiNnB5oBsPuFJCRaftQ0MUAnD3UBNbC5s8rDNpQCjViolvC4CDuY-Yc1TGtKxGkPp03zKnfkSwLSdV6hGAdxLiEtGGoIPD3jHO8fGQGiNtU1gTmkUofrgndPITh5A9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=tPnUDMcO9eNYilTtpt-FH35gF8ZQ2355GHJqwoPHnEqZRjrB4whPtkLBrMqv2juShO95kKKuA2L-tEN1Ulc2ZiP2lyYlu3T2BAMyNInQaxxNGe86bYexSLiQNvLKksN4SDPjuxcSMJ9Y2v1zORwvpwCjKgzD5AEV5yaCfyONbD3rmFhqwruhaFIs1Y-HPJS8WZPBfhKpXpfrJZfv12ZXza4XznyzhaoT0_YhsohF7s82XKOMb0kE29HwdMPHFb_md66NXX2hfGqKYAMVmyAqkXSMJAbDFfXX5uLXYaXO3_r7ekab4cA_XpJhHF94eRMzEzWN9o_xG0MAY4qUfUrYEj5ME20v6Ws2223z-NtBYtH0CU4u4MltCZ5iLUPMfe4uBxw7pQ7D_p6DmQTAhNXLs4pSh5LiWMoacrdlKmgzFMR-C7kid03P0YXuX9shnLji7vZTEE-Pctz9lLc0NVxa03xHW83ymOjecTLXfghYnjcHfZWMhi6JLuGcnYJmuBVn1UpW8z-So17YLaWhY2J0EtWx8uToaGquic4SkorgNUCNpiNnB5oBsPuFJCRaftQ0MUAnD3UBNbC5s8rDNpQCjViolvC4CDuY-Yc1TGtKxGkPp03zKnfkSwLSdV6hGAdxLiEtGGoIPD3jHO8fGQGiNtU1gTmkUofrgndPITh5A9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
مهدی توتونچی: کاش به جای علیپور، کنعانی به مانیکور می رفت!
🎙
وحید فاضلی مربی پرسپولیس: ناخن های کنعانی را مثبت می‌بینم یعنی او تمرکزش کاملا روی دربی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105523" target="_blank">📅 00:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105522">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=JkBgA4uXutBEfhf_ZwcIJxb68Fc9YMD9CPZ_slP46_tzKCpuga26nbn7eF_Z-esWLuybPFWe_x55h_Sc4B9_HynuBtzvk9bacPZ54jfo2uyHDsMqlPPpA0uKeiTOgp6fg-JSgazWVROKGCONmgS9fDh1bxoImBFmDhDFr5ZCWo_0Jfc2wkJwo6p-GTIxEEZqrAus4-UBn8Ijtc-IN7eDGCdGOO3e1Fy_BAucR9wbZxxNuX8NKhp5Dg5jCrGfaPLcHv9yIqW9t9tLUmAF1I6k43-zwnjlbystbMJV53dndWWmJLDQUSV5Wkh7XzDw3-Vvs2rdZn3Q0ENn3GckvA036g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=JkBgA4uXutBEfhf_ZwcIJxb68Fc9YMD9CPZ_slP46_tzKCpuga26nbn7eF_Z-esWLuybPFWe_x55h_Sc4B9_HynuBtzvk9bacPZ54jfo2uyHDsMqlPPpA0uKeiTOgp6fg-JSgazWVROKGCONmgS9fDh1bxoImBFmDhDFr5ZCWo_0Jfc2wkJwo6p-GTIxEEZqrAus4-UBn8Ijtc-IN7eDGCdGOO3e1Fy_BAucR9wbZxxNuX8NKhp5Dg5jCrGfaPLcHv9yIqW9t9tLUmAF1I6k43-zwnjlbystbMJV53dndWWmJLDQUSV5Wkh7XzDw3-Vvs2rdZn3Q0ENn3GckvA036g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📰
🚨
📊
آنالیز دربی پایتخت توسط محمد تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/105522" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105521">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e16c038f7.mp4?token=Nx6B0KsufeMBBCnDwgFG2XfgVomIlqcDHWvFVqRlLdErDewDsymMPeekcB9QiKvs5ctLTsacxqLl7AanWjQkgziXZ5rJxzT_iaqINPoVlGFPtNbTc2NiSj33iWWOXOntb8HtmpJQYjTMWRDcuWBeeneZD0LtQzu3IVhrOC8QbBN48nVPDK7yNx4yu8iZmV2j2U52FML8EAEPP8tF1ckOB89CMAU7n9rLdUVSoSe1vYJ-ngTLMpoHWKS9KLtekn0RaBrC2WQc1oZJEQCq7JIFz1IQrzsMiZ94CoUy-CiNJ3tyOZQmwmUchPFi8iWUgHISz1x50W_TLbnEXPCy0nHXdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e16c038f7.mp4?token=Nx6B0KsufeMBBCnDwgFG2XfgVomIlqcDHWvFVqRlLdErDewDsymMPeekcB9QiKvs5ctLTsacxqLl7AanWjQkgziXZ5rJxzT_iaqINPoVlGFPtNbTc2NiSj33iWWOXOntb8HtmpJQYjTMWRDcuWBeeneZD0LtQzu3IVhrOC8QbBN48nVPDK7yNx4yu8iZmV2j2U52FML8EAEPP8tF1ckOB89CMAU7n9rLdUVSoSe1vYJ-ngTLMpoHWKS9KLtekn0RaBrC2WQc1oZJEQCq7JIFz1IQrzsMiZ94CoUy-CiNJ3tyOZQmwmUchPFi8iWUgHISz1x50W_TLbnEXPCy0nHXdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاری‌سن‌ژرمن بازم گل خورد اینبار از موناکو
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105521" target="_blank">📅 23:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105520">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZAXQFhnRtVMKnYbSTukeUHB1bIdddSM3TqdaskqFzggfVhZOtZD15blLiFe9gmbsYAg2efz0joncVGGVbfkKzTrpW5XC2bJuwlcg7jj-WwfduoHxDIdEX0gCx1EYRWTb-M61Iy-nT3AIQfhIQ6OXNN6qxNtJGs2zrvx-UF8QoJcfo0Ka8SomovcMoaChwx4oRLfw6VvYqLl07UAatW0h2BgZiSN-wvfrsbvRQS_J-2OG6YFEA8obVQC9hQ7LoREiCjvVe5nRXHwBd-u0NQjCStmCpepVyYtNYqN0ZSJi5deUiotRniNaE9RuKay8phveLBzZg_9p8HPtIs6XYrsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
برخلاف شایعه ساعات اخیر، عارف‌‌آقاسی مدافع استقلال دچار هیچگونه مصدومیتی نیست و در بازی با آلومینیوم به میدان خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105520" target="_blank">📅 23:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105519">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDSmCoIn7FJlwCx9EKlynMCQ29_HdmrWAUFfBL_EVCRhgHr2fRLkXBVzSvqxsVnruN5tTE-x1prg_eDf2VOAl3BN0PQbfffNZxvj6svRfiWr4Lp_0ea5N_gypAyFCcChVKhzhLmoMVieDrkcBeKdBukEB6IWhBwC4Sd85VUzgk8JW_2lG3Xn2w3APrKx_io_2Bx74EAeMJA9bNZmuGfDKDn-2qSegoPCBAPtMjUpRyvxmFuikMv-NYPZt4YNlhRpAMeRow088SEpJCyibKHvZ-_I3KnCV3tMW3HQ9HZZVEmECLHfFK7Q6_hw_SL-kRZxi2Ayqk0lLLUig8UwvsdchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
استوری یاسر‌آسانی برای صالح‌حردانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105519" target="_blank">📅 23:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105518">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1298395760.mp4?token=X_xvbtCLGaNLKd0t1Q6mMECaaoz_eRDegQjJrocKsd82CyZw4R1ap0vdnaPFZp6-kR9QStK-V-2xkQ23kaML1hil4VVreJgki_fUL3u61FxQWRGpKdfjNRFu_un1Kedz-yOtsnfb6DOGaWSoWixs38c3vU3YKkfkuVALPVfD0wU6_IiJQGcPKsguL6e-VKgs2P7-6u7R_2brNah_lHh1fCfxMjbrFLCvqbzIzR0mpGXzemI6puKmc_vhbZXPxZLHU7WL01T3vgdTsj521dC05blkQ2je9UGPT6k4ZaihfQMV8rn5tW22PcSYhnsAbrXg1mwtPZwJk1wMEi8UQRoRrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1298395760.mp4?token=X_xvbtCLGaNLKd0t1Q6mMECaaoz_eRDegQjJrocKsd82CyZw4R1ap0vdnaPFZp6-kR9QStK-V-2xkQ23kaML1hil4VVreJgki_fUL3u61FxQWRGpKdfjNRFu_un1Kedz-yOtsnfb6DOGaWSoWixs38c3vU3YKkfkuVALPVfD0wU6_IiJQGcPKsguL6e-VKgs2P7-6u7R_2brNah_lHh1fCfxMjbrFLCvqbzIzR0mpGXzemI6puKmc_vhbZXPxZLHU7WL01T3vgdTsj521dC05blkQ2je9UGPT6k4ZaihfQMV8rn5tW22PcSYhnsAbrXg1mwtPZwJk1wMEi8UQRoRrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
آنالیز زوج سمت راست استقلال در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105518" target="_blank">📅 22:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105517">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2xS-C2S3N2f2DJv0fU9vmagjRYCs8hMtdX6K5f7QMwd6_sViWYETAgOrQS4zFYWwjwaGe9jDWfyrWF-YR4U1IQAbKAD78Vq4Y0Evti5SimMda5G8o8CZquIDH20CYweeyPHbKY9GCvUJMNjbVE4I-w22JADlVPgyIcyH-DaSnl6yJ9tVZwCuOQrqehi56SnLUHESyl1lQZ8xupG3TXyrUlHiYWuWqQ3Vw1D0OjsaOBuUJAXmy6Pv8ok28zVe_3uLH4kym8mGLVQ_OAfXoNZysmsjA_qFDF4WTuv8ZFwwKfHqTw0BPHXp2yxkUHxBgGHBm2eOUP7hvZHbqzaO40D4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قرارداد چند نفر از اعضای تیمش از جمله لوئیز انریکه و ژائو‌نوس را تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105517" target="_blank">📅 22:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105516">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0b4fd3a2.mp4?token=JwogUXpU7XYSqGEDqAjEU-WqwtEdiBcsm2hmz_2312hcQjTYz7Una8wXYvSCVTJscjMJmdJRClv6rKe1q0ixuU21GzkHB5aDQ8Mq-UQRRmSydalYAZYLxyuMd2sM8nQnZdtNgponwHJ3bckLIFt_nhLw7I6VWCXDaDvbyFcWIJjUGom-SE1X0Z4X8Z3BlSdoGlS4WdTzBR1SiQ6YZPhYBVZzyE2ERoEXqzE5LZjJMWu1vmrNcTAHlBCEeyxdNd-LtDsGvhj_ulJ6asFw8wUsYiig1cruN8Zka7SPJqxOb1qAB7Q-CuA63V0T-TdSuZtrBKXCjbxLq8PST97spNDu_HoHywBLpPWOdNhFvholN-TorTj2DCf_Qk-D6YPr7y8p-9fPH03Cj8-aKuNyLsjZkJVENzQMig4K0tnsLSBLJAzGqvUhpuh81rCc0yd_Wku1cLe5aU3tTWxN66SkjviSYeVVGb61Qg1Pt3nxKNbkAld_amPhuaV-xBPSYHiIJZW9teAviUIXaV2zaYXXy9lA8M41FewDSgAUbp3vLY0cPk_jkSn0YukvoLNCFQ6leq1710MWbgsBtBs2NZiZJquxfaoRcs4j1ttcsNz8lXu0LnBlUZTpoHiCaP9zStK0by0K-7Md96DFWGkOVG7AbL1XbXriWMVJu2X9VFKW_MgBoLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0b4fd3a2.mp4?token=JwogUXpU7XYSqGEDqAjEU-WqwtEdiBcsm2hmz_2312hcQjTYz7Una8wXYvSCVTJscjMJmdJRClv6rKe1q0ixuU21GzkHB5aDQ8Mq-UQRRmSydalYAZYLxyuMd2sM8nQnZdtNgponwHJ3bckLIFt_nhLw7I6VWCXDaDvbyFcWIJjUGom-SE1X0Z4X8Z3BlSdoGlS4WdTzBR1SiQ6YZPhYBVZzyE2ERoEXqzE5LZjJMWu1vmrNcTAHlBCEeyxdNd-LtDsGvhj_ulJ6asFw8wUsYiig1cruN8Zka7SPJqxOb1qAB7Q-CuA63V0T-TdSuZtrBKXCjbxLq8PST97spNDu_HoHywBLpPWOdNhFvholN-TorTj2DCf_Qk-D6YPr7y8p-9fPH03Cj8-aKuNyLsjZkJVENzQMig4K0tnsLSBLJAzGqvUhpuh81rCc0yd_Wku1cLe5aU3tTWxN66SkjviSYeVVGb61Qg1Pt3nxKNbkAld_amPhuaV-xBPSYHiIJZW9teAviUIXaV2zaYXXy9lA8M41FewDSgAUbp3vLY0cPk_jkSn0YukvoLNCFQ6leq1710MWbgsBtBs2NZiZJquxfaoRcs4j1ttcsNz8lXu0LnBlUZTpoHiCaP9zStK0by0K-7Md96DFWGkOVG7AbL1XbXriWMVJu2X9VFKW_MgBoLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هوشنگ نصیرزاده: هیچ‌کس نمی‌تونه از آسانی شکایت کنه؛ افسوس از این اعتراض‌های آماتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105516" target="_blank">📅 22:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf94f3a1ca.mp4?token=GbNz7HjSQH2a0NOi79wqh1qC6lKWdOw7JsLqG3etEGJU2sZoAeNnxRIqYardZToOpDpzPOkDtb9P5NGeqnIaN-4XGgPwOG7E5bkdN5dkePx33R1i8EYlXiYbaUzd_ujFU-F_5MGu9z95sHwmGCwD-gBtRPTlCr3cu4zirDxV9KldWeUe-g4j9kWXiAnOdwLOaBgAtknTOFnEBbgRN0oRn5Xrx7FRF7lvK3o8yDwep0kBAbb8RKkRVbEQgAji6ExruR8z-n4Sivx0ol_-FR3wXCOXPvzvYmnEQmlerKxmrGYEWN0mA82cLNjEUqgWUf-6yQZlknOHgpG9Lrj6dvkK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf94f3a1ca.mp4?token=GbNz7HjSQH2a0NOi79wqh1qC6lKWdOw7JsLqG3etEGJU2sZoAeNnxRIqYardZToOpDpzPOkDtb9P5NGeqnIaN-4XGgPwOG7E5bkdN5dkePx33R1i8EYlXiYbaUzd_ujFU-F_5MGu9z95sHwmGCwD-gBtRPTlCr3cu4zirDxV9KldWeUe-g4j9kWXiAnOdwLOaBgAtknTOFnEBbgRN0oRn5Xrx7FRF7lvK3o8yDwep0kBAbb8RKkRVbEQgAji6ExruR8z-n4Sivx0ol_-FR3wXCOXPvzvYmnEQmlerKxmrGYEWN0mA82cLNjEUqgWUf-6yQZlknOHgpG9Lrj6dvkK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی محسن خلیلی از حاشیه‌سازی هواداران پرسپولیس درباره اوستون اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105515" target="_blank">📅 21:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bknK205Hewa9fRHH3GcAqpaZ7ANF95n4nCWnvEauKveHQtIvYPXqZTVLmzppATGwH8JOmXlzntpm7WAqajnuFSPtHWx2fB3I57fyDvJudcbkVyn7Utye8T3kz1serjDQ1FDj_CkJXBYC2aIxecb_dyMj8Clq0ZGbcenm7ruqw_5fkUhQEjOvhZQHTW6QvrwJUpnHd46alnb1uRJBl0rC8h0XXi9aRaf-fjcTfxUN_lNtBt54ZVDb2nDGtLZB15SDN6Tt4o6FMj8N9StEbW7onBfle2a5xODmwceIbMt-7cSH34gefUyUh6JGsgm_eNFi6wd3RYfGanjSL4Tp0t2nYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
ترکیب رئال‌مادرید مقابل بتیس؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105514" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b668e9a164.mp4?token=fDNym-7j7iGCsOfwj65MRc4CuS6WatitAT0-wp25vgK2Msr47M7hUJp6pmN2C2pSs_Jz2wD6l5KWjXAbHQt0QUbpJ4_XKr9jqzKXmyVvBugbqZuK5udxTddh_-aMiPTaDDboj7Zy6-L4swrC7xkAL8-jHF99pmwwVndUuov_kjKH92way80_LeZLA_OBpowhDOjUuMe24gw1_COFalqeFJ3Ny2NSyP828ZWOUk7QavnLaVzWFVxkVtou7RtxJuvvBCfTy3SxjQtBZsgi3v7hDGAB1hoUaJ7wIwYtcWzwgUNlV9j_6loPA2ETqkp1bbCX4FJfwAINrcfyxcgkjcJ-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b668e9a164.mp4?token=fDNym-7j7iGCsOfwj65MRc4CuS6WatitAT0-wp25vgK2Msr47M7hUJp6pmN2C2pSs_Jz2wD6l5KWjXAbHQt0QUbpJ4_XKr9jqzKXmyVvBugbqZuK5udxTddh_-aMiPTaDDboj7Zy6-L4swrC7xkAL8-jHF99pmwwVndUuov_kjKH92way80_LeZLA_OBpowhDOjUuMe24gw1_COFalqeFJ3Ny2NSyP828ZWOUk7QavnLaVzWFVxkVtou7RtxJuvvBCfTy3SxjQtBZsgi3v7hDGAB1hoUaJ7wIwYtcWzwgUNlV9j_6loPA2ETqkp1bbCX4FJfwAINrcfyxcgkjcJ-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان چالش
🎀
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105513" target="_blank">📅 21:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=ToCNVxYOHXbpDJ11_ZlWoH4BmUP8YvMeJXcP49nNGRC6sn50GmLTVFIINmFxPGWzbXxowfsNtAN1BAcciAMr5In5bPshlGYmUJXFEXG0dpmQhEpExUFJLfHO2rHcVFwQBgWWNEWkzIO9JJxfAieeH40cfQcsEgC6smkYxL6AZah-bEsExtd7Ec5EKmecajMZrZARNp9CNbPREC_Zz_EW6-dkJlGdxBLG5AkRDHhYHffcERLWzVKvjG5joR2UBYmodz4T4Y8vKNHe7FwkJZXsEZEwa-QNACTcDY7Mc6zLpDKbEeIJPYa0NdOnckRUOgmLVId1dJnqi7ttju4OZABf9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=ToCNVxYOHXbpDJ11_ZlWoH4BmUP8YvMeJXcP49nNGRC6sn50GmLTVFIINmFxPGWzbXxowfsNtAN1BAcciAMr5In5bPshlGYmUJXFEXG0dpmQhEpExUFJLfHO2rHcVFwQBgWWNEWkzIO9JJxfAieeH40cfQcsEgC6smkYxL6AZah-bEsExtd7Ec5EKmecajMZrZARNp9CNbPREC_Zz_EW6-dkJlGdxBLG5AkRDHhYHffcERLWzVKvjG5joR2UBYmodz4T4Y8vKNHe7FwkJZXsEZEwa-QNACTcDY7Mc6zLpDKbEeIJPYa0NdOnckRUOgmLVId1dJnqi7ttju4OZABf9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
🇮🇷
یاسر همرنگ داور سابق فوتبال:
❌
با یک عکس نمی‌توان راجع به دادن کارت قرمز قضاوت کرد. تنها ایراد وارده به بنیادی‌فر چک نکردن ناخن بازیکن است. داور VAR زمانی داور را می‌تواند صدا کند که یک صحنه‌ای از عمل «وحشیانه» بازیکن موجود باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105512" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=Ucb9yrQkQfBCPoyay72_t5pHs5zslPYi_gBEpZTGBpG0rlOZnTM-MOrtWxcEEY3JJVSw56IqF1Yki1t5k1RAUCCmSmdMT79s74iftnLH72c1fAGjdEluCE8z79ZBHwjK9cVw3JIi7LJR1hFaNR6HfgC2XpNDT6iLFqgeRFqcueMhIhTWxrbwTBgq1iBkPDE4Pxg6P1bMpsVSWTLPF0ICYinl5DnCxHXLPNClgTotZFaDmH_AU5LoS6fgfkLHDc91L034rl2PisxiX-fZJqBarPZGwQmBwfSy2tvkCH1S_A982h45U-tj-AGJinGQcRdfa1rzr3rpquHC6Nv9HS_4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=Ucb9yrQkQfBCPoyay72_t5pHs5zslPYi_gBEpZTGBpG0rlOZnTM-MOrtWxcEEY3JJVSw56IqF1Yki1t5k1RAUCCmSmdMT79s74iftnLH72c1fAGjdEluCE8z79ZBHwjK9cVw3JIi7LJR1hFaNR6HfgC2XpNDT6iLFqgeRFqcueMhIhTWxrbwTBgq1iBkPDE4Pxg6P1bMpsVSWTLPF0ICYinl5DnCxHXLPNClgTotZFaDmH_AU5LoS6fgfkLHDc91L034rl2PisxiX-fZJqBarPZGwQmBwfSy2tvkCH1S_A982h45U-tj-AGJinGQcRdfa1rzr3rpquHC6Nv9HS_4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
⚠️
جلالی: هنوز هم سر حرفم هستم؛ قلعه‌نویی در اروپا بود، از مورینیو بهتر می شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105511" target="_blank">📅 20:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=To8z_nHBVqD6ZQaDcHwysKELZeqAXMguxxN5u7yNxGhez2zhIXQZXuK920MCZ_8qFxNLEDVtURPDKuXvlTvjPxPeOFkNZpCjo8k8JdxGJr0iBxmQuiEI0VP6atLQUb3M4dROaFqdDwYP2Q2eqfIhMMd64S18AZmCqurAg1Qp8dTfolwGDqaiOkAg92jj_d3jLMZrnlHOStRGuyD8P8-4hjNmkxsBY1pLQtYL828zSMwrheyG4QyIdLzYrXKyTcqWAOxnAMe32dWRj2zfjTOU92ruTT2WslP31K6jqPnTDTe7XM1Ioua5Aox8fWCCaJdHP5S7Uf8w1BHR-xCr5-6QFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=To8z_nHBVqD6ZQaDcHwysKELZeqAXMguxxN5u7yNxGhez2zhIXQZXuK920MCZ_8qFxNLEDVtURPDKuXvlTvjPxPeOFkNZpCjo8k8JdxGJr0iBxmQuiEI0VP6atLQUb3M4dROaFqdDwYP2Q2eqfIhMMd64S18AZmCqurAg1Qp8dTfolwGDqaiOkAg92jj_d3jLMZrnlHOStRGuyD8P8-4hjNmkxsBY1pLQtYL828zSMwrheyG4QyIdLzYrXKyTcqWAOxnAMe32dWRj2zfjTOU92ruTT2WslP31K6jqPnTDTe7XM1Ioua5Aox8fWCCaJdHP5S7Uf8w1BHR-xCr5-6QFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
نصیرزاده مدیرعامل سابق تراکتور: بیرانوند در صورت سربازی باید به لیگ یک برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105510" target="_blank">📅 19:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=Z4UvvD8guqivj20CO7Ct-H8mIE_x32BkpwPtskKuKMO6hG38e4f2RFuMAnV8w2bzZ0oeCRS2qrlRoxVXcDvAEDr6BdDQMKNWHLvmywwxA8eVBTvcbupafobihK9O8wXe6EM_UrwGHBsQ-BoSI7C6CtZuY5jFmP4q7tz7NAul4tDdRDwKaMi81v39YG9QT3K9cvs7Ii9KB8SS9Gh6tOl0h9gyCGNaZt3Ew4Uz_XJuhi2srtB10weIVw1lU-fU4E7QExfpsGK8f5eUQ_HZvbDxTELKQ5QM3byjEQHX3HigGP7X1wXoCew-vwatsUIcyz73e7Ba0wDt1IaTneA_B884iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=Z4UvvD8guqivj20CO7Ct-H8mIE_x32BkpwPtskKuKMO6hG38e4f2RFuMAnV8w2bzZ0oeCRS2qrlRoxVXcDvAEDr6BdDQMKNWHLvmywwxA8eVBTvcbupafobihK9O8wXe6EM_UrwGHBsQ-BoSI7C6CtZuY5jFmP4q7tz7NAul4tDdRDwKaMi81v39YG9QT3K9cvs7Ii9KB8SS9Gh6tOl0h9gyCGNaZt3Ew4Uz_XJuhi2srtB10weIVw1lU-fU4E7QExfpsGK8f5eUQ_HZvbDxTELKQ5QM3byjEQHX3HigGP7X1wXoCew-vwatsUIcyz73e7Ba0wDt1IaTneA_B884iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
آنالیز گل‌های دربی اخیر پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105509" target="_blank">📅 19:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
⚠️
رضا قیطاسی تو مسابقات طناب‌کشی بازی‌های جهانی عشایری موفق به کسب مدال نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105508" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=fpzRgYmKT9jneVGNxkiJmdFCvZugWwz65EEW3vRYrORnWTks-3MujZuh93MAZjsX3hTJ9C6kfJMlG4lnaxIxS3m8LWVEK0ZRE8tt3Sj4YpCzdaooZoI88ZSUqH9YOvDtd3FJyiD1q6jcCrEvkpVr6Ciy35bDmvv-VKSXT_YaYRN7btJvzkyjH1ANLjBSCH4b1SlAE5l6Gmg5KelbBqb6IRKZ98Z4tdTj3vcNg5wOSwd2SnqbrvvC4DR8a_Jbc5-xTKekmPeRAsfhlmfywrsIPuzI6_k2mit77M_MaHHdhB6yoiG_OQri4o3pwpectznyLfcDClr0slbm2CMHDAp8jaMT1LROF9_RbOK66V0uUvO0SXx1ueIrVsO1AMAir3HL7hTAlCXEGEdXwMMnF6RUAdPmeQe0kXvq_c5hvfkYYpbWYSyjsbFvGUO2Ei1s0EoBUGQUUvET8ooSYFY5ZRfOgtP6C42GLY7sNOB9n214LAnq1ZuPr5y_uXCNA0z74Q4LNzkEHNya0M_A1hnzAbHD55n2sXVIU8Bw-QJ4jzvCbAS41sN5ZUk3GUGnvWrz-iDhsCDoMWX4IDxFMW8cv8Dy_puBt4BCBoFMmSCrrNOJHgegw6XAh2qHmzm_9v7JWoRyKj0kFfFAo72Qn5HxW3FiI0pZjcpUWSMdfL7-AnzUSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=fpzRgYmKT9jneVGNxkiJmdFCvZugWwz65EEW3vRYrORnWTks-3MujZuh93MAZjsX3hTJ9C6kfJMlG4lnaxIxS3m8LWVEK0ZRE8tt3Sj4YpCzdaooZoI88ZSUqH9YOvDtd3FJyiD1q6jcCrEvkpVr6Ciy35bDmvv-VKSXT_YaYRN7btJvzkyjH1ANLjBSCH4b1SlAE5l6Gmg5KelbBqb6IRKZ98Z4tdTj3vcNg5wOSwd2SnqbrvvC4DR8a_Jbc5-xTKekmPeRAsfhlmfywrsIPuzI6_k2mit77M_MaHHdhB6yoiG_OQri4o3pwpectznyLfcDClr0slbm2CMHDAp8jaMT1LROF9_RbOK66V0uUvO0SXx1ueIrVsO1AMAir3HL7hTAlCXEGEdXwMMnF6RUAdPmeQe0kXvq_c5hvfkYYpbWYSyjsbFvGUO2Ei1s0EoBUGQUUvET8ooSYFY5ZRfOgtP6C42GLY7sNOB9n214LAnq1ZuPr5y_uXCNA0z74Q4LNzkEHNya0M_A1hnzAbHD55n2sXVIU8Bw-QJ4jzvCbAS41sN5ZUk3GUGnvWrz-iDhsCDoMWX4IDxFMW8cv8Dy_puBt4BCBoFMmSCrrNOJHgegw6XAh2qHmzm_9v7JWoRyKj0kFfFAo72Qn5HxW3FiI0pZjcpUWSMdfL7-AnzUSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
تلاش‌جالب یک پدر ایرانی برای گزارش دربی برای پسر روشن‌دلش که حسابی دیدنیه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105507" target="_blank">📅 18:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b357d488.mp4?token=mW9_wAoqEVhRjL_gu05ZB0S509Ibh7k1FhziIGE2KE4EoIf9SR8fCk0NZDC5pFrHi3iIz-prkP2Sa4eqGgRz49nEssoqlxw6YZFkguYIUveoCdxEJw0lkkI4KmsBmgibRXDy9M6tM8mBFus1GUH_CrDW-Ow9XRfUcw4U6jhNvXtWEf3TTT4yPRoJ4ykTWIgPxczxKgkITd99gN_amS-Zdko2hUqSoIjWOoPW1L8E4ZBrDqoi2zl2JrFbTFLV_pT4VkKmQ_F4Sdfn5HUxxSu9rBNf_hha3QcRC-b16qxEbYsOgmV2ROeLa7EkoewiFv8eJKS7xL5UQlGZWQ2P8xqRAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b357d488.mp4?token=mW9_wAoqEVhRjL_gu05ZB0S509Ibh7k1FhziIGE2KE4EoIf9SR8fCk0NZDC5pFrHi3iIz-prkP2Sa4eqGgRz49nEssoqlxw6YZFkguYIUveoCdxEJw0lkkI4KmsBmgibRXDy9M6tM8mBFus1GUH_CrDW-Ow9XRfUcw4U6jhNvXtWEf3TTT4yPRoJ4ykTWIgPxczxKgkITd99gN_amS-Zdko2hUqSoIjWOoPW1L8E4ZBrDqoi2zl2JrFbTFLV_pT4VkKmQ_F4Sdfn5HUxxSu9rBNf_hha3QcRC-b16qxEbYsOgmV2ROeLa7EkoewiFv8eJKS7xL5UQlGZWQ2P8xqRAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
افشاگری محمود فکری: خیلی از دربی‌ها رو از بالا دستور میدادن مساوی بشه و ممکنه هنوز اینکار رو بکنن
❌
نتیجه دربی رو خیلی از پشت پرده کنترل میکنن، خودم هم شاهدش بودم بارها و میدیدم به مربی ها میگفتن بازی رو مساوی تموم کنید یا به داور ها گوشزد میکردن اگه یک تیم گل زد جوری بچینید تیم مقابل هم گل بزنه یا بهش میگفتن اگه مساوی بود ریتم بازی رو بگیر تا با همین نتیجه تموم بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105506" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105505" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105505" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTkdFlDO5z6QXGJI33U8u87x-nguGGIVx-wo44tuU1lUdG0guyzZZn72iSiuhDHbaZig5PJ4rtfPb9mN3jIPUccb1cByXGCVM1aLQheZEe1oQG8KVe4dUDdQRkANU_FlNISUHg4Frjx4SRKe3GGiaT4vYKhXLFKlvR48t2YhQOJYG8dLs1Jm5ETXA1e6aIrZR8z8xDXaKK7wXNInZHGUNNrQSShWJwjpeVEXFTqnFG3pTuLjaPypN8sPy0NoP1bnhh7mJwPxkKrLxeutWslfwTmEdJ4GqhAW5mwjA68jA9XB6y3VSgGSccs8RLYDt1r3c2igPjV9rUE7njx_-JbFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105504" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHpZsHViVL3JxMlVl3G3t0gO8nseiuRBoMyR1_VrU0EcmK4kOmgV2pnQ45I8x6DCiPyjmATmKfa1Lhg_VFmdVclKlpdpcAMIks3BP1slTReUFHZly3KBjM8XGLdPBN1d8DbHNVfkDzA0DaaqZ37GpKOT4FKHbIqIkM1IX52hVILF3G12dokECphzIKWBu4j8XNwJhJWg__2faPGzJMBMQKwrTBPYO3Kwa5pP7RzW6xmcU9bkbiTs8DflhR6cvknawv3XN5dsq33VjnnHYld4PjcY62npCK7T-_pESonC8Ao0wpUFP5yH4VeUyo8YEUWUwxBRrioWK5K6WK33HlLWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار استقلال در حاشیه بازی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105503" target="_blank">📅 17:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=bI28t2a0Bh4nRwEL-0pi9LvVu2I43_BextT0GRdMk7nTMDxARJ50HOyGBjBUhQCEirxf3muHTBHMlCE0lU5tHDp-MjFoIvu0D23Fh7DSIoNMWc75ZY_qebq37dXtDVwubNPJoE8E2irsKYdf-GQlrlCZbhqTz4liPeEpjn7a5RbBf7HLMvyRN9SaxsNAPKfMyvcl03RH1-kAMl7NW4Ydg6JvHT0Z1SOm4-Q-VNbu40ZXvr89Ck7FdMBufOsKw_bnRiUrohmIO5867BtbzIWuz776iXT--2CyIqsckPq6_QLKIQMNgeDEAj70znX__r2KOx5qqNaaN4msMgis2F3dvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=bI28t2a0Bh4nRwEL-0pi9LvVu2I43_BextT0GRdMk7nTMDxARJ50HOyGBjBUhQCEirxf3muHTBHMlCE0lU5tHDp-MjFoIvu0D23Fh7DSIoNMWc75ZY_qebq37dXtDVwubNPJoE8E2irsKYdf-GQlrlCZbhqTz4liPeEpjn7a5RbBf7HLMvyRN9SaxsNAPKfMyvcl03RH1-kAMl7NW4Ydg6JvHT0Z1SOm4-Q-VNbu40ZXvr89Ck7FdMBufOsKw_bnRiUrohmIO5867BtbzIWuz776iXT--2CyIqsckPq6_QLKIQMNgeDEAj70znX__r2KOx5qqNaaN4msMgis2F3dvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚔️
🇮🇷
🇮🇷
نبرد جالب و دیدنی تیکدری و صالح حردانی در حاشیه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105502" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=ls9YYlMhRqKcLfG0wG4G5Yw0XpNoNUMC3tTgWlkWChigVzRRF805kUcXG4TzLXaQ_PPmYuEdaqucCiow_aDnUNjDOJjwfuFMyfH_4UJFQtYCAjYts7z_rWMGONKwNkxaIznvRwdFf67NAJzN4VMghs98wumls69sGIhuRP4EpY5Xk42E4WVggDBJpiqLhFjJkxc1fGd2joBbOyT0lF1rPvAP7oJsQBUEfMnTVAAb9n0TOLpBiZldY_o9b8eYQNFXB-Wny3nG8f_IvdTvgL2oWr9qONiXR0GoHdwLTkSvqm--fYXc__z4eP4UC0OC-9CE8pHqMickXGRD1oDUVMxIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=ls9YYlMhRqKcLfG0wG4G5Yw0XpNoNUMC3tTgWlkWChigVzRRF805kUcXG4TzLXaQ_PPmYuEdaqucCiow_aDnUNjDOJjwfuFMyfH_4UJFQtYCAjYts7z_rWMGONKwNkxaIznvRwdFf67NAJzN4VMghs98wumls69sGIhuRP4EpY5Xk42E4WVggDBJpiqLhFjJkxc1fGd2joBbOyT0lF1rPvAP7oJsQBUEfMnTVAAb9n0TOLpBiZldY_o9b8eYQNFXB-Wny3nG8f_IvdTvgL2oWr9qONiXR0GoHdwLTkSvqm--fYXc__z4eP4UC0OC-9CE8pHqMickXGRD1oDUVMxIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🇮🇷
علی‌تاجرنیا: خودم پیش قدم میشم و‌ مشکل بین صالح و اقا سهراب رو حل میکنم. چیز خاصی نیست. هر تصمیمی سهراب بگیره باید احترام بزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105501" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=hIWBsE4F1HG74LaJR3fZYq1_HAzABtbbr-PbjxXnfptKaDELOwPlVVjofuTNRkA4XiSkhTkm3VjsCaZzdaXIB6VQ4dQ2MtneYM6J1FzqF-I2oOsXG2W9MXrM7gnYgW4W9I6zLE_jB5CkxBKsLB4kpA4bNYkk7LMfJXzT6lxTIRvqX3Bon1UK2wR1vBhXkqWGdSOYKwCnwpJ4UkqVySHauLn43J_glRyAt3lDODu5DZgOp8e0FjWrLkBjXx4lVzrepsUUGV3lXaf5T6F4fCkWEHacc_XqauEmhXqBSzKVxa6xYwKB-xAE3pqVz_MnRqEjLJIgViIW6OS2yQf-e_S7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=hIWBsE4F1HG74LaJR3fZYq1_HAzABtbbr-PbjxXnfptKaDELOwPlVVjofuTNRkA4XiSkhTkm3VjsCaZzdaXIB6VQ4dQ2MtneYM6J1FzqF-I2oOsXG2W9MXrM7gnYgW4W9I6zLE_jB5CkxBKsLB4kpA4bNYkk7LMfJXzT6lxTIRvqX3Bon1UK2wR1vBhXkqWGdSOYKwCnwpJ4UkqVySHauLn43J_glRyAt3lDODu5DZgOp8e0FjWrLkBjXx4lVzrepsUUGV3lXaf5T6F4fCkWEHacc_XqauEmhXqBSzKVxa6xYwKB-xAE3pqVz_MnRqEjLJIgViIW6OS2yQf-e_S7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
بیژن طاهری سرپرست استقلال: بعد از 23 شهریور که بازی آسیایی را برگزار کردیم اگر سرمربی ما صلاح بداند بازیکنانمان را به تیم امید می دهیم/ در اردوی قبل پرسپولیس به تیم امید بازیکن نداد اما محرومش نکردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105500" target="_blank">📅 16:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇷
❌
صالح‌حردانی بدلیل انجام برخی کارهای بی‌انضباطی خصوصا در بازی دربی، از سوی سهراب بختیاری‌زاده تا اطلاع ثانوی از حضور در تمرینات منع شده و احتمالا بازی روز یکشنبه مقابل آلومینیوم اراک غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105499" target="_blank">📅 16:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105498">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD5hztz3TZ16twDQjj86PTmC_5SQszjO_g2eiKT338ws6RiWXWiBN1Qj-JNgKuDnni-wM9XgiM0sfzSb5HNwq3rPvP8OmpWvlVS2K95gV3KtKpxGQF_MoaQFJYIjnS-btrf4TADSGRr_ydy2m7AE5-lo6GTKhixr4ULrOOTdKUEroxYdlbN07YlCIKY_-VoAUTYopFlfZnI0qLXxFiX9hoyVU7rph31gEWfTZRWQuZO7btELp0IngCldTE9iNeSgj9TRpfN23vPkLuQlqlheVQzjqtic1w1-f_dk-Fgp-1ZKxCkygsVJJDWy572PFtPKy1T5ntw9HTBYifR_18mnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105498" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhmV58yeRkUA8WAVEJXmG89Sg_kfyMpf86PFRvlMfA5AucMTnwSqr14321_aOmSduT8i9WXBO05SAhFN8k1rxCYhr7gM9y4VISeohIsXlzbkZNyP6QUzlU8gpa7t0fltpXYb4NQs2WbD-VI96U7LKuIyS8nFCzz8QPjuhNhB1_HBoLB7z_Say0hIwvBjBaGpdb7lutgugqMnQl02gQnw7Qu1FVqnqnbA826uXnQ9DpyQ1pIb2pmwT_1qDV-imjUSsXXs-COUx4-KKyoxLZthi1rYCzuI18tQjqnhbXOcRIckaEXtYhXjjFcQ9__NaZgvIHGZjtD96p2aPKKU0bwGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
ترکیب منتخب بازیکنان بدون‌تیم؛ چقدر ستاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105497" target="_blank">📅 16:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105496">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👀
⁉️
🏆
توپ‌طلا رو باید بدن کوارتسخلیا یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105496" target="_blank">📅 15:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=lwVUfxLLHdiTQGmuDTRxSnuy9ELwTNkoyVIEGhm2F3R_3FGuRR8T7im4PXZqCrIDJJKrqhLlvG-fzmzbC52R6xH2PbB3T9mFV-pyhVlt0wTlh34CtX416ZUKGWPdxVYtV0PN0LVS8rbJkTXjtMVndqirVDVcqaPHTLDvDbJ8NzmG1yWXeQFi0YoJ6aG-yusUEVAFR_e6VT6c1t6vVXXsIU-X6zzOnyOKfVpfwqs5s8uaTz_CuVC2agEvutA5gWyri9sCduA5sDdiHJ5-EgP7qtWKNUg0dyOCVi0zwEaqDa3_MZ7EE5FujHOFF-HjGMp51aWPhnke3tgUgG-SmJOw-lbF7tva3531cXEidCSWqTYgYdujN5uWGyJdhpj93GdrKxjFX-luItKaOizopj6WSUl2excZMK_UuspN4MFyWcKrNj0Kxl8Zo6hhMbCiMTu2KWKSGmVFtvKFhZGjvZ98H0A7N7NUDAOGdfqOTLY4_X4NSgT-FBL_QJcqzdlqOYCG9riwy0RBpS8BbPAIkkPO3gAV5NixOV1Da7o3SnFDsXG4gahRxQ52YTCqSVjd4xHjclNb5C2FDKEzcMyx0eFSGDzk84iMD09jdlOxZiydNINM0_SgkMdKOYJiKTum61_YHhzIGBy5fKvlTpDqvAJAsywsM7pgLh7sLHz9g1yTCjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=lwVUfxLLHdiTQGmuDTRxSnuy9ELwTNkoyVIEGhm2F3R_3FGuRR8T7im4PXZqCrIDJJKrqhLlvG-fzmzbC52R6xH2PbB3T9mFV-pyhVlt0wTlh34CtX416ZUKGWPdxVYtV0PN0LVS8rbJkTXjtMVndqirVDVcqaPHTLDvDbJ8NzmG1yWXeQFi0YoJ6aG-yusUEVAFR_e6VT6c1t6vVXXsIU-X6zzOnyOKfVpfwqs5s8uaTz_CuVC2agEvutA5gWyri9sCduA5sDdiHJ5-EgP7qtWKNUg0dyOCVi0zwEaqDa3_MZ7EE5FujHOFF-HjGMp51aWPhnke3tgUgG-SmJOw-lbF7tva3531cXEidCSWqTYgYdujN5uWGyJdhpj93GdrKxjFX-luItKaOizopj6WSUl2excZMK_UuspN4MFyWcKrNj0Kxl8Zo6hhMbCiMTu2KWKSGmVFtvKFhZGjvZ98H0A7N7NUDAOGdfqOTLY4_X4NSgT-FBL_QJcqzdlqOYCG9riwy0RBpS8BbPAIkkPO3gAV5NixOV1Da7o3SnFDsXG4gahRxQ52YTCqSVjd4xHjclNb5C2FDKEzcMyx0eFSGDzk84iMD09jdlOxZiydNINM0_SgkMdKOYJiKTum61_YHhzIGBy5fKvlTpDqvAJAsywsM7pgLh7sLHz9g1yTCjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👍
همسر رشید مظاهری: شوهرم قبل از انتشار آن استوری خود برای من فرستاد و گفت که اگر حتی روزی به اعدام و زندان محکوم شوم، فدای یک تار موی ملت چون همین افراد من را معروف کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105495" target="_blank">📅 15:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=exoaFXDRE83Mot7SNHOlWoyaQi54gXwVDrVPL4NcAx51fAegfrz7WXLJVyX5e6EqjjpsNrPfiBHwgVJ77JLG_zr5Zh_E6NQwwBmuT0scIk08YTRYsuyWHZmL2NZ8jK7i0SL-iL-_CyYxCNT7vfOfcbXtCJuOK4b7gG1qqPKvZvbl-qP_PZL-qbq_ibcf6JL4Mfk0sEjYoXsg-rMZNWMAPJxxioAbpRHBI1Hv6Wvh5HzfDQYK6vs0kihHS1itPyzsqovBSPtKGjuJn1Gc5rvfVIKHbp7Y-A0nnMbeaySYb3k3uF44Of9TFajlPZtiLvyb1VGuEl5Ec4A0muk9uN7LVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=exoaFXDRE83Mot7SNHOlWoyaQi54gXwVDrVPL4NcAx51fAegfrz7WXLJVyX5e6EqjjpsNrPfiBHwgVJ77JLG_zr5Zh_E6NQwwBmuT0scIk08YTRYsuyWHZmL2NZ8jK7i0SL-iL-_CyYxCNT7vfOfcbXtCJuOK4b7gG1qqPKvZvbl-qP_PZL-qbq_ibcf6JL4Mfk0sEjYoXsg-rMZNWMAPJxxioAbpRHBI1Hv6Wvh5HzfDQYK6vs0kihHS1itPyzsqovBSPtKGjuJn1Gc5rvfVIKHbp7Y-A0nnMbeaySYb3k3uF44Of9TFajlPZtiLvyb1VGuEl5Ec4A0muk9uN7LVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
از یک دربی تا دربی بعدی...
💵
دلار: +۱۰۰,۰۰۰ تومان افزایش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105494" target="_blank">📅 14:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=U8zDWh8onfSbaxWpV0kJz6sS1WDfmMDa8HhsfUCLGtFpUwb4WY-7mCARcd5iWaW1iOH-q7zVfz9nt_GUqA287d3tzcII6yWKFe_S4vrjoYF2wA3FBOoomWSMYKl9ntC760m76uQgbt69mSeOZiPtK5n-dTBxzL6qC8loikcrqFLXL5rSzDXbijrGWxtqa6S4BCGDSImmEE1QDve0Q2VD4SL6kQN1eb0WNcRWGQ2sE52cNR0GhCJAyxkJMlwyqhc8oBHurnfWZbGkc6POczrhs4ry2MP4QAUqaebEt4ZI3bJhKdiDaimmTGoEvtuhh5ROWWfK0tgq8X5t9SfQJI-4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=U8zDWh8onfSbaxWpV0kJz6sS1WDfmMDa8HhsfUCLGtFpUwb4WY-7mCARcd5iWaW1iOH-q7zVfz9nt_GUqA287d3tzcII6yWKFe_S4vrjoYF2wA3FBOoomWSMYKl9ntC760m76uQgbt69mSeOZiPtK5n-dTBxzL6qC8loikcrqFLXL5rSzDXbijrGWxtqa6S4BCGDSImmEE1QDve0Q2VD4SL6kQN1eb0WNcRWGQ2sE52cNR0GhCJAyxkJMlwyqhc8oBHurnfWZbGkc6POczrhs4ry2MP4QAUqaebEt4ZI3bJhKdiDaimmTGoEvtuhh5ROWWfK0tgq8X5t9SfQJI-4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال به هیچ‌جای زندگیت نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105493" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=XFZHPGyEzPvkbeTnUousnuPI_1VOOIibBJX-ANw-ke004qfDVlWDo7pzq6zzUZLNBHKK5Ee3rz-s3MMwb-kKtQ1neWSBcu1Lmejs5n5LG6bnywSqmp16zuwVs-KtvZ385QVJpD_7ocYuEZQYyKGX6Rb-hzUU7O1WYy9Q6o-jlORcDIRHd3gCvm3TaujiXGVOhIGtS_ZGpEnA9rcOzmRMMkuFXM6lr9kO78w9HDxpFAx15qb6uBithgGZV1cxqs7kS9wmb0lYbmLLMCWpro9Ro30We7fH8DbaatUdnRUNRQUIYedpPFGfVL2YcwTRuzbmSFf3D_-tY5EPU-odJD5E0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=XFZHPGyEzPvkbeTnUousnuPI_1VOOIibBJX-ANw-ke004qfDVlWDo7pzq6zzUZLNBHKK5Ee3rz-s3MMwb-kKtQ1neWSBcu1Lmejs5n5LG6bnywSqmp16zuwVs-KtvZ385QVJpD_7ocYuEZQYyKGX6Rb-hzUU7O1WYy9Q6o-jlORcDIRHd3gCvm3TaujiXGVOhIGtS_ZGpEnA9rcOzmRMMkuFXM6lr9kO78w9HDxpFAx15qb6uBithgGZV1cxqs7kS9wmb0lYbmLLMCWpro9Ro30We7fH8DbaatUdnRUNRQUIYedpPFGfVL2YcwTRuzbmSFf3D_-tY5EPU-odJD5E0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وارث شماره ۱۰ آرژانتین که‌ خواهد بود؟
🇦🇷
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105492" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878e055f11.mp4?token=L6hjQyl77778a_i-m_2DE5XhsdPVvvopsSc5S3T1N4y1JJpbS6sxiU2hKNh0_hjWXftiUiFLSxu9oEs76dwp8GBVrxwdelT6jfbkqNEWc_kwqbiQLc0Ov6PHVT8GM_k3-BjQLvwuNxyBJbdWg0gKvlxSGK-cl1KHFPkaMZbnsJqwibknIgsn8vPeXsosOpky-MB5tJpUDU-f-ZpX7XcjYX9VPRaw8pLAzjQVvk4LsTlBji6tj1m8wFXpOKv61wd5iz2E7zaK7e7aNntW-68Js5CGPcX9EeSt4R2q8YIlQwzzZYXatM7NX_ASNW5axApQzKZ_Jxl5_kISHSekujsKpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878e055f11.mp4?token=L6hjQyl77778a_i-m_2DE5XhsdPVvvopsSc5S3T1N4y1JJpbS6sxiU2hKNh0_hjWXftiUiFLSxu9oEs76dwp8GBVrxwdelT6jfbkqNEWc_kwqbiQLc0Ov6PHVT8GM_k3-BjQLvwuNxyBJbdWg0gKvlxSGK-cl1KHFPkaMZbnsJqwibknIgsn8vPeXsosOpky-MB5tJpUDU-f-ZpX7XcjYX9VPRaw8pLAzjQVvk4LsTlBji6tj1m8wFXpOKv61wd5iz2E7zaK7e7aNntW-68Js5CGPcX9EeSt4R2q8YIlQwzzZYXatM7NX_ASNW5axApQzKZ_Jxl5_kISHSekujsKpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
برند Dyson یه مسواک ۵۰۰ دلاری ساخته که دوربین داره! با AI بین دندونا رو می‌بینه و خودش دقیقاً همون‌جا دهان‌شویه می‌پاشه، و تصویر زنده داخل دهنتونم روی گوشی نشون می‌ده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105491" target="_blank">📅 14:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز جذاب و دیدنی از پلن‌های مختلف استقلال و پرسپولیس در دربی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105490" target="_blank">📅 13:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105489" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105489" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtV6-fze1BceOfLA2o1-HF1dRSKuB_B5ew6L6rYXUXReyAuXrFbAjc8mPfwLOcVtS9blp6BuZH-h8dsso37jC0Mukz5MsedAnmYFS7gZFkaGuE2fvfWubt9482D__56482srjk-4nsNNjj3HE_plGQCLXj8nVwYn_T0bc79iavfG-R2eaAtmytuxdy2OZOXgRz44V352eKG1i9BXKeZ96awhV90RXZBRdhL8t92IyOOEJLINMrPlEY8ozNiDS-sx-DP5ypE6vDjRmz7o2ErKXKpW5Gq4UG3ccXXXMbnO5NBWV1186cmKqr5X1u4URUWKkzW2th4pqL5H5Mkgoxt1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105488" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=jiGl1YyuY_acXfiXeSE1AT1QP11Y70HA0hEM5JYKsvY-ZHSsL3Y1wbLlNIbWbQzNIH0TkUeLBt2b_i_yB2kmwcYFnR_bn0gp4p4dpJvSVhQCk0PyjlTwSlCtlgdS3ZPgRMBC5CEiCH1TaOW6ppbEZl_um5KA1hKB9rhsWtrqCE4C0dYnQA08siE90efY2TlcF7eH9rMkWFQhEY4Y8sYEOAV4bZDNOsKZKzMNWnBRXWNlc0MFzkSueRt_nhFqjJ0zBF__Hc_yayJUvcX6TdTvH09bxjWTOmQqswdQdkWykoVxNUUb4_a6TD05tNKvlnRiQv5tA8uGlYTGIJTBSEljFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=jiGl1YyuY_acXfiXeSE1AT1QP11Y70HA0hEM5JYKsvY-ZHSsL3Y1wbLlNIbWbQzNIH0TkUeLBt2b_i_yB2kmwcYFnR_bn0gp4p4dpJvSVhQCk0PyjlTwSlCtlgdS3ZPgRMBC5CEiCH1TaOW6ppbEZl_um5KA1hKB9rhsWtrqCE4C0dYnQA08siE90efY2TlcF7eH9rMkWFQhEY4Y8sYEOAV4bZDNOsKZKzMNWnBRXWNlc0MFzkSueRt_nhFqjJ0zBF__Hc_yayJUvcX6TdTvH09bxjWTOmQqswdQdkWykoVxNUUb4_a6TD05tNKvlnRiQv5tA8uGlYTGIJTBSEljFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
اسطوره معین دیشب به یاد بانو هایده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105487" target="_blank">📅 13:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtH-vggpyCgItwp7tu0JlR3yV2UPviLuU01BK3XvVDcEL_ig6veQgS1i5Fl3Qas3rpK4fuXpuYgxBxjaqavrqqEp_5KQ8W1DrqZKMd9dBwQokpfbosdFuPgNTxSzyJ9HdLPIG3IGJ_0rHOHSyy4Ch2bl_cCZvPJS-xtsBhYK6dicEyHvMxEyJ7CgHZubiLefjk-CqTugnOi5Lbn-lloDiOmiXPaKH44pROIFVm0dPA-CIytDXbYjAv0HVjbw2VL5Mm5Q3b2yj9VRvc33WVQ-MgWcG8MxuT5-Y4PhPaXN1ZLXz1_-01kw_9PqkaB19f_BVLoFqPJZQHQjSCGk275bdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درصد برد ژابی‌آلونسو در تیم‌های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105486" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105485" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjfZv_2lVVSZvCjb8hiRMduQGRafq0KEwbqYKXZLlGyE132F0JlSp5LGVXxQMF76ZKgOWdIss9k4uZWQq5UPJ8IHJpOwNBjvz-ov_Zw8ZjMwQ7jjsNwnsoDx4xMJr98cU_z2DaCEAIPkTinZfco5E-x3HAKsa8ZXGC_lcwK0_KOtlfxvHI2bsXn6rrP-cJC_WvySVpOu1wsCq1nqGYhdbr7e6qvqPFCVCeCqO9mpNUIyTQR8lK32B45klAXd_axK6C6wueC-gvXLNTxPDhcGws5Y0QoDMDAuLrnWNwr6AniQM2JagnJNkYXzgz4qC0boj6s6APLECiBWaXDiyKRRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
نگاهی‌بهترین‌گلزنان فعال در دنیای‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105484" target="_blank">📅 11:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👍
▶️
اجرای ترانه حماسی ‌"ای‌ایران" توسط اسطوره معین در کنسرت چند هزار نفری خودش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105483" target="_blank">📅 11:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPEepEj0gkV0AmsDNW47diCY1H-MRNi4byn4JV3Sf2WTTV0AASzZ6DCZ6NI4UNY9WNv1jY4VZ9YEkcKsqZzF1fwRZJrARHooxpPslgi8fkl43brqMmufxd2JdVrRAahPf6Ebck8384vD3g7l7JRdbOE07O0yUDL7LVDZfqcHfZt4Tqqbwcu3F0srB-QEl156J44AaaszP1lkX7NUdkAL7BAzxea1lWQrlp9ORF58kVmyHJcFxwQcNvcWlI6m_fgWFkWJEC9mOXXkiJk849tS0UiXZaXFD3uqM9HkQP5qyxNSaL-O_JDv1al5YxdtBgLNEF_ZBWQoHPepaUCSFT6w5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو دربارهٔ بازنشستگی لیونل مسی از تیم ملی:
صحبت کردن دربارهٔ مسی مسئلهٔ پیچیده‌ایه. چیز زیادی برای گفتن نیست. هیچ کلمه‌ای نمی‌تونه کیفیت او رو به‌ عنوان بازیکن توصیف کنه. او با ۳۸ یا ۳۹ سال وارد این جام جهانی شد و دقیقا همون‌طور بود که همه دیدیم.
او یکی از اون بازیکن‌هاییه که دلتنگ‌شون خواهی شد. مجبور خواهیم شد برای لذت بردن از این سال‌های آخرش بعضی بازی‌های MLS رو تماشا کنیم کاری که شخصاً زیاد خوشم نمیاد ازش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105482" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2EY2N2Ez4hPsTjCaBJnWtxvUSLZzgGkOTiepUfi9QBBOHo-NPCc_7X40pj9JdsJVUeqpOUWFvqGU5-drGlX05yFGa0DglkpaV9Zgysh2bTo27lFrSJSXohnBrPRl2fWdYWcSIq30duIWwSpLpNnQIQ3ZyJflvmGQKwwpjAVopEKGc51TPQXXgoox4geyRBmkEevU_NqFV5pUiQKhki_mZQZ3MIgXrHiaHihAtddIy9rgUSBPZ4RoYl-kBucsi2Uz7jBxf-cVKcKBAwTHKuOzxR1wCIN7kpLSwZfhBcBzqnkqcgfOC3t8p57PDsFOG76WgqYFtQNECeROGGouHSqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htpm7fWm7mKF0Kanh01Q08VId8HnGbeWmi6SvMQmikKTpHv8JpdB0v-ALksC3WP7W4rBn7ik0H4W2K02ZDG_4_ip2dkn2iLbuz1e95pKnpcjL9A0p8NI6HMyirAfIiVTZNkwzg0wdcpXjxKF3DrALyFkIyLRcYsFjhSJE8fsJ3K5mu-9LsIjxiE1XtPosWYVQPivsTcTSOfmWBUzJC4ZN1SY9UpHN4GqsoVBfso8QB8ZizlGsQmJsmukRkgfkf35Chc8YuB4fu7kcubxNv6cvptSJKITr5JPiI8Jf1PGjpX-U4LvLmvDfXbd9ut0jmSdANvoYUbWiexHpJXXebJGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCXf0n2anAqLxVFE2ldlSPytaBw5H_IJuzJ0cyJPUdKe7N5BmuN7KDWrVFfBtow2yQrmhuDViNECnlklhyBfEvrbyaSEPidQQ2mSouGccPjtpU5OLUjqDoFxlj157hgaEIyRTw28k5Uxj6vn3CdOymCQzy1-Z9QKSmDzyNB47q5qeSerGClmz-o6TPASCN5DnjvfSFchuM4ZB9d0jReCOvTO1oX4IMtOqAZNbOxEwM7xf51BJJSUljoceLB2He1E_EvEAKqC0DKZeOy9b1eZZJjkhGLlLTnkuxQJpK02Yt8JJnbTa1N1Gu8UAbrtrqSQ6yHRUjxbKryt91OQrtIcdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس جذاب در حاشیه دربی
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105479" target="_blank">📅 10:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👍
💥
عایشه‌گل دیشب رفته کنسرت معین و از لذت بی‌نهایت صدای اسطوره ایران بهره‌مند شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105478" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خولیان آلوارز در اتلتیکومادرید موندنی شد.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105477" target="_blank">📅 09:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
یادآوری تلخ‌ترین خاطره مشترک وریا و سیدجلال؛ خط خوردن از تیم ملی برای جام جهانی ۲۰۱۸؛ از خداحافظی زورکی کیروش برای سیدجلال تا غافلگیری وریا از خط خوردنش از تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105476" target="_blank">📅 09:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtG2f-G0nqFT2Q9AAbws032oSTd3-VAqaUxQ0ET1cF809zpRB0IQg0Nk9Surg_h0ZdPZf0cnAeYgDtPKv85MEHMW4fGD5HkGeBb2HcrBENs-v-yWxxYEc1VK2-d8rp8zuFdKPnbdRorzxtxORtA8MJVIT6zUNtJ_HX5yo_p8Yct48OaQKXFxtxEiQJLZYZVaowl-CQUHE7XbnT0jPNcpqCkwJrzIuLC5it0C6i9pE54PtFeHne_whGgva5BW9keuV9U5w4L9ydL8RYI3lQUMRtiFmfke9ONLkXD2DNVVDN659g1yykLj-39UZ1OHWLm15Q0Dxgq8h0mKDrplkCo-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وریا غفوری عزیز و همسرش
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105474" target="_blank">📅 09:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
⚠️
اوج قدرت صداوسیما مردمی در تمسخر و تحقیر رئیس جمهور بزرگترین کشور دنیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105473" target="_blank">📅 08:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105470" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=Bs0tcA4u6vClyM33-eYIjb1acncUZ6yopEAniurEF38OXIqDvYfCTjn_q6gJL-3wp6fMEE_0al88x3zpwHoUmHgucRNcC7o6zriLiC--TA_X829DP5BPpPd5t3vPmx7EQOA29fTnN0W-WAD9kzqTcCOXrMI3iBdibpqy_fZgmv78nZ6eRmyDaUhg1-lFKHqMTDDtNNYC7kfObrCB3G2mkZuDKn1sGH0Lh0DMwkQBHDNQnHRQPSRtXHKvSQUTXG5VMNaCqzJb01OR-ak95JgnTFyqzlCJ-Rkua0grc-FVeJqBo3fux57fGGNEnOcdSukRvdLEeupjR4zRo6iMbFCpdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=Bs0tcA4u6vClyM33-eYIjb1acncUZ6yopEAniurEF38OXIqDvYfCTjn_q6gJL-3wp6fMEE_0al88x3zpwHoUmHgucRNcC7o6zriLiC--TA_X829DP5BPpPd5t3vPmx7EQOA29fTnN0W-WAD9kzqTcCOXrMI3iBdibpqy_fZgmv78nZ6eRmyDaUhg1-lFKHqMTDDtNNYC7kfObrCB3G2mkZuDKn1sGH0Lh0DMwkQBHDNQnHRQPSRtXHKvSQUTXG5VMNaCqzJb01OR-ak95JgnTFyqzlCJ-Rkua0grc-FVeJqBo3fux57fGGNEnOcdSukRvdLEeupjR4zRo6iMbFCpdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
واکنش‌ها به صحنه جنجالی دربی:
🇮🇷
بیژن‌طاهری سرپرست استقلال: کنعانی قشنگ انگشت خودشو فرو کرده و کشیده!
❌
میثاقی: بنظرم باید طول درمان بگیره!
🇮🇷
محسن‌خلیلی: صحنه خیلی قشنگیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105469" target="_blank">📅 01:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=hAJ9FCUSWmw_BwUHonddiUit4KieLnT-Hjy5wLOk1U_pbx9tC96bp1XwIshsHizO9iYn1w2DvBYohj5GRo9iWVfiYE-ACpSabskdyDctuQTDdA5TXoCWnWdiO-OzNApEUn2L_qOYOcv_q6Ee3muQdzz4Ey7FhMzJduWtmvD-WMOJ-EpKCn5iA16EbaC2WdwJtlInQfpMgc49Ln73yS1vPPrvS3HezZ1tNFCM46_cJQKkzBxrEOAlH4Ij7xewvr2iGWIxcTZNXO-Pmgv0TIlAjjGy2mCxD8rqcZsNcxE1HL2tEoHa-yCizY93brxlX9143K8z02G1ucDIChSJqLFsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=hAJ9FCUSWmw_BwUHonddiUit4KieLnT-Hjy5wLOk1U_pbx9tC96bp1XwIshsHizO9iYn1w2DvBYohj5GRo9iWVfiYE-ACpSabskdyDctuQTDdA5TXoCWnWdiO-OzNApEUn2L_qOYOcv_q6Ee3muQdzz4Ey7FhMzJduWtmvD-WMOJ-EpKCn5iA16EbaC2WdwJtlInQfpMgc49Ln73yS1vPPrvS3HezZ1tNFCM46_cJQKkzBxrEOAlH4Ij7xewvr2iGWIxcTZNXO-Pmgv0TIlAjjGy2mCxD8rqcZsNcxE1HL2tEoHa-yCizY93brxlX9143K8z02G1ucDIChSJqLFsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105468" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=KH4iuhCgu-_OjTK3O4Tip-pYvimaQOsTzwr-y-ooKpoF4qt9wrTMw4KyGv_O9XBo9chq2WNYByWnMeCTlAihuv1tpxqL48m1Q0PDw2s-qvghqiG1xw_wwZJqbz9Ibem8j9JXzHuy1GjRq2F1RmxF9xNsHWWvFGBZjm4lrDiiC4vOcWftXfkCnd6fla7Grc8R3hCQaqnvUM90kUVj3-JByezf-_qBQJ-4f_HeBuGbUDjz-xfcBDPmWtu_2jsnWY2ophvefxsIX6kzvW8JUqrRNjiLL_ZyGn6LGW2pb3aW2Z_zS13rHkYgYmyFxiwro1Usm3U4jQxxcyUdWRt3XJ0xmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=KH4iuhCgu-_OjTK3O4Tip-pYvimaQOsTzwr-y-ooKpoF4qt9wrTMw4KyGv_O9XBo9chq2WNYByWnMeCTlAihuv1tpxqL48m1Q0PDw2s-qvghqiG1xw_wwZJqbz9Ibem8j9JXzHuy1GjRq2F1RmxF9xNsHWWvFGBZjm4lrDiiC4vOcWftXfkCnd6fla7Grc8R3hCQaqnvUM90kUVj3-JByezf-_qBQJ-4f_HeBuGbUDjz-xfcBDPmWtu_2jsnWY2ophvefxsIX6kzvW8JUqrRNjiLL_ZyGn6LGW2pb3aW2Z_zS13rHkYgYmyFxiwro1Usm3U4jQxxcyUdWRt3XJ0xmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
📹
🇮🇷
🇮🇷
🟨
نظر اتاق VAR در دیدار دربی درباره صحنه درگیری کنعانی زادگان و آقاسی نظرش بر کارت زرد بوده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105467" target="_blank">📅 00:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=bLp-izXhh5tg-N3pq4rLANgP2cH8Kjvb6r-JOlnf3fBe5lN_GeeHyJTpV3MEuofPhOSMcbDwIuSDYHD8rvCOfDmI3d8eHinuXHTwgdghSb4k3XRz-hH8_LNObasCvQwl6Tp6Sn_4Kao-OrKFP_L-0rPxGvQffvkmT4lJaq4mMYyrijD_pNiDOn3fUqNnCleKDBwbqiPvLoDMikli-wOEruR3dExpv6wTv3c35uFdWGnNWf_P-u7FSmPxnr-lqN9LJb7qRmFnZw1wjqx3SsWx6xDlYm8_NrXnXeTsIzA76WvWDNuGje_IfKx_l9OwRhn-qD7AXBfZTflM8pG24l5jFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=bLp-izXhh5tg-N3pq4rLANgP2cH8Kjvb6r-JOlnf3fBe5lN_GeeHyJTpV3MEuofPhOSMcbDwIuSDYHD8rvCOfDmI3d8eHinuXHTwgdghSb4k3XRz-hH8_LNObasCvQwl6Tp6Sn_4Kao-OrKFP_L-0rPxGvQffvkmT4lJaq4mMYyrijD_pNiDOn3fUqNnCleKDBwbqiPvLoDMikli-wOEruR3dExpv6wTv3c35uFdWGnNWf_P-u7FSmPxnr-lqN9LJb7qRmFnZw1wjqx3SsWx6xDlYm8_NrXnXeTsIzA76WvWDNuGje_IfKx_l9OwRhn-qD7AXBfZTflM8pG24l5jFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
بیژن طاهری سرپرست استقلال: آدان دیگر به استقلال بر نمی گردد باشگاه هم پولش را می دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105466" target="_blank">📅 00:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=a0HKyWPKsMOn-h-9zUpnSA9FooIqszPDD5__7lHZf3YeEHubF0X7f7wJt64kvg9pLzSHOGHTGdGOS2lK6hius68MJi9zBbhWSPI9o8MVi3TPW9m7atiUkRTzNB4FjplYzfckLd1buUZQx0BNKRbLmaZPIhjSVnnVvGnqUgFFrw7Q-YGC3GmfgdQkWZKL3_0-3LJqRZudhQ_zUYtVcA8Sb2m9cn45ugmvcN0tfNcmolQ3DjqfxJ-AyPeFcBFrvKH5DBXYqNoiBg-bn70Qjs33SOL8ByUkoYgPc4hqG-t9OlLa-OATeLet3Fj8ipIuV7ONn8JmwyM69fs7zyVgtwgTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=a0HKyWPKsMOn-h-9zUpnSA9FooIqszPDD5__7lHZf3YeEHubF0X7f7wJt64kvg9pLzSHOGHTGdGOS2lK6hius68MJi9zBbhWSPI9o8MVi3TPW9m7atiUkRTzNB4FjplYzfckLd1buUZQx0BNKRbLmaZPIhjSVnnVvGnqUgFFrw7Q-YGC3GmfgdQkWZKL3_0-3LJqRZudhQ_zUYtVcA8Sb2m9cn45ugmvcN0tfNcmolQ3DjqfxJ-AyPeFcBFrvKH5DBXYqNoiBg-bn70Qjs33SOL8ByUkoYgPc4hqG-t9OlLa-OATeLet3Fj8ipIuV7ONn8JmwyM69fs7zyVgtwgTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105465" target="_blank">📅 00:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=UgvXwJFOnXfgK-m8y19x-fDhVC9g5rCyN7Rhv9z36vXZB4zGmN-zwATQ2eEylNN5N5-BwF6m_kERfcZJbEWu3Cf_JlG4Qa14haXEtALZELV2-bFxXQlHPL_VkHfodY0Hupg8J6JF9kennchGYzrDahv7teRy_NKKidhY8Bu65yIv6nL7wc5J5xOb3aq7Aaeo1oaFGgu9YSrvtiU03JppqFuvmw0Xm9n6YNufBfOa9gaBHYU-tRtgXWybkTRGbC2UymmRA20Jd2C1jxprx3B9sVeY54dPFCl35Cx3If0ISYg-hub1w8SU-ep8Ndoc3lDp8tG7O5Di03qqYohGKcw6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=UgvXwJFOnXfgK-m8y19x-fDhVC9g5rCyN7Rhv9z36vXZB4zGmN-zwATQ2eEylNN5N5-BwF6m_kERfcZJbEWu3Cf_JlG4Qa14haXEtALZELV2-bFxXQlHPL_VkHfodY0Hupg8J6JF9kennchGYzrDahv7teRy_NKKidhY8Bu65yIv6nL7wc5J5xOb3aq7Aaeo1oaFGgu9YSrvtiU03JppqFuvmw0Xm9n6YNufBfOa9gaBHYU-tRtgXWybkTRGbC2UymmRA20Jd2C1jxprx3B9sVeY54dPFCl35Cx3If0ISYg-hub1w8SU-ep8Ndoc3lDp8tG7O5Di03qqYohGKcw6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105464" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=vDlY0e-NDLqu3dMaXS1yPLaqrFZyp-NdrrXZFPSxJzDb-WEsRs9gUGgyknDngQ8V7HS0sNjI9rBNCVsdizmIJZ16WcZFKNM0zC7cDG9rpwTv1gJ4vdN_-J10eEFztUTnmzufp9gM8okBN21XGL1Cyu0kyYhpRCCFfDuOxJzVg6NSEfwwSty9RPOscnxD0w4rct2nXnukYtwCXyU9cbbaRL9DrWn3WijZRC9qhz4Q42jaXSdblD9cbs63Jxr6VmksphdAZb4TDbllmNAFnT2g56O5oog6PSiMba36bC-rLxCRVV9IqQRrDchGKpwD88gntTT5UJANzIMZcNjwVjyJbAH2k4De7J3hSt6pdFHRN2xbG_910ITnC5AvInRCm8HdfDf3wnOxXqO-aJmZFAoZxty0PyJpr84KZggoShI6idky1HVqR_zU1dis0yioSfORpG_UrJU2WFi5juD8BaaHnRRBsUimX25i8DnBkD_atGtB70mATUyAgtLPWpD0KZwKRVuezCW-BHBbZhzx2dV7zFGYWgS-kJnaRUXEEGj0jdhj48kDoME7pLnvpkL6uTA_C8LnT7crJq1N27p6xN_JJRvDPAp1VDwA-4kuXr3xUvlz04Maox7-QHURrmMOVlATfN-w5dUMVe2U72kjYkp10cvMrV_rJW9vA56gr6afQcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=vDlY0e-NDLqu3dMaXS1yPLaqrFZyp-NdrrXZFPSxJzDb-WEsRs9gUGgyknDngQ8V7HS0sNjI9rBNCVsdizmIJZ16WcZFKNM0zC7cDG9rpwTv1gJ4vdN_-J10eEFztUTnmzufp9gM8okBN21XGL1Cyu0kyYhpRCCFfDuOxJzVg6NSEfwwSty9RPOscnxD0w4rct2nXnukYtwCXyU9cbbaRL9DrWn3WijZRC9qhz4Q42jaXSdblD9cbs63Jxr6VmksphdAZb4TDbllmNAFnT2g56O5oog6PSiMba36bC-rLxCRVV9IqQRrDchGKpwD88gntTT5UJANzIMZcNjwVjyJbAH2k4De7J3hSt6pdFHRN2xbG_910ITnC5AvInRCm8HdfDf3wnOxXqO-aJmZFAoZxty0PyJpr84KZggoShI6idky1HVqR_zU1dis0yioSfORpG_UrJU2WFi5juD8BaaHnRRBsUimX25i8DnBkD_atGtB70mATUyAgtLPWpD0KZwKRVuezCW-BHBbZhzx2dV7zFGYWgS-kJnaRUXEEGj0jdhj48kDoME7pLnvpkL6uTA_C8LnT7crJq1N27p6xN_JJRvDPAp1VDwA-4kuXr3xUvlz04Maox7-QHURrmMOVlATfN-w5dUMVe2U72kjYkp10cvMrV_rJW9vA56gr6afQcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105463" target="_blank">📅 23:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125703b27b.mp4?token=so65KRe3JB66iEu3a10g0nphfVWf5YWUAR5qQdmNp1zBcRsWC_IS4SQXOmMQCuNTDml4SL8atjWo_s_-0MiV_Go_p_j8WhyGJ9JoQeVVZsVldG1AjtZAi3IfsPXI5rIVUH7heifT3uMpfSYrza_YiFne88741KBrmoq4_2KZTUeWJ1y-GfTFxAsVpMvlGX_foLu32MQGULFv_FRe3J_ee3KMR0KD28zx6wa9mQR-_ocPNDSpqvePAuesGnXMOTju8L8bTifaEG_csv-a0nlq14McOhuue5LK8TdRPgqF4FIvGPgZprl_wGgzPYhBYconkqnbWw2RWFPJVM9O_jFpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125703b27b.mp4?token=so65KRe3JB66iEu3a10g0nphfVWf5YWUAR5qQdmNp1zBcRsWC_IS4SQXOmMQCuNTDml4SL8atjWo_s_-0MiV_Go_p_j8WhyGJ9JoQeVVZsVldG1AjtZAi3IfsPXI5rIVUH7heifT3uMpfSYrza_YiFne88741KBrmoq4_2KZTUeWJ1y-GfTFxAsVpMvlGX_foLu32MQGULFv_FRe3J_ee3KMR0KD28zx6wa9mQR-_ocPNDSpqvePAuesGnXMOTju8L8bTifaEG_csv-a0nlq14McOhuue5LK8TdRPgqF4FIvGPgZprl_wGgzPYhBYconkqnbWw2RWFPJVM9O_jFpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇶🇦
رسمی؛ السیو رومانیولی از لاتزیو به السد قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105462" target="_blank">📅 23:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=h6T0-SIJ7dLuO5bD9UCHOwwDRf49zQF54OUS7lLR7fT5v03b3JeKCBz9yqIhtvpNRTb2OqkhpOHt246CvYxB9p8uoAG9j41tFfk41kMXMaCQxGorcH7f2xVOvm1FwnYVVxse2ra1eDa3O4WdyATpm1_Cqo4x35HB_6blOyuff0mn5F93p7dpfSxUmsZqmxf_7lR1480KxJogwiqUuaNhCn82CWbJUgHsVrkjqg1JUuUBwxUfcvwJ74BY4mMAV7iQH6TgHdJs3Gz7bOtefq1Ws411CxGwkwxD3T5Qv36mhzrkSkAzopLK91ZfkEznZGbzdkYsUD2LUegCqcd8mqLE5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=h6T0-SIJ7dLuO5bD9UCHOwwDRf49zQF54OUS7lLR7fT5v03b3JeKCBz9yqIhtvpNRTb2OqkhpOHt246CvYxB9p8uoAG9j41tFfk41kMXMaCQxGorcH7f2xVOvm1FwnYVVxse2ra1eDa3O4WdyATpm1_Cqo4x35HB_6blOyuff0mn5F93p7dpfSxUmsZqmxf_7lR1480KxJogwiqUuaNhCn82CWbJUgHsVrkjqg1JUuUBwxUfcvwJ74BY4mMAV7iQH6TgHdJs3Gz7bOtefq1Ws411CxGwkwxD3T5Qv36mhzrkSkAzopLK91ZfkEznZGbzdkYsUD2LUegCqcd8mqLE5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
گابریل‌ژسوس بعد از حضور در تمرینات فلیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105461" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=A8qjflZ3rXTPTWRnOXL2ea_6Mv3C6v3mTKL82dl54r-TDK8zsKKDYLIGLQreOLWR90VKswvPhtF7e-gtZC_CyRhs8sT725iX7Aqywr1bZZT7myiShxbJK8ZPjiUybhexy0qF0JjPU0NXY8oYsQ3ICpBG0meuhlWG1eqAi6VZ_BwQmSUTBroc9Q7TvmDrwwNA3bCehWDt8uUHspwP_xDzvaoceq7Y02Ktz6nkLXhbvx22dr8uLSbubyvMOHwIZ0Y2banAoZ3FORZD375tjlCbvINmwRjkAlMQjo2OLljtnRHzsfE5PuCuUkxVSId3ng6mQ_AHiMGS375UC6W6X6KtQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=A8qjflZ3rXTPTWRnOXL2ea_6Mv3C6v3mTKL82dl54r-TDK8zsKKDYLIGLQreOLWR90VKswvPhtF7e-gtZC_CyRhs8sT725iX7Aqywr1bZZT7myiShxbJK8ZPjiUybhexy0qF0JjPU0NXY8oYsQ3ICpBG0meuhlWG1eqAi6VZ_BwQmSUTBroc9Q7TvmDrwwNA3bCehWDt8uUHspwP_xDzvaoceq7Y02Ktz6nkLXhbvx22dr8uLSbubyvMOHwIZ0Y2banAoZ3FORZD375tjlCbvINmwRjkAlMQjo2OLljtnRHzsfE5PuCuUkxVSId3ng6mQ_AHiMGS375UC6W6X6KtQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بابک‌زنجانی از دزدان قهار مملکت: پیشنهاد ۲۰۰۰ میلیاردی خرید سایپا رو دادم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105459" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEpg8Rn86RTlhu14hCru2a6L3MCrtOlNelknmm3vUy23893cKWA5pXor8x_AK-Z59twDUpgTWi_YCF0B47VxtcvboNk5kzg4XXpQiU3X-7vEa8RXQ-cjp4YzBAdYlttbWAQixAcZUH8xpXbjyAhZwu1OPonpzanS3a1tq3XgNk2-eb0GmdYD5oKducNVf-jM2GIGc66qDFQwoqFuPA26sC624exrv9gXWzeHt4nzMUMTDjfeGweu6rzHuVC7QHZSx9V8bCT6s1tjl0oD_6sqNmjKqXgwoYhz2hdX0-fpgto1Z2uIgCRdnKNuarz-xlw-Cdzk8pjgt1moE0UVGrGxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
💸
درآمد باشگاه بارسلونا برای اولین بار در تاریخ، از یک میلیارد یورو فراتر رفت.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105458" target="_blank">📅 21:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=sjLGKtZzhjyRYj4CYfGcBmebOZ9zhXKBT8vQKZ5EWvbJyNXIVzoDIV9mI2ovPLsueVzsqeUMIl1FrADVtlatcwkI7yW-wP_Gm97DTYLSBdnbMrOLAJSllh-3kHgHrK6qSFX1IuhubCcmViGaw-F3eUGfenfizZSKlfvQQ9RIPBB5SkEJ7qQSyPo95tbSApfHnIIE1QTdjfxwcMmCYYG8ZmaroibTm4j1Z29oihisHuOB5nfRA3JH5i83SH5PMfd68BWob9gHn1yYY4BBVyK3hukr9mIq-pG48PhbmfME6N-aHjWqHmxt_Hi-NzzL_y6IGTXjezAXaqMqie5wXqpeiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=sjLGKtZzhjyRYj4CYfGcBmebOZ9zhXKBT8vQKZ5EWvbJyNXIVzoDIV9mI2ovPLsueVzsqeUMIl1FrADVtlatcwkI7yW-wP_Gm97DTYLSBdnbMrOLAJSllh-3kHgHrK6qSFX1IuhubCcmViGaw-F3eUGfenfizZSKlfvQQ9RIPBB5SkEJ7qQSyPo95tbSApfHnIIE1QTdjfxwcMmCYYG8ZmaroibTm4j1Z29oihisHuOB5nfRA3JH5i83SH5PMfd68BWob9gHn1yYY4BBVyK3hukr9mIq-pG48PhbmfME6N-aHjWqHmxt_Hi-NzzL_y6IGTXjezAXaqMqie5wXqpeiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
چنتا سوپرگل زده شده روی کار‌تیمی تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105457" target="_blank">📅 21:03 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
