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
<img src="https://cdn4.telesco.pe/file/Rji-R79DuVbL6sPCwcDAcSGz0KB6oIlZl2rK-ztXAPefwzPsiOMXsxeXC3VUDK5DDQIkECm-o-eEuBBBASA6mFjt6D-4b6-_PSzyokh8IfkzLnlvSw2oHPQHITYRnZS65XCtSp_asOEwfERrTradleQORv-GSlyy_iZbG1nI5u6bUsRGYvsPmPC-TOA_5EyA4_c-BvhDbTXUvmwdCrF4GMQIrwVi1sJR9kxqr-q2ojJHeLZ5VFDJLJMWk3ZQsMg0NMp_HtU4-fCSEbjKwfZvN9sUrluQJR7qt2fWlJlN2Wcc9uW33ngrxEbwONqZ3u2oUq0KIgOz6YVwoajwKqgDgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MyIYK6ZjoTlwoAPLzdxy7wk1Pl9eq6Ckkr9HyE_kkyoJwqYB3Adb4XBA1dhnuC5gWZ8Gg52IJFP3D9Zk_WP6qhY_V8D4_8ypyv_xBLspbkZ1hl28vh10UITop2SZr3eWI4ASRVkgtQeJ-m_fbL2ad-3MPIzDIteDKD35okEh3oGMrcRyiVjZ1qrJLracZKiFS0IdAES8Pd_-wgjH99IqDQ4Mz2sf-BvwnJlhZ2CEA8mmdtm1dD33Wu3iUAD40hAfj-VbjZRLPpWJkvHvIsKuoUhYXpYTTosntCfnvP06XIFooBVGZCCa7ErvhHCfVyj9EmLqm-_u301ZJbGNL9zg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Xbm7RVNxpUfIH1l5Mf7XhG_B93XeZy9NdnMajqD7gAbeU6QgmEDWlfUZRdULun0fD_budg8-1oOWy5insHKRJcJM738XkzBAQfBPDGji0J9o5ALpQmyDpyuEXJ0OiuRKqjtYuMrivR7BugMxaosuosNNuAzr-ZYpvihq-Jh762ap_tkp3a_Uif0MH9CDQYGPGmscbJDPYhlgUon2TPpqdqXbWr0l4SHVoa8o6HyCc9SzeOmYznzwcZtKj8dxS8IbaoOlDdrNx9nZ2IOYX-A18w4SBi0EpdiVAh3q0tN5j3Ck2Og4wV0ngiYkxxwJIQZSOMs-cU-n-KEvRU4dhqLZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG1NIjKvmHGb3MedptkzN_ivYtmSgbcG0P1wm8quaCg1I9QMotksBBJTH6IMdlKbHbZsoUbusGm3lo9bTGfPdsro1-mQZWEhy7mjMsWSCxQ0Sy7DFNnaO8yukdjzAiVTnJ5SaM8PmRhO0wy3aSfNtA0eUz4jMM6yp5d8uXQ0DMSyjADhnQPfWCdhN7ILB9zTCN7il6COtvKmwcPTKhh2TzDdoClJU7HAb48o_6EV-j6ww38I9McaDqy0nGwKTYfFMBnujnA0xbxgaagW33lA5RL53bdau0xeTQBxoJsB_vOy-Or0-tf2YzYQq2dzADSzGl6PyukOvCLf-kkDqfPT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/whitedns/1894" target="_blank">📅 17:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1893">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZQalnFnIn0LF2vthhx85u_c8zL0ZXNjkxI-sPQKjlHN8cXPVXhDQVgNygFJiwaavtxgy3f9z70OcCrDzaAGVDHRDyZJkb1pg0CSF03lqBh0H7GN__vAXV5yGmPUI7ekccRjo_9Sc4upy9eJJvx3cH3LpTEbLru-27pGc7D7YPRyIGf2omZDsG68mdzuFaeYmaAYIer9_ucPg8YvVDjahoYW-0Z4jGgu0-u_8IDKEVB6EQSlgXr5hAcGnBS_nvu4RNQQJ09JDVGmt3UYZ0QedPAQLboQSSHBqGxu-FuNG8HjQo-u5bW9oDBg5fZoHz_mVtT1aw49SJJSffBi99uzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ArasClient | کلاینت قدرتمند اندروید
یک کلاینت مدرن و متن‌باز برای مدیریت کانفیگ‌ها، Subscriptionها و اتصال‌های مختلف، با امکانات پیشرفته برای تست و مدیریت سرورها.
➿
➿
➿
➿
➿
➿
➿
➿
➿
⚡️
Smart Connect
تست هم‌زمان کانفیگ‌ها و مرتب‌سازی بر اساس Latency برای پیدا کردن سریع‌تر گزینه مناسب.
📡
Subscription Management
مدیریت چند Subscription، بروزرسانی کانفیگ‌ها، نمایش حجم مصرفی و زمان باقی‌مانده و امکانات بیشتر برای مدیریت سرورها.
.arasc
فرمت اختصاصی ArasClient برای Import / Export و اشتراک‌گذاری کانفیگ‌ها با حالت Protected.
🔐
Per-App & Routing
پشتیبانی از Per-App، Routing، Proxy Chain و Policy Group در بخش‌های پشتیبانی‌شده.
🔥
پروتکل‌های پشتیبانی‌شده
VLESS • VMess • Trojan
Shadowsocks • Hysteria • Hysteria2
WireGuard • AnyTLS • AmneziaWG
MASQUE • Mieru • SOCKS • HTTP
➿
➿
➿
➿
➿
➿
➿
➿
➿
🌐
Aether / WARP
پشتیبانی از پروفایل‌های Aether و قابلیت‌هایی مثل:
• WireGuard / MASQUE
• ECH و Fragmentation
• Endpoint Scanner
• WARP Key
• Psiphon و Tor
📊
امکانات بیشتر
• تست و مرتب‌سازی جهانی کانفیگ‌ها
• نمایش اطلاعات اتصال و مصرف ترافیک
• تشخیص کشور سرور بر اساس IP
• Backup & Restore
• Dark / Light Theme
• Logcat و ابزارهای عیب‌یابی
• تنظیمات پیشرفته Core و شبکه
➿
➿
➿
➿
➿
➿
➿
➿
➿
😎
Open Source • Android
👩‍💻
GitHub:
https://github.com/ArasTey/ArasClient
🖼️
Telegram :
https://t.me/imArasTey
📥
Releases:
https://github.com/ArasTey/ArasClient/releases</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/whitedns/1893" target="_blank">📅 17:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1892">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkW_rlSxm91-W1io0MwzAFelI5tyIfMTWcSNUmR6aaks-VvDDpWoPiJm5t0_ypRerTTRgAKNxPLQhiw766j8ThJUpbgdz38Hpu_VavFee035pzQlj93-iYOOHiIcTVpDzccijcbPiOAAghinCNKAsag5upKFBkkEUA_VL0ODuck74bNIxiuRuLZY6dW1K8lq3nqeIDIZ8uvYqSiwH0PsvilTs9XURVZo-0nmfVvsuYMy1pzNcMP_pnomJb8CUnWs_lo2RftcrznZpiHAePGTcyEYYtUFDgryg5zdtyhbiPnpNgSMMc_nOANtqc33jOho4N9sUTky4Adxe6Aa1cGnBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
آموزش جدید رسید!
🥹
✨
اسکن آیپی تمیز با WhiteDNS Scanner و استفاده ازش توی کانفیگ
🔥
💗
از نصب اپ تا تست نهایی، همه‌چیز مرحله‌به‌مرحله توی ویدیو هست
🎀
🎬
ببینینش:
https://youtu.be/GDo6p_z3CAw
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clBTfSpIdtLsUGTD4n9QuZ-3Hofmhz10HXcWJtJjUdI8J_-406ke8fStwDl36OeKNgVDTVWh7_usQLc6pyqeZNBDOzghOAupCcoRx-WZP7W96ZzzAnoshc2ursSqRbUXXjLZgICaEzuGz4YwxXdYcieZrSWCdLcX1k64hHzaX8cPHh-oNTWzCt-OicDZ4m1ZqBWUlKD3etgQ3miffNh3CqnCUDL2OADaLoZJG71Q7pjk0jp9KBkdqfvRrCa1vbZ98YlqCLviw6Me8tQd2QauvYFFwQVz53hhgSH1FLzqlXAFaMD2Kz295AGlt8BeoH5-3_Jk4Fh_yw5w0-nOBgp49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
بچه‌هااا یه آموزش خفن و کاربردی جدید دارم براتون!
🥹
💗
می‌خواین هاست رایگان بسازین و ازش کانفیگ V2Ray رایگان بگیرین؟
👀
✨
توی این ویدیو با Blue Knight Panel همه‌چیز رو از صفر باهم ساختیم و آخرش هم کانفیگ رو تست کردیم
😍
🔥
اگه این چیزا برات جالبه، حتماً یه سر به ویدیو بزن؛ قول میدم ارزش دیدن داره
🫶🏻
🎬
ویدیوی جدید رو ببین:
https://youtu.be/TmHM_yBPOUU
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💬
تعدادی سرور اختصاصی جدید اضافه شد!
دوستان عزیز، برای استفاده از سرورهای جدید، لطفاً از مسیر زیر سابسکریپشن اختصاصی رو تازه‌سازی کنید:
✨
بخش سابسکریپشن
✨
سابسکریپشن اختصاصی
✨
دکمهٔ تازه‌سازی
🔄
فکر می‌کنیم ظرفیت فعلی برای همهٔ کاربران کافی باشه، ولی اگر نیاز به ظرفیت بیشتری باشه، حتماً سرورهای بیشتری اضافه می‌کنیم.
آی‌پی‌های این سرورها اختصاصی هستن و انتظار داریم باهاشون بتونید به‌راحتی به شبکه‌های اجتماعی و تمام ابزارهای هوش مصنوعی دسترسی داشته باشید
❤️</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚠️
دوستانی که از نرم افزار whiteasther استفاده میکنند و مشکل ورود به وبسایت ها و یا سرویس های  تحریمی دارند
:
🔥
با یک سری تغییرات که روی سرور exit chain  یا همان زنجیره خروج  دادیم . احتمالا مشکل خیلی از دوستان حل خواهد شد
🛠
برای این منظور کارهای زیر را انجام دهید :
1. وارد ربات
@WhiteDnsChainbot
شوید و کانفیگ(های) مورد نظر خود را انتخاب و دریافت کنید
📥
2.در تنظیمات اپ whiteaesther به مسیرها-زنجیره خروج و در نسخه دسکتاپ به قسمت پیشرفته - زنجیره خروج  بروید و ادرس ساب خودتون را وارد کنید
⚙️
3.کانکت شوید
🚀
موفق باشید
🙏
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">💬
با از کار افتادن سرویس های BPB فشار بیشتری روی سرور های اختصاصی هستش (شاید براتون کار کنه و شاید درست بشه).
ما سعی میکنیم کیفیت سرویس های عمومی رو بیشتر مدیریت کنیم و از شما هم میخوام اگر مایل هستید به ما کمک کنید.
❤️
تنها راه کمک به ما سرویس Patreon هستش و فقط برای ساکنین خارج از ایران قابل دسترسی هستش.
🗺
امروز به ما ماهی ۲۲دلار بهمون کمک میشه اما ماه ها بوده که هزینه های ما بیشتر از ۱۰برابر این هستشو همش از هزینه شخصی پرداخت شده و تا جایی که بتونیم ادامه میدیم.
https://www.patreon.com/cw/WhiteDNS
یک سرور آمریکا
🇺🇲
جدید اضافه کردیم و سرور هایی که براتون کار نمیکرد رو حذف کردیم.
برای دسترسی به سرور جدید، به بخش سابسکریپشن برید و ساب اختصاصی رو بروزرسانس کنید.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1873" target="_blank">📅 13:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1872">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👀
یه تغییر آزمایشی روی
سرورهای اختصاصی
دادیم
فعلاً تعداد سرورها به
۴ سرور
در این کشورها کاهش پیدا کرده:
🇺🇸
آمریکا |
🇸🇬
سنگاپور |
🇫🇮
فنلاند |
🇩🇪
آلمان
آی‌پی این سرورها
هر ۲۴ ساعت یک‌بار تغییر می‌کنه
تا احتمال فیلتر شدن کمتر بشه.
قبل از تست، حتماً اشتراک رو به‌روزرسانی کنید:
بخش اشتراک‌ها → اشتراک اختصاصی → گزینه «تازه سازی»
بعد از به‌روزرسانی، سرورها رو تست کنید و نتیجه رو بهمون بگید
🙌</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان سلام :
ما برای کانفیگ whitedns ربات داریم
@MasterDnsManager_bot
این کانفیگ ها یک روزه هست ، با حجم محدود
⚠️
به درد افرادی میخوره که هیچی براشون کار نمیده و با یک سرعت خیلی خیلی پایین فقط می‌خوان یک وبسایت چک کنند و یا تلگرام اخبار بخوانند و یا پیام متنی بدهند
این روش سرعتش در بهترین حالت ممکن شاید به ۵۰۰ کیلوبایت برسه
عده ای از دوستان درخواست میفرستند که برای روز مبادا می‌خوایم ، که درخواست رد میشه ، توضیح دادیم که دوستان دلخور نشن
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1870" target="_blank">📅 14:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1869">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AmKF2INEXr2ZyWUJESE0Ck09LG_udroLNFprqRvE-gOD_XqFzqXmhYfifvX9yoZlXh9MiJCMsguWYWfQn7gE4vtKvao7mXqxf0mdRyqJ7tDXI4ggqGYKhqgu1bt54iTZnKRXwmZX8n1WRIwMWIxg4Lh9dudhmR7tDkd5iRbQ05ddZ1LeR2SEVm_PAoJhaf0bgrlYc56OuMsIt5rCcGKu25pQG3h-Ug1bE7jJIs-Bna7E2HoarVsieHW23XEBl0WmEtEB3kiF09C1WL-RMlyDMLKfeGtOeXpLbPEnTutvvRXUpuQAWzXoWq4YYgEXUWfPcGanPSwiwv8AtZ5Z4xLGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه پایان فعالیت ربات
@WhiteDnsResponder_bot
کاربران و همراهان عزیز،
به اطلاع می‌رسانیم که فعالیت این ربات و خدمات مرتبط با آن از امروز به‌طور کامل متوقف می‌شود و پس از این، هیچ‌گونه سرویس، پاسخ‌گویی یا پشتیبانی از طریق این ربات ارائه نخواهد شد.
از اعتماد، همراهی و بازخوردهای ارزشمند شما در تمام این مدت صمیمانه سپاسگزاریم. حضور شما نقش مهمی در مسیر فعالیت این پروژه داشت.
با آرزوی بهترین‌ها برای همه شما
🌹
تیم WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1869" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1868">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مهم "
⚠️
⚠️
⚠️
📢
راهنمای تست اتصال WhiteVPN نسخه 1.6.10
لاگ‌های ارسال‌شده از چند دستگاه، نسخهٔ مختلف اندروید، وای‌فای و اینترنت همراه بررسی شدند. در بسیاری از موارد، کاربران فقط چند ثانیه بعد از زدن دکمهٔ اتصال، آن را دستی قطع کرده‌اند؛ درحالی‌که برنامه هنوز مشغول بررسی سرورها بوده است.
در نسخهٔ 1.6.10 برنامه ابتدا سرورهای اختصاصی را آزمایش می‌کند و اگر آن‌ها پاسخ ندهند، سراغ مسیرهای جایگزین می‌رود. این فرایند در شرایط فعلی اینترنت ایران ممکن است
تا دو یا سه دقیقه
طول بکشد.
لطفاً برای تست دقیق، مراحل زیر را به‌ترتیب انجام دهید:
مطمئن شوید نسخهٔ نصب‌شده
WhiteVPN 1.6.10 (85)
است.
وارد تنظیمات برنامه شوید و گزینهٔ
تعمیر اتصال / Repair connection
را اجرا کنید.
بخش
Split Tunneling
را موقتاً خاموش کنید.
در بخش انتخاب موقعیت، گزینهٔ
Automatic / خودکار
را انتخاب کنید.
اگر امکان انتخاب سابسکریپشن دارید، فعلاً
سابسکریپشن عمومی WhiteDNS
را انتخاب کنید.
دکمهٔ اتصال را بزنید و تا
سه دقیقه کامل
برنامه را قطع نکنید.
هنگام اتصال، بین وای‌فای و اینترنت همراه جابه‌جا نشوید و برنامه را از Recent Apps نبندید.
اگر پیام «متصل» نمایش داده شد، حداقل ۳۰ ثانیه صبر کنید و سپس موارد زیر را آزمایش کنید:
بازکردن یک سایت در مرورگر
ارسال یک پیام در تلگرام
بازکردن یک سایت خارجی دیگر
⚠️
اگر برنامه متصل شد ولی اینترنت یا تلگرام کار نکرد:
لطفاً اتصال را بلافاصله قطع نکنید. در همان وضعیت متصل:
اگر برنامه «متصل» شد ولی اینترنت کار نکرد، اتصال را قطع نکنید. در همان وضعیت، از همان گزینه‌ای که قبلاً برای
کپی و ارسال گزارش اتصال
استفاده کرده‌اید، لاگ را کپی و برای ما ارسال کنید. سپس نوع اینترنت، نام اپراتور، مدل گوشی، نسخهٔ اندروید و اینکه سابسکریپشن خصوصی یا عمومی انتخاب شده را بنویسید.
آیا هیچ سایتی باز نمی‌شود یا فقط تلگرام مشکل دارد؟
آیا حالت Always-on VPN یا «مسدودکردن اتصال بدون VPN» فعال است؟
اتصال با سابسکریپشن خصوصی انجام شده یا عمومی؟
اگر برنامه بیشتر از سه دقیقه روی «در حال اتصال» ماند، باز هم ابتدا گزارش را کپی کنید و سپس اتصال را قطع کنید. گزارش‌هایی که بعد از قطع اتصال گرفته می‌شوند ممکن است بخشی از اطلاعات اصلی خطا را نداشته باشند.
بررسی‌های فعلی نشان می‌دهد تعدادی از مسیرهای اختصاصی
AnyTLS
داخل ایران پاسخ پایدار ندارند. در چند آزمایش، سرورهای اختصاصی شکست خورده‌اند ولی برنامه پس از انتقال به سابسکریپشن عمومی با موفقیت متصل شده است. به همین دلیل تا زمان اصلاح مسیرهای اختصاصی، استفاده از
سابسکریپشن عمومی
پیشنهاد می‌شود.
همچنین اگر از نسخهٔ 1.6.9 استفاده می‌کنید و برنامه «متصل» نشان می‌دهد ولی دیتا ردوبدل نمی‌شود، حتماً به نسخهٔ
1.6.10
به‌روزرسانی کنید. نسخهٔ 1.6.9 در بعضی شرایط ممکن بود اتصال ناموفق را به‌اشتباه متصل نمایش دهد.
از ارسال گزارش‌های دقیق شما ممنونیم. این گزارش‌ها مستقیماً برای شناسایی اپراتورها و مسیرهای مسدودشده استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚠️
🔥
تعدادی از دوستان به خاطر فیلترینگ شدید توی منطقه ای که زندگی میکنند توی نسخه 1.6.9 دچار مشکل شده بودند .
کانکشن برقرار میشد ولی ترافیک نداشتند .توی نسخه 1.6.10 این مشکل به طور کامل رفع شده است و احتمالا خیلی از کاربران مثل نسخه های گذشته به راحتی متصل خواهند شد
دوستان تا ما مشکل سرورهای اختصاصی را حل کنیم فعلا از سرورهای عمومی استفاده کنید
⚠️
دوستان چنانچه هنوز برای اتصال مشکل دارید لطفا با نگه داشتن انگشتتون روی دکمه اتصال لاگ برنامه را کپی و برای ایدی ادمین که توی بایو هست بفرستید
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1866" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1863">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bMnrwKJaUuQy2_PPmB8XMF017tO6_xNds9S2oj10erOPTDNiRAH28rzcmJpJWV75SA-KQHmkb5c03rXWOmqhr6Xd6cAAow8h_3Q1xX58bOLroDFPZQJeVIvv6y_Vs8zHwB33fWhijYueMWV8HuZzsY6rnhq2wPN19uZiMuUl8cG6omkpOpM8fZKxWLnFW20Vpe0GB1V1GH4NtdifcSq6ZABH38S5qzYNkmxnv2d4u2W20qd9_XsRTF4IRRd7M4SMreG2cBpyL1Js9wvsns7QYBOobTO0SMRudZ9CYEuwp0x4UimRS56W28C-OXvdFCrmoJr5WkWjAL3e_WF3LmEK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EPCjSZzm-06Q0r6tgkAUxAdzMD93RmUQCBkHYJlhfZo6C-gsl1d4XoeAcEufSnv9i30CH3DdF_OU7MTbJVOnn7EwIJ4ekJyIBVJMIhQ_yJBdHJd4kvX3Yz1wMrJlW8k9AnxTsloj4Bp_IDaLX8-KlWhXPtBIgZ5djaIMKicv51MgVYaCU3ZW-7YuQsn9_WUU8FQxppK_FbCH5RHi34S-LgMHu4yvBuXoOb5eC6nLOhvtgjnknV_AP6hOOjgJI6uR5ZJcMZGrqctPkvN9mXJ4TXzyGfij_mPEBept0uLUSVJmDqvx_mAuW8NE0nOAllddSyv5MFUfERcpeJrAXFP6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YW2fY844I5kq1aECe2ng6Yprkb1kSb3ZehxtyiUgVqyuQI-ZgGg5SCjVv7kVAgyYxdkyibiUzJRCVEMh0Vvkvlb6ofL7tA8aRzfQTvcDk-mwUCneDQWB24IzkTQePmA4pUXVhTpySSCCLrXl6ZofB0bOkRm3XaSQwPUmctUxWUDK_Ae35PBk50Tj69FlypaEfa-DjwFfspSpko4qpEcZf_FzFgikztWyYzucb8VbdSo6rPzpEXGuPhlIFcq3gUzQshq9PD12i9ojs-hN96Bl5VZvGNEjGcWYgTJUduCT1Fx2ljtTr_x_5WPC3433tnSxFgCW2I03w4aKwbul77etBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-poll">
<h4>📊 الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ اخرین نسخه whitevpn</li>
<li>✓ اخرین نسخه whiteaesther</li>
<li>✓ اخرین نسخه whitedns/coreforge</li>
<li>✓ هیچ کدام</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1852" target="_blank">📅 18:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbxPsbu4GnfDkdrZ3hMsIY3gT2Un5aFY88QnSRmTI8JUL8GnXPz6qfv7Hlz9DcTx133v4lr2mds3QpawchiBEJvWCctChtQmS1r4E1q8CQ9N9UnCB4RKtjOF4A9XgXW_8OeBOV2Ybr4qoZnYQ7MaY_cpryNCMB6nvrgRL7otO-1eq_lQ2EWiscmGX47hRFRyVHoZuYkRKTa6uCnCCUUEpwZgUYkDRCLIMNbp6OAn6W0PoWYU9LvmBwjtEin8Sf7trTHBVn7ANmoI2HiTZD0DRXGywEC8X3RmTqkO4kf44dVS7PSwwph7v0oKf19vtG2b-_ir8JOVok2KoRQZqFnq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.
لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید. نسخه جدید رو می‌تونید از صفحه GitHub ما هم دانلود کنید:
🛡
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.9
💬
بعد از نصب نسخه جدید، اگر هنوز مشکلی داشتید لطفاً بهمون خبر بدید. گزارش‌هاتون کمک می‌کنه مشکل‌های باقی‌مونده رو دقیق‌تر پیدا کنیم.
ممنون که با گزارش‌هاتون کمکمون می‌کنید
🤍</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1848" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1847">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FR4sTIKZCd1z6VWw0tOPGihMj5CQlazx6u9bBZdIzEHw4kRMU_WIoKC6FhgQa3lGPSmEhrL8s8mZCgEtNHJAg1Mxx5U3ixKPzFHXqOOie00KpxHn2sFOfJpBV1kpfoGm4YUaRoCZUwZ5DQ-qudIQ5lYerywrqRLE2W1ix07MZHNWtHTwEvOnc2CZN4uRdse0lv2XF76uEV-P6_R4Aejyulotw8I2rTWexQqbA-zv6Ram-R5pFvCUM6HCNZq6s8_m-Xxpd5hiVTyLgQ2UFV8Kgbdcgi003XMyVBPyu52zJZD-Ks8lNrsZWM9TtxMYGMYwZAkb0g05lRPlrEhVGhXJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی whiteaesther desktop 1.9.7 pre-release
⚡️
اتصال باید خیلی سریع‌تر شود
کلادفلر در همان جواب ثبت‌نام، آدرس دقیقی را که به دستگاه شما داده اعلام می‌کند. موتور آن را می‌خواند، ذخیره می‌کرد، و بعد نادیده می‌گرفت — و به‌جایش حدود ۲۵۰۰ آدرس را یکی‌یکی امتحان می‌کرد تا یکی جواب بدهد.
🔑
و مشکل «دیگر نمی‌توانم ثبت‌نام کنم»
اگر تا حالا پیش آمده که بعد از چند بار نصب مجدد یا اتصال ناموفق، برنامه اصلاً نتوانسته شناسه بگیرد — این همان بود.
ثبت‌نام همان لحظه‌ای که سرور جواب می‌داد خرج می‌شد، ولی تا چند مرحله بعد روی دیسک ذخیره نمی‌شد. اگر وسطش چیزی قطع می‌شد، ثبت‌نام رفته بود ولی شمرده شده بود. و چون سهمیهٔ کلادفلر روی آی‌پی است، همین می‌توانست گوشی روی همان وای‌فای را هم از کار بیندازد.
حالا اول ذخیره می‌شود، بعد بقیهٔ کارها.
🛡
و یک حالت خراب که دیگر ممکن نیست
قبلاً اگر با وایرگارد وصل بودید و MASQUE را امتحان می‌کردید، هیچ‌کدام دیگر کار نمی‌کرد. ساختار جدید طوری است که این وضعیت اصلاً قابل ساختن نیست.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.7
⚠️
نسخهٔ آزمایشی است — در فهرست به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد.
شناسهٔ فعلی‌تان خودش منتقل می‌شود؛ کاری لازم نیست بکنید و چیزی پاک نمی‌شود.
💬
اگر اتصال سریع‌تر نشد، یا هر چیز عجیبی دیدید، بگویید.
@whitedns</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1847" target="_blank">📅 12:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/BKxBNi7uhFc0zLM3x8Oh1tE_8mZ5JQV-2p7CfDXUg4PsPq8qsBJoSvbGqwYT_T-AUtV1PDO1EjoCmgruybDTCEtAzJIHhPxmcA5il5yJqFfzu6MYa_v8thgvxaHkIowEBtAPFeSSjVi7ZbfGGtlLuKuEvV89XoBFln6gXeX3C21JGBZX4TTkzQUrzIOnGaD2Mw8oXZBMRJkc2NZ9d6Xvb6FVQNtavJHeDcQ1TIcbRYmmWNl8Tb1oGKTM5ef05UzIMTJZhhOBshR9it4xvTBnh-hYa6IJlSiuUeAj1IQjVTLZVByiABI8ZTdbQdK1-nOd4atYFk1eXuzS1wx8EsljCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/aRE4XLrAt9kTmKt7oJNwSdxjwBys3qwXm3ZmMlMQQxrYyqPFobaE71dwyWBCSHlq5rcDbShpR4zudXE35Kiom2aT4pqrU69fZu-pqh1X474rSen_ikwxdpm-JMyWMgtABpFobf86J4VSZ3RWS5Nh7UGm0_bLXaWlOs66OLMC4o5wzYDhtTz6k_pkoq75C1gg7IAa1kvS-IaIeGSV5YRpOejhq1Kyl2btfnhvnz8brNgXU3uCk9Gqad-STriAf1MrU_p7huyTjzOTPgGeyu6FE8EDykJ1Q8MkcBtVIyPs89L4sikTe4PRfFRV-ecC_oosnW6OegJ4kNfqPNMmckNa3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚠️
یک امکانی که توی اخرین نسخه ازمایشی whiteaesther موبایل و دسکتاپ تقویت و بهینه سازی شد - امکان ست کردن dns بود که تقریبا هیچ کس بهش توجه نکرد جز یک گروه خیلی کوچک به نام گیمرهای عزیز
😁
😃
از این امکان استفاده کنید حتما خیلی از مشکلات شما را حل میکنه
🤓
لیست dns های عمومی :
۱. DNSهای عمومی و معمولی
Google
8.8.8.8
8.8.4.4
Cloudflare
1.1.1.1
1.0.0.1
Yandex
77.88.8.8
77.88.8.1
Quad9
9.9.9.9
149.112.112.112
OpenDNS
208.67.222.222
208.67.220.220
AdGuard Unfiltered
94.140.14.140
94.140.14.141
Control D
76.76.2.0
76.76.10.0
DNS.WATCH
84.200.69.80
84.200.70.40
DNS.SB
185.222.222.222
45.11.45.11
AliDNS
223.5.5.5
223.6.6.6
DNSPod
119.29.29.29
—
Hurricane Electric
74.82.42.42
—
Comodo Secure DNS
8.26.56.26
8.20.247.20
Neustar UltraDNS
156.154.70.1
156.154.71.1
LibreDNS
88.198.92.222
—
360 Secure DNS
101.226.4.6
218.30.118.6
OneDNS
117.50.10.10
52.80.52.52
Quad9 Unfiltered
9.9.9.10
149.112.112.10
DNS4EU Unfiltered
86.54.11.100
86.54.11.200
۲. DNSهای امنیتی، ضدتبلیغات و خانوادگی
Yandex Family
77.88.8.7
77.88.8.3
Cloudflare Security
1.1.1.2
1.0.0.2
Cloudflare Family
1.1.1.3
1.0.0.3
AdGuard Default
94.140.14.14
94.140.15.15
AdGuard Family
94.140.14.15
94.140.15.16
OpenDNS FamilyShield
208.67.222.123
208.67.220.123
CleanBrowsing Security
185.228.168.9
185.228.169.9
CleanBrowsing Adult
185.228.168.10
185.228.169.11
CleanBrowsing Family
185.228.168.168
185.228.169.168
Control D Malware
76.76.2.1
76.76.10.1
Control D Ads
76.76.2.2
76.76.10.2
Control D Family
76.76.2.4
76.76.10.4
DNS4EU Protective
86.54.11.1
86.54.11.201
۳. DNSهای رمزگذاری‌شده (DoH و DoT)
Google
https://dns.google/dns-query
Cloudflare
https://cloudflare-dns.com/dns-query
Quad9
https://dns.quad9.net/dns-query
AdGuard
https://dns.adguard-dns.com/dns-query
Control D
https://freedns.controld.com/p0
NextDNS
https://dns.nextdns.io
Mullvad
https://dns.mullvad.net/dns-query
DNS.SB
https://doh.dns.sb/dns-query
AliDNS
https://dns.alidns.com/dns-query
DNSPod
https://dns.pub/dns-query
OpenDNS
https://doh.opendns.com/dns-query</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1845" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💬
کاربران WhiteVPN روی اندروید
اگر اخیراً داخل برنامه با مشکل اتصال یا اختلال مواجه شدید، لطفاً برای کمک به تست و بررسی مشکل این مراحل رو انجام بدید:
1. ابتدا گوشی رو یک‌بار
Restart
کنید.
2. وارد تنظیمات گوشی بشید و برای WhiteVPN گزینه
Force Stop / توقف اجباری
رو بزنید.
3. سپس
Clear Data / پاک کردن داده‌های برنامه
رو انجام بدید.
4. برنامه رو دوباره باز کنید و اتصال رو تست کنید.
در اکثر موارد بعد از انجام این مراحل مشکل برطرف میشه.
اگر بعد از انجام این مراحل همچنان مشکل داشتید، لطفاً نتیجه رو به ما گزارش بدید تا بتونیم دقیق‌تر بررسی کنیم.
ممنون که با تست و گزارش‌هاتون به بهتر شدن WhiteVPN کمک می‌کنید
🤍</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1844" target="_blank">📅 09:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vN1m02iInzLH827js4q82QA2lVVmDErISugT4SyZgHQqE0wcY5LOZLHanVRpSzqyaF9tN8wSB4a-kWlkAgUZauSx8mk_sKwhUT4IpXNS8dKUiqjWyP0lKnIHWcW1Q0vy5CglG8X7mxs5QcD4_cODClJxm043DQL-l9vUILcYC0MqUK6ha_Agqsd4jLQgtcIHl2GtUjf1vLQYvv_Nr9XPWek0-JhV93FOiUdkUceis_oGR0Or48tnoBjXkDCczZUFo3FAU4JsUxzf8QK-sQq9eBZ2Ej-H7V5McC1yIEZYLboTrLX6McfGN0adxCdMGRzIoAbn-_4u6KzRS_e5AXJPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ازمایشی whitevpn desktop1.0.23 pre-release
🧪
این نسخه آزمایشی است، نه انتشار رسمی. برنامه خودش آن را پیشنهاد نمی‌دهد. اگر نسخه پایدار می‌خواهید، روی ۱.۰.۲۲ بمانید.
چه چیزی تازه است:
- فایل نصبی
.msi
برای ویندوز — نصب در Program Files، میانبر منوی Start، و حذف از تنظیمات ویندوز. نسخه zip هم هست.
📦
- گزینه «همه سرورها» — اگر چند سابسکریپشن دارید، از میان سرورهای همه آن‌ها انتخاب می‌کند.
🌐
- پروکسی سیستم و حالت تونل حالا در منوی آیکون کنار ساعت هستند.
⏰
بیشتر از همه به تست فایل نصبی نیاز داریم، چون اولین بار است ساخته می‌شود. اگر ۱.۰.۲۲ را دارید، این را رویش نصب کنید و ببینید درست جایگزین می‌شود.
اگر مشکلی دیدید گزارش بدهید — اگر بتوانید محتوای صفحه Logs را هم بفرستید کمک بزرگی است.
📝
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.23-rc1
@whitedns</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1843" target="_blank">📅 06:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1839">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-poll">
<h4>📊 خیلی از دوستان میگن الان یکی دو روزه اختلال شدید دارند و برنامه های white براشون کار نمیکنه . شما چطور؟</h4>
<ul>
<li>✓ هیچی کار نمیکنه</li>
<li>✓ همه کار میکنند</li>
<li>✓ فقط whitevpn کار میکنه</li>
<li>✓ فقط whiteaesther کار میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1839" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1838">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qr2Rp-nN444LQ__ygZNfvk7QqpwFy0r0S5aNHvCkU_G9UvLLOL8wGhItMfJoMxaWH-bXiCkuIqC8RNbf_oPZ2Q7mjqaoYivdFjqlz1XpTeOVdDB-xwq4bOxDo198MwB5SzTAXwmZr-vTbUg8oo_JZoOto223FfL1Eubcm7p8w3Q61BCGhKwhPrMXXgwJX225uZ3ni9Do9AzvTa8NtNNwNiV-r1p7SHeGa7ZuK_0DH2pNLkSULUn9D1x1dHzF3guF19XvJ3KafewWOiXJfa1nvKgbMG0rgLooJ7nP06xVSdgZvanOygJTEh17l91sKX-wh15lHe4QHWKkWRXL-AA3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther mobile V1.9.4
pre-release
الان DNS inside the tunnel روی همه حالت ها اعمال میشود - قبلا این امکان فقط برای حالت proxy بود.
🌐
چی درست شد
▫️
فیلد «DNS inside the tunnel» بالاخره کار می‌کند.
✅
تا حالا هر چی وارد می‌کردید نادیده گرفته می‌شد و همیشه از
1.1.1.1
استفاده می‌شد. اگه با سایت‌های تست DNS چک کرده بودید و جواب عوض نمی‌شد، دلیلش همین بود.
اگه خالی بگذارید مثل قبل
1.1.1.1
می‌ماند. در حالت chain اعمال نمی‌شود، چون آنجا نام‌ها رمزگذاری‌شده و از سمت خروجی پرسیده می‌شوند.
🔒
و بهینه سازی موتور و routing , ......................
نصب:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.4
@whitedns</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1838" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1837">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tpXjLdK0SBzpi-C0IvOO8-sjKiZ0YretVawFfyDt_rfxV1EuHzjPtmkje4eFPsqL8wb1ys4Qh-McrLwwaL-pPn8raWuqFO8zUDi1MCDzOyL3Jvk5SugKEzuQUc34WcxKOSbc5ts8l0l5RKznSDySJL6EWfMLdvgTLCuiEuLIyRtQ3Y1hg-ldqccQzPIlPQSyEp4lSbKKhfQWeXibiYuDbWXc3DW9Wa55JpLbMciP_eFscbqWLt0fwkTIvC1L7XhzLlqiGNYzlr83MQrEt9WZzgfcYrY_YyIb5OgzRPluPa-kHQgUNfbtNU2Asl-a2bNeGZ2DsHZgIbsdutCutmLvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther desktop 1.9.5  — رفع باگ پورت و یک سری بهینه‌سازی روی موتور و .........
🚀
اگر بعد از هر بار اتصال، پورت پراکسی محلی عوض می‌شد و تنظیماتتان به هم می‌ریخت، این نسخه همان را درست می‌کند.
✅
پورت دوباره ۱۸۱۹ می‌ماند — هر کریری که وصل شود.
🔒
این باگ از نسخهٔ ۱.۹.۲ به بعد دیده می‌شد، از وقتی دکمهٔ اتصال شروع کرد خودش راه خروج را پیدا کند و سایفون یا تور بیشتر برنده می‌شدند.
🕵️‍♂️
📥
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.5
⚠️
نسخهٔ آزمایشی است — در فهرست دانلودها به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد. با همین لینک بگیریدش.
اگر پورت باز هم جابه‌جا شد، حتماً بگویید.
📢
@whitedns</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1837" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1836">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM0z9-T2kCXQWM9SKO1y1cKzDyETdgdNE2wJyWu8lzRJXhIvM_NsVrW3_YL0zF8Lk_StFkf4fT9SAkhG_W3aWRg5boW7NsIu_Xhu8xP1-Gd7jjQwA__Ybp6zsA7wDlTnTs6-Sn8-2WdOgPiir1S1lnoZ30ykq3deBVEmuz0PHQbSsvmiiTpeDUw5I-B77U35srqK1bs67Qd30A3oM1b4295DRCH0ML7zOZpcTHB1bFFKl_G3_ggod2nveKMFnzhYE6yJgLKhgiWGFKYRbnIt29WM8V9zW15nFObrqXvw9kUDDbpkyznHAEUKUjXwa65XD4m92w-fwJ82E_SmgGsE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه
WhiteGame
یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور ویژه برای بهینه‌سازی پینگ، سنجش کیفیت اتصال (QoS) و رفع چالش‌ها و محدودیت‌های ارتباط با سرورهای بازی طراحی شده است.
📊
این ابزار با شبیه‌سازی پروپ‌های شبکه‌ای و سنجش شاخص‌های کلیدی و نوسانات پکت‌ها تحت وب، به گیمرها این امکان را می‌دهد که وضعیت زیرساخت اتصال خود را پیش از ورود به بازی ارزیابی کنند. جای دارد گفته شود که تمرکز ما روی
UDP
است، همچنین قابلیت
Test Real Path
در اپلیکیشن، پینگ واقعی و دقیق شما را در زمان Matchmaking و InGame نمایش می‌دهد .
🔐
پروتکل‌های پشتیبانی‌شده:
Warp | WireGuard | Amnezia | Xray
✨
ویژگی‌های برجسته:
• Packet Loss Injector
• Jitter Plus
• Gaming DNS Spy
• Optimizer Warp و WireGuard
⚙️
علاوه بر این، ابزارهایی برای ساخت و مدیریت کانفیگ در اختیار شماست؛ با استفاده از بخش Generation برنامه، تنها کافی است Public Key سرور خود را قرار دهید تا خروجی موردنظر به‌صورت خودکار تولید شود .
📉
همچنین در مرحله تست آزمایشی (Beta)، حدود ۳۰۰ نفر از کاربران با استفاده از ترکیب Warp و پنل BpB توانستند میزان Packet Loss خود را در شرایط ناپایدار کنونی به نزدیک ۰٪ برسانند.
🤝
امیدواریم با بازخوردها و پیشنهادات شما، این پروژه را روزبه‌روز بهبود ببخشیم.
https://github.com/TaJirax/WhiteGame
@Whitedns</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OdEsuYxuxuyWndhwaquZ7TYW2YGj6AJgxWpivMin-24D4GmI4uvbvzGXYx-bjnENa71ayMHUyf9qJVl_-MwywRd-euadSZjLT9i5ti-l-qiSN_3CjJtZ6OdBPii2c8A3nhWUlTI46O0l50vyZYvicYUDtyh5CoS555oaSzuw0P5BnmH61j9756Aar18iIVxFRHzjtQgIguhlpvi_2uvlXiV2CwM8BApTLHPnweRGB4rm8OeSsg55jZP-mJxEmLIm0yYhwLojVyB9o82tUNHJsiwr11nX0EijDyGaWVCI5kaMqp-D7j71fTa7PPJoz3Ja8h5uWkMgchcnRDbGLCsqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1833">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cbu73r4ayIWjAvbcz7rrQQYG8gcP3xUxpvm5CxO1mYBl_8Bcs6wAvmG1xKgtt87lI6JVNM4wvbkTW8N0lDOMVqUKFvb6MiJh9mDB3Mp00HN5Z73Nga0W2lgQG0ClwcfxJZ6VeZZysTOcGbb9UYEP86hZ8TBy1TukpKpXtUYITrYxYkenV3EjYs4Pfecox5cpeN6vpRm51keW4a0uJIpiYluCkSYLlLeehtf2PvCcjiw1kKhBxwomyaHjsA-DBPFa6vfOqdOSEtOCJur9Nrj-6_rVktHQgackpmBFdxx22GXXGJ_EqdYKOLhFhP6CEh0GBXQqe4hByU34D9ZEYnkbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1833" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1830">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel (Orihost).rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1830" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1829">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsaLN2RZubNeuLVxPac0ZH_mnCvBqlg-fh29D_V-l0Mq7kHu1h-VEb1inRibKw17BZNTC2WA5eFl8bHrgaJKY-JAYD59ku_TCeCkMP6RZ32mxE7e3DFersqEp4qleW-3_7AfWJ3q_X1Nx_vKNYGDF_1W-dHuxfIP6JIrmvecclPn8C3rJk8ootsf1isaARoTfappFDRsxteUCd9HeUS56w8VvDdj8LxWklWvVoHsRtat-5tHu7Gwj0MwwlmNAJexmFSd8JScpCkQ447kz9YTbsF7fkGzbsxpmURgHgY89S7jw8y33qQ_BJCZCwsF1zfIXhnGSYOJpl_JBHvd6cEFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1829" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1823">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.9.3-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1823" target="_blank">📅 14:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1822">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jjMcjTYfjb1EymUCU7YL3VbzP89FUy2BY1JdyStWjF9JRnl3jHOaXxGWtBsrOFwnZJlIeiRXpEnJsE3qfNZ96nGdf0l6iOdarjgjWSWoJ_C9uk4Q91nbH0e5hQHwdqXimqFfoeZitruIQvPCr2E3wVCqfB7MSRjXkgeaUS2W-lhUZ2ozdYZjBiOUeAzlim-3rs7iSydpEFWv3ZP0ZIEhJdSrs_n4O74zQ6aU-mCziw74OYGjWRyILPyE_NGsM9cghMQ8bgH36-hSLgtdtLEnxWIcCnOl9lEy1Q1m-KpYnpdhWSJP7zFqV3q-JMcpJHFgXEjJsNI84rHvJwDT9v2yOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
Mobile 1.9.3 — نسخه پایدار
🔥
نسخه پایدار 1.9.3 منتشر شد. برای به‌روزرسانی می‌توانید از قابلیت جدید داخل اپ استفاده کنید یا فایل را مستقیماً روی نسخه فعلی نصب کنید.
برنامه را حذف نکنید تا هویت و تنظیماتتان حفظ شوند.
قابلیت‌های جدید
آپدیت مستقیم از داخل اپ
کارت «نسخه جدید منتشر شده» حالا می‌تواند فایل به‌روزرسانی را دانلود و نصب کند.
این قابلیت فقط زمانی فعال است که:
پوشش اتصال روی «کل دستگاه» باشد.
فایل با همان کلید نسخه نصب‌شده امضا شده باشد.
ابزارک صفحه اصلی
بدون باز کردن برنامه، اتصال را برقرار یا قطع کنید. برای افزودن ابزارک، در Settings دکمه Add را بزنید.
هنگام جست‌وجوی مسیر نیز دکمه قطع اتصال در دسترس خواهد بود.
مشکلات رفع‌شده
مشکل نسخه 1.8.0 که ممکن بود برای یک هویت دو رکورد نگه دارد، برطرف شده است. اگر نصب شما در این وضعیت گیر کرده باشد، با اولین اتصال خودکار اصلاح می‌شود.
جست‌وجوی طولانی finding a working route اکنون محدودیت زمانی دارد. این فرایند قبلاً روی شبکه‌های دشوار ممکن بود تا ۲۷ دقیقه طول بکشد.
هنگام جابه‌جایی بین وای‌فای و دیتای موبایل، تونل تا جای ممکن به شبکه جدید منتقل می‌شود و از ابتدا ساخته نخواهد شد.
اتصال MASQUE in MASQUE اصلاح شده است. اگر روش اول برای هاپ داخلی پاسخ ندهد، روش دوم نیز آزمایش می‌شود.
تمام اصلاح‌های نسخه 1.8.1 نیز در این نسخه قرار دارند.
روش نصب دستی
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.3
فایل مناسب معماری گوشی را دانلود کنید.
اگر نمی‌دانید کدام فایل مناسب است، نسخه universal را بگیرید و آن را روی نسخه فعلی نصب کنید.
در صورت مشاهده مشکل، از مسیر Settings ← Diagnostics گزینه Send diagnostics را بزنید و گزارش را ارسال کنید.
⚠️
@whitedns</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mwiM6jaCO419wPuHlYdORlG1ERfnNJDHcjb3Ld1CtO4Apjn0dwBbOPuH0pMymKAvyqKo645sZviQdUz0SX0xAS9bXVUSTGYX-Pv48rHQVhRqf4fvThJaRAsPNcqw-5jlO3q2McmdYv9z9hKlj_a0v9tWGC6jbOW5dWNyetiSczW8YI9GvAyIe5DFSKrrSG8Nl2BvI5rKCvRIisTidVch2DRs13nEA1XvjzlsMmXFe4pw7mNP8_aCtfwbNbRQT9lYhmlKG973NNKEJpQo2jahgyzP2J6Rh6ij7uQv1QOm1szMPuS79piqnu7x01W9UqhivkKlqD12RvnxKvqLhI4suw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/whitedns/1821" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1820">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NoF8Y5z_XeGSTobHxSF1WXSwoZzTktaHe2oGuylBD7kvsfCmpm-AKV0sl2skCeXZs0wWYdFqgT0xZb3o-tdenJ0sUm4G33oUunsA54Air_RJarTi_NTWkKTgGF7o4HHUQUB8-NIxiVzNNjYoVXGRCkqE9S5PoOuXuMFDby_GPNcYGSSo5OeBuG5rkSFbEAIMO3cNssJsyHmL68Y8EBw5-lSNclmX5mLAiyjnyPZg1pi9ZvDm7laxE7ACntp_x15rLEd4FR7KnLC_hWPqgx3el9BQVkN6IDIodghmbNjRG_oEXSE4E0h4V8MptRAz6DE018Qt3drUDO3NLTZcGMrb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
CottenRouter v1.2.13
منتشر شد!
سریع‌تر، پایدارتر و آماده برای ترافیک سنگین
⚡️
• رفع مشکلات نصب
SlipGate
روی سرورهای تازه
• جلوگیری از Down شدن Router هنگام قطع نصب یا SSH
• رفع تداخل Domain و Port بین Backendها
• امنیت بهتر
CottenDNS
و
StormDNS
0
٪ Query Loss
در تست ۵۱۲ کلاینت همزمان
• پردازش بیش از
۲۲K Query/s
• بهبود TUI، خطاها و سیستم Purge
✅
آپدیت مستقیم بدون حذف Routeها، Backendها و تنظیمات قبلی
💻
GitHub
https://github.com/TaJirax/CottenRouter
📋
لیست کامل تغییرات
v1.2.13
https://github.com/TaJirax/CottenRouter/blob/main/docs/releases/v1.2.13.md
@whitedns</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1820" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/C8X0UOTibpijzEvCF_Q-_wdndDlRytC_EMYePB03mfUalsqaI64SwQRpV2YBWU4ylstYSmNnceDEMEjX9wTDysdBCfV6bBf3vdD-cTRwBOsQwoS9yxDgAk_7oF7KRpiPUhd55C4OkX2rjDD1TBtINLyHxM2ocxFPFK695G-f1zXSx7WjEKU0Lu0t18PY_JrVXUzPCCzw1vkDxOK7BPTJapVam1DBwgs73gpwNkhcafOiU8k5Ms3oCQdYfgsdVvYc_TtFigsVVkfKjZnXx4YfgmfEzU1lCL2o0tGIemFl5FCU3J88jxnkGh0PwDREZAc1bHhVWPpYGIktP5ZaNNx7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6kqKoumAeGevhbqfvvvRer6egUDAabvldU3WieBzTKQNngLkNUY563VFbsGM0Y6WGdMWwfgcUGOO0B4pgbdrrv0Oe1ZaerSYuKT7wQ_RlK4ZKL9UhdsAFQrQeXm0IOyPUkpzeucthuj48_2oHynaQQN9ouknuNa_vMgeUscriGxO3EVyQRLd5F2IEFsjJOTMXjrM1aHIN4U9nRPLzvDcZI3dsqfc_tfC_A00P7Fj2VnmXLqBa1b4QBq7A59mMs8WJXOwotWnp1ZpxsoVZWHypn5BHcBobHYZN4WcEj7E3xDdAJ7uJ907K0WOwYhg00uY3ASN9rz8LPb8rsW6nvKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qMuGAjw2HxmPA8oMk1HVCvhsHgE6sdo-MK0dtQeZGVsDjsz9csDCZuMSLPXCEfczcn1_Er_TCjTwZczxVN63tAv55U3imReZyEjc3AKZDCZXiMueO0KKHGBdWzVb19Cs1jejZCD57KYc9SE56sNZl6CrljWdjaU9mr0RJCLnYFguZIzQuKkrltTBx4SpHZxqE4osEI_aRdqxLp6qn2YIHDgey_Oje1PMv_qU9mhIcM62UOxik60p6qRmjt_JUmgf1pOmCeyZZf3CDZabNI1uD53SCDu2Pg6gAJtWUcLfg6t__1Fh8op0t5Kj782JOH71_DgXyN9U2ihkcBUnVD_Taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AVzRob3YxQnh4ED5wIM-UsmtqG1RwT2C_Xu1IXZtq2Gfg8-un0-iUyhtzvNhOQXGgimqGR33ztrHcZO-T-p36JysRPaAdAKPBhDRK_SsQMGPw-bNHJhnutP8bPxnF69UTYXKQrU9BqhJw_E8y8LHWiDS9SFjaVLTRZUoh6hv3j7SprlLdXdu36C2ogvXl2gECXEvp_OuHq_v0Xhbkma8xoMow4QEkuY9ffAMV5CBEo3zeWzcOHmpbMPlJXEj1X0GjM-NJGdnm5-ddnJDpj-SXSc54qGw10Su32vh9_pr4zs67cYvMfmJgxcR_JbaTmfIxBgxe6ts64fbpttHdtvYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1805">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">💬
دوستان ما هرشب سرور های اختصاصی رو روی WhiteVPN بروز میکنیم تا از فیلتر شدن سرور ها جلوگیری کنیم.
متاسفانه این‌چند روز سرور سنگاپور رو نداریم ، توی یک شب ۳۰ ترابایت مصرف شد و هزینه زیادی داشت. وقتی خاموشش کردیم، دیگه سرور سنگاپور ارایه نمیداد.
باید دوباره موجود بشه و براتون یکی به زودی میسازیم.
🔒
اگر براتون مستقیم وصل نمیشه، به یک سرور عمومی وصل بشید و اختصاصی رو زنجیر Chain بکنید تا آی‌پی ثابت بگیرید.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1805" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1793">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CVyRFfbw6V3jgpQk35j5vFyAr4l5bTnPi_mj67dXJTWTE0y6QaeFtDA982PKJSIG0MABuN8-YT2UdkFW9BnJI9j2nymUdDyHjPJUi7Q3j6R5mwOxtd1hb-Xuxs7Mzq9Xc2j_0ruyaohBOFIXUKLr-q-QG1jV3aIMhUU77YSMdC7nKXqTGdTQswYH2ANOc2-eD2ykMPCJQTcbguRIbjX_dN4pv441xNTm7fZ_agRhYg8XRsTaGVlp0yYEyKxXqyIw5d4qEqbXyAkTgQ1QxC-hmRLURUrmoLmBCiML3mrwboCXHmwcyI1eO2OhaSMt4n6wFgRCNTobKz8sv6Te9mlyCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر به هر دلیلی نیاز به کانفیگ (cottondns,masterdns,stromdns) برای اپ
WhiteDNS
دارید از ربات زیر میتونید با محدودیت حجم و روزانه کانفیگ بگیرید.
⚠️
این کانفیگ 1 روزه و با حجم 0.5 گیگ هست
در حال حاضر تعداد کانفیگی که میتونیم بدیم خیلی محدود است و فقط با تاییدیه ادمین برای شما ارسال میشه
⛔️
لطفا اگر اشنایی ندارید و کنکجاوید و یا میخواید ازمایش کنید و... درخواست ندید
@MasterDnsManager_bot
WhiteDNSاپلیکیشن
دانلود اندروید
•
دانلود دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/1793" target="_blank">📅 09:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LPqUL0GZeVf_o4qc5kXVPSflApjW8o9s7l3OZz708Ujbdb0BIfNfsQYJtGw_x_R1s9QkdueMcgVQWRRzhm5vczIPbaWX_8kzD1YqJJJQgAZ-3iQDE-Ck2PuxKlEYw5CluObR2Sw5H2arp9tb7Xmxhx9B5ETvbXIFSfeeezZeHBUtqRsGC89Cw0NIdmHt6Ij_7ZT0X-5wKgEcbFuw4H4YvhZb4FiQUAq15au8oJcilwuAYOYo9w6UhT0vAmUs02S0gW4EsEJ7PNLeFVVvh3APyaYZH8J3jBDzLcu1EBwNpGnbE72YJNUe9c9_bfHJ2ev8E8jjtYH5XQboNluqL43ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
🤖
قابلیت جدید : (نسخه ازمایشی )
⚠️
⚠️
⚠️
گفت‌وگو با هوش مصنوعی در ربات
🔥
WhiteDNSResponder V.5
نسخه ازمایشی حتما باگ هایی دارد  و  دچار اشکالاتی خواهد شد که با پشنهادات و کمک شما هر روز بهبود خواهد یافت
👀
از این پس می‌توانید مستقیماً داخل ربات با هوش مصنوعی گفت‌وگو کنید، سؤال بپرسید، متن تولید یا ترجمه کنید و درباره موضوعات مختلف توضیح بگیرید.
این امکان جدید به صورت محدود و با درخواست کاربر فعال میشود.
⚠️
@WhiteDnsResponder_bot
🔐
نحوه درخواست دسترسی
1️⃣
وارد گفت‌وگوی خصوصی ربات شوید.
2️⃣
از منوی ربات گزینه /airequest را انتخاب کنید.
3️⃣
درخواست شما برای مدیر ارسال می‌شود.
4️⃣
پس از تأیید، دسترسی به‌صورت خودکار فعال شده و نتیجه از طریق ربات به شما اعلام می‌شود.
نیازی به پیدا کردن یا ارسال شناسه عددی تلگرام نیست.
🔹
روش استفاده
پس از فعال‌شدن دسترسی، سؤال خود را بعد از دستور /ai بنویسید:
/ai تفاوت DNS و VPN چیست؟
یا:
/ai یک متن رسمی برای درخواست همکاری بنویس
🔹
دستورات کاربردی
/ai سوال شما
شروع یا ادامه گفت‌وگو با هوش مصنوعی
/ainew
پاک‌کردن گفت‌وگوی قبلی و شروع مکالمه‌ای تازه
/aistatus
مشاهده سهمیه روزانه، میزان مصرف و تعداد درخواست‌های باقی‌مانده
📊
محدودیت‌های فعلی
• سهمیه روزانه براساس تأیید مدیر: ۵ یا ۱۰ پیام
• حداکثر ۳ درخواست در هر ۵ دقیقه
• حداکثر ۲۰۰۰ نویسه برای هر پیام
• نگهداری موقت چهار بخش قبلی مکالمه برای ادامه بهتر گفتگو
• قابل استفاده فقط در گفت‌وگوی خصوصی با ربات
• سهمیه روزانه در نیمه‌شب به وقت UTC تمدید می‌شود
🔒
امنیت و حریم خصوصی
• هوش مصنوعی به سرور، فایل‌ها، دستورات سیستمی یا اطلاعات خصوصی تلگرام شما دسترسی ندارد.
• متن مکالمات توسط این قابلیت در پایگاه داده ذخیره نمی‌شود.
• تنها شناسه کاربر، وضعیت دسترسی و میزان مصرف سهمیه ثبت می‌شود.
• لطفاً رمز عبور، اطلاعات بانکی، کلید API یا اطلاعات محرمانه ارسال نکنید.
⚠️
این قابلیت فعلاً به‌صورت محدود و آزمایشی ارائه می‌شود. درخواست‌های تکراری ارسال نخواهند شد و در صورت استفاده نادرست یا ارسال خودکار پیام‌ها، دسترسی کاربر ممکن است غیرفعال شود.
🤍
WhiteDNS — دسترسی ساده‌تر به ابزارهای کاربردی هوش مصنوعی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1790" target="_blank">📅 15:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1789">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✍️
موقت
اگر روی ویندوز و یا اندروید نسخه قدیمی دارید
⚠️
⚠️
ویندوز :
گزینه reset app data را بزنید و بعد uninstall کنید و جدیدترین نسخه را نصب کنید
اندروید :
حتما ورژن قدیمی را uninstall کنید و ورژن جدید را نصب کنید
@whitedns</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1789" target="_blank">📅 04:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✍️
موقت
برای جمینای و بقیه هوش مصنوعی ها بر اساس تستی که کردیم روی سایفون و تور راحت باز میشه - اگر تور و سایفون مستقیم وصل نمیشه اول با اتر وصل بشید و بعد خروجی را روی سایفون و یا تور تنظیم کنید.
در ضمن اگر روی یک اپراتور جواب نمیگیرید حتما حداقل یک اپراتور دیگه را هم تست کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/1787" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1785">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 امشب ساعت 8 به وقت ایران لایو بگذاریم جواب سوالات را بدیم ؟</h4>
<ul>
<li>✓ بله😍</li>
<li>✓ خیر😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/1785" target="_blank">📅 14:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1784">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nGF2vQU6Q9_292ep0o252AlX_JSpnWPBksmw48BbKgbpuvIFtKTCKRwUZXvQLBMAPqwNlGnJcOCkyv3A84y0Y89M0CVBnRbun6Dqql79sSRCdZqwqUKmnU61RRTHsJx7uCfjS8l9F9UQcXRks2DE51hfPXOj0iTNl1WVq1JwJKqihZNnhegIm3ZmiZFJE4CUG3Fah8xzh9_2rzlmqZNk-40Uzxbh0Cn-aSJpTBx66K3Q7-WTNJrukF77BNiu5nr757J1ZflfoEzX4ZauLEoA-FnnakEZHNZWME5OajXf-47ZG-glWXoVH-ymP0X8iHD6m2qC7uJZRoHomG1PeTlzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/whitedns/1784" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1778">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gIY4eKIG11WRx-B71BLAUmAFuI0w24ERolWi_j-LdvjgsF9-l_cymYZajPCfsEnUpK7zDyXQ4kdJ5rHHDIdpTcOIqVwQPqSv3WQTvjYAYJP1zDIxsi_-90jxSusRfCn3uZWFknnLubHt5lNsFe7ZPi1GkW927-5GrH6tqeJnQwhZ-ynanejavDw77hz0qR6-_Dvy7DO9wsBIWqQefasS7DuQNowqZMN3eNL9HAUevSN0v4-z4bDbHvkzvffBtRkYE8qbiJhwwDOb42LCgzSlDOQRj2dQNirBQP_rBGGwkOd8rJ27KSbGbn8HLgFUr7cyiJUYRwiaKRuAWI99RU0RSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
WhiteAesther mobile 1.6.1 (stable)
دوستانی که منتظر اپدیت بودند الان میتونند اپدیت کنند
⚠️
✨
چه چیزی جدید است؟
🔗
زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی. حامل اول چیزی است که شبکهٔ شما می‌بیند و حامل دوم چیزی است که سایت‌ها می‌بینند.
مسیرها ← حامل ← «خودم انتخاب می‌کنم»
⚡️
سایفون بهتر
سایفون به سرورهای بیشتری دسترسی دارد و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد، پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
🤖
حالت خودکار (آزمایشی)
اگر روشنش کنید، برنامه خودش اتر، سایفون و تور را هم‌زمان امتحان می‌کند و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود. راهی که روی هر شبکه کار کرد را هم یادش می‌ماند و دفعهٔ بعد سریع‌تر وصل می‌شود.
فعلاً پیش‌فرض خاموش است تا بیشتر امتحان شود. برای روشن کردن: مسیرها ← حامل ← «خودکار (آزمایشی)»
🛠
اگر نسخهٔ آزمایشی ۱.۶.۰ را نصب کرده بودید و وصل نمی‌شدید، این نسخه آن مشکل را برطرف می‌کند.
💡
نکته
اگر اتر روی اینترنت شما وصل نشد، سایفون را امتحان کنید:
مسیرها ← حامل ← «خودم انتخاب می‌کنم» ← سایفون
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.1
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.1-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.1-universal.apk
روی نسخهٔ فعلی به‌روزرسانی می‌شود و تنظیمات شما می‌ماند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید (همراه اول، ایرانسل، وای‌فای خانگی و…).
@whitedns</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1778" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1777">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RT_Ezai74E7_XU66ruTdxu3Uhlt-mAbo0VwI3pkKWRi797K-8rhVWQZDIEl_UPu26EdpE_kR8Ffh4IfJ5upcdbPp44l1b1z1lYPEMpRipZvaDEnHr6yBNhaslNmwWeK3gynd2_HnrALayaukWOGVMZ6hB1nedg36etkn6k2Zq7c17id95vmoIdQkUVnaWGei03iJM_wv260Kg-QUy8JUe1OT1LrjOR-2l1iBgg10s6OHubVuOKKqLK8fdalxY-Wu40qJP0exvV8VLDsMZgEFX3EXymWuJshnI3QG2R7k10gVb-dDUf5V7Mc4bXK9aZ6qMlT-C89KJAereQF_b6TdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther desktop  1.9.1 (stable)
🔥
دوستانی که منتظر اپدیت بودند الان دیگه میتونند اپدیت کنند
⚠️
پنج ایراد درست شد که سه‌تایشان را فقط وقتی می‌دیدید که شبکه سخت می‌شد.
دکمهٔ «یکی که کار می‌کند را پیدا کن» حالا واقعاً می‌گردد
تا امروز، جست‌وجو روی همان گزینهٔ اول می‌ایستاد و می‌گفت وصل شد — حتی وقتی نشده بود. هیچ‌وقت به سایفون، تور و شش ترکیب زنجیره‌ای نمی‌رسید. حالا هر راه را تا آخر امتحان می‌کند، و یکی را فقط وقتی قبول می‌کند که یک درخواست واقعی از آن رد شده و برگشته باشد.
⚠️
یک نشتی در حالت زنجیره‌ای بسته شد
اگر پروتکل را روی WireGuard یا MASQUE H3 گذاشته بودید و بعد سایفون یا تور را جلویش می‌گذاشتید، Aether از کنار آن کریر بیرون می‌رفت — یعنی از همان آدرسی که زنجیره برای پنهان کردنش وجود داشت. حالا پشت هر کریری خودکار روی MASQUE H2 قفل می‌شود.
به هر کریر همان‌قدر وقت داده می‌شود که لازم دارد
جست‌وجو قبلاً هر تلاش را سر ۹۰ ثانیه می‌برید، در حالی که سایفون در اولین اتصال روی شبکهٔ سخت تا ۵ دقیقه وقت می‌خواهد. نتیجه‌اش این بود که روی سخت‌ترین شبکه‌ها — دقیقاً جایی که این دکمه برای آن ساخته شده — هیچ‌وقت جواب نمی‌داد.
و چند چیز کوچک‌تر
• جست‌وجو ساعت نشان می‌دهد و از اول می‌گوید چقدر ممکن است طول بکشد
• سایفون می‌گوید اولین اتصالش روی شبکهٔ سخت چند دقیقه است، تا فکر نکنید هنگ کرده
• عمق جست‌وجو (از turbo تا thorough)
حالا واقعاً رعایت می‌شود
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.1
ویندوز → .exe
مک (اپل سیلیکون) → macos_arm64.dmg
مک (اینتل) → macos_x86_64.dmg
لینوکس → .AppImage یا .deb / .rpm
@whitedns</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1777" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1776">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ubeo1Ll0BwvnJKXQlsYOVOH2Zc8qDQqBoOOKBGTLxfd2TVQXwn2pKXMkuA7PCVnYUmtkd3HysODd0oC2PUD9K3FqMshNGX1YBBgaPo8gnM0OSfAbPpXwbezE2FqHyIvAr0WM27kS6HZQS3XRwx2qUCVkuQTO8HWVS9CCC1Rm47doJsT1x2o0p9IjnUS23O9hk9Oog1ug_4pS3K7Pt1hOtU0oU2aYvjunz20w1wIpGSbw3ODmF2ta_iH9iE6SIkCutDv1_Ixixjgj5AaDYT5meYB5LxlEAjx1fAONE8HljU5wWROINHvIcYhnvCyhtqdd5S0R7iw1kbeuYwh3qaPMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه پایدار WhiteAesther به‌زودی منتشر می‌شود!
🚀
تجربه‌ای سریع‌تر، امن‌تر و مطمئن‌تر در دسکتاپ و موبایل. منتظر باشید
💚
@whiteaesther</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1776" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1772">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gFpt7MMj8IxW4k_6tsi8cUr3QgJ1KjBnBKrAC1gE-01o8ctgu55VUr9ib3JHxsCYuMx4Y7uU_vT09bdXxHhqDy1NOetrK9YrZ8D9Th9E61q1zuYq8S0GTHx-wyyTw_yfv0A192K5K53pZqx8oGR8ZUPT7rYNmlxb5BzhybQ22i5JA6MJOotEk7eVZhaGlVTpGE-D9k4tu0HaqqA_H5jyGKyzb37PNA6degz-Cud2aGXNJf1dpgOPNUEFrSKNRQAvcRrF5QnwEp5Nakwbv-hgto5ERLdbLBGyB4zl86AgFZqBPJxeDJt5u8qfdp0SEyNce3cJnZS5RsfezU0RhuJz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1772" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1771">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستان :
⚠️
⚠️
اگر پست ها را کامل نخوندید . لطفا توی گروه ها پیام ندید . چون کاملا مشخص هست خیلی از دوستان حتی 10 ثانیه هم وقت نگذاشتند . این مدل پیام دادن فقط باعث گمراهی بقیه میشه . لطفا کاملا پست ها را مطالعه کنید .برنامه را کاملا بررسی کنید . تنظیمات متفاوت را انجام دهید وفقط با توجه به روشی که توی پست های بالا گفته شده گزارش کنید
سپاس</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1771" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1770">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UQ6LK7xZ5B_SyiVwuATyVFMV7W844apRwAl5R4cyU6LWzvTEFVIou9qS8hxi_BO2peUvQ9nq0nOwMxrib28MmjSj4AefnT5dxvDaK7dlVUPfhbmrXFsQ8GwwtFqBXzUmB7Mw36GUYRzQJQ-V0XoagvfXlxtw7jeTsGILsFpOx0at9JlCoPxJD5lrlADlbkMjiE3KTfzBx8lKd_tx8PUyokaWi_UJnbiK2trBOBY3GaYHYdvJT1BWjTGGilZf6s1plC_X4i-vWwx85aXVklcHEuS72_7a92xN-McwPIy_RVM8ob8xWQkc4eNVNgn_6dirA-vbNZGNnfc9RLUQIx92OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا توی نسخه اندروید هم شما حالت اتوماتیک دارید ، خودش می‌گرده و بهترین حالت را انتخاب می‌کنه و وصل میشه
#WhiteAesther_Mobile_1
.6.0</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1770" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1769">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteAesther Mobile  1.6.0
حالت خودکار: فقط دکمهٔ اتصال را بزنید
🔥
🔥
🔥
🔥
⚠️
این نسخه آزمایشی است و ممکن است باگ داشته باشد. داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود.
✨
چه چیزی جدید است؟
دیگر لازم نیست بدانید اتر، سایفون یا تور کدام روی اینترنت شما کار می‌کند. در حالت «خودکار» برنامه خودش اول اتر را امتحان می‌کند و اگر نشد سایفون و تور را، و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود.
راهی را هم که روی هر شبکه کار کرد یادش می‌ماند؛ دفعهٔ بعد روی همان وای‌فای یا همان سیم‌کارت خیلی سریع‌تر وصل می‌شود.
📱
استفاده
برای بیشتر کاربران خودکار از قبل روشن است؛ فقط دکمهٔ اتصال را بزنید.
اگر قبلاً حامل را دستی انتخاب کرده‌اید: تب «مسیرها» ← کارت «حامل» ← «خودکار (پیشنهادی)».
⏳
اولین بار روی یک اینترنت سخت ممکن است چند دقیقه طول بکشد؛ لطفاً صبر کنید. روی صفحه نوشته می‌شود الان کدام راه را امتحان می‌کند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.0
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.0-universal.ap
@whitedns</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1769" target="_blank">📅 15:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1768">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RiEtf_r6V_GJZaIMnLrF7GHiHv8iVpIDx77vtyhrwENDIo9Ab_o7C2ymtg4x24cKewucz2zzFUmLowYl3Be3B3pYyV-bj8aDnRrO9ihpWaZcZqw4OIr0hr93fYaLhIoZw6NZSi3jC5sBahRRaaPbXtI9MWAsQuDGPPlNayu9gd6zAHfyM3sefOXV4m7rvZyKNQczSlVBn6Eb3BTeZOhTNioen3eHtlEeHdxUeu4hP9Rtxzx6736PrBfpgrla8KZnO4G8tUtrJQK_ze0HXi2bqThqKbwMbI2W3qOK7LWBMfpjhzoz2pQa7UF6YYTsbXL2VRZQM9RNxypTkAOHzENaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی نسحه دسکتاپ یک گزینه اتوماتیک ما داریم . که خودش بهترین کانکشن را براتون پیدا میکنه
#
WhiteAesther_desktop_1
.9.0</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1768" target="_blank">📅 14:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1767">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوستان :
اموزش هایی که ما توی پست های کانال میگذاریم به خدا برای شماست - والا ما خودمون بلدیم !
خواهشا وقت بگذارید مطالعه کنید</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1767" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1766">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-poll">
<h4>📊 توی این نسخه ازمایشی whiteaesther مشکل شما برای اتصال و استفاده از هوش مصنوعی حل شد ؟</h4>
<ul>
<li>✓ 😏اتصال اوکی شد ولی هوش مصنوعی کار نمیکنه</li>
<li>✓ ❤️هوش مصنوعی و اتصال اوکی شد</li>
<li>✓ کلا نتونستم وصل بشم😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1766" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1762">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther mobile 1.5.0
⚠️
⚠️
⚠️
⚠️
این یک نسخهٔ آزمایشی است و ممکن است باگ داشته باشد. برای همین داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود. اگر به اتصال پایدار نیاز دارید، فعلاً روی نسخهٔ فعلی بمانید.
━━━━━━━━━━
✨
چه چیزی جدید است؟
۱
. زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی که بخواهید. حامل اول چیزی است که شبکهٔ شما (اپراتور) می‌بیند و حامل دوم چیزی است که سایت‌ها و اینترنت می‌بینند.
۲. سایفون بهتر
سایفون حالا به سرورهای بیشتری دسترسی دارد (از جمله سرورهای داوطلبانهٔ Conduit) و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد؛ پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
━━━━━━━━━━
📱
چطور استفاده کنم؟
۱
. به تب «مسیرها» بروید و در صفحهٔ «چطور وصل می‌شود» پایین بیایید تا به کارت «حامل» برسید.
۲. در بخش «اول — چیزی که شبکه شما می‌بیند» حامل اول را انتخاب کنید.
۳. در بخش «بعد — چیزی که اینترنت می‌بیند» حامل دوم را انتخاب کنید. اگر فقط یک حامل می‌خواهید، «هیچ‌چیز دیگر» را بزنید.
۴. با دکمهٔ «ترتیب را جابه‌جا کن» جای دو حامل با یک لمس عوض می‌شود.
۵. «پوشش» باید روی «کل دستگاه» باشد؛ سایفون و تور در حالت «فقط پروکسی» اجرا نمی‌شوند.
۶. به «خانه» برگردید و وصل شوید. آنجا مسیر کامل نوشته می‌شود، مثلاً «متصل از طریق سایفون، بعد اتر»، و وضعیت هر حامل جداگانه نشان داده می‌شود.
━━━━━━━━━━
🔀
کدام ترکیب برای چه کاری؟
🔹
اتر ← سایفون
اتر وصل می‌شود ولی می‌خواهید سایت‌ها آی‌پی خارجی سایفون را ببینند، نه کلودفلر. کشور خروجی را هم می‌توانید در کارت «کشور خروجی» انتخاب کنید.
🔹
اتر ← تور
بیشترین حریم خصوصی، ولی کند.
🔹
سایفون ← اتر
وقتی اتر روی شبکهٔ شما مستقیم وصل نمی‌شود: سایفون راه را باز می‌کند و اتر از داخل آن بیرون می‌رود.
🔹
سایفون ← تور
وقتی تور مستقیم بسته است.
🔹
تور ← اتر / تور ← سایفون
برای شبکه‌هایی که فقط تور (با پل) از آن‌ها بیرون می‌رود. این دو ترکیب کمتر از بقیه آزمایش شده‌اند و نتیجهٔ شما برای ما خیلی ارزشمند است.
اگر یک ترتیب وصل نشد، «ترتیب را جابه‌جا کن» را بزنید و دوباره امتحان کنید. اینکه کدام ترتیب جواب بدهد به شبکهٔ شما بستگی دارد.
━━━━━━━━━━
💡
نکته‌ها
• زنجیره از یک حامل تنها کندتر است. اگر یک حامل به‌تنهایی برایتان کار می‌کند، همان را نگه دارید.
• وقتی اتر حامل دوم است، خودکار از H2 استفاده می‌کند و انتخاب پروتکل اثری ندارد.
• وقتی تور حامل دوم است، اسنوفلیک کار نمی‌کند؛ تور مستقیم، با پل obfs4 یا با پل‌هایی که به شما داده شده وصل می‌شود.
• اولین اتصال سایفون ممکن است چند دقیقه طول بکشد؛ صبر کنید.
• اگر برای سایفون کشوری انتخاب کرده‌اید و وصل نمی‌شود، «بهترین گزینهٔ موجود» را انتخاب کنید.
• اگر در تنظیمات اندروید «VPN همیشه روشن» همراه با «مسدود کردن اتصال‌های بدون VPN» روشن است، ممکن است سایفون و تور وصل نشوند؛ خاموشش کنید.
━━━━━━━━━━
🐞
گزارش باگ
اگر به مشکلی خوردید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده». لطفاً بنویسید کدام ترکیب را امتحان کردید و روی چه اینترنتی بودید (همراه اول، ایرانسل، وای‌فای خانگی و…).
━━━━━━━━━━
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.5.0
⚠️
در صورت امکان ورژن قبلی را کاملا uninstall کنید و ورژن جدید را نصب کنید تا کاملا بروز شود
⚠️
• بیشتر گوشی‌ها: WhiteAestherMobile-1.5.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.5.0-universal.apk
روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان حفظ می‌شود. برای برگشتن به نسخهٔ پایدار (1.4.2) باید اول این نسخه را حذف کنید.
@whitedns</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1762" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther desktop 1.9.0
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
این نسخه «آزمایشی» (Pre-release) است و ممکن است باگ داشته باشد. بنا به درخواست تعداد زیادی از شما، آن را زودتر در اختیارتان می‌گذاریم.
✅
اگر نسخهٔ فعلی برایتان بدون مشکل کار می‌کند، فعلاً نیازی به به‌روزرسانی ندارید.
✨
چه چیزهایی جدید است؟
🔗
زنجیر کردن دو راه خروج
حالا می‌توانید Aether، سایفون و تور را دوتادوتا و به هر ترتیبی پشت هم بگذارید. اولی شما را از شبکهٔ فیلترشده بیرون می‌برد، دومی تعیین می‌کند با چه IP و از چه کشوری دیده شوید.
مثلاً Aether ← سایفون: سرعت Aether برای بیرون رفتن، و کشور خروجِ سایفون.
🔍
دکمهٔ «یکی که کار می‌کند را پیدا کن»
اگر نمی‌دانید روی شبکهٔ شما کدام راه جواب می‌دهد، اپ خودش همه را یکی‌یکی امتحان می‌کند و اولی را که وصل شد نگه می‌دارد.
🟢
سایفون خیلی بهتر وصل می‌شود
خیلی‌ها گفته بودند با اپ خود سایفون وصل می‌شوند ولی با حالت سایفونِ ما نه. علتش را پیدا کردیم: سایفونِ ما نمی‌توانست از پروکسی‌های داوطلبانهٔ خود سایفون (in-proxy) استفاده کند، یعنی همان راهی که در ایران بیشتر از همه جواب می‌دهد. فهرست سرورهایش هم به‌روز نمی‌شد. هر دو مشکل برطرف شد و سایفون حالا برای وصل شدن تا ۵ دقیقه صبر می‌کند (قبلاً ۲ دقیقه بود).
📥
دانلود:
https://github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.0
⚠️
دوستان حتما  delete cache/data را بزنید تا کاملا بروز از برنامه استفاده کنید
⚠️
🪟
ویندوز: WhiteAesther_1.9.0_windows_x86_64.exe
🍎
مک با چیپ M1 و جدیدتر: WhiteAesther_1.9.0_macos_arm64.dmg
🍎
مک اینتل: WhiteAesther_1.9.0_macos_x86_64.dmg
🐧
لینوکس: فایل AppImage یا deb یا rpm (نسخهٔ x86_64 یا arm64)
🐞
اگر به مشکلی خوردید:
دکمهٔ Advanced ← عیب‌یابی ← در بخش «گزارش»، دکمهٔ «ذخیرهٔ گزارش» یا «کپی» را بزنید و برای ما بفرستید. آدرس‌های IP به‌طور پیش‌فرض در گزارش پنهان می‌شوند.
📘
آموزش نسخهٔ 1.9.0
١) کجاست؟
بالای برنامه دکمهٔ Advanced را بزنید ← از منوی کنار، «مسیرها و پروتکل‌ها» ← کارت «راه خروج».
٢) یک راه خروج (مثل قبل)
در ردیف «خروج از این شبکه با» یکی را انتخاب کنید (Aether، سایفون یا تور) و ردیف «و سپس خروج از» را روی «هیچ‌چیز دیگر» بگذارید.
٣) زنجیر کردن دو راه خروج
در ردیف اول چیزی را بزنید که شما را از شبکه بیرون می‌برد، و در ردیف دوم چیزی که می‌خواهید IP و کشورِ خروجتان مالِ آن باشد. زیر این دو ردیف یک کادر دقیقاً می‌گوید این ترکیب چه چیزی به شما می‌دهد و چه چیزی نه.
💾
برای اینکه انتخابتان بعد از بستن برنامه هم بماند، «ذخیرهٔ پروفایل» را بالای صفحه بزنید.
چند ترکیب کاربردی:
• Aether ← سایفون: وقتی Aether وصل می‌شود ولی IP از کشور دیگری می‌خواهید. کشور را از «کشور خروج» انتخاب کنید (فهرست کشورها بعد از اولین اتصال سایفون ظاهر می‌شود).
• سایفون ← Aether: وقتی Aether به‌تنهایی وصل نمی‌شود ولی سایفون می‌شود. خروجتان همچنان نزدیک خودتان است و کشورتان عوض نمی‌شود. شرطش این است که قبلاً حداقل یک بار با خود Aether (بدون زنجیره) وصل شده باشید.
• تور ← سایفون: وقتی نه Aether و نه سایفون به‌تنهایی وصل نمی‌شوند. کندتر است، ولی یک راه دیگر است.
نکته: وقتی تور نفر دوم زنجیره است، از «پل‌ها» استفاده نمی‌کند؛ کارِ بیرون رفتن را نفر اول انجام داده.
نکته: زنجیره‌ای که سایفون یا تور در آن باشد UDP را عبور نمی‌دهد. سایت‌ها و بیشتر برنامه‌ها عادی کار می‌کنند، ولی بعضی تماس‌های صوتی و تصویری یا بازی‌های آنلاین ممکن است کار نکنند.
٤) پیدا کردن خودکار
در همان صفحه، کادر سبز «نمی‌دانید کدام کار می‌کند؟» را پیدا کنید و «یکی که کار می‌کند را پیدا کن» را بزنید.
اپ اول تک‌ها را امتحان می‌کند (Aether، سایفون، تور) و فقط اگر هیچ‌کدام وصل نشد سراغ ترکیب‌ها می‌رود. به هرکدام تا ۹۰ ثانیه فرصت می‌دهد و نتیجهٔ هر تلاش را همان‌جا نشان می‌دهد. هر وقت خواستید، «توقف جستجو» را بزنید.
٥) درباره سایفون
اولین اتصال سایفون ممکن است چند دقیقه طول بکشد، مخصوصاً وقتی از طریق پروکسی‌های داوطلبانه وصل می‌شود. عجله نکنید؛ تا ۵ دقیقه صبر می‌کند.
⚠️
مشکلات شناخته‌شده
• زنجیره‌هایی که به Aether ختم می‌شوند (مثل سایفون ← Aether) ممکن است بعد از چند ثانیه قطع و دوباره وصل شوند (وضعیت reconnecting). روی رفعش کار می‌کنیم.
• ترکیب سایفون ← تور، و قابلیت Kill switch (قطع ترافیک هنگام افتادن تونل) در حالت زنجیره، هنوز کمتر آزمایش شده‌اند.
ممنون که با ما هستید
🤍
گزارش‌های شما مستقیم به بهتر شدن نسخهٔ پایدار کمک می‌کند.
@whitedns</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1761" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1759">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.   بعدش دوباره وصل بشید.   خود اپ هم…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1759" target="_blank">📅 15:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Vufs_VXvbwdXAred1MJ_kbqLs5wIz5Pku744uCrQDPWWevnnArJwe0nobcp4F0k6nuzX3OdTDFQtv5bDj2UqZxCuPdnljLhBkDKD3nnMJ9FaBGFHcrYAmCl3A6kD2vFUeFlpCx8ddJw_-e-c6mAKU66VTwLGy36GsazGavGBb2LnQH5-6woj4zZWcj5TMB5lOnJfJmFXsRWk2RsMO4Il8Bq21eDHZQYxcuFbcXzfoN1vJjq2oss93OxeuU8Z53a7BGff8Lfa6zYhf-RlOg9YZ-tR3qZiRQXtZ2_WQqFLY_fvVKxJXVkJR_EhGwPnd6cENoDV7gd_7b3S5lNQg1Y5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
WhiteVPN Desktop v1.0.22 منتشر شد
این نسخه چند مشکل مهم را برطرف می‌کند که می‌توانست باعث
عدم اتصال، ذخیره‌نشدن تنظیمات و ناسازگاری برخی کانفیگ‌ها
شود. همچنین از این نسخه،
سرورهای اختصاصی WhiteVPN
هم به نسخه دسکتاپ اضافه شده‌اند.
━━━━━━━━━━━━━━━━━━
در این نسخه چه مواردی اضافه شد و چه باگ هایی رفع شد :
🖥
سرورهای اختصاصی و عمومی، هر دو در دسکتاپ
تا امروز نسخه دسکتاپ فقط از سرورهای عمومی استفاده می‌کرد، در حالی که نسخه موبایل روی سرورهای اختصاصی قرار داشت.
حالا هر دو فهرست داخل برنامه در دسترس هستند و از صفحه
Subscriptions
می‌توانید مشخص کنید از کدام منبع متصل شوید.
نصب‌های جدید به‌صورت پیش‌فرض با
فهرست اختصاصی
شروع می‌شوند.
اگر یکی از فهرست‌ها در دسترس نباشد، برنامه دیگر همان‌جا متوقف نمی‌شود و به‌صورت خودکار منابع دیگر را بررسی می‌کند؛ از جمله:
• فهرست داخلی دیگر
• سابسکریپشن‌های شخصی شما
• کانفیگ‌هایی که دستی وارد کرده‌اید
برنامه همچنین اعلام می‌کند اتصال از کدام منبع انجام شده است. انتخاب اصلی شما تغییر نمی‌کند و در اتصال بعدی دوباره همان منبع امتحان خواهد شد.
━━━━━━━━━━━━━━━━━━
🛠
رفع مشکل «هیچ سروری وصل نمی‌شود»
در نسخه‌های قبلی، اگر روی فهرست داخلی فیلتر
کشور
یا
نوع اتصال
انتخاب می‌کردید و بعد به سابسکریپشن شخصی خودتان می‌رفتید، همان فیلتر روی فهرست جدید هم اعمال می‌شد.
در نتیجه ممکن بود تمام سرورهای شما رد شوند، بدون اینکه مشخص باشد مشکل از کجاست.
حالا هر فهرست تنظیمات و فیلترهای خودش را نگه می‌دارد.
وقتی وارد فهرست دیگری می‌شوید، آن فهرست از حالت
Automatic
شروع می‌شود و وقتی برمی‌گردید، انتخاب قبلی شما همچنان حفظ شده است.
━━━━━━━━━━━━━━━━━━
⚙️
رفع مشکل ذخیره‌نشدن تنظیمات
برخی گزینه‌های صفحه Settings تغییر می‌کردند، اما پس از خروج از صفحه به حالت قبلی برمی‌گشتند.
این مشکل برای گزینه‌هایی مثل:
Amnezia Noise
و
این‌ها مستقیم خارج شوند
برطرف شده است.
حالا تغییرات مثل نسخه موبایل، به‌درستی ذخیره می‌شوند.
━━━━━━━━━━━━━━━━━━
🔗
پشتیبانی بهتر از کانفیگ‌ها
پشتیبانی از موارد زیر اصلاح و کامل‌تر شده است:
anytls
socks
HTTP Proxy
قبلاً کانفیگ‌های anytls ممکن بود اصلاً در فهرست نمایش داده نشوند.
کانفیگ‌های socks و HTTP Proxy هم ذخیره و نمایش داده می‌شدند، اما هنگام اتصال به‌درستی کار نمی‌کردند.
این مشکلات در نسخه جدید برطرف شده‌اند.
━━━━━━━━━━━━━━━━━━
🐧
رفع مشکل آیکون Tray در لینوکس
در برخی نسخه‌های لینوکس، کلیک روی آیکون WhiteVPN کنار ساعت باعث بازگشت پنجره برنامه نمی‌شد.
این مشکل در نسخه 1.0.22 برطرف شده است.
━━━━━━━━━━━━━━━━━━
⚠️
کاربران لینوکس، این بخش را حتماً بخوانید
نام فایل‌های لینوکس تغییر کرده است.
فایل‌های بدون پسوند amd64 و arm64 حالا از
WebKitGTK 4.1
استفاده می‌کنند و مناسب سیستم‌های جدید هستند، از جمله:
• Ubuntu 24.04 و جدیدتر
• Debian 13
• Fedora 40 و جدیدتر
اگر از
Ubuntu 22.04
یا
Debian 12
استفاده می‌کنید، نسخه webkit40 را دانلود کنید:
WhiteVPN-Desktop-1.0.22-linux-amd64-webkit40.deb
در نسخه‌های قبلی، نام‌گذاری فایل‌های Linux بین amd64 و arm64 یکسان نبود و همین موضوع می‌توانست باعث انتخاب فایل اشتباه و خطای Dependency شود.
این نام‌گذاری حالا اصلاح شده است.
✅
برای کاربران Linux با پردازنده Intel/AMD، ساده‌ترین گزینه همچنان
AppImage
است:
WhiteVPN-Desktop-1.0.22-linux-amd64.AppImage
━━━━━━━━━━━━━━━━━━
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
📥
راهنمای سریع انتخاب فایل
🪟
Windows — Intel / AMD
windows-x64
🪟
Windows — ARM / Snapdragon
windows-arm64
🍎
Mac — Apple Silicon / M1 و جدیدتر
macos-arm64
🍎
Mac — Intel
macos-amd64
🐧
Ubuntu 24.04+ / Debian 13
linux-amd64.deb
🐧
Ubuntu 22.04 / Debian 12
linux-amd64-webkit40.deb
🐧
Fedora / RPM-based Linux
linux-amd64.rpm
━━━━━━━━━━━━━━━━━━
📢
@whitedns</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1758" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.
بعدش دوباره وصل بشید.
خود اپ هم هر ۳۰دقیقه اتوماتیک ساب رو آپدیت میکنه.
کشور ها ثابت میمونه و فقط آی‌پی ها عوض میشن.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1757" target="_blank">📅 10:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1756">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🛡
انتشار نسخه WhiteVPN 1.6.7
👆
دوستانی که این ورژن رو قبلا دانلود کرده بودند. دوباره نصبش کنید چون سرور های عمومی یک باگی داشت که رفع شد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1756" target="_blank">📅 10:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1751">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.7-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1751" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1751" target="_blank">📅 10:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1750">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCR49b9XcWZp7Sm0fobvFkXpSmIr4BGAsuL4tNAY-LgNI4QMllV3kF5_BFUsNSQg9C8L9HqkBiX9EfNIeOxRcno88TOMEwazzsZ4R09vo-q2ezv93RMqwLBNljOpiOimOWaQ_TiPwXvExDss_XbvePrPb72sHnUeD9pQiI8kXl3_eDZCHOy5j7MpKZ47LHXq8eP_yael8mKR6tNuKf61ovGvJ7eHJZU8HXkQnTwZkx4xeewZjusM4ueC3PQueNk89Kfz9OkNNs6LDY5x_oNieK79BJVd5LfiTdByUL6-uTpO0_ZdMcMITqpXRJEixLEQK8nbCba9r0a-JQLsB9w8Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه WhiteVPN 1.6.7
✍️
تغییرات این نسخه
🟢
توی این نسخه، ما سرور های اختصاصی خودمون رو هر چند ساعت یکبار تازه میکنیم تا پایداری بیشتر بشه. و فیلترنشن.
🟢
۳ کشور جدید به سرور های اختصاصی اضافه کردیم
🇺🇸
🇩🇪
🇸🇬
🟢
با کمک تیم پس‌کوچه
@paskoocheh
یکسری حفره امنیتی رو رفع کردیم
🟢
حالا میتونید همزمان تست سرعت بگیرید و هرکدوم رو خواستید کنسل کنید.
پیشنهاد میکنم حتما این ورژن رو بگیرید تا آپدیت های سرور های اختصاصی براتون بیاد.
⭐️
دانلود کنید، به بقیه معرفی کنید و نتیجه تست هاتون رو برای ما بفرستید تا مارو هم خوشحال کنید.
💻
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1750" target="_blank">📅 10:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1749">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان عزیز من مجبور به پاک کردن ورژن آخر شدم. ساب های عمومی کار نمیکردند داخل اپ. به زودی آپدیت میکنم و دوباره پست رو میفرستم براتون.
سرور های اختصاصی توی این ورژن جدید که دانلود کردید باید درست کار کنه.
شرمنده همگی
❤️</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1749" target="_blank">📅 09:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
امروز یک آپدیت جدید برای WhiteVPN داریم
توی این ورژن، یکسری تغییرات امنیتی داشتیم به کمک بچه های تیم پسکوچه.
👨‍💻
مهمتر از همه، سرور های اختصاصی رو اپدیت میکنیم تا هر چند ساعت آپ‌پی های جدید بهتون بده.
این یکم هزینه های مارو بیشتر میکنه اما اینطوری کار فیلترچی رو سخت‌تر میکنیم و سرویس ها دیگه فیلتر نمیشن.
🥺
دیروز مادربزرگ خودم برای اولین بار از ابزار هامون استفاده می‌کرد و چنان دعای خیری برام کرد که انرژی ۲۰برابر شده.
هیچی چیزی ارزشش از این بیشتر نیست که بتونیم با عزیز هامون در ارتباط بمونیم.
هوای هم دیگرو داشته باشید
ارادت
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1746" target="_blank">📅 06:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1745">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">با WhiteAesther به Tor و Psiphon وصل شو!
🔥
https://youtu.be/WiybhJ7ylps
آخرین نسخه WhiteAesther
🦋
WhiteAesther Windows
WhiteAesther Android</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1745" target="_blank">📅 02:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
وایت‌اِستر موبایل نسخهٔ 1.4.2 منتشر شد
WhiteAesther Mobile v1.4.2
حالا سه راه خروج دارید، نه یکی.
از این نسخه اگر شبکه جلوی یک مسیر را گرفت، بدون نصب برنامهٔ دیگری می‌توانید مسیر بعدی را امتحان کنید.
⚡️
اِتر | Aether
همان موتور اصلی برنامه؛ سریع‌ترین مسیر و حالت پیش‌فرض.
🌐
سایفون |Psiphon
از شبکهٔ سایفون استفاده می‌کند. کمی کندتر است، اما ممکن است روی شبکه‌هایی که اِتر جواب نمی‌دهد متصل شود.
🧅
تور | Tor
عبور از سه بازپخش؛ مناسب زمانی که حریم خصوصی اهمیت بیشتری دارد. کندترین گزینه بین سه مسیر.
✅
تمام قابلیت‌های قبلی با هر سه مسیر کار می‌کنند:
• زنجیرهٔ خروج
• تقسیم ترافیک
• قوانین مسیریابی
• کلید قطع اضطراری
✨
تغییرات مهم نسخهٔ 1.4.2
• انتخاب کشور خروجی برای سایفون
• دریافت پل تور با یک دکمه
• امکان فراموش کردن نقطهٔ پایانی و جست‌وجوی دوباره
• رفع مشکل ثابت ماندن آدرس بدون تونل
• رفع نمایش اشتباه آی‌پی در حالت سایفون
• اضافه شدن سه موتور با فقط حدود ۱۴ مگابایت افزایش حجم
⬇️
دانلود نسخه موبایل
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
📖
آموزش کامل استفاده
برای مشاهده، بخش زیر را باز کنید
👇
۱️⃣ انتخاب راه خروج
وارد این بخش شوید:
پیشرفته ← مسیرها و پروتکل‌ها
در کارت
«راه خروج»
سه گزینه دارید.
اِتر
| Aether
همان حالت قبلی و سریع‌ترین مسیر.
سایفون
|Psiphon
پیدا کردن خودکار مسیر و امکان انتخاب کشور خروج.
تور
| Tor
مناسب‌تر برای ناشناس‌ماندن، اما کندتر.
مسیر موردنظر را انتخاب کنید و سپس
اتصال
را بزنید.
⚠️
در حالت سایفون و تور، تنظیمات نقطهٔ پایانی و انتخاب پروتکل اثری ندارند؛ این موارد فقط مخصوص اِتر هستند.
━━━━━━━━━━
۲️⃣ انتخاب کشور خروج در سایفون
بعد از انتخاب سایفون، گزینه
«کشور خروج»
ظاهر می‌شود.
🔸
در اولین استفاده ممکن است فقط
«بهترین گزینه موجود»
نمایش داده شود.
این طبیعی است؛ فهرست کشورها بعد از اولین اتصال موفق دریافت می‌شود.
🔸
انتخاب کشور یک ترجیح است، نه تضمین.
بعضی کشورها ظرفیت کمتری دارند و ممکن است اتصال به آن‌ها موفق نشود.
اگر یک کشور متصل نشد، گزینه
«بهترین گزینه موجود»
را انتخاب کنید تا سایفون از تمام سرورهای قابل دسترس استفاده کند.
🔄
تغییر کشور نیازمند اتصال مجدد است.
━━━━━━━━━━
۳️⃣ تور و پل‌ها
بعد از انتخاب تور، بخش
«پل‌ها»
نمایش داده می‌شود.
خاموش
اتصال مستقیم به تور.
همراه برنامه
استفاده از پل‌های داخلی.
گزینه‌های ترابرد:
obfs4
snowflake
meek
چسبانده‌شده
برای وارد کردن پل شخصی.
در این حالت می‌توانید پل را دستی وارد کنید یا گزینه
«از تور پل بگیر»
را بزنید.
🔑
هنگام دریافت پل، کشوری را وارد کنید که از آن متصل هستید.
مثال:
IR
منظور کشور فعلی شماست، نه کشوری که می‌خواهید آی‌پی خروجی آن را داشته باشید.
💡
ابتدا با اِتر یا سایفون متصل شوید و بعد پل بگیرید.
پل‌های جدید به فهرست اضافه می‌شوند و موارد قبلی حذف نمی‌شوند.
━━━━━━━━━━
۴️⃣ نکته مهم درباره تور
تور فقط ترافیک زیر را عبور می‌دهد:
TCP
برنامه درخواست‌های ناسازگار را مدیریت می‌کند تا اتصال بی‌دلیل معلق نماند.
برای بازی، تماس تصویری و استفاده‌های حساس به تأخیر، اِتر یا سایفون انتخاب مناسب‌تری هستند.
━━━━━━━━━━
۵️⃣ اگر راه خروج قطع شود
اگر پردازش سایفون یا تور متوقف شود، وایت‌اِستر آن را تشخیص می‌دهد، وضعیت را
«خطا»
نشان می‌دهد و زنجیره اتصال را می‌بندد.
اگر گزینه
«اگر تونل قطع شد، ترافیک را مسدود کن»
فعال باشد، ترافیک بسته باقی می‌ماند تا خارج از تونل ارسال نشود.
برای بازگرداندن اتصال، ابتدا
قطع اتصال
را بزنید.
@whitedns</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1743" target="_blank">📅 19:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1741">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
وایت‌اِستر دسکتاپ نسخهٔ ۱.۸.۰ منتشر شد
WhiteAesther Desktop v1.8.0
حالا سه راه خروج دارید، نه یکی.
تا امروز ترافیک شما از مسیر کلادفلر عبور می‌کرد. این مسیر سریع است، اما معمولاً کشور خروج شما را تغییر نمی‌دهد.
از نسخهٔ ۱.۸.۰ دو مسیر جدید اضافه شده است:
⚡️
اِتر
Aether
همان حالت قبلی و سریع‌ترین گزینه برای استفاده روزمره.
🌐
سایفون
Psiphon
مسیر مناسب را پیدا می‌کند و امکان انتخاب کشور خروج را می‌دهد.
در حال حاضر
۲۵ کشور
در دسترس است.
🧅
تور
Tor
ترافیک را از چند بازپخش عبور می‌دهد؛ مناسب‌تر برای حریم خصوصی، اما کندتر.
پل نیز پشتیبانی می‌شود و امکان دریافت خودکار پل وجود دارد.
✅
هر سه مسیر با قابلیت‌های زیر کار می‌کنند:
• زنجیرهٔ خروج
• کل دستگاه
• تونل کامل
تنظیمات قبلی شما تغییری نکرده است. اگر چیزی را تغییر ندهید، برنامه مثل قبل کار خواهد کرد.
⬇️
دانلود نسخه دسکتاپ
https://github.com/WhiteDNS/WhiteAesther/releases/latest
📖
آموزش کامل مسیرهای خروج جدید
برای مشاهده، بخش زیر را باز کنید
👇
۱️⃣ انتخاب راه خروج
وارد این بخش شوید:
پیشرفته ← مسیرها و پروتکل‌ها
در کارت
«راه خروج»
سه گزینه دارید.
اِتر
Aether
همان حالت قبلی و سریع‌ترین مسیر.
سایفون
Psiphon
پیدا کردن خودکار مسیر و امکان انتخاب کشور خروج.
تور
Tor
مناسب‌تر برای ناشناس‌ماندن، اما کندتر.
مسیر موردنظر را انتخاب کنید و سپس
اتصال
را بزنید.
⚠️
در حالت سایفون و تور، تنظیمات نقطهٔ پایانی و انتخاب پروتکل اثری ندارند؛ این موارد فقط مخصوص اِتر هستند.
━━━━━━━━━━
۲️⃣ انتخاب کشور خروج در سایفون
بعد از انتخاب سایفون، گزینه
«کشور خروج»
ظاهر می‌شود.
🔸
در اولین استفاده ممکن است فقط
«بهترین گزینه موجود»
نمایش داده شود.
این طبیعی است؛ فهرست کشورها بعد از اولین اتصال موفق دریافت می‌شود.
🔸
انتخاب کشور یک ترجیح است، نه تضمین.
بعضی کشورها ظرفیت کمتری دارند و ممکن است اتصال به آن‌ها موفق نشود.
اگر یک کشور متصل نشد، گزینه
«بهترین گزینه موجود»
را انتخاب کنید تا سایفون از تمام سرورهای قابل دسترس استفاده کند.
🔄
تغییر کشور نیازمند اتصال مجدد است.
━━━━━━━━━━
۳️⃣ تور و پل‌ها
بعد از انتخاب تور، بخش
«پل‌ها»
نمایش داده می‌شود.
خاموش
اتصال مستقیم به تور.
همراه برنامه
استفاده از پل‌های داخلی.
گزینه‌های ترابرد:
obfs4
snowflake
meek
چسبانده‌شده
برای وارد کردن پل شخصی.
در این حالت می‌توانید پل را دستی وارد کنید یا گزینه
«از تور پل بگیر»
را بزنید.
🔑
هنگام دریافت پل، کشوری را وارد کنید که از آن متصل هستید.
مثال:
IR
منظور کشور فعلی شماست، نه کشوری که می‌خواهید آی‌پی خروجی آن را داشته باشید.
💡
ابتدا با اِتر یا سایفون متصل شوید و بعد پل بگیرید.
پل‌های جدید به فهرست اضافه می‌شوند و موارد قبلی حذف نمی‌شوند.
━━━━━━━━━━
۴️⃣ نکته مهم درباره تور
تور فقط ترافیک زیر را عبور می‌دهد:
TCP
برنامه درخواست‌های ناسازگار را مدیریت می‌کند تا اتصال بی‌دلیل معلق نماند.
برای بازی، تماس تصویری و استفاده‌های حساس به تأخیر، اِتر یا سایفون انتخاب مناسب‌تری هستند.
━━━━━━━━━━
۵️⃣ اگر راه خروج قطع شود
اگر پردازش سایفون یا تور متوقف شود، وایت‌اِستر آن را تشخیص می‌دهد، وضعیت را
«خطا»
نشان می‌دهد و زنجیره اتصال را می‌بندد.
اگر گزینه
«اگر تونل قطع شد، ترافیک را مسدود کن»
فعال باشد، ترافیک بسته باقی می‌ماند تا خارج از تونل ارسال نشود.
برای بازگرداندن اتصال، ابتدا
قطع اتصال
را بزنید.
❓
اگر سؤال یا مشکلی داشتید، در گروه وایت‌دی‌ان‌اس مطرح کنید.
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1741" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1740">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XQYb3mauIF4hiFGBBH7k8vKpe2lT5ALPG32JJXuOw6DP6UhJAUvSDems_ny95QdBv43jcdnESBE1caL_lXnO3ujvvU54fp8HL7cricwKA253oPc7v8le2yKbKRO-sCb61DsYrcCV-Yy72yRIBrRgF1iOjNfIL1AS6DDVUjSuA6H_St1V-6nocVyVt-NuujZvmkb4kHRlZ0rdVGh21bWGpCXBTK9d3WqBDUKPchLjfBBRGtveRukjpEdLkFi9wyUtBbkcsjgn7-iAGFFsVMcqiDaHArp7on4KNVAZnBhkbtBjGjMfZ6b_4FFn2liUuaX3qdUycL5JIJB90QTS6ER7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon
🔥
@whitedns</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1740" target="_blank">📅 11:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1738">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-poll">
<h4>📊 سرور های اختصاصی براتون وصل میشن؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1738" target="_blank">📅 11:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1737">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL8oKAonubiy-owFdFbiefal7EMTYhh2WFoS78ZIyDnB7dp40bXEXNf70ejbAtcZI_XHTqKeHqk5p5dH1p8BAW2opyLtZ8q26f_5_3NofkFlxnNUW7fpCkZ2gnJL-F4_jKKNWJUARXc0WI2Ul1qRCPTrq-3TBYaRHOoxg5PKv9qSIkFDtQJojtvMsVK63wb9CYE2NrfG1PLQw5Zz8pFR-794lGBOxY340RGoOy8Y4YMEMNx6CHey1U6spJf8gCQDZlLKsOfWeHfQUN1l4zANCExNq_5_nVpdssENr8xfD2mZUuKytzexwEf-hupU-0wpvAnQlmOYqKnu1DHLa5KC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
💬
Support Bot:
@WhiteDnsResponder_bot
🔗
WhiteDnsChain
@WhiteDnsChainbot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1737" target="_blank">📅 08:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1736">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">از دیروز تا حالا تعداد اتصال‌ها چند برابر شده؛ از کامنت‌هاتون هم معلومه که این تغییر رو حس کردید
🙌
جالبه بدونید ما با فقط ۱۰ تا سرور و ماهی ۱۵۰ دلار هزینه، داریم هر هفته به حدود ۵۰ هزار کاربر فعال داخل اپ WhiteVPN، رایگان سرویس می‌دیم!
این تازه بدون حساب کردن کاربرهای ویندوزه؛ با اون‌ها، آمار خیلی بیشتر هم می‌شه.
😑
آدم این عددها رو که می‌بینه، بیشتر حرص پول‌هایی رو می‌خوره که تا امروز به فیلترشکن‌فروش‌ها داده
واقعاً ممنون از انرژی مثبتی که بهمون می‌دین و وقتی که می‌ذارید تا تجربه‌هاتون رو زیر پست‌ها بنویسید. همین بازخوردها کمک می‌کنه بفهمیم کجا خوب پیش رفتیم و کجا هنوز باید بهتر بشیم.
به‌زودی WhiteVPN Desktop رو هم با سرورهای اختصاصی آپدیت می‌کنیم تا کاربرهای دسکتاپ هم از این اتصال‌ها استفاده کنن.
🎮
یه سورپرایز هم برای کاربرهای WhiteAesther و بچه‌هایی داریم که دنبال سرویس مخصوص گیمینگ بودن
ممنون که کنارمونید
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1736" target="_blank">📅 06:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1735">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ما سعی میکنیم هر ۲
یا
۳ روز سرور هارو عوض کنیم تا تا جای ممکن از فیلتر شدن آی‌پی ها جلوگیری کنیم
.
همچنین کشور های دیگه رو هم اضافه میکنیم تا آپشن های بیشتری داشته باشید
❤️
🛡
سرور های اختصاصی رایگان، امن و مدیریت شده توسط
تیم ما هستن.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1735" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1734">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید. امیدوارم همه بتونید به سرور های اختصاصی وصل بشید.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1734" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1729">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">36.1 MB</div>
</div>
<a href="https://t.me/whitedns/1729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/whitedns/1729" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1728">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5lO-S2QW-UGOILcwAsJJ3CT65JvfSH7KoycXkw_WiD5SHFhGHQKfdFwl8SQaN7y-BYrkEJ8sTroMx9CzC3leWYdYjtJx1uWxvqe12biRrW6tr_Lk1uQ9BVu5E1zbpMOsTsv4Jj2OOIXh-jEI1k9hnXYdI5vbD7KKAovLKS7SnpHRKtYKz6FNVXNXf73DEWiNy9ONJ9cQ1JeNfy_oU8sikooGwblfvL2sHgnvyvfQUz1RaL3jzUXNxU-nJsQSR7u9dEAdGp7vbKkaXQIlLVtzCGRShrYeKzaFyPiVArCzafA1HL7Nc1vGL3KjZF-eeF5Or75WfBoUESXHPAFGy7i_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
🟢
توی این نسخه ما ۱۰سرور اختصاصی WhiteVPN گذاشتیم. همه داخل فنلاند هستند.  بعد از تست کردن سرور کشور های دیگه رو هم اضافه میکنیم.
در صورت فیلتر شدن سرویس ها، سرور هارو جایگزین میکنیم.
🟢
توی این ورژن، اپ اول سعی میکنه به سرور های اختصاصی WhiteVPN وصل بشه، در صورتی که امکان‌پذیر نبود بعد سرور های عمومی رو امتحان میکنیم.
📱
دانلود آخرین نسخه از گیتهاب
✍️
دوستانی که ورژنی که دقیقه هایی پیش فرستادیم رو گرفتن، دوباره دانلود و نصب کنید.
❤️
نتیجه اتصال رو برای ما بفرستید.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1728" target="_blank">📅 14:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✍️
یه زودی یک آپدیت جدید داریم برای WhiteVPN روی اندروید.
توی این ورژن سرور های اختصاصی WhiteVPN رو اضافه کردیم. برای شروع ۱۰تا سرور اختصاصی فنلاند به صورت آزمایشی اضافه کردیم.
اگر بازخورد ها خوب بود، سرور های کشور های مختلف رو اضافه میکنیم.
توی این ورژن جدید، اپ اپل سعی میکنه به سرور های اختصاصی ما وصل بشه، بعد میره روی سرور های عمومی.
خیلی زود برای دستکتاپ هم آماده میشه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1725" target="_blank">📅 13:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
نسخه جدید WhiteDNS Clean IP Finder منتشر شد — v1.4.3
این آپدیت، قابلیت‌های جدید و اصلاحات مهم نسخه‌های v1.4.1 تا v1.4.3 را یک‌جا ارائه می‌دهد.
✨
مهم‌ترین تغییرات:
⚡️
اضافه شدن حالت اسکن سریع
Fast Scan Mode
🌐
اضافه شدن انتخابگر شبکه‌های Edge
Edge Network Picker
☁️
پشتیبانی از سرویس‌های مختلف از جمله:
Cloudflare • Cloudflare Pages • Vercel • Render • Railway •
Fly.io
• Netlify • Koyeb • Glitch
🎯
اسکن هوشمند بر اساس دامنه‌های اختصاصی هر پلتفرم، برای پیدا کردن IPهای واقعاً قابل استفاده
🔐
افزایش دقت در اسکن‌های Scoped با بررسی معتبرتر Certificate و پاسخ دامنه
🌍
اصلاح تشخیص روی Port 80 و جلوگیری از نتیجه‌های اشتباه مبتنی بر CDN Header
🚂
بازگشت دامنه
railway.app
به دامنه‌های شناسایی Railway
🛠
بهبود منطق اسکن، افزایش دقت نتایج و رفع چندین باگ
📱
💻
نسخه‌های منتشرشده برای:
Android • Windows • Linux • macOS • Termux
اگر هنوز از نسخه‌های قبلی استفاده می‌کنید، پیشنهاد می‌شود مستقیماً به v1.4.3 بروید.
🔗
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.4.3
@whitedns</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1724" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب
https://youtu.be/h920xIQCMP4?si=gjpsrzgky62iOy25
@whitedns</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1723" target="_blank">📅 20:31 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
