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
<img src="https://cdn5.telesco.pe/file/brtrORJalMfrrebJiXj9ESFbviE5gYZKclHTVBpmy43AiV9Jmr7f1TTryIeA8SacmQH9mowl3zJgWnC3E2tcWWRPjcqfUrJGijb2KBJ7eclEbviVvwY__SonjrrPX7Zvdea-z3asA6ki4wqF7txg_X2W2YWD91JZjozBRlRsqlGZ_Ytb_RmTLS0WcHMid36Puyh7G6Nirv1UWeyeLuUEgN5-d9GaQKgkv1qxDbmJupJGzxHJ3qkmuOpffG0hUnhXQ2ImcPgITbZFacSMxwFs5XrLHI_2ITbmMEwL7HGRBCg70NI1FsWKf1fIKStz28qOKYIVUUsDutT_Esr43fsWiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 501K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 08:27:22</div>
<hr>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aciY3P9YX3YhtWuL15LXx4HG_txeo3NEBb5fH9fPd8X85RMPOAhVwl9iNFk80kDbQbWQgANE7LXeDzpGokZfr2PKAcsS8IVilN2jdc8tj4KPrRPg9NuCm99LtLCvS6tYZf-BE5cevsmu9eUCDfeyFZxbrkIfSmGt4_EbuEFwAJcapVoR68rd1FmhwdQfdKVWb9TbBIAvYg4HL8PKZGuxFtUqaoN99CaN3xyNxZXvF9kIe8YFDzM5m4gJG00fjMECVL2-Undtgr1sFVOHJt3r1_pV8gnR0qyNuOrbgryp1vbRlgLUG_XAYuB53yqDTibO5WMJirW1N_HeChSDqrJ7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE3ou-csGdduQBcPL3w1dVjemzPn2as8NdND-0mJfm0k0zyEkgOuJeYqLowVZjjYk6pQsdZNeU6JJytnmym0urI6c7_FjAqLxzW4OV_98nIXR3Jb5x6XQZ9MSMmy7VKFRzCccmYoKghLCTULxePCJtMy7jgzgVLEcYnmtT6qk7xa7kWjR85ZX3JdF_0-TDDnVs48HOQ0ockObe6S_CYL9jRtzAJsHBfhz28wVFMoZXdqQy3hdq9qKLScwI_PRgslAVtuuMkRUxGYQQSKrwokmewQjbAqzG9y0wsHfgPIjqLKijeeJbq_AtlxNfJAbcYvdoRtdq50_pK2QjQX0oG5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwrjqzJZLvYeQPrWUrGgVxTc0Q2d8OepgLor2EB05Co-f_AOG9uunLGwD_EKqUXuLIhfDRhFx7HsmHVJ5JivS9qdJ0lQBbVMoOhCvQLCJF17n9AFCpOZJwUoQDAnMnfApfn1OsnwLLbFB0xpsydGEK-HM0GGSotcTxHoXNyLPa0WcLnymWb4ZhemZIcyW_d3LyrJym4uQdms4Oy5gqraQ3eQUCGc-8RtKUfqvfHu8BYV2M_kOLR7NeJs3cIYvY_Qz-FqpL9MQi6Qi0lSfjG7pN5DbbC-yUBSlDioexWekoR30clhH1Aju2S0D31Bp96ih4lK6BpUUzeF1SCObHNGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glryTqvJKAIoCivGtk5cF192CB0_AwtUdhGhBH0Tu3EousB5BpVUSM6aG5eL_UQmjD_dy1kOjKBuLr3WQ1IRoRd0lxeg5KHfJQd2HqDSuMw-l8srTJVdEOPaHjJBYZBOzYy0gQWMr0Llb4AJ3l1naP5UNqZcnB4WGHcoqXLUm1rRNPD_f3AYWKEqJqgnzbaEnO0SfYKAawXe0Uk9brS6keGm8TnJTjQq6rBA6KQUWuJ44mP3S-jQCTEN4NnkmPL41zJ98Fc5Y1bo14qoiMlWgRn6DV6vFoZBXz30Q0yXVoMXszBB3I2thvnU4oM7-6Gd9EsLvdh_zc4k9-lp6yCYkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCgWKCFaaaua0yMM7WwZVZT_LoFmW3gk69Y-KuW0Yq-t2T4YA0P-EN0zaeY79fiHVPjfgxUsj1bH0jUYZ3TYfSlEzw5XRNH-VsLlxbWrimI8YNspLi4BO5M5lPdB0_dJ55c9OuGmf9hrH6O-TWfQbEkAW4gLuneKR_Dpz7fZ8wyhKbuSvJlEf4Gl_ohRa2J1arJ6z3dZaNa3zVFryE9YOALZf7WXiF-k67oVfc0anzPpo2fnjA9D0lXg0_JdoNWeY01nbHmU0oZk3jgBJTT0pvp4vTHlH1RyouGkd84z7jjG3DzVPGNEDpRU60VYAi00y1EcjCaV91aWUZEFN8itYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtBuGxMX4z8Q4-7mtkGA1HK0mvta3V4T2H1bEOhj7v3uQvJ7uGSfSQVMunsTzwxce2-2FsGpNsKRZPp8Z8ts4Mn2ubC5ve6-vh4sf46lCnxoc2v-k59SK4rJ3vB2RZVrZccNsAyWH03Op1SFREfHM4xmUO83-ZUGuLZ-8glWLAAz94xK6DW9iA_Zq9iBdhlRzlUPTj9o9_HC8rKa4Z5Gsh1AGy_G6Gr08y2cIOl1Te9O8znxnpJitgtNVsFB1kCP-QPBOqKuv1PHj_T8iidHqaNIwZvjnDOnyVI4IOzi_pIPa_twOaLG1wdsj0WRfHvc-5v_yvYINnxKVmzs6m6YxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuwkUouDRqDTUE1FImiwbLac18WgGcd6Pfywfy49u7T7xbIJ-GqQU0LwuEQofxIGbYR7NdQHd68Xi7Ajc6q5ekwOhjxcTm3wLKKe-aUDLBbf2nqAJCW6vy-1hHVXiXwLSQhftZ5SIeMbk27VzYFVrjfdqP5aIBUpeg43336szcfi7ggSfZ85q1YUSVkjrscMtue9a6fYdQN6TlWP1wsPh1Ja0zPi0CsQh2_F0yy9l5Guehi0SPEnf5Czn45LcXjuzEsIaIJN2cYESh09liW4xvsptHoEclAzP1srLFJa7K2Snqipoxj9Xme54B8o3wwcPqV-p6IcQcOFF4k5TsmFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsJY7DmlZrVWgcCc36Wr1700qIQDod6evO_YlADCr3ubBe0ggikUEJp628MjeprEE7kKMi1pDmpA44fwGf1vETjUt0uwaj3QQYE-7AwfiiOU46Ckv5r3KHlSWDZsWPIvox3j5qRunj4Un9gFt9YDO82GFtwhBWK-ftlezefBag_nZO2BJm3G724Tmjsrw-VGzbIdrcsWzHogVtYlc0arZGtuOMJF_TZhLeQt-sz_LZMvuGQ_Q7efunUJdScf6NoCpQ1Y6z30JPMwjrl13CirTJIL50SidqToCBs72XlhBQA63X3QDcJ3qH_HwIf_s-sr5qXI-6vL6Y1-9WGc-bgg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ofCNhZ1eXlL7KTd0qoSpbRP16wSf9NTFvZa3r1yaLxObgyMuG1DyAPqzV4cVrdkT3pshFu13rlScWl7IsakMSeEZhLOnCYRs1ucpAaabNPYuG7P7cQbV3N7XataSg64968U4W8CSIpqfT-VBIxDHaLu4pxWVrxTUWYjvG-JxLHJ-UiWYyUUQ7M4i1oRV_fcrKXzHolJ0666WGa1Y6gXLAdl8Tg73S9_jp40jxO_wffbm4EATV_YiX6mLEfWn5ejynv9YvdLydl6QHRfHRTsXW8EEze_d-PKlSlEF9j9E7fAy9I0k4tm9a82b9_g7tjwhbysa8fr2pKxYfnSb57rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxmJjOyBZ0BmweILxNdcjJGf-C7iBaQqno2sGN-ynGvbJMWxLJeSbqyVgcG3QbPDqP8ZsUCIrOS619BbMJTKFNbVjVEuHOgRmgesIK3e2UWT_M3p7kLPzjXYvG7uAalJm6qbVBJuq9kt4VGCZ0WXGs99WGzPMT-f4g8PUU6Zsx9rWhSkcKvObUAyrr97ejf8l7YiMrK-KohPlNlKddRZtZNYbW_MBBYGICTRITwgFaVndHQz0A-bUCNilOJ3iKl6lTCzDzQWqbx7-lvFLG0OaQHDBuZTPoLDOTyLJErArSq8C0YuEfskUddrXDD9c1jr1-5Sf8BDs47wVbloI4NazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNd2CdItzmWQo6TQnbKw9Brd0z29wFc-gAxOfjlDA_wsojPV0bd3tKTi5q3XreUmdeUIGMoenMYyFskj1wihTGD0hgPMlfA9PXv3eDhWHvjpRDn1Rw5S3MND4iaD9Fq5ddGWWtVQ1fF5KZyTbx62VvUmzOUkUTOceTyB3ADP_z5CP-kooq3Lz57mVK90XCluycu4P8XEnQxjbDPITS1m_Xxa92glNOvnUENhg_OzpTnF8qyFHs1XgrGnXQGVsb6vBVePUtKWBZ4h-jb5N0GL8eWfXwM9ljakaoAhmb6WG1-NiLOoYuHm8tqWEl3_g1pIlOkBhrrEgtQ2fCJ-HzXn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH_M--OTSpuK6xijkzCgM7EGKq80OhtwgVWGCmearlmC7aC1W7FFknIEq6nL_XcD2-1PRMa7TN_AvioWZgb1Y9Sw1E8lowh6vieTh8Pj8np6ZMteYWfrLAWVOR-hf2cydqxNpt5RoKdl-pDwSGaoaty0l91sblEiaxt8Z0O8zKVwaroAlkMGvzbWxUaclyhTnY7LJBWhYh5b0T3H0A_NzaUxzvLrudZfGUn9iRNmdHVbqT-qhABGowBUMuFm8THUJ9SKGkAKhzapsUIyry2AHAesAlXmkNKOcnvhwtHny1gbkn0Sqjo5bgwrHnjBoFTfKHH3SvosALF03ayGG7uAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C19gnHYhEj1VTaqLa_JsCTh_xcby803d97Nh6n4DhsNQgcavXnqfbwkMDEI42paHkYqeqZPoQ6SucfnB_FZJex5zIXOfPquHvm2Wz38IUdOeGzUGTOHxDktiv3VL-kI3MouDZ8WP1Lv8ZTJedzODGEoCXwCcmVohKL1InJw3qx_Y1_7gyL11FRNSZzdJBEXjEll2zt37BRgi3ceSpSC3-h3LOZmmwR_6wW84BBj8DuHTOh4QG3xUEuQ45FRJhnsbp9JZyfI5EVSVk_zBEiP_V4-4Dq7hNViPYIMu09llUbk-EH5TCczvdC6QRFq5KdRctf5Jbs_Iz6tXaurEgKkPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuH7kZqIo1KPVOKHCVJPbJrNzCiYbxfita9GVSnduXxjTzfi3AKR7QVqD2nd-eWJoNt7Kj_9PkQGXGn8UWeBozdYrnWboh3KRhAYx0KeZEtwFxuqq5M4jdgdPw2qB_T6l7o0U62X0tB8Jgw2fvxLiTlnGlrBI6tIUutdS2_iTbtp6rXArN_o3g-VJdo8kd6NFGJtBPwvzFJNFiou2cFRZ2_md5Uv7DzxLn74LMM7neTNxC9K9pAzd-TYLne0ZX0EjrkVdnU3VhR6E-E9IDaDHVv_A96DjcXfrIwlg3Kik3F141o20II0OP4z49ogoj43VGhubaaRIrXgQM0cjUA70A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx67Yuy0o0FTpB4N8sJK3oDGHy_j7THIM9i-YoN5yu_GjjKxTYfYbSEsz4jE-d3MGf9ANyE2U7g02H78X_ldCmpmmYOLIoA4dOqHs8HQQrMO7I4_GQHECzPawzkkhg34kDnARRD4woG5CstP6V1hkm60EMOXUkkIFpqrwpMxsR4qhAiB8vw6Agkru-xxoAc62Pvty0qRFcvNB-rTr_il0TLB2N6Fgw0mmeX9YezTAqJuZQ_-BB1wDvt4xqAsCk3xJO6zWt_xd8cimQ-HPCASFS6ls6xoogG-VEBQcedBACp85U-qpNJ1gmjuqdGhrABlv9QFfa4qGOCKoT5lxuJTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpIfQ_GT7qrU7EH7jDyci5ZkzH0ZluY8vIFWDzsuErCDf_ePXKwpNjhpQl9fv1E3eO6mhKzNe2Op6fbLgWgzAjYSI08JT0hiFkiczU0tHW6QEVs3ba0dtWkQ8xV8BR194hsE-6XagNoLDBIEqhhTolLN4hJvDd3fVRo7FgamjxCRa7fuu_bpbfWFt0-oblVoMc8anPPnKPQxvjAsd4gXgwRdZZy_fYwaE2NM9UuBttZYv80W-Oc_BSU4DEGZpg8qCV8p_qfVu21B9-GcLCXPf5jMQACbQiWW_l7A0AaKAb7AS-OtfL5IaKxjNUSk9x0iH7ohFEKTBcHIul_g0GAV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1git3DNZi4UbfRWiWLlD1mmu0NapExuNFU4qGBTdm-_vodScDPaAwNxC4nliw-K0Z8iJ4s4r5DWarkKZ6pDGbOd1FXw-jqVJYHgKotSo0cm-GfqEhQ3pQvpHatdzAIB-erj4llSZ62UtBUAZyXaLfNi2yf2mZLZk8y3sI_uHB_g6FEk4JRlcW79YR1TxjU_1UfcuZqGA5nEAJvI0g7l1-THdSkwEeVuehBoKquvSBklv699qzDuaZ8vINGtHK9-9FQzUgzcAy_RY6TpbAUsLcFKROFRoJeoL0FlTVV118_me78zNU7Re38yaFQSRnf_xCSkRFdzBCZhQ3UpJaRSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYdJqaiYXZyYi__F1XAM22YO67kdAKSV0F4hU1wqssDH9Vk7cwuQtWU69sDsUO99X4mp1aBkMjbJ0TmfrLcjVQ_3nCg3b3B5ZX-F9loeZl414NEvwOvVoEgrVOHJXZHtZXuDRrnkCUdkQJw5ToO-54vRfcZ2E1-DzaXQxkofDCjD3ZHTLHihzAr0JR4aKCjox3HAa0-tsXKieWvxWvDTLxoBr3UgU517HxgEARNp71_7cBEyQhEP53rBWZLemQliLNqaKorG3IGvyb7hy0TI-imKL1u_MBE3OWtENz2HpCDlnIjnBWVw7ARVjv9OGyAY3QyOIV9GgSD4XL1W98u-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWyRHGdSdije0HpZGADMkjPvQBjUAqjCQTuhjrTvgFA5h9wsQdvRzOupAYblL4RoSYFRUZBM_goRY31Z84Oq6fYpmzCChxLd8SZydJWdoM5xZUJbcYKi2MqrzRSgGDOYbsWL_76wWEtBaDoF_ckUF0hGU1JXexYFagQxZPWRGhVYQza3vfkEC8sgfz-nBOz4HdPWK5EPPN1_LKF6QokNu0MyGvwR14IHBdMNc7G1DNZj4_fu19NojruX7h_IUv5xq2a7AFgYY-GGAO4ChbhIRarEnc0uMeONnSHjyKPy3MvrTsM8krDFsFPIrjwzNjmlggiN7B9xoUjdmtt2Q4rgtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0HCDRgZIIq2HuulZtVyzYvfMi5IeDp_yshZ3Hq5trumVl9DKS2-yiKlleQpPuVcEvcjvhooiEBtifLvo18H1OUNfgkxTfvuLaDB790ZjOsF19TBniimJexe3vrIyknaoFMRsqPpTWceZkWwMeFA9LrNsKiRBO_Sx06-su-YHH4fcVQsX1j2X8ydqWYF9VLVYzrJve4N3ma1G7rBMnl_wyXdhK7rHR38ADbQIZVuB6GqEcJbZnwN3hvT4ILRRSfXpFkB3ruOYlyrXvWXkp27xqsmLLHOAggQqnka4ba3M4x0ZFDqHm1GoEhZ5N4-DLyJk0LYfOBNzdKgLhQI6dpNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBjxBAM1LmO6x9esji0nAoK41Y-y7bqr8CqniZJlzNJQ1NH2wZQ2ynJpVOWfjjhjUEIxp-DVi5Q4_fjeMaPyGuzeIvinf2JDWSadi4dVoc8tTA5NEd1Rg6twC-z4uD1bY0RbqQywaZANpi5PwQAqfhPjxdPW_CHa-Jtf6Q_kPeDTqhKctCYkNOSHJugrkmvkXtt7Z_9P_zzyu5r9GMQERNHV7lkgEXqPSv14H_ROYu_kvV1Kr7mwRCnkgQUgEf1NBBThbTbuKn3vIuCZbm-mnp3yUhlloZ-6kvKA4Ns6hTwH_5PylIu3tYoOpDhepyF11_zg4rESUHMicZlcuUTGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMjJ_qNfR6zo-B4GdnkAhHIIqK3JiGKAmQJH0AtVdW0y-ezq7K_o3o9rdbmafAJFiYp2m2Vu1oX6sKu5xlicb_5lTFuzoNTr9TaL3OxutBt_MfCzq0xOphfkFSYsN_5KXsbjTgqF5gk1dsSc39NB9OfjcIV-DmlO9F3jn52uMYTrOj_GfvzXiCLp7VhZQHdgCfOAZSyRyyPq5KHdTvPnBdD_QprZDyC6k0P4Co864YdMtFybtuu9ISRTJZJm9jZJd4qpcIU2eQH1QvdkJpi5YRwlEm0HUw1I5GqVs2Mr1LX7bkYp32Tq_ac_t2l7YUMJOS85a50B-H2S7JJYNUECWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn6Od9pp-UP1ZWfMdYNRmiEo2G87UABrsayd59oNFuSiX3xHOKJMpUy0FbHEha7ZGI3I42mZIX32KRXZQs7ohDUkiJuWEm_-53bBfIjnDo4KdCNbsFHNiUW8eIORpTiE2Ak23hKor-OGVwP3yQeOrBJnURiqBup0_4mTlclaE0Ij02v9DC7VOpypK0Mj9qfGRiMVo32MWL86FD2_wZoB9-2kV7TLmk8LRa3_30j9Hs6oVT19aC3BLDka7rcc7kIc_DfYfAb7jktbOfaqWk0pcRiG7ujEy5x45rn6j4e9k6Zig0KF1WYI4jS2jiWLXjfXcWTvV7u7JBtd-SlISOMKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAbkOKEeVzbJs-rSYYFtOjGp1A88eyJrnipNsriCzb4bJau4ETL4oQNkcim9BjL_amaZBLGj8_a1TMVzJt9TIOoiDNmShR24-j8X5nqz-OhxNPrC4Jj8nSZY5-niIYQFimw2BLwVAah6Ftzkr_p9Z3tRDFqWco3FbTaX3iHBquIJupV0E0GIhT_UzEiiaVlqIwbUfKJpiTQvpqdAKorwvoNaxSQD3rOR4KDSCv0xl4rMCz1xGtD-sOPZUtyNeDPMzEy-A7PEvCq2--MvpnHRTRVYKLk5DHMyPzaOqcEBlHAM02zp3KJV85PilXh8OCMnq2NTS_2YHb7qvv6EJJQlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEOVHNaZv2Jxpa4FGlutaaQ1RN5oZTeTOac107O3ExlLld8x7-VadbIqSuuLrzTF40_8ltaCjUQ9p_nbge5HvDBAYjNhgxSh7_yre8yTREqJ9qkLg_V9tbEyDjiBKI379_1ohdzErultbb1__og8ixJVCWW26nMZSiA_qgnPIWRnHT98LLzMlO0MakrcdqQUsph1RpQ-pYUkd411SUr7E3UFDuRSU5WvPKLJczswAboac73jrhnvgnPhszQasabTwy5DQ4H8rWAe4667xZwOHPDrWqSVIS2Nl7EiL-P5_9NmebeLm61HBwqHmI9cGSC3bUtpcAZ0IHZZhRRcq4f7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbWpYUj6mrKFYAaIskFT2Bmr0zTJfJoyxk1QMRn0bRYspK79gEyC4Ui8Cg351pDGVRjKYTzClNOLzjNERUte11TgdMqYd_Q0uYFucdHjH-_DbLifbRYE2ePvIL6xnzAgpotLEgMGOw3eunQlFxJ2uvKovdTmUzf0JO_coqPROYc0ssS9QouZAQVEzhf9sjBd-8gN2d3D-xFHEPIKczIc6P921UFhwlT6TPnPuGpXwOvk_yD-0sa9ujO74puX7mnyAcVBf2vj0THcsgLS7lMv0ozFd20iZZuFk-dzpdgfhrmdPDxn_3zTdQJwbClCAsQulgxx3M7qlL7W8BPRWgpL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpMD_1FG6n3vd4aatAz4wQbDPL61KikOWUNgLMz6OcqbIcouug5_F_8InnD8NRM2mNRiRQasEm45dJkAVBb5q_occWGpw9aj0mg27J0Mw1L4Tcj201mKBn3psSMElUx97Z9EHyNHH1EtHzzlVU8NuGDF7XgLPXGcul3X6VuEyb9X6-ho8kI5E5sSVGgpadFTzJeQcHJBBLIsOxyh-ZGV3UwjAD1Az_qJr-x37Gfyh461L5O3t5d4KiuKN2AYRsJ8QPt0kS0ze7jvacwD8XXNuqKji1PRIIYdXTro13kG96hxLgt1P3AiZtAEdWu6saQaOEwzXaPERnqAp7zi5ylLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=APPzhk5ndpZACGZg-UD4Dy5ayB1yU8Hme-iHa0wGnZD6FJJBC1H_eQH_BxHCL6lRplsuLDYJ3lQ24ebxCZXy24a37bgseQ5tizY2ANqaDrashsGikCJxI9hJPouggjrYd8JqVjQxPdFgjjcS0Ulk6BW0YhX2vtexWP5EgLi6tD3suRjGkWrefyVlt-29PeXzU05kk4Ka4YFdpP5xrWDA9Lh9DAcPkl60dRZlq_CVPOJ0hoCWZX7Da0PumS55hQHoctvBtEiaz4qlktG1nUnHVxeRib_RzTTTnPi69IKzpmherHP8um6YopdqblNKOw5aIsXqXnjDb3bDVYzB4zPFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=AOnxDC33RA_1PWs1JpxW-13tPCFlFAXaCoUeIxfpMMFxFfGBFSl7x2_25URN0R5Ok2uWXtA4RGDK7xSXgHzkDYPh1FRnyrvl3USBkaDFqRd2FRSu9Gz8dzKO83pm6eZBwUM1y4BihGdtDyGvxYK1n0CiIv_DCHzIkz-aKgAPMnIQA7wskY-PxP21ctWLR0cftKVbpsCfZtKpePdPgML476xNVT3oIYmF9J7HCp7U3zSvnoIyGZCtDnYGXzRVWU8lJwE6Gb8507aLfBoc6zzh_RapwaQaQ4fkbvz7vjg23UT2vqa4Qs62BHPtAwt6JfshcG-wNS7cLHjIg7VwsjCvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=XroAY9u-8DgYpJtxbAovszkiZuV-loKCtMbmlKgzvp7fA3xAiEo4ATiIaAgw-NI_ZuDGxGZE_p2nzzmb97T4wd9fwvlcRwxTkmhZsqu-OKuJ-TJNGjE4lGB0rrhouQdsdWVz5onQHgGODh_kDI1X9xN6nLcLrkoHLR4lHxIs3rAB_wGz_P-QBQqvUo9Vig3Gs0GzoZSL2aegpBK9SjcX-mA16h4fU_t879dNGXqFkjMPteB6Q0ODxKceKVlJ5FQAi3hOEhYDe46RlT9NCcJ0rJIpiaBjWA1jJ1aDOvelEmCxs_QwM7b0-mXOszD106saoSP4yLmkMilJg1xGdIzvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=sHLKZyBA7IwEiSBJ9BXep9YZ9p3YMGnRYCfXBkd0bq-6f3Px3Rx6deDyd26QxbUaDq85MVofagixtMoZA0u5rrd63AgKDHhMDvAwdwypD-PMWTEEpiokA1nKgb4jPiCkUinIy3TfToP2JbOYoTV10BPPQyJH5e-J35hZeEuCOgyFYmTwvfpB-T_-9zEvdQP8TMd_iWhgFOU8YcJc22_QItBxkWsa-T0dDZgqQuzm638vWN5GhV4i_1tCf4PlOZcaLq-irAKw8SIsHYjktmv-U0BDP7CHRp--wFmBOuyG34awma5Yxwq0PyLBWdfPlKQg9DrRJQ4ODQMiJuIEOUNNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=da_snm1DjMbDeDEx8bWfCfcMB53QQXAL4Knkp_eNGEd1PafEmimg2-3DZS7F7SaxY3dMpiokVknUUexauau0kpRWzbcAW86LqIchSdIZvD0E89oqFR1LW_-zhOKYPEpl1HoAFBdJfdHcWoFBcpadtOTAj4zfsgmeaxeuF-ENW1JVmVj51F0F1vut-h_XEKkp_CuiJ6PstWUAjicofHMWBmjV0rXABp-o6PcKEmnq0X8XJGljlJM5nRSbhYrse9Iv1f08YoUpjEnCeTMmPaQqGsWfEATaIFMB-f3x33J0UocVBobLqOCU6KE7QogZTOue_hQpypk-ti-7VGds8Ewkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=YXt4-0nT7LDHdfzKjkRWc2Td2ufOgF2fM4-eR1u1xQjyNrwJ0lR_pMBONntFZta5TthzbssuUgsT9v_CHPErLPAFuQIKPDmkGfw3LbqVWePIxbaU9rKIarkajV6c9-O_N2it-AqajB12JHg_qZUWjTCTun8OB0QXVwmwqj3OYVy3I-Xjy4tDkEKYlgbB1IEi6AA0n7SyQEapDZRAdTk6r9dh6VxZgjw26h1-vMYp_HaiuGM_c5Lw8NWDxCizwKgEckpNfGKmYR7YvO5nwDJvhYfr8worTqO7C1MRE4y2opUijLPECCgOd5SQK3C6P71iUQSrtGS8T6OfI9z1BG1xVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q59OSAtfrpCUVoTduRY2AMt69f2btWXtgTsWicBIRsiRBvbyE2kZLBtuHnBjJ4R3TMySAgRXHPEOICG4V9aGxevlSb7Sse0FUy6McXh5NH97S9DYfwJlvXKXb_-oKIo014lLqRawODUwk-LB3NA23CGjwobErFgpvQ6ku61OURlFLSgfVNUTNdNTm3_dpN1oHfgWTlI2LMhU0jZDnqgdby7pxCxwqW-j7EzZp7jtrIMb331sIj8rDYdsThpVR6Iw6QbqcvDVTAtgQUqY7gQe6ML3FmyhlOHz_r07Qt1gQ57WszTuDRcTBCkODRxIj60EGRIKM9fOU-ZO2QBz5drzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=jpQ5PAg43W6lOwv12-fQdXrChG2o_CprOX20B6Wc_WkMGCfXXVGIO6hsPgf3VIJXYmTLOGtzNiLl2e9ibuI2gVEhorXMV6CV7wDjzv4UqrahHqw_W5xdmQRy8ZDOVGp1a39MJNCaQ5UracptIMaQlMwettDPAfC5ZL8z6-BkdoxTgckgO8LKjsZfcQfq1zw0vdc-iRpMhNDuhLeH8LM9fDS2l_i10u9kIdP5o4P8QcWJUvxKRnJuC0JcctB8JzbNeR9OWXxVuuqt-CnV7l8y_6VMb8iSCXLBM-4VjNhQkO7uThUmRga0Z0U52y-GSW8chCe6hg92SpF4zbkk5oeAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=jpQ5PAg43W6lOwv12-fQdXrChG2o_CprOX20B6Wc_WkMGCfXXVGIO6hsPgf3VIJXYmTLOGtzNiLl2e9ibuI2gVEhorXMV6CV7wDjzv4UqrahHqw_W5xdmQRy8ZDOVGp1a39MJNCaQ5UracptIMaQlMwettDPAfC5ZL8z6-BkdoxTgckgO8LKjsZfcQfq1zw0vdc-iRpMhNDuhLeH8LM9fDS2l_i10u9kIdP5o4P8QcWJUvxKRnJuC0JcctB8JzbNeR9OWXxVuuqt-CnV7l8y_6VMb8iSCXLBM-4VjNhQkO7uThUmRga0Z0U52y-GSW8chCe6hg92SpF4zbkk5oeAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTMc-Y21r0xJKbsEAbVDDRRfrdt6qMKPKXkeAt6cP7g7fjUvcvQ5w6_kgKtHqX2UPecPVPbWdg5dsBPwQ45Imov_zaXPLqbZr36TAiYonRas5fnMPn3H9roOo420LFJ4y66yF9zX3PVH3el6yWYx6pFeuwNMB4dz4zCQZ5POkiTSglUKkbb4AY64QZNX4V1TIOjmqN0GfNbNWdNFyaYf11Waw9qbPi7swO2ajkdc9Xb_aHwreTq-5dF7lCbz6rkyv_pDocpugHSTcDsZ3NnDqKCrfAz9wgu3pNawSD70X15YRm-T20CjiczRI_-MHlgbMFqZ4DFbxbrpFLjDW82BIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=dj424v9AH5VHInY7PdChzI4lE80_WzesVkwWXE__gZl7msnUn_tMg0bokQxChVjRqaK0zrOf5OYwMLtXPTDzeuBgY5hAkRwJ9N0IbWKN-NlmJSzaiVprsG3uSrpyOEDQrlgVnrgyaiOcU3yhmcCc6A78wcWsM85RhN36Er_ar0O51fMpvTjd_sRec1w1qnfUlNxhlQ8dGn1q6GBf_svEiStKlhjiFBGEzZCDjaVamWl4OwgE5stnEjljF_kriqRviaFkacvvnx9wKgDbEzhL_vXoWoa7puZlp8nuHvn6xnJOC5QVE8CyuOIMD-dGh8tLMNfip26q9IzVECncGFrG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=dj424v9AH5VHInY7PdChzI4lE80_WzesVkwWXE__gZl7msnUn_tMg0bokQxChVjRqaK0zrOf5OYwMLtXPTDzeuBgY5hAkRwJ9N0IbWKN-NlmJSzaiVprsG3uSrpyOEDQrlgVnrgyaiOcU3yhmcCc6A78wcWsM85RhN36Er_ar0O51fMpvTjd_sRec1w1qnfUlNxhlQ8dGn1q6GBf_svEiStKlhjiFBGEzZCDjaVamWl4OwgE5stnEjljF_kriqRviaFkacvvnx9wKgDbEzhL_vXoWoa7puZlp8nuHvn6xnJOC5QVE8CyuOIMD-dGh8tLMNfip26q9IzVECncGFrG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=f40KZdm4Ab5t_zLyDUMqYNMdKRq9iFRue-hkJsu5ddONOS-6u2epmU13DXPvNoAdUL52CwNMD_ZpkmYKY8bMSPGJTI-cnaYLFNNkmDaMpqgKt211P5_U4pxWWz6aFpejz29gytiIQu7O6s-R6WexDvDFRjVDc-MHpOMeCsYgRRQfj-hmNpxneGR7TxQkhnT8K38rv5GMUtgzK-qxFfqS0Nb8VQJlvAydZRIOpoJHGtLHrpz59nHg2ZnwGX9MML83Mt6t1zXqFhGWcwU5D3SweYv5CX03TPRYSNcHmg2L7CEOJbNHIfQHmdygjNNaKD0ixa9oR3dkhDLgLQ1w3ZG-ESdzZC3Ki2mlFeqmI6MkWhQweJWxyWYUaSC3hYcYTPWdALYpic628qYD5lbm8qurvcZzkNvboo4sRg_CS2HkPnVva_s-9Jl69EI7iQ3g7OCraGEvJfBavhGGMrFknIIqTZDLyzw9yozYNVXoH9NDmVWHQ5f8-iBfJxSuJEl7EbGADIP3XMJ63otzf9du_usc7OyI29IeFk0AmoN3pLuRN00E9TCvEUBNxkV2oV4tVcvQDjOQ9NoYqJx7Er2BrmyNB0wqNfEw_fTKMrrtHfTjgN0DFUfDy2Gn84LTgoz7_d2yjz6P0NGZRbyFZkoi5EUQZw1pp6ZaVT_5bLSRRiXl_lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=f40KZdm4Ab5t_zLyDUMqYNMdKRq9iFRue-hkJsu5ddONOS-6u2epmU13DXPvNoAdUL52CwNMD_ZpkmYKY8bMSPGJTI-cnaYLFNNkmDaMpqgKt211P5_U4pxWWz6aFpejz29gytiIQu7O6s-R6WexDvDFRjVDc-MHpOMeCsYgRRQfj-hmNpxneGR7TxQkhnT8K38rv5GMUtgzK-qxFfqS0Nb8VQJlvAydZRIOpoJHGtLHrpz59nHg2ZnwGX9MML83Mt6t1zXqFhGWcwU5D3SweYv5CX03TPRYSNcHmg2L7CEOJbNHIfQHmdygjNNaKD0ixa9oR3dkhDLgLQ1w3ZG-ESdzZC3Ki2mlFeqmI6MkWhQweJWxyWYUaSC3hYcYTPWdALYpic628qYD5lbm8qurvcZzkNvboo4sRg_CS2HkPnVva_s-9Jl69EI7iQ3g7OCraGEvJfBavhGGMrFknIIqTZDLyzw9yozYNVXoH9NDmVWHQ5f8-iBfJxSuJEl7EbGADIP3XMJ63otzf9du_usc7OyI29IeFk0AmoN3pLuRN00E9TCvEUBNxkV2oV4tVcvQDjOQ9NoYqJx7Er2BrmyNB0wqNfEw_fTKMrrtHfTjgN0DFUfDy2Gn84LTgoz7_d2yjz6P0NGZRbyFZkoi5EUQZw1pp6ZaVT_5bLSRRiXl_lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/durdPnVviKaUU0CdLGLfsDgHrDwRHmsTFOSvd0UThuIKi_yqPLQqts_I44xuxeqsj_66UvSrSsEpK12z6XywWFaHdHgAgvbAsciEu-MErAnU_Y3p9cV41iRMKC6LziTpRqNZKmKfc0sc6qfek8hZEtTICh12-5GKDOSiaj84jf2f4ugMp0PTBnubYNQYF1qdy68hR6ecyDHQjQzKZj12PpR8AVmNxiF8mcla_z1YUO0X-89_a4s6JseCC5pjW9biYxHOL_QnO7Lw3f1mQjWMmc6BgZaG3ZPRMsR28yrJkEdazsYG74K279njmzscXh1L807M_H85V_gzq3Ie7HSjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=eNuRr7w-EKoc5hhdlsCP43Ah0vwaKJbSYoHgOMFzlFPHwECcjYXm14kuQ_dMT7Vlu27c5Rn7ptgqupol7LAE8HcXuj0tAS82YWWMLTXVoKY0yggQm6LDwzAU2Cm1FxOqg-_wy4-MTengHzhNb8n2fvzBBpBDLkVetsbv94rzbwU4wHizNPEYt-9w7CvQtQsWs7vz8WgybFoV0fRF_HUYciSnT9zfWUVM7-LatpCMMqNmnb7LczcuHDrOmlrz6PCQhoBsSKMDYBigZPdXSWKr6F4Q7c3_TQD1-DJt_dgGw18RWE9tozcB5c-o7ko2o7d4QP-paRPTF03XrtJT5Ticiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=eNuRr7w-EKoc5hhdlsCP43Ah0vwaKJbSYoHgOMFzlFPHwECcjYXm14kuQ_dMT7Vlu27c5Rn7ptgqupol7LAE8HcXuj0tAS82YWWMLTXVoKY0yggQm6LDwzAU2Cm1FxOqg-_wy4-MTengHzhNb8n2fvzBBpBDLkVetsbv94rzbwU4wHizNPEYt-9w7CvQtQsWs7vz8WgybFoV0fRF_HUYciSnT9zfWUVM7-LatpCMMqNmnb7LczcuHDrOmlrz6PCQhoBsSKMDYBigZPdXSWKr6F4Q7c3_TQD1-DJt_dgGw18RWE9tozcB5c-o7ko2o7d4QP-paRPTF03XrtJT5Ticiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TseuQK0iyCPbDdjw2XBT4_t530_wBRhkdxYX73EhNrGj1ivVwBTRCK4_n_zt5cSrw3T7ZPwr-NWtsOlMNrhrzs7oClCqRNRKuDRLxtLs0u0miZYPRoh2Tt2UecRUSuyZiRsSr-ilKqUn5JMX1qRVSamoz6QfG0Vj1gnvBXO-dVhSWO1GZSIMl5ChOf7vx1QdZqUBdR87SKCGBDLXG8ipLzOPK6RYIaj2qNmHP6qLDTkDJmZWO3HfmjoIRM7UqhDTUM4Ndv-ZskQEUxXkHgLuWNn2SJ2ZZGpQDFBbbIa2pSE3XyLNkyp-Qz2irCeI7YHR_04Kwz-tZ_Wd3gsDh6NYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNFaYs1O5qzsSPncVCXLVa7hokDMOXmhbGEfkoHzCnL_RfmNR4PAYwYj3NfacF3xx9krDOPMnoDwWxGIRCMVF8wjdn0bULkRByYK-sdF69fuje6aE7E8yKIZo4coGogQXlQvH1YqZuX3sJsu2P8_1wUJgli9Ah4Gj4FTEHfVDFmEvhNxLby-_oEFXDV4DbqUi1OQDCgb-vHLmYCUOFy4BkpwX0l5tKmRKxO0HdvhrgDsPakDpRUVyWB2fb3v_nZqVK76fMERsotcQypIl-pxckjq-qFpJp5EdOSL9TCp8ODYM59dWatPA2L3Mc77jU_bJkxio_zXx9jrj8vYywW9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPtfnU4hXaw1rUisqzyBQGNueiQbUfDqwjY-acMryk4gvjg3xflMJtiIs8rCwy0Q5vxisBqYbZAxDH5hQFctIo9mJUnjBbqgKnBTWUQvFM-9qakIacjrGhOBUZtCcLYq9CQNiHGPU8CzHGfvs-wOMBCU73xflAemvu_yRKXeynhF8m8ml0zvAA0GdNcKMyMwkgWww3vZhq3pPVnZBoLQwbomcgf4kqQGwcyE_1VK1MUFIDE5j3Y_OeRfNJwKCYf3rJ36Yo1emkc4b81FtkWwUDPns4KC2ZyM-t4wi0nTBkpdQFT6Ydpk9R2cE1da3-d_h-3O4vEKmKmn8g8EDIOGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaEYO5YncbjYYX8HelGpJpz8ss1rXiTncED8k0PpYiRd83Q9aNZAe0ENMvyUuPwcLg0Dv5ORtAtfpVwTKgRbMCD3eQLf1iPGN9ArA6Bw_7JRhIum3ZqbsZ_xlYDu6HjEqL2zNjkoiLLM0kCwjfn3Ad9870xbiBioVFLDCjBxj_iuNsksRZB_irsXXjXdXz8c57RhfQlJS4Q3ulotJaSPVyZ5vta3FpMq9Y5YpkVy1DVohJK5Ih5skb_52-da2WRem-LZjx_3X-XRhspcqDSMFAPr1-eCFvpYpAYBDOcfjCdYDlN0JOfHgcZ1rsNt9yUbWP9QjYieblTUHzsxjzbrhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAtKHMucSMuKxgi9tRWhmeWLECDPLTVLOCMOZMxrlbyOLTr5fJNxn3Xp03AbOscjqGC0HdJnB5FLn5XWkYPJoHEFAn_KHz4i2yBzVGMnpH8SexTZxc45TidW66tO1vXuKz8-HvussZoyCbLeosgAvo6vhCa5Fb9NI5bXhLMQxK0iwuG8hkU3qeweBvy_I2ni7YGAq-cp3hVIpAFDevioS01mUxbuALVeuoBpsOwiMJIx6kSK9GV7FAtv33qnQw7zQRRd7lhxLPwEe4R29Cev6aaRF1lbIscLtjKK6qyMAhQiB3bozQC1ZlIt2hXupHEybFJNm6ZLuxz_n8E0Wgd9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi4l2Ze2bwUGKzJP_pMAMjTeVI3MtTj-C-ZxApfeo-Ls00MXDqP9mGOaDIl4WI5lxJCvYKqEfktQcHbulP7yDa8XI8ogUE3qpgSe2g-Z9M1hAPTZ4fI-aCZvnb-WcDaFPHkUCYbHxmdWeFBY64V5eajiOk_14uEOWfKzTMRe_bTIh48mXkMVMecVe2lYxGnpKP03Fcc5iKi-EjmIAOFxvGLOxcfsNn0E4ltbKVsIoKqj2p0r2QJrSGediemrDlST3lB55ngvSyXyF8JtYW9cryyPeEaN95CetU6GJBml7AlgiyAbPeeQv46ym_8ENhf5DfGWkqTsoRV_TiqvUx65yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0x810XezS1LAufNH133k35b9f0uiHSeWfijF2rScqzAJZ3TPIDYRQiC4JdSMenTaWPzv1WgJ4lZbtsj4I3aEj0opxJtQEXdFmTR-1v82FjaKV7wyGnzbtHo2SsACXXDtIy1zcSlaXYR4jhYzoYEn1sEepPEEZqhbDJG4dmYhmyDCz1cPv7YW0fsx5qVOAiOhR5Fn_CPpzRwaijfAJMG5zzQg2Y-22MYBGcUShcR-xQUhbPvSJuBVeLVw-DXsOruWfFifNwBS4nIJaUO7TloTI12y_hq4aNdu5Ol_vSIeGfDgP0O8gPy8-CnRz0sddOoj8KriRkfDMqgq7gxzUKF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi1EfyvAgJ6GfZXFv4QkgRI6MChS1zbGX6gGKW9t-BFPeY7nLJyTa60pdeIkf1dDx214K28-f3M3Mn7xdWFdSv9fy3nuKXZmau2F7pjhJZdOFLTlCXbbxS9qsob0Gxr9LfB0Uy8CDnqNTVtfeiaoDN3DANbx-ctBmr3S0isSgdTvC5TpaX1ofTA0TkP8lTLdYe7DtlS4KA-YPBPmWFrEgV3Z2gYmII_F8Et9mIoODmjpUyH_EDKjhkScPllEBmovc9nUvuYknWxek-dZD-jSOhd3VUyacyENgUYAiXRiR9aZBBQMgvytfsZmvA2FuIfCWFfhPF-fUOMHhxZwu5YCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-WHYmCA4g2c4Sdx0zoBfXLv1XRCshEuI2-_JLHcP7aC0-KJpxyiZDvaUhAH-FRWDOXodiC2a-B1SbJ-R7ThQhONHtHBaVat8NDpucSuBMYd-LkOuzI1B2vBFc9tuL1TEQ_FTsH6C4Oaihaiexx6OGC4RKW7F_ZsQij2TJw784HKdz5PtthwApqoxgDBjCN-bouyiHEQDKlcdLL_ahX3TKoFtxGnHcPhTQoKNPOj5n_kbxTKgsoYze5YTuPyc9J5cQOb1EVmRtU8N401sKv5sAGopAKFe6nk5xnN8M3-IfXXeBZk-E6AftEKxFMX3nJF5_HWIYOTjDeyXlEj8Ss8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok_RM4rCVFmPUW2wdF18e2qiJ0yWjdL1_4DcU8vG4lqiXk1nFBIGNK36eaVtPbIrUFHWYbECEeJiDunagqjxgC_ZpgIQ8xzLwWpnNkYqSqMj85itT2n5BCeKMptJQ5dr8EIDxwYa3DBMAWWn7CqGwJSmVcPuKFN86k7GlL-TfKX-hBKW7kk1G9Bubanke4snjmOGVyf-wzBVtDZaKLpJYJjL_MFfNo4-x4Sgqn2WZS0QPhkP0oNbLkrqtjereCZ7omW2RI4knjYBu5wOXHPAlWEedtFj3CnDVlwvZTg10l2l37mCbnYo9u5EHu_PhPg4-U7FosnAy-pUvoy243FMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEBegP2wEFqY8Uvo2mMK1kT0LFxCAb7_R4C4kJwbZsL-JrJLLBTvTF5ik8NIaH_cfggkYqM8NZ6kc7T8vL0v393_njM16pvKA8qLM0ZXIvhtKbbRZYoYGBrKbg4nNhHloj4nuW_AvCLbNG5g4ExykGUxTeRNoudontko3yQIqmqFjZhdvUCOXhkQPWAeE8cAneP61BRVLoZEDsb-3pMJzGJUgaK91ssM5GihLfnGXUByEtpXEmFNPFJ1f51yXeZqpxaSLJdcfLcm-mcxxQM_v1nbYNZ9_Fy4w1ztf2nSUkRZ9Bh5w42j6XrglQhV_7V8kzGTyglVk9pW5dOBLFWFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEXsdBxEAeqxAq80qYYKElmTjEv21zeP2IwZxN0kjDNVQCI-tIPoQP84eODDR8aJmm8MhTL7WH6gusTbitCF5uLN0DYfqdz2yr_Sink21rIark2JytXEdyTWY0APSyWBzpz4DR5O5boPXlGC3sLI9I9EYKglR4za-CRpykF7f5Botn53XBIgKC4-9zCwnm5Rdc_76aq8SkHUYjxMV3QTYMaBL6hTNrmVwNJyCiUWPKRDR2x4xRw94hZ27Mfrb2MnsF5SsJz64_H-aVAcplSrsqkxs9ymW2gOTVPEYRqpUwc4JkrNq0B1wQRBKB0ChldrMz1kOjcciF3QZ33cxgUGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f76HRybMSdeSS8swWv4153yQQRQW6SFlYNKS7je4n0tEpbTGTXIkQMDDklme1qAemCADd2A1sDGp1Tx3qs4w1A-CCK6pt3Cxv_xUKeAdCcvN-4Sn0wugXNTDPAh3wR0mif_Gr3fiYbNBiZ2JGhyRGmJbdPKtVvh4suEIKUhhgFPPYC09kOyucIGJkXZJj6ho_N4GfhonU_TsdKCGuEQZh6k7kW-M8qi1FMNdrxcfSoWjLKBxc-0Zer3XLv5pKUrj1exWaTneUPK3S1h7tXdKK-SjveRMIAB3D5wntV7zNWHGsMkUiodnPU37dIl4FpA6-13xgOwzu951_lHHF0JZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvSfjLI-Q392MPXPF_bD7jJOOuJARLun-iXJ-Q6MQvll28s1i3AkLoHI9UzAemLg3jDv7cGHHZ7QE-l3PtBwIKPfUsH4P95RhinXz7eoTdRw-Q5h3bbr_zBto3YJ2KcFGf2TW-M8sYqS93wDfHbLBRBTHwhkbYWe_wJdu69qML7PEl6hJyg1_ypm43axRkaCDPvJEiWHKkOHuJmKzJEAzxzxIGarc1bU5q5sAd5gukkhUBs4kf6QrfCMeVr3kgONQYxqOyvjfVChXkS_60lI5xc10ek78WBdOXWc16rK_0-sBEuL_wiXwPzKA1Xsfn_3oKcidHarutxM7W1I3tCaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyqUmBSmvVwX5sjigdv9BlUD5H7UCCCWQsu8JTvlp1gEsdkVncjQXxQ-BZODN8nA6jfoqriQVvdsga9WrX2cZYgG8DBgB6csYGMqZf6Mp9u1EqNedcFl8QMB3WEmbbDD0j_U5MpBVGr92XmQv3vpOJo_1E2L2LnjalZm92KYqzZVuT7MqUmTeWmWuc6jq4l_kGH1iSE1UoljDsjbLEAAkXCarJEULpEJuQqfC6Md_z3YljC5xEn3n3FK9NmAFEBkaJssPAucaVR-PmY2tGhsK-dLv_I_jKOPRENcHp6Nm52zZss3VkDmucpByxRHo8sNuuLvj-eqLxSdI3oHzCIuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qq002gs7P_1MonCFR_Abvug1qLqsL5O5doRQ_hQXzOpjwem5Fff1IUKpdTsRPJg56wswvPUPQB4LjSFS5ysMJqW0sJMxO86-rSQ8tWDhndoZQEvHeo_irZAE_Rdo89JTXYSSANbkIqAsbW8oBrZt1SLiZNrFstm_4B7Lx1j8H7ZRiPuQnRs_v9R9FjNYV99ucFtlYEG6sPs0NIo9JfMCsjeXYHWZqTdf6AVx0v0jLh8sPA3xcxcm_5m16f5tIX5lq608Hj29XBi3zrhsMBTYFLjhjeta2SRbKNki3zh2nHp8XhHXtcs9zU6qzRsYDjrStwy_a1Cd1Dlxw4IbLQQF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGqFf38VhYa8aQrwFm_Iz0nzXz1JI6HcOBEHJWerzhlYBJJc9lpoydPm8jyXfHcKULTS9zuacWvbXffAXZRAtHrMGorejDtz82pBjwXuYyZ8CjiLnmfD4tTeSeaN1GaQc_jWgAKYNRPXZ-RvJmOCVl33qgHrsTc-Sq9VoF5OKxCDB0nlq4R2O1zMRU5Kpp1QQSzu5qIuffAwwzgNwbRRxU_Ik5_8SLm4cR23l9pFCuvS4St-OXd4NtuatD2JSMW6R_1tsXoXmmPg5EdcHLy3KmqoGW0n-wfFdBsJyCUF24SekLDydWadn0OzM2tnzzesfJjMRfrqGIYP0_5rRXmVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbn2MRvq5ecKusg8PCBBqwB2OCMWCYrDCyBW1N3G6REektr40_UW2VIZt1ekQWtLujUAltTSVdRhFkuYQlTVxd6Hi8DB-9o3zdObo7wn7UBQKuiT4LIU94Q5fve_dkYybq6KD1GbiGu6ipgYTHAU2TI8eJrHvyCR4phfmprCvV7ECrMpozBjjmhA-7BhAw4Zv1IKWaoURJ5LfIZOvWlOaHk8cSOAUXhcIql3fbrH91KX8ajpSmYgsUG28bcc3iVDOOwSrQIEe3nXb11QMFPGzgqfr5JhPlOb6XAwhXW1m5AbZt9XH5xMxDUBaC3rLK5vUaVIx0wSNhLbiF8zYfG3R5rcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbn2MRvq5ecKusg8PCBBqwB2OCMWCYrDCyBW1N3G6REektr40_UW2VIZt1ekQWtLujUAltTSVdRhFkuYQlTVxd6Hi8DB-9o3zdObo7wn7UBQKuiT4LIU94Q5fve_dkYybq6KD1GbiGu6ipgYTHAU2TI8eJrHvyCR4phfmprCvV7ECrMpozBjjmhA-7BhAw4Zv1IKWaoURJ5LfIZOvWlOaHk8cSOAUXhcIql3fbrH91KX8ajpSmYgsUG28bcc3iVDOOwSrQIEe3nXb11QMFPGzgqfr5JhPlOb6XAwhXW1m5AbZt9XH5xMxDUBaC3rLK5vUaVIx0wSNhLbiF8zYfG3R5rcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrclVqrCWrcBIdO41DM-xAm2T-f_G5cxUrOR0GdA68FoV2TNiFLqr4pf2feftCOuUlHy6pgPbdMX_wY_f0-lXGnz-mdf_w3ljLXHbqM4MZrHV1FsnV2fr_60whtoUOXIiiQPSGLV85IF0LFDY3SZyObjaGh1zDtVUXj-irGOQonmIaOCibWcaBGJ5MD1NGVDEXh7OqVQ74JR9L_D51Tp13uTCJmwH3eP711j0eavmwtbk56T4Msr7tZD9YnTStJwcgEcP63FV8vvS-5OcCCm_mngg7wtqPaaxO-3_ko9mQRfLLNVbEWdizWVaONsnEAogtPtGv-Ru0M37qP12Wbshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqvd-1hIdjWBMi7m8xC7MUSmmx8Had1ak__y-BdDgFV9NhWY838HdXJjWhuf-gnNjqO0UZnLUIgQOPt__Fl3EP7cLuhRpOzXpBSSwbYCllANsif0s6xlYNmQ_Ed-PsoOXol8UCvkKznH1QTzl3ooIUkJyYh1DYWmv4-7Ni9NKrt8KGr_vdKHxdm7Ah5VUrw7qHKao_zJpnc38IB-q0uXbr7BD34_tqiTTOKghCgdgyJNGE2btajkZUUWFhwGDkO78dlmznoSVEE0dhgwT8Bmdlao8wIU-xiy1Zex30K4moeznzeCiTwIOq5KlvXEScSIEB2VLl9BGtk_ZF8pzyABHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSlggK_G1cVHIr2Oy1nJgWgRa3RsgHjm9U3KlvBUPyz4rH637snGPO6FV-h85DdxJQMOcYzxuRmadpDFSggt6fS1Zl7aOpiHNA5p_n_EBoNxuh8RHJTpFd9SqNTYe4hHpEeC4lVCIpPVRKLB6_Efoybh9cODSUaePk0UBtDjjZPScKz9SzM4ESwZK0dqKytfqBafB_wwseRrvXv760F7jrdnHQuuZRTpVzbruAsVbeM_AOHG1szSheBdZblb5ySW3LEvFIQUxQRFf_jI6aj4HhxAfrElnABCP24ATESufljKvM23Emn_ScJ_tlQSP89d9M2LbYP6iDhI9AOFvVr-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9pls2J2Z6ZEdImmQ4oBmmHMuTnPxqZDBjZB1xO89EwfsgP-OrFQhSj8rY3EzX4tDF6y1tHJyuFc1_gEpX12zQOc8SceaOO1z0T-RDJcxwinSLeKJTh9Byz5nHqcurpl2toHFjpJ1bi3HxBDqnVtDsyhKyeHxj312KK94dEFpKVjFWs4kQPEpxlZldNOZlu0RxqoUFmETM0fvvxBt4N8Rn2ZqIP25jG_JXBeEo3-ZP92Br46uQt6aDGk8jMxAf4OOGG8YzMMS3ZZhPM6UXuuV1AzDJt2jJeRA6amTdMts8wbLmesLXAfKDUR5Mr-IKDWiflRG-MY6ZVcjRfaE_27Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hoc6na_qhSQMHXURpNrqzvZQkVOPKf6rS3Dg_qhbAUidainWlfL59q3hlpl-vOw1bVE4hXY-x5bodR8hN5jM7-OsNN-C6qdZw_Mw6nwqbye_VMLlpAzP6eXZV-rVxuKec7vlcVvoejg9ervlpmsNAk6xE5jLvQ_DhC_VOLENVPnoBMTktiah9Qk8xJhVcv7WGE_86eKNloaJ931EDJ-iEL_G3R9_Xp1B05kaLSVrJ-OoOeu0sBHeUaUylQjyGPSWayLN8rCsPJIlshi8Kd_fK4tG_DlPaJLXc2mqrRr-kAZ4VWtVyRZiTRssMxkK7eYVjtWoAo43-ydmVZni3GwTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=q-VpXpiKggRZZTu5zKq6TNokXF0QfeXLtsuSYlhUCdXUoAUaDyMz1DUocDnQH4m-n_ut0g3Gl1L4ctDRGxavHaVR5RK1m37x1mZR4kKUmCZdrOhBtHl-elXi4fA6MOfCEAQ5MS1ppvGLyP4GLLsQUbaHNAOg699ctNGWOc9fmh6Obq1j1_XuQjGsXO-_7y6L3l9flGbPb_qoXWkALXdYPV4l5-73u4tJNNl1Q6rl8UINmKYtNfTFlrCYRAzMEk4fPwlEySml0NNOZ8mhM0G6UEGE-6SdVCvcp3PN-kXXFvP3nYw8JCwt8KmbHYtOjkjf9hn-bn8_8jlopp6sRvHQ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=q-VpXpiKggRZZTu5zKq6TNokXF0QfeXLtsuSYlhUCdXUoAUaDyMz1DUocDnQH4m-n_ut0g3Gl1L4ctDRGxavHaVR5RK1m37x1mZR4kKUmCZdrOhBtHl-elXi4fA6MOfCEAQ5MS1ppvGLyP4GLLsQUbaHNAOg699ctNGWOc9fmh6Obq1j1_XuQjGsXO-_7y6L3l9flGbPb_qoXWkALXdYPV4l5-73u4tJNNl1Q6rl8UINmKYtNfTFlrCYRAzMEk4fPwlEySml0NNOZ8mhM0G6UEGE-6SdVCvcp3PN-kXXFvP3nYw8JCwt8KmbHYtOjkjf9hn-bn8_8jlopp6sRvHQ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7KY8Kypdv06Gdr5Cd0SmXT-xjfF01S_IKHA7lCQ2b55tKGY2qzlkRyX3fFsY18DZMVu_6NGq_zRcfutyLYTLx_EHi5taoV30bhJ4cGxgzqLTKMRnkPiQqRou_v9tVgrS_kVvdxbPrCv36jh_patnwRQXUo7zAtW41vPAnyCDYanaR4wBeu7BbTegziCbwyqC9v1O6nhDWnaVTX0S58t9g0sJVczWKanTMVAgKoaPELj88v2JurCD0OngbCyaHJAVCjYpm7RnhwDcAZThqmIENd4aOwgj8O9XYg_VX5zAOhgIbec1VYdkrJ9FWbwLet6NNq2lk6xUQs6dcSDU2YjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E14sGUQyas46H8toaKevIMnPnG9gQ2r1nuzFkFOiJrVgKdIiG74la9EnQXi_XTBfOkRaMF1t-YH-7dTjXJu9z9JgqFwx6y-_hhrvakBfP9hCt3mfseoP61RTVxBjoVrKaccutJY96OBcUySoKh_L6-9DybhGAagAWf5Da3GD3H5oyUEIxCN1LIaU2D3piBddqdHsfLMoAIIdEBZpjQa4tBN72jwbgi0g-OPQVJkfzL1GCtjdFqQCQYBG3FhhZpZEDT0RgfpLVviqa02oFh8Ei4Me_6LEOddiR7HFHlmFg0WYLF2J_kpA4WISAbPuWWlXozfAQlWQ9m5VZJ57rTrb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjLGUwTJJnM9RBhqs6FH3PYcl3Lq2NUnc1u4BA0ofeOpv7BKYW9VYZAMyI22sDWxeQ7z70Hl5AdgsU6YNdd8n_2hdwdUHd3Z5t8aCGrtC2Z8lav9UBWRKQwZiK7mTg7coQGNwpICscn9JlBI4J0pMzNbfMaOfjhHdFq2TvG5yf7JGpP3NeGF51oQ7FQl2sycwfUWJD_vpxY9kcOS1mQc39TRQpeoIFouzolAtz6KwTKUHM3h07HLQSTt_EkjAJ8leOPuOGRYZNFzm4BTfZUJJjT5yXOESxHOAs8lNyL-kVnvS8F_dX-FBm-LHOSOzE7ViAKK1gy8G5gv0_QBJLcuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjx6RxSrlxUzJ-hLqrr6-8B-L6PhSF-9vy-yVkctm9Vbamm1G9Q36Ho839zj67ZyOOZx5fXo_41q1n3kZp55TaX5dJXk6So6BS3l1UG3a_G-YS4GMVQycbySgCRwH2ghFxOhzqcoVXne_ALlwGZzy_hWj2yKYHicctJAjex9z18hjl_MF36ixAeFzybeo9dKwn7YAlM_4c7yODlirQIgZSCC20Z40AisFQstVszyFucdis4WdGWFbPtjP3h-l3--9zNW99kyvqnUo2CpwVI9zIpeGOyr7y4A1g2bGCCPgy4vaVIW4vNBKRUaTYmkQ0CERMIh_aIDPNfn30FWjqC67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Thxg9hREmBtW7AsrDxksiX-Xvzv7-VJxuIb7Jc4HGSFYHGfO1jDEgCabNnrjblejghZAlCn9T4CRgVCThHBON40sZYGciUnIYV_2JhQwdq1ZszYCWVMRw_t1W9eHRgbZM-4nkH2pcuRCYivR4cD3Z7XANKY6P-UCMxgTMI3P3NK2PWWLGrJgcCJCWOnplJ65iblFqW-F-h2Ju_qPHAqDu5GwWpT_ythIbiYc0DyVToILsU3lIE24sAvCj-fgxaI20vGdmZDMYnfA4OygFDcb0cFADCI9uLxrP_8SCNxaExP5trWoesSRdalU5Z3IJyJJg_STorhP3B6i26u90HtfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLdBVtFEVVsuqoaUcKq_t6iBoUaIz2G1M9pzJQgmR2UyHPEa3TxmY4A_GgD9oTxdQqf6OdQ_IfIKql2niydUL0Ms3PnpQ7vRnq7ya0AnPMmMgJL23gOMm3fcwDB7fkR7Ugm9LA159oFGCHNEKHL_AhoYCOYewNo5rKfKxhdX0CENlemwdgixkIZ7lxjor7qGOggXOCHNUjodShb0xxZkXEdEkzCYmYoJxrSevJtADKfGvw_uXxKVURRqSzmbFzlG07shyxmrZLC6U-uQuSoj7PL6OpTqj1T2kaT8kTvY88MZgktY-qlnyT-n8555fqtG8L9tAegSNCUKQYv7f5iSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukqlpbqb4WLl8Mzppj_m3Q5SWpyR9_7dOl64My8aJpW5iszRosTMrQgO4uUR-Q-MVUDKnGkkCF5zfxkROVbMQ1jSOed4-dKxezu7zfu11I2-TGJtn_zdjGcCzfuMCQqUKk1MtMRuB5KCv7DJuy1E9B-sP8Wvgz1t38XW7mmTCSBgjeEiA-MPclSgdNMg9Sva2dOheKwenXbHf42Qbh3Aq46oA_HHeJkWoUBqIDqX5MQs04G1xULfp33m9-_6uNr4RuQUbW7xwlsXjSFT1HcX_R4XCUbhjF4C8csY6sBr51ySqKw7AyCoFpEWlLWvC-VUFm9g04uslgUtkA-pXODMLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMNmMUBfXI37qhRRtBXxNe3_0u5lk0KJOjvLJ84BxqwULgX3jYF--MuGv-LmBnCYPto1zedJV-npbAM2yxKbb-VtFhCpGU_7c6DmspQ8U66kGiftdSlILpzml-BqE3GUfS1XTpWogsPC6a8kcV8DXa2jg40Exi61REv5W3C6TlanEDy7XMGTTua4zggOZqhk3j8Dwe1GAEMMK7Z0DEwNd_V-aUhD-evUMYDvlaaL9eMQ2zWtbtSTEcByttjxC7Fk5MhmtED775VPYXyiNtRagjzKKFIBCDAOym_AXHxM4kklb2jG66mLTAlU2UixdUNUKM0XE2_saz23nmp6JPJTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_uhxUNJsth01uXcgdIQDjheAlUmgk1I6VT3ppx-N0x-g2B71Mf1rkAhiFfSbV34m09aPD7isBzptpV8yYLfM17_m-3D2D1vIcA71UALShBlCZvr8ftdt9JXXVktXmUCsiqic8VgVP0oB-joXHuUg-EfKG2fNhf6sp9lb1FlRtg3HIJgam1Hdg_FyCvNjyMFtHBtPWsNllBfxcevuTt7OWVhJZuaQlShsWiqpr-S2S6WvofgJAhGBobcEcSrlkbCXbjic9zBQVgCOpQKm9xMO6vgh79DD_GLzNpHhEv1-zrV8dcSQsFmiYGi7xWpDzBwFFr_2BheLo-KhqcDF2vUig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om1gRJ6h8z3ovhmo5F7v1iabRJ4HRwWmxVn2C1WS-n4q_6zPXm0dTecDeOfLI-BhyL46HO5AOpcYMxYDQzpZpCTvyeS3-GAu6Wxr-VfI1HX3TgT-ls_eqP-RyQeIjfxXYOM7msPjW4gp9bPw6dcG2g8vhCPqTy6QVIOHsYBUUau8S8qbOBbDNfSeFxNJ6RSBN_I0o4j4pyPmlemYmieJ6o-3Zf2vo-TgWSrp0Wa1qzeEGJmBDKN9-wTP_Hxd1AyLtXsr7e5yP0HYH3ccOIdKQFT8EkV1dHSMFr3b1wHaaX1tHegaPZ5UW8Vg11QKi6Ye7FTH54izTodVnf1e_QkAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRzZowdkKBn1EreMTpzXQqE30HO8l4T-9pzuvKrhLpcTmLhE5Ez-qAq_LNOXWXh71xknz74j1Z5JpOImmY-cRfWdLh2K40E7yYMXS3tzcJ-MalJii9M1Ml7cGIFc1peoyk3GdrsKTnzMfTB6FeijP6-y_BjRSaZ3QYVZWWrHEGjA9r3beZs9458puyGt0L48HB5Wy4ZB_kLvOeTEj-Z2VL1Wma9oVOE4jPT4-piHdeILGd1KtiWyQ2rN0y6_8cCmcP7utjOP04SN3Ci31aJF3a_hQlfc2_-nrsFyqchJdGdJlrIsYwSl8Ob3BBm_aH5Z865zJ59Fzcn5Lww01K_wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=tmUr8sTdxul0seN5xF7rzCAADtFPP3CAe47hdwchx2qNo00MKcUHvjBOOJmp8XI7aWssN7adT4xm5miVpCGpFO0vs5TF8vg6IQr_E20G6hSMKaztS9Np30pA0tlTqhyDkm0TqXj_Y2oSa2eW9UW6iXRDX6h-0Hy3tzYvNbHGy41dfRKu44SXXcDaMXPGWeIX2ZUOt_BAkgwRwaO-6Yg4urIF5MrB3CjV-xHIgK4hIsrZgoxavnJbW02v4nWG0aHz-mU5H2p3jxRMkDMon57-V-cx3RL-HoJPkqBEtk0pNNGlO4FaZNF49Mot-vkbdJU_h-u_bndpMAp6SjvrQrX5cze3DUlPApPpBcv7b8Nr8hAYm4UUL4_33OE-teX3D4rQC-1AKxUqdVspXD5tzeRXM0exnlN_OQ8aGg4e2Qy7sNqCAzoOg5qo_qMvRzXU8ZhGkoei2eMfVZynX6xGD7CvtHJ_b5S2uAsHhHUzxn0Pn06pJ3tGrmp8f_jK7I9p4XNDEyYaTeyCEa0T4uSM6PTsk0974peum-dXjNiAsYsfNwg-EBGNuarRBrhVMZqivq6ig7AYVtmZAqh8jI83R1Mvuts2bq9y78uh-xCFzAwc2ILd76OQAGD-ODNXIK4nzZJ9lX6bnfvqOyFckJTDZbbPlHf0a_7AtLsiyLstmU0UEZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=tmUr8sTdxul0seN5xF7rzCAADtFPP3CAe47hdwchx2qNo00MKcUHvjBOOJmp8XI7aWssN7adT4xm5miVpCGpFO0vs5TF8vg6IQr_E20G6hSMKaztS9Np30pA0tlTqhyDkm0TqXj_Y2oSa2eW9UW6iXRDX6h-0Hy3tzYvNbHGy41dfRKu44SXXcDaMXPGWeIX2ZUOt_BAkgwRwaO-6Yg4urIF5MrB3CjV-xHIgK4hIsrZgoxavnJbW02v4nWG0aHz-mU5H2p3jxRMkDMon57-V-cx3RL-HoJPkqBEtk0pNNGlO4FaZNF49Mot-vkbdJU_h-u_bndpMAp6SjvrQrX5cze3DUlPApPpBcv7b8Nr8hAYm4UUL4_33OE-teX3D4rQC-1AKxUqdVspXD5tzeRXM0exnlN_OQ8aGg4e2Qy7sNqCAzoOg5qo_qMvRzXU8ZhGkoei2eMfVZynX6xGD7CvtHJ_b5S2uAsHhHUzxn0Pn06pJ3tGrmp8f_jK7I9p4XNDEyYaTeyCEa0T4uSM6PTsk0974peum-dXjNiAsYsfNwg-EBGNuarRBrhVMZqivq6ig7AYVtmZAqh8jI83R1Mvuts2bq9y78uh-xCFzAwc2ILd76OQAGD-ODNXIK4nzZJ9lX6bnfvqOyFckJTDZbbPlHf0a_7AtLsiyLstmU0UEZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=ADIxXGRExW0VZ9sw6pqTMaW_KdfUvKglBjdOzh6DfyY4rG8SVh50yim5VqhzVlN5Hjkn6lj9dPeqoGMvBXpTcWa8MLIwOYAHUZPqBVVGzcwqufphzeCcn-DUOyt1yKsSyNRp8J5OIlG4JblcKTEi7_FNCirPgB0l_KJfAJkOnm9H6Cy8yBHibVqRJVy3PyuFVfwszZNO--ylBhdtQoucJvioOo6JPoHnfDCZ3GTub08bFoGr9qPt4bu0BwuCB1ejH8BlQjt-aSyxGN3ZQUi8B0hiii_968FTUXIarjAfygU-UD-D0HwlQ-FfGJZKWBQErDpt4Ac42zo2_M-D_DAu0VoMeL26kp6izzD7byYwDV4iuZEMd3O4VgK-Vs5GyBBGBoO4KQHi0ZdV7n7Tbq4bKhniw9TlTMtV-13gptDH09vrs0P7_CedRRPSTMXaea283v_ES5C1Ci1YEGZ_ggTtDYg3xCf-PTZ69TUDzLNrLp9HxLVhXOipmf8-bggOZWAWCxoJ5u8Kt3b9XfcbUlyBR0oqxRSIE8QmH1SM_BxTK8Xmm6m6qaSDpndtRyDn6lt9tWb6TLWUM3uw3Vg6WKqDuCf9FTwc4Hjx7N0ahPCvcKmoWRbLiS5O-FI17ISgLbwKndFkXq735kf1d1yskUUaghePQoFiKYxG9YaZpQS0xgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=ADIxXGRExW0VZ9sw6pqTMaW_KdfUvKglBjdOzh6DfyY4rG8SVh50yim5VqhzVlN5Hjkn6lj9dPeqoGMvBXpTcWa8MLIwOYAHUZPqBVVGzcwqufphzeCcn-DUOyt1yKsSyNRp8J5OIlG4JblcKTEi7_FNCirPgB0l_KJfAJkOnm9H6Cy8yBHibVqRJVy3PyuFVfwszZNO--ylBhdtQoucJvioOo6JPoHnfDCZ3GTub08bFoGr9qPt4bu0BwuCB1ejH8BlQjt-aSyxGN3ZQUi8B0hiii_968FTUXIarjAfygU-UD-D0HwlQ-FfGJZKWBQErDpt4Ac42zo2_M-D_DAu0VoMeL26kp6izzD7byYwDV4iuZEMd3O4VgK-Vs5GyBBGBoO4KQHi0ZdV7n7Tbq4bKhniw9TlTMtV-13gptDH09vrs0P7_CedRRPSTMXaea283v_ES5C1Ci1YEGZ_ggTtDYg3xCf-PTZ69TUDzLNrLp9HxLVhXOipmf8-bggOZWAWCxoJ5u8Kt3b9XfcbUlyBR0oqxRSIE8QmH1SM_BxTK8Xmm6m6qaSDpndtRyDn6lt9tWb6TLWUM3uw3Vg6WKqDuCf9FTwc4Hjx7N0ahPCvcKmoWRbLiS5O-FI17ISgLbwKndFkXq735kf1d1yskUUaghePQoFiKYxG9YaZpQS0xgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e20W1t21ESYWl_-0stb3pMdLvLeOjg2eWmDKf05tAdWIHaer_j5V6jaDywdWgkGL4yiiuy8n8i24eWkVVNxHJR11n4lo9P3nVfMe71OdpgCE6lJzYYcKsSbJjr0AyD3db0MIz7mZnofiuTfU5hgXA4AO8_hTeKa54fQ61Br5NWC-nQXwN2iWQIkZ229f6Kqck6-brguVEGAjag5oxN4YGNVkRuaBH-L0w-u_lcak3r6x-SA3J_UBipL8Lp0L_9ah2boxd8qUDEUmHhQeNz6vA5AvVI-X_Q24jkZCUmRx-0z4mMMEQmOup2t3YOm20obB8o0yWAb0gCxAnaiXi0hpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=lXRIp98iJLdkXeXlKgugF4ZPv70hkj3GeUeKp8NynCvjgsalgdEzmtos7MqdAOBukf6ihY3Nqc7vWVG5cvx_ToRvOidCkLVj9YjLJYVkQ-ELncuFCD3SwynN3WZusIhkA9fHMBoTvxB71m2SceWTLOU3msVxccZDue8OXSACqV5aXNflvhcTwXlJPIe0KQctW4RIDHGybYrSrk1rCuWORAhvzPqFgt-XNqhRSGoIWsUUjEpwlbK46z1-f68zFrbAVuT4YaXX3KK2zLTZrkVwNzsE0NAw1_QZgW1hMvVs-eVLC4tocfdhaAExGu2Tf_XZnGHgrJbKdCnQFFJdKFqetQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=lXRIp98iJLdkXeXlKgugF4ZPv70hkj3GeUeKp8NynCvjgsalgdEzmtos7MqdAOBukf6ihY3Nqc7vWVG5cvx_ToRvOidCkLVj9YjLJYVkQ-ELncuFCD3SwynN3WZusIhkA9fHMBoTvxB71m2SceWTLOU3msVxccZDue8OXSACqV5aXNflvhcTwXlJPIe0KQctW4RIDHGybYrSrk1rCuWORAhvzPqFgt-XNqhRSGoIWsUUjEpwlbK46z1-f68zFrbAVuT4YaXX3KK2zLTZrkVwNzsE0NAw1_QZgW1hMvVs-eVLC4tocfdhaAExGu2Tf_XZnGHgrJbKdCnQFFJdKFqetQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W00jUEkwUvjW5VYih1NTcNVP8DS_TOWBudnWMMhHn14IV1rGSd0feZLptzABpkBy1ItF2b28Sc08yY1w36GHMxiGis9blFVJlWx9Q6dUt78Yzqecglm-szLh5KE_ExKWvQyJpXksnhVH7eII4S6q6kK62-H9sKgQg3RCsaQHQHgWJscssGXF1ZRs41YT0ba17YS5lAVECKAiLZacTLoX8kReC1nd3tWvzngmfwOKv0Y94WYFhWPA4Jm2ZK0b9YRdcT9RFID7xHcKGkDl_yjC3BS7McX241L_J75fE_tDxzr5cyMoOUb5pKVVEXyXDJjeM4CnDhx78URbpNZfVbIMhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4GrqDx529r2Ct-w5NGjpl6KaEo44jyDKgkLPLeNYM9IYtOUba-hVCEcTTCV7jdxMZ5dxHhFg-uzWZFd4RqZ5RCYlidXIIMkthp2FwP4xPBvkNGwwun4EBwyBHKxNpzgLNdXhzYAS5PnNSXIL6rdNNCQuQzIiit3XkheNWLAl-tZiOmBBsGRcI57Q7fZy7IOz5oEmS-QPjc2jcOdbN0zd6yQ3jqHeHQ5MIHphkpVwoTJ9XdUTcauLv0xtpEZSbMVsYBnF-CyGNawxdr2fYVR53mzuZj7T3KhxcCTl2-18ER45tP4gSiuZs7Lz0JlB_kjxAqhaUW_gej4RCOSdFepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI7HarUrNfcidFqe02rfVUz_FNttFE28X542aMKjOicjC14jBRBoSxqx72mZAnay-LJaYSFtxuq8bQVjsdWU3cDQg65zp94CWceBIXzn0QYMZ7e2C8NKnoxVmseZyyYSokWFZF5BeqkezsfBio0JBQVb7Pr20whozZpyqzcdScOYJSjNK2kS5-DQK-QzY4mOa5XpPkoqYA7Ps-SlJEEDaNVTVm8em8wvLdOHgE7IGwwRm4P8YH3lIje61GkgAwiz3XkJRh8wQTuzOQbrjZlJ-6BSYPfcqLFovDgUmYPgLA-NWZdzVXUclFDmeFsQ_DXUZ6_AG8yqIls_g0-5bLeG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnaZecuy1ETUkbZqPKy_3eJqeZzlrhOnox0D2cSz1AmHCZOf156F2lyi3fD63E1gHVZGwlEr9XXUTQCBxlx_a5UNr-XxEhNNovxRTBUzwVj2Ey6R5NihTQbj2fiQsrtUk1Mo4hgrrPO7BxTCcIGvIqc98Vz-jCbTh-IS0FloEA2o-QDBsnzmr7dJTHbdLpw6Z5DOpVZqczyUhRj0BWW1iwO27bK_c2Zpx1cmv9OE9N3keSkIesbPFVeuBcruZsLnIDMahDm6-SnkdOujyLxxKTm7Ryj5XLuJ1dHG5lmeNPjNRtKKIoKcG3wxRCYQ_ChT74A4tkBR7eLNBZfxXtlJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=OrmQ6H3JssX6D3ShGV4awqhxY6M94V8QAA7vuSV1hn0quL5geJ-lDspcWsBLHpxJZl8AJFpJHx-kuNjadUoH5hw1IDvKU9VUAVkeqsCUfysrqkGxx0ug1P5KuNIu1sv0OmKTlIa6GT-55hmIA5zcYGGAUoTGL1CTQSOiRN5kHYRCJXFpXTVxAVlgxdtIE1He07Izecx-CJf6ObzAWkmThLM2Y29FJ6_CueRdBxmP7ndBZGfplVnEZFDQ19x3WytqbThvksnhd0t5l1wFYxdq8OBYcDvHeU332j32hig9jdk88Q_EZYRHaF0aNDGlBX125H8UTR2Dw4Uf7ceNz85Xp0nPvggtyRIaZ0_nTf9dTFGOycXXTF7t6qXPkMNaIjM3dwS5rzsc7vPctQcf0_9C5N9KqKAJnqUtwwjVRIBZQAxGn3yOWMFSCtz1gQIIcP4NKqCozvsCtbLNY2ISbAYOkzdaOXLCJ7cvlCkhTjvcP6R5gb1yPR8P825I7XuOy8MUCTxCKMwwj8dCyU6i3P8iHUOqNv5npbl1aeSeXwpZKsxp1WBtBKCQtFE5r_NdGfvIW5UNeP64WHlXYGW3DvCGfbw6wzNfhUW-1KgHYTqAhYwzs2uQLIOz6zjCpF1czpzxO1My4860JNx6MYOjG3F347jG3cRGnqiDEpTUM3J3Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX3OSkCfk2t2h9NBtjmwjCYM_YUE1KEdH2WX3GB5E0PMbpkJjPDY_ntHsPTdBCbL0kondH1gKVZkeYQBc8pkC_A5wPsCKhjrlkDngDdA7jHo0KhKadfSWzpremONv7IcJ8d7Nf4I5dR91NxLZb-wl1ndFcQlLK58pG3AnyrO65R3Ki7a1yWcmqtpQi-kL0vyYngJgB1dXWlO6IKeg-a5z8QEA6eROBBXBPGQrwlezd8NceBQPTlxLxZUTNGfAHr182LrVZyZhTur9s59Y3vb-RqAr8-Dp5x_ozxCG1NQ8boWDBbtZmETh-JyyZLQ1P0CFENZE4LlreiJkLfRLuAiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJLZiX8KxUpLcNdY_Xk7B4oSI_9EKq9Fm5XfBdhmu1kBhAv6K8AjjjfTuvW1QyCxVrtVCh2sL4Xxw5ya1xAw4Er4xRSGUsuQv8hFlsJqTNrf0_rqoPajhOe0IItWdqYo4194nd4diZYu9a-V13sznmBsrSCLuEwrAmXUZbUagCzLuNBhHx3AgV3Nr4848Q0JTW3FnfAWZtCMVW7YsVBPHDZFNpwQtpHNRRn_B-RJ_yzf1Bscj7lUfS1ClciVxXbPQIUHq6XADS9tar5DeKH7LubteK1IGWqEh-tfI06B1xGcVKquHU_LTCavoAUMUvKsvCvGmb0RuDJNN6U4TbFkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFZiAHhbWltALiqpxbb5pf5hxVEs1L_4m9Ba9W3gU_S1-3vJlGLXOFAFiCaTyF6a2SG1fZ1gs5tyxhqZx2Z0kdo0In6ETOvswqxFQKmpl-PZRBRPS6LKRdiVT_rsnA6PmgBI_OC4OV3T5CAMGgUbfegpszzzf-kVN7SGfXOG2sWO93Vo_G2cZXk8QuU5LsVsvkTQOa8w0M9AQFQbX9Vwyk7gH-4Xjh7t002TH6vE41hwPRkw-0TZrJxbJtAoDEtCYurqpsdpy0gQwf7G6mBeQhIG8egMYnzTvSwdLvY1mRHQVgiSvbWN1vxFiYEyRWsFeq4hJkNK8F6ykNsg094oCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx-jcijPAyLRaoggVqT5--rCP96HeK-NhnCu9o3F03bHKcC0yY4KHqpp-a7w0fIjKE-owyyTJ9z2Qgrufna72b88qb6rHsT6rMMH72YeDI8YEZ9MJozjztGW_9ZGGiKx72Ja5wusRCikfWt0NjLHFDOOPgM0tAAxOvDXzUv7MpD_eDkO9c4XhS9bBsV2NZDiVUfMN7g4FlDwe8R0vVfKVAHlQdxB0iJjU7xa6CROXAcIBMCQUgvzgDkEpYHgDV7inVyJVyQXJCf1qN1sgo0QsQiFzLkmHt49RShIYhWj5UxQoVOBSYtU-S9OFwVpqG61LSquJ64oJ7N-g7t1l5ggIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
