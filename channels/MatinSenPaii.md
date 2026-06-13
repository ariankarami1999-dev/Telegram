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
<img src="https://cdn1.telesco.pe/file/D6nIAJAn6mXi2HaM5xpj5niwowP9fqjWKrkOUodc26glr4YbAnDy1vEsuP7mB0X2nM0oPSnPg3AfsgV61nbhPoUR0dwaChz2BHNzUZp_SSlEXYJYk0QO2VT1EQCM29NxALki2rNWtv1O_sraF1vbAhnrMrYc1_J-nPf297BXZXGtFyvDkCcK_W9PGZxwrVwNZKYEtL_YsAtsxiyxjgQwSwlNuBEfpFOMQqQRZkASejh2D8-H1tZQqfcGvt6FH48K8zxuyFB9NjvpDO4iQH-Cq052MhFQ_Il-1PR4LExNsaUIIT3a_gz7DzNpxxsOXS45JjZe618R2itS8uNxH-DkeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a19-R3tk3tWJf7NkyW5J2Uivf2Xl9oVsVCD7lZVFkiZasj6jrFfs9MDKhS_MyPuQuvJV13zTxIw4rzjFsMP0PR7fWQHYE6jQQ4qni6thZpXxvyt8Ds5HUXFWFvTpnJ0SVcnCrWClfzVLSZADagMOjhLyOs2y53gBached7W72BF6ajVdKGLOvsws4yj7DFqAFvZVcIr1WNAGF2pPemUtlLfmIx5Gm79WlkPwskL_2aWrNqObFE-OvHVUIqn4tzPFJ4DV2I5Pfnml_gNc4M_s8KGCOOlCo06zWjsX1l4-1xXLJiOZ5Kx08hm4lP0fTDDhyv_VDAIXiyOWTeGNLXh7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=tSF7YYKsruIYnciz5ceaoUIzyCEMNwkYR4EXbHsrn7dS-ERlJrcwJZGsS5ahACrgvWz6HM45fjVtBxNGKGmwK7nb9G9D8rXNOrtyKm7SR5PEP4CBDy6q9IYd2_xVWZZLZIaVStTbGQmoF4oTOUK18M2y4oy6jnIloYcJw_xGLS-S4go3nF-RDSsHqcEFsXUXIuLXOUS1Gfa2oxXQAKm24z5rqLYIekNHSXmzpi9jZvjJmoyH1TdLXIPFHfttfPErEUb8Kywi00Kjp_sgNUxACWJKszK4V8NOK60A9pTeVE0CsnA6RjY2y18M3XZKersjt692_AyTqXIMUHdSdQfTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=tSF7YYKsruIYnciz5ceaoUIzyCEMNwkYR4EXbHsrn7dS-ERlJrcwJZGsS5ahACrgvWz6HM45fjVtBxNGKGmwK7nb9G9D8rXNOrtyKm7SR5PEP4CBDy6q9IYd2_xVWZZLZIaVStTbGQmoF4oTOUK18M2y4oy6jnIloYcJw_xGLS-S4go3nF-RDSsHqcEFsXUXIuLXOUS1Gfa2oxXQAKm24z5rqLYIekNHSXmzpi9jZvjJmoyH1TdLXIPFHfttfPErEUb8Kywi00Kjp_sgNUxACWJKszK4V8NOK60A9pTeVE0CsnA6RjY2y18M3XZKersjt692_AyTqXIMUHdSdQfTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WMsghahcpFADXQYSPt7TcGiNgWKX4JBDqC-_2-_wdKY03d_7GFNEITLJqp2FFOcilZP77GRi9wH9f1VGtxjRO6tvkZIUHeMcetWlqWbUeDuK4VdsL2L1wk4I7QghKhfxT3781Zd2pQ9E8F4ZVcEXpTwguuJ2iItgUwG_nPMG_JR3F3TSUKhKfJeu1aQg2T88zqFFKVf2KRbaa-22Oo6vgiAHa3I7r382NlQhPi9ndpm_b7VBwAiuahyzzVIdHYEvW0lN5jYkTyvFY0xq9CRCJnoeuhPLFM5TX5wEremTlp4JVslrHHbkqb90XM4ciLXWebAK2mIE7k2nNmWUhMd0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SukYsMasXIOiwVcVwbOdNrEQSRSWzVpEJgrEEI9RYsyrAyPNv9wtcgOAb4BEiB2DRupFk4BuopGKBBtuPFi-4xsdH0rAoihhZto0OKgio3WZUQuGYoSU86l_z0omrgXBlkKjzmy2OMi9R1VIgpCGelzFK0yeXx8oLaSUFX8zsfZ7HSt6nUT98YAobVC-7_jESwz0xTeRPn7s2zv41DsinuF5UGApuq0qcnSikw154iY-rYhRHFEQA5VAWK8oerRSQRSBrPB_8Q3NSXZz1A0b1IJ6Sm5TLSpyR7J3AITsdxd5onU3p1HxzfbdMCxtLbCUzHg_Zy-aZCMWQzgW-t3Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdEYH3KtvvnEdio4kw49JwcfN5hujKMD3OrX_tl3rIZwHXeresM4HCRrLYdhGp_ckaDAmflrVZU87Ak35zCN2G3k185Y1bEL6NIR2cKoBZ-sC4Nsj7FpG6d2cEiVlA6ITGGiueGUPFzxMonX_8R5BEhBfoFVDKwjlm6d0pWNL6kfqvMt9uAEUpiaVU2Hx9MolbeYiobUUTY3sGnWAvPyUbOukYKSCpEPmQDuoPPLMCPWGzDS3JXiZsYqmXyH5WmY9jvc7pZxXVp68alhTwbOKnAvq1AUkkgKN901FVFLFyu5iO26aDjgm-wSVtLK2WhjnOT_NfW8YrPV6AvEU8oa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KoGsYfD_37YFMty__dTc6lcRYgPhgBaEWUUGifWNtsikEFU-6gxOU18IliockCKoF2UaZEalNMceApRL0MWR4I16sozIwWA64j_8bd4Y4iYM-GZxIHWYUWtFdk3WziU1755Ldhceuuys-cJDcPUamVbzUl6cGFUM2mGer6ECQuBgJFWXpK0fooKU30HReTyThAWpqzqCucjYldL4zBdYvrvjSM3cZrRfS2osXmSy6ibqzZv0VRZ9bYdLSS9XB5AG7-KPIMTWz0Eaqm8amWsorlURzpyF8tQJdhofBnJnI9yJQ2-8ZGcQI5P9B3cxY3va37Gu1di7Wveh9qfZ4lvnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=kwr-BGsiwWw-pxJotPrJbiSTFWk5A6l9ON9JpWTlmbw-zvG-WngK3IIIYD3xf4ml1IZdPD-QYeT65rzqq3j5845Xdv7q5_0LwqbLO4VEHiY09tG4PrHNYs6HQ6yLKStEZPvyTALUvXbuu2iA3U37fxXt2SdqR7fAr6Hao2Ge3Uli_cFRujHIWx9sN6_WnhPn0N75ZmkVk7oQ3pPv8m4JBqQUFk15AexfT9Diw1G0aO8ohFhlG9_4IFUlHw3YgAGxYppRtbre2c_6pCK0sSworYcM_gJcZYysgaCWHxpAeFNKVE_0Qbow95BlbjQEmljQQ-6vsUHZOn6UJzQ8KTTekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=kwr-BGsiwWw-pxJotPrJbiSTFWk5A6l9ON9JpWTlmbw-zvG-WngK3IIIYD3xf4ml1IZdPD-QYeT65rzqq3j5845Xdv7q5_0LwqbLO4VEHiY09tG4PrHNYs6HQ6yLKStEZPvyTALUvXbuu2iA3U37fxXt2SdqR7fAr6Hao2Ge3Uli_cFRujHIWx9sN6_WnhPn0N75ZmkVk7oQ3pPv8m4JBqQUFk15AexfT9Diw1G0aO8ohFhlG9_4IFUlHw3YgAGxYppRtbre2c_6pCK0sSworYcM_gJcZYysgaCWHxpAeFNKVE_0Qbow95BlbjQEmljQQ-6vsUHZOn6UJzQ8KTTekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7ejXXJ8B5Nucn-NTLazRkXeco3dTkWpz1sQ09fCPbnzvF2YYIIe4rnSTD2UW0ppc3AROpnc8nX5NCKTFjPANSAfhk0TubczFGC8IO9BsuSYvKdnfW7AvBZfoVggkwul-YeJVY-JV5KxjGsvCvSs6g9S_ekHYZ1Z7Ken4AjgcXKr1vYNIaRclHG2E_tewS8wmpPglt_F8MrdL_wOF5QFIJgP92niZfywmZhX9TfAn8KzNLVALjbA3n--19d4LYbzlY29mt75T9Ur8nqrq48avVXIHOYxRvSoumanKrFbyQJtrTIT7yi8xcfn52lPl6e8zl2TkVLhId6I6ngDmXX26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxnQgrKsNoVY8xlyCjmldVRWT7mEv8w8I83ErHHFcFvv6sKGtglEw4-lgR0SaPTeFL6Hmx2t4OzkIB8WqKIQIeo6sWh8Qv6jDDuzpEBYOcz5dIYWMa__kRGuhDUVcYt20r8xsehLOU6hVU7V8YTzg3swtOVRZnIcwaq3asgbxAfKMNCE6nAL1DukIYXrE6H0JtaUb-S2I-APLV6UZOtA8hmVVwNiWVVW0hunWd7a8sAWN8XnXO3W5TA3e7RAn9qDW7Qd3OoQmwvhRFg8qe7Co1K2VSQi9kv2Ec-n8G3HprffW6wBdA3NfjX3d5D9UN1PjQjF9N75LGkw3Ko0j_hq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2fEVmo9hNiZrtXXTjXAr4HEO38ONnttsTQXYDWUq_IB6qbL4Kg1bkbUxZj0o6sg1vcaq-y5E1w1X_9_FB-fSJVOD3fcZbs8b5-1gdHHYC_I39rlC9LdswhxzjAWdZqN1mIbrikl3BGx_unMxn8RJ_p1_04GckNRqvwN4TuiZ0k6JpCzibEB2EYOw4DHPwsoBYJ-tBT26glbb9uXe68Zdtdz70VfGJRpojr4gZpYBJbue5z_s3u_SW76nfrhIiSXnoQBnGvzPg1bi_0Z1CkSRmE8HurBDZM-zrcwsmA1Hj3xLss1argL8cxRcSzV-6P5sNTTcAp9DT1XfXxp17JvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pq5AHUzcI-ejv9gqoi05pysSatrMbimwQfISDSO_FG_d12DqO78mT8BhlpP4stSGJshGH02x2Mv8dSWsprEMjTz3If5sj5qzYHOs79Idx8TruNKJ152mdB9yg39LsfTAZ-En_GzQrFGspNlslgmpVgWIAFhW9AP6Ix6TjR-VDWtUh9jmmtF9caxcJx2LSFOrmRDX8bPAcDP3IHgGeKlLOpR8YX0zSDd29d7sVzc8Jl24sCDAk03fImHOOxD1omZjdj61Pab9Jp0RU1zEres_vkjFTT-pkG615piVR1-sKR6A05N5xjQR5NV7a3AMaRVH6ZC6jOSA01kqPHKw0AqCcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RtyxXUImWiae7P_BSi4vtCAAuFYLmH4w3iPOqXzoSXluW3DmZbTDUjUl28KFJ1gqYgOV8G09HVQzDnFs-FEdX8XQG9lfVSAqW3HYvEJ0PCwpxOtUgxB19MRuFwk6H7XfkVh80JdDNahBmCqp2cawSP3MzdoLzOOCji9mF_JGuJvcqKtbVLKMPYrNRN_90kKXrQldJ0d0Ae6QN8qS-_y-QA-j0H2UhipZ6OGS1YN-De6b3-scZbkng17AfSMS-9iOYaMeIYGjUE2_D0OLTSJf0-NwYWWe65zoeJPUr1TM_Zrigc958WyB4qj7djn9CbZp1H8u5x5XrceCiDnUo1qLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3803">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Whw4fTp0xj3tZ7PKGDtUnUQWYp36at2S_enq_ubF-xX_lRwmJQX1dftVvo54eTS8JzFJuNDRGGH8CB13yCCeDIfyNY3f8RtcUR-gU8ZDOYpeVcpRWtALSHOAUp-hdvaiUXvCmyWkowbRL2VGWKn4bNcL22WldThw3v1qiSgk58bkUqjsYsGKqx2YmpNTexgm_2cLHvTPny9oOfJ4gxLxP_QSd2pwX_TdI_WJ7uOIjfmgTLZyNATesv6Cv8rRL8DvQnIw1LnVp5eMqffTI6ch2icnEsmFerD5IRvcNpe434VUoO_omQsW4rF7WC0IibC9rTeJwUtJOfYfDwNzNxDVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یه نکته‌ی جالب از کنفرانس WWDC اپل!
توی ویدیو هر بار که کلمه سیری گفته می‌شد فرکانس‌های ۳، ۴، ۵ و ۶ کیلوهرتز صدا رو کات می‌کردن. چرا؟
برای اینکه وقتی دارید ویدیو رو می‌بینید، سیری توی دیوایس‌های اطراف شما بی‌دلیل بیدار نشه.
✍️
Behrad Javed
منبع</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3803" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3802">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگر از
http://Netlen.com.tr
بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار
یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰
باز هم خود دانید</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3802" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3801">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ببینید واقعا درک می‌کنم که ۶ دلار هزینه سرور و دامنه براتون زیاده، اما اگر سه چهار نفر با هم بگیرید بهتون فشار نمیاد. همه هم می‌تونید استفاده کنید
برای من سود و ضرری نداره صرفا می‌خوام بدونید که با نفری ۱۵۰-۲۰۰ میتونید راهش بندازید</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3801" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3800">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-poll">
<h4>📊 میتونم بپرسم چرا هنوز راه ننداختین؟</h4>
<ul>
<li>✓ هزینش زیاد بود واسم</li>
<li>✓ آموزش پیچیده بود واسم</li>
<li>✓ حوصله‌ام نشد و بعد از قطعی مغزم نیاز به استراحت داشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3800" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3799">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3799" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3798">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:  1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3798" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3797">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3797" target="_blank">📅 17:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3796">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-poll">
<h4>📊 آیا سرور MasterDNS راه انداختید برای خودتون و خانوادتون؟</h4>
<ul>
<li>✓ آری👍</li>
<li>✓ خیر👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3796" target="_blank">📅 17:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد. توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3794" target="_blank">📅 16:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3793">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tRChjmKxSplFmAmktCmWqTOwFTx4jxiN6SaEK9CklKV9wOwDsUtfExEYMKCPbU141PRsES8oyIRHuT_kPI9AS9ixvCN9v571ys1YDONv6IUT41xuPzIcmXmLeVLCo-OY-wpy9cPwsCJXOCu2kw5mllGpNQ77cMGTEZK92IV9oGbeWQgfoAaauDRkD-aYMsfYswCkssfQh1z7jpIthHfxPXO98lIMB0M4EcXFQpEsb8MmocCY8u3lZYaIq0RMx61QwB8ORK-9RkQYNmeMMjboP5Ko2MTnbmv1rXyw-zIbNbVy4wYxDkJYmiScvg7npSOBOsMs-ss2utZYRxjr7pp_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد.
توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه
و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3793" target="_blank">📅 15:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3789">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NV3nUB2M4BPP8T3qC6KGHE31IFiybXcRz_dNpU4B6Ipr8HObMvK_TXaezbzCqFgFOfxm2L2R3n5zKDzdopZCbIYmeFE6sAI0WOhqOtB-kPxM1SfLJgPhwNTJrRv2NgN4i1S9Ecw8Beiw13pYEk9t2Eq9ffbG7kFIRhid1feFvyzht38HRpYwcUszuDsBW86apUw7rredg22aIEkPfTh016KVnyTPSNcIMfrKqsNhadPMPQFPUWjIMbMaaOJYT6NynahjEQEKH1aRWTZ5Tpq4hc1sfwu71LqP5W_DAdvLqS7GcpQtXNy3aHcUTcbcnEO0Py0GAi9PMmWoVGONb_SlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PgGm7ifKrLz6R8Be-FYClFATmJP9ALXqdmEjWUZpCLJ6GtxbKPrlzVT9vp4uBretTY6EQhxazKEmK4CViQQTOzib-eBFCjAUZNiM0YxAFbf828OJUEJOEcqOdx5YHh6ckdUAT4NFcibVLhbrsz67UvcNHvMwBJZI6TpuDtVj1wdDSpDDIayBtJp3wMVbVWdJMfibAF0O1kUu1b8zICbges_WfKmKmT7RwJ6NOjAHalrEOKKOK2HT0yzNNuj8Pea2JCyszshGXxKqFTIGssU01wWGVcuB3X9QG0YtW2JmzY02Qo0fZBqc3eetOi2A75Kg6jSQVUtU0Y0cT0ff-T7cAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y0JugHBa3Yf67WDNYHi6mVKsvP0U3U7joCRT-KPDba24Lgq_F5M-pAAU42i1fStmuXBFf7gAczhGYJVWQ2b5uBEar9hBKPT_w9biE2jgKIPVGbKaysnKX5o8IZq9QRy-PRTYXZGywl3qsfceGh2WvVPgDzEtX1O_PTgd3mBoirSug4_ji0pACHfg9JoyIOsYOyUSD2mGwKxrsVd7ow2dyxFIke1sxkyD6XTRjrMB_5MnOpLCQknSeJjLVz6RrNFVX0oFT4D9YiFp38-0jShx9cDcUAp-CpXO7hOTxmU8It96hrJUUcOe5gQJZ9bMCvnI9k_l9V4MwL4Mdvv5NXvLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MHSHsXqLvXGQraZ4sUa6FefwGTrPj6P6SGSEqzPuMQJ_fVyHBH8uZ0XAsthrBI3NI0S5lRwRXy7AWJN0Rz0T5QBp21II64PzjTZpMZUcvzQmJA3leg4S2WaIM7HRNxPZ6LpgfbEmqyoPHnE-H-nTlilunwjb0RIy1MUrJRTj8rvMLhvLr9XH1R0V6ZjtqLcFKhUmgjXV2PFB0wpymd1nA-q8BxOwp_UkU1BFsmtcbeYSXXcC8gOBqaeSoTBxFVhZvXQBeVkYGIzOYLuUBvxJzZD46YVdl01BBb294vWhShsYRx4XEEGAPsQD2glfsjYoqcJwxlCpZ2ot3aOBGDtrqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش فعالسازی Fragment توی اپلیکیشن MahsaNG برای رفع مشکل سرعت آپلود و محدودیت اتصال توی برخی نقاط
روی Auto بذارید فعلا، من در ادامه واستون یه سری تنظیمات پیش‌فرض می‌ذارم که تست کنید روی اینترنتتون
اگر الان کانفیگ واستون با سرعت خوبی وصله، نیازی به فعال کردن Fragment ندارید. چون سرعت کلی رو پایین میاره</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3789" target="_blank">📅 13:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3788">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ما آخر نفهمیدیم جنگ شد یا نشد</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3788" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3784">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امیدوارم
WhiteDNS
ستاپ کرده باشید. برای اتصال توی شرایط جنگ
دیگه حوصله‌ی اصرار نیست</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3784" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3782">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اگر خواستید مفهوم فیلترینگ منطقه‌ای رو بفهمید، سوار اتوبوس بشید و از تهران برید خوزستان. به هر شهری می‌رسید آیپی تمیزهاتون از کار میفتن و باید دوباره اسکن کنید. به استان خوزستان که می‌رسید، گوشی تبدیل به یه پاره آجر بی‌مصرف میشه و فقط می‌تونید باهاش زنگ بزنید
😂</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/3782" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3781">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Izsf06APcUhDVd-CHBDGXRJ0zN1HxnjibEQBLdAy39xYWQPMzjRoJxhvUZYa6N7ehdpsv8L4Ea9-e53Yp4aJ3ebhc08VmRjIu9iugv9k3qnAQN73wMSDMva9zKB4R3rIxkSg5m0WCIBNXBj60z6jSnIpGJzHMX57Y1KSyEpoUJFBtQX9jNgVq7oBx9KLNATAnQS8wlxImc9kuC_Tu06K9ph920JlE0UIQfOmMkOZRs5cXV8__xlh_7XQ_XtR3kzVZJrjrLzYvD0VrW8Ql8KTGAbvP5EWEy6FF1BT-wHARAR_nwpOUi5vKACb7Rbudck-chRKgAIG7uohe_1q1V9OHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتشه یه سری حقایق راجب بورسیه MEXT ژاپن بگم.
حالم از این پوسترا مخصوصا راجب بورسیه‌ی ژاپن به هم می‌خوره.
واقعیت:
۱- از چندین هزار متقاضی، سالانه زیر ۵۰ نفر(متغیر) مجموعا از تمام مقاطع برگزیده میشن که اونم کاملا شانسیه.
۲- انتخاب شدن شما تماما به نیاز ژاپن بستگی داره و اصلا هم اعلام نمی‌کنن که ما به فلان رشته نیاز داریم. ممکنه شما تمام شرایط عالی رو داشته باشی با بالاترین نمره، اما «امسال ژاپن به رشته شما نیاز نداشته باشه»(مقطع ارشد و دکتری) و این رو به صورت مبهم فقط بهتون میگن که شما رد شدید! یعنی هیچ دلیلی برای رد شدنتون بهتون نمیدن توی هیچ مقطعی. شخص A با دانش نزدیک به صفر بدون بلد بودن انگلیسی یا ژاپنی قبول میشه چون ژاپن این رشته رو نیاز داره، شخص B بدون توضیح رد میشه با اینکه دانش و علم خیلی بالایی داره یا حتی مدرک زبان ژاپنی داره، چون به رشته‌اش نیاز ندارن. و فقط میگن رد شدی بدون توضیح.
۳- روند غربالگری به شدت غیراستاندارد، و رد شدن توی هر مرحله بدون توضیح هست(سه مرحله داره شامل ارسال مدارک و آزمون کتبی و مصاحبه که هرجا رد شدید، علتی نمیگن)
۴- ثبت نام برخلاف به روز بودن خود کشور ژاپن، به صورت کاملا سنتی و با پست کردن مدرک کاغذی برای سفارت توی یه فرآیند بسیار زمان‌بر و استرس‌زا(نکنه فلان چیز رو یادم رفته باشه) و هزارتا دنگ و فنگ انجام میشه. همه چیز کاغذی. همه‌چیز. یعنی حتی زحمت نمی‌دن به خودشون کد ملی شما رو وارد کنن اطلاعاتتون رو بگیرن. و توی همه‌ی ۱۵-۲۰ تا مدرکی هم که می‌خوان، یه نقطه اگر اشتباه باشه رد می‌شید توی مرحله‌ی اول. که باز هم توضیحی نمی‌دن بهتون که چرا رد شدید. صرفا میگن نقص مدارک
۵- شما ممکنه تمام تلاشتون رو بکنید، همه‌ی مراحل رو قبول بشید، اما در نهایت ژاپن توی اون سال Mext رو برای ایران کنسل کنه!! بله درست شنیدید. پارسال به خاطر جنگ ۱۲ روزه، ژاپن بورسیه‌اش رو برای ایران لغو کرد(
🤣
🤣
🤣
) صرفا چون تایم آزمونش جنگ شد. به تعویق هم ننداخت. لغو کرد. امسال هم همین شد دقیقا و به دلیل وضعیت کشور، لغو کرد. و تمام کسایی که پارسال و امسال هدفشون رو گذاشته بودن Mext، گند خورد به زندگیشون.
خلاصه‌ی کلام اینکه برای بورسیه تمرکزتون رو روی ژاپن به تنهایی نذارید و چندین تا کشور زیر نظرتون باشه</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3781" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3780">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RbFFZ_RzBxzxgKd0kX5GpOeow4ZBr5yHJPdwBYDyKkYLJOJISn9mFQcyzpRpktLh3RG48CE1QxMGmTBx8RPjY6_VBhb053ys6DD-xCDF0il4t7sGj5tWzQBRqpKHtpBKFQ6wOMs150hSNVH_6V8jT1yLQR64-aKj6RF4CYB-FwfZMDLMOW2-zJPIslK3bOp4pqM5sRvBwqJJG585t8w42XuhXiGcLcZH9bTVRpd1vzhN_WMk0796DWOaDh8yk3UpBBaE-O6jA2AGMm4-7qxdTcL8o-BTC6_ofTD8j2nCwn_amsysWMBI1S_g1hKk0chQLG9w5d4M23sHaBQe9h9sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
پروژه‌ی FreeLLMAPI — یه پروکسی OpenAI-compatible فوق‌العاده‌ست که ۱۶ تا از بهترین ارائه‌دهنده‌های LLM(مدل‌های زبانی بزرگ. همون هوش مصنوعی خودمون) رایگان رو روی هم جمع کرده!
تقریباً ۱٫۷ میلیارد توکن توی هر ماه ظرفیت inference (از Google Gemini، Groq، Mistral، Cerebras، OpenRouter، GitHub Models، Cloudflare، NVIDIA، HuggingFace و ... + هر endpoint سفارشی مثل Ollama، vLLM، LM Studio و غیره) می‌ده.
ویژگی‌های اصلی:
🔤
یه endpoint واحد (/v1/chat/completions) برای همه‌چی
🔤
روتینگ هوشمند + failover خودکار (اگر یه کلید به rate limit خورد، سریع میره سراغ بعدی)
🔤
مدیریت دقیق quota هر api key تا زیر حد استفاده‌ی رایگان بمونیم
🔤
کلیدها به صورت رمزنگاری‌شده ذخیره میشن
🔤
داشبورد باحال برای مدیریت api key
🔤
نصب خیلی راحت با Docker
در واقع همه free tierهای پراکنده رو تبدیل کرده به یه LLM قدرتمند و همیشه در دسترس، بدون اینکه مجبور بشی با کلی SDK و rate limit جداگانه کلنجار بری.
بهترین‌ها برای کدنویسی (بر اساس این پروژه و لیست هوش مصنوعی‌ها) عمدتاً DeepSeek V4 Pro، Qwen3-Coder سری (مخصوصاً Qwen3-Coder Next و 480B) و Codestral/Devstral هستن.
⚡️
لینک پروژه:
https://github.com/tashfeenahmed/freellmapi
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3780" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3779">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3779" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3777">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sglpRODtobp_D9r8bUUfH6m8qFKixGhR7Cg1aXAVzGgR9r3YMrTpcb9-pAdnmX87iPZl_4-uF9EVTamB3o63vKaJARccBFNym_5fsaeqYrGo-9qHobghnwTJaC7ax-DQ83IJGtZkDjVdggkZzmNTfjQ0uW8Qvn2q_EiGp4KwB3DB20n-2QSdKVecJBuRrtY84imXoDnRBxk84mzg7Zox7xtnYhQBmRMFVKNbLXAQulu7f8tku6m1BJqZVy4r-QH02ijE5wB6gfkD-2HWZX93GtATTleZTfxIWTfppwgQpJkWSHbj1qDTqlUmyeWoMZHjtaEY0gG4wzpg4hKg3znLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fOBKCx8VzGhZ1bLP_NNw8e0crnw4R9IGInwMDBGPHVDrtFgxFmor8q5t_eS7enuwZZ7DNdZwNQqljnWhhkvK936TJDcyjyTTU3wVWmKwhAWjVCRmQVgjtsGUEaZl7yt2ZhQl8n8m0Mapr6QIvjQl2z1XiRhzK7nb8DXb9AIibqJe0CXaJErUp202IL1PPr3NIVsP3xIfUdKitlZ3Sg2zhZykduY0JdfDqjhVHaHgnTRyM4sDk8HQLdIJunds4Mgh6dUP1j_L3we1Wwd1sL-7AnkM39jfdYtcL0uqmljVrJy3NS0GArxjIdgNvEDCRD7pQYOcy4nCYpEZOIiz994K8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بچه‌های WhiteDNS دارن رو یه چیزی کار می‌کنن که شاهکاره ایده‌اش
(عاشق UI اولیه‌ی اپلیکیشنم
😂
)</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3777" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3776">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QnLcuVctKJoRtr4fBi8Gpfzj3uAwIuqS1s3mqSvMPhk6icOyLnWMB-3GlUvKQ703A0vRE_Bd5NR8rEkC5m8h-q6uqDoLTuh5_zLUH4vWhwgVDSpI4Mjg7jv-7PAXVDnyArDQzGswgMzc33H1igCT9ultQkkzBbrKDkuOzZz6SmdnhdyAozsz1i4-OtuBTwcCGFraHWuq6harmaC--nJa3JTKHDOJx6jlVgWzYvxp2pxHaMRh9Ko4tk3F5rcoeu2-Ew9whrr90CaRXr4jPFvD67-ZyZmINtkBk3y5VE8YOSMc9MiQSUCheXSKgyGQSDPXxMoK4oiVLsylbMt2jAbaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!  این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3776" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3775">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=TwZuNVybUjFckfGGgsNcvLTgG8PfTFxqMWNwKDDhcfnwnrH9v8tg0q3ltQduEBVYz7juueJvte_DuzJUler9S8raEZhQ2jjTeovHcay0AryKIZNvmzo6YKNGwDSZenprVjURRAv8BWVwuRCKhF0tStaoUpzNVjyHZjpVpctNAKnMo8ri4ccqB5GhiXUJ46kWLyE65zpKug8aB2x_bx6Ns-Wpj1LRsdPl1BG3OHx2eTuHQv1DkEYCZVisfrpfOR1jXtJfHEFprnyAlznXd973w3UNJxxvkrKb8p2gMnXfEPhWE_nQzuK1ZIhsLkc_fUfPkx5uc1_IxVH4UQo60Zr7wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=TwZuNVybUjFckfGGgsNcvLTgG8PfTFxqMWNwKDDhcfnwnrH9v8tg0q3ltQduEBVYz7juueJvte_DuzJUler9S8raEZhQ2jjTeovHcay0AryKIZNvmzo6YKNGwDSZenprVjURRAv8BWVwuRCKhF0tStaoUpzNVjyHZjpVpctNAKnMo8ri4ccqB5GhiXUJ46kWLyE65zpKug8aB2x_bx6Ns-Wpj1LRsdPl1BG3OHx2eTuHQv1DkEYCZVisfrpfOR1jXtJfHEFprnyAlznXd973w3UNJxxvkrKb8p2gMnXfEPhWE_nQzuK1ZIhsLkc_fUfPkx5uc1_IxVH4UQo60Zr7wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!
این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.
همینطور به دلیل توانایی‌های بالاش، برای موضوعات حساس مثل امنیت سایبری(هک و امنیت)، زیست‌شناسی(شاید تولید سلاح‌های زیستی)، شیمی(شاید تولید مواد مخدر
😂
) و مطالب مشابه، از مدل ضعیف‌تر Opus 4.8 استفاده می‌شه.
همینطور همزمان مدل Mythos 5 هم معرفی شده که یه نسخه از Fable 5 با محدودیت‌های امنیتی کمتره.
فعلاً Mythos 5 فقط در اختیار تیم‌های امنیت سایبری خود آمریکا و زیرساخت‌های حیاتیش هست و ممکنه بعداً برای پژوهش‌های پزشکی و امنیتی به افراد مورد اعتماد بیشتری داده بشه. طبق جدول منتشر شده، Mythos 5 و Fable 5 در بنچمارک‌ها امتیاز بالاتری نسبت به GPT 5.5 و Gemini 3.1 Pro و خود Claude Opus 4.8 کسب کردن</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3775" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3774">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAgjs6tkjq3his7uYt4k47qt7C9nuBbGZSGbrNfR1pS9SOjT41MfLQ5M7-NBq4BqfEEI5M2Ilas7Xvd7ommId8nZpn-ybXLg5pr92TEzmx_B966DyflPbtFYq8T0tdrdeRPguG5XEXbVwwn-gBsZNieiIL_ZSrX35EnhESAePU4_LF7m86ydV5YD7ext-pqn4wlS2ufKpr1gVU263zbf3QwlhlhbVW8bkrp7fqYnu21_H2eE2-9QubTNQXp_kvk9vCLuwwZg_MAKetIByb126huktMo51dfqTypDxn2Awu-OAJk4kFMIqOPTwrkYXjxl2Zxpn5vEtKFoZN1XJDA9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3774" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3773">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3iTS3hLv7DIMsVW6pdPQNyCSxlGf7CsuEaKuxCDie9Kytv1qY_UuTF5Wgr88hc7YeY179MFtjM0Vi5NymsfJ9aIvzEZch7TiIQVniR3TtGs1bDDXvKkYZBUIwpTI_W0qYr_GcIKuh9OJC0L4T5RcgPTI1Y7l8EGRQP0pMubN9pcookaEyWjD74UuEZuU_0K37PdUOOizoT7k3IVmE4Yftck7j8aQb0yKepKXY5LndvmVUEG-MP9oz6Odi6yUdWLK4LpFTy2xWtX6Fp1fMctvUoeTUoRCu0GS8S392x8U9TJP0CIeEa-8c5HnCjIvPFwCoroNuQc_k5eQ80RzCznlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ساب‌ها رو می‌تونید توی هر کلاینت V2rayای که دارید وارد کنید و استفاده کنید ازشون</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3773" target="_blank">📅 14:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3772">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ساب لینک مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها: https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3772" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3771">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3771" target="_blank">📅 13:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3770">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/3770" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3769">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=jFuJgqw-mfsLRmB1e0ussRugFyyiRMaN8N1eJUGGxb3r93I8-HbF5HkZDK1wIryMSeDmy5xpSpgjO76siD8-AGpC7GQN9EhNx2Gzs17v00EdArI9gzcpZa4JSW0UyqbREQNLqQSeUrWTfGut2Qf0pWSpFbZSg1IEQEYYQ_dIDmCTOKdwLYYEFLlP2j80WIJS6cfA8FCH8sV2TdsLEdZSE0894fxfRwFWFWXEAI4GODyFp6akkpAaEvCAf3-AKB6yj4F2v_p_uza6fe7T8Gs1k6YoO4l434l3pL6MW5dsh6UcQAlu47QPuozbrtT5iFzrh0HECkRu2iEl-EQELsI52Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=jFuJgqw-mfsLRmB1e0ussRugFyyiRMaN8N1eJUGGxb3r93I8-HbF5HkZDK1wIryMSeDmy5xpSpgjO76siD8-AGpC7GQN9EhNx2Gzs17v00EdArI9gzcpZa4JSW0UyqbREQNLqQSeUrWTfGut2Qf0pWSpFbZSg1IEQEYYQ_dIDmCTOKdwLYYEFLlP2j80WIJS6cfA8FCH8sV2TdsLEdZSE0894fxfRwFWFWXEAI4GODyFp6akkpAaEvCAf3-AKB6yj4F2v_p_uza6fe7T8Gs1k6YoO4l434l3pL6MW5dsh6UcQAlu47QPuozbrtT5iFzrh0HECkRu2iEl-EQELsI52Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش وارد کردن کلید avast secureline
هر کلید برای صد کاربر هستش
اگه به لوکیشن گیر داد داخل نرفت یبار کلیر کش کنید دوباره کلید رو وارد کنید یا به نت دیگه و vpn دیگه</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3769" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3768">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=o7O5MaEbmAHcP-_VEVeNLSJVg2fuf-e6a0Qf791APoxEjWIPXf4eDodv_qafyd4_LxUa4x8t_8A7tr7Rk-6IKV9Ai9TW0IuJ25Z-8WRw4yM7HNnCuZlMf5G42JSa8JtAs2qAk55q6zJgshzEnZs5V5R1uZzdcAaFuqfa6u0CI3u0Z5R7mHmlVZJSP0BJYRpeho2QziSngetVuKt2HL2Jfgc7sHxx71O79rRsVuzb2sGuJH6WeQYkBTzUa-GY19HJSwmKeuVtvW72Yt_w0YFdM5NiB3M2ySSavyFxv9zsI4CWRd0UIhOVtQGObaEUc0xpwl78XJzym5llhRGH4hLrd76ZtGYqNssKpQLnko25XS3pwWiRHW6zCCycrdLMn3MufSHuc_evgxVNVvPX3vjqqHmsdqF1oMXOLzwYaN_2Tzo6HkP3mS7la3xrGzButDsR5PwuPfL8lZthPysWgIkcs1TRNyx3mGOBGFVDsU_vrBYbaeSnLshyImWpKZwwxab5uMryEg7djkKkjtU1pOwqjQrLcB5b2aJ3Pf8SU4kmaQYZ7q3XG5JE7fCUpEEa_B06vSG3iuvx6uzTh-RNhCNURf-aoB8kQ8nk9I-wcuYqpwC6mlEMmzVOguMs3egZskrAE73xFmzKlRqntIJQhZD9cAynbNZs6RFWAtWA0oFlFeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=o7O5MaEbmAHcP-_VEVeNLSJVg2fuf-e6a0Qf791APoxEjWIPXf4eDodv_qafyd4_LxUa4x8t_8A7tr7Rk-6IKV9Ai9TW0IuJ25Z-8WRw4yM7HNnCuZlMf5G42JSa8JtAs2qAk55q6zJgshzEnZs5V5R1uZzdcAaFuqfa6u0CI3u0Z5R7mHmlVZJSP0BJYRpeho2QziSngetVuKt2HL2Jfgc7sHxx71O79rRsVuzb2sGuJH6WeQYkBTzUa-GY19HJSwmKeuVtvW72Yt_w0YFdM5NiB3M2ySSavyFxv9zsI4CWRd0UIhOVtQGObaEUc0xpwl78XJzym5llhRGH4hLrd76ZtGYqNssKpQLnko25XS3pwWiRHW6zCCycrdLMn3MufSHuc_evgxVNVvPX3vjqqHmsdqF1oMXOLzwYaN_2Tzo6HkP3mS7la3xrGzButDsR5PwuPfL8lZthPysWgIkcs1TRNyx3mGOBGFVDsU_vrBYbaeSnLshyImWpKZwwxab5uMryEg7djkKkjtU1pOwqjQrLcB5b2aJ3Pf8SU4kmaQYZ7q3XG5JE7fCUpEEa_B06vSG3iuvx6uzTh-RNhCNURf-aoB8kQ8nk9I-wcuYqpwC6mlEMmzVOguMs3egZskrAE73xFmzKlRqntIJQhZD9cAynbNZs6RFWAtWA0oFlFeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Avast
Secureline
آموزش دریافت لایسنس‌کی یکماهه
لینک سایت
https://businesshub.avast.com/dashboard
فیک میل
https://temp-mail.org/en/
https://internxt.com/temporary-email
https://mail.tm/en/
https://temp-mail.io/en
لینک دانلود
•
Android
•
iOS
برای کانکت شدن از ی vpn کمکی حتما استفاده کنید
از پروتکل mimic و openvpn استفاده کنید
ÐΛɌ₭ᑎΞ𐒡𐒡</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3768" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3767">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ennIYcN1y8UGAeeIBcpjM7uB72G59c4m6VBoyr3Leqo6V26x3JLpA9VN7Sj2BK6IEon1Ch9XC-SJVUT5Pb944wH8pikO5Zrx4Ii5QoEHbttgLoITl-2Kblunq6TkZRg-UVUP4qDjR1vWiz9abdrqK1Ai4lpqN0GQ0TDkZloqT5aVAiQNWcmtbwECOwmf8cNYQ79Az9SC4dvKKaADrz0QlGf_A9PaYrp4spMMYMohoF-Uy63tqu7k8XvjQl0VWQmBLu4tOQanPNH5gA-f-sCBwE4aK_-HSdlErl_73_9rWg7RN1mQKEK0J4UgAsrsHI7xpLb8wFQa3jQhirYJKCisKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد وایب کده. اسم دیگه روش گذاشتن قرار نیست ماهیتش رو عوض کنه
و نه خوبه نه بد. بحثش به شدت مفصله</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3767" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3766">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برای WhiteDNS از
http://Netlen.com.tr
هم میتونید سرور بگیرید. فقط قبلا یه تایمی درگاه ترونش خراب بود نمیدونم درست شده یا نه
اینجا میتونید با شماره ایرانتون هم رجیستر کنید</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3766" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3765">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FG0Yw_a9NrhK1_HJSUl0vlSSYkV_7_uNwhNM9huKpbJVhcmTJ5B8ih4gLcqW1Z7H1Nr_limJsFoL-Zvm5SEiJpX598TxXMyGeZbrh3hdcipIu-1U01rzLalXk6DmYFWNklsXw8PiQOKfFF0KDwnmvzKa3GeA0Ulg_KFTbe7Dr7Kz25GeuhrDmtDp6WAzbmWxz7mKnYE6aDGN734KjMPi19OUOG9xaP8UkikSTDHMwNn2My_uscfaqJMgCCczgNSYHcZmOI6bKtZ_BMK3k-rpzqfHtAzlS8uAlNsfkcchucbojY5JnFxdsbvZPw5YUosKzm0Fk5XKVoQzulm6ppvZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام بچه‌ها:
متین جان لطفا تو کانال اعلام کن که از namecheap دامنه نگیرن. من گرفتم و بعد دو روز به علت تحریمات اکانتمو بست.</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3765" target="_blank">📅 13:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3764">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3764" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3763">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3763" target="_blank">📅 09:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3762">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان اگر خواستید از سایت yotta سرور و دامنه بگیرید، می‌تونید آدرس فیک از
fakexy.com
بگیرید و استفاده کنید</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3762" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3761">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Valid-08-June-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/MatinSenPaii/3761" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3760">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cf13d855.webm?token=dPUS1ziuxneAGGNk9C6WyiY0ylGHeYK_eOF6_uh189vUU1RKdZOrxJUevPBDn4pYDKps-xfgyAwqz-m1vNEvhOtSf4v9F7J02CXCxUP5BuEj6hn7WtgB5bFwRP6NqFO3FqEbPGP5UdhgfjWav7i9gayCoowTtTSlba7alYgMtx1ne3a7DiV8LoqKBOZ-QNUY0GNRmucrtuKlUHkvsw4DpEfCrtWlYrfEfyGqqnBRTJYH2jaaAbXST1fEj2YNxJiFUWLH7sL2D9xskurkf9aCpKL9Ni2PqwdwQsdmc2ob-MauVnFHzZw_p03DdvTDvO0O1IWBPpwWO3tT6Bgyu26p9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cf13d855.webm?token=dPUS1ziuxneAGGNk9C6WyiY0ylGHeYK_eOF6_uh189vUU1RKdZOrxJUevPBDn4pYDKps-xfgyAwqz-m1vNEvhOtSf4v9F7J02CXCxUP5BuEj6hn7WtgB5bFwRP6NqFO3FqEbPGP5UdhgfjWav7i9gayCoowTtTSlba7alYgMtx1ne3a7DiV8LoqKBOZ-QNUY0GNRmucrtuKlUHkvsw4DpEfCrtWlYrfEfyGqqnBRTJYH2jaaAbXST1fEj2YNxJiFUWLH7sL2D9xskurkf9aCpKL9Ni2PqwdwQsdmc2ob-MauVnFHzZw_p03DdvTDvO0O1IWBPpwWO3tT6Bgyu26p9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3760" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3759">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Valid-08-June-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینها 688 تا ریزالوری هستن که Valid بودن توی دوره‌ی قطعی برای من، از اون 5800 تا ریزالور ویدئوی WhiteDNS</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3759" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3758">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-poll">
<h4>📊 دوستانی که سرور دارید، دیتاسنترای ایرانتون...</h4>
<ul>
<li>✓ اصلا وصل نشده بود هنوز اینترنتش</li>
<li>✓ وصل شده بود، الان قطع شد</li>
<li>✓ وصل شده بود و هنوز وصله</li>
<li>✓ سرور ندارم، دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/MatinSenPaii/3758" target="_blank">📅 13:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3757">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/MatinSenPaii/3757" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3756">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هر پنج دقیقه میرم یه پینگ میگیرم ببینم وضعیت چیه
روانیمون کردن</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3756" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3755">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اینکه هنوز اینترنت قطع نشده جای تعجب داره به خدا</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/MatinSenPaii/3755" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3754">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مجددا تأکید می‌کنم که سرورهای عمومی سرعت به شدت پایینی دارن مخصوصا توی محدودیت‌های شدید و بسته شدن ریزالورها. تمام تلاش رو بذارید روی راه‌اندازی
سرور+دامنه شخصی</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/MatinSenPaii/3754" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3753">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سرورهای عمومی MasterDns(با کلاینت WhiteDNS):
1-
https://t.me/Masir_Sefid/612</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/MatinSenPaii/3753" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3752">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lT8l2ikUoR4zqmODfoG2ulpTVfgd5IrTOm2Z_EhcymXyeWrHvVsW-Q1gtYAXBlrSdcZd0RYXjKlRZHGRh5nCojckwhbYwNUrqYebZAkLrLTc6cJr4NR8faZ2r2aoD2yIVjmXWAdrv9-9MjAb5csrdGACxebLlC_cuBDjDJrelfXbiTuyP-M1FZbtcWMoFmmFo_FLyMukBVhGnZwzpANtTzMJr1xvnN9CEFB6cylKWYjjFYBYUdL6LsO2kjAf-sAKHBeNSRnj5hsE9ZRTaFWu1fXvBEJVWraGd76H5Hu8yUwfob2tPm9-E_hD0cR7ylpwy-BGZhagFAiKEFNThiicYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/MatinSenPaii/3752" target="_blank">📅 08:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/MatinSenPaii/3751" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/MatinSenPaii/3750" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y7Ls9DY2_xmza0P9cx2A5Ez1QzOEaCNS6NS-D2SaOArP0mRafq4d732ZjGZk1KqVPqQp0yEJPO4h6TZSzate_bzkF496Mx8Nc5kaNcDUpT0Qh1gKPl1q9Gz4z1V3n8ymDzOWyyXXWm0W385Z4mjuG_IbeQlSf7sbmg4kODHWWuDYCem-eBRu1s8CCw3afdj4cpCQeUkZX9xAxJfY1i2X4nlXvmR33XkB8N5MzwYeXCmIu-ezAkkU8fzn1yXeO0qwW7SBGSS3ihGlFwtCtf41Wuuif59DAZzP5QrfVZ2SsTgCxNfAOc0GKwt0oS0gEcDywojA0e9Eav_xrM_5ucPRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/MatinSenPaii/3749" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3748">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-poll">
<h4>📊 سرعت اینترنتتون؟</h4>
<ul>
<li>✓ تفاوتی نکرده</li>
<li>✓ یه کم کندی حس میکنم</li>
<li>✓ تمام کانفیگا از کار افتاده و نمیتونم به هیچی وصل بشم</li>
</ul>
</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/MatinSenPaii/3748" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3746">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Matin SenPai
pinned «
دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه. توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل: https://youtu.be/6Pm7kNQb3mo سر هر تحرک…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3746" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3745">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3745" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3744">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تا حالا حمله‌ی پیش‌دستانه تجربه نکردیم. اگر منطقی باشه، اینترنت به جای قطع شدن باید قوی‌تر بشه</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/MatinSenPaii/3744" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3743">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه.
توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل:
https://youtu.be/6Pm7kNQb3mo
سر هر تحرک نظامی و موشک مجبورم این حرفو بزنم چون احتمالش هست واقعا هر لحظه</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/MatinSenPaii/3743" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3742">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">تغییرات WhiteDNS Wizard v1.1.0
- خطای ACME و DNS بهتر تشخیص داده می‌شود.
- قبل از ساخت SSL، برنامه چک می‌کند دامنه واقعا روی Cloudflare فعال و درست تنظیم شده باشد.
- پیام‌های خطا واضح‌تر شده‌اند و کاربر بهتر می‌فهمد مشکل از توکن، دامنه یا DNS است.
- آموزش دسترسی‌های Cloudflare در README کامل‌تر شده.
- Reality XHTTP با Reality TCP Vision جایگزین شد.
- Reality حالا از
xtls-rprx-vision
استفاده می‌کند.
- انتخاب SNI برای Reality امن‌تر و پایدارتر شده.
- مسیر نصب روی سرور از
/opt
به
/var/lib/whitedns
منتقل شد تا روی VPSهای بیشتری بدون مشکل کار کند.
- مشکل ساخت فایل Docker Compose روی بعضی سرورها رفع شد.
- نصب Docker Compose Plugin روی سیستم‌عامل‌های مختلف بهتر شده.
- بیلدهای GitHub Release سریع‌تر شده‌اند و به صورت موازی ساخته می‌شوند.
- چند مشکل مربوط به مسیر فایل‌ها، ریستور، تست‌ها و آپلود فایل‌ها رفع شد.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.1.0</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3742" target="_blank">📅 21:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3741">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه جمله‌ی مشترک که از افرادی که پایتون اولین زبان برنامه‌نویسیشون بوده و بعد از اون رفتن سراغ یه زبان دیگه(علی‌الحصوص
زبان‌های کامپایلری
) زیاد شنیدم، این بوده که تازه با یاد گرفتن یه زبان جدید فهمیدن برنامه‌نویسی چیه. و درک و قدرت حل مسئله‌شون اونجا بوده که رشد کرده. علتش برام جالبه</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3741" target="_blank">📅 20:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3740">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3740" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3739">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید
https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3739" target="_blank">📅 15:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3738">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
|
پروکسی 2
|
پروکسی 3
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3738" target="_blank">📅 11:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3737">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVUavwQZmsIzZQyikxxSG6_HHvynadCW0EwARlzQprBEiqN6VprkB9LlJEp8vbnCac4Xtt9DXmYYz1X-WtUhLM3tKbU2KTnBeT2hJXS16iJab8xhjFwbzr7XvL85ysWuG0_ZGu5ghVstzQ1toPZQLc60m6pzmdtSdrlnYLvBUcdRamAy2wJIR2SRsiRzveXrZaSe-fr_62L0wXLe9VgqrnSZIi70gczL_xlQQX9vzdl0QAeO5565bN7qYxdpyycMUQonZAgbQibrdo1GZgypLK7zaDb3NJkGmWaloPnNg92vGGi9M764jfAQckU1gEqR-YWCn0NevJc89SA42KifXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه نهان
🍷
پنلی بر بستر
#کلودفلر
با کلی قابلیت به صورت رایگان و تنها با دادن ip واسه خودتون یا خانواده فیلترشکن بسازید...
ویژگی های این پنل:
✅
⭐
محدودیت حجم گذاشت
🗓
تاریخ انقضا تعیین کرد
🚫
دسترسی رو قطع کرد
✅
دوباره فعالش کرد
❗️
مصرفش رو دید
و همه اینا بدون دست زدن به مستقیم به Worker یا KV.
‏یه سری امکانات مدیریتی هم داره که بعد از مدتی استفاده واقعاً به درد می‌خورن:
⚡️
داشبورد مصرف
☁️
Cloudflare Analytics
🔔
نوتیف با بات تلگرام
💾
Backup / Restore
و چندتا ابزار دیگه که کم‌کم بیشتر میشن.
لینک خود پروژه:
https://github.com/itsyebekhe/nahan
@yebekhe
👑</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3737" target="_blank">📅 08:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3736">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🍷
یه سری نکات رو بگم در مورد bpb:  کانفیگ ممکنه پینگ نده واستون ولی کار کنه الویت رو پینگ نزارید  داخل تنظیمات اگر مشکلی بود به جای chrome از firefox استفاده کنید  اگر اینترنت شما 8.8.8.8 کار نمیکنه یا اختلال داره سعی کنید از dns زیر استفاده کنید:(کمترین اختلال…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3736" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3735">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه  نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی  BPB برای دانلود فایل…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3735" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3734">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏نسخه‌ 4.2.2 پنل BPB منتشر شد
🕶️
طبق گفته‌ی
برنامه‌نویس پروژه
، این نسخه مشکلاتی که از سمت کلادفلر بودن رو برطرف کرده
🔁
اگر دارید پنل جدید باهاش می‌سازید هیچ کار اضافه‌تری نیاز نیست، ولی اگر آپدیت می‌کنید باید همه‌ی ساب‌ها رو آپدیت کنید و اگر دستی توی داشبورد مقدار compatibility date رو تغییر داده بودید، بذارید روی جدیدترین تاریخ
طبق ویدئویی که برای آپدیت دادم
📆
تغییرات این نسخه:
1- بخش جدید External Raw configs:
میتونید ساب و کانفیگای شخصیتون رو اضافه کنید که همه‌شون به ساب Raw اضافه می‌شن
💪
2- بخش UpStream اضافه شده که می‌تونید به طور مثال
127.0.0.1:40443
رو به عنوان آیپی و پورت دیفالت بذارید(برای اسپوف) که به ساب Normal و Raw اضافه میشه و دیگه نیازی نیست دستی ویرایش کنید
💪
3- تغییرات جدید هسته‌ی Xray اعمال شده که حتما باید کلاینتاتون(V2rayNG یا هر کلاینتی استفاده می‌کنید) آخرین نسخه رو داشته باشه
😎
جزئیات کامل تغییرات رو اینجا بخونید:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.2
آموزش ویدئویی آپدیت از نسخه قدیمی به جدید:
https://t.me/MatinSenPaii/3732
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3734" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3733">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TgimhSgXD7ilHxIHZLSaQQcG2LXZsKZnGEJfo-Z8KHoPlukX2G1k5U8K3iWCjFRgHjC1qdMkFU9LpNnpeB1S5rMAN-VrFTqRGIi-P_sz1cTA_gPyjuSN_rs_1LJir2pCQr5wPxZoWnPKeF2k_Yi8PWnT7sF_TYy-htRWC7QPF7-3N3-HPNkw21uNjICrFnPEbfd8A2ya3rFe3CBDFb3xI_fvb2kpu6zSmb8JdFoGI91peet7SNCvQ9NYm2OX_OoW60NWHIVBtEf8w9Q7TGJx6St6UwKKBC1hAtVokoO79b6jCIEyMhKl6CwigM0DqMX-pcy2p8q_it9l2gOae0LLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار دیسلایک اضافه کردن به توییتر</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3733" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3732">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه
نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  BPB برای دانلود فایل ورکر:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
⭐️
توی این ویدئو بهتون یاد میدم که چه شکلی می‌تونید پنل BPB رو آپدیت کنید
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
قبلش باید این شکلی یکی ساخته باشین:
https://youtu.be/_aXy8wwyRG8
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3732" target="_blank">📅 16:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3731">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
1500 کانفیگ جدید به ساب WhiteDNS اضافه شد
.
همون ساب های قبلی رو رفرش کنید.
⬅️
آموزش استفاده از FlClash
⬅️
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3731" target="_blank">📅 15:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3730">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚠️
Confirmed: Metrics show a major disruption to internet connectivity in Pakistan-administered Azad Jammu and Kashmir.</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3730" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3729">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یک سری بحث و احتمال هست که یوتیوب فیلترش برداشته بشه، همون‌طور که گویا برای یک سری شده الان هم (البته مشخص نیست اختلاله یا واقعا داره رفع فیلتر میشه).
اینکه حقی که ازمون گرفتن رو بدن هنر نیست، ولی خب واقعا خوب میشه اگه این اتفاق بیفته و مردم همه بتونن دسترسی داشته باشن
♥️
همون‌طور که
قبلاً هم بارها گفتم
، ما یوتیوبر بی خانمان هم بشیم مهم نیست، مهم دسترسی درست هست و آزاد برای همه هستش.
اون یوتوبر بی‌شرفی که ناراحت میشه از آزاد شدن دسترسی هم بنظرم هرچه سریعتر آرک تمرینی نفس نکشیدن رو شروع بکنه
🫵🏻</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3729" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3728">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مراقب باشید سرور ۱۲۸ مگابایت رم و بدون ipv4 و اینا نخرید دوستان
😂
اونا رو هیچ کاریشون نمی‌تونید بکنید</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3728" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3727">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یکی از دوستان توییتر(ixAbolfazl)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد و کریپتو هم قبول میکنن مجدد یه سریا  آدرس: serverhunter.com</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3727" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3726">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OodEQ3HaUoBEgWTsz-WVkJn9CmzMN0p2DLhrKA1Okb_g3BlVlNqNFdEG4dSDSNuK9I7LzNNYDytcsjrldEFQnt9sahKFbXdr20PIQiaRmXDU3Jp8YVsUYjguNqPM92vj2bruACEYk99fPd1WA_KtTCIbMxCJJnTViJ2Qf-QJPxgq8RacYsZTWecs0ylmQoqBzvlhhNHYebQK9SvUZvNiKVKQn2xSbBRy5W3n_UXqJttGzJUut6vnsGurhb1GGyw8dV3PkRMMX0VoXOU5OwFHyFMUgptEL086b3esWHDB6c2Rs6yUxMX7wZcl-gm9OABOQdhcX-j6yy_pWhk6xEdLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر(
ixAbolfazl
)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی
یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد
و کریپتو هم قبول میکنن مجدد یه سریا
آدرس:
serverhunter.com</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3726" target="_blank">📅 08:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3724">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TJZFGwzwGlilVzxLAoZT6Vr6At7DDrMCzuneq7h_2dGomWyVFE--kNTW-320GCnyv4hbEtQunEmySsKqu1RefJ9i2T0afRbmu7kWzuw6wzJGofuQIXjjJ0Li-GgjMN6Wc-ZlCw16EnmlgtmDmwFIymPgKLGseUqTXJrYufqNYpDxBmIhzKg3-p_d5rDoZfvBUsUG2ERwbz1hdOU-Wl-wfVbRGauZ-kgdjJB2BpurEktbO6vSFZ-aZFkMPOy2oKSjDSr-acbieAVS-hha0wCbeHFpou3iDtmahqpouMG9opbjci4ts4tOvjTwraHZ_BG6d_RtGlSl0mFpwWGu71EbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i1C7AEyANkfpzi7lduKZQMF2hpfraRkiJfioOeYGgTTfs0grM244ggZCHy4n6jnPaJP8gjAupokaDonHht5oyq6bkTKtU1_PrD2XITaW3RXLDn8GEnwMZjphvj_q5MFvt6xrLJZQl7J3Qp6WsxwUGvx18gmlpH8syD7hnLIrUNsIPTSkAiOrlYhJ_yg8pXR7sf9Dp0OFtCtUYobBNnxe6sGWZVIj5Y4qy_kO_xk-1cNMDVZfMUVAldN3fClLdslZ7mkvZoqkej-xz4MMLztOO_4Cd7o-9XkXSMDpkpXxzmJOB39sWr9JwM_8sRyo4eAiJMNlC6-wh2y8aPlswNA3ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">والا برای من هیچکدوم روی ایرانسل و همراه اول نمیان
یه سری شایعه شده بود که میخوان یوتوب رو رفع فیلتر کنن
اما خب بازیشونه دیگه. سرگرم کردن ملت</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3724" target="_blank">📅 02:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3723">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EZkWfipw6c_RNujmdzg0LO3CT7Y5MOVS9GMbLJsOVOc8WuQ5SZ99PTLI58Gm8izHm97i54N0i1ZVo4CIkvxPrjZxnEUKe9F_s5Pp33NAy8i9tNdGkVQN9WuKxO5stmZvX0QQFEmYCqsF5d2BgDUD47lOEIS0zexwh3onPSd9izwfLMiMiglndtJBxkxv0iNJsnSNATkeXl-pSppbOB3p5JDU3d7KZbUMx3IIjBu8FAeH79soDBJBfICfB6EwRtBfRgUv0vb3wGeLRAmXCxauczxjq_L8O-otsZMI9E19HDphmYja0HY91y7Wl-_iauqJk2bM0t-o3aiUnnslo6FCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شما هم این شکلی شده بچه‌ها؟ با لایک و دیسلایک بگید
شنیدم این رو چند بار از سر شب</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3723" target="_blank">📅 02:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3716" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بفرمایید تست کنید. ورژن 0.6.0</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/MatinSenPaii/3716" target="_blank">📅 02:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bx9eHJNXp-iWO6xkp2BLXbScSuCPxr_h-5KR78Ae5xw6MZk3EMiojgE9MluNm8LO8vbmPz5T1k0WnQA28lS3vO37WLNs5VpgZbstKMJSGfwKLS5SY1NuCKqACRH6bu_wiYSmlKMu-Za_meo2m3c6TnmpzrHyUDc40Z3BF3kaLEJf8qZR6TM2SBd1fYiqwvdcdhlQ420fTnkTMREg1esLw_h7d1aO0BAJStY8mQdZ3RKT3gyRoIZkCByOfcBrzjnvt2UTkMB4OjaryufWI74AS0CpLgKPvQ-9hfMqAouH9fcg6-HJSnkBOxEfAx0V6pY1DbqkjhZHppH4SH-4cQya5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3715" target="_blank">📅 01:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3714">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3714" target="_blank">📅 00:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TDiaf_C1n6L_jmPmw7iEPGj1JkHglTTbEFzpNophZRbcoYNG1rOnO2wtf5EAJi395LyAnelkWVwhfBd-XTJDCUJ8p2SAf1AmNC2kmSaNw-4LGHdo0DBtG-gwVb8p1KCeCPj786Dh5oRMmygeZu8TYWeBf-CdLCOiatdZ680bxHWaQ_Gr4Wth7qBeaJWOYvI5B1u9b5jBNpoPEorpt7SXHiYQhouL1r-QrLLGOrTp61_k5YJzKgVXbpFQSh48wr1bHEKcomc8H1C41WYlbsA-qztVN56pvyOz6v4TYfSLVidpmSjnPYTXRgeTUlL2ASwf68hx-HPJYijYeH6j_xfE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3713" target="_blank">📅 00:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3712" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3711" target="_blank">📅 00:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3710">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NY9jdFS1xg5n2BXfuJGnhJ4MTxPXkdqG8_snr0rVvdLowIf0NwsvZz6H24wPIvlhJmPlQR0PKs_bxoOly59Sz9f-ESSCP6hVBVXcPFOwNEo4347p1IA38T4hgdJhcjIKX_H0VWQS1YRx2i5qDKr6GuZ8MJZ4QmYE1FO2AGzytCgu6M0N7pCX2FzTiRQIBLAQJVMKh2cEYlP_bQ9BWww__7G8skt1z6bgE2VevFDeKYkVQJFEzs3cBvSaMq6zypDpWfE09UANoiLiDWjCfxDaoFWCS984soRrz8KvO9dp89PcimGUMzpY1N3yCU3siLc61zInhD57605afU7YRnKkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس WhiteDNS-Wizard برای کسایی طراحی شده که سرور و دامنه خریدن، و حالا نمی‌دونن که با اینا چیکار بکنن
👍
این نرم‌افزار مولتی‌کراس پلتفرم تحت CLI اوپن سورس، از شما اطلاعات سرور و دامنه میگیره، به علاوه API-TOKEN کلودفلر، و برای شما صفر تا صد کار نصب پنل، گرفتن سرتیفیکیت و ssl و ... رو انجام میده. و این خروجی‌ها رو میده:
1- کانفیگ VLESS WS شخصی
2- کانفیگ REALITY-XHTTP شخصی
3- کانفیگ Hysteria2 شخصی
4- کانفیگ Shadowsocks شخصی
5- کانفیگ Tor vless ws
6- کانفیگ Tor Hysteria2
7- کانفیگ Tor direct
8- به زودی مستر و ... هم اضافه میشه
آموزشش رو هم داریم با آپدیت بعدی
گیتهاب:
https://github.com/iampedii/WhiteDNS-Wizard
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3710" target="_blank">📅 22:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXQt1zS9ZYXUpCn4eRgPRZTkcHhwPpR44ZTsLfJQAF-IDEv6IgUsrfjSsVd_3VgRKRmtX0D77V3QsNdPzqOgfMtDEWd2LSxfyX2G-YisIaXbq80R9P8XgxIOywyL8yVZNUqo7UueLsza_qHOfLwCjunk_9vL9-jPRrK5KLeCKyiY6BqHL0VWf7chrrYW6DTvnnHin063Achcb78NXEAHXtYY862Jm7uK16SBOjDizGDeWbmRJP5Mk0_w32CJ-rSedeThiJGSmRyV2GsWXaGGZ0-6fCxLwqwgncmB4keeflCC4TGakXieYe6TkVppIQWlWlUXZ0gfzhw4zsctHYkm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AzadiTunnel نسخه آیفون شیر و خورشید
👑
یک اپ iOS برای اتصال امن و پایدارتر، با تمرکز روی تجربه ساده، CDN Fronting، DNS هوشمند و تست اتصال.
📱
لینک مستقیم اپ استور:
https://apps.apple.com/ca/app/azaditunnel/id6776486891
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3709" target="_blank">📅 20:27 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
