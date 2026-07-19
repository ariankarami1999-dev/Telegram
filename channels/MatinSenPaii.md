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
<img src="https://cdn1.telesco.pe/file/Y9zlHIxOiiwNvfMwAR-jO60FMuCUe-dS-kuxKiv5H6bcY6pbJTkD39tSV_eu9uWD6WTn-Lp6DC-sAZBHH0qIPuYgj41JulYyqA-4r1-vGSvD2IGAWiyFuS4OqhjJdi6UqjZu8vN2Q848ZgpJK5TJSLZG5rNAzRxLH3gEkgQuHj3AaDDvR4A-skiGiR9YPhd0AqWhkWBQcB5j3AY0gSImrwenyWOX7YrqAyuMKey3jLON-c8o1VYXHTMY5BrDMW_YmmFDPTCHE7m-Jha8Hd4DauIcoqWk9aYWuJh6zopEnph2v5K9qd0gGdyV09ZomsVzGII9ucDB8d9RlN8p1UDE8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 02:54:57</div>
<hr>

<div class="tg-post" id="msg-4578">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گویا شرکت Moonshot ، توسعه‌دهنده‌ی مدل چینی Kimi 3 انقدر به خاطر تهاجم مردم فشار اومده به سرورهاش که کلا فروش اشتراک‌های جدید رو متوقف کرده:))
همینطور اونایی که قبلاً اشتراک ۲۰ دلاری رو خریدن هم شاکین. چون مدل سنگینه، توکن‌ها خیلی سریع‌تر از مدل‌های قبلی مصرف می‌شه و کاربرها می‌گن بودجه‌ی هفتگیشون تو دو روز اول تموم می‌شه. (این رو با مدل قبلی یعنی K2.5 که خیلی به‌صرفه‌تر بود مقایسه می‌کنن).
توی فروم‌های تخصصی (مثل Hacker News) بحثِ جالبی راه افتاده؛ خیلیا می‌گن دقیقاً به خاطر همین مشکلاته که ما باید به سمت مدل‌های اوپن‌سورس و اجرا روی سخت‌افزارهای خودمون بریم، وگرنه حتی بزرگ‌ترین استارتاپ‌ها هم یه جایی زیر بارِ ترافیکِ مدل‌های هوش مصنوعی زانو می‌زنن.
هرچند توی ایران متاسفانه نمیتونیم زیاد به همچین چیزای گل و بلبلی که خارجیا میگن واقع‌بینانه نگاه کنیم</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/MatinSenPaii/4578" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4577">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هرچقدر بگم هرمس برای تحقیق و پیدا کردن گسترده‌ی یه چیزی عالیه کم گفتم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/4577" target="_blank">📅 23:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4576">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبر فوری :  ‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید دو تا باگ SQL Injection و RCE داره  نسخه های اصلاح شده: WordPress 6.8 → 6.8.6 یا جدیدتر WordPress 6.9 → 6.9.5 یا جدیدتر WordPress 7.0 → 7.0.2 یا جدیدتر    @Linuxor ~ seramo_ir</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4576" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خبر فوری :
‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید
دو تا باگ SQL Injection و RCE داره
نسخه های اصلاح شده:
WordPress 6.8 → 6.8.6 یا جدیدتر
WordPress 6.9 → 6.9.5 یا جدیدتر
WordPress 7.0 → 7.0.2 یا جدیدتر
@Linuxor
~ seramo_ir</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4575" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IyflgtsFv0v75GEc6D2k9mMYt3ScQ4Hte3VK1fA94HRAR_f07-1eltgDH-kVj6cegl3C290xe9eIgJb59-4o1AFy455QELBusLISILUJYo7aYjTDIzed_6SQTXkSuAfrdncFAI3h9cji_GDmAYG4mMD2iy9Zk-aLY2r0vJ7ReHyBbVobuCdbhhUnl5dJbpU5SCP5qIfBFrQX5ALa3HnPSSbXEUXndFzCe-DQwXMKhfyF5xsvZ1O-wQkpKrdN-MLNUzP_KlyTw-GgU8gUbRuS_cIBqahDQHbPRgDs3NVJ6qzaeTyxGMMxgEfiD-K7EfbIeDcQByO6bcJEoManqpFYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌های متخصص امنیت (که توی حوزه SOC و Red Team فعاله) یه سایت و کامیونیتی زده به اسم VulnCity (شهر آسیب‌پذیری‌ها). که یه مرجع جامع و دورهمی برای بچه‌های امنیته.
1- مقالات و آموزش‌های دست‌اول: مؤسس سایت هر چیزی که توی پروژه‌های واقعی (مثل Red Teaming) یاد می‌گیره رو به‌صورت مقاله می‌ذاره اونجا.
2- شبکه‌سازی: بچه‌های امنیت می‌تونن با هم چت کنن، پروفایل همدیگه رو ببینن و یه تیم بسازن.
3- بخش Vulndark: یه قسمت باحال داره که اخبار مارکت‌های فعال دارک‌وب، فعالیت گروه‌های هکری و خبر لو رفتن دیتابیس‌ها رو پوشش می‌ده.
آدرس سایت:
🔗
https://vulncity.com
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4574" target="_blank">📅 20:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فرق H3 و H2 برای من روی یه اینترنت، 18 و 2 مگابیته
یعنی H2 سرعتش پایینتره
همینطور وایرگارد و gool هم برای من همون سرعت H3 رو دارن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4573" target="_blank">📅 20:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">من حس میکنم به قدرت gool پی نبردید
یه تست بکنید جداً</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4572" target="_blank">📅 14:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-poll">
<h4>📊 حالا دوستان MASQUEـی، بهم بگید کدومش بهتره توی آپلود/دانلود؟</h4>
<ul>
<li>✓ http/3</li>
<li>✓ http/2</li>
<li>✓ مسکی نیستم دیدن نتایج👺</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4571" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-poll">
<h4>📊 توی Aether بیشتر روی کدوم پروتکل بودید و براتون بهتر بوده تا الان؟</h4>
<ul>
<li>✓ 1- MASQUE</li>
<li>✓ 2- Wireguard</li>
<li>✓ 3- Gool(warp-in-warp)</li>
<li>✓ استفاده نکردم</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4569" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4568">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر دنبال یه آرشیو کامل از یاد گرفتن ساخت کانفیگ با سرور شخصی و تمام روش های
#اینترنت
آزاد هستید از مبتدی تا حرفه ای میتونید از این آرشیو کامل که یکی از بچها زحمت کشیده و آرشیو بسیار کاملیه استفاده کنید.
لینک سایت:
👇
(باز نشد با فیلتر برید)
filtershekan.sbs
خلاصه:این سایت برای تمام آموزش
#امنیت
ساخت
#کانفیگ
و تمام روش هایی که شما رو میتونه با کمترین هزینه و رایگان وصل کنه رو گذاشته.
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4568" target="_blank">📅 13:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">اطلاعیه:
سطح پهنای باند و کیفیت اتصال اینترنت در تمامی اپراتورها و دیتاسنترها به‌طور قابل‌توجهی کاهش یافته است. بررسی‌ها نشان می‌دهد ظرفیت پهنای باند نسبت به روز گذشته کاهش محسوسی داشته است.
همچنین برخی رسانه‌ها از اختلال یا قطعی در خطوط انتقال پهنای باند و زیرساخت شبکه در برخی مناطق کشور، به دلیل حملات منتسب به آمریکا، خبر داده‌اند. :))</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4567" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آپلود عملا مرده</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4566" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ENGJgkvs-NfH7Oj8eu7Oq2n9tHsq6zHpq8ah-oIxBInUwyTUkq0gxEhT-P45jO8j4RelvnT9nKfIW1zFuiM3ZGzxlmx-hR7H3LfduZWt6JhfkqdhKOcY6itcB8780xVEiPuo5fKu5gXvkK1-cV4v07yuBbu0rRGeubalKA02hTfl0ZISxu8FowSP3SwzGTTZZmc8iSvRJYB34E3cjyPlpRQVVviEGKCMJa_259nJC7siaAZaVhuTlVCI9EuEvYGTHSXcg1xHzbiw7x4qei1OemwhD-BkVcfpqjg9tlRQE8vhWk7P5IetwSk67RVkTxwXnP_A-x1fWiFAIcNPbunKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کپچایی بود خدایی حالم بد شد
کم کم ما ربات تشخیص داده میشیم،‌هوش مصنوعی انسان</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4565" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=jEzq7jqhHaCWgJq5k2Qa_K8YeMKF9k5ttRItwzOy-eX2x1ZA4vFLkkYoGMb8JX2ZFc70voQPNrd1RSaGjg5_E2wIFv-RItsSxiuHmWdwqkRjZ2gJ0t-NakXHnDq-LAIBaHCaqFHUSisdpKLEW9ob6udf3d-WA2pFrIg4tAa6zHyF9Z9XlSPppTxooU4Ytcvmh9BTdfsRYr7lTaNeLM7VFkepU6UFD4NeeYUtbzVDuUU2F6aEEmjzp05DelAIkVrFeuO9IqESatlXOiXK-RkkYMGvgINqeaNxJuGySL3lOHta2JoSP-bufPFiLoTSYJE7vi8YRZgtHfG1N5Cml-gdog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=jEzq7jqhHaCWgJq5k2Qa_K8YeMKF9k5ttRItwzOy-eX2x1ZA4vFLkkYoGMb8JX2ZFc70voQPNrd1RSaGjg5_E2wIFv-RItsSxiuHmWdwqkRjZ2gJ0t-NakXHnDq-LAIBaHCaqFHUSisdpKLEW9ob6udf3d-WA2pFrIg4tAa6zHyF9Z9XlSPppTxooU4Ytcvmh9BTdfsRYr7lTaNeLM7VFkepU6UFD4NeeYUtbzVDuUU2F6aEEmjzp05DelAIkVrFeuO9IqESatlXOiXK-RkkYMGvgINqeaNxJuGySL3lOHta2JoSP-bufPFiLoTSYJE7vi8YRZgtHfG1N5Cml-gdog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : ترامپ از کشته شدن سربازانش بسیار عصبانی و خمشگین شده است.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4564" target="_blank">📅 22:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سرعت نت من به شدت پایین اومده. از 30 مگابیت به 2 مگابیت عملا. با و بدون وی پی ان هم فرقی نمیکنه
نمیدونم چه گندی دارن می‌زنن باز</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4563" target="_blank">📅 21:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رفقا یکی از دوستان من به اسم محمد، خارج از کشور هستش و برنامه‌نویس Back-end با بیش از ۵ سال سابقه کار هستش و روی پروژه‌های مختلفی از جمله سیستم‌های رزرو پرواز، پلتفرم VOD، مارکت‌پلیس، سیستم‌های پرداخت، احراز هویت، پنل‌های مدیریتی و معماری میکروسرویس کار کرده.
تکنولوژی‌هایی که بهشون مسلط هست:
Node.js • TypeScript • PostgreSQL • Redis • Docker • RabbitMQ • Microservices • Prisma • REST API
هم برای همکاری Remote میتونه اقدام کنه، و هم اگر فرصت مناسبی باشه، برای Relocation مشکلی نداره
حیفه که از چنین استعدادی استفاده نشه
😁
لینکدینش:
https://www.linkedin.com/in/mr-ln
آیدی تلگرامش:
@MRLN2001</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4562" target="_blank">📅 20:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این وسط مدل Claude Fable 5 موندگار شد.
آنتروپیک اعلام کرده که از ۲۰ جولای، مدل Claude Fable 5 رو توی همه‌ی پلن‌های Max و Team Premium (با ۵۰ درصد محدودیت‌ها) نگه می‌داره. کاربرای Pro و Team Standard هم می‌تونن با استفاده از Credit بهش دسترسی داشته باشن و یک اعتبار ۱۰۰ دلاری هم دریافت می‌کنن. به نظر میاد فشار رقابت سنگین با GPT-5.6 Sol و Kimi 3 باعث شده آنتروپیک از برنامه‌ی قبلیش برای حذف کردن Fable 5 از پلن‌های اشتراکی عقب‌نشینی کنه که خب قابل پیش‌بینی بود
🤤</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4561" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مدل Kimi 3 اومده با context یک میلیونی و به نظر خیلی خفن میاد
هرچند همیشه گفتم به بنچمارک‌ها اعتباری نیست، باید در عمل دید که چیکار میکنه</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4560" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از بچه‌ها به اسم ارشیای عزیز این ایمیل رو بهم داد، برای خرید سرور:
من از hostvds خریدم. ۹۹ سنت هزینشه، یه ۴۹ سنت خرج می‌کنی ترافیکش‌ نامحدود میشه. هزینه رو یه دفعه کم نمیکنه ساعتی کسر میشه. اگه یه دفعه آیپی فیلتر بود میتونی سرور رو حذف کنی یدونه دیگه دیپلوی کنی.
پرداخت کریپتویی داره
با ایران مشکلی نداره
۲ ماهه باهاش مستر dns و پنل ثنایی فعال کردم.
پایداری و سرعتش خیلی خفن نیست ولی بدک هم نیست.</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4559" target="_blank">📅 18:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TDt4x0VlPBy4oFGG6Z_sTNXD-_aE_aAsXjV4mLVJXVMp6RafSjlwx6qch1lIgMk0h56LJmmHygLjire5T0X7zUAeXI663wUVm7Y0KpVTUe8Jh6vGDhi_kqNYZ7vL1AelgR1eN3cu29tNEaVLuW5y7-sxV5OMCnH6iBgl3GlqNUAYMOVjPIJQP60zUPdXeuliJm4AH1j0LYcGKpOAdg3Zje6xl075JjgJ_sbIUY76SwcmgbqSGwQSHdtGzWJFZo_EkEIrFSIM9yApPJZBeGoTQ6sXgXd_yzBTDv6XAHJmzkH4cy_D4HXFepgKlNT4yfL2QWtyNzM_xkigPffGvaCwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان گویا yotta src روی سرورهایی که برای masterdns استفاده میشن، ابیوز میزنه و سرور رو بدون اطلاع قبلی می‌بنده. لطفا دیگه به این قصد ازش خرید نکنید تا اطلاع ثانوی
و میگردم سایت اوکی پیدا میکنم واسه‌ی خرید سرور با کریپتو باز هم</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4558" target="_blank">📅 12:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">پاول دورف و ایلان ماسک هردو گفته بودن اگه دانشجو هستید بهترین چیزی که میتونید یاد بگیرید ریاضی و فیزیک هستش
راستم میگن اما حرفشون یه اشکالی داره، یادگیری ریاضی فیزیک برای پولدارا و بی دغدغه هاست، برای مثال به خصوص توی ایران یادگیری ریاضی و فیزیک درامد خوبی نداره و شمارو اصلا وارد Positive Feedback Loop نمیکنه که توش پیشرفت کنید، ولی واقعا راست میگن من خودم اگر هیچ دغدغه مالی نداشتم تا آخر عمر ریاضی و فیزیک یاد می‌گرفتم چون جز بنیادی و مهم ترین ابزار های فکری بشر هستن!
@Linuxor</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4557" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان عزیز لطفا مراقب خودتون باشید و توی جاده و نزدیک پل‌ها تردد نکنید اصلا
خیلی خطرناکه این روزا</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4556" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6tJ8kjTjFPpC-tvA6Xc_u7RbC0GHHkg2nNk_45YV83sFvQdo2b0cwwSpj9qho-lVV2KA6cB3SfwQhqvjrxMnMEa3dQJrzNq4_BcgH08iKfe-5hzYrv0P_ns7ytqF2WEt3ozbKJ87Ea3QEMzqrvGLjJn3GANVt_ZYu7B2Cb7vePh7PGBGPFnQa4RZzCmMsUzrC8-sI_DBP6xFNPp4N-p7cVlXR3mDdENaPSqr3wNQnRuhWqK0CnXkezZ95cXLKX9lmfK44PUeT8jPgY0Eo49sWiVxRv65OhB6MB08dLHRItDa5VtP3PsU9G0E0JRCQZo3a0mR6iCJbq0vuhjh-m6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسایی که تا الان براشون کانکت نشده بود، یا کار نمیکرد، حدسم اینه به احتمال 90 درصد واستون کار کنه با تغییر پروتکل ارتباطی Masque به http2. من تا الان Masque روی نت مخابرات واسم کار نمیکرد، اما با این ورژن جدید دارم همین پیام رو میذارم با MASQUE+Turbo+Ipv4+Http2</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4555" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4554">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید! نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن 1.2.0 ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک: قبل از این، بخش Validation ابزار با پینگ…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4554" target="_blank">📅 02:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZsjvovrChEKplolzVhz6aUILldxcSU2iQg-fcBOCzewAXTpjHYwon17c8sxzsjyrVjsVQ4YNCGOgdmsJwMaCDRNDn7R_tBUlxL3KiA5onYjMjGoOGURaomvRCfT6ewXtMK52ifinXkhyMuL3pY4FohHFPyUWGWF41dnsdW2MqoJGfg8gFeoSIlOI4q8VXSrIqTwauh7pS3OWE7ZRqzgxhq_HT829apAVkMjSuDKJwQH1TBBqYknfW6vyBl21jTuSOWlhoU8IXCUY8NxcwibOq3dDUJgQvz_QXx7fM_moRDDQ4mWXx6GFZL7lNTyNqL1l1mkRbYIoYkCE1wckW1QoMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kp0lkONmZwr0dL8FtU6ZHL7hfX3hKrXEdZydY2ZaafbzmOzVxP-5Ls9k9Sj8yyQaBDMMpF5txUNtlqtu1joCjM_zuTzWsy4f6VFb4BBtKrlWv3TBouk5lvknwMw3Z26fDgN2H0zo-zGPTsrabTvLm2b_-h6jPWCqSICyWoHgnsu24DIVJLQN_h6tiMyXLSk29-IptZNecO8V7iBh6ACzcUjUoJdR1u2-yDPf5w0AqeHH03zlacFEwd2VneAwkTq24R1pdxB-IQY4gjEW1tHk-EH3lbOmXtOYCdcjnABNh7HbunYkMPGbMU4eF4bDmPUJHGzqjBIXYthZZS_6eL5wAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/4552" target="_blank">📅 01:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به زودی به GUI هم اضافه‌ش میکنم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4551" target="_blank">📅 22:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether منتشر شد.
v1.2.0
چند تا مشکلی که گزارش کرده بودید توی این نسخه برطرف شده:
- مشکل اینکه بعضی وقتا تونل ظاهرا وصل میشد ولی هیچ سایتی باز نمیشد فیکس شد.
یعنی SOCKS5 فقط وقتی باز میشه که مطمئن باشه
تونل واقعا کار میکنه... :))
مشکل دیر reconnect شدن روی MASQUE HTTP/2 هم برطرف شد.
الان براش HTTP/2 PING اضافه کردم و خیلی سریع ‌تر تشخیص میده.
اسکنر MASQUE هم بهتر شده
چند تا رنج IP رسمی Cloudflare که برای MASQUE استفاده میشن به اسکنر اضافه کردم، همراه با پورت‌ های بیشتر
در نتیجه شانس پیدا کردن Gateway سالم بیشتر شده.
موقع اجرای MASQUE هم دیگه راحت میتونید بین
HTTP/3
و
HTTP/2
انتخاب کنید.
کنار هر گزینه هم یه توضیح کوتاه گذاشتم که بدونید کدوم برای چه شرایطی بهتره.
به طور خلاصه:
HTTP/3
برای شبکه‌های عادی و سالم
HTTP/2
برای وقتی که UDP یا QUIC محدود شده
لینک پروژه هسته:
https://github.com/CluvexStudio/Aether
اگه خوشتون اومد از این پروژه، میتونید Star بدید بهم :))
Readme
هم بخونید حتما!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4550" target="_blank">📅 22:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
فیلترنت به طرز همیشگی افتضاحه و عملا سرعت آپلود نداریم داخل هر پنلی چه کلودفلر چه سرور شخصی با ی راه وضعیت بهتر کنید.
دی ان اس گوگل اختلال زیاد داره داخل هر اپلیکیشن وارد کردید کانفیگ رو دنبال گزینه Dns بگردید و هر مقدار بود بزارید روی این مقدار مشکل حل میشه:
9.9.9.9
9.9.9.12
149.112.112.112
9.9.9.9
💡
داخل پنل هم دارید تغییر بدید این واسه همه اپرارتور ها جوابه بهتر از کلودفلر و گوگل هست تو این شرایط.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4549" target="_blank">📅 21:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدل Fable 5 - بودجه 100$</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4548" target="_blank">📅 21:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مدل Fable 5 - بودجه 100$</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4547" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مدل GPT 5.6 Sol - بودجه 100 دلار</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4546" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مدل Fable 5 - بودجه 25$</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4545" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4544">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مدل GPT 5.6 Sol - بودجه 25 دلار</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4544" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4543">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه آزمایش خیلی جالب توی وبلاگ TryAI انجام شده. اومدن یه محیط ایزوله ساختن و به دو تا از قوی‌ترین مدل‌های هوش مصنوعی یعنی Claude Fable 5 و GPT-5.6 Sol، یه آهنگ (Uptown Funk از برونو مارس)، یه متن از لیریکس آهنگ، یه سری ابزار (مثل سرچ وب، دسترسی به APIهای تولید ویدیو و ابزار تدوین ffmpeg) و یه بودجه مشخص دادن.
هدف این بود که مدل‌ها رو به حال خودشون رها کنن تا صفر تا صد یه موزیک ویدیو رو خودشون کارگردانی و تدوین کنن! هر مدل با دو تا بودجه‌ی ۲۵ دلاری و ۱۰۰ دلاری تست شد. نتایج و درس‌هایی که از این آزمایش گرفتن خیلی جالبه:
1- آزادی عمل تو انتخاب ابزار: هر مدل روش متفاوتی رو پیش گرفت. مثلاً کلاد تو هر دو حالت فقط رفت سراغ تبدیل «متن به ویدیو» (Text-to-Video). اما مدل Sol تو بودجه‌ی ۲۵ دلاری، اول عکس ساخت و بعد عکس‌ها رو متحرک کرد (Image-to-Video) و تو بودجه‌ی ۱۰۰ دلاری همزمان از ۳ تا مدل ویدیویی مختلف برای ساختن شات‌هاش استفاده کرد.
2- درک سطحی از شعر: هوش مصنوعی لیریکس رو خیلی لغوی و تحت‌الفظی می‌فهمه! مثلاً وقتی خواننده می‌خونه "Make a dragon wanna retire" (می‌خوام اژدها رو بازنشسته کنم)، هوش مصنوعی دقیقاً یه اژدهای واقعی میاره تو تصویر!
😂
3- مشکل در ریتم و تدوین: با اینکه مدل‌ها با ابزار ffmpeg بیت (Beat) آهنگ رو پیدا کردن و کات‌ها رو روی ضرب آهنگ زدن، اما حرکات داخل ویدیو (مثل رقصیدن یا حرکت دوربین) اصلاً با تمپوی آهنگ هم‌خونی نداشت و یه‌کم تو ذوق می‌زد.
4- کم‌کاری توی بازبینی: یکی از نقاط ضعف بزرگ مدل‌ها این بود که اصلاً خروجی کار خودشون رو نقد و اصلاح نمی‌کردن. یعنی وقتی یه شات رو تولید می‌کردن، همون رو می‌چسبوندن تو ویدیو و دیگه برنمی‌گشتن که افکت بهتری روش بندازن یا اگه بی‌کیفیت بود حذفش کنن. (به قول معروف چشم‌بسته تحویل می‌دادن).
5- بودجه‌ی اضافی کمکی نکرد: دادن ۱۰۰ دلار بودجه واقعاً زیاد بود! هیچ‌کدوم از مدل‌ها نتونستن از تمام این ظرفیت استفاده کنن (نهایتاً حول‌وحوش ۳۶ تا ۴۸ دلار خرج کردن). می‌تونستن با این پول کلی عکس ثابت از کاراکترها بسازن تا مشکل تغییر قیافه‌ها تو طول ویدیو حل بشه، ولی هیچ‌کدوم به این راهکار فکر نکردن.
6- هزینه‌های پنهان: با اینکه بودجه تولید ویدیو محدود بود، اما هزینه‌ی توکن‌های خود LLM برای کلاد به شدت گرون‌تر دراومد (حدود ۱۷ تا ۲۵ دلار فقط پول توکن)، در حالی که این هزینه برای مدل OpenAI زیر ۴ دلار بود. با این حال تیم سازنده به صورت سلیقه‌ای، خروجی ۱۰۰ دلاریِ کلاد رو بیشتر از بقیه پسندیدن.
حرف آخر:
هیچ‌کدوم از موزیک ویدیوهای نهایی شاهکار از آب درنیومدن و هنوز شکافِ بزرگی تو انسجام داستان، ثبات چهره‌ی کاراکترها و خلاقیت تدوین وجود داره. اما اینکه یه هوش مصنوعی خودش بره مدل ویدیویی انتخاب کنه، پرامپت بنویسه، ویدیو بسازه و با ابزارهای خط فرمان ادیتش کنه، یه کم ترسناک ولی باحاله!
لینک مقاله اصلی با ویدیوها:
https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6
سورس کد این پلتفرم (اگه می‌خواید خودتون تست کنید):
https://github.com/hershalb/music-video-arena
هر 4 تا ویدئوش رو آپلود می‌کنم ببینید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4543" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خب گویا تیم Turso دارن روی نسخه جدیدی از PostgreSQL با زبان Rust کار می‌کنن و هدفشون اینه که چیزی شبیه به LLVM برای دیتابیس‌ها بسازن. این یه قدم جذاب برای امن‌تر و ماژولارتر کردن اکوسیستمش محسوب میشه در کل. منتها این بازنویسی همه‌چیز به Rust هم خودش موج/تب جالبیه
🤔
لینک کامل خبر:
https://turso.tech/blog/a-new-modern-version-of-postgres-in-rust</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4542" target="_blank">📅 09:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4541">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مافیا بخوابه، شهروندا بیدار شین همه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4541" target="_blank">📅 09:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سرعت آپلود به شدت ضعیف شده اینجا</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4540" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4539" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4538" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4537" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4532" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4531">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4531" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4523" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4523" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N4UVC-wGnuDXe20k7J2EiSOlDookRTA0rLd2XsFFg1CGr3RLK0gNwRoGG1H6eUs9MsYq8UMrvJ7RgjRpkD9fVviHua71dHVl8JRqotQqJzuu1YesPO6bHvQMB6g7wn3sc7Oly3ftooQPueqRIlYMGoUiUcCzoqZmPu1cR_ZgGxHTwnbcJa9SilQCK_52ckzteY_QO4fs1FBww1uMoWCtH3GXhA3_eLAwJeQrlyv36dMcCvtAA79czweKTk1_PQRp8Aj2LWwQXvLF0_fhK71YFcV9_ogWAI7bMdjkQ2PBNpY6fzeqRDD33P3igFJqAZl2JGEwjFGRX4MlTPfZnOKjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4522" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شاید هم عاقل شدن
چه میدونم والا</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4521" target="_blank">📅 22:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فکر کنم تا اسرائیل حمله نکرده نت رو قطع نمی‌کنن</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4520" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مرز "یادگیری" و "تنبلی" با LLM ها واقعا یه خط موی باریکه</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4519" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4518">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خالق لینوکس: هوش مصنوعی یه ابزاره، هرکی دوست نداره جمع کنه بره!
🐧
یه بحث جنجالی توی لیست پستی توسعه‌دهندگان لینوکس بالا گرفته بود سر اینکه آیا باید از هوش مصنوعی (LLMها) برای بررسی کدها و کمک به Maintainerهای لینوکس استفاده بشه یا نه. بعضی‌ها خیلی سفت‌وسخت مخالف بودن و می‌گفتن کلاً نباید پای AI به هسته لینوکس باز بشه.
اما
لینوس توروالدز
(خالق لینوکس) همونطور که از شخصیت رک و بی‌اعصابش انتظار می‌رفت، وارد بحث شده و یه جواب به شدت قاطع داده.
خلاصه‌ی حرف‌های لینوس ایناست:
1-
لینوکس پروژه ضد هوش مصنوعی نیست:
لینوس صراحتاً گفته: "می‌دونم بعضی‌ها از هوش مصنوعی متنفرن، اما لینوکس قرار نیست یکی از اون پروژه‌های ضد AI باشه. اگه کسی با این قضیه مشکل داره، می‌تونه طبق قانونِ اوپن‌سورس پروژه‌مون رو Fork کنه یا کلاً از اینجا بره!"
2-
کسی که میگه AI به درد نمی‌خوره، اصلاً باهاش کار نکرده:
به گفته‌ی لینوس: "AI مثل بقیه ابزارهایی که داریم، صرفاً یه ابزاره. شاید تا یه سال پیش کاربردش واضح نبود، اما الان دیگه شکی توش نیست که مفیده. هرکسی که به مفید بودنش شک داره، کاملاً مشخصه که تا حالا ازش استفاده نکرده."
3-
به جای غر زدن، درستش کنیم:
لینوس قبول داره که هوش مصنوعی گاهی اوقات به خاطر پیدا کردن باگ‌های خجالت‌آور یا تولید کارهای اضافه، می‌تونه برای مدیران پروژه‌ها دردسرساز باشه. اما می‌گه راه‌حلش این نیست که "سرمون رو بکنیم تو برف و بگیم من چیزی نمی‌شنوم". راه‌حل اینه که یاد بگیریم چطور از این ابزارها برای «کمک» به تیم استفاده کنیم، نه اینکه کلاً حذفشون کنیم.
4-
انسان‌ها هم بی‌نقص نیستن:
لینوس یه تیکه‌ی سنگین هم انداخته: "بله، AI بی‌نقص نیست. ولی محض رضای خدا، هرکسی که به مشکلات AI اشاره می‌کنه، بهتره تو آینه به خودش هم نگاه کنه! چون هوش طبیعیِ انسان‌ها هم همیشه اونقدرها عالی و بی‌نقص نیست."
حرف آخر:
در نهایت لینوس آب پاکی رو ریخته رو دست همه و گفته لینوکس یه پروژه‌ی تکنولوژی‌محوره، نه یه کمپین مذهبی یا اجتماعی. ما اوپن‌سورس کار می‌کنیم چون نتیجه‌ش می‌شه تکنولوژی بهتر، و تصمیماتمون رو هم بر اساس ارزش‌های فنی می‌گیریم، نه از روی «ترس از ابزارهای جدید». به قول معروف: پیشرفت منتظر کسی نمی‌مونه!
لینک ایمیل اصلی لینوس توی لور:
https://lore.kernel.org/linux-media/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4518" target="_blank">📅 18:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4517">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قبلا چندتا مقاله خونده بودم، اما تا با چشم خودم ندیدم قبولش نکردم.
واقعا AI ها، زبان TypeScript رو خیلی خیلی بهتر از مابقی زبان‌ها می‌فهمن</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4517" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4516">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ماجرای اوپن سورس شدن xAI Grok-Build  داستان یه مقدار خنده‌دار (و یه مقدار دارک) هستش. همونطور که می‌دونید Grok-Build همون ایجنت کدنویسی تحت ترمینال شرکت xAI (مال ایلان ماسک) هست که به‌تازگی توی گیت‌هاب اوپن‌سورس شده؛ اما پشت این اوپن‌سورس شدن یه رسوایی بزرگ…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4516" target="_blank">📅 16:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4515">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آیا هوش مصنوعی داره قدرت تفکر رو از ما می‌گیره؟
🏃‍♂
یه مقاله‌ی جالب توی وبلاگ ArtFish منتشر شد، درباره‌ی اینکه چطور داریم کم‌کم «فکر کردن» رو به هوش مصنوعی واگذار می‌کنیم. نویسنده‌ی مقاله خودش توی بخش توسعه‌ی Gemini کار می‌کنه، ولی یه سری دغدغه‌های به‌شدت درست و روانی مطرح کرده که خوندنش خالی از لطف نیست.
خلاصه‌ی بحث و چند تا نکته‌ی جذابی که گفته:
1-
از موتور جستجو تا ماشین فکر:
قبل از چت‌جی‌پی‌تی و جمنای و...، ما برای پیدا کردن جواب می‌رفتیم گوگل می‌کردیم، ولی همون سرچ کردن هم نیاز به «فکر» داشت. باید سوال رو می‌شکستیم، منابع رو می‌خوندیم و خودمون ترکیبشون می‌کردیم تا به جواب برسیم. اما الان هوش مصنوعی تمام این مراحلِ میانی رو حذف کرده و یه جواب شسته‌رفته و آماده می‌ذاره کف دستمون. این کار زمان رو ذخیره می‌کنه، اما «فکر کردن» رو هم حذف می‌کنه
🤔
2-
داستان ترسناک مرد میکروفون‌دار!
نویسنده تعریف می‌کنه که دوستش تو یه رویداد استارتاپی تو سانفرانسیسکو یه نفر رو دیده که یه میکروفون کوچیک به لباسش وصل کرده بوده و کل مکالمات روزمره‌ش رو ضبط می‌کرده. آخر شب هم می‌داده به هوش مصنوعی تا تحلیلش کنه! اون آدم با افتخار می‌گفته: "کلاد از من باهوش‌تره و تفکر انتقادی (Critical Thinking) بهتری داره، پس من کلاً فکر کردنم رو سپردم به اون!"
🎤
3-
مرز بین دستیار و از دست دادن استقلال:
ما همیشه بین «جواب‌های سریع» و «تفکر عمیق» یه معامله می‌کنیم. وقتی برای هر سوال کوچیک و بزرگی (از اینکه "شام چی بخورم؟" تا سوالات فلسفی و تاریخی) سریع گوشی رو درمیاریم و از AI می‌پرسیم، کم‌کم قدرت استدلال، حدس زدن و بحث کردن رو از دست می‌دیم
🗃️
4-
داستان سفر پرتغال:
یه جای قشنگ مقاله می‌گه با خواهرش تو پرتغال بودن و براشون یه سوال تاریخی/فرهنگی پیش میاد. خواهرش سریع می‌گه "بذار از ChatGPT بپرسم". اما نویسنده می‌گه "نه، بیا اول خودمون فکر کنیم." شروع می‌کنن به حدس زدن، تئوری بافتن، مخالفت با هم و استفاده از اطلاعات دبیرستانشون. بعد از کلی بحث، می‌رن از AI می‌پرسن و می‌بینن خیلی از حدس‌هاشون درست بوده. لذتِ اون «مسیر فکری» دقیقاً چیزیه که داریم با هوش مصنوعی از دستش می‌دیم
🗺
5-
اگه من کارای روتین رو بدم به AI، زندگیم بهتر نمی‌شه؟
اینم یه زاویه‌ست. خیلیا می‌گن اگه تسک‌های خسته‌کننده (مثل ترجمه داکیومنت یا خلاصه‌سازی) رو بدیم به AI، وقتمون برای تفکر مهم‌تر و جذاب‌تر آزاد می‌شه. اما مشکل اینجاست که مرز بین «اتوماتیک کردن کار» و «تنبل شدن ذهن» خیلی باریکه. مثل دانش‌آموزایی که حل مسئله‌ی فیزیک رو می‌دن به AI؛ درسته که نمره می‌گیرن، اما در نهایت یاد نمی‌گیرن «چطور» به اون جواب برسن
👍
حرف آخر:
سوال اصلی اینه که ما دقیقاً داریم چیو اتوماتیک می‌کنیم؟ «کارهای انسانی» رو یا «عاملیت (Agency) و تفکر انسانی» رو؟ استفاده از AI عالیه، ولی یادمون نره که بعضی وقتا حدس زدن، اشتباه کردن و با ذهن خودمون به جواب رسیدن، همون چیزیه که ما رو انسان نگه می‌داره
🛡
لینک مقاله‌ی اصلی:
https://www.artfish.ai/p/offloading-thinking-to-ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4515" target="_blank">📅 14:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4514">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_2kaYq_eFh6X3kwoSsznOycAnFcKkAklqfFyw62K_ZpxQkq_ixPSFI9tc3H5jyGS0bZjmBUS0eHv_Jj3feckilz4VXhDW71Qhiice4pK7e4KX7ekfaZiXm7A2fFVylkPub46souN85Wc_Mc1ShPa0ngrLsnSihPZ0oIldDvcKTnBwbkAbh5pEgFDAEiBL0sqRjtLvn_SWoZrVqtoHGbH2icaQ2_FvvfqNs7M48RzxGISwF_KKxdI6acRyIFnS9sbMVKHHtJWnxI5LTAkCEbHCnOFViwYcjNdSN7D6qAMjd95ieijMqTjUvELqJlC9vettfgb_QTzD26XFPkMP2HOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای اوپن سورس شدن xAI Grok-Build
داستان یه مقدار خنده‌دار (و یه مقدار دارک) هستش. همونطور که می‌دونید Grok-Build همون ایجنت کدنویسی تحت ترمینال شرکت xAI (مال ایلان ماسک) هست که به‌تازگی توی گیت‌هاب اوپن‌سورس شده؛ اما پشت این اوپن‌سورس شدن یه رسوایی بزرگ خوابیده بود.
داستان از این قراره:
1- رسوایی سرقت کد (Spyware شدن ابزار): چند وقت پیش، یه سری از محقق‌های امنیتی و دولوپرها نشستن ریکوئست‌های شبکه‌ی Grok-Build رو مانیتور کردن. دیدن این ابزار وقتی روی سیستم کاربر اجرا می‌شه، فقط فایل‌هایی که بهش می‌گی رو نمی‌خونه؛ بلکه داره تو بک‌گراند کل هیستوری گیت، کل فایل‌های پروژه (حتی اونایی که بهش ربطی نداره)، کلیدهای SSH، پسوردها و Credentials رو زیپ می‌کنه و می‌فرسته روی سرورهای xAI!
😂
2- مچ‌گیری و آبروریزی توی توییتر: وقتی این قضیه لو رفت، توییتر منفجر شد. همه شروع کردن به گفتن اینکه xAI داره دیتای خصوصیِ دولوپرها رو واسه Train کردن مدل‌هاش می‌دزده و اسم ابزار رو گذاشتن «جاسوس‌افزار (Spyware)».
3- ماله‌کشیِ سریع xAI: شرکت xAI وقتی دید مچش رو بدجور گرفتن، سریعا یه بیانیه داد و آپلود اتوماتیک دیتا رو قطع کرد. گفتن تمام دیتای قبلی رو پاک می‌کنیم و یه دستور /privacy هم اضافه کردن که کاربر بتونه کنترل کنه چه دیتایی بره به سرورا.
4- تیر آخر (اوپن‌سورس کردن اجباری): برای اینکه اعتماد از دست‌رفته رو برگردونن و بگن «ببینید ما هیچ کدی رو قایم نکردیم و چیزی نمی‌دزدیم»، مجبور شدن کُل پروژه‌ی ۸۰۰ هزار(
😭
😭
😭
) خطی Grok-Build رو (که به زبان Rust نوشته شده) اوپن‌سورس کنن! الان سورس کدش به صورت کامل روی اکانت xai-org تو گیت‌هاب منتشر شده:
https://github.com/xai-org/grok-build
خلاصه:
دلیل خنده‌ی ملت اینه که xAI از قصد نمی‌خواست این ابزار خفن رو اوپن‌سورس کنه، ولی چون دولوپرها مچشون رو سر «دزدی بی‌سروصدای کدها» گرفتن، واسه فرار از رسوایی و اعتمادسازی مجدد، مجبور شدن کل سورسش رو بریزن بیرون!
ولی خب، از هر زاویه‌ای نگاه کنیم، این رسوایی در نهایت به نفع ما دولوپرها تموم شد و الان یه ایجنت کدنویسی لوکال، قدرتمند و اوپن‌سورس داریم که می‌تونیم مستقیما رو سیستم خودمون (بدون فرستادن دیتا به سرورهای اونا) اجراش کنیم.
هرچند فعلا باید خودمون بیلد بگیریم با Rust
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4514" target="_blank">📅 08:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4513">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ماجرا داره این اوپن سورس شدن
که خب به نفع ما مردمه به هر حال
و خنده دار</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4513" target="_blank">📅 07:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انقدر خندیدم که دل درد گرفتم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4512" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4511">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">https://github.com/xai-org/grok-build</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4511" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4510">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برگام
گویا Grok-Build به طور کامل اوپن سورس شده
😂</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4510" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4509">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هک Suno فاش کرد این هوش مصنوعی با دزدیدن میلیون‌ها آهنگ از یوتیوب و دیزر، یاد گرفته موسیقی بسازد.  در یک رسوایی دوگانه، گزارش 404 Media فاش کرد که Suno، سازنده موسیقی با AI، هدف یک «حمله زنجیره تأمین» (نفوذ از طریق تامین‌کنندگان نرم‌افزاری) قرار گرفته است.…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4509" target="_blank">📅 07:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4508">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kW3Zn3gtJRCObtcMP5vvgwc_l2h1Pcwr-1FiE9DxRewMOS_wD1zTxHa_ytYFlBR9OGwg0Vt_ccm8Gubytgf-7XFcs9WZ5tzTEoC1cwIWa-JOpNYIJT3Hcddg_tIl4WrVt2JFGLWHVHCGPQFfJttcazWo_jbsAA9WIx3YbobLKYpckmdz3YgNrt8wD20daceXr-6uW39LIlMtmlPEaEYHhzoSynbrLM6tXx8LUlFU146Qnk9FVrn5KqW31bPqjYDClj5eNKzn5IprMcx1mT6ctNyUthshA77zwyjhS9_fqJUX1Mc19rE9e31lp-v23ceUZ0c-cepQi6htWfAN3AaKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هک Suno فاش کرد این هوش مصنوعی با دزدیدن میلیون‌ها آهنگ از یوتیوب و دیزر، یاد گرفته موسیقی بسازد.
در یک رسوایی دوگانه، گزارش 404 Media فاش کرد که Suno، سازنده موسیقی با AI، هدف یک «حمله زنجیره تأمین» (نفوذ از طریق تامین‌کنندگان نرم‌افزاری) قرار گرفته است. هکر با دسترسی به اعتبارنامه‌های یک کارمند، به کد منبع دست یافت که ثابت می‌کند Suno برای آموزش مدل‌های خود، دهه‌ها محتوای صوتی را از یوتیوب موزیک، دیزر و پادکست‌ها «اسکرپ» (استخراج انبوه و غیرقانونی) کرده است.
شرکت Suno پیش‌تر ادعا می‌کرد بر اساس «دکترین استفاده منصفانه» (قانون اجازه استفاده محدود از اثرات دارای کپی‌رایت برای اهداف تحلیلی یا آموزشی) عمل می‌کند، اما شرکت‌های ضبط موسیقی معتقدند دور زدن پروتکل‌های حفاظتی یوتیوب، نقض صریح DMCA (قانون کپی‌رایت دیجیتال) است. این وضعیت مانند آن است که کسی برای یادگیری نقاشی، موزه‌ها را شبانه تخلیه کند و ادعا کند چون آثار «در معرض دید» بوده‌اند، کپی‌برداری از آن‌ها مجاز است. علاوه بر این، داده‌های حساس کاربران از جمله شماره تلفن و بخشی از اطلاعات کارت‌های بانکی در Stripe لو رفته است؛ حادثه‌ای که Suno در نوامبر 2025 رخ داد اما آن را به عنوان یک «حادثه امنیتی محدود» پنهان کرد و کاربران را مطلع نساخت.
منبع:
https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/
✍️
هوش مصنوعی گراتومیک</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4508" target="_blank">📅 07:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4507">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نسخه‌ی اندروید هم دوستم زحمتشو کشید نوشت:
https://github.com/ZethRise/Aethery
البته هنوز باید کاملترش کنه
😀</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4507" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4506">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o2dV9JIhQ41RFPjOVqj-dIvV4Q1QQ-NUFkzdc4kJ7QLA-ufRGcidlyd2U2qvuuzhFcHXrUhk57eThXAULbPqpcjjU3_BTt-Dk_K6KxD9alc31aPf5dOmIALOd1rmkNGnTlbXxYqlC5qo5PRgxDaEZa8IYjMtM7AMIIjqBbKQbwnOLsUo8MnxlI94g4BL2eu4XIjFjczDZ0cTh0c1ThOXa23zpZlMtQ7VFQJHpd3_72vjTFu5yIT4J8dd9EMiP5EAbBuCOyAu0me7zAr8Htn0gw6DnqXubHw5EbR71yQMxEw_fMc3MsLrOQcAekGh1HXSkYg2YDdRHUs8-yX-At_icA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن Aether-GUI آپدیت شد به ورژن 0.3.0
تغییراتی که توی این ورژن دادم:
الف) آپدیت به هسته‌ی 1.1.1 خود Aether که سه تا قابلیت داره:
1- دیگه وقتی می‌نویسه Connected، یعنی واقعا Connected! تونل الان به‌ صورت سرتاسری اعتبارسنجی می‌شه تا مشکلی که توی اون برنامه متصل نشون داده می‌شد اما هیچ ترافیکی جریان نداشت، برطرف بشه.
2- خودترمیمی MASQUE — در صورت قطع شدن تونل یا شکست توی اعتبارسنجی، Aether به‌طور خودکار مجددا اتصال رو برقرار می‌کنه.
3- اتصال مجدد سریع — آخرین تنظیماتی که باهاش تونستید وصل بشید به حافظه سپرده میشه تا سری بعدی خیلی سریعتر وصل بشید.
ب) مشکل ارور setup prompts برطرف شد کامل
ج) مشکل بافر نامحدودی که باعث افزایش تدریجی و مداوم مصرف پردازنده توی حین مسیر اتصال و توی تمام سیستم‌ها می‌شد، برطرف شد. الان مصرف CPU نزدیک به 0 هست.
د) تمامی کتابخونه‌های غیرضروری و سنگین، حذف شدن
از اینجا دانلود کنید:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4506" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4505">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش ساخت کانفیگ bepass uoosef
1. از یکی از لینک های زیر پلاگین bepass رو دانلود کنید
✅
•
https://github.com/bepass-org/nekobepass/releases
2. پلاگین رو داخل برنامه نکوباکس فعال کنید.
3. وارد لینک زیر بشید و فایل worker رو دانلود کنید
•
https://github.com/bepass-org/bepass-worker
4. به کلودفلر برید و یک ورکر بسازید وفایل رو داخلش اپلود کنید
5. ورکر خودتون رو در فرمت زیر قرار دهید
https://name.workers.dev/dns-query
• /dns-query
6. فایل خامی که باید در اخر ادرس worker خودتونو داخلش قرار بدید  داخل لینک زیر هستش
https://rentry.co/bepass
💡
خلاصه و نکته:اگر حوصله ساخت این کانفیگ رو ندارید میتونید از کانفیگ اماده زیر استفاده کنید و از نسخه ۱.۳.۴ برنامه رو بریزید:
#کانفیگ
های آماده بدون نیاز به ساخت:
👇
https://rentry.co/bepass
(این کانفیگ هیچ ربطی به پنل هایی مثل نهان یا bpb نداره و کاملا متفاوت و نتیجه دیگه ای داره به خاطر وجود پلاگین یوسف د نکوباکس)
#یوسف_قبادی
@xsfilterrnet
👑
@Paradise_Of_Freedom
⚡️</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4505" target="_blank">📅 23:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">همراه اول Masque + Balanced ترکیب خیلی خوبیه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4504" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4503">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">این‌روزا تماما بغضم. از دیدن این وضع زندگی و اینهمه فشاری که به مردمم میاد
از اینکه حتی نمیتونن یه زندگی معمولی داشته باشن
از اینکه نه نونی هست برای خوردن، نه آینده ای برای امیدوار بودن..
هر روز میبینم که قطعی برق چه ضرر‌هایی داره به مردم جنوب میزنه..یکی رو خودش بنزین خالی میکنه، یکی از شدت فشار جلوی دوربین گریه میکنه..یکی گوسفند مرده رو میذاره رو کولش که ببره برای زن و بچه‌ای که دوساله گوشت نخوردن..
چی میتونم بگم، فقط اینکه پا به پاشون من هم غمگینم..</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4503" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">همراه اول Masque + Balanced ترکیب خیلی خوبیه</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4502" target="_blank">📅 19:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4501">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی: https://github.com/CluvexStudio/Aether لینک پروژه GUI من: https://github.com/MatinSenPai/Aether-GUI دستور نصب از ترموکس:  curl -fsSL https://raw.githubusercontent.co…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4501" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خیلیا سر ویدئوها از من می‌پرسید که کدوم روش برای نت ملی جوابه؟ و آیا «اینم زمان نت ملی قطع میشه»؟
جوابش اینجاست که کامل توضیح دادم:
https://t.me/MatinSenPaii/3680
اما خلاصه بخوام بهتون بگم نه این متد ویدئوی آخری نه پنل‌های کلودفلر هیچکدوم وصل نمی‌مونن طبیعتا. اگه اینا وصل می‌موند که دنیا گلستان می‌شد. قطعی اینترنت معنایی نداشت دیگه.
با بسته شدن
cloudflare.com
و آیپی‌هاش، اکثرا از کار میفتن(sni کمی سختتر)</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4500" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4499">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مشکل گیر کردن روی answering setup prompts رو هم برق برگشت سعی می‌کنم برطرف کنم
🎨</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4499" target="_blank">📅 11:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">و رفقا در مورد ویدئوی قبل و اسکنر، من مشغول کار کردن روش هستم که اسکنر رو خیلی خیلی قوی‌تر و پایدار تر بکنم روی اینترنت‌های محدودتر مخصوصا نت همراه، و به زودی ورژن جدید SenPai Scanner همراه با نسخه‌ی اندرویدش قرار داده میشه روی گیتهاب
تا اون موقع با تعداد ورکر پایین(50 یا زیر 50) و با کانفیگ‌های BPB یا Edge یا پنل Nahan تست بگیرید. با خود Cfnew تست نگیرید</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4498" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تمام تلاشم این بود تا قبل از ساعت 12 که برق بره ویدئو رو بذارم
🦆</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4497" target="_blank">📅 11:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4496">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTDFU5PH7QvDyxnrtV-RMg88NsPo5x4W1DhPUSsSisWRXfHoXZKHZvXH40EJyXhZ33R3VyegXS89JxSS0Ybiat2Z5_NP2VmHaJoBtyebzSwWkgL9cS0frmJB6RrhNX89_vVFOyQ35yrF2y7u2mX77ICMwoe64Zs9j_wc7GGUS4Hf_1tBN7UKr_bnFs5rY1v6PneM44nGsTeKqXz5nOiyAe7dXI88aTmYLB6Sgl4P_3PJodcuTFkiTi2D1dl6Uq-oC8aueD8xmL7qtE8A6x4KNNaTsXP8vRSkU7u_5f1_iWCLL55mbU0KodWc0jk46lV7zxbw4iEG_rdJxUKjsvKzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/4496" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نفر اول:
دوست ممد
🥳</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4495" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4494">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش رو ضبط کردم. قرار میدم واستون کمی دیگه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4494" target="_blank">📅 10:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">متشکرم از همه‌ی دوستان بابت فیدبک
روی ایرانسل و مبین نت اختلال بیشتره، مخابرات و آسیاتک و همراه اول جواب بهتری گرفته بودن همه
برای گیم هم Wireguard بزنید. نه warp on warp</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4493" target="_blank">📅 08:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4492" target="_blank">📅 08:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگر سؤالی دارید، توی کانال سازنده‌ی اصلی هسته‌ی پروژه بپرسید:
https://t.me/CluvexStudio</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4491" target="_blank">📅 08:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7bDgaJdmlwQXKrRFZu8vEId3L_k1Kx5ZgYR73snSG8htlhV7UD64or-Mwc81MiEAXeOActUIrmdTjIqZNRIN0VdC3xAYjkqzrNHE0-h610HBLvtpWjIQQVlnAUVapYVACU41l7JgEAUXhtexYJ-tsQbcllOSJX8-oQ-q-yop731P9y-If4Q-76AnpEJWyJ1cFj0dX_FKeYgZvifg9md4H4MXtTMogYtzronVdsf-VYT1qKMIIOovVTkP_6rHKoyxAg-5bA7hqihkZ2tMtNqPRvUEMaA1-ALXVDgTPgvC6ZlvmFwmcrmN37QD3sl-obJ11Wi5IV_bOt7vEvapvrecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که Wireguard آیپی ایران نشون میده(نه آیپی خودتونو)  ولی Warp on Warp آلمانه اصولا بعد از کانکت شدن هم خیلی راحت روی V2rayN بزنید و وصل بشید: socks://Og@127.0.0.1:1819#Aether-GUI</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4490" target="_blank">📅 08:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هنوز کسی سر گیم فیدبک نداده
👀</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4489" target="_blank">📅 08:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XR4AqwIhawV6r93YQCU2Z7eIGI3zA6MheCP_gqns_hk7YOvp1EzWon69BpXWVqb4s89MqqqfpaI_ZJCRHF9SUQGOwA5tmJoeUpvucq_Ke2HAIhyMHmBl0lDLdBX-E9Bg114kvmA5TDPXWh9V2cYM9Ho6q3SukTnpzxfHDjSaLH9Yduyb_GACoTTCyR3yG4z7T6kQDtnfVLM_M56W_36rJVS2SiTINpsQTadFCM4lzFjIVWG5L1YSwrhtJSKGyvkx7foYtqpnn6B3_1pBGs0F0wVWAcilUIukbXNJVozwhUbmvg0XAeKemlXclCt6acK-o_riJVdGqt0yHZPQgmtp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو مثل دوستمون می‌گیرید، پروتکل‌های wireguard و warp on warp رو امتحان کنید و همچنین scan mode رو هرچی از چپ به راست ببرید، سختگیرانه‌تر جستجو می‌کنه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4488" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">موقتا نیاز دارم بچه‌های گیمر سر این متد Aether بهم فیدبک بدن، ببینم تا چه حد پاسخگو بوده براشون هر پروتکل(یا اصلا نبوده)
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4487" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4486" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به همین راحتی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4485" target="_blank">📅 08:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خوبیش نسبت به Worker کلودفلر اینه که محدودیتی در کار نیست و همچنین دردسر اضافی هم نداره.
سازنده هم لطف کرد اسکریپت راحتتر واسه ترموکس نوشت:
https://t.me/CluvexStudio/254</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4484" target="_blank">📅 07:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بفرمایید دانلود کنید. قبلش با سازنده‌ی پروژه مشورت کوتاهی داشتم و اجازه گرفتم که روی یه پروژه‌ی مجزا GUI رو بنویسم دنبال راهی هستم که همچنان اتصال راحتتر بشه. فایل Setup رو دانلود و نصب کنید https://github.com/MatinSenPai/Aether-GUI</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4483" target="_blank">📅 07:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه ‌GUI راحتتر واسش نوشتم روی ویندوز</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4482" target="_blank">📅 07:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4481">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">روی گوشی درست نمایش داده نمیشه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4481" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4480">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خیلی خلاصه بگم:
فیلترینگ به‌طور معمول دو راه داره برای شناسایی:
(الف) دیدن امضای مشخص پروتکل در هندشیک،
(ب) بلاک‌کردن آدرس‌های شناخته‌شده یا کل ترافیک UDP.
حالا  Aether راه (الف) رو با تقلید از HTTPS معمولی + نویز خنثی می‌کنه، و راه (ب) رو با اسکن دائمی آدرس‌ها + قابلیت سوییچ به TCP (h2) دور می‌زنه.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4480" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4479">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R4mTlhFvGzWU1SPcNgRLw3na7y24sA9e_I5HP1wpKeEqEX6mfEzqmNft6ycBwSyewge9EiAnyDTvyX7W_uNV0i9vn0GTi8ICniRAsI6kGwtHk9G3ycNFhtU_44srExm-RqQnd4Pu7EmG6OENxS_vuk0-Mx6gaD7Eu_twzpp-IY37ZKE-0p7lShUf3a8amPvm-wwGplPZ0LouBdol3FlZ6sbR8vfflt6q8Nqhh7TCzLGHJFudMvNI_lL6XfpHO4HNRF2XlCkIIp4fc9XfSoZeXx3xpj0WiRrO6g0n9ZZjfZiwWQWEakCb7AbJeWu95pYMUXfjv491MS_Gn8sSnN8dVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4479" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4478">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4478" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4477">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به زودی آموزشش رو می‌ذارم. هم دسکتاپ هم اندروید</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4477" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4476">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
خلاصه از متن و ساده کردن برای دوستان مبتدی:
شما فیلترشکن oblivion یا وارپ(
1.1.1.1
) قطعا میشناسید.
این فیلترشکن ها تا قبل از دی ماه خونین متصل بود و شما با تنها وارد کردن یه مقداری مثل ip شیر و خورشید متصل میشدید ولی بعد از اون ماجرا ها از کار افتاد و هسته عملا بروز نشده بود تا الان.
حالا یعنی چی یعنی واسه
#اندروید
و
#ios
قراره هسته اپلیکیشن هایی که مربوط به این روش بودن بروز شن و شما بتونید با اپلیکیشن هایی مثل:
Oblivion
(اندروید)
Defyx
(ios,اندروید)
💡
نکته:فیلترشکن defyx رو میتونید بریزید و از یوتوب بدون تبلیغ و سرور های معمولی به صورت نامحدود استفاده کنید.
متصل بشید خلاصه بود از این پروژه وارپ این وارپ.
متین به زودی آموزشش رو میگیره
❗️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4476" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4475">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u2_hZzB7YRy8il6IAwYJHeZaaSjd2n8oEW9uTdhgKoFaq5DCDA_CksmZzGH75XdL3K4UIQPfGUtI0bstEEPKYz2TBKTZeXI7fT7hzUDENyjJ6l56Fe5AzIEcvLEduAkAciceXznwq--rqRUPQu_RAETZQ_NUK4qL305nkeUyQdpWiXBS07s6AES17q3nhexKDfgmNm-9gC-imCEIkdgTEvGWXK4iteKn4VQa0dyjpyzOH2urQXXVJ0vF0wl3nKtR8KbqokI5hHCob66E9tQyUOsPe_Tgf9g2aDwiC9vngfaPWD2P8KVXiw-kc313H9D8iCDqcbxLgTuWxvlvpa1sMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق‌العاده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4475" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الان خودم ران کردم و حقیقتا جالبه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4474" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگر ارور Port already in use روی ترموکس می‌گیرید، باید لوکال پورت V2rayNG رو از ۱۰۸۰۸ تغییر بدید</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4473" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد Aether  با ترکیب Cloudflare  پروتکل MASQUE (روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی  برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4472" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether
یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد
Aether
با ترکیب Cloudflare
پروتکل MASQUE
(روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی
برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود رو اسکن و انتخاب میکنه پس نیازی نیست دستی چیزی تنظیم کنیم یا دنبال سرور از پیش‌ آماده بگردی...
روی شبکه‌هایی که فیلترینگ سنگین و پیچیده دارن هم عملکرد خوبی/عالی داره چون از پروتکل‌ هایی استفاده می‌کنه که خودشون رو کاملاً شبیه ترافیک وب معمولی نشون میدن. :))
پروتکل‌ها:
MASQUE + WireGuard + WARP-in-WARP
برای MASQUE هم به‌ صورت پیش‌فرض از HTTP/3 استفاده میکنه ولی اگه تو شبکه‌ای هستی که HTTP/3 یا QUIC محدود شده
میتونی بری روی HTTP/2 که سازگاری بیشتری با شبکه‌های محدودتر داره.
یه اسکنر داخلی هم داره که خودش endpoint های سالم رو پیدا میکنه و انتخابشون میکنه :))
مناسب هم برای شبکه‌های به‌شدت محدود هم شبکه‌های عادی.
پشتیبانی از:
Linux، macOS، Windows، Android/Termux
دانلود:
https://github.com/CluvexStudio/Aether/releases/tag/v1.0.0
اینترنت آزاد برای همه! :))
بزودی توی Defyx و Oblivion هم اضافه‌اش میکنیم!
داکیومنت فارسی/اینگلیسی هم کامل نوشته شده توی گیت‌هابم حتما بخونید:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4471" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/itgysqipM1L-X18MsCxxU--yuxNRRaecGfcPd1z9ibtidHNLPDcwyb_tpZ9ScRdlCIJRTzJkJxc8FzNEULnseOHhb2sBVYOhw-a_6A1OVlmyEwnFZm8qAVNjrBwPkT7WruEXtqR1u2fXMB5jHpQly_sXRnl7Nxj1UgTtXJEqWfyVTy9foftJEWDAc0WeQCqHeE5GQqnn1H5xeJFSShz7pfc3pdjhCG-Y8JOpiFMIq-VEG3ad_SHkLlAVcrVY5e2_i733IIpnYOVrDS-M3Yu6JLOXGUCFM2ymkAeN9fwHChOydpBu1obGakf92bcke6fCsnEyrGtSMsEWKmf8MBn3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J6fw8P05LIIPjKw4vLLlscxghJQsNDyaGGgarK0TbHtwlr7d1hda3nfQCzmN0XYECsFtjtpbR8StWCqCKvC2UlGVsgDncQj1HsozE0oZhpCBii2rW5geK9z6QAxPonyiO5aDMp7BA3X3TwadlxC9eoYyRpTZ6WCQ7f8qaX9BFViZXu5LbOMkDJoyZM-N7zUL3pAJNxggHe4RQtBawF4uHT0xPD1fQcdCQAmL6eb58f0R1tcPSNfi6SctDFJfxfmfKbR0OrwWQcfvNvcTaiJbhjLooMq4QRpiWPLP5D15vro1hl-yeBuf0tWCPjffiC853c_KQDo2y-IRMvN8Qv1I6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از کلاد خواستم که
https://github.com/Graphify-Labs/graphify
رو نصب کنه روی پروژه‌ام(کارش اینه که کل کدبیس رو تبدیل به یه گراف دانشی عظیم می‌کنه تا Agentها به‌جای باز کردن مداوم فایل‌ها و دنبال کردن importها، ساختار پروژه و ارتباطات بین بخش‌های مختلفش رو مستقیما درک کنن) و کلاد ازم پرسید داداش مطمئنی میخوای اینو نصب کنی؟
زدم Proceed که آره مطمئنم
دوباره رفت یه کم دیگه گشت
گفت ببین این پروژه تازه سه ماه هست اومده، 86 کا استار گرفته روی گیتهاب. خیلی مشکوک میزنه. نصب نکن چون امکان نداره یه پروژه یهویی انقدر پیشرفت کنه
😂
😂</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4469" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4468">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OsjT_3GQJQywvU-NDJOGDttqNPW1XCo5lrY582a8G-SbfefBJBEdm2R1owCYdKJSZ1yRMZ3-CHSi2GWXfgvUy-vz6k5642vsnfGV9mvtN1vKMNrNiDylOaTVqKlzvTPHeKTbwxE4yK_fk0YCrZcj-xaB1vrFsCF2kvvxLRvmtylAU-qiYQjQacrGUBWHSGMH_MbSKS2lptQrsVSr2l6aNmqdrGo_bcRM-qDHfiKTWjm6YEkzpXAeNxbm36NoP118EcCIaxzCVTS3hf8uBPbgF6_NQAj0riXnxgprNbgObH_-2IsTtFDc1QtJZw5PSmL5gwfQs5WCDujMppwqqwVoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا گویا دامنه‌ی
t.me
مجددا در دسترس قرار گرفت بعد از توییت پاول</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4468" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4467">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ببخشید.
خودتون میدونید دیگه بانو
❤️</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4467" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=Qbr3i9M7FpYLU8AXV7hGR2eE29rwQgA2LNBEtuAZ35QxoOQvEXWhAJtVH5tO6YU_gwOyVd5iD4kiSB7u0uX9c7s_uGHsmnjs1Ap0Mp8iTXKJgdTbJ3o0ylPDYLFc9e7moscuwGiNfjEwYWR5szVAnP_UeGjLQt1XVxkkkQYvgNgsTZiqGIDqrTY4u_1u5XwkFDatH2kSur04Xmq6_YDf8OdOY5ZzpjX_46q4G5uhV44A0EL0PHEGTza5bWmqWLCBHrPH5Z85s-l0ttTTunAgB47g7MM5xUHaW-MofV3fQE8-_uHgMR4PPRF4HazNym1Iy3QmvFXdlxztc1HughYbOA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=Qbr3i9M7FpYLU8AXV7hGR2eE29rwQgA2LNBEtuAZ35QxoOQvEXWhAJtVH5tO6YU_gwOyVd5iD4kiSB7u0uX9c7s_uGHsmnjs1Ap0Mp8iTXKJgdTbJ3o0ylPDYLFc9e7moscuwGiNfjEwYWR5szVAnP_UeGjLQt1XVxkkkQYvgNgsTZiqGIDqrTY4u_1u5XwkFDatH2kSur04Xmq6_YDf8OdOY5ZzpjX_46q4G5uhV44A0EL0PHEGTza5bWmqWLCBHrPH5Z85s-l0ttTTunAgB47g7MM5xUHaW-MofV3fQE8-_uHgMR4PPRF4HazNym1Iy3QmvFXdlxztc1HughYbOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خودم نگهش میداشتم
👍</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4466" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.  اگر…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4465" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
