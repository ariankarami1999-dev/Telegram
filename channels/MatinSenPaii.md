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
<img src="https://cdn1.telesco.pe/file/KUhbMzt0qX18aBnOVNBvzo6gIJ7fVOOuF4cwbvxLsU-2ISWMfEmi37vm9MGb2klveB_dWSrLPvT-J5dkYgNVFvvMMcdsW3wAwIH9s4jGbSRfP24axscFQzL7bzeanYTr-PV4qramanNSRZThzkCdzO1pHgS7N6iYb77mIMygT4HRCcXjwnDdqD0kXBuZl3oTk68UOOV7QfXM3TQgEUA6abpGftXXRSQJeazz8Fby4vmlFud6gA1gmhOkOnIh4YNTg7eZX4A4201wyGjegHxND1z7NPjH-m6-v-VeeRwSOeJC7IqleCA-jx-AH30fAxjXRFBiabZsqvXyoqL_kAe0_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 03:32:20</div>
<hr>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iDSSl-kXranZEbARBxpXs01fB61jYmFG_WcxNOmZwcBB0k3J215ix0uMdD776CKqOJOklosFIpoQMY9I59faM_n7MKFu35KPPHoMYe4jvoVM3g07wKc6f1sziLZgjKNJFxpicYIwEfxC6jIUiyvanrqd1l7Sg95HnphHDPEJV9AZI_fVmn3A5NaXDaxt9ar3lTo3pjnAJNBzk0NemRtY7lFojy1rCbS9ddf8NPhN0r8yUbX_r8s7plK25ZvUZ1ZjmxH3PDna27StfpC21mJA95pXnUa8fXoNvIiM2ZhQZZLs0l0-wIf6uqRny9jLhEsv7DPqpWxj7_Eck_kTLTWqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a4GiwGoLKktHY4PL2HCIkK-upcxvR8Kup63Gsf9_SEzY8yFHLMaa2mLc259W3_GUVaTZQS_y6pRNE-3ku31Ink_UTwGjGoe0h6rkZ-KfuZgPgjJMJKMhLBEqeWtJbRoxQ99ie1_BsZmoMDrwdrPBH3I3eUQoygWe6QiDkQ6LX5bQrPC_nmoRKVNzfa6BBTjoB-8I1C9DC21gGSJDKw0uGYzLnXRoctT17pTg9cS52AM5U0KNNg93B-RH0FNz1O2ueqofajm96EA7G3yyI8XD_pYb9oRhYGjgf4mJzr6ltZNFtpZphgN50aDMWr67DbacNHw2JFcFKMh0Fxr49jYe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bckQtYtukglnOiT8RDlEPs1YOG827DO-aoyK1So5S-JR6vVO4Le7XRuZFcPjZgJgjPu8fU9jrO6leHNczB78FgFfgsDhQUW4dI6Y-MKgXpb9iKJV9njwy9WBR-0JLcFyYne2ATW3bjN30ZL-99UP-T3f6LuxKu0NwR6i4s2QzD6gfdzG-hM30ohzt2cpu9GnV-OwffPGEV7QCR9HslEnTdgCG-xOFsIjNx8DOktmov9aItDKJntLhXlZb8NzQsRLQFt2AyC1cF6DNVCLECunGSD6xcCnOI4FF5M30TkyiTcZlQDQCaK926hHpJtkrs_iLPCnMPKBEbnRZdVIZ2DA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aa4QmCMkpYGFemYtw0KdVsjJO_wUyMXQm--x23TPdPWD-nV3o0sgGB3rSmZG5Vy1r4ylkborT9mfTYCa7BQFKEc8pz3EMOXSg0SMYdJnBRkRaLAKlv3NwZnBBaQx2vOnPaZzVJ3wRdHM5G-yek6K7QRNuRepbwx99WVBABfR4F1pM9f7SEOZoSCEl-ERE4yDTYfbuSfKq8Dnwd518XxiVvW87PUOZuqdHtI9gV4LmIISgWrkAVpiZjlDPA6wktE1PY0eQQt0f6-_xVX7JiHnCW0m_ACUPPoGHcPcEwdCs9QKAKBHUT48dm-j-kl_3qFt8rm2dd-ujYKLXOloFwaWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1X4S6qNJl5TpajrdZR6OE76fMoEmUN5kPiMVw4BW2AkHspeG-333DyDUjDSpF4qcg8-iHO7fGdeyuehtSrMyepyW5DhhaAJS9gVEYvncgz76tV5XgZ9PBRhDgW8kXRw9RPBLAGNfZYN8jxeNDEgIgOyRaMxi_Y6WgXh4Dlgw7mDZtQq73f7aieZV8oUbhZKhkUKqbcKxXwazsq7QsiNuovgV8GyUJDXC5B_4fdIimVkfvH11hn-fjdgfF6-sSgU6hCCeDqpjrPET-929exLklWW10Qz8ZvvKw7o5qpYlsL2IG0EmXUHW_Eu9g2xHdbn-PcEN_3Zg-xUkfTjDWztnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r0Acwyt33Dg5ZSGWL7cFmbqBpnjQwWv6OWt820wWK0_aaiu6LDF7NhuBCt8PNHjr4vfmde8xPEKayZxbCp8GITC8sp66QLfy9GsUjFEu5JpdfFwjEhoEogNiNHD0WqjGoUUSMqqOYchYhX14wSDoyDJwJHwCsiz6Mu6OQT5JQ0hjuqFnbpx4JHmHz_jF6SCL4OKlSsXbUVbJ2vWoize1T9CQzrWLwaYbHwSO_sw5RAp3L_lKhRbdglcJzqt7ytvv44wzv51EDjaSfJk6f8dD68Tf0CLKb6NWYCQtLvC1-eypYcuyAZQw8HyTR6O11ZAfnnUssMQB8fku3TB94HzSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V9pRKI7U_H42IUSv_FVwWqfTBO4xPj2KNMTzwIZPZTrUPHWlpZvDhOhEgC4b_4EiZOnn8Tn3DwT3N24OUwPyW71hJ7Q0wDAwfanIGew49x7v0y-_xXvTyYCs6bAe58zYfkXVzdaKnCLWh1lSVLD-EUbdBqeE0SjkjwyTrnT-z_6huC2jYrOUDn94oxaWDv-Oj85Z-cIK6QQ9bjD7fsJSHLM0yL5qVexG7ZG_ejb6Nz9cOc9xXBkYYZecLv52rMsx1-HFH-bBaFVcuATdjlL3IxCdKaFx5h9VMmL4xRpNa6DDI5yaW4wgEqEZ4__VZWcVJfuxn0UjEDww8crtqc69Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c_yEXlPkq4Bhq2739zlBAfnXRObMoSIHuaj8bEqT0mvlh-Qox9dtkU3W_69vflwKwDX_saVhOUgQ_rfug0IPug2TTCR7C0RVvEtM-5hiwyqpYkkRVNTGX25UHm3FSWQ0DF3A-KMHmCXCM1OvXKqODIqQu45CjFvlI5VbMowJootrf7lqbroh_XSk1Y_p8NyMK87_7JKCWGASNOSroYij0Dla9fmUvbKI5MPT-8K12v_6bhzu6zIQtMr24QwxPVI80WQ4lqd7kDbiFhQihZtgicTAeFh1LuqrSEFoqWKGTJjrNMqMJGPGFxR6J73n5efW1HpnCxGpFh-Gk9db0OoTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FsTCds8gJd-knBQCdrzbv_cK_f4KRvCckB1NMuPdi4A2iioXQLdi6EXfZ9kssZZkR9wfuxl6Xx2naa4_HigDbqHBONdm-z8KSbz9lFUw-oNT9ACeliihGx5_9EwZuwgZyHenGm4PU7cZZmwetLYRvl7bVnAtuMuOeRaPXqOzSx8Cmdz5BMf27ZID32zTSsecUTDdaMndmj3hs3-M7f1LYRBIeO_yvbOx_t9i0F60xfP9f6xdV1rPzOfHasqGved1VyfwICUoEeiSBot3onEQBj7h6N3OwREu6bBSiDcuQgsoZj87yjyBB08iL8ItP-t17JdWcov4jeRecNv_hN_6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eBEvPd7r9sTRvZtCtl6y1m8p-cl9yCrLbBN7c0gWE70Z92fI68nNXFMgjoQ0C7HqJ8vEnwLbCflrVKscwj38JSWJxcmdEfZrTX59NjRerPEh9vIOUspBLy8DRRwCpUzK9qJtuvkEc6kcR5pwa17U7v1SKN_Ew1PKRYz9uu8x5uZ3XyhceXWrsIoFaeftpRnb5sFKleY0AbGzyEbnLpohknVpjNQKmKf2BXgVdaV7_Eo5RfeWn18W96cKkAOdhBzsryT5vzeFNhP6aZJlYK9Ivrc_3DL4ZuM3Boto-ej-KjljXYPMphccDsVaTBCt2Y8NKd7MyaPmPuWPFRgobJ-_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیشرفت ai واقعا گاهی اوقات ترسناک به نظر می‌رسه، اما من به شخصه باور دارم که نه جای متخصصینِ واقعی رو قراره بگیره، نه قراره اتفاق بدی برای زندگیمون بیفته(به جز افزایش قیمت رم
🤣
)
در کل، نباید نسبت بهش گارد گرفت. نباید هم نسبت بهش پذیرای 100 درصد بود که "آره ai خداست هرچی بگه درسته"
مخصوصا توی برنامه‌نویسی خیلی خیلی جنگ و دعوا هست و می‌بینم که کسایی که به خودشون میگن وایب کدر و کسایی که به خودشون نمی‌گن وایب کدر، هر روز توی سر و کله‌ی همدیگه می‌زنن. که خب صحبت طولانی‌ایه؛ اما
نه اونی که می‌گه نباید از ai زیاد استفاده بشه اشتباه می‌کنه
نه اونی که می‌گه کلا همه چیز رو باید سپرد دست ai
چون این دوتا دارن راجب دوتا شرایط و چیز کاملا متفاوت صحبت می‌کنن. و این وسط یه سری سؤتفاهم‌های بزرگی پیش اومده و هر دو دسته پیش همدیگه منفور شدن.
به نظرم با گذشت زمان، خودش درست میشه
بازار، خودشو پیش می‌بره و پیدا می‌کنه
و در نهایت، کار هر دو دسته هم مشخص میشه.
الان همگی توی قطار پیشرفت ai هستیم و صدای همدیگه رو نمی‌شنویم:) بهتره صبر کنیم ببینیم کجا می‌ایسته، یا لااقل سرعتش کمی کمتر می‌شه، اون زمان میشه بحث و استدلال کرد دقیق</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y9-sdAR_dTGxi5ynd60ak3Ky7QA1wYtp1j8o2CvQ6zIX_3MgB9Pg2l5fXTTAcQMRfvb_sCbrgTWgIaxJFlaeUVxdoEMbW8-Ud805PWS04H1K4bfEAlZee9qT6IAZ2r9CKNeLM5SjzyJgL-gGS5h60pa9mjIaloaq4zWL3ovgrSihEK-TaM2S8UZ9DK8PCLxLzAKangVz0W4kS-dREJdRpYKLG6NUQJpNitxySZDHwC_XRzcVMIiwR281fePtnebHNRa2ffCpwv06cjOPVbvE0iFcU7Mq2s_cbyLaPSEcAoY-iCbzspOEe3r3GJqpsJhLU1ZoEpGkf5tqR03_vjE1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VRvwXw_k1EvDHr_GFcl5zuZ_CXS1j9xcxnaWTfEek1g0AJJzhdtip4P675vhm5ie7YGRAUsmjYSmFOKWZVpe8a4cLhoRw9cV1t9jjl41TmtkLPW8GOxkmfyTO3dXttcG5PIAgUR_wliH_GJ4_4EGXHS1TptIhBupqrJp1_SzmeUtQcoNObtgYamMKhvGsnd5ecbdIPrVw6Zh-QqsQZIh195JDBl4I8XdkM0QJ480HcIEjHBZqOsysQXG4PYm2jPdUcH_nZu8Dmb7oNUdpPZ6sPyrYfrfFydEmeEjK09mAYInqvMaaIBmIBsnLGEuLCU5gr54sEP19e8C8S-ekdWS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tTd0q5KpTJ8zrU_viNVeVqbOZnze_hYhew9VgJF9FHcStzxj3BvRAVMGe0g2MIOQPm6DhFIqn3gQfu8vLey2u28P_sKLbE6VN9XsYamX-7CN_gkpvqzMPtg8PpLBokh5KT1M5tTsM7_v-ZpKyEvQJPuRvjJUaoIxSTDeuBjN5xpY-Zz4zqLYYwWwBWWUYBODbrs0NSm6x5i2Df13Eulh5jot9XQ6_SLx1u8FsqsnjuZo0oFJFOLhknxSi-kB1kCGPpdS9M4B3MHcwcuH1I7zzc_VSpul3VPlkn0RGu89cx0dYaVaSxVUGHr2wMwqFRNyEbhwYBUbKjXW7eOflt4iXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/foGFeeV7G5RrNshYI1b10REUFA5uDZlENX5yFZLeHj5YlaSx7Rsa0Xlx7nX-Pifm8Pejexm6uEii5gcTYcQ9SukGGAB5jhYCVAjuaHYBkMT2bvsrXZ4FwMOfCxSLeWkDM9ISI6uPpJ7n2EXBNt3oqGbkaaFiI7EoU4IaePo3xU67r7ZV1V56vGnaxas8YNYAxp6XJKmVXESyo7lXyUKgis6mAUYKwDSvpS9gsuqqCo5zCLLYTVChK4g9CwWBsXVRPR_vUo64Ou9BqOk1qxYFxsM6ROUPICH-2u0jxE8kRUjthHcBdEMTC5MEqsSDolkxf14cGSA_x4xEXlFUHpxknA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZW2GTCS9crhNrstde2Nf7PEFOS92hsfhLP9O9zPrU8J7a-Cay_KqBGTQB33YHpbbjLL7vt70t2-VwfZadeXwtvI9dChLpeswQD-PcjR3tZFVd4TqXbCpsjJJAPxFbW3l6BsBxbIoib1SCirKM3IZ_MyQqeQm4nK_NSUyLyOV4QpbdtypqSTZQNif8tA96FUb3hlRsp1LiUtKeJl6WseJ0NPcgLaeWi45YIxrWavz-1bEZGF4nb4zTOk2b5ZSwhIZQG9CmSCbvZxCr8Wzzm0YYHFpIyjI6jfDUbr9Hd9hVt_dYnU195m33d6NX03Wnkixfwm1zPFD9e8mnlSJbHsqYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر توی ردیت، مدل GLM 5.2 رو روی سیستم خودش راه انداخته با ۴ تا RTX 3090 و 192 گیگ رم
😂
وزن Q2 مدل رو هم ران کرده که توضیح میدم چیه. همینطور با اینکه تقریبا از بیس‌ترینش استفاده کرده، گفته که GLM 5.2 داره کار کدنویسی و پلن و هرچی که نیاز دارم رو عالی انجام میده.
تأکید کرده که مدل توی کد زدن، پروسه‌نویسی و حتی کارهای طولانی و autonomous خیلی قوی عمل می‌کنه. و واقعا حس Frontier Model می‌ده.
حالا Q2 یعنی چی؟
حرف Q مخفف Quantization (کوانتایز) هست. یعنی وزن‌های مدل رو از دقت بالا (معمولاً ۱۶ بیت) به دقت خیلی پایین‌تر کاهش دادن تا:
حجم فایل خیلی کوچک‌تر بشه
حافظه (VRAM/RAM) خیلی کمتر مصرف کنه
سریع‌تر اجرا بشه
Q2 یعنی مدل به ۲ بیت کوانتایز شده.
این پایین‌ترین سطح کوانتایز رایج هست (از Q2 تا Q8 و حتی Q1 وجود داره).
همینطور طبق گفته‌ی خودش برقش هم خورشیدیه و هزینه‌ی برق نمیده
🔋
مشخصات سیستمش هم اینه:
۴ تا RTX 3090 (هر کدوم ۲۴ گیگ) که میشه ۹۶ گیگ VRAM
سی‌پی‌یو هم Ryzen 9 9900X
۱۹۲ گیگ رم DDR5 (Overclock شده روی ۵۶۰۰ مگاهرتز)
مادربرد MSI 840B (هرچند بهش گفتن برای این ستاپ ایدئال نیست، ولی خودش جواب داده که فعلا داره جواب می‌ده
😂
)
ایشالا قسمت ما هم بشه
پست اصلی:
https://www.reddit.com/r/ZaiGLM/s/Ew9JHC2XIA
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTa-0rJ9Vf2huHUJh9_R-GqtfzODonIjYYrQaZVeTO0HcVsAAi4C0ba0ZUuxSKSRsPV5pZjnAJa5U4N8Es4QuUq-8w2hNcTr4wAw_GCQAQeIRnUisj-CYRplKB8i7jw9e165yIIdt-C3qVvPo4qFt9IDU89d3lxuRJn-UfA_8eauiNoqpsKKMJWOa8xyIgocsnywjsupr5wkLLYYLrSl1qUEFnnhnkDUxiKnW-ic1RAcn9Crychc3AbiJL6Iusn1sv0TWkUO57QjJTbHKvAiVWxHccUh_8fbpad7Sp-nIRhaOpit8IQe41PK4Ul0HP63ueN3tA2k2ciG6Mq7xAJVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wxnk5hV8HxlEuAbsTF00Gqn3OlmCuRaaTGqC4Ql5PGdRxjcdquMvBlWbKu5PiM-JB3_l5_zk207pXDG7ZqsJaq0gVjqm8G04NHMvfpf1q7m2DwQuI-7C8VpA1_jKNHW881OeRdy-NvDUGNeFz4aGPHyPd_QEyEp6lfJZB3H8RvQzN2P0fII-SD_ZTvLd2AIMnj_JLx2IIxg5e3cHKOscljI2OTdZjPveQ7iyuZt0WVQnl5llOh1aUEvmsVwd06NlH-90WPFy1nwqaSt5R7_KH0DynpM8sn2Su2ZtVV101vECd8YKnXi0W9BTx-pM0gNsrsyq2Ey791fwNZE6YhKEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=q51Jp0ExY4S-DrfMl-iX5eGFZlDuWquETy0Up750hpmPAvJ_LHaVvoP868BwR-8Hl8vVW-C8sMwUUOT8FHa_-Zk4dEe0w9BFAgvrq6jcCdEmGtBK4hKV8820rklCASOd68VcXFHDGbPqE1-cRuXnBrtYEfLzyKwwjXY5LIZzZIbzf8_US7q6dMCZohJyDmfE9Dq7zoHdJdTguuv-peiB_uoMgBsJ_ebQPuCpSogzSn2v9rctAA7ii_hilUB6Atp3r44zlywD6nqd8PjdZAoonFsJcZZeneDfl5o9L0gMqNslJ7d4HyTA3Jlr0_hbsnPH87ag-9kE1ZN7FL9P6hwrqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=q51Jp0ExY4S-DrfMl-iX5eGFZlDuWquETy0Up750hpmPAvJ_LHaVvoP868BwR-8Hl8vVW-C8sMwUUOT8FHa_-Zk4dEe0w9BFAgvrq6jcCdEmGtBK4hKV8820rklCASOd68VcXFHDGbPqE1-cRuXnBrtYEfLzyKwwjXY5LIZzZIbzf8_US7q6dMCZohJyDmfE9Dq7zoHdJdTguuv-peiB_uoMgBsJ_ebQPuCpSogzSn2v9rctAA7ii_hilUB6Atp3r44zlywD6nqd8PjdZAoonFsJcZZeneDfl5o9L0gMqNslJ7d4HyTA3Jlr0_hbsnPH87ag-9kE1ZN7FL9P6hwrqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZSqfSOErsk_Fq2s9NcwrqsX1t6GLM-W6pEk9MS4Yz0DzA9AFxl2OuZ9jCwkQCoS1hSAU8uEwICgK5nmnB6X0IMEFpeMU8hgag81rGVLoWwzswuDUiJ4KoDMMJd7jSgE0UPZIL90WTOG3A0MRFHnoho34lQIKmAst6Xs0Q0B4KieT1JrTf5DM_mhsgu5v27poSIIKMJIjHTcVOB1A1qB4WrXto8EXOpKRw2_auyJdnTJ0PK72_vNgVxsST1vwRVKCWejXroSkYExccdDY1ifsNJ368d9taAmFxORBOSRNNcmgHH3v4FzAyAp8JfAnPRrXH-uU-7tKaeLwQnhPzPm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/geCHsW8xmR6y3t8XR4Hq8QkIB31El7Oj2J61rzFx3Zy0ZF8lFAvIwGm3Bm-_AYqzr3AAjKsbL4njN0kWfElmpyMrwjzHHtoi4seSrZ0DjvZKraKI3YdNN4B3uJqouDUVB35fSEKVO3ROToh09AQkuBkhiBDgjgPlSpcRV329hB9jRGlpdEMm6GSGJ1b2zhnGOSR9qNRv0fhfYOKrD6YHd0r7F_-fMVcDRvn0cXHGmnO4VRET912KfsNyvffLfGhEGQnHXrfUtHFe-xOJy1XO1P4sEJqJH3lu-Q2soenEn2sxtFo65Zr8QTvLeepNekQoNQ79kMv61aTghCWSfM0YHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور
/learn
هست.
به‌جای اینکه بشینید دستی یه
SKILL.md
بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش بقیه‌ش رو انجام بده.
🗃️
وقتی دستور /learn رو می‌زنید، ایجنت با ابزارهای خودش (read_file، search_files، web_extract) منبع رو می‌خونه، یه skill استاندارد می‌سازه و ذخیره می‌کنه — و روی همه‌جا یکسان کار می‌کنه.
چند تا مثال که بهتر متوجه بشید:
۱- /learn the auth flow in ~/projects/backend
کل منطق احراز هویت پروژه‌تون رو یاد می‌گیره؛ دفعه‌ی بعد برای پروژه‌ی بعدی، فقط صداش می‌زنید.
📞
۲- /learn
https://docs.someapi.com
مستندات یه API رو می‌بلعه و تبدیلش می‌کنه به یه مهارتِ آماده. مثلا من خودم سر API تلگرام و اینکه هی آپدیت میده و ai ها رسما نادون میشن سرش، این قضیه خیلی به دردم خورد
💻
۳- /learn my writing style at
https://example.blog.com
استایل نوشتن خودتون رو بهش یاد می‌دید که من روی این می‌خوام یه کم مانور بدم و قشنگ تستش کنم و نتیجه رو بهتون می‌گم:)
📚
🌍
نکته‌های باحالش:
• مهارت‌ها توی ~/.hermes/skills/ ذخیره و persistent می‌شن
• بارگذاری سه‌سطحیه؛ محتوای کامل skill فقط وقتی نیاز باشه لود می‌شه — توکن الکی نمی‌سوزه
• و اما مهم‌ترینش از نظر من: نمی‌خوای کورکورانه بنویسه؟ با write_approval: true توی تنظیماتش، هر skill رو قبل از ذخیره خودت تأیید کن! کنترل کامل=)
🛡
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4069" target="_blank">📅 10:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4068">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7gSIUeZnqZMD9CveCyudcWojq2htZbZMC4PxG0VZJVxTvfI3AITRZ58fOsEAdTuh1ytib9wltL6d2eWvT9Tn02p1Y83z4bB2M0KuhfSPoSMCzjhYR_l5jEguRwA1pvS3HMnkUkqkEarnHp2-X8qmXYn9JvT_QJSnD0El_sKrecdAhhukzag1acJR7OpFiCCgwls9LV3BJGq9NEUlEkGNmGC0hBgk2s2YlQ1zbDK2x_wSNGAZ5d6kon9TEsXRPzQGgp10yJ2gy48Yn1AYNNjUDZfOXEmOQ9ICAEuOg7FlGFUc0gewJjTcV8zxxLP7qGdJZ2p4EMjDNZg9QUOEBxt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ai-news-bot-MatinSenPaii.zip</div>
  <div class="tg-doc-extra">50.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1- باید فایل .bat رو ادیت کنید و مسیر پوشه‌ی خودتون رو از فایل پایتون بهش بدید
2- من با venv و همه چیز گذاشتم که دردسر نصب یا ... نکشید
3- توی config.json هم باید api جمنای و توکن BotFather و آیدی عددی خودتون رو قرار بدید. توی این ویدئو اینها رو یاد دادم که چه شکلی بگیرید:
https://www.youtube.com/watch?v=7qYPK3dGoK4</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4066" target="_blank">📅 02:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4062">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nYA_vze-IqVzCPqH7C-ujRnJFVUlen-MXF7mcBiD4jgcEaQe6w9FYRcTtvquq_GvNYXm_Kztigv4hgRfjigEaVmrx7ApSgQZa0h_ZG0lqxlcouaueqgoDktbxirPTz9TDx5ivuFrjFklhL7QGZc9W90ALhmsMFTLcWooZzFLScFTsf-qY3rpbR__FoBkC2bRx7A1iLUN2TAEyG_PkISyfWfE8s6MM0PMrl9Ul2ZMNgzJpeeNe3weGatGoV8GC9h8Z8uE55TpagKw34JH5jN_PdfKQnCF05Lnb9xDEc1gK3HZfLYcsVaDqvGkscAUJNHQEC-m7ln7ptfwIBJ9CIqSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LgazkWSjo4_B6iv4nJh23NMMvn0QQId2e5SzNgnGP0mTGAfvUpBwBiSrR3urmoX_OeJOWbpBJFujz2Z5kQf49FJv6Cq1y_X97G9V0pENc7yuRJ6K2N2v15B-WsvMJnd6MLrEmEvqHswprlVO6Sa_cX9QxevohhUq50-o2LCkzpeasMpCgKZhrNah64U3dnRpZyKXhN1fHSE5Po5gPeLLCD8KMXZsDJBFk5IT6gZneHAtpKFKcKuXnoCMoQlcviqeuxqF15j7-KR8uJqiGoBIxSi3FxwM4F7Oy3mIWe8Ctsq5aBqbXwudUCR_6WRmV0VbdESvtZooSzptjE9tH4vEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TpsWEa5OkFOWWzo2rzKDVqCWSwJGXEs4I9aO0ffjLmlrJH4YOlGOykhEtqkWrs_uwguLgHq_9VuslnnFBjU1nHLiNTumVxhJXOgNcc4lG5Sj_R7tC-JllCtG987xf6H8aIu9bB8J5W42SdwM0_r--eGOEBYrHOpQrBSGcDdcGfqVkfjbqoHkrpAhO_ZFSiRUCFtKVBTOMXbbYC9OFzbv5mIb429Zdi6QimYVaT3I70JfrGDj6Fap76BcW2JlS3HFYRIzFI0y-GZR27ygwtNtNK-CdukYhBY93cVhzBUSSYF1SgzggevKKB_ha7FjiLy3UBhO-WeMc-0PVOHD4DaHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/owwWgEh33OCIgM2W5KVEU4ci_1voJDGsZmY3Nu3gKORuPZ3O8AMDNpr1dT5wvxsa0t9zYcOE6d5cH8jG3HliRv-d4t-IZUDCz-TYfpsLArkVpnj-ZSTGAN04Ln-DnULAJjbPxUODIU-tc-pmb9BsNK8i1x-UaTQpqdC1E2hu_WCECmBzcrA3NwKI_5HDDUW-DmQKkx9ocolLDpY-0IJG2KMMsPLPcspzrwimOMMuccaCIS9KILeINZORXNv1SRZHhv4WCf1TeZ5HTkcVtrdyW0hNR2VWtY5sIjWGPQtPwcf8NU25-cmxC_4f7aGjsmmReXWtP4Vd56AVrbQvfmHteA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!
توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini 3.5 flash lite ترجمه‌ی روون می‌کنه به فارسی، و توی ربات تلگرامم می‌فرسته پیوی من. که خب کار ساده‌ایه و بهتون ایده میدم چه شکلی می‌تونید پیچیده‌ترش هم بکنید!
الان، شروع می‌کنم فرآیندی که این اسکریپت خیلی ساده رو ساختم، بهتون توضیح می‌دم.
1- اولین کار، گرفتن API ها بود. از Nara Router تونستم 7 میلیون توکن رایگان روزانه بگیرم که اینجا گفتم چه شکلی:
https://t.me/MatinSenPaii/4061
و همینطور از
https://aistudio.google.com
هم یه api رایگان جمنای گرفتم. که مدلهای دیگه‌اش به درد نمیخورن از لحاظ لیمیت، ولی مدل Gemini 3.1 flash lite واقعا توی لیمیت‌ها خداست. 500 تا ریکوئست روزانه و 250 کا توکن که اصلا پر نمیشه. برای ترجمه عالیه. اما برای خود Hermes مناسب نیستش چون که TPM بالایی مصرف می‌کنه و Exceed میشه.
2- توی Hermes، از قسمت مدل‌ها،  Nara رو اضافه کردم. خودش اتوماتیک تشخیص داد و گفت کدوم مدلش رو می‌خوای؟ گفتم mimo pro 2.5(که در حال حاضر رایگانه توی Nara اما خب واقعا توکن مصرفیش هم بد نبود برای تسک من).
3- وارد چت Hermes شدم، و چیزی که می‌خواستم رو بهش گفتم. گفتم که می‌خوام یه ربات تلگرام بنویسی که هر بار رانش می‌کنم، آخرین اخبار ai رو با api جمنای بگیره، و حتما از مدل gemini-3.1-flash-lite استفاده کنه و عینا همین.(اگر نگید دقیقا یهو میره مدل 2.0 رو میذاره بدبخت میشید) و برام بفرسته.
5- سری اول ربات رو ساخت، و بعدش بهش گفتم یه سری قابلیت اضافه کنه. مثلا زمانش رو بگه که چقدر وقت پیش بوده یا فرمت بندی رو درست کنه. همینطور گفتم که برام یه اسکریپت ویندوزی بنویسه که هر بار کلیک کردم روش، این رو ران کنه( این شکلی راحتترم خودم)
6- همونطور که توی تصویر می‌بینید، خیلی تمیز برداشت خبر GPT 5.6 که واقعا هم سه ساعت پیش اومده بود رو پوشش داد، همینطور خبر های دیگه که یکی از نیازهای روزمره‌ی من رو برطرف کرد تا حدی. که یه دید کلی نسبت به اخبار ai روز داشته باشم. سورس کدش رو هم براتون پست می‌کنم که اگر دوست داشتید، تست کنید. هرچند چیز خاصی نیست؛ خودتون می‌تونید بهترش رو بنویسید
7- چطوری می‌تونید بیشتر درگیرش بشید؟
بیاید با همین "بات جمع‌آوری اخبار مربوط به ai" مثال بزنم.
شما می‌تونید این رو روی یه سرور لینوکسی ران کنید که 24/7 ران باشه و هر خبر جدیدی اومد، درجا بفرسته واستون. یا حتی ببریدش روی worker کلودفلر. و هر یه ساعت یه بار چک کنه، اگر خبر جدیدی اومده باشه واستون بفرسته
همینطور می‌تونید یه سیستم پست‌ساز نیمه خودکار بسازید برای تلگرام و بدید که پست بسازه برای چنلتون(و این وسط توسط خودتون یا یه agent هوش مصنوعی دیگه review بشه!)
خلاصه که راه برای درگیر شدن باهاش زیاده. کمی تایم بذارید، و کار با این ابزارهای جدید رو یاد بگیرید. من هم خودم اول یادگیری هستم طبیعتا:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f6oCCHIV2e8H08qIkIzJzrMwECnBJNdZVm0dh9HuxZc4q93u7FEuCMreYUo4_9h7eoeb9tlRzxivzxozThhcZ0v6F91WnQFSTFMdZXcJRxCkZiIoDYvPujL9ZZgv-01FTMptQ31RU5U2a_jbV8HdBAGBnEU4RCbaTWRCzjUx1hmP0sYM-CzLNGBCkvq0Ks6N8uH6SHMjD9SSVjcrNmnqxRxbzEIaDqq4CGlWLb22QWKNtT7bzrYO2iQ_8G9QF_siRUIg2BI6Jq7P1-UJcHYwaVLDtYzIww1Pl3QXtCTCjx_NWqe13cUXECdW0-W33QlQXSVfu3jo9s_9WWEVbKqaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4059">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به قول یکی از بچه‌ها یه چرت می‌زنیم بیدار میشیم می‌بینیم ده تا هوش مصنوعی api رایگان دادن
😂
چون خیلی حجم مطالب زیاد شد این دو روز
به زودی دسته‌بندی می‌کنم و می‌ذارم
همینطور بهترین‌هاش رو(که زود گذر نیستن) ویدئو می‌کنم و یاد میدم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4059" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=WVjS8LRp1x8uJSF-l44LpbSUSVa-Jb1iO_WAVnqOQU_MgQdLp-Cm3iNw_4F45sael0zT4FenedfxHwTi-2bPSVYW2QhWik76m4CSTvgQDzhviH6_hWt2gfsCAIBndiC88dBkE8cdci_5n45GSc_aYEg7yj1BRfNd7839SssoRneup8cL8XJIBTC_ohtMhGPKxUAfMdaO5umaGcJJC3U0I923x5egnzQQ_hDMt9JuWH1uTReAPb-iOozpA2IWitl222cmDB5UnEUZDc-2YEImoihaFaM7E6JKwPVw7eWLJ2zSOGiNJ9ZaRnDTpNEgpWuME2WPbniSjtoLYaa0Y7ocZRDeMSx58Wq7Sov3S4gv5spZF37uWfsoJxcq7fRY5hm39LkCKkz5yZY-LB3FIE0d_217eNh0ylKh1tVzJJbKdKCwtHcp1H8dyIa-C93dcJP6Owbrozj4REN8OdBZEj_WkafJEc_eh63bVYtWoscWoZqCHXuIp2bvZpOMsMgbS4BncTdh_Yh2rbNn8AeWKRv0_voeN5HzGIWzgcaxRrFodF7VY6S0Nsg_ErctSmhIAAdQY1QCQSVdxJn0IUvgiv6tNv3ZcNhKrb119Z1Cx96_-AcO1IOcoRzfnUU652EmDVCkgrQweoTSElNo8S2HhwJEmQMpbWFsz7R7UsMgsMgklpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=WVjS8LRp1x8uJSF-l44LpbSUSVa-Jb1iO_WAVnqOQU_MgQdLp-Cm3iNw_4F45sael0zT4FenedfxHwTi-2bPSVYW2QhWik76m4CSTvgQDzhviH6_hWt2gfsCAIBndiC88dBkE8cdci_5n45GSc_aYEg7yj1BRfNd7839SssoRneup8cL8XJIBTC_ohtMhGPKxUAfMdaO5umaGcJJC3U0I923x5egnzQQ_hDMt9JuWH1uTReAPb-iOozpA2IWitl222cmDB5UnEUZDc-2YEImoihaFaM7E6JKwPVw7eWLJ2zSOGiNJ9ZaRnDTpNEgpWuME2WPbniSjtoLYaa0Y7ocZRDeMSx58Wq7Sov3S4gv5spZF37uWfsoJxcq7fRY5hm39LkCKkz5yZY-LB3FIE0d_217eNh0ylKh1tVzJJbKdKCwtHcp1H8dyIa-C93dcJP6Owbrozj4REN8OdBZEj_WkafJEc_eh63bVYtWoscWoZqCHXuIp2bvZpOMsMgbS4BncTdh_Yh2rbNn8AeWKRv0_voeN5HzGIWzgcaxRrFodF7VY6S0Nsg_ErctSmhIAAdQY1QCQSVdxJn0IUvgiv6tNv3ZcNhKrb119Z1Cx96_-AcO1IOcoRzfnUU652EmDVCkgrQweoTSElNo8S2HhwJEmQMpbWFsz7R7UsMgsMgklpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8XpOYv1c3f1skXm-gypbdjkW6RDNH02zpIoieZ3D2eHIQhjOeESR7P0zC9gPRfgudB0iNTPYBQE-rC0offzKFSZwY-0B_l8Uvb4U0IvVFJ1g91cPy_uKqWc10PVkatCWLGfcOCzz-XyGmbY4kIlZ-DBVrylp72A2KV8RXPe1VOdCfeMpOieIeIoXA9kTrEAkxWq1tuL7POtTMt_fKEMMLt8ARQaABnXo8SjD7wXuqHtZnNe9GcPP18IZd7r0ZDKqIOpb2LnzqXtoICyy7e86k5PF2Ntr9uXSUF2fROrR_neC-XYeyBBDkhD7z_OnyxCz-jGCMaowWw7-Ei2cxRLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gx63DAjTALFjzSl3o4fSzYhrEXvMFKlbCz5H5N-7BQYuHq9I81NueYFWXi_TvFxQcaWxpT2Z_mk2ZPF0aqlroXpigL7wFlCDSvgZT20xf89orTKJdUdWZ5lIvdN-5thgZjC0--U9hLBTByl7IttC2sgw60CDSox6j0occUMO_4OpxB74dv9WPpXckOnlK77ponCftI6t4PYZgOIQGUx1ZRJHCbn3boaWJJCs-BTcJ843nNPHOq8YJXB8GxPVL2zvjBfG01ljWV9g6mA8RRy_Hcae_eU25GjA5Lt-85LQZKsjFivA4e6l8_PKGJNTESVBoeGOlGTVteSRp8lBm0GeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dastamo Begir</div>
  <div class="tg-doc-extra">MEZZO</div>
</div>
<a href="https://t.me/MatinSenPaii/4047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4047" target="_blank">📅 14:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این نت دیتاسنترا کی می‌خواد مثل آدم وصل بشه من نمی‌دونم.
فکر کنم جدی جدی کابلا رو بریدن الان نمی‌دونن کدومش مال کدومه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4046" target="_blank">📅 13:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">موشک ملی‌شکن
🔥
@HexConfigs.npvt</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4045" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8zBhAeVfYVlXmWmMUwu3x-oh0Cycf4hOiFNzv_0iL9llvvVUpd6QrSM5JjltPSQusDSOHhaYeCFVprNZgjeyLonOfv8PMtMGpGV8vmtD_JriI6nHO4uVuubU2kRRb2LjRBrb8q4hvo_u1ZJ-xUYbZURPUMq-tTNibEcNAqBeUwSXsO-rRMyjKonLjDeDQb5qF_QKbUHPPMLEWqoft8z25l51BvnlLN3aqg5Jn0OgUz6lo0avqbHuZbmNqEPSPyEAhH6W9Suty96VvCcf82AzNWCy_hpBKcXq9W8mqu700F6jNtHchOCiytpr9ME7LhyTiCf3CX_9dKBY42NqaKazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4044" target="_blank">📅 13:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB
۱۰۰ دلار میده
باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4043" target="_blank">📅 13:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چندتا نکته:
1- کاربرا توی ردیت گزارش دادن که برای استفاده از مدلهای anthropic زیاد به باگ می‌خورن و علت می‌تونه استفاده سایت از apiهای دزدی باشه. بهترین نتیجه رو با GLM میده
2- اگر از GLM استفاده می‌کنید هم، یا به ایجنت فول اکسس ندید(که .env) و اینهاتون رو نخونه، یا توی پروژه‌های حساس ازش استفاده نکنید</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4042" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2Pjdm5oTpLrReOw2s69MYh-zC4B9CVHXYHoREls3H5TdK7HKbfmYCK5uTC2rZCPOsERAhEAQTPITOgofYdL-z8GbK9Zz29lP27iSReqZ1azNgRU03ql84hnEEgVee5jnkgcLuVCuyLAuKcyB_a-6VzEztExA3j3TjkW_VBNyDRxPgcceF8fLi1sb-EjlNbZ8X8Uk3vWq71t5INCgJNTSldNHG3VoO9s-_NP8jiafxbPtK2ZRg63q34nbsG68ZY-YiZPWDTGy7jxXWRA3tBpDnmwr9uN7pO3HQURFKt-2FBwDG6HqnkaR_G79gYYeDcJ36NOvEuaI_Kves47t9PDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایپی 188.114.97.6 دیگه سفید مطلق نیست و با ایپی های دیگه کلودفلر فرقی نداره. /// البته رو بیشتر نت ها به غیر ایرانسل کانکشن خاکستری نداریم و به راحتی میشه به کانفیگ های پشت کلودفلر وصل شد. برای ایرانسل (و بعضی نتهای دیگر در برخی مناطق) هم با استفاده از فرگمنت…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4041" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G0s4_m-6al_HuKICKIR7Rq-KHGWnJbZ-G-s81rEzIRnWSZL6q_qGI4aujYKW3pCM3Uu3GNc2POzsovpxWbJ9TlLt0NwH1S5cGT6zrVxgEnogEQaMJRm6DdRsDr4LqtrbdTo7Layzj3_Reqoyfz362W-PfriFB03u26OFMk631j4hrJMD5CXvYP7_JaB4s-66aT0BfJlAQ8c4E0SAluGQpL6w290bZvV_3AaYcK2mEkbrFuPgCPTOQLD3bwlrXBZZV6P1FDDn2MOPEh1oi5NpOuSR1vu073mreZRZexj4mGvwvuBP9Hr_mIBP4hjSi2o-pcB37dshM-XnQRRkqhTbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4040" target="_blank">📅 07:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWoncUIMmHMwU8z4Hnm2Wk35ujNqkQYi7OQ2ebUov3hSE8qwALYGLID2XAXLuXYgxha1G4fEcChcHSV4MUpUNsGIz167riaFRsXq7TEVCe6qIyohqYqFIwkA0ETCkOsmSqmujUsbS6M-0JWi7ulfv8ZJpXynHCI89_xyDz2xb5Iyk6DEzc-O1lNik4CWyQ3Y4acvqQTIu7rE9Qfj6NY-APsxGKWGGW-jrYP11l1QH68BKJS2z0nAo2HfmAyVFyUOUeFADfbAjR8Kq2XOOWblyLk7ROVHDoDSbKnzIXUiT3tPCOe5l4EOV_qLPnCYQ9BBFXjqEuNscU3mpg7PNQc5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.  عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4039" target="_blank">📅 01:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4037">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GLcSqat8nppuGIGuYyZqKJGogWeCEJF5LvV2ae4MvPUDtFfi-UWnWQLzRYKA0HRJZ7N0_7SdEsAMRobRyfeSvFctWVrBSH63S2f-94F7PMN9MjhVsUhJQZhYPpuw_Sk5fbaZxuNFW7xuLE-1POZCkQAeLU27jjsHQzsCO7c-Zg5M7DWzrcs1OKkXpluFoC7N_Rgdm59WO_aUHakQzrfU-IeNXhSlydn0gAr27jkCaKQaKC1Ow_YXJxh5lmt5vmCZHDH0x7LijiypMH8ji5ADzNSVv3UjsY3qNJ2C1ZYUDcan_Cikdi76ARdo3A5d8kvZ4X6EcBrrhfDjeTNMtj50yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.
عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:
https://t.me/MatinSenPaii/4023
)
این ربات تلگرامی که One Shot کرد، کلی چیز داشت که اصلا من بهش نگفته بودم اما چون صرفا فکر کرده بود که "منطقا" باید وجود داشته باشن، خودش نوشت. که خب هم خوبه هم بد.
و واقعا نتیجه 20 برابر خفن‌تر از باتی بود که با MiMo(که خب بنده خدا مدل رایگان بود) نوشتم توی ویدئو:
1- بعد از اینکه ویدئو رو میفرسته، خودش پاک می‌کنه( از روی دیسک )
2- به لیمیت Bot-API تلگرام اهمیت داد و محدودیت حجم 50 مگابایتی دیفالت(قابل تغییر در صورت ساخت local-tg-api شخصی) گذاشت.
3- کدها به شدت تمیز و مرتب و با structure درست نوشته شدن
4- خودش چندین بار همه‌ی فابلیت‌ها رو تست کرد و تا مطمئن نشد که هیچ مشکلی وجود نداره، تسک رو تموم نکرد.
5- بزرگترین تفاوتش با MiMo این بود که میمو صرفا تف کاری کرد که یه چیزی باشه که جواب بده. یعنی اصلا فکر نکرده بود که این قراره یوزر بیاد روش، روی سرور ران بشه، قابلیت سرچ کاربرا باید چطوری باشه، لیمیت داشته باشه حجم، و... . اما GLM کاملا فکر اینجاها رو کرده بود بدون اینکه بپرسه حتی
6- مهمتر از همه، یک بار فقط بهش گفتم و همه رو نوشت. نه گیر کرد، نه اشتباهی کرده بود.
حدودا 5 دلار مصرف کرد و حدود 140 کا توکن، که به نظرم ضریب دار حساب کرده خود AgentRouter برای GLM چون اونقدرا زیاد نبود کار، نهایتا 1 دلار باید مصرف میکرد برای همچین تسکی.</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4037" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4036">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">می‌خوام همین رباتی که توی ویدئو نوشتم رو، با GLM-5.2 و همین api رایگان agentrouter که گرفتم بنویسم ببینم چند دلار مصرف می‌کنه. با همون پرامپت و با Cline اکستنشن VsCode</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4036" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4034" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4033">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4033" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4030">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TbkQDJHX3UKuYgbPuwXuZT-9duOZkRIfpQsDMtbydzMmq7LnJIk78uUHZLhlN9aELnCEDnG1QRAmA0lZElNXPAkmQC0QyTkZs0UwFfk-O8goHsdmTCtWXLArp6qWw6jMvhhpTbj9GBc1QphOGsEh8U1sxz1VWASIDuGD5fcQCZvloBzeSm1qE57ewBFstmtnK53pCwUm9WKJcZeBllwB_WivLIrl_tkTdWfhueGsez9Ku4P0HdkTAS-_jbH1wXegIFtd6AyamzYEg_ieFIR0pvngOtoD4V58fD0zif46GDaE1jWiFHe1MgWWdrVfxtAkRxTM_Bp8VBLxywIRPTLL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر براتون سؤاله که چرا OpenCode انقدر شبیه به MiMo هست، باید بگم که میمو خودش Fork اوپن کد هست و بر اساس اون ساخته شده
🧮</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4030" target="_blank">📅 23:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4029">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">واقعا یه سری آیپی‌های تمیز کلودفلر، سرعت آپلودشون خیلی خیلی بیشتره. الان که ویدئو رو آپلود کردم متوجه شدم قشنگ.
خوشحالم از پیشنهاد دوستان که تست سرعت آپلود به اسکنر اضافه شد توی ورژن آخر</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4029" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4028">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شدیدا حس میکنم یه چیزی اشکال داره راجبش ولی نمیتونم ثابت کنم
😂
۱۵۰ دلار آخه؟</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4028" target="_blank">📅 22:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4023">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qi4EnNZT4BRG0cOvUH_G3eVby38PBmsnmgL5qh7bxCOqyV7FUDtpWLLePUnjgig1yJZz_FvsakT_J4DciegzbvQiyL2oUHSf8YUDqKcnttkmYOuAnadjIF3TilZ_lM_IV0j_qETggCoxxwngaFQdJQ_M0KxMNOLsJbNb5Z1kkpginf-o4VuwGrH886n5zzw4TenncbhA98iuynB0LF59A2vNkq3sNtkac-INq1Uei_KqEImkNsZDInpE-RpwE8GJLtfdABZB7R704cQMWvleRPn8tklTdYU4D9wnfNGyUcaohyKGQnm_E-2eXMIlMbPNy5lmpQE8uA3XI1vNBsBiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UvuMgR8hhRseRfXMsfeFrPYEzqcX6RSXg9zN_tL4Xwr6ejL7gulET0_9wOxS0LauxkshvE1FVktz9wUJb6EdnC9mcyhsn1alhfcwB6IfXO4ODSdd3hH8YQSABqb7YFAR9gctafCajQL5ORz0-xuGz2BKzLq4jIMOWpmjEgYmWaA0lKvJf-7Sv9P9MJnEH_LmgtkoKOZxTHezfGKeanQVdkfihdjE7-cUgc18uTOMrGQviVNp2OFG-uycv84Tz1zUz7DA8Gubt5I8QpJcOAYSvzD1beyG7VXjIdQJ9Vu4uOgXtlZ9_bj9AyRbhh9LIqqVDH2VsCTR0nCpc01gOmgnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MnkPUvJg3imKgEv_cPN5M-cul1jMZFPgOpgPdAtiIGvPahClAKwYcNqT977mRdJEt7cRuRIrWgs3xGIsBiwyY6F3_lSfAhMG_zaAC3ytNMvXnoL2jdJ-no6ObdMe5ve6FQibB480CyTxnhxhYxtIVjztDfk9eE-fBQz_YCHlvOC2bhuEOz4ztK4F0RiSqIRDFeYhAxqjwSBjQ7XTFY4CcOr2UJq08lWZABZc7ZHDFKRIMDGP7vglgWmOrtkWQ6bK5tYpE95C_AZliZYZRdfCsq6AKgLQLOc-EWlAzoDA9Ca6gzctbPljs4QejRGfnmfC_VSCMiG0uHY76rlcZSh7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ExDkOIySP0TYQwwgIjQa3t-LCaeHyC_Sibfl2LSGzVhgFlmv1HWnc-2kZA53uNhrpC1j90cw047dAzTF6POecXogJCbsOqMNlupYfva7M4osHWDUdAYUIo4mMeK9gzScc3I-uwjXsFBVkXFRXvq_ZFqy2Hey9nGJAQubkJtrqYzoX_BRaRdSrKWSysXOb3hDq6UGVi1w4hTPeuUPRt_RWdsTakshw2nQHVOnPbHFJBp1tTT-iosyqXekvJOUm9JhQ8w_6qKGVWPoiHVpgVtsMX7BWlD_pc2aT4yeS3FiLi-SRU0aPI1fp_Bi_hrNvN2w4FLjxYqah7PD4flamX97kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pod50s7_R8vXIVSmG6ZopWX8bEW1Pp0tEMcpMr6Vua8mkj57d2oKsL5ty_4LHRWB3RV99pEoKTHwUD6ZQN4EJcIFgU9BD6AD9g9GI8wIJmXXYd8BKca0RQgR0DSSmd4ZjqYXjhIRlZGsjTsHblrfytoCP6bRtWLPMiNK1WUpLmVfqx_XON9mg3YZxokDCqwiS3ukdiSgJ4slLFMYXb11zTW5HdmXcbFkoRA5cIZ9el2Vx6EqO-9d9QhpXXZ2hvkUyBdvMZYX-afEeJ_06S2mJj_IWAi9MgXsoxUNtKU8WSFalFGCSR4lxykfH2xr0XwPyGm0lntxkxZ8HhjmESA2Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این وبسایت، می‌تونید 150 دلار کردیت api برای مدل‌های
Claude Opus 4.8
Gpt 5.5
و غول چینی GLM 2.5
رو میده.
مهم: به این نکات توجه داشته باشید
https://t.me/MatinSenPaii/4042
منم الان 150 دلار رو گرفتم. با گیتهاب ثبت نام کردم ثبت نام عادی disable شده بود توسط ادمین.
برای موجودی بخش wallet رو چک نکنید. از منوی همبرگری سمت چپ، account settings رو بزنید، درست میشه طبق تصویر.
با تشکر از
شهریار
عزیز
فردا استفاده می‌کنم ببینم چطوره:) ایشالا که نبنده اکانت رو
من خودم با لینک رفرال ثبت نام کردم، فکر کنم ۱۰۰ دلار بیشتر بهتون میده(به جای ۵۰ دلار، ۱۵۰؟)؟ نمیدونم. این لینک رفرال منه اگه خواستید بزنید:
https://agentrouter.org/register?aff=PvaZ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4023" target="_blank">📅 22:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4022">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پارت 2:
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
پارت 1:
https://t.me/MatinSenPaii/4021
#MiMo</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4022" target="_blank">📅 21:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4021">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q3HLrHEmyqDx9-jIHnBo3OHaJ-B_EN-Y62wN8thS0oGJFsjQ80cpd1OpthpYCMxfyxYu32ecvBvMrGFZ1WTQE_WG_s8Y0xvxawUfUkcaf9SRduF6buiZrBNq8wQ_TEEFJy4Ez0QW1e5Z1nibrYzb2awm8pDktdMAw12cTKJujrQP-a916SG_hOUJ_cvOHCVY_yLC1MsUi65Cocl_CmqSh0ma-uGtCeprizfCfasfWjsoQJaL5dDxQf4fBws6s8S-HX3X7wIrkoT1JX0RcDFmO2E9iGZMVIuNvWg73fr0LZC4xE5iwH9SvQ3Lu1DcDsDRoAkVTWqyCixsk6xlArllUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:
1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید:
https://grok.com
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای مختلف رو نصب کنیم روی سیستم عاملمون
2- ابزار MiMo Code رو نصب می‌کنیم
3- کار باهاش رو یاد میگیریم و مود‌های مختلفش رو بررسی می‌کنیم
4- یه ربات تلگرام تیک‌تاک دانلودر وایب کد(5 دقیقه) و وایب دی‌باگ(50 دقیقه
😂
) می‌کنیم
🤎
اسپانسر ویدئو:
شمع‌های دست‌ساز لیرا:
https://t.me/liracandles
❤️
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
✉️
پارت 2(بخش پروژه‌ای که می‌سازیم):
https://t.me/MatinSenPaii/4022
💰
دونیت</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4021" target="_blank">📅 21:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4020">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">توی ویدئو از عمد وایب کد کردم صفر تا صد. و قشنگ می‌بینید که Vibe Debugging ده برابر Vibe Coding زمان می‌بره
😂
😂</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4020" target="_blank">📅 20:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4019">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ویدئوی امروز راجب Mimo code شیائومیه. و با پلن رایگانش یه بات تیک‌تاک دانلودر تلگرامی می‌نویسیم با یه پنل مدیریت کوچولو، که خب چون یوتوب به شدت حساسه روی ربات‌های دانلودر، مجبورم اون بخشش که ربات رو می‌نویسم و باهاش از تیک‌تاک دانلود می‌کنم رو اینجا جداگونه آپلود کنم</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4019" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4018">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4018" target="_blank">📅 16:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4017">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MbOVHWiSsM8K7jwvMlhdUzswhheGf9IhAu4qM83OKqYfwi34oWGVlH_WkKZ96pcGf82UaGK6dgx5QfvTEqTYkOmzlmEoFpbcuNEnx167QI9yyP0B8V1t4w-b0IgqvZzhQwy59vnC1HnESXmv80jh6Y_sc-X8BEfFV0q_3WcV8q-SmbYe4ZG_Jn6jClks2BiDo8ka2KSXkKTXnMcEguP-dV_8ee7L723AHROLyiiK77WMUhKxv1DDKUvx0WNNkRVXg4uSB_aUtQQTaH1T28oiOpkpUWPm_c95O2Z4zOoWTmtfv57jBdjHDbXEcSIDkBHjcERVsTZ_0t-p3KxbiQDRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تازه فهمیدم میشه با توییتر پریمیوم از grok پریمیوم استفاده کرد. بازم دست اون عزیزی که به من پریمیوم هدیه داد درد نکنه
گروک بیلد رو دیدم، جالب بود
خوبیش اینه که وقتی رقابت زیاد میشه، 1- یا قیمت اشتراکا میاد پایینتر یا 2- کیفیت بهتر میشه و میره به سمت تسک‌های ایجنتیک سنگین رو خوب(و بهتر از رقبا) انجام دادن. تا اینجا Mimo و GLM و مدل‌های چینی، واقعا توی هزینه و... همه رو میزنن</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4017" target="_blank">📅 16:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4016">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAr5gLwWQKn0qOsRBF2ceSArHQ7PkI59nZntblGFt3w_64XM0vznMCq78Oej52Vfl47RasfvqWpRy7QXJcioejcA55kXlSrsQs15V77DzKvqn7hOVnEvqW8LmWxZzhOA8gxoi41NnjzwHt8rXR579O5LptYge5sh38lSWN-HkVXnYjNi5ZI5OEbMaVoYpA1hOaer-6kNjiDsGaJgrVUf0_RPz7MPU5r8Vy_LsOdaEAWFdDjttLbqm0GL0iPuyo8hSeSncWQaQ7HAe-CjmiRoReRCmx0xBJ3D3s9n-uNurXN9O1Vdm0Stx9qL44ZQakH1KqiCtFjkAApFYI1-JP4UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه بیش از ۱۸۰ هزار star گیت‌هاب گرفت — یعنی سریع‌ترین رشد یه پروژه متن‌باز ایجنتی توی ۲۰۲۶. مجوزش هم MIT و کاملاً رایگانه.
تفاوتش با بقیه ایجنت‌ها اینه که نه صرفا یه دستیار کدنویسی تنهاست، نه یه wrapper ساده دور یه API. هرمس روی سرور/کامپیوتر تو زندگی می‌کنه، از هر تجربه‌ای یاد می‌گیره و هر روز کاربلدتر می‌شه.
مثلا دیشب که من بهش گفتم جدیدترین اخبار فیلم و سریال رو برام پیدا کن.
رفت که توی گوگل سرچ کنه، اما گوگل بلاکش کرد و نتونست.
به جاش از یه راه جایگزین استفاده کرد.
دفعه‌ی بعد، که اینجا پستش رو گذاشتم:
https://t.me/MatinSenPaii/4014
بهش گفتم که خب جدیدترین اخبار ai رو بیار
دیگه نرفت سراغ گوگل. چون یاد گرفته بود که گوگل روی آیپی من بلاک می‌کنه، برای همین مستقیم از ابزار جایگزینش استفاده کرد. که ما رو میرسونه به اولین و بهترین ویژگیش:
🤔
حلقه یادگیری بسته — قابلیت اصلی
این مهم‌ترین ویژگی هرمسه. بعد از هر اجرای task، هرمس یه لایه ارزیابی اضافه می‌کنه — نتیجه رو بررسی می‌کنه، الگوهای قابل استفاده رو استخراج می‌کنه و به صورت فایل‌های Skill ذخیره می‌کنه. دفعه بعد که مشکل مشابهی داشته باشی، به جای اینکه از صفر استدلال کنه، مستقیم از Skill آماده استفاده می‌کنه.
ادعای عملکردی‌شون هم اینه که ایجنت‌هایی با ۲۰+ Skill خودساخته، task‌های مشابه رو ۴۰٪ سریع‌تر (از نظر مصرف token و زمان) انجام می‌دن — که توسط TokenMix هم تایید شده.
📚
همه جا هست، با یه حافظه مشترک
تلگرام، دیسکورد، اسلک، واتساپ، سیگنال، ایمیل، CLI — یه ایجنت، یه حافظه، همه‌ی پلتفرم‌ها. به علاوه دو ماه پیش هم پشتیبانی از iMessage، WeChat و اندروید (از طریق Termux) اضافه شد.
💪
ابزارهای قدرتمند built-in
جستجوی وب، اتوماسیون مرورگر، vision، تولید تصویر، text-to-speech و استدلال چندمدله — همه از طریق یه اشتراک Nous Portal یا api ای که شما می‌دید بهش(اگر این قابلیبت‌ها رو داشته باشه مثلا جمنای) قابل دسترسه.
همینطور با Nous Portal، OpenRouter (بیش از ۲۰۰ مدل)، NovitaAI، NVIDIA NIM، Xiaomi MiMo، xAI/GLM، Kimi، OpenAI، Hugging Face یا endpoint شخصی خودت کار می‌کنه. با دستور hermes model بین مدل‌ها سوئیچ می‌کنی — بدون تغییر کد، بدون lock-in.
:
📆
زمان‌بندی طبیعی
زمان‌بندی با زبان طبیعی برای گزارش‌ها، بک‌آپ‌ها و briefingها — بدون نظارت، از طریق gateway اجرا می‌شه. یعنی می‌تونی بگی «هر صبح ساعت ۸ یه خلاصه از جدیدترین اخبار ai بفرست پیوی تلگرامم» و کار تمومه. مثل n8 n سر آدم کچل نمیشه.
🏆
اپ دسکتاپ (تازه اومده)
بیست روز پیش، Hermes Desktop به صورت public preview با نصب‌کننده‌ی native برای ویندوز، مک و لینوکس منتشر شد. اپ دسکتاپ از همون core مشترکه — config، API key، session، Skill و حافظه رو با CLI و gateway به اشتراک می‌ذاره. یه fork جدید نیست، فقط یه رابط گرافیکی روی همون ایجنته.
😎
حریم خصوصی و امنیت
تمام داده‌ها روی ماشین خودت می‌مونن. هیچ telemetry و trackingی نیست. از آپریل ۲۰۲۶ تا الان هیچ CVE عمومی‌ای برای هرمس گزارش نشده، و به صورت پیش‌فرض اسکن prompt injection و فیلتر credential هم داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4016" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4015">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب خب، دیروز فرصت نشد؛
امروز Hermes رو یه معرفی کامل می‌کنم</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4015" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4014">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rnLB2OvXly-xDjjZvHGWxwys2cpxcU0ogKIU73mAL-LYZ868IOHC8rmRfy4UmYNbGRmS9fws9z_7zr_j4fznFe8Wz9R6Mh0mF3vqWUFflUzXvEJVFI8c-TiLVB6zoTv-ImvoLqdBMihERVPlL-jOObnBYUzAd_WAvHtdCjqZqpjteYSfr51DBIpsDejW_UeAypb8vMBnnWOwx5Q_7URy3UUwI-yx9i9W8DnkjGEJUEzZ3bjwoa9PUzNrzEya-9QPNJ1Y999vEVDvdIabuKwa7cSe8IK8SVfp03EFA8Y1kjEtgb-rN-Cru0RdDi4bnf0H6vIa7RSqmBf7tcl5zTB5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:  سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4014" target="_blank">📅 02:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خلاصه‌سازی ترانسکریپت YouTube</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4013" target="_blank">📅 00:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJdsKlW0nzoySqXE42poNmRh7Jng2lSHvsubkKJ8laS9UPIq8ceH-clJKppyySchP4zowEd6s4jRCU8Gxa3DZV0afhSFp7EXbOFCtrdrgcQYzoyB477_0cB6ly-WwXkpW53LNg8tEQifmxFunIPvFRa2hYlMbCr3BGrYleFYTo5jUfTT_iybheEF6T6tq1CQov8t3TiEbojYEMhmxf0xDx2vUynmppqRBp6VkaHA7-2_-q1hWXTo1v6Otj6Mz5OkRY9UvTlxMWYZd0J-I9h-rMQl7t_fukd-xbhHF1b0dIR07b0Fs7frhdabEBUQ52WCH3Bwq2NLBn9wEPuqxFx7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:
سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون
اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه
برنامه‌ریزی cron job برای وظایف تکراری
مدیریت فایل‌ها (خواندن، نوشتن، جستجو، ویرایش، patch)
💻
توسعه نرم‌افزار
ساختاردهی کامل پروژه، کدنویسی و ریفکتور
گردش کار PR (branch، commit، open، review، merge)
توسعه مبتنی بر تست، دیباگ، بررسی کد
ساخت و اجرای پروژه‌ها (Python، Node.js و غیره)
🌐
وب و تحقیق
مرور وب، scrape صفحات و جستجو
فراخوانی API، تعامل با GitHub، Airtable، Notion، Google Workspace
جستجوی مقالات علمی در arXiv
مانیتور کردن وبلاگ‌ها و فیدهای RSS
🎨
خلاقیت و مدیا
تولید ASCII art، دیاگرام‌های معماری، اینفوگرافیک
ساخت پروتوتایپ HTML، انیمیشن‌های p5.js
تحلیل تصویر، تبدیل متن به گفتار
خلاصه‌سازی ترانسکریپت YouTube
🤖
Agent های خودمختار
تفویض زیروظایف به subagent های پس‌زمینه برای کار موازی
راه‌اندازی Codex/Claude Code برای وظایف تخصصی کدنویسی
📋
بهره‌وری
حافظه پایدار (یادآوری ترجیحات بین session ها)
سیستم Skill (ذخیره workflow های قابل استفاده مجدد)
یادداشت‌برداری با Obsidian
کنترل خانه هوشمند (Philips Hue)</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4012" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون https://t.me/MatinSenPaii/3990 ، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4011" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4010">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اپلیکیشنش متاسفانه پر از باگه اصلا Custom Url به درستی نمیگیره، سرچش بعضی وقتا خرابه و...
البته خودشون هم گفته بودن فاز تست هست هنوز
درود بر CLI</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4010" target="_blank">📅 00:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RahJC86YL6ErGyQxywiBLTEMjuSobbR1brCUeewBNfX-bcMFYXkHCZNOb0-r20QtzWTPn9ez0R7Gv_x_rPwpO4731jHzmjCryulN_p9yWjFsr0DbbKm5Cv8eNwiWvIIi_anaxRxOk5ru27pRQl6z2WEVAUgB9FEqm5lkmA6FTDH93aO0M4mOWV15BWe1JzD8cXNphOFPOqHIq979errsAWtO4ywYaR23lsHwNmw3-x_7YD2Hl96__1YPDsY5_orE7IMO_68YHkpH_edmC1pEnX2nyfIu0J93Tu8_-ArhZExgCHUUp1E3ByfGltvKlyyJq3Xrf9za6aTtP5KiJRQQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i2KSndSqPdmvWF8iuf4MVwtiqudEAvHbPSD8DALj3t9y111-XfwYBtuaHeAvYx8h0FFdnOD_flFQPZwcK0v0pF0dzadnkb519zqxJz3K7MHuayNNumi-AxsDuYqSMs7bRj1SPKq4LFobliJjugbs4PzhUgr5pCj54GRK2vi3aUhrAQPXp-t-5HNQCP_rzK-YZeEo1MHAE7NcKCq1ZgudSqOLBHuPlTxm_noePA3J-TZOziNtVn5DObj85v8wYbliARC6Hy6KSWZv5DlD3TmBECSCeA9-XwIkLME3m1hpj-srZB4qF7B-zyySCHrWeIA6iiOIvLwtMdogteT8J4h3Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون
https://t.me/MatinSenPaii/3990
، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4008" target="_blank">📅 00:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lV5d2XOVUpljfBEPhFmlKiRR_H4QKsnoY4ZHcg6y-GJtxBvl-Lcr27gO71W_60QBIMaUK4UpvT4Qc8uUVi5dR8giLYl13lrtLsUdlqOiHBpt6QDJVpSjsFNGjcLWsYKVlEJrXd4jvxFRTwaU2nHo9euJsHGUJi9_KT09FGqsqRCBunwVDkoGviAaIKKaGJ67gNrvSbUTSAQzabh7xvk1Sgb9rmrBx70QG6ORkZziG3OtSbB7uF9ViYKHoAlpD_zfPsXMjz3cqftizz5TlPCJnln906Dt9caeA7n3m2t8ow-CPwECzyv0WVwCTQf2fT9lqqUPFV2kd-G_rYSmeJl6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKly0Vf3ll-LWL2nHzqklTBYq9KY_PV5rHzb8mLMPpA4wEAk9M_UVx1z8nqvzLIoSkH4w0JTsOI66sGZjv5srSR9LdAgI__tU1NjFQYaf8EqBGdGUQAipQ_-lodWaalyHHoEivRd5U-6A2wlTXNvcVQW4zkknnK1KNxjO6RPiKvamq7ucD1NgpoTU7I1dwxJfCbVLYD-2tT1cy9zuIgNIte2_JmtykVl5wRJgbklfGV63TjO-lWdnTwthC_H-28RYXjCdXcXDmxFv3gsMOHbbLLO1WhLhsVCxKvExyMMgKpSqA19Gn0ugU0O1qHpCH2vfslh3sy9EqKh629vcy0TDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3998" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/3998" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/3997" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برای دور زدن تحریم‌های اندروید استودیو، قبلا هزارتا پشتک وارو میزدیم. همزمان Shecan میزدیم و پروکسی و وی پی ان
🤣
اما الان با پروکسیفایر که وسطای این ویدئو
https://t.me/MatinSenPaii/3372
آموزش داده بودم، به راحتی هرچی نیاز داشتم با کانفیگ‌های کلودفلر دانلود کردم. با pdanet+ هم میتونید دور بزنید</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3996" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برای یه کاری دارم اندروید استودیو نصب می‌کنم و از الان گریه‌ام گرفته
😭
خداحافظ جای خالی روی لپ تاپ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3995" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:  برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید. برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3994" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:
برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید.
برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.
بعدش روی آیکن مربع (سمت چپ فیلد Name و آیکن سنجاق) بزنین تا همه رکورد‌ها رو  انتخاب کنه و بعد پاک کنین همه رو.
اینکارو که کردید برگردید توی قسمت overview  و روی Review on Blocked Content page → بزنین.
توی صفحه بعدی روی آیکن سه نقطه بزنین و گزینه Request Review رو بزنین و I have removed the content. رو انتخاب کنین و بعد روی Request review بزنین.
یکم بعدش باید آنبلاک بشه دامینتون.
هرموقع که آنبلاک شد برگردید تو قسمت Dns Records و روی گزینه Import بزنین و اون خروجی‌ای که دفعه قبلی اکسپورت کرده بودن رو این سری import کنین که راحت همه رکوردهاتون برگردن.
احتمالش زیاده که مشکلتون حل بشه و دامینتون برگرده.</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/3993" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از اینجا مستقیم میتونید برید سراغ آفر دیپ‌سیک رایگان اگه گیج شدید:
https://www.openmodel.ai/event</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/3992" target="_blank">📅 15:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3991" target="_blank">📅 15:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kNlhMEo_k0FBU6m70NAjwjbGNVoSTKAt4WuICDqm_p6hMUd0Egu9om1oZ37OiQlaDgHbJ3eRW4fofUTWXQMi77QUtkU2egh7jxHELqPKaM7hMhR3eLIZqz27Ev8_U15MdI8yhYGRw4r79ut5q8NAzIH1yQDJ6gsTmSBYwZBJX_fgoiTVGer2V5hqxpHvbsE2Yq6f_aG5ry4YBnQh90-mGK8iLSwNqd45UhDcZ_4Swoy24e_CdFKupqOuqyw_qjw6xetXl_LElAU2-s3W93zP0cGalFp2qLpb1k4RH7D85lwa_iRjGx824e6eFGuajkvaXHkHtk5BihQ5iHM9_N3OqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده
https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3990" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gfMqTM1ggzzauZ2_2EBfWMZ4jLzd4vwgIPE1LobnikFt1PvWo74SgXzgiKkA-1OuzY-isaWHO4Hjv8bO7inz4rCnyoo1ZC_XXLU3bnCEAYAFpnC3bDRSS0Ul-PC4Ri5yIQsRgbP1xqerTNF_BMdBGBQtTQHd6vcYmI2qy8iv034qt57tB9UslASHFwFlK2eU8bitYi_fpiUjY9ZuoHBnW0c-5-k5H6Ed9SYBpNEKKcNdFwBaOqwJY44Lzuf7a-UqWeGdbRTXE3Cm7VgZunYMVissBAMcd45Duun3cEMiP5fW_SmV2O1wXp5w3Z8rMQM6R9Cxq02-MBtlKnwIErweSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..    Site 1: retrogames.onl‎ Site 2: retrogames.cc   @Linuxor ~ fireabusefyan</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3989" target="_blank">📅 14:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct-V9xCktLbeVeIAnrBtdr8FXaSNwmrv5G_wt9NSyC0-wENrCZp13Kma_dnfQWP3BsV-zAn1yhOLCCEuif3DZg9NISZMprbyMcOCpfkskeKL0znf4YKO23mIJDT6G4fcoe7Cbhnt7pq6cRvMYF9B5r7H8aVMGPaphKaNKZzzUGwnHz1Jtc_lHOVwrnTvpXmKa-q5S8M8BKsNHHzN9bOWJAC5hg9aT79sb0OX1axIHC4J3swpTOBSCYOM5B8xv1ddDkDw5nJQ3TOk2CFn2lzZmsigo8fiF8G2Hsf2oz06vh6AnFhogbCDlWs6r49dymbDvtCOGrrqQD1PsgMX_TTA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..
Site 1:
retrogames.onl
‎
Site 2:
retrogames.cc
@Linuxor
~ fireabusefyan</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3988" target="_blank">📅 14:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده
اول باید چک کنی آب وصله بعد کارتو بکنی وگرنه ممکنه گیر کنی
✍️
ادوارد وانیلی</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/3987" target="_blank">📅 13:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NUvOJpGjB9FDMst5ykZCSGk0B_ZyHgraEQx7JbtoP677qyy4IYZoSrRr6-GoX63LePt3xNXTlqWaEzBfbEYyBhk4lTJE_Uau0E4szNfNRCBvGvPLVFdni0oJ-MZQSlVvA_JBswQ8DRmvNsFk8tHVUuUVC9CfczmF2Z2mwM4lQRQCe5N-aabJzhpcY9uNvGeY5pcuyFLuc-TWOvmIdQEcK-b0Vj_6DlP-3n8b4lbgCappTYoDesGSVPtKKBxVQvEvjapYZV-G8Tk5qsS_x0tMS32kQ5jjINAxSYsdrZNGJoB1HhPxEv-CJf1InRYQCZVp1cCNpMjcxGotqs9F4tJ6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید که توی توییتر یا جای دیگه، ننویسه عکستون توسط هوش مصنوعی ساخته شده(نمیدونم چرا برای خودم رو مخه) می‌تونید یک بار اون عکس رو توی save message تلگرامتون بفرستید، سیوش کنید مجددا که متادیتا پاک بشه و اونوقت اگه پستش کنید اینو نمی‌نویسه</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3986" target="_blank">📅 11:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Olu_m0wudl6EAWPPgIm6IkP_YhiX138ljSLMkgTPDukDWGpRLRoHVuKDEnj2uOuvYpud8RKnLyoGhaseZqaWiDf_IxSJ1WxkwVvF7fXIhN1SZHf87s1_AizrY1SqJ59w9hi35C8mXwbRxrlzsPXVqPBNK5asTCkxVvGUWLc60-S695Z_1LjUOtDSXgpKYnHLlae07o8DXut4x4T2vtv9YMA50gM3ZGDVgWUFex0n_9hMjgOhbvtfBUiworyCENekwml2mXgUv_zqXVMhcBf3HI27nOzhysLVaWvaAEfDLy-NKkPoWiyLM9pw1DxyWUJbHUpwrdawjVxUJI3Eyn6How.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیستم بانکداری و کریپتو رسما تبدیل به طویله شده</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3985" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3984" target="_blank">📅 17:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3983" target="_blank">📅 17:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Iwana Proxy_1.0.apk</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3982" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
